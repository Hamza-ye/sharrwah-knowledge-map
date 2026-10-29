#!/usr/bin/env bash
# The journey helper: every operation on a live journey run (capture/runs/journey-repl.mjs) in one command.
#   PLATFORM=<platform> capture/jstep.sh <label> start <store> <cdp-port> <fresh|profile>   start the runner
#   capture/jstep.sh <label> '<json>' ['<json>' ...]   run steps; prints each step row and the last step's main region
#                                                     and dialogs (accessibility tree, link addresses left out)
#   capture/jstep.sh <label> show <step> aria|text|frame|html|htmlctx [<regex>]
#                                                     print a held step's witness (read only): its accessibility tree
#                                                     (link addresses left out), text, frames' trees, HTML matches
#   capture/jstep.sh <label> close                    close the run (writes run.json and the trace), stop the runner
#   capture/jstep.sh <label> log [<lines>]             the runner's output (an evaluate step's value is printed there)
# The runner's log, its platform and its commands file live in $JOURNEY_WORKDIR (default
# /tmp/other-product-class-journeys), outside the repository.
cd "$(dirname "$0")/.." || exit 1
SP=${JOURNEY_WORKDIR:-/tmp/other-product-class-journeys}; mkdir -p "$SP"
L=$1; shift
case "$1" in
  start)
    store=$2; port=$3; ctx=$4
    [ -n "${PLATFORM:-}" ] && [ -d "$PLATFORM" ] || { echo "PLATFORM must name a platform folder"; exit 1; }
    : > "$SP/$L-cmds.jsonl"; echo "$PLATFORM" > "$SP/$L.platform"
    env PLATFORM="$PLATFORM" CDP_URL="http://127.0.0.1:$port" $([ "$ctx" = fresh ] && echo RUN_CONTEXT=fresh) ${RUN_ADOPT_PAGE:+RUN_ADOPT_PAGE=$RUN_ADOPT_PAGE} \
      nohup setsid node capture/runs/journey-repl.mjs "$L" "$store" "$SP/$L-cmds.jsonl" > "$SP/$L.log" 2>&1 &
    for i in $(seq 1 120); do grep -q 'run dir' "$SP/$L.log" 2>/dev/null && break; sleep 0.5; done
    head -1 "$SP/$L.log"
    exit 0 ;;
esac
P=$(cat "$SP/$L.platform" 2>/dev/null)
R=$(sed -n 's/^run dir: .*raw\/runs\///p' "$SP/$L.log" 2>/dev/null | head -1)
[ -n "$R" ] && [ -n "$P" ] || { echo "no live run for $L"; exit 1; }
D="$P/raw/runs/$R"
case "$1" in
  show)
    n=$(printf '%03d' "$2"); what=$3; rx=${4:-.}
    case $what in
      aria) grep -v '/url:' "$D/steps/$n.aria.yaml" | grep -E -- "$rx" ;;
      text) grep -E -- "$rx" "$D/steps/$n.text.txt" ;;
      frame) for f in "$D"/steps/$n.frame-*.aria.yaml; do [ -f "$f" ] && { echo "== $(basename "$f")"; grep -v '/url:' "$f" | grep -E -- "$rx"; }; done ;;
      html) grep -o -E -- "$rx" "$D/steps/$n.html" | head -60 ;;
      htmlctx) grep -n -B6 -A6 -E -- "$rx" "$D/steps/$n.html" | cut -c1-400 | head -80 ;;
    esac
    exit 0 ;;
  log) tail -n "${2:-20}" "$SP/$L.log" | cut -c1-6000; exit 0 ;;
  close)
    echo '{"do":"close"}' >> "$SP/$L-cmds.jsonl"
    for i in $(seq 1 120); do [ -f "$D/run.json" ] && break; sleep 1; done
    for p in $(pgrep -x node); do tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null | grep -q "journey-repl.mjs $L " && kill $p; done
    [ -f "$D/run.json" ] && echo "closed $D" || echo "NOT closed $D"
    exit 0 ;;
esac
# A last argument that is a number is the number of tree lines to print (default 70).
last=${@: -1}; if [[ "$last" =~ ^[0-9]+$ ]]; then set -- "${@:1:$#-1}"; else last=70; fi
timeout 280 python3 capture/journey_step.py "$D" "$SP/$L-cmds.jsonl" "$@" "$last"
