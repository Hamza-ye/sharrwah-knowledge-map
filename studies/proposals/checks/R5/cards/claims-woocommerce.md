# Cards: what the proposals cite as not found or absent, on woocommerce

6 records, from Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8.

## The points cited

- **Q1, section 1, line 11:** - WooCommerce's reading showed no part of a store holding its own settings for some of its places: its "Selling location(s)" is one setting for the store. Q1-WC-N01, Q1-WC-K0536
- **Q1, section 2, line 73:** - Not taken: WooCommerce's store-wide places, since the other four set prices, currencies and content per place; and Salla's default market holding the store's settings, since explicit store defaults let a setting be set once and differ only where a market overrides it. Q1-WC-N01, Q1-SA-016
- **Q5, section 1, line 11:** - Plans decide too, matching by role: Salla's electronic methods are "متاحة ضمن الباقات المدفوعة فقط"; Zid's Starter plan has only "Basic payment methods (bank transfer, cash on delivery)"; Shopify's custom payment extensions are "limited to eligible Shopify Plus Merchants only". A plan level that decides which methods a store can use was not in what was read on WooCommerce. Q5-SA-P0068, Q5-ZD-P0150, Q5-SH-K1700, Q5-WC-N09
- **Q5, section 1, line 15:** - Fees can follow the provider: BigCommerce's Open Payment Provider fee falls on orders not processed through its Embedded list; in Shopify's store fake-demo-sharrwah (countryCode YE), observed on 5 October 2026, ONERWAY (Direct) in test mode showed a "0.6% transaction fee". A fee that depends on the provider was not in what was read on WooCommerce or Zid. Q5-BC-085, Q5-SH-086, Q5-WC-N08, Q5-ZD-N10
- **Q5, section 5, line 133:** - Which conditions a list entry may carry: plans gate methods on Salla and Zid, while a plan level was not in what was read on WooCommerce; the design keeps conditions as data. A company decision on plans settles it. Q5-SA-P0068, Q5-ZD-P0150, Q5-WC-N09
- **Q5, section 5, line 134:** - A fee that depends on the provider: the design keeps the provider on every payment record. A company decision settles it. Q5-BC-085, Q5-WC-N08
- **Q5, section 6, line 143:** - The international services behind the platforms are closed to Yemen, which forbids them on Yemen's lists as of 2026-10-10: Stripe is unavailable, WooPayments not available (a request to add it is open), and a PayPal account in Yemen cannot receive money. WooPayments for businesses outside its listed countries, and زد باي outside Saudi Arabia and Kuwait, are absent. YA-62 (Unavailable @ Stripe's service, as of 2026-10-10), YA-62 (Not available, a request to add it open @ WooPayments's service, as of 2026-10-10), YK-514 (cannot receive money @ PayPal's service, as of 2026-10-10), Q5-WC-A0002, Q5-ZD-A0002
- **Q5, section 7, line 162:** - Whether Sharrwah charges a fee that depends on the provider an order was paid through, and whether its fees are taken from payments or billed apart. Q5-BC-085, Q5-SH-086, Q5-WC-N08, Q5-ZD-N10
- **Q5, section 7, line 163:** - Whether plans limit which methods a store can offer. Q5-SA-P0068, Q5-ZD-P0150, Q5-WC-N09
- **Q7, section 1, line 8:** - Below the store, Zid also holds prices per market, set for each market and channel "وبعملة السوق نفسها". WooCommerce's reading didn't show groups of countries below the store with their own currency and prices. Q7-ZD-019 Q7-WC-N16
- **Q8, section 1, line 67:** - One feature is "Hidden while incomplete so it can't ship merchant-toggleable". When, or by what steps, a feature moves between these states was not in what was read. Q8-WC-025; Q8-WC-N02
- **Q8, section 2, line 100:** - When an offer moves stage is Sharrwah's call; WooCommerce's steps were not in what was read (rule 4). Q8-WC-N02

## The cards

### Q1-WC-N01

**Cited at:** Q1, section 1, line 11; Q1, section 2, line 73

**Record** (`studies/proposals/records/Q1/woocommerce/not-found.tsv`):
- nf_id: Q1-WC-N01
- bears_on: 1;2
- what_is_missing: a part of one store that groups some of the places it sells to and holds its own settings for them, with the rest taken from the store
- kind: not in what was read
- read: sharrwah-knowledge-map@98f560e89dc72be24b539513a8a7e59f19d096b8:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/102-wordpress.org/text.txt; sharrwah-knowledge-map@98f560e89dc72be24b539513a8a7e59f19d096b8:evidence/product-class/runs/20261011T090749Z-q1r-woocommerce-more-2/items/011-woocommerce.com/text.txt; sharrwah-knowledge-map@98f560e89dc72be24b539513a8a7e59f19d096b8:evidence/product-class/runs/20261012T104936Z-s01-sources/items/093-woocommerce.com/text.txt; woocommerce-11.2.1:src/Internal/Admin/Translations.php; sharrwah-knowledge-map@98f560e89dc72be24b539513a8a7e59f19d096b8:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/081-woocommerce.com/text.txt (read 2026-10-19)
- searched: python3 -I method/corpus_search.py woocommerce "market" "markets" "storefront" "storefronts" "channel" "channels" "language" "languages" "domain" "domains" "catalog" "catalogs" "price list" "price lists" "business entity" "business entities" "merchant of record" "data residency" "stored in Europe" "plan" "plans" "feature flag" "feature flags" "payment methods per country" --max 10 ; opened: wordpress.org/plugins/woocommerce, google-for-woocommerce product-feed page, buy-now-pay-later, src/Internal/Admin/Translations.php, product-category/business-services; not read: the other listed documents (marketing channels code, product pages, extension category pages)
- who_can: agent

### Q5-WC-N09

**Cited at:** Q5, section 1, line 11; Q5, section 5, line 133; Q5, section 7, line 163

**Record** (`studies/proposals/records/Q5/woocommerce/not-found.tsv`):
- nf_id: Q5-WC-N09
- bears_on: 1
- what_is_missing: A plan or subscription level of the platform that decides which payment methods a store can turn on
- kind: not in what was read
- read: sharrwah-knowledge-map@3e1d174b368f5e02692393624d97b26968c1cf54:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/034-woocommerce.com/text.txt (read 2026-10-19); woocommerce-11.2.1:src/StoreApi/Utilities/PaymentUtils.php; woocommerce-11.2.1:includes/admin/settings/class-wc-settings-advanced.php
- searched: python3 -I method/corpus_search.py woocommerce "Adyen" "default payment method" "default payment methods" "selected by default" "custom payment gateway" "custom payment gateways" "plan" "plans" "transaction fee" "transaction fees" "hosting provider" "hosting providers" "PCI DSS" --with "payment gateway" "payment gateways" "payment method" "payment methods" --max 10; opened: https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/ (held), and the release files src/StoreApi/Utilities/PaymentUtils.php and includes/admin/settings/class-wc-settings-advanced.php (searched with grep for default payment method); not read: woocommerce.pot, html-admin-page-status-report.php, class-wc-admin-setup-wizard.php, and the captures our-policies/pci-compliance, buy-now-pay-later (read earlier for other points), products/xero, woopay-customer-documentation, woocommerce-gateway-purchase-order, products, eu-vat-number, order-attribution-tracking, stripe acquirer-disclosure
- who_can: agent

### Q5-WC-N08

**Cited at:** Q5, section 1, line 15; Q5, section 5, line 134; Q5, section 7, line 162

**Record** (`studies/proposals/records/Q5/woocommerce/not-found.tsv`):
- nf_id: Q5-WC-N08
- bears_on: 1
- what_is_missing: A fee the platform charges on orders according to which payment provider processed them
- kind: not in what was read
- read: sharrwah-knowledge-map@3e1d174b368f5e02692393624d97b26968c1cf54:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/034-woocommerce.com/text.txt (read 2026-10-19); woocommerce-11.2.1:src/StoreApi/Utilities/PaymentUtils.php; woocommerce-11.2.1:includes/admin/settings/class-wc-settings-advanced.php
- searched: python3 -I method/corpus_search.py woocommerce "Adyen" "default payment method" "default payment methods" "selected by default" "custom payment gateway" "custom payment gateways" "plan" "plans" "transaction fee" "transaction fees" "hosting provider" "hosting providers" "PCI DSS" --with "payment gateway" "payment gateways" "payment method" "payment methods" --max 10; opened: https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/ (held), and the release files src/StoreApi/Utilities/PaymentUtils.php and includes/admin/settings/class-wc-settings-advanced.php (searched with grep for default payment method); not read: woocommerce.pot, html-admin-page-status-report.php, class-wc-admin-setup-wizard.php, and the captures our-policies/pci-compliance, buy-now-pay-later (read earlier for other points), products/xero, woopay-customer-documentation, woocommerce-gateway-purchase-order, products, eu-vat-number, order-attribution-tracking, stripe acquirer-disclosure
- who_can: agent

### Q5-WC-A0002

**Cited at:** Q5, section 6, line 143

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot-absences.tsv`):
- absence_id: S01-WC-N01
- bullet: e
- what_is_absent: WooPayments for individuals and businesses based in any country that the Supported countries list does not name.
- list_cite_ids: S01-WC-C086;S01-WC-C087
- complete_cite_ids: S01-WC-C088
- note: The Other countries section says the WooCommerce team is working to make WooPayments available to other countries, and that a merchant whose country is not available can vote for it on the WooPayments feature requests page.

**Citation S01-WC-C086 (the list):** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Supported countries | 2026-09-25 | kind: stated | quote check: found
- quote: WooPayments is available for individuals and businesses in: Australia Austria Belgium Bulgaria Canada Croatia Cyprus Czech Republic Denmark Estonia Finland France Germany Greece Hong Kong Hungary Ireland Italy Japan Latvia
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: …cts Expand Woo Marketplace Code Snippets Expand WooPayments / Documentation / WooPayments Documentation / WooPayments: Compatibility / WooPayments in Your Country WooPayments in Your Country If you are an individual or business based in one of our supported countries, you can sign up as a merchant with WooPayments. Once that's done, you can accept payments from customers anywhere in the world in over 100 supported currencies. Supported countries ⟪WooPayments is available for individuals and businesses in: Australia Austria Belgium Bulgaria Canada Croatia Cyprus Czech Republic Denmark Estonia Finland France Germany Greece Hong Kong Hungary Ireland Italy Japan Latvia⟫ Lithuania Luxembourg Malta Netherlands New Zealand Norway Poland Portugal Romania Singapore Slovakia Slovenia Spain Sweden Switzerland United Arab Emirates United Kingdom United States NOTE: If you're using WooPayments for a business, the relevant country is the one where your business is registered - not the one in which you personally live. For example, if you live in South Africa but your business is registered in the Sweden, you can use WooP…

**Citation S01-WC-C087 (the list):** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Supported countries | 2026-09-25 | kind: stated | quote check: found
- quote: Lithuania Luxembourg Malta Netherlands New Zealand Norway Poland Portugal Romania Singapore Slovakia Slovenia Spain Sweden Switzerland United Arab Emirates United Kingdom United States
- title, opening and note boxes: as for this source's citation above
- in context: …ness based in one of our supported countries, you can sign up as a merchant with WooPayments. Once that's done, you can accept payments from customers anywhere in the world in over 100 supported currencies. Supported countries WooPayments is available for individuals and businesses in: Australia Austria Belgium Bulgaria Canada Croatia Cyprus Czech Republic Denmark Estonia Finland France Germany Greece Hong Kong Hungary Ireland Italy Japan Latvia ⟪Lithuania Luxembourg Malta Netherlands New Zealand Norway Poland Portugal Romania Singapore Slovakia Slovenia Spain Sweden Switzerland United Arab Emirates United Kingdom United States⟫ NOTE: If you're using WooPayments for a business, the relevant country is the one where your business is registered - not the one in which you personally live. For example, if you live in South Africa but your business is registered in the Sweden, you can use WooPayments for that business by selecting Sweden when signing up. Outlying territories of France A business must be located in Metropolitan France or within a French overseas region or ter…

**Citation S01-WC-C088 (the words that make the list complete):** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Other countries | 2026-09-25 | kind: stated | quote check: found
- quote: In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries.
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: …tries do not have access to all account types because our partner (Stripe) strictly adheres to the laws and regulations of the country each account is based in. Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type. Engaging in any commercial activities typically requires a trade license or permit in the UAE. Therefore, only the Business account type is available for the UAE. Other countries ↑ Back to top ⟪In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries.⟫ We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country. If you want to use WooPayments, but it's not available in your country, please vote for your country to be supported on the WooPayments feature requests page. On this page Supported countries Outlying territories of France Outlying territories of the Netherlands Outlying territories of the UK Outl…

### Q7-WC-N16

**Cited at:** Q7, section 1, line 8

**Record** (`studies/proposals/records/Q7/woocommerce/not-found.tsv`):
- nf_id: Q7-WC-N16
- bears_on: 2
- what_is_missing: Groups of countries, each with its own currency and prices, set below the store, and how many a plan allows
- kind: not in what was read
- read: sharrwah-knowledge-map@3ca083a8f87c7640ac650906132caf20a3b42697:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/058-woocommerce.com/text.txt (https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/); sharrwah-knowledge-map@3ca083a8f87c7640ac650906132caf20a3b42697:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/040-woocommerce.com/text.txt (https://woocommerce.com/document/shop-currency/); not read: the release files it listed (payment extension suggestions, default payment gateways, setup wizard, homescreen and settings scripts) and https://woocommerce.com/document/woopayments/our-policies/prohibited-and-restricted-products/, https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways/, https://woocommerce.com/document/woocommerce-square/: their snippets name buyers' payment wallets and gateway lists (read 2026-10-19)
- searched: python3 -I method/corpus_search.py woocommerce wallet wallets "cash on delivery" "merchant of record" "merchants of record" "business entity" "business entities" "market currency" "market currencies" "enabled currencies" "presentment currency" "presentment currencies" "product currency" --with currency currencies --max 10
- who_can: agent

### Q8-WC-N02

**Cited at:** Q8, section 1, line 67; Q8, section 2, line 100

**Record** (`studies/proposals/records/Q8/woocommerce/not-found.tsv`):
- nf_id: Q8-WC-N02
- bears_on: 3
- what_is_missing: A WooCommerce statement of when or by what steps a feature on the Features screen moves from the "Experimental features" section to the main list, to enabled by default, or to deprecated_since
- kind: not in what was read
- read: woocommerce-11.2.1:src/Internal/Features/FeaturesController.php; https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/contribution/releases/schedule.md (2026-10-19); https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/contribution/releases/prereleases.md (2026-10-19)
- searched: python3 -I method/corpus_search.py woocommerce "experimental features" "is_experimental" "enabled by default" "opt-out" --max 10; python3 -I method/corpus_search.py woocommerce "release schedule" "release cycle" "feature flag" "beta tester" "release candidate" "monthly release" --max 10; opened FeaturesController.php; not read: abstract-wc-shipping-method.php, wc-update-functions.php, OnboardingTasks/Tasks/Tax.php, OrderMilestoneEasterEgg.php, Internal/Admin/Settings.php, CostOfGoodsSoldController.php, CustomOrdersTableController.php, OrdersTableStatusUnionQuery.php, OrderReviews/Scheduler.php, and the captured pages listed (their snippets concern single settings)
- who_can: agent
- route: read the developer.woocommerce.com documentation on the Features screen and feature flags, live
