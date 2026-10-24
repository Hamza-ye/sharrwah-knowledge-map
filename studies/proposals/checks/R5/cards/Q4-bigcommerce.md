# Cards: Q4 on bigcommerce

13 records cited by `studies/proposals/drafts/Q4/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - All five let a seller take orders that the buyer pays outside the platform. They match on role (basis 4), each in its own words, all in stated pages: with a Shopify manual payment method the seller "can arrange to receive their payment in a way that works best for them"; with Salla's bank transfer "يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك"; Zid shows the merchant's bank account at payment "لتمكين العملاء من الدفع عن طريق التحويل البنكي"; with WooCommerce's direct bank transfer "the payment process is manual and happens outside your WooCommerce powered store"; BigCommerce's offline payment methods "do not require a credit card or a traditional payment gateway". Q4-SH-K1737, Q4-SA-P0099, Q4-ZD-K0124, Q4-WC-002, Q4-BC-P0114
- **section 1, line 8:** - WooCommerce and BigCommerce share the term offline payment method (basis 1), and Salla and Zid the terms التحويل البنكي and الدفع عند الاستلام (basis 1), all in stated pages. Q4-WC-002, Q4-BC-P0114, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 9:** - Cash on delivery collected by the seller's own carrier keeps the money out of Salla: with a carrier outside Salla's shipping labels "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة", and the amounts are settled "مباشرة بين التاجر وشركة الشحن". WooCommerce's cash on delivery "lets you take payments at the time of delivery", BigCommerce's lets customers "pay you with cash", and Shopify lists it among the common types of manual payments (role, basis 4, all stated). Q4-SA-P0091, Q4-SA-P0092, Q4-WC-004, Q4-BC-P0117, Q4-SH-003
- **section 1, line 10:** - Orders the seller creates take such payments too (role, basis 4, all stated): a Salla manual order takes bank transfer with the receipt uploaded, or cash on delivery with its commission; Zid's تفعيل الدفع اليدوي lets the merchant "إنشاء وتنفيذ الطلبات دون الحاجة إلى وجود عملية دفع إلكترونية فعلية"; BigCommerce's manual orders "can reference an offline payment such as cash or check". Q4-SA-007, Q4-ZD-001, Q4-BC-020
- **section 1, line 15:** - No one term covers all five. Shopify says manual payment methods, with cash on delivery, money orders and bank transfers as common types; WooCommerce says offline payment method; BigCommerce's offline payment methods are Bank deposit, Cash on delivery, Check, Money order and Pay in store; Salla and Zid name each method, as التحويل البنكي and الدفع عند الاستلام. Q4-SH-003, Q4-WC-002, Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 16:** - The seller can name a method (role, basis 4, both stated): Shopify's custom manual payment method takes a Custom payment method name, with Cash on Delivery (COD), Bank Deposit, Money Order and other names reserved; each BigCommerce offline method takes a Display Name shown at checkout. Q4-SH-007, Q4-BC-007
- **section 1, line 20:** - **Recording the payment.** Four platforms have the seller record by hand a payment received outside them (role, basis 4): Shopify's Mark as paid, "if you have accepted payment outside of Shopify"; Zid's Bulk Payment Status Update in its plan comparison (shipped); WooCommerce's offline methods "require you to manually verify the payment was processed" before the seller changes the status; BigCommerce's merchant moves the order on "After receiving the payment". Q4-SH-012, Q4-ZD-K0208, Q4-WC-018, Q4-BC-P0115
- **section 1, line 22:** - Shopify and BigCommerce keep that payment as a transaction on the order (role, basis 4, both stated): `orderMarkAsPaid` records "a payment transaction for the outstanding amount"; BigCommerce's Transactions API creates records "for payments that were processed externally". WooCommerce's order carries `date_paid` and `transaction_id` (shipped). Q4-SH-039, Q4-BC-K0100, Q4-WC-043
- **section 1, line 25:** - WooCommerce, BigCommerce and Salla carry payment in the one order status (role, basis 4). WooCommerce sets cash-on-delivery orders to Processing "until payment is collected", though Processing means "Payment has been received (paid)"; BigCommerce places offline-paid orders in Awaiting Payment (both stated). Salla's dashboard text (recorded session, 12 October 2026) shows قيد المراجعة on the confirmation page "عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام", and its help offers to set cash-on-delivery orders to تم التنفيذ at once, "لتجنب إشكالية سوء فهم العميل لحالة" that status. Q4-WC-015, Q4-WC-019, Q4-BC-P0115, Q4-SA-018, Q4-SA-045
- **section 1, line 28:** - **Refunds.** WooCommerce and BigCommerce record a refund that the seller makes outside them (role, basis 4, both stated): a WooCommerce order can reach Refunded "without the customer’s funds having been returned"; recording an offline refund in BigCommerce is "an optional manual process". When a refund can't go through Salla, the merchant transfers the amount to the customer's bank account or adds it to the customer's wallet in the store. Q4-WC-026, Q4-BC-018, Q4-SA-009
- **section 1, line 29:** - **Fees.** Shopify and BigCommerce differ (both stated): Shopify says "you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers"; BigCommerce charges its Open Payment Provider fee on orders "processed using offline payment methods" by stores on self-serve plans, while Performance plan stores under contracted terms are exempt. Its Pricing article (official page) bills the fee "monthly in arrears", "as a separate line item on your invoice". Q4-SH-K1740, Q4-BC-012, Q4-BC-P0125
- **section 1, line 37:** - BigCommerce leaves place to the merchant, who checks the Available Countries of each offline method; a Zid bank account's IBAN must start with SA or AE. Q4-BC-P0121, Q4-ZD-006
- **section 1, line 41:** - **Who may record** (role, basis 4, both stated). Shopify's orderMarkAsPaid needs the mark_orders_as_paid permission, and BigCommerce's Manual payment option the Finalize Manual Orders using Manual Payments permission. Q4-SH-042, Q4-BC-022
- **section 2, line 55:** - **Seller-collected payment method**: Sharrwah would offer ways of paying in which the buyer pays the seller, or someone the seller engages such as its own courier, outside Sharrwah, with no money passing through Sharrwah or a payment service it provides. Sharrwah would show the method, keep the order, and record what the seller says it received or refunded. Q4-SH-K1737, Q4-WC-002, Q4-BC-P0114
- **section 2, line 56:** - Built-in kinds, each off until the seller turns it on: **bank transfer to the seller**; **cash on delivery**, collected by the seller's courier or carrier; **payment at pickup**, at the seller's branch or store; and a **seller-named method** with the seller's own name. They draw on BigCommerce's five offline methods, Pay in store among them, Salla's and Zid's bank transfer and cash on delivery, and Shopify's custom manual payment method. Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098, Q4-SH-007
- **section 2, line 58:** - The same methods serve orders the seller creates, the payment being recorded as the order is made, as Salla's manual orders, Zid's تفعيل الدفع اليدوي and BigCommerce's manual orders allow. Q4-SA-007, Q4-ZD-001, Q4-BC-020
- **section 2, line 68:** - Alternative not taken: one order status that carries payment, as on WooCommerce, BigCommerce and Salla, for that reason. Q4-BC-P0115
- **section 2, line 69:** - **Payment record**: an entry on the order for each payment the seller says it received outside Sharrwah: amount, currency, method, the date received, who entered it, and an optional reference and proof. Each entry states that no money passed through Sharrwah. Marking an order paid writes one entry for the amount outstanding. Q4-SH-039, Q4-BC-K0100, Q4-WC-043
- **section 2, line 72:** - Only staff with a permission for it may enter payments, as on Shopify and BigCommerce. Q4-SH-042, Q4-BC-022
- **section 2, line 77:** - **Refund record**: a refund of a seller-collected payment is made by the seller outside Sharrwah (to the buyer's bank account, in cash, or as credit in the store where it offers one) and entered on the order: amount, route, date and who entered it. Sharrwah's screens would say the refund was recorded, not that it was sent. Q4-BC-018, Q4-SA-009
- **section 2, line 82:** - Alternative not taken: BigCommerce's merchant-set Available Countries as the only control of place. Salla's limit by the seller's country is one a seller can't set (rule 1); the buyer's area stays among the seller's conditions. Q4-BC-P0121, Q4-SA-054
- **section 2, line 84:** - **Seller-collected order charge**: if Sharrwah charges for orders paid outside it, the charge would be set per plan and billed to the seller apart from any order, never taken from an order's money, which Sharrwah doesn't hold. Whether to charge at all is a company decision. Q4-BC-012, Q4-BC-P0125, Q4-SH-K1740
- **section 2, line 85:** - Why: rule 3. A billing route not tied to proceeds belongs in the data model now, as BigCommerce bills its fee monthly as a separate line; the amount can wait. Q4-BC-P0125
- **section 2, line 88:** - **Payment events**: Sharrwah's API would let another system, such as a bank feed, an invoicing tool or a courier, enter a payment or refund on an order, and would tell apps when a payment status changes. Why: rule 2, as banks and couriers differ by place and change, so they plug in behind the API. Q4-SH-039, Q4-BC-K0100, Q4-ZD-K0206
- **section 3, line 100:** - **Plugs in:** other systems that enter payments through **Payment events**. Q4-SH-057, Q4-BC-K0100
- **section 3, line 104:** - **Set per plan:** whether a store gets the methods, which conditions it may set, and any **Seller-collected order charge**: Salla offers bank transfer on its basic plan, Zid's restrictions start at its growth plan, and BigCommerce's fee applies on self-serve plans. Q4-SA-P0099, Q4-ZD-K0357, Q4-BC-012
- **section 3, line 105:** - **Set per store and method:** on or off, name, instructions, accounts and conditions. Q4-BC-007, Q4-ZD-007
- **section 3, line 110:** - **Set by Sharrwah:** the kinds per place, plan entitlements, any charge, and, only by the founder's decision, a collection service. Q4-SA-054, Q4-BC-012
- **section 5, line 133:** - Whether orders paid outside Sharrwah bear a charge, on which plans, and how it is billed. The design keeps a charge line billed apart from orders. Settled by the company decision on charges. Q4-SH-K1740, Q4-BC-012
- **section 5, line 135:** - The currency of an amount received. Shopify converts it at the live rate and asks the seller to correct it for reporting; on BigCommerce offline methods take additional currencies; at one of Yemen's areas a domestic sale is paid in rials only (section 6). The design keeps amount and currency on each entry, unconverted. Settled by the design's currency model. Q4-SH-026, Q4-BC-029, YA-21 (rial only @ the internationally recognized government's area, as of 2026-04-24)
- **section 7, line 160:** - Will Sharrwah charge for orders paid outside it, on which plans, and billed how? Q4-SH-K1740, Q4-BC-012

## The cards

### Q4-BC-P0114

**Cited at:** section 1, line 7; section 1, line 8; section 2, line 55

**Record** (`studies/proposals/records/Q4/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-113
- bullet: end-payment
- placement: where
- identifier: Offline Payment Methods
- statement: Offline payment methods are ways to pay for orders that do not require a credit card or a traditional payment gateway. These can be helpful alternatives to make payments attainable for shoppers. Unlike most online payment methods, such as through a payment gateway, collecting payment is not immediate in these methods.
- cite_ids: S01-BC-C197;S01-BC-C198
- from: new

**Citation S01-BC-C197:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` | line 88: introduction | 2026-10-13 | kind: stated | quote check: found
- quote: Offline payment methods are ways to pay for orders that do not require a credit card or a traditional payment gateway. These can be helpful alternatives to make payments attainable for shoppers.
- in context: …eckout Configurations PAYMENT METHODS Available Payment Gateways Offline Payments Setup Bank Deposit Cash on Delivery Check Money Order Pay in Store TROUBLESHOOTING Understanding Checkout Errors Shipping Tax Security B2B DESIGN AND CONTENT MANAGE STORE CHANNEL MANAGER MARKETING DATA SOLUTIONS ACCOUNT TD BANK Offline Payment Methods What We'll Cover How it works Requirements Enabling offline payment methods Configuring offline payment methods FAQ ⟪Offline payment methods are ways to pay for orders that do not require a credit card or a traditional payment gateway. These can be helpful alternatives to make payments attainable for shoppers.⟫ Unlike most online payment methods, such as through a payment gateway, collecting payment is not immediate in these methods. What is an Open Payment Provider fee? For stores on self-serve plans, orders processed using offline payment methods and payment providers that are not on our Embedded Payment Provider list are assessed an Open Payment Provider fee. Orders processed through Embedded Payment Providers and Performance plan stores operating u…

**Citation S01-BC-C198:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` | line 88: introduction | 2026-10-13 | kind: stated | quote check: found
- quote: Unlike most online payment methods, such as through a payment gateway, collecting payment is not immediate in these methods.
- title, opening and note boxes: as for this source's citation above
- in context: …Shipping Tax Security B2B DESIGN AND CONTENT MANAGE STORE CHANNEL MANAGER MARKETING DATA SOLUTIONS ACCOUNT TD BANK Offline Payment Methods What We'll Cover How it works Requirements Enabling offline payment methods Configuring offline payment methods FAQ Offline payment methods are ways to pay for orders that do not require a credit card or a traditional payment gateway. These can be helpful alternatives to make payments attainable for shoppers. ⟪Unlike most online payment methods, such as through a payment gateway, collecting payment is not immediate in these methods.⟫ What is an Open Payment Provider fee? For stores on self-serve plans, orders processed using offline payment methods and payment providers that are not on our Embedded Payment Provider list are assessed an Open Payment Provider fee. Orders processed through Embedded Payment Providers and Performance plan stores operating under contracted terms are not subject to this fee. How It Works Once enabled, shoppers will see your offline method as an ava…

### Q4-BC-P0117

**Cited at:** section 1, line 9

**Record** (`studies/proposals/records/Q4/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-116
- bullet: a;end-payment
- placement: where
- identifier: Configuring Offline Payment Methods: Cash on delivery
- statement: You can set up your online store to allow your customers to pay you with cash by setting up a Cash on Delivery payment method.
- cite_ids: S01-BC-C201
- from: new

**Citation S01-BC-C201:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` | line 139: Configuring Offline Payment Methods, Cash on delivery | 2026-10-13 | kind: stated | quote check: found
- quote: You can set up your online store to allow your customers to pay you with cash by setting up a Cash on Delivery payment method.
- in context: … the shopper to make a bank deposit payment. This text will appear on the order confirmation page and in the confirmation email sent to the shopper. Want to add the order number to your bank deposit instructions? You can add the variable %%OrderID%% to add the order ID to these details. This variable will be replaced with the Order ID when viewed by a customer. Note that this is only supported in the Bank Deposit payment method. CASH ON DELIVERY ⟪You can set up your online store to allow your customers to pay you with cash by setting up a Cash on Delivery payment method.⟫ Specify an address for the shopper to send the payment as well as other preferences in the fields under the Cash on Delivery tab. Display Name - Enter what will your customers see this option called during checkout. Available Countries - Check the box for the countries where this payment method is available at checkout. Delivery Information - Enter any information necessary for the shopper to complete the payment This information will be display…

### Q4-BC-020

**Cited at:** section 1, line 10; section 2, line 58

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-020
- bears_on: 1;3
- identifier: Manual orders
- statement: Manual orders can reference an offline payment such as cash or check, or you can manually enter their credit card details if you are using a non-hosted payment gateway.
- cite_ids: Q4-BC-C025
- from: held

**Citation Q4-BC-C025:** `https://support.bigcommerce.com/s/article/Creating-a-Manual-Order` | introduction | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/019-support.bigcommerce.com/text.txt` (12776 bytes), fetched 2026-10-13T05:40:15Z, captured
- quote: Manual orders can reference an offline payment such as cash or check, or you can manually enter their credit card details if you are using a non-hosted payment gateway.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …lfillment purposes. Look different? This article covers the old experience for creating manual orders. See Manual Orders and Draft Orders for help with the new experience. How It Works When you create a manual order, you can build an order from scratch using your store's existing customer, product, and shipping details. You can also enter custom information to take orders with products and shipping rates that aren't available on your storefront. ⟪Manual orders can reference an offline payment such as cash or check, or you can manually enter their credit card details if you are using a non-hosted payment gateway.⟫ Non-credit card online payment methods, such as PayPal or Apple Pay, cannot be used in a manual order. Additionally, you can save an order as a draft, which will generate a cart URL. This unique URL can then be sent to customers, allowing them to go directly to your storefront cart page with a pre-populated cart that is ready for check out. See Creating a Draft Order for more details. Requirements Your store must have your default currency assig…

### Q4-BC-006

**Cited at:** section 1, line 15; section 2, line 56

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-006
- bears_on: 2
- identifier: Configuring Offline Payment Methods
- statement: Bank deposit Cash on delivery Check Money order Pay in store
- cite_ids: Q4-BC-C006
- from: held

**Citation Q4-BC-C006:** `https://support.bigcommerce.com/s/article/Offline-Payment-Methods?language=en_US` | Configuring Offline Payment Methods (list of tabs) | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:42Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` (8085 bytes), fetched 2026-10-13T05:39:57Z, captured
- quote: Bank deposit Cash on delivery Check Money order Pay in store
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …nage Payments and Manage Settings permissions must be enabled on your user account. Enabling Offline Payment Methods To set up an offline payment method, go to Settings › Payments and select a currency from the drop-down list. Click the Open tab, and expand Offline Payment Methods. Click the Set up button next to the offline method that you want to use. On the next page, configure your selected payment method. Configuring Offline Payment Methods ⟪Bank deposit Cash on delivery Check Money order Pay in store⟫ BANK DEPOSIT You can set up your store to allow your customers to make a payment directly into your bank account by setting up a Bank Deposit payment method. This payment method displays your bank account information and instructions to your customer after their order is complete. In the Bank Deposit tab, enter your preferences in the fields below. Display Name - Enter what will your customers see this option called during checkout. Available Co…

### Q4-BC-007

**Cited at:** section 1, line 16; section 3, line 105

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-007
- bears_on: 2
- identifier: Display Name
- statement: Display Name — Enter what will your customers see this option called during checkout.
- scope: each offline payment method tab
- cite_ids: Q4-BC-C007
- from: held

**Citation Q4-BC-C007:** `https://support.bigcommerce.com/s/article/Offline-Payment-Methods?language=en_US` | Configuring Offline Payment Methods: Bank Deposit | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:42Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` (8085 bytes), fetched 2026-10-13T05:39:57Z, captured
- quote: Display Name — Enter what will your customers see this option called during checkout.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …. Configuring Offline Payment Methods Bank deposit Cash on delivery Check Money order Pay in store BANK DEPOSIT You can set up your store to allow your customers to make a payment directly into your bank account by setting up a Bank Deposit payment method. This payment method displays your bank account information and instructions to your customer after their order is complete. In the Bank Deposit tab, enter your preferences in the fields below. ⟪Display Name - Enter what will your customers see this option called during checkout.⟫ Available Countries - Check the box for the countries where this payment method is available at checkout. Account Information - Enter all the bank account information necessary for the shopper to make a bank deposit payment. This text will appear on the order confirmation page and in the confirmation email sent to the shopper. Want to add the order number to your bank deposit instructions? You can add the variable %%OrderID%% to add the order ID…

### Q4-BC-P0115

**Cited at:** section 1, line 20; section 1, line 25; section 2, line 68

**Record** (`studies/proposals/records/Q4/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-114
- bullet: end-payment
- placement: decides
- identifier: Offline Payment Methods: How It Works: Awaiting Payment
- statement: Orders placed using an offline payment method are placed in Awaiting Payment order status. After receiving the payment, you can manually set the order to the Awaiting Fulfillment or another order status as you process the order.
- cite_ids: S01-BC-C199
- from: new

**Citation S01-BC-C199:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` | line 101: How It Works | 2026-10-13 | kind: stated | quote check: found
- quote: Orders placed using an offline payment method are placed in Awaiting Payment order status. After receiving the payment, you can manually set the order to the Awaiting Fulfillment or another order status as you process the order.
- in context: …ayment Provider fee. Orders processed through Embedded Payment Providers and Performance plan stores operating under contracted terms are not subject to this fee. How It Works Once enabled, shoppers will see your offline method as an available payment method at checkout. After the customer places their order, they will be shown the information and instructions you configured during setup in their email invoice and on the order confirmation page. ⟪Orders placed using an offline payment method are placed in Awaiting Payment order status. After receiving the payment, you can manually set the order to the Awaiting Fulfillment or another order status as you process the order.⟫ Requirements Your store's checkout type must be Optimized One-Page Checkout or Custom Checkout. To set up and manage payment methods, the Manage Payments and Manage Settings permissions must be enabled on your user account. Enabling Offline Payment Methods To set up an offline payment method, go to Settings › Payments and select a currency from the drop-down list. Click the Open tab, and expand Offline Payment Methods. Click the Set up button ne…

### Q4-BC-K0100

**Cited at:** section 1, line 22; section 2, line 69; section 2, line 88; section 3, line 100

**Record** (`studies/proposals/records/Q4/bigcommerce/copied.tsv`):
- concern_id: BC-C-020
- placement: where
- structure: API reference group: /developer/api-reference/rest/admin/payments/transactions
- identifier: /developer/api-reference/rest/admin/payments/transactions
- statement: The Transactions API lets you create transaction records in BigCommerce for payments that were processed externally. This enables merchants to use BigCommerce for post-order actions such as capture, void, and refund on transactions that originated outside of BigCommerce.
- cite_ids: BC-S-0111

**Citation BC-S-0111:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/payments/transactions.md` | page introduction | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/053-docs.bigcommerce.com/text.txt` (778 bytes), fetched 2026-10-12T04:20:08Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/002-docs.bigcommerce.com/text.txt` (778 bytes), fetched 2026-10-12T10:49:37Z, captured
- quote: The Transactions API lets you create transaction records in BigCommerce for payments that were processed externally. This enables merchants to use BigCommerce for post-order actions such as capture, void, and refund on transactions that originated outside of BigCommerce.
- title: Transactions API (Beta)
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. The Transactions API lets you create transaction records in BigCommerce for payments that were processed externally. This enables merchants to use BigCommerce for post-order actions such as capture, v…
- headings: Transactions API (Beta)
- in context: > This page is for Developer. > For clean Markdown of any page, append .md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. # Transactions API (Beta) ⟪The Transactions API lets you create transaction records in BigCommerce for payments that were processed externally. This enables merchants to use BigCommerce for post-order actions such as capture, void, and refund on transactions that originated outside of BigCommerce.⟫ For supported providers, payment methods, and detailed usage instructions, see the [Transactions API guide](/developer/docs/admin/checkout-and-cart/payments/transactions-api).

### Q4-BC-018

**Cited at:** section 1, line 28; section 2, line 77

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-018
- bears_on: 3
- identifier: offline refund
- statement: In this case, performing an offline refund is an optional manual process to record (within BigCommerce) that a refund has been actioned against an order.
- scope: You are refunding a customer who paid via an offline payment method (cash, bank deposit, cheque or money order).
- cite_ids: Q4-BC-C022;Q4-BC-C023
- from: held

**Citation Q4-BC-C022:** `https://support.bigcommerce.com/s/article/Processing-Refunds` | FAQ: When can I perform an offline refund? | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/023-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/023-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:43Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/007-support.bigcommerce.com/text.txt` (20846 bytes), fetched 2026-10-13T05:39:59Z, captured
- quote: In this case, performing an offline refund is an optional manual process to record (within BigCommerce) that a refund has been actioned against an order.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …t your restocking fee from the total amount to refund to the customer. We recommend clearly stating your restocking fee in your returns policy page. REFUND METHODS When can I perform an offline refund? You can perform an offline refund if: You are refunding a customer who paid via an offline payment method (cash, bank deposit, cheque or money order). You actioned the refund directly via the payment gateway/processor, and not through BigCommerce. ⟪In this case, performing an offline refund is an optional manual process to record (within BigCommerce) that a refund has been actioned against an order.⟫ This ensures that your order information is up-to-date on your BigCommerce store, which is important if you perform future partial refunds against the same order. Can I refund an order that was paid with a gift certificate? Yes. In this case, you will technically not be refunding the funds back to the gift certificate, but crediting the customer's account with store credit. Can I refund an order that was paid with store credit? Yes. As with gift…

**Citation Q4-BC-C023:** `https://support.bigcommerce.com/s/article/Processing-Refunds` | FAQ: When can I perform an offline refund? | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/023-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/023-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:43Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/007-support.bigcommerce.com/text.txt` (20846 bytes), fetched 2026-10-13T05:39:59Z, captured
- quote: You are refunding a customer who paid via an offline payment method (cash, bank deposit, cheque or money order).
- title, opening and note boxes: as for this source's citation above
- in context: …th that product will be removed from the order if the product is removed. How can I charge a restocking fee when refunding a returned order? While you cannot add a charge when processing a return, you can deduct your restocking fee from the total amount to refund to the customer. We recommend clearly stating your restocking fee in your returns policy page. REFUND METHODS When can I perform an offline refund? You can perform an offline refund if: ⟪You are refunding a customer who paid via an offline payment method (cash, bank deposit, cheque or money order).⟫ You actioned the refund directly via the payment gateway/processor, and not through BigCommerce. In this case, performing an offline refund is an optional manual process to record (within BigCommerce) that a refund has been actioned against an order. This ensures that your order information is up-to-date on your BigCommerce store, which is important if you perform future partial refunds against the same order. Can I refund an order that was paid…

### Q4-BC-012

**Cited at:** section 1, line 29; section 2, line 84; section 3, line 104; section 3, line 110; section 5, line 133; section 7, line 160

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-012
- bears_on: 3
- identifier: Open Payment Provider fee
- statement: For stores on self-serve plans, orders processed using offline payment methods and payment providers that are not on our Embedded Payment Provider list are assessed an Open Payment Provider fee. Orders processed through Embedded Payment Providers and Performance plan stores operating under contracted terms are not subject to this fee.
- scope: stores on self-serve plans
- cite_ids: Q4-BC-C012;Q4-BC-C013;Q4-BC-C014
- from: held

**Citation Q4-BC-C012:** `https://support.bigcommerce.com/s/article/Offline-Payment-Methods?language=en_US` | What is an Open Payment Provider fee? | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:42Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` (8085 bytes), fetched 2026-10-13T05:39:57Z, captured
- quote: For stores on self-serve plans, orders processed using offline payment methods and payment providers that are not on our Embedded Payment Provider list are assessed an Open Payment Provider fee.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …works Requirements Enabling offline payment methods Configuring offline payment methods FAQ Offline payment methods are ways to pay for orders that do not require a credit card or a traditional payment gateway. These can be helpful alternatives to make payments attainable for shoppers. Unlike most online payment methods, such as through a payment gateway, collecting payment is not immediate in these methods. What is an Open Payment Provider fee? ⟪For stores on self-serve plans, orders processed using offline payment methods and payment providers that are not on our Embedded Payment Provider list are assessed an Open Payment Provider fee.⟫ Orders processed through Embedded Payment Providers and Performance plan stores operating under contracted terms are not subject to this fee. How It Works Once enabled, shoppers will see your offline method as an available payment method at checkout. After the customer places their order, they will be shown the information and instructions you configured during setup in their email invoice and on the order confirmation page. Orders placed using …

**Citation Q4-BC-C013:** `https://support.bigcommerce.com/s/article/Offline-Payment-Methods?language=en_US` | What is an Open Payment Provider fee? | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/022-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:42Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` (8085 bytes), fetched 2026-10-13T05:39:57Z, captured
- quote: Orders processed through Embedded Payment Providers and Performance plan stores operating under contracted terms are not subject to this fee.
- title, opening and note boxes: as for this source's citation above
- in context: …ayment gateway. These can be helpful alternatives to make payments attainable for shoppers. Unlike most online payment methods, such as through a payment gateway, collecting payment is not immediate in these methods. What is an Open Payment Provider fee? For stores on self-serve plans, orders processed using offline payment methods and payment providers that are not on our Embedded Payment Provider list are assessed an Open Payment Provider fee. ⟪Orders processed through Embedded Payment Providers and Performance plan stores operating under contracted terms are not subject to this fee.⟫ How It Works Once enabled, shoppers will see your offline method as an available payment method at checkout. After the customer places their order, they will be shown the information and instructions you configured during setup in their email invoice and on the order confirmation page. Orders placed using an offline payment method are placed in Awaiting Payment order status. After receiving the payment, you can manually set the order to the Awai…

**Citation Q4-BC-C014:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | OFFLINE PAYMENT METHODS | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/015-support.bigcommerce.com/text.txt` (0 bytes), `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/015-support.bigcommerce.com/raw.html` (961887 bytes), fetched 2026-10-13T00:35:35Z, captured
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/002-support.bigcommerce.com/text.txt` (11615 bytes), fetched 2026-10-13T05:39:51Z, captured
- quote: In addition to the above payment gateway integrations, orders processed using offline payment methods are also subject to the Open Payment Provider fee.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …nce ✔ ✔ ✔ ✔ ✔ ✔ BitPay ✔ ✔ Chase Merchant Services ✔ ✔ ✔ ✔ ✔ Clover Payments ✔ Commonwealth Bank ✔ ✔ ✔ ✔ Cybersource ✔ ✔ ✔ ✔ ✔ ✔ Electronic Payment Exchange (EPX) ✔ ✔ Eway Rapid ✔ ✔ Mercado Pago ✔ ✔ ✔ Moneris ✔ ✔ ✔ MyVirtualMerchant ✔ ✔ Nexi XPay ✔ ✔ ✔ ✔ ✔ NMI ✔ ✔ Opayo by Elavon ✔ ✔ ✔ ✔ ✔ Optty ✔ ✔ QuickBooks Payments ✔ ✔ Serve First ✔ Square ✔ ✔ ✔ ✔ Tilopay ✔ ✔ ✔ ✔ ✔ USAePay ✔ Windcave ✔ ✔* ✔ ✔ *See article for details. OFFLINE PAYMENT METHODS ⟪In addition to the above payment gateway integrations, orders processed using offline payment methods are also subject to the Open Payment Provider fee.⟫ Bank deposit Money order Cash on delivery Pay in-store Check* *B2B Edition adopts the Check offline payment method to enable the Purchase Order (PO) payment method. Note that Performance plan stores operating under contracted terms are not subject to the Open Payment Provider fee. Alternative Payment Methods and Digital Wallets Alternative Payment Methods (APMs) are payment options that often do not require a major credit card scheme such as Vis…

### Q4-BC-P0125

**Cited at:** section 1, line 29; section 2, line 84; section 2, line 85

**Record** (`studies/proposals/records/Q4/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-124
- bullet: c
- placement: decides
- identifier: About BigCommerce Pricing: Open Payment Provider fees: invoice
- statement: Fees are billed monthly in arrears (after the service period) as a separate line item on your invoice.
- scope: self-serve plans; orders not processed through providers on the Embedded Payment Providers list
- cite_ids: S01-BC-C211
- from: new

**Citation S01-BC-C211:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/040-support.bigcommerce.com/text.txt` | line 123: Open Payment Provider fees | 2026-10-13 | kind: stated | quote check: found
- quote: Fees are billed monthly in arrears (after the service period) as a separate line item on your invoice.
- in context: …the automatic upgrade is sent to the billing contact specific in the Account Dashboard. OVERAGE FEES Scale and Performance plans apply an overage fee on Inclusive GMV above their monthly threshold, charged at a flat percentage rate. The fee applies only to GMV exceeding the threshold, not your total GMV for the month. This means costs scale predictably with your sales volume, which is particularly useful for businesses with seasonal variability. ⟪Fees are billed monthly in arrears (after the service period) as a separate line item on your invoice.⟫ Core and Growth plans automatically upgrade when you reach their GMV threshold, so there are no overage charges on these plans. OPEN PAYMENT PROVIDER FEES On self-serve plans, an Open Payment Provider fee is applied to orders, both online and offline, that are not processed through providers on the Embedded Payment Providers list. The fee is determined at the order level, meaning each order is attributed to the provider that processed it. Stores…

### Q4-BC-P0121

**Cited at:** section 1, line 37; section 2, line 82

**Record** (`studies/proposals/records/Q4/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-120
- bullet: e
- placement: decides
- identifier: Configuring Offline Payment Methods: Available Countries
- statement: Available Countries — Check the box for the countries where this payment method is available at checkout.
- scope: the countries the merchant checks for each offline payment method
- conditions: S01-BC-115;S01-BC-116;S01-BC-117;S01-BC-118;S01-BC-119
- cite_ids: S01-BC-C205
- from: new

**Citation S01-BC-C205:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` | line 130: Configuring Offline Payment Methods (the same field under each method) | 2026-10-13 | kind: stated | quote check: found
- quote: Available Countries — Check the box for the countries where this payment method is available at checkout.
- in context: …Pay in store BANK DEPOSIT You can set up your store to allow your customers to make a payment directly into your bank account by setting up a Bank Deposit payment method. This payment method displays your bank account information and instructions to your customer after their order is complete. In the Bank Deposit tab, enter your preferences in the fields below. Display Name - Enter what will your customers see this option called during checkout. ⟪Available Countries - Check the box for the countries where this payment method is available at checkout.⟫ Account Information - Enter all the bank account information necessary for the shopper to make a bank deposit payment. This text will appear on the order confirmation page and in the confirmation email sent to the shopper. Want to add the order number to your bank deposit instructions? You can add the variable %%OrderID%% to add the order ID to these details. This variable will be replaced with the Order ID when viewed by a customer. Note that t…

### Q4-BC-022

**Cited at:** section 1, line 41; section 2, line 72

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-022
- bears_on: 4
- identifier: Finalize Manual Orders using Manual Payments
- statement: To select the Manual payment option during the Payment step, the Finalize Manual Orders using Manual Payments permission must be enabled.
- cite_ids: Q4-BC-C027
- from: held

**Citation Q4-BC-C027:** `https://support.bigcommerce.com/s/article/Creating-a-Manual-Order` | Requirements | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/019-support.bigcommerce.com/text.txt` (12776 bytes), fetched 2026-10-13T05:40:15Z, captured
- quote: To select the Manual payment option during the Payment step, the Finalize Manual Orders using Manual Payments permission must be enabled.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …RL can then be sent to customers, allowing them to go directly to your storefront cart page with a pre-populated cart that is ready for check out. See Creating a Draft Order for more details. Requirements Your store must have your default currency assigned to the default storefront channel (channel ID 1). See the FAQ for more information. To create a manual order, the Manage Orders and Add Orders permissions must be enabled on your user account. ⟪To select the Manual payment option during the Payment step, the Finalize Manual Orders using Manual Payments permission must be enabled.⟫ Creating a Manual Order Go to Orders › Add. You will be taken to the Add an Order screen. Creating a manual order consists of four phases: Customer info - Entering the billing details. Items - Adding items to the cart. Fulfillment - Entering the shipping details. Payment - Selecting a payment gateway and entering the payment details. Adding Customer Info When you create a manual order, you will start on the Customer info step. Under Customer inf…

### Q4-BC-029

**Cited at:** section 5, line 135

**Record** (`studies/proposals/records/Q4/bigcommerce/statements.tsv`):
- stmt_id: Q4-BC-029
- bears_on: 4
- identifier: transactional currencies
- statement: All offline payment methods support additional transactional currencies.
- cite_ids: Q4-BC-C034
- from: held

**Citation Q4-BC-C034:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | transactional currencies | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (14272 bytes), fetched 2026-10-13T05:41:00Z, captured
- quote: All offline payment methods support additional transactional currencies.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency. Display currencies transact in your store's default currency. As such, they use the payment methods configured for the store's default currency. See Available Payment Gateways for a table of payment gateways that support additional transactional currencies. ⟪All offline payment methods support additional transactional currencies.⟫ If there are no payment methods currently set up for a transactional currency, you'll see a Set up button in the Payment provider column, under Additional Currencies in your store's Currencies settings. If your store has additional storefronts, you will be able to manage which transactional currencies are available on each storefront, allowing you to create a unique set of supported currencies per storefront. See Currencies in our Multi-Storefro…
