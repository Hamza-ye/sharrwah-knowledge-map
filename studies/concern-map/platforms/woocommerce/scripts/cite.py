# Citation register for the WooCommerce Q1 run.
# Every quote is checked against the working copy before it is written to ../citations.tsv:
#   access_path local    -> the release file (woocommerce-11.2.1:<path>), exact text after whitespace folding
#   access_path md / raw -> the fetched file as served (raw HTML: tags removed, block tags as line breaks, entities decoded)
#   access_path rendered -> the page_text.mjs copy (document.body.innerText)
# Usage from Python:  sys.path.insert(0, SCRIPTS); import cite; cid = cite.add(...)
# CLI:  python3 -I cite.py check      re-checks every row against its working copy
import csv, html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
TSV = os.path.join(ROOT, "citations.tsv")
INDEX = os.path.join(HERE, "cite_index.tsv")   # cite_id -> working copy used for the check
RELEASE = "/home/user/woocommerce-release/11.2.1/woocommerce"
COLS = ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
_cache = {}


def fold(s):
    s = s.replace(" ", " ").replace("​", "").replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def clean(s):
    return re.sub(r"[\t\r\n]+", " ", str(s)).strip()


def text_of(path, access):
    key = (path, access)
    if key not in _cache:
        t = open(path, encoding="utf-8", errors="replace").read()
        if access == "raw" and re.search(r"<html|<body|<div", t[:5000], re.I):
            # served text of the raw HTML: scripts and styles dropped, block tags become line breaks,
            # inline tags are removed without a separator, entities decoded
            t = re.sub(r"<(script|style|noscript|template)\b.*?</\1>", " ", t, flags=re.S | re.I)
            t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
            t = re.sub(r"</?(p|div|li|ul|ol|br|h[1-6]|tr|td|th|table|section|article|header|footer|nav|main|aside|dt|dd|pre|blockquote|figure|figcaption|details|summary|hr)\b[^>]*>", "\n", t, flags=re.I)
            t = re.sub(r"<[^>]+>", "", t)
            t = html.unescape(t)
        _cache[key] = fold(t)
    return _cache[key]


def rows():
    if not os.path.exists(TSV):
        return []
    with open(TSV, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def index():
    out = {}
    if os.path.exists(INDEX):
        for line in open(INDEX, encoding="utf-8"):
            a, b = line.rstrip("\n").split("\t")
            out[a] = b
    return out


def next_id():
    n = 0
    for r in rows():
        m = re.match(r"WC-S-(\d+)$", r["cite_id"])
        if m:
            n = max(n, int(m.group(1)))
    return f"WC-S-{n + 1:04d}"


def check_one(quote, working, access):
    q = fold(quote)
    if not q:
        return "empty quote"
    if len(q) > 320:
        return f"quote too long ({len(q)})"
    if "..." in q or "…" in q:
        return "ellipsis in quote (choose a quote without one)"
    if q not in text_of(working, access):
        return "quote not found in working copy"
    return ""


_existing = None


def add(source, locator, quote, source_date, date_basis, accessed, access_path, working, cite_id=None, dedupe=True):
    """Append one citation after checking the quote. Returns the cite_id (an existing one if identical)."""
    global _existing
    if access_path == "local" and not working:
        working = os.path.join(RELEASE, source.split(":", 1)[1])
    err = check_one(quote, working, "raw" if access_path in ("raw",) else access_path)
    if err:
        raise ValueError(f"{err}: {source} | {locator} | {quote[:120]}")
    if _existing is None:
        _existing = {(r["source"], r["locator"], r["quote"]): r["cite_id"] for r in rows()}
    key = (clean(source), clean(locator), clean(quote))
    if dedupe and key in _existing:
        return _existing[key]
    cid = cite_id or next_id()
    new = not os.path.exists(TSV)
    with open(TSV, "a", encoding="utf-8") as f:
        if new:
            f.write("\t".join(COLS) + "\n")
        f.write("\t".join(clean(x) for x in [cid, source, locator, quote, source_date, date_basis, accessed, access_path]) + "\n")
    with open(INDEX, "a", encoding="utf-8") as f:
        f.write(f"{cid}\t{working}\n")
    _existing[key] = cid
    return cid


def check_all():
    idx, bad, n = index(), 0, 0
    seen = set()
    for r in rows():
        n += 1
        if r["cite_id"] in seen:
            print("duplicate id", r["cite_id"]); bad += 1
        seen.add(r["cite_id"])
        w = idx.get(r["cite_id"])
        if not w:
            print("no working copy", r["cite_id"]); bad += 1; continue
        err = check_one(r["quote"], w, r["access_path"])
        if err:
            print(r["cite_id"], err, r["quote"][:80]); bad += 1
    print(f"{n} citations, {bad} problems")


if __name__ == "__main__" and sys.argv[1:] == ["check"]:
    check_all()
