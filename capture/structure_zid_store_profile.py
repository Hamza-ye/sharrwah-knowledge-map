"""Hold, from one answer to GET hermod.zid.sa/v1/managers/account/profile, the store's plan policies and the signed-in
user's permissions as two structures:
  zid/structures/store-plan-policies/   items.jsonl: one policy per line, in the answer's order: key, then the entry
                                        as stated in user.store.subscription.policies_v2 (enabled, config,
                                        available_in), with the value of the same key in subscription.policies
  zid/structures/store-permissions/     items.jsonl: user.permissions, one per line as stated (id, slug, name,
                                        description, order, relies_on, package_restrictions), with user.roles in meta

    python3 capture/structure_zid_store_profile.py <run-id>

The answer is the first one the run holds for that path (its answers.jsonl). Each meta.json names the answer file,
the call (step, time) and the subscription it belongs to (package_code, package_name, expired_at).
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = '/v1/managers/account/profile'


def main():
    run_id = sys.argv[1]
    run = ROOT / 'zid' / 'raw' / 'runs' / run_id
    row = next(r for r in map(json.loads, open(run / 'answers.jsonl')) if r['path'] == PATH and r['file'])
    f = run / row['file']
    user = json.loads(f.read_bytes())['user']
    sub = user['store']['subscription']
    source = {'run_id': run_id, 'answer': str(f.relative_to(ROOT)), 'host': row['host'], 'method': row['method'],
              'path': row['path'], 'first_call': {k: row['calls'][0][k] for k in ('step', 't', 'status')},
              'sha256': hashlib.sha256(f.read_bytes()).hexdigest()}
    store = {'store_id': user['store']['id'], 'store_title': user['store']['title'],
             'subscription': {k: sub.get(k) for k in ('package_code', 'package_key', 'package_name', 'subscribed_at',
                                                       'expired_at', 'is_trial', 'tier')}}
    extractor = {'path': 'capture/structure_zid_store_profile.py', 'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

    out = ROOT / 'zid' / 'structures' / 'store-plan-policies'
    out.mkdir(parents=True, exist_ok=True)
    items = [{'key': k, **v, 'policies': sub.get('policies', {}).get(k)} for k, v in sub.get('policies_v2', {}).items()]
    (out / 'items.jsonl').write_text(''.join(json.dumps(i, ensure_ascii=False) + '\n' for i in items))
    (out / 'meta.json').write_text(json.dumps({
        'structure': 'zid/store-plan-policies', 'platform': 'zid', 'surface': 'merchant API (hermod.zid.sa), as the dashboard reads it',
        'source': source, 'of': store,
        'shape_observed': 'user.store.subscription.policies_v2: object keyed by policy key ("<feature>" or '
                          '"<feature>.<part>"), each {enabled, config, available_in: {ar, en, package_key} or []}; '
                          'user.store.subscription.policies: object keyed by policy key, each a boolean',
        'counts': {'policies_v2': len(items), 'policies': len(sub.get('policies', {})),
                   'enabled': sum(1 for i in items if i.get('enabled'))},
        'extractor': extractor,
    }, indent=2, ensure_ascii=False) + '\n')

    out = ROOT / 'zid' / 'structures' / 'store-permissions'
    out.mkdir(parents=True, exist_ok=True)
    perms = user.get('permissions', [])
    (out / 'items.jsonl').write_text(''.join(json.dumps(p, ensure_ascii=False) + '\n' for p in perms))
    (out / 'meta.json').write_text(json.dumps({
        'structure': 'zid/store-permissions', 'platform': 'zid', 'surface': 'merchant API (hermod.zid.sa), as the dashboard reads it',
        'source': source, 'of': store, 'roles': user.get('roles'),
        'shape_observed': 'user.permissions: list of {id, slug, name, description, order, relies_on, '
                          'package_restrictions: [{package_key, names}]}, the signed-in user\'s permissions',
        'counts': {'permissions': len(perms), 'with_package_restrictions': sum(1 for p in perms if p.get('package_restrictions'))},
        'extractor': extractor,
    }, indent=2, ensure_ascii=False) + '\n')
    print(len(items), 'policies;', len(perms), 'permissions')


if __name__ == '__main__':
    main()
