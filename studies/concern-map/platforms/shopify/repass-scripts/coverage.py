import sys, os, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
rows = rd(os.path.join(WORK, "reviewed-statements.tsv"))
for f in sorted(glob.glob(os.path.join(WORK, "added", "*.tsv"))):
    rows += rd(f)
con = [r["concern_id"] for r in rd(os.path.join(FIRST, "concerns.tsv"))]
if os.path.exists(os.path.join(WORK, "new-concerns.tsv")):
    con += [r["concern_id"] for r in rd(os.path.join(WORK, "new-concerns.tsv"))]
cov = collections.defaultdict(set)
for r in rows:
    cov[r["placement"]].add(r["concern_id"])
for p in ["where", "decides", "responsible", "boundary", "reason"]:
    miss = [c for c in con if c not in cov[p]]
    print(f"{p}: {len(con)-len(miss)}/{len(con)}; missing {len(miss)}: " + " ".join(m[5:] for m in miss))
print("statements:", len(rows))
