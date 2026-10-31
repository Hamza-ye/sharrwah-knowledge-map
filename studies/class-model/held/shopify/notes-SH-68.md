# Held pass, Shopify, batch SH-68: notes

130 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl` (one row per page; the entries' locators give its line and pointer). Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-68`).
- 1 to 18: the international pricing page of www.shopify.com/ae-ar (items.jsonl line 1): its terms entry, the hero, the fee table and its two FAQs;
- 19 to 130: the ae-ar plans page (line 2): its terms entry, the hero, the four plan cards and their features, the always-included block, the POS Pro and Agentic cards, two figures, and the comparison table to its row 66 (Assign local domains). SH-69 begins at row 67.

**No batch had placed this structure before this one.** SH-69 to SH-79 hold the rest of it and haven't run. The rules below are written for them: each kind of line is decided once, here, from its first entries and the pages' own data.

**Placed:** 130 entries in 170 lines: 122 entries on capabilities, 4 `new` (one new thing), 4 `out`; 31 entries take more than one line. Supports: 146 `core`, 20 `shows`; no `own-service`, `extension-point` or `outside`. One filler line (ChatGPT; Gemini, the venues of Sell in AI chats). 63 lines carry qualities.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` (it lists nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv` rows 141 (this structure), 40 and 129 (the 30 September pricing page the concern map read); the ledger `index/ledger/sitemap--shopify-com-sitemaps.tsv` (every read site's /pricing pages captured by run 20261031T003815Z-shopify-com-pricing-by-country); `selection.tsv`'s row; `show --meta`; `meta.json`'s source;
- items.jsonl lines 1 to 3 (the three ae-ar pages) whole, and every read site's three pages for the measurement of R0 (by `uri`);
- the model: `caps --terms` with the English twins' headings, `cells`, `land_points.py cell` for CM-PLN-001, CM-TAX-008 and the plan rows' citations (which cell cites which of the 30 September table's rows, SH-S-7001 to SH-S-7079);
- SA-3's notes and placements, the precedent for a plans page (Salla's `com-plans`).

The English words I give for Arabic lines are their twins' on the English sites (items.jsonl), read to clarify only; every line's terms and quotes are the Arabic entry's own.

## Rules my lines follow, for SH-69 to SH-79

### R0. How an entry's sites become its scope (the brief's known case)

1. **Plans first, then sites.** A line's scope is the plans it is stated for, in the page's words (Basic, Grow, Advanced, Plus; Agentic; POS Pro; on the POS page Starter and Retail), then its sites, all `;`-separated: `Basic;Grow;Advanced;Plus;www.shopify.com/ae-ar`.
2. **The sites, read by language.** An entry is one set of words, so its labels can only be sites of its language: the 18 English-language sites state English words; the three Arabic sites (www.shopify.com/ae-ar, www.shopify.com/eg, www.shopify.com/sa) state Arabic words. A line in neither language (the plan names alone, SH-E-907c9d89) is read against all 21.
   - **A line whose labels are every read site of its language takes no site in scope.** This is a reading of the brief's 'A line that every read site of its page states takes no scope': read literally, no Arabic or English line could ever take none. I measured it (point 3): such a line's twin is stated, with the same values, on every site of the other language. So every read site states it, each in its own language.
   - **Five such lines keep their labels,** since their twin is missing from some sites or states other values there:
     - SH-E-10989871 (22): Basic's 'sell online, in person and in AI chats'. The www.shopify.com/ie and www.shopify.com/pk cards have no such feature.
     - SH-E-3add0529 (51): the always-included block. On www.shopify.com, au, ca, ie, sg and uk, its fourth card is on in-person sales, not support.
     - SH-E-2d8f8c4c (68): Earn 1% back. The maximums differ by site.
     - SH-E-ff61aa7e (87): the POS Pro row. The prices differ by site, and www.shopify.com's Plus cell adds 'Up to 200 with Shopify Payments'.
     - SH-E-e4bfb392 (SH-69's 28): the Shopify Capital footnote. www.shopify.com, au, ca, ie and uk state other words.
   - **SH-E-725fcc54 (118) takes no site.** Its English twin states the same fee on all 18 sites: 11 write '$99/mo' and 7 write '$99 USD/mo'.
   - **Every other line takes its labels,** after its plans: a line that only some sites of its language state is stated for those sites. This keeps lines that differ only by a link to the site's own page as separate lines, each with its own sites. An example is the fee table's Shopify Payments row, which links /ae-ar/pricing, /eg/pricing or /sa/pricing (5; SH-79's sa line). So does a currency code written out. A line's absence from a site is not a statement (the brief): the scope says where the line is stated, never where it isn't.
   - **A page's terms entry always takes its labels** (R1): its prices are the sites'.
3. **The measurement,** for the coordinator. My scratch scripts compared each line with its twin on every read site.
   - **What a twin is:** the same element on the other site's page of the same kind:
     - a plan card by its `planType`;
     - a card feature by its `planType` and `name`;
     - a comparison row by its place in the table. ae-ar's 84 rows align with www.shopify.com/ae's, and eg's and sa's 76 with the 76-row English sites' (www.shopify.com/in among them), row for row with the same cells. Those 76 rows are the ones all 18 English sites hold.
     - any other item by its path, since the POS and international pages have one shape on every read site.
   - **When a twin is the same:** where it states the same numbers. Numbers written in words in one language don't count as a difference: 24/7, 3rd, 1000s, '1- or 3-year', 'Level 1'.
   - **The result:** of the structure's 1,056 entries, 362 lines (terms entries aside) are on every read site of their language: 178 English, 184 Arabic. 357 take no site; 5 keep their labels (above). The 178 English lines' Arabic twins are each one line, the same on the three Arabic sites.
   - **What it doesn't test:** words against their translation, beyond numbers and presence.

### R1. A page's terms entry (`loaderData.*.pricing`, with `enPath` and `experimentVariationId`)

One per page, or per set of pages with the same text. `enPath` names the page (/pricing, /pos/pricing, /international/pricing). `experimentVariationId` is the variant it was served. `pricing` holds the site's terms, the same object on its three pages but for `signupTypes`.

Three lines, each `core`, the labels as scope, the keys as terms:
- **CM-PLN-001:** `basicAnnualPrice`, `minimumMonthlyPrice` (with its currency), `paidTrialAmount`, `paidTrialMonths` and `trialLength` as qualities, written `key: value`;
- **CM-PLN-002:** `annualDiscountPercentage`, the yearly billing period's discount;
- **CM-POS-001:** `posProPriceUsd` and `posRetailLocations`. The POS page uses the latter as 'more than 1,000 locations', which clarifies it only.

`promoAmount` repeats the paid trial. The reading names the page, quotes `experimentVariationId` whole and `signupTypes`. `googleCountryOffer` is named for Google, but no held text of the pages uses it, so it gives no line (notes, below). It is `core` as the cell holds the plan table's price rows (SH-S-7001, SH-S-7002), and as SA-3 placed prices.

### R2. Plan cards and what the page holds beside them

- **A plan card (`pricingCards`):** two `core` lines, its plan and its sites as scope:
  - CM-PLN-001, with `monthlyPrice`, `yearlyMonthlyPrice` and `promoText` as qualities, and `planDescription` in reading;
  - CM-PLN-002, with `yearlyMonthlyPrice`, the yearly period.

  Cards carry prices, so their labels are usually one site. Plus's price is 'starting at' (`priceLabel`).
- **A card feature (`planFeatures`):** placed on the capability its `summary` names, not its `name` key, `core`, with its plan as scope:
  - **Where its key misleads:** `card_rates_short` is a card rate on most sites (CM-PAY-007) and the third-party providers' fee on the sites without Shopify Payments (CM-PLN-003). `checkout_capacity` says 'Fully customizable checkout' (CM-CHK-003).
  - **A feature with a value** (a count, a rate, a price or a level of support: '10 inventory locations', 'Up to 5 staff accounts', 'Card rates from 2.9%', '24/7 local chat support') is its own card's plan's only: a higher plan's card or the table states its own.
  - **A feature with none** ('Built-in AI assistant', 'Live 3rd-party shipping rates') takes its plan and the plans above it, since the cards say 'Everything in Basic', 'Everything in Grow' and 'Everything in Advanced'. Those three lines are CM-PLN-001 `core`, the plans' tiers, with the card's plan as scope.
  - **A feature that names several things** takes a line for each: 'Sell online, in person, and in AI chats' is CM-SFR-001, CM-POS-001 and CM-AIA-005.
  - **The credits feature** (`gmv_rewards_signup_redesign`) is the new thing below, with its maximum, its 0.5% back on sales and its domain credit as qualities.
- **The POS Pro card (`posProCard`):** CM-POS-001 `core`, its price as quality. Each feature takes its own capability and CM-POS-001 (a product of its own: R8), with 'POS Pro' as scope.
- **The Agentic card (`agenticPlanCard`):** a plan, so CM-PLN-001 `core`, and CM-AIA-005 `core` for selling through AI channels, both scoped 'Agentic'. Its features are placed by what each states:
  - Shopify's Catalog and the choice of AI channels: CM-AIA-005;
  - 'Only pay when you make a sale': CM-PLN-003, a fee on sales set by plan;
  - its card rate: CM-PAY-007.

  `starterPlanCard` is null on these pages; where it isn't, place it as a plan card.
- **`alwaysIncluded`:** one `core` line per card, on the capability the card names:
  - themes: CM-SFR-001, and CM-AIA-001 for designing the store from a text prompt;
  - checkout: CM-CHK-001, its 15% conversion figure as quality;
  - Sidekick: CM-AIA-002;
  - support: CM-ONB-003, or in-person sales (CM-POS-001) where the site's fourth card is that;
  - multichannel: CM-CHN-001.

  No plan in scope: 'Always included' names none.
- **`statCards`** are `out` (R10).

### R3. The comparison table (`compareAllFeatures`)

- **The `table` entry** (`planNames`): CM-PLN-001 `core`, no scope (all 21 sites), as SA-3's table header.
- **A row: its capability.** A row is placed by what it states, on the capability whose cell cites the same plan row. Search its English heading (its own, or its twin's) with `caps --terms`: the cells cite the 30 September table's rows by heading, and their terms hold them. Every row of this batch had such a cell but these:
  - Earn 1% back: the new thing;
  - Accept payments with a phone or card reader;
  - Customer profiles and Returns under In-person sales;
  - Millions of tokens.
- **A row: its support.** `core`, a plan line that includes it, except where the cell or its note says otherwise:
  - Unlimited contacts and Capture customer leads are `shows`, as their cells (not defined);
  - Unlimited web hosting counts on CM-OPS-003, not CM-SFR-010;
  - Collective's sourcing is `shows` on CM-CAT-010 (its note);
  - a merchant of record's handling of duties is CM-MKS-003's (CM-TAX-008's note).
- **A row: scope and quality.** The plans whose cells hold a check or a value are its scope; a dash leaves its plan out. The page defines both marks: `checkAlt` 'مضمنة' and `dashAlt` 'غير مضمنة', in items.jsonl line 2, which no entry holds. Then come the sites (R0). The cells' values by plan are qualities (R7).
- **A row: its tooltip.** The tooltip is the row's definition. A thing it names as the row's own takes a line: B2B's blended or B2B-only store (CM-B2B-001), the devices of 'with a phone or card reader' (CM-POS-002), the AI chats' venues as fillers (R9). Things it names as examples or uses in a list take none, as the ruling after SA-41 has it: POS Pro's 'like …', Sidekick's uses, Inventory management's 'adjust quantities, see history', Additional staff accounts' control of access.
- **A row: its footnote.** A mark (`*`, or SH-69's `¹ ² ³`) points to a footnote: the note row '*Requires Shopify Payments', or the `apyDisclaimer` list items. The footnote is part of the row: its reading quotes it. The note row itself is CM-PAY-002 `shows`.
- **Section headings** (rows whose cells are all empty `text`): the rulings after SA-2, SA-5 and SA-28.
  - A title that names a capability or one part of the platform takes that capability's line, `shows`: Pricing CM-PLN-001; In-person sales CM-POS-001; AI features CM-AIA-001; Accepting payments CM-PAY-001; Hosting CM-OPS-003; Marketing CM-MKT-005; Marketplaces CM-CHN-003 (الأسواق here is marketplaces, not Markets); Sell globally CM-MKS-001.
  - A title that names only a grouping is `out`: Core features, Customization.
  - For SH-69: Finance (الأموال) groups four of Shopify's finance products, which are four capabilities, so it is `out`; Just for Plus (خاص بخطة Plus فقط) names a plan: CM-PLN-001 `shows`, scope Plus.
- **A row under a section whose title names a capability** takes that capability's line too, where the row is a kind of it (M-6 refined). Customer profiles and Returns under In-person sales take CM-POS-001; Website builder under AI features takes CM-AIA-001. A row whose capability already is the section's own, or its child, takes no extra line: Sidekick (CM-AIA-002), card payments in person (CM-PAY-021). Rows under Marketing, Hosting, Marketplaces and Sell globally take only their own lines.

### R4. The POS page (`planSummaries`, `posLiteVsProPlans`, `sideBySideGridContent`, `howToGetStartedContent`, `promoCardsContent`, `faqContent`)

SH-69 and SH-70 hold its ae-ar entries; I read them to write these rules.

- **A plan summary** (`mainPlans`, `alternatePlans`): one entry per plan, with many fields. Each line is `core`, with the plan (`display_name`) and the sites as scope, and the values as qualities:
  - CM-PLN-001: `monthly_price`, `annual_price`, `annual_monthly_price`, `paid_trial`; its descriptions in reading;
  - CM-PLN-002: the annual, biennial and triennial monthly prices, the billing periods;
  - CM-PAY-007: `card_rates.online`;
  - CM-PLN-003: `card_rates.third_party`;
  - CM-POS-001: `pos_pro_add_on`, with its free three months, `included_in_plan`, `is_available` and price, and `pos_bundle`'s bundled price;
  - CM-STF-001: `maximum_staff_accounts`;
  - CM-PAY-017: `local_payment_methods`, where it isn't null.

  `active_plan`, `recommended` and the `*_next` prices go in reading. Starter (`starter_2022`, 5 USD a month) and Retail (POS Pro included) are plans, CM-PLN-001 like the four.
- **A plan summary's features:** each on its own capability and on CM-POS-001, since the page lists the point of sale's features by plan, with the plan as scope. The leads, each to confirm with `caps --terms`:
  - staff access to POS and POS logins: CM-STF-001;
  - simple or rich customer profiles: CM-CUS-001;
  - returns at the original or at any location: CM-RET-003;
  - staff roles and permissions: CM-STF-002;
  - customer loyalty insights: search loyalty and analytics;
  - inventory management: CM-INV-001;
  - professional retail reports: CM-ANL-002;
  - omnichannel selling: CM-CHN-001.
- **`posLiteVsProPlans` and `plans`** (POS Lite, 'البيع الشخصي العادي', 'included in every plan', against POS Pro): CM-POS-001 `core`. POS Lite takes the four plans as scope; POS Pro takes its price as quality. Their features are placed as the summaries'.
- **`sectionHeader`:** as R3's section headings. A header whose subhead states what the platform does is placed by it: 'What is POS Pro?' is CM-POS-001 `core`. 'Included in every plan' names only the plans its items are in: it is the POS page's container, CM-POS-001 `shows`, scope Basic;Grow;Advanced;Plus.
- **`sideBySideItems`:** each heading and subhead on the capability it names, `core`: a feature statement.
- **`blocks`** (how to get started): `shows` on what each names, as SA-3's closing banner. 'Start free, no credit card' is CM-ACC-001 and CM-PLN-001; 'set up your store' is CM-ONB-004; 'customize with apps' is CM-APP-001.
- **`promoCardsContent`:** `shows` on what the card names: POS hardware CM-POS-002, a demo of POS CM-POS-001.
- **`questions`:** R6.

### R5. The international fees table (`redesignData`)

- **`hero`:** CM-MKS-003 `core`: Managed Markets shows the buyers the fees passed on to them, at checkout.
- **`pricingTable`'s `columnHeaders`:** CM-MKS-003 `shows`, the frame of the rows: fees with and without Shopify Managed Markets.
- **Rows of `type: header`:** section headings (R3). 'International features' is CM-MKS-001 `shows`.
- **Rows of `type: standard`:** on the row's own capability, `core`. The left (with Managed Markets) and right (without) values are qualities, each labelled; the description and disclaimers go in reading:
  - Shopify Payments processing: CM-PAY-007;
  - Currency conversion: CM-MKS-007, and CM-MKS-006 for its description's local currencies;
  - Duties and import tax at checkout: CM-TAX-008.
- **The row of `type: exclusive`:** CM-MKS-003 `core`, its fee as quality (3.5%, 3.25% on Plus). Its footnote, 'shipping rates apply separately', is the asterisked labels' term: CM-SHP-002 `shows`.
- **The exclusive row's `features`:** each takes CM-MKS-003 `core` (a product of its own: R8), and its own capability:
  - the merchant-of-record service: its tax registration is CM-TAX-003 `core`;
  - managed international pricing: CM-CAT-013 `core`, by the exclusive row's disclaimer, which defines it;
  - one-session setup: CM-MKS-003 only;
  - discounted international shipping labels: CM-SHP-002 `core`;
  - unlimited HS code classification and import restrictions management: CM-SHP-020 `core`;
  - guaranteed duties: CM-TAX-008 `shows`, as the cell's SH-S-0571;
  - Shopify Protect: CM-PAY-010 `core`.

  The page names no provider. The cell's Global-e, the merchant of record, rests on other statements; the reading cites it where it bears.
- **`faq`:** R6.

### R6. FAQs (`accordionItems` on the plans and international pages, `questions` on the POS page)

An FAQ is placed by what its answer states, on the capability the question asks about, and on each thing the answer names as its own:
- `core` where the answer states the platform's own feature or behaviour, as rule 4 has an FAQ that names a built-in feature: Managed Markets builds its fees into the prices buyers see;
- `shows` where it gives terms only (costs, fees, contract periods, cancellation, the plan's monthly cost) or names a topic;
- `outside` where it names a third party doing it with no interface of the platform.

Things the answer names in passing, in a list, take no line (the ruling after SA-41). The answer's words go in reading. The FAQ section's heading isn't an entry here; elsewhere it is CM-ONB-003 `shows`, as SA-3.

### R7. Qualities: when a line holds a price, a rate or a limit

- **Form:** `<what>: <value in its words>`, `<what>` an English label and the value copied from the entry. Per plan, write `<value> (<plan>), <value> (<plan>)`, in the table's column order, plans with the same value together: `(Basic, Grow, Advanced)`. Several qualities go `;`-separated.
- **What counts:**
  - a price, a fee, a rate or a discount;
  - a credit or its maximum;
  - a trial's length or price;
  - a count or limit: inventory locations, staff accounts, catalogs, headless storefronts, tokens, reports, automated translations, synced orders;
  - a level in words that bounds the thing: limited or full checkout customization; standard, 2x or 10x API limits; limited or full data access;
  - a number a card claims: conversion 15% better on average.
- **Never:** a check or a dash, which give the scope; a support level or a kind of profile in words ('Live chat', 'Simple'), which go in reading; a store's own value.

### R8. When a line states a second thing

- **Each thing the line names as its own takes its line** (rule 2): the card feature of three ways to sell; the currency conversion row's local currencies; the always-included cards. Things named in a list in passing take none (R3's tooltips, R6).
- **Follow the cell's note** where it says where else the line counts: CM-CAT-010, CM-SFR-010, CM-TAX-008 (R3).
- **A product of its own** (Managed Markets, POS Pro, Agentic) gives each of its features its line beside the feature's own. The four plans' cards don't: the plan is their features' scope.
- **A row read with its section** takes the section's capability where it is a kind of it (R3).

### R9. When a line names a partner or a third party

- **A venue** where the platform puts the merchant's products: the filler of the `core` line (M-3). The AI chats are 'ChatGPT, Gemini'.
- **A third party named as providing the service,** in a footnote or disclaimer: an `outside` line on that service's capability, the third party as filler, beside the row's own line. Read the capability's cell first: it may hold the same. This is SH-69's `apyDisclaimer`:
  - Stripe Payments Company for money transmission and account services;
  - Fifth Third Bank N.A. holding the funds;
  - Celtic Bank issuing the Balance and Credit cards, under licence from Visa U.S.A. Inc.;
  - WebBank issuing Shopify Capital's United States financing;
  - Melio for Bill Pay, named by its logo's `alt`.

  These lead to CM-PAY-023 to CM-PAY-027. 'Shopify is a technology company, not a bank' goes in reading.
- **Shopify's brand in a product's name names no maker:** Shopify Payments, Managed Markets, Protect, Collective, Markets, B2B, Balance, Capital, Credit, Bill Pay. Each is `core` by its cell's admin place or plan row. Hydrogen, 'a React-based toolkit from Shopify', and Oxygen, 'Shopify's free global hosting solution', are `core`, as CM-SFR-011's cell holds them; `own-service` is the other reading.
- **No filler:**
  - card brands named as what buyers pay with (Visa, Mastercard; the Amex rates' row);
  - an unnamed third party ('third-party providers', 'from third parties');
  - a law named as the subject of a tool ('Tools for GDPR compliance', on the ie card), which is the filler only where the line says the law sets the terms.

### R10. When a line is `out`

- the testimonial block's figures (`statCards`: '$1.1 trillion', '26 seconds'), as SA-3's testimonials;
- a section heading that names only a grouping: Core features, Customization, SH-69's Finance;
- a currency sign or a UI string alone. None is in this batch: the selection's rule prunes buttons, toggles, images and links, which also takes away the Agentic card's link to /agentic-plan.

### R11. Leads for the English card features, by `name` key

These are leads, from the capabilities' names and cells. Each batch reads its own summary and searches:

| Key | Summary | Lead |
| --- | --- | --- |
| `shipment_short` | Up to 87% off shipping | CM-SHP-002, whose cell holds the plan line Shipping discounts (quality) |
| `pos_pro_locations` | Up to 200 POS Pro locations | CM-POS-001 (quality) |
| `fraud_check_and_3d_secure_checkout` | Fraud protection and 3D Secure checkout | search CM-ORD-006 and CM-PAY-010; 3D Secure, search |
| `simplified_gdpr_compliance` | Tools for GDPR compliance | CM-TRU-005 |
| `automated_vat_collection` | Automatic VAT collection | CM-TAX-002 |
| `bot_protection` | Bot protection | CM-TRU-004 |
| `manage_business_entities_per_market` | Manage businesses by market | CM-ACC-005 |
| `marketing_across_channels` | Track marketing across channels | search CM-MKT-008 |
| `built_in_seo_features` | Built-in SEO features | CM-CNT-007 |
| `bundles_and_recommendations` | Upsell with bundles and recommendations | CM-SEL-006 and CM-MKT-021 or CM-MKT-023 |
| `schedule_launches_and_discounts` | Schedule launches and discounts | CM-MKS-002 (Rollouts) and CM-MKT-001 |

The other keys are this batch's: R2, and the lines of 22 to 50.

## New things

**`new:Earn 1% back on all sales as subscription credits`**, 4 lines: 28 (Basic card), 33 (Grow card), 41 (Advanced card), 68 (the table's row).
- **What it is:** the platform credits the merchant's subscription with 1% of all sales (0.5% on payments not through Shopify Payments). It runs up to a maximum per plan (4,500, 6,500 and 8,000 US dollars on these pages; none on Plus), 'valid for your first 6 months or until you reach the max'. The cards add a domain credit: 'Add a domain, get US$20'.
- **Its place of its own:** a plan line, the comparison table's row 'Earn 1% back on all sales' (اربح عائدًا بنسبة 1% على جميع المبيعات), as B-extent's "What a place of its own is". Every read site's cards and table state it.
- **Its names:** the English words 'Earn 1% back on all sales', 'subscription credits', 'Earn up to $4,500 in credits'; the Arabic 'اربح عائدًا بنسبة 1% على جميع المبيعات', 'كرصيد اشتراك', 'اكسب ما يصل إلى $ 4,500 كأرصدة'. The card's key is `gmv_rewards_signup_redesign`.
- **Proposed:** domain A, area PLN. Parent CM-PLN-004 (platform billing), where credits against the bills sit (the help section 'Managing credit notes and billing credits', SH-I-2348, which CM-PLN-006's reading names). CM-PLN-001 is the other parent, since the maximum is set by plan.
- **Searched:** `caps --terms` subscription credit, billing credit, credit note, GMV, incentive, reward(s), credits, cash back, cashback, رصيد, أرصدة, استرداد; `search` subscription credit, billing credits, credit notes.
  - The hits are buyers' cashback and store credit (CM-LOY-001, CM-LOY-003), refunds (CM-RET-002), billing (CM-PLN-004, whose cell holds credit notes, not credits earned on sales), Salla's prepaid balance (CM-PLN-006) and Salla's GMV-based terms (CM-PLN-001 by another platform's cell).
  - None holds the platform's credits to the merchant.

## Entries I couldn't tell, and what would settle each

- **R0's per-language reading of the scope** (every line): the alternative is the literal one, labels always but on SH-E-907c9d89. It would give 357 more lines a scope of 18 English or 3 Arabic sites, every one of them universal by R0's measurement. The coordinator decides; R0 lists everything needed to redo it either way.
- **8, managed international pricing, on CM-CAT-013** (a CHANGES line): read by entry 6's definition, it is the platform raising 'أسعار المنتجات الدولية' itself. The alternative is CM-MKS-003 alone, as Managed Markets' own feature. What would settle it: a help page or admin route of Managed Markets' pricing, held but not in this structure.
- **11 and 12 on CM-SHP-020** (a CHANGES line): HS code classification is the customs code of the capability's name. Import restrictions management could instead be CM-CAT-009 (product restrictions, which holds nothing on Shopify). The admin's Managed Markets routes would settle what the restrictions limit.
- **84 on CM-POS-002 `core`** (a CHANGES line): a plan line that includes card-present payment with the merchant's phone (Tap to Pay on iPhone or Android) or a paired card reader. The cell held only Shopify's sale of hardware (`own-service`) and its terms. `shows` is the alternative, if a plan line that names devices is read as naming the hardware's use, not the platform's device.
- **7, the merchant-of-record service, on CM-TAX-003 `core`:** the cell holds Global-e's registration under Managed Markets as `outside`. The entry names no provider, so I placed it by what it shows. Filing and remittance gave no CM-TAX-006 line: that cell's automated filing covers only sales where the merchant is merchant of record.
- **`googleCountryOffer: $500 USD`** (1, 19, and every terms entry): an offer named for Google, used by no held text of the three ae-ar pages. I gave it no line. A page or sign-up step that shows the offer would settle its capability: advertising (CM-MKT-010) is the plain lead, not evidence.
- **Section headings** (4, 64, 83, 88, 92, 100, 104, 115, 125): `shows` on the capability their title names. The alternative is `out`, if every table section is read as only a grouping. Marketing (104) is the closest case: its rows are several capabilities' things.
- **51's CM-AIA-001 line,** designing the store 'from a simple text prompt': an AI feature by the table's Website builder row, which its section names. The card itself doesn't say AI.
- **50, `checkout_capacity`:** the key says capacity and the summary says 'Fully customizable checkout'. I placed the summary's words (CM-CHK-003). High-volume checkout (CM-CHK-001) is what the key may mean.
- **55, 'flexible delivery options'** of POS Pro: their kind isn't named. I placed them on CM-SHP-006 (pickup and the store's own delivery), beside CM-SHP-007 for the pickup.
- **56 to 60, the Agentic plan:** a plan of its own (CM-PLN-001), at 0 US$ a month. Its page, www.shopify.com/agentic-plan, is captured (run 20260930T050139Z-shopify-com-pages, the ledger) but outside this structure. Its country pages (/ae-ar/agentic-plan) weren't attempted.
- **59, 'Only pay when you make a sale',** on CM-PLN-003: its rate isn't stated.

## A structure whose items and sources disagree

- **The terms entry's Basic annual price doesn't follow the site's own cards.**
  - The plans pages' terms entry (19, the same words on ae-ar, eg and sa) gives 'basicAnnualPrice: <span>$24.00 USD</span>' and a 25% annual discount.
  - The same value stands on www.shopify.com and www.shopify.com/ae, but the Basic cards' yearly prices differ by site: 29 on ae-ar (21; the table's Pay yearly row, 66), ae and www.shopify.com, and 24 on eg and sa.
  - On the POS pages, the ae-ar summary gives Basic `annual_monthly_price` 29 (`annual_price` 348; SH-69's 30), while the English www.shopify.com/ae POS page gives 24 (288) beside its card's 29.

  The bytes state each; every line quotes its own entry's figure. Which price is charged isn't held. The pages were served under different variants (`experimentVariationId`), which may be the cause (an assumption).
- **The eg and sa pages write their prices in Arabic-Indic digits** ('‏٢٧ US$' on their Basic cards), while ae-ar writes Western digits. They are the entries' own words: quote them as written.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records (`meta.json`'s source, one record per page); the items are the source's own data, by the register.

## What the sources state that no entry holds (for the second stage)

In items.jsonl line 2 (the ae-ar plans page), these are pruned or not wrapped by the selection's rule, so no entry holds them:
- `compareAllFeatures.checkAlt` 'مضمنة', `dashAlt` 'غير مضمنة' and `captionText`: the table's own marks. R3 reads them.
- the hero's `toggle` ('ادفع سنويًا', 'ادفع شهريًا'), the yearly or monthly choice: CM-PLN-002, already held by the cards' lines.
- `turnPlansIntoProgress`, the closing banner: the trial again.
- `wordOnTheStreet.testimonial`, a merchant's quote: `out` in any case.
- `ctaHrefs`, sign-up links with `locale=ar-AE&language=ar`.
- `thereIsMore.agenticPlanCard.button.href` '/ae-ar/agentic-plan': a lead for CM-PLN-001 and CM-AIA-005, to read on the captured www.shopify.com/agentic-plan.

## The checker's lines, read again

- **`CHANGES CM-CAT-013@shopify gains core, by line 14` (8):** kept. The fee table's own definition makes managed international pricing the platform pricing products itself, which the cell held only for apps (`extension-point`). The alternative is under "couldn't tell".
- **`CHANGES CM-POS-002@shopify gains core, by line 122` (84):** kept. A plan line includes card-present payment by phone or card reader. The alternative is under "couldn't tell".
- **`CHANGES CM-SHP-020@shopify gains core, by lines 18, 20` (11, 12):** kept. The cell's reading says no held Shopify statement names an HS code; this one does, as a Managed Markets feature. It changes the cell from `not-stated` to `core`.
- **`CHANGES CM-CAT-010@shopify gains core` (80), corrected:** CM-CAT-010's note keeps Shopify Collective's statements `shows` there (the coordinator, after E-anchor batch 4). The line is `shows` now and changes nothing.
- **`NOTE` on a product named with the platform's brand** (lines 5, 8, 9, 24, 25, 32, 110, 111, 116, 134, 169, as the checker numbers the file, header as line 1): Managed Markets, Shopify Payments, Shopify Protect, Shopify B2B, Shopify Collective and Shopify Markets. Each is `core` by its cell's place, not by its name:
  - Managed Markets' routes managed and :id/managed;
  - Shopify Payments' route and plan row;
  - Protect's route shopify-protect;
  - B2B's admin label and plan row;
  - Collective's plan row;
  - Markets' route and plan row.
- **`NOTE` on footnote marks** (lines 16, 17, 139, 168, 170: entries 10, 98, 127, 129): each reading quotes its footnote. 10's is in its row's `footnoteHtml` (6); the others' is the note row '*يتطلب Shopify Payments' (99).
- **`NOTE` on a new thing whose entry has leads** (lines 48, 54, 63, 103). I read the leads' cells: CM-SFR-008 (by the popover's 'domain'), CM-PLN-001 and CM-API-001 (by the plan names Grow and Advanced), and CM-PAY-002, CM-AIA-003 and CM-PAY-013 (by 'Shopify Payments' and other words of 68's tooltip). None holds credits to the merchant: the domain credit is a way to earn the credit, and Shopify Payments its condition.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 4 lines.

## Problems with the brief or the script

- **The brief's known case meets the structure's dedup by words.** An entry's labels are the sites that state it 'in those words', and no Arabic line can be stated by an English site. So 'a line that every read site of its page states takes no scope', read literally, applies to one line in 1,056. R0 is my reading, measured; the brief could say which it means.
- **Some quotes can't be whole.** A placements row can't hold a double quote, so a source's quoted term is quoted without its quotation marks: 6's disclaimer, يرفع "التسعير الدولي المُدار"; 102's ".myshopify.com".
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief itself states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **R0 stands: a line's sites are read against the sites of its own language.**
  - A line on every read site of its language takes no scope, where its twin on the other language's sites states the same values. That holds for 357 of 362 such lines.
  - The brief's known case says "every read site". With English and Arabic sites read together, this is how it applies.
- **One line is moved.** Managed Markets' international pricing (SH-E-cc9c56da) goes to CM-MKS-006, not CM-CAT-013, as SH-34's check placed Managed Markets' prices: a market's adapted prices are international pricing, not the platform's automatic pricing of products. CM-CAT-013 doesn't change.
- **Kept:**
  - CM-POS-002 gains `core` from the plan line that includes taking payments with a phone or a card reader;
  - CM-SHP-020 is `core` from Managed Markets' HS code classification and import restrictions management;
  - Collective's line is `shows`, as CM-CAT-010's note keeps it.
- **New thing:** Earn 1% back on all sales as subscription credits, a plan line, decided with the others.
- **R1 to R11 stand for SH-69 to SH-79.**
  - The Arabic-Indic digits of the eg and sa pages are quoted as written.
  - `googleCountryOffer` takes no line.
- **Cost:** 29.7 million tokens over 104 requests, about 228,000 an entry.
