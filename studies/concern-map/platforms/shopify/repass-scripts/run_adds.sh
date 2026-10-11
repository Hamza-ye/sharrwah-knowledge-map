#!/bin/bash
# Rebuilds every added statement and citation in a fixed order, so citation ids stay stable.
set -e
cd "$(dirname "$0")/.."
rm -f work/cites-added.tsv work/added/*.tsv
python3 -I scripts/review.py
for s in add_plan_rows add_routes add_osh add_web add_store_values extend add_schema add_web2; do python3 -I scripts/$s.py; done
