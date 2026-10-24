# Prints the concern x placement cells with no statement in work/reviewed.tsv (plus optional extra statements file).
# Usage: python3 -I coverage.py [extra_statements.tsv]
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
st = rd(f"{SP}/work/reviewed.tsv")
for extra in sys.argv[1:]:
    st += rd(extra)
con = rd(f"{FIRST}/concerns.tsv")
have = collections.defaultdict(set)
for r in st:
    have[r["concern_id"]].add(r["placement"])
cnt = collections.Counter()
for c in con:
    miss = [p for p in PLACEMENTS if p not in have[c["concern_id"]]]
    for p in PLACEMENTS:
        if p in have[c["concern_id"]]: cnt[p] += 1
    if miss:
        print(c["concern_id"], ",".join(miss), "|", c["concern"][:110])
print(cnt, len(con))
