import json, os, sys
Z = sys.argv[1]; sys.path.insert(0, os.path.join(Z, "scripts")); import zverify
reg = json.load(open(os.path.join(Z, "fetched", "registry.json"), encoding="utf-8"))
reg["https://zid.sa/sitemap.xml"] = {"files": [os.path.join(Z, "fetched", "site", "sitemap.xml")]}
inv = json.load(open(os.path.join(Z, "fetched", "inventory.json"), encoding="utf-8"))
bad = 0
from collections import Counter
c = Counter()
for e in inv:
    files = reg.get(e["url"], {}).get("files")
    if not files: print("NO SOURCE", e["url"]); bad += 1; continue
    r = zverify.check(e["quote"], files); c[r] += 1
    if not r.startswith("found"): bad += 1; print("NOT FOUND", e["inv_id"], e["list"], e["quote"][:100])
print(c, "bad", bad)
