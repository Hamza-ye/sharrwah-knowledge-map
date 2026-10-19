# Notes: Q1, shopify

## What was read

All of it was held, at observed-sh `c8b5fbee25966372a0475e6ed81f0b7760ac2921`. No live page was read.

- Help Center pages, through `method/help_map.py` (English):
  - markets/customizations/overview;
  - markets/getting-started/overview, market-types, set-up-markets, requirements-and-considerations, localization and submarkets (submarkets was opened and skimmed, and added nothing new);
  - markets/customizations/local-currencies and business-entities;
  - international/payments;
  - international/pricing/supported-currencies;
  - payments/third-party-providers, plus its configuring-providers and payment-gateway-availability pages.
- Fetch-archive records, through `method/warc_text.py`:
  - shopify.dev ShopFeatures.md (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@8632954`);
  - www.shopify.com/international/managed (`raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz@17135260`);
  - www.shopify.com/payment-gateways (`…/fetch.warc.gz@41642451`);
  - the changelog post on multi-currency payouts in Australia and France (`raw/runs/20261007T071251Z-published-changelog-posts/fetch.warc.gz@267183`).
- `structures/shopify/shop-request-details/<store>/items.jsonl` for all 14 stores. These were read for the nine feature keys the coordinator named: perMarketIncoterms, landedCostIncoterms, multiCurrencyGatewayEnabled, subCountryMarketsEnabled, marketDeliveryProfiles, managedMarkets, usingMarketsPro, catalogRolloutsEnabled and threeDSecureEligibilityForCountry. `meta.json` and `sets.jsonl` were read for capture-gb-plus.

## How the store-feature statements are built

- There is one statement per key and value: Q1-SH-081 to Q1-SH-091.
- Each statement's text is the first store's JSON line.
- Its scope lists every store and set with that value.
- Each store is cited at the first set where it has that value.
- `marketDeliveryProfiles` appears only for store zyd38b-ze.
- Some stores lack some keys at some sets. For example, perMarketIncoterms is absent at 2jiwxs-gr set 1.

## What couldn't be read

- The payment-gateways page's filter by country. The held text stops before any country is chosen (Q1-SH-N03).
- Each captured store's country. RequestDetails doesn't hold it, and admin Settings > General isn't held (Q1-SH-N04, routed to the founder).

## Copies

- No copy was found wrong.
- Q1-SH-071, from www.shopify.com/international/managed, states Managed Markets eligibility in different words from Q1-SH-K1956. The managed page says "based in the United States, Canada, or the United Kingdom". The Help Center copy says "continental United States, and to certain stores in Canada and the United Kingdom".

## Problems with the method

- Two quotes failed at first because the source puts a sentence's closing period right after a `</strong>` or `</a>` tag. The quote check then doesn't match the period. Those two statements end just before the period: Q1-SH-065 and Q1-SH-070.
- Each Help Center citation carries the REGISTER date-seen for help-center, 2026-10-16, since the pages are undated.
- One corpus search ran past the 120-second tool timeout and finished in the background.
- The brief asks for help pages to be cited by "the source help_map.py prints". Those sources were used as given.

## Re-check against the observed runs, 19 October 2026

All reading was held, at observed-sh `c8b5fbee25966372a0475e6ed81f0b7760ac2921`, read with `git --git-dir=/home/user/observed-sh/.git show` from outside the repository.

### What was read

- The guides `README.md` and `docs/READING.md`, whole.
- Searches, each with `python3 -I method/corpus_search.py shopify … --max 10`:
  - for Q1-SH-N01: `perMarketIncoterms landedCostIncoterms multiCurrencyGatewayEnabled marketDeliveryProfiles managedMarkets usingMarketsPro catalogRolloutsEnabled threeDSecureEligibilityForCountry`;
  - for Q1-SH-N02: `"now available in" "newly supported countries" "expanding to" "متاح الآن في" --with "Shopify Payments" "شوبيفاي للمدفوعات"`;
  - for Q1-SH-N03: `"Third-party payment providers" PaymentProviders "Choose a provider" "مزودي الدفع التابعين لجهات خارجية"`;
  - for Q1-SH-N04: `billingAddress "Store address" "Billing address" "عنوان المتجر" "عنوان الفوترة" --with capture-gb-plus capture-grow 2jiwxs-gr`;
  - for the copied gaps on the party responsible (Q1-SH-G0133, G0135, G0138, G0139, G0141): `"Business entity used for" "merchant of record" "responsible for" "the entity that" "الكيان التجاري" "التاجر المسجل" --with Markets currency Rollouts "Backup region" domains`;
  - for Q1-SH-G0132 (a stated reason): `"Markets is" because "so that you can" "لأن" --with Markets "الأسواق"`.
- The pointers: the answers of `PaymentProviders`, `ShopifyPaymentsData` and `MarketsHomeCurrencyOptions`, and each store's General settings page in the sweeps and journeys.
- Run files opened:
  - `raw/runs/20261005T002448Z-journey-dev-store-region/`: `actions.jsonl`, `steps/001.text.txt` to `006.text.txt`, `answers.jsonl`, and the `PaymentProviders` and `ShopifyPaymentsData` answers of step 6;
  - `raw/runs/20261005T013804Z-sweep-paid-store/`: `steps/170.text.txt`, `steps/387.text.txt`, `answers.jsonl`, and the `ThirdPartyPaymentProviders` answer of step 387;
  - `raw/runs/20260930T002940Z-sweep-trial/steps/387.aria.yaml`, and step 387 of the sweeps `20260930T045741Z-sweep-trial2`, `20260930T103225Z-sweep-dev`, `20261002T003831Z-sweep-capture-plus`, `20261002T003931Z-sweep-capture-advanced` and `20261002T004032Z-sweep-capture-grow` (`.aria.yaml`);
  - `raw/runs/20261002T004032Z-sweep-capture-grow/`: the `MarketsHomeCurrencyOptions` answer of step 308, and the `BillingAddress` answer the N04 search listed;
  - `raw/runs/20260930T170204Z-journey-market/`: `actions.jsonl` and `steps/006.aria.yaml`;
  - `raw/runs/20261005T003901Z-journey-vantage/`: `actions.jsonl`, and `steps/002`, `003`, `006`, `009`, `014`, `015`, `016` and `017` `.text.txt`;
  - for Q1-SH-N01, the three answers named in its `read`;
  - `derived/admin-operations.jsonl`, for the queries `ThirdPartyPaymentProviders` and `MarketsHomeCurrencyOptions`;
  - `index/operations.jsonl`, for the runs and stores that called the pointed operations.
- Read by a script in the scratch directory, which printed only the keys named here:
  - every run's `actions.jsonl`, for the steps whose page ended at `/settings/general`, with the "Store address" lines of those steps' files. 121 steps across 9 stores. Each that shows an address shows Yemen, or "Sanaa, Yemen" for fake-demo-sharrwah from 5 October 2026;
  - every held `PaymentProviders` answer (222) and `ShopifyPaymentsData` answer (53): `countryCode`, `currencyCode`, Shopify Payments' `eligible`, and the names of the third-party providers. Every one gives `"countryCode":"YE"` and `"currencyCode":"YER"`, and every `ShopifyPaymentsData` answer gives `"eligible":false`;
  - every held `RequestDetails` answer (7,596): `billingAddress` and `shop.currencyCode`. capture-plus-dev's give `"countryCodeV2":"US"` and `"currencyCode":"USD"`. All the others give `"YE"` and `"YER"`.
- Also seen in those answers:
  - the `RequestDetails` answers for ctcbwa-r1 and fake-demo-sharrwah carry the same shop id, `gid://shopify/Shop/84760363223`;
  - those for hjhjhjjjhj and zyd38b-ze carry the same shop id, `gid://shopify/Shop/82604425462`;
  - one answer, in run `20261007T174307Z-sweep-staff-pos-user-administrator`, names no store and was not used.
- The `MarketsHomeCurrencyOptions` answer's `currencies` list holds 130 items. Only the item YER was recorded (Q1-SH-105).
- The region list of the New market condition picker (journey-vantage step 9) holds 245 lines. It was not recorded.

### Open items

- Q1-SH-N04 is closed by Q1-SH-092 and Q1-SH-093, and moved to `not-found-closed.tsv`. The admin's RequestDetails answer itself holds `billingAddress.countryCodeV2` beside the feature values. The structure's `items.jsonl` doesn't hold it. Its route to the founder (Settings > General) is no longer needed: the runs hold that page for 9 stores (Q1-SH-101).
- Q1-SH-N03 is narrowed. The runs show the providers the admin listed to Yemen-address stores (Q1-SH-103, with Q1-SH-094 to Q1-SH-097). What is still missing: every other country or region.
- Q1-SH-N01 is unchanged. The answers the search listed give the keys' values, not what they govern. The search and the answers read were added to the row.
- Q1-SH-N02 is unchanged. The run documents the search listed are `AnalyticsSchemas` answers. Their snippets match "expanding to new markets" in a report field's text. None was opened.
- The copied gaps Q1-SH-G0132, G0133, G0135, G0138, G0139 and G0141 are unchanged:
  - the run documents the responsibility search listed are consent labels, theme translations, and the Policies pages' "you are responsible for ensuring they are accurate and comply with applicable laws";
  - those the reason search listed are `Feed` answers and notification previews.

  None bears on the gaps, and none was opened.
- The coordinator listed no phrases for this folder.

### Wording check

- The rows that stay are Q1-SH-N01, N02 and N03.
- Each name, path or phrase they give as Shopify's is in what their `read` names or in this folder's records. The phrase "Payment information by country or region" in Q1-SH-N03 was checked in the payment-gateways record (`fetch.warc.gz@41642451`, through `method/warc_text.py --text`).
- No wording was changed.

### New statements

- There are 16 new statements, Q1-SH-092 to Q1-SH-107, with citations Q1-SH-C192 to Q1-SH-C229.
- For each store, Q1-SH-092 cites one `RequestDetails` answer: the earliest that a step called, or, for the import run's stores, the earliest call.
- For the import run (`20260930T003329Z-pilot-import`), a call has no step. Its locator and date basis give the call's time instead.
- The market name "Capture UK" in Q1-SH-107 was typed in the run.

### Not read

- The sweeps' other Markets pages (`/markets`, `/markets/<id>`, `/markets/managed…`).
- The journey `20260930T014656Z-journey-order-lifecycle`.
- The third-party provider detail pages (`/settings/payments/third-party-providers/24`, `/41156609`).
- The rest of `20260930T170204Z-journey-market` beyond step 6.

### Problems

- Each corpus search took several minutes while other runs searched at the same time.
- The brief caps a search at 3 run documents, but the pointers (each store's General settings page, and the answers of the three operations) cover many files. They were read by script for the keys named above, and only the files cited were read whole.
