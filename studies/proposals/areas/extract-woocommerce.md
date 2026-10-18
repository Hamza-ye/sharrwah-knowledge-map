# woocommerce: its own organizing lists, as recorded

From `studies/concern-map/platforms/woocommerce/inventory.tsv` (654 entries) and `concerns.tsv` (118 concerns). Each entry keeps its `inv_id` and `cite_id`; the citation gives its source at a commit. List names are the inventory's own labels for where each list came from.


## Lists


### api-resources (211 entries, 0 out of the concern map's scope)

Entries: wc/v1; wc/v2; wc/v3; wc-telemetry; wc/v4; wc/store/v1; wc/private; wc-admin; wc-analytics; wccom-site/v3; wc/v3 > coupons; wc/v3 > customer-downloads; wc/v3 > customers; wc/v3 > network-orders; wc/v3 > order-notes; wc/v3 > order-refunds; wc/v3 > orders; wc/v3 > product-attribute-terms; wc/v3 > product-attributes; wc/v3 > product-categories; wc/v3 > product-custom-fields; wc/v3 > product-reviews; wc/v3 > product-shipping-classes; wc/v3 > product-tags; wc/v3 > products; wc/v3 > product-variations; wc/v3 > refunds; wc/v3 > reports-sales; wc/v3 > reports-top-sellers; wc/v3 > reports-orders-totals; wc/v3 > reports-products-totals; wc/v3 > reports-customers-totals; wc/v3 > reports-coupons-totals; wc/v3 > reports-reviews-totals; wc/v3 > reports; wc/v3 > settings; wc/v3 > settings-options; wc/v3 > shipping-zones; wc/v3 > shipping-zone-locations; wc/v3 > shipping-zone-methods; wc/v3 > tax-classes; wc/v3 > taxes; wc/v3 > variations; wc/v3 > webhooks; wc/v3 > system-status; wc/v3 > system-status-tools; wc/v3 > shipping-methods; wc/v3 > payment-gateways; wc/v3 > data; wc/v3 > data-continents; wc/v3 > data-countries; wc/v3 > data-currencies; wc/v3 > paypal-standard; wc/v3 > paypal-webhooks; wc/v3 > paypal-buttons; wc/v4 > fulfillments; wc/v4 > products; wc/v4 > customers; wc/v4 > order-notes; wc/v4 > shipping-zones; wc/v4 > shipping-zone-method; wc/v4 > orders; wc/v4 > refunds; wc/v4 > offline-payment-methods; wc/v4 > settings-general; wc/v4 > settings-email; wc/v4 > settings-emails; wc/v4 > settings-products; wc/v4 > settings-payment-gateways; wc/v4 > settings-tax; wc/v4 > settings-account; wc/v4 > settings; wc/store/v1 > /batch; wc/store/v1 > /cart; wc/store/v1 > /cart/add-item; wc/store/v1 > /cart/apply-coupon; wc/store/v1 > /cart/coupons; wc/store/v1 > /cart/coupons/(?P<code>[\w-]+); wc/store/v1 > /cart/extensions; wc/store/v1 > /cart/items; wc/store/v1 > /cart/items/(?P<key>[\w-]{32}); wc/store/v1 > /cart/remove-coupon; wc/store/v1 > /cart/remove-item; wc/store/v1 > /cart/select-shipping-rate; wc/store/v1 > /cart/update-item; wc/store/v1 > /cart/update-customer; wc/store/v1 > /checkout; wc/store/v1 > /checkout/(?P<id>[\d]+); wc/store/v1 > /order/(?P<id>[\d]+); wc/store/v1 > /products/attributes; wc/store/v1 > /products/attributes/(?P<id>[\d]+); wc/store/v1 > /products/attributes/(?P<attribute_id>[\d]+)/terms; wc/store/v1 > /products/categories; wc/store/v1 > /products/categories/(?P<id>[\d]+); wc/store/v1 > /products/brands; wc/store/v1 > /products/brands/(?P<identifier>[\w-]+); wc/store/v1 > /products/collection-data; wc/store/v1 > /products/reviews; wc/store/v1 > /products/tags; wc/store/v1 > /products; wc/store/v1 > /products/(?P<id>[\d]+); wc/store/v1 > /products/(?P<slug>[\S]+); wc/private > /patterns; wc/store/v1 > /shopper-lists; wc/store/v1 > /shopper-lists/(?P<slug>[a-z0-9-]+); wc/store/v1 > /shopper-lists/(?P<slug>[a-z0-9-]+)/items; wc/store/v1 > /shopper-lists/(?P<slug>[a-z0-9-]+)/items/(?P<key>[\w-]{32}); wc-admin > notice (Notice); wc-admin > features (Features); wc-admin > experiments (Experiments); wc-admin > marketing (Marketing); wc-admin > marketing/overview (MarketingOverview); wc-admin > marketing/recommendations (MarketingRecommendations); wc-admin > marketing/channels (MarketingChannels); wc-admin > marketing/campaigns (MarketingCampaigns); wc-admin > marketing/campaign-types (MarketingCampaignTypes); wc-admin > options (Options); wc-admin > payment-gateway-suggestions (PaymentGatewaySuggestions); wc-admin > themes (Themes); wc-admin > plugins (Plugins); wc-admin > onboarding/free-extensions (OnboardingFreeExtensions); wc-admin > onboarding/product-types (OnboardingProductTypes); wc-admin > onboarding/profile (OnboardingProfile); wc-admin > onboarding/tasks (OnboardingTasks); wc-admin > onboarding/themes (OnboardingThemes); wc-admin > onboarding/plugins (OnboardingPlugins); wc-admin > onboarding (OnboardingProducts); wc-admin > mobile-app (MobileAppMagicLink); wc-admin > mobile-app (MobileAppQRLogin); wc-admin > shipping-partner-suggestions (ShippingPartnerSuggestions); wc-analytics > admin/notes (Notes); wc-analytics > NoteActions; wc-analytics > Coupons; wc-analytics > Data; wc-analytics > DataCountries; wc-analytics > data/download-ips (DataDownloadIPs); wc-analytics > Orders; wc-analytics > Products; wc-analytics > ProductAttributes; wc-analytics > ProductAttributeTerms; wc-analytics > ProductCategories; wc-analytics > ProductVariations; wc-analytics > ProductReviews; wc-analytics > ProductsLowInStock; wc-analytics > activity-panel/counts (ActivityPanelCounts); wc-analytics > SettingOptions; wc-analytics > Taxes; wc-analytics > customers (Customers); wc-analytics > leaderboards (Leaderboards); wc-analytics > Reports/Controller; wc-analytics > reports/import (Reports/Import/Controller); wc-analytics > reports/(?P<type>[a-z]+)/export (Reports/Export/Controller); wc-analytics > reports/products (Reports/Products/Controller); wc-analytics > reports/variations (Reports/Variations/Controller); wc-analytics > reports/products/stats (Reports/Products/Stats/Controller); wc-analytics > reports/variations/stats (Reports/Variations/Stats/Controller); wc-analytics > reports/revenue/stats (Reports/Revenue/Stats/Controller); wc-analytics > reports/orders (Reports/Orders/Controller); wc-analytics > reports/orders/stats (Reports/Orders/Stats/Controller); wc-analytics > reports/categories (Reports/Categories/Controller); wc-analytics > reports/taxes (Reports/Taxes/Controller); wc-analytics > reports/taxes/stats (Reports/Taxes/Stats/Controller); wc-analytics > reports/coupons (Reports/Coupons/Controller); wc-analytics > reports/coupons/stats (Reports/Coupons/Stats/Controller); wc-analytics > reports/stock (Reports/Stock/Controller); wc-analytics > reports/stock/stats (Reports/Stock/Stats/Controller); wc-analytics > reports/downloads (Reports/Downloads/Controller); wc-analytics > reports/downloads/stats (Reports/Downloads/Stats/Controller); wc-analytics > reports/customers (Reports/Customers/Controller); wc-analytics > reports/customers/stats (Reports/Customers/Stats/Controller); wc-analytics > imports (AnalyticsImports); wc-analytics > reports/performance-indicators (Reports/PerformanceIndicators/Controller); wc-admin > launch-your-store; wccom-site/v3 > connection; wccom-site/v3 > installer; wccom-site/v3 > ssr; wccom-site/v3 > status; wc-telemetry > tracker; Introduction; Authentication; Index; Coupons; Customers; Orders; Order actions; Order notes; Order refunds; Products; Product variations; Product attributes; Product attribute terms; Product categories; Product custom fields; Product shipping classes; Product tags; Product reviews; Reports; Refunds; Tax rates; Tax classes; Webhooks; Settings; Setting options; Payment gateways; Shipping zones; Shipping zone locations; Shipping zone methods; Shipping methods; System status; System status tools; Data


### other:marketplace-categories (79 entries, 0 out of the concern map's scope)

- Extensions (WC-I-0489, WC-S-0694; concerns WC-C-017 WC-C-059)
- Themes (WC-I-0490, WC-S-0695; concerns WC-C-017 WC-C-111)
- Business services (WC-I-0491, WC-S-0696; concerns WC-C-112)
- Extensions > Developed by Woo (WC-I-0492, WC-S-0697; concerns WC-C-050)
- Extensions > Official payments (WC-I-0493, WC-S-0698; concerns WC-C-005)
- Extensions > Shipping, delivery and fulfillment (WC-I-0494, WC-S-0699; concerns WC-C-061)
- Extensions > Conversion (WC-I-0495, WC-S-0700; concerns WC-C-105)
- Extensions > Customer service (WC-I-0496, WC-S-0701; concerns WC-C-106)
- Extensions > Merchandising (WC-I-0497, WC-S-0702; concerns WC-C-104)
- Extensions > Store content and customizations (WC-I-0498, WC-S-0703; concerns WC-C-107)
- Extensions > Store management (WC-I-0499, WC-S-0704; concerns WC-C-109)
- Extensions > Marketing (WC-I-0500, WC-S-0705; concerns WC-C-110)
- Extensions > Official payments > Processors & gateways (WC-I-0501, WC-S-0706; concerns WC-C-005)
- Extensions > Official payments > Wallets & express checkouts (WC-I-0502, WC-S-0707; concerns WC-C-005)
- Extensions > Official payments > Buy now pay later (WC-I-0503, WC-S-0708; concerns WC-C-005)
- Extensions > Official payments > Crypto payments (WC-I-0504, WC-S-0709; concerns WC-C-005)
- Extensions > Official payments > B2B payments (WC-I-0505, WC-S-0710; concerns WC-C-005)
- Extensions > Official payments > In-person payments (WC-I-0506, WC-S-0711; concerns WC-C-005 WC-C-089)
- Extensions > Shipping, delivery and fulfillment > Delivery options and enhancements (WC-I-0507, WC-S-0712; concerns WC-C-061)
- Extensions > Shipping, delivery and fulfillment > Fulfillment and dropshipping (WC-I-0508, WC-S-0713; concerns WC-C-061)
- Extensions > Shipping, delivery and fulfillment > Inventory and order management (WC-I-0509, WC-S-0714; concerns WC-C-061)
- Extensions > Shipping, delivery and fulfillment > Label printing (WC-I-0510, WC-S-0715; concerns WC-C-061)
- Extensions > Shipping, delivery and fulfillment > Shipping rates at checkout (WC-I-0511, WC-S-0716; concerns WC-C-061)
- Extensions > Conversion > Customer feedback (WC-I-0512, WC-S-0717; concerns WC-C-105)
- Extensions > Conversion > Promotions (WC-I-0513, WC-S-0718; concerns WC-C-105)
- Extensions > Conversion > Recovering orders (WC-I-0514, WC-S-0719; concerns WC-C-105)
- Extensions > Conversion > Rewards and loyalty (WC-I-0515, WC-S-0720; concerns WC-C-105)
- Extensions > Conversion > Store alerts (WC-I-0516, WC-S-0721; concerns WC-C-105)
- Extensions > Conversion > Upsells and cross-sells (WC-I-0517, WC-S-0722; concerns WC-C-105)
- Extensions > Customer service > Customer Accounts (WC-I-0518, WC-S-0723; concerns WC-C-106)
- Extensions > Customer service > Live chat (WC-I-0519, WC-S-0724; concerns WC-C-106)
- Extensions > Customer service > Managing customers (WC-I-0520, WC-S-0725; concerns WC-C-106)
- Extensions > Customer service > Post-purchase services (WC-I-0521, WC-S-0726; concerns WC-C-106)
- Extensions > Customer service > Support (WC-I-0522, WC-S-0727; concerns WC-C-106)
- Extensions > Merchandising > Memberships (WC-I-0523, WC-S-0728; concerns WC-C-102)
- Extensions > Merchandising > Additional purchases (WC-I-0524, WC-S-0729; concerns WC-C-104)
- Extensions > Merchandising > B2B (WC-I-0525, WC-S-0730; concerns WC-C-103)
- Extensions > Merchandising > Bookings and appointments (WC-I-0526, WC-S-0731; concerns WC-C-101)
- Extensions > Merchandising > Bundles (WC-I-0527, WC-S-0732; concerns WC-C-104)
- Extensions > Merchandising > Gifts (WC-I-0528, WC-S-0733; concerns WC-C-104)
- Extensions > Merchandising > Order options (WC-I-0529, WC-S-0734; concerns WC-C-104)
- Extensions > Merchandising > Pricing (WC-I-0530, WC-S-0735; concerns WC-C-104)
- Extensions > Merchandising > Product display (WC-I-0531, WC-S-0736; concerns WC-C-104)
- Extensions > Merchandising > Product options (WC-I-0532, WC-S-0737; concerns WC-C-104)
- Extensions > Merchandising > Product variations (WC-I-0533, WC-S-0738; concerns WC-C-104)
- Extensions > Merchandising > Subscriptions (WC-I-0534, WC-S-0739; concerns WC-C-100)
- Extensions > Store content and customizations > Cart and checkout features (WC-I-0535, WC-S-0740; concerns WC-C-107)
- Extensions > Store content and customizations > International and localization (WC-I-0536, WC-S-0741; concerns WC-C-108)
- Extensions > Store content and customizations > Product images and media (WC-I-0537, WC-S-0742; concerns WC-C-107)
- Extensions > Store content and customizations > Search and navigation (WC-I-0538, WC-S-0743; concerns WC-C-107)
- Extensions > Store content and customizations > Store page enhancements (WC-I-0539, WC-S-0744; concerns WC-C-107)
- Extensions > Store management > Payment management (WC-I-0540, WC-S-0745; concerns WC-C-005)
- Extensions > Store management > Business insights (WC-I-0541, WC-S-0746; concerns WC-C-109)
- Extensions > Store management > Import and export (WC-I-0542, WC-S-0747; concerns WC-C-109)
- Extensions > Store management > Merchant financing (WC-I-0543, WC-S-0748; concerns WC-C-016)
- Extensions > Store management > Order management (WC-I-0544, WC-S-0749; concerns WC-C-109)
- Extensions > Store management > Policy and security (WC-I-0545, WC-S-0750; concerns WC-C-109)
- Extensions > Store management > Sales tax and duties (WC-I-0546, WC-S-0751; concerns WC-C-056 WC-C-058)
- Extensions > Store management > Admin and notifications (WC-I-0547, WC-S-0752; concerns WC-C-109)
- Extensions > Store management > Point of sale (WC-I-0548, WC-S-0753; concerns WC-C-089)
- Extensions > Store management > Accounting (WC-I-0549, WC-S-0754; concerns WC-C-109)
- Extensions > Marketing > Advertising and promotions (WC-I-0550, WC-S-0755; concerns WC-C-110)
- Extensions > Marketing > Automation (WC-I-0551, WC-S-0756; concerns WC-C-110)
- Extensions > Marketing > CRM (WC-I-0552, WC-S-0757; concerns WC-C-110)
- Extensions > Marketing > Reporting and analytics (WC-I-0553, WC-S-0758; concerns WC-C-110)
- Extensions > Marketing > Sales channels (WC-I-0554, WC-S-0759; concerns WC-C-110)
- Extensions > Marketing > SEO and SEM (WC-I-0555, WC-S-0760; concerns WC-C-110)
- Extensions > Marketing > Email (WC-I-0556, WC-S-0761; concerns WC-C-110)
- Extensions > Marketing > Social (WC-I-0557, WC-S-0762; concerns WC-C-110)
- Business services > Insurance (WC-I-0558, WC-S-0763; concerns WC-C-112)
- Business services > Business Formation (WC-I-0559, WC-S-0764; concerns WC-C-112)
- Business services > Communication (WC-I-0560, WC-S-0765; concerns WC-C-112)
- Business services > Compliance (WC-I-0561, WC-S-0766; concerns WC-C-112)
- Business services > Developer Services (WC-I-0562, WC-S-0767; concerns WC-C-112)
- Business services > Finance (WC-I-0563, WC-S-0768; concerns WC-C-112)
- Business services > Law (WC-I-0564, WC-S-0769; concerns WC-C-112)
- Business services > Other (WC-I-0565, WC-S-0770; concerns WC-C-112)
- Business services > Productivity (WC-I-0566, WC-S-0771; concerns WC-C-112)
- Business services > Support (WC-I-0567, WC-S-0772; concerns WC-C-112)

### extension-points (50 entries, 0 out of the concern map's scope)

Entries: WC_Payment_Gateway; woocommerce_payment_gateways; WC_Payment_Gateway_CC; WC_Payment_Gateway_ECheck; WC_Payment_Token; WC_Shipping_Method; woocommerce_shipping_methods; WC_Integration; woocommerce_integrations; woocommerce_email_classes; woocommerce_get_settings_pages; WC_Address_Provider; WC_Log_Handler; woocommerce_webhook_topics; woocommerce_rest_api_get_rest_namespaces; woocommerce_admin_rest_controllers; wc_admin_register_page; IntegrationInterface; AbstractPaymentMethodType; ExtendSchema; woocommerce_register_additional_checkout_field; FeaturesUtil::declare_compatibility; Extending the Store API; Available extensible endpoints; Adding fields and passing values; Exposing your data; Available Formatters; Marking a cart item as a child of another cart item; Updating the cart on-demand; Getting started with Cart and Checkout extensibility; Additional checkout fields; Available slots; Checkout flow and events; Filtering payment methods in the Checkout block; Payment method integration; Checkout Utilities; DOM events; Available Filters; Inner block types; Cart line items; Checkout and place order button; Coupons; Order summary items; Totals footer item; How the checkout block processes an order; Removing checkout fields; Product collection block; DOM events sent from product collection block; Registering custom collections in product collection block; On-Sale Badge block


### other:payment-extension-suggestions (46 entries, 0 out of the concern map's scope)

- airwallex (WC-I-0365, WC-S-0365; concerns WC-C-004)
- antom (WC-I-0366, WC-S-0366; concerns WC-C-004)
- mercado_pago (WC-I-0367, WC-S-0367; concerns WC-C-004)
- mollie (WC-I-0368, WC-S-0368; concerns WC-C-004)
- payfast (WC-I-0369, WC-S-0369; concerns WC-C-004)
- paymob (WC-I-0370, WC-S-0370; concerns WC-C-004)
- paypal_full_stack (WC-I-0371, WC-S-0371; concerns WC-C-004)
- paypal_wallet (WC-I-0372, WC-S-0372; concerns WC-C-004)
- payoneer (WC-I-0373, WC-S-0373; concerns WC-C-004)
- paystack (WC-I-0374, WC-S-0374; concerns WC-C-004)
- paytrail (WC-I-0375, WC-S-0375; concerns WC-C-004)
- payu_india (WC-I-0376, WC-S-0376; concerns WC-C-004)
- razorpay (WC-I-0377, WC-S-0377; concerns WC-C-004)
- square (WC-I-0378, WC-S-0378; concerns WC-C-004)
- stripe (WC-I-0379, WC-S-0379; concerns WC-C-004)
- tilopay (WC-I-0380, WC-S-0380; concerns WC-C-004)
- viva_wallet (WC-I-0381, WC-S-0381; concerns WC-C-004)
- woopayments (WC-I-0382, WC-S-0382; concerns WC-C-004 WC-C-006)
- amazon_pay (WC-I-0383, WC-S-0383; concerns WC-C-004)
- affirm (WC-I-0384, WC-S-0384; concerns WC-C-004)
- afterpay (WC-I-0385, WC-S-0385; concerns WC-C-004)
- clearpay (WC-I-0386, WC-S-0386; concerns WC-C-004)
- klarna (WC-I-0387, WC-S-0387; concerns WC-C-004)
- kustom_checkout (WC-I-0388, WC-S-0388; concerns WC-C-004)
- helcim (WC-I-0389, WC-S-0389; concerns WC-C-004)
- komoju (WC-I-0390, WC-S-0390; concerns WC-C-004)
- monei (WC-I-0391, WC-S-0391; concerns WC-C-004)
- coinbase (WC-I-0392, WC-S-0392; concerns WC-C-004)
- billie (WC-I-0393, WC-S-0393; concerns WC-C-004)
- bolt_checkout (WC-I-0394, WC-S-0394; concerns WC-C-004)
- authorize_net (WC-I-0395, WC-S-0395; concerns WC-C-004)
- depay (WC-I-0396, WC-S-0396; concerns WC-C-004)
- elavon (WC-I-0397, WC-S-0397; concerns WC-C-004)
- eway (WC-I-0398, WC-S-0398; concerns WC-C-004)
- fortis (WC-I-0399, WC-S-0399; concerns WC-C-004)
- gocardless (WC-I-0400, WC-S-0400; concerns WC-C-004)
- nexi_checkout (WC-I-0401, WC-S-0401; concerns WC-C-004)
- paypal_zettle (WC-I-0402, WC-S-0402; concerns WC-C-004)
- rapyd (WC-I-0403, WC-S-0403; concerns WC-C-004)
- paypal_braintree (WC-I-0404, WC-S-0404; concerns WC-C-004)
- visa_as (WC-I-0405, WC-S-0405; concerns WC-C-004)
- ngenius (WC-I-0406, WC-S-0406; concerns WC-C-004)
- mastercard (WC-I-0407, WC-S-0407; concerns WC-C-004)
- evergreen (WC-I-0408, WC-S-0408; concerns WC-C-004)
- mypos (WC-I-0409, WC-S-0409; concerns WC-C-004)
- heliopay (WC-I-0410, WC-S-0410; concerns WC-C-004)

### admin-navigation (40 entries, 0 out of the concern map's scope)

- Status > System status (WC-I-0036, WC-S-0036; concerns WC-C-083)
- Status > Tools (WC-I-0037, WC-S-0037; concerns WC-C-083)
- Status > Logs (WC-I-0038, WC-S-0038; concerns WC-C-037)
- WooCommerce (WC-I-0039, WC-S-0039; concerns WC-C-081)
- WooCommerce > Home (WC-I-0040, WC-S-0040; concerns WC-C-081)
- WooCommerce > Orders (WC-I-0041, WC-S-0041; concerns WC-C-070)
- WooCommerce > Customers (WC-I-0042, WC-S-0042; concerns WC-C-073)
- WooCommerce > Reports (WC-I-0043, WC-S-0043; concerns WC-C-038)
- WooCommerce > Settings (WC-I-0044, WC-S-0044; concerns WC-C-081)
- WooCommerce > Status (WC-I-0045, WC-S-0045; concerns WC-C-083)
- WooCommerce > Extensions (WC-I-0046, WC-S-0046; concerns WC-C-063)
- WooCommerce > Notifications (WC-I-0047, WC-S-0047; concerns WC-C-069)
- WooCommerce > Coupons (WC-I-0048, WC-S-0048; concerns WC-C-074)
- Products (WC-I-0049, WC-S-0049; concerns WC-C-064)
- Products > All Products (WC-I-0050, WC-S-0050; concerns WC-C-064)
- Products > Add New (WC-I-0051, WC-S-0051; concerns WC-C-064)
- Products > Categories (WC-I-0052, WC-S-0052; concerns WC-C-064)
- Products > Tags (WC-I-0053, WC-S-0053; concerns WC-C-064)
- Products > Brands (WC-I-0054, WC-S-0054; concerns WC-C-064)
- Products > Attributes (WC-I-0055, WC-S-0055; concerns WC-C-064)
- Products > Reviews (WC-I-0056, WC-S-0056; concerns WC-C-065)
- Products > Product Import (WC-I-0057, WC-S-0057; concerns WC-C-067)
- Products > Product Export (WC-I-0058, WC-S-0058; concerns WC-C-067)
- Payments (WC-I-0059, WC-S-0059; concerns WC-C-001)
- Marketing (WC-I-0060, WC-S-0060; concerns WC-C-084)
- Marketing > Overview (WC-I-0061, WC-S-0061; concerns WC-C-084)
- Marketing > Coupons (WC-I-0062, WC-S-0062; concerns WC-C-074)
- Setup Wizard (WC-I-0063, WC-S-0063; concerns WC-C-081)
- Analytics (WC-I-0064, WC-S-0064; concerns WC-C-038)
- Analytics > Overview (WC-I-0065, WC-S-0065; concerns WC-C-038)
- Analytics > Products (WC-I-0066, WC-S-0066; concerns WC-C-038)
- Analytics > Revenue (WC-I-0067, WC-S-0067; concerns WC-C-038)
- Analytics > Orders (WC-I-0068, WC-S-0068; concerns WC-C-038)
- Analytics > Variations (WC-I-0069, WC-S-0069; concerns WC-C-038)
- Analytics > Categories (WC-I-0070, WC-S-0070; concerns WC-C-038)
- Analytics > Coupons (WC-I-0071, WC-S-0071; concerns WC-C-038 WC-C-074)
- Analytics > Taxes (WC-I-0072, WC-S-0072; concerns WC-C-038 WC-C-054)
- Analytics > Downloads (WC-I-0073, WC-S-0073; concerns WC-C-038 WC-C-066)
- Analytics > Stock (WC-I-0074, WC-S-0074; concerns WC-C-038 WC-C-068)
- Analytics > Settings (WC-I-0075, WC-S-0075; concerns WC-C-038)

### settings (35 entries, 0 out of the concern map's scope)

- General (WC-I-0001, WC-S-0001; concerns WC-C-030 WC-C-052)
- Products (WC-I-0002, WC-S-0002; concerns WC-C-064)
- Tax (WC-I-0003, WC-S-0003; concerns WC-C-054)
- Shipping (WC-I-0004, WC-S-0004; concerns WC-C-075)
- Payments (WC-I-0005, WC-S-0005; concerns WC-C-001)
- Accounts & Privacy (WC-I-0006, WC-S-0006; concerns WC-C-045 WC-C-073)
- Emails (WC-I-0007, WC-S-0007; concerns WC-C-076)
- Integration (WC-I-0008, WC-S-0008; concerns WC-C-046 WC-C-086)
- Site visibility (WC-I-0009, WC-S-0009; concerns WC-C-082)
- Point of Sale (WC-I-0010, WC-S-0010; concerns WC-C-089)
- Advanced (WC-I-0011, WC-S-0011; concerns WC-C-078)
- Products > General (WC-I-0012, WC-S-0012; concerns WC-C-064)
- Products > Inventory (WC-I-0013, WC-S-0013; concerns WC-C-068)
- Products > Downloadable products (WC-I-0014, WC-S-0014; concerns WC-C-066)
- Tax > Tax options (WC-I-0015, WC-S-0015; concerns WC-C-054)
- Tax > Standard rates (WC-I-0016, WC-S-0016; concerns WC-C-054)
- Shipping > Shipping zones (WC-I-0017, WC-S-0017; concerns WC-C-075)
- Shipping > Shipping settings (WC-I-0018, WC-S-0018; concerns WC-C-075)
- Shipping > Classes (WC-I-0019, WC-S-0019; concerns WC-C-075)
- Shipping > Shipping providers (WC-I-0020, WC-S-0020; concerns WC-C-092)
- Emails > Email options (WC-I-0021, WC-S-0021; concerns WC-C-076)
- Advanced > Page setup (WC-I-0022, WC-S-0022; concerns WC-C-072)
- Advanced > REST API keys (WC-I-0023, WC-S-0023; concerns WC-C-078)
- Advanced > REST API caching (WC-I-0024, WC-S-0024; concerns WC-C-078)
- Advanced > Webhooks (WC-I-0025, WC-S-0025; concerns WC-C-077)
- Advanced > Legacy API (WC-I-0026, WC-S-0026; concerns WC-C-078)
- Advanced > WooCommerce.com (WC-I-0027, WC-S-0027; concerns WC-C-035 WC-C-063)
- Advanced > Blueprint (beta) (WC-I-0028, WC-S-0028; concerns WC-C-094)
- Payments > main (WC-I-0029, WC-S-0029; concerns WC-C-001)
- Payments > offline (WC-I-0030, WC-S-0030; concerns WC-C-002)
- Payments > cod (WC-I-0031, WC-S-0031; concerns WC-C-002)
- Payments > bacs (WC-I-0032, WC-S-0032; concerns WC-C-002)
- Payments > cheque (WC-I-0033, WC-S-0033; concerns WC-C-002)
- Tax > Reduced rate rates (WC-I-0034, WC-S-0034; concerns WC-C-054)
- Tax > Zero rate rates (WC-I-0035, WC-S-0035; concerns WC-C-054)

### other:features (32 entries, 0 out of the concern map's scope)

- WooCommerce Analytics (WC-I-0325, WC-S-0325; concerns WC-C-038 WC-C-088)
- Product gallery videos (WC-I-0326, WC-S-0326; concerns WC-C-064 WC-C-088)
- Cart & Checkout Blocks (WC-I-0327, WC-S-0327; concerns WC-C-072 WC-C-088)
- Rate limit Checkout (WC-I-0328, WC-S-0328; concerns WC-C-031 WC-C-088)
- Marketplace (WC-I-0329, WC-S-0329; concerns WC-C-063 WC-C-088)
- Order withdrawal (WC-I-0330, WC-S-0330; concerns WC-C-088 WC-C-091)
- Order Attribution (WC-I-0331, WC-S-0331; concerns WC-C-085 WC-C-088)
- Site visibility badge (WC-I-0332, WC-S-0332; concerns WC-C-082 WC-C-088)
- HPOS Full text search indexes (WC-I-0333, WC-S-0333; concerns WC-C-033 WC-C-088)
- HPOS Data Caching (WC-I-0334, WC-S-0334; concerns WC-C-033 WC-C-088)
- Remote Logging (WC-I-0335, WC-S-0335; concerns WC-C-036 WC-C-088)
- Deferred emails (WC-I-0336, WC-S-0336; concerns WC-C-076 WC-C-088)
- Customer review request (beta) (WC-I-0337, WC-S-0337; concerns WC-C-065 WC-C-088)
- Email improvements (WC-I-0338, WC-S-0338; concerns WC-C-076 WC-C-088)
- Blueprint (beta) (WC-I-0339, WC-S-0339; concerns WC-C-088 WC-C-094)
- Block Email Editor (alpha) (WC-I-0340, WC-S-0340; concerns WC-C-076 WC-C-088)
- Variation gallery (WC-I-0341, WC-S-0341; concerns WC-C-064 WC-C-088)
- Color swatches for attributes (WC-I-0342, WC-S-0342; concerns WC-C-064 WC-C-088)
- Point of Sale (WC-I-0343, WC-S-0343; concerns WC-C-088 WC-C-089)
- POS staff (WC-I-0344, WC-S-0344; concerns WC-C-088 WC-C-089)
- Order Fulfillments (WC-I-0345, WC-S-0345; concerns WC-C-088 WC-C-092)
- WooCommerce MCP (WC-I-0346, WC-S-0346; concerns WC-C-088 WC-C-095)
- Clear Customer Sessions When Empty (WC-I-0347, WC-S-0347; concerns WC-C-072 WC-C-088)
- Push Notifications (WC-I-0348, WC-S-0348; concerns WC-C-088 WC-C-090)
- REST API Caching (WC-I-0349, WC-S-0349; concerns WC-C-078 WC-C-088)
- Save for Later in Cart (WC-I-0350, WC-S-0350; concerns WC-C-088 WC-C-097)
- Wishlists (WC-I-0351, WC-S-0351; concerns WC-C-088 WC-C-097)
- Cache Product Objects (WC-I-0352, WC-S-0352; concerns WC-C-064 WC-C-088)
- Back in Stock Notifications (WC-I-0353, WC-S-0353; concerns WC-C-069 WC-C-088)
- Unified block editor assets (WC-I-0354, WC-S-0354; concerns WC-C-088)
- High-Performance order storage (WC-I-0355, WC-S-0355; concerns WC-C-033 WC-C-088)
- Cost of Goods Sold (WC-I-0356, WC-S-0356; concerns WC-C-088 WC-C-093)

### legal-agreements (25 entries, 8 out of the concern map's scope)

- Terms of Service (WC-I-0630, WC-S-0643; concerns WC-C-015 WC-C-019 WC-C-023 WC-C-026 WC-C-027 WC-C-028 WC-C-029 WC-C-040 WC-C-041 WC-C-042 WC-C-049 WC-C-057 WC-C-058 WC-C-117)
- Privacy Policy (WC-I-0631, WC-S-0830; concerns WC-C-024 WC-C-040 WC-C-042 WC-C-043)
- Privacy Notice for California Users (WC-I-0632, WC-S-0831; concerns WC-C-024)
- Do not sell or share my personal information (WC-I-0633, WC-S-0832; concerns WC-C-024)
- WooCommerce Support Policy (WC-I-0634, WC-S-0833; concerns WC-C-062)
- Refund Policy (WC-I-0635, WC-S-0834; concerns WC-C-017)
- Marketplace Vendor Agreement (WC-I-0638, WC-S-0576; concerns WC-C-017)
- Store guidelines (WC-I-0639, WC-S-0846; concerns WC-C-022)
- Restricted businesses and activities (WC-I-0640, WC-S-0563; concerns WC-C-011)
- Request a data processing agreement (WC-I-0641, WC-S-0847; concerns WC-C-044)
- Connected Account Agreement (WC-I-0642, WC-S-0507; concerns WC-C-020 WC-C-048)
- Woo Guidelines for CBD and Other Hemp-Derived Products (WC-I-0643, WC-S-0837; concerns WC-C-011)
- AI Guidelines (WC-I-0644, WC-S-0838; concerns WC-C-096)
- WooCommerce usage tracking (WC-I-0646, WC-S-0570; concerns WC-C-035)
- WooCommerce Analytics data syncing (WC-I-0647, WC-S-0573; concerns WC-C-039 WC-C-117)
- wooads-policy (WC-I-0650, WC-S-0842; concerns WC-C-117 WC-C-114)
- GPLv3 (WC-I-0654, WC-S-0589; concerns WC-C-025)

Out of the concern map's scope: Woo trademark guidelines (Rules for using Woo's own trademarks and logos; no store concern is placed by them.); Brand and logo guidelines (Rules for using Woo's own trademarks and logos; no store concern is placed by them.); Cookie Policy (Covers cookies on the WooCommerce.com website itself, not the merchant's store.); customer-research-agreement (Terms for taking part in Woo's customer research, not a store concern.); code-of-conduct (Community code of conduct for Woo events and spaces, not a store concern.); terms-conditions/woopayments-promotion (Time-limited WooPayments promotional offer terms; they set no standing placement.); terms-conditions/woopayments-mid-2025-promotional-offer-terms-and-conditions (Time-limited WooPayments promotional offer terms; they set no standing placement.); terms-conditions/woopayments-action-promotion-2023 (Time-limited WooPayments promotional offer terms; they set no standing placement.)


### other:emails (23 entries, 0 out of the concern map's scope)

- New order (WC_Email_New_Order) (WC-I-0294, WC-S-0294; concerns WC-C-076)
- Cancelled order (WC_Email_Cancelled_Order) (WC-I-0295, WC-S-0295; concerns WC-C-076)
- Cancelled order (WC_Email_Customer_Cancelled_Order) (WC-I-0296, WC-S-0296; concerns WC-C-076)
- Failed order (WC_Email_Failed_Order) (WC-I-0297, WC-S-0297; concerns WC-C-076)
- Failed order (WC_Email_Customer_Failed_Order) (WC-I-0298, WC-S-0298; concerns WC-C-076)
- Order on-hold (WC_Email_Customer_On_Hold_Order) (WC-I-0299, WC-S-0299; concerns WC-C-076)
- Processing order (WC_Email_Customer_Processing_Order) (WC-I-0300, WC-S-0300; concerns WC-C-076)
- Completed order (WC_Email_Customer_Completed_Order) (WC-I-0301, WC-S-0301; concerns WC-C-076)
- Refunded order (WC_Email_Customer_Refunded_Order) (WC-I-0302, WC-S-0302; concerns WC-C-071 WC-C-076)
- Order details (WC_Email_Customer_Invoice) (WC-I-0303, WC-S-0303; concerns WC-C-076)
- Customer note (WC_Email_Customer_Note) (WC-I-0304, WC-S-0304; concerns WC-C-076)
- Reset password (WC_Email_Customer_Reset_Password) (WC-I-0305, WC-S-0305; concerns WC-C-073 WC-C-076)
- New account (WC_Email_Customer_New_Account) (WC-I-0306, WC-S-0306; concerns WC-C-073 WC-C-076)
- Payment gateway enabled (WC_Email_Admin_Payment_Gateway_Enabled) (WC-I-0307, WC-S-0307; concerns WC-C-076)
- POS completed order (WC_Email_Customer_POS_Completed_Order) (WC-I-0308, WC-S-0308; concerns WC-C-076 WC-C-089)
- POS refunded order (WC_Email_Customer_POS_Refunded_Order) (WC-I-0309, WC-S-0309; concerns WC-C-076 WC-C-089)
- Fulfillment created (WC_Email_Customer_Fulfillment_Created) (WC-I-0310, WC-S-0310; concerns WC-C-076 WC-C-092)
- Fulfillment updated (WC_Email_Customer_Fulfillment_Updated) (WC-I-0311, WC-S-0311; concerns WC-C-076 WC-C-092)
- Fulfillment deleted (WC_Email_Customer_Fulfillment_Deleted) (WC-I-0312, WC-S-0312; concerns WC-C-076 WC-C-092)
- Review request (WC_Email_Customer_Review_Request) (WC-I-0313, WC-S-0313; concerns WC-C-065 WC-C-076)
- Order withdrawal request received (WC_Email_Customer_Order_Withdrawal_Requested) (WC-I-0314, WC-S-0314; concerns WC-C-076 WC-C-091)
- Order withdrawal request (WC_Email_Order_Withdrawal_Requested) (WC-I-0315, WC-S-0315; concerns WC-C-076 WC-C-091)
- Partially refunded order (WC_Email_Customer_Partially_Refunded_Order) (WC-I-0316, WC-S-0316; concerns WC-C-071 WC-C-076)

### webhook-topics (17 entries, 0 out of the concern map's scope)

Entries: coupon.created; coupon.updated; coupon.deleted; coupon.restored; customer.created; customer.updated; customer.deleted; order.created; order.updated; order.deleted; order.restored; product.created; product.updated; product.deleted; product.restored; product.published; action


### other:onboarding-tasks (17 entries, 0 out of the concern map's scope)

- Set up additional payment options (WC-I-0417, WC-S-0417; concerns WC-C-004)
- Choose your theme (WC-I-0418, WC-S-0418; concerns WC-C-111)
- Customize your store (WC-I-0419, WC-S-0419; concerns WC-C-111)
- Get your products shipped (WC-I-0420, WC-S-0420; concerns WC-C-075)
- Enhance your store with extensions (WC-I-0421, WC-S-0421; concerns WC-C-063)
- Get the free WooCommerce mobile app (WC-I-0422, WC-S-0422; concerns WC-C-090)
- Launch your store (WC-I-0423, WC-S-0423; concerns WC-C-082)
- Grow your business (WC-I-0424, WC-S-0424; concerns WC-C-084)
- Set up payments (WC-I-0425, WC-S-0425; concerns WC-C-004)
- Import your products (WC-I-0426, WC-S-0426; concerns WC-C-067)
- Review shipping options (WC-I-0427, WC-S-0427; concerns WC-C-075)
- Select your shipping options (WC-I-0428, WC-S-0428; concerns WC-C-075)
- You created %s (WC-I-0429, WC-S-0429; concerns WC-C-081)
- You added store details (WC-I-0430, WC-S-0430; concerns WC-C-081)
- Collect sales tax (WC-I-0431, WC-S-0431; concerns WC-C-054)
- Discover ways of extending your store with a tour of the Woo Marketplace (WC-I-0432, WC-S-0432; concerns WC-C-063)
- Get paid with WooPayments (WC-I-0433, WC-S-0433; concerns WC-C-006)

### other:woopayments-doc-topics (16 entries, 0 out of the concern map's scope)

- Account Management (WC-I-0596, WC-S-0801; concerns WC-C-009 WC-C-048)
- Compatibility (WC-I-0597, WC-S-0802; concerns WC-C-006 WC-C-010)
- Currencies (WC-I-0598, WC-S-0803; concerns WC-C-053)
- Customization and Translation (WC-I-0599, WC-S-0804; concerns WC-C-006)
- Fees and Debits (WC-I-0600, WC-S-0805; concerns WC-C-012 WC-C-051)
- Fraud and Disputes (WC-I-0601, WC-S-0806; concerns WC-C-013 WC-C-115 WC-C-116)
- In-Person Payments (WC-I-0602, WC-S-0807; concerns WC-C-014)
- Managing Money and Refunds (WC-I-0603, WC-S-0808; concerns WC-C-007)
- Our Policies (WC-I-0604, WC-S-0809; concerns WC-C-008 WC-C-009 WC-C-011 WC-C-018 WC-C-019 WC-C-049)
- Payment Failures / Declines (WC-I-0605, WC-S-0810; concerns WC-C-006)
- Payment Methods (WC-I-0606, WC-S-0811; concerns WC-C-006)
- Payouts (WC-I-0607, WC-S-0812; concerns WC-C-007 WC-C-051)
- Stripe Capital (WC-I-0608, WC-S-0813; concerns WC-C-016)
- Subscriptions (WC-I-0609, WC-S-0814; concerns WC-C-100)
- Taxes and Documents (WC-I-0610, WC-S-0815; concerns WC-C-021)
- Testing and Troubleshooting (WC-I-0611, WC-S-0816; concerns WC-C-006)

### other:plugin-page-features (13 entries, 1 out of the concern map's scope)

- Create beautiful, enticing storefronts (WC-I-0612, WC-S-0817; concerns WC-C-111)
- Increase revenue (WC-I-0613, WC-S-0818; concerns WC-C-072)
- Customize product pages in minutes (WC-I-0614, WC-S-0819; concerns WC-C-064)
- Showcase physical and digital goods (WC-I-0615, WC-S-0820; concerns WC-C-064)
- Sell subscriptions, bookings, or memberships (WC-I-0616, WC-S-0821; concerns WC-C-100 WC-C-101 WC-C-102)
- Rise to the top of search results (WC-I-0617, WC-S-0822; concerns WC-C-110)
- Choose how you want to get paid (WC-I-0619, WC-S-0824; concerns WC-C-006)
- Configure your shipping options (WC-I-0620, WC-S-0825; concerns WC-C-060 WC-C-061)
- Simplify sales tax (WC-I-0621, WC-S-0826; concerns WC-C-055)
- Grow your business, add features, and monitor your store on the go (WC-I-0622, WC-S-0827; concerns WC-C-084 WC-C-090)
- Own and control your store data – forever (WC-I-0623, WC-S-0828; concerns WC-C-032)
- Connection to WooCommerce.com (WC-I-0624, WC-S-0829; concerns WC-C-063)

Out of the concern map's scope: Build on a platform that scales (A scalability claim on the plugin page; it names no concern with a placement.)


### access-scopes (9 entries, 0 out of the concern map's scope)

Entries: customer; shop_manager; manage_woocommerce; create_customers; view_woocommerce_reports; product, shop_order, shop_coupon; Read; Write; Read/Write


### other:core-shipping-methods (9 entries, 0 out of the concern map's scope)

- Flat rate (flat_rate) (WC-I-0284, WC-S-0284; concerns WC-C-075)
- Free shipping (free_shipping) (WC-I-0285, WC-S-0285; concerns WC-C-075)
- Flat rate (legacy) (legacy_flat_rate) (WC-I-0286, WC-S-0286; concerns WC-C-075)
- Free shipping (legacy) (legacy_free_shipping) (WC-I-0287, WC-S-0287; concerns WC-C-075)
- International flat rate (legacy) (legacy_international_delivery) (WC-I-0288, WC-S-0288; concerns WC-C-075)
- Local delivery (legacy) (legacy_local_delivery) (WC-I-0289, WC-S-0289; concerns WC-C-075)
- Local pickup (legacy) (legacy_local_pickup) (WC-I-0290, WC-S-0290; concerns WC-C-075)
- Local pickup (local_pickup) (WC-I-0291, WC-S-0291; concerns WC-C-075)
- Local pickup (pickup_location) (WC-I-0292, WC-S-0292; concerns WC-C-075)

### other:order-statuses (8 entries, 0 out of the concern map's scope)

- Pending payment (WC-I-0317, WC-S-0317; concerns WC-C-070)
- Processing (WC-I-0318, WC-S-0318; concerns WC-C-070)
- On hold (WC-I-0319, WC-S-0319; concerns WC-C-070)
- Completed (WC-I-0320, WC-S-0320; concerns WC-C-070)
- Cancelled (WC-I-0321, WC-S-0321; concerns WC-C-070)
- Refunded (WC-I-0322, WC-S-0322; concerns WC-C-070 WC-C-071)
- Failed (WC-I-0323, WC-S-0323; concerns WC-C-070)
- Draft (checkout-draft) (WC-I-0324, WC-S-0324; concerns WC-C-070 WC-C-072)

### other:privacy-exporters-erasers (8 entries, 0 out of the concern map's scope)

- add_exporter: WooCommerce Customer Data (WC-I-0357, WC-S-0357; concerns WC-C-045)
- add_exporter: WooCommerce Customer Orders (WC-I-0358, WC-S-0358; concerns WC-C-045)
- add_exporter: WooCommerce Customer Downloads (WC-I-0359, WC-S-0359; concerns WC-C-045 WC-C-066)
- add_exporter: WooCommerce Customer Payment Tokens (WC-I-0360, WC-S-0360; concerns WC-C-045 WC-C-098)
- add_eraser: WooCommerce Customer Data (WC-I-0361, WC-S-0361; concerns WC-C-045)
- add_eraser: WooCommerce Customer Orders (WC-I-0362, WC-S-0362; concerns WC-C-045)
- add_eraser: WooCommerce Customer Downloads (WC-I-0363, WC-S-0363; concerns WC-C-045 WC-C-066)
- add_eraser: WooCommerce Customer Payment Tokens (WC-I-0364, WC-S-0364; concerns WC-C-045 WC-C-098)

### other:shipping-partner-suggestions (6 entries, 0 out of the concern map's scope)

- ShipStation (WC-I-0411, WC-S-0411; concerns WC-C-061)
- Skydropx (WC-I-0412, WC-S-0412; concerns WC-C-061)
- Envia (WC-I-0413, WC-S-0413; concerns WC-C-061)
- Easyship (WC-I-0414, WC-S-0414; concerns WC-C-061)
- Packlink (WC-I-0415, WC-S-0415; concerns WC-C-061)
- WooCommerce Shipping (WC-I-0416, WC-S-0416; concerns WC-C-060)

### other:tos-woo-services (5 entries, 0 out of the concern map's scope)

- WooCommerce (WC-I-0625, WC-S-0458; concerns WC-C-023)
- WooPayments (WC-I-0626, WC-S-0458; concerns WC-C-006 WC-C-023)
- WooCommerce Shipping (WC-I-0627, WC-S-0458; concerns WC-C-023 WC-C-060)
- WooCommerce Tax (WC-I-0628, WC-S-0458; concerns WC-C-023 WC-C-055)
- MailPoet (WC-I-0629, WC-S-0458; concerns WC-C-023 WC-C-113)

### other:core-payment-gateways (4 entries, 0 out of the concern map's scope)

- Direct bank transfer (WC-I-0280, WC-S-0280; concerns WC-C-002)
- Check payments (WC-I-0281, WC-S-0281; concerns WC-C-002)
- Cash on delivery (WC-I-0282, WC-S-0282; concerns WC-C-002)
- PayPal Standard (WC-I-0283, WC-S-0283; concerns WC-C-003)

### other:core-integrations (1 entries, 0 out of the concern map's scope)

- MaxMind Geolocation (WC-I-0293, WC-S-0293; concerns WC-C-046)

## Concerns recorded for this platform

- WC-C-001: Buyer payments through payment gateways (no balance held in core). Terms: Payment gateways; Payments
- WC-C-002: Offline payment methods (direct bank transfer, check, cash on delivery). Terms: Direct bank transfer; Check payments; Cash on delivery; offline
- WC-C-003: PayPal Standard (core gateway that redirects to PayPal). Terms: PayPal Standard
- WC-C-004: Payment provider suggestions per store country (Payments settings). Terms: Payments; Set up payments; payment-gateway-suggestions
- WC-C-005: Third-party payment extensions (Marketplace Official payments). Terms: Official payments; Processors & gateways; Wallets & express checkouts; Buy now pay later; Crypto payments; B2B payments
- WC-C-006: WooPayments payment processing (Woo-made extension and service). Terms: WooPayments
- WC-C-007: WooPayments account balance and payouts. Terms: Payouts; account balance
- WC-C-008: WooPayments reserves (funds withheld for risk). Terms: reserve
- WC-C-009: WooPayments know-your-customer verification. Terms: Know Your Customer; KYC
- WC-C-010: WooPayments availability by country. Terms: WooPayments in Your Country; supported countries
- WC-C-011: Restricted and prohibited businesses on WooPayments. Terms: prohibited or restricted; restricted businesses or activities
- WC-C-012: WooPayments fees. Terms: Fees; Fees and Debits
- WC-C-013: WooPayments fraud protection rules set by the merchant. Terms: fraud protection; Fraud and Disputes
- WC-C-014: WooPayments in-person payments (card readers, Tap to Pay). Terms: In-Person Payments
- WC-C-015: WooPay (saved checkout details across stores). Terms: WooPay
- WC-C-016: Merchant financing (Stripe Capital). Terms: Stripe Capital; Merchant financing
- WC-C-017: Woo Marketplace sales and vendor revenue share. Terms: Woo Marketplace; Marketplace Vendor Agreement; Refund Policy
- WC-C-018: Cardholder data security for WooPayments (PCI DSS). Terms: PCI DSS; Level 1 service provider
- WC-C-019: PCI DSS compliance of the merchant's store. Terms: PCI-DSS compliance and WooCommerce
- WC-C-020: Licence under which WooPayments funds are held and moved. Terms: Connected Account Agreement
- WC-C-021: Tax reporting tied to payments (Form 1099-K, tax invoices for fees). Terms: Taxes and Documents; Form 1099-K; Documents
- WC-C-022: Prohibited items for e-commerce on WordPress.com sites (Store guidelines). Terms: Store guidelines
- WC-C-023: Contracting entity for Woo services. Terms: Woo services; WooCommerce, Inc.; WooCommerce Ireland Ltd.
- WC-C-024: Data controller for Woo services. Terms: Controllers and Responsible Companies
- WC-C-025: Core software licence and warranty. Terms: GPLv3; open-source
- WC-C-026: Governing law and courts. Terms: Jurisdiction and Applicable Law
- WC-C-027: Merchant responsibility for the store's sales, receipts, refunds and consumer law. Terms: Ecommerce Services; Your responsibilities
- WC-C-028: US sanctions on access to Automattic and Woo services. Terms: US Economic Sanctions; OFAC
- WC-C-029: Sanctions and export compliance of the merchant's own sales. Terms: export, import, and sanctions laws
- WC-C-030: Selling and shipping locations. Terms: Selling location(s); Shipping location(s)
- WC-C-031: Checkout rate limiting. Terms: Rate limit Checkout
- WC-C-032: Store data in the merchant's own WordPress database. Terms: Own and control your store data – forever
- WC-C-033: Order storage tables (High-Performance Order Storage). Terms: High-Performance order storage; HPOS
- WC-C-034: Hosting of the store. Terms: WooCommerce Server Recommendations
- WC-C-035: Usage tracking sent to WooCommerce. Terms: WooCommerce usage tracking; wc-telemetry
- WC-C-036: Remote logging to WooCommerce. Terms: Remote Logging
- WC-C-037: Store logs. Terms: Logs; Logging in WooCommerce
- WC-C-038: Store analytics and reports kept in the store. Terms: Analytics; Reports; WooCommerce Analytics
- WC-C-039: WooCommerce Analytics service (data synced to Automattic). Terms: WooCommerce Analytics data syncing
- WC-C-040: Data shared with payment providers. Terms: Privacy considerations when using official payments extensions
- WC-C-041: Data shared with shipping providers. Terms: Privacy considerations when using official shipping extensions
- WC-C-042: WooPayments data and saved-card tokens held by the payment partner. Terms: payment token
- WC-C-043: Transfer outside the EEA and UK of data processed by Automattic. Terms: Transferring Information
- WC-C-044: Automattic as processor of site visitors' data (data processing agreement). Terms: Data Processing Agreement
- WC-C-045: Personal data export, erasure and retention. Terms: Accounts & Privacy; Personal data retention
- WC-C-046: Customer geolocation (MaxMind and IP lookup services). Terms: MaxMind Geolocation; Default customer location
- WC-C-047: Address autocomplete providers. Terms: Address autocomplete; Preferred address autocomplete provider
- WC-C-048: WooPayments dependence on Stripe and processor substitution. Terms: built in partnership with Stripe
- WC-C-049: WordPress.com / Jetpack connection for Woo services. Terms: WordPress.com account; Jetpack connection
- WC-C-050: Woo-made extensions (Developed by Woo). Terms: Developed by Woo
- WC-C-051: WooPayments payout currency and currency conversion. Terms: Payout currencies; currency conversion fee
- WC-C-052: Store currency (one base currency per store). Terms: Currency; base currency
- WC-C-053: Selling in more than one currency (multi-currency). Terms: multi-currency; International and localization
- WC-C-054: Core tax calculation with merchant-entered rates. Terms: Tax; Tax options; Standard rates; Collect sales tax
- WC-C-055: WooCommerce Tax (automated tax calculation service). Terms: WooCommerce Tax; Automated taxes
- WC-C-056: Third-party tax extensions (Sales tax and duties). Terms: Sales tax and duties
- WC-C-057: Taxes on Woo's own fees. Terms: Taxes; VAT/GST/CT on fees
- WC-C-058: Customs duties and import taxes on shipments. Terms: customs charges, import taxes or duties
- WC-C-115: Stripe Radar screening on WooPayments accounts. Terms: Stripe Radar
- WC-C-116: Disputes (chargebacks) on WooPayments transactions. Terms: Managing Disputes; dispute; chargeback
- WC-C-117: Store data synced to Automattic for Jetpack-connected Woo services. Terms: Jetpack Sync; What data does Jetpack sync
- WC-C-059: Third-party extensions and services (general). Terms: Third-Party Services; extensions
- WC-C-060: WooCommerce Shipping (labels and carrier rates). Terms: WooCommerce Shipping
- WC-C-061: Third-party shipping carriers and shipping extensions. Terms: Shipping, delivery and fulfillment; shipping partner suggestions
- WC-C-062: Support for Woo and Marketplace products. Terms: WooCommerce Support Policy
- WC-C-063: WooCommerce.com connection, extension installs and Marketplace subscriptions. Terms: WooCommerce.com; Extensions; Connection to WooCommerce.com
- WC-C-064: Products and catalogue structure (types, variations, attributes, categories, tags, brands). Terms: Products; Product variations; Attributes; Categories; Tags; Brands
- WC-C-065: Product reviews and review requests. Terms: Reviews; Product reviews; Review request
- WC-C-066: Downloadable products and customer downloads. Terms: Downloadable products; Downloads
- WC-C-067: Product import and export (CSV). Terms: Product Import; Product Export; Import your products
- WC-C-068: Inventory and stock levels. Terms: Inventory; Stock
- WC-C-069: Back-in-stock notifications. Terms: Back in Stock Notifications; Stock Notifications
- WC-C-070: Orders and order statuses. Terms: Orders; Order statuses; Order notes
- WC-C-071: Refunds. Terms: Refunds; Order refunds; Refunded
- WC-C-072: Cart and checkout. Terms: Cart; Checkout; Cart & Checkout Blocks; Page setup
- WC-C-073: Customer accounts. Terms: Customers; Customer; Accounts & Privacy
- WC-C-074: Coupons and discounts. Terms: Coupons
- WC-C-075: Shipping zones, methods and classes (core). Terms: Shipping zones; Shipping settings; Classes; Flat rate; Free shipping; Local pickup
- WC-C-076: Transactional emails. Terms: Emails; Email options
- WC-C-077: Webhooks. Terms: Webhooks; webhook topics
- WC-C-078: REST API, API keys and settings API. Terms: WooCommerce REST API; REST API keys; Legacy API
- WC-C-079: Store API (public storefront API). Terms: Store API
- WC-C-080: Roles and capabilities. Terms: Customer; Shop manager; manage_woocommerce
- WC-C-081: Store administration: home, setup wizard, onboarding tasks and inbox. Terms: Home; Setup Wizard; onboarding
- WC-C-082: Site visibility (coming soon and launch). Terms: Site visibility; Coming soon; Launch your store
- WC-C-083: Store status, tools and system report. Terms: Status; System status; Tools
- WC-C-084: Marketing hub (channels, campaigns, recommendations). Terms: Marketing; Overview
- WC-C-085: Order attribution. Terms: Order Attribution
- WC-C-086: Extension framework (settings pages, integrations, admin pages, feature compatibility). Terms: Integration; Settings API; WC_Integration
- WC-C-087: Block extensibility (cart, checkout and product blocks) and Store API extensions. Terms: Cart and Checkout extensibility; Additional checkout fields; ExtendSchema; Product collection block
- WC-C-088: Feature settings (opt-in and opt-out features). Terms: Features
- WC-C-089: Point of Sale in the mobile app. Terms: Point of Sale; POS
- WC-C-090: Mobile app and push notifications. Terms: WooCommerce mobile app; Push Notifications
- WC-C-091: Order withdrawal requests. Terms: Order withdrawal
- WC-C-092: Order fulfillments and shipping providers. Terms: Order Fulfillments; Shipping providers
- WC-C-093: Cost of goods sold. Terms: Cost of Goods Sold
- WC-C-094: Blueprint (export and import of store configuration). Terms: Blueprint (beta)
- WC-C-095: WooCommerce MCP (AI assistant access to the store). Terms: WooCommerce MCP; Model Context Protocol
- WC-C-096: AI features offered by Automattic. Terms: Artificial Intelligence; AI Guidelines
- WC-C-097: Shopper lists (wishlists, save for later). Terms: Wishlists; Save for Later in Cart; shopper-lists
- WC-C-098: Saved payment methods (payment tokens). Terms: Payment Token API; WooCommerce Customer Payment Tokens
- WC-C-099: Reference data (countries, continents). Terms: Data; data/countries; data/continents
- WC-C-100: Subscriptions (recurring billing). Terms: Subscriptions
- WC-C-101: Bookings and appointments. Terms: Bookings and appointments
- WC-C-102: Memberships. Terms: Memberships
- WC-C-103: B2B selling (wholesale, quotes, B2B payments). Terms: B2B; B2B payments
- WC-C-104: Merchandising extensions (bundles, gifts, product options, pricing, display, variations, extra purchases, order options). Terms: Merchandising; Bundles; Gifts; Product options; Pricing; Product display; Product variations; Additional purchases; Order options
- WC-C-105: Conversion extensions (feedback, promotions, order recovery, loyalty, alerts, upsells). Terms: Conversion
- WC-C-106: Customer service extensions (accounts, live chat, customer management, post-purchase, support). Terms: Customer service
- WC-C-107: Store content and customization extensions (checkout features, media, search, page enhancements). Terms: Store content and customizations
- WC-C-108: International and localization extensions. Terms: International and localization
- WC-C-109: Store management extensions (insights, import/export, order management, policy and security, notifications, accounting). Terms: Store management
- WC-C-110: Marketing extensions (advertising, automation, CRM, reporting, sales channels, SEO, email, social). Terms: Marketing
- WC-C-111: Storefront design (themes and block patterns). Terms: Themes; Choose your theme; Customize your store
- WC-C-112: Business services (formation, legal, compliance, insurance, finance). Terms: Business services
- WC-C-113: Email marketing (MailPoet, a Woo service). Terms: MailPoet
- WC-C-114: WooAds (ad campaign data service). Terms: WooAds
- WC-C-118: EU VAT number collection and validation (EU VAT Number, a Woo-made extension). Terms: EU VAT Number
