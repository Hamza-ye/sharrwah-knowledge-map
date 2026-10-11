#!/bin/bash
# Fetch a URL with curl (logged), make a visible-text copy for reading if it is HTML, print the text path.
# Usage: bash get.sh URL
D=$(cd "$(dirname "$0")" && pwd)
out=$(python3 -I "$D/fetch.py" curl "$1")
status=$(echo "$out" | cut -f1); file=$(echo "$out" | cut -f2)
f="$D/../fetched/$file"
if [[ "$file" == *.html ]]; then python3 -I "$D/html2text.py" "$f" >/dev/null; echo "$status ${f%.html}.txt"; else echo "$status $f"; fi
