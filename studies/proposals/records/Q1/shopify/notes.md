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

## Re-check against the step text from saved HTML, 19 October 2026

Everything read was observed-sh `51626891aa711ee9c3ef2d05ce63c95396dca949`, `derived/step-text-from-html/`, with the runs' `actions.jsonl` and `answers.jsonl` (for the store each run names) and, for the steps cited, `steps/NNN.aria.yaml`, all read with `git --git-dir=/home/user/observed-sh/.git show` from outside the repository.

### What was read

- observed-sh's `docs/READING.md`, the folder's entry, and the folder's `meta.json`.
- Searches, each `python3 -I method/corpus_search.py shopify … --only "step text from saved HTML" --max 10`:
  - Q1-SH-N01: `perMarketIncoterms landedCostIncoterms multiCurrencyGatewayEnabled marketDeliveryProfiles managedMarkets usingMarketsPro catalogRolloutsEnabled threeDSecureEligibilityForCountry Incoterms` (no document matched);
  - Q1-SH-N02: `"now available in" "newly supported countries" "expanding to" "coming soon to" "not available in your country" "متاح الآن في"` (one report page, not opened);
  - Q1-SH-N03: `"Payment information by country or region" "available in your country" "Supported countries" "Choose a provider" "اختيار مزود" --with Yemen YE "اليمن"` (no document matched), then without `--with`, adding `"available in your region" "غير متاح في بلدك"`;
  - the copied gaps: `"Business entity used for" "merchant of record" "responsible for" "Backup Region" "Rollouts" "الكيان التجاري" "التاجر المسجل"`, then with `"is responsible for" "you are responsible" "مسؤول عن"` in place of `"responsible for" "Rollouts"`;
  - for the draft's ids and the question's sentences: `"Create market" inherits Inherited Customized "backup region" "Parent market" Sub-region "can browse your store" "إنشاء سوق" "موروث"`; `"Managed Markets" "Global-e" "merchant of record" "without registering a business" "الأسواق المُدارة"`; `"Create United States Market" "Create United Kingdom Market" "Create European Union Market" "Learn more about markets" International Domestic`; `"Business entity used for" "Store currency" "Store address" "Backup region" "change your store currency" "Manage entities" "عملة المتجر"`; `"Automatic redirection" "redirect customers" geolocation "IP address" "can't complete a purchase" "won’t be able to check out"`; `"Shopify Balance" "not available in your country" "isn't available in your country" "not available in your region" "isn’t available in your region" Stripe`; `"Local payment methods" "states or provinces" province Sub-region`; `"available in your country" "available in your region" "not yet available" "isn't available in" "only available in" "available to merchants in" "unsupported country" "غير متوفر في"` (no document matched); `"View markets" "Create and edit markets" "Manage markets" "Markets permissions" "Edit markets"`; `"per market" "theme customization" "Advanced plan" "Business entities" "Plus plan"`.
- Texts opened (`<run>/NNN.html.txt`):
  - `20260930T170204Z-journey-market/`: 001, 002, 005, 007, 017, 020, 023, 046, 048, 049, 077, 088, 089, 090;
  - `20261004T223401Z-journey-business-entity/`: 001, 013, 014, 031, 034, 051, 052, 070;
  - `20261004T092557Z-sweep-instances/060.html.txt`;
  - `20260930T045741Z-sweep-trial2/376.html.txt`;
  - `20261002T004032Z-sweep-capture-grow/`: 316, 376, 377, 414, 419;
  - `20261002T003831Z-sweep-capture-plus/416.html.txt` and `416.frame-1.html.txt` (empty).
- `steps/NNN.aria.yaml` of each step a new statement cites, and of journey-market 007 and 089, for whether the tree shows the same words.

### Open items

- Q1-SH-N01, N02 and N03 are unchanged. Their searches, and for N03 the step opened, were added to the rows. Sweep-trial2 step 376 (Q1-SH-123) is one more Yemen-address store's Payments page; no text shows another country's providers.
- The copied gaps Q1-SH-G0132, G0133, G0135, G0138, G0139 and G0141 are unchanged. The searches listed the Rollouts navigation, the General page and privacy policy pages ("Shopify is responsible for the processing of your personal information"); none names a party responsible for these settings.
- No row is routed to the founder or to either.

### Wording check

- The rows that stay, Q1-SH-N01 to N03, gained no new name, path or phrase. No wording was changed.

### New statements

- 16 new statements, Q1-SH-108 to Q1-SH-123, with citations Q1-SH-C230 to Q1-SH-C246. Each says in its `note` that it is in the saved HTML of its step, and whether the step's `aria.yaml` shows the same words.
- Q1-SH-116, 118, 119, 121 and 122 are words the step's `aria.yaml` doesn't show. Q1-SH-118, 119 and 121 sit in dialogs' markup, not marked hidden; nothing in the files shows whether those dialogs were open.
- No text between `⟦hidden⟧` and `⟦/hidden⟧` was recorded.
- Lists not recorded in full: the market currency picker's "All currencies" (about 130 items, journey-market step 20), the General page's Store currency list (about 160 items, journey-business-entity step 14), and its Time zone list.
- Names typed in the runs: "Capture market" (journey-market) and "Capture Entity" (journey-business-entity, steps 11 and 12).
- Stores as `answers.jsonl` names them: demo-fake-dev-store (journey-market), capture-advanced (journey-business-entity), capture-grow (sweep-instances `20261004T092557Z`), ibx5bt-xy (sweep-trial2).

### Read and found the same as recorded

- The admin's Shopify Payments Terms page (sweep-capture-plus step 416) holds the text that Q1-SH-K1536 and Q1-SH-K1614 copy from the published terms, and Part II's regions Australia, Canada, United Kingdom and United States. It doesn't hold Q1-SH-K1604's sentence, which is copied from another page (terms-payfac).
- The Managed Markets routes of the sweeps (steps 311 to 316) held the Markets list, not a Managed Markets page.
- The Plus trial page (sweep-capture-grow step 419) lists "Localized selling with Shopify Markets" and "Accept local payment methods*" as "Feature enabled" in both of its columns. Its footnote for "*" isn't in the text. Not recorded.

### Not read

- journey-market steps beyond those listed, among them the returns rules (50 to 71), the catalog (79 to 81) and the EU market's compare-at and shipping pages (98 to 110).
- journey-business-entity's other steps.
- The other sweeps' Markets, General and Payments pages, which the searches listed with the same snippets.

### For the draft

- Q1-SH-034: Q1-SH-108, Q1-SH-109, Q1-SH-110. A saved market page with "No shipping rates" held "Region Active" and that its customers "won’t be able to check out"; a shipping zone's page held "To start selling to 27 countries/regions in this zone, include them in a market".
- Q1-SH-008 and Q1-SH-K1931: Q1-SH-113. The saved graph view's "Store defaults" includes the business entity, checkout and accounts, and returns, beside currency, domain and taxes.
- Q1-SH-041, Q1-SH-043, Q1-SH-100 and Q1-SH-K1268: Q1-SH-114, Q1-SH-115, Q1-SH-116, Q1-SH-118. Switching a store's business entity, in one run: the organization's entities in two countries, "multiple tax forms", the store address updated to match the new entity, and the markup's "contact support to deactivate active Shopify Payments, Balance, and Capital accounts".
- Q1-SH-K1243 and Q1-SH-K1271: Q1-SH-116, Q1-SH-117, Q1-SH-119. "Store address must be in the same country as the business entity"; changing it "may affect subscription fees, billing currency and apps".
- Q1-SH-K1935 and Q1-SH-K1936: Q1-SH-121. The store currency dialog's markup lists reasons for changing, among them "Testing payment processors not available in current currency".
- Q1-SH-065: Q1-SH-123. A Yemen-address store's saved Payments page held "Payment providers" and "Choose a provider", with no Shopify Payments section.
- Not tied to a draft id: Q1-SH-111 (Saudi Riyal "Recommended" for a market including Saudi Arabia), Q1-SH-112 (Avalara duty calculation "for a 0.5% transaction fee"), Q1-SH-120 (SSN for a United States individual entity), Q1-SH-122 (Backup Region options Canada and Yemen).
- The other draft ids: nothing in the texts read changes or adds to them.

### Problems

- A quote containing the markup's "Loading…" was refused by the checker as an ellipsis, so Q1-SH-113 cites two quotes around it.
- The cap of 3 documents per search was kept for the open items. For the draft's ids, the brief asks to look for the same flow in the new texts, and the two journeys were read beyond 3 steps.
