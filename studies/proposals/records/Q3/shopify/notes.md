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
