# Notes on ZD-11 (Zid: `store-plan-policies`, items 232 to 361)

**What the batch holds:** 130 entries, at `high` effort, all of `store-plan-policies` (`zid/structures/store-plan-policies/items.jsonl`, lines 232 to 361, `marketing.information_message` to `products_analytics.export`). All evidence is at other-product-class@0d79b794f. The policies are the Demo Store's (store 127604), on `new_professional.yearly` (`meta.json` `of`), from the answer `meta.json` names under `source`: `GET /v1/managers/account/profile`, run 20261028T144855Z-dashboard-routes-en.

**Where the rest is.** ZD-9 placed items 1 to 101 and ZD-10 items 102 to 231. I read their lines and notes, with the coordinator's checks, first, and kept to them. ZD-12 and ZD-13 hold the rest, from item 362 (`products_analytics.number_of_times_added_to_cart`) on. They haven't run. `marketing.*` is split between ZD-10 and this batch, and `products_analytics.*` between this batch and ZD-12.

**Count:** 130 entries. 127 are on a capability and 3 are `new`, with no `out`. That makes 145 lines: 142 `capability` and 3 `new`, with 108 `core` and 37 `shows`. There are no `own-service`, `extension-point` or `outside` lines and no filler. Three lines carry a quality, each a limit from `config`.

## How the entries were read

I kept ZD-9's and ZD-10's rules, with the coordinator's checks:
- **Enabled policies** (`enabled: true`, a plan in `available_in`, `policies: true`): `core`. The `scope` is the plan key the source states the policy is available in. The reading says 'available in <plan> (<Arabic>)', with no claim that this is the lowest plan including it (the coordinator's check of ZD-10).
- **Disabled policies** (`enabled: false`, `available_in: []`, `policies: null`; 37 here): `shows`, with the scope `Demo Store (store_id 127604)`.
- **Terms.** The only term is the key. No item has a label.
- **Keys named for a product** take their group's capability, read with the App Market category the cell cites, as ZD-10 did. Where a key's own part names a thing (`upp_rewards`, `smartarget_stories`, `social_proof_sales`, `nerachat_whatsapp_bot`), it takes that thing's capability. No key names a maker, and a key is a flag's name, so no line has a filler.
- **Exports** take a CM-MIG-001 line beside their thing's line, as ZD-9 and ZD-10 did.
- **The analytics' measures** (`operational_analytics.*`, `orders_analytics.*`) are on CM-ANL-001 and name no other line, as ZD-9 placed the abandoned carts' measures and ZD-10 the financial ones.

### What is new in this batch: pages and locales that clarify the keys

Unlike ZD-10's keys, many keys here have a held page or locale string that names the same setting. I read them to clarify the entries only (brief, rule 1), and quoted them at their files:
- **`orders_and_products_specifications.*` and `orders_products_specifications.*`** are the settings of ZD-1's Orders and products properties (`settings/orders-products`, ZD-E-f53e771c), held at `20261028T150740Z-settings-gaps-en/steps/009.text.txt`. Their locale keys are `settings:orderProducts.*` (`dashboard-locales/items.jsonl`, lines 3000 to 3030 in English, from 19840 in Arabic).
- **`order_checkout_page.*` and some `payment_options.*`** are read with Checkout page options, `steps/006.text.txt`, as ZD-9 read `checkout_page_options.*`.
- **`order_page.*`** are read with the orders page (`20261028T160128Z-dashboard-routes-rest-en/steps/234.text.txt`) and the `orders` locale strings: the bulk actions (lines 6091 to 6102), the exports (lines 6505 to 6545), and 'Order activity' (line 6297).

### Limits and values in `config`

Three policies state a limit, each placed in `quality` as `<key part> limit: <value>`:
- `markets_management.active_markets`: `limit: 5` (Elite). CM-MKS-001's cell already has five markets on الباقة الاحترافية (ZD-S-0749). The store's flag `must_use_markets_pricing` is false (ZD-E-2e0aa613), and the repository's README says the dashboard doesn't offer the Demo Store Markets.
- `multiple_xml_feeds.max_feeds`: `limit: 20` (Elite).
- `order_page.edit_order`: `limit: 0` (Enterprise). Whether 0 means no limit, as CM-ORD-002's plan line Unlimited Order Editing / تعديل الطلبات بدون حدود suggests, or no edits, isn't stated. The policy is enabled, which suggests no limit, but that is a reading (the same open question as ZD-10's `group_limit: 0`).

The other configs give values, which go in `reading`:
- `onboarding.onboarding`: `model: Monthly+Yearly 1:1 Meeting`;
- `order_management_new_order.payment_methods`: `payment_methods: [bt, pl, cod, cop]`;
- `order_management_new_order.shipping`: `only_zidship: false`;
- `payment_options.payment_gateways`: `gateways: [tap]`.

**The plans available in.** Enterprise (`enterprise`) and Elite (`elite`) appear again, on policies enabled for this Professional store:
- Enterprise: `onboarding.onboarding`, `order_management_new_order.payment_methods`, `order_page.edit_order`;
- Elite: `markets_management.active_markets`, `multiple_xml_feeds.max_feeds`, `order_management_new_order.shipping`, `payment_options.payment_gateways`.

Rise (`rise`, الانطلاقة) holds 19 of this batch's policies, as in ZD-9. I kept the source's plan keys as scope, as the coordinator ruled.

### Where I kept to the model and earlier batches

**Pages and routes placed before:**
- `metafields`: CM-CNT-002, ZD-5's meta-fields route (ZD-E-b282ea2b);
- `multiple_xml_feeds.*`: CM-CHN-004, ZD-1's Product Feeds (ZD-E-d2acff45) and ZD-4's seo/feeds (ZD-E-86a03522), whose page gives a feed link to `feed.xml`;
- `options_library.new_option`: CM-CAT-002, ZD-1's Options library (ZD-E-f69da32f);
- `operational_analytics` and `products_analytics`: CM-ANL-001, ZD-5's analytics routes (ZD-E-173fdeea, ZD-E-93823a61);
- `order_page`: CM-ORD-001, ZD-5's orders route (ZD-E-bea90466);
- `order_page.order_custom_status`: CM-ORD-003, ZD-5's Customize status (ZD-E-36de6d4e);
- `order_page.order_return`: CM-RET-003, ZD-5's orders/:id/return (ZD-E-24b225f5);
- `order_page.order_summary`, and `order_management_new_order.order_summary`: CM-ORD-008, as ZD-5 placed orders/:id/summary (ZD-E-452a895a), with the cell's ZD-S-0823. CM-ORD-009's own reading puts Zid's Order Summary there, not in printed documents;
- `order_checkout_page.checkout_constraints`: CM-PAY-019 and CM-SHP-001, as ZD-7's flag `checkout_constraints` (ZD-E-935799cf) and ZD-1's Shipping and payment constraints;
- `order_page.request_due_payment`: CM-PAY-032 and CM-ORD-002, as ZD-9's permission `orders.request.due.payment` (ZD-E-38eaf220);
- `orders_products_specifications` (the bare key): CM-ORD-001 and CM-CAT-001, as ZD-1's Orders and products properties and ZD-7's permission;
- `orders_products_specifications.similar_products`: CM-MKT-023, as ZD-6's Similar Products (ZD-E-d8585d70), on the coordinator's decision.

**Plan lines the cells hold:**
- `merchants_relations.merchants_relations`: CM-ONB-003's Dedicated merchant relation manager (ZD-I-0395);
- `order_page.bulk_change_order_status`, `.changing_order_statuses`, `.order_status`: CM-ORD-003's Bulk Change Order Status, Change Order Status, Order Status;
- `order_page.bulk_change_payment_status`, `.payment_status`, `.bulk_payment_action`: CM-ORD-015;
- `order_page.bulk_order_export`: CM-ORD-001, and CM-MIG-001's Bulk Export Orders;
- `order_page.export_orders_preparation_list`: CM-SHP-009's Export Order Fulfillment List / تصدير قائمة تجهيز الطلبات (ZD-I-0270), with CM-MIG-001;
- `order_page.order_notes`: CM-ORD-013's Order Notes (ZD-I-0271);
- `order_page.order_tags`: CM-ORD-011;
- `order_page.printing_invoice` and `.bulk_print`: CM-ORD-008's Invoice Printing;
- `order_page.printing_shipping_waybill` and `.bulk_print_waybill`: CM-SHP-002's Shipping Label Printing (and the locale's 'Print shipping label');
- `order_management_new_order.*`: CM-ORD-005, the merchant's new order (create.store.orders; ZD-5's Manual orders, ZD-E-61eef07c). A part that names another thing takes its line too: customer information (CM-CUS-001), the order summary (CM-ORD-008), payment methods (CM-PAY-001), shipping (CM-SHP-001), auto dispatch (CM-SHP-009);
- `payment_options.*`: bank transfer (CM-PAY-030), Apple Pay (CM-PAY-012, as ZD-9's `apple_pay_alert_in_all_browsers`), instalments (CM-PAY-015's خدمات التقسيط), online payments (CM-PAY-001), gateways (CM-PAY-011), Zid Pay (CM-PAY-002), and non-online guest payments (CM-PAY-016 and CM-CHK-001);
- `payments.mispay`, `.tabby`, `.tamara` (disabled): CM-PAY-015, whose cell names all three among Zid's instalment providers;
- `product_bundles.*`: CM-SEL-006.

**The disabled groups named for products:**
- `marketing.*` (27, finishing ZD-10's group):
  - the products whose key part names nothing (`klaviyo`, `linkaraby`, `mailchimp`, `masrad`, `noti_money`, `popautomate`, `shrinkit`, `slide`, `smartarget`, `tapfiliate`, `zotabox`) go on CM-MKT-005, read with the App Market category التسويق والنمو (ZD-I-0455), as ZD-10's. I didn't place `klaviyo` or `mailchimp` on email marketing, or `tapfiliate` on affiliates, on the product's name: nothing held says what they are;
  - `quantum_retail_media` goes on CM-MKT-005 too. Its words "retail media" could name advertising (CM-MKT-010, which holds nothing on Zid). I didn't place it there on the key alone;
  - `lucky_wheel` goes on CM-MKT-005, read as a marketing activity. No capability holds a lucky wheel (searched: lucky wheel; spin; gamification);
  - `information_message`, `message_bar`, `popup` and `popup_forms` go on CM-SFR-007, as ZD-10's pop-ups;
  - `instagram_catalog` goes on CM-CHN-004, as ZD-10's `google_merchant_center`;
  - `instagram_follow_us`, `social_follow_us` and `tiktok_follow_us` go on CM-SFR-005 (below);
  - `smartarget_stories` goes on CM-SFR-005, read with the App Market category المحتوى المرئي والقصص (ZD-I-0450), which the cell cites;
  - `nerachat_whatsapp_bot` goes on CM-SUP-004, as ZD-10's `customer_support.chatbot` and `marketing.businesschat`;
  - `reviews` goes on CM-SUP-001, `social_proof_sales` on CM-SUP-003, `upp_rewards` on CM-LOY-004, and `ziadah_upsell_cross_sell` on CM-MKT-021.
- `mobile_apps.*` (2) go on CM-CHN-006, read with the App Market category تطبيقات الجوال للمتجر (ZD-I-0437). That `app_bunches` names the cell's عناقيد التطبيقات (ZD-S-1081), "app bunches", is a reading on the words only.
- `operations.*` (4: `returnplus`, `scribes`, `switchpro`, `yamm`) go on CM-APP-002. Their group's words match the App Market category العمليات وإدارة المتجر (ZD-I-0442), and CM-APP-002, the App Market itself, is the only cell that cites it. No capability holds store operations as one thing. `returnplus` could be a returns app (category المرتجعات والاستبدال, ZD-I-0447, cited by CM-RET-003), but I didn't place it there on the product's name.
- `productivity.zapier` goes on CM-APP-001, the apps a store installs. No App Market category or capability holds "productivity" (searched: productivity; الإنتاجية). I didn't place it on workflow automation (CM-AUT-001) on the product's name.

## The new things

**`new:Minimum and maximum order limit`:** two entries, ZD-E-cac86133 (`orders_and_products_specifications.max_limit_for_order`) and ZD-E-86767b80 (`.min_limit_for_order`). Both are enabled and available in Growth (`new_growth`), so `core`.
- **Its place of its own:** a policy in the plan's own list, which is a plan line. Its setting sits in ZD-1's Orders and products properties page ('Enable minimum order limit', 'Enable maximum order limit', `steps/009.text.txt`, lines 42 and 44), which is not a place of its own by itself.
- **Its names:** English 'Minimum order limit' and 'Maximum order limit'; Arabic الحد الأدنى للطلب and الحد الأقصى للطلب, with تفعيل حد أدنى للطلب and تفعيل حد أقصى للطلب (`dashboard-locales/items.jsonl`, lines 3008, 3009, 3020, 3021 in English; 19848, 19849, 19860, 19861 in Arabic).
- **What isn't stated:** whether the limit is on the order's value or its quantity.
- **Proposed domain, area and parent:** domain C, under CM-ORD-010 (order receiving settings), or as a rule beside the checkout.
  - It isn't CM-ORD-010's daily order limit, which is how many orders the store accepts.
  - It isn't CM-CHK-005's validation, which is app-written rules (a Shopify Function API). That cell's note says Shopify's Order limit apps don't state what they limit, so they could be the same role on Shopify: the coordinator may join them.
- **Searched:** minimum order; maximum order; order limit; minimum order amount; order minimum; minimum purchase; purchase limit; quantity limit; min order; max order; الحد الأدنى للطلب; حد الطلب; حد أدنى; حد أقصى; الحد الأقصى; أدنى; minimum; maximum.

**`new:Shipment receipt by another person`:** one entry, ZD-E-c5337f63 (`orders_and_products_specifications.shipment_receipt_by_different_consignee`). It is enabled and available in Growth, so `core`.
- **Its place of its own:** a plan line, as above. Its setting is 'Show feature for shipment receipt by another person.' in Orders and products properties (`steps/009.text.txt`, line 30, checked on the demo store).
- **Its names:** English as quoted, and the key's "different consignee"; Arabic عرض خيار استلام الشحنة من شخص آخر (`dashboard-locales`, lines 3027 and 19867).
- **Proposed domain, area and parent:** domain C, under CM-SHP-001 (shipping and delivery), or as an option at checkout (CM-CHK-009).
- **Not gifting (CM-LOY-006),** buying a product for someone else: nothing says the other person isn't the buyer's agent.
- **Searched:** recipient; receiver; consignee; another person; someone else; shipment receipt; deliver to; المستلم; شخص آخر; استلام; استلام الشحنة.

## The checker's CHANGES, and what I decided

- **CM-CHN-004 becomes held, and gains `core` (lines 34 and 35, `multiple_xml_feeds.*`; line 3, `marketing.instagram_catalog`, `shows`).** I kept them. ZD-1 placed Product Feeds (ZD-E-d2acff45) and ZD-4 placed seo/feeds (ZD-E-86a03522) here, and the feeds page gives an XML feed link (`20261028T160128Z-dashboard-routes-rest-en/steps/091.text.txt`, lines 55 and 59). Those lines aren't amended yet, which is why the checker flags this.
- **CM-MKT-023 becomes held, with `core` (line 127, `orders_products_specifications.similar_products`).** I kept it. The coordinator decided ZD-4's Similar Products is CM-MKT-023's, and ZD-6's line (ZD-E-d8585d70) is on it. The setting is 'Enable similar products on each product page' (`steps/009.text.txt`, line 52). The `new:Similar products` of one product's page (ZD-E-58ea454e) is the merchant's own choice of products, and it is the coordinator's to align.
- **CM-SFR-007 becomes held, with `shows` only (lines 2, 10, 14 and 15).** I kept them. `popup`, `popup_forms` and `message_bar` name the capability's pop-ups and bars. `information_message` is read as a bar or banner, which is weaker. All are disabled.
- **CM-SFR-015 becomes held, and gains `core` (lines 125, 126 and 128).** I kept them. The capability's own name holds Salla's عرض مرات الشراء and عرض المنتجات التي نفدت في نهاية الصفحة, and Zid's page states the same settings: 'Show out of stock products at the end of the page.' and 'Show product purchase count' (`steps/009.text.txt`, lines 64 and 60). 'Show remaining quantity for products when they reach a certain inventory threshold.' (line 56) is how the storefront shows a product too. It is not the low-stock alert (CM-INV-004), which is its own setting on the same page (lines 69 to 71).
- **CM-SUP-003 becomes held, with `shows` (line 23, `marketing.social_proof_sales`).** I kept it. The key's words "social proof" are the capability's. It is disabled, from the key alone. `sold_products_count` ('Show product purchase count') could also be social proof. I placed it on CM-SFR-015 by its words, which name a display.

## Entries I couldn't tell, and what would settle each

- **`instagram_follow_us`, `social_follow_us` and `tiktok_follow_us` (disabled), on CM-SFR-005.** No capability holds the store's links to its social accounts (searched: social links; social media links; social icons; social accounts; follow; التواصل الاجتماعي). I read them as elements added to the storefront, the cell's design elements beyond the theme. They could instead be marketing (CM-MKT-005), under their group, or a new thing. What would settle it: the App Market apps or the theme setting these policies gate.
- **`onboarding.onboarding` (Enterprise), on CM-ONB-003.** I read it as Zid's support to the merchant by its config's meetings, 'Monthly+Yearly 1:1 Meeting'. The checker's first lead is CM-ONB-004, the admin's setup wizard, which holds nothing on Zid. Meetings aren't a wizard. What would settle it: the plan line or page this policy gates.
- **`order_management_new_order.*`, on CM-ORD-005.** I read the group as the merchant's new (manual) order, by its parts: adding products, customer information, draft orders, payment methods, shipping, the order summary. That it isn't the staff's new-order notification (CM-NTF-002, a lead "by new order") is a reading.
- **`order_management_new_order.auto_dispatch`, on CM-ORD-005 and CM-SHP-009.** No string is held. What "dispatch" sends, a shipment to a carrier or the order to a branch, isn't stated.
- **`order_management_new_order.payment_methods`'s config `[bt, pl, cod, cop]`.** The codes' meanings aren't stated. Read with Zid's own words elsewhere, they could be bank transfer (CM-PAY-030), payment link (CM-PAY-032), cash on delivery (CM-PAY-029) and cash or card on pickup. I placed only CM-PAY-001 and CM-ORD-005. What would settle it: the new order's payment options in the locales or a page.
- **`order_management_new_order.shipping`'s config `only_zidship: false`.** I read it as not limited to Zid's own shipping (ZidShip, CM-SHP-002's زد شب). That is a reading.
- **`order_page.setting_order_pickup_times`, on CM-SHP-009.** The orders' bulk action 'Schedule a pickup time to collect shipment' (`dashboard-locales`, line 6100) names a carrier collecting the shipment. The checker's lead CM-SHP-007 is the buyer's pickup, a homonym. It could also be CM-SHP-002's labels through ZidShip.
- **`order_page.product_sales`, on CM-ANL-002 and CM-MIG-001.** I read it as the orders' export 'Products sales' (`dashboard-locales`, lines 6528 and 6529). It could instead be a column or tab of the orders page.
- **`order_page.bulk_print`, on CM-ORD-008.** Which documents it prints isn't stated, as ZD-8 found for `orders.print`.
- **`order_page.order_updates_history`, on CM-ORD-001.** I read it as an order's 'Order activity' (`dashboard-locales`, line 6297). No capability holds an order's timeline apart.
- **`orders_and_products_specifications.auto_return_of_quantity`, on CM-INV-001.** The page says 'Automatically return canceled orders' product quantities to inventory.' (`steps/009.text.txt`, line 50). The key's "return" could also be read as returns (CM-RET-003), a lead. The page's words name cancellation: CM-ORD-004, whose Zid cell is `not-stated`, would gain a `core` line. I didn't place it there, since the key's words don't name cancellation. What would settle it: the coordinator's reading of the page as clarifying the key.
- **`order_checkout_page.buy_as_b2b`, on CM-B2B-001.** I read it as Checkout page options' 'Allow customers to change their customer type to a company' (`steps/006.text.txt`, line 107). That they are the same setting is a reading.
- **`order_checkout_page.confirm_the_exact_address_after_purchase`, on CM-CUS-008.** Read beside the page's 'Customer address determination' (lines 42 and 43). The cell's checkout setting for the customer's address rests on S-02's statements. It could also be CM-CUS-009 (map services), as ZD-9's `geolocation_service`.
- **`order_checkout_page.customer_notes`, on CM-ORD-013.** The capability's own name is Salla's Customer notes. ZD-9 named CM-CHK-009 for the same page's setting. A notes field the buyer fills in at checkout could be either.
- **`order_checkout_page.send_invoices_via_email`, on CM-ORD-008 only.** Sending by email could also take CM-NTF-004 (message delivery by email). ZD-10 kept `invoice_settings.enable_zid_system_to_send_invoices` on CM-ORD-008 alone, and so did I.
- **`payment_options.payment_gateways`'s config `gateways: [tap]`, on CM-PAY-011.** The cell names Tap (ZD-S-0610). I gave the line no filler, since the config's value is a flag's value, not a statement that Tap does it. The coordinator may read it as one.
- **`payment_options.online_payments`, on CM-PAY-001.** It could be CM-PAY-002, Zid's own online payments, but `payment_options.zidpay` is a policy of its own beside it.
- **`payment_options.zidpay`, on CM-PAY-002 with `core`.** It is a product named with Zid's brand. The plan policy includes it, so it is `core`. The cell's `own-service` rests on Zid Pay's terms, not on this key.
- **`markets_management.active_markets`, Elite, limit 5.** CM-MKS-001's cell has five markets on Professional (ZD-S-0749). That Elite's 5 is the same five isn't stated.
- **The analytics' measures:**
  - `orders_analytics.sales_per_inventory_location` could also take CM-INV-005 (a lead), and `.sales_value_overtime` and `.total_sales` could take CM-ANL-002, whose cell holds the plan lines Reports - Sales Value Over Time and Reports - Total Sales. I kept every measure on CM-ANL-001 alone, as ZD-9 and ZD-10 did;
  - `operational_analytics.in_reverse_to_reversed_average` is read as a returned order's time to its reversal, from the key's words.

## A structure whose items and sources disagree

None found. Each entry's text matches its item at `items.jsonl` lines 232 to 361, in order. Every enabled item has `policies: true`, and every disabled one has `config: null`, `available_in: []` and `policies: null`.

## What a source states that no entry holds (leads for the second stage)

- **`20261028T150740Z-settings-gaps-en/steps/009.text.txt`, Orders and products properties.** Some of its settings may be policies of ZD-12 or ZD-13. If none is, they are leads:
  - 'Automatically change paid new orders status to "completed"' and '... "ready"' (lines 32 and 35), for CM-ORD-003;
  - 'Enable reorder feature' (line 37), for CM-ORD-014;
  - 'Enable manual payment', 'Record manual orders with payment handled outside Zid without affecting your business financial calculations.' (lines 39 and 40), for CM-ORD-005 and CM-PAY-016;
  - 'Enable adding the products to wishlist' (line 67), for CM-LOY-005;
  - 'Enable low stock notifications' (lines 69 to 71), for CM-INV-004, which holds nothing on Zid;
  - its locales add 'Show donation gift feature' and 'Enable Quick Donation' (`dashboard-locales`, lines 3028 and 3030), which the demo store's page doesn't show, for CM-SEL-007.
- **The `orders` locale strings,** `dashboard-locales/items.jsonl`, lines 6091 to 6102: the bulk action 'Duplicate order' (line 6096), for CM-ORD-005 or CM-ORD-014, and 'View orders summaries' (line 6102), for CM-ORD-008.
- **`steps/006.text.txt`, Checkout page options:** the 'Shipping and payment options display', Compact view and Full view (lines 33 to 40), for CM-CHK-001, still not held by a policy so far.

## The checker's other lines

- **NOTEs on first leads that hold nothing:**
  - CM-CUS-007 (consent, by "marketing, whatsapp") is no lead, as ZD-10 found;
  - CM-ONB-004 (by "onboarding") is above;
  - CM-OPS-004 (by "status") is the store's system status, a homonym of an order's status;
  - CM-SHP-014 (by "constraint, order") is app-written fulfilment rules, a homonym, as ZD-10's CM-SHP-013;
  - CM-CHK-004 (by "checkout, purchase") is checkout UI extensions: no key names one;
  - CM-CUS-003 (by "action, bulk") is the customers' bulk actions, not the orders';
  - CM-ORD-009 (by "order summary") is no lead: its own reading puts Zid's Order Summary in CM-ORD-008;
  - CM-CAT-006 (by "tags") is product tags, not order tags;
  - CM-SHP-007 (by "pickup") is above.
- **NOTEs on new things with leads:**
  - CM-ORD-010 holds the store's working hours, and its note keeps Salla's daily order limit, not a limit on one order;
  - CM-ORD-008 (by "receipt") and CM-SHP-020 (by "shipment") are no leads for the consignee.

## Problems with the brief or the script

- None with the script. The leads came from the key's words, as the coordinator's fix intended.
- One reading choice the brief leaves open:
  - Some held pages and locale strings name the same setting as a key, and some state more than the key's words, such as the cancellation in `auto_return_of_quantity`.
  - I used them to clarify the entries, as rule 1 allows, and placed only what the key's own words name. The coordinator may rule otherwise.

## The coordinator's check (30 October 2026, after the batch)

- **The batch keeps to what each key's own words name,** as the brief asks. A product named only by its brand isn't placed by what the product is said to do elsewhere (`klaviyo`, `zapier`, `returnplus`). `auto_return_of_quantity` stays on CM-INV-001 alone: the page names canceled orders as its trigger, not as its thing.
- **The cells it changes stand:** Zid's display settings (CM-SFR-015, out-of-stock products and the sold and remaining counts, which the capability's own Salla terms name), and social proof (CM-SUP-003, `shows`, the policy disabled).
- **Its two new things** (minimum and maximum order limits; shipment receipt by another person) are decided with Zid's others before its amendment.
