# Q5 on Shopify: notes

## What was read (2026-10-19)

From the Help Center map (`help_map.py shopify 7659`, the Payments menu), in English, from observed-sh at c8b5fbee25966372a0475e6ed81f0b7760ac2921 (`structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/…`):
- `payments.md`
- `payments/getting-paid.md`
- `payments/third-party-providers.md`
- `payments/third-party-providers/configuring-providers.md`
- `payments/third-party-providers/payment-gateway-availability.md`
- `payments/third-party-providers/updating-third-party-providers.md`
- `payments/third-party-providers/adyen-gateway.md`
- `payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md`
- `payments/additional-payment-methods.md`
- `payments/additional-payment-methods/activate-payment-methods.md`
- `payments/additional-payment-methods/deactivate-payment-methods.md`
- `payments/accelerated-checkouts/amazonpay/amazon-pay.md`
- `payments/shop-cash/payouts-and-reconciliation.md`
- `products/purchase-options/subscriptions/considerations.md`
- `intro-to-shopify/initial-setup/setup-store-management.md`: only the passage the corpus search pointed to

From this repository's capture run `20261011T061248Z-q1-shopify-sources`:
- `https://shopify.dev/docs/apps/build/payments.md` (item 121)
- `https://www.shopify.com/partners/terms` (item 152): section C.4, "Additional Terms Applicable to Payments Developers", and the definition of "Payments Developer"

Corpus searches, each with `--max 10`:
- discontinuation terms with payment provider, gateway or method, in English and Arabic;
- where the money goes;
- payments apps;
- merchant account with third-party provider;
- Amazon Pay agreement;
- payment gateways page.

The commands that bear on not-found rows are given in `not-found.tsv`.

## Live pages

None were read.

## Not read

- `https://www.shopify.com/payment-gateways`, the per-country list of gateways. It is held and readable at `observed-sh@c8b5fbee:raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz@41642451` but was not read (Q5-SH-N03).
- `help.shopify.com/en/manual/compliance/legal/hemp/payments.md`, which the gateways search listed.
- The Arabic versions of the pages above. Each page was read in English only, and none was quoted in Arabic.
- Amazon's customer agreement and policies at `https://pay.amazon.com/help/201212190`. It is not held, and as a provider's own terms it was not read (Q5-SH-N01).
- The Revenue Share agreement and the Payments Platform Developer Guidelines that the Partner Program Agreement names. They were not looked for.
- The local payment method subpages, the per-country Shopify Payments pages and the PayPal subpages were not opened. The copies already cover these topics.

## Copies

- No copy was found wrong.
- Q5-SH-065 continues Q5-SH-K1704, which copies only the first sentence of the Wind Down Period clause.
- The PayPal Wallet row Q5-SH-034 holds the whole table row. Q5-SH-K1716 copies its last cell.

## Selection

- 29 concerns were copied, including S-01, which was set to `copy` already. 123 were set aside.
- No concern was added.
- SH-C-047 (Shopify Checkout), SH-C-142 (Point of Sale) and SH-C-156 (Apps and third-party services) were copied after reading their statements with `show`, because those statements are about using Shopify Checkout for payment processing, using the same payment processor for POS, and disabling Third Party Services.

## Method

- Where a statement ends at an inline HTML tag in the held Markdown, as in `Settings > <a>General</a>.`, the checker's markup removal leaves a space before the full stop. Those statements (Q5-SH-004, Q5-SH-012, Q5-SH-051) end before the tag and its trailing punctuation.
- For Q5-SH-018 the same thing happens in the middle of a sentence, so the statement starts at "then".
- Help Center pages show no date. Their citations give `undated`, with the held commit as the basis.

## Re-check against the observed runs, 19 October 2026

### What was read

- The guides `README.md` and `docs/READING.md` of observed-sh at c8b5fbee25966372a0475e6ed81f0b7760ac2921, whole.
- Searches:
  - `python3 -I method/corpus_search.py shopify "PaymentProviders" "third-party-providers" "مزودو الدفع" --max 10` (sentences 1 and 3, and Q5-SH-N03);
  - `python3 -I method/corpus_search.py shopify "Amazon Pay" "أمازون باي" "amazonPay" --with "agreement" "policies" "اتفاقية" --max 10` (Q5-SH-N01);
  - `python3 -I method/corpus_search.py shopify "merchant account" "حساب التاجر" "payout" "الدفعات" --with "third-party" "Tap Payments" "مزود" --max 10` (Q5-SH-N02 and sentence 5);
  - `python3 -I method/corpus_search.py shopify "Shopify Payments isn't available" "not available in your country" "غير متاح في بلدك" "Shopify Payments غير متوفر" --max 10` (sentences 1 and 2): it listed only MarketingConsentLabels and ThemeLocaleTranslations answers, none opened;
  - `python3 -I method/corpus_search.py shopify "deprecationStatus" "no longer supported" "choose a new provider" "لم يعد مدعومًا" --max 10` (sentence 4): it listed translation and introspection answers and a partner dashboard step, none opened. Nothing was recorded for sentence 4;
  - `python3 -I method/held_index.py https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers`.
- Files, all at observed-sh c8b5fbee25966372a0475e6ed81f0b7760ac2921, under `raw/runs/`:
  - `20260930T074710Z-m0-account`: `answers.jsonl`, `actions.jsonl` (steps 20 to 23), the answers PaymentProviders (step 22), ShopifyPaymentsData (step 21);
  - `20260930T045741Z-sweep-trial2`: `actions.jsonl` (steps 386 to 389), `answers.jsonl`, `steps/387.aria.yaml`, the answers ThirdPartyPaymentProviders and ShopPayExpressData (step 387), and the countryCode in PaymentProviders (step 388);
  - `20260930T024857Z-buyer-prereq`: `answers.jsonl`, the answers ShopifyPaymentsData and PaymentProviders (step 2);
  - `20261005T013804Z-sweep-paid-store`: `actions.jsonl`, `answers.jsonl`, `steps/376.text.txt`, `387.text.txt`, `389.text.txt`, the answers PaymentProviders (step 376), ThirdPartyPaymentProvider (step 388), AdditionalPaymentProviders (step 377);
  - `20261006T225457Z-sweep-trial-my-store-8`: `actions.jsonl`, `answers.jsonl`, `steps/376.text.txt`, `387.text.txt`, the answer PaymentProviders (step 376);
  - `20260930T014656Z-journey-order-lifecycle`: `actions.jsonl`, `answers.jsonl`, `steps/009.aria.yaml`, `010.aria.yaml`, `011.aria.yaml`, `027.aria.yaml`, the answers OrderDetailsPayment (step 30) and OrderManualPaymentMethods (step 8);
  - `index/operations.jsonl`, the rows of ShopifyPaymentsData.

### Open items

- Q5-SH-N01: unchanged. No run document the search listed has a title or snippet about Amazon's customer agreement and policies. The search was added to `searched`.
- Q5-SH-N02: unchanged. No run document the search listed has a title or snippet about where a third-party provider holds the money. The search was added to `searched`.
- Q5-SH-N03: narrowed. The runs show what the admins of stores with countryCode YE listed as third-party payment providers (Q5-SH-085, Q5-SH-086). The payment gateways page's own list is still not read: no run step was found that names or links it. `read` and `searched` were extended.
- No copied gap (G or H) is cited by `account.md`.
- The starting message listed no phrases for this folder.

### Wording

- The three rows were checked against the pages their `read` names. Their quoted phrases ("You meet and adhere to Amazon's customer agreement and policies", "the purchase amount is transferred to your merchant account", "check with the payment provider", "primary resource") are in those pages, and "direct" and "external" providers are in the folder's records. No wording was changed.

### Stores and lists

- Every store observed here states `"countryCode":"YE"` in its PaymentProviders answer.
- The ThirdPartyPaymentProvider and AdditionalPaymentProviders answers of run `20261005T013804Z-sweep-paid-store`, which `answers.jsonl` names as store fake-demo-sharrwah, carry `applicationUrl` values with `shop=ctcbwa-r1.myshopify.com`. The scope names fake-demo-sharrwah, as the run and the same run's PaymentProviders answer (`"url":"https://fake-demo-sharrwah.myshopify.com"`) state it.
- The country of demo-fake-dev-store for Q5-SH-092 and Q5-SH-093 is cited from the same store's PaymentProviders answer in run `20260930T024857Z-buyer-prereq`, since the journey's own answers read here don't state it.
- The AdditionalPaymentProviders answer (store fake-demo-sharrwah, step 377) lists 38 providers, each with a `countries` list. Only Tabby and Tap Payments were recorded (Q5-SH-088, Q5-SH-089).
- The ThirdPartyPaymentProviders answer of run `20260930T045741Z-sweep-trial2` (store ibx5bt-xy, step 387) and its page list six providers, ONERWAY (Direct) among them. They were read but not recorded, since the page's tree isn't one passage. The paid store's page (Q5-SH-085) lists five, and its Payments page shows ONERWAY (Direct) as the active provider (Q5-SH-086).

### Not read

- MarketsHomeCurrencyOptions answers, and the General settings pages (`/settings/general`) of the sweeps: the stores' country was taken from their PaymentProviders answers.
- The pilot-import PaymentProviders answers, the staff sweeps' step 387, ShopifyPaymentsFeeSchedule, ShopifyPaymentsOnboardingQuery and AmazonPaymentProvider answers of the paid store, and the trial2 AdditionalPaymentProviders answer.
- No journey that installs a third-party provider was looked for.

### Problems

- A Shopify corpus search took one to several minutes. The searches for sentences 1, 2 and 4 listed mostly translation answers (MarketingConsentLabels, ThemeLocaleTranslations) whose text holds the terms, so they pointed at no payment pages. The payment pages were found through the pointers, `held_index.py` and the runs' `actions.jsonl`.
