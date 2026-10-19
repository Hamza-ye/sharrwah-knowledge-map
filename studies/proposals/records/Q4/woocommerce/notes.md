# Notes: Q4 on WooCommerce (checking run)

## What was read

- Held captures (read 2026-10-19, through their text files): woocommerce.com/document/bacs/, /cash-on-delivery/, /cheque/ (capture run 20261012T104936Z-s01-sources); /managing-orders/order-statuses/, /woo-mobile-app-point-of-sale-mode/ (searched with grep, lines read around matches), /woocommerce-analytics/ (searched with grep, lines read around matches) (capture run 20261010T235357Z-q1-woocommerce-sources).
- Release files, read by line ranges only: includes/class-wc-post-types.php 440-450; includes/gateways/cod/class-wc-gateway-cod.php (grep of its strings); includes/gateways/cheque and bacs gateway (grep); includes/admin/meta-boxes/views/html-order-items.php 400-415; includes/rest-api/Controllers/Version2 and Version3 orders controllers (grep for set_paid); includes/class-wc-order.php 352-367; includes/wc-order-functions.php 134-140; src/Internal/Orders/IppFunctions.php 1-80.
- Corpus searches: one for the question's topics ("offline payment", "offline payments", "cash on delivery", "direct bank transfer", "check payments", --max 10), then one each for sentences [1], [3], [4] and [5] (first pass), and one more each in the second pass; the commands are in not-found.tsv. The [5] search: `python3 -I method/corpus_search.py woocommerce "collect on delivery" "cash on delivery" "COD" "pay on delivery" --with "WooCommerce Shipping" "shipping label" "shipping labels" "In-Person Payments" "card reader" --max 10`; opened src/Internal/Orders/IppFunctions.php and the COD page.
- WooCommerce's material is in English only; no other language was searched.
- No live page was read.

## Searches added (second pass, after the brief's items 8 and 10 were fixed)

The first per-sentence searches left out the terms of about 30 account points. The left-out points, with their terms, are listed in /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/records/Q4-woocommerce/left-out-points.md. One more search was run for each sentence that had such points ([2] had none before, and shares [1]'s added search); each command is in the `searched` field of the rows it carries (N05 to N20):
- [1] and [2]: terms for the usage-agreement point, intermediary payments in point of sale, and plan lists. No listed document was opened: the snippets show icon code, WooPayments pages and Stripe's agreements.
- [3]: terms for pending-payment emails, partial payments, payment terms, deleting and cancelling, reports by payment method, payment periods, order-received messages, the order API's payment fields and cash drawers. Opened: order-statuses page, roles-capabilities page, ListTable.php, thankyou.php, V4 OrderSchema.php.
- [4]: terms for multi-currency, e-transfers, B2B, order permissions, per-customer limits and label cancelling. Opened: shop-currency page.
- [5]: payout and balance terms with In-Person Payments and cash on delivery. Opened: woopayments/managing-money/ and woopayments/settings-guide/ (searched with grep).

They added statements Q4-WC-039 to Q4-WC-047 and rows Q4-WC-N05 to Q4-WC-N20.

## Account points not checked (past the 20th row)

- Shopify [4]: B2B drafts (Q4-SH-029).
- Salla [4]: one COD order per customer per day (Q4-SA-020); label cancellation (Q4-SA-012); Salla Point with a lapsed card subscription (Q4-SA-040).

Account points resting only on N, G or H ids were not sorted: Shopify Q4-SH-G0101, Q4-SH-G0102, Q4-SH-N01 to N04; Salla Q4-SA-N01 to N03, Q4-SA-G0117, Q4-SA-H0008.

## Copies

- Copied gaps (Q4-WC-G0002 to G0134) concern who is responsible for, and why WooCommerce places, offline methods, analytics, orders, refunds, In-Person Payments and Point of Sale. None bears on a matter this run read for; none is cited.
- No copy was found wrong. Q4-WC-K0443 repeats Q4-WC-K0438.
- The In-Person Payments documentation (Q4-WC-K0439) lists ten countries; the release code (Q4-WC-038) checks only US/USD and CA/CAD. Both are recorded as read.

## Problems

- For one shell loop reading the captures' raw.html dates, the working directory was set inside evidence/product-class/runs, against the run's constraint. Only grep was run there; nothing was written.
- The first pass's single per-sentence search left about 30 account points unchecked; the second pass covered them (above).
- The corpus search prints two different commits of this repository for the same capture (7d4a58f… and 5597a2f…); captures are cited by URL.
