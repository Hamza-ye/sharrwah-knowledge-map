# Phase 1: fetch each cited web URL as served (curl), keep body, headers and transfer facts.
# Usage: python3 -I fetch_raw.py ITEMS_JSON RUN_DIR
import json, os, re, subprocess, sys, hashlib, datetime, urllib.parse
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
items = [i for i in json.load(open(sys.argv[1], encoding="utf-8")) if i["kind"] == "web"]
run = sys.argv[2]

def slug(it):
    host = urllib.parse.urlparse(it["url"]).netloc.lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    return f'{it["n"]:03d}-{re.sub(r"[^a-z0-9.-]", "-", host)}'

def ext_for(ctype):
    c = (ctype or "").lower()
    if "pdf" in c: return "pdf"
    if "html" in c: return "html"
    if "json" in c: return "json"
    if "xml" in c: return "xml"
    if c.startswith("text/"): return "txt"
    if "image/" in c: return c.split("image/")[1].split(";")[0].strip() or "img"
    return "bin"

def fetch(it):
    d = os.path.join(run, "items", slug(it))
    os.makedirs(d, exist_ok=True)
    body, hdr = os.path.join(d, "raw.body"), os.path.join(d, "headers.txt")
    started = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    p = subprocess.run(["curl", "-sS", "-L", "--max-redirs", "8", "--max-time", "150", "-A", UA,
                        "-H", "Accept-Language: " + os.environ.get("CAPTURE_LANG", "ar,en;q=0.8"), "--compressed",
                        "-D", hdr, "-o", body,
                        "-w", '{"code":%{http_code},"final":"%{url_effective}","ctype":"%{content_type}","bytes":%{size_download}}',
                        it["url"]], capture_output=True, text=True)
    try:
        w = json.loads(p.stdout)
    except Exception:
        w = {"code": 0, "final": "", "ctype": "", "bytes": 0}
    rec = dict(n=it["n"], url=it["url"], dir=os.path.relpath(d, run), fetched_at=started,
               curl_exit=p.returncode, curl_error=p.stderr.strip()[:200], http_code=w["code"],
               final_url=w["final"], content_type=w["ctype"], bytes=w["bytes"], cited_in=it["cited_in"])
    if os.path.exists(body) and os.path.getsize(body) > 0:
        ext = ext_for(w["ctype"])
        # PDFs served with a generic type still start with %PDF
        with open(body, "rb") as fh:
            if fh.read(5) == b"%PDF-": ext = "pdf"
        final = os.path.join(d, f"raw.{ext}")
        os.replace(body, final)
        rec["raw_file"] = os.path.basename(final)
        rec["sha256"] = hashlib.sha256(open(final, "rb").read()).hexdigest()
        rec["raw_ext"] = ext
    else:
        if os.path.exists(body): os.remove(body)
        rec["raw_file"], rec["sha256"], rec["raw_ext"] = "", "", ""
    json.dump(rec, open(os.path.join(d, "fetch.json"), "w"), ensure_ascii=False, indent=1)
    return rec

with ThreadPoolExecutor(max_workers=int(os.environ.get("CAPTURE_WORKERS", "6"))) as ex:
    recs = list(ex.map(fetch, items))
json.dump(recs, open(os.path.join(run, "phase1.json"), "w"), ensure_ascii=False, indent=0)
ok = sum(1 for r in recs if 200 <= r["http_code"] < 300 and r["raw_file"])
print(f"fetched {len(recs)}; 2xx with body {ok}; other {len(recs) - ok}")
