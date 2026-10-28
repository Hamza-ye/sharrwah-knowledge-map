"""Hold, in the run, every JSON answer the run's own pages received, and every write they sent.

    python3 capture/answers.py <platform> [--all | <run-id> ...]

Default: every finished browser run of <platform> with no answers.jsonl yet (a run does not change after it ends);
--all writes every such run again.

Reads the run's trace.zip (or its parts, trace.zip.00, .01, ..., when it was cut to stay under GitHub's 100 MB
limit for one file): the calls of the pages the run acted on (the pages its .trace members hold snapshots of),
from its .network members, with their bodies from resources/. Writes each JSON response body exactly as received:
  <platform>/raw/runs/<run>/answers/<host>/<path>/<sha256>.json   an answer, under its request path
  <platform>/raw/runs/<run>/answers.jsonl   one row per answer: file, host, method, path, bytes, calls (step, between,
                                            t, status, query, request_body, trace_request, trace_response)
A call is JSON when its response's type names json, or its body parses as JSON and starts with { or [. Calls with
the same host, method, path and JSON content (keys in any order) are one row, held as the first received. A write (a
method other than GET, HEAD or OPTIONS) whose response is not JSON is a row of its own with file null, so every
write the pages sent is listed. A call belongs to the step whose [t_start, t_end] holds its start, or to the step
before it (between: true; step 0 = before the first step). request_body is the body as sent (text up to 200,000
characters; a longer one is named by its trace_request only).
"""
import hashlib
import io
import json
import re
import shutil
import sys
import zipfile
from bisect import bisect_right
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
READS = {'GET', 'HEAD', 'OPTIONS'}


def trace_zip(run):
    """The run's trace: trace.zip, or the parts it was cut into in order (trace.zip.00, trace.zip.01, ...)."""
    if (run / 'trace.zip').exists():
        return zipfile.ZipFile(run / 'trace.zip')
    parts = sorted(run.glob('trace.zip.[0-9][0-9]'))
    return zipfile.ZipFile(io.BytesIO(b''.join(p.read_bytes() for p in parts))) if parts else None


def safe(part):
    return re.sub(r'[^A-Za-z0-9_.@=-]', '_', part).strip('_') or '_'


def content_key(data):
    try:
        return hashlib.sha256(json.dumps(json.loads(data), sort_keys=True, ensure_ascii=False).encode('utf-8', 'surrogatepass')).hexdigest()
    except ValueError:
        return hashlib.sha256(data).hexdigest()


def is_json(mime, data):
    if data is None:
        return False
    if 'json' in (mime or '').lower():
        return True
    head = data.lstrip()[:1]
    if head not in (b'{', b'['):
        return False
    try:
        json.loads(data)
        return True
    except ValueError:
        return False


def run_answers(run):
    out = run / 'answers'
    if out.exists():
        shutil.rmtree(out)
    steps = [json.loads(l) for l in open(run / 'actions.jsonl') if l.strip()] if (run / 'actions.jsonl').exists() else []
    starts = [s['t_start'] for s in steps]
    z = trace_zip(run)
    names = set(z.namelist())

    def res(f):
        n = f if f.startswith('resources/') else 'resources/' + f
        return z.read(n) if n in names else None

    own = set()
    for name in names:
        if name.endswith('.trace'):
            for line in io.TextIOWrapper(z.open(name), encoding='utf-8'):
                if '"frame-snapshot"' in line:
                    ev = json.loads(line)
                    if ev.get('type') == 'frame-snapshot' and (ev.get('snapshot') or {}).get('pageId'):
                        own.add(ev['snapshot']['pageId'])
    groups, rows = {}, []
    for name in sorted(names):
        if not name.endswith('.network'):
            continue
        for line in io.TextIOWrapper(z.open(name), encoding='utf-8'):
            if not line.strip():
                continue
            e = json.loads(line).get('snapshot')
            if not e or e.get('pageref') not in own:
                continue
            req, resp = e['request'], e['response']
            method = req['method']
            u = urlsplit(req['url'])
            c = resp.get('content') or {}
            data = res(c['_file']) if c.get('_file') else None
            json_body = is_json(c.get('mimeType'), data)
            if not json_body and method in READS:
                continue
            pd = req.get('postData') or {}
            body = pd.get('text') or None
            if body is None and pd.get('_file'):
                raw = res(pd['_file'])
                body = raw.decode('utf-8', 'replace') if raw is not None else None
            if body is not None and len(body) > 200000:
                body = None
            t0 = e['startedDateTime']
            i = bisect_right(starts, t0)
            call = {'step': steps[i - 1]['step'] if i else 0, 'between': bool(i) and t0 > (steps[i - 1].get('t_end') or t0),
                    't': t0, 'status': resp.get('status'), 'query': u.query or None,
                    **({'request_body': body} if method not in READS else {}),
                    'trace_request': pd.get('_file'), 'trace_response': c.get('_file')}
            if not json_body:
                rows.append({'file': None, 'host': u.hostname, 'method': method, 'path': u.path, 'mime': c.get('mimeType'),
                             'bytes': len(data) if data is not None else None, 'calls': [call]})
                continue
            k = (u.hostname, method, u.path, content_key(data))
            g = groups.get(k)
            if not g:
                sha = hashlib.sha256(data).hexdigest()
                sub = [safe(p) for p in u.path.split('/') if p] or ['_']
                f = out.joinpath(safe(u.hostname), *sub, f'{sha}.json')
                if not f.exists():
                    f.parent.mkdir(parents=True, exist_ok=True)
                    f.write_bytes(data)
                g = groups[k] = {'file': str(f.relative_to(run)), 'host': u.hostname, 'method': method, 'path': u.path,
                                 'bytes': len(data), 'calls': []}
                rows.append(g)
            g['calls'].append(call)
    (run / 'answers.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
    return rows


def main():
    platform, rest = sys.argv[1], sys.argv[2:]
    runs = ROOT / platform / 'raw' / 'runs'
    every = '--all' in rest
    names = [a for a in rest if a != '--all'] or sorted(
        p.name for p in runs.iterdir() if (p / 'run.json').exists()
        and ((p / 'trace.zip').exists() or (p / 'trace.zip.00').exists())
        and (every or not (p / 'answers.jsonl').exists()))
    for name in names:
        rows = run_answers(runs / name)
        held = [r for r in rows if r['file']]
        print(name, '| answers', len(held), '| MB', round(sum(r['bytes'] for r in held) / 1e6, 1),
              '| calls', sum(len(r['calls']) for r in rows),
              '| writes', sum(1 for r in rows for _ in r['calls'] if r['method'] not in READS), flush=True)


if __name__ == '__main__':
    main()
