#!/bin/bash
# Render one URL with page_text.mjs into fetched/, log to fetched/log.tsv.
# Usage: render.sh URL OUTNAME
set -u
Z=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid
url=$1; out=$2
log=$Z/fetched/log.tsv
[ -f "$log" ] || printf 'fetched_at\tmethod\turl\tstatus\tfinal_url\tbytes\tsha256\tfile\n' > "$log"
j=$(node /home/user/sharrwah-knowledge-map/method/capture/page_text.mjs "$url" "$Z/fetched/$out" 2>&1 | tail -1)
ts=$(echo "$j" | jq -r '.fetched_at // empty' 2>/dev/null); st=$(echo "$j" | jq -r '.status // .error // empty' 2>/dev/null)
fin=$(echo "$j" | jq -r '.final_url // empty' 2>/dev/null); ch=$(echo "$j" | jq -r '.text_chars // empty' 2>/dev/null); h=$(echo "$j" | jq -r '.text_sha256 // empty' 2>/dev/null)
[ -z "$ts" ] && ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf '%s\trender\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ts" "$url" "$st" "$fin" "$ch" "$h" "$out" >> "$log"
echo "$st $ch $out $(echo "$j" | jq -r '.title // empty' 2>/dev/null)"
sleep 1
