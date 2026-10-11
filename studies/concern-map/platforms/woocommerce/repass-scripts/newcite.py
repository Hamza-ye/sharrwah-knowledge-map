# Helpers for the re-pass spec: make citations and statements, and record gaps.
#   R(path, start, end=None, nth=1, after=None)  release quote: lines from the nth line containing `start`
#                                                (searching after the first line containing `after`, if given)
#                                                through the first following line containing `end`; whitespace folded
#   RL(path, a, b=None)                          release quote by line numbers
#   Web(url, quote, locator)                     a quote from a captured web page (checked against the capture)
#   Old(cite_id)                                 an existing first-run citation
#   S(concern, placement, cite, identifier, scope="", note="", more=())   a statement
#   G(concern, placement, what, means, who, route, why, kind)             a gap
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import qcheck
WOO = qcheck.WOO
FIRST = "/home/user/sharrwah-knowledge-map/studies/concern-map/platforms/woocommerce"
REL_DATE = ("2026-10-09", "released: WooCommerce 11.2.1 on WordPress.org (plugin-info.json last_updated 2026-10-09 3:35pm GMT)")
ACCESSED = "2026-10-11"
csv.field_size_limit(10**9)

def _rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

OLD = {r["cite_id"]: r for r in _rd(os.path.join(FIRST, "citations.tsv"))}
WEBDATE = {}
for r in OLD.values():
    if r["source"].startswith("http"):
        WEBDATE.setdefault(r["source"], (r["source_date"], r["date_basis"], r["accessed"], r["access_path"]))
NEWPAGES = {}  # url -> (source_date, date_basis, accessed, access_path), filled by the spec for pages captured in the re-pass

_lines = {}
def _L(path):
    if path not in _lines:
        _lines[path] = open(os.path.join(WOO, path), encoding="utf-8").read().split("\n")
    return _lines[path]

def fold(s):
    return re.sub(r"\s+", " ", s).strip()

def RL(path, a, b=None):
    b = b or a
    L = _L(path)
    q = fold(" ".join(L[a - 1:b]))
    loc = f"line {a}" if a == b else f"lines {a}-{b}"
    return {"source": f"woocommerce-11.2.1:{path}", "locator": loc, "quote": q,
            "source_date": REL_DATE[0], "date_basis": REL_DATE[1], "accessed": ACCESSED, "access_path": "local"}

def R(path, start, end=None, nth=1, after=None):
    """Anchors are matched with whitespace folded on both sides."""
    L = [fold(x) for x in _L(path)]
    start, end, after = fold(start), (fold(end) if end else None), (fold(after) if after else None)
    i0 = 0
    if after:
        i0 = next((i for i, l in enumerate(L) if after in l), None)
        if i0 is None:
            raise SystemExit(f"'after' anchor not found: {path}: {after!r}")
    hits = [i for i in range(i0, len(L)) if start in L[i]]
    if len(hits) < nth:
        raise SystemExit(f"anchor not found: {path}: {start!r}")
    a = hits[nth - 1]
    b = a
    if end:
        b = next((i for i in range(a, len(L)) if end in L[i]), None)
        if b is None:
            raise SystemExit(f"end anchor not found: {path}: {end!r} after {start!r}")
    return RL(path, a + 1, b + 1)

def Web(url, quote, locator):
    res = qcheck.check(quote, url)
    if not res.startswith("found"):
        raise SystemExit(f"quote not found ({res}) in {url}: {quote[:100]!r}")
    d = NEWPAGES.get(url) or WEBDATE.get(url)
    if not d:
        raise SystemExit(f"no date record for {url}")
    return {"source": url, "locator": locator, "quote": quote, "source_date": d[0], "date_basis": d[1],
            "accessed": d[2], "access_path": d[3]}

def Old(cid):
    r = OLD[cid]
    return {"cite_id": cid, **{k: r[k] for k in ("source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path")}}

STATEMENTS, GAPS = [], []
P = {"where", "decides", "responsible", "boundary", "reason"}
def S(concern, placement, cite, identifier, scope="", note="", more=()):
    assert placement in P, placement
    if len(cite["quote"]) > 400:
        raise SystemExit(f"quote too long ({len(cite['quote'])}): {concern} {placement} {cite['quote'][:80]}")
    STATEMENTS.append({"concern_id": concern, "placement": placement, "cite": cite, "more": list(more),
                       "identifier": identifier, "scope": scope, "note": note})

KINDS = {"page not read", "observation needed", "searched, not found", "stated only in general terms"}
def G(concern, placement, what, means, who, route, why, kind):
    assert placement in P and who in ("agent", "founder", "either") and kind in KINDS, (concern, placement, who, kind)
    GAPS.append({"concern_id": concern, "placement": placement, "what_would_show_it": what, "means": means,
                 "who_can": who, "route": route, "why_not_held": why, "gap_kind": kind})

# pages read in the re-pass: (source_date, date_basis, accessed, access_path)
NEWPAGES.update({
    "https://woocommerce.com/document/customer-order-withdrawal/": ("2026-10-09", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/high-performance-order-storage/": ("2025-12-20", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/introduction-to-woocommerce-bookings/": ("2026-06-22", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/marketplace-developers-customer-overview/": ("2026-02-28", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/subscriptions/": ("2026-06-23", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/support-guide/": ("2026-06-15", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/woocommerce-marketplace-suggestions-settings/": ("2026-02-28", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/woopay-merchant-documentation/": ("2026-05-20", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://automattic.com/ai-guidelines": ("2026-08-18", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
})
for _u in ["apis/store-api/rate-limiting.md", "features/products/product-customs-data.md", "features/email/customer-review-request.md",
           "extensions/extension-onboarding/integrating-coming-soon-mode.md", "features/orders/high-performance-order-storage/enable-hpos.md",
           "wc-cli/wc-cli-commands/wc-com.md", "best-practices/data-management/data-stores.md",
           "extensions/best-practices-extensions/gdpr-compliance.md"]:
    NEWPAGES["https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/" + _u] = (
        "2026-10-11", "undated live page; counts as current on the day it was read", "2026-10-11", "md")

def RS(path, a, b, sub):
    """A release quote that is a part of lines a-b (whitespace folded)."""
    whole = RL(path, a, b)
    sub = fold(sub)
    if sub not in whole["quote"]:
        raise SystemExit(f"substring not in {path}:{a}-{b}: {sub[:80]!r}")
    whole["quote"] = sub
    return whole
NEWPAGES.update({
    "https://woocommerce.com/document/subscriptions/develop/action-reference/": ("2025-02-18", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/bookings-rest-api-reference/": ("2026-10-11", "undated live page (redirects to woocommerce.github.io/woocommerce-bookings-api-docs/); counts as current on the day it was read", "2026-10-11", "rendered"),
    "https://woocommerce.com/document/woopayments/settings-guide/": ("2026-09-25", "last updated: JSON-LD dateModified", "2026-10-11", "rendered"),
})
