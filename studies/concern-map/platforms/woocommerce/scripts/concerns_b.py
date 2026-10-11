# Concerns B: partners and services around the store, and the core commerce concerns.
import re
from spec import C, S, N, I
from concerns_a import E, ST, NAV, API, EXT, WPT, MKT, LEG, PES, TOSL, PPF, CORE_LEGAL, CORE_LEGAL_NOTE

WH, AS, EM, OS_, FT = "^webhook-topics$", "^access-scopes$", "^other:emails$", "^other:order-statuses$", "^other:features$"
OT, SH, SPS = "^other:onboarding-tasks$", "^other:core-shipping-methods$", "^other:shipping-partner-suggestions$"
FEAT_DECIDES_NOTE = "A setting on the Features section of Settings > Advanced."

# ---------------- partners and services around the store ----------------
C("WC-C-059", "Third-party extensions and services (general)", "Third-Party Services; extensions",
  "Split from Woo-made extensions (WC-C-050) and from Marketplace sales (WC-C-017).",
  match=[(MKT, E("Extensions"))],
  software=S("extension point", ["tos_ext_gpl", "tos_ext_own_terms", "readme_hooks", "va_gpl"]),
  decides=S("merchant", ["tos_3p_enable"]),
  legal=S("app developer", ["tos_3p_not_vetted", "tos_3p_risk"], "Sources differ in emphasis: the Terms say Third-Party Services are not vetted, endorsed or controlled by Automattic, while the readme says Woo developers vet each new Marketplace extension. Both recorded."),
  boundary=S("WordPress plugin hooks and filters; each extension's own terms and servers", ["readme_hooks", "tos_ext_own_terms", "readme_vet", "mkt_country_filter"], "The Marketplace offers a Country filter on extensions."),
  reason=N())

C("WC-C-060", "WooCommerce Shipping (labels and carrier rates)", "WooCommerce Shipping",
  "Split from third-party carriers (WC-C-061) and from core shipping (WC-C-075).",
  match=[(SPS, E("WooCommerce Shipping")), (TOSL, E("WooCommerce Shipping")), (PPF, E("Configure your shipping options"))],
  software=S("separate service or product line", ["doc_wcs_labels", "privship_wcs_jetpack", "doc_wcs_norates"]),
  decides=S("operator, per market or plan", ["doc_wcs_us", "readme_wcs_us_only", "readme_wcs_us"], "Available to stores based in the United States that use U.S. dollars."),
  legal=S("partner", ["tos_ship_intermediary", "tos_ship_carriers", "jp_easypost"], "Automattic is only an intermediary; data passes through Automattic's servers to EasyPost and the mailing services."),
  boundary=S("Jetpack connection; labels bought in the order admin; Automattic validates but does not store the data it passes on", ["privship_wcs_jetpack", "doc_wcs_labels", "jp_validate_not_store"]),
  reason=N())

C("WC-C-061", "Third-party shipping carriers and shipping extensions", "Shipping, delivery and fulfillment; shipping partner suggestions",
  "", match=[(SPS, r"^(ShipStation|Skydropx|Envia|Easyship|Packlink)$"), (MKT, r"^Extensions > Shipping, delivery and fulfillment"), (API, r"^wc-admin > shipping-partner-suggestions"),
             (PPF, E("Configure your shipping options"))],
  software=S("extension point", ["dev_ship_api", I(MKT, E("Extensions > Shipping, delivery and fulfillment"))]),
  decides=S("merchant", ["tos_third_party_pay"], "The Terms give EasyPost as an example of a third-party shipping service the merchant may decide to use."),
  legal=S("partner", ["privship_shared", "tos_3p_not_vetted"]),
  boundary=S("Shipping Method API (WC_Shipping_Method and the woocommerce_shipping_methods filter)", ["dev_ship_api", I(EXT, r"^WC_Shipping_Method")]),
  reason=N())

C("WC-C-062", "Support for Woo and Marketplace products", "WooCommerce Support Policy",
  "", match=[(LEG, E("WooCommerce Support Policy"))],
  software=S("separate service or product line", ["legal_support_policy"]),
  decides=S("platform at build", ["legal_support_policy"]),
  legal=S("separate entity of the platform", ["legal_support_policy", "va_support"], "Products sold on WooCommerce.com are supported through WooCommerce's helpdesk; vendors answer through WooCommerce's support system."),
  boundary=S("WooCommerce.com helpdesk", ["va_support"]),
  reason=N())

C("WC-C-063", "WooCommerce.com connection, extension installs and Marketplace subscriptions", "WooCommerce.com; Extensions; Connection to WooCommerce.com",
  "", match=[(ST, E("Advanced > WooCommerce.com")), (API, r"^wccom-site/v3( > |$)"), (NAV, E("WooCommerce > Extensions")),
             (PPF, E("Connection to WooCommerce.com")), (FT, E("Marketplace")), (OT, r"^(Enhance your store with extensions|Discover ways of extending)")],
  software=S("separate service or product line", ["readme_wccom_connect", "doc_connect", I(API, E("wccom-site/v3")), "code_feat_marketplace"]),
  decides=S("merchant", ["doc_connect"]),
  legal=S("separate entity of the platform", ["tos_woo_services", "privmkt_sites", "privmkt_not_shared"], "WooCommerce.com is a Woo service; it learns which sites use each subscription but generally not customer data."),
  boundary=S("wccom-site/v3 REST endpoints (connection, installer, ssr, status)", [I(API, r"^wccom-site/v3 > ")]),
  reason=N())

# ---------------- catalogue ----------------
PROD_API = r"^wc/v3 > (product-attribute-terms|product-attributes|product-categories|product-custom-fields|product-tags|products|product-variations|variations)$"
C("WC-C-064", "Products and catalogue structure (types, variations, attributes, categories, tags, brands)", "Products; Product variations; Attributes; Categories; Tags; Brands",
  "Split from reviews (WC-C-065), downloads (WC-C-066), import/export (WC-C-067) and stock (WC-C-068).",
  match=[(ST, r"^Products( > General)?$"), (NAV, r"^Products( > (All Products|Add New|Categories|Tags|Brands|Attributes))?$"), (API, PROD_API),
         (API, r"^wc/v4 > (products|settings-products)$"), (API, r"^wc/store/v1 > /products(?!/reviews)"), (API, r"^Product (variations|attributes|attribute terms|categories|custom fields|tags)$"),
         (API, E("Products")), (WH, r"^product\."), (AS, E("product, shop_order, shop_coupon")), (FT, r"^(Product gallery videos|Variation gallery|Color swatches for attributes|Cache Product Objects)$"),
         (PPF, r"^(Customize product pages in minutes|Showcase physical and digital goods)$"), (API, r"^wc-analytics > (Products|ProductVariations|ProductCategories|ProductAttributes|ProductAttributeTerms)$")],
  software=S("core", [I(ST, E("Products")), I(API, E("wc/v3 > products")), "doc_install_items"]),
  decides=S("merchant", [I(NAV, E("Products > Add New"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 products and related routes; Store API /products; webhook topics product.*", [I(API, E("wc/v3 > products")), I(API, E("wc/store/v1 > /products")), I(WH, E("product.created"))]),
  reason=N())

C("WC-C-065", "Product reviews and review requests", "Reviews; Product reviews; Review request",
  "", match=[(NAV, E("Products > Reviews")), (API, r"product-reviews$"), (API, E("wc/store/v1 > /products/reviews")), (API, E("Product reviews")),
             (EM, r"^Review request"), (FT, r"^Customer review request")],
  software=S("core", [I(NAV, E("Products > Reviews")), I(API, E("wc/v3 > product-reviews"))]),
  decides=S("buyer", ["code_reviews_verified"], "Buyers write reviews; the merchant sets who may review and moderates them."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 products/reviews; Store API /products/reviews", [I(API, E("wc/v3 > product-reviews")), I(API, E("wc/store/v1 > /products/reviews"))]),
  reason=N())

C("WC-C-066", "Downloadable products and customer downloads", "Downloadable products; Downloads",
  "", match=[(ST, E("Products > Downloadable products")), (API, E("wc/v3 > customer-downloads")), (NAV, E("Analytics > Downloads")),
             (API, r"^wc-analytics > (reports/downloads|data/download-ips)"), ("^other:privacy-exporters-erasers$", r"Downloads")],
  software=S("core", [I(ST, E("Products > Downloadable products"))]),
  decides=S("merchant", [I(ST, E("Products > Downloadable products"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 customers/{id}/downloads", [I(API, E("wc/v3 > customer-downloads"))]),
  reason=N())

C("WC-C-067", "Product import and export (CSV)", "Product Import; Product Export; Import your products",
  "", match=[(NAV, r"^Products > Product (Import|Export)$"), (OT, E("Import your products"))],
  software=S("core", [I(NAV, E("Products > Product Import")), I(NAV, E("Products > Product Export"))]),
  decides=S("merchant", [I(NAV, E("Products > Product Import"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=N(),
  reason=N())

C("WC-C-068", "Inventory and stock levels", "Inventory; Stock",
  "", match=[(ST, E("Products > Inventory")), (NAV, E("Analytics > Stock")), (API, r"^wc-analytics > (reports/stock|ProductsLowInStock)")],
  software=S("core", [I(ST, E("Products > Inventory"))]),
  decides=S("merchant", [I(ST, E("Products > Inventory"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("stock fields on products through the products REST routes", [I(API, E("wc/v3 > products"))]),
  reason=N())

C("WC-C-069", "Back-in-stock notifications", "Back in Stock Notifications; Stock Notifications",
  "", match=[(NAV, E("WooCommerce > Notifications")), (FT, E("Back in Stock Notifications"))],
  software=S("core", [I(FT, E("Back in Stock Notifications")), I(NAV, E("WooCommerce > Notifications"))]),
  decides=S("merchant", [I(FT, E("Back in Stock Notifications"))], FEAT_DECIDES_NOTE),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=N(),
  reason=N())

# ---------------- orders, refunds, checkout, customers ----------------
C("WC-C-070", "Orders and order statuses", "Orders; Order statuses; Order notes",
  "Split from refunds (WC-C-071), fulfillments (WC-C-092) and withdrawal requests (WC-C-091).",
  match=[(NAV, E("WooCommerce > Orders")), (API, r"^wc/v3 > (orders|order-notes|network-orders)$"), (API, r"^wc/v4 > (orders|order-notes)$"),
         (API, r"^wc/store/v1 > /order/"), (API, r"^(Orders|Order actions|Order notes)$"), (OS_, "."), (WH, r"^order\."),
         (API, E("wc-analytics > Orders"))],
  software=S("core", [I(NAV, E("WooCommerce > Orders")), I(API, E("wc/v3 > orders"))]),
  decides=S("platform at build", [I(OS_, E("Pending payment")), "doc_order_status"], "The status list is defined in core (wc_get_order_statuses); the merchant moves orders between statuses."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 orders; webhook topics order.*; Store API /order", [I(API, E("wc/v3 > orders")), I(WH, E("order.created")), I(API, r"^wc/store/v1 > /order/")]),
  reason=N())

C("WC-C-071", "Refunds", "Refunds; Order refunds; Refunded",
  "Split from orders (WC-C-070); the money movement belongs to the gateway (WC-C-001).",
  match=[(API, r"^wc/v3 > (order-refunds|refunds)$"), (API, E("wc/v4 > refunds")), (API, r"^(Order refunds|Refunds)$"),
         (EM, r"(Refunded order|Partially refunded order)"), (OS_, E("Refunded"))],
  software=S("core", [I(API, E("wc/v3 > order-refunds")), I(OS_, E("Refunded"))]),
  decides=S("merchant", [I(API, E("wc/v3 > order-refunds"))]),
  legal=S("merchant", ["tos_ecom_disputes"]),
  boundary=S("REST wc/v3 orders/{id}/refunds and refunds", [I(API, E("wc/v3 > order-refunds")), I(API, E("wc/v3 > refunds"))]),
  reason=N())

C("WC-C-072", "Cart and checkout", "Cart; Checkout; Cart & Checkout Blocks; Page setup",
  "Split from checkout extensibility (WC-C-087) and the Store API as a whole (WC-C-079).",
  match=[(API, r"^wc/store/v1 > /(cart|checkout)(?!/coupons|/apply-coupon|/remove-coupon|/extensions|/select-shipping-rate|/update-customer)"),
         (FT, r"^(Cart & Checkout Blocks|Clear Customer Sessions When Empty)$"), (ST, E("Advanced > Page setup")), (OS_, r"^Draft"), (PPF, E("Increase revenue"))],
  software=S("core", [I(FT, E("Cart & Checkout Blocks")), I(API, E("wc/store/v1 > /checkout"))]),
  decides=S("merchant", [I(ST, E("Advanced > Page setup")), "code_guest_checkout"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("Store API /cart and /checkout routes", [I(API, E("wc/store/v1 > /cart")), I(API, E("wc/store/v1 > /checkout"))]),
  reason=N())

C("WC-C-073", "Customer accounts", "Customers; Customer; Accounts & Privacy",
  "", match=[(NAV, E("WooCommerce > Customers")), (API, E("wc/v3 > customers")), (API, r"^wc/v4 > (customers|settings-account)$"), (API, E("Customers")),
             (WH, r"^customer\."), (AS, r"^(customer|create_customers)$"), (EM, r"^(New account|Reset password)"), (ST, E("Accounts & Privacy")),
             (API, E("wc/store/v1 > /cart/update-customer")), (API, r"^wc-analytics > (customers|reports/customers)")],
  software=S("core", [I(API, E("wc/v3 > customers")), "doc_roles"]),
  decides=S("merchant", ["doc_accounts_privacy", "code_guest_checkout"], "The merchant sets guest checkout and account creation."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 customers; webhook topics customer.*", [I(API, E("wc/v3 > customers")), I(WH, E("customer.created"))]),
  reason=N())

C("WC-C-074", "Coupons and discounts", "Coupons",
  "", match=[(NAV, r"Coupons"), (API, E("wc/v3 > coupons")), (API, E("Coupons")), (WH, r"^coupon\."), (NAV, E("Analytics > Coupons")),
             (API, r"^wc/store/v1 > /cart/(coupons|apply-coupon|remove-coupon)"), (API, r"^wc-analytics > (reports/coupons|Coupons$)")],
  software=S("core", [I(API, E("wc/v3 > coupons")), I(NAV, E("Marketing > Coupons"))]),
  decides=S("merchant", [I(NAV, E("Marketing > Coupons"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 coupons; webhook topics coupon.*; Store API cart coupon routes", [I(API, E("wc/v3 > coupons")), I(WH, E("coupon.created")), I(API, E("wc/store/v1 > /cart/apply-coupon"))]),
  reason=N())

C("WC-C-075", "Shipping zones, methods and classes (core)", "Shipping zones; Shipping settings; Classes; Flat rate; Free shipping; Local pickup",
  "Split from WooCommerce Shipping (WC-C-060), carriers (WC-C-061) and fulfillments (WC-C-092).",
  match=[(ST, r"^Shipping( > (Shipping zones|Shipping settings|Classes))?$"), (SH, "."), (EXT, r"^(WC_Shipping_Method|woocommerce_shipping_methods)"),
         (API, r"^wc/v3 > (shipping-zones|shipping-zone-locations|shipping-zone-methods|shipping-methods|product-shipping-classes)$"),
         (API, r"^wc/v4 > (shipping-zones|shipping-zone-method)$"), (API, r"^(Shipping zones|Shipping zone locations|Shipping zone methods|Shipping methods|Product shipping classes)$"),
         (API, E("wc/store/v1 > /cart/select-shipping-rate")), (OT, r"^(Select your shipping options|Review shipping options|Get your products shipped)$")],
  software=S("core", [I(ST, E("Shipping")), I(SH, E("Flat rate (flat_rate)"))]),
  decides=S("merchant", [I(ST, E("Shipping > Shipping zones"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("Shipping Method API; REST wc/v3 shipping zones and methods; store address as origin", ["dev_ship_api", I(API, E("wc/v3 > shipping-zones")), "code_store_address"]),
  reason=N())

C("WC-C-076", "Transactional emails", "Emails; Email options",
  "", match=[(ST, r"^Emails"), (EM, "."), (EXT, r"^woocommerce_email_classes"), (FT, r"^(Deferred emails|Email improvements|Block Email Editor)"), (API, r"^wc/v4 > settings-emails?$")],
  software=S("core", [I(ST, E("Emails")), I(EXT, r"^woocommerce_email_classes")]),
  decides=S("merchant", [I(ST, E("Emails > Email options"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("WC_Email classes registered through the woocommerce_email_classes filter", [I(EXT, r"^woocommerce_email_classes")]),
  reason=N())

# ---------------- integration surfaces ----------------
C("WC-C-077", "Webhooks", "Webhooks; webhook topics",
  "", match=[(WH, "."), (ST, E("Advanced > Webhooks")), (API, E("wc/v3 > webhooks")), (API, E("Webhooks")), (EXT, r"^woocommerce_webhook_topics")],
  software=S("core", [I(ST, E("Advanced > Webhooks")), "doc_webhooks"]),
  decides=S("merchant", ["doc_webhooks"], "The merchant chooses topics and the delivery URL."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("HTTP POST to the merchant's URL with topic and signature headers", ["code_webhook_signature", I(WH, E("order.created"))]),
  reason=S("other: \"Webhooks are useful for integrating your store with third-party services or other external APIs that support them.\"", ["doc_webhooks_why"]))

C("WC-C-078", "REST API, API keys and settings API", "WooCommerce REST API; REST API keys; Legacy API",
  "Split from the public Store API (WC-C-079).",
  match=[(API, r"^wc/v[1-4]$"), (ST, r"^Advanced( > (REST API keys|REST API caching|Legacy API))?$"), (AS, r"^(Read|Write|Read/Write)$"),
         (API, r"^(Introduction|Authentication|Index|Settings|Setting options)$"), (API, r"^wc/v3 > (settings|settings-options)$"),
         (API, r"^wc/v4 > (settings|settings-general)$"), (FT, E("REST API Caching")), (EXT, r"^woocommerce_rest_api_get_rest_namespaces")],
  software=S("core", [I(API, E("wc/v3")), "doc_rest"]),
  decides=S("merchant", ["doc_rest_keys", I(AS, E("Read/Write"))], "The merchant generates keys with read, write or read/write permission."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST namespaces wc/v1 to wc/v3 (wc/v4 behind a feature flag); consumer key authentication", [I(API, r"^wc/v[1-4]$"), "dev_rest_auth"]),
  reason=N())

C("WC-C-079", "Store API (public storefront API)", "Store API",
  "", match=[(API, E("wc/store/v1")), (API, r"^wc/store/v1 > "), (EXT, ".", r"^apis/store-api/extending-store-api/")],
  software=S("core", ["dev_store_api", "code_store_api_ns"]),
  decides=S("platform at build", ["dev_store_api_unauth"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("unauthenticated wc/store/v1 routes; extendable with ExtendSchema", ["dev_store_api_unauth", "dev_extend_store_api"]),
  reason=N())

C("WC-C-080", "Roles and capabilities", "Customer; Shop manager; manage_woocommerce",
  "", match=[(AS, r"^(customer|shop_manager|manage_woocommerce|create_customers|view_woocommerce_reports|product, shop_order, shop_coupon)$")],
  software=S("core", [I(AS, E("shop_manager")), "doc_roles"]),
  decides=S("merchant", ["doc_roles_assign"], "Roles are defined at build; the merchant assigns them."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("WordPress roles and capabilities", [I(AS, E("manage_woocommerce"))]),
  reason=N())

# ---------------- administration ----------------
C("WC-C-081", "Store administration: home, setup wizard, onboarding tasks and inbox", "Home; Setup Wizard; onboarding",
  "", match=[(NAV, r"^WooCommerce( > (Home|Settings))?$"), (NAV, r"^Setup Wizard"), (API, E("wc-admin")),
             (API, r"^wc-admin > (notice|features|experiments|options|plugins|onboarding)"), (API, r"^wc-analytics > (admin/notes|NoteActions)"),
             (OT, r"^(You created %s|You added store details)$")],
  software=S("core", [I(NAV, E("WooCommerce > Home")), I(NAV, r"^Setup Wizard")]),
  decides=S("merchant", [I(OT, E("You added store details"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("wc-admin REST namespace", [I(API, E("wc-admin"))]),
  reason=N())

C("WC-C-082", "Site visibility (coming soon and launch)", "Site visibility; Coming soon; Launch your store",
  "", match=[(ST, E("Site visibility")), (FT, E("Site visibility badge")), (OT, E("Launch your store")), (API, E("wc-admin > launch-your-store"))],
  software=S("core", [I(ST, E("Site visibility")), "doc_coming_soon"]),
  decides=S("merchant", ["doc_coming_soon"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=N(),
  reason=N())

C("WC-C-083", "Store status, tools and system report", "Status; System status; Tools",
  "", match=[(NAV, r"^(WooCommerce > Status|Status > (System status|Tools))$"), (API, r"^wc/v3 > system-status"), (API, r"^System status( tools)?$")],
  software=S("core", [I(NAV, E("WooCommerce > Status"))]),
  decides=S("merchant", [I(NAV, E("Status > Tools"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("REST wc/v3 system_status and system_status/tools", [I(API, E("wc/v3 > system-status"))]),
  reason=N())

C("WC-C-084", "Marketing hub (channels, campaigns, recommendations)", "Marketing; Overview",
  "Split from marketing extensions (WC-C-112).",
  match=[(NAV, r"^Marketing( > Overview)?$"), (API, r"^wc-admin > marketing"), (OT, E("Grow your business")), (PPF, r"^Grow your business")],
  software=S("core", [I(NAV, E("Marketing")), I(API, E("wc-admin > marketing (Marketing)"))]),
  decides=S("merchant", [I(NAV, E("Marketing > Overview"))]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("wc-admin marketing endpoints (channels, campaigns, recommendations)", [I(API, r"^wc-admin > marketing/")]),
  reason=N())

C("WC-C-085", "Order attribution", "Order Attribution",
  "", match=[(FT, E("Order Attribution"))],
  software=S("core", [I(FT, E("Order Attribution")), "doc_attribution"]),
  decides=S("merchant", ["code_feat_attribution"], FEAT_DECIDES_NOTE + " On by default."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=N(),
  reason=S("other: \"providing an understanding of the effectiveness of various marketing efforts\"", ["doc_attribution"]))

C("WC-C-086", "Extension framework (settings pages, integrations, admin pages, feature compatibility)", "Integration; Settings API; WC_Integration",
  "Split from checkout block extensibility (WC-C-087) and payment and shipping APIs (WC-C-001, WC-C-075).",
  match=[(EXT, r"^(WC_Integration|woocommerce_integrations|woocommerce_get_settings_pages|woocommerce_admin_rest_controllers|wc_admin_register_page|FeaturesUtil::declare_compatibility)"),
         (ST, E("Integration"))],
  software=S("extension point", [I(EXT, r"^WC_Integration"), "dev_integration"]),
  decides=S("merchant", ["tos_3p_enable"]),
  legal=S("app developer", ["tos_3p_not_vetted"]),
  boundary=S("WC_Integration class; woocommerce_get_settings_pages filter; wc_admin_register_page", [I(EXT, r"^WC_Integration"), I(EXT, r"^woocommerce_get_settings_pages"), I(EXT, r"^wc_admin_register_page")]),
  reason=N())

C("WC-C-087", "Block extensibility (cart, checkout and product blocks) and Store API extensions", "Cart and Checkout extensibility; Additional checkout fields; ExtendSchema; Product collection block",
  "", match=[(EXT, ".", r"^block-development/extensible-blocks/"), (EXT, ".", r"^apis/store-api/extending-store-api/"), (EXT, r"^(IntegrationInterface|AbstractPaymentMethodType|ExtendSchema|woocommerce_register_additional_checkout_field)"),
             (API, E("wc/store/v1 > /cart/extensions"))],
  software=S("extension point", ["dev_blocks_ext", I(EXT, r"^ExtendSchema")]),
  decides=S("merchant", ["tos_3p_enable"], "The merchant enables extensions. Inference: each extension's developer decides what it adds to cart and checkout."),
  legal=S("app developer", ["tos_3p_not_vetted"]),
  boundary=S("IntegrationInterface, ExtendSchema, payment method registration and the additional checkout fields API", [I(EXT, r"^IntegrationInterface"), I(EXT, r"^ExtendSchema"), I(EXT, r"^woocommerce_register_additional_checkout_field")]),
  reason=N())

C("WC-C-088", "Feature settings (opt-in and opt-out features)", "Features",
  "", match=[(FT, "."), (EXT, r"^FeaturesUtil::declare_compatibility")],
  software=S("core", [I(FT, E("High-Performance order storage")), I(EXT, r"^FeaturesUtil::declare_compatibility")]),
  decides=S("merchant", [I(FT, E("Order Attribution"))], "Each feature has a default set at build; the merchant can toggle those shown in the UI."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("FeaturesUtil::declare_compatibility for extensions", [I(EXT, r"^FeaturesUtil::declare_compatibility")]),
  reason=N())

C("WC-C-089", "Point of Sale in the mobile app", "Point of Sale; POS",
  "Split from WooPayments in-person payments (WC-C-014).",
  match=[(ST, E("Point of Sale")), (FT, r"^(Point of Sale|POS staff)$"), (EM, r"^POS "), (MKT, r"(Store management > Point of sale|Official payments > In-person payments)$")],
  software=S("separate service or product line", ["code_feat_pos", "doc_pos"], "POS mode lives in the WooCommerce mobile app; sales sync with the store."),
  decides=S("operator, per market or plan", ["doc_pos_country", "doc_pos_currency"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("mobile app syncing with the store", ["doc_pos_sync"]),
  reason=N())

C("WC-C-090", "Mobile app and push notifications", "WooCommerce mobile app; Push Notifications",
  "", match=[(OT, E("Get the free WooCommerce mobile app")), (API, r"^wc-admin > mobile-app"), (FT, E("Push Notifications")), (PPF, r"^Grow your business")],
  software=S("separate service or product line", ["code_feat_push", I(OT, E("Get the free WooCommerce mobile app"))]),
  decides=S("merchant", [I(OT, E("Get the free WooCommerce mobile app"))]),
  legal=N(),
  boundary=S("wc-admin mobile-app endpoints (magic link, QR login)", [I(API, r"^wc-admin > mobile-app")]),
  reason=N())

C("WC-C-091", "Order withdrawal requests", "Order withdrawal",
  "", match=[(FT, E("Order withdrawal")), (EM, r"withdrawal")],
  software=S("core", ["code_feat_withdrawal", I(EM, r"Order withdrawal request \(")]),
  decides=S("merchant", ["code_feat_withdrawal"], FEAT_DECIDES_NOTE),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("public order withdrawal request with emails to customer and store", [I(EM, r"withdrawal")]),
  reason=N("No source read gives the reason for the feature."))

C("WC-C-092", "Order fulfillments and shipping providers", "Order Fulfillments; Shipping providers",
  "", match=[(FT, E("Order Fulfillments")), (ST, E("Shipping > Shipping providers")), (API, E("wc/v4 > fulfillments")), (EM, r"^Fulfillment ")],
  software=S("core", ["code_feat_fulfillments", "doc_fulfillment"]),
  decides=S("merchant", ["doc_fulfillment"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("fulfillments API for shipping tools and providers", ["doc_fulfillment_api", I(API, E("wc/v4 > fulfillments"))]),
  reason=N())

C("WC-C-093", "Cost of goods sold", "Cost of Goods Sold",
  "", match=[(FT, E("Cost of Goods Sold"))],
  software=S("core", ["code_feat_cogs"]),
  decides=S("merchant", ["code_feat_cogs"], FEAT_DECIDES_NOTE),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=N(), reason=N())

C("WC-C-094", "Blueprint (export and import of store configuration)", "Blueprint (beta)",
  "", match=[(ST, E("Advanced > Blueprint (beta)")), (FT, E("Blueprint (beta)"))],
  software=S("core", [I(ST, E("Advanced > Blueprint (beta)"))]),
  decides=S("merchant", [I(FT, E("Blueprint (beta)"))], FEAT_DECIDES_NOTE),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=N(), reason=N())

C("WC-C-095", "WooCommerce MCP (AI assistant access to the store)", "WooCommerce MCP; Model Context Protocol",
  "", match=[(FT, E("WooCommerce MCP"))],
  software=S("core", ["dev_mcp", I(FT, E("WooCommerce MCP"))]),
  decides=S("merchant", [I(FT, E("WooCommerce MCP"))], FEAT_DECIDES_NOTE),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("Model Context Protocol tools exposing WooCommerce functions", ["dev_mcp"]),
  reason=N())

C("WC-C-096", "AI features offered by Automattic", "Artificial Intelligence; AI Guidelines",
  "", match=[(LEG, E("AI Guidelines"))],
  software=S("separate service or product line", ["tos_ai"]),
  decides=S("merchant", ["tos_ai_output"]),
  legal=S("merchant", ["tos_ai_output"], "The user is responsible for input and use of output."),
  boundary=S("Terms of Service section 8.k and the AI Guidelines", ["tos_ai", "legal_ai_guidelines"]),
  reason=N())

C("WC-C-097", "Shopper lists (wishlists, save for later)", "Wishlists; Save for Later in Cart; shopper-lists",
  "", match=[(FT, r"^(Wishlists|Save for Later in Cart)$"), (API, r"^wc/store/v1 > /shopper-lists")],
  software=S("core", [I(FT, E("Wishlists")), I(API, E("wc/store/v1 > /shopper-lists"))]),
  decides=S("merchant", [I(FT, E("Save for Later in Cart"))], FEAT_DECIDES_NOTE),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("Store API shopper-lists routes", [I(API, E("wc/store/v1 > /shopper-lists"))]),
  reason=N())

C("WC-C-098", "Saved payment methods (payment tokens)", "Payment Token API; WooCommerce Customer Payment Tokens",
  "Split from tokens held by WooPayments' partner (WC-C-042).",
  match=[(EXT, r"^WC_Payment_Token"), ("^other:privacy-exporters-erasers$", r"Payment Tokens")],
  software=S("core", ["dev_tokens", I(EXT, r"^WC_Payment_Token")]),
  decides=S("buyer", ["dev_tokens"], "Users manage tokens in their account and choose saved tokens at checkout."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("Payment Token API used by gateways", ["dev_tokens"]),
  reason=N())

C("WC-C-099", "Reference data (countries, continents)", "Data; data/countries; data/continents",
  "", match=[(API, r"^wc/v3 > (data|data-continents|data-countries)$"), (API, E("Data")), (API, E("wc-analytics > DataCountries"))],
  software=S("core", [I(API, E("wc/v3 > data-countries"))]),
  decides=N("Inference: the platform at build; the country lists ship with the release."),
  legal=N(),
  boundary=S("REST wc/v3 data endpoints", [I(API, E("wc/v3 > data"))]),
  reason=N())
