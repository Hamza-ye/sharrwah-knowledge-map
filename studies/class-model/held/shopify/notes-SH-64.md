# SH-64: notes

Batch SH-64: 82 entries of Shopify's `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, line 10, Winter 2026). They run from Marketing's ChatGPT XXL card (Shopify Product Network, SH-E-7cdac625) through Checkout, Operations, Shop app, B2B, Finance and Shipping, to the Developer collection's Agentic Commerce, Sidekick and Apps + Themes (SH-E-28c61fba). SH-65 to SH-67 hold the rest.

What I read:
- the brief (`briefs/H-held.md`);
- the digest, `held/rules/editions-page-data.md`, whole, its section 6 included;
- the last section of `held/review-H-rulings.md`;
- observed-sh's `README.md` and `structures/README.md`, `docs/READING.md` by its sections on fetch runs and structures, and `docs/GAPS.md` and `structures/REGISTER.tsv` by their Editions rows;
- the selection rows for `editions` and `editions-page-data`;
- B-extent's "Cells and evidence" and "Conventions from the dry run";
- the evidence map's Shopify line.

Earlier batches' notes, only where a case needed it:
- `notes-SH-53.md`, E23: Shop Pay apart from the platform, for the Shop Pay cards;
- `notes-SH-57.md`, E54: Collective's sourcing side, CM-CAT-010 `shows`;
- `notes-SH-63.md`, its opening lines: where SH-63 ended.

Precedent lines, read with `earlier`, `makers` and `grep` on the placements:
- the changelog's lines on Product Network, local payment methods, packages, DDP labels, HS codes, Shop Campaigns and Sidekick app extensions (SH-34 to SH-41);
- the Editions lines of SH-50 to SH-63, among them SH-62's 'More B2B-compatible apps' and SH-63's Sidekick app discovery and 'Improved theme discovery', the merchant twins of three of my cards.

`makers` found no maker statement for Shopify Product Network.

Counts:
- entries: 79 on capabilities only, 3 with a new line, none out;
- lines: 148, of which 97 `core`, 21 `own-service`, 12 `extension-point`, 12 `shows`, 4 `core;extension-point`, 1 `extension-point;shows` and 1 `outside`.

## The new things

- **`new:Bin locations`**, `shows`, one entry: SH-E-2a4aabb7, Operations' list, 'Bin locations in the Order Printer app'.
  - The card: 'Pick orders faster by assigning bin locations to each SKU using a CSV or the bulk editor in the' 'Order Printer' 'app.', with a help link to products/inventory/setup/bin-locations.
  - It is where in a location each SKU is kept, for picking.
  - Support: the bins are assigned in the Order Printer app, which has no maker statement held, so `shows`, the maker a gap (the digest's table). The app takes its own CM-ORD-009 `shows` line, as SH-E-34d0a6d8's pick lists do.
  - Place of its own: none held. It is a help page and a feature of an app, not an admin route, section, API group, plan line or app category.
  - Proposed: domain B, area INV, parent CM-INV-005 (inventory locations: locations, branches and warehouses). The coordinator may find it a part of CM-INV-005 instead.
  - Name: English only; the Editions hold no Arabic.
  - Searched: bin location; bin; pick list; packing slip; order printer.
- **Kept names, new lines:**
  - `new:Shoppable videos` (SH-55's name): SH-E-3613410c, 'Shoppable videos on Shop', `own-service`. It is Shop's own feature: 'Add shoppable videos to' 'Shop' 'and AI will optimize their distribution with built-in ranking and recommendations.' The earlier lines are `extension-point`, for third parties' videos through Shop Minis (Tolstoy, Videowise, Showday). This card names no third party.
  - `new:Quantity rules` (SH-50's) and `new:Quick order lists` (SH-53's), each `core`: SH-E-8e679815, 'Horizon themes work with B2B'. The card reads 'All Horizon themes support built-in volume pricing, quantity rules, and quick order lists.' Built into the platform's themes, so `core` (the digest's rule 22). The earlier lines are `shows`.

## Rules I followed that the digest doesn't state (E115 on)

- **E115: a merchant's own card disputes and cashback are the account's or the card's.** Disputes filed on the merchant's own Shopify Balance or Shopify Credit transactions go on CM-PAY-023 `core` and CM-PAY-025 `own-service`. They don't go on CM-PAY-009, whose disputes are buyers' chargebacks (a homonym). Credit's cashback is a quality of CM-PAY-025, not CM-LOY-003, which is buyers' cashback (SH-E-d38fd64f, SH-E-f1ad6192).
- **E116: one line per country for carriers.** A card naming carriers each in its own country takes one CM-SHP-002 `core` line and one CM-SHP-015 `shows` line per country, each with its scope and fillers (the ruling after SH-34, with rule 42; SH-E-83836ab1, SH-E-2cb0aaeb). DDP and DDU labels also take CM-TAX-008 `core`, as the changelog's SH-E-da6a8538 does, since no merchant of record is named.
- **E117: a Managed Markets card stated 'US only'.** Its CM-MKS-003 line takes 'US only'. Its features on other capabilities take 'Managed Markets and US only': payouts on CM-PAY-005, HS codes on CM-SHP-020 (SH-E-bb0211f7). Instant compliance checks stay on CM-MKS-003, as its restricted products do.
- **E118: the Shopify mobile app's own features.** Quick sale and the watch app are CM-SRF-001 `core`, the admin's own mobile client (rule 7). The payments they take go on their own capabilities: Tap to Pay on CM-PAY-021, payment links on CM-PAY-032 (SH-E-c52f377c, SH-E-5f128cfb, SH-E-e6b1e0c3).
- **E119: a fulfillment card's list.** Each item takes its line (E80). The card is CM-SHP-009, an order's 'in progress' status and its statuses CM-ORD-003, and its timeline notes CM-ORD-013 (SH-E-2efda9ff).
- **E120: Shop's products for each shopper.** Shop personalizing a store's Shop storefront 'with relevant products for each shopper' is CM-MKT-023 `own-service`, beside CM-CHN-002 `own-service` (E102 with E75; SH-E-45c8318b).
- **E121: Built for Shopify's prioritization, featuring and grace period.** These are CM-APP-002 `core;extension-point`, third parties' apps ranked and marked (E70, E86), each scoped 'Built for Shopify' (E101, as SH-E-fb94d7b6). The grace period's 60 days is a quality.
- **E122: developers' commerce agents.** Agents built on the Catalog API, MCP tools or Checkout Kit are CM-AIA-005 `extension-point`, the developer side of SH-63's Agentic cards. The checkout they present (Checkout MCP, Checkout Kit) is CM-CHK-001 `core`, as SH-E-5abe5931 placed Checkout Kit. The Dev Dash is CM-PTN-001 `core` (E87). The catalog feed 'soon' for 'select partners' is `shows` on the same line (rule 34; SH-E-2f39c99b).
- **E123: integrations by named third parties.** Integrations the card credits to third parties ('pre-built integrations by Patchworks, Fulfil, and Kensium'), with no interface of the platform named, are `outside` on CM-PAY-028. The integrators and the ERPs are its fillers (the check after SH-60; SH-E-fd1070f8).
- **E124: third parties' EDI apps.** Apps linked at App Store addresses whose companies the card names as the source of the work ('Sync EDI purchase orders from Crstl and SPS Commerce …') are `extension-point`, those companies its fillers (SH-E-d7ef6efa). An app whose words show no third party doing the work stays `shows` (the ruling after SH-43).

## Entries I couldn't tell, and what would settle each

- **SH-E-c71f44ea, 'Reminders for Shop Pay subscriptions':** `core` on CM-PAY-022 and CM-SEL-001, as Shop Pay in the platform's checkout. Its help link is in the Shop channel's manual (online-sales-channels/shop/manage-shop-store/products-and-collections#subscriptions), which could make the reminders Shop's, `own-service`. The help page, not read, would settle it.
- **SH-E-c52f377c, quick sale:** placed on CM-SRF-001. Selling in person is CM-POS-001's thing, but that capability's name keeps it to the POS app.
  - Its payment links make CM-PAY-032 held on Shopify for the first time ('accept payments with Tap to Pay or payment links').
  - The coordinator decides whether the mobile app's in-person selling joins CM-POS-001.
- **SH-E-c233667e, 'Shop Pay works with Global-e':** CM-PAY-011 `extension-point`, Global-e its filler. Its Try it link opens a third-party provider's page in the admin (settings/payments/third-party-providers/34635777), and Managed Markets isn't named. If that provider page is Managed Markets', the line would be CM-MKS-003 `outside`. The provider's id isn't named in any source I read.
- **SH-E-fd1070f8, ERP integrations:** `outside` by the rule after SH-60 (E123). The Winter 2024 Edition's Acumatica integration (SH-E-6b5615a1) is `extension-point`, so the two are to be aligned.
- **SH-E-d7ef6efa, EDI:** `extension-point` (E124). If the coordinator reads Crstl and SPS Commerce only as the apps' names, the ruling after SH-43 makes it `shows`, the maker a gap.
- **SH-E-2efda9ff:** CM-ORD-003 and CM-ORD-013 held nothing on Shopify. Both lines make a cell held. CM-ORD-003's note keeps apart only the buyer's order status page, and Shopify's fulfillment statuses are not customizable as Salla's statuses are. The checker's first lead, CM-OPS-004 (store status), is the system status report: not this entry's thing.
- **SH-E-45c8318b:** the CM-MKT-023 line (E120) makes that cell held. E75's Search & Discovery lines would make it held as well, once amended.
- **SH-E-2a4aabb7:** `new:Bin locations`, or CM-INV-005's.
- **SH-E-c8e73f6e, Shop order tracking:** the source disagrees with itself, not with the item. Its `title` reads '18 more countries', its `headlineTitle` '21 more countries', and its description lists 21 countries. The scope holds the 21 the description names.
- **SH-E-066318aa, Shopify Collective:** 'now available in 35 additional countries' names none of them, so the line takes no scope. Its section, B2B, gives no CM-B2B-001 line: business buyers aren't named (rule 2).
- **SH-E-28c61fba:** CM-DVT-001 for the developers' Web Vitals data, and CM-APP-006 for the app's pages in the admin it measures. It isn't the storefront's `new:Web performance dashboard`.
- **SH-E-7cdac625, Shopify Product Network:** CM-CHN-005 `shows` (no maker held), 'US only' its scope. The store's search, collections, emails and post-purchase pages, where the app surfaces products, take no line (E81). The checker's leads CM-CAT-005 (brands) and CM-PTN-009 (commission) are homonyms: other merchants' brands, and the merchant's own commission.
- **SH-E-67b2a072, 'Sidekick recommends apps':** its lines are those of its merchant twin, SH-63's SH-E-eb93704f (CM-AIA-002, CM-APP-002, CM-APP-001). Its CM-APP-002 line takes 'Built for Shopify' as its scope (E101), since the card names those apps' prioritization and badges.

## Leads no line takes

- SH-E-6eb3aade: CM-ONB-004 (onboarding) is the checker's first lead, but the onboarding is Shopify Payments' own, CM-PAY-002's part.
- SH-E-71d4650c and others: CM-MKS-009 (countries) is the checker's lead by 'countries'. The countries are each line's scope, not reference data.
- SH-E-4ec913ee: CM-B2B-005, shopping lists, held nothing. The list ends 'and more', so its items take no line (E80, as SH-62's twin). Quote requests and custom buyer roles are leads too.
- SH-E-d8190ffb: CM-API-010 (conditional webhooks), the lead by 'conditions', is no lead.

## What a source states that no entry holds

I read no run step, answer or page beyond the entries' own text. No leads for the second stage.

## Problems with the brief or the script

- `held_entries.py batches` takes no `--platform`. It builds the batches, so no agent needs it.
- None else.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 82 of 82 entries, no problem.
- **The `CHANGES` stand.** Each follows the digest's table, its rules or an earlier line. The four cells held for the first time stay as marked readings: payment links from quick sale, Shop's products for each shopper, and the order statuses and timeline notes.
- **CM-PAY-028's two third-party integrations differ by their own words, and both stand:**
  - 'pre-built integrations by Patchworks, Fulfil, and Kensium' names no platform interface, so `outside` (E123; B-extent);
  - Acumatica's integration (SH-E-6b5615a1, SH-55) is 'leveraging our full suite of B2B features', the platform's own features named as what it works through, so `extension-point`.
- **The rules E115 to E124 stand** and join the digest's section 6.
- **The new thing** Bin locations is `shows`, in the Order Printer app with no maker held, and has no place of its own. Shoppable videos, Quantity rules and Quick order lists keep their names. Their supports are decided with each thing.
- **Open, as placed:** Shop Pay's subscription reminders `core`; Global-e on CM-PAY-011; the EDI apps `extension-point`; the card that counts 18 countries in its title and lists 21.
- **Cost:** 14.9 million tokens over 79 requests, about 182,000 an entry. The context reached about 336,000 tokens.
