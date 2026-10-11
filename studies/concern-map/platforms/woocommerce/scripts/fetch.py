# Fetch one URL into ../fetched/ and log it in ../fetched/log.tsv.
# Usage: python3 -I fetch.py curl URL [NAME]      raw body with curl -sS -L
#        python3 -I fetch.py render URL [NAME]    visible text via method/capture/page_text.mjs
# Waits so that one host gets at most about one request per second.
# The log columns: url, file, http_status, fetched_at (UTC), sha256, final_url, content_type, method, note
import hashlib, json, os, re, subprocess, sys, time, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "fetched"))
LOG = os.path.join(OUT, "log.tsv")
RATE = os.path.join(HERE, ".last_request_per_host.json")
PAGE_TEXT = "/home/user/sharrwah-knowledge-map/method/capture/page_text.mjs"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
COLS = ["url", "file", "http_status", "fetched_at", "sha256", "final_url", "content_type", "method", "note"]


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slug(url, suffix):
    p = urllib.parse.urlparse(url)
    s = (p.netloc + p.path + ("_" + p.query if p.query else "")).lower()
    s = re.sub(r"[^a-z0-9.]+", "_", s).strip("_")[:150]
    return s + suffix


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


def sha_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest() if os.path.exists(path) else ""


def do_curl(url, name):
    path = os.path.join(OUT, name or slug(url, ".body"))
    wait_for_host(url)
    at = now()
    p = subprocess.run(["curl", "-sS", "-L", "--max-redirs", "8", "--max-time", "120", "-A", UA,
                        "-H", "Accept-Language: en,ar;q=0.8", "--compressed", "-o", path,
                        "-w", "%{http_code}\t%{url_effective}\t%{content_type}", url],
                       capture_output=True, text=True)
    code, final, ctype = (p.stdout.split("\t") + ["", "", ""])[:3]
    note = p.stderr.strip()[:200]
    # name the file by what came back
    if not name and os.path.exists(path):
        c = ctype.lower()
        ext = ".html" if "html" in c else ".json" if "json" in c else ".xml" if "xml" in c else ".pdf" if "pdf" in c else ".txt" if c.startswith("text/") else ".bin"
        if ext == ".txt" and url.endswith(".md"):
            ext = ".md"
        base = path[:-5]
        newp = base if base.endswith(ext) else base + ext
        os.replace(path, newp)
        path = newp
    row = dict(url=url, file=os.path.relpath(path, OUT) if os.path.exists(path) else "", http_status=code, fetched_at=at,
               sha256=sha_file(path), final_url=final, content_type=ctype, method="curl", note=note)
    log(row)
    return row


def do_render(url, name):
    path = os.path.join(OUT, name or slug(url, ".rendered.txt"))
    wait_for_host(url)
    p = subprocess.run(["node", PAGE_TEXT, url, path], capture_output=True, text=True, timeout=180)
    try:
        rec = json.loads(p.stdout.strip().splitlines()[-1])
    except Exception:
        rec = {"error": (p.stderr or p.stdout).strip()[:200]}
    row = dict(url=url, file=os.path.relpath(path, OUT) if os.path.exists(path) else "", http_status=rec.get("status", ""),
               fetched_at=rec.get("fetched_at", now()), sha256=sha_file(path), final_url=rec.get("final_url", ""),
               content_type="text/plain (document.body.innerText)", method="rendered:page_text.mjs",
               note=(rec.get("error") or ("title: " + rec.get("title", "")))[:200])
    log(row)
    return row


if __name__ == "__main__":
    mode, url = sys.argv[1], sys.argv[2]
    name = sys.argv[3] if len(sys.argv) > 3 else None
    row = (do_curl if mode == "curl" else do_render)(url, name)
    print("\t".join(str(row[c]) for c in ["http_status", "file", "final_url", "content_type", "note"]))
