# Compact view: per concern, up to N entries per list (for writing placements).
# Usage: python3 -I show_inv2.py PREFIX [N]
import csv, os, sys, collections
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(D)
ms = {}; exec(open(os.path.join(D, "mapping_def.py")).read(), ms)
pref = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
rows = list(csv.DictReader(open(os.path.join(OUT, "work", "inventory_raw.tsv"), encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
by = collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows:
    ks, _ = ms["map_row"](r["list"], r["entry"], r["group"], r["extra"])
    for k in ks:
        if k.startswith(pref):
            by[k][r["list"]].append(r["entry"] + ("  {" + r["group"][:40] + "}" if r["list"] in ("plan-features", "admin-navigation", "settings", "other:help-center-sections") else ""))
for k in sorted(by):
    tot = sum(len(v) for v in by[k].values())
    print(f"== {k} ({tot})")
    for lst, es in by[k].items():
        print(f"   [{lst}] " + " | ".join(es[:n]) + (f" ... (+{len(es)-n})" if len(es) > n else ""))
