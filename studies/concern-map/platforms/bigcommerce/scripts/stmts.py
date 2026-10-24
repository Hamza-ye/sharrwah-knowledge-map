# Statements: BigCommerce's own words, verbatim, placed under the placement whose question they answer.
# Each statement becomes one citation (its quote is the statement) unless the same quote is already cited.
import csv, os, re
from bcsrc import F
from firstline import first as first_sentence

ST = []  # dicts: c, pl, key, loc, structure, ident, text, scope, note


def S(c, pl, key, loc, structure, ident, text, scope="", note=""):
    ST.append(dict(c=c, pl=pl, key=key, loc=loc, structure=structure, ident=ident, text=text, scope=scope, note=note))


# ---------- generated statements ----------
_acc = open(os.path.join(F, "docs/overview_api-fundamentals_api-accounts.md"), encoding="utf-8").read().splitlines()


def scope_row(c, param):
    for l in _acc:
        cells = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[2] == f"`{param}`":
            S(c, "boundary", "d:overview/api-fundamentals/api-accounts", "## OAuth scopes", "Developer docs: API Accounts, OAuth scopes table",
              param, " | ".join(cells[:4]))
            return
    raise KeyError(param)


_hooks = {}
with open(os.path.join(F, "webhook-events.tsv"), encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        _hooks.setdefault(r["scope"], r)
_PAGEKEY = {"integrations_webhooks_event-reference_events.md": ("d:integrations/webhooks/event-reference/events", "Developer docs: Webhook Events"),
            "integrations_webhooks_event-reference_channel-events.md": ("d:integrations/webhooks/event-reference/channel-events", "Developer docs: Channel Webhooks"),
            "integrations_webhooks_event-reference_inventory-and-location-events.md": ("d:integrations/webhooks/event-reference/inventory-and-location-events", "Developer docs: Inventory and location events"),
            "integrations_webhooks_event-reference_b2b-edition.md": ("d:integrations/webhooks/event-reference/b2b-edition", "Developer docs: B2B Edition Webhooks")}


def plain(s):
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return re.sub(r"\s+", " ", s.replace("**", "").replace("`", "").replace("\\", "")).strip()


def hook(c, topic, maxlen=260):
    r = _hooks[topic]
    key, structure = _PAGEKEY[r["page"]]
    d = plain(r["description"])
    if len(d) > maxlen:
        cut = d[:maxlen]
        i = cut.rfind(". ")
        d = cut[:i + 1] if i > 30 else cut
    import bcsrc
    text = f"{topic} | {d}"
    if not bcsrc.found(text, key).startswith("found"):
        text = f"{topic}* | {d}"  # topics marked with an asterisk support data filtering on the metafield namespace
    S(c, "boundary", key, f"## {r['section']}", structure, topic, text)


_set = open(os.path.join(F, "apiref/rest_admin_management_settings.md"), encoding="utf-8").read().splitlines()


def setting(c, name):
    for l in _set:
        cells = [plain(x) for x in l.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] == name:
            S(c, "decides", "a:rest/admin/management/settings", "## Available settings and configuration",
              "API reference: Settings V3", f"Settings V3: {name}", f"{cells[0]} | {cells[1]}",
              note="A settings resource the store's settings expose through the API.")
            return
    raise KeyError(name)


def group(c, path, maxlen=300, text=None, scope=""):
    key = "a:" + path
    t = text or first_sentence(key, maxlen)
    h1 = os.path.basename(path)
    S(c, "where", key, "page introduction", f"API reference group: /developer/api-reference/{path}", f"/developer/api-reference/{path}", t, scope)


PLAN_SCOPE = "plans Core, Growth, Scale, Performance (columns of the plan comparison table)"


def plan(c, feature, text, note=""):
    S(c, "decides", "w:pricing/", "Compare plans table (raw HTML)", "Pricing page: plan comparison", feature, text, PLAN_SCOPE, note)


ICONS = "Per-plan cells for this line are images with alt text \"blue-checkmark\""

# ---------- where: API reference groups ----------
group(1, "rest/admin/catalog/products", text="The Catalog API manages products, categories, brands, bulk pricing rules, and more.")
group(2, "rest/admin/catalog/brands", text="Our Catalog brands endpoints let you create individual brands and modify the brands associated with a storeʼs products")
group(3, "rest/admin/catalog/categories", text="The Catalog API manages products, categories, brands, bulk pricing rules, and more.")
group(3, "rest/admin/catalog/category-trees", text="Our Catalog category trees and their categories endpoints are the more modern and performant counterparts to the categories (deprecated) endpoints.")
group(4, "rest/admin/management/inventory")
group(6, "rest/admin/management/pickup")
group(6, "rest/admin/management/pickup/pickup-methods")
group(7, "rest/admin/management/price-lists")
group(8, "rest/admin/management/pricing")
group(9, "rest/admin/management/promotions")
group(9, "rest/admin/management/promotion-settings")
group(10, "rest/admin/content/marketing")
group(14, "rest/admin/management/carts")
group(14, "rest/storefront/carts")
group(15, "rest/admin/management/abandoned-carts")
group(15, "rest/admin/content/abandoned-cart-emails", text="Abandoned Cart Emails V3 API managing Handlebars-based emails.")
group(16, "rest/admin/management/checkouts", text="Create and manage checkouts from existing carts using BigCommerce checkout logic.")
group(16, "rest/storefront/checkouts")
group(18, "rest/admin/management/orders")
group(18, "rest/admin/management/order-operations")
group(20, "rest/admin/payments/transactions")
group(22, "rest/admin/payments")
group(23, "rest/admin/payments/methods", text="Retrieve the payment methods a store accepts.")
group(24, "rest/admin/payments/stored-instruments")
group(31, "rest/b2b/management/invoice-management")
group(31, "rest/b2b/management/payment", maxlen=230)
group(32, "rest/admin/management/customers/v3")
group(32, "rest/storefront/customers")
group(33, "rest/admin/authentication-apis/customer-login-api/overview")
group(33, "rest/admin/authentication-apis/current-customer/overview")
group(34, "rest/admin/management/customer-segmentation")
group(35, "rest/admin/management/subscribers")
group(36, "rest/admin/management/wishlists")
group(37, "rest/storefront/consent")
group(38, "rest/admin/management/channels")
group(40, "rest/admin/management/sites")
group(41, "rest/admin/management/redirects", maxlen=90)
group(42, "rest/admin/content/themes")
group(42, "rest/admin/content/custom-template-associations")
group(43, "rest/admin/content/widgets")
group(43, "rest/admin/content/page-widgets")
group(44, "rest/admin/management/scripts", text="Add client-side code to a BigCommerce storefront page or associate a script with a channel.")
group(45, "rest/admin/content/pages")
group(45, "rest/admin/content/store-content")
group(46, "rest/admin/content/email-templates", text="Manage Handlebars-based email templates globally and create channel-specific overrides.")
group(47, "rest/admin/management/settings")
group(47, "rest/admin/management/store-information/v2")
group(49, "rest/admin/management/store-information/v3")
group(52, "rest/admin/management/infrastructure-hosting")
group(53, "rest/admin/authentication-apis/storefront-api-tokens/overview")
group(55, "graphql/account/overview")
group(58, "rest/integrations/webhooks", text="Get notified when specific events occur on a BigCommerce store.")
group(60, "rest/admin/management/system-logs")
group(63, "mcp/overview")
group(65, "rest/b2b/overview", text="REST APIs for B2B Edition — BigCommerce's add-on for business-to-business commerce.")
group(65, "rest/b2b/management/overview", text="The B2B Edition Management APIs let you perform server-to-server operations for managing B2B storefronts.")
group(70, "rest/admin/management/shipping")
group(71, "rest/integrations/shipping-provider", maxlen=90)
group(72, "rest/admin/management/tax")
group(73, "rest/integrations/tax-provider", maxlen=170)
group(74, "rest/admin/management/currencies")
group(75, "rest/admin/management/geography")

# ---------- boundary: OAuth scopes ----------
for c, p in [(1, "store_v2_products"), (2, "store_v2_products"), (3, "store_v2_products"), (4, "store_inventory"), (5, "store_locations"),
             (6, "store_fulfillment_methods_manage"), (10, "store_v2_marketing"), (14, "store_cart"), (16, "store_checkout"),
             (16, "store_content_checkout"), (18, "store_v2_orders"), (19, "store_order_fulfillment_manage"), (20, "store_v2_transactions"),
             (22, "store_payments_access_token_create"), (23, "store_payments_methods_read"), (24, "store_stored_payment_instruments"),
             (29, "account_checkouts_create"), (32, "store_v2_customers"), (33, "store_v2_customers_login"), (38, "store_channel_settings"),
             (38, "store_channel_listings"), (40, "store_sites"), (42, "store_themes_manage"), (45, "store_v2_content"),
             (47, "store_v2_information"), (48, "store_translations"), (49, "store_metafield_write"), (49, "store_metafield_write_all"),
             (53, "store_storefront_api"), (55, "account_read"), (59, "store_app_extensions_manage"), (61, "account_users_write"),
             (65, "store_b2b_manage"), (31, "store_b2b_manage")]:
    scope_row(c, p)

# ---------- boundary: webhook topics ----------
for c, t in [(1, "store/product/created"), (2, "store/brand/metafield/created"), (3, "store/category/created"), (4, "store/channel/*/inventory/product/stock_changed"),
             (5, "store/inventory/location/created"), (7, "store/priceList/created"), (11, "store/channel/{channel_id}/settings/search/updated"),
             (14, "store/cart/created"), (15, "store/cart/abandoned"), (16, "store/channel/{channel_id}/settings/checkout/updated"),
             (18, "store/order/created"), (18, "store/order/statusUpdated"), (19, "store/shipment/created"), (20, "store/order/transaction/created"),
             (21, "store/order/refund/created"), (24, "store/customer/payment/instrument/default/updated"), (32, "store/customer/created"),
             (33, "store/customer/channel/login/access/updated"), (35, "store/subscriber/created"), (38, "store/channel/created"),
             (40, "store/channel/{channel_id}/settings/site/updated"), (41, "store/redirects/updated"), (42, "store/channel/{channel_id}/theme/configuration/activated"),
             (44, "store/channel/{channel_id}/script/created"), (45, "store/channel/{channel_id}/page/created"),
             (46, "store/channel/{channel_id}/email/templates/updated"), (47, "store/information/updated"),
             (48, "store/channel/{channel_id}/settings/locale/added"), (49, "store/metafield/created"), (58, "store/hook/deliveryException"),
             (59, "store/app/uninstalled"), (65, "store/company/created"), (74, "store/channel/{channel_id}/settings/currency/updated"),
             (78, "store/channel/{channel_id}/settings/security/updated")]:
    hook(c, t)

# ---------- decides: settings resources ----------
for c, n in [(1, "Catalog"), (1, "Storefront Product"), (3, "Storefront Category"), (4, "Inventory"), (4, "Inventory Notifications"),
             (11, "Search Filters"), (11, "Storefront Search"), (46, "Email Statuses"), (47, "Store Profile"), (47, "Storefront Status"),
             (47, "Storefront SEO"), (48, "Store Locale"), (62, "Analytics"), (78, "Storefront Security")]:
    setting(c, n)

# ---------- decides: plan lines (pricing page, raw HTML) ----------
plan(1, "Products, file storage, and bandwidth", "Products, file storage, and bandwidth", ICONS + " in all four plan columns.")
plan(5, "Inventory locations", "Up to 4 Up to 5 Up to 8 Custom", "The cells of the Inventory locations line, in plan order Core, Growth, Scale, Performance.")
plan(7, "Price Lists", "Give B2B customers a B2C-level experience with custom pricing at the SKU level for customer groups.",
     "Tooltip of the Price Lists line. Its cells read — (Core), — (Growth), — (Scale), and an image with alt text \"blue-checkmark\" (Performance). Inference: the line is included only on Performance.")
plan(9, "Advanced promotions management", "Advanced promotions management",
     "Cells read — (Core), — (Growth), — (Scale), and an image with alt text \"blue-checkmark\" (Performance). Inference: included only on Performance.")
plan(10, "Coupons, discounts, and gift cards", "With more than 70 discount options available out-of-the-box, BigCommerce offers advanced but user-friendly promotions tools",
     "Tooltip of the line Coupons, discounts, and gift cards. " + ICONS + " in all four plan columns.")
plan(11, "Product filtering", "Improve the shopping experience by enabling shoppers to easily and dynamically filter products.",
     "Tooltip of the Product filtering line. Cells read — (Core), — (Growth), then check images (Scale, Performance). Inference: included from Scale up.")
plan(12, "Product ratings and reviews", "Product ratings and reviews", ICONS + " in all four plan columns. Google customer reviews reads —, —, then check images on Scale and Performance.")
plan(14, "Persistent cart", "Improve your customer's experience by saving their shopping cart to their account, so when they switch devices, their cart is still there.",
     "Tooltip of the Persistent cart line. Cells read — (Core), then check images (Growth, Scale, Performance).")
plan(15, "Abandoned cart saver", "This conversion tool automatically sends shoppers a customizable series of emails, which motivates them to complete their purchase.",
     "Tooltip of the Abandoned cart saver line. Cells read — (Core), then check images (Growth, Scale, Performance).")
plan(16, "Single-page checkout", "Single-page checkout", ICONS + " in all four plan columns.")
plan(24, "Stored credit cards", "Returning customers are sent to the payment step with their billing and shipping automatically filled to save time at checkout.",
     "Tooltip of the Stored credit cards line. Cells read — (Core), then check images (Growth, Scale, Performance).")
plan(26, "Open Payment Provider Fee", "2.0% 1.0% 0.6% 0.0% with contract*", "Cells of the Open Payment Provider Fee line, in plan order Core, Growth, Scale, Performance.")
plan(26, "Orders through Embedded Payment Providers", "$0 fee $0 fee $0 fee $0 fee", "Cells of the line Orders through Embedded Payment Providers, in plan order Core, Growth, Scale, Performance.")
plan(27, "Apple Pay, Google Pay, and Amazon Pay", "Apple Pay, Google Pay, and Amazon Pay", ICONS + " in all four plan columns.")
plan(30, "GMV cap", "Up to $30K TTM Up to $100K TTM $33,333/mo* Custom", "Cells of the GMV cap line, in plan order Core, Growth, Scale, Performance.")
plan(34, "Customer groups and segmentation", "Segment your customers for pricing, product access, and promotions to create differentiated experiences on your website.",
     "Tooltip of the line. Cells read — (Core), then check images (Growth, Scale, Performance).")
plan(38, "Online storefront", "Online storefront", ICONS + " in all four plan columns.")
plan(39, "Multi-storefront", "Add storefront $30/mo (max. 3) Add storefront $50/mo (max. 5) Add storefront $100/mo (max. 8) Contact Sales",
     "Cells of the Multi-storefront line, in plan order Core, Growth, Scale, Performance.")
plan(45, "Built-in blog", "Help improve your SEO rankings and deliver a content-rich experience to your shoppers with a blog.", "Tooltip of the Built-in blog line. " + ICONS + " in all four plan columns.")
plan(61, "Staff accounts", "Staff accounts", ICONS + " in all four plan columns.")
plan(62, "Professional reporting tools", "Professional reporting tools", ICONS + " in all four plan columns.")
plan(67, "Google / Meta / TikTok / Microsoft / Pinterest (Feedonomics Surface)", "Feedonomics Surface connects your store to ad channels and keeps product listings accurate as your catalog changes. The basic plan is free for up to 100,000 SKUs.")
plan(68, "Amazon / eBay / Walmart", "Connect your store to the world’s largest marketplaces to reach millions of new shoppers while managing all your orders from BigCommerce.",
     "Tooltip of the Amazon / eBay / Walmart line. " + ICONS + " in all four plan columns.")
plan(69, "Point of sale", "Connect your offline and online business with POS integrations to Square, Vend, Clover, Heartland Retail, and more.",
     "Tooltip of the Point of sale line. " + ICONS + " in all four plan columns.")
plan(70, "Real-time shipping quotes", "Give shoppers the most accurate shipping pricing available with real-time rates from UPS, USPS, FedEx, Australia Post, Royal Mail, Canada Post, and more.",
     "Tooltip of the Real-time shipping quotes line. " + ICONS + " in all four plan columns. The ShipperHQ shipping rules engine line reads Available, Available, Available, then a check image.")
plan(74, "Multi-currency", "Accept payments in over 100+ currencies and offering local payment methods through the provider of your choice.",
     "Tooltip of the Multi-currency line. " + ICONS + " in all four plan columns.")
plan(77, "BigCommerce mobile app", "BigCommerce mobile app", ICONS + " in all four plan columns.")
plan(78, "Free sitewide HTTPS and dedicated SSL", "All traffic to your site is over HTTPs and comes with a free dedicated SSL",
     "Tooltip of the line. " + ICONS + " in all four plan columns.")

from stmts_hand import hand, hand2, hand3, hand4  # noqa: E402
hand(S)
hand2(S)
hand3(S)
hand4(S)
