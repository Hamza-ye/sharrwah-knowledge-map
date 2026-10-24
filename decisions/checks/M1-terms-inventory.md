# M1: payment terms inventory, Shopify and Salla

How Shopify and Salla name and bound 15 payment concepts, taken only from evidence already held. Read-only; written 24 October 2026.

## How to read the citations

Paths are short forms of these:

| Short form | Full path |
|---|---|
| `RT:N` | `/home/user/observed-sh/structures/shopify/admin-route-titles-en/items.jsonl`, line N |
| `ROUTER:N` | `/home/user/observed-sh/structures/shopify/admin-router/items.jsonl`, line N |
| `GQL:N` | `/home/user/observed-sh/structures/shopify/admin-graphql-schema/2026-10/items.jsonl`, line N (one type per line) |
| `CLI:N` | `/home/user/observed-sh/structures/shopify/cli-extension-templates/cdn.shopify.com@templates.json/items.jsonl`, line N |
| `HC:file:N` | `/home/user/observed-sh/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/` + file, line N |
| `SA-en:N` / `SA-ar:N` | `/home/user/observed-sa/structures/salla/help-articles/en/texts.jsonl` (or `ar/`), record `position` N |
| `SMENU-en:N` / `SMENU-ar:N` | `/home/user/observed-sa/structures/salla/dashboard-settings-menu/merchant@en/items.jsonl` (or `merchant@ar`), line N |
| `SNAV:N` | `/home/user/observed-sa/structures/salla/dashboard-nav/prod/items.jsonl`, line N |
| `SSTAT:N` | `/home/user/observed-sa/structures/salla/order-statuses/merchant@ar/items.jsonl`, line N |
| `SINV:N` | `/home/user/observed-sa/structures/salla/invoice-settings/public-demo@en/items.jsonl`, line N |
| `SAPI:N` | `/home/user/observed-sa/structures/salla/docs-operations/md-openapi/items.jsonl`, line N (one operation per line) |
| `SSHOW` | `/home/user/observed-sa/structures/salla/showcase-store-payments/com-en-sa/items.jsonl` (51 stores) |
| `AREAS` | `/home/user/sharrwah-knowledge-map/studies/proposals/areas/areas.tsv` |

Quotes are verbatim. The Salla help articles in `en/` are Salla's own English pages. Some carry editors' `[Verify: …]` notes, which I have not quoted.

---

## 1. Payment method, and the ways to pay a platform offers

**Shopify**
- **Names:** "payment methods", managed in "Payments" settings, in an area the help calls "Payment providers". `RT:546` "Payments". `HC:payments.md:3` "they can choose to pay for their order using any of the methods that you've activated".
- **Extent:** cards, wallets, local methods and others.
  - `GQL:2491` `PaymentMethods`: "Some of the payment methods used in Shopify." Values run from VISA and MASTERCARD to PAYPAL, BITCOIN, INTERAC and BANCONTACT.
  - `GQL:1295` `DigitalWallet`: "Digital wallet, such as Apple Pay, which can be used for accelerated checkouts." Values: APPLE_PAY, ANDROID_PAY, GOOGLE_PAY, SHOPIFY_PAY, FACEBOOK_PAY, AMAZON_PAY.
  - `RT:774` "Local payment methods". `RT:563` "Shopify Payments payment methods".
- **Where:** a settings page, Settings > Payments. On the order, `GQL:2306` `Order.paymentGatewayNames`.
- **Area:** A-11 (`AREAS` row A-11).

**Salla**
- **Names:**
  - `SMENU-en:8` "Payments" (`SMENU-ar:8` "المدفوعات").
  - The page is "Payment Methods". `SA-en:565` "Under Settings & Tools, click Payment Methods".
  - Its sections are listed in `SA-en:807`: "Electronic payments — the most secure and the easiest to activate.", "Digital wallets, such as PayPal and stc pay.", "Other payment gateways (Moyasar and HyperPay).", "Buy now, pay later methods, such as Tabby and Tamara.", "Bank accounts."
- **Extent:**
  - `SAPI:212` "Available Payment Methods" lists slugs `credit_card`, `paypal`, `mada`, `free`, `bank` ("BankTransfer"), `cod` ("COD"), `apple_pay`, `stc_pay`, `tamara_installment`, `tabby_installment`.
  - `SSHOW` adds what live stores show. `mada`, `credit_card` and `apple_pay` appear in 51 of 51 stores. The other identifiers are `customer_wallet`, `cod`, `bank`, `mispay_installment`, `madfu_installment`, `emkan_installment`, `paypal` and `mokafaa_alrajhi_loyalty`.
  - Salla's split: `SA-en:921` "Electronic payment includes all payment methods except cash on delivery and bank transfer."
- **Where:** a settings page (Store settings > Payment methods). Checkout options sit on the same page (`SA-en:565`, "Checkout page settings").
- **Area:** A-11. Salla keeps checkout with payments (`AREAS` A-08 note).

## 2. Payment provider, gateway or processor

**Shopify**
- **Names:**
  - "payment provider", "payment gateway" and "third-party provider". `HC:payments/getting-paid.md:3` "All Shopify-supported payment methods rely on third-party providers to process your transactions."
  - `RT:573` "Third-party payment providers". `RT:565` "Shopify Payments".
- **Extent:**
  - `HC:payments/third-party-providers.md:5` "Shopify supports two different types of credit card payment providers: **direct providers** and **external providers**."
  - The table in `HC:payments/getting-paid.md:21` has a "Provider type" column. Its values are "Payment gateway" or "Accelerated checkout".
  - Each transaction names its gateway: `GQL:2447` `OrderTransaction.gateway`, `formattedGateway` and `manualPaymentGateway`.
- **Where:** a settings page. Shopify Payments has its own sub-pages (`RT:565`–`RT:574`).
- **Area:** A-11 for third-party providers. A-12 for Shopify Payments itself.

**Salla**
- **Names:**
  - "Electronic payments", "payment gateway" and "Salla Payments". `SA-en:24` "Electronic Payments is a service provided by Salla that allows your store to process online transactions automatically."
  - `SA-en:565` "merchants using Salla Payments".
  - `SA-en:807` "Other payment gateways (Moyasar and HyperPay)."
- **Extent:**
  - The API records a provider per transaction: `SAPI:208` `payment_method.payment_provider`, "Payment Provider Name", example `salla_pay`.
  - The transactions log shows a "Payment gateway" column (`SA-en:548`).
  - Charity stores have their own gateways. `SA-en:37` is titled "Activating the PayTabs payment gateway for charitable organizations".
- **Where:** a settings page (Payment Methods).
- **Area:** A-11 for outside gateways. A-12 for Salla Payments. A-34 for charity gateways.

## 3. Additional payment methods, or payments apps

**Shopify**
- **Names:** `RT:552` "Additional payment methods". `RT:542` "Add payment method".
- **Extent:**
  - `HC:payments/additional-payment-methods/activate-payment-methods.md:3` "Additional payment methods include options such as PayPal Express Checkout, buy now, pay later services, and regional payment methods."
  - Some of them come as apps. Same file, line 45: "you can also install additional payment providers as apps".
  - The extension points form a CLI group, "Payments extensions" (`"type": "payments_extension"`). It holds six templates: "Card present", "Credit card", "Custom credit card", "Custom onsite", "Offsite" and "Redeemable" (`CLI:70`–`CLI:75`).
  - `HC:payments/shopify-payments/transactions/private-label-credit-cards.md:53` "An offsite payment extension is best for banks that require a hosted payment page."
- **Where:** a settings section (Settings > Payments > Additional payment methods), filled by payments apps and payments extensions.
- **Area:** A-11, with A-24 (apps) and A-25 (extension points).

**Salla**
- **Names:** none. Salla has no "additional payment methods" name. The nearest are "Digital wallets", "Other payment gateways (Moyasar and HyperPay)" and the "Buy now, pay later methods", each switched on with "(Activate)" (`SA-en:807`).
- **Extent:** the providers named on the page. I found no app or extension point through which a third party adds a payment method.
  - Searched the help articles (en) for `payment (gateway )?app|payments app`. The only hit was an accounting app (`SA-en:1277`).
- **Area:** A-11.

## 4. Manual payment methods, and what is recorded when one is used

**Shopify**
- **Names:** `RT:551` and `RT:556` "Manual payment methods". The order actions are "Record payment" (`RT:476`) and "Mark as paid".
- **Extent:**
  - `HC:payments/manual-payments.md:5` "Common types of manual payments include cash on delivery (COD), money orders, and bank transfers."
  - The merchant can also create a custom method. Line 59: "The following names are reserved by Shopify and can't be used:" (written in the file as `can&#39;t`). The reserved names are Bank Deposit, Cash, Cash on Delivery (COD), custom, External Credit, External Debit, Gift Card, Money Order and Store Credit.
  - Each method has "**Additional details**" and "**Payment instructions**" fields (same file).
- **What is recorded:**
  - `HC:payments/manual-payments.md:10` "Orders that accept manual payments are marked as unpaid on the **Orders** page."
  - `HC:fulfillment/managing-orders/payments/deferred-payments.md:129` "**Mark as paid** - Use when you've already received payment for the current order".
  - `HC:payments/partial-payments.md:44` "You can record a manual partial payment, such as a bank deposit or cash on delivery. Manual payments aren't captured by Shopify."
  - The API has `orderMarkAsPaid` and `orderCreateManualPayment` (`GQL:2268`), `Order.canMarkAsPaid` (`GQL:2306`) and `OrderTransaction.manualPaymentGateway` (`GQL:2447`).
- **Where:** set up on the settings page. Recorded through an order action.
- **Area:** A-11 for setup. A-09 for recording.

**Salla**
- **Names:** "Bank transfer" and "Cash on delivery". Salla calls them "manual payment methods" in `SA-en:921`: "the less reliance on manual payment methods".
- **Extent:**
  - `SA-en:565` "Bank transfer (customers transfer payment directly to your account)" and "Cash on Delivery (collected by the shipping company or your own courier)".
  - Bank accounts shown to buyers are separate from the payout account. `SA-en:9` "It is used to enable customers to pay via bank transfer and appears to them during order completion."
  - I found no custom manual method. Searched en for `custom payment method|manual payment method`; it returned only `SA-en:921`.
- **What is recorded:**
  - A receipt and a status. `SA-en:426`, for a manual order: "Select the bank and upload the payment receipt." `SA-en:495` "customers must complete the bank transfer immediately and upload the payment receipt during checkout."
  - The order holds `receipt_image`, "Payment receipt image URL, if available.", and `bank` (`SAPI:5`).
  - Statuses: `SSTAT:2` `payment_pending` "بإنتظار الدفع" and `SSTAT:3` `under_review` "بإنتظار المراجعة". In English, `SINV:12` "Awaiting Payment" and "Waiting For Review".
- **Where:** the settings page (Payment methods > Bank accounts) and the order.
- **Area:** A-11 and A-09.

## 5. Payment capture: capture settings, authorization, authorization expiry

**Shopify**
- **Names:** `RT:548` "Payment capture method". The order action is `RT:470` "Capture payment". The admin intent is `settings/PaymentCaptureMethod` (`ROUTER:1004`).
- **Extent:**
  - Four options. `HC:payments/payment-authorization.md:11`–`14`: "**Automatically at checkout**", "**Automatically when order is fulfilled**", "**Automatically capture per fulfillment (Shopify Plus plan only)**" and "**Manually**".
  - Authorization period, line 32: "provides an authorization period of 7 days". Line 52: after that, "a 1.75% charge applies" on Plus extended authorizations.
  - Schema:
    - `GQL:2452` `OrderTransactionKind` includes AUTHORIZATION, CAPTURE and EMV_AUTHORIZATION.
    - `GQL:2447` `OrderTransaction.authorizationExpiresAt` and `multiCapturable`.
    - `GQL:3220` `ShopifyPaymentsExtendedAuthorization`, with `extendedAuthorizationExpiresAt`.
    - `GQL:2335` `OrderCaptureInput.finalCapture`.
    - `GQL:2380` financial statuses AUTHORIZED and EXPIRED.
- **Where:** a settings section (Settings > Payments) and an order action.
- **Area:** A-11 for the setting. A-09 for capture on the order. A-12 for Shopify Payments' extended authorization.

**Salla**
- **Names:** none.
- **Extent:** no capture setting, authorization or authorization expiry in the held evidence. The only nearby item is the API's `void` on a transaction (term 6).
- **Searched:**
  - Corpus tool: `capture authorization authorize "pre-authorization"`. The only hits were app grants, OAuth and photo capture.
  - Help articles: en `authoriz|\bcapture|pre-auth|hold the amount`; ar `تفويض|حجز المبلغ|الحجز المسبق|التقاط الدفع`.
- **Area:** A-11 (absent).

## 6. Refund, and void

**Shopify**
- **Names:** `RT:481` "Refund". The financial statuses are "Voided" and "Refunded" (`GQL:2380`).
- **Extent:**
  - Refund destinations. `HC:fulfillment/managing-orders/refunding-orders.md:16` "you can refund to the original payment method, [store credit](…), or both". `GQL:2819` `RefundMethodAllocation` has ORIGINAL_PAYMENT_METHODS and STORE_CREDIT.
  - Transaction kinds VOID, REFUND and SUGGESTED_REFUND (`GQL:2452`). Mutations `refundCreate` and `transactionVoid` (`GQL:2268`).
  - Void, `HC:fulfillment/managing-orders/order-status.md:91`: "The authorized payment was voided, which releases the hold on the customer's payment method before it's captured."
  - `HC:fulfillment/managing-orders/canceling-orders.md:66` "If the payment wasn't captured, then the payment status changes to **Voided**."
- **Where:** an order action. A void follows cancelling an order that has not been captured.
- **Area:** A-09.

**Salla**
- **Names:** "Refund", "(Refund the customer)" and "Refund amount". The statuses are "مسترجع" (`restored`, `SSTAT:10`) and "قيد الإسترجاع" (`restoring`, `SSTAT:11`). Staff need the permission `order_refund_payment` (`SNAV:2`).
- **Extent:**
  - `SA-en:804` "Click (Refund the customer), pick the refund method, enter the amount, and confirm. The money is sent back through the original payment gateway."
  - Refund to the wallet, same article: "Credit added to the store wallet can only be spent on another purchase in your store."
  - `SA-en:994` "Automatic refunds are not supported for orders paid through bank transfer." and "Automatic refunds are not supported for cash-on-delivery payments."
  - API, `SAPI:211` "Update Transaction": "This endpoint allows you to `refund`, `void`, or `reverse` a transaction" and "The store must have enough balance to process the refund amounts".
  - `SAPI:9` order action `refund`, "Refund Order".
  - `SAPI:5` `payment_actions.refund_action.can_refund_to_wallet`.
  - Void appears only in the API enum. The help articles have no payment sense of "void"; their only hits are for shipping labels.
- **Where:** an order action, and the electronic payment transactions log (`SA-en:548` "From the transactions list, click Refund.").
- **Area:** A-09.

## 7. Payment method customizations: hide, reorder, rename

**Shopify**
- **Names:** `RT:549` "Payment method customizations". `RT:557` "Payment customizations". In the schema, `GQL:2472` `PaymentCustomization`, "A payment customization.", with `functionId` and `shopifyFunction`.
- **Extent:**
  - `HC:checkout-settings/checkout-customization.md:73` "This payment method customization allows you to sort, reorder, hide, rename payment methods and set payment terms on a checkout".
  - Credit-card fields can be customized only on Plus in the United States and Canada (same file, "Availability based on subscription and geography").
- **Who performs them:**
  - Apps and Functions, switched on in settings. Same file, line 118: "In the **Payment customizations** section, click **Manage**."
  - The Function template is `CLI:58` `payment_customization`, group "Functions".
  - `HC:checkout-settings/customize-checkout-configurations/customization-options.md:213` "Developers can rename, reorder, and sort the payment methods available to customers during checkout using the" Payment Customization Function API.
  - Shopify's own free app, Checkout Blocks, does it too (`HC:checkout-settings/checkout-blocks/customizations/payment-methods.md`).
- **Area:** A-08 and A-11, with A-24 (apps) and A-25 (Functions).

**Salla**
- **Names:** "Payment restrictions" ("قيود الدفع", `SA-ar:165`, titled "إعدادات قيود الدفع").
- **Extent:**
  - `SA-en:923` "Payment restrictions are specific conditions applied to payment methods in your store".
  - When a condition is met, the actions are "Reject the transaction", "Place the order under review" and "Hide the payment method".
  - `SA-en:807` "showing specific methods only when the cart contains products from certain categories, hiding cash on delivery from new customers".
  - I found no reorder or rename of payment methods. Searched en for `(rearrange|reorder|sort|rename|order of)…payment method` and ar for `ترتيب طرق الدفع|إعادة ترتيب…الدفع|تسمية…طرق الدفع`.
- **Who performs them:** the merchant, in settings (`SA-en:923` "Under Settings & Tools, click Payment Restrictions"). No app or function point was found.
- **Area:** A-11.

## 8. Gift cards as a way to pay, their expiry, and Apple Wallet passes

**Shopify**
- **Names:** `RT:301` "Gift cards", `RT:550` "Gift card expiration" and `RT:547` "Apple Wallet Passes". These sit as anchors on the Payments settings page, `ROUTER:1004`, whose eligibility includes the `GIFT_CARDS` permission.
- **Extent:**
  - `GQL:1672` `GiftCard` "A gift card that customers use as a payment method. Stores the initial value, current balance, and expiration date."
  - Expiry units DAYS, MONTHS and YEARS (`GQL:1675`).
  - `HC:products/gift-card-products/modify-gift-card-settings.md:14` "By default, gift cards don't expire because it's illegal in some countries for gift cards to expire."
  - Apple Wallet passes, line 55: "With a pass, customers can check a gift card's balance and redeem the gift card in store."
- **Where:** a settings page. `HC:products/gift-card-products/modify-gift-card-settings.md:24` "In the <strong>Payment configuration</strong> section, click <strong>Gift card expiration</strong>." That section is under Settings > Payments, line 22.
- **Area:** A-32. Shopify files gift cards with products (`AREAS` A-32 note).

**Salla**
- **Names:** "gift card", "Gifting" (`SMENU-en:22` "GiftingNew"; `SMENU-ar:22` "نظام الإهداءجديد") and "Digital card" ("بطاقة رقمية", `SNAV:3`).
- **Extent:**
  - Not a payment method. A gift card is a coupon inside a digital product. `SA-en:1066` "On Salla, a gift card is built from three pieces: fixed-amount coupons, a digital product that hands those coupon codes to the buyer, and the digital gifting app that delivers the card to the recipient."
  - Same article: "The recipient adds products to the cart in your store and applies the coupon at checkout."
  - No gift card expiry setting was found. `SA-en:1066` has no line matching `expir|valid|end date`.
- **Apple Wallet:** used for order tracking, not gift cards. `SA-en:1183` "Orders paid with Apple Pay appear automatically in the customer's Apple Wallet."
- **Where:** Marketing > Gifting, an app, plus coupons.
- **Area:** A-32, with A-05 (coupons). Apple Wallet order tracking is A-09.

## 9. Store credit, and a customer wallet

**Shopify**
- **Names:** "Store credit" (`RT:216`, under customer accounts settings). In the schema, `GQL:3283` `StoreCreditAccount`, "A store credit account contains a monetary balance that can be redeemed at checkout for purchases in the shop." Shopify has no "customer wallet" name. `DigitalWallet` (`GQL:1295`) means buyers' wallets such as Apple Pay.
- **Extent:**
  - It is a payment method. `HC:customers/store-credit.md:3` "display store credit as a payment method at checkout".
  - Expiry is set per issue. Line 90: "Store credit expiration is set per issuance."
  - A refund can go to store credit (`GQL:3303` `StoreCreditRefundInput.expiresAt`).
  - "Store Credit" is a reserved manual-method name (term 4).
- **Where:** Customer accounts settings. `HC:customers/store-credit.md:48` "You can manage whether to display store credit as a payment method from the **Customer accounts** settings".
- **Area:** A-32.

**Salla**
- **Names:** "Customer wallet" (`SMENU-en:20`; `SMENU-ar:20` "محفظة العميل"). It is under Marketing in the nav, at `marketing/customer_wallet` (`SNAV:4`). Its payment identifier is `customer_wallet` (`SSHOW`, 32 of 51 stores).
- **Extent:**
  - `SA-en:36` "The customer wallet is a feature that creates a wallet for each customer where they can keep:" "Cashback balances" and "Refunded amounts".
  - Same article: "The wallet acts as an internal payment method". It needs a custom domain: "your store must be connected to a custom domain".
  - Cashback expiry: "you can set the expiration period for cashback balances".
  - At checkout, `SA-en:461`: "selecting Pay via wallet on the checkout page".
  - API, `SAPI:93` "Deposit to Wallet": "This endpoint will work only if the store has the [Customer Wallet](…) application installed."
- **Where:** a Marketing tool, which is an app with settings.
- **Area:** A-32. Salla files it with marketing (A-05).

## 10. The platform's balance

**Shopify**
- **Names:** "Shopify Payments balance" and "Payout balance".
- **Extent:**
  - `GQL:3193` `ShopifyPaymentsAccount` "Tracks current balances across all supported currencies, payout schedules, and [`ShopifyPaymentsBalanceTransaction`](…) records.", with the field `balance`.
  - `GQL:3197` "A transaction that contributes to a Shopify Payments account balance."
  - `HC:payments/shopify-payments/payouts/view-details.md:3` "The **Payout balance** amount represents the funds that have been captured but not yet added to a scheduled payout, not including reserved funds."
- **Not the same thing:**
  - "Shopify Balance" (`RT:767`) is a separate account. `HC:finance/shopify-balance.md:3` "Shopify Balance is a money management account". It belongs to A-13.
  - An order's unpaid "balance" is different again (`RT:492` "Waive balance").
- **Where:** Payouts (`RT:579`), under Finance.
- **Area:** A-12.

**Salla**
- **Names:** "Balance & billing" (`SMENU-en:7`; `SMENU-ar:7` "الرصيد والفواتير") and "Wallet & Invoices". `SA-en:1240` "three main balances:" "Store balance", "Electronic payments balance" and "Cash on Delivery (COD) payments balance".
- **Extent:**
  - Store balance, `SA-en:1240`: "Used for internal store services, such as:" "Auto-renewing your subscription plan".
  - Electronic payments balance, same article: "This represents your current online sales revenue." Its uses include "Customer refunds". "This balance appears only if Electronic Payments are activated."
  - COD balance, same article: "Shows confirmed COD payments collected from customers."
  - In the UAE, `SA-en:1241` names an "Online-payments balance": "Earnings from your store sales before they are automatically transferred to your bank account."
- **Where:** a settings page (Payment Methods > Wallet & Invoices tab).
- **Area:** A-12 (`AREAS` names "Salla Payments and Salla's wallet"). The store balance also serves A-03 billing, and the COD balance A-10.

## 11. Payout and settlement, and their timing

**Shopify**
- **Names:** "Payouts" (`RT:579`), "Shopify Payments payout schedule" (`RT:568`) and "settlement time".
- **Extent:**
  - `GQL:3229` `ShopifyPaymentsPayoutInterval` "The interval at which payouts are sent to the connected bank account." Values: DAILY, WEEKLY, MONTHLY, MANUAL.
  - `GQL:3223` `ShopifyPaymentsPayout` "A transfer of funds between a merchant's Shopify Payments balance and their [`ShopifyPaymentsBankAccount`](…)".
  - `HC:payments/shopify-payments/payouts/payout-timing.md:15` "You can choose daily, weekly, or monthly payouts". Line 19: "Payout schedules use business days only." Line 35: "Settlement times vary by country, risk level, and the transaction type."
  - Third-party gateways pay out themselves. `HC:payments/getting-paid.md:13` "If customers pay using third-party payment gateways, then you can't view payout information in your Shopify admin."
- **Where:** Shopify Payments settings for the schedule. Finance > Payouts for the payouts.
- **Area:** A-12.

**Salla**
- **Names:** "Payout cycle" or "Transfer Cycle" ("Electronic payment transfer cycle", `SA-en:549`), and "Withdraw Balance".
- **Extent:**
  - `SA-en:807` "Your payout cycle is how often the money you've earned through electronic payments on your store's orders is transferred to your bank account." Also: "The minimum total that can be transferred to a merchant is SAR 100."
  - By plan, same article: "Plus plan: once a week.", "Pro plan: every 48 hours", "Salla Special plan: daily."
  - Store-balance withdrawals, `SA-en:1240`: "Withdrawal requests are confirmed every Monday at 8:00 AM".
  - UAE, `SA-en:1241`: "Weekly on Thursdays", minimum "AED 250".
  - COD balances: term 15.
  - The payout account is set at verification. `SA-en:9` "It is used to transfer your dues from Salla to your bank account".
- **Where:** a settings page (Payment Methods > Electronic payments > Transfer Cycle).
- **Area:** A-12. The payout bank account is with verification, A-18 (`AREAS` A-12 note).

## 12. Fees: transaction fees and provider fees

**Shopify**
- **Names:** "third-party transaction fees", "credit card rate" and "Payment rates" (`RT:571`). The fee pages are titled "Shopify Payments Fees" (`RT:773`).
- **Extent:**
  - `HC:payments/getting-paid.md:11` "you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify".
  - `HC:payments/shopify-payments/payouts/pay-periods-and-fees.md:7` "When you use Shopify Payments, you pay the credit card rate, but you don't pay a transaction fee."
  - Per transaction: `GQL:3605` `TransactionFee` "Transaction fee related to an order transaction.", with `flatFee`, `rate`, `rateName`, `taxAmount` and `type`.
  - Balance transactions carry `fee` and `net` (`GQL:3197`).
  - Store credit is charged too. `HC:customers/store-credit.md:30`: orders paid with store credit "are charged [third-party transaction fees](…)" for stores created on or after May 12, 2025.
- **Where:** plan billing for transaction fees. The Shopify Payments account page for rates.
- **Area:** A-03 for transaction fees and A-12 for Shopify Payments rates.

**Salla**
- **Names:** "payment processing fees", "Fee calculator" and "Online-payment fees".
- **Extent:**
  - `SA-en:24` "The Fee Calculator helps you estimate payment processing fees per order."
  - `SA-en:143` "Payment processing fees VAT is included in the monthly Purchase Invoice issued by Salla."
  - `SA-en:1241` "Online-payment fees are calculated according to the payment services agreement signed during your store verification."
  - Reports, `SA-en:921`: "along with the sales value and fees for each method".
  - COD fees are the carrier's (term 15).
- **Where:** the settings page (Electronic payments > Fee calculator), the monthly purchase invoice and reports.
- **Area:** A-12. Carrier COD fees are A-10.

## 13. Payments per business entity

**Shopify**
- **Names:** `RT:544` "Business Entity Payments", with the context string `RT:545` "Fallback page heading shown while loading payment settings for a specific business entity.". Also "Business Entities" (`RT:523`) and "Selling with multiple entities".
- **Extent:**
  - `GQL:217` `BusinessEntity` "A legal entity through which a merchant operates. … can be associated with its own [`ShopifyPaymentsAccount`](…). [`Market`](…) objects can be assigned to a business entity to determine payment processing and [`Order`](…) attribution."
  - Each order and payout names its entity: `Order.merchantBusinessEntity` (`GQL:2306`) and `ShopifyPaymentsPayout.businessEntity` (`GQL:3223`).
  - `HC:markets/customizations/business-entities.md:6` "A business entity is the legal entity that processes payments for orders in a market."
  - Line 48: "payouts for each entity are deposited into the bank account associated with that entity's Shopify Payments account. Each entity can have its own payout currency and schedule."
  - Plans: `HC:payments/shopify-payments/onboarding/selling-with-multiple-entities.md:3` "available only for organizations on the Shopify Plus and Shopify Enterprise Commerce plan".
- **Where:** Payments settings per entity, organization settings and markets customizations.
- **Area:** A-12, with A-01 (business entities) and A-15 (markets).

**Salla**
- **Names:** nothing like it in the held evidence. A store has one entity type, chosen at verification. `SA-en:1223` "3. Select the business entity type" ("Individual", "Establishment", "Company"), then "4. Enter bank account details".
- **Extent:** payouts go to that one account. `SA-en:1241` "The bank account used during store verification". Separate businesses can only run separate stores (`SMENU-en:4` "Manage stores").
- **Searched:** corpus tool `"business entity" "legal entity" "الكيان"` with `payment payout "المدفوعات"`; help en `legal entit|business entit|…commercial registration|each market…(payment|bank|verification)`.
- **Area:** A-18.

## 14. Payment terms (pay later, due dates) and payment reminders

**Shopify**
- **Names:** `RT:475` "Payment terms" and `RT:541` "Payment reminders".
- **Extent:**
  - `GQL:2503` `PaymentTerms` "Payment terms are created from templates that specify net terms (payment due after a certain number of days) or fixed schedules with specific due dates."
  - `GQL:2514` `PaymentTermsType`: RECEIPT, NET, FIXED, FULFILLMENT, UNKNOWN.
  - `HC:fulfillment/managing-orders/payments/deferred-payments.md:7` "Payment terms let you set the date that payment is due." The table lists "Due on receipt", "Due on fulfillment", "Net term" (net 7 to net 90) and "Fixed term".
  - Reminders, line 150: "You can create up to five payment reminders. Payment reminders can be set to the payment due date, or up to 30 days after the due date."
  - Mutations `paymentTermsCreate`, `paymentReminderSend` and `paymentScheduleCapture` (`GQL:2268`).
  - For B2B: `BuyerExperienceConfiguration.paymentTermsTemplate` (`GQL:219`).
- **Where:** payment terms are an order or draft-order action. Reminders are set in Settings > Notifications (`deferred-payments.md:157`).
- **Area:** A-09 and A-23.

**Salla**
- **Names:** no merchant-set payment terms. "Pay later" means outside "Buy now, pay later" providers. On the order there are "Send payment link" and "Extend payment due".
- **Extent:**
  - `SA-en:565` "Salla also supports installment and deferred payment services, including:" Tabby, Tamara, Mispay, Madfu and Emkan.
  - The provider sends the reminders. `SA-en:577` "Tamara sends reminders via SMS and email before each due date."
  - On orders: `SAPI:9` actions `send_payment_link` ("Send payment link") and `extend_payment_due` ("Extend payment due"). `SAPI:5` `pending_payment_ends_at`, "Pending payment expiration value.".
  - `SA-en:911` "You can also send the payment link directly from the dashboard and extend the payment deadline if needed."
- **Searched:** corpus tool `"payment terms" "net 30" "due date" "استحقاق"`. It found only BNPL, Salla's own plan instalments and unrelated uses.
- **Area:** A-11 for BNPL. A-09 for the payment link and deadline.

## 15. Cash on delivery through a courier: who collects, and settlement

**Shopify**
- **Names:** "Cash on Delivery (COD)", a manual method (`HC:payments/manual-payments.md:5`).
- **Extent:**
  - The merchant creates it as a custom manual method. `HC:intro-to-shopify/initial-setup/sell-in-italy/italy-cash-on-delivery.md:10` "You can create COD (Cash on Delivery) as a payment method by following these instructions: [Create a Custom Manual Payment Method](…)."
  - Line 12 points to an app category, "Cash/Collect on Delivery (COD) Apps".
  - Shopify itself has no courier collection or settlement in the held evidence. The order is marked paid by hand (term 4).
- **Searched:** corpus tool `"cash on delivery" COD` with `courier carrier "delivery company" "shipping company"`. It found only gateway labels, Flow fields and app listings. Also grepped the Help Center Markdown.
- **Area:** A-11, with A-10.

**Salla**
- **Names:** "Cash on delivery with Salla shipping labels / waybills" and "COD balance".
- **Who collects:** the carrier. `SA-en:565` "Cash on Delivery (collected by the shipping company or your own courier)".
- **Through Salla's labels** (`SA-en:570`):
  - Carriers: "Aramex", "J&T Express", "AyMakan", "SMSA", "RedBox", "Shipa".
  - Fee: "The shipping company’s COD fee per order is: SAR 8.00 + VAT". "If you charge customers more than the company’s COD fee, the extra amount will be added to your wallet as profit."
  - Cap: "the maximum COD order value is capped at SAR 1,000".
  - Settlement days: "The transfer days for cash on delivery balances from shipping companies that support COD via Salla shipping labels are:" "Sunday" and "Wednesday". "Invoices are issued for orders that have been successfully delivered or shipped."
  - Scope: "This feature is currently available only for stores operating within the Kingdom of Saudi Arabia."
  - The money lands in the COD balance (term 10).
- **Carriers outside Salla's labels** settle on their own terms:
  - `SA-en:234` "cash on delivery amounts are transferred to the merchant every 5 business days".
  - `SA-en:277` "If there are cash on delivery amounts held for you, the invoice total is deducted from them."
  - In the UAE, `SA-en:1241`: "Cash-on-delivery tracking in Wallet is not available for UAE stores currently."
- **Where:** shipping settings (carrier "Shipping rates" tab and the "cash on delivery" settings). The balance is under Wallet & Invoices.
- **Area:** A-10 (`AREAS` A-10 "collecting cash on delivery"), with A-12 for the balance.
