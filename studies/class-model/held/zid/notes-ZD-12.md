# Notes on ZD-12 (Zid: `store-plan-policies`, items 362 to 491)

**What the batch holds:** 130 entries, at `high` effort, all of `store-plan-policies` (`zid/structures/store-plan-policies/items.jsonl`, lines 362 to 491, `products_analytics.number_of_times_added_to_cart` to `terms_&_conditions.exchange_and_return_policies`). All evidence is at other-product-class@0d79b794f. The policies are the Demo Store's (store 127604), on `new_professional.yearly` (`meta.json` `of`), from the answer `meta.json` names under `source`: `GET /v1/managers/account/profile`, run 20261028T144855Z-dashboard-routes-en.

**Where the rest is.** ZD-9 placed items 1 to 101, ZD-10 items 102 to 231 and ZD-11 items 232 to 361. I read their lines and notes, with the coordinator's checks, first, and kept to them. ZD-13 holds the rest, from item 492 on, and hasn't run. `products_analytics.*` is split between ZD-11 and this batch.

**Count:** 130 entries, all on a capability: 0 `new`, 0 `out`. That makes 145 lines, all `capability`, with 141 `core` and 4 `shows`. There are no `own-service`, `extension-point` or `outside` lines and no filler. Three lines carry a quality from `config`.

## How the entries were read

I kept the earlier batches' rules, with the coordinator's checks:
- **Enabled policies** (`enabled: true`, a plan in `available_in`, `policies: true`; 127 here): `core`. The `scope` is the plan key the source states the policy is available in. The reading says 'available in <plan> (<Arabic>)', with no claim that this is the lowest plan including it.
- **Disabled policies:** `shows`.
  - `shipping_&_fulfilment.nitros` and `.torod` have `available_in: []` and `policies: null`: their scope is `Demo Store (store_id 127604)`, as before.
  - **`service_fee` is the one disabled policy that states a plan** (`items.jsonl`, line 424: `enabled: false`, `config: null`, `available_in` Starter / البداية / `new_starter`, `policies: null`). It is the only such item in the structure: no other item is disabled with a plan. I kept the coordinator's rule, so its scope is `new_starter`, and its reading says it is disabled for the Demo Store though `available_in` names Starter. What a plan stated beside `enabled: false` means isn't stated. It is for the plans' cells at Zid's amendment.
- **Terms.** The only term is the key. No item has a label.
- **Keys named for a product** (`nitros`, `torod`) take their group's capability, read with the App Market category the cell cites, as ZD-10 and ZD-11 did. Neither key's words say what the product does, and no key names a maker, so no line has a filler.
- **Exports and imports** take a CM-MIG-001 line beside their thing's line (6 lines).
- **The analytics' measures** (`products_analytics.*`, `promotions_analytics.*`, `summary_analytics.*`) are on CM-ANL-001, and the Sales reports' columns (`sales_reports.*`) on CM-ANL-002. They name no other line, as ZD-9 to ZD-11 placed the measures. There is one exception, `promotions_analytics.number_of_discount_codes` (below).
- **A config's feature takes its line,** as ZD-10 gave `coupons.multiple_coupons`'s `with_advanced_analytics` a CM-ANL-001 line: `shipping.methods`'s `allow_prioritization: true` takes CM-SHP-015, as ZD-4 placed shipping-prioritization (ZD-E-114f5af8). Every other config value goes in `reading`:
  - `allow_all` and `allow_selected` (`products.bulk_edit_products`, `products.export_products`);
  - `allow_bulk_action` (`questions_&_ratings.*`);
  - `zidship_only` (`shipping.couriers_customization`);
  - `allow_custom` (`store_design_options.themes`);
  - `no_time_limit` (`store_domain.request_domain`).

### Pages and locales that clarify the keys

As in ZD-11, I read held pages and the dashboard's strings to clarify the keys only (brief, rule 1), and quoted them at their files:
- **The analytics' tabs:** 'Promotions' and 'Summary' (`dashboard-locales/items.jsonl`, lines 16306 and 16308, of `analytics:tabs.*`, lines 16302 to 16308). The measures' own names are at `analytics:marketing.*` (lines 16130 to 16219), such as 'Number of discount codes' (16165) and 'Customer funnel' (16216).
- **The Sales reports page,** `20261028T160128Z-dashboard-routes-rest-en/steps/179.text.txt`, lines 41 to 80. Its columns are 'Total sales', 'Cogs', 'Discounts', 'Shipping revenue', 'Shipping cost', 'Tax amount', 'Gross margin', 'Returned orders value' and 'Number of cancelled/returned orders'. The tooltips are at `reports:sales.tooltips.*` (lines 3378 to 3407).
- **The SEO store pages,** `steps/054.text.txt`: the home page's 'SEO title (Arabic)', 'Meta description (Arabic)' and 'Sitemap' (lines 53 to 77). The dashboard names the SEO section `navbar:seoEnhancement`, 'SEO' (line 7457), the policy group's own word.
- **The Brand page,** `steps/132.text.txt`: 'Copyright text' (line 53) and 'Business center' (line 76).
- **The Themes page,** `steps/121.text.txt`: 'Theme library' and 'Custom themes' (lines 43 and 53).
- **The theme editor's sections** 'Header' and 'Footer' (`theme-editor:mainSections.*`, lines 2102 and 2101).
- **Store information's tabs:**
  - 'Store information', 'Business details' and 'Business address' (`settings:information.main.tabs.*`, lines 2791, 2790 and 2789);
  - 'Business center' (`settings:information.store.labels.businessCenter`, line 2801).
- **The product types:**
  - 'Grouped product' (line 4513), 'Voucher' (4505) and 'Dynamic Bundle' (4502);
  - the add menu's 'Combine multiple products into one bundle' (7256) and 'Create reusable and purchasable vouchers' (7261).
- **The plans table** `subscription:featuresTable.*` (lines 2291 to 2385): 'Custom shipping methods' (2366, 2367) and 'Storage and packaging services' (2379, 2380).
- **The delivery note:** 'Add delivery note for your customer, such as extra fees, delivery terms, or the expected delivery date.' (`logistics:expectedDeliveryDate.description`, line 9238).
- **The checkout option** `settings:checkout.form.serviceFee`: 'Zid assurance' / ضمان زد (lines 2572 and 19412).

### Limits and values in `config`

Three policies state a value of the kind `quality` records. Each is placed as `<key part> limit: <value>`, or as the config's own key:
- **`store_design_options.language_storefront`** (Elite): `language_limit: 0`. Whether 0 means none or no limit isn't stated, as ZD-10's `group_limit: 0` and ZD-11's `edit_order limit: 0`. The policy is enabled, which suggests no limit, but that is a reading.
- **`store_design_options.sdk_theme`** (Enterprise): `sdk_theme limit: 5`. CM-SFR-002's cell has the plan line Store - SDK Template Design (Up to 2), on pro (ZD-S-1001). The two numbers differ: the limit's unit (themes, templates) isn't stated.
- **`technical_support.technical_support`** (Elite): `response_time_in_hours: 3`, a response time for Zid's support (CM-ONB-003).

**The plans available in.** Enterprise (`enterprise`) and Elite (`elite`) appear again, on policies enabled for this Professional store:
- Enterprise: `products.bulk_edit_products`, `products.export_products`, `questions_&_ratings.filter`, `store_design_options.sdk_theme`, `store_design_options.themes`, `store_domain.request_domain`;
- Elite: `questions_&_ratings.delete`, `.disable`, `.publish`, `shipping.couriers_customization`, `shipping.methods`, `store_design_options.language_storefront`, `technical_support.technical_support`.

The Elite and Enterprise questions-and-ratings policies each carry `allow_bulk_action: true`, beside the `bulk_*` policies on Growth.

**Sales reports and the cell's plans.** All of `sales_reports.*` are available in Professional. The CM-ANL-002 cell's التقارير is 'خاصة فقط لباقة الأعمال الكبيره ، النخبة ، الإحترافية' (ZD-S-1048).

### Where I kept to the model and earlier batches

**Pages and routes placed before:**
- `products.brands`: CM-CAT-005, ZD-1's Brands (ZD-E-2ebc7f5d).
- `products.bulk_edit_products`: CM-CAT-001, with ZD-5's products/bulk-edit (ZD-E-51d8cc5b).
- `products.delete_products`: CM-CAT-001, with ZD-5's Trash bin (ZD-E-1661ea01).
- `products.products_arrangment`: CM-CAT-001, ZD-5's Product sorting (ZD-E-4f3a7d6e).
- `products.metafields`: CM-CNT-002, ZD-1's Custom fields (ZD-E-e4375347).
- `products.stock_logs`: CM-INV-002, ZD-5's Inventory stock changes (ZD-E-dc08a83f), with the cell's Inventory Management Logs (ZD-I-0244).
- `products.similar_products`: CM-MKT-023, as ZD-6's Similar Products (ZD-E-d8585d70) and ZD-11's `orders_products_specifications.similar_products`, on the coordinator's decision.
- `products.product_filtration`: CM-SFR-013, ZD-1's Filters (ZD-E-f6c8b5fb), under the permission `manageFiltrationSettings`, whose word "filtration" the key shares.
- `sales_reports`: CM-ANL-002, ZD-5's Sales reports (ZD-E-8ed14cad).
- `seo_enhancements.*`: CM-CNT-007, ZD-1's SEO (ZD-E-c1faddd4) and Store pages (ZD-E-ebc79fa9).
- `store_design_options.custom_robots`: CM-CNT-007, ZD-1's Robots.txt (ZD-E-3fd6a495).
- `store_design_options.custom_llms_txt`: CM-AIA-005, ZD-1's llms.txt (ZD-E-4ff63e71).
- `store_design_options.store_brand`, `.store_identity` and `.copyright_statement`: CM-SFR-001, ZD-1's Brand / هوية المتجر (ZD-E-55895a88).
- `store_design_options.themes`: CM-SFR-001, ZD-1's Themes (ZD-E-c28dc0e8).
- `store_design_options.store_main_menu`: CM-CNT-005, ZD-1's Menu.
- `store_design_options.landing_pages`: CM-SFR-006, ZD-1's Landing pages.
- `store_design_options.extra_pages`: CM-CNT-003, the cell's Manage additional pages / إدارة الصفحات الإضافية (ZD-I-0539).
- `store_domain.*`: CM-SFR-008, ZD-1's Domains list and ZD-5's Link existing domain (ZD-E-8652b562).
- `store_info.*`: Store information's three tabs:
  - 'Store information' and 'Business address' on CM-ACC-006 (ZD-E-39413325, ZD-E-59097d2d);
  - 'Business details' on CM-ACC-004 (ZD-E-4699c09a).
- `store_language_and_currencies.*`: CM-MKS-006 and CM-MKS-008, ZD-1's Languages & currencies (ZD-E-0f96f279).
- `store_whatsapp.use_without_subscription`: CM-NTF-004, ZD-1's Whatsapp (ZD-E-4a0d6399).
- `shipping.address_fields_customizations`: CM-CUS-008, ZD-5's customize-address (ZD-E-74a75376).
- `shipping.custom_shipping`: CM-SHP-015, ZD-5's custom shipping methods (ZD-E-0cf2e9ae).
- `shipping.pickup_service`: CM-SHP-007, ZD-5's Pickup in store (ZD-E-b591d10d).
- `subscription_management.*`: CM-PLN-001, with each part's own cell:
  - payment options: CM-PLN-005;
  - purchase history: CM-PLN-004, ZD-4's Billing transactions;
  - recurring payment: CM-PLN-002;
  - subscription data: ZD-5's Billing (ZD-E-a21cabe4).

  Each part also takes CM-PLN-001, as ZD-11 gave each `order_management_new_order.*` part its group's line: each is a part of managing the store's subscription. The leads CM-SEL-001 (subscriptions a store sells) and CM-APP-003 (app charges) are homonyms.
- `terms_&_conditions.*`: CM-CNT-008, ZD-4's legal pages (ZD-E-af5d4e29, ZD-E-5361e877).

**Plan lines the cells hold:**
- `products.availability_notifications`: CM-MKT-016's Product Availability Notification, on growth and pro (ZD-S-0924). The lead CM-MKT-017 (wishlist notifications) is a different thing.
- `products.barcode_printing`: CM-CAT-015.
- `products.bundle_offers` and `.dynamic_bundle`: CM-SEL-006 (Bundle Offers; Add Dynamic Bundle).
- `products.downloadable` and `.voucher`: CM-SEL-002 (Create Downloadable Product; Digital Vouchers).
- `products.gifting_products`: CM-LOY-006.
- `products.wishlist`: CM-LOY-005's Customer Wishlist.
- `products.export_products`, `.import_products` and `.bulk_export_selected_products`: CM-CAT-001's Export Products and Import Products, with CM-MIG-001.
- `products.product_categories`: CM-CAT-003's Product Categories.
- The analytics' measures name the CM-ANL-001 cell's own plan lines where they match, such as Coupons - Coupon Results, Orders per Auto Discount, Total Order Sales Using Discount Codes, Sales Value Over Time, Top-Selling Cities and Customer Journey Stages.
- `promotions_analytics.number_of_discount_codes` takes a second line, on CM-MKT-002. That cell's plan line Number of Discount Codes / عدد أكواد الخصم (ZD-I-0293) has the same words (rule 2). The dashboard's string defines the measure as 'Total number of discount coupons including the deleted coupons' (line 16166). Whether the plan line is the same measure or a limit on how many codes a store may make isn't stated.
- `seo_enhancements.categories` takes CM-CAT-003 too: that cell cites a category's search-engine fields, not on the free plan (ZD-S-1020). `seo_enhancements.products` takes CM-CAT-001 the same way, as part of the product record. That second line is a reading, made by analogy with the categories.
- `sms_campaigns.*`: CM-MKT-007, ZD-1's Marketing campaigns (ZD-E-f32c302f), and the cell's Marketing - SMS Content (ZD-I-0301).
- `store_design_options.css`, `.theme_customization` and `.sdk_theme`: CM-SFR-002 (ZD-S-1002, ZD-S-1075, ZD-S-1001).
- `store_design_options.templates`: CM-SFR-001's Various Ready-Made Templates (ZD-I-0328). The lead CM-MIG-003 (export templates) is a homonym.
- `shipping.zidship`: CM-SHP-002's زد شب / ZidShip, a product named with Zid's brand. The policy includes it, so it is `core`.
- `shipping.couriers`, `.couriers_customization` and `.methods`' prioritization: CM-SHP-015.
- `technical_support.technical_support`: CM-ONB-003.

## The checker's CHANGES, and what I decided

- **CM-AIA-005 becomes held, with `core` (line 97, `store_design_options.custom_llms_txt`).** I kept it. ZD-1 placed llms.txt there (ZD-E-4ff63e71), and its page says 'Manage the information in your llms.txt file to help AI platforms better understand your store and provide accurate responses to customers.' (`steps/075.text.txt`, line 39). Those lines aren't amended yet, which is why the checker flags this.
- **CM-MKT-023 becomes held, with `core` (line 31, `products.similar_products`).** I kept it, on the coordinator's decision for Zid's Similar Products, as ZD-11's line on the same thing.
- **CM-SFR-007 becomes held, with `core` (line 94, `store_design_options.announcement_bar`).** I kept it. The key's words "announcement bar" are the capability's own thing (Storefront announcement bars; Salla's شريط إعلاني أعلى المتجر). The policy is enabled and available in Starter. ZD-11's pop-ups and bars on this cell were all disabled, so `shows`. No held page shows Zid's announcement bar: the policy is its only statement.
- **CM-SFR-015 becomes held, with `core` (line 104, `store_design_options.recently_added_products`).** I kept it, but it is a reading. I read the key, under store design, as the storefront showing the newest products: how the storefront shows products. It could instead be a section of the theme (CM-SFR-001). The only string with these words is the admin home's widget, 'Your most recently added products.' (`home:widgets.productsTable.description`, line 10884), which isn't the storefront. ZD-11's lines (out-of-stock products at the end, the sold and remaining counts) make this cell held anyway.
- **CM-SHP-007 becomes held, with `core` (line 86, `shipping.pickup_service`).** I kept it. ZD-5 placed Pickup in store here (ZD-E-b591d10d: 'Let customers pick up their orders directly from your physical locations.', `steps/098.text.txt`, line 33). The plans table's 'Deliver to customers' addresses or enable in-store pickup.' (`dashboard-locales`, line 2369) names the buyer's pickup too. The alternative is the carrier's pickup of shipments, as ZD-11 read `order_page.setting_order_pickup_times` (CM-SHP-009).
- **CM-SHP-011 gains `core` (line 82, `shipping.fulfillment_service`).** I kept it. The cell holds the App Market category (`extension-point`) and Zid's outsourcing services (خدمات التعهيد, `outside`, ZD-S-0920). A plan policy that includes a fulfilment service is the plan line's `core` (M-9). The plans table's 'Storage and packaging services', 'Comprehensive solutions for product storage and professional packaging.' (lines 2379 and 2380), names what such a service is.
  - **What isn't stated:** whether the policy gates Zid's own service, the outsourcing providers' (which would be `outside`, as the cell's ZD-S-0920), or fulfilment apps.
  - **What would settle it:** the dashboard page or plan line this policy gates.
- **CM-SHP-018 becomes held, with `core` (line 81, `shipping.estimated_delivery_config`).** I kept it, as the narrower thing (rule 2), but it is a reading. The dashboard's strings hold a delivery note per shipping option, 'Add delivery note for your customer, such as extra fees, delivery terms, or the expected delivery date.' (line 9238), with 'Auto-assign expected delivery date' (`logistics:expectedDeliveryDate.timeSlotSettings.autoAssign`). I read them as the delivery promise the store makes its buyers.
  - **What isn't stated:** that these strings are what the key gates.
  - **The alternative:** CM-SHP-001, the shipping settings. The coordinator may prefer it.

## Entries I couldn't tell, and what would settle each

- **`service_fee` (disabled), on CM-TRU-020 and CM-SUP-008, with `shows`.** By its words alone, a service fee could be a fee on the buyer or one of Zid's fees (the lead CM-PAY-007). I read it instead as Zid assurance (ضمان زد), for three reasons:
  - the dashboard's string key for that checkout option is `settings:checkout.form.serviceFee`, 'Zid assurance' (lines 2572 and 19412);
  - Checkout page options shows it as 'Zid assurance', 'Ensure faster customer follow-up and proactive handling of all shipment updates, giving your customers confidence that their rights are safeguarded' (`20261028T155108Z-markets-api-en/steps/006.text.txt`, lines 106 and 107);
  - the development store's feature flags answer holds a flag `service_fee: true` (`20261028T190230Z-devstore-billing-en/answers/hermod.zid.sa/v1/managers/store/feature-flags/3ad39202….json`).

  Both cells cite Zid Assurance's setting, صفحة إتمام الشراء > ضمان زد (ZD-S-0996). The lines are `shows`, so they change no cell. What would settle it: the code that ties the policy to the option, which the repository doesn't hold as items (GAPS.md: the dashboard's API calls).
- **`shipping_&_fulfilment.nitros` and `.torod` (disabled), on CM-SHP-011.** I read their group with the App Market category الشحن والتخزين (ZD-S-0412), which the cell cites, as ZD-11 read products under `marketing`. They could be carriers (CM-SHP-015). Nothing held says what either product does, and no maker is stated.
- **`shipping.countries_and_cities_customization`, on CM-SHP-001.** I read it as the shipping zones' and tiers' countries and cities, which ZD-5 placed on CM-SHP-001. It could instead be the address customization by country (CM-CUS-008), or a shipping method's coverage, 'Countries and cities' (`logistics:serviceLevelDetails.countriesAndCities`). The lead CM-MKS-009 is the API's reference data, a different thing.
- **`shipping.couriers_customization`'s `zidship_only: true`.** I read it as limited to ZidShip's couriers, and placed no CM-SHP-002 line on the value alone, as ZD-11 did with `only_zidship`.
- **`products.grouped_products`, on CM-SEL-006.** The product type's own strings call it a bundle ('Start by selecting the products you want to include to appear as a single bundle for the customer', line 4041). CM-CAT-001's plan line Product Management - Bulk Add Products / إدارة المنتجات - إضافة منتجات مجمعة, 'Create linked product groups for easy display and increased cross-selling opportunities' (ZD-S-0916, growth and pro), may be the same thing: its Arabic مجمعة is "grouped", and the policy is on Growth. The coordinator may join them.
- **`products.product_actions`, on CM-CAT-001.** Which actions it gates isn't stated. I read it as the products list's actions, such as the bulk actions (`products:bulkActions.*`, lines 3709 to 3711).
- **`products.product_filtration`, on CM-SFR-013.** It could be the admin products list's filter, as ZD-10's `customers.customers_filter` (CM-CUS-001). I followed the permission's word `manageFiltrationSettings`, on the storefront's Filters page.
- **`store_info.business_center`, on CM-ACC-004.** 'Business center' sits among the store's accounts, beside Facebook, Instagram and the website (Brand page, `steps/132.text.txt`, line 76; `settings:information.store.labels.businessCenter`). I read it as the Saudi Business Center, which the cell names for verification (ZD-S-0752). It could instead be a link the storefront shows (CM-SFR-001, the Brand page).
- **`store_whatsapp.use_without_subscription`, on CM-NTF-004.** I read it as Zid WhatsApp being usable on Professional without the WhatsApp service's own subscription (ZD-4's whatsapp/subscription, ZD-E-fd58944b). That is a reading.
- **`store_design_options.js`, on CM-SFR-002.** I read the store's custom JavaScript as theme code, with the CSS customization, as the capability's Salla terms join them. It isn't CM-SFR-004, apps' scripts in the storefront. The cell holds no JS statement of Zid's.
- **`store_design_options.header_and_footer_customization`, on CM-SFR-002.** Read with the theme editor's sections 'Header' and 'Footer'. The cell CM-SFR-001's footer text (ZD-S-1076) is close.
- **`store_design_options.themes`' `allow_custom: true`.** I read it as custom themes, which the Themes page lists ('Custom themes', 'Zid Theme Market provides the ability to customize themes for your store'). I placed no CM-SFR-003 line on the value.
- **`store_domain.request_domain`'s `no_time_limit: true`.** Read as no time limit on requesting a domain. What the limit would be isn't stated.
- **`subscription_management.recurring_payment`, on CM-PLN-002 and CM-PLN-001.**
  - **My reading:** the subscription's automatic renewal payment.
  - **The alternative:** recurring payments a store charges its buyers. The dashboard's strings name an 'Eshtarek App fee' on payment links' recurring payments (`payments:paymentLinks.details.recurringPaymentFees`). Read that way, it would be CM-SEL-001.
  - **Why I kept my reading:** its group is the merchant's own subscription, beside purchase history and subscription data.
- **`summary_analytics`, on CM-ANL-001 and CM-ANL-003.** I read 'Summary' as the analytics overview's tab, ZD-1's All analytics (CM-ANL-003). Its measures stay on CM-ANL-001 alone.
- **`sales_reports.product_cost`, `.returned_orders`, `.cancelled_orders_value` and `.taxes`.** These are columns of the Sales reports, measures, and I kept them on CM-ANL-002 alone, as ZD-9 to ZD-11 kept measures off their subjects' cells. The leads each name another cell:
  - CM-CAT-012's Product Cost Report (`shows`);
  - CM-RET-003's plan line Returned Orders, 'Track return orders accurately…' (ZD-S-0910, pro);
  - CM-ORD-004, whose reading keeps Canceled Orders Value as a measure;
  - CM-TAX-001.

  The coordinator may add a line on any of them.
- **`sales_reports.gross_sales`.** The page holds no column named so. I read it beside 'Total sales' (line 62).
- **`terms_&_conditions.complaints_&_suggestions`, on CM-CNT-008 alone,** as ZD-4 placed the legal page. CM-SUP-008 (customer complaints about the store), a lead, has the cell `not-stated`. The legal page gives the store's complaints contacts ('Add complaints & suggestions information for your store', ZD-4), not a complaints record.

## A structure whose items and sources disagree

None found. Each entry's text matches its item at `items.jsonl` lines 362 to 491, in order. The disabled items have `config: null` and `policies: null`. `service_fee` is the only disabled item with a plan in `available_in` (above).

## What a source states that no entry holds (leads for the second stage)

- **The plans table in the dashboard's strings,** `subscription:featuresTable.*` (`dashboard-locales/items.jsonl`, lines 2291 to 2385). It states lines by tier (`lite` = Rise, `growth`, `professional`), such as:
  - 'Account manager', 'Available (4 meetings and annual performance reports)' on Professional (lines 2291 to 2295), for CM-ONB-003;
  - 'Inventory management', '1 free warehouse' and '5 free warehouses' (lines 2320 to 2324), for CM-INV-005;
  - 'Installment options', 'Enable installment plans through tamara and tabby.' (2361, 2362), for CM-PAY-015;
  - 'Bank transfer' by tier, 'Standard', 'Priority' and '24/7 premium' (2356 to 2360);
  - 'Shipping by speed' and 'Shipping by weight' (2375 to 2378);
  - 'Pre-sales consultant', 'Store activation consultant' and 'Zid communities' (2297 to 2311), the last for CM-ONB-003, which holds no community.

  No entry holds them. They read as the plans page's comparison, which ZD-6 may have read from the answer instead.
- **The sales report's 'Payment processing fees'**, 'Zid Payments fees for all orders paid via Zid Payments, including taxes, regardless of order status.' (`reports:sales.tooltips.paymentProcessingFees.description`; page `steps/179.text.txt`, line 72), for CM-PAY-007.
- **The sales report's tabs** 'Cashier', 'Affiliates' and 'Bundle offers' (`steps/179.text.txt`, lines 54 to 57), reports by those dimensions.
- **'Auto-assign expected delivery date'** (`logistics:expectedDeliveryDate.timeSlotSettings.autoAssign`), with CM-SHP-018 above.

## The checker's other lines

- **NOTEs on first leads that hold nothing:**
  - CM-B2B-006 (sales reps, by "sales rep", lines 54 to 64) is a homonym: the key's `sales_reports` read as "sales rep";
  - CM-API-009 (webhooks, by "notifications", line 8) is no lead: the entry is buyers' availability notifications;
  - CM-AIA-003 (AI content generation, by "description, seo" and "product, seo", lines 67 and 69): no key names AI;
  - CM-B2B-007 (buyer portal, by "storefront", line 103): the entry is the storefront's languages;
  - CM-ORD-009 (printed order documents, by "order, summary", lines 135 and 136): the entries are analytics measures.

## Problems with the brief or the script

- None with the script.
- One reading choice the brief leaves open, as in ZD-11: the dashboard's strings often name the same thing as a key with more words (the product types, the analytics' tabs, Zid assurance). I used them to clarify the entries, and quoted them at their files. The `service_fee` line rests most on such a string, since the key's own words ("service fee") don't name Zid assurance.

## The coordinator's check (30 October 2026, after the batch)

- **`shipping.pickup_service` is on CM-SHP-002, not CM-SHP-007.** Its words, the pickup service, are the plan line Merchant Pickup Service that CM-SHP-002's Zid cell cites (ZD-I-0210), beside Schedule Order Pickups - Zid Ship: the carrier's collection of the merchant's shipments. The buyer's pickup in store is the route Zid names `store-pickup`, which ZD-4 placed on CM-SHP-007, so that cell is held without this line.
- **The other readings stand, each marked:** recently added products as a display setting (CM-SFR-015); the estimated delivery's settings as delivery promises (CM-SHP-018), read with the delivery note's 'expected delivery date'; the fulfilment service as a plan line that includes it (CM-SHP-011, M-9); and `service_fee` as Zid assurance, `shows`, on the dashboard's own string.

**The coordinator, after SA-2 (30 October 2026):** this batch's llms.txt line on CM-AIA-005 is `shows` now, and the entry takes CM-CNT-007 `core`. A store's llms.txt is a file the platform writes for AI platforms to read the store; it gives buyers no channel and no purchase, and Zid keeps it in its SEO section (`review-H-rulings.md`, the ruling after SA-2).
