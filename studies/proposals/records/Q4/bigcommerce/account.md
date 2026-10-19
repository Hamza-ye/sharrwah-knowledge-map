# Q4 on BigCommerce: checked against Shopify and Salla

## [1]

- **differs** (role): BigCommerce's "offline payment methods" "do not require a credit card or a traditional payment gateway", and "collecting payment is not immediate"; shoppers see them at checkout. Against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737; Salla [1]: Q4-SA-P0099, Q4-SA-P0068. Q4-BC-P0114, Q4-BC-001
- **differs** (role): they are set up at Settings › Payments, Open tab. Against Shopify [1]: Q4-SH-K1735, Q4-SH-K1193. Q4-BC-003
- **differs** (role): Bank Deposit lets customers pay "directly into your bank account"; its Account Information shows after the order is complete. Against Salla [1]: Q4-SA-P0100, Q4-SA-003. Q4-BC-P0116
- **differs** (term): Cash on Delivery lets customers "pay you with cash"; the merchant gives an address for the payment and Delivery Information. Against Shopify [1]: Q4-SH-045; Salla [1]: Q4-SA-P0098. Q4-BC-P0117, Q4-BC-009, Q4-BC-010
- **differs** (role): Pay in Store has customers pay "at your physical store location". Against Salla [1]: Q4-SA-048. Q4-BC-P0120
- **differs** (role): manual orders created in the control panel "can reference an offline payment such as cash or check". Against Salla [1]: Q4-SA-007. Q4-BC-020
- **differs** (role): BigCommerce charges a fee on orders through Open Payment Providers, the store's "connected payment gateways", on self-service plans. Against Salla [1]: Q4-SA-K1639. Q4-BC-K0143, Q4-BC-K0149
- **differs** (term): with the standalone PayPal gateway, PayPal charges a per-transaction fee by region. Against Salla [1]: Q4-SA-K1626. Q4-BC-P0126
- **goes beyond:** API-created orders can carry `external_source` for "a POS or accounting system". Q4-BC-046
- **goes beyond:** B2B Edition keeps the Check method for buyers with a Company account; for others it recommends "another offline payment method" "if you wish to support payments outside of your checkout". Q4-BC-044
- **goes beyond:** the Master Services Agreement creates "No agency, partnership, joint venture or employment relationship". Q4-BC-P0129
- **not in what was read:** a term on whom the contract of sale is with, or who is merchant of record. Against Shopify [1]: Q4-SH-K1491, Q4-SH-K1492. Q4-BC-G0035
- **not in what was read:** who receives the payment for offline methods, and whether BigCommerce has any part in it. Against Salla [1]: Q4-SA-P0091, Q4-SA-P0199, Q4-SA-P0080. Q4-BC-H0008
- **not in what was read:** whether offline-paid orders show in any BigCommerce balance or dashboard. Against Salla [1]: Q4-SA-A0002. Q4-BC-N01
- **not in what was read:** a point-of-sale product of BigCommerce's own that takes cash, or records payments through intermediaries. Against Salla [1]: Q4-SA-031, Q4-SA-034. Q4-BC-N02

## [2]

- **differs** (role): BigCommerce's name is "Offline payment methods": Bank deposit, Cash on delivery, Check, Money order and Pay in store (Pay in-store in the gateways table); one guide names Bank Transfer. Against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [2]: Q4-SA-K1604, Q4-SA-K1579. Q4-BC-P0114, Q4-BC-006, Q4-BC-030, Q4-BC-032
- **differs** (identifier): B2B Edition codes are `bankdeposit`, `cod`, `cheque`, `moneyorder` and `instore`, each "(offline)"; `cod` is also Salla's key. Against Salla [2]: Q4-SA-050; Salla [1]: Q4-SA-K1608. Q4-BC-033, Q4-BC-037, Q4-BC-036, Q4-BC-039, Q4-BC-038
- **goes beyond:** `bpay` (BPAY, offline) is listed too, and `bigcommerce` covers "gift certificates, store credit, and manual payment". Q4-BC-035, Q4-BC-034
- **differs** (role): each method takes a Display Name shown at checkout; entering "Purchase Order" there makes a Purchase Order method, which B2B Edition builds on Check. Against Shopify [2]: Q4-SH-007. Q4-BC-007, Q4-BC-011, Q4-BC-031
- **differs** (role): a manual order's "Manual payment" option is for "record-keeping for over-the-phone or in-person orders that have already been paid", with a Description field. Against Shopify [2]: Q4-SH-035, Q4-SH-039. Q4-BC-021, Q4-BC-023
- **goes beyond:** `%%OrderID%%` puts the order ID in Bank Deposit instructions, only for that method. Q4-BC-008
- **not in what was read:** a list of the plans offering offline methods. Against Salla [2]: Q4-SA-K1605. Q4-BC-N03

## [3]

### Instructions and status

- **differs** (role): the merchant's instructions show in the email invoice and on the order confirmation page. Against Shopify [3]: Q4-SH-006, Q4-SH-009. Q4-BC-002, Q4-BC-P0118, Q4-BC-P0119
- **differs** (role): offline-paid orders are placed in Awaiting Payment ("payment has yet to be confirmed"); after payment the merchant sets another status by hand. Against Shopify [3]: Q4-SH-K1736, Q4-SH-005; Salla [3]: Q4-SA-018. Q4-BC-P0115, Q4-BC-025, Q4-BC-K0096
- **differs** (role): Pending, Awaiting Payment and Declined are unpaid; Captured, Awaiting Fulfillment, Awaiting Pickup, Awaiting Shipment, Completed, Refunded, Partially Refunded, Partially Shipped and Shipped are paid. Against Shopify [3]: Q4-SH-018; Salla [3]: Q4-SA-011. Q4-BC-026, Q4-BC-027
- **differs** (role): the Transactions API creates records for "payments that were processed externally"; a transaction carries `offline` and `custom` objects. Against Shopify [3]: Q4-SH-039; Salla [3]: Q4-SA-059. Q4-BC-K0100, Q4-BC-K0103, Q4-BC-045
- **not in what was read:** a field for a receipt or proof of payment. Against Salla [3]: Q4-SA-015. Q4-BC-N04
- **not in what was read:** recording a full or partial payment other than by status or the API. Against Shopify [3]: Q4-SH-012, Q4-SH-021. Q4-BC-N06
- **not in what was read:** emails while awaiting or on receiving payment. Against Shopify [3]: Q4-SH-020; Salla [3]: Q4-SA-063. Q4-BC-N07
- **not in what was read:** an automatic status for cash on delivery, or a payment deadline. Against Salla [3]: Q4-SA-019, Q4-SA-017. Q4-BC-N09, Q4-BC-N10
- **not in what was read:** converting an amount received in another currency. Against Shopify [3]: Q4-SH-026. Q4-BC-N12

### Refunds and cancelling

- **differs** (role): for Bank Deposit, COD, Check and Money Order the refund methods are "Original payment provider processed external to BigCommerce", Store Credit and Third party provider; the merchant must "manually provide the refund", and recording it is "an optional manual process"; it can't be re-processed. Against Shopify [3]: Q4-SH-K1492; Salla [3]: Q4-SA-008, Q4-SA-010. Q4-BC-P0010, Q4-BC-015, Q4-BC-016, Q4-BC-017, Q4-BC-018, Q4-BC-019
- **differs** (role): "Cancelling an order will not refund the order." Against Shopify [3]: Q4-SH-032. Q4-BC-028
- **not in what was read:** which orders can be deleted. Against Shopify [3]: Q4-SH-030. Q4-BC-N08

### Fees and billing

- **differs** (role): on self-serve plans, orders using offline payment methods are assessed an Open Payment Provider fee, as are other orders "processed externally to the BigCommerce platform"; contracted Performance plans are exempt. It is billed monthly and "must not be passed through to shoppers". Offline and manual orders count in GMV, and manual-payment orders "are counted toward your BigCommerce account billing". Against Shopify [3]: Q4-SH-K1740; Salla [3]: Q4-SA-K0051. Q4-BC-012, Q4-BC-013, Q4-BC-014, Q4-BC-021, Q4-BC-P0124, Q4-BC-P0125
- **not in what was read:** a carrier's cash-on-delivery fee, or a label cost taken from a balance. Against Salla [3]: Q4-SA-P0059, Q4-SA-013. Q4-BC-N11

### B2B Edition invoices

- **differs** (role): Purchase Order invoices carry "net payment terms" (Net 0 to Net 60); invoices can be issued automatically for offline orders; offline methods "cannot be selected" to pay invoices, and offline payments are "manually recorded". Against Shopify [3]: Q4-SH-014. Q4-BC-040, Q4-BC-041, Q4-BC-042, Q4-BC-043, Q4-BC-K0183, Q4-BC-P0011

### Reports

- **not in what was read:** a report or filter by payment method, or point-of-sale reports. Against Shopify [3]: Q4-SH-033; Salla [3]: Q4-SA-002, Q4-SA-049, Q4-SA-064, Q4-SA-K0582, Q4-SA-036, Q4-SA-042. Q4-BC-N05, Q4-BC-N02

## [4]

- **differs** (role): for each offline method the merchant checks Available Countries. Against Salla [4]: Q4-SA-054; Shopify [4]: Q4-SH-027. Q4-BC-P0121
- **differs** (role): "All offline payment methods support additional transactional currencies." Against Shopify [4]: Q4-SH-K1739. Q4-BC-029
- **differs** (role): checkout must be Optimized One-Page or Custom; setup needs Manage Payments and Manage Settings; the Manual payment option needs Finalize Manual Orders using Manual Payments. Against Shopify [4]: Q4-SH-042. Q4-BC-004, Q4-BC-005, Q4-BC-022
- **differs** (role): store-level methods can be enabled or disabled per B2B Company. Against Salla [4]: Q4-SA-055; Shopify [4]: Q4-SH-029. Q4-BC-K0184
- **goes beyond:** a manual order's payment method can't be changed once created. Q4-BC-024
- **goes beyond:** the Payments API "does not expose methods for processing offline payment methods". Q4-BC-K0118
- **not in what was read:** testing an offline method. Against Shopify [4]: Q4-SH-028. Q4-BC-N13
- **not in what was read:** order-value, product, customer or per-day conditions. Against Salla [4]: Q4-SA-022, Q4-SA-020. Q4-BC-N14
- **not in what was read:** a label rule tied to payment, or a point-of-sale subscription lapse. Against Salla [4]: Q4-SA-012, Q4-SA-040. Q4-BC-N15, Q4-BC-N02

## [5]

- **goes beyond:** through a supporting gateway, cash payment APMs (Boleto Bancário, Fawry) let the shopper pay a slip in cash at a retail location. Q4-BC-047, Q4-BC-048
- **not in what was read:** a BigCommerce service or named app collecting cash on delivery for the merchant. Against Shopify [5]: Q4-SH-046; Salla [5]: Q4-SA-062, Q4-SA-P0041, Q4-SA-P0038, Q4-SA-K1602, Q4-SA-060. Q4-BC-N16, Q4-BC-H0008
