"""Compute each capability's count and kind from the parts' cells, by the plan's one rule (PLAN.md, Stage 4A, "The kind
and the count"; `studies/class-model/briefs/B-extent.md`).

Usage: python3 -I method/class_kinds.py [--domain D] [--out PATH]

Reads every part folder in studies/class-model/parts/ (or one domain's), with the `derived.tsv` that
`method/check_class_part.py` writes: run the checker on each part first. For each capability:
- for each platform, its cell's `held` and the placements its evidence supports (`placed_as`), or `no cell`;
- the count: how many platforms hold statements and place it in their core or as their own service;
- the kind: `class` where the count is at least one; `slot` where every platform whose statements show it places it
  only as an extension point or outside; otherwise `open: third parties where stated`, where some platform places it
  with third parties and another is `not-stated`, or `open: unplaced`, where every platform that shows it is
  `not-stated` (`studies/class-model/review-dry-run-rulings.md`, convention 12). `open` is never folded into the others;
- the scope a `class` holds under: `general` where some platform's own placement holds generally, else the scopes of
  the statements that place it (a plan, a beta, an observed store).
With fewer than five platforms mapped, a `class` stays a class, while a `slot` or an `open` is provisional.
A platform with `none-held`, or no cell, is never counted as lacking the capability.
Prints a summary per domain and kind, and writes the table (default: stdout as TSV with --out -).
"""
import argparse, csv, os, sys

csv.field_size_limit(10**9)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PART_ORDER, rows

OWN = {"core", "own-service"}
THIRD = {"extension-point", "outside"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain")
    ap.add_argument("--out")
    ap.add_argument("--exclude", default="", help="parts to leave out, comma-separated, as class_merge.py --exclude")
    a = ap.parse_args()
    leave = {x for x in a.exclude.replace(";", ",").split(",") if x.strip()}
    base = os.path.join(MODEL, "parts")
    caps, cells = {}, {}
    for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        dom, _, kind = d.partition("-")
        if (a.domain and dom != a.domain) or kind not in PART_ORDER or d in leave:
            continue
        for r in rows(os.path.join(base, d, "capabilities.tsv")):
            caps[r["cap_id"]] = r | {"domain": dom}
        if not os.path.exists(os.path.join(base, d, "derived.tsv")):
            sys.exit(f"{d}: no derived.tsv; run method/check_class_part.py on it first")
        for r in rows(os.path.join(base, d, "derived.tsv")):
            cells[r["cap_id"], r["platform"]] = r
    out = []
    for cid in sorted(caps):
        per, count, shows, third, scopes = {}, 0, 0, 0, []
        for p in PLATFORMS:
            c = cells.get((cid, p))
            if not c:
                per[p] = "no cell"
                continue
            placed = set(x for x in c["placed_as"].split(";") if x)
            per[p] = f"{c['held']}:{';'.join(sorted(placed))}" if c["held"] == "statements" else "none-held"
            if c["held"] == "statements":
                shows += 1
                if placed & OWN:
                    count += 1
                    scopes.append(c.get("own_scopes", "") or "general")
                elif placed and placed <= THIRD:
                    third += 1
        if count >= 1:
            kind = "class"
        elif shows and third == shows:
            kind = "slot"
        elif third:
            kind = "open: third parties where stated"
        else:
            kind = "open: unplaced"
        scope = "" if kind != "class" else ("general" if "general" in scopes else " / ".join(scopes))
        out.append([cid, caps[cid]["domain"], caps[cid]["area"], caps[cid]["capability"], caps[cid]["parent"], str(count), kind, scope]
                   + [per[p] for p in PLATFORMS])
    head = ["cap_id", "domain", "area", "capability", "parent", "count", "kind", "class_scope"] + list(PLATFORMS)
    summary = {}
    for r in out:
        summary.setdefault(r[1], {}).setdefault(r[6], 0)
        summary[r[1]][r[6]] += 1
    for dom in sorted(summary):
        print(f"domain {dom}: " + ", ".join(f"{k} {n}" for k, n in sorted(summary[dom].items())), file=sys.stderr)
    if a.out:
        f = sys.stdout if a.out == "-" else open(a.out, "w", encoding="utf-8", newline="")
        f.write("\t".join(head) + "\n")
        for r in out:
            f.write("\t".join(v.replace("\t", " ") for v in r) + "\n")
        if f is not sys.stdout:
            f.close()


if __name__ == "__main__":
    main()
