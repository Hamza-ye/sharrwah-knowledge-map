# Build fetched/registry.json: cited URL -> working copies, access path, source date and its basis.
import json, os, re, sys, csv, html
Z = sys.argv[1]
F = os.path.join(Z, "fetched")
reg = {}
MONTHS = {m: i for i, m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"], 1)}
SHORT = {m[:3]: i for m, i in MONTHS.items()}
def iso(m, d, y): return f"{int(y):04d}-{MONTHS.get(m, SHORT.get(m[:3], 0)):02d}-{int(d):02d}"
def add(url, files, access, date, basis):
    e = reg.setdefault(url, {"files": [], "access": access, "date": date, "basis": basis})
    for f in files:
        if f not in e["files"]: e["files"].append(f)
READ = "2026-10-12"
UNDATED = "undated; live page read 2026-10-12"
# docs .md
for d in ("docs", "docs/api"):
    for f in sorted(os.listdir(os.path.join(F, d))):
        if not f.endswith(".md"): continue
        p = os.path.join(F, d, f)
        t = open(p, encoding="utf-8").read()
        m = re.search(r"\*\*Updated:\*\*\s*(\d{1,2}) (\w+) (\d{4})", t)
        if m: add(f"https://docs.zid.sa/{f}", [p], "md", iso(m.group(2), m.group(1), m.group(3)), "Updated date shown on page")
        else: add(f"https://docs.zid.sa/{f}", [p], "md", READ, UNDATED)
add("https://docs.zid.sa/llms.txt", [os.path.join(F, "docs-llms.txt")], "raw", READ, UNDATED)
add("https://zid.sa/llms.txt", [os.path.join(F, "zidsa-llms.txt")], "raw", READ, UNDATED)
# help rendered
def help_date(text):
    m = re.search(r"آخر تحديث\s+(\w+) (\d{1,2}), (\d{4})", text)
    return (iso(m.group(1), m.group(2), m.group(3)), "last updated (آخر تحديث) shown on page") if m else (READ, UNDATED)
for row in csv.reader(open(os.path.join(F, "helptxt", "index.tsv"), encoding="utf-8"), delimiter="\t"):
    p = os.path.join(F, row[0]); t = open(p, encoding="utf-8").read()
    d, b = help_date(t)
    add(row[1], [p], "rendered", d, b)
# help raw settings articles
import urllib.parse
for u in open(os.path.join(F, "helpraw", "settings-urls.txt"), encoding="utf-8").read().split():
    slug = urllib.parse.unquote(u.replace("https://help.zid.sa/", "").strip("/"))
    name = re.sub(r"[^A-Za-z0-9_-]", "x", slug)[:60]
    p = os.path.join(F, "helpraw", name + ".html")
    if not os.path.exists(p): continue
    t = html.unescape(re.sub(r"<[^>]+>", "\n", open(p, encoding="utf-8").read()))
    d, b = help_date(re.sub(r"\s+", " ", t))
    # if a rendered copy exists for the same URL, keep both files
    hit = [k for k in reg if urllib.parse.unquote(k).rstrip("/") == urllib.parse.unquote(u).rstrip("/")]
    if hit: reg[hit[0]]["files"].append(p)
    else: add(u, [p], "raw", d, b)
# help category pages
for u, f in [("https://help.zid.sa/category/zid-pay/", "help/cat5.html"),
             ("https://help.zid.sa/category/%d8%a7%d9%84%d8%a5%d8%b9%d8%af%d8%a7%d8%af%d8%a7%d8%aa/", "help/cat1.html"),
             ("https://help.zid.sa/", "help/home.html")]:
    add(u, [os.path.join(F, f)], "raw", READ, UNDATED)
# zid.sa pages from the fetch log
lastmod = dict(l.rstrip("\n").split("\t") for l in open(os.path.join(F, "site", "lastmod.tsv"), encoding="utf-8"))
for row in csv.reader(open(os.path.join(F, "log.tsv"), encoding="utf-8"), delimiter="\t"):
    if len(row) < 8 or row[1] != "curl": continue
    url, f = row[2], row[7]
    if re.match(r"^https://zid\.sa/(en|ar)/", url) and f.startswith("site/"):
        cu = url if url.endswith("/") else url + "/"
        base = cu.rstrip("/")
        p = os.path.join(F, f)
        t = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"Last Updated</[^>]+>\s*<[^>]+>\s*(\w+) (\d{4})", t)
        m2 = re.search(r"آخر تحديث</[^>]+>\s*<[^>]+>\s*(\S+) (\d{4})", t)
        mb = re.search(r"(\w{3}) (\d{1,2}), (\d{4})<!-- -->(\d+) min read|(\w{3}) (\d{1,2}), (\d{4})\d+ min read", re.sub(r"<[^>]+>", "", t))
        if m: add(cu, [p], "raw", f"{m.group(2)}-{MONTHS[m.group(1)]:02d}", "Last Updated shown on page")
        elif m2:
            AR = {"يناير":1,"فبراير":2,"مارس":3,"ابريل":4,"أبريل":4,"مايو":5,"يونيو":6,"يوليو":7,"اغسطس":8,"أغسطس":8,"سبتمبر":9,"اكتوبر":10,"أكتوبر":10,"نوفمبر":11,"ديسمبر":12}
            add(cu, [p], "raw", f"{m2.group(2)}-{AR.get(m2.group(1), 0):02d}", "آخر تحديث shown on page")
        elif "/blog/" in cu and mb:
            g = [x for x in mb.groups() if x]
            add(cu, [p], "raw", iso(g[0], g[1], g[2]), "publication date shown on page")
        elif base in lastmod: add(cu, [p], "raw", lastmod[base], "sitemap lastmod (zid.sa/sitemap.xml)")
        else: add(cu, [p], "raw", READ, UNDATED)
# others
add("https://api.zid.sa/v1/market/public/categories", [os.path.join(F, "apps/categories.json")], "raw", READ, UNDATED)
add("https://zid.sa/_next/static/chunks/2501-f29c20b24ab64821.js", [os.path.join(F, "js/2501-f29c20b24ab64821.js")], "raw", "2026-10-11", "HTTP Last-Modified header of the file")
add("https://apps.zid.sa/en-sa/apps", [os.path.join(F, "apps/apps-en.render.txt")], "rendered", READ, UNDATED)
for row in csv.reader(open(os.path.join(F, "log.tsv"), encoding="utf-8"), delimiter="\t"):
    if len(row) < 8 or row[1] != "curl" or "help-partner.zid.sa" not in row[2] or not row[7].endswith(".html"): continue
    p = os.path.join(F, row[7]); t = re.sub(r"<[^>]+>", "\n", open(p, encoding="utf-8").read())
    m = re.search(r"\n\s*(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})\s*\n", t)
    if m: add(row[2], [p], "raw", iso(m.group(1), m.group(2), m.group(3)), "date shown on article")
    else: add(row[2], [p], "raw", READ, UNDATED)
json.dump(reg, open(os.path.join(F, "registry.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(reg))
from collections import Counter
print(Counter(v["basis"] for v in reg.values()))
# Page-shown dates checked by reading the pages (the regexes above miss these two layouts).
reg = json.load(open(os.path.join(F, "registry.json"), encoding="utf-8"))
reg["https://zid.sa/en/legal/terms-conditions/"].update(date="2025-01", basis="Last Updated shown on page: January 2025")
reg["https://zid.sa/ar/legal/terms-conditions/"].update(date="2026-08", basis="آخر تحديث shown on page: اغسطس 2026")
json.dump(reg, open(os.path.join(F, "registry.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("overrides applied")
# Two sources used by the inventory and statements that the loops above do not cover.
reg = json.load(open(os.path.join(F, "registry.json"), encoding="utf-8"))
reg["https://zid.sa/sitemap.xml"] = dict(files=[os.path.join(F, "site/sitemap.xml")], access="raw", date=READ, basis=UNDATED)
reg["https://c.zid.sa/ar-sa"] = dict(files=[os.path.join(F, "misc/c-zid-sa.txt")], access="rendered", date=READ, basis=UNDATED)
json.dump(reg, open(os.path.join(F, "registry.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("extra sources added", len(reg))
