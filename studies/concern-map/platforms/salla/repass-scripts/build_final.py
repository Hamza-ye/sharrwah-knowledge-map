# Assembles final/ for the Salla re-pass: inventory, concerns, citations, statements, gaps, not-reached and the
# first run's placements.tsv kept as a record (the checker reads it). review-log.tsv is written by review.py and
# notes.md separately. Usage: python3 -I build_final.py
import sys, os, re, json, collections, shutil, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from srcs import osa
import gapspec as G

OUT = f"{SP}/final"
READ_DAY = "2026-10-11"
reviewed = rd(f"{SP}/work/reviewed.tsv")
new_st = rd(f"{SP}/work/new_statements.tsv")
new_cit = rd(f"{SP}/work/new_citations.tsv")
first_cit = rd(f"{FIRST}/citations.tsv")
inv = rd(f"{FIRST}/inventory.tsv")
con = rd(f"{FIRST}/concerns.tsv")

# ---------------- new concerns and their inventory entries ----------------
cit_new_extra = []
def new_cite(cid, path, line, quote, locator, date, basis):
    raw = osa(path).split("\n")[line - 1]
    assert quote in raw, (path, line, quote)
    cit_new_extra.append(dict(cite_id=cid, source=f"observed-sa@145f137:{path}", locator=locator, quote=quote, source_date=date,
                              date_basis=basis, accessed=READ_DAY, access_path="local"))
    return cid
nid = max(int(r["cite_id"].split("-")[-1]) for r in new_cit) + 1
PMD = "structures/salla/portal-menu-definitions/layout-mf@prod/items.jsonl"
PMD_DATE = ("2026-10-08", "undated menu definition in the Partners portal bundle; held copy captured 2026-10-08")
c92 = new_cite(f"SA-S-{nid}", PMD, 92, '"title":"Transfer Domain","route":"domains-transfer"', "line 92", *PMD_DATE); nid += 1
c93 = new_cite(f"SA-S-{nid}", PMD, 93, '"title":"Domain Assignment","route":"domains-assignment"', "line 93", *PMD_DATE); nid += 1

def cite_of(c, p):
    rows = [r for r in new_st if r["concern_id"] == c and r["placement"] == p]
    return rows[0]["cite_ids"]
sm = {r["cite_ids"]: r for r in new_st}
NEW_INV = [
    ("SA-I-2621", "admin-navigation", "Domains", cite_of("SA-C-301", "decides"), "SA-C-301"),
    ("SA-I-2622", "admin-navigation", "Domains Management", cite_of("SA-C-301", "where"), "SA-C-301"),
    ("SA-I-2623", "admin-navigation", "Transfer Domain", c92, "SA-C-301"),
    ("SA-I-2624", "admin-navigation", "Domain Assignment", c93, "SA-C-301"),
]
def loc_url(cite):
    q = [r for r in new_st if r["cite_ids"] == cite][0]["statement"]
    return re.search(r"<loc>([^<]+)</loc>", q).group(1)
for iid, c in [("SA-I-2625", "SA-C-302"), ("SA-I-2626", "SA-C-303"), ("SA-I-2627", "SA-C-304")]:
    cid = cite_of(c, "where")
    NEW_INV.append((iid, "other:partners-sitemap", loc_url(cid), cid, c))
NEW_CON = [
    ("SA-C-301", "Domains in the Partners portal (Domains Management, Transfer Domain, Domain Assignment)",
     "Domains | Domains Management | Transfer Domain | Domain Assignment | domain-purchase | manage-domains", "SA-I-2621 SA-I-2622 SA-I-2623 SA-I-2624",
     "New in the re-pass (11 October 2026): the Partners portal menu (portal-menu-definitions) names a Domains section that no first-run concern covers; kept apart from the merchant's store domain (SA-C-007) because it sits in the Partners portal under its own feature flag and permission."),
    ("SA-C-302", "Store migration service from other platforms (شروط وأحكام خدمة انتقال المتاجر من منصات أخرى إلى منصة سلة)",
     "شروط وأحكام خدمة انتقال المتاجر من منصات أخرى إلى منصة سلة", "SA-I-2625",
     "New in the re-pass: the partners.salla.com sitemap lists the service's terms, which no first-run concern covers; kept apart from import and export (SA-C-027) because the terms set their own eligibility, benefits and entity."),
    ("SA-C-303", "Store growth acceleration programme for partner agencies (اتفاقية الوكالات لتقديم خدمات لتجار سلة; برنامج تسريع نمو المتاجر)",
     "اتفاقية الوكالات لتقديم خدمات لتجار سلة (Service Level Agreement – SLA) | برنامج تسريع نمو المتاجر", "SA-I-2626",
     "New in the re-pass: the partners.salla.com sitemap lists the agreement, which no first-run concern covers; kept apart from the merchant services marketplace (SA-C-205) because Salla assigns stores to agencies under its own terms."),
    ("SA-C-304", "Global selling programme for partners (partners.salla.com/global-selling-program)",
     "قدّم خدماتك لتجار يتوسعون عالميًا | المدفوعات و البيع بالنيابة (MoR)", "SA-I-2627",
     "New in the re-pass: the partners.salla.com sitemap lists the programme's page, which no first-run concern covers."),
]
for iid, lst, entry, cid, c in NEW_INV:
    inv.append(dict(inv_id=iid, list=lst, entry=entry, cite_id=cid, concern_ids=c, out_of_scope_reason=""))
for c, name, terms, invs, note in NEW_CON:
    con.append(dict(concern_id=c, concern=name, platform_terms=terms, inv_ids=invs, split_note=note))

# ---------------- statements ----------------
statements = [{k: r[k] for k in ST_COLS} for r in reviewed] + [{k: r[k] for k in ST_COLS} for r in new_st]
po = {p: i for i, p in enumerate(PLACEMENTS)}
statements.sort(key=lambda r: (r["concern_id"], po[r["placement"]]))

# ---------------- pages read per concern, for the gaps' why_not_held ----------------
READ = collections.defaultdict(set)
for r in statements:
    if r["structure"].startswith("http"):
        READ[r["concern_id"]].add(r["structure"])
cur = None
for l in open(f"{SP}/work/lists/b4_help.txt", encoding="utf-8").read().split("\n") + open(f"{SP}/work/lists/b9_help.txt", encoding="utf-8").read().split("\n"):
    l = l.strip()
    if l.startswith("# SA-C-"):
        cur = l[2:]
    elif l.startswith("http") and cur:
        READ[cur].add(l)
H = "https://help.salla.sa/article/"
EXTRA = {
    "SA-C-005": [H + "إدارة-باقة-المتجر-الاشتراكات-الفواتير-والترقية/gbc2ct0nerndys7sk4l2rvc1"],
    "SA-C-060": [H + "إدارة-حساب-متجر-الجملة/uolbxkfv65drw1l0q7z6dtmk"],
    "SA-C-062": [H + "إدارة-حساب-متجر-الجملة/uolbxkfv65drw1l0q7z6dtmk"],
    "SA-C-072": [H + "برنامج-الإحالة-التسويق-بالعمولة-لباقات-سلة/ho98sug89tipkyg6cc9jmqrx"],
    "SA-C-094": [H + "إنشاء-حساب-مطور-apple-عبر-تطبيق-الجوال/tzh23j2nr3m34cvgukmpsdxd"],
    "SA-C-095": [H + "دليل-البدء-مع-سلة-بوينت/po4oioshrwxgomjuw2t9n50b"],
    "SA-C-096": [H + "منصة-محلي-والانضمام-لها/pvoh9k11k2sjti6k1xu667e5"],
    "SA-C-115": [H + "كيف-تستفيد-من-بوليصات-الشحن-في-سلة/y2pqllcsineilgx6h7ofivut", H + "إدارة-شركات-الشحن-من-صفحة-الشحن-الموحد/o7pdd5c586q5yl98jmpi2xt3"],
    "SA-C-139": [H + "-إعدادات-شركات-الشحن-والتوصيل-ضمن-بوليصات-سلة/hpia1p1cwm8qtudm44p8jve5"],
    "SA-C-140": [H + "-إعدادات-شركات-الشحن-والتوصيل-ضمن-بوليصات-سلة/hpia1p1cwm8qtudm44p8jve5", H + "-نظام-مستويات-التسعير-للبوليصات-tier-pricing-system/iq494xevre0wubk305cvf9xy"],
    "SA-C-146": [H + "تفاصيل-العنوان-والهوية-في-صفحة-الدفع-لطلبات-الشحن-الدولي/xv4salemauzwaoov97ccuvwf"],
    "SA-C-162": [H + "جاهزية-الشحن-الدولي/vidfaxjgo1wz8xjimrwfgswi"],
    "SA-C-122": [H + "نصائح-لحماية-متجرك-من-الاحتيال/xiu0yycxeuii6wrdn0hfyowh"],
    "SA-C-231": [H + "قانون-التجارة-الإلكترونية/di3p4uro9bna3ezsld2fjznr"],
    "SA-C-066": [H + "قانون-التجارة-الإلكترونية/di3p4uro9bna3ezsld2fjznr"],
    "SA-C-204": ["https://partners.salla.com/help-center/ما-هو-التحقق-من-الهوية-ولماذا-هو-مهم"],
    "SA-C-205": ["https://partners.salla.com/help-center/هل-يتطلب-تواجدي-في-السعودية-لعرض-خدماتي"],
    "SA-C-195": ["https://partners.salla.com/help-center/كيف-أتلقى-المدفوعات-لتطبيقي-على-المنصة"],
    "SA-C-190": ["https://docs.salla.dev/authorization.md", G.APPS_POLICY],
    "SA-C-191": [G.APPS_POLICY], "SA-C-192": [G.APPS_POLICY], "SA-C-193": [G.APPS_POLICY], "SA-C-194": [G.APPS_POLICY],
    "SA-C-196": [G.JOIN_POLICY], "SA-C-197": ["https://docs.salla.dev/embedded-sdk/getting-started.md", G.APPS_POLICY],
    "SA-C-198": [G.APPS_POLICY], "SA-C-199": ["https://docs.salla.dev/app-onboarding/overview.md", G.APPS_POLICY],
    "SA-C-200": [G.APPS_POLICY], "SA-C-201": [G.APPS_POLICY], "SA-C-202": [G.APPS_POLICY],
    "SA-C-203": ["https://docs.salla.dev/salla-cli/auth.md", "https://docs.salla.dev/ai-agent-kit/overview.md", "https://docs.salla.dev/ai-agent-kit/auth.md"],
    "SA-C-207": ["https://docs.salla.dev/report-builder/overview.md"], "SA-C-145": ["https://docs.salla.dev/ship-fulfillment-apis/getting-started.md"],
    "SA-C-101": ["https://docs.salla.dev/twilight-sdk/overview.md", "https://status.salla.sa/"],
    "SA-C-235": ["https://status.salla.sa/", G.APPS_POLICY, G.JOIN_POLICY],
    "SA-C-232": [H + "سياسة-نشر-التطبيق-في-متجر-التطبيقات-1/l6e8bqm8vm89arp4krr40cdm"],
    "SA-C-234": [H + "نصائح-لحماية-متجرك-من-الاحتيال/xiu0yycxeuii6wrdn0hfyowh", "https://docs.salla.dev/security.md"],
    "SA-C-303": ["https://partners.salla.com/legal/اتفاقية-الوكالات-لتقديم-خدمات-لتجار-سلة"],
    "SA-C-304": ["https://partners.salla.com/global-selling-program"],
    "SA-C-176": [G.JOIN_POLICY], "SA-C-175": [G.APPS_POLICY],
}
for c, us in EXTRA.items():
    READ[c].update(us)
def short(u):
    u = urllib.parse.unquote(u)
    m = re.match(r"https://help\.salla\.sa/article/(.+)/([a-z0-9]{24})$", u)
    if m:
        return "help.salla.sa/article/…/" + m.group(2) if len(m.group(1)) > 60 else u.replace("https://", "")
    return u.replace("https://", "")
def read_note(c, limit=4):
    us = sorted(READ.get(c, set()))
    if not us:
        return ("the held help-centre sitemaps (help.salla.sa/articles/sitemap/ar-0..3.xml) list no article specific to this "
                "concern, and no docs page or policy names it")
    s = "; ".join(short(u) for u in us[:limit])
    return s + (f" and {len(us) - limit} more" if len(us) > limit else "")

# ---------------- gaps ----------------
have = collections.defaultdict(set)
for r in statements:
    have[r["concern_id"]].add(r["placement"])
cname = {r["concern_id"]: r["concern"] for r in con}
gaps = []
for r in con:
    c = r["concern_id"]
    name = cname[c]
    for p in PLACEMENTS:
        if p in have[c]:
            continue
        rn = read_note(c)
        if (c, p) in G.OVR:
            what, means, who, route, why, kind = G.OVR[(c, p)]
            why = why.replace("{read}", rn)
        elif p == "responsible" and c in G.GENERAL:
            url, art, quote = G.GENERAL[c]
            what = f"A Salla term or developer policy that names {name} and says who answers for it"
            means, who, kind = "ask the platform", "founder", "stated only in general terms"
            route = f"{url} ({art}); question to partners@salla.sa"
            why = (f"The terms read speak of apps, themes or partners in general, e.g. '{quote}' ({art}); applying that clause to "
                   f"this concern would be inference. Also read: {rn}")
        elif p == "responsible" and c in G.PAY_CONTRACT:
            what = f"The payment services contract (عقد خدمات الدفع), which would say who holds and answers for the funds in {name}"
            means, who, kind = "record a journey", "founder", "observation needed"
            route = G.PAY_JOURNEY
            why = f"The contract is not public and no held journey shows it; help articles name it without its parties. Read: {rn}"
        elif p == "responsible" and c in G.SHIP_PAGE:
            what = f"Salla's shipping terms naming who answers for {name}"
            means, who, kind = "save a page from a browser", "founder", "observation needed"
            route = G.SHIP_PAGE[c]
            why = G.SALLA_403 + f"; the pages read state no responsibility: {rn}"
        elif p == "responsible":
            what = f"A clause of Salla's usage agreement (اتفاقية الاستخدام) that names {name} and says who answers for it"
            means, who, kind = "save a page from a browser", "founder", "observation needed"
            route = G.TERMS
            why = G.SALLA_403 + f"; the pages read state no responsibility: {rn}"
        elif p == "reason" and c in G.PRODUCT:
            what = f"A sentence on Salla's product page giving the reason {name} is placed and offered as it is"
            means, who, kind = "save a page from a browser", "founder", "observation needed"
            route = G.PRODUCT[c]
            why = G.SALLA_403 + f"; the pages read give no reason: {rn}; " + G.DASH_TEXT_SEARCH
        elif p == "reason":
            what = f"A sentence in Salla's own material giving the reason {name} is placed and controlled as it is"
            means, who, kind = "ask the platform", "founder", "searched, not found"
            route = G.ask_route(c, name)
            why = f"Read and none gives a reason: {rn}; " + G.DASH_TEXT_SEARCH
        elif p == "boundary":
            what = f"A Merchant API resource, webhook event, app scope, storefront component or setting that names {name}"
            means, who, kind = "ask the platform", "founder", "searched, not found"
            route = (f"docs.salla.dev API reference, then a question to partners@salla.sa: is there an API, webhook event or app scope for {name}?")
            why = (G.HELD_API_LISTS[0].upper() + G.HELD_API_LISTS[1:] + f"; the pages read describe dashboard steps only: {rn}")
        else:
            sys.exit(f"no gap rule for {c} {p}")
        gaps.append(dict(concern_id=c, placement=p, what_would_show_it=what, means=means, who_can=who, route=route,
                         why_not_held=why, gap_kind=kind))

# ---------------- not reached ----------------
nr = rd(f"{FIRST}/not-reached.tsv")
known = {r["url"] for r in nr}
need = collections.defaultdict(list)
for g in gaps:
    if g["route"].startswith("https://salla.com/"):
        need[g["route"]].append(f"{g['concern_id']} {g['placement']}")
for u, cells in sorted(need.items()):
    enc = urllib.parse.quote(u, safe=":/")
    if u in known or enc in known:
        continue
    nr.append(dict(url=u, status="not requested: salla.com answers 403 with a bot challenge from this session (tested on https://salla.com/terms, 2026-10-10)",
                   needed_for="Re-pass gaps: " + ", ".join(cells),
                   what_to_look_for="Salla's own statement of who answers for the concern, the reason it is offered as it is, and any terms it links to"))
nr.append(dict(url="https://partners.salla.com/global-selling-program",
               status="read 2026-10-11 (rendered and raw HTML); the FAQ answers are collapsed and in neither",
               needed_for="Re-pass gap: SA-C-304 decides",
               what_to_look_for="The answers to 'من يمكنه التسجيل كشريك؟', 'هل لازم أكون في السعودية؟' and 'هل التسجيل عليه رسوم او التزام؟'"))
# the salla.com cells the brief routes to the founder also need the URL listed when the first run listed it under another need
for r in nr:
    if r["url"] in need and not r["needed_for"].startswith("Re-pass"):
        r["needed_for"] = r["needed_for"] + " | Re-pass gaps: " + ", ".join(need[r["url"]])

# ---------------- write ----------------
os.makedirs(OUT, exist_ok=True)
INV_COLS = ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"]
CON_COLS = ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"]
NR_COLS = ["url", "status", "needed_for", "what_to_look_for"]
wr(f"{OUT}/inventory.tsv", INV_COLS, inv)
wr(f"{OUT}/concerns.tsv", CON_COLS, con)
wr(f"{OUT}/citations.tsv", CIT_COLS, first_cit + new_cit + cit_new_extra)
wr(f"{OUT}/statements.tsv", ST_COLS, statements)
wr(f"{OUT}/gaps.tsv", GP_COLS, gaps)
wr(f"{OUT}/not-reached.tsv", NR_COLS, nr)
shutil.copyfile(f"{FIRST}/placements.tsv", f"{OUT}/placements.tsv")
cells = collections.Counter(p for c in have for p in have[c])
print("inventory", len(inv), "concerns", len(con), "citations", len(first_cit) + len(new_cit) + len(cit_new_extra),
      "statements", len(statements), "gaps", len(gaps), "not-reached", len(nr))
print("cells with a statement", dict(cells), "total", sum(cells.values()))
print("gaps by placement", dict(collections.Counter(g["placement"] for g in gaps)))
print("gaps by kind", dict(collections.Counter(g["gap_kind"] for g in gaps)))
print("gaps by who", dict(collections.Counter(g["who_can"] for g in gaps)))
