"""Salla docs-operations: tags, scopes; events: dashboard list vs docs list."""
import json
import re
from collections import Counter, defaultdict

B = "/home/user/observed-sa/structures/salla"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


ops = load(f"{B}/docs-operations/md-openapi/items.jsonl")
tagc = Counter()
scope_re = re.compile(r"`([a-z_\.\-]+)`\s*-\s*([^\n<]+)")
by_tag = defaultdict(list)
scopes_by_tag = defaultdict(Counter)
allscopes = Counter()
noscope = 0
for o in ops:
    d = o["document"]["paths"][o["path"]][o["method"]]
    tags = d.get("tags") or []
    short = tags[-1] if tags else None
    tagc[short] += 1
    by_tag[short].append(f"{o['method'].upper()} {o['path']} ({d.get('summary')})")
    desc = d.get("description") or ""
    m = re.search(r'<Accordion title="Scopes".*?</Accordion>', desc, re.S)
    if m:
        sc = scope_re.findall(m.group(0))
        for s, lab in sc:
            scopes_by_tag[short][s] += 1
            allscopes[s] += 1
    else:
        noscope += 1
print("TAGS", len(tagc))
for t, n in sorted(tagc.items(), key=lambda x: -x[1]):
    print(f"  {t}: {n} | scopes {dict(scopes_by_tag[t])}")
print("ops without scopes accordion", noscope)
print("DISTINCT SCOPES", len(allscopes), sorted(allscopes))
print("first-tag folders", Counter((o["document"]["paths"][o["path"]][o["method"]].get("tags") or ["?"])[0].rsplit("/", 1)[0] for o in ops))
import sys
for t in sys.argv[1:]:
    print("== OPS for tag", t)
    for x in by_tag.get(t, []):
        print("   ", x)
