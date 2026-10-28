#!/usr/bin/env bash
# Fetch an exact list of URLs into one WARC (+ CDX) as one run under <platform>/raw/runs/<run-id>/.
#   PLATFORM=<platform folder> capture/fetch.sh <label> <url-list-file> [wait-seconds]
# FETCH_UA=<user agent> replaces the default one; it is recorded.
# Only the listed URLs are requested (no recursion); robots.txt and any other automated-access directive has no
# authority over what is fetched: `-e robots=off` states it. Every response is kept, including errors and challenge
# pages. Files coding agents load as instructions, and robots.txt, are not fetched: their URLs are listed in
# skipped-urls.txt.
set -euo pipefail
label="$1"; list="$2"; wait="${3:-1}"
root="$(cd "$(dirname "$0")/.." && pwd)"
[ -n "${PLATFORM:-}" ] && [ -d "$root/$PLATFORM" ] || { echo "PLATFORM must name a platform folder of this repository" >&2; exit 1; }
run_id="$(date -u +%Y%m%dT%H%M%SZ)-$label"
dir="$root/$PLATFORM/raw/runs/$run_id"
mkdir -p "$dir/tmp"
UA="${FETCH_UA:-Mozilla/5.0 (X11; Linux x86_64) other-product-class-capture/0.1 (read-only evidence capture)}"
NOT_HELD='/(agents?\.md|claude(\.local)?\.md|gemini\.md|\.cursorrules|\.windsurfrules|\.clinerules|copilot-instructions\.md|SKILL\.md|robots\.txt)([?#].*)?$'
grep -i -E "$NOT_HELD" "$list" > "$dir/skipped-urls.txt" || true
grep -v -i -E "$NOT_HELD" "$list" > "$dir/urls.txt" || true
[ -s "$dir/skipped-urls.txt" ] || rm -f "$dir/skipped-urls.txt"
# The network path this client uses, as the platform's Cloudflare edge sees it (IP last octet masked): the host of
# the first listed URL.
th="$(head -1 "$dir/urls.txt" | sed -E 's#^https?://([^/]+).*#\1#')"
net="$( { curl -s --max-time 20 -A "$UA" "https://$th/cdn-cgi/trace" || true; } | awk -F= -v th="$th" '
  $1=="ip"{ip=$2; sub(/[.:][0-9a-f]+$/, ".x", ip)} $1=="loc"{loc=$2} $1=="colo"{colo=$2} $1=="http"{h=$2}
  END{if (loc != "") printf "{\"via\": \"curl %s/cdn-cgi/trace\", \"ip\": \"%s\", \"loc\": \"%s\", \"colo\": \"%s\", \"http\": \"%s\"}", th, ip, loc, colo, h}')"
[ -n "$net" ] || net="{\"via\": \"$th answered no /cdn-cgi/trace\"}"
started="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
set +e
wget --input-file="$dir/urls.txt" \
     --warc-file="$dir/fetch" --warc-cdx -e robots=off --warc-header="operator: other-product-class capture/fetch.sh" \
     --user-agent="$UA" --wait="$wait" --tries=2 --timeout=90 --compression=auto \
     --content-on-error --server-response --no-verbose \
     --directory-prefix="$dir/tmp" --delete-after --output-file="$dir/wget.log"
rc=$?
set -e
rm -rf "$dir/tmp"
ended="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
cat > "$dir/run.json" <<EOF
{
  "run_id": "$run_id", "platform": "$PLATFORM", "label": "$label", "kind": "fetch", "started": "$started", "ended": "$ended",
  "tool": "$(wget --version | head -1)", "user_agent": "$UA", "wait_seconds": $wait,
  "url_count": $(grep -cv '^\s*$' "$dir/urls.txt"), "urls_sha256": "$(sha256sum "$dir/urls.txt" | cut -d' ' -f1)",
  "wget_exit": $rc, "network": $net,
  "script": {"path": "capture/fetch.sh", "sha256": "$(sha256sum "$0" | cut -d' ' -f1)"}
}
EOF
echo "$dir"
