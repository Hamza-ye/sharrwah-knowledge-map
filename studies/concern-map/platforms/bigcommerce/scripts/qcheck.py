# Pre-check: every statement and list quote against the working copies (checker's matching rules).
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/bigcommerce/scripts")
import bcsrc, inventory, stmts
from collections import Counter
bad = 0
res = Counter()
for st in stmts.ST:
    r = bcsrc.found(st["text"], st["key"])
    res[r.split(" (")[0]] += 1
    if not r.startswith("found"):
        bad += 1
        print(f"STATEMENT C{st['c']:03d}/{st['pl']} [{st['key']}] {r}: {st['text'][:150]}")
seen = set()
for row in inventory.all_lists():
    key, quote = row[2], row[4]
    if (key, quote) in seen: continue
    seen.add((key, quote))
    r = bcsrc.found(quote, key)
    if not r.startswith("found"):
        bad += 1
        print(f"LIST {row[0]} [{key}] {r}: {quote[:150]}")
print(len(stmts.ST), "statements;", dict(res), "; problems:", bad)
