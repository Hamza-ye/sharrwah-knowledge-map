# D: The Shopify money data model (Admin GraphQL 2026-10, plus guides for purchase options, B2B, returns, order editing and multi-entity)

**Reader D.** This file covers the data model of money in the 2026-10 Admin GraphQL API, plus the developer guides for purchase options, B2B, returns and exchanges, order editing, multiple entities and order attribution.

## How claims are cited

- **[S:X]**: the type or enum appears in `schema/admin-2026-10-money.md` or in `/home/user/observed-sh/.../2026-10/items.jsonl`. These two files hold type names, fields and enum values. They have no field descriptions, and type descriptions are cut off at the first newline.
- **[R:X.field]**: the text comes from the shopify.dev reference page `https://shopify.dev/docs/api/admin-graphql/2026-10/<kind>/<X>.md`, fetched read-only. I fetched these because the extract has no field, argument or enum-value descriptions, and the invariants are written there.
- **[C:path]**: the claim comes from `corpus/dev/docs/<path>`, which mirrors `https://shopify.dev/docs/<path>`.
- **"Inference:"** marks my own reasoning rather than Shopify's text.

## Corpus anomalies

- `apps/build/orders-fulfillment/order-management-apps/manage-test-orders.md` is byte-identical to `edit-orders.md` (same md5). The live URL also serves the "Edit existing orders" page. No separate test-order guide exists in this slice.
- `orderPaymentStatus` says its `paymentReferenceId` is "returned by orderCreatePayment" [R:queries/orderPaymentStatus]. No `orderCreatePayment` mutation exists in the 2026-10 `Mutation` type [S:Mutation]. Only `orderCreateMandatePayment` and `paymentScheduleCapture` return a `paymentReferenceId`.

---

## 0. The model in one paragraph

Shopify keeps four money records that never collapse into one:

1. **Agreement ledger.** An append-only `SalesAgreement` stream on the `Order`. Each agreement holds signed `Sale` lines. It records what the buyer and merchant agreed and every later change to it.
2. **Payment-attempt ledger.** `OrderTransaction` records the authorize, capture, void and refund actions against payment providers. Each has a `kind` and a `status`, and they are chained by `parentTransaction`.
3. **Booked cash-flow ledger.** `TenderTransaction` is immutable and records only real money movement.
4. **Processor ledger.** `ShopifyPaymentsBalanceTransaction` records gross, fee and net, and feeds a `ShopifyPaymentsPayout`. Each payout is tied to a `BusinessEntity`.

**Obligation timing** is a separate object. `PaymentTerms` holds one or more `PaymentSchedule`s, each with `dueAt`, `balanceDue` and `totalBalance`. Because timing is separate, "what is owed" (agreement totals minus received money, shown as `Order.totalOutstandingSet`) can be collected later through:
- stored permission (`PaymentMandate` or `CustomerPaymentMethod`);
- an invoice link;
- a manual or offline record (`orderCreateManualPayment` or `orderMarkAsPaid`);
- a recurring engine (`SubscriptionContract` → `SubscriptionBillingCycle` → `SubscriptionBillingAttempt` → new `Order`).

**Stored value** sits in two ledgers outside the order: `StoreCreditAccount` (per owner and currency) and `GiftCard`. Each has its own typed transaction history. Store credit transactions point back to the `OrderTransaction` that caused them.

**Every amount** is a `MoneyBag` (shop currency plus presentment currency). Every order carries `merchantBusinessEntity` and may carry `merchantOfRecordApp`.

---

## 1. Entity map

The notation is `A —rel→ B [cardinality]`. Cardinality is read from list or connection types.

### 1.1 Order hub

```
Order
 ├─agreements→ SalesAgreement [0..n]   (OrderAgreement | OrderEditAgreement | RefundAgreement | ReturnAgreement)
 ├─transactions→ OrderTransaction [0..n]   (args: capturable, manuallyResolvable)
 ├─refunds→ Refund [0..n]
 ├─returns→ Return [0..n]
 ├─paymentTerms→ PaymentTerms [0..1]
 ├─paymentCollectionDetails→ OrderPaymentCollectionDetails [1] ─vaultedPaymentMethods→ PaymentMandate [0..n]
 ├─suggestedRefund(args)→ SuggestedRefund [computed]
 ├─disputes→ OrderDisputeSummary [0..n]
 ├─additionalFees→ AdditionalFee [0..n];  lineItems→ LineItem [n];  shippingLines→ ShippingLine [n]
 ├─purchasingEntity→ PurchasingEntity [0..1]  (B2B: company + location)
 ├─merchantBusinessEntity→ BusinessEntity [1]
 ├─merchantOfRecordApp→ OrderApp [0..1];  app→ OrderApp;  attribution→ OrderAttribution
 └─requestedOrderEdits→ RequestedOrderEdit [0..n]  (buyer-initiated)
```
Sources: [S:Order], [R:Order].

The `Order` object carries the derived money fields. Section 2.2 explains them:
- `originalTotalPriceSet`, `totalPriceSet`, `currentTotalPriceSet`
- `subtotalPriceSet`, `currentSubtotalPriceSet`
- `totalOutstandingSet`, `totalReceivedSet`, `netPaymentSet`, `totalRefundedSet`, `totalRefundedShippingSet`
- `totalCapturableSet`, `refundDiscrepancySet`, `totalCashRoundingAdjustment`, `totalTipReceivedSet`
- duties: `originalTotalDutiesSet` and `currentTotalDutiesSet`
- additional fees: `originalTotalAdditionalFeesSet` and `currentTotalAdditionalFeesSet`
- flags: `fullyPaid`, `unpaid`, `capturable`, `canMarkAsPaid`, `refundable`, `closed`, `test`, `edited`, `merchantEditable` with `merchantEditableErrors`, and `displayFinancialStatus`

### 1.2 Agreement ledger: what was agreed

```
SalesAgreement (interface: id, happenedAt, reason: OrderActionType, app, user: StaffMember)
 ├─ OrderAgreement ─order→ Order
 ├─ OrderEditAgreement
 ├─ RefundAgreement ─refund→ Refund [1]
 └─ ReturnAgreement ─return→ Return [1]
SalesAgreement ─sales→ Sale [1..n]
Sale (interface: actionType: SaleActionType, lineType: SaleLineType, quantity, taxes[SaleTax],
      totalAmount, totalDiscountAmountBeforeTaxes, totalDiscountAmountAfterTaxes, totalTaxAmount — all MoneyBag)
 ├─ ProductSale ─lineItem→ LineItem      ├─ TipSale ─lineItem→ LineItem
 ├─ GiftCardSale ─lineItem→ LineItem     ├─ ShippingLineSale ─shippingLine→ ShippingLine
 ├─ DutySale ─duty→ Duty                 ├─ AdditionalFeeSale ─additionalFee→ SaleAdditionalFee
 ├─ FeeSale ─fee→ Fee                    ├─ AdjustmentSale
 └─ UnknownSale  (forward-compatibility for "new sale types that have been added in future API versions")
```
Sources: [S:SalesAgreement], [S:Sale], [S:UnknownSale].

- Shopify "creates a sales agreement whenever an order is placed, edited, or refunded… A sale record is specific to a type of order line" [R:SalesAgreement].
- `OrderActionType` values: `ORDER`, `ORDER_EDIT`, `REFUND`, `RETURN`, `UNKNOWN` [R:enums/OrderActionType].
- `SaleActionType` values: `ORDER` ("A purchase or charge"), `RETURN` ("A removal or return"), `UPDATE` ("A change to the price, taxes, or discounts for a prior purchase") and `UNKNOWN` [R:enums/SaleActionType].
- `SaleLineType` values: `PRODUCT`, `TIP`, `GIFT_CARD`, `SHIPPING`, `DUTY`, `ADDITIONAL_FEE`, `FEE`, `ADJUSTMENT`, `UNKNOWN`.
- An `ADJUSTMENT` sale "represents the difference between the original total value of all line items that were refunded, and the actual amount refunded", for example a restocking fee or goodwill payment [S:SaleLineType].

### 1.3 Payment-attempt ledger: what was attempted or settled with a provider

```
OrderTransaction
 ├─order→ Order [0..1]        ├─parentTransaction→ OrderTransaction [0..1]  ("for example the authorization of a capture")
 ├─kind: OrderTransactionKind ├─status: OrderTransactionStatus ├─errorCode: OrderTransactionErrorCode
 ├─amountSet: MoneyBag        ├─amountRoundingSet: MoneyBag (cash rounding)
 ├─gateway / formattedGateway ├─manualPaymentGateway: Boolean
 ├─paymentDetails→ PaymentDetails (CardPaymentDetails | LocalPaymentMethodsPaymentDetails | PaypalWalletPaymentDetails | ShopPayInstallmentsPaymentDetails)
 ├─paymentId, accountNumber, receiptJson, paymentIcon
 ├─authorizationExpiresAt     ├─manuallyCapturable, multiCapturable, totalUnsettledSet
 ├─fees→ TransactionFee [n]   ├─settlementCurrency, settlementCurrencyRate
 ├─currencyExchangeAdjustment→ CurrencyExchangeAdjustment
 ├─shopifyPaymentsSet→ ShopifyPaymentsTransactionSet (extendedAuthorizationSet, refundSet.acquirerReferenceNumber)
 ├─device→ PointOfSaleDevice, location→ Location, user→ StaffMember
 └─maximumRefundableV2 (only for SuggestedRefund)
```
Sources: [S:OrderTransaction], [R:OrderTransaction].

Transactions are also reachable from other parents:
- `Refund.transactions`
- `Return.transactions`
- `SubscriptionBillingAttempt.transactions`
- `CashTrackingSession.cashTransactions`
- `OrderPaymentStatus.transactions`
- `StoreCreditAccountTransaction.origin` (the union `StoreCreditAccountTransactionOrigin` = `OrderTransaction`) [S].

Field semantics worth copying:
- `fees` is "Only present for Shopify Payments transactions".
- `currencyExchangeAdjustment` is "the amount lost or gained due to fluctuations in the currency exchange rate".
- `totalUnsettledSet` is "The amount of the original authorization that remains unsettled… During a pending capture, this reflects the full outstanding balance including the pending amount".
- `authorizationExpiresAt` is "available only to stores on a Shopify Plus plan".
- `receiptJson` "is gateway-specific and not a stable contract… Apps shouldn't parse or rely on this field for business logic" [R:OrderTransaction].
- `errorCode` is "A standardized error code, independent of the payment provider" [S:OrderTransactionErrorCode], with about 47 values such as `CARD_DECLINED`, `INSUFFICIENT_FUNDS`, `AUTHENTICATION_REQUIRED` and `AUTHORIZATION_EXPIRED`.
- `ShopifyPaymentsExtendedAuthorization` defines two expiries. `standardAuthorizationExpiresAt` is "The time after which capture will incur an additional fee". `extendedAuthorizationExpiresAt` is the time after which "the merchant is unable to capture the payment" [R].

### 1.4 Booked ledger and processor ledger

```
TenderTransaction  (QueryRoot.tenderTransactions — shop-level stream)
 ├─order→ Order [0..1] ("null if the order has been deleted")
 ├─amount: MoneyV2, processedAt, paymentMethod: String, remoteReference, test, user
 └─transactionDetails→ TenderTransactionDetails (TenderTransactionCreditCardDetails)

ShopifyPaymentsAccount (per BusinessEntity) ─balance→ [MoneyV2] (multi-currency)
 ├─balanceTransactions→ ShopifyPaymentsBalanceTransaction [n]
 │     amount, fee, net, type: ShopifyPaymentsTransactionType (~110 values), sourceType: ShopifyPaymentsSourceType,
 │     sourceId, sourceOrderTransactionId (→ OrderTransaction), associatedOrder, adjustmentReason, adjustmentsOrders[],
 │     associatedPayout {id, status: ShopifyPaymentsBalanceTransactionPayoutStatus}
 ├─payouts→ ShopifyPaymentsPayout [n]  (gross, net, issuedAt, status, transactionType DEPOSIT|WITHDRAWAL,
 │     summary: ShopifyPaymentsPayoutSummary, bankAccount, businessEntity [1], externalTraceId)
 ├─payoutSchedule (interval DAILY|WEEKLY|MONTHLY|MANUAL + anchors) ├─bankAccounts→ ShopifyPaymentsBankAccount
 └─disputes→ ShopifyPaymentsDispute (amount, type INQUIRY|CHARGEBACK, status, reasonDetails, evidenceDueBy, finalizedOn, order, disputeEvidence)
```
Sources: [S], [R:TenderTransaction], [R:ShopifyPaymentsBalanceTransaction], [R:ShopifyPaymentsPayout].

### 1.5 Refunds, returns and adjustments

```
Refund ─order→ Order [1]; ─return→ Return [0..1]
 ├─refundLineItems→ RefundLineItem [n] (lineItem, quantity, restockType, location, priceSet, subtotalSet, totalTaxSet)
 ├─refundShippingLines→ RefundShippingLine [n] (shippingLine, subtotalAmountSet, taxAmountSet)
 ├─duties→ RefundDuty [n] (originalDuty, amountSet)
 ├─orderAdjustments→ OrderAdjustment [n] (amountSet, taxAmountSet, reason: OrderAdjustmentDiscrepancyReason)
 ├─transactions→ OrderTransaction [n]
 └─totalRefundedSet
Order.suggestedRefund(refundLineItems, refundDuties, shipping, refundMethodAllocation: ORIGINAL_PAYMENT_METHODS|STORE_CREDIT…)
 → SuggestedRefund (amountSet, maximumRefundableSet, subtotalSet, discountedSubtotalSet, totalTaxSet, totalDutiesSet,
    totalCartDiscountAmountSet, refundLineItems, refundDuties, shipping,
    suggestedTransactions→ SuggestedOrderTransaction(kind SUGGESTED_REFUND, parentTransaction, maximumRefundableSet),
    suggestedRefundMethods→ SuggestedRefundMethod (SuggestedStoreCreditRefund: amount, maximumRefundable, expiresAt))
Return ─order→ Order; status: ReturnStatus; returnLineItems; exchangeLineItems→ ExchangeLineItem; returnShippingFees→ ReturnShippingFee;
 reverseFulfillmentOrders; refunds→ Refund [n]; transactions→ OrderTransaction [n];
 suggestedFinancialOutcome(args)→ SuggestedReturnFinancialOutcome
   (financialTransfer: ReturnOutcomeFinancialTransfer = InvoiceReturnOutcome | RefundReturnOutcome, maximumRefundable, totalTax, totalDuties, totalAdditionalFees…)
```
Sources: [S], [R:Refund], [R:SuggestedRefund], [R:Return], [R:unions/ReturnOutcomeFinancialTransfer].

- `OrderAdjustment` "accounts for the difference between a calculated and actual refund amount" [S].
- `InvoiceReturnOutcome.amount` is "The total monetary value to be invoiced" [R]. A return or exchange can therefore end with the **buyer owing money**, not only with a refund.

### 1.6 Terms, schedules, mandates and instruments

```
PaymentTermsTemplate (name, paymentTermsType, dueInDays)    (QueryRoot.paymentTermsTemplates)
PaymentTerms ─order→ Order [0..1] | ─draftOrder→ DraftOrder [0..1]
 (paymentTermsName, paymentTermsType: PaymentTermsType, dueInDays, due, overdue)
 └─paymentSchedules→ PaymentSchedule [1..n] (issuedAt, dueAt, completedAt, due, balanceDue, totalBalance; amount DEPRECATED)
PaymentMandate (id, paymentInstrument: PaymentInstrument = BankAccount | VaultCreditCard | VaultPaypalBillingAgreement)
CustomerPaymentMethod ─customer→ Customer
 ├─instrument→ CustomerPaymentInstrument (BankAccount | CustomerCreditCard | CustomerPaypalBillingAgreement | CustomerShopPayAgreement)
 ├─mandates→ PaymentMandateResource [n] (resourceType: MandateResourceType, resourceId)
 ├─subscriptionContracts→ SubscriptionContract [n]
 └─revokedAt, revokedReason: CustomerPaymentMethodRevocationReason
```
Sources: [S], [R].

- `PaymentMandate` is "A payment instrument and the permission the owner of the instrument gives to the merchant to debit it" [R].
- `PaymentMandateResource.id` "Matches the corresponding `CustomerPaymentMethod.id` token, so partners can identify which payment method to use for a given mandate scope (e.g., SUBSCRIPTIONS)" [R].
- `MandateResourceType` values: `CREDENTIAL_ON_FILE`, `CHECKOUT`, `DRAFT_ORDER`, `ORDER`, `SUBSCRIPTIONS` [R].
- Inference: one stored instrument carries several scoped permissions (mandates). The order sees only the mandates scoped to it, through `Order.paymentCollectionDetails.vaultedPaymentMethods`.

### 1.7 Draft order (pre-order quote, invoice, B2B)

`DraftOrder` has these money and lifecycle fields [S], [R:DraftOrder]:
- status: `status: DraftOrderStatus`, `ready` (async calculation finished), `completedAt`
- totals: `totalPriceSet`, `subtotalPriceSet`, `lineItemsSubtotalPrice`, `totalDiscountsSet`, `totalShippingPriceSet`, `totalTaxSet`
- payment split: `deposit: DepositConfiguration` (`DepositPercentage`), `amountDueNowSet`, `amountDueLaterSet`, `paymentTerms`
- inventory: `reserveInventoryUntil`
- invoice: `invoiceUrl`, `invoiceSentAt`
- parties: `purchasingEntity`, `order→ Order [0..1]`
- currency: `presentmentCurrencyCode` and `currencyCode`
- `warnings: [DraftOrderWarning]`

### 1.8 Stored value

```
StoreCreditAccount ─owner→ HasStoreCreditAccounts (Customer, CompanyLocation) ; balance: MoneyV2 (one currency)
 └─transactions→ StoreCreditAccountTransaction [n] (account, amount, balanceAfterTransaction, createdAt, event: StoreCreditSystemEvent, origin→ OrderTransaction)
     ├ StoreCreditAccountCreditTransaction (expiresAt, remainingAmount)
     ├ StoreCreditAccountDebitTransaction
     ├ StoreCreditAccountDebitRevertTransaction ─debitTransaction→ Debit
     └ StoreCreditAccountExpirationTransaction ─creditTransaction→ Credit
GiftCard (initialValue, balance, expiresOn, enabled, deactivatedAt, crossCurrencyRedemptionStrategy, isRedeemable,
          customer, recipientAttributes→ GiftCardRecipient, order/lineItem [0..1] — "null if the gift card was issued manually")
 └─transactions→ GiftCardTransaction [n]: GiftCardCreditTransaction | GiftCardDebitTransaction | GiftCardCashOutTransaction
```
Sources: [S], [R:StoreCreditAccount], [R:GiftCard].

A store credit account "has an owner that cannot be transferred. The account balance is redeemable at checkout only when the owner is authenticated via new customer accounts" [R:StoreCreditAccount].

### 1.9 Purchase-option layer

```
SellingPlanGroup [1]──[n] SellingPlan ──[n] Product/ProductVariant
SellingPlan: category (SUBSCRIPTION|PRE_ORDER|TRY_BEFORE_YOU_BUY|OTHER), billingPolicy (Fixed|Recurring), deliveryPolicy (Fixed|Recurring),
             inventoryPolicy→ SellingPlanInventoryPolicy.reserve (ON_SALE|ON_FULFILLMENT), pricingPolicies
SellingPlanFixedBillingPolicy: checkoutCharge→ SellingPlanCheckoutCharge(type PERCENTAGE|PRICE, value),
             remainingBalanceChargeTrigger, remainingBalanceChargeExactTime, remainingBalanceChargeTimeAfterCheckout (ISO8601 duration)
SellingPlanFixedDeliveryPolicy: fulfillmentTrigger (ANCHOR|ASAP|EXACT_TIME|UNKNOWN), fulfillmentExactTime, anchors, cutoff, preAnchorBehavior, intent
SubscriptionContract ─customer, ─customerPaymentMethod→ CustomerPaymentMethod [0..1], ─originOrder→ Order, ─orders→ Order [n],
             ─billingAttempts→ SubscriptionBillingAttempt [n], billingPolicy, deliveryPolicy, deliveryPrice, lines, discounts,
             status, lastPaymentStatus, lastBillingAttemptErrorType, nextBillingDate, revisionId, latestCommittedProjectedOrderTotals, app
SubscriptionBillingCycle ─sourceContract→ SubscriptionContract; ─editedContract→ SubscriptionBillingCycleEditedContract [0..1]
             cycleIndex, cycleStartAt, cycleEndAt, billingAttemptExpectedDate, skipped, edited, status (BILLED|UNBILLED), billingAttempts [n]
SubscriptionBillingAttempt ─subscriptionContract [1]; idempotencyKey; originTime; paymentGroupId; paymentSessionId;
             respectInventoryPolicy; state: SubscriptionBillingAttemptState; transactions→ OrderTransaction [n]
```
Sources: [S], [R:SellingPlan], [R:SellingPlanFixedBillingPolicy], [R:SubscriptionContract], [R:SubscriptionBillingCycle], [R:SubscriptionBillingAttempt].

### 1.10 Cash and point-of-sale

```
CashDrawer (location, balance, netSales, totalSales/Refunds/Adjustments/Discrepancies, cashActivities, pointOfSaleDevices)
PointOfSaleDevicePaymentSession ─pointOfSaleDevice [1], ─cashDrawer [1], ─location [1]
 (status OPEN|CLOSED, currency, cashCountedAtOpen/Close, expectedCashAtOpen/Close, closingAdjustment, totalDiscrepancy,
  netCashSales, totalCashSales, totalCashRefunds, totalSales, totalRefunds, totalAdjustments, totalsReady,
  openingStaffMember/closingStaffMember, cashActivities→ CashActivity (CashAdjustmentActivity|CashCountActivity|CashTransactionActivity: cash, staffMember, time))
CashTrackingSession (older model: openingBalance, expectedOpeningBalance, expectedBalance, closingBalance, expectedClosingBalance,
  totalDiscrepancy, adjustments→ CashTrackingAdjustment, cashTransactions→ OrderTransaction [n])
```
Sources: [S], [R:PointOfSaleDevicePaymentSession], [R:CashTrackingSession].

### 1.11 Entities and currency

- `MoneyBag {shopMoney, presentmentMoney}` appears on almost every amount [S:MoneyBag].
- `Order.currencyCode` is "The shop currency when the order was placed". `Order.presentmentCurrencyCode` is "The currency used by the customer" [R:Order].
- `BusinessEntity` holds `address`, `companyName`, `displayName`, `legalEntityId`, `primary`, `archived` and `shopifyPaymentsAccount` [S]. "Every shop must have one primary business entity" [R:BusinessEntity].
- Relations: `Order.merchantBusinessEntity [1]`, `ShopifyPaymentsPayout.businessEntity [1]`, and `Market` assigned to an entity [C:apps/build/markets/multiple-entities.md].

---

## 2. Separate ledgers and the derived order money fields

### 2.1 The ledgers

| Ledger | Record | Grain | Mutability | What it is authoritative for |
|---|---|---|---|---|
| (a) Agreed | `SalesAgreement` with its `Sale`s | per order event (place, edit, refund, return) × line type | Append-only. Corrections are new agreements with `RETURN` or `UPDATE` sales or `ADJUSTMENT` lines. "The allocation of currency units across line items is immutable… never reallocated" [S:Sale] | Revenue, discount, tax and duty per line; the reason (`OrderActionType`); the actor (`app`, `user`) |
| (b) Attempted or settled | `OrderTransaction` | per provider action | Status can move, for example `PENDING` to `SUCCESS` (Inference). Corrections are new child transactions (`VOID`, `REFUND`) linked by `parentTransaction` | Authorization, capture and refund facts; gateway; errors; fees; settlement currency |
| (c) Booked | `TenderTransaction` | per real money movement | "immutable once created" | Cash flow: "always represents actual money movement between a buyer and a shop… can be used instead of OrderTransactions for reconciling a shop's cash flow" [R:TenderTransaction] |
| (d) Processor | `ShopifyPaymentsBalanceTransaction` → `ShopifyPaymentsPayout` | per balance movement | Reversals are separate types (`*_REVERSAL`, `DISPUTE_REVERSAL`, `CHARGEBACK_HOLD_RELEASE`) | Gross, fee and net per source; payout membership. "The payout only contains balance transactions that were available at this time [issuedAt]" [R:ShopifyPaymentsPayout] |

Two further ledgers sit beside these:
- **Timing ledger:** `PaymentTerms` and `PaymentSchedule`, which say when the outstanding balance is due.
- **Stored-value ledgers:** `StoreCreditAccountTransaction` and `GiftCardTransaction`, which keep their own `balanceAfterTransaction` or `balance`.

How the ledgers link:
- A balance transaction points to the payment attempt via `sourceOrderTransactionId`, and to the order via `associatedOrder`.
- A store credit transaction points to the payment attempt via `origin`.
- A refund agreement (`RefundAgreement.refund → Refund.transactions`) ties (a) to (b).
- Inference: `TenderTransaction` has no foreign key to `OrderTransaction`. Reconciling (c) to (b) uses `order`, `processedAt`, amount and `remoteReference`. A tender record is best read as a projection of the successful, money-moving transactions (`SALE`, `CAPTURE`, `REFUND`, and probably `CHANGE`). Authorizations, voids and failures never become tender.

Two documented reconciliation gaps:
- For online exchanges, "captured payments are not yet directly associated with the return. To reconcile these, you can fetch all transactions on the `Order` and match them to the `SalesAgreement` based on the amount and creation timestamp" [C:apps/build/orders-fulfillment/returns-apps/read-exchanges.md].
- `Return.transactions` is populated for "POS returns and exchanges: Includes both refunds and captured payments" and for "Online returns and exchanges: Includes refunds only" (same file).

### 2.2 Order money fields and where each comes from

Quotes are from [R:Order]. "Inference" marks the formula I reconstructed.

| Field | Shopify definition | Derived from (Inference) |
|---|---|---|
| `originalTotalPriceSet` | "total price of the order at the time of order creation" | The `OrderAgreement` sales only |
| `totalPriceSet` | "total price of the order, before returns… includes taxes and discounts" | Placement plus edits, before returns |
| `currentTotalPriceSet` | "total price of the order, after returns" | Sum over all agreements' sales (ORDER + UPDATE − RETURN) |
| `currentSubtotalPriceSet`, `currentTotalTaxSet`, `currentTotalDiscountsSet`, `currentTotalDutiesSet`, `currentTotalAdditionalFeesSet`, `currentShippingPriceSet` | "after returns, refunds, order edits, and cancellations" | Same, split by `SaleLineType` |
| `totalReceivedSet` | "total amount received from the customer before returns" | Successful `SALE` plus `CAPTURE` transactions (and manual payments) |
| `totalRefundedSet` | "total amount that was refunded" | Successful `REFUND` transactions. `totalRefundedShippingSet` is the shipping portion |
| `netPaymentSet` | "based on the total amount received minus the total amount refunded" | received − refunded |
| `totalOutstandingSet` | "total amount not yet transacted… positive… merchant's favor (payment from customer to merchant)… negative… customer's favor (refund from merchant to customer)" | ≈ `currentTotalPriceSet` − `netPaymentSet` ± adjustments. **It is signed**: one field expresses both "owed" and "owing" |
| `totalCapturableSet` | "authorized amount that's uncaptured or undercaptured… This amount isn't adjusted for returns" | Successful `AUTHORIZATION` minus `CAPTURE` and `VOID` (`OrderTransaction.totalUnsettledSet` per authorization) |
| `refundDiscrepancySet` | "difference between the suggested and actual refund amount of all refunds… positive… merchant's favor" | Sum of `Refund.orderAdjustments`, compared against `SuggestedRefund` |
| `totalCashRoundingAdjustment` | `CashRoundingAdjustment {paymentSet, refundSet}`: "can be applied to totalReceived [or totalRefunded]… positive or negative… 0… for non-cash" | Sum of `OrderTransaction.amountRoundingSet` |
| `totalTipReceivedSet` | "sum of all tip amounts" | `TipSale` |
| `fullyPaid` | "true when the total amount received equals or exceeds the order total" | |
| `unpaid` | "Whether no payments have been made" | |
| `capturable` | "an authorized payment exists that hasn't been fully captured yet" | |
| `canMarkAsPaid` | "false if the order is already paid, is canceled, has pending Shopify Payments transactions, or has a negative payment amount" | |
| `refundable` | "false for orders with no eligible payment transactions, such as fully refunded orders or orders with non-refundable payment methods" | |
| `closed` | "all its line items have been fulfilled or canceled, and all financial transactions are complete" | |

Other derived amounts outside `Order`:
- `CalculatedOrder.totalOutstandingSet` during an edit: "Total price of the order less the total amount received from the customer" [R:CalculatedOrder]. This is the clearest statement of the formula.
- `DraftOrder.amountDueNowSet`: "When there are payment terms this is the value of the deposit (0 by default). When there are no payment terms, this is the total price." `amountDueLaterSet`: "total price minus the deposit amount (if any). When there are no payment terms, this is 0" [R:DraftOrder].
- `PaymentSchedule.balanceDue` is "Remaining balance to be **captured**". `totalBalance` is "Remaining balance to be **paid or authorized**" [R:PaymentSchedule]. Inference: a schedule can be covered by an authorization (`totalBalance`=0) while still needing capture (`balanceDue`>0). The deprecated `PaymentSchedule.amount` points to "`balanceDue`, `totalBalance`, or `Order.totalOutstandingSet`" [S:items.jsonl]. So the schedule's money is derived, not stored.

---

## 3. State machines

### 3.1 `OrderTransactionKind` × `OrderTransactionStatus`

Kinds [R:enums/OrderTransactionKind]:
- `AUTHORIZATION`: "reserved against the cardholder's funding source. Money does not change hands until… captured"
- `CAPTURE`: "transfer of the money that was reserved by an authorization"
- `SALE`: "authorization and capture performed together in a single step"
- `VOID`: "cancelation of an authorization transaction"
- `REFUND`: "partial or full return of captured funds… can happen only after a capture is processed"
- `CHANGE`: "money returned to the customer when they've paid too much during a cash transaction"
- `EMV_AUTHORIZATION`: card-present authorization
- `SUGGESTED_REFUND`: "can be used to create a refund"

Statuses: `PENDING`, `AWAITING_RESPONSE`, `SUCCESS`, `FAILURE`, `ERROR`, `UNKNOWN` [R:enums/OrderTransactionStatus].

The graph below is my reading of the kinds and the `parentTransaction` links (Inference):
```
AUTHORIZATION(SUCCESS) ──CAPTURE(parent=auth)×n [multiCapturable; finalCapture voids remainder]──▶ captured
        │                    └─ partial capture → order PARTIALLY_PAID
        ├──VOID(parent=auth)──▶ released (order VOIDED if nothing captured)
        └──(no capture before expiry)──▶ order EXPIRED (errorCode AUTHORIZATION_EXPIRED)
SALE(SUCCESS) ≡ authorization+capture
CAPTURE|SALE ──REFUND(parent=capture|sale)×n ──▶ PARTIALLY_REFUNDED / REFUNDED
Any kind: PENDING|AWAITING_RESPONSE → SUCCESS | FAILURE | ERROR | UNKNOWN
```
Rules that constrain the graph:
- `ReturnRefundOrderTransactionInput.parentId`: "The transaction must be of kind `CAPTURE` or a `SALE`" [R].
- `transactionVoid(parentTransactionId)` takes "An uncaptured authorization transaction" [R].

### 3.2 `OrderDisplayFinancialStatus` and how it is derived

Shopify defines the values by observable payment facts [R:enums/OrderDisplayFinancialStatus]:
- `PENDING`: "payment provider needs time to complete the payment, or when manual payment methods are being used"
- `AUTHORIZED`: "appears only for manual payment capture… should be captured before the authorization period expires"
- `PARTIALLY_PAID`: "manually captured… less than the full order value"
- `PAID`: "automatically or manually captured, or the order was marked as paid"
- `PARTIALLY_REFUNDED` / `REFUNDED`: refunded less than / the full amount paid
- `VOIDED`: "authorized but uncaptured payment was voided… distinct from the order's status: an order can remain open even when its payment is voided"
- `EXPIRED`: "Payment wasn't captured before the payment provider's deadline"

Inference: the status is a projection of (b) against (a), roughly comparing `totalReceivedSet`, `totalCapturableSet`, `totalRefundedSet` and pending transactions with the current total. Imported orders can override it at creation only. `OrderCreateFinancialStatus` "Can only be set when the order is created". If omitted, it "will be derived through the given transactions… it's possible to specify a status that doesn't match the given transactions and it will persist, but if an operation later occurs on the order, the status may then be recalculated" [R:OrderCreateOrderInput.financialStatus].

### 3.3 Payment terms and schedules

- `PaymentTermsType` values [R]:
  - `RECEIPT`: "due on receipt"
  - `NET`: "due a number of days after issue"
  - `FIXED`: "due on a specified date"
  - `FULFILLMENT`: "due on fulfillment"
  - `UNKNOWN`
- Schedule state comes from flags and timestamps, not an enum [R:PaymentSchedule], [R:PaymentTerms]:
  - `issuedAt` ("when the invoice is sent")
  - `dueAt`
  - `due`
  - `completedAt` ("when the payment schedule is paid or fulfilled")
  - `PaymentTerms.due` ("has a payment schedule that's due")
  - `PaymentTerms.overdue` ("has overdue payment schedules")
- Inference: the implied states are issued, due, overdue and completed. A `FULFILLMENT` schedule gets its `dueAt` only when the fulfillment event occurs.
- `PaymentScheduleInput` rules: `dueAt` "must be provided for fixed type payment terms". `issuedAt` "must be provided for net type payment terms" [R].

### 3.4 `DraftOrderStatus`

- `OPEN`: "not been paid, and an invoice hasn't been sent"
- `INVOICE_SENT`
- `COMPLETED`: "The draft order has been paid" [R]

Inference: `COMPLETED` really means converted to an `Order` (`completedAt`, `order`). Completion with payment terms produces an unpaid order, so "paid" is loose wording. `ready` gates completion because "Draft orders might have asynchronous operations".

### 3.5 Subscriptions

- **Contract** (`SubscriptionContractSubscriptionStatus`) [R]:
  - `ACTIVE`
  - `PAUSED`: "expected to resume"
  - `CANCELLED`: "ended by an unplanned customer action"
  - `EXPIRED`: "ended per the expected circumstances. All billing and delivery cycles… executed"
  - `FAILED`: "ended because billing failed and no further billing attempts are expected"
  - Transitions are explicit mutations: `subscriptionContractActivate`, `subscriptionContractPause`, `subscriptionContractCancel`, `subscriptionContractExpire`, `subscriptionContractFail`. "The create input doesn't accept a status" [C:apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract.md].
  - App uninstall: "48 hours after a user uninstalls a subscription app, any subscription contracts… that haven't been terminated are cancelled" [C:…/subscriptions/contracts.md].
  - `lastPaymentStatus` is `SUCCEEDED` or `FAILED`.
- **Billing cycle**:
  - `status` is `BILLED` or `UNBILLED`, with flags `skipped` and `edited`.
  - The index "doesn't reset when a contract is edited".
  - "Billing occurs at the end of each cycle for the upcoming delivery period".
  - Edits only to "the current billing cycle and any billing cycle that's up to 1 year after" [C:…/subscriptions/billing-cycles.md].
- **Billing attempt** (`SubscriptionBillingAttemptState` union) [R], [C:…/build-a-subscription-contract.md]:
  - `SubscriptionBillingAttemptPendingState {processing}` → `SubscriptionBillingAttemptSuccessState {order}` (terminal), or
  - → `SubscriptionBillingAttemptFailedState {error: General|Inventory|Payment|Unexpected}` (terminal), or
  - → `SubscriptionBillingAttemptActionRequiredState {action: SubscriptionBillingAttemptPaymentChallenge {nextActionUrl, status: OFF_SESSION_REJECTED→ON_SESSION_CHALLENGED}}`, which then moves to a terminal state.
  - Old flat fields (`errorCode`, `nextActionUrl`, `order`, `ready`, `processingError`) are deprecated: "Use `state` instead" [S:items.jsonl].
  - "The `subscription_billing_attempts/success` and `…/failure` webhooks aren't triggered until the challenge is completed. If the customer doesn't complete the challenge, then your app won't be notified."

### 3.6 `ReturnStatus`

Transitions [C:apps/build/orders-fulfillment/returns-apps.md]:
- `returnRequest` → `REQUESTED`
- `returnDeclineRequest` → `DECLINED` (only from `REQUESTED`, only if not refunded; permanent)
- `returnApproveRequest`, `returnCreate` or `returnReopen` → `OPEN` (approval is permanent)
- `returnProcess` → `CLOSED` "when all items have been processed and a restock decision has been made"
- `removeFromReturn` → `CLOSED` when empty
- `returnCancel` → `CANCELED` (only if `OPEN`, not refunded, no dispositions, no Shopify Shipping label)
- `returnClose` → `CLOSED`

Financial side:
- "Returns and exchanges only appear in sales agreements after they're processed" [C:…/returns-apps/read-exchanges.md].
- Canceling a return reverses "all sales records generated from the creation of a return" [C:…/returns-apps/build-return-management.md].
- `Order.returnStatus: OrderReturnStatus` is an aggregate for display only (`NO_RETURN`, `RETURN_REQUESTED`, `IN_PROGRESS`, `INSPECTION_COMPLETE`, `RETURNED`, `RETURN_FAILED`).

### 3.7 Disputes

- `DisputeType`: `INQUIRY` or `CHARGEBACK`. `type` "Indicates if this dispute is still in the inquiry phase or has turned into a chargeback" [R].
- `DisputeStatus`: `NEEDS_RESPONSE`, `UNDER_REVIEW`, `WON`, `LOST`, `ACCEPTED`, `PREVENTED` ("prevented from becoming a formal chargeback"), and `CHARGE_REFUNDED` (deprecated).
- Timestamps: `initiatedAt`, `evidenceDueBy`, `evidenceSentOn`, `finalizedOn`.
- Evidence is submitted through `disputeEvidenceUpdate(input.submitEvidence)`.
- Money effects show in the processor ledger as `DISPUTE_WITHDRAWAL`, `DISPUTE_REVERSAL`, `CHARGEBACK_FEE`, `CHARGEBACK_FEE_REFUND`, `CHARGEBACK_HOLD`, `CHARGEBACK_HOLD_RELEASE` [S:ShopifyPaymentsTransactionType].

### 3.8 Stored-value transaction kinds

- **Store credit** [R]:
  - Types: credit, debit, debit revert, expiration.
  - Credits carry `expiresAt` and a `remainingAmount`, which "will decrease when a debit spends this credit. It may also increase if that debit is subsequently reverted".
  - "Debit transactions will always spend the soonest expiring credit first."
  - Debit reverts occur "when an order is cancelled, refunded or in the event of a payment failure at checkout".
  - Expiration subtracts "the remaining amount of the credit transaction".
  - `StoreCreditSystemEvent` values: `ADJUSTMENT`, `ORDER_PAYMENT`, `ORDER_REFUND`, `PAYMENT_FAILURE` ("reverted due to another payment method failing"), `PAYMENT_RETURNED` ("smaller amount… captured than… authorized"), `ORDER_CANCELLATION` ("returned when an authorized payment was voided"), `TAX_FINALIZATION`, `RECURRING_PAYMENT`.
  - Inference: store credit follows authorize-then-capture semantics inside the order.
- **Gift card**: credit, debit, and cash-out ("balance was redeemed for cash"). Deactivation is irreversible: "After a gift card is deactivated, it can't be used for further purchases or re-enabled" [R:GiftCard].

### 3.9 Payout and balance transaction

- `ShopifyPaymentsPayoutStatus` [R]:
  - `SCHEDULED`: "created and had transactions assigned… not yet submitted to the bank"
  - `PAID`: "deposited"
  - `FAILED`: "declined by the bank"
  - `CANCELED`: "canceled by Shopify"
  - `IN_TRANSIT`: deprecated
- A balance transaction's payout status adds `PENDING` and `ACTION_REQUIRED` [S].
- Payout direction is `DEPOSIT` or `WITHDRAWAL`, so a negative balance can pull money from the bank.

### 3.10 POS session and async jobs

- **POS session:** `OPEN` → `CLOSED`. "Payments can't be processed or refunded during a closed session, and the cash drawer balance can't be adjusted or corrected" [S:PointOfSaleDevicePaymentSessionStatus].
- **Async job results:**
  - `OrderCancelStatus` and `OrderCreateMandatePaymentStatus`: `STARTED`, `SUCCEEDED`, `FAILED`.
  - `OrderPaymentStatusResult`: `INITIATED`, `PENDING`, `PROCESSING`, `REDIRECT_REQUIRED`, `RETRYABLE`, `AUTHORIZED`, `CAPTURED`, `PURCHASED`, `SUCCESS`, `PARTIAL_SUCCESS`, `VOIDED`, `REFUNDED`, `ERROR`, `UNKNOWN` [S].
  - Inference: a payment request has its own lifecycle, separate from the transactions it produces.

---

## 4. Operations: mutation, effect, preconditions

Quotes are from [R:mutations/X] unless marked otherwise.

**Capture, void and payment recording**

- **`orderCapture(input: OrderCaptureInput{id, parentTransactionId, amount, currency, finalCapture})`**
  - Effect: creates a `CAPTURE` transaction.
  - Requires the `capture_payments_for_orders` permission.
  - "The capture amount can't be greater than the amount of the authorized transaction."
  - `currency` "must be the presentment currency… required… where the currency and presentment currency differ".
  - Multi-capture "as long as the order transaction is multi-capturable"; Plus only.
  - `finalCapture`: "Only applies to Shopify Payments authorizations which are multi-capturable. If true, any uncaptured amount from the authorization will be voided… defaults to false".
- **`transactionVoid(parentTransactionId)`**
  - Effect: creates a `VOID` against "An uncaptured authorization transaction".
  - Requires permission to cancel orders.
- **`orderMarkAsPaid(input{id})`**
  - "An order can be marked as paid only if it has a positive outstanding balance and its financial status isn't already `PAID`."
  - It "will either create a new sale transaction for the full outstanding amount or capture an existing authorized transaction".
- **`orderCreateManualPayment(id, amount, paymentMethodName, processedAt)`**
  - Records "a manual payment for an `Order` that isn't fully paid". Partial amounts are allowed; `amount` is Plus only.
  - `paymentMethodName` defaults to 'Other'.
  - `processedAt` can be backdated.
  - Errors: `AMOUNT_NOT_POSITIVE`, `AMOUNT_EXCEEDS_BALANCE`, `CURRENCY_MISMATCH`, `PROCESSED_AT_INVALID`, `ORDER_IS_TEMPORARILY_UNAVAILABLE` [S].
  - Inference: this is the generic "offline tender" primitive for cash on delivery, bank transfer and similar.

**Mandate and schedule collection**

- **`orderCreateMandatePayment(id, mandateId, idempotencyKey!, amount, autoCapture=true, paymentScheduleId)`**
  - Effect: async `Job` plus `paymentReferenceId`. "Subsequent calls with the same key return the original payment result rather than creating a new payment."
  - `autoCapture:false` means authorize only.
  - `amount` is Plus only.
  - Scopes: `write_payment_mandate` and `pay_orders_by_vaulted_card`.
  - Poll with `orderPaymentStatus(orderId, paymentReferenceId)` [R:queries/orderPaymentStatus].
- **`paymentScheduleCapture(paymentScheduleId)`**
  - "Captures payment for a due `PaymentSchedule` using the vaulted payment method associated with the order… resolves the order and mandate from the given payment schedule".
  - Async; the job result reuses `OrderCreateMandatePaymentJobResult`.
- **`paymentReminderSend(paymentScheduleId)`**: sends an email reminder and returns `success`.

**Payment terms**

- **`paymentTermsCreate(referenceId, {paymentTermsTemplateId, paymentSchedules})`**, plus **`paymentTermsUpdate`** and **`paymentTermsDelete`**
  - Order only. "To create payment terms on a draft order, use a draft order mutation and include the request with the `DraftOrderInput`."
  - Error codes are coarse: `PAYMENT_TERMS_CREATION_UNSUCCESSFUL` and similar.

**Draft orders and invoices**

- **`draftOrderComplete(id, paymentGatewayId, sourceName, paymentPending[deprecated])`**
  - Converts the draft to an order with these options: "Mark the order as paid immediately", "Set the order as payment pending using payment terms", "Specify a custom payment amount", "Select a specific payment gateway".
  - "When completing a draft order, inventory is reserved".
  - Requires "access to mark as paid, or set payment terms".
- **`draftOrderInvoiceSend(id, email)`**: sends the `invoiceUrl` checkout link. `draftOrderInvoicePreview` previews it.
- **`orderInvoiceSend(id, email)`**: the same for an existing order, used for exchange balances [C:…/returns-apps/manage-exchanges.md] and for edits.

**Refunds and returns**

- **`refundCreate(RefundInput)`**
  - Input fields:
    - `refundLineItems` (with restock)
    - `shipping`
    - `refundDuties`
    - `transactions: [OrderTransactionInput{amount, gateway, kind, orderId, parentId}]`
    - `refundMethods: [RefundMethodInput{storeCreditRefund{amount, expiresAt}}]`, "instructions to process the financial outcome"
    - `allowOverRefunding` (default false): "allow the total refunded amount to surpass the amount paid"
    - `discrepancyReason: OrderAdjustmentInputDiscrepancyReason` (`RESTOCK`, `DAMAGE`, `CUSTOMER`, `OTHER`)
    - `currency` (presentment)
    - `processedAt`, `notify`
  - Idempotency: "As of 2026-04, the idempotency key is required and must be provided using the `@idempotent` directive."
  - Effect: a `Refund` plus a `RefundAgreement`, plus `OrderAdjustment`s when actual ≠ calculated (Inference, from [S:OrderAdjustment]).
  - Guidance for prepaid subscriptions: "refund specific line items and quantities rather than refunding custom dollar amounts. Refunding custom amounts negatively impacts merchant sales reporting" [C:…/subscriptions/fulfillments.md].
- **`returnProcess(ReturnProcessInput{returnId, returnLineItems{id, quantity, dispositions}, exchangeLineItems, refundDuties, refundShipping, tipLineId, financialTransfer{issueRefund{orderTransactions[{parentId, transactionAmount}], refundMethods, allowOverRefunding}}, notifyCustomer})`**
  - "confirms the quantities… creates `FulfillmentOrder` objects for exchange items and records all transactions in the merchant's financial reports".
  - Refunding is optional or deferred: "You may also choose not to refund at all and instead refund at a later time" [C:…/build-return-management.md].
  - `returnRefund` is deprecated in favour of `returnProcess`. It worked only "when the return status is `OPEN` or `CLOSED`".
  - Difference from `refundCreate`: `refundCreate` lets you specify restocking; `returnProcess` ties the refund to return line items and dispositions.
- **Exchanges with a balance due**
  - "Only exchanges with a net payable balance due by the buyer are placed on hold". The hold is fulfillment `ON_HOLD` with reason `AWAITING_PAYMENT`.
  - Sequence: `orderInvoiceSend` → payment → `fulfillmentOrderReleaseHold` [C:…/manage-exchanges.md].
  - "Native exchanges do not create a separate new order. They're updates to the existing order" [C:…/read-exchanges.md].

**Cancellation and editing**

- **`orderCancel(orderId, reason, restock!, refundMethod{originalPaymentMethodsRefund | storeCreditRefund{expiresAt}}, notifyCustomer, staffNote; refund deprecated)`**
  - Async job.
  - "Authorized payments will be voided regardless of this setting."
  - Preconditions: "hasn't already been cancelled", "no pending payment authorizations", "no active returns in progress", "no outstanding fulfillments that can't be cancelled". Irreversible.
  - Errors: `NO_REFUND_PERMISSION`, `NO_REFUND_TO_STORE_CREDIT_PERMISSION`, `STORE_CREDIT_REFUND_EXPIRATION_IN_PAST`, `STORE_CREDIT_REFUND_MISSING_CUSTOMER`, `STORE_CREDIT_REFUND_B2B_NOT_SUPPORTED` [S].
- **`orderEditBegin(id)` → `CalculatedOrder` + `OrderEditSession`; staged `orderEdit*` mutations; `orderEditCommit(id, notifyCustomer, staffNote)`**
  - "You can only edit unfulfilled line items. If an edit changes the total order value, then the customer might need to pay a balance or receive a refund."
  - Store currency only: "Editing orders placed in international currencies requires…" Checkout Extensions; no orders before 2019 [C:…/order-management-apps/edit-orders.md].
  - Inference on the money mechanics: commit appends an `OrderEditAgreement` with `UPDATE`/`ORDER`/`RETURN` sales. `currentTotalPriceSet` moves and `totalOutstandingSet` becomes positive (owed) or negative (credit). `Order.paymentCollectionDetails` ("for an order that requires additional payment following an edit") exposes `additionalPaymentCollectionUrl` and `vaultedPaymentMethods` (`PaymentMandate`s) for `orderCreateMandatePayment`. A negative balance is settled with `refundCreate`. `notifyCustomer:true` sends "an email invoice with the updated order information".

**Imported orders**

- **`orderCreate(order: OrderCreateOrderInput{financialStatus, transactions[OrderCreateOrderTransactionInput{kind=SALE, status=SUCCESS, amountSet, gateway, giftCardId, authorizationCode, receiptJson, processedAt, locationId, deviceId, test}], currency, presentmentCurrency, companyLocationId, processedAt, sourceName…}, options{inventoryBehaviour BYPASS|DECREMENT_IGNORING_POLICY|DECREMENT_OBEYING_POLICY, sendReceipt, sendFulfillmentReceipt})`**
  - Used for imports or orders that don't come through checkout.
  - Transactions are recorded facts, not processed; this is my reading of `status` defaulting to `SUCCESS`, an inference.
  - `presentmentCurrency` "must be specified if any presentment currencies are used".
  - Future `processedAt` is "clamped to the current time" as of 2026-07.

**Stored value**

- **`storeCreditAccountCredit(id = account | Customer | CompanyLocation, {creditAmount, expiresAt, notify})`**
  - "automatically creates an account if one doesn't exist for the specified currency".
  - Errors include `CREDIT_LIMIT_EXCEEDED`, `UNSUPPORTED_CURRENCY`, `EXPIRES_AT_IN_PAST`, `MISMATCHING_CURRENCY`.
- **`storeCreditAccountDebit(id, {debitAmount})`**: errors include `INSUFFICIENT_FUNDS`, `MISMATCHING_CURRENCY`.
- **`giftCardCredit` / `giftCardDebit(id, {amount, note, processedAt})`**: for top-ups and corrections. Errors: `INSUFFICIENT_FUNDS`, `GIFT_CARD_LIMIT_EXCEEDED`, `MISMATCHING_CURRENCY`, `NEGATIVE_OR_ZERO_AMOUNT`. `giftCardDeactivate` is one-way.

**Subscription billing**

- **`subscriptionBillingAttemptCreate(subscriptionContractId, {idempotencyKey!, originTime, billingCycleSelector, paymentProcessingPolicy, inventoryPolicy, actor})`**
  - "creates an `Order` when successful".
  - `paymentProcessingPolicy` values: `FAIL_UNLESS_VALID_PAYMENT_METHOD` (default) and `SKIP_PAYMENT_AND_CREATE_UNPAID_ORDER` ("create an unpaid order").
  - `inventoryPolicy` values: `PRODUCT_VARIANT_INVENTORY_POLICY` and `ALLOW_OVERSELLING`.
  - `originTime` keeps fulfillment on the anchor when billing is late.
- **`subscriptionBillingCycleCharge`** and **`subscriptionBillingCycleBulkCharge`**: "a single successful charge per billing cycle, and only charges cycles with a billing attempt expected date in the past or within the next 24 hours" [C:…/billing-cycles/manage-billing-cycle-contracts.md].

**Vaulting and payment methods**

- **`customerPaymentMethodRemoteCreate(customerId, remoteReference{stripePaymentMethod | authorizeNetCustomerPaymentProfile | braintreePaymentMethod})`**
  - Imports a gateway token. `EXACTLY_ONE_REMOTE_REFERENCE_REQUIRED`.
  - "initially has incomplete details… poll… until all details are available or the payment method is revoked".
- **`customerPaymentMethodCreditCardCreate/Update(sessionId)`**: the `sessionId` comes from Shopify's Cardserver/"Cardsink", obtained "in a PCI complaint environment". The payload has `processing` (true means the method is null for now).
- **`customerPaymentMethodPaypalBillingAgreementCreate/Update`**: billing agreement IDs "begin with `B-`" [C:…/migrate-customer-information.md].
- **`customerPaymentMethodRevoke`**: "Revocation will fail if the payment method has active subscription contracts."
- **`customerPaymentMethodGetUpdateUrl`**: "only supports Shop Pay".
- **`customerPaymentMethodSendUpdateEmail`**: sends the customer an email to update the method.
- **`paymentInstrumentSendAddEmail(mandate{resourceId, resourceType})`**: "secure link to add a new payment instrument… for a specific resource such as a subscription, order, or draft order".
- **`customerPaymentMethodGetDuplicationData(customerPaymentMethodId, targetShopId, targetCustomerId)` → `encryptedDuplicationData` → `customerPaymentMethodCreateFromDuplicationData`**
  - Copies a vaulted method to another shop.
  - Errors `SAME_SHOP` and `INVALID_ORGANIZATION_SHOP` [S] suggest it works within one organization (Inference).

**POS cash**

- `pointOfSaleDevicePaymentSessionOpen` (`balance` optional; errors `ALREADY_OPEN`, `NO_CASH_DRAWER_ASSOCIATED`)
- `pointOfSaleDevicePaymentSessionCount` (mid-session count)
- `pointOfSaleDevicePaymentSessionAdjust(cash, staffMemberId, reasonCodeId, note)`
- `pointOfSaleDevicePaymentSessionClose(balance!)`
- All of them carry `staffMemberId!` and an optional `reasonCodeId` (`cashManagementReasonCodeCreate`). Errors: `SESSION_ALREADY_CLOSED`, `TIME_BEFORE_SESSION_OPEN`, `CURRENCY_MISMATCH` [S].
- Drawer setup: `cashDrawerCreate`, `cashDrawerFindOrCreate`, `pointOfSaleDeviceAssignToCashDrawer`.

---

## 5. Purchase options: separating "what is owed" from "when it is collected"

**Shared mechanism.** A `SellingPlan` attaches four independent policies to a line: pricing, billing, delivery and inventory. "Billing: Defines the intervals of time between the placement of an order and payment collection. Delivery: … from the time that the order is created to the time that it leaves the merchant's possession. Inventory: … committed when the order is created or when the order is fulfilled" [C:apps/build/purchase-options.md]. "Delivery and billing policies must be either all `recurring` or all `fixed`" [C:…/purchase-options/deferred.md]. Inference: Shopify treats the timing of money, the timing of goods and the timing of stock reservation as three separate axes on the same agreement.

**Deferred purchases (pre-order and TBYB)** [C:…/deferred.md], [C:…/deferred/model-deferred-purchase-solutions.md]:
- **What is owed** is fixed at checkout: the full order total is in the `OrderAgreement`.
- **When it is collected**:
  - `SellingPlanFixedBillingPolicy.checkoutCharge` (`PERCENTAGE` or `PRICE`) is charged at checkout.
  - `remainingBalanceChargeTrigger` (`NO_REMAINING_BALANCE`, `EXACT_TIME`, `TIME_AFTER_CHECKOUT` with an ISO8601 duration such as `P14D`, `ON_FULFILLMENT`) sets when the rest is charged.
  - Shopify materialises this as `PaymentTerms` on the order: "Orders with a deferred payment will have an attached payment term that indicates when the payment should be made and how".
  - Odd wording: "You can set the checkout charge value to `0` to charge the full amount at checkout". This conflicts with `NO_REMAINING_BALANCE`, and the theme guide says TBYB checkout charge "will usually be $0" ([C:storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines.md]).
- **Aggregation rules when a cart mixes plans**:
  - "each order can have only one deferred payment due date"
  - "only the earliest due date is applied"
  - "the due on fulfillment payment term takes precedence over any specific date"
  - "All deposits are summed and charged at checkout"
  - Payment-customization-function terms "are only considered when the cart contains at least one line not associated to a selling plan"
  - Function deposits "Apply to all lines without a selling plan"
  - Shipping in an all-deferred cart: "the customer will pay the shipping cost when the remaining balance amount is charged" [C:…/deferred/delivery-and-deferment.md]
- **Permission to collect later.** "Shopify also vaults the payment method" at checkout. The app collects with `orderCreateMandatePayment` using a `mandateId` from `Order.paymentCollectionDetails.vaultedPaymentMethods`, an idempotency key and optionally `paymentScheduleId`, then polls `orderPaymentStatus`.
- **Who owns what.**
  - Shopify: "Collecting initial payments", "Storing payment methods", "Managing inventory".
  - App: "Charging customers on the balance due date", "Scheduling fulfillments", "Handling trial and return periods", and automating any process around payment failures ("It's your app's responsibility to schedule the charge at the right time and automate any process around payment failures").
- **Inventory and fulfillment.** `inventoryPolicy.reserve` is `ON_SALE` or `ON_FULFILLMENT`. `deliveryPolicy.fixed.fulfillmentTrigger` is `ASAP`, `EXACT_TIME`, `UNKNOWN` or `ANCHOR`.
- **Constraints.**
  - Gateways limited to Shopify Payments, PayPal Express, Adyen and some Stripe.
  - No local payment methods.
  - Not on draft orders, B2B or POS.
  - The Order Edits API "only supports removing a product with a pre-orders or TBYB".
- **Prohibitions.** "Don't vault payment methods for any purpose other than processing recurring or deferred payments", "Don't overbill", and don't use the APIs for "installments, layaways, and crowdfunding" [C:…/model-deferred-purchase-solutions.md].
- **Consumer protection.** Pre-order apps must obtain "customer consent to delays that exceed 30 days if no shipping time is stated and include a mechanism to return the funds".

**Subscriptions** [C:…/subscriptions/model-subscriptions-solution.md], [C:…/contracts.md], [C:…/fulfillments.md]:
- **Checkout to contract.** "Shopify first creates a transaction and then an order… then generates a subscription contract and creates a billing attempt on the initial purchase." Contracts arrive asynchronously ("rely on subscription contract webhooks").
- **The contract is detached from the plan.** "Updating the original plan doesn't modify pre-existing subscription contracts."
- **What is owed per cycle is the contract, not the plan.**
  - The pricing policy "serves as a guide… the price of the line item does not update automatically".
  - In the new calculate API, `appManagedPricingPolicy` "doesn't drive the calculated price". The app sets `priceOverride`; "Omitted priceOverride reprices the line" from the current variant price [C:…/contracts/migrate-to-subscription-calculation-api.md].
  - Contract changes go through `SubscriptionContractCalculation` (calculate → poll → commit; "Nothing is created or applied until the calculation is committed"; commit errors include `STALE_CONTRACT`).
  - Shown to the merchant as `latestCommittedProjectedOrderTotals`.
- **When it is collected.**
  - `SubscriptionBillingPolicy` (`interval`, `intervalCount`, `anchors`, `minCycles`/`maxCycles`) generates `SubscriptionBillingCycle`s.
  - The app initiates each charge. Shopify: "Billing and processing purchase payments". App: "Scheduling and automating payments… and handles billing failures".
  - Each successful attempt creates a **new Order** with its own agreements and transactions.
  - Retry guidance: "Only rebill… error codes that make sense to retry, such as `INSUFFICIENT_FUNDS`… [not] more than 30 times in 35 days. These requests will be failed and the payment method will be revoked". This matches `CustomerPaymentMethodRevocationReason.TOO_MANY_CONSECUTIVE_FAILURES`.
  - `paymentGroupId` ("shared between retried payment attempts") and `paymentSessionId` ("shared between payment attempts with similar payment details") de-duplicate success metrics.
- **Prepaid subscriptions.**
  - "bill less frequently than you deliver". The billing cadence must be a whole multiple of the delivery cadence.
  - One `Order` holds all cycles: "checkout line item quantity is `1` and order line item quantity is `3`". There are N `FulfillmentOrder`s in `SCHEDULED` status with `fulfillAt`, and inventory is committed when each opens.
  - Refunds unwind in reverse chronological order and "doesn't automatically cancel the renewal".
  - "Changes to fulfillment orders aren't automatically reflected on subscription contracts, and… vice versa."
  - For contracts that are already billed, edit the `Order`; for unbilled ones, edit the contract [C:…/fulfillments/sync-orders-subscriptions.md].
- **Combining contracts.** `subscriptionBillingCycleContractConcatenateCalculate` lets one attempt produce **one order linked to several contracts**. It uses "the anchor's payment method and policies". Every named member is billed "even when none of your `lines` carry an `originLineId` from it" [C:…/contracts/combine-subscription-contracts.md].
- **No payment method.** "create and commit a contract without a payment method by passing `paymentMethod: { none: true }`… pass `paymentProcessingPolicy: SKIP_PAYMENT_AND_CREATE_UNPAID_ORDER`… order… can be paid using an invoice or through manual payment capture" [C:…/migrate-subscription-contracts.md].
- **Checkout charge.** Subscriptions always have checkout charge `percentage` 100 [C:storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme.md].

---

## 6. B2B

- **Buyer and location configuration.** Parties are `Company` → `CompanyLocation` → `CompanyContact`. A purchase carries `PurchasingEntity` (company plus location plus contact). Money policy lives on the location's `BuyerExperienceConfiguration` [R:CompanyLocation]:
  - `paymentTermsTemplate` ("merchant configured payment terms")
  - `deposit: DepositPercentage` (input `DepositInput.percentage` "Must be between 1 and 99, inclusive")
  - `checkoutToDraft` ("checkout to draft order for merchant review")
  - `editableShippingAddress`
  - It is set with `companyLocationUpdate(buyerExperienceConfiguration{paymentTermsTemplateId…})` [C:apps/build/b2b/manage-client-company-locations.md].
- **Pay-now-only is derived.** `payNowOnly` is deprecated: "Please use `checkoutToDraft` (must be false) and `paymentTermsTemplate` (must be nil) to derive this instead" [S:items.jsonl]. Inference: Shopify modelled "pay now" as the absence of terms and review, not as a separate flag.
- **Checkout-to-draft.** The checkout submits a `DraftOrder` rather than an `Order`. Checkout UI can detect `checkoutSettings.orderSubmission === 'DRAFT_ORDER'` [C:apps/build/b2b/create-checkout-ui.md]. The merchant then reviews and runs `draftOrderInvoiceSend` / `draftOrderComplete` [C:apps/build/b2b/draft-orders.md]. The money split appears as `DraftOrder.amountDueNowSet` (deposit) and `amountDueLaterSet` (terms).
- **Collection under terms.**
  - `PaymentTerms` / `PaymentSchedule` on the order.
  - `paymentReminderSend`.
  - `paymentScheduleCapture` uses "the vaulted payment method associated with the order" (mandate scopes `ORDER` and `DRAFT_ORDER`).
  - Offline payments use `orderCreateManualPayment` / `orderMarkAsPaid`.
  - Inference: vaulted cards for B2B are order- or draft-scoped `PaymentMandate`s rather than subscription-scoped `CustomerPaymentMethod`s.
- **Pricing.** Catalogs with price lists per location. Where several catalogs apply, buyers "receive the lowest listed price within those catalogs" [C:apps/build/b2b/start-building.md].
- **Store credit.** `CompanyLocation` implements `HasStoreCreditAccounts`, and `storeCreditAccountCredit` accepts a `CompanyLocation` ID. However, `orderCancel` returns `STORE_CREDIT_REFUND_B2B_NOT_SUPPORTED` [S], so refund-to-credit on cancel is blocked for B2B.
- **Imports.** `orderCreate` with `companyLocationId` plus `customer.toAssociate`. The customer "must have a role assignment to the specified company location". `priceSet` is optional: "the API populates the price automatically based on the variant price… can result in inaccurate order data" [C:apps/build/b2b/import-orders.md].
- **Exclusion.** "B2B doesn't support purchase options, such as subscriptions, pre-orders, and try before you buy" [C:apps/build/b2b.md].

---

## 7. Multiple entities and merchant of record

- **`BusinessEntity` as the legal seller.**
  - "Every shop must have one primary business entity".
  - "You can only assign one legal entity for each country" [C:apps/build/markets/multiple-entities.md].
- **What changes when an order falls under another entity.**
  1. **Routing.** "Each individual market… can be assigned one of your shop's legal entities… customers… contextualized into this market will only be shown the set of payment methods that have been enabled for the respective legal entity". This is set via `marketCreate` / `marketUpdate` with `business_entity_id`.
  2. **Processor account.** "Each legal entity… can onboard its own Shopify Payments account… allowing payments and orders on these accounts to be routed to a specific legal entity… process domestic transactions… wider range of potential payout currencies". `BusinessEntity.shopifyPaymentsAccount` → its own balances, balance transactions, disputes, bank accounts and payouts. `ShopifyPaymentsPayout.businessEntity` is non-null.
  3. **Attribution.** `merchantBusinessEntity` appears on `Order`, `DraftOrder`, `Market` and `ShopifyPaymentsPayout`, and as `merchantBusinessEntityId` in REST and webhooks. `Order.merchantBusinessEntity` is "Used for tax reporting, legal compliance, and determining which business entity is responsible for the order" [R:Order].
  4. **Limits.**
     - "Third party payment providers, Subscriptions, Reporting and Analytics" are available only for the primary entity.
     - "only Shopify Payments, PayPal Express, and manual payment methods are supported across multiple entities".
     - Inference: the ledgers stay per shop while the processor ledger splits per entity.
- **`merchantOfRecordApp`** (`OrderApp`): "The application acting as the Merchant of Record for the order. The Merchant of Record is responsible for tax collection and remittance" [R:Order]. The schema separates three roles: who created the order (`Order.app`), who is the legal seller for tax (`merchantOfRecordApp`), and which entity of the shop is responsible (`merchantBusinessEntity`). Inference: no other money field changes type, so MoR changes responsibility, not the shape of the ledgers.
- **Channel attribution** (actors, not money):
  - `Order.attribution` is resolved from the `sourceName` handle.
  - Definitions are "retain[ed]… after a merchant uninstalls your app so historical orders can still resolve".
  - Deleting a definition "doesn't change historical orders" [C:apps/build/sales-channels/order-attribution.md].

---

## 8. Invariants and rules worth copying

1. **Sales allocation.** Sales are in minor units. The remainder is allocated "one at a time, starting with the first line item". The allocation is "immutable… never reallocated" [S:Sale].
2. **Agreements are append-only and itemised.** A refund that differs from line value produces reversal sales plus one `ADJUSTMENT` sale for the difference [S:SaleLineType]. The payment side records the same difference as `OrderAdjustment` with a reason, rolled up as `Order.refundDiscrepancySet` with a sign convention ("positive… merchant's favor").
3. **Outstanding balance is signed.** One field covers both directions (`totalOutstandingSet`). Payment primitives reject amounts beyond it (`AMOUNT_EXCEEDS_BALANCE`). Refunds reject amounts beyond what was paid unless `allowOverRefunding:true`.
4. **Transaction chaining.**
   - Capture ≤ authorization.
   - Void only an uncaptured authorization.
   - Refund only after capture; the refund parent is a `CAPTURE` or `SALE`.
   - `finalCapture` voids the remainder.
   - `totalCapturableSet` "isn't adjusted for returns".
5. **Currency discipline.**
   - Every amount is a `MoneyBag`.
   - Capture and refund currency must be the presentment currency when it differs from the shop currency.
   - Store credit accounts are single-currency, with one account per owner per currency.
   - Gift cards declare a `crossCurrencyRedemptionStrategy` (`NONE`, `MARKET_FX` "Only applicable for gift cards issued in the shop currency", `SPOT_FX`).
   - FX gain or loss on a transaction is explicit (`currencyExchangeAdjustment`).
   - Order editing is limited to store-currency orders.
6. **Idempotency on every money-creating call.** `orderCreateMandatePayment.idempotencyKey!`, `SubscriptionBillingAttemptInput.idempotencyKey!` ("avoid duplicate payments"), and `refundCreate` `@idempotent` (required from 2026-04). Retried commits are safe: "Retrying a commit for an already committed calculation returns the committed result" [C:…/build-a-subscription-contract.md].
7. **Async money operations return a job or reference that you poll.** `orderCancel` (`OrderCancelJobResult`), `orderCreateMandatePayment` and `paymentScheduleCapture` (`paymentReferenceId` → `orderPaymentStatus`), billing attempts (`state`), and `customerPaymentMethodRemoteCreate` ("incomplete state… poll").
8. **One-way transitions.** Approved or declined returns, cancelled orders, deactivated gift cards and committed calculations ("A successful calculation is immutable") cannot be reversed. Corrections are new records, for example `returnReopen` and debit-revert transactions.
9. **Test isolation.** `Order.test`: "A test order can't be converted into a real order and vice versa". `test` appears on `OrderTransaction`, `TenderTransaction` and balance transactions.
10. **Closed POS session freezes money.** "Payments can't be processed or refunded during a closed session". Every cash movement records `staffMember`, `time` and an optional reason code. Expected and counted amounts are both kept, and the difference is `totalDiscrepancy`.
11. **Permission is scoped and revocable.**
    - Mandates are scoped by `MandateResourceType`.
    - Revocation carries a reason enum (`MANUALLY_REVOKED`, `MERGED`, `CUSTOMER_REDACTED`, `TOO_MANY_CONSECUTIVE_FAILURES`, `CVV_ATTEMPTS_LIMIT_EXCEEDED`, gateway causes).
    - A payment method cannot be revoked while active subscription contracts use it.
    - Vaulting is restricted to recurring or deferred purposes.
12. **Store credit expiry.** Earliest-expiring credit is spent first. Reverting a debit restores the original credit's `remainingAmount`. Expiry subtracts exactly the remaining amount.
13. **Deferred-terms aggregation.** One deferred due date per order. The earliest date wins. Due-on-fulfillment beats dates. Deposits are summed.
14. **Separate billing grain from delivery grain.**
    - Prepaid: one order, many scheduled fulfillment orders.
    - Pay-per-delivery: one order per billing attempt.
    - At most one successful charge per billing cycle, and only within 24 hours of the expected date.
15. **Reconcile changes to what was agreed with sales agreements.** Returns and exchanges enter agreements only when processed. Return cancel reverses its sales. Exchanges stay on the original order.
16. **Gateway-opaque data is quarantined.** `receiptJson` is not a contract. `errorCode` is the normalised, provider-agnostic error.

---

## 9. Class-level questions for Sharrwah (provider-agnostic)

1. **[information]** Which record is authoritative for each of these: what was agreed (append-only sales), what a provider attempted or settled (attempts with kind and status), what moved money (immutable tender), and what a processor or wallet credited net of fees? How are differences between them stored as explicit records (adjustments, discrepancies, rounding) rather than overwritten?
2. **[information]** Is "amount outstanding" one signed quantity computed as agreed total minus net received, so that an edit, exchange or partial refund can make the merchant owe the buyer? Or are there two fields that can disagree?
3. **[lifecycle]** Is the obligation's timing (due now, deposit, net-N, on receipt, on delivery, fixed date) a separate entity from the obligation's amount? Can an order hold several timed instalments, each with its own "to be authorized" and "to be captured" balances?
4. **[lifecycle]** For each payment arrangement (card, wallet, cash on delivery, bank or remittance transfer, agent cash-in, store credit, gift card), which steps exist: reserve, settle, release, reverse? Which of them can be partial, repeated, or expire? Which record captures each step?
5. **[rules]** What hard guards apply? Capture ≤ authorization; refund ≤ captured unless an explicit over-refund is allowed; manual payment ≤ outstanding; currency must match presentment. Which guards are explicit flags that need a reason?
6. **[rules]** How do multiple deferred-payment lines in one cart combine into a single due date and a single deposit? What wins when policies conflict (earliest date, on-delivery precedence, sum of deposits)?
7. **[actors]** Who is allowed to initiate each money movement (buyer at checkout, staff with a named permission, an app holding a scoped mandate, a scheduler)? Is the actor (staff member, app, device, location) stamped on every agreement and transaction?
8. **[actors]** Which legal entity is the seller of record for each order? Which entity's processor account and payout does the money flow to? If a third party acts as merchant of record for tax, how is that recorded without changing the order's ledgers?
9. **[events]** Which money operations are asynchronous (provider callbacks, 3-D Secure or OTP challenges, agent confirmations, bank transfers)? What job or reference does the caller poll? Which events fire only after the buyer completes an action?
10. **[events]** How is every money-creating request made idempotent (client keys, retry-safe commits)? How are retries of one logical payment grouped so that success metrics and dunning don't double-count?
11. **[variability]** How are amounts represented across currencies: shop versus presentment versus settlement? Is FX gain or loss recorded per transaction? What is the redemption policy for stored value issued in one currency and spent in another? This matters in Yemen, where YER exchange rates differ by region, and USD and SAR circulate alongside YER.
12. **[variability]** How is cash rounding to available denominations recorded, both on payments and refunds, without distorting the agreed total?
13. **[lifecycle]** What is the permission object behind a later charge (mandate, credential on file, standing order, wallet token)? How is it scoped to a resource (order, draft, subscription), revoked with a reason, auto-revoked after repeated failures, and replaced via a secure buyer link?
14. **[rules]** When an edit, return or exchange changes what was agreed after payment, does the system add a new agreement with reversal, update and adjustment lines? How does it then route the net difference: refund to the original method, refund to store credit, an invoice for the balance, or holding fulfillment until paid?
15. **[information]** Are stored-value instruments (store credit, gift cards, wallet top-ups) separate ledgers with balance-after, expiry, debit-revert and FIFO-by-expiry? Is their link back to the originating order payment kept?
16. **[scope]** Which payment arrangements are allowed with which purchase options (subscriptions, pre-order, try-before-you-buy, B2B terms, draft or quote orders, point of sale)? Is "pay now only" a stored flag or derived from the absence of terms and review?
17. **[quality]** How does reconciliation work across ledgers when a direct foreign key is missing (for example online exchange payments matched by amount and timestamp)? How does Sharrwah avoid creating such gaps?
18. **[events]** How are processor-side events that the merchant did not initiate (disputes, chargeback holds and releases, reserves, fees, lending remittances, payout failures and withdrawals) represented? How are they linked back to orders?
19. **[lifecycle]** For cash handled by staff or couriers, what is the session model (open with a count, adjust with a reason, mid-shift count, close with expected versus counted)? What is frozen once a session closes? This matters for cash on delivery and courier remittance.
20. **[extension]** Which parts of the money lifecycle can an extension own (scheduling deferred charges, dunning, trial periods, contract pricing per cycle), and which must the platform own (initial collection, vaulting, inventory, tax)? How do extensions read and write shared records instead of shadow copies?
21. **[quality]** How are test transactions isolated so they can never become real, and real ones never become test, across every ledger?
22. **[variability]** How are imported historical orders recorded with backdated, pre-settled transactions and an overridable financial status? What later operation is allowed to recompute that status?
23. **[information]** Is the order's financial status a stored state or a projection? If it is a projection, what is the exact rule from (agreed total, received, capturable, refunded, pending, expired) to the displayed status?
24. **[scope]** How are recurring commitments modelled? A contract detached from the plan it came from, billing cycles with per-cycle overrides and skips, one order per successful charge (or one order holding all prepaid cycles), and combining several contracts into one order.

