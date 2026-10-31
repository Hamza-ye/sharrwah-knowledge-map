# SH-60: notes

**The batch.** 103 entries of Shopify's `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, line 8, the Winter 2025 Edition):
- the merchant collections Wholesale (15 cards, entries 1 to 15), Global (10, entries 16 to 25), Shipping (12, entries 26 to 37), Operations (20, entries 38 to 57) and Finance (7, entries 58 to 64);
- the developer collections Storefronts (12, entries 65 to 76) and Extensions (27, entries 77 to 103).

None of these collections has a description of its own (`descriptionHtml` is empty), so each card is read by its own words, its links and its collection's title. The page's two summaries, Top updates (`collections/0`) and the developer Top updates (`developerCollections/0`), are `isSummary: true` with no products; they are read with the cards they link (E69) and go to the second stage (the digest's rule 37).

**What I read.** The brief; the digest `held/rules/editions-page-data.md`, read again after it changed on disk during the run (its new section 6, E59 to E76, and 'The next batches number their rules from E77', which the coordinator's message also asked); the last section of `held/review-H-rulings.md`; `notes-SH-59.md`, lines 1 to 57 (its batch and its rules, as the coordinator asked); observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` (its headings and Published section: nothing on the Editions), `structures/README.md`, and the `REGISTER.tsv` row for `shopify/editions-page-data`; the selection rows for `editions` and `editions-page-data`; B-extent's "Cells and evidence" and "Conventions from the dry run"; the evidence map's observed-sh section.

From other batches' notes, only where the digest sends to a case:
- `notes-SH-57.md`, lines 69 to 80: E58, for the digest's rule 46 (a B2B card takes CM-B2B-001 where its words name business buyers);
- `notes-SH-58.md`, lines 62 to 73: E65 to E68, the cases behind the digest's section 6 (E66, a card's staff permissions; E68, places named in a card's news);
- `notes-SH-54.md`, lines 73 to 79: E31, the lead card behind the digest's rule 34.

Earlier lines were read through `earlier` and with `grep` of the placements on a feature's name or capability: SH-59's twins (its lines 75 to 77 and 81 to 91), SH-57's Summer 2024 Managed Markets cards (its lines 139 to 141, and the lines citing SH-E-88ff9045, SH-E-c2d7fa41, SH-E-d69af767 and SH-E-3209d8f4), deposits, Klarna, ShipBob, CM-SHP-015's carrier lines, Semantic Search, Admin languages, Admin search, Sidekick, `new:Finance`, Shopify Credit and Capital, CM-MKT-003, CM-MKT-009 and Collective's CM-CHN-005 and CM-CAT-010 lines. `makers` was run once, for Shopify Capital (SH-E-136aca69, 'We've just released Shopify Capital for merchants in France.', SH-35's `core`).

**Count.** 103 entries: 99 `capability`, 3 `new`, 1 `out` (entry 42, the admin's loading speed). They take 186 lines:
- `core` 126;
- `extension-point` 35;
- `own-service` 13;
- `shows` 7;
- `core;extension-point` 4.

## New things

Each is a thing an earlier batch named, so I kept its name. The Editions are in English only, so no Arabic name is held.

- **`new:Admin languages`** (entry 17, SH-E-19b0178e, 'A more localized Shopify'): 'Shopify now offers merchants in Europe and Japan better translations in the admin', scoped `Europe;Japan`, `core` (the platform offers it now; SH-34's line was `shows`). It is the admin's own interface language, one new thing across the platforms (the ruling after SA-49; the digest's section 4). Its place of its own is SH-34's Admin languages; this card has none. Proposed domain A, under the merchant's account, as the coordinator decides it with SH-34's and Salla's `العربية / English`. Terms searched: 'admin language; interface language; display language; translations in the admin; localized admin; admin translation' (no capability).
- **`new:Admin search`** (entry 47, SH-E-b9413d62, 'Powerful search everywhere'): 'Search is smarter across Shopify, including the Shopify app and the variable picker in Shopify Flow.', `core` (SH-36's lines were `shows`; the digest's section 4 says it is decided with Zid's and Salla's admin search). This card has no place of its own. The leads CM-SFR-013 (the buyers' storefront search, another thing) and CM-AUT-001 (Flow, named after 'including') take no line. Terms searched: 'admin search; search the admin; search across the admin; global search' (no capability).
- **`new:Finance`** (entry 58, SH-E-14db54ab, 'Unified finance everywhere'): 'a new, comprehensive finance home', linked to admin.shopify.com/finance, `core`. It is the admin's Finance section, the new thing SH-12 and SH-39 named (SH-E-f18a277e, SH-E-b9245d10, SH-E-44c35194): a container over Capital, Credit, Balance, Payments, Bill Pay and Taxes, whose place of its own is the admin route SH-12 read (finance:dashboard, titled Finance). The leads CM-PAY-025, CM-PAY-026 and CM-TAX-009 hold pages under that address, not the section. Proposed domain C, area PAY, no parent. Terms searched: 'finance home; Finance; finances'.

Three near-new things are placed on the nearest capability, each a reading:
- **Sitemaps** (entry 76): no capability names sitemaps ('sitemap; sitemaps' found none). I placed them on CM-CNT-007 (SEO) `core`, since a sitemap lists the store's pages for search engines. Hydrogen's Sitemaps API is no API group of the reference, so it is no place of its own.
- **Session recordings** (entry 103): no capability holds them ('session recording; heatmap'). The card is apps' pixels, CM-MKT-009 `extension-point`.
- **Custom IDs and upserts** (entry 56): no capability holds them ('custom id; upsert; external id; identifier'). I placed them on CM-API-001 `core`, as the cell holds the API's conventions (Global IDs).

## Rules I followed that the digest doesn't hold (E77 on)

- **E77. Managed Markets' features.** A feature goes on its own capability, scoped 'Managed Markets' (the digest's rules 29 and 45). Where the card's title names Managed Markets, it also takes CM-MKS-003 `core`, with no scope, as SH-57's SH-E-88ff9045, SH-E-c2d7fa41 and SH-E-d69af767 did:
  - entry 22 ('Order editing works with Managed Markets', also E74) and entry 23 ('New payment options for Managed Markets');
  - entries 19 (insurance) and 21 (Shipbob) name it only in their descriptions, so they take only their feature's line.

  Rule 45's 'its other features go on their own capabilities' could also be read to give no CM-MKS-003 line to 22 and 23. The coordinator decides.
- **E78. A B2B line's support is that of the B2B thing the card shows** (E58; the digest's rule 46).
  - It is `extension-point` where apps do it for business buyers: entry 2 (an app's shipping message 'just for B2B customers'), 4 (apps add 'features for B2B customers'), 11 ('18 more apps now compatible with B2B') and 94 (pixels for B2B and DTC).
  - It is `core` where the platform does it: entries 1, 5, 7, 9 and 10.
  - This gives CM-B2B-001 its first `extension-point` (CHANGES below).
  - Entry 6 names companies, not business buyers, so it takes CM-B2B-002 rather than CM-B2B-001. Entry 3 names only 'sales staff' (see the cases left open).
- **E79. Twins across sections.** The Wholesale cards 2 and 3 are SH-59's Checkout cards 52 and 53 (SH-E-527880a0, SH-E-ad3dbd9b) in other words. The developer cards 82, 83, 85 and 86 are the merchant cards of SH-59 and this batch: SH-E-527880a0 and 2; SH-E-ad3dbd9b and 3; SH-E-32015411; SH-E-3f1880a2. Each keeps its twin's capabilities and terms, its support and scope by its own words (the digest's rule 4; E61). Entry 70, 'Enhanced accelerated checkout buttons', is the developer side of SH-59's SH-E-a6edb57a. As SH-59's E74 had it for that card, its 'support Shopify Functions and bundles' takes no line.
- **E80. A list in a card's news.**
  - An exhaustive list of what the news now covers takes a line each (E68): entry 26's 'applied across subscriptions, draft order invoices, and imported orders' gives CM-SEL-001, CM-ORD-005 and CM-MIG-001.
  - A list introduced by 'including', 'like' or 'such as', or ending 'and more', takes none (rule 51). The cases are entries 11, 36, 47, 51, 52, 59, 60, 88, 92 and 100.
  - A place where the card's own news happens takes its line (E68). The cases are:
    - the Shopify app's home screen (49, CM-SRF-001);
    - POS location settings (37, CM-POS-001);
    - Hydrogen's carts (72, CM-CHK-002);
    - the logged-in checkout (89, CM-CHK-001).
  - A place named as where only takes none: 'from the admin or the Shopify app' (58).
- **E81. A first-party app's card is read by its title.** Where the title names the app's own feature ('Metaobject triggers in Flow', 'Return automation in Flow'), the platform's thing it acts on takes no line (the digest's rule 16): CM-CNT-002 and CM-RET-003 take none. Where the title names the platform's feature that the app automates ('Automate new account setup', entry 6), that feature's capabilities take `core` lines beside the app's `own-service`. Those are CM-B2B-002, CM-B2B-003 and CM-B2B-006, the last as its cell's permission 'Assign staff to company locations' names it.
- **E82. Collective's work with third parties.** 'Automate Shopify Collective returns, with or without 3P apps' (entry 13) keeps Collective's own returns to suppliers in its CM-CHN-005 `own-service` line (the ruling after SH-57). The third parties' apps take CM-RET-003 `extension-point`, a cell that already holds it. Collective's order risk flags (15) stay in its CM-CHN-005 line, as its rates and inventory do.
- **E83. A card whose title names the API it extends** ('More content in GraphQL APIs', 67; 'GraphQL orderCreate API', 102; 'Sync catalogs with custom IDs', 56) takes CM-API-001 `core` beside the capabilities of the things the API now covers (the digest's rule 17; E67).
- **E84. Pixels.** Events the platform sends to pixels are `core` on CM-MKT-009 and on the events' capability, as its webhooks are (the digest's rule 17): entry 95, CM-CHK-001. Pixels that developers build or customize are `extension-point` (94, 103), as SH-50 to SH-52 placed Web Pixels Extensions.
- **E85. Hydrogen.** A Hydrogen card takes CM-SFR-011 `core` (its title's Hydrogen, the platform's own headless framework), and the thing it says Hydrogen now supports takes its line (E74). The cases are gift cards (72, CM-LOY-002), consent (73, CM-TRU-006) and a CLI flag (74, CM-DVT-002). The variants a hook displays take none (75).

## Entries I couldn't tell, and what would settle each

1. **The new analytics' rollout.** Its own card (43) says 'now rolling out to everyone', and the summary rolls it out (E69), so 43 is `shows`. Cards 10, 44, 45 and 49 name 'the new analytics' or 'New analytics' and state no limit of their own, so I kept them `core`. They sit in their collection's flat list, which gives 43 no structure of a lead card (rule 34; SH-54's E31). If the coordinator reads 43's limit into the cards that name its product, they are `shows`.
2. **Customer account extensions** (entry 4): 'Customer account extensions are now available' is `extension-point` by its own words. The summary's 'We're rolling out … customer account extensions' links SH-59's card (#customer-account-extensions), not this one. If E69 is read by feature rather than by card, entry 4 is `shows` too.
3. **Shipbob** (entry 21, the CHANGES on CM-SHP-002): 'Buy and print Managed Markets shipping labels from Shipbob.' I read a third party reaching the platform's labels, so `extension-point`. No interface is named, so `outside` is the other reading. A held page on the integration (its link, support.shipbob.com, isn't held) would settle it.
4. **'(wholesale)' in a title** (entry 3): its `title` reads 'Functions work with draft orders (wholesale)', and its words name no business buyer. I gave it no B2B line. If the coordinator reads 'wholesale' in a card's own title as naming B2B selling, it takes CM-B2B-001 (see the problems).
5. **Shopify Capital** (entry 64): `core`, since it names the admin ('submit required application documents directly within the admin'). The digest's rule 21 keeps Capital `shows` where only its brand is named. A maker statement would make it `own-service`, as Shopify Lending's is (SH-E-797024ee). The one `makers` found, 'We've just released Shopify Capital' (SH-E-136aca69), was SH-35's `core`.
6. **Semantic Search in more languages** (entry 16): no scope, since the card states none. The changelog's post on the same news (SH-E-f64dc5b2) is scoped 'Shopify plan or above'. If a twin's scope may carry across structures, it takes that scope.
7. **orderCreate** (entry 102): CM-ORD-005 (orders created outside the checkout) is the nearest. CM-ORD-001 (orders) is the broader reading.
8. **Entry 6's B2B lines** (E81): if the coordinator reads the assignments as what Flow names in passing, CM-B2B-002, CM-B2B-003 and CM-B2B-006 drop, leaving CM-AUT-001 alone.

## A structure whose items and sources disagree

- The developer summary (`developerCollections/0`) says 'Functions work with carts of up to 200 items', linking #dynamic-scaling-for-execution-limits. That card (entry 84) says 'Function execution limits now scale with carts that have over 200 lines'. The two differ ('up to' against 'over'). I took the card's words as the quality.
- The `title` field of the twins carries a suffix the shown `headlineTitle` lacks: '(wholesale)' (entries 2 and 3) and '(developer)' (82, 83 and 86). The suffix reads as the source's label for which twin a card is. The digest's rule 1 counts `title` among a card's words, so its terms stand, but see case 4.

## What a source states that no entry holds (for the second stage)

- The Winter 2025 Top updates (items.jsonl line 8, `collections/0`, `isSummary: true`) and the developer Top updates (`developerCollections/0`): headings with no products (the digest's rule 37). The merchant summary names this batch's cards 1, 41, 42 and 43. The developer summary names 72, 74, 75, 76, 81, 84 and 68.
- The cards' links outside the held sources (rule 53):
  - www.shopify.com/enterprise/blog/draft-orders-winter-editions (entries 1 to 3; `held_index.py`: not held);
  - www.shopify.com/enterprise/blog/b2b-customer-account-extensions (4);
  - shopify.com/blog/organizations-and-user-management (38, 40);
  - shopify.com/blog/admin-performance-improvements (42);
  - shopify.com/blog/shopify-tax-simplified-vat-compliance (63);
  - support.shipbob.com's Shopify-Managed-Markets article (21).

  Only the first was looked up. The blog pages would say how far the Winter 2025 B2B draft-order features and role-based access had rolled out.

## The checker's CHANGES, read again

- **CM-AUT-001 gains `own-service`** (lines 17 and 95 to 101: entries 6 and 50 to 55). Shopify Flow is `own-service` on its own features (SH-E-0678ff26; the digest's section 3; the ruling after SH-55 aligned 38 lines). The cell isn't amended yet. Kept.
- **CM-B2B-001 gains `extension-point`** (lines 9, 13, 30, 170: entries 2, 4, 11 and 94). Apps for business buyers: B2B-compatible apps, customer account extensions, checkout extensions and pixels (E78). Kept. Line 9 is the weakest: its B2B words are in a 'For example'.
- **CM-CHN-005 gains `own-service`** (lines 31, 33, 35, 36: entries 12 to 15). Shopify Collective is `own-service` (SH-E-850b28ae; the digest's section 3). Kept.
- **CM-MKT-003 gains `core` and becomes held** (line 147: entry 81). 'Discount functions can now power up to 25 automatic discounts': automatic discounts, applied without a code (the digest's rule 47). SH-58's E67 and earlier Editions lines (SH-E-a890e154, SH-E-8c1d6bd3, SH-E-00357e3e) placed the same. Kept.
- **CM-SFR-013 gains `own-service`** (line 37: entry 16). Search & Discovery is `own-service` (SH-E-9b869699; SH-57's E58). Kept.
- **CM-SHP-002 gains `extension-point`** (line 45: entry 21, Shipbob). Kept, open (case 3).

## The checker's notes, read again

- **`core` on a product named with the platform's brand** (lines 10, 40, 41, 92, 107, 108, 110 to 112, 115 and 167). Each is the platform's own by a digest rule:
  - Shopify Functions, a developer tool (rule 17);
  - Shopify Tax (rule 7);
  - the Shopify Theme Store, the platform's own marketplace, as the App Store is;
  - Shopify Balance (rule 25);
  - Shopify Bill Pay at `finances/billpay` (section 3);
  - Shopify Capital in the admin (case 5);
  - the Subscriptions Reference app, a developer resource (rule 17).
- **`own-service`** lines: Flow, Collective, Search & Discovery and Shopify Credit, each by the digest's section 3.
- **New things with leads** (lines 39, 91, 106): their leads' cells were read; none holds the thing (above).
- **First leads that hold nothing**:
  - CM-MKS-009 (lines 50, 60): the countries are those lines' scopes, market data, not the entries' thing;
  - CM-CNT-010 (line 83) and CM-APP-010 (line 185): leads by a shared word only ('product, url'; 'integration').

## Problems with the brief or the script

- The coordinator's message numbered this batch's rules E60.1 on, then E77 on. The digest's section 6 says E77 on, and I followed it.
- The digest's rule 45 and SH-57's practice differ on whether a Managed Markets feature card also takes CM-MKS-003 (E77).
- The twins' `title` suffixes '(wholesale)' and '(developer)' look like the source's own labels for twins, though the digest counts `title` among a card's words. A rule on whether such a suffix names the card's thing would settle case 4.
- No problem with the scripts. The checker's final line: '103 of 103 entries placed; 0 problems'.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 103 of 103 entries, no problem.
- **One line corrected:** Managed Markets' labels 'from Shipbob' (line 45) are `outside`, with Shipbob as filler. B-extent's `outside` is a third party doing the work 'with no interface of the platform named', which is the card's case. So CM-SHP-002 doesn't gain `extension-point`.
- **The other `CHANGES` stand:**
  - Flow's, Collective's and Search & Discovery's lines are `own-service`, by the digest's table.
  - CM-B2B-001's `extension-point` comes from apps that serve business buyers (E78). Entry 2's case, an example inside its card's news, is a marked reading.
  - CM-MKT-003 is `core` for up to 25 automatic discounts (E67).
- **The rules E77 to E85 stand** and join the digest's section 6.
- **The new things** keep their names: Admin languages, Admin search and Finance. Their supports differ between batches, and are decided with each thing.
- **Open, as placed:** the rollouts read card by card (E69); Shopify Capital `core`; Semantic Search with no scope.
- **Cost:** 16.9 million tokens over 78 requests, about 164,000 an entry. The context reached about 405,000 tokens.
