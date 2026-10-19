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
