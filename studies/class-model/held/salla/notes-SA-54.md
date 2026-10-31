# Held pass, Salla, batch SA-54: notes

80 entries (effort high), evidence at observed-sa@b0bd0b16, all of `settings-center` as rebuilt after SA-50 (one entry per node, every store's answer in it, with `if:`). Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-54`). Fourteen sub-pages, all opened by items SA-48 and SA-49 placed:
- 1 to 42, seven of the Orders section's: Shipping label cost deduction (`/orders/shipping-label-deduction`, 1 to 6), Auto restock based on order status (7 to 11), Manage refund statuses (`/orders/control-refund`, 12 to 17), Customer notes (18 to 23), Order cancellation (24 to 31), Reorder (32 to 35), Order editing (`/orders/edit-policy`, 36 to 42);
- 43, the Payments section's Payment Restrictions (`/payments/payment-restrictions`);
- 44 to 80, six of the Products section's: Show “You may also like” section on product page (`products.recommendations`, 44 to 48), Product display in store (`products.product_quantity`, 49 to 54), Automatic pricing (`products.auto_pricing`, 55 to 59), Product tax pricing (60 to 64), Show number of purchases (65 to 71), Back in stock alerts (`/products/notify_availability`, 72 to 80).
- Twelve bodies are the same bytes on all five stores (sha256 of `<label>/<section>.json` compared: shipping-label-deduction `74507abe…`, auto-restock `43001f5f…`, control-refund `70df0081…`, customer-notes `e97fcbd3…`, cancellation `50b7b006…`, reorder `91c20a46…`, edit-policy `4e20859c…`, payment-restrictions `3d5bbbe6…`, recommendations `95ca1e17…`, auto_pricing `96537711…`, product_tax_pricing `6aa8a761…`, purchase_count `b3b45b8f…`). Two differ on the real store only:
  - `products~products.product_quantity.json` (`ebb14cff…` on four stores, `c5725714…` on the real one): the real store's form has an id and an extra item, so its nodes are other entries (SA-56, below);
  - `products~notify_availability.json` (`77cea7b0…`, `c6ea3595…`): the real store's answer, updated on 11 October, differs only in its fields' loading states and a value binding; its nodes are the same.

**Placed:** 75 entries on capabilities, none `new`, 5 `out`, in 87 lines: 62 `core`, 19 `shows`, 1 `extension-point` (CM-NTF-004, entry 77), 5 `out`. No `own-service` or `outside`, no filler.
- Lines by capability: CM-SFR-015 12, CM-ORD-004 8, CM-MKT-016 8, CM-SHP-002 6, CM-ORD-013 6, CM-ORD-002 6, CM-INV-001 5, CM-RET-002 5, CM-MKT-023 5, CM-CAT-013 5, CM-PLN-006 4, CM-TAX-001 4, CM-ORD-014 3, and one each on CM-PAY-005, CM-PAY-019, CM-AIA-001, CM-ONB-003, CM-NTF-004.
- `shows`: every line of Manage refund statuses (behind `control-refund-status`, 12 to 16), Order editing (`customer-editing`, 36 to 41) and Automatic pricing (`metal-pricing`, 55 to 59), and the cancellation page's three gated settings (29, 30 behind `advanced-order-cancellation-statuses`; 31 behind `order-cancellation-reasons`). None of these five features is released on any held store.
- Scope on 31 lines: `product-availability-notify` (9), `customer-editing` (6), `control-refund-status` (5), `metal-pricing` (5), `advanced-order-cancellation-statuses` (2), `not advanced-order-cancellation-statuses`, `order-cancellation-reasons`, `ai-driven-personalized-product` and `product-price-tax-included` (one each).
- Three qualities: one edit per order (38), the remaining quantity shown under five items (54), up to five categories for the purchase count (70).
- **The checker prints no `CHANGES` line: no cell changes.**

**Sources read:** the brief and what it names; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's row for `settings-center`, `index/ledger-summary.tsv`; the selection row; B-extent's "Cells and evidence" and conventions, through the earlier batches' rules; the rulings' last section; SA-48's to SA-53's notes, their rules S1 to S12, R1 to R9, T1 to T8, U1 to U8, V1 to V8 and W1 to W8, and the coordinator's checks; the earlier lines `held_entries.py earlier` named (SA-16, SA-21, SA-33, SA-48, SA-49, SA-50, SA-51, SA-52, SA-53).
- **The bodies.** I walked the fourteen bodies once, with a script that prints each node and the `if`s above it, and opened a body's code only where the walk left a column open. These are the entries the bodies settled:
  - the lists, to see whether an entry stands for the settings list alone or for it and a Save list whose label is an unresolved array (3, 9, 14, 20, 26, 34, 38, 42, 46, 51, 57, 62, 64, 67, 74, 80);
  - 43, the component that draws Payment Restrictions;
  - 48, the `if` on the first option's label, which the entry renders without its condition;
  - 56, where the alert sits;
  - 64, the help link's address;
  - 49 to 54 and 72 to 80, the real store's differing bytes.
- **To clarify only, each cited where a line rests on it:**
  - `dashboard-features/*@en/items.jsonl` for the nine features (demo lines: `control-refund-status` 328, `customer-editing` 329, `order-cancellation-reasons` 331, `advanced-order-cancellation-statuses` 333, `ai-driven-personalized-product` 418, `product-availability-notify` 507, `hide-out-of-stock-products` 523, `product-price-tax-included` 526, `metal-pricing` 556), with the other three stores' lines;
  - the Pro store's settings pages, `20261009T033607Z-sweep-settings-demo-en/steps/042` to `056` (cited: 045, 047, 049 to 056), and the Basic store's, `20261008T141131Z-sweep-merchant-en/steps/343`, `345`, `346`, `348`. They show which settings each store's page displays: entries 12, 24, 27, 36, 43, 44, 48, 49, 54, 55, 62, 63, 64, 65, 72;
  - `dashboard-translations/{en,ar}/settings.json` for the Arabic quotes, and the keys no body uses (below).

## The rules: S1 to S12 and R1 to W8, kept, and what I added where they don't reach

I kept the earlier rules as the coordinator's checks and rulings left them:
- S1 for each sub-page: the item that opens it (SA-48's, SA-49's) and the concern map's key, SA-S-1741 to SA-S-1754.
- S7, R5 and U2 for the forms and lists, with U2's two capabilities where a page is itself two things. Shipping label cost deduction is the case, CM-SHP-002 and CM-PLN-006, as SA-48 placed its item (1 to 3).
- V7 for the Save lists whose label is an unresolved array. These merge with the settings list: 3, 9, 14, 20, 46, 51, 57, 67. Edit-policy's and Back in stock alerts' Save buttons have a string label, so their lists stand alone and are `out` (42, 80).
- T1 for the sections with `features` (control-refund, edit-policy, auto_pricing, notify_availability), and S4 and W7 for a node's `features` or `flag:` (29 to 31, 63).
- V1 for the node under `not advanced-order-cancellation-statuses` (28): the feature is released nowhere, so the node shows on every store, `core`.
- S11 for the gated pages whose plan gates SA-33 placed `core` (36, 55).
- U3 for the page a component draws (43).
- V4 and S7 for the channel select whose SMS option names an App Store provider (77).
- V8 for alerts that state a rule of the page's own thing (38, 56, 62).
- T4 for Mushammir (48).
- S5 and W4 for an option that names another capability's thing (6, 48).

For the coordinator to align with SA-55 and SA-56, I added:
- **X1. A help link in a settings list** (64: 'Need help with tax settings? Visit our Help Center', to https://help.salla.sa). The list holds it beside the Save button. The link names a place, the platform's help centre, so it isn't a UI string by the brief's test ('names no place'). It goes on CM-ONB-003 `core`, as S8 places an `s:link` on the page it opens. The Save button is in `reading`, and the tax settings the link names in passing take no line. If the coordinator reads such a link as 'Learn more', the line is `out`. CM-ONB-003 is `core` either way.
- **X2. An option whose label is given under a store feature** (48: the first option of 'Products to show' reads 'Similar products recommended by Mushammir' where `useFeature ai-driven-personalized-product` holds, and 'Random products' otherwise). The option's thing takes its own line, on CM-AIA-001 by T4, with the feature as that line's scope (T2, W4, the ruling after SH-69). The select's own line, CM-MKT-023, keeps no scope.
- **X3. A setting that takes a cost from another capability's balance** (6: 'From store balance and online payments'). It takes that balance's line beside the wallet's, as S5 has the label cost deduction on CM-PLN-006. The e-payments balance is CM-PAY-005's, which its note keeps apart from the store balance.
- **X4. A storefront page whose settings are all display options keeps the page's capability for each** (49 to 54 on CM-SFR-015; 65 to 70 likewise). S6's first refinement, 'a display option of a capability's own thing goes on that capability alone', is read for a capability's own feature (images, offers, brands, recommendations). It isn't read for a value the storefront shows. The remaining quantity (54) is the stock CM-INV-001 tracks, shown and not set, so it takes no CM-INV-001 line (S7). The sold-out products (52) are CM-SFR-015's own plan line, 'عرض المنتجات التي نفدت في نهاية الصفحة'. If the coordinator reads S6 the other way, 54 takes a CM-INV-001 `core` line, and CM-INV-001 is `core` already.

## `new` things

None. Each entry's thing is already a capability's: the sub-pages by the concern map's settings keys and the items SA-48 and SA-49 placed on them; the settings by the capability of what they set (S5, S7). Searched with `caps --terms`, besides the leads:
- help center, مركز المساعدة, help article;
- quantity, الكمية, كمية, quantity selector, manual quantity, remaining quantity, الكمية المتبقية, purchase quantity, purchase count, عدد مرات الشراء, sold out, نفدت;
- cancellation reason, أسباب الإلغاء, gold, الذهب, metal, معادن;
- VAT-inclusive, شاملة الضريبة, tax-inclusive, prices include tax;
- label cost, wallet deduction, e-payments, المدفوعات الإلكترونية;
- restock, إعادة المخزون, reorder, buy again, اعادة الطلب;
- customer note, order note, ملاحظات, edit window, out of stock;
- variant alert, message template, قالب الرسالة, Mushammir, مشمر.

CM-RET-004 (order withdrawal requests, WooCommerce's) matched 'order note'. It is a buyer's request the merchant reviews, not the buyer's own cancellation that 27 sets, so the cancellation page stays on CM-ORD-004.

## The `CHANGES` lines

None.

## Entries I couldn't tell, and what would settle each

- **54, Show remaining product quantity:** CM-SFR-015 alone (X4), or also CM-INV-001. The coordinator's reading of S6 against S7 settles it. No cell changes either way.
- **64, the help link:** CM-ONB-003 `core` (X1), or `out` as a UI string. No cell changes either way.
- **48, Mushammir's option:** CM-AIA-001 `core` by T4, as SA-50 placed the checkout's 'Powered by Mushammir'. CM-AIA-001's name is 'the platform's AI features in the merchant's admin', and this option chooses what buyers see on the product page. If the coordinator keeps CM-AIA-001 to the admin's AI tools, the option is CM-MKT-023's input alone. CM-AIA-001 is `core` already.
- **6, 'From store balance and online payments':** CM-PAY-005 (the e-payments balance, X3), not CM-PAY-002 (the payment service). The Arabic, 'المحفظة (رصيد المتجر والمدفوعات الإلكترونية)', names the wallet holding both balances. A help article on the label deduction would settle which balance is drawn first.
- **5, 'no contracts or minimums':** kept in `reading`, not as a quality. The cell's reading holds the same terms ('without contracting with the carrier', SA-S-5059) in its reading. A minimum the platform states would be a quality.
- **38, the one edit per order:** taken as a quality ('Customers can edit the order only once.'). The alert's other rule, 'only to orders in the “Pending review” status', is a condition, kept in `reading`.
- **36 to 41 and 55 to 59, `shows`:** both pages' plan gates are SA-33's `core` lines (SA-E-ac07181a, SA-E-7e66f749). The Pro store's pages read 'Access restricted' and 'You don’t have the required permissions to access this page.' in place of their settings (steps 049 and 053). The Basic store's page for auto pricing reads the upgrade line (step 345). Each line stands on its own entry (S11), as the coordinator settled for SA-48's items.

## A structure whose items and sources disagree

- **Entry 77's id and control name render as a translation:** 'id: Sales channels (قنوات البيع) [channels]'. The body's id and name are `channels`, which the build resolves as the key `channels` of the settings translations. This is cosmetic, like SA-49's 35 and SA-50's 46 and 50. It makes `held_entries.py` lead to CM-CHN-001 ('by channels, sales channels, قنوات البيع'), which is no lead.
- **Entry 48's option given under an `if`** is rendered 'option: {_: if; else: …; $: …}' without its condition, `useFeature ai-driven-personalized-product`. The body governs (`products~products.recommendations.json`). This is the same gap V1 and U4 found for `getFeatureState` and `getFeatureVisibility`.
- **The real store's Product display in store:** its answer gives the form the id `products.product_quantity` and adds an item 'hide_out_of_stock_products' (`features: {flagKey: hide-out-of-stock-products, released: true}`, while the store's features list has it unreleased: `real-merchant@en/items.jsonl` line 524). Its form, lists and items are therefore SA-56's entries 50 to 55 (SA-E-f681f5be, SA-E-9de20349, SA-E-fb2936c7, SA-E-87c46536, SA-E-9ac6524a, SA-E-3ce8a012), the twins of my 50 to 54. My lines for them are CM-SFR-015 `core`, with the threshold quality on display_product_quantity. **I don't know whether SA-56 has run, so the coordinator should align the two.**
  - The item's own `features` says `released: true` and the store's list says `released: false`. The list is the store's answer, so it governs (S4), and the item is SA-56's.
- **Entry 32, the Reorder section, carries no `parent`.** Its body names none (`"path": "/orders/reorder"`, no `parent`), unlike the other sub-pages. The entry is right.

## For the second stage: what the sources state that no entry holds

Keys of `structures/salla/dashboard-translations/{en,ar}/settings.json` that no settings body uses:
- **`orders/cancellation#reasons.*`** (30 keys): the strings of the component CancellationReasonsSection, which draws 31 behind `order-cancellation-reasons`. They name 'Customer-specific reasons' and 'Store-specific reasons' (the latter 'not shown to customers'), system reasons that 'can only be enabled or disabled', custom reasons, and the limit 'You can enable up to 10 reasons.'. This is a lead for CM-ORD-004, and the limit a quality, behind an unreleased feature.
- **`payments/payment-restrictions#*`** (55 keys, besides `payments/payment-restrictions/rule-form`): the strings of the component `payment-rules:list` (43). They give:
  - the actions 'Hide payment method', 'Under review' and 'Reject operation';
  - the condition types 'Amount paid', 'Customer country / IP Address', 'Customer country / phone code', 'Credit card country', 'Customer group', 'Guest checkout', 'Partial payment method', 'Specific categories', 'Products quantity' and 'Markets';
  - 'The selected action applies to the chosen payment methods when all conditions are met'.

  This is what CM-PAY-019 does, a lead for its reading.
- **`orders/control-refund#order-statuses.*`**: 'Order statuses eligible for refunds', an older label of 16's select.
- **`products/products.purchase_count#condition/products.*`**: 'Products', 'The selected products above are those for which the purchase count will be visible to customers…'. This is a per-product version of 69 and 70 that the body doesn't offer.
- **`orders/shipping-label-deduction#method.description`**: 'Choose how the shipping label cost is deducted from your store wallet.'
- **`products#products.product_price_included_tax.label`**: 'Enter VAT-inclusive product prices', a second key for 63's label.

Run pages:
- `20261009T033607Z-sweep-settings-demo-en/steps/050.text.txt`, lines 145 to 147: Payment Restrictions' component shows 'Payment Restrictions', '(0)' and 'Create rule' on the Pro store.
- `…/steps/056.text.txt`, line 165: 'Message preview', the back-in-stock message's preview, a component string.

The Back in stock alerts channel 'Store notification' / 'إشعارات المتجر' (77, option key `channels.option.mobile`) is a channel to buyers that no capability holds, as SA-52 found for the browser push option. As an option it is the setting's input (S7). A place of its own would make it a capability.

## Leads set aside as no leads

- **By a permission's name:** CM-ORD-001, CM-PAY-020 (`order_management`); CM-ACC-006 (`store_setting_browse`); CM-MKT-016 (`stock_settings_management` on 49).
- **By a control's or field's name, through `held_entries.py earlier`:** `method`, `description`, `hours`, `window`, `days`, `duration`, `types`, `content_title`, `Sales`.
- **By a common word:**
  - CM-SHP-022, CM-SHP-003, CM-ACC-004, CM-PAY-004, CM-ORD-007, CM-ORD-015, CM-OPS-004, CM-CNT-008, CM-CNT-003;
  - CM-CUS-001, CM-STF-002, CM-CUS-005, CM-INV-010, CM-CHK-009, CM-TAX-008, CM-AIA-003, CM-TAX-003, CM-PLN-007, CM-TAX-005;
  - CM-B2B-003, CM-B2B-001, CM-CHK-010, CM-API-013, CM-ANL-002, CM-INV-002, CM-INV-004, CM-ACC-005, CM-TRU-005, CM-RET-001, CM-RET-003;
  - CM-SHP-017, CM-SHP-007, CM-ORD-010, CM-PAY-029, CM-LOY-008, CM-PAY-032, CM-NTF-003, CM-CUS-007.
- **Named only as an input:** CM-B2B-004 ('Quote orders', an option of 11), CM-CAT-003, CM-CAT-005 and CM-CAT-002 (the categories, brands and variants settings are set by), CM-ORD-003 (the statuses).
- **Kept apart by its note:** CM-LOY-007 (reorder reminders, apart by CM-ORD-014's note).
- **No lead:** CM-CHN-001 (the build fault on 77).
- **Labels of other pages:** `Order statuses` (CM-ORD-003, SA-17 and SA-19) and `Message subject` (CM-SUP-002, SA-52:39).

## The checker's lines, read again

- **No `CHANGES` line.**
- **NOTE line 9, brand:** 'Salla Shipping Labels' / 'بوليصات سلة' (5). It is `core` by what the entry shows, Salla's own label service on its own settings page, the cell's term. A brand in a product's name is no maker statement.
- **The 'holds other entries: a container' notes:** each is a section, a form or a list I placed as a container on the page's capability. Two are not containers: line 22 (16, the statuses select) and line 77 (70, the categories select). Each holds only its `s:base-url`, which is `out` (17, 71). Their lines are settings.

## Problems with the brief or the script

- `show` renders an option label given under an `if` without its condition (48, above). This is one more case of the `if:` gap the coordinator noted after SA-52.
- `held_entries.py earlier` still takes some control names as keys (`method`, `description`, `hours`, `window`, `days`, `duration`, `types`, `content_title`) and the mistranslated `Sales` (77). They printed unrelated capabilities and cost little.
- No other problem. The entries carried their sections' `features`, `flag:` and `if:`, so the gates needed no body, apart from 48's option.
