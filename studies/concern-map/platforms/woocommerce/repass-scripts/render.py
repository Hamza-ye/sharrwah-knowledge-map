# Render one URL with method/capture/page_text.mjs into ../fetched/ and log it in ../fetched/log.tsv.
# Usage: python3 -I render.py URL [NAME]
import json, os, re, subprocess, sys, time, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.normpath(os.path.join(HERE, "..", "fetched"))
LOG = os.path.join(OUT, "log.tsv")
RATE = os.path.join(OUT, ".last_request_per_host.json")
PAGE_TEXT = "/home/user/sharrwah-knowledge-map/method/capture/page_text.mjs"
url = sys.argv[1]
p = urllib.parse.urlparse(url)
name = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"[^a-z0-9.]+", "_", (p.netloc + p.path).lower()).strip("_")[:150] + ".rendered.txt"
host = p.netloc.lower()
try:
    last = json.load(open(RATE))
except Exception:
    last = {}
gap = time.time() - last.get(host, 0)
if gap < 1.2:
    time.sleep(1.2 - gap)
last[host] = time.time()
json.dump(last, open(RATE, "w"))
out = os.path.join(OUT, name)
r = subprocess.run(["node", PAGE_TEXT, url, out], capture_output=True, text=True, cwd="/tmp")
try:
    rec = json.loads(r.stdout.strip().splitlines()[-1])
except Exception:
    rec = {"error": (r.stderr or r.stdout).strip()[:200]}
with open(LOG, "a", encoding="utf-8") as f:
    f.write("\t".join(str(x).replace("\t", " ") for x in [url, name if os.path.exists(out) else "", rec.get("status", ""), rec.get("fetched_at", ""),
            rec.get("text_sha256", ""), rec.get("final_url", ""), "text/plain (rendered text)", "render (method/capture/page_text.mjs)", rec.get("error", "")]) + "\n")
print(rec.get("status"), rec.get("text_chars"), out)
