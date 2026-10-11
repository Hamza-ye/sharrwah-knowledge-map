# Print inventory rows mapped to the given concern keys (prefix match), for writing placements.
# Usage: python3 -I show_inv.py KEYPREFIX [MAX]
import csv, os, sys, collections
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(D)
ms = {}; exec(open(os.path.join(D, "mapping_def.py")).read(), ms)
pref = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 40
rows = list(csv.DictReader(open(os.path.join(OUT, "work", "inventory_raw.tsv"), encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
by = collections.defaultdict(list)
for r in rows:
    ks, _ = ms["map_row"](r["list"], r["entry"], r["group"], r["extra"])
    for k in ks:
        if k.startswith(pref):
            by[k].append(r)
for k in sorted(by):
    print(f"== {k} ({len(by[k])})")
    for r in by[k][:mx]:
        print(f"   {r['list']} | {r['entry'][:90]} | {r['group'][:60]}")
