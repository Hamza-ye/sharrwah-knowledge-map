# Build the raw inventory from Shopify's own lists held in observed-sh@b46731d0 and from
# two live pages read in this run. Every row carries a verbatim quote and a line locator.
# Output: work/inventory_raw.tsv
# Columns: list, entry, group, extra, source, file, locator, quote, source_date, date_basis, access_path
# Run: python3 -I build_inventory.py
import json, os, re, glob

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBS = "/home/user/observed-sh/"
S = OBS + "structures/shopify/"
FETCHED = os.path.join(OUT, "fetched")
ROWS = []

def meta_date(d):
    """First ISO date found in the structure's meta.json (the capture date)."""
    p = os.path.join(d, "meta.json")
    if not os.path.exists(p):
        p = os.path.join(os.path.dirname(d), "meta.json")
    t = open(p, encoding="utf-8").read()
    m = re.search(r"(20\d\d-\d\d-\d\d)", t)
    if m:
        return m.group(1)
    m = re.search(r"(20\d\d)(\d\d)(\d\d)T\d{6}Z", t)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

def src_of(path):
    return "observed-sh@b46731d0:" + os.path.relpath(path, OBS)

def frag(raw, key, value):
    """The verbatim JSON fragment for key/value as it appears in the raw line."""
    cands = []
    for ea in (True, False):
        v = json.dumps(value, ensure_ascii=ea)
        cands += [f'"{key}": {v}', f'"{key}":{v}']
    for c in cands:
        if c in raw:
            return c
    for ea in (True, False):
        v = json.dumps(value, ensure_ascii=ea)
        if v in raw:
            return v
    raise ValueError(f"fragment not found: {key}={value!r}")

def add(lst, entry, group, extra, path, lineno, quote, sdate, basis=None, access="local", source=None, locator=None):
    if len(quote) > 320:
        quote = quote[:320]
        # keep verbatim prefix
    ROWS.append(dict(list=lst, entry=entry, group=group or "", extra=extra or "",
                     source=source or src_of(path), file=path,
                     locator=locator or f"line {lineno}", quote=quote, source_date=sdate,
                     date_basis=basis or f"undated list; captured {sdate} (meta.json)",
                     access_path=access))

def lines(path):
    with open(path, encoding="utf-8") as fh:
        for i, raw in enumerate(fh, 1):
            raw = raw.rstrip("\n")
            if raw.strip():
                yield i, raw, json.loads(raw)

# ---------------------------------------------------------------- api-resources
d = S + "admin-graphql-reference-nav/shopify.dev@latest"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("api-resources", it["label"], "GraphQL Admin API reference", it["key"], d + "/items.jsonl", i,
        frag(raw, "label", it["label"]), sd, locator=f"line {i} (top-level category of the GraphQL Admin API reference navigation)")

d = S + "dev-docs-nav/shopify.dev@2026-10-07"; sd = meta_date(d)
navs = {}
for i, raw, it in lines(d + "/items.jsonl"):
    navs[it["uri"]] = (i, raw, it["values"].get("loaderData.*.navData"))

# API references sidebar (as stated on the API reference pages; read from the Ajax API page's loader data)
i, raw, nd = navs["https://shopify.dev/docs/api/ajax"]
def walk(nodes, groupname, depth):
    for n in nodes:
        label = n.get("label")
        if n.get("isGroup") and depth == 0:
            walk(n.get("children") or [], label, 1)
            continue
        add("api-resources", label, "API references: " + groupname, n.get("href") or "",
            d + "/items.jsonl", i, frag(raw, "label", label), sd,
            locator=f"line {i} (uri https://shopify.dev/docs/api/ajax, loaderData navData, group '{groupname}')")
        if n.get("children") and depth < 2:
            walk(n["children"], groupname + " > " + label, depth + 1)
walk(nd["navItems"], "", 0)

def nav_children(uri, fn):
    i, raw, nd = navs[uri]
    fn(i, raw, nd)

# Functions API reference
def fx(i, raw, nd):
    for n in nd["navItems"][0]["children"]:
        if n.get("children") and n["label"] == "Deprecated APIs":
            for k in n["children"]:
                add("api-resources", k["label"], "Shopify Functions API reference > Deprecated APIs", k.get("href", ""),
                    d + "/items.jsonl", i, frag(raw, "label", k["label"]), sd,
                    locator=f"line {i} (uri https://shopify.dev/docs/api/functions/latest, navData)")
        else:
            add("api-resources", n["label"], "Shopify Functions API reference", n.get("href", ""),
                d + "/items.jsonl", i, frag(raw, "label", n["label"]), sd,
                locator=f"line {i} (uri https://shopify.dev/docs/api/functions/latest, navData)")
nav_children("https://shopify.dev/docs/api/functions/latest", fx)

# Storefront API reference categories
def sf(i, raw, nd):
    for n in nd["navItems"]:
        if n["label"] == "GraphQL Types":
            continue
        add("api-resources", n["label"], "Storefront API reference", n.get("key", ""),
            d + "/items.jsonl", i, frag(raw, "label", n["label"]), sd,
            locator=f"line {i} (uri https://shopify.dev/docs/api/storefront/latest, navData top-level category)")
nav_children("https://shopify.dev/docs/api/storefront/latest", sf)

# Customer Account API reference: its one category holds the root queries and mutations
def ca(i, raw, nd):
    for n in nd["navItems"]:
        if n["label"] != "Common objects":
            continue
        for g in n["children"]:
            if g["label"] in ("Queries", "Mutations"):
                for k in g["children"]:
                    add("api-resources", k["label"], "Customer Account API reference > Common objects > " + g["label"], k.get("href", ""),
                        d + "/items.jsonl", i, frag(raw, "label", k["label"]), sd,
                        locator=f"line {i} (uri https://shopify.dev/docs/api/customer/latest, navData, {g['label']})")
nav_children("https://shopify.dev/docs/api/customer/latest", ca)

# Payments Apps API reference: groups, and the mutations the Payment Processing group names
def pa(i, raw, nd):
    for n in nd["navItems"]:
        if n["label"] == "GraphQL Types":
            continue
        add("api-resources", n["label"], "Payments Apps API reference", "",
            d + "/items.jsonl", i, frag(raw, "label", n["label"]), sd,
            locator=f"line {i} (uri https://shopify.dev/docs/api/payments-apps/latest, navData top-level category)")
        for g in n.get("children") or []:
            if g["label"] in ("Mutations", "Queries"):
                for k in g["children"]:
                    add("api-resources", k["label"], f"Payments Apps API reference > {n['label']} > {g['label']}", k.get("href", ""),
                        d + "/items.jsonl", i, frag(raw, "label", k["label"]), sd,
                        locator=f"line {i} (uri https://shopify.dev/docs/api/payments-apps/latest, navData, {n['label']} > {g['label']})")
nav_children("https://shopify.dev/docs/api/payments-apps/latest", pa)

# Events API reference resources
def ev(i, raw, nd):
    for n in nd["navItems"]:
        for k in n.get("children") or []:
            add("api-resources", k["label"], "Events API reference", k.get("href", ""),
                d + "/items.jsonl", i, frag(raw, "label", k["label"]), sd,
                locator=f"line {i} (uri https://shopify.dev/docs/api/events/latest, navData)")
nav_children("https://shopify.dev/docs/api/events/latest", ev)

# Partner API reference categories
def pt(i, raw, nd):
    for n in nd["navItems"]:
        if n["label"] == "GraphQL Types":
            continue
        add("api-resources", n["label"], "Partner API reference", "",
            d + "/items.jsonl", i, frag(raw, "label", n["label"]), sd,
            locator=f"line {i} (uri https://shopify.dev/docs/api/partner/latest, navData top-level category)")
nav_children("https://shopify.dev/docs/api/partner/latest", pt)

# ---------------------------------------------------------------- access-scopes
d = S + "dev-dashboard-scopes/dev-dashboard@select-scopes"; sd = meta_date(d)
items = list(lines(d + "/items.jsonl"))
bypos = {it["position"]: it for _, _, it in items}
seen_scopes = set()
for i, raw, it in items:
    t = it.get("text") or ""
    if "parent" in it and re.fullmatch(r"(unauthenticated_|customer_)?(read|write)_[a-z0-9_]+", t):
        res = bypos[it["parent"]]["text"]
        api = ""
        for _, _, k in items:
            if k.get("parent") == it["parent"] and k.get("text") in ("Admin API", "Customer Account API", "Storefront API", "Shop API"):
                api = k["text"]; break
        add("access-scopes", t, res, api, d + "/items.jsonl", i, frag(raw, "text", t), sd,
            locator=f"line {i} (resource '{res}', {api})")
        seen_scopes.add(t)

# access-scopes doc page (live .md): scopes it names that the Dev Dashboard list does not
md = os.path.join(FETCHED, "shopify.dev_docs_api_usage_access-scopes.md")
section = ""
for i, line in enumerate(open(md, encoding="utf-8"), 1):
    line = line.rstrip("\n")
    if line.startswith("## "):
        section = line[3:]
    if not line.startswith("| `"):
        continue
    first_cell = line.split(" | ")[0]
    for s in re.findall(r"`([a-z0-9_]+)`", first_cell):
        if s in seen_scopes:
            continue
        seen_scopes.add(s)
        add("access-scopes", s, "access-scopes page: " + section, "", md, i, "`" + s + "`", "2026-10-10",
            basis="undated live page; read 2026-10-10", access="md",
            source="https://shopify.dev/docs/api/usage/access-scopes.md",
            locator=f"line {i} (section '{section}')")

# ---------------------------------------------------------------- webhook-topics
d = S + "cli-webhook-topics/app-webhook-trigger@2026-10"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("webhook-topics", it["value"], "CLI allowed topics (API 2026-10)", "", d + "/items.jsonl", i,
        frag(raw, "value", it["value"]), sd)
d = S + "admin-webhook-topics/fake-demo-sharrwah"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    x = it["item"]
    add("webhook-topics", x["description"], "Admin webhook topics (Settings > Notifications > Webhooks)", x["topic"],
        d + "/items.jsonl", i, frag(raw, "description", x["description"]), sd)

# ---------------------------------------------------------------- settings
seen = set()
for inst in ["ibx5bt-xy", "demo-fake-dev-store", "fake-demo-sharrwah"]:
    d = S + "admin-settings-nav/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        k = it["id"]
        if k in seen:
            continue
        seen.add(k)
        grp = it.get("scope") or ("child of " + it.get("parent", ""))
        add("settings", it["title"], "Settings navigation (" + grp + ")", k, d + "/items.jsonl", i,
            frag(raw, "title", it["title"]), sd, locator=f"line {i} (id {k})")

# ---------------------------------------------------------------- admin-navigation
navlabels = {}
for inst, rng in [("fake-demo-sharrwah@settings-subscribe-select-plan", range(1, 32)),
                  ("demo-fake-dev-store@settings-organization-account", range(1, 34))]:
    d = S + "admin-main-nav/" + inst; sd = meta_date(d)
    items = list(lines(d + "/items.jsonl"))
    bypos = {it["position"]: it for _, _, it in items}
    for i, raw, it in items:
        if it["position"] not in rng:
            continue
        t = it.get("text") or ""
        href = it.get("href") or ""
        par = bypos.get(it.get("parent")) if it.get("parent") is not None else None
        ptxt = re.sub(r"\d+$", "", par["text"]) if par else ""
        key = (ptxt, t)
        if not t or key in navlabels:
            continue
        if re.search(r"\d$", t):  # badge counts appended to labels ('Orders3')
            continue
        navlabels[key] = t
        grp = "Main navigation" + (" > " + ptxt if par else "")
        add("admin-navigation", t, grp, href, d + "/items.jsonl", i, frag(raw, "text", t), sd)

d = S + "admin-router"; sd = meta_date(d)
seen = set()
for i, raw, it in lines(d + "/items.jsonl"):
    s = it.get("section")
    if not s or s in seen:
        continue
    seen.add(s)
    add("admin-navigation", s, "Admin router section", it["id"], d + "/items.jsonl", i, frag(raw, "section", s), sd,
        locator=f"line {i} (first route of section {s}: {it['id']})")

# ---------------------------------------------------------------- roles and permissions
seen = set()
for inst in ["org-239421532", "ctcbwa-r1"]:
    d = S + "admin-roles/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        if it["name"] in seen:
            continue
        seen.add(it["name"])
        add("other:staff-roles", it["name"], "Roles (" + str(it.get("category")) + ")", it.get("roleType", ""),
            d + "/items.jsonl", i, frag(raw, "name", it["name"]), sd)

d = S + "collaborator-access-permissions/org-239421532@request-access"; sd = meta_date(d)
section = sub = ""
for i, raw, it in lines(d + "/items.jsonl"):
    if it["type"] == "mark":
        lab = it["label"]
        if re.search(r" \d+/\d+$", lab):
            section = re.sub(r" \d+/\d+$", "", lab); sub = ""
            add("other:staff-permissions", lab, "Collaborator request permissions: section", "", d + "/items.jsonl", i,
                frag(raw, "label", lab), sd)
        else:
            sub = lab
            add("other:staff-permissions", section + " > " + lab, "Collaborator request permissions: sub-group", "",
                d + "/items.jsonl", i, frag(raw, "label", lab), sd)
        continue
    if it.get("label"):
        ent = section + (" > " + sub if sub else "") + " > " + it["label"]
        add("other:staff-permissions", ent, "Collaborator request permissions: " + section, it.get("value", ""),
            d + "/items.jsonl", i, frag(raw, "value", it["value"]), sd)

d = S + "admin-assignable-permissions/ctcbwa-r1"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("other:staff-permissions", it["value"], "Organization assignable store permissions", "",
        d + "/items.jsonl", i, frag(raw, "value", it["value"]), sd)

d = S + "partner-api-client-permissions/partner-5236935@new"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    if it["type"] == "checkbox":
        add("other:partner-permissions", it["label"], "Partner API client permission sets", it["value"],
            d + "/items.jsonl", i, frag(raw, "label", it["label"]), sd)

# ---------------------------------------------------------------- plan-features
d = S + "plan-comparison-public/www.shopify.com_pricing"; sd = meta_date(d)
group = ""
for i, raw, it in lines(d + "/items.jsonl"):
    if it.get("kind") != "row" or it.get("section") != 1:
        continue
    c0 = it["cells"][0]
    if c0["tag"] == "th" and c0.get("colspan") == "5":
        group = c0["text"]
        add("plan-features", group, "Public pricing: section", "", d + "/items.jsonl", i, frag(raw, "text", group), sd)
        continue
    if c0["tag"] == "th":
        vals = " | ".join(c["text"] for c in it["cells"][1:])
        add("plan-features", c0["text"], "Public pricing: " + group, vals, d + "/items.jsonl", i, frag(raw, "text", c0["text"]), sd)
    else:
        add("plan-features", c0["text"], "Public pricing: " + group + " (footnote row)", "", d + "/items.jsonl", i, frag(raw, "text", c0["text"]), sd)

d = S + "plan-comparison-admin/ibx5bt-xy"; sd = meta_date(d)
groups = {}
for i, raw, it in lines(d + "/items.jsonl"):
    if it["kind"] == "container":
        if it["position"] == 0:
            continue
        groups[it["position"]] = it["text_outside_rows"]
        add("plan-features", it["text_outside_rows"], "Admin plan comparison: group", "", d + "/items.jsonl", i,
            frag(raw, "text_outside_rows", it["text_outside_rows"]), sd)
    else:
        add("plan-features", it["label"], "Admin plan comparison: " + groups.get(it["container"], ""), " | ".join(it["cells"]),
            d + "/items.jsonl", i, frag(raw, "label", it["label"]), sd)

d = S + "billing-plans/2jiwxs-gr"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("plan-features", it["plan.name"], "Billing plans (internal names)", it.get("plan.monthlyPrice.amount", ""),
        d + "/items.jsonl", i, frag(raw, "plan.name", it["plan.name"]), sd)

d = glob.glob(S + "dev-store-plans/*")[0]; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("plan-features", it["label"], "Development store plans", it["value"], d + "/items.jsonl", i, frag(raw, "value", it["value"]), sd)

seen = set()
for inst in ["fake-demo-sharrwah@charges-filter", "fake-demo-sharrwah@expense-report"]:
    d = S + "billing-charge-categories/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        if it["value"] in seen:
            continue
        seen.add(it["value"])
        add("other:billing-charge-categories", it["label"], "Billing charge categories (" + inst.split("@")[1] + ")", it["value"],
            d + "/items.jsonl", i, frag(raw, "value", it["value"]), sd)

# ---------------------------------------------------------------- legal-agreements
d = S + "shopify-legal-index/www.shopify.com_legal"; sd = meta_date(d)
items = list(lines(d + "/items.jsonl"))
heading = ""
for idx, (i, raw, it) in enumerate(items):
    t = it["text"]
    if it["kind"] == "text":
        nxt = items[idx + 1][2] if idx + 1 < len(items) else None
        if nxt and nxt["kind"] == "text" and it["position"] >= 2:
            heading = t
            add("legal-agreements", t, "Shopify Legal index: heading", "", d + "/items.jsonl", i, frag(raw, "text", t), sd)
        continue
    add("legal-agreements", t, "Shopify Legal index: " + heading, it.get("href", ""), d + "/items.jsonl", i, frag(raw, "text", t), sd)

# financial products named on the financial complaint form (live page)
fc = os.path.join(FETCHED, "www.shopify.com_legal_tools_report-an-issue_financial-complaint.rendered.txt")
fl = open(fc, encoding="utf-8").read().split("\n")
start = fl.index("Please select") if "Please select" in fl else None
if start is not None:
    for j in range(start + 1, len(fl)):
        t = fl[j].strip()
        if not t or t == "Financial product":
            break
        add("legal-agreements", t, "Financial complaint form: products", "", fc, j + 1, t, "2026-10-10",
            basis="undated live page; read 2026-10-10", access="rendered",
            source="https://www.shopify.com/legal/tools/report-an-issue/financial-complaint",
            locator=f"line {j + 1} (Complaint details select)")

# ---------------------------------------------------------------- extension-points
d = S + "cli-extension-templates/cdn.shopify.com@templates.json"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    ent = f"{it['name']} ({it['identifier']})"
    add("extension-points", ent, "CLI extension templates: " + it.get("group", ""), it.get("type", ""),
        d + "/items.jsonl", i, frag(raw, "identifier", it["identifier"]), sd)

for inst in ["admin@2026.10.0-rc.11", "checkout@2026.7.1", "customer-account@2026.7.1", "point-of-sale@2026.7.1"]:
    d = S + "ui-extension-targets/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        add("extension-points", it["target"], "UI extension targets: " + inst, it.get("type", "") if isinstance(it.get("type"), str) else "",
            d + "/items.jsonl", i, frag(raw, "target", it["target"]), sd)

for inst in ["capture-plus@installed", "capture-plus@first-party"]:
    d = S + "flow-connectors/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        add("extension-points", it["name"], "Flow connectors (" + inst.split("@")[1] + ")", it.get("id", ""),
            d + "/items.jsonl", i, frag(raw, "name", it["name"]), sd)

d = S + "web-pixel-events/shopify.dev@2026-09-30"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    grp = it["uri"].split("/web-pixels-api/")[1].split("/")[0]
    add("extension-points", it["title"], "Web Pixels API: " + grp, it["uri"], d + "/items.jsonl", i, frag(raw, "title", it["title"]), sd)

# ---------------------------------------------------------------- sign-up, entities, accounts
d = S + "business-entity-types/fake-demo-sharrwah@types"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("other:business-entities", it["label"].split(" ")[0] if it["value"] != "default_non_profit" else "Non-Profit",
        "Business entity types (Add business entity)", it["value"], d + "/items.jsonl", i, frag(raw, "value", it["value"]), sd)
d = S + "business-entity-types/fake-demo-sharrwah@countries"; sd = meta_date(d)
first = next(lines(d + "/items.jsonl"))
add("other:business-entities", "Add business entity: country list (237 options)", "Business entity countries", "value list",
    d + "/items.jsonl", first[0], frag(first[1], "label", first[2]["label"]), sd,
    locator="lines 1-237 (one option per line; first option quoted)")
for inst, label in [("accounts.shopify.com@signup", "I'm located in: (233 options)"),
                    ("partners.shopify.com@create-organization", "Country/region (233 options)")]:
    d = S + "signup-countries/" + inst; sd = meta_date(d)
    first = next(lines(d + "/items.jsonl"))
    add("other:signup", label, "Sign-up country list (" + inst + ")", "value list", d + "/items.jsonl", first[0],
        frag(first[1], "label", first[2]["label"]), sd, locator="lines 1-233 (one option per line; first option quoted)")
for inst in sorted(os.listdir(S + "sign-in-methods")):
    d = S + "sign-in-methods/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        t = it.get("text") or ""
        al = it.get("aria_label") or ""
        if re.search(r"(Continue with|Sign in with)", t):
            add("other:signup", t, "Sign-in methods (" + inst + ")", it.get("kind", ""), d + "/items.jsonl", i, frag(raw, "text", t), sd)
        elif re.search(r"Continue with", al):
            add("other:signup", al, "Sign-up methods (" + inst + ")", it.get("kind", ""), d + "/items.jsonl", i, frag(raw, "aria_label", al), sd)
d = S + "account-destinations/accounts.shopify.com"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    if it.get("kind") == "link" and it.get("text"):
        add("other:account-destinations", it["text"], "Where do you want to go?", it.get("href", ""), d + "/items.jsonl", i, frag(raw, "text", it["text"]), sd)

# ---------------------------------------------------------------- commerce protocol (UCP)
d = S + "storefront-ucp-profile/capture-plus"; sd = meta_date(d)
sj = d + "/source.json"
src_text = open(sj, encoding="utf-8").read()
prof = json.loads(src_text)["ucp"]
for k in prof["services"]:
    add("other:ucp", k, "UCP merchant profile: services", "", sj, 0, f'"{k}"', sd, locator=f"ucp.services.{k}")
for k in prof["capabilities"]:
    add("other:ucp", k, "UCP merchant profile: capabilities", "", sj, 0, f'"{k}"', sd, locator=f"ucp.capabilities.{k}")
for k in prof["payment_handlers"]:
    add("other:ucp", k, "UCP merchant profile: payment handlers", "", sj, 0, f'"{k}"', sd, locator=f"ucp.payment_handlers.{k}")
d = S + "ucp-agent-profile/shopify.dev@2026-04-08-valid-with-capabilities"; sd = meta_date(d)
sj = d + "/source.json"
ap = json.load(open(sj, encoding="utf-8"))
ap = ap.get("ucp", ap)
for k in ap.get("capabilities", {}):
    add("other:ucp", k, "UCP agent profile: capabilities", "", sj, 0, f'"{k}"', sd, locator=f"ucp.capabilities.{k}")
d = S + "storefront-ucp-mcp-tools/capture-plus"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    add("other:ucp", it["name"], "Store MCP endpoint tools", "", d + "/items.jsonl", i, frag(raw, "name", it["name"]), sd)

# ---------------------------------------------------------------- app store categories
d = S + "app-store-taxonomy/apps.shopify.com_categories"; sd = meta_date(d)
for i, raw, it in lines(d + "/pages.jsonl"):
    crumbs = [c["name"] for c in (it.get("breadcrumb") or [])]
    grp = " > ".join(crumbs[:-1]) if crumbs else "top level"
    add("other:app-store-categories", it["h1"], "App Store categories: " + grp, it["url"], d + "/pages.jsonl", i, frag(raw, "h1", it["h1"]), sd)

# ---------------------------------------------------------------- Shopify's own product menu (shopify.com header)
d = S + "shopify-com-header-nav/www.shopify.com"; sd = meta_date(d)
items = list(lines(d + "/items.jsonl"))
in_products = False; grp = ""
for i, raw, it in items:
    t = it.get("text") or ""
    if t == "Products":
        in_products = True; continue
    if not in_products:
        continue
    if t in ("Non-stop innovation", "NON-STOP INNOVATION", "Latest updates", "Pricing", "Enterprise"):
        break
    if it["kind"] == "text" and t.isupper():
        grp = t; continue
    if it["kind"] == "text" and not it.get("href"):
        # descriptions under a link are not entries
        continue
    add("other:shopify-com-products", t, "shopify.com header > Products > " + grp, it.get("href", ""), d + "/items.jsonl", i, frag(raw, "text", t), sd)

# ---------------------------------------------------------------- Shopify's own apps (Google Play publisher page)
d = S + "play-publisher-apps/google-play@pub-shopify-inc"; sd = meta_date(d)
seen = set()
for i, raw, it in lines(d + "/items.jsonl"):
    desc = it.get("desc") or ""
    if "\nShopify Inc.\n" in desc:
        name = desc.split("\n")[0]
        if name in seen:
            continue
        seen.add(name)
        add("other:shopify-apps", name, "Google Play publisher Shopify Inc.", "", d + "/items.jsonl", i, frag(raw, "desc", desc)[:200] if False else json.dumps(name)[1:-1], sd)

# ---------------------------------------------------------------- notifications and translations
d = S + "notification-templates/customer@fake-demo-sharrwah"; sd = meta_date(d)
grp = ""
for i, raw, it in lines(d + "/items.jsonl"):
    if it["role"] == "heading" and it["name"] not in ("Customer notifications",):
        grp = it["name"]
        add("other:notification-templates", grp, "Customer notifications: group", "", d + "/items.jsonl", i, frag(raw, "name", grp), sd)
    elif it["role"] == "link" and it["name"] not in ("Notifications", "Customize email templates") and grp:
        add("other:notification-templates", it["name"], "Customer notifications: " + grp, "", d + "/items.jsonl", i, frag(raw, "name", it["name"]), sd)
d = S + "notification-templates/staff@fake-demo-sharrwah"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    nm = it.get("name") or ""
    if it.get("role") in ("link", "heading") and nm and nm not in ("Notifications",):
        add("other:notification-templates", nm, "Staff notifications", it.get("role", ""), d + "/items.jsonl", i, frag(raw, "name", nm), sd)

d = S + "translatable-resources/translate-and-adapt@capture-plus"; sd = meta_date(d)
grp = ""
for i, raw, it in lines(d + "/items.jsonl"):
    if it["role"] == "heading" and it["depth"] == 1 and it["name"] != "Localized content:":
        grp = it["name"]
    elif it["role"] == "button" and it["depth"] == 1 and it["name"] not in ("View store",):
        add("other:translatable-resources", it["name"], "Translate & Adapt: " + grp, "", d + "/items.jsonl", i, frag(raw, "name", it["name"]), sd)

# ---------------------------------------------------------------- partner dashboard and app store registration
d = S + "partner-dashboard-nav/partner-5236935@after-email-verified"; sd = meta_date(d)
for i, raw, it in lines(d + "/items.jsonl"):
    if it.get("kind") == "link" and it.get("text") and it["text"] != "Return to home page":
        add("other:partner-dashboard", it["text"], "Partner Dashboard navigation (after email verified)", it.get("href", ""), d + "/items.jsonl", i, frag(raw, "text", it["text"]), sd)

# ---------------------------------------------------------------- value lists recorded as one entry each
for sid, inst, key, label in [
    ("tracking-carriers", "capture-plus@return-form", "label", "Tracking carriers (204 options)"),
    ("return-reasons", "capture-plus@the-complete-snowboard", "label", "Return reasons (10 options)"),
    ("inventory-adjustment-reasons", "capture-plus@adjust-available", "label", "Inventory adjustment reasons (7 options)"),
    ("storefront-languages", "capture-plus@add-language", "label", "Add language (136 languages)"),
]:
    d = S + sid + "/" + inst; sd = meta_date(d)
    for i, raw, it in lines(d + "/items.jsonl"):
        if it.get(key) and it.get(key) != "Select...":
            add("other:value-lists", label, sid, "value list", d + "/items.jsonl", i, frag(raw, key, it[key]), sd,
                locator=f"from line {i} (one option per line; first option quoted)")
            break


# ---------------------------------------------------------------- Help Center section lists (selected parents)
d = S + "help-section-children/help.shopify.com@en-md"; sd = meta_date(d)
HELP_PARENTS = ['payments.md', 'payments/shopify-payments.md', 'payments/shopify-payments/onboarding.md',
    'payments/shopify-payments/payouts.md', 'payments/shopify-payments/store-currency.md',
    'payments/shopify-payments/supported-countries.md', 'international.md', 'international/pricing.md', 'markets.md',
    'markets/customizations.md', 'finance.md', 'privacy-and-security/privacy.md',
    'privacy-and-security/privacy/international-data-transfers.md', 'compliance/legal.md', 'taxes.md', 'taxes/shopify-tax.md',
    'taxes/shopify-tax/automated-filing.md', 'taxes/tax-apps.md', 'your-account/manage-billing.md',
    'your-account/manage-billing/billing-charges/types-of-charges/taxes.md', 'fulfillment.md', 'sell-in-person.md', 'apps.md',
    'checkout-settings.md']
HP = {'https://help.shopify.com/en/manual/' + x: x for x in HELP_PARENTS}
for i, raw, it in lines(d + "/items.jsonl"):
    if it["page"] in HP:
        add("other:help-center-sections", it["title"], "Help Center: In this section of " + HP[it["page"]], it.get("href", ""),
            d + "/items.jsonl", i, frag(raw, "title", it["title"]), sd)

# ---------------------------------------------------------------- tables of contents of the legal agreements (rendered live pages)
def toc(url, fname, stop_prefixes):
    path = os.path.join(FETCHED, fname)
    L = open(path, encoding="utf-8").read().split("\n")
    k = L.index("TABLE OF CONTENTS")
    out = []
    for j in range(k + 1, len(L)):
        t = L[j].strip()
        if not t:
            if out:
                break
            continue
        if any(t.startswith(sp) for sp in stop_prefixes) or len(t) > 90 or t in [x[1] for x in out]:
            break
        out.append((j + 1, t))
    return path, out

for url, fname, title, date, basis in [
    ("https://www.shopify.com/legal/terms", "www.shopify.com_legal_terms.rendered.txt", "Shopify Terms of Service", "2026-08-01", 'last updated (page states "Last updated on: August 1, 2026")'),
    ("https://www.shopify.com/legal/terms-shopify-payments", "www.shopify.com_legal_terms-shopify-payments.rendered.txt", "Shopify Payments Terms of Service", "2026-10-10", "undated live page; read 2026-10-10"),
    ("https://www.shopify.com/legal/terms-payfac", "www.shopify.com_legal_terms-payfac.rendered.txt", "Shopify Payments Facilitator Terms", "2026-09-22", 'last modified (page states "Last modified: September 22, 2026")'),
    ("https://www.shopify.com/legal/processor-list", "www.shopify.com_legal_processor-list.rendered.txt", "Payment Processors for Shopify Payments", "2026-10-10", "undated live page; read 2026-10-10"),
    ("https://www.shopify.com/legal/dpa", "www.shopify.com_legal_dpa.rendered.txt", "Shopify Data Processing Addendum", "2026-07-07", 'last updated (page states "Last updated on: July 7, 2026")'),
    ("https://www.shopify.com/legal/privacy", "www.shopify.com_legal_privacy.rendered.txt", "Shopify Privacy Policy", "2026-07-07", 'updated (page states "UPDATED JULY 7, 2026")'),
]:
    path, items = toc(url, fname, ["Last updated", "Last modified", "UPDATED", "The Terms", "The following", "Shopify Data Processing"])
    for ln, t in items:
        add("legal-agreements", t, title + ": table of contents", "", path, ln, t, date, basis=basis, access="rendered",
            source=url, locator=f"line {ln} (TABLE OF CONTENTS)")

# section 9 of the Terms of Service names the Additional Services one by one
path = os.path.join(FETCHED, "www.shopify.com_legal_terms.rendered.txt")
for j, t in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
    if re.match(r"^9\.\d+ \S", t):
        add("legal-agreements", t.strip(), "Shopify Terms of Service: 9. Additional Services", "", path, j, t.strip(), "2026-08-01",
            basis='last updated (page states "Last updated on: August 1, 2026")', access="rendered",
            source="https://www.shopify.com/legal/terms", locator=f"line {j} (section 9 subheading)")

# the access-scopes page names its permission request paths as headings
md = os.path.join(FETCHED, "shopify.dev_docs_api_usage_access-scopes.md")
for j, t in enumerate(open(md, encoding="utf-8").read().split("\n"), 1):
    if t.startswith("### ") and "permission" in t.lower() or t.startswith("### Shopify approval scopes"):
        h = t[4:].strip()
        add("access-scopes", h, "access-scopes page: Requesting specific permissions", "", md, j, t, "2026-10-10",
            basis="undated live page; read 2026-10-10", access="md",
            source="https://shopify.dev/docs/api/usage/access-scopes.md", locator=f"line {j} (heading)")

# ---------------------------------------------------------------- write
os.makedirs(os.path.join(OUT, "work"), exist_ok=True)
cols = ["list", "entry", "group", "extra", "source", "file", "locator", "quote", "source_date", "date_basis", "access_path"]
def clean(v):
    return str(v).replace("\t", " ").replace("\n", " ").replace("\r", " ")
with open(os.path.join(OUT, "work", "inventory_raw.tsv"), "w", encoding="utf-8") as fh:
    fh.write("\t".join(cols) + "\n")
    for r in ROWS:
        fh.write("\t".join(clean(r[c]) for c in cols) + "\n")
from collections import Counter
c = Counter(r["list"] for r in ROWS)
for k, v in sorted(c.items()):
    print(k, v)
print("total", len(ROWS))
