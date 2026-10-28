"""Drive a live journey-repl run and show what its steps produced.

    python3 capture/journey_step.py <run-dir> <commands.jsonl> '<json command>' ['<json command>' ...] [lines]

Appends the commands, in order and at once, to the commands file the runner reads
(capture/runs/journey-repl.mjs), waits for every step they produce (commands that make no step, such as
stopped-at-confirm / close, produce none), then prints each step row (outcome, error, landed URL,
rendered) and the accessibility tree of the last step's main region and open dialogs (first [lines] lines
each, default 60). The steps' full files are in <run-dir>/steps/.
"""
import json
import re
import sys
import time
from pathlib import Path

NON_STEP = {'stopped-at-confirm', 'close'}


def regions(aria, limit):
    lines = aria.splitlines()
    out, i = [], 0
    while i < len(lines):
        m = re.match(r'^(\s*)- (main|dialog\b[^:]*|alertdialog\b[^:]*):?', lines[i])
        if m and not any(o[0] <= i < o[1] for o in [(a, b) for a, b, _ in out]):
            ind = len(m.group(1))
            j = i + 1
            while j < len(lines) and (len(lines[j]) - len(lines[j].lstrip()) > ind):
                j += 1
            out.append((i, j, lines[i:j][:limit]))
            i = j
        else:
            i += 1
    return out


def main():
    run, cmd_file = Path(sys.argv[1]), Path(sys.argv[2])
    rest = sys.argv[3:]
    limit = int(rest.pop()) if rest and rest[-1].isdigit() else 60
    cmds = [json.loads(a) for a in rest]
    actions = run / 'actions.jsonl'
    before = sum(1 for _ in open(actions)) if actions.exists() else 0
    with open(cmd_file, 'a') as f:
        for cmd in cmds:
            f.write(json.dumps(cmd, ensure_ascii=False) + '\n')
    steps = sum(1 for c in cmds if c.get('do') not in NON_STEP)
    for c in cmds:
        if c.get('do') in NON_STEP:
            print('appended', c.get('do'))
    if not steps:
        return
    while not actions.exists() or sum(1 for _ in open(actions)) < before + steps:
        time.sleep(1)
    rows = [json.loads(l) for l in open(actions).read().splitlines()[before:before + steps]]
    for row in rows:
        print(json.dumps({k: row.get(k) for k in ('step', 'outcome', 'error', 'url', 'ready')}, ensure_ascii=False))
    aria = (run / 'steps' / f"{rows[-1]['step']:03d}.aria.yaml")
    if aria.exists():
        for a, b, part in regions(aria.read_text(), limit):
            print('\n'.join(l for l in part if '/url:' not in l))
            if b - a > limit:
                print(f'  … {b - a - limit} more lines')


if __name__ == '__main__':
    main()
