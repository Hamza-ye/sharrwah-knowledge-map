# Cards: Q1 on shopify

27 records cited by `studies/proposals/drafts/Q1/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Shopify sets up per place in a market, "a set of customers that you define in your store"; a sub-region market "targets a specific state or province", and on it "you can customize only the shipping options". Q1-SH-014, Q1-SH-021, Q1-SH-022
- **section 1, line 12:** - What a market or storefront can set for itself, matching on role (basis 4): Shopify lists "currency, product availability, theme content, domains, languages, and taxes"; Salla's market page holds currencies, branches, shipping, domain, login options and design; a Zid market has a name, countries and "عملة السوق"; BigCommerce's storefronts set domains, themes, currencies and price lists. Q1-SH-K1931, Q1-SA-004, Q1-ZD-004, Q1-BC-005
- **section 1, line 15:** - Payment methods: Shopify shows local payment methods on a market's payments card when it "contains a country that is eligible"; Salla lets the merchant "تخصيص طرق الدفع حسب السوق الذي يختاره العميل"; BigCommerce sets them for each transactional currency. Q1-SH-051, Q1-SA-033, Q1-BC-053
- **section 1, line 16:** - A legal entity, on Shopify Plus: "A business entity is the legal entity that processes payments for orders in a market", and "Each entity has its own Shopify Payments account, payout currency, and bank account". Q1-SH-041, Q1-SH-K1268
- **section 1, line 17:** - What stays one for the whole store: on Shopify, "Staff permissions can't be assigned per market", while Salla can restrict a role "بحسب السوق المطلوب"; on BigCommerce, orders arrive in one area with "storefront attribution", and the store's address type and country are "inherently global" (not checked on Zid), as WooCommerce's store address, "the location where you are based as a seller", is one, a match on role (basis 4). Q1-SH-035, Q1-SA-028, Q1-BC-003, Q1-BC-018, Q1-WC-001
- **section 1, line 18:** - Placing a buyer, matching on role (basis 4): Shopify uses the IP address or "a market-specific domain, subdomain, or subfolder"; Salla's buyer picks the market; WooCommerce offers "Geolocate". Q1-SH-060, Q1-SH-061, Q1-SA-032, Q1-WC-005
- **section 1, line 19:** - Buyers outside the store's places, matching on role (basis 4): on Shopify they "can browse your store, but can't complete a purchase"; Salla's merchant can confine buying "على السوق المطابق لدولة العميل"; WooCommerce's shipped code has an optional zone for "any regions that have not been listed above". Q1-SH-018, Q1-SA-022, Q1-WC-027
- **section 1, line 23:** - Shopify: a market without its own customization "inherits the value from its parent market", and with no parent "the store default is used". Staff reach Markets through permissions such as `CREATE_AND_EDIT_MARKETS` (shipped admin code), and apps through the `read_markets` and `write_markets` scopes. Q1-SH-008, Q1-SH-K0176, Q1-SH-K0862
- **section 1, line 31:** - Who contracts with the seller follows the seller's place in three platforms' terms, matching on role (basis 4): Shopify contracts "based on the billing address of your Store"; BigCommerce's table runs by the merchant's country of residence down to "Any other jurisdiction"; WooCommerce names "WooCommerce Ireland Ltd." for residents of its "Designated Countries". Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499
- **section 1, line 32:** - One store's saved step text (capture-advanced, 4 October 2026) ties its address to its business entity: switching "will update this store's business details"; once a United States entity was chosen, the markup held "Store address must be in the same country as the business entity" and, with no match in the accessibility tree, "Store address will update to match new legal entity", which "may affect subscription fees, billing currency and apps"; and a dialog's markup, with nothing to show it was open, holds "To switch your legal entity, contact support to deactivate active Shopify Payments, Balance, and Capital accounts." Q1-SH-114, Q1-SH-117, Q1-SH-116, Q1-SH-118
- **section 1, line 34:** - The platform's own payment product depends on where the seller is based, matching on role (basis 4), Shopify's in its payments terms and the others in help pages: Shopify Payments needs "a business located in your Designated Country"; Zid Pay is "متاح لتجار المملكة العربية السعودية و دولة الكويت"; WooPayments counts the country "where your business is registered — not the one in which you personally live"; BigCommerce Payments needs a store "located in the United Kingdom or the United States"; Salla pays UAE stores "كل يوم خميس" once their balance passes 250 dirhams. Q1-SH-K1536, Q1-ZD-K0005, Q1-WC-K0402, Q1-BC-P0068, Q1-SA-K1547
- **section 1, line 37:** - What is offered depends on the seller's place, matching on role (basis 4): where Shopify Payments "isn't available in your country", the seller chooses another provider; WooCommerce's code (shipped) keeps "The payment extension list for each country"; Salla's multiple markets feature "is currently available only in Saudi Arabia". Shopify's admin code (shipped) gates Shopify Balance on `"regions":["US"]`, and one Salla session's feature list (observed, 9 October 2026) gives `kyc_new_workflow` the list `"countries": ["AE", "SA", "KW", "QA", "OM", "BH"]`. Q1-SH-065, Q1-WC-K0054, Q1-SA-036, Q1-SH-K0041, Q1-SA-K1988
- **section 1, line 38:** - Fees by place, matching on role (basis 4), Shopify's in a help page and the others in their terms: Shopify's currency conversion fee "is either 1.5% or 2%, depending on your store's location"; BigCommerce's "Fees are payable in U.S. Dollars, unless otherwise specified"; Zid's are "بالريال السعودي أو بعملة التاجر المحلية". Q1-SH-057, Q1-BC-K0177, Q1-ZD-K0156
- **section 1, line 39:** - Yemen, as observed on Shopify: for capture-gb-plus on 5 October 2026, with a business entity address of `"countryCode":"YE"`, Shopify Payments was `"eligible":false` and Stripe `"available":false,"eligible":false`; fake-demo-sharrwah, with a Sanaa address, was listed third-party providers that day, Tap Payments and Cybersource among them; and ibx5bt-xy, billed at `"countryCodeV2":"YE"` (29 September 2026), had "Choose a provider" in its saved Payments step text of 30 September 2026. WooCommerce's code (shipped) suggests only `VISA` for store country YE. Q1-SH-094, Q1-SH-098, Q1-SH-095, Q1-SH-103, Q1-SH-092, Q1-SH-123, Q1-WC-K0333
- **section 2, line 62:** - It draws on WooCommerce's standard country list and BigCommerce's countries, states and provinces, with levels below country from Shopify's sub-region markets, Salla's markets for an "منطقة أو مدينة" and BigCommerce's tax zones. Why: places are data (rule 1) behind their own part (rule 2), with levels below country from the start, since adding them later changes every record naming a place (rule 3). Not taken: countries only, as in WooCommerce's selling locations, since Shopify and BigCommerce set delivery and tax below a country. Q1-WC-K1382, Q1-SH-022, Q1-SA-K1976, Q1-BC-129, Q1-WC-K0536
- **section 2, line 63:** - **Operating place**, proposed: a place, or a group of places, whose sellers Sharrwah serves, with their set-up: the contracting entity, terms and law; the currency of Sharrwah's fees and their tax; verification and documents; the payment providers offered, in order; the services offered; the default store currency and language; and where store data is kept. One set-up can serve every place not named. Q1-SH-K1243, Q1-BC-K0425
- **section 2, line 66:** - **Seller entity**, proposed: the person or company that sells: its kind, its country of registration (for a person, of residence), its address, documents and bank account. Its country is the store's **home place**, which picks the operating place; the store's own address, in that country, serves tax and delivery. Q1-WC-K0402, Q1-WC-001, Q1-SH-117
- **section 2, line 67:** - It takes the country of registration from WooPayments; the entity apart from the store, used "for financial products, markets, apps, and taxes in this shop" (capture-gb-plus, observed 5 October 2026), with the store's address in its country (capture-advanced's saved step text, 4 October 2026), from Shopify; and the sign-up country from Salla. Sharrwah verifies it, and it changes only by a controlled change acting on new orders, as Shopify asks a seller to "promptly update your location", a market's entity change "affects only new orders", and Zid wants an empty wallet before a store changes country. Why: apart from the store, it lets one seller run several stores, and a market later use another entity, without changing stored records (rule 3). Q1-WC-K0402, Q1-SH-100, Q1-SH-117, Q1-SA-K1989, Q1-SH-K1271, Q1-SH-043, Q1-ZD-K0230
- **section 2, line 71:** - **Market**, proposed: a part of a store that sells to chosen places from the register, with its own values for some settings and the store's defaults for the rest: currencies, prices and products, languages and web address, theme content, payment methods and delivery options, and later tax display and a legal entity. Every store has a **home market** from creation; the seller adds others, each a draft, hidden or active; each order records its market. Q1-SH-K1931, Q1-BC-017, Q1-SH-008
- **section 2, line 74:** - **Market selection**, proposed: a buyer is placed by the market's web address, else by choice, else by location; the seller can confine checkout to the market's places, and chooses the **fallback** for a buyer in no market, browsing only or buying in the home market, since Shopify blocks such buying while Salla and WooCommerce make it optional. The rest is left to the build (rule 3). Q1-SH-061, Q1-SA-032, Q1-SH-018, Q1-SA-022, Q1-WC-027
- **section 2, line 76:** - It takes the two kinds from BigCommerce's display and transactional currencies and Shopify's gateway-bound local currency, and the price modes from Salla's per-market or automatic prices and Zid's copied, converted or manual ones. Why: what the buyer is charged in decides what the provider must support and what reaches the seller (rule 3); rates come from sources that change, so the rate source is its own part (rule 2). Q1-SA-019, Q1-ZD-011, Q1-SH-057
- **section 2, line 77:** - **Payment provider**, proposed: a company that takes buyers' payments for a seller, in Sharrwah's **provider catalogue** with its places, currencies and methods. For each operating place Sharrwah sets which providers are offered, in order. The seller makes a **provider connection** with credentials from their own account, after the provider's onboarding, and turns **payment methods** on per market and per charged currency. Q1-SH-065, Q1-SA-K1656, Q1-BC-P0048
- **section 2, line 78:** - It takes the offer by the seller's place from Shopify and WooCommerce, the seller's own credentials from Salla and Zid, the provider's underwriting from BigCommerce, methods per market from Shopify and Salla, and per currency from BigCommerce. Why: providers change, so they sit behind one interface (rule 2); and the seller contracts with the provider, which settles under that contract, as Salla's page on Tabby says, so no seller money is held through Sharrwah (rule 3, the guard). Q1-WC-K0054, Q1-ZD-K0094, Q1-SH-051, Q1-SA-033, Q1-SA-089
- **section 2, line 80:** - **Availability rule**, proposed: for each feature, service and provider, the operating places and plans where Sharrwah offers it, set by Sharrwah and read wherever something is offered (rule 1); it takes places as keys from Shopify Balance and Salla's `kyc_new_workflow`, and plans from Zid's markets. Q1-SH-K0041, Q1-SA-K1988, Q1-ZD-K0235
- **section 2, line 82:** - **Market access**, proposed and left to the build (rule 3): staff can be limited to a market, as on Salla and unlike Shopify, and apps reach markets through scopes, as Shopify's `read_markets`. Q1-SA-028, Q1-SH-035, Q1-SH-K0862
- **section 3, line 88:** - Set per operating place: all of its set-up (section 2), places sharing one and one serving every place not named. Q1-SH-K1243, Q1-BC-K0425
- **section 3, line 89:** - Set per seller entity: its country, documents, bank account and payment accounts, as each Shopify entity has its own payments account, payout currency and bank account; the store's address stays in its country. Q1-SH-K1268, Q1-SH-117
- **section 3, line 91:** - Set per market: its places and the settings it holds for itself (section 2). Q1-SH-K1931, Q1-SA-004
- **section 3, line 97:** - Set by the seller's staff, by permission, as on Shopify and BigCommerce. Q1-SH-K0176, Q1-BC-061
- **section 4, line 112:** 11. Later, and only on the decisions in section 5: a market's own legal entity, a merchant-of-record service, and any arrangement that holds sellers' money through Sharrwah (A-12). Q1-SH-041, Q1-SH-K1958
- **section 5, line 116:** - Levels below country. The records don't settle which settings vary below a country: Shopify's sub-region markets customize "only the shipping options", while Salla's markets reach an "منطقة أو مدينة" but tax by market needs "دولة واحدة فقط"; in Yemen, facts hold at cities and at areas of control (section 6). Keep the register's levels open, areas of control among them, and each setting's levels; the design settles them. Q1-SH-022, Q1-SA-K1976, Q1-SA-023, YK-12 (split @ Sana'a and Aden, as of 2026)
- **section 5, line 119:** - Provider connections by area. In Yemen a provider from one area operates in the other only with separate infrastructure, and each Shopify entity holds its own payments account. Keep a provider connection able to belong to a market or an area, not only to a store; the design settles it with the providers' terms. YK-124 (only with separate infrastructure in the other area @ Aden, as of 2024-04-05), Q1-SH-K1268
- **section 5, line 120:** - A market's own legal entity. Shopify Plus lets a market use another entity, whose change "affects only new orders". Keep a market able to name a seller entity, and each order the entity that sold; sellers' demand and the founder settle when it is built. Q1-SH-041, Q1-SH-043
- **section 5, line 122:** - The rate source. Where Salla's automatic prices take their rate was not in what was read (not checked on Zid); WooPayments takes its rates from its server, and Shopify's automatic rates carry a fee by the store's location. Keep the rate source its own part and each order's rate on the order; a company decision on a rate provider settles it, with section 6. Q1-SA-N02, Q1-WC-K0755, Q1-SH-057
- **section 5, line 124:** - Markets within markets. A Shopify market inherits from a parent, and "Different customizations follow different inheritance rules". Keep a market able to have a parent; the design settles it. Q1-SH-008, Q1-SH-009
- **section 6, line 133:** - **Payment provider** and **provider connection**: Stripe was unavailable for Yemen, as for the Shopify store capture-gb-plus with its Yemen entity address on 5 October 2026, while a merchant uses Cash Pay's payment API with credentials of its own; this allows an offer for Yemen unlike other places', and a connection by the seller's own credentials, at these services and dates: Q1-SH-095, YA-62 (Unavailable @ Stripe's service, as of 2026-10-10), YA-115 (a username, a service-provider ID and an encrypted password, and a certificate for release @ Cash Pay (Cash e-wallet)'s service, as of 2024-03-17).
- **section 7, line 140:** - Where Sharrwah's company is based, and which entity contracts with sellers in each operating place, under which law and terms. Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499, Q1-SA-095
- **section 7, line 144:** - The currency of Sharrwah's own fees, and the tax charged on them, in each place. Q1-SA-096, Q1-BC-K0177, Q1-SH-116
- **section 7, line 148:** - Which exchange-rate provider Sharrwah uses, if any. Q1-WC-K0755, Q1-SH-057

## The cards

### Q1-SH-014

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-014
- bears_on: 2
- identifier: Market
- statement: A market is a set of customers that you define in your store. Markets can be made up of countries or regions for cross-border sales, company locations for B2B sales, retail locations for in-person sales, or sales channels for selling across channels.
- cite_ids: Q1-SH-C014
- from: held

**Citation Q1-SH-C014:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md` | Important markets concepts > Market | 2026-10-16 | kind: stated | quote check: found
- quote: A market is a set of customers that you define in your store. Markets can be made up of countries or regions for cross-border sales, company locations for B2B sales, retail locations for in-person sales, or sales channels for selling across channels.
- title: Overview of markets features and concepts
- the page opens: By using Markets, you can customize and tailor your customer experience for different regions, customer groups, retail locations, and sales channels. Each market represents a set of customers, such as those in a particular region, and the customizations you apply to that market determine what experience those customers get when they visit your store. Markets are made up of two key components: * Conditions: Conditions define who your market applies to. Conditions can be countries and regions for …
- headings: Overview of markets features and concepts > Important markets concepts {#concepts} > Market
- in context: …ies globally, then you can configure markets to use business entities in different global regions. Configuring business entities requires the Plus plan. <a href="/manual/markets/getting-started/requirements-and-considerations#plan-reqs">Learn more about the plan requirements for Markets features</a>.</td> </tr> </tbody> </table> ## Important markets concepts {#concepts} Before you start creating markets, review the following concepts. ### Market ⟪A market is a set of customers that you define in your store. Markets can be made up of countries or regions for cross-border sales, company locations for B2B sales, retail locations for in-person sales, or sales channels for selling across channels.⟫ When you create new markets for the first time, their market customizations inherit your store's default settings. If you create a submarket, then the submarket inherits its customizations from the parent market. You can override inherited values and customize the following aspects of your store: * [Currency](/manual/markets/customizations/local-currencies) * [Catalogs](/manual/markets/customizations/catalogs) (product prices and publishing) * […

### Q1-SH-021

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-021
- bears_on: 1
- identifier: Sub-region markets
- statement: A sub-region market targets a specific state or province, instead of a whole country.
- marker: Early access
- cite_ids: Q1-SH-C021
- from: held

**Citation Q1-SH-C021:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md` | Sub-region markets | 2026-10-16 | kind: stated | quote check: found
- quote: A sub-region market targets a specific state or province, instead of a whole country.
- title: Understanding market types
- the page opens: Markets can be created for different types of customers depending on how you sell. Each market type uses a different kind of condition to define its audience. You can combine market types in the same store to manage cross-border selling, wholesale, retail, and selling across sales channels from a single place. Country or region markets Country or region markets are displayed to customers based on their geographic location. These markets are used for cross-border and international selling. When a…
- a note box: Early access Sub-region markets are available as an early access feature. Features and functionality might change before general availability.
- a note box: Plan requirement Retail markets are available for all Shopify plans. Customizing catalogs to use with retail markets requires Shopify POS Pro or the Plus plan.
- a note box: Plan requirement On the Basic, Grow, and Advanced plans, you can assign up to 3 active catalogs across all your B2B markets. Assigning 3 catalogs to one B2B market uses the full limit. You need to remove or draft an existing assignment before you can add catalogs to another market. On the Shopify Pl
- headings: Understanding market types > Country or region markets > Sub-region markets {#sub-region-markets}
- in context: …lar selling strategy. For example, if you have the same pricing, products, and shipping strategy for France, Germany, and Italy, then you can create a single Europe market rather than three separate markets. ### Sub-region markets {#sub-region-markets} <aside class="note note-beta"><h4>Early access</h4><p>Sub-region markets are available as an early access feature. Features and functionality might change before general availability.</p> </aside> ⟪A sub-region market targets a specific state or province, instead of a whole country.⟫ Use one when you want different shipping for part of a country. For example, if customers in California need different shipping rates or delivery options than customers in New York, then you can create a separate market for each state and give each one its own [shipping options](/manual/fulfillment/setup/shipping-options). On a sub-region market, you can customize only the shipping options. Everything else, such as currency, catalogs, theme, and…

### Q1-SH-022

**Cited at:** section 1, line 7; section 2, line 62; section 5, line 116

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-022
- bears_on: 1;2
- identifier: Sub-region markets
- statement: On a sub-region market, you can customize only the shipping options. Everything else, such as currency, catalogs, theme, and domain, is inherited from the parent market.
- marker: Early access
- cite_ids: Q1-SH-C022
- from: held

**Citation Q1-SH-C022:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md` | Sub-region markets | 2026-10-16 | kind: stated | quote check: found
- quote: On a sub-region market, you can customize only the shipping options. Everything else, such as currency, catalogs, theme, and domain, is inherited from the parent market.
- title: Understanding market types
- the page opens: Markets can be created for different types of customers depending on how you sell. Each market type uses a different kind of condition to define its audience. You can combine market types in the same store to manage cross-border selling, wholesale, retail, and selling across sales channels from a single place. Country or region markets Country or region markets are displayed to customers based on their geographic location. These markets are used for cross-border and international selling. When a…
- a note box: Early access Sub-region markets are available as an early access feature. Features and functionality might change before general availability.
- a note box: Plan requirement Retail markets are available for all Shopify plans. Customizing catalogs to use with retail markets requires Shopify POS Pro or the Plus plan.
- a note box: Plan requirement On the Basic, Grow, and Advanced plans, you can assign up to 3 active catalogs across all your B2B markets. Assigning 3 catalogs to one B2B market uses the full limit. You need to remove or draft an existing assignment before you can add catalogs to another market. On the Shopify Pl
- headings: Understanding market types > Country or region markets > Sub-region markets {#sub-region-markets}
- in context: …ore general availability.</p> </aside> A sub-region market targets a specific state or province, instead of a whole country. Use one when you want different shipping for part of a country. For example, if customers in California need different shipping rates or delivery options than customers in New York, then you can create a separate market for each state and give each one its own [shipping options](/manual/fulfillment/setup/shipping-options). ⟪On a sub-region market, you can customize only the shipping options. Everything else, such as currency, catalogs, theme, and domain, is inherited from the parent market.⟫ A sub-region market covers a smaller area than the country market, so it's a [submarket](/manual/markets/getting-started/submarkets) of that market. For example, a market for California is a submarket of a market for the United States. You can also target a smaller area for a B2B market. When you add company locations to a market, you can filter them by region or sub-region, such as a state or province. To create a sub-region market, refer to [C…

### Q1-SH-K1931

**Cited at:** section 1, line 12; section 2, line 71; section 3, line 91

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-106
- placement: decides
- structure: https://help.shopify.com/en/manual/markets.md
- identifier: Customizing market experiences
- statement: Customizations control settings, such as currency, product availability, theme content, domains, languages, and taxes.
- cite_ids: SH-S-0541
- note: first run's citation

**Citation SH-S-0541:** `https://help.shopify.com/en/manual/markets.md` | Customizing market experiences | 2026-10-10 | kind: stated | quote check: found
- quote: Customizations control settings, such as currency, product availability, theme content, domains, languages, and taxes.
- title: Markets
- the page opens: You can use Markets to manage how different customers experience your store based on their location, customer group, retail location, or sales channel. Markets let you define audiences using conditions and tailor their experience with customizations, including currency, language, pricing, and theme content. You can manage your markets from the Markets page in your Shopify admin. Understanding and setting up markets Get familiar with the key markets concepts, such as conditions and customizations…
- headings: Markets > Customizing market experiences
- in context: …. ### Understanding and setting up markets Get familiar with the [key markets concepts](/manual/markets/getting-started/overview), such as conditions and customizations that make up each market. When you're ready, you can create markets, choose market types, and configure localization. ### Customizing market experiences You can override your store's default settings for specific markets by adding [customizations](/manual/markets/customizations). ⟪Customizations control settings, such as currency, product availability, theme content, domains, languages, and taxes.⟫ If shipping options by market are available for your store, then you can also set up [shipping options for each market](/manual/fulfillment/setup/shipping-options). The [backup region](/manual/markets/backup-region) determines the experience for customers who don't match any active market. ### Managing discounts, gift cards, and SEO [Discounts and gift cards](/manual/markets/discounts-and-gift-cards) work across markets, but fixed-amount values …

### Q1-SH-051

**Cited at:** section 1, line 15; section 2, line 78

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-051
- bears_on: 1;5
- identifier: Local payment methods
- statement: When a market contains a country that is eligible for one or more local payment methods, then a payments card is displayed in your market settings with the available local payment methods.
- cite_ids: Q1-SH-C051
- from: held

**Citation Q1-SH-C051:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/international/payments.md` | Local payment methods | 2026-10-16 | kind: stated | quote check: found
- quote: When a market contains a country that is eligible for one or more local payment methods, then a payments card is displayed in your market settings with the available local payment methods.
- title: Payments
- the page opens: Your market settings include a payments card that displays eligible local payment methods, as well as a link to your payment settings where you can activate and customize a variety of payment methods. Shopify Payments and other payment providers {#other-payment-providers} Only stores with Shopify Payments or Adyen as the primary gateway can process payments in a customer's local currency. The following payment options are compatible with multi-currency processing: * Shopify Payments credit card …
- a note box: Tip If you want to encourage your customers to use multi-currency compatible payment methods, then use Shopify Scripts to hide other payment providers for customers who have a foreign currency at checkout.
- headings: Payments > Local payment methods {#local-payment-methods}
- in context: …total up and your customer pays €8.90 EUR. <aside class="note note-information"><h4>Tip</h4><p>If you want to encourage your customers to use multi-currency compatible payment methods, then use Shopify Scripts to <a href="/en/manual/checkout-settings/script-editor/examples/payment-gateway-scripts">hide other payment providers for customers who have a foreign currency at checkout</a>.</p> </aside> ## Local payment methods {#local-payment-methods} ⟪When a market contains a country that is eligible for one or more local payment methods, then a payments card is displayed in your market settings with the available local payment methods.⟫ For example, you have a market for Europe that only contains Belgium, then Bancontact is available on the payments card. If you have a market for Europe that contains both Belgium and Netherlands, then both Bancontact and iDEAL | Wero are available on the payments card. From the payments card, you can activate or deactivate an eligible local payment method. Learn more about [local payment methods](/manual/payments/shopify-payments/local-payment-…

### Q1-SH-041

**Cited at:** section 1, line 16; section 4, line 112; section 5, line 120

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-041
- bears_on: 1
- identifier: Business entities
- statement: A business entity is the legal entity that processes payments for orders in a market.
- scope: Plus plan only
- cite_ids: Q1-SH-C041
- from: held

**Citation Q1-SH-C041:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md` | Setting up business entities for markets | 2026-10-16 | kind: stated | quote check: found
- quote: A business entity is the legal entity that processes payments for orders in a market.
- title: Setting up business entities for markets
- the page opens: Plan requirement Business entities are available on the Plus plan only. A business entity is the legal entity that processes payments for orders in a market. If your business has different legal entities in different countries or regions, then you can assign specific business entities to specific markets so that payments are processed through the correct entity. By default, all orders in your store are processed through your primary Shopify Payments account, which is associated with your store's…
- a note box: Plan requirement Business entities are available on the Plus plan only.
- a note box: Caution To avoid payments being processed through an incorrect business entity, verify that your submarkets are inheriting the expected business entity. If there's any ambiguity due to multiple parents, then add an explicit business entity customization to the submarket.
- a note box: Caution Before you can assign business entities to markets, you need to set up additional Shopify Payments accounts for each legal entity. Refer to Selling with multiple entities to learn more.
- headings: Setting up business entities for markets
- in context: # Setting up business entities for markets <aside class="note note-plan"><h4>Plan requirement</h4><p>Business entities are available on the Plus plan only.</p> </aside> ⟪A business entity is the legal entity that processes payments for orders in a market.⟫ If your business has different legal entities in different countries or regions, then you can assign specific business entities to specific markets so that payments are processed through the correct entity. By default, all orders in your store are processed through your primary Shopify Payments account, which is associated with your store's home country. If you have multiple Shopify Payments accounts for different legal entities in different cou…

### Q1-SH-K1268

**Cited at:** section 1, line 16; section 3, line 89; section 5, line 119

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-005
- placement: boundary
- structure: https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md
- identifier: Connect Shopify Payments to each entity
- statement: Each entity has its own Shopify Payments account, payout currency, and bank account, so you need to complete this process for every entity that you want to activate.
- cite_ids: SH-S-0258
- note: first run's citation

**Citation SH-S-0258:** `https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md` | Connect Shopify Payments to each entity | 2026-10-10 | kind: stated | quote check: found
- quote: Each entity has its own Shopify Payments account, payout currency, and bank account, so you need to complete this process for every entity that you want to activate.
- title: Selling with multiple entities
- the page opens: Plan requirement Selling from multiple entities with Shopify Payments is available only for organizations on the Shopify Plus and Shopify Enterprise Commerce plan. You can sell from multiple entities in a single store both online and using Shopify POS with Shopify Payments. This lets you streamline your business operations, operate multiple legal entities within the same country, expand internationally, and manage payouts and orders in the same store. Supported structures include online and reta…
- a note box: Plan requirement Selling from multiple entities with Shopify Payments is available only for organizations on the Shopify Plus and Shopify Enterprise Commerce plan.
- a note box: Note If you want to add a business entity to your Shopify account, then learn more about managing business entities.
- headings: Selling with multiple entities > Selling from multiple entities {#selling-multiple-entities} > Connect Shopify Payments to each entity {#connect-shopify-payments-to-entity}
- in context: …fy Payments. #### Steps: 1. From your Shopify admin, go to **Settings** > [**Organization**](https://admin.shopify.com/settings/organization-details). 2. Add each business entity that you want to sell from. Learn more about [adding business entities](/manual/your-account/business-entities). ### Connect Shopify Payments to each entity {#connect-shopify-payments-to-entity} After adding your entities, connect a Shopify Payments account to each one. ⟪Each entity has its own Shopify Payments account, payout currency, and bank account, so you need to complete this process for every entity that you want to activate.⟫ #### Steps: 1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments). 2. In the **Shopify Payments** section, click **Add Shopify Payments account**. 3. Select the business entity, and then complete the account setup. 4. Complete identity verification if prompted. 5. After connecting your entity, repeat the connection process to Shopify Payments for all other business entities. ### Assign entit…

### Q1-SH-035

**Cited at:** section 1, line 17; section 2, line 82

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-035
- bears_on: 1
- identifier: Staff permissions for using Markets
- statement: Staff permissions can't be assigned per market. If a staff member has permission to view orders, then they can view orders from all markets.
- cite_ids: Q1-SH-C035
- from: held

**Citation Q1-SH-C035:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/requirements-and-considerations.md` | Staff permissions for using Markets, note | 2026-10-16 | kind: stated | quote check: found
- quote: Staff permissions can't be assigned per market. If a staff member has permission to view orders, then they can view orders from all markets.
- title: Requirements and considerations for using markets
- the page opens: Before you set up Markets, review the requirements, considerations, staff permissions, and plan availability to make sure Markets fits your business. Requirements for using Markets To use Markets, your store needs to meet the following requirements: * To accept payments in multiple currencies, you need to use Shopify Payments or Adyen as your payment processor. If you use a different payment processor, then customers in all markets pay in your store's default currency. * You need to have shippin…
- a note box: Note Staff permissions can't be assigned per market. If a staff member has permission to view orders, then they can view orders from all markets.
- headings: Requirements and considerations for using markets > Considerations for using Markets
- in context: …tyle="text-align:center; color:#7ab55c">✔</td> </tr> <tr> <td scope="row"><a href="/manual/your-account/business-entities">Customize business entities in different markets</a></td> <td style="text-align:center">✘</td> <td style="text-align:center">✘</td> <td style="text-align:center">✘</td> <td style="text-align:center; color:#7ab55c">✔</td> </tr> </tbody> </table> </div> ## Staff permissions for using Markets <aside class="note"><h4>Note</h4><p>⟪Staff permissions can't be assigned per market. If a staff member has permission to view orders, then they can view orders from all markets.⟫</p> </aside> To access the **Markets** page, a staff member needs all of the following permissions: * Home * Orders (all permissions) * Products (all permissions) * Analytics (all permissions) * Discounts (all permissions) * Catalogs (create and edit) * Store settings: manage settings, shipping and delivery, taxes and duties, domains

### Q1-SH-060

**Cited at:** section 1, line 18

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-060
- bears_on: 1
- identifier: Determining markets
- statement: When a customer first visits your store, their geographic location is determined by using their IP address, and they're matched to the appropriate market.
- cite_ids: Q1-SH-C060
- from: held

**Citation Q1-SH-C060:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/localization.md` | Determining markets | 2026-10-16 | kind: stated | quote check: found
- quote: When a customer first visits your store, their geographic location is determined by using their IP address, and they're matched to the appropriate market.
- title: Setting up localization for markets
- the page opens: When customers visit your online store, they need to be matched to the right market so they receive the right customer experience. This process is also known as localization or localized customer experience. You have options for both automatic and manual localization, depending on your preferences. Localizing customers to the correct market experience directly affects your conversion rates and customer satisfaction: * Customers are more likely to complete a purchase when prices are in a familiar…
- a note box: Note Automatic redirection relies on IP-based geolocation, which isn't always accurate. Customers using VPNs, corporate networks, or certain mobile carriers might be detected in the wrong location. For this reason, it's recommended to also provide a country and language selector so customers can cho
- a note box: Note If your online store theme doesn't have selectors, then customers who are incorrectly localized have no way to switch to the correct experience.
- headings: Setting up localization for markets > Determining markets
- in context: … customers in Europe expect tax-inclusive prices, but customers in the United States expect tax to be added during checkout. Showing the wrong format creates confusion. * Some regions require specific pricing formats, tax displays, or product information. Localizing customers to the correct market helps you to meet these requirements. ## Determining markets Markets for a customer are automatically determined by using the following information: * ⟪When a customer first visits your store, their geographic location is determined by using their IP address, and they're matched to the appropriate market.⟫ * The customer's browser language preferences are used to determine which language to display, if you've configured multiple languages for that market. * If a customer arrives on a market-specific domain, subdomain, or subfolder (for example, yourstore.com/fr/), then they get the experience for that market. * If a customer manually chooses a different country or language by using your store's selectors, then their preference is saved and used fo…

### Q1-SH-061

**Cited at:** section 1, line 18; section 2, line 74

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-061
- bears_on: 1
- identifier: Determining markets
- statement: If a customer arrives on a market-specific domain, subdomain, or subfolder (for example, yourstore.com/fr/), then they get the experience for that market.
- cite_ids: Q1-SH-C061
- from: held

**Citation Q1-SH-C061:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/localization.md` | Determining markets | 2026-10-16 | kind: stated | quote check: found
- quote: If a customer arrives on a market-specific domain, subdomain, or subfolder (for example, yourstore.com/fr/), then they get the experience for that market.
- title: Setting up localization for markets
- the page opens: When customers visit your online store, they need to be matched to the right market so they receive the right customer experience. This process is also known as localization or localized customer experience. You have options for both automatic and manual localization, depending on your preferences. Localizing customers to the correct market experience directly affects your conversion rates and customer satisfaction: * Customers are more likely to complete a purchase when prices are in a familiar…
- a note box: Note Automatic redirection relies on IP-based geolocation, which isn't always accurate. Customers using VPNs, corporate networks, or certain mobile carriers might be detected in the wrong location. For this reason, it's recommended to also provide a country and language selector so customers can cho
- a note box: Note If your online store theme doesn't have selectors, then customers who are incorrectly localized have no way to switch to the correct experience.
- headings: Setting up localization for markets > Determining markets
- in context: …to meet these requirements. ## Determining markets Markets for a customer are automatically determined by using the following information: * When a customer first visits your store, their geographic location is determined by using their IP address, and they're matched to the appropriate market. * The customer's browser language preferences are used to determine which language to display, if you've configured multiple languages for that market. * ⟪If a customer arrives on a market-specific domain, subdomain, or subfolder (for example, yourstore.com/fr/), then they get the experience for that market.⟫ * If a customer manually chooses a different country or language by using your store's selectors, then their preference is saved and used for future visits. ## Automatic redirection <aside class="note"><h4>Note</h4><p>Automatic redirection relies on IP-based geolocation, which isn't always accurate. Customers using VPNs, corporate networks, or certain mobile carriers might be detected in the wrong location. For this reason, it's recommended to a…

### Q1-SH-018

**Cited at:** section 1, line 19; section 2, line 74

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-018
- bears_on: 1
- identifier: Country or region markets
- statement: Customers from countries that aren't included in any active market can browse your store, but can't complete a purchase.
- cite_ids: Q1-SH-C018
- from: held

**Citation Q1-SH-C018:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md` | Country or region markets | 2026-10-16 | kind: stated | quote check: found
- quote: Customers from countries that aren't included in any active market can browse your store, but can't complete a purchase.
- title: Understanding market types
- the page opens: Markets can be created for different types of customers depending on how you sell. Each market type uses a different kind of condition to define its audience. You can combine market types in the same store to manage cross-border selling, wholesale, retail, and selling across sales channels from a single place. Country or region markets Country or region markets are displayed to customers based on their geographic location. These markets are used for cross-border and international selling. When a…
- a note box: Early access Sub-region markets are available as an early access feature. Features and functionality might change before general availability.
- a note box: Plan requirement Retail markets are available for all Shopify plans. Customizing catalogs to use with retail markets requires Shopify POS Pro or the Plus plan.
- a note box: Plan requirement On the Basic, Grow, and Advanced plans, you can assign up to 3 active catalogs across all your B2B markets. Assigning 3 catalogs to one B2B market uses the full limit. You need to remove or draft an existing assignment before you can add catalogs to another market. On the Shopify Pl
- headings: Understanding market types > Country or region markets
- in context: …cation. These markets are used for cross-border and international selling. When a customer visits your online store, their location is determined and they're matched to the appropriate country or region market. The customer then receives the experience that you've configured for that market, including currency, language, product availability, and theme customizations. A country or region market can contain a single country or multiple countries. ⟪Customers from countries that aren't included in any active market can browse your store, but can't complete a purchase.⟫ The [backup region](/manual/markets/backup-region) experience is displayed for customers that don't match any active markets. ### Single-country markets Single-country markets contain one country or region. When you create a single-country market, the currency is automatically set to that country's local currency. Use single-country markets when you have a specific selling strategy for a country. For example, if a significant portion of your int…

### Q1-SH-008

**Cited at:** section 1, line 23; section 2, line 71; section 5, line 124

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-008
- bears_on: 2
- identifier: Inheritance
- statement: If a market doesn't have a specific customization, then it inherits the value from its parent market. If there's no parent market, then the store default is used.
- cite_ids: Q1-SH-C008
- from: held

**Citation Q1-SH-C008:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/overview.md` | Inheritance | 2026-10-16 | kind: stated | quote check: found
- quote: If a market doesn't have a specific customization, then it inherits the value from its parent market. If there's no parent market, then the store default is used.
- title: Adding and removing market customizations
- the page opens: When you create a market, it inherits your store's default settings. You can override any of these defaults by adding customizations to the market. Each customization controls a specific aspect of the customer experience. You can customize only catalogs and currencies for channel markets. Customizations apply as soon as you save them. If you want to schedule a catalog's status change, then you can use a rollout to schedule when a catalog becomes active or returns to a draft. Market customization…
- headings: Adding and removing market customizations > Inheritance
- in context: …s experience.</td> </tr> <tr> <td scope="row"><a href="/manual/markets/customizations/duties-and-taxes">Duties and taxes</a></td> <td>How taxes are displayed and whether duties are collected at checkout.</td> </tr> <tr> <td scope="row"><a href="/manual/markets/customizations/business-entities">Business entities</a></td> <td>Which legal entity processes payments for the market. Shopify Plus only.</td> </tr> </tbody> </table> </div> ## Inheritance ⟪If a market doesn't have a specific customization, then it inherits the value from its parent market. If there's no parent market, then the store default is used.⟫ When you add a customization to a market, the setting moves from the **Inherited** section to the **Customized** section on the market detail page. You can remove a customization at any time to revert to the inherited value. Different customizations follow different inheritance rules. Some are overridden by the submarket's value, whereas others (like catalogs) are combined. Refer to each customization's page for details on how inheritance works.…

### Q1-SH-K0176

**Cited at:** section 1, line 23; section 3, line 97

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-106
- placement: decides
- structure: structures/shopify/admin-router
- identifier: option-definition:create
- statement: "eligibility":{"features":["marketDrivenShipping"],"oneOf":[{"permissions":["OVERVIEWS","REPORTS","PRODUCTS","DOMAINS","PREFERENCES"]},{"permissions":["VIEW_MARKETS","CREATE_AND_EDIT_MARKETS"]}]}
- cite_ids: SH-S-5205
- note: section Markets; the same eligibility on 1 more route(s): option-definition:update

**Citation SH-S-5205:** `observed-sh@e49840729:structures/shopify/admin-router/items.jsonl` | line 753 (option-definition:create) | 2026-09-29 | kind: shipped | quote check: found
- quote: "eligibility":{"features":["marketDrivenShipping"],"oneOf":[{"permissions":["OVERVIEWS","REPORTS","PRODUCTS","DOMAINS","PREFERENCES"]},{"permissions":["VIEW_MARKETS","CREATE_AND_EDIT_MARKETS"]}]}
- in context: …Landing-loader-cd13471c6191.js"]},"titleLoader":{"function":true,"imports":["./title-loader-5ef89b2fe33b.js"]},"component":{"function":true,"imports":["./ManagedMarketsLanding-1371e16ce2d3.js"]}} {"id":"option-definition:create","parent":"market","position":8,"array_offset":1960137,"section":"Markets","path":"shipping-option/create","title":{"value":"Add shipping option"},"resource":"option-definition","actionType":"create","context":["intents"],⟪"eligibility":{"features":["marketDrivenShipping"],"oneOf":[{"permissions":["OVERVIEWS","REPORTS","PRODUCTS","DOMAINS","PREFERENCES"]},{"permissions":["VIEW_MARKETS","CREATE_AND_EDIT_MARKETS"]}]}⟫,"sliceName":"markets-section","sliceId":"S-325a46","loader":{"function":true,"imports":["./MarketsV2MarketDetailsPage-customization-shipping-OptionDefinitionsDefinitionCreate-loader-0e3a71bb47b6.js"]},"action":{"function":true,"imports":["./MarketsV2MarketDetailsPage-customization-shipping-OptionDefinitionsDefinitionCreate-action-d419e1c4b6ed.js"]},"component":{"function":true,"imports":["./OptionDefinitionCreate-ff56df8bd66d.js"]},"form":{"func…

### Q1-SH-K0862

**Cited at:** section 1, line 23; section 2, line 82

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-106
- placement: boundary
- structure: structures/shopify/dev-access-lines
- identifier: write_markets
- statement: This path requires both the [`read_markets`](https://shopify.dev/docs/api/usage/access-scopes#read_markets) and [`write_markets`](https://shopify.dev/docs/api/usage/access-scopes#write_markets) scopes. See [Manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes) for how to add them to your app.
- cite_ids: SH-S-6232
- note: https://shopify.dev/docs/apps/build/orders-fulfillment/market-driven-shipping/upgrade-your-app.md

**Citation SH-S-6232:** `observed-sh@e49840729:structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl` | line 2672 (https://shopify.dev/docs/apps/build/orders-fulfillment/market-driven-shipping/upgrade-your-app.md > Upgrade your app for market-driven shipping > Upgrade path: writers > Option B: Write through the Markets API) | 2026-09-30 | kind: stated | quote check: found
- quote: This path requires both the [`read_markets`](https://shopify.dev/docs/api/usage/access-scopes#read_markets) and [`write_markets`](https://shopify.dev/docs/api/usage/access-scopes#write_markets) scopes. See [Manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes) for how to add them to your app.
- headings: Manage access scopes > Step 4: Update your app access scopes > Access scopes that must be granted by the merchant
- in context: …opify.dev/docs/api/usage/access-scopes#read_markets) scope. See [Manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes) for how to add it to your app. `read_markets` Manage access scopes https://shopify.dev/docs/apps/build/orders-fulfillment/market-driven-shipping/upgrade-your-app.md text Upgrade your app for market-driven shipping Upgrade path: writers Option B: Write through the Markets API ⟪This path requires both the [`read_markets`](https://shopify.dev/docs/api/usage/access-scopes#read_markets) and [`write_markets`](https://shopify.dev/docs/api/usage/access-scopes#write_markets) scopes. See [Manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes) for how to add them to your app.⟫ `read_markets` `write_markets` Manage access scopes https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/build-fulfillment-solutions.md text Build fulfillment solutions Requirements * Your app has the `merchant_managed_fulfillment_orders` and `third_party_fulfillment_orders` [access scopes](https://shopify.dev/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](https://shopify.dev/…

### Q1-SH-K1243

**Cited at:** section 1, line 31; section 2, line 63; section 3, line 88; section 7, line 140

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-002
- placement: decides
- structure: https://www.shopify.com/legal/terms
- identifier: 13. Shopify Contracting Party and Forum
- statement: Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store.
- cite_ids: SH-S-0001
- note: first run's citation

**Citation SH-S-0001:** `https://www.shopify.com/legal/terms` | 13. Shopify Contracting Party and Forum | 2026-08-01 | kind: official page | quote check: found
- quote: Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store.
- title: Shopify Terms of Service - Shopify
- in context: …of the Services; b. using third-party proxies or other interventions that impair the security of Account Data; or c. using the Services otherwise in violation of these Terms of Service. To the extent that you impair the security of Account Data, Shopify cannot ensure PCI DSS compliance and is not responsible for the security of Account Data. Information on PCI DSS can be found on the PCI Council's website. 13. Shopify Contracting Party and Forum ⟪Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store.⟫ Forum Selection. Any dispute or claim relating to the Services or these Terms of Service can only be brought in the courts listed in the table below. Those courts have exclusive jurisdiction, and each party agrees to that jurisdiction and will not object to it. MERCHANT BILLING ADDRESS REGION SHOPIFY CONTRACTING PARTY/PARTIES REGISTERED OFFICE FORUM United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, O…

### Q1-SH-114

**Cited at:** section 1, line 32

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-114
- bears_on: 2;3
- identifier: Settings > General > Switch business details
- statement: Switching will update this store's business details. You'll receive multiple tax forms and may need to verify your business.
- scope: store capture-advanced, observed 2026-10-04
- cite_ids: Q1-SH-C237
- from: held
- note: in the saved HTML of step 34; the step's aria.yaml shows the same words

**Citation Q1-SH-C237:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T223401Z-journey-business-entity/034.html.txt` | run 20261004T223401Z-journey-business-entity, step 34 (Settings > General > Switch business details) | 2026-10-04 | kind: observed | quote check: found
- step 34: Switch (business entity) | https://admin.shopify.com/store/capture-advanced/settings/general/business-entity | "capture advanced · General · Shopify" | 2026-10-04T22:43:40.013Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/034.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/034.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T223401Z-journey-business-entity/034.html.txt`
- quote: Switching will update this store's business details. You'll receive multiple tax forms and may need to verify your business.
- in context: …front API Brand Integrate brand assets across sales channels, themes and apps [heading: Resources] Change log View change log Shopify Help Center Get help Hire a Shopify Partner Hire a Partner Keyboard shortcuts Store activity log [heading: Organizations and store transfers] This store can't be transferred because it's a development store created for testing. Remove store from organization Close [heading: Switch business details] Continue Cancel ⟪Switching will update this store's business details. You'll receive multiple tax forms and may need to verify your business.⟫ Search [Search] [ ] My Second Demo Store - entity Yemen [ ] demo fake dev store - entity Yemen [ ] capture plus - entity Yemen [ ] capture grow - entity Yemen [ ] Capture Entity United States

### Q1-SH-117

**Cited at:** section 1, line 32; section 2, line 66; section 2, line 67; section 3, line 89

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-117
- bears_on: 3
- identifier: Settings > General > Confirm store address
- statement: Store address must be in the same country as the business entity Updated store address United States
- scope: store capture-advanced, observed 2026-10-04
- cite_ids: Q1-SH-C240
- from: held
- note: in the saved HTML of step 52; the step's aria.yaml shows the same words in the dialog Confirm store address

**Citation Q1-SH-C240:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T223401Z-journey-business-entity/052.html.txt` | run 20261004T223401Z-journey-business-entity, step 52 (Settings > General > Switch business details, Confirm store address) | 2026-10-04 | kind: observed | quote check: found
- step 52: Confirm (store address United States) | https://admin.shopify.com/store/capture-advanced/settings/general/business-entity | "capture advanced · General · Shopify" | 2026-10-04T22:47:58.254Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/052.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/052.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T223401Z-journey-business-entity/052.html.txt`
- quote: Store address must be in the same country as the business entity Updated store address United States
- in context: …r business. Search [Search] [ ] My Second Demo Store - entity Yemen [ ] demo fake dev store - entity Yemen [ ] capture plus - entity Yemen [ ] capture grow - entity Yemen [ ] Capture Entity United States Store address will update to match new legal entity. This may affect subscription fees, billing currency and apps. Confirm store address [heading: There are 3 errors:] Street must contain letters City must contain letters ZIP code can't be blank ⟪Store address must be in the same country as the business entity Updated store address United States⟫ [accessibilitylabel: Edit] Unsaved changes Cancel Confirm

### Q1-SH-116

**Cited at:** section 1, line 32; section 7, line 144

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-116
- bears_on: 2;3
- identifier: Settings > General > Switch business details: Confirm store address
- statement: Store address will update to match new legal entity. This may affect subscription fees, billing currency and apps.
- scope: store capture-advanced, observed 2026-10-04
- cite_ids: Q1-SH-C239
- from: held
- note: in the saved HTML of step 52, after Capture Entity, United States, was chosen; the step's aria.yaml doesn't show these words; the switch was cancelled at step 71

**Citation Q1-SH-C239:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T223401Z-journey-business-entity/052.html.txt` | run 20261004T223401Z-journey-business-entity, step 52 (Settings > General > Switch business details, Confirm store address) | 2026-10-04 | kind: observed | quote check: found
- step 52: Confirm (store address United States) | https://admin.shopify.com/store/capture-advanced/settings/general/business-entity | "capture advanced · General · Shopify" | 2026-10-04T22:47:58.254Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/052.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/052.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T223401Z-journey-business-entity/052.html.txt`
- quote: Store address will update to match new legal entity. This may affect subscription fees, billing currency and apps.
- in context: …etails] Continue Cancel [heading: There are 3 errors:] Street must contain letters City must contain letters ZIP code can't be blank Switching will update this store's business details. You'll receive multiple tax forms and may need to verify your business. Search [Search] [ ] My Second Demo Store - entity Yemen [ ] demo fake dev store - entity Yemen [ ] capture plus - entity Yemen [ ] capture grow - entity Yemen [ ] Capture Entity United States ⟪Store address will update to match new legal entity. This may affect subscription fees, billing currency and apps.⟫ Confirm store address [heading: There are 3 errors:] Street must contain letters City must contain letters ZIP code can't be blank Store address must be in the same country as the business entity Updated store address United States [accessibilitylabel: Edit] Unsaved changes Cancel Confirm

### Q1-SH-118

**Cited at:** section 1, line 32

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-118
- bears_on: 2;3
- identifier: Settings > General: Switch business details (contact support)
- statement: To switch your legal entity, contact support to deactivate active Shopify Payments, Balance, and Capital accounts.
- scope: store capture-advanced, observed 2026-10-04
- cite_ids: Q1-SH-C241
- from: held
- note: in the saved HTML of step 14 (Settings > General), in a dialog's markup, not marked hidden; the step's aria.yaml doesn't show these words; nothing in the file shows whether the dialog was open

**Citation Q1-SH-C241:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T223401Z-journey-business-entity/014.html.txt` | run 20261004T223401Z-journey-business-entity, step 14 (Settings > General) | 2026-10-04 | kind: observed | quote check: found
- step 14: Settings > General | https://admin.shopify.com/store/capture-advanced/settings/general | "capture advanced · General · Shopify" | 2026-10-04T22:37:45.629Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/014.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/014.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T223401Z-journey-business-entity/014.html.txt`
- quote: To switch your legal entity, contact support to deactivate active Shopify Payments, Balance, and Capital accounts.
- in context: …?] Confirm Cancel Before Country: Not provided Business type: Not provided Name: Not provided After Country: Not provided Business type: Not provided Name: Not provided Changing business type creates a new entity. You'll get multiple tax forms and may need to verify your business. The current entity stays the same. [heading: Switch business details] [accessibilitylabel: Contact Shopify Support (opens in a new tab)] Contact Shopify Support Cancel ⟪To switch your legal entity, contact support to deactivate active Shopify Payments, Balance, and Capital accounts.⟫ [heading: Switch business details] Close You don't have permission to switch business details. Contact your store administrator to request changes. [heading: Confirm store address] Confirm store address Cancel When changing country, you'll receive multiple tax forms and may need to verify your business. This can also affect subscription fees, billing currency, and apps Store address must be in the same country as the business entity Updated stor…

### Q1-SH-K1536

**Cited at:** section 1, line 34

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-063
- placement: decides
- structure: https://www.shopify.com/legal/terms-shopify-payments
- identifier: Part I, A. Your Role
- statement: Your Role. To utilize the Payments Services, you must be a business located in your Designated Country.
- cite_ids: SH-S-0088
- note: first run's citation

**Citation SH-S-0088:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, A. Your Role | 2026-10-10 | kind: official page | quote check: found
- quote: Your Role. To utilize the Payments Services, you must be a business located in your Designated Country.
- title: Shopify Payments Terms of Service - Shopify
- in context: …Cryptocurrency Payment Protocol into a Payment Processor Account, the legal terms of the applicable Payment Processor will apply. Unless you are using another Coinbase product or have separately created an account with Coinbase for this purpose, Coinbase does not provide, and is not responsible for the security of, any cryptocurrency wallet that you use as a Payout Account or otherwise to receive payments via the Cryptocurrency Payment Protocol. ⟪Your Role. To utilize the Payments Services, you must be a business located in your Designated Country.⟫ The Payments Services. Shopify hereby grants you a non-exclusive, non-transferable, non-sublicensable, limited, revocable right to use the Payments Services (the "License"). The License shall be for the term of this Agreement only. Neither the License nor any other provision hereof shall grant any rights in the Payments Services or other intellectual property rights except the limited License of use set out above. You shall not: (i) permit any t…

### Q1-SH-065

**Cited at:** section 1, line 37; section 2, line 77

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-065
- bears_on: 3;5
- identifier: Activate a credit card payment provider
- statement: If Shopify Payments isn't available in your country, then in the Payment providers section, click Choose a provider
- cite_ids: Q1-SH-C065
- from: held

**Citation Q1-SH-C065:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md` | Activate a credit card payment provider, steps (Desktop) | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: If Shopify Payments isn't available in your country, then in the Payment providers section, click Choose a provider
- title: Configuring third-party payment providers
- the page opens: If you're not using Shopify Payments and you want to accept credit cards, then you can choose from over 100 credit card payment providers for your Shopify store. You can activate or change a payment provider from the Payments page of your Shopify admin. Depending on the requirements of the payment provider, you might be required to submit and verify your bank account information with them so that your store can complete transactions. Contact your payment provider to confirm whether or not you ca…
- a note box: Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner.
- a note box: Note Only the store owner can add a payment provider.
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Configuring third-party payment providers > Activate a credit card payment provider {#activate-credit-card-provider} > Steps:
- in context: …add a payment provider. Steps: Desktop From your Shopify admin, go to Settings > Payments. Do one of the following: If you have Shopify Payments active, then in the Shopify payments section, click Manage. At the bottom of the page, click Switch to a third-party provider, and then click Switch to a third-party provider again to confirm. If you don't have Shopify Payments active, then in the Shopify payments section, click See all other providers. ⟪If Shopify Payments isn't available in your country, then in the Payment providers section, click Choose a provider⟫. Select the provider that you want to use from the list. Enter your account credentials for the provider that you selected. Click Activate. Click Save. Mobile From the Shopify app, tap, and then tap Settings. In the Store settings section, tap Payments. Do one of the following: If you have Shopify Payments active, then in the Shopify payments section, tap Manage. At the bottom of the page, tap Switch to a third-party provider, and then tap Switc…  (matched markup removed)

### Q1-SH-K0041

**Cited at:** section 1, line 37; section 2, line 80

**Record** (`studies/proposals/records/Q1/shopify/copied.tsv`):
- concern_id: SH-C-088
- placement: decides
- structure: structures/shopify/admin-router
- identifier: balance:root
- statement: "eligibility":{"oneOf":[{"entitlements":["shopifyFinance.balance"],"regions":["US"]},{"betas":["749e4f05"]},{"entitlements":["shopifyFinance.balance"],"regions":["GB"],"betas":["a2abf0ea"]}]}
- cite_ids: SH-S-5046
- note: section Banking

**Citation SH-S-5046:** `observed-sh@e49840729:structures/shopify/admin-router/items.jsonl` | line 84 (balance:root) | 2026-09-29 | kind: shipped | quote check: found
- quote: "eligibility":{"oneOf":[{"entitlements":["shopifyFinance.balance"],"regions":["US"]},{"betas":["749e4f05"]},{"entitlements":["shopifyFinance.balance"],"regions":["GB"],"betas":["a2abf0ea"]}]}
- in context: …anking","path":"tax-forms/1099-misc","title":{"value":"1099-MISC forms"},"context":["organizationFlags"],"eligibility":{"permissions":["VIEW_TAX_DOCUMENTS"]},"sliceName":"banking-section","sliceId":"S-37ddd7","loader":{"function":true,"imports":["./inactive-merchant.loader-4eadfb0da2cb.js"]},"component":{"function":true,"imports":["./Tax1099MiscForms-71fef8959775.js"]}} {"id":"balance:root","position":0,"array_offset":1475698,"section":"Banking",⟪"eligibility":{"oneOf":[{"entitlements":["shopifyFinance.balance"],"regions":["US"]},{"betas":["749e4f05"]},{"entitlements":["shopifyFinance.balance"],"regions":["GB"],"betas":["a2abf0ea"]}]}⟫,"sliceName":"banking-section","sliceId":"S-37ddd7","icon":"money","loader":{"function":true,"imports":["./BankingSection-loader-689f50d506ac.js"]},"component":{"function":true,"imports":["./BankingSection-78b4a757e5c9.js"]},"errorBoundary":{"function":true,"imports":["./ErrorBoundary-fdab2796e95a.js"]}} {"id":"balance:ensure-terms-of-service","parent":"balance:root","position":0,"array_offset":1476327,"section":"Banking","sliceName":"banking-sec…

### Q1-SH-057

**Cited at:** section 1, line 38; section 2, line 76; section 5, line 122; section 7, line 148

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-057
- bears_on: 3;5
- identifier: Automatic exchange rates
- statement: When you use automatic exchange rates, a currency conversion fee is included in the price displayed to your customer. The fee is either 1.5% or 2%, depending on your store's location.
- cite_ids: Q1-SH-C057
- from: held

**Citation Q1-SH-C057:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md` | Exchange rates with markets > Automatic exchange rates | 2026-10-16 | kind: stated | quote check: found
- quote: When you use automatic exchange rates, a currency conversion fee is included in the price displayed to your customer. The fee is either 1.5% or 2%, depending on your store's location.
- title: Setting up currencies for markets
- the page opens: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency. You can set a specific currency for each market so that your customers can browse, pay, and receive refunds in a currency that's familiar to them. Displaying prices in local currencies improves the customer experience and can help to increase conversion rates in international m…
- a note box: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency.
- a note box: Sidekick You can ask Sidekick which currency a market shows to buyers, whether local currencies and rounding are turned on, and whether its exchange rate is automatic or manual. Use a prompt such as What currency does each of my markets show buyers and are any using manual exchange rates.
- a note box: Caution When using manual exchange rates, you're responsible for keeping rates current. If your manual rate diverges significantly from the actual exchange rate, then you might experience inaccuracies on international orders. Review your manual rates regularly to ensure they reflect current market c
- headings: Setting up currencies for markets > Exchange rates with markets > Automatic exchange rates
- in context: …ets When you sell in local currencies, product prices are converted from your base currency using exchange rates. You can choose between automatic and manual exchange rates, depending on how much control you need over your international pricing. ### Automatic exchange rates With automatic exchange rates, prices are converted using the current market exchange rate. Rates are sourced from financial markets and updated regularly throughout the day. ⟪When you use automatic exchange rates, a currency conversion fee is included in the price displayed to your customer. The fee is either 1.5% or 2%, depending on your store's location.⟫ This fee covers the cost of processing the payment in a different currency than your payout currency. The price displayed to your customer is calculated using the following formula: `Customer price = Base price x Exchange rate x (1 + Conversion fee)` For example, base price for a product in your store is $100.00 USD. The exchange rate to EUR is 0.92, and your store's conversion fee is 1.5%. The following is how your currency conversion is calcul…

### Q1-SH-094

**Cited at:** section 1, line 39

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-094
- bears_on: 3;5
- identifier: PaymentProviders: businessEntity.address.countryCode, businessEntity.paymentSettings
- statement: "businessEntity":{"id":"gid://shopify/BusinessEntity/44100091961","address":{"countryCode":"YE","__typename":"BusinessEntityAddress"},"paymentSettings":{"flexibleGatewaysEligible":true,"thirdPartyDirectEligible":true,"thirdPartyAdditionalPaymentMethodsEligible":true,"__typename":"PaymentSettings"}
- scope: store capture-gb-plus, observed 2026-10-05; "countryCode":"YE","currencyCode":"YER"
- cite_ids: Q1-SH-C207;Q1-SH-C206
- from: held

**Citation Q1-SH-C207:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/PaymentProviders/e31645b940e2be6d5c7608d23f3a9cbe2692a50f0cd88ca4ed0f69363798dd0f.json` | PaymentProviders, store capture-gb-plus, step 6 | 2026-10-05 | kind: observed | quote check: found
- quote: "businessEntity":{"id":"gid://shopify/BusinessEntity/44100091961","address":{"countryCode":"YE","__typename":"BusinessEntityAddress"},"paymentSettings":{"flexibleGatewaysEligible":true,"thirdPartyDirectEligible":true,"thirdPartyAdditionalPaymentMethodsEligible":true,"__typename":"PaymentSettings"}
- in context: …tionMethod"}],"__typename":"PaymentAuthorizationSettings"},"__typename":"QueryRoot","billingAccount":{"id":"gid://shopify/BillingAccount/269465964","currentSubscription":{"id":"gid://shopify/BillingSubscription/0","baseCommissionRate":"0.002","discountCommissionsUntil":null,"__typename":"BillingSubscription"},"__typename":"BillingAccount"},"staffMember":{"id":"gid://shopify/StaffMember/115536527417","isShopOwner":true,"__typename":"StaffMember"},⟪"businessEntity":{"id":"gid://shopify/BusinessEntity/44100091961","address":{"countryCode":"YE","__typename":"BusinessEntityAddress"},"paymentSettings":{"flexibleGatewaysEligible":true,"thirdPartyDirectEligible":true,"thirdPartyAdditionalPaymentMethodsEligible":true,"__typename":"PaymentSettings"}⟫,"shopifyPaymentsAccountNext":null,"amazonPay":{"id":"gid://shopify/PaymentProvider/163","name":"Amazon Pay","eligible":false,"transactionFee":0.2,"configuration":null,"onboardingParams":null,"__typename":"PaymentProvider"},"paypalExpress":{"id":"gid://shopify/PaymentProvider/41","eligible":false,"name":"PayPal Express Checkout","onboardingParams":{"partner_id":"NGL898N6ALUB6","return_url":"https://admin.shopify.com/store/capture-gb-plus/payments…

**Citation Q1-SH-C206:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/PaymentProviders/e31645b940e2be6d5c7608d23f3a9cbe2692a50f0cd88ca4ed0f69363798dd0f.json` | PaymentProviders, store capture-gb-plus, step 6 | 2026-10-05 | kind: observed | quote check: found
- quote: "url":"https://capture-gb-plus.myshopify.com","countryCode":"YE","currencyCode":"YER"
- title, opening and note boxes: as for this source's citation above
- in context: …tectedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":true,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"MANUAL","__typename":"CheckoutSettings"},"__typename":"Shop","name":"capture gb plus","description":null,⟪"url":"https://capture-gb-plus.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/115536527417","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":false,"shopifyPlus":true,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":false,"__typename":"EntitlementsType"},"developmentShop":true,"multiLegalEntitiesPhase":"ELIGIBLE"},"paymentAuthorizationSettings":{"id":"gid…

### Q1-SH-098

**Cited at:** section 1, line 39

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-098
- bears_on: 3
- identifier: ShopifyPaymentsData: businessEntity.shopifyPayments.eligible
- statement: "shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","name":"Shopify Payments","eligible":false,"cardPresentSupported":false
- scope: store capture-gb-plus, observed 2026-10-05; "countryCode":"YE","currencyCode":"YER"
- cite_ids: Q1-SH-C211;Q1-SH-C206
- from: held
- note: the 53 ShopifyPaymentsData answers held across the runs all give "eligible":false (see notes.md)

**Citation Q1-SH-C211:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/ShopifyPaymentsData/e41413f261d39ac4ff99b77ceb00db15d9df7c5fed4c89736e1ea555659d540b.json` | ShopifyPaymentsData, store capture-gb-plus, step 6 | 2026-10-05 | kind: observed | quote check: found
- quote: "shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","name":"Shopify Payments","eligible":false,"cardPresentSupported":false
- in context: {"data":{"businessEntity":{"id":"gid://shopify/BusinessEntity/44100091961",⟪"shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","name":"Shopify Payments","eligible":false,"cardPresentSupported":false⟫,"transactionFee":0.0,"discountedTransactionFee":0.0,"discountedTransactionFeeEndedAt":null,"idVerificationForOnboardingRequired":false,"idVerificationOutcome":null,"missingAttributesInfo":null,"paymentMethods":[{"name":"visa","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"mastercard","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"american_express","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"apple_pay","t…

**Citation Q1-SH-C206:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/PaymentProviders/e31645b940e2be6d5c7608d23f3a9cbe2692a50f0cd88ca4ed0f69363798dd0f.json` | PaymentProviders, store capture-gb-plus, step 6 | 2026-10-05 | kind: observed | quote check: found
- quote: "url":"https://capture-gb-plus.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …tectedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":true,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"MANUAL","__typename":"CheckoutSettings"},"__typename":"Shop","name":"capture gb plus","description":null,⟪"url":"https://capture-gb-plus.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/115536527417","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":false,"shopifyPlus":true,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":false,"__typename":"EntitlementsType"},"developmentShop":true,"multiLegalEntitiesPhase":"ELIGIBLE"},"paymentAuthorizationSettings":{"id":"gid…

### Q1-SH-095

**Cited at:** section 1, line 39; section 6, line 133

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-095
- bears_on: 3;5
- identifier: PaymentProviders: businessEntity.stripe
- statement: "stripe":{"id":"gid://shopify/PaymentProvider/67","available":false,"eligible":false,"configuration":null,"__typename":"PaymentProvider"}
- scope: store capture-gb-plus, observed 2026-10-05; "countryCode":"YE","currencyCode":"YER"
- cite_ids: Q1-SH-C208;Q1-SH-C206
- from: held

**Citation Q1-SH-C208:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/PaymentProviders/e31645b940e2be6d5c7608d23f3a9cbe2692a50f0cd88ca4ed0f69363798dd0f.json` | PaymentProviders, store capture-gb-plus, step 6 | 2026-10-05 | kind: observed | quote check: found
- quote: "stripe":{"id":"gid://shopify/PaymentProvider/67","available":false,"eligible":false,"configuration":null,"__typename":"PaymentProvider"}
- in context: …091816505,"activation_url":"https://app.shopify.com/services/connected_paypal/partner_referral/83091816505?seller_of_record_id=44100091961&uniqueId=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ild6RXhOVFV6TmpVeU56UXhOMTA9IiwiZXhwIjoiMjAyNi0xMC0wNVQwODoyNjozMS41MjNaIiwicHVyIjoiZXhwcmVzc19jaGVja291dCJ9fQ%3D%3D--353ef4364330501d6980631b74676950c409f6b9"},"transactionFee":0.2,"url":"https://www.paypal.com/us/home","configuration":null,"__typename":"PaymentProvider"},⟪"stripe":{"id":"gid://shopify/PaymentProvider/67","available":false,"eligible":false,"configuration":null,"__typename":"PaymentProvider"}⟫,"thirdPartyPaymentProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/24","paypalExpressAvailable":false,"group":"OTHER","thirdPartyCoexistenceCandidate":false,"threeDSecureReady":false,"name":"(for testing) Bogus Gateway","url":"https://help.shopify.com/en/manual/checkout-settings/test-orders","transactionFee":0.0,"apiClientId":null,"canProcessThirdPartyShopPay":false,"paymentMethods":[{"name":"bogus","type":"CREDIT_CARD","__typen…

**Citation Q1-SH-C206:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T002448Z-journey-dev-store-region/answers/admin.shopify.com/PaymentProviders/e31645b940e2be6d5c7608d23f3a9cbe2692a50f0cd88ca4ed0f69363798dd0f.json` | PaymentProviders, store capture-gb-plus, step 6 | 2026-10-05 | kind: observed | quote check: found
- quote: "url":"https://capture-gb-plus.myshopify.com","countryCode":"YE","currencyCode":"YER"
- title, opening and note boxes: as for this source's citation above
- in context: …tectedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":true,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"MANUAL","__typename":"CheckoutSettings"},"__typename":"Shop","name":"capture gb plus","description":null,⟪"url":"https://capture-gb-plus.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/115536527417","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":false,"shopifyPlus":true,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":false,"__typename":"EntitlementsType"},"developmentShop":true,"multiLegalEntitiesPhase":"ELIGIBLE"},"paymentAuthorizationSettings":{"id":"gid…

### Q1-SH-103

**Cited at:** section 1, line 39

**Record** (`studies/proposals/records/Q1/shopify/statements.tsv`):
- stmt_id: Q1-SH-103
- bears_on: 3;5
- identifier: ThirdPartyPaymentProviders: businessEntity.paymentProviders
- statement: "paymentProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/24","name":"(for testing) Bogus Gateway","available":true,"threeDSecureReady":false,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"bogus","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/33325057","name":"Tap Payments","available":true,"threeDSecureReady":true,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"omannet","__typename":"PaymentMethod"},{"name":"apple_pay","__typename":"PaymentMethod"},{"name":"mada","__typename":"PaymentMethod"},{"name":"benefit","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/41156609","name":"ONERWAY (Direct)","available":true,"threeDSecureReady":true,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"visaelectron","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"maestro","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentMethod"}],"configuration":{"id":"gid://shopify/PaymentProviderConfiguration/117617459415","enabled":true,"__typename":"PaymentProviderConfiguration"},"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/44990465","name":"Integration-UseePay","available":true,"threeDSecureReady":true,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentMethod"},{"name":"maestro","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/60358657","name":"PagBrasil - Cartão de crédito","available":true,"threeDSecureReady":false,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"elo","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"hypercard","__typename":"PaymentMethod"},{"name":"hyper","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/84246529","name":"Cybersource","available":true,"threeDSecureReady":true,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentMethod"},{"name":"unionpay","__typename":"PaymentMethod"},{"name":"apple_pay","__typename":"PaymentMethod"},{"name":"google_pay","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"}],"__typename":"PaymentProviderConnection"}
- scope: store fake-demo-sharrwah, observed 2026-10-05; Store address: Sanaa, Yemen
- cite_ids: Q1-SH-C216;Q1-SH-C217;Q1-SH-C218;Q1-SH-C219;Q1-SH-C220;Q1-SH-C221;Q1-SH-C222
- from: held
- note: the list in full, as the answer gives it (6 providers); the page at Settings > Payments > Third-party payment providers lists those not yet set up (step 387)

**Citation Q1-SH-C216:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ThirdPartyPaymentProviders/0eb7c0e0428af37ad4b5099e23dd50df0ad4ad1ac7c2c8a1b0ee476658cc834b.json` | ThirdPartyPaymentProviders, store fake-demo-sharrwah, step 387 | 2026-10-05 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/24","name":"(for testing) Bogus Gateway","available":true,"threeDSecureReady":false
- in context: …data":{"businessEntity":{"id":"gid://shopify/BusinessEntity/47940239575","internalId":"gid://shopify/BusinessEntity/47940239575","paymentSettings":{"flexibleGatewaysEligible":true,"thirdPartyDirectEligible":true,"__typename":"PaymentSettings"},"shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","configuration":null,"__typename":"PaymentProvider"},"paymentProviders":{"edges":[⟪{"node":{"id":"gid://shopify/PaymentProvider/24","name":"(for testing) Bogus Gateway","available":true,"threeDSecureReady":false⟫,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"bogus","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/33325057","name":"Tap Payments","available":true,"threeDSecureReady":true,"onboardingParams":null,"deprecatio…

**Citation Q1-SH-C217:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ThirdPartyPaymentProviders/0eb7c0e0428af37ad4b5099e23dd50df0ad4ad1ac7c2c8a1b0ee476658cc834b.json` | ThirdPartyPaymentProviders, store fake-demo-sharrwah, step 387 | 2026-10-05 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/33325057","name":"Tap Payments","available":true,"threeDSecureReady":true
- title, opening and note boxes: as for this source's citation above
- in context: …ymentProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/24","name":"(for testing) Bogus Gateway","available":true,"threeDSecureReady":false,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"bogus","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/33325057","name":"Tap Payments","available":true,"threeDSecureReady":true⟫,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"omannet","__typename":"PaymentMethod"},{"name":"apple_pay","__typename":"PaymentMethod"},{"name":"mada","__typename":"PaymentMet…

**Citation Q1-SH-C218:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ThirdPartyPaymentProviders/0eb7c0e0428af37ad4b5099e23dd50df0ad4ad1ac7c2c8a1b0ee476658cc834b.json` | ThirdPartyPaymentProviders, store fake-demo-sharrwah, step 387 | 2026-10-05 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/41156609","name":"ONERWAY (Direct)","available":true,"threeDSecureReady":true
- title, opening and note boxes: as for this source's citation above
- in context: …me":"mastercard","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"omannet","__typename":"PaymentMethod"},{"name":"apple_pay","__typename":"PaymentMethod"},{"name":"mada","__typename":"PaymentMethod"},{"name":"benefit","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/41156609","name":"ONERWAY (Direct)","available":true,"threeDSecureReady":true⟫,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"visaelectron","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"maestro","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentM…

**Citation Q1-SH-C219:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ThirdPartyPaymentProviders/0eb7c0e0428af37ad4b5099e23dd50df0ad4ad1ac7c2c8a1b0ee476658cc834b.json` | ThirdPartyPaymentProviders, store fake-demo-sharrwah, step 387 | 2026-10-05 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/44990465","name":"Integration-UseePay","available":true,"threeDSecureReady":true
- title, opening and note boxes: as for this source's citation above
- in context: …name":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentMethod"}],"configuration":{"id":"gid://shopify/PaymentProviderConfiguration/117617459415","enabled":true,"__typename":"PaymentProviderConfiguration"},"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/44990465","name":"Integration-UseePay","available":true,"threeDSecureReady":true⟫,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentM…

**Citation Q1-SH-C220:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ThirdPartyPaymentProviders/0eb7c0e0428af37ad4b5099e23dd50df0ad4ad1ac7c2c8a1b0ee476658cc834b.json` | ThirdPartyPaymentProviders, store fake-demo-sharrwah, step 387 | 2026-10-05 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/60358657","name":"PagBrasil - Cartão de crédito","available":true,"threeDSecureReady":false
- title, opening and note boxes: as for this source's citation above
- in context: …":"mastercard","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentMethod"},{"name":"maestro","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/60358657","name":"PagBrasil - Cartão de crédito","available":true,"threeDSecureReady":false⟫,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"elo","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"hypercard","__typename":"PaymentMethod"},{"name":"hyper","__typename":"PaymentMethod…

**Citation Q1-SH-C221:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ThirdPartyPaymentProviders/0eb7c0e0428af37ad4b5099e23dd50df0ad4ad1ac7c2c8a1b0ee476658cc834b.json` | ThirdPartyPaymentProviders, store fake-demo-sharrwah, step 387 | 2026-10-05 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/84246529","name":"Cybersource","available":true,"threeDSecureReady":true
- title, opening and note boxes: as for this source's citation above
- in context: …:[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"elo","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"hypercard","__typename":"PaymentMethod"},{"name":"hyper","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/84246529","name":"Cybersource","available":true,"threeDSecureReady":true⟫,"onboardingParams":null,"deprecationStatusV2":"undefined","preferred":false,"paymentMethods":[{"name":"visa","__typename":"PaymentMethod"},{"name":"mastercard","__typename":"PaymentMethod"},{"name":"american_express","__typename":"PaymentMethod"},{"name":"diners_club","__typename":"PaymentMethod"},{"name":"discover","__typename":"PaymentMethod"},{"name":"jcb","__typename":"PaymentM…

**Citation Q1-SH-C222:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt` | step 170 (Settings > General) | 2026-10-05 | kind: observed | quote check: found
- step 170: visit route commerce-protection (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: organization-settings:organizations,organization-settings:organization:settings,customer-privacy,setting:legal,settings) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/general | "My Store · General · Shopify" | 2026-10-05T02:57:24.932Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.html`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt`
- quote: Store address Sanaa, Yemen
- in context: …s Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com General General Business details Business entity used for financial products, markets, apps, and taxes in this shop My Store - entity Yemen Store contact details My Store 7amza.it@gmail.com · No phone number ⟪Store address Sanaa, Yemen⟫ Submit Store defaults Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER) Backup Region Yemen [Yemen] Determines settings for customers outside of your markets Unit system Metric system [Metric system] Default weight unit Kilogram (kg) [Kilogram (kg)] Time zone (GMT+03:00) Riyadh [(GMT+03:00) Riyadh] Sets the time for when orders and analytics a…
