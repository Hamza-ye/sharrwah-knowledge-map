# Cards: Q7 on woocommerce

14 records cited by `studies/proposals/drafts/Q7/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Prices held: Shopify, Zid, WooCommerce and BigCommerce hold a seller's own prices in one currency per store, and match on role (basis 4). Shopify's store currency is the one "for pricing products and running reports"; Zid's العملة الأساسية is "العملة التي تم إدخال أسعار المنتجات باستخدامها"; WooCommerce allows "one base currency per store", and "WooCommerce uses it to display product prices and record new orders"; BigCommerce's default currency is "assigned during store creation, is always a transactional currency". Salla's seller sets the store's current currency, but the words read don't say prices are entered in it, so Salla's match is partial. Q7-SH-K1935 Q7-ZD-002 Q7-WC-K0745 Q7-WC-K0747 Q7-BC-013 Q7-SA-001
- **section 1, line 9:** - Amounts: Zid passes an amount to payment providers "in the smallest currency unit"; Shopify's MoneyBag carries `shopMoney` and `presentmentMoney` side by side; WooCommerce's shipped code records an order's currency "in ISO format". Not checked on Salla, for Zid's amount unit (Q7-ZD-024). Q7-ZD-024 Q7-SH-123 Q7-WC-055
- **section 1, line 10:** - Shown to buyers: Shopify and Zid set the shown currency per market, and match on role (basis 4). Shopify's currency customization "determines what currency is displayed to customers in that market"; Zid's عملة السوق is the currency "لعرض أسعار المنتجات داخل هذا السوق". WooCommerce keeps one list for the whole store, its "Enabled currencies". Q7-SH-076 Q7-ZD-K0236 Q7-WC-013
- **section 1, line 12:** - Paid by buyers: on Shopify, BigCommerce, WooCommerce and Salla the currency shown and the currency charged can differ, and what the payment provider supports decides the charge; they match on role (basis 4). Zid's pages aren't reconciled (below): Q7-SH-K1938 Q7-BC-014 Q7-WC-029 Q7-SA-K1963
- **section 1, line 15:** - WooCommerce: the Currency Converter Widget "changes the display of prices only", and the store's base currency is still charged. Q7-WC-029
- **section 1, line 18:** - Each order records its currency, and four record the store's currency or a rate beside it, matching on role (basis 4): Shopify's order has `presentmentCurrencyCode`, and its MoneyBag holds both amounts; Zid's order gives the "Exchange rate of the store currency relative to the order currency"; BigCommerce's has `currency_code`, `default_currency_code` and `currency_exchange_rate`; Salla's an `exchange_rate` with `base_currency`, `exchange_currency` and `rate`; WooCommerce's a single "Currency the order was created with, in ISO format." (shipped code; the others stated). Q7-SH-124 Q7-SH-123 Q7-ZD-010 Q7-BC-020 Q7-SA-016 Q7-WC-055
- **section 1, line 19:** - Paid out: Shopify and WooCommerce use the same term, "payout currency" (basis 1), with the same definition (basis 3): Shopify's is "the currency that Shopify Payments uses to deposit money into your bank account", WooCommerce's "the currency in which funds are paid out into your bank account" (stated). On store fake-demo-sharrwah (30 September 2026, observed), a report page's saved markup hid a metric, "Payout amount in payout currency": "Value of the payout, in the currency the payout was issued in". Q7-SH-004 Q7-WC-004 Q7-SH-206
- **section 1, line 20:** - The currency paid out can differ from the one paid, and the provider converts: Shopify applies a rate and fee "at the time of payment capture"; WooCommerce converts a payment matching none of the seller's bank accounts "into your default currency and paid out into the default account"; on BigCommerce "the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope" (stated). On store fake-demo-sharrwah (30 September 2026, observed), a report page's saved markup also hid a metric, "Foreign exchange fees": "Currency conversion fees you pay when customers purchase in a different currency". Q7-SH-013 Q7-WC-K0737 Q7-BC-P0015 Q7-SH-207
- **section 1, line 27:** - A store's own currency is set for the store, by the seller, with a default from the store's country; Zid, WooCommerce and BigCommerce match on role (basis 4). Zid asks for it "بناء على عملة دولتك"; WooCommerce's onboarding sets `woocommerce_currency` from the country's `currency_code` (shipped code); BigCommerce's default currency "is assigned based on your location" (stated). Q7-ZD-001 Q7-WC-054 Q7-BC-029
- **section 1, line 31:** - The currency paid out is set for the payment account, by its region, entity, country or provider. Shopify's "domestic currency is determined by your Shopify Payments region and is the default currency for your payouts", and each business entity has "its own Shopify Payments account, payout currency, and bank account" (not checked on Salla, Q7-SH-K1268); where WooCommerce's chart lists one currency for a country, "those payouts can only be sent to banks in your country"; BigCommerce's merchant sets it "through its payment provider". Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-BC-P0016
- **section 1, line 41:** - What is already recorded: WooCommerce's "Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same." Zid's help says instead "سيتم تحويل المبيعات إلى العملة الجديدة بناءً على سعر الصرف في تلك اللحظة", so total sales may change. Q7-WC-027 Q7-ZD-003
- **section 1, line 42:** - Rates are automatic or fixed by the seller. Shopify's markets choose Dynamic, "to automatically convert prices", or Manual, "to set a fixed exchange rate" (not checked on Salla, Q7-SH-078); WooCommerce's rates come by default from "the WooPayments server"; BigCommerce's merchant can use its Currency Service or "use the API to automatically update the exchange rate from their trusted source" (stated). On store demo-fake-dev-store (30 September 2026, observed), a market's saved markup held "Exchange rate (FX)" with Dynamic, Manual and "1 YER = 0.0024448788 SAR", and "Price rounding" with "Round up to the nearest SAR 1.00" and "Do not round prices". Q7-SH-078 Q7-WC-K0755 Q7-BC-035 Q7-SH-204
- **section 1, line 43:** - Refunds go in the currency paid, and match on role (basis 4): on Shopify "in the currency that they used to pay for the order"; on WooCommerce the balance is debited "using the exchange rate at the time you issued the refund". Q7-SH-068 Q7-WC-019
- **section 1, line 44:** - The platforms change currencies themselves: on stores using Shopify Payments, Shopify changed markets that charged in Bulgarian Lev "to display and charge customers in Euros on your behalf" (not checked on Salla or BigCommerce, Q7-SH-107); one of WooCommerce's upgrade routines rewrote recorded orders' `_order_currency` from KIP to LAK (shipped). Q7-SH-107 Q7-WC-057
- **section 1, line 49:** - WooCommerce: with bank accounts in several currencies, the seller can "view your balance in each currency". Q7-WC-048
- **section 1, line 53:** - Shopify, WooCommerce and BigCommerce keep the seller's balance per currency, and match on role (basis 4): "across all supported currencies", "in each currency", "per currency" (stated). Q7-SH-131 Q7-WC-048 Q7-BC-058
- **section 2, line 57:** - **Currency table**. Proposed: each currency Sharrwah supports is a row of data, with its code, the size of its smallest unit and its symbol; a currency is added, renamed or retired by changing rows, not code. Q7-ZD-024 Q7-WC-055
- **section 2, line 58:** - From the platforms: Zid's smallest unit and WooCommerce's ISO codes. Why: rule 3, as codes and units sit in every stored amount; and rule 2, as currencies change, like Shopify's Bulgarian markets moving to the euro, or WooCommerce rewriting KIP to LAK. Q7-SH-107 Q7-WC-057
- **section 2, line 61:** - **Store currency**. Proposed: each store has exactly one, in which the seller's prices are entered and reports run. The seller picks it when creating the store, from those its place allows, with the place's default preselected. Q7-WC-K0745 Q7-SH-K1935 Q7-ZD-001
- **section 2, line 62:** - From the platforms: one currency per store for a seller's prices (Shopify, Zid, WooCommerce, BigCommerce), with a default from the store's country (Zid, WooCommerce, BigCommerce). Why: rule 1, as the default and choices come from **place currency settings**, not a build per place; and rule 3, as each **order currency record** converts to it. Q7-ZD-002 Q7-BC-013 Q7-WC-054 Q7-BC-029
- **section 2, line 63:** - **Place currency settings**. Proposed: for each place it serves, Sharrwah sets a default currency and the currencies a store there may price in, show, charge in and be paid out in; the last two are also bounded by the **provider currency capability** of the providers connected there. Q7-ZD-001 Q7-WC-054
- **section 2, line 64:** - From the platforms: country defaults (Zid, WooCommerce, BigCommerce), Salla's list of currencies a store could add, each tied to a country (observed, store demo, 9 October 2026), and WooCommerce's payout currencies by country. Why: rule 1. Q7-BC-029 Q7-SA-031 Q7-WC-K0739
- **section 2, line 67:** - Not taken: WooCommerce's one list for the whole store, as a market can hold such a list, but the list can't hold prices per place. Q7-WC-013
- **section 2, line 72:** - From the platforms: the currencies and rates Shopify, Zid, BigCommerce and Salla record on orders; WooCommerce's earlier orders, which keep their currency and totals; refunds in the currency paid (Shopify) at the refund's rate (WooCommerce). Why: rule 3, as an order whose amounts follow a later rate or store currency no longer shows what the buyer paid. Q7-SA-016 Q7-WC-027 Q7-SH-068 Q7-WC-019
- **section 2, line 74:** - **Exchange rate**, with its **rate source**. Proposed: each rate Sharrwah uses, to show prices or convert amounts for reports, comes from the rate source of that currency of the market: automatic, from a plugged-in **rate provider** on a stated schedule, or manual, fixed by the seller; converted prices follow that currency's rounding rule. A payment provider's rate on a payment is its own; Sharrwah records the rate and fee it reports. Q7-SH-078 Q7-WC-K0755 Q7-BC-035
- **section 2, line 76:** - **Payout account**, with its **payout currency**. Proposed: each destination a seller is paid out to has one payout currency. A seller may have several, one the default, and a payment in a currency matching none is converted by the provider to the default's. Which currencies a payout account may have is set per place and provider. Q7-SH-004 Q7-WC-K0737 Q7-SH-P0155
- **section 2, line 77:** - From the platforms: Shopify's and WooCommerce's payout currency and default account, and Shopify's Multi-Currency Payouts; payout currencies bounded by region or entity (Shopify), country and its banks (WooCommerce, Salla), or the provider (BigCommerce). Why: rule 3, as the money flow ends at this payout, and partner contracts decide its currencies. Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-SA-K1964 Q7-BC-P0016
- **section 2, line 78:** - **Seller ledger**. Proposed: each amount owed to or by a seller, for sales, fees, refunds and payouts, is an entry in one currency. Balances are per currency, never added across currencies, and move between currencies only by a recorded conversion. The ledger records what is owed, whoever holds the money. Q7-SH-131 Q7-WC-048 Q7-BC-058
- **section 2, line 81:** - **Currency migration**. Proposed: the store owner may change the store currency until the first order; after it, only a currency migration run by Sharrwah can, leaving every recorded order as it is and stating whether prices convert at a stated rate or keep their numbers. The same migration serves a change Sharrwah makes for a whole place. Q7-SA-004 Q7-SH-008 Q7-WC-027
- **section 2, line 82:** - From the platforms: Salla's bar once there are orders; Shopify's owner-only change; prices kept by number (Shopify, BigCommerce) or converted (Zid); Shopify's Bulgaria change, made on its stores' behalf, and WooCommerce's routine rewriting orders' currency code. Why: rule 3, as a later change mustn't rewrite an order's currency; and rule 4, as the treatment of prices stays open (section 5). Q7-SH-006 Q7-BC-053 Q7-ZD-K0302 Q7-SH-107 Q7-WC-057
- **section 3, line 87:** - What can plug in: Q7-BC-005 Q7-WC-K0755
- **section 3, line 89:** - **Rate provider**: a swappable source of automatic rates, like WooCommerce's server or the merchant's own source on BigCommerce. Q7-WC-K0755 Q7-BC-035
- **section 3, line 93:** - Per store: the **store currency**, one per store. Q7-WC-K0745
- **section 3, line 98:** - Per order: the charged currency, the store-currency amounts and the rates, fixed when it is placed. Q7-ZD-010 Q7-WC-027
- **section 7, line 151:** - Which rate provider Sharrwah uses for automatic rates. Q7-WC-K0755 Q7-BC-035
- **section 8, line 159:** - What the records show: Shopify and WooCommerce define the payout currency in the same terms, and BigCommerce's settlement currency matches it on role (basis 4). It is set for the payment account: by region or business entity on Shopify, with more currencies on some plans; by country on WooCommerce; through the provider on BigCommerce; by the country's banks on Salla. Balances before payout are kept per currency on Shopify, WooCommerce and BigCommerce. Salla's balance holds sales proceeds before transfer; the page naming its currency wasn't read, and the run on store real-merchant gave the store's wallets in SAR (12 October 2026, observed). Zid's terms set its wallet's currency by the merchant's country; the currency of Zid Pay's balance and deposits, and of Shopify's reserved funds, wasn't in what was read. S01-VP-23 Q7-SH-004 Q7-WC-004 Q7-BC-P0014 Q7-SH-012 Q7-SH-K1268 Q7-SH-P0155 Q7-WC-K0739 Q7-BC-P0016 Q7-SA-K1964 Q7-SH-131 Q7-WC-048 Q7-BC-058 Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022 Q7-ZD-P0122 Q7-ZD-N01 Q7-ZD-N02 Q7-SH-N01

## The cards

### Q7-WC-K0745

**Cited at:** section 1, line 7; section 2, line 61; section 3, line 93

**Record** (`studies/proposals/records/Q7/woocommerce/copied.tsv`):
- concern_id: WC-C-052
- placement: decides
- structure: https://woocommerce.com/document/shop-currency/
- identifier: Shop currency
- statement: WooCommerce only allows for one base currency per store.
- cite_ids: WC-S-0874

**Citation WC-S-0874:** `https://woocommerce.com/document/shop-currency/` | Shop currency | 2026-10-09 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/040-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:02Z, captured)
- quote: WooCommerce only allows for one base currency per store.
- title: Shop currency: documentation - WooCommerce
- in context: … displays and charges in. It does not convert any amounts for you. Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount - update your prices yourself if you need to. Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same. Check that your payment gateway supports the new currency before you switch. Multiple currencies ⟪WooCommerce only allows for one base currency per store.⟫ If you'd like to display products in different currencies (or allow customers to pay in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin. We urge you to evaluate the reasons for opting for a multi-currency setup to help choose the right extension(s) to help achieve your goals. Here are some options for additional currencies: WooPayments gives you free access to multi-currency functio…

### Q7-WC-K0747

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q7/woocommerce/copied.tsv`):
- concern_id: WC-C-052
- placement: decides
- structure: https://woocommerce.com/document/shop-currency/
- identifier: Setting a store’s base currency
- statement: Each WooCommerce store can set one base currency. WooCommerce uses it to display product prices and record new orders.
- cite_ids: WC-S-0876

**Citation WC-S-0876:** `https://woocommerce.com/document/shop-currency/` | Setting a store’s base currency | 2026-10-09 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/040-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:02Z, captured)
- quote: Each WooCommerce store can set one base currency. WooCommerce uses it to display product prices and record new orders.
- title: Shop currency: documentation - WooCommerce
- in context: … Site administration / Store settings / Shop currency Shop currency Currency settings ↑ Back to top WooCommerce has several currency options to choose from when setting up your store. This document will guide you through the following: How to set your shop's base currency. Suggestions for displaying products in currencies other than your base currency. Basic information about exchange rates and fees. Setting a store's base currency ↑ Back to top ⟪Each WooCommerce store can set one base currency. WooCommerce uses it to display product prices and record new orders.⟫ Before changing the currency, confirm that your payment gateway supports it. You need access to WooCommerce settings in your WordPress dashboard. To set the store's currency: From your WordPress admin, navigate to WooCommerce > Settings > General and scroll to the bottom of that screen. Under the Currency options, configure your currency settings as needed: Currency: Choose the currency the store will display on products. Currency position: Choo…

### Q7-WC-055

**Cited at:** section 1, line 9; section 1, line 18; section 2, line 57

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-055
- bears_on: 1;3
- identifier: orders: currency
- statement: 'description' => __( 'Currency the order was created with, in ISO format.', 'woocommerce' ),
- scope: wc/v3 orders
- cite_ids: Q7-WC-C055
- from: held

**Citation Q7-WC-C055:** `woocommerce-11.2.1:includes/rest-api/Controllers/Version2/class-wc-rest-orders-v2-controller.php` | line 1260 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'description' => __( 'Currency the order was created with, in ISO format.', 'woocommerce' ),
- in context: …, 'readonly' => true, ), 'version' => array( 'description' => __( 'Version of WooCommerce which last updated the order.', 'woocommerce' ), 'type' => 'string', 'context' => array( 'view', 'edit' ), 'readonly' => true, ), 'status' => array( 'description' => __( 'Order status.', 'woocommerce' ), 'type' => 'string', 'default' => OrderStatus::PENDING, 'enum' => $this->get_order_statuses(), 'context' => array( 'view', 'edit' ), ), 'currency' => array( ⟪'description' => __( 'Currency the order was created with, in ISO format.', 'woocommerce' ),⟫ 'type' => 'string', 'default' => get_woocommerce_currency(), 'enum' => array_keys( get_woocommerce_currencies() ), 'context' => array( 'view', 'edit' ), ), 'date_created' => array( 'description' => __( "The date the order was created, in the site's timezone.", 'woocommerce' ), 'type' => 'date-time', 'context' => array( 'view', 'edit' ), 'readonly' => true, ), 'date_created_gmt' => array( 'description' => __( 'The date the order was created, as G…

### Q7-WC-013

**Cited at:** section 1, line 10; section 2, line 67

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-013
- bears_on: 2
- identifier: Enabled currencies
- statement: Initially, the Enabled currencies list will only show your default store currency.
- scope: WooPayments multi-currency
- cite_ids: Q7-WC-C013
- from: held

**Citation Q7-WC-C013:** `https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/` | Configuring multi-currency | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/058-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:04Z, captured)
- quote: Initially, the Enabled currencies list will only show your default store currency.
- title: Multi-currency with WooPayments Documentation - WooCommerce
- in context: …at. Enabling multi-currency ↑ Back to top To enable the multi-currency feature, if it's not already: Go to Payments > Settings in your WordPress dashboard. Scroll down to the bottom and click on Advanced settings. Check the Enable Multi-Currency box. Click Save changes at the bottom. Configuring multi-currency ↑ Back to top Once WooPayments multi-currency has been enabled, a tab for it's settings will be added to the WooCommerce > Settings page. ⟪Initially, the Enabled currencies list will only show your default store currency.⟫ Enabled currencies ↑ Back to top Clicking the Add/remove currencies button will show a list of supported currencies. From this list, you can select all the currencies that you want to allow your customers to view prices in. After selecting any additional currencies you'd like to add to your store, click Update selected to save that list. Afterward, the Enabled currencies list will reflect those changes. Currencies can also be removed by unchecki…

### Q7-WC-029

**Cited at:** section 1, line 12; section 1, line 15

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-029
- bears_on: 1
- identifier: Multiple currencies: Currency Converter Widget
- statement: Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers — your store’s base currency is still used.
- scope: Currency Converter Widget
- cite_ids: Q7-WC-C029
- from: held

**Citation Q7-WC-C029:** `https://woocommerce.com/document/shop-currency/` | Multiple currencies | 2026-10-09 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/040-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:02Z, captured)
- quote: Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers — your store’s base currency is still used.
- title: Shop currency: documentation - WooCommerce
- in context: … in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin. We urge you to evaluate the reasons for opting for a multi-currency setup to help choose the right extension(s) to help achieve your goals. Here are some options for additional currencies: WooPayments gives you free access to multi-currency functionality, enabling customers to view and pay for products in their preferred currency. ⟪Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers - your store's base currency is still used.⟫ Using the Currency Converter Widget enables your store to run on a single currency, which simplifies store administration, accounting, and general maintenance; and helps customers to view your product catalog in their native currency. TIV Multi-Currency for WooCommerce allows customers to pay in the currency of their choice. MultilingualPress can display your content, products, and prices in multiple languages and currencies. Currency Switcher f…

### Q7-WC-004

**Cited at:** section 1, line 19; section 8, line 159

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-004
- bears_on: 1
- identifier: payout currency
- statement: The payout currency is the currency in which funds are paid out into your bank account.
- scope: WooPayments
- cite_ids: Q7-WC-C004
- from: held

**Citation Q7-WC-C004:** `https://woocommerce.com/document/woopayments/currencies/currencies-overview/` | Currencies in a transaction | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/057-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:04Z, captured)
- quote: The payout currency is the currency in which funds are paid out into your bank account.
- title: Currencies with WooPayments Documentation - WooCommerce
- in context: …ntially involve multiple currencies: The customer currency is the currency displayed to customers while they browse your store and the currency they are charged in when they pay for their order. This can also be referred to as the "presentment currency." By default, the customer currency will be the same as the store currency in your WooCommerce settings. Using WooPayments' built-in multi-currency functions, the customer currency can be changed. ⟪The payout currency is the currency in which funds are paid out into your bank account.⟫ This can also be referred to as the "settlement currency." The payout currency may not always be the same as the customer currency. For some merchants, it's possible to receive payouts in different currencies into different bank accounts. Tracking currencies The WooPayments dashboard can track the currencies involved in each transaction, including payouts, payments, and disputes. This section highlights the elements of the dashboard that provide…

### Q7-WC-K0737

**Cited at:** section 1, line 20; section 2, line 76

**Record** (`studies/proposals/records/Q7/woocommerce/copied.tsv`):
- concern_id: WC-C-051
- placement: decides
- structure: https://woocommerce.com/document/woopayments/payouts/payout-currencies/
- identifier: Payout currencies
- statement: If you take a payment in a currency that doesn’t match the currency of one of your bank accounts, it will be converted into your default currency and paid out into the default account.
- cite_ids: WC-S-0535

**Citation WC-S-0535:** `https://woocommerce.com/document/woopayments/payouts/payout-currencies/` | Payout currencies | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/075-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:05Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/098-woocommerce.com/text.txt` (fetched 2026-10-12T10:51:09Z, captured)
- quote: If you take a payment in a currency that doesn’t match the currency of one of your bank accounts, it will be converted into your default currency and paid out into the default account.
- title: Payout currencies Documentation - WooCommerce
- in context: …cumentation / WooPayments: Payouts / Payout currencies Payout currencies WooPayments can accept payments in over 100 different currencies. However, if the customer's currency differs from your account's payout currency, you will be charged a currency conversion fee. To avoid these fees, you may be able to have funds in different currencies paid out into separate bank accounts. When using multiple bank accounts, one must be chosen as the default. ⟪If you take a payment in a currency that doesn't match the currency of one of your bank accounts, it will be converted into your default currency and paid out into the default account.⟫ EXAMPLE: A merchant in Germany sells goods throughout Europe, and has a default bank account in Euros. They have also added a second bank account denominated in Swiss francs. As a result, payouts for orders that were paid for in Swiss francs will be sent to the Swiss franc bank account. Payments for other orders will be converted to Euros (if needed) and paid out into the default Euro bank account. Eligibility To see if you are eligible to add b…

### Q7-WC-054

**Cited at:** section 1, line 27; section 2, line 62; section 2, line 63

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-054
- bears_on: 2
- identifier: woocommerce_currency (from locale-info currency_code)
- statement: 'woocommerce_currency'           => $country_info['currency_code'],
- cite_ids: Q7-WC-C054
- from: held

**Citation Q7-WC-C054:** `woocommerce-11.2.1:src/Admin/API/OnboardingProfile.php` | line 358 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'woocommerce_currency'           => $country_info['currency_code'],
- in context: …units( WP_REST_Request $request ) { $country_code = $request->get_param( 'country_code' ); $locale_info = include WC()->plugin_path() . '/i18n/locale-info.php'; if ( empty( $country_code ) || ! isset( $locale_info[ $country_code ] ) ) { return new WP_Error( 'woocommerce_rest_invalid_country_code', __( 'Invalid country code.', 'woocommerce' ), array( 'status' => 400 ) ); } $country_info = $locale_info[ $country_code ]; $currency_settings = array( ⟪'woocommerce_currency' => $country_info['currency_code'],⟫ 'woocommerce_currency_pos' => $country_info['currency_pos'], 'woocommerce_price_thousand_sep' => $country_info['thousand_sep'], 'woocommerce_price_decimal_sep' => $country_info['decimal_sep'], 'woocommerce_price_num_decimals' => $country_info['num_decimals'], 'woocommerce_weight_unit' => $country_info['weight_unit'], 'woocommerce_dimension_unit' => $country_info['dimension_unit'], ); foreach ( $currency_settings as $key => $value ) { update_opti…

### Q7-WC-K0739

**Cited at:** section 1, line 31; section 2, line 64; section 2, line 77; section 8, line 159

**Record** (`studies/proposals/records/Q7/woocommerce/copied.tsv`):
- concern_id: WC-C-051
- placement: decides
- structure: https://woocommerce.com/document/woopayments/payouts/payout-currencies/
- identifier: Eligibility
- statement: If your country only has a single currency listed, that means you can only accept payouts in that currency, and those payouts can only be sent to banks in your country.
- cite_ids: WC-S-0536

**Citation WC-S-0536:** `https://woocommerce.com/document/woopayments/payouts/payout-currencies/` | Eligibility | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/075-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:05Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/098-woocommerce.com/text.txt` (fetched 2026-10-12T10:51:09Z, captured)
- quote: If your country only has a single currency listed, that means you can only accept payouts in that currency, and those payouts can only be sent to banks in your country.
- title: Payout currencies Documentation - WooCommerce
- in context: …LE PAYOUT CURRENCIES Australia AUD Bulgaria BGN, CHF, DKK, EUR, GBP, NOK, SEK, USD Canada CAD, USD Czech Republic CHF, CZK, DKK, EUR, GBP, NOK, SEK, USD Hong Kong HKD Hungary CHF, DKK, EUR, GBP, HUF, NOK, SEK, USD Japan JPY New Zealand NZD Poland CHF, DKK, EUR, GBP, NOK, PLN, SEK, USD Romania CHF, DKK, EUR, GBP, NOK, RON, SEK, USD Singapore SGD United Arab Emirates AED United States USD Other supported countries CHF, DKK, EUR, GBP, NOK, SEK, USD ⟪If your country only has a single currency listed, that means you can only accept payouts in that currency, and those payouts can only be sent to banks in your country.⟫ The rest of this section - including the second chart below - does not apply to you. If your country does have multiple currencies listed, consult the second chart below, which lists the countries where you can pay out funds in each currency. CURRENCY CAN BE PAID OUT TO BANKS IN... AED United Arab Emirates AUD Australia BGN Bulgaria CAD Canada CHF Liechtenstein, Switzerland CZK Czech Republic DKK Denmark EUR Austria, Belgium, Bulgaria, Croatia, …

### Q7-WC-027

**Cited at:** section 1, line 41; section 2, line 72; section 2, line 81; section 3, line 98

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-027
- bears_on: 3
- identifier: Changing the base currency
- statement: Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same.
- cite_ids: Q7-WC-C027
- from: held

**Citation Q7-WC-C027:** `https://woocommerce.com/document/shop-currency/` | Changing the base currency | 2026-10-09 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/040-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:02Z, captured)
- quote: Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same.
- title: Shop currency: documentation - WooCommerce
- in context: …nd its functionality, we recommend working with a Woo Agency Partner or a WooCommerce developer on Codeable. Changing the base currency ↑ Back to top Changing your base currency changes which currency your store displays and charges in. It does not convert any amounts for you. Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount - update your prices yourself if you need to. ⟪Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same.⟫ Check that your payment gateway supports the new currency before you switch. Multiple currencies ↑ Back to top WooCommerce only allows for one base currency per store. If you'd like to display products in different currencies (or allow customers to pay in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin. We urge you to evaluate the reasons for opting for a multi-currency setup to hel…

### Q7-WC-K0755

**Cited at:** section 1, line 42; section 2, line 74; section 3, line 87; section 3, line 89; section 7, line 151

**The same record as Q1-WC-K0755,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: By default, exchange rates are regularly retrieved from the WooPayments server.
- scope: WooPayments

### Q7-WC-019

**Cited at:** section 1, line 43; section 2, line 72

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-019
- bears_on: 3
- identifier: Refunds and currencies
- statement: If you refund a currency-converted payment, the amount deducted from your balance is converted to the customer currency using the exchange rate at the time you issued the refund. Since exchange rates can vary over time, the amount deducted from your balance may be more or less than the original payment.
- scope: WooPayments multi-currency
- cite_ids: Q7-WC-C019
- from: held

**Citation Q7-WC-C019:** `https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/` | Refunds and currencies | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/058-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:04Z, captured)
- quote: If you refund a currency-converted payment, the amount deducted from your balance is converted to the customer currency using the exchange rate at the time you issued the refund.
- title: Multi-currency with WooPayments Documentation - WooCommerce
- in context: …rance > Widgets and look for the "Currency Switcher" widget and add it to the best location in your theme. In the widget setting, choose if you want the widget to display currency symbols and flags next to the currency name. Customer default currency ↑ Back to top Lastly, your customers can choose their preferred currency on the My Account > Account Details page. Selecting your default currency as a customer. Refunds and currencies ↑ Back to top ⟪If you refund a currency-converted payment, the amount deducted from your balance is converted to the customer currency using the exchange rate at the time you issued the refund.⟫ Since exchange rates can vary over time, the amount deducted from your balance may be more or less than the original payment. Put another way: the customer will always be refunded the exact amount that they paid and in the currency that they paid in, regardless of any rate fluctuations between the time of the transaction and the time of the refund. For example, if your payout currency is EUR and you receive a 60 USD order when the exchange rate …

### Q7-WC-057

**Cited at:** section 1, line 44; section 2, line 58; section 2, line 82

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-057
- bears_on: 3
- identifier: wc_update_250_currency: _order_currency
- statement: // Update LAK currency code. $wpdb->update( $wpdb->postmeta, array( 'meta_value' => 'LAK', ), array( 'meta_key'   => '_order_currency', 'meta_value' => 'KIP', ) );
- cite_ids: Q7-WC-C057
- from: held

**Citation Q7-WC-C057:** `woocommerce-11.2.1:includes/wc-update-functions.php` | lines 1050-1060 | 2026-10-09 | kind: shipped | quote check: found
- quote: // Update LAK currency code. $wpdb->update( $wpdb->postmeta, array( 'meta_value' => 'LAK', ), array( 'meta_key'   => '_order_currency', 'meta_value' => 'KIP', ) );
- in context: …or 2.4.1 * * @return void */ function wc_update_241_db_version() { WC_Install::update_db_version( '2.4.1' ); } /** * Update currency settings for 2.5 * * @return void */ function wc_update_250_currency() { global $wpdb; // Fix currency settings for LAK currency. $current_currency = get_option( 'woocommerce_currency' ); if ( 'KIP' === $current_currency ) { update_option( 'woocommerce_currency', 'LAK' ); } // phpcs:disable WordPress.DB.SlowDBQuery ⟪// Update LAK currency code. $wpdb->update( $wpdb->postmeta, array( 'meta_value' => 'LAK', ), array( 'meta_key' => '_order_currency', 'meta_value' => 'KIP', ) );⟫ // phpcs:enable WordPress.DB.SlowDBQuery } /** * Update DB version for 2.5 * * @return void */ function wc_update_250_db_version() { WC_Install::update_db_version( '2.5.0' ); } /** * Update ship to countries options for 2.6 * * @return void */ function wc_update_260_options() { // woocommerce_calc_shipping option has been removed in 2.6. if ( 'no' === get_option( 'woocommerce_calc_shipping' ) ) { update_option( 'woocommerce_ship_to_countries', '…

### Q7-WC-048

**Cited at:** section 1, line 49; section 1, line 53; section 2, line 78; section 8, line 159

**Record** (`studies/proposals/records/Q7/woocommerce/statements.tsv`):
- stmt_id: Q7-WC-048
- bears_on: 4
- identifier: Overview: account balance
- statement: If you have added multiple bank accounts to receive payouts in different currencies, a dropdown is shown so you can view your balance in each currency.
- scope: WooPayments
- cite_ids: Q7-WC-C048
- from: held

**Citation Q7-WC-C048:** `https://woocommerce.com/document/woopayments/managing-money/` | Overview | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/090-woocommerce.com/text.txt` (fetched 2026-10-12T10:51:01Z, captured)
- quote: If you have added multiple bank accounts to receive payouts in different currencies, a dropdown is shown so you can view your balance in each currency.
- title: Managing Money with WooPayments Documentation - WooCommerce
- in context: …ey can move through your site and your account. This document explains how WooPayments presents information to you about where your money came from and where it's going. Overview ↑ Back to top The Payments > Overview page gives you a brief summary of how money is flowing through your WooPayments account. The top section shows your account balance. Click the question mark icons to learn more about what each figure means, or consult this document. ⟪If you have added multiple bank accounts to receive payouts in different currencies, a dropdown is shown so you can view your balance in each currency.⟫ Occasionally, the top box may change, such as if you have a dispute nearing its deadline or if there's another time-sensitive action needed for your account. To keep your store and WooPayments account running smoothly, it is recommended that you attend to any tasks that appear here. Below that, the Payouts section shows a list of your recent payouts and their amounts. The Account Details section shows your account's status. In most cases, your a…
