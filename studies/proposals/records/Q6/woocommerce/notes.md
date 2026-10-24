# Notes: Q6 on WooCommerce (checking run)

## Selection

18 concerns copied, 51 set aside (S-01 included), none added. 421 statements and 26 gaps were copied.

## What was read

Accounts read: Shopify, Salla and Zid (`records/Q6/<platform>/account.md`). The checker reported no issues for any of them. No account ids were looked up.

Searches, all `python3 -I method/corpus_search.py woocommerce ... --max 10`, in English (WooCommerce's material held here is English):
- Topics: "store address" "where your business is located" "sign up" "eligible" "supported countries" "not available in your country". Read: StoreDetails.php, class-wc-settings-general.php, class-wc-admin-settings.php, class-wc-countries.php and i18n/countries.php (release files, searched with grep); https://woocommerce.com/document/woopayments/compatibility/countries/; https://woocommerce.com/document/configuring-woocommerce-settings/general/; https://woocommerce.com/document/woo-mobile-app-point-of-sale-mode/.
- [1], first: "18 years" "age of majority" "legal age" "legal name" "account owner" "accounts owners" "business registration" "identity verification" "proof of address" "refuse" "business type" "business types" "individual" "individuals" "change country". Read: the WooPayments know-your-customer and account-management pages.
- [1], second: "You must be" "years old" "minimum age" "eligible to use" "your account" "accurate". Nothing new in it. The Terms of Service (https://wordpress.com/tos/) is held only as 403 captures (evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/101-wordpress.com, evidence/product-class/runs/20261012T104936Z-s01-sources/items/104-wordpress.com), so I read it live.
- [2], first: "not available in your country" "isn't available" "is not available" "not supported in your country" "alternative" "alternatives" "third-party payment" "available countries" "available in" "only available". Read: src/Internal/Admin/WCPayPromotion/DefaultPromotions.php (WooPay countries `array( 'US' )`, which copy Q6-WC-K0447 already shows), and the buy-now-pay-later, local-payment-methods and Google for WooCommerce product-feed pages.
- Shared by [1] and [2], for the points left out of the searches above. The command is in `not-found.tsv`. Read: the payout-currencies, is-woopayments-required-to-take-payments and why-payouts-suspended pages.

Live page read: https://wordpress.com/tos/, raw HTML, served in English (`lang="en"`), read 2026-10-19 and marked "Last Updated: October 6, 2026". My working copy is in the scratch directory. No other live page was read.

## Left out

- In the payout-currencies tables, I recorded only the "United Arab Emirates" and "Other supported countries" rows of the first chart. Its other 12 rows and the second chart were left out.
- The buy-now-pay-later table shows which provider is available in which country only as marks that aren't text, so I recorded none of its rows.
- Account points past the 20th not-found row, not checked: Salla [1] Q6-SA-018 (acknowledging official procedures before registering), Q6-SA-041 (waqf legal representative), Q6-SA-046 (Emirates ID starting 784) and Q6-SA-047 (licence issued on an alternative ID).
- Account points not sorted because they rest only on N or G ids: Shopify Q6-SH-N01, N02, N03, G0009, G0011, G0216 and G0217; Salla Q6-SA-G0160, G0162, G0176, G0177, G0213, G0214, N01, N02, N03 and N04; Zid Q6-ZD-G0041, G0044, G0045, G0047, G0049, G0055, G0057, G0058, N01, N02 and N03.

## Problems with the method

- The briefs were revised during this run, on 19 October. The [1] searches and the first [2] search had already been run when the revision asked for the unmatched points to be listed first, every point's terms to go in one call, and at most two searches per sentence. I then listed the points in the scratch directory (`unmatched-points.md`) and ran one more search, shared by [1] and [2], for the points left out. [1] therefore had three searches, not two.
- The shared search left out some terms I had listed: "plan", "plans", "fees", "language", and any term for country pages. Rows Q6-WC-N01, N05, N13 and N15 cite that search, but it carried only part of their points' terms.
- In that shared search, "marketplace" matched the footer of nearly every captured woocommerce.com page, so its first ten captured results were chosen by the footer.
- Between searches the corpus search printed different repository commits (3e1d174…, a5798659…, dcabee22…). Each not-found row's `read` field uses the commit its search printed.

## Copies

I found no copy wrong or out of date.
