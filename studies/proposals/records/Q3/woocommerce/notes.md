# Q3, WooCommerce: notes (checking run)

## What was read

- Step 1: `selection.tsv` judged by terms, and by `copy_statements.py show` for WC-C-001, 002, 003, 004, 005, 012, 015, 016, 021, 027, 030, 034, 048, 051, 053, 054, 055, 066, 081, 089, 090, 118 and S-01. 26 rows copied (S-01 included), 48 set aside.
- The in-depth accounts: `records/Q3/shopify/account.md`, `records/Q3/salla/account.md`, `records/Q3/zid/account.md`. `check_proposals.py records Q3 <platform>` reported no issues for each. Ids looked up in the Shopify folder: Q3-SH-K2276, Q3-SH-P0046, Q3-SH-K1539, Q3-SH-K1540, Q3-SH-011, Q3-SH-089, Q3-SH-090, Q3-SH-091 (8). None in the Salla or Zid folders.
- `copied-view.tsv`, read once after the accounts; `copied-gaps.tsv` listed by concern; `copied-pilot-gaps.tsv` and `copied-pilot-absences.tsv`.
- Topic search (no map is held): `python3 -I method/corpus_search.py woocommerce "requirement" "requirements" "eligibility" "verification" "verify your" "Know your customer" "Launch your store" "before you can" --max 10`. Read from it: woocommerce.com/document/woopayments/our-policies/know-your-customer/; woocommerce.com/document/woopayments/our-policies/ (capture 20261012T104936Z-s01-sources item 091; `held_index.py` names the earlier capture item 066 for this URL). Also read, as a document the topics led to, in the release: `src/Admin/Features/OnboardingTasks/Tasks/LaunchYourStore.php`, `src/Admin/Features/OnboardingTasks/TaskLists.php` (lines 100-140), `src/Admin/Features/LaunchYourStore.php` (grep only), `includes/admin/settings/class-wc-settings-site-visibility.php` (grep only), `src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsService.php` (lines 28-80 and a grep).
- Sentence [1] search, for the account points not yet matched: given in `not-found.tsv` rows N01-N06. Read from it: woocommerce.com/document/woopayments/startup-guide/, .../our-policies/prohibited-and-restricted-products/, .../settings-guide/ (lines 108-125).
- Sentence [4] search: given in rows N07-N09. Read from it: woocommerce.com/document/woopayments/payment-methods/local-payment-methods/ (by grep, then lines 25-30, 66-72 and 99-112 of its text).
- All pages read were held captures, read on 2026-10-19. No live page was read.

## Account points not checked

These account points were not among the terms of the sentence searches, so no row was recorded for them: Shopify [1] "Choosing the store currency" (Q3-SH-002), "Europe and the United Kingdom" (Q3-SH-065), "Providers and entities" (Q3-SH-K1264), "Displaying the store in Shop" (Q3-SH-075); Shopify [4] "Admin request" (rests on Q3-SH-N03), "The plan and the store's state" (Q3-SH-036), "Shop" (Q3-SH-030), "Hemp" (Q3-SH-056); Salla [1] the help centre on foreigners and the e-commerce licence (Q3-SA-032), the commercial registration within 30 days (Q3-SA-030); Salla [2] Basic plan product types (Q3-SA-029), Tabby and Tamara (Q3-SA-K1617), Mahally and the wholesale market (Q3-SA-061), the freelance document covering products (Q3-SA-022); Salla [4] payouts delayed during a complaint (Q3-SA-K0073), Mahally and Salla Capital messages (Q3-SA-062); Zid [1] confirmation codes (Q3-ZD-029), national address (Q3-ZD-039), promotional licences (Q3-ZD-052); Zid [2] one published product (Q3-ZD-P0116), Nafath (Q3-ZD-P0117), Apple Pay Merchant Terms (Q3-ZD-074), cash on delivery terms (Q3-ZD-049), wallet withdrawals (Q3-ZD-P0063), moving the store to another country (Q3-ZD-P0152), digital products (Q3-ZD-P0159), Mazeed, Jahez, Amazon and Trendyol (Q3-ZD-061), sender name, WhatsApp and the mobile app (Q3-ZD-K0509); Zid [4] reporting changes within a week (Q3-ZD-078), Mazeed and Trendyol review times (Q3-ZD-063), bank-transfer subscriptions (Q3-ZD-048), store regulations (Q3-ZD-051), account termination (Q3-ZD-040).

Account points resting only on not-found rows or copied gaps were not sorted against: Zid [2] "No check by Zid before a store is opened" (Q3-ZD-N03), Zid [4] "Zid's stated reason" (Q3-ZD-G0002), Salla [4] "Still open".

## What couldn't be read

- The Site visibility settings' text is in built JavaScript; the PHP class holds only its label.
- The full prohibited and restricted businesses list, Alipay's Terms of Service and the Weixin Pay Proper Use Rules, to which the pages link, were not opened.

## Copies

- None found wrong or out of date.

## Problems

- One command, a search of the release for the launch-your-store code, began with a `cd` into `/home/user/woocommerce-release/11.2.1/woocommerce` before running `grep` with absolute paths. Nothing was run from that folder other than `grep`, and nothing was written there. Later commands didn't change directory.
- Many account points (above) were left unchecked: one search per sentence with all their terms would have been long; the searches covered points on money flows, legal structure and the data model first.
- The account's length counts its point names; it sits at about 820 words without ids.
