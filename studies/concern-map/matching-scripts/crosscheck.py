"""List generated candidate pairs that are neither in the same match row nor co-listed
in an unclear row, by descending score. Usage: python3 -I crosscheck.py <q1m_dir> [min_score]"""
import csv, os, sys
csv.field_size_limit(10**9)
d = sys.argv[1]; mn = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
def rows(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
row_of = {}
for r in rows(os.path.join(d, "matches.tsv")):
    for k in ("shopify", "salla", "woocommerce"):
        for c in filter(None, r[k].split(";")):
            row_of[c] = r["match_id"]
uc = []
for r in rows(os.path.join(d, "unclear.tsv")):
    s = set()
    for k in ("shopify", "salla", "woocommerce"):
        s.update(filter(None, r[k].split(";")))
    uc.append(s)
n = 0
for r in rows(os.path.join(d, "work", "candidates.tsv")):
    sc = float(r["score"]); a, b = r["a"], r["b"]
    if sc < mn:
        continue
    if a in row_of and row_of.get(a) == row_of.get(b):
        continue
    if any(a in s and b in s for s in uc):
        continue
    n += 1
    print(f"{sc:.2f} {a} [{row_of.get(a,'-')}] {r['a_name'][:45]} || {b} [{row_of.get(b,'-')}] {r['b_name'][:45]} || T:{r['term_shared'][:70]} I:{r['ident_shared'][:40]} tf:{r['tfidf']}")
print("total", n)
