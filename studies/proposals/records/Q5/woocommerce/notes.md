# Notes: Q5 on WooCommerce (checking run, 2026-10-19)

## What was read

- `selection.tsv`: 23 concerns copied, 59 set aside, and S-01 copied as already set. The copy gave 521 statements, 30 gaps, 172 pilot statements, 3 pilot gaps and 1 pilot absence.
- The accounts of shopify, salla and bigcommerce for Q5. The checker reports no issues for any of their folders, and no ids were looked up in them.
- `copied-index.tsv` whole, and `copied-view.tsv` once. The copied gaps were read for the concerns copied; the pilot's gaps and absence were read too.
- Held WooCommerce 11.2.1 release files, searched with grep and read around the lines cited:
  - `src/Internal/Admin/Settings/PaymentsController.php`
  - `includes/class-wc-payment-gateways.php`
  - `includes/abstracts/abstract-wc-payment-gateway.php`
  - `includes/gateways/cod/class-wc-gateway-cod.php`
  - `src/Enums/PaymentGatewayFeature.php`
  - `src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php`
  - `includes/wc-rest-functions.php`
  - `includes/rest-api/Controllers/Version2/class-wc-rest-payment-gateways-v2-controller.php`
  - `src/StoreApi/Utilities/PaymentUtils.php`
  - `includes/admin/settings/class-wc-settings-advanced.php`
  - `includes/admin/class-wc-admin-setup-wizard.php`
- Held captures, read in English: the WooPayments pages on local payment methods, whether WooPayments is required, the settings guide, buy now pay later, the WooPayments vs. Stripe comparison, deleting an account, and negative balances; the POS mode page; the Subscriptions page; the Stripe page; the WooCommerce Square page; the PCI DSS compliance page; the raw `payment-gateway-api.md`; and https://stripe.com/legal/ssa-service-terms and https://woocommerce.com/products/, searched with grep only.
- Live pages: none.

## What couldn't be read

- https://wordpress.com/tos/ is held, but both captures are 403, so it is not readable. The copies cite it, and this run neither read it nor routed it to the founder.

## Copies

- None was found wrong or out of date. Statement Q5-WC-016 records the whole "Types of payment gateway" list. Copies Q5-WC-K0005 and Q5-WC-K0031 hold items 1 and 4 of that list in part.

## Points not checked

No row was recorded for these account points. No search of this run carried their terms, and each sentence's searches were already used.

- Salla [1]: Q5-SA-020 (Emkan) and Q5-SA-068 (Tabby keys).
- Salla [2]: Q5-SA-016 (market selector), Q5-SA-059 (cash on delivery hidden from banned customers) and Q5-SA-063 (Recurring Payments scope).
- BigCommerce [1]: Q5-BC-072 (notifications and logs), Q5-BC-073 (methods per currency), Q5-BC-K0182 (B2B per Company), Q5-BC-081 (local method prerequisites) and Q5-BC-101 (Embedded list "based on current partner classifications").
- Salla [3]: Q5-SA-P0073 (charities), Q5-SA-004 (service provider definition), Q5-SA-062 (Recurring Payments), Q5-SA-K1638 (other gateways collect instead) and Q5-SA-008 (salla.com/payments).
- BigCommerce [3]: Q5-BC-006 (Available Payment Gateways list), Q5-BC-075 (integration counts), Q5-BC-086 (orders through the API and POS), Q5-BC-105 (Embedded Providers integrate directly) and Q5-BC-P0022 (consumer financing and BitPay).
- Shopify [4]: Q5-SH-021 (third-party providers moving to new integrations) and Q5-SH-047 (Shop Pay Express).
- Salla [4]: Q5-SA-K1654 (Tap and K net) and Q5-SA-058 (charity gateway switch).
- BigCommerce [4]: Q5-BC-092 (B2B method removal), Q5-BC-P0080 (PayPal Checkout migration) and Q5-BC-P0035 (legacy Stripe method).
- Shopify [5]: Q5-SH-K1742 (local methods in payouts).
- BigCommerce [5]: Q5-BC-P0091 (Stripe OCS and Braintree timing).

## Problems with the method

- The checking brief changed on disk during the run, on 19 October 2026. The new text allows a second search per sentence for points the first search left out, and asks for a row for each unshown point up to 20. The run followed it from then on: 17 rows were recorded, and the unmatched points are listed in the scratch directory's `unmatched-points.md`.
- For [1], three corpus searches were run: the first one, a search for "at the same time" (with WooPayments, Stripe and PayPal), run before the brief changed, and the second search for points left out. That is one more than the revised brief allows.
- The repository's HEAD moved during the run. Held paths in `read` are given at commit 3e1d174b368f5e02692393624d97b26968c1cf54, at which the capture files exist.
