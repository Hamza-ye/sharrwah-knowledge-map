"""Select what the final review of the class's model's extent reads, by risk, and check what the reviewers write
(PLAN.md, Stage 4A; the method report, sections 7 and 13; the brief `studies/class-model/briefs/R-extent.md`;
the inspection `studies/class-model/inspection-Q3R.md`, part 2).

    python3 -I method/review_select.py [--sample 0.05] [--seed 20261030] [--batch-size 30]
    python3 -I method/review_select.py check --share N --batch B

Run it once, after the last merge (Q3's amendments included), and commit the selection: its commit is the one the
reviewers' messages name. It writes studies/class-model/review/selection.tsv, one row per item. An item is a cell
(a capability on one platform) with every reason it was chosen, or a question that isn't one cell. Reasons:
- kind: a cell its capability's kind hinges on (the one cell of a class whose count is 1; every cell of a slot or open);
- count: a cell of a class held with statements but placed neither core nor own-service, which would change the count;
- none-held: a cell with nothing held where the platform's own statements hold two or more of the other platforms'
  terms for it, the leads a false none-held leaves;
- role: a landing joined on role, a reading; terms-homonym: a landing joined on a term Q1 lists as a homonym;
- own-service: a placement as the platform company's own service, on maker evidence;
- scope: a class that holds only under a plan, a beta or an observed store (its class_scope isn't general);
- strained: a capability with landings marked strained, one item per capability: should a concern be split out?;
- flag: each question the merge leaves (counted twice with a cell resting on the statement alone, ruled differently,
  one capability?, strained?), and one item for the counted-twice flags where no cell rests on the statement alone;
- coordinator: every row the coordinator wrote or changed, in any of the parts' files or scope.tsv, and every line of
  the parts' notes that names the coordinator, which also shows what was taken out;
- lead: every line of a part's notes that names the final review or the reviewer; a capability whose cells cite only
  inventory entries;
- q3: every candidate miss and unclear row of Q3's check, every beyond-the-class row the model doesn't answer, and a
  seeded tenth of its covered rows;
- sample: a seeded sample of each part's other cells, at least two or the fraction given, whichever is larger.
"""
import argparse, glob, math, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows, fold, items, key, hits

MERGED = os.path.join(MODEL, "merged")
REVIEW = os.path.join(MODEL, "review")
OUT = os.path.join(REVIEW, "selection.tsv")
SHARES = {"A": "1", "B": "1", "C": "2", "D": "3", "E": "4", "F": "4", "G": "4"}
OWN = {"core", "own-service"}
THIRD = {"extension-point", "outside"}
HOMONYMS = ["supported countries", "complaint", "log", "rate limit", "mcp", "ucp", "order limit"]
MARK = re.compile(r"\(the coordinator|the coordinator, ")
HEAD_COV = ["item", "verdict", "severity", "basis", "correction", "what_would_settle_it"]


def seed_domains():
    return {r["area_id"]: r["domain"].split(" ")[0] for r in rows(os.path.join(MODEL, "seed", "km-areas.tsv"))}


def share_of(cap, part=None, areas=None):
    if part:
        return SHARES.get(part.split("-")[0], "4")
    m = re.match(r"CM-([A-Z0-9]{3})-", cap or "")
    return SHARES.get((areas or {}).get(m.group(1), "") if m else "", "4")


def select(a):
    areas = seed_domains()
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(MERGED, "cells.tsv"))}
    ev = rows(os.path.join(MERGED, "evidence.tsv"))
    cell_items, other = {}, []

    def add_cell(cap, plat, reason, detail, part=None):
        k = (cap, plat)
        it = cell_items.setdefault(k, {"reasons": [], "details": [], "part": part or (cells.get(k) or {}).get("part", "")})
        if reason not in it["reasons"]:
            it["reasons"].append(reason)
        if detail and detail not in it["details"]:
            it["details"].append(detail)

    def add_other(reason, cap, detail, part=None):
        other.append({"reasons": [reason], "cap": cap, "plat": "", "details": [detail], "part": part or ""})

    placed = {k: set((r.get("placed_as") or "").split(";")) - {""} for k, r in cells.items()}
    for c, k in kinds.items():
        kind = k["kind"]
        if kind == "class" and int(k["count"] or 0) == 1:
            for p in PLATFORMS:
                if placed.get((c, p), set()) & OWN:
                    add_cell(c, p, "kind", "the one cell that makes this capability a class; is it another capability's thing, in any domain? (caps)")
        elif kind != "class":
            for p in PLATFORMS:
                if (c, p) in cells:
                    add_cell(c, p, "kind", f"a cell of a {kind}: a missed core would change the kind")
        if kind == "class" and (k.get("class_scope") or "general") != "general":
            add_other("scope", c, f"a class that holds only under: {k.get('class_scope')}")
    for (c, p), r in cells.items():
        if kinds.get(c, {}).get("kind") == "class" and r["held"] == "statements" and not (placed[(c, p)] & OWN):
            add_cell(c, p, "count", "held, but placed neither core nor own-service: does the platform do it itself after all?")
        if "own-service" in placed[(c, p)]:
            add_cell(c, p, "own-service", "placed as the company's own service: does a statement name the company?")
    # none-held cells whose platform holds two or more of the other platforms' terms
    terms_of = {}
    for (c, p), r in cells.items():
        for t in (r.get("terms") or "").split(";"):
            t = fold(t.strip())
            if len(t) > 2:
                terms_of.setdefault(c, {}).setdefault(p, set()).add(t)
    hay = {p: [fold(s["identifier"] + " " + s["statement"]) for s in items(p)] for p in PLATFORMS}
    for (c, p), r in cells.items():
        if r["held"] != "none-held":
            continue
        ts = set().union(*[v for q, v in terms_of.get(c, {}).items() if q != p] or [set()])
        if len(ts) < 2:
            continue
        best = max((sum(1 for t in ts if hits(t, h)) for h in hay[p]), default=0)
        if best >= 2:
            add_cell(c, p, "none-held", f"nothing held, while one of its statements holds {best} of the other platforms' terms: read candidates")
    for r in rows(os.path.join(MERGED, "landings.tsv")):
        if r["join"] == "role":
            add_cell(r["cap_id"], r["platform"], "role", f"{r['concern_id']} joined on role")
        elif r["join"] == "terms":
            text = fold(r["join_evidence"] + " " + r["reading"])
            hit = [h for h in HOMONYMS if hits(h, text)]
            if hit:
                add_cell(r["cap_id"], r["platform"], "terms-homonym", f"{r['concern_id']} joined on a term Q1 lists as a homonym ({', '.join(hit)})")
    strained = {}
    for r in rows(os.path.join(MERGED, "landings.tsv")):
        if r["fit"] == "strained":
            strained.setdefault(r["cap_id"], []).append(r["concern_id"])
    for c, cs in sorted(strained.items()):
        add_other("strained", c, f"strained landings: {', '.join(cs)}: should a concern be split out, and where?")
    loose = 0
    for r in rows(os.path.join(MERGED, "flags.tsv")):
        cs = sorted(set(re.findall(r"CM-[A-Z0-9]{3}-\d{3}", r["flag"])))
        if r["kind"] == "counted twice" and "rests on it alone" not in r["flag"]:
            loose += 1; continue
        add_other("flag", cs[0] if cs else "", f"{r['kind']}: {r['flag']}")
    if loose:
        add_other("flag", "", f"counted twice: {loose} statements that support core or own-service in two domains with no cell resting on them alone (merged/flags.tsv): settle them together by the brief's rule")
    inv_only = {}
    for r in ev:
        inv_only.setdefault(r["cap_id"], set()).add("inv" if re.match(r"^[A-Z]{2}-I-\d{4}$", r["key"]) else "stmt")
    for c, s in inv_only.items():
        if s == {"inv"}:
            add_other("lead", c, "every cell cites inventory entries only: a capability, or does it fold into its parent?")
    base = os.path.join(MODEL, "parts")
    for d in sorted(os.listdir(base)):
        for f in ("evidence.tsv", "landings.tsv", "cells.tsv", "capabilities.tsv", "rulings.tsv", "qualities.tsv", "slot-fillers.tsv"):
            for r in rows(os.path.join(base, d, f)):
                if MARK.search(" ".join(r.values())):
                    cap, plat = r.get("cap_id", ""), r.get("platform", "")
                    what = r.get("concern_id") or r.get("key") or r.get("candidate_id") or cap
                    if cap and plat and (cap, plat) in cells:
                        add_cell(cap, plat, "coordinator", f"{d}/{f}: {what}", part=d)
                    else:
                        add_other("coordinator", cap, f"{d}/{f}: {what}", part=d)
        notes = os.path.join(base, d, "notes.md")
        if os.path.exists(notes):
            for i, l in enumerate(open(notes, encoding="utf-8").read().split("\n"), 1):
                low = l.lower()
                if "the coordinator" in low and l.lstrip().startswith(("-", "*", "|")):
                    add_other("coordinator", (re.findall(r"CM-[A-Z0-9]{3}-\d{3}", l) or [""])[0], f"{d}/notes.md line {i}: {' '.join(l.split())[:200]}", part=d)
                elif ("final review" in low or "the reviewer" in low) and l.lstrip().startswith(("-", "*")):
                    add_other("lead", (re.findall(r"CM-[A-Z0-9]{3}-\d{3}", l) or [""])[0], f"{d}/notes.md line {i}: {' '.join(l.split())[:200]}", part=d)
    for r in rows(os.path.join(MODEL, "scope.tsv")):
        if MARK.search(r.get("reason", "")):
            add_other("coordinator", "", f"scope.tsv: {r['concern_id']}: domain {r['domain']}, also {r['also'] or '-'}")
    rnd = random.Random(a.seed)
    q3 = []
    for path in sorted(glob.glob(os.path.join(MODEL, "q3", "check-*.tsv"))):
        q3 += rows(path)
    covered = [r for r in q3 if r["result"] == "covered"]
    for r in q3:
        who = r["who_answers"]
        if r["result"].startswith("candidate miss") or r["result"] == "unclear" or (r["result"] == "beyond the class" and "model" not in who) \
                or r.get("rest", "").startswith("candidate miss"):
            add_other("q3", (r["cap_ids"].split(";") or [""])[0], f"Q3's {r['set']}:{r['row_id']}: {r['result']}")
    for r in rnd.sample(covered, max(1, round(len(covered) * 0.1))) if covered else []:
        add_other("q3", (r["cap_ids"].split(";") or [""])[0], f"Q3's {r['set']}:{r['row_id']}: covered (a seeded tenth)")
    by_part = {}
    for k, r in cells.items():
        if k not in cell_items:
            by_part.setdefault(r.get("part", ""), []).append(k)
    for part, ks in sorted(by_part.items()):
        for k in rnd.sample(sorted(ks), min(len(ks), max(2, math.ceil(len(ks) * a.sample)))):
            add_cell(k[0], k[1], "sample", f"a seeded sample of {part}'s other cells")
    out = []
    for (c, p), it in sorted(cell_items.items()):
        out.append([",".join(it["reasons"]), c, p, " | ".join(it["details"]), share_of(c, None, areas)])
    for it in other:
        out.append([it["reasons"][0], it["cap"], "", " | ".join(it["details"]), share_of(it["cap"], it["part"] if not it["cap"] else None, areas)])
    out.sort(key=lambda x: (x[4], x[1], x[2], x[0]))
    counters, lines = {}, []
    for i, x in enumerate(out, 1):
        n = counters.get(x[4], 0); counters[x[4]] = n + 1
        lines.append([f"R-{i:04d}"] + [" ".join(str(v).split()) for v in x] + [str(n // a.batch_size + 1)])
    os.makedirs(REVIEW, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("item\treasons\tcap_id\tplatform\tdetail\tshare\tbatch\n")
        for l in lines:
            f.write("\t".join(l) + "\n")
    print(f"{os.path.relpath(OUT, os.path.dirname(MODEL))}: {len(lines)} items ({len(cell_items)} cells, {len(other)} other) from {len(cells)} cells")
    for s in sorted(counters):
        sel = [l for l in lines if l[5] == s]
        reasons = {}
        for l in sel:
            for r in l[1].split(","):
                reasons[r] = reasons.get(r, 0) + 1
        print(f"  share {s}: {len(sel)} items in {max(int(l[6]) for l in sel)} batches; " + ", ".join(f"{k} {v}" for k, v in sorted(reasons.items())))


def check(a):
    sel = [r for r in rows(OUT) if r["share"] == a.share and r["batch"] == a.batch]
    if not sel:
        sys.exit(f"no items for share {a.share}, batch {a.batch} in {os.path.relpath(OUT, os.path.dirname(MODEL))}")
    path = os.path.join(REVIEW, f"coverage-{a.share}-{a.batch}.tsv")
    if not os.path.exists(path):
        sys.exit(f"no {path}")
    keys = set()
    for p in PLATFORMS:
        keys |= {key(s) for s in items(p)}
    raw = open(path, encoding="utf-8").read().split("\n")
    problems = []
    if raw[0].split("\t") != HEAD_COV:
        problems.append(f"header must be: {' '.join(HEAD_COV)}")
    seen = {}
    for i, l in enumerate(raw[1:], 2):
        if not l.strip():
            continue
        f = l.split("\t")
        if len(f) != len(HEAD_COV) or '"' in l:
            problems.append(f"line {i}: {len(HEAD_COV)} tab-separated fields, no quoting"); continue
        r = dict(zip(HEAD_COV, f))
        if r["item"] in seen:
            problems.append(f"line {i}: {r['item']} again")
        seen[r["item"]] = i
        if r["verdict"] not in ("holds", "wrong", "unclear"):
            problems.append(f"line {i}: verdict is holds, wrong or unclear")
        if r["verdict"] == "wrong":
            if r["severity"] not in ("kind", "placement", "structure", "reading"):
                problems.append(f"line {i}: a wrong item's severity is kind, placement, structure or reading")
            if not re.match(r"^[A-Z]-[a-z-]+/[a-z-]+\.(tsv|md)|^scope\.tsv", r["correction"]):
                problems.append(f"line {i}: a correction names <part>/<file>, the row and the new value")
        elif r["severity"] or r["correction"]:
            problems.append(f"line {i}: severity and correction are for wrong items")
        if r["verdict"] == "unclear" and not r["what_would_settle_it"].strip():
            problems.append(f"line {i}: an unclear item says what would settle it")
        if not r["basis"].strip():
            problems.append(f"line {i}: basis names the keys read")
        for b in [x.strip() for x in r["basis"].split(";") if x.strip()]:
            if re.match(r"^[A-Z]{2}-(C-\d{3}/[a-z]+/[A-Z]{2}-S|I)-\d{4}$", b) and b not in keys:
                problems.append(f"line {i}: {b} is not a statement key or inventory id")
    for r in sel:
        if r["item"] not in seen:
            problems.append(f"{r['item']} has no line")
    for x in seen:
        if x not in {r["item"] for r in sel}:
            problems.append(f"{x} is not an item of share {a.share}, batch {a.batch}")
    for p in problems:
        print("PROBLEM", p)
    print(f"{len([x for x in seen if x in {r['item'] for r in sel}])} of {len(sel)} items; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", default="select", choices=["select", "check"])
    ap.add_argument("--sample", type=float, default=0.05)
    ap.add_argument("--seed", type=int, default=20261030)
    ap.add_argument("--batch-size", type=int, default=30)
    ap.add_argument("--share"); ap.add_argument("--batch")
    a = ap.parse_args()
    (check if a.cmd == "check" else select)(a)


if __name__ == "__main__":
    main()
