# Q4 on Shopify: what Shopify shows

## [1]

- Shopify's Help Center describes "manual payment methods" for customers who don't want to pay by credit card: these customers can still place orders online, and the seller "can arrange to receive their payment in a way that works best for them", then approve the order. Q4-SH-001, Q4-SH-002, Q4-SH-K1737
- A seller picks a suggested manual payment method, or creates a custom one, on the Payment providers settings page (Settings > Payments). The admin files it as the "Manual payment methods" page under Payments. Q4-SH-K1735, Q4-SH-K1738, Q4-SH-K2859, Q4-SH-K2860, Q4-SH-K1193
- Shopify's terms say any contract of sale is "directly and only between you and the customer", and that the seller is the merchant of record. Q4-SH-K1491, Q4-SH-K1492
- For Italy, the Help Center says to set up COD (Cash on Delivery) as a custom manual payment method. Q4-SH-045
- The copied gaps on who is responsible for manual payment methods, and why they are placed as they are, stay open. Q4-SH-G0101, Q4-SH-G0102

## [2]

- Shopify calls these "Manual payment methods" (Arabic: "طرق الدفع اليدوية") and names cash on delivery (COD), money orders and bank transfers as common types. Q4-SH-003, Q4-SH-004
- A custom method takes a "Custom payment method name". The names Bank Deposit, Cash, Cash on Delivery (COD), custom, External Credit, External Debit, Gift Card, Money Order and Store Credit are reserved by Shopify. Q4-SH-007
- In the Admin API, Shopify records such payments with `orderCreateManualPayment` and `orderMarkAsPaid`, both described as recording "payments received outside the standard checkout process". Q4-SH-035, Q4-SH-039
- The list of suggested methods offered in Settings > Payments wasn't in what was read. Q4-SH-N03

## [3]

### Payment instructions and order status
- The seller writes "Payment instructions", which show on the order confirmation page. The customer sees the method's name and these instructions there. Q4-SH-006, Q4-SH-009
- Orders that use a manual payment method are marked as unpaid, or "Pending", on the Orders page. "Payment pending" lists an order created with a manual payment method, such as Cash On Delivery, as one of its reasons. Q4-SH-K1736, Q4-SH-008, Q4-SH-016
- "Unpaid" covers the Authorized, Pending, Expired and Partially paid payment statuses. "Paid" covers an order that "was marked as paid". The API enum `OrderDisplayFinancialStatus` lists PENDING, AUTHORIZED, PARTIALLY_PAID, PARTIALLY_REFUNDED, VOIDED, PAID, REFUNDED and EXPIRED. Q4-SH-018, Q4-SH-017, Q4-SH-044
- For pending payments, Shopify sends no Pending payment email when the seller uses a manual payment gateway. Q4-SH-020

### Recording the payment
- After the seller receives payment, they mark the order as paid on its details page (Collect payment > Mark as paid, "if you have accepted payment outside of Shopify") and fulfill it as they would an online payment. Q4-SH-005, Q4-SH-012, Q4-SH-013
- With "Mark as paid", the amount "isn't captured again by your payment provider", and an order confirmation email goes to the customer. Q4-SH-011
- `orderMarkAsPaid` creates a sale transaction for the full outstanding amount, updates the order's financial status, and logs payment events "for tracking and analytics purposes". Its scenarios include orders created with manual payment methods. Q4-SH-039, Q4-SH-040, Q4-SH-041
- `orderCreateManualPayment` records a manual payment for an order that isn't fully paid. It takes a payment method name (default 'Other') and a processedAt date, which may be in the past for imported transactions. Q4-SH-035, Q4-SH-037, Q4-SH-038
- On Shopify Plus, partial payments can be recorded through Collect payment > Record payment for orders with payment terms. "Manual payments aren't captured by Shopify." A recorded partial payment changes the order status to Partially paid and shows in the customer's account. Q4-SH-021, Q4-SH-022, Q4-SH-023, Q4-SH-024
- For a draft order marked as paid under international sales tools, the "Amount received" is converted at the live rate, and the seller updates it "for reporting purposes" if it differs. Q4-SH-026

### Payment terms
- Orders with Payment pending can take payment terms: Due on receipt, Due on fulfillment, Net term (net 7 to net 90) or Fixed term. An order not paid by the due date becomes Overdue, and the payment status shows "Due". Q4-SH-014, Q4-SH-015, Q4-SH-019, Q4-SH-K0917, Q4-SH-K1448

### Fees
- No third-party transaction fees are charged on manual payment methods, including draft orders marked as paid with a manual method. Q4-SH-K1740, Q4-SH-K1335, Q4-SH-025

### Refunds, cancelling and deleting
- The terms place refunds, among other things, on the seller. Q4-SH-K1492
- Orders paid with a manual payment method are among the only order types that can be deleted. Deleted orders "are no longer tracked in reports". Q4-SH-030, Q4-SH-031
- Cancelling an order that is fulfilled but whose payment isn't collected "prevents you from collecting payment". Q4-SH-032
- How a refund of an order paid by a manual method is handled wasn't in what was read. Q4-SH-N02

### Reports
- In the payments finance reports, an order marked as paid with the method "Other" shows its payment method as "Manual". These reports "are based on captured payments across your payment gateways". Q4-SH-033, Q4-SH-034

## [4]

- Accepting manual payments in multiple currencies requires Shopify Payments and the international sales tools. Q4-SH-K1739, Q4-SH-010
- Email money transfers, set up as a custom manual method, are available only to merchants in Canada. Q4-SH-027
- Manual payment methods don't support test mode: testing one takes a real order. Q4-SH-028
- For B2B company locations whose orders are submitted as drafts, manual payment methods don't display during the initial checkout. Q4-SH-029
- The API's `amount` field on `orderCreateManualPayment` needs a Shopify Plus store. Both mutations need the `write_orders` scope and the mark_orders_as_paid permission. The mutation's error codes include AMOUNT_EXCEEDS_BALANCE and CURRENCY_MISMATCH. Q4-SH-036, Q4-SH-042, Q4-SH-043
- A statement of the countries or plans where manual payment methods are offered wasn't in what was read. Q4-SH-N04

## [5]

- For Italy, the Help Center sends sellers to set up COD as a custom manual payment method, and points to App Store apps related to COD. Q4-SH-045, Q4-SH-046
- A Shopify service that collects cash on delivery for the seller wasn't in what was read. Q4-SH-N01
