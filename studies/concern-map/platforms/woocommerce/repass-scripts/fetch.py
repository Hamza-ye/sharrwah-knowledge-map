# Fetch one URL into ../fetched/ (curl, raw body) and log it in ../fetched/log.tsv.
# Usage: python3 -I fetch.py URL [NAME]
# One host gets at most about one request per second. Log columns:
# url, file, http_status, fetched_at (UTC), sha256, final_url, content_type, method, note
import hashlib, json, os, re, subprocess, sys, time, datetime, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "fetched"))
LOG = os.path.join(OUT, "log.tsv")
RATE = os.path.join(OUT, ".last_request_per_host.json")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
COLS = ["url", "file", "http_status", "fetched_at", "sha256", "final_url", "content_type", "method", "note"]
os.makedirs(OUT, exist_ok=True)

def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def wait_for_host(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    try:
        last = json.load(open(RATE))
    except Exception:
        last = {}
    gap = time.time() - last.get(host, 0)
    if gap < 1.2:
        time.sleep(1.2 - gap)
    last[host] = time.time()
    json.dump(last, open(RATE, "w"))

def log(row):
    new = not os.path.exists(LOG)
    with open(LOG, "a", encoding="utf-8") as f:
        if new:
            f.write("\t".join(COLS) + "\n")
        f.write("\t".join(str(row.get(c, "")).replace("\t", " ").replace("\n", " ") for c in COLS) + "\n")

url = sys.argv[1]
p = urllib.parse.urlparse(url)
name = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"[^a-z0-9.]+", "_", (p.netloc + p.path + ("_" + p.query if p.query else "")).lower()).strip("_")[:150]
tmp = os.path.join(OUT, name + ".body")
wait_for_host(url)
at = now()
r = subprocess.run(["curl", "-sS", "-L", "--max-redirs", "8", "--max-time", "120", "-A", UA,
                    "-H", "Accept-Language: en,ar;q=0.8", "--compressed", "-o", tmp,
                    "-w", "%{http_code}\t%{url_effective}\t%{content_type}", url], capture_output=True, text=True)
code, final, ctype = (r.stdout.split("\t") + ["", "", ""])[:3]
c = ctype.lower()
ext = ".html" if "html" in c else ".json" if "json" in c else ".xml" if "xml" in c else ".pdf" if "pdf" in c else (".md" if url.endswith((".md", ".mdx")) else ".txt") if c.startswith("text/") else ".bin"
path = os.path.join(OUT, name + ext)
if os.path.exists(tmp):
    os.replace(tmp, path)
sha = hashlib.sha256(open(path, "rb").read()).hexdigest() if os.path.exists(path) else ""
log(dict(url=url, file=os.path.basename(path) if os.path.exists(path) else "", http_status=code, fetched_at=at, sha256=sha,
         final_url=final, content_type=ctype, method="curl", note=r.stderr.strip()[:200]))
print(code, path)
