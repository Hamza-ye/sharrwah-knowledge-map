# E — In-person money handling, finance products coupled to sales, and merchant→platform obligations (Shopify)

Reader slice E. Source: the Shopify help and dev corpus, plus the schema extract `admin-2026-10-money.md`. Every claim cites a source. My own reasoning is marked **Inference:**.

**Path legend** (corpus-relative):
- `POS/` = `help/manual/sell-in-person/shopify-pos/`
- `SETUP/` = `help/manual/sell-in-person/getting-started/setup-payment-method/`
- `FIN/` = `help/manual/finance/`
- `BILL/` = `help/manual/your-account/manage-billing/`
- `ORG/` = `help/manual/organization-settings/billing/`
- `[schema X]` = a type in `scratchpad/schema/admin-2026-10-money.md`
- `[fetched …]` = a page missing from the corpus that I read with curl. There are two: `help/manual/sell-in-person/shopify-pos/selling-offline/offline-checkout` and `shopify.dev/docs/apps/launch/billing/manual-pricing` (+ `/subscription-billing/create-usage-based-subscriptions`).

---

## 0. The model underneath, in brief

1. **Tenders differ by who attests the outcome.** There are three kinds of attester:
   - **Processor-attested:** Shopify Payments cards, Tap to Pay, QR local methods, and Shop Pay Installments (where Affirm approves).
   - **Platform-ledger:** gift card and store credit. These are internal stored-value ledgers that Shopify both issues and debits.
   - **Staff-attested:** cash, and "custom payment" types such as checks and external terminals. Shopify only records these: "funds aren't processed by Shopify… Custom payment methods are for payment tracking purposes" (`SETUP/enable-payments.md`).

   Two further states sit beside these: **deferred** ("Mark unpaid", partial payments) and **provisional** (offline card payments, processed on reconnect).
2. **Cash is a custody ledger, separate from the order ledger.** Orders carry cash `OrderTransaction`s, of kind `SALE`/`CHANGE`, with device, location and staff. Separately, a per-device **register/payment session** tracks the expected and counted contents of a **cash drawer**, records adjustments with reason codes, and turns the difference into a discrepancy attributed to staff and session. Nothing in Shopify moves counted cash to a bank. The cash ledger ends at the drawer count (`POS/cash-register-management/*`, `[schema PointOfSaleDevicePaymentSession, CashDrawer]`).
3. **The Shopify Payments balance is the platform's programmable money stream.** Processing fees, reserves and chargeback holds are netted from it, and so are lender claims:
   - Capital remittances for loans accepted on or after March 9, 2026.
   - Credit "Pay over time" repayments.

   All of these are netted "before your payout is deposited". Merchant-defined splits then run on arrival in Balance (auto-transfer rules). The payout carries an **Adjustments** section showing the deductions (`FIN/shopify-capital/united-states.md`, `FIN/shopify-credit/manage-account.md`, `FIN/shopify-balance/managing-account/auto-transfers.md`, `[schema ShopifyPaymentsTransactionType]`).
4. **Obligations are computed on all sales, but collected only where money is reachable.** Capital remittance is a percentage of daily sales "regardless of the order source, the payment processing method that was used, or whether the order was later refunded or canceled". That base includes cash and POS sales. Collection, however, comes from the Payments balance or a bank debit (`FIN/shopify-capital/*.md`).
5. **Merchant→platform billing is a separate invoice ledger.** It runs on 30-day/annual cycles with amount thresholds and is paid from a stored external instrument (card, PayPal, ACH, SEPA, UPI mandate, Balance card). It is not paid from payouts. Failure leads to retries, then a freeze at 28 days, then a right to terminate 60 days after suspension (`BILL/*`). Two exceptions run the other way. Payments processing fees are deducted from payouts. A negative Payments balance can be added to bills (`BILL/billing-charges/types-of-charges.md`, `BILL/billing-charges/types-of-charges/unknown-charge.md`).
6. **App developers bill merchants through the platform's invoice.** The merchant approves each charge. Usage charges are bounded by a merchant-adjustable `cappedAmount` per 30-day cycle. Shopify collects, remits the developer's share and handles chargebacks. The developer decides refunds (`dev/docs/apps/launch/billing.md`, `[fetched manual-pricing]`, `BILL/…/app-charges.md`).

---

## 1. In-person arrangements

### 1.1 Tender catalogue and how each outcome is established
- **Configuration is two-level.** A default list in the POS editor applies to new devices. Each device can only *deactivate* items from that list: "you can't activate payments on individual POS devices that aren't included in the default list". Example: if **Mark as unpaid** is off in the defaults, no device can turn it on. Card readers accept every brand supported in the region and can't be restricted per brand. Parent/child dependencies aren't enforced: turning off **Credit and debit** doesn't turn off **Allow manual card entry (MOTO)** (`SETUP/enable-payments.md`).
- **Cash.** On by default. "There are no additional fees or charges to the customer or to the store for cash payments." Shopify "calculates the change and tracks the amount of cash in the cash drawer". Staff accept a suggested or typed amount received (`POS/payment-management/cash-payments.md`, `SETUP/enable-payments.md`).
- **Card present (Shopify Payments).** Chip, contactless, swipe (fallback only) and wallets. Tap to Pay on iPhone/Android uses in-person rates. Android requires another reader for PIN or swipe (`POS/payment-management/card-payments.md`, `tap-to-pay-*.md`). Card-present acceptance has two country rules (`SETUP/compliance.md`):
  - The store's country must match every location's country, and the store currency must match both the local currency and the payout bank currency.
  - Shopify Payments can accept in-person payments in **one country per store**. Plus multi-entity is the exception.
- **Manual card entry.** "card-not-present transactions, even when the customer is in your store". Charged at a different rate, has added fraud risk, and isn't allowed offline (`POS/payment-management/card-payments.md`).
- **External terminal / custom payment type** (checks, third-party terminals). Staff create a named custom type, process on the external device, then tap **Mark as paid**. Tracked fields are order number, customer, line items, total incl. taxes, timestamps, and the custom type used. There are no Shopify fees. The tip is to create one custom type per terminal or per card brand "for better payment tracking" (`POS/payment-management/card-payments.md#external-card-reader`, `SETUP/enable-payments.md#custom`). Refunds go back only through the custom method: "Orders paid with a custom payment method can only be refunded with the custom payment method" (`POS/order-management/complete-refund-orders.md`).
- **Local payment methods** (Alipay, iDEAL | Wero, Klarna, Swish, TWINT, MobilePay, Satispay, USDC, WeChat Pay, Shop Pay). The POS shows a QR code, the customer pays on their own device, and "Shopify POS waits for payment success, and then displays as approved". These are treated as non-card-present at online rates. They carry "higher chargeback risk in retail settings" because goods leave immediately. A method appears only if it supports the **location's currency**. Retail-compatible third-party payment apps from the payment partner platform can also appear (`POS/payment-management/accepting-local-payments.md`). Local and offsite methods can't be used to collect on existing orders that include a shipping line (`SETUP/troubleshoot-pos-payments.md`).
- **Shop Pay Installments** (US/USD only). Approval happens on the customer's phone via QR. "After the purchase is verified by Affirm", staff confirm the status is **Completed**. Rules:
  - Basket must be $50–$20,000 USD.
  - Biweekly plans accept credit or debit; monthly plans debit only.
  - No split payments, no gift cards, no exchanges, no refund to gift card. Refunds go to the original method only.
  - Same transaction fees as online.
  - Staff can **Assist another customer** while the checkout runs in the background (`POS/payment-management/shop-pay-installments.md`).
- **Gift card.** A platform-issued stored value redeemable on every Shopify-checkout channel, and "the balance automatically updates across all sales channels". It can't be reloaded after redemption. Third-party physical cards need 8–20 alphanumeric codes. The validation code can't be retrieved after leaving the screen. Selling a gift card requires full payment: "You can't mark a checkout that contains a gift card product as partially paid or unpaid" (`POS/payment-management/gift-cards/*.md`, `multiple-partial-payments.md`).
  - **Cash-out:** requires the **Cash out gift cards** permission or manager approval. The balance must be under $15 USD or local equivalent, the card active and unexpired, and the payout cash only (`gift-cards/cashing-out.md`).
- **Store credit.** A per-customer wallet, labelled **Wallets** on the profile. The **maximum possible amount** is always applied ("You can't redeem custom partial amounts"). It can't be used with a gift card product in the cart or offline. It needs the **Redeem store credit** permission. Staff with **Manage a customer's store credit** can manually **Add/Remove** with an optional expiry. It can't be active on POS unless it is also active online (`POS/payment-management/store-credit/*.md`, `SETUP/enable-payments.md#store-credit`). `[schema StoreCreditSystemEvent]` = ADJUSTMENT, ORDER_PAYMENT, ORDER_REFUND, PAYMENT_FAILURE, PAYMENT_RETURNED, ORDER_CANCELLATION, TAX_FINALIZATION, RECURRING_PAYMENT.
- **Subscriptions at POS** (POS Pro, Shopify Payments). Card or wallet only, total > 0, no split, no offline, no gift card. "If a customer wants to purchase other items… with a different payment method, then you need to create a separate order" (`POS/payment-management/subscriptions.md`).
- **Mark unpaid.** "The order is processed as a 0.00 payment and can be paid for later" (`POS/payment-management/select-payment-methods.md`). Unpaid and offline orders can show a register-prefixed number such as `#1-1005` [fetched offline-checkout].

### 1.2 Authorization vs capture at the counter
- **Delayed capture** (POS Pro, on by default): card payments "are authorized at the point of sale and captured after a delay of up to 15 minutes". While uncaptured, the payment status is **Authorized**. Staff can **cancel the order** instead of refunding, and "Transaction fees don't apply to canceled orders". After capture, changing items or amount requires a refund.
  - Not available in Germany or Italy.
  - These payments can't be cancelled in the window: gift card, cash, Interac, EFTPOS, manual credit, and split-payment orders.
  - The authorization hold may show on the customer's statement for up to 30 days.

  (`POS/payment-management/card-payments.md#delayed-capture`)
- **Schema:** `OrderTransactionKind` includes `AUTHORIZATION`, `CAPTURE`, `SALE`, `VOID`, `REFUND`, `CHANGE`, `EMV_AUTHORIZATION`, `SUGGESTED_REFUND`. `OrderTransactionStatus` includes `PENDING`, `AWAITING_RESPONSE`, `UNKNOWN`. `OrderDisplayFinancialStatus` includes `AUTHORIZED`, `PARTIALLY_PAID`, `EXPIRED`, `VOIDED`. `OrderTransaction` carries `device: PointOfSaleDevice`, `location`, `user: StaffMember`, `manualPaymentGateway`, `amountRoundingSet`, `fees: [TransactionFee]`, `parentTransaction`, `authorizationExpiresAt` ([schema OrderTransaction]). **Inference:** `EMV_AUTHORIZATION` is the card-present authorization record that delayed capture and offline payments rely on. `CHANGE` records cash handed back. The schema extract has no descriptions for these kinds.
- **PIN re-entry.** A staff member must re-enter their POS PIN after a checkout error, a cancelled checkout, or a cancelled tip, "to prevent customers from checking out without paying" (`POS/payment-management/card-payments.md#pos-security`).

### 1.3 Split and partial payments
- **Split payment** takes several tenders for one order. **Mark as partially paid** saves the order. A later **Collect payment** takes any amount by any method (`POS/payment-management/multiple-partial-payments.md`).
- **Lock rule:** "If you refund or exchange an item that's part of an order being paid for in multiple payments or edit the order, then you can't receive additional payments on that order" (same page and `complete-refund-orders.md`).
- **EU restriction:** some EU retail locations (France, Italy, Spain) can't mark a transaction partially paid or unpaid (`multiple-partial-payments.md`).
- **Gift-card redemption** that leaves a remainder offers **Add payment** or **Mark as partial** (`gift-cards/redeem-gift-cards.md`).

### 1.4 Change and cash rounding
- Rounding uses the "Swedish rounding method". It is applied to the final total after discounts and taxes, on cash payments **and refunds/exchanges**. Example: $9.99 CAD paid → +$0.01 adjustment → $10.00. A partial refund of $5.02 → −$0.02 → $5.00 (`POS/cash-rounding-on-pos.md`). Rules:
  - Only cash is rounded, and only when the checkout currency equals the location's local currency.
  - Refunds to gift card aren't rounded.
  - Full refunds and cancellations reverse the original rounded amount.
  - Partial refunds and exchanges use the rule of the return location.
  - The location's custom rule applies, otherwise the country default. Methods: **No rounding / Nearest** (with midpoint choice) **/ Round up always / Round down always**.
  - Countries ship with defaults (AU 0.05, CA 0.05, NO/SE 1.00, …). New stores, or first retail locations created on or after July 6, 2026, get further defaults (e.g. Chile 10 CLP, Hungary 5 HUF, Peru round down 0.10).
  - The cash counting tool hides denominations no longer in circulation.
- "If your POS staff accepts the exact unrounded amount… but selects a rounded suggestion… Shopify POS records the rounded amount" (`POS/cash-rounding-on-pos.md`).
- **Records:**
  - Order: **Cash rounding** adjustment and **Rounded net payment**. The timeline shows unrounded amount, adjustment and final amount.
  - Reports: `cash_rounding` and `rounded_net_payments` in ShopifyQL.
  - Cash tracking: gross, refunds and net shown rounded.
  - Schema: `CashRoundingAdjustment {paymentSet, refundSet}`, `Order.totalCashRoundingAdjustment`, `OrderTransaction.amountRoundingSet`.

  Receipts, email/SMS and the customer display all show both unrounded and rounded totals (`POS/cash-rounding-on-pos.md`, `POS/receipt-management/cash-rounding.md`).

### 1.5 Tips
- Card-only on supported readers, and only on the "credit payment method" (`POS/tips.md`).
- Settings: up to 3 percentage presets, optional custom amount, and optional **Minimum tip amounts** (fixed amounts below a transaction limit).
- **Cap:** for USD/CAD, the maximum tip is 1000 for checkout totals up to 500, and 2× the total above that. Other currencies, and split payments in any currency, cap at 2× the checkout total.
- A tip can be refunded without refunding the order.
- A **Tips report** shows tips per staff member, and the **Finances** report shows totals (`POS/tips.md`).
- Schema: `TipSale`, `Order.totalTipReceivedSet` ([schema]).
- **Who receives tips:** the docs only attribute tips to staff for reporting. The money settles to the merchant with the card payment. **Inference:** paying tips out to staff is outside Shopify, so the platform tracks a liability to staff without settling it.

### 1.6 Offline
- **Offline checkout** [fetched offline-checkout]: accepts cash and custom payment methods. Requires:
  - the customer's phone or email;
  - the **Switch device to offline checkout** permission, with optional manager PIN approval logged in the store activity log;
  - leaving the device on and staying logged in, since logging out "might cause loss of offline orders".

  Orders and inventory sync on reconnect. Not available in France.
- **Offline payments** (cards) (`POS/selling-offline/offline-payments.md`):
  - "Offline transactions aren't routed to the payment processor. You might not know that a transaction has failed until you reconnect."
  - Payments are "captured after your device reconnects". Reconnect "ideally within 24 hours".
  - Order badges go **Payment pending** → **Paid** or **Card declined**. If declined, contact the customer using the email or phone collected.
- **Exposure limits** (merchant-set, store-wide, auto-converted per country): **Device daily limit** (total offline card payments per device) and **Transaction limit** (per order; above it, use cash). Permission: **Accept offline credit and debit payments**.
- **Exclusions:** swipe, Tap to Pay, MOTO, Interac (CA) and eftpos (AU) aren't allowed offline. The feature is off in France. Store credit and subscriptions are unavailable offline. Cash rounding works offline on POS 11.11+.
- **Always-on card authorization** (POS Terminal): with offline checkout on and the terminal still online, card-present payments are authorized in real time [fetched offline-checkout].

### 1.7 Refunds and exchanges in person
- **Cap per tender:** "The amount that a customer paid with a payment method is the maximum that you can refund with that payment method." A **Split refund** spreads the refund across methods. Return reasons can be required, with **Unknown** as the default and **Other** needing text. **Unverified returns** are refunds without an order. A return already in progress in the admin blocks POS returns (`POS/order-management/complete-refund-orders.md`).
- **Interac:** refunds must be in person with the same card present, and can't be done from the admin. If the refund fails but the return processes, staff manually enter the **Amount to refund**. Wallet-paid orders need the same device and card. For exchanges, the balance owed can go to *any* Interac card. With a split payment that includes Interac, staff can't exchange down to a lower total (`POS/payment-management/refund-interac-payments.md`).
- **Refund to gift card:** a **new** card needs ≥1 fulfilled return item. Reloading an **existing** card is allowed only for Shopify Payments transactions; for cash or other institutions the option is greyed out. Limits:
  - must stay within the gift card purchase limit;
  - not for split refunds that include Interac;
  - not for subscriptions;
  - can be sent to a different customer;
  - returns started in the admin can't be refunded to a gift card on POS.

  (`POS/payment-management/gift-cards/refund-to-gift-card.md`)
- **Refund to store credit:** requires a customer profile, which is created on the fly if missing, and the setting **Allow orders to be refunded to store credit**. The customer gets an **Order refund** email, not **Store credit issued** (`store-credit/returns-and-exchanges.md`).
- **Exchanges** (POS Pro) go through one **Return or exchange** flow. A net positive balance is collected and a net negative balance is refunded. Store credit can be applied or refunded. Restock happens at the processing location (`POS/order-management/exchange.md`).
- Refunding a gift card *purchase* requires deactivating the card first (`gift-cards/sell-gift-cards-pos.md`).

### 1.8 Receipts
Print, email or text. Printed and emailed receipts show cash rounding. A gift-card receipt shows the last 4 digits and the remaining balance. Offline receipts are sent after reconnect. Subscription purchases trigger a separate confirmation email (`POS/receipt-management/cash-rounding.md`, `gift-cards/redeem-gift-cards.md`, `selling-offline/offline-payments.md`, `subscriptions.md`).

---

## 2. Cash as a ledger

- **Concept.** "A register session is a record of all cash activity and payments during specified intervals, including the starting float, any cash added or removed, and the final count." At close, the **Cash tracking** and **Session** reports "compare your expected cash total against what's physically in the drawer" (`POS/cash-register-management.md`).
- **Purpose is accountability:** "make sure that staff are accountable for the cash they handle, and identify any discrepancies" (`register-sessions-in-shopify-pos.md`). The test-transaction guide also says sessions "hold staff accountable" (`SETUP/test-transaction.md`).
- **Opening.**
  - *Manual:* enter **Current amount in drawer**, optionally using **Count cash** (bills/coins).
  - *Automatic:* if the previous session ended and nobody opens a new one, the next order opens one, with "The calculated cash balance at the end of the previous register session" as the start. The first session starts at 0.
  - **Require cash counting at session start and end** is optional. Without it, sessions still track payments "but won't explicitly track cash amounts".
- **Adjustments.** **Add cash / Remove cash**, with a reason when reason codes are on. Reasons include not enough change, a drawer over limit, or a temporary removal. **Reason codes** can also be required for every manual **Open drawer**, with **Other** plus a note (`register-sessions-in-shopify-pos.md`, `register-sessions-in-shopify-admin.md#reason-codes`, `cash-drawer.md`).
- **Closing.** Count the cash → set the desired float → remove the excess → review **Session complete** ("The amount of cash in the cash drawer and the expected balance should be the same") → print. "After a register session is closed, it can't be reopened or edited."
  - **Remote close from the admin:** enter **Cash counted**, confirm the discrepancy, and select the cash left in the drawer. If a transaction is mid-flight, "a new session opens automatically when the next transaction completes" (`register-sessions-in-shopify-admin.md`).
- **Discrepancy definitions** (`cash-tracking-reports-by-location.md`):
  - **Opening discrepancy** = amount reported at the end of the last session vs amount counted at the start of this one.
  - **Closing discrepancy** = (counted at start + cash payments received) vs counted at end. Cash payments = **Gross payments** − **Refunds** = **Net payments**, rounded where applicable.
- **Reports.**
  - **Session:** times, net payments by payment type, cash activity.
  - **Net payments:** by type.
  - **Session activity:** every cash movement, incl. drawer openings.
  - CSV export of a discrepancy summary or of sessions.
  - **Cash tracking by location** (POS Pro): discrepancy summary, cash payments, and a session list sortable by total discrepancy. Permissions: **View payment register session history** and **View payment register sessions in the POS channel** (`register-sessions-in-shopify-admin.md`, `cash-tracking-reports-by-location.md`).
- **Constraints.**
  - One open session per device.
  - Sessions are stored on the device: "Sessions created on one device aren't visible on other devices". They may vanish on reinstall unless the location is on POS Pro, where the admin has them all.
  - "Register sessions aren't for long term reporting". Long-open sessions make **Expected cash** inaccurate.
  - The cash counting tool supports only AUD, CAD, EUR, GBP, JPY, NZD, PLN, SGD, USD.
  - Cash drawers and devices are **one-to-one** in the app. Many devices to one drawer needs the new API (`register-sessions-in-shopify-pos.md`, `cash-drawer.md`).
- **Schema: two generations.**
  - *Legacy* `CashTrackingSession`: opening/closing balance, expected balances, `totalDiscrepancy`, `cashTransactions: OrderTransactionConnection`, `adjustments: CashTrackingAdjustment{cash, note, staffMember, time}`, opening/closing staff and notes, `registerName`, `location`.
  - *Newer* `PointOfSaleDevicePaymentSession`: `cashDrawer: CashDrawer!`, `pointOfSaleDevice`, `cashCountedAtOpen/AtClose`, `expectedCashAtOpen/AtClose`, `closingAdjustment`, `totalDiscrepancy`, `totalCashSales/Refunds`, `netSales`, `currency`, `totalsReady`, `status OPEN|CLOSED` ("Payments can't be processed or refunded during a closed session, and the cash drawer balance can't be adjusted or corrected").
  - `CashDrawer {location, balance, totalSales, totalRefunds, totalAdjustments, totalDiscrepancies, netSales, pointOfSaleDevices, cashActivities}`. `CashActivity` (interface: cash, paymentSession, staffMember, time) has the variants `CashAdjustmentActivity`, `CashCountActivity`, `CashTransactionActivity`.
  - Mutations: `pointOfSaleDevicePaymentSessionOpen|Count|Adjust|Close(…, staffMemberId, reasonCodeId, note, time)`, `cashDrawerCreate`, `pointOfSaleDeviceAssignToCashDrawer`. Error codes: `CURRENCY_MISMATCH`, `NO_CASH_DRAWER_ASSOCIATED`, `ALREADY_OPEN`, `SESSION_ALREADY_CLOSED`, `TIME_BEFORE_SESSION_OPEN`, `REASON_CODE_NOT_FOUND`.

  **Inference:** the newer model separates *drawer* (a physical custody container, location-bound, possibly shared by devices) from *session* (a time-bounded accountability interval), and records counts as events rather than only opening and closing fields. Mid-shift blind counts become possible.
- **How cash links to orders.** Each cash sale is an `OrderTransaction` (gateway cash, kind `SALE`, plus `CHANGE` where applicable) carrying `device`, `location` and `user`. The session aggregates them via `cashTransactions` and `totalCashSales/Refunds`. Rounding sits on the order and the transaction. `TenderTransaction` ("a transaction with financial impact on a shop's balance sheet") exposes `paymentMethod`, `user` and `remoteReference` ([schema]). **Inference:** the order ledger says what was owed and what tender settled it. The drawer ledger says where the physical cash is and who handled it. Discrepancy belongs only to the drawer ledger and never edits orders.
- **Cash beyond the drawer.** No Shopify page covers depositing drawer cash to a bank. The only cash-in path is a separate product: Shopify Balance **Add cash** at Green Dot retailers (§3.2). **Inference:** for Yemen, courier COD bags and agent floats are a third custody container that Shopify lacks. Couriers fall outside the drawer→session model, which assumes a fixed device and location.

---

## 3. Finance products coupled to sales

### 3.1 The payout stream as the hub
- `ShopifyPaymentsAccount {balance:[MoneyV2], balanceTransactions, payouts, payoutSchedule{interval DAILY|WEEKLY|MONTHLY|MANUAL}}`.
- `ShopifyPaymentsBalanceTransaction {amount, fee, net, type, sourceType, associatedOrder, associatedPayout{status}, adjustmentReason, adjustmentsOrders}`.
- `ShopifyPaymentsPayout {gross, net, status SCHEDULED|IN_TRANSIT|PAID|FAILED|CANCELED, transactionType DEPOSIT|WITHDRAWAL, summary{chargesGross/Fee, refundsFeeGross, adjustmentsGross, reservedFundsGross/Fee, retriedPayoutsGross, advanceGross/Fees, usdcRebateCreditAmount}}` ([schema]).
- The `ShopifyPaymentsTransactionType` enum names every claim that can hit the stream:
  - `CHARGE`, `REFUND`, `REFUND_FAILURE`, `DISPUTE_WITHDRAWAL/REVERSAL`, `CHARGEBACK_HOLD/_RELEASE`, `CHARGEBACK_FEE`;
  - `RESERVED_FUNDS`, `RESERVED_FUNDS_WITHDRAWAL/REVERSAL`, `RISK_WITHDRAWAL/REVERSAL`;
  - `LENDING_DEBIT/CREDIT`, `LENDING_CAPITAL_REMITTANCE`, `LENDING_CREDIT_REMITTANCE`, `LENDING_CAPITAL_REFUND`, `LENDING_CREDIT_REFUND` (each with `_REVERSAL`);
  - `BILLING_DEBIT/_REVERSAL`, `SHIPPING_LABEL`, `CUSTOMS_DUTY`, `IMPORT_TAX`;
  - `ADVANCE`, `ADVANCE_FUNDING`;
  - `BALANCE_TRANSFER_INBOUND/OUTBOUND`, `MERCHANT_TO_MERCHANT_*`, `COLLECTIONS_CREDIT`, `ACH_BANK_FAILURE_DEBIT_FEE`, `CURRENCY_CONVERSION`, `TRANSFER/_FAILURE/_CANCEL`.

  Every type has a reversal twin. **Inference:** the platform models every claim as a signed, reversible balance entry linked to its source. `BILLING_DEBIT` and `SHIPPING_LABEL` show that platform charges *can* be netted from the stream, although the help docs describe bills as paid by external instrument (§4).
- Payments processing fees "are deducted from your payouts rather than billed on your Shopify bill" (`BILL/billing-charges/types-of-charges.md`).

### 3.2 Shopify Balance
Balance is a money account at partner banks. "Shopify is a tech company, not a bank" (`FIN/finance.md`).
- **Where payouts land.** The main Balance account becomes the payout account automatically, "up to 7 days earlier than a bank", typically 1–3 business days. Switching to Balance avoids the payout pause; switching away "might cause delays" and deactivates auto-transfer rules. One Balance account per store (`FIN/shopify-balance/payouts/payout-accounts.md`, `key-benefits-and-features.md`).
- **Auto-transfer rules.** "Auto-transfer rules run each time you receive a Shopify Payments payout", in this order:
  1. Sales-tax set-aside.
  2. Percentage distribution rules (sum ≤100%, up to 5 Balance destinations, unlimited external destinations).
  3. The remainder stays in the main account.

  Further rules:
  - Percentages only: no fixed amounts, no schedules.
  - Shopify Payments payouts only.
  - Internal transfers are instant and can't be cancelled. External transfers go by ACH in 1–3 days and can be cancelled while pending.
  - Edits apply to the next payout.
  - If one transfer fails (insufficient funds, closed account, daily transfer limit), "the rest of your payout still arrives… and other rules… continue to run" (`managing-account/auto-transfers.md`).
- **Sales-tax set-aside.** Can be inexact when payouts include refunds or chargebacks. A negative tax figure moves money back from the tax account "unless your sales tax account doesn't have enough funds". It excludes channels that remit tax themselves and third-party tax services (`FIN/shopify-balance/taxes/sales-tax.md`).
- **Moving money out.** Transfers to banks go same day if before 1 pm ET. The daily transfer limit is hidden, adjusts over time, and blocks transfers that exceed it. The card spend limit starts at $5,000/day/card and ATM at $500/day (rising to $1,000), with ATM fees counted against the limit. Domestic wire $10, ACH free. A suspicious movement blocks transfers and card creation until identity is verified (physical cards stay active) (`managing-account/transactions.md`, `transfers.md`, `account.md`).
- **Cash in through retail agents** (early access, US): generate a barcode in the app, valid 1 hour, tied to one retailer and amount (to change, cancel and regenerate). The cashier scans it and takes the cash. It shows **Pending**, becomes available after 1 business day, and each attempt expires after 24 hours.
  - Limits: $1,500 per rolling 24 h ("doesn't reset at midnight"), $3,500 per 7 days, $5,000 per calendar month (PT).
  - Each barcode counts as at least $500 from generation, so at most 3 per 24 h. Amounts over $500 split into several barcodes.
  - If funds don't appear within 3 days, the receipt is the evidence (`FIN/shopify-balance/adding-cash.md`).
- **Coupling to lenders and billing.** "any Shopify Capital remittances or repayments that you need to pay are also withdrawn from Shopify Balance" (`eligibility.md`). An additional Balance account can't be closed while it is used for payouts or Capital repayments (`managing-account/multiple-accounts.md`). The Balance card is the default payment method for Shopify bills for new Balance users (`BILL/paying-your-bills/making-payments/payment-methods-for-bills.md`).

### 3.3 Shopify Capital
Capital takes three legal forms: a **loan** (US/CA/AU/FR/DE; "Total payment amount" = loan + "Fixed borrowing cost"), a **merchant cash advance** that is a "purchase of your future sales" (UK/IE/NL/ES; "Total to remit" = amount × factor; UK partner YouLend, "purchase price", "termination amount"), and a **flex account** (credit line, early access US) (`FIN/shopify-capital.md`, `shopify-capital-glossary.md`, `united-kingdom.md`).
- **What the obligation is.** "Remittance rate… The percentage of your daily sales revenue that will be remitted… until the total to remit has been remitted" (glossary).
- **Base:** "all sales that are associated with your Shopify account… online store, at your retail locations, from any sales channels… and through any apps", and daily revenue "includes all orders that are marked as paid on that day, regardless of the order source, the payment processing method that was used, or whether the order was later refunded or canceled", including shipping and taxes. Test-mode orders are excluded. "No payment is taken on days when there are no sales" (`united-states.md`, `united-kingdom.md`, `ireland.md`).
- **On refunds:** the base is gross and refunds aren't netted. **Inference:** `LENDING_CAPITAL_REFUND` exists in the enum, but the help docs describe no remittance reversal for refunded or cancelled sales.
- **How it is collected.**
  - US loans accepted **on or after March 9, 2026** (Texas: Sept 1, 2025) are collected "directly from your Shopify Payments balance". If uncollectable "after these attempts", they are debited from the bank. Texas has no bank fallback. Retries are automatic, and persistent failure is a default.
  - Older loans and other countries use a daily bank debit with "isn't debited again" on failure; the next day proceeds as usual.
  - Deductions appear in the payout **Adjustments** section, in Capital history, and per order transaction (`united-states.md`, `australia.md`, `ireland.md`).
- **Terms.**
  - Loans: max 18 months, with minimums of 30% by month 6 and 60% by month 12, else possible default.
  - MCA: "no deadline". Manual prepayment over 1 unit is allowed but "the cost of funds remains the same". A second loan's repayments start only after the first is repaid.
  - Fee models: a fixed fee (factor) or a monthly fixed fee.
  - Flex: a monthly % fee on the average outstanding balance, accrued daily and charged at month end. $200 minimum draw. Repayment rate is adjustable when drawing and takes effect in 2–3 days. Capacity is reviewed weekly (`united-states.md`, `united-kingdom.md`, `shopify-capital-flex/*.md`).
- **Lock-in and eligibility.**
  - Switching away from Shopify Payments "is restricted until you've repaid".
  - In MCA countries, changing the remittance bank also changes the payout bank and needs a new debit mandate.
  - Eligibility depends on sales, "failed debits for Shopify Services", reserves, chargebacks and returns, and tenure of at least 3 months. Payout cadence affects eligibility (`eligibility.md`).

### 3.4 Shopify Credit
- A pay-in-full Visa charge card with a monthly statement and a one-month grace period. **Pay in full** is an automatic bank debit on the last business day of grace. **Pay over time** takes a % of daily sales "deducted from your Shopify Payments balance before your payout is deposited", falls back to a bank debit, carries an 11% fee with early-payoff discounts, and runs up to 10 months. Remaining balance at 10 months is debited; if that fails, a 2% monthly late fee applies and the cards lock (`FIN/shopify-credit.md`, `manage-account.md`).
- "In the event of an automatic payment failing or being reversed after the statement period, you're automatically switched to paying over time." Payments apply to the oldest statement first.
- The credit limit is reviewed monthly from sales and repayment history. If it falls below the balance, the merchant must pay down (`manage-account.md`, `getting-started.md`).
- **Cross-product locks** ("If your cards are locked for more than one of these reasons, then they unlock only after every reason is resolved"):
  - 5 consecutive failed bank debits (balance-collection failures don't count);
  - a Shopify Payments account issue;
  - Credit or Capital financing suspended;
  - a **Capital default**;
  - the store not on an active plan, which includes **frozen for an unpaid Shopify bill** (`manage-account.md#locked-cards`).

### 3.5 What this says about payouts
**Inference:** Shopify treats the settlement balance as an **ordered waterfall of claims**:
1. Processor fees, reserves and holds.
2. Lender remittances (Capital, Credit), with bank-debit fallback.
3. Possibly platform billing (`BILLING_DEBIT`).
4. Then the payout itself.
5. Then merchant splits in Balance (tax first, percentages next).

Claims are percentage-of-sales (lenders) or percentage-of-payout (splits). Each is a signed, reversible entry shown on the payout as **Adjustments**. Cash and external-terminal sales count toward the lender's base but never enter the waterfall. That is why a fallback (bank debit) exists.

---

## 4. Merchant → platform obligations

- **What is billed** (`BILL/billing-charges.md`, `types-of-charges.md`, `shopify-charges.md`):
  - *Recurring*, every 30 days: subscription, recurring app fees, Shopify Messaging beyond 10,000 free emails, Shopify POS subscriptions (listed in `BILL/…/local-currency.md`).
  - *Pay-per-use*: third-party transaction fees, shipping labels/adjustments/insurance, Shopify Tax fees, app usage.
  - *One-time*, on separate bills: themes, domains, one-time apps, brokered Partner Directory services.
  - **Not on the bill:** Shopify Payments processing fees (deducted from payouts) and external app charges.
- **Third-party transaction fees** apply when a third-party provider is used. On stores created on or after May 12, 2025, they also apply to the portion paid with **store credit or gift cards**, even under Shopify Payments.
  - **Exempt:** Shopify Payments, Shop Pay, Shop Pay Installments, manual methods ("cash, cash on delivery (COD), and bank transfers"), PayPal when Shopify Payments is primary. Also: "Transaction fees don't apply for POS orders or for manual payment methods… draft orders marked as paid or pending".
  - **Formula** per 30 days: `[(cost of products − discounts) + tax + shipping] × rate`.
  - "aren't returned to you when you issue an order refund", and are not refunded on cancellation (`third-party-transaction-fees.md`, `credit-notes-and-billing-credits.md`).
- **Shopify Tax fees:** applied after 100,000 in sales, capped at 0.99 per order and 5,000 per year per region (US/EU/UK/CA) per store (`shopify-tax-transaction-fees.md`).
- **Cycles and thresholds.**
  - The subscription runs 30 days or 1 year and is billed in UTC. The merchant can't choose the date and is "invoiced every 30 days… Payment is made in advance".
  - Each app runs its own 30-day cycle, charged with the next Shopify bill.
  - Annual plans still get a monthly bill, possibly $0.
  - **Billing threshold:** when "third-party transaction fees, recurring app charges, and other outstanding charges" exceed it, an off-cycle bill is issued. Subscription fees count in the running total but not in threshold bills.
  - Shipping labels can continue to 110% of the threshold and then stop until paid.
  - For Plus organizations, "Platform fees don't count toward the billing threshold" (`billing-cycles-thresholds.md`, `app-charges.md`, `ORG/view-bills.md`).
- **How bills are paid.**
  - Instruments: credit card, co-branded debit card (no prepaid or virtual), Balance card, PayPal, Revolut Pay, Apple Pay/Google Pay (plan checkout only), ACH, SEPA, UPI (India).
  - ACH eligibility: store ≥90 days old, ≥$10k monthly GMV over 90 days, >75% first-attempt invoice success.
  - A **backup** payment method is used automatically when the primary fails.
  - India: RBI e-mandate via Razorpay or UPI autopay, with pre-debit notifications. Bills over ₹15,000 need OTP or authorization (older mandates ₹5,000).
  - EU invoices may require 3DS. Attempts retry to the same pending verification.
  - The statement descriptor is `SHOPIFY * <9-digit bill number>`.

  (`payment-methods-for-bills.md`, `add-verify-bank.md`, `managing-payment-methods.md`, `account-billing-india/*`, `unknown-charge.md`)
- **Failed bill → freeze.** "Shopify doesn't grant extensions or grace periods." On failure, "Shopify retries the charge periodically. Your store remains fully active", and "If the invoice is still unpaid after 28 days from the first failed attempt, then your store becomes frozen." Frozen means:
  - the admin and storefront are inaccessible, but billing history is viewable;
  - "all billing attempts stop" and recurring app charges freeze;
  - reactivation requires paying **each** invoice, including charges accrued during the 28 days (apps, transaction fees, shipping);
  - if more than 30 days have passed since the last bill, the merchant must pick a plan and prepay;
  - "If outstanding fees remain unpaid for 60 days following the date of suspension, then Shopify reserves the right to terminate".

  To switch to Pause and Build, all outstanding invoices must be paid first (`billing-extensions.md`, `frozen-store.md`, `app-charges.md#app-charges-frozen-store`).
- **Currency.** USD by default. Local currency is available in AU, CA, EU, IN, JP and UK (all plans), and in CZ, DK, LI, NO, PL, RO, SG, SE and CH (non-Plus). The plan is priced natively. Apps, POS subscriptions, themes, domains, labels and third-party transaction fees are converted with a 1.5% FX fee, except third-party transaction fees, which are exempt. A change takes effect next cycle: outstanding charges stay in the old currency and credits are converted. App developers can price in the merchant's billing currency via `shopBillingPreferences` (`local-currency.md`, `dev/docs/apps/launch/billing.md`).
- **Taxes on bills** depend on the billing address: e.g. KSA VAT 15%, UAE 5%, Egypt 14%, Tanzania 18%, South Africa 15% with no exemption. A valid tax ID gives exemption where allowed (`BILL/billing-charges/types-of-charges/taxes/*.md`). Plus organizations: address and currency are set by contract (`ORG/billing-preferences.md`).
- **Refunds and credits.**
  - Plans are "generally non-refundable". Review windows: 7 days (monthly), 30 days (annual or first post-trial), 14 days (SEPA), 90 days (Brazil).
  - A **credit note** reduces an unpaid bill, or triggers a refund for a paid one. The account **balance** offsets future invoices.
  - Credits are **category-specific** (subscription/app/shipping/transaction) and future-only. They expire 60 days after deactivation.
  - Upgrades are immediate and prorated by credit. Downgrades take effect at the end of the cycle.
  - A cancelled shipping label becomes a credit "towards future label purchases".

  (`refund-policy-subscriptions.md`, `credit-notes-and-billing-credits.md`, `billing-plan-changes.md`, `shopify-charges.md`)
- **Reverse coupling.** "Charges might be added to your bills if your Shopify Payments account has a negative balance… refunds or… chargebacks". Capital repayments can appear as debits. Chargebacks can produce invoices after deactivation (`unknown-charge.md`, `billing-considerations-pause-deactivate-store.md`).
- **Organizations.** Plus has one consolidated invoice and one payment method for all stores. Shipping labels are always charged to the main store's method. Other plans are invoiced per store (`ORG/billing.md`, `billing-preferences.md`, `manage-store-billing.md`).

### 4.1 How apps charge merchants
- All App Store apps "are required to use a Shopify provided billing solution". With **Shopify App Pricing** (the default), "Charges are directly added to the merchant's Shopify invoice", "Shopify collects the charge and automatically pays out your share", and "Shopify handles all chargeback-related processes". It supports free, monthly or annual recurring, and usage plans with usage events via the App Events API. **Manual Pricing** (legacy Billing API) is needed for one-time purchases (`dev/docs/apps/launch/billing.md`).
- **Consent.** The app creates `appSubscriptionCreate` or `appPurchaseOneTimeCreate`, and Shopify returns a `confirmationUrl` where the merchant "either approves or declines". Upgrades and downgrades go through the same flow.
- **Usage caps.** Usage plans need a `cappedAmount`: "the maximum that a merchant is billed for during the 30-day billing cycle". Merchants can change it in the admin. Webhooks fire at 90% of the cap (`APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT`) and on change (`APP_SUBSCRIPTIONS_UPDATE`). Usage can pair only with a 30-day recurring fee. Adjustments available: app credits, subscription discounts, free trials (new subscriptions only), refunds [fetched manual-pricing; create-usage-based-subscriptions].
- **What the merchant sees.**
  - "Shopify allows only one active recurring charge per app at any time".
  - Upgrade proration: $5 + ($15 − $5)×15/30 = $10. A downgrade gives an "application credit".
  - When the spending limit is reached, "no additional charges… until a new billing cycle".
  - Uninstalling stops future cycles, but an already-generated pending charge stays. "Shopify can't remove or cancel a pending third-party app charge". Before payment the developer can issue a credit; after payment, a refund. Refunds are "at the app developer's discretion", and Shopify follows up after 3 days.
  - Shopify-built apps: refund considered if uninstalled within 7 days.

  (`BILL/…/third-party-charges/app-charges.md`, `refund-policy-subscriptions.md`)

---

## 5. Parties and who owes whom

| Flow | Debtor → Creditor | Attester / ledger | Source |
|---|---|---|---|
| Counter sale, cash | Customer → Merchant | Staff (amount received, change); drawer session | `POS/payment-management/cash-payments.md` |
| Cash drawer custody | Staff (opening/closing staff member) accountable → Merchant | Session discrepancy | `register-sessions-*` , `[schema PointOfSaleDevicePaymentSession]` |
| Card present / local method | Customer → Merchant via Shopify Payments (processor); fees Merchant → Platform (netted) | Processor / wallet | `card-payments.md`, `accepting-local-payments.md` |
| External terminal / custom | Customer → Merchant via third party; Shopify only records | Staff "Mark as paid" | `card-payments.md#external-card-reader` |
| Shop Pay Installments | Customer → Affirm; Affirm → Merchant (payout up to 3 business days) | Affirm approval | `shop-pay-installments.md`, `FIN/…/payout-accounts.md` |
| Gift card / store credit | Merchant owes Customer stored value; spending debits it; Merchant → Platform transaction fee on that portion (stores created on or after May 12 2025) | Platform ledger | `gift-cards/*`, `store-credit/*`, `third-party-transaction-fees.md` |
| Tips | Customer → Merchant (card); Merchant ↔ Staff off-platform (**Inference**) | Tips report by staff | `POS/tips.md` |
| Offline card | Customer → Merchant, provisional; on decline Merchant chases Customer | Deferred processor | `offline-payments.md` |
| Capital | Merchant → Lender (WebBank US; YouLend UK) via % of all sales, collected from payouts/bank | Platform computes base | `FIN/shopify-capital/*` |
| Credit | Merchant → Issuer (Celtic Bank) via statement / % of sales | Platform collects | `FIN/shopify-credit/*` |
| Platform billing | Merchant → Shopify (subscription, fees, labels, Tax, Messaging) | Invoice ledger | `BILL/*` |
| App charges | Merchant → Shopify (collector) → App developer (revenue share); refunds Developer → Merchant | Invoice ledger + merchant approval | `dev/docs/apps/launch/billing.md`, `app-charges.md` |
| Negative Payments balance | Merchant → Shopify, added to bills | Balance ledger → invoice | `unknown-charge.md` |
| Cash-in at retailer | Merchant hands cash to Green Dot retailer (agent) → Balance account | Barcode + retailer receipt | `FIN/shopify-balance/adding-cash.md` |

---

## 6. Invariants and rules worth copying

1. **Refund ≤ amount paid with that tender.** Custom-type payments refund only through the custom type (`complete-refund-orders.md`).
2. **A refund, exchange or order edit on a multi-payment order freezes further collection** (`multiple-partial-payments.md`).
3. **Stored-value purchases must be fully paid.** A gift card in the cart blocks partial/unpaid and store credit (`multiple-partial-payments.md`, `redeem-store-credit.md`).
4. **Store credit is applied at maximum, never a chosen partial amount** (`redeem-store-credit.md`).
5. **Cash rounding:** applies only to cash, only when checkout currency = location currency. Full refunds reverse the original rounding. Partial refunds use the return location's rule. Gift-card refunds are unrounded. The *recorded* amount is what staff select (`cash-rounding-on-pos.md`).
6. **One open session per device. A closed session is immutable, and in the API it cannot take payments, refunds or adjustments** (`register-sessions-*`, `[schema PointOfSaleDevicePaymentSessionStatus]`).
7. **Expected close = counted open + net cash payments ± adjustments. Discrepancy = counted − expected,** for both opening and closing (`cash-tracking-reports-by-location.md`).
8. **Every manual drawer open and every cash add/remove can require a reason code; "Other" requires a note** (`register-sessions-in-shopify-pos.md#reason-code`).
9. **Offline exposure is bounded by a per-device daily cap and a per-order cap. A contact identifier is mandatory. Late declines become a receivable against a known customer** (`offline-payments.md`).
10. **Authorization window:** capture after up to 15 minutes. Cancel (fee-free) inside the window, refund outside. Some tenders are never cancellable (`card-payments.md`).
11. **Country/currency lock:** store country = retail location country, and store currency = local currency = payout bank currency for processor-backed in-person payments (`SETUP/compliance.md`).
12. **Lender base = gross daily sales across all channels and tenders, including tax and shipping, not netted for later refunds. Zero sales → zero remittance** (`FIN/shopify-capital/*.md`).
13. **Collection fallback ladder:** Payments balance (several attempts) → bank debit → failure, which counts toward default or locks. Jurisdictions can forbid a rung (Texas) (`united-states.md`, `shopify-credit/manage-account.md`).
14. **Auto-split ordering:** tax set-aside → percentage rules (≤100%) → remainder. One failed leg doesn't block the others (`auto-transfers.md`).
15. **Billing:** prepaid cycles. Thresholds trigger interim bills. Retries continue for 28 days, then freeze. Then a 60-day path to termination. Reactivation requires every invoice paid in sequence (`billing-extensions.md`, `frozen-store.md`).
16. **Credits are category-scoped and future-only** (`credit-notes-and-billing-credits.md`).
17. **Third-party charges need explicit merchant approval of terms. Usage is hard-capped per cycle by a merchant-editable cap, with a 90% warning** [fetched create-usage-based-subscriptions].
18. **Agent cash-in:** single-use code bound to one location and amount, valid 1 h. Attempt expires in 24 h. Rolling 24 h / 7 d / monthly caps, with a per-code minimum count of $500 (`adding-cash.md`).

---

## 7. Tensions and edge cases

- **Remittance on refunded sales.** The Capital base counts refunded and cancelled orders and cash orders. A merchant can owe remittance on revenue they never kept or that never touched the Payments balance (`FIN/shopify-capital/*`). **Inference:** for a COD-heavy market, a sales-percentage lender claim must decide whether "sale" means *ordered*, *delivered*, or *cash collected and remitted by courier*.
- **Fees that survive reversal.** Third-party transaction fees aren't returned on refund or cancel. Delayed capture is the only way to avoid fees on mistakes (`third-party-transaction-fees.md`, `card-payments.md`).
- **Stored value is "free" for some stores and fee-bearing for others,** depending on the store creation date (May 12, 2025) (`third-party-transaction-fees.md`). The cut-off is policy-dated, not structural.
- **Device-local cash sessions.** A lost device or a reinstall can lose session history unless the location pays for POS Pro. Custody evidence then depends on the plan tier (`register-sessions-in-shopify-pos.md`).
- **One drawer per device in the app, many devices per drawer in the API.** The help docs and schema diverge (`cash-drawer.md`, `[schema CashDrawer.pointOfSaleDevices]`).
- **Rounding recorded as selected, not as received.** Staff selecting a rounded suggestion while taking exact cash creates a silent drawer variance (`cash-rounding-on-pos.md`).
- **Offline acceptance is a merchant credit decision.** Shopify doesn't underwrite declines, and the merchant sets the caps. Interac and eftpos are banned offline (`offline-payments.md`).
- **Interac refund can fail after the return completes.** Items leave the order and the amount is entered manually (`refund-interac-payments.md`). Ledger and inventory can disagree.
- **Refund destination asymmetry.** Reloading an existing gift card is allowed only from Shopify Payments transactions. Cash refunds can go only to a *new* gift card (`refund-to-gift-card.md`).
- **Bills vs payouts.** The help docs say bills are paid by card, PayPal or debit mandate, while the schema has `BILLING_DEBIT` from the Payments balance and the docs say negative Payments balances flow into bills. **Inference:** two-way netting exists but is not a merchant-selectable payment method.
- **The freeze cascades across products.** An unpaid bill → frozen store → Credit cards locked. A Capital default → Credit locked. Failed debits for Shopify Services reduce Capital and Credit eligibility (`shopify-credit/manage-account.md`, `shopify-capital/eligibility.md`). The platform-billing ledger is load-bearing for the finance ledgers.
- **Freeze accrual gap.** 28 days of app and transaction charges keep accruing while the store is active and unpaid, and must be paid as a second invoice to reactivate (`app-charges.md#app-charges-frozen-store`).
- **App charges are collected by Shopify, but Shopify can't refund them.** The developer decides (`app-charges.md`).
- **Tips:** card-only. Cash tips are unrecorded and their distribution to staff is unmodelled (`POS/tips.md`).
- **Cash counting tool supports only 9 currencies** (`register-sessions-in-shopify-pos.md`). **Inference:** YER-denominated counting needs custom denominations, and possibly dual-currency drawers (YER/SAR/USD), which `CURRENCY_MISMATCH` errors suggest Shopify forbids per session.

---

## 8. Class-level questions (provider-agnostic)

1. **[information]** How is a tender whose outcome is attested only by a person (cash at a counter, cash collected by a courier, an external terminal, an agent-wallet receipt) represented differently from one attested by a processor? What evidence must accompany it: who, which device or route, when, external reference?
2. **[actors]** What custody units hold staff-attested money (drawer, courier bag, agent float)? How is each bound to a person, a location or route, and a time interval? Who is accountable for a discrepancy, and how is that recorded without rewriting orders?
3. **[lifecycle]** What are the states of a custody interval (open → counted → adjusted → closed)? Which actions are forbidden after close? How is a missed close or a remote close handled?
4. **[rules]** When one obligation is satisfied over time by several arrangements (deposit by wallet, remainder in cash on delivery), what invariant links order total, received, outstanding and refundable per tender? Which events lock further collection?
5. **[lifecycle]** Which arrangements have a separate authorization phase before a final outcome? What window and policy (cancel without fee vs refund) applies, and which arrangements can never be cancelled?
6. **[quality]** When the platform cannot reach the attesting party (offline, agent network down), which outcomes are provisional? What per-transaction and per-device-day limits cap exposure? How does a later failure become a receivable against an identified customer?
7. **[rules]** How is a refund's destination chosen? Options are the original tender (capped at the amount paid, same-instrument rules), stored value (new or existing), or cash. Who must authorize each?
8. **[information]** How are value differences that are not price changes recorded (change given, cash rounding, tips, FX conversion), so that order, tender and custody totals each reconcile independently?
9. **[actors]** Who issues and is liable for stored value (gift card, store credit, platform wallet)? Does spending it create a platform fee or a settlement obligation between merchant and platform?
10. **[extension]** What is the single money stream the platform controls (settlement or payout balance)? What ordered, reversible claims can be netted from it before the merchant is paid (processing fees, reserves, lender remittance, credit repayment, platform bills, merchant-defined splits)?
11. **[lifecycle]** When a claim cannot be collected from that stream, what is the fallback ladder (retry, bank or wallet debit, stored card)? What counts as a failure, and which cross-product consequences follow (lock, freeze, eligibility loss)?
12. **[scope]** Should sales settled outside the platform's money flow (cash, COD, external terminals, agent wallets) count toward obligations computed on sales: financing remittance, platform fees, tax set-aside? How is collection enforced when nothing passes through the platform to deduct from?
13. **[rules]** What does the merchant owe the platform? On what cadence (prepaid cycle vs arrears), with what off-cycle triggers (amount thresholds), in which currency, and with what taxes?
14. **[actors]** How are charges from third parties (apps, partners, couriers, lenders) to merchants consented to, capped per cycle, collected by the platform, remitted to the third party, and refunded? Who bears chargeback and refund risk?
15. **[events]** Which events must every money movement carry so that per-drawer, per-location, per-staff and per-courier reports can be rebuilt? Candidates: device, location, staff, session, reason code, reversal link.
16. **[variability]** How are country and currency constraints modelled (store country, location country, settlement currency)? What happens with multi-currency cash (e.g. YER/SAR/USD in one drawer), denominations, and local rounding rules?
17. **[extension]** How does cash enter the platform's digital ledger through third-party agents (single-use codes bound to amount and location, expiry, rolling limits)? How are pending and available represented?
18. **[quality]** Which records are immutable (closed sessions, captured payments, issued invoices)? What correction instruments exist (reasoned adjustments, refunds, credit notes, category-scoped credits)?
19. **[rules]** Which invariants stop sub-balances (drawer, wallet, store credit, tax set-aside account) from going negative? What happens when a reversal exceeds available funds?
20. **[rules]** Which arrangement-specific constraints restrict basket composition or flow (stored value can't buy stored value; subscriptions card-only; installments not splittable)? How can these be expressed as generic eligibility rules rather than special cases?
