"""Hold the Zid merchant dashboard's page index as a structure: zid/structures/dashboard-page-index/.

    .venv/bin/python capture/structure_zid_dashboard_page_index.py <code-fetch-run-id>

One code module of the dashboard (in the code fetch run) states a list of the dashboard's pages, each an object
{pageKey: `<key>`, path: `<path>`, title: t(`<namespace>:<key>`), ...}. Writes:
  source.js     that module's bytes as received
  items.jsonl   one page per line, in the module's order: pageKey, path and title key as written (a template
                expression such as `apps.${a}` is kept as written), with title_en and title_ar, the strings
                zid/structures/dashboard-locales holds under that exact key
  meta.json     source record, shape as observed, counts
Some entries sit inside conditional spreads in the code (`...r?[{pageKey:`settings.markets`,...}]:[]`): the items do
not state the condition; source.js does.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

from warcio.archiveiterator import ArchiveIterator

ROOT = Path(__file__).resolve().parent.parent
ENTRY = re.compile(r'pageKey:`([^`]+)`,path:`([^`]+)`,title:[\w$]+\(`([^`]+)`')


def main():
    run_id = sys.argv[1]
    warc = ROOT / 'zid' / 'raw' / 'runs' / run_id / 'fetch.warc.gz'
    found = None
    with open(warc, 'rb') as f:
        for r in ArchiveIterator(f):
            if r.rec_type != 'response':
                continue
            body = r.content_stream().read()
            if b'pageKey:`settings.markets`' in body:
                found = (r.rec_headers.get_header('WARC-Target-URI'), body, {
                    'record_id': r.rec_headers.get_header('WARC-Record-ID'), 'date': r.rec_headers.get_header('WARC-Date'),
                    'status': r.http_headers.get_statuscode(), 'content_type': r.http_headers.get_header('Content-Type'),
                    'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()})
                break
    uri, body, meta = found
    strings = {}
    for l in open(ROOT / 'zid' / 'structures' / 'dashboard-locales' / 'items.jsonl'):
        i = json.loads(l)
        strings[(i['language'], f"{i['namespace']}:{i['key']}")] = i['value']
    items = [{'pageKey': k, 'path': p, 'title': t, 'title_en': strings.get(('en', t)), 'title_ar': strings.get(('ar', t))}
             for k, p, t in ENTRY.findall(body.decode('utf-8'))]
    out = ROOT / 'zid' / 'structures' / 'dashboard-page-index'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'source.js').write_bytes(body)
    (out / 'items.jsonl').write_text(''.join(json.dumps(i, ensure_ascii=False) + '\n' for i in items))
    (out / 'meta.json').write_text(json.dumps({
        'structure': 'zid/dashboard-page-index', 'platform': 'zid', 'surface': 'merchant dashboard (dashboard.zid.sa)',
        'source': {'run_id': run_id, 'warc': str(warc.relative_to(ROOT)), 'uri': uri, **meta},
        'shape_observed': 'object literals {pageKey, path, title: t(<namespace>:<key>), sidebar?} in arrays, some inside '
                          'conditional spreads, in a minified module',
        'counts': {'pages': len(items), 'with_title_en': sum(1 for i in items if i['title_en']),
                   'with_title_ar': sum(1 for i in items if i['title_ar'])},
        'items': 'items.jsonl: pageKey, path, title as written; title_en and title_ar joined from '
                 'zid/structures/dashboard-locales on the exact <namespace>:<key>',
        'extractor': {'path': 'capture/structure_zid_dashboard_page_index.py',
                      'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }, indent=2, ensure_ascii=False) + '\n')
    print(out, len(items), 'pages')


if __name__ == '__main__':
    main()
