#!/bin/bash
# Fetch one page as a working copy and log it to fetched/log.tsv.
# Usage: fetch.sh URL            (help.shopify.com / shopify.dev: URL ending .md, fetched with curl;
#                                 anything else: rendered with method/capture/page_text.mjs)
set -u
base=$(cd "$(dirname "$0")/.." && pwd)
url=$1
mkdir -p "$base/fetched/pages"
name=$(echo "$url" | sed 's#https\?://##; s#[/?=&]#_#g')
now=$(date -u +%FT%TZ)
case "$url" in
  *.md|*.md\?*)
    out="$base/fetched/pages/$name"
    [ "${out%.md}" = "$out" ] && out="$out.md"
    code=$(curl -sS -L -o "$out" -w '%{http_code} %{url_effective}' -A 'Mozilla/5.0 (research; Q1 concern map)' "$url" 2>&1)
    status=${code%% *}; final=${code#* }
    sha=$(sha256sum "$out" | cut -d' ' -f1)
    printf '%s\t%s\tcurl\t%s\t%s\t%s\t%s\n' "$now" "$url" "$status" "fetched/pages/$(basename "$out")" "$sha" "$final" >> "$base/fetched/log.tsv"
    echo "$status $out"
    ;;
  *)
    out="$base/fetched/pages/$name.txt"
    r=$(timeout 150 node /home/user/sharrwah-knowledge-map/method/capture/page_text.mjs "$url" "$out")
    status=$(echo "$r" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); print(d.get("status"))' 2>/dev/null)
    sha=$(echo "$r" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); print(d.get("text_sha256",""))' 2>/dev/null)
    note=$(echo "$r" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); print(d.get("final_url",""), d.get("title",""), d.get("error",""))' 2>/dev/null)
    printf '%s\t%s\tpage_text.mjs\t%s\t%s\t%s\t%s\n' "$now" "$url" "$status" "fetched/pages/$(basename "$out")" "$sha" "$note" >> "$base/fetched/log.tsv"
    echo "$status $out $note"
    ;;
esac
sleep 1.2
