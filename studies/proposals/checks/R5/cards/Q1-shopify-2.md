# Cards: Q1 on shopify

29 records cited by `studies/proposals/drafts/Q1/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 39:** - Yemen, as observed on Shopify: for capture-gb-plus on 5 October 2026, with a business entity address of `"countryCode":"YE"`, Shopify Payments was `"eligible":false` and Stripe `"available":false,"eligible":false`; fake-demo-sharrwah, with a Sanaa address, was listed third-party providers that day, Tap Payments and Cybersource among them; and ibx5bt-xy, billed at `"countryCodeV2":"YE"` (29 September 2026), had "Choose a provider" in its saved Payments step text of 30 September 2026. WooCommerce's code (shipped) suggests only `VISA` for store country YE. Q1-SH-094, Q1-SH-098, Q1-SH-095, Q1-SH-103, Q1-SH-092, Q1-SH-123, Q1-WC-K0333
- **section 1, line 43:** - A seller adds a place to sell to, matching on role (basis 4): on Shopify, a market with a Regions condition; on Salla, "+ سوق جديد"; on Zid, a market published or kept "كسوق مخفي"; on BigCommerce, a merchant "creates a new channel to sell in a new context"; on WooCommerce, a country added to the shipped setting "Selling location(s)". Q1-SH-031, Q1-SA-005, Q1-ZD-012, Q1-BC-K0211, Q1-WC-K0536
- **section 1, line 44:** - Shopify's records differ on a market without shipping rates: its help says markets "can be activated only for countries and regions that have shipping rates" (16 October 2026), while one store's saved step text (demo-fake-dev-store, 30 September 2026) held "Region Active" for such a market, whose customers "won’t be able to check out". The proposal rests on what both show: no checkout without shipping rates. Q1-SH-034, Q1-SH-109, Q1-SH-108
- **section 1, line 45:** - A store's first place comes with it, matching on role (basis 4): Shopify creates markets with a new store automatically, and Zid's first market is "السوق الافتراضي وهو السوق المحلي". In the Salla store named demo, observed on 8 October 2026, activating Markets affects "how inventory is deducted" and "cannot be disabled except by contacting the Account Manager". Q1-SH-027, Q1-ZD-003, Q1-SA-107
- **section 1, line 48:** - Shopify's payments terms let it "add a new Designated Country"; BigCommerce says "Additional regions and countries will be launching soon"; WooCommerce ranks "new countries and currencies" partly by store owners' requests. What adding a country involves on the platform's side was not in what was read for Shopify or BigCommerce. Q1-SH-K1604, Q1-BC-P0030, Q1-WC-K0403, Q1-SH-N02, Q1-BC-N04
- **section 1, line 52:** - Changing the store's currency, matching on role (basis 4): on Shopify, where it is "used within your Shopify admin for pricing products and running reports", a change after the first sale goes through Shopify Support, and a store currency dialog's markup in capture-advanced's saved step text (4 October 2026), with nothing to show it was open, lists "Testing payment processors not available in current currency" among reasons for a change; on Salla, "بشرط أن لا يكون هناك طلبات شراء للعملاء"; on Zid, prices are converted "بناءً على سعر الصرف في وقت التغيير"; on WooCommerce, "Your product prices keep the same numbers", and earlier orders keep their currency. Q1-SH-K1935, Q1-SH-K1936, Q1-SH-121, Q1-SA-093, Q1-ZD-K0302, Q1-WC-016
- **section 1, line 53:** - Adding a currency for buyers, matching on role (basis 4): on BigCommerce it takes "the Manage Settings permission"; on WooCommerce, "a multi-currency extension/plugin"; Shopify sets one per market, and with manual rates the conversion fee "is deducted from your payout". Q1-BC-061, Q1-WC-K0751, Q1-SH-058
- **section 1, line 54:** - Shown or charged, matching on role (basis 4): on BigCommerce, for a currency to be transactional "a payment gateway that supports the currency must be enabled", and each added transactional currency gets its own payment methods; on Shopify only Shopify Payments or Adyen "as the primary gateway can process payments in a customer's local currency"; Zid Pay charges in the store's العملة الأساسية, except through K-Net; WooCommerce's Currency Converter Widget "changes the display of prices only". Q1-BC-049, Q1-BC-053, Q1-SH-K1937, Q1-ZD-K0300, Q1-WC-018
- **section 1, line 55:** - Connecting a payment provider, matching on role (basis 4): on Shopify "Only the store owner can add a payment provider"; on Salla the seller copies credentials from their own gateway account (dashboard text, observed 8 October 2026), and for Tabby "Your settlement terms and merchant fees follow your agreement with Tabby"; on Zid the seller enters "مفاتيح الربط"; on BigCommerce, the seller applies to the provider and must "complete underwriting" first; on WooCommerce, gateways "can be added through traditional plugins". Q1-SH-064, Q1-SA-K1656, Q1-SA-089, Q1-ZD-K0094, Q1-BC-P0048, Q1-WC-K0006
- **section 1, line 56:** - The platform's own product can shut out others, matching on role (basis 4): Salla Payments can't be turned on while Tap is linked (dashboard text, observed 8 October 2026); Zid Pay allows no other gateway except Tamara and Tabby; where Shopify Payments is available, "standalone Stripe isn't available as an alternative". Q1-SA-K1653, Q1-ZD-K0089, Q1-SH-K1528
- **section 1, line 57:** - Admitting a provider to the platform, matching on role (basis 4): Shopify's payments apps "must be approved by Shopify"; Zid's providers supply "a file for each country where the payment provider operates"; WooCommerce's vendor agreement, a stated source, requires "a separate agreement with Automattic and/or WooCommerce". Q1-SH-K1697, Q1-ZD-K0082, Q1-WC-K0353
- **section 2, line 67:** - It takes the country of registration from WooPayments; the entity apart from the store, used "for financial products, markets, apps, and taxes in this shop" (capture-gb-plus, observed 5 October 2026), with the store's address in its country (capture-advanced's saved step text, 4 October 2026), from Shopify; and the sign-up country from Salla. Sharrwah verifies it, and it changes only by a controlled change acting on new orders, as Shopify asks a seller to "promptly update your location", a market's entity change "affects only new orders", and Zid wants an empty wallet before a store changes country. Why: apart from the store, it lets one seller run several stores, and a market later use another entity, without changing stored records (rule 3). Q1-WC-K0402, Q1-SH-100, Q1-SH-117, Q1-SA-K1989, Q1-SH-K1271, Q1-SH-043, Q1-ZD-K0230
- **section 2, line 69:** - **Store currency**, proposed: the one currency a store prices and reports in, defaulting from the operating place; the seller changes it freely until the first order, then only through a change that leaves past orders as they were (rule 3). Q1-SH-K1935, Q1-BC-060
- **section 2, line 70:** - It takes the default from BigCommerce and Zid, the lock after orders from Shopify and Salla, and past orders kept from WooCommerce; converting prices at the day's rate, as Zid does, or keeping the numbers, as WooCommerce does, is the seller's choice. Q1-ZD-015, Q1-SH-K1936, Q1-SA-093, Q1-WC-016, Q1-ZD-K0302
- **section 2, line 72:** - It takes store defaults overridden per market from Shopify, whose markets graph view lists a "Business entity" under "Store defaults" in one store's saved step text (demo-fake-dev-store, 30 September 2026), and from BigCommerce; markets made with the store from Shopify and Zid; the hidden state from Zid; and orders that record their market from BigCommerce's storefront attribution. Why: a seller entering a new place adds a market, not a store (rule 1); and with a home market from the start, a second market changes no stored data (rule 3), where Salla's switch-on changes inventory deduction and is undone only through the account manager. Q1-SH-113, Q1-SH-027, Q1-ZD-003, Q1-ZD-012, Q1-BC-003, Q1-SA-107
- **section 2, line 75:** - **Market currency**, proposed: each of a market's currencies is **charged**, so the buyer pays in it, or **shown**, so prices display in it and the buyer pays in the store currency. A currency is charged only where a connected provider supports it, with its own payment methods. Prices are the seller's own or converted at a rate from the **rate source**, rounded as the seller sets, and each order records its rate. Q1-BC-049, Q1-BC-053, Q1-SH-K1937
- **section 2, line 79:** - Not taken now: a Sharrwah payment product that holds sellers' money and shuts out others, as Salla Payments does Tap, Zid Pay most gateways, and Shopify Payments standalone Stripe. The design keeps room for it (section 5); it, and any payment account opened through Sharrwah, goes live only by the founder's decision. Q1-SA-K1653, Q1-ZD-K0089, Q1-SH-K1528
- **section 2, line 81:** - **Tax by place** and **delivery zone**, proposed and left to the build (rule 3): tax rates per place, as in BigCommerce's zones and WooCommerce's country codes; delivery zones as sets of places with methods, a market going live only where its places have one, since on Shopify no checkout runs without shipping rates, and one store's saved step text (capture-grow, 4 October 2026) says that to sell to a zone's countries, "include them in a market". Q1-BC-129, Q1-WC-024, Q1-SH-034, Q1-SH-108, Q1-SH-110
- **section 3, line 86:** - Plugs in: payment providers, through Sharrwah's payments interface after Sharrwah's approval and an agreement, as Shopify approves payments apps, Zid asks for a file per country and WooCommerce for a separate agreement. Q1-SH-K1697, Q1-ZD-K0082, Q1-WC-K0353
- **section 3, line 87:** - Plugs in: the rate source, as WooPayments' rates are "regularly retrieved from the WooPayments server" and Shopify's can be set by hand; and a location lookup, as WooCommerce's "Geolocate". Q1-WC-K0755, Q1-SH-058, Q1-WC-005
- **section 3, line 90:** - Set per store: the store currency and defaults, the plan, and the store's own country, which BigCommerce holds "inherently global" (not checked on Zid). Q1-SH-K1935, Q1-BC-018
- **section 3, line 94:** - Set per plan: how many markets, and which market settings, as Zid's counts and Shopify's per-market theme on "the Advanced plan or higher". Q1-ZD-K0235, Q1-SH-037
- **section 3, line 95:** - Set by Sharrwah: the place register, operating places, the provider catalogue and availability rules, as Shopify keeps its Designated Countries in its terms and WooCommerce its suggestions in code. Q1-SH-K1604, Q1-WC-K0054
- **section 3, line 96:** - Set by the seller: the home place at sign-up, markets, currencies and prices, provider connections, tax rates and delivery zones; on Shopify "Only the store owner can add a payment provider". Q1-SA-K1989, Q1-SH-064
- **section 4, line 112:** 11. Later, and only on the decisions in section 5: a market's own legal entity, a merchant-of-record service, and any arrangement that holds sellers' money through Sharrwah (A-12). Q1-SH-041, Q1-SH-K1958
- **section 5, line 120:** - A market's own legal entity. Shopify Plus lets a market use another entity, whose change "affects only new orders". Keep a market able to name a seller entity, and each order the entity that sold; sellers' demand and the founder settle when it is built. Q1-SH-041, Q1-SH-043
- **section 5, line 121:** - A merchant of record. Shopify's Managed Markets lets a seller sell abroad "without registering a business, registering for tax, or arranging customs clearance", with Global-e as merchant of record. Keep a slot for such a partner on a market, under the guard where it holds sellers' money through Sharrwah; a partner decision settles it (section 7). Q1-SH-K1966, Q1-SH-K1958
- **section 5, line 123:** - Where store data is kept. New Shopify merchants in Europe have their data at rest in Europe, a BigCommerce store's data region is a copied gap, and Yemen's evidence bears on it (section 6). Keep each store's data location, set at creation from its operating place; a company decision with a lawyer settles it. Q1-SH-K2321, Q1-BC-G0154
- **section 5, line 124:** - Markets within markets. A Shopify market inherits from a parent, and "Different customizations follow different inheritance rules". Keep a market able to have a parent; the design settles it. Q1-SH-008, Q1-SH-009
- **section 7, line 141:** - Whether Sharrwah offers a payment product of its own or opens payment accounts for sellers, and under which licence; the platforms' terms tie such products to a regulator, as Salla's transfers to "سلطة وصلاحيات البنك المركزي" and Shopify's Canadian payments entity to the Bank of Canada. Q1-SA-097, Q1-SH-K1614, Q1-WC-K0371, YA-102 (banks and licensed non-bank institutions @ the internationally recognized government's area, as of 2026-02)
- **section 7, line 142:** - Which payment providers Sharrwah works with in each place, and on what agreement. Q1-SH-K1550, Q1-ZD-K0082, Q1-WC-K0353
- **section 7, line 143:** - Which places' sellers may register, which of Yemen's areas Sharrwah serves, and which place follows Yemen. Q1-SH-K1270, Q1-ZD-K0226, YK-12 (split @ Sana'a and Aden, as of 2026), YA-27 (FTO and SDGT @ the United States' area, as of 2025-03-05)
- **section 7, line 145:** - Where sellers' data is stored. Q1-SH-K2321, Q1-BC-G0154, YK-290 (regular books, computer systems kept in Yemen @ the unified Republic's area, as of 2005)
- **section 7, line 146:** - Whether to work with a merchant-of-record partner. Q1-SH-K1958

## The cards

### Q1-SH-092

**Cited at:** section 1, line 39

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-092
- bears_on: 3
- identifier: RequestDetails: billingAddress.countryCodeV2
- statement: "billingAddress":{"id":"gid://shopify/ShopAddress/98503459116","countryCodeV2":"YE","__typename":"ShopAddress"}
- scope: store 2jiwxs-gr, observed 2026-10-06; store capture-advanced, observed 2026-09-30; store capture-client-store-vny2vy5w, observed 2026-10-07; store capture-gb-plus, observed 2026-10-05; store capture-grow, observed 2026-09-30; store capture-plus, observed 2026-09-30; store ctcbwa-r1, observed 2026-09-30; store demo-fake-dev-store, observed 2026-09-29; store fake-demo-sharrwah, observed 2026-09-29; store hjhjhjjjhj, observed 2026-09-29; store ibx5bt-xy, observed 2026-09-29; store ts15uk-ug, observed 2026-10-05; store zyd38b-ze, observed 2026-09-21
- cite_ids: Q1-SH-C192;Q1-SH-C193;Q1-SH-C194;Q1-SH-C195;Q1-SH-C196;Q1-SH-C197;Q1-SH-C198;Q1-SH-C199;Q1-SH-C200;Q1-SH-C201;Q1-SH-C202;Q1-SH-C203;Q1-SH-C204
- from: held
- note: the statement is the first store's answer; each store is cited at one answer; every RequestDetails answer held for these stores gives countryCodeV2 YE; closes Q1-SH-N04 with Q1-SH-093

**Citation Q1-SH-C192:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261006T232216Z-journey-signup-new-account/answers/admin.shopify.com/RequestDetails/0d44fe1d0c18e705adecbcb537d9f53b786f61e3c190a0ed6f2ed818c4265c73.json` | RequestDetails, store 2jiwxs-gr, step 18 | 2026-10-06 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/98503459116","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …iedSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":true,"subCountryMarketsEnabled":true},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/98503459116","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-10-06T23:34:22Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

**Citation Q1-SH-C193:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T232928Z-journey-dev-stores/answers/admin.shopify.com/RequestDetails/35a8bef5c9a915c8a4567d383c67b9a2e8bf2a88c3a643a1c74f3f5c6778253e.json` | RequestDetails, store capture-advanced, step 23 | 2026-09-30 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/79286665321","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/79286665321","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":"unlimited_app_development","__typename":"Shop","createdAt":"2026-09-30T23:44:16Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxPro…

**Citation Q1-SH-C194:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261007T054834Z-journey-client-transfer/answers/admin.shopify.com/RequestDetails/f6222ae3054c15c8ba68493299375c31a4b4d3d6bdbcd991e8beb3842c53ec5c.json` | RequestDetails, store capture-client-store-vny2vy5w, step 1 | 2026-10-07 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/76813402310","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …iedSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":true,"subCountryMarketsEnabled":true},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/76813402310","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-10-07T05:04:21Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

**Citation Q1-SH-C195:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/RequestDetails/fe8b066114d46358c5bbad90bb8dd786184f9c549c88ab6645158b8d059f2171.json` | RequestDetails, store capture-gb-plus, step 5 | 2026-10-05 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/83091816505","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/83091816505","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":"shopify_plus_app_development","__typename":"Shop","createdAt":"2026-10-05T00:25:27Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"max…

**Citation Q1-SH-C196:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T232928Z-journey-dev-stores/answers/admin.shopify.com/RequestDetails/c75e162c029fc15fc6e79728fd0eab43b1a8a0eafe4aada0ab792c7ca5409d33.json` | RequestDetails, store capture-grow, step 18 | 2026-09-30 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/84122501317","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/84122501317","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":"professional_app_development","__typename":"Shop","createdAt":"2026-09-30T23:42:18Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"max…

**Citation Q1-SH-C197:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T232928Z-journey-dev-stores/answers/admin.shopify.com/RequestDetails/ae7b24c94efce755ab79e4adb3f14115bf859d4f93124f588adf173d9d824382.json` | RequestDetails, store capture-plus, step 13 | 2026-09-30 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/101061591336","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/101061591336","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":"shopify_plus_app_development","__typename":"Shop","createdAt":"2026-09-30T23:39:53Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"max…

**Citation Q1-SH-C198:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/RequestDetails/330ffbc0dce2e3095e5cac9b657e653d8144df87b57d15b2144aacbdd7ff1a1d.json` | RequestDetails, store ctcbwa-r1, step 503 | 2026-09-30 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/84760363223","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/84760363223","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-09-29T01:30:15Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

**Citation Q1-SH-C199:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260929T234339Z-m0-trial/answers/admin.shopify.com/RequestDetails/af6a094f6c39b6ab14b2729b743e71c61dc49ff972416c623fe1596e95ce33f0.json` | RequestDetails, store demo-fake-dev-store, step 23 | 2026-09-29 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/77090947207","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/77090947207","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":"basic_app_development","__typename":"Shop","createdAt":"2026-09-29T04:05:45Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProduct…

**Citation Q1-SH-C200:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260929T234339Z-m0-trial/answers/admin.shopify.com/RequestDetails/1b5f22d7b855f5d027eaceb2a6065e21f3c007c276218d501a1f6dbd85be6812.json` | RequestDetails, store fake-demo-sharrwah, step 1 | 2026-09-29 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/84760363223","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/84760363223","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-09-29T01:30:15Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

**Citation Q1-SH-C201:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T003329Z-pilot-import/answers/admin.shopify.com/RequestDetails/557811fd68ebe6eff2ad7f323041a0c9479932ac31be1c7958f06cbc78593b40.json` | RequestDetails, store hjhjhjjjhj, call at 2026-09-29T01:24:35.783Z (import run, no step) | 2026-09-29 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/82604425462","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …gsGBZ-9UL60XjCA","shopifyEmployeeSession":false,"shopifyEmployeeId":null,"features":{"hasInitiatedOnboardingToBanking":false,"hasEverOnboardedToBanking":false,"rbacEnabled":true,"__typename":"ShopFeatures"},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/82604425462","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop"},"staffMember":{"id":"gid://shopify/StaffMember/109583597814","locale":"en","accountAccess":"Account owner","isShopOwner":true,…

**Citation Q1-SH-C202:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260929T234339Z-m0-trial/answers/admin.shopify.com/RequestDetails/12a6a637416d8cff479ca2e47f6d2e9f0d2e85fb9e2f267f4838a64b34d44c3f.json` | RequestDetails, store ibx5bt-xy, step 12 | 2026-09-29 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/83298910421","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/83298910421","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-09-29T03:53:56Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

**Citation Q1-SH-C203:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T115840Z-journey-organization/answers/admin.shopify.com/RequestDetails/2e5a751f64da5269bfe24e19cc3579c225867b298be6677183975e92fea68652.json` | RequestDetails, store ts15uk-ug, step 37 | 2026-10-05 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/85449375980","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …dSpellcastingEnabled":true,"volumePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/85449375980","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-10-05T12:08:54Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

**Citation Q1-SH-C204:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T003329Z-pilot-import/answers/admin.shopify.com/RequestDetails/5fabc9b84175de4928682b7afec2bb26b511253ed98899c1909847df6397b4b3.json` | RequestDetails, store zyd38b-ze, call at 2026-09-21T21:16:33.419Z (import run, no step) | 2026-09-21 | kind: observed | quote check: found
- quote: "billingAddress":{"id":"gid://shopify/ShopAddress/82604425462","countryCodeV2":"YE","__typename":"ShopAddress"}
- in context: …umePricingEnabled":true,"marketsHome":true,"newMarketsPermissions":true,"taxFilingEnabled":false,"sandbox":false,"marketDeliveryProfiles":false,"marketDrivenShipping":false,"subCountryMarketsEnabled":false},⟪"billingAddress":{"id":"gid://shopify/ShopAddress/82604425462","countryCodeV2":"YE","__typename":"ShopAddress"}⟫,"unifiedAdminEnabled":true,"lastActivePriceLookupKey":null,"__typename":"Shop","createdAt":"2026-09-21T21:16:09Z","setupRequired":false,"resourceLimits":{"maxProductOptions":3,"maxProductVariants":2048,"__t…

### Q1-SH-123

**Cited at:** section 1, line 39

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-123
- bears_on: 3;5
- identifier: Settings > Payments: Payment providers
- statement: [heading: Payment providers] Providers that enable you to accept payment methods at a rate set by the third-party. An additional fee will apply to new orders once you select a plan . Choose a provider Additional payment providers Offer methods processed offsite or through custom checkout integrations
- scope: store ibx5bt-xy, observed 2026-09-30
- cite_ids: Q1-SH-C246
- from: held
- note: in the saved HTML of step 376; the step's aria.yaml shows the heading Payment providers, the same sentence and the link Choose a provider; the store's billing address country is in Q1-SH-092

**Citation Q1-SH-C246:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/376.html.txt` | run 20260930T045741Z-sweep-trial2, step 376 (Settings > Payments) | 2026-09-30 | kind: observed | quote check: found
- step 376: visit route payments:settings (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:index,payments:settings:secondary-gateways) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments | "My Store · Payments · Shopify" | 2026-09-30T07:52:56.988Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/376.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/376.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/376.html.txt`
- quote: Providers that enable you to accept payment methods at a rate set by the third-party. An additional fee will apply to new orders once you select a plan . Choose a provider Additional payment providers Offer methods processed offsite or through custom checkout integrations
- in context: … Store 2 stores [Search] Organization Users Billing [initials: MS] [alt: My Store] My Store ibx5bt-xy.myshopify.com General Plan Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Payments] Submit [heading: Payment providers] ⟪Providers that enable you to accept payment methods at a rate set by the third-party. An additional fee will apply to new orders once you select a plan . Choose a provider Additional payment providers Offer methods processed offsite or through custom checkout integrations⟫ Add [heading: Payment configuration] Payment capture method Manual payment methods Payment method customizations Gift card expiration Apple Wallet passes Learn more about payments Close [heading: Secure your account with two-step authentication] Set up two-step You need to set-up two-step authentication before adding a bank account. Two-step authentication helps secure your important details. Once it's turned on, it's much more difficult for una…

### Q1-SH-031

**Cited at:** section 1, line 43

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-031
- bears_on: 4
- identifier: Create a market
- statement: To create a Regional market, select **Regions**, and then select the country or regions to create a market for.
- cite_ids: Q1-SH-C031
- from: held

**Citation Q1-SH-C031:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/set-up-markets.md` | Create a market, step 5 | 2026-10-16 | kind: stated | quote check: found
- quote: To create a Regional market, select **Regions**, and then select the country or regions to create a market for.
- title: Creating and activating markets
- the page opens: You can create markets from the Markets page in your Shopify admin to define where and how you sell to different customer groups. After you create a market, you can configure its customizations and activate it to make it available to customers. Review your default markets When you create a Shopify store, the following markets are created for you automatically: * Domestic market: Your store's home country or region, as determined by your store's address and currency. This is your domestic market …
- headings: Creating and activating markets > Create a market {#create-market}
- in context: …Create market**. 3. In the **Name** section, enter a name for your new market. 4. Next to the name field, select the publishing status for your new market. Select **Active** to display the new market to customers as soon as it's created, or **Draft** to preview the market before displaying it on your online store. 5. In the **Includes** section, click **Add condition**. This condition defines which of your customers the market is displayed to: * ⟪To create a Regional market, select **Regions**, and then select the country or regions to create a market for.⟫ * To create a sub-region market, select **Regions**, open the country you want to target, and then select the states or provinces to create a market for. Learn more about [sub-region markets](/manual/markets/getting-started/market-types#sub-region-markets). * To create a B2B market, select **Company locations**, and then select the company locations to create a market for. To limit the market to one area, use the **in** filter to display only co…

### Q1-SH-034

**Cited at:** section 1, line 44; section 2, line 81

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-034
- bears_on: 4
- identifier: Requirements for using Markets
- statement: You need to have shipping rates configured for all countries and regions that you want to sell to. Markets can be activated only for countries and regions that have shipping rates.
- cite_ids: Q1-SH-C034
- from: held

**Citation Q1-SH-C034:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/requirements-and-considerations.md` | Requirements for using Markets | 2026-10-16 | kind: stated | quote check: found
- quote: You need to have shipping rates configured for all countries and regions that you want to sell to. Markets can be activated only for countries and regions that have shipping rates.
- title: Requirements and considerations for using markets
- the page opens: Before you set up Markets, review the requirements, considerations, staff permissions, and plan availability to make sure Markets fits your business. Requirements for using Markets To use Markets, your store needs to meet the following requirements: * To accept payments in multiple currencies, you need to use Shopify Payments or Adyen as your payment processor. If you use a different payment processor, then customers in all markets pay in your store's default currency. * You need to have shippin…
- a note box: Note Staff permissions can't be assigned per market. If a staff member has permission to view orders, then they can view orders from all markets.
- headings: Requirements and considerations for using markets > Requirements for using Markets
- in context: …Markets fits your business. ## Requirements for using Markets To use Markets, your store needs to meet the following requirements: * To accept payments in multiple currencies, you need to use [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as your payment processor. If you use a different payment processor, then customers in all markets pay in your store's default currency. * ⟪You need to have shipping rates configured for all countries and regions that you want to sell to. Markets can be activated only for countries and regions that have shipping rates.⟫ ## Considerations for using Markets Before you use Markets, review the following considerations: * [Fixed amount discounts](/manual/discounts/discount-types/percentage-fixed-amount) can be created only in your store's default currency. The discount amount is converted to your customer's currency at checkout based on current exchange rates. * [Staff permissions](/manual/your-account/users/roles/permissions) can't be assigned per market. For examp…

### Q1-SH-109

**Cited at:** section 1, line 44

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-109
- bears_on: 4
- identifier: Markets > Capture market: More settings, status
- statement: More settings for Capture market Shipping Not configured No shipping rates Customer privacy Cookie banner, Data sharing opt-out Region Active
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q1-SH-C231
- from: held
- note: in the saved HTML of step 17; the step's aria.yaml shows the same words (Region Active)

**Citation Q1-SH-C231:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/017.html.txt` | run 20260930T170204Z-journey-market, step 17 (Markets > Capture market) | 2026-09-30 | kind: observed | quote check: found
- step 17: Save market (update) | https://admin.shopify.com/store/demo-fake-dev-store/markets/53126234247 | "demo fake dev store · Markets · Capture market · Shopify" | 2026-09-30T17:07:24.789Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/017.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/017.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/017.html.txt`
- quote: More settings for Capture market Shipping Not configured No shipping rates Customer privacy Cookie banner, Data sharing opt-out Region Active
- in context: …ad only Mark all as read [accessibilitylabel: Mark all as read] Alerts about your store and account will show here [heading: Capture market] ⟦hidden⟧ Press enter or space to select a node.You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel. ⟦/hidden⟧ ⟦hidden⟧ Press enter or space to select an edge. You can then press delete to remove it or escape to cancel. ⟦/hidden⟧ Parent market Store default ⟪More settings for Capture market Shipping Not configured No shipping rates Customer privacy Cookie banner, Data sharing opt-out Region Active⟫ More actions [accessibilitylabel: More actions] Edit market handle Delete market View online store Markets [heading: Shipping rates aren't set up] Manage shipping Customers in Capture market won't be able to check out because there are no shipping rates for this market. Create a shipping zone for Capture market and add rates. [accessibilitylabel: Market details] Name [Capture market] [label: Status] Draft Active Includes Saudi Arabia [accessibil…

### Q1-SH-108

**Cited at:** section 1, line 44; section 2, line 81

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-108
- bears_on: 4
- identifier: Markets > Capture market: Shipping rates aren’t set up
- statement: [heading: Shipping rates aren’t set up] Manage shipping Customers in Capture market won’t be able to check out because there are no shipping rates for this market. Create a shipping zone for Capture market and add rates.
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q1-SH-C230
- from: held
- note: in the saved HTML of step 17, after the market including Saudi Arabia was saved; the step's aria.yaml shows the same words; the market name Capture market was typed in the run

**Citation Q1-SH-C230:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/017.html.txt` | run 20260930T170204Z-journey-market, step 17 (Markets > Capture market) | 2026-09-30 | kind: observed | quote check: found
- step 17: Save market (update) | https://admin.shopify.com/store/demo-fake-dev-store/markets/53126234247 | "demo fake dev store · Markets · Capture market · Shopify" | 2026-09-30T17:07:24.789Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/017.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/017.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/017.html.txt`
- quote: Customers in Capture market won’t be able to check out because there are no shipping rates for this market. Create a shipping zone for Capture market and add rates.
- in context: …idden⟧ Press enter or space to select an edge. You can then press delete to remove it or escape to cancel. ⟦/hidden⟧ Parent market Store default More settings for Capture market Shipping Not configured No shipping rates Customer privacy Cookie banner, Data sharing opt-out Region Active More actions [accessibilitylabel: More actions] Edit market handle Delete market View online store Markets [heading: Shipping rates aren't set up] Manage shipping ⟪Customers in Capture market won't be able to check out because there are no shipping rates for this market. Create a shipping zone for Capture market and add rates.⟫ [accessibilitylabel: Market details] Name [Capture market] [label: Status] Draft Active Includes Saudi Arabia [accessibilitylabel: Edit conditions] [heading: Customized] Create unique configurations for customers in this market Inherited Currency Store default Yemeni Rial (YER) Catalogs Only includes products published to Online store All products Discounts Store default All eligible discounts Domain / language Store default demo-fake-dev-store.…

### Q1-SH-027

**Cited at:** section 1, line 45; section 2, line 72

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-027
- bears_on: 4
- identifier: Review your default markets
- statement: When you create a Shopify store, the following markets are created for you automatically:
- cite_ids: Q1-SH-C027
- from: held

**Citation Q1-SH-C027:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/set-up-markets.md` | Review your default markets | 2026-10-16 | kind: stated | quote check: found
- quote: When you create a Shopify store, the following markets are created for you automatically:
- title: Creating and activating markets
- the page opens: You can create markets from the Markets page in your Shopify admin to define where and how you sell to different customer groups. After you create a market, you can configure its customizations and activate it to make it available to customers. Review your default markets When you create a Shopify store, the following markets are created for you automatically: * Domestic market: Your store's home country or region, as determined by your store's address and currency. This is your domestic market …
- headings: Creating and activating markets > Review your default markets
- in context: # Creating and activating markets You can create markets from the [**Markets**](https://admin.shopify.com/markets) page in your Shopify admin to define where and how you sell to different customer groups. After you create a market, you can [configure its customizations and activate it](/manual/markets/getting-started/managing-markets) to make it available to customers. ## Review your default markets ⟪When you create a Shopify store, the following markets are created for you automatically:⟫ * Domestic market: Your store's home country or region, as determined by your store's address and currency. This is your domestic market and represents the default customer experience. The country in your domestic market is set as your backup region by default. * International market: A curated list of countries or regions where merchants similar to you also sell. This market is inactive by default. Review these markets before you start using th…

### Q1-SH-K1604

**Cited at:** section 1, line 48; section 3, line 95

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-066
- placement: decides
- structure: https://www.shopify.com/legal/terms-payfac
- identifier: Part I, D. Assignment and Amendment
- statement: We may amend Part II at any time, in our sole discretion, including to add, remove, or replace an Acquirer for any Designated Country, or to add a new Designated Country.
- cite_ids: SH-S-0137
- note: first run's citation

**Citation SH-S-0137:** `https://www.shopify.com/legal/terms-payfac` | Part I, D. Assignment and Amendment | 2026-09-22 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/147-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/118-shopify.com/text.txt` (fetched 2026-10-12T10:51:24Z, captured)
- quote: We may amend Part II at any time, in our sole discretion, including to add, remove, or replace an Acquirer for any Designated Country, or to add a new Designated Country.
- title: Shopify Payments Facilitator Terms (Merchant Agreement) - Shopify
- in context: …the provision and/or auditing of records requested in relation to inquiries by us, Acquirer, and/or Payment Networks with respect to chargebacks, suspected fraud, and requests for information from us, Acquirer, Payment Networks, tax or other governmental authorities. Assignment and Amendment. You agree and authorize the assignment of this Supplement, without additional approval, to a different Acquirer as determined by us in our sole discretion. ⟪We may amend Part II at any time, in our sole discretion, including to add, remove, or replace an Acquirer for any Designated Country, or to add a new Designated Country.⟫ Your continued use of the services after that time is acceptance of the amended Part II. Help Center. Our Help Center has guides, policies, and instructions that explain how the service works and what we need from you, including information about payments and your account. We may update the Help Center from time to time, and the current version is the one that applies. You can read it at help.shopify.com. If anything in the Help Center conflicts…

### Q1-SH-K1935

**Cited at:** section 1, line 52; section 2, line 69; section 3, line 90

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-107
- placement: decides
- structure: https://help.shopify.com/en/manual/payments/shopify-payments/store-currency/understanding-store-and-payout-currencies.md
- identifier: Store currency
- statement: Your store currency is the currency used within your Shopify admin for pricing products and running reports.
- cite_ids: SH-S-0361
- note: first run's citation

**Citation SH-S-0361:** `https://help.shopify.com/en/manual/payments/shopify-payments/store-currency/understanding-store-and-payout-currencies.md` | Store currency | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/074-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:03Z, captured)
- quote: Your store currency is the currency used within your Shopify admin for pricing products and running reports.
- title: Understanding your store and payout currencies
- the page opens: The currency on your Shopify admin and that is displayed to your customers on your online store is your store currency. The currency your deposits from Shopify Payments orders are made in is your payout currency. Store currency Your store currency is the currency used within your Shopify admin for pricing products and running reports. This is the primary currency that your customers will use when making purchases on your store. You can select any currency from the available options in your store…
- headings: Understanding your store and payout currencies > Store currency
- in context: # Understanding your store and payout currencies The currency on your Shopify admin and that is displayed to your customers on your online store is your **store currency**. The currency your deposits from Shopify Payments orders are made in is your **payout currency**. ## Store currency ⟪Your store currency is the currency used within your Shopify admin for pricing products and running reports.⟫ This is the primary currency that your customers will use when making purchases on your store. You can select any currency from the available options in your store settings based on your customer base's location. Learn more about how to [change your store currency](/manual/payments/shopify-payments/store-currency/changing-your-store-currency). ## Payout currency The payout currency refers to the currency that Shopify Payments uses to deposit mon…

### Q1-SH-K1936

**Cited at:** section 1, line 52; section 2, line 70

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-107
- placement: decides
- structure: https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/account-setup.md
- identifier: help.shopify.com/en/manual/payments/shopify-payments/onboarding/account-setup.md
- statement: If you need to change your store currency after making your first sale, then contact Shopify Support.
- cite_ids: SH-S-0370
- note: first run's citation

**Citation SH-S-0370:** `https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/account-setup.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/063-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:02Z, captured)
- quote: If you need to change your store currency after making your first sale, then contact Shopify Support.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account
- in context: …ng-in/secure-sign-in) is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your [store currency](/manual/intro-to-shopify/initial-setup/setup-business-settings#select-a-store-currency) before making your first sale. It's the currency that will be used throughout your Shopify admin, for pricing your products and viewing your reports. ⟪If you need to change your store currency after making your first sale, then contact Shopify Support.⟫ ## Activating Shopify Payments {#set-up-shopify-payments} You can activate Shopify Payments as your payment gateway from the [**Payments**](https://admin.shopify.com/payments) section of your Shopify admin. If you don't have a payment gateway set up to accept credit and debit cards at checkout, then you can set up Shopify Payments to begin selling. If you have a third-party payment gateway set up, then you can switch to Shopify Payments, or you …

### Q1-SH-121

**Cited at:** section 1, line 52

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-121
- bears_on: 5
- identifier: Settings > General: Change store currency, Reason for changing (optional)
- statement: [label: Reason for changing (optional)] Testing payment processors not available in current currency Default currency does not match my intended choice Experimenting with different markets Other
- scope: store capture-advanced, observed 2026-10-04
- cite_ids: Q1-SH-C244
- from: held
- note: in the saved HTML of step 14 (Settings > General), in the markup of a dialog headed Change store currency, not marked hidden; the step's aria.yaml doesn't show these words; the dialog's Store currency list holds about 160 currencies and was not recorded

**Citation Q1-SH-C244:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T223401Z-journey-business-entity/014.html.txt` | run 20261004T223401Z-journey-business-entity, step 14 (Settings > General) | 2026-10-04 | kind: observed | quote check: found
- step 14: Settings > General | https://admin.shopify.com/store/capture-advanced/settings/general | "capture advanced · General · Shopify" | 2026-10-04T22:37:45.629Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/014.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/014.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T223401Z-journey-business-entity/014.html.txt`
- quote: [label: Reason for changing (optional)] Testing payment processors not available in current currency Default currency does not match my intended choice Experimenting with different markets Other
- in context: …₴) United Arab Emirates Dirham (AED) Uruguayan Peso (UYU $) Uzbekistani Som (UZS) Vanuatu Vatu (VUV) Venezuelan Bolívar (VES) Vietnamese Dong (VND ₫) West African CFA Franc (XOF F CFA) Yemeni Rial (YER) Zambian Kwacha (ZMW ZK) Belarusian Ruble (2000-2016) (BYR) São Tomé & Príncipe Dobra (1977-2017) (STD) São Tomé & Príncipe Dobra (STN Db) Bolívar Soberano (VED) Venezuelan Bolívar (2008-2018) (VEF) Unknown Currency (XXX) XCG (XCG) USDC (USDC USD) ⟪[label: Reason for changing (optional)] Testing payment processors not available in current currency Default currency does not match my intended choice Experimenting with different markets Other⟫ [heading: Change currency formatting] Save Cancel Change how currencies are displayed on your store. {{amount}} and {{amount_no_decimals}} will be replaced with the price of your product. Submit [label: HTML with currency] [label: HTML without currency] [label: Email with currency] [label: Email without currency] My Store 4 stores [Search] Organization Users Billing [initials: ca] [alt: capture advanced] capture advanced capture-advanced.myshopi…

### Q1-SH-058

**Cited at:** section 1, line 53; section 3, line 87

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-058
- bears_on: 5
- identifier: Manual exchange rates
- statement: When you use manual exchange rates, the currency conversion fee isn't added to the customer-facing price. Instead, the fee is deducted from your payout.
- cite_ids: Q1-SH-C058
- from: held

**Citation Q1-SH-C058:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md` | Exchange rates with markets > Manual exchange rates | 2026-10-16 | kind: stated | quote check: found
- quote: When you use manual exchange rates, the currency conversion fee isn't added to the customer-facing price. Instead, the fee is deducted from your payout.
- title: Setting up currencies for markets
- the page opens: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency. You can set a specific currency for each market so that your customers can browse, pay, and receive refunds in a currency that's familiar to them. Displaying prices in local currencies improves the customer experience and can help to increase conversion rates in international m…
- a note box: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency.
- a note box: Sidekick You can ask Sidekick which currency a market shows to buyers, whether local currencies and rounding are turned on, and whether its exchange rate is automatic or manual. Use a prompt such as What currency does each of my markets show buyers and are any using manual exchange rates.
- a note box: Caution When using manual exchange rates, you're responsible for keeping rates current. If your manual rate diverges significantly from the actual exchange rate, then you might experience inaccuracies on international orders. Review your manual rates regularly to ensure they reflect current market c
- headings: Setting up currencies for markets > Exchange rates with markets > Manual exchange rates
- in context: …e rates, you're responsible for keeping rates current. If your manual rate diverges significantly from the actual exchange rate, then you might experience inaccuracies on international orders. Review your manual rates regularly to ensure they reflect current market conditions.</p> </aside> With manual exchange rates, you set a fixed exchange rate for each currency. This gives you full control over the converted price displayed to your customers. ⟪When you use manual exchange rates, the currency conversion fee isn't added to the customer-facing price. Instead, the fee is deducted from your payout.⟫ This means the price the customer pays is exactly what you've set, but your payout is slightly less than the converted amount. #### Steps: 1. From your Shopify admin, go to [**Markets**](https://admin.shopify.com/markets). 2. Click the market that you want to update. 3. In the currency settings, select **Manual**. 4. Enter the exchange rate that you want to use. 5. Click **Save**. Manual exchange rates are a good choice when the following is tru…

### Q1-SH-K1937

**Cited at:** section 1, line 54; section 2, line 75

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-108
- placement: decides
- structure: https://help.shopify.com/en/manual/international/payments.md
- identifier: Shopify Payments and other payment providers
- statement: Only stores with [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway can process payments in a customer's local currency.
- cite_ids: SH-S-0545
- note: first run's citation

**Citation SH-S-0545:** `https://help.shopify.com/en/manual/international/payments.md` | Shopify Payments and other payment providers | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/036-help.shopify.com/text.txt` (fetched 2026-10-11T06:12:59Z, captured)
- quote: Only stores with [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway can process payments in a customer's local currency.
- title: Payments
- the page opens: Your market settings include a payments card that displays eligible local payment methods, as well as a link to your payment settings where you can activate and customize a variety of payment methods. Shopify Payments and other payment providers {#other-payment-providers} Only stores with Shopify Payments or Adyen as the primary gateway can process payments in a customer's local currency. The following payment options are compatible with multi-currency processing: * Shopify Payments credit card …
- a note box: Tip If you want to encourage your customers to use multi-currency compatible payment methods, then use Shopify Scripts to hide other payment providers for customers who have a foreign currency at checkout.
- headings: Payments > Shopify Payments and other payment providers {#other-payment-providers}
- in context: # Payments Your market settings include a payments card that displays eligible [local payment methods](/manual/international/payments#local-payment-methods), as well as a link to your payment settings where you can activate and customize a variety of payment methods. ## Shopify Payments and other payment providers {#other-payment-providers} ⟪Only stores with [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway can process payments in a customer's local currency.⟫ The following payment options are compatible with multi-currency processing: * Shopify Payments credit card payments * Shop Pay * Apple Pay and Google Pay * Paypal Express If you use a different payment provider, then the local currency feature will only affect how prices are displayed to customers in your store. At checkout, the price will be converted to your store's default currency, and your customer will be charged in that currency. Here's …

### Q1-SH-064

**Cited at:** section 1, line 55; section 3, line 96

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-064
- bears_on: 5
- identifier: Activate a credit card payment provider
- statement: Only the store owner can add a payment provider.
- cite_ids: Q1-SH-C064
- from: held

**Citation Q1-SH-C064:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md` | Activate a credit card payment provider, note | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: Only the store owner can add a payment provider.
- title: Configuring third-party payment providers
- the page opens: If you're not using Shopify Payments and you want to accept credit cards, then you can choose from over 100 credit card payment providers for your Shopify store. You can activate or change a payment provider from the Payments page of your Shopify admin. Depending on the requirements of the payment provider, you might be required to submit and verify your bank account information with them so that your store can complete transactions. Contact your payment provider to confirm whether or not you ca…
- a note box: Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner.
- a note box: Note Only the store owner can add a payment provider.
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Configuring third-party payment providers > Activate a credit card payment provider {#activate-credit-card-provider}
- in context: …re providing your bank account information. Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner. Activate a credit card payment provider {#activate-credit-card-provider} You can have only one credit card payment provider activated at a time. If you already have a provider activated, then you can change your credit card payment provider. Note ⟪Only the store owner can add a payment provider.⟫ Steps: Desktop From your Shopify admin, go to Settings > Payments. Do one of the following: If you have Shopify Payments active, then in the Shopify payments section, click Manage. At the bottom of the page, click Switch to a third-party provider, and then click Switch to a third-party provider again to confirm. If you don't have Shopify Payments active, then in the Shopify payments section, click See all other providers. If Shopify Payments isn…  (matched markup removed)

### Q1-SH-K1528

**Cited at:** section 1, line 56; section 2, line 79

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-062
- placement: decides
- structure: https://help.shopify.com/en/manual/payments/third-party-providers/payment-gateway-availability.md
- identifier: Stripe availability in Shopify Payments regions
- statement: then standalone Stripe isn't available as an alternative.
- scope: Shopify Payments regions
- cite_ids: SH-S-0384
- note: first run's citation

**Citation SH-S-0384:** `https://help.shopify.com/en/manual/payments/third-party-providers/payment-gateway-availability.md` | Stripe availability in Shopify Payments regions | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/079-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:03Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/044-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:22Z, captured)
- quote: then standalone Stripe isn't available as an alternative.
- title: Understanding payment gateway availability
- the page opens: When setting up payments on your Shopify store, select payment gateways and providers that are compatible and available in your region. Use the Shopify payment gateways page as your primary resource for up-to-date information about which payment solutions are available for your store. Check payment gateway availability by country You can filter available payment providers by country or region to find detailed and updated information about which payment gateways are available in your store's loca…
- headings: Understanding payment gateway availability > Stripe availability in Shopify Payments regions {#stripe-in-shopify-payments-regions}
- in context: …yments/shopify-payments/supported-countries) where your business is located, then Stripe won't be available for you to activate. This is because Stripe is Shopify Payments' banking partner, and all payment reporting and management takes place in your Shopify admin. If you can't activate Shopify Payments in a supported country, for example, because of [what you sell](/manual/payments/shopify-payments/onboarding/eligibility#prohibited-businesses), ⟪then standalone Stripe isn't available as an alternative.⟫ Instead, [add a third-party payment provider](/manual/payments/third-party-providers) that supports your business type. ## Frequently asked questions about payment gateway availability <div class="accordion-faq"> <details> <summary id="stripe-not-available">Why isn't Stripe available as a payment gateway?</summary> In countries where Shopify Payments is available, Stripe isn't listed as a separate third-party payment gateway, for the reason desc…

### Q1-SH-K1697

**Cited at:** section 1, line 57; section 3, line 86

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-076
- placement: decides
- structure: https://shopify.dev/docs/apps/build/payments.md
- identifier: Considerations table, Approval process
- statement: To make sure merchants can present a positive buyer experience, payments apps must be approved by Shopify.
- cite_ids: SH-S-0442
- note: first run's citation

**Citation SH-S-0442:** `https://shopify.dev/docs/apps/build/payments.md` | Considerations table, Approval process | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (fetched 2026-10-11T06:13:08Z, captured)
- quote: To make sure merchants can present a positive buyer experience, payments apps must be approved by Shopify.
- title: Extensions for payments
- the page opens: Payments extensions integrate with the Shopify admin and checkout to provide customized payment processing services for merchants. Only approved Partners can build payments extensions on Shopify's Payments Platform. Payments extensions provide merchant stores with the following features: * provide additional payment methods * perform specific operations on payment methods * control payment security for buyers * automate payment services, such as reoccurring payments * decide if they want to capt…
- headings: Extensions for payments > Considerations
- in context: …ble introduces the key considerations for Partners that are building payments apps. | Consideration | Description | | - | - | | [Minimum product requirements](https://shopify.dev/docs/apps/build/payments/requirements#technical-requirements) | All payments extensions must adhere to technical requirements and provide a high-quality merchant experience. | | [Approval process](https://shopify.dev/docs/apps/build/payments/payments-extension-review) | ⟪To make sure merchants can present a positive buyer experience, payments apps must be approved by Shopify.⟫ For more information on requirements for payments apps, refer to [Payment extensions requirements](https://shopify.dev/docs/apps/build/payments/requirements). | | [Making your app discoverable](https://shopify.dev/docs/apps/build/payments/onboard-a-merchant-payments-extension) | For a payments extension to appear on Shopify's public list of payment gateways, the payments extension must meet certain criteria. After the criteria are met, Payments …

### Q1-SH-100

**Cited at:** section 2, line 67

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-100
- bears_on: 2;3
- identifier: Settings > General: Business details
- statement: Business details Business entity used for financial products, markets, apps, and taxes in this shop capture gb plus - entity Yemen Manage entities in Organization settings
- scope: store capture-gb-plus, observed 2026-10-05
- cite_ids: Q1-SH-C213
- from: held

**Citation Q1-SH-C213:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/steps/006.text.txt` | step 6 (Settings > General) | 2026-10-05 | kind: observed | quote check: found
- step 6: the new store: Settings > General (business entity, store address, currency) | https://admin.shopify.com/store/capture-gb-plus/settings/general | "capture gb plus · General · Shopify Plus" | 2026-10-05T00:26:18.948Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T002448Z-journey-dev-store-region/steps/006.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T002448Z-journey-dev-store-region/steps/006.html`, `observed-sh@febbf6c98:raw/runs/20261005T002448Z-journey-dev-store-region/steps/006.text.txt`
- quote: Business details Business entity used for financial products, markets, apps, and taxes in this shop capture gb plus - entity Yemen Manage entities in Organization settings
- in context: …ts Analytics Sales channels Online Store Agentic Apps Add Settings My Store 5 stores [Search] Organization Users Billing CGP capture gb plus capture-gb-plus.myshopify.com General Plan Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Markets Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com General ⟪Business details Business entity used for financial products, markets, apps, and taxes in this shop capture gb plus - entity Yemen Manage entities in Organization settings⟫ Store contact details capture gb plus 7amza.it@gmail.com · No phone number Store address Yemen Development store Created at October 5, 2026 Submit Store defaults Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER) Backup Region Yemen [Yemen] Determines settings for customers outside of your markets Unit system Metric system [Metric system] Default weight unit Kilogram (kg) [Kilogram (kg)] Time zone (GMT-05:00…

### Q1-SH-K1271

**Cited at:** section 2, line 67

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-006
- placement: responsible
- structure: https://www.shopify.com/legal/terms
- identifier: 5. Payment of Fees and Taxes
- statement: You must maintain an accurate location in the administrative console of your Shopify Store. If you change jurisdictions you must promptly update your location in the administrative console.
- cite_ids: SH-S-0038
- note: first run's citation

**Citation SH-S-0038:** `https://www.shopify.com/legal/terms` | 5. Payment of Fees and Taxes | 2026-08-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/143-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/117-shopify.com/text.txt` (fetched 2026-10-12T10:51:23Z, captured)
- quote: You must maintain an accurate location in the administrative console of your Shopify Store. If you change jurisdictions you must promptly update your location in the administrative console.
- title: Shopify Terms of Service - Shopify
- in context: …ethod ignoring any such deduction or withholding that may be required. You are solely responsible for determining, collecting, withholding, reporting, and remitting applicable taxes, duties, fees, surcharges and additional charges that arise from or as a result of any sale on your Shopify Store or your use of the Services. The Services are not a marketplace. Any contract of sale made through the Services is directly between you and the customer. ⟪You must maintain an accurate location in the administrative console of your Shopify Store. If you change jurisdictions you must promptly update your location in the administrative console.⟫ Shopify does not provide refunds. Your access to and use of any tools that Shopify offers to you that help you calculate or estimate taxes that arise from or as a result of a sale on your Store ("Shopify Tax") is subject to the Shopify Tax Terms of Service or that help you file such taxes ("Shopify Tax Automated Filing") is subject to the Shopify Tax Automated Filing Terms of Service. 6. Confidentiality Which means Both you and Shopify agree to …

### Q1-SH-043

**Cited at:** section 2, line 67; section 5, line 120

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-043
- bears_on: 2
- identifier: Considerations
- statement: Changing the business entity for a market affects only new orders.
- cite_ids: Q1-SH-C043
- from: held

**Citation Q1-SH-C043:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md` | Considerations | 2026-10-16 | kind: stated | quote check: found
- quote: Changing the business entity for a market affects only new orders.
- title: Setting up business entities for markets
- the page opens: Plan requirement Business entities are available on the Plus plan only. A business entity is the legal entity that processes payments for orders in a market. If your business has different legal entities in different countries or regions, then you can assign specific business entities to specific markets so that payments are processed through the correct entity. By default, all orders in your store are processed through your primary Shopify Payments account, which is associated with your store's…
- a note box: Plan requirement Business entities are available on the Plus plan only.
- a note box: Caution To avoid payments being processed through an incorrect business entity, verify that your submarkets are inheriting the expected business entity. If there's any ambiguity due to multiple parents, then add an explicit business entity customization to the submarket.
- a note box: Caution Before you can assign business entities to markets, you need to set up additional Shopify Payments accounts for each legal entity. Refer to Selling with multiple entities to learn more.
- headings: Setting up business entities for markets > Considerations
- in context: …uropean customers' payments are processed by the UK entity. This is important for businesses that need to comply with local payment regulations, simplify tax reporting, or manage payouts in different currencies through local bank accounts. ## Considerations Before you set up business entities to use with Markets, review the following considerations: * Business entities are relevant only for stores using Shopify Payments with multiple accounts. * ⟪Changing the business entity for a market affects only new orders.⟫ Existing orders continue to be associated with the business entity that was active when the order was placed. * If you don't add a business entity customization to a market, then orders in that market are processed through your default Shopify Payments account. * Some regions have regulations about which entity can process payments for customers in that region. Verify with a legal or finance expert that your business entity assignments comply wi…

### Q1-SH-113

**Cited at:** section 2, line 72

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-113
- bears_on: 1;2
- identifier: Markets > Markets graph view: Store defaults
- statement: Store defaults demo-fake-dev-store.myshopify.com English [accessibilitylabel: Loading…] 15 products Yemeni Rial (YER) 7 discounts Eligibility varies by buyer demo fake dev store - entity Business entity demo fake dev store configuration Checkout and accounts Not collecting Taxes and duties No rules set Returns and cancellations
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q1-SH-C235;Q1-SH-C236
- from: held
- note: in the saved HTML of step 90; the step's aria.yaml shows the same items under the tree item Store defaults, each market a child of it

**Citation Q1-SH-C235:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/090.html.txt` | run 20260930T170204Z-journey-market, step 90 (Markets > Markets graph view) | 2026-09-30 | kind: observed | quote check: found
- step 90: Graph view | https://admin.shopify.com/store/demo-fake-dev-store/markets/graph | "demo fake dev store · Markets · Markets graph view · Shopify" | 2026-09-30T18:44:56.573Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/090.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/090.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/090.html.txt`
- quote: Store defaults demo-fake-dev-store.myshopify.com English
- in context: …lt: My Store] My Store My Store [initials: MS] [alt: My Store] My Store Create store [initials: Dd] [alt: Demo-name demo-last-name] Demo-name demo-last-name 7amza.it@gmail.com Log out Alerts View unread only Mark all as read [accessibilitylabel: Mark all as read] Alerts about your store and account will show here [heading: Markets graph view] Create market View as List view [accessibilitylabel: Back to Capture market page] Capture market Markets ⟪Store defaults demo-fake-dev-store.myshopify.com English⟫ [accessibilitylabel: Loading...] 15 products Yemeni Rial (YER) 7 discounts Eligibility varies by buyer demo fake dev store - entity Business entity demo fake dev store configuration Checkout and accounts Not collecting Taxes and duties No rules set Returns and cancellations Canada Capture market Draft European Union United States Yemen ⟦hidden⟧ Press enter or space to select a node.You can then use the arrow keys to move the node around. Press d…

**Citation Q1-SH-C236:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/090.html.txt` | run 20260930T170204Z-journey-market, step 90 (Markets > Markets graph view) | 2026-09-30 | kind: observed | quote check: found
- step 90: Graph view | https://admin.shopify.com/store/demo-fake-dev-store/markets/graph | "demo fake dev store · Markets · Markets graph view · Shopify" | 2026-09-30T18:44:56.573Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/090.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/090.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/090.html.txt`
- quote: 15 products Yemeni Rial (YER) 7 discounts Eligibility varies by buyer demo fake dev store - entity Business entity demo fake dev store configuration Checkout and accounts Not collecting Taxes and duties No rules set Returns and cancellations
- title, opening and note boxes: as for this source's citation above
- in context: …ials: Dd] [alt: Demo-name demo-last-name] Demo-name demo-last-name 7amza.it@gmail.com Log out Alerts View unread only Mark all as read [accessibilitylabel: Mark all as read] Alerts about your store and account will show here [heading: Markets graph view] Create market View as List view [accessibilitylabel: Back to Capture market page] Capture market Markets Store defaults demo-fake-dev-store.myshopify.com English [accessibilitylabel: Loading...] ⟪15 products Yemeni Rial (YER) 7 discounts Eligibility varies by buyer demo fake dev store - entity Business entity demo fake dev store configuration Checkout and accounts Not collecting Taxes and duties No rules set Returns and cancellations⟫ Canada Capture market Draft European Union United States Yemen ⟦hidden⟧ Press enter or space to select a node.You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel. ⟦/hidden⟧ ⟦hidden⟧ Press enter or space to select an edge. You can then press delete to remove it or escape to cancel. ⟦/hidden⟧ [accessibilitylabel: Zoom controls, currently 88%] 88% Zoom in ⇧ + Zoom out ⇧ - Zoom to 100% ⇧ 0 Zoom to …

### Q1-SH-110

**Cited at:** section 2, line 81

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-110
- bears_on: 4
- identifier: Settings > Shipping and delivery > General profile: Shipping zones
- statement: Shipping zones Domestic Yemen Standard 3–5 business days ﷼2600.00 Add shipping option International United Arab Emirates, Austria, Australia, 25 more To start selling to 27 countries/regions in this zone, include them in a market
- scope: store capture-grow, observed 2026-10-04
- cite_ids: Q1-SH-C232
- from: held
- note: in the saved HTML of step 60; the step's aria.yaml shows the same words

**Citation Q1-SH-C232:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T092557Z-sweep-instances/060.html.txt` | run 20261004T092557Z-sweep-instances, step 60 (Settings > Shipping and delivery > General profile) | 2026-10-04 | kind: observed | quote check: found
- step 60: visit route delivery-profile:update (path from linked from 20261002T004032Z-sweep-capture-grow step 484) | https://admin.shopify.com/store/capture-grow/settings/shipping/profiles/117465678021 | "capture grow · Shipping and delivery · General profile · Shopify" | 2026-10-04T10:39:49.556Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T092557Z-sweep-instances/steps/060.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T092557Z-sweep-instances/steps/060.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T092557Z-sweep-instances/060.html.txt`
- quote: Shipping zones Domestic Yemen Standard 3–5 business days ﷼2600.00 Add shipping option International United Arab Emirates, Austria, Australia, 25 more To start selling to 27 countries/regions in this zone, include them in a market
- in context: …s channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: General profile] [accessibilitylabel: Shipping and delivery] [heading: Products] All products not in other profiles New products are added by default [accessibilitylabel: Fulfillment location] Fulfillment location Open location details Shop location Yemen Add location ⟪Shipping zones Domestic Yemen Standard 3-5 business days ریال2600.00 Add shipping option International United Arab Emirates, Austria, Australia, 25 more To start selling to 27 countries/regions in this zone, include them in a market⟫ Free International Shipping 20kg and up Free International ریال4500.00 International Shipping ریال30.00 Add shipping option Add zone [heading: Not fulfilling from] Open location details My Custom Location 123 Main St, Toronto Ontario A1A 1A1, Canada Start shipping Snow City Warehouse App Start shipping Close

### Q1-SH-037

**Cited at:** section 3, line 94

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-037
- bears_on: 1
- identifier: Considerations for using Markets
- statement: Per-market theme customization, such as showing different section content, banners, or layouts for different markets, requires the Advanced plan or higher. On other plans, all markets share the same theme customization.
- scope: Advanced plan or higher
- cite_ids: Q1-SH-C037
- from: held

**Citation Q1-SH-C037:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/requirements-and-considerations.md` | Considerations for using Markets | 2026-10-16 | kind: stated | quote check: found
- quote: Per-market theme customization, such as showing different section content, banners, or layouts for different markets, requires the Advanced plan or higher. On other plans, all markets share the same theme customization.
- title: Requirements and considerations for using markets
- the page opens: Before you set up Markets, review the requirements, considerations, staff permissions, and plan availability to make sure Markets fits your business. Requirements for using Markets To use Markets, your store needs to meet the following requirements: * To accept payments in multiple currencies, you need to use Shopify Payments or Adyen as your payment processor. If you use a different payment processor, then customers in all markets pay in your store's default currency. * You need to have shippin…
- a note box: Note Staff permissions can't be assigned per market. If a staff member has permission to view orders, then they can view orders from all markets.
- headings: Requirements and considerations for using markets > Considerations for using Markets
- in context: …erted to your customer's currency at checkout based on current exchange rates. * [Staff permissions](/manual/your-account/users/roles/permissions) can't be assigned per market. For example, if a staff member has the permission to view **Orders**, then they can view orders in all your store's markets. * Only one theme can be published at a time. You can customize your theme per market, but customizations must be applied to your published theme. * ⟪Per-market theme customization, such as showing different section content, banners, or layouts for different markets, requires the Advanced plan or higher. On other plans, all markets share the same theme customization.⟫ Learn more about [customizing your online store for markets](/manual/markets/customizations/online-store). * [Post-purchase apps](/manual/checkout-settings/customize-checkout-configurations/checkout-apps#post-purchase-offers) work only in your store's default currency. Post-purchase offers aren't displayed for customers in markets that use a different currency. * Only customers from countries or regions in an active market can check out. If you …

### Q1-SH-K1958

**Cited at:** section 4, line 112; section 5, line 121; section 7, line 146

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-110
- placement: responsible
- structure: https://help.shopify.com/en/manual/international/managed-markets.md
- identifier: help.shopify.com/en/manual/international/managed-markets.md
- statement: When you use Managed Markets, Global-e becomes the _merchant of record_.
- cite_ids: SH-S-0563
- note: first run's citation

**Citation SH-S-0563:** `https://help.shopify.com/en/manual/international/managed-markets.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/034-help.shopify.com/text.txt` (fetched 2026-10-11T06:12:59Z, captured)
- quote: When you use Managed Markets, Global-e becomes the _merchant of record_.
- title: Managed Markets
- the page opens: Managed Markets expands the capabilities of the international sales tools. Along with tools that help you to set up and manage selling in international markets, Managed Markets offers additional features powered by Global-e to help you scale and optimize your international markets directly from your Shopify admin. Managed Markets is only available to merchants based in the continental United States, and to certain stores in Canada and the United Kingdom. Read more about the requirements and cons…
- headings: Managed Markets
- in context: …Managed Markets offers additional features powered by Global-e to help you scale and optimize your international markets directly from your Shopify admin. Managed Markets is only available to merchants based in the continental United States, and to certain stores in Canada and the United Kingdom. Read more about the [requirements and considerations](/manual/international/managed-markets/requirements-and-considerations) for using Managed Markets. ⟪When you use Managed Markets, Global-e becomes the _merchant of record_.⟫ A merchant of record is the legal entity responsible for selling products to a customer, and for adhering to local laws and regulations in another region or country. Unless another party such as Global-e is hired to take on these responsibilities, most merchants act as their own merchant of record. When you act as your own merchant of record, you're responsible for registering for and remitting taxes, arranging to accept local methods of payment…

### Q1-SH-K1966

**Cited at:** section 5, line 121

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-110
- placement: reason
- structure: https://help.shopify.com/en/manual/international/managed-markets/overview.md
- identifier: help.shopify.com/en/manual/international/managed-markets/overview.md
- statement: You can use Managed Markets to sell to customers in other countries without registering a business, registering for tax, or arranging customs clearance in each destination.
- cite_ids: SH-S-0634
- note: first run's citation

**Citation SH-S-0634:** `https://help.shopify.com/en/manual/international/managed-markets/overview.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/035-help.shopify.com/text.txt` (fetched 2026-10-11T06:12:59Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/028-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:06Z, captured)
- quote: You can use Managed Markets to sell to customers in other countries without registering a business, registering for tax, or arranging customs clearance in each destination.
- title: Overview of Managed Markets
- the page opens: You can use Managed Markets to sell to customers in other countries without registering a business, registering for tax, or arranging customs clearance in each destination. Your customers buy from your store, in your brand's checkout, and pay in their own currency. Their order arrives without a surprise bill at the door. Managed Markets builds on Shopify Markets, the tools built into every store for selling in other countries, including localized domains and store translation. With Shopify Marke…
- headings: Overview of Managed Markets
- in context: # Overview of Managed Markets ⟪You can use Managed Markets to sell to customers in other countries without registering a business, registering for tax, or arranging customs clearance in each destination.⟫ Your customers buy from your store, in your brand's checkout, and pay in their own currency. Their order arrives without a surprise bill at the door. Managed Markets builds on [Shopify Markets](/manual/markets), the tools built into every store for selling in other countries, including localized domains and [store translation](/manual/international/languages). With Shopify Markets on its own, you remain the [merchant of record](#merchant-of-reco…

### Q1-SH-K2321

**Cited at:** section 5, line 123; section 7, line 145

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-181
- placement: where
- structure: https://help.shopify.com/en/manual/privacy-and-security/privacy/international-data-transfers/onward-transfers.md
- identifier: Data hosting locations
- statement: New merchants in Europe automatically avail of this new infrastructure and now have their store data, order data and customer personal data stored at rest in Europe by default.
- scope: new merchants in Europe
- cite_ids: SH-S-0638
- note: first run's citation

**Citation SH-S-0638:** `https://help.shopify.com/en/manual/privacy-and-security/privacy/international-data-transfers/onward-transfers.md` | Data hosting locations | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/083-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:04Z, captured)
- quote: New merchants in Europe automatically avail of this new infrastructure and now have their store data, order data and customer personal data stored at rest in Europe by default.
- title: Onward transfers of personal data
- the page opens: In order to provide our services to you effectively, the personal data that you provide to the Shopify entity that you contract with is transferred to the following recipients: * certain other Shopify entities, and * carefully selected and trusted subprocessors This section provides information on how onward transfers are governed. Onward transfers of personal data from the European Economic Area (EEA) and the United Kingdom (UK) Shopify International Limited, an Irish-registered entity, is Shop…
- headings: Onward transfers of personal data > Data hosting locations
- in context: …that we can offer a reliable and scalable infrastructure that can handle unpredictable volumes across our entire merchant database. We need to be able to move data geographically in order to operate our services, and we have mechanisms in place to do so in accordance with applicable laws and regulations, including GDPR. Shopify now stores certain merchant and customer personal data in Europe (namely the EEA, UK and/or Switzerland), as follows: * ⟪New merchants in Europe automatically avail of this new infrastructure and now have their store data, order data and customer personal data stored at rest in Europe by default.⟫ * All existing Shopify features will continue to work. * Even where merchant customer personal data is stored in Europe, we will rely on international data transfers for processing that personal data. ## How Shopify chooses its Subprocessors In line with the GDPR and other applicable data protection laws, Shopify adopts a range of best practice measures when enlisting subprocessors: * We choose the companies we work with carefully. * We only use…

### Q1-SH-009

**Cited at:** section 5, line 124

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-009
- bears_on: 2
- identifier: Inheritance
- statement: Different customizations follow different inheritance rules. Some are overridden by the submarket's value, whereas others (like catalogs) are combined.
- cite_ids: Q1-SH-C009
- from: held

**Citation Q1-SH-C009:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/overview.md` | Inheritance | 2026-10-16 | kind: stated | quote check: found
- quote: Different customizations follow different inheritance rules. Some are overridden by the submarket's value, whereas others (like catalogs) are combined.
- title: Adding and removing market customizations
- the page opens: When you create a market, it inherits your store's default settings. You can override any of these defaults by adding customizations to the market. Each customization controls a specific aspect of the customer experience. You can customize only catalogs and currencies for channel markets. Customizations apply as soon as you save them. If you want to schedule a catalog's status change, then you can use a rollout to schedule when a catalog becomes active or returns to a draft. Market customization…
- headings: Adding and removing market customizations > Inheritance
- in context: …Plus only.</td> </tr> </tbody> </table> </div> ## Inheritance If a market doesn't have a specific customization, then it inherits the value from its parent market. If there's no parent market, then the store default is used. When you add a customization to a market, the setting moves from the **Inherited** section to the **Customized** section on the market detail page. You can remove a customization at any time to revert to the inherited value. ⟪Different customizations follow different inheritance rules. Some are overridden by the submarket's value, whereas others (like catalogs) are combined.⟫ Refer to each customization's page for details on how inheritance works. ## Add customizations Customizations are added per market. When you click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg" alt="Plus Circle Icon" class="admin-icon" /> next to a setting on a market's detail page, you override the inherited value with a market-specific customization. #### Steps: 1. From your Shopify admin, go …

### Q1-SH-K1614

**Cited at:** section 7, line 141

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-067
- placement: responsible
- structure: https://www.shopify.com/legal/terms-shopify-payments
- identifier: Part II, B. Canada, Regulated Payment Services
- statement: Shopify Payment Activities Inc. is registered with the Bank of Canada as a Payment Service Provider under the Retail Payment Activities Act.
- scope: Canada
- cite_ids: SH-S-0125
- note: first run's citation

**Citation SH-S-0125:** `https://www.shopify.com/legal/terms-shopify-payments` | Part II, B. Canada, Regulated Payment Services | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: Shopify Payment Activities Inc. is registered with the Bank of Canada as a Payment Service Provider under the Retail Payment Activities Act.
- title: Shopify Payments Terms of Service - Shopify
- in context: …yment Services. Where the Payments Services include payment activities that are regulated under the Retail Payment Activities Act (Canada) (collectively, "Regulated Payment Services"), solely with respect to the provision of such Regulated Payment Services to you, "Shopify", "we", "us", or "our" shall mean Shopify Payment Activities Inc., a Canadian corporation, with offices located at 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8. ⟪Shopify Payment Activities Inc. is registered with the Bank of Canada as a Payment Service Provider under the Retail Payment Activities Act.⟫ Shop Pay Installments. By using Shop Pay Installments, you accept and agree to be bound by the Shop Pay Installments Terms and the Merchant Agreement (Shop Pay Installments) with Affirm. You may disable Shop Pay Installments on the Shopify Admin. Managed Markets. By accepting this Agreement, you are also accepting and agreeing to be bound by the Service Terms - Shopify Managed Markets (the "Managed Markets Terms") with Global-e, the merchant of …

### Q1-SH-K1550

**Cited at:** section 7, line 142

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-063
- placement: boundary
- structure: https://www.shopify.com/legal/processor-list
- identifier: www.shopify.com/legal/processor-list
- statement: By accepting the Shopify Payments Terms of Service, you accept and agree to be bound by the Payment Processor Terms identified for your Designated Country.
- cite_ids: SH-S-0144
- note: first run's citation

**Citation SH-S-0144:** `https://www.shopify.com/legal/processor-list` | introduction | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/139-shopify.com/text.txt` (fetched 2026-10-11T06:13:10Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/116-shopify.com/text.txt` (fetched 2026-10-12T10:51:22Z, captured)
- quote: By accepting the Shopify Payments Terms of Service, you accept and agree to be bound by the Payment Processor Terms identified for your Designated Country.
- title: Payment Processors for Shopify Payments - Shopify
- in context: …Editions 150+ updates to Shopify, twice a year. LATEST UPDATES Agentic Storefronts Campaign Autopilot Shopify AI Toolkit for devs Pricing Enterprise Log in Start for free Payment Processors for Shopify Payments TABLE OF CONTENTS A. Global B. North America C. EMEA D. Asia-Pacific The following tables identify, for each Designated Country, (a) the Payment Processor(s), and (b) the agreements and documents that comprise the Payment Processor Terms. ⟪By accepting the Shopify Payments Terms of Service, you accept and agree to be bound by the Payment Processor Terms identified for your Designated Country.⟫ A. Global DESIGNATED COUNTRY PAYMENT PROCESSOR PAYMENT PROCESSOR TERMS All Shopify Payments regions The Bridge entity (an affiliate of Stripe) that applies based on your location. See here. Account Terms Bridge Terms B. North America DESIGNATED COUNTRY PAYMENT PROCESSOR PAYMENT PROCESSOR TERMS Canada Stripe Payments Canada, Ltd. Account Terms Stripe Connected Account Agreement Stripe Services Agreement Stripe Payment Method Terms Privacy Policy …

### Q1-SH-K1270

**Cited at:** section 7, line 143

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-006
- placement: decides
- structure: https://help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md
- identifier: restrictions that apply to all users
- statement: * Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account.
- cite_ids: SH-S-0304
- note: first run's citation

**Citation SH-S-0304:** `https://help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md` | restrictions that apply to all users | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/101-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:05Z, captured)
- quote: * Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account.
- title: Unsupported countries and regions
- the page opens: Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors. The following list contains the countries and regions that aren't supported by Shopify: * Cuba * Iran * North Korea * Syria * The Crimea region of Ukraine, and the so-called Donetsk and Luhansk People's Republics in Ukraine The following restrictions apply to all users of Shopify: * Individuals and businesses within unsupported countries a…
- headings: Unsupported countries and regions
- in context: … regions Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors. The following list contains the countries and regions that aren't supported by Shopify: * Cuba * Iran * North Korea * Syria * The Crimea region of Ukraine, and the so-called Donetsk and Luhansk People's Republics in Ukraine The following restrictions apply to all users of Shopify: ⟪* Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account.⟫ * Access to storefronts and accounts is prohibited within unsupported countries and regions. * Products originating from unsupported countries and regions are prohibited. * Orders shipping to unsupported countries and regions are prohibited.
