# Notes: Q7 on Shopify

## Selection
16 rows copied: SH-C-005, 037, 064, 065, 069, 070, 079, 080, 081, 106, 107, 108, 109, 110 and 111, plus S-01. 48 rows set aside, with their reasons in `selection.tsv`. The judgement used each concern's terms, and `copy_statements.py show` for the concerns whose terms didn't decide it (SH-C-054, 057, 005, 062, 076, 112, 113 and 016). A count of currency words across every candidate's statements was also run. The copy step wrote 214 statements, 15 gaps, 161 pilot statements, 0 pilot gaps and 2 pilot absences.

## What was read (all held; no live page was read)
All Help Center pages were read in English, through `method/help_map.py shopify page`, from observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:

- Pages from the map (menus Payments 7659, International sales tools 12041, Markets 12382):
  - payments/shopify-payments/store-currency/understanding-store-and-payout-currencies
  - changing-your-store-currency
  - selling-and-getting-paid-in-different-currencies
  - supported-payout-currencies
  - payouts-in-multiple-currencies
  - markets/customizations/local-currencies
  - international/pricing/refunds
  - international/pricing/limitations
  - international/pricing/primary-gateway-support
  - international/pricing/supported-currencies
  - payments/paypal/multicurrency
  - markets/bulgaria-currency-transition
- Pages opened from corpus searches:
  - fulfillment/managing-orders/create-orders/international-drafts
  - fulfillment/managing-orders/managing-order-details (only the section "Check an order's currency")
  - markets/customizations/business-entities
  - intro-to-shopify/initial-setup/setup-business-settings (only the section "Select a store currency")
  - international/managed-markets/overview and international/managed-markets/shopify-payments (only the lines with currency, flow of funds and payouts)
  - payments/shopify-payments/payouts/reserves, view-details, lower-or-missing-payouts, payout-timing and onboarding/bank-account-requirements (only the lines with "currenc" or "USD")
- Admin GraphQL schema 2026-10 (`structures/shopify/admin-graphql-schema/2026-10/items.jsonl`): the types MoneyBag, Order, Shop, CurrencySetting, MarketCurrencySettings, PriceList, ShopifyPaymentsAccount, ShopifyPaymentsBalanceTransaction, ShopifyPaymentsBankAccount and ShopifyPaymentsPayout. Their currency fields have no description in this structure, so they are recorded as their JSON field lines.
- Store request details (`structures/shopify/shop-request-details/<store>/items.jsonl` and `sets.jsonl`): the `features` key `multiCurrencyGatewayEnabled` on capture-plus, capture-grow, ibx5bt-xy, zyd38b-ze and ts15uk-ug.
  - Only capture-plus, capture-grow and ibx5bt-xy are recorded. On zyd38b-ze and ts15uk-ug every set reads `false`.
  - The other keys in the brief's pointer (`perMarketIncoterms`, `landedCostIncoterms`, `subCountryMarketsEnabled`, `marketDeliveryProfiles`, `managedMarkets`, `usingMarketsPro`, `catalogRolloutsEnabled`, `threeDSecureEligibilityForCountry`) were seen but not recorded. Their names don't name a currency.
- The Shopify Payments terms capture: sharrwah-knowledge-map evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt (https://www.shopify.com/legal/terms-shopify-payments). Only its sentences containing "currenc" were read.

## Tables recorded row by row
- "Payout currencies you can use based on your Shopify Payments region": all 39 rows (Q7-SH-018 to Q7-SH-056).
- "ISO country codes for currencies accepted on Shopify Payments through multi currency": all 44 rows (Q7-SH-136 to Q7-SH-179).
- "Payment methods for Shopify Payments" (local pricing support): all 11 rows (Q7-SH-089 to Q7-SH-099).

## Tables not recorded
- The bank account requirements table on onboarding/bank-account-requirements: currency by country, more than 20 rows.
- The Multi-Currency Payouts tables "Shopify plan eligibility", "Bank account requirements by business entity location" and "Payout routing".
- The conversion fee table by store location on markets/customizations/local-currencies.
- The Managed Markets local payment method tables (US, UK, Canada), which have a Currency column.

## Copies that differ from what was read
Copy Q7-SH-K1936 (account-setup page) says to contact Shopify Support to change the store currency after the first sale. Two pages read say otherwise:
- changing-your-store-currency says only the store owner can change it, from Settings > General (Q7-SH-008);
- setup-business-settings gives the steps for a change after the first order, which add a check of "I understand the risk of changing the store currency" (Q7-SH-181).

Both statements name K1936 in their note.

## Problems with the method
- Some statements first combined quotes from places in a page that aren't next to each other. The checker rejects a statement that isn't verbatim in its first cited source, so each of those quotes became its own statement. One list statement, Q7-SH-059, now includes a "Learn more" sentence that sits between two of its items.
- Some quotes ran past 300 characters. They were split into consecutive pieces, each cited separately.

## Re-check against the observed runs, 19 October 2026

All files below were read from observed-sh at commit c8b5fbee25966372a0475e6ed81f0b7760ac2921, with `git show`.

### What was read
- The guides: `README.md` and `docs/READING.md`, whole.
- Searches (`python3 -I method/corpus_search.py shopify … --max 10`):
  - N01: "Reserved funds" "reserve" "Payout balance" "الأموال المحجوزة" "الاحتياطي" --with "currency" "USD" "عملة";
  - N02: "existing orders" "past orders" "previous orders" "الطلبات السابقة" "الطلبات الحالية" --with "currency" "currencies" "عملة" "العملة";
  - N03: "Change store currency" "Store currency" "I understand the risk of changing the store currency" "تغيير عملة المتجر" "عملة المتجر";
  - N04: "Global-e" "Managed Markets" "Global-e account" "الأسواق المُدارة" "Managed markets" --with "currency" "currencies" "عملة" "العملة";
  - sentence 1: "presentmentCurrencyCode" "presentmentMoney" "shopMoney" "Currency display" "عرض العملة";
  - sentence 2: "Local currencies" "baseCurrency" "localCurrencies" "enabledPresentmentCurrencies" "العملات المحلية";
  - sentence 3: "Change currency" "Manage currencies" "Exchange rate" "تغيير العملة" "سعر الصرف" --with "market" "Markets" "الأسواق";
  - sentence 4: "Payout currency" "payout account" "defaultCurrency" "عملة الدفع" "عملة المدفوعات".
- `python3 -I method/held_index.py` on https://admin.shopify.com/payments/payouts, /settings/general and /settings/payments.
- Run files opened:
  - raw/runs/20261005T013804Z-sweep-paid-store/steps/170.text.txt (General settings, fake-demo-sharrwah);
  - raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/170.text.txt (General settings, ts15uk-ug) and steps/450.text.txt (gift card product);
  - raw/runs/20261002T003831Z-sweep-capture-plus/steps/170.aria.yaml (General settings), and its answers MarketsHomeCurrencyOptions/c0db7883….json and ShopifyPaymentsData/383a6cb4….json, with its `answers.jsonl` and `actions.jsonl`;
  - raw/runs/20260930T113624Z-journey-giftcard-product/steps/002.aria.yaml;
  - raw/runs/20260930T170204Z-journey-market/steps/099.aria.yaml and 089.aria.yaml;
  - raw/runs/20260930T014656Z-journey-order-lifecycle: `answers.jsonl`, the answers SuggestedFinancialOutcomeQuery/6e6d198f….json, OrderDetailsPayment/72ab439f….json and OrderDetails/9dcdca0a….json (the last two hold no currency beyond YER amounts and were not recorded);
  - raw/runs/20261005T035526Z-sweep-staff-customer-support/steps/397.text.txt (payouts page);
  - `derived/admin-operations.jsonl` (the query of MarketsHomeCurrencyOptions) and `index/operations.jsonl` (the runs calling the pointer operations).
- Stores: each store is named as the run's `answers.jsonl` names it. Run 20261005T013804Z-sweep-paid-store names two stores (fake-demo-sharrwah and ctcbwa-r1); Q7-SH-191 names fake-demo-sharrwah from its step's address.
- The `MarketsHomeCurrencyOptions` answer's `currencies` list holds 130 items. Only the YER item is recorded (Q7-SH-194); the shop's own currency is YER.

### Open items
- Q7-SH-N01: unchanged. No run shows the payouts page to the store owner: its held steps are staff sweeps that show "You need permission to view this feature". Search and file added to the row.
- Q7-SH-N02: unchanged. Search added to the row.
- Q7-SH-N03: unchanged. The held General settings steps show the **Store defaults** section with "Yemeni Rial (YER)" (recorded as Q7-SH-191), but no step opens the Change store currency menu. Search, files and a narrowed route added.
- Q7-SH-N04: unchanged. Search and file added to the row.
- No copied gap is cited in the account. The starting message listed no phrases.

### Wording changes (step 4)
- Every name kept in the rows ("Reserved funds", "Payout balance", "Payment Processor Account", "Store defaults", "Currency display", "Change store currency", "drop-down menu", "Global-e account", "currency customization") is in a page the row's `read` names. No detail was removed.
- Routes of N01 and N03 no longer give an admin address (see problems).

### New statements
Q7-SH-191 to Q7-SH-200 (10), with citations Q7-SH-C216 to Q7-SH-C228.

### Not read
- The answers of `PaymentProviders` and the third-party payment providers pages (pointers): they name providers, not currencies, and were not opened.
- The other run documents the sentence searches listed (MarketsPicker, MarketGraphProductPricingDetail and DraftOrderMarkets answers, other journey-market steps, staff sweeps' General settings steps, Shopify Payments terms steps, AnalyticsShopifyQl answers).

### Problems with the brief or the tools
- The checker reports a founder route whose address any held step holds, even where the held steps show a different state of the page (a staff permission page, or a menu left closed). For N01 and N03 the route now names the page in the Help Center's words instead of its address, and says what the held steps show.
