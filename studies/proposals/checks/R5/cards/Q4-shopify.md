# Cards: Q4 on shopify

21 records cited by `studies/proposals/drafts/Q4/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - All five let a seller take orders that the buyer pays outside the platform. They match on role (basis 4), each in its own words, all in stated pages: with a Shopify manual payment method the seller "can arrange to receive their payment in a way that works best for them"; with Salla's bank transfer "يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك"; Zid shows the merchant's bank account at payment "لتمكين العملاء من الدفع عن طريق التحويل البنكي"; with WooCommerce's direct bank transfer "the payment process is manual and happens outside your WooCommerce powered store"; BigCommerce's offline payment methods "do not require a credit card or a traditional payment gateway". Q4-SH-K1737, Q4-SA-P0099, Q4-ZD-K0124, Q4-WC-002, Q4-BC-P0114
- **section 1, line 9:** - Cash on delivery collected by the seller's own carrier keeps the money out of Salla: with a carrier outside Salla's shipping labels "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة", and the amounts are settled "مباشرة بين التاجر وشركة الشحن". WooCommerce's cash on delivery "lets you take payments at the time of delivery", BigCommerce's lets customers "pay you with cash", and Shopify lists it among the common types of manual payments (role, basis 4, all stated). Q4-SA-P0091, Q4-SA-P0092, Q4-WC-004, Q4-BC-P0117, Q4-SH-003
- **section 1, line 11:** - In their terms (official pages), Shopify tells the seller any contract of sale is "directly and only between you and the customer"; Salla's agreement says "ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام", and lets Salla require that payments be made directly between merchant and consumer through their own bank accounts; Zid says it is "ليست طرفاً في العلاقة بين المستهلك والتاجر", which names no one in the role. Q4-SH-K1491, Q4-SA-P0080, Q4-SA-P0081, Q4-ZD-029
- **section 1, line 15:** - No one term covers all five. Shopify says manual payment methods, with cash on delivery, money orders and bank transfers as common types; WooCommerce says offline payment method; BigCommerce's offline payment methods are Bank deposit, Cash on delivery, Check, Money order and Pay in store; Salla and Zid name each method, as التحويل البنكي and الدفع عند الاستلام. Q4-SH-003, Q4-WC-002, Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 16:** - The seller can name a method (role, basis 4, both stated): Shopify's custom manual payment method takes a Custom payment method name, with Cash on Delivery (COD), Bank Deposit, Money Order and other names reserved; each BigCommerce offline method takes a Display Name shown at checkout. Q4-SH-007, Q4-BC-007
- **section 1, line 20:** - **Recording the payment.** Four platforms have the seller record by hand a payment received outside them (role, basis 4): Shopify's Mark as paid, "if you have accepted payment outside of Shopify"; Zid's Bulk Payment Status Update in its plan comparison (shipped); WooCommerce's offline methods "require you to manually verify the payment was processed" before the seller changes the status; BigCommerce's merchant moves the order on "After receiving the payment". Q4-SH-012, Q4-ZD-K0208, Q4-WC-018, Q4-BC-P0115
- **section 1, line 21:** - In the saved markup's text of two steps on store demo-fake-dev-store (30 September 2026), the Collect payment menu of a draft order and of order #1006 holds "Credit card" and "Mark as paid" (markup only: the accessibility trees hold just the button), and order #1006's Mark as paid dialog holds "Mark this order as paid if you received $1.00 USD from another payment method.", words its accessibility tree holds too. Q4-SH-059, Q4-SH-060, Q4-SH-061
- **section 1, line 22:** - Shopify and BigCommerce keep that payment as a transaction on the order (role, basis 4, both stated): `orderMarkAsPaid` records "a payment transaction for the outstanding amount"; BigCommerce's Transactions API creates records "for payments that were processed externally". WooCommerce's order carries `date_paid` and `transaction_id` (shipped). Q4-SH-039, Q4-BC-K0100, Q4-WC-043
- **section 1, line 24:** - **Payment status.** Shopify and Zid keep payment apart from the order's progress (role, basis 4, both stated): an order made with a Shopify manual payment method gets the Payment pending status; Zid's order has a payment status (pending, paid, failed, refunded) beside an order status (new, preparing, indelivery, delivered and others). Q4-SH-016, Q4-ZD-016, Q4-ZD-015
- **section 1, line 26:** - **Time to pay** (role, basis 4, all stated). Salla's merchant can turn off the bank-transfer مهلة الدفع, so that the customer must transfer and attach the receipt on completing the order; WooCommerce's Hold Stock "automatically cancels eligible Pending payment orders created through checkout after the configured time limit"; Shopify lets the seller add payment terms, after which an unpaid order becomes Overdue. Q4-SA-047, Q4-WC-039, Q4-SH-014
- **section 1, line 27:** - In the saved markup's text of store capture-plus's New company page (2 October 2026), the Payment terms options are No payment terms, Due on fulfillment, and Net 7 to Net 90; its accessibility tree holds the heading only. Q4-SH-062
- **section 1, line 29:** - **Fees.** Shopify and BigCommerce differ (both stated): Shopify says "you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers"; BigCommerce charges its Open Payment Provider fee on orders "processed using offline payment methods" by stores on self-serve plans, while Performance plan stores under contracted terms are exempt. Its Pricing article (official page) bills the fee "monthly in arrears", "as a separate line item on your invoice". Q4-SH-K1740, Q4-BC-012, Q4-BC-P0125
- **section 1, line 35:** - **By place.** Shopify and Salla limit methods by the seller's country (role, basis 4, both stated): Shopify offers email money transfers only to merchants in Canada (not checked on Zid); Salla's help says its STC pay, الدفع عن التسليم and حوالة بنكية are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط" (29 September 2026). Q4-SH-027, Q4-SA-054
- **section 1, line 41:** - **Who may record** (role, basis 4, both stated). Shopify's orderMarkAsPaid needs the mark_orders_as_paid permission, and BigCommerce's Manual payment option the Finalize Manual Orders using Manual Payments permission. Q4-SH-042, Q4-BC-022
- **section 1, line 51:** - **Shopify and BigCommerce.** A service of either that collects cash on delivery for the seller was not in what was read. For sellers in Italy, Shopify's Help Center points to App Store apps related to COD. Q4-SH-N01, Q4-BC-N16, Q4-SH-046
- **section 2, line 55:** - **Seller-collected payment method**: Sharrwah would offer ways of paying in which the buyer pays the seller, or someone the seller engages such as its own courier, outside Sharrwah, with no money passing through Sharrwah or a payment service it provides. Sharrwah would show the method, keep the order, and record what the seller says it received or refunded. Q4-SH-K1737, Q4-WC-002, Q4-BC-P0114
- **section 2, line 56:** - Built-in kinds, each off until the seller turns it on: **bank transfer to the seller**; **cash on delivery**, collected by the seller's courier or carrier; **payment at pickup**, at the seller's branch or store; and a **seller-named method** with the seller's own name. They draw on BigCommerce's five offline methods, Pay in store among them, Salla's and Zid's bank transfer and cash on delivery, and Shopify's custom manual payment method. Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098, Q4-SH-007
- **section 2, line 57:** - Each carries instructions shown to the buyer on the confirmation page and in the order notification; Shopify's show on the order confirmation page. Q4-SH-006
- **section 2, line 60:** - Alternative not taken: cash on delivery only as a seller-named method, as Shopify's Help Center has sellers in Italy set it up. Cash on delivery is tied to couriers, carriers and shipping methods on Salla, Zid and WooCommerce, which a seller-named method can't carry (rule 2). Q4-SH-045, Q4-SA-P0199, Q4-WC-033
- **section 2, line 64:** - Alternative not taken: account details only as free-text instructions, as in Shopify's payment instructions. A structured account can be checked against its place's format (rule 1). Q4-SH-006
- **section 2, line 65:** - **Payment status**: each order would carry a payment status apart from its fulfilment status: awaiting payment, awaiting review, partially paid, paid, partially refunded, refunded or voided, and overdue once a due date passes. It follows from the order's **Payment record** and **Refund record** entries; only voiding is set directly. Q4-SH-016, Q4-ZD-016, Q4-ZD-015
- **section 2, line 66:** - It draws on Shopify's and Zid's separate payment status, Shopify's Overdue after payment terms, and Salla's قيد المراجعة for bank-transfer and cash-on-delivery orders. Q4-SH-014, Q4-SA-018
- **section 2, line 69:** - **Payment record**: an entry on the order for each payment the seller says it received outside Sharrwah: amount, currency, method, the date received, who entered it, and an optional reference and proof. Each entry states that no money passed through Sharrwah. Marking an order paid writes one entry for the amount outstanding. Q4-SH-039, Q4-BC-K0100, Q4-WC-043
- **section 2, line 71:** - The seller confirms the amount and currency received before the entry is written; Shopify's Mark as paid dialog names both, in the saved markup's text of one step on store demo-fake-dev-store (30 September 2026): "Mark this order as paid if you received $1.00 USD from another payment method." Q4-SH-061
- **section 2, line 72:** - Only staff with a permission for it may enter payments, as on Shopify and BigCommerce. Q4-SH-042, Q4-BC-022
- **section 2, line 73:** - Why: rule 3. Entries rather than a paid flag let part payments, several receipts and corrections come without a change of model; Shopify records part payments on its Shopify Plus plan. Q4-SH-022
- **section 2, line 74:** - Alternative not taken: a status change alone, as on WooCommerce and BigCommerce, or Zid's Bulk Payment Status Update, since reports need the amount and date received: WooCommerce's analytics count by Date Paid, and Shopify asks for the amount received "For reporting purposes". Q4-WC-032, Q4-SH-026, Q4-ZD-K0208
- **section 2, line 75:** - **Payment window**: per method, an optional time for the buyer to pay after ordering; when it ends, the order shows overdue or is cancelled with its stock released, as the seller chooses. Rule 3 puts only the due date in the data model now and leaves the rest to the build. Q4-SA-047, Q4-WC-039, Q4-SH-014
- **section 2, line 76:** - Payment terms can be set on one order or for a business customer, as Shopify gives them for orders and, in the saved markup's text of its New company page (store capture-plus, 2 October 2026), for a company. Q4-SH-014, Q4-SH-062
- **section 2, line 84:** - **Seller-collected order charge**: if Sharrwah charges for orders paid outside it, the charge would be set per plan and billed to the seller apart from any order, never taken from an order's money, which Sharrwah doesn't hold. Whether to charge at all is a company decision. Q4-BC-012, Q4-BC-P0125, Q4-SH-K1740
- **section 2, line 88:** - **Payment events**: Sharrwah's API would let another system, such as a bank feed, an invoicing tool or a courier, enter a payment or refund on an order, and would tell apps when a payment status changes. Why: rule 2, as banks and couriers differ by place and change, so they plug in behind the API. Q4-SH-039, Q4-BC-K0100, Q4-ZD-K0206
- **section 2, line 89:** - It draws on Shopify's `orderMarkAsPaid`, a Flow template on store capture-plus (7 October 2026) that marks an order paid "When your bank, invoicing or payment system confirms a payment through your webhook", BigCommerce's Transactions API and Zid's payment-status webhook. Q4-SH-039, Q4-SH-057
- **section 3, line 98:** - **Plugs in:** a kind of **Seller-collected payment method** that one place needs, added by Sharrwah behind the method's interface, as Shopify offers email money transfers only to merchants in Canada (not checked on Zid). Q4-SH-027
- **section 3, line 99:** - **Plugs in:** apps that add to a method, as Shopify's Help Center points to App Store apps related to COD. Q4-SH-046
- **section 3, line 100:** - **Plugs in:** other systems that enter payments through **Payment events**. Q4-SH-057, Q4-BC-K0100
- **section 3, line 107:** - **Set per order:** payment and refund entries, proof and a due date. Q4-SA-015, Q4-SH-014
- **section 3, line 108:** - **Set per business customer:** payment terms, as the saved markup's text of Shopify's New company page holds them (store capture-plus, 2 October 2026). Q4-SH-062
- **section 3, line 109:** - **Set per staff member:** the permission to enter payments. Q4-SH-042
- **section 5, line 133:** - Whether orders paid outside Sharrwah bear a charge, on which plans, and how it is billed. The design keeps a charge line billed apart from orders. Settled by the company decision on charges. Q4-SH-K1740, Q4-BC-012
- **section 5, line 135:** - The currency of an amount received. Shopify converts it at the live rate and asks the seller to correct it for reporting; on BigCommerce offline methods take additional currencies; at one of Yemen's areas a domestic sale is paid in rials only (section 6). The design keeps amount and currency on each entry, unconverted. Settled by the design's currency model. Q4-SH-026, Q4-BC-029, YA-21 (rial only @ the internationally recognized government's area, as of 2026-04-24)
- **section 5, line 139:** - Sharrwah's position in a sale paid outside it. The design nowhere assumes Sharrwah is a party to such a sale. Settled by the founder with a lawyer (section 7). Q4-SH-K1491, Q4-ZD-029
- **section 7, line 156:** - Sharrwah's position in sales paid outside it: will its agreement say the sale is between seller and buyer only, and that Sharrwah has no part in cash on delivery or bank transfer, as Shopify's, Salla's and Zid's terms say of themselves? Q4-SH-K1491, Q4-SA-P0080, Q4-ZD-029
- **section 7, line 160:** - Will Sharrwah charge for orders paid outside it, on which plans, and billed how? Q4-SH-K1740, Q4-BC-012

## The cards

### Q4-SH-K1737

**Cited at:** section 1, line 7; section 2, line 55

**Record** (`studies/proposals/records/Q4/shopify/copied.tsv`):
- concern_id: SH-C-079
- placement: decides
- structure: https://help.shopify.com/en/manual/payments/manual-payments.md
- identifier: help.shopify.com/en/manual/payments/manual-payments.md
- statement: When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them.
- cite_ids: SH-S-0385
- note: first run's citation

**Citation SH-S-0385:** `https://help.shopify.com/en/manual/payments/manual-payments.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- quote: When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them.
- title: Manual payment methods
- the page opens: Some customers don't want to pay for their orders using a credit card. These customers can still place their orders online if you set up a manual payment method. When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. You can send an invoice to your customer. After you receive the payment, you can then manually approve the order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. I…
- a note box: Note You aren't charged third-party transaction fees for manual payments.
- headings: Manual payment methods
- in context: # Manual payment methods Some customers don't want to pay for their orders using a credit card. These customers can still place their orders online if you set up a manual payment method. ⟪When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them.⟫ You can [send an invoice](/manual/fulfillment/managing-orders/payments/deferred-payments#email-an-order-invoice-to-a-customer) to your customer. After you receive the payment, you can then manually approve the order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. If your store and your customers are based in Canada, then you can accept [email money transfers](/manual/payments/manual-payments/ema…

### Q4-SH-003

**Cited at:** section 1, line 9; section 1, line 15

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-003
- bears_on: 2;5
- identifier: Manual payment methods
- statement: Common types of manual payments include cash on delivery (COD), money orders, and bank transfers.
- cite_ids: Q4-SH-C003
- from: held

**Citation Q4-SH-C003:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md` | Manual payment methods | 2026-10-16 | kind: stated | quote check: found
- quote: Common types of manual payments include cash on delivery (COD), money orders, and bank transfers.
- title: Manual payment methods
- the page opens: Some customers don't want to pay for their orders using a credit card. These customers can still place their orders online if you set up a manual payment method. When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. You can send an invoice to your customer. After you receive the payment, you can then manually approve the order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. I…
- a note box: Note You aren't charged third-party transaction fees for manual payments.
- headings: Manual payment methods
- in context: …g a credit card. These customers can still place their orders online if you set up a manual payment method. When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. You can [send an invoice](/manual/fulfillment/managing-orders/payments/deferred-payments#email-an-order-invoice-to-a-customer) to your customer. After you receive the payment, you can then manually approve the order. ⟪Common types of manual payments include cash on delivery (COD), money orders, and bank transfers.⟫ If your store and your customers are based in Canada, then you can accept [email money transfers](/manual/payments/manual-payments/email-money-transfers). <aside class="note"><h4>Note</h4><p>You aren't charged <a href="/en/manual/your-account/manage-billing/billing-charges">third-party transaction fees</a> for manual payments.</p> </aside> Orders that accept manual payments are marked as unpaid on the **Orders** page. After you receive payment f…

### Q4-SH-K1491

**Cited at:** section 1, line 11; section 5, line 139; section 7, line 156

**Record** (`studies/proposals/records/Q4/shopify/copied.tsv`):
- concern_id: SH-C-054
- placement: responsible
- structure: https://www.shopify.com/legal/terms
- identifier: 4. Your Responsibilities
- statement: You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the customer. You are the seller or merchant of record for all sales through the Services.
- cite_ids: SH-S-0011
- note: first run's citation

**Citation SH-S-0011:** `https://www.shopify.com/legal/terms` | 4. Your Responsibilities | 2026-08-01 | kind: official page | quote check: found
- quote: You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the customer. You are the seller or merchant of record for all sales through the Services.
- title: Shopify Terms of Service - Shopify
- in context: …you access the Shopify API, your use of the Shopify API is subject to the API Terms. You acknowledge and agree to provide public-facing contact information, terms of service, a refund policy, and shipping policies (including order fulfilment timelines) on your Shopify Store. Public-facing contact information should include your name, address, telephone number, and email address. You should inform your customers if you use a third-party supplier. ⟪You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the customer. You are the seller or merchant of record for all sales through the Services.⟫ You are responsible for the creation and operation of your Shopify Store, your Materials, the goods and services that you may sell through the Services, and all aspects of the transactions between you and your customer(s). This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, returns, fulfilling any sales or customer service, fraudulent trans…

### Q4-SH-007

**Cited at:** section 1, line 16; section 2, line 56

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-007
- bears_on: 4
- identifier: Custom payment method name
- statement: Bank Deposit Cash Cash on Delivery (COD) custom External Credit External Debit Gift Card Money Order Store Credit
- cite_ids: Q4-SH-C008;Q4-SH-C009
- from: held
- note: the list of names reserved by Shopify for a custom manual payment method

**Citation Q4-SH-C008:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md` | Create a custom manual payment method | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: Bank Deposit Cash Cash on Delivery (COD) custom External Credit External Debit Gift Card Money Order Store Credit
- title: Manual payment methods
- the page opens: Some customers don't want to pay for their orders using a credit card. These customers can still place their orders online if you set up a manual payment method. When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. You can send an invoice to your customer. After you receive the payment, you can then manually approve the order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. I…
- a note box: Note You aren't charged third-party transaction fees for manual payments.
- in context: …g payment or if you want to offer your customers alternative ways to pay, such as booking a service and paying in person, then you can create a custom manual payment method. Steps: Desktop From your Shopify admin, go to Settings > Payments. In the Manual payment methods section, select Create custom payment method. In Custom payment method name, enter the name of your payment method. The following names are reserved by Shopify and can't be used: ⟪Bank Deposit Cash Cash on Delivery (COD) custom External Credit External Debit Gift Card Money Order Store Credit⟫ In Additional details, enter any information that you want displayed next to the payment method in your checkout. In Payment instructions, enter the instructions that you want your customer to follow to pay for the order. These instructions are displayed on the order confirmation page after the customer completes their order. Click Activate. Mobile From the Shopify app, tap, and then tap Settings. In the Store settings section, tap Payments. In …  (matched markup removed)

**Citation Q4-SH-C009:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md` | Create a custom manual payment method | 2026-10-16 | kind: stated | quote check: found
- quote: The following names are reserved by Shopify and can't be used:
- title, opening and note boxes: as for this source's citation above
- headings: Manual payment methods > Create a custom manual payment method > Steps:
- in context: …sections"><details open><summary id="desktop">Desktop</summary><ol> <li><p>From your Shopify admin, go to <strong>Settings</strong> > <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p> </li> <li><p>In the <strong>Manual payment methods</strong> section, select <strong>Create custom payment method</strong>.</p> </li> <li><p>In <strong>Custom payment method name</strong>, enter the name of your payment method. ⟪The following names are reserved by Shopify and can't be used:⟫</p> <ul> <li>Bank Deposit</li> <li>Cash</li> <li>Cash on Delivery (COD)</li> <li>custom</li> <li>External Credit</li> <li>External Debit</li> <li>Gift Card</li> <li>Money Order</li> <li>Store Credit</li> </ul> </li> <li><p>In <strong>Additional details</strong>, enter any information that you want displayed next to the payment method in your checkout.</p> </li> <li><p>In <strong>Payment instructions</strong>, enter the instructions that you want…

### Q4-SH-012

**Cited at:** section 1, line 20

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-012
- bears_on: 3
- identifier: Collect payment > Mark as paid
- statement: Click Mark as paid if you have accepted payment outside of Shopify.
- cite_ids: Q4-SH-C014
- from: held

**Citation Q4-SH-C014:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/fulfillment/managing-orders/payments/deferred-payments.md` | Accept payment for an order pending payment, Steps | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: Click Mark as paid if you have accepted payment outside of Shopify.
- title: Managing orders with deferred payments
- the page opens: For orders with a full or partial outstanding balance, you can send an invoice to your customer for the order, accept the payment for the order by credit, or mark the order as paid if you have already received payment by another method. Payment terms for payments due late for an order Payment terms let you set the date that payment is due. If an order has a status of Payment pending, then you can add payment terms for orders that are due to be paid at a later date. You can choose from the follow…
- a note box: Note Customers can view and pay individual payment requests in their customer accounts, but only when a payment request has been sent from the Shopify admin. For orders with multiple fulfillments where payment requests haven't been sent, customers can pay only for the full order.
- a note box: Note Payment reminders aren't sent for orders with purchase options such as subscriptions, preorders, or try before you buy.
- headings: Managing orders with deferred payments > Accept payment for an order pending payment > Steps:
- in context: … mark the order as paid. Learn more about orders with pending payments. If your payment provider supports multiple payments, then you can capture partial payments up to the total order amount. Otherwise, you can collect only the total amount of the order. Steps: 1. From your Shopify admin, go to Orders. 2. From the Orders page, click order number. 3. In the Payment pending section, click Collect payment. 4. Select one of the following options: * ⟪Click Mark as paid if you have accepted payment outside of Shopify.⟫ * Click Pay by credit card if you have the customer's credit card information ready. 5. If you select Pay by credit card, then enter the customer's billing and credit card information, and then click Charge. Set payment reminders You can use the payment reminders feature to automatically send your customer a scheduled payment reminder email for an order that has payment terms assigned. You can create up to five payment reminders. Payment reminde…  (matched markup removed)

### Q4-SH-059

**Cited at:** section 1, line 21

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-059
- bears_on: 3
- identifier: Draft order: Payment; Collect payment
- statement: Payment due later [label: Payment due later] [accessibilitylabel: Collect payment] Credit card Mark as paid
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q4-SH-C073
- from: held
- note: in the saved HTML of step 6 (new draft order, later #D16), markup only: it says nothing of whether the menu was open; the step's aria.yaml shows the button Collect payment [expanded] and the text Payment due later, but not the items Credit card and Mark as paid; bears on Q4-SH-012

**Citation Q4-SH-C073:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T014656Z-journey-order-lifecycle/006.html.txt` | run 20260930T014656Z-journey-order-lifecycle, step 6 (https://admin.shopify.com/store/demo-fake-dev-store/draft_orders/new) | 2026-09-30 | kind: observed | quote check: found
- step 6: open payment options (Collect payment) | https://admin.shopify.com/store/demo-fake-dev-store/draft_orders/new | "demo fake dev store · Drafts · Create order · Shopify" | 2026-09-30T01:47:57.747Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/006.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/006.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T014656Z-journey-order-lifecycle/006.html.txt`
- quote: Payment due later [label: Payment due later] [accessibilitylabel: Collect payment] Credit card Mark as paid
- in context: …ple and blue with the text "SHOPIFY" in a sans serif typeface on top.] The Complete Snowboard Ice Ice [accessibilitylabel: Unit price YER 699.95, adjust price] YER 699.95 Quantity [1] YER 699.95 [accessibilitylabel: Remove item] Added 1 product [heading: Payment] Send invoice Collect payment Subtotal 1 item YER 699.95 Add discount No discount - YER 0.00 Add shipping or delivery No shipping - YER 0.00 Estimated tax Not calculated Total YER 699.95 ⟪Payment due later [label: Payment due later] [accessibilitylabel: Collect payment] Credit card Mark as paid⟫ Unsaved changes Unsaved changes Discard Save 0 tasks running Work with Sidekick Work with Sidekick [heading: Add note] Done Cancel Notes 0/5000 To comment on a draft order or mention a staff member, use Timeline instead [heading: Share checkout link] Copy link Close Share the checkout link with your customer to checkout and place the order. Product prices Lock all product prices so they don't change [accessibilitylabel: Lock all product prices s…

### Q4-SH-060

**Cited at:** section 1, line 21

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-060
- bears_on: 3
- identifier: Order: Payment information; Collect payment
- statement: $1.00 of the balance is currently unauthorized [accessibilitylabel: Collect payment] Credit card Mark as paid
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q4-SH-C074
- from: held
- note: order #1006, in the saved HTML of step 45, markup only; the step's aria.yaml shows the button Collect payment but not the items Credit card and Mark as paid; bears on Q4-SH-012

**Citation Q4-SH-C074:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T090458Z-journey-order-detail/045.html.txt` | run 20260930T090458Z-journey-order-detail, step 45 (https://admin.shopify.com/store/demo-fake-dev-store/orders/6407318864007) | 2026-09-30 | kind: observed | quote check: found
- step 45: choose Mark as paid | https://admin.shopify.com/store/demo-fake-dev-store/orders/6407318864007 | "demo fake dev store · Orders · #1006 · Shopify" | 2026-09-30T09:23:56.475Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T090458Z-journey-order-detail/steps/045.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T090458Z-journey-order-detail/steps/045.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T090458Z-journey-order-detail/045.html.txt`
- quote: $1.00 of the balance is currently unauthorized [accessibilitylabel: Collect payment] Credit card Mark as paid
- in context: … typeface on top.] The Complete Snowboard Ice Ice Unit price $1.00 × 3 3 Total $3.00 USD [heading: Partially paid] [accessibilitylabel: Payment information] Resend invoice [accessibilitylabel: Access more payment actions] [accessibilitylabel: Access more payment actions] Add payment terms Collect payment Original order September 30, 2026 $2.00 USD Subtotal 3 items $3.00 USD Total $3.00 USD Paid Approximately YER473.23 $2.00 USD Balance $1.00 USD ⟪$1.00 of the balance is currently unauthorized [accessibilitylabel: Collect payment] Credit card Mark as paid⟫ Timeline [heading: Timeline] [label: Comment] [initials: Dd] Comment ⟦hidden⟧ Bold Italic Strikethrough Link Heading Quote Code Bullets Numbers Decrease Level Increase Level Attach Files Undo Redo [Enter a URL...] [Link] [Unlink] ⟦/hidden⟧ [placeholder: Leave a comment...] Post Only you and other staff can see comments Only you and other staff can see comments Today You sent invoice #1006 to fake fake-fake (sharrwah@gmail.com) 5 minutes ago You …

### Q4-SH-061

**Cited at:** section 1, line 21; section 2, line 71

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-061
- bears_on: 3
- identifier: Order: Mark as paid (dialog)
- statement: Mark this order as paid if you received $1.00 USD from another payment method.
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q4-SH-C075
- from: held
- note: order #1006, in the saved HTML of step 45; the step's aria.yaml shows the same words, in the dialog "Mark as paid"; bears on Q4-SH-012

**Citation Q4-SH-C075:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T090458Z-journey-order-detail/045.html.txt` | run 20260930T090458Z-journey-order-detail, step 45 (https://admin.shopify.com/store/demo-fake-dev-store/orders/6407318864007) | 2026-09-30 | kind: observed | quote check: found
- step 45: choose Mark as paid | https://admin.shopify.com/store/demo-fake-dev-store/orders/6407318864007 | "demo fake dev store · Orders · #1006 · Shopify" | 2026-09-30T09:23:56.475Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T090458Z-journey-order-detail/steps/045.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T090458Z-journey-order-detail/steps/045.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T090458Z-journey-order-detail/045.html.txt`
- quote: Mark this order as paid if you received $1.00 USD from another payment method.
- in context: …s: Customer events G S E Go to Settings: Shipping G S S Go to Settings: Taxes G S X Go to Settings: Notifications G S N Go to Settings: Gift cards G S I Go to Content: Files G S F Go to Settings: Account G S A Go to Settings: Online Store G S W Go to Settings: Point of Sale G S T Go to Settings: Billing G S B Go to Settings: Plan G B P Go to Settings: Metafields G S M [heading: Mark as paid] [accessibilitylabel: Mark as paid] Mark as paid Cancel ⟪Mark this order as paid if you received $1.00 USD from another payment method.⟫

### Q4-SH-039

**Cited at:** section 1, line 22; section 2, line 69; section 2, line 88; section 2, line 89

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-039
- bears_on: 3
- identifier: orderMarkAsPaid
- statement: Marks an order as paid by recording a payment transaction for the outstanding amount. Use the orderMarkAsPaid mutation to record payments received outside the standard checkout process.
- cite_ids: Q4-SH-C044
- from: held

**Citation Q4-SH-C044:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz` | 5326539 | 2026-09-30 | kind: stated | quote check: found (markup removed)
- quote: Marks an order as paid by recording a payment transaction for the outstanding amount. Use the orderMarkAsPaid mutation to record payments received outside the standard checkout process.
- title: orderMarkAsPaid - GraphQL Admin
- in context: --- title: orderMarkAsPaid - GraphQL Admin description: >- ⟪Marks an order as paid by recording a payment transaction for the outstanding amount. Use the orderMarkAsPaid mutation to record payments received outside the standard checkout process.⟫ The orderMarkAsPaid mutation is particularly useful in scenarios where: - Orders were created with manual payment methods (cash on delivery, bank deposit, money order) - Payments were received offline and need to be recorded in the system - Previously authorized payments need to be captured manually - Orders require manual payment reconciliation due to external payment processing The mutation validates that the order can be marked as paid before…  (matched markup removed)

### Q4-SH-016

**Cited at:** section 1, line 24; section 2, line 65

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-016
- bears_on: 3
- identifier: Payment status: Pending
- statement: Manual payment methods, such as Cash On Delivery, are activated for your store. An order is created using a manual payment method.
- cite_ids: Q4-SH-C018;Q4-SH-C019
- from: held
- note: one of the reasons listed for the Payment pending status

**Citation Q4-SH-C018:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/fulfillment/managing-orders/order-status.md` | Payment status | 2026-10-16 | kind: stated | quote check: found
- quote: Manual payment methods, such as Cash On Delivery, are activated for your store. An order is created using a manual payment method.
- title: Understanding your order statuses
- the page opens: Orders have a variety of statuses such as order status, payment status, fulfillment status, and return status. These statuses are used to create views that help you to track the progress of your orders and find orders that need work. You can filter your orders using different combinations of order statuses. Order status {#order-status-desc} Orders are either Open or Archived, but can have additional statuses. Archived orders that were canceled, display Canceled and Archived statuses. Orders have…
- headings: Understanding your order statuses > Payment status {#order-payment-status-desc}
- in context: …es that the payment provider has started processing, but needs time to complete the payment. The order is created, customers can complete the checkout, and inventory is reserved for the order, but payment isn't guaranteed.</li> <li>You create an order, check <a href="/manual/fulfillment/managing-orders/payments/deferred-payments#add-payment-terms-for-payments-due-later-for-an-order">Payment due later</a>, and then set the payment terms.</li> <li>⟪Manual payment methods, such as Cash On Delivery, are activated for your store. An order is created using a manual payment method.⟫</li> </ul></td> </tr> <tr> <td scope="row">Authorized</td> <td><p>The payment provider validated your customer's payment information. The <strong>Authorized</strong> status is displayed only if you capture payments manually. It acts as your cue to capture payments before the authorization period expires. The <strong>Authorized</strong> payment status is used with credit card payments and some other payment methods.</p> <p>The order is created, c…

**Citation Q4-SH-C019:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/fulfillment/managing-orders/order-status.md` | Payment status | 2026-10-16 | kind: stated | quote check: found
- quote: Orders have the Payment pending status for one of the following reasons:
- title, opening and note boxes: as for this source's citation above
- headings: Understanding your order statuses > Payment status {#order-payment-status-desc}
- in context: … status {#order-payment-status-desc} The payment status of an order is an important part of the information that determines what tasks you need to do for an order. Orders have one or more of the following payment statuses: <table> <caption>Overview of payment statuses and associated actions.</caption> <thead> <tr> <th scope="col" width="25%">Status</th> <th scope="col">Description</th> </tr> </thead> <tbody> <tr> <td scope="row">Pending</td> <td>⟪Orders have the Payment pending status for one of the following reasons:⟫<ul> <li>During checkout, a customer pays with a <a href="/manual/payments/additional-payment-methods">different payment method than credit card</a>. In this case, the Payment pending status indicates that the payment provider has started processing, but needs time to complete the payment. The order is created, customers can complete the checkout, and inventory is reserved for the order, but payment isn't guaranteed.</li> <li>You create an order,…

### Q4-SH-014

**Cited at:** section 1, line 26; section 2, line 66; section 2, line 75; section 2, line 76; section 3, line 107

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-014
- bears_on: 3;4
- identifier: Payment terms
- statement: You can add payment terms for orders that have pending payments and have the Payment pending status. If the order isn't paid by the due date, then the order status becomes Overdue.
- cite_ids: Q4-SH-C016
- from: held

**Citation Q4-SH-C016:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/fulfillment/managing-orders/payments/deferred-payments.md` | Add payment terms for payments due later for an order | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: You can add payment terms for orders that have pending payments and have the Payment pending status. If the order isn't paid by the due date, then the order status becomes Overdue.
- title: Managing orders with deferred payments
- the page opens: For orders with a full or partial outstanding balance, you can send an invoice to your customer for the order, accept the payment for the order by credit, or mark the order as paid if you have already received payment by another method. Payment terms for payments due late for an order Payment terms let you set the date that payment is due. If an order has a status of Payment pending, then you can add payment terms for orders that are due to be paid at a later date. You can choose from the follow…
- a note box: Note Customers can view and pay individual payment requests in their customer accounts, but only when a payment request has been sent from the Shopify admin. For orders with multiple fulfillments where payment requests haven't been sent, customers can pay only for the full order.
- a note box: Note Payment reminders aren't sent for orders with purchase options such as subscriptions, preorders, or try before you buy.
- headings: Managing orders with deferred payments > Payment terms for payments due late for an order
- in context: …tion Due on receipt The payment is due on the date that you send the invoice to your customer. Due on fulfillment The payment is due on the date that you fulfill all items in the order. Net term The payment is due within the specified number of days from the issue date. The available terms are net 7, net 15, net 30, net 45, net 60, and net 90. Fixed term The payment is due on a specific date. Add payment terms for payments due later for an order ⟪You can add payment terms for orders that have pending payments and have the Payment pending status. If the order isn't paid by the due date, then the order status becomes Overdue.⟫ Steps: 1. From your Shopify admin, go to Orders. 2. Click the order that you want to add payment terms for. 3. In the Payment pending section, click, and then click Add payment terms. 4. From the Payment terms drop-down menu, select a payment term for your order. 5. Click Save. Edit or remove payment terms from an order If an order has payment terms, then you can edit or remove payment terms. Steps: 1. From your Shopify admin, go to Orders. 2. C…  (matched markup removed)

### Q4-SH-062

**Cited at:** section 1, line 27; section 2, line 76; section 3, line 108

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-062
- bears_on: 3;4
- identifier: New company: Payment terms
- statement: [heading: Payment terms] No payment terms Due on fulfillment Net 7 Net 15 Net 30 Net 45 Net 60 Net 90
- scope: store capture-plus, observed 2026-10-02
- cite_ids: Q4-SH-C076
- from: held
- note: in the saved HTML of step 174 (New company page), markup only, as the page's options under the heading; the step's aria.yaml shows the heading Payment terms but not these options; bears on Q4-SH-014

**Citation Q4-SH-C076:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/174.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 174 (https://admin.shopify.com/store/capture-plus/companies/new) | 2026-10-02 | kind: observed | quote check: found
- step 174: visit route company:create (path from router) | https://admin.shopify.com/store/capture-plus/companies/new | "capture plus · Companies · New company · Shopify Plus" | 2026-10-02T02:10:08.524Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/174.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/174.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/174.html.txt`
- quote: [heading: Payment terms] No payment terms Due on fulfillment Net 7 Net 15 Net 30 Net 45 Net 60 Net 90
- in context: …d a location to this company. This is where you'll ship products to. Each location can have custom catalogs, checkout settings, and more. You can add more locations later. [heading: Shipping address] [accessibilitylabel: Clear shipping address] Clear Add address [x] Billing address same as shipping address [label: Location ID] [details: Add an existing external ID or create a unique ID.] [heading: Markets] Yemen [heading: Catalogs] Add a catalog ⟪[heading: Payment terms] No payment terms Due on fulfillment Net 7 Net 15 Net 30 Net 45 Net 60 Net 90⟫ [heading: Checkout] Ship to address [label: Allow customers to ship to any one-time address] Order submission [label: Order submission] Orders without shipping addresses will be submitted as draft orders Automatically submit orders Submit all orders as drafts for review [heading: Tax details] [label: Tax ID] [label: Tax settings] Collect tax Collect tax unless exemptions apply Don't collect tax Save [heading: Keyboard Shortcuts] General shortcut…

### Q4-SH-K1740

**Cited at:** section 1, line 29; section 2, line 84; section 5, line 133; section 7, line 160

**Record** (`studies/proposals/records/Q4/shopify/copied.tsv`):
- concern_id: SH-C-079
- placement: decides
- structure: https://help.shopify.com/en/manual/payments/shopify-payments.md
- identifier: transaction fees paragraph
- statement: and you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers.
- cite_ids: SH-S-0322
- note: first run's citation

**Citation SH-S-0322:** `https://help.shopify.com/en/manual/payments/shopify-payments.md` | transaction fees paragraph | 2026-10-10 | kind: stated | quote check: found
- quote: and you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers.
- title: Shopify Payments
- the page opens: Shopify Payments is the simplest way to accept payments online. It eliminates the hassle of setting up a third-party payment provider or merchant account and having to enter the credentials into Shopify. With Shopify Payments you're automatically set up to accept all major payment methods as soon as you create your Shopify store. If you already use a direct third-party payment provider, then you can also use Shopify Payments alongside your existing provider to offer additional payment methods su…
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Shopify Payments
- in context: …href="/en/manual/privacy-and-security/account-security">account security</a>. If you deactivate two-step authentication in the future, then you expose your account and financial information to potential criminal attacks.</li> </ul> </aside> When you use [Shopify Payments](/manual/payments/shopify-payments), you aren't charged third-party transaction fees for orders that are processed through Shopify Payments, Shop Pay, and Shop Pay Installments, ⟪and you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers.⟫ If you elect to use Shopify Payments as your primary payment provider, then PayPal transactions are exempt from third-party transaction fees. If you use Shopify Payments alongside a third-party provider, then transaction fees apply. Learn more about [using Shopify Payments with a third-party provider](/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider). You can use the [Shopify Payments activity report](/manual/…

### Q4-SH-027

**Cited at:** section 1, line 35; section 3, line 98

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-027
- bears_on: 4
- identifier: Email money transfers
- statement: Email money transfers are available only to merchants in Canada.
- scope: Canada
- cite_ids: Q4-SH-C032
- from: held

**Citation Q4-SH-C032:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments/email-money-transfers.md` | Email money transfers, Note | 2026-10-16 | kind: stated | quote check: found
- quote: Email money transfers are available only to merchants in Canada.
- title: Email money transfers
- the page opens: Note Email money transfers are available only to merchants in Canada. If your store is in Canada, then you can let your customers pay with an email money transfer instead of with a credit card. Canadian customers can use an email money transfer service like Interac to securely pay for their order. At checkout, you give the customer your email address and a secret question and answer that they use as a password for the money transfer. When your customer makes the email money transfer, they need t…
- a note box: Note Email money transfers are available only to merchants in Canada.
- headings: Email money transfers
- in context: # Email money transfers <aside class="note"><h4>Note</h4><p>⟪Email money transfers are available only to merchants in Canada.⟫</p> </aside> If your store is in Canada, then you can let your customers pay with an **email money transfer** instead of with a credit card. Canadian customers can use an email money transfer service like [Interac](https://interac.ca/en/interac-e-transfer-consumer.html) to securely pay for their order. At checkout, you give the customer your email address and a secret question and answer that they use as a password for the money transfer. When y…

### Q4-SH-042

**Cited at:** section 1, line 41; section 2, line 72; section 3, line 109

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-042
- bears_on: 4
- identifier: orderMarkAsPaid
- statement: Requires write_orders access scope. Also: The user must have mark_orders_as_paid permission.
- cite_ids: Q4-SH-C048
- from: held

**Citation Q4-SH-C048:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz` | 5326539 | 2026-09-30 | kind: stated | quote check: found (markup removed)
- quote: Requires write_orders access scope. Also: The user must have mark_orders_as_paid permission.
- title: orderMarkAsPaid - GraphQL Admin
- headings: order​Mark​As​Paid
- in context: …order's financial status is updated to reflect the payment, and payment events are logged for tracking and analytics purposes. Learn more about managing orders in apps. api_version: 2026-07 source_url: html: 'https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderMarkAsPaid' md: >- https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderMarkAsPaid.md api_name: admin api_type: graphql type: mutation --- orderMarkAsPaid mutation ⟪Requires write_orders access scope. Also: The user must have mark_orders_as_paid permission.⟫ Marks an order as paid by recording a payment transaction for the outstanding amount. Use the orderMarkAsPaid mutation to record payments received outside the standard checkout process. The orderMarkAsPaid mutation is particularly useful in scenarios where: * Orders were created with manual payment methods (cash on delivery, bank deposit, money order) * Payments were received offline and need to be recorded in the system * Previously authorized …  (matched markup removed)

### Q4-SH-046

**Cited at:** section 1, line 51; section 3, line 99

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-046
- bears_on: 5
- identifier: Cash on Delivery in Italy
- statement: Additionally, there are many apps in our App Store related to COD that can help you create a more personalized experience: Cash/Collect on Delivery (COD) Apps - Shopify App Store.
- scope: Italy
- cite_ids: Q4-SH-C052
- from: held

**Citation Q4-SH-C052:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/sell-in-italy/italy-cash-on-delivery.md` | Cash on Delivery in Italy | 2026-10-16 | kind: stated | quote check: found
- quote: Additionally, there are many apps in our App Store related to COD that can help you create a more personalized experience:
- title: Cash on Delivery in Italy
- the page opens: Cash on Delivery (COD) remains a significant payment method for Italian customers, accounting for 1 in 10 e-commerce transactions in Italy. With COD, customers pay in cash upon delivery, which is preferred due to Italy's cultural inclination towards cash transactions, providing a sense of security and financial control. For Italian e-commerce businesses, COD offers several advantages: * Enhanced Customer Trust: Customers can inspect the product before making payment, which reduces fraud risks. *…
- headings: Cash on Delivery in Italy
- in context: …several advantages: * **Enhanced Customer Trust**: Customers can inspect the product before making payment, which reduces fraud risks. * **Broader Customer Base**: COD accommodates those who prefer cash transactions, a prevalent choice in Italy. You can create COD (Cash on Delivery) as a payment method by following these instructions: [Create a Custom Manual Payment Method](/manual/payments/manual-payments#create-a-custom-manual-payment-method). ⟪Additionally, there are many apps in our App Store related to COD that can help you create a more personalized experience:⟫ [Cash/Collect on Delivery (COD) Apps - Shopify App Store](https://apps.shopify.com/categories/orders-and-shipping-delivery-and-pickups-cash-collect-on-delivery-cod).

### Q4-SH-006

**Cited at:** section 2, line 57; section 2, line 64

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-006
- bears_on: 3
- identifier: Payment instructions
- statement: These instructions display on the order confirmation page after a customer completes their order. When you enter this information, check with your bank or delivery service to find out exactly what a customer must do to complete the payment.
- cite_ids: Q4-SH-C007
- from: held

**Citation Q4-SH-C007:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md` | Use a suggested manual payment method | 2026-10-16 | kind: stated | quote check: found
- quote: These instructions display on the order confirmation page after a customer completes their order. When you enter this information, check with your bank or delivery service to find out exactly what a customer must do to complete the payment.
- title: Manual payment methods
- the page opens: Some customers don't want to pay for their orders using a credit card. These customers can still place their orders online if you set up a manual payment method. When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. You can send an invoice to your customer. After you receive the payment, you can then manually approve the order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. I…
- a note box: Note You aren't charged third-party transaction fees for manual payments.
- headings: Manual payment methods > Use a suggested manual payment method > Steps:
- in context: …ayments"><strong>Payments</strong></a>.</p> </li> <li><p>In the <strong>Payment providers</strong> section, select one of the available manual payment methods.</p> </li> <li><p>In <strong>Additional details</strong>, enter any information that you want displayed next to the payment method in your checkout.</p> </li> <li><p>In <strong>Payment instructions</strong>, enter the instructions that you want your customers to follow to pay for an order. ⟪These instructions display on the order confirmation page after a customer completes their order. When you enter this information, check with your bank or delivery service to find out exactly what a customer must do to complete the payment.⟫</p> </li> <li><p>Click the activate payment method button.</p> </li> </ol> </details><details><summary id="mobile">Mobile</summary><ol> <li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIc…

### Q4-SH-045

**Cited at:** section 2, line 60

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-045
- bears_on: 1;5
- identifier: Cash on Delivery in Italy
- statement: You can create COD (Cash on Delivery) as a payment method by following these instructions: Create a Custom Manual Payment Method.
- scope: Italy
- cite_ids: Q4-SH-C051
- from: held

**Citation Q4-SH-C051:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/sell-in-italy/italy-cash-on-delivery.md` | Cash on Delivery in Italy | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: You can create COD (Cash on Delivery) as a payment method by following these instructions: Create a Custom Manual Payment Method.
- title: Cash on Delivery in Italy
- the page opens: Cash on Delivery (COD) remains a significant payment method for Italian customers, accounting for 1 in 10 e-commerce transactions in Italy. With COD, customers pay in cash upon delivery, which is preferred due to Italy's cultural inclination towards cash transactions, providing a sense of security and financial control. For Italian e-commerce businesses, COD offers several advantages: * Enhanced Customer Trust: Customers can inspect the product before making payment, which reduces fraud risks. *…
- headings: Cash on Delivery in Italy
- in context: …ers pay in cash upon delivery, which is preferred due to Italy's cultural inclination towards cash transactions, providing a sense of security and financial control. For Italian e-commerce businesses, COD offers several advantages: * Enhanced Customer Trust: Customers can inspect the product before making payment, which reduces fraud risks. * Broader Customer Base: COD accommodates those who prefer cash transactions, a prevalent choice in Italy. ⟪You can create COD (Cash on Delivery) as a payment method by following these instructions: Create a Custom Manual Payment Method.⟫ Additionally, there are many apps in our App Store related to COD that can help you create a more personalized experience: Cash/Collect on Delivery (COD) Apps - Shopify App Store.  (matched markup removed)

### Q4-SH-022

**Cited at:** section 2, line 73

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-022
- bears_on: 3
- identifier: Record a manual partial payment
- statement: You can record a manual partial payment, such as a bank deposit or cash on delivery. Manual payments aren't captured by Shopify.
- scope: stores on the Shopify Plus plan
- cite_ids: Q4-SH-C026
- from: held

**Citation Q4-SH-C026:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/partial-payments.md` | Record a manual partial payment | 2026-10-16 | kind: stated | quote check: found
- quote: You can record a manual partial payment, such as a bank deposit or cash on delivery. Manual payments aren't captured by Shopify.
- title: Collecting and recording partial payments
- the page opens: Plan requirement This feature is available to stores on the Shopify Plus plan. You can collect and record multiple partial payments for orders with payment terms in your Shopify admin. With partial payments you can offer flexible payment options to your customers, let your customers pay with multiple payment methods on a single order, and collect deposits or upfront payments. You can collect or record partial payments using the following payment methods: * vaulted credit card (for B2B customers)…
- a note box: Plan requirement This feature is available to stores on the Shopify Plus plan.
- headings: Collecting and recording partial payments > Record a manual partial payment
- in context: … want to collect a partial payment for. 3. Click **Collect payment** > **Enter credit card**. 4. In the **Amount** section, select **Fixed amount** or **Percentage**, and then enter the amount that you want to charge your customer. 5. In the **Card number** section, enter the credit card details. 6. In the **Billing address** enter the billing details or select **Same as shipping address**. 7. Click **Charge**. ## Record a manual partial payment ⟪You can record a manual partial payment, such as a bank deposit or cash on delivery. Manual payments aren't captured by Shopify.⟫ If you have [manual payment methods](/manual/payments/manual-payments) configured, then you can select the payment method that you want to record for the partial payment. #### Steps: 1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders). 2. Click the order that you want to record a partial payment for. 3. Click **Collect payment** > **Record payment**. 4. In the **Amount** section, select **Fixed amount** or **Percenta…

### Q4-SH-026

**Cited at:** section 2, line 74; section 5, line 135

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-026
- bears_on: 3
- identifier: Amount received
- statement: If you use international sales tools, then the value for Amount received is the value in the customer's local currency converted to your store's currency. The conversion is based on the live currency rate. For reporting purposes, if the amount you received is different than the amount displayed, then update it.
- cite_ids: Q4-SH-C031
- from: held

**Citation Q4-SH-C031:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/fulfillment/managing-orders/create-orders/get-paid.md` | Marking payment as paid on a draft order | 2026-10-16 | kind: stated | quote check: found
- quote: The conversion is based on the live currency rate. For reporting purposes, if the amount you received is different than the amount displayed, then update it.
- title: Getting paid for draft orders
- the page opens: When a draft order is ready to be paid by a customer, you can send an invoice or checkout link so that your customer can input their own payment information and pay for the order from the online checkout. Otherwise, if you have your customer's billing information, then you can manually accept payment for draft orders by credit card. You can also mark an order as paid when you've already received payment. When you accept payment for a draft order, it becomes an order on the Orders page. Tip If yo…
- a note box: Tip If you have a Point of Sale retail location using Shopify POS Pro, then your customers can pay for their draft orders in person. Learn more about saving and retrieving a Shopify POS cart.
- a note box: Tip To see more videos, visit our YouTube channel.
- a note box: Note Credit card transaction fees aren't returned to you when you issue a refund.
- headings: Getting paid for draft orders > Marking payment as paid on a draft order {#mark-as-paid}
- in context: …port a past order from another platform into your Shopify admin, then you can mark the order as paid. The received amount isn't captured again by your [payment provider](/manual/payments/third-party-providers), and the customer receives an order confirmation email. If you use [international sales tools](/manual/international), then the value for **Amount received** is the value in the customer's local currency converted to your store's currency. ⟪The conversion is based on the live currency rate. For reporting purposes, if the amount you received is different than the amount displayed, then update it.⟫ #### Steps: 1. From your Shopify admin, go to **Orders** > [**Drafts**](https://admin.shopify.com/draft_orders). 2. Click the existing draft order that you want to mark as paid. 3. In the **Payment** section, click **Collect payment**, and then click **Mark as paid**. 4. Optional: If the **Amount received** value is different than the amount that you received, then update the value. 5. Click **Create order**. 6. Optional: If any [checkout valida…

### Q4-SH-057

**Cited at:** section 2, line 89; section 3, line 100

**Record** (`studies/proposals/records/Q4/shopify/statements.tsv`):
- stmt_id: Q4-SH-057
- bears_on: 1;3
- identifier: Flow templates: Mark order as paid when webhook received
- statement: When your bank, invoicing or payment system confirms a payment through your webhook, mark the matching order as paid. Built for bank transfer, invoice and cash on delivery orders that Shopify cannot capture itself.
- scope: store capture-plus, observed 2026-10-07
- cite_ids: Q4-SH-C071
- from: held

**Citation Q4-SH-C071:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-1.text.txt` | step 31, frame 1 (https://flow.shopifyapps.com/editor/templates) | 2026-10-07 | kind: observed | quote check: found
- step 31: Flow templates: Next (page 31) | https://admin.shopify.com/store/capture-plus/apps/flow/editor/templates | "capture plus · Flow · Shopify Plus" | 2026-10-07T07:56:42.058Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-0.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-0.html`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-0.text.txt`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-1.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-1.html`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.frame-1.text.txt`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.html`, `observed-sh@febbf6c98:raw/runs/20261007T075321Z-journey-flow-templates/steps/031.text.txt`
- quote: When your bank, invoicing or payment system confirms a payment through your webhook, mark the matching order as paid. Built for bank transfer, invoice and cash on delivery orders that Shopify cannot capture itself.
- in context: …country differs from the shipping country. The first one is only flagged for review; a customer who does it again is blocked from checking out. Orders, Risk Tag order when webhook received New When an external system calls your webhook with an order number and a tag, add that tag to the order. Lets a 3PL, ERP or no-code tool mark orders as shipped, invoiced or reviewed without Admin API access. Orders Mark order as paid when webhook received New ⟪When your bank, invoicing or payment system confirms a payment through your webhook, mark the matching order as paid. Built for bank transfer, invoice and cash on delivery orders that Shopify cannot capture itself.⟫ Orders Send payment reminder 24 hours before due date New Sends customers a payment reminder the day before their balance is due. Reduces missed payments and gives customers time to ensure their payment method is ready. Works for both installment invoice and deposit auto-charge orders. Payment reminders, Orders Reward VIP customers with $20 store credit New When the VIP tag is added to a customer, issue them $20 in store credit that never expire…
