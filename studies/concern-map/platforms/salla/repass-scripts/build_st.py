# Builds the new statements and citations from spec.py, checking each statement is verbatim in its source.
# Writes work/new_statements.tsv and work/new_citations.tsv. Usage: python3 -I build_st.py
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from srcs import *
import spec

READ_DAY = "2026-10-11"
AR_MONTHS = {"يناير": 1, "فبراير": 2, "مارس": 3, "أبريل": 4, "إبريل": 4, "مايو": 5, "يونيو": 6, "يوليو": 7, "أغسطس": 8,
             "سبتمبر": 9, "أكتوبر": 10, "نوفمبر": 11, "ديسمبر": 12}
first_cit = {r["cite_id"]: r for r in rd(f"{FIRST}/citations.tsv")}
cap_date = {r["url"]: r["fetched_at"][:10] for r in rd(f"{CAP}/manifest.tsv")}

def help_date(lines):
    for l in lines:
        m = re.search(r"تاريخ اخر تحديث:\s*\S+\s+(\d{1,2})\s+(\S+)\s+(\d{4})", l)
        if m and m.group(2) in AR_MONTHS:
            return f"{m.group(3)}-{AR_MONTHS[m.group(2)]:02d}-{int(m.group(1)):02d}"
    return None

def found(st, texts):
    sv = variants(st)
    for t in texts:
        tv = variants(t)
        for a, b in zip(sv, tv):
            if a and a in b:
                return True
    return False

def json_texts(raw):
    out = [raw]
    strs = []
    for line in raw.splitlines():
        try:
            o = json.loads(line)
        except Exception:
            continue
        def walk(o):
            if isinstance(o, dict):
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
            elif isinstance(o, str):
                strs.append(o)
        walk(o)
    out.append("\n".join(strs))
    try:
        o = json.loads(raw)
        def walk2(o):
            if isinstance(o, dict):
                for v in o.values(): walk2(v)
            elif isinstance(o, list):
                for v in o: walk2(v)
            elif isinstance(o, str):
                strs.append(o)
        walk2(o)
        out.append("\n".join(strs))
    except Exception:
        pass
    return out

def quote_of(st):
    if len(st) <= 300:
        return st
    q = st[:300]
    return q[:q.rfind(" ")] if " " in q else q

LOCAL_DATES = [
    ("partners.salla.com/sitemap.xml", "2026-10-07", "undated sitemap entry; held sitemap captured 2026-10-07"),
    ("help.salla.sa/llms.txt", "2026-10-08", "undated file; held copy captured 2026-10-08"),
    ("structures/salla/portal-help-center-article/", "2026-10-08", "undated FAQ answer; held copy captured 2026-10-08"),
    ("structures/salla/portal-menu-definitions/", "2026-10-08", "undated menu definition in the Partners portal bundle; held copy captured 2026-10-08"),
    ("raw/runs/20261008T145200Z-sweep-partner-portal-routes-en/", "2026-10-08", "request recorded during a sweep of the Partners portal on 2026-10-08"),
    ("structures/salla/dashboard-translations/", "2026-10-08", "undated UI text; translation file held 2026-10-08"),
]
def local_date(path):
    for pre, d, b in LOCAL_DATES:
        if path.startswith(pre):
            return d, b
    raise SystemExit(f"no date rule for {path}")

st_rows, cit_rows = [], []
WCACHE, WCID = {}, {}
n = 5001
for s in spec.NEW:
    k = s["kind"]
    if k == "E":
        c = first_cit[s["cite"]]
        src = c["source"]
        if src.startswith("observed-sa@"):
            raw = osa(src.split(":", 1)[1])
            texts = json_texts(raw) if src.endswith((".json", ".jsonl")) else [raw]
        else:
            texts = [web_lines(src)[0] and "\n".join(web_lines(src)[0])]
        if not found(s["st"], texts):
            sys.exit(f"E not found: {s['c']} {s['p']} {s['cite']} {s['st'][:60]}")
        structure = src
        st_rows.append(dict(concern_id=s["c"], placement=s["p"], structure=structure, identifier=s["ident"], statement=s["st"],
                            scope=s["scope"], cite_ids=s["cite"], note=s["note"]))
        continue
    wkey = (s.get("url"), s.get("line"), s.get("part")) if k == "W" else None
    if wkey and wkey in WCACHE:
        prev = WCACHE[wkey]
        st_rows.append(dict(concern_id=s["c"], placement=s["p"], structure=s["url"], identifier=s["ident"] or s["loc"],
                            statement=prev, scope=s["scope"], cite_ids=WCID[wkey], note=s["note"]))
        continue
    cid = f"SA-S-{n}"; n += 1
    if k == "W":
        lines, f = web_lines(s["url"])
        line = lines[s["line"] - 1].strip()
        if s["part"]:
            if s["part"] in line or md_plain(norm(s["part"])) in md_plain(norm(line)):
                st = s["part"]
            else:
                sys.exit(f"W part not in line: {s['c']} {s['p']} line {s['line']}: {s['part'][:50]} || {line[:80]}")
        else:
            st = line
        if not st:
            sys.exit(f"W empty line: {s['c']} {s['p']} {s['url']} {s['line']}")
        host = s["url"].split("/")[2]
        is_md = s["url"].endswith(".md")
        loc = f"{s['loc']} (line {s['line']} of the {'markdown' if is_md else 'rendered text'})"
        if host == "help.salla.sa":
            d = help_date(lines)
            if not d:
                sys.exit(f"no help date: {s['url']}")
            basis = "last-updated date shown on the page (تاريخ اخر تحديث)"
        else:
            day = cap_date.get(s["url"], READ_DAY) if not os.path.exists(wc_path(s["url"])) else READ_DAY
            d, basis = day, f"undated live page; counts as current on the day read ({day})"
        accessed = READ_DAY
        cit_rows.append(dict(cite_id=cid, source=s["url"], locator=loc, quote=quote_of(st), source_date=d, date_basis=basis,
                             accessed=accessed, access_path="md" if is_md else "rendered"))
        st_rows.append(dict(concern_id=s["c"], placement=s["p"], structure=s["url"], identifier=s["ident"] or s["loc"],
                            statement=st, scope=s["scope"], cite_ids=cid, note=s["note"]))
        WCACHE[wkey] = st; WCID[wkey] = cid
    elif k == "T":
        path = f"structures/salla/dashboard-translations/{s['lang']}/{s['ns']}.json"
        v = tr_value(s["lang"], s["ns"], s["key"])
        st = s["part"] if s["part"] else v
        if s["part"] and s["part"] not in v:
            sys.exit(f"T part not in value: {s['c']} {s['key']}")
        if not found(st, json_texts(osa(path))):
            sys.exit(f"T not found in file: {s['c']} {s['key']}")
        d, basis = local_date(path)
        src = f"observed-sa@145f137:{path}"
        cit_rows.append(dict(cite_id=cid, source=src, locator=s["key"], quote=quote_of(st), source_date=d, date_basis=basis,
                             accessed=READ_DAY, access_path="local"))
        st_rows.append(dict(concern_id=s["c"], placement=s["p"], structure=src, identifier=s["key"], statement=st,
                            scope=s["scope"], cite_ids=cid, note=s["note"]))
    elif k == "J":
        path = s["path"]
        raw = osa(path)
        rlines = raw.split("\n")
        ln = s["line"]
        if ln is None:
            ln = line_of(raw, s["part"])
            if not ln:
                sys.exit(f"J part not found: {path} {s['part'][:60]}")
        line = rlines[ln - 1]
        if s["field"]:
            o = json.loads(line)
            art = [a for a in o.get("articles", []) if str(a["id"]) == s["field"]]
            if not art:
                sys.exit(f"J no article {s['field']} on line {ln}")
            v = art[0]["content"]["ar"]
            st = s["part"] if s["part"] else v.strip()
            if s["part"] and md_plain(norm(s["part"])) not in md_plain(norm(v)):
                sys.exit(f"J part not in article {s['field']}")
        else:
            st = s["part"] if s["part"] else line.strip()
            if s["part"] and s["part"] not in line:
                sys.exit(f"J part not in line {ln}: {path}")
        texts = json_texts(raw) if path.endswith((".json", ".jsonl")) else [raw]
        if not found(st, texts):
            sys.exit(f"J not found: {s['c']} {path} {st[:60]}")
        d, basis = local_date(path)
        src = f"observed-sa@145f137:{path}"
        cit_rows.append(dict(cite_id=cid, source=src, locator=s["loc"] or f"line {ln}", quote=quote_of(st), source_date=d,
                             date_basis=basis, accessed=READ_DAY, access_path="local"))
        st_rows.append(dict(concern_id=s["c"], placement=s["p"], structure=src, identifier=s["ident"] or f"line {ln}",
                            statement=st, scope=s["scope"], cite_ids=cid, note=s["note"]))
    # every web statement must also be verbatim in its working copy text
    if k == "W" and not found(st, ["\n".join(lines)]):
        sys.exit(f"W not found in working copy: {s['c']} {s['p']}")

wr(f"{SP}/work/new_statements.tsv", ST_COLS, st_rows)
wr(f"{SP}/work/new_citations.tsv", CIT_COLS, cit_rows)
print("new statements", len(st_rows), "new citations", len(cit_rows), "last id", n - 1)
print(collections.Counter(r["placement"] for r in st_rows))
