# Q7 on Shopify: what Shopify's material shows

## [1]

### Store currency
- Shopify names a **store currency**: the currency of the Shopify admin, the one products are priced in and reports run in, and the one displayed to customers on the online store. Shopify calls it the primary currency customers use when purchasing. Q7-SH-K1934 Q7-SH-K1935 Q7-SH-K2916 Q7-SH-001 Q7-SH-003
- Reports can be viewed only in the store currency. Fixed price discounts exist only in the store default currency. Q7-SH-074 Q7-SH-111
- In the Admin GraphQL API (2026-10), the shop's currency is `Shop.currencyCode`. Amounts are carried as a `MoneyBag`, whose `shopMoney` is the amount in the shop's base currency and whose `presentmentMoney` is the amount in the customer's selected currency. Q7-SH-K2893 Q7-SH-122 Q7-SH-123
- In the stores the runs observed, the store currency was the Yemeni Rial. The General settings page's **Store defaults** showed, under **Currency display**, "Yemeni Rial (YER)" on store fake-demo-sharrwah (store address Sanaa, Yemen, observed 5 October 2026). The admin's answer to `MarketsHomeCurrencyOptions` gave `shop.currencyCode` "YER" on store capture-plus (observed 2 October 2026). Q7-SH-191 Q7-SH-192
- On the page that creates a gift card product, the **Currency** menu offered "Store currency (YER) Yemeni Rial" and, under "Market currencies", nine currencies from Czech Koruna to Yemeni Rial, each marked "Not eligible" and disabled (store demo-fake-dev-store, observed 30 September 2026). On store ts15uk-ug the same page said that gift cards are issued in the store currency and can be redeemed in any currency, with exchange rates determined at checkout using the Market settings (observed 7 October 2026). Q7-SH-196 Q7-SH-197

### Currency shown to buyers and paid by them
- A market's currency is the one displayed to customers on the online store, and transactions are performed in it. Each market can have a currency customization, and prices are displayed in the currency set for the customer's market. Q7-SH-K1941 Q7-SH-K1931 Q7-SH-076
- Shopify publishes a list of currencies that can be accepted and refunded through Shopify Payments, with an asterisk on the currencies not available to merchants in France. Q7-SH-135 Q7-SH-136 Q7-SH-179
- Only stores whose primary gateway is Shopify Payments or Adyen can process payments in a customer's local currency. With any other provider, the price is converted to the store's default currency at checkout and customers in all markets pay in that currency. Q7-SH-K1937 Q7-SH-K1938 Q7-SH-075 Q7-SH-070
- Within Shopify Payments, Shopify lists each payment method's support for local pricing: credit card checkout, Shop Pay, Klarna, iDEAL | Wero, EPS Payments and Bancontact "Fully supported"; Apple Pay, Google Pay and PayPal Express "Supported but without checkout restrictions"; Amazon Pay and "Others" "Unsupported and prices convert to shop currency". Q7-SH-089 Q7-SH-099
- With Adyen, transactions are processed in the currency Shopify sends to Adyen. PayPal accepts payments in various currencies when the store sells in multiple currencies through Shopify Payments. Q7-SH-100 Q7-SH-087
- Shopify POS sells in a location's local currency only when the store has a business entity with Shopify Payments set up for that country. Q7-SH-072
- Under Managed Markets, customers pay in their own currency, and Shopify Payments is used for all Managed Markets transactions and payouts. Q7-SH-184 Q7-SH-182
- An order records both `Order.currencyCode` and `Order.presentmentCurrencyCode`. In the admin, the order's **Paid** section shows the amount in the customer's currency (the presentment currency). An order whose payment was converted back to the store currency at checkout doesn't display as a multi-currency order. Q7-SH-124 Q7-SH-125 Q7-SH-105
- Under the Shopify Payments terms, cryptocurrency wallets can be a Payment Method, and settlement funds include cryptocurrency. Under the Cryptocurrency Credit Reward Program, some Credits may be paid in stablecoins such as USD Coin. Q7-SH-P0016 Q7-SH-P0014 Q7-SH-K1757
- Between August 8, 2025 and December 31, 2026, businesses selling in Bulgaria in Euros must display prices in both Euros and Bulgarian Lev. Transactions still take place in one currency. Q7-SH-115 Q7-SH-116
- In a run on store demo-fake-dev-store (30 September 2026), the European Union market's **Use local currencies** setting said "Let customers pay in their region’s currency", and that product pricing will include, when applicable, a 2% conversion rate fee paid by customers, with exchange rates determined at the time of purchases and refunds. On store capture-plus, the admin's `MarketsHomeCurrencyOptions` answer gave `foreignExchangeFee` "0.02" (2 October 2026). Q7-SH-198 Q7-SH-199 Q7-SH-193
- In the order journey on store demo-fake-dev-store (30 September 2026), a return's `maximumRefundable` carried both `presentmentMoney` and `shopMoney`, each in `currencyCode` "YER". Q7-SH-200

### Currency paid out to the seller
- Shopify names a **payout currency**: the currency that Shopify Payments deposits into the seller's bank account in. The customer's payment currency, and the store currency, can differ from it. Q7-SH-002 Q7-SH-004 Q7-SH-010
- When a customer pays in a currency other than the payout currency, an exchange rate and a conversion fee are applied at payment capture. Shopify charges the fee in the payout currency. Q7-SH-013 Q7-SH-K1950 Q7-SH-K1953 Q7-SH-084
- With Multi-Currency Payouts, orders paid in a currency that has its own payout account are paid out to that account. Orders in any other currency are converted to the default account's currency. On plans without Multi-Currency Payouts, all payouts are converted to the domestic currency. Q7-SH-P0155 Q7-SH-062 Q7-SH-065 Q7-SH-057
- Shopify publishes, per store location, the domestic payout currency and the additional payout currencies available, in a 39-row table running from Australia to the United States. A separate table gives each country's settlement currency. Q7-SH-018 Q7-SH-056 Q7-SH-P0068 Q7-SH-P0156
- In the API, a payout bank account carries `ShopifyPaymentsBankAccount.currency`, and the Shopify Payments account carries `defaultCurrency`. Q7-SH-134 Q7-SH-133

## [2]

### Store currency
- The seller can select the store currency from the options in store settings. Shopify does not name the full list of those options in what was read. Q7-SH-003 Q7-SH-N03
- If Shopify Payments is the credit card gateway, the currency must be changed by editing the bank account and currency settings used by Shopify Payments. Q7-SH-180
- Managed Markets requires the store currency to stay set to the currency required for the region. Q7-SH-006

### Market currency
- The currency is set per market, as a currency customization under **Markets**. Submarkets inherit their parent market's currency unless they have their own customization. Q7-SH-076 Q7-SH-077 Q7-SH-K1225
- A single-country market starts with that country's currency. A multi-country market starts with the store's base currency and has **Local currencies** activated. Turning **Local currencies** off shows the market's base currency to everyone in that market. Q7-SH-079 Q7-SH-080 Q7-SH-081
- If a country's local currency isn't supported by Shopify Payments, the market's base currency is shown there instead. The currencies available depend on the store's location and payment processor. Q7-SH-083
- In the API, a market's currency settings are `MarketCurrencySettings.baseCurrency` and `localCurrencies`, and the shop lists `enabledPresentmentCurrencies`. Q7-SH-128 Q7-SH-129 Q7-SH-126 Q7-SH-127
- Showing prices in local currencies requires Shopify Payments. Shopify's plan comparison marks it "Included" on all four plans. Setting product prices and percentage adjustments per market doesn't require Shopify Payments. A price list carries its own `PriceList.currency`. Q7-SH-K2660 Q7-SH-K2790 Q7-SH-071 Q7-SH-130
- In the stored admin answers, the store feature `multiCurrencyGatewayEnabled` reads `false` on stores ibx5bt-xy, capture-plus and capture-grow in their first set, and `true` on capture-plus and capture-grow from their second set. Q7-SH-186 Q7-SH-187 Q7-SH-188 Q7-SH-189 Q7-SH-190
- On store capture-plus (2 October 2026), the admin's `ShopifyPaymentsData` answer gave Shopify Payments `"eligible":false`. Its `MarketsHomeCurrencyOptions` answer listed 130 currencies; the YER item had `automaticRate` null. Q7-SH-195 Q7-SH-194
- A draft order with no customer uses the store's default currency. Otherwise the customer's shipping address decides the market, and its currency. Q7-SH-103 Q7-SH-102

### Payout currency
- The domestic currency is set by the store location (the Shopify Payments region) and is the default payout currency. Non-domestic payout currencies depend on the Shopify plan and on the location entered in General settings. Q7-SH-011 Q7-SH-012 Q7-SH-017
- A US-based store's default payout currency is always USD and can't be changed. On the Basic or Grow plan, a store based in Canada can choose USD instead of CAD as its default payout currency. Q7-SH-016 Q7-SH-058
- Multi-Currency Payouts is not available on the Basic, Grow or Shopify plan. It also requires a business entity and a bank account in an eligible region. Q7-SH-K1636 Q7-SH-059
- Each business entity has its own Shopify Payments account, payout currency and bank account. Markets decide which entity processes a region's transactions, and an order goes through the primary Shopify Payments account unless its market is assigned another entity. Business entities are on the Plus plan only. Q7-SH-K1268 Q7-SH-K1266 Q7-SH-117 Q7-SH-118
- In Singapore, Hong Kong and the United Arab Emirates, non-domestic payout accounts must still be based in the domestic region. Q7-SH-060
- The conversion fee depends on the store's primary country, or, for a multi-entity store, on the entity that processes the payment. Q7-SH-K1946 Q7-SH-082

## [3]

### Changing the store currency
- Only the store owner can change the store currency, under **Settings > General > Store defaults**. A change after the first order requires checking **I understand the risk of changing the store currency**. A copied statement from the account-setup page says to contact Shopify Support for a change after the first sale. Q7-SH-008 Q7-SH-181 Q7-SH-K1936
- Shopify lists the effects of a change. Product prices and discount rates take the new currency but keep the same amount. Shipping rates aren't updated, and gift cards in the old currency stop working. Reports, pending payments and later refunds may be affected. With a provider other than Shopify Payments, every market moves to the new currency. Managed Markets is deactivated. Q7-SH-006 Q7-SH-009
- After the change, the admin doesn't show product or discount prices in the earlier currency. Q7-SH-007

### Changing market currencies, rates and drafts
- Under each market's currency settings, the seller chooses **Dynamic** or **Manual** exchange rates. A single-country market's currency can be changed to any supported currency. Q7-SH-078 Q7-SH-079 Q7-SH-K1942
- A draft order keeps the exchange rate from its creation, unless it is edited later, which reprices the whole order. The seller can override the currency on a draft order. Q7-SH-101 Q7-SH-102
- Editing orders placed in international currencies is available only to some stores. Q7-SH-073
- Shopify does not say, in what was read, what changing a market's currency does to orders already placed. For a market's business entity, a change affects only new orders. Q7-SH-N02 Q7-SH-119

### Refunds and chargebacks after the fact
- Refunds go out in the currency the customer paid in. Any conversion uses the current rate, also when a manual rate is set, and conversion fees aren't charged on refunds. Under Managed Markets, refunds within 30 days use the rate given at purchase, and each order's exchange rate is guaranteed for 30 days. Q7-SH-068 Q7-SH-069 Q7-SH-085 Q7-SH-013 Q7-SH-185 Q7-SH-183
- Under Multi-Currency Payouts, refunds and chargebacks come out of the bank account in the order's currency, or out of the default account if no such account exists. Chargebacks are converted at the rate on the chargeback date. Q7-SH-066 Q7-SH-067 Q7-SH-086
- Historical exchange rates for each order can be viewed in its timeline. Q7-SH-014

### Payout accounts
- A payout currency is added by adding a bank account in that currency under **Settings > Payments > Shopify Payments > Payout accounts**. A replacement account must keep the same country and currency. When a currency's account is deleted, that currency's payouts go to the default account. Q7-SH-015 Q7-SH-061 Q7-SH-063 Q7-SH-064
- Activating Multi-Currency Payouts requires the store owner. Q7-SH-059

### A change Shopify made: Bulgaria
- After Bulgaria moved to the Euro, Shopify switched markets that charged in Bulgarian Lev to Euros on stores using Shopify Payments. Store default currencies and product prices were left unchanged. Q7-SH-106 Q7-SH-107 Q7-SH-108
- Stores not using Shopify Payments must change their default currency and pricing themselves, and can't switch back afterwards. Catalogs in Bulgarian Lev stay valid, but once updated they can't be switched back. Q7-SH-109 Q7-SH-112 Q7-SH-113
- Gift cards and discounts in Lev are converted when redeemed. Q7-SH-110
- Shopify deactivated BGN payout accounts where a EUR account existed, and converted lone BGN accounts to EUR. Q7-SH-114

## [4]
- Shopify Payments' account in the API tracks current balances across all supported currencies (`ShopifyPaymentsAccount.balance` is a list of amounts). Payout and transaction details can be separated and filtered by currency. Q7-SH-131 Q7-SH-132 Q7-SH-120 Q7-SH-121
- The Shopify Payments terms place settlement with a Payment Processor, into a Payment Processor Account, and then the Payout Account. The terms read do not name the currency of funds held there or of Reserved funds. Q7-SH-P0010 Q7-SH-P0024 Q7-SH-N01
- For international Managed Markets orders, Shopify Payments holds the money in a Global-e account. What was read does not name the currency held there. Q7-SH-K1600 Q7-SH-P0100 Q7-SH-N04
