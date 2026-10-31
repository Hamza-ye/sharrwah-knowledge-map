# Held pass, Salla, batch SA-32: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163: the first 130 rows of `plan-gates`, the repository's derived table `derived/plan-gates.tsv` (addresses /orders/statuses to /reports). Entry numbers below are the batch's order (`held_entries.py show --batch SA-32`).

**Placed:** 128 entries on capabilities (entry 77 also takes a `new` line), 2 `new` (91, 117), no `out`, in 150 lines. 20 entries take two lines. Supports: 128 `core`, 22 `shows`; no `own-service`, `extension-point` or `outside`. One filler, `tiktok` (106, as SA-8 wrote it). No quality: no row states a limit, a price or a fee.

**Sources read:**
- the guides the brief names: observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `index/ledger-summary.tsv`, and the register's rows for the three structures the table is built from (`dashboard-features`, `dashboard-edu`, `merchant-plans`). No ledger file enumerates the derived table; `index/ledger/feature.tsv` counts the features;
- the table's own description: `docs/READING.md` ("What a plan, a permission or a store's state allows, in Salla's words, beside what each store's pages showed") and the header of `capture/gates.py`, its only writer, which names its sources: the navigation entries' features (`structures/salla/dashboard-nav/prod/source.json` and `dashboard-nav-segments/prod/*.json`), the features list per store (`dashboard-features/<store>@en/items.jsonl`), the edu table (`dashboard-edu/prod/items.jsonl`, from the bundle `raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz@39521943`) and the English sweeps of three stores;
- to clarify only: the features list's `released`, `type` and `countries` for each row's features (no row here has a country); the nav entries' titles, labels and permissions (`dashboard-nav-segments/prod/*.json`); the edu banners' names (`dashboard-translations/en/reminders.json` and `ar/reminders.json`, keys `edu.<key>.feature_name`); and the steps the table names, plus a few steps of the same sweeps (cited in each line).

**No batch has placed `plan-gates` before.** SA-33 and SA-34 hold the rest of it (rows 131 to 284 of the table) and haven't run. The rules my lines follow are below, so the coordinator can align them.

## Rules my lines follow, for SA-33 and SA-34

1. **What a row is.** One row is one dashboard address and the plan gate Salla states for it. Its line goes on the capability whose cell already cites the address (the cells name Salla's links by path), or the capability the address's page is, as SA-7 and SA-8 placed the same routes (/localization, /logs/*, /manage/experts, /marketing/*, /channel/*). Where the path leaves the thing unclear, I read the nav entry's title in `dashboard-nav-segments/prod/*.json` (Product certificates, Join requests, Bullet Delivery, Shipping performance).
2. **Which column says what.**
   - `nav_features`, `features_list_plans`, `edu_allowedPlans` and the `merchant` and `public_demo` lines are Salla's words, and the entry's text. Terms come from `nav_features` (the cells already use these flag names as terms).
   - `enabled_merchant`, `enabled_demo` and `enabled_public_demo` are Salla's features list per store: a store's value, so they go in `reading`, never `quality` or `scope`.
   - The `demo` column holds the Pro store's page lines verbatim (`capture/gates.py`), but the brief names `demo` among the repository's own columns. So I took no term or scope from it; I quote it only where I cite its step (20, 36, 48, 49).
   - `steps` is the repository's; each quote cites the step it names.
3. **`supports`, by the features list's own state (the brief's ruling on flags):**
   - the row's feature `released: true`, with plans: `core`;
   - `released: false`: `shows`, whatever the pages say (15, 32, 37, 44, 48 to 51, 59, 60, 64, 80, 92, and the `multi-countries-link` line of 11);
   - `released: true`, no plans, enabled on all three stores: `core` (24, 34, 38, 55, 56, 73 to 76, 79, 81, 82, 93, 95);
   - a feature not in the features list (`sweply`, `shift_reports`, `soft_pos`, `digital-code-log`): `core` where the edu row or a page states plans (25, 69, 89), or the route is Salla Point's own (70); `shows` with no plan stated and a 404 page (61).
   - Salla Chat is `shows` wherever it stands (43, 97): the coordinator's ruling on SA-8, 'Salla Chat is no longer available for new subscriptions.'
4. **`scope`, one per entry, the first of these that the row states:**
   - the features list's plans, in its own identifiers and order, repeats dropped (`salla-ads: pro, plus, special, pro` gives `pro;plus;special`);
   - else the edu row's `allowedPlans` as written (`plus;team;special`): the same bundle maps `team` to `pro` (its function on `e==="team"`, record @39521943), which each such line says;
   - else the plans the Basic store's page names, in its words (`Special;Pro;Plus` from 'Available on Special, Pro, and Plus plans'; `plus;pro;special` from the Arabic report gate);
   - else the nav feature's name, the route's store gate (`influencer-marketplace`, `shipping-policy-archive`), as SA-8 and SA-9 wrote a route's feature gate;
   - else empty (98, 107, 123: the edu row's `allowedPlans` is empty).

   Where a row has two features with different plans (11), the scope is their union, and each line's reading names its own feature's plans.
5. **Edu-only rows** (96 to 128: no nav feature) state a banner, not a gate on the page. The banner's feature, as its key's `feature_name` names it and the Basic store's page shows it ('Add New Customer' / 'Available on Plus, Pro, and Special' on /customers), is what the plans are stated for. So the line goes on the banner's feature, not on the list page at the address: /orders is Order Editing (CM-ORD-002), /customers/groups/new Bulk Customer Group Management (CM-CUS-003), /payments Salla Payments (CM-PAY-002), /products/branches/new and /products/branches/* Branch Pickup (CM-SHP-007), /products Product Import (CM-MIG-001). Terms are the path's segment that names the thing, where one does.
6. **App pages** (`/apps/view/<id>`, 97 to 99, 119): a line on CM-APP-002, the App Store's page for one app, `core`; and a line on the app's thing: `core` where the model's flag for it is released (ZATCA, CM-TAX-007), `shows` where it isn't released (Store Blog, CM-CNT-004; Digital Gift Cards, CM-LOY-002, whose cell's `wallet-gift-card` isn't released) or is listed unavailable (Salla Chat). No maker is stated for any of them: a gap. They aren't embedded pages, so no CM-APP-007 line.
7. **A gate that names another capability's thing takes that capability's line too:** /marketing/integration-tools/snapchat (Pixels & feeds, CM-MKT-009) is gated by `salla-ads` (CM-MKT-010); /logs/export by `advance-audit-log` (CM-TRU-003); /users/roles by `user-advance-management` (CM-STF-001); /users/targets by `app_pos` (CM-POS-001); /shipping/bullet-delivery by `shipping-routes` (CM-SHP-016); /reports/performance by `reports` (CM-ANL-002).
8. **Containers.** /more and /tools are menu groups whose pages answer 404: the mobile menu's Shipping & delivery (`more.json`, `mega.json`) and the Tools menu's Shipping (`tools.json`), each carrying `shipping-policy-archive`. Each goes on CM-SHP-001, the capability its title names (rule 3), with a second line on CM-SHP-002 for its feature, the cell's own flag. The other /more groups (Customers, Help Desk, Payment, Tools, Logs) carry no feature, so the table holds no row for them.
9. **No CM-PLN-001 line per row**, as ZD-9 to ZD-13 gave none per plan policy. The plans are each line's scope.
10. **Measures stay on CM-ANL-001** (75, 76), as ZD-13 kept ZidShip's analytics and reports there.

## Where I kept to earlier batches and the model

- SA-7 and SA-8's capabilities for the same routes: /localization (CM-INV-005, and CM-MKS-001 for Multi Market), /logs/audit (CM-TRU-003), /logs/export (CM-MIG-004), /logs/messages (CM-NTF-003), /manage/experts and its orders (CM-PTN-005), /marketing/influencers (CM-MKT-015), /marketing/customer_wallet (CM-LOY-001), /marketing/campaign/retargeting (CM-MKT-005), /marketing/ads/dashboard (CM-MKT-010), /marketing/ads/tools/tiktok (CM-MKT-009 and CM-MKT-010, terms and filler `tiktok`), /marketing/seo/* (CM-CNT-007), /channel/mahally (CM-CHN-002), /channel/chat (CM-SUP-004, `shows`).
- The model's own flag placements: `customer-metadata` on CM-CUS-001 (`core`), `custom-customer-fields` on CM-CUS-001 (`shows`), `app-performance-reports` on CM-ANL-002 (`shows`), `metal-pricing` on CM-CAT-013 (SA-1).
- Zid's plan policies (ZD-9 to ZD-13): a released policy for a plan is `core` with the plan as scope; a disabled one `shows`; measures on CM-ANL-001.

## New things

1. **Bullet Delivery** (التوصيل السريع; the shipping menu also calls it Express shipping, الشحن السريع), entry 77. Its place of its own is an admin route and a nav entry (`/shipping/bullet-delivery`, `dashboard-nav-segments/prod/shipping.json`; the sweep's title 'Express Delivery'), gated by `shipping-routes` (plans pro, special). Its page says 'This feature is only available in the سلة سبيشل, سلة برو plan.' (`20261008T133523Z-sweep-demo-store-en/steps/273.text.txt`). Proposed: domain C, area SHP, parent CM-SHP-001. Searched: express; bullet; التوصيل السريع; الشحن السريع; same-day (only CM-CHK-008, quick checkout, by "express"). What it delivers isn't stated; the gate's feature, shipping routes, suggests it rides on them (a reading).
2. **Product certificates** (شهادات المنتج; its page is titled 'Certificate templates'), entry 91. Its place of its own is a nav entry in Products and its route `/products/certificates` (`dashboard-nav-segments/prod/products.json`), feature `product-certificates`, released, plans plus, pro, special. Proposed: domain B, area CAT, parent CM-CAT-001. Searched: certificate; شهادة; شهادات; certificate templates; شهادات المنتج (found only CM-SFR-010's SSL certificate, CM-PAY-003's onboarding and CM-TRU-010's legal compliance, none of them this). What a certificate certifies isn't stated.
3. **Custom Product Fields** (الحقول المخصصة), entry 117. Its place of its own is the dashboard address `/products/options/custom-fields/*` under Categories & options, with an edu row (team, special), and the concern map's plan line إضافة حقول مخصصة للمنتج (SA-S-2134), which no cell cites. Proposed: domain B, area CAT, parent CM-CAT-001. Searched: custom field; حقول مخصصة; product field; attribute; specification; مواصفات; metadata. CM-CNT-002's note keeps Salla's custom fields out of metafields (U-005), so I didn't place them there. The alternative is a line on CM-CAT-001.

## Entries I couldn't tell, and what would settle each

- **The edu rows' plans against the features list.** On 1 the edu row allows basic and the features list doesn't; on 54 the edu row leaves out plus, which the features list includes; on 110 the Basic store's page names Plus, which the edu row leaves out. On 40 and 124 every store's page, the Basic ones included, says 'Available on your plan'. I scoped by the features list, or the edu row where it is the only one, and named the difference in `reading`. A Basic store's journey into each page (does it open?) would settle which gate holds.
- **Edu-only rows with no swept page** (96 to 100, 107, 108, 117, 119, 123, 125): the line rests on the edu row and its banner's name alone. Settled by sweeping those addresses on a Basic store.
- **96, /apps/all**: the App Store's banner is scoped plus, team, special, though the App Store is open to every store. What the plans gate there isn't stated.
- **23 and 62, `abandoned-cart-rule`**: I read the feature as the carts' recovery rules (CM-MKT-022), beside the records at /marketing/carts (CM-CHK-007). The bundle's use of the flag would settle it.
- **64, Referral program** (`affiliate-referral`, not released): on CM-MKT-013, whose cell's app holds /marketing/referrals. Whether it refers buyers (CM-LOY-008, which holds nothing on Salla) or partners isn't stated. The page, which no held step opened beyond its gate, would settle it.
- **61, Events manager** (`sweply`, 404 on the Pro store): placed `shows` on CM-MKT-005 with the campaigns. What it manages isn't stated.
- **70, Activate Card Payments**: `core` on CM-POS-001 as Salla Point's page; `shows` on CM-PAY-021, since the row doesn't say who processes the payment (the cell's statement names Geidea, `outside`).
- **118, /themes**: the banner is 'Theme editor' in English and إدارة الثيمات (managing themes) in Arabic. I followed the Arabic and the cell's /themes (CM-SFR-001); the English would put it on CM-SFR-002.
- **75 and 76**: shipping measures on CM-ANL-001 alone. CM-SHP-002 (Salla's shipments, 'Track your Salla shipments') is the alternative for 75.
- **9, /products/quantities/bulk**: the cell's link names it Inventory management (CM-INV-001), and its edu banner 'Quantities Log' (CM-INV-002's thing). I kept the cell's link.

## Items against sources

- The table writes a plan twice where the features list does (`salla-ads`, `bulk-seo`: pro twice). The source holds the repeat; the scope drops it.
- `multi-warehouse-link` is the only feature here whose plans list `team` (team, special), where every other feature writes `pro`.
- Enabled against plans: `import-products` (17) and `mahly` (36) are enabled on none of the stores, the Pro store included, though their plans include pro; `manage-products-by-branches` (20) is enabled on the Pro store, whose page still says 'This feature isn’t available on your plan'; `auth-forced` (49) lists pro and special, and the Pro store's page names Special only. The bytes don't say why; each is in its line's `reading`.

## For the second stage: what the sources state that no entry holds

- The edu banners' own texts, title and message, for each address (`dashboard-translations/en/reminders.json`, `ar/reminders.json`, keys `edu.*`), and the help article each edu row links (`dashboard-edu/prod/items.jsonl`, `action.url`, 71 rows). They name each banner's feature in both languages: leads for the cells whose Arabic names are missing.
- 'Digital Gift Cards *additional fees' (`edu.apps_view_66849380.feature_name`): an extra fee for gift cards, a quality for CM-LOY-002 if a held page states it.
- Salla Point: its card payments need a subscription ('Subscribe to Salla Point to activate card payments.', `20261009T000815Z-sweep-nav-unreached-demo-en/steps/013.text.txt`), and its shift reports are turned on in its settings ('Activate shift reports from Settings to view this page.', step 011 of the same run). Leads for CM-POS-001 and CM-PAY-021.
- Shipping performance's measures (COD delivery success rate, paid delivery success rate; `20261008T133523Z-sweep-demo-store-en/steps/262.text.txt`) and the shipping reports' (average logistics cost per order, average pickup time, by label source and carrier; step 264).
- App Settings: 'Select default apps for email, SMS, and WhatsApp notifications.' (`20261009T000815Z-sweep-nav-unreached-demo-en/steps/006.text.txt`), for CM-NTF-004.
- The nav's badges: Salla Point's 'Free Cashier' tag, and the 'New' tags of Employees targets, the mobile app's Reports and Auto pricing (Auto pricing also `isBeta: true`; `dashboard-nav-segments/prod/products.json`).

## The checker's lines, read again

- `NOTE line 44`: "core on a product named with the platform's brand" (39, /manage/domain): the brand is in the quoted plan line, 'Upgrade to Salla Plus or Pro and get a custom domain for your store.'. The line is `core` by Salla's own Domain settings and its released flag `domain`, not by a product's name.
- `NOTE` lines 89, 105 and 137, new things whose entries have leads: the leads are CM-SHP-016 by `shipping-routes` (77, which takes its line beside the new one), and CM-PLN-001, CM-PLN-002, CM-EVO-001 and CM-B2B-003 by plan names or the words "feature" and "merchant". The plan names are the scope, not the thing.
- **Leads that are no leads:** CM-PLN-001 and CM-PLN-002 lead from nearly every row by its plans' names; CM-EVO-001 (holding nothing on Salla), CM-B2B-003 and CM-AIA-001 by "feature" and "merchant"; CM-SHP-023 (holding nothing) for /shipping by "plan" and "shipping"; CM-API-013 (holding nothing) for /users by "merchant" and "user". None is an entry's thing.
- No `CHANGES` line: no line alone changes a cell. Three `NEW` names.

## Problems with the brief or the script

- **The brief's `demo` column.** For `plan-gates`, `demo` is the Pro store's page lines, verbatim (`capture/gates.py`), not an observation of the repository's. The brief's list fits `permission-gates`' `demo_or_admin`. I followed the brief and took no term or scope from it (rule 2 above).
- **One scope per entry, with two features** (11): the rule gives the union, and a `shows` line for a Special-only flag carries `team;special`. Each line's reading names its own feature's plans.
- **Quoting with ' beside possessives.** A closing quote right after a digit (CM-MKT-007's, Q1's) reads as the start of a quote, so I wrote those possessives another way.

The checker's last line, for SA-32: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (30 October 2026, after the batch)

- **The brief's known case on derived tables is corrected.** In `plan-gates`, `demo` holds the Pro store's plan lines, quoted whole from its page, as `merchant` holds the Basic store's (`capture/gates.py`, lines 1 to 30 and 184). So it quotes the platform. The brief had listed it among the repository's own columns. The lines here took no term or scope from it, so none changes. SA-33 and SA-34, and the `permission-gates` batches, read the corrected case.
- **The rules for SA-33 and SA-34 stand,** as the notes set them out: supports from the features list, scope in the order the notes give, the edu banner's feature for a row with only a banner, and no CM-PLN-001 line.
- **The new things are decided with every platform's:** Bullet Delivery, Product certificates and Custom Product Fields. Two points go with them:
  - the concern map's plan line إضافة حقول مخصصة للمنتج (SA-S-2134), which no cell cites, is evidence for the third;
  - CM-CNT-002's homonym note (U-005) is read first.
- **The checker's NOTE on line 44** (entry 39, `/manage/domain`) stands as the notes read it: `core` from Salla's own Domain settings and its released flag `domain`.
- **Cost:** 16.5 million tokens over 83 requests, about 127,000 an entry. No cell changes: the concern map had read the features list's plans. The yield is the three new things.
