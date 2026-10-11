#!/bin/bash
# Render each URL in a list file (one per line) with page_text.mjs, sequentially, logging each fetch.
D=$(cd "$(dirname "$0")" && pwd)
while read -r u; do
  [ -z "$u" ] && continue
  python3 -I "$D/fetch.py" render "$u" | cut -f1,2 | sed "s|^|$u\t|"
done < "$1"
