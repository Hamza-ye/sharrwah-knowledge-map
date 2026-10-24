# Print lines of a source's working copy (as the checker would see them) that match a regex. Usage: q.py URL REGEX [max]
import json, os, re, sys
Z = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid"
sys.path.insert(0, os.path.join(Z, "scripts")); import zverify
reg = json.load(open(os.path.join(Z, "fetched", "registry.json"), encoding="utf-8"))
url, pat = sys.argv[1], sys.argv[2]; mx = int(sys.argv[3]) if len(sys.argv) > 3 else 20
files = reg[url]["files"]
n = 0
for fp in files:
    raw = open(fp, encoding="utf-8", errors="replace").read()
    t = zverify.html_text(raw) if fp.endswith(".html") else raw
    for line in t.split("\n"):
        l = zverify.norm(line)
        if l and re.search(pat, l):
            print(l); n += 1
            if n >= mx: sys.exit()
    if n: break
