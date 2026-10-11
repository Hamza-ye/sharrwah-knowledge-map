# List cells still empty after reviewed candidates (work/kept.tsv) and the spec statements.
# Usage: ALLOW_WORKING=1 python3 -I empty_cells.py spec_a spec_b ...
import csv, os, sys, importlib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newcite
for p in sys.argv[1:]:
    importlib.import_module(p)
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv.field_size_limit(10**9)
con = [r["concern_id"] for r in csv.DictReader(open("/home/user/sharrwah-knowledge-map/studies/concern-map/platforms/woocommerce/concerns.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE)]
have = collections.Counter()
for r in csv.DictReader(open(os.path.join(W, "work", "kept.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE):
    have[(r["concern_id"], r["placement"])] += 1
for s in newcite.STATEMENTS:
    have[(s["concern_id"], s["placement"])] += 1
gapped = {(g["concern_id"], g["placement"]) for g in newcite.GAPS}
P = ["where", "decides", "responsible", "boundary", "reason"]
print("cells with a statement:", {p: sum(1 for c in con if have[(c, p)]) for p in P})
empty = [(c, p) for c in con for p in P if not have[(c, p)] and (c, p) not in gapped]
print("empty, no gap:", len(empty))
byp = collections.defaultdict(list)
for c, p in empty:
    byp[p].append(c[5:])
for p in P:
    print(p, len(byp[p]), " ".join(byp[p]))
