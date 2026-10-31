# Held pass, Salla, batch SA-16: notes

130 entries (effort high), evidence at observed-sa@b0bd0b16: entries 74 to 203 of `dashboard-features`, the features list, continuing from SA-15. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-16`). Every entry is held under the demo store (`demo@en`, store-sherawya, Pro); 124 also under the real store (`real-merchant@en`, dandye-dandy-ksa, Pro); `canvas-mode` (108) under the demo store and the public demo. Five are held under the demo store alone, because the real store's value differs and is a separate entry (SA-17's): 86 `store-app-scopes`, 91 `multi-countries-basic`, 92 `multi-warehouses`, 97 `store-status`, 124 `manage-products-by-branches`.

**Placed:** 129 entries on capabilities, 1 `new` (14), no `out`, in 141 lines. Eleven entries take two lines: 40, 42, 44, 47, 72, 89, 93, 95, 108, 113 and 118. Supports: 122 `core`, 19 `shows`; no `own-service`, `extension-point` or `outside`. No filler: every flag named for a third party (Zapier, Google, Facebook, Snapchat, TikTok, MyFatoorah, DHL, WebEngage, Virtooal) is its capability's evidence, never a filler (the brief). One quality: `branches: limit 20` (89, `store-branch`, the entry's `limit: 20`).

**Sources read:** the brief and what it names; SA-15's notes and placements first, with the coordinator's check; the rulings, their last section included; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's row for `dashboard-features`, `index/ledger-summary.tsv` and `index/ledger/feature.tsv` (the features ledger, for each feature's gate and landed address); `docs/PLAN.md`'s Instruments (lines 11 to 15) for the stores' plans; the four stores' `items.jsonl`, compared feature by feature; the concern map's statements of the Basic store's list (`studies/concern-map/platforms/salla/citations.tsv`) and the cells that cite them (`merged/evidence.tsv`); the earlier batches' lines that name the same features (SA-2, SA-9, SA-11, SA-12, SA-15, SA-20 to SA-23, SA-32 to SA-34); the platform's locales: `dashboard-translations/en/feature-content.json` and `ar/feature-content.json` (a locale keyed by feature name, with each feature's name, description and highlights: 105 features, 41 of them in this batch), and single keys of `reminders.json`, `marketing.json`, `editor.json`, `sdk.json` and `settings.json`; one settings-center file for one condition (entry 111, below); the model's cells.

## Rules my lines follow

I kept SA-15's ten rules (the capability whose cell holds the same flag; `released` sets `core` or `shows`; each entry's own store's `released`; scope from `plans` in the list's order, repeats dropped; the stores' values in `reading`; the feature's name as its only term; no filler from a flag's name; type `app` on its thing, the install link taking no line; an earlier batch's line kept where the feature is the same thing). Four more, for this batch:

11. **The locale `feature-content.json` names many features.** Where its name for a feature is a capability's own term, the line goes there, even where the concern map put the flag on the parent:
    - `customer-advance-management` (6): 'Flag unreliable customers', 'كشف العملاء غير الجادين', CM-CUS-006's own term. The model's SA-S-3167 sits on CM-CUS-001.
    - `order-advance-management` (66): 'New order', 'Create orders on behalf of customers', CM-ORD-005 (manual orders). The model's SA-S-3278 sits on CM-ORD-001.
    - `store-branch` (89): 'In-store pickup', 'الاستلام من الفرع', a second line on CM-SHP-007 beside SA-32's CM-INV-005.
    - `payments-operations` (72): 'Online payments', 'المدفوعات الإلكترونية', CM-PAY-002's own term, a second line beside SA-32's CM-PAY-020.

    Each of these cells is already `core` on Salla, so none changes.
12. **A feature whose name names two things takes two lines**, as SA-15 gave `inventory::print_export`: `coupon-affiliate` (40: CM-MKT-014, CM-MKT-002), `coupon-export` (42: CM-MKT-002, CM-MIG-001), `mahly-coupon` (47: CM-CHN-002, CM-MKT-002), `customize-login-for-multi-markets` (93: CM-MKS-001, CM-CUS-010). A coupon's condition (`coupon-payment-method`, `coupon-customer`, `coupon-countries`, `coupon-multi-market`) is a part of coupons and takes CM-MKT-002 alone.
13. **A feature that gates two earlier lines' pages takes both their capabilities:** `restore-data` (95), the gate of /orders/trash and /products/trash (`index/ledger/feature.tsv`; SA-32's CM-ORD-012 and CM-CAT-001); `abandoned-cart-rule` (44), CM-CHK-007 and CM-MKT-022 as SA-15 and SA-32; `partner-merchant-affiliate` (118), the model's CM-PTN-009 and SA-12's CM-MKT-014, whose affiliate routes render behind it; `ai-bundles` (113), below.
14. **A released feature whose thing nothing held states** is placed where its name and neighbours put it, `core` (as SA-15's SMS services), except where its one identifiable word names a third party or a technical term only: then `shows`, as SA-15 kept `storage-station` (17 `zapier-service`, 71 `gotenberg-webhook`).

**`released` differs by store** (the brief's known case). Where this entry's stores differ from the others, my line takes its own value and names the others:
- `store-app-request` (83): released on the two Pro stores, not on the Basic store or the public demo, whose value the model read (SA-S-3327, `shows`). Mine is `core`, enabled false on both Pro stores.
- `multi-countries-basic` (91): released on the demo store alone; the Basic store, the public demo and the real store hold it released false (the model's SA-S-3340, `shows`). Mine is `core`; SA-11's markets routes are gated on it ('not multi-countries-basic').

**`canvas-mode` (108)** is released false on all four stores, enabled on the demo store and the public demo. Its two lines are SA-2's, after the coordinator's check: CM-SFR-006 and CM-AIA-002, both `shows`, scope `plus;pro;special`. The model's SA-S-3374 sits on CM-SFR-002 (`shows`); the coordinator may move it.

**Lines whose support differs from the model's line for the Basic store's statement, on cells already `core`:** 3 `suggested-by-moshamer` (released, `core`; the model's `shows`), 23 to 25 the three conversion apps (released, type app, `core`; the model's `shows`, maker not stated), 31 `update-products` (`core`, by its place among the import and export flags; the model's `shows`), 44 `abandoned-cart-rule` (`core`; the locale states what it is: 'Recover sales from abandoned carts'). None changes a cell.

## New things

1. **national-day-banners**, entry 14: the flag `national-day-banners`, not released, plans plus and pro, enabled on both Pro stores. `shows`.
   - What it is, from the locale: the dashboard's National Day reminders (`structures/salla/dashboard-translations/en/reminders.json`, keys `national_day.*`), four banners to the merchant promoting cart offers ('Same Customer, 30% Bigger Carts with Cart Offers'), cashback, and two apps, Cartat ('Recover up to 30% of your abandoned carts with Cartat') and Zood ('Increase order value with Zood — up to 40% conversion rate'). A reading: the flag's name and the keys' prefix match.
   - **No place of its own:** one flag and four locale strings.
   - Proposed: domain A, area ONB, parent CM-ONB-003 (the platform's support and learning for merchants), or decided as no capability: the banners promote other capabilities' features, as the edu banners do, which SA-14 and SA-15 placed each on its feature. Name in English: National Day banners; the Arabic strings are under the same keys in `ar/reminders.json`.
   - Searched: banner; بنر; national day; وطني; occasion; مناسب; reminder; تذكير; announcement; seasonal; موسم; promotion; tips; edu. Found CM-SFR-007 (storefront banners), CM-MKT-019 (marketing calendar), CM-LOY-007 (reorder reminders): none is banners to the merchant in the admin.
   - The checker's NOTE on its lead, CM-PLN-001: a lead by plan names only, no lead.

## The checker's CHANGES line

- **`CHANGES CM-AUT-001@salla holds nothing: becomes held, by line 18`** (entry 17, `zapier-service`). Read again against its source: the demo store's and the real store's lists hold `zapier-service` released true, plans pro and special, enabled true (line 240 of each `items.jsonl`); the Basic store and the public demo hold it released true, enabled false. Its neighbours are the external services' flags (`external-services`, `mail-service`, `google-merchant-feed`, `google-site-verification`). The line is `shows`, so the cell becomes held with no placement. Kept, as a reading resting on the name.
  - **A lead the brief's sources don't reach:** Salla's App Store lists an app 'Zapier' whose short description begins 'تطبيق ذكي لربط التطبيقات الأخرى ودمجها معًا، وإتمام المهام الروتينية تلق' (`structures/salla/marketplace-apps/api@ar/items.jsonl`, id 554657544), and the help tree holds 'Connect your store with Zapier' (`structures/salla/help-embedded-tree/en/items.jsonl`, slug integration-with-zapier-platform). That supports CM-AUT-001's thing (automations across apps), done by a third party: whichever batch places those entries sets the cell's placement (`extension-point` or `outside`), and this line's `shows` stays as the flag's.
  - Alternatives: `new:zapier-service`, or `out` of CM-AUT-001 if the coordinator holds that a third party's automations are not the class's workflow automation.

## Entries I couldn't tell, and what would settle each

- **1, `cash-payment`** (not released): `shows` on CM-PAY-016 by its name and its place right after `cod`, `bank`, `mada` and `credit_card`. CM-PAY-029 (cash on delivery, `cod`'s cell) is the alternative. What the flag gates isn't held.
- **16, `mail-service`** (released): `core` on CM-NTF-004 by its name, the store's email sending. The locale's 'Store email', 'Send emails from your store domain', belongs to another feature, `email-provider` (SA-17's), and 'Business email' to `business-email`. If `mail-service` is the store's own mailbox rather than sending, CM-SFR-009 (DNS) or a new thing would take it.
- **27, `webengage`** (type app, not released): `shows` on CM-MKT-009 by its neighbours. **A lead the brief's sources don't reach:** the App Store's 'WebEngage', 'تطبيق WebEngage يقدم لك أدوات متقدمة في أتمتة التسويق وإدارة الحملات التسويقية', company 'WebEngage Technologies DMCC' (`structures/salla/marketplace-apps/api@ar/items.jsonl`, id 197781498), and the help article slug webengage-marketing-notifications-app (`structures/salla/help-sitemaps/articles-en-1/items.jsonl`, position 91). These put it on CM-MKT-006 (marketing automations), whose Salla cell holds nothing. The coordinator may move the line; it would then change CM-MKT-006.
- **43, `partnerships`** (released): `core` on CM-MKT-013 by its name and its marketing neighbours. Nothing held in reach says what it is. CM-PTN-005 or a new thing are the alternatives.
- **71, `gotenberg-webhook`** (released): `shows` on CM-API-009 by the word webhook. Its neighbours are order flags (`order-summary`, `duplicated-order-check`, `partial-payments`), so it may be an internal service of order documents (CM-ORD-008, invoices) or the software's own plumbing (`out`). Nothing held in reach says.
- **87, `dark-mode`**: `core` on CM-CHN-006, by its neighbours (the store app's flags) and the app maker's setting 'Enable dark mode' (`dashboard-translations/en/editor.json`, `appmaker_general_settings.enable_dark_mode`). The dashboard's own 'Dark mode' (`sdk.json`, `common.dark_mode`) is the alternative: an admin preference, which no capability holds.
- **98, `product-sorting`**: `core` on CM-CAT-003, by its locale, 'Arrange products within each category'. CM-CAT-001 is the alternative.
- **105, `legacy-login-flow`**: `core` on CM-CUS-010, the buyers' sign-in, by its neighbours `cross-store-login` and `re-captcha-v3`. **A lead:** the storefront's own feature list holds it beside `guest-checkout` and `embedded-login-checkout` (`structures/salla/storefront-init/index@demo-ar/source.json`), which supports the buyers' side. CM-TRU-001 (the admin's sign-in) is the alternative.
- **111, `ai-driven-personalized-product`**: `core` on CM-MKT-023. The products settings label a recommendation type 'Similar products recommended by Mushammir' (`dashboard-translations/en/settings.json`, `products/products.recommendations#types.ai_products`) under the condition `useFeature` `ai-driven-personalized-product`. That condition is in `structures/salla/settings-center/demo@en/products~products.recommendations.json`, a settings-center file: the brief's list of clarifying sources doesn't name it, and I cite it for the condition only. CM-AIA-001 (an AI feature, though for buyers) could take a second line.
- **113, `ai-bundles`**: CM-SFR-002 and CM-AIA-001, as SA-9 read the themes editor's AI section generator behind `AI_BUNDLES` (SA-E-33115730), and as its neighbours, the theme flags, suggest. The model's SA-S-3385 sits on CM-SEL-006 (product bundles), which neither supports. The coordinator may move it.
- **118, `partner-merchant-affiliate`**: two lines, CM-PTN-009 (the model's) and CM-MKT-014 (SA-12's routes). One of them may be enough; the ruling after SA-22 keeps a second line for a page that is two things, and this is a flag, not a page.
- **57, `cash-on-delivery-settings`**: CM-PAY-029 alone. The model also cites it on the parent CM-PAY-016.
- **72, `payments-operations`**: the second line on CM-PAY-002 rests on the locale's 'Online payments', 'Accept payments with Mada, Apple Pay, and credit cards'. If the coordinator holds that a feature's locale doesn't name a second thing, CM-PAY-020 alone stands.

## Items against sources

None: each entry's text matches its stores' `items.jsonl` lines byte for byte in value. Two remarks:
- `mahly-coupon` (47) is held only on the Pro stores. The Basic store's and the public demo's lists don't hold it, which is why the concern map has no statement of it, and why every later feature's line number in those two lists is one less.
- `store-branch`'s `limit` is 20 on the Pro stores and 5 on the Basic store and the public demo. The model records 5 (SA-S-3338) as the feature's limit; it is the Basic plan's.

## For the second stage: what the sources state that no entry holds

From `structures/salla/dashboard-translations/en/feature-content.json` (and `ar/`), a feature's own description, for cells the model holds:
- **CM-ORD-014:** 'Duplicate a previous order with the same details or edit it as needed' (`order-reorder`). The cell's note says who repeats the order isn't stated; this says the merchant does.
- **CM-SHP-007:** 'Let customers pick up orders from your branches', 'Increase average order value at pickup' (`store-branch`). The cell's note says nothing held defines it.
- **CM-CUS-006:** 'Identify customers with repeated order cancellations', 'Reduce fake or unreliable orders' (`customer-advance-management`).
- **CM-ORD-005:** 'Capture phone and WhatsApp orders' (`order-advance-management.highlights`). The cell says Salla's statements don't say where a manual order is made.
- **CM-MKT-016:** 'Send alerts by email, SMS, or WhatsApp' (`product-availability-notify.highlights`).
- **CM-MKT-014 and CM-MKT-002:** 'Set affiliate commissions for each purchase' (`coupon-affiliate.highlights`).
- **CM-MKT-002:** 'Import coupon codes from a ready file', 'Set usage limits for each coupon' (`coupon-group.highlights`).
- **CM-ORD-010:** 'Stop orders outside working hours' (`receiving-orders-times.highlights`).
- **CM-SUP-002:** 'Collect customer ratings after each order' (`order-send-rating.highlights`).
- **CM-PAY-002:** 'Accept payments with Mada, Apple Pay, and credit cards' (`payments-operations.highlights`).
- **CM-MIG-001:** 'Download data in XLSX or CSV formats' (`export-product-orders.highlights`), a format the cells don't hold.
- **CM-CHN-002 and CM-MKT-002:** 'Create Mahally coupons with fixed or percentage discounts', 'Set each coupon’s start and end dates' (`mahly-coupon.highlights`).

The locale names 64 features outside this batch (`ai-description-generator`, `business-email`, `email-provider`, `pre-order-campaigns`, `salla-importer`, `tabby`, `tamara` and others), some of them SA-15's entries and the rest SA-17's: leads for SA-17.

From `structures/salla/marketplace-apps/api@ar/items.jsonl`: the apps Zapier (554657544) and WebEngage (197781498), above.

## Problems with the brief or the script

- **The brief's list of clarifying sources doesn't name `feature-content.json` by name.** It is the platform's locale keyed by feature, and it states most of what a features batch needs: for 41 of this batch's features, what they are. I read it as one of "the platform's locales", as SA-15 read `reminders.json` for the edu banners. The coordinator may want the brief's known case for `dashboard-features` to name it.
- **The App Store's listing (`marketplace-apps`) and the settings centre aren't in the clarifying sources,** yet they would settle three of my unclear entries (17, 27, 111). I placed by the sources the brief names and listed them as leads.
- **The concern map's statements of the features list cite the Basic store only,** so a line on a feature `released` on the Pro stores alone (83, 91) differs from the model's `shows`. Listed above.

The checker's last line, for SA-16: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **`zapier-service` is `extension-point` on CM-AUT-001,** Zapier its filler. The App Store lists a Zapier app for linking apps and automating routine tasks (`marketplace-apps`, id 554657544), so the released feature (plans pro and special) is the store's link to Zapier: a third party automating the store through what Salla provides. Salla's CM-AUT-001 cell, which held nothing, becomes held with `extension-point`.
- **`webengage` moves to CM-MKT-006,** marketing automations, as the App Store describes WebEngage. It stays `shows`, since the feature isn't released, so the cell is held with no placement.
- **The brief now names both sources the notes used,** among what may clarify an entry: the features' locale (`feature-content.json`) and the App Store's listing.
- **`ai-bundles` is the themes editor's AI section bundles,** by SA-9's route and these lines. The concern map's row for it on CM-SEL-006, product bundles, is a homonym, and is read again at Salla's amendment.
- **`canvas-mode` is `shows`,** as SA-2's lines are after SA-15's check.
- **New thing:** national-day-banners, an unreleased feature for the dashboard's promotional reminders. It is decided with every platform's new things, probably as no capability.
- **Cost:** 9.3 million tokens over 55 requests, about 72,000 an entry. Two cells change: CM-AUT-001 and CM-MKT-006.
