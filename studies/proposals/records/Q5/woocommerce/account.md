# Q5 on WooCommerce: check

## [1]

- **differs** (role): methods are turned on in the **Payments** settings (menu item needs `manage_woocommerce`); each core offline gateway has an "Enable/Disable" box, off by default. Against Shopify [1]: Q5-SH-K1524; Shopify [1]: Q5-SH-K0193; Salla [2]: Q5-SA-017; Salla [2]: Q5-SA-K1509; BigCommerce [1]: Q5-BC-066. Q5-WC-K0002, Q5-WC-K0004, Q5-WC-001, Q5-WC-K0032, Q5-WC-K0033, Q5-WC-K0034, Q5-WC-012
- **differs** (role): `woocommerce_available_payment_gateways` lets code drop gateways; a gateway can set `max_amount`. Against Shopify [1]: Q5-SH-K1761; Salla [2]: Q5-SA-041; Salla [1]: Q5-SA-047. Q5-WC-002, Q5-WC-K0019, Q5-WC-003
- **differs** (role): Cash on delivery can be limited by shipping method and to non-virtual orders. Against BigCommerce [1]: Q5-BC-P0121. Q5-WC-004, Q5-WC-005
- **differs** (role): extensions are suggested by store country, in priority order (`IR` is empty); suggestions can be turned off. Against Shopify [1]: Q5-SH-K1526; BigCommerce [1]: Q5-BC-075; BigCommerce [1]: Q5-BC-P0034. Q5-WC-K0054, Q5-WC-K0055, Q5-WC-K0059, Q5-WC-K0315, Q5-WC-K0056, Q5-WC-K0057
- **differs** (role): WooPayments "is not required" and can run with the Stripe plugin "at the same time", but not with an existing Stripe account. Against Shopify [1]: Q5-SH-017; Shopify [1]: Q5-SH-001; Shopify [1]: Q5-SH-038. Q5-WC-K0359, Q5-WC-018, Q5-WC-031, Q5-WC-K0713
- **differs** (role): WooPayments is open in supported countries, by where a business is registered; card networks, processors and their financial service providers bar some businesses; Woo may refuse or suspend accounts. Against Shopify [1]: Q5-SH-K1532; Salla [1]: Q5-SA-K1532; BigCommerce [1]: Q5-BC-095. Q5-WC-K0400, Q5-WC-K0402, Q5-WC-K0406, Q5-WC-K0405, Q5-WC-K0416, Q5-WC-K0422, Q5-WC-K0418, Q5-WC-A0002
- **differs** (role): local methods, BNPL and WooPay come with WooPayments, by its account country; WooPay is U.S.-only; BNPL also depends on the buyer's country, currency and cart total. Against Shopify [1]: Q5-SH-K2661; Shopify [1]: Q5-SH-K1745; Salla [1]: Q5-SA-036. Q5-WC-006, Q5-WC-008, Q5-WC-009, Q5-WC-021, Q5-WC-023, Q5-WC-K0446, Q5-WC-K0447, Q5-WC-K0448
- **differs** (role): providers decide too: Alipay and WeChat Pay review merchants and bar businesses; methods depend on "account status"; P24 reviews merchants continuously; CBD sellers must use Square or Viva Wallet. Against Salla [1]: Q5-SA-007; Salla [1]: Q5-SA-025; Salla [1]: Q5-SA-K0091; BigCommerce [1]: Q5-BC-P0048 ("Each provider has"); BigCommerce [1]: Q5-BC-069. Q5-WC-007, Q5-WC-010, Q5-WC-011, Q5-WC-014, Q5-WC-K0417, Q5-WC-K0350
- **differs** (role): gateways are "additional plugins"; a Marketplace "Payments Solution" needs a separate agreement. Against Shopify [1]: Q5-SH-K1696; Shopify [1]: Q5-SH-K1700. Q5-WC-K0007, Q5-WC-K0353, Q5-WC-K0354
- **differs** (role): WooPayments may use third-party payment processors, including "an alternative third-party payment processor". Against Shopify [1]: Q5-SH-K1560; Salla [1]: Q5-SA-P0079. Q5-WC-K0368, Q5-WC-K0712, Q5-WC-P0018
- **differs** (role): extensions have "their own requirements … and terms"; WooPayments creates a Stripe Express account. Against Shopify [1]: Q5-SH-053; BigCommerce [1]: Q5-BC-005; Salla [2]: Q5-SA-052. Q5-WC-K0830, Q5-WC-P0023, Q5-WC-K0371
- **differs** (role): a gateway declares whether it supports `subscriptions`. Against Shopify [1]: Q5-SH-003. Q5-WC-029, Q5-WC-030
- **differs** (role): POS card payments use WooPayments or Stripe, in listed countries and the default currency. Against Shopify [1]: Q5-SH-K2930. Q5-WC-026, Q5-WC-K0439, Q5-WC-K0440, Q5-WC-K1320, Q5-WC-K1321
- **differs** (role): "PCI DSS compliance is ultimately the responsibility of the store owner". Against BigCommerce [1]: Q5-BC-099. Q5-WC-040
- **not in what was read:** a plan level that decides which methods a store can use. Against Salla [1]: Q5-SA-P0099. Q5-WC-N09
- **not in what was read:** a platform fee that depends on which provider processed an order. Against BigCommerce [1]: Q5-BC-003. Q5-WC-N08
- **not in what was read:** a provider offered only to merchants it has already approved. Against Shopify [1]: Q5-SH-071. Q5-WC-N13
- **not in what was read:** which method is selected in advance at checkout. Against Shopify [1]: Q5-SH-004. Q5-WC-N14
- **not in what was read:** a step in which the platform enables an extension before merchants can use it. Against Shopify [1]: Q5-SH-058. Q5-WC-N15
- **not in what was read:** fewer gateways for stores set up through a partner. Against BigCommerce [1]: Q5-BC-004. Q5-WC-N16

## [2]

- **differs** (role): third parties' terms "may apply"; Woo is "not involved". Against BigCommerce [2]: Q5-BC-K0453; Salla [2]: Q5-SA-005. Q5-WC-K0009, Q5-WC-K0010, Q5-WC-K0832
- **differs** (role): BNPL turns on once Stripe verifies the merchant's information; some details change only in the Stripe Express dashboard. Against BigCommerce [2]: Q5-BC-096. Q5-WC-022, Q5-WC-K0722

## [3]

- **differs** (role): WooPayments is "the only payment gateway designed by Woo for Woo". Against Shopify [3]: Q5-SH-K1533; Salla [3]: Q5-SA-P0002; BigCommerce [3]: Q5-BC-K0129. Q5-WC-K0363, Q5-WC-K0361, Q5-WC-017
- **differs** (role): gateway types are Form based, iFrame based, Direct and Offline; core has Direct bank transfer, Check payments and Cash on delivery. Against BigCommerce [3]: Q5-BC-068; BigCommerce [3]: Q5-BC-060; Shopify [3]: Q5-SH-K1533. Q5-WC-016, Q5-WC-K0025, Q5-WC-K0026, Q5-WC-K0027
- **differs** (role): gateways are plugins built on `WC_Payment_Gateway`, `WC_Payment_Gateway_CC` or `WC_Payment_Gateway_ECheck`, and loaded through `woocommerce_payment_gateways`. Against Shopify [3]: Q5-SH-K1694. Q5-WC-K0006, Q5-WC-K0013, Q5-WC-K0014, Q5-WC-K0015, Q5-WC-K0016, Q5-WC-K0017
- **differs** (role): "Official payments" splits into Processors & gateways, Wallets & express checkouts, Buy now pay later, Crypto payments, B2B payments and In-person payments; suggestions are typed `psp`, `apm`, `express_checkout`, `bnpl`, `crypto`. Against BigCommerce [3]: Q5-BC-106; BigCommerce [3]: Q5-BC-001. Q5-WC-K0337, Q5-WC-K0338, Q5-WC-K0339, Q5-WC-K0340, Q5-WC-K0341, Q5-WC-K0342, Q5-WC-K0343, Q5-WC-039
- **differs** (role): WooPayments builds in express checkouts, BNPL (Affirm, Afterpay, Klarna) and local methods. Against Shopify [3]: Q5-SH-P0052; Shopify [3]: Q5-SH-K1741; BigCommerce [3]: Q5-BC-002. Q5-WC-019, Q5-WC-020, Q5-WC-006
- **differs** (term): Third-Party Services include extensions and point-of-sale terminals, and "aren't vetted, endorsed, or controlled by Automattic". Against Shopify [3]: Q5-SH-K1721; BigCommerce [3]: Q5-BC-031. Q5-WC-K0827, Q5-WC-K0831, Q5-WC-037, Q5-WC-038
- **differs** (role): WooPayments "is powered by Stripe"; the Stripe entity depends on the account country. Against Shopify [3]: Q5-SH-K1555. Q5-WC-K0008, Q5-WC-P0108, Q5-WC-P0140
- **differs** (role): paid extensions are sold on WooCommerce.com, and WooCommerce pays the vendor 70%. Against Salla [3]: Q5-SA-K2138. Q5-WC-K0735, Q5-WC-K0461
- **differs** (role): "Our developers vet each new extension". Against BigCommerce [3]: Q5-BC-K0315. Q5-WC-K0828
- **differs** (identifier): REST access to `payment_gateways` needs `manage_woocommerce`. Against Salla [3]: Q5-SA-K2048. Q5-WC-041
- **differs** (role): POS mode takes Tap to Pay, card readers or cash. Against Salla [3]: Q5-SA-P0095. Q5-WC-027, Q5-WC-K0438

## [4]

- **differs** (role): P24 "can no longer be enabled" on new accounts, by Przelewy24's rule; revoked access makes orders "fail at checkout". Against Salla [4]: Q5-SA-033; Shopify [4]: Q5-SH-016. Q5-WC-013, Q5-WC-014, Q5-WC-015
- **differs** (role): PayPal Standard isn't loaded on new installs, but stays where it is enabled or has orders. Against Shopify [4]: Q5-SH-016; Shopify [4]: Q5-SH-015. Q5-WC-K0042, Q5-WC-K0044
- **differs** (role): before disabling WooPayments, enable another gateway; keep the plugin 6 months for refunds and disputes; Stripe Billing renewals continue. Against Shopify [4]: Q5-SH-015; BigCommerce [4]: Q5-BC-093. Q5-WC-032, Q5-WC-033, Q5-WC-034, Q5-WC-035, Q5-WC-036
- **differs** (role): opting out of Stripe's updated agreement ends WooPayments; the balance is still paid out. Against Shopify [4]: Q5-SH-K1564. Q5-WC-K0485, Q5-WC-K0714, Q5-WC-K0715
- **differs** (role): Woo may end access or force refunds "if a payment processor or regulatory authority requires it". Against Salla [4]: Q5-SA-001. Q5-WC-K0716
- **differs** (role): Woo may remove a Product "from the Marketplace(s) and/or a User's Website". Against Shopify [4]: Q5-SH-K2168; Salla [4]: Q5-SA-060; BigCommerce [4]: Q5-BC-K0454. Q5-WC-K0462
- **not in what was read:** what a developer owes merchants when it stops supporting an extension. Against Shopify [4]: Q5-SH-063. Q5-WC-N06
- **not in what was read:** notice before the suggested providers change. Against BigCommerce [4]: Q5-BC-102. Q5-WC-N07

## [5]

- **differs** (role): WooPayments payments, minus fees, go to the account balance, then after a pending period to a bank account or U.S. debit card, daily by default. Against Shopify [5]: Q5-SH-K1555; Salla [5]: Q5-SA-P0004; Salla [5]: Q5-SA-P0020; Salla [5]: Q5-SA-P0055; BigCommerce [5]: Q5-BC-P0040. Q5-WC-P0024, Q5-WC-P0027, Q5-WC-P0034, Q5-WC-P0036, Q5-WC-P0038, Q5-WC-K0431
- **differs** (role): Stripe, as agent, holds funds in Pooled Accounts and controls reserves; in the UAE, Network International holds them. Against Shopify [5]: Q5-SH-K1555; Salla [5]: Q5-SA-P0054. Q5-WC-P0103, Q5-WC-P0121, Q5-WC-P0124, Q5-WC-P0111, Q5-WC-P0143
- **differs** (role): a payment in a currency with no matching bank account is converted to the default currency. Against Salla [5]: Q5-SA-P0168; BigCommerce [5]: Q5-BC-K0396. Q5-WC-P0049, Q5-WC-P0051
- **differs** (role): BNPL pays WooPayments "the entire purchase amount immediately"; the provider collects instalments and interest. Against Shopify [5]: Q5-SH-028; Salla [5]: Q5-SA-P0102; BigCommerce [5]: Q5-BC-P0022. Q5-WC-P0056, Q5-WC-024, Q5-WC-025
- **differs** (role): direct bank transfer customers pay "directly via their bank account"; such and check orders stay On hold. Against Salla [5]: Q5-SA-P0099; BigCommerce [5]: Q5-BC-P0115; Shopify [5]: Q5-SH-K1737. Q5-WC-P0094, Q5-WC-P0095, Q5-WC-K0037, Q5-WC-P0096
- **differs** (role): Cash on delivery is paid at delivery, and the merchant marks a POS cash payment complete. Against Salla [5]: Q5-SA-P0092; BigCommerce [5]: Q5-BC-P0115. Q5-WC-P0097, Q5-WC-K0039, Q5-WC-028
- **differs** (role): PayPal Standard pays the merchant's PayPal Business email, capturing through a WordPress.com proxy. Against Shopify [5]: Q5-SH-030; BigCommerce [5]: Q5-BC-P0024; Salla [5]: Q5-SA-034. Q5-WC-P0157, Q5-WC-P0102, Q5-WC-P0101
- **differs** (role): Woo can't help with Stripe extension payouts; release timing wasn't read. Against Shopify [5]: Q5-SH-P0050; Shopify [5]: Q5-SH-064. Q5-WC-P0159, Q5-WC-H0003
- **differs** (role): Stripe Capital is repaid from a share of daily transactions. Against Salla [5]: Q5-SA-P0131. Q5-WC-P0074
- **goes beyond:** Woo is "not involved" in the merchant's transactions, WooPay ones included. Q5-WC-P0006, Q5-WC-P0010
- **goes beyond:** a FROD balance is "a special bucket of funds" inside the WooPayments account. Q5-WC-042
- **not in what was read:** where money from third-party extensions is held. Against BigCommerce [5]: Q5-BC-P0089. Q5-WC-N01
- **not in what was read:** where crypto payments go. Against Shopify [5]: Q5-SH-K1756. Q5-WC-N02
- **not in what was read:** where in-person card payments go. Against Salla [5]: Q5-SA-K1435. Q5-WC-N03
- **not in what was read:** platform services charged to the balance. Against Salla [5]: Q5-SA-P0126. Q5-WC-N04
- **not in what was read:** extensions withholding from the balance. Against Salla [5]: Q5-SA-K1686. Q5-WC-N05
- **not in what was read:** buyer credit paid into payouts. Against Shopify [5]: Q5-SH-074. Q5-WC-N10
- **not in what was read:** cross-border money held with a partner. Against Shopify [5]: Q5-SH-K1600. Q5-WC-N11
- **not in what was read:** a backup provider for card payments. Against Shopify [5]: Q5-SH-040. Q5-WC-N12
- **not in what was read:** separate balances for each provider. Against Salla [5]: Q5-SA-A0002. Q5-WC-N17
