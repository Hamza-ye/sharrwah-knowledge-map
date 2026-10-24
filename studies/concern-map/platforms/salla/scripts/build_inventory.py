# Build the inventory from Salla's own lists held in observed-sa@145f137.
# Writes OUT/scripts/build/inventory_build.json: rows with list, entry, citation and concern keys / out-of-scope reason.
# Usage: python3 -I build_inventory.py
import json, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import OBS, OUT, ACCESSED, local_source, lines, window, meta_date, load_meta, find_line, clean
import maps

S = "structures/salla"
ROWS = []
UNMAPPED = []


def add(listname, entry, rel, line_no, needle, concerns, struct_dir=None, date=None, date_basis=None, locator=None, quote=None):
    ln = lines(rel)[line_no - 1]
    q = quote if quote is not None else window(ln, needle)
    if q not in ln:
        raise ValueError(f"quote not in line {rel}:{line_no}")
    if date is None:
        m = load_meta(struct_dir or os.path.dirname(rel))
        date = meta_date(m)
    if date_basis is None:
        date_basis = f"undated list; held copy captured {date}"
    if isinstance(concerns, str):
        ck, oos = [], concerns[len("OOS: "):] if concerns.startswith("OOS: ") else concerns
    elif concerns:
        ck, oos = list(dict.fromkeys(concerns)), ""
    else:
        ck, oos = [], ""
        UNMAPPED.append((listname, entry))
    ROWS.append(dict(list=listname, label=clean(entry), entry=clean(verbatim(listname, entry)), concern_keys=ck, oos=oos,
                     cite=dict(source=local_source(rel), locator=locator or f"line {line_no}", quote=clean(q),
                               source_date=date, date_basis=date_basis, accessed=ACCESSED, access_path="local")))


PREFIXES = ("app type: ", "App Store category: ", "App Store goal: ", "app listing category: ", "app listing goal: ",
            "theme category: ", "App Functions event: ", "Twilight component: ", "docs navbar > ", "Salla Special page: ")


def verbatim(listname, e):
    """The platform's own name, without the context labels this script adds."""
    for p in PREFIXES:
        if e.startswith(p):
            return e[len(p):]
    if e.startswith("Ecommerce event ("):
        return e.split("): ", 1)[1]
    if e.startswith("salla.com plans ("):
        return e.split("): ", 1)[1]
    if listname == "plan-features" and re.match(r"^(سلة بلس|سلة برو): ", e):
        return e.split(": ", 1)[1]
    if listname in ("api-resources", "admin-navigation") and " > " in e:
        return e.split(" > ")[-1]
    return e


def jl(rel):
    return [json.loads(x) for x in lines(rel) if x.strip()]


# ---------- api-resources: Merchant API navigation
rel = f"{S}/docs-sidebar/merchant-api@20261009T033553Z/items.jsonl"
rows = jl(rel)
webhooks_folder = None
for i, d in enumerate(rows):
    if d["depth"] == 0 and d["type"] == "apiDetailFolder" and d["name"] == "Webhooks":
        webhooks_folder = d["pointer"]
for i, d in enumerate(rows):
    name = d.get("name", "")
    needle = f'"name": {json.dumps(name, ensure_ascii=False)}'
    if d["depth"] == 0:
        c = maps.MERCHANT_API_DOCS.get(name)
        if c is None and d["type"] == "apiDetailFolder" and name == "Webhooks":
            c = maps.HEADING
        add("api-resources", f"Merchant API > {name}", rel, i + 1, needle, c)
    elif d["depth"] == 1 and d["type"] == "apiDetailFolder":
        add("api-resources", f"Merchant API > APIs > {name}", rel, i + 1, needle, maps.MERCHANT_API.get(name))
    elif d["depth"] == 1 and d["type"] == "doc" and d.get("parent") == webhooks_folder:
        add("api-resources", f"Merchant API > Webhooks > {name}", rel, i + 1, needle, maps.DUP_TOPIC)

# ---------- api-resources: other developer navigations (folders)
for nav, fmap in maps.OTHER_API_FOLDERS.items():
    rel = f"{S}/docs-sidebar/{nav}/items.jsonl"
    title = load_meta(os.path.dirname(rel)).get("nav_title", nav)
    for i, d in enumerate(jl(rel)):
        if d["type"] != "apiDetailFolder" or "name" not in d:
            continue
        name = d["name"]
        c = fmap.get(name, fmap.get("*"))
        add("api-resources", f"{title} > {name}", rel, i + 1, f'"name": {json.dumps(name, ensure_ascii=False)}', c)

# ---------- extension-points: developer docs navbar
rel = f"{S}/docs-navigation/v2@20261009T001017Z/items.jsonl"
for i, d in enumerate(jl(rel)):
    name = d.get("title") or d.get("name")
    key = "title" if "title" in d else "name"
    add("extension-points", f"docs navbar > {name}", rel, i + 1, f'"{key}": {json.dumps(name, ensure_ascii=False)}',
        maps.DOCS_NAVBAR.get(name))

# ---------- extension-points: app types offered when creating an app
rel = f"{S}/portal-app-categories/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"app type: {d['label']['en']}", rel, i + 1, f'"value": "{d["value"]}"', maps.APP_TYPES.get(d["value"]))

# ---------- extension-points: App Store categories
rel = f"{S}/app-categories/api@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"App Store category: {d['name']}", rel, i + 1, f'"name": {json.dumps(d["name"], ensure_ascii=False)}',
        maps.APP_CATEGORIES.get(d["name"]))
rel = f"{S}/app-categories/api-app-impact@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"App Store goal: {d['name']}", rel, i + 1, f'"name": {json.dumps(d["name"], ensure_ascii=False)}',
        "OOS: a merchant-goal tag for browsing the App Store (what an app helps with), not a part of the platform")
rel = f"{S}/portal-categories/app@partner-en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"app listing category: {d['name']['en']}", rel, i + 1, f'"slug": "{d["slug"]}"',
        maps.PORTAL_APP_CATEGORIES.get(d["slug"]))
rel = f"{S}/portal-categories/app_impact@partner-en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"app listing goal: {d['name']['en']}", rel, i + 1, f'"slug": "{d["slug"]}"',
        "OOS: a merchant-goal tag for an app's listing, not a part of the platform")
rel = f"{S}/portal-categories/theme@partner-en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"theme category: {d['name']['en']}", rel, i + 1, f'"position": {d["position"]}',
        "OOS: an industry sector used to classify themes, not a part of the platform")

# ---------- extension-points: App Functions supported events
rel = f"{S}/docs-event-lists/app-functions.supported-events/items.jsonl"
for i, d in enumerate(jl(rel)):
    nm = d["cells"].get("Event Name", "")
    add("extension-points", f"App Functions event: {nm.strip('*')}", rel, i + 1, nm, ["app_functions"])

# ---------- extension-points: storefront e-commerce events
for lab in sorted(os.listdir(os.path.join(OBS, S, "docs-event-lists"))):
    if not (lab.startswith("ecommerce-events.") or lab.startswith("ecommerc-events.")):
        continue
    rel = f"{S}/docs-event-lists/{lab}/items.jsonl"
    for i, d in enumerate(jl(rel)):
        # each item reads "`Event Name` - description"; the name is the part in backticks
        m = re.match(r"`([^`]+)`", d.get("item", ""))
        if not m:
            raise ValueError(f"no event name in {rel} item {i + 1}")
        nm = m.group(1)
        add("extension-points", f"Ecommerce event ({lab.split('.', 1)[1]}): {nm}", rel, i + 1, nm, ["storefront_events"])

# ---------- extension-points: Twilight web components
rel = f"{S}/twilight-components/docs-json@2.14.587/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("extension-points", f"Twilight component: {d['tag']}", rel, i + 1, f'"tag": "{d["tag"]}"', ["storefront_sdk_components"])

# ---------- access-scopes
rel = f"{S}/portal-app-scopes/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("access-scopes", d["slug"], rel, i + 1, f'"slug": "{d["slug"]}"', maps.SCOPES.get(d["slug"]))

# ---------- webhook-topics (union across Salla's lists; first list that shows a topic is cited)
seen = set()
rel = f"{S}/portal-webhook-events/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    t = d["slug"]
    seen.add(t)
    add("webhook-topics", t, rel, i + 1, f'"slug": "{t}"', maps.topic_concerns(t))


def topic_from_cell(s):
    m = re.search(r"`([a-z_.A-Z]+)\s*`", s)
    return m.group(1) if m else None


for lab, col in (("webhooks", "Name"), ("partner-apis.app-events", "Event Name"),
                 ("recurring-payments.webhook-events", "Event"), ("comm-apps.event-payload-reference", "Event")):
    rel = f"{S}/docs-event-lists/{lab}/items.jsonl"
    for i, d in enumerate(jl(rel)):
        t = topic_from_cell(d["cells"].get(col, ""))
        if not t or t in seen:
            continue
        seen.add(t)
        add("webhook-topics", t, rel, i + 1, t, maps.topic_concerns(t))
rel = f"{S}/docs-event-lists/webhook-events.communciation-apps/items.jsonl"
for i, d in enumerate(jl(rel)):
    t = topic_from_cell(d["cells"].get("Type", ""))
    if not t or t in seen:
        continue
    seen.add(t)
    c = maps.topic_concerns(t) if t == "auth.otp.verification" else ["communication_apps"]
    add("webhook-topics", t, rel, i + 1, t, c)

# ---------- settings: the Settings panel menu
rel = f"{S}/dashboard-settings-menu/merchant@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    if d["kind"] == "text":
        add("settings", d["text"], rel, i + 1, f'"text": {json.dumps(d["text"], ensure_ascii=False)}', maps.HEADING)
    else:
        add("settings", d["text"], rel, i + 1, f'"href": "{d["href"]}"', maps.SETTINGS_MENU.get(d["href"]))

# ---------- settings: sub-pages of the settings centre, named by the dashboard's settings translations
sc = f"{S}/settings-center/merchant@en/items.jsonl"
tr = f"{S}/dashboard-translations/en/settings.json"
tr_line = lines(tr)[0]
tr_obj = json.loads(tr_line)
sc_date = meta_date(load_meta(os.path.dirname(sc)))
for i, d in enumerate(jl(sc)):
    if d["kind"] != "s:section":
        continue
    sec = d["section"]
    if "/" not in sec and sec != "markets":
        continue  # top-level pages are inventoried from the settings menu
    label = tr_obj.get(sec)
    if not label:
        add("settings", sec, sc, i + 1, f'"section": "{sec}"', maps.settings_sub_concerns(sec))
        continue
    q = f'{json.dumps(sec, ensure_ascii=False)}:{json.dumps(label, ensure_ascii=False)}'
    add("settings", label, tr, 1, q, maps.settings_sub_concerns(sec), struct_dir=f"{S}/dashboard-translations",
        date=sc_date, date_basis=f"undated list; settings centre section {sec} held {sc_date}; label from the dashboard's settings translations",
        locator=f'key "{sec}" (settings centre section, items.jsonl line {i + 1})', quote=q)

# ---------- admin-navigation: merchant dashboard main navigation (en)
rel = f"{S}/dashboard-main-navigation/merchant@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    text = d.get("text", "")
    if d["kind"] == "link":
        c = maps.MAIN_NAV_HREF.get(d["href"])
        add("admin-navigation", text, rel, i + 1, f'"href": "{d["href"]}"', c)
    elif d["kind"] == "button":
        c = maps.MAIN_NAV_BUTTON.get(text) or "OOS: a menu button that opens a group whose links are inventoried one by one"
        add("admin-navigation", text or "(button)", rel, i + 1, f'"position": {d["position"]}', c)
    else:
        c = maps.HEADING if d.get("parent") == 0 else "OOS: an action button inside a page that is inventoried itself"
        add("admin-navigation", text, rel, i + 1, f'"text": {json.dumps(text, ensure_ascii=False)}', c)

# ---------- admin-navigation: Salla Partners portal side menu (en)
rel = f"{S}/partners-portal-navigation/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    text = d.get("text", "")
    if d["kind"] == "link":
        add("admin-navigation", f"Partners portal > {text or '(no text)'}", rel, i + 1, f'"position": {d["position"]}', maps.PARTNER_NAV.get(d["href"]))
    else:
        add("admin-navigation", f"Partners portal > {text}", rel, i + 1, f'"position": {d["position"]}', maps.HEADING)

# ---------- plan-features: plans offered in the merchant dashboard (ar)
rel = f"{S}/merchant-plans/merchant@ar/items.jsonl"
for i, d in enumerate(jl(rel)):
    plan = d["name"]
    for f in d["features"]:
        needle = f'"title": {json.dumps(f["title"], ensure_ascii=False)}, "description": {json.dumps(f["description"], ensure_ascii=False)}, "icon": {json.dumps(f["icon"], ensure_ascii=False)}, "code": "{f["code"]}"'
        add("plan-features", f"{plan}: {f['title']}", rel, i + 1, needle, maps.PLAN_TITLES.get(f["title"]),
            locator=f"line {i + 1} (plan {plan}), feature code {f['code']}")
        for s in f.get("sub_features", []):
            nd = f'"parent_code": "{f["code"]}", "title": {json.dumps(s["title"], ensure_ascii=False)}'
            add("plan-features", f"{plan}: {s['title']}", rel, i + 1, nd, maps.PLAN_TITLES.get(s["title"]),
                locator=f"line {i + 1} (plan {plan}), sub-feature of {f['code']}")

# ---------- plan-features: salla.com plans page, key features per market (ar-sa, ar-ae)
for market in ("ar-sa", "ar-ae"):
    rel = f"{S}/com-plans/{market}/text.txt"
    ls = lines(rel)
    start = next(n for n, l in enumerate(ls) if l.strip() == "المزايا الأساسية")
    cap = meta_date(load_meta(os.path.dirname(rel)))
    add("plan-features", f"salla.com plans ({market}): المزايا الأساسية", rel, start + 1, "المزايا الأساسية", maps.HEADING,
        date_basis=f"undated page; held copy captured {cap}")
    n = start + 1
    while n < len(ls) and not ls[n].startswith("انضم لأكثر من"):
        t = ls[n].strip()
        c = maps.PLAN_KEYS_AR.get(t, maps.PLAN_SECTION_OOS)
        add("plan-features", f"salla.com plans ({market}): {t}", rel, n + 1, t, c,
            date_basis=f"undated page; held copy captured {cap}")
        n += 1

# ---------- plan-features: Salla Special page (ar-sa; the ar-ae page is identical)
rel = f"{S}/com-specialplan/ar-sa/text.txt"
for t, c in maps.SPECIAL_LINES.items():
    n = find_line(rel, t)
    add("plan-features", f"Salla Special page: {t}", rel, n, t, c)

# ---------- legal-agreements: footer of salla.com pages (plans page, ar-sa)
rel = f"{S}/com-plans/ar-sa/text.txt"
for t, c in maps.FOOTER_LEGAL.items():
    n = find_line(rel, t)
    add("legal-agreements", t, rel, n, t, c, date_basis="undated footer; held copy captured 2026-10-08")

# ---------- other: the footer's list of countries Salla's site says it is available in
rel = f"{S}/com-plans/ar-sa/text.txt"
for t, c in maps.FOOTER_MARKETS.items():
    n = find_line(rel, t)
    add("other:footer-markets", t, rel, n, t, c, date_basis="undated footer; held copy captured 2026-10-08")

# ---------- legal-agreements: policy pages listed in salla.com's sitemaps
for sm, label in (("sitemap_ar-SA.xml", "ar-SA"), ("sitemap_en-SA.xml", "en-SA"), ("sitemap_ar-AE.xml", "ar-AE"), ("sitemap_en-AE.xml", "en-AE")):
    rel = f"salla.com/{sm}"
    for n, l in enumerate(lines(rel)):
        m = re.search(r"<loc>(https://salla\.com/[^<]*)</loc>", l)
        if not m:
            continue
        u = m.group(1)
        path = urllib.parse.unquote(urllib.parse.urlparse(u).path)
        p2 = re.sub(r"^/(en-sa|ar-ae|en-ae)", "", path)
        c = maps.legal_path_concerns(p2)
        if c is None:
            continue
        add("legal-agreements", u, rel, n + 1, f"<loc>{u}</loc>", c, struct_dir=f"{S}/com-sitemaps/sitemap-{label.lower()}-xml",
            date_basis=f"undated sitemap entry; held sitemap captured {meta_date(load_meta(f'{S}/com-sitemaps/sitemap-{label.lower()}-xml'))}")

# ---------- other: staff permissions (groups and permissions)
rel = f"{S}/staff-permission-groups/demo@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("other:staff-permissions", d["name"], rel, i + 1, f'"name": {json.dumps(d["name"], ensure_ascii=False)}, "label"', maps.HEADING)
    for p in d.get("permissions", []):
        add("other:staff-permissions", p["name"], rel, i + 1, f'"name": "{p["name"]}"', maps.perm_concerns(p["name"]),
            locator=f"line {i + 1} (group {d['name']})")

# ---------- other: permissions a partner may request on a merchant's store
rel = f"{S}/portal-stores-access-requests-permissions/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    gname = d["name"]["en"]
    add("other:partner-access-permissions", gname, rel, i + 1, f'"en": {json.dumps(gname, ensure_ascii=False)}}}, "permissions"', maps.HEADING)
    for p in d.get("permissions", []):
        c = maps.perm_concerns(p["key"])
        add("other:partner-access-permissions", p["key"], rel, i + 1, f'"key": "{p["key"]}"', c,
            locator=f"line {i + 1} (group {gname})")

# ---------- other: order statuses
rel = f"{S}/order-statuses/merchant@ar/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("other:order-statuses", d["name"], rel, i + 1, f'"name": {json.dumps(d["name"], ensure_ascii=False)}, "type"', maps.ORDER_STATUSES)

# ---------- other: payment methods shown on Salla stores (showcase)
rel = f"{S}/showcase-store-payments/com-en-sa/items.jsonl"
seenm = set()
for i, d in enumerate(jl(rel)):
    for m in d.get("payments", []):
        if m in seenm:
            continue
        seenm.add(m)
        add("other:store-payment-methods", m, rel, i + 1, f'"{m}"', maps.STORE_PAYMENT_METHODS.get(m),
            locator=f"line {i + 1} (first store whose page lists it)")

# ---------- other: countries an app listing may declare support for
rel = f"{S}/portal-apps-supported-countries/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("other:app-supported-countries", d["name"]["en"], rel, i + 1, f'"code": "{d["code"]}"', ["salla_markets_served", "app_store"])

# ---------- other: the partner portal's country picker
rel = f"{S}/portal-countries/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("other:portal-countries", d["name"]["en"], rel, i + 1, f'"code": "{d["code"]}"', ["geo_reference_data"])

# ---------- other: partner payout statuses
rel = f"{S}/portal-payouts-filters/partner@en/items.jsonl"
for i, d in enumerate(jl(rel)):
    lab = (d.get("label") or {}).get("en") if d.get("label") else None
    for ch in d.get("children", []):
        if ch.get("name") == "status":
            for o in ch.get("options", []):
                en = o["label"]["en"]
                c = "OOS: the 'All' option of the filter, not a status" if o["value"] == "" else ["app_billing_partner_payouts"]
                add("other:partner-payout-statuses", en, rel, i + 1, f'"value": "{o["value"]}"', c,
                    locator=f"line {i + 1} (filter group {lab})")

# ---------- other: partner ID verification (types and statuses)
for lab, name in (("portal-settings-verification-id/partner@en", "partner-id-types"), ("portal-settings-verification-id-profile/partner@en", "partner-id-statuses")):
    rel = f"{S}/{lab}/items.jsonl"
    for i, d in enumerate(jl(rel)):
        add(f"other:{name}", d["label"]["en"], rel, i + 1, f'"value": {d["value"]}', ["partner_account"])

# ---------- other: dashboard feature flags
rel = f"{S}/dashboard-features/merchant@en/items.jsonl"
fidx = maps.flag_index()
for i, d in enumerate(jl(rel)):
    nm = d["name"]
    c = fidx.get(nm) or maps.FLAG_OOS
    add("other:dashboard-features", nm, rel, i + 1, f'"name": "{nm}"', c)

# ---------- other: the dashboard's registry of its apps (micro-frontends)
rel = f"{S}/dashboard-apps/prod/items.jsonl"
for i, d in enumerate(jl(rel)):
    add("other:dashboard-apps", d["name"], rel, i + 1, f'"name": "{d["name"]}"', maps.dashboard_app_concerns(d["name"]))

os.makedirs(os.path.join(OUT, "scripts", "build"), exist_ok=True)
json.dump(ROWS, open(os.path.join(OUT, "scripts", "build", "inventory_build.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
from collections import Counter
print("rows", len(ROWS))
print(Counter(r["list"] for r in ROWS))
print("unmapped", len(UNMAPPED))
for u in UNMAPPED:
    print("  UNMAPPED", u)
