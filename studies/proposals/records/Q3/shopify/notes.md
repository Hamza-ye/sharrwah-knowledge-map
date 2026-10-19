# Q3, Shopify: notes

## What was read

All held, at observed-sh `c8b5fbee25966372a0475e6ed81f0b7760ac2921`. Help Center pages are under `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/` and were read in English through `method/help_map.py`.

- **Map pages, for sentence [1] (10):**
  - `payments/shopify-payments/onboarding/account-setup.md`
  - `intro-to-shopify/initial-setup/setup-prepare-for-launch.md`
  - `intro-to-shopify/pricing-plans/free-trial.md`
  - `payments/shopify-payments/onboarding/proof-of-liveness.md`
  - `compliance/legal/handling-store-review.md`
  - `compliance/legal/alcohol.md`
  - `compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md`
  - `payments/shopify-payments/onboarding/american-express-requirements.md`
  - `payments/shopify-payments/onboarding/eu-verification.md`
  - `payments/shopify-payments/onboarding/bank-account-ownership-verification.md`
- **Pages found through the corpus search:**
  - `online-sales-channels/shop/eligibility/requirements.md` (linked from the launch page);
  - `fulfillment/fulfilling-orders/shipping-labels/buying-labels/troubleshooting-labels.md`, only the section "Shipping labels are temporarily unavailable while your account is verified".
- **Read for sentence [4] and for the not-found rows:**
  - `payments/shopify-payments/supported-countries/united-states/requirements.md`, the first part, through the Individuals list;
  - `compliance/legal/hemp/requirements.md`;
  - `compliance/legal/hemp/payments.md`;
  - `payments/shopify-payments/configuring-shopify-payments.md`, the bank account considerations only.
- **Data model, step 4:**
  - `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz` at offset 8639159 (ShopifyPaymentsAccount.md), through `method/warc_text.py --text`;
  - `structures/shopify/flow-step-environment/capture-plus@order-created/items.jsonl` line 733 (the `onboardable` field).
- **Corpus searches:** the commands are given in `not-found.tsv`. One more search, for sentence [1], was `python3 -I method/corpus_search.py shopify "before you can" "eligibility requirements" "merchant requirements" "قبل أن تتمكن" "متطلبات الأهلية" --max 10`.

## Live pages

None were read.

## What couldn't be read

- The `--text` output of the WARC record at offset 8639159 lists `activated` but no `onboardable` field. The corpus search snippet of the record at offset 11280587 shows `onboardable`, but the `--text` output of that record didn't show it either. `onboardable` is cited from the Flow step environment instead (Q3-SH-087).
- `admin.shopify.com/settings/payments` isn't held (`held_index.py`: not held). The verification request page is routed to the founder (Q3-SH-N03).

## Copies

- No copy was found wrong or out of date.
- Q3-SH-K1542 already records "Only the store owner can activate or switch to Shopify Payments." My own statement of that sentence was dropped as a staff permission under [3].
- The EU page's statement that only the store owner can view verification requests was also left out under [3].

## Method

- **Quotes from step lists.** Steps and notes in the held Help Center Markdown are inline HTML. The quote checker turns tags into spaces, which leaves a space before closing punctuation, as in "click Next ." So statements taken from step lists end before the final word's period: Q3-SH-003, 004, 006, 007, 008 and 029.
- **The added row.** SH-C-047 was added in `selection.tsv` with its terms from `concerns.tsv`. Its area id isn't in `concerns.tsv`, so the `area_id` column is empty.
- **Scope of the EU page.** The scopes for Q3-SH-065 to Q3-SH-074 are given in the words of the page title, "Shopify Payments accounts in Europe and the United Kingdom (UK)". The section "Verification timeline for new accounts" on that page doesn't restate the region itself.

## Re-check against the observed runs, 19 October 2026

### What was read

All at observed-sh `c8b5fbee25966372a0475e6ed81f0b7760ac2921`, through `git show`.

- **Guides:** `README.md` and `docs/READING.md`, whole.
- **Searches:**
  - N01: `python3 -I method/corpus_search.py shopify "payouts are paused" "complete verification" "verify your identity" "verification deadline" "إيقاف الدفعات مؤقتًا" "إكمال التحقق" "التحقق من هويتك" --max 10`
  - N02: `python3 -I method/corpus_search.py shopify "license" "licence" "age verification" "ترخيص" "التحقق من العمر" --with "alcohol" "hemp" "cannabis" "الكحول" "القنب" --max 10`
  - N03: `python3 -I method/corpus_search.py shopify "Activate Shopify Payments" "Complete account setup" "verification" "تفعيل Shopify Payments" "إكمال إعداد الحساب" --with "settings/payments" --max 10`; `python3 -I method/held_index.py https://admin.shopify.com/settings/payments` (not held) and `.../store/fake-demo-sharrwah/settings/payments` (readable in sweep steps).
  - Sentence [1]: `python3 -I method/corpus_search.py shopify "Pick a plan" "Select a plan" "password protected" "Remove password" "Not eligible" "isn't eligible" "not available in your country" "اختر خطة" "غير مؤهل" --max 10`
  - Sentence [4]: `python3 -I method/corpus_search.py shopify "Opening soon" "store is unavailable" "checkout is disabled" "can't accept payments" "payouts paused" "trial has expired" "المتجر غير متاح" "انتهت الفترة التجريبية" --max 10`
  - Sentences [2] and [3] share the reading of [1].
- **Run files opened:**
  - `raw/runs/20261005T013804Z-sweep-paid-store/`: `answers/admin.shopify.com/ShopifyPaymentsData/a54107f8….json`; `steps/376.text.txt` (Payments); `steps/387.text.txt` (Third-party payment providers); `steps/388.text.txt` (ONERWAY (Direct)); `steps/391.text.txt` (Two-Step authentication setup); `steps/477.text.txt` (General); `actions.jsonl`, `answers.jsonl`.
  - The 52 ShopifyPaymentsData answers the runs hold, only their `eligible`, `idVerificationForOnboardingRequired`, `missingAttributesInfo` and `configuration` values: every one gives `"eligible":false`, `"idVerificationForOnboardingRequired":false`, `"missingAttributesInfo":null` and `"configuration":null`.
  - `raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.text.txt` (Orders) and `actions.jsonl`.
  - `raw/runs/20261004T232751Z-journey-subscribe-grow/steps/001.aria.yaml`, `002.aria.yaml` and `actions.jsonl`.
  - `raw/runs/20261005T082612Z-journey-themes/answers/admin.shopify.com/ThemeLocaleTranslations/0d72b96c….json` (by `grep -o`), `answers.jsonl` and `actions.jsonl` line 12.
  - `raw/runs/20260930T014656Z-journey-order-lifecycle/actions.jsonl` (the pointer journey): its steps create a draft order, an order, a return and a refund on demo-fake-dev-store; nothing in them bears on the question, and no step file was opened.
  - `index/operations.jsonl`, for the runs that called ShopifyPaymentsData, PaymentProviders and MarketsHomeCurrencyOptions.
- **Not read:** the PaymentProviders and MarketsHomeCurrencyOptions answers (the providers and currencies offered bear on other questions); the Banners and SurfaceGuides answers the searches listed; the Partner Dashboard's "Verify your identity" steps (run 20261007T010009Z-journey-partner-dashboard, steps 094 to 096), which concern the Partner and Dev Dashboard account, not a store.

### Open items

- Copied gaps cited in `account.md`: none (it cites the pilot absence Q3-SH-A0002, not a G or H gap). Phrases from the coordinator: none.
- **Q3-SH-N01:** unchanged. The runs read hold no Shopify Payments account and no verification timeline. Search and files added to `searched` and `read`.
- **Q3-SH-N02:** unchanged. The search listed no run document. Search added to `searched`.
- **Q3-SH-N03:** unchanged, still routed to the founder. The Payments settings page is held in the sweeps, but it shows a third-party provider and no Shopify Payments section, and the store's ShopifyPaymentsData answer gives `"eligible":false` (Q3-SH-100). The route now says the runs' stores show that value.

### Wording changes (step 4)

- Q3-SH-N02: "licences" became "licenses", as Q3-SH-051 and Q3-SH-093 spell it. The account's three uses of "licence(s)" were changed the same way.
- Q3-SH-N01 and Q3-SH-N03: every name and path they give is in what their `read` names (eu-verification.md, account-setup.md) or in Q3-SH-003 and Q3-SH-069 to Q3-SH-072. No change.

### New statements

Q3-SH-100 to Q3-SH-105, citations Q3-SH-C140 to Q3-SH-C149.
- Q3-SH-100's scope gives the store's country and currency from its General settings page in the same run (Q3-SH-C141, C142).
- Q3-SH-105: `answers.jsonl` names no store for this answer (`"store": null`); its endpoint names `demo-fake-dev-store`, cited as Q3-SH-C149, and the step's address in `actions.jsonl` is in the same store.

### Problems

- `held_index.py` reports `https://admin.shopify.com/settings/payments`, the address the Help Center links, as not held; the runs' steps are held under `https://admin.shopify.com/store/<handle>/settings/payments`, and only that form lists them.
- A corpus search whose `--with` term is a path (`settings/payments`) matched over 5,000 answers, since many answers carry admin addresses.

## Re-check against the step text from saved HTML, 19 October 2026

### What was read

All at observed-sh `51626891aa711ee9c3ef2d05ce63c95396dca949`, through `git show`.

- **Guides:** `docs/READING.md` (the folder's entry and the run files' table) and `derived/step-text-from-html/meta.json`; `derived/step-text-from-html/index.tsv`, for the runs it covers.
- **Searches,** each with `--only "step text from saved HTML" --max 10`:
  - N01 and N03: `python3 -I method/corpus_search.py shopify "payouts are paused" "complete verification" "verify your identity" "verification deadline" "Activate Shopify Payments" "Complete account setup" "إيقاف الدفعات مؤقتًا" "إكمال التحقق" "التحقق من هويتك" "تفعيل Shopify Payments"` (35 documents: account security, sign-in, staff invitation and policy steps);
  - N03 and Q3-SH-100: `... "Shopify Payments" "شوبيفاي للمدفوعات" --with "eligible" "not available" "isn't available" "unavailable" "Activate" "verification" "غير متاح" "مؤهل"` (163 documents, led by the plan pages);
  - N01: `... "deadline" "payouts paused" "on hold" "suspended" "restricted" "store is paused" "الموعد النهائي" "معلق" --with "payouts" "Shopify Payments" "store" "checkout" "verification"`;
  - N02: `... "license" "licence" "age verification" "ترخيص" "التحقق من العمر" --with "alcohol" "hemp" "cannabis" "CBD" "الكحول" "القنب"` (2 documents: Dev Dashboard Catalogs, product category names);
  - Q3-SH-027, 028, 101 (sentence [1]): `... "select a plan" "Pick a plan" "trial has expired" "password protected" "Remove password" "store is unavailable" "اختر خطة" "انتهت الفترة التجريبية" "محمي بكلمة مرور"` and `... "private mode" "Store access" "password page" "Opening soon" "can't accept orders" "can’t accept payments" "الوضع الخاص" "الوصول إلى المتجر"`;
  - Q3-SH-012, 015, 017, 020, 023, 041, 043, 061, 062: `... "government-issued ID" "account representative" "beneficial owner" "upload documents" "bank statement" "Proof of Liveness" "information requests" "هوية حكومية" "ممثل الحساب" "كشف حساب بنكي"` (only the account profile's name field matched);
  - Q3-SH-057, 058, 077, 083, K1536, K2268, A0002: `... "not available in your country" "not supported in your country" "isn't available in your region" "not eligible" "isn't eligible" "requirements" "غير متاح في بلدك" "غير مؤهل" --with "Shopify Payments" "Shop" "Balance" "Capital" "payouts" "bank account"` (currency and pickup-location eligibility, discount requirements) and `... "chargeback rate" "eligible products" "Shopify Balance" "Shopify Capital" "Shop Pay Installments" "American Express" "payout account" "bank account" --with "requirement" "required" "eligible" "eligibility" "unavailable" "not available" "you need" "must"`;
  - Q3-SH-K1237: `... "Create a Shopify account" "legal name" "Business details" "Store owner" "business entity" "الاسم القانوني" "تفاصيل النشاط التجاري" "مالك المتجر" --with "required" "must" "add" "Add"`.
- **Files opened** (`derived/step-text-from-html/`): `20260930T103225Z-sweep-dev/376.html.txt` and `396.html.txt`; `20260930T045741Z-sweep-trial2/376.html.txt`, `387.html.txt`, `408.html.txt`, `422.html.txt`, `154.html.txt`, `125.html.txt` (grep); `20261002T003831Z-sweep-capture-plus/376.html.txt`; `20261002T004032Z-sweep-capture-grow/376.html.txt`; `20260930T002940Z-sweep-trial/376.html.txt` and `059.html.txt`; `20261004T115543Z-storefront-page-types/001.html.txt`, `001.frame-0.html.txt`, `001.frame-1.html.txt`; `20261004T223401Z-journey-business-entity/013.html.txt`. With `grep` only, for verif, identity document, deadline and Activate Shopify Payments: steps 380 to 382, 396, 399, 400, 413 and 417 of the sweep-dev and sweep-trial2 runs (none holds them).
- **Run files,** for addresses, titles, dates, stores and the aria comparison: the `actions.jsonl` and `answers.jsonl` (store field only) of runs 20260930T103225Z-sweep-dev, 20260930T045741Z-sweep-trial2, 20261004T115543Z-storefront-page-types and 20261004T223401Z-journey-business-entity; `steps/376.aria.yaml` and `422.aria.yaml` of the first two, `steps/408.aria.yaml` of sweep-trial2, `steps/001.frame-0.aria.yaml` of storefront-page-types and `steps/013.aria.yaml` of journey-business-entity, with `grep` for the recorded words.
- **Not read:** the other 160 Shopify Payments documents past the first ten (the same plan pages in other runs and steps); the Shop Pay Installments terms past section 2; the account profile pages (step 465), whose match was the name field's help text; the pickup-point and currency "Not eligible" lists, which bear on other questions.

### Open items

- Copied gaps cited in `account.md`: none (Q3-SH-A0002 is a pilot absence).
- **Q3-SH-N01:** unchanged. Search and files added to `searched` and `read`.
- **Q3-SH-N02:** unchanged. Search added to `searched`.
- **Q3-SH-N03** (routed to the founder): unchanged, still routed to the founder. The Payments pages saved in the 30 September sweeps show a test payment gateway (a development store, Q3-SH-106) or a third-party provider and no Shopify Payments section, and the routes for onboarding, information requests and identity documents all ended at the same page. Search and files added.
- **The draft's Shopify ids:** each was read with `record_ids.py`. What the new texts add is listed under "For the draft". The others showed nothing in the new texts: Q3-SH-012, 014, 015, 017, 020, 023, 041, 043, 053, 057, 058, 061, 062, 065, 066, 070, 072, 073, 077, 083, 086, 095, 101, A0002, K1237, K1536, K2268, N01, N02, P0045, P0085.

### Wording changes (step 4)

- None. N01, N02 and N03 name nothing the new texts contradict, and every name and path they give is still in what their `read` names or in the folder's statements.

### New statements

Q3-SH-106 to Q3-SH-111, citations Q3-SH-C150 to Q3-SH-C155. Each `note` says it is in the saved HTML of its step and whether the step's aria tree shows the same words.
- Stores are named as each run's `answers.jsonl` names them: demo-fake-dev-store, ibx5bt-xy, capture-plus, capture-advanced. The steps' addresses name the same handles.
- Q3-SH-107 is in a dialog in the markup, not between hidden markers; the aria tree of its step doesn't show it, and its note says so.
- Q3-SH-106 and Q3-SH-107 begin with the extractor's `[heading: …]` marker, kept so that the heading and the words after it are one passage of the file.

### For the draft

- **Q3-SH-100:** Q3-SH-108. On another store (ibx5bt-xy, 30 September 2026), the plan page's saved HTML says "Shopify Payments is not available on your store."
- **Q3-SH-K1274:** Q3-SH-107. A trial store's saved Payments page holds, in a dialog, "You need to set-up two-step authentication before adding a bank account."
- **Q3-SH-027 and Q3-SH-028:** Q3-SH-109 and Q3-SH-106. On development stores, the saved Preferences page holds Private mode on with "Your online store is in development. To let visitors access your store, give them the password.", and the saved Payments page "Development stores can only process test payments".
- Not tied to a draft id: Q3-SH-110 (Shop Pay Installments terms: Affirm may deny access; information identifying the seller and beneficial owners is required) and Q3-SH-111 (a US Individual entity's SSN field, "Used for tax filing and verification").

### Problems

- The extracted text keeps markers such as `[heading: …]` and `[label: …]` inline, so a heading and the paragraph after it can only be quoted together with the marker.
- A search with a common term in `--with` (such as "store" or "Capital") matches the admin's navigation and keyboard-shortcut text on almost every page, so its first ten documents are mostly noise.
