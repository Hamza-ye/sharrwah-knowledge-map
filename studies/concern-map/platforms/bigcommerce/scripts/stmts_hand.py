# Hand-copied statements (verbatim from the working copies; checked by qcheck.py, then by the checker on the capture).
MSA = "c:terms/"
PAY = "d:admin/checkout-and-cart/payments/overview"
PCI = "d:storefront/headless/pci-compliance"
BCP = "w:payments/bigcommerce-payments/"
PRICE = "w:pricing/"
FEES = "c:terms/fees-and-billing/"
DPA = "c:privacy/data-processing-addendum/"
PRIV = "c:privacy/"
SUBP = "c:privacy/data-processors/"
CUR = "d:admin/store-configuration/currencies/overview"
TAXS = "a:rest/admin/management/tax/tax-settings/update-tax-settings"
TAXP = "d:integrations/tax-providers"
HOOKS = "d:integrations/webhooks/overview"
RATE = "d:overview/api-fundamentals/rate-limits"
ACC = "d:overview/api-fundamentals/api-accounts"
LL = "llms_dev"


def hand(S):
    # ---------- 1-3 catalog ----------
    S(64, "where", "w:product/", "All Features: AI & agentic commerce", "Product page: All Features", "BigCommerce Companion",
      "BigCommerce Companion Use an AI assistant embedded directly into the control panel to help manage your business.")
    S(64, "where", "w:product/", "All Features: AI & agentic commerce", "Product page: All Features", "BigAI",
      "BigAI Create product descriptions faster with AI-powered content generation and SEO optimization.")
    # ---------- 6 pickup ----------
    S(6, "where", "w:product/", "All Features: Omnichannel & growth", "Product page: All Features", "Buy online, pick up in store",
      "Buy online, pick up in store Connect inventory and fulfillment across physical and digital channels.")
    # ---------- 12, 13, 17 ----------
    S(13, "where", LL, "## API Docs: Beta Product Recommendations", "Developer docs index (llms.txt), API Docs", "Beta Product Recommendations > Product Recommendations",
      "Beta Product Recommendations > Product Recommendations Update Google Vertex Ai Settings")
    S(17, "where", LL, "## API Docs: Beta Checkout Extensions", "Developer docs index (llms.txt), API Docs", "Beta Checkout Extensions > Extensions",
      "Beta Checkout Extensions > Extensions Create Extension")
    S(43, "where", LL, "## API Docs: Beta Page Widgets", "Developer docs index (llms.txt), API Docs", "Beta Page Widgets > Page Widgets",
      "Beta Page Widgets > Page Widgets Publish or Overwrite Page Content")
    S(66, "where", LL, "## API Docs: Beta Powered By", "Developer docs index (llms.txt), API Docs", "Beta Powered By > Stores",
      "Beta Powered By > Stores Create Store")
    S(66, "boundary", LL, "## API Docs: Beta Powered By", "Developer docs index (llms.txt), API Docs", "Beta Powered By > Plans",
      "Beta Powered By > Plans Create Store Plan Change")
    S(66, "where", "w:payments/", "Platform menu: Partners", "BigCommerce site menu", "Powered By",
      "Powered By Resell ecommerce with Commerce-as-a-Service.")

    # ---------- 16 checkout ----------
    S(16, "where", "d:admin/checkout-and-cart/open-checkout/pciguide", "Step 2", "Developer docs: Configuring Open Checkout to comply with PCI DSS 4.0",
      "Settings > Checkout", "In the control panel, navigate to *Settings > Checkout*, and select *Custom Checkout*.")
    S(16, "responsible", MSA, "Security: Checkout Environment; PCI", "Master Services Agreement", "Checkout Environment; PCI",
      "For example, you will be solely liable for PCI compliance with respect to modifications to the checkout environment, including modifications via apps or a developer")

    # ---------- 18-21 orders ----------
    S(18, "where", "w:product/", "All Features: Operations & catalog", "Product page: All Features", "Order management",
      "Order management Manage orders from every channel in a single location.")
    S(20, "decides", "d:admin/checkout-and-cart/payments/transactions-api", "## Prerequisites", "Developer docs: Transactions API", "Transactions API prerequisites",
      "The payment provider must be enabled and configured with the same channel and currency that the order is placed against.")
    S(20, "reason", "d:admin/checkout-and-cart/payments/transactions-api", "## Prerequisites", "Developer docs: Transactions API", "Transactions API prerequisites",
      "This is because the payment provider ID is stored against the transaction at time of creation.")
    S(20, "responsible", "d:admin/checkout-and-cart/payments/transactions-api", "## Prerequisites", "Developer docs: Transactions API", "Provider configuration required",
      "If the payment provider is not configured in BigCommerce when the transaction is created, no provider ID will be stored")
    S(21, "boundary", PAY, "## FAQ: Can I issue a refund?", "Developer docs: Payments API", "Refunds API",
      "You can issue a refund using the store control panel (Help Center), the Refunds API, or through the payment gateway directly.")
    S(21, "where", "w:product/", "All Features: Checkout & payments", "Product page: All Features", "Refunds & returns",
      "Refunds & returns Create a smoother post-purchase experience with flexible returns and refund workflows.")

    # ---------- 22 payment processing ----------
    S(22, "where", PAY, "Payments API (introduction)", "Developer docs: Payments API", "https://payments.bigcommerce.com/stores/{{STORE_HASH}}/payments",
      "Process the payment: https://payments.bigcommerce.com/stores/{{STORE_HASH}}/payments")
    S(22, "where", "a:rest/admin/payments", "Payment Processing (introduction)", "API reference: Payment Processing", "BigCommerce Payments Gateway",
      "Also note that payment processing requests use the BigCommerce Payments Gateway, which uses a different server than our other REST APIs.")
    S(22, "responsible", PAY, "## PCI compliance", "Developer docs: Payments API", "PCI compliance",
      "BigCommerce is only responsible for the security of payment methods while the payment is en route from payment request to payment processor. As a third-party developer, you are responsible for developing your applications in a PCI-compliant manner.")
    S(22, "decides", PAY, "## FAQ: Can I add my payment gateway?", "Developer docs: Payments API", "compatible payment gateways",
      "The Payments API does not support using gateways that are not on the list of compatible payment gateways.")
    S(22, "decides", PAY, "## Technical details: Authorization", "Developer docs: Payments API", "Authorization",
      "If you configure a payment gateway for authorization only, authorization happens at the time of processing. You will need to capture the order later using the control panel or the Capture API.")
    S(22, "boundary", PAY, "## Technical details: Token", "Developer docs: Payments API", "payment_access_token",
      "The payment_access_token is not from the payment provider. It is created by BigCommerce.")
    S(22, "reason", PAY, "Implementation note", "Developer docs: Payments API", "3D Secure",
      "Because requests to our Payments API must be initiated in a server-to-server context rather than from the storefront, any 3D Secure-enabled card must first be saved during a shopper-initiated transaction and then charged as a stored payment instrument.")
    S(22, "boundary", PAY, "## FAQ: Are offline payment methods supported?", "Developer docs: Payments API", "offline payment methods",
      "The Payments API processes credit card payments through supported payment gateways; it does not expose methods for processing offline payment methods (Help Center) such as cash on delivery.")

    # ---------- 23, 24 ----------
    S(23, "decides", "a:rest/admin/payments/methods", "Payment Methods (introduction)", "API reference: Payment Methods", "Payment Methods V3",
      "Use V3 for any new integration. The V2 endpoint is preserved for compatibility with existing integrations that haven't yet migrated.")
    S(24, "boundary", "a:rest/admin/payments/stored-instruments", "Stored Instruments API (introduction)", "API reference: Stored Instruments API (Beta)", "payments.bigcommerce.com",
      "Payments server (payments.bigcommerce.com) — For PCI-compliant operations that handle raw card data, such as attaching an instrument to a customer. Authenticate with a Bearer instrument access token (IAT).")
    S(24, "decides", PAY, "## Error codes: 30002", "Developer docs: Payments API", "30002",
      "Vaulting service is currently not available. | The vaulting feature is not enabled on this store.")

    # ---------- 25 BigCommerce Payments ----------
    S(25, "where", BCP, "Native features", "BigCommerce Payments product page", "BigCommerce Payments by PayPal",
      "Built with PayPal's infrastructure, which manages PCI compliance and risk controls so your team can focus on selling, not on maintaining payment security.")
    S(25, "where", BCP, "FAQs: How do balance and payouts work?", "BigCommerce Payments product page (raw HTML)", "Money Dashboard",
      "Balance and payout reporting are handled natively inside your BigCommerce admin through the Money Dashboard.")
    S(25, "decides", BCP, "FAQs: Where is it available?", "BigCommerce Payments product page (raw HTML)", "BigCommerce Payments availability",
      "Initially, BigCommerce Payments is available only to US-based merchants with self-serve and retail plans.", "US-based merchants with self-serve and retail plans")
    S(25, "decides", "w:payments/", "BigCommerce Payments by PayPal", "Payments page", "BigCommerce Retail Plan",
      "*Must be on BigCommerce Retail Plan to qualify")
    S(25, "decides", BCP, "Pricing that scales with you", "BigCommerce Payments product page", "Card processing rate",
      "Core Card processing rate: 2.89% + $0.30 Growth Card processing rate: 2.59% + $0.30 Scale & Performance Card processing rate: 2.39% + $0.30",
      "eligible US merchants", "The page adds: Rates apply to eligible US merchants.")
    S(25, "responsible", BCP, "FAQs: Is it secure and PCI compliant?", "BigCommerce Payments product page (raw HTML)", "PCI compliance",
      "Yes. BigCommerce Payments is built with PayPal's infrastructure, which manages PCI compliance and risk controls at the platform level, so your team doesn't have to.")
    S(25, "boundary", BCP, "Getting started: Go live in four steps", "BigCommerce Payments product page", "Configure",
      "Configure Add your bank account and set payment preferences.")
    S(25, "boundary", PAY, "## Compatible payment gateways", "Developer docs: Payments API", "BigCommerce Payments",
      "BigCommerce Payments | ✓ | ✓", note="Row of the compatible payment gateways table: Stored instruments, Raw card data.")
    S(25, "reason", BCP, "FAQs: We already use another payment provider", "BigCommerce Payments product page (raw HTML)", "BigCommerce Payments",
      "It's a native experience where your payments data lives alongside your orders and payouts in one place, reducing the operational overhead of managing a separate tool.")
    S(25, "where", "w:pricing/", "Embedded Payment Provider List", "Pricing page (raw HTML)", "Embedded Payment Provider List",
      "Embedded Payment Provider List* BigCommerce Payments Adyen Affirm")

    # ---------- 26 payment providers ----------
    S(26, "where", "w:payments/", "More ways to get paid", "Payments page", "pre-integrated online payment solutions",
      "Choose from more than 65 pre-integrated online payment solutions, serving 150+ countries and over 140 currencies.")
    S(26, "decides", PRICE, "How the Open Payment Provider Fee Works", "Pricing page (raw HTML)", "Open Payment Provider Fee",
      "BigCommerce charges a monthly fee on self-service plans (Core, Growth, and Scale) for orders processed through Open Payment Providers.")
    S(26, "decides", PRICE, "Embedded Payment Provider List", "Pricing page (raw HTML)", "Embedded Payment Provider List",
      "*This list reflects our current Embedded Payment Provider program and may change over time.")
    S(26, "responsible", FEES, "Open Payment Provider Fees", "Fees and Billing Terms", "Open Payment Provider Fees",
      "For the avoidance of doubt, Open Payment Provider Fees are charged by Commerce, not by Customer’s payment gateway or payment provider, and are separate from any fees charged by such payment gateway or payment provider.")
    S(26, "decides", PRICE, "PayPal Braintree rate", "Pricing page", "PayPal Braintree",
      "Application for a PayPal Braintree account does not guarantee approval. Periodically, PayPal Braintree reviews its customer accounts to make sure its services and rates fit your account activity.",
      "United States-based business")
    S(26, "decides", PRICE, "PayPal Braintree rate", "Pricing page", "PayPal Braintree",
      "Eligibility requires that you must be a United States-based business.", "United States-based business")
    S(26, "where", "w:payments/gateways/", "Supporting payments across the globe", "Payment gateways page", "Choose Your Region",
      "Click your country from the list of regions below to get connected — we’ve partnered with leading payment companies across the world to ensure that you have the right local options.",
      note="The regions listed are North America, Asia-Pacific, Europe and Latin America, with 31 countries under them (raw HTML).")
    S(26, "responsible", "w:product/", "FAQ: Does BigCommerce charge payment fees?", "Product page (raw HTML)", "Embedded Payment Providers",
      "BigCommerce does not charge payment fees on orders processed through eligible Embedded Payment Providers. Standard payment processing fees from your chosen payment provider still apply.")

    # ---------- 27 wallets ----------
    S(27, "where", "w:product/", "All Features: Checkout & payments", "Product page: All Features", "Digital wallets",
      "Digital wallets Support PayPal, Venmo, PayPal Pay Later, Klarna, Afterpay, Apple Pay, and Google Pay, with accelerated checkout options.")
    S(27, "boundary", PAY, "Payments API (introduction)", "Developer docs: Payments API", "wallet-type providers",
      "The API flow does not support hosted, offsite, or wallet-type providers like Amazon Pay.")

    # ---------- 28 PCI ----------
    S(28, "responsible", MSA, "Security: Payment Cards", "Master Services Agreement", "Payment Cards",
      "Commerce is responsible for the security of credit cardholder data to the extent that Commerce has control of that data.")
    S(28, "responsible", MSA, "Security: Payment Cards", "Master Services Agreement", "Payment Cards",
      "You represent and warrant that you will determine the PCI merchant requirements applicable to you and your use of the Services.")
    S(28, "decides", MSA, "Security: Checkout Environment; PCI", "Master Services Agreement", "PCI Compliance Condition",
      "(i) you comply with Commerce documentation and in-product notifications, and (ii) you use a Commerce checkout environment that has not been modified except through the Commerce control panel.")
    S(28, "responsible", PCI, "## Who is responsible", "Developer docs: PCI Compliance", "PCI DSS Attestation of Compliance (AOC)",
      "BigCommerce is a PCI DSS compliant service provider and validates annually all requirements (1-12) including as a shared hosting provider.")
    S(28, "reason", MSA, "Security: Checkout Environment; PCI", "Master Services Agreement", "Checkout Environment; PCI",
      "Commerce will provide a secure environment (including appropriate technical, physical and organizational security measures and safeguards) for customer data stored and processed via the standard Commerce checkout (\"Customer Data\") in order to protect Customer Data from unauthorized access and use.")
    S(28, "boundary", PCI, "## Who is responsible", "Developer docs: PCI Compliance", "SAQs",
      "If your application handles credit card data, you will need to be PCI compliant. Submit self-assessment questionnaires (SAQs) to compliance@bigcommerce.com.")

    # ---------- 29 Unified Billing ----------
    S(29, "where", "d:integrations/apps/unified-billing/overview", "Unified Billing Overview", "Developer docs: Unified Billing Overview", "Unified Billing",
      "Unified Billing allows merchants to buy apps through the BigCommerce App Marketplace and have the charges included on their BigCommerce invoice.")
    S(29, "boundary", "d:integrations/apps/unified-billing/overview", "## Authentication", "Developer docs: Unified Billing Overview", "GraphQL Account API",
      "The Unified Billing GraphQL API uses Account-Level API tokens for authentication.")
    S(29, "responsible", "c:terms/us-uk-ca-merchant-unified-billing/", "Opt-in and Opt-out", "Merchant Unified Billing (United States, United Kingdom, and Canada Only)", "Unified Billing Partner",
      "Effective upon opt-in, you acknowledge that the Unified Billing Partners have appointed Commerce as agent for the collection and disbursement of monies, in the name of the Unified Billing Partners",
      "United States, United Kingdom, and Canada")
    S(29, "responsible", "c:terms/us-uk-ca-merchant-unified-billing/", "Payment Terms: Collection and Distribution", "Merchant Unified Billing (United States, United Kingdom, and Canada Only)", "Collection and Distribution",
      "those amounts received by Commerce shall be treated as received by the Unified Billing Partner directly so that the Unified Billing Merchant’s obligation is extinguished and there is no risk of loss to the Unified Billing Merchant if Commerce fails to distribute the funds to the Unified Billing Partners.",
      "United States, United Kingdom, and Canada")
    S(29, "boundary", "c:terms/us-uk-ca-merchant-unified-billing/", "Opt-in and Opt-out", "Merchant Unified Billing (United States, United Kingdom, and Canada Only)", "third-party payment processors",
      "Commerce is acting only for the Unified Billing Partners and does not act for you in collecting and disbursing such monies and Commerce will not process any payments directly, and it will rely on third-party payment processors to handle all payments made by you to Unified Billing Partners.",
      "United States, United Kingdom, and Canada")
    S(29, "responsible", "c:terms/in-merchant-unified-billing/", "Opt-in and Opt-out", "Merchant Unified Billing (India Only)", "Unified Billing Apps",
      "Effective upon opt-in, Commerce, through its payment processor, shall collect the funds from you for Unified Billing App purchases made by you on or through the Website and/or Commerce Marketplace", "India")
    S(29, "responsible", "c:terms/in-merchant-unified-billing/", "Invoicing", "Merchant Unified Billing (India Only)", "Invoicing",
      "Unified Billing Merchants shall be invoiced by Commerce for Unified Billing App purchases made by you on or through the Website and/or Commerce Marketplace.", "India")
    S(29, "responsible", "c:terms/merchant-unified-billing/", "Opt-in and Opt-out", "Merchant Unified Billing", "Unified Billing Partner",
      "Effective upon opt-in, you acknowledge that the Unified Billing Partners have appointed Commerce as agent for the collection and disbursement of monies, in the name of the Unified Billing Partners, for your purchases from the Unified Billing Partners processed on or through the Website and/or the Commerce Marketplace")
    S(29, "decides", "c:terms/merchant-unified-billing/", "Opt-in and Opt-out", "Merchant Unified Billing", "Opt-in and Opt-out",
      "You opt into unified billing by purchasing, on or through the Website and/or the Commerce Marketplace, goods from a Unified Billing Partner.")
    S(29, "decides", "d:integrations/apps/unified-billing/overview", "## Requirements and limitations", "Developer docs: Unified Billing Overview", "Partner Portal Account",
      "A Partner Portal Account with approved Partner status.")
    S(29, "reason", "w:apps/", "One platform. One invoice.", "Apps & Integrations page", "Unified Billing badge",
      "Any apps with the Unified Billing badge roll every charge into a single BigCommerce invoice. Less admin, cleaner books, zero surprises.")

    # ---------- 30 fees and billing ----------
    S(30, "where", FEES, "Fees", "Fees and Billing Terms", "Fees",
      "Fees may include subscription fees, GMV overage fees, Open Payment Provider Fees, and any other fees described on the Website or in an applicable Order.")
    S(30, "decides", FEES, "Upgrades/Downgrades: Automatic Upgrades", "Fees and Billing Terms", "Automatic Upgrades",
      "If you do not qualify for your then-current Service plan, then Commerce may automatically upgrade you to a Service plan for which you do qualify.")
    S(30, "decides", PRICE, "How Scale plan pricing works", "Pricing page", "Scale",
      "Once TTM GMV reaches $2 million, the account will automatically upgrade to Performance.", "Scale plan")
    S(30, "responsible", FEES, "Taxes", "Fees and Billing Terms", "Taxes",
      "You will be responsible for the payment of all Taxes applicable to your use of the Services.")
    S(30, "boundary", FEES, "Authorized Payment Method", "Fees and Billing Terms", "Authorized Payment Method",
      "You authorize Commerce to charge all fees (including GMV overage fees and Open Payment Provider Fees) to your authorized payment method on file")
    S(30, "decides", FEES, "Fees", "Fees and Billing Terms", "Fees",
      "Fees are payable in U.S. Dollars, unless otherwise specified.")
    S(30, "decides", "c:terms/jurisdiction-specific-terms/", "EMEA: Late Payments", "Jurisdiction-Specific Terms", "Late Payments",
      "If Service fees are not paid on the Billing Date, interest will accrue on such outstanding fees at the rate of 8% above the European Central Bank’s base rate per annum.",
      "Customers domiciled within the European Union or the United Kingdom")

    # ---------- 31 B2B invoices and payments ----------
    S(31, "decides", "a:rest/b2b/management/payment", "Payments (introduction)", "API reference (B2B Edition): Payments", "Company payment methods",
      "Every payment method you have enabled on the store-level can be enabled or disabled as needed on the Company level.")
    S(31, "where", "w:product/", "All Features: B2B commerce", "Product page: All Features", "Invoicing & net terms",
      "Invoicing & net terms Support invoices, net terms, credit limits, and B2B purchasing workflows.")

    # ---------- 33 customer login ----------
    S(56, "decides", ACC, "### Store-level API accounts", "Developer docs: API Accounts", "Settings > Store-level API accounts",
      "Merchants generate single-store API credentials when they create API accounts in their store control panel, in the Settings > Store-level API accounts menu.")

    # ---------- 38-40 channels, MSF, sites ----------
    S(38, "where", "a:rest/admin/management/channels", "## Channels", "API reference: Channels", "channel",
      "A channel is anywhere a merchant sells their products. This encompasses headless storefronts, marketplaces, POS systems, and marketing platforms.")
    S(38, "boundary", "a:rest/admin/management/channels", "### Platform", "API reference: Channels", "type and platform",
      "A channel's type and platform combination must be a valid pair as indicated in the table below.")
    S(39, "where", MSA, "Certain Definitions", "Master Services Agreement", "Multi-Storefront",
      "“Multi-Storefront” or “MSF” means the ability to manage multiple unique Storefronts within one Store. A Multi-Storefront enabled Store must meet additional requirements.")
    S(74, "decides", CUR, "## Adding a currency", "Developer docs: Currencies Overview", "MSF-enabled control panel",
      "Transactional currencies can't be created via API, so they'll need to be added via the active MSF-enabled control panel.")

    # ---------- 42 themes ----------
    S(42, "responsible", "c:terms/store-terms/", "Design Themes: Support", "Store Terms", "Design Themes",
      "Technical support for a design theme is the responsibility of the designer licensor, and Commerce does not accept any responsibility to provide such support.")
    S(42, "responsible", "c:terms/store-terms/", "Design Themes: Security Updates", "Store Terms", "Theme Components",
      "Commerce is not responsible for providing updates to themes developed by external developers.")
    S(42, "decides", "c:terms/store-terms/", "Design Themes: Multiple Stores", "Store Terms", "Multiple Stores",
      "This license only allows you to use each licensed Design theme for a single Store/website per license purchased.")

    # ---------- 50-52 Catalyst, Makeswift, Native Hosting ----------
    S(50, "where", LL, "## Docs: Catalyst", "Developer docs index (llms.txt)", "/developer/docs/storefront/catalyst/overview",
      "Catalyst is BigCommerce's composable, fully customizable headless ecommerce storefront framework, built with Next.js and the GraphQL Storefront API.")
    S(50, "where", "w:llms.txt", "## Products & Solutions (US/EN)", "www.bigcommerce.com llms.txt", "Catalyst (Storefront Framework)",
      "**Catalyst (Storefront Framework):** https://www.bigcommerce.com/product/catalyst/")
    S(51, "where", LL, "## Docs: Makeswift", "Developer docs index (llms.txt)", "/developer/docs/storefront/catalyst/makeswift/overview",
      "How Makeswift, BigCommerce's visual page builder, integrates with Catalyst, and which setup paths give you a Makeswift-connected project.")
    S(51, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "Makeswift, Inc.",
      "Makeswift, Inc. a Delaware Corporation in the United States New York Makeswift visual editor / builder")
    S(52, "where", "d:storefront/catalyst/deployment/native-hosting/overview", "Native Hosting Overview", "Developer docs: Native Hosting Overview", "Native Hosting",
      "BigCommerce provides hosting for your Catalyst projects, allowing you to fully deploy your Catalyst storefront without having to depend on an external hosting provider.")
    S(52, "reason", "d:storefront/catalyst/deployment/native-hosting/overview", "Native Hosting Overview", "Developer docs: Native Hosting Overview", "Native Hosting",
      "Native Hosting is the recommended way to host Catalyst: hosting and billing stay consolidated with your BigCommerce store, and you deploy, configure, and monitor your storefront entirely through the Catalyst CLI.")
    S(52, "boundary", "d:storefront/catalyst/deployment/native-hosting/overview", "### OpenNext", "Developer docs: Native Hosting Overview", "OpenNext Cloudflare adapter",
      "BigCommerce's hosting infrastructure uses the OpenNext Cloudflare adapter.")
    S(52, "decides", "d:storefront/catalyst/deployment/native-hosting/overview", "Warning", "Developer docs: Native Hosting Overview", "closed beta",
      "To express interest in gaining access, fill out the Native Hosting Closed Beta Interest Form.", note="The warning above it says Native Hosting is in closed beta.")

    # ---------- 53-57 APIs ----------
    S(53, "where", "a:graphql/overview", "GraphQL API Overview", "API reference: GraphQL API Overview", "Storefront API",
      "Storefront API — Query products, customers, and carts from the storefront.")
    S(54, "where", "a:graphql/overview", "GraphQL API Overview", "API reference: GraphQL API Overview", "Admin API",
      "Admin API — Query and mutate store data server-side.")
    S(55, "where", "a:graphql/overview", "GraphQL API Overview", "API reference: GraphQL API Overview", "Account API",
      "Account API — Manage account-level resources such as users.")
    S(55, "boundary", ACC, "### Account-level API accounts", "Developer docs: API Accounts", "Account-level API credentials",
      "Account-level API credentials provide direct access to all the account's stores, not just the store that was signed in at the time of creation.")
    S(56, "where", ACC, "## API accounts", "Developer docs: API Accounts", "API accounts",
      "BigCommerce offers three types of OAuth-based API accounts to developers who wish to use BigCommerce's REST APIs: store-level credentials, app-level credentials, and account-level credentials.")
    S(56, "decides", ACC, "### Store-level API accounts", "Developer docs: API Accounts", "Store-level API accounts",
      "You can't change store-level access tokens or OAuth scopes.")
    S(56, "boundary", ACC, "## OAuth scopes", "Developer docs: API Accounts", "default scope",
      "Webhooks are accessible from the default scope that is automatically accessible to all API accounts.")
    S(56, "reason", ACC, "## API accounts", "Developer docs: API Accounts", "OAuth scope",
      "It's best practice to limit each account's OAuth scope to only the privileges needed to complete that app or user's designated tasks.")
    S(56, "responsible", "c:terms/api-terms/", "User Information & Security: User Information", "API Terms", "User Information",
      "You will use commercially reasonable efforts to protect all information collected from Your Users (as defined in the Store Terms) through your API client from unauthorized access, use, or disclosure.")
    S(57, "decides", RATE, "## Rate limits by plan type", "Developer docs: API rate limits", "Pro",
      "Pro | 60k per hour (450 / 30sec)", "Pro plan")
    S(57, "decides", RATE, "## Rate limits by plan type", "Developer docs: API rate limits", "Plus & Standard",
      "Plus & Standard | 20k per hour (150 / 30sec)", "Plus and Standard plans")
    S(57, "decides", RATE, "### Unlimited rate plan", "Developer docs: API rate limits", "Unlimited Rate Plan",
      "The Unlimited Rate Plan is for some BigCommerce Enterprise clients. It has no request rate limits.", "some BigCommerce Enterprise clients")
    S(57, "where", RATE, "## Rate limits by plan type", "Developer docs: API rate limits", "quota",
      "Apps using OAuth are rate-limited based on a quota that's refreshed every 30 seconds.")
    S(57, "decides", RATE, "## Rate limits by plan type", "Developer docs: API rate limits", "quota",
      "The maximum quota varies by store plan and requested resources.")
    S(57, "boundary", RATE, "## How limits work", "Developer docs: API rate limits", "store quota",
      "All apps accessing the store share the store's quota.")
    S(57, "reason", RATE, "API rate limits (introduction)", "Developer docs: API rate limits", "rate limits",
      "BigCommerce aims to provide outstanding platform reliability. To ensure reliability, we implement safeguards in the form of rate limits for our REST APIs.")
    S(57, "responsible", "c:terms/api-terms/", "API Use, Monitoring, Volume Limits: Volume Limits", "API Terms", "Volume Limits",
      "You will not attempt to exceed or circumvent limitations on access, calls and use of the Commerce API")
    S(57, "boundary", RATE, "## Best practices", "Developer docs: API rate limits", "HTTP 429",
      "Process rate limit HTTP 429 status code accurately, distribute request loads evenly, store results, and repeat requests strategically to boost app performance and prevent outages.")

    # ---------- 58 webhooks ----------
    S(58, "decides", HOOKS, "## Callback retry mechanism", "Developer docs: Webhooks Overview", "is_active",
      "After the final retry attempt (cumulatively 48 hours after the first delivery attempt), the webhook will be deactivated, and an email will be sent to the email address registered for the subscribing app.")
    S(58, "decides", HOOKS, "## Callback retry mechanism", "Developer docs: Webhooks Overview", "blocklist",
      "If at any point in the two minute window the success/failure ratio dips below 90%, the destination URI's domain will be blocklisted for three minutes.")
    S(58, "reason", HOOKS, "## Platform limits", "Developer docs: Webhooks Overview", "Platform limits",
      "To maintain the performance, security, and reliability of the webhooks service, the following platform limits are in place.")
    S(58, "reason", HOOKS, "### Post app uninstall actions", "Developer docs: Webhooks Overview", "Post app uninstall actions",
      "To avoid accumulating unused webhooks, BigCommerce automatically deletes registered webhooks on app uninstall.")
    S(58, "boundary", HOOKS, "## Delivery mechanisms", "Developer docs: Webhooks Overview", "Delivery mechanisms",
      "BigCommerce delivers webhook events to the following endpoint types. Choose the delivery mechanism that best fits your architecture:")

    # ---------- 59 apps ----------
    S(59, "where", "d:integrations/apps/guide/types-of-apps", "Types of Apps", "Developer docs: Types of Apps", "single-click and connector",
      "The two types of apps, single-click and connector, are defined by the method of authentication.")
    S(59, "decides", "d:integrations/apps/guide/approval-requirements", "App Store Approval Requirements", "Developer docs: App Store Approval Requirements", "Marketplace team",
      "The Marketplace team reviews all app submissions and tests apps to verify they meet App Marketplace listing standards.")
    S(59, "decides", "d:integrations/apps/guide/types-of-apps", "## Visibility", "Developer docs: Types of Apps", "Unlisted",
      "Only approved partners can create unlisted apps.")
    S(59, "boundary", "d:integrations/apps/guide/types-of-apps", "## Single-Click", "Developer docs: Types of Apps", "Single-Click",
      "Once granted, the app can request a permanent access_token for making REST API requests on the user's behalf.")
    S(59, "responsible", MSA, "Third-Party Product Integration", "Master Services Agreement", "Third-Party Products",
      "If you install or enable a Third- Party Products for use with the Commerce’s Service, you grant us permission to allow the applicable Third-Party Product Provider to access your data and content and other materials")

    # ---------- 60-62 ----------
    S(60, "where", TAXP, "## Verifying your integration", "Developer docs: Tax Providers", "Settings > Advanced > Store logs",
      "If the connection is unsuccessful or the response contains errors, merchants can navigate to Settings > Advanced > Store logs in the control panel.")
    S(61, "where", "a:graphql/account/overview", "GraphQL Account API overview", "API reference: GraphQL Account API overview", "control panel users",
      "The GraphQL Account API's users feature lets you create, edit, and delete BigCommerce control panel users.")
    S(62, "where", "w:product/", "All Features: Enterprise & developers", "Product page: All Features", "Big Open Data Solutions",
      "Big Open Data Solutions Connect commerce data to BigQuery and leading analytics platforms including Tableau, Power BI, and Looker.")
    S(62, "decides", FEES, "Commerce Analytics", "Fees and Billing Terms", "Commerce Analytics",
      "Fees for the Commerce Analytics Service are charged in advance based on your store plan.")

    # ---------- 63-64 MCP, agentic, AI ----------
    S(63, "decides", "a:mcp/overview", "## Enable MCP on your store", "API reference: MCP Server Overview", "store owner",
      "You must be a store owner to enable MCP on a store.")
    S(63, "decides", "a:mcp/overview", "## Enable MCP on your store", "API reference: MCP Server Overview", "Storefront MCP",
      "On the MCP page, turn on the Storefront MCP toggle. Review and accept the terms of service to enable the MCP server for your store.")
    S(63, "where", "a:mcp/overview", "## Enable MCP on your store", "API reference: MCP Server Overview", "Settings > API and MCP > MCP",
      "In the BigCommerce control panel, go to Settings. Under API and MCP, select MCP.")
    S(63, "responsible", "w:product/", "All Features: AI & agentic commerce", "Product page: All Features", "Agentic checkout",
      "Agentic checkout Enable transactions within AI-powered shopping experiences while remaining merchant of record.")
    S(63, "boundary", "c:terms/ai-features-addendum/", "Agentic Search: Data Scope and Restrictions", "AI Features Addendum", "Agentic Search",
      "Only catalog-related data is processed under Agentic Search. No personally identifiable information (PII), checkout data, or customer order information is used unless otherwise agreed in writing.")
    S(63, "decides", "c:terms/ai-features-addendum/", "Agentic Search: Data Scope and Restrictions", "AI Features Addendum", "Agentic Search",
      "Customer may opt out of individual platforms by notifying Commerce.")
    S(64, "responsible", "c:terms/ai-features-addendum/", "AI (Third- Party) Enablement", "AI Features Addendum", "AI (Third- Party) Enablement",
      "The customer remains fully responsible for Third-Party Products including those which enable AI within or connected to the Service.")
    S(64, "decides", "c:terms/ai-features-addendum/", "AI Features Integrated into the Services: Modifications, Termination and Suspension", "AI Features Addendum", "AI Features",
      "Commerce may suspend, modify, or discontinue AI Features at any time.")
    S(64, "boundary", "c:terms/ai-features-addendum/", "AI Features Integrated into the Services: No Input Training", "AI Features Addendum", "No Input Training",
      "Commerce does not use Customer inputs to train its models and will ensure its third–party providers used to provide the AI Features do the same.")

    # ---------- 65 B2B ----------
    S(65, "where", "w:apps/", "Spotlight", "Apps & Integrations page", "B2B Edition",
      "B2B Edition provides enterprise level B2B features to extend the native B2B capabilities of BigCommerce.")
    S(65, "decides", "a:rest/b2b/overview", "B2B REST APIs", "API reference: B2B REST APIs", "B2B Edition enabled",
      "These APIs are available to stores with B2B Edition enabled.")

    # ---------- 67 Feedonomics ----------
    S(67, "where", MSA, "Certain Definitions", "Master Services Agreement", "Feedonomics Platform",
      "“Feedonomics Platform” means Feedonomics proprietary software which uses data to deliver the Services under this Agreement.")
    S(67, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "Feedonomics Holdings, LLC",
      "Feedonomics Holdings, LLC, a Delaware corporation in the United States New York Feedonomics Platform")

    # ---------- 70-71 shipping ----------
    S(71, "boundary", "a:rest/integrations/shipping-provider", "## Authentication", "API reference: Shipping Providers", "Shipping Providers",
      "This specification file describes API requests BigCommerce will make to a registered shipping carrierʼs server to check connection options and retrieve rates.")
    S(71, "decides", "a:rest/integrations/shipping-provider", "## Authentication", "API reference: Shipping Providers", "carrier server",
      "As such, the method of authentication is determined by the carrier server.")
    S(71, "boundary", "d:integrations/shipping-providers", "## Returning shipping quotes", "Developer docs: Shipping Providers", "Quote URL",
      "Whenever shipping rates are required, BigCommerce checks its internal cache for valid entries. BigCommerce uses valid entries and does not call the shipping carrier.")
    S(70, "where", TAXP, "## End-to-end testing", "Developer docs: Tax Providers", "Settings > Setup > Shipping",
      "The shipping origin address, found by navigating to Settings > Setup > Shipping, is configured.")
    S(70, "where", "w:product/", "All Features: Operations & catalog", "Product page: All Features", "Shipping",
      "Shipping Offer flexible shipping options, real-time rates, and fulfillment integrations.")

    # ---------- 72-73 tax ----------
    S(72, "decides", "d:admin/store-configuration/tax/tax-settings", "Tax Settings", "Developer docs: Tax Settings", "Tax settings",
      "Tax settings allow you to choose how a store handles tax calculation and price display. For example, you can set how a store handles taxes if an enabled tax service is unavailable.")
    S(72, "decides", TAXS, "Request body", "API reference: Update Tax Settings", "should_use_geolocation_to_determine_guest_shopper_tax_zone",
      "This setting determines which tax zone a store uses to estimate tax for guest shoppers.")
    S(72, "reason", "d:admin/store-configuration/tax/tax-settings", "## Estimate taxes and display prices based on tax zone", "Developer docs: Tax Settings", "Tax Settings API",
      "The Tax Settings API supports cross-border transactions. You can localize storefront prices for shoppers from different regions.")
    S(73, "where", TAXP, "## Configure tax provider settings in the control panel", "Developer docs: Tax Providers", "Settings > Setup > Tax",
      "Merchants can adjust these settings by navigating to Settings > Setup > Tax > *TaxProviderName* in the control panel.")
    S(73, "where", TAXP, "Tax Providers", "Developer docs: Tax Providers", "Tax Provider API",
      "The Tax Provider API works in conjunction with a BigCommerce app, so you will need to build an app that integrates the Tax Provider API.")
    S(73, "decides", TAXS, "Request body", "API reference: Update Tax Settings", "fallback_strategy",
      "Describes the fallback behavior that applies when a tax provider produces an error. A merchant may decide to use a flat 10% fallback tax rate, their basic tax settings, or to block the transaction until they achieve a successful result.",
      note="Allowed values: FIXED, BASIC, DISABLE; default FIXED.")
    S(73, "decides", TAXP, "### Tax provider visibility", "Developer docs: Tax Providers", "Tax provider visibility",
      "By default, a newly registered tax provider is visible only on the store that performed the registration.")
    S(73, "decides", TAXP, "## Configure tax provider settings in the control panel", "Developer docs: Tax Providers", "Settings > Setup > Tax",
      "Before you can provide tax estimates, the merchant must choose which regions they want you to service.")
    S(73, "reason", TAXP, "### Performance", "Developer docs: Tax Providers", "timeout",
      "To protect the shopper checkout experience from overly slow tax responses, tax estimate requests will time out after a set period of time.")
    S(73, "boundary", TAXP, "### Performance", "Developer docs: Tax Providers", "timeout",
      "The default timeout threshold of four seconds is intended to support a wide variety of use cases (e.g., large tax estimate requests).")
    S(73, "boundary", "a:rest/integrations/overview", "Provider APIs", "API reference: Provider APIs", "Provider APIs",
      "Provider APIs use a reverse data flow — BigCommerce calls *your* app's endpoints to retrieve data on behalf of a store.")
    S(73, "boundary", TAXS, "Request body", "API reference: Update Tax Settings", "document_submission_strategy",
      "This setting determines whether BigCommerce submits tax documents to third-party tax providers when orders are created or when payments are captured online.")

    # ---------- 74 currencies ----------
    S(74, "where", CUR, "## Adding a currency", "Developer docs: Currencies Overview", "Settings > Setup > Currencies",
      "Navigate to Settings > Setup > Currencies, then select Add a Currency")
    S(74, "decides", CUR, "## Active vs. Transactional", "Developer docs: Currencies Overview", "Transactional currency",
      "Transactional currency - When a currency is set as transactional, shoppers in associated countries will both see prices on the storefront in that currency and be charged in that currency when they check out.")
    S(74, "decides", CUR, "## Multi-currency definitions", "Developer docs: Currencies Overview", "Settlement Currency",
      "The merchant can set their settlement currency through its payment provider.")
    S(74, "responsible", CUR, "## Multi-currency definitions", "Developer docs: Currencies Overview", "Transactional Currency",
      "If there's a discrepancy between the storefront active currency and the transactional currency, a shopper has to pay a conversion fee and the conversion rate used is outside of BigCommerce's scope.")
    S(74, "responsible", CUR, "## Multi-currency definitions", "Developer docs: Currencies Overview", "Bank Conversion Rate",
      "This rate might not align with the BigCommerce conversion rate, and BigCommerce has no visibility into it.")
    S(74, "boundary", CUR, "## Multi-currency definitions", "Developer docs: Currencies Overview", "Transactional Currency",
      "the transactional currency is what BigCommerce passes to the payment provider and what is charged to a shopper's bank account.")
    S(74, "decides", CUR, "## Preconfiguring the store", "Developer docs: Currencies Overview", "multi-currency compatible payment gateway",
      "A multi-currency compatible payment gateway set up and enabled. (Your store's default currency can use any gateway).")
    S(74, "reason", CUR, "Currencies Overview", "Developer docs: Currencies Overview", "Multi-Currency",
      "Allowing customers to shop and check out in their native currency provides a more consistent and positive shopping experience, and maintaining price expectations throughout the shopping process encourages conversions for merchants.")
    S(74, "boundary", "d:admin/checkout-and-cart/payment-providers/stripe/integrating-stripe-adaptive-pricing", "Integrating Stripe Adaptive Pricing", "Developer docs: Integrating Stripe Adaptive Pricing", "Stripe Adaptive Pricing",
      "Stripe detects the shopper's currency, handles the FX conversion (24-hour rate guarantee), and renders a currency selector next to the payment methods.")
    S(74, "reason", "d:admin/checkout-and-cart/payment-providers/stripe/integrating-stripe-adaptive-pricing", "## How it works", "Developer docs: Integrating Stripe Adaptive Pricing", "Stripe OCS Checkout Session",
      "Your custom checkout listens for that flag and narrows the payment methods list to only the Stripe OCS Checkout Session method, because other gateways cannot settle in the presentment currency.")

    # ---------- 76-78 ----------
    S(76, "where", "w:product/", "All Features: Enterprise & developers", "Product page: All Features", "Staging environments",
      "Staging environments Test, preview, and deploy updates without disrupting live storefronts.")
    S(77, "decides", "c:terms/mobile-app-terms/", "License", "Mobile App Terms", "License",
      "Commerce grants you a revocable, non-exclusive, non-sublicensable, non-transferable, worldwide, limited license to install and use the Application solely in connection with your Account for so long as your Services subscription remains in effect")
    S(77, "responsible", "c:terms/mobile-app-terms/", "Compatibility; Performance", "Mobile App Terms", "Compatibility; Performance",
      "Use of the Application requires a compatible device with supported software and internet access. You are responsible for paying all fees associated with the foregoing.")
    S(78, "where", "w:product/secure-web-hosting/", "Certified Tier 1 security and compliance", "Hosting and Security page", "Tier 1 certifications",
      "We provide critical security and compliance for enterprise brands worldwide with an ever-growing list of Tier 1 certifications including ISO, SOC, PCI, FIPS, RH-ISAC, GDPR, and CCPA.")

    # ---------- 79 contracting entity ----------
    S(79, "responsible", MSA, "Contracting Entity", "Master Services Agreement", "Contracting Entity",
      "“Commerce” means the Commerce entity with which you are entering into this Agreement.")
    S(79, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "United States",
      "United States Commerce.com US, Inc., a Texas corporation in the United States New York Ecommerce Platform, Extensions, and certain Professional Services",
      "Country of Residence of Merchant: United States")
    S(79, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "United Kingdom",
      "United Kingdom Commerce Software UK Ltd., a United Kingdom limited company England and Wales", "Country of Residence of Merchant: United Kingdom")
    S(79, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "European Union",
      "European Union Commerce Software Ireland Ltd., an Irish limited company Ireland", "Country of Residence of Merchant: European Union")
    S(79, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "Australia",
      "Australia Commerce.com Pty. Ltd., an Australia proprietary limited company New South Wales, Australia", "Country of Residence of Merchant: Australia")
    S(79, "responsible", MSA, "Contracting Entity table", "Master Services Agreement", "Any other jurisdiction",
      "Any other jurisdiction Commerce.com Pty. Ltd., an Australia proprietary limited company New York Ecommerce Platform, Extensions, and certain Professional Services",
      "Country of Residence of Merchant: Any other jurisdiction")
    S(79, "responsible", "c:terms/jurisdiction-specific-terms/", "Germany: Contracting Entity", "Jurisdiction-Specific Terms", "Germany",
      "“Commerce” means the Commerce entity with which you are entering into this Agreement, i.e. Commerce Software Ireland Ltd, 32 Merrion Street Upper Dublin 2, D02KW80, Ireland, registration number 631113.",
      "Customers domiciled in Germany")
    S(79, "decides", MSA, "Governing Law; Jurisdiction", "Master Services Agreement", "Governing Law; Jurisdiction",
      "The law that will govern the validity and construction of this Agreement and apply in any dispute or lawsuit arising out of or relating to this Agreement is as set forth in table in the Contracting Entity Section above.")
    S(79, "boundary", MSA, "Arbitration Agreement and Class Action Waiver: Applicability", "Master Services Agreement", "Arbitration Agreement",
      "This Arbitration Agreement and Class Action Waiver (“Arbitration Agreement”) applies only to Customers domiciled in the United States.", "Customers domiciled in the United States")
    S(79, "where", MSA, "Master Services Agreement (preamble)", "Master Services Agreement", "Commerce.com US, Inc.",
      "This Master Services Agreement (\"Agreement\") is between Commerce.com US, Inc. and any of Commerce’s affiliates")

    # ---------- 80 sanctions ----------
    S(80, "responsible", MSA, "Anti-Corruption, Export and Sanctions Compliance", "Master Services Agreement", "Sanctions List",
      "are not, and will ensure that your Relevant Parties and customers are not, (a) nationals, residents, agents or representatives of Iran, Cuba, North Korea, Syria, the Crimea Region of Ukraine, or any other region subject to comprehensive U.S. sanctions")
    S(80, "responsible", MSA, "Anti-Corruption, Export and Sanctions Compliance", "Master Services Agreement", "sanctions screenings",
      "shall implement an effective, risk-based compliance program and necessary internal controls (including, but not limited to, conducting sanctions screenings of your Relevant Parties and customers)")
    S(80, "decides", MSA, "Anti-Corruption, Export and Sanctions Compliance", "Master Services Agreement", "material breach",
      "A violation of the foregoing representations, warranties, or covenants will constitute a material breach of this Agreement, and, in the event of such a violation, Commerce may, at its sole option, terminate this Agreement for cause")
    S(80, "boundary", MSA, "Anti-Corruption, Export and Sanctions Compliance", "Master Services Agreement", "cooperate with Commerce",
      "shall reasonably cooperate with Commerce to (a) ensure compliance with sanctions, embargoes, and other Applicable ABAC Laws")
    S(80, "where", MSA, "Anti-Corruption, Export and Sanctions Compliance", "Master Services Agreement", "Anti-Corruption, Export and Sanctions Compliance",
      "Anti-Corruption, Export and Sanctions Compliance. With respect to this Agreement, you represent, warrant, and covenant that you:")

    # ---------- 81 processing roles ----------
    S(81, "responsible", DPA, "Roles and Processing", "Data Processing Addendum", "Roles and Processing",
      "A Commerce Entity shall act as Processor and Process the Personal Data only to provide the Services, on Customer’s documented instructions, or as consistent with the Agreement or any underlying Agreement.")
    S(81, "responsible", PRIV, "Shoppers: Information Usage", "Privacy Policy", "Shoppers",
      "We use this information as a Processor to provide our services to Merchants, support and Process orders, and manage risk and fraud. The Merchant is the Controller of this information")
    S(81, "boundary", PRIV, "Shoppers", "Privacy Policy", "Shopper requests",
      "When appropriately identified, we can forward Shopper requests to Merchants, but we are unable to action the request.")
    S(81, "where", DPA, "OPERATION OF THIS DPA", "Data Processing Addendum", "Exhibit B",
      "Exhibit B (Commerce.com Specific Data Processing Terms) which applies only to Commerce.com Processing")
    S(81, "decides", DPA, "Data Processing Limitations", "Data Processing Addendum", "Data Processing Limitations",
      "Except as specifically provided in writing otherwise, the Services are not intended to store, use, or otherwise Process any type of Personal Data that may be considered “sensitive data” or “special categories of personal data” under Data Protection Laws")

    # ---------- 82 data transfer and location ----------
    S(82, "where", DPA, "Exhibit B: Data Transfer", "Data Processing Addendum", "Data Transfer",
      "Commerce.com may transfer, process and store Personal Data in regions in which Commerce.com or its Subprocessors operate, subject to compliance with Data Protection Laws.")
    S(82, "where", SUBP, "Commerce Third-Party Subprocessors: Google", "Third-Party Subprocessors", "Google",
      "Infrastructure hosting, document management, and communications Service delivery / product functionality for AI chatbots USA, Germany, or Australia")
    S(82, "where", SUBP, "Commerce Third-Party Subprocessors: Amazon", "Third-Party Subprocessors", "Amazon",
      "Amazon Analytics Data hosting Online store metrics Hosting customer / product catalog data, feed data, logs, etc. USA")
    S(82, "where", SUBP, "Commerce Third-Party Subprocessors: Cloudflare", "Third-Party Subprocessors", "Cloudflare",
      "Cloudflare DDoS mitigation, threat detection, and CDN DDoS protection, digital threats monitoring, and accelerated content delivery USA, with globally decentralized CDN")
    S(82, "where", PRIV, "Accountability and Safeguards for Onward Transfer: Data Transfer", "Privacy Policy", "Data Transfer",
      "To provide our services, it may be necessary to transmit Personal Data outside of the country, state, or province where the data was collected/received, including to the United States.")
    S(82, "boundary", DPA, "Exhibit B: Data Transfer", "Data Processing Addendum", "Data Privacy Frameworks",
      "Commerce.com is a participant in the EU-U.S. Data Privacy Frameworks as well as in the UK and Swiss Extension to the EU-U.S. Data Privacy Framework.")
    S(82, "boundary", DPA, "Exhibit B: Data Transfer", "Data Processing Addendum", "EU SCCs",
      "the Standard Contractual Clauses approved by the European Commission on 4 June 2021 under Commission Implementing Decision (EU) 2021/914")
    S(82, "decides", DPA, "Exhibit A: Integrity and Stability", "Data Processing Addendum", "Integrity and Stability",
      "Commerce.com infrastructure is logically segmented and replicated throughout multiple availability zones.")

    # ---------- 83 subprocessors and hosting ----------
    S(83, "responsible", MSA, "Hosting Services", "Master Services Agreement", "Hosting Services",
      "Commerce has entered into arrangements with one or more third parties for hosting services that are essential to the Services, incorporated within the Services and without which the Services could not be provided to you.")
    S(83, "decides", DPA, "Subprocessing: Additions; Replacement", "Data Processing Addendum", "Additions; Replacement",
      "This DPA is Customer’s general written authorization for a Commerce Entity to engage Subprocessors")
    S(83, "where", DPA, "Subprocessing", "Data Processing Addendum", "Subprocessors",
      "Commerce.com’s current Subprocessors are set forth at https://www.commerce.com/privacy/data-processors/, or its successor page.")
    S(83, "responsible", SUBP, "Footnote 2", "Third-Party Subprocessors", "Subprocessors",
      "a Commerce Entity does not transfer any PII to subprocessors without: (i) a security assessment, (ii) a privacy assessment, including an assessment of transfer impact; and (iii) a data protection agreement")
    S(83, "where", "w:product/secure-web-hosting/", "Industry leading uptime", "Hosting and Security page", "uptime",
      "With 100% uptime during Cyber Week since 2016 (and 99.98% since 2009), BigCommerce delivers peak performance, at peak times, for the world's most demanding brands.")
    S(83, "boundary", MSA, "Backup Storage", "Master Services Agreement", "Backup Storage",
      "IT IS SOLELY YOUR DUTY AND RESPONSIBILITY TO BACKUP SEPARATELY YOUR FILES AND DATA THAT MAY RESIDE ON COMMERCE SERVERS.")

    # ---------- 84 third-party products ----------
    S(84, "decides", MSA, "Third-Party Product Integration", "Master Services Agreement", "Third-Party Product Integration",
      "Commerce may, in its discretion and without liability to you, decide to no longer support such integration and migrate your Services subscription to a different integration.")
    S(84, "responsible", MSA, "Third-Party Product Integration", "Master Services Agreement", "Third-Party Product Provider",
      "Any exchange of data, content or materials, and any other interaction between you and the Third- Party Product Provider is solely between you and the Third-Party Product Provider.")
    S(84, "decides", MSA, "Third-Party Product Integration", "Master Services Agreement", "Third-Party Products",
      "Commerce does not guarantee the availability of Third-Party Products and you acknowledge that Commerce may disable access to any Third-Party Products at any time and for any reason in its sole discretion without notice to you.")
    S(84, "where", MSA, "Scope and Definitions: Scope", "Master Services Agreement", "Scope",
      "Except as otherwise specified, this Agreement does not apply to Third-Party Products, which are governed by their own terms of service.")
    S(84, "boundary", MSA, "Certain Definitions: Extension", "Master Services Agreement", "Extension",
      "For the avoidance of doubt, an Extension is a Service and is not a Third-Party Product.")

    # ---------- 85 AUP / regulated products ----------
    S(85, "responsible", "c:terms/acceptable-use-policy/", "Highly Regulated Products: Representations and Warranties", "Acceptable Use Policy", "Highly Regulated Products",
      "You acknowledge that Commerce makes no guarantees regarding the legality of products sold in specific jurisdictions, and it is your responsibility to verify compliance with all applicable laws.")
    S(85, "responsible", "c:terms/acceptable-use-policy/", "Highly Regulated Products: Disclaimer", "Acceptable Use Policy", "Disclaimer",
      "Commerce disclaims any responsibility for evaluating or confirming the legality of your products or services. You are solely responsible for ensuring that your products comply with applicable laws.")
    S(85, "decides", "c:terms/acceptable-use-policy/", "Prohibited Activities/Content: Lawful Purposes Only", "Acceptable Use Policy", "Lawful Purposes Only",
      "You may not use the Website or Services or allow any third party to use the Website or Services for any purpose that is determined by Commerce, in its discretion, to be unlawful, invasive, infringing, obscene, offensive, defamatory or fraudulent")
    S(85, "boundary", "c:terms/acceptable-use-policy/", "Highly Regulated Products: Disclaimer", "Acceptable Use Policy", "third-party service provider policies",
      "Commerce shall not be liable for any damages, losses, or liabilities related to regulatory changes or third-party service provider policies affecting regulated products or services.")

    # ---------- 86 stores and materials ----------
    S(86, "responsible", "c:terms/store-terms/", "Stores and Materials", "Store Terms", "Your Materials",
      "You are solely responsible for your Stores and Your Materials.")
    S(86, "responsible", "c:terms/store-terms/", "Compliance: Privacy Policy", "Store Terms", "Privacy Policy",
      "You will establish and follow a privacy policy that (a) complies with all Laws, (b) is readily accessible to Your Users, and (c) clearly discloses how you collect, use, share, secure, and disclose personal information.")
    S(86, "decides", "c:terms/store-terms/", "Remedies: Content Removal", "Store Terms", "Content Removal",
      "Commerce may do so and may remove any of your Stores or Your Materials it believes may be (or are alleged to be) in violation of any Laws, this Agreement or are otherwise objectionable or offensive in Commerce’s sole discretion.")
    S(86, "where", "c:terms/store-terms/", "Stores and Materials", "Store Terms", "Store",
      "A Store can be individually configured with its own settings, payment methods, and 3rd party apps.")
    S(86, "boundary", "c:terms/store-terms/", "Compliance: User Agreement", "Store Terms", "User Agreement",
      "You will enter into an agreement with Your Users that will include all pertinent provisions of the Agreement and release Commerce and its licensors from any and all liability for damages or losses Your Users may incur as a result of using your Stores.")

    # ---------- 87 agents ----------
    S(87, "responsible", "c:terms/merchant-client-terms/", "Agents: Representations and Warranties", "Merchant-Client Terms", "Agents",
      "You have the authority as agent for Client to bind Client to the Agreement.")
    S(87, "where", "c:terms/merchant-client-terms/", "Agents: Applicability", "Merchant-Client Terms", "Client",
      "In the event you use the Services for and on behalf of your third-party client (“Client”) (i.e., as an agent of Client), the following terms will apply.")
    S(87, "decides", "c:terms/merchant-client-terms/", "Agents: Notices", "Merchant-Client Terms", "Notices",
      "Any notices that Commerce is required to provide shall be provided to you and/or Client as determined by Commerce in its sole discretion")

    # ---------- 88 infringing materials ----------
    S(88, "where", "c:terms/infringing-materials-protocol/", "Protocol", "Infringing Materials Protocol", "Protocol",
      "Commerce complies with the provisions of the Digital Millennium Copyright Act (DMCA) and applicable law for copyright infringement.")
    S(88, "boundary", "c:terms/infringing-materials-protocol/", "Reporting Claims of Infringement", "Infringing Materials Protocol", "Intellectual Property Agent",
      "the intellectual property rights holder may request that Commerce remove or disable the material by submitting written notification to our Intellectual Property Agent.")
    S(88, "reason", "c:terms/infringing-materials-protocol/", "Protocol", "Infringing Materials Protocol", "DMCA",
      "because the DMCA provides a useful framework for resolving disputes surrounding allegedly infringing materials in other contexts or jurisdictions, where applicable, Commerce applies this protocol to other allegations of infringement of intellectual property rights.")


def hand2(S):
    LOC = "d:admin/catalog-and-inventory/inventory-locations"
    BETA = "d:beta"
    S(5, "where", LOC, "Locations", "Developer docs: Locations", "Locations",
      "*Locations* allow merchants to track product inventory across multiple physical or virtual locations.")
    S(5, "decides", LOC, "## Managing locations", "Developer docs: Locations", "Enterprise plan",
      "Enterprise plan: 100; can be customized by request", "Enterprise plan",
      "The same list reads: Standard plan: up to 4; Plus plan: up to 5; Pro plan: up to 8. The pricing page names the plans Core, Growth, Scale and Performance (Up to 4, Up to 5, Up to 8, Custom); both are recorded as stated.")
    S(5, "decides", LOC, "Alternate behavior", "Developer docs: Locations", "Aggregated stock",
      "By request, your store can instead use Aggregated stock, where stock from *all locations* is summed up for Stencil's storefront and location queries.")
    S(11, "where", "w:product/", "All Features: Operations & catalog", "Product page: All Features", "Product filtering",
      "Product filtering Create advanced product discovery experiences with customizable filtering.")
    for c, scope in ((13, "Product Recommendations API (closed beta)"), (17, "Checkout Extensions (closed beta)"),
                     (43, "Page Widgets API (closed beta)"), (66, "Powered By (closed beta)")):
        S(c, "decides", BETA, "Closed Betas", "Developer docs: Closed Betas", "Closed Betas",
          "These features are in closed beta and are not available by default. To request access, contact BigCommerce support.", scope)
    S(19, "where", "a:rest/admin/management/orders", "page introduction", "API reference group: /developer/api-reference/rest/admin/management/orders",
      "/developer/api-reference/rest/admin/management/orders",
      "Manage order coupons, messages, products, shipping addresses, statuses, taxes, shipments, and shipping address quotes.")
    S(21, "boundary", "d:admin/checkout-and-cart/orders/refunds", "Order Refunds", "Developer docs: Order Refunds", "Order V3",
      "Order V3 exposes endpoints for creating refunds against orders with settled payments.")
    S(26, "boundary", PAY, "Payments API (introduction)", "Developer docs: Payments API", "connected payment gateways",
      "The Payments API lets you process payments through the store’s connected payment gateways.")
    S(28, "where", "a:rest/admin/payments", "Payment Processing (introduction)", "API reference: Payment Processing", "PCI-compliant payments server",
      "The Payment Processing API uses BigCommerce's PCI-compliant payments server and a supported payment gateway to charge customers.")
    S(34, "boundary", "a:rest/admin/management/customer-segmentation", "## Authentication and scopes", "API reference: Customer Segmentation", "store_v2_customers",
      "These endpoints use the Customers OAuth scope.")
    S(8, "boundary", "a:rest/admin/management/pricing", "page introduction", "API reference: Pricing", "CORS",
      "The REST Storefront API uses CORS headers for authentication, and therefore has no required scopes.")
    S(37, "boundary", "a:rest/storefront/consent", "page introduction", "API reference: Storefront Cookie Consent", "CORS",
      "The REST Storefront API uses CORS headers for authentication, and therefore has no required scopes.")
    S(37, "decides", "d:storefront/catalyst/features/cookie-consent", "## Enable cookie consent", "Developer docs: Catalyst Cookie Consent", "Security Settings",
      "Cookie consent is controlled by a storefront-level setting in the BigCommerce control panel.", "Catalyst storefronts")
    S(37, "responsible", "d:storefront/catalyst/features/cookie-consent", "Warning", "Developer docs: Catalyst Cookie Consent", "Cookie Consent",
      "Store owners are solely responsible for ensuring their storefront complies with all applicable privacy laws — including GDPR, CCPA, and any other regulations in the jurisdictions where they operate.", "Catalyst storefronts")
    S(38, "decides", "d:admin/multi-storefront/overview", "## Channels", "Developer docs: Introduction to Multi-Storefront", "channel",
      "A merchant creates a new channel to sell in a new context.")
    S(39, "reason", "d:admin/multi-storefront/overview", "Introduction to Multi-Storefront", "Developer docs: Introduction to Multi-Storefront", "Multi-storefront",
      "We intend to provide these new features with no breaking changes to the platform so that existing single-storefront merchant stores continue to function as they did previously, and the existing APIs function as before for these stores.")
    S(44, "where", "d:integrations/scripts", "## Scripts API and Script Manager", "Developer docs: Scripts API", "Script Manager",
      "The control panel counterpart of the Scripts API is the Script Manager, which is available in the channel settings for the subject storefront on non-Blueprint stores.")
    S(44, "decides", "d:integrations/scripts", "## Scripts API and Script Manager", "Developer docs: Scripts API", "Script Manager",
      "After a merchant installs your app, the app can freely update its own scripts. All the app's scripts are available in the Script Manager for the merchant to inspect.")
    S(48, "where", "d:admin/store-configuration/translations/overview", "Translations Admin GraphQL API", "Developer docs: Translations Overview", "Translations Admin GraphQL API",
      "The Translations Admin GraphQL API is available on any storefront type – Stencil, Catalyst or any other headless.")
    S(48, "decides", "d:admin/store-configuration/settings/locales-configuration", "## Getting started", "Developer docs: Locales Configuration", "locales",
      "With the GraphQL Admin API, merchants can add, update, or remove locales for each sales channel, change locale status, and set a locale as the default.")
    S(48, "decides", "d:admin/store-configuration/settings/locales-configuration", "## Getting started", "Developer docs: Locales Configuration", "locales",
      "Each storefront can have up to 5 locales.")
    S(67, "boundary", "c:terms/acceptable-use-policy/", "Prohibited Activities/Content: Other Prohibited Activities", "Acceptable Use Policy", "Feedonomics Holdings LLC",
      "This includes, but is not limited to, using Secure File Transfer Protocol (SFTP) and/or encrypting the data you transmit to Feedonomics Holdings LLC.")
    S(68, "where", "w:product/", "All Features: Omnichannel & growth", "Product page: All Features", "Marketplaces",
      "Marketplaces Sell across Amazon, Walmart, eBay, and additional marketplace channels.")
    S(68, "boundary", "a:rest/admin/management/channels", "### Platform", "API reference: Channels", "amazon",
      "`amazon` | `marketplace`, `marketing`")
    S(69, "where", "w:product/", "All Features: Omnichannel & growth", "Product page: All Features", "POS integrations",
      "POS integrations Connect online and in-store sales through leading point-of-sale systems.")
    S(69, "boundary", "a:rest/admin/management/channels", "### Platform", "API reference: Channels", "square",
      "`square` | `pos`")
    S(72, "boundary", "d:admin/store-configuration/tax/tax-settings", "## Update tax settings", "Developer docs: Tax Settings", "/v3/tax/settings",
      "PUT https://api.bigcommerce.com/stores/{{STORE_HASH}}/v3/tax/settings")
    STG = "d:integrations/platform-solutions/staging-with-staging-pro"
    S(76, "decides", STG, "StagingPro", "Developer docs: StagingPro", "StagingPro",
      "StagingPro is a full-service sandbox, testing, staging, and CI/CD solution for Enterprise-level BigCommerce stores.", "Enterprise-level BigCommerce stores")
    S(76, "decides", STG, "StagingPro", "Developer docs: StagingPro", "StagingPro",
      "To add StagingPro to a store or set of stores, connect with your BigCommerce representative.")
    S(76, "boundary", STG, "StagingPro", "Developer docs: StagingPro", "StagingPro public API",
      "It uses Git, BigCommerce's APIs, and StagingPro's public API to provide an auditable solution.")
    S(77, "where", "c:terms/mobile-app-terms/", "Mobile App Terms (preamble)", "Mobile App Terms", "Commerce Mobile Application",
      "By using the Commerce Mobile Application (“Application”), you agree to be bound by the Agreement and these incorporated Mobile App Terms.")
    S(82, "responsible", DPA, "Exhibit B: Data Transfer", "Data Processing Addendum", "Data Transfer",
      "Commerce.com will notify Customer if it can no longer meet its obligation to provide the level of protection required by Data Protection Laws.")
    S(87, "boundary", "c:terms/merchant-client-terms/", "Agents: Contractual Relationship", "Merchant-Client Terms", "Contractual Relationship",
      "You will promptly provide Commerce written confirmation of the relationship between you and Client")
    S(88, "decides", "c:terms/acceptable-use-policy/", "Prohibited Activities/Content: Violations of Third Party Rights", "Acceptable Use Policy", "Violations of Third Party Rights",
      "Commerce may remove or block access to Your Materials upon receipt of proper notice of copyright infringement.")
    S(47, "decides", "d:admin/store-configuration/settings/store-configuration", "Store configuration", "Developer docs: Store configuration", "global default",
      "When these merchants configure their store settings, they're modifying the global default versions of their settings.")
    S(47, "where", "d:admin/store-configuration/settings/store-configuration", "Store configuration", "Developer docs: Store configuration", "Settings APIs",
      "BigCommerce's Settings APIs can manage many of the configuration settings that are exposed to merchants in their store control panel, such as the store's name and contact information, SEO settings, and search filters.")


def hand3(S):
    ADJ = "d:admin/catalog-and-inventory/inventory-adjustments"
    S(4, "where", ADJ, "Inventory adjustments", "Developer docs: Inventory adjustments", "Inventory API",
      "Because inventory and products are separate entities, an inventory adjustment that the Inventory API processes does not update the product's date_modified timestamp.")
    S(4, "reason", ADJ, "Concurrent requests", "Developer docs: Inventory adjustments", "strict order",
      "Internally, concurrent requests are handled one-by-one and have a strict order, to avoid overselling.")
    PLG = "d:admin/catalog-and-inventory/pricing/price-lists"
    S(7, "decides", PLG, "Price Lists", "Developer docs: Price Lists", "Price List Assignment API",
      "You can assign a price list to a specific sales channel, customer group, or customer group on a specific sales channel, using price list assignments in the Price List Assignment API.")
    S(7, "boundary", PLG, "### OAuth scopes", "Developer docs: Price Lists", "Products",
      "The following OAuth Scopes are required: * Products")
    PRO = "d:admin/catalog-and-inventory/promotions/overview"
    S(9, "boundary", PRO, "Prerequisites", "Developer docs: Promotions overview", "store_v2_marketing",
      "An API Account with an OAuth scope that includes modify store_v2_marketing")
    S(9, "where", PRO, "Promotions in the control panel", "Developer docs: Promotions overview", "Marketing > Promotions > Automatic",
      "After you create the promotion, it will appear under Marketing > Promotions > Automatic.")
    S(9, "decides", PRO, "Recommended usage", "Developer docs: Promotions overview", "active promotions",
      "BigCommerce recommends having less than 100 active promotions on storefronts, and there should be at most ten rules per promotion.")
    S(9, "reason", PRO, "Recommended usage", "Developer docs: Promotions overview", "active promotions",
      "This recommended usage helps to prevent a slowdown of the checkout process or contribute to an out-of-memory error.")
    FAC = "d:storefront/headless/products/faceted-textual-search"
    S(11, "decides", FAC, "Faceted search", "Developer docs: Faceted and Textual Search with the GraphQL Storefront API", "SearchProducts",
      "Note that you can query facets, filter by rating, or filter by \"in-stock\" only if the merchant is on a Pro or Enterprise plan.", "Pro or Enterprise plan")
    S(11, "decides", FAC, "Faceted search", "Developer docs: Faceted and Textual Search with the GraphQL Storefront API", "Product Filtering settings",
      "In addition, only facets that a merchant marks as visible in their Product Filtering settings will be returned.")
    SEG = "d:admin/customers/customer-segmentation/overview"
    S(34, "decides", SEG, "Exclusive enterprise feature", "Developer docs: Customer Segmentation overview", "Exclusive enterprise feature",
      "The Customer Segmentation API is available to enterprise customers.", "enterprise customers")
    S(34, "where", SEG, "Customer Segmentation overview", "Developer docs: Customer Segmentation overview", "Promotions standard editor",
      "Manual segments created with the Segmentation API will be visible within the Promotions standard editor control panel UI Targeting section.")
    S(46, "where", "d:admin/store-configuration/emails/overview", "Emails overview", "Developer docs: Email templates overview", "Marketing › Transactional Emails",
      "To edit transactional email templates in a store's control panel, log in and navigate to Marketing › Transactional Emails.")
    S(70, "decides", "d:admin/store-configuration/shipping/overview", "Shipping", "Developer docs: Shipping", "shipping zones",
      "You can configure shipping zones in the control panel or use the API to designate where a merchant ships their products and with which shipping methods should be available in each geographic region.")
    REC = "d:beta/product-recommendations/overview"
    S(13, "where", REC, "Product Recommendations overview", "Developer docs: Product Recommendations (beta)", "Google Vertex AI",
      "BigCommerce integrates with Google Vertex AI to generate recommendations.")
    S(13, "decides", REC, "Product Recommendations overview", "Developer docs: Product Recommendations (beta)", "Enterprise plans",
      "This is only available for BigCommerce Enterprise plans.", "BigCommerce Enterprise plans")
    S(13, "responsible", REC, "Pricing", "Developer docs: Product Recommendations (beta)", "Google Cloud account",
      "This solution is run in your Google Cloud account; thus, you will be responsible for all fees from Google.")
    S(13, "boundary", REC, "Product Recommendations overview", "Developer docs: Product Recommendations (beta)", "GraphQL Storefront API",
      "You can query product recommendations to display on storefronts using the GraphQL Storefront API after you set up this integration.")
    S(13, "reason", REC, "Product Recommendations overview", "Developer docs: Product Recommendations (beta)", "BigCommerce Analytics",
      "We need the data collected from BigCommerce Analytics to train the ML models. Thus, if you've turned off the native BigCommerce Analytics, you must turn it on to utilize BigAI product recommendations.")
    PB = "d:beta/powered-by/api-documentation"
    S(66, "where", PB, "Powered By", "Developer docs: Powered By (beta)", "Powered by",
      "Powered by is a collection of partner-focused APIs that enables you to offer BigCommerce stores to your merchants and seamlessly onboard them to our ecommerce platform.")
    S(66, "decides", PB, "Powered By", "Developer docs: Powered By (beta)", "billing relationship",
      "Additionally, you can decide whether you own the billing relationship for your merchant's BigCommerce products or let BigCommerce manage billing directly with the merchant.")
    CX = "d:beta/checkout-extensions/overview"
    S(17, "reason", CX, "Checkout Extensions overview", "Developer docs: Checkout Extensions (beta)", "custom checkouts",
      "Therefore, we don’t recommend using custom checkouts because they may be incompatible with extensions.")
    S(17, "boundary", CX, "FAQ", "Developer docs: Checkout Extensions (beta)", "Route",
      "Yes, our partner Route has created a checkout extension to extend the shipping step on the checkout page to include package protection as an option.")
    REV = "d:storefront/guides/graphql-storefront-api/products-and-catalog/product-reviews"
    S(12, "where", REV, "Product Reviews with the GraphQL Storefront API", "Developer docs: Product Reviews with the GraphQL Storefront API", "built-in comment system",
      "BigCommerce's GraphQL Storefront API allows you to create and query product reviews through the built-in comment system.")
    S(12, "decides", REV, "## Store settings", "Developer docs: Product Reviews with the GraphQL Storefront API", "review submission",
      "The merchant must enable this overall setting for the review submission process. Turning off this setting cancels any attempts to submit reviews.")
    SC = "d:storefront/headless/site-content"
    S(45, "boundary", SC, "Site Content with the GraphQL Storefront API", "Developer docs: Site Content with the GraphQL Storefront API", "GraphQL Storefront API",
      "BigCommerce's GraphQL Storefront API allows you to retrieve site content from each storefront channel.")
    S(45, "reason", SC, "Site Content with the GraphQL Storefront API", "Developer docs: Site Content with the GraphQL Storefront API", "site content",
      "Having access to site content makes it easier to build headless storefront applications using BigCommerce's built-in content, such as theme widgets.")
    S(42, "where", "d:storefront/stencil/overview", "Stencil Overview", "Developer docs: Stencil Overview", "Stencil",
      "Learn how to get up to speed on Stencil, BigCommerce's Handlebars-based theme engine.")
    S(49, "where", "d:admin/store-configuration/metafields/store-metafields", "Store Metafields", "Developer docs: Store Metafields", "store metafields",
      "Store metafields allow you to attach a metafield to the store itself. They are suitable for any global information against the store that is not channel specific.")
    S(62, "decides", "d:integrations/platform-solutions/analytics-with-bodl", "Subscribe to BODL events", "Developer docs: Big Open Data Layer for Storefront Analytics", "BODL",
      "Merchants must enable BODL in the store control panel for your script to subscribe to BODL events.")
    S(15, "where", "d:storefront/headless/cart-and-checkout/abandoned-carts", "Recovering Abandoned Carts", "Developer docs: Recovering Abandoned Carts", "Settings > General > Miscellaneous",
      "To enable the Abandoned Cart Saver notifications on your store, go to Settings > General > Miscellaneous in an active MSF-enabled control panel.")
    S(53, "reason", "d:storefront/guides/graphql-storefront-api/overview", "GraphQL Storefront API overview", "Developer docs: GraphQL Storefront API overview", "GraphQL",
      "Additionally, by leveraging the power of GraphQL, data for multiple resources can be returned from a single API call, which simplifies integration and increases performance so that developers can focus on building delightful shopper experiences.")
    S(33, "boundary", "d:storefront/headless/cart-and-checkout/carts", "Customer Login", "Developer docs: Managing Carts", "Send login token",
      "The Customer Login API requires your application to generate a JWT, then send it as a path parameter of the Send login token endpoint.")
    S(33, "reason", "d:storefront/headless/customers", "Managing customers", "Developer docs: Managing customers", "private tokens",
      "We recommend using private tokens for server-side sign-in because they are designed for server-to-server use.")
    S(6, "boundary", "d:integrations/platform-solutions/buy-online-pick-up-in-store/overview", "Buy Online, Pick up in Store overview", "Developer docs: Buy Online, Pick up in Store overview", "partner solutions",
      "You can store back-office components, such as location and inventories, on partner solutions. These partner solutions then serve as the source of truth for your data.")
    S(1, "boundary", "d:admin/catalog-and-inventory/products-overview", "Digital products", "Developer docs: Catalog Overview", "digital products",
      "Files can only be added to digital products via control panel or WebDav -- attaching via the API is not supported.")
    S(27, "boundary", "d:admin/checkout-and-cart/payment-providers/wallets/filter-wallet-shipping-options", "Filter wallet shipping options", "Developer docs: Filter wallet shipping options", "filterAvailableShippingOptions",
      "A custom checkout based on checkout-js can control which shipping options shoppers see in the Apple Pay, Google Pay, and Stripe Link V2 wallet interfaces.")


def hand4(S):
    S(54, "boundary", "d:admin/store-configuration/settings/locales-configuration", "GraphQL Admin API HTTP configuration", "Developer docs: Locales Configuration", "/graphql",
      "POST https://api.bigcommerce.com/stores/{{store_hash}}/graphql")
    S(50, "boundary", "d:storefront/catalyst/overview", "Capabilities", "Developer docs: Catalyst overview", "GraphQL Storefront API",
      "Scalable GraphQL implementation. Catalyst features scalable implementation of the GraphQL Storefront API.")
    S(62, "boundary", "d:integrations/platform-solutions/analytics-with-bodl", "Prerequisites", "Developer docs: Big Open Data Layer for Storefront Analytics", "Enable data layer mutation",
      "Enable BODL on the subject storefront using the control panel or the GraphQL Admin API's Enable data layer mutation")
    S(39, "boundary", "d:admin/multi-storefront/overview", "Introduction to Multi-Storefront", "Developer docs: Introduction to Multi-Storefront", "partners",
      "To provide the full multi-storefront, multi-channel support that merchants with complex stores expect and require, our partners must adapt.")
    S(51, "boundary", "llms_dev", "## Docs: Native Hosting, Makeswift", "Developer docs index (llms.txt)", "MAKESWIFT_SITE_API_KEY",
      "How the Makeswift site URL and the MAKESWIFT_SITE_API_KEY variable behave when you deploy a Makeswift-enabled Catalyst storefront to Native Hosting.")
