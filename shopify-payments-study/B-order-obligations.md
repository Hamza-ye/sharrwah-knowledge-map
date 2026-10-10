# B — Order-side obligations, arrangements and money outcomes (Shopify)

Reader B. Slice: orders, drafts, B2B, returns, gift cards, store credit, purchase options, multi-currency, as reflected on the order.

**How to read the citations**
- `MO/` = `help/manual/fulfillment/managing-orders/`
- `B2B/` = `help/manual/b2b/checkout-and-orders/`
- `GC/` = `help/manual/products/gift-card-products/`
- `PO/` = `help/manual/products/purchase-options/`
- `IP/` = `help/manual/international/pricing/`
- `SC` = `help/manual/customers/store-credit.md`
- `[S:Type]` = a type in `schema/admin-2026-10-money.md`.
- `[fetched]` = a page that was missing from the corpus and was fetched read-only from help.shopify.com. Two pages are like this: `MO/returns/processing-returns` and `MO/managing-order-details`.
- A few pages outside my slice are cited by full path where the docs I was reading relied on them.
- The schema extract lists field names without their descriptions. Where I give what an Order total means, I took it from the Shopify API reference as I remember it, and I mark it **API-recall**.

---

## 0. The model in one paragraph

The Shopify order is not a single "amount due". It is four things that are kept apart and then compared:

1. **What was agreed.** An append-only ledger of `SalesAgreement` records (`OrderAgreement`, `OrderEditAgreement`, `RefundAgreement`, `ReturnAgreement`). Each one carries a `reason` of type `OrderActionType` (ORDER / ORDER_EDIT / REFUND / RETURN) and itemised `Sale` records typed by `SaleLineType`: PRODUCT, TIP, GIFT_CARD, SHIPPING, DUTY, ADDITIONAL_FEE, FEE, ADJUSTMENT [S:SalesAgreement, S:Sale, S:SaleLineType]. Shopify "creates a sales agreement whenever an order is placed, edited, or refunded" [S:SalesAgreement].
2. **What money moved.** An `OrderTransaction` ledger. Each transaction has a `kind` (AUTHORIZATION, CAPTURE, SALE, VOID, REFUND, CHANGE, EMV_AUTHORIZATION, SUGGESTED_REFUND) and a `status` (SUCCESS, FAILURE, PENDING, ERROR, AWAITING_RESPONSE, UNKNOWN). It can have a `parentTransaction`, and it records its gateway, fees, settlement currency and rate [S:OrderTransaction, S:OrderTransactionKind, S:OrderTransactionStatus].
3. **When it is due.** `PaymentTerms` holding `PaymentSchedule`s. Each schedule has `amount`, `balanceDue`, `issuedAt`, `dueAt`, `completedAt` and `due` [S:PaymentTerms, S:PaymentSchedule].
4. **Derived balances and a display status.** The balances are `totalOutstandingSet`, `totalReceivedSet`, `netPaymentSet`, `totalCapturableSet`, `totalRefundedSet` and `refundDiscrepancySet`. The display status is `displayFinancialStatus` [S:Order].

Stored value (gift cards, store credit) lives in separate ledger accounts. They connect to the order through transactions: `StoreCreditAccountTransactionOrigin` = `OrderTransaction` [S:StoreCreditAccountTransactionOrigin]. Almost every money field is a `MoneyBag` with `shopMoney` and `presentmentMoney` [S:MoneyBag].

The docs consistently make a change to *what is owed* a separate step from *settling* it:
- After an edit, "The refund isn't complete when you edit an order… You need to refund your customer after you update the order" (`MO/editing-orders/products.md`).
- A discount saved on the refund page "will display a refund owed to the customer" even if no refund is issued (`MO/refunding-orders.md`).

---

## 1. What creates or changes an obligation

### 1.1 Order placement (checkout)
- Placing an order creates the order and an `OrderAgreement` [S:OrderAgreement]. How much becomes "paid" at that moment depends on the capture setting:
  - "Automatically at checkout" (the default)
  - "Automatically when order is fulfilled"
  - "Automatically capture per fulfillment (Shopify Plus plan only)"
  - "Manually"

  (`help/manual/payments/payment-authorization.md`). Under the last three the order sits at **Authorized** (`MO/order-status.md`).
- The order is created as **Payment pending** in three cases (`MO/order-status.md`):
  - The customer paid with a non-card method. The provider "has started processing, but needs time… inventory is reserved for the order, but payment isn't guaranteed".
  - The merchant ticked "Payment due later" and set terms.
  - A "manual payment method, such as Cash On Delivery" was used.
- Product data on the order is snapshotted: "This information is locked when the order is created" (titles, prices, compare-at prices, weights, variants) (`MO/managing-order-details` [fetched]).
- Return rules are also effectively snapshotted: "Changes to your return rules apply only to future orders" (`MO/returns/return-rules.md`).

### 1.2 Draft order → invoice → order
- A draft is a *proposal* and owes nothing yet. `DraftOrderStatus` is OPEN, INVOICE_SENT or COMPLETED [S:DraftOrderStatus]. "When a draft order is paid, it becomes a regular order" (`MO/create-orders.md`).
- There are three ways to complete it (`MO/create-orders/get-paid.md`):
  - The customer pays through an invoice or checkout link, after which the order "is automatically marked as **Paid**" (`MO/create-orders/send-draft.md`).
  - **Credit card** entry (Shopify Payments only).
  - **Mark as paid**.

  In the API this is `draftOrderComplete(id, paymentPending, paymentGatewayId, sourceName)`. `paymentPending` lets a draft become an order that still owes money [S:MUTATIONS].
- Price lock:
  - A draft can **Lock product pricing**, so prices don't change when catalog prices change (up or down) (`MO/create-orders/create-draft.md`).
  - Invoices and links default to locked: "the pricing is set to lock by default unless you manually set it to be unlocked" (`MO/create-orders/send-draft.md`).
  - Bundles can't be locked (`MO/create-orders/create-draft.md`).
- Staleness rule: if a product or shipping rate changed, "you must resolve the issues and apply changes before payment can be captured" (**New updates to this draft order**). Price-locked items are exempt (`MO/create-orders/get-paid.md`).
- Price overrides:
  - A **custom price** replaces the listed price, and no reduction is shown. A **discount** shows as a reduction (`MO/create-orders/create-draft.md`).
  - At most 5 discount codes per order. Shipping and BXGY codes aren't supported on drafts. Customer-entered codes at checkout are off by default and must be enabled per draft. A deactivated or ineligible discount blocks completion until it is removed (`MO/create-orders/discounts.md`).
- Validation: unmet checkout rules show "Business rules that apply to this draft order". The merchant can choose **Ignore and create order**, or enable "Ignore all checkout rules" on the invoice (`MO/create-orders/create-draft.md`).
- Lifecycle: drafts created on or after 2025-04-01 are auto-deleted after 1 year of inactivity, and any edit resets the timer (`MO/create-orders.md`). "Deleting a completed draft order doesn't delete the order" (`MO/create-orders/create-draft.md`).
- Schema totals on drafts: `amountDueNowSet`, `amountDueLaterSet`, `deposit: DepositConfiguration` (`DepositPercentage.percentage`), `paymentTerms`, `presentmentCurrencyCode`, `purchasingEntity`, `poNumber`, `reserveInventoryUntil` [S:DraftOrder].

### 1.3 Payment terms (deferred obligation)
- The four term types (`MO/payments/deferred-payments.md`, `MO/create-orders/create-draft.md`):
  - **Due on receipt**: due "on the date that you send the invoice".
  - **Due on fulfillment**: due "on the date that you fulfill all items".
  - **Net term**: net 7, 15, 30, 45, 60 or 90, "from the issue date".
  - **Fixed term**: a specific date.
- The schema mirrors these as `PaymentTermsType` RECEIPT / NET / FIXED / FULFILLMENT / UNKNOWN. Terms are created from a `PaymentTermsTemplate` (`dueInDays`), optionally with explicit `PaymentScheduleInput {issuedAt, dueAt}` [S:PaymentTermsType, S:PaymentTermsTemplate, S:PaymentTermsCreateInput].
- B2B lists the terms differently: "No payment terms" (the default), Net, Due on fulfillment, and Fixed date. Fixed date is only allowed on individual drafts, and the doc says "All terms start from the day the order is placed" (`B2B/payment-terms.md`). See §9 for how this conflicts with "issue date".
- Terms can be added, edited or removed on an existing order only while it is **Payment pending** (`MO/payments/deferred-payments.md`).
- **Due on fulfillment** can be applied after creation only if the order has no fulfillments (`MO/payments/deferred-payments.md`).
- "Payments aren't automatically captured when the payment terms expire" (`B2B/payment-terms.md`).

### 1.4 Deposits
- Plan and basis:
  - Shopify Plus only.
  - A percentage, set on a company, a company location ("Require deposit on orders created at checkout") or a draft order (`B2B/payment-terms.md`, `MO/create-orders/create-draft.md`).
  - "The deposit is a percentage of the order subtotal only—it doesn't include taxes or shipping… The remaining balance, including taxes and shipping, is paid later" (`B2B/draft-orders.md`).
- Status effects (`B2B/payment-terms.md`):
  - Captured deposit → **Partially paid**.
  - Deposit paid by a manual method → **Payment pending** until it is recorded.
- Allowed tenders:
  - "Store credit can't be used towards a deposit. Deposits are treated as upfront commitments", but store credit *can* pay a terms invoice (`B2B/store-credit.md`).
  - Deposits can be paid by credit card or a manual method (`B2B/payment-terms.md`).
- Purchase-option deposits (pre-orders) work differently: deposits on multiple items "are combined and charged at checkout" (`PO/pre-orders/setup.md`). In the schema these are `SellingPlanCheckoutCharge` (PERCENTAGE or PRICE) [S:SellingPlanCheckoutChargeType].

### 1.5 B2B checkout-to-draft ("Submit for approval")
- With **Submit all orders as drafts for review**, checkout shows **Submit for approval**. "No payment is collected at checkout". The order lands in Drafts with prices locked and "aren't complete until you click **Create order** or the customer submits payment after you send them an invoice" (`B2B/checkout-settings.md`, `B2B/draft-orders.md`).
- Payment handling under review:
  - A deposit is shown at checkout but "not captured immediately" (`B2B/payment-terms.md`).
  - A vaulted card or bank account chosen at checkout is labelled **Selected at checkout** and is charged after confirmation (`B2B/vaulted-cards.md`, `B2B/vaulted-bank-accounts.md`).
  - Manual methods only become available after review, on a new invoice (`B2B/checkout-settings.md`).
- Schema: `BuyerExperienceConfiguration {checkoutToDraft, deposit, editableShippingAddress, payNowOnly, paymentTermsTemplate}` [S:BuyerExperienceConfiguration].
- You can make only some orders go to review by using the Payment Customization Function (`B2B/draft-orders.md`).

### 1.6 Purchase options (selling plans)
- The three options are "subscriptions, preorders, and try-before-you-buy" (`PO/purchase-options.md`). `SellingPlanCategory` is PRE_ORDER, SUBSCRIPTION, TRY_BEFORE_YOU_BUY or OTHER [S:SellingPlanCategory].
- **Pre-order**:
  - "collect full, partial, or no payment at the time the customer places their order. Collecting payments stores your customer's payment method" (`PO/pre-orders.md`).
  - When the remaining balance is charged is set by `SellingPlanFixedBillingPolicy.remainingBalanceChargeTrigger`: NO_REMAINING_BALANCE / EXACT_TIME / TIME_AFTER_CHECKOUT / ON_FULFILLMENT [S:SellingPlanRemainingBalanceChargeTrigger]. Inventory is reserved ON_SALE or ON_FULFILLMENT [S:SellingPlanReserve].
  - Mixed carts: "The earliest due date applies to all products"; "due on fulfillment … takes priority over specific dates"; deposits are combined (`PO/pre-orders/setup.md`).
  - The merchant can collect the deferred balance early, from the **Partially paid** card ("charge the stored card"), but is warned about chargebacks (`PO/pre-orders/manage-pre-orders.md`).
  - Legal duties: there must be a reasonable basis for the ship date (30 days if none is stated), and a revised date plus a right to cancel or refund if it is missed (`PO/pre-orders/setup.md`).
  - Requires Shopify Payments or PayPal Express (`PO/pre-orders.md`).
- **Try before you buy**:
  - Ship first and charge later. Optionally "create a full authorization on your customer's payment method before fulfilling" (`PO/try-before-you-buy.md`).
  - Deferred payments are all due on the soonest due date (`PO/try-before-you-buy/setup.md`).
  - Requires Shopify Payments, Adyen or Stripe.
- **Subscriptions**:
  - Two billing models: "Pay-as-you-go" and "Pre-paid" (`PO/subscriptions/model-types.md`).
  - **Pay-per-delivery** creates a new order every interval. **Prepaid** is one order paid as a lump sum with **Scheduled** fulfillments (`PO/subscriptions/manage-subscriptions/manage-subscription-orders.md`).
  - Customers are billed "the day after the subscription is due at 10:00 am in your store's local time" (`PO/subscriptions/considerations.md`).
  - A `SubscriptionContract` (billingPolicy, `customerPaymentMethod`, `currencyCode`, `nextBillingDate`, status ACTIVE / PAUSED / CANCELLED / EXPIRED / FAILED) generates `SubscriptionBillingAttempt`s. Attempts are idempotent ("use idempotency keys to avoid duplicate order creation"); their state is pending, success (→ order), failed or action-required (payment challenge) [S:SubscriptionContract, S:SubscriptionBillingAttempt].
  - `SubscriptionBillingAttemptPaymentProcessingPolicy` includes `SKIP_PAYMENT_AND_CREATE_UNPAID_ORDER` [S:…]. Inference: an obligation can be materialised before it is paid.
  - Retry policy: the merchant sets the number of retries, the days between them, and the final action (skip, pause or cancel) (`PO/subscriptions/shopify-subscriptions/manage-subscriptions/manage-app-settings.md`).
  - Customers get an email 3 days before each charge (`…/shopify-subscriptions/customer-experience.md`).
  - Gift cards and Scripts apply only to the first payment (`PO/subscriptions/considerations.md`). Store credit pays only the initial purchase (`SC`).
  - A discount code is snapshotted into the contract and survives deactivation of the code (`PO/subscriptions/manage-subscriptions/subscription-discounts.md`).
  - Subscriptions can't be put on draft orders (`PO/subscriptions/considerations.md`).
  - Purchase options can't be combined on one product (`PO/pre-orders/setup.md`).

### 1.7 Order edits
- Edits are allowed on unfulfilled items only. Discounts can be added to fulfilled items too (`MO/editing-orders/considerations.md`).
- "The order total updates … and the order displays whether a refund is owed to the customer or a balance is owed to you" (`MO/editing-orders/considerations.md`).
- Flow-of-funds table (`MO/editing-orders/products.md`):
  - Total decreases → issue a refund (a separate step).
  - Total increases → "collect payment by sending an invoice … or … accept payment".
  - Zero-price custom item → no action.
- Each edit produces an `OrderEditAgreement`. `OrderPaymentCollectionDetails {additionalPaymentCollectionUrl, vaultedPaymentMethods}` is "for an order that requires additional payment following an edit" [S:OrderEditAgreement, S:OrderPaymentCollectionDetails].
- What is *not* recalculated on edit (`MO/editing-orders/considerations.md`):
  - Shipping rates. A custom shipping charge can be added.
  - Some discounts. Only order-wide percentage discounts, and multi-use fixed-amount product or collection codes, are recalculated.
  - Duties and taxes stay **Duties (original)** and **Taxes (original)** until **Update order** is clicked.
- Shipping-address change (`MO/editing-orders/customer-details.md`):
  - Taxes are recalculated (unfulfilled orders only). The Summary shows "the difference to collect or refund".
  - If tax goes up, the merchant can invoice it or "track it on the order details page to collect it later". If it goes down, the merchant refunds it.
- Orders that can't be edited (`MO/editing-orders/considerations.md`):
  - Imported orders (only the creating app can edit them).
  - Shop Pay Installments orders.
  - Local delivery.
  - Orders with fulfilled items when duties are charged.
  - Possibly **Payment pending** orders.
  - Bundles can't be added.
- Prepaid subscription orders allow no quantity edits. Pay-per-delivery orders do allow them. Editing never changes the contract (`PO/subscriptions/manage-subscriptions/manage-subscription-orders.md`). On pre-order orders you can't add a new pre-order item (`PO/pre-orders/manage-pre-orders.md`).

### 1.8 Cancellation
- Cancellation means "halting order processing". The refund choices are "Original payment method" (default), "Store credit" (with an expiry option) or "Later" (`MO/canceling-orders.md`).
- Status effects: uncaptured → **Voided**; fully refunded → **Refunded**; a later partial refund → **Partially refunded** (`MO/canceling-orders.md`).
- "After an order is partially fulfilled, you can't cancel it."
- "Fulfilled but payment isn't collected: Canceling an order prevents you from collecting payment."
- Schema: `orderCancel(refund, refundMethod{originalPaymentMethodsRefund, storeCreditRefund{expiresAt}}, restock, reason, …)`.
  - Reasons: CUSTOMER / DECLINED / FRAUD / INVENTORY / STAFF / OTHER.
  - Errors include `NO_REFUND_TO_STORE_CREDIT_PERMISSION`, `STORE_CREDIT_REFUND_MISSING_CUSTOMER` and `STORE_CREDIT_REFUND_B2B_NOT_SUPPORTED` [S:OrderCancelRefundMethodInput, S:OrderCancelReason, S:OrderCancelUserErrorCode].
- A customer **cancellation request** does not change the order on its own. It is resolved through the refund flow (**Remove items**) or declined (`MO/returns/self-serve-returns/management.md`).

### 1.9 Returns and exchanges (obligation in either direction)
- "Return fees and exchange items are applied against returned items to determine whether a refund is due or payment needs to be collected" (`MO/returns/creating-returns.md`).
- The three outcomes:
  - The merchant owes money → refund now or later.
  - The customer owes money → send an invoice at processing, or capture or mark paid afterwards.
  - Even exchange → "money paid for the returning items is applied to the new items".
- Fees (`MO/returns/return-rules.md`, `MO/returns/processing-returns` [fetched]):
  - **Restocking fee**: a percentage of the return. It can be edited per return or per item, and is "calculated by how many items you choose to process".
  - **Return shipping**: free, a flat rate "charged one time per return", or a customer-bought label. It is "applied the first time you process the return".
  - Restocking fees are only shown on returns of fulfilled items.
- Tax on fees: from 2026-10-23, return shipping fees on US-shipped orders are taxed under Shopify Tax or Tax Platform. Restocking fees are never taxed (`MO/returns/return-rules.md`).
- Partial processing "might require payment, even if processing everything would result in a refund" (`MO/returns/creating-returns.md`).
- Exchange items:
  - They are put on hold while payment is awaited, unless **Release fulfillment** is used ([fetched] processing-returns).
  - Their inventory isn't reserved until the return is processed.
  - They can't be added on orders with duties.
  - Order-level discounts can't be applied to them (`MO/returns/creating-returns.md`).
- Removing return items "adjusts the order balance". A return can be cancelled only if it is not refunded, not restocked, open, has no label, and its fulfillment isn't cancelled ([fetched] processing-returns).
- Schema:
  - `Return.suggestedFinancialOutcome` and `suggestedRefund` [S:Return].
  - `returnProcess(…financialTransfer{issueRefund{orderTransactions, refundMethods, allowOverRefunding}}, refundDuties, refundShipping, tipLineId)` [S:ReturnProcessInput].
  - `SaleActionType` RETURN [S:SaleActionType].

### 1.10 Other obligation sources
- **Tips**:
  - Added at checkout as a percentage of the subtotal "before taxes and shipping".
  - Capped at 100% of the order total and at $1000 USD.
  - Not allowed with selling plans or Shop Pay Installments.
  - Refunding a tip is a manual amount entry (`help/manual/checkout-settings/tips.md`).
  - Schema: `TipSale`, `Order.totalTipReceivedSet` [S:TipSale, S:Order].
- **Duties and additional fees**: `DutySale`, `AdditionalFeeSale`, `currentTotalDutiesSet` vs `originalTotalDutiesSet` [S:Order]. Refund toggles exist for "Duties and import taxes on refunded items" and "Additional fees: Customs clearance" (`MO/refunding-orders.md`).
- **Gift card sale**:
  - A liability: "Gift cards can create a liability to provide future sales" (`GC/issue-gift-card.md`).
  - The card is *created when the gift-card line is fulfilled*. Auto-fulfilment happens "when an order is paid", except on medium or high-risk orders (`GC/modify-gift-card-settings.md`, `GC/overview.md`).
  - Schema: `GiftCardSale`, `GiftCard.order`, `GiftCard.lineItem` [S:GiftCardSale, S:GiftCard].
- **Store credit issuance**: an adjustment, or a refund-to-store-credit (`SC`) [S:StoreCreditSystemEvent].
- **Chargebacks**: after a partial refund, "the customer can still initiate a chargeback for the full value … you're debited for the full order amount" (`MO/refunding-orders.md`).

---

## 2. Arrangements on the order

### 2.1 Collecting an outstanding amount after checkout
| Arrangement | Rules | Source |
|---|---|---|
| **Send invoice** (checkout link) | For **Payment pending** orders and drafts. The customer picks the method. After an edit, accelerated checkouts (such as Apple Pay) aren't offered. No invoice is possible for a draft in a non-store currency with terms. | `MO/payments/deferred-payments.md`, `MO/editing-orders/considerations.md`, `MO/create-orders/create-draft.md` |
| **Payment request per fulfillment** | Only for "Due on fulfillment" orders. Each request covers line items plus tax; "Shipping, fees, and duties are included with the final fulfillment". Item discounts follow their items; "order-level discounts … divided evenly across each fulfillment"; shipping discounts go on the final request. The deposit is applied to the first request. Not available with fulfillment-based auto-capture. Customers can pay a single request only if it was sent. | `MO/payments/deferred-payments.md` |
| **Pay by credit card / Enter credit card** (merchant-keyed) | Shopify Payments only, verification required. | `MO/create-orders/get-paid.md`, `MO/payments/deferred-payments.md` |
| **Mark as paid** | "The received amount isn't captured again by your payment provider". On drafts, **Amount received** is editable (FX-converted at the live rate). Can be blocked while a provider payment is pending. Schema: `orderMarkAsPaid`, `Order.canMarkAsPaid`. | `MO/create-orders/get-paid.md`, `MO/payments/pending-payments.md`, [S:Order] |
| **Record payment** (manual, partial) | Plus. Fixed or percentage amount, choice of manual method → **Partially paid**. Schema: `orderCreateManualPayment(amount, paymentMethodName, processedAt)`, errors `AMOUNT_EXCEEDS_BALANCE`, `CURRENCY_MISMATCH`. | `help/manual/payments/partial-payments.md`, [S:OrderCreateManualPaymentOrderCreateManualPaymentErrorCode] |
| **Charge vaulted card / bank account** | B2B, Shopify Payments; bank accounts US only. "By vaulting … gives permission for that card to be used for the current order and future orders". Not auto-charged at term expiry. Automate with Flow trigger **Payment schedule is due** → action **Charge vaulted payment for B2B order**. Deleted vaults can still be charged for existing pending orders. Schema: `orderCreateMandatePayment(mandateId, paymentScheduleId, amount, autoCapture, idempotencyKey)`, `paymentScheduleCapture`, `PaymentMandate`, `MandateResourceType` (CREDENTIAL_ON_FILE / CHECKOUT / DRAFT_ORDER / ORDER / SUBSCRIPTIONS). | `B2B/vaulted-cards.md`, `B2B/vaulted-bank-accounts.md`, [S:MUTATIONS, S:MandateResourceType] |
| **Customer "Pay now"** | B2B customer account, any time before the due date and still allowed after it (the order shows **Overdue**). | `B2B/payment-terms.md` |
| **Payment reminders** | Up to five, on the due date or up to 30 days after. Not for subscriptions, pre-orders or TBYB. Schema: `paymentReminderSend(paymentScheduleId)`. | `MO/payments/deferred-payments.md`, [S:MUTATIONS] |
| **Capture authorized funds** | Full or partial. Multiple partial captures "up to the authorized amount" if the provider supports it (Plus + Shopify Payments, Amex / Visa / Discover / Mastercard). "Transaction fees apply to each capture". Bulk capture always captures the full amount. Schema: `orderCapture{parentTransactionId, amount, currency, finalCapture}`. | `MO/payments/capturing-payments.md`, [S:OrderCaptureInput] |
| **Collect a deferred balance early** | Pre-order and TBYB: from the **Partially paid** card, charge the stored card or send an invoice. | `PO/pre-orders/manage-pre-orders.md`, `PO/try-before-you-buy/manage-try-before-you-buy.md` |

The gap between authorized and owed: "It isn't possible to collect more money than the value that was initially authorized… edit the order and send an invoice for the difference" (`MO/payments/capturing-payments.md`).

### 2.2 Satisfying a refund obligation
- **Refund method** choices are **Original payment**, **Store credit**, or **Original payment & store credit**. Store credit can be given an expiry (`MO/returns/processing-returns` [fetched], `MO/refunding-orders.md`).
- **Split across tenders**: "a suggested split for how the refund applies to each transaction is displayed. If the order includes a gift card, then the suggestion tries to refund the gift card in full first. You can adjust … up to the amount available for each payment method" (`MO/refunding-orders.md`). Schema: `SuggestedRefund.suggestedTransactions`, `suggestedRefundMethods` (`SuggestedStoreCreditRefund`), `maximumRefundableSet` [S:SuggestedRefund].
- **Later** is allowed after cancelling or processing a return. The outstanding balance banner then pre-fills the refund amount ([fetched] processing-returns, `MO/canceling-orders.md`).
- **To a gift card**:
  - The original card is reloaded automatically.
  - Reloading during return or exchange only works if the original transaction was via Shopify Payments; otherwise a new card is issued.
  - An expired card must have its expiry extended first.
  - A deactivated card can't take a refund; issue a new card or refund to store credit instead (`GC/manage-purchased-gift-cards.md`).
- **Cash, manual or third-party**: "Refunds use the same payment method that was used to pay for the order. You can't issue a refund to a different card or bank account" (`IP/refunds.md`). If the customer has lost access, "they need to contact the bank" (`MO/refunding-orders.md`). Inference: for COD or manual gateways the refund is recorded on the order and the cash moves outside Shopify. The corpus slice has no explicit "cash refund" flow.
- Refunds can't be reversed. "If you initiate a refund by mistake, then you can create a new draft order and collect the payment again" (`MO/refunding-orders.md`).

---

## 3. Financial status

### 3.1 Statuses and what produces them (`MO/order-status.md` unless noted)
| Status (UI) | Produced by |
|---|---|
| **Pending / Payment pending** | An asynchronous non-card method in progress; "Payment due later" + terms; a manual method such as COD; a deposit paid by a manual method (`B2B/payment-terms.md`). |
| **Authorized** | Manual or at-fulfillment capture after a successful authorization. "Displayed only if you capture payments manually". |
| **Due** (filter or badge) | Terms on a **Payment pending** order, not captured by the due date (includes due today). Docs elsewhere say the order "becomes **Overdue**" (`MO/payments/deferred-payments.md`). |
| **Expiring** (badge, not a status) | Two days before the authorization deadline. |
| **Expired** | An authorization was not captured in time, or an alternative provider "unable to process the payment" (the pending expiry is "typically a week", `MO/payments/pending-payments.md`). |
| **Partially paid** | A manual partial capture; a captured deposit; a recorded partial payment (`B2B/payment-terms.md`, `help/manual/payments/partial-payments.md`); pre-order or TBYB with a balance still to come (`PO/pre-orders/manage-pre-orders.md`). |
| **Paid** | Captured (automatically or manually), or marked as paid. |
| **Partially refunded** | Refunded less than "the full amount that the customer paid". |
| **Refunded** | The full amount the customer paid was returned. |
| **Voided** | The authorization was released before capture. Cancelling an uncaptured order produces this. "An order can remain **Open** while its payment status is **Voided**". |
| **Unpaid** (aggregate) | Authorized + Pending + Expired + Partially paid. |

- Schema enums: `OrderDisplayFinancialStatus` = PENDING, AUTHORIZED, PARTIALLY_PAID, PARTIALLY_REFUNDED, VOIDED, PAID, REFUNDED, EXPIRED. There is no DUE or OVERDUE value; those come from `PaymentTerms.due` / `overdue` and `PaymentSchedule.due` [S:OrderDisplayFinancialStatus, S:PaymentTerms].
- `OrderCreateFinancialStatus` (the same values) can be set only at creation, for imports [S:OrderCreateFinancialStatus].
- Order-level booleans: `fullyPaid`, `unpaid`, `capturable`, `canMarkAsPaid`, `refundable`, `restockable` [S:Order].
- **Inference**: the display status is a lossy projection of the ledger. Payment status sits on a separate axis from order status (Open / Archived / Canceled) and from fulfillment and return statuses.

### 3.2 Balances (API-recall definitions; field names from [S:Order])
- `totalPriceSet`: the total "before returns". `originalTotalPriceSet`: the total at creation. `currentTotalPriceSet`: the total "after returns and edits".
- `totalReceivedSet`: "total amount received from the customer before returns".
- `totalRefundedSet` and `totalRefundedShippingSet`.
- `netPaymentSet` = received − refunded.
- `totalCapturableSet`: "the authorized amount that's uncaptured or undercaptured … isn't adjusted for returns".
- `totalOutstandingSet`: "amount not yet transacted… positive = merchant's favor (payment from customer), negative = customer's favor (refund owed)". **Inference**: this is the single signed figure behind both the "amount to collect" and "refund owed" banners after edits and returns.
- `refundDiscrepancySet`: the difference between suggested and actual refunds (positive = merchant's favor).
- Per transaction: `maximumRefundable`, `totalUnsettledSet`, `manuallyCapturable`, `multiCapturable`, `authorizationExpiresAt` [S:OrderTransaction].

### 3.3 How edits and refunds interact with captured money
- An increase after capture is never added to the existing authorization. It becomes a new collection: an invoice, or "collect payment" (`MO/payments/capturing-payments.md`).
- Under capture-at-fulfillment, the merchant can **Capture payment early** (`MO/payments/capturing-payments.md`).
- Reports: an edit made on a later day "displays as a separate order in your reports" (`MO/editing-orders/considerations.md`). **Inference**: reporting is dated by agreement (`SalesAgreement.happenedAt`), not by order.

---

## 4. Refund and return money logic

- **What a refund is made of** (`MO/refunding-orders.md`):
  - Line quantities (a quantity of 0 isn't refunded).
  - **Restock items** (only when inventory is tracked).
  - **Refund shipping**, capped at the amount charged per shipping line. It can't be refunded if an order-level free-shipping discount was applied.
  - Duties and customs fees toggles.
  - An editable **Refund amount**, "to deduct a restocking fee".
  - Schema: `RefundInput{refundLineItems, shipping, refundDuties, transactions, refundMethods, discrepancyReason, allowOverRefunding, currency}`. `Refund` contains `refundLineItems` (price, subtotal, totalTax, restockType), `refundShippingLines` (subtotal, tax), `duties`, `orderAdjustments` and `transactions` [S:RefundInput, S:Refund, S:RefundLineItem, S:RefundShippingLine].
- **Discrepancy and adjustment**:
  - If the refund differs from the computed one, an `OrderAdjustment{amountSet, taxAmountSet, reason}` "accounts for the difference between a calculated and actual refund amount".
  - Reasons: RESTOCK, DAMAGE, CUSTOMER, REFUND_DISCREPANCY, FULL_RETURN_BALANCING_ADJUSTMENT, PENDING_REFUND_DISCREPANCY [S:OrderAdjustment, S:OrderAdjustmentDiscrepancyReason].
  - Sales side: an `ADJUSTMENT` sale "represents the difference between the original total value of all line items that were refunded, and the actual amount refunded", for example restocking fees and goodwill [S:SaleLineType].
- **Rounding and allocation invariant**: money is held in the smallest currency unit. Remainders are allocated "one at a time, starting with the first line item". "The allocation … is immutable… never reallocated" [S:Sale].
- **Refund-page discount**: it "applies to the full quantity of that item" and is saved on **Save** "whether or not you complete the refund", creating an outstanding refund owed (`MO/refunding-orders.md`).
- **Ceiling**: partial refunds can be issued "until you've reached the total available to refund, which is the original amount of the order" (`MO/refunding-orders.md`).
- **Over-refund**:
  - Only for an order previously refunded to store credit.
  - Only with Shopify Payments.
  - Needs a permission.
  - "doesn't reverse the store credit refund". The merchant must debit store credit manually.
  - Schema: `allowOverRefunding` (`MO/refunding-orders.md`, `SC`, [S:RefundInput]).
- **Lock after store credit**: once store credit has been refunded, "the original payment method is locked on the refund screen, limiting the refundable amount (for example, to shipping costs only)" (`MO/refunding-orders.md`).
- **Returns versus refunds**:
  - Returns are for fulfilled, not-yet-refunded items only. "You can't create a return after a refund has been issued".
  - Return reasons are recorded only through returns. "Reason for refund" is just a note.
  - Refunding an unfulfilled item removes it from fulfilment (`MO/refunding-orders.md`, `MO/returns/creating-returns.md`).
- **Fees on refunds** (`MO/refunding-orders.md`, `IP/fees.md`):
  - Shopify Payments: card fees are not returned.
  - Third-party gateway in a country where Shopify Payments is available: transaction fees are not returned.
  - Where Shopify Payments isn't available: a pro-rata transaction-fee credit, and only for refunds made in the admin.
  - Currency conversion fees are never returned. No new conversion fee is charged on the refund.
- **Timing**:
  - EU: refunds are due "within 14 days of the cancellation request" (`MO/returns/return-rules.md`).
  - Customer notification is on by default.
  - Shopify sends "Send notification once refund is finalized" ([fetched] processing-returns). Inference: refunds can be asynchronous or pending (see `PENDING_REFUND_DISCREPANCY`).
- **Exchange netting**: an even exchange applies the old payment to the new items. Otherwise there is a refund or a collection (`MO/returns/creating-returns.md`).
- **Bulk-cancel hazard**: "all canceled orders are refunded immediately, including orders that have already been refunded, which can trigger duplicate refund processing" (`MO/canceling-orders.md`).

---

## 5. Stored value

### 5.1 Gift cards (a bearer instrument, a liability, issued per store)
- **Issuance paths**:
  - Sold as a gift card product (created on fulfillment).
  - Created in the admin "without receiving any payment" (promotion, custom denomination after a draft invoice, refund).
  - Created by Flow or an app (`GC/overview.md`, `GC/issue-gift-card.md`). The `Issue method` filter has issued / purchased / app (`GC/manage-purchased-gift-cards.md`).
- **Limits** (`GC/overview.md`, `GC/add-update-gift-card-products.md`):
  - The value must be > 0.
  - Product denominations: ≤ $10,000 USD equivalent, fixed.
  - Admin-created cards: ≤ $2,000 USD equivalent, which Support can raise or lower.
  - Customers can't enter custom amounts.
- **Expiry**: none by default. If enabled, the default is five years. Expiry can be edited per card, even after it has expired (`GC/modify-gift-card-settings.md`, `GC/add-update-gift-card-products.md`).
- **Balance mutability**:
  - "Gift card balances can't be edited directly from the Shopify admin. A balance changes only through redemption, a refund, or a custom integration" (`GC/manage-purchased-gift-cards.md`).
  - Schema: `giftCardCredit` / `giftCardDebit` with errors INSUFFICIENT_FUNDS, MISMATCHING_CURRENCY, GIFT_CARD_LIMIT_EXCEEDED. `GiftCardTransaction` kinds are Credit, Debit and CashOut [S:GiftCardTransaction, S:GiftCardTransactionUserErrorCode].
- **Deactivation** is permanent. A card can't be deleted. Refunding a *purchased* card auto-deactivates it, and the refund need not be the full amount paid. Admin-created cards can't be refunded (`GC/manage-purchased-gift-cards.md`).
- **Redemption** (`GC/redeem-gift-card.md`):
  - Applies to the whole total including tax and shipping.
  - Multi-use, combinable with discount codes, and several cards can be used on one order.
  - Can't buy another gift card.
  - First subscription payment only.
  - Only at the issuing store.
  - If the total changes after the card is applied (for example, final tax), the customer covers the difference with another method.
- **Security**: only the last 4 characters are visible (`maskedCode`, `lastCharacters`) (`GC/manage-purchased-gift-cards.md`, [S:GiftCard]).
- **Discounted sale**: "Customer pays $80 USD … can be redeemed for a value $100 USD" (`GC/discounted-gift-cards.md`). Inference: the liability is the face value, not the price paid.
- **Fees**: for stores created on or after 2025-05-12, gift card and store credit tender is charged third-party transaction fees (`GC/overview.md`, `IP/fees.md`).
- **Currency**:
  - *Store-currency* cards redeem in any currency. They are converted at the *redemption* rate, with no second conversion fee and no rounding, and the remainder is converted back.
  - *Local-currency* cards redeem only in a matching currency unless cross-currency redemption is on. That setting is chosen at creation and is immutable (`GiftCardCrossCurrencyRedemptionStrategy` NONE / MARKET_FX / SPOT_FX).
  - The card's currency "is locked after the card is first sold or used". If the store currency changes, the card may become unredeemable but still show as Active (`IP/gift-cards.md`, [S:GiftCardCrossCurrencyRedemptionStrategy]).
  - FX-drift example: sold for CAD 100 = USD 73, redeemed later when CAD 100 = USD 100 → "you effectively lose $27" (`GC/issue-gift-card.md`).

### 5.2 Store credit (an account ledger owned by a customer or a company location)
- **Owner**: a customer (D2C only) or a **company location** (B2B, shared by all authorized contacts, not transferable) (`SC`, `B2B/store-credit.md`). Schema: `StoreCreditAccount{balance, owner: HasStoreCreditAccounts}` [S:StoreCreditAccount].
- **Ledger**: `StoreCreditAccountCreditTransaction` (`expiresAt`, `remainingAmount`), `…DebitTransaction`, `…DebitRevertTransaction`, `…ExpirationTransaction`. Each records `balanceAfterTransaction`, an `event` of type `StoreCreditSystemEvent` (ADJUSTMENT, ORDER_PAYMENT, ORDER_REFUND, PAYMENT_FAILURE, PAYMENT_RETURNED, ORDER_CANCELLATION, TAX_FINALIZATION, RECURRING_PAYMENT) and an `origin` (an `OrderTransaction`) [S:StoreCreditAccount*].
- **Expiry** (`SC`):
  - Set per issuance; there is no store default.
  - Expires at "end of the day in your store's timezone".
  - Consumption is earliest-expiry-first.
- **Limits**: "less than $15,000 USD on a single customer account" and "less than $10,000 USD on a company location" (`SC`, `B2B/store-credit.md`). Schema error: CREDIT_LIMIT_EXCEEDED.
- **Redemption rules** (`SC`):
  - "Only the full store credit amount can be applied". The customer can't choose a partial amount.
  - Only the balance in the checkout currency is shown.
  - Only available on the online store, POS and Shop.
  - **Not on draft orders or edited orders**. The workaround is to send a checkout link.
  - Requires new customer accounts or Shop Pay.
  - Initial subscription purchase only.
  - In B2B it can't pay deposits.
- **Reporting**: store credit appears "as a payment provider" in payment reports. There are "Outstanding store credit balance" and "Store credit transactions" reports (`SC`).

---

## 6. Parties and who can act

- **Buyer / customer**:
  - Pays at checkout, by invoice link, or through **Pay now** in their account.
  - Can request returns and cancellations.
  - Manages subscription payment methods, can skip, pause or cancel, and confirms challenged payments (`B2B/payment-terms.md`, `MO/returns/self-serve-returns/setup.md`, `…/shopify-subscriptions/customer-experience.md`).
  - Gift card recipients are distinct from buyers (`GiftCardRecipient`) [S:GiftCardRecipient].
- **B2B company → company location → B2B customer (contact)**:
  - Terms, deposits, checkout-to-draft, vaulted methods and store credit attach to the **location** (or to the company for all its locations).
  - The order carries `purchasingEntity` and `poNumber` [S:Order, S:DraftOrder].
  - "Both the B2B customer that placed the order and the location admin can request returns" (`MO/returns/self-serve-returns/setup.md`).
  - Only customers can vault cards or bank accounts ("You can't vault credit card details that you enter manually") (`B2B/vaulted-cards.md`).
  - Changing the vaulted bank account on an order needs the customer's approval (`B2B/vaulted-bank-accounts.md`).
- **Merchant / staff permissions**:
  - **Refund to original payment method**; **Refund to store credit**; **Over-refund orders previously refunded to store credit** (`MO/refunding-orders.md`).
  - **Edit orders** (`MO/editing-orders/considerations.md`). Shipping address: **Manage order information**, **Edit orders** or **Fulfill and ship orders** (`MO/editing-orders/customer-details.md`).
  - **Return** (`MO/returns/creating-returns.md`). Reviewing requests needs the **Orders** permission (`MO/returns/self-serve-returns/management.md`).
  - **Draft orders > Charge vaulted card** and **> Charge vaulted bank account** (`B2B/vaulted-cards.md`, `B2B/vaulted-bank-accounts.md`).
  - **Store credit** + **Edit store credit** + **View store credit transactions** (`SC`). For companies, Company-scoped **Edit store credit** (`B2B/store-credit.md`).
  - Without both refund permissions, "the Refund method section isn't displayed" ([fetched] processing-returns).
  - Schema records the acting `user: StaffMember` and `app` on every agreement and refund [S:SalesAgreement, S:Refund].
- **Apps**:
  - Pre-order, TBYB and subscription apps own the selling-plan logic.
  - "Only the app that creates an order can edit the order" (imported orders) (`MO/editing-orders/considerations.md`).
  - A refund in the admin may also need cancellation in the app (`PO/pre-orders/manage-pre-orders.md`).
- **Payment provider**: owns the asynchronous pending state and the expiry ("contact the payment provider to find out if the payment can still be captured") (`MO/payments/pending-payments.md`).
- **Merchant of record**: for drafts under Managed Markets, either Managed Markets or the store (`MO/create-orders/international-drafts.md`). Schema: `merchantOfRecordApp`, `merchantBusinessEntity` [S:Order].
- **Automation actor**: Shopify Flow can capture non-high-risk orders, cancel high-risk ones, and charge vaulted payments when a schedule is due (`MO/protecting-orders/shopify-flow.md`, `B2B/vaulted-cards.md`).

---

## 7. Multi-currency on the order

- **Three currencies**: **Store currency**, **Local (presentment) currency** and **Payout currency** (`IP/exchange-rates.md`). Order money is held as `MoneyBag{shopMoney, presentmentMoney}`, plus `currencyCode` and `presentmentCurrencyCode` [S:MoneyBag, S:Order].
- **When the rate is fixed** (`IP/exchange-rates.md`):
  - "Currency conversion occurs at the time of a transaction, such as when you capture a payment, you issue a refund, or when there is a chargeback".
  - Before capture, shop-currency values are "estimates". Under manual capture, €90 authorized can land as $98 instead of $100.
  - Fulfilment-time line conversions are approximate.
- **Drafts**: the FX rate is "calculated when you create the draft order… fixed and used on the invoice". Editing a saved draft re-rates the whole order (`MO/create-orders/create-draft.md`). Mark-as-paid "Amount received" is converted at the live rate and can be edited (`MO/create-orders/get-paid.md`).
- **Edits** (`MO/editing-orders/considerations.md`):
  - A new item uses the current rate.
  - A quantity increase uses the original rate.
  - A removal or decrease uses the original rate, "so that your customer isn't affected".
  - Editing international-currency orders "is only available to some stores". The fallback is refund + new draft.
- **Refunds** (`IP/refunds.md`):
  - Always in the currency the customer paid, and to the same method.
  - The conversion uses the current rate (even with manual rates).
  - The merchant carries the FX gain or loss. Example: €85 = $100 at sale, $110 at refund.
- **Chargebacks** convert at the time of transfer, with no conversion fee (`IP/exchange-rates.md`).
- **Subscriptions** keep the first order's rate (`IP/exchange-rates.md`).
- **Fees**: the conversion fee is 1.5% (US) or 2% (France and others), 3% for PayPal Wallet. It is charged at capture and folded into the displayed price (`IP/fees.md`).
- **Restrictions**:
  - With terms on a non-store-currency draft → card or mark-as-paid only (`IP/limitations.md`).
  - Local currencies need Shopify Payments or Adyen; otherwise orders settle in store currency (`IP/limitations.md`).
  - Checkout restrictions switch the currency to match the shipping destination (`IP/checkout-restrictions.md`).
  - Reports are in store currency only (`IP/limitations.md`).
- **Volatile currencies** are not auto-activated because "you might gain or lose large amounts of money on returns or exchanges". The 20 listed include ARS and TRY (`IP/volatile-currencies.md`). YER is in the list of supported Shopify Payments currencies (`IP/supported-currencies.md`).
- **Discounts**: fixed amounts are created in store currency and converted at checkout (or at the manual rate). Percentages don't convert (`IP/discounts.md`, `help/manual/markets/discounts-and-gift-cards.md`).
- **Transaction-level FX**: `OrderTransaction.settlementCurrency`, `settlementCurrencyRate`, `currencyExchangeAdjustment{originalAmountSet, adjustment, finalAmountSet}` [S:OrderTransaction, S:CurrencyExchangeAdjustment].

---

## 8. Invariants and rules worth copying

1. Changing what is owed (edit, return, discount, address change) never moves money by itself. It produces a signed outstanding balance that needs a separate settlement action (`MO/editing-orders/products.md`, `MO/refunding-orders.md`).
2. Capture ≤ authorized. Extra amounts need a new collection (`MO/payments/capturing-payments.md`). Multiple captures are allowed only if the provider supports them, and each capture is charged (`MO/payments/capturing-payments.md`).
3. Refunds ≤ the original amount. Per-tender refunds ≤ the amount available on that tender. Shipping refunds ≤ the shipping charged. The ceiling is broken only by the explicit `allowOverRefunding` path (`MO/refunding-orders.md`, [S:RefundInput]).
4. Refunds are irreversible. Corrections are new obligations (a draft) (`MO/refunding-orders.md`).
5. A return must come before a refund. A return requires fulfilled, unrefunded items (`MO/refunding-orders.md`, `MO/returns/creating-returns.md`).
6. No cancellation after partial fulfillment. A cancellation with no capture → Voided (`MO/canceling-orders.md`).
7. The ledgers are append-only: a sales agreement per action, immutable minor-unit allocation, and adjustment lines for discrepancies [S:SalesAgreement, S:Sale, S:OrderAdjustment].
8. Refunds go out in the currency paid and to the method paid with. The rate is set at the time of each money transaction (`IP/refunds.md`, `IP/exchange-rates.md`).
9. The order snapshots product data, return rules, the draft FX rate, the subscription FX rate and the discount on a subscription contract (`MO/managing-order-details` [fetched], `MO/returns/return-rules.md`, `MO/create-orders/create-draft.md`, `IP/exchange-rates.md`, `PO/subscriptions/manage-subscriptions/subscription-discounts.md`).
10. Stored-value balances change only through ledger transactions, never by direct edit (`GC/manage-purchased-gift-cards.md`, `SC`).
11. Deposits are a % of the subtotal, excluding tax and shipping. Deposits can't be paid with store credit. Plus only (`B2B/draft-orders.md`, `B2B/store-credit.md`).
12. Mixed deferred items → earliest due date wins, except that due-on-fulfillment beats dates (`PO/pre-orders/setup.md`).
13. Subscription billing attempts are idempotent [S:SubscriptionBillingAttempt]. So are mandate payments (`idempotencyKey`) [S:MUTATIONS].
14. Numbers:
    - Shopify Payments authorization: 7 days. Plus extended authorization: up to 30 days, with a 1.75% fee after 7 days (`help/manual/payments/payment-authorization.md`).
    - **Expiring** badge: 2 days before the deadline.
    - Pending-payment expiry: about 1 week.
    - Net terms: 7 / 15 / 30 / 45 / 60 / 90.
    - Up to 5 reminders, up to 30 days after the due date.
    - Bulk cancel: ≤ 250 orders. Self-serve return requests: ≤ 250 lines.
    - Gift cards: ≤ $10k (product) and ≤ $2k (admin-created).
    - Store credit: < $15k per customer and < $10k per company location.
    - Tips: ≤ 100% and ≤ $1000.
    - Drafts: 5 discount codes; auto-deleted after 1 year.
    - Conversion fee: 1.5% / 2%.
    - Subscription billing: the day after due, at 10:00 store time.
    - Payment-method update links expire after 48 h (`PO/subscriptions/manage-subscriptions/manage-customer-subscriptions.md`).

---

## 9. Tensions and edge cases

- **When net terms start.** "From the issue date" (`MO/payments/deferred-payments.md`, `MO/create-orders/create-draft.md`) versus "All terms start from the day the order is placed" (`B2B/payment-terms.md`). `PaymentSchedule.issuedAt` suggests the issue date is the real anchor.
- **Due vs Overdue.** The UI uses **Due** (which includes overdue), says the order "becomes **Overdue**", and customer accounts also show "**Overdue**". The financial-status enum has neither (`MO/order-status.md`, `MO/payments/deferred-payments.md`, [S:OrderDisplayFinancialStatus]).
- **Are return fees deducted automatically?**
  - `MO/returns/creating-returns.md` says fees "are applied against returned items to determine whether a refund is due".
  - `MO/returns/return-rules.md` says "Return fees aren't automatically deducted from refunds… manually deduct".
  - `MO/refunding-orders.md` says to edit the Refund amount "to deduct a restocking fee".
- **Can gift cards be local currency?** `help/manual/markets/discounts-and-gift-cards.md` says "You can't create gift cards in a specific market's local currency". `IP/gift-cards.md` and `GC/issue-gift-card.md` describe local-currency and cross-currency gift cards.
- **B2B refund to store credit.** `B2B/store-credit.md` says store credit can be offered as a refund. `orderCancel` has the error `STORE_CREDIT_REFUND_B2B_NOT_SUPPORTED` [S:OrderCancelUserErrorCode].
- **Refund method.** `IP/refunds.md` says refunds always go to the same method, yet store-credit refunds and over-refunds exist (`MO/refunding-orders.md`). Inference: "same method" applies to card-network tenders only.
- **Over-refund creates double value** (store credit plus card) unless the merchant debits it manually (`MO/refunding-orders.md`).
- **Partial refunds don't cap chargebacks.** The full amount is debited and the merchant must dispute (`MO/refunding-orders.md`).
- **Bulk cancel can double-refund already-refunded orders.** After a lost chargeback, cancel with "Later" to avoid a second refund (`MO/canceling-orders.md`).
- **Cancelling a fulfilled-but-unpaid order** destroys the right to collect (`MO/canceling-orders.md`).
- **Pending provider payments** block edits, restocks, cancellations, mark-as-paid and manual collection. Fulfilment is not blocked, which lets the merchant ship unpaid goods (`MO/payments/pending-payments.md`).
- **Partial return processing** can flip the sign of the balance. Docs warn against refunding before a later collection (`MO/returns/creating-returns.md`).
- **App-unaware edits**: a fulfilment app may ship an item that was removed "and not paid for" (`MO/editing-orders/considerations.md`).
- **Discounts not recalculated on edit**, so the merchant must check totals (`MO/editing-orders/considerations.md`).
- **Subscription failure modes**: a high-risk initial subscription order blocks renewals until it is fulfilled or cancelled; cancelling an order doesn't cancel the contract (`PO/subscriptions/manage-subscriptions/manage-subscription-orders.md`, `MO/returns/self-serve-returns/setup.md`). Insufficient inventory means no order is created (`…/manage-contracts.md`).
- **Gift card refunds**: a refund to an expired card fails until the expiry is extended. A deactivated card can't take a refund. Reloading needs Shopify Payments (`GC/manage-purchased-gift-cards.md`).
- **FX**: authorizing in one currency and capturing later causes drift. Refunds at the current rate cause gains or losses. Store currency changes leave gift cards "Active" but unredeemable (`IP/exchange-rates.md`, `IP/gift-cards.md`).
- **Store credit gaps**: it can't be applied to drafts or edits, can't be partially applied, and can't pay deposits (`SC`, `B2B/store-credit.md`).
- **Marking a draft paid before the customer pays** breaks the invoice link (`MO/create-orders/send-draft.md`).
- **Shop Pay Installments orders can't be edited**. The fix is refund + new order (`MO/editing-orders/considerations.md`).
- **Deletion**: only test orders, manual-payment orders, drafts marked paid, API imports and drafts can be deleted. Orders paid with a gift card can be archived but not deleted (`MO/canceling-orders.md`). Inference: tender type drives record immutability.

**Inference for Sharrwah (Yemen).** COD and bank transfer map onto **Payment pending** → **Mark as paid** or **Record payment**. Cash refunds need a recorded refund with no gateway. A volatile local currency argues for fixing the rate per transaction and carrying a currency-exchange adjustment, as Shopify does. B2B net terms with deposits are likely to matter early.

---

## 10. Class-level questions (provider-agnostic)

1. Which events can change what a buyer owes after the order exists (edits, address and tax changes, returns, exchanges, fees, discounts, cancellations), and how is the difference settled in each direction? Is settlement automatic or a separate act? — *events*
2. Is "what was agreed" recorded as an append-only ledger of agreements and line-typed sales, separate from "what money moved"? How are discrepancies between the two recorded? — *information*
3. What signed balance (outstanding / owed) is the single source of truth, and which statuses are projections of it? — *information*
4. When is an obligation fixed: at proposal (draft/quote), at acceptance (checkout or submit-for-approval), or at fulfillment? What is snapshotted at each point (price, FX rate, tax, rules, discounts)? — *lifecycle*
5. How are due dates expressed (on receipt, net-N from issue, fixed date, on fulfillment, per-fulfillment request), and what happens at the due date: an automatic charge, a reminder, or only a status change? — *rules*
6. Can a single obligation be split into instalments or deposits, and how is each part's basis defined (subtotal vs total incl. tax and shipping)? Which tenders may pay which part? — *rules*
7. What is the ceiling on collection (authorized amount, outstanding balance) and on refunds (paid amount, per tender, per shipping line)? Under what explicit override can a ceiling be exceeded? — *rules*
8. Which actor may create, change, collect and refund each kind of obligation (buyer, contact, location admin, staff role, app, automation)? How is that recorded on each money event? — *actors*
9. What standing permission (mandate or vault) allows the merchant to charge later? Who grants it, what is it scoped to, and can it outlive deletion of the instrument? — *actors*
10. How does a refund choose among multiple tenders (stored value first? per-tender caps?), and how is a refund to stored value that later converts to cash reconciled? — *rules*
11. Are gift cards and store credit modelled as owned ledger accounts with typed transactions (credit, debit, revert, expire)? What makes them liabilities vs promotional credit, and how is face value vs price paid accounted for? — *information*
12. What happens to obligations when the payment path fails or stalls (async pending, expired authorization, failed renewal, inventory shortage)? What retry, idempotency and fallback rules exist? — *quality*
13. In which currency is each obligation denominated, when is the rate fixed, and who bears FX gains or losses on capture, refund, chargeback and stored-value redemption? — *variability*
14. How do deferred purchase options (pre-order, try-before-buy, subscription) plug into the same obligation model, and what combination rules apply in mixed carts? — *extension*
15. Which order states block which money actions (pending provider payment, partial fulfillment, imported or app-owned, installments), and why? — *rules*
16. How are third-party fees (processing, conversion, transaction) treated when obligations are reversed? Are they ever refunded to the merchant? — *scope*
17. Which money facts are recorded off-platform (cash, bank transfer, COD) versus executed on-platform, and how does the order distinguish recorded from captured money? — *scope*
18. How do refunds and chargebacks interact (partial refund then full dispute, cancellation after a lost dispute) so that money isn't returned twice? — *quality*
19. How are B2B parties (company, location, contact) attached to terms, deposits, vaulted instruments and stored value, versus D2C customers? — *actors*
20. When an order's owed amount changes, how is reporting dated (by original order vs by change event)? — *information*
