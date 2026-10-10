# A1 — Arrangements: how Shopify models what satisfies a commerce obligation

**Slice:** 84 help-center files (payments overview, getting paid, authorization, partial payments, manual, additional, accelerated, third-party, PayPal, Shop Pay/Protect, Shop Pay Installments (SPI), Shopify Payments (SP) local/managed methods, SP + third-party, dynamic checkout, checkout settings, international payments). All were read in full.
**Out-of-slice anchors**, used only where the slice links to them: `help/manual/fulfillment/managing-orders/order-status.md` (payment-status definitions) and `help/manual/fulfillment/managing-orders/payments/pending-payments.md` (pending restrictions). Both are in the corpus.
**Fetched read-only, not in corpus:** `https://help.shopify.com/en/manual/payments/shopify-payments/local-payment-methods/oxxo` (cited as [fetched:oxxo]). It is the only cash-voucher method and is directly relevant to a cash-heavy market.
Statements are from the docs unless marked **Inference:**.

---

## 0. The model underneath (Inference, synthesised from everything below)

- An **order** creates one monetary obligation (buyer → merchant). It is settled by one or more **transactions**. Each transaction is attached to a **payment method**, which is routed to a **provider/gateway**.
- Each transaction produces an outcome: authorized, captured, pending, expired, voided, refunded, or disputed.
- The order's **payment status** is a roll-up of those transactions. Admin actions (capture, mark as paid, record payment, refund) are moves on transactions, not edits of the order.
- Money movement is a separate layer with three settlement regimes:
  1. Shopify settles (SP payouts).
  2. A third party settles directly to the merchant (gateway, PayPal, Amazon).
  3. The merchant collects offline (manual methods).
- Risk is partitioned per arrangement. It can sit with the card network process, Shopify Protect, PayPal, Amazon, a BNPL lender (Affirm or Klarna), or nobody (non-disputable bank pushes). In the last case the merchant carries it.

---

## 1. OBLIGATIONS

**What creates it.**
- Checkout creates the order. The customer "can choose to pay for their order using any of the methods that you've activated" [help/manual/payments.md].
- Draft orders with **payment terms** create obligations that fall due later and can be paid in parts [help/manual/payments/partial-payments.md].
- Manual methods create an order whose obligation is explicitly open. The merchant can "send an invoice" and later "manually approve the order" [help/manual/payments/manual-payments.md].
- Recurring obligations come from subscriptions:
  - Subscriptions require SP "as your primary payment gateway" [help/manual/payments.md].
  - PayPal needs a billing agreement via "Reference Transactions" [help/manual/payments/paypal/reference-transactions.md].

**Amount composition.**
- SPI thresholds are evaluated on the total "including discounts, shipping, and taxes" [help/manual/payments/shop-pay-installments.md].
- Tips "are part of the order total" and are subject to processing fees. They are calculated on the "subtotal before taxes and shipping", capped at 100% of the order total and at $1000 USD [help/manual/checkout-settings/tips.md].
- Duties attract transaction fees even on test orders [help/manual/checkout-settings/test-orders/processing-test-order.md].

**When it is due.**
- **At checkout** under the default capture policy, "Automatically at checkout" [help/manual/payments/payment-authorization.md].
- **At fulfillment** under capture-at-fulfillment policies, or under "Due on fulfillment" payment terms. With such terms, "Payment is due when the entire order is fulfilled instead of per fulfillment" [help/manual/payments/payment-authorization.md].
- **By a due date** under payment terms. The status `Due` means payment "hasn't yet been captured by the due date" [help/manual/fulfillment/managing-orders/order-status.md].
- **Within a method-specific window** for asynchronous methods:
  - Multibanco: 7 days, or the order is canceled [help/manual/payments/shopify-payments/local-payment-methods/multibanco.md].
  - OXXO: the barcode is valid 5 days, plus up to 3 business days to confirm [fetched:oxxo].
  - ACH: up to 4 business days [help/manual/payments/shopify-payments/local-payment-methods/ach.md].

**Second-order obligations (obligation splitting).**
- With BNPL the buyer's debt moves to a lender:
  - SPI: "Affirm is responsible for collecting payments from your customers, and you aren't at risk if your customers stop making payments" [help/manual/payments/shop-pay-installments/getting-paid.md].
  - Klarna Pay in 30 days: the buyer's 30-day window "starts when you capture the payment, not when the customer places the order" [help/manual/payments/shopify-payments/local-payment-methods/klarna.md].
- Refunding an SPI order as store credit or a gift card "has no impact on the customer's payment schedule or balance with Affirm" [help/manual/payments/shop-pay-installments/customer-experience.md]. The two obligations are decoupled.

**How the amount changes.**
- Capturing less than the full amount gives `Partially paid` [help/manual/fulfillment/managing-orders/order-status.md].
- "The amount that is authorized is the maximum amount that you can capture" [help/manual/payments/payment-authorization.md].
- An accepted post-purchase upsell means "the original order is edited to include the new product" [help/manual/checkout-settings/order-processing.md].
- SPI orders can't be edited. Adding an item creates "an invoice ... for the outstanding balance", which must be paid "using a different payment method because additional invoices aren't supported by Shop Pay Installments" [help/manual/payments/shop-pay-installments/faq.md].
- USDC: "If you edit an order to a higher amount, then an additional credit is generated for any subsequent charge" [help/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md]. This implies the extra amount is a new charge.
- Editing an order re-evaluates PayPal Seller Protection eligibility [help/manual/payments/paypal/paypal-seller-protection.md].
- Changing the shipping address voids Shopify Protect [help/manual/payments/shop-pay/shopify-protect/protect-order-with-shopify-protect.md].

**Reverse obligations.**
- Merchant → buyer refunds. Tips are not included automatically: "you must add the tip amount manually" [help/manual/checkout-settings/tips.md].
- Merchant → Shopify:
  - Fees, and the ACH "$4 USD fee" on failure and "$15 USD fee" on a lost dispute [help/manual/payments/shopify-payments/local-payment-methods/ach.md].
  - The extended-authorization 1.75% fee [help/manual/payments/payment-authorization.md].
  - The MobilePay "49 DKK per month" charge on Shopify bills [help/manual/payments/shopify-payments/local-payment-methods/mobilepay.md].
- Platform → buyer (forced): if Shop Pay payout setup isn't completed "within 21 days of receiving your first payment through Shop Pay, then all payments will be automatically refunded to the customer" [help/manual/payments/shop-pay/activating-shop-pay.md].

**Subscription obligations outlive instruments, but not methods.**
- If a customer deletes a Shop Pay card, linked subscriptions "continue until the customer cancels them" [help/manual/payments/shop-pay/shop-pay.md].
- If the merchant deactivates Shop Pay, subscription payments fail. "After multiple failed billing attempts, the subscriptions are canceled" [help/manual/payments/shop-pay/deactivating-shop-pay.md].

---

## 2. ARRANGEMENTS

### 2.1 Shopify's own taxonomies

Shopify does not use one classification. It uses at least eight overlapping ones.

1. **Admin sections** in Settings > Payments:
   - "Shopify Payments"
   - "Payment providers" (third-party "credit card payment provider")
   - "Additional payment methods"
   - "Manual payment methods"
   - "Payment customizations"

   Sources: [help/manual/payments/additional-payment-methods/activate-payment-methods.md], [help/manual/payments/manual-payments.md], [help/manual/checkout-settings/checkout-customization.md].
2. **Sub-sections inside Shopify Payments ("Manage payment methods")**: "Wallets", "Local payment methods", "Crypto", the "Shop Pay"/"Shop" section, and card types. Sources: [help/manual/payments/accelerated-checkouts/amazonpay/amazon-pay.md], [help/manual/payments/shopify-payments/local-payment-methods/ach.md], [help/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md].
3. **"Provider type"** in the getting-paid table: "Payment gateway" or "Accelerated checkout". It is crossed with **"How you get paid"**: "Through Shopify Payments", "By Amazon", or "By PayPal" [help/manual/payments/getting-paid.md].
   - Oddity: SPI is typed "Payment gateway", while PayPal Express is "Accelerated checkout".
4. **"direct providers"** (pay on your store) versus **"external providers"** (checkout hosted elsewhere) [help/manual/payments/third-party-providers.md].
5. **"primary payment provider"** versus additional. "A primary payment provider processes credit and debit card transactions. Additional payment methods like PayPal process only PayPal payments and don't replace a primary provider." Without one, checkout shows "This store is currently unable to accept payments" [help/manual/payments/troubleshooting.md].
   - There is also a **"secondary gateway"**, kept for legacy subscriptions [help/manual/payments/third-party-providers/updating-third-party-providers.md].
6. **Local payment method subclasses** [help/manual/payments/shopify-payments/local-payment-methods.md]:
   - "Flexible payment options" (Klarna, Meses sin intereses)
   - "Mobile wallet and app-based payments"
   - "Cash and voucher payments" (OXXO)
   - "Bank transfer and direct debit payments"
7. **Accelerated checkout buttons**: "Unbranded" ("Buy it now", which goes to the Shopify Checkout) versus "Branded" (third-party method with prefilled data) [help/manual/online-store/dynamic-checkout.md].
8. **Reserved manual-method names**, which reveal internal tender types: "Bank Deposit, Cash, Cash on Delivery (COD), custom, External Credit, External Debit, Gift Card, Money Order, Store Credit" [help/manual/payments/manual-payments.md].

**Inference:** the real axes underneath are:
- who processes the transaction,
- who settles the funds,
- whether the instrument is held by Shopify (Shop Pay vault) or by a third party,
- whether completion is synchronous,
- whether capture can be separated from authorization.

### 2.2 Behaviour by class

**SP cards** (the "payment gateway")
- Capture: all four capture policies. Authorization lasts 7 days, extendable on Plus.
- Refunds: through SP, deducted from the next payout.
- Currency: multi-currency processing.
- Completion: synchronous.
- Settlement: Shopify payouts. Fees: no third-party transaction fee.
- Risk/disputes: chargebacks are managed in admin. Shopify routes "each payment to the processor most likely to authorize it".
- Sources: [help/manual/payments/payment-authorization.md], [help/manual/payments/getting-paid.md], [help/manual/international/payments.md].

**Third-party card provider** (direct or external; "over 100")
- Capture: per the Shopify capture setting. The authorization period depends on the provider. Expiry warning emails are only sent with SP.
- Refunds: via the provider. Some need provider-side configuration (Authorize.net "Bill To Last Name is required").
- Currency: converted to the store default currency, except with Adyen.
- Completion: can show `Pending` or `Expired`.
- Settlement: the provider pays the merchant. Payout info "can't view ... in your Shopify admin".
- Fees: third-party transaction fees.
- Risk: the provider handles disputes. With Adyen, Shopify's fraud tools are not available.
- Sources: [help/manual/payments/third-party-providers/configuring-providers.md], [help/manual/payments/third-party-providers/set-up-authorize-net.md], [help/manual/payments/third-party-providers/adyen-gateway.md], [help/manual/payments/third-party-providers/updating-third-party-providers.md].

**SP alongside a third-party provider** (hybrid)
- Routing: cards go to the third party with SP as backup ("payment recovery"). Wallets and local methods that the third party lacks go to SP.
- Settlement: split by provider.
- Fees: SP rates "plus a 1.25% premium".
- Risk: Shopify Protect only covers SP transactions.
- Source: [help/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md].

**Wallets** (Apple Pay, Google Pay, Amazon Pay with SP, PayPal Wallet)
- They ride on the card provider.
- Apple Pay needs network tokenization. It shows the "device account number" last four, not the card's.
- Amazon Pay with SP: refunds within 90 days.
- Settlement: "Through Shopify Payments".
- Risk: Amazon handles A-to-z claims (7 days to reply). PayPal Wallet can be eligible for PayPal Seller Protection.
- Sources: [help/manual/payments/accelerated-checkouts/apple-pay.md], [help/manual/payments/accelerated-checkouts/google-pay.md], [help/manual/payments/accelerated-checkouts/amazonpay/amazon-pay.md], [help/manual/payments/getting-paid.md].

**Shop Pay** (Shopify vault and accelerated checkout)
- Funding: cards plus 15 listed SP local methods. It excludes PayPal and Klarna.
- Settlement: SP payouts.
- Risk: Shopify Protect (US only).
- Sources: [help/manual/payments/shop-pay/shop-pay.md], [help/manual/payments/shop-pay/shopify-protect/protect-order-with-shopify-protect.md].

**PayPal Express Checkout** (an "Additional payment method" that renders as an accelerated button)
- Capture: manual capture and refunds need completed account setup.
- Currency: multi-currency orders are reviewed manually by default.
- Settlement: "By PayPal".
- Fees: exempt from third-party fees if SP is primary.
- Risk: PayPal Seller Protection.
- Sources: [help/manual/payments/paypal/set-up-paypal.md], [help/manual/payments/paypal/multicurrency.md], [help/manual/payments/paypal/paypal-seller-protection.md].

**Additional payment methods / payment apps** (BNPL, regional, crypto)
- Capture: if a provider "doesn't support manual payments, then payments on orders processed by that provider are captured automatically".
- Completion: often async. While `Payment pending`, edits, cancels, manual collection and mark-as-paid can be blocked.
- Settlement: the provider settles.
- Fees: third-party fees.
- Risk: depends on the provider. Crypto has "No chargebacks" and "no automatic refunds".
- Sources: [help/manual/payments/payment-authorization.md], [help/manual/payments/additional-payment-methods/cryptocurrency.md], [help/manual/fulfillment/managing-orders/payments/pending-payments.md].

**SP local payment methods**
- Capture: mostly auto-only. BLIK, MB WAY and Przelewy24 can't be captured manually; MobilePay can, but only for the full amount.
- Refunds: usually 180-day windows, and the processing fee is not refunded.
- Currency and eligibility: gated by customer country, currency and market.
- Completion: async via redirect, which produces `Payment pending`.
- Settlement: SP payouts.
- Risk: many methods cannot be disputed.
- Sources: per-method files under help/manual/payments/shopify-payments/local-payment-methods/.

**BNPL/installments**
- SPI is powered by Affirm. The merchant is paid in full at capture, and Affirm carries the credit risk.
- Klarna via SP: Klarna decides disputes.
- Meses sin intereses (MSI): issuer-based credit-card installments in Mexico, MXN only.
- Adyen credit-card installments for Brazil (2–12) and Mexico (3/6/9/12/18).
- Sources: [help/manual/payments/shop-pay-installments/getting-paid.md], [help/manual/payments/shopify-payments/local-payment-methods/installments-with-msi.md], [help/manual/payments/third-party-providers/adyen-gateway.md].

**Manual payment methods** (COD, bank transfer, money order, custom)
- Capture: there is none ("Manual payments aren't captured by Shopify"). The merchant marks the order as paid.
- Refunds: outside Shopify. **Inference:** the docs say nothing about refund mechanics for these methods.
- Currency: multi-currency only with SP plus the international tools. With Adyen they default to the store currency.
- Completion: offline and indefinite.
- Settlement: the merchant collects directly. Fees: "You aren't charged third-party transaction fees".
- Sources: [help/manual/payments/manual-payments.md], [help/manual/payments/partial-payments.md], [help/manual/payments/third-party-providers/adyen-gateway.md].

**Shop Cash** (Shopify-funded reward used as tender)
- It is applied first.
- Refunds go to the Shop Pay method first, and the remainder goes back to the Shop Cash balance.
- Currency: converted at the current rate.
- Settlement: paid out as "Shop Cash credit".
- Merchants "can't opt out".
- Source: [help/manual/payments/shop-cash.md].

**Test payment gateway** (a simulated provider)
- It replaces the card provider. Card number 1 approves, 2 declines, 3 simulates a gateway failure.
- Test orders don't appear in payouts or reports.
- Source: [help/manual/checkout-settings/test-orders/payments-test-mode.md].

### 2.3 Enablement, ordering, restriction

**Enablement paths differ by class.**
- Cards:
  - SP is activated with KYC and 2-step authentication.
  - A third-party provider is chosen via "Switch to a third-party provider" or "See all other providers", followed by credentials.
  - "Only the store owner can add a payment provider" [help/manual/payments/third-party-providers/configuring-providers.md].
- Additional methods: chosen from search by method or provider, then credentials or an app install, then "Manage", then the merchant connects an external account [help/manual/payments/additional-payment-methods/activate-payment-methods.md].
- Wallets: checkboxes under the card provider's "Wallets" [help/manual/payments/accelerated-checkouts/google-pay.md].
- Manual methods: either "suggested" or "custom", each with "Additional details" (shown at checkout) and "Payment instructions" (shown on the order confirmation page) [help/manual/payments/manual-payments.md].
- Local methods: some are on by default (EPS, iDEAL, Klarna, Multibanco, MSI in their home countries). Some go through review (Multibanco approval "up to 48 hours"; Klarna "controls eligibility decisions"). Swish and iDEAL are "automatically reviewed for eligibility on a regular basis" [help/manual/payments/shopify-payments/local-payment-methods/*.md].

**Managed payment methods** [help/manual/payments/shopify-payments/managed-payment-methods.md]
- Auto-activates SP local methods "based on the regions where you sell".
- Requires Shopify Network Intelligence.
- "If you've previously deactivated a local payment method, then managed payment methods doesn't reactivate it."
- Excludes card types, Cash/COD, manual methods, gift cards, custom payment apps, and third-party integrations.
- Won't auto-activate the SP version of a method if a third-party version (for example Klarna) is installed.

**Ordering.**
- Express Checkout buttons "are ordered dynamically to display the fastest checkout method" [help/manual/payments/accelerated-checkouts.md].
- Branded buttons depend on settings, Shop Promise (which prioritises Shop Pay), browser, device and "personal payment history" [help/manual/online-store/dynamic-checkout.md].
- Managed payment methods personalise the order by buyer location, history and local trends, but "Existing customizations are respected" [help/manual/payments/shopify-payments/managed-payment-methods.md].
- Payment customization apps can "sort, reorder, hide, rename payment methods and set payment terms":
  - On non-Plus plans in the US/CA, only non-card methods can be customised.
  - On Plus, card fields and payment terms at checkout can also be customised.
  - Plus custom apps can hide accelerated checkouts via the Payment Customization API.
  - Source: [help/manual/checkout-settings/checkout-customization.md].
- Finland: "a payment method won't be selected by default" [help/manual/payments.md].

**Hard constraints.**
- "You can have only one credit card payment provider activated at a time" [help/manual/payments/third-party-providers/configuring-providers.md].
- Only "one direct third-party payment provider alongside Shopify Payments at a time". This is not available in multi-entity setups [help/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md].
- Stripe is unavailable wherever SP is supported, even if the merchant is ineligible for SP [help/manual/payments/third-party-providers/payment-gateway-availability.md].
- Activating Adyen "deactivates Shopify Payments". Adyen local methods require the Adyen card app as primary [help/manual/payments/third-party-providers/adyen-gateway.md].
- "You must deactivate any conflicting additional payment gateways before you can activate local payment methods" [help/manual/payments/shopify-payments/local-payment-methods.md].
- SPI requires both SP and Shop Pay [help/manual/payments/shop-pay-installments/eligibility.md].
- The provider list is "filtered based on your store's address" [help/manual/payments/third-party-providers/configuring-providers.md].
- PayPal requires the store country to match the PayPal account country [help/manual/payments/paypal/common-issues.md].

---

## 3. AUTHORIZATION & OUTCOMES

**Four stages: authorization, capture, clearing, funding** [help/manual/payments/getting-paid.md].
- Authorization: the issuer checks validity and funds. "No funds are transferred."
- Capture: sends the transaction to the acquirer.
- Clearing: the issuer and the network take their fees.
- Funding: the acquirer takes its fee and pays the merchant account.

**Capture policies** [help/manual/payments/payment-authorization.md]

1. **"Automatically at checkout"** (default).
   - Cards are captured at sale.
   - Some additional methods are captured "when the provider completes payment processing".
2. **"Automatically when order is fulfilled"**.
   - The order is `Authorized` at checkout and captured when the *entire* order is fulfilled within the authorization period.
   - "Partially fulfilled orders won't be captured."
   - The provider "must support authorization periods".
   - It applies only to orders placed after the policy is activated.
   - It is incompatible with fulfillment apps that need a paid status.
   - B2B orders without a valid authorization and "due on fulfillment" terms must be captured manually.
3. **"Automatically capture per fulfillment"** (Shopify Plus only).
   - Line items and their taxes are captured as each item is fulfilled. "shipping, fees, and duties" are captured at final fulfillment.
   - It needs multi-capture support. If the method can't capture multiple partial payments, "payment for the entire order will be captured at the first fulfillment".
   - Discounts: item-level discounts stay in each line. Order-level discounts are "evenly spread across each fulfillment". Shipping discounts are taken at the final capture.
   - Automation is removed if a fulfillment is canceled, payment is captured manually, an item is returned, or the order is partially or fully refunded.
4. **"Manually"**.
   - The merchant captures the full or a partial amount within the authorization period.
   - "multiple partial payments" are possible when "a third-party payment provider that supports that functionality, or you're on Shopify Plus".
   - Stated reasons include:
     - fraud review
     - accounting rules
     - "local regulation that prescribes ... at least one payment method that allows your customer to pay for the order upon delivery"
     - third-party capture apps

- A third-party app that auto-captures should be paired with the manual setting. Running both causes "conflicts and unexpected behavior".
- "Payment capture settings apply only to orders that are placed in your online store. Point of sale (POS) orders aren't affected."
- Adyen offers its own Automatic, Manual and "Capture on fulfillment" options [help/manual/payments/third-party-providers/adyen-gateway.md].

**Authorization periods.**
- SP: "7 days".
- Plus with SP: extended periods.
  - Visa, Mastercard and Amex: "Up to 30 days".
  - Discover and JCB: "Up to 10 days".
  - Diners and China UnionPay: 7 days.
  - Capturing "after the standard 7 day period" adds a 1.75% charge.
  - To avoid that fee, the docs suggest canceling the order and re-creating it.
- Warning email "1 day before an authorization expires". This only works with SP.
- Bank holds can show "up to 30 days" even after capture or cancel.
- Sources: [help/manual/payments/payment-authorization.md].
- The `Expiring` badge appears "two days before the deadline" [help/manual/fulfillment/managing-orders/order-status.md].
- Klarna Pay in 30 days: capture "until midnight ... UTC on the 28th calendar day" from the order, otherwise the payment "expires and becomes void" [help/manual/payments/shopify-payments/local-payment-methods/klarna.md].
- MobilePay: 7 days, no extended authorization, full capture only [help/manual/payments/shopify-payments/local-payment-methods/mobilepay.md].

**Capture-capability matrix (examples).**
- No manual capture: BLIK, MB WAY, Przelewy24.
- Full capture only: MobilePay.
- No partial capture: USDC.
- Auto-capture fallback for additional methods that don't support manual capture.
- Sources: [help/manual/payments/shopify-payments/local-payment-methods/blik.md], [help/manual/payments/shopify-payments/local-payment-methods/mb-way.md], [help/manual/payments/shopify-payments/local-payment-methods/przelewy24.md], [help/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md], [help/manual/payments/payment-authorization.md].

**Asynchronous completion.**
- Redirect methods (Bancontact, EPS, iDEAL, Klarna): "If [method] is still finalizing the transaction when the customer returns to checkout, then their order is created with the **Payment pending** status. This is designed to prevent the customer from getting stuck waiting." The docs warn the merchant to make sure apps and channels check payment status before fulfilling [help/manual/payments/shopify-payments/local-payment-methods/bancontact.md and siblings].
- Pending payments "have an expiry date, which is typically a week". After that the status becomes `Expired` [help/manual/fulfillment/managing-orders/payments/pending-payments.md].
- Customer emails:
  - On success, a "payment ... was received" email.
  - On failure, an email with a "**Pay now** link" to retry.
  - Manual gateways send no email.
  - Source: [help/manual/fulfillment/managing-orders/payments/pending-payments.md].
- Method windows:
  - ACH: up to 4 business days [help/manual/payments/shopify-payments/local-payment-methods/ach.md].
  - Multibanco: 7 days, then canceled [help/manual/payments/shopify-payments/local-payment-methods/multibanco.md].
  - OXXO:
    - Barcode valid 5 days, plus 3 Mexican business days to confirm.
    - Confirmation "can take up to 3 business days after the customer pays".
    - It auto-cancels and releases inventory only "When OXXO is the only payment on the order".
    - Source: [fetched:oxxo].
  - Przelewy24: a canceled bank flow leaves "a temporary pending order ... for up to 60 minutes" [help/manual/payments/shopify-payments/local-payment-methods/przelewy24.md].
  - Adyen local methods (AliPay, WeChat Pay): pending, with most updates "within a few minutes, but some may take up to 10–15 minutes" [help/manual/payments/third-party-providers/adyen-gateway.md].
  - PayPal to an unverified account: "payment is pending", deposit up to 2 business days after verification [help/manual/payments/paypal/set-up-paypal.md].
  - PayPal multi-currency: manual review is the default [help/manual/payments/paypal/multicurrency.md].
  - MB WAY: approval required "within 4 minutes", otherwise there is no order [help/manual/payments/shopify-payments/local-payment-methods/mb-way.md]. This is synchronous by design.

**Inventory and outcomes.**
- "Inventory is held only when the customer submits their payment information. If a payment fails, then the hold is released" [help/manual/checkout-settings.md].
- `Pending` and `Authorized` orders reserve inventory [help/manual/fulfillment/managing-orders/order-status.md].
- Crypto's "longer settlement times ... can cause overselling in flash sales" [help/manual/payments/additional-payment-methods/cryptocurrency.md].

**Partial payments** (Plus) [help/manual/payments/partial-payments.md]
- Applies to orders "with payment terms".
- Tender types:
  - "vaulted credit card" (B2B)
  - "new credit card"
  - "manual payment, such as a bank deposit" (via "Record payment")
- Amounts can be a "Fixed amount" or a "Percentage".
- The order becomes `Partially paid`. The payment method is chosen when the payment is recorded, not when the draft is created.

**Decline and error handling.**
- Hybrid setups have "payment recovery": card declines or errors are retried through SP. It is "not configurable and can't be deactivated", and it applies to cards only [help/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md].
- Adyen anomalies [help/manual/payments/third-party-providers/adyen-gateway.md]:
  - "customer charged but no order": create a draft order and mark it as paid.
  - "charged twice": one capture plus one dangling authorization.
  - "order created but payment declined".
- The abandoned checkout "payment events" and the order timeline are the diagnostic records [help/manual/payments/troubleshooting.md].

**Marking as paid.**
- Manual-method orders sit at `Pending`. After receiving money the merchant marks them as paid [help/manual/payments/manual-payments.md].
- `Paid` = "automatically or manually captured, or the order was marked as paid" [help/manual/fulfillment/managing-orders/order-status.md].

**Test mode.**
- Options are the Test payment gateway, SP test mode, or a third-party test mode.
- While any of them is active, "Customers can't place live orders" [help/manual/checkout-settings/test-orders/payments-test-mode.md].
- The test gateway needs an amount above "$1 USD", is incompatible with POS and subscriptions, and requires a paid plan.
- SP test mode excludes some local methods (iDEAL; Bancontact and Multibanco "don't work" in test mode), POS readers, SPI and PayPal Wallet.
- Shop Pay "can't simulate a test order" [help/manual/payments/shop-pay/activating-shop-pay.md].
- Manual methods "don't support test mode".
- Third-party test-mode orders "aren't considered test orders" and can't be deleted [help/manual/checkout-settings/test-orders/processing-test-order.md].

**Plan gates.**
- Plus only:
  - per-fulfillment capture
  - extended authorization (with SP)
  - partial payments
  - multiple partial captures (unless the third-party provider supports them)
  - card-field and payment-terms customisation
  - custom Shopify Functions apps
  - Sources: [help/manual/payments/payment-authorization.md], [help/manual/payments/partial-payments.md], [help/manual/checkout-settings/checkout-customization.md].
- Basic or higher: payment customization apps, Buy with Prime [help/manual/payments/accelerated-checkouts/amazonpay/buy-with-prime.md].
- Plus and Enterprise: multi-entity [help/manual/payments/shop-pay-installments/eligibility.md].

---

## 4. RECONCILIATION & MONEY MOVEMENT

**Order payment statuses** [help/manual/fulfillment/managing-orders/order-status.md]

- `Pending` has three causes:
  - an async provider is processing,
  - "Payment due later" terms,
  - a manual method.
- `Authorized` is "displayed only if you capture payments manually". It is the cue to capture.
- `Due`: past or at the payment-terms due date.
- `Expiring` is a badge, not a status.
- `Expired` means either the authorization lapsed, or an alternative provider "unable to process the payment".
- `Paid`.
- `Partially paid`.
- `Partially refunded`.
- `Refunded`.
- `Voided`: the authorization is released. It is "separate from a canceled order" and "An order can remain Open while its payment status is Voided."
- `Unpaid` is an aggregate of Authorized, Pending, Expired and Partially paid.

Order archiving: orders that are "paid for and fulfilled" or "fully refunded" archive automatically [help/manual/checkout-settings/order-processing.md].

**Record linkage.**
- The order timeline section "Payment was processed" contains "Information from the gateway" and the **Payment ID**.
- "Only the payment ID is sent to your payment provider". Order number and ID can't be used to match.
- "Authorization keys are available only in your third party payment provider account."
- Source: [help/manual/payments/third-party-providers/updating-third-party-providers.md].
- Adyen `merchantReference` = `{shopId}-{paymentId}`. Adyen's PSP reference "isn't stored in Shopify" [help/manual/payments/third-party-providers/adyen-gateway.md].

**Method labelling on records.**
- The SPI order CSV shows "Shopify Payments" rather than "Shop Pay Installments" [help/manual/payments/shop-pay-installments/activating-shop-pay-installments.md].
- Shop Cash appears as "Shop Cash credit" on payouts. Integrations may need to map `shop_cash` [help/manual/payments/shop-cash.md].
- Apple Pay shows the device account last four [help/manual/payments/accelerated-checkouts/apple-pay.md].

**Who settles the funds.**
- **Shopify (SP payouts):**
  - SP cards, Apple Pay, Google Pay, Amazon Pay with SP, PayPal Wallet (France and US only), Shop Pay, SPI, Shop Cash, local methods, and Buy with Prime ("After payment is captured by Amazon ... next Shopify Payments payout").
  - Sources: [help/manual/payments/getting-paid.md], [help/manual/payments/accelerated-checkouts/amazonpay/buy-with-prime.md].
  - Banks can take "up to five days" after a payout is sent, and "Payouts aren't sent on bank holidays" [help/manual/payments/getting-paid.md].
- **Third party directly:**
  - PayPal Express ("By PayPal"), legacy Amazon Pay ("By Amazon"), third-party card gateways, additional methods.
  - Payout info for these isn't visible in admin [help/manual/payments/getting-paid.md].
- **Merchant directly:** manual methods. "Manual payments aren't captured by Shopify" [help/manual/payments/partial-payments.md].
- **USDC:** either the local-currency SP payout, or a USDC balance that "you must manually claim". Each claim requires reconnecting the wallet [help/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md].
- **Multi-entity:** SPI is "paid out through the Shopify Payments account of the business entity that processed the order, in that entity's payout currency" [help/manual/payments/shop-pay-installments/getting-paid.md].

**Refund money flows.**
- SP refunds are deducted from the next payout.
- Legacy SPI refunds (orders before Aug 29, 2025) could debit the bank. If that failed, the money was recovered later as "Installments Balance Recovery", a payout adjustment [help/manual/payments/shop-pay-installments/getting-paid.md].
- Multibanco refunds: Stripe emails the buyer for an IBAN, then sends a credit transfer. Only after that does the order show Refunded [help/manual/payments/shopify-payments/local-payment-methods/multibanco.md].
- USDC refunds come from the USDC balance, or from the fiat balance converted to USDC [help/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md].
- Processing fees are not returned for EPS, iDEAL, Klarna, Multibanco or ACH. The SPI fee is not returned [respective files].

**Fees as reconciliation items.**
- Third-party transaction fees apply to all non-SP gateways "even when Shopify Payments is activated", except:
  - PayPal, when SP is primary [help/manual/payments/third-party-providers.md];
  - Amazon Pay with SP [help/manual/payments/accelerated-checkouts/amazonpay/amazon-pay.md];
  - manual methods [help/manual/payments/manual-payments.md].
- **Inference:** fee basis = (processor) × (whether Shopify brokered the money). That makes "brokered financially by Shopify" [help/manual/payments/getting-paid.md] a first-class attribute of each transaction.

**Chargeback ledgering under Shopify Protect.**
- The disputed amount and fee are debited, then "immediately reimbursed ... as a credit".
- If the bank rules for the merchant, "Shopify reverses the credit".
- Source: [help/manual/payments/shop-pay/shopify-protect/addressing-chargebacks.md].

---

## 5. PARTIES & LIABILITY

**Parties.**
- Buyer and merchant (the store owner alone controls providers and PayPal details).
- Shopify (platform and SP). Stripe "is Shopify Payments' banking partner".
- Issuer, acquirer and card networks.
- Third-party gateways.
- Wallet operators (Apple, Google, Amazon, PayPal).
- BNPL lenders (Affirm for SPI, Klarna).
- Global-E for Managed Markets.
- Crypto processors.
- Sources: [help/manual/payments/third-party-providers/payment-gateway-availability.md], [help/manual/payments/getting-paid.md], [help/manual/payments/shopify-payments/managed-payment-methods.md].

**Merchant of record.**
- "Managed Markets (merchant of record service)" requires SP [help/manual/payments/third-party-providers/adyen-gateway.md].
- Its cross-border orders are "processed through Managed Markets ... powered by Global-E"; domestic orders go through SP [help/manual/payments/shopify-payments/managed-payment-methods.md].
- **Inference:** otherwise the merchant is the seller of record.

**Who bears risk.**
- **Shopify Protect** (free) [help/manual/payments/shop-pay/shopify-protect/*.md]
  - Covers Shop Pay only, not SPI.
  - Covers fraudulent and unrecognized chargebacks only.
  - Eligibility:
    - US merchant with a US SP account;
    - order is all physical shipped items (no digital or pickup items);
    - fulfilled with valid tracking from a supported carrier "within 7 days" and "in transit ... within 10 days";
    - only the first subscription order;
    - the shipping address was not changed.
  - Managed Markets SP orders are auto-protected.
  - Statuses: "Shopify Protect", "Protected by Shopify Protect", "Not protected by Shopify Protect". It "doesn't prevent orders from being placed".
  - Mutually exclusive with the paid legacy "Fraud Protect", which "can't be reactivated" once deactivated.
- **PayPal Seller Protection**
  - Covers "Unauthorized transaction" and "Item Not Received". INR applies only to claims in PayPal's Resolution Center, not to card chargebacks.
  - Ratings: "Eligible" or "Ineligible".
  - Proof of delivery is required, with signature for orders "of $750 USD or more".
  - "isn't managed by Shopify".
  - Source: [help/manual/payments/paypal/paypal-seller-protection.md].
- **Amazon:** handles A-to-z claims. The merchant has 7 days to respond [help/manual/payments/accelerated-checkouts/amazonpay/amazon-pay.md].
- **Affirm (SPI):**
  - Carries the credit risk.
  - Disputes: the merchant has 15 days for evidence, then Affirm resolves within 15 days, holding the funds for 30 days.
  - "There's no additional cost to you if the customer is refunded."
  - Source: [help/manual/payments/shop-pay-installments/faq.md].
- **Klarna:** "Klarna decides the outcome" and controls eligibility [help/manual/payments/shopify-payments/local-payment-methods/klarna.md].
- **Non-disputable arrangements (the merchant owns complaint handling):**
  - iDEAL ("Customers can't dispute"; complaints to authorities can disable the method).
  - Swish, Przelewy24, Multibanco, USDC.
  - EPS ("no chargeback process").
  - OXXO.
  - Crypto ("No chargebacks").
  - Sources: the respective files; [fetched:oxxo].
- **Disputable but provider-decided:**
  - BLIK (up to 13 months).
  - MB WAY and TWINT (the bank or scheme decides).
  - ACH (60 days, "final and there is no process for appeal").
  - "Shopify isn't liable for chargebacks" [help/manual/payments/shopify-payments/local-payment-methods/ach.md].
- **Adyen merchants:** lose SP dispute management, card-testing protection and fraud analytics. Adyen Support owns payouts, chargebacks and reconciliation [help/manual/payments/third-party-providers/adyen-gateway.md].

**Buyer experience.**
- Payment instructions appear on the order confirmation page for manual methods [help/manual/payments/manual-payments.md].
- Voucher references (Multibanco "reference number, entity number, and correct amount") are injected into emails via `transaction.buyer_pending_payment_instructions` [help/manual/payments/shopify-payments/local-payment-methods/multibanco.md].
- Authorization holds can confuse buyers for "up to 30 days" [help/manual/payments/payment-authorization.md].
- SPI sends reminder emails before each installment. Paid interest isn't refunded [help/manual/payments/shop-pay-installments/customer-experience.md].
- Klarna and Multibanco require an email checkout, not phone-only. Shop Pay won't save details for phone-only contacts [respective files; help/manual/payments/shop-pay.md].

---

## 6. VARIABILITY & EXTENSION POINTS

**By country.**
- SP availability.
- PayPal Express is unavailable in France and the US, where PayPal Wallet via SP is used instead [help/manual/payments/paypal.md].
- PayPal India supports USD only and no domestic INR [help/manual/payments/paypal/paypal-india.md].
- Shop Pay for third-party gateways only in Australia, France and the US [help/manual/payments/shop-pay/activating-shop-pay.md].
- SPI: US, Canada and UK online; US-only at POS; domestic-only [help/manual/payments/shop-pay-installments/*.md].
- Google Pay on SP everywhere except France [help/manual/payments/accelerated-checkouts/google-pay.md].
- Email money transfers are Canada-only [help/manual/payments/manual-payments/email-money-transfers.md].
- A mandatory order-review step in Japan and Europe [help/manual/checkout-settings/order-processing.md].
- Finland: no preselected payment method.

**By currency.**
- "Only stores with Shopify Payments or Adyen as the primary gateway can process payments in a customer's local currency."
- Compatible methods: SP cards, Shop Pay, Apple Pay and Google Pay, PayPal Express.
- Everything else is converted to the store default at checkout, and the order page "doesn't indicate that the order is a multi-currency order".
- Worked example: (price × rate) + conversion fee, e.g. 1.5%, plus optional rounding.
- Source: [help/manual/international/payments.md].
- Local methods are gated by currency and market [help/manual/payments/shopify-payments/local-payment-methods.md].

**By plan:** see §3.

**By entity.**
- SPI eligibility and financing plans are per entity.
- Only SP may be the direct provider in multi-entity setups.
- Sources: [help/manual/payments/shop-pay-installments/eligibility.md], [help/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md].

**By channel.**
- Capture settings don't apply to POS.
- Shop Pay at POS works via a QR code to the Shop website.
- ACH and Bancontact are not available on POS.
- TWINT has a POS QR flow.
- The Buy Button channel has no Apple Pay.
- Accelerated buttons buy a single variant only and ignore cart attributes.
- Sources: [help/manual/payments/payment-authorization.md], [help/manual/payments/shop-pay/shop-pay.md], [help/manual/online-store/dynamic-checkout/compatibility.md], [help/manual/payments/accelerated-checkouts/apple-pay.md].

**By business type.**
- Przelewy24 excludes individuals, sole proprietors, dropshippers, and others [help/manual/payments/shopify-payments/local-payment-methods/przelewy24.md].
- ACH requires more than 100 fulfilled orders [help/manual/payments/shopify-payments/local-payment-methods/ach.md].
- Swish, TWINT, iDEAL and Klarna require policies to be published on the storefront [help/manual/checkout-settings/refund-privacy-tos.md and method files].

**Extension points.**
- Payment apps for card providers and for additional methods. The legacy ActiveMerchant route is retired [help/manual/payments/third-party-providers/configuring-providers.md].
- The Payment Customization API / Shopify Functions [help/manual/checkout-settings/checkout-customization.md].
- Checkout rules and validations, with "Allow all customers to complete checkout" as a fail-open toggle [help/manual/checkout-settings/checkout-customization.md].
- Post-purchase extensions.
- The Shop Pay Wallet API ("Shop Pay on any platform") [help/manual/payments/shop-pay/shop-pay-on-any-platform.md].
- The iOS Buy SDK.
- Liquid `payment_terms` banners [help/manual/payments/shop-pay-installments/product-banner.md].
- Notification Liquid for pending instructions.
- Custom manual methods.
- Shopify Flow and fraud rules alongside Adyen.

---

## 7. INVARIANTS / RULES worth copying

1. **One primary card processor.** The store can't take payments without it. Other arrangements are additive [help/manual/payments/troubleshooting.md], [help/manual/payments/third-party-providers/configuring-providers.md].
2. **Authorized amount ≥ captured amount.** Captures happen inside an authorization window. Capturing beyond 7 days on SP costs 1.75% [help/manual/payments/payment-authorization.md].
3. **Capture policy is snapshotted at order creation.** Capture at fulfillment "only applies to orders placed after the feature is activated" [help/manual/payments/payment-authorization.md].
4. **Capability fallback.**
   - If a method can't do manual capture, it is auto-captured.
   - If it can't do multi-capture, it is captured in full at the first fulfillment.
   - Sources: [help/manual/payments/payment-authorization.md].
5. **Create the order before a slow outcome finalises.** The order then sits in `Payment pending` instead of blocking checkout, and mutations are locked while pending [help/manual/payments/shopify-payments/local-payment-methods/eps.md], [help/manual/fulfillment/managing-orders/payments/pending-payments.md].
6. **Pending has an expiry.** For OXXO, an order whose only tender is OXXO auto-cancels and releases inventory. Mixed-tender orders do not [fetched:oxxo].
7. **Retired providers stay resolvable for refunds.** "Don't uninstall an additional payment method app". Keep old credentials for returns [help/manual/payments/additional-payment-methods/deactivate-payment-methods.md], [help/manual/payments/third-party-providers/configuring-providers.md].
8. **Automation never overrides explicit merchant intent.** Managed methods don't reactivate what the merchant deactivated, and personalisation respects existing customizations [help/manual/payments/shopify-payments/managed-payment-methods.md].
9. **Manual tenders are recorded, never captured.** They carry merchant-supplied instructions shown after checkout. Names that collide with system tenders are reserved [help/manual/payments/manual-payments.md].
10. **Partial payments are fixed or percentage amounts** against an order with payment terms, and they drive `Partially paid` [help/manual/payments/partial-payments.md].
11. **Reconciliation key.** One opaque payment ID per transaction goes to the provider. The order number never does [help/manual/payments/third-party-providers/updating-third-party-providers.md].
12. **Refund caps.**
    - Refunds can't exceed what was effectively paid (the USDC cashback cap).
    - Refund windows are per method: Amazon Pay 90 days; ACH, EPS, iDEAL and Klarna 180 days.
    - Sources: [help/manual/payments/shopify-payments/local-payment-methods/usdc-payments.md], [help/manual/payments/accelerated-checkouts/amazonpay/amazon-pay.md].
13. **Split refunds across tenders in a fixed priority** (Shop Pay method first, then Shop Cash). Partial refunds allow a manual split [help/manual/payments/shop-cash.md].
14. **Test mode is store-wide.** It blocks live card orders. Test transactions are excluded from payouts and reports [help/manual/checkout-settings/test-orders/payments-test-mode.md].

---

## 8. TENSIONS & EDGE CASES

- **FX gap.** A foreign-currency capture uses "the current conversion rate and not the rate at the time of authorization", so "you might lose money" [help/manual/payments/payment-authorization.md]. Non-SP gateways silently convert to the store currency and the order isn't flagged as multi-currency [help/manual/international/payments.md].
- **Overloaded statuses.**
  - `Pending` means three different things: async provider, payment terms, or a manual method [help/manual/fulfillment/managing-orders/order-status.md].
  - The manual-payments page calls these orders both "unpaid" and "Pending" [help/manual/payments/manual-payments.md].
  - `Expired` means either an authorization lapse or provider failure.
  - `Authorized` is said to display "only if you capture payments manually", yet capture-at-fulfillment also leaves orders "Authorized" [help/manual/payments/payment-authorization.md].
- **Circular dependency.** Capture-at-fulfillment is incompatible with fulfillment apps that wait for a paid status. Automatic fulfillment with manual capture requires capturing first [help/manual/payments/payment-authorization.md], [help/manual/checkout-settings/order-processing.md].
- **Fulfilling unpaid orders.** Pending orders are not blocked from fulfillment, so apps must check payment status [help/manual/fulfillment/managing-orders/payments/pending-payments.md].
- **Money without an order, and orders without money** (Adyen): 3DS abandonment, double authorization, late declines. All are repaired manually with draft orders [help/manual/payments/third-party-providers/adyen-gateway.md].
- **Double credit.** An ACH buyer can get both a refund and a won dispute [help/manual/payments/shopify-payments/local-payment-methods/ach.md].
- **Doc contradictions on SPI.**
  - Payouts "adhere to the same payout schedule" [help/manual/payments/shop-pay-installments/getting-paid.md] versus "Custom payout schedules don't affect" them, "You get paid by Affirm" [help/manual/payments/shop-pay-installments/faq.md].
  - Disputes are managed in admin via "Open response" [getting-paid.md] versus "You don't receive a notification in your Shopify admin" [faq.md].
- **Decoupled lender debt.** Store-credit refunds leave the buyer owing Affirm. Interest and the SPI fee are not refunded [help/manual/payments/shop-pay-installments/customer-experience.md].
- **Long tail of buyer payment dates.** Klarna Pay in 30 days with a late capture can push the buyer's due date to "close to 58 days after they placed the order" [help/manual/payments/shopify-payments/local-payment-methods/klarna.md].
- **Refunds outside the system.**
  - After the refund window, refunds happen "outside of Shopify" (Amazon Pay) or via "an external service" (Klarna).
  - Crypto refunds are manual through the gateway.
  - Multibanco refunds wait on the buyer supplying an IBAN.
  - Sources: the respective files.
- **Different method sets per checkout path.** Shop Pay restricts methods per market "at the platform level" (for example, cards only in Germany). The same store therefore offers different arrangements on the Shop Pay path and the standard path [help/manual/payments/shop-pay/shop-pay.md].
- **Feature exclusions by arrangement.**
  - No post-purchase upsells with accelerated, additional, local or installment payments, with subscriptions, or with duties plus multi-currency [help/manual/checkout-settings/order-processing.md].
  - No tips with SPI. Offsite gateways may not recognise the tip line [help/manual/checkout-settings/tips.md].
  - Apple Pay discount codes only work if entered before tapping the button [help/manual/payments/accelerated-checkouts/apple-pay.md].
- **Configuration fragility.**
  - Updating a gateway integration requires re-enabling Shop Pay [help/manual/payments/third-party-providers/updating-third-party-providers.md].
  - With PayPal setup incomplete, the merchant can receive money but can't refund or manually capture [help/manual/payments/paypal/set-up-paypal.md].
  - PayPal is hidden for subscription carts until Reference Transactions are approved, and a denial may not be notified [help/manual/payments/paypal/reference-transactions.md].
  - When PayPal auto-declines multi-currency orders, the merchant "aren't be notified" [help/manual/payments/paypal/multicurrency.md].
- **Mixed tender with an async leg.** If an OXXO leg fails after a gift card leg succeeded, the order stays open with inventory reserved, and the merchant must clean up [fetched:oxxo].
- **Forced reversals by platform rule.** The Shop Pay 21-day setup rule triggers auto-refunds [help/manual/payments/shop-pay/activating-shop-pay.md].

**Inference — implications for Sharrwah (Yemen):**
- The relevant Shopify sub-model is the one without its own processor: one third-party card provider, plus additional and manual methods, with no multi-currency processing, no payout visibility, and order-level "mark as paid".
- COD, bank deposit and wallet-push methods map to manual methods (indefinite `Pending`, no capture, no disputes). OXXO and Multibanco map to vouchers with expiry.
- Shopify's weakest seams are exactly the ones a Yemen launch leans on:
  - refunding manual tenders;
  - mixed tender with an async leg;
  - FX between quote and settlement, which will be acute with dual exchange rates.
- These deserve first-class design.

---

## 9. CLASS-LEVEL QUESTIONS

1. **[information]** What is the unit of satisfaction: a transaction per tender attempt? Which attributes must every transaction carry? Candidates: method, processor, settler, currency, authorized versus captured amount, provider reference, a "brokered by platform" flag.
2. **[lifecycle]** Which arrangements complete asynchronously, and what may and may not happen to the order while an outcome is pending (edit, cancel, fulfill, re-collect, mark paid)?
3. **[rules]** When is an obligation due — at checkout, at fulfillment (whole or per shipment), by a terms date, or within a method window — and who chooses: platform, merchant policy, or the arrangement's capabilities?
4. **[rules]** When a merchant policy needs a capability an arrangement lacks (deferred capture, multi-capture, partial capture), what is the deterministic fallback?
5. **[lifecycle]** How long can an authorization or pending outcome live? What happens automatically at expiry (void, cancel, release inventory), and how does that differ for single-tender and mixed-tender orders?
6. **[information]** How is the order-level payment status derived from transactions? Which states are distinct (authorized, pending, due, expired, voided, partially paid, partially or fully refunded), and which are aggregates ("unpaid")?
7. **[actors]** For each arrangement, who holds the funds between buyer action and merchant payout? Who settles: platform, provider, or merchant-direct?
8. **[actors]** For each arrangement, who carries fraud, credit and dispute risk (platform guarantee, provider protection, lender, issuer process, nobody)? What merchant duties keep the protection valid (fulfillment deadlines, tracking, address immutability)?
9. **[events]** Which external events change an outcome after checkout (provider confirmation, voucher payment, expiry, dispute opened or decided, lender default), and how are they idempotently linked back to the right order and transaction?
10. **[information]** What single opaque key links a platform transaction to the provider's ledger? What provider data is kept versus left in the provider (auth keys, PSP references)?
11. **[variability]** How does the quoted currency relate to the charged and settled currency? Who bears FX between authorization and capture? How is a converted order marked so it is visibly multi-currency?
12. **[rules]** How are refunds constrained per arrangement (windows, non-refundable fees and interest, caps from rewards or cashback, out-of-band refunds for offline tenders)? How are refunds split across multiple tenders?
13. **[scope]** Is BNPL modelled as a payment method or as a second obligation between buyer and lender? What happens to that second obligation on partial refunds, store-credit refunds and order edits?
14. **[lifecycle]** How do order edits that raise the total get funded when the original arrangement can't take another charge (SPI → invoice for a different method)?
15. **[rules]** What constraints govern combining arrangements (one primary card processor, one secondary, conflicting gateways, provider-bundled local methods)? Is there a fallback or retry route on decline?
16. **[extension]** What is the plug-in contract for a new arrangement: capabilities declared (manual capture, multi-capture, refunds, disputes, async, currencies), lifecycle callbacks, buyer-instruction payloads, and the retire/uninstall semantics needed for later refunds?
17. **[variability]** Which arrangement availability is decided by the platform (market, currency, buyer contact type, entity, plan, channel), and which by the merchant (activate, order, hide, rename)? Does automation respect explicit merchant opt-outs?
18. **[events]** What does the buyer receive at each outcome: instructions on confirmation, voucher references, success or failure emails with a retry link? Which arrangements send nothing (manual)?
19. **[quality]** How are test outcomes (approve, decline, gateway error, dispute) simulated per arrangement? How does test mode avoid blocking live sales and polluting payouts and reports?
20. **[scope]** Which arrangements must work offline or in person (POS, COD, voucher at an agent)? Do capture and authorization policies apply to those channels at all?
