# Print first-run candidates in chunks for one-by-one review.
import csv, sys, os
csv.field_size_limit(10**9)
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
r = list(csv.DictReader(open(os.path.join(here, 'candidates.tsv')), delimiter='\t', quoting=csv.QUOTE_NONE))
lo, hi = int(sys.argv[1]), int(sys.argv[2])
def short(s):
    s = s.replace('https://help.shopify.com/en/manual/', 'HC:').replace('https://www.shopify.com/legal/', 'LEGAL:')
    s = s.replace('https://shopify.dev/docs/', 'DEV:').replace('observed-sh@b46731d0:structures/shopify/', 'OSH:')
    s = s.replace('sharrwah-knowledge-map:evidence/shopify-engineering/runs/', 'ENG:')
    return s
for i, x in enumerate(r):
    if x['join'] != 'first-run' or not (lo <= i < hi):
        continue
    print(f"{i} {x['concern_id']} {x['placement'][:4].upper()} [{x['cite_ids']}] {short(x['structure'])} @ {x['identifier'][:90]}")
    print(f"    {x['statement']}")
