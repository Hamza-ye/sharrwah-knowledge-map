# Cards: Q4 on woocommerce

12 records cited by `studies/proposals/drafts/Q4/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - All five let a seller take orders that the buyer pays outside the platform. They match on role (basis 4), each in its own words, all in stated pages: with a Shopify manual payment method the seller "can arrange to receive their payment in a way that works best for them"; with Salla's bank transfer "يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك"; Zid shows the merchant's bank account at payment "لتمكين العملاء من الدفع عن طريق التحويل البنكي"; with WooCommerce's direct bank transfer "the payment process is manual and happens outside your WooCommerce powered store"; BigCommerce's offline payment methods "do not require a credit card or a traditional payment gateway". Q4-SH-K1737, Q4-SA-P0099, Q4-ZD-K0124, Q4-WC-002, Q4-BC-P0114
- **section 1, line 8:** - WooCommerce and BigCommerce share the term offline payment method (basis 1), and Salla and Zid the terms التحويل البنكي and الدفع عند الاستلام (basis 1), all in stated pages. Q4-WC-002, Q4-BC-P0114, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 9:** - Cash on delivery collected by the seller's own carrier keeps the money out of Salla: with a carrier outside Salla's shipping labels "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة", and the amounts are settled "مباشرة بين التاجر وشركة الشحن". WooCommerce's cash on delivery "lets you take payments at the time of delivery", BigCommerce's lets customers "pay you with cash", and Shopify lists it among the common types of manual payments (role, basis 4, all stated). Q4-SA-P0091, Q4-SA-P0092, Q4-WC-004, Q4-BC-P0117, Q4-SH-003
- **section 1, line 15:** - No one term covers all five. Shopify says manual payment methods, with cash on delivery, money orders and bank transfers as common types; WooCommerce says offline payment method; BigCommerce's offline payment methods are Bank deposit, Cash on delivery, Check, Money order and Pay in store; Salla and Zid name each method, as التحويل البنكي and الدفع عند الاستلام. Q4-SH-003, Q4-WC-002, Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 20:** - **Recording the payment.** Four platforms have the seller record by hand a payment received outside them (role, basis 4): Shopify's Mark as paid, "if you have accepted payment outside of Shopify"; Zid's Bulk Payment Status Update in its plan comparison (shipped); WooCommerce's offline methods "require you to manually verify the payment was processed" before the seller changes the status; BigCommerce's merchant moves the order on "After receiving the payment". Q4-SH-012, Q4-ZD-K0208, Q4-WC-018, Q4-BC-P0115
- **section 1, line 22:** - Shopify and BigCommerce keep that payment as a transaction on the order (role, basis 4, both stated): `orderMarkAsPaid` records "a payment transaction for the outstanding amount"; BigCommerce's Transactions API creates records "for payments that were processed externally". WooCommerce's order carries `date_paid` and `transaction_id` (shipped). Q4-SH-039, Q4-BC-K0100, Q4-WC-043
- **section 1, line 25:** - WooCommerce, BigCommerce and Salla carry payment in the one order status (role, basis 4). WooCommerce sets cash-on-delivery orders to Processing "until payment is collected", though Processing means "Payment has been received (paid)"; BigCommerce places offline-paid orders in Awaiting Payment (both stated). Salla's dashboard text (recorded session, 12 October 2026) shows قيد المراجعة on the confirmation page "عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام", and its help offers to set cash-on-delivery orders to تم التنفيذ at once, "لتجنب إشكالية سوء فهم العميل لحالة" that status. Q4-WC-015, Q4-WC-019, Q4-BC-P0115, Q4-SA-018, Q4-SA-045
- **section 1, line 26:** - **Time to pay** (role, basis 4, all stated). Salla's merchant can turn off the bank-transfer مهلة الدفع, so that the customer must transfer and attach the receipt on completing the order; WooCommerce's Hold Stock "automatically cancels eligible Pending payment orders created through checkout after the configured time limit"; Shopify lets the seller add payment terms, after which an unpaid order becomes Overdue. Q4-SA-047, Q4-WC-039, Q4-SH-014
- **section 1, line 28:** - **Refunds.** WooCommerce and BigCommerce record a refund that the seller makes outside them (role, basis 4, both stated): a WooCommerce order can reach Refunded "without the customer’s funds having been returned"; recording an offline refund in BigCommerce is "an optional manual process". When a refund can't go through Salla, the merchant transfers the amount to the customer's bank account or adds it to the customer's wallet in the store. Q4-WC-026, Q4-BC-018, Q4-SA-009
- **section 1, line 31:** - **Reports.** Zid's analytics give "نسب استخدام طرق الدفع في متجرك", and Salla's dashboard text (recorded session, 12 October 2026) the distribution of payments by payment method: a match on role (basis 4) across stated and observed sources. With WooCommerce's default Date Paid, "orders without a paid date are excluded". Q4-ZD-022, Q4-SA-049, Q4-WC-032
- **section 1, line 40:** - **By carrier, courier or shipping method** (role, basis 4, all stated). On Salla "يمكن تفعيل أو تعطيل الدفع عند الاستلام بشكل مستقل لكل مندوب أو تسعيرة"; Zid's cash on delivery is turned on per carrier; WooCommerce's merchant chooses "which shipping methods and rates will offer COD". Q4-SA-P0199, Q4-ZD-K0111, Q4-WC-033
- **section 1, line 50:** - **WooCommerce.** A cash-on-delivery order can be paid by card at delivery through WooPayments' In-Person Payments, which marks the order Complete at payment, and WooPayments "pays out money from incoming orders into your linked bank account or debit card". Q4-WC-036, Q4-WC-046
- **section 2, line 55:** - **Seller-collected payment method**: Sharrwah would offer ways of paying in which the buyer pays the seller, or someone the seller engages such as its own courier, outside Sharrwah, with no money passing through Sharrwah or a payment service it provides. Sharrwah would show the method, keep the order, and record what the seller says it received or refunded. Q4-SH-K1737, Q4-WC-002, Q4-BC-P0114
- **section 2, line 60:** - Alternative not taken: cash on delivery only as a seller-named method, as Shopify's Help Center has sellers in Italy set it up. Cash on delivery is tied to couriers, carriers and shipping methods on Salla, Zid and WooCommerce, which a seller-named method can't carry (rule 2). Q4-SH-045, Q4-SA-P0199, Q4-WC-033
- **section 2, line 67:** - Why: rule 3, as the data model is expensive to change after launch. A cash-on-delivery order is delivered before it is paid; one status for both puts WooCommerce's in Processing, which means paid, and led Salla to offer a setting so customers don't misread تم التنفيذ. Q4-WC-015, Q4-WC-019, Q4-SA-045
- **section 2, line 69:** - **Payment record**: an entry on the order for each payment the seller says it received outside Sharrwah: amount, currency, method, the date received, who entered it, and an optional reference and proof. Each entry states that no money passed through Sharrwah. Marking an order paid writes one entry for the amount outstanding. Q4-SH-039, Q4-BC-K0100, Q4-WC-043
- **section 2, line 74:** - Alternative not taken: a status change alone, as on WooCommerce and BigCommerce, or Zid's Bulk Payment Status Update, since reports need the amount and date received: WooCommerce's analytics count by Date Paid, and Shopify asks for the amount received "For reporting purposes". Q4-WC-032, Q4-SH-026, Q4-ZD-K0208
- **section 2, line 75:** - **Payment window**: per method, an optional time for the buyer to pay after ordering; when it ends, the order shows overdue or is cancelled with its stock released, as the seller chooses. Rule 3 puts only the due date in the data model now and leaves the rest to the build. Q4-SA-047, Q4-WC-039, Q4-SH-014
- **section 2, line 78:** - Why: rule 3 (money flows): no Sharrwah balance exists for such an order to refund from, and a WooCommerce order can reach Refunded "without the customer’s funds having been returned", which this wording avoids. Q4-WC-026
- **section 2, line 80:** - It draws on Salla's and Zid's seller-set restrictions, and on cash on delivery set per courier, carrier or shipping method on Salla, Zid and WooCommerce. Q4-SA-055, Q4-SA-P0199, Q4-ZD-K0111, Q4-WC-033
- **section 2, line 87:** - **Payment reports**: reports would count seller-collected orders by method and by the amount and date recorded. Rule 3 leaves them to the build; they need only the **Payment record**. Q4-SA-049, Q4-ZD-022, Q4-WC-032
- **section 2, line 91:** - It draws on Salla's label carriers, whose cash reaches the store's account on a set cycle, Zid's service collecting "نيابة عن التاجر" into محفظة التاجر after a separate fee, and WooPayments' card payment at delivery. Q4-SA-P0093, Q4-ZD-K0122, Q4-ZD-K0119, Q4-WC-036
- **section 3, line 106:** - **Set per courier, carrier or shipping method:** whether cash on delivery is offered. Q4-ZD-K0111, Q4-WC-033
- **section 3, line 111:** - **Set by the seller:** methods, instructions, accounts, conditions, and payment and refund entries. Q4-ZD-007, Q4-WC-018

## The cards

### Q4-WC-002

**Cited at:** section 1, line 7; section 1, line 8; section 1, line 15; section 2, line 55

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-002
- bears_on: 1;2
- identifier: Direct Bank Transfer (BACS): offline payment method
- statement: This is an offline payment method, meaning that the payment process is manual and happens outside your WooCommerce powered store.
- scope: Direct Bank Transfer (BACS)
- cite_ids: Q4-WC-C002
- from: held

**Citation Q4-WC-C002:** `https://woocommerce.com/document/bacs/` | Direct Bank Transfer (BACS) | 2025-08-19 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/079-woocommerce.com/text.txt` (5990 bytes), fetched 2026-10-12T10:50:50Z, captured
- quote: This is an offline payment method, meaning that the payment process is manual and happens outside your WooCommerce powered store.
- title: Direct Bank Transfer (BACS) Documentation - WooCommerce
- in context: …erce ProductsExpand Taxes ShippingExpand Payments Orders Data and reporting Customers Marketing Site administrationExpand Store designExpand Mobile AppExpand Get helpExpand Documentation / WooCommerce / Payments / Direct Bank Transfer (BACS) Direct Bank Transfer (BACS) Direct Bank Transfer, which might also be referred to as Bank Account Clearing System (BACS), is a payment method that lets your customers pay you directly via their bank account. ⟪This is an offline payment method, meaning that the payment process is manual and happens outside your WooCommerce powered store.⟫ It's important to be clear that when a customer chooses to pay with Direct Bank Transfer, it is up to them to initiate this payment via their bank. The order is set to "On hold" in WooCommerce, as you the store owner must check your bank account for this incoming deposit before processing their order. It's essential to verify that you've been paid, and the transaction has cleared and is in your account before shipping an order and marking it as …

### Q4-WC-004

**Cited at:** section 1, line 9

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-004
- bears_on: 1
- identifier: Cash on Delivery
- statement: Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer’s ordered products.
- cite_ids: Q4-WC-C004
- from: held

**Citation Q4-WC-C004:** `https://woocommerce.com/document/cash-on-delivery/` | Cash on Delivery | 2025-05-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/080-woocommerce.com/text.txt` (4790 bytes), fetched 2026-10-12T10:50:51Z, captured
- quote: Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer’s ordered products.
- title: Cash on Delivery Documentation - WooCommerce
- in context: … Develop on Woo Hire an expert Get support $ USD Find extensions, themes, guides, and more Go to search results page Search Log inGet started WooCommerce WooCommerce Getting started Migrating to WooCommerce ProductsExpand Taxes ShippingExpand Payments Orders Data and reporting Customers Marketing Site administrationExpand Store designExpand Mobile AppExpand Get helpExpand Documentation / WooCommerce / Payments / Cash on Delivery Cash on Delivery ⟪Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer's ordered products.⟫ WooCommerce sets orders using Cash on Delivery (COD) to "Processing" until payment is collected. You, as the store owner, should confirm that payments for Cash on Delivery orders have been collected before setting orders to "Complete" in WooCommerce. If you are using the WooCommerce mobile app and a card reader to collect In-Person Payments, it marks orders "Complete" automatically at the time of payment. For more information see Managing Orders…

### Q4-WC-018

**Cited at:** section 1, line 20; section 3, line 111

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-018
- bears_on: 3
- identifier: Order statuses: On hold
- statement: Offline payment methods require you to manually verify the payment was processed. Once you confirm payment has been received, you can change the status of the order.
- cite_ids: Q4-WC-C018
- from: held

**Citation Q4-WC-C018:** `https://woocommerce.com/document/managing-orders/order-statuses/` | Order statuses in WooCommerce: On hold | 2026-08-21 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/027-woocommerce.com/text.txt` (9657 bytes), fetched 2026-10-10T23:54:01Z, captured
- quote: Offline payment methods require you to manually verify the payment was processed. Once you confirm payment has been received, you can change the status of the order.
- title: Order Statuses Documentation - WooCommerce
- in context: … or warehouse's cue to ship the order and manually change the status to Completed. Completed The order has been fulfilled and is complete. Requires no further action. On hold The order is awaiting payment confirmation. Stock is reduced, but you need to confirm payment. The On hold status is generally assigned to an order when a customer pays via an "offline" payment method that does not have immediate payment confirmation, like the BACS gateway. ⟪Offline payment methods require you to manually verify the payment was processed. Once you confirm payment has been received, you can change the status of the order.⟫ The On hold status may be temporarily assigned to orders if the customer paid using a delayed notification payment method, like SEPA Direct Debit. Depending on the payment gateway in use on your site, the order may move automatically from On hold to a different status once the payment clears. Check the order notes on the order and the documentation of your payment gateway for details. You may also see the On hold status if you use a payment gate…

### Q4-WC-043

**Cited at:** section 1, line 22; section 2, line 69

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-043
- bears_on: 3;5
- identifier: wc/v4 orders: payment_method, payment_method_title, transaction_id, date_paid
- statement: 'payment_method'       => $order->get_payment_method(), 'payment_method_title' => $order->get_payment_method_title(), 'transaction_id'       => $order->get_transaction_id(), 'date_paid'            => wc_rest_prepare_date_response( $order->get_date_paid(), false ),
- cite_ids: Q4-WC-C043
- from: held

**Citation Q4-WC-C043:** `woocommerce-11.2.1:src/Internal/RestApi/Routes/V4/Orders/Schema/OrderSchema.php` | lines 661-664 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'payment_method'       => $order->get_payment_method(), 'payment_method_title' => $order->get_payment_method_title(), 'transaction_id'       => $order->get_transaction_id(), 'date_paid'            => wc_rest_prepare_date_response( $order->get_date_paid(), false ),
- in context: …me' => $order->get_shipping_first_name(), 'last_name' => $order->get_shipping_last_name(), 'company' => $order->get_shipping_company(), 'address_1' => $order->get_shipping_address_1(), 'address_2' => $order->get_shipping_address_2(), 'city' => $order->get_shipping_city(), 'state' => $order->get_shipping_state(), 'postcode' => $order->get_shipping_postcode(), 'country' => $order->get_shipping_country(), 'phone' => $order->get_shipping_phone(), ), ⟪'payment_method' => $order->get_payment_method(), 'payment_method_title' => $order->get_payment_method_title(), 'transaction_id' => $order->get_transaction_id(), 'date_paid' => wc_rest_prepare_date_response( $order->get_date_paid(), false ),⟫ 'date_paid_gmt' => wc_rest_prepare_date_response( $order->get_date_paid() ), 'date_completed' => wc_rest_prepare_date_response( $order->get_date_completed(), false ), 'date_completed_gmt' => wc_rest_prepare_date_response( $order->get_date_completed() ), 'cart_hash' => $order->get_cart_hash(), 'payment_url' => $order->get_checkout_payment_url(), 'is_editable' => $order->is_editable(), 'needs_payment' => $order->needs_payment(), 'needs_processing'…

### Q4-WC-015

**Cited at:** section 1, line 25; section 2, line 67

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-015
- bears_on: 3
- identifier: Processing (Cash on Delivery)
- statement: WooCommerce sets orders using Cash on Delivery (COD) to “Processing” until payment is collected.
- scope: Cash on Delivery (COD)
- cite_ids: Q4-WC-C015
- from: held

**Citation Q4-WC-C015:** `https://woocommerce.com/document/cash-on-delivery/` | Cash on Delivery | 2025-05-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/080-woocommerce.com/text.txt` (4790 bytes), fetched 2026-10-12T10:50:51Z, captured
- quote: WooCommerce sets orders using Cash on Delivery (COD) to “Processing” until payment is collected.
- title: Cash on Delivery Documentation - WooCommerce
- in context: … started WooCommerce WooCommerce Getting started Migrating to WooCommerce ProductsExpand Taxes ShippingExpand Payments Orders Data and reporting Customers Marketing Site administrationExpand Store designExpand Mobile AppExpand Get helpExpand Documentation / WooCommerce / Payments / Cash on Delivery Cash on Delivery Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer's ordered products. ⟪WooCommerce sets orders using Cash on Delivery (COD) to "Processing" until payment is collected.⟫ You, as the store owner, should confirm that payments for Cash on Delivery orders have been collected before setting orders to "Complete" in WooCommerce. If you are using the WooCommerce mobile app and a card reader to collect In-Person Payments, it marks orders "Complete" automatically at the time of payment. For more information see Managing Orders. This document takes you through the steps to activate and configure Cash on Delivery (COD) on y…

### Q4-WC-019

**Cited at:** section 1, line 25; section 2, line 67

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-019
- bears_on: 3
- identifier: Order statuses: Processing
- statement: Payment has been received (paid), and the stock has been reduced. The order is awaiting fulfillment.
- cite_ids: Q4-WC-C019
- from: held

**Citation Q4-WC-C019:** `https://woocommerce.com/document/managing-orders/order-statuses/` | Order statuses in WooCommerce: Processing | 2026-08-21 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/027-woocommerce.com/text.txt` (9657 bytes), fetched 2026-10-10T23:54:01Z, captured
- quote: Payment has been received (paid), and the stock has been reduced. The order is awaiting fulfillment.
- title: Order Statuses Documentation - WooCommerce
- in context: … used by the block-based checkout before an order is submitted. Orders in the Draft status are only visible on the "Draft" sub-tab of the Orders overview page. See the Draft order status section below. Pending payment The order has been received, but no payment has been made. Pending payment orders are generally awaiting customer action. If your customer needs a payment link to make payment, see the documentation on paying for orders. Processing ⟪Payment has been received (paid), and the stock has been reduced. The order is awaiting fulfillment.⟫ All orders require processing except those in which all products are both virtual and downloadable. This is the store owner's or warehouse's cue to ship the order and manually change the status to Completed. Completed The order has been fulfilled and is complete. Requires no further action. On hold The order is awaiting payment confirmation. Stock is reduced, but you need to confirm payment. The On hold status is generally assigned to an order w…

### Q4-WC-039

**Cited at:** section 1, line 26; section 2, line 75

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-039
- bears_on: 3
- identifier: Hold Stock
- statement: When the Hold Stock setting is enabled, WooCommerce automatically cancels eligible Pending payment orders created through checkout after the configured time limit and releases their held stock back to available inventory.
- cite_ids: Q4-WC-C039
- from: held

**Citation Q4-WC-C039:** `https://woocommerce.com/document/managing-orders/order-statuses/` | Order statuses in WooCommerce: Cancelled | 2026-08-21 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/027-woocommerce.com/text.txt` (9657 bytes), fetched 2026-10-10T23:54:01Z, captured
- quote: When the Hold Stock setting is enabled, WooCommerce automatically cancels eligible Pending payment orders created through checkout after the configured time limit and releases their held stock back to available inventory.
- title: Order Statuses Documentation - WooCommerce
- in context: …immediately. With delayed notification payment methods, an order can remain On hold while the payment is confirmed, then move to Failed if the payment is rejected. See how to understand and fix failed orders in WooCommerce for more details. Cancelled The order was canceled by an admin or the customer. When an order has the Cancelled status, stock for line items on the order is returned to the store's inventory if inventory management is enabled. ⟪When the Hold Stock setting is enabled, WooCommerce automatically cancels eligible Pending payment orders created through checkout after the configured time limit and releases their held stock back to available inventory.⟫ An order with the Cancelled status may need to be refunded. Check the order notes and your payment gateway's documentation for details. Refunded An admin or shop manager has fully refunded the order's value after payment. If you use the Manual Refund option, the order can reach this status without the customer's funds having been returned. See the documentation on refunding orders in WooCommerce for more details. Visual diagram of order status f…

### Q4-WC-026

**Cited at:** section 1, line 28; section 2, line 78

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-026
- bears_on: 3
- identifier: Order statuses: Refunded
- statement: If you use the Manual Refund option, the order can reach this status without the customer’s funds having been returned.
- cite_ids: Q4-WC-C026
- from: held

**Citation Q4-WC-C026:** `https://woocommerce.com/document/managing-orders/order-statuses/` | Order statuses in WooCommerce: Refunded | 2026-08-21 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/027-woocommerce.com/text.txt` (9657 bytes), fetched 2026-10-10T23:54:01Z, captured
- quote: If you use the Manual Refund option, the order can reach this status without the customer’s funds having been returned.
- title: Order Statuses Documentation - WooCommerce
- in context: …bled. When the Hold Stock setting is enabled, WooCommerce automatically cancels eligible Pending payment orders created through checkout after the configured time limit and releases their held stock back to available inventory. An order with the Cancelled status may need to be refunded. Check the order notes and your payment gateway's documentation for details. Refunded An admin or shop manager has fully refunded the order's value after payment. ⟪If you use the Manual Refund option, the order can reach this status without the customer's funds having been returned.⟫ See the documentation on refunding orders in WooCommerce for more details. Visual diagram of order status flow This flow chart shows the typical path from a temporary Draft checkout record through payment and fulfillment, plus other statuses you may see when payment is delayed, fails, is cancelled, or is refunded. Draft is a temporary block-based checkout state before submission. A submitted order typically moves from Pending payment to Processi…

### Q4-WC-032

**Cited at:** section 1, line 31; section 2, line 74; section 2, line 87

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-032
- bears_on: 3
- identifier: Date Paid
- statement: With Date Paid selected, orders without a paid date are excluded from both reports.
- scope: Taxes report and Orders or Revenue reports
- cite_ids: Q4-WC-C032
- from: held

**Citation Q4-WC-C032:** `https://woocommerce.com/document/woocommerce-analytics/` | Troubleshooting (Taxes report) | 2026-10-09 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/044-woocommerce.com/text.txt` (25891 bytes), fetched 2026-10-10T23:54:02Z, captured
- quote: With Date Paid selected, orders without a paid date are excluded from both reports.
- title: Analytics and Sales Reports Documentation - WooCommerce
- in context: …s differ from the actual figures on your website you can clear the cache by going to WooCommerce > Status > Tools and running the Clear Analytics Cache tool. If the figures still look off after clearing the cache, try re-importing historical data. When comparing the Taxes report with Orders or Revenue, use the same report period and the configured Date Type in Analytics > Settings. The Taxes report follows that setting; the default is Date Paid. ⟪With Date Paid selected, orders without a paid date are excluded from both reports.⟫ Changing Date Type invalidates the report cache automatically. A difference caused by the reports using different date bases does not require re-importing historical data. Questions and support Do you still have questions and need assistance? This documentation is about the free, core WooCommerce plugin, for which support is provided in our community forums on WordPress.org. By searching this forum, you'll often find that your question has been …

### Q4-WC-033

**Cited at:** section 1, line 40; section 2, line 60; section 2, line 80; section 3, line 106

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-033
- bears_on: 4
- identifier: Cash on Delivery: Enable for shipping methods
- statement: Enable for shipping methods – Choose which shipping methods and rates will offer COD
- scope: Cash on Delivery (COD)
- cite_ids: Q4-WC-C033
- from: held

**Citation Q4-WC-C033:** `https://woocommerce.com/document/cash-on-delivery/` | Setup and Configuration | 2025-05-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/080-woocommerce.com/text.txt` (4790 bytes), fetched 2026-10-12T10:50:51Z, captured
- quote: Enable for shipping methods – Choose which shipping methods and rates will offer COD
- title: Cash on Delivery Documentation - WooCommerce
- in context: …ess the Cash on Delivery configuration settings. Clicking the "Enable" button will activate COD. Once enabled, clicking the "Manage" button will take you to the configuration page where you configure COD settings. Configure your settings: Enable COD - Enable to use. Disable to turn off. Title - Choose the title shown to customers during checkout Description -Add info shown to customers if they choose COD Instructions - Explain how to pay via COD ⟪Enable for shipping methods - Choose which shipping methods and rates will offer COD⟫ Accept for virtual orders - Tick box to allow COD for virtual products Save changes This is the settings page for Cash on Delivery. Fill in the instructions for COD payments here and set which shipping methods it applies to. If you are interested in additional features, check out the Advanced Cash on Delivery with Fee extension. Questions and support Do you still have questions and need assistance? This documentation is about the free, core WooC…

### Q4-WC-036

**Cited at:** section 1, line 50; section 2, line 91

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-036
- bears_on: 3;5
- identifier: Cash on Delivery: In-Person Payments
- statement: If you are using the WooCommerce mobile app and a card reader to collect In-Person Payments, it marks orders “Complete” automatically at the time of payment.
- scope: Cash on Delivery (COD)
- cite_ids: Q4-WC-C036
- from: held

**Citation Q4-WC-C036:** `https://woocommerce.com/document/cash-on-delivery/` | Cash on Delivery | 2025-05-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/080-woocommerce.com/text.txt` (4790 bytes), fetched 2026-10-12T10:50:51Z, captured
- quote: If you are using the WooCommerce mobile app and a card reader to collect In-Person Payments, it marks orders “Complete” automatically at the time of payment.
- title: Cash on Delivery Documentation - WooCommerce
- in context: …tion / WooCommerce / Payments / Cash on Delivery Cash on Delivery Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer's ordered products. WooCommerce sets orders using Cash on Delivery (COD) to "Processing" until payment is collected. You, as the store owner, should confirm that payments for Cash on Delivery orders have been collected before setting orders to "Complete" in WooCommerce. ⟪If you are using the WooCommerce mobile app and a card reader to collect In-Person Payments, it marks orders "Complete" automatically at the time of payment.⟫ For more information see Managing Orders. This document takes you through the steps to activate and configure Cash on Delivery (COD) on your store. Setup and Configuration Follow the steps below to setup Cash on Delivery (COD) on your store: Navigate to: WooCommerce > Settings > Payments > Take offline payments. Click the Enable button for Cash on Delivery. After enabling, click the Manage button to access the Cash on Delivery configuration sett…

### Q4-WC-046

**Cited at:** section 1, line 50

**Record** (`studies/proposals/records/Q4/woocommerce/statements.tsv`):
- stmt_id: Q4-WC-046
- bears_on: 5
- identifier: WooPayments settings: Payouts
- statement: The Payouts section controls how often WooPayments pays out money from incoming orders into your linked bank account or debit card.
- scope: WooPayments
- cite_ids: Q4-WC-C046
- from: held

**Citation Q4-WC-C046:** `https://woocommerce.com/document/woopayments/settings-guide/` | Payouts | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T084016Z-q1r-woocommerce-more/items/019-woocommerce.com/text.txt` (14309 bytes), fetched 2026-10-11T08:40:26Z, captured
- quote: The Payouts section controls how often WooPayments pays out money from incoming orders into your linked bank account or debit card.
- title: WooPayments: Settings Guide Documentation - WooCommerce
- in context: … a support phone number has been set, it cannot be left blank. We strongly suggest filling these settings out, since they can help prevent disputes from customers who might otherwise have trouble contacting you for assistance. NOTE: The customer support email and phone number settings covered here are not the same as updating the email or phone number that you have on file in your Stripe Express account. To do that, please see this page. Payouts ⟪The Payouts section controls how often WooPayments pays out money from incoming orders into your linked bank account or debit card.⟫ Payout schedule This setting allows you to specify a payout schedule that works best for your business. You can find more information on the options in our dedicated payout schedule document. If it's been less than 7 days since your first transaction with WooPayments, you will not be able to change your payout schedule until the initial 7 day waiting period has passed. Payout bank account Your bank account or debit card details are securely stor…
