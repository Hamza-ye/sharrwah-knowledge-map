# Notes: Q6, shopify

## Selection

- Copied 22 rows: SH-C-001, 002, 004, 005, 006, 008, 062, 063, 064, 068, 075, 081, 086, 088, 091, 098, 100, 104, 110, 173, 174, and S-01.
- Set aside the other 86. Their reasons are in `selection.tsv`.
- Added no concern.

## What was read

Held, observed-sh at c8b5fbee25966372a0475e6ed81f0b7760ac2921:

- Help Center pages, through `method/help_map.py shopify page`, all in English (md/en):
  - intro-to-shopify/initial-setup/setup-getting-started (nothing new);
  - intro-to-shopify/pricing-plans/free-trial;
  - intro-to-shopify/initial-setup/setup-business-settings;
  - intro-to-shopify/initial-setup/new-to-shopify-checklists/general-checklist;
  - payments/shopify-payments/supported-countries;
  - payments/shopify-payments/onboarding/eligibility;
  - payments/third-party-providers/payment-gateway-availability;
  - intro-to-shopify/pricing-plans/pricing-overview;
  - payments/third-party-providers/configuring-providers;
  - checkout-settings/test-orders/payments-test-mode (it repeats what configuring-providers says);
  - your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills;
  - your-account/manage-billing/paying-your-bills/managing-payments/billing-address.
- `raw/runs/20261006T232216Z-journey-signup-new-account`: `actions.jsonl`, `run.json`, the text of steps 001 to 003, 012, 013 and 019, the aria of steps 004 and 010, and these answers:
  - ShopifyPaymentsData, ShopifyPaymentsActive, SignupMutation, BusinessDetailsData;
  - EligibilityQuery, FinanceApp, CoreCapital;
  - the first part of atlas.shopifysvc.com/countries.
- `structures/shopify/sign-in-methods/accounts.shopify.com@signup` (items.jsonl, meta.json).
- `structures/shopify/com-llms/llms-txt` (source.txt line 43, items.jsonl line 28, meta.json).
- `structures/shopify/help-center/help.shopify.com@en-ar/meta.json`.
- `raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz@41642451` (https://www.shopify.com/payment-gateways), through `warc_text.py`.

Held in this repository's capture runs:

- https://www.shopify.com/legal/terms, from `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/143-shopify.com/text.txt`: sections 1 and 2.
- https://help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md, from items/101-help.shopify.com/text.txt.

Corpus searches (commands are in `not-found.tsv` where a row rests on them):

- "age of majority", "business purposes", "سن الرشد", "18 عامًا";
- "isn't available in your country", "not available in your region", "unsupported country", "غير متاح في بلدك", "غير مدعوم".

## Live pages read

- https://www.shopify.com/payment-gateways, read 2026-10-19 through `method/capture/page_text.mjs`, served in English.
  - It showed the "Type in your country" filter and the unfiltered list of providers. Nothing from it is cited.
  - Working copy: `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/records/Q6-shopify/pg-live.txt`.

## What could not be read

- The per-country results of the payment gateways filter. They show only after typing a country (Q6-SH-N01).
- The Settings > Payments page of store 2jiwxs-gr. It is not held (Q6-SH-N02).
- Steps 002 and 003 of the sign-up journey. Their visible-text files hold only an extraction error ("visible text failed"). Their aria files were not needed: the aria of step 004 holds the "I'm located in:" combobox.

## Copies out of date or wrong

- Q6-SH-P0097, the pilot's list of "Shopify Payments for <country>" pages, has 40 items and no China item.
  - The held Help Center page (observed-sh c8b5fbee, run 20261016T213535Z-help-en-ar-html-md) lists 41 items, including "Shopify Payments for China".
  - Recorded as Q6-SH-023. The pilot's absence Q6-SH-A0002 counts 40 items.

## Problems with the method

- `check_proposals.py` rejects a not-found row whose `route` names an address that is held, even when `who_can` is `either`.
  - For Q6-SH-N01 and Q6-SH-N03, the held copies (the shopify.com/payment-gateways archive record and the accounts.shopify.com@signup structure) were read. They don't show what the rows ask for: filtered results, and what happens after choosing a place.
  - The routes now name the pages in words instead of by address.
- `help_map.py shopify page` reports "not held" for `md/en/manual/your-account/legal/unsupported-countries-and-regions.md`. That page was read from this repository's capture run instead.
- The `I'm located in:` list has 233 options. It is recorded whole as one statement (Q6-SH-010) with 19 citations. Nothing presents it as complete, so no absence rests on it.

## Re-check against the observed runs, 19 October 2026

### What was read

All in observed-sh at c8b5fbee25966372a0475e6ed81f0b7760ac2921:

- The guides: `README.md` and `docs/READING.md`, whole.
- `index/operations.jsonl`: the rows of `PaymentProviders`, `ShopifyPaymentsData` and `MarketsHomeCurrencyOptions`. None calls `PaymentProviders` for store 2jiwxs-gr.
- `derived/admin-controls.jsonl`: the "Choose a provider" control, by `grep`. Nothing from it is cited.
- `raw/runs/20260930T071154Z-m0-instruments`: `answers.jsonl` (its PaymentProviders and ShopifyPaymentsData rows), and the answers `PaymentProviders/c17dfbe2…` and `ShopifyPaymentsData/0a1aef7b…`. Nothing from them is cited: the store ts15uk-ug answers below show the same keys.
- `raw/runs/20260930T003329Z-pilot-import/answers.jsonl`: its PaymentProviders and ShopifyPaymentsData rows only.
- `raw/runs/20261005T013804Z-sweep-paid-store`: `actions.jsonl`, and the text of steps 170 (General), 376 (Payments) and 387 (Third-party payment providers). Nothing from them is cited.
- `raw/runs/20261006T225457Z-sweep-trial-my-store-8`: `actions.jsonl`, `answers.jsonl` (two rows), the text of steps 170, 376 and 387, and the answers `PaymentProviders/e2e77d78…` and `ShopifyPaymentsData/5e7fd81f…`.
- `raw/runs/20260930T045741Z-sweep-trial2/actions.jsonl` and `raw/runs/20260930T002940Z-sweep-trial/actions.jsonl`: which steps visit the General and third-party providers pages. Their steps hold no text files. They were not read.
- `raw/runs/20261004T223401Z-journey-business-entity`: `actions.jsonl`, and the aria of steps 003 and 031.
- `raw/runs/20261005T002448Z-journey-dev-store-region`: `actions.jsonl`, and the text of step 006. Nothing from it is cited.
- `raw/runs/20261006T232216Z-journey-signup-new-account`: `actions.jsonl` (step 5), and the text of steps 005 and 007.

Corpus searches, all `python3 -I method/corpus_search.py shopify … --max 10`:

- N02: "Choose a provider" "Third-party payment providers" "مزود دفع تابع لجهة خارجية" "اختيار مزوّد". Then the same terms, with "Payment providers", "isn't available in your country" and "مزودو الدفع", `--with "2jiwxs"`.
- N01: "Type in your country" "payment-gateways" "Third-party payment providers" "مزودو الدفع التابعون لجهات خارجية", `--with "Yemen" "اليمن"`.
- N03: "I'm located in" "Business location" "located in" "موقع النشاط التجاري" "أنا موجود في", `--with "Yemen" "Iran" "Cuba" "Syria"`.
- G0216: "isn't supported in your country" "not available in your country" "unsupported countries" "sanctions" "غير مدعوم في بلدك" "العقوبات".
  - The run documents listed are `MarketingConsentLabels` and `ThemeLocaleTranslations` answers, and the admin's Shopify Payments Terms of Service pages (step 416 of the sweeps).
  - None was opened. The terms are copied (Q6-SH-K2268, K2269).
- G0217: "screening" "sanctioned" "embargoed" "restricted region" "فحص العقوبات" "محظورة".
  - The run documents listed are a Flow templates page, a Flow answer, and the same Shopify Payments terms pages.
  - None was opened.
- G0009: "multiple entities" "multiLegalEntitiesPhase" "Add business entity" "كيانات متعددة" "إضافة كيان تجاري".
  - The run documents listed are `MarketsHomeShop` answers.
  - None was opened. `multiLegalEntitiesPhase` was read in the PaymentProviders answers above.
- G0011: "Business entity used for financial products" "country of your business" "store country" "بلد المتجر" "الكيان التجاري".
  - The run documents listed are General settings pages of the sweeps and journeys.
  - Store ts15uk-ug's General page and the business-entity journey were read.
- Sentence 1: "Create account" "Start free trial" "verify your identity" "legal entity" "إنشاء حساب" "التحقق من هويتك", `--with "Yemen" "YE" "اليمن"`.
  - The run documents listed are the sign-up journeys' steps, and policy answers.
  - Sentence 2 shares the N02 searches.

### Open items

- **Q6-SH-N01: unchanged.** The runs hold no page of the payment gateways filter. The search is added to its row.
- **Q6-SH-N02: narrowed.** Store ts15uk-ug's ShopifyPaymentsData answer gives `"eligible":false`. Its Payments settings page and its Third-party payment providers page were read (Q6-SH-036, 040, 041). What remains is the same pages for store 2jiwxs-gr. No run calls `PaymentProviders` for that store.
- **Q6-SH-N03: unchanged.** Sign-up steps 005 and 007 show the location field as "[Yemen]". They show no words about the list as a whole. The search and steps are added to its row.
- **Q6-SH-G0216, G0217, G0009, G0011: unchanged.** No run document read shows them.
  - Q6-SH-039 (`multiLegalEntitiesPhase`) bears on G0009's topic. It names no one responsible.
- No phrases were listed by the coordinator.

### Wording check (step 4)

- N01, N02 and N03 were checked. Every name, label and path they give is in what their `read` names or in this folder's records: "Type in your country" (the live page read), "Payment providers section" and "Choose a provider" (configuring-providers.md, Q6-SH-025, and now Q6-SH-040), `country=YE` (Q6-SH-011), and "I'm located in:" (step 004 aria).
- No change was needed, apart from N02's narrowing.

### New statements

Q6-SH-035 to Q6-SH-043, with citations Q6-SH-C079 to Q6-SH-C091.

### Not recorded or not read

- The Country code list of "Add business entity" (business-entity journey, step 003 aria) has 237 options, with Yemen [selected]. Each option carries nested `img` and `text` lines.
  - It was not recorded: in full, it would need about 50 citations.
  - Nothing presents it as complete.
- Store fake-demo-sharrwah's Payments and Third-party payment providers pages (sweep-paid-store, steps 376 and 387) were read but not recorded. ONERWAY (Direct) is active there.
- These pointers were not read: the journey `20260930T014656Z-journey-order-lifecycle`, and `MarketsHomeCurrencyOptions` answers. They bear on no sentence of Q6.
- The sweeps' General pages of other stores (capture-plus, capture-advanced, capture-grow, demo-fake-dev-store) were not read.

### Problems

- In `20260930T071154Z-m0-instruments/answers.jsonl`, the PaymentProviders answer listed for store ctcbwa-r1 (`c17dfbe2…`) carries `"url":"https://fake-demo-sharrwah.myshopify.com"`. It was not cited.
- The brief's `date_basis` wording ("observed in run <run>, step <n>") differs from the earlier rows' wording. The new rows use the brief's.
