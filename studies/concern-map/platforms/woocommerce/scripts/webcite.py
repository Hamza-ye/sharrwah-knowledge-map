# Helpers to register citations from fetched web pages and from the release, under symbolic keys.
# Keys map to cite_ids in out/cite_keys.json, so concern and placement scripts can refer to them.
import csv, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cite

FETCHED = os.path.normpath(os.path.join(HERE, "..", "fetched"))
KEYS = os.path.join(HERE, "out", "cite_keys.json")
REL_DATE = "2026-10-09"
REL_BASIS = "released: WooCommerce 11.2.1 on WordPress.org (plugin-info.json last_updated 2026-10-09 3:35pm GMT)"
_log = None
FAILURES = []
TRY = os.environ.get("CITE_TRY") == "1"
_keys = None


def keys():
    global _keys
    if _keys is None:
        _keys = json.load(open(KEYS)) if os.path.exists(KEYS) else {}
    return _keys


def save_keys():
    json.dump(keys(), open(KEYS, "w"), indent=0, sort_keys=True)


def log_rows():
    global _log
    if _log is None:
        with open(os.path.join(FETCHED, "log.tsv"), encoding="utf-8") as f:
            _log = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    return _log


def find_fetch(url, method):
    rows = [r for r in log_rows() if r["url"] == url and r["method"].startswith(method) and r["http_status"].startswith("2")]
    if not rows:
        raise LookupError(f"no {method} fetch for {url}")
    return rows[-1]


def page_date(html_path):
    h = open(html_path, encoding="utf-8", errors="replace").read()
    for basis, rx in [("last updated: JSON-LD dateModified", r'"dateModified":"(\d{4}-\d\d-\d\d)'),
                      ("last updated: meta article:modified_time", r'article:modified_time" content="(\d{4}-\d\d-\d\d)'),
                      ("published: JSON-LD datePublished", r'"datePublished":"(\d{4}-\d\d-\d\d)')]:
        m = re.search(rx, h)
        if m:
            return m.group(1), basis
    return None, None


def web(key, url, quote, locator, source_date=None, basis=None, method=None):
    """Register a quote from a fetched URL. Raw GitHub files are checked as served (md);
    HTML pages are checked against the rendered copy when one exists, else against the raw HTML."""
    if key in keys():
        return keys()[key]
    if method is None:
        if "raw.githubusercontent.com" in url:
            method = "curl"
        else:
            try:
                find_fetch(url, "rendered"); method = "rendered"
            except LookupError:
                method = "curl"
    r = find_fetch(url, method)
    path = os.path.join(FETCHED, r["file"])
    accessed = r["fetched_at"][:10]
    if method == "rendered":
        access = "rendered"
    elif "raw.githubusercontent.com" in url:
        access = "md"
    else:
        access = "raw"
    if not source_date:
        try:
            c = find_fetch(url, "curl")
            cp = os.path.join(FETCHED, c["file"])
            if cp.endswith(".html"):
                source_date, basis = page_date(cp)
        except LookupError:
            pass
    if not source_date:
        source_date, basis = accessed, "undated live page; counts as current on the day it was read"
    try:
        cid = cite.add(source=url, locator=locator, quote=quote, source_date=source_date, date_basis=basis,
                       accessed=accessed, access_path=access, working=path)
    except ValueError as e:
        if not TRY:
            raise
        FAILURES.append((key, str(e)[:160])); print("FAIL", key, access, str(e)[:110]); return None
    keys()[key] = cid
    save_keys()
    return cid


def rel(key, path, quote, locator=None):
    """Register a quote from the release (woocommerce-11.2.1:<path>). Locator defaults to the first matching line."""
    if key in keys():
        return keys()[key]
    full = os.path.join(cite.RELEASE, path)
    if locator is None:
        lines = open(full, encoding="utf-8", errors="replace").read().split("\n")
        q = cite.fold(quote)
        n = next((i + 1 for i, l in enumerate(lines) if q[:60] in cite.fold(l)), None)
        locator = f"line {n}" if n else "file"
    try:
        cid = cite.add(source="woocommerce-11.2.1:" + path, locator=locator, quote=quote, source_date=REL_DATE,
                       date_basis=REL_BASIS, accessed="2026-10-10", access_path="local", working=full)
    except ValueError as e:
        if not TRY:
            raise
        FAILURES.append((key, str(e)[:160])); print("FAIL", key, "local", str(e)[:110]); return None
    keys()[key] = cid
    save_keys()
    return cid


def k(key):
    return keys()[key]
