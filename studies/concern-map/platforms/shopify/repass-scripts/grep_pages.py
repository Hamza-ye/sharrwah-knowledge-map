# Search the captured pages (and this run's working copies) for a regex; print URL and matching sentence-ish spans.
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
pat = re.compile(sys.argv[1], re.I)
only = sys.argv[2] if len(sys.argv) > 2 else ""
width = int(sys.argv[3]) if len(sys.argv) > 3 else 260
urls = sorted(MANIFEST)
for url in urls:
    if only and only not in url:
        continue
    cap, r = MANIFEST[url]
    fp = os.path.join(cap, r["dir"], "text.txt")
    if not os.path.exists(fp):
        fp = os.path.join(cap, r["dir"], r["primary_file"])
    txt = open(fp, encoding="utf-8", errors="replace").read()
    for m in pat.finditer(txt):
        a = max(0, m.start() - width // 2); b = min(len(txt), m.end() + width // 2)
        print(url.replace("https://", ""), "::", txt[a:b].replace("\n", " / "))
log = os.path.join(BASE, "fetched", "log.tsv")
for r in rd(log):
    if only and only not in r["url"]:
        continue
    fp = os.path.join(BASE, "fetched", r["out"])
    if os.path.exists(fp):
        txt = open(fp, encoding="utf-8", errors="replace").read()
        for m in pat.finditer(txt):
            a = max(0, m.start() - width // 2); b = min(len(txt), m.end() + width // 2)
            print("WC:" + r["url"].replace("https://", ""), "::", txt[a:b].replace("\n", " / "))
