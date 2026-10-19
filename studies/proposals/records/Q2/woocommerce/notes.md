# Notes · Q2 · WooCommerce

## Selection

44 concerns set to `copy`, plus S-01; 37 set aside, each with its reason in `selection.tsv`. No concern added. `copy_statements.py copy` wrote 616 copies, 56 copied gaps, 172 pilot statements, 3 pilot gaps and 1 pilot absence.

## What was read (all on 2026-10-18)

Held (captures in this repository, sharrwah-knowledge-map@53c7c948509805be97aa365270136b03dd0a4f84):
- https://woocommerce.com/document/woopayments/payment-methods/local-payment-methods/ (items/072, run 20261010T235357Z-q1-woocommerce-sources): text.txt in full, and raw.html for the WeChat Pay customer section and two links
- https://woocommerce.com/document/woopay-merchant-documentation/ (items/018, run 20261011T084016Z-q1r-woocommerce-more)
- https://woocommerce.com/document/eu-vat-number/ (items/025, run 20261010T235357Z-q1-woocommerce-sources)
- https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/ (items/022, same run): the lines that matched the search
- https://stripe.com/legal/ssa (items/077, run 20261012T104936Z-s01-sources): section 13 Regional Terms, and the lines that matched "embargo", "sanction" and data transfer. The Stripe Connected Account Agreement, accepted at WooPayments signup, points to this agreement (copies Q2-WC-P0103, Q2-WC-P0107).

Release files (woocommerce-11.2.1):
- `src/Internal/OrderWithdrawal/OrderWithdrawalFeatureHighlightNotification.php`, lines 80 to 180
- `src/Internal/Integrations/WPConsentAPI.php`, its doc comments only: no place or law named
- `readme.txt`: the changelog date of 11.2.1 (2026-10-09), used as the source_date of the release citations

Live (1 page):
- https://woocommerce.com/document/woopay-customer-documentation/, rendered through `method/capture/page_text.mjs`, served in English, read 2026-10-18. The working copy is in the scratch directory. Its two quotes are "pending capture".

Corpus searches, all `--max 10`:
1. `"not available in" "only available" "due to regulatory" "regulations" "legal requirements" "sanctioned" "not supported in your country"`
2. `"due to various" "required by law" "country-specific laws" "embargo" "GDPR" "comply with local" "local laws" "regulatory requirements"`
3. `"servers in the United States" "stored in the United States" "data centers" "data centres" "located in the United States" "hosted in"`

Plus one search for each not-found row; `not-found.tsv` gives them.

Among the documents these searches listed, these were not opened:
- the release's code files whose only match was the generic phrase "only available";
- https://woocommerce.com/usage-tracking/ (concern WC-C-035, set aside);
- https://woocommerce.com/document/order-fulfillment/;
- https://woocommerce.com/document/woo-mobile-app-point-of-sale-mode/;
- the bookings REST API reference;
- the Xero pages;
- https://developer.woocommerce.com/llms.txt;
- `includes/class-wc-privacy.php`, `wc-update-functions.php` and `ShopperLists/Privacy/Privacy.php`;
- https://stripe.com/legal/ssa-service-terms.

The KYC page and the WooPayments countries page were not reread, because copies already hold their statements.

## Not read or not recorded

- **Przelewy24's MCC table.** Only its five rows marked for a place are recorded (Q2-WC-024 to Q2-WC-028). The other rows of the table on the local payment methods page were not recorded.
- **Alipay and WeChat Pay site requirements.** The page's bullet list of these requirements was not recorded. Only its reason sentence is (Q2-WC-013).
- **Refund time limits and closed betas.** These parts of the same page were not recorded.
- **Stripe Services Agreement, sections 13.2 onwards.** The Dispute Resolution sections, and the Regional Terms for Brazil, India, Indonesia, Malaysia, Mexico and Thailand, were not recorded. Those six countries are not among WooPayments' listed countries.
- **UAE disclosure list.** The list after "Stripe may disclose or transfer this data and information to its Affiliates" (Stripe Services Agreement, UAE 13.3) was not recorded.
- **Provider terms.** These were not read: the Alipay Terms of Service and the Weixin Pay Proper Use Rules (Q2-WC-N01), and the Stripe Sub-processors List (Q2-WC-N03).
- **Duplicate pilot statement.** The copies Q2-WC-K0405 and Q2-WC-P0171 hold the same statement, from the WooPayments countries page. They come from different sources, the concern map and the pilot, and this is not a problem with either copy.

## Copies found wrong or out of date

None found. The checker reports no copy as changed.

## Problems with the method

- **Nested lists in the account.** The checker counts each item of a nested list in `account.md` as a separate point, so a lead-in item followed by sub-items fails. Points were written as single list items.
- **Table rows.** Rows on the local payment methods page are recorded with single spaces between their cells. The checker accepted them.
