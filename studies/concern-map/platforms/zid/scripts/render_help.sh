#!/bin/bash
Z=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid
n=0
while IFS=$'\t' read -r url key; do
  n=$((n+1)); out="helptxt/$(printf '%03d' $n)-$key.txt"
  [ -s "$Z/fetched/$out" ] && continue
  $Z/scripts/render.sh "$url" "$out" >/dev/null
  printf '%s\t%s\n' "$out" "$url" >> $Z/fetched/helptxt/index.tsv
done < $Z/fetched/help/render-list.tsv
echo done
