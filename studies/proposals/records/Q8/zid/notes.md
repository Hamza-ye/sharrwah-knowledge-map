# Notes: Q8 on Zid (check against shopify, woocommerce)

## Selection
- 37 concerns copied, 59 set aside, S-01 set aside. No concern added.

## What was read
- Accounts: `studies/proposals/records/Q8/shopify/account.md` and `studies/proposals/records/Q8/woocommerce/account.md`. Both pass `check_proposals.py records` with no issues. No cited id was looked up.
- First corpus search (question topics, ar and en): `python3 -I method/corpus_search.py zid "الباقات" "باقة" "الإضافات" "plans" "plan" "Pricing" "تجريبي" "beta" "add-ons" "add-on" --max 10`. Read from what it listed:
  - https://zid.sa/llms.txt
  - https://help.zid.sa/subscription/
  - https://docs.zid.sa/create-first-app.md
  - https://zid.sa/en/pricing/: the rendered text is the error page, so its raw.html was searched with bounded `grep` only.
- Search A (unmatched account points; command in `not-found.tsv`). Read https://help-partner.zid.sa/en/articles/10325692-critical-update-new-shipping-pricing-structure.
- Search B (points left out of A; command in `not-found.tsv`). Read https://docs.zid.sa/authorization.md, around its version note.
- Unmatched points and their search terms: scratch file `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/records/Q8-zid/unmatched-points.md`.

## Live pages read (2026-10-19), through `method/capture/page_text.mjs`
- https://changelog.partner.zid.sa/: served in English. Most of the page is posts by partners. Only the board's own text and its Status filter were recorded.
- https://changelog.zid.sa/ar: served in Arabic.
- https://zid.sa/en/enterprise/: served in English. Its rendered text is the error page ("Oops! Something went wrong."). The raw HTML holds marketing headings and no plan terms. Nothing was recorded from it.

## Not checked
These account points were neither matched nor carried by a search term in either of the two searches allowed per sentence. So they have no row and no label:
- WooCommerce [2]: Q8-WC-003, Q8-WC-005 (packages);
- WooCommerce [3]: Q8-WC-007 (packages merged into core), Q8-WC-068 (theme submissions), Q8-WC-K0869 (connecting a store), Q8-WC-037 (suggestions by base location), Q8-WC-044 (Country filter) and Q8-WC-036 (Woo Express plan rules);
- Shopify [3]: Q8-SH-K2066 (who may create a sales channel).

## Problems with the method
- Not read: the plan headings "All features of Starter package, plus:" and "All features of Rise package, plus:" on zid.sa/en/pricing/. They sit in the page's JSON, and which plan card each belongs to couldn't be told from the raw page. Neither was recorded as a statement. The account cites the copy that carries the first of them (Q8-ZD-K0006).
- To check the column order of `not-found.tsv`, I printed the header line of `studies/proposals/records/Q8/shopify/not-found.tsv`. The run's constraints allow only my own folder's files for that. Only the header row was read.
- Several Shopify and WooCommerce points share one not-found row where they ask for the same thing (Q8-ZD-N04, N05, N07, N10).
