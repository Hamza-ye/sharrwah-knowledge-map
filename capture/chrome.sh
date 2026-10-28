#!/usr/bin/env bash
# Start the capture browser: system Google Chrome, headed, with the dedicated capture profile in
# ./capture-profile (git-ignored), and remote debugging on 127.0.0.1:9230 for Playwright to attach.
#   capture/chrome.sh [start-url]
# Sign in by hand in this window; session drivers attach with connectOverCDP and open their own tabs.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
profile="${CAPTURE_PROFILE:-$root/capture-profile}"
port="${CDP_PORT:-9230}"
if curl -s "http://127.0.0.1:$port/json/version" >/dev/null 2>&1; then
  echo "a browser is already listening on 127.0.0.1:$port"; curl -s "http://127.0.0.1:$port/json/version"; exit 0
fi
mkdir -p "$profile"
nohup google-chrome --user-data-dir="$profile" --remote-debugging-port="$port" --remote-debugging-address=127.0.0.1 \
  --no-first-run --no-default-browser-check "${1:-about:blank}" >/dev/null 2>&1 &
for _ in $(seq 1 40); do curl -s "http://127.0.0.1:$port/json/version" && exit 0; sleep 0.5; done
echo "capture browser did not open the debugging port" >&2; exit 1
