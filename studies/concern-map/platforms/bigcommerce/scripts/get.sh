#!/bin/bash
# Working-copy fetch with logging. Usage: get.sh MODE URL OUTNAME
#   MODE raw    -> curl body as served
#   MODE render -> page_text.mjs visible text
# Every fetch is appended to fetched/log.tsv: utc, mode, url, http, final_url, out, bytes, sha256
B=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/bigcommerce
LOG=$B/fetched/log.tsv
[ -f "$LOG" ] || printf 'utc\tmode\turl\thttp\tfinal_url\tout\tbytes\tsha256\n' > "$LOG"
mode=$1; url=$2; out=$B/fetched/$3
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "$mode" = raw ]; then
  w=$(curl -sS -L --max-redirs 8 --max-time 90 -A "$UA" -H 'Accept-Language: en,ar;q=0.8' --compressed -o "$out" -w '%{http_code}\t%{url_effective}' "$url" 2>&1)
  code=$(printf '%s' "$w" | cut -f1); final=$(printf '%s' "$w" | cut -f2)
else
  if [ "$mode" = links ]; then tool=$B/scripts/links.mjs; elif [ "$mode" = slow ]; then tool=$B/scripts/slow_text.mjs; else tool=/home/user/sharrwah-knowledge-map/method/capture/page_text.mjs; fi
  j=$(node "$tool" "$url" "$out" 2>&1 | tail -1)
  code=$(printf '%s' "$j" | python3 -I -c 'import json,sys
try: print(json.loads(sys.stdin.read()).get("status"))
except Exception: print("ERR")')
  final=$(printf '%s' "$j" | python3 -I -c 'import json,sys
try: d=json.loads(sys.stdin.read()); print(d.get("final_url") or d.get("error",""))
except Exception: print("")')
fi
bytes=$( [ -f "$out" ] && stat -c %s "$out" || echo 0 )
sha=$( [ -f "$out" ] && sha256sum "$out" | cut -d' ' -f1 || echo "" )
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$now" "$mode" "$url" "$code" "$final" "$3" "$bytes" "$sha" >> "$LOG"
echo "$code $bytes $3 <- $final"
sleep 1
