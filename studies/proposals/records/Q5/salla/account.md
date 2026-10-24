# Q5 on Salla: what the platform shows

## [1]

### اتفاقية الاستخدام and transaction limits
- Salla's usage agreement (اتفاقية الاستخدام) gives Salla's administration the right to cancel, modify or change any of the payment methods it has made available on the platform. Q5-SA-001
- Under the same article, Salla provides the payment and settlement system through its partners (عبر شركائها). Payment runs through the payment options available on the platform, or any payment method Salla provides from time to time. Salla may at any time require payments to pass directly between merchant and consumer through their own bank accounts. Q5-SA-P0079, Q5-SA-P0081
- The agreement says the online payment service is provided to make things easier and to protect the rights of merchants and stores. Q5-SA-002
- The merchant undertakes to run the store's payments through the payment methods the agreement sets. Salla may block a payment that breaches the agreement, and may refuse, cancel or suspend purchases whether or not they are paid. Q5-SA-003, Q5-SA-P0082, Q5-SA-P0088
- Salla sets limits on electronic payment transactions by country and by product type. The limits may differ between stores, by store size, sector and Salla's own policies. A merchant cannot raise them manually. Q5-SA-047, Q5-SA-048, Q5-SA-049

### Plans, verification and the selling policy
- On باقة بيسك, a merchant can turn on bank transfer and cash on delivery. Electronic payment methods are available only on paid plans. Q5-SA-P0099, Q5-SA-P0098, Q5-SA-P0068
- Salla Payments in the UAE and Kuwait requires the Plus, Pro or Special plan. The dashboard's feature flags list the plans plus, pro and special for stc-pay, apple-pay, tamara, tabby, hyperpay and the other gateways. Q5-SA-K1522, Q5-SA-K1528, Q5-SA-K1510, Q5-SA-K1511, Q5-SA-K1614, Q5-SA-K1617, Q5-SA-K1643
- A method can need store verification first. The request to activate Salla Payments is reviewed during the verification review, and payment and settlement operations are suspended until verification is complete. Q5-SA-K0091, Q5-SA-K1527, Q5-SA-P0136
- Activating electronic payments includes agreeing to سياسة البيع. That policy states its aim and lists the products and services it bans outright. Q5-SA-K1532, Q5-SA-010, Q5-SA-011
- In the runs, the gateways answer for store merchant (the page shows بيسك), on 8 October 2026, marked مدى and the other quick methods `"blocked_by": "requires_paid_plan"`, with the reason "قم بترقية باقتك لتفعيل المدفوعات الإلكترونية". Its verification was uncompleted, with `"blocks_payment_activation": true`. Its طرق الدفع page said مدفوعات سلة is "متاحة في بلس وبرو وسبيشل", and that the store was not verified. Q5-SA-069, Q5-SA-070, Q5-SA-071, Q5-SA-072
- For store real-merchant (Pro, `"merchant_type": "KSA"`), on 12 October 2026, verification was completed, `"blocks_payment_activation": false`, and the summary showed `"has_approved_epayment_request": true`. Q5-SA-074
- The selling policy's clauses on who may change it, and on the Salla entity bound by it, were not in what was read. Q5-SA-G0169, Q5-SA-G0170

### Country
- Some methods are reserved for stores in Saudi Arabia: مدى, فيزا and Google Pay; STC Pay; and, in the payment-restrictions article, STC pay, cash on delivery and bank transfer. Q5-SA-036, Q5-SA-042
- Outside Saudi Arabia, Apple Pay turns on after verification and activation of Tap. Tamara and Tabby accounts are opened directly with them, and Mispay, Madfu and Emkan are not available. Q5-SA-027, Q5-SA-018, Q5-SA-019, Q5-SA-021
- Salla lists the UAE's and Kuwait's methods separately. Q5-SA-K1520, Q5-SA-K1521, Q5-SA-K1622, Q5-SA-K1623, Q5-SA-P0101

### Tamara, Tabby and Emkan
- The agreement says some providers set their own conditions and costs, over which Salla has no authority. Q5-SA-007
- Emkan is offered to stores verified with a commercial registration, and not to stores with a freelance document. In the comparison table, the products allowed for instalments are reviewed internally with the merchant. Q5-SA-020, Q5-SA-024, Q5-SA-022
- Further Tamara instalment options depend on the merchant's contract with Tamara and on the customer's eligibility. Tabby decides whether a customer or an order is eligible for its service. Q5-SA-025, Q5-SA-066
- Connecting Tabby needs the merchant's keys from the Tabby account, and agreement to Salla's terms of use. Q5-SA-068
- The terms of the merchant's own agreements with Tamara, Tabby and Geidea were not in what was read. Q5-SA-N03

## [2]

### التاجر
- The merchant turns methods on from the طرق الدفع page: chooses a method, presses (تفعيل) and completes its details. The merchant can turn electronic payments off with the payment methods toggle, and can turn off any active digital wallet. Q5-SA-017, Q5-SA-050, Q5-SA-039
- The staff permissions include payment_methods_activation (تفعيل وإلغاء تفعيل طرق الدفع). Q5-SA-K1509
- With Markets turned on, the طرق الدفع page has a market selector for managing each market's settings. Q5-SA-016
- Through payment restrictions (قيود الدفع), offered on Pro and Special only, the merchant picks the methods a rule restricts, its conditions (amount, quantity, customer or card country, customer group, categories, guest checkout, markets, partial-payment pairs) and its action: reject, review, or hide the method. Q5-SA-041, Q5-SA-043, Q5-SA-044, Q5-SA-045, Q5-SA-046, Q5-SA-051, Q5-SA-009, Q5-SA-K1666
- A dashboard setting hides cash on delivery from customers who are banned in other Salla stores. Q5-SA-059

### Gateway settings
- In the gateway settings, the merchant either connects an existing business account with the provider or sends a request to open one. The provider's team answers by email. A request can be rejected, and the merchant is told to ask the provider for the reasons. Q5-SA-052, Q5-SA-053, Q5-SA-054, Q5-SA-055, Q5-SA-056, Q5-SA-057
- The merchant's dealings with third-party service providers form an independent contractual relationship, under the agreement between merchant and provider. Q5-SA-005
- For apps, enabling the Recurring Payments scope goes through Salla Support. Q5-SA-063

## [3]

### طرق الدفع
- The طرق الدفع page has these sections: مدفوعات سلة; وسائل الدفع الآجل (Tabby, Tamara, MISpay, Madfu, Emkan); المحافظ الرقمية (PayPal); and طرق دفع أخرى, which includes bank transfer. Q5-SA-012, Q5-SA-013, Q5-SA-014, Q5-SA-015
- Salla describes Salla Payments as a Salla service that processes the store's payments and completes the financial operations with banks and payment methods. Apple Pay and STC Pay are turned on from the مدفوعات سلة section. Q5-SA-P0002, Q5-SA-028, Q5-SA-032
- salla.com/payments lists cards, mobile wallets, instalments and digital wallets, with American Express and Google Pay marked قريبًا. Q5-SA-008
- Other gateways (ميسر, هايبر باي) are connected with the merchant's own credentials. The dashboard tells the merchant that payments will then be collected through that gateway instead of Salla Payments. While a Tap connection is active, Salla Payments cannot be activated. Q5-SA-K1638, Q5-SA-K1656, Q5-SA-K1639, Q5-SA-K1653, Q5-SA-040
- Charities connect an external gateway instead of Salla's. Salla's guidance on gateways such as Moyasar or HyperPay is written for charities and digital stores. Q5-SA-P0073, Q5-SA-029, Q5-SA-030, Q5-SA-031, Q5-SA-058
- Cash on delivery runs either through Salla's shipping labels or through the merchant's own carrier. Point-of-sale card payments in Salla Point go through a Geidea account. Q5-SA-P0095, Q5-SA-K1598, Q5-SA-K1436
- The usage agreement defines مزود الخدمة as services Salla provides through third parties, where Salla only provides the connection. Q5-SA-004, Q5-SA-P0077, Q5-SA-006, Q5-SA-061
- The real store's gateways answer, on 12 October 2026, grouped its methods as online_payment_gateways (one item: slug salla, labelled noon), digital_wallets (paypal), bnpl (tabby, tamara, mispay, madfu, emkan) and other_payment_methods (mokafaa-alrajhi, cod). Q5-SA-073
- No list was found that is presented as the complete set of gateways a merchant can connect. The comparison page مقارنة بوابات الدفع is not held. Q5-SA-N04

### Apps
- Apps from Salla's App Store can hold the payments, transactions, settlements and subscriptions scopes. Q5-SA-K2048, Q5-SA-K2057, Q5-SA-K2058, Q5-SA-K2061
- The Recurring Payments feature lets merchants and third-party apps offer subscription billing. Once it is enabled, an app processes recurring payments through the API, and the payment goes through the gateway. Q5-SA-062, Q5-SA-064, Q5-SA-065, Q5-SA-K1695
- Paid apps are paid through Salla. Q5-SA-K2138

## [4]
- Salla may cancel, modify or change any payment method it made available. No notice or effect of this was found in what was read. Q5-SA-001, Q5-SA-N01
- If the Tap payment service is cancelled, the K net tap connection is cancelled automatically. Q5-SA-K1654
- A merchant already connected directly to stc pay can keep that connection, but cannot return to it after moving to Salla's gateway. Q5-SA-033, Q5-SA-K1627
- A charity store switching gateways is told that the current gateway will be replaced by the next. Q5-SA-058
- When activating an app, the merchant agrees that Salla may unlink or stop the app if there is a violation. Q5-SA-060
- The agreement disclaims Salla's responsibility for poor or late performance by gateways and banks, and for a provider's failure towards the merchant. Q5-SA-P0084, Q5-SA-005
- What happens when a payment partner is unavailable was not in what was read: where Salla handles it, the rule or setting that decides it, and its reason. Q5-SA-G0224, Q5-SA-G0225, Q5-SA-G0226

## [5]

### Salla Payments
- A customer's electronic payment goes first to رصيد المدفوعات الإلكترونية, and then to the merchant's bank account on the transfer cycle. Q5-SA-P0004, Q5-SA-P0005, Q5-SA-P0006, Q5-SA-P0007
- The transfer cycle depends on the plan (weekly, 48 hours, daily), with other minimums and days in the UAE and Kuwait. Q5-SA-P0020, Q5-SA-P0021, Q5-SA-P0022, Q5-SA-P0052, Q5-SA-P0062, Q5-SA-P0008
- Payouts go to the bank account given during store verification. Q5-SA-P0055, Q5-SA-K1562
- Payments are settled and transferred under the payment services contract (عقد خدمات الدفع) signed during verification. Q5-SA-P0054, Q5-SA-P0064
- These were not in what was read: the contract's parties, the entity or licence under which Salla Payments funds are held, who settles them, and in what capacity Salla receives them. Q5-SA-G0113, Q5-SA-G0114, Q5-SA-G0115, Q5-SA-G0177, Q5-SA-H0002, Q5-SA-H0004, Q5-SA-H0008
- When a merchant activates Salla's payment gateway, all payments are received in Saudi riyals. Q5-SA-P0168
- The real store's wallet summary, on 12 October 2026, listed three wallets: Wallet, Electronic Payments (salla_pay) and Cash on Delivery Payments (salla_cod), the second with its total fees and tax. Its last e-payment payout, paid, carried the hint "It will reach your account within 2-4 business days." Its online-payments wallet page took total fees and tax on fees from total payments to give total payouts. Q5-SA-075, Q5-SA-076, Q5-SA-077

### Tabby, Tamara, Mokafaa Al Rajhi, other gateways and PayPal
- Payments through Tabby are collected by Tabby, not by Salla Payments, and the store receives its dues under its agreement with Tabby. Q5-SA-P0102, Q5-SA-067
- Tamara is responsible for transferring the value of orders paid through Tamara to the merchant. Q5-SA-P0106
- Salla's comparison table names each BNPL service as the party collecting from the customer, and says the provider transfers amounts to the store periodically. Q5-SA-023, Q5-SA-026
- Payments are transferred by Mokafaa Al Rajhi to the merchant's own account with Mokafaa Al Rajhi. Q5-SA-P0108
- External gateways collect payments instead of Salla Payments. Q5-SA-K1639
- Salla's store wallet has no tab or balance for Tabby, Tamara, Mokafaa Al Rajhi, PayPal, an external gateway or bank transfer. Q5-SA-A0002
- PayPal is connected with the email of the merchant's PayPal account. Where PayPal payments go was not in what was read. Q5-SA-034, Q5-SA-035, Q5-SA-037, Q5-SA-038, Q5-SA-N02

### Bank transfer, cash on delivery and Salla Point
- With bank transfer, the customer transfers the order amount directly from their bank account to the merchant's. Q5-SA-P0099, Q5-SA-P0100
- Cash on delivery through the merchant's own carrier is settled directly between the merchant and the carrier, and Salla does not collect it. Through Salla's shipping labels, the carrier transfers the amount to Salla. Q5-SA-P0092, Q5-SA-P0091, Q5-SA-P0041, Q5-SA-P0042, Q5-SA-P0093
- In Salla Point, a successful card payment is transferred by bank transfer through the provider, such as Geidea. Q5-SA-K1435

### Salla Capital, shipping labels and settlements
- Salla Capital collects 25% of net sales from each payout, and transfers the rest to the merchant's bank account. Q5-SA-P0131, Q5-SA-P0132
- Shipping-label amounts are held from the e-payments balance and paid to the carrier by Salla. Q5-SA-P0126, Q5-SA-P0127, Q5-SA-P0128
- Dropshipping apps can withhold amounts from the merchant's wallet for settlement. Q5-SA-K1686, Q5-SA-K1690
