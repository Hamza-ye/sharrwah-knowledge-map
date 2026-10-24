# 12. Glossary

The words Sharrwah's decision records rely on, each with its extent: what it covers and what it leaves out (`METHOD.md` sections 4 and 6; amendments 2 and 3). A record uses a term only as far as its own Terms table says. When a term's meaning changes here, the records that use it go under review (`METHOD.md` section 10).

**How an entry reads.**
- **Here** is the term's meaning in Sharrwah's records. Where Sharrwah coins a term, a record defines it, and that is a decision, not a claim.
- **Shopify** and **Salla** give each platform's own names and structures. These are facts, each with its source.
- *Interpretation* and *Assumption* mark what is not a fact (`METHOD.md` section 6). *Open* marks what the held evidence doesn't settle, with what would settle it.
- **Used by** names the records.

**Sources.** The short forms are those of `decisions/checks/M1-terms-inventory.md`, whose table names each one's file, plus two:
- `SDS:N`: observed-sa's `structures/salla/docs-dataschemas/definitions/items.jsonl`, line N;
- `STR:payments.json`: observed-sa's `structures/salla/dashboard-translations/en/payments.json`.

The evidence repositories are read at observed-sh `febbf6c` (20 October 2026) and observed-sa `4ca2e89` (12 October 2026). `python3 -I method/inventory_quotes.py architecture/12-glossary.md` checks the quotes.

**Salla's English and Arabic.** Salla's English help articles are Salla's own published translations of Arabic originals, and some carry translators' "[Verify: …]" notes. Where a meaning turns on Salla's wording, the Arabic original is cited too, since the two can differ. For example, the English page gives a carrier's cash-on-delivery fee as "SAR 8.00 + VAT" (`SA-en:570`), where the Arabic gives SMSA's as "8.00 ر.س + 2% من قيمة المعاملة غير شاملة للضريبة" (`SA-ar:878`).

## Money, and who holds it

### sellers' money
- **Here:** the money a buyer pays for a seller's order, from the buyer's payment until the seller has it. The founder's guard of 18 October uses these words (`founder-decisions.tsv`, G1).
- **Covers:** payments for orders by any payment method, and refunds of them.
- **Leaves out:** Sharrwah's own fees (*Sharrwah's fees*); value a seller owes a buyer, such as store credit, which is not money paid in (*stored value*); money products a platform offers sellers, such as loans (area A-13).
- **Shopify:** "The **Payout balance** amount represents the funds that have been captured but not yet added to a scheduled payout, not including reserved funds." (`HC:payments/shopify-payments/payouts/view-details.md:3`)
- **Salla:** the electronic payments balance, "This represents your current online sales revenue." (`SA-en:1240`); in Arabic, "رصيد المدفوعات الإلكترونية متابعة المبالغ المحصلة عبر وسائل الدفع الإلكترونية والرسوم والصافي المستحق للتحويل" (`SA-ar:663`).
- **Used by:** D-001, D-004.

### held through Sharrwah
- **Here:** sellers' money is held through Sharrwah under either of two arrangements, as the founder's guard of 18 October names them (`founder-decisions.tsv`, G1):
  - **A:** Sharrwah itself holds it;
  - **B:** a payment company holds it in an account opened through Sharrwah.

  Nothing else is held through Sharrwah.
- **An account opened through Sharrwah** (B) is one the seller sets up from inside the platform, with the platform's own payment service. **The seller's own account** (C) is one the seller holds with a provider under its own contract, and links to the platform. Both platforms draw this line:
  - **Shopify** sets up its own service inside the admin: "You can activate Shopify Payments from the **Payments** page in your Shopify admin" (`HC:payments/shopify-payments/onboarding.md:3`), to "complete your Shopify Payments account setup" (`HC:payments/shopify-payments/onboarding.md:5`). A third-party provider is linked instead: "Enter your account credentials for the provider that you selected." (`HC:payments/third-party-providers/configuring-providers.md:32`)
  - **Salla's** own service: "Electronic payments is a Salla service that processes payments in your store directly" (`SA-en:807`); "خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر" (`SA-ar:1501`). Its money sits in a balance Salla keeps (`SA-en:1240`), which D-001 classes as A. An outside gateway is linked: "you need the Secret Key from your Moyasar merchant account" (`SA-en:318`); "فستحتاج إلى الحصول على المفتاح السري (Secret Key) وإعدادات API الخاصة بحسابك" (`SA-ar:1064`). Then "payments flow straight through to your account" (`SA-en:318`).
- *Open:* a provider whose onboarding the seller would start from inside Sharrwah, with its contract directly with the seller, would sit on this line. Which side such a provider falls is decided when one is proposed (S-07), and a case that is B goes to the founder.
- **Used by:** D-001, D-004.

### seller's own account
- **Here:** an account the seller holds with a provider or courier under its own contract, linked to Sharrwah with the seller's own credentials, keys or account number. It is option C of D-001. See *held through Sharrwah* for where it ends and B begins.
- **Shopify:** "Enter your account credentials for the provider that you selected." (`HC:payments/third-party-providers/configuring-providers.md:32`)
- **Salla:** a gateway, "you need the Secret Key from your Moyasar merchant account" (`SA-en:318`). A carrier: "The connection is made once the contract between the two parties is in place and your account number is linked in Salla." (`SA-en:277`)
- **Used by:** D-001, D-004.

### at launch
- **Here:** from when Sharrwah first goes live in any market, for as long as the founder hasn't switched A or B on there. Defined for D-001's line.
- *Interpretation:* the line's "at launch" reads as a lasting state, not a single day, because its last sentence ("Switching either on stays yours") is the only way the state ends.
- **Used by:** D-001.

### reserved, not built
- **Here:** for A and B (D-001), nothing that holds money is designed, built, integrated or contracted. The payment boundary (D-002) leaves room for either behind it, and the settlement contract is named there but not designed. **Switching on** A or B in a market is the founder's decision. It can come only after the arrangement is built, with its licence or its processor.
- **Used by:** D-001, D-002.

### custodian
- **Here:** who holds a payment's money at a given time:
  - the provider, on the provider's own record;
  - the courier, for cash it collected on delivery;
  - the seller, where the buyer paid the seller directly.

  D-002 (element 3) defines it, and D-003 keeps sums apart by it.
- **Shopify:** no field names one. Cash taken at the counter is tracked per drawer: "Tracks the balance in a cash drawer for a point of sale device over the course of a shift." (`GQL:318`)
- **Salla:** keeps cash collected on delivery apart in a balance, which "Shows confirmed COD payments collected from customers." (`SA-en:1240`). With its own carriers, a carrier holds the cash until it transfers it: "If there are cash on delivery amounts held for you, the invoice total is deducted from them." (`SA-en:277`)
- *Interpretation:* neither platform names a custodian on each payment. Sharrwah does because, under C, the money for one store's orders sits with several parties at once.
- **Used by:** D-002, D-003.

### platform balance
- **Here:** money a platform keeps for a seller in a balance of its own payment service. In D-001's terms it is A or B, and it is not built at launch.
- **Shopify:** `ShopifyPaymentsAccount`, which "Tracks current balances across all supported currencies, payout schedules" (`GQL:3193`). Shopify Balance is a different product: "Shopify Balance is a money management account" (`HC:finance/shopify-balance.md:3`), in area A-13.
- **Salla:** "three main balances:" "Store balance", "Electronic payments balance" and "Cash on Delivery (COD) payments balance" (`SA-en:1240`). The store balance is "Used for internal store services, such as:" "Auto-renewing your subscription plan" (`SA-en:1240`).
- **Used by:** D-001.

### settlement and payout
- **Here:** settlement is when a provider credits a payment to the seller's account with it. A payout moves money from a balance to the seller's bank account. Under C each provider does both on its own terms, and Sharrwah sends no payouts (D-004).
- **Shopify:** "The interval at which payouts are sent to the connected bank account." (`GQL:3229`); "Settlement times vary by country, risk level, and the transaction type." (`HC:payments/shopify-payments/payouts/payout-timing.md:35`). For other providers it shows none: "If customers pay using third-party payment gateways, then you can't view payout information in your Shopify admin." (`HC:payments/getting-paid.md:13`)
- **Salla:** "Your payout cycle is how often the money you've earned through electronic payments on your store's orders is transferred to your bank account." (`SA-en:807`). The account is set at verification: "It is used to transfer your dues from Salla to your bank account" (`SA-en:9`).
- **Used by:** D-001, D-002, D-003, D-004, D-005.

### provider fees
- **Here:** what a provider or courier charges the seller for a payment: processing fees, a courier's fee for cash on delivery, and tax on them. Payments records them as reported (D-002, D-003). They are not Sharrwah's fees.
- **Shopify:** "When you use Shopify Payments, you pay the credit card rate, but you don't pay a transaction fee." (`HC:payments/shopify-payments/payouts/pay-periods-and-fees.md:7`). Per transaction: "Transaction fee related to an order transaction." (`GQL:3605`)
- **Salla:** "The Fee Calculator helps you estimate payment processing fees per order." (`SA-en:24`); "Online-payment fees are calculated according to the payment services agreement signed during your store verification." (`SA-en:1241`). Its cash-on-delivery ledger has a column "Cash on delivery fees" beside "Carrier" (`STR:payments.json`).
- **Used by:** D-002, D-003, D-004.

### Sharrwah's fees
- **Here:** what Sharrwah charges a seller. Sharrwah bills them apart from sellers' money, and never deducts them from it (D-004). Which fees, and how they are billed, is left to S-03 (area A-03).
- **Shopify, a precedent:** a platform fee on sales through other providers. "you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify" (`HC:payments/getting-paid.md:11`); "Transaction fees don't apply for POS orders or for manual payment methods" (`HC:your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees.md:23`).
- **Salla:** invoices its own fees: "Payment processing fees VAT is included in the monthly Purchase Invoice issued by Salla." (`SA-en:143`)
- **Used by:** D-001, D-003, D-004.

## Ways to pay

### payment method
- **Here:** a way a buyer pays for an order, which the seller turns on. The platforms have three kinds:
  1. **through a provider:** cards, wallets, local methods and pay later, processed by a provider, including a platform's own payment service;
  2. **paid to the seller directly and recorded by hand:** bank transfer, cash on delivery, money order (*manual payment method*);
  3. **stored value spent at checkout:** gift cards, store credit, a customer's wallet. These spend value the seller already owes, and no money moves (*stored value*).

  In M1's records "payment method" means kinds 1 and 2, unless a record says otherwise. Whether kind 3 is a payment method in Sharrwah is left to S-05.
- **Shopify:** customers "can choose to pay for their order using any of the methods that you've activated" (`HC:payments.md:3`). Manual methods are among them (`HC:payments/manual-payments.md:5`). A gift card is "A gift card that customers use as a payment method." (`GQL:1672`), and store credit can be shown "as a payment method at checkout" (`HC:customers/store-credit.md:3`).
- **Salla:** its Payment Methods page holds "Digital wallets, such as PayPal and stc pay.", "Other payment gateways (Moyasar and HyperPay).", "Buy now, pay later methods, such as Tabby and Tamara." and "Bank accounts." (`SA-en:807`), with Salla's own electronic payments and cash on delivery. "Electronic payment includes all payment methods except cash on delivery and bank transfer." (`SA-en:921`). The customer wallet "acts as an internal payment method" (`SA-en:36`). A gift card is not a payment method: "On Salla, a gift card is built from three pieces: fixed-amount coupons, a digital product that hands those coupon codes to the buyer, and the digital gifting app that delivers the card to the recipient." (`SA-en:1066`)
- **Where they differ:** Shopify makes gift cards and store credit payment methods. Salla makes a gift card a coupon, and its customer wallet a payment method.
- **Used by:** D-001, D-002, D-004, D-005.

### payment provider
- **Here:** the company that processes or receives a payment for a method: a processor or gateway, a wallet, a bank, or an installment company. A platform's own payment service is a provider too. D-001 names a courier collecting cash on delivery apart from providers.
- **Shopify:** "All Shopify-supported payment methods rely on third-party providers to process your transactions." (`HC:payments/getting-paid.md:3`); "Shopify supports two different types of credit card payment providers: **direct providers** and **external providers**." (`HC:payments/third-party-providers.md:5`). Each transaction names its gateway (`GQL:2447`).
- **Salla:** "Electronic Payments is a service provided by Salla that allows your store to process online transactions automatically." (`SA-en:24`). Outside gateways sit beside it (`SA-en:807`). Each transaction names its provider, "Payment Provider Name" (`SAPI:208`).
- *Open:* the held articles don't settle whether Salla limits outside gateways to some kinds of store; one guide is addressed to "charities and digital stores" (`SA-en:2`). This doesn't bear on M1's decisions.
- **Used by:** D-001, D-002, D-004, D-005.

### manual payment method
- **Here:** the buyer pays the seller outside any provider integration, and the seller records the payment by hand: a bank transfer to the seller's account, cash on delivery, a money order, or a method the seller names. The money goes to the seller directly.
- **Shopify:** "Common types of manual payments include cash on delivery (COD), money orders, and bank transfers." (`HC:payments/manual-payments.md:5`); "Orders that accept manual payments are marked as unpaid on the **Orders** page." (`HC:payments/manual-payments.md:10`); "Manual payments aren't captured by Shopify." (`HC:payments/partial-payments.md:44`). The seller records it: "**Mark as paid** - Use when you've already received payment for the current order" (`HC:fulfillment/managing-orders/payments/deferred-payments.md:129`). The seller can also name a method of its own, apart from the names Shopify reserves (`HC:payments/manual-payments.md:59`).
- **Salla:** "Bank transfer (customers transfer payment directly to your account)" (`SA-en:565`). The buyer uploads a receipt: "customers must complete the bank transfer immediately and upload the payment receipt during checkout." (`SA-en:495`). The order waits in "بإنتظار الدفع" (`SSTAT:2`) or "بإنتظار المراجعة" (`SSTAT:3`). No method of the seller's own naming was found (inventory, section 4).
- **Used by:** D-001, D-002.

### cash on delivery
- **Here:** the buyer pays cash when the order is delivered, to a courier or to the seller's own staff. Under D-001 the courier holds the cash until it settles with the seller under their agreement, and Sharrwah holds none. Cash collected through a platform's own shipping labels into a platform balance would be A, which is not built at launch (D-001).
- **Shopify:** a manual method: "Common types of manual payments include cash on delivery (COD), money orders, and bank transfers." (`HC:payments/manual-payments.md:5`). The held evidence shows no collection or settlement by Shopify itself (inventory, section 15). Apps fill it: "Cash/Collect on Delivery (COD) Apps" (`HC:intro-to-shopify/initial-setup/sell-in-italy/italy-cash-on-delivery.md:12`).
- **Salla:** "Cash on Delivery (collected by the shipping company or your own courier)" (`SA-en:565`). Two arrangements:
  - **Salla's own labels:** the cash goes to Salla's cash-on-delivery balance, and Salla transfers it: "The transfer days for cash on delivery balances from shipping companies that support COD via Salla shipping labels are:" (`SA-en:570`); "الأيام المحددة لتحويل رصيد الدفع عند الاستلام من الشركات التي تدعم الدفع عند الاستلام في بوليصات سلة إلى التاجر هي" (`SA-ar:878`). "This feature is currently available only for stores operating within the Kingdom of Saudi Arabia." (`SA-en:570`)
  - **A carrier under the seller's own contract:** the carrier settles. "cash on delivery amounts are transferred to the merchant every 5 business days" (`SA-en:234`); "ويتم تحويل مبالغ الدفع عند الاستلام كل 5 أيام عمل للتاجر" (`SA-ar:602`). Another carrier deducts its invoice from the cash it holds: "في حال وجود مبالغ دفع عند الاستلام فانه يتم خصم مبلغ الفاتورة منها" (`SA-ar:359`).
- **Used by:** D-001, D-002, D-004.

### authorization and capture
- **Here:** an authorization reserves an amount on the buyer's payment method, and a capture takes it. D-002 carries both as outcome kinds and as a capability, "hold and capture later". When to capture is the seller's setting, left to S-07.
- **Shopify:** the capture settings are "**Automatically at checkout**", "**Automatically when order is fulfilled**", "**Automatically capture per fulfillment (Shopify Plus plan only)**" and "**Manually**" (`HC:payments/payment-authorization.md:11`). Shopify Payments "provides an authorization period of 7 days" (`HC:payments/payment-authorization.md:32`). The kinds include AUTHORIZATION and CAPTURE (`GQL:2452`).
- **Salla:** none in the held evidence: no capture setting, authorization or expiry (inventory, section 5).
- **Used by:** D-002, D-003.

### refund and void
- **Here:** a refund returns captured money to the buyer. A void cancels an authorization before capture. Both are outcomes that draw on an earlier outcome (D-002, element 4).
- **Shopify:** "you can refund to the original payment method" (`HC:fulfillment/managing-orders/refunding-orders.md:16`), or to store credit. "The authorized payment was voided, which releases the hold on the customer's payment method before it's captured." (`HC:fulfillment/managing-orders/order-status.md:91`)
- **Salla:** "The money is sent back through the original payment gateway." (`SA-en:804`); "Credit added to the store wallet can only be spent on another purchase in your store." (`SA-en:804`). Its API: "This endpoint allows you to `refund`, `void`, or `reverse` a transaction" (`SAPI:211`).
- **Where they differ:** both refund to stored value as well as to the original method. Salla shows void only in its API.
- **Used by:** D-002, D-003, D-004.

### manual reversal
- **Here:** a refund made outside the provider, because the method can't reverse, as with a bank transfer or cash. D-002's outcome is "manual reversal required", and the seller's attestation that they paid back closes it.
- **Shopify:** "Some payment methods can't be refunded to the original payment method." (`HC:fulfillment/managing-orders/refunding-orders.md:19`); "If the refund can't be completed to the original payment method, then you can resolve the customer outside the original payment method" (`HC:payments/shopify-payments/refunds-troubleshooting.md:91`).
- **Salla:** "Automatic refunds are not supported for orders paid through bank transfer." and "Automatic refunds are not supported for cash-on-delivery payments." (`SA-en:994`)
- **Used by:** D-002.

### rules on payment methods
- **Here:** the seller's rules that change which methods a buyer sees at checkout, or what happens when one is used. D-002 decides only that rules which hide, reorder or rename methods are applied by the order side's checkout. Rules that reject a payment or hold an order for review are left to S-07, and whether apps can supply rules to S-06.
- **Shopify:** "This payment method customization allows you to sort, reorder, hide, rename payment methods and set payment terms on a checkout" (`HC:checkout-settings/checkout-customization.md:73`). Apps make them: "Developers can rename, reorder, and sort the payment methods available to customers during checkout" (`HC:checkout-settings/customize-checkout-configurations/customization-options.md:213`).
- **Salla:** "Payment restrictions are specific conditions applied to payment methods in your store" (`SA-en:923`), "قيود الدفع" in Arabic (`SA-ar:165`). Their actions are "Reject the transaction", "Place the order under review" and "Hide the payment method" (`SA-en:923`). The merchant sets them, and no reorder or rename was found (inventory, section 7).
- **Where they differ:** Shopify's held evidence shows sorting, reordering, hiding, renaming and payment terms, made by apps. Salla's shows rejecting, holding for review and hiding, set by the merchant.
- **Used by:** D-002.

### payment terms
- **Here:** when payment for an order is due, as the seller sets it: on receipt, on fulfilment, after a number of days, or on a date. D-002 carries them as a capability: an order may be placed before payment succeeds, "by a due date the order side sets". Their rules and reminders are left to S-05 and S-11.
- **Shopify:** "Payment terms let you set the date that payment is due." (`HC:fulfillment/managing-orders/payments/deferred-payments.md:7`). The types are RECEIPT, NET, FIXED and FULFILLMENT (`GQL:2514`).
- **Salla:** no seller-set payment terms in the held evidence (inventory, section 14). An order's payment deadline can be extended: "You can also send the payment link directly from the dashboard and extend the payment deadline if needed." (`SA-en:911`)
- **Used by:** D-002.

### installments and pay later
- **Here:** the buyer pays in parts, or later, to a provider who pays the seller. D-005 defers when the seller is paid under them.
- **Shopify:** "Additional payment methods include options such as PayPal Express Checkout, buy now, pay later services, and regional payment methods." (`HC:payments/additional-payment-methods/activate-payment-methods.md:3`)
- **Salla:** "Salla also supports installment and deferred payment services, including:" Tabby, Tamara, Mispay, Madfu and Emkan (`SA-en:565`). The provider reminds the buyer: "Tamara sends reminders via SMS and email before each due date." (`SA-en:577`)
- **Used by:** D-005.

### stored value
- **Here:** value a buyer holds to spend in one store: gift cards, store credit, a customer's wallet. It is value the seller owes the buyer, not money held for anyone. Whether Sharrwah offers it, and whether it is a payment method or a discount, is left to S-05. A wallet buyers pay money into would hold buyers' money, which no M1 record decides. That would be a founder decision (`METHOD.md` section 3).
- **Shopify:** "A gift card that customers use as a payment method. Stores the initial value, current balance, and expiration date." (`GQL:1672`); "A store credit account contains a monetary balance that can be redeemed at checkout for purchases in the shop." (`GQL:3283`)
- **Salla:** the customer wallet keeps "Cashback balances" and "Refunded amounts" (`SA-en:36`). A gift card is coupons in a digital product (`SA-en:1066`).
- *Interpretation:* the held evidence shows stored value credited by the seller, as refunds or cashback, or bought as a product. It doesn't show a buyer paying money into a wallet. Salla's API deposits to a wallet, but "This endpoint will work only if the store has the" wallet application (`SAPI:93`), and doesn't say who deposits.
- **Used by:** D-003.

## The payment boundary (D-002)

### order side
- **Here:** the parts of Sharrwah that deal with what a buyer owes and why: checkout, orders, returns, and the seller's view of them. It owns what was agreed and is due, the amount still owed, the order's states, and the seller's rules that hide, reorder or rename methods (D-002). How it divides into modules is left to S-05.
- **Shopify, nearest:** the order's own payment fields, such as `totalOutstandingSet`, `displayFinancialStatus` and `paymentTerms` (`GQL:2306`).
- **Used by:** D-002, D-003.

### payments side
- **Here:** the part of Sharrwah behind the payment boundary, which D-002 and D-003 call "payments". It owns provider accounts and protocols, provider fees, settlement, payout and custody records, reconciliation, risk and disputes, and which providers are available (D-002). It carries out the founder's direction F-06, payments as a concern of their own (`founder-decisions.tsv`).
- **Shopify, nearest:** the extension points through which providers plug in, the CLI group "Payments extensions" with six templates (`CLI:70`–`CLI:75`), and its payments apps API (E030 to E032).
- **Used by:** D-002, D-003.

### payment boundary
- **Here:** the line between the order side and payments, and the seven elements that cross it: offer, attempt, outcome record, reverse money, verdicts, capabilities and context reads (D-002).
- **Used by:** D-002, D-003.

### amount owed
- **Here:** one amount a buyer owes for an order, with its reference. An offer and an attempt are made for it (D-002, elements 1 and 2). The order side derives what is still owed from outcome records.
- **Shopify:** `Order.totalOutstandingSet` (`GQL:2306`).
- **Salla:** an order can wait for payment until a deadline, "Pending payment expiration value." (`SAPI:5`)
- **Used by:** D-002.

### attempt
- **Here:** one try to pay an amount owed with one method. Its id is the idempotency key. Its states are in progress, buyer action needed, pending, succeeded, failed, expired and unknown (D-002, element 2).
- **Shopify:** a transaction's statuses are SUCCESS, FAILURE, PENDING, ERROR, AWAITING_RESPONSE and UNKNOWN (`GQL:2453`). Its failure codes are "A standardized error code, independent of the payment provider." (`GQL:2450`)
- **Used by:** D-002.

### outcome record
- **Here:** what payments posts to the order for each result: its id, its attempt, the outcome it draws on, its kind (sale, authorization, capture, refund or void), status, amount, evidence level, custodian, method, provider reference, time, and test or live (D-002, element 3).
- **Leaves out:** three of Shopify's eight kinds, CHANGE, EMV_AUTHORIZATION and SUGGESTED_REFUND (`GQL:2452`). *Interpretation:* the first two belong to point of sale (S-10), and the third reads, by its name, as a calculation rather than a result. The schema line doesn't describe them.
- **Shopify:** an order's transactions, `OrderTransaction` (`GQL:2447`), with the kinds SALE, CAPTURE, AUTHORIZATION, VOID, REFUND, CHANGE, EMV_AUTHORIZATION and SUGGESTED_REFUND (`GQL:2452`).
- **Salla:** a transaction names its provider (`SAPI:208`), and can be refunded, voided or reversed (`SAPI:211`).
- **Used by:** D-002, D-003.

### evidence level
- **Here:** what an outcome's claim rests on: the provider's record, a courier event, a seller attestation or a buyer claim (D-002, element 3).
- **Shopify:** the seller marks a manual method's payment as received: "**Mark as paid** - Use when you've already received payment for the current order" (`HC:fulfillment/managing-orders/payments/deferred-payments.md:129`). A transaction says whether its gateway is manual, `manualPaymentGateway` (`GQL:2447`).
- **Salla:** a bank transfer carries the buyer's receipt, "Payment receipt image URL, if available." (`SAPI:5`), and waits in "بإنتظار المراجعة" (`SSTAT:3`).
- *Interpretation:* neither platform names levels. Both tell a provider's result apart from a payment the seller or the buyer reports.
- **Used by:** D-002, D-003.

### capability
- **Here:** what a method can do, which the order side asks instead of naming a provider: hold and capture later; refund by API, and in part; the kind of buyer action; its evidence level; whether an order may be placed before payment succeeds; and its currencies and markets (D-002, element 6).
- **Shopify:** per transaction, `manuallyCapturable` and `multiCapturable` (`GQL:2447`); per order, `capturable` and `refundable` (`GQL:2306`).
- **Used by:** D-002.

### verdict
- **Here:** a decision about a payment that bears on fulfilment: a risk hold, a payment under review, or a dispute's status. Only the verdict crosses, and the order side decides what it does (D-002, element 5).
- **Shopify:** `Order.risks` and `disputes` (`GQL:2306`); "A dispute occurs when a buyer questions the legitimacy of a charge with their financial institution." (`GQL:3209`). Dispute statuses are listed at `GQL:1441`, and risk levels at `GQL:2960`.
- **Salla:** a seller's payment restriction can "Place the order under review" (`SA-en:923`). That is a seller's rule, not one of payments' verdicts (*rules on payment methods*).
- **Used by:** D-002.

### live and test
- **Here:** whether an outcome moved real money. The seller ledger posts only from live outcomes (D-003).
- **Shopify:** `OrderTransaction.test` (`GQL:2447`), and `test` on a balance transaction (`GQL:3197`).
- **Used by:** D-002, D-003.

## The seller ledger (D-003)

### seller ledger
- **Here:** the order side's record of what each seller is owed and owes: sales and refunds from outcome records, and Sharrwah's fees. It holds no money. Payments keeps its own records of custody, payouts and provider fees (D-003).
- **Shopify, nearest:** its ledger is inside its payment service, "A transaction that contributes to a Shopify Payments account balance." (`GQL:3197`). Of its 114 types of balance transaction, 38 are reversals, and 36 of those are named as the reversal of another type (`GQL:3240`, counted by script).
- **Used by:** D-003.

### posting key
- **Here:** the key that makes an entry post once: the outcome id, or the provider's reference, with the type of entry. It never expires (D-003).
- **Shopify, a precedent:** the payments app's request ids are idempotency keys that don't expire (E032:198; E031:277). The Admin API's keys expire after 24 hours (E034:109, 137).
- **Used by:** D-003.

## Legal words (D-004)

### agency role
- **Here:** whether Sharrwah acts for the seller in collecting or handling payments. Under C it has none (D-004, row 5).
- **The references,** from the pilot's variation point S01-VP-06 (`studies/subjects/S-01/variation-points.tsv`, quotes checked in the pilot):
  - Shopify: "appoint us as your agent";
  - Stripe, behind WooPayments: "appoints Stripe as User’s agent";
  - Zid: "authorize Zid to execute payment processes on their behalf";
  - BigCommerce: "No agency ... relationship is created";
  - Salla: "authorize Salla to use it for payment processing".
- **Used by:** D-004.

### security interest
- **Here:** a right a platform or processor takes over a seller's funds, to secure what the seller owes it. Under C Sharrwah takes none (D-004, row 12).
- **The references,** from S01-VP-10: Shopify, "first priority lien and security interest"; Stripe, "a lien over all funds".
- **Used by:** D-004.
