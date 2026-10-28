"""Regenerate <platform>/index/runs.tsv from <platform>/raw/runs/*/run.json plus <platform>/index/run-notes.tsv (the
one place a person annotates a run), and <platform>/index/SHA256SUMS for every file of every finished run, so each
run's bytes can be verified later (`sha256sum -c <platform>/index/SHA256SUMS` from the repository root).

    python3 capture/runs_index.py <platform>
"""
import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    platform = sys.argv[1]
    runs, index = ROOT / platform / 'raw' / 'runs', ROOT / platform / 'index'
    index.mkdir(parents=True, exist_ok=True)
    notes = {}
    nf = index / 'run-notes.tsv'
    if nf.exists():
        with open(nf, newline='') as f:
            for row in csv.DictReader(f, delimiter='\t'):
                notes.setdefault(row['run_id'], []).append(row['note'])

    rows, sums = [], []
    for d in sorted(p for p in runs.iterdir() if p.is_dir()) if runs.is_dir() else []:
        meta = json.loads((d / 'run.json').read_text()) if (d / 'run.json').exists() else {}
        files = sorted(p for p in d.rglob('*') if p.is_file() and p.name != 'last.json')
        steps = sum(1 for _ in open(d / 'actions.jsonl')) if (d / 'actions.jsonl').exists() else ''
        rows.append({
            'run_id': d.name, 'kind': meta.get('kind', ''), 'label': meta.get('label', ''),
            'started': meta.get('started', ''), 'ended': meta.get('ended', ''),
            'steps_or_urls': steps if steps != '' else meta.get('url_count', ''),
            'files': len(files), 'bytes': sum(p.stat().st_size for p in files),
            'script': (meta.get('script') or {}).get('path', ''), 'script_sha256': (meta.get('script') or {}).get('sha256', ''),
            'tool': meta.get('tool') or (f"playwright-core {meta.get('playwright_core')} / Chrome {meta.get('browser_version')}" if meta.get('playwright_core') else ''),
            'network': ' '.join(f"{k}={(meta.get('network') or {}).get(k)}" for k in ('loc', 'colo')) if meta.get('network') else '',
            'complete': 'yes' if meta else 'no (no run.json)',
            'notes': ' | '.join(notes.get(d.name, [])),
        })
        if meta:  # runs still in progress are listed but not hashed yet
            sums.extend(f'{sha256(p)}  {p.relative_to(ROOT)}' for p in files)

    cols = ['run_id', 'kind', 'label', 'started', 'ended', 'steps_or_urls', 'files', 'bytes', 'script', 'script_sha256',
            'tool', 'network', 'complete', 'notes']
    with open(index / 'runs.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    (index / 'SHA256SUMS').write_text(''.join(s + '\n' for s in sums))
    unknown = sorted(set(notes) - {r['run_id'] for r in rows})
    print(f'runs: {len(rows)}  files hashed: {len(sums)}  notes for missing runs: {unknown}', file=sys.stderr)


if __name__ == '__main__':
    main()
