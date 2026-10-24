# Print lines of a source's working copy that match a regex, BOMs removed, odd characters shown.
# Usage: python3 -I grab.py KEY REGEX [MAXLEN]
import sys, re
sys.path.insert(0, "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/bigcommerce/scripts")
import bcsrc
key, rx = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 400
_, files, _, _, _ = bcsrc.resolve(key)
for fp in files:
    if not fp.endswith((".txt", ".md")): continue
    for i, l in enumerate(open(fp, encoding="utf-8", errors="replace"), 1):
        l = l.rstrip("\n").replace("﻿", "")
        if re.search(rx, l):
            odd = sorted({c for c in l if ord(c) > 126 and c not in "—–’‘“”é"})
            print(f"{fp.split('/')[-1]}:{i}: {l[:mx]}" + (f"   [odd: {' '.join(hex(ord(c)) for c in odd)}]" if odd else ""))
