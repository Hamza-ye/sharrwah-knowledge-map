# Re-pass spec, part G: a gap for every cell that still has no statement.
# Run after the statement parts (spec_a..spec_d); it reads work/kept.tsv and the statements registered so far.
import csv, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newcite
from newcite import G, S, Old

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIRST = "/home/user/sharrwah-knowledge-map/studies/concern-map/platforms/woocommerce"
csv.field_size_limit(10**9)
def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

# one more statement before the gaps are computed
S("WC-C-056", "decides", Old("WC-S-0852"), "11. Third-Party Services",
  note="Section 11 defines Third-Party Services to include extensions provided by a third party.")

CON = {r["concern_id"]: r["concern"] for r in rd(os.path.join(FIRST, "concerns.tsv"))}
P = ["where", "decides", "responsible", "boundary", "reason"]
have = collections.Counter()
sources = collections.defaultdict(list)
def short(src):
    s = src.replace("woocommerce-11.2.1:", "release ").replace("https://", "")
    return s
for r in rd(os.path.join(W, "work", "kept.tsv")):
    have[(r["concern_id"], r["placement"])] += 1
    if short(r["structure"]) not in sources[r["concern_id"]]:
        sources[r["concern_id"]].append(short(r["structure"]))
for s in newcite.STATEMENTS:
    have[(s["concern_id"], s["placement"])] += 1
    if short(s["cite"]["source"]) not in sources[s["concern_id"]]:
        sources[s["concern_id"]].append(short(s["cite"]["source"]))

def read_list(c, n=5):
    src = [x for x in sources[c] if not x.startswith("developer.woocommerce.com/llms.txt")]
    return "; ".join(src[:n]) if src else "the concern's inventory entries"

TOS_ROUTE = "wordpress.com/tos/ (section 1 'Who's Who', 8.j 'Ecommerce Services: Your responsibilities', 11 'Third-Party Services'); woocommerce.com/contact-us/ to ask"
CAA = "Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507)"

LEGAL = {"WC-C-020", "WC-C-022", "WC-C-023", "WC-C-024", "WC-C-025", "WC-C-026", "WC-C-027", "WC-C-028", "WC-C-029", "WC-C-043", "WC-C-044"}
CATEGORY = {f"WC-C-{n:03d}" for n in range(100, 113)}
CATEGORY_PAGE = {
    "WC-C-100": "woocommerce.com/product-category/woocommerce-extensions/merchandising/ (Subscriptions)",
    "WC-C-101": "woocommerce.com/product-category/woocommerce-extensions/merchandising/ (Bookings and appointments)",
    "WC-C-102": "woocommerce.com/product-category/woocommerce-extensions/merchandising/ (Memberships)",
    "WC-C-103": "woocommerce.com/product-category/woocommerce-extensions/merchandising/ (B2B)",
    "WC-C-104": "woocommerce.com/product-category/woocommerce-extensions/merchandising/",
    "WC-C-105": "woocommerce.com/product-category/woocommerce-extensions/conversion/",
    "WC-C-106": "woocommerce.com/product-category/woocommerce-extensions/customer-service-2/",
    "WC-C-107": "woocommerce.com/product-category/woocommerce-extensions/store-content-and-customizations/",
    "WC-C-108": "woocommerce.com/product-category/woocommerce-extensions/store-content-and-customizations/ (International and localization)",
    "WC-C-109": "woocommerce.com/product-category/woocommerce-extensions/operations/",
    "WC-C-110": "woocommerce.com/product-category/woocommerce-extensions/marketing-extensions/",
    "WC-C-111": "woocommerce.com/product-category/themes/ and the release's wc-admin themes routes",
    "WC-C-112": "woocommerce.com/product-category/business-services/",
}

# Marketplace categories whose product listing (wccom-extensions search API, read 11 October 2026) has no product in Developed by Woo
NO_WOO = {
    "WC-C-102": ("memberships", 11, "SkyVerge, itthinx, TIV.NET INC., Addify, Kestrel, Nexolis, Flintop, W7S",
                 "woocommerce.com/document/woocommerce-memberships-hook-reference/ (WooCommerce Memberships, vendor SkyVerge)"),
    "WC-C-108": ("international-and-localization", 18,
                 "TIV.NET INC., WPExperts, Weglot, Addify, YayCommerce, Syde, KoalaApps, ExpandNow Ltd., Teamwant, Nexa Plugins, Tyche Softwares, FmeAddons, Jeroen Sormani, Zorem, EU AI Label",
                 "woocommerce.com/document/weglot-translate-woocommerce/ (Weglot Translate, vendor Weglot)"),
}

def gap_general_responsible(c):
    G(c, "responsible",
      f"A term, policy or document of WooCommerce or Automattic that names {CON[c]} and says who is legally responsible for it.",
      "ask the platform", "founder", TOS_ROUTE,
      f"The Terms name WooCommerce among the Woo services (section 1) and make the user 'solely responsible for all of your ecommerce activities' (8.j), "
      f"and section 11 speaks of Third-Party Services in general; no term, policy or document read names this concern. Read for it: {read_list(c)}.",
      "stated only in general terms")

SPECIAL = {
    ("WC-C-008", "responsible"): ("page not read", "founder", "read a page", CAA,
        f"The WooPayments docs say Stripe 'applies and manages reserves' (WC-S-0855), but no Woo or Automattic term read assigns legal responsibility for them. "
        "The Connected Account Agreement is Stripe's own document; the brief limits sources to the platform's own material, so whether it may be read as part of WooPayments' terms is for the founder."),
    ("WC-C-009", "responsible"): ("page not read", "founder", "read a page", CAA,
        "The docs say the merchant verifies information 'with Stripe' (WC-S-0504) and that WooPayments must gather it (WC-S-0516), but no Woo or Automattic term read says who is legally responsible for the checks. "
        "The Connected Account Agreement is Stripe's own document; whether it may be read as part of WooPayments' terms is for the founder."),
    ("WC-C-010", "responsible"): ("page not read", "founder", "read a page", CAA,
        "The countries doc says account types differ because 'our partner (Stripe) strictly adheres to the laws and regulations of the country each account is based in' (WC-S-0513); no Woo or Automattic term read assigns responsibility for country eligibility. "
        "Whether Stripe's agreement may be read as part of WooPayments' terms is for the founder."),
    ("WC-C-051", "responsible"): ("page not read", "founder", "read a page", CAA,
        "The payout-currency and fee docs state the conversion rules (WC-S-0535, WC-S-0540) but not who is legally responsible for payouts and conversion. "
        "Whether Stripe's agreement may be read as part of WooPayments' terms is for the founder."),
    ("WC-C-115", "responsible"): ("page not read", "founder", "read a page", CAA + "; Stripe's Radar terms",
        "The Radar doc says most Radar rules 'are managed by our team and cannot be modified by merchants' (WC-S-0865), but no term read says who is legally responsible for the screening. "
        "Stripe's documents are outside the platform's own material unless the founder decides otherwise."),
    ("WC-C-020", "decides"): ("page not read", "founder", "read a page", CAA,
        "No WooCommerce or Automattic source read names the licence, the licensed entity or the regulator under which WooPayments balances are held or moved (first-run notes). "
        "The Connected Account Agreement is Stripe's own document; whether it may be read is for the founder."),
    ("WC-C-020", "where"): ("page not read", "founder", "read a page", CAA,
        "Where the funds sit is described only as a 'WooPayments account balance' on a Stripe Express account (WC-S-0529, WC-S-0504); no source read names the licensed holder."),
    ("WC-C-020", "boundary"): ("page not read", "founder", "read a page", CAA,
        "The docs name the agreement (WC-S-0507) but no interface or event at the licence boundary."),
    ("WC-C-020", "reason"): ("page not read", "founder", "read a page", CAA,
        "No source read gives a reason for the placement of WooPayments funds with Stripe."),
    ("WC-C-010", "where"): ("observation needed", "founder", "record a journey",
        "WooPayments onboarding on a test store: WP Admin > Payments > set up WooPayments (country and account type steps)",
        "The countries doc says the business's registration country is selected 'when signing up' (WC-S-0512) but no page read shows where in the product the country is set or checked; the onboarding runs on WooPayments' servers and needs a WordPress.com account."),
    ("WC-C-010", "boundary"): ("observation needed", "founder", "record a journey",
        "WooPayments onboarding on a test store: WP Admin > Payments > set up WooPayments; the release's WooPayments onboarding REST routes (src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsRestController.php) are the store side",
        "No page read names the API or event through which a country's eligibility is checked; a recorded onboarding would show the requests and the Stripe Express hand-off."),
    ("WC-C-051", "where"): ("observation needed", "founder", "record a journey",
        "A store with WooPayments: Payments > Settings (payout and currency sections) and the Stripe Express dashboard",
        "The docs state the payout-currency rules (WC-S-0535, WC-S-0536) but not where bank accounts for each currency are added; the partnership doc says some account information can only be updated in the Stripe Express dashboard, without naming payout currencies."),
    ("WC-C-115", "boundary"): ("observation needed", "founder", "record a journey",
        "A store with WooPayments: Payments > Settings > Fraud protection, and a test transaction blocked by Radar",
        "The Radar doc says Radar is used and rules are managed by the WooPayments team (WC-S-0864, WC-S-0865); no page read names the interface through which Radar results reach the store."),
    ("WC-C-046", "responsible"): ("searched, not found", "founder", "ask the platform",
        "woocommerce.com/document/maxmind-geolocation-integration/ (read); MaxMind's GeoLite2 licence is MaxMind's own document",
        "The doc tells the merchant to create a MaxMind account and licence key (WC-S-0908 and new statements) but no Woo or Automattic page read says who is legally responsible for the geolocation data; MaxMind's terms are a third party's document."),
}

def gap_for(c, p):
    if (c, p) in SPECIAL:
        kind, who, means, route, why = SPECIAL[(c, p)]
        what = {"where": f"A source that states where {CON[c]} sits (product, host, page or code path).",
                "decides": f"A source that states what turns {CON[c]} on or off, limits it, or sets its value.",
                "responsible": f"A source that states who is legally responsible for {CON[c]}.",
                "boundary": f"A source that names the API, event, setting or contract at the boundary of {CON[c]}.",
                "reason": f"A source that states why {CON[c]} is placed as it is."}[p]
        G(c, p, what, means, who, route, why, kind)
        return
    if p == "responsible":
        gap_general_responsible(c)
        return
    if c in CATEGORY and c != "WC-C-111" and p in ("decides",):
        G(c, p, f"A WooCommerce statement of what turns {CON[c]} on or limits it, other than the Terms' general clause on Third-Party Services.",
          "ask the platform", "founder", TOS_ROUTE,
          f"For this Marketplace category the only source on who decides is the Terms' general definition of Third-Party Services ('you may enable, use, or purchase ... extensions, plugins ...', WC-S-0852), "
          "which speaks of all third-party products; the category mixes products made by Woo and by third parties, so applying it here would be inference.",
          "stated only in general terms")
        return
    if c in NO_WOO and p == "boundary":
        slug, n, vendors, example = NO_WOO[c]
        G(c, p, "The developer documentation of a Woo-made product in this category, naming its hooks, REST routes or other interfaces.",
          "read a page or ask the platform", "founder",
          f"searched: woocommerce.com/wp-json/wccom-extensions/1.0/search?category={slug} (the Marketplace's product listing for the category, {n} products), "
          f"compared with category=developed-by-woo (63 products); not read: the vendors' own docs on woocommerce.com, e.g. {example}",
          f"None of the {n} products the Marketplace lists in this category is in Developed by Woo (vendors: {vendors}). "
          "Vendors' own docs on woocommerce.com are not used as WooCommerce statements, as in the first run; whether they may be is for the founder.",
          "searched, not found")
        return
    if c in LEGAL and p in ("where", "boundary"):
        G(c, p,
          "A WooCommerce or Automattic source placing this concern in the software or naming an API, event or setting at its boundary." if p == "where" else
          "A WooCommerce or Automattic source naming the API, event, setting or contract at the boundary of this concern.",
          "read a page or ask the platform", "either", f"searched: {read_list(c)}",
          f"The sources read state {CON[c]} as terms or policy; none places it in the software or names an interface for it.",
          "searched, not found")
        return
    if p == "reason":
        G(c, p, f"A WooCommerce or Automattic statement of why {CON[c]} is placed as it is (in its documentation, the code's comments, or a developer.woocommerce.com blog post).",
          "read a page or ask the platform", "either",
          f"searched: {read_list(c)}; not searched: developer.woocommerce.com/blog/",
          "The pages and code read for this concern describe it without giving a reason for its placement.",
          "searched, not found")
        return
    # remaining where / decides / boundary cells
    what = {"where": f"A source that states where {CON[c]} sits (product, host, admin page or code path).",
            "decides": f"A source that states what turns {CON[c]} on or off, limits it, or sets its value (a setting, condition, capability or eligibility rule).",
            "boundary": f"A source that names the API, hook, event or contract through which {CON[c]} meets the rest."}[p]
    G(c, p, what, "read a page or ask the platform", "either", f"searched: {read_list(c)}",
      "The sources read for this concern do not state this.", "searched, not found")

for c in CON:
    for p in P:
        if not have[(c, p)]:
            gap_for(c, p)
