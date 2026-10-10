# A2 — Shopify Payments as processor/payment facilitator, and its risk side

Reader A2. Source: Shopify Help Center corpus (downloaded, treated as data) plus the Admin GraphQL 2026-10 money schema extract.

**Citation legend.** All paths are relative to the corpus root (`help/X.md` corresponds to `https://help.shopify.com/en/X`).
- `SP/` = `help/manual/payments/shopify-payments/`
- `CB/` = `help/manual/payments/chargebacks/`
- `FP/` = `help/manual/payments/fraud-prevention/`
- `PO/` = `help/manual/fulfillment/managing-orders/protecting-orders/`
- `schema:X` = type `X` in `scratchpad/schema/admin-2026-10-money.md`
- Pages marked "(outside slice)" were read only to close a gap: `help/manual/payments/payment-authorization.md`, `help/manual/payments/getting-paid.md`, `help/manual/international/pricing/fees.md`, `help/manual/international/pricing/exchange-rates.md`, `help/manual/payments/shop-pay/shopify-protect/*.md`.

Text marked "Inference:" is my own reading and is not stated in the sources.

---

## 0. The shape in one paragraph

Shopify Payments ("an integrated payment gateway offered by Shopify", `SP/onboarding/eligibility.md`) puts a **platform-held merchant balance** between the order and the bank. The merchant is underwritten: they declare their identity, entity, ownership and bank account, and they are monitored continuously. A captured payment becomes a **balance transaction**, recorded as gross amount, fee and net. Balance transactions are batched into **payouts**, which move money to the bank (DEPOSIT) or pull it from the bank (WITHDRAWAL). Refunds, disputes, fees, reserves, holds, lending repayments and platform bills are all further signed entries on the same ledger, and each correction has its own reversal type. Card-network outcomes (authorization, 3DS liability shift, disputes, monitoring programs) arrive from outside the platform. The platform decides how much of the balance is **available**: settlement delay, payout schedule, reserves, holds, the negative-balance threshold, and NDRP enrollment. Card networks and banks decide dispute outcomes. Shopify says it does not decide them and is not liable for them (`CB/../chargebacks.md`).

---

## 1. THE PROCESSOR RELATIONSHIP

**Who is behind it:**
- Processors: "Stripe, PayPal, or Adyen, depending on your region" (`SP/payouts/account-holds.md`). The US and France use several partners, so a merchant can receive more than one payout a day (`SP/payouts/schedule-payouts.md`).
- Banking partners impose KYC "to comply with regulations that are designed to prevent financial crimes" (`SP/onboarding/account-setup.md`).
- Transactions are smart-routed "to the payment processor most likely to authorize them" (`SP/transactions/declined-payments.md`).

**Gates to entry:**
- Supported country; business and products not prohibited (regulated goods, financial services and crypto, adult, pseudo-pharma, gambling, counterfeit; varies by country); compliance with the per-country Terms of Service (`SP/onboarding/eligibility.md`).
- Account representative at least 18. A minor's parent or guardian must be the representative, and other listed people must be at least 13 (`SP/onboarding/eligibility.md`).
- Two-step authentication is mandatory; "payouts might be placed on hold" without it. Only the store owner can activate Shopify Payments (`SP/onboarding/account-setup.md`).

**What is declared:**
- Personal, address and ID data; business information; the phone number shown on the customer's statement; **Business type** and **Store details**; then **Submit for verification** (`SP/onboarding/account-setup.md`).
- Entity forms are enumerated in `schema:ShopifyPaymentsBusinessType` (INDIVIDUAL, SOLE_PROP, LLC, PUBLIC_COMPANY, NON_PROFIT_*, GOVERNMENT, FREE_ZONE_LLC, SOLE_ESTABLISHMENT, …).
- Registered businesses must give a tax ID. An invalid one "can potentially result in failed payouts, and a hold on your ability to accept orders" (`SP/configuring-shopify-payments.md`; `schema:ShopifyPaymentsTaxIdentificationType`).
- Changing the legal name, tax ID or business type "will result in a new legal entity being created" (`SP/configuring-shopify-payments.md`).

**Roles** (`SP/onboarding/account-setup.md`; `SP/onboarding/eu-verification.md`):
- **Account representative**: always a natural person, never a company. For individuals it is the owner-operator; otherwise someone who can "legally bind the business". Being representative is not the same as being a beneficial owner. The role "can't be waived".
- **Owner**: holds 25% or more, directly or indirectly. **Director**. **Executive**.
- Owners are checked against the government registry. Individuals, sole proprietors, public companies and governments are exempt. Entities with no 25% owner verify their directors instead; the UK requires both.
- Mismatches come back pre-filled with "the names that banking partners were expecting". The merchant resolves them by **Digital attestation** or by uploading a document.

**Evidence standards:**
- Documents are accepted only through secure admin banners; those sent by email or chat are "redacted and rendered unusable" (`SP/onboarding/account-setup.md`).
- Colour photographs, not scans; four borders visible; data must match the account.
- Review takes up to 24 hours ("pending"). There is a "maximum number of attempts".
- No PO boxes; legal names only.
- **Proof of Liveness** (selfie plus ID): required by country, owner-only (`SP/onboarding/proof-of-liveness.md`).

**Descriptors** (`SP/configuring-shopify-payments.md`):
- The customer statement name must be 2–19 characters and include the shop, legal or DBA name, or URL. Shopify rewrites an insufficient one to avoid "payout or charge holds".
- The payout statement name is 5–22 Latin characters and defaults to `Shopify`.
- Schema: `schema:ShopifyPaymentsAccount.chargeStatementDescriptor(s)` and `payoutStatementDescriptor`.

**Bank account** (`SP/onboarding/bank-account-requirements.md`):
- Must be a checking or current account on the country's rail (BECS, SEPA with IBAN whitelists, ACH, FPS, SPEI). US merchants can use Shopify Balance.
- Not accepted: savings accounts, flex-currency accounts, money-transfer services, wire-only accounts, prepaid cards.
- The bank may require **debit authorization** details (Stripe ACH IDs, Bacs SUN, SEPA creditor ID of Stripe Payments Europe Ltd, PayPal, Adyen). These cover debiting the merchant "for fees, refunds, or chargebacks".
- Status lifecycle: `schema:ShopifyPaymentsBankAccountStatus` NEW / VALIDATED / VERIFIED / ERRORED.

**Changing the bank account** (`SP/configuring-shopify-payments.md`; `SP/store-currency/payouts-in-multiple-currencies.md`):
- The merchant must confirm the old account number first.
- Payouts pause for 3–5 business days. With Multi-Currency Payouts the pause covers all accounts; it does not apply when switching to Shopify Balance. Adding an account more than 24 hours after setup also triggers the pause.
- Payouts already scheduled go to the old account. "If a scheduled payout fails, then it's automatically retried to your new bank account within 72 hours." Payouts "are created 1–2 days in advance."

**Charging is allowed before payouts are:**
- Merchants "can use it to accept payments right away", but "if Shopify's banking partners require more information… your… account is put on hold" (`SP/payouts/account-holds.md`).
- EU and UK accounts created from June 2026 onward (`SP/onboarding/eu-verification.md`): payouts are paused immediately; charges are paused 30 days after the first order; payments are refunded to customers 90 days after the first order.
- Missing a re-verification deadline pauses payouts, and later charges. Both pauses lift automatically. "Periodic re-verification is a normal part of using Shopify Payments" and requirements "can't be waived".

**Continuous risk review** (`SP/onboarding/acceptable-business-practices.md`):
- Merchants are held to "a higher standard" than the card networks.
- Criteria:
  - account and compliance: tax information, age, address discrepancies;
  - customer practices: listing accuracy, counterfeit, delivery against promises, subscription transparency, dark patterns;
  - credibility: fake reviews and claims;
  - transaction patterns: chargebacks, refunds, fulfilment, "Historical patterns across any businesses that you operate", volume spikes.
- **Action ladder:** custom payout schedule (5–20 business days) → reserves → holds on payouts or charges → document requests → review or termination → "payouts might be suspended or your ability to process charges… deactivated".
- Hold reasons also include supportability, sanctions, and **creditor or legal action** (`SP/payouts/account-holds.md`). A processor is "legally required to place a hold… for the amount specified in the notice", and "Shopify can't remove this type of hold".
- During a hold, checkout usually continues, but "in some cases, your store can't accept new orders". Admin status shows Green, Yellow or Red (`SP/configuring-shopify-payments.md`).

**Exit and re-entry:**
- **Reapplication** (`SP/onboarding/reapplying-to-shopify-payments.md`) requires 6–12 consecutive months on a third-party gateway, a chargeback rate below 1%, prompt tracked fulfilment, "All pending balances are cleared", and no negative balance. Early review is possible after 4 months with zero Shopify Payments chargebacks. A reserve may be attached on approval.
- **Deactivation** (`SP/configuring-shopify-payments.md`) is blocked until Shopify Capital is repaid. It removes cards, wallets and Shop Pay, and deletes market fixed prices (store currency only afterwards).
- A deactivated store still receives pending payouts but can't fix failures (`SP/payouts/payout-timing.md`). It must reopen to answer chargebacks (`CB/chargebacks-in-admin.md`).

**Multiple entities** (`SP/onboarding/selling-with-multiple-entities.md`; Plus and Enterprise only):
- "Each entity has its own Shopify Payments account, payout currency, and bank account."
- Markets decide which entity processes a sale; for POS, the location decides. "Until you assign an entity to a market, that entity won't process any transactions."
- Subscriptions always run through the primary entity.
- Not supported: "split payments between businesses" (marketplace or commission structures), and routing by shipping address.
- Schema: `schema:BusinessEntity.shopifyPaymentsAccount`; `schema:ShopifyPaymentsPayout.businessEntity`.

**Coexisting with a third-party processor** (`SP/using-shopify-payments-with-a-third-party-provider.md`):
- The third party stays primary for cards. Shopify Payments takes Shop Pay, local methods and missing wallets.
- **Payment recovery** retries the third party's declined cards through Shopify Payments; it "isn't configurable and can't be deactivated".
- One third-party provider at most; not available with multiple entities; Shopify Protect covers Shopify Payments transactions only.

**Schema handle.** `schema:ShopifyPaymentsAccount` = {activated, onboardable, country, defaultCurrency, balance: [MoneyV2] (one per currency), bankAccounts, payoutSchedule, payouts, balanceTransactions, disputes}.

---

## 2. OUTCOMES & STATES (how a charge becomes a balance entry)

**Authorization and capture** (`help/manual/payments/payment-authorization.md`, outside slice):
- Capture modes:
  - automatically at checkout (the default);
  - automatically when the whole order is fulfilled;
  - per fulfilment (Plus only);
  - manually.
- The Shopify Payments authorization period is **7 days**.
- **Extended authorization** (Plus plus Shopify Payments): Visa, Mastercard and Amex up to 30 days; Discover and JCB up to 10; Diners and UnionPay 7. "When you manually capture a payment after the standard 7 day period, then a 1.75% charge applies."
- "The amount that is authorized is the maximum amount that you can capture."
- A foreign-currency capture uses the rate at capture, "not the rate at the time of authorization".
- Schema:
  - `schema:OrderTransaction.authorizationExpiresAt`, `manuallyCapturable`, `multiCapturable` and `totalUnsettled`. Inference: `totalUnsettled` is the amount still capturable.
  - `schema:ShopifyPaymentsTransactionSet.extendedAuthorizationSet` is a `schema:ShopifyPaymentsExtendedAuthorization` with `standardAuthorizationExpiresAt` and `extendedAuthorizationExpiresAt`.
  - Transaction kinds (`schema:OrderTransactionKind`): AUTHORIZATION, CAPTURE, SALE, VOID, REFUND, EMV_AUTHORIZATION, CHANGE, SUGGESTED_REFUND.
  - Transaction statuses (`schema:OrderTransactionStatus`): SUCCESS, FAILURE, PENDING, ERROR, AWAITING_RESPONSE, UNKNOWN.
  - Order rollup (`schema:OrderDisplayFinancialStatus`): PENDING, AUTHORIZED, PARTIALLY_PAID, PAID, PARTIALLY_REFUNDED, REFUNDED, VOIDED, EXPIRED.

**Capture is the ledger event.** "Settlement time refers to the amount of time between when a customer's payment is captured and those funds are available to be paid out… recorded in Coordinated Universal Time (UTC)" (`SP/payouts/payout-timing.md`). Currency conversion and fees are also applied at capture (`SP/store-currency/supported-payout-currencies.md`; `help/manual/international/pricing/fees.md`). Inference: an authorization creates no balance entry; a CHARGE balance transaction is created at capture, already carrying its fee and net.

**Outcomes before an order exists:**
- Shopify Payments "can block some high-risk checkout attempts before an order is created". Such an attempt shows "Blocked due to high risk of fraud" and "No payment is captured", and appears under **Abandoned checkouts > Blocked**. IP blocklists last 6–24 hours (`PO/fraud-analysis.md`).
- With **Decline charges that fail CVV verification** or the AVS postal-code equivalent turned on, a failed check means "no order is placed" (`SP/configuring-shopify-payments.md`). Fraud Control checkout rules block checkouts too (`FP/fraud-control-app.md`).
- **Minimum transaction amounts**: USD 0.50, EUR €0.50, GBP £0.30, JPY ¥50, and so on. Below the minimum "the customer can't complete their purchase", to avoid "losses… after accounting for Shopify Payments fees" (`SP/transactions/min-transaction-amounts.md`).

**Declines** (`SP/transactions/declined-payments.md`):
- The issuer decides, and "Most declines are generic".
- Normalized codes: `schema:OrderTransactionErrorCode` (CARD_DECLINED, DO_NOT_HONOR, FRAUD_SUSPECTED, CARD_TESTING, AUTHENTICATION_REQUIRED, AUTHORIZATION_EXPIRED, AMOUNT_TOO_SMALL…).
- Failed attempts can show as pending charges on the customer's account for 3–5 days (`SP/transactions/pending-charges.md`).
- Plus merchants get "smart retries and rerouting" (`FP/preventing-fraud.md`).

**3DS, PSD2 and liability shift** (`SP/transactions/psd2-and-3d-secure-checkout.md`):
- When a payment is "successfully authenticated by 3D secure", "the liability for fraudulent chargebacks or disputes is shifted from merchants to card issuers".
- Issuers can withdraw the shift. Visa's example: more than $7,500 USD in fraudulent chargebacks in a month.
- Shopify Payments "only uses 3D Secure when required by the issuing bank" (**Dynamic 3DS**, `FP/preventing-fraud.md`).
- The **Visa Secure Excessive Fraud Program** (US) removes liability shift on domestic 3DS until the merchant exits (`CB/monitoring-programs.md`).
- `SP/configuring-shopify-payments.md` says more bluntly that with 3DS on "a fraudulent chargeback can't be filed". Treat the liability-shift wording as the precise one.

**Card classification drives price, not state:**
- US **Standard** (consumer) versus **Premium** (commercial cards and Amex) (`SP/transactions/credit-card-rates.md`).
- Domestic, international or EEA. EEA cards are "treated the same way that domestic cards are treated" (`SP/transactions/domestic-international-eu-credit-cards.md`).
- Manual entry costs more. Private label cards on "proprietary networks" can't be processed and need an extension (`SP/transactions/private-label-credit-cards.md`).

**Refund states** (`SP/payouts/refunds.md`; `SP/refunds-troubleshooting.md`):
- A refund is **Pending** for up to 2 business days and reaches the customer in up to 10 business days.
- It can't be canceled, goes only to the original method, and can usually be issued up to 120 days after the sale.
- Failure causes: amount above the original, outside the timeframe, an open chargeback, the customer's instrument can't receive it, a provider error, or an OXXO payment.
- Past the negative-balance threshold the order shows **Refund pending** (see §4).
- Schema: `schema:ShopifyPaymentsRefundSet.acquirerReferenceNumber` (ARN, for Visa and Mastercard).

**Test mode.** "No real payments are captured"; "Simulated transactions don't appear in your payouts or reports" (`SP/testing-shopify-payments.md`). Schema flags: `schema:ShopifyPaymentsBalanceTransaction.test`, `schema:OrderTransaction.test`. Test cards exist for each failure mode, including "Disputed transaction, also known as a chargeback" (4000000000000259).

---

## 3. FEES & CURRENCY

**Fee model** (`SP/onboarding/cost-of-shopify-payments.md`; `SP/../shopify-payments.md`; `SP/payouts/pay-periods-and-fees.md`):
- The card rate depends on the plan. There are "no monthly fees, no hidden fees, and no setup fees".
- No third-party transaction fees apply to Shopify Payments, Shop Pay, Shop Pay Installments or manual methods. PayPal is exempt if Shopify Payments is the primary provider.
- Leaving Shopify Payments brings back "subscription transaction fees".
- Rates are shown as **Domestic** and **Rest of World**.
- Alongside a third-party provider:
  - third-party transactions pay the plan's third-party transaction fee;
  - Shopify Payments transactions (including recovered payments) pay standard rates **plus a 1.25% premium** (`SP/using-shopify-payments-with-a-third-party-provider.md`).
- US: a 1% cross-border fee applies to cards issued outside the US (`SP/transactions/domestic-international-eu-credit-cards.md`).

**Fees that never come back:**
- "No additional transaction fee is incurred" on a refund, "However, the original credit card transaction fee isn't refunded" (`SP/payouts/refunds.md`).
- Currency conversion fees aren't refunded either, but "you're not charged additional conversion fees when you issue a refund or when you receive a chargeback" (`help/manual/international/pricing/fees.md`, outside slice).

**Tax on fees.** In Switzerland, the EU, Australia and Singapore, tax is added to processing fees. A 0% reverse charge applies in the UK and the EU except Ireland (`SP/payouts/pay-periods-and-fees.md`). `schema:TransactionFee` = {amount, flatFee, flatFeeName, rate, rateName, taxAmount, type}, attached as `schema:OrderTransaction.fees[]`. Fees are therefore modelled as rate plus flat fee plus tax, per transaction.

**Three currencies:**
- **Store currency**: "used within your Shopify admin for pricing products and running reports".
- **Payout currency**: "the currency that Shopify Payments uses to deposit money into your bank account" (`SP/store-currency/understanding-store-and-payout-currencies.md`).
- **Presentment currency**: the customer's local currency (`help/manual/international/pricing/fees.md`).
- Schema:
  - `schema:MoneyBag` = {shopMoney, presentmentMoney};
  - `schema:OrderTransaction.settlementCurrency` and `settlementCurrencyRate`. Inference: the currency the transaction settles into on the balance, and the rate used;
  - `schema:Order.presentmentCurrencyCode`.
- The store currency can be changed after the first sale only through Support (`SP/onboarding/account-setup.md`). Side effects: prices keep the number but take the new currency, gift cards in the old currency die, refunds are affected (`SP/store-currency/changing-your-store-currency.md`).

**Conversion timing:**
- "When a customer pays in a currency that's different from your payout currency, a currency exchange rate and conversion fee are applied at the time of payment capture. If you issue a refund, then the refund is processed at the current exchange rate, and no conversion fees are charged" (`SP/store-currency/supported-payout-currencies.md`).
- Chargebacks are converted at the time of the chargeback. "You might receive small adjustments to cover rate fluctuations. These are separate from the chargeback fee" (`CB/chargeback-process.md`).
- "The foreign exchange rate used is always the rate at the time of the transaction" (`help/manual/international/pricing/exchange-rates.md`).
- Schema: `schema:CurrencyExchangeAdjustment` = {originalAmountSet, adjustment, finalAmountSet} on `schema:OrderTransaction.currencyExchangeAdjustment`; balance type `CURRENCY_CONVERSION` (`schema:ShopifyPaymentsTransactionType`).

**Conversion fee:**
- Rates: US 1.5%, France 2%, other regions 2%. PayPal Wallet through Shopify Payments: 3% (US and France only) (`help/manual/international/pricing/fees.md`).
- Calculation changed on April 6, 2026 (`SP/store-currency/currency-conversion-calculation.md`):
  - old: `(Gross order − Shopify Payments fees) × rate ÷ (1 + rate)`, so the effective rate was below the stated rate;
  - new: `gross × rate`.
- The conversion rate is "a mid-market rate, without any markup". The fee is built into converted prices: `(price × rate) × (1 + fee)` (`help/manual/international/pricing/exchange-rates.md`).

**Multi-Currency Payouts (MCP)** (`SP/store-currency/payouts-in-multiple-currencies.md`; `SP/store-currency/supported-payout-currencies.md`):
- Advanced and Plus only, with one bank account per currency. Lower plans are paid in the domestic currency after conversion.
- Fee: Global 1.5% (Advanced) / 1% (Plus); US 1% / 0.75%. It is "based on the payout currency, not whether a currency conversion occurs."
- Orders in a currency with no account go to the **default** account and are converted.
- Refunds and chargebacks are taken "in the same currency as the original order", from that currency's account, or from the default account if none exists.
- Schema: mutation `shopifyPaymentsPayoutAlternateCurrencyCreate` returns `schema:ShopifyPaymentsToolingProviderPayout`, with errors such as `ALTERNATE_CURRENCY_PAYOUT_FAILED_NO_ELIGIBLE_BALANCE`. Inference: an on-demand payout of one currency's balance.

**Multi-entity.** Each entity processes in its domestic currency, "avoiding international and foreign exchange fees" (`SP/onboarding/selling-with-multiple-entities.md`).

---

## 4. BALANCE & PAYOUTS

**Balance buckets** (`SP/payouts/reserves.md`; `SP/payouts/view-details.md`):
- **Payout balance**: "Funds that have been captured but not yet added to a scheduled payout, not including reserved funds."
- **Reserved funds**: "Money that's temporarily held."
- "Your total balance is the sum of your Payout balance and Reserved funds amounts."
- Transactions move through payout status **Pending**, then the payout's status. "The Payout Date for pending transactions is an estimate only."

**Balance transaction model** (`schema:ShopifyPaymentsBalanceTransaction`). The description reads "Records money movement from charges, refunds, payouts, adjustments, or other payment activities. Includes the gross amount, processing fees, and resulting net amount". Fields:
- `amount`, `fee`, `net`, `type`, `sourceType`, `sourceId`, `sourceOrderTransactionId`;
- `associatedOrder` {id, name};
- `associatedPayout` {id, status};
- `adjustmentReason`;
- `adjustmentsOrders[]` {amount, fees, net, orderTransactionId, name, link};
- `transactionDate`, `test`.

`schema:ShopifyPaymentsSourceType` takes CHARGE, REFUND, DISPUTE, ADJUSTMENT, ADJUSTMENT_REVERSAL, SYSTEM_ADJUSTMENT and TRANSFER.

**Transaction types** (`schema:ShopifyPaymentsTransactionType`), my grouping:
- **Core:** CHARGE, REFUND, REFUND_FAILURE, CHARGE_/REFUND_ADJUSTMENT, ADJUSTMENT, CURRENCY_CONVERSION, STRIPE_FEE.
- **Disputes:** DISPUTE_WITHDRAWAL/REVERSAL, CHARGEBACK_FEE/_FEE_REFUND, CHARGEBACK_HOLD/_HOLD_RELEASE, CHARGEBACK_PROTECTION_*, SELLER_PROTECTION_*.
- **Risk:** RESERVED_FUNDS(_WITHDRAWAL/_REVERSAL), RISK_WITHDRAWAL/REVERSAL.
- **Payouts:** TRANSFER, TRANSFER_FAILURE/CANCEL/REFUND, ACH_BANK_FAILURE_DEBIT_FEE.
- **Platform bills:** BILLING_DEBIT, SHIPPING_LABEL*, CUSTOMS_DUTY, IMPORT_TAX, TAX_ADJUSTMENT_*, REFERRAL_FEE.
- **Lending:** LENDING_*, ADVANCE(_FUNDING).
- **Ecosystem:** SHOPIFY_COLLECTIVE_*, MERCHANT_TO_MERCHANT_*, CHANNEL_*, SHOP_CASH_*, BALANCE_TRANSFER_*.
- **Goodwill and collections:** PROMOTION_/MERCHANT_GOODWILL_/ANOMALY_/COLLECTIONS_CREDIT.

Nearly every non-core type has a `_REVERSAL` twin. Inference: the ledger is append-only, and corrections are compensating entries.

**Activity report.** The **Shopify Payments activity report** (`SP/payouts/payouts-activity-report.md`) groups activity "by the type of balance transaction, not by the payment method". A card, a local method and Shop Pay Installments all land in **Charges**. Other groups include Refunds, Disputes ("Chargebacks, dispute holds, dispute fees"), Reserves & Holds ("Reserved funds, risk holds, and related reversals"), Shopify Capital, Duties & Taxes, Shipping, Internal Transfers, Promotions & Credits, Payouts and Other.

**Payout object** (`schema:ShopifyPaymentsPayout`):
- Fields: bankAccount, businessEntity, externalTraceId, gross, net, issuedAt, status, summary, transactionType.
- `transactionType` (`schema:ShopifyPaymentsPayoutTransactionType`) is **DEPOSIT** or **WITHDRAWAL**, so a payout is signed.
- Status (`schema:ShopifyPaymentsPayoutStatus`): SCHEDULED, IN_TRANSIT, PAID, FAILED, CANCELED.
- A balance transaction's payout status (`schema:ShopifyPaymentsBalanceTransactionPayoutStatus`) adds PENDING and ACTION_REQUIRED.
- `schema:ShopifyPaymentsPayoutSummary` gives gross and fee for charges, refunds, adjustments, reservedFunds, retriedPayouts and advance, plus `usdcRebateCreditAmount`.
- Admin statuses (`SP/payouts/view-details.md`):
  - **Scheduled**;
  - **Deposited** ("doesn't mean that you have the funds");
  - **Failed**;
  - **Withdrawn** ("withdrawal request was sent to your bank… only applies in regions where Shopify Payments debits negative balances").

**Timing** (`SP/payouts/payout-timing.md`):
- Settlement is counted in business days from capture, in UTC. Captures from Friday to Sunday are "grouped and sent together as one payout".
- Minimum settlement days: AU 2; most countries 3; HK and SG 4; JP and UAE 5; MX 7. ACH Direct Debit takes up to 4.
- "Refunds and chargebacks can settle faster than charges."
- Below the country's minimum payout amount (e.g. €1), a payout "stays in a pending state".
- Schedule: daily, weekly or monthly (Japan has no daily). A monthly anchor beyond month-end is paid on the last day. Changing the schedule delays pending payouts (`SP/payouts/schedule-payouts.md`; `schema:ShopifyPaymentsPayoutSchedule` {interval DAILY|WEEKLY|MONTHLY|MANUAL, weeklyAnchor, monthlyAnchor}).

**Failed payouts** (`SP/payouts/failed-payouts.md`):
- Reasons include a wrong account, currency mismatch, account type, payee-name mismatch, closed account, and an account "isn't set up for withdrawals".
- A failure can cause an "immediate payout hold, or a hold after multiple consecutive failures". Payouts restart manually, or automatically when the bank account is replaced.
- A failed debit for a negative payout is "attempted two additional times before payouts to that bank account are paused".

**Reserves** (`SP/payouts/reserves.md`):
- Two types: **Fixed amount reserve** (e.g. $1,000 for 120 days) and **Percentage-based reserve** (e.g. 10% of each transaction for 120 days).
- A reserve "generally don't stop you from accepting payments", and its terms arrive by email.
- Triggers: extended billing cycles, elevated chargebacks, refund rate, extended delivery timelines (events, pre-orders), volume surges.
- The ledger records **negative reserve transactions** (withheld) and **positive reserve transactions** (released). An early release produces "a bulk positive reserve transaction", offset later "with equal negative reserve transactions".
- Before expiry, a review can "lift, maintain, reduce, or increase" the reserve. "Some reserves can't be appealed."

**Holds versus reserves.** A hold stops payouts until a cause is resolved (§1). A reserve withholds a defined slice for a defined period. In the ledger, holds appear as RISK_WITHDRAWAL/RISK_REVERSAL and CHARGEBACK_HOLD/_RELEASE; reserves appear as RESERVED_FUNDS_*. Inference from the type names plus `SP/payouts/payouts-activity-report.md`.

**Negative balance and recovery** (`SP/payouts/refunds.md`; `CB/chargeback-process.md`):
- Refunds are "deducted from your next available payout".
- When the balance can't cover a refund or chargeback:
  - in 17–19 listed countries (US, UK, CA, AU and most of the EU) the shortfall is "debited from your bank account… outside your regular payout schedule";
  - elsewhere, it is "deducted from subsequent payouts".
  - The two pages' lists differ: the refunds page includes AT and FR, the chargeback page doesn't.
- A failed debit is retried "after 3 business days". After that, the merchant must change the bank account or repay manually.
- "Each merchant has a dynamic negative balance limit." Beyond it, refunds become **Refund pending**. Funds "aren't returned to the customer until the negative balance is cleared", and refunds then process "in the order they were created".
- A negative balance clears through a bank debit "within 2 business days", same-day or next-day sales, or **Make a payment** by card.
- In HK, JP, RO, SG, MX, and in Europe with a non-Euro bank account, negative balances "are cleared by future sales".
- EU debits rely on the "SEPA mandate" in the Terms of Service. Aged balances go to the "Shopify Recovery team".

---

## 5. DISPUTES & RISK

**Chargeback versus inquiry** (`CB/chargeback-process.md`):
- **Chargeback**: "The disputed amount and chargeback fee are withdrawn immediately." If the merchant wins, both are returned. If they lose, both are lost.
- **Inquiry**: "No money is taken during the investigation." If it goes the customer's way, it "might escalate to a full chargeback".
- Schema: `schema:DisputeType` = CHARGEBACK | INQUIRY. `schema:OrderDisputeSummary.initiatedAs` keeps the original type.

**Lifecycle** (`CB/chargeback-process.md`):
1. The customer disputes the charge with their bank.
2. Funds and the fee are withdrawn.
3. The merchant is notified with a deadline and, where available, an **issuer claim**.
4. The merchant submits evidence, "usually 7-21 days".
5. Card-company review takes "up to 75 days". Inquiries take "65-75 days".
6. The outcome is a win, a "Partial win", or a loss.

Rules around the decision:
- "After the bank or credit card company rules… there's no appeal process and the decision is final."
- After a win, "the customer's bank can dispute the same transaction again" with a new deadline (`CB/resolve-chargeback.md`).
- Each order transaction can be disputed separately, so one order can carry several chargebacks.
- The deadline is in the store's timezone, defaulting to 11:59 PM, with "no exceptions" (`CB/chargebacks-in-admin.md`).

**Statuses:**
- Admin: **open**, **submitted**, **won**, **lost**, **resolved** (NDRP). "Under review" also appears (`CB/chargebacks-in-admin.md`; `CB/resolve-chargeback.md`).
- API (`schema:DisputeStatus`): NEEDS_RESPONSE, UNDER_REVIEW, WON, LOST, ACCEPTED, PREVENTED, CHARGE_REFUNDED.
- Inference mapping: open ↔ NEEDS_RESPONSE; submitted ↔ UNDER_REVIEW. ACCEPTED corresponds to the merchant clicking **Accept chargeback**. CHARGE_REFUNDED plausibly closes an inquiry ended by a full refund. PREVENTED or "resolved" plausibly covers NDRP auto-resolution.

**Reasons:**
- Docs list Fraudulent, Unrecognized, Duplicate, Subscription canceled, Product not received, Product unacceptable, Credit not processed and General (`CB/chargeback-reasons.md`). `CB/chargeback-process.md` says "seven categories".
- `schema:ShopifyPaymentsDisputeReason` adds INCORRECT_ACCOUNT_DETAILS, INSUFFICIENT_FUNDS, BANK_CANNOT_PROCESS, DEBIT_NOT_AUTHORIZED, CUSTOMER_INITIATED and NONCOMPLIANT. Inference: these are bank-debit or local-method dispute reasons.
- `reasonDetails.networkReasonCode` keeps the raw network code.

**Evidence** (`CB/chargeback-process.md`; `CB/chargebacks-in-admin.md`):
- Shopify adds order facts automatically: products, customer, addresses, IP, fulfilment and tracking PDF, refunds, undisputed order history, earlier disputes, and the relevant policy.
- "Your response is submitted to the credit card company on the due date, even if you don't add any evidence yourself." **Submit now** locks the evidence.
- File limits: 2 MB per file, 4 MB in total, one file per evidence type.
- **Accept chargeback**: "you aren't refunded for the chargeback fee" (`CB/resolve-chargeback.md`).
- Schema:
  - `schema:ShopifyPaymentsDisputeEvidence` holds typed slots (refundPolicyDisclosure, cancellationRebuttal, fulfillments[], typed files);
  - `schema:ShopifyPaymentsDispute` = {amount, evidenceDueBy, evidenceSentOn, finalizedOn, initiatedAt, order, reasonDetails, status, type};
  - mutation `disputeEvidenceUpdate(…, submitEvidence)`.

**Refunds and disputes interact:**
- "You can't refund a chargeback after the chargeback process has started" (`CB/chargebacks-in-admin.md`).
- On an inquiry, a full refund means "the cardholder can't initiate a chargeback". A partial refund does not prevent one.
- A chargeback the customer cancels still needs a bank **withdrawal letter**, confirming the funds were "re-debited from the customer's account" and "returned to you". Cancellation takes 30–90 days (`CB/resolve-chargeback.md`).

**Money effects:**
- "If you're using Shopify Payments and you're issued a chargeback, then the amount is deducted from your next available payout" (`CB/../chargebacks.md`).
- After a win, "the full chargeback amount plus the chargeback fee is returned in your next payout" (`CB/resolve-chargeback.md`). `chargebacks.md` instead says "Shopify might refund the chargeback fee depending on your country or region", so the pages are inconsistent.
- If funds are insufficient, the shortfall is debited from the bank or offset against future payouts (§4).
- Ledger types: DISPUTE_WITHDRAWAL, DISPUTE_REVERSAL, CHARGEBACK_FEE, CHARGEBACK_FEE_REFUND, CHARGEBACK_HOLD, CHARGEBACK_HOLD_RELEASE.
- **Chargeback fees** (`CB/chargeback-process.md`): US $15, UK £10, most of the EU €15 (Ireland €15 + 23% VAT), AU $25, NZ $20, JP ¥1,300, MX $200, HK $85, SG $16.35. The NDRP fee table is identical (`CB/network-dispute-resolution-programs.md`).

**Shopify Protect** (`help/manual/payments/shop-pay/shopify-protect/addressing-chargebacks.md`, outside slice):
- Covers fraudulent and unrecognized chargebacks on protected Shop Pay orders.
- The amount and fee are "debited from your account" and then "immediately reimbursed… as a credit". If the bank later rules for the merchant, "Shopify reverses the credit".
- It does not cover other dispute reasons. Only US stores using Shop Pay are covered (`FP/preventing-fraud.md`).
- The legacy paid **Fraud Protect** guaranteed payment on protected orders and handled the chargeback process (`PO/../protecting-orders.md`). Once deactivated, it can't be reactivated.

**Chargeback rate** (`CB/chargeback-process.md`; `CB/chargeback-monitoring.md`):
- The rate is the number of chargebacks in a month divided by **chargeback-eligible transactions** in the same month. "Winning a dispute doesn't remove it."
- Two variants: **Standard chargeback rate**, which excludes network dispute resolution program (NDRP) cases, and **NDRP-inclusive chargeback rate**. The NDRP-inclusive rate "determines Shopify Payments account monitoring, including account warning banners, reserve thresholds, account standing, and eligibility for features such as the Shop app".
- Fraud Control health tiers: **Good standing** below 0.4%, **At risk** 0.4–0.6%, **Elevated risk** above 0.6% of orders (`FP/fraud-control-app.md`).
- "If you receive a high number of chargebacks, then payment processing is deactivated and you might be removed from Shopify Payments" (`CB/chargeback-reasons.md`).

**NDRP** (`CB/network-dispute-resolution-programs.md`):
- Automatic enrollment possible at an NDRP-inclusive rate of 1.5% or more over 90 days. Merchants below a minimum volume are excluded.
- Every new dispute is "resolved automatically, with the full order amount reimbursed to the customer", with no evidence window and no appeal, plus a fee per dispute.
- A 10% payout reserve applies. It can be lifted early if the merchant exits the program.
- If the 90-day rate is still above 1% after the reserve expires, further reserves or holds may follow.
- Exit condition: below 1.00% over 90 days, sustained for 30 consecutive days, while still processing.
- NDRP can be applied after termination to disputes on orders processed before termination.

**Card-network monitoring** (`CB/monitoring-programs.md`):
- **EFWs** (Visa TC40, Mastercard SAFE) can occur on refunded transactions, unless the refund is a reversal within 2 hours of capture. Timeline terms are **Data month** and **Report month**.
- **VAMP** (disputes plus TC40 fraud): "Excessive" at a ratio of 1.5% (2.2% in CEMEA) with a count of 1,500 (150 in CEMEA).
- **Visa Secure Excessive Fraud** (US): $75,000 and 0.9%. The penalty is loss of liability shift.
- **Mastercard ECP**: ECM at 100–299 disputes and 1.5–2.99%; HECM at 300 or more and 3%. Fines escalate to $200,000. Exit takes 3 months below the threshold.
- **MATCH** and **VMSS** are terminated-merchant files. MATCH code 4: chargebacks above 1% of transactions and at least $5,000 in a month. A merchant must be listed "within one business day of termination", for 5 years. "Shopify generally can't process for businesses listed on MATCH."

**Fraud analysis** (`PO/fraud-analysis.md`):
- Per-order **fraud indicators** (AVS, CVV, location versus payment, device and network, multiple cards).
- A **fraud recommendation**: low, medium or high risk, with next-step text ("Consider canceling this order"). It is ML trained across all Shopify stores. There is none for test, free, gift-card-only, POS, B2B or renewal orders.
- Schema: `schema:Order.riskLevel` and `risks`.
- Automation uses the Flow trigger **Order risk analyzed**. Capture workflows require manual capture (`PO/shopify-flow.md`).
- Card testing: authorization holds "can appear on the real cardholder's statement even when no payment is captured", and can still lead to chargebacks (`FP/preventing-fraud.md`).

---

## 6. PARTIES & LIABILITY

- **Platform (Shopify).** Presents itself as the gateway the merchant contracts with, under the Shopify Payments Terms of Service. It collects KYC/KYB data, holds and nets the merchant balance, sets the settlement and payout schedule, reserves and holds, collects negative balances by debit (under the SEPA mandate in the EU) or by offset, and compiles and submits dispute evidence. "Shopify isn't liable for chargebacks… isn't involved in the decision making of chargeback outcomes" (`CB/../chargebacks.md`).
- **Processors** (Stripe, PayPal, Adyen). Run the transactions and bank debits, and must impose creditor holds that only they can lift (`SP/payouts/account-holds.md`; `SP/onboarding/bank-account-requirements.md`).
- **Banking partners.** Set the verification requirements. They also "notify Shopify if your ratios place you at risk for enrollment into VAMP" (`CB/monitoring-programs.md`). Inference: they hold the acquiring role.
- **Issuer.** Approves or declines and decides disputes. "The customer's bank and credit card company make a decision based on the evidence" (`CB/chargeback-process.md`). After 3DS, the issuer carries fraud liability.
- **Networks.** Set monitoring programs, fines and MATCH/VMSS. Processors are "required to follow" them.
- **Merchant.** Merchant of record by implication. Inference: the merchant's legal or DBA name must appear on the customer's statement, and the merchant bears chargebacks, fees and fines. "You are solely responsible for any costs that result from chargebacks" (`FP/fraud-control-app.md`).
- Under Managed Markets, cross-border orders are processed by Global-E (`SP/managed-payment-methods.md`), and Global-E can be the merchant of record (`help/manual/fulfillment/managing-orders/create-orders/international-drafts.md`).
- **Who can act.** Only the store owner can activate the account, edit bank details, view account details, resolve holds, or complete verification (`SP/onboarding/account-setup.md`; `SP/configuring-shopify-payments.md`; `SP/payouts/account-holds.md`; `SP/onboarding/eu-verification.md`).

**Who bears the risk at each stage:**

| Stage | Who bears risk |
|---|---|
| Checkout | The platform can block, and the merchant's rules can block. |
| Authorization | The issuer decides. |
| Authenticated (3DS) | Fraud liability moves to the issuer. |
| Captured | The merchant owns the fee, which is not refundable. |
| In balance (settlement delay or reserve) | The platform holds funds as security against the merchant's future debts. |
| Refund | Paid from the merchant's balance. If short, the merchant's bank is debited or the refund queues as pending. |
| Dispute | The merchant loses the amount and fee unless they win, or unless Shopify Protect covers fraud on protected orders, in which case the platform absorbs it. |
| Network fines and listing | The merchant. |
| Termination | NDRP and MATCH can still apply afterwards. |

---

## 7. RECONCILIATION

**Linking chain:**

`Order` → `OrderTransaction` → `ShopifyPaymentsBalanceTransaction` → `ShopifyPaymentsPayout` → bank deposit.

- `OrderTransaction` carries: id, kind, status, gateway, paymentId, amountSet (MoneyBag), fees[TransactionFee], settlementCurrency/Rate, currencyExchangeAdjustment, parentTransaction, receiptJson, shopifyPaymentsSet.refundSet.acquirerReferenceNumber.
- `ShopifyPaymentsBalanceTransaction` links back through `sourceOrderTransactionId`, `sourceId`/`sourceType` and `associatedOrder`, and carries amount/fee/net.
- `ShopifyPaymentsPayout` is reached through `associatedPayout.id`. It carries gross, net, summary, status, issuedAt, bankAccount, businessEntity and **externalTraceId**.
- The bank deposit is identified by the "Bank reference", also called the Trace ID or "transfer reference number" (`SP/payouts/lower-or-missing-payouts.md`; `SP/payouts/view-details.md`), and by the payout statement name.
- Disputes link through `schema:ShopifyPaymentsDispute.order` and `schema:Order.disputes`.
- Refunds link to the customer's bank through the ARN (`SP/payouts/refunds.md`).
- Adjustments can fan out to several orders through `adjustmentsOrders[]`.

**Merchant-facing artefacts:**
- The order timeline message "[payout amount] will be added to your [date] payout", which reveals the FX rate and fee (`help/manual/international/pricing/fees.md`).
- The payout detail page: an Overview (amount, status, bank, transfer reference, breakdown of charges, refunds, adjustments and reserves) plus a Transactions list (`SP/payouts/view-details.md`).
- **Export payout transactions** (one payout, one deposit) and **Export balance transactions** (a date range). CSV columns: Transaction Date, Type, Order, Card Brand, Card Source, Payout Status, Payout Date, Available On, Amount, Fee, Net. Exports are emailed to the user and the store owner.
- Transaction filters: type, payout status, payment method, card, transaction date, payout date, currency.
- The **Shopify Payments activity report** (`SP/payouts/payouts-activity-report.md`):
  - one report per payout currency;
  - Starting balance, then Balance change from activity (Gross activity, Fees, Payouts, Net amount), then Ending balance;
  - PDF export, custom ranges from January 1, 2025, and a 3-day data delay;
  - "isn't a statement of revenue". Finance reports are order-based and "might use different timing or totals";
  - stated mismatch causes: date ranges and time zones, payout timing, data delay, currency, third-party methods, revenue versus balance.
- The **Payments finance report** shows volume by card type (`SP/transactions/credit-card-rates.md`). The **Chargeback rate** report is under Analytics (`CB/chargeback-monitoring.md`).
- Tax: Shopify files Form 1099-K in the US. Tax detail on fees is available on the Payouts page (`SP/configuring-shopify-payments.md`; `SP/payouts/pay-periods-and-fees.md`).

---

## 8. VARIABILITY

Most of these are cited in the sections above.

- **Country:**
  - availability and the prohibited list;
  - documents and liveness;
  - bank rail, payout currencies, and the processor that performs debits;
  - settlement days and minimum payout (`SP/payouts/payout-timing.md`); no daily payouts in Japan;
  - minimum transaction amounts;
  - chargeback and NDRP fees;
  - debit versus offset recovery (`SP/payouts/refunds.md`);
  - tax and reverse charge on fees (`SP/payouts/pay-periods-and-fees.md`);
  - conversion fee rate; US 1% cross-border fee; US Standard/Premium pricing; EEA cards treated as domestic; PSD2 3DS;
  - the June 2026 EU/UK verification timeline;
  - VAMP thresholds for CEMEA; AusPayNet reviews quarterly (`CB/monitoring-programs.md`);
  - MCP rules, with domestic-only banks in SG, HK and UAE;
  - Shopify Protect is US only.
- **Plan:**
  - card rates;
  - MCP needs Advanced or Plus;
  - multi-entity needs Plus or Enterprise;
  - extended authorization, capture per fulfilment and authorization-rate optimization need Plus (`FP/preventing-fraud.md`);
  - fraud recommendations need Grow or Shopify Payments (`PO/fraud-analysis.md`);
  - Plus contracts are excluded from Shopify Payments alongside a third-party provider.
- **Business type and risk:**
  - the KYB path depends on the entity form;
  - reserve triggers include annual subscriptions, events, custom and pre-order businesses, and volume spikes (`SP/payouts/reserves.md`);
  - settlement time varies by "region, risk level, and the payment method used" (`SP/payouts/payout-timing.md`).
- **Method:**
  - ACH Direct Debit settles in up to 4 business days;
  - OXXO can't be refunded to its original method;
  - local methods need extra approval (`SP/onboarding/account-setup.md`), and managed payment methods switches them on automatically (`SP/managed-payment-methods.md`).

---

## 9. INVARIANTS AND RULES WORTH COPYING

1. **Capture creates the balance entry.** Settlement time is counted from capture, and FX and fees are fixed at capture (`SP/payouts/payout-timing.md`; `SP/store-currency/supported-payout-currencies.md`).
2. **Every balance entry is gross, fee and net, and every payout is a signed DEPOSIT or WITHDRAWAL** (`schema:ShopifyPaymentsBalanceTransaction`; `schema:ShopifyPaymentsPayoutTransactionType`).
3. **Corrections are compensating entries.** There is a `*_REVERSAL` type for each credit or debit type (`schema:ShopifyPaymentsTransactionType`).
4. **Balance has two buckets:** total = **Payout balance** + **Reserved funds**, and reserved funds can't be paid out (`SP/payouts/reserves.md`).
5. **Authorized is the maximum capturable.** Standard authorization lasts 7 days; capturing after 7 days carries a 1.75% surcharge (`help/manual/payments/payment-authorization.md`).
6. **Fees are sunk.** Refunds don't return the processing or conversion fee and add none of their own (`SP/payouts/refunds.md`; `help/manual/international/pricing/fees.md`).
7. **Refunds are irrevocable and go only to the original method** (`SP/payouts/refunds.md`).
8. **A refund is blocked while a chargeback is open.** On an inquiry, a full refund pre-empts the chargeback (`CB/resolve-chargeback.md`).
9. **Chargebacks debit immediately; inquiries don't move money** (`CB/chargeback-process.md`).
10. **Evidence is auto-submitted on the due date. The deadline is hard, and the decision is final** (`CB/chargebacks-in-admin.md`; `CB/chargeback-process.md`).
11. **The chargeback rate counts disputes filed, not disputes lost.** NDRP-resolved disputes are included in the rate that drives standing (`CB/chargeback-process.md`).
12. **NDRP enrollment** at 1.5% or more over 90 days, with a 10% reserve. Exit requires below 1.00% sustained for 30 days (`CB/network-dispute-resolution-programs.md`).
13. **Reapplication** needs 6–12 months of third-party history, a chargeback rate below 1%, and no negative balance (`SP/onboarding/reapplying-to-shopify-payments.md`).
14. **Negative balance:** debit or offset depending on region. A failed debit is retried after 3 business days. Past the dynamic limit, refunds queue FIFO as **Refund pending** (`SP/payouts/refunds.md`).
15. **Bank-change cooling-off:** confirm the old account; pause 3–5 business days; payouts already scheduled go to the old account; a failure is retried to the new account within 72 hours (`SP/configuring-shopify-payments.md`).
16. **Unverified new account (EU/UK, June 2026 onward):** payouts paused from day 0, charges paused at day 30, payments refunded at day 90 (`SP/onboarding/eu-verification.md`).
17. **Weekend capture batching:** Friday–Sunday captures form one payout. Settlement counts business days only (`SP/payouts/payout-timing.md`).
18. **A payout below the country minimum stays pending** (`SP/payouts/payout-timing.md`).
19. **Disputes and refunds settle in the original order currency, against that currency's payout account or the default** (`SP/store-currency/payouts-in-multiple-currencies.md`).
20. **Descriptor integrity:** the customer statement name must identify the merchant (2–19 characters), and the platform auto-corrects it rather than holding funds (`SP/configuring-shopify-payments.md`).

---

## 10. CLASS-LEVEL QUESTIONS FOR SHARRWAH

1. **[lifecycle]** When the platform holds merchant funds, what ledger states can those funds be in (pending settlement, available, reserved, held, in transit, paid, failed, withdrawn), and which events move them between states?
2. **[events]** Which event creates the merchant's receivable: order placed, authorization, capture, fulfilment, or confirmation of a cash or offline settlement? Is that event identical for every payment arrangement, including cash on delivery (COD), bank transfer and wallets?
3. **[information]** What is the atomic ledger entry? Gross, fee, tax-on-fee and net; source type and source id; order link; payout link; currency and rate. Are corrections always new reversal entries rather than edits?
4. **[rules]** How is available balance computed (settlement delay by risk tier and method, minimum payout, reserves, holds), and who can change each term? Which changes can a merchant appeal, and how?
5. **[actors]** Who is the legal counterparty for each obligation?
   - customer to merchant (merchant of record);
   - merchant to platform (fees, debts);
   - platform to processor or bank;
   - courier or COD collector to platform?

   Which of these does Sharrwah itself take on?
6. **[rules]** What must a merchant declare and prove before charges are allowed, and what before payouts? (Shopify separates "can charge" from "can be paid".) What happens to money collected before verification completes: held, refunded at day N?
7. **[lifecycle]** What is the merchant-standing ladder (normal, slowed payouts, reserve, payout hold, charge hold, termination), and which signals feed each step? Is it the platform's own standard or an external one?
8. **[events]** When a refund or dispute exceeds the balance, how is the debt recovered (bank debit under a mandate, offset against future sales, manual payment, collections), and what happens to customer refunds while the debt is open (queued FIFO)?
9. **[scope]** Which dispute channels exist in Sharrwah's arrangements (card chargebacks, wallet disputes, COD refusals, bank-transfer claims, platform-mediated complaints)? Does the platform adjudicate any of them itself, or only relay them?
10. **[information]** For each dispute: type (inquiry or chargeback), reason taxonomy plus raw external code, amount and currency, deadlines, an evidence model with auto-collected order facts, status machine, fee, and final effect on the ledger?
11. **[rules]** Is the dispute or chargeback rate measured on filed disputes or lost disputes? Over what window and denominator? What thresholds trigger which consequences?
12. **[actors]** Where can liability move away from the merchant (authentication, platform protection programs, carrier or COD agent guarantees)? How is that move recorded as a credit and reversal pair?
13. **[variability]** Which terms vary by country, merchant tier or plan, risk level and payment method (fees, settlement days, minimums, debit-versus-offset recovery, payout currencies)? Are they modelled as configuration rather than code?
14. **[information]** Which identifiers must cross every boundary so that order → payment → ledger entry → payout → bank statement reconciles? Examples: payout trace or reference, ARN equivalent, a descriptor the customer recognizes.
15. **[rules]** For multiple currencies (for Yemen this may mean YER at differing rates, plus USD and SAR): in which currency is each entry booked, at which moment is the rate fixed, who bears FX movement between authorization or capture and refund or dispute, and is the conversion fee charged on gross or net?
16. **[extension]** How do non-payment platform charges (shipping labels, duties, subscriptions, lending repayments, referral fees, inter-merchant transfers) net against the same balance without corrupting payment reconciliation?
17. **[quality]** Which reports does each actor need (per-payout export, period activity statement per currency, dispute-rate report), with what data latency? How does the platform explain balance activity versus revenue?
18. **[scope]** Does Sharrwah allow multiple legal entities per store or marketplace splits? (Shopify explicitly refuses "split payments between businesses".) If it does, each entity needs its own KYB, balance, bank account and dispute ledger.
19. **[lifecycle]** What survives termination: pending payouts, disputes on past orders, reserves held "for a specified period", outstanding debts? And what external blacklist or reporting duty (a MATCH analogue) does the platform owe?

Inference for Sharrwah: in markets without reliable bank-debit mandates, Shopify's "All other countries" model is the practical default. In that model, debts are recovered by offsetting future sales, which makes reserves and settlement delays the main protection against loss.
