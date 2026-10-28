"""Join every route of the Zid dashboard's route manifest to the browser-run steps that hold it:
zid/index/ledger/dashboard-routes.tsv.

    python3 capture/ledger_zid.py

The routes are zid/structures/dashboard-route-manifest/items.jsonl, in the manifest's order. Columns:
  route_id, parent_id, path, index      as the manifest states them
  path_joined                           the paths along parent_id joined with '/' (':lang/stores/:storeId/...')
  has_page                              the manifest's hasDefaultExport
  status                                opened: a step with outcome ok landed on a URL this path matches; failed: only
                                        steps whose action failed landed there; redirected: a step was sent to this
                                        route (its intent names the route id) and landed elsewhere; not opened: no step
  steps                                 every step that landed on a URL this path matches, as <run-id>#<step>
  sent_to                               the steps whose intent names the route id, as <run-id>#<step> -> landed path
  first                                 the first step that landed here with outcome ok and its page ready (else the
                                        first that landed here): its witnesses, steps/NNN.text.txt and .aria.yaml
A landed URL matches a path when each ':param' takes one segment and the rest is equal; an optional '?' segment may
be absent. The query string is not compared. A URL that several paths match is held by the ones with the most static
segments (`customers/groups/create` before `customers/groups/:id`), as React Router ranks a static segment before a
dynamic one; a layout route and its index route share a path and both hold it.
"""
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
Z = ROOT / 'zid'


def main():
    routes = [json.loads(l) for l in open(Z / 'structures' / 'dashboard-route-manifest' / 'items.jsonl')]
    by_id = {r['id']: r for r in routes}

    def joined(r):
        segs = []
        while r:
            if r.get('path'):
                segs.append(r['path'])
            r = by_id.get(r.get('parentId'))
        return '/'.join(reversed(segs))

    def pattern(p):
        parts = []
        for seg in p.split('/'):
            opt = seg.endswith('?')
            s = seg[:-1] if opt else seg
            body = '[^/]+' if s.startswith(':') else re.escape(s)
            parts.append(f'(?:/{body})?' if opt else f'/{body}')
        return re.compile('^' + ''.join(parts) + '/?$')

    steps = []
    for run in sorted((Z / 'raw' / 'runs').iterdir()):
        if not (run / 'actions.jsonl').exists() or not (run / 'run.json').exists():
            continue
        for l in open(run / 'actions.jsonl'):
            if l.strip():
                s = json.loads(l)
                u = urlsplit(s['url'])
                if u.hostname == 'dashboard.zid.sa':
                    steps.append((run.name, s, u.path))
    pats = []
    for r in routes:
        pj = joined(r)
        static = sum(1 for seg in pj.split('/') if seg and not seg.startswith(':'))
        pats.append((r, pj, pattern(pj) if pj else re.compile('^/?$'), static))
    assigned = {r['id']: [] for r in routes}
    for rid, s, p in steps:
        matching = [(r, static) for r, _, rx, static in pats if rx.match(p)]
        top = max((static for _, static in matching), default=None)
        for r, static in matching:
            if static == top:
                assigned[r['id']].append((rid, s, p))
    rows = []
    for r, pj, _, _ in pats:
        hits = assigned[r['id']]
        sent = [(rid, s, p) for rid, s, p in steps
                if re.search(r'(^| )' + re.escape(r['id']) + r'( |$)', (s.get('intent') or '').removeprefix('manifest route '))]
        ok = [h for h in hits if h[1]['outcome'] == 'ok']
        status = 'opened' if ok else 'failed' if hits else 'redirected' if sent else 'not opened'
        first = next((h for h in hits if h[1]['outcome'] == 'ok' and h[1].get('ready')), hits[0] if hits else None)
        rows.append({
            'route_id': r['id'], 'parent_id': r.get('parentId', ''), 'path': r.get('path', ''), 'index': r.get('index', ''),
            'path_joined': pj, 'has_page': r.get('hasDefaultExport'), 'status': status,
            'steps': ' '.join(f"{rid}#{s['step']}" for rid, s, _ in hits),
            'sent_to': ' '.join(f"{rid}#{s['step']}->{p}" for rid, s, p in sent),
            'first': f"zid/raw/runs/{first[0]}/steps/{first[1]['step']:03d}.text.txt zid/raw/runs/{first[0]}/steps/{first[1]['step']:03d}.aria.yaml" if first else '',
        })
    out = Z / 'index' / 'ledger'
    out.mkdir(parents=True, exist_ok=True)
    with open(out / 'dashboard-routes.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    counts = {}
    for row in rows:
        counts[row['status']] = counts.get(row['status'], 0) + 1
    print(len(rows), 'routes', counts)


if __name__ == '__main__':
    main()
