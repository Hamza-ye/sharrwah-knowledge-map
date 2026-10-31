# Held pass, Salla, batch SA-15: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163: the last 57 rows of `dashboard-edu` (its items.jsonl lines 17 to 73, entries 1 to 57 here), then the first 73 entries of `dashboard-features` (entries 58 to 130). Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-15`).

**Placed:** 128 entries on capabilities, 2 `new` (34, 80), no `out`, in 136 lines. Six entries take two lines: 3, 8, 24, 42, 104 and 129. Supports: 126 `core`, 10 `shows`; no `own-service`, `extension-point` or `outside`. One filler, `tiktok` (3, as SA-8 and SA-32 wrote it). No quality: no entry's own text states a limit, a price, a fee or a duration.

**Sources read:** the brief and what it names; SA-14's notes and placements first, then SA-32's and SA-33's notes, SA-2's check, and SA-32 and SA-34's placements for the edu rows' addresses in `plan-gates`; the rulings; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for both structures, `index/ledger-summary.tsv` and `index/ledger/feature.tsv`; `docs/PLAN.md`'s Instruments and its item 5, for the stores' plans; the edu table's `source.js` (for /products/new); `capture/gates.py` line 148 (one line, for the same row); the banners' names, titles, messages and highlights in `structures/salla/dashboard-translations/en/reminders.json` and `ar/reminders.json`; the features list of the four stores (`structures/salla/dashboard-features/<store>/items.jsonl`); one nav entry (`dashboard-nav-segments/prod/shipping.json`, Bullet Delivery) and one setting's strings (`dashboard-translations/en/settings.json`, `shipping#bullet-delivery-status`); the model's cells, notes and the concern map's own flag statements (`merged/evidence.tsv`, `class_slice.py key`).

## What `dashboard-features`' entries are

Each entry is one feature's value as one or more stores hold it. Here every entry is held under `demo@en` (store-sherawya, Pro), and all but three also under `real-merchant@en` (dandye-dandy-ksa, Pro, `docs/PLAN.md` item 5). The other stores' values of the same feature (the Basic merchant store and the public demo, mostly `enabled: false`) are other entries, in SA-16 and SA-17. The three held under the demo store alone (63 `languages`, 79 `tax-profiles`, 81 `shipping-delivery-zones`) differ on the real store: a second language, `enabled: false`, `can_manage: false`.

The concern map had already read the Basic merchant store's list (`merchant@en`): 61 of the 73 features here are statements of the model (SA-S-2965 to SA-S-3147), and each line cites its statement. Twelve have none: the seven SMS services (85 to 91), the two SMS apps (92, 93), `whatsapp-chat` (101), `inventory::print_export` (104) and `utm-campaign` (127).

## Rules my `dashboard-features` lines follow, for SA-16 and SA-17

No batch had placed `dashboard-features` before. SA-16 and SA-17 hold the rest of it and haven't run. My lines follow these rules, so the coordinator can align the three:
1. **The capability** is the one whose cell already holds the same flag, as the concern map read it from the Basic store's list (its SA-S statement, cited in `reading`). Where the model holds no statement of the flag, the flag's name and its neighbours in the list's order are read for its thing, a reading, said so in the line and in "Entries I couldn't tell".
2. **Supports, by the brief's ruling on flags:** `released: true` is `core`; `released: false` is `shows`, whatever `enabled` says (99, 120 to 122, 127 and 129 are enabled on the Pro stores while not released). One exception, kept from the model: `storage-station` (94) is released, but what it is isn't stated, so it stays `shows` on CM-SHP-001, where the model's SA-S-3077 reads it 'undefined'.
3. **`released` is the answering store's value,** as the model's note on each statement says. Where the Pro stores and the Basic store differ, my line takes its own entry's value and names the other: `paypal` (128) is released on the two Pro stores and not on the Basic one (SA-S-3145, `shows` in the model), so my line is `core`.
4. **Scope:** the feature's `plans`, in the list's own identifiers and order, repeats dropped (`plus, pro, special, pro` gives `plus;pro;special`; `customer-wallet` keeps `special;pro;plus`), as SA-32's rule 4. No store label in the scope: every feature here names its plans.
5. **The store's values go in `reading`:** `enabled` for each store holding the entry, with the store's name and plan; a feature's other keys (`default`, `languages`, `product_id`, `price_id`, `can_manage`, `app_id`, `url`).
6. **Terms:** the feature's name, the entry's only word for its thing.
7. **No filler from a flag's name:** a flag named for a carrier, a payment provider or an SMS provider is the capability's evidence, never a slot filler (the brief).
8. **A feature of type `app`** with an install link (`url: https://s.salla.sa/apps/install/<id>`) is placed on its thing, as the model places `zatca` and `size-guides` (type app) on theirs. The link names another place, the App Store's install page, so it takes no CM-APP-002 line. No maker is stated: a gap.
9. **A feature that is an earlier batch's thing keeps that line's capability:** `bullet-delivery-v2` (80) is SA-32's new Bullet Delivery (below). `advance-audit-log` (59), `webhooks` (95) and `user-advance-management` (100) keep the capabilities SA-32 gave the gates they stand for.
10. **`canvas-mode` isn't in this batch.** It is in SA-16 or SA-17. The coordinator's check after SA-2 puts it on Mushammir Studio, CM-SFR-006 and CM-AIA-002, with its plans (plus, pro, special) as scope. But the features list holds it `released: false` on all four stores (enabled on the demo store and the public demo), so under the brief's ruling on flags its lines are `shows`, not `core`. The batch that places it should say so; the coordinator may want to rule.

## Rules my `dashboard-edu` lines follow

I kept SA-14's eight rules, which keep to SA-32's reading of the same table: the line goes on the banner's feature as its `feature_name` names it; scope is `allowedPlans` as written (`team` left unmapped, each line naming the bundle's mapping); supports by the features list's state for the banner's feature; app pages take a CM-APP-002 line; terms from the address's segment; the row's other keys in `reading`; a difference between the edu row's plans and the features list named in `reading`; no CM-PLN-001 line. Where several features could be the banner's, I named the one whose name matches it (`tiktok-pixel`, `affiliate`, `bank-offer`, `cashback-accessibility`, `product-quantity-log`, `digital-code`, `digital-file`, `theme-purchases`): a reading.

**Where my edu lines differ from SA-32's lines for the same address** (SA-32 and SA-34 read these rows through `plan-gates`, often by the address's nav feature; my lines go by the banner, as SA-14's rule 1 says):
- **7, /marketing/campaign/retargeting:** CM-MKT-007, not SA-32's CM-MKT-005. The banner's Arabic name, 'حملات تسويقية عبر الرسائل النصية وإشعارات التطبيق', is CM-MKT-007's own plan line word for word. CM-MKT-005 is its parent; SA-32's line rested on the gate `sweply`. No lead named CM-MKT-007; `caps --terms "sms"` found it.
- **36, /products/quantities/bulk:** CM-INV-002 (Inventory log, سجل كميات المنتجات), by the banner 'Quantities Log' / 'سجل الكميات' and its flag `product-quantity-log`. SA-32 kept the cell's link, CM-INV-001, and named this banner as the alternative.
- **29, /products/importer:** `core` on CM-MIG-001, by the banner's feature `import-products` (released, though enabled on none of the four stores). SA-32's line for the address is `shows`, by its nav feature `products-importer`, not released.
- **54, /products:** `shows` on CM-MIG-001. The banner's own flag is `products-competitor-import-banner` (its key is `edu.products_home_competitor`), not released. SA-32's line is `core`, from the edu row's plans alone.
- **47, /products/new:** scope `basic;plus;team;special`, the row's own plans. SA-32's line carries `plus;team;special` (see "Items against sources").
- **41, /users/roles:** CM-STF-002 alone; SA-32's second line, CM-STF-001, came from its nav feature, which the edu row doesn't name.

Each of these cells is already `core` on Salla, so none changes.

## New things

1. **Custom Product Fields** (الحقول المخصصة), entry 34: the edu row of `/products/options/custom-fields/*`, `team;special`. The same new thing SA-32 named for the same row in `plan-gates` (its entry 117) and SA-33 for `/products/options/custom-fields`, named the same way, with the same place of its own and the same proposal: domain B, area CAT, parent CM-CAT-001. The banner: 'Custom fields let you add options your customers can choose from, such as color, size, dimensions, and more.' No lead. Searched by SA-32 (custom field; حقول مخصصة; product field; attribute; specification; مواصفات; metadata); I searched custom field again and found only CM-CHK-009 (the orders' custom fields) and CM-CNT-002 (whose note keeps Salla's custom fields out).
2. **Bullet Delivery** (التوصيل السريع), entry 80: the released flag `bullet-delivery-v2` (plans plus, pro, special). SA-32 named the new thing for `/shipping/bullet-delivery` (its entry 77), whose nav entry is titled 'Bullet Delivery' and gated by `shipping-routes` (`dashboard-nav-segments/prod/shipping.json`). Its setting, 'Accept express shipping orders', reads 'Enable this option to accept express delivery orders and display express carriers at checkout' (`dashboard-translations/en/settings.json`, `shipping#bullet-delivery-status`). I named it the same way, `core`. Its place of its own is SA-32's: the admin route and nav entry. Proposed as SA-32 proposed it: domain C, area SHP, parent CM-SHP-001.
   - **The checker's NOTE on its leads:** CM-SHP-015 (by the flag's name; its cell holds `bullet-delivery-v2` as a released carrier flag, SA-S-3044, and `bullet-delivery` and `bullet-delivery-page`) and CM-PLN-001 (plan names, no lead). I read CM-SHP-015's cell: the concern map counts the flag among one flag per integrated carrier. The setting's 'display express carriers at checkout' fits that reading too. So CM-SHP-015 `core` is the alternative to the new line, or Bullet Delivery is decided as CM-SHP-015's evidence. The coordinator decides it with SA-32's entry. I gave one line, not two, so the one flag doesn't count twice.

## Entries I couldn't tell, and what would settle each

- **85 to 93, the SMS services and apps:** placed `core` on CM-NTF-004 by their place in the list, a reading. The run of services right after `sms-gateways` (positions 97 to 115 of the demo store's list) holds five names that say SMS (`turkey-sms-service`, `malath-sms-service`, `shamel-sms-service`, `our-sms`, `hisms-service`), but also `intercom-service`. No held statement in this batch's reach says what `msegat-service`, `unifonic-service`, `nexmo-service`, `twilio-service`, `message-bird-service`, `jawal-b-service`, `mshastra-service` or `connect-saudi-service` does. The dashboard's Communication Apps page, or the App Store's pages for the apps 1204217777 and 1492232924, would settle it.
- **101, `whatsapp-chat`** (type app, app_id 1000374481): CM-SUP-004 by its name, chat with customers over WhatsApp (the cell's Salla Chat holds a WhatsApp path). CM-NTF-004 (message delivery over WhatsApp) is the alternative. The app's page would settle it.
- **104, `inventory::print_export`:** two lines, CM-INV-001 and CM-MIG-001 (its export). CM-INV-001 alone is the alternative.
- **127, `utm-campaign`** (not released): `shows` on CM-MKT-008, read by its name as crediting orders to campaigns by UTM parameters. This is the batch's one `CHANGES` line (below). CM-MKT-005 (campaigns) is the alternative.
- **94, `storage-station`:** released, `shows` on CM-SHP-001 as the model reads it (SA-S-3077, 'undefined'). If it is a fulfilment or storage provider, CM-SHP-011 would take it, `core`. Nothing held in reach says so.
- **81, `shipping-delivery-zones`** (not released): `shows` on CM-SHP-001 as the model reads it (SA-S-3045). CM-SHP-008 (Salla's Branch Delivery Zones) is the alternative.
- **125, `mokafaa-alrajhi`:** `core` on CM-PAY-001, as the model's SA-S-3140. CM-PAY-011's cell holds Mokafaa Al Rajhi's payments as a provider's (`outside`, S01-SA-107), and CM-PAY-013's note keeps it under the parent. I kept the model's line.
- **63, `languages`:** its `product_id` 1304367330 and `price_id` 1135067888 suggest the feature is sold as a product with a price (a reading). The list doesn't say. The cell's plan line 'الترجمة الفورية *برسوم إضافية' is a lead. The subscription's add-ons, if a held answer names this product id, would settle it.
- **21, /orders/reservations:** the banner's English name is 'Pre-order', its Arabic 'إدارة الحجوزات' and its message about booking appointments. I took CM-SEL-004 by the Arabic and the message, as the ruling after SA-4 takes one element's more exact words, and as SA-32 placed the row. CM-SEL-005 (pre-orders, flag `pre-order-campaigns`, released, pro and special) is the alternative.
- **30, /importer:** CM-MIG-002, as SA-32 placed the row: the page is the advanced importer (the cell's /importer), its banner image `importer-v2`. The banner's name, 'Import & Export' / 'الاستيراد والتصدير', is CM-MIG-001's term, the alternative.
- **38, /themes:** CM-SFR-001 by the Arabic 'إدارة الثيمات', as SA-32 did. The English 'Theme editor' and its message 'Learn how to customize your theme, arrange sections, and publish a storefront' would put it on CM-SFR-002.
- **3, /marketing/ads/tools/tiktok:** two lines as SA-32 (CM-MKT-009 for the plugin's tracking, CM-MKT-010 for TikTok in Salla Ads' tools). The plugin also 'syncs your products automatically', a product feed, which CM-MKT-009's note leaves to domain E.
- **8, /marketing/carts:** two lines as SA-32: CM-CHK-007 for the list, CM-MKT-022 for the recovery its message names, which CM-CHK-007's note keeps in domain D.

## Items against sources

- **`plan-gates`' row for /products/new carries another row's plans.** `capture/gates.py` keys the edu rows by address (line 148, `edu = {address(x['category']): x ...}`), so the six rows `/products/new?type=*` (plus, team, special) and the row `/products/new` (basic, plus, team, special; `source.js`, `items.jsonl` line 63) fall on one key and the last one wins. The table's `edu_allowedPlans` for /products/new is `plus, team, special`, and SA-32's line (SA-E-afc4ae5d) has that scope. The row's own plans include basic (47 here). The coordinator may align SA-32's line.
- **The features list holds `released` per store.** `paypal` is released on the Pro stores and not on the Basic one; the model read only the Basic one. Other features may differ the same way across SA-16 and SA-17's entries.
- In `dashboard-edu`, the banners' names aren't in the items, as SA-14 found: they are in the locales by `contentKey`.

## For the second stage: what the sources state that no entry holds

From the banners' locale strings (`structures/salla/dashboard-translations/en/reminders.json`, `ar/reminders.json`):
- **CM-LOY-003:** 'With cashback offers, the repeat purchase rate among merchants has increased by more than 55%.' (`edu.marketing_offers_cashback.message`), as SA-33 found on the page.
- **CM-SHP-007:** 'Merchants who use pickup achieve an average order value up to 2X higher compared to delivery.' (`edu.products_branches_new.message`).
- **CM-MIG-005 or CM-MIG-002:** the Arabic message of /products/importer names moving products from Shopify or Zid, 'سواء كنت تستخدم شوبيفاي أو زد، يمكنك نقل منتجاتك إلى سلة' (`edu.products_importer.message`), where the English names Excel files. The /importer and /products banners name 'your previous platform'.
- **CM-CHK-009 and CM-CAT-001:** the Arabic message of /orders/custom-fields names product details too, 'وعرض تفاصيل إضافية للمنتجات' (`edu.orders_custom_fields.message`).
- **CM-SFR-013:** the brands banner's name 'Brands: add & filter' / 'إضافة وتصفية العلامات التجارية' names filtering by brand.
- **CM-MKS-008:** '40+ store languages' / 'إتاحة +40 لغة في المتجر' (`edu.manage_languages.feature_name`), a count the cell's plan line holds already.
- **CM-SEL-002:** the digital product's 'Content protection via limited links or limited downloads' (`edu.products_new_digital.highlights`).
- **Bullet Delivery:** its setting 'Accept express shipping orders' (`dashboard-translations/en/settings.json`, `shipping#bullet-delivery-status.label`).

From the features list, for SA-16 and SA-17's leads: the run of SMS services and apps at positions 97 to 115 (`infobip-service` to `connect-saudi-service`), `whatsapp`, `whatsapp-api` and `whatsapp-otp` beside `whatsapp-chat` (126 to 129), and `pre-order-campaigns` (548).

## The checker's lines, read again

- **`CHANGES CM-MKT-008@salla holds nothing: becomes held, by line 133`** (entry 127, `utm-campaign`). Read again against its source: the demo store's and the real store's lists hold `utm-campaign` `released: false`, plans plus, pro, special, enabled true. The line is `shows`, so the cell becomes held with no placement. Kept. Other batches already place UTM things on CM-MKT-008: SA-25's Order Source (`utm_source`, `core` after the coordinator's check) and the UTM builder (`shows`, SA-E-e6ec033b, SA-E-fc34d3b2), so the cell becomes held by those lines too. The flag's thing rests on its name: a reading.
- **`NOTE line 85`:** the new thing Bullet Delivery has leads CM-SHP-015 and CM-PLN-001. Read above, under New things.
- **`NEW`:** Custom Product Fields and Bullet Delivery, one line each, both earlier batches' new things.
- **Leads that are no leads:** CM-PLN-001 on every entry (plan names); CM-B2B-003 (10, 54: 'product', 'special'); CM-CNT-010 (13, 18: 'product', 'url' in the help article's address); CM-MKT-003 on 51 ('code'); CM-POS-001 on 92, 93 and 101 (by 'app' and 'pro'). None is an entry's thing.

## Problems with the brief or the script

- **The batch message names `canvas-mode`** as a feature to keep to SA-2's check, but it isn't in this batch; and the features list holds it not released, which the brief's ruling makes `shows` (rule 10 above).
- **`show` prints a feature entry's store labels, not its stores' plans.** The plans of the demo store and the real store are in observed-sa's `docs/PLAN.md`, which a line must cite for a store's plan. A line in the brief's known cases naming the four stores and their plans (merchant@en store-1-da Basic, demo@en store-sherawya Pro, public-demo@en giftshop2024 Basic when its list was read, on 9 October, real-merchant@en dandye-dandy-ksa Pro) would save each features batch the lookup.
- **The concern map already read the Basic store's features list,** so most feature entries repeat a statement the model holds. The yield here is the twelve flags the model holds no statement of, and the per-store differences (`paypal`).

The checker's last line, for SA-15: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **`canvas-mode` is released false on all four stores,** so SA-2's two lines for the canvas, Mushammir Studio, are `shows` now. The app is deployed but not offered (SA-32's rule 6). SA-16 and SA-17 place the feature itself the same way.
- **The plan gates' row for `/products/new` had the wrong plans.** The derived table keys edu rows by address without the query string (`capture/gates.py`, line 148). SA-32's line takes the edu row's own `basic;plus;team;special`, as entry 47 does, and `evidence-map.md` notes the defect.
- **The brief now names the features list's four stores and their plans,** and says that a feature's `released` and `enabled` can differ by store.
- **The edu lines that differ from SA-32's stand,** each by its banner's own feature (SA-14's rule 1). None changes a cell.
- **New things:** Custom Product Fields and Bullet Delivery, under SA-32's names. Bullet Delivery's flag `bullet-delivery-v2`, and the model's reading of it as a carrier flag (SA-S-3044), are decided with SA-32's entry 77.
- **Cost:** 14.9 million tokens over 77 requests, about 115,000 an entry. CM-MKT-008 is held already by SA-25's `core`.
