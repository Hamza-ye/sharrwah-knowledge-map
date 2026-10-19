# Notes: Q4, shopify

## Selection
- Copied: SH-C-018, SH-C-045, SH-C-054, SH-C-055, SH-C-057, SH-C-062, SH-C-079, SH-C-084, SH-C-087. The other 53 rows, S-01 among them, are set aside, each with a reason in selection.tsv. No concern was added.

## What was read
All held, at observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921. No live page was read.
- Help Center, through help_map.py: manual-payments.md (and its Arabic version content.html/ar/manual/payments/manual-payments.html), manual-payments/email-money-transfers.md, fulfillment/managing-orders/payments.md, payments/deferred-payments.md, payments/pending-payments.md, order-status.md (and the Arabic order-status.html, for the Unpaid row only), refunding-orders.md, create-orders/get-paid.md, payments/partial-payments.md, checkout-settings/test-orders/processing-test-order.md, b2b/checkout-and-orders/checkout-settings.md, canceling-orders.md, reports-and-analytics/.../finances-report.md (payments section only), intro-to-shopify/initial-setup/sell-in-italy/italy-cash-on-delivery.md, customers/customer-accounts/upgrade/customization-options.md (the manual payment line only).
- shopify.dev, held in raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz: orderCreateManualPayment.md (offset 5274404) and orderMarkAsPaid.md (offset 5326539). Also the Order object record at offset 7922646, through grep only.
- Admin GraphQL schema structures/shopify/admin-graphql-schema/2026-10/items.jsonl, through grep only (lines 2358, 2359, 2380).
- Corpus searches: given in not-found.tsv.

## Not read
- The B2B pages payment-methods.md, payment-terms.md and the setup checklists, which the corpus search listed.
- The App Store category for COD apps named on the Italy page.
- Shopify Flow's "Mark order as paid" action page.

## Problems
- Some Help Center sentences hold inline HTML (`<strong>`, `<a>`) right before punctuation. With markup removed, the checker leaves a space before the punctuation, so those sentences don't match verbatim. For the Unpaid row I quoted the Arabic version instead. For the finances report's Payment method row (Q4-SH-033) the statement keeps the source's `<strong>` tags. For pending-payments (Q4-SH-020) the statement stops before the link.
- Help Center pages show no date. source_date gives the date the Help Center capture was held, and the shopify.dev fetch run date for the API pages, as date_basis says.
- No copy was found wrong or out of date.

## Re-check against the observed runs, 19 October 2026

### What was read
- observed-sh's README.md and docs/READING.md, whole, at c8b5fbee25966372a0475e6ed81f0b7760ac2921.
- Corpus searches (all `--max 10`):
  - `python3 -I method/corpus_search.py shopify "Manual payment methods" "manual payment method" "طرق الدفع اليدوية" "Create custom payment method"`
  - `python3 -I method/corpus_search.py shopify "Cash on Delivery (COD)" "cash on delivery" "الدفع عند الاستلام"`
  - `python3 -I method/corpus_search.py shopify "Mark as paid" "markAsPaid" "orderMarkAsPaid" "وضع علامة مدفوع"`
  - `python3 -I method/corpus_search.py shopify "refund" "Refund" "استرداد" --with "manual" "Cash on Delivery" "Bank Deposit" "Money Order"`
  - `python3 -I method/corpus_search.py shopify "Payment pending" "Cash on Delivery (COD)" "معلّق" --with "Payment pending" "Cash on Delivery"`
  - `python3 -I method/corpus_search.py shopify "responsible" "merchant of record" "manual payment" "المسؤول" --with "manual payment" "Manual payment methods"`
  - `python3 -I method/corpus_search.py shopify "Manual payment methods" "manual payment" "طرق الدفع اليدوية" --with "not available" "only available" "Shopify Plus" "country" "غير متاح"`
  - `python3 -I method/held_index.py` on https://admin.shopify.com/settings/payments/manual-payment-methods and https://admin.shopify.com/settings/payments.
- Files, all observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:
  - raw/runs/20261005T013804Z-sweep-paid-store: steps/393.text.txt, steps/376.text.txt, actions.jsonl (step 393), answers.jsonl (steps 376 and 393), answers/admin.shopify.com/PaymentProviders/4c65727d….json.
  - raw/runs/20261002T003831Z-sweep-capture-plus: answers.jsonl (PaymentProviders), answers/admin.shopify.com/PaymentProviders/b7bbabb4….json.
  - The PaymentProviders answers of every run, through a script that printed only each answer's store url, countryCode, plan and manualProviders names (222 files). Every one lists Cash on Delivery (COD), Money Order and Bank Deposit, and every one states countryCode YE. Only the two above are recorded.
  - raw/runs/20260930T014656Z-journey-order-lifecycle: actions.jsonl, answers.jsonl, steps/010, 029 and 030 aria.yaml, and the answers OrderManualPaymentMethods, Order (step 28), RefundCreate, OrderDetailsPayment (step 30), Timeline (steps 10 and 30).
  - raw/runs/20260930T003329Z-pilot-import: answers.jsonl (PaymentProviderCreate row), answers/admin.shopify.com/PaymentProviderCreate/c9701d9e….json.
  - raw/runs/20261007T075321Z-journey-flow-templates: actions.jsonl (steps 27 and 31), answers.jsonl (store names), steps/027 and 031 text.txt and frame-0/frame-1 text.txt.
  - derived/admin-controls.jsonl, through grep only (manual-payment-methods lines).
- New statements: Q4-SH-047 to Q4-SH-058 (12), citations Q4-SH-C053 to Q4-SH-C072.

### Stores
- The Flow templates run's answers.jsonl names its store as capture-plus. Its Flow answers name none.
- The pilot import's PaymentProviderCreate call carries no step. Its date is the call's `t` in answers.jsonl, and the locator gives its HAR entry.

### Open items
- Q4-SH-N01 (Shopify collecting COD money): unchanged. Searches and reads added to the row. Q4-SH-058 and Q4-SH-057 bear on sentences 1, 3 and 5 but don't show a collecting service.
- Q4-SH-N02 (refund of a manually paid order): narrowed. The order-lifecycle journey shows how a refund of an order marked as paid is recorded (Q4-SH-052 to Q4-SH-056). Still missing: whether money moves, as Shopify states it, and the case of an order placed at checkout with a named manual method.
- Q4-SH-N03 (suggested methods list): narrowed. The runs hold the manualProviders the page received (Q4-SH-048, Q4-SH-049), but the page's drop-down is closed in every held step. The route now names the drop-down to open, without the page address, which the checker reports as held: the held page shows the drop-down closed. who_can stays founder.
- Q4-SH-N04 (countries or plans): narrowed. Observations for one Plus store and one other store are recorded (Q4-SH-048, Q4-SH-049). A statement from Shopify is still missing.
- Q4-SH-G0101, Q4-SH-G0102 (responsibility, reason): unchanged. The responsibility search's run hits are Timeline answers ("Marked the manual payment as received") and SurfaceGuides answers that carry the Help Center page. None names a responsible party or a reason.
- No phrases were listed by the coordinator for this folder.

### Wording (step 4)
- N01, N02, N03 and N04 checked against their `read`. "Payment providers", "Manual payment methods drop-down menu" and "suggested manual payment methods" are in manual-payments.md. The App Store category URL is on the Italy page. `manualProviders` and `PaymentProviders` are the answer's keys. No detail was removed.

### Not read
- The other run documents the searches listed: the PaymentProviders answers beyond the summary above, the SurfaceGuides answers, the journey-order-detail and pilot-import Order, Timeline and OrderDetailsPayment answers, and the sweeps' payments sub-pages (steps 378 to 417).
- The pointers ShopifyPaymentsData and MarketsHomeCurrencyOptions, the General settings pages and the third-party providers pages: they don't bear on a sentence of Q4 beyond what is recorded.

### Problems
- A Timeline answer's `additionalContent` (with "Gateway" / "manual") is a JSON string nested in the answer, with escaped quotes. It isn't recorded, because it's unclear how the checker decodes a nested string.

## Re-check against the step text from saved HTML, 19 October 2026

### What was read
- observed-sh's docs/READING.md (the `derived/step-text-from-html/` entry) and `derived/step-text-from-html/meta.json`, at 51626891aa711ee9c3ef2d05ce63c95396dca949. Only that folder's texts were read, with the runs' `actions.jsonl` for steps' addresses, titles and dates, `answers.jsonl` for store names, and `steps/NNN.aria.yaml` to compare each recorded step.
- Corpus searches (all `--max 10`; only their "observed-sh: step text from saved HTML" hits were used):
  - `python3 -I method/corpus_search.py shopify "Cash on Delivery (COD)" "cash on delivery" "الدفع عند الاستلام"`
  - `python3 -I method/corpus_search.py shopify "refund" "Refund" "استرداد" --with "Manual" "Cash on Delivery" "Bank Deposit" "Money Order"`
  - `python3 -I method/corpus_search.py shopify "Manual payment methods" "manual payment method" "طرق الدفع اليدوية" "Create custom payment method" "Bank Deposit"`
  - `python3 -I method/corpus_search.py shopify "Manual payment methods" "manual payment" "طرق الدفع اليدوية" --with "not available" "only available" "Shopify Plus" "country" "غير متاح"`
  - `python3 -I method/corpus_search.py shopify "responsible" "merchant of record" "المسؤول" --with "manual payment" "Manual payment methods"` (no saved-HTML hits)
  - `python3 -I method/corpus_search.py shopify "Mark as paid" "Mark order as paid" "Collect payment" "Record payment" "وضع علامة مدفوع"`
  - `python3 -I method/corpus_search.py shopify "Payment pending" "Payment instructions" "Payment terms" "Due on receipt" "تعليمات الدفع"` (saved-HTML hits for "Payment terms" only)
  - `python3 -I method/corpus_search.py shopify "Custom payment method name" "Additional details" "Amount received" "Email money transfer" "Third-party transaction fees"` (saved-HTML hits for "Third-party transaction fees" only)
- Files, all observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/:
  - 20260930T014656Z-journey-order-lifecycle: 006, 007, 008 and 029 .html.txt (with steps/006.aria.yaml and 029.aria.yaml);
  - 20260930T090458Z-journey-order-detail: 045 and 046 .html.txt (with steps/045.aria.yaml and 046.aria.yaml);
  - 393.html.txt of 20261002T003831Z-sweep-capture-plus, 20261002T004032Z-sweep-capture-grow, 20261002T003931Z-sweep-capture-advanced, 20260930T045741Z-sweep-trial2, 20260930T002940Z-sweep-trial and 20260930T103225Z-sweep-dev;
  - 20261002T003831Z-sweep-capture-plus: 174.html.txt (with steps/174.aria.yaml).
- New statements: Q4-SH-059 to Q4-SH-062 (4), citations Q4-SH-C073 to Q4-SH-C076.

### Stores
- The order-lifecycle and order-detail journeys name their store as demo-fake-dev-store in answers.jsonl; the capture-plus sweep names capture-plus.

### Open items
- Q4-SH-N01 (Shopify collecting COD money): unchanged. The saved-HTML hits for "cash on delivery" are purchase order and New supplier pages, where it is one of a supplier's payment terms. Search added to the row.
- Q4-SH-N02 (refund of a manually paid order; routed to either): unchanged. The saved HTML of the refund page (order-lifecycle step 29) holds "Manual", "Enter manual refund amount", "YER 699.95 available for refund" and "This order is missing a customer. Store credit refunds require a customer."; the step's aria.yaml shows the same words, so nothing is new from this source. Search and read added.
- Q4-SH-N03 (the drop-down's list; routed to the founder): unchanged. The saved HTML of the Manual payment methods page (step 393) in six sweeps holds the headings and "Manual payment method", with no list of methods and no frame. The route stays as written. Search and reads added.
- Q4-SH-N04 (countries or plans): unchanged. The saved-HTML hits are capture-plus Payments pages whose navigation lists "Manual payment methods"; none states a country or plan. Search added.
- Q4-SH-G0101, Q4-SH-G0102 (responsibility, reason): unchanged. The search had no saved-HTML hits.

### Wording (step 4)
- N01 to N04 checked again: no detail they give rests on the new texts, and nothing read contradicts them. No change.

### For the draft
- Q4-SH-012 (Collect payment > Mark as paid): adds Q4-SH-059, Q4-SH-060 and Q4-SH-061. In two journeys on store demo-fake-dev-store, the saved HTML of a draft order and of an order holds a Collect payment menu with the items "Credit card" and "Mark as paid", and the order's Mark as paid dialog reads "Mark this order as paid if you received $1.00 USD from another payment method." (The menu items are in the markup only; the dialog's words are also in the accessibility tree.)
- Q4-SH-014 (payment terms): adds Q4-SH-062. On store capture-plus's New company page, the saved HTML's Payment terms options are No payment terms, Due on fulfillment and Net 7 to Net 90; Q4-SH-014 rests on the Help Center's terms for orders.
- The other Shopify ids the draft cites (Q4-SH-003, 006, 007, 016, 022, 026, 027, 039, 042, 045, 046, 057, K1491, K1737, K1740, N01): the searches above found nothing in the new texts that changes or adds to them. The "0.2% third-party transaction fees apply if not using shopify payments" text on the Shopify Plus upgrade pages (step 422 of the sweeps) doesn't name manual payment methods, so it isn't recorded against Q4-SH-K1740.

### Not read
- The other saved-HTML documents the searches listed: the order-detail and customer-account refund pages, the other order and draft order pages with the Collect payment menu, the purchase order and supplier pages, the B2B company location pages, the Payments sub-pages (steps 378 to 417) and the Plus upgrade pages.

### Problems
- The extracted text keeps markers such as `[accessibilitylabel: Collect payment]` inline with the page's words; the statements quote them as the file holds them.
