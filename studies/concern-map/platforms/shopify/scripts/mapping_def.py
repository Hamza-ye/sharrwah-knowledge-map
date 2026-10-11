# Mapping of inventory entries to concerns. Each function returns (set_of_concern_keys, out_of_scope_reason).
import re

CAPITAL = ["fin.capital_us", "fin.capital_uk", "fin.capital_ca", "fin.capital_au", "fin.capital_fr", "fin.capital_de", "fin.capital_mca_eu"]
OOS_HEADING = "group heading in the list; the items under it are placed individually"
OOS_TOOLING = "developer tooling for building apps (how code is written and shipped), not a commerce concern with a placement of its own"
OOS_UNSTATED = "admin route section whose function the captured route data does not state; no placement can be shown"

# ------------------------------------------------------------------ access scopes
SCOPE_STEMS = [
    (r"^all_orders$", ["ord.orders", "apps.restricted_scopes"]),
    (r"^analytics(_annotations)?$|^reports$", ["an.analytics"]),
    (r"^app_proxy$", ["apps.theme_app_ext"]),
    (r"^apps$", ["apps.apps", "apps.restricted_scopes"]),
    (r"^(assigned|merchant_managed|third_party)_fulfillment_orders$", ["shp.fulfillment", "shp.fulfillment_services"]),
    (r"^marketplace_fulfillment_orders$", ["shp.fulfillment", "chan.marketplaces", "apps.restricted_scopes"]),
    (r"^custom_fulfillment_services$|^fulfillments$", ["shp.fulfillment_services"]),
    (r"^audit_events$", ["acct.audit_log"]),
    (r"^(customer_events|pixels|custom_pixels|server_pixels)$", ["an.customer_events"]),
    (r"^(all_)?cart_transforms$", ["chk.cart_transform_fn"]),
    (r"^validations$", ["chk.validation_fn"]),
    (r"^cash_tracking$", ["pay.cash"]),
    (r"^(channels|publications)$", ["chan.sales_channels"]),
    (r"^checkout_kit_enhanced_buyer_events$", ["chk.checkout", "an.customer_events"]),
    (r"^checkout_and_accounts_configurations$", ["chk.checkout_branding"]),
    (r"^checkout_settings$", ["chk.checkout_branding", "apps.restricted_scopes"]),
    (r"^checkout_branding_settings$", ["chk.checkout_branding"]),
    (r"^checkouts$", ["chk.checkout", "chk.cart"]),
    (r"^companies$|^locations$(?#customer_ only)", None),  # resolved below
    (r"^customer_data_erasure$", ["priv.data_requests"]),
    (r"^customer_merge$|^customer_tags$|^customers$", ["cust.customers"]),
    (r"^delivery_customizations$", ["shp.delivery_customization_fn"]),
    (r"^(price_rules|discounts)$", ["mktg.discounts"]),
    (r"^discovery$", ["cat.search"]),
    (r"^draft_orders$", ["ord.draft_orders"]),
    (r"^files$", ["cat.files"]),
    (r"^fulfillment_constraint_rules$", ["shp.fulfillment_constraints_fn"]),
    (r"^gift_card(s|_transactions)$", ["cat.gift_cards"]),
    (r"^inventory$|^product_inventory$", ["cat.inventory"]),
    (r"^inventory_(shipments|shipments_received_items|transfers)$", ["cat.inventory_transfers"]),
    (r"^legal_policies$", ["cat.policies"]),
    (r"^(locales|translations)$", ["cat.translations"]),
    (r"^marketing_(events|integrated_campaigns)$", ["mktg.campaigns"]),
    (r"^marketplace_orders$", ["chan.marketplaces", "ord.orders", "apps.restricted_scopes"]),
    (r"^marketplace_returns$", ["chan.marketplaces", "ord.returns", "apps.restricted_scopes"]),
    (r"^markets(_home)?$", ["mkt.markets"]),
    (r"^merchant_approval_signals$", ["apps.restricted_scopes"]),
    (r"^(metaobject_definitions|metaobjects|metafields)$", ["cat.custom_data"]),
    (r"^mobile_platform_applications$", ["ext.mobile_app", "apps.restricted_scopes"]),
    (r"^online_store_navigation$", ["cat.navigation"]),
    (r"^(online_store_pages|content)$", ["cat.pages_blogs"]),
    (r"^order_edits$", ["ord.order_editing"]),
    (r"^orders$", ["ord.orders"]),
    (r"^own_subscription_contracts$|^subscription_contracts$", ["ext.subscriptions", "apps.restricted_scopes"]),
    (r"^purchase_options$|^selling_plans$", ["ext.subscriptions"]),
    (r"^payment_customizations$", ["pay.customization_fn"]),
    (r"^(payment_gateways|payment_sessions)$", ["pay.payments_apps", "apps.restricted_scopes"]),
    (r"^payment_mandate$", ["pay.vaulting", "apps.restricted_scopes"]),
    (r"^customer_payment_methods$", ["pay.vaulting", "apps.restricted_scopes"]),
    (r"^payment_terms$", ["b2b.payment_terms"]),
    (r"^privacy_settings$", ["priv.customer_privacy"]),
    (r"^product_listings$", ["chan.product_feeds"]),
    (r"^products$|^product_tags$", ["cat.products"]),
    (r"^resource_feedbacks$", ["chan.sales_channels"]),
    (r"^returns$", ["ord.returns"]),
    (r"^rollouts$", ["mkt.rollouts"]),
    (r"^script_tags$", ["cat.themes"]),
    (r"^shipping$", ["shp.rates", "shp.carrier_rates"]),
    (r"^shopify_payments_payouts$", ["pay.payouts"]),
    (r"^shopify_payments_bank_accounts$", ["pay.payouts", "pay.funds"]),
    (r"^shopify_payments_(disputes|dispute_evidences|dispute_file_uploads)$", ["pay.disputes"]),
    (r"^shopify_payments(_accounts|_accounts_sensitive)?$", ["pay.shopify_payments"]),
    (r"^shopify_payments_legal_entities$", ["pay.shopify_payments", "acct.business_entity"]),
    (r"^financial_kyc_information$", ["pay.kyc", "apps.restricted_scopes"]),
    (r"^store_credit_account(s|_transactions)$", ["cat.store_credit"]),
    (r"^taxes$", ["tax.calculation", "tax.third_party", "apps.restricted_scopes"]),
    (r"^themes$", ["cat.themes"]),
    (r"^users$", ["acct.staff", "apps.restricted_scopes"]),
    (r"^delivery_promises$", ["shp.delivery_promises", "apps.restricted_scopes"]),
    (r"^shop_pay_installments_pricing$", ["pay.installments"]),
    (r"^product_pickup_locations$", ["shp.local_pickup_delivery"]),
    (r"^draft_orders$", ["ord.draft_orders"]),
    (r"^capital$", CAPITAL),
    (r"^capital_.*$", CAPITAL),
    (r"^gates$", ["ext.digital_goods"]),
    (r"^shipping_labels?$", ["shp.labels"]),
    (r"^inventory_purchase_orders$", ["cat.inventory_transfers"]),
    (r"^delivery_option_generators$", ["shp.delivery_option_fn"]),
    (r"^packing_slip_templates$", ["ord.printing"]),
    (r"^payment_notifications$", []),
    (r"^product_feeds$", ["chan.product_feeds"]),
    (r"^shopify_payments_provider_accounts_sensitive$", ["pay.shopify_payments", "pay.processing", "apps.restricted_scopes"]),
    (r"^theme_code$", ["cat.themes"]),
    (r"^bulk_operations$", ["apps.api_platform"]),
    (r"^bundles$", ["ext.upsell_bundles"]),
]

SCOPE_HEADINGS = {
    "Shopify approval scopes": ["apps.restricted_scopes"], "Orders permissions": ["apps.restricted_scopes", "ord.orders"],
    "Subscription APIs permissions": ["apps.restricted_scopes", "ext.subscriptions"],
    "Shopify Payments dispute evidence permissions": ["apps.restricted_scopes", "pay.disputes"],
    "Theme permissions": ["apps.restricted_scopes", "cat.themes"], "Protected customer data permissions": ["apps.protected_customer_data"],
}

def map_scope(entry, group, extra):
    if entry in SCOPE_HEADINGS:
        return set(SCOPE_HEADINGS[entry]) | {"apps.scopes"}, None
    s = entry
    prefix = ""
    for p in ("unauthenticated_", "customer_"):
        if s.startswith(p) and not s.startswith("customer_events") and not s.startswith("customer_merge") \
                and not s.startswith("customer_data_erasure") and not s.startswith("customer_payment_methods") \
                and not s.startswith("customer_tags"):
            prefix = p; s = s[len(p):]; break
    s = re.sub(r"^(read|write)_", "", s)
    keys = set(["apps.scopes"])
    if prefix == "unauthenticated_":
        keys.add("chan.headless")
        if s == "checkouts":
            keys.add("chk.cart"); return keys, None
        if s == "product_listings":
            keys.add("cat.products"); return keys, None
    if prefix == "customer_":
        keys.add("cust.accounts")
    if s == "companies":
        keys.add("b2b.companies"); return keys, None
    if s == "locations":
        keys.add("b2b.companies" if prefix == "customer_" else "cat.locations"); return keys, None
    for pat, ks in SCOPE_STEMS:
        if ks is None:
            continue
        if re.search(pat, s):
            keys.update(ks); return keys, None
    return set(), None

# ------------------------------------------------------------------ webhook topics
TOPIC = [
    (r"^app/scopes_update$", ["apps.scopes"]),
    (r"^app/uninstalled$", ["apps.apps"]),
    (r"^app_(purchases_one_time|subscriptions)/", ["bill.app_billing"]),
    (r"^audit_events/", ["acct.audit_log"]),
    (r"^bulk_operations/", ["apps.api_platform"]),
    (r"^carts/", ["chk.cart"]),
    (r"^checkouts/", ["chk.checkout", "chk.abandoned"]),
    (r"^channels/", ["chan.sales_channels"]),
    (r"^(collection_listings|product_listings|scheduled_product_listings|product_feeds)/", ["chan.product_feeds"]),
    (r"^(collection_publications|product_publications)/", ["chan.sales_channels"]),
    (r"^collections/", ["cat.collections"]),
    (r"^(companies|company_contact_roles|company_contacts|company_locations)/", ["b2b.companies"]),
    (r"^customer\.(joined|left)_segment$", ["cust.segments"]),
    (r"^customer\.tags_", ["cust.customers"]),
    (r"^customer_account_settings/", ["cust.accounts"]),
    (r"^customer_groups/", ["cust.segments"]),
    (r"^customer_payment_methods/", ["pay.vaulting"]),
    (r"^customers/(data_request|redact)$", ["apps.compliance_webhooks", "priv.data_requests"]),
    (r"^customers/", ["cust.customers"]),
    (r"^customers_(email_marketing_consent|marketing_consent|whats_app_marketing_consent)/", ["cust.marketing_consent"]),
    (r"^delivery_promise_settings/", ["shp.delivery_promises"]),
    (r"^discounts/", ["mktg.discounts"]),
    (r"^disputes/", ["pay.disputes"]),
    (r"^domains/", ["cat.domains"]),
    (r"^draft_orders/", ["ord.draft_orders"]),
    (r"^finance_app_staff_member/", ["acct.staff"]),
    (r"^finance_kyc_information/", ["pay.kyc"]),
    (r"^fulfillment_orders/order_routing_complete$", ["ord.order_routing", "shp.fulfillment"]),
    (r"^fulfillment_orders/line_items_prepared_for_(local_delivery|pickup)$", ["shp.local_pickup_delivery", "shp.fulfillment"]),
    (r"^fulfillment_orders/(fulfillment_service_failed_to_complete|fulfillment_request_|cancellation_request_)", ["shp.fulfillment_services", "shp.fulfillment"]),
    (r"^(fulfillment_events|fulfillment_holds|fulfillment_orders|fulfillments)/", ["shp.fulfillment"]),
    (r"^(inventory_items|inventory_levels)/", ["cat.inventory"]),
    (r"^(inventory_shipments|inventory_transfers)/", ["cat.inventory_transfers"]),
    (r"^locales/", ["cat.translations"]),
    (r"^locations/", ["cat.locations"]),
    (r"^markets_backup_region/", ["mkt.backup_region"]),
    (r"^markets/", ["mkt.markets"]),
    (r"^(metafield_definitions|metaobjects)/", ["cat.custom_data"]),
    (r"^(order_transactions|tender_transactions)/", ["pay.transactions"]),
    (r"^orders/edited$", ["ord.order_editing", "ord.orders"]),
    (r"^orders/risk_assessment_changed$", ["ord.risk"]),
    (r"^orders/shopify_protect_eligibility_changed$", ["pay.protect"]),
    (r"^orders/paid$", ["ord.orders", "pay.transactions"]),
    (r"^orders/", ["ord.orders"]),
    (r"^(payment_schedules|payment_terms)/", ["b2b.payment_terms"]),
    (r"^variants/(in|out_of)_stock$", ["cat.products", "cat.inventory"]),
    (r"^products/", ["cat.products"]),
    (r"^profiles/", ["shp.rates"]),
    (r"^refunds/", ["ord.refunds"]),
    (r"^requested_order_edit/", ["ord.order_editing"]),
    (r"^(returns|reverse_deliveries|reverse_fulfillment_orders)/", ["ord.returns"]),
    (r"^rollouts/", ["mkt.rollouts"]),
    (r"^segments/", ["cust.segments"]),
    (r"^(selling_plan_groups|subscription_billing_attempts|subscription_billing_cycle_edits|subscription_billing_cycles|subscription_contracts)/", ["ext.subscriptions"]),
    (r"^shipping_addresses/", ["cust.customers"]),
    (r"^shop/redact$", ["apps.compliance_webhooks", "data.retention"]),
    (r"^shop/update$", ["acct.store_settings"]),
    (r"^tax_services/", ["tax.third_party"]),
    (r"^themes/", ["cat.themes"]),
]

def enum_to_topic(enum):
    special = {"CUSTOMER_TAGS_ADDED": "customer.tags_added", "CUSTOMER_TAGS_REMOVED": "customer.tags_removed"}
    if enum in special:
        return special[enum]
    prefixes = ["CUSTOMERS_EMAIL_MARKETING_CONSENT", "CUSTOMERS_MARKETING_CONSENT", "CUSTOMERS_WHATS_APP_MARKETING_CONSENT",
                "CUSTOMER_ACCOUNT_SETTINGS", "CUSTOMER_GROUPS", "CUSTOMERS", "DRAFT_ORDERS", "FULFILLMENT_ORDERS", "FULFILLMENT_HOLDS",
                "FULFILLMENTS", "ORDER_TRANSACTIONS", "ORDERS", "PRODUCTS", "REFUNDS", "SHOP", "THEMES", "INVENTORY_LEVELS",
                "INVENTORY_ITEMS", "LOCATIONS", "TENDER_TRANSACTIONS", "MARKETS", "INVENTORY_TRANSFERS", "INVENTORY_SHIPMENTS",
                "DISCOUNTS", "COLLECTIONS", "CHECKOUTS", "CARTS"]
    for p in prefixes:
        if enum.startswith(p + "_"):
            return p.lower() + "/" + enum[len(p) + 1:].lower()
    return enum.lower()

def map_topic(entry, group, extra):
    t = extra and enum_to_topic(extra) or entry
    keys = {"apps.webhooks"}
    for pat, ks in TOPIC:
        if re.search(pat, t):
            keys.update(ks); return keys, None
    return set(), None

# ------------------------------------------------------------------ API resources
ADMIN_CAT = {
    "Access": ["apps.scopes"], "Analytics": ["an.analytics"], "Apps": ["apps.apps"],
    "B2B": ["b2b.companies", "cat.catalogs", "b2b.payment_terms"], "Billing": ["bill.app_billing"],
    "Bulk operations": ["apps.api_platform"], "Cart": ["chk.cart"],
    "Checkout and accounts configurations": ["chk.checkout_branding"], "Checkout branding": ["chk.checkout_branding"],
    "Common objects": ["apps.api_platform"], "Customers": ["cust.customers"],
    "Discounts and marketing": ["mktg.discounts", "mktg.campaigns"], "Inventory": ["cat.inventory"],
    "Localizations": ["cat.translations"], "Metafields": ["cat.custom_data"], "Metaobjects": ["cat.custom_data"],
    "Online store": ["cat.themes", "cat.pages_blogs", "cat.navigation"], "Orders": ["ord.orders"],
    "Privacy": ["priv.customer_privacy", "priv.data_requests"], "Products and collections": ["cat.products", "cat.collections"],
    "Retail": ["chan.pos"], "Shipping and fulfillment": ["shp.fulfillment", "shp.rates"], "Shopify Markets": ["mkt.markets"],
    "Shopify Payments": ["pay.shopify_payments", "pay.payouts", "pay.disputes"], "Store properties": ["acct.store_settings"],
    "Webhooks": ["apps.webhooks"],
}
SIDEBAR = {
    "Versioning": ["apps.api_platform"], "API authentication": ["apps.api_platform"], "Access scopes": ["apps.scopes"],
    "GraphQL pagination": ["apps.api_platform"], "Search query syntax": ["apps.api_platform"], "Global IDs": ["apps.api_platform"],
    "Response status codes": ["apps.api_platform"], "Limits": ["apps.api_platform"], "Idempotent requests": ["apps.api_platform"],
    "Feature previews": ["apps.api_platform"],
    "GraphQL Admin API": ["apps.api_platform"], "Shopify Functions": ["apps.functions"], "ShopifyQL for analytics": ["an.analytics"],
    "Events": ["apps.webhooks"], "Webhooks": ["apps.webhooks"], "Payments Apps API": ["pay.payments_apps"],
    "REST Admin API (legacy)": ["apps.api_platform"],
    "Polaris references": ["apps.admin_ui_ext"], "App Home (iframe)": ["apps.admin_ui_ext"], "App Home (UI extension)": ["apps.admin_ui_ext"],
    "Admin": ["apps.admin_ui_ext"], "Checkout": ["chk.checkout_ui_ext"], "Customer accounts": ["apps.customer_account_ui_ext"],
    "POS": ["chan.pos_ui_ext"], "Using web components": ["apps.admin_ui_ext"],
    "Storefront API": ["chan.headless"], "Liquid": ["cat.themes"], "Ajax API": ["cat.themes"], "About the Ajax API": ["cat.themes"],
    "Section Rendering API": ["cat.themes"], "Hydrogen framework": ["chan.headless"], "Hydrogen React library": ["chan.headless"],
    "Storefront Web Components": ["chan.headless"], "Standard events and actions": ["an.customer_events"],
    "Customer Privacy API": ["priv.customer_privacy"], "Customer Account API": ["cust.accounts"], "WebMCP Tools": ["chan.agentic"],
    "Partner API": ["apps.partner_program"], "App Events API": ["apps.partner_program"],
    "Customer authentication": ["cust.identity_providers"], "Third-party identity providers": ["cust.identity_providers"],
    "Multipass": ["cust.identity_providers"], "Web pixel": ["an.customer_events"], "About Web pixel app extensions": ["an.customer_events"],
    "Web Pixels API": ["an.customer_events"], "Shop API": ["chan.shop"], "Shop Minis": ["chan.shop"], "Shop Pay Wallet API": ["pay.shop_pay"],
}
FUNCTIONS = {
    "Cart and Checkout Validation": ["chk.validation_fn"], "Cart Transform": ["chk.cart_transform_fn"],
    "Delivery Customization": ["shp.delivery_customization_fn"], "Discount": ["mktg.discount_fn"],
    "Fulfillment Constraints": ["shp.fulfillment_constraints_fn"], "Order Routing Location Rule": ["ord.order_routing"],
    "Payment Customization": ["pay.customization_fn"], "Order Discount": ["mktg.discount_fn"],
    "Product Discount": ["mktg.discount_fn"], "Shipping Discount": ["mktg.discount_fn"],
}
EVENTS = {
    "Article": ["cat.pages_blogs"], "Blog": ["cat.pages_blogs"], "Collection": ["cat.collections"], "Company": ["b2b.companies"],
    "Customer": ["cust.customers"], "FulfillmentOrder": ["shp.fulfillment"], "InventoryItem": ["cat.inventory"],
    "InventoryShipment": ["cat.inventory_transfers"], "InventoryTransfer": ["cat.inventory_transfers"], "Location": ["cat.locations"],
    "MetafieldDefinition": ["cat.custom_data"], "Metaobject": ["cat.custom_data"], "MetaobjectDefinition": ["cat.custom_data"],
    "Order": ["ord.orders"], "Page": ["cat.pages_blogs"], "Product": ["cat.products"], "Refund": ["ord.refunds"], "Return": ["ord.returns"],
}
CA_OPS = [
    (r"^company|^companyLocation", ["b2b.companies"]), (r"^customerEmailMarketing|WhatsAppMarketingConsent", ["cust.marketing_consent"]),
    (r"^customer", ["cust.customers"]), (r"^draftOrder$", ["ord.draft_orders"]), (r"^order$", ["ord.orders"]),
    (r"OrderEdit|orderRequestEdit", ["ord.order_editing"]), (r"^orderRequestReturn$|^return", ["ord.returns"]),
    (r"^shop$", ["acct.store_settings"]), (r"^metafields", ["cat.custom_data"]), (r"^storefrontCustomerAccessTokenCreate$", ["chan.headless"]),
    (r"^subscription", ["ext.subscriptions"]),
]

def map_api(entry, group, extra):
    if group == "GraphQL Admin API reference":
        if entry == "GraphQL Types":
            return set(), "the API reference's index of all types (connections, enums, payloads); not a functional group"
        if entry == "Timeline events":
            return set(), "cross-resource activity log (events and comments on other resources); its placement follows the resources it records"
        return set(ADMIN_CAT[entry]), None
    if group.startswith("API references"):
        if group.startswith("API references: Dev tools"):
            return set(), OOS_TOOLING
        if group.endswith("REST Admin API (legacy)"):
            return {"apps.api_platform"}, None
        if group.endswith("Ajax API"):
            return {"cat.themes"}, None
        if group.endswith("Customer authentication"):
            return {"cust.identity_providers"}, None
        if group.endswith("Web pixel"):
            return {"an.customer_events"}, None
        if group.endswith("Shop Minis"):
            return {"chan.shop"}, None
        if entry in SIDEBAR:
            return set(SIDEBAR[entry]), None
        return set(), None
    if group.startswith("Shopify Functions API reference"):
        return set(FUNCTIONS[entry]) | {"apps.functions"}, None
    if group == "Storefront API reference":
        m = {"Cart": ["chk.cart"], "Common objects": [], "Customers": ["cust.customers"], "Metaobjects": ["cat.custom_data"], "Search": ["cat.search"]}
        return set(m[entry]) | {"chan.headless"}, None
    if group.startswith("Customer Account API reference"):
        for pat, ks in CA_OPS:
            if re.search(pat, entry):
                return set(ks) | {"cust.accounts"}, None
        return {"cust.accounts"}, None
    if group.startswith("Payments Apps API reference"):
        if entry == "publicApiVersions":
            return {"pay.payments_apps", "apps.api_platform"}, None
        return {"pay.payments_apps"}, None
    if group == "Events API reference":
        return set(EVENTS[entry]) | {"apps.webhooks"}, None
    if group == "Partner API reference":
        m = {"Active subscription": ["bill.app_billing"], "App subscription cancel": ["bill.app_billing"], "App events": [],
             "Common objects": [], "Historical events": [], "Transactions": ["apps.partner_payouts"]}
        return set(m[entry]) | {"apps.partner_program"}, None
    return set(), None

# ------------------------------------------------------------------ settings and admin navigation
SETTINGS = {
    "Organization": ["acct.organization", "acct.business_entity"], "Users": ["acct.staff"], "Roles": ["acct.roles"],
    "Security": ["acct.signin_security"], "Billing": ["bill.billing"], "General": ["acct.store_settings", "acct.business_entity"],
    "Plan": ["bill.plans"], "Payments": ["pay.providers"], "Checkout": ["chk.checkout"], "Customer accounts": ["cust.accounts"],
    "Shipping and delivery": ["shp.rates"], "Taxes and duties": ["tax.calculation", "tax.registrations", "tax.duties"],
    "Locations": ["cat.locations"], "Markets": ["mkt.markets"], "Apps": ["apps.apps"], "Sales channels": ["chan.sales_channels"],
    "Domains": ["cat.domains"], "Customer events": ["an.customer_events"], "Notifications": ["ops.notifications"],
    "Metafields and metaobjects": ["cat.custom_data"], "Languages": ["cat.translations"], "Customer privacy": ["priv.customer_privacy"],
    "Policies": ["cat.policies"],
}
MAINNAV = {
    "Orders": ["ord.orders"], "Drafts": ["ord.draft_orders"], "Shipping labels": ["shp.labels"], "Abandoned checkouts": ["chk.abandoned"],
    "Products": ["cat.products"], "Collections": ["cat.collections"], "Inventory": ["cat.inventory"], "Purchase orders": ["cat.inventory_transfers"],
    "Transfers": ["cat.inventory_transfers"], "Gift cards": ["cat.gift_cards"], "Customers": ["cust.customers"], "Segments": ["cust.segments"],
    "Companies": ["b2b.companies"], "Growth": ["mktg.campaigns"], "Attribution": ["mktg.attribution"], "Autopilot": ["mktg.campaigns"],
    "Campaigns": ["mktg.campaigns"], "Discounts": ["mktg.discounts"], "Content": ["cat.custom_data", "cat.files", "cat.navigation", "cat.pages_blogs"],
    "Metaobjects": ["cat.custom_data"], "Files": ["cat.files"], "Menus": ["cat.navigation"], "Blog posts": ["cat.pages_blogs"],
    "Markets": ["mkt.markets"], "Catalogs": ["cat.catalogs"], "Rollouts": ["mkt.rollouts"], "Analytics": ["an.analytics"],
    "Reports": ["an.analytics"], "Live View": ["an.analytics"], "Sales channels": ["chan.sales_channels"], "Apps": ["apps.apps"],
}
ROUTER = {
    "AbandonedCheckouts": ["chk.abandoned"], "Account": ["acct.staff"], "AdminDev": ["apps.custom_apps"], "AdminScan": ["cat.products"],
    "Agentic": ["chan.agentic"], "Analytics": ["an.analytics"], "Apps": ["apps.apps"], "Banking": ["fin.balance"],
    "Billing": ["bill.billing", "bill.plans"], "Blockchain": ["ext.digital_goods"], "Capital": CAPITAL, "Cards": ["fin.balance_cards"],
    "Catalogs": ["cat.catalogs"], "Checkout": ["chk.checkout"], "Collections": ["cat.collections"], "CommerceProtection": ["chk.bot_protection"],
    "Companies": ["b2b.companies"], "Content": ["cat.custom_data", "cat.files", "cat.pages_blogs", "cat.navigation"], "Credit": ["fin.credit"],
    "CustomStorefronts": ["chan.headless"], "CustomerAccounts": ["cust.accounts"], "CustomerEvents": ["an.customer_events"],
    "Customers": ["cust.customers"], "Discounts": ["mktg.discounts"], "Domains": ["cat.domains"], "Email": ["mktg.messaging"],
    "Finances": ["pay.payouts", "ord.risk", "fin.bill_pay"], "Flow": ["ops.flow"], "Foundation": ["acct.store_lifecycle"],
    "GiftCards": ["cat.gift_cards"], "Growth": ["mktg.campaigns"], "Intents": ["apps.admin_ui_ext"], "Inventory": ["cat.inventory"],
    "Listings": ["chan.product_feeds"], "Location": ["cat.locations"], "Marketing": ["mktg.campaigns"], "Markets": ["mkt.markets"],
    "MerchantAuditLog": ["acct.audit_log"], "MerchantCheckout": ["chk.checkout"], "MetafieldDefinitions": ["cat.custom_data"],
    "MobileChat": ["ops.inbox"], "Notifications": ["ops.notifications"], "OnlineStore": ["cat.themes"], "Orders": ["ord.orders"],
    "OrganizationSettings": ["acct.organization"], "Payments": ["pay.providers", "pay.shopify_payments"], "Plus": ["bill.plans"],
    "Privacy": ["priv.customer_privacy"], "Products": ["cat.products"], "ProfileAssessment": ["pay.kyc", "acct.identity_verification"],
    "QuickSale": ["chan.pos"], "Reviews": ["ops.reviews"], "Rollouts": ["mkt.rollouts"], "SalesChannels": ["chan.sales_channels"],
    "Shipping": ["shp.rates"], "ShippingLabels": ["shp.labels"], "ShopifyFulfillmentNetwork": ["shp.sfn"], "Sidekick": ["ops.sidekick"],
    "StoreLanguages": ["cat.translations"], "Taxes": ["tax.calculation", "tax.registrations", "tax.filing", "tax.third_party"],
    "Trust": ["acct.identity_verification"],
}
ROUTER_OOS = {
    "AiValue": OOS_UNSTATED, "Batches": OOS_UNSTATED, "Extensibility": OOS_UNSTATED,
    "EmptyTest": "test scaffolding in the admin bundle, not a merchant concern",
    "TestIntent": "test scaffolding in the admin bundle, not a merchant concern",
    "RichTextEditor": "shared editor component of the admin, not a concern",
    "Home": "the admin's landing page; it gathers other concerns rather than holding one",
    "Settings": "container for the settings pages, each listed and placed separately",
    "MilestoneAwards": "recognition of merchant sales milestones; no commerce placement shown in the lists read",
    "WatchApp": "companion watch app page; no commerce placement shown in the lists read",
}

# ------------------------------------------------------------------ staff permissions
PERM = [
    (r"apply_discounts", ["mktg.discounts"]), (r"set_payment_terms", ["b2b.payment_terms"]),
    (r"pay_(draft_)?orders_by_credit_card", ["pay.transactions"]), (r"vaulted", ["pay.vaulting"]),
    (r"mark_(draft_)?orders_as_paid", ["pay.manual"]), (r"capture_payments", ["pay.transactions"]),
    (r"fulfill_and_ship", ["shp.fulfillment"]), (r"buy_shipping_labels", ["shp.labels"]),
    (r"over_refund|refund_to_store_credit", ["ord.refunds", "cat.store_credit"]), (r"refund_orders", ["ord.refunds"]),
    (r"return_orders", ["ord.returns"]), (r"abandoned_checkouts", ["chk.abandoned"]), (r"edit_orders", ["ord.order_editing"]),
    (r"draft_orders", ["ord.draft_orders"]), (r"inventory_transfers|inventory_shipments", ["cat.inventory_transfers"]),
    (r"manage_inventory", ["cat.inventory"]), (r"product", ["cat.products"]), (r"gift_cards", ["cat.gift_cards"]),
    (r"erase_customer_data|request_customer_data", ["priv.data_requests"]),
    (r"company_store_credit|store_credit_account", ["cat.store_credit"]), (r"store_credit_settings", ["cat.store_credit"]),
    (r"compan", ["b2b.companies"]), (r"merge_customers|customers", ["cust.customers"]),
    (r"marketing", ["mktg.campaigns"]), (r"discounts", ["mktg.discounts"]),
    (r"content_links|^links$", ["cat.navigation"]), (r"metaobject", ["cat.custom_data"]), (r"files", ["cat.files"]),
    (r"legal_entity", ["acct.multi_entity"]), (r"catalogs", ["cat.catalogs"]), (r"rollouts", ["mkt.rollouts"]), (r"markets", ["mkt.markets"]),
    (r"identity_providers", ["cust.identity_providers"]), (r"checkout_settings", ["chk.checkout"]),
    (r"quick_sale", ["chan.pos"]),
    (r"applications_billing|billing_application_charges", ["bill.app_billing"]),
    (r"billing_subscriptions", ["bill.plans"]), (r"billing", ["bill.billing"]),
    (r"shopify_payments_payouts|view_payouts", ["pay.payouts"]), (r"shopify_payments_accounts", ["pay.shopify_payments"]),
    (r"shopify_payments_transfers", ["pay.payouts"]), (r"payment_settings|payments_settings", ["pay.providers"]),
    (r"balance_bank_accounts", ["fin.balance"]), (r"shopify_credit", ["fin.credit"]), (r"disputes", ["pay.disputes"]),
    (r"tax_documents", ["fin.tax_documents"]),
    (r"reports|overviews|dashboard", ["an.analytics"]),
    (r"edit_theme_code|themes", ["cat.themes"]), (r"pages", ["cat.pages_blogs"]),
    (r"private_apps", ["apps.custom_apps"]),
    (r"preferences", ["acct.store_settings"]), (r"delivery_settings", ["shp.rates"]), (r"taxes_settings", ["tax.calculation", "tax.registrations"]),
    (r"locations", ["cat.locations"]), (r"domains", ["cat.domains"]), (r"custom_pixels", ["an.customer_events"]),
    (r"policies", ["cat.policies"]), (r"applications", ["apps.apps"]), (r"orders", ["ord.orders"]), (r"home", []),
]
SECTION = {"Home": [], "Orders": ["ord.orders"], "Drafts": ["ord.draft_orders"], "Products": ["cat.products"],
           "Gift cards": ["cat.gift_cards"], "Customers": ["cust.customers"], "Marketing": ["mktg.campaigns"],
           "Discounts": ["mktg.discounts"], "Content": ["cat.custom_data", "cat.files", "cat.navigation"], "Markets": ["mkt.markets"],
           "Checkout and customer accounts": ["chk.checkout", "cust.accounts"], "Quick sale": ["chan.pos"],
           "Finance": ["bill.billing", "pay.payouts", "pay.providers"], "Analytics": ["an.analytics"], "Online store": ["cat.themes"],
           "App development": ["apps.custom_apps"], "Store settings": ["acct.store_settings"], "Apps and channels": ["apps.apps", "chan.sales_channels"]}
SUBGROUP = {"Returns and refunds": ["ord.returns", "ord.refunds"], "Abandoned checkouts": ["chk.abandoned"], "Inventory": ["cat.inventory"],
            "Companies": ["b2b.companies"], "Campaigns": ["mktg.campaigns"], "Metaobject definitions": ["cat.custom_data"],
            "Entries": ["cat.custom_data"], "Files": ["cat.files"], "Catalogs": ["cat.catalogs"]}

def map_perm(entry, group, extra):
    keys = {"acct.roles"}
    if "section" in group:
        sec = re.sub(r" \d+/\d+$", "", entry)
        keys.update(SECTION.get(sec, [])); return keys, None
    if "sub-group" in group:
        sub = entry.split(" > ")[-1]
        keys.update(SUBGROUP.get(sub, [])); return keys, None
    hay = (extra or entry).lower()
    for pat, ks in PERM:
        if re.search(pat, hay):
            keys.update(ks); return keys, None
    return keys, None

# ------------------------------------------------------------------ plan features
PLAN = {
    "Pay monthly": ["bill.plans"], "Pay yearly": ["bill.plans"], "Earn 1% back on all sales": ["bill.plans"],
    "Online store": ["cat.themes"], "Themes and templates": ["cat.themes"], "Sell unlimited products": ["cat.products"],
    "World's best-converting checkout": ["chk.checkout"], "Sell on social and marketplaces": ["chan.sales_channels"],
    "Sell in AI chats": ["chan.agentic"], "Shopify B2B": ["b2b.companies", "cat.catalogs"], "Inventory management": ["cat.inventory"],
    "Inventory locations": ["cat.locations"], "Additional staff accounts": ["acct.staff"], "Invite third-party collaborators": ["acct.collaborators"],
    "Sell and source products with Shopify Collective": ["chan.collective"], "200+ real-time reports, plus custom analytics": ["an.analytics"],
    "24/7 support": ["ops.support"], "Free Shopify Academy courses": ["ops.support"],
    "Casual, in-person sales at pop-ups and events": ["chan.pos"], "POS Pro: Advanced tools for brick‑and‑mortar retailers": ["chan.pos"],
    "Website builder": ["ops.sidekick", "cat.themes"], "Millions of tokens": ["ops.sidekick"], "Sidekick, AI assistant for commerce": ["ops.sidekick"],
    "Shopify Payments": ["pay.shopify_payments"], "Online standard card rates": ["pay.fees"], "Online premium card rates": ["pay.fees"],
    "Online international rates": ["pay.fees"], "PayPal Wallet rates": ["pay.paypal"], "MB WAY rates": ["pay.local_methods", "pay.fees"],
    "Bizum rates": ["pay.local_methods", "pay.fees"], "In-person card rates": ["pay.pos_payments", "pay.fees"], "USDC rates": ["pay.crypto", "pay.fees"],
    "In-person manual rates": ["pay.pos_payments", "pay.fees"], "Third-party transaction fees": ["bill.transaction_fees"],
    "Built-in fraud analysis*": ["ord.risk"], "*Requires Shopify Payments": ["pay.shopify_payments"],
    "Unlimited web hosting": ["cat.hosting"], "Custom domain name": ["cat.domains"], "Free SSL certificate": ["cat.hosting"],
    "Unlimited contacts": ["cust.customers"], "Create customer segments": ["cust.segments"], "Create email campaigns": ["mktg.messaging"],
    "Pay-per-send SMS campaigns": ["mktg.messaging"], "Capture customer leads": ["mktg.campaigns"], "Chat with customers": ["ops.inbox"],
    "Create marketing automations": ["mktg.campaigns"], "Abandoned checkout recovery": ["chk.abandoned"],
    "Create and share discount codes": ["mktg.discounts"], "Sell gift cards": ["cat.gift_cards"],
    "Acquire customers risk-free with Shop Campaigns": ["mktg.shop_campaigns"],
    "Shipping discounts": ["shp.labels"], "Buy and print shipping labels": ["shp.labels"], "Shipping insurance*": ["shp.insurance"],
    "3rd-party calculated shipping rates": ["shp.carrier_rates"],
    "Import unlimited orders from marketplaces": ["chan.marketplaces"], "50 synced marketplace orders per month": ["chan.marketplaces"],
    "Over 50 synced marketplace orders": ["chan.marketplaces"],
    "Integrate with 1000s of apps": ["apps.apps"], "Checkout customization": ["chk.checkout_branding", "chk.checkout_ui_ext"],
    "Build custom apps using Shopify APIs": ["apps.custom_apps"], "API rate limits": ["apps.api_platform"], "Build headless storefronts": ["chan.headless"],
    "Translate your storefront": ["cat.translations"], "Show prices in local currencies*": ["mkt.local_currency"],
    "Localized selling with Shopify Markets": ["mkt.markets"], "Accept local payment methods*": ["pay.local_methods"],
    "Assign local domains": ["mkt.local_domains"], "Estimate and collect duties and taxes": ["tax.duties"],
    "Manage money with Shopify Balance¹": ["fin.balance"], "Flexible growth funding through Shopify Capital²": CAPITAL,
    "Shopify Credit pay-in-full Visa® card³": ["fin.credit"], "Schedule, pay, and manage bills with Shopify Bill Pay": ["fin.bill_pay"],
    "Automated sales tax calculations": ["tax.calculation"], "Tax liability tracking": ["tax.registrations"],
    "VAT validation, exemptions, and invoicing": ["tax.vat_exemptions"], "Advanced tax platform": ["tax.third_party"],
    "High volume checkout": ["chk.checkout"], "Merchandise with Shopify Combined Listings": ["cat.combined_listings"],
    "Optimize ads with Shopify Audiences": ["mktg.audiences"], "Free expansion stores": ["acct.organization"], "Bot protection": ["chk.bot_protection"],
    "Up to 500% higher API call limits": ["apps.api_platform"], "Test new features before launch": ["bill.plans"],
    "Personalize store with custom functions": ["apps.functions"], "Custom user groups": ["acct.roles"], "Plus Certified apps": ["apps.app_store"],
}

def map_plan(entry, group, extra):
    if group.endswith(": section") or group.endswith(": group"):
        if entry == "Pricing":
            return {"bill.plans"}, None
        return set(), OOS_HEADING
    if group.startswith("Billing plans") or group.startswith("Development store plans"):
        return {"bill.plans"} | ({"apps.partner_program"} if group.startswith("Development") else set()), None
    if entry in PLAN:
        return set(PLAN[entry]), None
    return set(), None

# ------------------------------------------------------------------ billing charge categories
CHARGE = {
    "ADDON_FEE": [], "APPLICATION_FEE": ["bill.app_billing"], "SHOPIFY_TAX_FILING": ["tax.filing"], "FEATURE_FEE": ["tax.third_party"],
    "DOMAIN_FEE": ["cat.domains"], "DUTIES_FEE": ["tax.duties"], "BROKERED_SERVICE_FEE": ["apps.partner_services"],
    "EXTERNAL_3PL_FEE": ["shp.fulfillment_services"], "INTERCHANGE_PLUS_PLUS_FEE": ["pay.fees"], "SHIPPING_INSURANCE": ["shp.insurance"],
    "MANAGED_MARKETS_SHIPPING_FEE": ["mkt.managed_markets"], "SHOPIFY_EMAIL": ["mktg.messaging"], "OTHER": [], "PARTNER_ADS": [],
    "PARTNER_APPLICATION_COMMISSION": [], "PLATFORM_FEE": [], "POS_FEE": ["chan.pos"], "POS_PRO": ["chan.pos"],
    "PROFESSIONAL_SERVICE": ["apps.partner_services"], "SHIPPING_DUTIES_TAXES": ["tax.duties", "shp.labels"], "SHIPPING_FEE": ["shp.labels"],
    "SHOP_CAMPAIGNS": ["mktg.shop_campaigns"], "SHOPIFY_BUYERS": [], "SHOPIFY_COLLABS_COMMISSION": ["mktg.collabs"],
    "SHOPIFY_COLLABS_PROCESSING_FEE": ["mktg.collabs"], "SHOPIFY_FULFILLMENT": ["shp.sfn"], "SHOPIFY_FULFILLMENT_TRANSPORTATION": ["shp.sfn"],
    "SHOPIFY_LOGISTICS": ["shp.sfn"], "SUBSCRIPTION_FEE": ["bill.plans"], "SUBSCRIPTION_DISCOUNT": ["bill.plans"], "TAP_TO_PAY": ["pay.pos_payments"],
    "SHOPIFY_TAX": ["tax.calculation"], "THEME_FEE": ["cat.themes"], "ORDER_COMMISSION": ["bill.transaction_fees"],
    "ORDER_COMMISSION_DISCOUNT": ["bill.transaction_fees"], "TAXES": ["bill.billing_taxes"],
}

def map_charge(entry, group, extra):
    if extra == "ALL":
        return set(), "the picker's 'All' option, not a charge category"
    return {"bill.billing"} | set(CHARGE[extra]), None

# ------------------------------------------------------------------ legal agreements and financial complaint products
LEGAL = {
    "Merchant Terms of Service": ["acct.contracting_party", "acct.store_owner"], "View merchant terms": ["acct.contracting_party", "acct.store_owner"],
    "View Shop Pay merchant terms": ["pay.shop_pay"], "View E.U. based merchants supplementary terms of service": ["leg.eu_platform_rules"],
    "View data processing addendum": ["data.roles"], "View terms of service frequently asked questions": ["an.network_intelligence"],
    "Shopify Payments Terms of Service": ["pay.shopify_payments"], "View Shopify Payments terms": ["pay.shopify_payments"],
    "View Shopify Protect terms": ["pay.protect"], "View Cryptocurrency Credit Reward Program terms": ["pay.crypto"],
    "Shopify API License and Terms of Use": ["apps.apps", "apps.partner_program"], "View Shopify API license terms": ["apps.apps", "apps.partner_program"],
    "View App Events API terms": ["apps.partner_program"], "Acceptable Use Policy": ["leg.aup"], "View Acceptable Use Policy": ["leg.aup"],
    "Report an issue with a merchant": ["leg.aup"], "Privacy & Data Protection": ["data.roles", "data.location"],
    "View privacy policy": ["data.roles", "data.location"], "View cookie policy": ["priv.customer_privacy"],
    "View guidelines for legal requests for information": ["leg.legal_requests"], "Shopify's Binding Corporate Rules": ["data.location"],
    "Intellectual Property": ["leg.ip"], "View copyright policy and report copyright infringement": ["leg.ip"],
    "View trademark policy and report trademark infringement": ["leg.ip"], "Partner Terms of Service": ["apps.partner_program"],
    "View partner terms": ["apps.partner_program"], "Report a partner violation": ["apps.partner_program"],
    "Financial Products": ["leg.financial_complaints"], "Submit a financial complaint": ["leg.financial_complaints"],
    "Shopify Fulfillment Network Terms of Service": ["shp.sfn"], "View fulfillment network terms": ["shp.sfn"],
    "Shopify Gift Card and Store Credit Terms": ["cat.gift_cards", "cat.store_credit"], "View terms": ["cat.gift_cards", "cat.store_credit"],
    "Legal Notices": ["leg.eu_platform_rules"], "Digital Service Act": ["leg.eu_platform_rules"], "Legal notices": ["leg.eu_platform_rules"],
    "Submit a P2B complaint": ["leg.eu_platform_rules"], "POS Equipment Agreement and Return Policies": ["chan.pos_hardware"],
    "Balance": ["fin.balance"], "Credit": ["fin.credit"], "Shop Pay Installments": ["pay.installments"],
    "Capital - US loan": ["fin.capital_us"], "Capital - US Merchant Cash Advance (MCA)": ["fin.capital_us"],
    "Capital - UK Merchant Cash Advance (MCA)": ["fin.capital_uk"], "Capital - Canada Merchant Cash Advance (MCA)": ["fin.capital_ca"],
    "Capital - Australia": ["fin.capital_au"],
}
LEGAL_OOS = {
    "Information about Shopify's Patents": "notice about Shopify's own patents; not a concern of the commerce platform's operation",
    "Information about Shopify's Trademarks": "notice about Shopify's own trademarks; not a concern of the commerce platform's operation",
}

TOC = {
    "1. Account Terms": ["acct.store_owner"], "2. Account Activation": ["acct.store_owner", "pay.providers"],
    "3. Shopify Rights": ["leg.aup"], "4. Your Responsibilities": ["acct.store_owner"],
    "5. Payment of Fees and Taxes": ["bill.billing", "bill.billing_taxes"], "8. Intellectual Property and Your Materials": ["leg.ip"],
    "11. Intellectual Property Infringement": ["leg.ip"], "12. Privacy and Data Protection": ["data.roles", "data.pci"],
    "13. Shopify Contracting Party and Forum": ["acct.contracting_party"], "14. Term and Termination": ["acct.store_lifecycle"],
    "9.2 Enhanced Services": ["an.network_intelligence"], "9.3 POS Services": ["chan.pos", "chan.pos_hardware"],
    "9.4 Shopify Shipping": ["shp.labels"], "9.5 SMS Messaging": ["mktg.messaging"], "9.6 Theme Store": ["cat.themes"],
    "9.7 Shopify Email": ["mktg.messaging"], "9.8 Shop": ["chan.shop"], "9.9 Third Party Services and Third Party Partners": ["apps.apps"],
    "9.11 Shopify Pixel Manager": ["an.customer_events"], "9.12 Audiences": ["mktg.audiences"],
    "9.13 Shopify Checkout Extensibility": ["chk.checkout_ui_ext"], "9.14 Agentic Storefronts": ["chan.agentic"],
    "A. The Shopify Payments Service": ["pay.shopify_payments"], "B. Getting a Payments Services Account": ["pay.kyc"],
    "C. Processing Transactions and Receiving Your Funds": ["pay.processing", "pay.funds", "pay.reserves"],
    "D. Termination and Other General Legal Terms": ["pay.shopify_payments"],
    "A. Australia": ["pay.shopify_payments", "pay.installments"], "B. Canada": ["pay.rpaa_canada", "pay.installments", "mkt.managed_markets"],
    "C. United Kingdom": ["pay.installments", "mkt.managed_markets"], "D. United States": ["pay.installments", "mkt.managed_markets"],
    "Account Terms": ["pay.payfac"], "Part I — Global Terms (Payment Facilitator)": ["pay.payfac"], "Part II — Regional Terms": ["pay.payfac"],
    "A. Global": ["pay.processing"], "B. North America": ["pay.processing"], "C. EMEA": ["pay.processing"], "D. Asia-Pacific": ["pay.processing"],
    "I. PURPOSE": ["data.roles"], "III. NATURE OF THE PROCESSING AND ROLES OF THE PARTIES": ["data.roles"],
    "IV. OBLIGATIONS OF PARTIES": ["data.roles", "data.subprocessors", "data.location"], "VI APPENDICES": ["data.roles", "data.location"],
    "Why we process your information": ["data.roles"], "Your rights over your information": ["priv.data_requests"],
    "Where we send your information": ["data.location"], "How long do we retain your information": ["data.retention"],
    "Our use of Machine Learning": ["data.roles"], "How we protect your information": ["data.roles"],
    "How we use \"cookies\" and other tracking technologies": ["priv.customer_privacy"],
    "United States Regional Privacy Notice": ["data.roles", "priv.data_requests"],
}
TOC_OOS = {
    "6. Confidentiality": "confidentiality clause between the contracting parties; not a concern with a commerce placement",
    "7. Limitation of Liability and Indemnification": "allocation of liability in general; recorded under the 'legal' placement of each concern instead",
    "9. Additional Services": OOS_HEADING, "10. Feedback and Reviews": "rules for feedback given to Shopify; not a commerce concern",
    "15. Modifications": "rules for changing the agreement; not a commerce concern", "16. General Conditions": "boilerplate clauses of the agreement; not a commerce concern",
    "9.1 Scope": "defines the term Additional Services; the services are listed and placed separately",
    "9.10 Beta Services": "pre-release features offered by invitation; no concern of its own is named",
    "Part I (Global Terms)": OOS_HEADING, "Part II (Regional Terms)": OOS_HEADING,
    "II. DEFINITIONS": "definitions section of the addendum; not a concern", "V. MISCELLANEOUS": "boilerplate section of the addendum; not a concern",
    "Introduction": "introduction of the policy; not a concern", "Our values": "statement of values; not a concern",
    "How you can reach us": "contact addresses; recorded as evidence for data.location, not a concern of its own",
}

def map_legal(entry, group, extra):
    if "table of contents" in group or "9. Additional Services" in group:
        if entry in TOC_OOS:
            return set(), TOC_OOS[entry]
        return set(TOC.get(entry, [])), None
    if entry in LEGAL_OOS:
        return set(), LEGAL_OOS[entry]
    if group == "Shopify Legal index: POS Equipment Agreement and Return Policies":
        return {"chan.pos_hardware"}, None
    if group.startswith("Financial complaint form"):
        return set(LEGAL[entry]) | {"leg.financial_complaints"}, None
    if entry in LEGAL:
        return set(LEGAL[entry]), None
    return set(), None

# ------------------------------------------------------------------ extension points
TEMPLATE = [
    (r"^(checkout_ui|post_purchase_ui)", ["chk.checkout_ui_ext"]), (r"^app_home$", ["apps.admin_ui_ext"]),
    (r"^customer_account_ui", ["apps.customer_account_ui_ext"]), (r"^admin_print", ["apps.admin_ui_ext", "ord.printing"]),
    (r"^admin_purchase_option", ["apps.admin_ui_ext", "ext.subscriptions"]), (r"^(admin_action|admin_block|conditional_admin_action|admin_link|support_link|editor_extension_collection)", ["apps.admin_ui_ext"]),
    (r"^(app_data|app_action|app_action_link|discount_app_action_link)$", ["ops.sidekick", "apps.admin_ui_ext"]),
    (r"^customer_segment_template", ["cust.segments", "apps.admin_ui_ext"]), (r"^product_configuration", ["ext.upsell_bundles", "apps.admin_ui_ext"]),
    (r"^discount_details_function_settings", ["mktg.discount_fn"]), (r"^validation_settings_ui", ["chk.validation_fn"]),
    (r"^order_routing_location_rule_ui", ["ord.order_routing"]), (r"^pos_", ["chan.pos_ui_ext"]),
    (r"^cart_checkout_validation$", ["chk.validation_fn", "apps.functions"]), (r"^cart_transform$", ["chk.cart_transform_fn", "apps.functions"]),
    (r"^delivery_customization$", ["shp.delivery_customization_fn", "apps.functions"]),
    (r"^(discount|order_discounts|product_discounts|shipping_discounts|discounts_allocator)$", ["mktg.discount_fn", "apps.functions"]),
    (r"^fulfillment_constraints$", ["shp.fulfillment_constraints_fn", "apps.functions"]),
    (r"^(local_pickup_delivery_option_generator|pickup_point_delivery_option_generator|fulfillment_option_generator)$", ["shp.delivery_option_fn", "apps.functions"]),
    (r"^payment_customization$", ["pay.customization_fn", "apps.functions"]), (r"^order_routing_location_rule$", ["ord.order_routing", "apps.functions"]),
    (r"^theme_app_extension$", ["apps.theme_app_ext"]), (r"^web_pixel$", ["an.customer_events"]), (r"^flow_", ["ops.flow"]),
    (r"^subscription_link_extension$", ["ext.subscriptions"]),
    (r"^card_present_payments$", ["pay.payments_apps", "pay.pos_payments"]), (r"^redeemable_payments$", ["pay.payments_apps", "cat.gift_cards"]),
    (r"_payments$", ["pay.payments_apps"]), (r"^channel_config$", ["chan.sales_channels"]), (r"^order_attribution_config$", ["mktg.attribution"]),
    (r"^tax_calculation$", ["tax.third_party"]),
]

def map_ext(entry, group, extra):
    if group.startswith("CLI extension templates"):
        ident = re.search(r"\(([a-z0-9_]+)\)$", entry).group(1)
        for pat, ks in TEMPLATE:
            if re.search(pat, ident):
                return set(ks), None
        return set(), None
    if group.startswith("UI extension targets"):
        t = entry
        if t == "admin.settings.order-routing-rule.render" or t == "admin.settings.internal-order-routing-rule.render":
            return {"ord.order_routing", "apps.admin_ui_ext"}, None
        if t == "admin.settings.validation.render":
            return {"chk.validation_fn", "apps.admin_ui_ext"}, None
        if t.startswith("admin.discount-details.function-settings"):
            return {"mktg.discount_fn", "apps.admin_ui_ext"}, None
        if t.startswith("admin.customers.segmentation-templates"):
            return {"cust.segments", "apps.admin_ui_ext"}, None
        if t in ("admin.app.tools.data", "admin.app.intent.render"):
            return {"ops.sidekick", "apps.admin_ui_ext"}, None
        if t.startswith("admin."):
            return {"apps.admin_ui_ext"}, None
        if t.startswith("purchase.") or t.startswith("Checkout::"):
            return {"chk.checkout_ui_ext"}, None
        if t.startswith("customer-account."):
            return {"apps.customer_account_ui_ext"}, None
        if t.startswith("pos."):
            return {"chan.pos_ui_ext"}, None
        return set(), None
    if group.startswith("Flow connectors"):
        return {"ops.flow"}, None
    if group.startswith("Web Pixels API"):
        return {"an.customer_events"}, None
    return set(), None

# ------------------------------------------------------------------ app store categories
APPCAT = [
    (r"^(Finding products apps|Sourcing option apps|Dropshipping apps|Print on demand|Sourcing options - Other|Wholesale apps)", ["ext.sourcing"]),
    (r"^Marketing and conversion apps$", ["mktg.campaigns"]),
    (r"^(Advertising apps|Ads|Advertising - Other|Affiliate program apps)$", ["ext.advertising"]),
    (r"^Order limit apps$", ["chk.validation_fn", "chk.checkout_ui_ext"]),
    (r"^(Checkout apps|Cart customization apps|Checkout - Other)$", ["chk.checkout_ui_ext"]),
    (r"^(Customer loyalty apps|Customer loyalty - Other|Donation apps|Loyalty and reward apps|Wishlist apps)$", ["ext.loyalty"]),
    (r"^Gift wrap and message apps$", ["ext.product_options"]), (r"^(Gift apps|Gift card apps|Gifts - Other)$", ["cat.gift_cards"]),
    (r"^Abandoned cart apps$", ["chk.abandoned"]), (r"^(Email marketing apps|SMS marketing apps)$", ["mktg.campaigns", "mktg.messaging"]),
    (r"^(Marketing apps|Marketing - Other|Web push apps)$", ["mktg.campaigns"]),
    (r"^(Promotion apps|Discount apps|Giveaways and contests apps|Promotions - Other)$", ["mktg.discounts"]),
    (r"^(Social trust apps|Product review apps|Social proof apps|Social trust - Other)$", ["ops.reviews"]),
    (r"^(Upsell and bundle apps|Countdown timer apps|Pre-order apps|Product bundle apps|Stock alert apps|Upsell and bundles - Other|Upsell and cross-sell apps)$", ["ext.upsell_bundles"]),
    (r"^Orders and shipping apps$", ["ord.orders", "shp.rates"]),
    (r"^ERP apps$", ["ext.accounting", "cat.inventory"]),
    (r"^(Inventory apps|Inventory optimization apps|Inventory - Other|Inventory sync apps)$", ["cat.inventory"]),
    (r"^Invoice and receipt apps$", ["ord.printing"]), (r"^Order editing apps$", ["ord.order_editing"]), (r"^Order tracking apps$", ["shp.tracking"]),
    (r"^(Order apps|Orders - Other)$", ["ord.orders"]),
    (r"^(Return and warranty apps|Returns and exchanges apps|Returns and warranty - Other|Warranties and insurance apps)$", ["ord.returns"]),
    (r"^Delivery and pickup apps$", ["shp.local_pickup_delivery"]), (r"^Shipping rate apps$", ["shp.carrier_rates"]),
    (r"^Third-party logistics \(3PL\) apps$", ["shp.fulfillment_services"]),
    (r"^(Shipping solution apps|Shipping apps|Shipping solutions - Other)$", ["shp.rates", "shp.labels"]),
    (r"^(Sales channel apps|Selling online apps|Selling online - Other)$", ["chan.sales_channels"]),
    (r"^(Selling in person apps|Retail apps|Selling in person - Other|SKU and barcode apps|Store locator apps)$", ["chan.pos"]),
    (r"^Marketplace apps$", ["chan.marketplaces"]), (r"^Product feed apps$", ["chan.product_feeds"]), (r"^Store data importer apps$", ["cat.products"]),
    (r"^Selling products apps$", ["cat.products"]),
    (r"^(Custom product apps|Custom file upload apps|Custom products - Other|Product variant apps)$", ["ext.product_options"]),
    (r"^(Digital goods and service apps|Digital goods and services - Other|Digital product apps|Event booking apps|NFT and tokengating apps)$", ["ext.digital_goods"]),
    (r"^(Payment apps|Pay later apps|Payment experience apps|Payment options - Other)$", ["pay.payments_apps"]),
    (r"^Subscription apps$", ["ext.subscriptions"]),
    (r"^(Pricing apps|Pricing optimization apps|Pricing - Other|Pricing quote apps)$", ["cat.products"]),
    (r"^Metafield apps$", ["cat.custom_data"]), (r"^Blog apps$", ["cat.pages_blogs"]), (r"^Product content apps$", ["cat.products"]),
    (r"^Cookie consent apps$", ["priv.customer_privacy"]), (r"^Currency and translation apps$", ["cat.translations", "mkt.local_currency"]),
    (r"^Geolocation apps$", ["mkt.local_domains"]), (r"^(Internationalization apps|Internationalization - Other)$", ["mkt.markets"]),
    (r"^(Navigation and menu apps)$", ["cat.navigation"]), (r"^(Search and filter apps|Search and navigation apps|Search and navigation - Other)$", ["cat.search"]),
    (r"^Mobile app builder apps$", ["ext.mobile_app"]),
    (r"^(Store design apps|Content apps|Content - Other|Design element apps|Animation and effect apps|Badge and icon apps|Design elements - Other|Image and media apps|3D/AR/VR apps|Image editor apps|Image gallery apps|Images and media - Other|Video and livestream apps|Notification apps|Banner apps|Form apps|Notifications - Other|Pop-up apps|Product display apps|Collection apps|Product comparison apps|Product display - Other|Site optimization apps|Accessibility apps|SEO apps|Site optimization - Other|Storefront apps|Page builder apps|Storefronts - Other)$", ["ext.store_design"]),
    (r"^Store management apps$", ["apps.apps"]),
    (r"^(Finance apps|Accounting apps|Finances - Other)$", ["ext.accounting"]), (r"^Tax apps$", ["tax.third_party"]),
    (r"^(Operations apps|Operations - Other)$", ["apps.apps"]), (r"^Analytics apps$", ["an.analytics"]), (r"^Bulk editor apps$", ["cat.products"]),
    (r"^Staff notification apps$", ["ops.notifications"]), (r"^Workflow automation apps$", ["ops.flow"]),
    (r"^Accounts and login apps$", ["cust.identity_providers"]), (r"^Fraud apps$", ["ord.risk"]),
    (r"^(Security apps|Anti theft apps|Legal apps|Security - Other)$", ["ext.security_legal"]),
    (r"^(Support apps|Chat apps|FAQ apps|Helpdesk apps|Support - Other|Survey apps)$", ["ext.support_helpdesk"]),
]

def map_appcat(entry, group, extra):
    for pat, ks in APPCAT:
        if re.search(pat, entry):
            return set(ks), None
    return set(), None

# ------------------------------------------------------------------ other lists
COMPRODUCTS = {
    "Website Builder": ["cat.themes", "ops.sidekick"], "Themes": ["cat.themes"], "Domains": ["cat.domains"], "Customer Accounts": ["cust.accounts"],
    "Sidekick": ["ops.sidekick"], "Online": ["cat.themes"], "AI Chats": ["chan.agentic"], "Point of Sale": ["chan.pos"], "Shop App": ["chan.shop"],
    "Social & Marketplaces": ["chan.sales_channels", "chan.marketplaces"], "Global": ["mkt.markets"], "B2B": ["b2b.companies"],
    "Across Markets": ["mkt.markets"], "Advertising & Campaigns": ["mktg.campaigns"], "Email & Customer Chat": ["mktg.messaging", "ops.inbox"],
    "Discounts": ["mktg.discounts"], "Analytics": ["an.analytics"], "Orders & Inventory": ["ord.orders", "cat.inventory"],
    "Shipping": ["shp.rates", "shp.labels"], "Finances & Funding": ["fin.balance", "fin.credit", "fin.bill_pay"] + CAPITAL,
    "Workflow Automation": ["ops.flow"], "Checkout": ["chk.checkout"], "Payments": ["pay.shopify_payments"], "Taxes": ["tax.calculation"],
    "Commerce for AgentsBuild with our agent tools": ["chan.agentic"], "Shopify App StoreLargest commerce ecosystem": ["apps.app_store"],
    "Shopify.devDev docs, CLI, and more": ["apps.api_platform"],
}
COMPRODUCTS_OOS = {"Test & Launch": "product menu label whose scope is not stated in the list; no placement can be shown"}

HELP = [
    (r"^Shopify Payments for ", ["pay.shopify_payments"]),
    (r"^Getting paid$", ["pay.payouts", "pay.providers"]), (r"^Shop Cash$", ["pay.shop_cash"]),
    (r"^Shop Pay accelerated checkout", ["pay.shop_pay"]), (r"^Shopify Payments$", ["pay.shopify_payments"]),
    (r"^PayPal Express Checkout$", ["pay.paypal"]), (r"^Accelerated checkouts", ["pay.wallets", "pay.shop_pay"]),
    (r"^Shop Pay Installments$", ["pay.installments"]), (r"^Third-party payment providers$", ["pay.payments_apps"]),
    (r"^Additional payment methods$", ["pay.payments_apps", "pay.crypto"]), (r"^Manual payment methods$", ["pay.manual"]),
    (r"partial payments", ["pay.transactions"]), (r"^Payment authorization and capture$", ["pay.transactions"]),
    (r"^Chargebacks and inquiries$", ["pay.disputes"]), (r"^Fraud prevention$", ["ord.risk"]),
    (r"^Troubleshooting (payment gateways|checkout payment issues)$", ["pay.providers"]),
    (r"^Supported countries for Shopify Payments$", ["pay.shopify_payments"]), (r"^Setting up Shopify Payments$", ["pay.kyc", "pay.shopify_payments"]),
    (r"^(Configuring|Testing) Shopify Payments$", ["pay.shopify_payments"]), (r"^Shopify Payments transactions$", ["pay.transactions"]),
    (r"^Store Currencies$", ["mkt.store_currency"]), (r"^Getting paid with Shopify Payments$", ["pay.payouts"]),
    (r"^Managed payment methods$", ["pay.shopify_payments"]), (r"^Using Shopify Payments with a third-party provider$", ["pay.shopify_payments", "pay.payments_apps"]),
    (r"^Local payment methods$", ["pay.local_methods"]), (r"^Troubleshooting failed or pending refunds$", ["ord.refunds"]),
    (r"^Shopify Payments eligibility$", ["pay.shopify_payments", "leg.payments_prohibited"]), (r"^Shopify Payments fees$", ["pay.fees"]),
    (r"^Setting up your Shopify Payments account$", ["pay.kyc"]), (r"^Acceptable business practices", ["pay.kyc", "pay.reserves", "leg.payments_prohibited"]),
    (r"^Proof of Liveness check$|^Reapplying for Shopify Payments$|account verification updates in Europe", ["pay.kyc"]),
    (r"^Bank account requirements for Shopify Payments$", ["pay.payouts"]), (r"^American Express requirements", ["pay.processing"]),
    (r"^Selling with multiple entities$", ["acct.multi_entity"]),
    (r"payout|activity report", ["pay.payouts"]), (r"^Shopify Payments refunds$", ["ord.refunds"]),
    (r"^Overview of reserves|account holds$", ["pay.reserves"]),
    (r"^Understanding your store and payout currencies$", ["mkt.store_currency", "pay.payouts"]),
    (r"^Selling and getting paid in different currencies$", ["mkt.local_currency", "mkt.fx"]),
    (r"^Supported payout currencies$|^Managing Multi-Currency Payouts", ["pay.payouts"]), (r"^Changing your store currency$", ["mkt.store_currency"]),
    (r"^Multi-currency$", ["mkt.local_currency"]), (r"^Currency conversion fee calculation", ["mkt.fx"]),
    (r"^Pricing in local currencies$", ["mkt.local_currency"]), (r"storefront redirection|Geolocation app|^International domains$|International SEO", ["mkt.local_domains"]),
    (r"^Localization and translation$|Translate & Adapt", ["cat.translations"]), (r"^Duties and import taxes$|international duty", ["tax.duties"]),
    (r"^Payments$", ["pay.providers"]), (r"^International shipping$", ["shp.rates"]), (r"^Duty and tax inclusive pricing$", ["tax.duties", "tax.calculation"]),
    (r"GPSR|CPSC|^Alcohol products$|^Hemp|dangerous goods|^Consumer protection laws$|right of withdrawal|Price Indication|TSE Compliance", ["leg.merchant_compliance"]),
    (r"^Managed Markets$", ["mkt.managed_markets"]),
    (r"^Understanding checkout restrictions$|restrictions in France|^Guidelines and restrictions for selling in local currencies$|^Rounding prices$|^Testing your multiple currency setup$|^Formatting how currency displays", ["mkt.local_currency"]),
    (r"^Currency conversions and exchange rates$|^Volatile currencies$|^Fees and costs$", ["mkt.fx"]),
    (r"^Primary gateways for international", ["mkt.local_currency", "pay.providers"]), (r"^Dynamic tax-inclusive pricing$", ["tax.calculation"]),
    (r"^Discounts and gift cards in Markets$", ["mktg.discounts", "cat.gift_cards"]), (r"^Discounts$", ["mktg.discounts"]),
    (r"^Gift cards$", ["cat.gift_cards"]), (r"^Refunds$", ["ord.refunds"]),
    (r"^Customizing markets$|^Getting started with markets$|^Adding and removing market customizations$|^Customizing online store for markets$", ["mkt.markets"]),
    (r"^Rollouts$", ["mkt.rollouts"]), (r"^Backup region in Markets$", ["mkt.backup_region"]), (r"currency change in Markets", ["mkt.local_currency"]),
    (r"^Creating catalogs for markets$", ["cat.catalogs"]), (r"^Setting up currencies for markets$", ["mkt.local_currency"]),
    (r"^Assigning domains and languages to markets$", ["mkt.local_domains", "cat.translations"]),
    (r"^Setting up duties and taxes for markets$", ["tax.duties"]), (r"^Setting up business entities for markets$", ["acct.multi_entity", "acct.business_entity"]),
    (r"^Overview of your financial information$", ["pay.payouts"]), (r"^Shopify Balance$", ["fin.balance"]),
    (r"^Shopify Capital$", CAPITAL), (r"^Shopify Credit$", ["fin.credit"]), (r"^Shopify Bill Pay$", ["fin.bill_pay"]),
    (r"Capital funding in the Shopify Balance app", ["fin.balance"] + CAPITAL), (r"Sidekick in the Shopify Balance app", ["fin.balance", "ops.sidekick"]),
    (r"^International transfers of personal data$|^Onward transfers|^Security of transfers", ["data.location"]),
    (r"^General Data Protection Regulation|^Navigating your privacy and data protection requirements$", ["data.roles"]),
    (r"^Managing customer privacy settings$", ["priv.customer_privacy"]), (r"^US state privacy laws$", ["priv.customer_privacy", "data.roles"]),
    (r"^Erase your data$", ["data.retention"]), (r"^Processing customer data requests$", ["priv.data_requests"]),
    (r"^Subprocessors$", ["data.subprocessors"]), (r"Shopify Network Intelligence", ["an.network_intelligence"]),
    (r"primary contracting entities", ["acct.contracting_party", "data.location"]),
    (r"Transparency Report", ["leg.legal_requests", "data.location"]),
    (r"^Dropshipping$", ["ext.sourcing", "leg.merchant_compliance"]), (r"^Product fulfillment documentation$", ["leg.aup"]),
    (r"^Unsupported countries and regions$", ["leg.sanctions"]), (r"^Shop Supplementary Guidelines", ["chan.shop"]),
    (r"^Resolving terms violations$|store review$|store termination$|non-consensual intimate imagery", ["leg.aup", "acct.store_lifecycle"]),
    (r"^General tax set-up steps$|impact of tax collection|^Include taxes in product prices$|^Shopify Tax$|^Basic Tax$|^Manual tax settings$|^Shipping tax$|^Digital product taxes$", ["tax.calculation"]),
    (r"^Setting up tax rates for Shopify POS$", ["tax.calculation", "chan.pos"]), (r"^Tax apps$|^Activating tax apps$|^Vertex$|^Avalara Tax Compliance$", ["tax.third_party"]),
    (r"^(US|EU|UK|Canadian) taxes$|^Taxes in Japan$|^GST in India FAQ$", ["tax.registrations", "tax.calculation"]),
    (r"^Tax reports$|^Data Exporter$", ["tax.registrations"]), (r"^Tax overrides and exemptions$", ["tax.vat_exemptions"]),
    (r"^Considerations for using Shopify Tax$|^Estimated taxes during checkout$|^Shopify Tax pricing$|^Shopify Tax features in Canada$", ["tax.calculation"]),
    (r"^Product categories$", ["tax.calculation", "cat.products"]), (r"^Choose a tax service$", ["tax.calculation", "tax.third_party"]),
    (r"^Update email notifications$", ["tax.registrations"]), (r"European Union and United Kingdom$", ["tax.calculation", "tax.vat_exemptions"]),
    (r"^VAT validation in checkout$", ["tax.vat_exemptions"]), (r"[Aa]utomated filing", ["tax.filing"]),
    (r"^Managing your Shopify bills$|^Paying your Shopify bills$|^Charges on your Shopify bills$|billing extensions|credit notes|^Shopify offers and promotions$", ["bill.billing"]),
    (r"refund policy for plans", ["bill.plans", "bill.billing"]), (r"pausing or deactivating", ["bill.billing", "acct.store_lifecycle"]),
    (r"Shopify billing in", ["bill.billing_taxes"]),
    (r"^Getting started shipping with Shopify$|^Setting up shipping and order fulfillment$", ["shp.rates", "shp.fulfillment"]),
    (r"^Overview of order fulfillment|^Fulfilling orders$", ["shp.fulfillment"]), (r"^Managing orders$", ["ord.orders"]), (r"^Fulfillment Network$", ["shp.sfn"]),
    (r"^Getting started with Shopify Point of Sale$|^Selling in person with Shopify POS$", ["chan.pos"]), (r"^Hardware for Shopify POS$", ["chan.pos_hardware"]),
    (r"^Retail markets$", ["chan.pos", "mkt.markets"]), (r"QuickBooks Desktop POS", ["chan.pos", "ext.accounting"]),
    (r"^About apps$|^Apps made by Shopify$|^Finding and choosing apps$|^Installing and setting up apps$|^Managing apps$|^Getting help with apps$|^Uninstalling apps$", ["apps.apps"]),
    (r"^App extensions and functions$", ["apps.functions", "apps.admin_ui_ext"]),
    (r"^Editing the checkout form options$|tipping options|address collection|^Placing a test order$", ["chk.checkout"]),
    (r"^Customizing and editing your checkout and accounts pages$", ["chk.checkout_branding"]), (r"order processing and archiving", ["ord.orders"]),
    (r"^Translating your checkout$", ["cat.translations", "chk.checkout"]), (r"maximum quantity of items per cart|^Cart permalinks$", ["chk.cart"]),
    (r"^Ship and pickup in one order", ["shp.local_pickup_delivery"]), (r"^Split shipping", ["shp.fulfillment"]), (r"^Adding store policies$", ["cat.policies"]),
    (r"selling to bots", ["chk.bot_protection"]), (r"^Customizing payment methods and delivery options at checkout$", ["pay.customization_fn", "shp.delivery_customization_fn"]),
    (r"^Checkout Blocks app$", ["chk.checkout_ui_ext"]), (r"Shopify Scripts and the Script Editor app", ["chk.checkout"]),
]

def map_help(entry, group, extra):
    for pat, ks in HELP:
        if re.search(pat, entry):
            return set(ks), None
    return set(), None

def map_other(lst, entry, group, extra):
    if lst == "other:help-center-sections":
        return map_help(entry, group, extra)
    if lst == "other:business-entities":
        return {"acct.business_entity"}, None
    if lst == "other:signup":
        if "options" in entry:
            return {"acct.signup_location"}, None
        return {"acct.signin_security"}, None
    if lst == "other:account-destinations":
        m = {"Your store": ["acct.store_owner"], "Shopify Partners": ["apps.partner_program"], "Shopify Learn": ["ops.support"],
             "Shopify Community": ["ops.support"], "Shopify Inbox": ["ops.inbox"], "Shopify Collabs": ["mktg.collabs"], "Need Help?": ["ops.support"]}
        if entry in m:
            return set(m[entry]), None
        return set(), "page footer link to a legal page that is placed under the legal index"
    if lst == "other:ucp":
        keys = {"chan.agentic"}
        if entry == "dev.shopify.shop_pay":
            keys.add("pay.shop_pay")
        elif entry == "com.google.pay":
            keys.add("pay.wallets")
        elif entry == "dev.shopify.card":
            keys.add("pay.providers")
        elif "checkout" in entry:
            keys.add("chk.checkout")
        elif "cart" in entry:
            keys.add("chk.cart")
        elif "order" in entry:
            keys.add("ord.orders")
        elif "catalog" in entry or entry == "get_product":
            keys.add("cat.products")
        elif "fulfillment" in entry:
            keys.add("shp.rates")
        elif "discount" in entry:
            keys.add("mktg.discounts")
        elif "identity_linking" in entry or "buyer_consent" in entry:
            keys.add("cust.accounts")
        return keys, None
    if lst == "other:app-store-categories":
        return map_appcat(entry, group, extra)
    if lst == "other:shopify-com-products":
        if entry in COMPRODUCTS_OOS:
            return set(), COMPRODUCTS_OOS[entry]
        return set(COMPRODUCTS.get(entry, [])), None
    if lst == "other:shopify-apps":
        m = {"Shop: Track, Pay, Discover": ["chan.shop"], "Shopify Point of Sale (POS)": ["chan.pos"], "Shopify Inbox": ["ops.inbox"],
             "Collabs: Content commerce": ["mktg.collabs"], "Customer View": ["chan.pos"]}
        if entry in m:
            return set(m[entry]), None
        if entry.startswith("Shopify: Ecommerce business"):
            return set(), "mobile client of the Shopify admin; the concerns it reaches are placed individually"
        if entry.startswith("Tinker by Shopify"):
            return set(), "separate creative-tools app published by Shopify; no commerce placement is shown in the lists read"
        return set(), None
    if lst == "other:notification-templates":
        if "Shopify Messaging" in entry:
            return {"mktg.messaging", "ops.notifications"}, None
        if entry == "Remarketing with Shop":
            return {"chan.shop", "ops.notifications"}, None
        return {"ops.notifications"}, None
    if lst == "other:translatable-resources":
        return {"cat.translations"}, None
    if lst == "other:partner-dashboard":
        m = {"App distribution": ["apps.app_store"], "Catalogs": ["chan.agentic"], "Themes": ["cat.themes", "apps.partner_program"],
             "Payouts": ["apps.partner_payouts"]}
        return set(m.get(entry, ["apps.partner_program"])), None
    if lst == "other:partner-permissions":
        m = {"View financials": ["apps.partner_payouts"], "Manage app subscriptions": ["bill.app_billing"], "Manage apps": [], "Manage themes": ["cat.themes"]}
        return set(m.get(entry, [])) | {"apps.partner_program"}, None
    if lst == "other:value-lists":
        m = {"Tracking carriers (204 options)": ["shp.tracking"], "Return reasons (10 options)": ["ord.returns"],
             "Inventory adjustment reasons (7 options)": ["cat.inventory"], "Add language (136 languages)": ["cat.translations"]}
        return set(m[entry]), None
    if lst == "other:staff-roles":
        keys = {"acct.roles"}
        if "POS" in entry or entry in ("Associate", "Cashier", "Sales associate", "Store manager", "Limited permissions"):
            keys.add("chan.pos")
        if entry == "App developer":
            keys.add("apps.custom_apps")
        if entry == "Collaborator access":
            keys.add("acct.collaborators")
        if entry.startswith("Organization"):
            keys.add("acct.organization")
        return keys, None
    if lst == "other:staff-permissions":
        return map_perm(entry, group, extra)
    if lst == "other:billing-charge-categories":
        return map_charge(entry, group, extra)
    return set(), None

def map_row(lst, entry, group, extra):
    if lst == "access-scopes":
        return map_scope(entry, group, extra)
    if lst == "webhook-topics":
        return map_topic(entry, group, extra)
    if lst == "api-resources":
        return map_api(entry, group, extra)
    if lst == "settings":
        return set(SETTINGS.get(entry, [])), None
    if lst == "admin-navigation":
        if group == "Admin router section":
            if entry in ROUTER_OOS:
                return set(), ROUTER_OOS[entry]
            return set(ROUTER.get(entry, [])), None
        if entry == "Home":
            return set(), "the admin's landing page; it gathers other concerns rather than holding one"
        if entry == "Settings":
            return set(), "container for the settings pages, each listed and placed separately"
        return set(MAINNAV.get(entry, [])), None
    if lst == "plan-features":
        return map_plan(entry, group, extra)
    if lst == "legal-agreements":
        return map_legal(entry, group, extra)
    if lst == "extension-points":
        return map_ext(entry, group, extra)
    return map_other(lst, entry, group, extra)
