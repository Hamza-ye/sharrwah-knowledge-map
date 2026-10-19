# Notes: Q4 on WooCommerce (checking run)

## What was read

- Held captures (read 2026-10-19, through their text files): woocommerce.com/document/bacs/, /cash-on-delivery/, /cheque/ (capture run 20261012T104936Z-s01-sources); /managing-orders/order-statuses/, /woo-mobile-app-point-of-sale-mode/ (searched with grep, lines read around matches), /woocommerce-analytics/ (searched with grep, lines read around matches) (capture run 20261010T235357Z-q1-woocommerce-sources).
- Release files, read by line ranges only: includes/class-wc-post-types.php 440-450; includes/gateways/cod/class-wc-gateway-cod.php (grep of its strings); includes/gateways/cheque and bacs gateway (grep); includes/admin/meta-boxes/views/html-order-items.php 400-415; includes/rest-api/Controllers/Version2 and Version3 orders controllers (grep for set_paid); includes/class-wc-order.php 352-367; includes/wc-order-functions.php 134-140; src/Internal/Orders/IppFunctions.php 1-80.
- Corpus searches: one for the question's topics ("offline payment", "offline payments", "cash on delivery", "direct bank transfer", "check payments", --max 10), then one each for sentences [1], [3], [4] and [5]; the commands for [1], [3] and [4] are in not-found.tsv. The [5] search: `python3 -I method/corpus_search.py woocommerce "collect on delivery" "cash on delivery" "COD" "pay on delivery" --with "WooCommerce Shipping" "shipping label" "shipping labels" "In-Person Payments" "card reader" --max 10`; opened src/Internal/Orders/IppFunctions.php and the COD page.
- WooCommerce's material is in English only; no other language was searched.
- No live page was read.

## Account points not checked

The per-sentence searches did not include terms for these account points, so they were not checked and stay out of account.md:
- Salla [1] usage agreement article 8 (Q4-SA-P0080, Q4-SA-P0081); Salla [1] Salla Point custom payment methods (Q4-SA-034, Q4-SA-035).
- Salla [2] plan feature lists (Q4-SA-K1604, Q4-SA-K1605, Q4-SA-K1580).
- Shopify [3]: no pending-payment email (Q4-SH-020); partial payments (Q4-SH-021 to Q4-SH-024); draft order amount received (Q4-SH-026); payment terms (Q4-SH-014, Q4-SH-015, Q4-SH-019, Q4-SH-K0917, Q4-SH-K1448); deleting and cancelling orders (Q4-SH-030, Q4-SH-031, Q4-SH-032); payment method shown in reports (Q4-SH-033, Q4-SH-034).
- Salla [3]: bank transfer payment period (Q4-SA-017, Q4-SA-047); COD confirmation message (Q4-SA-063); orders filtered by payment method (Q4-SA-002); order API payment object (Q4-SA-059, Q4-SA-060, Q4-SA-061, Q4-SA-K0577); Salla Point drawer reports (Q4-SA-042, Q4-SA-043, Q4-SA-044); reports by payment method (Q4-SA-049, Q4-SA-052, Q4-SA-051); shipping reports (Q4-SA-064, Q4-SA-065); Salla Point methods in reports (Q4-SA-036, Q4-SA-037); nine statuses (Q4-SA-011, Q4-SA-K0598, Q4-SA-K0599).
- Shopify [4]: multi-currency (Q4-SH-K1739, Q4-SH-010); Canada (Q4-SH-027); B2B (Q4-SH-029); API scopes and fields (Q4-SH-036, Q4-SH-042, Q4-SH-043).
- Salla [4]: one COD order per customer per day (Q4-SA-020); label cancellation (Q4-SA-012); Salla Point with lapsed card subscription (Q4-SA-040).
- Salla [5]: carrier-to-Salla flow and payout schedule (Q4-SA-P0041, Q4-SA-P0042, Q4-SA-P0039, Q4-SA-P0093, Q4-SA-K1587); wallet COD tab (Q4-SA-P0038, Q4-SA-023, Q4-SA-024, Q4-SA-025, Q4-SA-K1590); UAE and Kuwait (Q4-SA-K1602, Q4-SA-P0150); order API cash_on_delivery (Q4-SA-060). Shopify [5] COD apps (Q4-SH-045, Q4-SH-046).

Account points resting only on N, G or H ids were not sorted: Shopify Q4-SH-G0101, Q4-SH-G0102, Q4-SH-N01 to N04; Salla Q4-SA-N01 to N03, Q4-SA-G0117, Q4-SA-H0008.

## Copies

- Copied gaps (Q4-WC-G0002 to G0134) concern who is responsible for, and why WooCommerce places, offline methods, analytics, orders, refunds, In-Person Payments and Point of Sale. None bears on a matter this run read for; none is cited.
- No copy was found wrong. Q4-WC-K0443 repeats Q4-WC-K0438.
- The In-Person Payments documentation (Q4-WC-K0439) lists ten countries; the release code (Q4-WC-038) checks only US/USD and CA/CAD. Both are recorded as read.

## Problems

- For one shell loop reading the captures' raw.html dates, the working directory was set inside evidence/product-class/runs, against the run's constraint. Only grep was run there; nothing was written.
- The brief's single per-sentence search, with its terms chosen before reading, left many account points unchecked (listed above).
- The corpus search prints two different commits of this repository for the same capture (7d4a58f… and 5597a2f…); captures are cited by URL.
