# Fetch one or more URLs as working copies into <output>/fetched/ and log each fetch.
# Usage: python3 -I fetch.py [--render] URL [URL ...]
#   default: curl -sS -L (for .md endpoints, raw files, HTML that holds its text)
#   --render: node page_text.mjs URL OUT_TXT (rendered visible text)
# Log columns: url, file, http_status, fetched_at (UTC), sha256
import hashlib, json, os, re, subprocess, sys, time, datetime, urllib.parse

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FETCHED = os.path.join(OUT, "fetched")
LOG = os.path.join(FETCHED, "log.tsv")
PAGE_TEXT = "/home/user/sharrwah-knowledge-map/method/capture/page_text.mjs"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

os.makedirs(FETCHED, exist_ok=True)
if not os.path.exists(LOG):
    with open(LOG, "w") as fh:
        fh.write("url\tfile\thttp_status\tfetched_at\tsha256\n")

def slug(url, suffix):
    p = urllib.parse.urlparse(url)
    host = p.netloc.lower()
    path = (p.path or "/").strip("/")
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", host + "_" + path)
    if p.query:
        s += "_q_" + re.sub(r"[^A-Za-z0-9._-]+", "_", p.query)
    s = s[:180]
    return s + suffix

def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def log(url, fname, status, ts, sha):
    with open(LOG, "a") as fh:
        fh.write("\t".join([url, fname, str(status), ts, sha]) + "\n")

def fetch_curl(url):
    fname = slug(url, "")
    if not re.search(r"\.(md|txt|html|json|xml|pdf)$", fname):
        fname += ".body"
    path = os.path.join(FETCHED, fname)
    ts = now()
    p = subprocess.run(["curl", "-sS", "-L", "--max-redirs", "8", "--max-time", "120", "-A", UA,
                        "-H", "Accept-Language: en", "--compressed", "-o", path,
                        "-w", "%{http_code} %{url_effective}", url], capture_output=True, text=True)
    parts = p.stdout.strip().split(" ", 1)
    status = parts[0] or "000"
    final_url = parts[1] if len(parts) > 1 else ""
    if p.returncode != 0:
        status = f"{status} curl_exit={p.returncode} {p.stderr.strip()[:120]}".replace("\t", " ").replace("\n", " ")
    sha = ""
    if os.path.exists(path):
        sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    log(url, fname if os.path.exists(path) else "", status, ts, sha)
    print(json.dumps({"url": url, "final_url": final_url, "file": fname, "status": status, "sha256": sha,
                      "bytes": os.path.getsize(path) if os.path.exists(path) else 0}))

def fetch_render(url):
    fname = slug(url, ".rendered.txt")
    path = os.path.join(FETCHED, fname)
    ts = now()
    p = subprocess.run(["node", PAGE_TEXT, url, path], capture_output=True, text=True, timeout=200)
    rec = {}
    try:
        rec = json.loads(p.stdout.strip().splitlines()[-1])
    except Exception:
        rec = {"error": (p.stderr or p.stdout)[:200]}
    status = str(rec.get("status")) if rec.get("status") is not None else ("err " + str(rec.get("error", ""))[:120])
    status = status.replace("\t", " ").replace("\n", " ")
    sha = ""
    if os.path.exists(path):
        sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    log(url, fname if os.path.exists(path) else "", status, rec.get("fetched_at", ts), sha)
    print(json.dumps({"url": url, "file": fname, "status": status, "sha256": sha,
                      "final_url": rec.get("final_url"), "title": rec.get("title"),
                      "chars": rec.get("text_chars")}))

args = sys.argv[1:]
render = False
if args and args[0] == "--render":
    render = True
    args = args[1:]
last_host_time = {}
for u in args:
    host = urllib.parse.urlparse(u).netloc
    t = last_host_time.get(host)
    if t is not None:
        wait = 1.1 - (time.time() - t)
        if wait > 0:
            time.sleep(wait)
    (fetch_render if render else fetch_curl)(u)
    last_host_time[host] = time.time()
    time.sleep(1.0)
