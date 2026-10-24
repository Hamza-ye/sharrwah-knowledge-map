# Q2 on Shopify: notes

## What was read

Every page was read through `method/help_map.py shopify page` from observed-sh at `c8b5fbee25966372a0475e6ed81f0b7760ac2921`, in English. The Help Center's REGISTER date seen is 2026-10-16. Pages were read on 2026-10-18.

Read in full or to the relevant section:
- compliance/legal/hemp/payments.md
- compliance/legal/hemp/selling-hemp.md
- compliance/legal/alcohol.md (no statement recorded: it gives the law to the seller as information)
- compliance/legal/eu-right-of-withdrawal.md
- compliance/legal/pricing-indication-directive.md
- international/pricing/checkout-restrictions.md
- international/managed-markets/prohibited-items.md (to the end of the category table)
- international/managed-markets/requirements-and-considerations.md (to the start of its compatible-countries table)
- privacy-and-security/privacy/customer-privacy-settings.md
- privacy-and-security/privacy/customer-privacy-settings/understanding-customer-privacy-settings.md
- sell-in-person/shopify-pos/country-requirements.md
- payments/shopify-payments/supported-countries/france/requirements.md (first section)

Read only for lines found with `grep`:
- international/managed-markets/deactivation.md
- international/managed-markets.md
- international/managed-markets/overview.md
- checkout-settings/checkout-form-options.md
- domains/managing-domain-ownership/edit-domain-contact-information.md
- domains/troubleshoot-issues-with-domains.md
- intro-to-shopify/pricing-plans/pricing-overview.md
- sell-in-person/shopify-pos/customize-pos/printed-receipts/considerations-for-the-visual-editor.md
- compliance/legal.md and payments/shopify-payments/onboarding/eligibility.md (for "hemp")

Corpus searches, each run with `--max 10`:
- `"regulatory requirements" "local regulations" "due to regulations" "legal requirements" "المتطلبات التنظيمية" "اللوائح المحلية"`
- `"to comply with" "in order to comply" "للامتثال" --with "not available" "isn't available" "unavailable" "غير متاح" "غير متوفر"`
- the two searches given in not-found.tsv

No live page was read.

## Not read

- The compatible-countries table of Managed Markets, and the full list of prohibited item categories. Neither is recorded as a list.
- The Managed Markets pages for Canada and the UK.
- The POS retail requirements for Italy (retail-requirements-italy).
- The Comply app's own terms. The Help Center names the app, and no agreement in Shopify's terms incorporates them.
- The Arabic versions of the pages read. The English pages were quoted.

## Problems with the method

- `help_map.py page` prints HTML inside `<aside>` notes. A quote that spans a `<strong>` tag depends on how the checker removes tags. The "Neighborhood" sentence was therefore left out, and only the next sentence was recorded (Q2-SH-032).
- The Managed Markets compatible-countries table runs to more than 50 rows. Under rule 5 each row would be its own statement, so it was left unrecorded.
- The run was stopped once by a usage limit before account.md was written. It continued from the files already in the folder.

## Re-check against the observed runs, 19 October 2026

### What was read

- The brief `R3-observed-recheck.md`; `R3-recording.md` (Rules, Quotes and citations, Output); Q2 and "How a run uses its question" in `questions-for-agents.md`; this folder's files.
- observed-sh at `c8b5fbee25966372a0475e6ed81f0b7760ac2921`: `README.md` and `docs/READING.md`, whole; `index/operations.jsonl` (rows for PaymentProviders, ShopifyPaymentsData, MarketsHomeCurrencyOptions).
- Corpus searches, each with `--max 10`:
  - `"hemp" "CBD" "القنب" --with "Shopify Payments"` (N01): no run document listed.
  - `"Managed Markets" "Global-e" "managedMarkets"` (N02).
  - `"unsupported countries" "unsupported region" "sanctions" "I'm located in" "غير مدعومة" "العقوبات"` (G0011, G0216, G0217).
  - `"Shopify International Limited" "Shopify Commerce Singapore" "Shopify Contracting Party" "Shopify Inc."` (G0003, G0004, G0005).
  - `"Shopify Capital" "lender" "تمويل Shopify" --with "Canada" "Australia" "كندا" "أستراليا"` (G0117, G0119, G0121): no run document listed.
  - `"Payment Facilitator" "Retail Payment Activities Act" "Shopify Payment Activities" "processing rate"` (G0093, G0096, G0097).
  - Sentence 1: `"not available in your country" "not available in your region" "isn't available in your country" "isn't available in your region" "not supported in your country" "غير متاح في بلدك" "غير متوفر في بلدك" "غير متاح في منطقتك"`.
  - Sentence 2: `"Customer data hosting" "data hosting location" "Shopify International Limited" "contracting entity" "استضافة بيانات العملاء"`.
  - Sentence 3: `"due to regulations" "local regulations" "regulatory requirements" "legal requirements" "to comply with" "اللوائح المحلية" "المتطلبات التنظيمية" "للامتثال"`.
  - `"eligible\":false" "threeDSecureEligibilityForCountry" "shopifyPaymentsAccount" "countryCode\":\"YE"` (the pointers).
- Run files opened (all under `raw/runs/`):
  - `20260930T002940Z-sweep-trial`: answers ShopifyPaymentsData `21d24a62…`, PaymentProviders `358609ed…`, MarketsHomeCurrencyOptions `abc9523d…`, MarketingConsentLabels `90f84a16…`; `actions.jsonl`; steps 170 (General), 376 (Payments), 377 (Add payment method), 387 (Third-party payment providers), `.aria.yaml`.
  - `20261006T225457Z-sweep-trial-my-store-8`: answers ManagedMarkets `04a9f889…`, PaymentProviders `e2e77d78…`; `actions.jsonl`; steps 316 and 387, `.text.txt`.
  - `20260930T003329Z-pilot-import`: answers RatesPreview `48a52f53…`, PaymentProviders `af95ff5e…`; `answers.jsonl` rows for them.
  - `20261005T013804Z-sweep-paid-store`: answer MarketingConsentLabels `8297ec2b…` (lines with "in your country"); steps 541 and 416, `.text.txt`.
  - `20261006T232216Z-journey-signup-new-account`: `actions.jsonl`; steps 004 (`.aria.yaml`, `.text.txt`), 007 and 010 (`.text.txt`).
  - `20260930T014656Z-journey-order-lifecycle`: `actions.jsonl`; every step's `.aria.yaml`, for lines with "available", "country", "region", "Yemen", "regulat", "law", "eligible", "not supported", "isn't". Nothing found there bears on Q2.
- The ShopifyPaymentsData and PaymentProviders answers of every run (274 files) were searched for `"name":"Shopify Payments","eligible":`, `"countryCode":` and the `"stripe":` object. All 52 ShopifyPaymentsData answers hold `"name":"Shopify Payments","eligible":false`. All 222 PaymentProviders answers hold `"countryCode":"YE"` and the same `"stripe"` object. One store's answers are recorded (Q2-SH-058 to Q2-SH-063).
- Stores: the runs name fake-demo-sharrwah, ts15uk-ug and zyd38b-ze in `answers.jsonl`. Country and currency come from each store's PaymentProviders answer (C063, C069, C076).

### Open items

- Q2-SH-N01: unchanged. The search listed no run document. Its `searched` and `read` are extended.
- Q2-SH-N02: unchanged. The ManagedMarkets answer (`"markets":{"nodes":[]`), the Managed Markets page (step 316) and the RatesPreview answer give no reason. Its `searched` and `read` are extended.
- Copied gaps G0003, G0004, G0005, G0011, G0093, G0096, G0097, G0117, G0119, G0121, G0146, G0216, G0217, G0219: none closed.
  - The Capital search (G0117, G0119, G0121) listed no run document. Every store observed is in YE.
  - G0003, G0004, G0093, G0096: the admin's Shopify Payments Terms of Service page (step 416 of the sweeps) shows the same terms the copies already hold. Nothing was recorded again.
  - G0216: the sign-up page (`20261006T232216Z-journey-signup-new-account`, step 004) shows the `combobox "I'm located in:"`, already copied as Q2-SH-K2662. It has 233 options, with "Yemen" selected. Searching it for Cuba, Iran, Korea, Syria, Crimea and Russia matched only "South Korea". The list is not presented as complete, so no absence is recorded, and the gap stays open.
  - G0005, G0011, G0097, G0146, G0217, G0219: no run document read gives a reason or a screening interface.
- Phrases from the starting message: none.

### Wording check

- Q2-SH-N01: the route's address `https://help.shopify.com/en/manual/compliance/legal/hemp` is shown in `compliance/legal.md`. That page was opened in the recording run (lines with "hemp") but was named only in `searched`. It is now also in `read`. No wording changed.
- Q2-SH-N02: its wording matches Q2-SH-K1956. The two route addresses are linked from `international/managed-markets.md`, which is in `read`. No change.

### Lists

- MarketsHomeCurrencyOptions (`20260930T002940Z-sweep-trial`) lists 130 currencies, with `"foreignExchangeFee":"0.02"`. None was recorded, because nothing in it bears on Q2.
- The checkout strings in the MarketingConsentLabels answer are one long list. Only the five entries that name a country or region as the cause were recorded (Q2-SH-065 to Q2-SH-069). Other entries with "country" or "region" were not recorded: mixed_destination_countries, pickup_unavailable_banner_title_with_country, simulated_express_checkout, shipping_errors.payment_method_not_supported, unavailable_address_country, unavailable_selected_address_for_region, change_country.*.

### Not read

- The other run documents the searches listed beyond those named above, including the remaining ManagedMarkets answers, the tax-service steps 529 and 533, the PrivacyPolicyQuery and Policy answers, the OrganizationLegalEntities and AssignableLegalEntities answers, and the partner-dashboard identity steps.

### Problems

- The pilot import run's answers have no step, only a HAR entry. Q2-SH-C075 and C076 give "step -" with the HAR entry in `locator` and `date_basis`.
- A step's `.text.txt` puts each list item on its own line. Q2-SH-064 and C068 write the list on one line and rely on the checker collapsing whitespace.


## The coordinator's correction, 19 October 2026

Q2 on Shopify's account cited some of Q2-SH-027 to Q2-SH-035 one number off, in six points: a statement was inserted after those points were written (the Q2 draft's notes found it). The ids are corrected by what each statement says, in Shopify's account and in the points and notes here that name them.


## Re-check against the step text from saved HTML, 19 October 2026

Source: observed-sh at `51626891aa711ee9c3ef2d05ce63c95396dca949`, folder `derived/step-text-from-html/`. Every statement below says what the saved page's markup held at that step, not what the page showed.

### What was read

- observed-sh's `docs/READING.md` (the folder's entry and the `steps/NNN.text.txt` entry) and `derived/step-text-from-html/meta.json`, at the commit. `README.md` was not re-read.
- The draft's Shopify ids, with `python3 -I method/record_ids.py` (35 ids).
- Searches, each `python3 -I method/corpus_search.py shopify <terms> --only "step text from saved HTML" --max 10`:
  - "hemp" "CBD" "القنب": 4 documents (Fabric metafield values, Dev Dashboard catalogs); none opened.
  - "Managed Markets" "Global-e": 17 documents. Opened `20261002T004032Z-sweep-capture-grow/316.html.txt` and `20260930T170204Z-journey-market/089.html.txt`.
  - "Shopify Payments" "eligible" "not available in your country" "isn't available": 459 documents. Opened `20260930T002940Z-sweep-trial/422.html.txt`; checked the same lines in `20260930T103225Z-sweep-dev/422.html.txt` and `20261002T003831Z-sweep-capture-plus/422.html.txt`.
  - "Shopify Capital" "Capital" "YouLend" "lender": 5,370 documents. Opened `20260930T045741Z-sweep-trial2/133.html.txt` (route capital:account:terms; it ended at `/capital/offers`).
  - "I'm located in" "unsupported" "sanction" "embargo" "Crimea": no document.
  - "third-party providers" "Third-party payment providers" "Supports 3DS": 22 documents. Opened step 387 of `20260930T002940Z-sweep-trial`, `20260930T103225Z-sweep-dev` and `20261002T003831Z-sweep-capture-plus`.
  - "Customer data hosting location" "data hosting" "stored in": no document.
  - "contracting party" "billing address" "Shopify International Limited" "Shopify Commerce Singapore": 407 documents; none opened (billing-address forms and draft orders; none names a Shopify company).
  - Sentence [1]: "not available in your country" "not available in your region" "isn't available in your country" "only available in" "not supported in your" "غير متاح في بلدك" "غير متوفر في": no document.
  - Sentence [3]: "regulations" "required by law" "due to local" "comply with" "legal requirements" "اللوائح": 132 documents; none opened beyond those below (Point of Sale app listing for NF525, already in the records as Q2-SH-053 to Q2-SH-057; Policies pages; Shop Pay Installments terms).
  - Sentence [2]: "legal entity" "Legal entities" "business entity" "data hosting": 154 documents. Opened `20261002T003831Z-sweep-capture-plus/060.html.txt` (settings/general).
  - For draft ids K2134, K1865, K1867, K1743, K1745, K1561, K1563: "Cookie banner" "privacy settings for each" "Data sharing" "regions where" (131; opened `20260930T002940Z-sweep-trial/444.html.txt`, checked `20261002T003831Z-sweep-capture-plus/443.html.txt`); "Shopify Tax" "tax services" "collect duties" (198; opened `20260930T002940Z-sweep-trial/542.html.txt`); "local payment methods" "payment methods are activated" (44; opened `20260930T002940Z-sweep-trial/414.html.txt`, which shows only ONERWAY (Direct) in test mode); "Payment Processor" "Stripe Payments" "Payment Facilitator" (54; the Shopify Payments terms and Balance pages, already copied; none opened).
- Each step's `actions.jsonl` row for its address, title and date, and `answers.jsonl` for the store names. Where the step has `steps/NNN.aria.yaml`, it was searched for the same words; each statement's note says what it showed.

### Open items

- Q2-SH-N01: unchanged. `searched` extended.
- Q2-SH-N02: unchanged. Neither Managed Markets page opened gives a reason. `searched` and `read` extended.
- Copied gaps G0003, G0004, G0005, G0011, G0093, G0096, G0097, G0117, G0146, G0219: unchanged. No text read gives a reason, place or boundary for them.
- Routed to the founder or either:
  - G0119, G0121 (Capital in Canada, Australia): unchanged. The route capital:account:terms, on store ibx5bt-xy (prices in YER), ended at `/capital/offers` with "There are no funding offers at the moment"; no terms, lender or provider. No store in Canada or Australia was observed.
  - G0216 (where the unsupported-region restriction applies): unchanged. The search for the sign-up list and the restriction's words listed no document.
  - G0217 (screening interface): unchanged. Nothing listed.
- New statements: Q2-SH-071 to Q2-SH-082 (12), citations Q2-SH-C077 to Q2-SH-C101.

### Wording check

- Q2-SH-N01 and Q2-SH-N02: no detail rests on the new texts; no change.

### Lists

- Q2-SH-078: the Tax regions table's first page only (15 rows); the saved HTML holds Previous and Next controls and no other page.
- Q2-SH-072, Q2-SH-073: recorded in full, with the card brand labels the markup states between the provider names.

### For the draft

- Q2-SH-058 (Shopify Payments "eligible":false for fake-demo-sharrwah): Q2-SH-071 adds the Subscribe to Plus page's words for the same store and for demo-fake-dev-store and capture-plus: "Shopify Payments is not available on your store."
- Q2-SH-K1337 (Transaction Fees with providers other than Shopify Payments): Q2-SH-071 adds the page's "0.2% third-party transaction fees apply if not using Shopify Payments" for the Plus plan, in those stores.
- Q2-SH-064 (third-party providers for ts15uk-ug on 2026-10-07): Q2-SH-072 and Q2-SH-073 add the lists for three other stores; fake-demo-sharrwah's held no ONERWAY (Direct), and demo-fake-dev-store's and capture-plus's held no Bogus Gateway.
- Q2-SH-K1865 and Q2-SH-K1867 (tax services by location; Shopify Tax destinations): Q2-SH-077, Q2-SH-078 and Q2-SH-079 add one store's Taxes page: Shopify Tax "now active" in the EU and UK, the tax service named per region (Manual, Basic or Shopify Tax), and shipping tax calculated automatically for Canada, the EU and the US.
- Q2-SH-K2134 (privacy settings per country and region): Q2-SH-080, Q2-SH-081 and Q2-SH-082 add the Cookie banner page's words on markets and regions that require a banner, and that compliance is the seller's responsibility.
- Q2-SH-K1243 and Q2-SH-K1248 (contracting party by billing address): nothing changes. Q2-SH-074 to Q2-SH-076 add, for one store's General page, that the store address must be in the business entity's country and that changing country can affect subscription fees and billing currency; they name no Shopify company.
- The other draft ids: nothing in the new texts read changes them.

### Not read

- The other documents the searches listed beyond those named above, including the other stores' step 316, 414, 443, 444 and 542 pages and the ended-trial runs' pages.

### Problems

- Statements Q2-SH-072, Q2-SH-073 and Q2-SH-078 hold the extracted text's bracketed attribute labels (`[accessibilitylabel: …]`) and line breaks as spaces, because the statement must be verbatim in the file; the checker's whitespace collapsing carries them.
- The dialogs' text (Q2-SH-074 to Q2-SH-076, Q2-SH-082) is in the saved markup but not the step's aria tree; nothing in the file says whether a dialog was open.
