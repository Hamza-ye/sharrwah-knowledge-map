# Notes on SH-90 (shopify, effort high)

75 entries of `plan-page-admin`, read at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure the pass reads). Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-90`).
- **1 to 61:** the rest of the admin's plan page at `settings/subscribe/select-plan` as the trial stores fake-demo-sharrwah and ibx5bt-xy rendered it on 30 September (runs `20260930T002940Z-sweep-trial` and `20260930T045741Z-sweep-trial2`, step 100): the comparison table from the row Create email campaigns (fake-demo-sharrwah's `items.jsonl`, line 193) to its last row, Plus Certified apps (line 393), then the page's five footnotes (lines 401 to 405).
- **62 to 75:** the first fourteen items of ibx5bt-xy's admin frame (its `items.jsonl`, lines 1 to 14): the skip link, the top bar's logo, search, alerts count and store name, the logo's link, and the main navigation from Home to Content. SH-91 holds the rest of the frame.

**Placed:** 75 entries in 81 lines.
- **By entry:** 59 on a capability, 16 out, none new. 4 entries take more than one line: 27, 28 and 29 (Build headless storefronts and its cells, on CM-SFR-011 and CM-CHN-007) and 58 (the disclaimer, four providers' lines).
- **By line:** 65 on capabilities (52 `core`, 8 `shows`, 5 `outside`) and 16 out. No line is `own-service` or `extension-point`.
- **Other columns:** 22 lines carry qualities and 5 fillers. No line takes a store (R89.1).

**Sources read:**
- the brief and what it names: the evidence map; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`; `REGISTER.tsv`'s rows for `plan-page-admin` and `plan-comparison-admin`; `index/ledger/admin-route.tsv`'s rows for `select-plan`; `selection.tsv`'s row; `show --meta`; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; the rulings' last section;
- SH-89's notes, with R89.1 to R89.9 and its coordinator's check, and SH-88's R88.1 to R88.6 with its check;
- the twins' lines, by number: SH-88's 62 to 97, SH-89's 2 to 23 and 118 to 145, SH-94's 33 to 38, SH-72's 25, SH-71's footnote line on SH-E-389f0e29, and SH-2's lines 61, 62 and 74 to 82 (`admin-main-nav`);
- `cells` for every capability placed on (35), the names of the leads' other capabilities, and `land_points.py cell CM-PAY-027 shopify` for its Melio rows;
- to clarify only: both pages' items, ibx5bt-xy's `source.html` around its top bar, and the trial stores' and the US store's PlanFeatureSetQuery answers (below).

The scratch scripts are in `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/SH-90/`: SH-89's `places.py` and `twins.py`, set to this batch; `rows.py`, which prints each table row with its cells by plan on both stores; `cmp.py`, which compares each row with the trial stores' and the US store's answers; `findtext.py` and `nav.py`, which find an entry's words in other structures with their lines; and `c1.py` to `c3.py`, which write the lines.

## Rules kept

R88.1 to R88.6 and R89.1 to R89.9 are kept, as the coordinator's checks after SH-88 and SH-89 settled them. Nothing here departs from them but one extension of R89.5 (below).
- **Scope (R89.1):** the plans the row's cells fill, by the page's names. Both stores state every entry of 1 to 61: `rows.py` finds the same rows and cells, in the same order, on both pages.
- **Twins (R89.2):** each row takes the line SH-88 or SH-89 gave the feature of the same summary.
  - The trial stores' two answers are identical, and every row of this range has a feature in them with the page's words, marks included (`cmp.py`).
  - The US store's answer (`20261027T175456Z-journey-signup-located-us`, `7bd0c74d….json`) states every one of these features in the same words, with the same values. So no reading names a difference.
  - The US answer's features the page doesn't render (Shop Campaigns, Optimize ads with Shopify Audiences, the sections Shipping and Tax) are SH-88's and SH-89's.
- **Cells (R89.5):** a value is a quality where its twin has it as one: Limited and Full, Limited and Full data access, Standard, Up to 2x and Up to 10x on select APIs, 1 and 25, the earnings rates, Up to 3% cashback and Up to 9. No cell of this range is a level that the twins keep in their readings.
- **Marks (R89.6):** SH-89's 'enabled', 'disabled' and '—' stand for this range's cells too. Each Just for Plus row names the dash on Basic, Grow and Advanced in its reading.
- **Sections (R89.7):**
  - Marketplaces: CM-CHN-003 `shows`.
  - Customization: `out`.
  - Sell globally: CM-MKS-001 `shows`.
  - Finance: `out`.
  - Just for Plus: CM-PLN-001 `shows`, scope Plus.
- **The frame (R89.9):** all of 62 to 75 are `out`.
  - **The navigation items** (69 to 75) each name the `admin-main-nav` entry of the same words for ibx5bt-xy and the lines SH-2 gave it.
  - **The logo link** (68) is `admin-main-nav`'s SH-E-effb6123, which SH-2's line 74 places `out`.
  - **The alerts count, '1'** (66), is the number inside the top bar's button 'Alerts Feed - 1 unseen alerts' (source.html). That count is the store's own data. The button itself is `admin-main-nav`'s SH-E-1dc638ea (SH-2's line 62).
  - **The store's name** (67) is My Store, as SH-80's line 31 places the same words.
  - **The skip link, the logo's images ('Shopify Shopify', two `img` alts), the search and its key hint** (62 to 65) are UI strings.

## What this batch adds

- **R90.1: a cell takes the row's second line where the twin's second line carries the value** (28 and 29, the counts 1 and 25 of Build headless storefronts).
  - R89.5 puts a row's second line on its heading only. SH-89's second lines (the billing period, B2B, an AI feature, sourcing) name what the row is, and carry no value.
  - CM-CHN-007's line is different. SH-88's line 90 carries the count, and the count is CM-CHN-007's thing, several storefronts in one store: its cell's only evidence is this plan row.
  - So the cells take a CM-CHN-007 line beside their CM-SFR-011 line, each with the count as quality. The heading takes both lines with no quality.
- **R90.2: the footnotes take their twins' lines on the public plans page** (SH-94's lines 33 to 38), with the page's own words:
  - **57, Bill Pay** ('Shopify Bill Pay is powered by Melio'): CM-PAY-027 `outside`, Melio its filler. The cell's SH-S-7201 already cites the same footnote on this page. No other entry holds these words.
  - **58, the disclaimer:** four lines, Balance's account (Stripe Payments Company and Fifth Third Bank N.A.), Balance's cards, Capital and Credit's cards. Capital's line takes 'United States', the country it names WebBank for (the ruling after SH-69). The public page writes U.S. there; the rest is the same.
  - **59, the Balance earnings rate:** CM-PAY-023 `shows`, with the footnote's own rates, 3.32% on Plus and 2.29% on the other plans, as quality. They differ from the row's cells (2.52% and 3.54%, entries 40 and 41), as SH-89's notes found. The twin's page states 3.54% and 2.52%, accurate as of September 28, 2026; this one January 2, 2026. This page also adds 'compounded and'.
  - **60, cashback:** CM-PAY-025 `shows`, the card's terms as qualities. The twin's words are the same but for its US$.
  - **61, Capital:** CM-PAY-026 `shows`. It is word for word the pricing data's footnote on 13 country sites (SH-E-761e7fbe, SH-72's line 25).
  - **The marks:** joined to their footnotes by their words, as SH-89 did: ¹ to 59, ² to 61 and ³ to 60. The page's list numbers them 1, 3 and 2.
- **R90.3: '*Requires Shopify Payments'** (37) is the section Sell globally's footnote to its two rows marked * (32 and 34). It is CM-PAY-002 `shows`, as the public table's footnote of the same words (SH-E-389f0e29, SH-71).
  - The trial stores' answers set `requiresShopifyPayments: true` on those two features alone.
  - The two rows' readings quote the footnote, and the condition stays out of their scope (R88.5).

## New things

None.

## Entries I couldn't tell, and what would settle each

- **28 and 29, the second line on CM-CHN-007 (R90.1).**
  - The other reading keeps R89.5 to the letter: the heading alone takes CM-CHN-007, and the count reaches that cell only through SH-88's line 90 and SH-71's line 77.
  - Either way, no cell's support changes. The coordinator's choice settles it.
- **14, '1% up to $99/mo', on CM-CHN-003 alone, as its twin.**
  - The fee is on synced marketplace orders over 50. The answers' description reads 'For orders above 50, pay a transaction fee.' and names no one who charges it.
  - The other reading adds CM-PLN-003, the platform's fee on sales by plan. But the fee is the same on every plan, and no lead or twin names CM-PLN-003.
  - A statement of who takes the fee would settle it.
- **21 and 22, Limited and Full data access, on CM-APP-009 alone.**
  - Which data Basic's custom apps can't reach isn't stated. The answers' description of `customization_custom_apps` is empty, and the row's tooltip isn't in the page's source (R89.4).
  - If it is buyers' personal data, CM-API-004 (protected customer data) would take a line.
  - The tooltip's words would settle it.
- **59 against 40 and 41, the earnings rates:** the footnote and the cells state different rates on the same page. The footnote's link is held (`help.shopify.com/en/manual/finance/shopify-balance/rewards/earning-rewards`: `20261016T213535Z-help-en-ar-html-md` and `20260930T003703Z-help-en-md`). Reading it could settle which rate applies when; I didn't read it (the brief: no further than the entry's sources).
- **64, 'Search', `out`.** R89.9 and the coordinator's message place the frame's search `out`. The ruling after SH-37 keeps the admin's search as a new thing, `new:Admin search`, which the changelog's and Editions' posts take (25 lines). The button states nothing more than its label, so it gives that new thing no evidence. The reading names `new:Admin search`, in case the coordinator would rather place the button there, `shows`.
- **66, the alerts count, `out`.** SH-2's line 62 places `admin-main-nav`'s button, 'Alerts Feed - 1 unseen alerts', on CM-NTF-002 as a container. This entry is the count alone, so it is the store's own data under R89.9.

## A structure whose items and sources disagree

- **The items join a top bar element's parts:**
  - 'Shopify Shopify' is two images, the glyph and the wordmark, each with the alt text Shopify;
  - 'CTRL K' is two `kbd` elements;
  - '1' is the inside of a button whose label, 'Alerts Feed - 1 unseen alerts', only the source holds (its `aria-label`).

  The source governs. Each reading names the element.
- **`entries.tsv` names a repeated text's first line only.** Free and '1% up to $99/mo' (4 cells each), Limited, Full data access, 1, '2.52% earnings rate' and Up to 3% cashback (3 or 4), and Standard (2) each stand for several cells. `places.py` found each place on both stores, and the lines take every plan each one stands for.
- **The footnotes' list numbers cross their marks** (R90.2), as SH-89 found.

## What a source states that no entry holds (for the second stage)

- **The rows' descriptions,** which the page shows only as tooltips. They are in both trial stores' answers, in the same words as the US store's, which SH-88 placed. They give no new lead. Examples are Translate your storefront's two automated translations, High volume checkout's 40K checkouts per minute, and Build headless storefronts' Hydrogen and Oxygen.
- **The footnotes' links are all held:**
  - the Balance Reward Terms, at help.shopify.com, in the runs above;
  - Shopify Credit's Issuing Bank Terms and Program Terms, in `20260930T050139Z-shopify-com-pages` and in this repository's `evidence/product-class/runs/20261011T075149Z-q1-shopify-sources-2/`.

  The first is a lead for CM-PAY-023's rates (above).

## Problems with the brief or the scripts

- **SH-89's notes had no coordinator's check when this batch began.** The check was added during the run, and I read it: it keeps R89.1 to R89.9 and the open choices.
- **`method/held_plan_frame.py` places SH-91's frame, not this batch's 14 frame entries.** I placed those by hand under R89.9, without reading the script's code, as the brief asks. Their readings may word the same rule differently from SH-91's lines.
- **`earlier` prints no twin across structures,** as SH-89 found. The rows were matched with SH-88's and SH-89's lines by summary, and the footnotes by their words (`findtext.py`).
- **No B-extent conflict** was found, beyond the two the brief states itself: qualities wider than B-extent's list, and the rulings.

## The checker's lines, read again

- **No `CHANGES`:** every line is on a cell that already holds its support.
- **No `NEW`.**
- **`NOTE` on a product named with the platform's brand:** lines 21 (Build custom apps using Shopify APIs), 37 (Shopify Markets), 43 (Shopify Balance), 46 (Shopify Capital), 47 (Shopify Credit), 49 (Shopify Bill Pay) and 52 (Shopify Combined Listings).
  - Each is a plan line, `core` as its twin and the cell's plan row hold it (SH-S-7054, SH-S-7059, SH-S-7062 to SH-S-7065, SH-S-7071), not by the name (R88.2).
  - For Capital, Credit and Combined Listings, whose own features are `own-service` by held maker statements, the plan line stays `core` (the rulings after SH-55 and SH-41; the corrections with the changelog digest).
  - Shopify Balance and Shopify Markets are the admin's own services (the correction on Shopify Balance). The APIs are the platform's own.
- **`NOTE` on footnote marks:** lines 36 and 38 (Show prices in local currencies*, Accept local payment methods*). Each reading quotes the page's footnote '*Requires Shopify Payments' (entry 37) and the answers' `requiresShopifyPayments: true` (R88.5).
  - The marks ¹, ² and ³ (39, 42 and 43) aren't flagged by the checker. Their readings name their footnotes all the same (R90.2).

## The coordinator's check

Measured: 13.5 million tokens over 71 requests, about 180,000 an entry. The checker prints no problem and no `CHANGES` line.
- **Kept:** R88's and R89's rules, and R90.1 to R90.3 (the headless storefronts' cells on CM-CHN-007 too, as their twin; the footnotes on their twins' lines, Bill Pay `outside` with Melio as the cell has it; the Payments footnote `shows`), and the open entries as placed. `plan-page-admin` is placed whole, with SH-91.
- **Entry 64, the top bar's search, corrected:** from `out` to `new:Admin search` `core`. The ruling after SH-37 keeps the admin's search a new thing while the rest of its frame is `out`, and SH-80 placed the mobile app's search tab the same way, its place of its own.
