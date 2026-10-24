# Cards: Q1 on bigcommerce

18 records cited by `studies/proposals/drafts/Q1/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 10:** - BigCommerce runs several storefronts from one store, which "may work for some merchants as a multi-region or cross-border solution": a match with the market on role (basis 4). Q1-BC-004
- **section 1, line 12:** - What a market or storefront can set for itself, matching on role (basis 4): Shopify lists "currency, product availability, theme content, domains, languages, and taxes"; Salla's market page holds currencies, branches, shipping, domain, login options and design; a Zid market has a name, countries and "عملة السوق"; BigCommerce's storefronts set domains, themes, currencies and price lists. Q1-SH-K1931, Q1-SA-004, Q1-ZD-004, Q1-BC-005
- **section 1, line 13:** - Prices: Salla's are entered per market or follow "سعرها الأساسي وسعر الصرف للعملة"; Zid's are copied from the main market, converted at the current rate, or entered by hand; BigCommerce's price lists set "different prices in the same currency per different storefronts". Q1-SA-019, Q1-ZD-011, Q1-BC-034
- **section 1, line 14:** - Tax: on Salla "ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط"; BigCommerce and WooCommerce set rates by geography, in zones "based on country, state, or postal code" and, in WooCommerce's shipped code, by a rate's "2 digit country code". Q1-SA-023, Q1-BC-129, Q1-WC-024
- **section 1, line 15:** - Payment methods: Shopify shows local payment methods on a market's payments card when it "contains a country that is eligible"; Salla lets the merchant "تخصيص طرق الدفع حسب السوق الذي يختاره العميل"; BigCommerce sets them for each transactional currency. Q1-SH-051, Q1-SA-033, Q1-BC-053
- **section 1, line 17:** - What stays one for the whole store: on Shopify, "Staff permissions can't be assigned per market", while Salla can restrict a role "بحسب السوق المطلوب"; on BigCommerce, orders arrive in one area with "storefront attribution", and the store's address type and country are "inherently global" (not checked on Zid), as WooCommerce's store address, "the location where you are based as a seller", is one, a match on role (basis 4). Q1-SH-035, Q1-SA-028, Q1-BC-003, Q1-BC-018, Q1-WC-001
- **section 1, line 24:** - BigCommerce: "Each new channel will use the store's global default values unless the merchant chooses to override them", matching Shopify's inheritance on role (basis 4). Q1-BC-017
- **section 1, line 27:** - Lists of places, matching on role (basis 4): in WooCommerce's shipped code, country codes and names "should follow the Unicode CLDR recommendation"; BigCommerce's Geography API gives "countries, states, and provinces". Q1-WC-K1382, Q1-BC-K0405
- **section 1, line 31:** - Who contracts with the seller follows the seller's place in three platforms' terms, matching on role (basis 4): Shopify contracts "based on the billing address of your Store"; BigCommerce's table runs by the merchant's country of residence down to "Any other jurisdiction"; WooCommerce names "WooCommerce Ireland Ltd." for residents of its "Designated Countries". Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499
- **section 1, line 34:** - The platform's own payment product depends on where the seller is based, matching on role (basis 4), Shopify's in its payments terms and the others in help pages: Shopify Payments needs "a business located in your Designated Country"; Zid Pay is "متاح لتجار المملكة العربية السعودية و دولة الكويت"; WooPayments counts the country "where your business is registered — not the one in which you personally live"; BigCommerce Payments needs a store "located in the United Kingdom or the United States"; Salla pays UAE stores "كل يوم خميس" once their balance passes 250 dirhams. Q1-SH-K1536, Q1-ZD-K0005, Q1-WC-K0402, Q1-BC-P0068, Q1-SA-K1547
- **section 1, line 36:** - The first currency comes from the seller's location, matching on role (basis 4): BigCommerce assigns the default currency "based on your location", and Zid's العملة الأساسية is picked "بناء على عملة دولتك". Q1-BC-060, Q1-ZD-015
- **section 1, line 38:** - Fees by place, matching on role (basis 4), Shopify's in a help page and the others in their terms: Shopify's currency conversion fee "is either 1.5% or 2%, depending on your store's location"; BigCommerce's "Fees are payable in U.S. Dollars, unless otherwise specified"; Zid's are "بالريال السعودي أو بعملة التاجر المحلية". Q1-SH-057, Q1-BC-K0177, Q1-ZD-K0156
- **section 1, line 43:** - A seller adds a place to sell to, matching on role (basis 4): on Shopify, a market with a Regions condition; on Salla, "+ سوق جديد"; on Zid, a market published or kept "كسوق مخفي"; on BigCommerce, a merchant "creates a new channel to sell in a new context"; on WooCommerce, a country added to the shipped setting "Selling location(s)". Q1-SH-031, Q1-SA-005, Q1-ZD-012, Q1-BC-K0211, Q1-WC-K0536
- **section 1, line 48:** - Shopify's payments terms let it "add a new Designated Country"; BigCommerce says "Additional regions and countries will be launching soon"; WooCommerce ranks "new countries and currencies" partly by store owners' requests. What adding a country involves on the platform's side was not in what was read for Shopify or BigCommerce. Q1-SH-K1604, Q1-BC-P0030, Q1-WC-K0403, Q1-SH-N02, Q1-BC-N04
- **section 1, line 53:** - Adding a currency for buyers, matching on role (basis 4): on BigCommerce it takes "the Manage Settings permission"; on WooCommerce, "a multi-currency extension/plugin"; Shopify sets one per market, and with manual rates the conversion fee "is deducted from your payout". Q1-BC-061, Q1-WC-K0751, Q1-SH-058
- **section 1, line 54:** - Shown or charged, matching on role (basis 4): on BigCommerce, for a currency to be transactional "a payment gateway that supports the currency must be enabled", and each added transactional currency gets its own payment methods; on Shopify only Shopify Payments or Adyen "as the primary gateway can process payments in a customer's local currency"; Zid Pay charges in the store's العملة الأساسية, except through K-Net; WooCommerce's Currency Converter Widget "changes the display of prices only". Q1-BC-049, Q1-BC-053, Q1-SH-K1937, Q1-ZD-K0300, Q1-WC-018
- **section 1, line 55:** - Connecting a payment provider, matching on role (basis 4): on Shopify "Only the store owner can add a payment provider"; on Salla the seller copies credentials from their own gateway account (dashboard text, observed 8 October 2026), and for Tabby "Your settlement terms and merchant fees follow your agreement with Tabby"; on Zid the seller enters "مفاتيح الربط"; on BigCommerce, the seller applies to the provider and must "complete underwriting" first; on WooCommerce, gateways "can be added through traditional plugins". Q1-SH-064, Q1-SA-K1656, Q1-SA-089, Q1-ZD-K0094, Q1-BC-P0048, Q1-WC-K0006
- **section 2, line 61:** - **Place register**, proposed: Sharrwah's one list of places: every country and, under it, the areas a setting needs, such as a region, a governorate or a city, each with its parent and a code. Markets, delivery zones, tax rates, addresses and operating places name their places from it. Q1-WC-K1382, Q1-BC-K0405
- **section 2, line 62:** - It draws on WooCommerce's standard country list and BigCommerce's countries, states and provinces, with levels below country from Shopify's sub-region markets, Salla's markets for an "منطقة أو مدينة" and BigCommerce's tax zones. Why: places are data (rule 1) behind their own part (rule 2), with levels below country from the start, since adding them later changes every record naming a place (rule 3). Not taken: countries only, as in WooCommerce's selling locations, since Shopify and BigCommerce set delivery and tax below a country. Q1-WC-K1382, Q1-SH-022, Q1-SA-K1976, Q1-BC-129, Q1-WC-K0536
- **section 2, line 63:** - **Operating place**, proposed: a place, or a group of places, whose sellers Sharrwah serves, with their set-up: the contracting entity, terms and law; the currency of Sharrwah's fees and their tax; verification and documents; the payment providers offered, in order; the services offered; the default store currency and language; and where store data is kept. One set-up can serve every place not named. Q1-SH-K1243, Q1-BC-K0425
- **section 2, line 68:** - Not taken: the seller's country as a store setting alone, like Salla's store country, since BigCommerce's contract follows the merchant's country of residence and WooPayments the business's registration. Q1-SA-K1989, Q1-BC-K0425, Q1-WC-K0402
- **section 2, line 69:** - **Store currency**, proposed: the one currency a store prices and reports in, defaulting from the operating place; the seller changes it freely until the first order, then only through a change that leaves past orders as they were (rule 3). Q1-SH-K1935, Q1-BC-060
- **section 2, line 71:** - **Market**, proposed: a part of a store that sells to chosen places from the register, with its own values for some settings and the store's defaults for the rest: currencies, prices and products, languages and web address, theme content, payment methods and delivery options, and later tax display and a legal entity. Every store has a **home market** from creation; the seller adds others, each a draft, hidden or active; each order records its market. Q1-SH-K1931, Q1-BC-017, Q1-SH-008
- **section 2, line 72:** - It takes store defaults overridden per market from Shopify, whose markets graph view lists a "Business entity" under "Store defaults" in one store's saved step text (demo-fake-dev-store, 30 September 2026), and from BigCommerce; markets made with the store from Shopify and Zid; the hidden state from Zid; and orders that record their market from BigCommerce's storefront attribution. Why: a seller entering a new place adds a market, not a store (rule 1); and with a home market from the start, a second market changes no stored data (rule 3), where Salla's switch-on changes inventory deduction and is undone only through the account manager. Q1-SH-113, Q1-SH-027, Q1-ZD-003, Q1-ZD-012, Q1-BC-003, Q1-SA-107
- **section 2, line 75:** - **Market currency**, proposed: each of a market's currencies is **charged**, so the buyer pays in it, or **shown**, so prices display in it and the buyer pays in the store currency. A currency is charged only where a connected provider supports it, with its own payment methods. Prices are the seller's own or converted at a rate from the **rate source**, rounded as the seller sets, and each order records its rate. Q1-BC-049, Q1-BC-053, Q1-SH-K1937
- **section 2, line 77:** - **Payment provider**, proposed: a company that takes buyers' payments for a seller, in Sharrwah's **provider catalogue** with its places, currencies and methods. For each operating place Sharrwah sets which providers are offered, in order. The seller makes a **provider connection** with credentials from their own account, after the provider's onboarding, and turns **payment methods** on per market and per charged currency. Q1-SH-065, Q1-SA-K1656, Q1-BC-P0048
- **section 2, line 81:** - **Tax by place** and **delivery zone**, proposed and left to the build (rule 3): tax rates per place, as in BigCommerce's zones and WooCommerce's country codes; delivery zones as sets of places with methods, a market going live only where its places have one, since on Shopify no checkout runs without shipping rates, and one store's saved step text (capture-grow, 4 October 2026) says that to sell to a zone's countries, "include them in a market". Q1-BC-129, Q1-WC-024, Q1-SH-034, Q1-SH-108, Q1-SH-110
- **section 3, line 88:** - Set per operating place: all of its set-up (section 2), places sharing one and one serving every place not named. Q1-SH-K1243, Q1-BC-K0425
- **section 3, line 90:** - Set per store: the store currency and defaults, the plan, and the store's own country, which BigCommerce holds "inherently global" (not checked on Zid). Q1-SH-K1935, Q1-BC-018
- **section 3, line 93:** - Set per charged currency: its payment methods, rate and rounding. Q1-BC-053
- **section 3, line 97:** - Set by the seller's staff, by permission, as on Shopify and BigCommerce. Q1-SH-K0176, Q1-BC-061
- **section 3, line 98:** - Set by the provider: its places and currencies, its onboarding and its settlement terms. Q1-BC-P0048, Q1-SA-089
- **section 7, line 140:** - Where Sharrwah's company is based, and which entity contracts with sellers in each operating place, under which law and terms. Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499, Q1-SA-095
- **section 7, line 144:** - The currency of Sharrwah's own fees, and the tax charged on them, in each place. Q1-SA-096, Q1-BC-K0177, Q1-SH-116

## The cards

### Q1-BC-004

**Cited at:** section 1, line 10

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-004
- bears_on: 1;2
- identifier: Use Cases
- statement: Depending on your business model, multi-storefront may work for some merchants as a multi-region or cross-border solution. However, some store functions are global and are shared across storefronts, such as the built-in blog. Additionally, even though the same product can be assigned to different storefronts, product attributes (like description and name) cannot be overridden into a different language without customization. Stores on a Performance plan will have access to additional product localization fields.
- cite_ids: Q1-BC-C005;Q1-BC-C006
- from: held

**Citation Q1-BC-C005:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Use Cases | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Depending on your business model, multi-storefront may work for some merchants as a multi-region or cross-border solution. However, some store functions are global and are shared across storefronts, such as the built-in blog.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …t.js, Gatsby.js, Nuxt.js, Contentful, Prismic, Contentstack, Uniform, Amplience, Shogun Frontend, and Bloomreach. Use Cases Multi-storefront can be useful for merchants who have multiple brands or who serve multiple segments like B2C, B2B, retail, and wholesale segments. You can also use additional storefronts as a marketing tool. For example, you can create a new storefront as a "microsite" that focuses on a specific product or campaign launch. ⟪Depending on your business model, multi-storefront may work for some merchants as a multi-region or cross-border solution. However, some store functions are global and are shared across storefronts, such as the built-in blog.⟫ Additionally, even though the same product can be assigned to different storefronts, product attributes (like description and name) cannot be overridden into a different language without customization. Stores on a Performance plan will have access to additional product localization fields. Features With multiple native storefronts, you can do all of this within the control panel: Create and manage multiple BigCommerce storefronts within a single…

**Citation Q1-BC-C006:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Use Cases | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Additionally, even though the same product can be assigned to different storefronts, product attributes (like description and name) cannot be overridden into a different language without customization. Stores on a Performance plan will have access to additional product localization fields.
- title, opening and note boxes: as for this source's citation above
- in context: …ike B2C, B2B, retail, and wholesale segments. You can also use additional storefronts as a marketing tool. For example, you can create a new storefront as a "microsite" that focuses on a specific product or campaign launch. Depending on your business model, multi-storefront may work for some merchants as a multi-region or cross-border solution. However, some store functions are global and are shared across storefronts, such as the built-in blog. ⟪Additionally, even though the same product can be assigned to different storefronts, product attributes (like description and name) cannot be overridden into a different language without customization. Stores on a Performance plan will have access to additional product localization fields.⟫ Features With multiple native storefronts, you can do all of this within the control panel: Create and manage multiple BigCommerce storefronts within a single control panel. Configure storefront settings and internal notifications for each storefront. Connect different domain names and SSL certificates for each storefront. Apply and customize themes, page templates, email templates, widgets, web pages, scripts, and social media links for each st…

### Q1-BC-005

**Cited at:** section 1, line 12

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-005
- bears_on: 1;2
- identifier: Features
- statement: With multiple native storefronts, you can do all of this within the control panel: Create and manage multiple BigCommerce storefronts within a single control panel. Configure storefront settings and internal notifications for each storefront. Connect different domain names and SSL certificates for each storefront. Apply and customize themes, page templates, email templates, widgets, web pages, scripts, and social media links for each storefront. Set and manage default storefront currency and unique sets of currencies per storefront. Configure unique checkout settings per storefront. Set up web analytics (like Google Analytics) specific to each storefront. Set up a Meta Pixel specific to each storefront. Create storefront-unique categories and make products available on one or multiple storefronts. Stores on a Performance plan will have access to additional product localization fields. Configure inventory settings for each storefront, including notifications. Control product filtering settings per storefront and per category. Configure category and web page URL structure per storefront. Use Price Lists for custom pricing on each storefront. View and manage orders and customers for multiple storefronts in one place. Control product purchasability per storefront. Create Automatic and Coupon Promotions per storefront (using the Standard Promotions editor). Manage customer groups (like retail or wholesale) for each storefront and set the default group. Create category-level discounts per storefront for specific customer groups. Create customers and manage login access to each storefront. Control storefront status for all storefronts from Channel Manager. Filter ecommerce sales reports by native storefront channel. Collect and export newsletter subscriptions per storefront. Create and manage 301 redirects per storefront. Manage shipping methods and out of delivery zone messaging per storefront.
- scope: multiple native storefronts
- cite_ids: Q1-BC-C007;Q1-BC-C008;Q1-BC-C009;Q1-BC-C010;Q1-BC-C011;Q1-BC-C012;Q1-BC-C013;Q1-BC-C014
- from: held

**Citation Q1-BC-C007:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: With multiple native storefronts, you can do all of this within the control panel: Create and manage multiple BigCommerce storefronts within a single control panel. Configure storefront settings and internal notifications for each storefront.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …refronts, such as the built-in blog. Additionally, even though the same product can be assigned to different storefronts, product attributes (like description and name) cannot be overridden into a different language without customization. Stores on a Performance plan will have access to additional product localization fields. Features ⟪With multiple native storefronts, you can do all of this within the control panel: Create and manage multiple BigCommerce storefronts within a single control panel. Configure storefront settings and internal notifications for each storefront.⟫ Connect different domain names and SSL certificates for each storefront. Apply and customize themes, page templates, email templates, widgets, web pages, scripts, and social media links for each storefront. Set and manage default storefront currency and unique sets of currencies per storefront. Configure unique checkout settings per s…

**Citation Q1-BC-C008:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Connect different domain names and SSL certificates for each storefront. Apply and customize themes, page templates, email templates, widgets, web pages, scripts, and social media links for each storefront. Set and manage default storefront currency and unique sets of currencies per storefront.
- title, opening and note boxes: as for this source's citation above
- in context: …es on a Performance plan will have access to additional product localization fields. Features With multiple native storefronts, you can do all of this within the control panel: Create and manage multiple BigCommerce storefronts within a single control panel. Configure storefront settings and internal notifications for each storefront. ⟪Connect different domain names and SSL certificates for each storefront. Apply and customize themes, page templates, email templates, widgets, web pages, scripts, and social media links for each storefront. Set and manage default storefront currency and unique sets of currencies per storefront.⟫ Configure unique checkout settings per storefront. Set up web analytics (like Google Analytics) specific to each storefront. Set up a Meta Pixel specific to each storefront. Create storefront-unique categories and make products available on one or multiple storefronts. Stores on a Performance plan will have access to additional produc…

**Citation Q1-BC-C009:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Configure unique checkout settings per storefront. Set up web analytics (like Google Analytics) specific to each storefront. Set up a Meta Pixel specific to each storefront. Create storefront-unique categories and make products available on one or multiple storefronts.
- title, opening and note boxes: as for this source's citation above
- in context: …ernal notifications for each storefront. Connect different domain names and SSL certificates for each storefront. Apply and customize themes, page templates, email templates, widgets, web pages, scripts, and social media links for each storefront. Set and manage default storefront currency and unique sets of currencies per storefront. ⟪Configure unique checkout settings per storefront. Set up web analytics (like Google Analytics) specific to each storefront. Set up a Meta Pixel specific to each storefront. Create storefront-unique categories and make products available on one or multiple storefronts.⟫ Stores on a Performance plan will have access to additional product localization fields. Configure inventory settings for each storefront, including notifications. Control product filtering settings per storefront and per category. Configure category and web page URL structure per storefront. Use Price Lists for custom pricing on each…

**Citation Q1-BC-C010:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Stores on a Performance plan will have access to additional product localization fields. Configure inventory settings for each storefront, including notifications. Control product filtering settings per storefront and per category. Configure category and web page URL structure per storefront.
- title, opening and note boxes: as for this source's citation above
- in context: … storefront currency and unique sets of currencies per storefront. Configure unique checkout settings per storefront. Set up web analytics (like Google Analytics) specific to each storefront. Set up a Meta Pixel specific to each storefront. Create storefront-unique categories and make products available on one or multiple storefronts. ⟪Stores on a Performance plan will have access to additional product localization fields. Configure inventory settings for each storefront, including notifications. Control product filtering settings per storefront and per category. Configure category and web page URL structure per storefront.⟫ Use Price Lists for custom pricing on each storefront. View and manage orders and customers for multiple storefronts in one place. Control product purchasability per storefront. Create Automatic and Coupon Promotions per storefront (using the Standard Promotions editor). Manage customer groups (like retail or wholesale) for each store…

**Citation Q1-BC-C011:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Use Price Lists for custom pricing on each storefront. View and manage orders and customers for multiple storefronts in one place. Control product purchasability per storefront. Create Automatic and Coupon Promotions per storefront (using the Standard Promotions editor).
- title, opening and note boxes: as for this source's citation above
- in context: … available on one or multiple storefronts. Stores on a Performance plan will have access to additional product localization fields. Configure inventory settings for each storefront, including notifications. Control product filtering settings per storefront and per category. Configure category and web page URL structure per storefront. ⟪Use Price Lists for custom pricing on each storefront. View and manage orders and customers for multiple storefronts in one place. Control product purchasability per storefront. Create Automatic and Coupon Promotions per storefront (using the Standard Promotions editor).⟫ Manage customer groups (like retail or wholesale) for each storefront and set the default group. Create category-level discounts per storefront for specific customer groups. Create customers and manage login access to each storefront. Control storefront status for all storefronts from Channel Manager. Filter ecommerce sales reports by…

**Citation Q1-BC-C012:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Manage customer groups (like retail or wholesale) for each storefront and set the default group. Create category-level discounts per storefront for specific customer groups. Create customers and manage login access to each storefront.
- title, opening and note boxes: as for this source's citation above
- in context: …y. Configure category and web page URL structure per storefront. Use Price Lists for custom pricing on each storefront. View and manage orders and customers for multiple storefronts in one place. Control product purchasability per storefront. Create Automatic and Coupon Promotions per storefront (using the Standard Promotions editor). ⟪Manage customer groups (like retail or wholesale) for each storefront and set the default group. Create category-level discounts per storefront for specific customer groups. Create customers and manage login access to each storefront.⟫ Control storefront status for all storefronts from Channel Manager. Filter ecommerce sales reports by native storefront channel. Collect and export newsletter subscriptions per storefront. Create and manage 301 redirects per storefront. Manage shipping methods and out of delivery zone messaging per storefront. With multiple headless s…

**Citation Q1-BC-C013:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Control storefront status for all storefronts from Channel Manager. Filter ecommerce sales reports by native storefront channel. Collect and export newsletter subscriptions per storefront. Create and manage 301 redirects per storefront.
- title, opening and note boxes: as for this source's citation above
- in context: …efront. Create Automatic and Coupon Promotions per storefront (using the Standard Promotions editor). Manage customer groups (like retail or wholesale) for each storefront and set the default group. Create category-level discounts per storefront for specific customer groups. Create customers and manage login access to each storefront. ⟪Control storefront status for all storefronts from Channel Manager. Filter ecommerce sales reports by native storefront channel. Collect and export newsletter subscriptions per storefront. Create and manage 301 redirects per storefront.⟫ Manage shipping methods and out of delivery zone messaging per storefront. With multiple headless storefronts, you can do all of this within the control panel: Create and manage multiple headless storefronts within a single control panel. Configure storefront settings for each storefront. Connect different domain names and SSL certifi…

**Citation Q1-BC-C014:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Features | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Manage shipping methods and out of delivery zone messaging per storefront.
- title, opening and note boxes: as for this source's citation above
- in context: …orefront for specific customer groups. Create customers and manage login access to each storefront. Control storefront status for all storefronts from Channel Manager. Filter ecommerce sales reports by native storefront channel. Collect and export newsletter subscriptions per storefront. Create and manage 301 redirects per storefront. ⟪Manage shipping methods and out of delivery zone messaging per storefront.⟫ With multiple headless storefronts, you can do all of this within the control panel: Create and manage multiple headless storefronts within a single control panel. Configure storefront settings for each storefront. Connect different domain names and SSL certificates for each storefront (this is managed outside of BigCommerce for headl…

### Q1-BC-034

**Cited at:** section 1, line 13

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-034
- bears_on: 2
- identifier: Pricing: price lists
- statement: You can set different prices per storefront by using price lists. By creating a channel-specific price list, you can set different prices in the same currency per different storefronts. For example, by having separate price lists for Spain and for France, merchants can set different prices in EUR for Spain and for France by assigning each price list to its related storefront. Price lists can also be assigned to a customer group or a combination of a storefront and customer group.
- cite_ids: Q1-BC-C059;Q1-BC-C060
- from: held

**Citation Q1-BC-C059:** `https://support.bigcommerce.com/s/article/Getting-Started-with-Localization-on-Multi-Storefronts` | Localizing Products: Pricing | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/029-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:30Z, captured)
- quote: You can set different prices per storefront by using price lists. By creating a channel-specific price list, you can set different prices in the same currency per different storefronts.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …front. See Adding Products (v3) for more information on product fields, and our Guide to v3 Products for an overview on configuring your catalog. PRODUCT FILTERING You can localize the display names of product filters and filter settings on each storefront. Filtering values will be automatically translated, based on the selected default language on the specific storefront. See Product Filtering for more information on using this feature. PRICING ⟪You can set different prices per storefront by using price lists. By creating a channel-specific price list, you can set different prices in the same currency per different storefronts.⟫ For example, by having separate price lists for Spain and for France, merchants can set different prices in EUR for Spain and for France by assigning each price list to its related storefront. Price lists can also be assigned to a customer group or a combination of a storefront and customer group. See Using Price Lists for more information on how this feature works. Localizing Promotions and Store Communications Promotions can vary by cultural, …

**Citation Q1-BC-C060:** `https://support.bigcommerce.com/s/article/Getting-Started-with-Localization-on-Multi-Storefronts` | Localizing Products: Pricing | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/029-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:30Z, captured)
- quote: For example, by having separate price lists for Spain and for France, merchants can set different prices in EUR for Spain and for France by assigning each price list to its related storefront. Price lists can also be assigned to a customer group or a combination of a storefront and customer group.
- title, opening and note boxes: as for this source's citation above
- in context: …isplay names of product filters and filter settings on each storefront. Filtering values will be automatically translated, based on the selected default language on the specific storefront. See Product Filtering for more information on using this feature. PRICING You can set different prices per storefront by using price lists. By creating a channel-specific price list, you can set different prices in the same currency per different storefronts. ⟪For example, by having separate price lists for Spain and for France, merchants can set different prices in EUR for Spain and for France by assigning each price list to its related storefront. Price lists can also be assigned to a customer group or a combination of a storefront and customer group.⟫ See Using Price Lists for more information on how this feature works. Localizing Promotions and Store Communications Promotions can vary by cultural, seasonal, regulatory, legal and brand strategy differences. For example, coupons can be embarrassing in some Southeast Asian countries. This is why having the ability to tailor transactional email and abandoned cart templates, set availability for promotions on storefronts, and providing translated…

### Q1-BC-129

**Cited at:** section 1, line 14; section 2, line 62; section 2, line 81

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-129
- bears_on: 2
- identifier: Zone type
- statement: Zone type — how the zone is defined. Zones can be based on country, state, or postal code.
- cite_ids: Q1-BC-C167
- from: held

**Citation Q1-BC-C167:** `https://support.bigcommerce.com/s/article/Manual-Tax-Setup` | Tax Zones | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/034-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:38Z, captured)
- quote: Zone type — how the zone is defined. Zones can be based on country, state, or postal code.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …ax zones. A tax zone specifies the geographical area where a group of tax rates apply. Set whether the tax zone geographical area applies to a customer's billing address, shipping or pickup address, or your store's shipping origin address in your tax settings. To view your tax zones, go to Settings › Tax, click Edit next to Basic Tax, then click on the Tax Rates and zones tab. You will see any current tax zones and an overview of their settings: ⟪Zone type - how the zone is defined. Zones can be based on country, state, or postal code.⟫ Price display - whether the zone's price display setting is tax inclusive or tax exclusive Status - whether the zone is currently active on the store or not DEFAULT ZONE All stores contain a Default Zone, which applies a 0% tax rate to any regions not set up in another zone. Do not set up tax rates in this zone. Unless you have nexus everywhere in the world, you will want to keep this as an "everywhere I don't need to charge taxes in" zone. ADDI…

### Q1-BC-053

**Cited at:** section 1, line 15; section 1, line 54; section 2, line 75; section 3, line 93

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-053
- bears_on: 5
- identifier: Setting up Payment Methods for Additional Transactional Currencies
- statement: The store’s default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency. Display currencies transact in your store's default currency. As such, they use the payment methods configured for the store’s default currency.
- cite_ids: Q1-BC-C085;Q1-BC-C086
- from: held

**Citation Q1-BC-C085:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | Setting up Payment Methods for Additional Transactional Currencies | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:41:00Z, captured)
- quote: The store’s default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency. Display currencies transact in your store's default currency.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …your store has USD as its default currency and offers GBP as a transactional currency, a €30 keychain with a modifier for engraving (add $5) will have its price calculated as: €30 + [$5 x (the autoconversion rate)] ANALYTICS Store analytics are displayed in the store's default currency, using the configured exchange rate. Since there is a conversion, these are approximate values. Setting up Payment Methods for Additional Transactional Currencies ⟪The store's default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency. Display currencies transact in your store's default currency.⟫ As such, they use the payment methods configured for the store's default currency. See Available Payment Gateways for a table of payment gateways that support additional transactional currencies. All offline payment methods support additional transactional currencies. If there are no payment methods currently set up for a transactional currency, you'll see a Set up button in the Payment provider column, under Additional Currencies in your store'…

**Citation Q1-BC-C086:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | Setting up Payment Methods for Additional Transactional Currencies | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:41:00Z, captured)
- quote: As such, they use the payment methods configured for the store’s default currency.
- title, opening and note boxes: as for this source's citation above
- in context: … the configured exchange rate. Since there is a conversion, these are approximate values. Setting up Payment Methods for Additional Transactional Currencies The store's default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency. Display currencies transact in your store's default currency. ⟪As such, they use the payment methods configured for the store's default currency.⟫ See Available Payment Gateways for a table of payment gateways that support additional transactional currencies. All offline payment methods support additional transactional currencies. If there are no payment methods currently set up for a transactional currency, you'll see a Set up button in the Payment provider column, under Additional Currencies in your store's Currencies settings. If your store has additional storefronts, you will be able t…

### Q1-BC-003

**Cited at:** section 1, line 17; section 2, line 72

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-003
- bears_on: 1
- identifier: Orders
- statement: Orders from all channels come into your BigCommerce orders area. Orders include storefront attribution and can be sorted per storefront.
- cite_ids: Q1-BC-C004
- from: held

**Citation Q1-BC-C004:** `https://support.bigcommerce.com/s/article/Multi-Storefront` | Introduction to Multi-Storefront | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/035-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:39Z, captured)
- quote: Orders from all channels come into your BigCommerce orders area. Orders include storefront attribution and can be sorted per storefront.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …Multi-Storefront (MSF) allows you to use a single BigCommerce "store" to power multiple "storefronts". Each of these storefronts can have its own unique domain, theme, categories, web pages, social media links, price lists, email templates, and more. The settings and data for each of these storefronts are managed from one BigCommerce control panel. Storefronts share your store's catalog. You can choose which products appear on which storefronts. ⟪Orders from all channels come into your BigCommerce orders area. Orders include storefront attribution and can be sorted per storefront.⟫ Storefronts can use BigCommerce's customizable, native theme platform (Stencil), or use a third-party, headless solution like Next.js, Gatsby.js, Nuxt.js, Contentful, Prismic, Contentstack, Uniform, Amplience, Shogun Frontend, and Bloomreach. Use Cases Multi-storefront can be useful for merchants who have multiple brands or who serve multiple segments like B2C, B2B, retail, and wholesale segments. You can also use additional storefronts as a mar…

### Q1-BC-018

**Cited at:** section 1, line 17; section 3, line 90

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-018
- bears_on: 1
- identifier: Global-only settings
- statement: Currently, the following settings are inherently global and cannot be modified with channel-specific overrides: > > * store\_address\_type > * store\_country
- cite_ids: Q1-BC-C034;Q1-BC-C035;Q1-BC-C036
- from: held

**Citation Q1-BC-C034:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/settings/store-configuration.md` | Editing store configuration settings: Global-only settings | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/075-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:30Z, captured)
- quote: Currently, the following settings are inherently global and cannot be modified with channel-specific overrides:
- title: Store Configuration
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. Settings API reference documentation BigCommerce's Settings APIs can manage many of the configuration settings that are exposed to merchants in their store control panel, such as the store's name and …
- headings: Store Configuration > Editing store configuration settings
- in context: …55-555-555", "store_name": "My Channel-Specific Name For Channel 124", "store_address": "124 Channel St" }, "meta": {} } ``` Because channel-specific values exist for all store profile object properties, this channel is configured to override all the global default store profile configuration settings. Changes to the global defaults will not affect this channel. ## Editing store configuration settings > **Note** > > #### Global-only settings > > ⟪Currently, the following settings are inherently global and cannot be modified with channel-specific overrides:⟫ > > * store\_address\_type > * store\_country You can modify global and channel-specific settings alike by sending `PUT` requests to the relevant endpoints. The following example uses the [Update store profile settings](/developer/api-reference/rest/admin/management/settings/store-profile/update-settings-store-profile) endpoint to modify a store's global default configuration: **`Example request: Update global store profile settings`** ```http t…

**Citation Q1-BC-C035:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/settings/store-configuration.md` | Editing store configuration settings: Global-only settings | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/075-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:30Z, captured)
- quote: * store\_address\_type
- title, opening and note boxes: as for this source's citation above
- headings: Store Configuration > Editing store configuration settings
- in context: …{} } ``` Because channel-specific values exist for all store profile object properties, this channel is configured to override all the global default store profile configuration settings. Changes to the global defaults will not affect this channel. ## Editing store configuration settings > **Note** > > #### Global-only settings > > Currently, the following settings are inherently global and cannot be modified with channel-specific overrides: > > ⟪* store\_address\_type⟫ > * store\_country You can modify global and channel-specific settings alike by sending `PUT` requests to the relevant endpoints. The following example uses the [Update store profile settings](/developer/api-reference/rest/admin/management/settings/store-profile/update-settings-store-profile) endpoint to modify a store's global default configuration: **`Example request: Update global store profile settings`** ```http title="Example request: Upda…

**Citation Q1-BC-C036:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/settings/store-configuration.md` | Editing store configuration settings: Global-only settings | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/075-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:30Z, captured)
- quote: * store\_country
- title, opening and note boxes: as for this source's citation above
- headings: Store Configuration > Editing store configuration settings
- in context: …specific values exist for all store profile object properties, this channel is configured to override all the global default store profile configuration settings. Changes to the global defaults will not affect this channel. ## Editing store configuration settings > **Note** > > #### Global-only settings > > Currently, the following settings are inherently global and cannot be modified with channel-specific overrides: > > * store\_address\_type > ⟪* store\_country⟫ You can modify global and channel-specific settings alike by sending `PUT` requests to the relevant endpoints. The following example uses the [Update store profile settings](/developer/api-reference/rest/admin/management/settings/store-profile/update-settings-store-profile) endpoint to modify a store's global default configuration: **`Example request: Update global store profile settings`** ```http title="Example request: Update global store pro…

### Q1-BC-017

**Cited at:** section 1, line 24; section 2, line 71

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-017
- bears_on: 1;2
- identifier: channel-specific
- statement: Once a merchant starts to take advantage of multi-storefront or other multi-channel functionality, they often want to configure settings differently for each sales channel. Each new channel will use the store's global default values unless the merchant chooses to override them by defining **channel-specific** settings.
- cite_ids: Q1-BC-C032;Q1-BC-C033
- from: held

**Citation Q1-BC-C032:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/settings/store-configuration.md` | Global settings and channel-specific settings | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/075-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:30Z, captured)
- quote: Once a merchant starts to take advantage of multi-storefront or other multi-channel functionality, they often want to configure settings differently for each sales channel.
- title: Store Configuration
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. Settings API reference documentation BigCommerce's Settings APIs can manage many of the configuration settings that are exposed to merchants in their store control panel, such as the store's name and …
- headings: Store Configuration > Global settings and channel-specific settings
- in context: …# Global settings and channel-specific settings ![settings-diagram.webp](https://storage.cloud.google.com/bigcommerce-production-dev-center/images/msf-beta-guide/settings-diagram.webp) The majority of BigCommerce merchants sell their products exclusively through the storefront website that comes preconfigured with their plan. When these merchants configure their store settings, they're modifying the **global default** versions of their settings. ⟪Once a merchant starts to take advantage of multi-storefront or other multi-channel functionality, they often want to configure settings differently for each sales channel.⟫ Each new channel will use the store's global default values unless the merchant chooses to override them by defining **channel-specific** settings. The Settings APIs use query parameters to distinguish which set of settings a request is accessing. Consider the following request to the [Get store profile settings](/developer/api-reference/rest/admin/management/settings/store-profile/get-settings-store-profile) endpoint: #### Request **`Example re…

**Citation Q1-BC-C033:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/settings/store-configuration.md` | Global settings and channel-specific settings | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/075-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:30Z, captured)
- quote: Each new channel will use the store's global default values unless the merchant chooses to override them by defining **channel-specific** settings.
- title, opening and note boxes: as for this source's citation above
- headings: Store Configuration > Global settings and channel-specific settings
- in context: …agram.webp) The majority of BigCommerce merchants sell their products exclusively through the storefront website that comes preconfigured with their plan. When these merchants configure their store settings, they're modifying the **global default** versions of their settings. Once a merchant starts to take advantage of multi-storefront or other multi-channel functionality, they often want to configure settings differently for each sales channel. ⟪Each new channel will use the store's global default values unless the merchant chooses to override them by defining **channel-specific** settings.⟫ The Settings APIs use query parameters to distinguish which set of settings a request is accessing. Consider the following request to the [Get store profile settings](/developer/api-reference/rest/admin/management/settings/store-profile/get-settings-store-profile) endpoint: #### Request **`Example request: Get store profile settings`** ```http title="Example request: Get store profile settings" showLineNumbers={false} GET https://api.bigcommerce…

### Q1-BC-K0405

**Cited at:** section 1, line 27; section 2, line 61

**Record** (`studies/proposals/records/Q1/bigcommerce/copied.tsv`):
- concern_id: BC-C-075
- placement: where
- structure: API reference group: /developer/api-reference/rest/admin/management/geography
- identifier: /developer/api-reference/rest/admin/management/geography
- statement: Get countries, states, and provinces. Use these endpoints to retrieve geographic data for use in shipping, tax, and address validation workflows.
- cite_ids: BC-S-0412

**Citation BC-S-0412:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/geography.md` | page introduction | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/027-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:19:42Z, captured)
- quote: Get countries, states, and provinces. Use these endpoints to retrieve geographic data for use in shipping, tax, and address validation workflows.
- title: Geography
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. Get countries, states, and provinces. Use these endpoints to retrieve geographic data for use in shipping, tax, and address validation workflows.…
- headings: Geography
- in context: > This page is for Developer. > For clean Markdown of any page, append .md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. # Geography ⟪Get countries, states, and provinces. Use these endpoints to retrieve geographic data for use in shipping, tax, and address validation workflows.⟫

### Q1-BC-K0425

**Cited at:** section 1, line 31; section 2, line 63; section 2, line 68; section 3, line 88; section 7, line 140

**Record** (`studies/proposals/records/Q1/bigcommerce/copied.tsv`):
- concern_id: BC-C-079
- placement: responsible
- structure: Master Services Agreement
- identifier: Any other jurisdiction
- statement: Any other jurisdiction Commerce.com Pty. Ltd., an Australia proprietary limited company New York Ecommerce Platform, Extensions, and certain Professional Services
- scope: Country of Residence of Merchant: Any other jurisdiction
- cite_ids: BC-S-0432

**Citation BC-S-0432:** `https://www.commerce.com/terms/` | Contracting Entity table | 2026-06-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` (fetched 2026-10-12T04:20:53Z, captured)
- quote: Any other jurisdiction Commerce.com Pty. Ltd., an Australia proprietary limited company New York Ecommerce Platform, Extensions, and certain Professional Services
- title: Master Services Agreement | Commerce
- in context: … Software UK Ltd., a United Kingdom limited company England and Wales Ecommerce Platform, Extensions, and certain Professional Services European Union Commerce Software Ireland Ltd., an Irish limited company Ireland Ecommerce Platform, Extensions, and certain Professional Services Australia Commerce.com Pty. Ltd., an Australia proprietary limited company New South Wales, Australia Ecommerce Platform, Extensions, and certain Professional Services ⟪Any other jurisdiction Commerce.com Pty. Ltd., an Australia proprietary limited company New York Ecommerce Platform, Extensions, and certain Professional Services⟫ If purchasing and/or contracting solely with Feedonomics Worldwide Feedonomics Holdings, LLC, a Delaware corporation in the United States New York Feedonomics Platform Worldwide Makeswift, Inc. a Delaware Corporation in the United States New York Makeswift visual editor / builder Eligibility. Minimum Age. The Services are available only to persons who are the age of majority and can form legally binding contracts under applicable law. Without li…

### Q1-BC-P0068

**Cited at:** section 1, line 34

**Record** (`studies/proposals/records/Q1/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-067
- bullet: e
- placement: decides
- identifier: Connecting with BigCommerce Payments: Requirements
- statement: Your store must be on a Core, Growth, or Scale plan. Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability. Your store’s checkout type must be Optimized One-Page Checkout or Custom Checkout. Your store must be located in the United Kingdom or the United States. Your new or existing PayPal Business account must be UK or US-based.
- scope: stores on a Core, Growth, or Scale plan (select Performance plan stores), located in the United Kingdom or the United States, with a UK or US-based PayPal Business account
- conditions: S01-BC-066;S01-BC-068;S01-BC-069;S01-BC-070;S01-BC-071;S01-BC-072;S01-BC-073;S01-BC-074;S01-BC-075;S01-BC-076;S01-BC-078;S01-BC-079;S01-BC-081;S01-BC-082;S01-BC-083;S01-BC-084;S01-BC-087
- cite_ids: S01-BC-C087;S01-BC-C088;S01-BC-C089;S01-BC-C090;S01-BC-C091
- from: new

**Citation S01-BC-C087:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 74: Requirements | 2026-10-13 | kind: stated | quote check: found
- quote: Your store must be on a Core, Growth, or Scale plan.
- in context: …. Shoppers benefit from a unified checkout experience, and funds are conveniently managed within a dedicated Balance dashboard directly inside BigCommerce. BigCommerce Payments Features BigCommerce Payments allows you to: manage your funds balances. keep track of your accounts from a single login. offer many popular payment methods. use additional tools to help you grow your business. sell securely with a brand your customers trust. Requirements ⟪Your store must be on a Core, Growth, or Scale plan.⟫ Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability. Your store's checkout type must be Optimized One-Page Checkout or Custom Checkout. Your store must be located in the United Kingdom or the United States. Your new or existing PayPal Business account must be UK or US-based. To set up and manage payment methods, the Manage Payments and Manage Settings permissions must b…

**Citation S01-BC-C088:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 75: Requirements | 2026-10-13 | kind: stated | quote check: found
- quote: Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability.
- in context: …, and funds are conveniently managed within a dedicated Balance dashboard directly inside BigCommerce. BigCommerce Payments Features BigCommerce Payments allows you to: manage your funds balances. keep track of your accounts from a single login. offer many popular payment methods. use additional tools to help you grow your business. sell securely with a brand your customers trust. Requirements Your store must be on a Core, Growth, or Scale plan. ⟪Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability.⟫ Your store's checkout type must be Optimized One-Page Checkout or Custom Checkout. Your store must be located in the United Kingdom or the United States. Your new or existing PayPal Business account must be UK or US-based. To set up and manage payment methods, the Manage Payments and Manage Settings permissions must be enabled on your user account. Setting up BigCommerce Payments To connect BigCommerce Payments with your store, go to Settings › …

**Citation S01-BC-C089:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 76: Requirements | 2026-10-13 | kind: stated | quote check: found
- quote: Your store’s checkout type must be Optimized One-Page Checkout or Custom Checkout.
- in context: …es BigCommerce Payments allows you to: manage your funds balances. keep track of your accounts from a single login. offer many popular payment methods. use additional tools to help you grow your business. sell securely with a brand your customers trust. Requirements Your store must be on a Core, Growth, or Scale plan. Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability. ⟪Your store's checkout type must be Optimized One-Page Checkout or Custom Checkout.⟫ Your store must be located in the United Kingdom or the United States. Your new or existing PayPal Business account must be UK or US-based. To set up and manage payment methods, the Manage Payments and Manage Settings permissions must be enabled on your user account. Setting up BigCommerce Payments To connect BigCommerce Payments with your store, go to Settings › Payments, and select a supported currency from the drop-down list. Under the Embedd…

**Citation S01-BC-C090:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 77: Requirements | 2026-10-13 | kind: stated | quote check: found
- quote: Your store must be located in the United Kingdom or the United States.
- in context: …ur accounts from a single login. offer many popular payment methods. use additional tools to help you grow your business. sell securely with a brand your customers trust. Requirements Your store must be on a Core, Growth, or Scale plan. Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability. Your store's checkout type must be Optimized One-Page Checkout or Custom Checkout. ⟪Your store must be located in the United Kingdom or the United States.⟫ Your new or existing PayPal Business account must be UK or US-based. To set up and manage payment methods, the Manage Payments and Manage Settings permissions must be enabled on your user account. Setting up BigCommerce Payments To connect BigCommerce Payments with your store, go to Settings › Payments, and select a supported currency from the drop-down list. Under the Embedded tab, expand Online Payment Methods and click Set up next to BigComme…

**Citation S01-BC-C091:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 78: Requirements | 2026-10-13 | kind: stated | quote check: found
- quote: Your new or existing PayPal Business account must be UK or US-based.
- in context: …e additional tools to help you grow your business. sell securely with a brand your customers trust. Requirements Your store must be on a Core, Growth, or Scale plan. Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability. Your store's checkout type must be Optimized One-Page Checkout or Custom Checkout. Your store must be located in the United Kingdom or the United States. ⟪Your new or existing PayPal Business account must be UK or US-based.⟫ To set up and manage payment methods, the Manage Payments and Manage Settings permissions must be enabled on your user account. Setting up BigCommerce Payments To connect BigCommerce Payments with your store, go to Settings › Payments, and select a supported currency from the drop-down list. Under the Embedded tab, expand Online Payment Methods and click Set up next to BigCommerce Payments. On the next page, click Set up to begin the onboarding …

### Q1-BC-060

**Cited at:** section 1, line 36; section 2, line 69

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-060
- bears_on: 3;5
- identifier: Setup
- statement: When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live.
- cite_ids: Q1-BC-C093
- from: held

**Citation Q1-BC-C093:** `https://support.bigcommerce.com/s/article/Managing-Currencies` | Adding a Currency: Setup | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/033-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:36Z, captured)
- quote: When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …n order to manage the currency settings in your store, you must have the Manage Settings permission enabled on your user account. This is enabled by default for users with the Store Administrator or Store Owner role. To learn more about the requirements for offering multiple transactional currencies in your store, see Using Multiple Currencies. Adding a Currency Setup Currency display configurations Transactions Additional display settings SETUP ⟪When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live.⟫ If a currency code is already set up, it will not be available in the list of currency codes when setting up a new currency. Existing currencies can be edited at any time. Use the following steps to add a currency. Localized Store Experiences: Local currency tokens are available for display in all of our supported languages. For more information on the default language store setting, see Store Profile Settings. 1. Go to Settings › Currencies, th…

### Q1-BC-K0177

**Cited at:** section 1, line 38; section 7, line 144

**Record** (`studies/proposals/records/Q1/bigcommerce/copied.tsv`):
- concern_id: BC-C-030
- placement: decides
- structure: Fees and Billing Terms
- identifier: Fees
- statement: Fees are payable in U.S. Dollars, unless otherwise specified.
- cite_ids: BC-S-0188

**Citation BC-S-0188:** `https://www.commerce.com/terms/fees-and-billing/` | Fees | 2026-06-15 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/112-commerce.com/text.txt` (fetched 2026-10-12T04:20:57Z, captured)
- quote: Fees are payable in U.S. Dollars, unless otherwise specified.
- title: Fees and Billing | Commerce
- in context: …PressPress Contact UsContact Us The terms below are incorporated into, and form an integral part of, the Commerce Master Services Agreement. Unless otherwise defined herein, capitalized terms shall have the meaning ascribed to them in the Agreement. Any breach of the terms below will be deemed a material breach of the Agreement. Fees. Commerce fees are due in the amount and at the billing date cycle identified on the Website or applicable Order. ⟪Fees are payable in U.S. Dollars, unless otherwise specified.⟫ If you are purchasing Services with a payment card, Commerce will automatically charge your payment card based on your billing date until you validly cancel the Services. The pricing identified on the Website or any Order includes Services for a single store only, unless otherwise specified. Fees may include subscription fees, GMV overage fees, Open Payment Provider Fees, and any other fees described on the Website or in an applicable Order. Ope…

### Q1-BC-K0211

**Cited at:** section 1, line 43

**Record** (`studies/proposals/records/Q1/bigcommerce/copied.tsv`):
- concern_id: BC-C-038
- placement: decides
- structure: Developer docs: Introduction to Multi-Storefront
- identifier: channel
- statement: A merchant creates a new channel to sell in a new context.
- cite_ids: BC-S-0222

**Citation BC-S-0222:** `https://docs.bigcommerce.com/developer/docs/admin/multi-storefront/overview.md` | ## Channels | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/072-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:27Z, captured)
- quote: A merchant creates a new channel to sell in a new context.
- title: Introduction to Multi-Storefront
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. Some merchants want to sell their products in different places. They may want to maintain multiple website-based eCommerce storefronts, or sell products from their store's catalog on other channels, s…
- headings: Introduction to Multi-Storefront > Channels
- in context: …gle.com/bigcommerce-production-dev-center/images/msf-beta-guide/channels-sites-diagram.webp) ## Channels [REST Management API channels reference](/developer/api-reference/rest/admin/management/channels) A **channel** is a place where a merchant's store sells products. Storefront websites, marketplaces like Amazon and eBay, point-of-sale systems, and marketing feeds are all sales channels. A custom channel may not fit into any one of these types. ⟪A merchant creates a new channel to sell in a new context.⟫ Channels can help to organize a merchant's complex business by allowing them to sell to many customers in many places from a single catalog in one BigCommerce store. In a transactional context, channel objects link together a variety of other objects that describe a particular shopper's experience on a sales channel. ![channels-sites-diagram.webp](https://storage.cloud.google.com/bigcommerce-production-dev-center/images/msf-beta-guide/channels-s…

### Q1-BC-P0030

**Cited at:** section 1, line 48

**Record** (`studies/proposals/records/Q1/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-029
- bullet: e
- placement: decides
- identifier: BigCommerce Payments (bigcommerce.co.uk): Where is it available?
- statement: Initially, BigCommerce Payments is available only to US- and UK-based merchants with self-serve and retail plans. Additional regions and countries will be launching soon.
- scope: US- and UK-based merchants with self-serve and retail plans
- conditions: S01-BC-039;S01-BC-041;S01-BC-043;S01-BC-044;S01-BC-051;S01-BC-055
- cite_ids: S01-BC-C031
- from: new

**Citation S01-BC-C031:** `https://www.bigcommerce.co.uk/payments/bigcommerce-payments/` | FAQs: Where is it available? | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/106-bigcommerce.co.uk/text.txt` (fetched 2026-10-12T10:51:14Z, captured)
- quote: Initially, BigCommerce Payments is available only to US- and UK-based merchants with self-serve and retail plans. Additional regions and countries will be launching soon.
- title: BigCommerce Payments – a native payments experience.
- in context: …then add payment options as you grow. One platform. One payout. PayPal confidence. Start your free trial SIMPLE AND EASY Pricing that scales with you. No hidden monthly fees. Rates vary by plan. All plans include access to PayPal, PayPal Pay Later, Klarna, Clearpay, Apple Pay, and Google Pay in one integration. Core Card processing rate: 1.4% + £0.30 Growth Card processing rate: 1.4% + £0.30 Scale & Performance Card processing rate: 1.2% + £0.30 ⟪Initially, BigCommerce Payments is available only to US- and UK-based merchants with self-serve and retail plans. Additional regions and countries will be launching soon.⟫ See BigCommerce documentation or contact support to confirm whether your account qualifies. Additional payment methods: PayPal Pay Later & Checkout: 2.9% + £0.30 BNPL (Klarna, Clearpay): 4.99% + £0.30 Rates shown are indicative, not guaranteed. Availability and features may vary by region and merchant eligibility. See BigCommerce documentation for details. NATIVE FEATURES Everything under one roof - from checkout to payouts. The payment methods …

### Q1-BC-061

**Cited at:** section 1, line 53; section 3, line 97

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-061
- bears_on: 5
- identifier: Manage Settings permission
- statement: In order to manage the currency settings in your store, you must have the Manage Settings permission enabled on your user account. This is enabled by default for users with the Store Administrator or Store Owner role.
- cite_ids: Q1-BC-C094
- from: held

**Citation Q1-BC-C094:** `https://support.bigcommerce.com/s/article/Managing-Currencies` | Requirements | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/033-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:36Z, captured)
- quote: In order to manage the currency settings in your store, you must have the Manage Settings permission enabled on your user account. This is enabled by default for users with the Store Administrator or Store Owner role.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …n your customers' local currencies provides a more familiar shopping experience and can increase conversion when expanding your store to a new region. In this article, you'll learn how to add currencies to your store, update your store's default currency, and manage how prices appear on your storefront when a specific currency is selected. For more information on how multicurrency works in BigCommerce, see Using Multiple Currencies. Requirements ⟪In order to manage the currency settings in your store, you must have the Manage Settings permission enabled on your user account. This is enabled by default for users with the Store Administrator or Store Owner role.⟫ To learn more about the requirements for offering multiple transactional currencies in your store, see Using Multiple Currencies. Adding a Currency Setup Currency display configurations Transactions Additional display settings SETUP When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live. If a curre…

### Q1-BC-049

**Cited at:** section 1, line 54; section 2, line 75

**Record** (`studies/proposals/records/Q1/bigcommerce/statements.tsv`):
- stmt_id: Q1-BC-049
- bears_on: 5
- identifier: transactional
- statement: In Bigcommerce, a currency can be transactional or used for display only. In order for a currency to be transactional, a payment gateway that supports the currency must be enabled.
- cite_ids: Q1-BC-C078
- from: held

**Citation Q1-BC-C078:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | How Multicurrency Works in Different Parts of the Store | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:41:00Z, captured)
- quote: In Bigcommerce, a currency can be transactional or used for display only. In order for a currency to be transactional, a payment gateway that supports the currency must be enabled.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …'s bank account country, additional cross-border fees may apply that can change the final settlement amount. You can choose whether a currency should be display-only or transactional when adding or editing a currency. How Multicurrency Works in Different Parts of the Store You can enable multiple currencies in your control panel from Settings › Currencies. To learn how to add new currencies and set your default currency, see Managing Currencies. ⟪In Bigcommerce, a currency can be transactional or used for display only. In order for a currency to be transactional, a payment gateway that supports the currency must be enabled.⟫ Once you've enabled multiple currencies, certain aspects of the store, such as orders, payment methods, and analytics, will be handled differently. Orders Shipping Refunds Supported Payment Methods Price Lists Modifiers Analytics ORDERS The View Orders page in the control panel includes the currency the order was transacted in. The order history page in a customer's storefront account displays past orders in the currency their order was transact…

### Q1-BC-P0048

**Cited at:** section 1, line 55; section 2, line 77; section 3, line 98

**Record** (`studies/proposals/records/Q1/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-047
- bullet: b
- placement: decides
- identifier: Embedded Payment Providers: How to add or switch a payment provider
- statement: Each provider has its own application process. 3. Apply and configure Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments.
- cite_ids: S01-BC-C061;S01-BC-C062
- from: new
- note: The page lists 21 Embedded Payment Providers, BigCommerce Payments among them.

**Citation S01-BC-C061:** `https://www.bigcommerce.com/payments/embedded-payment-providers/` | How to add or switch a payment provider: 2. Choose | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/011-bigcommerce.com/text.txt` (fetched 2026-10-13T00:35:32Z, captured)
- quote: Each provider has its own application process.
- title: Embedded Payment Providers | BigCommerce
- in context: …end to end, depending on the provider, account underwriting, and reconciliation needs. The four-step process includes: 1. Decide Compare your current fee exposure to the cost of switching. For some customers the fee is smaller than the switching cost. Additional information can be found in the Help Center about Payment Gateways. 2. Choose Pick a provider from the list above based on your country, currency, payment methods, and integration needs. ⟪Each provider has its own application process.⟫ 3. Apply and configure Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments. 4. Test and launch Run test transactions before going live. Review your reconciliation flows. Monitor your first few weeks of orders to confirm everything is working. Need help along the way? BigCommerce support is available throughout the process. Detailed setup guides are available in the Help …

**Citation S01-BC-C062:** `https://www.bigcommerce.com/payments/embedded-payment-providers/` | How to add or switch a payment provider: 3. Apply and configure | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/011-bigcommerce.com/text.txt` (fetched 2026-10-13T00:35:32Z, captured)
- quote: Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments.
- title: Embedded Payment Providers | BigCommerce
- in context: …ciliation needs. The four-step process includes: 1. Decide Compare your current fee exposure to the cost of switching. For some customers the fee is smaller than the switching cost. Additional information can be found in the Help Center about Payment Gateways. 2. Choose Pick a provider from the list above based on your country, currency, payment methods, and integration needs. Each provider has its own application process. 3. Apply and configure ⟪Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments.⟫ 4. Test and launch Run test transactions before going live. Review your reconciliation flows. Monitor your first few weeks of orders to confirm everything is working. Need help along the way? BigCommerce support is available throughout the process. Detailed setup guides are available in the Help Center. Frequently asked questions What is the Open Payment Provider Fee? A monthly fee charged by BigCommerce for orders processed through Open Payment…
