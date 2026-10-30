# C-backfill-zid: notes

## What this part did

C-zid added one capability to domain C: CM-ORD-015, order payment status (an order's paid or unpaid state, tracked and changed apart from its order status), parent CM-ORD-001, landed from ZD-C-028 (C-zid's notes, Batch 1 and Batch 4). This part writes its three missing cells: Shopify's, Salla's and WooCommerce's. BigCommerce's cell is already written (`none-held`, by C-bigcommerce). No capability is added, no concern landed, no ruling written. Each row is a reading unless it quotes a statement.

Read: the brief; `model --domain C --areas ORD`; C-zid's Batch 1 and Batch 4 notes and its CM-ORD-015 rows (Zid's cell rests on ZD-C-028: the webhook topic order.payment_status.update, ZD-S-0722, and the plan lines Payment Status and Bulk Payment Status Update, ZD-S-0723 and ZD-S-0724); `candidates --domain C --platform <platform> --areas ORD` for the three platforms; the evidence of CM-ORD-001, CM-ORD-003, CM-PAY-016 and CM-PAY-020, to keep apart what they hold; `caps --terms` for payment status, financial status, mark as paid, partial payment and حالة الدفع (only CM-ORD-015, CM-PAY-005 and CM-PAY-016 matched); then `search` on each platform, with the terms in each cell's reading or `searched`.

## The cells (readings)

- **Shopify: `statements`, `core`.** Three statements, each cited for its words about the order's paid or unpaid state:
  - the webhook topic orders/paid, SH-C-084/boundary/SH-S-1299. It is the lead C-zid named. I cite the statement rather than the placed entry SH-I-0535 (the same topic, which CM-ORD-001 cites), because a statement covers it;
  - "Orders that accept manual payments are marked as unpaid on the **Orders** page" (SH-C-079/boundary/SH-S-0386);
  - the staff permission MARK_ORDERS_AS_PAID (SH-I-1087), the merchant's change of the state.

  **Also cited elsewhere:** SH-S-1299 is `core` in CM-PAY-020, SH-I-0535 is `core` in CM-ORD-001, and SH-S-0386 and SH-I-1087 are `core` in CM-PAY-016. CM-ORD-015 and CM-PAY-020 are both under CM-ORD-001, so they make one tree. CM-PAY-016 is under CM-PAY-001, so SH-S-0386 and SH-I-1087 are in two trees, and the checker flags them (below).

  **Apart from the order status:** the concern map holds no Shopify order statuses (CM-ORD-003's Shopify cell is `none-held`), so nothing held puts the paid state inside an order status. The cell rests on the state's own webhook topic, page mark and permission, as Zid's does.
- **Salla: `none-held`.** C-zid's lead, order.payment.updated (SA-S-1583, `core` in CM-ORD-001), isn't this capability by its words:
  - its Arabic name is "تحديث طريقة دفع الطلب", an update of the order's payment method;
  - Salla's app-functions list describes it as "Triggered when payment information is updated" (SA-C-196/boundary/SA-S-1271, domain F).

  Awaiting payment, بإنتظار الدفع (slug payment_pending, SA-S-2672), is one of Salla's order statuses. The staff permission to browse "الطلبات بحالة (بإنتظار الدفع)" (SA-S-2278) is already `core` in CM-ORD-003. So Salla's statements hold the payment wait inside the order status, which is CM-ORD-003's, not apart from it. The cell's reading lists every kind of hit.
- **WooCommerce: `none-held`.** Every hit puts the payment state in the order status:
  - the status Pending payment (WC-I-0317, CM-ORD-003);
  - the gateways setting the status, "Awaiting BACS payment" (WC-S-0604) and On hold or Processing through filters (WC-S-5004 to WC-S-5006);
  - the stock hold "for unpaid orders", whose unpaid order is "the pending order" (WC-S-5401).

  WC-S-5401 bears on the payment state in its words, but only as the pending status, so it isn't cited here. It is already in CM-INV-008 (domain B) and CM-ORD-004.

## A reading for the reviewer: the cells differ in how the platforms hold the state

Zid and Shopify name the paid or unpaid state with its own webhook topic (order.payment_status.update; orders/paid). Salla and WooCommerce, in what the concern map holds, name it only as order statuses: بإنتظار الدفع / payment_pending, and Pending payment.

If the reviewer reads CM-ORD-015 as the payment state wherever it is held, Salla's SA-S-2672 and SA-S-2278 and WooCommerce's WC-I-0317 and WC-S-5401 could be cited here as `shows`. I didn't cite them, because the capability is defined as apart from the order status, and those statements are CM-ORD-003's or already cited there.

## Kept apart

- **CM-ORD-003 (order statuses):** Salla's بإنتظار الدفع and WooCommerce's Pending payment, On hold and Processing (above).
- **CM-PAY-020 (payment transactions):**
  - Shopify's capture settings, order_transactions/create and the permissions to capture or pay by credit card;
  - Salla's Transactions;
  - WooCommerce's process_payment.

  Only orders/paid is cited in both, for its words about the order being paid.
- **CM-PAY-016 (manual payment methods):** Shopify's draft-order permissions to mark as paid (SH-I-1086, SH-I-0897) and Record payments (SH-I-0876) aren't cited here. The first two are about draft orders. Record payments is a payment recorded, not the order's state.
- **CM-ORD-005 (drafts):** draftOrderComplete's requirement of access to mark as paid (SH-S-6196).
- **Homonyms and false hits:**
  - Salla's مدفوعات: Salla Payments, its balance, payouts and fees (PAY's);
  - Salla's report_most_customer_paid (domain D's reports), and the partner payout status Paid (SA-I-1948);
  - WooCommerce's "Get paid with WooPayments", its payouts, and Automattic's Paid Services;
  - Shopify's payment terms (SH-C-045, SH-C-158), and its notification templates Pending payment success and Pending payment error (SH-I-2025, SH-I-2026, domain D), which are names only.

  None is cited.

## Gaps

- **Shopify:** no statement held gives Shopify's own term for the state, such as a financial or payment status field or a filter on the Orders page. I searched financial status, displayFinancialStatus, payment status, partially paid and others (the cell's reading). Only the topic, the page mark and the permission are held.
- **Salla:**
  - the released flag partial-payments (SA-C-040/decides/SA-S-3286, plans plus, pro, special) is a name with no definition. Whether it is an order's partially paid state, or a way of paying in parts, isn't stated, so it isn't cited;
  - no Merchant API field for an order's payment state is held.
- **WooCommerce:** the release fixed by checksum holds what the concern map doesn't. These were read as context and are not cited:
  - the REST orders schema's set_paid, "Define if the order is paid. It will set the status to processing and reduce stock items.", and date_paid, "The date the order was paid" (`woocommerce/includes/rest-api/Controllers/Version2/class-wc-rest-orders-v2-controller.php`, at `/home/user/woocommerce-release/11.2.1`);
  - wc_get_is_paid_statuses(), "Get list of statuses which are consider 'paid'" (`woocommerce/includes/wc-order-functions.php`).

  A reading: they suggest that WooCommerce derives the paid state from the order status, which would fit the `none-held` cell for a state kept apart from the status. A capture placing them in WC-C-070 would let the cell say so from a statement.

## Checker flags, and answers

The checker prints 0 problems and 4 flags:
- **cells.tsv line 3 (Salla, `none-held`, 104 matches) and line 4 (WooCommerce, `none-held`, 20 matches):**
  - most matches are the generic paid and مدفوعات, which name payments, payouts, fees and paid plans;
  - the rest are the order statuses and the event order.payment.updated.

  Each cell's reading names the kinds of hit and why they aren't this capability (above).
- **SH-C-079/boundary/SH-S-0386 and SH-I-1087,** cited by CM-ORD-015 and CM-PAY-016, in two trees. Each statement names two things, and they bear on both:
  - SH-S-0386: a manual payment method, and the unpaid mark it leaves on the order;
  - SH-I-1087: marking an order paid, which is how a manual payment is recorded, and a change of the order's payment state.

  The coordinator may make one of the two `shows`.
