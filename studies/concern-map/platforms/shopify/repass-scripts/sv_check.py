import sys, os, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
cand = rd(os.path.join(BASE, 'candidates.tsv'))
dec = {}
for line in open(os.path.join(WORK, 'decisions', 'router.txt')):
    if line.startswith('#') or not line.strip(): continue
    i, a, to, why = line.rstrip('\n').split('|', 3)
    dec[int(i)] = (a, to, why)
def keys_of(stmt):
    obj = json.loads(stmt[len('"eligibility":'):])
    out = set()
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ('entitlements', 'features') and isinstance(v, list):
                    out.update((k, x) for x in v)
                elif isinstance(v, (dict, list)): walk(v)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(obj); return out
kept_keys = collections.defaultdict(set)
for i, x in enumerate(cand):
    if x['join'] == 'router-eligibility':
        a, to, why = dec.get(i, ('k', '', ''))
        ks = keys_of(x['statement'])
        if a == 'k': kept_keys[x['concern_id']] |= ks
        if to: kept_keys[to] |= ks
for i, x in enumerate(cand):
    if x['join'] == 'store-values':
        kind, key = x['identifier'].split('.', 1)
        ok = (kind, key) in kept_keys[x['concern_id']]
        targets = sorted(c for c, ks in kept_keys.items() if (kind, key) in ks and c != x['concern_id'])
        print(i, x['concern_id'], x['identifier'], 'KEEP' if ok else 'DROP', targets, x['statement'][-60:])
