#!/bin/bash
# Fetch one URL as served (curl) into fetched/, log to fetched/log.tsv.
# Usage: fetch.sh URL OUTNAME [lang]
# Keeps about one request per second per host by sleeping 1.2 s after each fetch.
set -u
Z=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid
url=$1; out=$2; lang=${3:-en,ar;q=0.8}
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
log=$Z/fetched/log.tsv
[ -f "$log" ] || printf 'fetched_at\tmethod\turl\tstatus\tfinal_url\tbytes\tsha256\tfile\n' > "$log"
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
w=$(curl -sS -L --max-redirs 8 --max-time 90 -A "$UA" -H "Accept-Language: $lang" --compressed \
     -o "$Z/fetched/$out" -w '%{http_code}\t%{url_effective}\t%{size_download}' "$url" 2>/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid/fetched/.curlerr)
code=$(echo "$w" | cut -f1); fin=$(echo "$w" | cut -f2); by=$(echo "$w" | cut -f3)
h=$( [ -f "$Z/fetched/$out" ] && sha256sum "$Z/fetched/$out" | cut -d' ' -f1 )
printf '%s\tcurl\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ts" "$url" "$code" "$fin" "$by" "$h" "$out" >> "$log"
echo "$code $by $out"
sleep 1.2
