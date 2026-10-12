# Helpers for writing statements and gaps (Q1 Zid run). Statement texts are verbatim excerpts; helpers below pull
# exact text from the working copies where the source is structured (plan data, API index, scope accordions).
import csv, json, os, re
Z = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid"
F = os.path.join(Z, "fetched")
STATEMENTS, GAPS = [], []

def S(c, p, url, loc, structure, ident, text, scope="", note="", quote=None):
    STATEMENTS.append(dict(c=c, p=p, url=url, loc=loc, structure=structure, ident=ident, text=text, scope=scope, note=note, quote=quote))

def G(c, p, what, means, who, route, why, kind):
    GAPS.append(dict(c=c, p=p, what=what, means=means, who=who, route=route, why=why, kind=kind))

OUTSIDE = "Outside the declaration-level scope: this run used no accounts and recorded no journeys."
def OBS(c, p, what, route, means="Record a journey in a store's dashboard on each plan, and with a staff role", who="founder"):
    G(c, p, what, means, who, route, OUTSIDE, "observation needed")
def ASK(c, p, what, route):
    G(c, p, what, "Ask Zid (the question is not answered on its public pages)", "founder", route,
      "Outside the declaration-level scope: it needs a question to the platform; the public pages read do not state it.", "observation needed")
def SNF(c, p, what, route, why="The pages in the route were read in this run; none states it."):
    G(c, p, what, "Read the pages again after an update, or ask Zid", "either", route, why, "searched, not found")
def PNR(c, p, what, route, why="Not read in this run."):
    G(c, p, what, "Fetch and read the page", "agent", route, why, "page not read")
TERMS_AR = "https://zid.sa/ar/legal/terms-conditions/"
def GEN(c, what="A clause that places legal responsibility for this concern by name", route=TERMS_AR):
    G(c, "responsible", what, "Read the agreement that governs this concern, or ask Zid", "either", route,
      "The Terms and Conditions speak of Zid's Services in general; applying such a clause to this concern would be inference.",
      "stated only in general terms")

# ---- sources ----
_help = {}
for row in csv.reader(open(os.path.join(F, "helptxt", "index.tsv"), encoding="utf-8"), delimiter="\t"):
    key = re.sub(r"^\d+-", "", os.path.basename(row[0])[:-4]); _help[key] = row[1]
def H(key):
    """help.zid.sa URL by rendered-file key (e.g. 'faq-22', 'about_zidpay') or by slug."""
    if key in _help: return _help[key]
    return f"https://help.zid.sa/{key}/"
def D(slug): return f"https://docs.zid.sa/{slug}.md"
AR_TERMS = TERMS_AR; EN_TERMS = "https://zid.sa/en/legal/terms-conditions/"
AR_ZPSA = "https://zid.sa/ar/legal/zidpay-terms-conditions-sa/"; EN_ZPSA = "https://zid.sa/en/legal/zidpay-terms-conditions-sa/"
AR_ZPKW = "https://zid.sa/ar/legal/zidpay-terms-conditions-kw/"; EN_ZPKW = "https://zid.sa/en/legal/zidpay-terms-conditions-kw/"
EN_PRIV = "https://zid.sa/en/legal/privacy-policy/"; AR_PRIV = "https://zid.sa/ar/legal/privacy-policy/"
PRICING = "https://zid.sa/en/pricing/"; PAYMENTS = "https://zid.sa/en/solutions/payments/"
CHUNK = "https://zid.sa/_next/static/chunks/2501-f29c20b24ab64821.js"
LLMS = "https://docs.zid.sa/llms.txt"; ZLLMS = "https://zid.sa/llms.txt"
CATS = "https://api.zid.sa/v1/market/public/categories"
PAYOUTS = "https://zid.sa/en/partners/developers/blog/partner-payouts/"

# structures
ST = {
 AR_TERMS: "الشروط والأحكام (zid.sa/ar/legal/terms-conditions; the Arabic version prevails)",
 EN_TERMS: "Terms & Conditions (zid.sa/en/legal/terms-conditions)",
 AR_ZPSA: "شروط وأحكام زد باي, Saudi Arabia (zid.sa/ar/legal/zidpay-terms-conditions-sa)",
 EN_ZPSA: "Zid Pay Terms and Conditions, Saudi Arabia (zid.sa/en/legal/zidpay-terms-conditions-sa)",
 AR_ZPKW: "شروط وأحكام زد باي, Kuwait (zid.sa/ar/legal/zidpay-terms-conditions-kw)",
 EN_ZPKW: "Terms and Conditions for Zed Pay – Kuwait (zid.sa/en/legal/zidpay-terms-conditions-kw)",
 EN_PRIV: "Privacy Policy (zid.sa/en/legal/privacy-policy)", AR_PRIV: "سياسة الخصوصية (zid.sa/ar/legal/privacy-policy)",
 PRICING: "pricing page, plan cards data (zid.sa/en/pricing)", PAYMENTS: "product page Payments (zid.sa/en/solutions/payments)",
 CHUNK: "pricing page compare-plans data (zid.sa script chunk 2501)", LLMS: "docs.zid.sa page index (llms.txt), API Docs navigation",
 ZLLMS: "zid.sa site index (llms.txt)", CATS: "App Market categories endpoint used by apps.zid.sa", PAYOUTS: "developer blog: Getting paid by Zid",
}
def struct(url, title=None):
    if url in ST: return ST[url]
    if url.startswith("https://docs.zid.sa/"): return f"docs.zid.sa: {title or url.rsplit('/', 1)[1]}"
    if url.startswith("https://help.zid.sa/"): return f"help.zid.sa article: {title}" if title else "help.zid.sa article"
    if url.startswith("https://help-partner.zid.sa/"): return f"partner help centre: {title}" if title else "partner help centre"
    return title or url

# plan-line objects from the compare-plans data
_chunk = open(os.path.join(F, "js", "2501-f29c20b24ab64821.js"), encoding="utf-8").read()
def PL(en, nth=0):
    ms = list(re.finditer(r'name:\{ar:"[^"]*",en:"' + re.escape(en) + r'"\},description:\{ar:"[^"]*",en:"[^"]*"\},plans:\{[^}]*\}\}', _chunk))
    return ms[nth].group(0)
PLAN_NOTE = "In the minified source, !0 is JavaScript true and !1 is false; a quoted number is the stated count. Keys: starter, launch, growth, pro."
PLAN_SCOPE = "compare-plans: starter, launch, growth, pro"

# API index lines
_llms = open(os.path.join(F, "docs-llms.txt"), encoding="utf-8").read()
def APIW(crumb, name=None):
    for m in re.finditer(r"^- " + re.escape(crumb) + r" \[([^\]]*)\]\((https://docs\.zid\.sa/[^)]*\.md)\)", _llms, re.M):
        if name is None or m.group(1) == name:
            return f"{crumb} [{m.group(1)}]({m.group(2)})"
    raise KeyError(crumb, name)

# scope accordion text of an endpoint page (whitespace collapsed; the checker collapses whitespace too)
def SCOPEQ(slug):
    t = open(os.path.join(F, "docs", "api", slug + ".md"), encoding="utf-8").read()
    m = re.search(r'<Accordion title="[^"]*[Ss]cope[^"]*"[^>]*>(.*?)</Accordion>', t, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip()
_api = {r["slug"]: r for r in csv.DictReader(open(os.path.join(F, "docs", "api-index.tsv"), encoding="utf-8"), delimiter="\t")}
def EP(slug):
    r = _api[slug]; return f'{r["method"]} {r["path"]}'
