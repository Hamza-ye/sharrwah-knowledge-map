# Shared helpers for the Q1 Shopify re-pass (questions/Q1-concern-map.md, "Changed on 11 October 2026").
# Run every script with python3 -I.
import csv, html, json, os, re, subprocess, unicodedata, collections

csv.field_size_limit(10**9)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # .../q1r/shopify
FIRST = "/home/user/sharrwah-knowledge-map/studies/concern-map/platforms/shopify"
CAPTURE = "/home/user/sharrwah-knowledge-map/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources"
OSH = "/home/user/observed-sh"
COMMIT = "e4984072995bf730a98292a1903de1a49390229a"
C9 = COMMIT[:9]
WORK = os.path.join(BASE, "work")
TODAY = "2026-10-11"

def rd(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def wr(path, cols, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(k, "")).replace("\t", " ").replace("\n", " ").replace("\r", " ") for k in cols) + "\n")

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

# ---------- git ----------
_GIT = {}
def git_show(path, commit=COMMIT):
    key = (commit, path)
    if key not in _GIT:
        p = subprocess.run(["git", "-C", OSH, "show", f"{commit}:{path}"], capture_output=True)
        _GIT[key] = p.stdout.decode("utf-8", errors="replace") if p.returncode == 0 else None
    return _GIT[key]

def git_ls(path, commit=COMMIT):
    p = subprocess.run(["git", "-C", OSH, "ls-tree", "--name-only", f"{commit}:{path}"], capture_output=True, text=True)
    return p.stdout.split() if p.returncode == 0 else []

_REG = None
def register():
    global _REG
    if _REG is None:
        _REG = {r["structure_id"]: r for r in csv.DictReader(git_show("structures/REGISTER.tsv").splitlines(), delimiter="\t", quoting=csv.QUOTE_NONE)}
    return _REG

def date_seen(sid):
    return register().get(sid, {}).get("date seen", "") or "undated"

# ---------- quote matching, as method/check_concern_map.py does it ----------
BIDI = dict.fromkeys(map(ord, "​‌‍‎‏‪‫‬‭‮⁦⁧⁨⁩﻿ـ"), None)
SUBS = [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
        ("−", "-"), (" ", " "), (" ", " "), (" ", " ")]
HARAKAT = re.compile(r"[ً-ْٰ]")

def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s)).translate(BIDI)
    for a, b in SUBS:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()

def md_plain(s):
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]{1,200}>", " ", s)
    s = s.replace("**", "").replace("__", "").replace("`", "").replace("\\", "")
    s = re.sub(r"(^|\s)#{1,6}\s", r"\1", s)
    s = s.replace("|", " ")
    return re.sub(r"\s+", " ", s).strip()

def variants(s):
    n = norm(s)
    p = md_plain(n)
    return [("exact", n), ("markup removed", p), ("case and diacritics ignored", HARAKAT.sub("", p).casefold())]

def html_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)</?(p|div|li|ul|ol|br|hr|h[1-6]|tr|td|th|table|thead|tbody|section|article|header|footer|nav|main|aside|blockquote|pre|dd|dt|dl|figure|figcaption)\b[^>]*>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", "", raw)
    return raw

def json_strings(o, out):
    if isinstance(o, dict):
        for v in o.values(): json_strings(v, out)
    elif isinstance(o, list):
        for v in o: json_strings(v, out)
    elif isinstance(o, str):
        out.append(o)
    return out

def json_unescaped(raw):
    out = []
    for line in raw.splitlines():
        try:
            out.append("\n".join(json_strings(json.loads(line), [])))
        except Exception:
            pass
    for line in raw.splitlines():
        try:
            out.append(json.dumps(json.loads(line), ensure_ascii=False))
        except Exception:
            out.append(line)
    try:
        out.append(json.dumps(json.loads(raw), ensure_ascii=False))
    except Exception:
        pass
    return "\n".join(out)

ROOTS = {"observed-sh": OSH, "sharrwah-knowledge-map": "/home/user/sharrwah-knowledge-map"}
MANIFEST = {}
def load_manifest(cap):
    mf = os.path.join(cap, "manifest.tsv")
    if os.path.exists(mf):
        for r in rd(mf):
            MANIFEST.setdefault(r["url"].split("#")[0], (cap, r))
load_manifest(CAPTURE)
# The Shopify Credit terms pages, captured by the coordinator, and the pages this re-pass cited after the gap review.
CAPTURE_2 = "/home/user/sharrwah-knowledge-map/evidence/product-class/runs/20261011T075149Z-q1-shopify-sources-2"
EXTRA_CAPTURES = [CAPTURE_2]
_more = os.path.join(BASE, "fetched", "capture", "EXTRA_RUNS")
if os.path.exists(_more):
    EXTRA_CAPTURES += [os.path.join(BASE, x.strip()) for x in open(_more) if x.strip()]
for _c in EXTRA_CAPTURES:
    load_manifest(_c)

_SRC = {}
def source_texts(source, allow_working=True):
    """Texts of a cited source, as the checker reads them. Web pages not in the capture fall back to
    this run's working copies in fetched/pages (only for our own pre-check)."""
    key = (source, allow_working)
    if key in _SRC:
        return _SRC[key]
    texts, why = None, ""
    if re.match(r"^https?://", source):
        k = source.split("#")[0]
        if k in MANIFEST:
            cap, r = MANIFEST[k]
            d = os.path.join(cap, r["dir"])
            texts = []
            for name in sorted(os.listdir(d)):
                fp = os.path.join(d, name)
                if not os.path.isfile(fp) or not name.startswith(("raw", "rendered", "text")):
                    continue
                if name.endswith((".pdf", ".bin", ".png", ".jpg", ".jpeg", ".gif", ".webp")):
                    continue
                raw = open(fp, encoding="utf-8", errors="replace").read()
                texts.append(raw)
                if name.endswith(".html"):
                    texts.append(html_text(raw))
                if name.endswith(".json"):
                    texts.append(json_unescaped(raw))
        elif allow_working:
            wc = working_copy(k)
            if wc:
                texts = [open(wc, encoding="utf-8", errors="replace").read()]
                why = "working copy"
            else:
                why = "not captured"
        else:
            why = "not captured"
    else:
        m = re.match(r"^([a-z0-9.-]+)(?:@([0-9a-f]{6,40}))?:(.+)$", source)
        if not m or m.group(1) not in ROOTS:
            why = "not a known local source"
        else:
            root, commit, rel = ROOTS[m.group(1)], m.group(2), m.group(3).strip().lstrip("/")
            rel = re.sub(r"[#:]L?\d+(-L?\d+)?$", "", rel)
            if commit:
                p = subprocess.run(["git", "-C", root, "show", f"{commit}:{rel}"], capture_output=True)
                raw = p.stdout.decode("utf-8", errors="replace") if p.returncode == 0 else None
            else:
                fp = os.path.join(root, rel)
                raw = open(fp, encoding="utf-8", errors="replace").read() if os.path.isfile(fp) else None
            if raw is None:
                why = "missing"
            else:
                texts = [raw]
                if rel.endswith((".json", ".jsonl")):
                    texts.append(json_unescaped(raw))
                if rel.endswith((".html", ".htm")):
                    texts.append(html_text(raw))
    if texts is not None:
        texts = [v for t in texts for v in variants(t)]
    _SRC[key] = (texts, why)
    return _SRC[key]

def check_quote(quote, source, allow_working=True):
    texts, why = source_texts(source, allow_working)
    if texts is None:
        return "unresolved", why
    qv = variants(quote)
    for (kind, q), level in zip(qv, range(3)):
        for (tkind, t) in texts:
            if tkind == kind and q and q in t:
                return ("found" if level == 0 else f"found ({kind})"), why
    return "not found", why

def working_copy(url):
    log = os.path.join(BASE, "fetched", "log.tsv")
    if not os.path.exists(log):
        return None
    best = None
    for r in rd(log):
        if r["url"].split("#")[0] == url and str(r["status"]).startswith("2"):
            for cand in (os.path.join(BASE, "fetched", r["out"]), os.path.join(BASE, r["out"])):
                if os.path.isfile(cand):
                    best = cand
    return best

# ---------- citations added by this re-pass (SH-S-7001 on) ----------
ADDED_CITES = os.path.join(WORK, "cites-added.tsv")
CCOLS = ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
_added = None
def _load_added():
    global _added
    if _added is None:
        _added = collections.OrderedDict()
        if os.path.exists(ADDED_CITES):
            for r in rd(ADDED_CITES):
                _added[(r["source"], r["quote"])] = r
    return _added

_EXISTING = None
def existing_cites():
    global _EXISTING
    if _EXISTING is None:
        _EXISTING = {}
        for path in (os.path.join(FIRST, "citations.tsv"), os.path.join(BASE, "citations-new.tsv")):
            for r in rd(path):
                _EXISTING.setdefault((r["source"], r["quote"]), r["cite_id"])
    return _EXISTING

def short(quote, limit=300):
    """A citation quote of about 300 characters at most: a verbatim prefix, cut at a space or comma."""
    if len(quote) <= limit:
        return quote
    cut = quote[:limit]
    j = max(cut.rfind(" "), cut.rfind(","))
    return cut[:j] if j > limit // 2 else cut

def cite(source, locator, quote, source_date, date_basis, access_path, accessed=TODAY):
    a = _load_added()
    key = (source, quote)
    if key in existing_cites():
        return existing_cites()[key]
    quote = short(quote)
    key = (source, quote)
    if key in existing_cites():
        return existing_cites()[key]
    if key in a:
        return a[key]["cite_id"]
    n = 7001 + len(a)
    cid = f"SH-S-{n:04d}"
    a[key] = {"cite_id": cid, "source": source, "locator": locator, "quote": quote, "source_date": source_date,
              "date_basis": date_basis, "accessed": accessed, "access_path": access_path}
    return cid

def save_cites():
    wr(ADDED_CITES, CCOLS, list(_load_added().values()))

def osh_cite(path, locator, quote, sid=None, source_date=None, date_basis=None):
    """A citation into observed-sh at the re-pass commit; checks the quote is in the file."""
    raw = git_show(path)
    assert raw is not None, f"no {path} at {C9}"
    src = f"observed-sh@{C9}:{path}"
    res, _ = check_quote(quote, src)
    assert res.startswith("found"), f"quote not in {path}: {quote[:120]}"
    if source_date is None:
        if sid:
            source_date, date_basis = date_seen(sid), "observed-sh structures/REGISTER.tsv, date seen"
        else:
            m = re.search(r"raw/runs/(\d{4})(\d\d)(\d\d)T", path)
            source_date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else "undated"
            date_basis = date_basis or "observed-sh run id (date the answer or page was received)"
    return cite(src, locator, quote, source_date, date_basis, "local")

def web_cite(url, locator, quote, source_date, date_basis, access_path):
    res, why = check_quote(quote, url)
    assert res.startswith("found"), f"quote not found in {url} ({res} {why}): {quote[:120]}"
    return cite(url, locator, quote, source_date, date_basis, access_path)

# ---------- statements added by this re-pass ----------
SCOLS = ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note"]

class Adder:
    """Collects added statements for one work/added/<name>.tsv file."""
    def __init__(self, name):
        self.name, self.rows = name, []
    def add(self, concern, placement, structure, identifier, statement, scope, cite_ids, note):
        assert placement in ("where", "decides", "responsible", "boundary", "reason"), placement
        assert re.match(r"^SH-C-\d{3}$", concern), concern
        self.rows.append({"concern_id": concern, "placement": placement, "structure": structure, "identifier": identifier,
                          "statement": statement, "scope": scope, "cite_ids": cite_ids if isinstance(cite_ids, str) else ";".join(cite_ids),
                          "note": note})
    def save(self):
        wr(os.path.join(WORK, "added", self.name + ".tsv"), SCOLS, self.rows)
        save_cites()
        print(f"{self.name}: {len(self.rows)} statements; citations added so far: {len(_load_added())}")
