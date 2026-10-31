# SH-67: Shopify `editions-page-data`, Spring '26 from Operations' Global to the Developer collection's Apps + Extensions

## What I read

- The brief (`briefs/H-held.md`), the structure's digest (`held/rules/editions-page-data.md`, section 6 included) and the last section of `held/review-H-rulings.md`.
- observed-sh at `e38dc17e3`: `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `shopify/editions` and `shopify/editions-page-data`, and the selection rows. The evidence map's Shopify part and its faults; B-extent's "Cells and evidence" and "Conventions from the dry run".
- Earlier batches' notes, only where the digest sends a case:
  - SH-66, its rules E135 to E144 and the coordinator's check, since my Developer cards repeat its merchant cards;
  - SH-62's E102 (Shop's own features), SH-61's E94 and SH-64's E117 (Managed Markets lists), SH-58's E67 (an API's field).
- Earlier lines, read by `grep` where `earlier` found none:
  - the Shop skill (SH-E-a2c16b9b) and the Shop Pay agent lines (SH-E-429c6a35, SH-E-fa5f4a5f);
  - Shop sign-in (SH-E-a4536e71) and Shop Minis;
  - USDC (SH-E-ff639531, SH-E-54492956), the named local methods (SH-E-fd124edd, SH-E-8f7827b3) and cash (SH-E-61408991);
  - Shopify Capital (SH-E-56d61216, SH-E-3a01bbfe, SH-E-c57999c8, SH-E-99955ac8, SH-E-df474732);
  - Quick Sale (SH-E-c52f377c) and Balance (SH-E-e6b1e0c3);
  - App versions (SH-E-9e317cee, SH-E-db88ed0f), nested cart lines (SH-E-8953e070), Dev MCP (SH-E-cefadf35, SH-E-e66eb919, SH-E-d1b018d2);
  - Shopify Tax (SH-E-29144b11, SH-E-b0925063), address autocomplete (SH-E-4969a4d9) and Admin languages.
- Twins named in the prompt: SH-66's 'Shopify AI Toolkit' (SH-E-80bdfc5c) and 'WhatsApp marketing consent' (SH-E-aa06fc7c).
- One linked page, where the card left the support open (R47.6): the Help Center's USDC page, held at observed-sh `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md`, lines 201 to 205 (the card links `…/shopify-payments/usdc-payments`, which `held_index.py` doesn't hold).
- For the new things' places only: observed-sh `structures/shopify/admin-router/items.jsonl`, lines 358 and 1178.
- `earlier` printed no earlier line for any of the 99 entries. The twins are cards in other words (E61, E79). I found the ones inside this batch by reading it: 16 and 72, 19 and 83, 35 and 73.

## Counts

- **Entries:** 99, all placed.
  - 96 take capability lines only.
  - 2 take a capability line and a `new` line: SH-E-0f6f1cd5 (Tipping) and SH-E-5d78ff45 (Admin languages).
  - 1 is `out`: SH-E-b67e40eb, the Everywhere Cap, merchandise.
- **Lines:** 175, of which 172 are capability, 2 new and 1 out.
- **By support:** core 120; extension-point 29; own-service 14; own-service;extension-point 5; shows 3; core;extension-point 2; core;shows 1.

## The new things

Both are names earlier batches gave, kept as they wrote them. The Editions are English only, so no Arabic name is held. Each has a place of its own, so each line takes the support of what the platform does (rule 22): `core`.

- **Tipping** (SH-50's name): SH-E-0f6f1cd5, 'Collect tips' in the Shopify app's Quick Sale.
  - **Its place of its own:** the admin router's anchor `{"title":"Tipping","path":"tipping"}` in the route `checkout-settings:index`, section Checkout (observed-sh `structures/shopify/admin-router/items.jsonl`, line 358). B-extent counts an anchor with its own title and path as a place of its own.
  - **Proposed:** SH-50's domain E, POS, under CM-POS-001 (SH-50's notes, line 191). That anchor puts tipping in the checkout too, so CM-CHK-001 is a candidate parent. The coordinator decides with SH-50's entries.
  - **Searched:** tipping; tips. No capability holds them.
- **Admin languages** (SH-34's name on Shopify): SH-E-5d78ff45, the Dev Dashboard's UI and navigation 'in your preferred language'.
  - It is the one new thing across the platforms, the admin's or a portal's own interface language (the ruling after SA-49). The digest calls it `العربية / English`; Shopify's lines name it `new:Admin languages` (SH-E-c4c8d76b, SH-E-19b0178e), and I kept that name.
  - **A place of its own on Shopify:** the admin route `accountLanguage:redirect` at `settings/account_language`, 'Account language', section Settings (`admin-router/items.jsonl`, line 1178). It only redirects, so its target governs (the ruling after SH-8). This is a lead, not a placement.
  - **Proposed:** domain A, the account. The Dev Dashboard's language is a partner's, under CM-PTN-001.

## Rules I followed that the digest doesn't hold (from E145)

- **E145: a cashback tied to a payment method stays on the method's capability.** The buyer's USDC cashback (SH-E-78b68756) is CM-PAY-018 `core`, not CM-LOY-003.
  - CM-LOY-003 is a store's cashback credited to its customer's wallet. Its cell finds no Shopify statement of cashback a store credits.
  - The help page names no one funding it: 'When your customers pay with USDC on Base at checkout, they might automatically receive USDC cashback on their purchase.' (line 203).
  - This is E115's test for the merchant's card cashback, applied to the buyer's payment option. A marked reading.
- **E146: the platform's own things reached from Shop take their own capability `core`, beside CM-CHN-002 `own-service`.** This is E102's store credit case.
  - In-store pickup and returns from Shop (SH-E-ad43b9bb) are CM-SHP-007 `core` and CM-RET-003 `core`.
  - Shop's own features take `own-service` on their capabilities (E102, E120): its sign-in (CM-CUS-010), its conversational search (CM-AIA-005), its recommendations (CM-MKT-023) and its demand indicators (CM-SUP-003, below).
  - The customer accounts Shop sign-in works with take no line (E81).
- **E147: Shop's demand indicators and low-stock flags on Shop's product pages are CM-SUP-003 `own-service`,** beside CM-CHN-002 (SH-E-dd0966ca). They are social proof shown to shoppers, a marked reading, since no held statement defines social proof. They aren't CM-INV-004, whose note makes low stock an alert to the store.
- **E148: a card that names Shopify Payments or Shopify Tax as the one doing a feature takes CM-PAY-002 or CM-TAX-002 `core` beside the feature's capability.** This follows SH-E-542edee2 and SH-E-29144b11. The cases are SH-E-4d12c941, SH-E-533253dd, SH-E-490a99a4, SH-E-810cb120, SH-E-a833fd34, SH-E-876083d6 and SH-E-a310449c.
- **E149: a Managed Markets card for named countries.**
  - The CM-MKS-003 line takes the countries as its scope ('UK;Canada').
  - Its other features take 'Managed Markets and UK;Canada' (E117 for another market's words).
  - Localized prices that include taxes split as E94 has it: CM-MKS-006 and CM-TAX-001 scoped 'Managed Markets', the duties staying on CM-MKS-003 (SH-E-71886bef).
- **E150: 'Coming soon to France.' beside a released feature** takes a second line on the same capability, `shows`, France its scope (the ruling after SH-34; SH-E-804fbdf7).
- **E151: Dev Dashboard cards.**
  - **The dashboard:** CM-PTN-001 `core`, since its cell holds the Dev dashboard (SH-I-2094). E87 extended to it.
  - **Dev stores in it:** CM-DVT-004 `core` (rule 41).
  - **Client transfer and collaborator stores:** they stay in CM-PTN-001's line, since CM-STF-005's note leaves the partner's own side to domain F.
  - **A partner's team roles:** CM-PTN-001 `core`, by the ruling on a partners' portal's permissions; the count is a quality.
  - The cases are SH-E-6055c1ba, SH-E-f60cc206, SH-E-6343ce1c, SH-E-5d78ff45, SH-E-df1cb8c1, SH-E-802a7c4b, SH-E-244b9ce2 and SH-E-1b8e2abd.
- **E152: an app's deploys or releases in CI/CD are CM-DVT-002 `core`.** The Summer 2023 card puts them through the CLI ('…deploy your extensions together in a single package through the CLI, providing an end-to-end CI/CD workflow.', SH-E-9e317cee). A marked reading (SH-E-af650ed4, SH-E-df1cb8c1).
- **E153: the Shopify AI Toolkit used on extensions' code, not on a store, is CM-DVT-001 alone** (SH-E-9eb60820, SH-E-2f3f9472). R47.3 and E135's CM-AIA-004 are for an assistant working on the store. The developer twin that builds 'storefronts, apps, and themes' (SH-E-e63a0cd0) keeps SH-66's CM-AIA-004 line.
- **E154: Dev MCP supporting a thing of the platform takes that thing's capability `core`,** as SH-E-d1b018d2's Liquid did: all API versions on CM-API-006 (SH-E-4889228a).
- **E155: an API 'before rollout to businesses' takes `core;shows` on one line,** as rule 34 does for an early-access link beside an admin link. The API is open to developers now, but its features aren't yet offered to stores (SH-E-84bad5e9, CM-CAT-003).
- **E156: Shopify Capital repaid from the Shopify Payments balance** (SH-E-9a01503e): CM-PAY-026 `shows`, the brand alone (rule 21), the repayment its quality (rule 48); and CM-PAY-005 `core`, the payment service's balance.
- **E157: E83's CM-API-001 line** goes to cards whose title names an API: GraphQL, Metafields and Metaobjects, Admin, Inventory, Collections. An API group that another capability already holds is that capability's line alone, such as the checkout and accounts configuration API on CM-CHK-003 (SH-E-c524bb88).

## Entries I couldn't tell, and what would settle each

- **SH-E-244b9ce2, 'App Events API'.**
  - **Where it is:** CM-APP-004 `core`, since that cell already holds an API group of that name (SH-I-0075, 'api-resources: App Events API') and rule 2 sends a held place to its capability.
  - **The doubt:** the card defines it as apps sending their own events to Shopify to watch their performance in the Dev Dashboard. CM-APP-004's thing is the platform notifying an app of its lifecycle, and its note reads SH-I-0075 as the Partner API's.
  - **What would settle it:** the API reference's page for App Events API, not read. If SH-I-0075 is this new API, CM-APP-004's reading of it needs correcting, and the entry is a new thing ('App Events API', domain F, under CM-PTN-001 or CM-APP-001).
- **SH-E-a833fd34, card testing blocked by Shopify Payments.** It is on CM-ORD-006, fraud analysis, the nearest capability. No capability holds a payment service's blocking of fraud at the transaction. The decision would be whether to make one, or to keep fraud analysis broad.
- **SH-E-5cae98ba, Shop skill.** 'approve purchases through' Shop is on CM-CHN-002 `own-service`, since the link is Shop's (`www.shopify.com/shop`). If Shop's approval is Shop Pay, it is CM-PAY-014 `own-service`, as SH-47's twin had Shop Pay. Shop's help on the skill (`shop.app/skill`, not read) would settle it.
- **SH-E-dd71d54a, Shop's 'Personalized search'.** Its CM-AIA-005 line reads 'through conversation' as AI, which the card doesn't name.
- **SH-E-dd0966ca, demand indicators.** CM-SUP-003 or a new thing: a definition of social proof, which no held statement gives.
- **SH-E-ad43b9bb, Shop to the retail store.** I placed no POS line for 'your retail store', since the card doesn't name POS (a lead).
- **SH-E-da2288cb, ShopifyQL's 'online editor'.** It takes no line: whether it is the admin's report editor (CM-ANL-002) or ShopifyQL Notebooks (own-service, the digest's table) isn't stated.
- **SH-E-34cff639, standard storefront events and actions.** 'AI agents' take CM-AIA-005 `extension-point`, a marked reading. The 'apps' beside them name no capability of their own.
- **SH-E-6c36622b, the billing address in validation functions.** It takes no line: no capability holds a checkout's billing address apart from the checkout.

## The `CHANGES` lines, and what I decided

Each stands, read against its sources:
- **CM-AIA-004 gains `core` and becomes held** (SH-E-e63a0cd0). It is the developer twin of SH-66's SH-E-80bdfc5c, which the coordinator's check kept (E135).
- **CM-AIA-005 gains `own-service`** (the Shop skill; Shop's conversational search). Rule 11 makes Shop's AI `own-service`. The skill is as SH-47's SH-E-a2c16b9b; the search is a marked reading.
- **CM-B2B-001 gains `extension-point`** (SH-E-6c36622b): apps' validation functions enforce B2B requirements (E78, rule 46).
- **CM-CHK-005 gains `own-service`** (Checkout Blocks' address rules and order limits): E103, and the digest's table for Checkout Blocks.
- **CM-CHN-002 gains `extension-point`** (Shop Minis, three entries): rule 11, others' Shop Minis.
- **CM-CUS-010 gains `own-service`** (Shop sign-in, twice): rule 11.
- **CM-DVT-004 gains `core`** (dev stores in the Dev Dashboard): rule 41. The platform keeps the stores for partners in its own dashboard.
- **CM-MKT-023 gains `own-service` and becomes held** (Shop's recommendations): E75 and E120.
- **CM-PAY-022 gains `extension-point`** (subscription payment methods replaced through apps' customer account extensions): rule 43, providers' access to stored methods.
- **CM-PAY-032 gains `core` and becomes held** (Quick Sale's payment links): E118, as SH-E-c52f377c.
- **CM-POS-003 gains `extension-point`** (cash management extensions): apps manage cash sessions through the platform's APIs and POS targets (rule 17). The cash drawer's audit trails stay there (E139).
- **CM-SUP-003 gains `own-service`** (Shop's demand indicators): E147 above, a marked reading. This is the line most worth a second look.

## Leads not taken

- **CM-CAT-009 (product restrictions), for SH-E-27d05538.** Managed Markets' restricted products stay on CM-MKS-003 (rule 45). CM-CAT-009's note keeps a payment service's prohibited products apart from a product's restrictions.
- **CM-INV-004 (low stock), for SH-E-dd0966ca.** It is an alert to the store, not a flag to shoppers.
- **CM-LOY-003 (cashback), for SH-E-78b68756 (E145) and SH-E-e86654d1.** The Balance cashback is the account's, CM-PAY-023 (E115).
- **CM-MKT-020 (ads wallet), for SH-E-e86654d1.** Balance pays the ads by ACH or wire. It isn't a balance kept for ad spend.
- **CM-ONB-004 (store setup), for SH-E-0277d6f7.** Shop Pay's 'simplified onboarding' isn't the store's setup wizard.
- **CM-CAT-003 and CM-CAT-005, for SH-E-5e0aef58.** Shop's merchandised categories are Shop's, and its 'brands' are the stores.
- **CM-PAY-003 (payment onboarding), for SH-E-490a99a4.** Its help address under `onboarding` only shows which feature is meant.
- **CM-API-006, for SH-E-5f455842.** The CLI's own semantic versions aren't the API's.
- **CM-APP-012 (marketplace connection), for SH-E-c82019e2.** Sales channel apps' channel connections aren't the store's link to a marketplace account.
- **CM-STF-002 and CM-STF-005, for SH-E-f60cc206 and SH-E-6055c1ba.** They are the partner's own team and stores, domain F.
- **CM-AIA-004, for SH-E-e32712e6.** The 'agents' that run CLI commands are named in passing.
- **CM-RET-003 and CM-SEL-001, for SH-E-e7c74624.** The App Store categories named there are the requirement's condition, so they are its scope, not lines.
- **CM-SFR-001, for SH-E-16e047a0.** 'directly from the product page' is named in passing.

## For the second stage

- **What the USDC help page states that no entry holds** (observed-sh `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md`):
  - line 203: 'A gift icon is displayed next to the USDC payment option at checkout to indicate that cashback is available.';
  - line 205: 'Cashback is distributed automatically to your customer's connected crypto wallet on Base 30 days after their purchase. Cashback rewards are capped at 100 USDC per transaction.' This is a quality of CM-PAY-018 if a statement is read for it.
- **What the admin router holds that this batch's entries don't:** the route 'Account language' at `settings/account_language` (`admin-router/items.jsonl`, line 1178), a lead for the interface language's new thing; and the anchor Tipping in the checkout settings (line 358).

## The structure against its source

I read the entries as `show` prints them, from the structure's items, and didn't compare them with the page's bytes. Nothing in the rendering looked cut or out of place: every card had its title, its description and its links.

## Problems and notes for the coordinator

- **`earlier` finds no twin in this part of Spring '26,** since the Developer cards repeat the merchant cards in other words. I found the in-batch twins by reading:
  - SH-E-6d43442a and SH-E-15aa8b66 (Shop Minis);
  - SH-E-69dcd480 and SH-E-1b8e2abd (ship and pick up);
  - SH-E-a87d1f84 and SH-E-c524bb88 (branding).
  
  The prompt named the two in SH-66.
- **The quote rule:** one reading quotes a held help page by its file and line, not an archive record, since the page is a structure's file. The checker found it.
- **Cost:** about 40 requests, the context near 200,000 tokens at the end.

## The coordinator's check

Measured: 20.3 million tokens over 88 requests, about 205,000 an entry. The checker prints no problem.
- **Kept:** every `CHANGES` line, E145 to E157 (the Editions digest's section 6) and the two new things, Tipping and Admin languages.
- **Corrected, line 87 (SH-E-244b9ce2, the App Events API):** from CM-APP-004 to CM-DVT-001 `core`. The card defines the API as an app sending its own events to Shopify to monitor the app, a developer tool (rule 17), as SH-49 read Fall 2026's app events; CM-APP-004's App Events API is the Partner API's events of an app's lifecycle (SH-I-0075), a homonym. Line 88's CM-PTN-001 stands.
- **E147, Shop's demand indicators on CM-SUP-003:** kept as the marked reading it is; the low-stock flag rides with it, for the amendment to decide with CM-SUP-003's definition.
- **SH-E-a833fd34 on CM-ORD-006:** kept as the nearest, with CM-PAY-002 by E148; whether a payment service's own fraud blocking is a thing of its own goes to the amendment.
- **SH-E-5cae98ba on CM-CHN-002 `own-service`:** kept. The card says purchases are approved 'through Shop', its link Shop's page; Shop Pay isn't named.
