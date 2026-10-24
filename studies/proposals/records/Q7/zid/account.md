# Q7, Zid: what Zid shows

## [1]

### Prices and the store's currency

- In the help, the seller chooses and activates the store's العملة الأساسية "بناء على عملة دولتك" under لوحة التحكم > الاعدادات > اللغات والعملات, and can activate other currencies and pick any of them with اختيار كعملة أساسية. Q7-ZD-001, Q7-ZD-K0298
- The help defines العملة الأساسية as the currency in which product prices were entered. Q7-ZD-002
- The Merchant API returns the store's `currency` ("Current currency configured for the store.") and `currencies` ("List of currencies supported by the store."), from GET /v1/managers/account/store/localization. Each product carries a `currency`, "Currency code of the product price (ISO 4217)." Q7-ZD-005, Q7-ZD-006, Q7-ZD-014, Q7-ZD-K0305

### Prices shown to buyers

- With مدفوعات زد active and other currencies activated, the help says buyers see product prices in the currency they choose, such as الريال العماني. Q7-ZD-K0300
- On the compare-plans page, Geo-Based Currency Settings is described as "Automatically adjust currencies based on customer location". Q7-ZD-K0299
- Under الأسواق, a price can be set for each market and channel "وبعملة السوق نفسها، دون الاعتماد على سعر عالمي واحد أو التحويل التلقائي للعملات". عملة السوق is described as the currency used to show product prices in that market. Q7-ZD-018, Q7-ZD-019, Q7-ZD-K0236

### Buyers' payments

- With مدفوعات زد, the final payment is made in the store's العملة الأساسية (الريال السعودي \ الدينار الكويتي) on every network except كي نت, which is paid in الدينار الكويتي. The amount paid is subject to the active payment gateway's exchange rate. Q7-ZD-K0300, Q7-ZD-K0301
- The help also says خاصية العملات lets a seller receive payments in different currencies in زد باي, once the currencies feature is activated in the store settings. Q7-ZD-004
- Each order records an `order_currency`, "the currency in which the order was placed and paid". It also records an `order_store_currency`, "the store’s base currency", with exchange rates, and `has_different_transaction_currency`. The View Order example shows an order total in ج.م (EGP) and a `transaction_amount_string` of 504.00 SAR. Q7-ZD-008, Q7-ZD-009, Q7-ZD-010, Q7-ZD-011, Q7-ZD-012, Q7-ZD-013, Q7-ZD-K0303
- Partners are told to convert the order total when the store currency, the order currency and the currency of the shipping address (for cash on delivery) differ. Q7-ZD-K0304
- The زد باي transactions table shows the column "العملة : عملة العميل". Q7-ZD-023
- In the Zid Payments Open APIs, Zid sends providers an amount "in the smallest currency unit", with SAR given in Halala, and a `currency` in ISO 4217. The Apple Pay session uses "currencyCode: {Merchant Currency based on country}". Q7-ZD-024, Q7-ZD-025, Q7-ZD-015
- The cash on delivery limit is given as "Up to $1000 (3750 SAR)". Q7-ZD-K0120, Q7-ZD-P0126
- The held material does not show the currency of payments through بوابات الدفع الأُخرى. Q7-ZD-N04

### Payouts to the seller

- Zid Pay deposit minimums and fees are stated as ١٠٠ ريال and ٣ ريال (Saudi Arabia), and ١ دينار كويتي (Kuwait). The held pages read do not name the currency of the deposit itself. Q7-ZD-K0025, Q7-ZD-K0026, Q7-ZD-K0029, Q7-ZD-P0041, Q7-ZD-N02
- The bank list holds Saudi banks and some Gulf banks. Q7-ZD-K0039, Q7-ZD-K0038
- Zid's fees are in الريال السعودي or the merchant's local currency, and all payments are in the local currency. Q7-ZD-K0156

## [2]

- The store's currency is set at the store level, in the store settings, by the seller choosing العملة الأساسية "بناء على عملة دولتك". In the API, each currency is tied to a country ("Country associated with the selected currency."). Q7-ZD-001, Q7-ZD-007
- Activating a country's currency activates shipping to that country. Q7-ZD-K0229
- مدفوعات زد is available to merchants in Saudi Arabia and Kuwait, and its payment currency is the store's العملة الأساسية, except on كي نت. Q7-ZD-K0300, Q7-ZD-A0002
- Markets are a level below the store. Each market has its countries and an عملة السوق. The default market is the local market. The number of markets depends on the plan. Q7-ZD-020, Q7-ZD-021, Q7-ZD-K0235
- The payments page says multiple currencies are offered "by activating the feature in your store settings. Your plan, your choices." (Arabic: "حسب باقتك"). Geo-Based Currency Settings is listed by plan on the compare-plans page. Q7-ZD-016, Q7-ZD-017, Q7-ZD-K0299
- The held material does not show which currencies a seller can choose, or whether the store's country or plan limits that choice. Q7-ZD-N05

## [3]

- The seller can change the العملة الأساسية in the store settings. Q7-ZD-001
- The help says that when the currency is changed, product prices are converted at the exchange rate at the time of the change, and sales are converted to the new currency at that moment's rate, so total sales may change. It asks the seller to edit all product prices for the new العملة الأساسية. Q7-ZD-K0302, Q7-ZD-003, Q7-ZD-002
- When a market is created, its prices can be copied as they are with the new market currency, converted at the current exchange rate, or entered by hand. Q7-ZD-022
- For Gulf merchants, moving the store to another country first needs the wallet balance brought to zero. Q7-ZD-K0230, Q7-ZD-P0152
- Zid may change subscription plans and fee prices with at least seven days' notice. Q7-ZD-K0157
- The held material does not show what happens to orders already recorded when the العملة الأساسية changes. Q7-ZD-N03

## [4]

- محفظة زد is in الريال السعودي for merchants outside Saudi Arabia, except merchants in the GCC, who can use it in their local currency. Balances in الريال العماني، الدرهم الإماراتي، الدينار الكويتي and الدينار البحريني cannot be withdrawn. Q7-ZD-K0136, Q7-ZD-K0137, Q7-ZD-P0122, Q7-ZD-P0123
- The wallet's withdrawal limit is twenty thousand riyals per withdrawal, and card top-ups are capped at five thousand riyals. Q7-ZD-K0133, Q7-ZD-K0134, Q7-ZD-P0151
- Zid collects cash on delivery amounts for زد شب and transfers them to the merchant's wallet. Q7-ZD-K0117, Q7-ZD-K0122, Q7-ZD-P0070
- Zid Pay keeps a merchant balance before deposit (رصيد التاجر; قيد المعالجة; لم يتم الإيداع), and may hold a مبلغ احتياطي. The pages read do not name the currency of that balance. Q7-ZD-K0033, Q7-ZD-K0023, Q7-ZD-P0035, Q7-ZD-P0021, Q7-ZD-N01
- Which entity holds Zid Pay, wallet and cash on delivery funds is not on the pages read. Q7-ZD-G0004, Q7-ZD-G0027, Q7-ZD-G0023
