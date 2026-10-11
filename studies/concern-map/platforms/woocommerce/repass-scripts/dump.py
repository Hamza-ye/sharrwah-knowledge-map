# Print candidates (with row numbers) for the given concerns, or for a list name.
# Usage: python3 -I dump.py CANDIDATES_TSV INVENTORY_TSV WC-C-001 [WC-C-002 ...]
import csv, sys
csv.field_size_limit(10**9)
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
want = set(sys.argv[3:])
for i, r in enumerate(rows, start=2):
    if r["concern_id"] in want:
        print(f"[{i}] {r['concern_id']} {r['placement']:<11} {r['join']:<10} {r['cite_ids']:<10} id={r['identifier'][:60]!r}")
        print(f"      {r['structure'][:110]}")
        print(f"      {r['statement'][:400]}")
