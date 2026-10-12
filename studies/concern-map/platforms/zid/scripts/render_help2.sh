#!/bin/bash
# Render help articles from a list (url<TAB>key) into fetched/helptxt/, numbering from START; append to index.tsv.
# Usage: render_help2.sh LIST START
Z=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid
list=$1; n=$(( $2 - 1 ))
while IFS=$'\t' read -r url key; do
  n=$((n+1)); out="helptxt/$(printf '%03d' $n)-$key.txt"
  [ -s "$Z/fetched/$out" ] && continue
  r=$($Z/scripts/render.sh "$url" "$out")
  printf '%s\t%s\n' "$out" "$url" >> $Z/fetched/helptxt/index.tsv
  echo "$r"
done < "$list"
echo done
