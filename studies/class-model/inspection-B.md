# Inspection of brief B (`studies/class-model/briefs/B-extent.md`)

Status: complete (30 October 2026). 19 findings: 13 must fix and 6 optional.

An inspection in Fagan's sense (1976): it looks for what would make an agent that follows the brief produce wrong, slanted or uncheckable rows. The inspector wrote none of the brief and changed nothing but this file. Every judgement below is marked **Reading**. Every count comes from a script named with it; the scripts are in the inspector's scratchpad and are restated in prose where a count depends on a choice.

## What was read, at which commits

- **This repository** at `93ebb15c` (branch `claude/vibrant-meitner-oh70v4`):
  - the brief, `studies/class-model/briefs/B-extent.md` (79 lines), whole;
  - `studies/class-model/seed/README.md` and `km-areas.tsv` (41 areas, 8 domains); not `km-questions.tsv`, as the brief says;
  - `studies/concern-map/README.md`; for each of the five platforms, the headers and columns of `concerns.tsv`, `statements.tsv`, `inventory.tsv`, `citations.tsv`, `gaps.tsv`, queried by script; the concern names of all five platforms; the `notes.md` sections "Lists used and their sizes" and "Where the inventory stops" (Salla's read in full, the others searched);
  - `studies/concern-map/matches.tsv` (88 rows) and `unclear-matches.tsv` (84 rows), by script; `map/out-of-scope.tsv`, by script; `matching-notes.md`, lines 196 to 212;
  - `questions/Q1-concern-map.md`, whole;
  - `PLAN.md`, lines 204 to 224 (Stage 4A) and 318 to 330 (section 6's kinds), and, for single checks, lines 36, 180 to 193, 284 to 300, 353 and 470 to 476;
  - `founder-decisions.tsv`, the rows of 26 to 29 October, for one check (the founder's intent of 29 October);
  - `evidence/product-class/README.md`, and the `manifest.tsv` of every run under `evidence/product-class/runs/`, by script;
  - `method/README.md`.
- **observed-sh** at `/home/user/observed-sh`, HEAD `19a5f643`: only to check that the commits Q1 cites (`b46731d0`, `e49840729`) exist and that the cited paths resolve at them.
- **observed-sa** at `/home/user/observed-sa`, HEAD `b0bd0b16`: the same check for `145f137`.
- **other-product-class** at `/home/user/other-product-class`, HEAD `0d79b794`: its `README.md` only. Q1 cites nothing in it (all Zid and BigCommerce citations are URLs; script below), so no citation the brief relies on resolves there.
- **The WooCommerce 11.2.1 release** at `/home/user/woocommerce-release/11.2.1`: the 41 release files that domain B's statements cite, each checked against `evidence/product-class/woocommerce-11.2.1/files.tsv` by sha256 (41 of 41 match).
- **After the findings were written:** `studies/class-model/inspection-A.md`, for the section on its must-fix findings.

**The repository moved during the inspection.** The coordinating session committed `7ad5cfda`, `e5af817b` and `addea485`, which changed `PLAN.md`, `STATE.md` and `founder-decisions.tsv` (the founder's change of 30 October, on architecture's own plan) and saved this file. `git diff 93ebb15c HEAD` shows no change to the brief, the seed, `studies/concern-map/` or `questions/`. Stage 4A's rules for the extent are unchanged in substance; only the bullet on the independent review gains "with the architecture plan". Every line number cited here is at `93ebb15c`.

### Citations the brief relies on resolve

For the statements of the concerns the inspector reads as domain B's (the sets are under finding 12), every cite id exists in its platform's `citations.tsv`, and every source resolves: Shopify 469 local paths at their observed-sh commit and 36 URLs; Salla 366 at `observed-sa@145f137` and 9 URLs; WooCommerce 91 release paths and 50 URLs; Zid 58 URLs; BigCommerce 61 URLs. A URL resolves through the `cited_in` column of a capture run's `manifest.tsv`, except `SH-S-7284` (`https://www.shopify.com/legal/terms`, cited by 6 of the in-scope statements), which no manifest lists by its id but whose URL is captured in `20261011T061248Z-q1-shopify-sources`. (Script: `resolve.py` in the scratchpad: `git cat-file -e <commit>:<path>` for local sources, path existence for the release and this repository, `cited_in` for URLs.)

## Summary

| # | Finding | Verdict |
| --- | --- | --- |
| 1 | No rule says which concerns belong to a domain. `concerns.tsv` has no area. The seed lists gift cards and Gifting in two domains each, and Q1's matches (`M-013`, `M-074`) cross domains. | must fix |
| 2 | The area rule presupposes that the platforms place things in the seed's areas. There is no rule where the two differ, where one shows the capability, or for mapped platforms, and domain H isn't ruled out. | optional |
| 3 | The dry run's mapping part has no domain to stay within. Read as written, about a hundred WooCommerce concerns outside B become "only WooCommerce" capabilities. | must fix |
| 4 | "Lands once" fails where a concern is coarser than the capabilities (`WC-C-064`, `BC-C-010`) and makes false "Q1 holds nothing" cells. A Q1 match with several concerns on one side is both a join and a grain difference. | must fix |
| 5 | The mapping maps onto "the anchor" only. Capabilities an earlier mapping part added get duplicated, and the platforms mapped before never get cells for them. The counts then depend on the order. | must fix |
| 6 | "Q1 holds nothing" has no fixed token. Absence rests on Q1's `notes.md`, a derived document that never calls a list complete, against PLAN line 292 and Q1's rule 6. | must fix |
| 7 | The four placement values have no rule tying them to statements: own extensions, API objects, merchant responsibility, and no supporting statement. The kind (`class` or `slot`) flips on them. | must fix |
| 8 | The cells can't be checked mechanically. There is no list separator. The statement key isn't unique (119, 130 and 97 rows on Shopify, Salla and WooCommerce). A single scope per cell loses each statement's scope. | must fix |
| 9 | The mapping pass has no column for how a concern joined, and the `join` values lack identifier and definition. Role joins can't be checked, though PLAN line 36 says the coordinator checks them. | must fix |
| 10 | A shared term alone can join different things. Q1 found 6 such cases, and domain B has `Locations` and `Subscriptions`. | must fix |
| 11 | `unclear-matches.tsv` has no `note` column, and no ruling on the 21 in-scope unclear candidates is asked for. | must fix |
| 12 | The parts aren't small. The anchor part for B reads about 410,000 to 918,000 bytes; the mapping part spans all domains. The brief gives no slice script, against PLAN lines 184 to 187. | must fix |
| 13 | Qualities have no capability and no scope, slot fillers presuppose the kind, and the unplaced limits Q1 left out can't be reached. | must fix |
| 14 | Cells carry no gaps, against PLAN line 353, so a placement read from weak evidence looks like any other. | must fix |
| 15 | URL sources and the release have no commit in `citations.tsv`, and the brief doesn't say whether context read beyond Q1 may be cited. | optional |
| 16 | The sentence on permissions, topics, scopes and plan lines can be read as excluding the concerns that are those systems. | optional |
| 17 | Smaller convention gaps: capability names, numbering across mapping parts, part names, `area` and `parent`, market-scoped capabilities. | optional |
| 18 | "Placement" means two things, and the agent never reads Q1's meanings or its rule on inference in notes. | optional |
| 19 | "Read in full" is not what Q1 shows for Salla (206 of 230 gaps "page not read"). | optional |

**What blocks the dry run.**
- **Finding 3, outright.** The WooCommerce part would land all 118 concerns against an anchor that holds only domain B.
- **Findings 1 and 4 make wrong rows in domain B itself.** Gift cards (`M-013`) and subscriptions (`M-074`) cross into domains C and D. `WC-C-064` would land in one capability and leave false "nothing held" cells in the others.
- **Findings 6 to 9 make the rows uncheckable.** The dry run's review, and the checker the plan wants from it (PLAN line 214), would then have nothing fixed to test.

**Reading:** the cheapest unblocking set is:
- a scope file assigning every concern to one domain (findings 1 and 3);
- `landings.tsv` (findings 4 and 9);
- fixed tokens, separator and statement key (findings 6 and 8);
- the placement tests with per-value evidence (finding 7).

## Findings

### 1. No rule says which concerns belong to a domain, and concerns and Q1's matches cross domains

**The brief's words.** Line 17: "Shopify's and Salla's `concerns.tsv`, whole; take the concerns that belong to your domain". Line 60: "In the anchor pass, a concern you look at and leave for another domain is listed, with that domain, in your notes." PLAN line 215 runs the anchor "one part per domain".

**The problem.** `concerns.tsv` has no area or domain column (header on every platform: `concern_id concern platform_terms inv_ids split_note`). Which concerns are a domain's is each agent's own judgement, made by seven anchor parts (domains A to G) that don't see each other's output. A concern that two domains can claim is taken twice, or by neither, and the only trace is free text in two `notes.md` files. **Reading:** this is the brief's largest source of wrong rows, because it decides what each part even looks at.

**The evidence.**
- The seed itself puts one grouping in two areas of different domains: Shopify's "gift cards" under SEL (domain B) and LOY (domain D); Salla's "Gifting" under SEL and LOY (`km-areas.tsv`, rows SEL and LOY; script: every `;`-separated label listed under more than one area).
- Concerns span domains: `SA-C-063` "Customer wallet, cashback and gift cards" (SEL and LOY); `SA-C-125` "Recurring payments and subscriptions sold by stores" (SEL and PAY); `SA-C-127` "Charity stores' payment gateways" (the seed's SEL label "Charity stores", and PAY); `BC-C-010` "Marketing: coupons, banners and gift certificates" (MKT and SEL or LOY); `WC-C-104` "Merchandising extensions (bundles, gifts, product options, pricing, display, variations, …)" and `WC-C-105` "Conversion extensions (feedback, promotions, order recovery, loyalty, alerts, upsells)".
- Q1's matches cross domains, so a match can be split between two parts: `M-013` joins `SH-C-025` Gift cards with `SA-C-063` (wallet); `M-074` joins `SH-C-186` Subscriptions and selling plans, `SA-C-125` and `WC-C-100`. Of the 88 matches, 13 touch a concern the inspector reads as domain B's, and 7 of them touch it only through a concern that could belong elsewhere (`M-020`, `M-046`, `M-055`, `M-065`, `M-075`, `M-080`, `M-083`). Of the 84 unclear candidates, 21 touch one (script over `matches.tsv` and `unclear-matches.tsv` with the sets of finding 12).

**Proposed fix.** Before any anchor part runs, the coordinator writes one scope file, for example `studies/class-model/scope.tsv`: `platform · concern_id · domain · reason`, one row for every concern of all five platforms (198 + 152 + 118 + 96 + 88 = 652 rows), each a reading, with one rule for a concern that spans domains (it goes to one domain, named in `reason`, and the other domain's part sees it read-only). The brief then says "take the concerns `scope.tsv` gives your domain", and the "left for another domain" list becomes unnecessary. A checker tests that every concern is in exactly one domain, and that every Q1 match's concerns are in one domain or the split is named.

### 2. The area rule presupposes that the platforms place things in the seed's areas

**The brief's words.** Line 30: "each capability gets one area, the one where the two platforms put it. Each platform's own place goes in its cell." Line 34: "in a new capability that only your platform shows, with its area."

**The problem.** The platforms put a capability in their own admin sections, API groups and app categories, not in the seed's areas; the area is the agent's matching of those places to the seed's labels. The rule gives no answer when the two platforms' places fall in different areas, when only one platform shows the capability, or in the mapping pass, where the seed has no labels for WooCommerce, Zid or BigCommerce (`seed/README.md`: "Its labels are Shopify's and Salla's only"). Nor does the brief say that domain H ("Beyond the references") takes no capabilities, as PLAN line 215 does. **Reading:** within a domain this misfiles rows rather than corrupting them, so it is optional once finding 1 fixes the domain.

**The evidence.** Subscriptions: Shopify's seed label puts "subscriptions" in SEL; Salla's concern `SA-C-125` sits under its "Recurring Payments API" in the docs navigation (`SA-S-1173`), and Salla's SEL labels don't name it. `WC-C-093` "Cost of goods sold" has no seed label at all and could be CAT, INV or ANL.

**Proposed fix.** Area by this order: the seed label that names the platform's own term; where the two platforms differ, the area of the platform whose place is an admin section, with the other area in `note`; in the mapping pass, the area of the anchor capability that is its nearest parent, else the seed label with the same term. Never an area of domain H. A checker tests that `area` is an `area_id` of the part's domain and that `cap_id` carries it.

### 3. The dry run's mapping part has no domain to stay within

**The brief's words.** Line 18: "in the mapping pass: your platform's `concerns.tsv`, whole". Line 32: "In the mapping pass: each of your platform's concerns lands once." Line 34: "or in a new capability that only your platform shows". Line 11: "Your message names the pass and your domain or platform."

**The problem.** In the dry run the anchor holds domain B only. A WooCommerce agent that follows the brief takes all 118 of its concerns and must land each one: every concern outside B (payments, tax, shipping, legal, …) has no anchor capability to land in, so it lands "in a new capability that only your platform shows". That is false for most of them: Shopify and Salla show payments and tax, they are simply not in the anchor yet. **Reading:** as written, the dry run's mapping part produces about a hundred wrong "only WooCommerce" capabilities, and the review of the dry run would review mostly these. This blocks the dry run.

**The evidence.** WooCommerce has 118 concerns (`concerns.tsv`); the inspector reads 5 as clearly domain B's and 9 more as possibly so (finding 12). 71 of the 118 are in a Q1 match with a Shopify or Salla concern (script over `matches.tsv`), so they are certainly not "only WooCommerce".

**Proposed fix.** The mapping part takes the concerns `scope.tsv` (finding 1) gives the domains the anchor already holds, and lists the rest as "not mapped: domain not in the anchor yet". Or the message for the dry run names the domain, and the brief says the mapping part takes only that domain's concerns. Either way the brief says so, not only the message.

### 4. "Lands once" fails where one platform's concern is coarser than the capabilities, and makes false "Q1 holds nothing" cells

**The brief's words.** Line 27: "Join concerns that are the same thing on both platforms … Q1's matches are such joins." Line 29: "Where they cut at different grains, you choose the capabilities, using `parent` where one holds others." Line 32: "each of your platform's concerns lands once." Line 50: "Q1 holds nothing for this platform here: say that in so many words." Line 60: "Every concern you take appears in a cell." PLAN line 215: "checks that each concern lands once".

**The problem.**
- In the mapping pass, a concern that covers several anchor capabilities can land in only one. The cells of the others then say "Q1 holds nothing" for that platform although Q1 holds statements for them inside the coarser concern. Under the plan's rule, a "nothing held" cell is not counted, so a false one lowers the count and can turn `class` into `slot`.
- The anchor pass says "appears in a cell" (no "once"), the mapping pass "lands once", the plan "lands once". Whether a concern whose statements are cited in two capabilities' cells has landed once or twice is not defined, so the coordinator's check has nothing fixed to test.
- A Q1 match with several concerns on one side is a grain difference, but line 27 calls every match a join. Followed literally, `M-011` makes one capability of products, options and variants, categories and brands.
- A capability's statements are not always in one concern, so a "nothing held" written from the concern list alone can be false.

**The evidence.**
- `M-011`: `SH-C-020` against `SA-C-020;SA-C-021;SA-C-022;SA-C-023` against `WC-C-064`. Its own `granularity` note: "Salla splits products (SA-C-020), options and variants (SA-C-021), categories (SA-C-022) and brands (SA-C-023); WooCommerce keeps all in WC-C-064; Shopify keeps variants with products, has no brands concern". 27 of the 88 matches hold more than one concern on at least one side (13 Shopify, 10 Salla and 10 WooCommerce cells hold a list; script).
- `WC-C-064` "Products and catalogue structure (types, variations, attributes, categories, tags, brands)" holds the `where` rows "Products > Categories" (`WC-S-0052`), "Products > Tags" (`WC-S-0053`), "Products > Brands" (`WC-S-0054`) and "Products > Attributes" (`WC-S-0055`). If it lands in a "Products" capability, the WooCommerce cells of whatever capabilities the anchor makes for categories, brands, and options and variants (Salla's `SA-C-022`, `SA-C-023`, `SA-C-021`) say "nothing held".
- `BC-C-010` "Marketing: coupons, banners and gift certificates" holds BigCommerce's only gift-certificate statements (1 for "gift certificate", 1 for "gift card"; script over `statements.tsv`). If it lands with coupons, BigCommerce's gift-card cell says "nothing held".
- WooCommerce's statements naming brands, variations, attributes or categories sit in `WC-C-064` and also in `WC-C-079` (Store API), `WC-C-038` (analytics), `WC-C-058`, `WC-C-104` and `WC-C-105` (script: regex over `identifier` and `statement`).

**Proposed fix.**
- Separate a concern's landing from the statements a cell cites. Each part writes `landings.tsv`: `platform · concern_id · cap_id · join · join_evidence`, exactly one row per concern taken. A cell may cite statements of a concern landed elsewhere; `reading` then says so.
- A coarser concern lands on the parent capability, and the child capabilities' cells cite its statements.
- A Q1 match with several concerns on a side is handled by line 29's rule, not as one capability.
- "Q1 holds nothing" is written only after searching the platform's statements, not only its concerns, for the capability's terms in every language the platform uses, with the search terms recorded (finding 6).

The checker tests "lands once" on `landings.tsv`.

### 5. The mapping pass maps onto "the anchor" only, so later capabilities are duplicated, and earlier platforms never get cells for them

**The brief's words.** Line 7: "Each is mapped onto the anchor's capabilities. Where a platform shows something the anchor doesn't, it adds a capability". Line 18: "the anchor's merged `studies/class-model/capabilities.tsv` and `cells.tsv`". Lines 33 and 34: "in an anchor capability … or in a new capability that only your platform shows". Line 40: "one row per capability and platform, for your pass's platforms."

**The problem.**
- **Duplicates.** Zid runs after WooCommerce. A concern Zid shares with a capability WooCommerce added is neither "an anchor capability" nor "only your platform's", so the brief has no place for it. Read literally, Zid adds the capability again. PLAN line 210 says each platform adds "what it alone shows", which presupposes mapping onto the model so far.
- **Missing cells.** A capability added in the mapping pass gets a cell only for the platform that added it, and for the platforms after it only if they map onto the model so far. Shopify and Salla never get one, even where the coarser anchor concern holds statements for it. The plan's count is then biased by the order: the count of a capability BigCommerce adds is at most 1, and the anchor's shape wins by construction. **Reading:** this is a slant toward Shopify's and Salla's shape, beyond the exemplar design the plan chose.
- **Strained fits.** These are free text in `notes.md` (line 36), so the reviewer's split has no checkable input.

**The evidence.** The order is WooCommerce, then Zid, then BigCommerce (brief line 7; PLAN line 210). `matches.tsv` has no `zid` or `bigcommerce` column: Q1 stopped Zid and BigCommerce before matching (`Q1-concern-map.md` line 116). Their mapping parts are therefore the only place their joins are made.

**Proposed fix.**
- The mapping part reads "the model so far": the anchor and every earlier mapping part, merged.
- For every capability a mapping part adds, the coordinator, or a short back-fill part, writes cells for the platforms already mapped. Each such cell cites their statements, or says "nothing held" after the search of finding 6. The new capability takes a `parent` where it refines an existing one.
- Strained fits go in a TSV, `strained.tsv`: `platform · concern_id · cap_id · what does not fit · evidence`.

### 6. "Q1 holds nothing" and "missing from a complete list" have no fixed form, and the completeness test contradicts Q1 and the plan

**The brief's words.** Line 50: "Q1 holds nothing for this platform here: say that in so many words. It never means the platform lacks it. A complete list showing it missing is named, with where that list is described as complete." Line 21: "each platform's `notes.md`, only where it says how complete one of its lists is".

**The problem.**
- "In so many words" fixes no token and no column, so neither the checker nor the coordinator's count can recognise the case mechanically.
- The test for absence points at Q1's `notes.md`. That is a derived document, and Q1's rule 2 says derived documents "only point" and are never cited. It also describes Q1's inventory (the lists Q1 read and their sizes, "where the inventory stops"), not the completeness of the platform's own list.
- PLAN line 292 counts absence "only from a complete list the platform publishes, such as an enumerated schema or a full plan table". Q1's rule 6 says observed-sh and observed-sa "hold what has been observed, not the platforms' full limits. A key or value absent from them is a gap, never 'does not exist'". Since 13 October, a "searched, not found" must show `method/corpus_search.py` run in every language (PLAN lines 473 to 476); the brief names none of this.
- The plan's kind-and-count rule does not use absence at all: a platform is counted only when it places the capability in its core or own service.

**The evidence.**
- `notes.md` never calls a list complete. Searched for "complete", "in full", "whole list", "every entry" and "all entries": 2 hits in Shopify's notes and 2 in WooCommerce's, all about other things; none in Salla's, Zid's or BigCommerce's.
- What the notes do have is sizes: for example Salla's "settings | `dashboard-settings-menu/merchant@en` | 23 pages and 4 group headings" (Salla `notes.md`, line 36). That is the menu of one observed store.

**Proposed fix.**
- Give the cell a fixed column `held`, with three values: `statements`, `none held` or `absent from a published complete list`.
- The third value is allowed only with the cite id of the platform's own list and its corpus search; Q1's notes are never its basis. Or drop it from this pass, since the count doesn't need it.
- `none held` records the search terms and languages used. The checker tests the token and, for `none held`, that no statement of that platform matches the recorded terms (finding 4).

### 7. The placement values have no rule tying them to statements, and the kind flips on them

**The brief's words.** Lines 42 to 48: "**Placement,** as your reading of those statements: `core`: part of the platform itself; `own service`: a separate line of the platform's company, such as a payments, shipping or buyer app of its own; `extension point`: where third parties plug in; `outside`: the platform says another party does it. More than one may apply." Line 38: "staff permissions, webhook topics, access scopes and plan lines are evidence for a capability".

**The problem.** The plan computes the kind from these values: `class` where a platform places the capability in its core or own service, `slot` where every platform that shows it gives `extension point` or `outside` (PLAN line 216). So the line between `own service` and `extension point`, and between `core` and `extension point`, decides the kind. The brief leaves four cases without a rule. **Reading:** without a rule, `core` becomes the default wherever a platform has an API object, and `slot` almost never results.
- **A platform's own extension sold through its extension point.** Woo-made extensions in the Woo Marketplace, or a platform's own app in its app store, fit both `own service` and `extension point`.
- **API resources at an extension point.** API objects, scopes and webhook topics that exist so that apps can do the work read as `core`, although line 38 calls them evidence.
- **"Another party".** Statements that make the merchant legally responsible can read as `outside`, and the brief doesn't say that "another party" means a third party, not the merchant or buyer.
- **No supporting statement.** There is no value for a platform that shows the capability but whose statements support no placement. The plan's rule then has no answer ("every platform that shows it" fails), and the agent is forced to pick one.

**The evidence.**
- **Subscriptions.** `WC-C-100`: `where` "Extensions > Merchandising > Subscriptions" (`WC-S-0739`); `decides` "WooCommerce Subscriptions is a premium extension …" (`WC-S-5351`). That it is Woo-made is stated only under another concern, `WC-C-050` "Developed by Woo" (`WC-S-0697`). Shopify's `SH-C-186`: `where` "Subscription apps" (`SH-S-2657`) and "Subscription apps enable developers and merchants to build subscription experiences" (`SH-S-0763`), with 14 `boundary` rows: access scopes such as `read_own_subscription_contracts` and `write_purchase_options`, webhook topics such as `subscription_billing_attempts/success` and `selling_plan_groups/create`, and the mutation `subscriptionContractActivate`. They are the API an app uses for its own subscription contracts, and read alone they look like `core`.
- **Gift cards.** `SH-C-025`'s `responsible` rows: "you are legally responsible for all gift card or store credit issuance and management; Shopify merely provides software" (`SH-S-0676`, also `SH-S-0677` and `SH-S-0678`), beside the admin routes `gift_cards` (`SH-S-5170`, `SH-S-5013`).
- **No `where` row.** `SH-C-038` Combined listings has none (gap `observation needed`); `WC-C-102` Memberships has a Marketplace category only.

**Proposed fix.** The brief states which statement supports which value. One proposal:
- `core`: a `where` row naming the platform's own admin section, setting or code path, or the platform's own API group;
- `own service`: a statement naming the platform's company, or a separate entity of it, as the maker or provider;
- `extension point`: an app-store or marketplace category, an extension target, or a provider interface;
- `outside`: a statement naming a third party, not the merchant or buyer, as the one who does it.

Each value carries its own cite ids (`core:SH-S-5170,SH-S-5013;extension point:SH-S-2657`). A fifth value, `not stated`, is for a platform whose statements support none. The reviewer and the checker then test each value against the statements it cites.

### 8. The cells are not mechanically checkable as specified

**The brief's words.**
- Line 41: "its terms, and where it puts the capability …, with each statement's concern id, cite id and identifier".
- Line 49: "The statements' scope, as stated".
- Line 65: "Tab-separated files, with a header row and no quoting".
- Line 67: `cells.tsv`: "`concern_ids` · `terms` · `where` (its own words, with ids) · `placement` · `scope` · `evidence` (cite ids and identifiers) · `reading`".

**The problem.**
- **No list separator.** No separator is set for multi-valued cells, and two placement values contain a space ("own service", "extension point"). Q1's own lists use three different separators: `;` (Shopify), a space (Salla, WooCommerce) and `, ` (Zid, BigCommerce) in `inventory.tsv`'s `concern_ids`.
- **The statement key isn't unique.** Concern id, cite id and identifier together don't identify a statement row, so a checker can't tie a cell's evidence to one row of `statements.tsv`, and the review "checks every placement against all of Q1's statements" can't be automated.
- **One scope per cell.** A single `scope` per cell can't keep each statement's scope, so line 59, "A statement scoped to one market keeps that scope", can't be verified once statements with different scopes are merged.
- **Free-text terms and places.** `terms` and `where` are free text, so a checker can't test that they are the platform's own words.

**The evidence.**
- **The key.** Rows sharing (`concern_id`, `cite_ids`, `identifier`) with another row: Shopify 119 of 3,005, Salla 130 of 2,560, WooCommerce 97 of 1,499, Zid 0, BigCommerce 0. Adding Q1's `placement` leaves 0 on every platform. In domain B's scope: Shopify 6 of 312 (for example `SH-C-188`, `SH-S-2207`, `product_configuration`, under `where` and `boundary`), Salla 26 of 375, WooCommerce 0 of 135. Script: counts of the key tuples over `statements.tsv`.
- **Scope.** Scoped statements in domain B's scope: Shopify 45 of 312 (for example "store capture-plus (its UCP profile)"), Salla 129 of 375 (for example "plan: سلة بلس"), WooCommerce 14 of 135.

**Proposed fix.**
- Fix one list separator, for example `;` with no spaces, and fixed tokens for placement and the other value sets.
- Cite each statement by the key `concern_id|placement|cite_id`, unique in every platform's file.
- Put the scope per statement in `evidence`, as `key=scope`, and drop the separate `scope` column or make it derived.
- `terms` holds only strings found verbatim in the cited statements or in the concern's `platform_terms`.

### 9. How a concern was joined can't be recorded in the mapping pass, and the join values are incomplete

**The brief's words.**
- Line 27: "by their own terms, identifiers or definitions".
- Lines 28 and 33: "Mark the join as a reading, and cite both definitions".
- Line 66: "`cap_id` (`CM-<area>-nnn`; in the mapping pass, new ones only) · … · `join` (`match`, `terms`, `role, a reading`, or `single`) · `note`".

**The problem.**
- **Missing values.** The `join` values have none for a join on identifiers or on definitions, both of which line 27 allows. An agent writes `terms` for them, which is wrong, or invents a value.
- **Definitions have no column.** "Cite both definitions" has no column, so the checker can't test it.
- **Mapping-pass landings leave no trace.** In the mapping pass, `capabilities.tsv` holds new capabilities only, and `cells.tsv` has no `join` column. So the basis on which a WooCommerce, Zid or BigCommerce concern lands in an existing capability (a Q1 match, terms, identifiers or role) is recorded nowhere but `notes.md`. PLAN line 36 makes each join on role "a reading the coordinator checks". In the mapping pass that check has nothing to test. For Zid and BigCommerce, which Q1 never matched, every join is the mapping agent's own.

**The evidence.** Q1's own match bases: term 65, term+identifier 11, term+definition 8, definition 3, identifier 1 (script: the "Basis kind" phrase in `matches.tsv`'s `note`).

**Proposed fix.** Use `landings.tsv` (finding 4) for both passes:
- `join` takes `match:<M-id>`, `terms`, `identifier`, `definition`, `role` or `single`;
- `join_evidence` gives the cite ids of both sides' terms, identifiers or definitions;
- `role` is always a reading.

The checker tests that every `match:` id exists and holds the concern, and that `role` and `definition` rows have cite ids for both sides.

### 10. A shared term alone can join two different things

**The brief's words.** Line 27: "**Join** concerns that are the same thing on both platforms, by their own terms, identifiers or definitions." Line 33: "where it is the same thing by terms, identifiers or definitions".

**The problem.** The brief guards a join on role (different names, same role), but not the opposite case: the same word naming different things. Q1's own matching pass found 6 such cases. **Reading:** a join on terms alone is the easiest wrong join for an agent to make, and the mapping pass has no Q1 match to check against for Zid and BigCommerce.

**The evidence.**
- `matching-notes.md`, line 200: "The same word naming different things (6 rows)" (U-034, U-040, U-044, U-045, U-062, U-084).
- **Locations.** Shopify's `SH-C-024` "Locations" (inventory locations; INV) against WooCommerce's `WC-C-030` "Selling and shipping locations" (the countries a store sells to).
- **Subscriptions.** `WC-C-100` "Subscriptions (recurring billing)" against "WooCommerce.com subscriptions", the purchases of extensions (`WC-S-0900`, under `WC-C-050`), and Zid's `ZD-C-020` "Zid subscription plans and fees / الاشتراكات".

**Proposed fix.** Add a rule: a shared term joins only where the cited definitions or identifiers show the same object; the same term for different objects stays apart and is listed in `notes.md` with both definitions.

### 11. The unclear candidates have no column the brief names and no ruling to record

**The brief's words.** Line 20: "`matches.tsv` and `unclear-matches.tsv`, with their `note` columns".

**The problem.**
- **No `note` column.** `unclear-matches.tsv` has none: its columns are `candidate_id shopify salla woocommerce why_unclear what_would_settle_it`.
- **No ruling is asked for.** PLAN line 36 makes the 84 unclear candidates "engineering's to rule under the founder's intent". The brief asks for "every join on role" in `notes.md` (line 70), but not for a ruling on each candidate in the part's scope. A candidate kept apart leaves no trace, and the extent's report can't list it for the founder's veto (PLAN line 219).

**The evidence.** 21 unclear candidates touch a concern of domain B's scope (`U-001` to `U-005`, `U-013`, `U-015`, `U-016`, `U-019`, `U-020`, `U-057`, `U-059` to `U-063`, `U-070`, `U-072`, `U-078`, `U-081`, `U-082`; script). Some name a ruling that would settle them, for example `U-002` (Collections against Categories): "Founder ruling; or a Shopify source stating whether collections or its taxonomy categories correspond to a store's product categories."

**Proposed fix.** Name the right columns (`why_unclear`, `what_would_settle_it`). Each part writes `rulings.tsv`: `candidate_id · ruling (joined as <cap_id>, or kept apart) · basis · evidence`, one row for every unclear candidate any of whose concerns the part takes. The checker tests the coverage.

### 12. The dry run's parts are not small, and the brief gives no script for the mechanical reading

**The brief's words.**
- Line 17: "Shopify's and Salla's `concerns.tsv`, whole".
- Line 18: "your platform's `concerns.tsv`, whole, and the anchor's merged … `capabilities.tsv` and `cells.tsv`".
- Line 72: "**Size:** your message gives it."

PLAN lines 184 to 187: "each brief keeps an agent's context small: … large files are queried with scripts, not loaded whole; outputs are small, and mechanical steps are scripts."

**The problem.** The brief tells agents to load whole files and gives no script to pull a domain's rows, and the size it defers to the message is not stated anywhere. **Reading:** the anchor part for domain B is medium-sized if the agent reads its rows with scripts, and large if it loads what the brief says to read whole. The mapping pass, one platform per part across all domains, is large by the plan's own rule.

**The evidence (sizes).** These come from the script `sizes.py` in the scratchpad, over the concern sets the inspector reads as domain B's (a reading from concern names, since Q1 holds no area). The sets are:
- Shopify: core 10 (`SH-C-020` to `-025`, `-038`, `-186`, `-189`, `-190`), possible 12 more;
- Salla: core 10 (`SA-C-020` to `-026`, `-028`, `-029`, `-031`), possible 11 more;
- WooCommerce: core 5 (`WC-C-064`, `-066`, `-068`, `-100`, `-101`), possible 9 more;
- Zid: core 4, possible 6 more;
- BigCommerce: core 5, possible 8 more.

| Platform | Concerns (core / with possible) | Statements | Statement bytes | Inventory entries | Cite ids | Citation-row bytes |
| --- | --- | --- | --- | --- | --- | --- |
| Shopify | 10 / 22 | 196 / 312 | 67,923 / 110,465 | 251 / 383 | 468 / 730 | 137,509 / 222,993 |
| Salla | 10 / 21 | 203 / 375 | 86,037 / 155,474 | 196 / 349 | 198 / 368 | 81,319 / 149,650 |
| WooCommerce | 5 / 14 | 78 / 135 | 17,329 / 31,903 | 72 / 108 | 87 / 153 | 23,790 / 42,528 |
| Zid | 4 / 10 | 28 / 58 | 8,742 / 19,661 | 59 / 80 | 71 / 116 | 18,544 / 32,057 |
| BigCommerce | 5 / 13 | 28 / 61 | 6,553 / 14,817 | 74 / 114 | 35 / 69 | 10,356 / 20,119 |

- **The anchor part (domain B).** The files the brief says to read whole are Shopify's and Salla's `concerns.tsv` (61,597 and 66,464 bytes; 64% and 38% of them is the `inv_ids` column, which the part doesn't need), `matches.tsv` (46,252) and `unclear-matches.tsv` (33,928). With the in-scope statements and inventory entries, the part reads about 410,000 bytes on the core sets, or 545,000 with the possible concerns. With the citation rows it reads about 629,000, or 918,000. **Assumption:** at about 4 bytes a token, that is 100,000 to 230,000 tokens of context, re-read every turn.
- **The mapping part, one platform across all domains.** For WooCommerce: 118 concerns, 1,499 statements (388,587 bytes), `inventory.tsv` 53,297, `citations.tsv` 441,143. Then come the merged anchor files, which the brief says to read too.
  - **Assumption:** about 254 capabilities and 508 cells. That figure counts each of the 62 Shopify–Salla matches as one capability and every other concern as its own (198 + 152 concerns, of which 81 and 77 are in those matches).
  - Zid's statements are 223,647 bytes and BigCommerce's 111,984.

**Proposed fix.**
- **A slice script,** like `method/subject_slice.py`, that prints the part's in-scope rows compactly: concern id, concern, `platform_terms` and `split_note`; then each statement by its key (finding 8), with its identifier, its first 150 characters and its scope; then the cite ids' sources.
- **Run the mapping pass per platform and domain,** not per platform. The anchor's cells are read per domain through the same script.
- **State the part's size cap in the brief,** with the counts above as the expected scale.

### 13. Qualities lose their capability and scope, and slot fillers ask the agent to judge the kind

**The brief's words.**
- Line 53: "**Qualities:** a limit, a certification, an uptime or a data location a platform states."
- Line 54: "**Slot fillers:** a provider, partner or law a platform names as filling a slot."
- Line 68: `qualities.tsv`: "`area` · `platform` · `quality` · `value` · `evidence`".
- Line 69: `slot-fillers.tsv`: "`cap_id` · `platform` · `filler` · `market` · `evidence`".

**The problem.**
- **No capability, no scope.** A quality has an area but no capability and no scope. A limit that holds on one plan or store becomes the platform's limit: a wrong row, against line 59.
- **Slot fillers presuppose the kind.** "Filling a slot" presupposes that the agent knows the capability is a slot, which is the kind the coordinator computes later (PLAN line 216).
- **Unplaced limits are out of reach.** Q1 left some domain-B limits unplaced, outside any concern, and the brief's reading list doesn't reach them.

**The evidence.** `SH-I-2519` `maxProductOptions` and `SH-I-2520` `maxProductVariants` are store resource limits, and `SH-I-2594` `sellsSubscriptions` is a store feature. All are out of scope in Q1, "Unplaced: no Shopify source held ties this key to a concern" (`map/out-of-scope.tsv`). Of the 389 out-of-scope entries, 25 have domain-B words (script: a regex over `entry`).

**Proposed fix.**
- `qualities.tsv`: `cap_id · platform · quality · value · scope · evidence` (statement keys).
- Slot fillers: "a third party or law a statement names as doing the capability for the merchant or the platform", with no judgement of the kind.
- Name `map/out-of-scope.tsv` as read-only context, for its unplaced keys in the part's domain, cited by their inventory ids and never landed as concerns.

### 14. Cells carry no gaps, so a placement read from weak evidence looks like any other

**The brief's words.** Line 19 names `statements.tsv`, `inventory.tsv` and `citations.tsv`; `gaps.tsv` is not named anywhere in the brief.

**The problem.** PLAN line 353: "A gap stays visible, with the work that would close it." A cell's placement is read from the statements that exist. Where Q1's `where` or `responsible` placement is a gap, nothing in the cell says so, so a `core` read from a plan line alone looks like a `core` read from an admin route. The review is told to check every placement against all of Q1's statements (PLAN line 214), but not against the gaps.

**The evidence.** In domain B's scope:
- `SH-C-038` has a `where` gap ("observation needed");
- 19 of the 21 Salla concerns have `responsible` as "page not read" (`SA-C-124` has a statement; `SA-C-125` has "stated only in general terms"), and 14 of the 21 also have `reason` as "page not read";
- `ZD-C-101` Gifting has only a `where` row, with its other placements gaps;
- `BC-C-036` Wishlists likewise has only a `where` row.

Script: per concern, statements by placement and gaps with their kind.

**Proposed fix.** Add `gaps.tsv` to the reading list and a `gaps` column to `cells.tsv`, listing the Q1 placements of the cell's concerns that are gaps, with their kind (`where:observation needed`).

### 15. Optional: the commit for URL sources, and what reading more context may produce

**The brief's words.** Line 19: "`citations.tsv` for the commit each source was read at". Line 22: "the structures Q1's citations name, at the commit `citations.tsv` gives, where a statement needs more context."

**The problem.** `citations.tsv` gives a commit only for observed-sh and observed-sa sources. URL sources carry none, and the release carries a version, not a commit. Their copies are in this repository's `evidence/product-class/runs/*/manifest.tsv`, found by URL, and in `/home/user/woocommerce-release/11.2.1`; the brief names neither. The brief also doesn't say whether more context read from a structure may be cited. Line 58 implies it may not ("every cell cites Q1's ids").

**The evidence.** Every Zid citation (1,087) and every BigCommerce citation (481) is a URL. So are 581 of WooCommerce's 1,466, 1,001 of Shopify's 5,055 and 278 of Salla's 2,982. Script: classifying `source` by prefix.

**Proposed fix.** Name the two places. Say that context read beyond Q1's statements informs a reading and is never cited; a needed new statement goes in `notes.md` as a gap.

### 16. Optional: the sentence on permissions, topics, scopes and plan lines can be read as excluding concerns

**The brief's words.** Line 38: "staff permissions, webhook topics, access scopes and plan lines are evidence for a capability, not capabilities themselves."

**The problem.** Q1 has concerns that are those systems: `SH-C-010` Roles and permissions, `SH-C-015` Subscription plans, `SH-C-158` Access scopes granted to apps, `SH-C-162` Webhooks, `SA-C-191` App access scopes. Each must land once. **Reading:** the sentence means each permission, topic, scope or plan line, but read literally it would leave these concerns without a capability. It doesn't affect domain B.

**Proposed fix.** "Each permission, webhook topic, access scope or plan line is evidence for a capability. The platform's permission system, webhooks, scopes and plans are themselves capabilities, in their own areas."

### 17. Optional: smaller gaps in the output's conventions

- **Capability names.** `capability` has no naming rule. Named in one platform's word (for example "Collections"), it steers the mapping pass's "same thing by terms" toward that platform. **Reading:** use a term both platforms share, or both terms ("Collections / Categories"), and have the mapping compare against every cell's `terms`, not the name.
- **Numbering in the mapping pass.** Sequential mapping parts must continue each area's numbering; the brief doesn't say from where. The checker can catch collisions.
- **Small undefined points.** `<part>` in `studies/class-model/parts/<part>/` has no naming rule. Whether `area` is the `area_id` or the name, and whether `parent` must be in the same area, are not said.
- **Market-scoped capabilities.** Line 59, "No market's facts decide a capability or its area", can be read as dropping a capability shown only under one market's scope. **Reading:** say that such a capability stays, with its scope in its cells, and that a market's provider or law is a slot filler.

### 18. Optional: "placement" means two things, and the brief doesn't give Q1's meanings

**The brief's words.** Line 19: "the platform's `statements.tsv` rows under every placement". Line 42: "**Placement,** as your reading of those statements: `core` …".

**The problem.**
- **Two meanings of one word.** In Q1, `placement` is the question a statement answers: `where`, `decides`, `responsible`, `boundary` or `reason` (`Q1-concern-map.md`, lines 68 to 73 and 95). In the brief, it is the value `core`, `own service`, `extension point` or `outside`.
- **Q1's rules are out of the agent's reach.** An agent that reads only its brief and what it names (`CLAUDE.md`) never reads Q1's text. So it doesn't learn what the five placements mean, or that a statement's `note` may hold inference that "never counts" (Q1 rule 5).
- **The values are Q1's dropped ones.** The brief's four values are close to the fixed values Q1 dropped on 11 October because they were "our category names, not the platforms' words" (Q1 lines 55 to 63). **Reading:** as marked readings with per-value evidence (finding 7) they are legitimate, but the brief should say why they return.

**The evidence.** Domain B's scope holds 3 inference notes (script: "infer" in `note`):
- `WC-C-100`'s `note`: "Inference: as a premium extension, it runs only where the merchant has bought and installed …". It bears directly on the placement of subscriptions (finding 7).
- The other two are BigCommerce's, on plan lines. `BC-C-007`: "Inference: the line is included only on Performance." `BC-C-011`: "Inference: included from Scale up."

Carried into a cell's `scope` as "plan: Performance", they would present an inference as the platform's statement.

**Proposed fix.** Name the brief's column `placed_as`. Quote Q1's five placements and rule 5 in the brief, in two lines.


### 19. Optional: "read in full" is not what Q1 shows for Salla

*Found after inspection A was read, by a check of the brief's own line 6; inspection A doesn't raise it.*

**The brief's words.** Line 6: "Shopify and Salla are the deepest evidence: 3,005 and 2,560 statements, read in full."

**The problem.** The statement counts are right (`statements.tsv`: 3,005 and 2,560 rows). "Read in full", though, is either a claim about Q1 or an instruction, and the brief doesn't say which. As a claim it doesn't hold for Salla: most of Salla's gaps are pages Q1 did not read. As an instruction it contradicts line 17, which takes only the domain's concerns. **Reading:** read as a claim, it would lend Shopify's and Salla's "nothing held" cells a weight Q1 doesn't give them.

**The evidence.** Salla's `gaps.tsv`: 206 of 230 gaps are "page not read", 18 "stated only in general terms" and 6 "observation needed". Shopify's: 182 of 249 are "searched, not found". PLAN line 193 says Shopify and Salla are "read first and in full" in the subjects, which is a different step.

**Proposed fix.** "Shopify and Salla hold the most statements (3,005 and 2,560)", and nothing more.

## What the cells give the plan's kind-and-count rule

The rule (PLAN line 216) needs four things for every capability and platform:
1. whether the platform shows the capability;
2. whether its placement includes `core` or `own service`;
3. whether its placement is only `extension point` or `outside`;
4. for the slot test, the set of platforms that show the capability.

The brief rightly doesn't ask the agent to compute the kind. **Reading:** as specified, the cells don't give the coordinator these four things reliably:
- **Showing** has no fixed token (finding 6). Finding 4's "lands once" makes some cells falsely "nothing held". Capabilities added in the mapping pass have no cells for the platforms mapped before (finding 5), so the coordinator can't tell "not compared" from "nothing held".
- **Placement** is multi-valued with no separator (finding 8). It has no per-value evidence and no rule tying values to statements (finding 7). A forced choice therefore stands in for "no statement supports a placement".
- **The slot test** depends on what "another party" means. `outside` read from statements that make the merchant responsible (`SH-S-0676`) turns `core` evidence into slot evidence (finding 7).
- **Slot fillers** ask the agent to judge "a slot" before the kind is computed (finding 13).

With findings 4 to 8 fixed, the computation is mechanical:
- the count is the number of platforms whose `held` is `statements` and whose `placed_as` contains `core` or `own service`;
- the kind is `class` if the count is at least 1;
- the kind is `slot` if every platform whose `held` is `statements` has a non-empty `placed_as` made only of `extension point` and `outside`;
- otherwise the kind is `open`.

**Reading:** the plan's rule itself has no answer for `open`: a capability whose count is 0 and that some platform shows with `not stated`. This belongs to the dry run's review of the rule, which the plan allows ("The dry run's review may refine the rule").

## Inspection A's must-fix findings, against brief B

Inspection A (`studies/class-model/inspection-A.md`) inspected brief A at `95fd2916`, then re-inspected `A-assign.md` and an earlier `B-extent.md` at `79ae9c27`. The verdicts below are the inspector's own, against brief B as it stands at `93ebb15c`. They were made after this inspection's own findings were written, and changed none of them. After A was read, three things were added from separate checks, none of them taken from A: finding 19, the detail of `SH-C-186`'s `boundary` rows in finding 7, and the BigCommerce notes in finding 18. No verdict changed. "B line n" is the current brief. Inspection A's own statuses in its re-inspection table describe the earlier B and are not relied on.

### Findings 1 to 21 (those marked must fix)

| A's # | A's finding, in short | Brief B | Evidence |
| --- | --- | --- | --- |
| 1 | Placement from labels Q1 abandoned; none for Zid and BigCommerce | **Partly resolved** | `placements.tsv` is on no read list. Placement is "your reading of those statements" (B line 42), read from `statements.tsv` "under every placement" (B line 19), the same way for all five platforms. But the tests A asked for, which statement maps to which value, are absent (this inspection's finding 7). |
| 2 | The joining rule isn't Q1's; agents rule the founder's unclear list | **Partly resolved** | B lines 27 and 28 state Q1's test (terms, identifiers or definitions), and a join on role is a reading that cites both definitions. Who rules the unclear list is recorded: PLAN line 36, under the founder's intent of 29 October (`founder-decisions.tsv`). Still open: no per-join record in the mapping pass (finding 9); no precedence between a match and an unclear candidate holding the same concern; no ruling recorded for candidates kept apart (finding 11). |
| 3 | Zid and BigCommerce never matched; `single-platform.tsv` covers three | **Partly resolved** | `single-platform.tsv` is on no read list, and Zid and BigCommerce are joined by the same test (B line 33). But B never says `matches.tsv` covers three platforms (B line 20 sends every part to it). Their joins aren't recorded per join (finding 9), and their "nothing held" cells show no search (finding 6). |
| 4 | "Exactly one capability" against "the smallest unit"; no lower bound | **Partly resolved** | "Smallest unit" is gone (B line 26), and B line 38 sets the lower bound. The anchor's grain is left to the agent with `parent` (B line 29), as the coordinator's disposition chose. But "lands once" (B line 32) still fails for a coarser concern in the mapping pass, and "appears in a cell" (B line 60) and "lands once" are not the same test (finding 4). |
| 5 | Kinds don't cover `outside` or mixed placements; the vendor's own apps vary | **Partly resolved** | (a) The plan's rule (PLAN line 216) gives `slot` to any mix of `extension point` and `outside`, and "More than one may apply" (B line 48) lets a mixed cell count. Still uncovered: no statement supporting any value, and a count of 0 that is not a slot (finding 7; the section above). (b) `own service` now names "a … buyer app of its own" (B line 44). But a vendor's extension sold through its own marketplace still fits `own service` and `extension point` alike (`WC-C-100`, `WC-S-5351`), and B doesn't keep it apart as A asked. |
| 6 | The count is "own" only; `not shown` counts against less-read platforms | **Partly resolved** | "A platform Q1 holds nothing for is not counted as lacking it" (PLAN line 216), and "It never means the platform lacks it" (B line 50). The kind separates `slot` from `class`. Still open: `gaps.tsv` is on no read list (finding 14), and no evidence level is given per cell. It could be derived from cite ids by `method/source_kinds.py` if the cells give statement keys (finding 8). |
| 7 | The "Why" steers; the handoff is unrecorded; the slot rule differs | **Resolved** | B line 3 is neutral: "It records what the platforms do … It decides nothing about Sharrwah, ranks nothing". The founder's intent is recorded (`founder-decisions.tsv`, 29 October, two "Intent" rows), and PLAN carries Stage 4A (lines 204 to 224). B states no slot rule, and the kind is the coordinator's. |
| 8 | The seed's questions pre-answer an unclear candidate | **Resolved for the questions; partly for the groupings** | "Leave out the seed's questions" (B line 15; PLAN line 207). But the groupings are still called "labels" and decide the area (B lines 15 and 30), without being marked as uncited leads. They list gift cards and Gifting in two areas each (findings 1 and 2). |
| 9 | No rule for concerns spanning areas; the seed overlaps; parts can't reconcile | **Partly resolved** | Parts are now domains, so fewer boundaries, and the coordinator merges and checks that each concern lands once (PLAN line 215). Still open: no pre-assignment, no tie-break and no rule for spanning concerns, and the "left for another domain" list is free text (B line 60; finding 1). |
| 10 | `absent` has no basis the agent can see | **Partly resolved** | The safe default is in: "Q1 holds nothing … never means the platform lacks it" (B line 50). But absence still rests on Q1's `notes.md` (B line 21), which never calls a list complete and is a derived document (finding 6). |
| 11 | Finding aids instead of lists; no commits pinned | **Resolved for local sources** | The other-product-class pointer is gone. Structures are read "at the commit `citations.tsv` gives" (B line 22), and `citations.tsv` is on the read list (B line 19). The optional remainder is URL sources and the release, which `citations.tsv` gives no commit for (finding 15). |
| 12 | Statements have no ids; the example cites another concern | **Partly resolved** | A statement is "concern id, cite id and identifier" (B line 41), and there is no example to be wrong. But that key sits on more than one row for Shopify (119 rows), Salla (130) and WooCommerce (97). With Q1's `placement` added it is unique (finding 8). |
| 13 | `decides` in one column for five platforms | **Resolved** | No `decides` column. Cells are per platform (B line 40), and decision statements are evidence (B line 38) or scope (B line 49). |
| 14 | The market rule contradicts `world` | **Partly resolved** | Slot fillers have their own file with `cap_id` and `market` (B lines 54 and 69). Scope is kept, as stated (B lines 49 and 59). But scope is one per cell (finding 8). Nothing says that a market's law built into a platform's own core is a scoped `core` cell rather than a slot filler. "No market's facts decide a capability" (B line 59) can be read as dropping such a capability (finding 17). |
| 15 | Qualities as `class` capabilities | **Partly resolved** | Qualities have their own file (B lines 53 and 68). But it has no `cap_id` and no `scope`, and the unplaced limits (`maxProductVariants`, `maxProductOptions`) can't be reached (finding 13). |
| 16(a) | Excluding `note` columns hides the matching pass's warnings | **Partly resolved** | `matches.tsv`'s `note` is read (B line 20). But the README's flags on `M-064` and `M-070` aren't in their notes (`M-064`: "Basis kind: term. Each is the platform's own chat with customers."), and B line 27 makes every match a join. Neither match is in domain B, so the dry run isn't affected. |
| 17 | Output cells can't be checked; no protocol for parallel parts | **Partly resolved** | Per-part folders and the coordinator's merge (B lines 11 and 63) settle the protocol, and cells are per capability and platform with separate columns (B line 67). Still uncheckable: list separators, the "nothing held" token, the complete-list column and the statement key (findings 6 and 8). |
| 19(a), (b) | No plan gating or evidence level per cell | **(a) Deferred; (b) not resolved** | (a) The coordinator's disposition defers plan gating to each area's detail. B keeps a plan only as a statement's scope (B line 49). (b) B has no evidence level. It is derivable from the cite ids (finding 8's statement keys and `method/source_kinds.py`). |

### The re-inspection's new problems N1 to N12 (all marked must fix)

These were raised against `A-assign.md` and the earlier B. Brief B replaced both, so several are moot. The verdicts are against B as it stands.

| A's # | In short | Brief B | Evidence |
| --- | --- | --- | --- |
| N1 | The merge between parts is unspecified | **Partly resolved** | One brief, parts in `parts/<part>/`, and the coordinator merges and checks that each concern lands once (B lines 11 and 63; PLAN line 215). Still unspecified: who settles a concern two anchor parts take (finding 1), and how earlier mapping parts' capabilities enter the model a later part maps onto (finding 5). |
| N2 | Part 1 split by platform can't apply the matched-concerns rule | **Resolved (moot)** | No part 1. The anchor reads Shopify and Salla together, with `matches.tsv` (B lines 17 and 20). |
| N3 | Assigning by where the platform puts it scatters matched groups and moves slots into APP | **Not resolved** | B line 30 assigns the area by "where the two platforms put it", with no tie-break, and the disposition leaves it to judgment. In domain B, five Shopify concerns are placed only through the app store (script over `where` rows): `SH-C-185`, `SH-C-187`, `SH-C-189` ("Custom product apps", the only `where` row), `SH-C-202` and `SH-C-154`. Salla puts options under Products (`SA-C-021`: the dashboard link "Categories & options", `/products/options`). By B line 30, `SH-C-189` could go to APP while its counterpart goes to CAT. |
| N4 | Zid's and BigCommerce's joins limited to part 1's area | **Resolved** | The mapping part reads the whole merged anchor (B line 18), so a Zid concern can meet any capability. **Note:** this inspection's finding 12 proposes splitting the mapping pass per domain for size. That split must keep N4 resolved: the scope file (finding 1) assigns each Zid and BigCommerce concern before the mapping, and a mapping part may still search other domains' capabilities by script. |
| N5 | A concern under `also_in` has no owner | **Partly resolved** | No `also_in`, and "lands once" holds. But who owns a concern that spans domains has no rule (finding 1). |
| N6 | What part 1 reads about lists never reaches part 2 | **Partly resolved** | The agent now reads `notes.md` itself (B line 21). But the notes don't call any list complete (finding 6). |
| N7 | `not shown` mixes "no concern" with "a concern with no `where` row" | **Partly resolved** | "Q1 holds nothing" (B line 50) means no statements, not no `where` row. But B gives no value for a platform that shows the capability with no statement supporting a placement (finding 7; `SH-C-038` has no `where` row). |
| N8 | `not shown` on Zid or BigCommerce implied absence elsewhere | **Resolved** | B line 50 holds for every platform: "It never means the platform lacks it." |
| N9 | `plan_gated: yes` fires on any named entitlement | **Resolved (moot)** | No `plan_gated`. Plan gating waits for each area's detail (the disposition). |
| N10 | The `reading` column has no meaning left | **Partly resolved** | B line 67: "`reading` (what in the cell is a reading)", and the join's reading is in `join` ("`role, a reading`"). But in the mapping pass no column records the join (finding 9), and `reading` is free text a checker can only test for being non-empty. |
| N11 | No column ties concerns to capabilities; no coverage rule | **Partly resolved** | `concern_ids` is a cell column (B line 67), and "Every concern you take appears in a cell" (B line 60). But what a part "takes" is undefined (finding 1), and "lands once" can't be tested from cells alone (finding 4). |
| N12 | Areas beyond the references can absorb concerns | **Partly resolved** | PLAN line 215: "H, beyond the references, takes no capabilities". B doesn't say so, and its agents read `km-areas.tsv`, which lists WLD, ENG, INT and MTH (finding 2). |

## Tests a checker for this brief's output should run

Some tests depend on the fixes above. They are marked with the finding they need. A checker can be written before the dry run; the dry run's review then adds what it finds (PLAN line 214).

**Form**
1. Every output file exists in `studies/class-model/parts/<part>/`, with the header exactly as the brief gives it. Every row has the header's number of fields; there is no quoting and no empty required field.
2. Multi-valued fields use the one fixed separator, and every token is from its field's value set: `placed_as`, `held`, `join` and `platform` (finding 8).
3. `cap_id` matches `^CM-[A-Z]{3}-\d{3}$`. Its area equals the `area` column, which is an `area_id` of the part's domain and never of domain H. `cap_id`s are unique across the merged model, and a mapping part's are new and numbered past the model's highest in each area.
4. `parent` is empty or an existing `cap_id`, with no cycles.

**Coverage**
5. Every concern `scope.tsv` gives the part appears exactly once in `landings.tsv` (findings 1 and 4), and no concern outside the scope does. Across merged parts, every concern of all five platforms lands exactly once.
6. Every landed concern appears in the `concern_ids` of a cell of the capability it lands in, for its platform.
7. `cells.tsv` has exactly one row per capability and platform, for every capability in scope and every platform the pass covers. After the back-fill, this holds for all five (finding 5).
8. Every unclear candidate any of whose concerns the part takes has a row in `rulings.tsv` (finding 11).

**Evidence**
9. Every concern id exists in its platform's `concerns.tsv` and carries the platform's prefix.
10. Every statement key `concern_id|placement|cite_id` exists in that platform's `statements.tsv` (finding 8). Its identifier, where quoted, equals the row's `identifier`. A key whose concern is not in the cell's `concern_ids` is named in `reading` (finding 4).
11. Every cite id exists in `citations.tsv` and resolves:
    - a local source with `git cat-file -e <commit>:<path>`;
    - a release path by sha256 against `evidence/product-class/woocommerce-11.2.1/files.tsv`;
    - a URL by URL in a capture run's `manifest.tsv`.

    The quote test is `method/quote_check.py`'s, as the concern map's checker uses it.
12. Every string in `terms` occurs verbatim in a cited statement's `identifier` or `statement`, or in the concern's `platform_terms`.
13. Every scope given with a statement key equals that statement's `scope`. A cited statement with a non-empty `scope` has it carried (finding 8).
14. `where` cites only keys whose Q1 placement is `where`, or names the exception in `reading`.

**Values and readings**
15. Every `placed_as` value carries at least one statement key. `held` set to `none held` comes with an empty `placed_as`, and `held` set to `statements` with at least one value or `not stated` (findings 6 and 7).
16. For `none held`, the search terms and languages are present. The checker re-runs them over the platform's whole `statements.tsv` and fails the cell if any statement matches (findings 4 and 6).
17. `absent from a published complete list` cites the platform's own list by cite id and a `method/corpus_search.py` run (finding 6), or the value is refused.
18. Every `landings.tsv` row with `join` set to `match:<M-id>` names an existing match that holds the concern. A `role` or `definition` row cites both sides' statements (finding 9).
19. Every `reading` is non-empty where `placed_as` is set, since a placement is always a reading.
20. Flags for the reviewer, not failures:
    - `own service` whose cited statements don't name the platform's company;
    - `outside` whose cited statements name only the merchant or buyer;
    - `core` resting only on `boundary` keys (finding 7).

**Side files**
21. `qualities.tsv` and `slot-fillers.tsv`: the `cap_id` exists. Every evidence key exists, and its scope is carried. A slot filler's `market` is set wherever its statement's scope names a country (finding 13).
22. `gaps`, where added (finding 14), equals Q1's `gaps.tsv` for the cell's concerns. The script can fill it, and the checker compares.

**Kind-readiness, after the merge**
23. Every cell parses into `held` and a set of `placed_as` values. The coordinator's computation runs on every capability and lists those whose kind is `open` (the section above).
24. The merged model holds no two capabilities whose cells cite the same statement key, unless one is the other's `parent` or `reading` names the split.
25. Every Q1 match's concerns land in one capability, or in a parent and its children, unless the split is named with its grain reason (finding 4).

## The coordinator's check and rulings (30 October 2026)

**The check.** I re-ran the inspection's central counts against the concern map at `93ebb15c`:
- `concerns.tsv` has no area or domain column on any platform;
- `M-011`, `M-013` and `M-074` hold what finding 4 and finding 1 say;
- `unclear-matches.tsv` has no `note` column;
- 71 of WooCommerce's 118 concerns are in a Q1 match with Shopify or Salla;
- the key (`concern_id`, `cite_ids`, `identifier`) repeats on 119, 130 and 97 rows;
- `WC-C-064`'s `where` rows include Categories, Tags, Brands and Attributes;
- `SH-S-0676` says the merchant is "legally responsible" for gift cards;
- `maxProductOptions`, `maxProductVariants` and `sellsSubscriptions` are unplaced in `map/out-of-scope.tsv`;
- Salla's gaps are 206 "page not read" of 230;
- `matching-notes.md` line 200 lists the six homonym rows.

Every one holds.

**One refinement, to finding 8.** A key of concern id, placement and *first* cite id is unique on every platform. Script: over each `statements.tsv`, the first id of `cite_ids`, split on `;` or a space. Shopify's `cite_ids` lists ids with `;`, and WooCommerce's 18 multi-cite rows with a space. So the key is `concern_id/placement/first_cite_id`, written with `/`, which no id or placement contains. The slice script prints it.

**Rulings.** Every finding is taken, the optional ones too, because each is cheap and each closes a way to a wrong row. Each is engineering's method ruling, listed at the next report.

| # | Ruling |
| --- | --- |
| 1 | A scope step runs before any part. It produces `studies/class-model/scope.tsv`: every concern of all five platforms in exactly one domain, A to G, with the other domains it also touches. A Q1 match's concerns share a domain unless the split is named. Its rows are readings, checked by the coordinator. A part takes its domain's concerns, and may cite statements of concerns from other domains that name it under `also`, without landing them |
| 2 | The area is what the capability is about, with the seed's labels as leads. The channel it is delivered through never sets it: an app-store category doesn't make a capability APP's. Never domain H (this also settles N3) |
| 3 | A mapping part is one platform and one domain, and takes that platform's concerns `scope.tsv` gives the domain |
| 4 | `landings.tsv` records each concern's landing, exactly once. A cell may cite statements of concerns landed elsewhere. A coarser concern lands on the parent capability, and the children's cells cite its statements. A Q1 match with several concerns on a side is a difference of grain, not one capability |
| 5 | A mapping part maps onto the domain's model so far: the anchor and every earlier mapping part. After a domain's mapping parts, a back-fill part writes the cells still missing, for every capability and platform |
| 6 | `held` takes `statements` or `none-held`. A `none-held` cell records the terms it searched, in each language, and the checker re-runs the search and lists what matches for the reviewer. Absence from a complete list is not recorded in this pass: the kind-and-count rule doesn't use it, and Q1's notes are never its basis |
| 7 | The placement tests go into the brief, and each value rests on statement keys in `evidence.tsv`, one row per statement. Three cases are settled: a product the platform's company makes is `own-service`, whatever channel sells it; an API that apps use to do the work supports `extension-point`; a merchant's or buyer's responsibility is never `outside`. A platform that shows the capability with no placement supported is `not-stated`, derived when no evidence row carries a placement |
| 8 | The list separator is `;`. Fixed tokens are hyphenated. The statement key is as refined above. Scopes and gaps are derived by script from the keys, not written by the agent |
| 9 | `landings.tsv` carries `join`: `match:<M-id>`, `terms`, `identifier`, `definition`, `role` or `single`, with `join_evidence` keys for both sides. `role` is always a reading |
| 10 | A shared term joins only where the cited definitions or identifiers show the same object. Homonyms stay apart, listed in the notes with both sides' keys |
| 11 | The unclear list's columns are named correctly. `rulings.tsv` gives a ruling on every candidate any of whose concerns the part takes. These rulings come to the founder's veto with the extent's report |
| 12 | `method/class_slice.py` prints a part's rows compactly, and searches a platform's statements. No file is loaded whole. Parts are one domain, and one domain and platform in the mapping pass. The brief states the expected size |
| 13 | `qualities.tsv` takes `cap_id`. A slot filler is a named third party or law, with no judgement of kind. Scope comes from the keys. `map/out-of-scope.tsv`'s unplaced entries are readable through the script, cited by inventory id, and never landed |
| 14 | The gaps on a cell's concerns are derived by script into the merged cells and shown to the reviewer |
| 15 | Copies of URL sources are in the capture runs' manifests, and the release is at its checked path. Context read beyond Q1's statements informs a reading and is never cited. A statement that is needed but not held goes in the notes as a gap |
| 16 | The sentence on permissions, topics, scopes and plan lines is reworded as proposed |
| 17 | The capability's name uses both platforms' terms, or a neutral term that names both. The mapping compares against the cells' terms, not the name. Numbering continues past the highest in each area. Parts are named `<domain>-anchor`, `<domain>-<platform>` and `<domain>-backfill`. `area` is the `area_id`, and `parent` is in the same domain. A capability shown under one market's scope stays, with that scope |
| 18 | The column is `supports`, in `evidence.tsv`. The brief quotes Q1's five placements and its rule 5, and says why the four values return: as marked readings with per-statement evidence, not as Q1's category labels |
| 19 | Line 6 says only that Shopify and Salla hold the most statements |

**The kind's `open` case** (a count of 0, with some platform `not-stated`) is computed and listed by the coordinator. The dry run's review rules on it, as the plan allows.

**A checker now, not after the dry run.** A first `method/check_class_part.py` runs the form, coverage and evidence tests (1 to 19 and 21) before the dry run, so each part checks itself before it hands back. The review adds what it finds.

**Re-inspection.** The brief's change is large, so the same inspector re-reads the changed brief and the scripts before anything runs.

## Re-inspection (30 October)

Status: complete (30 October 2026).

**Summary.** Of the 19 findings, 17 are resolved. Two are resolved in the brief, while the checker's tests for them misfire: 7 (R5) and 9 (R1, R4). The fixes bring 16 new problems:
- 7 to fix before the dry run, each a few lines of the checker or a sentence of the brief;
- 4 to settle before domain B's later mapping parts or a second domain;
- 5 optional.

| # | Finding | Verdict |
| --- | --- | --- |
| 1 | No rule for which concerns are a domain's | resolved |
| 2 | The area rule assumed the seed's areas | resolved |
| 3 | The dry run's mapping part had no domain | resolved |
| 4 | "Lands once" against coarser concerns; false "nothing held" | resolved (optional remainder: R14) |
| 5 | Mapping onto the anchor only; no cells for earlier platforms | resolved (new problem: R3) |
| 6 | No token for "nothing held"; absence from `notes.md` | resolved |
| 7 | Placement values with no tests | resolved in the brief; the checker's flags misfire (R5) |
| 8 | Cells not checkable | resolved |
| 9 | Joins not recorded in the mapping pass | resolved in the brief; checker gaps (R1, R4) |
| 10 | A shared term joining different things | resolved |
| 11 | No `note` column; no rulings | resolved; a ruling isn't tested against the landings (R9) |
| 12 | Parts not small; no slice script | resolved for the dry run; not for domain C (R10) |
| 13 | Qualities without capability or scope | resolved (optional remainder: R11) |
| 14 | No gaps in cells | resolved |
| 15 | Commits for URL sources; citing extra context | resolved |
| 16 | The permissions sentence | resolved |
| 17 | Smaller conventions | resolved |
| 18 | "Placement" with two meanings | resolved |
| 19 | "Read in full" | resolved |
| R1 | The checker crashes on a key with an unknown prefix, printing only that key | before the dry run |
| R2 | Problems in an earlier part are reported as the current part's | before the dry run |
| R3 | One back-fill per domain, while the dry run runs it after WooCommerce alone | before the full run |
| R4 | A `match:` landing isn't tested against where the match's other concerns landed | before the dry run |
| R5 | The safety flags on placements miss their cases: (a) `core` on `boundary` is silenced by a `shows` row; (b) `own-service` passes any statement naming the platform | (a) before the dry run; (b) optional |
| R6 | Any statement can be cited in any cell, so one can support capabilities in two domains | before the full run |
| R7 | A move breaks the moving part's re-check; no procedure for a concern moved into a domain already run | before the full run |
| R8 | The scope part reads no Q1 matches, though its rule needs them, and naming the match clears any split | before the dry run |
| R9 | A ruling isn't tested against the landings: `apart` passed for a candidate the part joined | before the dry run |
| R10 | The size line fails beyond domain B (Shopify's checkout-to-tax and shipping concerns: 73, with 1,063 statements) | before the full run |
| R11 | Qualities: scopes not derived; unplaced limits have no citable value | optional |
| R12 | "Domain F holds … its APIs" can pull a feature's API out of its subject's domain | before the dry run |
| R13 | Small inconsistencies (`not stated` and `not-stated`, lenient separators, `model` reading the running part) | optional |
| R14 | A `none-held` search is only as good as its terms | optional |
| R15 | The back-fill must write files the brief doesn't mention | optional |
| R16 | Where the merge lives | optional |

**What this is.** The same inspector re-reads brief B as rewritten at `92ec26fd`, with its two new scripts, `method/class_slice.py` and `method/check_class_part.py`. For each of the 19 findings above, it says whether the rewrite resolves it. It looks for new problems the fixes brought in, and it runs the scripts on domain B's concerns and on a synthetic part built in the scratchpad. As before, every judgement is a **Reading**, and every count comes from a script that was run.

**Read, at `92ec26fd`:**
- the brief, whole;
- both scripts, whole;
- the coordinator's check and rulings above;
- `method/README.md`'s two new rows.

The concern map, the seed and Q1 are unchanged since `93ebb15c` (`git diff 93ebb15c 92ec26fd` touches only the brief, the two scripts, `method/README.md`, `PLAN.md`, `STATE.md`, `founder-decisions.tsv`, a founder message and this file).

**Run, in the scratchpad** (`reinsp/` under the inspector's scratchpad, with `CLASS_MODEL_DIR` set to `reinsp/model`, a copy of `studies/class-model/seed`):
- every `class_slice.py` command, on real domain-B concerns;
- `check_class_part.py` on four inputs:
  - a synthetic `scope.tsv` for all 652 concerns, written by a keyword script (`tools/mkscope.py`). It is a test fixture, not a reading of the domains: the inspector's domain-B sets are forced to B, and everything else is assigned by keywords;
  - a synthetic `B-anchor` part (`tools/mkpart.py`): 17 capabilities, 27 landings (2 of them `moved:D`), 34 cells, 72 evidence rows, all on real statement keys;
  - a synthetic `B-woocommerce` part: 2 new capabilities, 8 landings, 19 cells;
  - a synthetic `B-backfill` part: 4 cells;
- 14 faulty copies of these, most with one fault, to see whether the checker catches it.

### The 19 findings, against the rewrite

| # | Finding, in short | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | No rule for which concerns are a domain's | **Resolved** | A scope part writes `scope.tsv`, one domain per concern, with `also` and the match rule (brief lines 6 and 43 to 51). The checker refuses domain H, a duplicate row, a missing concern, an `also` naming the row's own domain, an empty reason, and a split match whose reason doesn't name it. Each was tested on a faulty copy. New problems from the fix: R6, R7 and R8. |
| 2 | The area rule assumed the seed's areas | **Resolved** | "The area is the `area_id` of your domain that the capability is about … The channel never sets it" (line 64); "Domain H takes nothing" (line 48). The checker tests that the area belongs to the domain and that the `cap_id` carries it (`check_class_part.py` lines 166 to 169). |
| 3 | The dry run's mapping part had no domain | **Resolved** | A mapping part is one platform and one domain (lines 12 and 75). The checker takes only the concerns `scope.tsv` gives that domain and refuses any other landing (lines 187 and 196). Tested: the synthetic `B-woocommerce` lands its 8 domain-B concerns and nothing else. |
| 4 | "Lands once" against coarser concerns; false "nothing held" | **Resolved** | `landings.tsv` lands each concern exactly once (checker lines 198 and 236). Cells may cite statements of concerns landed elsewhere (line 67), a coarser concern lands on the parent (line 67), and a match with several concerns on a side is a difference of grain (line 61). `none-held` must record its search terms, and the checker re-runs them. Tested: the synthetic Brands cell searched "brand;vendor;علامة تجارية" and was flagged with 9 Shopify hits. Remainder, optional: R14. |
| 5 | Mapping onto the anchor only; no cells for earlier platforms | **Resolved** | "The domain's model so far: the anchor and every earlier mapping part" (line 75; checker lines 130 and 131). A back-fill writes the missing cells (lines 80 to 82; checker line 319). `fit` carries `strained` (line 114). Tested: the back-fill was asked for exactly the Shopify and Salla cells of `B-woocommerce`'s two new capabilities. With one of the 4 removed, the check named that cell and no other. New problem from the fix: R3. |
| 6 | No token for "nothing held"; absence from `notes.md` | **Resolved** | `held` is `statements` or `none-held` (line 115). Absence from a complete list is no longer recorded, and `none-held` "never means the platform lacks the capability" (line 86). |
| 7 | Placement values with no tests | **Resolved in the brief; the checker's flags misfire** | The tests are at lines 88 to 95. They settle the platform's own extension (`own-service`), the API apps use (`extension-point`) and the merchant's responsibility (`shows`). `not-stated` is derived. Both of the checker's safety flags miss the case they were added for (R5). |
| 8 | Cells not checkable | **Resolved** | The separator is `;` and tokens are hyphenated (line 112). The key `concern_id/placement/first_cite_id` repeats on no row of any platform: 3,005, 2,560, 1,499, 654 and 473 rows give as many keys (script over each `statements.tsv`). Scopes are derived per key into `derived.tsv`, for example `SA-C-020/decides/SA-S-1949=plan: سلة بلس`. Terms are tested against the cited statements. |
| 9 | Joins not recorded in the mapping pass | **Resolved in the brief; two checker gaps** | `landings.tsv` carries `join` and `join_evidence` in every part (line 114). The checker tests that a match exists and holds the concern, and that other joins cite both sides. But it crashes on a key with an unknown prefix (R1). Nor does it test that a `match:` landing's capability holds any of the match's other concerns (R4). |
| 10 | A shared term joining different things | **Resolved** | Line 59 cites Q1's list of the six homonym cases. Remainder, optional: the brief says never to load the concern map's files whole, and the script has no command for `matching-notes.md` (R13). |
| 11 | No `note` column; no rulings | **Resolved; one checker gap** | The columns are named (line 28), and `rulings.tsv` holds a ruling on every candidate that holds a landed concern. The checker tests coverage: removing `U-002`'s ruling gave "no ruling on U-002". But it doesn't test a ruling against the landings (R9). |
| 12 | Parts not small; no slice script | **Resolved for the dry run** | Measured with `class_slice.py`: the scope part prints 153,822 bytes. `B-anchor` prints 46,660 bytes of Shopify statements for 14 concerns, 59,852 of Salla's for 13, and about 7,900 bytes of matches each. `B-woocommerce` prints 12,565 bytes for 8 concerns. Remainder, before the full run: the brief's size line doesn't hold for domain C (R10). |
| 13 | Qualities without capability or scope; slot fillers judged a kind | **Resolved, with remainders** | `qualities.tsv` takes `cap_id` (line 117). A slot filler involves no judgement of kind (line 101). Remainders, optional: qualities' scopes aren't derived, and an unplaced entry has no citable value (R11). |
| 14 | No gaps in cells | **Resolved** | `derived.tsv` lists the gaps on each cell's cited concerns, for example `SH-C-038/where:observation needed`. |
| 15 | Commits for URL sources; citing extra context | **Resolved** | Line 41. |
| 16 | The sentence on permissions read as excluding concerns | **Resolved** | Line 62. |
| 17 | Smaller conventions | **Resolved** | Names (line 63), numbering (lines 65 and 76; the checker tests "numbered past the model's highest"), part names (line 12; the checker refuses others), `area_id` and same-domain `parent` (line 113), market-scoped capabilities (line 64). |
| 18 | "Placement" with two meanings | **Resolved** | Q1's five placements and its rule 5 are quoted (lines 18 to 25), and the column is `supports` (line 116). `class_slice.py` marks an inference note, for example `WC-C-100/decides/WC-S-5351 … [note: inference]`. |
| 19 | "Read in full" | **Resolved** | Line 8. |

### What the scripts did

**`class_slice.py`.** Every command works as the brief describes:
- `seed`;
- `concerns`, with `--all --where`, and with `--domain` from `scope.tsv`. A concern another domain lists under `also` is shown as "read-only: cite, never land";
- `statements`, `key`, `matches`, `gaps`, `outscope` and `model`. `key` answers `NOT FOUND` for an unknown key;
- `search`. It ignores case and Arabic hamza: "الاقسام" and "الأقسام" both find Salla's 2 statements. It matches substrings, so a short term casts wide: "tag" finds 96 Shopify statements.

`model` prints the domain's capabilities, landings and cells compactly: 4,823 bytes for the fixture's 19 capabilities.

**`check_class_part.py`.**
- **Clean inputs.** The synthetic scope passes with 0 problems once every split match is named. The same keyword assignment, before the reasons were edited, gave 53 problems. The synthetic `B-anchor` and `B-woocommerce` pass with 0 problems.
- **Faults it catches:** a missing ruling, a cell with no evidence, a landed concern its cell doesn't cite, a term not found in a statement, an `also` concern landed, `none-held` terms that match statements (a flag), and `core` resting only on `boundary` statements (a flag).
- **What it misses or mishandles:** R1 to R5, R7 and R9 below.

### New problems

The repository moved again during the re-inspection, to `b460d54b`: the founder's answers of 30 October, and `PLAN.md`'s Stage 4A rewritten to describe this method. `git diff 92ec26fd HEAD` shows no change to the brief, the scripts, `studies/concern-map/` or the seed. Line numbers are the brief's and the scripts' at `92ec26fd`.

**Verdicts.** "Before the dry run" means a cheap fix the dry run should have. "Before the full run" means a decision needed before domain B's Zid and BigCommerce parts, or before a second domain. "Optional" means it doesn't make wrong rows.

#### R1. The checker crashes on a key with an unknown prefix (before the dry run)

**Where.** `check_class_part.py` line 222 (`join_evidence`), line 340 (qualities and slot fillers) and line 362 (rulings) call `platform_of()`. That function calls `sys.exit` on an unknown prefix (`class_slice.py` line 64); only `evidence.tsv` catches the exit (line 265).

**Problem.** One stray match id, candidate id or `cap_id` in a key column stops the whole check. The run prints a single line, with no file or line number and none of the other problems. It also leaves any earlier `derived.tsv` in place, now stale.

**Evidence.** Tested on faulty copies: `M-011;U-059` in a `join_evidence` printed only "unknown platform prefix: M-011", with exit 1. `CM-CAT-003` in a ruling's `keys` printed only "unknown platform prefix: CM-CAT-003".

**Fix.** Catch the exit at every call, and report "`<file>` line n: `<token>` is not a statement key", as `evidence.tsv` already does.

#### R2. Problems in an earlier part are reported as the current part's (before the dry run)

**Where.** `load_part()` checks every earlier part's files with `table()` (lines 47 to 64 and 136), and its messages carry no part name.

**Problem.** Checking `B-woocommerce` reports faults in `B-anchor` as if they were `B-woocommerce`'s. Its agent is told to "fix every problem it prints" and to "write only your part's files", so it can do neither. This is likely in the dry run, since the review may correct `B-anchor` after its check. Nor does the checker ask whether an earlier part passed its own check; it trusts any folder that exists.

**Evidence.** Two faulty copies, each checked as `B-woocommerce`:
- `B-anchor/qualities.tsv` deleted: the check printed "PROBLEM qualities.tsv: missing";
- a 3-field row added to `B-anchor/capabilities.tsv`: it printed "PROBLEM capabilities.tsv line 19: 3 fields, header has 5". `B-woocommerce`'s own `capabilities.tsv` has 3 lines.

**Fix.** Prefix every message with its part's folder. Report an earlier part's fault as "`B-anchor` doesn't pass its check; re-run the check on it".

#### R3. One back-fill per domain, but the dry run runs it after WooCommerce alone (before the full run)

**Where.**
- Brief lines 7 to 10: "the back-fill", once per domain, after the mapping parts.
- `PART_ORDER` (`class_slice.py` line 41) ends with one `backfill`.
- The checker's back-fill needs cells for "platforms already mapped": every mapping folder that exists (lines 152 and 319).

**Problem.** The dry run is scope, `B-anchor`, `B-woocommerce`, `B-backfill`. When `B-zid` and `B-bigcommerce` run later, their new capabilities need a back-fill too, and `B-backfill` already exists. The brief doesn't say whether that part is reopened, extended or replaced. Its re-check fails until someone edits another run's files.

The back-fill also accepts cells for a platform not yet mapped (line 249 lets a back-fill write any platform's cell). The later Zid part then writes the same cell again, and its check doesn't see the duplicate, since `B-backfill` isn't among Zid's earlier parts.

**Evidence.** Tested: a `B-zid` folder with one new capability was added after the synthetic `B-backfill`. Re-checking `B-backfill` then demanded every capability's Zid cell ("no cell for CM-CAT-001 and zid", and so on, 20 times, in this fixture where the Zid part wrote no cells).

**Fix.** Either one back-fill after each mapping part, named for it (`B-backfill-woocommerce`), checked against the parts before it; or one back-fill per domain, after all three mapping parts, with the dry run's back-fill a one-off named as such. Refuse back-fill cells for platforms not yet mapped.

#### R4. A `match:` landing isn't tested against where the match's other concerns landed (before the dry run)

**Where.** Lines 212 to 218 test only that the match exists and holds the concern.

**Problem.** A concern can land "by Q1's match" in a capability where none of the match's other concerns landed. The join's stated basis is then false, and the checker is silent. This matters most in the mapping parts, where WooCommerce lands by match on the anchor's capabilities.

**Evidence.** Tested: `WC-C-064` landed `match:M-011` in `CM-INV-003` (inventory transfers), where none of `M-011`'s concerns landed. The check gave "0 problems, 0 flags".

**Fix.** Test that the capability, its parent or one of its children holds another of the match's concerns, in the model so far or in this part. Otherwise `match:` is a problem. Also test the reverse at the merge: a match's concerns spread over unrelated capabilities is flagged.

#### R5. The two safety flags on placements miss their cases (a: before the dry run; b: optional)

**Where.** Line 298: "core rests only on boundary statements" fires only when every evidence row of the cell is `core` and every statement is `boundary`. Lines 277 and 278: the `own-service` flag fires only when the statement doesn't match the platform's name (`COMPANY`, lines 34 and 35).

**Problem.**
- **(a)** One `shows` row on any statement silences the `core` flag, though `core` still rests only on `boundary` statements. That is the case finding 7 was about (`SH-C-186`'s scopes and topics), and an agent that also cites a `where` row for the terms writes exactly that cell.
- **(b)** The `own-service` flag passes any statement that names the platform. The brief's test is that the statement names the company "as the maker or provider", and a statement can name the platform without naming any maker.

**Evidence.**
- **(a)** Tested: `CM-SEL-002`'s Shopify cell had `core` on two `boundary` rows of `SH-C-186`, plus a `shows` row on its `where` row. The check gave no flag and derived `core`. Without the `shows` row, the flag fired.
- **(b)** The flag's pattern matches 1,051 of Shopify's 3,005 statements, 633 of Salla's 2,560, 748 of WooCommerce's 1,499, 222 of Zid's 654 and 93 of BigCommerce's 473 (script). Tested: `own-service` on `WC-C-100/decides/WC-S-5351`, "WooCommerce Subscriptions is a premium extension …", which names no maker, raised no flag. On `WC-C-104/where/WC-S-0702`, "Merchandising", it did.

**Fix.**
- **(a)** Test the statements that carry `core`: flag when all of them are `boundary`.
- **(b)** Flag every `own-service` row for the reviewer, since they are few and they decide the kind. Or require `why` to quote the maker phrase, and test that the quote occurs in the statement.

#### R6. Any statement can be cited in any cell, so one statement can support capabilities in two domains (before the full run)

**Where.**
- The brief says a part "may cite" the concerns of other domains that name it under `also` (lines 34 and 46).
- It also says "A cell may cite statements of a concern landed elsewhere" (line 67), and that `none-held` and the back-fill search "the platform's statements" (lines 69 and 82), which returns statements of every concern.
- The checker tests that a key exists and is the cell's platform's (lines 264 to 273), not which concern or domain it comes from.

**Problem.** The `also` restriction is neither enforced nor consistent with the search instructions. One Salla statement can back a `core` cell in domain B and another in domain C. Each capability's kind is computed on its own, so the same evidence counts twice. Nothing across domains checks it.

**Evidence.** Tested: `B-anchor`'s `CM-SEL-002` Salla cell cited `SA-C-125/where/SA-S-1173`. In the fixture `SA-C-125` is in domain F and doesn't name B under `also`. The check gave 0 problems, and `derived.tsv` gave the cell `core` ("Recurring Payments API").

**Fix.** Say what a cell may cite: its own domain's concerns and those naming it under `also`. A search hit in another concern of another domain is a lead, recorded in the notes or cited with a flag. In the checker:
- flag a key whose concern scope.tsv gives to another domain without naming this one under `also`;
- at the merge, flag a key that supports `core` or `own-service` in capabilities of two domains.

#### R7. A move breaks the moving part's re-check, and a concern moved into a domain already run has no procedure (before the full run)

**Where.** Brief line 67: "A concern that belongs to another domain lands as `moved:<domain>` … and the coordinator moves it." `check_class_part.py` lines 196 and 197 refuse any landing of a concern that scope.tsv doesn't give the domain, a `moved:` row included.

**Problem.** Once the coordinator applies the move in scope.tsv, the part that asked for it fails its own check. And a concern moved into a domain whose parts already ran (a later domain moving one into B) has no part to land it.

**Evidence.** Tested: `SH-C-026` was moved to D in scope.tsv, as `B-anchor`'s `moved:D` row asked. Re-checking `B-anchor` gave "PROBLEM landings.tsv line 27: scope.tsv doesn't give SH-C-026 to domain B".

**Fix.** Accept `moved:<X>` where scope.tsv now gives the concern to X. Say who lands a concern moved into a domain already run: a short amendment part, checked like a mapping part.

#### R8. The scope part's reading has no Q1 matches, though its rule depends on them (before the dry run)

**Where.**
- Brief line 45: the scope part reads `concerns --all --where` and `seed`.
- Line 47: "A Q1 match keeps its concerns in one domain".
- `class_slice.py` has no command that lists every match, and `concerns` doesn't print a concern's match ids.
- The checker (lines 106 to 114) accepts a split match whenever the reason names it.

**Problem.** The agent learns of the matches only from the checker's complaints. The cheapest way to clear those complaints is to append the match id to each reason, which turns "keeps its concerns in one domain" into "names the match". **Reading:** the scope's errors carry into every domain, so it is worth getting right first.

**Evidence.** The keyword fixture, which knows nothing of the matches, gave 53 problems on its first check. Appending each split match's id to its concerns' reasons cleared all 53 (script `tools/mkscope.py --fix-matches`).

**Fix.** Print each concern's match and unclear-candidate ids in `concerns --all --where` (or add `matches --all`), and tell the scope part to read them before assigning. Have the checker list every split match, named or not, for the coordinator's check of `scope.tsv`.

#### R9. A ruling isn't tested against the landings (before the dry run)

**Where.** Lines 349 to 366 test a ruling's form, and that every needed candidate has one, but not what it says.

**Problem.** A ruling can say `apart` while the part joins the candidate's concerns in one capability, or `joined:<cap>` while they land elsewhere. These rulings go to the founder's veto with the extent's report (ruling 11), so a contradiction misinforms the founder.

**Evidence.** The synthetic `B-anchor` joins `SH-C-021` and `SA-C-022` (both in `U-002`) in `CM-CAT-003` on role, while its `rulings.tsv` says `U-002` is `apart`. The check gave 0 problems.

**Fix.** `apart` is a problem when two of the candidate's concerns from different platforms land in one capability. `joined:<cap>` is a problem unless at least two of its concerns land in that capability, its parent or a child.

#### R10. The size line doesn't hold beyond domain B (before the full run)

**Where.** Brief line 122: "An anchor part takes about 10 to 25 concerns per platform, with about 300 to 400 statements each".

**Problem.** Domain C is several times that, and its agent would load far more than "small".

**Evidence.** Shopify's concerns `SH-C-046` to `-105` and `-114` to `-126` (cart and checkout to tax, and shipping; chosen by id range, not by a scope reading) are 73 concerns with 1,063 statements (script).

**Fix.** Before domain C runs, split its anchor by area (CHK, ORD, PAY, TAX, SHP, RET), or by pairs of areas, with `scope.tsv`'s domain as the outer bound.

#### R11. Qualities: no derived scope, and unplaced limits have no citable value (optional)

**Where.**
- The brief lets a quality cite "an unplaced inventory entry by its id" (lines 38 and 41), and its `value` is "the platform's words" (line 117).
- `derived.tsv` covers cells only.

**Problem.** A quality's scope isn't derived anywhere. The value of an unplaced limit isn't in its inventory entry: it sits in Q1's `notes.md`, which is never cited. And the one citable variant limit disagrees with the unplaced one, a disagreement Q1 recorded only in `notes.md`.

**Evidence.**
- `SH-I-2520` `maxProductVariants`. Its citation `SH-S-7362` quotes only `"section": "resourceLimits", "key": "maxProductVariants"`, and its reason says "values per store in notes.md, Unplaced keys". Shopify's `notes.md`, lines 210 to 213, gives `2048`.
- `search --terms "100 variants;2048;maxProductVariants"` finds only `SH-C-020/decides/SH-S-7214`, "up to 100 variants for each of your products".
- Shopify's `notes.md`, line 204, records the disagreement.

**Fix.** Derive the qualities' scopes into a `derived-qualities.tsv`. For an unplaced entry, record the key as the quality, with the value "not in the concern map", and name the observed-sh structure in the notes as a gap.

#### R12. "Domain F holds … its APIs" can pull a feature's API out of its subject's domain (before the dry run)

**Where.** Brief line 49: "Domain F holds the app platform itself, its APIs, webhooks, developer tooling and partners."

**Problem.** "Its APIs" can be read as every API, against line 45's "what the concern is about". The seed itself lists Salla's storefront API under both SFR (domain E) and API (domain F), and puts Salla's rate-limiting and versioning pages under OPS (domain G).

**Evidence.** Concerns named after a feature's API:
- `SA-C-125` "Recurring payments and subscriptions sold by stores (Recurring Payments API; Subscriptions)": the inspector's keyword fixture put it in F on the word "API";
- `WC-C-079` "Store API (public storefront API)";
- `SA-C-101` "Storefront API used by store pages";
- `BC-C-053` "GraphQL Storefront API and storefront API tokens";
- `SA-C-201` "API rate limits".

**Fix.** "Domain F holds the API platform: its conventions, authentication, versioning and limits. A feature's own API goes with the feature."

#### R13. Small inconsistencies (optional)

- **Two spellings of one token.** Brief line 95 says "`not stated`"; the scripts derive `not-stated`.
- **Lenient separators.** `ids()` (`class_slice.py` lines 73 and 74) accepts commas and spaces in `also`, `join_evidence` and `keys`, although the brief says `;`.
- **Two meanings of "the model so far".** `model` reads every part folder that exists, the running part's own and, on a re-run, later ones (`part_dirs`, lines 211 to 218). The checker's model so far is the earlier parts only.
- **Rulings on moved concerns.** `taken` includes `moved:` landings, so a part rules on the candidates of concerns it moved out.
- **One statement, two values.** Two values on one statement are allowed, though line 95 says "each on its own statements".
- **No command for the homonym list.** Line 59 points at `matching-notes.md`, but line 32 says never to load the concern map's files whole, and no command prints that file.

#### R14. A `none-held` search is only as good as its terms (optional)

**Where.** Lines 289 to 295 re-run the agent's own terms.

**Problem.** A term that matches nothing passes silently.

**Evidence.** The synthetic parts' `none-held` cells searched `zzzfixtureterm` and passed with no flag.

**Fix.** Also run the capability's terms from its other platforms' cells over this platform's statements, and flag the hits.

#### R15. The back-fill must write files the brief doesn't mention (optional)

**Problem.** The checker requires all seven files with headers (line 120). The brief tells the back-fill only that it "add[s] no capabilities and land[s] no concerns" (line 82).

**Evidence.** The synthetic back-fill, written with only `cells.tsv` and `evidence.tsv`, got five "missing" problems.

**Fix.** Say "write the other files with their headers only", or have the checker accept their absence in a back-fill.

#### R16. Where the merge lives (optional)

**Problem.** The brief says "The coordinator checks your rows and merges the parts" (line 12), but `model` and the checker read the parts' folders, never a merged file. A correction the coordinator makes after review must therefore go into the parts' own files, or later parts won't see it.

**Fix.** Say that the parts' folders are the model, and that a coordinator's correction is made in them, noted in that part's notes.

### Can the dry run start?

**Reading:** yes, after seven small fixes. None needs a change to the design.
- **The scope part** can start once R8 and R12 are in. R8 means printing each concern's match ids and telling the agent to read them; R12 is one sentence on F's APIs.
  - Its checker already does what the brief asks; every scope check was tested on a faulty copy.
  - The scope comes first because every domain's parts read it, and a split match cleared only by naming is costly to undo later.
  - Its reading is 153,822 bytes for the five platforms, about 38,000 tokens at an assumed 4 bytes a token, plus the 652 rows it writes.
- **`B-anchor`** can start once the checker has R1, R2, R4, R5(a) and R9, a few lines each. Without them, these kinds of wrong row pass the part's own check, and only the review would catch them. Its reading for the fixture's 27 domain-B concerns is about 106,500 bytes of statements, 15,700 of matches and 8,600 of gaps.
- **`B-woocommerce`**: as for `B-anchor`. R4 matters most here, since WooCommerce lands by Q1's matches.
- **`B-backfill`**: as planned, with its other files written with headers (R15). R3 must be settled before `B-zid` runs.
- **Before the full run:** R3, R6, R7 and R10.

**What the re-inspection's scripts are.** They are in the inspector's scratchpad, under `reinsp/`:
- `tools/mkscope.py` and `tools/mkpart.py`: the fixtures;
- `model/`: the test model directory, a copy of the seed with the fixture's `scope.tsv` and parts;
- `mut/`: the last faulty copy.

The fixtures are tests of the scripts, not readings of the evidence.
