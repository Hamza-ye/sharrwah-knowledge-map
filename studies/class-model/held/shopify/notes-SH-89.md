# Notes on SH-89 (shopify, effort high)

130 entries of two structures, read at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure the pass reads). Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-89`).
- **1 to 29, `plan-feature-set`:** the last 29 of its 109 entries, from the selection's latest answer, `raw/runs/20261027T175456Z-journey-signup-located-us/answers/admin.shopify.com/PlanFeatureSetQuery/7bd0c74d….json`, the US store tuu1u4-v0's (SH-88's R88.4):
  - 1 to 21: the sections Finance (1 to 5), Tax (6 to 10) and Just for Plus (11 to 21) of `planFeatureSet`;
  - 22 to 29: the add-on set In-person selling (`planAddOnFeatureSet`), its values by `pos_lite` and `pos_pro`, not by plan.
- **30 to 130, `plan-page-admin`:** the first 101 of its 251 entries: the admin's plan selection page at `settings/subscribe/select-plan`, as the trial stores fake-demo-sharrwah and ibx5bt-xy rendered it on 30 September (runs `20260930T002940Z-sweep-trial` and `20260930T045741Z-sweep-trial2`, step 100; `structures/shopify/plan-page-admin/<store>/source.html`):
  - 30 to 69: the page's heading and its four plan cards (fake-demo-sharrwah's `items.jsonl`, lines 1 to 42);
  - 70 to 130: the comparison table, from its header Compare plans to the row Create customer segments under Marketing (lines 43 to 188). SH-90 begins with the row Create email campaigns (line 193).
  - Both stores state every entry of this range: the two pages' items are the same but for ibx5bt-xy's admin frame (its lines 1 to 87 and 493) and its Plus card's title, `Plus` with an aria-hidden `+` (its line 119). Those make 89 entries labelled ibx5bt-xy alone, all in SH-90 and SH-91.

**Placed:** 130 entries in 144 lines.
- **By entry:** 118 on a capability, 7 on a new thing (SH-68's) and 5 out. 13 entries take more than one line.
- **By line:** 132 on capabilities, 7 new and 5 out.
- **Supports:** 121 `core` and 11 `shows` on capabilities, 7 `core` on the new thing. No line is `own-service`, `extension-point` or `outside`.
- **Other columns:** 52 lines carry qualities and none a filler. 6 lines, of 6 entries, take the store tuu1u4-v0 (R88.4).

**Sources read:**
- the brief and what it names: the evidence map; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`; `REGISTER.tsv`'s rows 128 and 130; `index/ledger-summary.tsv` and `index/ledger/admin-route.tsv`'s rows for `select-plan`; `selection.tsv`'s rows; `show --meta`; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; the rulings' last section;
- SH-88's notes, whole, with its coordinator's check, and its lines; SH-92's notes, rules P1 to P12 and its check;
- the twins' lines, by number: SH-71's 85 to 99, SH-72's 165 to 188, SH-74's 19 to 24, SH-75's 15 and 108 to 118, SH-92's 2 to 50, SH-70's 130, SH-14's 19 and SH-1's 189;
- `cells` for every capability placed on, and for CM-PLN-004 and CM-PTN-008; `caps --terms` for the add-on's words (POS staff, retail reports, retail inventory, omnichannel, exchange, purchase location, customer profile, in-person selling, POS Lite), for fees and trials (variable fee, platform fee, transaction fee, trial, paid trial) and for the new thing (below); `class_slice.py key SH-S-7017`;
- to clarify only: the two pages' `source.html` (the cards' labels and `data-plan-id`, the table's cells, its buttons and the footnotes' list), and both trial stores' own PlanFeatureSetQuery answers at steps 99 to 101 (below).

The scratch scripts are in `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/SH-89/`: SH-88's `twins.py`, `status.py` (extended to `planAddOnFeatureSet`) and `verify.py`; `allstores.py`, which compares each store's every answer; `verify2.py`, which checks each feature's scope against its values; and `places.py`, which finds every place of an entry's text in both stores' items, with its card, row and column.

## `plan-feature-set` (1 to 29): R88 kept

R88.1 to R88.6, as the coordinator's check after SH-88 settled them, are kept:
- the plans in scope by their display names, Shopify's identifiers in the reading;
- a plan that lacks a feature left out of the scope and named in the reading, with no extra `shows` line;
- the store tuu1u4-v0 only where the stores' answers differ.

What this part adds:
- **Sections (R88.1).**
  - Finance is `out`, as its twin (SH-71's line 85).
  - Tax is CM-TAX-001 `shows`, as its twin (SH-74's line 19), with the store, since no other store's answer holds the section.
  - Just for Plus is CM-PLN-001 `shows`, scope Plus, as its twin (SH-71's line 90).
  - In-person selling, the add-on set's section, is CM-POS-001 `shows`, as R88.1 places the section In-person sales.
- **The store (R88.4),** measured with `status.py` and `allstores.py`:
  - Finance and its 4 features: the same in all 12 other stores' latest answers;
  - Tax and its 4 features, and plus_shopify_audiences (14): in this answer only, so they take tuu1u4-v0;
  - Just for Plus and its other 9 features: the same in 9 stores' latest answers, and in an earlier answer of each of the other 3;
  - In-person selling and its 7 features: the same in 8 stores' latest answers, and in an earlier answer of each of the other 4.
- **The VAT feature (9)** takes 'EU and UK sales' in its scope with ` and `, as the coordinator's check after SH-74 wrote its twin's.
- **The marks ¹, ² and ³** (Balance, Capital, Credit).
  - The answer holds no footnotes. The admin plan page renders the same summaries with the same marks, and its footnotes (plan-page-admin, `items.jsonl` lines 403 to 405: entries SH-E-e612df5c, SH-E-f770e328 and SH-E-9efbb5e0, of SH-90 or SH-91). The readings quote them, as SH-71 quoted the public page's. This is a reading: they are another store's page, of 30 September.
  - The page's footnotes are a numbered list (`<ol>`, source.html): 1 the Balance earnings rate, 2 cashback, 3 Capital's financing. Capital's mark is ² and Credit's ³, so the marks and the list's numbers cross. The readings join each mark to its footnote by its words, as SH-71's lines 87 and 88 did.
  - The Balance footnote states 'Stores on Shopify Plus are rewarded with 3.32%, and all other plans receive 2.29%.' The same page's row states 2.52% and 3.54% (lines 309 to 312), as this answer does. The line takes the answer's values, and the reading names the difference.
- **The add-on set (22 to 29).**
  - **Scope.** pos_lite is the plans' own in-person selling: the set's Pricing reads 'Included with all plans' (23). Its features take the five plans the answer lists, by display name: a reading of "all plans". pos_pro is POS Pro, the paid add-on, and a feature that comes with it takes `POS Pro` as scope (the ruling after SH-70). A feature with values for both takes `Starter;Basic;Grow;Advanced;Plus;POS Pro`, its levels in quality or reading (R88.3). A feature false for pos_lite takes `POS Pro` alone, pos_lite named in reading.
  - **Twins:** the POS page's list posLiteVsProPlans (PosLite, Casual in-person selling, 'Included in every plan'; PosPro, POS Pro) and its features (SH-72's lines 165 to 188). Each feature takes its twins' two lines, on its own capability and on CM-POS-001.
  - **Pricing (23)** names two things: the plans' included in-person selling, and POS Pro with its price. It takes two lines on CM-POS-001 (the ruling after SH-34). The second takes no scope, as the add-on's own offer (the ruling after SH-70).
  - **Descriptions:** Retail inventory management lists 'Create purchase orders, perform stock counts, optimize stock levels, and more.', Retail reports 'actionable dashboards, cash tracking, and daily sales reports', and Omnichannel selling 'features like' local delivery and pickup. Each is a list of uses, so its things take no line (R88.2; the ruling after SA-41). Customer profiles' 'targeted marketing campaigns' is a use too.

## `plan-page-admin` (30 to 130): the rules this batch sets (R89), for the coordinator to check and SH-90 and SH-91 to keep

- **R89.1: Scope.** The page's plans by its own names: Basic, Grow, Advanced and Plus. The cards pair them with Shopify's identifiers themselves (`data-plan-id` basic, professional, unlimited and shopify_plus, source.html), as the coordinator's alignment does.
  - **No store:** both held stores state every entry of this batch. This is R88.6, as it placed this table's header (SH-88's line 6). Where the US store's answer states another value or other words, the reading says so.
  - **A card's part** takes its card's plan.
  - **A card's feature with no value** takes its plan and the plans above it, each card holding 'Everything in' the one before (SH-92's P1 and P4). One with a value takes its own card's plan only.
  - **A table row** takes the plans its cells fill, with a value or the mark enabled. **A cell** takes its column's plan or plans.
  - **A heading, a section or a mark** takes no plan.
- **R89.2: Twins.**
  - **The cards** are the admin's renderings of the public plans page's cards (plan-page-public, SH-92's lines 6 to 50), with the pricing data's plan features (SH-70, SH-72, SH-75).
  - **The table** is the admin's rendering of the plan feature set. Its rows and values are those of both trial stores' own PlanFeatureSetQuery answers at the page's steps 99 to 101 (`raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/PlanFeatureSetQuery/09dfdcee8ce3db7eab1cc5974c0a61218275bf2e057ccd79d4d55c859683b6e4.json`; `raw/runs/20260930T045741Z-sweep-trial2/answers/admin.shopify.com/PlanFeatureSetQuery/2d267dabb3880691011f9b17cec0a199fbf5330fa189fc947ee7ff51ee061598.json`). That they are the page's data is a reading, from their rows and values.
  - Each row takes the lines SH-88 gave the feature of the same summary in the US store's answer, with the concern map's SH-S-70xx where the cell cites the public table's row of 30 September. `earlier` finds the rows' labels (SH-88's lines and SH-71's), not the cells'.
  - **Each line quotes the page's own words.** Where the US store's answer (SH-88) states others, the reading says so: the prices, the credits' maximums, the in-person row and POS Pro's Plus cell.
- **R89.3: The cards' parts** (SH-92's P3 and P4):
  - **name and description:** CM-PLN-001 `core`, the card's plan. A name is one entry for the card's title and the table's column;
  - **price:** CM-PLN-001 `core`. Its quality is its label's words, '$27 USD per month, try for $1', as monthly price and trial price. The parts the items join, '$27 $1 /mo', are hidden from the accessibility tree. The admin's cards show no billing period, so no CM-PLN-002 line;
  - **the badge** '3-month trial', on Basic, Grow and Advanced: CM-PLN-001 `core`, the paid trial, as SH-1's line 189;
  - **features:** as their twins.
- **R89.4: Buttons.**
  - **Try Basic, Try Grow, Try Advanced and Select Plus** have no link. They start the plan's trial or select the plan, the admin's own plan selection: CM-PLN-001 `core`, the card's plan. They name a plan, so they aren't frame.
  - **The credits' buttons** open a dialog (`aria-haspopup`) that the page doesn't hold: the credits' line.
  - **The Plus cell's '+ variable fees'**, labelled 'View variable platform fee details': CM-PLN-001 `core`, a part of Plus's price.
  - **The rows' tooltip buttons** ('See details for …', 31 rows) aren't items. Their tooltips aren't in the page's source.
- **R89.5: Rows and cells.** The table renders each row as its heading and one cell per plan, each an item, and the build makes one entry of a repeated text.
  - **A row's heading** takes its twin's lines, with the plans its cells fill as scope. It takes a quality only from its own words (Sell unlimited products, 200+ real-time reports), never from its cells.
  - **A cell's value** takes its row's capability, its column's plan or plans as scope, and its value as quality. A level in words goes in reading instead (Full-featured, Live chat, Enhanced live chat, Priority support; R88.3).
  - **A row's second line** (CM-PLN-002, CM-B2B-003, CM-AIA-001, CM-CAT-010) goes on its heading only.
  - **A text in several cells** is one entry, and its line takes every plan it stands for (Full-featured, Up to 3 catalogs, 10, Live chat, $89/mo per location). `places.py` found each place, in both stores' items.
- **R89.6: Marks.** 'enabled' (152 cells a store), and 'disabled' with '—' (30 cells a store, a pair in each), are the check's and the dash's text. Only screen readers read them (`s-internal-text`, `accessibilityvisibility` exclusive).
  - They name no thing of their own, so they are `out`.
  - Each row's line reads them: it takes the plans enabled marks as its scope, and names in reading the plan a dash leaves out (R88.3).
  - The three entries stand for cells of SH-90's rows too, and their lines cover them.
- **R89.7: Sections.** The table's section titles render as rows with no cells, and are R88.1's:
  - in this batch: Pricing CM-PLN-001 `shows`; Core features `out`; In-person sales CM-POS-001 `shows`; AI features CM-AIA-001 `shows`; Hosting CM-OPS-003 `shows`; Marketing CM-MKT-005 `shows`;
  - for SH-90 and SH-91: Marketplaces CM-CHN-003 `shows`; Customization `out`; Sell globally CM-MKS-001 `shows`; Finance `out`; Just for Plus CM-PLN-001 `shows`, scope Plus (SH-88's lines 80, 84 and 91, and this batch's 1 and 11).
- **R89.8: Containers.** The page's heading, Plans starting at $1 (30), and the table's header, Compare plans (70), are CM-PLN-001 `core` with no scope (M-13): the admin's own page for choosing a plan, and its comparison (SH-88's line 6).
- **R89.9: The admin's frame,** decided once for the run. SH-90 and SH-91 hold all of it.
  - ibx5bt-xy's page rendered in a settings dialog, so its items hold the admin's frame (its `items.jsonl` lines 1 to 87 and 493; REGISTER: 'read from <body>, the admin's navigation included'). It is `out`, as the admin's own frame (the ruling after SH-37):
    - the skip link, the search and its key hint, the store's name and the dialog's Close are UI strings;
    - **the main navigation** (Home to Settings, lines 8 to 23) is the admin's navigation. `admin-main-nav` holds it for ibx5bt-xy (label ibx5bt-xy@home) and for this very page on fake-demo-sharrwah (fake-demo-sharrwah@settings-subscribe-select-plan), and its batches placed each item. Here it is a repeat, the extractor having read `<body>`: `out`, the reading naming the `admin-main-nav` entry of the same words;
    - **the keyboard shortcuts** (General shortcuts to Go to Settings: Metafields, lines 27 to 87) are the admin's frame. Each shortcut names another place as a key's target, not its own thing, as a route's `nextRoutes` does (the brief). The list itself names no capability: `out`.
  - **The exception:** the trial banner, 'Trial ends in 2 days', 'Subscribe for $1' and 'Select a plan' (lines 24 to 26, linking subscribe/checkout). It states the store's paid trial and its price, the plan page's own subject. It takes its twin's line in `admin-main-nav`: CM-PLN-001 `core`, quality 'paid trial: Subscribe for $1' (SH-3's line 9, on SH-E-71d2ecf6).
  - **'Plus+'** (ibx5bt-xy's line 119) is the Plus card's title, `Plus`, with an aria-hidden `+` (source.html). It takes this batch's 59's line.

## New things

No new thing is proposed. Seven entries join SH-68's new thing:
- **`new:Earn 1% back on all sales as subscription credits`:**
  - **Entries:** the cards' credits, 40, 48 and 58 ('Earn $4,500+ in credits', '$6,500+', '$8,000+'); the table's row Earn 1% back on all sales, 85; its cells, 86 to 88 (Up to $4,500, $6,500 and $8,000 USD).
  - **Place of its own:** a plan line, here the admin's own table row and plan cards.
  - **Its values:** Plus's cell is disabled, a dash. The US store's answer states Up to $5,000, $7,500 and $10,000 USD (SH-88's line 13).
  - **Proposed** as in SH-68's notes: domain A, area PLN, parent CM-PLN-004.
  - **Name:** English only, since the admin isn't held in Arabic.
  - **Leads:** CM-PTN-008, by the words earn and sale. It holds nothing on Shopify: it is Salla's referral commissions on its plans, not credits to the merchant (SH-68's notes).
  - **Searched again:** subscription credit; credits; earn back; back on all sales. The hits are CM-LOY-003 (the buyer's cashback), CM-MKT-020 (the ads wallet) and CM-PAY-018 (cryptocurrency, by credits): none is the thing.

## Entries I couldn't tell, and what would settle each

- **R89.6, the marks `out`.** The other reading gives enabled a line on each row's capability: about 30 lines in this batch, duplicating the rows' lines and changing no cell. The coordinator's reading of a mark as an entry settles it.
- **R89.5, a cell on a line of its own.** The other reading puts every cell's value on its row's heading line, as qualities by plan, and makes the cell entries `out`. Either way each value reaches its cell once. R89.5 follows SH-92's P3, which split a card the same way. The coordinator's choice settles it for SH-90 and SH-91.
- **R89.9, the navigation `out`.** The other reading gives each navigation item and shortcut that names a section that section's line, about 65 lines that repeat `admin-main-nav`'s. The coordinator's veto would settle it before SH-90 places them.
- **34, 43, 51 and 61, the cards' prices, with no CM-PLN-002 line.** The public cards' prices took CM-PLN-002 because their switch made them yearly (SH-92's P3). The admin's cards state a price per month and no period.
- **77, '+ variable fees', on CM-PLN-001.** What the variable platform fee is taken on isn't held: its dialog wasn't opened. If it is a share of sales, it is CM-PLN-003's too. The dialog's words would settle it.
- **116, 'Casual, in-person sales at pop-ups and events', on CM-POS-001 alone.**
  - The trial stores' answers give it the type casual_in_person_sales and the description 'Accept payments using Tap to Pay for iPhone or Android or a card reader.'. The page doesn't render that description.
  - SH-88 placed the US store's feature, 'Accept payments with a phone or card reader', on CM-PAY-021 and CM-POS-002 (its lines 32 and 33), by its words.
  - The other reading takes those two lines here as well, by the twin.
- **23 to 29, pos_lite's scope.** 'Included with all plans' is read as the five plans the answer lists. The other readings are no plan at all, or the POS page's four (SH-72's line 165).
- **27 and 28, the descriptions' lists** (purchase orders and stock counts; dashboards and cash tracking). They take no line. The other reading gives Retail inventory management lines on CM-INV-007 and CM-INV-003, and Retail reports one on CM-POS-003, POS Pro their scope.
- **35, 44, 52 and 62, the plan buttons, on CM-PLN-001 `core`.** The other reading is `out`, as UI strings. They name a plan and its trial, which the brief's UI string doesn't.
- **2, Balance:** its footnote's rates (3.32% and 2.29%) differ from the values (above). Which rate a store earns isn't settled by either.

## A structure whose items and sources disagree

- **The cards' prices:** the items join a card's three hidden parts as '$27 $1 /mo'. The source's label states '$27 USD per month, try for $1' (`aria-label`, source.html). The source governs: the quality takes the label's words.
- **'Plus+':** the `+` is an aria-hidden span inside the title (ibx5bt-xy's source.html), not a word of it.
- **The footnotes' numbers** cross the marks (above).
- **The Balance footnote's rates** differ from its row's (above).
- **`entries.tsv` names a repeated text's first line only:** 'enabled' stands for 152 cells a store, 'disabled' and '—' for 30. Their places are read from both stores' items (`places.py`).

## What a source states that no entry holds (for the second stage)

- **The trial stores' answers at step 98** request the plan RETAIL too (`answers/admin.shopify.com/PlanFeatureSetQuery/c6039bbf4031394b363a50a844539c551b88b63ac6d382197e7eaeb92a376006.json`, the same file in both runs, which their `answers.jsonl` names for step 98). They state Retail's values: pay_monthly '$89 USD/mo', pay_yearly_savings '$79 USD/mo', and pos_pro '1 location included per location'. These are leads for CM-PLN-001, CM-PLN-002 and CM-POS-001 on the Retail plan. The selection reads only the latest answer.
- **The rows' descriptions,** which the page shows only as tooltips. They are in the trial stores' answers, and most in the US store's, which SH-88 placed: Sell in AI chats' ChatGPT and Gemini; Unlimited web hosting's 'unlimited bandwidth'; Casual, in-person sales' Tap to Pay or a card reader.
- **The dialogs the page doesn't hold:** the credits' (three buttons) and the variable platform fee's. Their words would settle 77 (above). Only a capture holds them, and this pass sends no request.

## Problems with the brief or the scripts

- **`earlier` prints no twin across structures.** Neither structure's items have the other's `name` key. The feature set's twins were matched with `twins.py`, and the page's rows with SH-88's lines by summary. The cards were matched by hand, by element, as SH-92 did.
- **The heading-only twin match misleads on 'Pricing'.** `twins.py` gives the add-on's Pricing (23) the public table's section heading Pricing. The real twins are the POS page's posLiteVsProPlans (above). This is SH-73's warning: match a twin by its meaning.
- **`show` lists CM-MKS-006 and CM-PAY-017 as leads of every feature** by the field name `requiresShopifyPayments` alone, as SH-88 found. They are no leads.
- **No B-extent conflict** was found, beyond the two the brief states itself (qualities wider than B-extent's list; the rulings).

## The checker's lines, read again

- **No `CHANGES`:** every line is on a cell that already holds its support, or on the new thing.
- **`NOTE` on a product named with the platform's brand:** lines 3 to 6 (Shopify Balance, Capital, Credit and Bill Pay), 14 and 15 (Shopify Combined Listings, Shopify Audiences), 109 and 110 (Shopify B2B) and 122 (Shopify Collective).
  - Each is a plan line, `core` as its twin and the cell's plan row (SH-S-7062 to SH-S-7065, SH-S-7071, SH-S-7072, SH-S-7008, SH-S-7013) hold it, not by the name (R88.2).
  - For Capital, Credit, Combined Listings and Collective, whose own features are `own-service` by held maker statements, the plan line stays `core`: the rulings after SH-55 and SH-41, and the corrections with the changelog digest.
- **`NOTE` on line 97,** the new thing's row, whose first lead CM-PTN-008 holds nothing. Its cell was read (above), and the reading names it.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 7 lines, SH-68's new thing.

## The coordinator's check

Measured: 25.6 million tokens over 101 requests, about 197,000 an entry. The checker prints no problem and no `CHANGES` line.
- **Kept:** SH-88's rules for `plan-feature-set`'s last 29, so that structure is placed whole; R89.1 to R89.9, which SH-90 keeps; the seven entries joining SH-68's new thing; and the open choices as placed (each cell its own line, the marks `out`, '+ variable fees' on CM-PLN-001, entry 116 on CM-POS-001, pos_lite read as five plans, the descriptions' lists taking no line).
- **R89.9, the veto not used:** the navigation and the keyboard shortcuts are the admin's frame on this page, `out`, as a page's frame is elsewhere (SH-20's built-in feature pages, the mobile app's R80.1); the other reading would repeat `admin-main-nav`'s lines and change no cell. SH-91, which holds nearly all of that frame, is placed by `method/held_plan_frame.py` under this rule.
