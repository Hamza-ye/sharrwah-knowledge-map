# Helpers for statements from web pages: the captured page text (capture 20261011T061248Z) or, for pages outside
# that capture, this run's working copies in fetched/pages (logged in fetched/log.tsv).
import os, re, html, collections, csv
from common import *

_FIRST_WEB = None
def first_web_dates():
    global _FIRST_WEB
    if _FIRST_WEB is None:
        _FIRST_WEB = collections.defaultdict(collections.Counter)
        for r in rd(os.path.join(FIRST, "citations.tsv")):
            if r["source"].startswith("http"):
                _FIRST_WEB[r["source"].split("#")[0]][(r["source_date"], r["date_basis"], r["access_path"])] += 1
    return _FIRST_WEB

WORKING_DATES = {
    "https://www.shopify.com/legal/shop-campaigns-merchant-terms": ("2026-05-20", 'last updated (page states "Last Updated: May 20th 2026")', "rendered"),
    "https://collabs.shopify.com/terms": ("2026-06-25", 'last updated (page states "Last Updated: June 25, 2026")', "rendered"),
    "https://www.shopify.com/legal/shopify-credit-program-terms": ("2024-09-01", 'effective date (page states "Effective Date: September 1, 2024")', "rendered"),
    "https://www.shopify.com/legal/shopify-credit-issuing-bank-terms": ("2024-09-01", 'effective date (page states "Effective Date: September 1, 2024")', "rendered"),
}

def date_for(url):
    u = url.split("#")[0]
    if u in WORKING_DATES:
        return WORKING_DATES[u]
    c = first_web_dates().get(u)
    if c:
        (d, basis, ap), _ = c.most_common(1)[0]
        if basis.startswith("undated live page"):
            return TODAY, "undated live page; read 2026-10-11 (capture 20261011T061248Z)", ap
        return d, basis, ap
    if u in MANIFEST:
        cap, r = MANIFEST[u]
        ap = "md" if u.endswith(".md") else "rendered"
        return TODAY, "undated live page; read 2026-10-11 (capture " + os.path.basename(cap)[:16] + ")", ap
    if working_copy(u):
        return TODAY, "undated live page; read 2026-10-11", ("md" if u.endswith(".md") else "rendered")
    raise SystemExit(f"no date for {u}")

def page_text(url):
    u = url.split("#")[0]
    if u in MANIFEST:
        cap, r = MANIFEST[u]
        d = os.path.join(cap, r["dir"])
        fp = os.path.join(d, "text.txt")
        if not os.path.exists(fp):
            fp = os.path.join(d, r["primary_file"])
        return open(fp, encoding="utf-8", errors="replace").read()
    wc = working_copy(u)
    assert wc, f"no capture or working copy for {u}"
    return open(wc, encoding="utf-8", errors="replace").read()

_PLAIN = {}
def plain(url):
    if url not in _PLAIN:
        t = page_text(url)
        # one normalized text per line block, so sentences don't run across headings
        blocks = [md_plain(norm(b)) for b in re.split(r"\n\s*\n|\n(?=#)|\n(?=- )|\n(?=\* )|\n(?=\d+\. )|\n", t)]
        _PLAIN[url] = [b for b in blocks if b]
    return _PLAIN[url]

END0 = re.compile(r'(?<=[.!?:;])["\')\]]?\s')
ABBR = re.compile(r'(?:\b(?:Inc|Ltd|Co|Corp|N\.A|U\.S|U\.S\.A|e\.g|i\.e|etc|No|S\.A|St|Mr|Ms|Dr|vs|approx|Pte|L\.L\.C|LLC|plc|GmbH|S\.A\.S|Sec|Art)|\b[A-Z])\.["\')\]]?\s$')
class _End:
    def finditer(self, b):
        for m in END0.finditer(b):
            if ABBR.search(b[max(0, m.start() - 12):m.end()]):
                continue
            yield m
END = _End()

def sentence(url, frag, n_sent=1, occurrence=0):
    """The sentence (or n_sent sentences) of the page that contains frag, normalized as the checker does."""
    f = md_plain(norm(frag))
    hits = [b for b in plain(url) if f in b]
    assert hits, f"fragment not on page {url}: {frag}"
    b = hits[occurrence]
    i = b.index(f)
    starts = [0] + [m.end() for m in END.finditer(b)]
    s = max(x for x in starts if x <= i)
    ends = [m.start() + 1 + (1 if b[m.start() + 1:m.start() + 2] in '"\')]' else 0) for m in END.finditer(b) if m.start() >= i + len(f) - 1]
    e = ends[n_sent - 1] if len(ends) >= n_sent else len(b)
    return b[s:e].strip()

def wcite(url, quote, locator=""):
    d, basis, ap = date_for(url)
    return web_cite(url, locator or "page text", quote, d, basis, ap)
