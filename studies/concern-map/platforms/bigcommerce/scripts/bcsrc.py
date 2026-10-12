# Source registry for the BigCommerce run: short keys -> URL, working-copy files, access path and date.
# Also holds the quote-matching rules copied from method/check_concern_map.py, so quotes can be
# checked against the working copies before the capture run.
import html, os, re, unicodedata

B = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/bigcommerce"
F = os.path.join(B, "fetched")
READ = "2026-10-12"
UNDATED = "undated live page; read on 2026-10-12"

LEGAL = {  # commerce.com path -> (working copy, revision date shown on the page)
    "terms/": ("web/commerce-terms.txt", "2026-06-01"),
    "privacy/": ("legal/privacy.txt", "2026-01-28"),
    "privacy/data-processing-addendum/": ("legal/privacy_data-processing-addendum.txt", "2026-05-14"),
    "privacy/data-processors/": ("legal/privacy_data-processors.txt", "2026-05-14"),
    "terms/acceptable-use-policy/": ("legal/terms_acceptable-use-policy.txt", "2025-07-31"),
    "terms/api-terms/": ("legal/terms_api-terms.txt", "2025-07-31"),
    "terms/fees-and-billing/": ("legal/terms_fees-and-billing.txt", "2026-06-15"),
    "terms/infringing-materials-protocol/": ("legal/terms_infringing-materials-protocol.txt", "2025-07-31"),
    "terms/jurisdiction-specific-terms/": ("legal/terms_jurisdiction-specific-terms.txt", "2025-10-17"),
    "terms/merchant-client-terms/": ("legal/terms_merchant-client-terms.txt", "2025-07-31"),
    "terms/mobile-app-terms/": ("legal/terms_mobile-app-terms.txt", "2025-07-31"),
    "terms/store-terms/": ("legal/terms_store-terms.txt", "2025-07-31"),
    "terms/merchant-unified-billing/": ("legal/terms_merchant-unified-billing.txt", "2025-07-31"),
    "terms/us-uk-ca-merchant-unified-billing/": ("legal/terms_us-uk-ca-merchant-unified-billing.txt", ""),
    "terms/in-merchant-unified-billing/": ("legal/terms_in-merchant-unified-billing.txt", "2025-07-31"),
    "terms/professional-services-program-document/": ("legal/terms_professional-services-program-document.txt", "2025-07-31"),
    "terms/ai-features-addendum/": ("legal/terms_ai-features-addendum.txt", "2026-06-01"),
    "website-terms/": ("legal/website-terms.txt", "2025-07-31"),
    "legal-archives/": ("legal/legal-archives.txt", "2026-07-17"),
}
WWW = {  # bigcommerce.com path -> working copies (rendered text first, raw html second)
    "pricing/": ["web/bc-pricing.txt", "web/bc-pricing.html"],
    "payments/": ["web/bc-payments.txt"],
    "payments/bigcommerce-payments/": ["web/bc-payments-bcp.txt", "web/bc-payments-bcp.html"],
    "payments/gateways/": ["web/bc-payments_gateways.txt", "web/bc-payments_gateways.html"],
    "apps/": ["web/bc-apps.txt"],
    "product/": ["web/bc-product.txt", "web/bc-product.html"],
    "product/secure-web-hosting/": ["web/bc-product_secure-web-hosting.txt"],
    "llms.txt": ["www-llms.txt"],
}
SPECIAL_DOC = {"storefront/catalyst/deployment/native-hosting/overview": "docs/native-hosting-overview.md"}
SPECIAL_API = {"rest/admin/management/tax/tax-settings/update-tax-settings": "apiref/tax-settings-update.md"}


def resolve(key):
    """key -> (url, [working copy paths], default access_path, source_date, date_basis)"""
    if key == "llms_root":
        return "https://docs.bigcommerce.com/llms.txt", [F + "/dev-llms.txt"], "raw", READ, UNDATED
    if key == "llms_dev":
        return "https://docs.bigcommerce.com/developer/llms.txt", [F + "/docs-developer-llms.txt"], "raw", READ, UNDATED
    kind, path = key.split(":", 1)
    if kind == "d":
        local = SPECIAL_DOC.get(path, "docs/" + path.replace("/", "_") + ".md")
        return f"https://docs.bigcommerce.com/developer/docs/{path}.md", [F + "/" + local], "md", READ, UNDATED
    if kind == "a":
        local = SPECIAL_API.get(path, "apiref/" + path.replace("/", "_") + ".md")
        return f"https://docs.bigcommerce.com/developer/api-reference/{path}.md", [F + "/" + local], "md", READ, UNDATED
    if kind == "c":
        local, date = LEGAL[path]
        basis = "Date of Last Revision shown on the page" if date else UNDATED
        return f"https://www.commerce.com/{path}", [F + "/" + local], "rendered", date or READ, basis
    if kind == "w":
        locs = [F + "/" + x for x in WWW[path]]
        if path == "llms.txt":
            return "https://www.bigcommerce.com/llms.txt", locs, "raw", "2026-02-02", "last-updated in the file's metadata"
        return f"https://www.bigcommerce.com/{path}", locs, "rendered", READ, UNDATED
    raise KeyError(key)

# ---------- quote matching, as in method/check_concern_map.py ----------
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
    return re.sub(r"(?s)<[^>]+>", "", raw)


_cache = {}


def texts_for(key):
    if key in _cache:
        return _cache[key]
    _, files, _, _, _ = resolve(key)
    out = []
    for fp in files:
        if not os.path.exists(fp):
            continue
        raw = open(fp, encoding="utf-8", errors="replace").read()
        forms = [raw] + ([html_text(raw)] if fp.endswith(".html") else [])
        for t in forms:
            out += variants(t)
    _cache[key] = out
    return out


def found(quote, key):
    tv = texts_for(key)
    if not tv:
        return "no working copy"
    for (kind, q), level in zip(variants(quote), range(3)):
        for tk, t in tv:
            if tk == kind and q and q in t:
                return "found" if level == 0 else f"found ({kind})"
    return "not found"
