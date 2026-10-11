# Overview of candidates per concern and placement.
# Usage: python3 -I overview.py CANDIDATES_TSV
import csv, sys, collections
csv.field_size_limit(10**9)
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
P = ["where", "decides", "responsible", "boundary", "reason"]
cov = collections.defaultdict(collections.Counter)
for r in rows:
    cov[r["concern_id"]][(r["placement"], r["join"][0])] += 1
for c in sorted(cov):
    print(c, " ".join(f"{p[:4]}:{cov[c][(p,'l')]}/{cov[c][(p,'f')]}" for p in P))
