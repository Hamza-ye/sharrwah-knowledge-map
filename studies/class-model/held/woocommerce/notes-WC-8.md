# Notes: held pass, WooCommerce, batch WC-8 (`release-settings`, the rest; `release-webhook-topics`; `woopayments-onboarding`)

**What the batch holds:** 60 entries, in 94 lines.
- **`release-settings`, 40 entries,** read from the release 11.2.1, unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`, cited as `woocommerce-11.2.1:<path>, lines …`:
  - `includes/admin/settings/class-wc-settings-products.php`: 32 entries, lines 125 to 499. These are the sections Measurements and Reviews of the tab's General section, then the Inventory and Downloadable products sections (`get_own_sections`, lines 58 to 64).
  - `class-wc-settings-shipping.php` (section Shipping settings): 7 entries, lines 111 to 172.
  - `class-wc-settings-site-visibility.php` (tab Site visibility): 1 entry, lines 39 to 44.
- **`release-webhook-topics`, 16 entries:** the default topic-hooks map in `includes/class-wc-webhook.php`, lines 987 to 1066.
- **`woopayments-onboarding`, 4 entries:** the four steps of the structure's first item. That item is the answer the Payments settings received in run `20261029T020454Z-store-setup-en`, steps 87 to 98 (`other-product-class@0d79b794f:woocommerce/structures/woopayments-onboarding/items.jsonl`, line 1).

**Kept to WC-7, and to WC-3 and WC-4.**
- I read WC-7's placements and notes to the end, with the coordinator's check, before placing anything.
- Every setting here has an option of the same key in WC-3's or WC-4's placements. Each takes that line's capability and supports, and its reading says so ("as WC-3 places its option").
- Each section's title entry is a container (rule 3, M-13), placed as WC-7 places its sections. Its children are named in its reading.
- **The 5 section ends are `out`,** as the coordinator ruled for WC-7's: `product_measurement_options`, `product_rating_options`, `product_inventory_options`, `digital_download_options` and `shipping_options`.
- **The Site visibility tab's slot goes on CM-ACC-009, `core`,** as WC-7 places Blueprint's slot. The slot is the tab's only element (`type: slotfill_placeholder`). The tab is listed with no condition (`includes/admin/class-wc-admin-settings.php`, line 60).
- **Scope:** empty for the settings and the topics. These are the release's definitions, not one store's values. A setting's default is in `reading`.
- **Quality:** empty throughout. Hold stock's 'x minutes' and Count partial downloads' '(by default, 30 minutes)' are a placeholder and a default, not stated limits, as WC-7 reads defaults.

**Count:**
- **By entry:** 55 `capability`, 5 `out`. One of the 55, WC-E-7c3b22d4 (`test_account`), also carries a `new` line.
- **By line:** 79 `core`, 6 `own-service`, 4 `shows` (one of them the `new` line), and the 5 `out` lines.

## How the entries were decided

**The settings.** Each takes WC-3's capability for its option. Lines that WC-3 doesn't have are added where the entry's words name a second thing (rule 2):

| Entries | Capability | Added here (rule 2) |
| --- | --- | --- |
| Measurements, Weight unit, Dimensions unit | CM-CAT-001 core | none |
| Reviews and its 5 settings | CM-SUP-001 core | none |
| Inventory, Manage stock, Out of stock notifications, Out of stock threshold, Out of stock visibility, Stock display format | CM-INV-001 core | Out of stock visibility and Stock display format: CM-SFR-015 core (below) |
| Hold stock (minutes) | CM-INV-008 core | CM-ORD-004 shows: 'the pending order will be cancelled'. The cell cites the same statement (WC-S-5401) as shows only, so I kept to it |
| Low stock notifications, Notification recipient(s), Low stock threshold | CM-INV-004 core | Low stock threshold: CM-NTF-002 core, 'you will be notified via email' |
| Low stock, out of stock and backorder notifications, Notification recipient(s) | CM-NTF-002 core | Out of stock threshold: CM-NTF-002 core, 'you will be notified via email' |
| Backorder notifications | CM-NTF-002 core | CM-INV-001 core, a reading (below) |
| Downloadable products and its 7 settings | CM-SEL-002 core | Downloads require login: CM-CUS-010 shows. Grant access after payment: CM-ORD-003 shows, since its tip names the statuses processing and completed |
| Shipping settings and its 5 settings | CM-SHP-001 core | Calculations: CM-CHK-002 core, 'on the cart page' |
| Site visibility's slot | CM-ACC-009 core | none |

**The webhook topics.** Each topic takes two lines, both `core`:
- one on its resource's capability, where the cell already cites the same topic (WC-S-0254 to WC-S-0269):
  - coupons: CM-MKT-002;
  - customers: CM-CUS-001;
  - orders: CM-ORD-001, with order.deleted and order.restored on CM-ORD-012;
  - products: CM-CAT-001;
- one on CM-API-008, whose cell cites some topics and says 'the others are alike'.

This follows the convention on the platform's own API for its own feature. Two topics also name a second thing in their `fired by` hooks:
- **order.updated** is fired by `woocommerce_order_refunded`, so a refund reaches the webhook: CM-RET-002 `core`, a reading.
- **product.created and product.updated** are fired by `woocommerce_new_product_variation` and `woocommerce_update_product_variation`: CM-CAT-002 `core`, a reading. Variations are WooCommerce's word for variants (that cell's reading).

product.published isn't placed on CM-CHN-001, as that cell's reading says. The entry's source is the code map. The admin's labels for the same topics ('Coupon created' and the rest, `includes/admin/settings/views/html-webhooks-edit.php`, lines 71 to 86) are cited in the readings, where the model's own statements come from. I gave the topics no line on CM-API-009 (webhooks set up in the admin), since the entry is the code's map, not the admin's list. The coordinator may add one.

**WooPayments' onboarding.** Each step is `own-service` on CM-PAY-003, the payment service's onboarding and verification:
- **Scope `US`.** The answer's request body is `{}`, so the location is the store's business location. That location is 'Business location:United States (US)' on the page where the answer was first received (`20261029T020454Z-store-setup-en/steps/087.text.txt`, line 118). The run's own note says the same of step 87 (`index/run-notes.tsv`), and it says that no choice of location saved until step 102 (Oman). The answer states `supported: true`.
- **Maker:** WooPayments is 'the only payment gateway designed by Woo for Woo' (WC-S-0557, M-1). WC-5 places it `own-service` for US. The steps are defined in WooCommerce's own release (`src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsService.php`, lines 32 to 37), so WooCommerce's own Payments settings host the flow. The service and its checks are WooPayments', so I kept `own-service` and gave no `core` line. That is a reading, for the coordinator.
- **The second things the steps name:**
  - **`payment_methods`:** CM-PAY-002 `own-service`. This is the step where the methods WooPayments takes are chosen.
  - **`wpcom_connection`:** CM-ACC-010 `own-service`. That cell already cites the WordPress.com connection as WooPayments' requirement.
  - **`test_account`:** `new:test account` (below).
  - **`business_verification`:** none beyond CM-PAY-003.
- **`required_steps: [wpcom_connection]`** names another step, not the entry's own thing, the way a route's `nextRoutes` does. So the two steps that carry it take no CM-ACC-010 line for it.
- **`status: not_started`** is this store's state, so it goes in `reading`.

## New things

- **`new:test account`** (WC-E-7c3b22d4, `test_account`, `/woopayments/onboarding/test_account`), supports `shows`.
  - **What it is:** WooPayments' test account, a step of its own in its onboarding, after the WordPress.com connection.
  - **Its place of its own:** none established. The step's path is an answer's field, not an entry of a route manifest. The Payments settings page opens the onboarding at `path=/woopayments/onboarding` (the `wpcom_connection` step's `auth` redirect, `items.jsonl`, line 2), so the step may be a sub-route of that settings page. No route list is held to show it.
  - **Proposed:** domain C, area PAY, parent CM-PAY-002 (the platform's own payment service), or CM-PAY-003 if the coordinator reads a test account as part of onboarding.
  - **Names:** English only ('test_account'). The platform holds no Arabic here.
  - **Searched:** test account; test mode; sandbox; test payments; development store; test; testing; demo mode. These found only development and partner stores (CM-DVT-003, CM-DVT-004, CM-DVT-006) and capabilities that hold the word "test" in other senses. No CM-PAY-002 or CM-PAY-003 cell, on any platform, holds "test" or "sandbox".
  - **The checker's leads:** CM-ACC-001, CM-ONB-004, CM-PAY-002 and CM-TRU-001. Each was read: none is a test account.
  - **Related:** WC-4's notes list WooPayments' `test_mode` and `dev_mode` as fields with no capability. The same thing may take them.

## The CHANGES line, and what I decided

- **CM-SFR-015 gains `core`** (lines 30 and 32: WC-E-f1fd2a4b, Out of stock visibility; WC-E-6564bcc3, Stock display format). I read both again against the source and kept them, as readings:
  - **'Hide out of stock items from the catalog'** (products.php, lines 350 to 356) decides how the storefront shows products that are out of stock. Salla's cell for the same capability rests on the same role: sold-out products put at the end of the page (SA-S-1978, the capability's note).
  - **'This controls how stock quantities are displayed on the frontend.'** (lines 358 to 372) is how the storefront shows products, in its own words.
  - The cell held only `extension-point`, from the Marketplace category Product display.
  - Both entries keep their WC-3 line on CM-INV-001. The merge will flag them as `core` in two domains (B and E).
  - If the coordinator keeps CM-SFR-015 to settings sections of their own (BigCommerce's Display), these two lines drop and the cell stays as it was.

## The checker's NOTEs, each read

- **`own-service` on CM-PAY-003, CM-PAY-002 and CM-ACC-010:** WooPayments' maker evidence, WC-S-0557 (M-1), as above. The WordPress.com connection is Automattic's, as CM-ACC-010's own cell holds.
- **First leads whose cell holds nothing, and that no line names.** Each was read:
  - **CM-AIA-003 (line 23, Notification recipient(s)):** matched by the words product and text only.
  - **CM-CNT-001 (line 41, Open in browser):** the files are the downloadable products' files, not a store's file library.
  - **CM-TRU-001 (line 42, Filename):** the security is the download files', not the admin's sign-in.
  - **CM-ACC-004 (line 95, `business_verification`):** the step names the verification of the business, not the entity the store operates as. Its `fields` are empty in the context the rule drops. The legal entity types WooPayments offers by country are in the structure `woopayments-onboarding-fields`, which the selection leaves out as market data. A lead for the second stage: if the coordinator reads WooPayments' asking for the entity type as a statement of CM-ACC-004 (Salla's cell rests on its verification's steps, as that capability's note says), that structure holds it.
- **The new thing whose entry has leads (line 93):** read, above.

## Entries I couldn't tell, and what would settle each

- **Backorder notifications on CM-INV-001** (WC-E-99401a1c), a reading:
  - the entry names backorders, which no statement held defines;
  - no capability of the model names them (searched: backorder; pre-order; preorder);
  - the setting is listed with the stock management settings (class `manage_stock_field`, products.php, line 303).

  A held statement of what a backorder is, such as the product editor's 'Allow backorders?', would settle whether it is stock management or a thing of its own. It isn't pre-orders (CM-SEL-005), but that is a reading too.
- **CM-SFR-015 for the two display settings:** above.
- **The onboarding's `core` side:** WooCommerce's own release defines the steps and serves their REST routes (`wc-admin/settings/payments/woopayments/onboarding`). A ruling on whether WooCommerce's own admin hosting a group company's onboarding is also `core` on CM-PAY-003 would settle it. I placed `own-service` only.
- **The webhook topics on CM-API-009:** see above.

## Where the items and the source differ: the source governs

- **The rebuilt entries agree with the source** for every setting here: their title, description, tip and type are their own arrays'. None carries a neighbour's field.
- **The items leave out what the source builds with `sprintf`:**
  - the File download method's tip and description (products.php, lines 399 to 415);
  - the redirect fallback's tip (line 431);
  - the Filename tip (line 477);
  - the Count partial downloads tip (line 490).

  I read each from the source, and took no terms from them.
- **The items leave out the options' labels,** such as the shipping destination's three choices and the download methods. The readings give them from the source.
- **`woopayments-onboarding`'s rule drops `context` and `actions`.** The steps' context holds the recommended methods, the connection's state and the verification's fields. I read item 1 to clarify only, and no line takes its terms from it.
- **The structure's entries are only item 1's steps.** Items 2 to 6, the country-change run, aren't entries. Among them is item 2, `supported: false`, with 'WooPayments is not supported in the selected business location.', which WC-4 and WC-5 used. So the onboarding's steps are placed for US only. The steps differ by item:
  - item 2, the unsupported location, has `wpcom_connection`, `test_account` and `business_verification`, without `payment_methods` (items.jsonl, line 2);
  - item 5, a supported one, has no `test_account` (line 5);
  - items 1, 3, 4 and 6 have all four.

  These are leads for the market subjects, and for where the test account is offered.

## For the second stage: what the sources state that no entry holds

- **WooPayments' recommended payment methods for US,** in `payment_methods`' context (items.jsonl, line 1): 'Credit/debit card' (required), Apple Pay, Google Pay, WooPay, Affirm, 'Cash App Afterpay', Klarna, Bancontact and more. Each has a description, such as 'Allow your shoppers to pay over time with Affirm.'. These are leads for the wallet, instalment and card capabilities, by location (items 3 to 6 hold other locations' lists, such as Clearpay and EPS).
- **The products tab's own sections:** 'General', 'Inventory' and 'Downloadable products' (products.php, lines 58 to 64).
- **The shipping tab's sections:** 'Shipping zones', 'Shipping settings', 'Classes', and 'Shipping providers' under the feature `fulfillments` (shipping.php, lines 56 to 66).
- **The webhook edit screen's fields:**
  - the status options, whose tip reads 'The options are &quot;Active&quot; (delivers payload), &quot;Paused&quot; (does not deliver), or &quot;Disabled&quot; (does not deliver due delivery failures).';
  - the topic 'Action', with its 'Action event';
  - 'Delivery URL' (`html-webhooks-edit.php`, lines 36 to 120; the status tip at line 39).

  These are for CM-API-009.
- **The hook names `wp_trash_post` and `woocommerce_trash_order`** for order.deleted (`class-wc-webhook.php`, lines 1027 to 1030). They name the trash that CM-ORD-012's reading says no statement holds.
- **The Count partial downloads tip** names 'download limits' (products.php, line 490). It is a lead for a download limit on CM-SEL-002, whose source is the product editor, not held here.

## Problems with the brief or the script

- **A run step as a scope's source.** The onboarding's location is stated only on the run's step page and in the run's note, not in the answer. I took it as the structure's source (`meta.json` names the run). The brief could say whether a run step a structure's `meta.json` names gives a `scope`.
- **`show --meta`** prints only `woopayments-onboarding`'s keys. The two `release:` structures have no `meta.json`, as WC-6 and WC-7 found.
- **Double quotes in a field:** some source strings hold double quotes, such as the verified owner label and the access-after-payment tip. They are described, not quoted, as WC-7 did.
- **B-extent and this brief** read the same on everything here, as far as I found.

## The coordinator's check (30 October 2026, after the batch)

- **The batch stands as placed.** Each setting keeps its WC-3 or WC-4 option's line, the section ends are `out` as in WC-7, and each webhook topic is `core` on its resource's capability and on CM-API-008.
- **Out of stock visibility and Stock display format also take CM-SFR-015,** the storefront's display settings, in their own words ('Hide out of stock items from the catalog'; 'This controls how stock quantities are displayed on the frontend.'), as ZD-11 places Zid's out-of-stock display. Their CM-INV-001 lines stand, and the merge counts each statement in both domains.
- **WooPayments' onboarding steps stay `own-service` only,** on CM-PAY-003: the onboarding is the service's own, which WooCommerce's release hosts. A run step named in the structure's `meta.json` is one of the entry's sources, so it may give the scope (US).
- **WooCommerce's batches are all placed** (WC-1 to WC-8, 801 entries). Its new things are decided with every platform's, after Salla's and Shopify's batches, since several may be things other platforms hold too: speed and backups (WC-1), with Zid's Extended caching; a payment service's test account; direct debit; and the software's own flags. Then WooCommerce is amended into the model.
