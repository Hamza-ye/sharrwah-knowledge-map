# Notes on ZD-10 (Zid: `store-plan-policies`, items 102 to 231)

**What the batch holds:** 130 entries, at `high` effort, all of `store-plan-policies` (`zid/structures/store-plan-policies/items.jsonl`, lines 102 to 231, `coupons.multiple_coupons` to `marketing.greenbill`). All evidence is at other-product-class@0d79b794f. The policies are the Demo Store's (store 127604), on `new_professional.yearly` (`meta.json` `of`), from the answer `meta.json` names under `source`: `GET /v1/managers/account/profile`, run 20261028T144855Z-dashboard-routes-en.

**Where the rest is.** ZD-9 placed items 1 to 101 and I read its lines and notes, with the coordinator's check, first. ZD-11 to ZD-13 hold the rest (from item 232 on). They haven't run.

**Count:** 130 entries. 129 are on a capability and 1 is `new`, with no `out`. That makes 149 lines: 148 `capability` and 1 `new`, with 86 `core` and 63 `shows`. There are no `own-service`, `extension-point` or `outside` lines and no filler. Four lines carry a quality, each a limit from `config`.

## How the entries were read

I kept ZD-9's rules, as the coordinator checked them:
- **Enabled policies.** A policy with `enabled: true`, a plan in `available_in` and `policies: true` is `core`. Its `scope` is the plan's `package_key`, and its `reading` gives the plan's English and Arabic names and the store's value.
- **Disabled policies.** A policy with `enabled: false`, `available_in: []` and `policies: null` is `shows`. Its scope is the store, `Demo Store (store_id 127604)`.
- **Terms and readings.** The only term is the key. No item has a label, and the dashboard's locales key no string on a policy key (I grepped `dashboard-locales/items.jsonl` for `live_analytics`, `extended_caching`, `customizable_reports`, `faq_page`, `customer_care`, `block_cod` and `corner_ribbon`, and found none). So every line is a reading from the key's words, and says so.
- **Keys named for a product.** A part named for a product takes its group's capability, read with the App Market category the cell cites, as ZD-9 did. Where the key's own part names a thing, it takes that thing's capability instead (as ZD-9's `lableb_search`). No key names a maker, and a key is a flag's name, so no line has a filler.
- **Exports and imports.** An export or import takes a CM-MIG-001 line beside its thing's line, as ZD-9's `.export`.

### What is new in this batch

**Limits in `config`.** Four policies state one, and each goes in `quality` as `<key part> limit: <value>`:
- `digital_products.file_count`: `limit: 15`;
- `digital_products.file_size`: `limit: 2147483648`, with no unit stated. That it is bytes (2 GiB) is an assumption;
- `inventory_locations.active_locations`: `limit: 6`. CM-INV-005's cell has 5 warehouses on Professional, with one more per Zid Cashier device (ZD-S-1021). Whether 6 is that sum isn't stated;
- `customers.create_customer_group`: `group_limit: 0`. Whether 0 means none or no limit isn't stated. The policy is enabled, which suggests no limit, but that is a reading.

**Flags in `config`.** The other configs hold flags, which go in `reading`:
- `coupons.multiple_coupons`: `with_advanced_analytics: true`. It takes a CM-ANL-001 line, as ZD-9's `coupons.analytics`;
- `customer_care.customer_care`: `ticketing_system`, `chat`, `whatsapp`, `call` and `am`, all true.

**Two plans that ZD-6's offered plans don't hold:**
- **Enterprise** (`enterprise`, برنامج الأعمال الكبيرة): `coupons.multiple_coupons`, `customer_care.customer_care` and `digital_products.file_count`. A reading: this is the "large-business plan" of CM-INV-005's ZD-S-1022 and the "Large Business" of CM-SHP-001's ZD-S-0858.
- **Elite** (`elite`, برنامج النخبة), as ZD-9 noted: `customers.create_customer_group`, `digital_products.file_size` and `inventory_locations.active_locations`.

**The store has these policies enabled though they are available in plans that aren't its own.** The Demo Store is on Professional, yet these six policies are enabled for it. So `available_in` can't simply be "the lowest plan that includes it", as ZD-9 read it, unless Enterprise and Elite sit below Professional, which nothing states. It could instead be an add-on or a grant to the demo store. I kept the `package_key` as the scope, as ZD-9 did. The coordinator should read `available_in` again for the plans' cells.

### Where I kept to the model and earlier batches

**Pages the dashboard's batches placed:**
- `customer_referrals`: CM-LOY-008, ZD-1's Customer Referrals (ZD-E-381f5c01);
- `customizable_reports`: CM-ANL-002, ZD-1's Reports (ZD-E-8de85945);
- `faq.faq_page`: CM-SUP-006, ZD-1's FAQs (ZD-E-b75e87bc);
- `financial_analytics` and its measures: CM-ANL-001, ZD-1's Financial analytics (ZD-E-f56068f0). The measures name no other line, as ZD-9 placed the abandoned carts' measures;
- `live_analytics`: CM-ANL-004, ZD-1's Live analytics (ZD-E-18bb9ce9);
- `inventory_product_reports`: CM-ANL-002, ZD-1's Inventory reports (ZD-E-c0926765);
- `inventory_locations.stock_managment`: CM-INV-001, ZD-1's Stock management (ZD-E-1f8e4f76);
- `.transferring_stock_auto_restock`: CM-INV-006, ZD-1's transfer requests with auto restock (ZD-E-206a540c);
- `fostering_charity.*`: CM-SEL-007, ZD-5's Charity fostering (ZD-E-3f16aba9). `.messages_balance` and `.sender_name` also take CM-NTF-004, as the cell's order status balance and Sender Name. The dashboard's strings make sponsoring a charity wait on the sender name's approval (`dashboard-locales`, `charity-fostering:senderNameUnderReview.description`).

**Plan lines the cells hold:**
- Block Customers on CM-CUS-005;
- Block Cash on Delivery on CM-PAY-029 (`customers.block_cod`);
- Create Customer Groups on CM-CUS-002;
- Add Business Customers on CM-B2B-001;
- Customer Information and Edit Customer Data on CM-CUS-001;
- Export Full Quantities and Update Product Quantities on CM-INV-001;
- Update Product Prices on CM-CAT-013;
- Inventory Count on CM-INV-003;
- Transfer Inventory Between Branches on CM-INV-006;
- Display Products by Customer City on CM-INV-010;
- Inventory Withdrawal Priority on CM-INV-009;
- the customer wallet on Professional on CM-LOY-001;
- Loyalty Programs, Earned Points, Points Redemption Methods and Points-Earning Customers on CM-LOY-004;
- خاصية الإهداء on CM-LOY-006;
- the invoice settings and ZD-S-0823's order summary on CM-ORD-008.

**The disabled groups named for products:**
- `customer_support.*` (29). The products go on CM-SUP-005 and the chats on CM-SUP-004, both read with the App Market category خدمة العملاء والمحادثات (ZD-I-0435), which both cells cite. On CM-SUP-004 are `all_day_chat`, `chatbot`, `livechat` and the four WhatsApp keys, as the store's WhatsApp chat and widget that earlier batches placed there. The contact-us keys, `contact_form` and `click_to_call` go on CM-SUP-005, since no capability holds a store's contact page (searched: contact us; contact form; اتصل بنا; تواصل معنا; call). `customer_support.faq` goes on CM-SUP-006.
- `finding_products.*` (3) go on CM-CAT-010, read with the App Market category إيجاد المنتجات (Dropshipping) (ZD-I-0446), the same words.
- `inventory_management.*` (11) go on CM-INV-001, read with the App Market category إدارة المنتجات والمخزون (ZD-I-0444), which the cell's reading names but doesn't cite. `lightspeed`, `vend`, `rewaa` and `zoho_inventory` could also be ERP or POS connections (CM-PAY-028, CM-POS-001, App Market category الربط مع الأنظمة (ERP/POS)). I didn't place them there on the product's name: nothing held says what they are.
- `marketing.*` (16 here; the group continues into ZD-11):
  - the products whose part names nothing (`10x`, `abkhas`, `adatik`, `adwhats`, `almoutasoq`, `araboost`, `codemap`, `glam`, `greenbill`) go on CM-MKT-005, read with the App Market category التسويق والنمو (ZD-I-0455);
  - `blog` goes on CM-CNT-004;
  - `businesschat` goes on CM-SUP-004;
  - `cartat_whatsapp` goes on CM-MKT-007, with the App Market category التسويق عبر واتساب (ZD-I-0456);
  - `corner_ribbon`, `countdown_popup` and `exit_popup` go on CM-SFR-007;
  - `google_merchant_center` goes on CM-CHN-004.

## The new thing

**`new:Extended caching`**: one entry, ZD-E-247e8175 (`extended_caching`), enabled, available in Professional (`new_professional`), `core`.
- **Its place of its own:** a policy in the plan's own list, which is a plan line (B-extent, "What a place of its own is").
- **Its name:** `extended_caching` only, in English. No label or locale string is held in either language.
- **Proposed domain and parent:** domain G (operations), as the store's environment, beside CM-OPS-003 (hosting of the store) and CM-OPS-001 (reliability). What it caches (the storefront's pages, the API, assets) isn't stated.
- **Not CM-API-012,** API response caching, which is WooCommerce's REST API setting. Nothing says Zid's policy caches the API.
- **Searched:** cache; caching; cached; storefront caching; page cache; performance; speed; سرعة; CDN; hosting; أداء المتجر; التخزين المؤقت; الكاش. I also grepped the dashboard locales for "cach": none.
- **The checker's view:** CHANGES and NEW name it only as new. The coordinator may instead rule it out as the software's own bookkeeping (a cache). But it is a policy the plan lists for the store, which the brief's rule 2 places on a capability.

## The checker's CHANGES, and what I decided

- **CM-ANL-004 becomes held, with `core` (line 127, `live_analytics`).** I kept it. ZD-1 already placed Live analytics (`analytics/live`, 'Real-time analytics and visitor tracking') here, and the policy's words name the same thing. Those lines aren't amended yet, which is why the checker flags this.
- **CM-LOY-008 becomes held, with `core` (line 7, `customer_referrals`).** I kept it. The capability was made from ZD-1's Customer Referrals page, and ZD-5's permissions are on it.
- **CM-SEL-007 becomes held, with `core` (lines 77, 78 and 80, `fostering_charity.*`).** I kept them. ZD-5 placed Charity fostering (دعم الجمعيات الخيرية), whose strings invite customers to donate, and its permission here.
- **CM-SUP-006 becomes held, with `core` (line 59, `faq.faq_page`; and line 18, `customer_support.faq`, `shows`).** I kept them. ZD-1 placed FAQs, the store's own FAQ for its buyers, here.
- **CM-SFR-007 becomes held, with `shows` only (lines 145 to 147).** I kept them. `countdown_popup` and `exit_popup` name pop-ups, which are the capability's thing. `corner_ribbon` is read as a banner, which is weaker. All three are disabled, so the cell becomes held, not placed.
- **CM-CHN-004 becomes held, with `shows` only (line 149, `marketing.google_merchant_center`).** Google Merchant Center is a term of the capability (product feeds for channels). The line is `shows` from a disabled key alone. What would settle it: what the policy gates, such as an App Market app or a feed page.

## Entries I couldn't tell, and what would settle each

- **`customer_care.customer_care` (Enterprise), on CM-ONB-003.** I read it as Zid's support to the merchant, from its config: ticketing, chat, WhatsApp, call and `am`. That `am` is an account manager is an assumption. It could instead be the store's care for its own buyers (CM-SUP-005). What would settle it: the page or plan line this policy gates.
- **`customers.block_cod`, on CM-PAY-029 only.** The plan line Block Cash on Delivery (ZD-S-0631) blocks COD 'in your store'. The key sits under `customers`, so it may block COD for chosen customers, which would add CM-CUS-005. That isn't stated.
- **`customers.customer_note`, on CM-CUS-001.** I read it as a note on a customer. It could be the buyer's note at checkout, the Checkout page options' 'Customer notes' that ZD-9 named for CM-CHK-009, or an order's note (CM-ORD-013).
- **`customize_shipping_options.*` (disabled), on CM-SHP-001, with CM-PAY-029 for `cod_activation_deactivation`.** These aren't named for a product, yet they are disabled, with no plan, like the App Market groups around them. What they gate isn't stated. They aren't CM-SHP-013's app-written delivery rules, which is a Shopify Function API.
- **`inventory_locations.supporting_shipping_options_for_shipping_and_storage` (Professional).** It is on CM-INV-005 (`core`) and CM-SHP-011 (`shows`). "shipping and storage" is the App Market category الشحن والتخزين that CM-SHP-011 cites, and the cell says Zid doesn't store products. So I didn't give it `core` there. What would settle it: the setting this policy gates.
- **`importing_products.*`.** Each is CM-MIG-001's, with a line for each thing it updates: quantities on CM-INV-001, prices on CM-CAT-013, and products and weights on CM-CAT-001. A weight could also be shipping data, but no capability holds product weights apart from the products.
- **`gift_page_options.customize_gifting_status_messages`.** It is on CM-LOY-006 and CM-NTF-001, as ZD-9's order status messages. Who receives them isn't stated.
- **`marketing.businesschat`, on CM-SUP-004.** It is read by "chat". It could be a marketing channel instead.
- **`marketing.cartat_whatsapp`, on CM-MKT-007.** It is read as WhatsApp marketing. "cartat" could name abandoned carts (CM-MKT-022), but the key's word isn't "cart".
- **The `customer_support.*` WhatsApp keys, on CM-SUP-004.** I read them as buyers reaching the store by WhatsApp. They could also be CM-NTF-004's message delivery.

## A structure whose items and sources disagree

None found. Each entry's text matches its item at `items.jsonl` lines 102 to 231, in order. The rendering leaves out a disabled item's `config: null`, `available_in: []` and `policies: null`, which the readings state.

## What a source states that no entry holds (leads for the second stage)

- `dashboard-locales/items.jsonl`, namespace `charity-fostering`, lines 13475 to 13487 (en) and from 30338 (ar). These are the Charity fostering page's strings: its campaign form, its message content, and its opportunities' periods ('Permanent opportunity', 'Period expired'). They are leads for CM-SEL-007, which ZD-5 placed.
- **No page or locale string of the App Market apps** that the disabled policies name (customer_support, inventory_management, finding_products, marketing) is held, as far as this batch read. So which apps each policy gates isn't held. That is a gap for CM-SUP-004, CM-SUP-005, CM-INV-001, CM-CAT-010, CM-MKT-005, CM-SFR-007 and CM-CHN-004.

## The checker's other lines

- **NOTEs on first leads that hold nothing:**
  - CM-API-013 (by "all, one", in `contact_us_all_in_one`) is no lead: the words are part of a product's name.
  - CM-CUS-007 (by "customer, whatsapp"; and "marketing, whatsapp") is no lead: no key names consent.
  - CM-SHP-013 (by "shipping options") is a homonym, as above.
  - CM-MKT-004 (by "discount", in `financial_analytics.total_discount_value`) is no lead: the entry is a measure, not discount logic.

## Problems with the brief or the script

- None with the leads: 95 of the 130 entries had leads from the key's words, as the coordinator's fix intended. Some leads come from words of a product's name: `all`, `one`, `merchant` (`omniful_merchant`, `google_merchant_center`) and `customer` with `support`. They are no leads.
- The brief changed during the batch (a WooCommerce ruling on `disable_ui`, rule 4). It doesn't bear on Zid's policies.

## The coordinator's check (30 October 2026, after the batch)

- **`available_in` is the plan the source states a policy is available in, and the lines say no more.** The repository's README calls it 'the plan it is available in', and the structure's `meta.json` gives the store's own plan: Demo Store, `new_professional` (Professional, tier 3). Six policies enabled for this Professional store state Enterprise or Elite, so the field isn't always the lowest plan that includes the policy. Each line's `scope` is the source's own plan key, and its reading says 'available in <plan>', with no claim that this is a lowest plan. That stands for ZD-9 and ZD-11 to ZD-13 too. What the field means beside the store's own plan is a reading for the plans' cells at Zid's amendment, with ZD-6's offered plans. Enterprise and Elite aren't among those plans.
- **Extended caching** is a new thing on a plan line, which the model counts as a place of its own. It is decided with WooCommerce's speed and cache things (WC-1, WC-3, WC-6): one capability for the store's speed and caching, or out as the software's own working.
- **The batch changes no cell beyond Zid's earlier batches.** Its policies confirm the pages and plan lines placed before.
