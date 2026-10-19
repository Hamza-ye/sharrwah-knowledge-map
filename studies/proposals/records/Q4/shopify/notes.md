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
