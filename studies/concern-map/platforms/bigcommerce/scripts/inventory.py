# Builds the inventory from BigCommerce's own lists (working copies in fetched/).
# Each list returns rows: (list_name, entry, cite_key, cite_locator, cite_quote, concern_numbers, out_of_scope_reason)
import csv, os, re
from bcsrc import F

OOS_OVERVIEW = "Overview page of the API reference; it names no resource of its own (the resources it introduces are entries of their own)."
OOS_SUPPORT = "BigCommerce's own customer support service level, sold with the plan; not a part of the commerce platform's division into concerns."


def api_nav():
    rows = []
    cite = ("llms_dev", "## Docs, API reference pages (index lines 536-645)",
            "- [Catalog - Brands](https://docs.bigcommerce.com/developer/api-reference/rest/admin/catalog/brands.md)")
    m = {  # index line -> concerns
        540: [14], 541: [16], 542: [37], 543: [32], 544: [35], 545: [32], 546: [18], 547: [6],
        549: [53], 550: [33], 551: [33], 552: [2], 553: [3], 554: [3], 555: [1], 556: [1], 557: [1], 558: [1],
        559: [15], 560: [42], 561: [46], 562: [45], 563: [10], 564: [45], 565: [42], 566: [43], 567: [43],
        568: [15], 569: [14], 570: [38], 571: [16], 572: [74], 573: [32], 574: [32], 575: [34], 576: [75],
        577: [52], 578: [4], 579: [18], 580: [18, 20, 21], 581: [6], 582: [6], 583: [6], 584: [8], 585: [7],
        586: [9], 587: [9], 588: [41], 589: [44], 590: [47], 591: [70], 592: [40], 593: [49], 594: [47],
        595: [35], 596: [60], 597: [72], 598: [72], 599: [72], 600: [72], 601: [36], 602: [22], 603: [24],
        604: [23], 605: [23], 606: [23], 607: [20], 608: [71, 73], 609: [71], 610: [73], 611: [58],
        612: [65], 613: [65], 614: [65], 615: [65], 616: [65], 617: [65], 618: [65], 619: [65], 620: [65],
        621: [65], 622: [65], 623: [65], 624: [65], 625: [65], 626: [65], 627: [65], 628: [65], 629: [31],
        630: [65], 631: [31], 632: [65], 633: [65], 634: [65], 635: [65], 636: [65], 638: [55],
        639: [63], 640: [63], 641: [63], 642: [63], 643: [63],
    }
    oos = {536: OOS_OVERVIEW, 537: "Download page for the OpenAPI specification files; not a resource.",
           538: "Status codes and query parameters common to all REST APIs; not a resource.",
           539: OOS_OVERVIEW, 548: OOS_OVERVIEW, 637: OOS_OVERVIEW}
    with open(os.path.join(F, "apiref-nav.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            line = int(r["line"])
            name = r["nav_title"]
            if name == "Overview" and r["h1"]:
                name = r["h1"]
            path = r["url"].replace("https://docs.bigcommerce.com/developer/api-reference/", "")[:-3]
            entry = f"{name} [{path}]"
            rows.append(("api-resources", entry, *cite, m.get(line, []), oos.get(line, "")))
    g = ("a:graphql/overview", "GraphQL API Overview, list of GraphQL APIs", "BigCommerce offers several GraphQL APIs for different use cases:")
    for name, c in (("Account API", [55]), ("Admin API", [54]), ("Storefront API", [53]), ("B2B API", [65])):
        rows.append(("api-resources", f"{name} [graphql]", *g, c, ""))
    b = ("llms_dev", "## API Docs, Beta groups (index lines 997-1019)",
         "- Beta Powered By > Accounts [List Accounts](https://docs.bigcommerce.com/developer/docs/beta/powered-by/api-reference/accounts/get-accounts.md)")
    for name, c in (("Beta Checkout Extensions", [17]), ("Beta Page Widgets", [43]), ("Beta Powered By", [66]),
                    ("Beta Product Recommendations", [13])):
        rows.append(("api-resources", name, *b, c, ""))
    return rows


def webhook_concerns(page, section, scope):
    s = scope
    c = set()
    if "/metafield" in s:
        c.add(49)
    sec = {"Brands": 2, "Cart line items": 14, "Carts": 14, "Categories": 3, "Category trees": 3, "Channel events": 38,
           "Customers": 32, "Delivery exception hooks": 58, "Emails": 46, "Inventory": 4, "Locations": 5, "Metafields": 49,
           "Modifiers": 1, "Notifications": 46, "Options": 1, "Orders": 18, "Pages": 45, "Price lists": 7,
           "Price list records": 7, "Price list assignments": 7, "Product assignments": 38, "Products": 1,
           "Redirects": 41, "Routes": 40, "Scripts": 44, "Settings": 47, "Shipments": 19, "Sites": 40, "SKUs": 1,
           "Social media links": 47, "Stores": 47, "Subscribers": 35, "Themes": 42,
           "Companies": 65, "Company Addresses": 65, "Company Users": 65, "Quotes": 65, "Super Admins": 65}[section]
    over = [("cart/abandoned", 15), ("order/refund", 21), ("order/transaction", 20), ("payment/instrument", 24),
            ("app/uninstalled", 59), ("settings/currency", 74), ("settings/locale", 48), ("settings/checkout", 16),
            ("settings/search", 11), ("settings/inventory", 4), ("settings/category", 3), ("settings/product", 1),
            ("settings/catalog", 1), ("settings/customer", 32), ("settings/security", 78), ("notifications/abandonedCart", 15),
            ("notifications/inventory", 4), ("login/access", 33), ("inventory/location/metafield", 5)]
    hit = [n for k, n in over if k in s]
    if hit:
        c.update(hit)
    else:
        c.add(sec)
    return sorted(c)


def webhooks():
    pages = {
        "integrations_webhooks_event-reference_events.md": ("d:integrations/webhooks/event-reference/events", "Webhook Events (all sections)",
            "This article contains a complete reference of all BigCommerce webhook events and their callback payloads."),
        "integrations_webhooks_event-reference_channel-events.md": ("d:integrations/webhooks/event-reference/channel-events", "Channel Webhooks (all sections)",
            "Developers building third-party sales channels or multi-storefront capabilities might need notification when a channel in BigCommerce changes so that they can perform downstream actions required to set up or deactivate the channel."),
        "integrations_webhooks_event-reference_inventory-and-location-events.md": ("d:integrations/webhooks/event-reference/inventory-and-location-events", "Inventory and location events",
            "This page is a reference for inventory and location webhooks for *Buy Online, Pick up in Store*. This article assumes that you're familiar with webhooks."),
        "integrations_webhooks_event-reference_b2b-edition.md": ("d:integrations/webhooks/event-reference/b2b-edition", "B2B Edition Webhooks",
            "This page is a reference for B2B Edition webhooks and it assumes that you're familiar with webhooks."),
    }
    rows = []
    with open(os.path.join(F, "webhook-events.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            key, loc, quote = pages[r["page"]]
            rows.append(("webhook-topics", r["scope"], key, loc, quote, webhook_concerns(r["page"], r["section"], r["scope"]), ""))
    return rows


SCOPE_MAP = {
    "store_payments_access_token_create": [22], "store_storefront_api": [53], "store_storefront_api_customer_impersonation": [53],
    "store_app_extensions_manage": [59], "store_cart": [14], "store_cart_read_only": [14],
    "store_channel_settings": [38], "store_channel_settings_read_only": [38], "store_channel_listings": [38], "store_channel_listings_read_only": [38],
    "store_checkout": [16], "store_checkout_read_only": [16], "store_content_checkout": [16], "store_content_checkout_read_only": [16],
    "store_v2_content": [45], "store_v2_content_read_only": [45], "store_v2_customers": [32], "store_v2_customers_read_only": [32],
    "store_v2_customers_login": [33], "store_fulfillment_methods_manage": [6, 19], "store_fulfillment_methods_read_only": [6, 19],
    "store_v2_information": [47], "store_v2_information_read_only": [47], "store_v2_marketing": [10], "store_v2_marketing_read_only": [10],
    "store_metafield_change_owner": [49], "store_metafield_write": [49], "store_metafield_write_all": [49],
    "store_v2_orders": [18], "store_v2_orders_read_only": [18], "store_order_fulfillment_manage": [19], "store_order_fulfillment_read_only": [19],
    "store_v2_transactions": [20], "store_v2_transactions_read_only": [20], "store_payments_methods_read": [23],
    "store_v2_products": [1, 2, 3], "store_v2_products_read_only": [1, 2, 3], "store_sites": [40], "store_sites_read_only": [40],
    "store_inventory": [4], "store_inventory_read_only": [4], "store_locations": [5], "store_locations_read_only": [5],
    "store_stored_payment_instruments_read_only": [24], "store_stored_payment_instruments": [24],
    "store_translations_read_only": [48], "store_translations": [48], "store_themes_manage": [42], "store_themes_read_only": [42],
    "store_b2b_manage": [65, 31], "account_read": [55], "account_apps_read": [55, 59], "account_checkouts_read": [55, 29],
    "account_checkouts_create": [55, 29], "account_stores_read": [55], "account_subscriptions_read": [55, 29],
    "account_subscriptions_cancel": [55, 29], "account_users_read": [55, 61], "account_users_write": [55, 61], "account_users_delete": [55, 61],
}


def scopes():
    rows = []
    p = os.path.join(F, "docs/overview_api-fundamentals_api-accounts.md")
    lines = open(p, encoding="utf-8").read().splitlines()[197:272]
    cite = ("d:overview/api-fundamentals/api-accounts", "## OAuth scopes (Token creation, Store resource and Account resource scopes tables)",
            "**Scope** grants and limits a program's ability to read and write data. Set the scopes to the minimum level of access your implementation needs.")
    for l in lines:
        m = re.match(r"^\|[^|]*\|[^|]*\|\s*`([a-z0-9_]+)`\s*\|", l)
        if m:
            rows.append(("access-scopes", m.group(1), *cite, SCOPE_MAP[m.group(1)], ""))
    return rows


def settings():
    cite = ("a:rest/admin/management/settings", "## Available settings and configuration",
            "Manage settings and configuration for BigCommerce hosted stores and headless storefronts.")
    m = {"Analytics": [62], "Catalog": [1], "Email Statuses": [46], "Favicon Image": [47], "Inventory": [4],
         "Inventory Notifications": [4], "Logo": [47], "Logo Image": [47], "Search Filters": [11], "Store Locale": [48],
         "Store Profile": [47], "Storefront Category": [3], "Storefront Product": [1], "Storefront Robots.txt": [47],
         "Storefront Search": [11], "Storefront Security": [78], "Storefront SEO": [47], "Storefront Status": [47],
         "Units of Measurement": [47]}
    return [("settings", k, *cite, v, "") for k, v in m.items()]


def plan_features():
    cite = ("w:pricing/", "Compare plans tables: Features, Payment Processing, Sales Channels, Service & Support (raw HTML)",
            "Annual online sales are calculated on a trailing 12-month basis using BigCommerce's GMV (gross order value minus 10%).")
    m = [("Mobile responsive website", [42]), ("BigCommerce mobile app", [77]), ("Single-page checkout", [16]),
         ("Apple Pay, Google Pay, and Amazon Pay", [27]), ("Products, file storage, and bandwidth", [1]), ("Staff accounts", [61]),
         ("Coupons, discounts, and gift cards", [9, 10]), ("Multi-currency", [74]), ("Real-time shipping quotes", [70]),
         ("Professional reporting tools", [62]), ("Built-in blog", [45]), ("Product ratings and reviews", [12]),
         ("Free sitewide HTTPS and dedicated SSL", [78]), ("ShipperHQ shipping rules engine", [70]),
         ("Customer groups and segmentation", [34]), ("Abandoned cart saver", [15]), ("Persistent cart", [14]),
         ("Stored credit cards", [24]), ("Google customer reviews", [12]), ("Product filtering", [11]),
         ("Custom product filtering", [11]), ("Price Lists", [7]), ("Advanced promotions management", [9]),
         ("Inventory locations", [5]), ("GMV cap", [30]), ("Orders through Embedded Payment Providers", [26]),
         ("Open Payment Provider Fee", [26, 30]), ("Embedded Payment Provider List", [26]), ("Online storefront", [38]),
         ("Multi-storefront", [39]), ("Point of sale", [69]), ("Amazon / eBay / Walmart", [68]),
         ("Google / Meta / TikTok / Microsoft / Pinterest (Feedonomics Surface)", [67, 68])]
    rows = [("plan-features", k, *cite, v, "") for k, v in m]
    for k in ("24/7 tech support — chat & email", "24/7 phone support (included)", "Express routing & priority support",
              "Customer Success Manager", "API support"):
        rows.append(("plan-features", k, *cite, [], OOS_SUPPORT))
    return rows


def embedded_providers():
    cite = ("w:pricing/", "Payment Processing table, Embedded Payment Provider List (raw HTML)",
            "The Embedded Payment Providers listed are not subject to any additional order fees. Any payment provider not on this list is considered an Open Payment Provider and is subject to the fee.")
    names = ["BigCommerce Payments", "Adyen", "Affirm", "Afterpay", "Amazon Pay", "Bank of New Zealand", "Checkout.com", "Clearpay",
             "Fortis (Acumatica Payments)", "Global Payments", "Klarna", "PayPal Braintree", "PayPal Complete Payments", "PayPal Wallet",
             "Bluesnap (powered by Payroc)", "Bankful (Pinwheel)", "Sezzle", "Stripe", "TD Online Mart", "Worldpay", "Zip Money"]
    return [("other:embedded-payment-providers", n, *cite, [25, 26] if n == "BigCommerce Payments" else [26], "") for n in names]


def legal():
    cite = ("c:terms/", "Master Services Agreement, Scope and Definitions: Incorporated Terms",
            "The following policies, guidelines, and agreements (“Incorporated Terms”) are hereby incorporated into, and form an integral part of, the Agreement to which you are agreeing to be bound:")
    m = [("Master Services Agreement", [79, 80, 28, 83, 84], ""), ("Privacy Policy (Commerce.com Specific)", [81, 82], ""),
         ("Privacy Policy (Feedonomics Specific)", [67, 81], ""), ("Privacy Policy (Makeswift Specific)", [51, 81], ""),
         ("Acceptable Use Policy", [85], ""), ("API Terms", [56, 57], ""), ("Fees and Billing Terms", [30, 26], ""),
         ("Infringing Materials Protocol", [88], ""), ("Jurisdiction-Specific Terms", [79], ""), ("Merchant-Client Terms", [87], ""),
         ("Mobile App Terms", [77], ""), ("Store Terms", [86, 42], ""), ("Data Processing Addendum", [81, 82, 83], ""),
         ("Unified Billing Terms", [29], ""), ("Unified Billing Terms (US, UK, & Canada)", [29], ""),
         ("Unified Billing Terms (India Specific)", [29], ""),
         ("Professional Services", [], "Program document for BigCommerce's own consulting and implementation services; not a part of the commerce platform's division into concerns."),
         ("AI Features Addendum", [64, 63], ""),
         ("Website Terms of Use", [], "Governs use of BigCommerce's marketing website, not the commerce services."),
         ("Legal Archives", [], "Earlier versions of the agreements; the current versions are entries of their own.")]
    return [("legal-agreements", k, *cite, v, o) for k, v, o in m]


def app_categories():
    cite = ("w:apps/", "Apps & Integrations: All Categories", "All Categories Accounting & Tax Ecommerce AI Analytics & Reporting")
    m = [("Accounting & Tax", [59, 73]), ("Ecommerce AI", [59, 64]), ("Analytics & Reporting", [59, 62]), ("B2B/Wholesale", [59, 65]),
         ("Catalog & Order Management", [59, 1, 18]), ("Checkout", [59, 16]), ("CMS & Hosting", [59, 45]),
         ("CRM & Customer Service", [59, 32]), ("Data Transfer/Migration Services", [59]), ("ERP", [59]), ("Financing", [59, 26]),
         ("Marketing", [59, 10]), ("Merchandising", [59]), ("Mobile", [59]), ("Payments & Security", [59, 26]),
         ("POS & In-Store", [59, 69]), ("Product & Shipping Protection", [59]), ("Product Sourcing", [59]),
         ("Sales Channels", [59, 68]), ("Shipping & Fulfillment", [59, 70, 71]), ("Site Tools", [59])]
    return [("other:app-marketplace-categories", k, *cite, v, "") for k, v in m]


def product_lines():
    cite = ("w:product/", "All Features (Checkout & payments; B2B commerce; AI & agentic commerce; Omnichannel & growth; Operations & catalog; Enterprise & developers)",
            "Checkout & payments Optimized checkout Reduce friction and increase conversion with a fast, streamlined checkout experience.")
    m = [("Optimized checkout", [16]), ("Checkout customization", [16]), ("Payment freedom", [26]), ("Digital wallets", [27]),
         ("Abandoned cart recovery", [15]), ("Refunds & returns", [21]),
         ("B2B Edition", [65]), ("Buyer portal", [65]), ("Customer-specific pricing", [65, 7]), ("Customer-specific catalogs", [65]),
         ("Sales rep ordering", [65]), ("Company account hierarchy", [65]), ("Quoting & CPQ", [65]), ("Invoicing & net terms", [31]),
         ("Requisition lists & reordering", [65]),
         ("BigAI", [64]), ("Feedonomics enrichment", [67]), ("AI discovery", [63]), ("Agentic checkout", [63]),
         ("Conversational shopping", [64]), ("BigCommerce Companion", [64]),
         ("Feedonomics Surface", [67]), ("Omnichannel management", [38]), ("Marketplaces", [68]), ("Social channels", [68]),
         ("Google Shopping", [68]), ("POS integrations", [69]), ("Buy online, pick up in store", [6]),
         ("Catalog management", [1]), ("Product filtering", [11]), ("Inventory management", [4]), ("Order management", [18]),
         ("Shipping", [70]), ("Tax", [72, 73]), ("Reporting & analytics", [62]), ("Customer groups", [34]),
         ("Open APIs", [56]), ("Headless commerce", [50, 53]), ("Composable commerce", [59]), ("GraphQL Storefront API", [53]),
         ("Integrations", [59]), ("Security & compliance", [78, 28]), ("Performance & reliability", [83]),
         ("Staging environments", [76]), ("Big Open Data Solutions", [62])]
    return [("other:product-lines", k, *cite, v, "") for k, v in m]


def contracting_entities():
    cite = ("c:terms/", "Master Services Agreement, Contracting Entity table",
            "If you have not previously entered into an agreement with a Commerce entity, then “Commerce” means the entity identified in the following table:")
    m = [("United States | Commerce.com US, Inc., a Texas corporation in the United States | New York", [79]),
         ("United Kingdom | Commerce Software UK Ltd., a United Kingdom limited company | England and Wales", [79]),
         ("European Union | Commerce Software Ireland Ltd., an Irish limited company | Ireland", [79]),
         ("Australia | Commerce.com Pty. Ltd., an Australia proprietary limited company | New South Wales, Australia", [79]),
         ("Any other jurisdiction | Commerce.com Pty. Ltd., an Australia proprietary limited company | New York", [79]),
         ("Worldwide | Feedonomics Holdings, LLC, a Delaware corporation in the United States | New York | Feedonomics Platform", [79, 67]),
         ("Worldwide | Makeswift, Inc. a Delaware Corporation in the United States | New York | Makeswift visual editor / builder", [79, 51])]
    return [("other:contracting-entities", k, *cite, v, "") for k, v in m]


def subprocessors():
    cite = ("c:privacy/data-processors/", "Third-Party Subprocessors (Commerce, Feedonomics and Commerce Extension tables)",
            "When acting as a processor on behalf of merchants in providing ecommerce Services, Commerce.com and its affiliates")
    hosting = {"Amazon", "Google", "Cloudflare"}
    names = ["Amazon", "Atlassian", "Cloudflare", "Confluent", "Google", "Sentry I/O by Functional Software", "Snowflake",
             "The Functionary", "Sysdig", "Sumo Logic", "Relyance AI", "ServiceNow Cloud Observability", "Teleport (Gravitational Inc)",
             "EPAM", "Microsoft", "AgileBits, Inc.", "NewRelic", "Cube27", "Microsourcing", "FDX South Africa", "Noibu"]
    return [("other:subprocessors", n, *cite, [83, 82] if n in hosting else [83], "") for n in names]


def all_lists():
    return (api_nav() + webhooks() + scopes() + settings() + plan_features() + embedded_providers() + legal()
            + app_categories() + product_lines() + contracting_entities() + subprocessors())
