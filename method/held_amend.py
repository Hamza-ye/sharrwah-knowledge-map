# The coordinator's amendments from the held pass (Stage 4A; briefs/H-held.md, "After the batches"): each checked
# placement of an entry on a capability becomes an evidence row of that platform's cell, in the part that holds the
# cell, with its terms added to the cell's, its slot filler and its quality in the part's own files; the cell's reading
# says what the held pass added, and a cell that held nothing becomes held. The entry's scope is read from its
# placement by class_slice.py. A `new` thing is placed only once the coordinator has decided it in held/new.tsv: the
# capability it is (made in an amendment part first), an existing one it turned out to be, or out.
#
# Usage:
#   python3 -I method/held_amend.py plan --platform P      what the amendment would write, per part and cell (no change)
#   python3 -I method/held_amend.py apply --platform P     writes it; then run check_class_part.py on each part it names,
#                                                          and class_merge.py --complete
# Run apply once per platform, after all its batches are checked: it refuses a platform whose evidence already holds
# one of its entries.
import argparse, collections, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HELD = os.path.join(MODEL, "held")
PARTS = os.path.join(MODEL, "parts")
NEW_HEAD = ["platform", "name", "decision", "reading"]


def clip(s, n):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def table(path):
    raw = open(path, encoding="utf-8").read().split("\n")
    head = raw[0].split("\t")
    return head, [dict(zip(head, l.split("\t"))) for l in raw[1:] if l.strip()]


def write(path, head, rs):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for r in rs:
            f.write("\t".join(r.get(h, "") for h in head) + "\n")


def plan(p):
    entries = {r["entry_id"]: r for r in rows(os.path.join(HELD, p, "entries.tsv"))}
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(MODEL, "merged", "cells.tsv"))}
    caps = {r["cap_id"] for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv"))}
    new = {}
    if os.path.exists(os.path.join(HELD, "new.tsv")):
        for r in rows(os.path.join(HELD, "new.tsv")):
            if r["platform"] == p:
                new[r["name"]] = r["decision"]
    rowsout, pending = collections.defaultdict(list), []
    extra = collections.defaultdict(lambda: {"terms": [], "fillers": [], "qualities": []})
    for path in sorted(glob.glob(os.path.join(HELD, p, "placements-*.tsv"))):
        batch = re.search(r"placements-(.+)\.tsv$", path).group(1)
        for r in rows(path):
            ids = [x.strip() for x in r["entry_id"].split(";") if x.strip()]
            cs, ss = [r["cap_id"].strip()] if r["cap_id"].strip() else [], [s.strip() for s in r["supports"].split(";") if s.strip()]
            if r["placement"] == "new":
                d = new.get(r["cap_id"][4:].strip())
                if not d:
                    pending.append((batch, r["cap_id"], ids))
                    continue
                if d == "out":
                    continue
                cs = [d.split(":", 1)[1]]
            elif r["placement"] != "capability":
                continue
            for c in cs:
                if c not in caps or (c, p) not in cells:
                    sys.exit(f"{batch}: {c} has no cell for {p} in the merged model; make it first")
                for e in ids:
                    for s in ss or ["shows"]:
                        rowsout[(c, p)].append({"cap_id": c, "platform": p, "supports": s, "key": e,
                                                "why": f"(the held pass, {batch}) {' '.join(r['reading'].split())}: {clip(entries[e]['text'], 120)}"})
                    x = extra[(c, p)]
                    x["terms"] += [t.strip() for t in r.get("terms", "").split(";") if t.strip()]
                    for fl in [t.strip() for t in r.get("filler", "").split(";") if t.strip()]:
                        x["fillers"].append({"cap_id": c, "platform": p, "filler": fl, "key": e})
                    for q in [t.strip() for t in r.get("quality", "").split(";") if t.strip()]:
                        what, _, val = q.partition(":")
                        x["qualities"].append({"cap_id": c, "platform": p, "quality": what.strip(), "value": val.strip() or what.strip(), "key": e})
    return cells, rowsout, pending, extra


def summary(evs, entries):
    by = collections.Counter(e["supports"] for e in evs)
    structs = list(dict.fromkeys(entries[e["key"]]["structure"] for e in evs))
    ids = list(dict.fromkeys(e["key"] for e in evs))
    first = "; ".join(clip(entries[i]["text"], 70) for i in ids[:3])
    return (f"The held pass adds {', '.join(f'{v} {k}' for k, v in by.items())} from {len(ids)} "
            f"entr{'y' if len(ids) == 1 else 'ies'} of {', '.join(structs)} ({', '.join(ids[:6])}{' …' if len(ids) > 6 else ''}: {first})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["plan", "apply"])
    ap.add_argument("--platform", choices=PLATFORMS, required=True)
    a = ap.parse_args()
    p = a.platform
    entries = {r["entry_id"]: r for r in rows(os.path.join(HELD, p, "entries.tsv"))}
    cells, out, pending, extra = plan(p)
    for b, name, ids in pending:
        print(f"PENDING {b}: {name} ({len(ids)} entries) waits on the coordinator's decision in held/new.tsv")
    by_part = collections.defaultdict(list)
    for k, evs in out.items():
        by_part[cells[k]["part"]].append((k, evs))
    became = sum(1 for k in out if cells[k]["held"] != "statements")
    print(f"{p}: {sum(len(v) for v in out.values())} evidence rows for {len(out)} cells in {len(by_part)} parts; "
          f"{became} cells that held nothing become held")
    for part, ks in sorted(by_part.items()):
        print(f"   {part}: {len(ks)} cells, {sum(len(v) for _, v in ks)} rows")
    PLACED = {"core", "own-service", "extension-point", "outside"}
    for k, evs in sorted(out.items()):
        was = set((cells[k].get("placed_as") or "").split(";")) - {"", "not-stated"}
        now = {e["supports"] for e in evs} & PLACED
        if cells[k]["held"] != "statements" or now - was:
            print(f"   CHANGES {k[0]}@{k[1]}: {cells[k]['held']}, placed {';'.join(sorted(was)) or 'nowhere'} -> adds {';'.join(sorted(now - was)) or 'shows only'} ({len(evs)} rows)")
    if a.cmd == "plan":
        return
    if pending:
        sys.exit("decide every new thing in held/new.tsv first")
    for part, ks in sorted(by_part.items()):
        d = os.path.join(PARTS, part)
        eh, ev = table(os.path.join(d, "evidence.tsv"))
        have = {r["key"] for r in ev}
        if any(e["key"] in have for _, evs in ks for e in evs):
            sys.exit(f"{part}: its evidence already cites entries of {p}: applied before")
        ch, cl = table(os.path.join(d, "cells.tsv"))
        idx = {(r["cap_id"], r["platform"]): r for r in cl}
        for k, evs in ks:
            ev += evs
            c = idx[k]
            note = summary(evs, entries)
            if c["held"] != "statements":
                c["held"] = "statements"
                c["reading"] = f"Nothing in the concern map; {note[0].lower() + note[1:]} (a reading of each entry, in its evidence row)."
            else:
                c["reading"] = (c["reading"].rstrip() + " " + note + ".").strip()
            c["terms"] = ";".join(dict.fromkeys([t for t in c.get("terms", "").split(";") if t] + extra[k]["terms"]))
        write(os.path.join(d, "evidence.tsv"), eh, ev)
        write(os.path.join(d, "cells.tsv"), ch, cl)
        for fname, key in (("slot-fillers.tsv", "fillers"), ("qualities.tsv", "qualities")):
            fh_, fr = table(os.path.join(d, fname))
            fr += [x for k, _ in ks for x in extra[k][key]]
            write(os.path.join(d, fname), fh_, fr)
        print(f"wrote {part}: check it with python3 -I method/check_class_part.py {part}")


if __name__ == "__main__":
    main()
