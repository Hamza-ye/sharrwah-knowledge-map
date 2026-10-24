# Notes: Q1 on WooCommerce (R3 check)

Run on 2026-10-19, at medium effort. It was a check against the accounts of Shopify, Salla and BigCommerce.

## Selection

- 28 concerns were copied and 30 set aside, S-01 among them. The copy gives 574 statements and 36 gaps.
- The ones I judged by `copy_statements.py show` were WC-C-001 to 016, 021, 023, 024, 026, 055, 057, 058, 060, 061, 089 and 118.
- I added no concern.

## The accounts

- All three accounts were present, and `check_proposals.py records Q1 <platform>` reported no issues for any of them.
- I looked up no ids in their folders.
- I did not sort against four points, because each rests only on N or G ids:
  - Shopify [2], the last point;
  - Salla [2], the last point;
  - Salla [3], the last point;
  - BigCommerce [5], the last point.

## What was read

WooCommerce has no help map, so I started from the corpus search.

**Topics search.** I ran `corpus_search.py woocommerce "selling location" "selling locations" "shipping zone" "shipping zones" "base location" "store address" "multi-currency" "currencies" "countries" --max 10` and read the following.

Captured pages:
- configuring-woocommerce-settings/general;
- woopayments/currencies/multi-currency-setup;
- woopayments/currencies/currencies-overview;
- shop-currency.

Release files, found by `grep` among the release files the search listed:
- `src/Admin/API/OnboardingProfile.php`, with `i18n/locale-info.php` for the SA and YE entries only;
- `includes/admin/settings/views/settings-tax.php`;
- `includes/admin/settings/views/html-settings-tax.php`;
- `includes/admin/settings/views/html-admin-page-shipping-zones.php`;
- `assets/client/admin/chunks/core-profiler.js`, with a bounded grep only.

**Sentence [1]** (with [2], which has no reading of its own):
- An earlier, narrower search was replaced by the one given in the not-found rows.
- I opened four documents: wordpress.org/plugins/woocommerce, the google-for-woocommerce product-feed page and `src/Internal/Admin/Translations.php` by grep, and woopayments buy-now-pay-later in part.

**Sentence [3]:**
- An earlier, narrower search was replaced by the one given in rows N07 and N08.
- I opened five documents:
  - stripe.com/legal/connect-account;
  - stripe.com/legal/ssa, its section 12 only;
  - buy-now-pay-later;
  - cash-on-delivery and bacs, by grep only. Neither names a country.
- I also ran a separate search for "Connected Account Agreement". It listed woopayments/account-management/partnership-with-stripe, and I read its one paragraph.
- The Stripe agreements were read because WooPayments' own page says the Connected Account Agreement "contains the terms you agreed to during the WooPayments signup process". The Connected Account Agreement in turn incorporates the Stripe Services Agreement.

**Sentence [4]:** I read `html-admin-page-shipping-zones.php` and woopayments/payment-methods/local-payment-methods.

**Sentence [5]:** I read `src/Admin/API/PaymentGatewaySuggestions.php` and woopayments-vs-stripe-plugin-comparison.
- In PaymentGatewaySuggestions, the `install_plugins` check guards only dismissing a suggestion. I recorded nothing from it.

**Live pages:** none were read.

## Tables and lists not recorded in full

- **The Stripe Services Agreement's table of Stripe contracting entities** (section 12) has more than 20 rows. I recorded only the United Arab Emirates and United States rows (Q1-WC-036, Q1-WC-037).
  - Not recorded: Canada, Mexico, Brazil, other Americas, the EEA countries, Gibraltar/Switzerland/United Kingdom, other EMEA, Australia, Hong Kong, India, Indonesia, Japan, Malaysia, New Zealand, Singapore, Thailand and other Asia Pacific.
- **The buy-now-pay-later page's tables** were not recorded:
  - providers by account country;
  - currency by account country;
  - minimum and maximum amounts.
- **The local payment methods page's tables** were not recorded: methods by account country, and customer country and currency requirements.

## Copies

- I found no copy wrong or out of date.
- Several copies repeat the same statement under different ids, for example Q1-WC-K0371, K0377 and K0384. I cited one of each.

## Not-found rows

- I recorded 12 rows, all `not in what was read` with `who_can` = agent. None is routed to the founder.
- No point was left unchecked: every account point other than the four above is either named by a point of this account or cited through a row.

## Problems with the method

- **The commit in the corpus search's paths changed during the run.** The later [3] search printed `2b5ce9fc…` where the earlier searches printed `98f560e8…`. Each row's `read` uses the commit its search printed.
- **Two lists in captured pages could not be quoted in one piece.**
  - "Selling location(s)" contains an ellipsis character ("All countries, except for…"). It was cited by two quotes that avoid it.
  - Two quotes were over 300 characters and were split.
- **The brief changed during the run.** The account limit went from about 800 words to about 1,200. The account follows the new limit.
