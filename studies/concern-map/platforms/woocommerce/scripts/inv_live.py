# Inventory rows from live WooCommerce/Automattic lists, each with a citation key.
# Usage: python3 -I inv_live.py -> out/inv_live.json
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from webcite import web as W, rel as R, k
F = os.path.normpath(os.path.join(HERE, "..", "fetched"))
rows = []


def add(lst, entry, key, note=""):
    rows.append(dict(list=lst, entry=entry, key=key, note=note))


def txt(name):
    return open(os.path.join(F, name), encoding="utf-8").read()


# ---------- A. REST API reference: navigation groups ----------
API = "https://woocommerce.github.io/woocommerce-rest-api-docs/"
h = txt("woocommerce.github.io_woocommerce_rest_api_docs.html")
for m in re.finditer(r"<h1 id='([^']+)'>(.*?)</h1>\s*(<p>(.*?)</p>)?", h, re.S):
    hid, title, p = m.group(1), html.unescape(m.group(2)), m.group(4) or ""
    ptxt = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
    first = re.split(r"(?<=\.)\s", ptxt)[0] if ptxt else ""
    quote = first if first and title.split()[0].lower()[:5] in first.lower() and len(first) < 300 else title
    key = "api_nav_" + hid
    W(key, API, quote, f"navigation group #{hid}")
    add("api-resources", title, key, note="REST API reference navigation group")

# ---------- B. Marketplace categories (rendered filter lists) ----------
MP = "https://woocommerce.com/products/"
for top in ["Extensions", "Themes", "Business services"]:
    key = "mkt_top_" + top.lower().replace(" ", "_")
    W(key, MP, top, "Marketplace navigation: Discover", method="rendered")
    add("other:marketplace-categories", top, key)
EXT = "https://woocommerce.com/product-category/woocommerce-extensions/"
cats = ["Developed by Woo", "Official payments", "Shipping, delivery and fulfillment", "Conversion", "Customer service",
        "Merchandising", "Store content and customizations", "Store management", "Marketing"]
for c in cats:
    key = "mkt_cat_" + re.sub(r"[^a-z]+", "_", c.lower()).strip("_")
    W(key, EXT, c, "Search filters > Category", method="rendered")
    add("other:marketplace-categories", "Extensions > " + c, key)
SUB = {
    "payment-gateways": "Official payments", "shipping-delivery-and-fulfillment": "Shipping, delivery and fulfillment",
    "conversion": "Conversion", "customer-service-2": "Customer service", "merchandising": "Merchandising",
    "store-content-and-customizations": "Store content and customizations", "operations": "Store management",
    "marketing-extensions": "Marketing"}
for slug, parent in SUB.items():
    url = EXT + slug + "/"
    t = txt("woocommerce.com_product_category_woocommerce_extensions_" + slug.replace("-", "_") + ".rendered.txt")
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    i = lines.index("Category")
    seg = lines[i + 1:lines.index("Price", i)]
    j = seg.index(parent)
    subs = []
    for x in seg[j + 1:]:
        if x in cats:
            break
        subs.append(x)
    for s_ in subs:
        key = "mkt_sub_" + re.sub(r"[^a-z]+", "_", (parent + " " + s_).lower()).strip("_")
        W(key, url, s_, f"Search filters > Category > {parent}", method="rendered")
        add("other:marketplace-categories", f"Extensions > {parent} > {s_}", key)
BS = "https://woocommerce.com/product-category/business-services/"
t = txt("woocommerce.com_product_category_business_services.rendered.txt")
lines = [l.strip() for l in t.split("\n") if l.strip()]
i = lines.index("Category")
for s_ in lines[i + 2:lines.index("Show search results", i)]:
    key = "mkt_bs_" + re.sub(r"[^a-z]+", "_", s_.lower()).strip("_")
    W(key, BS, s_, "Search filters > Category (Business services)", method="rendered")
    add("other:marketplace-categories", "Business services > " + s_, key)

# ---------- C. Blocks and Store API extension points (developer docs index) ----------
LL = "https://developer.woocommerce.com/llms.txt"
for line in txt("developer.woocommerce.com_llms.txt.txt").split("\n"):
    m = re.match(r"^\[([^\]]+)\]\((https://raw\.githubusercontent\.com/woocommerce/woocommerce/trunk/docs/([^)]+))\)", line)
    if not m:
        continue
    title, url, p = m.groups()
    if p.startswith("block-development/extensible-blocks/") or p.startswith("apis/store-api/extending-store-api/"):
        q = f"[{title}]({url})"
        key = "llms_" + re.sub(r"[^a-z0-9]+", "_", p.lower()).strip("_")
        W(key, LL, q, "llms.txt index entry")
        grp = "Blocks" if p.startswith("block-development") else "Store API"
        add("extension-points", title, key, note=p)

# ---------- D. WooPayments documentation topics ----------
WPD = "https://woocommerce.com/document/woopayments/"
t = txt("woocommerce.com_document_woopayments.rendered.txt")
lines = [l.strip() for l in t.split("\n") if l.strip()]
i = next(n for n, l in enumerate(lines) if l.endswith("Our topic pages are:"))
for topic in lines[i + 1:lines.index("Contact support", i)]:
    key = "wpd_topic_" + re.sub(r"[^a-z]+", "_", topic.lower()).strip("_")
    W(key, WPD, topic, "Specific topics: topic pages", method="rendered")
    add("other:woopayments-doc-topics", topic, key)

# ---------- E. Plugin page features (wordpress.org) ----------
PP = "https://wordpress.org/plugins/woocommerce/"
PPD, PPB = "2026-10-09", "plugin page shows Version 11.2.1 and 'Last updated 1 day ago' when read on 2026-10-10"
for lead, q in [
    ("Create beautiful, enticing storefronts", "Create beautiful, enticing storefronts with themes suited to your brand and industry."),
    ("Increase revenue", "Increase revenue with an optimized shopping cart experience that converts."),
    ("Customize product pages in minutes", "Customize product pages in minutes using modular product blocks."),
    ("Showcase physical and digital goods", "Showcase physical and digital goods, product variations, custom configurations, instant downloads, and affiliate items."),
    ("Sell subscriptions, bookings, or memberships", "Sell subscriptions, bookings, or memberships, with our developer-vetted extensions."),
    ("Rise to the top of search results", "Rise to the top of search results by leveraging WordPress’ SEO advantage."),
    ("Build on a platform that scales", "Build on a platform that scales. Get flexible ecommerce for high-volume stores."),
    ("Choose how you want to get paid", "Choose how you want to get paid. Conveniently manage payments from the comfort of your store with WooPayments"),
    ("Configure your shipping options", "Configure your shipping options. Print USPS labels right from your dashboard and even schedule a pickup with WooCommerce Shipping (U.S.-only)."),
    ("Simplify sales tax", "Simplify sales tax. Add WooCommerce Tax or similar integrated services to make automated calculations a reality."),
    ("Grow your business, add features, and monitor your store on the go", "Grow your business, add features, and monitor your store on the go"),
    ("Own and control your store data – forever", "Own and control your store data – forever"),
    ("Connection to WooCommerce.com", "Connection to WooCommerce.com"),
]:
    key = "pp_" + re.sub(r"[^a-z]+", "_", lead.lower()).strip("_")
    W(key, PP, q, "Description", PPD, PPB)
    add("other:plugin-page-features", lead, key)

# ---------- F. Woo services named in the Terms of Service ----------
for s_ in ["WooCommerce", "WooPayments", "WooCommerce Shipping", "WooCommerce Tax", "MailPoet"]:
    add("other:tos-woo-services", s_, "tos_woo_services")

# ---------- G. Legal agreements and policies ----------
TOSD, TOSB = "2026-10-06", "last updated: Terms of Service 'Last Updated: October 6, 2026'"
PS = "https://woocommerce.com/page-sitemap.xml"
W("legal_privacy_title", "https://automattic.com/privacy/", "Your privacy is critically important to us.", "Privacy Policy (opening)")
W("legal_ca_notice", MP, "Privacy Notice for California Users", "site footer", method="rendered")
W("legal_dnsmpi", "https://woocommerce.com/do-not-sell-or-share-my-personal-information/", "Do not sell or share my personal information", "page heading")
W("legal_support_policy", "https://woocommerce.com/support-policy/", "We support products sold on WooCommerce.com (the “Products”), which may be developed by WooCommerce or a third-party developer.", "WooCommerce Support Policy")
W("legal_refund_policy", "https://woocommerce.com/refund-policy/", "For extensions and themes purchased from our Marketplace, we offer a full refund within 30 days of your date of purchase.", "Refund Policy")
W("legal_trademark", MP, "Woo trademark guidelines", "site footer", method="rendered")
W("legal_brand", MP, "Brand and logo guidelines", "site footer", method="rendered")
W("legal_store_guidelines", "https://en.support.wordpress.com/store-guidelines/", "Store guidelines", "page heading")
W("legal_dpa_page", "https://en.support.wordpress.com/automattic-gdpr/data-processing-agreements/", "The Data Processing Agreement is an amendment to our Terms of Service and is available to all WordPress.com site owners.", "Request a data processing agreement")
W("legal_cbd", TOSURL := "https://wordpress.com/tos/", "If you’re using Ecommerce Services to sell CBD and other hemp-derived products using Woo, you must follow the Woo Guidelines for CBD and Other Hemp-Derived Products.", "8. j. Ecommerce Services: Prohibited Uses", TOSD, TOSB)
W("legal_ai_guidelines", TOSURL, "Please see our AI Guidelines for the policies you must comply with when you use AI features", "8. k. Artificial Intelligence", TOSD, TOSB)
W("legal_cookie", "https://woocommerce.com/tracking-and-opt-outs/", "You can also find details about the cookies we use on WooCommerce.com in our Cookie Policy", "Other tracking")
for slug in ["customer-research-agreement", "code-of-conduct", "wooads-policy", "terms-conditions/woopayments-promotion",
             "terms-conditions/woopayments-mid-2025-promotional-offer-terms-and-conditions", "terms-conditions/woopayments-action-promotion-2023"]:
    W("legal_ps_" + re.sub(r"[^a-z0-9]+", "_", slug), PS, f"https://woocommerce.com/{slug}/", "page sitemap <loc>")
LEGAL = [
    ("Terms of Service", "tos_scope", "woocommerce.com/terms-conditions/ redirects to wordpress.com/tos/"),
    ("Privacy Policy", "legal_privacy_title", ""),
    ("Privacy Notice for California Users", "legal_ca_notice", ""),
    ("Do not sell or share my personal information", "legal_dnsmpi", ""),
    ("WooCommerce Support Policy", "legal_support_policy", ""),
    ("Refund Policy", "legal_refund_policy", ""),
    ("Woo trademark guidelines", "legal_trademark", ""),
    ("Brand and logo guidelines", "legal_brand", ""),
    ("Marketplace Vendor Agreement", "va_parties", ""),
    ("Store guidelines", "legal_store_guidelines", "referenced by the Terms for Ecommerce Services"),
    ("Restricted businesses and activities", "restricted_stripe_list", "referenced by the Terms for WooPayments"),
    ("Request a data processing agreement", "legal_dpa_page", "referenced by Terms section 19"),
    ("Connected Account Agreement", "wp_caa", "accepted at WooPayments signup, per the WooPayments docs"),
    ("Woo Guidelines for CBD and Other Hemp-Derived Products", "legal_cbd", ""),
    ("AI Guidelines", "legal_ai_guidelines", ""),
    ("Cookie Policy", "legal_cookie", ""),
    ("WooCommerce usage tracking", "ut_off_default", ""),
    ("WooCommerce Analytics data syncing", "wca_sync", ""),
    ("customer-research-agreement", "legal_ps_customer_research_agreement", "page sitemap entry"),
    ("code-of-conduct", "legal_ps_code_of_conduct", "page sitemap entry"),
    ("wooads-policy", "legal_ps_wooads_policy", "page sitemap entry"),
    ("terms-conditions/woopayments-promotion", "legal_ps_terms_conditions_woopayments_promotion", "page sitemap entry"),
    ("terms-conditions/woopayments-mid-2025-promotional-offer-terms-and-conditions", "legal_ps_terms_conditions_woopayments_mid_2025_promotional_offer_terms_and_conditions", "page sitemap entry"),
    ("terms-conditions/woopayments-action-promotion-2023", "legal_ps_terms_conditions_woopayments_action_promotion_2023", "page sitemap entry"),
    ("GPLv3", "readme_license", "release readme.txt and license.txt"),
]
for entry, key, note in LEGAL:
    add("legal-agreements", entry, key, note)

for r in rows:
    r["cite_id"] = k(r["key"])
json.dump(rows, open(os.path.join(HERE, "out", "inv_live.json"), "w"), ensure_ascii=False, indent=0)
from collections import Counter
for a, b in Counter(r["list"] for r in rows).items():
    print(b, a)
print(len(rows), "live rows")
