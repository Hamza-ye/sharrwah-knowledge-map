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

## Re-check against the step text from saved HTML, 19 October 2026

All files below are at observed-sh 51626891aa711ee9c3ef2d05ce63c95396dca949.

### What was read

- `docs/READING.md`, its entry for `derived/step-text-from-html/`, and that folder's `meta.json` and `index.tsv`.
- Searches (each listed the corpus "observed-sh: step text from saved HTML" where it says so):
  - `python3 -I method/corpus_search.py shopify "Amazon Pay" "أمازون باي" --with "customer agreement" "policies" "اتفاقية" "سياسات" --max 10` (Q5-SH-N01): no step text from saved HTML listed;
  - `python3 -I method/corpus_search.py shopify "merchant account" "حساب التاجر" "payout" "الدفعات" --with "third-party" "مزود دفع خارجي" "مزود" --max 10` (Q5-SH-N02): 6 documents, each a sweep's step 416, the Shopify Payments Terms of Service, none opened;
  - `python3 -I method/corpus_search.py shopify "payment-gateways" "payment gateways" "بوابات الدفع" --max 10` (Q5-SH-N03): no step text from saved HTML listed;
  - `python3 -I method/held_index.py https://www.shopify.com/payment-gateways` (Q5-SH-N03): held, readable only in a fetch archive (`raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz@41642451`); no run step listed. Not read, as outside this re-check's folder;
  - `python3 -I method/corpus_search.py shopify "Payment providers" "مزودو الدفع" "Payment methods" "طرق الدفع" "Activate" "تنشيط" --max 10` (sentences 1 and 2): 716 documents; the first listed were Local payment methods (step 414) and plan pages (step 98);
  - `python3 -I method/corpus_search.py shopify "Additional payment methods" "طرق الدفع الإضافية" "Third-party payment providers" "مزودو الدفع الخارجيون" "Manual payment methods" "طرق الدفع اليدوية" --max 10` (sentence 3): 122 documents, the sweeps' steps 387, 388 and 393;
  - `python3 -I method/corpus_search.py shopify "no longer supported" "Deactivate" "إلغاء التنشيط" "لم يعد مدعومًا" "choose a new provider" --with "payment" "الدفع" --max 10` (sentence 4): 99 documents, the sweeps' steps 388 (provider pages) among them;
  - `python3 -I method/corpus_search.py shopify "Payouts" "الدفعات" "Mark as paid" "وضع علامة مدفوع" "payout account" --max 10` (sentence 5): 460 documents, the first listed the partner payouts pages (steps 373 to 375) and payouts routes (steps 402 to 405); none opened beyond the payouts step below.
- Texts read, under `derived/step-text-from-html/`, with each run's `actions.jsonl` for the step's address, title and date:
  - `20260930T045741Z-sweep-trial2/`: `376`, `377`, `383`, `387`, `393`, `397`, `414` (`.html.txt`);
  - `20261002T003831Z-sweep-capture-plus/`: `376`, `387`, `388`, `477`;
  - `20261002T004032Z-sweep-capture-grow/387`;
  - `20260930T103225Z-sweep-dev/`: `376`, `387`, `388`, `397`;
  - `20260930T002940Z-sweep-trial/388`;
  - `20260930T025819Z-journey-buyer-checkout/`: the Payment sections of `039` and `040`.
- To compare with the trees: `steps/387.aria.yaml` and `376.aria.yaml` of `20260930T045741Z-sweep-trial2`; `376`, `387` and `388` of `20261002T003831Z-sweep-capture-plus`; `388` of `20260930T002940Z-sweep-trial`.

### Open items

- Q5-SH-N01: unchanged. The search listed no step text from saved HTML. The search was added to `searched`.
- Q5-SH-N02: unchanged. The search listed only the Shopify Payments Terms of Service steps, whose snippets are about Shopify Payments and cryptocurrency payout accounts. The search was added to `searched`.
- Q5-SH-N03: unchanged in what is missing. No step's page is the payment gateways page. The two provider lists read here (Q5-SH-094, Q5-SH-095) were added to the row's parenthesis, and its `read` and `searched` were extended.
- No copied gap is cited by `account.md`. No row is routed to the founder or to either. Q5's draft isn't written, so there is no "For the draft" list.

### Wording

- Q5-SH-N03: "stores with countryCode YE" became "stores with countryCode YE or Store address Yemen", since store capture-plus's country is stated by its General page (Q5-SH-C153), not by an answer read here. Its other details are unchanged; the quoted phrases of the three rows were checked in the previous re-check.

### Stores and what the texts are

- Each new statement is from a saved page's markup, said so in its `note`. Q5-SH-098 is a dialog's text that the step's `aria.yaml` does not show; the note says it is in the markup, not shown as open. No recorded text stands between `⟦hidden⟧` and `⟦/hidden⟧`.
- The card labels in Q5-SH-094 and Q5-SH-095 are `accessibilitylabel` attributes as the text file gives them; the aria trees show the provider names and Supports 3DS but not these labels.
- Store capture-plus is named as the step addresses (`/store/capture-plus/`) give it. Its country, store type and currency come from the same run's General settings page (step 477, Q5-SH-C153). The page titles of these steps end "Shopify Plus"; no plan name was recorded as scope.
- Store fake-demo-sharrwah (Q5-SH-098) is named by the step address; its countryCode is cited from the paid-store sweep's PaymentProviders answer (Q5-SH-C128, observed 2026-10-05), a different date from the step's.
- Store ibx5bt-xy (Q5-SH-094): countryCode from Q5-SH-C121.
- The same five-provider list was also in the saved HTML of `20261002T004032Z-sweep-capture-grow/387` and `20260930T103225Z-sweep-dev/387`. Not recorded again. The development-store notice and Test payment gateway text were also in `20260930T103225Z-sweep-dev/376` and `388`. Not recorded again.
- The buyer checkout journey's step 39 (store demo-fake-dev-store) showed Credit card with Testing instruction under Payment. Not recorded: it is a development store's test gateway and adds nothing to Q5-SH-096 and Q5-SH-097.
- The payouts routes of `20260930T045741Z-sweep-trial2` and `20260930T103225Z-sweep-dev` (step 397) read "There's no page at this address".
- The Payments page of `20260930T045741Z-sweep-trial2` (step 376) holds a two-step authentication dialog ("You need to set-up two-step authentication before adding a bank account."), not in its aria tree. Not recorded.

### Not read

- The sweeps' steps 416 (Shopify Payments Terms of Service, covered by copies), 398 to 413 and 415, the capture-advanced sweep, the sweep-instances runs' provider pages, the partner payouts pages, and the frames of the checkout journey.

### Problems

- `corpus_search.py` has no option to search one corpus, so each search ran over every corpus; seven searches run together took about four minutes. The run-steps corpora were listed but not opened, as this re-check reads only the saved-HTML texts.
- To name store fake-demo-sharrwah, the first row of `20260930T002940Z-sweep-trial/answers.jsonl` was looked at; the step's address names the same store.
