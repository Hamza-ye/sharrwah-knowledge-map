# Notes: Q1 draft proposal (R4)

## What I read

- The brief, `studies/proposals/briefs/R4-drafting.md`, whole.
- Q1's section of `studies/proposals/questions-for-agents.md`: sentences [1] to [5].
- Q1's rows in `studies/proposals/areas/depth.tsv`: Shopify, Salla and BigCommerce read in depth; Zid and WooCommerce checks.
- The five accounts, `studies/proposals/records/Q1/<platform>/account.md`: Shopify, Salla and BigCommerce first, in `depth.tsv`'s order, then Zid and WooCommerce.
- From each platform's `notes.md`, only these lists, found by listing each file's headings:
  - copies found wrong or out of date: each "Copies" section. None of the five reports a copy wrong or out of date. Shopify's notes say Q1-SH-071 and Q1-SH-K1956 state Managed Markets eligibility in different words, and BigCommerce's that Q1-BC-071 and Q1-BC-K0139 give different figures; the draft cites none of the four.
  - account points not checked: Zid's "Account points not checked", and WooCommerce's "The accounts" and "Not-found rows", which hold its list of points not sorted against. Shopify, Salla and BigCommerce, read in depth, have no such list.
- Records by id, with `python3 -I method/record_ids.py`: every id the five accounts cite (725), saved in my scratch directory and read through a compact view of each record's statement, identifier, scope, and each citation's date and source; then the full records, quotes included, of the ids the draft quotes or rests on. The draft cites 131 statements, copies and citations, and 5 not-found rows and copied gaps (`check_proposals.py drafts Q1 --cited` lists them).
- `python3 -I method/source_kinds.py` on the 249 sources those records cite, for the kinds the draft names where a comparison mixes them.
- The areas list: in `studies/proposals/areas/areas.md`, the 17 areas whose questions include Q1: A-01, A-03, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-18, A-19, A-20, A-21, A-22, A-30, A-31 and A-33. Section 4 names some of them on its parts; nothing else in the draft rests on them.
- `studies/proposals/yemen-digest.md`, whole, once, after writing sections 1 to 5 and 7. Then Stage 1's rows by id: YA-01, YA-03, YA-07, YA-15, YA-21, YA-27, YA-48, YA-62, YA-102, YA-103, YA-114, YA-115, YK-12, YK-124, YK-128, YK-131, YK-207, YK-209, YK-290, YK-369, YK-452 and YK-515. The draft cites 13 of them: YA-01, YA-07, YA-15, YA-21, YA-27, YA-62, YA-102, YA-115, YK-12, YK-124, YK-290, YK-369 and YK-452.

## What the records don't show

- Where the rate behind Salla's automatic pricing by exchange rate comes from, and who sets it (Q1-SA-N02). Salla's help or dashboard text naming the rate's source would show it.
- What adding a country involves on Shopify's and BigCommerce's own side, for their payment services or the platform (Q1-SH-N02, Q1-BC-N04). A page of theirs on launching a country would show it.
- Which region holds a BigCommerce store's data, and whether a merchant can choose it (Q1-BC-G0154). BigCommerce's Trust Center page, which the run couldn't read, would show it.
- Which settings vary below a country, beyond what the records give: Shopify's sub-region markets customize only shipping (Q1-SH-022), and Salla's markets reach a region or city (Q1-SA-K1976) while tax by market needs one country (Q1-SA-023). Pages on sub-country markets or zones for the other settings would show it.
- Who keeps Salla's and BigCommerce's lists of countries and their subdivisions (copied gaps Q1-SA-G0157 and Q1-BC-G0140, not cited in the draft); only WooCommerce's records give a source, the Unicode CLDR recommendation (Q1-WC-K1382).
- Which governorates or districts each of Yemen's areas of control covers: no axis or constant in the digest lists them (section 6). A dated source listing each area's governorates and districts would show it.
- Whether a seller may show prices, without charging them, in a currency other than the rial at either area: the digest's YA-21 gives the currency sales must be paid in, and YA-149 what some online sellers price in, but no axis or constant gives a rule on showing prices. A dated source giving such a rule, with its place, would show it.

## Where I cited past the guide

- Statements, copies and citations: 131 distinct ids against about 40. Section 1 compares the five platforms on Q1's five sentences, mostly with one id per platform per point, and cites 115; 82 of these carry the elements of sections 2 to 7, which add 16 more (the seller entity's verification and change, the merchant of record, markets within markets, and the licence, provider and registration decisions). By platform: Shopify 45, Salla 29, Zid 20, WooCommerce 19, BigCommerce 18.
- Yemen facts: 14, each an axis or constant at one place, against about 8. Five give the rial's split, which bears on the place register, the market currency and the rate source (YK-12, YA-01 at Sana'a and at Aden, YA-07, YA-15, YK-452 in section 5); two give a provider's reach by area (YK-124, YK-369); the others give Stripe's unavailability and one Yemeni provider's credentials (YA-62, YA-115), the rial-only rule (YA-21), the rule on who may provide e-payment services (YA-102), records kept in Yemen (YK-290), and, for section 7, the US designations of Ansarallah (YA-27).
- Not-found rows and copied gaps (5) and "Yemen's evidence doesn't show" (1) are within the guide.

## Problems with the brief and the tools

- `check_proposals.py` reads a Yemen fact's bracket only to the first closing parenthesis, so a place that holds parentheses, as the digest's "E-Pay (Kuraimi Islamic Microfinance Bank)'s service" and "Cash Pay (Cash e-wallet)'s service", lost its date. I wrote those places as "Kuraimi Islamic Microfinance Bank's E-Pay service" and "the Cash e-wallet's Cash Pay service".
- `record_ids.py` prints a Stage 1 constant without its date; I took each constant's date from the digest.
- I read the areas list after writing sections 1 to 5, not before as the brief's order puts it, and then named areas only on section 4's parts.
- The checks' accounts and notes name none of Q1-SH-092 to Q1-SH-107 or Q1-SA-105 to Q1-SA-113, which the in-depth accounts cite, so whether the checks covered the points resting on them isn't shown. I wrote "not checked on Zid" only where a check's list names a point: Q1-BC-018, and Salla's point resting on Q1-SA-N02. WooCommerce's list names "Salla [2], the last point", which in the current account rests on Q1-SA-105, Q1-SA-106 and Q1-SA-N02; its notes don't say which version they read, so the draft doesn't mark that point for WooCommerce.
- WooCommerce's notes give its list of points not sorted against under "The accounts", not under a heading of its own, so I read that section and "Not-found rows" to find it.
