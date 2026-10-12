#!/bin/bash
Z=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid
while IFS=$'\t' read -r url slug; do
  [ -s "$Z/fetched/docs/api/$slug.md" ] && continue
  $Z/scripts/fetch.sh "$url" "docs/api/$slug.md" >/dev/null
done < $Z/fetched/docs/api-urls.tsv
echo done
