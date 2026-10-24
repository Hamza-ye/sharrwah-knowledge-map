# Q3, WooCommerce: notes (checking run)

## What was read

- Step 1: `selection.tsv` judged by terms, and by `copy_statements.py show` for WC-C-001, 002, 003, 004, 005, 012, 015, 016, 021, 027, 030, 034, 048, 051, 053, 054, 055, 066, 081, 089, 090, 118 and S-01. 26 rows copied (S-01 included), 48 set aside.
- The in-depth accounts: `records/Q3/shopify/account.md`, `records/Q3/salla/account.md`, `records/Q3/zid/account.md`. `check_proposals.py records Q3 <platform>` reported no issues for each. Ids looked up in the Shopify folder: Q3-SH-K2276, Q3-SH-P0046, Q3-SH-K1539, Q3-SH-K1540, Q3-SH-011, Q3-SH-089, Q3-SH-090, Q3-SH-091 (8). None in the Salla or Zid folders.
- `copied-view.tsv`, read once after the accounts; `copied-gaps.tsv` listed by concern; `copied-pilot-gaps.tsv` and `copied-pilot-absences.tsv`.
- Topic search (no map is held): `python3 -I method/corpus_search.py woocommerce "requirement" "requirements" "eligibility" "verification" "verify your" "Know your customer" "Launch your store" "before you can" --max 10`. Read from it: woocommerce.com/document/woopayments/our-policies/know-your-customer/; woocommerce.com/document/woopayments/our-policies/ (capture 20261012T104936Z-s01-sources item 091; `held_index.py` names the earlier capture item 066 for this URL). Also read, as a document the topics led to, in the release: `src/Admin/Features/OnboardingTasks/Tasks/LaunchYourStore.php`, `src/Admin/Features/OnboardingTasks/TaskLists.php` (lines 100-140), `src/Admin/Features/LaunchYourStore.php` (grep only), `includes/admin/settings/class-wc-settings-site-visibility.php` (grep only), `src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsService.php` (lines 28-80 and a grep).
- Sentence [1] search, for the account points not yet matched: given in `not-found.tsv` rows N01-N06. Read from it: woocommerce.com/document/woopayments/startup-guide/, .../our-policies/prohibited-and-restricted-products/, .../settings-guide/ (lines 108-125).
- Sentence [4] search: given in rows N07-N09. Read from it: woocommerce.com/document/woopayments/payment-methods/local-payment-methods/ (by grep, then lines 25-30, 66-72 and 99-112 of its text).
- All pages read were held captures (their text files, `access_path` = rendered), read on 2026-10-19. No live page was read.

## Added search (second run, after the brief's items 8 and 10 were fixed)

- Why: the first sentence searches for [1] and [4] carried only some of the unmatched account points' terms; the fixed item 8 allows one more search for the points left out, and sentences may share it. The points and their terms are listed in the scratch file `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/records/Q3-woocommerce/left-out-points.txt`.
- Search, shared by [1] and [4]: the command given in `searched` of rows Q3-WC-N10 to N20. Read from it (4 of 5 allowed): woocommerce.com/document/shop-currency/, woocommerce.com/document/google-for-woocommerce/get-started/product-feed-information-and-free-listings/ (by grep), woocommerce.com/document/cash-on-delivery/, woocommerce.com/document/woopayments/account-management/. One more statement (Q3-WC-049) was recorded from the startup guide read in the first run.
- New: statements Q3-WC-042 to 051, citations Q3-WC-C049 to C058, rows Q3-WC-N10 to N20. Rows were chosen in item 10's order: points on money flows, legal structure and partner contracts first (N10-N19), then [1] in the accounts' order (N20).

## Account points not checked

Past the 20th row: Salla [2] Mahally and the wholesale market (Q3-SA-061); Zid [1] national address (Q3-ZD-039), promotional licences (Q3-ZD-052); Zid [2] Nafath (Q3-ZD-P0117), digital products (Q3-ZD-P0159), sender name, WhatsApp and the mobile app (Q3-ZD-K0509); Shopify [4] "Hemp" (Q3-SH-056); Zid [4] bank-transfer subscriptions (Q3-ZD-048).

Not sorted against, as they rest only on not-found rows or copied gaps: Shopify [4] "Admin request" (Q3-SH-N03); Zid [2] "No check by Zid" (Q3-ZD-N03); Zid [4] "Zid's stated reason" (Q3-ZD-G0002); Salla [4] "Still open". Shopify [4] "Shop" (Q3-SH-030), "Europe and the United Kingdom", "Providers and entities", the Salla and Zid points listed in the first run's version of this section are now sorted or have rows.

## What couldn't be read

- The Site visibility settings' text is in built JavaScript; the PHP class holds only its label.
- The full prohibited and restricted businesses list, Alipay's Terms of Service and the Weixin Pay Proper Use Rules, to which the pages link, were not opened.

## Copies

- None found wrong or out of date.

## Problems

- One command, a search of the release for the launch-your-store code, began with a `cd` into `/home/user/woocommerce-release/11.2.1/woocommerce` before running `grep` with absolute paths. Nothing was run from that folder other than `grep`, and nothing was written there. In the second run, one command reading the shop-currency capture began with a `cd` into `evidence/product-class/runs` (output discarded) before `wc` and `awk` with absolute paths; nothing was written there. No other command changed directory.
- The account's length counts its point names; it sits at about 1,080 words without ids, under the fixed cap of about 1,200.
