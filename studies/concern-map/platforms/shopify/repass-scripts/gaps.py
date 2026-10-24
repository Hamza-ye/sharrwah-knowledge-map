# One gap row for every concern x placement with no statement (questions/Q1-concern-map.md, rule 4), with its kind:
#   page not read | observation needed | searched, not found | stated only in general terms
# Writes work/gaps.tsv.
import sys, os, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

con = rd(os.path.join(FIRST, "concerns.tsv")) + rd(os.path.join(WORK, "new-concerns.tsv"))
cites = {}
for path in (os.path.join(FIRST, "citations.tsv"), os.path.join(BASE, "citations-new.tsv"), os.path.join(WORK, "cites-added.tsv")):
    for r in rd(path):
        cites[r["cite_id"]] = r
stmts = rd(os.path.join(WORK, "reviewed-statements.tsv"))
for f in sorted(glob.glob(os.path.join(WORK, "added", "*.tsv"))):
    stmts += rd(f)
have = collections.defaultdict(list)
pages = collections.defaultdict(list)
for s in stmts:
    have[(s["concern_id"], s["placement"])].append(s)
    for c in ids(s["cite_ids"]):
        src = cites[c]["source"].split("#")[0]
        if src.startswith("http") and src not in pages[s["concern_id"]]:
            pages[s["concern_id"]].append(src)

router = {}
for l in git_show("structures/shopify/admin-router/items.jsonl").splitlines():
    d = json.loads(l)
    router[d["id"]] = d

def n(c):
    return int(c[5:])
LEGAL = {2, 14, 17, 66, 67, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184}
FIN = set(range(63, 76)) | {77, 78, 80, 81, 82, 85, 86} | set(range(88, 100))
DEV = {157, 158, 159, 160, 161, 162, 167, 168, 169, 170, 171}
PLANS = "stores on each plan (Basic, Grow, Advanced, Plus), paid, and the development editions already held"
TOS = "https://www.shopify.com/legal/terms"
SPT = "https://www.shopify.com/legal/terms-shopify-payments"
LEGAL_INDEX = "https://www.shopify.com/legal (the legal index, held as structures/shopify/shopify-legal-index)"
GAP_COLS = ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"]
OBS = {"record a journey", "open a store on a plan", "save a page from a browser", "ask the platform"}
HM = "https://help.shopify.com/en/manual/"

# Pages read on 11 October 2026 for the gap review (working copies in fetched/pages, logged in fetched/log.tsv).
READ = {
 "SH-C-001": "your-account/manage-orgs-and-stores/change-transfer-ownership", "SH-C-003": "organization-settings", "SH-C-010": "your-account/users/roles",
 "SH-C-011": "your-account/users/security/collaborator-accounts", "SH-C-012": "shopify-admin/activity-logs", "SH-C-013": "your-account/manage-orgs-and-stores/manage-store-details",
 "SH-C-015": "intro-to-shopify/pricing-plans", "SH-C-020": "products/add-update-products", "SH-C-021": "products/collections", "SH-C-022": "products/inventory",
 "SH-C-023": "products/inventory/inventory-transfers", "SH-C-024": "fulfillment/setup/locations", "SH-C-025": "products/gift-card-products", "SH-C-026": "customers/store-credit",
 "SH-C-027": "shopify-admin/productivity-tools/file-uploads", "SH-C-028": "custom-data/overview", "SH-C-029": "online-store/themes", "SH-C-030": "online-store/blogs",
 "SH-C-031": "online-store/menus-and-links", "SH-C-032": "international/localization-and-translation", "SH-C-033": "domains", "SH-C-034": "checkout-settings/refund-privacy-tos",
 "SH-C-035": "online-store/storefront-search", "SH-C-037": "b2b/catalogs", "SH-C-038": "products/combined-listings-app", "SH-C-039": "customers/manage-customers",
 "SH-C-040": "customers/customer-segmentation", "SH-C-046": "checkout-settings/add-to-cart-limit", "SH-C-047": "checkout-settings", "SH-C-048": "checkout-settings/customize-checkout-configurations",
 "SH-C-050": "promoting-marketing/create-marketing/abandoned-checkouts", "SH-C-054": "fulfillment/managing-orders", "SH-C-055": "fulfillment/managing-orders/create-orders",
 "SH-C-056": "fulfillment/managing-orders/editing-orders", "SH-C-057": "fulfillment/managing-orders/refunding-orders", "SH-C-058": "fulfillment/managing-orders/returns",
 "SH-C-061": "fulfillment/managing-orders/printing-orders", "SH-C-087": "sell-in-person/hardware/cash-drawer", "SH-C-114": "fulfillment/setup/shipping-profiles",
 "SH-C-115": "fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping", "SH-C-118": "fulfillment/fulfilling-orders", "SH-C-121": "fulfillment/setup/delivery-methods",
 "SH-C-126": "fulfillment/setup/order-status-page/order-tracking", "SH-C-127": "discounts/discount-types", "SH-C-129": "promoting-marketing",
 "SH-C-130": "promoting-marketing/create-marketing/shopify-messaging", "SH-C-143": "sell-in-person/hardware", "SH-C-145": "reports-and-analytics",
 "SH-C-150": "fulfillment/setup/notifications", "SH-C-153": "inbox/setup", "SH-C-154": "online-sales-channels/shop/product-reviews", "SH-C-167": "apps/app-types/custom-apps",
 "SH-C-176": "compliance/intellectual-property", "SH-C-202": "ai-powered-tools/shopify-magic", "SH-C-141": "online-sales-channels/shopify-collective/suppliers/payments",
}
READ = {c: "https://help.shopify.com/en/manual/" + p for c, p in READ.items()}
READ.update({"SH-C-168": "https://help.shopify.com/en/partners/partner-program/about", "SH-C-144": "https://shopify.dev/docs/api/pos-ui-extensions",
             "SH-C-164": "https://shopify.dev/docs/api/admin-extensions", "SH-C-139": "https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/oxygen-runtime",
             "SH-C-133": "https://www.shopify.com/legal/shop-campaigns-merchant-terms", "SH-C-134": "https://collabs.shopify.com/terms",
             "SH-C-082": "https://www.shopify.com/legal/shop-cash-merchant-terms (served the Shop Campaigns Merchant Terms)",
             "SH-C-184": "https://www.shopify.com/legal/compliance/reports"})
NOT_FOUND_404 = {"SH-C-036": HM + "domains/ssl-certificates", "SH-C-043": HM + "customers/manage-customers/customer-marketing-consent",
                 "SH-C-131": HM + "promoting-marketing/analyze-marketing/marketing-attribution"}

def read_list(c, limit=4):
    out = []
    for u in pages.get(c, []):
        u2 = u[:-3] if u.endswith(".md") else u
        if u2 not in out:
            out.append(u2)
    if c in READ and READ[c] not in out:
        out.append(READ[c] + " (read 2026-10-11)")
    return out[:limit] + ([f"and {len(out) - limit} more"] if len(out) > limit else [])

def read_text(c):
    rl = read_list(c)
    return "; ".join(rl)

def admin_routes(c):
    out = []
    for p in ("where", "decides"):
        for s in have.get((c, p), []):
            if s["structure"] == "structures/shopify/admin-router" and s["identifier"] in router:
                out.append(s["identifier"])
    return list(dict.fromkeys(out))

GENERAL_TOS = (f"The Terms of Service ({TOS}) speak of the Services in general: '13. Shopify Contracting Party and Forum' names the contracting party "
               "for the Services as a whole, and '4. Your Responsibilities' states the merchant's responsibilities for them; no clause names this concern")
GENERAL_SPT = (f"The Shopify Payments Terms of Service ({SPT}) speak of the Payments Services in general ('Part I, A. The Payment Processor'); "
               "no clause names this concern")
GENERAL_POS = (f"The Terms of Service ({TOS}) speak of the POS Services in general in '9.3 POS Services'; no clause names this concern")

OVERRIDE = {
    ("SH-C-201", "responsible"): ("The Shopify Plus agreement: the parties and the clauses on renewal and term", "open a store on a plan", "founder",
        "a paid Shopify Plus store: admin Settings > Plan, the 'Shopify Plus Terms' route (settings:plan:plus:terms, path plus/terms)",
        "The Plus terms page is shown inside the admin; no public copy was found, and the Plus contract answers held are empty (PlusContractDetails: currentContractTerms null; RenewalsQuery: renewals []).",
        "observation needed"),
    ("SH-C-201", "boundary"): ("The contract or setting through which a Plus store's term and renewals are agreed (the Plus terms, the 3-year renewal flow)", "open a store on a plan", "founder",
        "a paid Shopify Plus store: admin routes settings:plan:shop_plus_self_renewals (Switch to 3-year term) and settings:plan:shop_plus_self_renewals:review",
        "The renewal routes require an organization flag (7351e1b4) and BILLING_SUBSCRIPTIONS; no observed store reached them, and the stores observed are trial, development and Plus development stores.",
        "observation needed"),
    ("SH-C-201", "reason"): ("A Shopify statement of why Plus is sold under its own contract and term (for example the 3-year term)", "ask the platform", "founder",
        "Shopify Plus sales, or the Plus terms page in a paid Plus store's admin", "No page held or read states a reason; the Plus terms are shown only in the admin.",
        "observation needed"),
    ("SH-C-202", "responsible"): ("A Shopify term that states who is responsible for text Shopify Magic generates (product descriptions, blog posts)", "read a page", "agent",
        LEGAL_INDEX + "; " + HM + "ai-powered-tools/shopify-magic",
        f"Read the Terms of Service ({TOS}), which do not name Shopify Magic or AI features, the built-in feature pages for Shopify Magic, and "
        f"{HM}ai-powered-tools/shopify-magic (read 2026-10-11), which cautions that 'AI outputs can contain errors, so review anything a tool creates or changes' but names no responsible party.",
        "searched, not found"),
    ("SH-C-202", "boundary"): ("The API, intent or extension through which Shopify Magic generates text in the product and blog editors", "record a journey", "either",
        "admin products/new and articles/new on any held store (store owner role), recording the operations the editor calls when 'Generate' is used",
        "No observed journey used the generate action; the operations index held names no Magic operation.", "observation needed"),
    ("SH-C-202", "reason"): ("A Shopify statement of why Shopify Magic is built into the admin rather than offered through apps", "read a page", "agent",
        "https://apps.shopify.com/built-in-features/magic-product-descriptions; " + HM + "ai-powered-tools/shopify-magic",
        "Read the two built-in feature pages and " + HM + "ai-powered-tools/shopify-magic (read 2026-10-11); they state what is included ('no apps required') but give no reason.",
        "searched, not found"),
    ("SH-C-089", "boundary"): ("The card program terms and the interface between Shopify, Stripe and the issuing bank for Balance cards", "ask the platform", "founder",
        "admin Banking > Shopify Balance terms (route shopify-balance:terms:detail, path terms/:kind) on a US store that has onboarded to Balance",
        "Shopify Balance is offered to US merchants; every observed store is registered in YE and none has onboarded (features hasInitiatedOnboardingToBanking false), so the admin terms routes were not reached; no public Balance card terms page was found.",
        "observation needed"),
    ("SH-C-093", "responsible"): ("The lender or provider and the agreement for Shopify Capital in Canada", "ask the platform", "founder",
        "Shopify Capital terms shown in the admin (route capital:account:terms, 'Capital Application') on an eligible store registered in Canada, or Shopify Support",
        "Read " + HM + "finance/shopify-capital/canada (captured): it names no lender or provider. The admin terms need a store registered in Canada; the observed stores are registered in YE.",
        "observation needed"),
    ("SH-C-094", "responsible"): ("The lender or provider and the agreement for Shopify Capital in Australia", "ask the platform", "founder",
        "Shopify Capital terms shown in the admin (route capital:account:terms) on an eligible store registered in Australia, or Shopify Support",
        "Read " + HM + "finance/shopify-capital/australia (captured): it names no lender or provider. The admin terms need a store registered in Australia; the observed stores are registered in YE.",
        "observation needed"),
    ("SH-C-174", "where"): ("Where the platform applies the restriction: sign-up, storefront access, Shopify Payments onboarding, checkout", "record a journey", "either",
        "sign-up at accounts.shopify.com/signup (the 'I'm located in:' list) and storefront and admin access from an unsupported region",
        "The captured help page on unsupported countries and regions states the restrictions but not where the platform enforces them; an absence from a held country list is not evidence.",
        "observation needed"),
    ("SH-C-174", "boundary"): ("The screening interface or contract term through which sanctions checks meet the rest of the platform", "ask the platform", "founder",
        "Shopify Support, or the Shopify Payments onboarding flow on a store in a supported country",
        "The captured help page, the Terms of Service and the Shopify Payments terms state the restrictions but name no screening API, event or setting.",
        "observation needed"),
    ("SH-C-035", "decides"): ("The settings or plan lines that turn storefront search and filters on or limit them (the Search & Discovery app's settings)", "record a journey", "either",
        "the Search & Discovery app by Shopify (apps.shopify.com/search-and-discovery) installed on a held store, its settings pages (store owner role)",
        "No route eligibility, store key or plan line held names search or filters, and " + HM + "online-store/storefront-search (read 2026-10-11) states no condition; the app's own settings were not recorded.",
        "observation needed"),
    ("SH-C-087", "decides"): ("The POS setting or staff permission that turns cash tracking on (cash drawer counts and adjustments)", "record a journey", "either",
        "Shopify POS app > Settings on a held store with a POS location (staff role with POS access)",
        "The POS settings recorded on store fake-demo-sharrwah show the Cash payment type switch but no cash tracking setting; " + HM + "sell-in-person/hardware/cash-drawer (read 2026-10-11) states none.",
        "observation needed"),
    ("SH-C-170", "decides"): ("What the plan subscription pages state about booking a Shopify expert or bringing your own partner (who offers it, on which plans)", "record a journey", "either",
        "admin routes subscribe:book-shopify-expert-intro-call and subscribe:bring-your-own-partner (plan subscription pages) on a trial store, store owner role",
        "The router states no eligibility for these routes (eligibility null), and no page held or read describes them.", "observation needed"),
    ("SH-C-154", "decides"): ("What a product review app's placement depends on (app installation and the theme app blocks it adds)", "read a page", "agent",
        "https://apps.shopify.com (the product reviews category) and the listings of review apps",
        "Read " + HM + "online-sales-channels/shop/product-reviews (read 2026-10-11) and the held App Store taxonomy; the page states the Shop review process and the taxonomy names the category, but neither states a condition for review apps.",
        "searched, not found"),
    ("SH-C-038", "where"): ("Where Shopify places combined listings (the Shopify Combined Listings app and the admin pages it adds)", "record a journey", "either",
        "store capture-plus (Shopify Plus App Development, development store), or a paid Shopify Plus store: install the Shopify Combined Listings app and record its pages (store owner role)",
        "The plan table row 'Merchandise with Shopify Combined Listings' and " + HM + "products/combined-listings-app (read 2026-10-11) describe the app's steps but name no admin route, and no route held names it.",
        "observation needed"),
    ("SH-C-036", "where"): ("Where the platform shows hosting and the SSL certificate of the store's domains", "record a journey", "either",
        "admin Settings > Domains on a held store with a connected domain (store owner role)",
        "The only sources held are the plan table rows 'Unlimited web hosting' and 'Free SSL certificate'; no route or captured page names where SSL is shown, and the guessed Help Center path " + NOT_FOUND_404["SH-C-036"] + " returned 404.",
        "observation needed"),
    ("SH-C-087", "where"): ("Where cash tracking lives: the POS app screens and the admin pages for cash drawer sessions", "record a journey", "either",
        "the Shopify POS app on a held store with a POS location (staff role with POS access), and the admin's POS pages",
        "The scope group 'Cash Tracking' (read_cash_tracking, write_cash_tracking) is held, but no route, app screen or page held or read names where cash tracking is shown.",
        "observation needed"),
    ("SH-C-120", "boundary"): ("The agreement or interface at the boundary of the Shopify Fulfillment Network and Shopify Logistics (the Shopify Fulfillment Network Terms of Service)", "read a page", "agent",
        "https://www.shopify.com/legal (the legal index lists 'Shopify Fulfillment Network Terms of Service' with the link /legal/terms#9-additional-services); " + TOS,
        "The legal index's link for the Shopify Fulfillment Network Terms of Service points to section 9 (Additional Services) of the Terms of Service; section 9 as captured has no Fulfillment Network clause (9.1 to 9.14), and the captured Help Center page on the network names no agreement or interface.",
        "searched, not found"),
    ("SH-C-005", "responsible"): ("A clause that names who is responsible when a store sells with more than one business entity", "read a page", "agent",
        HM + "payments/shopify-payments/onboarding/selling-with-multiple-entities; " + SPT,
        "Read the captured Help Center page on selling with multiple entities and the Shopify Payments terms; neither names who is responsible for each entity's sales.",
        "searched, not found"),
}

def gap(c, p, name, terms):
    k = n(c)
    key = (c, p)
    if key in OVERRIDE:
        w, m, who, route, why, kind = OVERRIDE[key]
        return dict(zip(GAP_COLS, [c, p, w, m, who, route, why, kind]))
    routes = admin_routes(c)
    rt = ", ".join(routes[:6])
    rl = read_text(c)
    nf = NOT_FOUND_404.get(c)
    if p == "where":
        if k in LEGAL:
            return dict(zip(GAP_COLS, [c, p, f"The page, form, setting or service in which Shopify places '{name}'", "read a page", "agent",
                LEGAL_INDEX + (f"; {rl}" if rl else ""), f"Read {rl or 'the captured legal pages'}; they state the rules but name no place in the platform where it lives.",
                "searched, not found"]))
        return dict(zip(GAP_COLS, [c, p, f"The admin section and route, settings page, separate host or app where Shopify places '{name}' ({terms})", "record a journey", "either",
            "Shopify admin (store owner role) on a store where it is offered", f"No route, settings entry, host or app held in observed-sh at {C9}, and no page read, names it.",
            "observation needed"]))
    if p == "decides":
        if k in LEGAL:
            return dict(zip(GAP_COLS, [c, p, f"The term, rule or setting that sets '{name}' and the condition it depends on", "read a page", "agent",
                LEGAL_INDEX + (f"; {rl}" if rl else ""), f"Read {rl or 'the captured legal pages'}; they state the concern but not what sets or limits it.",
                "searched, not found"]))
        return dict(zip(GAP_COLS, [c, p, f"The eligibility, entitlement, plan line, setting or staff permission that turns '{name}' on, limits it or sets its value", "open a store on a plan", "founder",
            (f"admin routes {rt} on " if rt else "the admin pages for it on ") + PLANS, "No eligibility, plan line, store key or staff permission held names it.",
            "observation needed"]))
    if p == "responsible":
        if k in FIN and k < 88:
            return dict(zip(GAP_COLS, [c, p, f"A clause of the Shopify Payments terms (or the Payment Processor's terms for the merchant's country) that names '{name}' and who is responsible for it", "read a page", "agent",
                SPT + (f"; {rl}" if rl else ""), GENERAL_SPT + (f"; the pages read for it ({rl}) name no party either." if rl else "."), "stated only in general terms"]))
        if k in FIN:
            return dict(zip(GAP_COLS, [c, p, f"The terms of '{name}' that name the providing entity, partner or lender and the merchant's obligations", "save a page from a browser", "founder",
                (rl + "; " if rl else "") + "the product's terms as the admin shows them when onboarding, on a store in a country where it is offered",
                "The terms are not public among the pages read; Shopify shows some product terms only inside the admin, and the observed stores are registered in YE.", "observation needed"]))
        if k in DEV or k in LEGAL:
            src = "https://www.shopify.com/legal/api-terms; https://www.shopify.com/partners/terms" if k in DEV else LEGAL_INDEX
            return dict(zip(GAP_COLS, [c, p, f"A clause that names the party responsible for '{name}'", "read a page", "agent", src + (f"; {rl}" if rl else ""),
                f"Read {rl or 'the captured terms'}" + ("; the captured API License and Terms of Use and Partner Program Agreement" if k in DEV else "") + "; none names a party responsible for this concern.",
                "searched, not found"]))
        general = GENERAL_POS if k in (87, 142, 143) else GENERAL_TOS
        return dict(zip(GAP_COLS, [c, p, f"A Shopify term, policy or legal-entity record that names '{name}' and the party responsible for it", "read a page", "agent",
            LEGAL_INDEX + (f"; {rl}" if rl else ""), general + (f"; the pages read for it ({rl}) name no party either." if rl else "."), "stated only in general terms"]))
    if p == "boundary":
        if k in LEGAL or k in FIN:
            return dict(zip(GAP_COLS, [c, p, f"The agreement, API, event or setting at the boundary of '{name}' (the contract the merchant accepts, or the interface between Shopify and the partner)", "read a page", "agent",
                LEGAL_INDEX + (f"; {rl}" if rl else "") + "; shopify.dev API reference",
                f"Read {rl or 'the captured pages'}, and searched the held API reference navigation and Admin API schema; none names an API, event, setting or contract for this concern.",
                "searched, not found"]))
        return dict(zip(GAP_COLS, [c, p, f"The API resource, webhook topic, access scope, extension target, intent or event at the boundary of '{name}' ({terms})", "read a page", "agent",
            "shopify.dev API reference (held as structures/shopify/admin-graphql-reference-nav and admin-graphql-schema), webhook topics (structures/shopify/admin-webhook-topics, cli-webhook-topics), https://shopify.dev/docs/api/usage/access-scopes",
            f"Searched the held API reference navigation, the Admin API 2026-10 schema, the webhook topics, the access lines and the Dev Dashboard scopes for '{terms}'; none names an API, event, scope, target or intent for it"
            + (f"; the pages read for it ({rl}) name none either." if rl else "."), "searched, not found"]))
    if p == "reason":
        if rl:
            why = f"Searched {rl} and the observed-sh structures held for it for a stated reason; none states one."
        else:
            why = ("No Help Center page for it is in the held section lists (structures/shopify/help-section-children)"
                   + (f", and the guessed path {nf} returned 404" if nf else "") + "; the captured pages and the observed-sh structures held for it state no reason.")
        return dict(zip(GAP_COLS, [c, p, f"A sentence in which Shopify states why '{name}' is placed as it is (built in, behind a plan or setting, run by a separate entity or partner, or left to apps)", "read a page", "agent",
            (rl + "; " if rl else "") + "the Help Center and shopify.dev pages on it; Shopify Engineering writing (evidence/shopify-engineering/runs)", why, "searched, not found"]))
    raise SystemExit(p)

rows = []
for r in con:
    c = r["concern_id"]
    for p in ("where", "decides", "responsible", "boundary", "reason"):
        if not have.get((c, p)):
            g = gap(c, p, r["concern"], r["platform_terms"][:120])
            if g["means"] in OBS:
                assert g["gap_kind"] == "observation needed", (c, p)
            rows.append(g)
wr(os.path.join(WORK, "gaps.tsv"), GAP_COLS, rows)
print("gaps:", len(rows), dict(collections.Counter(x["placement"] for x in rows)))
print("by kind:", dict(collections.Counter(x["gap_kind"] for x in rows)))
print("by who:", dict(collections.Counter(x["who_can"] for x in rows)))
