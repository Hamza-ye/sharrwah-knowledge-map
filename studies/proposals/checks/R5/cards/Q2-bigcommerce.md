# Cards: Q2 on bigcommerce

15 records cited by `studies/proposals/drafts/Q2/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 8:** - WooCommerce's terms exclude anyone located or residing in a place "subject to comprehensive US sanctions", Crimea, Donetsk and Luhansk among them. BigCommerce's merchant warrants that it, its Relevant Parties and its customers are not nationals or residents of a region "subject to comprehensive U.S. sanctions", and screens them. The two match on the same term; Shopify's list matches theirs by role. Q2-WC-K0526; Q2-BC-K0430; Q2-BC-K0431; Q2-SH-K2275
- **section 1, line 14:** - Shopify activates eligible payment methods "based on the regions where you sell", each local method showing only "when a customer is in a supported country and selects an eligible currency". WooCommerce shows one only "if the customer billing country and the customer currency meet the requirements". BigCommerce's depend on "your store’s country and currency combination". They match by role, all help pages, and differ on whose place counts. Q2-SH-K1745; Q2-SH-K1743; Q2-WC-029; Q2-BC-038
- **section 1, line 16:** - The platforms also choose among providers. Activating Zid Pay turns off the store's other gateway (Zid's terms); Salla's dashboard texts (recorded 8 October 2026) say Salla Payments can't be activated with an active Tap link (not checked on BigCommerce). These match by role. So do Shopify's Transaction Fees on "all payment providers other than Shopify Payments" and BigCommerce's monthly fee for orders through Open Payment Providers. Q2-ZD-K0088; Q2-SA-K1653; Q2-SH-K1337; Q2-BC-K0143
- **section 1, line 22:** - On Shopify, each additional address field's requirement "depends on the customer's country or region and can't be changed" (not checked on BigCommerce). Salla's dashboard texts (recorded 8 October 2026) let a store require the national address of customers in Saudi Arabia, mandatory from الهيئة العامة للنقل, a seller who turns it off bearing the consequences. Zid's seller sets address fields per country. Shopify's privacy settings are set "for each country and region where you sell to", BigCommerce's cookie consent by "a storefront-level setting". Q2-SH-032; Q2-SA-K0800; Q2-SA-K0798; Q2-ZD-022; Q2-SH-K2134; Q2-BC-K0205
- **section 1, line 24:** - Shopify's tax services "depend on the location of your business", and Shopify Tax calculates only for destinations in the United States, the European Union, the United Kingdom or Canada. BigCommerce takes tax engines through its Tax Provider API. Salla's ZATCA link is for stores in Saudi Arabia only. Q2-SH-K1865; Q2-SH-K1867; Q2-BC-K0381; Q2-SA-K1936
- **section 1, line 32:** - Shopify's contracting party is set "based on the billing address of your Store", with a row for all other jurisdictions (Shopify International Limited). Woo services come from WooCommerce Ireland Ltd. for those residing in its "Designated Countries", among them "all countries located in Europe", and from WooCommerce, Inc. for others. BigCommerce's table sets company and law per place, ending "Any other jurisdiction". They match by role, as do Shopify's and BigCommerce's rows for every remaining place. Q2-SH-K1243; Q2-SH-K1248; Q2-WC-K0499; Q2-WC-K0496; Q2-WC-K0498; Q2-BC-K0419; Q2-BC-K0425
- **section 1, line 35:** - Shopify's Terms of Service are governed by the laws of Ontario. The Stripe Services Agreement applies Regional Terms by country, and to countries it doesn't list the United States' Regional Terms in the Americas and Ireland's elsewhere (not checked on Zid). Salla's Arabic text prevails over translations (النص العربي لاتفاقية الاستخدام يظل هو الأصل), BigCommerce's English text: these match by role. Q2-SH-K1253; Q2-WC-055; Q2-SA-030; Q2-BC-015
- **section 1, line 36:** - Each platform names an agreement made directly between the seller and a provider. Shopify "is not a party to any of the Payment Processor Terms"; Stripe's Connected Account Agreement is between the seller and "the applicable Stripe entity"; with BigCommerce Payments "the merchant’s payment relationship remains directly with PayPal" (a press page); Salla calls such dealings "علاقة تعاقدية مستقلة عن منصة سلّة"; Zid is "ليست طرفًا" in logistics agreements. They match by role. Q2-SH-K1580; Q2-WC-P0103; Q2-BC-P0040; Q2-SA-004; Q2-ZD-K0347
- **section 1, line 37:** - Shopify stores new European merchants' data "at rest in Europe by default", its admin showing the Customer data hosting location. BigCommerce makes "regional hosting available", in Europe or the Asia-Pacific region rather than the United States, its primary storage being Google Cloud's U.S.-Central1. They match by role. Q2-SH-K2321; Q2-SH-031; Q2-BC-031; Q2-BC-032
- **section 1, line 38:** - Which Automattic company controls WooCommerce data depends "on the particular service and the location of the individual"; BigCommerce processes shoppers' information as processor, the merchant being controller. Salla's privacy policy is held but not read on storage. Zid may transfer data abroad "if appropriate safeguards are in place"; where it stores data was not in what was read. Q2-WC-K0502; Q2-BC-K0436; Q2-SA-G0218; Q2-ZD-K0283; Q2-ZD-G0060
- **section 2, line 48:** - Everything here is Sharrwah's proposed design, not what a platform does: one mechanism, a **Place rule** on a **Place**, at whatever level the evidence shows things differing. Q2-SH-K2275; Q2-WC-K0496; Q2-BC-K0425
- **section 2, line 50:** - Draws on: areas within a country (Shopify's Crimea, Donetsk and Luhansk; WooPayments' states, Washington D.C. and Puerto Rico), a group (WooCommerce's Designated Countries), and defaults for unlisted places, by row (Shopify's all other jurisdictions; BigCommerce's "Any other jurisdiction") or by region (Stripe's Regional Terms), which the tree's inheritance combines. Q2-SH-K2275; Q2-WC-K0407; Q2-WC-K0496; Q2-SH-K1248; Q2-BC-K0425; Q2-WC-055
- **section 2, line 57:** - **Restricted places**: lists of places where Sharrwah refuses business, each entry with its regime and its effects (opening an account, reaching a storefront, a product's origin, an order's destination, using a service), held per **Contracting entity** and per service. Screening named persons is a step whose doer is set per company. Q2-SH-K2276; Q2-SH-K2279; Q2-ZD-K0254; Q2-BC-K0431
- **section 2, line 59:** - **Contracting entity**: the Sharrwah company a seller contracts with, per **Place** on the **Place reference** its terms choose, and per service (the platform, a payment service, a regulated activity), each row with its governing law, forum and prevailing language. The root's row covers every other place. Q2-SH-K1243; Q2-SH-K1615; Q2-BC-K0419; Q2-BC-K0425
- **section 2, line 60:** - Draws on: Shopify's table by billing address and its Canadian company for regulated payments; BigCommerce's table with law per row; WooCommerce's split by residence; Salla's and Zid's single Saudi company, here a one-row table; the prevailing text (Arabic at Salla, English at BigCommerce). Q2-SH-K1248; Q2-SH-K1615; Q2-BC-K0425; Q2-WC-K0499; Q2-SA-033; Q2-ZD-K0212; Q2-SA-030; Q2-BC-015
- **section 2, line 61:** - Why: rule 3, legal structure is expensive to change, so the table exists from the first build; rule 1, a company for a new place is then set up, not built. Not taken: one company fixed for every place, as Salla's agreement and its en-ae page read. Q2-SA-033; Q2-SA-020; Q2-BC-K0425
- **section 2, line 63:** - Draws on: Shopify's changeable processors per Designated Country; Stripe's entity per account country; availability by the buyer's place and currency (Shopify, WooCommerce), the store's country and currency (BigCommerce) and legal form (WooPayments in the UAE; Zid Pay's KNET); gateways by country (Zid). Why: rule 2, each provider behind its own part; rule 1. Q2-SH-K1563; Q2-SH-K1561; Q2-WC-P0108; Q2-SH-K1743; Q2-BC-038; Q2-WC-K0411; Q2-ZD-K0087
- **section 2, line 64:** - Sharrwah's own choices among providers, one turning another off (Zid Pay; Salla Payments, observed) or a fee on others (Shopify; BigCommerce), are **Place rules** whose source is Sharrwah, set per **Place** (rule 1), so that one can differ where Sharrwah's own service isn't offered: for two stores registered in Yemen, the saved HTML of Shopify's Subscribe to Plus step held its third-party transaction fees beside Shopify Payments being unavailable (30 September and 2 October 2026). Whether to have any is a company decision. Q2-ZD-K0088; Q2-SA-K1653; Q2-SH-K1337; Q2-BC-K0143; Q2-SH-071
- **section 2, line 65:** - **Provider agreement**: the seller's own agreement with a **Provider**, named per **Place**. Sharrwah is not a party by default: Shopify says it isn't party to its processors' terms, and the other four name the seller's agreement as one with the provider. Q2-SH-K1580; Q2-WC-P0103; Q2-BC-P0040; Q2-SA-004; Q2-ZD-K0347
- **section 2, line 71:** - Not taken: leaving legality to the seller alone, as BigCommerce's Highly Regulated Products terms do, since rules Sharrwah knows from providers and places would then not act at sign-up or checkout. Q2-BC-K0460
- **section 2, line 73:** - Draws on: Shopify's address fields by the customer's country, which can't be changed; Salla's national address for customers in Saudi Arabia and Shopify's cookie banner for markets that require it, matching by role as settings the seller may turn off (both observed); Zid's address fields set by the seller per country; privacy settings per country (Shopify) and per storefront (BigCommerce). Why: rule 1. Q2-SH-032; Q2-SA-K0798; Q2-SH-080; Q2-SH-082; Q2-ZD-022; Q2-SH-K2134; Q2-BC-K0205
- **section 2, line 74:** - **Data location**: where a store's data, orders and customers' personal data are held, per **Place** on the seller's **Place reference**, the root's location by default, shown to the seller; with, per place, who is controller and who processor, and the basis for any transfer abroad. Q2-SH-K2321; Q2-SH-031; Q2-BC-031; Q2-BC-K0436
- **section 2, line 75:** - Draws on: Shopify's European storage by default, shown in its admin; BigCommerce's regional hosting and its processor and controller roles; WooCommerce's controller by service and location; Zid's transfers under safeguards. Why: rule 3, where data sits is expensive to change after launch, so data is placeable by region from the first build. Not taken: one fixed location, as Shopify and BigCommerce set it per place. Q2-SH-K2321; Q2-BC-031; Q2-BC-K0436; Q2-WC-K0502; Q2-ZD-K0283
- **section 2, line 79:** - **Tax service**: tax calculation and links to tax authorities as **Providers** per **Place**, on the seller's place or the order's destination. Q2-SH-K1865; Q2-SH-K1867; Q2-BC-K0381; Q2-SA-K1936
- **section 2, line 80:** - Why: rule 2; the rest is left to the build (rule 3). Not taken: one built-in engine for every place, as Shopify Tax's calculations cover only some destinations, and one store's table named three services by region (saved HTML, fake-demo-sharrwah, 30 September 2026). Q2-BC-K0381; Q2-SH-K1867; Q2-SH-078
- **section 3, line 86:** - Plugs in: tax engines (BigCommerce's Tax Provider API), links to a tax authority (Salla's ZATCA link, Saudi stores only), identity checks in a provider's name (Zid Pay's Nafath check), hosting regions (BigCommerce's on Google Cloud), and logistics companies the seller contracts with (Zid). Q2-BC-K0381; Q2-SA-K1936; Q2-ZD-K0263; Q2-BC-032; Q2-ZD-K0347
- **section 3, line 87:** - Set per **Place** at any level, none fixed in advance: an area within a country, a country, a group, and a default for every other place. Q2-SH-K2275; Q2-WC-K0496; Q2-BC-K0425
- **section 3, line 89:** - Set per buyer's place, with the currency: payment methods shown, products shown, address fields required; per store's country and currency together: BigCommerce's local methods. Q2-WC-029; Q2-SH-019; Q2-SH-032; Q2-BC-038
- **section 3, line 94:** - Set by the seller: privacy settings per country and region (Shopify); address fields per country (Zid); turning off the national address at its own risk (Salla) or the cookie banner for an app's (Shopify), both observed; the regions a tax provider serves (BigCommerce); screening its own parties and customers (BigCommerce). Q2-SH-K2134; Q2-ZD-022; Q2-SA-K0798; Q2-SH-082; Q2-BC-K0386; Q2-BC-K0431
- **section 5, line 113:** - Which sanctions regimes bind Sharrwah, on which lists, and who screens. Keep **Restricted places** per company and per service, and screening as a step whose doer is set. Settled by where the company is based and which banks and providers it uses. Of Zid Pay's two open-ended lists, only the Kuwaiti one names اليمن. Q2-ZD-K0254; Q2-ZD-K0252; Q2-BC-K0431; Q2-ZD-G0055
- **section 5, line 115:** - Where a seller's data is held, and on what basis it moves. Keep **Data location** settable per place. Settled by the company decision on hosting. Q2-SH-K2321; Q2-BC-031
- **section 7, line 136:** - Where Sharrwah's company is based, and which company contracts with sellers at each place, under which law, forum and prevailing language. Q2-SH-K1243; Q2-BC-K0419; Q2-SA-020; Q2-ZD-K0212; Q2-SA-030
- **section 7, line 137:** - Which sanctions regimes Sharrwah applies, to whom (the seller, its owners, its buyers), at which points, and who screens. Q2-SH-K2268; Q2-WC-K0526; Q2-ZD-K0254; Q2-BC-K0431
- **section 7, line 139:** - Whether Sharrwah is a party to sellers' payment arrangements or only connects sellers to providers; whether any holds sellers' money through Sharrwah is the founder's decision. Q2-SH-K1603; Q2-BC-P0040
- **section 7, line 142:** - Where sellers' and buyers' data is hosted at each place, and whether Sharrwah is its processor or its controller. Q2-SH-K2321; Q2-BC-K0436; Q2-WC-K0502

## The cards

### Q2-BC-K0430

**Cited at:** section 1, line 8

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-080
- placement: responsible
- structure: Master Services Agreement
- identifier: Sanctions List
- statement: are not, and will ensure that your Relevant Parties and customers are not, (a) nationals, residents, agents or representatives of Iran, Cuba, North Korea, Syria, the Crimea Region of Ukraine, or any other region subject to comprehensive U.S. sanctions
- cite_ids: BC-S-0437

**Citation BC-S-0437:** `https://www.commerce.com/terms/` | Anti-Corruption, Export and Sanctions Compliance | 2026-06-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` (fetched 2026-10-12T04:20:53Z, captured)
- quote: are not, and will ensure that your Relevant Parties and customers are not, (a) nationals, residents, agents or representatives of Iran, Cuba, North Korea, Syria, the Crimea Region of Ukraine, or any other region subject to comprehensive U.S. sanctions
- title: Master Services Agreement | Commerce
- in context: …in, retain, or direct regulatory approvals, licenses, permits, business, contracts, investments, sales, tax or duty assessments, import or export clearances, foreign exchange clearances, or other advantages; shall cause all of your employees, officers, directors, agents, contractors, vendors, and partners (collectively, "Relevant Parties") to comply with all of the terms contained in this Anti-Corruption, Export and Sanctions Compliance Section; ⟪are not, and will ensure that your Relevant Parties and customers are not, (a) nationals, residents, agents or representatives of Iran, Cuba, North Korea, Syria, the Crimea Region of Ukraine, or any other region subject to comprehensive U.S. sanctions⟫; (b) on the List of Specially Designated Nationals & Blocked Persons, the Sectoral Sanctions Identifications (SSI) List, or Foreign Sanctions Evaders List maintained by the Office of Foreign Assets Control of the U.S. Department of the Treasury, or any other applicable list of sanctioned, embargoed, blocked, criminal, or debarred persons maintained by any U.S. or non-U.S. government, the European Union, Interpol, the United Nations, the World Ba…

### Q2-BC-K0431

**Cited at:** section 1, line 8; section 2, line 57; section 3, line 94; section 5, line 113; section 7, line 137

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-080
- placement: responsible
- structure: Master Services Agreement
- identifier: sanctions screenings
- statement: shall implement an effective, risk-based compliance program and necessary internal controls (including, but not limited to, conducting sanctions screenings of your Relevant Parties and customers)
- cite_ids: BC-S-0438

**Citation BC-S-0438:** `https://www.commerce.com/terms/` | Anti-Corruption, Export and Sanctions Compliance | 2026-06-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` (fetched 2026-10-12T04:20:53Z, captured)
- quote: shall implement an effective, risk-based compliance program and necessary internal controls (including, but not limited to, conducting sanctions screenings of your Relevant Parties and customers)
- title: Master Services Agreement | Commerce
- in context: …rtue of such person being a director or owning voting shares or interests), or acts, directly or indirectly, for or on behalf of, any person or entity on a Sanctions List; or (d) otherwise the target of any sanctions, suspensions, embargoes or debarment by the U.S. government or any other government or public international organization; shall secure all necessary export/sanctions licenses or authorizations to the extent applicable and necessary; ⟪shall implement an effective, risk-based compliance program and necessary internal controls (including, but not limited to, conducting sanctions screenings of your Relevant Parties and customers)⟫ to ensure compliance with Applicable ABAC Laws and this Anti-Corruption, Export and Sanctions Compliance Section; shall review and adhere to Commerce's Company Associate Compliance Guide if provided by Commerce; and shall reasonably cooperate with Commerce to (a) ensure compliance with sanctions, embargoes, and other Applicable ABAC Laws and/or (b) review and remediate actual or potential violations of sanctions or other Applicable ABAC Laws, in…

### Q2-BC-038

**Cited at:** section 1, line 14; section 2, line 63; section 3, line 89

**Record** (`studies/proposals/records/Q2/bigcommerce/statements.tsv`):
- stmt_id: Q2-BC-038
- bears_on: 1
- identifier: Local Payment Methods
- statement: Note that availability for local payment methods depend on your store’s country and currency combination.
- cite_ids: Q2-BC-C042
- from: held

**Citation Q2-BC-C042:** `https://support.bigcommerce.com/s/article/Connecting-with-BigCommerce-Payments?language=en_US` | Payment Methods: Local Payment Methods | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/016-support.bigcommerce.com/text.txt` (fetched 2026-10-13T00:35:36Z, captured)
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:39:50Z, captured)
- quote: Note that availability for local payment methods depend on your store’s country and currency combination.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …ay Later. * Before accepting payments, you must confirm your BigCommerce Payments account in the Actions section. † Alternative payment method transactions are Authorize and capture only, regardless of the selected Transaction type. Delayed capture is not supported. LOCAL PAYMENT METHODS Under Payment Methods, the Local Payment Methods section allows you to manage additional payment methods; letting eligible shoppers pay in their local currency. ⟪Note that availability for local payment methods depend on your store's country and currency combination.⟫ Before accepting payments, you must confirm your BigCommerce Payments account in the Actions section. Alternative payment method transactions are Authorize and capture only, regardless of the selected Transaction type. Delayed capture is not supported. Stored payment methods and recurring payments are not supported. Bancontact - Check to accept Bancontact payments. BLIK - Check to accept BLIK payments. EPS - Check to accept EPS (Electronic Payme…

### Q2-BC-K0143

**Cited at:** section 1, line 16; section 2, line 64

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-026
- placement: decides
- structure: Pricing page (raw HTML)
- identifier: Open Payment Provider Fee
- statement: BigCommerce charges a monthly fee on self-service plans (Core, Growth, and Scale) for orders processed through Open Payment Providers.
- cite_ids: BC-S-0154

**Citation BC-S-0154:** `https://www.bigcommerce.com/pricing/` | How the Open Payment Provider Fee Works | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/102-bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:51Z, captured)
- quote: BigCommerce charges a monthly fee on self-service plans (Core, Growth, and Scale) for orders processed through Open Payment Providers.
- title: BigCommerce Pricing and Plan Information | BigCommerce
- in context: …Embedded Payment Providers listed are not subject to any additional order fees. Any payment provider not on this list is considered an Open Payment Provider and is subject to the fee. *This list reflects our current Embedded Payment Provider program and may change over time. Any updates apply to future orders only; they won't affect charges already billed. Learn more about reducing or eliminating this fee. How the Open Payment Provider Fee Works ⟪BigCommerce charges a monthly fee on self-service plans (Core, Growth, and Scale) for orders processed through Open Payment Providers.⟫ This fee is billed by BigCommerce directly to you, not your shoppers, and appears as a separate line item on your monthly invoice. It's separate from any fees your payment provider charges. Fee Rates by Plan Each order is attributed to the payment provider that processes it. For example, if an Embedded Payment Provider processes the order, no fee applies to that transaction. If all orders are processed through Embedded Payment Providers, your fe…

### Q2-BC-K0205

**Cited at:** section 1, line 22; section 2, line 73

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-037
- placement: decides
- structure: Developer docs: Catalyst Cookie Consent
- identifier: Security Settings
- statement: Cookie consent is controlled by a storefront-level setting in the BigCommerce control panel.
- scope: Catalyst storefronts
- cite_ids: BC-S-0216

**Citation BC-S-0216:** `https://docs.bigcommerce.com/developer/docs/storefront/catalyst/features/cookie-consent.md` | ## Enable cookie consent | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/094-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:49Z, captured)
- quote: Cookie consent is controlled by a storefront-level setting in the BigCommerce control panel.
- title: Cookie Consent
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. > How Catalyst's built-in cookie consent manager, powered by c15t, gates Script Manager scripts by consent category, and how to choose a consent storage mode. Catalyst includes a built-in cookie conse…
- headings: Cookie Consent > Enable cookie consent
- in context: …** > > This documentation describes how Catalyst's cookie consent tools work. It is not legal advice. Store owners are solely responsible for ensuring their storefront complies with all applicable privacy laws - including GDPR, CCPA, and any other regulations in the jurisdictions where they operate. We recommend consulting qualified legal counsel to confirm your implementation meets your specific compliance requirements. ## Enable cookie consent ⟪Cookie consent is controlled by a storefront-level setting in the BigCommerce control panel.⟫ 1. Open [Security Settings](https://login.bigcommerce.com/deep-links/manage/settings/security) in the control panel. 2. Scroll to **Your customers' privacy**. 3. Enable **Cookie consent tracking**. When enabled, Catalyst displays the consent banner to shoppers who have not yet made a selection. When disabled, no banner is shown and all scripts load unconditionally. ### Add a privacy policy link If your store has a privacy policy page, you can su…

### Q2-BC-K0381

**Cited at:** section 1, line 24; section 2, line 79; section 2, line 80; section 3, line 86

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-073
- placement: where
- structure: API reference group: /developer/api-reference/rest/integrations/tax-provider
- identifier: /developer/api-reference/rest/integrations/tax-provider
- statement: Use BigCommerce’s platform-to-platform Tax Provider API to integrate a tax calculation engine into the BigCommerce storefront and control panel.
- cite_ids: BC-S-0388

**Citation BC-S-0388:** `https://docs.bigcommerce.com/developer/api-reference/rest/integrations/tax-provider.md` | page introduction | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/060-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:15Z, captured)
- quote: Use BigCommerce’s platform-to-platform Tax Provider API to integrate a tax calculation engine into the BigCommerce storefront and control panel.
- title: Tax Provider API
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. Use BigCommerce's platform-to-platform Tax Provider API to integrate a tax calculation engine into the BigCommerce storefront and control panel. Supports estimate, adjust, commit, and void operations.…
- headings: Tax Provider API
- in context: > This page is for Developer. > For clean Markdown of any page, append .md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. # Tax Provider API ⟪Use BigCommerce's platform-to-platform Tax Provider API to integrate a tax calculation engine into the BigCommerce storefront and control panel.⟫ Supports [estimate](/developer/api-reference/rest/integrations/tax-provider/estimate-taxes), [adjust](/developer/api-reference/rest/integrations/tax-provider/adjust-tax-quote), [commit](/developer/api-reference/rest/integrations/tax-provider/commit-tax-quote), and [void](/developer/api-reference/rest/integrations/tax-provider/void-tax-quote) operations. For more information, see [Tax Provider API Overview](/developer/docs/integrations/tax-provid…

### Q2-BC-K0419

**Cited at:** section 1, line 32; section 2, line 59; section 7, line 136

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-079
- placement: decides
- structure: Master Services Agreement
- identifier: Governing Law; Jurisdiction
- statement: The law that will govern the validity and construction of this Agreement and apply in any dispute or lawsuit arising out of or relating to this Agreement is as set forth in table in the Contracting Entity Section above.
- cite_ids: BC-S-0426

**Citation BC-S-0426:** `https://www.commerce.com/terms/` | Governing Law; Jurisdiction | 2026-06-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` (fetched 2026-10-12T04:20:53Z, captured)
- quote: The law that will govern the validity and construction of this Agreement and apply in any dispute or lawsuit arising out of or relating to this Agreement is as set forth in table in the Contracting Entity Section above.
- title: Master Services Agreement | Commerce
- in context: …ED BY APPLICABLE LAW, COMMERCE WILL HAVE NO LIABILITY FOR ANY HARM OR DAMAGE ARISING OUT OF OR IN CONNECTION WITH ANY PRE-RELEASEPRODUCT. Customer's rights with respect to a PRE-RELEASE Services terminate upon the earliest of: (i) commercial release of a generally available version, (ii) end of any applicable subscription term in an Order or otherwise noted by Commerce, or (iii) notice by either party. Miscellaneous. Governing Law; Jurisdiction. ⟪The law that will govern the validity and construction of this Agreement and apply in any dispute or lawsuit arising out of or relating to this Agreement is as set forth in table in the Contracting Entity Section above.⟫ YOU HEREBY CONSENT TO, AND WAIVE ALL DEFENSES OF LACK OF PERSONAL JURISDICTION AND FORUM NON CONVENIENS WITH RESPECT TO, THE JURISDICTION AND VENUE OF THE FEDERAL AND STATE COURTS LOCATED IN TRAVIS COUNTY, TEXAS (USA). The prevailing party in any dispute arising out of this Agreement shall be entitled to recover its reasonable attorney's fees and costs, in addition to any other relief granted. The United Nations Convention on Contracts for the I…

### Q2-BC-K0425

**Cited at:** section 1, line 32; section 2, line 48; section 2, line 50; section 2, line 59; section 2, line 60; section 2, line 61; section 3, line 87

**The same record as Q1-BC-K0425,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Any other jurisdiction Commerce.com Pty. Ltd., an Australia proprietary limited company New York Ecommerce Platform, Extensions, and certain Professional Services
- scope: Country of Residence of Merchant: Any other jurisdiction

### Q2-BC-015

**Cited at:** section 1, line 35; section 2, line 60

**Record** (`studies/proposals/records/Q2/bigcommerce/statements.tsv`):
- stmt_id: Q2-BC-015
- bears_on: 1;2
- identifier: Language
- statement: Language. This Agreement has been prepared in the English language. In the event of any conflict or inconsistency between the English language version of this Agreement and any translation thereof, the English language version shall prevail.
- cite_ids: Q2-BC-C017
- from: held

**Citation Q2-BC-C017:** `https://www.commerce.com/terms/` | Miscellaneous: Language | 2026-06-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` (fetched 2026-10-12T04:20:53Z, captured)
- quote: Language. This Agreement has been prepared in the English language. In the event of any conflict or inconsistency between the English language version of this Agreement and any translation thereof, the English language version shall prevail.
- title: Master Services Agreement | Commerce
- in context: …CONVENIENS WITH RESPECT TO, THE JURISDICTION AND VENUE OF THE FEDERAL AND STATE COURTS LOCATED IN TRAVIS COUNTY, TEXAS (USA). The prevailing party in any dispute arising out of this Agreement shall be entitled to recover its reasonable attorney's fees and costs, in addition to any other relief granted. The United Nations Convention on Contracts for the International Sale of Goods will not apply to this Agreement and is hereby expressly excluded. ⟪Language. This Agreement has been prepared in the English language. In the event of any conflict or inconsistency between the English language version of this Agreement and any translation thereof, the English language version shall prevail.⟫ Severability. If any provision of this Agreement is found to be unenforceable or invalid, that provision will be limited or eliminated to the minimum extent necessary so that the Agreement will otherwise remain in full force and effect and enforceable. Waiver. No waiver of any provision of this Agreement, nor consent by Commerce to the breach of or departure from any provision of this Agreement, will in any event be binding on or effective again…

### Q2-BC-P0040

**Cited at:** section 1, line 36; section 2, line 65; section 7, line 139

**Record** (`studies/proposals/records/Q2/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-039
- bullet: b
- placement: responsible
- identifier: BigCommerce Payments: the merchant’s payment relationship
- statement: While BigCommerce Payments is co-branded and embedded into BigCommerce, the merchant’s payment relationship remains directly with PayPal.
- cite_ids: S01-BC-C047
- from: new
- note: Press release dated October 20, 2025, announcing BigCommerce Payments before its launch.

**Citation S01-BC-C047:** `https://www.commerce.com/press/bigcommerce-payments-powered-by-paypal/` | paragraph beginning "The BigCommerce Payments architecture" | 2025-10-20 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/012-commerce.com/text.txt` (fetched 2026-10-13T00:35:31Z, captured)
- quote: While BigCommerce Payments is co-branded and embedded into BigCommerce, the merchant’s payment relationship remains directly with PayPal.
- title: Commerce Introduces BigCommerce Payments Powered by PayPal
- in context: …them to seize the future with confidence and agility," said Michelle Gill, Executive Vice President and General Manager, Small Business & Financial Services, PayPal. "By bringing together PayPal's world-renowned reliability, security and global reach with Commerce's merchant-focused platform, we're helping merchants thrive in the next era of ecommerce." The BigCommerce Payments architecture is built to ensure transparency and merchant ownership. ⟪While BigCommerce Payments is co-branded and embedded into BigCommerce, the merchant's payment relationship remains directly with PayPal.⟫ BigCommerce Payments will introduce a dedicated "Money" dashboard within the BigCommerce Control Panel, offering merchants direct access to manage and monitor their payments and balance activity. Features include: Real-time balance insights Top-ups and payouts Bank and card connections Currency management This embedded experience will mirror key capabilities of the merchant's PayPal dashboard, providing a streamlined experience where merchants c…

### Q2-BC-031

**Cited at:** section 1, line 37; section 2, line 74; section 2, line 75; section 5, line 115

**Record** (`studies/proposals/records/Q2/bigcommerce/statements.tsv`):
- stmt_id: Q2-BC-031
- bears_on: 2
- identifier: regional hosting
- statement: Commerce makes regional hosting available for merchants interested in hosting their stores in Europe or the Asia-Pacific (APAC) region rather than in the United States.
- cite_ids: Q2-BC-C034
- from: held
- note: with Q2-BC-032, closes Q2-BC-G0154

**Citation Q2-BC-C034:** `sharrwah-knowledge-map@98f560e89dc72be24b539513a8a7e59f19d096b8:evidence/product-class/blocked-evidence-founder/bigcommerce/Commerce's Trust Center documentation/Commerce & International Data Transfers Whitepaper (9.16.2025).pdf` | Optional Additional Measures You Can Take to Minimise Data Transfer Concerns | 2025-09 | kind: stated | quote check: found
- quote: Commerce makes regional hosting available for merchants interested in hosting their stores in Europe or the Asia-Pacific (APAC) region rather than in the United States.
- in context: …sational security measures (if data might be exported from the EU).2 Where practical, we may execute the SCCs even with adequate jurisdictions so that transfers remain valid if adequacy changes. Our ISMS and PIMS require security and privacy reviews of all subprocessors both prior to onboarding and at regular intervals thereafter. Optional Additional Measures You Can Take to Minimise Data Transfer Concerns As described further in the FAQs below, ⟪Commerce makes regional hosting available for merchants interested in hosting their stores in Europe or the Asia-Pacific (APAC) region rather than in the United States.⟫ The Commerce platform also provides merchants with latitude and functionality to control the personal data that their store collects, uses, and retains. For merchants that are particularly concerned about data transfers, the Commerce platform allows merchants to ask shoppers for their consent to process data overseas.3 Though uncommon as of the 2 Commerce may use similar or related data transfer mechanisms, such as the UK International Data Tran…

### Q2-BC-032

**Cited at:** section 1, line 37; section 3, line 86

**Record** (`studies/proposals/records/Q2/bigcommerce/statements.tsv`):
- stmt_id: Q2-BC-032
- bears_on: 2
- identifier: Where is my data stored and processed?
- statement: Commerce primarily utilizes Google Cloud’s U.S.-Central1 region as our primary data storage location, with additional locations hosted on Google Cloud’s Europe-West3 and Australia-SE1 regions.
- cite_ids: Q2-BC-C035
- from: held
- note: with Q2-BC-031, closes Q2-BC-G0154

**Citation Q2-BC-C035:** `sharrwah-knowledge-map@98f560e89dc72be24b539513a8a7e59f19d096b8:evidence/product-class/blocked-evidence-founder/bigcommerce/Commerce's Trust Center documentation/Commerce & International Data Transfers Whitepaper (9.16.2025).pdf` | FAQs: Where is my data stored and processed? | 2025-09 | kind: stated | quote check: found
- quote: Commerce primarily utilizes Google Cloud’s U.S.-Central1 region as our primary data storage location, with additional locations hosted on Google Cloud’s Europe-West3 and Australia-SE1 regions.
- in context: …ls, and resources may be available via third parties in the app marketplace. You can find more information here about the storefront cookies necessary for the Commerce platform to function properly. Merchants can independently choose whether to use additional custom or third-party cookies, scripts, applications, integrations, etc., to support their own marketing or other commercial interests and activities. Where is my data stored and processed? ⟪Commerce primarily utilizes Google Cloud's U.S.-Central1 region as our primary data storage location, with additional locations hosted on Google Cloud's Europe-West3 and Australia-SE1 regions.⟫ Across each region, our infrastructure is replicated throughout multiple availability zones to promote resilience. See our Third Party Suprocessor page for more information about our subprocessors and where your data is stored or processed. 8 Commerce has registered with the Association of National Advertisers (ANA) to provide independent third-party dispute resolution at no cost to the complaining party. You can contact ANA and/or learn more ab…

### Q2-BC-K0436

**Cited at:** section 1, line 38; section 2, line 74; section 2, line 75; section 7, line 142

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-081
- placement: responsible
- structure: Privacy Policy
- identifier: Shoppers
- statement: We use this information as a Processor to provide our services to Merchants, support and Process orders, and manage risk and fraud. The Merchant is the Controller of this information
- cite_ids: BC-S-0443

**Citation BC-S-0443:** `https://www.commerce.com/privacy/` | Shoppers: Information Usage | 2026-01-28 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/105-commerce.com/text.txt` (fetched 2026-10-12T04:20:50Z, captured)
- quote: We use this information as a Processor to provide our services to Merchants, support and Process orders, and manage risk and fraud. The Merchant is the Controller of this information
- title: Privacy Policy | Commerce
- in context: …tionality we do not control. We may share Contact Information within Commerce. We may also share information as identified in Section 8 below. Shoppers. Information Collected. When Shoppers interact with a Merchant's ecommerce offering through the Commerce.com platform, we may collect and Process Contact Information, Browser Information, Security Information and Transaction Information of the Shopper on behalf of the Merchant. Information Usage. ⟪We use this information as a Processor to provide our services to Merchants, support and Process orders, and manage risk and fraud. The Merchant is the Controller of this information⟫ and Shoppers who have questions about our use of this information should contact the Merchant. We may also use certain information as a Controller to improve and personalize our services, and manage risk and fraud. Merchant Privacy Policies. Merchants are responsible to provide their Shoppers: • required privacy notices and policies outlining their privacy practices and how the Merchant, Commerce.com and relevant third parties collect and Proces…

### Q2-BC-K0460

**Cited at:** section 2, line 71

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-085
- placement: responsible
- structure: Acceptable Use Policy
- identifier: Disclaimer
- statement: Commerce disclaims any responsibility for evaluating or confirming the legality of your products or services. You are solely responsible for ensuring that your products comply with applicable laws.
- cite_ids: BC-S-0467

**Citation BC-S-0467:** `https://www.commerce.com/terms/acceptable-use-policy/` | Highly Regulated Products: Disclaimer | 2025-07-31 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/109-commerce.com/text.txt` (fetched 2026-10-12T04:20:54Z, captured)
- quote: Commerce disclaims any responsibility for evaluating or confirming the legality of your products or services. You are solely responsible for ensuring that your products comply with applicable laws.
- title: Acceptable Use Policy | Commerce
- in context: …sibility to verify compliance with all applicable laws. Indemnification. You agree to indemnify and hold harmless Commerce and its affiliates from any claims, losses, damages, liabilities, or costs (including reasonable attorneys' fees) arising from your breach of this Section 2 or related representations, including claims involving product liability, regulatory violations, or other legal claims relating to your products or services. Disclaimer. ⟪Commerce disclaims any responsibility for evaluating or confirming the legality of your products or services. You are solely responsible for ensuring that your products comply with applicable laws.⟫ Commerce shall not be liable for any damages, losses, or liabilities related to regulatory changes or third-party service provider policies affecting regulated products or services. Inapplicability of Damage Exclusions and Limitation of Liability. The limitation of liability provisions outlined in the Agreement do not apply to your breach of the Representations and Warranties section or your Indemnification obligations under this Acceptable Use …

### Q2-BC-K0386

**Cited at:** section 3, line 94

**Record** (`studies/proposals/records/Q2/bigcommerce/copied.tsv`):
- concern_id: BC-C-073
- placement: decides
- structure: Developer docs: Tax Providers
- identifier: Settings > Setup > Tax
- statement: Before you can provide tax estimates, the merchant must choose which regions they want you to service.
- cite_ids: BC-S-0393

**Citation BC-S-0393:** `https://docs.bigcommerce.com/developer/docs/integrations/tax-providers.md` | ## Configure tax provider settings in the control panel | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/085-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:40Z, captured)
- quote: Before you can provide tax estimates, the merchant must choose which regions they want you to service.
- title: Tax Providers
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. The Tax Provider API allows you to provide business-to-consumer sales tax estimates to shoppers on the storefront and to merchants in the control panel; it can also be used to submit documents for tax…
- headings: Tax Providers > Configure tax provider settings in the control panel
- in context: …ished a connection, merchants can adjust their tax provider settings to activate supported functions on their store. Merchants can adjust these settings by navigating to **Settings > Setup > Tax > *TaxProviderName*** in the control panel. > **Note** > > Is your tax provider not visible in the control panel? Ensure that you have sent the update connection request as described in the [establishing a connection](#establishing-a-connection) section. ⟪Before you can provide tax estimates, the merchant must choose which regions they want you to service.⟫ The control panel displays a list of countries and subdivisions that you support. If you support document submission, the merchant can choose to select the **Submit Order Data** checkbox. This allows merchants to submit tax documents for supported transactions on their store. ## Verifying your integration To help verify your integration we offer a test connection function in the control panel. This function will trigger a request to the tax prov…
