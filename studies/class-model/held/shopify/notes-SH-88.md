# Notes on SH-88 (shopify, effort high)

85 entries of three structures, read at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure the pass reads). Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-88`).
- **1 to 4, `partners-dashboard-routes`:** the label `@source-maps`, its items at positions 123, 124, 125 and 127 (`items.jsonl`, lines 124 to 126 and 128), with their files in `source.jsonl`. Position 126 is SH-87's (its SH-E-594777b0).
- **5, `plan-comparison-admin`:** the header container of the admin's plan table at `settings/subscribe/select-plan`, held the same on the trial stores fake-demo-sharrwah and ibx5bt-xy (step 100 of runs `20260930T002940Z-sweep-trial` and `20260930T045741Z-sweep-trial2`). It is the structure's only entry: its 73 other items (11 section containers and 62 rows) have none, as the selection's note reads ('the rows not cited').
- **6 to 85, `plan-feature-set`:** the first 80 of its 109 entries: the sections Pricing to Sell globally of `planFeatureSet`, each section with its features, in the answer's order. They come from the answer `raw/runs/20261027T175456Z-journey-signup-located-us/answers/admin.shopify.com/PlanFeatureSetQuery/7bd0c74d….json`, the selection's latest. SH-89 holds the rest: Finance, Tax and Just for Plus, and the add-on set In-person selling (`planAddOnFeatureSet`, 7 features).

**Placed:** 85 entries in 96 lines.
- **By entry:** 80 on a capability, 2 on a new thing, 3 out. 11 entries take more than one line.
- **By line:** 91 on a capability, 2 new and 3 out.
- **Supports:** 76 `core` on capabilities, 2 `core` on new things, 14 `shows` and 1 `core;extension-point`. No line is `own-service` or `outside`.
- **Other columns:** 6 lines carry fillers and 34 qualities. 34 lines, of 27 entries, take the store tuu1u4-v0 in their scope (R88.4).

**Sources read:** the brief and what it names, and the evidence map. Then:
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`, and `REGISTER.tsv`'s rows for the three structures;
- `selection.tsv`'s rows and `show --meta`;
- B-extent.md's "Cells and evidence" and "Conventions from the dry run";
- the rulings' last section;
- SH-86's and SH-87's notes (R86.1 to R86.12, and both coordinator's checks), and SH-68's and SH-92's notes (R0 to R11, P1 to P12, and both checks).

The answer itself, and to clarify only:
- the run's `answers.jsonl` row, giving the store, step 30 and the variables;
- `index/instruments.json` for the store;
- the same run's BillingPlans answer;
- the other 120 PlanFeatureSetQuery answers, compared by a scratch script (R88.4);
- the pricing pages' `pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`, line 162, for the plan names.

For the routes, `source.jsonl`'s three section files, and the routes runs' steps 7, 10 and 11 and the from-source run's step 5.

## The routes (1 to 4)

SH-86's rules R86.1 to R86.12 and both coordinator's checks are kept; nothing here departs from them. Each route is its section's own index or fallback, so it takes its section's line (rule 3) with no term (R86.2: an index takes none):
- **1, PosDashboard's own route** (its path is `ROUTES.POS_DASHBOARD`, which the file sets to `/`; element PosDashboardLoader, module `./components/pos-dashboard`): CM-POS-001 `shows`, as its section (SH-86's SH-E-c13a76bf, SH-87's SH-E-cb34116d). Opened, the section lands on the partner's Home (routes run, step 10).
- **2, Activity's `/`** (ActivityLogLoader, `./activity-log`, for a user with develop_apps): CM-PTN-001 `core`, as its section (SH-86's SH-E-a9bc30c5). The user's gate goes in `reading` (R86.8).
- **3, SandboxOrganizations' `/`** (SandboxOrganizationsIndexLoader): `new:Sandbox organizations` `core`, SH-86's new thing.
- **4, SandboxOrganizations' last Route** (no path, element NotFound): `out`, the section's not-found fallback (R86.5). It has no `*` path, but the same element.

## The rules this batch sets (R88), for the coordinator to check and SH-89 to keep

The pricing batches' rules (SH-68's R0 to R11, SH-92's P1 to P12) are taken where they fit. Where they don't, the rule says so.

- **R88.1: a section** (`featureCategory`, `title`) is placed as its twin, the public comparison table's section heading of the same title (SH-68's R3; the rulings after SA-2, SA-5 and SA-28).
  - **A title that names a capability, or one part of the platform,** takes that capability's line, `shows`, with no plan in its scope. Pricing is CM-PLN-001; In-person sales CM-POS-001; AI features CM-AIA-001; Accepting payments CM-PAY-001; Hosting CM-OPS-003; Marketing CM-MKT-005; Shipping CM-SHP-001; Marketplaces CM-CHN-003; Sell globally CM-MKS-001.
  - **A title that names only a grouping is `out`:** Core features, Customization.
  - **For SH-89,** SH-68's R3 already reads two of its sections: Finance is `out`, and Just for Plus is CM-PLN-001 `shows`, scope shopify_plus. Tax takes its twin heading's line where one is held; otherwise it goes by the title, on the taxes' capability.
  - **The key is named in `reading`.** A key that names a product (`shopify_payments`, `shopify_shipping`, `shopify_marketplace_connect`) gives no line of its own, as a key's prefix isn't the entry's words (M-6 refined). The product's own feature carries the product: Shopify Payments, 36.
- **R88.2: a feature** is a plan line: B-extent's "a policy in the plan's own list", here the admin's own plan-by-feature data.
  - **Its twin.** Its `summary` is its twin row's heading and its `description` that row's tooltip, word for word. The twin is the row of the public table (`pricing-page-data`) of the same heading, matched by heading and tooltip by a scratch script, `twins.py`; `earlier` finds no twin across the two structures. The feature takes its twin's lines: capability, support, second lines and fillers. Its terms are its own summary's words, as the twin's are.
  - **Its type** (`pay_yearly_savings`, `swipe_rate`, `online_international_rates_when_premium`) is named in `reading` where it says more than the summary.
  - **A feature with no twin** is placed by its words on the capability whose cell cites the same plan row: Free Shopify Academy courses on CM-ONB-003, the 30 September row SH-S-7016.
  - **Its description:** a thing it names as the feature's own takes a line (SH-68's R3: the carriers of Shipping discounts, the merchant's own account in 3rd-party calculated shipping rates). Things it lists in passing ('like …', a list of uses) take none (the ruling after SA-41).
  - **A feature under a section whose title names a capability** also takes the section's line where it is a kind of that capability, and its own capability isn't the section's or its child (SH-68's R3). Customer profiles and Returns take CM-POS-001; Website builder takes CM-AIA-001.
  - **A name that carries the platform's brand** (Shopify B2B, Shopify Collective, Shopify Payments, Shopify Markets, Free Shopify Academy courses) names no maker. The feature is a plan line, and a plan line that includes a product stays `core` (the ruling after SH-55). The possessive on Hydrogen and Oxygen, “Shopify's React-based toolkit” and “Shopify's free global hosting solution”, names Shopify their provider (the ruling after SH-43). Build headless storefronts is still a plan line, so it stays `core`, as its twin.
- **R88.3: the values per plan give the scope and the qualities.**
  - **Scope.** The plans whose `value` is `true`, a text or a number are the line's scope, in the answer's `planName`: `starter_2022`, `basic`, `professional`, `unlimited`, `shopify_plus`, in the answer's order.
    - A plan whose value is `false` is left out of the scope and named in `reading`. So is a plan the values don't list: In-person manual rates lists no starter_2022.
    - This is the pricing batches' dash ('a dash leaves its plan out', SH-68's R3): for that plan the statement supports no placement. That is how this batch reads the coordinator's 'a feature a plan lacks is `shows` for that plan'.
    - A feature that every listed plan lacks would be `shows`, its plans its scope, as SH-74's Advanced tax platform ('Add on' on every plan). None of this batch's features is.
  - **'Add on'** keeps its plan in the scope, and the value goes in `reading`, as the twin of 3rd-party calculated shipping rates has it (SH-73's line 87: Grow's 'Add on' in scope).
  - **The `planName` identifiers are the source's** (rule 5: a plan in the source's identifiers). The POS page's plan summaries pair each with its name (`display_name` with `internal_name`, `pricing-page-data/…/items.jsonl`, line 162): Starter `starter_2022`, Basic `basic`, Grow `professional`, Advanced `unlimited`, Plus `shopify_plus`, Retail `retail`. The coordinator may write the names instead, to align with the pricing lines' `Basic;Grow;Advanced;Plus`.
  - **Qualities.** A price, rate, fee, count, limit, or a level in words that bounds the thing, is a quality (SH-68's R7). It is written `<value> (<planName>, …)`, plans with the same value together, in the answer's order. `true`, `false`, 'Add on' and a level of support or of a profile in words (Live chat, Simple, Full-featured, At purchase location) are not qualities: they go in `reading`.
  - **Starter.** A value for Starter states what the public table has no column for: its 2 inventory locations, its card rates of 5% + 30¢, its 5% third-party fee.
- **R88.4: the store.** The selection reads the latest answer.
  - **Whose it is:** the store tuu1u4-v0's, from step 30 of run `20261027T175456Z-journey-signup-located-us`, with the variables planNames STARTER_2022, BASIC, PROFESSIONAL, UNLIMITED, SHOPIFY_PLUS and includeAddOns true. It is a store in the United States: `index/instruments.json` gives it "business entity 'My Store - entity, United States'" and US Dollar.
  - **The other answers:** 120, all from the capture account's twelve other stores, from 21 September to 7 October. Each section and feature was compared with each store's latest answer (scratch `status.py`): its words, `requiresShopifyPayments`, and its values on the plans both answers list.
  - **No store:** a line whose section or feature every other store's answer states the same takes no store, as SH-68's R0 takes no site for a line that every read site states. That is 53 of the 80 entries.
  - **The store:** a line that only this answer holds, or whose words or values differ elsewhere, takes the store after its plans, `…;tuu1u4-v0`, as R0 lists sites after plans. That is 27 entries:
    - prices: Pay monthly and Pay yearly; the other stores state $27 and $72 USD/mo on basic and professional;
    - the credits' maximums: $4,500, $6,500 and $8,000 elsewhere;
    - words that differ: the in-person feature's ('Casual, in-person sales at pop-ups and events' elsewhere) and POS Pro's summary and Plus value;
    - in this answer only: Free Shopify Academy courses, the POS Customer profiles and Returns, the section Accepting payments with its 12 features, Shop Campaigns, and the section Shipping with its 4 features.
  - **By country, not by date, is a reading.** The other stores' $27 and $72 are the 30 September admin table's on two of them (`plan-comparison-admin`, items.jsonl line 3), and this answer's $39 and $105 are www.shopify.com's.
  - **For SH-89:**
    - the Finance section and its 4 features are the same in every store's answer;
    - the Tax section with its 4 features, and plus_shopify_audiences, are in this answer only;
    - the other Just for Plus features are in every store's answers: the latest answers of capture-advanced, capture-grow and zyd38b-ze request no SHOPIFY_PLUS, but their earlier answers hold the section;
    - the scratch scripts are in the folder named in the report.
- **R88.5: the mark \*.** A summary ending in `*` has `requiresShopifyPayments: true` in this answer. That is the public table's footnote '*Requires Shopify Payments' (SH-E-389f0e29).
  - The reading quotes both. It is a condition on the store's own setup, so it goes in `reading`, not in the scope, as the pricing lines have it (SH-71's lines 50, 80 and 82).
  - No CM-PAY-002 line is added: the pricing rows with the mark take none, and only the table's note row is CM-PAY-002 `shows` (SH-68's R3). This answer holds no note row.
- **R88.6: the admin's plan table** (`plan-comparison-admin`).
  - Its header container, Compare plans over Basic, Grow, Advanced and Plus, is the admin's own comparison of its plans: CM-PLN-001 `core` with no scope, since both held stores state it. This is SH-68's R3 for the public table's header. It is a container (M-13).
  - Its sections and rows would follow R88.1 to R88.5, the plans by the table's own names.

## New things

No new thing is proposed. Two entries join earlier batches' new things:
- **`new:Sandbox organizations`** (3, SH-E-3ae5cec0, the index at `/:organizationId/sandbox_organizations/`, position 125): SH-86's.
  - **Place of its own:** the route.
  - **Proposed** as in SH-86's notes: domain F, area DVT, parent CM-DVT-003.
  - **Name:** English only, since the dashboard isn't held in Arabic.
  - **Leads:** CM-ACC-003 and CM-PTN-002, by the word organization, hold an owner's several stores and the partner's own organization (SH-86's notes).
  - **Searched again:** sandbox; sandbox organization. Nothing is found.
- **`new:Earn 1% back on all sales as subscription credits`** (10, SH-E-fc0bf14b, `core_earn_back`): SH-68's.
  - **Place of its own:** a plan line. Here it is the admin's own plan feature, besides the public table's row.
  - **Its words:** 'Earn 1% back on all sales', 'subscription credits', 'Valid for your first 6 months or until you reach the max.'. The maximums are Up to $5,000, $7,500 and $10,000 USD on basic, professional and unlimited, the same as www.shopify.com's; starter_2022 and shopify_plus are false.
  - **Proposed** as in SH-68's notes: domain A, area PLN, parent CM-PLN-004.
  - **Leads:** CM-PLN-001 and CM-PTN-008, by the words basic, subscription, earn and sale, hold the plans and partners' referrals, not credits to the merchant.
  - **Searched again:** subscription credit; billing credit; earn back; earn 1%. Nothing is found.

## Entries I couldn't tell, and what would settle each

- **R88.3's reading of 'a feature a plan lacks is `shows` for that plan'.**
  - The other reading is a second line per feature, `shows` on the same capability, scoped to the plans whose value is `false`.
  - That would add about 15 lines and change no cell. The checker also allows a second line on one capability only for another thing under its own condition (the ruling after SH-34).
  - The coordinator's choice settles it. Every plan left out is named in `reading`, so either can be built from the lines.
- **R88.4's store.** The other reading puts tuu1u4-v0 on every line, since the selection reads one store's answer. The measurement (R88.4) is what the choice rests on, as R0's was.
- **The scope's plan identifiers** (R88.3): `planName` or the display names. Both are the source's, paired at the POS page's summaries.
- **68's professional 'Add on'** in the `core;extension-point` line's scope, as its twin. The other reading is `shows` for professional, an add-on the plan doesn't include, as SH-74's Advanced tax platform.
- **1, PosDashboard's index, `shows`; and 2, Activity's index, CM-PTN-001.** SH-86's doubts carry over to both (its notes: the POS page itself; CM-APP-002 for Activity by the element's name). A partner whose pages render would settle them.
- **25, Free Shopify Academy courses.**
  - No pricing-page-data or plan-page-public entry holds the row, so its line rests on the 30 September row SH-S-7016 alone.
  - Whether the 31 October pages dropped it isn't settled: twins were matched by heading only.
- **8, Pay yearly.** The answer states $89 and $359 USD/mo for professional and unlimited. www.shopify.com's table of 31 October states $79 and $299 for Grow and Advanced (SH-E-4c658b69). The same run's BillingPlans answer agrees with the feature set: annualPrice 1068.0 and 4308.0, twelve times 89 and 359. Which yearly price a US store is charged isn't settled by either. The lines quote their own words.

## A structure whose items and sources disagree

- **`REGISTER.tsv` counts 120 answers in 46 runs on 12 stores.** 121 are held, in 47 runs on 13 stores (the runs' `answers.jsonl`): the US store's answer of 27 October is the 121st. It is the selection's latest, and the only one with the Shopify Payments, Shipping and Tax sections. The register's row is older than the run (an assumption, from its count).
- **The plan feature set's prices differ from the public table's** (8, above). Plus's monthly value is 'Starts at $2,300 USD/mo' in both. The same run's BillingPlans answer states shopify_plus at monthlyPrice 2500.0 and annualPrice 30000.0 USD (`answers/admin.shopify.com/BillingPlans/2db78a22….json`). That may be a price before Plus's variable part, which the admin table writes as 'Starts at $2,300 USD/mo+ variable fees' (`plan-comparison-admin/fake-demo-sharrwah/items.jsonl`, line 3). This is a reading.
- **`plan-comparison-admin` has one entry for 74 items** (above). Its items and `source.html` agree. The two stores' `items.jsonl` are identical.

## What a source states that no entry holds (for the second stage)

- **The BillingPlans answer of the same run** (`raw/runs/20261027T175456Z-journey-signup-located-us/answers/admin.shopify.com/BillingPlans/2db78a22b9d7315d3a329899dc0b46396f5f7f866f0f8bd01c1147cdaa950f27.json`) holds each plan's monthly and annual price as an amount, in USD:

  | Plan | Monthly | Annual |
  | --- | --- | --- |
  | basic | 39.0 | 348.0 |
  | professional | 105.0 | 1068.0 |
  | unlimited | 399.0 | 4308.0 |
  | shopify_plus | 2500.0 | 30000.0 |
  | starter_2022 | 5.0 | 60.0 |
  | retail | 89.0 | 948.0 |

  These are qualities for CM-PLN-001 and CM-PLN-002, the Retail plan among them.
- **The admin table's Plus cell** 'Starts at $2,300 USD/mo+ variable fees' (`plan-comparison-admin/fake-demo-sharrwah/items.jsonl`, line 3): a variable fee on Plus, a lead for CM-PLN-001 and CM-PLN-003. Its container 'Sell globally*Requires Shopify Payments' (line 53) holds the footnote.
- **The other twelve stores' answers,** for the market subjects (prices by market): the plans' prices ($27 and $72 USD/mo on basic and professional monthly; $19, $54 and $299 yearly), the credits' maximums, and the sections they don't hold (R88.4). Each store's latest answer is named in the scratch script's output.

## Problems with the brief or the scripts

- **`earlier` prints no twin** across the feature set and the pricing pages: neither has the other's `name` key. The twins were matched by heading and tooltip with a scratch script that reads `entries.tsv` and the placements, listed in the report.
- **`show` lists CM-MKS-006 and CM-PAY-017 as leads of every feature** by the field name `requiresShopifyPayments` alone. That is no lead (the brief), and the readings don't name them.
- **The coordinator's rule on a plan that lacks a feature** can be read two ways (above). R88.3 says which this batch took.
- **No B-extent conflict** was found, beyond the two the brief states itself (qualities wider than B-extent's list; the rulings).

## The checker's lines, read again

- **`CHANGES CM-POS-002@shopify gains core, by line 33`** (27, the phone and card reader of 'Accept payments with a phone or card reader'). Kept. It is the plan line that includes taking payments with a phone or a paired card reader. SH-68's line 122 placed it so, and the coordinator's check after SH-68 kept it; SH-71's line 33 is the same. The cell changes by this line alone because the earlier batches' lines aren't amended into the model yet.
- **`NOTE` on a product named with the platform's brand** (lines 20, 21, 26, 30, 45 and 94: Shopify B2B twice, Shopify Collective, Free Shopify Academy courses, Shopify Payments, Shopify Markets). Each is `core` as a plan line, which the twin and the cell hold (SH-S-7008, SH-S-7013, SH-S-7016, SH-S-7020, SH-S-7059), not by the name (R88.2).
- **`NOTE` on footnote marks** (lines 55, 77, 93 and 95: Built-in fraud analysis, Shipping insurance, Show prices in local currencies, Accept local payment methods). Each reading quotes the footnote '*Requires Shopify Payments' (SH-E-389f0e29) and the answer's `requiresShopifyPayments: true` (R88.5).
- **`NOTE` on a new thing whose entry has leads** (lines 4 and 13). The leads are read above, with SH-86's and SH-68's notes. None holds sandbox organizations or credits to the merchant.
- **`NEW`:** Sandbox organizations and Earn 1% back on all sales as subscription credits, 1 line each. Both are earlier batches' new things.

## The coordinator's check

Measured: 21.0 million tokens over 94 requests, about 247,000 an entry. The checker prints no problem.
- **Kept:** R88.1 to R88.6, which SH-89 keeps; the routes by R86; the one `CHANGES` line, CM-POS-002 `core`, as SH-68:122 and SH-71:33 placed the same plan line; and the two entries joining earlier new things.
- **The plans in scope, aligned:** the 80 lines that named Shopify's identifiers now name the plans as the pricing lines do (Starter, Basic, Grow, Advanced, Plus), the identifiers paired with them by the pricing data's own answer (`pricing-page-data` items.jsonl, line 162) and named in each reading. The cells' scopes then compare across the admin's and the public tables.
- **The open choices:** a plan that lacks a feature stays out of the `core` line's scope, named in its reading, with no extra `shows` line; the US store `tuu1u4-v0` stays in scope only where the stores' answers differ; Grow's 'Add on' stays as its twin has it.
- **The price differences** (Grow's and Advanced's yearly prices, Plus's monthly) and the register's stale count of answers are leads for the second stage, in this batch's notes; the register is observed-sh's own, read-only here.
