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
