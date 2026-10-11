# Further observed-sh statements for cells the review and the first add scripts left empty, and for the new
# concerns SH-C-201 and SH-C-202. Every statement is a verbatim excerpt of the first cited file at the re-pass commit.
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import routerlib
A = Adder("osh")
W, D = routerlib.make(A)

# ---------- admin router ----------
D("SH-C-121", "shipping:eligibility", "parent route of local-delivery:list and pickup-in-store:list (the router's parent field)")
D("SH-C-162", "notification-settings", "parent route of notification-settings:webhooks (the router's parent field)")
W("SH-C-170", "subscribe:book-shopify-expert-intro-call", "under the plan subscription routes")
W("SH-C-170", "subscribe:bring-your-own-partner", "under the plan subscription routes")
W("SH-C-201", "settings:plan:shop_plus_self_renewals")
W("SH-C-201", "settings:plan:shop_plus_self_renewals:review")
W("SH-C-201", "settings:plan:plus:terms")
D("SH-C-201", "settings:plan:shop_plus_self_renewals")
W("SH-C-011", "settings:organizations:accounts:collaborator", "organization settings, accounts")

# ---------- admin permission tree ----------
PT = "structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/items.jsonl"
pt_lines = {}
for n, l in enumerate(git_show(PT).splitlines(), start=1):
    d = json.loads(l)
    pt_lines.setdefault(d["id"], (n, l, d))
PC = {json.loads(l)["id"]: json.loads(l)["title"] for l in git_show(PT.replace("items.jsonl", "categories.jsonl")).splitlines()}

def P(c, pid, note=""):
    n, l, d = pt_lines[pid]
    cid = osh_cite(PT, f"line {n} (id {pid})", l, sid="shopify/admin-permission-tree")
    A.add(c, "decides", "structures/shopify/admin-permission-tree", pid, l, "", cid,
          f"staff permission in the admin's permission tree, category {d['category']} ({PC.get(d['category'], '')})" + ("; " + note if note else ""))

for c, ps in [("SH-C-045", ["SET_PAYMENT_TERMS_FOR_ORDERS", "SET_PAYMENT_TERMS_FOR_DRAFT_ORDERS"]),
              ("SH-C-149", ["ERASE_CUSTOMER_DATA", "REQUEST_CUSTOMER_DATA"]),
              ("SH-C-023", ["VIEW_INVENTORY_PURCHASE_ORDERS", "CREATE_AND_EDIT_INVENTORY_PURCHASE_ORDERS"]),
              ("SH-C-022", ["VIEW_INVENTORY_COUNTS", "MANAGE_INVENTORY_COUNTS", "PERFORM_INVENTORY_COUNTS"]),
              ("SH-C-151", ["MANAGE_AUTOMATIONS", "MANAGE_AUTOMATION_SETTINGS"]),
              ("SH-C-009", ["MANAGE_STAFF_PERMISSIONS", "ADD_REMOVE_STAFF"]),
              ("SH-C-007", ["AUTHENTICATION_MANAGEMENT"]),
              ("SH-C-010", ["STAFF_API_PERMISSION_MANAGEMENT", "MANAGE_STAFF_PERMISSIONS"]),
              ("SH-C-011", ["MANAGE_COLLABORATORS"]),
              ("SH-C-088", ["VIEW_BALANCE_BANK_ACCOUNTS"]),
              ("SH-C-090", ["VIEW_ALL_SHOPIFY_CREDIT_TRANSACTIONS"]),
              ("SH-C-016", ["VIEW_BILLING_DETAILS", "BILLING_PAY_INVOICES"])]:
    for p in ps:
        P(c, p)

# ---------- PlanFeatureSetQuery answer (store ibx5bt-xy) ----------
PF = "raw/runs/20260930T045741Z-sweep-trial2/answers/admin.shopify.com/PlanFeatureSetQuery/c6039bbf4031394b363a50a844539c551b88b63ac6d382197e7eaeb92a376006.json"
for c, q, ident in [("SH-C-108", '"summary":"Show prices in local currencies*","type":"sell_globally_local_currencies","requiresShopifyPayments":true', "sell_globally_local_currencies"),
                    ("SH-C-080", '"summary":"Accept local payment methods*","type":"sell_globally_local_payments","requiresShopifyPayments":true', "sell_globally_local_payments")]:
    cid = osh_cite(PF, f"planFeatureSet feature type {ident}", q)
    A.add(c, "decides", "PlanFeatureSetQuery answer (admin.shopify.com)", ident, q, "store ibx5bt-xy", cid,
          "the admin's plan feature set; requiresShopifyPayments is the platform's own flag on the feature")

# ---------- sign-up page (journey) ----------
SJ = "raw/runs/20261006T232216Z-journey-signup-new-account"
q = 'combobox "I\'m located in:"'
c1 = osh_cite(f"{SJ}/steps/004.aria.yaml", "step 4, main", q)
q2 = '"url":"https://accounts.shopify.com/signup?rid=80f62031-b9ea-44db-a2bd-4695f6dfdd49","title":"Sign up — Shopify"'
c2 = osh_cite(f"{SJ}/actions.jsonl", "step 4", q2)
A.add("SH-C-006", "where", "journey signup-new-account (accounts.shopify.com/signup)", "I'm located in:", q, "", [c1, c2],
      "the sign-up page on accounts.shopify.com (actions.jsonl step 4 names the page)")

# ---------- admin operation areas (answers.jsonl endpoints) ----------
def endpoint(run, op, store=None, area=None):
    path = f"raw/runs/{run}/answers.jsonl"
    for n, l in enumerate(git_show(path).splitlines(), start=1):
        d = json.loads(l)
        if d["operation"] == op and (store is None or d["store"] == store) and (area is None or d["area"] == area):
            q = f'"endpoint": "{d["endpoint"]}"'
            assert q in l, (op, q)
            return path, n, q, d
    raise SystemExit(f"no {op} in {run}")

def AREA(c, run, op, store, area, placement="where", note=""):
    path, n, q, d = endpoint(run, op, store, area)
    cid = osh_cite(path, f"line {n} ({op})", q)
    A.add(c, placement, "admin.shopify.com operations (answers.jsonl)", f"{area}/{op}", q, f"store {store}" if store else "", cid,
          f"the admin's '{area}' operation area; {{hash}} stands for the persisted query hash in the recorded endpoint" + ("; " + note if note else ""))

AREA("SH-C-201", "20260930T002940Z-sweep-trial", "PlusContractDetails", "ctcbwa-r1", "contractmanagement")
AREA("SH-C-201", "20260930T002940Z-sweep-trial", "RenewalsQuery", "ctcbwa-r1", "contractmanagement")
AREA("SH-C-004", "20260930T003329Z-pilot-import", "ValidationSchemaByContextQuery", "ibx5bt-xy", "completeness_engine")
AREA("SH-C-004", "20260930T002940Z-sweep-trial", "LegalEntityTypesByCountryCode", "ctcbwa-r1", "organizations")
AREA("SH-C-008", "20260930T002940Z-sweep-trial", "RemediationQuery", "ctcbwa-r1", "profile_assessment")
AREA("SH-C-089", "20260930T002940Z-sweep-trial", "CardsIndexQuery", "ctcbwa-r1", "banking")
AREA("SH-C-090", "20260930T002940Z-sweep-trial", "CreditIndexBanking", "ctcbwa-r1", "banking")
AREA("SH-C-091", "20260930T002940Z-sweep-trial", "CapitalAccountOverviewQuery", "ctcbwa-r1", "capital")
AREA("SH-C-001", "20260930T002940Z-sweep-trial", "ShopsOnlyActiveDestinations", None, "destinations")

# ---------- answers that state values ----------
def ANS(c, placement, path, q, ident, scope, note, structure, extra=()):
    cid = osh_cite(path, ident, q)
    A.add(c, placement, structure, ident, q, scope, [cid] + list(extra), note)

PI = "raw/runs/20260930T003329Z-pilot-import"
VS = f"{PI}/answers/admin.shopify.com/ValidationSchemaByContextQuery/af5fd2e6c25b57c52a53f76f96890e83c867eda67736593863b4d855f6b44752.json"
vline = endpoint("20260930T003329Z-pilot-import", "ValidationSchemaByContextQuery", "ibx5bt-xy", "completeness_engine")
vq = '"variables": {"jurisdiction": "YE", "legalEntityType": "default_company"}'
vcid = osh_cite(vline[0], f"line {vline[1]} (ValidationSchemaByContextQuery variables)", vq)
for f in ["legalEntity.registeredBusinessName", "legalEntity.governmentIdentifiers"]:
    raw = git_show(VS)
    i = raw.index('{"field":"' + f + '"')
    q = routerlib.balanced(raw, i)
    ANS("SH-C-004", "decides", VS, q, f, "jurisdiction YE, legalEntityType default_company (store ibx5bt-xy)",
        "field requirement in the validation schema the admin's completeness_engine area returns; the variables are in the run's answers.jsonl",
        "ValidationSchemaByContextQuery answer (admin.shopify.com, completeness_engine)", [vcid])

LT = "raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/LegalEntityTypesByCountryCode/88c4f66dd8648347f352c6975976a099104ef72a2f596617b2da01c7c6ba08f1.json"
lq = '{"handle":"default_individual","name":"Individual","category":"individual"'
lt_line = endpoint("20260930T002940Z-sweep-trial", "LegalEntityTypesByCountryCode", "ctcbwa-r1", "organizations")
ltq = '"variables": {"countryCode": "YE"}'
ltc = osh_cite(lt_line[0], f"line {lt_line[1]} (LegalEntityTypesByCountryCode variables)", ltq)
for h, nm, cat in [("default_individual", "Individual", "individual"), ("default_company", "Company", "company"), ("default_non_profit", "Non-Profit", "non_profit")]:
    q = '{"handle":"%s","name":"%s","category":"%s"' % (h, nm, cat)
    ANS("SH-C-004", "decides", LT, q, h, "countryCode YE (store ctcbwa-r1)",
        "business entity types the admin offers for the country; the variables are in the run's answers.jsonl",
        "LegalEntityTypesByCountryCode answer (admin.shopify.com, organizations)", [ltc])

OL = "raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/OrganizationLegalEntities/1033e95626c25c43367e339160a0a99a12a0facad9be572e3630832689d14d2a.json"
ANS("SH-C-004", "responsible", OL, '"legalEntityType":null,"principalsCount":0,"countryCode":"YE","category":"UNSPECIFIED"', "LegalEntity",
    "the organization of store ctcbwa-r1", "the merchant's own business entity record as the admin returns it (names left out of the quote)",
    "OrganizationLegalEntities answer (admin.shopify.com, organizations)")

SI = "raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/ServerIntent/14e5d45d59e7503af9ab6057d3e52a56bdb445b60169b7a320f79eab64e45b47.json"
ANS("SH-C-020", "where", SI, '"entrypoint":"ServerIntents::FormContracts::ProductEditScalarFields"', "ServerIntents::FormContracts::ProductEditScalarFields",
    "store fake-demo-sharrwah", "code path named in the ServerIntent answer's form validation provider",
    "ServerIntent answer (admin.shopify.com)")
si_line = None
for n, l in enumerate(git_show("raw/runs/20260930T002940Z-sweep-trial/answers.jsonl").splitlines(), start=1):
    if "ServerIntent/14e5d45d59e7503af9ab6057d3e52a56bdb445b60169b7a320f79eab64e45b47.json" in l:
        si_line = (n, l)
        break
siq = '"variables": {"action": "edit", "type": "product"'
assert siq in si_line[1]
sic = osh_cite("raw/runs/20260930T002940Z-sweep-trial/answers.jsonl", f"line {si_line[0]} (ServerIntent variables)", siq)
A.add("SH-C-020", "boundary", "admin.shopify.com operations (answers.jsonl)", "ServerIntent action edit, type product", siq,
      "store fake-demo-sharrwah", sic, "the intent the admin requests from its ServerIntent operation, as recorded with the answer")

# ---------- plan pages (footnotes) ----------
PP = "structures/shopify/plan-page-public/www.shopify.com_pricing/items.jsonl"
PA = "structures/shopify/plan-page-admin/ibx5bt-xy/items.jsonl"
def FN(c, placement, path, q, ident, scope, note):
    cid = osh_cite(path, ident, q, sid="shopify/" + path.split("/")[2])
    ident = ("www.shopify.com/pricing" if "plan-page-public" in path else "admin plan page (settings/plan)") + f" ({ident})"
    A.add(c, placement, "structures/shopify/" + path.split("/")[2], ident, q, scope, cid, note)
pub = ""
adm = "store ibx5bt-xy"
FN("SH-C-088", "responsible", PP, "Shopify is a tech company, not a bank. We partner with Stripe Payments Company for money transmission services and account services with funds held at Fifth Third Bank N.A., Member FDIC.", "footnote", pub, "")
FN("SH-C-089", "responsible", PP, "Shopify Balance Visa® Commercial cards are powered by Stripe and issued by Celtic Bank pursuant to a license from Visa U.S.A. Inc.", "footnote", pub, "")
FN("SH-C-090", "responsible", PP, "Shopify Credit Visa® Commercial Credit cards are powered by Stripe and issued by Celtic Bank pursuant to a license from Visa U.S.A. Inc. See Issuing Bank Terms and Program Terms.", "footnote", pub, "")
FN("SH-C-091", "responsible", PP, "All funding through Shopify Capital in the U.S. is issued by WebBank.", "footnote", "U.S.", "")
FN("SH-C-091", "responsible", PA, "All funding through Shopify Capital in the United States is issued by WebBank.", "footnote", "United States; store ibx5bt-xy", "the admin plan page words it differently from the public page")
FN("SH-C-098", "responsible", PP, "Shopify Bill Pay is provided by Melio", "footnote", pub, "")
FN("SH-C-098", "responsible", PA, "Shopify Bill Pay is powered by Melio", "footnote", adm, "the admin plan page says 'powered by' where the public page says 'provided by'")
FN("SH-C-184", "decides", PP, "Yes. Shopify is certified Level 1 PCI DSS compliant, and stores powered by Shopify are PCI compliant by default, which helps keep payment information secure.", "FAQ answer", "", "")

# ---------- App Store built-in feature pages ----------
BF = "structures/shopify/app-store-built-in-features"
def bf_items(page):
    path = f"{BF}/apps.shopify.com_built-in-features_{page}/items.jsonl"
    return path, [(n, json.loads(l)) for n, l in enumerate(git_show(path).splitlines(), start=1)]

def BT(c, placement, page, startswith, note="", scope=""):
    path, items = bf_items(page)
    for n, d in items:
        if d["text"].startswith(startswith):
            q = d["text"]
            cid = osh_cite(path, f"line {n} ({d['tag']})", q, sid="shopify/app-store-built-in-features")
            A.add(c, placement, f"{BF} ({page})", f"apps.shopify.com/built-in-features/{page}", q,
                  scope, cid, note)
            return
    raise SystemExit(f"{page}: no text starting {startswith!r}")

def BL(c, page, note=""):
    path, items = bf_items(page)
    for n, d in items:
        for k in d["links"]:
            if k["href"].startswith("https://admin.shopify.com/"):
                q = k["href"]
                cid = osh_cite(path, f"line {n} (link '{k['text']}')", q, sid="shopify/app-store-built-in-features")
                A.add(c, "where", f"{BF} ({page})", f"apps.shopify.com/built-in-features/{page}", q, "", cid,
                      "the page's 'Get started' link into the admin" + ("; " + note if note else ""))
                return
    raise SystemExit(f"{page}: no admin link")

BL("SH-C-202", "magic-product-descriptions")
BL("SH-C-202", "magic-blog-posts")
BT("SH-C-202", "where", "magic-product-descriptions", "Use directly in your Shopify admin")
BT("SH-C-202", "decides", "magic-product-descriptions", "Your Shopify plan includes free AI-generated product descriptions")
BT("SH-C-202", "decides", "magic-blog-posts", "Your Shopify plan includes blogging tools, including Shopify Magic")
BL("SH-C-126", "order-tracking")
BT("SH-C-126", "decides", "order-tracking", "Your Shopify plan includes order tracking features")
BT("SH-C-148", "decides", "automated-privacy", "Your Shopify plan includes automated privacy features")
BT("SH-C-044", "decides", "b2b", "Included with Shopify Plus")
BT("SH-C-044", "decides", "b2b", "Your Shopify Plus plan gives you everything you need to run your wholesale business")
BT("SH-C-041", "decides", "customer-accounts", "Enable B2B buying by adding customer profiles to a company")
BT("SH-C-020", "decides", "product-variants", "Your Shopify plan comes with everything you need to create up to 100 variants",
   "differs from the maxProductVariants value (2048) in the stores' resourceLimits; both recorded")
BT("SH-C-026", "decides", "store-credit", "Before you can issue and accept store credit")
BT("SH-C-110", "responsible", "managed-markets", "Managed Markets acts as your Merchant of Record")
BT("SH-C-088", "responsible", "shopify-balance", "Shopify partners with Stripe Payments Company")
BT("SH-C-091", "responsible", "shopify-capital", "* Funding through Shopify Capital is available in select countries")
BT("SH-C-075", "responsible", "shop-pay-installments", "Rates from 0-36% APR.")
BT("SH-C-117", "decides", "shopify-shipping", "Labels from Shopify include address validation and up to $200 insurance")
BT("SH-C-100", "decides", "shopify-tax-eu", "Shopify Tax automatically calculates and collects VAT", "scope from the page: its admin link is settings/taxes/EU", "EU")
BT("SH-C-100", "decides", "shopify-tax-uk", "Shopify Tax automatically calculates and collects VAT", "scope from the page: its admin link is settings/taxes/GB", "UK")
BT("SH-C-104", "decides", "shopify-tax-us", "Automate the preparation, filing, and remittance of sales tax returns", "scope from the page: its admin link is settings/taxes/US", "US")
BT("SH-C-050", "decides", "abandoned-checkout-recovery", "Your Shopify plan includes abandoned cart recovery features")
BT("SH-C-055", "decides", "draft-orders", "Your Shopify plan comes with everything you need to create draft orders")
# ---------- boundary: API reference groups and extension targets ----------
NAV = "structures/shopify/admin-graphql-reference-nav/shopify.dev@latest/items.jsonl"
for key, kind in [("catalogs", "queries"), ("catalogCreate", "mutations")]:
    q = '{"key": "%s", "label": "%s", "href": "/docs/api/admin-graphql/latest/%s/%s"' % (key, key, kind, key)
    cid = osh_cite(NAV, f"line 20 (group products-and-collections, {kind} {key})", q, sid="shopify/admin-graphql-reference-nav")
    A.add("SH-C-037", "boundary", "structures/shopify/admin-graphql-reference-nav", key, q, "GraphQL Admin API (latest)", cid,
          "listed in the API reference's 'Products and collections' group")
UX = "structures/shopify/ui-extension-targets/checkout@2026.7.1/items.jsonl"
for n, l in enumerate(git_show(UX).splitlines(), start=1):
    d = json.loads(l)
    if d["target"] in ("purchase.checkout.block.render", "purchase.thank-you.block.render"):
        q = '"interface": "%s", "target": "%s"' % (d["interface"], d["target"])
        cid = osh_cite(UX, f"line {n}", q, sid="shopify/ui-extension-targets")
        A.add("SH-C-049", "boundary", "structures/shopify/ui-extension-targets (checkout@2026.7.1)", d["target"], q, "checkout UI extensions 2026.7.1", cid,
              "extension target in the checkout UI extensions type definitions")
# ---------- boundary: intents the admin requests from its server_intents area (run 20261006T225457Z, store ts15uk-ug) ----------
SIR = "raw/runs/20261006T225457Z-sweep-trial-my-store-8/answers.jsonl"
intent_concern = {("create", "catalog"): "SH-C-037", ("create", "collection"): "SH-C-021", ("create", "company"): "SH-C-044",
                  ("create", "article"): "SH-C-030", ("create", "page"): "SH-C-030", ("create", "customer"): "SH-C-039",
                  ("create", "discount"): "SH-C-127", ("create", "purchase_order"): "SH-C-023", ("create", "inventory_transfer"): "SH-C-023",
                  ("create", "location"): "SH-C-024", ("create", "market"): "SH-C-106", ("create", "metaobject_definition"): "SH-C-028",
                  ("create", "draft_order"): "SH-C-055", ("create", "role"): "SH-C-010", ("create", "user"): "SH-C-009",
                  ("create", "product"): "SH-C-020", ("open", "rollout"): "SH-C-112", ("create", "delivery_profile"): "SH-C-114"}
done = set()
for n, l in enumerate(git_show(SIR).splitlines(), start=1):
    d = json.loads(l)
    if d.get("area") != "server_intents" or d["operation"] != "ServerIntent":
        continue
    v = (d["calls"][0].get("variables") or {})
    key = (v.get("action"), v.get("type"))
    c = intent_concern.get(key)
    if not c or key in done:
        continue
    done.add(key)
    q = '"variables": {"action": "%s", "type": "%s"' % key
    assert q in l, q
    cid = osh_cite(SIR, f"line {n} (ServerIntent {key[0]} {key[1]})", q)
    A.add(c, "boundary", "admin.shopify.com operations (answers.jsonl), server_intents area", f"ServerIntent {key[0]} {key[1]}", q,
          "store ts15uk-ug", cid, "the intent (action, type) the admin sends to its server_intents operation area, as recorded with the answer")
A.save()
