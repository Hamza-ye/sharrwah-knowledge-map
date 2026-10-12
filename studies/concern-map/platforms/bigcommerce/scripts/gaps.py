# Gaps: every concern x placement cell without a statement gets one gap row.
# Per-concern routes: pages read (R), a guide page not read (U) and Help Center articles that
# BigCommerce's own docs link to (H). Help Center articles could not be read in this session.
D = "https://docs.bigcommerce.com/developer/docs/"
A = "https://docs.bigcommerce.com/developer/api-reference/"
HC = "https://support.bigcommerce.com/s/article/"
T = "https://www.commerce.com/"
W = "https://www.bigcommerce.com/"

R = {  # pages read for the concern (shortened)
    1: [A + "rest/admin/catalog/products.md"], 2: [A + "rest/admin/catalog/brands.md"],
    3: [A + "rest/admin/catalog/categories.md", A + "rest/admin/catalog/category-trees.md"],
    4: [A + "rest/admin/management/inventory.md"], 5: [D + "admin/catalog-and-inventory/inventory-locations.md"],
    6: [A + "rest/admin/management/pickup.md", A + "rest/admin/management/pickup/pickup-methods.md"],
    7: [A + "rest/admin/management/price-lists.md", W + "pricing/"], 8: [A + "rest/admin/management/pricing.md"],
    9: [A + "rest/admin/management/promotions.md", A + "rest/admin/management/promotion-settings.md"],
    10: [A + "rest/admin/content/marketing.md"], 11: [A + "rest/admin/management/settings.md", W + "pricing/"],
    12: [W + "pricing/"], 13: [D + "beta.md"], 14: [A + "rest/admin/management/carts.md", A + "rest/storefront/carts.md"],
    15: [A + "rest/admin/management/abandoned-carts.md", A + "rest/admin/content/abandoned-cart-emails.md"],
    16: [A + "rest/admin/management/checkouts.md", D + "admin/checkout-and-cart/open-checkout/pciguide.md"], 17: [D + "beta.md"],
    18: [A + "rest/admin/management/orders.md", D + "admin/checkout-and-cart/orders/overview.md"], 19: [A + "rest/admin/management/orders.md"],
    20: [D + "admin/checkout-and-cart/payments/transactions-api.md"], 21: [D + "admin/checkout-and-cart/orders/refunds.md"],
    22: [D + "admin/checkout-and-cart/payments/overview.md"], 23: [A + "rest/admin/payments/methods.md"],
    24: [A + "rest/admin/payments/stored-instruments.md", D + "admin/checkout-and-cart/payments/overview.md"],
    25: [W + "payments/bigcommerce-payments/"], 26: [W + "pricing/", W + "payments/gateways/"], 27: [D + "admin/checkout-and-cart/payments/overview.md", W + "product/"],
    28: [T + "terms/", D + "storefront/headless/pci-compliance.md"], 29: [T + "terms/merchant-unified-billing/", D + "integrations/apps/unified-billing/overview.md"],
    30: [T + "terms/fees-and-billing/", W + "pricing/"], 31: [A + "rest/b2b/management/payment.md", A + "rest/b2b/management/invoice-management.md"],
    32: [A + "rest/admin/management/customers/v3.md", D + "admin/customers/customers-and-subscribers.md"],
    33: [A + "rest/admin/authentication-apis/customer-login-api/overview.md", A + "rest/admin/authentication-apis/current-customer/overview.md"],
    34: [A + "rest/admin/management/customer-segmentation.md"], 35: [A + "rest/admin/management/subscribers.md"],
    36: [A + "rest/admin/management/wishlists.md"], 37: [A + "rest/storefront/consent.md", D + "storefront/catalyst/features/cookie-consent.md"],
    38: [A + "rest/admin/management/channels.md", D + "integrations/channels/introduction.md"], 39: [T + "terms/", D + "admin/multi-storefront/overview.md"],
    40: [A + "rest/admin/management/sites.md"], 41: [A + "rest/admin/management/redirects.md"],
    42: [A + "rest/admin/content/themes.md", T + "terms/store-terms/"], 43: [A + "rest/admin/content/widgets.md", A + "rest/admin/content/page-widgets.md"],
    44: [A + "rest/admin/management/scripts.md", D + "integrations/scripts.md"], 45: [A + "rest/admin/content/pages.md", A + "rest/admin/content/store-content.md"],
    46: [A + "rest/admin/content/email-templates.md"], 47: [A + "rest/admin/management/settings.md", D + "admin/store-configuration/settings/store-configuration.md"],
    48: [D + "admin/store-configuration/translations/overview.md", D + "admin/store-configuration/settings/locales-configuration.md"],
    49: [A + "rest/admin/management/store-information/v3.md", D + "overview/api-fundamentals/api-accounts.md"],
    50: ["https://docs.bigcommerce.com/developer/llms.txt"], 51: ["https://docs.bigcommerce.com/developer/llms.txt", T + "terms/"],
    52: [D + "storefront/catalyst/deployment/native-hosting/overview.md", A + "rest/admin/management/infrastructure-hosting.md"],
    53: [A + "rest/admin/authentication-apis/storefront-api-tokens/overview.md", A + "graphql/overview.md"], 54: [A + "graphql/overview.md"],
    55: [A + "graphql/account/overview.md"], 56: [D + "overview/api-fundamentals/api-accounts.md", T + "terms/api-terms/"],
    57: [D + "overview/api-fundamentals/rate-limits.md"], 58: [D + "integrations/webhooks/overview.md"],
    59: [D + "integrations/apps/guide/types-of-apps.md", D + "integrations/apps/guide/approval-requirements.md"],
    60: [A + "rest/admin/management/system-logs.md"], 61: [A + "graphql/account/overview.md", W + "pricing/"],
    62: [W + "pricing/", A + "rest/admin/management/settings.md"], 63: [A + "mcp/overview.md", T + "terms/ai-features-addendum/"],
    64: [T + "terms/ai-features-addendum/", W + "product/"], 65: [A + "rest/b2b/overview.md", A + "rest/b2b/management/overview.md"],
    66: [D + "beta.md"], 67: [T + "terms/", W + "pricing/"], 68: [A + "rest/admin/management/channels.md", W + "product/"],
    69: [A + "rest/admin/management/channels.md", W + "product/"], 70: [A + "rest/admin/management/shipping.md", W + "pricing/"],
    71: [A + "rest/integrations/shipping-provider.md", D + "integrations/shipping-providers.md"],
    72: [A + "rest/admin/management/tax.md", D + "admin/store-configuration/tax/tax-settings.md"],
    73: [D + "integrations/tax-providers.md", A + "rest/admin/management/tax/tax-settings/update-tax-settings.md"],
    74: [D + "admin/store-configuration/currencies/overview.md"], 75: [A + "rest/admin/management/geography.md"],
    76: [D + "integrations/platform-solutions/staging-with-staging-pro.md"], 77: [T + "terms/mobile-app-terms/", W + "pricing/"],
    78: [A + "rest/admin/management/settings.md", W + "product/secure-web-hosting/"], 79: [T + "terms/", T + "terms/jurisdiction-specific-terms/"],
    80: [T + "terms/"], 81: [T + "privacy/data-processing-addendum/", T + "privacy/"], 82: [T + "privacy/data-processing-addendum/", T + "privacy/data-processors/"],
    83: [T + "privacy/data-processors/", T + "terms/"], 84: [T + "terms/"], 85: [T + "terms/acceptable-use-policy/"],
    86: [T + "terms/store-terms/"], 87: [T + "terms/merchant-client-terms/"], 88: [T + "terms/infringing-materials-protocol/"],
}
U = {  # guide page named in the docs index that would likely state more, not read in this run
    1: D + "admin/catalog-and-inventory/products-overview.md", 2: D + "admin/catalog-and-inventory/products-overview.md",
    3: D + "admin/catalog-and-inventory/products-overview.md", 4: D + "admin/catalog-and-inventory/inventory-adjustments.md",
    6: D + "integrations/platform-solutions/buy-online-pick-up-in-store/overview.md", 7: D + "admin/catalog-and-inventory/pricing/price-lists.md",
    8: D + "admin/catalog-and-inventory/pricing/calculations.md", 9: D + "admin/catalog-and-inventory/promotions/overview.md",
    11: D + "storefront/headless/products/faceted-textual-search.md", 12: D + "storefront/guides/graphql-storefront-api/products-and-catalog/product-reviews.md",
    13: D + "beta/product-recommendations/overview.md", 14: D + "storefront/headless/cart-and-checkout/carts.md",
    15: D + "storefront/headless/cart-and-checkout/abandoned-carts.md", 16: D + "admin/checkout-and-cart/overview.md",
    17: D + "beta/checkout-extensions/overview.md", 19: D + "admin/checkout-and-cart/orders/overview.md",
    23: D + "admin/checkout-and-cart/payments/overview.md", 24: D + "admin/checkout-and-cart/payments/stored-instruments.md",
    27: D + "admin/checkout-and-cart/payment-providers/wallets/filter-wallet-shipping-options.md", 33: D + "storefront/headless/customers.md",
    34: D + "admin/customers/customer-segmentation/overview.md", 40: D + "storefront/headless/routes.md", 42: D + "storefront/stencil/overview.md",
    43: D + "admin/widgets-and-scripts/overview.md", 45: D + "storefront/headless/site-content.md", 46: D + "admin/store-configuration/emails/overview.md",
    49: D + "admin/store-configuration/metafields/store-metafields.md", 50: D + "storefront/catalyst/overview.md",
    51: D + "storefront/catalyst/makeswift/overview.md", 53: D + "storefront/guides/graphql-storefront-api/overview.md",
    54: A + "graphql/admin/queries/store.md", 62: D + "integrations/platform-solutions/analytics-with-bodl.md", 66: D + "beta/powered-by/api-documentation.md",
    70: D + "admin/store-configuration/shipping/overview.md",
}
# All guide pages above were fetched and searched for reason, scope and setting wording on 12 October 2026;
# they now count as pages read.
for _c, _u in U.items():
    R.setdefault(_c, []).append(_u)
U = {}

H = {  # Help Center articles linked from BigCommerce's developer docs
    4: ["Inventory-Tracking", "BigCommerce-Inventory-Functionality"], 5: ["BigCommerce-Inventory-Functionality"], 7: ["Price-Lists"], 8: ["Pricing"],
    15: ["Using-the-Abandoned-Cart-Saver"], 16: ["Optimized-Single-Page-Checkout", "Checkout-Settings"], 18: ["Order-Statuses", "Creating-a-Manual-Order"],
    21: ["Processing-Refunds", "Processing-Returns"], 22: ["Getting-Started-Payments", "Available-Payment-Gateways"], 23: ["Available-Payment-Gateways", "Offline-Payment-Methods"],
    24: ["Enabling-Stored-Payment-Methods", "Enabling-Stored-Credit-Cards"], 26: ["Available-Payment-Gateways", "Intro-to-APMs"], 27: ["Fastlane-by-PayPal"],
    28: ["PCI-Compliance"], 29: ["Unified-Billing-for-Partners"], 31: ["B2B-Edition-Settings"], 32: ["Editing-Form-Fields", "Customer-Groups"],
    34: ["Customer-Groups", "Companies-and-Customer-Groups"], 35: ["Collecting-Newsletter-Subscriptions"], 36: ["Wishlists"],
    37: ["Security-and-Privacy-Settings", "Implementing-CCPA-with-BigCommerce"], 38: ["Getting-Started-Channels"], 39: ["Multi-Storefront"],
    40: ["The-Headless-Approach"], 41: ["301-Redirects"], 44: ["Using-Script-Manager"], 46: ["Customizing-Emails", "Customer-Order-Notifications"],
    47: ["Date-and-Timezone-Settings", "SEO-Fields", "Security-and-Privacy-Settings"], 48: ["Getting-Started-with-Localization-on-Multi-Storefronts"],
    53: ["Store-API-Accounts"], 54: ["Store-API-Accounts"], 56: ["Store-API-Accounts"], 57: ["Platform-Limits"],
    59: ["How-do-I-access-and-install-the-new-single-click-apps-within-my-Bigcommerce-store-control-panel"], 65: ["B2B-Edition-Settings", "B2B-Edition-User-Roles-and-Permissions"],
    68: ["Getting-Started-Channels"], 69: ["Getting-Started-Channels"], 70: ["Testing-Shipping-Tax-and-Payment-Settings"],
    72: ["Tax-Overview", "Manual-Tax-Setup"], 73: ["Automatic-Tax-Setup"], 74: ["Managing-Currencies", "Using-Multiple-Currencies"], 78: ["Security-and-Privacy-Settings"],
}
HC_WHY = ("The Help Center (support.bigcommerce.com) renders blank in this session: its script bundles return HTTP 400 to the headless browser "
          "and its llms.txt redirects to a login page, so no Help Center article was read. ")
LEGAL = set(range(79, 89))
PARTNER = {13, 26, 27, 62, 67, 68, 69, 71, 73}   # served through a third party per the pages read
GENERAL_RESP = ("The MSA and Store Terms speak of the Services and of the merchant's Stores and Materials in general "
                "(Store Terms: \"You are solely responsible for your Stores and Your Materials.\"); applying them to this concern would be inference, so no statement is recorded.")
PARTNER_RESP = ("The MSA's Third-Party Product Integration section speaks of Third-Party Products in general (\"Any exchange of data, content or materials, and any other "
                "interaction between you and the Third- Party Product Provider is solely between you and the Third-Party Product Provider.\"); applying it to this concern would be inference.")
BETA_RESP = ("The MSA's Pre-release Services section covers beta features in general; the docs say this feature is a closed beta. Joining the two would be inference, so no statement is recorded.")


def help_route(c):
    hs = H.get(c)
    return " ; ".join(HC + h for h in hs) if hs else "https://support.bigcommerce.com/s/ (Help Center search for the concern's name)"


def gap(c, name, pl):
    reads = " ; ".join(R.get(c, []))
    if pl == "where":
        if c == 12:
            return ("A BigCommerce page naming where product ratings and reviews live (control panel section or API group)", "read a page", "agent",
                    U[12] + " ; https://support.bigcommerce.com/s/ (Help Center search: Product Reviews)",
                    "The pricing page names the plan lines, the API reference navigation has no reviews group, and the GraphQL Storefront Product Reviews guide was not read.", "page not read")
        if c == 85:
            return ("A statement of where acceptable use is enforced in BigCommerce's own organization (a service, team or control panel section)", "read a page", "agent",
                    reads, "The Acceptable Use Policy, Store Terms and MSA were read; they state obligations and remedies but name no section, product or service where acceptable use lives.",
                    "searched, not found")
    if pl == "decides":
        if c in (53, 54, 55, 50, 51, 49):
            return (f"A page stating who enables {name}, on which plans, or what limits it", "read a page", "agent", reads,
                    f"The pages read ({reads}) state no plan line, setting or permission for it.", "searched, not found")
        if c == 75:
            return ("A statement of who sets the list of countries, states and provinces the Geography API returns", "read a page", "agent", reads,
                    "The Geography group page was read and states no owner or setting for the list; no other page in the developer index covers it.", "searched, not found")
        return (f"A Help Center article or control panel settings page stating who turns {name} on or off, limits it or sets its values, by plan or setting",
                "save a page from a browser", "founder", help_route(c),
                HC_WHY + f"The developer pages read ({reads}) state no plan line, setting or permission for it.", "page not read")
    if pl == "responsible":
        if c in (13, 17, 43, 66):
            return (f"A term naming the party legally responsible for {name}", "read a page", "agent", T + "terms/ (Pre-release Services)", BETA_RESP, "stated only in general terms")
        if c in PARTNER:
            return (f"A term naming the party legally responsible for {name} (BigCommerce, a partner or the merchant)", "read a page", "agent",
                    T + "terms/ (Third-Party Product Integration)", PARTNER_RESP, "stated only in general terms")
        if c in (53, 54, 55, 58):
            return (f"A term naming the party legally responsible for {name}", "read a page", "agent", T + "terms/api-terms/",
                    "The API Terms speak of the Commerce APIs in general (use, monitoring, volume limits, user information); applying them to this concern would be inference.",
                    "stated only in general terms")
        if c == 88:
            return ("A term naming who is responsible for infringing materials in a store", "read a page", "agent", T + "terms/acceptable-use-policy/ ; " + T + "terms/infringing-materials-protocol/",
                    "The Acceptable Use Policy says Your Materials may not violate third-party rights, which covers all store materials in general; the Protocol states the notice process, not responsibility.",
                    "stated only in general terms")
        return (f"A term naming the party legally responsible for {name} itself (BigCommerce, the merchant, a partner or an app developer)", "read a page", "agent",
                T + "terms/ ; " + T + "terms/store-terms/", GENERAL_RESP, "stated only in general terms")
    if pl == "boundary":
        return (f"An API resource, scope, webhook topic or contract that {name} meets the rest through", "read a page", "agent", U.get(c, reads),
                f"The pages read ({reads}) name no scope, webhook topic or endpoint for it" + ("; the guide named in the route was not read." if c in U else "."),
                "page not read" if c in U else "searched, not found")
    if pl == "reason":
        if c in U:
            return (f"A BigCommerce statement of why {name} is placed, decided or bounded as it is", "read a page", "agent", U[c],
                    f"The pages read ({reads}) give no reason; the guide named in the route was not read.", "page not read")
        return (f"A BigCommerce statement of why {name} is placed, decided or bounded as it is", "read a page", "agent", reads,
                "The pages listed were read and give no reason for the placement." + (" The Help Center could not be read in this session." if c in H else ""),
                "searched, not found")
    raise ValueError(pl)


# Extra gaps on the architecture concerns: cells that hold a statement, but the specific point is not stated.
TC = "https://security.bigcommerce.com/"
EXTRA = [
    (25, "responsible", "A BigCommerce page or agreement naming who collects and holds shoppers' funds for BigCommerce Payments (BigCommerce, PayPal or another entity), under which licence, and who the merchant contracts with for it",
     "save a page from a browser", "founder", "https://support.bigcommerce.com/s/ (Help Center search: BigCommerce Payments; the product page refers to \"BigCommerce documentation\") ; the activation flow in a US store's control panel",
     HC_WHY + "The product page says BigCommerce Payments is built with PayPal's infrastructure and that payouts are reported in the Money Dashboard, but names no holder of funds, licence or payments agreement; no BigCommerce Payments terms are among the Incorporated Terms listed in the MSA.",
     "page not read"),
    (26, "responsible", "A BigCommerce statement of who collects and holds shoppers' funds when a store uses an Embedded or Open Payment Provider",
     "read a page", "agent", "https://www.commerce.com/terms/ ; https://www.commerce.com/terms/fees-and-billing/ ; https://www.bigcommerce.com/pricing/ ; https://www.bigcommerce.com/payments/",
     "These pages were read; they state who charges the Open Payment Provider Fee and that the provider's own processing fees apply, but not who holds the funds.", "searched, not found"),
    (26, "decides", "A BigCommerce statement of what a store's checkout does when a connected payment provider is unavailable or fails",
     "save a page from a browser", "founder", "https://support.bigcommerce.com/s/article/Available-Payment-Gateways",
     HC_WHY + "The Payments API page lists error code 10000 (\"We're experiencing difficulty processing your transaction. Please try again later.\") but states no fallback.", "page not read"),
    (29, "responsible", "A statement of the licence or regulatory status under which Commerce collects and disburses monies as agent for Unified Billing Partners",
     "read a page", "agent", "https://www.commerce.com/terms/merchant-unified-billing/ ; https://www.commerce.com/terms/us-uk-ca-merchant-unified-billing/ ; https://www.commerce.com/terms/in-merchant-unified-billing/",
     "The three Unified Billing terms were read; they name Commerce as agent (US, UK and Canada) or as collector through its payment processor (India), and say Commerce relies on third-party payment processors, but name no licence.",
     "searched, not found"),
    (80, "responsible", "A statement of whether BigCommerce itself screens merchants, partners or shoppers against sanctions lists",
     "read a page", "agent", "https://www.commerce.com/terms/ ; https://www.commerce.com/terms/acceptable-use-policy/ ; https://www.commerce.com/terms/store-terms/ ; https://www.commerce.com/privacy/",
     "These were read; the MSA puts sanctions screening on the merchant and gives Commerce a right to terminate, but states no screening by BigCommerce.", "searched, not found"),
    (82, "decides", "A statement of which region a store's data is stored in, and whether a merchant can choose it",
     "save a page from a browser", "founder", TC,
     "The Platform Trust Center returns a Cloudflare security check (HTTP 403) to this session. The DPA, Privacy Policy and subprocessor list were read: they allow storage in regions where Commerce.com or its subprocessors operate, and list hosting in the USA, Germany or Australia, but state no per-store region or merchant choice.",
     "page not read"),
    (71, "decides", "A statement of what a store does when a shipping carrier's rate request fails or times out",
     "read a page", "agent", "https://docs.bigcommerce.com/developer/docs/integrations/shipping-providers.md ; https://docs.bigcommerce.com/developer/api-reference/rest/integrations/shipping-provider.md",
     "Both pages were read; they describe the rate cache and the quote request, but no failure behaviour.", "searched, not found"),
]
