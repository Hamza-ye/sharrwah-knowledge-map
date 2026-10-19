# Notes: Q4 on BigCommerce (checking run)

## What was read

All held, from this repository's capture runs; no live page was read, and no founder's save (PDF) was opened.

- support.bigcommerce.com (capture run 20261013T053949Z-s01-bigcommerce-help-founder-machine): Offline-Payment-Methods?language=en_US (whole), Processing-Refunds, Creating-a-Manual-Order, Order-Statuses, Available-Payment-Gateways?language=en_US (offline and APM sections), Pricing (Open Payment Provider fees, Eligible Orders), B2B-Edition-Settings (Invoices, Purchase Order, FAQ), Using-Multiple-Currencies, Getting-Started-Payments, Intro-to-APMs, Getting-Started-Channels (POS lines), Testing-Shipping-Tax-and-Payment-Settings, B2B-Edition-User-Roles-and-Permissions (payment-terms rows), Checkout-Settings (offline lines only).
- docs.bigcommerce.com: api-reference/rest/b2b/management/payment.md (supported payment methods table), docs/admin/checkout-and-cart/orders/overview.md (transactions example, order source), docs/admin/checkout-and-cart/payments/overview.md (status and offline lines).

## Tables

- The B2B Edition supported-payment-methods table (payment.md) has more than 20 rows. Recorded only the rows for offline and manual payment: `bankdeposit`, `bigcommerce`, `bpay`, `cheque`, `cod`, `instore`, `moneyorder`. Not recorded: the gateway rows, `storecredit` and `testgateway`.

## Searches

- Sentence [1] had two searches: a first one (POS, carriers, contract of sale) and, since that one left out the Money dashboard, a second one that added it with `--with`. N02 gives both commands.
- Sentences [3] and [4] each had a second, supplementary search for account points the first left out (automatic status, payment deadline, carrier commission, cash drawer, shipping labels, exchange rate; Canada, POS, subscription, shipping labels). The rows they serve (N09 to N12, N15) give that command.
- No row needed a founder route: none of the missing items is named by BigCommerce's own material as a page or setting.

## Copies

- No copy was found wrong or out of date.
- `copied-pilot-absences.tsv` holds no rows.

## Points not checked

None: 16 not-found rows were recorded, under the 20-row cap. Points that rest only on N or G ids in the accounts (Shopify Q4-SH-N01 to N04, Q4-SH-G0101 and G0102; Salla Q4-SA-N01 to N03, Q4-SA-G0117) were not sorted against, as the brief says.

## Problems with the method

- The repository's HEAD commit changed between corpus searches during the run (7d4a58f6…, 5597a2f5…, 3e1d174b…), so held captures are cited by URL, as the brief says, and `read` names them by URL.
- `access_path` for held captures is set to `local`; the brief's column list doesn't say which value a captured page takes.
