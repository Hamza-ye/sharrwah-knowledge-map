# Cards: Q7 on shopify

30 records cited by `studies/proposals/drafts/Q7/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Prices held: Shopify, Zid, WooCommerce and BigCommerce hold a seller's own prices in one currency per store, and match on role (basis 4). Shopify's store currency is the one "for pricing products and running reports"; Zid's العملة الأساسية is "العملة التي تم إدخال أسعار المنتجات باستخدامها"; WooCommerce allows "one base currency per store", and "WooCommerce uses it to display product prices and record new orders"; BigCommerce's default currency is "assigned during store creation, is always a transactional currency". Salla's seller sets the store's current currency, but the words read don't say prices are entered in it, so Salla's match is partial. Q7-SH-K1935 Q7-ZD-002 Q7-WC-K0745 Q7-WC-K0747 Q7-BC-013 Q7-SA-001
- **section 1, line 9:** - Amounts: Zid passes an amount to payment providers "in the smallest currency unit"; Shopify's MoneyBag carries `shopMoney` and `presentmentMoney` side by side; WooCommerce's shipped code records an order's currency "in ISO format". Not checked on Salla, for Zid's amount unit (Q7-ZD-024). Q7-ZD-024 Q7-SH-123 Q7-WC-055
- **section 1, line 10:** - Shown to buyers: Shopify and Zid set the shown currency per market, and match on role (basis 4). Shopify's currency customization "determines what currency is displayed to customers in that market"; Zid's عملة السوق is the currency "لعرض أسعار المنتجات داخل هذا السوق". WooCommerce keeps one list for the whole store, its "Enabled currencies". Q7-SH-076 Q7-ZD-K0236 Q7-WC-013
- **section 1, line 12:** - Paid by buyers: on Shopify, BigCommerce, WooCommerce and Salla the currency shown and the currency charged can differ, and what the payment provider supports decides the charge; they match on role (basis 4). Zid's pages aren't reconciled (below): Q7-SH-K1938 Q7-BC-014 Q7-WC-029 Q7-SA-K1963
- **section 1, line 13:** - Shopify: only stores with Shopify Payments or Adyen "as the primary gateway can process payments in a customer's local currency"; otherwise "the price will be converted to your store's default currency, and your customer will be charged in that currency". Q7-SH-K1937 Q7-SH-K1938
- **section 1, line 18:** - Each order records its currency, and four record the store's currency or a rate beside it, matching on role (basis 4): Shopify's order has `presentmentCurrencyCode`, and its MoneyBag holds both amounts; Zid's order gives the "Exchange rate of the store currency relative to the order currency"; BigCommerce's has `currency_code`, `default_currency_code` and `currency_exchange_rate`; Salla's an `exchange_rate` with `base_currency`, `exchange_currency` and `rate`; WooCommerce's a single "Currency the order was created with, in ISO format." (shipped code; the others stated). Q7-SH-124 Q7-SH-123 Q7-ZD-010 Q7-BC-020 Q7-SA-016 Q7-WC-055
- **section 1, line 19:** - Paid out: Shopify and WooCommerce use the same term, "payout currency" (basis 1), with the same definition (basis 3): Shopify's is "the currency that Shopify Payments uses to deposit money into your bank account", WooCommerce's "the currency in which funds are paid out into your bank account" (stated). On store fake-demo-sharrwah (30 September 2026, observed), a report page's saved markup hid a metric, "Payout amount in payout currency": "Value of the payout, in the currency the payout was issued in". Q7-SH-004 Q7-WC-004 Q7-SH-206
- **section 1, line 20:** - The currency paid out can differ from the one paid, and the provider converts: Shopify applies a rate and fee "at the time of payment capture"; WooCommerce converts a payment matching none of the seller's bank accounts "into your default currency and paid out into the default account"; on BigCommerce "the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope" (stated). On store fake-demo-sharrwah (30 September 2026, observed), a report page's saved markup also hid a metric, "Foreign exchange fees": "Currency conversion fees you pay when customers purchase in a different currency". Q7-SH-013 Q7-WC-K0737 Q7-BC-P0015 Q7-SH-207
- **section 1, line 21:** - Shopify pays out in several currencies with Multi-Currency Payouts, where "orders paid for in that currency are paid out to that bank account", on its Advanced and Plus plans. Q7-SH-P0155
- **section 1, line 28:** - In the runs (observed), a Shopify store with an address in Sanaa, Yemen showed "Yemeni Rial (YER)" in its store defaults (store fake-demo-sharrwah, 5 October 2026), and Salla's list of currencies a store could add held Yemen's YER (store demo, 9 October 2026). Q7-SH-191 Q7-SA-031
- **section 1, line 29:** - A market takes its default currency from its countries or its place: a Shopify market for one country is "automatically set to that country's local currency" (not checked on Salla, Q7-SH-079); Zid shows "السوق الافتراضي وهو السوق المحلي" (stated). On store demo-fake-dev-store (30 September 2026, observed), saved markup held, for a market including Saudi Arabia, Saudi Riyal (SAR) as "Recommended" above an "All currencies" list marking Yemeni Rial (YER) as "Store currency"; and, on a draft order for the market Yemen, "Market currency" Yemeni Rial (YER) with eight "Other currencies". Q7-SH-079 Q7-ZD-020 Q7-SH-202 Q7-SH-203 Q7-SH-201
- **section 1, line 30:** - The currency charged is set per currency, within what the provider supports, by BigCommerce's seller through each currency's "Transacting currency"; on Shopify, by the store's primary gateway (above). Q7-BC-031 Q7-SH-K1937
- **section 1, line 31:** - The currency paid out is set for the payment account, by its region, entity, country or provider. Shopify's "domestic currency is determined by your Shopify Payments region and is the default currency for your payouts", and each business entity has "its own Shopify Payments account, payout currency, and bank account" (not checked on Salla, Q7-SH-K1268); where WooCommerce's chart lists one currency for a country, "those payouts can only be sent to banks in your country"; BigCommerce's merchant sets it "through its payment provider". Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-BC-P0016
- **section 1, line 35:** - Who may change a store's currency: on Shopify "Only the store owner can change store currency", and a change after the first order needs a check of "I understand the risk of changing the store currency" (stated); on Salla, holders of the staff permission `currency_setting_edit` (observed in store demo's staff permission list, 8 October 2026). On store capture-plus (2 October 2026, observed), the General settings page's saved markup held a "Change store currency" heading with only Save and Cancel under it. Q7-SH-008 Q7-SH-181 Q7-SA-K1950 Q7-SH-205
- **section 1, line 37:** - A change treats prices in one of three ways: Q7-SH-006 Q7-ZD-K0302 Q7-SA-004
- **section 1, line 38:** - The numbers stay and the currency changes, on Shopify and BigCommerce, which match on role (basis 4): "The currency of your product prices and discount rates update automatically, but not the amount"; "changing the default currency will not trigger price recalculation for the catalog". Q7-SH-006 Q7-BC-053
- **section 1, line 42:** - Rates are automatic or fixed by the seller. Shopify's markets choose Dynamic, "to automatically convert prices", or Manual, "to set a fixed exchange rate" (not checked on Salla, Q7-SH-078); WooCommerce's rates come by default from "the WooPayments server"; BigCommerce's merchant can use its Currency Service or "use the API to automatically update the exchange rate from their trusted source" (stated). On store demo-fake-dev-store (30 September 2026, observed), a market's saved markup held "Exchange rate (FX)" with Dynamic, Manual and "1 YER = 0.0024448788 SAR", and "Price rounding" with "Round up to the nearest SAR 1.00" and "Do not round prices". Q7-SH-078 Q7-WC-K0755 Q7-BC-035 Q7-SH-204
- **section 1, line 43:** - Refunds go in the currency paid, and match on role (basis 4): on Shopify "in the currency that they used to pay for the order"; on WooCommerce the balance is debited "using the exchange rate at the time you issued the refund". Q7-SH-068 Q7-WC-019
- **section 1, line 44:** - The platforms change currencies themselves: on stores using Shopify Payments, Shopify changed markets that charged in Bulgarian Lev "to display and charge customers in Euros on your behalf" (not checked on Salla or BigCommerce, Q7-SH-107); one of WooCommerce's upgrade routines rewrote recorded orders' `_order_currency` from KIP to LAK (shipped). Q7-SH-107 Q7-WC-057
- **section 1, line 48:** - Shopify: the Shopify Payments account "Tracks current balances across all supported currencies". The currencies of Reserved funds, of funds in a Payment Processor Account, and of the Global-e account in which Shopify Payments "holds the money" of international Managed Markets orders weren't in what was read. Not checked on Salla, for the Global-e account (Q7-SH-K1600), nor on BigCommerce, for the currencies not read. Q7-SH-131 Q7-SH-N01 Q7-SH-K1600 Q7-SH-N04
- **section 1, line 53:** - Shopify, WooCommerce and BigCommerce keep the seller's balance per currency, and match on role (basis 4): "across all supported currencies", "in each currency", "per currency" (stated). Q7-SH-131 Q7-WC-048 Q7-BC-058
- **section 2, line 58:** - From the platforms: Zid's smallest unit and WooCommerce's ISO codes. Why: rule 3, as codes and units sit in every stored amount; and rule 2, as currencies change, like Shopify's Bulgarian markets moving to the euro, or WooCommerce rewriting KIP to LAK. Q7-SH-107 Q7-WC-057
- **section 2, line 59:** - **Money amount**. Proposed: every stored amount is a whole number of its currency's smallest unit, with that currency's code; a converted amount keeps the original, the result and the rate between them. Q7-ZD-024 Q7-SH-123
- **section 2, line 60:** - From the platforms: the unit from Zid, and the pair from Shopify's MoneyBag, which holds the shop's and the customer's amounts. Why: rule 3, as changing how amounts are stored after launch would touch every order and balance. Q7-ZD-024 Q7-SH-123
- **section 2, line 61:** - **Store currency**. Proposed: each store has exactly one, in which the seller's prices are entered and reports run. The seller picks it when creating the store, from those its place allows, with the place's default preselected. Q7-WC-K0745 Q7-SH-K1935 Q7-ZD-001
- **section 2, line 65:** - **Market**, with its **display currency**. Proposed: a group of buyer countries within one store, with one display currency, other currencies its buyers may pick, and, optionally, its own prices in its own currency. Every store starts with one market for its own place, in the store currency. A buyer is placed by country, then may pick among the market's currencies. Q7-SH-076 Q7-ZD-K0236 Q7-ZD-020
- **section 2, line 66:** - From the platforms: Shopify's currency per market and one-country default; Zid's market currency, local default market and prices "وبعملة السوق نفسها"; Salla's default by location and the buyer's own pick. Why: rule 1, as one store is set up for each place it sells to; and rule 3, as the level at which prices and currencies sit is part of the data model. Q7-SH-079 Q7-ZD-019 Q7-SA-K1957 Q7-SA-K1956
- **section 2, line 69:** - From the platforms: BigCommerce's transactional or display-only setting per currency, and its gateway rule; Shopify's and Salla's charge in one currency when the provider can't take the shown one. Why: rule 2, as a change of provider then changes a market's set-up, not checkout or orders. Q7-SH-K1938 Q7-SA-K1963
- **section 2, line 70:** - Not taken: Shopify's tie of local-currency payment to the store's one primary gateway, for all markets, as a store selling to several places may need a provider in each (rule 1). Q7-SH-K1937
- **section 2, line 71:** - **Order currency record**. Proposed: an order records, when placed, the charged currency and every amount in it, the same amounts in the store currency, the display currency if different, and each rate used, with its source and time; none is recomputed. A refund goes out in the charged currency, any conversion of it at that day's rate, recorded beside the first. Q7-SH-123 Q7-ZD-010 Q7-BC-020
- **section 2, line 72:** - From the platforms: the currencies and rates Shopify, Zid, BigCommerce and Salla record on orders; WooCommerce's earlier orders, which keep their currency and totals; refunds in the currency paid (Shopify) at the refund's rate (WooCommerce). Why: rule 3, as an order whose amounts follow a later rate or store currency no longer shows what the buyer paid. Q7-SA-016 Q7-WC-027 Q7-SH-068 Q7-WC-019
- **section 2, line 74:** - **Exchange rate**, with its **rate source**. Proposed: each rate Sharrwah uses, to show prices or convert amounts for reports, comes from the rate source of that currency of the market: automatic, from a plugged-in **rate provider** on a stated schedule, or manual, fixed by the seller; converted prices follow that currency's rounding rule. A payment provider's rate on a payment is its own; Sharrwah records the rate and fee it reports. Q7-SH-078 Q7-WC-K0755 Q7-BC-035
- **section 2, line 75:** - From the platforms: Shopify's Dynamic or Manual rate per market, with Price rounding beside it in a market's saved markup (store demo-fake-dev-store, 30 September 2026, observed); WooCommerce's server rates and BigCommerce's merchant's own source through the API; the rate on a payment, outside BigCommerce's scope, and Shopify's rate and fee at capture. Why: rule 2, as the source is likely to change; and rule 1, as a place may need its own. Q7-BC-P0015 Q7-SH-013 Q7-SH-204
- **section 2, line 76:** - **Payout account**, with its **payout currency**. Proposed: each destination a seller is paid out to has one payout currency. A seller may have several, one the default, and a payment in a currency matching none is converted by the provider to the default's. Which currencies a payout account may have is set per place and provider. Q7-SH-004 Q7-WC-K0737 Q7-SH-P0155
- **section 2, line 77:** - From the platforms: Shopify's and WooCommerce's payout currency and default account, and Shopify's Multi-Currency Payouts; payout currencies bounded by region or entity (Shopify), country and its banks (WooCommerce, Salla), or the provider (BigCommerce). Why: rule 3, as the money flow ends at this payout, and partner contracts decide its currencies. Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-SA-K1964 Q7-BC-P0016
- **section 2, line 78:** - **Seller ledger**. Proposed: each amount owed to or by a seller, for sales, fees, refunds and payouts, is an entry in one currency. Balances are per currency, never added across currencies, and move between currencies only by a recorded conversion. The ledger records what is owed, whoever holds the money. Q7-SH-131 Q7-WC-048 Q7-BC-058
- **section 2, line 81:** - **Currency migration**. Proposed: the store owner may change the store currency until the first order; after it, only a currency migration run by Sharrwah can, leaving every recorded order as it is and stating whether prices convert at a stated rate or keep their numbers. The same migration serves a change Sharrwah makes for a whole place. Q7-SA-004 Q7-SH-008 Q7-WC-027
- **section 2, line 82:** - From the platforms: Salla's bar once there are orders; Shopify's owner-only change; prices kept by number (Shopify, BigCommerce) or converted (Zid); Shopify's Bulgaria change, made on its stores' behalf, and WooCommerce's routine rewriting orders' currency code. Why: rule 3, as a later change mustn't rewrite an order's currency; and rule 4, as the treatment of prices stays open (section 5). Q7-SH-006 Q7-BC-053 Q7-ZD-K0302 Q7-SH-107 Q7-WC-057
- **section 2, line 83:** - Not taken: Shopify's change by the owner after the first order, behind a risk check, as Shopify lists its effects on reports, pending payments and refunds; self-contained orders let it be allowed later (rule 4). Q7-SH-181 Q7-SH-006
- **section 3, line 88:** - **Provider currency capability**: each payment provider plugged in declares, per place and payment method, the currencies it can charge and pay out in, and reports each payment's rate and fee. It draws on BigCommerce's gateway support per currency and settlement currency set through the provider, Shopify's rate and fee at capture, and Shopify's support by method, down to "Unsupported and prices convert to shop currency". Q7-BC-005 Q7-BC-P0016 Q7-SH-013 Q7-SH-099
- **section 3, line 90:** - A cross-border seller of record, as Shopify's Managed Markets works through a Global-e account, is kept open (section 5). Q7-SH-K1600
- **section 3, line 91:** - What is set per what. Where the platforms differ in level, the proposal takes the finer, so a coarser set-up is still one setting (rule 1): Q7-SH-078 Q7-BC-031
- **section 3, line 94:** - Per market: the **display currency**, its other currencies and its own prices, as Shopify and Zid set them per market. Q7-SH-076 Q7-ZD-019
- **section 3, line 95:** - Per currency of a market: charged or shown only, as BigCommerce sets for each currency; and the **rate source**, which Shopify sets per market and BigCommerce per currency. Q7-BC-031 Q7-SH-078
- **section 3, line 97:** - Per payout account: the **payout currency**, as Shopify's and Salla's bank accounts each carry one. Q7-SH-004 Q7-SA-K1964
- **section 3, line 100:** - Who sets each: Q7-SH-008 Q7-SA-K1956 Q7-BC-P0015
- **section 3, line 101:** - Sharrwah sets the **currency table** and each place's **place currency settings**, and runs each **currency migration**, as Shopify changed its stores' Bulgarian markets on their behalf. Q7-SH-107
- **section 3, line 102:** - The store owner sets the **store currency**, as only the owner can on Shopify; staff holding a currency permission, like Salla's `currency_setting_edit` (store demo, 8 October 2026, observed), set the markets' currencies and rate sources. Q7-SH-008 Q7-SA-K1950
- **section 5, line 123:** - Which currencies can be charged and paid out at each place. Keep them as **provider currency capability** data for each place, not code. Settled by: the contracts with the providers Sharrwah works with (section 7). Q7-SH-K1937 Q7-BC-P0016
- **section 5, line 124:** - Several payout currencies, and an entity per place. Shopify gives each business entity its own payout currency, and several payout currencies only on some plans. Keep each **payout account** tied to its provider account and contracting entity. Settled by: where the company is based, and its contracts (section 7). Q7-SH-K1268 Q7-SH-P0155
- **section 5, line 125:** - How a **currency migration** treats prices: converted at a stated rate, as Zid's help describes, or kept by number, as Shopify and BigCommerce say. Keep the **order currency record** self-contained, so either fits. Settled by: the first migration Sharrwah needs. Q7-ZD-K0302 Q7-SH-006
- **section 5, line 126:** - A cross-border seller of record: Shopify's Managed Markets holds the money in a Global-e account whose currency wasn't in what was read. Keep the **order currency record** able to hold a third party's charged currency and rate. Settled by: a company decision on such a partner (section 7). Q7-SH-K1600 Q7-SH-N04
- **section 7, line 146:** - Which payment providers Sharrwah works with at each place, given that what they support decides the currencies buyers can be charged in, and sellers paid out in; Stripe isn't available for Yemen. Q7-SH-K1937 Q7-BC-P0016 Q7-SA-K1963 YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 148:** - Whether Sharrwah converts currencies, or charges a conversion fee, itself, as Shopify applies a rate and fee at capture, or leaves conversion and its rate to the providers, as BigCommerce does. At the internationally recognized government's area, foreign currency is bought and sold in cash only, not through digital platforms. Q7-SH-013 Q7-BC-P0015 YK-05 (cash only, not through digital platforms @ the internationally recognized government's area, as of 2025-02-22)
- **section 7, line 150:** - Where the company is based, and whether it contracts through a separate entity in each place, since a payout currency can follow the payment account's region or entity. Q7-SH-012 Q7-SH-K1268
- **section 7, line 152:** - Whether Sharrwah works with a cross-border seller of record, as Shopify does through Managed Markets. Q7-SH-K1600
- **section 7, line 153:** - Sharrwah's own legal position on keeping sellers' balances and on converting currencies, and any licence either needs, for the founder with a lawyer. The platforms' terms show only what they require of their sellers: Shopify's, that a seller opens accounts with Payment Processors; Salla's, that it provides payment and settlement through its partners. Q7-SH-P0010 Q7-SA-P0079
- **section 8, line 159:** - What the records show: Shopify and WooCommerce define the payout currency in the same terms, and BigCommerce's settlement currency matches it on role (basis 4). It is set for the payment account: by region or business entity on Shopify, with more currencies on some plans; by country on WooCommerce; through the provider on BigCommerce; by the country's banks on Salla. Balances before payout are kept per currency on Shopify, WooCommerce and BigCommerce. Salla's balance holds sales proceeds before transfer; the page naming its currency wasn't read, and the run on store real-merchant gave the store's wallets in SAR (12 October 2026, observed). Zid's terms set its wallet's currency by the merchant's country; the currency of Zid Pay's balance and deposits, and of Shopify's reserved funds, wasn't in what was read. S01-VP-23 Q7-SH-004 Q7-WC-004 Q7-BC-P0014 Q7-SH-012 Q7-SH-K1268 Q7-SH-P0155 Q7-WC-K0739 Q7-BC-P0016 Q7-SA-K1964 Q7-SH-131 Q7-WC-048 Q7-BC-058 Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022 Q7-ZD-P0122 Q7-ZD-N01 Q7-ZD-N02 Q7-SH-N01

## The cards

### Q7-SH-K1935

**Cited at:** section 1, line 7; section 2, line 61

**The same record as Q1-SH-K1935,** whose card is in `Q1-shopify-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Your store currency is the currency used within your Shopify admin for pricing products and running reports.
- scope: 

### Q7-SH-123

**Cited at:** section 1, line 9; section 1, line 18; section 2, line 59; section 2, line 60; section 2, line 71

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-123
- bears_on: 1
- identifier: MoneyBag.presentmentMoney; MoneyBag.shopMoney
- statement: The `presentmentMoney` field contains the amount in the customer's selected currency. The `shopMoney` field contains the equivalent in the shop's base currency.
- scope: GraphQL Admin API 2026-10
- cite_ids: Q7-SH-C148
- from: held

**Citation Q7-SH-C148:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/admin-graphql-schema/2026-10/items.jsonl` | line 2263 (type MoneyBag, description) | 2026-09-30 | kind: stated | quote check: found
- quote: The `presentmentMoney` field contains the amount in the customer's selected currency. The `shopMoney` field contains the equivalent in the shop's base currency.
- in context: MoneyBag OBJECT A collection of monetary values in their respective currencies. Used throughout the API for multi-currency pricing and transactions, when an amount in the shop's currency is converted to the customer's currency of choice. ⟪The `presentmentMoney` field contains the amount in the customer's selected currency. The `shopMoney` field contains the equivalent in the shop's base currency.⟫ presentmentMoney MoneyV2! shopMoney MoneyV2! {"name": "MoneyBag", "kind": "OBJECT", "description": "A collection of monetary values in their respective currencies. Used throughout the API for multi-currency pricing and transactions, when an amount in the shop's currency is converted to the customer's currency of choice. The `presentmentMoney` field contains the amount in the customer's selected currency. The `shopMoney` field contains the equiva…

### Q7-SH-076

**Cited at:** section 1, line 10; section 2, line 65; section 3, line 94

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-076
- bears_on: 1;2
- identifier: currency customization
- statement: Each market can have a currency customization that determines what currency is displayed to customers in that market. When a customer visits your store, their market is identified and prices are displayed in the currency configured for that market.
- cite_ids: Q7-SH-C091
- from: held

**Citation Q7-SH-C091:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md` | Setting up currencies for markets | 2026-10-16 | kind: stated | quote check: found
- quote: Each market can have a currency customization that determines what currency is displayed to customers in that market. When a customer visits your store, their market is identified and prices are displayed in the currency configured for that market.
- title: Setting up currencies for markets
- the page opens: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency. You can set a specific currency for each market so that your customers can browse, pay, and receive refunds in a currency that's familiar to them. Displaying prices in local currencies improves the customer experience and can help to increase conversion rates in international m…
- a note box: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency.
- a note box: Sidekick You can ask Sidekick which currency a market shows to buyers, whether local currencies and rounding are turned on, and whether its exchange rate is automatic or manual. Use a prompt such as What currency does each of my markets show buyers and are any using manual exchange rates.
- a note box: Caution When using manual exchange rates, you're responsible for keeping rates current. If your manual rate diverges significantly from the actual exchange rate, then you might experience inaccuracies on international orders. Review your manual rates regularly to ensure they reflect current market c
- headings: Setting up currencies for markets
- in context: …opify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency.</p> </aside> You can set a specific currency for each market so that your customers can browse, pay, and receive refunds in a currency that's familiar to them. Displaying prices in local currencies improves the customer experience and can help to increase conversion rates in international markets. ⟪Each market can have a currency customization that determines what currency is displayed to customers in that market. When a customer visits your store, their market is identified and prices are displayed in the currency configured for that market.⟫ If a market's currency is different from the currency your product prices are set in, then prices are converted using either automatic or manual exchange rates. A [currency conversion fee](/manual/international/pricing/fees#shopify-payments-currency-conversion-fee) is applied when using automatic rates. ## Currency inheritance [Submarkets](/manual/markets/getting-started/submarkets) inherit the currency customization of their parent market by de…

### Q7-SH-K1938

**Cited at:** section 1, line 12; section 1, line 13; section 2, line 69

**Record** (`studies/proposals/records/Q7/shopify/copied.tsv`):
- concern_id: SH-C-108
- placement: decides
- structure: https://help.shopify.com/en/manual/international/payments.md
- identifier: Shopify Payments and other payment providers
- statement: At checkout, the price will be converted to your store's default currency, and your customer will be charged in that currency.
- cite_ids: SH-S-0546
- note: first run's citation

**Citation SH-S-0546:** `https://help.shopify.com/en/manual/international/payments.md` | Shopify Payments and other payment providers | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/036-help.shopify.com/text.txt` (4380 bytes), fetched 2026-10-11T06:12:59Z, captured
- quote: At checkout, the price will be converted to your store's default currency, and your customer will be charged in that currency.
- title: Payments
- the page opens: Your market settings include a payments card that displays eligible local payment methods, as well as a link to your payment settings where you can activate and customize a variety of payment methods. Shopify Payments and other payment providers {#other-payment-providers} Only stores with Shopify Payments or Adyen as the primary gateway can process payments in a customer's local currency. The following payment options are compatible with multi-currency processing: * Shopify Payments credit card …
- a note box: Tip If you want to encourage your customers to use multi-currency compatible payment methods, then use Shopify Scripts to hide other payment providers for customers who have a foreign currency at checkout.
- headings: Payments > Shopify Payments and other payment providers {#other-payment-providers}
- in context: …yen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway can process payments in a customer's local currency. The following payment options are compatible with multi-currency processing: * Shopify Payments credit card payments * Shop Pay * Apple Pay and Google Pay * Paypal Express If you use a different payment provider, then the local currency feature will only affect how prices are displayed to customers in your store. ⟪At checkout, the price will be converted to your store's default currency, and your customer will be charged in that currency.⟫ Here's how the currency conversion process works for customers: * Prices will display to customers in their local currency * At checkout, prices will be converted to your store's default currency * The final charge on their payment method will be in your store's default currency * They might incur additional currency conversion fees from their payment provider For example, your store currency is USD, and you sell a T-shirt for $10.00 USD. Your c…

### Q7-SH-K1937

**Cited at:** section 1, line 13; section 1, line 30; section 2, line 70; section 5, line 123; section 7, line 146

**The same record as Q1-SH-K1937,** whose card is in `Q1-shopify-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Only stores with [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway can process payments in a customer's local currency.
- scope: 

### Q7-SH-124

**Cited at:** section 1, line 18

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-124
- bears_on: 1
- identifier: Order.presentmentCurrencyCode
- statement: {"name": "presentmentCurrencyCode", "type": "CurrencyCode!"}
- scope: GraphQL Admin API 2026-10
- cite_ids: Q7-SH-C149
- from: held

**Citation Q7-SH-C149:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/admin-graphql-schema/2026-10/items.jsonl` | line 2306 (type Order, field presentmentCurrencyCode) | 2026-09-30 | kind: stated | quote check: found
- quote: {"name": "presentmentCurrencyCode", "type": "CurrencyCode!"}
- in context: …e": "originalTotalPriceSet", "type": "MoneyBag!"}, {"name": "paymentCollectionDetails", "type": "OrderPaymentCollectionDetails!"}, {"name": "paymentGatewayNames", "type": "[String!]!"}, {"name": "paymentTerms", "type": "PaymentTerms"}, {"name": "phone", "type": "String"}, {"name": "physicalLocation", "type": "Location", "deprecated": "Use `fulfillmentOrders` to get the fulfillment location for the order"}, {"name": "poNumber", "type": "String"}, ⟪{"name": "presentmentCurrencyCode", "type": "CurrencyCode!"}⟫, {"name": "processedAt", "type": "DateTime!"}, {"name": "productNetwork", "type": "Boolean!"}, {"name": "publication", "type": "Publication"}, {"name": "purchasingEntity", "type": "PurchasingEntity"}, {"name": "referralCode", "type": "String", "deprecated": "Use `customerJourneySummary.lastVisit.referralCode` instead"}, {"name": "referrerDisplayText", "type": "String", "deprecated": "Use `customerJourneySummary.lastVisit.referralInfoHtml` instea…

### Q7-SH-004

**Cited at:** section 1, line 19; section 2, line 76; section 3, line 97; section 8, line 159

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-004
- bears_on: 1;2
- identifier: Payout currency
- statement: The payout currency refers to the currency that Shopify Payments uses to deposit money into your bank account. This depends on the location of your store, and your bank account must generally be in the same country as your store.
- cite_ids: Q7-SH-C004
- from: held

**Citation Q7-SH-C004:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/understanding-store-and-payout-currencies.md` | Payout currency | 2026-10-16 | kind: stated | quote check: found
- quote: The payout currency refers to the currency that Shopify Payments uses to deposit money into your bank account. This depends on the location of your store, and your bank account must generally be in the same country as your store.
- title: Understanding your store and payout currencies
- the page opens: The currency on your Shopify admin and that is displayed to your customers on your online store is your store currency. The currency your deposits from Shopify Payments orders are made in is your payout currency. Store currency Your store currency is the currency used within your Shopify admin for pricing products and running reports. This is the primary currency that your customers will use when making purchases on your store. You can select any currency from the available options in your store…
- headings: Understanding your store and payout currencies > Payout currency
- in context: …he currency used within your Shopify admin for pricing products and running reports. This is the primary currency that your customers will use when making purchases on your store. You can select any currency from the available options in your store settings based on your customer base's location. Learn more about how to [change your store currency](/manual/payments/shopify-payments/store-currency/changing-your-store-currency). ## Payout currency ⟪The payout currency refers to the currency that Shopify Payments uses to deposit money into your bank account. This depends on the location of your store, and your bank account must generally be in the same country as your store.⟫ For instance, if your store is in Canada but you prefer to get paid in USD, then your bank account should also support USD and be based in Canada or the United States. Learn more about [bank account requirements](/manual/payments/shopify-payments/onboarding/bank-account-requirements).

### Q7-SH-206

**Cited at:** section 1, line 19

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-206
- bears_on: 1;4
- identifier: Analytics > Reports: Payout amount in payout currency
- statement: Payout amount in payout currency Value of the payout, in the currency the payout was issued in
- scope: store fake-demo-sharrwah, observed 2026-09-30
- cite_ids: Q7-SH-C234
- from: held
- note: In the saved HTML of step 1 (admin.shopify.com/store/fake-demo-sharrwah/analytics/reports/442400983), between ⟦hidden⟧ and ⟦/hidden⟧: text the markup itself hid. The step's aria.yaml shows the name Payout amount in payout currency, not this description. The run's answers.jsonl names fake-demo-sharrwah and ctcbwa-r1; the store is named by the step's address.

**Citation Q7-SH-C234:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T144209Z-sweep-instances/001.html.txt` | run 20260930T144209Z-sweep-instances, step 1, metric description, lines 362-363 and 787-788 | 2026-09-30 | kind: observed | quote check: found
- step 1: visit route analytics:reports:id (path from linked from 20260930T002940Z-sweep-trial step 10) | https://admin.shopify.com/store/fake-demo-sharrwah/analytics/reports/442400983?ql=FROM+payments%2C+gift_cards%2C+fees%2C+chargebacks%2C+store_credit_transactions%2C%0A++++store_credit_summaries%2C+payment_attempts%2C+shopify_payments_balance_report%2C%0A++++sales_taxes%2C+payouts%2C+pricing_adjustments%0A++SHOW+refunded_gift_card_value%2C+refunded_payments%2C+rounded_net_payments%2C%0A++++adjusted_gift_card_value%2C+average_foreign_exchange_fees%2C%0A++++average_managed_markets_fees%2C+average_international_fees%2C%0A++++average_shopify_payments_processing_fees%2C+cash_rounding%2C+chargeback_amount%2C%0A++++chargeback_rate%2C+chargebacks%2C+credited_store_credit_value%2C%0A++++debited_store_credit_value%2C+disabled_gift_card_value%2C+ending_gift_card_balance%2C%0A++++ending_store_credit_balance%2C+expired_store_credit_value%2C+failed_payment_attempts%2C%0A++++foreign_exchange_fees%2C+gift_card_balance_net_change%2C+gift_cards_adjusted%2C%0A++++gift_cards_disabled%2C+gift_cards_issued%2C+amount_gross%2C+gross_payments%2C%0A++++included_tax_amount%2C+international_fees%2C+issued_gift_card_balance%2C%0A++++managed_markets_fees%2C+managed_markets_taxes%2C+amount_net%2C+net_payments%2C%0A++++net_payments_excluding_gift_cards%2C+orders_with_transactions%2C%0A++++payment_authorization_rate%2C+payment_authorization_rate_raw%2C%0A++++shopify_payments_processing_fees%2C+payout_amount%2C%0A++++payout_amount_in_payout_currency%2C+pricing_adjustment_value%2C%0A++++redeemed_gift_card_value%2C+sales_taxes%2C+sold_gift_card_balance%2C%0A++++starting_gift_card_balance%2C+starting_store_credit_balance%2C%0A++++store_credit_balance_net_change%2C+successful_payments%2C+total_payment_attempts%2C%0A++++transaction_amount%2C+transaction_count%2C+transactions%2C+unique_payment_attempts%0A++SINCE+startOfDay%28-30d%29+UNTIL+today%0A++ORDER+BY+refunded_gift_card_value+DESC%0AVISUALIZE+refunded_gift_card_value+TYPE+treemap | "My Store · Reports · demo-Refunded gift card value · Shopify" | 2026-09-30T14:42:11.530Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T144209Z-sweep-instances/steps/001.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T144209Z-sweep-instances/steps/001.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T144209Z-sweep-instances/001.html.txt`
- quote: Payout amount in payout currency Value of the payout, in the currency the payout was issued in
- in context: …cessing fees you pay per order through Shopify Payments Helps you: Calculate net revenue after subtracting payment processing costs Compare processing fees across different payment methods or order sizes Cumulative available ⟦/hidden⟧ ⟦hidden⟧ Payout amount Value of the payout Helps you: Track your total earnings from Shopify Payments over time Plan business expenses and investments based on payout amounts Cumulative available ⟦/hidden⟧ ⟦hidden⟧ ⟪Payout amount in payout currency Value of the payout, in the currency the payout was issued in⟫ Helps you: Track payouts in their original currency to avoid conversion confusion Plan international banking and currency exchange based on payout currencies Cumulative available ⟦/hidden⟧ ⟦hidden⟧ Pricing adjustment value Value of pricing adjustments made to orders Helps you: Calculate the total revenue impact of your pricing strategies Compare the profitability of different pricing adjustment amounts Cumulative available ⟦/hidden⟧ ⟦hidden⟧ Red…

### Q7-SH-013

**Cited at:** section 1, line 20; section 2, line 75; section 3, line 88; section 7, line 148

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-013
- bears_on: 1;3
- identifier: Currency conversion and exchange rates
- statement: When a customer pays in a currency that's different from your payout currency, a currency exchange rate and conversion fee are applied at the time of payment capture. If you issue a refund, then the refund is processed at the current exchange rate, and no conversion fees are charged for refunds.
- cite_ids: Q7-SH-C024
- from: held

**Citation Q7-SH-C024:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/supported-payout-currencies.md` | Currency conversion and exchange rates {#shopify-payments-payout-conversion} | 2026-10-16 | kind: stated | quote check: found
- quote: When a customer pays in a currency that's different from your payout currency, a currency exchange rate and conversion fee are applied at the time of payment capture. If you issue a refund, then the refund is processed at the current exchange rate, and no conversion fees are charged for refunds.
- title: Supported payout currencies
- the page opens: Various payout currencies are available through Shopify Payments, depending on your store's location. The payout currencies available to you depend on which country or region your store is based in. Your domestic currency is determined by your store location, and additional non-domestic currencies might be available depending on your Shopify plan. Understanding your domestic currency helps you determine whether Multi-Currency Payout fees apply to your payouts. Domestic vs. non-domestic currencie…
- a note box: Note If your store is based in the United States, then USD is always your default payout currency and can't be changed to another currency. You can add bank accounts in other supported currencies such as AUD, CAD, EUR, and GBP to receive secondary payouts in those currencies, but your primary payout
- headings: Supported payout currencies > Currency conversion and exchange rates {#shopify-payments-payout-conversion}
- in context: …ope="row">Domestic currency</td> <td>The default currency based on your store's location (for example, EUR for Germany, CAD for Canada)</td> <td>No fee</td> </tr> <tr> <td scope="row">Non-domestic currency</td> <td>Any currency that isn't your domestic currency (for example, USD for a Canada-based store)</td> <td>Fee applies based on plan</td> </tr> </tbody> </table> ## Currency conversion and exchange rates {#shopify-payments-payout-conversion} ⟪When a customer pays in a currency that's different from your payout currency, a currency exchange rate and conversion fee are applied at the time of payment capture. If you issue a refund, then the refund is processed at the current exchange rate, and no conversion fees are charged for refunds.⟫ In the [**Payments**](https://admin.shopify.com/settings/payments) section of your Shopify admin, you can track the current exchange rates and view historical exchange rates used for specific orders in the order's [timeline](/manual/fulfillment/managing-orders/managing-order-details#view-an-orders-timeline). ## Adding payout currencies {#changing-your-payout-currency} If your country and Shopify plan support [Multi-Currency Payouts](/manual/paym…

### Q7-SH-207

**Cited at:** section 1, line 20

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-207
- bears_on: 1;3
- identifier: Analytics > Reports: Foreign exchange fees
- statement: Foreign exchange fees Currency conversion fees you pay when customers purchase in a different currency
- scope: store fake-demo-sharrwah, observed 2026-09-30
- cite_ids: Q7-SH-C235
- from: held
- note: In the saved HTML of step 1 (admin.shopify.com/store/fake-demo-sharrwah/analytics/reports/442400983), between ⟦hidden⟧ and ⟦/hidden⟧: text the markup itself hid. The step's aria.yaml does not show this description. The store is named by the step's address.

**Citation Q7-SH-C235:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T144209Z-sweep-instances/001.html.txt` | run 20260930T144209Z-sweep-instances, step 1, metric description, lines 655-656 | 2026-09-30 | kind: observed | quote check: found
- step 1: visit route analytics:reports:id (path from linked from 20260930T002940Z-sweep-trial step 10) | https://admin.shopify.com/store/fake-demo-sharrwah/analytics/reports/442400983?ql=FROM+payments%2C+gift_cards%2C+fees%2C+chargebacks%2C+store_credit_transactions%2C%0A++++store_credit_summaries%2C+payment_attempts%2C+shopify_payments_balance_report%2C%0A++++sales_taxes%2C+payouts%2C+pricing_adjustments%0A++SHOW+refunded_gift_card_value%2C+refunded_payments%2C+rounded_net_payments%2C%0A++++adjusted_gift_card_value%2C+average_foreign_exchange_fees%2C%0A++++average_managed_markets_fees%2C+average_international_fees%2C%0A++++average_shopify_payments_processing_fees%2C+cash_rounding%2C+chargeback_amount%2C%0A++++chargeback_rate%2C+chargebacks%2C+credited_store_credit_value%2C%0A++++debited_store_credit_value%2C+disabled_gift_card_value%2C+ending_gift_card_balance%2C%0A++++ending_store_credit_balance%2C+expired_store_credit_value%2C+failed_payment_attempts%2C%0A++++foreign_exchange_fees%2C+gift_card_balance_net_change%2C+gift_cards_adjusted%2C%0A++++gift_cards_disabled%2C+gift_cards_issued%2C+amount_gross%2C+gross_payments%2C%0A++++included_tax_amount%2C+international_fees%2C+issued_gift_card_balance%2C%0A++++managed_markets_fees%2C+managed_markets_taxes%2C+amount_net%2C+net_payments%2C%0A++++net_payments_excluding_gift_cards%2C+orders_with_transactions%2C%0A++++payment_authorization_rate%2C+payment_authorization_rate_raw%2C%0A++++shopify_payments_processing_fees%2C+payout_amount%2C%0A++++payout_amount_in_payout_currency%2C+pricing_adjustment_value%2C%0A++++redeemed_gift_card_value%2C+sales_taxes%2C+sold_gift_card_balance%2C%0A++++starting_gift_card_balance%2C+starting_store_credit_balance%2C%0A++++store_credit_balance_net_change%2C+successful_payments%2C+total_payment_attempts%2C%0A++++transaction_amount%2C+transaction_count%2C+transactions%2C+unique_payment_attempts%0A++SINCE+startOfDay%28-30d%29+UNTIL+today%0A++ORDER+BY+refunded_gift_card_value+DESC%0AVISUALIZE+refunded_gift_card_value+TYPE+treemap | "My Store · Reports · demo-Refunded gift card value · Shopify" | 2026-09-30T14:42:11.530Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T144209Z-sweep-instances/steps/001.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T144209Z-sweep-instances/steps/001.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T144209Z-sweep-instances/001.html.txt`
- quote: Foreign exchange fees Currency conversion fees you pay when customers purchase in a different currency
- in context: …er revenue from expired store credits that customers never used Set optimal expiration periods to balance customer satisfaction with cash flow Cumulative available ⟦/hidden⟧ ⟦hidden⟧ Failed payment attempts Number of failed payment attempts Helps you: Identify payment methods or processors that fail too often and need replacement Reduce revenue loss by improving payment systems that cause the most failures Cumulative available ⟦/hidden⟧ ⟦hidden⟧ ⟪Foreign exchange fees Currency conversion fees you pay when customers purchase in a different currency⟫ Helps you: Factor conversion costs into international pricing strategies Identify which currencies cost the most to accept Cumulative available ⟦/hidden⟧ ⟦hidden⟧ Gift card balance net change Net change in gift card balances in the given period Gift card balance net change = ending gift card balance - starting gift card balance Helps you: Track whether your gift card liability is growing or shrinking over time Adjust gift card marketing when lia…

### Q7-SH-P0155

**Cited at:** section 1, line 21; section 2, line 76; section 5, line 124; section 8, line 159

**Record** (`studies/proposals/records/Q7/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-154
- bullet: e;end-payout
- placement: decides
- identifier: Multi-Currency Payouts, Set up Multi-Currency Payouts
- statement: If your store is on the Advanced plan or the Shopify Plus plan in an eligible Shopify Payments region, then you can set up more than one bank account with Multi-Currency Payouts. You can add a secondary payout account in a non-domestic currency, and orders paid for in that currency are paid out to that bank account.
- scope: Advanced plan or Shopify Plus plan, eligible Shopify Payments region
- conditions: none stated
- cite_ids: S01-SH-C364;S01-SH-C365
- from: new
- note: Phase A3 audit, recorded under the addition to step 3 (anything else the documents read state on the subject).

**Citation S01-SH-C364:** `sharrwah-knowledge-map@0189968256432898fd8ec48937109901f18a6412:evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/073-help.shopify.com/text.txt` | Set up Multi-Currency Payouts | 2026-10-11 | kind: stated | quote check: found
- quote: If your store is on the Advanced plan or the Shopify Plus plan in an eligible Shopify Payments region, then you can set up more than one bank account with Multi-Currency Payouts.
- title: Managing Multi-Currency Payouts with Shopify Payments
- the page opens: If you have an international customer base, then handling payouts in multiple currencies can help you optimize the payment process. With Multi-Currency Payouts, you can add multiple bank accounts to receive payouts in different currencies and avoid currency exchange fees. To use Multi-Currency Payouts, your store must meet specific plan and location requirements. You can add one bank account for each supported payout currency available for your region and Shopify plan, and fees apply when you re…
- a note box: Note If you add a payout bank account more than 24 hours after completing your Shopify Payments setup, then your payouts are temporarily paused for 3-5 business days. If you use Multi-Currency Payouts, then adding a bank account for a new currency can pause payouts to all of your payout accounts, no
- a note box: Note The Multi-Currency Payout fee is based on the payout currency, not whether a currency conversion occurs. Even if a customer pays in USD and you receive a payout in USD, the fee applies if USD isn't your domestic currency.
- headings: Managing Multi-Currency Payouts with Shopify Payments > Requirements for Multi-Currency Payouts > Plan requirements
- in context: …ngdom (GBP)</td> <td>USD payouts are issued to a United States-based bank account. Non-USD payouts, such as AUD, CAD, EUR, and GBP payouts, require a bank account outside the United States in the corresponding currency's region. EUR payouts require an IBAN from a supported SEPA country; IBANs issued in Monaco (MC), San Marino (SM), Andorra (AD), and Vatican City (VA) aren't supported.</td> </tr> </tbody> </table> ## Set up Multi-Currency Payouts ⟪If your store is on the Advanced plan or the Shopify Plus plan in an eligible Shopify Payments region, then you can set up more than one bank account with Multi-Currency Payouts.⟫ You can add a secondary payout account in a non-domestic currency, and orders paid for in that currency are paid out to that bank account. With this setup, you can receive payouts in that currency without incurring foreign exchange, or FX, fees. ### Add a bank account for Multi-Currency Payouts {#add-multi-currency-bank} For businesses located in regions such as Canada, where both CAD and USD are commonly used, you can link two bank accounts to …

**Citation S01-SH-C365:** `sharrwah-knowledge-map@0189968256432898fd8ec48937109901f18a6412:evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/073-help.shopify.com/text.txt` | Set up Multi-Currency Payouts | 2026-10-11 | kind: stated | quote check: found
- quote: You can add a secondary payout account in a non-domestic currency, and orders paid for in that currency are paid out to that bank account.
- title, opening and note boxes: as for this source's citation above
- headings: Managing Multi-Currency Payouts with Shopify Payments > Set up Multi-Currency Payouts
- in context: …ed States in the corresponding currency's region. EUR payouts require an IBAN from a supported SEPA country; IBANs issued in Monaco (MC), San Marino (SM), Andorra (AD), and Vatican City (VA) aren't supported.</td> </tr> </tbody> </table> ## Set up Multi-Currency Payouts If your store is on the Advanced plan or the Shopify Plus plan in an eligible Shopify Payments region, then you can set up more than one bank account with Multi-Currency Payouts. ⟪You can add a secondary payout account in a non-domestic currency, and orders paid for in that currency are paid out to that bank account.⟫ With this setup, you can receive payouts in that currency without incurring foreign exchange, or FX, fees. ### Add a bank account for Multi-Currency Payouts {#add-multi-currency-bank} For businesses located in regions such as Canada, where both CAD and USD are commonly used, you can link two bank accounts to receive payouts in each currency. You can add a bank account to receive payouts in a non-domestic currency. For Shopify Payments accounts i…

### Q7-SH-191

**Cited at:** section 1, line 28

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-191
- bears_on: 1;2
- identifier: Settings > General: Store defaults, Currency display
- statement: Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER)
- scope: store fake-demo-sharrwah, observed 2026-10-05; Store address: Sanaa, Yemen
- cite_ids: Q7-SH-C216;Q7-SH-C217
- from: held
- note: The store is named by the step's address; the run's answers.jsonl names fake-demo-sharrwah and ctcbwa-r1

**Citation Q7-SH-C216:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt` | step 170 (admin.shopify.com/store/fake-demo-sharrwah/settings/general), Store defaults | 2026-10-05 | kind: observed | quote check: found
- step 170: visit route commerce-protection (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: organization-settings:organizations,organization-settings:organization:settings,customer-privacy,setting:legal,settings) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/general | "My Store · General · Shopify" | 2026-10-05T02:57:24.932Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.html`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt`
- quote: Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER)
- in context: … Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com General General Business details Business entity used for financial products, markets, apps, and taxes in this shop My Store - entity Yemen Store contact details My Store 7amza.it@gmail.com · No phone number Store address Sanaa, Yemen Submit Store defaults ⟪Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER)⟫ Backup Region Yemen [Yemen] Determines settings for customers outside of your markets Unit system Metric system [Metric system] Default weight unit Kilogram (kg) [Kilogram (kg)] Time zone (GMT+03:00) Riyadh [(GMT+03:00) Riyadh] Sets the time for when orders and analytics are recorded To change your user level time zone and language visit your account settings Order ID format Shown on the order page, customer pages, and customer order notificatio…

**Citation Q7-SH-C217:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt` | step 170, store contact details | 2026-10-05 | kind: observed | quote check: found
- step 170: visit route commerce-protection (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: organization-settings:organizations,organization-settings:organization:settings,customer-privacy,setting:legal,settings) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/general | "My Store · General · Shopify" | 2026-10-05T02:57:24.932Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.html`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt`
- quote: Store address Sanaa, Yemen
- in context: … Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com General General Business details Business entity used for financial products, markets, apps, and taxes in this shop My Store - entity Yemen Store contact details My Store 7amza.it@gmail.com · No phone number ⟪Store address Sanaa, Yemen⟫ Submit Store defaults Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER) Backup Region Yemen [Yemen] Determines settings for customers outside of your markets Unit system Metric system [Metric system] Default weight unit Kilogram (kg) [Kilogram (kg)] Time zone (GMT+03:00) Riyadh [(GMT+03:00) Riyadh] Sets the time for when orders and analytics are recorded To change your user level time zone and language visi…

### Q7-SH-079

**Cited at:** section 1, line 29; section 2, line 66

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-079
- bears_on: 2;3
- identifier: Currency for single-country markets
- statement: When you create a market for a single country, the market's currency is automatically set to that country's local currency. For example, creating a Japan market automatically sets the currency to JPY. You can change this to any supported currency.
- cite_ids: Q7-SH-C095
- from: held

**Citation Q7-SH-C095:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md` | Currency for single-country markets | 2026-10-16 | kind: stated | quote check: found
- quote: When you create a market for a single country, the market's currency is automatically set to that country's local currency. For example, creating a Japan market automatically sets the currency to JPY. You can change this to any supported currency.
- title: Setting up currencies for markets
- the page opens: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency. You can set a specific currency for each market so that your customers can browse, pay, and receive refunds in a currency that's familiar to them. Displaying prices in local currencies improves the customer experience and can help to increase conversion rates in international m…
- a note box: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency.
- a note box: Sidekick You can ask Sidekick which currency a market shows to buyers, whether local currencies and rounding are turned on, and whether its exchange rate is automatic or manual. Use a prompt such as What currency does each of my markets show buyers and are any using manual exchange rates.
- a note box: Caution When using manual exchange rates, you're responsible for keeping rates current. If your manual rate diverges significantly from the actual exchange rate, then you might experience inaccuracies on international orders. Review your manual rates regularly to ensure they reflect current market c
- headings: Setting up currencies for markets > Currency for single-country markets
- in context: …version fee is included in the price that's displayed to your customer. * Select **Manual** to set a fixed exchange rate. The conversion fee isn't added to prices displayed to your customer. Instead, the fee is reflected in your payouts. 6. Optional: Activate **Rounding** to adjust converted prices to standard price points. For example, $10.00 USD instead of $10.27 USD. 7. Click **Done**. 8. Click **Save**. ## Currency for single-country markets ⟪When you create a market for a single country, the market's currency is automatically set to that country's local currency. For example, creating a Japan market automatically sets the currency to JPY. You can change this to any supported currency.⟫ ## Currency for multi-country markets When you create a market with multiple countries, the default currency is set to your store's base currency, and local currencies are activated. This means each country in the market displays prices in its own local currency, automatically converted from the market's base currency. If you deactivate local currencies for a multi-country market, then prices in the market's base currency are displayed for all c…

### Q7-SH-202

**Cited at:** section 1, line 29

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-202
- bears_on: 2;3
- identifier: Markets > Capture market: Add currency customization, Currency (Recommended; All currencies)
- statement: [label: Currency] Saudi Riyal (SAR) [label: Recommended] Saudi Riyal (SAR) [label: All currencies]
- scope: store demo-fake-dev-store, market Capture market (Includes Saudi Arabia), observed 2026-09-30
- cite_ids: Q7-SH-C230
- from: held
- note: In the saved HTML of step 21 (admin.shopify.com/store/demo-fake-dev-store/markets/53126234247): what the markup held, not what the page showed or that the menu was open. The step's aria.yaml shows Currency and Saudi Riyal (SAR) and that the market includes Saudi Arabia, not the Recommended or All currencies labels.

**Citation Q7-SH-C230:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/021.html.txt` | run 20260930T170204Z-journey-market, step 21, Add currency customization, line 211 | 2026-09-30 | kind: observed | quote check: found
- step 21: currency SAR | https://admin.shopify.com/store/demo-fake-dev-store/markets/53126234247 | "demo fake dev store · Markets · Capture market · Shopify" | 2026-09-30T17:10:12.658Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/021.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/021.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/021.html.txt`
- quote: [label: Currency] Saudi Riyal (SAR) [label: Recommended] Saudi Riyal (SAR) [label: All currencies]
- in context: …ccessibilitylabel: Memory settings] Memory [accessibilitylabel: Memory] Allow Sidekick to update and access preferences you've shared. [accessibilitylabel: Expand] [accessibilitylabel: Close Sidekick] Where should we begin? Work with Sidekick Work with Sidekick [heading: Manage Subfolders] Done Cancel [label: Domain Suffix] [details: Example: eu for European Union.] Language URL actions English Default demo-fake-dev-store.myshopify.com/en- Adapt ⟪[label: Currency] Saudi Riyal (SAR) [label: Recommended] Saudi Riyal (SAR) [label: All currencies]⟫ Let customers pay in their region's currency. Use local currencies Afghan Afghani (AFN ؋) Albanian Lek (ALL) Algerian Dinar (DZD) Angolan Kwanza (AOA Kz) Argentine Peso (ARS $) Armenian Dram (AMD ֏) Aruban Florin (AWG) Australian Dollar (AUD $) Azerbaijani Manat (AZN ₼) Bahamian Dollar (BSD $) Bangladeshi Taka (BDT ৳) Barbadian Dollar (BBD $) Belize Dollar (BZD $) Bermudan Dollar (BMD $) Bolivian Boliviano (BOB Bs) Bosnia-Herzegovina Convertible…

### Q7-SH-203

**Cited at:** section 1, line 29

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-203
- bears_on: 2;3
- identifier: Markets > Capture market: Add currency customization, Currency, All currencies (item Store currency)
- statement: Store currency Yemeni Rial (YER)
- scope: store demo-fake-dev-store, market Capture market, observed 2026-09-30
- cite_ids: Q7-SH-C231
- from: held
- note: In the saved HTML of step 21: one item of the All currencies list, which holds 129 items (127 on line 213, then Yemeni Rial (YER) under Store currency and Zambian Kwacha (ZMW ZK)); not what the page showed or that the menu was open. The step's aria.yaml does not show this list.

**Citation Q7-SH-C231:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/021.html.txt` | run 20260930T170204Z-journey-market, step 21, Add currency customization, All currencies, lines 214-215 | 2026-09-30 | kind: observed | quote check: found
- step 21: currency SAR | https://admin.shopify.com/store/demo-fake-dev-store/markets/53126234247 | "demo fake dev store · Markets · Capture market · Shopify" | 2026-09-30T17:10:12.658Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/021.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/021.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/021.html.txt`
- quote: Store currency Yemeni Rial (YER)
- in context: …e Dollar (SRD $) Swazi Lilangeni (SZL) Swedish Krona (SEK kr) Swiss Franc (CHF) Tajikistani Somoni (TJS) Tanzanian Shilling (TZS) Thai Baht (THB ฿) Tongan Paʻanga (TOP T$) Trinidad & Tobago Dollar (TTD $) Turkish Lira (TRY ₺) Ugandan Shilling (UGX) Ukrainian Hryvnia (UAH ₴) United Arab Emirates Dirham (AED) Uruguayan Peso (UYU $) US Dollar (USD $) Uzbekistani Som (UZS) Vanuatu Vatu (VUV) Vietnamese Dong (VND ₫) West African CFA Franc (XOF F CFA) ⟪Store currency Yemeni Rial (YER)⟫ Zambian Kwacha (ZMW ZK) [label: Price rounding] Round up to the nearest SAR 1.00 Do not round prices [label: Exchange rate (FX)] Dynamic Manual 1 YER = 0.0024448788 SAR Updated: 4 minutes ago Product pricing will include a 2% conversion rate fee paid by customers. Exchange rates are determined at the time of purchases and refunds. Learn more Cancel Done

### Q7-SH-201

**Cited at:** section 1, line 29

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-201
- bears_on: 1;2
- identifier: Drafts > Create order: Markets, Currency (Market currency; Other currencies)
- statement: Yemen [label: Currency] [label: Market currency] Yemeni Rial (YER) [label: Other currencies] Czech Koruna (CZK Kč) Danish Krone (DKK kr) Euro (EUR €) Hungarian Forint (HUF Ft) Polish Zloty (PLN zł) Romanian Leu (RON lei) Swedish Krona (SEK kr) US Dollar (USD $)
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q7-SH-C229
- from: held
- note: In the saved HTML of step 5 (draft order page, admin.shopify.com/store/demo-fake-dev-store/draft_orders/new): what the markup held, not what the page showed. The step's aria.yaml shows the market button Yemen and the YER amounts, not the Currency labels or the currencies listed.

**Citation Q7-SH-C229:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T014656Z-journey-order-lifecycle/005.html.txt` | run 20260930T014656Z-journey-order-lifecycle, step 5, heading Markets, lines 86-87 | 2026-09-30 | kind: observed | quote check: found
- step 5: add the selected variant | https://admin.shopify.com/store/demo-fake-dev-store/draft_orders/new | "demo fake dev store · Drafts · Create order · Shopify" | 2026-09-30T01:47:51.720Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/005.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/005.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T014656Z-journey-order-lifecycle/005.html.txt`
- quote: Yemen [label: Currency] [label: Market currency] Yemeni Rial (YER) [label: Other currencies] Czech Koruna (CZK Kč) Danish Krone (DKK kr) Euro (EUR €) Hungarian Forint (HUF Ft) Polish Zloty (PLN zł) Romanian Leu (RON lei) Swedish Krona (SEK kr) US Dollar (USD $)
- in context: …ate store [initials: Dd] [alt: Demo-name demo-last-name] Demo-name demo-last-name 7amza.it@gmail.com Log out Alerts View unread only Mark all as read [accessibilitylabel: Mark all as read] Alerts about your store and account will show here [heading: Create order] [heading: Notes] [accessibilitylabel: Add note] [heading: Customer] Search or create a customer [Search or create a customer] [heading: Markets] [accessibilitylabel: View markets graph] ⟪Yemen [label: Currency] [label: Market currency] Yemeni Rial (YER) [label: Other currencies] Czech Koruna (CZK Kč) Danish Krone (DKK kr) Euro (EUR €) Hungarian Forint (HUF Ft) Polish Zloty (PLN zł) Romanian Leu (RON lei) Swedish Krona (SEK kr) US Dollar (USD $)⟫ [heading: Tags] [accessibilitylabel: Manage tags] Find or create tags Drafts [heading: Products] [accessibilitylabel: Access more product actions] Reserve items Lock product pricing Custom item Product [alt: Top and bottom view of a snowboard. The top view shows abstract circles and lines in shades of teal. The bottom view shows abstract circles and lines in shades of purple and blue with the text "SHOPIFY" in a sans serif typeface on top.] The …

### Q7-SH-K1268

**Cited at:** section 1, line 31; section 2, line 77; section 5, line 124; section 7, line 150; section 8, line 159

**The same record as Q1-SH-K1268,** whose card is in `Q1-shopify-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Each entity has its own Shopify Payments account, payout currency, and bank account, so you need to complete this process for every entity that you want to activate.
- scope: 

### Q7-SH-012

**Cited at:** section 1, line 31; section 2, line 77; section 7, line 150; section 8, line 159

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-012
- bears_on: 2
- identifier: Domestic currency
- statement: Your domestic currency is determined by your Shopify Payments region and is the default currency for your payouts.
- cite_ids: Q7-SH-C023
- from: held

**Citation Q7-SH-C023:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/supported-payout-currencies.md` | Domestic vs. non-domestic currencies | 2026-10-16 | kind: stated | quote check: found
- quote: Your domestic currency is determined by your Shopify Payments region and is the default currency for your payouts.
- title: Supported payout currencies
- the page opens: Various payout currencies are available through Shopify Payments, depending on your store's location. The payout currencies available to you depend on which country or region your store is based in. Your domestic currency is determined by your store location, and additional non-domestic currencies might be available depending on your Shopify plan. Understanding your domestic currency helps you determine whether Multi-Currency Payout fees apply to your payouts. Domestic vs. non-domestic currencie…
- a note box: Note If your store is based in the United States, then USD is always your default payout currency and can't be changed to another currency. You can add bank accounts in other supported currencies such as AUD, CAD, EUR, and GBP to receive secondary payouts in those currencies, but your primary payout
- headings: Supported payout currencies
- in context: …or region your store is based in. Your domestic currency is determined by your store location, and additional non-domestic currencies might be available depending on your Shopify plan. Understanding your domestic currency helps you determine whether [Multi-Currency Payout fees](/manual/payments/shopify-payments/store-currency/payouts-in-multiple-currencies#multi-currency-payout-fees) apply to your payouts. ## Domestic vs. non-domestic currencies ⟪Your domestic currency is determined by your Shopify Payments region and is the default currency for your payouts.⟫ Understanding the difference between domestic and non-domestic currencies helps you determine which fees might apply to your payouts. <table> <caption>Difference between domestic and non-domestic currencies</caption> <thead> <tr> <th scope="col">Currency type</th> <th scope="col">Definition</th> <th scope="col">Multi-Currency Payout fee</th> </tr> </thead> <tbody> <tr> <td scope="row">Domestic currency</td> <td>The default currency based on your…

### Q7-SH-008

**Cited at:** section 1, line 35; section 2, line 81; section 3, line 100; section 3, line 102

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-008
- bears_on: 3
- identifier: Settings > General > Store defaults > Currency display > Change store currency
- statement: Only the store owner can change store currency. You can view and change your store currency from the **Store defaults** section of the [**General**](https://admin.shopify.com/settings/general) settings page.
- cite_ids: Q7-SH-C018;Q7-SH-C019
- from: held
- note: Copy Q7-SH-K1936, from the account-setup page, says to contact Shopify Support to change the store currency after the first sale.

**Citation Q7-SH-C018:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Changing your store currency {#changing-your-store-currency} | 2026-10-16 | kind: stated | quote check: found
- quote: Only the store owner can change store currency.
- title: Changing your store currency
- the page opens: You can change the default currency displayed on your store to customers, even if this is not your local currency. This allows you to cater to your largest customer segment or to target a market where you expect to make more sales. Changing your store currency can have legal implications and other impacts that you need to consider. Legal and tax considerations Before you change your store currency, you need to review any potential legal or tax implications involved with selling in a currency tha…
- a note box: Tip Your Shopify admin won't display a record of your product and discount prices in the previously assigned currency. Before changing your store currency, you can export your products to a CSV file to create a backup of your pricing list, and export your discounts codes to a CSV file to see an over
- headings: Changing your store currency > Changing your store currency {#changing-your-store-currency}
- in context: …ng your store's currency, then [contact the app developer](/manual/apps/getting-support) for clarification. [Apps built by Shopify](https://apps.shopify.com/collections/made-by-shopify) will continue to work with your new currency. ## Changing your store currency {#changing-your-store-currency} Your store currency is the currency that's used in your Shopify admin. It's the currency that you price your products in and that's used in your reports. ⟪Only the store owner can change store currency.⟫ You can view and change your store currency from the **Store defaults** section of the [**General**](https://admin.shopify.com/settings/general) settings page. Before you change your store currency, review the impact and legal considerations this action has on your store. #### Steps: 1. From your Shopify admin, go to **Settings** > [**General**](https://admin.shopify.com/settings/general). 2. In the **Store defaults** section, under **Currency d…

**Citation Q7-SH-C019:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Changing your store currency {#changing-your-store-currency} | 2026-10-16 | kind: stated | quote check: found
- quote: You can view and change your store currency from the **Store defaults** section of the [**General**](https://admin.shopify.com/settings/general) settings page.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Changing your store currency {#changing-your-store-currency}
- in context: …developer](/manual/apps/getting-support) for clarification. [Apps built by Shopify](https://apps.shopify.com/collections/made-by-shopify) will continue to work with your new currency. ## Changing your store currency {#changing-your-store-currency} Your store currency is the currency that's used in your Shopify admin. It's the currency that you price your products in and that's used in your reports. Only the store owner can change store currency. ⟪You can view and change your store currency from the **Store defaults** section of the [**General**](https://admin.shopify.com/settings/general) settings page.⟫ Before you change your store currency, review the impact and legal considerations this action has on your store. #### Steps: 1. From your Shopify admin, go to **Settings** > [**General**](https://admin.shopify.com/settings/general). 2. In the **Store defaults** section, under **Currency display**, click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="Horizontal menu" class="admin-icon" /…

### Q7-SH-181

**Cited at:** section 1, line 35; section 2, line 83

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-181
- bears_on: 3
- identifier: Settings > General > Store defaults > Change store currency, I understand the risk of changing the store currency
- statement: If you're changing your currency after your first order, then you also need to check I understand the risk of changing the store currency. You can also optionally select the reason for changing the currency.
- cite_ids: Q7-SH-C206
- from: held
- note: Copy Q7-SH-K1936 says to contact Shopify Support to change the store currency after the first sale.

**Citation Q7-SH-C206:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/setup-business-settings.md` | Select a store currency {#select-a-store-currency}, Steps (Desktop), step 4 | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: If you're changing your currency after your first order, then you also need to check I understand the risk of changing the store currency. You can also optionally select the reason for changing the currency.
- title: Adding business settings for your store
- the page opens: Before you start setting up your Shopify store, you need to create a Shopify account and add business information for your store. You don't need to include every detail right away, but be sure to add the following items: * Store name * Legal business name and address * Store time zone * Default store currency * Default weight unit * Password to protect your online store Review your myshopify.com domain name {#review-myshopify-domain} During account creation, you're assigned an automatically-gene…
- a note box: Caution If you opt to use a custom domain for your storefront, then make sure that you record and keep your original myshopify.com domain name somewhere safe. After you change your primary domain from myshopify.com to your custom domain, you still need to use your original myshopify.com domain name 
- a note box: Caution Changing your store name doesn't change your default myshopify.com domain name. Learn more about choosing a new myshopify.com domain name.
- a note box: Note Your legal business name is a separate setting in the Business details section. Editing your legal business name doesn't change the company name in your store address. Learn more about editing a business entity.
- headings: Adding business settings for your store > Select a store currency {#select-a-store-currency} > Steps:
- in context: …n, you can choose which currency your store uses (for example, USD, EUR, CAD, AUD, JPY). If you're using Shopify Payments as your credit card payment gateway, then you must change your currency by editing the bank account and currency settings used by Shopify Payments. Steps: Desktop From your Shopify admin, go to Settings > General. In the Store defaults section, click > Change store currency. Select a new monetary unit with the drop-down menu. ⟪If you're changing your currency after your first order, then you also need to check I understand the risk of changing the store currency. You can also optionally select the reason for changing the currency.⟫ Click Save. Optional: To change the way monetary amounts are displayed, complete the following steps: Click > Change currency formatting. Make changes to your currency formatting. Click Save. Mobile From the Shopify app, tap, and then tap Settings. In the Store settings section, tap General. In the Store defaults section, tap or > Change store currency. Select a new monetary unit with the drop-down menu. If you're changing your currency after yo…  (matched markup removed)

### Q7-SH-205

**Cited at:** section 1, line 35

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-205
- bears_on: 3
- identifier: Settings > General: Change store currency
- statement: [heading: Change store currency] Save Cancel [accessibilitylabel: Change store currency]
- scope: store capture-plus, observed 2026-10-02
- cite_ids: Q7-SH-C233
- from: held
- note: In the saved HTML of step 60 (admin.shopify.com/store/capture-plus/settings/general): a dialog heading the markup held, not a dialog the page showed open; the markup holds no currency list or other text under it. The step's aria.yaml shows neither these words nor the Store defaults section.

**Citation Q7-SH-C233:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 60, lines 188-191 | 2026-10-02 | kind: observed | quote check: found
- step 60: visit route inactive-account:checkout:select-plan (path from router) | https://admin.shopify.com/store/capture-plus/settings/general | "capture plus · General · Shopify" | 2026-10-02T01:04:39.293Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt`
- quote: [heading: Change store currency] Save Cancel [accessibilitylabel: Change store currency]
- in context: …lose You don't have permission to switch business details. Contact your store administrator to request changes. [heading: Confirm store address] Confirm store address Cancel When changing country, you'll receive multiple tax forms and may need to verify your business. This can also affect subscription fees, billing currency, and apps Store address must be in the same country as the business entity Updated store address [accessibilitylabel: Edit] ⟪[heading: Change store currency] Save Cancel [accessibilitylabel: Change store currency]⟫ [heading: Change currency formatting] Save Cancel Change how currencies are displayed on your store. {{amount}} and {{amount_no_decimals}} will be replaced with the price of your product. Submit [label: HTML with currency] [label: HTML without currency] [label: Email with currency] [label: Email without currency]

### Q7-SH-006

**Cited at:** section 1, line 37; section 1, line 38; section 2, line 82; section 2, line 83; section 5, line 125

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-006
- bears_on: 3
- identifier: Impact of changing store currency
- statement: * The currency of your product prices and discount rates update automatically, but not the amount. For example, if you change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD. * The amount and currency of shipping rates aren't updated automatically. * Gift cards with remaining balances in the old currency will no longer work. * Apps that have currency requirements different from the new currency won't work after the currency has been changed. * Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles. * Changing your store currency might affect orders with pending payments. * Refunds processed after a currency change will also be affected by the currency change due to the difference in values. * If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to match the new currency. * If you're using Paypal Express, then your new currency might not be supported. * Managed Markets is deactivated if you change your store currency. To continue using Managed Markets, your store currency must remain set to the required currency for your region.
- cite_ids: Q7-SH-C006;Q7-SH-C007;Q7-SH-C008;Q7-SH-C009;Q7-SH-C010;Q7-SH-C011;Q7-SH-C012;Q7-SH-C013;Q7-SH-C014;Q7-SH-C015;Q7-SH-C016
- from: held

**Citation Q7-SH-C006:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: Before you change your store currency, review the following impact of this change on your store:
- title: Changing your store currency
- the page opens: You can change the default currency displayed on your store to customers, even if this is not your local currency. This allows you to cater to your largest customer segment or to target a market where you expect to make more sales. Changing your store currency can have legal implications and other impacts that you need to consider. Legal and tax considerations Before you change your store currency, you need to review any potential legal or tax implications involved with selling in a currency tha…
- a note box: Tip Your Shopify admin won't display a record of your product and discount prices in the previously assigned currency. Before changing your store currency, you can export your products to a CSV file to create a backup of your pricing list, and export your discounts codes to a CSV file to see an over
- headings: Changing your store currency > Legal and tax considerations
- in context: …accountant to make sure changing your currency doesn't require any changes to the taxes you have set up. Check with a legal expert to verify there are no legal implications when changing your store currency. ## Impact of changing store currency ⟪Before you change your store currency, review the following impact of this change on your store:⟫ * The currency of your product prices and discount rates update automatically, but not the amount. For example, if you change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD. * The amount and currency of shippi…

**Citation Q7-SH-C007:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * The currency of your product prices and discount rates update automatically, but not the amount. For example, if you change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …set up. Check with a legal expert to verify there are no legal implications when changing your store currency. ## Impact of changing store currency Before you change your store currency, review the following impact of this change on your store: ⟪* The currency of your product prices and discount rates update automatically, but not the amount. For example, if you change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD.⟫ * The amount and currency of shipping rates aren't updated automatically. * Gift cards with remaining balances in the old currency will no longer work. * Apps that have currency requirements different from the new currency won't work after the …

**Citation Q7-SH-C008:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * The amount and currency of shipping rates aren't updated automatically.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …mpact of this change on your store: * The currency of your product prices and discount rates update automatically, but not the amount. For example, if you change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD. ⟪* The amount and currency of shipping rates aren't updated automatically.⟫ * Gift cards with remaining balances in the old currency will no longer work. * Apps that have currency requirements different from the new currency won't work after the currency has been changed. * Changing your store currency might affect you…

**Citation Q7-SH-C009:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * Gift cards with remaining balances in the old currency will no longer work.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …and discount rates update automatically, but not the amount. For example, if you change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD. * The amount and currency of shipping rates aren't updated automatically. ⟪* Gift cards with remaining balances in the old currency will no longer work.⟫ * Apps that have currency requirements different from the new currency won't work after the currency has been changed. * Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles. * C…

**Citation Q7-SH-C010:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * Apps that have currency requirements different from the new currency won't work after the currency has been changed.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …ou change from USD to CAD, then a product that was listed as 20 USD is now listed as 20 CAD. * The amount and currency of shipping rates aren't updated automatically. * Gift cards with remaining balances in the old currency will no longer work. ⟪* Apps that have currency requirements different from the new currency won't work after the currency has been changed.⟫ * Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles. * Changing your store currency might affect orders with pending payments. * Refunds processed after a currency change will…

**Citation Q7-SH-C011:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …of shipping rates aren't updated automatically. * Gift cards with remaining balances in the old currency will no longer work. * Apps that have currency requirements different from the new currency won't work after the currency has been changed. ⟪* Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles.⟫ * Changing your store currency might affect orders with pending payments. * Refunds processed after a currency change will also be affected by the currency change due to the difference in values. * If you use a payment provider other than Shopi…

**Citation Q7-SH-C012:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * Changing your store currency might affect orders with pending payments.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …rk. * Apps that have currency requirements different from the new currency won't work after the currency has been changed. * Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles. ⟪* Changing your store currency might affect orders with pending payments.⟫ * Refunds processed after a currency change will also be affected by the currency change due to the difference in values. * If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to mat…

**Citation Q7-SH-C013:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * Refunds processed after a currency change will also be affected by the currency change due to the difference in values.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: … won't work after the currency has been changed. * Changing your store currency might affect your reports, due to currency rate fluctuations and the report update cycles. * Changing your store currency might affect orders with pending payments. ⟪* Refunds processed after a currency change will also be affected by the currency change due to the difference in values.⟫ * If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to match the new currency. * If you're using Paypal Express, then your new currency might not be supported. * Managed Markets is…

**Citation Q7-SH-C014:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to match the new currency.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: … rate fluctuations and the report update cycles. * Changing your store currency might affect orders with pending payments. * Refunds processed after a currency change will also be affected by the currency change due to the difference in values. ⟪* If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to match the new currency.⟫ * If you're using Paypal Express, then your new currency might not be supported. * Managed Markets is deactivated if you change your store currency. To continue using Managed Markets, your store currency must remain set to the required currency…

**Citation Q7-SH-C015:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * If you're using Paypal Express, then your new currency might not be supported.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …after a currency change will also be affected by the currency change due to the difference in values. * If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to match the new currency. ⟪* If you're using Paypal Express, then your new currency might not be supported.⟫ * Managed Markets is deactivated if you change your store currency. To continue using Managed Markets, your store currency must remain set to the required currency for your region. <aside class="note note-information"><h4>Tip</h4><p>Your Shopif…

**Citation Q7-SH-C016:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/store-currency/changing-your-store-currency.md` | Impact of changing store currency | 2026-10-16 | kind: stated | quote check: found
- quote: * Managed Markets is deactivated if you change your store currency. To continue using Managed Markets, your store currency must remain set to the required currency for your region.
- title, opening and note boxes: as for this source's citation above
- headings: Changing your store currency > Impact of changing store currency
- in context: …ifference in values. * If you use a payment provider other than Shopify Payments, then the currencies of all of your markets will update to match the new currency. * If you're using Paypal Express, then your new currency might not be supported. ⟪* Managed Markets is deactivated if you change your store currency. To continue using Managed Markets, your store currency must remain set to the required currency for your region.⟫ <aside class="note note-information"><h4>Tip</h4><p>Your Shopify admin won't display a record of your product and discount prices in the previously assigned currency. Before changing your store currency, you can <a href="/en/manual/products/imp…

### Q7-SH-078

**Cited at:** section 1, line 42; section 2, line 74; section 3, line 91; section 3, line 95

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-078
- bears_on: 2;3
- identifier: Markets > Currency > Dynamic / Manual
- statement: * Select **Dynamic** to automatically convert prices. Prices are converted using the current market exchange rate, updated regularly. The currency conversion fee is included in the price that's displayed to your customer. * Select **Manual** to set a fixed exchange rate. The conversion fee isn't added to prices displayed to your customer. Instead, the fee is reflected in your payouts.
- cite_ids: Q7-SH-C093;Q7-SH-C094
- from: held

**Citation Q7-SH-C093:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md` | Add a currency customization to a market, step 5 | 2026-10-16 | kind: stated | quote check: found
- quote: * Select **Dynamic** to automatically convert prices. Prices are converted using the current market exchange rate, updated regularly. The currency conversion fee is included in the price that's displayed to your customer.
- title: Setting up currencies for markets
- the page opens: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency. You can set a specific currency for each market so that your customers can browse, pay, and receive refunds in a currency that's familiar to them. Displaying prices in local currencies improves the customer experience and can help to increase conversion rates in international m…
- a note box: Note To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor. If you use a different provider, then customers in all markets pay in your store's default currency.
- a note box: Sidekick You can ask Sidekick which currency a market shows to buyers, whether local currencies and rounding are turned on, and whether its exchange rate is automatic or manual. Use a prompt such as What currency does each of my markets show buyers and are any using manual exchange rates.
- a note box: Caution When using manual exchange rates, you're responsible for keeping rates current. If your manual rate diverges significantly from the actual exchange rate, then you might experience inaccuracies on international orders. Review your manual rates regularly to ensure they reflect current market c
- headings: Setting up currencies for markets > Add a currency customization to a market
- in context: …ide> ## Add a currency customization to a market 1. From your Shopify admin, go to [**Markets**](https://admin.shopify.com/markets). 2. Click the market that you want to customize. 3. Click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg" alt="Plus Circle Icon" class="admin-icon" /> next to **Currency**. 4. Select the currency you want to use for this market. 5. Select your exchange rate settings: ⟪* Select **Dynamic** to automatically convert prices. Prices are converted using the current market exchange rate, updated regularly. The currency conversion fee is included in the price that's displayed to your customer.⟫ * Select **Manual** to set a fixed exchange rate. The conversion fee isn't added to prices displayed to your customer. Instead, the fee is reflected in your payouts. 6. Optional: Activate **Rounding** to adjust converted prices to standard price points. For example, $10.00 USD instead of $10.27 USD. 7. Click **Done**. 8. Click **Save**. ## Currency for single-country markets When you create a market for a single country, the market's currency is…

**Citation Q7-SH-C094:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md` | Add a currency customization to a market, step 5 | 2026-10-16 | kind: stated | quote check: found
- quote: * Select **Manual** to set a fixed exchange rate. The conversion fee isn't added to prices displayed to your customer. Instead, the fee is reflected in your payouts.
- title, opening and note boxes: as for this source's citation above
- headings: Setting up currencies for markets > Add a currency customization to a market
- in context: …m/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg" alt="Plus Circle Icon" class="admin-icon" /> next to **Currency**. 4. Select the currency you want to use for this market. 5. Select your exchange rate settings: * Select **Dynamic** to automatically convert prices. Prices are converted using the current market exchange rate, updated regularly. The currency conversion fee is included in the price that's displayed to your customer. ⟪* Select **Manual** to set a fixed exchange rate. The conversion fee isn't added to prices displayed to your customer. Instead, the fee is reflected in your payouts.⟫ 6. Optional: Activate **Rounding** to adjust converted prices to standard price points. For example, $10.00 USD instead of $10.27 USD. 7. Click **Done**. 8. Click **Save**. ## Currency for single-country markets When you create a market for a single country, the market's currency is automatically set to that country's local currency. For example, creating a Japan market automatically sets the currency to JPY. You can change this to any supported…

### Q7-SH-204

**Cited at:** section 1, line 42; section 2, line 75

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-204
- bears_on: 2;3
- identifier: Markets > Capture market: Add currency customization, Price rounding; Exchange rate (FX)
- statement: [label: Price rounding] Round up to the nearest SAR 1.00 Do not round prices [label: Exchange rate (FX)] Dynamic Manual 1 YER = 0.0024448788 SAR Updated: 4 minutes ago
- scope: store demo-fake-dev-store, market Capture market, observed 2026-09-30
- cite_ids: Q7-SH-C232
- from: held
- note: In the saved HTML of step 21: the options as the markup held them, not which one the page showed selected. The step's aria.yaml shows 1 YER = 0.0024448788 SAR and Updated: 4 minutes ago, not the Price rounding or Exchange rate (FX) labels or their options.

**Citation Q7-SH-C232:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T170204Z-journey-market/021.html.txt` | run 20260930T170204Z-journey-market, step 21, Add currency customization, lines 216-218 | 2026-09-30 | kind: observed | quote check: found
- step 21: currency SAR | https://admin.shopify.com/store/demo-fake-dev-store/markets/53126234247 | "demo fake dev store · Markets · Capture market · Shopify" | 2026-09-30T17:10:12.658Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/021.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T170204Z-journey-market/steps/021.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T170204Z-journey-market/021.html.txt`
- quote: [label: Price rounding] Round up to the nearest SAR 1.00 Do not round prices [label: Exchange rate (FX)] Dynamic Manual 1 YER = 0.0024448788 SAR Updated: 4 minutes ago
- in context: … kr) Swiss Franc (CHF) Tajikistani Somoni (TJS) Tanzanian Shilling (TZS) Thai Baht (THB ฿) Tongan Paʻanga (TOP T$) Trinidad & Tobago Dollar (TTD $) Turkish Lira (TRY ₺) Ugandan Shilling (UGX) Ukrainian Hryvnia (UAH ₴) United Arab Emirates Dirham (AED) Uruguayan Peso (UYU $) US Dollar (USD $) Uzbekistani Som (UZS) Vanuatu Vatu (VUV) Vietnamese Dong (VND ₫) West African CFA Franc (XOF F CFA) Store currency Yemeni Rial (YER) Zambian Kwacha (ZMW ZK) ⟪[label: Price rounding] Round up to the nearest SAR 1.00 Do not round prices [label: Exchange rate (FX)] Dynamic Manual 1 YER = 0.0024448788 SAR Updated: 4 minutes ago⟫ Product pricing will include a 2% conversion rate fee paid by customers. Exchange rates are determined at the time of purchases and refunds. Learn more Cancel Done

### Q7-SH-068

**Cited at:** section 1, line 43; section 2, line 72

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-068
- bears_on: 1;3
- identifier: Refunds
- statement: Refunds are always issued to a customer in the currency that they used to pay for the order.
- cite_ids: Q7-SH-C083
- from: held

**Citation Q7-SH-C083:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/international/pricing/refunds.md` | Refunds | 2026-10-16 | kind: stated | quote check: found
- quote: Refunds are always issued to a customer in the currency that they used to pay for the order.
- title: Refunds
- the page opens: Refunds are always issued to a customer in the currency that they used to pay for the order. When you issue refunds, the following rules apply: * Refunds use the same payment method that was used to pay for the order. You can't issue a refund to a different card or bank account. * Refunds are issued in the same currency that the customer used to pay for the order. If the customer paid in Euros, then they receive a refund in Euros. * If the currency needs to be converted for the refund, then the …
- headings: Refunds
- in context: # Refunds ⟪Refunds are always issued to a customer in the currency that they used to pay for the order.⟫ When you issue refunds, the following rules apply: * Refunds use the same payment method that was used to pay for the order. You can't issue a refund to a different card or bank account. * Refunds are issued in the same currency that the customer used to pay for the order. If the customer paid in Euros, then they receive a refund in Euros. * If the currency needs to be converted for the refund, then the current currency rate, and not the currenc…

### Q7-SH-107

**Cited at:** section 1, line 44; section 2, line 58; section 2, line 82; section 3, line 101

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-107
- bears_on: 2;3
- identifier: Changes to Markets currency customizations with Bulgarian Lev
- statement: If you use Shopify Payments, then your markets were previously configured to display and charge customers in Bulgarian Lev. This configuration has been changed to display and charge customers in Euros on your behalf.
- scope: Bulgarian Lev (BGN)
- cite_ids: Q7-SH-C131
- from: held

**Citation Q7-SH-C131:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/bulgaria-currency-transition.md` | Changes to Markets currency customizations with Bulgarian Lev | 2026-10-16 | kind: stated | quote check: found
- quote: If you use Shopify Payments, then your markets were previously configured to display and charge customers in Bulgarian Lev. This configuration has been changed to display and charge customers in Euros on your behalf.
- title: Bulgaria currency change in Markets
- the page opens: Bulgaria completed their changeover plan to transition from using the Bulgarian Lev (BGN) to the Euro (EUR) for electronic transactions on January 1, 2026. Use this page to find out everything you need to know about the change inside Shopify. Changes to Markets currency customizations with Bulgarian Lev If you use Shopify Payments, then your markets were previously configured to display and charge customers in Bulgarian Lev. This configuration has been changed to display and charge customers in …
- a note box: Note Fixed price discounts only exist in your store default currency. When you change your store default currency to Euros, check your fixed price discounts and adjust them accordingly.
- headings: Bulgaria currency change in Markets > Changes to Markets currency customizations with Bulgarian Lev
- in context: # Bulgaria currency change in Markets Bulgaria completed their changeover plan to transition from using the Bulgarian Lev (BGN) to the Euro (EUR) for electronic transactions on January 1, 2026. Use this page to find out everything you need to know about the change inside Shopify. ## Changes to Markets currency customizations with Bulgarian Lev ⟪If you use Shopify Payments, then your markets were previously configured to display and charge customers in Bulgarian Lev. This configuration has been changed to display and charge customers in Euros on your behalf.⟫ No other aspects of your customer experience have been changed. ## Changes to store default currency and pricing with Bulgarian Lev Your store's default currency and product pricing aren't changed. If your store default currency is set to use Bulgarian Lev and you use Shopify Payments, then your product prices are now converted to Euros for customers to buy in. It's recommended that you update your product pricing and store default currency to E…

### Q7-SH-K1600

**Cited at:** section 1, line 48; section 3, line 90; section 5, line 126; section 7, line 152

**Record** (`studies/proposals/records/Q7/shopify/copied.tsv`):
- concern_id: SH-C-065
- placement: responsible
- structure: https://help.shopify.com/en/manual/international/managed-markets/overview.md
- identifier: Flow of funds
- statement: After an international Managed Markets order is placed in your store, Shopify Payments processes the transaction and holds the money in a Global-e account.
- scope: international Managed Markets orders
- cite_ids: SH-S-0565
- note: first run's citation

**Citation SH-S-0565:** `https://help.shopify.com/en/manual/international/managed-markets/overview.md` | Flow of funds | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/035-help.shopify.com/text.txt` (13523 bytes), fetched 2026-10-11T06:12:59Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/028-help.shopify.com/text.txt` (13523 bytes), fetched 2026-10-12T10:50:06Z, captured
- quote: After an international Managed Markets order is placed in your store, Shopify Payments processes the transaction and holds the money in a Global-e account.
- title: Overview of Managed Markets
- the page opens: You can use Managed Markets to sell to customers in other countries without registering a business, registering for tax, or arranging customs clearance in each destination. Your customers buy from your store, in your brand's checkout, and pay in their own currency. Their order arrives without a surprise bill at the door. Managed Markets builds on Shopify Markets, the tools built into every store for selling in other countries, including localized domains and store translation. With Shopify Marke…
- headings: Overview of Managed Markets > Merchant of record {#merchant-of-record} > Flow of funds {#flow-of-funds}
- in context: …ains unchanged. The disclaimer is a required part of the merchant of record arrangement. You can't hide or reword it, and no setting in your Shopify admin or your theme turns it off. The only way to remove it for a market is to [deactivate Managed Markets](/manual/international/managed-markets/deactivation) for that market and act as your own merchant of record. ### Flow of funds {#flow-of-funds} Managed Markets features are powered by Global-e. ⟪After an international Managed Markets order is placed in your store, Shopify Payments processes the transaction and holds the money in a Global-e account.⟫ When Global-e goes across the border, they act as your merchant of record. Global-e holds the funds to remit the costs to proper authorities that are involved in the cross-border commerce transaction. ## Pricing {#pricing} Managed Markets has the following fees for international orders: * A transaction fee: * 3.25% for stores on the Shopify Plus plan. * 3.5% for stores that are on the Basic, Grow, or Advanced plan. * A [currency conversion fee](…

### Q7-SH-131

**Cited at:** section 1, line 48; section 1, line 53; section 2, line 78; section 8, line 159

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-131
- bears_on: 4
- identifier: ShopifyPaymentsAccount
- statement: Financial account information for merchants using Shopify Payments. Tracks current balances across all supported currencies, payout schedules, and
- scope: GraphQL Admin API 2026-10
- cite_ids: Q7-SH-C156
- from: held

**Citation Q7-SH-C156:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/admin-graphql-schema/2026-10/items.jsonl` | line 3193 (type ShopifyPaymentsAccount, description) | 2026-09-30 | kind: stated | quote check: found
- quote: Financial account information for merchants using Shopify Payments. Tracks current balances across all supported currencies, payout schedules, and
- in context: ShopifyPaymentsAccount OBJECT ⟪Financial account information for merchants using Shopify Payments. Tracks current balances across all supported currencies, payout schedules, and⟫ [`ShopifyPaymentsBalanceTransaction`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ShopifyPaymentsBalanceTransaction) records. accountOpenerName String activated Boolean! balance [MoneyV2!]! balanceTransactions ShopifyPaymentsBalanceTransactionConnection! hideTransfers Boolean first Int after String last Int before String reverse Boolean sortKey BalanceTransactionSortKeys query String savedSearchId ID bankAccounts ShopifyPaymentsBan…

### Q7-SH-099

**Cited at:** section 3, line 88

**Record** (`studies/proposals/records/Q7/shopify/statements.tsv`):
- stmt_id: Q7-SH-099
- bears_on: 1
- identifier: Shopify Payments support for local pricing, row Others
- statement: Others Unsupported and prices convert to shop currency
- scope: Shopify Payments
- cite_ids: Q7-SH-C120
- from: held

**Citation Q7-SH-C120:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/international/pricing/primary-gateway-support.md` | table "Payment methods for Shopify Payments" (Payment category, Payment method, Support), row Others | 2026-10-16 | kind: stated | quote check: found (markup removed)
- quote: Others Unsupported and prices convert to shop currency
- title: Primary gateways for international and local pricing support
- the page opens: On this page you can find a breakdown of payment methods supporting local pricing within Shopify Payments, as well as details on Adyen's integration with international sales tools for currency processing. Shopify Payments support for local pricing The following table lists the payment methods for Shopify Payments and their level of support for local pricing. Payment methods for Shopify Payments Payment category Payment method Support Credit card Credit card checkout Fully supported Accelerated c…
- in context: …ckout Fully supported Accelerated checkout Shop Pay Fully supported Apple Pay Supported but without checkout restrictions Google Pay Supported but without checkout restrictions Amazon Pay Unsupported and prices convert to shop currency Local payment methods Klarna Fully supported iDEAL Wero Fully supported EPS Payments Fully supported Bancontact Fully supported Additional payment methods PayPal Express Supported but without checkout restrictions ⟪Others Unsupported and prices convert to shop currency⟫ Adyen's compatibility with international sales tools Adyen is a third-party payment gateway available for enterprise-level businesses. It can be used with international sales tools to sell in local currencies. Transactions are processed in the currency sent by Shopify to Adyen when international sales tools are activated. You need to configure the currencies of your markets within Adyen. If the currency matches one of Adyen's settlement currenci…  (matched markup removed)

### Q7-SH-P0010

**Cited at:** section 7, line 153

**The same record as Q5-SH-P0010,** whose card is in `Q5-shopify-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: By accepting this Agreement and the Payment Processor Terms for your Designated Country you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors for Payment Processing (each a "Payment Processor Account").
- scope: 
