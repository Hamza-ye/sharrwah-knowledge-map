"""Hold the Zid merchant dashboard's route manifest as a structure: zid/structures/dashboard-route-manifest/.

    .venv/bin/python capture/structure_zid_dashboard_manifest.py <fetch-run-id>

Reads, from the fetch run's WARC, the dashboard's shell page (the run's first URL) and the manifest file the shell
names (`/assets/manifest-<version>.js`, which sets `window.__reactRouterManifest`), and writes:
  source.js     the manifest file's bytes as received
  items.jsonl   one route per line, in the manifest's order: the route object as the manifest states it
  meta.json     source (run, WARC record of the manifest and of the shell that names it), shape as observed, counts
"""
import hashlib
import json
import re
import sys
from pathlib import Path

from warcio.archiveiterator import ArchiveIterator

ROOT = Path(__file__).resolve().parent.parent


def responses(warc):
    with open(warc, 'rb') as f:
        for r in ArchiveIterator(f):
            if r.rec_type == 'response':
                body = r.content_stream().read()
                yield r.rec_headers.get_header('WARC-Target-URI'), body, {
                    'record_id': r.rec_headers.get_header('WARC-Record-ID'), 'date': r.rec_headers.get_header('WARC-Date'),
                    'status': r.http_headers.get_statuscode(), 'content_type': r.http_headers.get_header('Content-Type'),
                    'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}


def main():
    run_id = sys.argv[1]
    run = ROOT / 'zid' / 'raw' / 'runs' / run_id
    warc = run / 'fetch.warc.gz'
    shell_uri = (run / 'urls.txt').read_text().split('\n')[0].strip()
    held = {uri: (body, meta) for uri, body, meta in responses(warc)}
    shell, shell_meta = held[shell_uri]
    name = re.search(rb'/assets/(manifest-[A-Za-z0-9]+\.js)', shell).group(1).decode()
    uri = f'https://dashboard.zid.sa/assets/{name}'
    body, meta = held[uri]
    text = body.decode('utf-8')
    prefix = 'window.__reactRouterManifest='
    assert text.startswith(prefix), text[:80]
    manifest = json.loads(text[len(prefix):].rstrip().rstrip(';'))
    routes = manifest['routes']
    out = ROOT / 'zid' / 'structures' / 'dashboard-route-manifest'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'source.js').write_bytes(body)
    (out / 'items.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in routes.values()))
    keys = {}
    for r in routes.values():
        for k in r:
            keys[k] = keys.get(k, 0) + 1
    rel = str(warc.relative_to(ROOT))
    (out / 'meta.json').write_text(json.dumps({
        'structure': 'zid/dashboard-route-manifest', 'platform': 'zid', 'surface': 'merchant dashboard (dashboard.zid.sa)',
        'source': {'run_id': run_id, 'warc': rel, 'uri': uri, **meta},
        'named_by': {'warc': rel, 'uri': shell_uri, **shell_meta},
        'shape_observed': 'one JavaScript statement, window.__reactRouterManifest = a JSON object with keys entry, routes, '
                          'url, version; routes is an object keyed by route id, each route an object with id, parentId, '
                          'path, index, hasAction, hasLoader, hasClientAction, hasClientLoader, hasClientMiddleware, '
                          'hasDefaultExport, hasErrorBoundary, module, imports, css (React Router manifest)',
        'manifest_top': {k: manifest[k] for k in manifest if k != 'routes' and k != 'entry'},
        'counts': {'routes': len(routes), 'keys': keys,
                   'hasClientLoader': sum(1 for r in routes.values() if r.get('hasClientLoader')),
                   'hasLoader': sum(1 for r in routes.values() if r.get('hasLoader')),
                   'hasAction': sum(1 for r in routes.values() if r.get('hasAction'))},
        'items': 'items.jsonl: the routes object\'s values in its order, each as stated',
        'extractor': {'path': 'capture/structure_zid_dashboard_manifest.py',
                      'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }, indent=2, ensure_ascii=False) + '\n')
    print(out, len(routes), 'routes', manifest.get('version'))


if __name__ == '__main__':
    main()
