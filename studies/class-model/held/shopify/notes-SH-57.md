# SH-57: Winter '24's last Developer groups, and Summer '24 from its Top 10 to Sell globally (high)

**What the batch is.** 86 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`), in the pages' order:
- **Winter '24** (line 6, `routes/($lang).editions.winter2024`), Developer (`pageSections/4`), its `sectionGroups` 17 to 22: Webhooks and Functions (entries 1 to 3), GraphQL (4 to 7), Keyboard swag drop (8), App Review/Discovery (9 to 11) and Insights/Audience (12, 13). Group 20, 'App Growth', holds no product, so no entry. SH-56 ended with group 16.
- **Summer '24** (line 7, `routes/($locale).editions.summer2024._index`, `formattedCollections/N/cards|list/K`), its first six collections: Top 10 (14 to 23), Expand across markets (24 to 26), Sell online (27 to 38), Sell in person (39 to 53), Sell wholesale (54 to 67) and Sell globally (68 to 86). The next collection, "World's best checkout", is SH-58's.

I read each entry against its object in the page data (my `ptr.py` in the scratchpad prints an item by its locator). Summer '24's collections all have an empty `descriptionHtml`, so each card is read with its collection's title, its `productType`, its `shortTitle` (the rendered heading, `structures/shopify/editions/www.shopify.com_editions_summer2024/items.jsonl`, lines 277 to 322) and its CTAs.

**Count.** 175 lines: 167 on a capability, 7 `new`, 1 `out`.
- Every entry is placed: 78 only on capabilities, 1 only `new` (SH-E-18409847, Web performance dashboard), 6 on both, 1 `out` (SH-E-0381e647, the Shopify Keyboard).
- Supports over the lines, a line with two supports counting in each: `core` 135, `own-service` 30, `shows` 16, `extension-point` 6.

**E1 to E50 are kept,** with the rulings in `review-H-rulings.md`'s last section. `held_entries.py earlier` printed an earlier line for 6 of the 86 entries (Shopify Magic, Managed Markets twice, Sign in with Shop, Combined Listings app, Store credit, Semantic Search, Headless B2B storefronts), and I kept to each, as the readings say. `makers` answered Managed Markets, Markets Pro, Stocky, Shopify Collective, Shopify Connector and Business Central in one call each.

## Rules I followed where E1 to E50 don't reach

### E51. Summer '24's page

- **Its cards.** A card's own words are its `title`, `shortTitle` (the heading the page renders), `descriptionHtml`, `ctas` (`title`, `url`), `signUpModal` and `productType`. `ariaLabel`, `ctaAriaLabel`, `handle`, `id`, the sizes, themes and media are no statement (E1).
- **Its Top 10 repeats cards of the later collections under other handles**, such as Markets, Managed Markets and Easy retail checkout. Each is placed by its own words (E10). The pairs I hold both of take the same lines: 15 and 24, 21 and 68, 23 and 39. The other Top 10 cards repeat features of later collections, which SH-58 holds: Shopify Magic, analytics, style settings and the Hydrogen Visual Editor.
- **The introduction card** ('Introducing the Summer ’24 Edition', entry 14) is the edition itself: CM-ONB-003 `core`, as its album (SH-E-09c20253, E2).

### E52. A CTA label with no CTA

The Markets cards 15 and 24 keep `ctaAriaLabel: 'Enter email address to get notified when Markets launches'`, but their `ctas` is `[]` and their `signUpModal` is `{}`, and the rendered page shows no button on them (lines 281 to 315 against the buttons at 300, 565 and 750). The label names a CTA the source no longer holds.
- I read it as no statement (E1) and placed the four Markets cards by their present tense: `core` on CM-MKS-001.
- If the coordinator reads the label as the edition's own 'Sign up to be notified' (E5), then 15 and 24 become `shows`, and 25 and 26 inherit it as their collection's cards (E5). CM-MKS-001 is `core` either way.

### E53. Managed Markets' cards

Markets Pro, renamed Managed Markets ('Markets Pro is now Managed Markets'), keeps E35:
- **CM-MKS-003.** It is `own-service` on SH-53's 'Our Merchant of Record capability' (SH-E-9e3f5c76), with `core` where the card links the admin's `settings/markets/pro/apply` (entries 69 to 72 and 76 to 79). Its two overview cards (21 and 68) link only shopify.com/markets/pro, so they are `own-service` alone. The line takes no scope: it is the offer itself (the ruling after SH-70).
- **A feature that comes with it** takes its own capability, `core`, scoped 'Managed Markets', as SH-55's DHL eCommerce labels are (E39). These are prices (CM-MKS-006), taxes shown in prices (CM-TAX-001), labels (CM-SHP-002), order edits (CM-ORD-002), payouts (CM-PAY-005), the order list (CM-ORD-001), captures and retries (CM-PAY-020), customs data (CM-SHP-020), the product index (CM-CAT-001), notices (CM-NTF-002, E42) and publication statuses (CM-MKS-001).
- **Duties stay on CM-MKS-003**, by CM-TAX-008's note: 'A merchant of record that handles duties for the store, such as Shopify's Managed Markets, is E's CM-MKS-003'. That covers 'duties and taxes in regional prices', 'Duties included in prices' and 'duties paid up front'. The taxes in prices take CM-TAX-001, whose definition includes how the store's prices show them. SH-34 put the changelog's duties-inclusive pricing on CM-TAX-008 (SH-E-53d52ef0). E41 and this batch follow the note, so the coordinator may align SH-34's line.
- **Restricted products stay CM-MKS-003's, not CM-CAT-009's.** CM-CAT-009's note names as a homonym 'prohibited product types', which 'restrict what a merchant may sell with that payment service'. Managed Markets' 'restricted from sale in certain regions' is the same kind.

### E54. Shopify Collective's features on other capabilities

By the ruling after SH-55, Collective is Shopify's own app. SH-40 places 'Let our AI-powered search inspire your journey' in Collective Discovery (SH-E-850b28ae) `own-service`. Each Collective card is CM-CHN-005 `own-service`. Where a card names a thing another capability holds, I gave that thing an `own-service` line too, each a reading:
- the supplier's shipping rates at checkout: CM-SHP-001. It isn't CM-SHP-004, whose rates are a third party's;
- the inventory confirmed between stores: CM-INV-001, as SH-55 put Stocky's transfers on CM-INV-006;
- the price lists a supplier shares with its retailers: CM-B2B-003's price lists assigned to business buyers.

The sourcing side is CM-CAT-010 `shows`, by its note (entry 58).

### E55. POS cards

- **POS itself.** Shopify POS is the platform's own client (E22): `core` on CM-POS-001. A link to `apps/point-of-sale-channel/...` also takes CM-APP-007 `core` (E7, as SH-50 and SH-53 did).
- **Receipts.** POS's digital receipts are CM-ORD-008 `core`, as SH-53 and SH-55 placed POS receipts (SH-E-4d179e85, SH-E-8c9fc235, SH-E-ab8c13e0). Their email opt-in is CM-CUS-007.
- **Staff credited with a sale** ('staff attribution', 'the name of the employee who completed the sale') is SH-50's Staff sales attribution, `core` (E46).
- **Devices.** POS Terminal and the Android hardware are CM-POS-002 `shows`, with no maker stated, and POS Go is `own-service` (E35). Stocky's smart grid extension is CM-POS-004 `shows`, as SH-55 placed Stocky's transfers extension, and its purchase orders are CM-INV-007 `own-service`.

### E56. The App Store and Theme Store for developers

The Developer cards on app discovery are the platform's own App Store, CM-APP-002 `core`:
- ads on its homepage, with 'soon on category pages' `shows`;
- the comparison page and category fields;
- listing translations;
- listing traffic in Google Analytics.

The 'theme install events' take CM-SFR-003 `core`. Google Analytics, where the developer reads the events, is the filler (E8). It isn't CM-ANL-007 (the store's commerce data) or CM-MKT-008 (orders credited to marketing): the data is the developer's, not the store's.

### E57. Billing

- **Billing currency.** 'Pay for your … plan in Japanese Yen' is CM-PLN-004, whose note names 'the billing currency'.
- **Billing payment method.** 'Pay … using SEPA direct debit' is CM-PLN-005, the means the platform charges.
- **Scope.** Both scopes join the countries and the plans with ` and ` (the ruling after SH-38).

### E58. Other readings of this batch

- **The Shopify Keyboard** (entry 8, group 'Keyboard swag drop') is `out`. It is a keyboard 'powered by Keychron', on pre-order from shopify.supply: merchandise, which does nothing on the platform for merchants, buyers, partners or developers (case 1).
- **A 'such as' list of kinds takes no line** (E4). 'manual payment methods at checkout, such as bank transfers, checks, and international wires' (entry 64) is CM-PAY-016 alone, so CM-PAY-030, not stated on Shopify, takes nothing (leads).
- **APIs named as what a thing is built with take no line** (the ruling after SA-41). These are 'using the Storefront API and Customer Account API' (66) and 'in the Storefront and Admin APIs' (3).
- **Sidekick** 'is live on thousands of Shopify stores' (entry 17). I read that as live on some stores, so `shows` (E5), as the earlier editions' Sidekick lines are (case 2).
- **Search & Discovery's cards** (29, 34 to 36) are `own-service` on CM-SFR-013, by SH-53's 'We’ve also made it easier…'. Each takes CM-APP-007 for its `apps/search-and-discovery` link. Semantic Search keeps SH-38's scope, `Shopify;Advanced`. Shopify Magic's AI ordering is CM-AIA-001 `core`, as Inbox's suggested replies are on CM-AIA-003 (SH-E-6a30460f).
- **The platform's own free themes** (Trade, entry 54; Rise for Japan, 75) are CM-SFR-001 `core` (the ruling after SH-53). Trade, 'designed for repeat and bulk purchasing' for 'a B2B store', also takes CM-B2B-001.
- **A B2B card takes CM-B2B-001** where its own words name business buyers ('B2B customer', 'B2B customers', 'B2B store', 'headless B2B storefronts'), as a kind of B2B selling (M-6 refined).
- **Unit pricing** (83) is CM-CAT-001 `core`: a price the platform keeps on the product (the ruling after SA-25), scoped 'EU;Switzerland' (case 6).
- **Qualities (E9):**
  - '10K+ categories and 2K+ attributes';
  - 'eight languages' of listings;
  - '2x increases in rate limits for all plans';
  - 'up to 10K ship-to locations per company';
  - '17 different Japanese fonts';
  - cookie banners in '32 languages'.

  These are claims, not qualities: 'as much as 57%', '1.5x faster', 'up to 4x more installs', 'billions of requests'.

## New things

Shopify's Editions are in English only, so no Arabic name is held. Each is an earlier batch's, and keeps its name. `caps --terms "admin search; global search; app version; roll back; rolled back; web performance; core web vitals; loading speed; staff attribution; employee who completed; attributed to; third-party CMS; content management; CMS; sanity"` finds no capability.

| New thing | Entries | Place of its own | Proposed domain, area, parent | Leads read |
| --- | --- | --- | --- | --- |
| App versions (SH-53's) | SH-E-db88ed0f: 'App configuration' 'is now a part of an app version and can be easily rolled back.', `core`, the platform's own developer tool, released (E46); its CLI part is CM-DVT-002 | None held: a shopify.dev guide | As SH-53: F, APP, under CM-APP-001, or beside CM-DVT-002 | CM-APP-010 (settings the platform holds per store, not an app's configuration), CM-API-008 and CM-API-009 (by the group's title 'Webhooks and Functions', not the card's), CM-DVT-001. SH-53's line reads `shows` |
| Admin search (SH-36's) | SH-E-ce87ea68: apps found 'in admin search results', `core` | None in this entry | As SH-36: decided with Zid's and Salla's admin search | CM-APP-002 (placed), CM-MKT-001 and CM-MKT-003 (by 'promotion', a homonym: an app's promotion, not a discount) |
| Web performance dashboard (SH-55's) | SH-E-18409847: 'Track how events impact store performance', its link `admin.shopify.com/reports/web_performance/loading_speed` and the help page `web-performance-dashboard`, `core` | An admin address under Reports, but the held router names no such route: its `analytics:reports:id` is `reports/:id`, one segment (`structures/shopify/admin-router/items.jsonl`). So I claim none | As SH-55: E, SFR, beside CM-OPS-003, or D, ANL, under CM-ANL-001 | CM-ANL-003 ('store performance', a homonym: sales, not web performance, as SH-55 found), CM-APP-004 (by 'app uninstalls', named in a list), CM-PLN-001 (by name) |
| Sanity integration (SH-50's) | SH-E-25e4d162: 'Liquid and Hydrogen storefronts can access third-party CMS data with support for metaobjects, currently available in the' Sanity Connect 'app', `extension-point`, filler Sanity | None in this entry: an App Store listing | As SH-50: E, CNT, near CM-CNT-003 | CM-CNT-002 (its metaobjects take an `extension-point` line beside it), CM-CHN-007 and CM-B2B-007 (by 'storefronts'): none holds a third party's content. SH-50's line reads `shows` |
| Staff sales attribution (SH-50's) | SH-E-f97a5ac3 and SH-E-6cc50442: 'easier staff attribution' on Shopify POS; SH-E-107a857a: 'the name of the employee who completed the sale' at POS checkout. Each is `core` | None in these entries: a POS checkout setting at `apps/point-of-sale-channel/settings/checkout-validations` | As SH-50: A, STF, under CM-STF-001 | CM-MKT-008 (orders credited to marketing, a homonym), CM-STF-001, CM-STF-004 (staff targets): neither. SH-50 and SH-53 read `shows`, SH-55 and this batch `core` |

## The CHANGES lines, and what I decided on each

Each line was read again against its source. Most repeat a change the coordinator has let stand after an earlier batch. They show as changes only because the model isn't amended yet.

**Repeats, kept:**
- **CM-MKS-003 gains `own-service`** (lines 36, 138, 143, 145, 149, 151, 158, 162, 164, 166): Managed Markets, by 'Our Merchant of Record capability' (SH-E-9e3f5c76; E35; the coordinator's check after SH-53).
- **CM-SFR-013 gains `own-service`** (lines 54, 62, 64, 67): Search & Discovery (the check after SH-53).
- **CM-CAT-008 gains `own-service`** (line 56): the Combined Listings app, now released, by SH-E-dc618719's 'new app for merchandising products' (the check after SH-54).
- **CM-CUS-010 gains `own-service`** (line 52): Sign in with Shop, Shop's own (the ruling after SH-34; the checks after SH-50 and SH-51).
- **CM-SEL-006 gains `own-service`** (line 59): bundles 'on Shop', Shop's own. The draft orders' bundles on the same line are `core`.
- **CM-INV-007 gains `own-service`** (line 95): Stocky's purchase orders, by 'We’ve introduced the option to' 'Edit' purchase orders in Stocky (SH-E-5b89aa16, placed so by SH-39).
- **CM-CHN-005 gains `own-service`** (lines 117, 119, 121, 123, 125): Shopify Collective (the ruling after SH-55).
- **CM-ORD-008 gains `core`** (lines 46, 75, 82): POS digital receipts, as SH-53's and SH-55's receipt lines.
- **CM-SHP-020 gains `core`** (line 165): 'Managed Markets now automatically enhances product descriptions shared with carriers, for faster clearance at customs.' That is customs data for shipments abroad, the cell's thing, scoped 'Managed Markets'. SH-36 put the EU customs identifiers of Managed Markets and Shopify Shipping there, `core` (SH-E-5669dc6b). If the coordinator reads Managed Markets' own features as `own-service`, the line changes support but not cell.

**This batch's own readings, kept and marked as readings (E54):**
- **CM-SHP-001 gains `own-service`** (line 118): Collective's 'accurate supplier shipping rates at checkout based on weight and location, rather than charging a flat rate', the rates buyers pay, worked out by Shopify's own app.
- **CM-INV-001 gains `own-service`** (line 122): Collective 'instantly confirms inventory between stores'.
- **CM-B2B-003 gains `own-service`** (lines 124, 126): Collective's price lists.

To settle the three: whether a first-party app's feature that touches another capability's thing takes that capability's line. Stocky's transfers on CM-INV-006 are the precedent. If the coordinator says no, the three lines go and their words stay in CM-CHN-005's readings.

## Entries I couldn't tell, placed where they most plainly belong

1. **The Shopify Keyboard** (SH-E-0381e647), `out`. To settle: whether merchandise the platform sells to developers is anything the class models. No capability holds it.
2. **Sidekick 'is live on thousands of Shopify stores'** (SH-E-f244d8db), `shows`. To settle: whether 'live on thousands' states a release to some stores (E5) or is a release marker for every store. If the latter, the line is `core`. CM-AIA-002 holds `core` from other lines either way.
3. **The Markets cards' CTA label** (SH-E-b10434e2, SH-E-cd9a9885, and with them SH-E-6aedfa28, SH-E-430bac12), `core` (E52).
4. **Collective's three other lines** (E54).
5. **Local payments in Japan** (SH-E-f44a40b4), CM-PAY-017 `core`, scoped Japan. CM-PAY-017's methods are 'offered through the platform's payment service', and the card doesn't say whether Konbini and QR codes come through Shopify Payments. Its help link is `payments/additional-payment-methods/activate-payment-methods`, and its CTA is the admin's `settings/payments` (`utm_feature=third-party-payments-japan`, no statement). If they are third parties' methods, the line belongs on CM-PAY-001.
6. **Unit pricing** (SH-E-d6ae89f8), CM-CAT-001 `core`. CM-CAT-013 (product pricing) is defined only by pricing apps, and CM-SFR-015 (storefront display) by display settings. Either would change its cell. To settle: whether a product's unit price is the product record's field or its display.
7. **The POS details page** (SH-E-5fa14188), CM-POS-001 `core`. 'A new design for POS details' could be read as the POS's own look, which the ruling after SH-37 would put `out` as it does the admin's frame. I read the products, orders and customers screens as the POS's own pages.
8. **Entry 50's 'using APIs to sync cash tracking reports with your accounting software'**, CM-PAY-028 `extension-point`, an unnamed third party through the platform's APIs. It could be read as the platform's own API for its own feature: `core` on CM-POS-003, which the card already takes.

## Structures whose items and sources disagree, or leave things out

- **Summer '24's Markets cards** keep a `ctaAriaLabel` for a CTA their `ctas` and `signUpModal` don't hold (E52). The rendering and the item agree (no button), and the label is the odd one out.
- **HTML entities in the text.** `Search &amp; Discovery` is held escaped in `descriptionHtml`, so a term or quote of 'Search & Discovery' doesn't match it. I named the app in my own words in `reading` and kept it out of `terms`.
- **Winter '24's group 20, 'App Growth'** (`pageSections/4/sectionGroups/20`), holds no product, so no entry holds it. SH-56 listed it with the Developer section's other titles.

## What the sources state that no entry holds (for the second stage)

- **Summer '24's `heroContent`:** 'Meet the most intuitive, most powerful, most unified Shopify yet', 'Scroll to explore 150+ updates' (line 7, `heroContent`). A general claim.
- **The media fields' own descriptions,** such as the Markets video's 'Shopify's Rohit Mishra, sits at a desk with a monitor displaying S…' (`primaryMediaDesktop.video.description`, entry 24's object). The structure drops them (`selection.tsv`). They describe the videos, which `editions-videos` holds.
- **Entry 28's 'powerful AI'** links the edition's own card `#ai-suggested-product-taxonomy`, in AI for commerce (SH-58's). That card holds the AI's line, and CM-CAT-004 here takes only the taxonomy.
- **Leads no line takes:**
  - CM-PAY-030, bank transfer, not stated on Shopify: 'bank transfers' among B2B's manual payment methods (SH-E-589768d7), named in a 'such as' list;
  - CM-ORD-003 (order statuses the merchant sets): 'the order's status' (SH-E-18950bc1), which is a payout's order, not a status the merchant sets;
  - CM-API-013 (account-level API): the checker's first lead for entries 4 and 74, by name only ('all, graphql'; 'rather, than'), neither of which names an account-level API.

## Problems with the brief or the script

- **The checker's brand NOTE** fires on the platform's own tools, services and clients: Shopify CLI, Shopify Functions, the Shopify App Store, Shopify Magic, Shopify POS and Shopify Payments (lines 2, 4, 14, 20, 30, 43, 48, 65, 77, 107, 155, 169). I read each again. Each is `core` by E3, E12.4, E22 or E24, and its reading names the words that place it.
- **The NOTE on a new thing whose entry has leads** points at the entry's first line. I read the leads it names (the table above).
- **The ruling's quote 'the Collective app' isn't found in held text** by the checker. I quoted SH-E-850b28ae's own words instead.
- No other problem.

## Where B-extent and the brief differ

None I relied on.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 86 of 86 entries, no problem, after the changes below.
- **The open question, decided** (the ruling after SH-57): a first-party app's feature takes another capability's line only where the app itself provides that capability's thing. Collective's supplier rates at checkout, its inventory confirmed between stores and its price lists are its own thing, CM-CHN-005's. Lines 118, 122, 124 and 126 are dropped, and their words stay in each entry's CM-CHN-005 line. Stocky's transfers stand.
- **E53's alignment is made.** SH-34's CM-TAX-008 line on Managed Markets' duties-inclusive pricing (SH-E-53d52ef0) is dropped: a merchant of record's duties are CM-MKS-003's, by CM-TAX-008's own note. The entry keeps its CM-MKS-003 and CM-MKS-006 lines.
- **The other cell changes stand,** each a repeat of a change the checks kept: the first-party apps' `own-service`, POS receipts, Managed Markets' customs data.
- **E51 to E58 stand for SH-58 to SH-67,** with E54 as decided above.
- **The open cases stand as marked readings:**
  - the Shopify Keyboard `out`, since it is merchandise, not a capability;
  - Sidekick 'live on thousands of Shopify stores' `shows`;
  - the Markets cards `core` (E52);
  - Konbini and QR-code payments on CM-PAY-017;
  - unit pricing on CM-CAT-001;
  - the accounting sync `extension-point`.
- **New things:** App versions, Admin search, Web performance dashboard, Sanity integration and Staff sales attribution, all named earlier and decided with the others. Their support differs from batch to batch, so it is decided with each thing.
- **Cost:** 28.3 million tokens over 110 requests, about 329,000 an entry. The context reached about 458,000 tokens, with 61 file reads.
