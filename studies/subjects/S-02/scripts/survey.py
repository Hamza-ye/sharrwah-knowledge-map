"""Survey items.jsonl files: row count, key union, first rows (truncated).
Usage: python3 -I survey.py <file> [n_samples] [maxlen]
"""
import json
import sys
from collections import Counter

path = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
maxlen = int(sys.argv[3]) if len(sys.argv) > 3 else 600

rows = []
with open(path, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

keys = Counter()
for r in rows:
    if isinstance(r, dict):
        keys.update(r.keys())
print(f"FILE {path}")
print(f"ROWS {len(rows)}")
print("KEYS", dict(keys))
for r in rows[:n]:
    s = json.dumps(r, ensure_ascii=False)
    print("  ", s[:maxlen] + ("..." if len(s) > maxlen else ""))
