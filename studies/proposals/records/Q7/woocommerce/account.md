# Q7 on WooCommerce, sorted against the Shopify and Zid accounts

## [1]

### Store currency
- **differs** (role): One base currency per store. `woocommerce_currency` "controls what currency prices are listed at in the catalog and which currency gateways will take payments in"; the base currency displays product prices and records new orders. Shopify [1]: Q7-SH-K1934; Zid [1]: Q7-ZD-002. Q7-WC-K0745 Q7-WC-K0746 Q7-WC-K0747 Q7-WC-024
- **differs** (role): Analytics data is converted into the store's default currency; Analytics > Orders has a Customer currency column. Shopify [1]: Q7-SH-074. Q7-WC-021 Q7-WC-022
- **differs** (identifier): The REST API has a `data-currencies` route; an order has one `currency`, "Currency the order was created with, in ISO format", also a column of the orders table. Shopify [1]: Q7-SH-K2893, Q7-SH-124; Zid [1]: Q7-ZD-005, Q7-ZD-008. Q7-WC-K0750 Q7-WC-055 Q7-WC-056

### Shown to and paid by buyers
- **differs** (term): WooPayments' **customer currency**, "displayed to customers while they browse your store and the currency they are charged in", is also called the "presentment currency". It defaults to the store currency; multi-currency can change it. Shopify [1]: Q7-SH-K1941, Q7-SH-122; Zid [1]: Q7-ZD-K0300 ("With مدفوعات زد active"). Q7-WC-002 Q7-WC-003 Q7-WC-K0754 Q7-WC-K0752
- **differs** (role): Core needs a multi-currency extension to show or charge another currency. WooPayments' free multi-currency lets customers pick from a list the seller defines, and changes only how prices are shown, not payouts. The Currency Converter Widget changes display only. Shopify [1]: Q7-SH-K1937; Zid [1]: Q7-ZD-K0300 ("With مدفوعات زد active"). Q7-WC-K0751 Q7-WC-010 Q7-WC-011 Q7-WC-028 Q7-WC-029
- **differs** (role): WooPayments accepts payments in over 100 currencies. Shopify [1]: Q7-SH-135. Q7-WC-001
- **differs** (role): Local payment methods show only when billing country and customer currency meet a table from Alipay to WeChat Pay (Bancontact, EPS, iDEAL | Wero: EUR; GrabPay: SGD; P24: EUR or PLN). Alipay's checkout currency must match the account's. Shopify [1]: Q7-SH-089. Q7-WC-036 Q7-WC-037 Q7-WC-038 Q7-WC-039 Q7-WC-040 Q7-WC-041 Q7-WC-042 Q7-WC-043 Q7-WC-044 Q7-WC-045 Q7-WC-046
- **differs** (term): PayPal Standard checks the store currency against a 27-currency list: "PayPal Standard does not support your store currency." Shopify [1]: Q7-SH-100. Q7-WC-058 Q7-WC-059
- **differs** (role): Card readers and Tap to Pay collect only in each country's default currency; core makes in-person payments eligible only for US stores in USD and Canadian stores in CAD. Shopify [1]: Q7-SH-072. Q7-WC-047 Q7-WC-060
- **differs** (role): Locale data moves Bulgaria from BGN to EUR on 2026-01-01. Shopify [1]: Q7-SH-115. Q7-WC-051
- **differs** (role): Payments > Transactions lists transactions regardless of currency, amounts in the payout currency. Zid [1]: Q7-ZD-023. Q7-WC-007
- **not in what was read:** a merchant-of-record service charging buyers abroad in their currency. Shopify [1]: Q7-SH-184. Q7-WC-N01
- **not in what was read:** cryptocurrency or stablecoin payment or settlement. Shopify [1]: Q7-SH-P0016. Q7-WC-N03
- **not in what was read:** fixed-amount discounts limited to the store currency. Shopify [1]: Q7-SH-111. Q7-WC-N09
- **not in what was read:** a product currency field; amounts in a currency's smallest unit. Zid [1]: Q7-ZD-014, Q7-ZD-024. Q7-WC-N07 Q7-WC-N08
- **not in what was read:** developer guidance on converting order totals; a cash on delivery limit in a currency. Zid [1]: Q7-ZD-K0304, Q7-ZD-K0120. Q7-WC-N10 Q7-WC-N11

### Paid out to the seller
- **differs** (term): WooPayments' **payout currency**, "the currency in which funds are paid out into your bank account", is also called the "settlement currency" and may differ from the customer currency. Payout pages show amounts in it. Shopify [1]: Q7-SH-002. Q7-WC-004 Q7-WC-005 Q7-WC-006 Q7-WC-009 Q7-WC-049
- **differs** (role): A payment matching no bank account's currency is converted to the default currency, paid into the default account, with a conversion fee; bank accounts in other currencies can take separate payouts. Shopify [1]: Q7-SH-013, Q7-SH-P0155; Zid [1]: Q7-ZD-004. Q7-WC-K0737 Q7-WC-K0738 Q7-WC-K0742 Q7-WC-K0743
- **differs** (role): Fees are charged in the customer currency when a bank account matches it, otherwise after conversion to the default currency; fees vary by country and currency paid. Shopify [1]: Q7-SH-K1950; Zid [1]: Q7-ZD-K0156. Q7-WC-032 Q7-WC-K0740 Q7-WC-K0427
- **differs** (role): A chart gives each country's payout currencies, from Australia (AUD) to the United States (USD); a single listed currency is paid only to banks in that country. Shopify [1]: Q7-SH-018; Zid [1]: Q7-ZD-K0039. Q7-WC-P0051 Q7-WC-K0739
- **differs** (role): Minimum payouts depend on the payout currency; instant payouts run from $50 to $1,000 USD. Zid [1]: Q7-ZD-K0025. Q7-WC-P0039 Q7-WC-P0048
- **not in what was read:** an API field for a payout bank account's currency. Shopify [1]: Q7-SH-134. Q7-WC-N05

## [2]
- **differs** (role): The seller sets the store currency under WooCommerce > Settings > General > Currency options: one only, from a drop-down defaulting to USD, or a custom currency. Shopify [2]: Q7-SH-003; Zid [2]: Q7-ZD-001 ("The store's currency"). Q7-WC-031 Q7-WC-K0749 Q7-WC-025
- **differs** (role): Onboarding sets `woocommerce_currency` from the given country's `currency_code` (SA: SAR). Zid [2]: Q7-ZD-001 ("The store's currency"); Shopify [2]: Q7-SH-079. Q7-WC-053 Q7-WC-054 Q7-WC-052
- **differs** (role): Multi-currency is enabled under Payments > Settings > Advanced settings; Enabled currencies starts with the store currency. It can switch customers to their local currency by geolocation; customers can choose one under My Account. Shopify [2]: Q7-SH-076, Q7-SH-083; Zid [2]: Q7-ZD-016; Zid [1]: Q7-ZD-K0299. Q7-WC-012 Q7-WC-013 Q7-WC-014 Q7-WC-015 Q7-WC-018
- **goes beyond:** a Price rounding setting rounds converted prices. Q7-WC-017
- **differs** (role): Payout currencies depend on the account's country; a multi-currency store "might also be able" to take payouts in several. Fees vary by the business's country. Shopify [2]: Q7-SH-011, Q7-SH-016, Q7-SH-060, Q7-SH-K1636, Q7-SH-K1946; Zid [2]: Q7-ZD-K0300. Q7-WC-K0739 Q7-WC-P0051 Q7-WC-K0743 Q7-WC-K0427
- **not in what was read:** business entities, each with its own account and payout currency. Shopify [2]: Q7-SH-K1268. Q7-WC-N04
- **not in what was read:** changing the store currency through payout bank settings. Shopify [2]: Q7-SH-180. Q7-WC-N12
- **not in what was read:** an API list of enabled currencies; stores' recorded multi-currency setting. Shopify [2]: Q7-SH-128, Q7-SH-186. Q7-WC-N06 Q7-WC-N13
- **not in what was read:** the currency of an order the seller creates. Shopify [2]: Q7-SH-103. Q7-WC-N14
- **not in what was read:** a currency turning on shipping; country groups below the store with their own currency and prices. Zid [2]: Q7-ZD-K0229, Q7-ZD-020; Zid [1]: Q7-ZD-018; Shopify [2]: Q7-SH-077, Q7-SH-006. Q7-WC-N15 Q7-WC-N16

## [3]
- **differs** (role): Changing the base currency changes what the store displays and charges in, and converts nothing: product prices keep their numbers; earlier orders keep their currency and totals. It needs access to WooCommerce settings and a gateway supporting the currency. Shopify [3]: Q7-SH-008, Q7-SH-006, Q7-SH-007; Zid [3]: Q7-ZD-K0302. Q7-WC-K0748 Q7-WC-026 Q7-WC-027 Q7-WC-023
- **differs** (role): An upgrade routine changed `woocommerce_currency` and orders' `_order_currency` from KIP to LAK. Shopify [3]: Q7-SH-106. Q7-WC-057
- **differs** (role): Exchange rates come from the WooPayments server, or a manual rate; switching the store currency and back forces fresh rates. Shopify [3]: Q7-SH-078. Q7-WC-K0755 Q7-WC-K0753 Q7-WC-016
- **differs** (role): A refund repays the exact amount in the currency paid; the balance is debited at the refund-time rate. Shopify [3]: Q7-SH-068. Q7-WC-019 Q7-WC-020
- **differs** (role): A dispute fee is in the customer currency when a bank account matches it, otherwise in the default payout currency. Shopify [3]: Q7-SH-066. Q7-WC-033 Q7-WC-034
- **differs** (role): A transaction's timeline shows the exchange rate and conversion fee, a separate line since June 7, 2021. Shopify [3]: Q7-SH-014. Q7-WC-008 Q7-WC-035
- **differs** (role): With several bank accounts, one must be the default. Shopify [3]: Q7-SH-015. Q7-WC-K0741
- **not in what was read:** editing orders placed in another currency; changing the account's country; notice of fee changes. Shopify [3]: Q7-SH-073; Zid [3]: Q7-ZD-K0230, Q7-ZD-K0157. Q7-WC-N17 Q7-WC-N18 Q7-WC-N19
- **not in what was read:** copying or converting prices for a new country group. Zid [3]: Q7-ZD-022. Q7-WC-N16

## [4]
- **differs** (role): With bank accounts in several currencies, the balance can be viewed in each. Payments enter the account balance, pending then available, before payout; HUF fillérs stay in it. Shopify [4]: Q7-SH-131; Zid [4]: Q7-ZD-K0033. Q7-WC-048 Q7-WC-P0025 Q7-WC-P0032 Q7-WC-P0035 Q7-WC-P0041
- **differs** (role): Under Stripe's terms, settlement funds sit in Pooled Accounts and are transferred net of fees; Stripe may withhold balance as a reserve. Shopify [4]: Q7-SH-P0010; Zid [4]: Q7-ZD-K0023. Q7-WC-P0121 Q7-WC-P0124 Q7-WC-P0059
- **differs** (role): Payout maxima are in USD: $9,999 to a US debit card, $1,000 for an instant payout. Zid [4]: Q7-ZD-K0133. Q7-WC-P0040 Q7-WC-P0048
- **differs** (role): For Cash on Delivery the store owner confirms payment was collected. Zid [4]: Q7-ZD-K0117. Q7-WC-050
- **not in what was read:** a platform wallet for the seller's money and its currency; a third party holding money for international orders. Zid [4]: Q7-ZD-K0136; Shopify [4]: Q7-SH-K1600. Q7-WC-N02 Q7-WC-N01
