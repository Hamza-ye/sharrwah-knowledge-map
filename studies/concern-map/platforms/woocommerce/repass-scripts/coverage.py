# Coverage of concern x placement cells by statements.
# Usage: python3 -I coverage.py CONCERNS_TSV STATEMENTS_TSV [STATEMENTS_TSV ...]
import csv, sys, collections
csv.field_size_limit(10**9)
P = ["where", "decides", "responsible", "boundary", "reason"]
con = [r["concern_id"] for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE)]
cov = collections.Counter()
for p in sys.argv[2:]:
    for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE):
        cov[(r["concern_id"], r["placement"])] += 1
print("cells with a statement:", {p: sum(1 for c in con if cov[(c, p)]) for p in P}, "of", len(con))
for c in con:
    miss = [p for p in P if not cov[(c, p)]]
    if miss:
        print(c, "empty:", " ".join(miss))
