# Phase 4: PDF text, duplicate removal, date hints and the run manifest.
# Usage: python3 -I finalize.py RUN_DIR [SKIP_JSON]
# SKIP_JSON maps a URL substring to the reason it was deliberately not fetched.
import json, os, re, subprocess, sys, hashlib, html

run = sys.argv[1]
p1 = {x["n"]: x for x in json.load(open(os.path.join(run, "phase1.json")))}
p2 = {x["n"]: x for x in json.load(open(os.path.join(run, "phase2.json")))}
p3 = {x["n"]: x for x in json.load(open(os.path.join(run, "phase3.json")))} if os.path.exists(os.path.join(run, "phase3.json")) else {}
SKIP = json.load(open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else {}

def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def first(pattern, text, flags=re.I):
    m = re.search(pattern, text, flags)
    return m.group(1) if m else None

def html_dates(text):
    pats = [
        ("meta:published", r'<meta[^>]+(?:property|name|itemprop)=["\'](?:article:published_time|og:published_time|datePublished|pubdate|publishdate|DC\.date\.issued|date)["\'][^>]*content=["\']([^"\']{8,40})'),
        ("meta:published", r'<meta[^>]+content=["\']([^"\']{8,40})["\'][^>]*(?:property|name|itemprop)=["\'](?:article:published_time|og:published_time|datePublished|pubdate|publishdate)["\']'),
        ("jsonld:published", r'"datePublished"\s*:\s*"([^"]{8,40})"'),
        ("time-tag", r'<time[^>]+datetime=["\']([^"\']{8,40})'),
        ("meta:modified", r'<meta[^>]+(?:property|name|itemprop)=["\'](?:article:modified_time|og:updated_time|dateModified|last-modified)["\'][^>]*content=["\']([^"\']{8,40})'),
        ("jsonld:modified", r'"dateModified"\s*:\s*"([^"]{8,40})"'),
    ]
    for src, p in pats:
        v = first(p, text)
        if v and re.match(r"(19|20)\d\d", v.strip()):
            return v.strip()[:10], src
    return None, None

def url_date(u):
    m = re.search(r"/(20\d\d)[/-](\d{1,2})[/-](\d{1,2})(?:/|$|-)", u)
    if m: return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}", "url"
    m = re.search(r"/(20\d\d)/(\d{1,2})/", u)
    if m and 1 <= int(m.group(2)) <= 12: return f"{m.group(1)}-{int(m.group(2)):02d}", "url"
    return None, None

def pdf_date(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, errors="replace").stdout
    for key in ("CreationDate", "ModDate"):
        m = re.search(rf"^{key}:\s+(.+)$", out, re.M)
        if m:
            y = re.search(r"((19|20)\d\d)", m.group(1))
            if y:
                mon = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b", m.group(1))
                return (y.group(1) + (f" {mon.group(1)}" if mon else "")), f"pdf:{key}"
    return None, None

def age(year):
    if not year: return "undated"
    y = int(year)
    if y >= 2025: return "2025-2026"
    if y >= 2023: return "2023-2024"
    return "before-2023"

seen, rows = {}, []
for n in sorted(p1):
    a, b, c = p1[n], p2.get(n, {}), p3.get(n, {})
    d = os.path.join(run, a["dir"])
    row = dict(n=n, url=a["url"], dir=a["dir"], fetched_at=a["fetched_at"], http_raw=a["http_code"] or "",
               http_browser=b.get("status") or "", final_url=b.get("final_url") or a["final_url"], content_type=a["content_type"],
               cited_in=" ".join(a["cited_in"]), note="")
    skip = next((v for k, v in SKIP.items() if k in a["url"]), None)
    raw_ok = 200 <= a["http_code"] < 300 and a["raw_file"]
    br_ok = (not b.get("error")) and b.get("status") and b["status"] < 400 and b.get("text_chars", 0) > 0
    primary = None
    if raw_ok: primary = a["raw_file"]
    elif b.get("browser_body") and br_ok: primary = b["browser_body"]
    elif br_ok: primary = "rendered.html"
    elif c.get("encoded_file"): primary = c["encoded_file"]
    elif c.get("archive_file"): primary = c["archive_file"]
    # PDF text for reading
    if primary and primary.endswith(".pdf") and os.path.exists(os.path.join(d, primary)):
        t = os.path.join(d, "text.txt")
        if not os.path.exists(t):
            subprocess.run(["pdftotext", "-layout", os.path.join(d, primary), t], capture_output=True)
    title = b.get("title", "") or ""
    text_chars = b.get("text_chars", 0) or 0
    if skip:
        row["result"], row["note"] = "skipped", skip
    elif primary and re.search(r"maintenance|hugedomains", (row["final_url"] or "") + " " + title, re.I):
        row["result"], row["note"] = "gone", f"page now shows: {title or row['final_url']}"
    elif primary and primary.startswith("archive"):
        row["result"], row["note"] = "captured from archive", f"Wayback Machine snapshot {c.get('archive_timestamp', '')}"
    elif primary:
        row["result"] = "captured"
        if not raw_ok: row["note"] = "raw fetch refused; captured through the browser"
        if primary.endswith("html") and br_ok and text_chars < 400: row["note"] = (row["note"] + "; " if row["note"] else "") + f"little visible text ({text_chars} characters)"
    elif a["http_code"] in (404, 410):
        row["result"] = "gone"
        row["note"] = f"HTTP {a['http_code']}"
    else:
        row["result"] = "blocked from here"
        row["note"] = (f"HTTP {a['http_code']}" if a["http_code"] else a["curl_error"][:80]) + (f"; browser: {b.get('error') or b.get('status')}" if b else "")
    # duplicates: keep the first copy, point later ones at it
    row["primary_file"], row["sha256"], row["bytes"] = primary or "", "", ""
    if primary and os.path.exists(os.path.join(d, primary)):
        h = sha(os.path.join(d, primary)); row["sha256"] = h; row["bytes"] = os.path.getsize(os.path.join(d, primary))
        if h in seen and primary.endswith(".pdf"):
            os.remove(os.path.join(d, primary))
            open(os.path.join(d, "duplicate-of.txt"), "w").write(seen[h] + "/" + primary + "\n")
            row["note"] = (row["note"] + "; " if row["note"] else "") + f"same file as {seen[h]}"
            row["primary_file"] = f"../{seen[h]}/{primary}"
        else:
            seen.setdefault(h, a["dir"])
    # date hint
    date, src = url_date(a["url"])
    if not date and primary:
        p = os.path.join(d, primary) if not row["primary_file"].startswith("..") else None
        if primary.endswith(".pdf") and p and os.path.exists(p):
            date, src = pdf_date(p)
        else:
            for f in ("rendered.html", "raw.html", primary):
                fp = os.path.join(d, f)
                if os.path.exists(fp) and f.endswith("html"):
                    date, src = html_dates(open(fp, encoding="utf-8", errors="replace").read())
                    if date: break
    if not date and c.get("archive_timestamp"):
        ts = c["archive_timestamp"]; date, src = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", "archive-snapshot (latest copy, not publication)"
    row["date_hint"], row["date_source"] = date or "", src or ""
    y = re.match(r"((19|20)\d\d)", date or "")
    row["age_class"] = age(y.group(1) if y else None)
    if row["age_class"] == "undated" and row["result"] == "captured":
        row["age_class"] = "undated (live page on capture date)"
    row["text_file"] = "text.txt" if os.path.exists(os.path.join(d, "text.txt")) else ""
    rows.append(row)

cols = ["n", "url", "result", "age_class", "date_hint", "date_source", "primary_file", "text_file", "sha256", "bytes",
        "http_raw", "http_browser", "final_url", "content_type", "fetched_at", "dir", "cited_in", "note"]
with open(os.path.join(run, "manifest.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(cols) + "\n")
    for r in rows:
        f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")
json.dump(rows, open(os.path.join(run, "manifest.json"), "w"), ensure_ascii=False, indent=0)
from collections import Counter
print(Counter(r["result"] for r in rows)); print(Counter(r["age_class"] for r in rows))
