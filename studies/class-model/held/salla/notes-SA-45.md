# Held pass, Salla, batch SA-45: notes

80 entries (effort high), evidence at observed-sa@b0bd0b163:
- 1: `portal-settings` (`partner@en`), the Partners portal settings page's one section, General Settings, with its three pages;
- 2 to 35: `report-catalog` (`demo@en`), the 34 reports of the dashboard's report catalog, in Salla's order (7 categories: sales 13, products 9, customers 3, payments-shipments 1, loyalty-program 2, marketing 3, salla-point 3);
- 36 to 54: `report-widget-categories` (`demo@en`), the 19 categories of the elements a custom report is built from;
- 55 to 80: `report-widgets` (`demo@en`), its items 1 to 26 of 124, the elements Salla publishes for Create report (`/reports/create`).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-45`). No batch had placed these four structures. `portal-settings`, `report-catalog` and `report-widget-categories` end here. **`report-widgets` doesn't:** SA-46 (its items 27 to 110, 81 entries) and SA-47 (items 111 to 124, 12 entries, with `report-widgets-legacy`) hold the rest, and haven't run. My rules for it are below, so they can keep to them.

**Placed:** 80 entries on capabilities, none `new`, none `out`, in 85 lines. Five entries take two lines: 1 (CM-PTN-002, CM-TRU-001), 36 App Widget (CM-ANL-002, CM-ANL-006), 47 Performance Summary (CM-ANL-002, CM-ANL-003), 78 Order sources and 79 Ad campaign performance (CM-ANL-002, CM-MKT-008). Supports: 84 `core`, 1 `extension-point` (36 on CM-ANL-006). No `own-service`, `outside` or `shows`, no filler, no quality. Scope on 4 lines: the catalog's gate `charity` (12 to 14, the three donation reports) and `t1` (31, Abandoned Cart Customers).

**Sources read:** the brief and what it names; SA-44's notes and placements (its lines 79 to 93, the portal's report builder), SA-12's and SA-14's notes and placements, SA-35, SA-36 and SA-38's lines for the portal's `/settings` routes; observed-sa's guides, the register's rows for the four structures, `index/ledger-summary.tsv` and `index/ledger/report.tsv`. Then each structure's `meta.json` and source: `portal-settings/partner@en/source.json`; `report-catalog/demo@en/categories.json`, the category lists and the 34 report bodies; `report-widget-categories/demo@en/source.json`; `report-widgets/demo@en/source.json` and `items.jsonl`. To clarify only: the labels, which are translation keys, in `structures/salla/dashboard-translations/{en,ar}/reportsv2.json`; the run steps the ledger joins (`20261008T213916Z-journey-report-catalog-demo`, steps 2, 12 and 35; `20261008T212405Z-journey-reports-create-demo`, steps 1 to 7); `performance-reports/demo@en/items.jsonl`, for Store performance's own reports; and the model's cells.

## The rules my lines follow (for SA-46 and SA-47)

1. **The dashboard's own reports are CM-ANL-002's, `core`** (the coordinator's check of SA-44). A report of the catalog, a widget Salla publishes, and a category of widgets are each a kind of report or a part of one. CM-ANL-002's note keeps Salla's report kinds with the reports, so none takes a line on its subject's capability: no CM-LOY-001 for the wallet's widgets, CM-LOY-005 for the wishlists', CM-PAY-001 for payment methods, CM-SHP for carriers, CM-INV-001 for stock, CM-MKT-022 or CM-CHK-007 for abandoned carts, CM-SFR-006 for landing pages, CM-POS-001 for Salla Point, CM-SEL-007 for donations, CM-MKT-016 for Notify When Available, CM-MKT-002 for coupons. CM-CAT-012's note says the same of the profit reports: 'Salla’s profit analytics are domain D’s'.
2. **The capability follows SA-12's lines.** The catalog's reports are SA-12's routes of a report category and of one report (`H.CATALOG_CATEGORY`, `H.CATALOG`) on CM-ANL-002. The widgets and their categories are what a custom report at `/reports/create` is built from, which SA-12 placed on CM-ANL-002, CM-ANL-003 its alternative (below).
3. **One exception: attribution.** A widget whose own words name orders credited to their sources or to campaigns (78 'Order sources', 79 'Ad campaign performance') takes a second line on CM-MKT-008, `core`. Attribution is the crediting itself, which the platform computes and shows only as such a report, as Shopify's cell rests on a conversion summary route. The coordinator's ruling after SA-25 keeps an order's Order Source (`utm_source`) on this cell. Visit sources (65) credit visits, not orders, and stay on CM-ANL-002 alone, as CM-MKT-008's cell reading left the permission تقارير مصادر الزيارات out.
4. **A widget's publisher:**
   - `salla`: CM-ANL-002 `core`;
   - `App ID: <REAL_APP_ID>` (items 120 to 122, one entry at line 120 in SA-47, category App Widget, data from `/platform/partners/<REAL_APP_ID>/dev`, title 'MySQL Probe'): an app's element shown in the store's report builder, CM-ANL-006 `extension-point`, the cell's Report Creator, as SA-44's lines; and CM-ANL-002 `core` beside it, as an element the merchant's own builder offers. Who made the held app isn't stated: a gap, never `own-service`;
   - `null` (34 items, 27 onward): each carries one of the catalog's reports as an element, 28 by their title, the report's label (item 27's 'catalog_sales_bundle_products'), and the others by their components' ids (`coupon_stats_outer`, `offers_stats_outer`, `catalog_products_abandoned_cart…`, `catalog_products_requests…`; one is titled 'catalog_customer_info'). Each is the same thing as that report-catalog entry here: CM-ANL-002 `core`, as entries 2 to 35. The widget states no gate, so it takes no scope; name the catalog's gate (`charity`, `t1`) in `reading`.
5. **A category is not a gate** and gives a widget no line (M-6, refined): the widget only sits under it. Its category goes in `reading`. Only the category entry whose own words name another capability's thing takes a second line: 47 Performance Summary, CM-ANL-003.
6. **The market tooltip** ('The data shown gives you a unified overview across all your store’s markets.', `shown_data_represents_general_view_and_includes_all_markets`, shown where the store has the feature `multi-countries` and a `market_scope`) is a note on the widget's data, not a gate and not a thing of the widget's own. It is named in `reading` and takes no CM-MKS-001 line or scope. The alternative, a `shows` line on CM-MKS-001 with scope `multi-countries` (M-14), would change no cell; the coordinator may rule it.
7. **Terms** come from the entry's text: the title key and the category for a widget (`most_orders_time;sales`), the label key and the slug for a report, the label and value for a category. The English and Arabic words are quoted in `reading` from `reportsv2.json`, by the key.
8. **Leads set aside as no leads:** CM-INV-010 and CM-AIA-003 (by 'Displays', 'حسب', 'such', words of every description), CM-ACC-001 and CM-MKS-009 (by `merchant` and `data` in the tooltip's condition), CM-MKS-001 (by `multi-countries`, rule 6), CM-MKS-007 (a homonym: a store's conversion rate, not a currency's), CM-PLN-001 (by 'performance'), CM-CUS-003, CM-ORD-009, CM-CHN-001, CM-CHK-006, CM-TRU-005 (by name only).

## Entry 1, the Partners portal's settings

One section, 'General Settings' / 'الاعدادات العامة', with three pages. A container: it goes on CM-PTN-002, the partner account's settings, the capability of its pages, as SA-35 and SA-36 placed `/settings/id-verification` and `/settings/connections` (M-13). Its third page, 'Protection and Security', 'Enable two-factor authentication' (Arabic 'تحكم في المصادقة الثنائية', control two-factor authentication), takes CM-TRU-001, as SA-35, SA-36 and SA-38 placed `/settings/security-settings`. ID Verification and Connections share the container's CM-PTN-002 line rather than repeating it. Connections names 'third-party apps': SA-35 read GitHub there, the partner account's own connection, not an app's authorization by a store (CM-API-002 set aside). Every page has `showAlert: false`, in `reading`.

## Entries I couldn't tell, and what would settle each

- **The widgets and categories: CM-ANL-002 or CM-ANL-003.** The categories' 13 subject values are the names of Store performance's own reports (`reportsv2:performance_summary`, `orders`, `sales`, `customers`, `visits`, `landing_pages`, `wishlists`, `conversion_rate`, `abandoned_carts`, `payments`, `shipping`, `stock`, `customer_wallet`; `performance-reports/demo@en/items.jsonl`). Create report's page is titled 'Salla | Store performance | Create report', and the saved custom report opens as a tab of `/reports/performance?report=<id>` (run `20261008T212405Z-journey-reports-create-demo`, steps 2 and 7). So the builder and its elements could be CM-ANL-003's, store performance. I kept SA-12's CM-ANL-002 for `/reports/create`, as the brief asks; the coordinator aligns SA-12, SA-45 to SA-47 either way. Neither changes a cell.
- **12 to 14, gate `charity`; 31, gate `t1`.** The catalog states the gate and not its meaning. The demo store, on Pro, opened all four (run `20261008T213916Z-journey-report-catalog-demo`, steps 12 to 14 and 35), and no features list holds `t1` or `charity`. A run of a store that the gates withhold, or the reports app's bundle, would settle what each is. `charity` is near CM-SEL-007 (donations); no line, by rule 1.
- **36, App Widget, `extension-point`.** It rests on the category's name and on its three widgets' publisher, an app id, whose data come through `/platform/partners/<id>/dev`. Whether the merchant's builder shows the widgets of every app installed, or only of the held partner's dev app, isn't stated.
- **78, 79 on CM-MKT-008** (rule 3). If the coordinator keeps them with the reports only, their second lines go; CM-MKT-008@salla would still become held from SA-25's Order Source line.

## A structure whose items and sources disagree

- **`report-widgets`:** `items.jsonl` holds each widget whole, with `thumbnail` and `config.component` (its type, properties and `sources`, each a URL and a jmespath transform). The entry's rendering leaves out `thumbnail` and `config.component`, so the widget's data source isn't in its text. The source governs: each reading names the URLs from `source.json`.
- **`report-catalog`:** each item holds the report's components and sources, but not its columns, which the report body holds (`report-<category>-<slug>.json`, `schema`, `columns`, `headerName: catalog_col_*`). The columns are below, for the second stage.
- **Labels are translation keys** (`catalog_*`, widget titles such as `most_orders_time`), as the register says. The words are in `reportsv2.json`. One key misleads: `products` there is 'Cost of goods sold' / 'تكلفة المنتجات المباعة', not the Products category, so entry 48's reading doesn't quote it.

## For the second stage: what the sources state that no entry holds

- **CM-CAT-012 (holds nothing):** the profit reports' columns `catalog_col_cost_price` 'Cost Price', `sell_price` and `profit` per product (`report-catalog/demo@en/report-products-profit_per_product.json`, and `..._per_bundle_product.json`). The cell's note gives Salla's profit analytics to domain D, so I gave no line.
- **CM-MKT-016:** Notify When Available's report (`report-products-order_per_product.json`) with 'Clients Notified' and 'Clients Awaiting to Be Notified' (`catalog_col_clients_notified`, `catalog_col_clients_awaiting`).
- **CM-MKT-003 or the bank offers' cell:** Promotions' column `is_bank_offer`, 'Bank Offer' (`report-marketing-special_offers.json`), and its filter of offer types from `/merchant-reports/v1/sales/offers/get-offer-types`.
- **CM-SHP:** 'Shipping carrier performance during the selected period, based on ratings, completed shipments, cost, and delivery time.' (widget 80; `reportsv2.json`): customers' ratings of carriers, a lead for whichever cell holds shipment ratings.
- **CM-ANL-002:** the reports' Sales Channels filter (run `20261008T213916Z-journey-report-catalog-demo`, step 2, 'Sales Channels'; steps 39 and 40 its 'Mobile App'); 'Report elements 0/16' on Create report (the register, a limit: a quality if a held page states it).
- **CM-MKS-001:** the market tooltip (rule 6), and `merchant.market_scope` read from the browser's storage.
- **CM-ANL-006:** the app widgets' data route `/platform/partners/<REAL_APP_ID>/dev?url=…&p_id=…`, the dev endpoint of the Report Creator (SA-47's items).

## The checker's lines, read again

- **`CHANGES` CM-MKT-008@salla gains `core` and becomes held, by lines 83 and 85** (78 Order sources, 79 Ad campaign performance). I read both against `source.json` and `reportsv2.json` again: 'Order sources and their conversion rates during the selected period.' and 'Performance of paid ad campaigns during the selected period, including visits, orders, sales, and conversion rates.', from `/merchant-reports/v1/conversion-rates/purchase-sources` and `/purchase-campaigns`. Kept (rule 3). SA-25's Order Source line, under the ruling after SA-25, would make the same change; the amendment hasn't run.
- **`NOTE` line 54, a product named with the platform's brand:** the category Salla Point. It is `core` because it is a category of Salla's own report builder, whatever the brand names; Salla Point's own maker is CM-POS-001's matter.
- **`NOTE` line 69, first lead CM-INV-010 holds nothing:** by 'Displays' and 'حسب', words every widget's description holds. No lead (rule 8), as SA-44 found.

## Problems with the brief or the script

- **The rendering of a JSON item leaves out keys** (`config.component`, `thumbnail`), so an entry's text can lack what places it. `show` could print an item's every key, or say which it left out.
- **Translation keys as labels.** The checker takes terms from the entry's text, which here holds only keys and slugs; the words are in the locale. I quoted the words in `reading` and kept the keys as terms.
- **Apostrophes:** as SA-44 did, I wrote ’ in prose, so that each ' … ' in a reading is a quote, and quoted no string that holds an ASCII apostrophe.

The checker’s last line, for SA-45: `80 of 80 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **CM-MKT-008 gains `core`, and it stands.** The widgets 'Order sources' and 'Ad campaign performance' credit orders to their sources and paid campaigns, as the ruling after SA-25 reads Order Source. It is the one exception to 'a report kind stays with the reports', since the widget's words state the attribution itself.
- **The report builder stays on CM-ANL-002.** Salla puts it under Store performance ('Store performance | Create report'), but a report the merchant composes is a report. SA-29 keeps Store performance's own tabs on CM-ANL-003. SA-46 and SA-47 keep to this batch's lines.
- **The gates `charity` and `t1`** stay as scope, with what they mean not stated.
- **The market tooltip** stays in `reading`: a widget shown where the store has `multi-countries` states nothing of markets itself.
- **App Widget's second line,** `extension-point` on CM-ANL-006, stands: widgets published by an app, with the maker a gap.
- **Cost:** 9.6 million tokens over 56 requests, about 120,000 an entry. One cell changes, CM-MKT-008, as SA-25's already does.
