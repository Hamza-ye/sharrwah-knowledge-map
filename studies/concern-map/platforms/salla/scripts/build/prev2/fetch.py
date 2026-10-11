# Fetch pages one at a time, keep working copies in OUT/fetched/<host>/, and log each fetch.
# Modes:
#   md       curl the URL as served (docs.salla.dev .md twins, raw files)
#   rendered node page_text.mjs URL OUT_TXT (rendered visible text)
# Usage: python3 -I fetch.py MODE URL [URL ...]
# Log: OUT/fetched/log.tsv  (url, file, http_status, fetched_at, sha256)
# Rate: at least MIN_GAP seconds between requests to the same host, strictly sequential.
import sys, os, re, json, time, hashlib, subprocess, datetime, urllib.parse

OUT = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1/salla"
FETCHED = os.path.join(OUT, "fetched")
LOG = os.path.join(FETCHED, "log.tsv")
PAGE_TEXT = "/home/user/sharrwah-knowledge-map/method/capture/page_text.mjs"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
MIN_GAP = 1.5
STATE = os.path.join(OUT, "scripts", ".last_hit.json")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def wait_for(host):
    try:
        last = json.load(open(STATE))
    except Exception:
        last = {}
    t = last.get(host, 0)
    gap = time.time() - t
    if gap < MIN_GAP:
        time.sleep(MIN_GAP - gap)
    last[host] = time.time()
    json.dump(last, open(STATE, "w"))


def local_name(url, mode):
    p = urllib.parse.urlparse(url)
    host = p.netloc.lower()
    path = urllib.parse.unquote(p.path)
    segs = [s for s in path.split("/") if s]
    if host == "help.salla.sa" and len(segs) >= 2 and segs[0] in ("article", "category"):
        base = ("en-" if "/en/" in url else "") + segs[0] + "-" + segs[-1]
    elif host == "help.salla.sa" and len(segs) >= 3 and segs[0] == "en" and segs[1] in ("article", "category"):
        base = "en-" + segs[1] + "-" + segs[-1]
    else:
        base = "_".join(segs) or "index"
        base = re.sub(r"[^A-Za-z0-9._-]", "-", base)
        if len(base) > 120:
            base = base[:100] + "-" + hashlib.sha1(url.encode()).hexdigest()[:10]
    if p.query:
        base += "_q-" + hashlib.sha1(p.query.encode()).hexdigest()[:8]
    ext = ".txt" if mode == "rendered" else ""
    if mode == "md" and not os.path.splitext(base)[1]:
        ext = ".body"
    d = os.path.join(FETCHED, host)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, base + ext)


def log(url, path, status, at):
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest() if path and os.path.exists(path) else ""
    rel = os.path.relpath(path, FETCHED) if path and os.path.exists(path) else ""
    with open(LOG, "a", encoding="utf-8") as f:
        f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in (url, rel, status, at, sha)) + "\n")
    return sha


def fetch_md(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    wait_for(host)
    out = local_name(url, "md")
    at = now()
    p = subprocess.run(["curl", "-sS", "-L", "--max-redirs", "5", "--max-time", "90", "-A", UA,
                        "-H", "Accept-Language: ar,en;q=0.8", "--compressed", "-o", out,
                        "-w", "%{http_code}", url], capture_output=True, text=True)
    status = p.stdout.strip() or ("curl-exit-%d %s" % (p.returncode, p.stderr.strip()[:80]))
    if not os.path.exists(out) or os.path.getsize(out) == 0:
        if os.path.exists(out):
            os.remove(out)
        out = ""
    sha = log(url, out, status, at)
    print(json.dumps({"url": url, "status": status, "file": out, "sha256": sha}, ensure_ascii=False))


def fetch_rendered(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    wait_for(host)
    out = local_name(url, "rendered")
    p = subprocess.run(["node", PAGE_TEXT, url, out], capture_output=True, text=True, timeout=180,
                       cwd=os.path.join(OUT, "scripts"))
    try:
        rec = json.loads(p.stdout.strip().splitlines()[-1])
    except Exception:
        rec = {"error": (p.stderr or p.stdout).strip()[:200], "fetched_at": now()}
    status = rec.get("status") or ("error: " + str(rec.get("error", ""))[:120])
    if not os.path.exists(out):
        out = ""
    sha = log(url, out, status, rec.get("fetched_at", now()))
    print(json.dumps({"url": url, "status": status, "final_url": rec.get("final_url"), "title": rec.get("title"),
                      "chars": rec.get("text_chars"), "file": out, "sha256": sha}, ensure_ascii=False))


if __name__ == "__main__":
    mode = sys.argv[1]
    for u in sys.argv[2:]:
        try:
            (fetch_md if mode == "md" else fetch_rendered)(u)
        except Exception as e:
            print(json.dumps({"url": u, "error": str(e)[:200]}))
