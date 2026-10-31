# Held pass, Salla, batch SA-14: notes

80 entries: the last 64 of `dashboard-app-routes` (items at items.jsonl lines 3093 to 3691: the apps domain, inventory, manage, payments, products, reports_mfe, shipping, users, utils, billing, mushammir-package, offers, themes-editor and media, mostly routes inside their pages' lazy chunks), then the first 16 of `dashboard-edu` (items.jsonl lines 1 to 16). Evidence at observed-sa@b0bd0b163.

**Placed:** 57 entries on capabilities, in 65 lines; 0 `new`; 23 `out`, in 13 lines. 78 lines in all.
- 8 entries take more than one line: 5 (two), 17 (three), 27 (five), 30, 33, 66, 67 and 68 (two each).
- 60 lines support `core` and 5 `shows`: 30's two lines (fulfilment centres, an unreleased flag), and the edu banners of Salla Chat (66), Digital Gift Cards (67) and Store Blog (68). No `own-service`, `extension-point`, filler or quality.
- 33 lines carry a scope: a route's guard feature (`webhooks`, `custom-urls`, `size-guides`, `brands`, `products-filters`, `shipping-ticket-system`, `shipping-fulfillment-centers`, `settings-control-panel`, `billing-native`), a route's plan gate (`special;pro`), or an edu row's `allowedPlans`.
- The `out` entries: the Algolia client's 11 request paths (39 to 49, one line), two cookie libraries' `/` (55, 59), four VML shapes (35, 56, 60, 64), two engine.io clients (53, 61), two grammar parsers' node types (62, 63), a progress bar's class names (58) and a form's validation error (57).

Entry numbers below are the batch's order (`held_entries.py show --batch SA-14`). Bundles are cited by their record. The page chunks are in `raw/runs/20261008T121539Z-dashboard-bundles-chunks2/fetch.warc.gz` (entries 1 to 53), `…-chunks3` (54 to 61), `…-chunks4` (62, 63) and `…-chunks5` (64), at the offsets the readings give.

## How I read the route entries

I kept SA-7's eight rules and the coordinator's checks after SA-8 to SA-13. Nearly every route here sits inside a page chunk, so `show --code 600` printed the router but not always the guard. I printed the batch's 31 records once each into my scratch folder, then searched them all in one pass for each page's guard (`mode:"page"`, `feature:`, `plan:`) and for its resource page's `basePath`, which gives each relative route its address. Each page's title comes from its app's locale breadcrumbs (`structures/salla/dashboard-translations/en/*.json`).
- **A feature in the page's resource configuration is the route's gate** (16, 17, 19, 20). The size charts, brands and filter options pages pass `feature` beside the staff permissions in the configuration of their resource page, not on a button. I read that as the page's gate, so its scope. The constants' values are in the products bundle (`…-chunks1/fetch.warc.gz@36502660`): `PRODUCT_SIZE_GUIDES="size-guides"`, `PRODUCT_BRANDS="brands"`, `PRODUCT_FILTERS="products-filters"`. This is a reading. A run of a Basic store at those addresses would settle whether the page is withheld.
- **A feature on a button isn't the route's scope,** as SA-13's notes say: the branches' add button `PRODUCT_BRANCHES` (3, 4, 14, 15), the staff's add button `USER_ADVANCE_MANAGEMENT` (36), and the tickets' add button (the tickets page's own guard names the same feature, so 27 and 28 take it from the guard).
- **The shipping restrictions page has a plan gate.** The guard of `rules-M-APPI25.js` (@14355779) is `M({mode:"page",permission:["shipping_rules_management"],plan:["special","pro"]})`. It names plans, so 27's restrictions line and 32 take the scope `special;pro`. SA-13 placed `/shipping/rule/*` with no scope, reading the plan only from the Basic store's page. The same guard would give that line `special;pro`. The coordinator may align them.
- **An entry that stands for routes of several pages** takes a line per page, each with its own item's scope: 5 (a webhook's and a custom link's `new`), 17 (`new` for size charts, options and brands) and 27 (`/` of five shipping pages).
- **Tab objects** (8 to 10, keys `id`, `label`, `path`) are the wallet page's tabs. Each is the label of its route (11 to 13), so it goes where the route goes (SA-7's rule 4).
- **Links in the performance report** (21 to 26, keys `label`). These are not routes. They are the calls to action of the recommendations in `reports_mfe`'s store performance report (`zE="store_performance"`, @13972700). Each one links to another app's page, such as `primary:{label:"rec_total_sales_cta",path:"/marketing/reorder-reminders/new"}`. Each names a place, so it isn't a bare UI string. It goes on the capability of the place it links to, as SA-7's rule 3 places a redirect. The feature names and descriptions are quoted from `reportsv2.json`.
- **The wallet's tabs:**
  - Store wallet is CM-PLN-006, the cell's Wallet at `/payments/wallet`;
  - Online payments ('Online payment payouts') is CM-PAY-005, the e-payments balance, which that cell's note keeps apart from the store balance;
  - Cash on delivery ('Cash on delivery payouts') is CM-PAY-029, whose cell already cites the wallet's cash-on-delivery summary.
- **DNS** (2) is CM-SFR-009, not CM-SFR-008. Its cell is the DNS records of the store's domain. No lead named it; `caps --terms "DNS"` found it.
- **Leads set aside:**
  - CM-PAY-020 and CM-RET-002 (`transaction_id`: the store wallet's transactions);
  - CM-ORD-014 (`reorder`: the cell's homonym);
  - CM-CHK-002 and CM-CHK-007 (`carts`: the link is to cart reminders, CM-MKT-022);
  - the Algolia paths' CM-TRU-001, CM-MKS-008, CM-API-007 and CM-SFR-013 (`security`, `languages`, `batch`, `search`), which are the client's words.

## Rules the edu lines follow, for SA-15

No batch has placed `dashboard-edu` before. `SA-15` holds the rest of it, rows 17 to 73, and hasn't run. These lines follow SA-32's reading of the same table's rows in `plan-gates` (its rules 4 to 6), so the two structures agree:
1. **What a row is.** One row is the education banner Salla keeps for one dashboard address (`category`, `contentKey`), with the plans its feature is allowed on (`allowedPlans`). The banner's feature, as its key's `feature_name` names it in `structures/salla/dashboard-translations/en/reminders.json` (and `ar/`), is what the plans are stated for. So the line goes on the banner's feature, not on the list page at the address: `/customers`' 'Add New Customer' is CM-CUS-001 and `/customers/groups/new`'s 'Bulk Customer Group Management' is CM-CUS-003. A row whose key has no `feature_name` (`edu.apps_all`) goes on the page at its address.
2. **Scope:** `allowedPlans` as written, `;`-separated in its order (`plus;team;special`), never mapped. The same bundle maps `team` to `pro` (`raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz@39521943`, SA-32's notes), and each line says so. A row with no `allowedPlans` has no scope (67).
3. **Supports,** by the features list's state for the banner's feature (the brief's ruling on flags):
   - `core` where it is Salla's own released feature;
   - `shows` where the model's flag for it is unreleased (`store-blog`, `wallet-gift-card`) or the thing is listed unavailable (Salla Chat, the coordinator's ruling after SA-8).
4. **App pages** (`/apps/view/<id>`) take a second line, CM-APP-002 `core`: the App Store's page for one app. No maker is stated, a gap. They aren't embedded pages, so they take no CM-APP-007 line (SA-32's rule 6).
5. **Terms:** the segment of `category` or `contentKey` that names the thing (`mahally`, `customers`, `currencies`, `logs/export`), or none (`/apps/view/*`). The banner's name is in `reading`, since the checker takes terms from the entry's own text.
6. **The row's other keys go in `reading`:** `hideWhenEntitled` (the banner is hidden once the store is entitled), a `banner` action (Salla Point's video). The help article (`action.url`) isn't quoted. A mark in a `feature_name` ('Digital Gift Cards *additional fees') is the locale's, not the entry's, so it isn't a quality. It goes in `reading` and in the leads below.
7. **Where the edu plans and the features list differ,** the line keeps the edu row's plans and names the difference: 71 (basic allowed, while `store-pages` lists plus, pro, special) and 77 (team and special, while `advance-audit-log` lists plus, pro, special). SA-32 found the same differences.
8. **No CM-PLN-001 line per row,** as SA-32's rule 9 gives none. The leads to CM-PLN-001 (by `plus`, `special`) are a word every row holds.

## Entries I couldn't tell, and what would settle each

- **21 to 26, the performance report's links.** I placed each on the capability of the place it links to. A second line on CM-ANL-003, for the report's recommendations themselves, is the alternative. The entries' own words are only a label key and a path, so I gave none. The coordinator may want one line for the recommendations as a feature of the report.
- **10 and 13, cash on delivery in the wallet.** These are on CM-PAY-029. The page calls them payouts ('Cash on delivery payouts'), and 'Your online payment and cash on delivery payouts are transferred to your bank account according to your plan's payout schedule.', so a CM-PAY-005 line is the alternative. I kept CM-PAY-005 for the e-payments balance, as its note reads.
- **16, 17, 19, 20, a feature in the page's configuration as its gate** (above). If the coordinator reads it as not a gate, these lines lose their scope.
- **17, the options page at `/products/options/templates`.** Its chunk (@13762527) imports its configuration and names no feature, so its line has no scope.
- **33, the shipment log's export.** Two lines: CM-SHP-009, and CM-MIG-001 as one object's export from its own list, as SA-11 placed the custom links' import. CM-SHP-009 alone is the alternative.
- **50 to 52, the settings pane's section routes.** These are on CM-ACC-006, as SA-13 placed the pane's root. Their condition `e` only chooses between the pane's two routers, so it isn't a scope. The scope is the pane's guard, `settings-control-panel`.
- **5 and 6, the manage app's `new` and `:webhookId`.** Their items include lines 2001, 2002 and 2007, which carry a `parent` and which SA-11 placed as the entries 'path: new; parent: /manage/webhooks/*' and the like. My lines repeat SA-11's placements (CM-API-009 `webhooks`, CM-CNT-006 `custom-urls`), so nothing differs. But the same items may stand under two entries (see "Problems").

## The CHANGES lines

- **CM-SHP-012@salla becomes held** (30, `:center_id` of the fulfilment centres), by a `shows` line only, so the cell stays without a placement. This is the same cell and reading as SA-13's entry 34, which the coordinator kept. Kept.

## Checker notes I read again

- **NOTE line 28, `marketing/offers` a container:** entry 26 is a link to `/marketing/offers`, not a route. The other paths it begins (22, 23) are links too. Each goes on its own place's capability.
- **NOTE line 47, `1/clusters` a container, and its first lead CM-API-007:** these are the Algolia client's request paths, not routes or containers. `batch` is the client's word (`/1/indexes/*/batch`), not Salla's bulk API. No line.

## What a source states that no entry holds (for the second stage)

- **CM-ANL-003:** the store performance report's recommendations and their claims (`structures/salla/dashboard-translations/en/reportsv2.json`, `rec_*_stat`). Examples: 'Cart reminders can recover 20%+ of abandoned carts.', 'Cart offers can increase AOV by 15% or more.', 'Merchants using cashback increased repeat purchases by over 55%.' and 'Loyalty programs can increase repeat purchase rates by up to 60%.'
- **CM-POS-001:** 'A free cashier for your shop, and easier selling at exhibitions and bazaars' and 'A free cashier system with your plan connects orders, inventory, and payments in one place.' (`reminders.json`, `edu.channel_sallapoint.*`). The price is free with the plan: a quality, if placed.
- **CM-LOY-002:** 'Digital Gift Cards *additional fees' / 'بطاقات الإهداء الرقمية *برسوم إضافية' (`reminders.json`, `edu.apps_view_66849380.feature_name`). An extra fee is a quality, as SA-32's notes say too.
- **CM-LOY-001, CM-LOY-004:** importing customers brings their loyalty points and wallets, 'استورد بيانات عملائك بسهولة، بما فيها نقاط الولاء والمحافظ' (`ar/reminders.json`, `edu.customers_imports.message`). The English message doesn't say so.
- **CM-PLN-006:** 'Your wallet balance may take up to 48 hours to update.' (`payments.json`, `wallet.balance.added_successfully_desc`), a duration.
- **CM-PAY-005:** 'View details of payouts transferred to your bank account.' (`wallet.transfer_cycle_invoices.page_description`), and payouts 'according to your plan's payout schedule' (`wallet.transfer_cycle.tooltip_desc`). The wallet's other routes (`transfer-cycle-invoices`, `unbilled-transactions`, `transactions`) are named in the locale's breadcrumbs, and no entry here holds them.
- **CM-CAT-005:** a brand's sales channels, a field of the brand form (web, app, `salla_point`), gated by `BRAND_SALES_CHANNELS`, 'brand-sales-channels', which the features list gives released false, plans plus, pro and special (`structures/salla/dashboard-features/demo@en/items.jsonl`; bundle @13805988).
- **CM-INV-005:** the inventory app's branches page shows an element only where the store's plan is `pro`, or `special` with another condition (`ro()==="pro"||ro()==="special"&&…`, @4893091). The element isn't read here.
- **CM-SHP-001, CM-SHP-016:** the restrictions page tells a store with routes activated that its first route was created, and offers a migration alert to routes where `shipping-routes` is on ('ShippingRoutesPage.rules-migration-alert-title', @14355779). This matches SA-13's lead on routes replacing rules.

## A structure whose items and sources disagree

None in the values. Two observations:
- In `dashboard-app-routes`, 21 to 26 and 8 to 10 are listed as path objects, but they are a report's links and a page's tabs. Each item's `keys` (`label`; `id`, `label`) shows it.
- In `dashboard-edu`, the banners' feature names aren't in the items. They are in the locales, by `contentKey`. The entry text has the address, the key and the plans only.

## Problems with the brief or the script

- **`show` lists an entry's items by app and path, ignoring `parent`.** So entries 5 and 6 list items 2001, 2002 and 2007, which carry a `parent` and which SA-11 placed under their own entries, 'path: new; parent: /manage/webhooks/*'. If the entries' ids are made with the parent, each such item stands under two entries, and both carry its lines. The lines agree here.
- **`show --code` doesn't reach a page's guard or `basePath`** where they sit away from the route (SA-13's check). Here most entries are routes inside page chunks, so printing each record once and searching all of them together answered the batch in a few commands.

## The coordinator's check (31 October 2026, after the batch)

- **The shipping restrictions' plan gate stands,** read from the page's own chunk: `plan` special and pro, the scope of entries 27 and 32. SA-13's line for `/shipping/rule/*` takes the same scope.
- **A feature named in a page's own setup is its gate** (16, 17, 19, 20: `size-guides`, `brands`, `products-filters`). It stands as the notes read it, a reading.
- **The performance report's recommendation buttons** go on the pages they open, as the notes placed them. The recommendations themselves are a lead for CM-ANL-003.
- **`show` lists items with the same app and path from every bundle.** Entries 5 and 6 each stand for items of two bundle versions. Their lines agree with SA-11's for the same paths, so nothing is placed twice.
- **The edu rules for SA-15 stand,** keeping to SA-32's reading of `allowedPlans`.
- **Cost:** 13.4 million tokens over 71 requests, about 168,000 an entry. No cell changes beyond SA-13's. The dashboard's routes, 706 entries over SA-7 to SA-14, are placed.
