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
