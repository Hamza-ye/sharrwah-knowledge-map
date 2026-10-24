# Cards: Q7 on bigcommerce

13 records cited by `studies/proposals/drafts/Q7/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Prices held: Shopify, Zid, WooCommerce and BigCommerce hold a seller's own prices in one currency per store, and match on role (basis 4). Shopify's store currency is the one "for pricing products and running reports"; Zid's العملة الأساسية is "العملة التي تم إدخال أسعار المنتجات باستخدامها"; WooCommerce allows "one base currency per store", and "WooCommerce uses it to display product prices and record new orders"; BigCommerce's default currency is "assigned during store creation, is always a transactional currency". Salla's seller sets the store's current currency, but the words read don't say prices are entered in it, so Salla's match is partial. Q7-SH-K1935 Q7-ZD-002 Q7-WC-K0745 Q7-WC-K0747 Q7-BC-013 Q7-SA-001
- **section 1, line 12:** - Paid by buyers: on Shopify, BigCommerce, WooCommerce and Salla the currency shown and the currency charged can differ, and what the payment provider supports decides the charge; they match on role (basis 4). Zid's pages aren't reconciled (below): Q7-SH-K1938 Q7-BC-014 Q7-WC-029 Q7-SA-K1963
- **section 1, line 14:** - BigCommerce: the seller sets each currency as "transactional or display-only"; to be transactional, "a payment gateway that supports the currency must be enabled"; and "Display currencies transact in your store's default currency". Q7-BC-031 Q7-BC-005 Q7-BC-014
- **section 1, line 18:** - Each order records its currency, and four record the store's currency or a rate beside it, matching on role (basis 4): Shopify's order has `presentmentCurrencyCode`, and its MoneyBag holds both amounts; Zid's order gives the "Exchange rate of the store currency relative to the order currency"; BigCommerce's has `currency_code`, `default_currency_code` and `currency_exchange_rate`; Salla's an `exchange_rate` with `base_currency`, `exchange_currency` and `rate`; WooCommerce's a single "Currency the order was created with, in ISO format." (shipped code; the others stated). Q7-SH-124 Q7-SH-123 Q7-ZD-010 Q7-BC-020 Q7-SA-016 Q7-WC-055
- **section 1, line 20:** - The currency paid out can differ from the one paid, and the provider converts: Shopify applies a rate and fee "at the time of payment capture"; WooCommerce converts a payment matching none of the seller's bank accounts "into your default currency and paid out into the default account"; on BigCommerce "the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope" (stated). On store fake-demo-sharrwah (30 September 2026, observed), a report page's saved markup also hid a metric, "Foreign exchange fees": "Currency conversion fees you pay when customers purchase in a different currency". Q7-SH-013 Q7-WC-K0737 Q7-BC-P0015 Q7-SH-207
- **section 1, line 27:** - A store's own currency is set for the store, by the seller, with a default from the store's country; Zid, WooCommerce and BigCommerce match on role (basis 4). Zid asks for it "بناء على عملة دولتك"; WooCommerce's onboarding sets `woocommerce_currency` from the country's `currency_code` (shipped code); BigCommerce's default currency "is assigned based on your location" (stated). Q7-ZD-001 Q7-WC-054 Q7-BC-029
- **section 1, line 30:** - The currency charged is set per currency, within what the provider supports, by BigCommerce's seller through each currency's "Transacting currency"; on Shopify, by the store's primary gateway (above). Q7-BC-031 Q7-SH-K1937
- **section 1, line 31:** - The currency paid out is set for the payment account, by its region, entity, country or provider. Shopify's "domestic currency is determined by your Shopify Payments region and is the default currency for your payouts", and each business entity has "its own Shopify Payments account, payout currency, and bank account" (not checked on Salla, Q7-SH-K1268); where WooCommerce's chart lists one currency for a country, "those payouts can only be sent to banks in your country"; BigCommerce's merchant sets it "through its payment provider". Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-BC-P0016
- **section 1, line 38:** - The numbers stay and the currency changes, on Shopify and BigCommerce, which match on role (basis 4): "The currency of your product prices and discount rates update automatically, but not the amount"; "changing the default currency will not trigger price recalculation for the catalog". Q7-SH-006 Q7-BC-053
- **section 1, line 42:** - Rates are automatic or fixed by the seller. Shopify's markets choose Dynamic, "to automatically convert prices", or Manual, "to set a fixed exchange rate" (not checked on Salla, Q7-SH-078); WooCommerce's rates come by default from "the WooPayments server"; BigCommerce's merchant can use its Currency Service or "use the API to automatically update the exchange rate from their trusted source" (stated). On store demo-fake-dev-store (30 September 2026, observed), a market's saved markup held "Exchange rate (FX)" with Dynamic, Manual and "1 YER = 0.0024448788 SAR", and "Price rounding" with "Round up to the nearest SAR 1.00" and "Do not round prices". Q7-SH-078 Q7-WC-K0755 Q7-BC-035 Q7-SH-204
- **section 1, line 50:** - BigCommerce: BigCommerce Payments shows "the existing balance per currency". Q7-BC-058
- **section 1, line 53:** - Shopify, WooCommerce and BigCommerce keep the seller's balance per currency, and match on role (basis 4): "across all supported currencies", "in each currency", "per currency" (stated). Q7-SH-131 Q7-WC-048 Q7-BC-058
- **section 2, line 62:** - From the platforms: one currency per store for a seller's prices (Shopify, Zid, WooCommerce, BigCommerce), with a default from the store's country (Zid, WooCommerce, BigCommerce). Why: rule 1, as the default and choices come from **place currency settings**, not a build per place; and rule 3, as each **order currency record** converts to it. Q7-ZD-002 Q7-BC-013 Q7-WC-054 Q7-BC-029
- **section 2, line 64:** - From the platforms: country defaults (Zid, WooCommerce, BigCommerce), Salla's list of currencies a store could add, each tied to a country (observed, store demo, 9 October 2026), and WooCommerce's payout currencies by country. Why: rule 1. Q7-BC-029 Q7-SA-031 Q7-WC-K0739
- **section 2, line 68:** - **Charged currency** and **shown-only currency**. Proposed: each currency of a market is one or the other. A shown-only currency converts prices for display, and the buyer pays in the store currency, as checkout says. A currency can be charged only if a provider connected for the market declares, in its **provider currency capability**, that it takes it. Q7-BC-031 Q7-BC-005 Q7-BC-014
- **section 2, line 71:** - **Order currency record**. Proposed: an order records, when placed, the charged currency and every amount in it, the same amounts in the store currency, the display currency if different, and each rate used, with its source and time; none is recomputed. A refund goes out in the charged currency, any conversion of it at that day's rate, recorded beside the first. Q7-SH-123 Q7-ZD-010 Q7-BC-020
- **section 2, line 74:** - **Exchange rate**, with its **rate source**. Proposed: each rate Sharrwah uses, to show prices or convert amounts for reports, comes from the rate source of that currency of the market: automatic, from a plugged-in **rate provider** on a stated schedule, or manual, fixed by the seller; converted prices follow that currency's rounding rule. A payment provider's rate on a payment is its own; Sharrwah records the rate and fee it reports. Q7-SH-078 Q7-WC-K0755 Q7-BC-035
- **section 2, line 75:** - From the platforms: Shopify's Dynamic or Manual rate per market, with Price rounding beside it in a market's saved markup (store demo-fake-dev-store, 30 September 2026, observed); WooCommerce's server rates and BigCommerce's merchant's own source through the API; the rate on a payment, outside BigCommerce's scope, and Shopify's rate and fee at capture. Why: rule 2, as the source is likely to change; and rule 1, as a place may need its own. Q7-BC-P0015 Q7-SH-013 Q7-SH-204
- **section 2, line 77:** - From the platforms: Shopify's and WooCommerce's payout currency and default account, and Shopify's Multi-Currency Payouts; payout currencies bounded by region or entity (Shopify), country and its banks (WooCommerce, Salla), or the provider (BigCommerce). Why: rule 3, as the money flow ends at this payout, and partner contracts decide its currencies. Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-SA-K1964 Q7-BC-P0016
- **section 2, line 78:** - **Seller ledger**. Proposed: each amount owed to or by a seller, for sales, fees, refunds and payouts, is an entry in one currency. Balances are per currency, never added across currencies, and move between currencies only by a recorded conversion. The ledger records what is owed, whoever holds the money. Q7-SH-131 Q7-WC-048 Q7-BC-058
- **section 2, line 82:** - From the platforms: Salla's bar once there are orders; Shopify's owner-only change; prices kept by number (Shopify, BigCommerce) or converted (Zid); Shopify's Bulgaria change, made on its stores' behalf, and WooCommerce's routine rewriting orders' currency code. Why: rule 3, as a later change mustn't rewrite an order's currency; and rule 4, as the treatment of prices stays open (section 5). Q7-SH-006 Q7-BC-053 Q7-ZD-K0302 Q7-SH-107 Q7-WC-057
- **section 3, line 87:** - What can plug in: Q7-BC-005 Q7-WC-K0755
- **section 3, line 88:** - **Provider currency capability**: each payment provider plugged in declares, per place and payment method, the currencies it can charge and pay out in, and reports each payment's rate and fee. It draws on BigCommerce's gateway support per currency and settlement currency set through the provider, Shopify's rate and fee at capture, and Shopify's support by method, down to "Unsupported and prices convert to shop currency". Q7-BC-005 Q7-BC-P0016 Q7-SH-013 Q7-SH-099
- **section 3, line 89:** - **Rate provider**: a swappable source of automatic rates, like WooCommerce's server or the merchant's own source on BigCommerce. Q7-WC-K0755 Q7-BC-035
- **section 3, line 91:** - What is set per what. Where the platforms differ in level, the proposal takes the finer, so a coarser set-up is still one setting (rule 1): Q7-SH-078 Q7-BC-031
- **section 3, line 92:** - Per place: the default and allowed currencies, in **place currency settings**, as the country gives the default on Zid, WooCommerce and BigCommerce. Q7-ZD-001 Q7-BC-029
- **section 3, line 95:** - Per currency of a market: charged or shown only, as BigCommerce sets for each currency; and the **rate source**, which Shopify sets per market and BigCommerce per currency. Q7-BC-031 Q7-SH-078
- **section 3, line 96:** - Per provider and place: the currencies it can charge and pay out in, and its rate and fee. Q7-BC-P0016 Q7-BC-P0015
- **section 3, line 99:** - Per seller and currency: the balances in the **seller ledger**. Q7-BC-058
- **section 3, line 100:** - Who sets each: Q7-SH-008 Q7-SA-K1956 Q7-BC-P0015
- **section 3, line 104:** - The payment provider decides what it can charge and pay out in, and its rates and fees, which on BigCommerce are outside the platform's scope. Q7-BC-P0015
- **section 5, line 123:** - Which currencies can be charged and paid out at each place. Keep them as **provider currency capability** data for each place, not code. Settled by: the contracts with the providers Sharrwah works with (section 7). Q7-SH-K1937 Q7-BC-P0016
- **section 7, line 146:** - Which payment providers Sharrwah works with at each place, given that what they support decides the currencies buyers can be charged in, and sellers paid out in; Stripe isn't available for Yemen. Q7-SH-K1937 Q7-BC-P0016 Q7-SA-K1963 YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 148:** - Whether Sharrwah converts currencies, or charges a conversion fee, itself, as Shopify applies a rate and fee at capture, or leaves conversion and its rate to the providers, as BigCommerce does. At the internationally recognized government's area, foreign currency is bought and sold in cash only, not through digital platforms. Q7-SH-013 Q7-BC-P0015 YK-05 (cash only, not through digital platforms @ the internationally recognized government's area, as of 2025-02-22)
- **section 7, line 149:** - In which currency Sharrwah bills its own fees at each place. BigCommerce's terms say "Fees are payable in U.S. Dollars, unless otherwise specified."; Zid's put its fees in Saudi riyals or the merchant's local currency. Q7-BC-K0177 Q7-ZD-K0156
- **section 7, line 151:** - Which rate provider Sharrwah uses for automatic rates. Q7-WC-K0755 Q7-BC-035
- **section 8, line 159:** - What the records show: Shopify and WooCommerce define the payout currency in the same terms, and BigCommerce's settlement currency matches it on role (basis 4). It is set for the payment account: by region or business entity on Shopify, with more currencies on some plans; by country on WooCommerce; through the provider on BigCommerce; by the country's banks on Salla. Balances before payout are kept per currency on Shopify, WooCommerce and BigCommerce. Salla's balance holds sales proceeds before transfer; the page naming its currency wasn't read, and the run on store real-merchant gave the store's wallets in SAR (12 October 2026, observed). Zid's terms set its wallet's currency by the merchant's country; the currency of Zid Pay's balance and deposits, and of Shopify's reserved funds, wasn't in what was read. S01-VP-23 Q7-SH-004 Q7-WC-004 Q7-BC-P0014 Q7-SH-012 Q7-SH-K1268 Q7-SH-P0155 Q7-WC-K0739 Q7-BC-P0016 Q7-SA-K1964 Q7-SH-131 Q7-WC-048 Q7-BC-058 Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022 Q7-ZD-P0122 Q7-ZD-N01 Q7-ZD-N02 Q7-SH-N01

## The cards

### Q7-BC-013

**Cited at:** section 1, line 7; section 2, line 62

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-013
- bears_on: 1;2
- identifier: Setting up Payment Methods for Additional Transactional Currencies
- statement: The store’s default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency.
- cite_ids: Q7-BC-C015
- from: held

**Citation Q7-BC-C015:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | Setting up Payment Methods for Additional Transactional Currencies | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:41:00Z, captured)
- quote: The store’s default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …your store has USD as its default currency and offers GBP as a transactional currency, a €30 keychain with a modifier for engraving (add $5) will have its price calculated as: €30 + [$5 x (the autoconversion rate)] ANALYTICS Store analytics are displayed in the store's default currency, using the configured exchange rate. Since there is a conversion, these are approximate values. Setting up Payment Methods for Additional Transactional Currencies ⟪The store's default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency.⟫ Display currencies transact in your store's default currency. As such, they use the payment methods configured for the store's default currency. See Available Payment Gateways for a table of payment gateways that support additional transactional currencies. All offline payment methods support additional transactional currencies. If there are no payment methods currently set up for a transactional currency, you'll see a Set up button in the Payme…

### Q7-BC-014

**Cited at:** section 1, line 12; section 1, line 14; section 2, line 68

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-014
- bears_on: 1;2
- identifier: Setting up Payment Methods for Additional Transactional Currencies
- statement: Display currencies transact in your store's default currency. As such, they use the payment methods configured for the store’s default currency.
- cite_ids: Q7-BC-C016
- from: held

**Citation Q7-BC-C016:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | Setting up Payment Methods for Additional Transactional Currencies | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:41:00Z, captured)
- quote: Display currencies transact in your store's default currency. As such, they use the payment methods configured for the store’s default currency.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …analytics are displayed in the store's default currency, using the configured exchange rate. Since there is a conversion, these are approximate values. Setting up Payment Methods for Additional Transactional Currencies The store's default currency, assigned during store creation, is always a transactional currency. When you create an additional transactional currency, you'll need to set up which payment methods you want to use for that currency. ⟪Display currencies transact in your store's default currency. As such, they use the payment methods configured for the store's default currency.⟫ See Available Payment Gateways for a table of payment gateways that support additional transactional currencies. All offline payment methods support additional transactional currencies. If there are no payment methods currently set up for a transactional currency, you'll see a Set up button in the Payment provider column, under Additional Currencies in your store's Currencies settings. If your store has additional storefronts, you will be able t…

### Q7-BC-031

**Cited at:** section 1, line 14; section 1, line 30; section 2, line 68; section 3, line 91; section 3, line 95

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-031
- bears_on: 2
- identifier: Transacting currency
- statement: Transacting currency — determines if the currency will be transactional or display-only.
- cite_ids: Q7-BC-C040
- from: held

**Citation Q7-BC-C040:** `https://support.bigcommerce.com/s/article/Managing-Currencies` | Adding a Currency: TRANSACTIONS | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/033-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:36Z, captured)
- quote: Transacting currency — determines if the currency will be transactional or display-only.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …rrency code that corresponds to the currency you want to set up, then click Next. 3. Configure your currency's display and transactional settings. 4. Save your changes. CURRENCY DISPLAY CONFIGURATIONS Display Name - used to identify his currency on the storefront. For example, Canadian Dollar. Default to [Currency Code] in these countries - visitors in these countries will have this currency selected by default. For example, Canada. TRANSACTIONS ⟪Transacting currency - determines if the currency will be transactional or display-only.⟫ To learn more about the difference between display and transactional currencies, see our article on Using Multiple Currencies Exchange rate - Currencies that are display-only have the option of having their exchange rate be static or dynamic. Transactional currencies use static conversion rates, while display-only currencies can use either static or dynamic conversion rates. Static - Set the exchange rate to automatically convert your prices and…

### Q7-BC-005

**Cited at:** section 1, line 14; section 2, line 68; section 3, line 87; section 3, line 88

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-005
- bears_on: 1;2
- identifier: Transactional currency
- statement: In order for a currency to be transactional, a payment gateway that supports the currency must be enabled.
- cite_ids: Q7-BC-C005
- from: held

**Citation Q7-BC-C005:** `https://support.bigcommerce.com/s/article/Using-Multiple-Currencies` | How Multicurrency Works in Different Parts of the Store | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/049-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:41:00Z, captured)
- quote: In order for a currency to be transactional, a payment gateway that supports the currency must be enabled.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …hange the final settlement amount. You can choose whether a currency should be display-only or transactional when adding or editing a currency. How Multicurrency Works in Different Parts of the Store You can enable multiple currencies in your control panel from Settings › Currencies. To learn how to add new currencies and set your default currency, see Managing Currencies. In Bigcommerce, a currency can be transactional or used for display only. ⟪In order for a currency to be transactional, a payment gateway that supports the currency must be enabled.⟫ Once you've enabled multiple currencies, certain aspects of the store, such as orders, payment methods, and analytics, will be handled differently. Orders Shipping Refunds Supported Payment Methods Price Lists Modifiers Analytics ORDERS The View Orders page in the control panel includes the currency the order was transacted in. The order history page in a customer's storefront account displays past orders in the currency their order was transact…

### Q7-BC-020

**Cited at:** section 1, line 18; section 2, line 71

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-020
- bears_on: 1
- identifier: Currency Fields
- statement: * `currency_id` - the display currency ID. Depending on the currency selected, the value may be different from the transactional currency. * `currency_code` - the currency code of the display currency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency. * `currency_exchange_rate` - the exchange rate between the store’s default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1). * `default_currency_id` - the transactional currency ID. * `default_currency_code` - the currency code of the transactional currency the shopper pays in.
- scope: Orders V2
- cite_ids: Q7-BC-C023;Q7-BC-C024;Q7-BC-C025;Q7-BC-C026;Q7-BC-C027
- from: held

**Citation Q7-BC-C023:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/orders.md` | ### Currency Fields | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/031-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:19:46Z, captured)
- quote: * `currency_id` - the display currency ID. Depending on the currency selected, the value may be different from the transactional currency.
- title: Orders V2
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. Manage order coupons, messages, products, shipping addresses, statuses, taxes, shipments, and shipping address quotes. Order The Order object contains a record of the purchase agreement between a shop…
- headings: Orders V2 > Order > Currency Fields
- in context: … The Order object contains a record of the purchase agreement between a shopper and a merchant. To learn more about creating orders, see [Orders API Guide](/developer/docs/admin/checkout-and-cart/orders). ### Currency Fields The **default** currency refers to the transactional currency which is the currency the shopper pays in. The **display** currency refers to the presentational currency used to present prices to the shopper on the storefront. ⟪* `currency_id` - the display currency ID. Depending on the currency selected, the value may be different from the transactional currency.⟫ * `currency_code` - the currency code of the display currency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency. * `currency_exchange_rate` - the exchange rate between the store's default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1).…

**Citation Q7-BC-C024:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/orders.md` | ### Currency Fields | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/031-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:19:46Z, captured)
- quote: * `currency_code` - the currency code of the display currency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency.
- title, opening and note boxes: as for this source's citation above
- headings: Orders V2 > Order > Currency Fields
- in context: …rders API Guide](/developer/docs/admin/checkout-and-cart/orders). ### Currency Fields The **default** currency refers to the transactional currency which is the currency the shopper pays in. The **display** currency refers to the presentational currency used to present prices to the shopper on the storefront. * `currency_id` - the display currency ID. Depending on the currency selected, the value may be different from the transactional currency. ⟪* `currency_code` - the currency code of the display currency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency.⟫ * `currency_exchange_rate` - the exchange rate between the store's default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1). * `default_currency_id` - the transactional currency ID. * `default_currency_code` - the currency code of the transactional currency the shopper pays in. The following additional fields are returned on orders when …

**Citation Q7-BC-C025:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/orders.md` | ### Currency Fields | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/031-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:19:46Z, captured)
- quote: * `currency_exchange_rate` - the exchange rate between the store’s default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1).
- title, opening and note boxes: as for this source's citation above
- headings: Orders V2 > Order > Currency Fields
- in context: … refers to the presentational currency used to present prices to the shopper on the storefront. * `currency_id` - the display currency ID. Depending on the currency selected, the value may be different from the transactional currency. * `currency_code` - the currency code of the display currency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency. ⟪* `currency_exchange_rate` - the exchange rate between the store's default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1).⟫ * `default_currency_id` - the transactional currency ID. * `default_currency_code` - the currency code of the transactional currency the shopper pays in. The following additional fields are returned on orders when Multi-Currency is enabled on the store: * `store_default_currency_code` - the currency code of the store's default currency. * `store_default_to_transactional_exchange_rate` - the exchange rate between the store's default currency and …

**Citation Q7-BC-C026:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/orders.md` | ### Currency Fields | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/031-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:19:46Z, captured)
- quote: * `default_currency_id` - the transactional currency ID.
- title, opening and note boxes: as for this source's citation above
- headings: Orders V2 > Order > Currency Fields
- in context: …* `currency_code` - the currency code of the display currency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency. * `currency_exchange_rate` - the exchange rate between the store's default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1). ⟪* `default_currency_id` - the transactional currency ID.⟫ * `default_currency_code` - the currency code of the transactional currency the shopper pays in. The following additional fields are returned on orders when Multi-Currency is enabled on the store: * `store_default_currency_code` - the currency code of the store's default currency. * `store_default_to_transactional_exchange_rate` - the exchange rate between the store's default currency and the transactional currency used in the order. **Example:*…

**Citation Q7-BC-C027:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/orders.md` | ### Currency Fields | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/031-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:19:46Z, captured)
- quote: * `default_currency_code` - the currency code of the transactional currency the shopper pays in.
- title, opening and note boxes: as for this source's citation above
- headings: Orders V2 > Order > Currency Fields
- in context: …ency used to present prices to the shopper on the storefront. Depending on the currency selected, the value may be different from the transactional currency. * `currency_exchange_rate` - the exchange rate between the store's default currency and the display currency. For orders created using the V2 endpoints, this value is always 1 (only in the storefront this value can be different to 1). * `default_currency_id` - the transactional currency ID. ⟪* `default_currency_code` - the currency code of the transactional currency the shopper pays in.⟫ The following additional fields are returned on orders when Multi-Currency is enabled on the store: * `store_default_currency_code` - the currency code of the store's default currency. * `store_default_to_transactional_exchange_rate` - the exchange rate between the store's default currency and the transactional currency used in the order. **Example:** ```json { ... "currency_id": 4, "currency_code": "EUR", "currency_exchange_rate": 1, "default_c…

### Q7-BC-P0015

**Cited at:** section 1, line 20; section 2, line 75; section 3, line 96; section 3, line 100; section 3, line 104; section 7, line 148

**Record** (`studies/proposals/records/Q7/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-014
- bullet: d;end-payment;end-payout
- placement: responsible
- identifier: Multi-currency definitions: Settlement Currency
- statement: If there's a discrepancy between the currency that a shopper transacts in and the currency in which a merchant settles, the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope.
- cite_ids: S01-BC-C015
- from: new

**Citation S01-BC-C015:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/currencies/overview.md` | ## Multi-currency definitions: Settlement Currency | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/073-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:28Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/006-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T10:49:41Z, captured)
- quote: If there's a discrepancy between the currency that a shopper transacts in and the currency in which a merchant settles, the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope.
- title: Currencies Overview
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. BigCommerce's flexible Currency settings assist developers in building Multi-Currency storefronts that empower shoppers and merchants to do business in their currency of choice. Allowing customers to …
- headings: Currencies Overview > Multi-currency definitions
- in context: …mprised of the currency and amount, the transactional currency is what BigCommerce passes to the payment provider and what is charged to a shopper's bank account. If there's a discrepancy between the storefront active currency and the transactional currency, a shopper has to pay a conversion fee and the conversion rate used is outside of BigCommerce's scope. | | Settlement Currency | The currency the merchant gets paid out to their bank account. ⟪If there's a discrepancy between the currency that a shopper transacts in and the currency in which a merchant settles, the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope.⟫ The merchant can set their settlement currency through its payment provider. | | BigCommerce Conversion Rate | Any conversion rate set on BigCommerce used to convert the product's default currency pricing into a new non-default currency. The conversion rate can be static or dynamic. | | Static Conversion Rate | One of the two auto-converted pricing options. If a merchant manually enters a static conversion rate, then the conversion rate will rem…

### Q7-BC-029

**Cited at:** section 1, line 27; section 2, line 62; section 2, line 64; section 3, line 92

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-029
- bears_on: 2
- identifier: Setup
- statement: When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live.
- cite_ids: Q7-BC-C038
- from: held

**Citation Q7-BC-C038:** `https://support.bigcommerce.com/s/article/Managing-Currencies` | Adding a Currency: SETUP | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/033-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:40:36Z, captured)
- quote: When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …n order to manage the currency settings in your store, you must have the Manage Settings permission enabled on your user account. This is enabled by default for users with the Store Administrator or Store Owner role. To learn more about the requirements for offering multiple transactional currencies in your store, see Using Multiple Currencies. Adding a Currency Setup Currency display configurations Transactions Additional display settings SETUP ⟪When you first create your store, your default currency is assigned based on your location. You can enable additional currencies to display prices and allow transactions where your frequent customers live.⟫ If a currency code is already set up, it will not be available in the list of currency codes when setting up a new currency. Existing currencies can be edited at any time. Use the following steps to add a currency. Localized Store Experiences: Local currency tokens are available for display in all of our supported languages. For more information on the default language store setting, see Store Profile Settings. 1. Go to Settings › Currencies, th…

### Q7-BC-P0016

**Cited at:** section 1, line 31; section 2, line 77; section 3, line 88; section 3, line 96; section 5, line 123; section 7, line 146; section 8, line 159

**Record** (`studies/proposals/records/Q7/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-015
- bullet: a;end-payout
- placement: decides
- identifier: Settlement Currency
- statement: The merchant can set their settlement currency through its payment provider.
- cite_ids: S01-BC-C016
- from: index:BC-C-074:BC-S-0403

**Citation S01-BC-C016:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/currencies/overview.md` | ## Multi-currency definitions | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/073-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:28Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/006-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T10:49:41Z, captured)
- quote: The merchant can set their settlement currency through its payment provider.
- title: Currencies Overview
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. BigCommerce's flexible Currency settings assist developers in building Multi-Currency storefronts that empower shoppers and merchants to do business in their currency of choice. Allowing customers to …
- headings: Currencies Overview > Multi-currency definitions
- in context: … and the transactional currency, a shopper has to pay a conversion fee and the conversion rate used is outside of BigCommerce's scope. | | Settlement Currency | The currency the merchant gets paid out to their bank account. If there's a discrepancy between the currency that a shopper transacts in and the currency in which a merchant settles, the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope. ⟪The merchant can set their settlement currency through its payment provider.⟫ | | BigCommerce Conversion Rate | Any conversion rate set on BigCommerce used to convert the product's default currency pricing into a new non-default currency. The conversion rate can be static or dynamic. | | Static Conversion Rate | One of the two auto-converted pricing options. If a merchant manually enters a static conversion rate, then the conversion rate will remain the same until and unless the merchant updates their currency settings to…

### Q7-BC-053

**Cited at:** section 1, line 38; section 2, line 82

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-053
- bears_on: 3
- identifier: Adding a currency: Note
- statement: For instance, changing the default currency will not trigger price recalculation for the catalog.
- cite_ids: Q7-BC-C064
- from: held

**Citation Q7-BC-C064:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/currencies/overview.md` | ## Adding a currency: Note | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/073-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:28Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/006-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T10:49:41Z, captured)
- quote: For instance, changing the default currency will not trigger price recalculation for the catalog.
- title: Currencies Overview
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. BigCommerce's flexible Currency settings assist developers in building Multi-Currency storefronts that empower shoppers and merchants to do business in their currency of choice. Allowing customers to …
- headings: Currencies Overview > Adding a currency
- in context: …ency code that corresponds to the currency you want to set up, then click **Next**. 3. Configure the currency's display and transactional settings. 4. Click **Save**. For more in-depth instructions and helpful screenshots, see [Adding a Currency](https://support.bigcommerce.com/s/article/Managing-Currencies-Beta#add) in the Help Center. > **Note** > > Do not change the default currency -- this may lead to unintended currency conversion issues. > ⟪For instance, changing the default currency will not trigger price recalculation for the catalog.⟫ > Additionally, changing the default currency will enable the newly assigned currency as transactional. ## How currencies work For details on how currencies are surfaced throughout BigCommerce APIs, user interfaces, and storefront components, see [How Currencies Work](/developer/docs/admin/store-configuration/currencies/how-currencies-work) ## Supported and unsupported features See the table below for a list of supported and unsupported features…

### Q7-BC-035

**Cited at:** section 1, line 42; section 2, line 74; section 3, line 89; section 7, line 151

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-035
- bears_on: 2;3
- identifier: Dynamic Conversion Rate
- statement: The merchant can either use BigCommerce Currency Service provided in the Currency setup page, or they can use the API to automatically update the exchange rate from their trusted source.
- cite_ids: Q7-BC-C044
- from: held

**Citation Q7-BC-C044:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/currencies/overview.md` | ## Multi-currency definitions: Dynamic Conversion Rate | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/073-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:28Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/006-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T10:49:41Z, captured)
- quote: The merchant can either use BigCommerce Currency Service provided in the Currency setup page, or they can use the API to automatically update the exchange rate from their trusted source.
- title: Currencies Overview
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. BigCommerce's flexible Currency settings assist developers in building Multi-Currency storefronts that empower shoppers and merchants to do business in their currency of choice. Allowing customers to …
- headings: Currencies Overview > Multi-currency definitions
- in context: …ntly fluctuating prices in non-default currencies. | | Dynamic Conversion Rate | One of the two auto-converted pricing options. If a merchant selects a dynamic conversion rate, they've tied themselves to a currency-conversion service, which will update the conversion rate at a certain frequency. This helps shopper-facing pricing remain most aligned to the store's default currency and keeps the non-default currency conversion rate at market rate. ⟪The merchant can either use BigCommerce Currency Service provided in the Currency setup page, or they can use the API to automatically update the exchange rate from their trusted source.⟫ | | Bank Conversion Rate | Conversion rate is used by merchants' or shoppers' payment or credit card providers when auto-converting from store's transactional currency. This rate might not align with the BigCommerce conversion rate, and BigCommerce has no visibility into it. | | Multi-Currency Pricing | Rather than opting for auto-converting product pricing from default currency using the BigCommerce Conversion Rate, the merchant has a choice to…

### Q7-BC-058

**Cited at:** section 1, line 50; section 1, line 53; section 2, line 78; section 3, line 99; section 8, line 159

**Record** (`studies/proposals/records/Q7/bigcommerce/statements.tsv`):
- stmt_id: Q7-BC-058
- bears_on: 4
- identifier: MANAGING CURRENCIES AND CONVERTING BALANCES
- statement: In the Currencies section, you can view and manage your configured currencies, as well as the existing balance per currency.
- scope: BigCommerce Payments
- cite_ids: Q7-BC-C069
- from: held

**Citation Q7-BC-C069:** `https://support.bigcommerce.com/s/article/Connecting-with-BigCommerce-Payments?language=en_US` | Balance dashboard: MANAGING CURRENCIES AND CONVERTING BALANCES | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/016-support.bigcommerce.com/text.txt` (fetched 2026-10-13T00:35:36Z, captured)
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:39:50Z, captured)
- quote: In the Currencies section, you can view and manage your configured currencies, as well as the existing balance per currency.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: … bank. Quickly link your account using Mastercard Data Connect or manually by entering your account details. Note that manual connection can take up to three business days to complete. If your bank cannot be found in the search results, you can also manually enter your bank details. You can also perform these functions directly in your PayPal dashboard by clicking Manage banks from your PayPal account. MANAGING CURRENCIES AND CONVERTING BALANCES ⟪In the Currencies section, you can view and manage your configured currencies, as well as the existing balance per currency.⟫ Expand your primary currency to view the linked bank account and set up automatic payouts to your bank or PayPal account. On the right side of the section, you can perform currency and balance actions, such as using the currency calculator to review balance exchanges, add additional currencies, mark a currency as primary, remove (close) a currency, and convert existing balances from one currency to another. To change existing balance from one en…

### Q7-BC-K0177

**Cited at:** section 7, line 149

**The same record as Q1-BC-K0177,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Fees are payable in U.S. Dollars, unless otherwise specified.
- scope: 

### Q7-BC-P0014

**Cited at:** section 8, line 159

**Record** (`studies/proposals/records/Q7/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-013
- bullet: end-payout
- placement: where
- identifier: Multi-currency definitions: Settlement Currency
- statement: The currency the merchant gets paid out to their bank account.
- cite_ids: S01-BC-C014
- from: new

**Citation S01-BC-C014:** `https://docs.bigcommerce.com/developer/docs/admin/store-configuration/currencies/overview.md` | ## Multi-currency definitions: Settlement Currency | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/073-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T04:20:28Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/006-docs.bigcommerce.com/text.txt` (fetched 2026-10-12T10:49:41Z, captured)
- quote: The currency the merchant gets paid out to their bank account.
- title: Currencies Overview
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. BigCommerce's flexible Currency settings assist developers in building Multi-Currency storefronts that empower shoppers and merchants to do business in their currency of choice. Allowing customers to …
- headings: Currencies Overview > Multi-currency definitions
- in context: …ency" in the payments industry. | | Transactional Currency | Comprised of the currency and amount, the transactional currency is what BigCommerce passes to the payment provider and what is charged to a shopper's bank account. If there's a discrepancy between the storefront active currency and the transactional currency, a shopper has to pay a conversion fee and the conversion rate used is outside of BigCommerce's scope. | | Settlement Currency | ⟪The currency the merchant gets paid out to their bank account.⟫ If there's a discrepancy between the currency that a shopper transacts in and the currency in which a merchant settles, the merchant has to pay a conversion fee, and the conversion rate used is outside of BigCommerce's scope. The merchant can set their settlement currency through its payment provider. | | BigCommerce Conversion Rate | Any conversion rate set on BigCommerce used to convert the product's default currency pricing into a new non-def…
