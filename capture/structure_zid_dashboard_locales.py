"""Hold the Zid merchant dashboard's locale files as a structure: zid/structures/dashboard-locales/.

    .venv/bin/python capture/structure_zid_dashboard_locales.py <code-fetch-run-id> <locales-fetch-run-id>

The dashboard's entry module (assets/entry.client-<hash>.js, in the code fetch run) states every locale file it loads:
an object {en: {<namespace>: <version>, ...}, ar: {...}}, loaded from /locales/<language>/<namespace>.json?<version>.
The locales fetch run holds each of those files. Writes:
  source/<language>/<namespace>.json   each file's bytes as received
  items.jsonl   one line per string: language, namespace, key (the nested keys joined with '.', as the dashboard's code
                names a string: '<namespace>:<key>'), value; in each file's order
  meta.json     the namespace map with its source record, each file's record, counts
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


def flat(node, prefix=''):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from flat(v, f'{prefix}.{k}' if prefix else k)
    else:
        yield prefix, node


def main():
    code_run, loc_run = sys.argv[1], sys.argv[2]
    runs = ROOT / 'zid' / 'raw' / 'runs'
    code_warc, loc_warc = runs / code_run / 'fetch.warc.gz', runs / loc_run / 'fetch.warc.gz'
    entry = next((u, b, m) for u, b, m in responses(code_warc) if '/assets/entry.client-' in u)
    js = entry[1].decode('utf-8')
    found = re.search(r'=\{(en:\{.*?\}),(ar:\{.*?\})\}', js)
    nsmap = {}
    for part in found.groups():
        lang, inner = part.split(':', 1)
        nsmap[lang] = dict(re.findall(r'"?([A-Za-z0-9_\-]+)"?:`([0-9a-f]{8})`', inner))
    held = {u: (b, m) for u, b, m in responses(loc_warc)}
    out = ROOT / 'zid' / 'structures' / 'dashboard-locales'
    files, items, missing = [], [], []
    for lang, namespaces in nsmap.items():
        for ns, ver in namespaces.items():
            uri = f'https://dashboard.zid.sa/locales/{lang}/{ns}.json?{ver}'
            if uri not in held:
                missing.append(uri)
                continue
            body, meta = held[uri]
            f = out / 'source' / lang / f'{ns}.json'
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(body)
            files.append({'file': str(f.relative_to(out)), 'uri': uri, **meta})
            if meta['status'] == '200':
                for key, value in flat(json.loads(body)):
                    items.append({'language': lang, 'namespace': ns, 'key': key, 'value': value})
    (out / 'items.jsonl').write_text(''.join(json.dumps(i, ensure_ascii=False) + '\n' for i in items))
    counts = {}
    for i in items:
        counts[i['language']] = counts.get(i['language'], 0) + 1
    (out / 'meta.json').write_text(json.dumps({
        'structure': 'zid/dashboard-locales', 'platform': 'zid', 'surface': 'merchant dashboard (dashboard.zid.sa)',
        'namespace_map': {'run_id': code_run, 'warc': str(code_warc.relative_to(ROOT)), 'uri': entry[0], **entry[2],
                          'stated': nsmap},
        'files': files, 'missing': missing,
        'shape_observed': 'one JSON file per language and namespace, an object of nested objects whose leaves are strings '
                          '(i18next resources, loadPath /locales/{{lng}}/{{ns}}.json)',
        'counts': {'files': len(files), 'strings': counts},
        'items': 'items.jsonl: one line per string, nested keys joined with "."',
        'extractor': {'path': 'capture/structure_zid_dashboard_locales.py',
                      'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }, indent=2, ensure_ascii=False) + '\n')
    print(out, len(files), 'files', counts, 'missing', len(missing))


if __name__ == '__main__':
    main()
