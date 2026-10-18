# bigcommerce: its own organizing lists, as recorded

From `studies/concern-map/platforms/bigcommerce/inventory.tsv` (569 entries) and `concerns.tsv` (88 concerns). Each entry keeps its `inv_id` and `cite_id`; the citation gives its source at a commit. List names are the inventory's own labels for where each list came from.


## Lists


### webhook-topics (201 entries, 0 out of the concern map's scope)

Entries: store/brand/metafield/created; store/brand/metafield/deleted; store/brand/metafield/updated; store/cart/*; store/cart/created; store/cart/updated; store/cart/deleted; store/cart/couponApplied; store/cart/abandoned; store/cart/converted; store/cart/metafield/created; store/cart/metafield/deleted; store/cart/metafield/updated; store/cart/lineItem/*; store/cart/lineItem/created; store/cart/lineItem/updated; store/cart/lineItem/deleted; store/category/*; store/category/created; store/category/updated; store/category/deleted; store/category/metafield/created; store/category/metafield/deleted; store/category/metafield/updated; store/customer/*; store/customer/created; store/customer/updated; store/customer/deleted; store/customer/address/*; store/customer/address/created; store/customer/address/updated; store/customer/address/deleted; store/customer/payment/instrument/default/updated; store/customer/metafield/created; store/customer/metafield/updated; store/customer/metafield/deleted; store/hook/deliveryException; store/inventory/location/metafield/created; store/inventory/location/metafield/deleted; store/inventory/location/metafield/updated; store/metafield/*; store/metafield/created; store/metafield/updated; store/metafield/deleted; store/modifier/updated; store/option/updated; store/order/*; store/order/created; store/order/updated; store/order/archived; store/order/statusUpdated; store/order/message/created; store/order/refund/created; store/order/transaction/created; store/order/transaction/updated; store/order/metafield/created; store/order/metafield/updated; store/order/metafield/deleted; store/priceList/created; store/priceList/updated; store/priceList/activated; store/priceList/deactivated; store/priceLists/deleted; store/priceList/record/created; store/priceList/record/updated; store/priceList/record/deleted; store/priceList/records/created; store/priceList/records/updated; store/priceList/records/deleted; store/priceList/assignment/updated; store/product/*; store/product/deleted; store/product/created; store/product/updated; store/product/inventory/updated; store/product/inventory/order/updated; store/product/metafield/created; store/product/metafield/updated; store/product/metafield/deleted; store/product/variant/metafield/created; store/product/variant/metafield/updated; store/product/variant/metafield/deleted; store/redirects/updated; store/shipment/*; store/shipment/created; store/shipment/updated; store/shipment/deleted; store/sku/*; store/sku/created; store/sku/updated; store/sku/deleted; store/sku/inventory/updated; store/sku/inventory/order/updated; store/app/uninstalled; store/information/updated; store/store/metafield/created; store/store/metafield/updated; store/store/metafield/deleted; store/subscriber/*; store/subscriber/created; store/subscriber/updated; store/subscriber/deleted; store/channel/*; store/channel/created; store/channel/updated; store/channel/{channel_id}/cart/*; store/channel/{channel_id}/cart/created; store/channel/{channel_id}/cart/updated; store/channel/{channel_id}/cart/deleted; store/channel/{channel_id}/cart/couponApplied; store/channel/{channel_id}/cart/abandoned; store/channel/{channel_id}/cart/converted; store/channel/{channel_id}/cart/lineItem/*; store/channel/{channel_id}/cart/lineItem/created; store/channel/{channel_id}/cart/lineItem/updated; store/channel/{channel_id}/cart/lineItem/deleted; store/channel/{channel_id}/category/*; store/channel/{channel_id}/category/created; store/channel/{channel_id}/category/updated; store/channel/{channel_id}/category/deleted; store/channel/{channel_id}/categoryTree/updated; store/customer/channel/login/access/updated; store/channel/{channel_id}/settings/emailStatus/updated; store/channel/{channel_id}/settings/emailStatus/deleted; store/channel/{channel_id}/email/templates/updated; store/channel/{channel_id}/email/templates/deleted; store/channel/metafield/created/; store/channel/metafield/updated; store/channel/metafield/deleted; store/channel/{channel_id}/notifications/abandonedCart/updated; store/channel/{channel_id}/notifications/inventory/updated; store/channel/{channel_id}/notifications/order/updated; store/channel/{channel_id}/order/*; store/channel/{channel_id}/order/created; store/channel/{channel_id}/order/updated; store/channel/{channel_id}/order/archived; store/channel/{channel_id}/order/statusUpdated; store/channel/{channel_id}/order/message/created; store/channel/{channel_id}/order/refund/created; store/channel/{channel_id}/page/created; store/channel/{channel_id}/page/updated; store/priceList/assignment/updated; store/channel/{channel_id}/product/assigned; store/channel/{channel_id}/product/unassigned; store/channel/{channel_id}/category/product/assigned; store/channel/{channel_id}/category/product/unassigned; store/channel/{channel_id}/settings/route/updated; store/channel/{channel_id}/script/created; store/channel/{channel_id}/script/updated; store/channel/{channel_id}/settings/*; store/channel/{channel_id}/settings/currency/updated; store/channel/{channel_id}/settings/profile/updated; store/channel/{channel_id}/settings/locale/added; store/channel/{channel_id}/settings/locale/updated; store/channel/{channel_id}/settings/locale/deleted; store/channel/{channel_id}/settings/logo/updated; store/channel/{channel_id}/settings/logo/image/updated; store/channel/{channel_id}/settings/favicon/image/updated; store/channel/{channel_id}/settings/checkout/updated; store/channel/{channel_id}/settings/seo/updated; store/channel/{channel_id}/settings/search/updated; store/channel/{channel_id}/settings/inventory/updated; store/channel/{channel_id}/settings/robots/updated; store/channel/{channel_id}/settings/category/updated; store/channel/{channel_id}/settings/product/updated; store/channel/{channel_id}/settings/catalog/updated; store/channel/{channel_id}/settings/security/updated; store/channel/{channel_id}/settings/searchContextFilters/updated; store/channel/{channel_id}/settings/customer/updated; store/channel/{channel_id}/settings/site/updated; store/channel/{channel_id}/settings/site/checkoutUrl/updated; store/channel/{channel_id}/settings/site/checkoutUrl/deleted; store/channel/{channel_id}/socialMediaLinks/updated; store/channel/{channel_id}/theme/configuration/created; store/channel/{channel_id}/theme/configuration/activated; store/channel/*/inventory/product/stock_changed; store/channel/*/inventory/product/low_stock_reached; store/channel/*/inventory/product/out_of_stock_reached; store/channel/*/inventory/product/settings_changed; store/inventory/location/created; store/inventory/location/updated; store/inventory/location/deleted; store/company/created; store/company/updated; store/company/deleted; store/company/statusUpdated; store/company/user/created; store/company/user/updated; store/company/user/deleted; store/company/superadmin/assignmentUpdated; store/company/address/created; store/company/address/updated; store/company/address/deleted; store/superadmin/created; store/superadmin/updated; store/superadmin/deleted; store/superadmin/assignmentUpdated; store/quote/created; store/quote/updated; store/quote/statusUpdated; store/quote/deleted


### api-resources (116 entries, 6 out of the concern map's scope)

Entries: Storefront Carts [rest/storefront/carts]; Storefront Checkouts [rest/storefront/checkouts]; Storefront Cookie Consent [rest/storefront/consent]; Storefront Customers [rest/storefront/customers]; Storefront Subscriptions [rest/storefront/subscriptions]; Storefront Form Fields [rest/storefront/form-fields]; Storefront Orders [rest/storefront/orders]; Storefront Pickup Options [rest/storefront/pickup-options]; Storefront API tokens [rest/admin/authentication-apis/storefront-api-tokens/overview]; Current Customer [rest/admin/authentication-apis/current-customer/overview]; Customer Login (SSO) [rest/admin/authentication-apis/customer-login-api/overview]; Catalog - Brands [rest/admin/catalog/brands]; Catalog - Categories [rest/admin/catalog/categories]; Catalog - Category trees [rest/admin/catalog/category-trees]; Catalog - Products [rest/admin/catalog/products]; Catalog - Product modifiers [rest/admin/catalog/product-modifiers]; Catalog - Product variants [rest/admin/catalog/product-variants]; Catalog - Product variant options [rest/admin/catalog/product-variant-options]; Abandoned Cart Emails [rest/admin/content/abandoned-cart-emails]; Custom Template Associations [rest/admin/content/custom-template-associations]; Email Templates [rest/admin/content/email-templates]; Pages V3 [rest/admin/content/pages]; Marketing [rest/admin/content/marketing]; Content [rest/admin/content/store-content]; Themes [rest/admin/content/themes]; Widgets [rest/admin/content/widgets]; Page widgets [rest/admin/content/page-widgets]; Abandoned carts [rest/admin/management/abandoned-carts]; Carts [rest/admin/management/carts]; Channels [rest/admin/management/channels]; Checkouts [rest/admin/management/checkouts]; Currencies [rest/admin/management/currencies]; Customers V3 [rest/admin/management/customers/v3]; Customers V2 [rest/admin/management/customers/v2]; Customer Segmentation [rest/admin/management/customer-segmentation]; Geography [rest/admin/management/geography]; Infrastructure Hosting [rest/admin/management/infrastructure-hosting]; Inventory [rest/admin/management/inventory]; Orders V2 [rest/admin/management/orders]; Order Operations [rest/admin/management/order-operations]; Pickup [rest/admin/management/pickup]; Pickup Methods [rest/admin/management/pickup/pickup-methods]; Pickup Options [rest/admin/management/pickup/pickup-options]; Pricing [rest/admin/management/pricing]; Price Lists [rest/admin/management/price-lists]; Promotions API [rest/admin/management/promotions]; Promotion Settings API [rest/admin/management/promotion-settings]; Redirects [rest/admin/management/redirects]; Scripts [rest/admin/management/scripts]; Settings V3 [rest/admin/management/settings]; Shipping V2 [rest/admin/management/shipping]; Sites [rest/admin/management/sites]; Store Information [rest/admin/management/store-information/v3]; Store Information V2 [rest/admin/management/store-information/v2]; Subscribers [rest/admin/management/subscribers]; System Logs [rest/admin/management/system-logs]; Tax [rest/admin/management/tax]; Tax Classes [rest/admin/management/tax/tax-classes]; Tax Classes V3 [rest/admin/management/tax/tax-classes/v3]; Tax Classes V2 [rest/admin/management/tax/tax-classes/v2]; Wishlist [rest/admin/management/wishlists]; Payment Processing [rest/admin/payments]; Stored Instruments API (Beta) [rest/admin/payments/stored-instruments]; Payment Methods [rest/admin/payments/methods]; Payment Methods V3 [rest/admin/payments/methods/v3]; Payment Methods V2 [rest/admin/payments/methods/v2]; Transactions API (Beta) [rest/admin/payments/transactions]; Provider APIs [rest/integrations/overview]; Shipping Providers [rest/integrations/shipping-provider]; Tax Provider API [rest/integrations/tax-provider]; Webhooks v3 [rest/integrations/webhooks]; B2B REST APIs [rest/b2b/overview]; Storefront [rest/b2b/storefront]; Authentication [rest/b2b/storefront/authentication]; Catalog [rest/b2b/storefront/catalog]; Companies and Users [rest/b2b/storefront/company]; Orders [rest/b2b/storefront/orders]; Quotes [rest/b2b/storefront/request-for-quote]; Super Admin [rest/b2b/storefront/sales-rep]; Shopping List [rest/b2b/storefront/shopping-list]; Store Settings [rest/b2b/storefront/store-settings]; Management [rest/b2b/management]; Overview [rest/b2b/management/overview]; Addresses [rest/b2b/management/addresses]; Authentication [rest/b2b/management/authentication]; Channels [rest/b2b/management/channels]; Company Management [rest/b2b/management/company]; Company Management [rest/b2b/management/company/companies]; Invoice Management [rest/b2b/management/invoice-management]; Orders [rest/b2b/management/orders]; Payments [rest/b2b/management/payment]; Quotes [rest/b2b/management/quotes]; Sales Staff [rest/b2b/management/sales-staff]; Shopping List [rest/b2b/management/shopping-list]; Super Admin [rest/b2b/management/super-admin]; Users [rest/b2b/management/users]; GraphQL Account API overview [graphql/account/overview]; MCP Server Overview [mcp/overview]; Agent Behavior for Tool Resynchronization [mcp/tool-resynchronization]; Storefront Session Sync [mcp/storefront-session-sync]; B2C Storefront [mcp/storefront/b2c]; B2B Storefront [mcp/storefront/b2b]; Account API [graphql]; Admin API [graphql]; Storefront API [graphql]; B2B API [graphql]; Beta Checkout Extensions; Beta Page Widgets; Beta Powered By; Beta Product Recommendations


Out of the concern map's scope: About Our APIs [about-our-apis] (Overview page of the API reference; it names no resource of its own (the resources it introduces are entries of their own).); Download OpenAPI Specifications [openapi-specifications] (Download page for the OpenAPI specification files; not a resource.); REST API Overview [rest/overview] (Status codes and query parameters common to all REST APIs; not a resource.); Storefront REST APIs [rest/storefront/overview] (Overview page of the API reference; it names no resource of its own (the resources it introduces are entries of their own).); Admin REST APIs [rest/admin/overview] (Overview page of the API reference; it names no resource of its own (the resources it introduces are entries of their own).); GraphQL API Overview [graphql/overview] (Overview page of the API reference; it names no resource of its own (the resources it introduces are entries of their own).)


### access-scopes (60 entries, 0 out of the concern map's scope)

Entries: store_payments_access_token_create; store_storefront_api; store_storefront_api_customer_impersonation; store_app_extensions_manage; store_cart; store_cart_read_only; store_channel_settings; store_channel_settings_read_only; store_channel_listings; store_channel_listings_read_only; store_checkout; store_checkout_read_only; store_content_checkout; store_content_checkout_read_only; store_v2_content; store_v2_content_read_only; store_v2_customers; store_v2_customers_read_only; store_v2_customers_login; store_fulfillment_methods_manage; store_fulfillment_methods_read_only; store_v2_information; store_v2_information_read_only; store_v2_marketing; store_v2_marketing_read_only; store_metafield_change_owner; store_metafield_write; store_metafield_write_all; store_v2_orders; store_v2_orders_read_only; store_order_fulfillment_manage; store_order_fulfillment_read_only; store_v2_transactions; store_v2_transactions_read_only; store_payments_methods_read; store_v2_products; store_v2_products_read_only; store_sites; store_sites_read_only; store_inventory; store_inventory_read_only; store_locations; store_locations_read_only; store_stored_payment_instruments_read_only; store_stored_payment_instruments; store_translations_read_only; store_translations; store_themes_manage; store_themes_read_only; store_b2b_manage; account_read; account_apps_read; account_checkouts_read; account_checkouts_create; account_stores_read; account_subscriptions_read; account_subscriptions_cancel; account_users_read; account_users_write; account_users_delete


### other:product-lines (45 entries, 0 out of the concern map's scope)

- Optimized checkout (BC-I-0497, BC-S-0014; concerns BC-C-016)
- Checkout customization (BC-I-0498, BC-S-0014; concerns BC-C-016)
- Payment freedom (BC-I-0499, BC-S-0014; concerns BC-C-026)
- Digital wallets (BC-I-0500, BC-S-0014; concerns BC-C-027)
- Abandoned cart recovery (BC-I-0501, BC-S-0014; concerns BC-C-015)
- Refunds & returns (BC-I-0502, BC-S-0014; concerns BC-C-021)
- B2B Edition (BC-I-0503, BC-S-0014; concerns BC-C-065)
- Buyer portal (BC-I-0504, BC-S-0014; concerns BC-C-065)
- Customer-specific pricing (BC-I-0505, BC-S-0014; concerns BC-C-065, BC-C-007)
- Customer-specific catalogs (BC-I-0506, BC-S-0014; concerns BC-C-065)
- Sales rep ordering (BC-I-0507, BC-S-0014; concerns BC-C-065)
- Company account hierarchy (BC-I-0508, BC-S-0014; concerns BC-C-065)
- Quoting & CPQ (BC-I-0509, BC-S-0014; concerns BC-C-065)
- Invoicing & net terms (BC-I-0510, BC-S-0014; concerns BC-C-031)
- Requisition lists & reordering (BC-I-0511, BC-S-0014; concerns BC-C-065)
- BigAI (BC-I-0512, BC-S-0014; concerns BC-C-064)
- Feedonomics enrichment (BC-I-0513, BC-S-0014; concerns BC-C-067)
- AI discovery (BC-I-0514, BC-S-0014; concerns BC-C-063)
- Agentic checkout (BC-I-0515, BC-S-0014; concerns BC-C-063)
- Conversational shopping (BC-I-0516, BC-S-0014; concerns BC-C-064)
- BigCommerce Companion (BC-I-0517, BC-S-0014; concerns BC-C-064)
- Feedonomics Surface (BC-I-0518, BC-S-0014; concerns BC-C-067)
- Omnichannel management (BC-I-0519, BC-S-0014; concerns BC-C-038)
- Marketplaces (BC-I-0520, BC-S-0014; concerns BC-C-068)
- Social channels (BC-I-0521, BC-S-0014; concerns BC-C-068)
- Google Shopping (BC-I-0522, BC-S-0014; concerns BC-C-068)
- POS integrations (BC-I-0523, BC-S-0014; concerns BC-C-069)
- Buy online, pick up in store (BC-I-0524, BC-S-0014; concerns BC-C-006)
- Catalog management (BC-I-0525, BC-S-0014; concerns BC-C-001)
- Product filtering (BC-I-0526, BC-S-0014; concerns BC-C-011)
- Inventory management (BC-I-0527, BC-S-0014; concerns BC-C-004)
- Order management (BC-I-0528, BC-S-0014; concerns BC-C-018)
- Shipping (BC-I-0529, BC-S-0014; concerns BC-C-070)
- Tax (BC-I-0530, BC-S-0014; concerns BC-C-072, BC-C-073)
- Reporting & analytics (BC-I-0531, BC-S-0014; concerns BC-C-062)
- Customer groups (BC-I-0532, BC-S-0014; concerns BC-C-034)
- Open APIs (BC-I-0533, BC-S-0014; concerns BC-C-056)
- Headless commerce (BC-I-0534, BC-S-0014; concerns BC-C-050, BC-C-053)
- Composable commerce (BC-I-0535, BC-S-0014; concerns BC-C-059)
- GraphQL Storefront API (BC-I-0536, BC-S-0014; concerns BC-C-053)
- Integrations (BC-I-0537, BC-S-0014; concerns BC-C-059)
- Security & compliance (BC-I-0538, BC-S-0014; concerns BC-C-078, BC-C-028)
- Performance & reliability (BC-I-0539, BC-S-0014; concerns BC-C-083)
- Staging environments (BC-I-0540, BC-S-0014; concerns BC-C-076)
- Big Open Data Solutions (BC-I-0541, BC-S-0014; concerns BC-C-062)

### plan-features (38 entries, 5 out of the concern map's scope)

- Mobile responsive website (BC-I-0397, BC-S-0010; concerns BC-C-042)
- BigCommerce mobile app (BC-I-0398, BC-S-0010; concerns BC-C-077)
- Single-page checkout (BC-I-0399, BC-S-0010; concerns BC-C-016)
- Apple Pay, Google Pay, and Amazon Pay (BC-I-0400, BC-S-0010; concerns BC-C-027)
- Products, file storage, and bandwidth (BC-I-0401, BC-S-0010; concerns BC-C-001)
- Staff accounts (BC-I-0402, BC-S-0010; concerns BC-C-061)
- Coupons, discounts, and gift cards (BC-I-0403, BC-S-0010; concerns BC-C-009, BC-C-010)
- Multi-currency (BC-I-0404, BC-S-0010; concerns BC-C-074)
- Real-time shipping quotes (BC-I-0405, BC-S-0010; concerns BC-C-070)
- Professional reporting tools (BC-I-0406, BC-S-0010; concerns BC-C-062)
- Built-in blog (BC-I-0407, BC-S-0010; concerns BC-C-045)
- Product ratings and reviews (BC-I-0408, BC-S-0010; concerns BC-C-012)
- Free sitewide HTTPS and dedicated SSL (BC-I-0409, BC-S-0010; concerns BC-C-078)
- ShipperHQ shipping rules engine (BC-I-0410, BC-S-0010; concerns BC-C-070)
- Customer groups and segmentation (BC-I-0411, BC-S-0010; concerns BC-C-034)
- Abandoned cart saver (BC-I-0412, BC-S-0010; concerns BC-C-015)
- Persistent cart (BC-I-0413, BC-S-0010; concerns BC-C-014)
- Stored credit cards (BC-I-0414, BC-S-0010; concerns BC-C-024)
- Google customer reviews (BC-I-0415, BC-S-0010; concerns BC-C-012)
- Product filtering (BC-I-0416, BC-S-0010; concerns BC-C-011)
- Custom product filtering (BC-I-0417, BC-S-0010; concerns BC-C-011)
- Price Lists (BC-I-0418, BC-S-0010; concerns BC-C-007)
- Advanced promotions management (BC-I-0419, BC-S-0010; concerns BC-C-009)
- Inventory locations (BC-I-0420, BC-S-0010; concerns BC-C-005)
- GMV cap (BC-I-0421, BC-S-0010; concerns BC-C-030)
- Orders through Embedded Payment Providers (BC-I-0422, BC-S-0010; concerns BC-C-026)
- Open Payment Provider Fee (BC-I-0423, BC-S-0010; concerns BC-C-026, BC-C-030)
- Embedded Payment Provider List (BC-I-0424, BC-S-0010; concerns BC-C-026)
- Online storefront (BC-I-0425, BC-S-0010; concerns BC-C-038)
- Multi-storefront (BC-I-0426, BC-S-0010; concerns BC-C-039)
- Point of sale (BC-I-0427, BC-S-0010; concerns BC-C-069)
- Amazon / eBay / Walmart (BC-I-0428, BC-S-0010; concerns BC-C-068)
- Google / Meta / TikTok / Microsoft / Pinterest (Feedonomics Surface) (BC-I-0429, BC-S-0010; concerns BC-C-067, BC-C-068)

Out of the concern map's scope: 24/7 tech support — chat & email (BigCommerce's own customer support service level, sold with the plan; not a part of the commerce platform's division into concerns.); 24/7 phone support (included) (BigCommerce's own customer support service level, sold with the plan; not a part of the commerce platform's division into concerns.); Express routing & priority support (BigCommerce's own customer support service level, sold with the plan; not a part of the commerce platform's division into concerns.); Customer Success Manager (BigCommerce's own customer support service level, sold with the plan; not a part of the commerce platform's division into concerns.); API support (BigCommerce's own customer support service level, sold with the plan; not a part of the commerce platform's division into concerns.)


### other:embedded-payment-providers (21 entries, 0 out of the concern map's scope)

- BigCommerce Payments (BC-I-0435, BC-S-0011; concerns BC-C-025, BC-C-026)
- Adyen (BC-I-0436, BC-S-0011; concerns BC-C-026)
- Affirm (BC-I-0437, BC-S-0011; concerns BC-C-026)
- Afterpay (BC-I-0438, BC-S-0011; concerns BC-C-026)
- Amazon Pay (BC-I-0439, BC-S-0011; concerns BC-C-026)
- Bank of New Zealand (BC-I-0440, BC-S-0011; concerns BC-C-026)
- Checkout.com (BC-I-0441, BC-S-0011; concerns BC-C-026)
- Clearpay (BC-I-0442, BC-S-0011; concerns BC-C-026)
- Fortis (Acumatica Payments) (BC-I-0443, BC-S-0011; concerns BC-C-026)
- Global Payments (BC-I-0444, BC-S-0011; concerns BC-C-026)
- Klarna (BC-I-0445, BC-S-0011; concerns BC-C-026)
- PayPal Braintree (BC-I-0446, BC-S-0011; concerns BC-C-026)
- PayPal Complete Payments (BC-I-0447, BC-S-0011; concerns BC-C-026)
- PayPal Wallet (BC-I-0448, BC-S-0011; concerns BC-C-026)
- Bluesnap (powered by Payroc) (BC-I-0449, BC-S-0011; concerns BC-C-026)
- Bankful (Pinwheel) (BC-I-0450, BC-S-0011; concerns BC-C-026)
- Sezzle (BC-I-0451, BC-S-0011; concerns BC-C-026)
- Stripe (BC-I-0452, BC-S-0011; concerns BC-C-026)
- TD Online Mart (BC-I-0453, BC-S-0011; concerns BC-C-026)
- Worldpay (BC-I-0454, BC-S-0011; concerns BC-C-026)
- Zip Money (BC-I-0455, BC-S-0011; concerns BC-C-026)

### other:app-marketplace-categories (21 entries, 0 out of the concern map's scope)

- Accounting & Tax (BC-I-0476, BC-S-0013; concerns BC-C-059, BC-C-073)
- Ecommerce AI (BC-I-0477, BC-S-0013; concerns BC-C-059, BC-C-064)
- Analytics & Reporting (BC-I-0478, BC-S-0013; concerns BC-C-059, BC-C-062)
- B2B/Wholesale (BC-I-0479, BC-S-0013; concerns BC-C-059, BC-C-065)
- Catalog & Order Management (BC-I-0480, BC-S-0013; concerns BC-C-059, BC-C-001, BC-C-018)
- Checkout (BC-I-0481, BC-S-0013; concerns BC-C-059, BC-C-016)
- CMS & Hosting (BC-I-0482, BC-S-0013; concerns BC-C-059, BC-C-045)
- CRM & Customer Service (BC-I-0483, BC-S-0013; concerns BC-C-059, BC-C-032)
- Data Transfer/Migration Services (BC-I-0484, BC-S-0013; concerns BC-C-059)
- ERP (BC-I-0485, BC-S-0013; concerns BC-C-059)
- Financing (BC-I-0486, BC-S-0013; concerns BC-C-059, BC-C-026)
- Marketing (BC-I-0487, BC-S-0013; concerns BC-C-059, BC-C-010)
- Merchandising (BC-I-0488, BC-S-0013; concerns BC-C-059)
- Mobile (BC-I-0489, BC-S-0013; concerns BC-C-059)
- Payments & Security (BC-I-0490, BC-S-0013; concerns BC-C-059, BC-C-026)
- POS & In-Store (BC-I-0491, BC-S-0013; concerns BC-C-059, BC-C-069)
- Product & Shipping Protection (BC-I-0492, BC-S-0013; concerns BC-C-059)
- Product Sourcing (BC-I-0493, BC-S-0013; concerns BC-C-059)
- Sales Channels (BC-I-0494, BC-S-0013; concerns BC-C-059, BC-C-068)
- Shipping & Fulfillment (BC-I-0495, BC-S-0013; concerns BC-C-059, BC-C-070, BC-C-071)
- Site Tools (BC-I-0496, BC-S-0013; concerns BC-C-059)

### other:subprocessors (21 entries, 0 out of the concern map's scope)

- Amazon (BC-I-0549, BC-S-0016; concerns BC-C-083, BC-C-082)
- Atlassian (BC-I-0550, BC-S-0016; concerns BC-C-083)
- Cloudflare (BC-I-0551, BC-S-0016; concerns BC-C-083, BC-C-082)
- Confluent (BC-I-0552, BC-S-0016; concerns BC-C-083)
- Google (BC-I-0553, BC-S-0016; concerns BC-C-083, BC-C-082)
- Sentry I/O by Functional Software (BC-I-0554, BC-S-0016; concerns BC-C-083)
- Snowflake (BC-I-0555, BC-S-0016; concerns BC-C-083)
- The Functionary (BC-I-0556, BC-S-0016; concerns BC-C-083)
- Sysdig (BC-I-0557, BC-S-0016; concerns BC-C-083)
- Sumo Logic (BC-I-0558, BC-S-0016; concerns BC-C-083)
- Relyance AI (BC-I-0559, BC-S-0016; concerns BC-C-083)
- ServiceNow Cloud Observability (BC-I-0560, BC-S-0016; concerns BC-C-083)
- Teleport (Gravitational Inc) (BC-I-0561, BC-S-0016; concerns BC-C-083)
- EPAM (BC-I-0562, BC-S-0016; concerns BC-C-083)
- Microsoft (BC-I-0563, BC-S-0016; concerns BC-C-083)
- AgileBits, Inc. (BC-I-0564, BC-S-0016; concerns BC-C-083)
- NewRelic (BC-I-0565, BC-S-0016; concerns BC-C-083)
- Cube27 (BC-I-0566, BC-S-0016; concerns BC-C-083)
- Microsourcing (BC-I-0567, BC-S-0016; concerns BC-C-083)
- FDX South Africa (BC-I-0568, BC-S-0016; concerns BC-C-083)
- Noibu (BC-I-0569, BC-S-0016; concerns BC-C-083)

### legal-agreements (20 entries, 3 out of the concern map's scope)

- Master Services Agreement (BC-I-0456, BC-S-0012; concerns BC-C-079, BC-C-080, BC-C-028, BC-C-083, BC-C-084)
- Privacy Policy (Commerce.com Specific) (BC-I-0457, BC-S-0012; concerns BC-C-081, BC-C-082)
- Privacy Policy (Feedonomics Specific) (BC-I-0458, BC-S-0012; concerns BC-C-067, BC-C-081)
- Privacy Policy (Makeswift Specific) (BC-I-0459, BC-S-0012; concerns BC-C-051, BC-C-081)
- Acceptable Use Policy (BC-I-0460, BC-S-0012; concerns BC-C-085)
- API Terms (BC-I-0461, BC-S-0012; concerns BC-C-056, BC-C-057)
- Fees and Billing Terms (BC-I-0462, BC-S-0012; concerns BC-C-030, BC-C-026)
- Infringing Materials Protocol (BC-I-0463, BC-S-0012; concerns BC-C-088)
- Jurisdiction-Specific Terms (BC-I-0464, BC-S-0012; concerns BC-C-079)
- Merchant-Client Terms (BC-I-0465, BC-S-0012; concerns BC-C-087)
- Mobile App Terms (BC-I-0466, BC-S-0012; concerns BC-C-077)
- Store Terms (BC-I-0467, BC-S-0012; concerns BC-C-086, BC-C-042)
- Data Processing Addendum (BC-I-0468, BC-S-0012; concerns BC-C-081, BC-C-082, BC-C-083)
- Unified Billing Terms (BC-I-0469, BC-S-0012; concerns BC-C-029)
- Unified Billing Terms (US, UK, & Canada) (BC-I-0470, BC-S-0012; concerns BC-C-029)
- Unified Billing Terms (India Specific) (BC-I-0471, BC-S-0012; concerns BC-C-029)
- AI Features Addendum (BC-I-0473, BC-S-0012; concerns BC-C-064, BC-C-063)

Out of the concern map's scope: Professional Services (Program document for BigCommerce's own consulting and implementation services; not a part of the commerce platform's division into concerns.); Website Terms of Use (Governs use of BigCommerce's marketing website, not the commerce services.); Legal Archives (Earlier versions of the agreements; the current versions are entries of their own.)


### settings (19 entries, 0 out of the concern map's scope)

- Analytics (BC-I-0378, BC-S-0009; concerns BC-C-062)
- Catalog (BC-I-0379, BC-S-0009; concerns BC-C-001)
- Email Statuses (BC-I-0380, BC-S-0009; concerns BC-C-046)
- Favicon Image (BC-I-0381, BC-S-0009; concerns BC-C-047)
- Inventory (BC-I-0382, BC-S-0009; concerns BC-C-004)
- Inventory Notifications (BC-I-0383, BC-S-0009; concerns BC-C-004)
- Logo (BC-I-0384, BC-S-0009; concerns BC-C-047)
- Logo Image (BC-I-0385, BC-S-0009; concerns BC-C-047)
- Search Filters (BC-I-0386, BC-S-0009; concerns BC-C-011)
- Store Locale (BC-I-0387, BC-S-0009; concerns BC-C-048)
- Store Profile (BC-I-0388, BC-S-0009; concerns BC-C-047)
- Storefront Category (BC-I-0389, BC-S-0009; concerns BC-C-003)
- Storefront Product (BC-I-0390, BC-S-0009; concerns BC-C-001)
- Storefront Robots.txt (BC-I-0391, BC-S-0009; concerns BC-C-047)
- Storefront Search (BC-I-0392, BC-S-0009; concerns BC-C-011)
- Storefront Security (BC-I-0393, BC-S-0009; concerns BC-C-078)
- Storefront SEO (BC-I-0394, BC-S-0009; concerns BC-C-047)
- Storefront Status (BC-I-0395, BC-S-0009; concerns BC-C-047)
- Units of Measurement (BC-I-0396, BC-S-0009; concerns BC-C-047)

### other:contracting-entities (7 entries, 0 out of the concern map's scope)

- United States | Commerce.com US, Inc., a Texas corporation in the United States | New York (BC-I-0542, BC-S-0015; concerns BC-C-079)
- United Kingdom | Commerce Software UK Ltd., a United Kingdom limited company | England and Wales (BC-I-0543, BC-S-0015; concerns BC-C-079)
- European Union | Commerce Software Ireland Ltd., an Irish limited company | Ireland (BC-I-0544, BC-S-0015; concerns BC-C-079)
- Australia | Commerce.com Pty. Ltd., an Australia proprietary limited company | New South Wales, Australia (BC-I-0545, BC-S-0015; concerns BC-C-079)
- Any other jurisdiction | Commerce.com Pty. Ltd., an Australia proprietary limited company | New York (BC-I-0546, BC-S-0015; concerns BC-C-079)
- Worldwide | Feedonomics Holdings, LLC, a Delaware corporation in the United States | New York | Feedonomics Platform (BC-I-0547, BC-S-0015; concerns BC-C-079, BC-C-067)
- Worldwide | Makeswift, Inc. a Delaware Corporation in the United States | New York | Makeswift visual editor / builder (BC-I-0548, BC-S-0015; concerns BC-C-079, BC-C-051)

## Concerns recorded for this platform

- BC-C-001: Products (catalog products, variants, variant options and modifiers). Terms: Catalog - Products | Catalog - Product variants | Catalog - Product variant options | Catalog - Product modifiers | Products
- BC-C-002: Brands. Terms: Catalog - Brands
- BC-C-003: Categories and category trees. Terms: Catalog - Categories | Catalog - Category trees
- BC-C-004: Inventory. Terms: Inventory | Store Inventory | Inventory management
- BC-C-005: Inventory locations. Terms: Store Locations | Locations | Inventory locations
- BC-C-006: Pickup (buy online, pick up in store). Terms: Pickup | Pickup Methods | Pickup Options | Storefront Pickup Options | Buy online, pick up in store
- BC-C-007: Price lists. Terms: Price Lists
- BC-C-008: Storefront pricing. Terms: Pricing
- BC-C-009: Promotions. Terms: Promotions API | Promotion Settings API | Advanced promotions management
- BC-C-010: Marketing: coupons, banners and gift certificates. Terms: Marketing | Coupons, discounts, and gift cards
- BC-C-011: Product filtering and storefront search. Terms: Search Filters | Storefront Search | Product filtering | Custom product filtering
- BC-C-012: Product ratings and reviews. Terms: Product ratings and reviews | Google customer reviews
- BC-C-013: Product recommendations (beta). Terms: Beta Product Recommendations
- BC-C-014: Carts. Terms: Carts | Storefront Carts | Persistent cart
- BC-C-015: Abandoned carts. Terms: Abandoned carts | Abandoned Cart Emails | Abandoned cart saver
- BC-C-016: Checkouts. Terms: Checkouts | Storefront Checkouts | Checkout Content | Single-page checkout
- BC-C-017: Checkout extensions (beta). Terms: Beta Checkout Extensions
- BC-C-018: Orders. Terms: Orders V2 | Storefront Orders | Orders
- BC-C-019: Order fulfillment and shipments. Terms: Order Fulfillment | Fulfillment Methods | Shipments
- BC-C-020: Order transactions. Terms: Order Transactions | Transactions API (Beta)
- BC-C-021: Refunds. Terms: Refunds | Refunds & returns
- BC-C-022: Payment processing (Payments API). Terms: Payment Processing | Create Payments
- BC-C-023: Payment methods. Terms: Payment Methods | Payment Methods V3 | Payment Methods V2
- BC-C-024: Stored payment instruments. Terms: Stored Instruments API (Beta) | Stored Payment Instruments | Stored credit cards
- BC-C-025: BigCommerce Payments. Terms: BigCommerce Payments | BigCommerce Payments by PayPal
- BC-C-026: Payment providers: Embedded and Open Payment Providers. Terms: Embedded Payment Providers | Open Payment Providers | Open Payment Provider Fee | Embedded Payment Provider List | Payment freedom
- BC-C-027: Digital wallets. Terms: Apple Pay, Google Pay, and Amazon Pay | Digital wallets
- BC-C-028: Payment card security (PCI DSS). Terms: Payment Cards | Checkout Environment; PCI | PCI Compliance
- BC-C-029: Unified Billing (app charges on the BigCommerce invoice). Terms: Unified Billing | Merchant Unified Billing | Unified Billing Partner
- BC-C-030: Fees and billing (subscription, GMV and plan). Terms: Fees and Billing | GMV cap | Open Payment Provider Fees
- BC-C-031: B2B Edition invoices and payments. Terms: Invoice Management | Payments | Invoicing & net terms
- BC-C-032: Customers. Terms: Customers V3 | Customers V2 | Storefront Customers | Storefront Form Fields | Customers
- BC-C-033: Customer login (SSO) and current customer. Terms: Customer Login (SSO) | Current Customer | Customers Login
- BC-C-034: Customer groups and segmentation. Terms: Customer Segmentation | Customer groups and segmentation | Customer groups
- BC-C-035: Subscribers. Terms: Subscribers | Storefront Subscriptions
- BC-C-036: Wishlists. Terms: Wishlist
- BC-C-037: Storefront cookie consent. Terms: Storefront Cookie Consent
- BC-C-038: Channels. Terms: Channels | Channel Settings | Channel Listings | Online storefront | Omnichannel management
- BC-C-039: Multi-Storefront. Terms: Multi-storefront | Multi-Storefront | MSF
- BC-C-040: Sites and routes. Terms: Sites | Sites & Routes
- BC-C-041: Redirects. Terms: Redirects
- BC-C-042: Themes. Terms: Themes | Custom Template Associations | Design Themes
- BC-C-043: Widgets and page widgets. Terms: Widgets | Page widgets | Beta Page Widgets
- BC-C-044: Scripts. Terms: Scripts
- BC-C-045: Pages and store content. Terms: Pages V3 | Content | Built-in blog
- BC-C-046: Email templates and transactional emails. Terms: Email Templates | Email Statuses | Notifications
- BC-C-047: Store profile and storefront settings. Terms: Settings V3 | Store Information V2 | Store Profile | Storefront Status | Storefront SEO | Information & Settings
- BC-C-048: Locales and translations. Terms: Store Locale | Store Translations
- BC-C-049: Metafields. Terms: Metafields | Metafield Ownership | Metafields Access | Store Information
- BC-C-050: Catalyst storefront framework. Terms: Catalyst | Headless commerce
- BC-C-051: Makeswift visual editor. Terms: Makeswift
- BC-C-052: Native Hosting (Infrastructure Hosting). Terms: Infrastructure Hosting | Native Hosting
- BC-C-053: GraphQL Storefront API and storefront API tokens. Terms: Storefront API | GraphQL Storefront API | Storefront API tokens | Storefront API Tokens
- BC-C-054: GraphQL Admin API. Terms: Admin API
- BC-C-055: Account-level resources (GraphQL Account API). Terms: Account API | GraphQL Account API | Account resource scopes
- BC-C-056: API accounts, OAuth scopes and API Terms. Terms: API Accounts | OAuth scopes | API Terms | Open APIs
- BC-C-057: API rate limits. Terms: Rate limits | Volume Limits
- BC-C-058: Webhooks. Terms: Webhooks v3 | Delivery exception hooks
- BC-C-059: Apps and the App Marketplace. Terms: App Marketplace | App Extensions | Apps & Integrations | Integrations
- BC-C-060: System logs and store logs. Terms: System Logs | Store logs
- BC-C-061: Staff accounts and control panel users. Terms: Staff accounts | Account Users
- BC-C-062: Reporting and analytics. Terms: Professional reporting tools | Reporting & analytics | Analytics | Big Open Data Solutions
- BC-C-063: MCP server and agentic commerce. Terms: MCP Server | Agentic checkout | AI discovery | Agentic Search
- BC-C-064: AI features. Terms: AI Features | BigAI | BigCommerce Companion | Conversational shopping | Ecommerce AI
- BC-C-065: B2B Edition (companies, users, quotes, shopping lists, sales staff). Terms: B2B Edition | B2B REST APIs | Buyer portal
- BC-C-066: Powered By (Commerce-as-a-Service). Terms: Powered By | Beta Powered By | Commerce-as-a-Service
- BC-C-067: Feedonomics. Terms: Feedonomics | Feedonomics Surface | Feedonomics Platform | Feedonomics enrichment
- BC-C-068: Marketplaces and social channels. Terms: Amazon / eBay / Walmart | Marketplaces | Social channels | Google Shopping | Sales Channels
- BC-C-069: Point of sale. Terms: Point of sale | POS integrations | POS & In-Store
- BC-C-070: Shipping. Terms: Shipping V2 | Shipping | Real-time shipping quotes | ShipperHQ shipping rules engine
- BC-C-071: Shipping providers. Terms: Shipping Providers
- BC-C-072: Tax configuration. Terms: Tax | Tax Classes | Tax Settings
- BC-C-073: Tax providers. Terms: Tax Provider API | Tax Providers
- BC-C-074: Currencies. Terms: Currencies | Multi-currency
- BC-C-075: Geography (countries and states). Terms: Geography
- BC-C-076: Staging environments. Terms: Staging environments | Staging Pro
- BC-C-077: BigCommerce mobile app. Terms: BigCommerce mobile app | Mobile App Terms | Commerce Mobile Application
- BC-C-078: Storefront HTTPS and storefront security. Terms: Free sitewide HTTPS and dedicated SSL | Storefront Security | Security & compliance
- BC-C-079: Contracting entity and governing law. Terms: Contracting Entity | Commerce Entity | Governing Law
- BC-C-080: Anti-corruption, export and sanctions compliance. Terms: Anti-Corruption, Export and Sanctions Compliance | Sanctions List
- BC-C-081: Personal data processing roles. Terms: Data Processing Addendum | Processor | Controller | Privacy Policy
- BC-C-082: Data transfer and storage location. Terms: Data Transfer | International Data Transfer
- BC-C-083: Subprocessors and hosting services. Terms: Third-Party Subprocessors | Hosting Services
- BC-C-084: Third-Party Products and their integration. Terms: Third-Party Products | Third-Party Product Integration
- BC-C-085: Acceptable use and highly regulated products. Terms: Acceptable Use Policy | Highly Regulated Products
- BC-C-086: Stores and merchant materials. Terms: Store Terms | Stores and Materials | Your Materials | Your Users
- BC-C-087: Agents acting for clients. Terms: Merchant-Client Terms | Agents
- BC-C-088: Infringing materials. Terms: Infringing Materials Protocol
