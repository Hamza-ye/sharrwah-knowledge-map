# Q5 on Shopify: account

## [1]

### The merchant, in Settings > Payments

- Customers can pay with any of the methods the merchant has activated in the **Payment providers** area of the admin. The merchant manages all of the store's payment methods there. Q5-SH-K1524, Q5-SH-005, Q5-SH-K1193, Q5-SH-K2854, Q5-SH-K2859
- For credit cards the merchant can use Shopify Payments, a third-party provider, or both together. Only one credit card payment provider can be active at a time. Q5-SH-001, Q5-SH-008
- Only the store owner can add or change a payment provider, activate or switch to Shopify Payments, or edit PayPal Express information. Q5-SH-009, Q5-SH-010, Q5-SH-K1542, Q5-SH-K1717
- The admin pages for payment settings require the `MANAGE_PAYMENTS_SETTINGS` or `SHOPIFY_PAYMENTS` permissions. Q5-SH-K0193, Q5-SH-K0198, Q5-SH-K2856, Q5-SH-K2860
- With **Payment Customization** (a Shopify Function), an app can rename, reorder or hide the payment methods shown at checkout. A store can have at most 25 such functions, and hiding specific placements is only available on Shopify Plus stores. Q5-SH-K1761, Q5-SH-K1764, Q5-SH-K1765, Q5-SH-K0925

### Shopify, by country, plan, configuration and business

- Shopify tells merchants to choose payment gateways that are compatible and available in their region. Its list of payment gateways by country is the reference. The third-party provider list in the admin is filtered by the store's address in Settings > General. Being listed on the gateways page doesn't guarantee that a provider can be reached in a given store's admin. Q5-SH-K1526, Q5-SH-002, Q5-SH-012, Q5-SH-013, Q5-SH-019, Q5-SH-018, Q5-SH-020, Q5-SH-N03
- Where Shopify Payments is supported, Stripe can't be activated, and standalone Stripe isn't an alternative for a merchant who can't activate Shopify Payments. Q5-SH-017, Q5-SH-K1527, Q5-SH-K1528
- Shopify Payments is only for eligible merchants. The merchant must be a business located in its Designated Country, and there are prohibited businesses, sanctions and KYC checks. Prohibited and Restricted Business categories may be imposed by law, through Payment Network Rules, by Shopify, or by a Payment Processor's Financial Services Providers. Q5-SH-K1532, Q5-SH-K1536, Q5-SH-K1540, Q5-SH-K2262, Q5-SH-K2265, Q5-SH-K2268, Q5-SH-K1622, Q5-SH-A0002
- Some methods require Shopify Payments: local payment methods, Shop Pay Installments, Amazon Pay with Shopify Payments, Managed Markets, and manual payments in more than one currency. Q5-SH-K2661, Q5-SH-K1689, Q5-SH-067, Q5-SH-K1957, Q5-SH-K1739
- Subscription products need Shopify Payments as the primary payment gateway. Third-party subscription apps need one of these gateways: Shopify Payments, PayPal Express, Authorize.net, Adyen or Stripe. Availability depends on the region and on the gateway's terms of service. Q5-SH-003, Q5-SH-076, Q5-SH-077
- POS must use the same payment processor as the online store. Q5-SH-K2930, Q5-SH-K1784
- Adyen is open only to organizations that already have Adyen approval. Activating it as the primary gateway deactivates Shopify Payments. Q5-SH-071, Q5-SH-072, Q5-SH-073
- Shopify Payments alongside a third-party provider: the store must be in a supported country and have an active direct third-party provider. Plus merchants with signed contracts aren't eligible, and multi-entity setups can't use it. Only one direct third-party provider is allowed, and payment recovery can't be turned off. Q5-SH-038, Q5-SH-039, Q5-SH-046
- For customers based in Finland, no payment method is selected by default at checkout. Q5-SH-004

### Shopify, over payments apps and the Payment Processors

- Only approved Partners can build payments extensions, and payments apps must be approved by Shopify. Payment providers apply to become a Payments Developer. Shopify decides, at its sole discretion, whether a Payments Application goes on its public list of payment gateways, and reviews new payment methods added to an app. An app that isn't publicly listed can be installed through a shareable installation link. Q5-SH-K1696, Q5-SH-K1697, Q5-SH-K1699, Q5-SH-059, Q5-SH-060, Q5-SH-061, Q5-SH-062, Q5-SH-K1698
- Once the payments app marks itself ready, Shopify enables it to be activated, and then the merchant activates it. Q5-SH-058
- Custom payment extensions are only for eligible Shopify Plus merchants. Q5-SH-K1700
- Within Shopify Payments, the merchant authorizes Shopify to decide which Payment Processor Accounts are opened and which processor handles each transaction. Shopify may change the Payment Processors. Q5-SH-K1560, Q5-SH-P0011, Q5-SH-K1561, Q5-SH-K1562
- Managed payment methods are activated according to the regions where the merchant sells. Q5-SH-K1745
- Each additional payment method app has its own requirements, typically an account with the payment provider. Third-party providers may require the merchant's bank account information. Q5-SH-053, Q5-SH-011

### What the admins of stores with countryCode YE or Store address Yemen showed

- In store ibx5bt-xy (countryCode YE, currencyCode YER), observed on 30 September 2026, the admin's answers gave Shopify Payments, Amazon Pay and PayPal Express Checkout as `"eligible":false`, and Stripe as `"available":false,"eligible":false`. Q5-SH-078, Q5-SH-080, Q5-SH-081, Q5-SH-082
- In store fake-demo-sharrwah (countryCode YE), observed on 5 October 2026, the answer gave `"thirdPartyDirectEligible":true` and `"thirdPartyAdditionalPaymentMethodsEligible":true`. Its Third-party payment providers page listed (for testing) Bogus Gateway, Cybersource, Integration-UseePay, PagBrasil - Cartão de crédito and Tap Payments. Its Payments page showed ONERWAY (Direct) in test mode, with "0.6% transaction fee • Card rates set by ONERWAY (Direct)". Q5-SH-084, Q5-SH-085, Q5-SH-086
- In the saved HTML of store ibx5bt-xy's Third-party payment providers page, observed on 30 September 2026, six providers were listed: (for testing) Bogus Gateway, Cybersource, Integration-UseePay, ONERWAY (Direct), PagBrasil - Cartão de crédito and Tap Payments, each with its card labels (Tap Payments's include Mada, Benefit and OmanNet). Q5-SH-094
- In store capture-plus (Store address Yemen, Development store, Yemeni Rial (YER)), observed on 2 October 2026 under a page title ending Shopify Plus, the saved HTML of the same page listed Cybersource, Integration-UseePay, ONERWAY (Direct), PagBrasil - Cartão de crédito and Tap Payments. Its Payments page held the heading "Development stores can only process test payments", with "Activate the test payment provider , or set your payment provider to test mode." Q5-SH-095, Q5-SH-096
- In store ts15uk-ug (countryCode YE), observed on 7 October 2026, the Payments page described Payment providers as "Providers that enable you to accept payment methods at a rate set by the third-party", and said "An additional fee will apply to new orders once you select a plan." Q5-SH-090

## [3]

- Shopify names these kinds: Shopify Payments, which it calls "the only payment gateway designed and operated by Shopify"; third-party credit card payment providers, over 100 of them, either **direct providers** or **external providers**; **Additional payment methods**, such as PayPal Express Checkout, buy now pay later services and regional payment methods, some of which are installed as apps; accelerated checkouts; and manual payment methods. Q5-SH-K1533, Q5-SH-006, Q5-SH-007, Q5-SH-049, Q5-SH-050, Q5-SH-051, Q5-SH-052, Q5-SH-K1725, Q5-SH-K1735, Q5-SH-027
- The Getting paid table lists each payment provider with its type: **Payment gateway** for Shopify Payments, Amazon Pay and Shop Pay Installments, and **Accelerated checkout** for Apple Pay, Amazon Pay on Shopify Payments, Google Pay, PayPal Express Checkout, PayPal Wallet and Shop Pay. Q5-SH-P0052, Q5-SH-028, Q5-SH-029, Q5-SH-030, Q5-SH-031, Q5-SH-032, Q5-SH-033, Q5-SH-034, Q5-SH-035, Q5-SH-036
- Shopify Payments also carries local payment methods and USDC. Q5-SH-K1741, Q5-SH-K1751, Q5-SH-K2760
- Add-ons on the developer side are payments extensions built with the Payments Apps API. There are five types: credit card, custom credit card, alternative, offsite and redeemables. The methods they support are cards, buy now pay later, bank transfers, cryptocurrency, cash and ATM, and wallets. Q5-SH-K1694, Q5-SH-056, Q5-SH-057, Q5-SH-K1695, Q5-SH-K1159
- Apple Pay, Google Pay, Meta Pay, Amazon Pay and PayPal Express Checkout are each a "Third Party Service" under section 9.9 of the Terms of Service. Q5-SH-K1721, Q5-SH-K1722, Q5-SH-K1723, Q5-SH-K1724, Q5-SH-K1711
- Shopify Payments is run with Payment Processors (Stripe entities, PayPal, Adyen, and others, by Designated Country). In the EU/EEA and UK it runs as Payment Facilitator, with Adyen N.V. as Acquirer. Q5-SH-K1555, Q5-SH-K1566, Q5-SH-K1574, Q5-SH-K1576, Q5-SH-K1607, Q5-SH-K1611
- In the stores observed: store ibx5bt-xy's answer listed the manual providers Cash on Delivery (COD), Money Order and Bank Deposit, each with `"group":"MANUAL"`, and gave `"localPaymentMethodsForMerchantCountry":[]`. Q5-SH-083, Q5-SH-079
- In store fake-demo-sharrwah, the third-party provider ONERWAY (Direct) was answered with `"kind":"app"`, and the answer behind the Add payment method page listed providers such as Tabby and Tap Payments. Q5-SH-087, Q5-SH-088, Q5-SH-089
- In store capture-plus, the saved HTML of the Test payment gateway page described it as "Use to test Shopify checkout. No transaction fees will be charged." Q5-SH-097
- In store ts15uk-ug, the Payments page's "More ways to pay" read "Offer methods processed offsite or through custom checkout integrations". Q5-SH-091

## [4]

- **Shopify Payments processors:** if a Payment Processor terminates its terms, Shopify may, but need not, offer a substitute processor. Shopify may add, remove or replace an Acquirer. Q5-SH-K1564, Q5-SH-K1604, Q5-SH-K1605
- **Third Party Services:** Shopify "may disable access to any Third Party Services at any time in its sole discretion and without notice". Q5-SH-K2168
- **Third-party providers moving to new integrations:** the way third-party providers connect to Shopify is being updated, with notices and banners in the admin. A provider with no updated integration means the merchant must choose a new provider. The PayPal Payflow/Payments Pro gateways must move to the Braintree payments app, and Shop Pay must be reactivated after the update. Q5-SH-021, Q5-SH-022, Q5-SH-023, Q5-SH-024, Q5-SH-025
- **Discontinued integrations:** ActiveMerchant is no longer used to integrate gateways. Since January 6, 2025, the Amazon Pay third-party integration is no longer supported, and stores in the United States can offer Amazon Pay with Shopify Payments instead. Q5-SH-016, Q5-SH-068
- **Shop Pay Express:** it is being replaced by Shopify Payments alongside a third-party provider. Basic, Shopify and Advanced stores are migrated automatically, and Plus stores opt in or keep it until their contract allows. Q5-SH-047, Q5-SH-048
- **After a change or deactivation:** a previous provider, or a deactivated additional payment method app, stays available for order returns. Shopify warns against uninstalling such an app, because it then can't be used for outstanding returns. Q5-SH-015, Q5-SH-054, Q5-SH-055
- **Deactivating a third-party provider, in one store:** in store fake-demo-sharrwah (countryCode YE), observed on 30 September 2026, the saved HTML of the ONERWAY (Direct) page held a dialog that read "If you deactivate ONERWAY (Direct), it will be removed as a payment option from your checkout. Your existing orders will not be affected and can still be managed from the orders page." Q5-SH-098
- **Payments apps (Partner Program Agreement):** an app must let merchants end their agreement with the provider on 7 days' notice, without penalty. If the developer stops supporting the app, a Wind Down Period of up to six months applies: support continues, a transition plan is agreed, and the developer must notify merchants of the date the app stops. Shopify may remove an app from its public list, or end its access, for breach. Q5-SH-063, Q5-SH-K1704, Q5-SH-065, Q5-SH-066

## [5]

- **Shopify Payments:** processing and settlement are carried out by the Payment Processors and their Financial Services Providers. Funds are held in Payment Processor Accounts and paid out to the merchant's payout bank account, or to a Shopify Balance account where it applies, net of fees, refunds, chargebacks and any reserves. Q5-SH-K1555, Q5-SH-K1596, Q5-SH-P0010, Q5-SH-P0060, Q5-SH-P0069, Q5-SH-P0151, Q5-SH-P0028, Q5-SH-K1799
- **Through Shopify Payments:** Apple Pay, Google Pay, Shop Pay, Shop Pay Installments, Amazon Pay on Shopify Payments, and PayPal Wallet in France and the United States. Shop Pay Installments is provided with Affirm, and the merchant receives the full payment in Shopify Payments payouts. Q5-SH-028, Q5-SH-029, Q5-SH-031, Q5-SH-032, Q5-SH-034, Q5-SH-035, Q5-SH-036, Q5-SH-K1686, Q5-SH-P0055, Q5-SH-K1690, Q5-SH-070
- **Local payment methods:** paid out in Shopify Payments payouts. Q5-SH-K1742
- **Shop Cash:** credited to the Shopify Payments balance and included in the next payout. There is no separate account. Q5-SH-074, Q5-SH-075, Q5-SH-K1758
- **Managed Markets:** Shopify Payments holds the money in a Global-e account, and payouts are processed daily, net of Permitted Deductions. Q5-SH-K1600, Q5-SH-K1601, Q5-SH-P0102, Q5-SH-P0143
- **Paid by the provider:** Amazon Pay's third-party integration pays "By Amazon", and PayPal Express Checkout pays "By PayPal", with its own methods of transferring funds. Q5-SH-030, Q5-SH-033, Q5-SH-069, Q5-SH-K1712, Q5-SH-P0051
- **Third-party credit card providers:** the amount is transferred to the merchant's merchant account. Payout information isn't visible in the admin, and Shopify says to check with the provider. Q5-SH-P0050, Q5-SH-026, Q5-SH-N02
- **Shopify Payments alongside a third-party provider:** cards go to the third-party provider, with Shopify Payments as backup. Shop Pay, local methods and wallets the third party doesn't offer go to Shopify Payments. Q5-SH-040, Q5-SH-041, Q5-SH-042, Q5-SH-043, Q5-SH-044, Q5-SH-045, Q5-SH-037
- **Payments apps:** they must settle transactions for merchants within 5 days at most. Q5-SH-064
- **Cryptocurrency:** paid directly by customers on-chain, or settled into a Payment Processor Account (Bridge, an affiliate of Stripe). Coinbase takes no custody. Q5-SH-K1756, Q5-SH-K1752, Q5-SH-K1754, Q5-SH-K1578
- **Manual payment methods:** the merchant arranges to receive the payment, and such orders are marked unpaid. Q5-SH-K1737, Q5-SH-K1736, Q5-SH-027
- **Marked as paid, in one store:** in store demo-fake-dev-store (countryCode YE), observed on 30 September 2026, the Mark as paid dialog said "Mark this order as paid if you received YER 699.95 from another payment method", and the order's timeline then showed "You manually marked YER699.95 as paid for this order." Q5-SH-092, Q5-SH-093
- **Not read:** Amazon's customer agreement and policies. Q5-SH-N01
