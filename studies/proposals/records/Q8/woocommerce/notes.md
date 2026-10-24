# Q8, WooCommerce: notes

## Selection

- 37 concerns copied. 83 set aside, including S-01. Each row's reason is in `selection.tsv`.
- `show` was run for WC-C-088, WC-C-034 and WC-C-033. The rest were judged by their terms.
- Copies: 681 statements and 69 gaps. WC-C-004 accounts for 286 of the statements, mostly `$country_extensions[...]` rows. For those rows only the identifiers were read, plus K0051 to K0063 and K0334 to K0336.

## What was read

**Release files (woocommerce-11.2.1), searched with grep and read around each hit:**
- `readme.txt` (header and Description)
- `woocommerce.php` (header)
- `src/Packages.php` (lines 1 to 80, plus the notice strings)
- `src/Internal/Features/FeaturesController.php`: docblock lines 195 to 318; feature definitions 319 to 728; the Features screen section 1470 to 1485
- `includes/react-admin/feature-config.php`
- `includes/wc-core-functions.php` (lines 2272 to 2295)
- `src/Utilities/PluginUtil.php` (lines 85 to 100)
- `src/Internal/Admin/FeaturePlugin.php` (around line 228)
- `src/Admin/RemoteSpecs/RuleProcessors/IsWooExpressRuleProcessor.php`
- `src/Admin/RemoteSpecs/RuleProcessors/BaseLocationCountryRuleProcessor.php` (header)
- `src/Admin/RemoteSpecs/RuleProcessors/GetRuleProcessor.php` (only its `case` lines)

**Captured pages (held):**
- https://woocommerce.com/products/
- https://woocommerce.com/product-category/woocommerce-extensions/
- https://woocommerce.com/product-category/woocommerce-extensions/conversion/ (Country filter lines only)
- https://woocommerce.com/product-category/woocommerce-extensions/merchandising/ (Country filter lines only)
- https://developer.woocommerce.com/llms.txt was used only as an index to find documentation addresses. It is not counted as reading those pages.

**Live pages,** read on 2026-10-19 as raw Markdown files with curl. All five were served in English. Working copies are in the scratch directory.
- https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/contribution/releases/schedule.md (English)
- https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/contribution/releases/prereleases.md (English)
- https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/extensions/core-concepts/example-header-plugin-comment.md (English)
- https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/submitting-your-product.mdx (English)
- https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/excellence-verified-badge.md (English)

All five were read for sentence [3], which reached its limit of 5 live pages. No live pages were read for [1] or [2].

## Not read

These were found in the llms.txt index but not read, because the live-page limit for [3] was reached:
- `woo-marketplace/monetization-expectations.md`
- `product-update-guidelines.md`
- `billing-api-saas.mdx`
- `managing-products.md`
- `contribution/contributing/deprecation-in-core.md`
- `contribution/releases/security-support.md`
- `testing/beta-testing.md`

Also not read: https://developer.woocommerce.com/release-calendar/ and https://woocommerce.com/pricing/, which is not held (Q8-WC-N01).

## Tables and lists

- **FeaturesController feature definitions** (about 30 entries). Only the entries recorded in Q8-WC-016 to Q8-WC-029 were recorded. These entries were left out:
  - `analytics`
  - Product gallery videos
  - `cart_checkout_blocks` (already copied, K1275)
  - `rate_limit_checkout`
  - `order_withdrawal`
  - `order_attribution`
  - `site_visibility_badge`
  - `hpos_fts_indexes`
  - `hpos_datastore_caching`
  - `remote_logging`
  - `deferred_transactional_emails`
  - `email_improvements`
  - `wc-visual-attribute`
  - `fulfillments`
  - `destroy-empty-sessions`
  - Push Notifications (already copied, K1326 and K1327)
  - `rest_api_caching` (already copied, K1138)
  - `cart_save_for_later`
  - `product_wishlist`
  - Cache Product Objects
  - Back in Stock Notifications
  - Unified block editor assets
  - the HPOS and Cost of Goods Sold definitions that other classes add
- **`GetRuleProcessor` rule types** (21 `case` lines). Only `is_woo_express` and `base_location_country` were recorded, through their classes (Q8-WC-036 and Q8-WC-037).
- **Pre-releases table:** all 6 rows were recorded (Q8-WC-049 to Q8-WC-054). For the rows `-beta.2`, ... and `-rc.2`, ..., the citation quotes only the timing cell. The release name holds a literal "...", and the checker rejects quotes containing ellipses. The statement keeps the source's text.

## Method problems

- Statements that joined two non-consecutive passages failed the checker's verbatim test. They were split into one statement per passage, which is why several statements share an identifier. Examples are `Packages::$base_packages` and `features: marketplace`.
- `$alpha_feature_testing_is_enabled` (`WOOCOMMERCE_ENABLE_ALPHA_FEATURE_TESTING`) is assigned at line 315 of `FeaturesController.php`, but no other use of it was found in that file. It was not recorded.

## Copies

- No copy was found wrong.
- The checker reported no copy as changed.
