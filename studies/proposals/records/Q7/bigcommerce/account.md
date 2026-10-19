# Q7, BigCommerce: sorted against Shopify and Zid

## [1]

- **differs** (definition): **Default currency**: "Merchants use this currency when any auto-conversion of pricing (product, tax, shipping, promotions) occurs". It is assigned at store creation and is always transactional. Sorted against Shopify [1]: Q7-SH-K1934; Zid [1]: Q7-ZD-002. Q7-BC-001 Q7-BC-013
- **differs** (role): Analytics show in the default currency, as approximate values. Store credit works only in the default currency, and a gift certificate is redeemed only in the currency selected. Sorted against Shopify [1]: Q7-SH-074. Q7-BC-027 Q7-BC-007 Q7-BC-026
- **differs** (definition): A **display currency** (the "Active Currency", or "presentment currency") shows prices while the order is transacted in the default currency, and checkout notes the actual amount. A **transactional currency** is shown, charged, and passed to the payment provider. Sorted against Shopify [1]: Q7-SH-K1941; Zid [1]: Q7-ZD-K0300 ("With مدفوعات زد active"), Q7-ZD-004. Q7-BC-002 Q7-BC-003 Q7-BC-004 Q7-BC-K0395 Q7-BC-K0401
- **differs** (role): A currency is transactional only once a gateway that supports it is enabled. Display currencies use the default currency's payment methods. The developer docs list "Stripe Payment Gateway" as supported and "Other Payment Gateways" as not. The Help Center's gateway tables tick Multicurrency for Adyen, BigCommerce Payments, PayPal and others. All offline methods support additional transactional currencies. Sorted against Shopify [1]: Q7-SH-K1937, Q7-SH-100; Zid [1]: Q7-ZD-K0300 ("With مدفوعات زد, the final payment"). Q7-BC-005 Q7-BC-006 Q7-BC-008 Q7-BC-009 Q7-BC-010 Q7-BC-011 Q7-BC-012 Q7-BC-014 Q7-BC-015 Q7-BC-K0397
- **differs** (role): BigCommerce Payments lists 24 supported currencies, from AUD to SEK. Sorted against Shopify [1]: Q7-SH-135. Q7-BC-016
- **differs** (role): Local Payment Methods let eligible shoppers pay in their local currency. Their availability, and that of digital wallets, depends on the store's country and currency combination. Sorted against Shopify [1]: Q7-SH-089. Q7-BC-017 Q7-BC-018 Q7-BC-019
- **goes beyond**: Stripe Adaptive Pricing lets shoppers pay in their presentment currency while the store settles in its default currency. It works only on the Stripe OCS Checkout Session method and is on by default for most stores. Q7-BC-K0402 Q7-BC-K0404 Q7-BC-P0035 Q7-BC-P0051 Q7-BC-P0102
- **differs** (role): A currency converter shows on the storefront, and a visitor whose IP address matches a supported country sees that currency automatically. Sorted against Zid [1]: Q7-ZD-K0300 ("With مدفوعات زد active"), Q7-ZD-K0299. Q7-BC-028
- **differs** (identifier): Orders V2 records `currency_code` (display), `default_currency_code` (transactional) and `currency_exchange_rate`. Under Multi-Currency it adds `store_default_currency_code` and `store_default_to_transactional_exchange_rate`. View Orders shows the transacted currency. Sorted against Shopify [1]: Q7-SH-124, Q7-SH-K2893; Shopify [3]: Q7-SH-014; Zid [1]: Q7-ZD-008, Q7-ZD-023. Q7-BC-020 Q7-BC-021 Q7-BC-022 Q7-BC-023 Q7-BC-P0028
- **differs** (role): The Currencies API manages "alternate currency display options". Transactional currencies can't be created through it, and a webhook fires when a channel's currency is updated. Sorted against Zid [1]: Q7-ZD-005; Shopify [2]: Q7-SH-128. Q7-BC-K0391 Q7-BC-K0394 Q7-BC-K0400
- **goes beyond**: Fixed and flat-rate shipping costs are set in the default currency and converted. Real-time carrier quotes come back in the transactional currency where the carrier supports it. Q7-BC-024 Q7-BC-025
- **differs** (role): Cryptocurrency payments "are enabled for all merchants", and BitPay settles to the merchant's bank account. Sorted against Shopify [1]: Q7-SH-P0016. Q7-BC-P0034 Q7-BC-P0022
- **differs** (definition): **Settlement Currency**: "The currency the merchant gets paid out to their bank account". The merchant sets it through the payment provider; for Stripe, by reaching out to Stripe. Sorted against Shopify [1]: Q7-SH-002; Shopify [2]: Q7-SH-011. Q7-BC-P0014 Q7-BC-P0016 Q7-BC-P0017
- **differs** (role): The merchant pays a conversion fee when the shopper's currency differs from the settlement currency, and the shopper pays one when the active and transactional currencies differ. In both cases the rate is outside BigCommerce's scope. Cross-border fees may change the settlement amount. Under Adaptive Pricing the merchant pays 0% on conversion. Sorted against Shopify [1]: Q7-SH-013; Shopify [2]: Q7-SH-K1946. Q7-BC-P0015 Q7-BC-K0398 Q7-BC-P0018 Q7-BC-P0050 Q7-BC-P0051 Q7-BC-P0101
- **differs** (role): Stripe OCS allows a different Stripe account for each currency configured. In BigCommerce Payments, the primary currency shows its linked bank account and automatic payouts. Sorted against Shopify [1]: Q7-SH-P0155; Shopify [2]: Q7-SH-K1268. Q7-BC-P0104 Q7-BC-059
- **differs** (role): The Fast payout fee is 1.50% (minimum $0.50). Sorted against Zid [1]: Q7-ZD-K0025. Q7-BC-P0077
- **differs** (role): "Fees are payable in U.S. Dollars, unless otherwise specified." Sorted against Zid [1]: Q7-ZD-K0156. Q7-BC-K0177
- **not in what was read**: Shopify [1]: Q7-SH-072. Q7-BC-N18
- **not in what was read**: Shopify [1]: Q7-SH-184. Q7-BC-N01
- **not in what was read**: Shopify [1]: Q7-SH-115. Q7-BC-N19
- **not in what was read**: Shopify [1]: Q7-SH-018. Q7-BC-N02
- **not in what was read**: Shopify [1]: Q7-SH-134. Q7-BC-N03
- **not in what was read**: Zid [1]: Q7-ZD-K0304. Q7-BC-N20
- **not in what was read**: Zid [1]: Q7-ZD-024. Q7-BC-N05
- **not in what was read**: Zid [1]: Q7-ZD-K0120. Q7-BC-N06
- **not in what was read**: Zid [1]: Q7-ZD-K0039. Q7-BC-N04

## [2]

- **differs** (role): A new store's default currency "is assigned based on your location". The seller enables more currencies, sets each as transactional or display-only, and sets "Default to [Currency Code] in these countries". Sorted against Shopify [2]: Q7-SH-003, Q7-SH-079; Zid [2]: Q7-ZD-001. Q7-BC-029 Q7-BC-030 Q7-BC-031
- **differs** (role): In a multi-storefront store, each storefront can have its own default currency (Set as Channel default currency) and its own transactional currencies. Shoppers can switch to any currency enabled at store level. Storefronts are added by plan. Sorted against Shopify [2]: Q7-SH-076; Zid [2]: Q7-ZD-020. Q7-BC-037 Q7-BC-038 Q7-BC-039 Q7-BC-040 Q7-BC-K0217
- **goes beyond**: Payment methods are set up under Settings › Payments for a currency chosen from the drop-down list. Q7-BC-041 Q7-BC-042
- **differs** (role): Display-only currencies can use a static or dynamic exchange rate, and transactional currencies use static ones. A dynamic rate updates every 4 hours, from BigCommerce Currency Service or through the API. Sorted against Shopify [3]: Q7-SH-078. Q7-BC-032 Q7-BC-033 Q7-BC-034 Q7-BC-035
- **differs** (role): Multi-Currency Pricing is set through price lists, which are limited to Performance plans. Fixed prices apply only to transactional currencies, with a price record for each currency. A display currency converts the default currency's price. A channel-specific price list sets prices in one currency for each storefront. Sorted against Shopify [2]: Q7-SH-K2660; Zid [1]: Q7-ZD-018; Zid [3]: Q7-ZD-022. Q7-BC-043 Q7-BC-044 Q7-BC-045 Q7-BC-046 Q7-BC-047 Q7-BC-K0037
- **differs** (role): The plan comparison's Multi-currency row reads "Accept payments in over 100+ currencies". Sorted against Zid [2]: Q7-ZD-016. Q7-BC-K0393
- **differs** (role): A manual order needs the default currency assigned to channel ID 1, and the seller picks the transaction's currency. Sorted against Shopify [2]: Q7-SH-103. Q7-BC-048 Q7-BC-049
- **differs** (role): BigCommerce Payments supports UK- and US-based stores, and offers UK and EMEA customers multi-currency balances. Sorted against Zid [2]: Q7-ZD-K0300. Q7-BC-P0087 Q7-BC-P0057
- **not in what was read**: Shopify [2]: Q7-SH-180. Q7-BC-N07
- **not in what was read**: Shopify [2]: Q7-SH-006. Q7-BC-N08
- **not in what was read**: Shopify [2]: Q7-SH-016. Q7-BC-N09
- **not in what was read**: Shopify [2]: Q7-SH-K1636. Q7-BC-N10
- **not in what was read**: Shopify [2]: Q7-SH-060. Q7-BC-N11

## [3]

- **differs** (role): The default currency is changed with Action › Set as default under Settings › Currencies. This needs the Manage Settings permission, which the Store Administrator and Store Owner roles have by default. Existing currencies can be edited at any time. Sorted against Shopify [3]: Q7-SH-008; Zid [3]: Q7-ZD-001. Q7-BC-050 Q7-BC-036 Q7-BC-051
- **differs** (role): The developer docs say "Do not change the default currency": changing it doesn't recalculate catalog prices, and it makes the new currency transactional. Sorted against Shopify [3]: Q7-SH-006; Zid [3]: Q7-ZD-K0302. Q7-BC-052 Q7-BC-053 Q7-BC-054
- **differs** (role): Refunds are made in the transactional currency, or in the default currency for display-only orders. Store credit isn't offered on non-default-currency orders. Under Adaptive Pricing, Stripe absorbs rate shifts on refunds. Sorted against Shopify [3]: Q7-SH-068. Q7-BC-055 Q7-BC-056 Q7-BC-057 Q7-BC-P0049
- **differs** (role): BigCommerce Payments refunds come from its balance. Sorted against Shopify [3]: Q7-SH-066. Q7-BC-P0076
- **differs** (role): In BigCommerce Payments, the merchant can add currencies, mark one as primary, close one, and convert balances between currencies. Sorted against Shopify [3]: Q7-SH-015. Q7-BC-060 Q7-BC-061 Q7-BC-P0073
- **not in what was read**: Shopify [3]: Q7-SH-059. Q7-BC-N12
- **not in what was read**: Shopify [3]: Q7-SH-114. Q7-BC-N13
- **not in what was read**: Zid [3]: Q7-ZD-K0230. Q7-BC-N14

## [4]

- **differs** (role): BigCommerce Payments shows a balance for each currency, and money is added to the primary currency's balance. UK and EMEA customers get "multi-currency balances in GBP, EUR, and more". Sorted against Shopify [4]: Q7-SH-131; Zid [4]: Q7-ZD-K0136. Q7-BC-058 Q7-BC-062 Q7-BC-P0057 Q7-BC-P0053
- **differs** (role): A PayPal platform account dedicated to the store "will handle all settlement", and a new account's initial payments are held for up to 21 days. Sorted against Shopify [4]: Q7-SH-P0010; Zid [4]: Q7-ZD-K0033. Q7-BC-P0070 Q7-BC-P0083
- **not in what was read**: Shopify [4]: Q7-SH-K1600. Q7-BC-N15
- **not in what was read**: Zid [4]: Q7-ZD-K0133. Q7-BC-N16
- **not in what was read**: Zid [4]: Q7-ZD-K0117. Q7-BC-N17
