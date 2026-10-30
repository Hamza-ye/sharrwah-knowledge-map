"""Select what the final review of the class's model's extent reads, by risk (PLAN.md, Stage 4A; the method report,
sections 7 and 13; the brief `studies/class-model/briefs/R-extent.md`).

    python3 -I method/review_select.py [--sample 0.05] [--seed 20261030]

Reads the merged files (run method/class_merge.py first) and the parts, and writes
studies/class-model/review/selection.tsv: one row per item to review, with why it was chosen and the reviewer's share.
An item is chosen where an error would change what the model says:
- kind: a cell its capability's kind hinges on: the one cell that makes a class whose count is 1; every cell of a slot
  or an open, since a missed core would change the kind;
- role: a landing joined on role, a reading;
- own-service: a cell placed as the platform company's own service, which rests on maker evidence;
- flag: each question the merge leaves for the review (a statement counted twice, a pair ruled differently, two
  capabilities that may be one, a fit that may be strained);
- coordinator: every row the coordinator wrote or changed, so that someone who made none of it checks it;
- sample: a seeded sample of the other cells.
"""
import argparse, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows

MERGED = os.path.join(MODEL, "merged")
OUT = os.path.join(MODEL, "review", "selection.tsv")
SHARES = {"A": "1", "B": "1", "C": "2", "D": "3", "E": "4", "F": "4", "G": "4"}
OWN = {"core", "own-service"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=float, default=0.05)
    ap.add_argument("--seed", type=int, default=20261030)
    a = ap.parse_args()
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(MERGED, "cells.tsv"))}
    dom = {c: r["domain"] for c, r in caps.items()}
    items, chosen = [], set()

    def add(kind, cap, plat, detail):
        items.append([kind, cap, plat, detail, SHARES.get(dom.get(cap, "?"), "4")])
        if plat:
            chosen.add((cap, plat))

    for c, k in kinds.items():
        kind = k["kind"]
        placed = {p: set((cells.get((c, p)) or {}).get("placed_as", "").split(";")) - {""} for p in PLATFORMS}
        if kind == "class" and int(k["count"] or 0) == 1:
            for p in PLATFORMS:
                if placed[p] & OWN:
                    add("kind", c, p, "the one cell that makes this capability a class")
        elif kind != "class":
            for p in PLATFORMS:
                if (c, p) in cells:
                    add("kind", c, p, f"a cell of a {kind}: a missed core would change the kind")
    for r in rows(os.path.join(MERGED, "landings.tsv")):
        if r["join"] == "role":
            add("role", r["cap_id"], r["platform"], f"{r['concern_id']} joined on role")
    for (c, p), r in cells.items():
        if "own-service" in r.get("placed_as", ""):
            add("own-service", c, p, "placed as the platform company's own service, on maker evidence")
    for r in rows(os.path.join(MERGED, "flags.tsv")):
        cs = sorted(set(re.findall(r"CM-[A-Z0-9]{3}-\d{3}", r["flag"])))
        add("flag", cs[0] if cs else "", "", f"{r['kind']}: {r['flag']}")
    base = os.path.join(MODEL, "parts")
    for d in sorted(os.listdir(base)):
        for f in ("evidence.tsv", "landings.tsv", "cells.tsv", "capabilities.tsv"):
            for r in rows(os.path.join(base, d, f)):
                text = " ".join(r.values())
                if "(the coordinator" in text or "the coordinator, " in text:
                    cap = r.get("cap_id", "")
                    add("coordinator", cap, r.get("platform", ""), f"{d}/{f}: {r.get('concern_id') or r.get('key') or cap}")
    rest = sorted(k for k in cells if k not in chosen)
    rnd = random.Random(a.seed)
    for c, p in rnd.sample(rest, max(1, round(len(rest) * a.sample))) if rest else []:
        add("sample", c, p, "a seeded sample of the other cells")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("item\tkind\tcap_id\tplatform\tdetail\tshare\n")
        for i, it in enumerate(items, 1):
            f.write("\t".join([f"R-{i:04d}"] + [" ".join(str(x).split()) for x in it]) + "\n")
    by = {}
    for it in items:
        by.setdefault((it[4], it[0]), 0)
        by[(it[4], it[0])] += 1
    print(f"{os.path.relpath(OUT, os.path.dirname(MODEL))}: {len(items)} items from {len(cells)} cells")
    for s in sorted({x[0] for x in by}):
        print(f"  share {s}: " + ", ".join(f"{k} {n}" for (ss, k), n in sorted(by.items()) if ss == s))


if __name__ == "__main__":
    main()
