# Held pass, Salla, batch SA-46: notes

81 entries (effort high), evidence at observed-sa@b0bd0b163, all of one structure: `report-widgets` (`demo@en`), its items 27 to 110 of 124, the elements Salla offers for Create report (`/reports/create`), answered at `api.salla.dev/reports/widgets` (run `20261008T212405Z-journey-reports-create-demo`, step 2; `meta.json`: `raw/runs/20261008T212405Z-journey-reports-create-demo/responses/0051.json`).

- Entries 1 to 31 (items 27 to 60): publisher `null`, type `agrid`, each carrying one of the report catalog's reports.
- Entries 32 to 81 (items 61 to 110): publisher `salla`, types `pipe` (1), `distribution` (14), `ranking` (19), `unit` (16).

**84 items, 81 entries.** Three items have no entry of their own, because their text is the same as an earlier item's:
- the entry at item 34 (SA-E-8e4aeef2) stands for items 34 (Coupon Discounts) and 35 (Promotions);
- the entry at item 36 (SA-E-80d77057) stands for items 36 (Abandoned Carts), 43 (Notify When Available) and 44 (Returned Products).

The text the three share is `config: {container: {type: container}}`, since their titles sit inside `config.component`, which the rendering leaves out. Each of these readings names every item it stands for. All of them place the same way.

**Placed:** 81 entries on capabilities, none `new`, none `out`, in 84 lines.
- 81 lines on CM-ANL-002, `core`.
- 3 second lines:
  - CM-PAY-009, `outside` (entry 40, item 69, Chargeback rate);
  - CM-LOY-008, `shows` (entry 37, item 66, Customers with referrals);
  - CM-CAT-012, `core` (entry 72, item 101, Total costs).
- No scope, filler or quality on any line.

**Sources read:**
- the brief and what it names;
- SA-45's notes and its placements (its `report-catalog` lines 2 to 35 and its `report-widgets` lines 55 to 80);
- the rulings, their last section included;
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md` (its reports row), `structures/README.md`, the register's rows for `report-widgets`, `report-widget-categories`, `report-widgets-legacy` and `portal-report-builder-widgets`, and `index/ledger-summary.tsv`'s report rows;
- `selection.tsv`'s rows; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run";
- the structure's `meta.json` and `items.jsonl`, each item whole, `config.component` included;
- to clarify only:
  - the titles and descriptions, which are translation keys, in `structures/salla/dashboard-translations/{en,ar}/reportsv2.json`;
  - the catalog's report bodies, for the gates (`structures/salla/report-catalog/demo@en/report-*.json`);
  - the model's cells;
  - S-01's statements S01-SA-180 and S01-SA-181, which CM-PAY-009's cell cites.

## The rules my lines follow: SA-45's, kept

1. **The dashboard's report builder stays on CM-ANL-002, `core`.** This is SA-45's rule 1 and the coordinator's check. A widget is a part of the custom report that SA-12 placed on CM-ANL-002, and CM-ANL-002's note keeps Salla's report kinds with the reports. No widget takes a line on its subject's capability where that cell already holds. That covers CM-LOY-001 (wallet), CM-LOY-004 (loyalty points and prizes), CM-LOY-005 (wishlists), CM-MKT-016 (back in stock), CM-MKT-022 and CM-CHK-007 (abandoned carts), CM-SUP-001 (ratings), CM-ORD-004 (cancellation), CM-ORD-006 (suspicious orders), CM-RET-003 (returns), CM-SEL-002 (digital codes), CM-SEL-006 (bundles), CM-SEL-007 (donations), CM-POS-001 (Salla Point), CM-CAT-002 (product options), CM-CHK-009 (order options), CM-CAT-005 (brands), CM-INV-005 (branches), CM-CHN-001 (sales channels), CM-SHP-001 and CM-SHP-009 (shipping), and CM-PAY-001 (payment methods).
2. **Publisher `null`** (SA-45's rule 4): each of these 31 entries carries one report of the catalog, by its title key. Its reading names that report's file and SA-45's entry. A gate the catalog sets on the report goes in `reading`, not in scope, since the widget doesn't state it:
   - `charity`: entries 22, 23 and 27 (Donations, Financial Donations, Quick Donations);
   - `t1`: entry 7 (Abandoned Cart Customers).

   Entry 3 (item 29) is titled `catalog_customer_info`, a key the reports' locale doesn't hold. Its tooltip key, `catalog_customers_purchases_by_customers_description`, 'Purchases by Customers report.', ties it to the catalog's Purchases by Customers (SA-E-3900e295).
3. **Publisher `salla`:** CM-ANL-002, `core`. No item of this batch has an app id.
4. **The category gives no line, and neither does the market tooltip.** The category goes in `reading` (SA-45's rule 5). The market tooltip, `shown_data_represents_general_view_and_includes_all_markets`, is shown where the store has the feature `multi-countries` and `merchant.market_scope`. It is named in `reading` on the 39 entries that carry it (SA-45's rule 6). No item has any other `visibleOn` condition.
5. **Terms:** the title key and the category, as SA-45's rule 7 sets them. The two entries whose container has no title (at items 34 and 36) take the category alone. Each second line takes the key its reading rests on.
6. **Attribution** (SA-45's rule 3) is in no widget of this batch. Nearby cases are under "Entries I couldn't tell".

## The three second lines, where SA-45's rule 1 doesn't reach

Rule 1 keeps report kinds off cells that already hold. These three entries name a thing whose Salla cell holds nothing, or one the coordinator has already placed from the same text.

- **Entry 40 (item 69), CM-PAY-009, `outside`.** Its description key is `financial_claims_percentage_description`, 'Percentage of payments held by the issuing bank due to disputes during the selected period.' It is the only lead of the batch made by a shared identifier. CM-PAY-009's Salla cell already cites the same key and text as `outside`, from S-01 (S01-SA-180, S01-SA-181; P-1 S01-VP-08). By rule 2 ("where a cell's reading cites the same … term, the entry is that capability's too") it takes the same line.
  - No cell changes.
  - The issuing bank is named in the locale's words, not in the entry's text, so it is in `reading` and not in `filler`.
- **Entry 37 (item 66), CM-LOY-008, `shows`.**
  - What it states: 'Customers with referrals' / 'نسبة العملاء الذين أحالوا عملاء آخرين' (the share of customers who referred other customers), with its data from `/merchant-reports/v1/customers/loyality-referral-engagement-rate`.
  - Why it is CM-LOY-008's: the cell's reading found no Salla statement of buyers inviting buyers, and this one shows them. The data's path puts it with the loyalty programme, CM-LOY-008's parent.
  - Why `shows`: it states no referral code, no reward, and no place of its own.
  - **The cell changes from holding nothing to held.**
- **Entry 72 (item 101), CM-CAT-012, `core`.**
  - What it states: Total costs' tooltip key, `includes_only_products_with_cost_price_in_product_details_page`. The English is 'Sum of all operational costs, including cost of goods sold, …'. The Arabic is 'تكلفة المنتجات (حسب التكلفة المُسجَّلة في بيانات المنتج)', the products' cost as recorded in the product's data.
  - Why it is CM-CAT-012's: it names a cost entered on the product, which is CM-CAT-012's thing.
  - Why `core`: the ruling after SA-25 places Salla's product Cost Price (`cost_price`) there as `core`.
  - CM-CAT-012's note gives Salla's profit analytics to domain D, and the entry's CM-ANL-002 line keeps them there. The second line is for the product's recorded cost, not for the analytics.
  - **The cell gains `core` and becomes held.** SA-25's `cost_price` line would make the same change under the same ruling; the amendment hasn't run.

## Entries I couldn't tell, and what would settle each

- **Entry 72, CM-CAT-012:** `core`, `shows`, or no line at all. The last would read the note's "Salla's profit analytics are domain D's" as covering the tooltip too, as SA-45 read the profit reports' `cost_price` columns. The coordinator's reading of the note against the ruling after SA-25 settles it. If no line, CM-CAT-012@salla is still made held by SA-25.
- **Entry 37, CM-LOY-008:** a widget that counts referrals shows the capability only through a report. Settling it needs either the coordinator's ruling on whether a report kind may make a cell that holds nothing held as `shows`, or a held page of Salla's loyalty programme naming referrals. The loyalty app's routes or locales may hold one; I didn't trace them (the brief's "Read as far as the entry's sources go").
- **Entry 40, CM-PAY-009, `outside`:** I followed the coordinator's line. The widget is Salla's own measure, from Salla's `/merchant-reports/v1/payments/complaint-stats-per-store` (`complaint_count`, `financial_claims`). If the coordinator reads the measure as Salla's, its line would be `shows` or `core`, but it would change no cell either way.
- **Measures that credit a result to a cause, kept on CM-ANL-002 alone:**
  - items 62, 97 and 74: 'Recovered carts after reminders' (twice) and 'Abandoned cart recovery rate', 'Percentage of customers who returned to complete their order after abandoning the cart.', which credit recovered carts to reminders;
  - item 83: 'Promotion sales', 'Promotions that generated the most sales during the selected period.';
  - item 80: 'Sales by channel', 'Sales channel contributions to total sales …', and item 92: 'Orders by Sales Channel';
  - item 88: 'Top keywords driving visits', which credits visits, not orders, like SA-45's visit sources.

  None credits orders to marketing campaigns or sources as items 78 and 79 of SA-45 do, so none takes CM-MKT-008. If the coordinator reads recovery after reminders as attribution, or as CM-MKT-022's own measure, items 62, 74 and 97 take a second line. Neither would change a cell: CM-MKT-022 is `core`, and CM-MKT-008 is made held by SA-25 and SA-45.
- **Item 70, 'Suspicious orders rate'** ('Percentage of orders flagged as suspicious …'): CM-ORD-006's cell reads the 'suspicious order' message (SA-S-5051). A second line, `shows` or `core`, would change nothing, since the cell is already `core`. I kept rule 1.

## A structure whose items and sources disagree

- **The rendering leaves out `config.component`** (as SA-45 noted). Three items' texts are then equal, and they collapse into two entries (above). Their titles are in the component.
- **The keys are translation keys.** `catalog_customer_info` (item 29) and the stat cards' labels (`catalog_stat_coupons_title`, `catalog_stat_customers`, `catalog_stat_sales`, `catalog_stat_usage`, `catalog_stat_repeat_rate`, `catalog_stat_offers_title`, `catalog_stat_offers_customers`, in items 34 and 35) aren't in `reportsv2.json`. Another locale file may hold them; I read only `reportsv2.json`.
- **`static` values are sample data.** Some examples: item 93's order types `standard`, `cod`, `digital`, `subscription`; item 92's `store`, `mobile`; item 80's `channel`. These are the widget's placeholder before its data loads, not a statement of which types a store has, so no line rests on them.

## For the second stage: what the sources state that no entry holds

All of these are in `structures/salla/report-widgets/demo@en/items.jsonl`, at the item's line, unless another file is named.

- **CM-ANL-002 / CM-MKT-009:**
  - item 61, Conversion funnel: its stages `visit_store`, `addition_to_cart`, `view_cart`, `start_checkout`, `complete_purchase`;
  - item 108: 'Customers who added products to cart during the selected period.'

  Store events counted by Salla: a lead for whichever cell holds the storefront's own event counts.
- **CM-SUP-001:**
  - item 63's split `four_and_five_stars` / `three_stars_and_below`;
  - item 100's 'Calculated by dividing the total rating score by the number of ratings.' (`reportsv2.json`, `store_rating_description`), the store rating's definition.
- **CM-SHP:**
  - item 105, 'Calculated by dividing total shipping time by the number of outgoing shipments in the selected period.', with its unit `hours`;
  - item 106, the same for the average shipping cost.

  Definitions, perhaps qualities of the kind `qualities.tsv` records.
- **CM-ORD-001:** item 94, Orders Pending Fulfillment: the statuses `waiting_for_review` and `underway`.
- **CM-ANL-002:**
  - item 71's 'based on the statuses you choose' (`return_rate_description`), which ties the return rate to the setting 'Statuses included in reports', already on CM-ANL-002's cell;
  - items 87 to 89's data from `/admin/v2/reports/visits/{cities,keywords,pages}`, Salla's admin API for visits.
- **CM-CAT-012:** items 39 and 40 (Profit per Product, Profit per Bundle Product) carry the columns `catalog_col_cost_price`, `catalog_col_sell_price` and `catalog_col_profits`, as SA-45 listed for the catalog's reports.
- **CM-MKT-003 or the bank offers' cell:** item 35 (Promotions) carries the column `catalog_col_is_bank_offer`, as SA-45 listed for the catalog.
- **CM-LOY-008:** the referral endpoint `/merchant-reports/v1/customers/loyality-referral-engagement-rate` (item 66). A held page of the loyalty programme naming referrals would settle what Salla offers.

## Leads set aside as no leads

None of these is a lead for this batch, as SA-45's rule 8 found:
- **by words every description holds:** CM-INV-010 (by 'display', 'حسب'; the checker's seven `NOTE`s on lines 52, 53, 55, 56, 66, 67 and 68), CM-AIA-003 (by 'such'), CM-NTF-002 and CM-CUS-011 (by 'salla', 'single', 'such');
- **by field names or the tooltip's condition:** CM-MKS-009 and CM-TRU-005 (by 'data'), CM-ACC-001 and CM-EVO-001 (by `merchant` and `feature` in the tooltip's condition), CM-MKS-001 (by `multi-countries`, rule 4);
- **by name only:** CM-APP-002 (by 'category', 'distribution'), CM-MKT-019 (by 'marketing', 'جدول'), CM-CNT-010 (by 'format', 'product'), CM-TAX-001 (by 'sale', 'قيمة'), CM-RET-003 (by 'item', 'order'), CM-SHP-012 and CM-SHP-019 (by 'stock', 'shipping'), CM-SFR-015;
- **by category values, which rule 4 gives no line:** CM-CAT-003 (by 'categories'), CM-LOY-004 (by 'loyalty-program'), CM-LOY-005 (by 'wishlists'), CM-INV-001 (by 'stock'), CM-CUS-001 (by 'customer').

## `new` things

None. Before the second lines, I searched `caps --terms` for chargeback / اعتراض, fraud / مشتبه, rating / تقييم, referral / إحالة, satisfaction / رضا, order option / خيارات الطلب, product option, digital code / أكواد, branch / فرع, brand / علامة تجارية, bundle / مجموعات المنتجات, order type / نوع الطلب, keyword / كلمات البحث, free shipping / شحن مجاني, cancel / إلغاء, delivery time / مدة الشحن, returning customer, repeat purchase, search keywords, visits / زيارات, conversion / تحويل and funnel. Each thing is held by a capability.

## The checker's lines, read again

- **`CHANGES` CM-LOY-008@salla, which holds nothing, becomes held, by line 39** (entry 37). I read it again against `items.jsonl` line 66 and `reportsv2.json` (`customers_with_referals`, both languages). Kept as `shows`, for the coordinator (above).
- **`CHANGES` CM-CAT-012@salla gains `core` and becomes held, by line 76** (entry 72). I read it again against `items.jsonl` line 101 and the key's words in both languages. Kept, for the coordinator (above). SA-25's line makes the same change under the ruling after SA-25.
- **`NOTE` lines 52, 53, 55, 56, 66, 67 and 68, first lead CM-INV-010:** by 'display' and 'حسب'. No lead.
- No other `NOTE`, no `NEW`.

## Problems with the brief or the script

- **Entries that stand for several items.** The rendering leaves out `config.component`, so items with different titles share one text and one entry. An entry then stands for three different reports, and its terms can only be the category. `show` could print the items an entry stands for, as it does for the route structures.
- **Translation keys as labels,** as SA-45 said. The checker tests terms and filler against the entry's text, which holds keys, so the issuing bank of entry 40 can't be its filler.
- **Quoting:** I wrote ’ in prose, as SA-44 and SA-45 did. Where the Arabic titles of items 86 and 109 hold ASCII apostrophes around 'أعلمني عند التوفر', their readings quote the parts on either side as separate quotes. No placement row holds a double quote.

The checker’s last line for SA-46, after this file was written: `81 of 81 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **The two cells this batch changes stand:**
  - CM-CAT-012: Total costs counts the cost recorded in each product's data, the same field the ruling after SA-25 and SA-26 places;
  - CM-LOY-008 is held by a `shows` line: 'Customers with referrals', the share of customers who referred others, from the API's `loyality-referral-engagement-rate`. A metric names the thing, but no referral code, reward or place of its own is stated.

  A report kind otherwise stays with the reports, as SA-45's rule 1 has it.
- **The chargeback rate's line stands** on CM-PAY-009 `outside`, as that cell cites the same key. The issuing bank stays in `reading`: the entry's text, translation keys only, doesn't name it.
- **Items that render the same text share an entry** (34 with 35, 36 with 43 and 44), and each reading names every item it stands for.
- **Cost:** 7.3 million tokens over 52 requests, about 90,000 an entry.
