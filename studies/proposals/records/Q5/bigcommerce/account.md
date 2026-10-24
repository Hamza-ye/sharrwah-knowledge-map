# Q5 on BigCommerce: what its material shows

## [1]

### The merchant, in the control panel

- The merchant connects gateways and enables methods under Settings › Payments. That page is set per currency, with an Embedded tab and an Online Payment Methods section. Amazon Pay, Apple Pay and Google Pay sit under its Digital Wallets section, and Fastlane by PayPal is a box in a gateway's settings tab. Q5-BC-066, Q5-BC-093, Q5-BC-098, Q5-BC-P0048
- Enabling, disabling or changing a payment method shows a notification in the control panel dashboard, and the change is recorded in the Staff Action Logs. Q5-BC-072
- The merchant also sets payment methods for each transactional currency. A currency is transactional only when a gateway that supports it is enabled. Display currencies use the default currency's methods. All offline methods support additional transactional currencies, and a Set up button appears under Additional Currencies where a transactional currency has no method. Q5-BC-073, Q5-BC-074, Q5-BC-087, Q5-BC-088, Q5-BC-089, Q5-BC-090, Q5-BC-K0392, Q5-BC-K0397
- For offline methods, the merchant ticks the countries where each method is available at checkout. Q5-BC-P0121
- In B2B Edition, every method enabled at store level can be enabled or disabled per Company, but only methods integrated as standard checkout modules. Q5-BC-K0182, Q5-BC-K0184, Q5-BC-091
- Once enabled, local payment methods have country and currency prerequisites, so shoppers see only the methods for their geolocation. An APM's display name at checkout can't be customized. Q5-BC-081, Q5-BC-083

### BigCommerce

- BigCommerce publishes the gateway integrations it supports. The Payments API doesn't support gateways outside its list of compatible gateways. Q5-BC-075, Q5-BC-K0113, Q5-BC-K0118, Q5-BC-K0152
- BigCommerce sorts providers into Embedded and Open Payment Providers. Its terms incorporate those lists and the fee rates by reference. On self-serve plans, an Open Payment Provider fee applies per order to orders not processed through an Embedded provider. This includes offline methods and custom integrations to Embedded processors, among them those connected through third-party apps. It doesn't apply to contracted Performance plans. Q5-BC-003, Q5-BC-036, Q5-BC-080, Q5-BC-085, Q5-BC-100, Q5-BC-K0141, Q5-BC-K0143, Q5-BC-K0147, Q5-BC-K0148, Q5-BC-P0124
- The Embedded list is "based on current partner classifications". BigCommerce invites merchants to pick a provider by "country, currency, payment methods, and integration needs". Q5-BC-101, Q5-BC-103
- BigCommerce Payments is limited by the store's country, plan and checkout type, and by the PayPal account's country. Fastlane by PayPal is limited by gateway, checkout type, the store's and the account's country, the currency, and staff permissions. Q5-BC-095, Q5-BC-K0132, Q5-BC-P0055, Q5-BC-P0058, Q5-BC-P0068, Q5-BC-P0087
- Store-level conditions on other methods: PayPal isn't offered to stores in India or Israel. Pay Later is limited to stores in listed countries. Cryptocurrency payments are enabled for all merchants. Q5-BC-P0034, Q5-BC-P0092, Q5-BC-P0096, Q5-BC-P0113
- The Master Services Agreement makes the merchant solely liable for PCI compliance when it uses a payment provider for which Commerce provides no integration. Q5-BC-099
- No statement of BigCommerce's reasons for how payment methods or providers are placed was found. Q5-BC-G0044, Q5-BC-G0050

### Partners and providers

- A store onboarded through a "Powered By" partner may not have access to every listed gateway. Q5-BC-004, Q5-BC-N02
- Each provider has its own application process and underwriting, and an application doesn't guarantee approval. PayPal Braintree also reviews accounts periodically. Q5-BC-P0048, Q5-BC-P0063, Q5-BC-P0065, Q5-BC-K0145, Q5-BC-K0146
- For regulated items, the merchant is sent to its gateway's terms of service. Five gateways "may allow" their sale, and USA ePay requires Paysafe as Merchant Services Provider. Q5-BC-069, Q5-BC-070, Q5-BC-K0461
- Each gateway's own documentation sets its requirements, limitations and supported countries and currencies. Q5-BC-005

## [2]

- The parties named are: the merchant (Settings › Payments; B2B Company settings), BigCommerce (lists, fee classes, compatibility), the Powered By partner, and each provider (application, underwriting, terms). Q5-BC-004, Q5-BC-069, Q5-BC-091, Q5-BC-093, Q5-BC-P0048
- For Fastlane, Braintree stores and non-US PayPal stores must first configure it in the provider's own account or dashboard before enabling it in BigCommerce. Q5-BC-096, Q5-BC-097
- Third-Party Products are governed by their own terms, and any interaction with their provider is between the merchant and that provider. Q5-BC-K0453, Q5-BC-K0456
- No term names the party legally responsible for payment methods or digital wallets. Q5-BC-G0043, Q5-BC-G0051

## [3]

### Providers

- Available Payment Gateways lists 23 Embedded gateway integrations. For each, it marks Manual Capture, 3D Secure, Multicurrency, Stored Payment Methods, Recurring Payments and MSF Payments. Q5-BC-006, Q5-BC-007, Q5-BC-008, Q5-BC-009, Q5-BC-010, Q5-BC-011, Q5-BC-012, Q5-BC-013, Q5-BC-014, Q5-BC-015, Q5-BC-016, Q5-BC-017, Q5-BC-018, Q5-BC-019, Q5-BC-020, Q5-BC-021, Q5-BC-022, Q5-BC-023, Q5-BC-024, Q5-BC-025, Q5-BC-026, Q5-BC-027, Q5-BC-028, Q5-BC-029, Q5-BC-030
- It also lists 22 Open gateway integrations. Q5-BC-037, Q5-BC-038, Q5-BC-039, Q5-BC-040, Q5-BC-041, Q5-BC-042, Q5-BC-043, Q5-BC-044, Q5-BC-045, Q5-BC-046, Q5-BC-047, Q5-BC-048, Q5-BC-049, Q5-BC-050, Q5-BC-051, Q5-BC-052, Q5-BC-053, Q5-BC-054, Q5-BC-055, Q5-BC-056, Q5-BC-057, Q5-BC-058, Q5-BC-059
- The Embedded Payment Providers page names 21 providers. Q5-BC-101, Q5-BC-K0131, Q5-BC-K0144
- The integration counts differ between pages: "over 60" (230 countries), "more than 65" (150+ countries), and "65+ payment providers across 100+ countries". Q5-BC-075, Q5-BC-K0139, Q5-BC-P0036, Q5-BC-P0037, Q5-BC-P0038
- BigCommerce Payments is described as an embedded payment solution, powered by PayPal. It covers cards, PayPal, Venmo, Pay Later and digital wallets. Q5-BC-K0129, Q5-BC-K0150, Q5-BC-P0055, Q5-BC-P0067
- Hosted gateways send shoppers to the provider's page. They and most APMs and wallets don't support Embedded Checkout on headless storefronts. Q5-BC-068, Q5-BC-P0090

### Add-ons

- "App payment processors" (Acumatica Payments, Payfabric, Bankful, Sezzle, Fortis, Worldpay WPG, Klarna Checkout) count as Embedded Payment Providers. Other processors on the App Marketplace may carry the Open Payment Provider fee. Q5-BC-031, Q5-BC-032, Q5-BC-033, Q5-BC-034, Q5-BC-035, Q5-BC-071, Q5-BC-N03
- The App Marketplace has a Payments & Security category (91 apps) and a Financing category (14). Q5-BC-106, Q5-BC-107
- Apps are single-click or connector, reviewed by the Marketplace team. Q5-BC-K0315, Q5-BC-K0316
- Consumer financing integrations and BitPay are offered as integrations. Q5-BC-P0022, Q5-BC-P0023
- Orders created through the API, POS apps and marketplaces like eBay or Etsy also count as processed outside BigCommerce for the fee. Q5-BC-086

### Methods

- APMs are "typically offered through a cooperating payment gateway". BigCommerce classes them as bank transfers, direct debit, cash payment, digital wallets, mobile payments, and delayed or installment payments. Q5-BC-001, Q5-BC-065, Q5-BC-079, Q5-BC-082, Q5-BC-077
- A table names every APM that can be enabled, with its gateways and countries. Its rows weren't recorded. Q5-BC-084
- Cards and the wallets PayPal, Apple Pay, Google Pay and Amazon Pay are named. Accelerated Checkout comes as Stripe Link (through the Stripe gateways) and Fastlane by PayPal. Q5-BC-002, Q5-BC-067, Q5-BC-076, Q5-BC-K0151
- The offline methods are Bank deposit, Cash on delivery, Check, Money order and Pay in-store. B2B Edition uses Check for the Purchase Order (PO) method. Q5-BC-060, Q5-BC-061, Q5-BC-062, Q5-BC-063, Q5-BC-064, Q5-BC-078, Q5-BC-P0114, Q5-BC-P0116, Q5-BC-P0117, Q5-BC-P0118, Q5-BC-P0119, Q5-BC-P0120
- The Embedded Providers "integrate directly with the BigCommerce platform", with setup and support in the store's dashboard. Q5-BC-105

## [4]

- The Embedded list "may evolve over time", with advance notice of changes. Q5-BC-102, Q5-BC-K0144
- Commerce may stop supporting a Third-Party Product integration and migrate the subscription, or disable access to Third-Party Products at any time without notice. Q5-BC-K0454, Q5-BC-K0455
- In B2B Edition, a method configured other than as a standard checkout module may disappear from Company payment settings, and an enabled one "can be automatically removed" on the next refresh. Q5-BC-092
- Switching providers is put at two weeks to four months. BigCommerce Payments is disconnected per currency by a toggle, and switching its linked PayPal account means disconnecting and reconnecting. Q5-BC-093, Q5-BC-094, Q5-BC-104
- Stores using PayPal Checkout are moved to BigCommerce Payments in waves unless they opt out, and new transactions then go through the BigCommerce Payments account. Q5-BC-P0080, Q5-BC-P0081
- The legacy Stripe optimized_checkout method doesn't support Adaptive Pricing. Payment Methods V2 is kept only for existing integrations. Q5-BC-P0035, Q5-BC-K0121
- What checkout does when a connected provider is unavailable wasn't found. Neither was what happens when an integration is retired, or to funds when a provider is disconnected. Q5-BC-G0048, Q5-BC-N01, Q5-BC-H0040

## [5]

- For any gateway, "You will control and direct funds in your merchant account with your merchant service provider". Q5-BC-P0089
- BigCommerce Payments: PayPal processes payments through a new PayPal platform account linked to the merchant's PayPal Business account. Funds sit in a BigCommerce Payments balance shown in the Money/Balance dashboard. Payouts go to a linked bank account or PayPal account, and initial payments are held up to 21 days. Q5-BC-P0040, Q5-BC-P0052, Q5-BC-P0069, Q5-BC-P0073, Q5-BC-P0074, Q5-BC-P0075, Q5-BC-P0083
- PayPal: funds go immediately into the merchant's PayPal account, then to the bank on request. Stripe OCS: payouts follow the account's payout schedule. Braintree: funds reach the bank 2 to 5 days after settlement. Q5-BC-P0024, Q5-BC-P0091, Q5-BC-P0099, Q5-BC-P0108
- BitPay settles to the merchant's bank account. Pay Later and consumer financing pay the merchant up front. Q5-BC-P0022, Q5-BC-P0023, Q5-BC-P0025, Q5-BC-P0095
- Bank Deposit pays into the merchant's bank account, and Cash on delivery, Check, Money order and Pay in Store pay the merchant directly. Such orders sit in Awaiting Payment. Q5-BC-P0115, Q5-BC-P0116, Q5-BC-P0117, Q5-BC-P0118, Q5-BC-P0119, Q5-BC-P0120
- Settlement currency is set with the provider. Q5-BC-K0396, Q5-BC-P0014, Q5-BC-P0027
- Who holds funds between payment and payout wasn't found, nor under whose licence or terms, nor who sends payouts for most providers. Q5-BC-H0002, Q5-BC-H0003, Q5-BC-H0007, Q5-BC-H0008, Q5-BC-H0033, Q5-BC-G0047, Q5-BC-G0049
