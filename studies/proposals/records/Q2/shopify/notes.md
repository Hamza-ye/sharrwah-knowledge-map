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
