# Working copies for the Salla re-pass: one URL per line in a list file.
# rendered pages via method/capture/page_text.mjs; docs.salla.dev .md and other raw files via curl.
# Sequential, at least 1.5 s between requests to the same host. Every request is logged in fetched/log.tsv.
# Usage: python3 -I fetch.py LIST_FILE [rendered|raw]
import sys, os, subprocess, time, json, hashlib, urllib.parse, datetime, re
SP = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1r/salla"
PT = "/home/user/sharrwah-knowledge-map/method/capture/page_text.mjs"
OUT = f"{SP}/fetched"
LOG = f"{OUT}/log.tsv"
lst, mode = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "rendered")
last = {}
if not os.path.exists(LOG):
    open(LOG, "w").write("url\tfile\tmode\thttp_status\tfetched_at\tsha256\tnote\n")
def slug(u):
    p = urllib.parse.urlparse(u)
    s = urllib.parse.unquote(p.path).strip("/").replace("/", "_") or "index"
    s = re.sub(r"[^\w؀-ۿ.\-]+", "-", s)[-120:]
    return p.netloc, s
for u in [l.strip() for l in open(lst, encoding="utf-8") if l.strip() and not l.startswith("#")]:
    host, s = slug(u)
    os.makedirs(f"{OUT}/{host}", exist_ok=True)
    wait = 1.5 - (time.time() - last.get(host, 0))
    if wait > 0:
        time.sleep(wait)
    last[host] = time.time()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if mode == "rendered":
        f = f"{OUT}/{host}/{s}.txt"
        p = subprocess.run(["node", PT, u, f], capture_output=True, text=True, timeout=120)
        try:
            rec = json.loads(p.stdout.strip().splitlines()[-1])
        except Exception:
            rec = {"error": (p.stderr or p.stdout)[:200]}
        st = rec.get("status", "")
        sha = rec.get("text_sha256", "")
        note = rec.get("error", "") or ("final_url " + rec.get("final_url", "") if rec.get("final_url") != u else "")
    else:
        f = f"{OUT}/{host}/{s}"
        p = subprocess.run(["curl", "-sS", "-L", "-o", f, "-w", "%{http_code}", "-A",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
                            "-H", "Accept-Language: en,ar;q=0.8", u], capture_output=True, text=True, timeout=120)
        st = p.stdout.strip()
        sha = hashlib.sha256(open(f, "rb").read()).hexdigest() if os.path.exists(f) else ""
        note = p.stderr.strip()[:200]
    with open(LOG, "a") as lg:
        lg.write("\t".join([u, os.path.relpath(f, OUT), mode, str(st), now, sha, note.replace("\t", " ")]) + "\n")
    print(st, u[:120], os.path.relpath(f, OUT))
