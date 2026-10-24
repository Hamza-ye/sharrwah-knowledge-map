# Q4 on WooCommerce: sorted against the Shopify and Salla accounts

## [1]

- **differs** (term, role): Direct Bank Transfer (BACS) lets customers "pay you directly via their bank account". It is "an offline payment method, meaning that the payment process is manual and happens outside your WooCommerce powered store". "Take payments in person via BACS"; off by default. Sorted against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [1]: Q4-SA-P0099, Q4-SA-P0068; Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737. Q4-WC-001, Q4-WC-002, Q4-WC-K0025, Q4-WC-K0028, Q4-WC-K0032
- **differs** (term, role): Cash on delivery, built in, lets "you take payments at the time of delivery of your customer’s ordered products": "by cash or other methods of payment". Off by default. Sorted against Salla [1]: Q4-SA-P0098, Q4-SA-K1530; Shopify [2]: Q4-SH-003, Q4-SH-004; Shopify [1]: Q4-SH-045. Q4-WC-004, Q4-WC-K0027, Q4-WC-K0029, Q4-WC-K0034
- **differs** (role): Check payments lets customers "place orders and pay offline by check"; off by default. Sorted against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737. Q4-WC-003, Q4-WC-K0026, Q4-WC-K0030, Q4-WC-K0033
- **differs** (role): "Offline" is a type of payment gateway: "No online payment is made." Sorted against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737. Q4-WC-K0031
- **differs** (role): Set at WooCommerce > Settings > Payments > Take offline payments: sections `offline`, `bacs`, `cheque`, `cod`; REST route `wc/v4` `offline-payment-methods`. Sorted against Shopify [1]: Q4-SH-K1735, Q4-SH-K1738, Q4-SH-K2859, Q4-SH-K2860, Q4-SH-K1193; Salla [1]: Q4-SA-003, Q4-SA-004, Q4-SA-006, Q4-SA-001. Q4-WC-005, Q4-WC-K0002, Q4-WC-K0021, Q4-WC-K0022, Q4-WC-K0023, Q4-WC-K0024, Q4-WC-K0035
- **differs** (role): The seller adds bank accounts (name, number, bank, routing number, IBAN, SWIFT/BIC), shown on the Order Received page and in order emails after checkout. Sorted against Salla [1]: Q4-SA-003, Q4-SA-004, Q4-SA-006, Q4-SA-001; Salla [1]: Q4-SA-P0100, Q4-SA-K1603, Q4-SA-021. Q4-WC-006, Q4-WC-007
- **differs** (role): Gateways are plugins; for third-party services "we’re not involved". Sorted against Salla [1]: Q4-SA-K1639, Q4-SA-K1656, Q4-SA-K1636. Q4-WC-K0006, Q4-WC-K0007, Q4-WC-K0008, Q4-WC-K0010
- **differs** (role): Point of Sale mode is "a digital cash register" taking card or cash, the seller entering the cash received; sales sync with the site. Sorted against Salla [1]: Q4-SA-031, Q4-SA-038, Q4-SA-033, Q4-SA-039, Q4-SA-K1402. Q4-WC-008, Q4-WC-009, Q4-WC-K1313, Q4-WC-K1318, Q4-WC-K1319, Q4-WC-K1323
- **not in what was read**: who the sale to the customer is between. Sorted against Shopify [1]: Q4-SH-K1491, Q4-SH-K1492. Q4-WC-N01
- **not in what was read**: how an order made with "Add new order" records an offline payment or its proof. Sorted against Salla [1]: Q4-SA-007, Q4-SA-K0504. Q4-WC-N02
- **not in what was read**: a statement that WooCommerce takes no part in cash on delivery, or may require direct payments. Sorted against Salla [1]: Q4-SA-P0080, Q4-SA-P0081. Q4-WC-N05
- **not in what was read**: recording Point of Sale payments taken through intermediaries. Sorted against Salla [1]: Q4-SA-034, Q4-SA-035. Q4-WC-N07

## [2]

- **differs** (term, identifier): "Direct bank transfer" (BACS), "Check payments" ("Cheque" before 3.3) and "Cash on delivery" (COD), each an "offline payment method"; keys `bacs`, `cheque`, `cod`. Sorted against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [2]: Q4-SA-K1604 ("The names in the dashboard"), Q4-SA-K1579, Q4-SA-050, Q4-SA-054. Q4-WC-001, Q4-WC-002, Q4-WC-011, Q4-WC-K0022, Q4-WC-K0023, Q4-WC-K0024, Q4-WC-K0025, Q4-WC-K0026, Q4-WC-K0027
- **differs** (role): A Title "shown to customers during checkout". Sorted against Shopify [2]: Q4-SH-007. Q4-WC-012
- **not in what was read**: a plan or pricing list naming these methods. Sorted against Salla [2]: Q4-SA-K1604 ("The plan feature lists"), Q4-SA-K1605, Q4-SA-K1580. Q4-WC-N08

## [3]

### Instructions and order status

- **differs** (term): "Instructions" for each method; for checks they "appear on the order thank-you page and in the order confirmation email". The order received page shows "Payment method:". Sorted against Shopify [3]: Q4-SH-006, Q4-SH-009. Q4-WC-021, Q4-WC-022, Q4-WC-023, Q4-WC-042
- **differs** (role): Bank transfer and check orders go On hold; COD orders go to Processing "until payment is collected" (On hold with a downloadable item); filters can change each. Sorted against Shopify [3]: Q4-SH-K1736, Q4-SH-008, Q4-SH-016; Salla [3]: Q4-SA-018; Salla [3]: Q4-SA-011, Q4-SA-K0598, Q4-SA-K0599; Salla [3]: Q4-SA-019, Q4-SA-045, Q4-SA-046. Q4-WC-013, Q4-WC-015, Q4-WC-017, Q4-WC-020, Q4-WC-K0036, Q4-WC-K0037, Q4-WC-K0038, Q4-WC-K0039
- **differs** (role): With Hold Stock enabled, WooCommerce "automatically cancels eligible Pending payment orders created through checkout after the configured time limit". Sorted against Salla [3]: Q4-SA-017, Q4-SA-047. Q4-WC-039
- **differs** (role): The orders list shows each order's payment method title ("via %s"). Sorted against Salla [3]: Q4-SA-002. Q4-WC-041
- **not in what was read**: an email to the customer while an offline-paid order awaits payment. Sorted against Shopify [3]: Q4-SH-020. Q4-WC-N09
- **not in what was read**: a message to the customer when an order paid on delivery is received. Sorted against Salla [3]: Q4-SA-063. Q4-WC-N15

### Recording the payment

- **differs** (role): "Offline payment methods require you to manually verify the payment was processed"; the seller then sets Processing or Completed. Sorted against Shopify [3]: Q4-SH-005, Q4-SH-012, Q4-SH-013; Salla [3]: Q4-SA-015, Q4-SA-016, Q4-SA-K0563. Q4-WC-014, Q4-WC-016, Q4-WC-018, Q4-WC-019
- **differs** (role): REST `set_paid` sets the order to processing and reduces stock. Sorted against Shopify [2]: Q4-SH-035, Q4-SH-039; Shopify [3]: Q4-SH-039, Q4-SH-040, Q4-SH-041. Q4-WC-024, Q4-WC-K0984
- **differs** (role): The `wc/v4` order schema carries `payment_method`, `payment_method_title`, `transaction_id` and `date_paid`. Sorted against Salla [3]: Q4-SA-059, Q4-SA-060, Q4-SA-061, Q4-SA-K0577; Salla [5]: Q4-SA-060. Q4-WC-043
- **not in what was read**: recording part of an order's payment, or a partly paid status. Sorted against Shopify [3]: Q4-SH-021, Q4-SH-022, Q4-SH-023, Q4-SH-024. Q4-WC-N10
- **not in what was read**: how the amount received is recorded when the currency differs. Sorted against Shopify [3]: Q4-SH-026. Q4-WC-N11
- **not in what was read**: payment due dates or terms on an order. Sorted against Shopify [3]: Q4-SH-014, Q4-SH-015, Q4-SH-019, Q4-SH-K0917, Q4-SH-K1448. Q4-WC-N12
- **differs** (role): In Point of Sale mode: "Mark payment as complete" after cash. Sorted against Shopify [3]: Q4-SH-005, Q4-SH-012, Q4-SH-013; Salla [3]: Q4-SA-032. Q4-WC-010
- **goes beyond**: WooPayments can't "interface with the BACS processing system". Q4-WC-027, Q4-WC-028

### Refunds

- **differs** (role): "Refund %s manually" needs the refund issued separately; an order can be Refunded "without the customer’s funds having been returned". Sorted against Salla [3]: Q4-SA-008, Q4-SA-009; Salla [3]: Q4-SA-010, Q4-SA-053. Q4-WC-025, Q4-WC-026, Q4-WC-K0995
- **differs** (role): Terms 8.j (Ecommerce Services) make the seller responsible for refunds and refund policies. Sorted against Shopify [3]: Q4-SH-K1492. Q4-WC-K0990, Q4-WC-K0991
- **differs** (role): Shop Managers can "View, edit, and delete orders, as well as process refunds". Sorted against Shopify [3]: Q4-SH-030, Q4-SH-031. Q4-WC-040
- **not in what was read**: what cancelling a shipped, unpaid order does to collecting payment. Sorted against Shopify [3]: Q4-SH-032. Q4-WC-N13
- **not in what was read**: reports of cash taken in Point of Sale mode. Sorted against Salla [3]: Q4-SA-042, Q4-SA-043, Q4-SA-044. Q4-WC-N16

### Fees

- **not in what was read**: any fee, or none, on offline-method orders. Sorted against Shopify [3]: Q4-SH-K1740, Q4-SH-K1335, Q4-SH-025; Salla [3]: Q4-SA-013; Salla [3]: Q4-SA-P0059, Q4-SA-K1593, Q4-SA-K1588; Salla [3]: Q4-SA-K0051. Q4-WC-N03

### Reports

- **differs** (role): Analytics excludes statuses the seller picks (default: Pending payment, Cancelled, Failed); with the default Date Type "Date Paid", "orders without a paid date are excluded". Sorted against Salla [3]: Q4-SA-K0582, Q4-SA-K2501. Q4-WC-029, Q4-WC-030, Q4-WC-031, Q4-WC-032, Q4-WC-K0599
- **not in what was read**: how reports show the payment method of offline-paid orders. Sorted against Shopify [3]: Q4-SH-033, Q4-SH-034. Q4-WC-N14
- **not in what was read**: reports split by payment method, or counting cash-on-delivery costs. Sorted against Salla [3]: Q4-SA-049, Q4-SA-052, Q4-SA-051. Q4-WC-N17
- **not in what was read**: reports of cash-on-delivery shipments delivered and collected. Sorted against Salla [3]: Q4-SA-064, Q4-SA-065. Q4-WC-N18
- **not in what was read**: Point of Sale payment methods in reports. Sorted against Salla [3]: Q4-SA-036, Q4-SA-037. Q4-WC-N19

## [4]

- **differs** (role): COD only for chosen shipping methods, and virtual orders only if ticked. Sorted against Salla [4]: Q4-SA-022, Q4-SA-026, Q4-SA-027, Q4-SA-028, Q4-SA-029, Q4-SA-030, Q4-SA-066, Q4-SA-K1584, Q4-SA-K1591. Q4-WC-033, Q4-WC-034, Q4-WC-K0039
- **differs** (role): Check payments "can also be useful to test purchases". Sorted against Shopify [4]: Q4-SH-028. Q4-WC-K0030
- **differs** (role): "Each WooCommerce store can set one base currency", used to record new orders. Sorted against Shopify [4]: Q4-SH-K1739, Q4-SH-010. Q4-WC-044
- **not in what was read**: an offline method offered to sellers in only one country. Sorted against Shopify [4]: Q4-SH-027. Q4-WC-N20
- **differs** (role): Order management belongs to the Shop Manager's "Manage orders" capability. Sorted against Shopify [4]: Q4-SH-036, Q4-SH-042, Q4-SH-043. Q4-WC-040
- **differs** (role): Point of Sale mode: store address in ten supported countries, native currency as store currency. Sorted against Salla [4]: Q4-SA-054, Q4-SA-005, Q4-SA-P0101. Q4-WC-035, Q4-WC-K1320, Q4-WC-K1321
- **not in what was read**: hiding an offline method by cart total, customer group or category. Sorted against Salla [4]: Q4-SA-055, Q4-SA-056, Q4-SA-057, Q4-SA-058, Q4-SA-K1664. Q4-WC-N04

## [5]

- **differs** (role): COD orders can be paid by card reader through WooPayments' In-Person Payments, which "marks orders “Complete” automatically". Eligible methods in code: `cod`, `woocommerce_payments`, `none`; stores US/USD or CA/CAD; the documentation lists ten countries; Stripe Terminal terms apply. Sorted against Salla [5]: Q4-SA-062, Q4-SA-K1585, Q4-SA-K1586, Q4-SA-014, Q4-SA-P0095, Q4-SA-K1589. Q4-WC-036, Q4-WC-037, Q4-WC-038, Q4-WC-K0438, Q4-WC-K0439, Q4-WC-K0440, Q4-WC-K0441

- **differs** (role): WooPayments "pays out money from incoming orders into your linked bank account" on a set schedule; the card reader fee is deducted from the WooPayments balance. Sorted against Salla [5]: Q4-SA-P0041, Q4-SA-P0042, Q4-SA-P0039, Q4-SA-P0093, Q4-SA-K1587; Salla [5]: Q4-SA-P0038, Q4-SA-023, Q4-SA-024, Q4-SA-025, Q4-SA-K1590. Q4-WC-045, Q4-WC-046
- **differs** (role): The COD page points to the "Advanced Cash on Delivery with Fee extension". Sorted against Shopify [5]: Q4-SH-045, Q4-SH-046. Q4-WC-047
- **not in what was read**: places where amounts collected in person are not shown, and how the seller follows them. Sorted against Salla [5]: Q4-SA-K1602, Q4-SA-P0150. Q4-WC-N06
