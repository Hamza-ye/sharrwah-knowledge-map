# Held pass, Salla, batch SA-17: notes

80 entries (effort high), evidence at observed-sa@b0bd0b163:
- `dashboard-features`, its last 38 entries (1 to 38): the end of the Pro stores' lists (1 to 21, positions 517 to 559 of the demo store's list), then the items held under one store because its value differs from the others (22 to 38);
- `dashboard-main-navigation`, its first 42 entries (39 to 80): `merchant@ar/items.jsonl` lines 1 to 42, from the mega-menu's button الكل to the group heading التسويق.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-17`).

**Placed:** 78 entries on capabilities, 1 `new` (30), 1 `out` (39), in 86 lines. Four entries take more than one line: 9 and 15 take three, 34 and 63 take two. Supports: 81 `core`, 4 `shows`; no `own-service`, `extension-point` or `outside`. No filler. Three qualities: `multi-countries limit: 10` (12), `max_inventory_types: 5` (15, on its CM-INV-005 line, where the model already records it) and `features_count: basic 50, plus 100, pro 150, special 5000` (24, as the model records it on CM-PLN-001).

**Sources read:** the brief and what it names: the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register's rows for both structures; `index/ledger-summary.tsv` and `index/ledger/feature.tsv` (each feature's gate and landed address); `show --meta` and the selection rows; the rulings, their last section included; SA-15's and SA-16's notes and placements, with the coordinator's checks; SA-20's and SA-21's notes and placements for the same navigation items (`dashboard-nav`), and SA-12, SA-22 and SA-32's lines for `/marketing/referrals`. Sources: the five stores' `dashboard-features/*/items.jsonl`, compared feature by feature; `dashboard-main-navigation/merchant@ar/` and `merchant@en/` `items.jsonl` and `source.html`; run `20261008T113513Z-dashboard-menus`, `steps/019.text.txt` and `steps/002.text.txt` (line 114, 'Basic'), and its run note. To clarify only: `dashboard-translations/en/feature-content.json` and `ar/feature-content.json`, two keys of `en/products.json`, and two apps of `marketplace-apps/api@ar/items.jsonl` (lines 489 and 650). The model: the cells of every capability a line names; the concern map's statements of the Basic store's list (`concern-map/platforms/salla/citations.tsv`) and the cells that cite them (`merged/evidence.tsv`), and `merged/qualities.tsv`.

## `dashboard-features`: the rules my lines follow

I kept SA-15's ten rules and SA-16's four (11 to 14), with the coordinator's checks after both: the capability whose cell holds the same flag, as the concern map read it from the Basic store's list; `released` sets `core` or `shows`, each entry's own store's value; scope from `plans` in the list's order, repeats dropped; the stores' values in `reading`; the feature's name as its term; no filler from a flag's name; a feature of type `app` on its thing, the install link taking no line; an earlier batch's line kept where the feature is the same thing; the locale `feature-content.json` naming the capability where its name is one's own term; two lines where a name names two things; a feature that gates several earlier lines' pages taking their capabilities; a released feature nothing defines placed by its name and neighbours, `core`.

Four more, for the entries held under one store (22 to 38):
15. **A flag stated only by its value** (`manage-products-by-branches-activate: true`, `shipping::has_bullet_delivery: true`, `customer-wallet-edit: true`), or by `enabled` and `configured` with no `released` (`report-visit`), is read by the brief's rule for a store's flag by its value: `true` is `core`, the store holding it its scope (`demo@en`, `public-demo@en`, `real-merchant@en`), as SA-16 scoped `store-status`.
16. **A feature with `plans: []`** is scoped by its store's label, as the brief says for a released flag that names no plan: `prebuilt-cart-offer` (34, `real-merchant@en`), `restriction-product-type` (27, `public-demo@en`).
17. **`released` differs by store again,** and four entries are released on one store where the Basic store, whose value the model read, holds `released: false`. Each line takes its own store's value and names the others:
    - `multi-warehouse-link` (23): released on the demo store alone; the model's SA-S-3525 sits on no cell. `core` on CM-INV-005, team and special, the gate of SA-20's Multi-Warehouse Management.
    - `store-blog` (28): released on the public demo alone; the model's SA-S-3389 is `shows` on CM-CNT-004. Mine is `core`.
    - `affiliate-referral` (29, 36): released on the public demo and the real store; SA-32's line for `/marketing/referrals` is `shows` by the Basic store's value. Mine are `core` on CM-PTN-008, SA-12's capability for the route.
    - `prebuilt-cart-offer` (34): released on the real store alone; the model's SA-S-3317 is `shows` on CM-MKT-003. Mine is `core`.

    Every one of these cells is already `core` on Salla, so none changes.
18. **A key that names a part of the feature's thing takes that part's line** (rule 12 widened to keys): `inventory-management` (15) names `enable_branch_inventories` (CM-INV-005) and `enable_quantity_logs` (CM-INV-002) beside CM-INV-001, each also in its locale's highlights. Its other keys (`enable_sku_inventories` true, `allow_negative_quantities` false) are values, in `reading`.

**Lines that differ from the model's line for the Basic store's statement, or that the model holds on no cell:**
- `product-sale-start` (7): CM-MKT-001, by the locale ('Sale start date', 'Set offers to start automatically') and the products page, which keeps the field under its discounts (`products.json`, `actions_bar.discounts.sale_start.label`). CM-CAT-013 (product pricing) is the alternative.
- `product-advance-management` (9): the locale names it 'Bulk product update'; it gates `/products/editor`, `/products/quantities` and `/products/quantities/bulk` (the ledger), so three lines, SA-20's capabilities for the three pages (CM-CAT-001, CM-INV-003, CM-INV-001).
- `product-default-weight` (13) and `product-show-sku` (14): CM-CAT-001, as values kept on the product record (the ruling after SA-25 and SA-26 on a record's fields). For 13, CM-SHP-001 is the alternative: its locale names carriers and shipping costs.
- `product-score` (20): CM-CAT-001 by SA-16's rule 14; the products page names a product quality score (`products.json`, `quality_score.*`). See "couldn't tell".
- `product-ai-enhance` (21): CM-AIA-003, AI writing a product's name and description (`products.json`, `quality_score.ai_button_disabled_tooltip`).
- `whatsapp` (26): CM-SUP-004, as SA-15 placed `whatsapp-chat`, by the locale's 'Sell and support customers through WhatsApp'.
- `prebuilt-cart-offer` (34): two lines, CM-MKT-003 (the model's, by the flag's name, a cart offer) and CM-SEL-006 (the locale's 'Product bundles', 'Sell multiple products in one offer'; Arabic 'باقات العروض').

## `dashboard-main-navigation`: no batch had placed it

SA-18 and SA-19 hold the rest of it and haven't run. My lines follow these rules, so they can keep to them and the coordinator can align the three:
1. **The structure is the Basic merchant store's rendered menu** (`merchant@ar`, run `20261008T113513Z-dashboard-menus` step 19, Arabic; the English is step 2, whose text shows 'Basic' at line 114). The selection holds the Arabic items only; each reading gives the English label from `merchant@en/items.jsonl` at the same position, which holds the same 133 items and addresses in the same order (the register).
2. **A link is the same thing as SA-20's `dashboard-nav` item of the same title and address,** so it takes that item's capability. Each reading names SA-20's entry. SA-20 kept to the routes' and plan gates' capabilities (SA-7 to SA-10, SA-32, SA-33), so these lines do too.
3. **`supports`: `core`.** Each link is Salla's own admin section. SA-20's rule 2 makes an item `shows` where its gate isn't released; no item here has one (SA-20 found only Multi Market, Import from platforms, Blog and Souq Eljomla, none of them in this part of the rendered menu).
4. **No scope.** The menu's entries carry none (SA-20's rule 3): they are the Basic store's, which each reading names. A nav item's gate (its `feature`) isn't in the rendered entry.
5. **The button الكل (39) is `out`:** it opens the mega-menu over the whole dashboard, a container over the whole admin (the ruling after SA-21).
6. **A group heading** (the `h3` الطلبات, المنتجات, التسويق: 40, 59, 80) is a container on the capability its title names, as SA-21 placed the nav's top-level sections of the same titles: CM-ORD-001, CM-CAT-001, CM-MKT-005. Coming groups (Online Store, Sales Channels, Customers, Staff, Reports; then Tools & Settings: Help Desk, Shipping, Payment, Tools, Logs) keep this rule; `Tools & Settings` itself names only a grouping of several capabilities' pages and would be `out` by the ruling after SA-28, unless the coordinator holds otherwise.
7. **A quick action** (`kind: text`, `parent` a link: the tooltip of the link's Quick actions button, or an item of its popover in `source.html`) is its own entry here, where SA-20's nav item held its actions inside the item. It takes:
   - another capability's line where it is another thing, as SA-20's rule 5: طلب جديد / New Order (42) CM-ORD-005; خيار جديد / New option (64) CM-CAT-002; إضافة قالب جديد under الاستيراد والتصدير (75) CM-MIG-003;
   - its link's capability where it creates the link's own thing or a part of it (where SA-20 named it in `reading` only, since it had no entry of its own): قسم جديد (50), the four cart-option kinds حقل نصي, حقل رقمي, حقل خيارات, حقل موعد (52 to 55), إضافة قالب جديد under قوالب التصدير (57), منتج ملموس (61, a kind of the catalog product, SA-20's CM-CAT-001 line), حملة جديدة (69), قيد جديد (71), فرع أو مستودع جديد (78).
   It is never `out`: each names a kind or a part of a place's thing, not a bare UI string.
8. **A link whose page is two things takes two lines,** as its nav item did: التصنيفات والخيارات (63), CM-CAT-003 and CM-CAT-002.
9. **Leads set aside:** CM-CHK-008 (quick checkout) on the words 'link' and طلب; CM-NTF-002 on جديدة; CM-MIG-001 on التصدير for the export templates (CM-MIG-003, its child, as SA-20); CM-INV-001 on `/products/quantities` (the audit is CM-INV-003).

**Differences between the rendered menu and the nav's data** (for SA-18, SA-19 and the coordinator): the rendered Products group lacks the nav's Multi-Warehouse Management and Multi Market (`/localization`) and Import from platforms (`/products/importer`); its All products offers one quick action, منتج ملموس, where the nav item lists seven kinds of product. The run note counts 'Products (14)'.

## New things

1. **Bullet Delivery** (التوصيل السريع), entry 30: the public demo's `shipping::has_bullet_delivery: true` (`public-demo@en/items.jsonl` line 564), held in no other store's list. `core`, scope `public-demo@en` (rule 15). The same new thing SA-32 named for `/shipping/bullet-delivery` and SA-15 for `bullet-delivery-v2`, named the same way, with the same place of its own (SA-32's admin route and nav entry) and proposal (domain C, area SHP, parent CM-SHP-001). As SA-15 noted, CM-SHP-015 holds `bullet-delivery-v2` as a carrier flag: whichever the coordinator decides for SA-32's entry, this line follows it. No lead; searched with SA-15's and SA-32's terms.

## Entries I couldn't tell, and what would settle each

- **8, `custom-fields`:** CM-CHK-009, the model's line and the gate of `/orders/custom-fields` (the ledger). But the locale's description, 'Custom fields let you add options your customers can choose from, such as color, size, dimensions, and more.', is word for word the banner SA-15 placed as the new Custom Product Fields (`/products/options/custom-fields/*`). If the same feature gates the products' custom fields too, a second line on that new thing would follow. The products' route's gate in `dashboard-app-routes` would settle it.
- **20, `product-score`:** CM-CAT-001, a reading. A product quality score with AI enhancement (`products.json`, `quality_score.*`) has no capability; `new:product-score` with `shows`, no place of its own (one flag and a page's strings), is the alternative. Searched: quality score; product score; enhance; score; جودة; تقييم المنتج (only complaints and carrier ratings came back).
- **26, `whatsapp`** (app 77955124): CM-SUP-004; CM-NTF-004 (message delivery over WhatsApp, the lead) is the alternative, and its locale's 'Re-engage customers interested in buying' would name CM-MKT-007. The app's page would settle it; the App Store's listing held has no app 77955124.
- **27, `restriction-product-type`** (not released): `shows` on CM-CAT-009 by its name. Its neighbours `restriction-online-payment-activation` and `store-status` read as restrictions on the store itself, which no capability holds; if so, it states what a store may sell, not the merchant's product restrictions. Nothing held in reach says.
- **33, `capped-fixed-fee`** (not released): `shows` on CM-PAY-007 by its neighbours, the payment flags. CM-PLN-003 (the platform's fee on sales) is the alternative. It is held only in the real store's list: the Basic store's, the demo store's and the public demo's lists don't hold it.
- **34, `prebuilt-cart-offer`:** two lines (CM-MKT-003, CM-SEL-006). If the ruling after SA-4 takes the more exact words, the English 'Product bundles' and the Arabic 'باقات العروض' (offer bundles) disagree on which; CM-MKT-021 (upsell and cross-sell offers) is a third reading. The offer's page would settle it.
- **38, `report-visit`:** CM-ANL-002, the visits report, `core` on the real store by its value. Its url is the App Store's app 165566897, 'Google Analytics' (line 489), 'هي خدمة تتيح لك تتبع تحركات الزوار داخل متجرك وتحليلها'. The same visitors' tracking would also be CM-MKT-009's (its `google-tag`) or CM-ANL-007's (data sent to an outside analytics platform, which holds nothing on Salla); I placed neither, since the entry names only the report and the link.
- **7, `product-sale-start`:** CM-MKT-001; CM-CAT-013 is the alternative.
- **13, `product-default-weight`:** CM-CAT-001; CM-SHP-001 is the alternative.

## A maker field the App Store's listing holds (for the coordinator)

`store-blog` (28) is type app, app_id 870050397, and `report-visit` (38) links app 165566897. The App Store's listing gives both the company 'سلة' (company id 2038173539; `marketplace-apps/api@ar/items.jsonl` lines 650 and 489). By M-1 that would name the platform as the apps' maker, and `store-blog`'s line would take `own-service` beside `core` (CM-CNT-004 would gain `own-service`). I didn't write it:
- the ruling after WC-4 counts a maker field only where merchants are shown it as one, and no held statement in this batch's reach says the App Store shows `company` as the maker;
- the same company id is given to 83 apps of the listing, among them Zapier, Mailchimp, Klaviyo, Facebook Pixel, Hotjar, Microsoft Clarity and Zoho Books: integrations with third parties' services. The coordinator's check after SA-16 placed Zapier (554657544, of the same company) as `extension-point`, Zapier its filler.

So `company: سلة` may mean Salla publishes the app, not that it makes the service. One ruling on the field would settle every Salla app of that company, and CM-APP-011 (apps the platform's company makes), which holds nothing on Salla. CM-ACC-002's cell lacks 'سلة' as a company name; it holds the group's legal entities.

## Items against sources

None: each entry's text matches its store's `items.jsonl` line in value. Remarks:
- The four stores' lists differ in length: features held in one list only are `manage-products-by-branches-activate` (demo), `shipping::has_bullet_delivery` (public demo), `customer-wallet-edit` and `capped-fixed-fee` (real store). So a feature's line number differs by store; each reading gives its own.
- `languages` holds the public demo's languages as an object keyed `0` and `2` (`{0: {…ar}, 2: {…en}}`), the other stores' as a list.
- In the main navigation, a quick action is a `text` item whose `parent` is its link's position; in `source.html` it is the tooltip (`p.text-xs`) of the link's `s-button` 'Quick actions', or an `h4` of its popover (the cart options' kinds).

## For the second stage: what the sources state that no entry holds

From `dashboard-translations/en/feature-content.json` (and `ar/`), for cells the model holds:
- **CM-INV-001 and CM-INV-002:** 'Adjust inventory manually', 'Track all inventory movements in an activity log' (`inventory-management.highlights`).
- **CM-INV-006:** 'Track all transfers and their statuses.' (`inventory-order.highlights`).
- **CM-SEL-002:** 'Let customers view files through a private link', 'Refresh the link automatically after each visit', 'Disable text selection and copying' (`digital-product-settings.highlights`).
- **CM-CHK-009:** 'Offer add-ons like wrapping and gift cards', 'Customize option prices' (`order-options.highlights`).
- **CM-MKS-008:** the name 'Auto-translation *additional fees apply' / 'الترجمة الفورية *برسوم إضافية' (`languages.name`), a fee mark the cell's plan line already holds.
- **CM-TAX-001:** 'Enter the final price with tax included' (`product-price-tax-included.highlights`).
- **CM-SFR-002:** 'Add custom interactions to your store' (`theme-custom-css.highlights`), JavaScript as well as CSS.
- **CM-CNT-004:** 'Link articles to related products' (`store-blog.highlights`).

From `dashboard-translations/en/products.json`: the product quality score (`quality_score.*`, among them 'Nice! Product quality +{{score}}'), for entry 20's thing.

From `marketplace-apps/api@ar/items.jsonl`: the 83 apps of company id 2038173539 ('سلة'), above.

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that is already `core`, or adds `shows` beside it. An earlier draft gave `store-blog` `core;own-service`, which the checker printed as CM-CNT-004 gaining `own-service`; I read the listing again and set it aside (above).
- **`NOTE` containers, 13 lines:** الكل (line 45, `out`: the whole admin's container) and the twelve links whose quick actions are entries with that link as `parent`. Each link is placed on its own capability; each action has its own line (rule 7). The group headings aren't flagged, since their `parent` is الكل; they are containers too (rule 6).
- **`NEW` Bullet Delivery, 1 line:** an earlier batch's new thing, named the same way.
- **Leads that are no leads:** CM-PLN-001 on every feature entry (plan names); CM-POS-001 on 26 and 28 ('app', 'pro'); CM-CHK-008 and CM-NTF-002 on the navigation (rule 9).

## Problems with the brief or the script

- **The brief's ruling on a maker field (after WC-4) and its M-1 pull apart on the App Store's `company`:** see above. The brief now names the App Store's listing among the clarifying sources, so every features batch will meet this field.
- **`show` prints a quick action's `parent` as its link's text,** which is ambiguous where two links share a title (قوالب التصدير under Orders, entry 56, and under Products, 76). The positions in `items.jsonl` settle it: entry 57's parent is position 17, the orders' templates; entry 75's is position 35, الاستيراد والتصدير.
- **The selection holds the Arabic menu only.** The English items, the same element, carry no entries, so a line's English terms can't be written (rule 5's terms come from the entry). The readings give them.

The checker's last line, for SA-17: `80 of 80 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **The App Store's `company` field is a maker statement,** by the ruling after SA-17. The store shows each app's company to merchants, and 83 apps carry Salla's own: Salla Point, Zapier, Mailchimp, Google Analytics and others.
  - `store-blog`'s line stays `core`, for the dashboard's own blog pages behind the feature (SA-11). The Blog app (870050397), Salla's, is `own-service` evidence for CM-CNT-004, read with the second stage.
  - `report-visit`'s line stands. Its app, Google Analytics by Salla, connects a third party who measures the visits.
- **`custom-fields` (8) stays on CM-CHK-009.** Its locale description matching SA-15's Custom Product Fields banner is a lead for that new thing's decision.
- **The rules for SA-18 and SA-19 stand,** among them the flags stated by value, `core` with the store's label as scope.
- **New thing:** Bullet Delivery, under SA-32's name. The mega menu's 'All' is `out`, as a container over the whole admin.
- **Cost:** 10.8 million tokens over 58 requests, about 135,000 an entry. No cell changes.
