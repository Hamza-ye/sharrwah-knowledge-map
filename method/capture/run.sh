#!/bin/bash
# One capture run: raw fetch of every item, browser render of every item, then finalize.
# Usage: run.sh ITEMS_JSON RUN_DIR   (CAPTURE_WORKERS sets how many fetches run at once)
set -eu
here=$(cd "$(dirname "$0")" && pwd)
items=${1:?items json}
run=${2:?run directory}
mkdir -p "$run"
python3 -I "$here/fetch_raw.py" "$items" "$run"
python3 -I -c 'import json, sys
p = json.load(open(sys.argv[1]))
json.dump([{"n": r["n"], "url": r["url"], "dir": r["dir"],
            "keep_body": not (200 <= r["http_code"] < 300 and r["raw_file"])} for r in p],
          open(sys.argv[2], "w"), indent=0)' "$run/phase1.json" "$run/render-list.json"
node "$here/render.mjs" "$run" "$run/render-list.json"
python3 -I "$here/finalize.py" "$run"
