# Q4 on WooCommerce: sorted against the Shopify and Salla accounts

## [1]

- **differs** (term, role): Direct Bank Transfer (BACS) lets customers "pay you directly via their bank account". It is "an offline payment method, meaning that the payment process is manual and happens outside your WooCommerce powered store". "Take payments in person via BACS"; off by default. Sorted against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [1]: Q4-SA-P0099, Q4-SA-P0068; Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737. Q4-WC-001, Q4-WC-002, Q4-WC-K0025, Q4-WC-K0028, Q4-WC-K0032
- **differs** (term, role): Cash on delivery, built in, lets "you take payments at the time of delivery of your customer’s ordered products": "by cash or other methods of payment". Off by default. Sorted against Salla [1]: Q4-SA-P0098, Q4-SA-K1530; Shopify [2]: Q4-SH-003, Q4-SH-004; Shopify [1]: Q4-SH-045. Q4-WC-004, Q4-WC-K0027, Q4-WC-K0029, Q4-WC-K0034
- **differs** (role): Check payments lets customers "place orders and pay offline by check"; off by default. Sorted against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737. Q4-WC-003, Q4-WC-K0026, Q4-WC-K0030, Q4-WC-K0033
- **differs** (role): "Offline" is a type of payment gateway: "No online payment is made." Sorted against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737. Q4-WC-K0031
- **differs** (role): Set at WooCommerce > Settings > Payments > Take offline payments: sections `offline`, `bacs`, `cheque`, `cod`; REST route `wc/v4` `offline-payment-methods`. Sorted against Shopify [1]: Q4-SH-K1735, Q4-SH-K1738, Q4-SH-K2859, Q4-SH-K2860, Q4-SH-K1193; Salla [1]: Q4-SA-003, Q4-SA-004, Q4-SA-006, Q4-SA-001. Q4-WC-005, Q4-WC-K0002, Q4-WC-K0021, Q4-WC-K0022, Q4-WC-K0023, Q4-WC-K0024, Q4-WC-K0035
- **differs** (role): The seller adds bank accounts (name, number, bank, routing number, IBAN, SWIFT/BIC), shown on the Order Received page and in order emails after checkout. Sorted against Salla [1]: Q4-SA-003, Q4-SA-004, Q4-SA-006, Q4-SA-001; Salla [1]: Q4-SA-P0100, Q4-SA-K1603, Q4-SA-021. Q4-WC-006, Q4-WC-007
- **differs** (role): Gateways are plugins; the terms: "third-party services, like Stripe or PayPal to collect payment", and "we’re not involved in any third-party services tied to those extensions". Sorted against Salla [1]: Q4-SA-K1639, Q4-SA-K1656, Q4-SA-K1636. Q4-WC-K0006, Q4-WC-K0007, Q4-WC-K0008, Q4-WC-K0010
- **differs** (role): Point of Sale mode (`point_of_sale`) is "a digital cash register" taking card or cash; for cash the seller enters the amount received and sees the change due. "All sales sync with your existing WooCommerce site." Sorted against Salla [1]: Q4-SA-031, Q4-SA-038, Q4-SA-033, Q4-SA-039, Q4-SA-K1402. Q4-WC-008, Q4-WC-009, Q4-WC-K1313, Q4-WC-K1318, Q4-WC-K1319, Q4-WC-K1323
- **not in what was read**: who the sale to the customer is between. Sorted against Shopify [1]: Q4-SH-K1491, Q4-SH-K1492. Q4-WC-N01
- **not in what was read**: how an order made with "Add new order" records an offline payment or its proof. Sorted against Salla [1]: Q4-SA-007, Q4-SA-K0504. Q4-WC-N02

## [2]

- **differs** (term, identifier): "Direct bank transfer" (BACS), "Check payments" ("Cheque" before 3.3) and "Cash on delivery" (COD), each an "offline payment method"; keys `bacs`, `cheque`, `cod`. Sorted against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [2]: Q4-SA-K1604 ("The names in the dashboard"), Q4-SA-K1579, Q4-SA-050, Q4-SA-054. Q4-WC-001, Q4-WC-002, Q4-WC-011, Q4-WC-K0022, Q4-WC-K0023, Q4-WC-K0024, Q4-WC-K0025, Q4-WC-K0026, Q4-WC-K0027
- **differs** (role): A Title "shown to customers during checkout". Sorted against Shopify [2]: Q4-SH-007. Q4-WC-012

## [3]

### Instructions and order status

- **differs** (term): "Instructions" for each method; for checks they "appear on the order thank-you page and in the order confirmation email". Sorted against Shopify [3]: Q4-SH-006, Q4-SH-009. Q4-WC-021, Q4-WC-022, Q4-WC-023
- **differs** (role): Bank transfer and check orders go On hold ("Awaiting BACS payment."); COD orders go to Processing "until payment is collected", or On hold with a downloadable item; filters can change each. Pending payment means "no payment has been made". Sorted against Shopify [3]: Q4-SH-K1736, Q4-SH-008, Q4-SH-016; Salla [3]: Q4-SA-018; Salla [3]: Q4-SA-019, Q4-SA-045, Q4-SA-046. Q4-WC-013, Q4-WC-015, Q4-WC-017, Q4-WC-020, Q4-WC-K0036, Q4-WC-K0037, Q4-WC-K0038, Q4-WC-K0039

### Recording the payment

- **differs** (role): "Offline payment methods require you to manually verify the payment was processed", then the seller changes the status (Processing or Completed; Complete for COD). Processing means "Payment has been received (paid)". Sorted against Shopify [3]: Q4-SH-005, Q4-SH-012, Q4-SH-013; Salla [3]: Q4-SA-015, Q4-SA-016, Q4-SA-K0563. Q4-WC-014, Q4-WC-016, Q4-WC-018, Q4-WC-019
- **differs** (role): REST `set_paid` sets the order to processing and reduces stock. Sorted against Shopify [2]: Q4-SH-035, Q4-SH-039; Shopify [3]: Q4-SH-039, Q4-SH-040, Q4-SH-041. Q4-WC-024, Q4-WC-K0984
- **differs** (role): In Point of Sale mode: "Mark payment as complete" after cash. Sorted against Shopify [3]: Q4-SH-005, Q4-SH-012, Q4-SH-013; Salla [3]: Q4-SA-032. Q4-WC-010
- **goes beyond**: WooPayments "does not possess the capability to interface with the BACS processing system"; merchants resolve discrepancies with customers and their bank. Q4-WC-027, Q4-WC-028

### Refunds

- **differs** (role): "Refund %s manually": "You will need to manually issue a refund through your payment gateway after using this."; an order can then be Refunded "without the customer’s funds having been returned". An order refunds API exists. Sorted against Salla [3]: Q4-SA-008, Q4-SA-009; Salla [3]: Q4-SA-010, Q4-SA-053. Q4-WC-025, Q4-WC-026, Q4-WC-K0995
- **differs** (role): Terms 8.j (Ecommerce Services) make the seller responsible for refunds and refund policies. Sorted against Shopify [3]: Q4-SH-K1492. Q4-WC-K0990, Q4-WC-K0991

### Fees

- **not in what was read**: any fee, or none, on offline-method orders. Sorted against Shopify [3]: Q4-SH-K1740, Q4-SH-K1335, Q4-SH-025; Salla [3]: Q4-SA-013; Salla [3]: Q4-SA-P0059, Q4-SA-K1593, Q4-SA-K1588; Salla [3]: Q4-SA-K0051. Q4-WC-N03

### Reports

- **differs** (role): Analytics > Settings > Excluded Statuses: by default Pending payment, Cancelled and Failed excluded, Processing, On hold and Completed included; Refunded can't be excluded. Default Date Type "Date Paid": "orders without a paid date are excluded". Sorted against Salla [3]: Q4-SA-K0582, Q4-SA-K2501. Q4-WC-029, Q4-WC-030, Q4-WC-031, Q4-WC-032, Q4-WC-K0599

## [4]

- **differs** (role): COD only for chosen shipping methods, and virtual orders only if ticked. Sorted against Salla [4]: Q4-SA-022, Q4-SA-026, Q4-SA-027, Q4-SA-028, Q4-SA-029, Q4-SA-030, Q4-SA-066, Q4-SA-K1584, Q4-SA-K1591. Q4-WC-033, Q4-WC-034, Q4-WC-K0039
- **differs** (role): Check payments "can also be useful to test purchases". Sorted against Shopify [4]: Q4-SH-028. Q4-WC-K0030
- **differs** (role): Point of Sale mode: store address in ten supported countries, native currency as store currency. Sorted against Salla [4]: Q4-SA-054, Q4-SA-005, Q4-SA-P0101. Q4-WC-035, Q4-WC-K1320, Q4-WC-K1321
- **not in what was read**: hiding an offline method by cart total, customer group or category. Sorted against Salla [4]: Q4-SA-055, Q4-SA-056, Q4-SA-057, Q4-SA-058, Q4-SA-K1664. Q4-WC-N04

## [5]

- **differs** (role): COD orders can be paid by card reader through WooPayments' In-Person Payments, which "marks orders “Complete” automatically at the time of payment". Code: eligible payment methods `cod`, `woocommerce_payments`, `none`; stores US/USD or CA/CAD. The documentation lists ten countries and default currencies only; Stripe Terminal terms apply. Sorted against Salla [5]: Q4-SA-062, Q4-SA-K1585, Q4-SA-K1586, Q4-SA-014, Q4-SA-P0095, Q4-SA-K1589. Q4-WC-036, Q4-WC-037, Q4-WC-038, Q4-WC-K0438, Q4-WC-K0439, Q4-WC-K0440, Q4-WC-K0441
