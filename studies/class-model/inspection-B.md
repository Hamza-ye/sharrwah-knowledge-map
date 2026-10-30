# Inspection of brief B (`studies/class-model/briefs/B-extent.md`)

Status: in progress. Findings are written as they are found; the summary table and the section on inspection A come last.

An inspection in Fagan's sense (1976): it looks for what would make an agent that follows the brief produce wrong, slanted or uncheckable rows. The inspector wrote none of the brief and changed nothing but this file. Every judgement below is marked **Reading**. Every count comes from a script named with it; the scripts are in the inspector's scratchpad and are restated in prose where a count depends on a choice.

## What was read, at which commits

- **This repository** at `93ebb15c` (branch `claude/vibrant-meitner-oh70v4`):
  - the brief, `studies/class-model/briefs/B-extent.md` (79 lines), whole;
  - `studies/class-model/seed/README.md` and `km-areas.tsv` (41 areas, 8 domains); not `km-questions.tsv`, as the brief says;
  - `studies/concern-map/README.md`; for each of the five platforms, the headers and columns of `concerns.tsv`, `statements.tsv`, `inventory.tsv`, `citations.tsv`, `gaps.tsv`, queried by script; the concern names of all five platforms; the `notes.md` sections "Lists used and their sizes" and "Where the inventory stops" (Salla's read in full, the others searched);
  - `studies/concern-map/matches.tsv` (88 rows) and `unclear-matches.tsv` (84 rows), by script; `map/out-of-scope.tsv`, by script; `matching-notes.md`, lines 196 to 212;
  - `questions/Q1-concern-map.md`, whole;
  - `PLAN.md`, lines 204 to 224 (Stage 4A) and 318 to 330 (section 6's kinds), and, for single checks, lines 36, 180 to 189, 284 to 300, 353 and 470 to 476;
  - `founder-decisions.tsv`, the rows of 26 to 29 October, for one check (the founder's intent of 29 October);
  - `evidence/product-class/README.md`, and the `manifest.tsv` of every run under `evidence/product-class/runs/`, by script;
  - `method/README.md`.
- **observed-sh** at `/home/user/observed-sh`, HEAD `19a5f643`: only to check that the commits Q1 cites (`b46731d0`, `e49840729`) exist and that the cited paths resolve at them.
- **observed-sa** at `/home/user/observed-sa`, HEAD `b0bd0b16`: the same check for `145f137`.
- **other-product-class** at `/home/user/other-product-class`, HEAD `0d79b794`: its `README.md` only. Q1 cites nothing in it (all Zid and BigCommerce citations are URLs; script below), so no citation the brief relies on resolves there.
- **The WooCommerce 11.2.1 release** at `/home/user/woocommerce-release/11.2.1`: the 41 release files that domain B's statements cite, each checked against `evidence/product-class/woocommerce-11.2.1/files.tsv` by sha256 (41 of 41 match).
- **After the findings were written:** `studies/class-model/inspection-A.md`, for the section on its must-fix findings.

### Citations the brief relies on resolve

For the statements of the concerns the inspector reads as domain B's (the sets are under finding 12), every cite id exists in its platform's `citations.tsv`, and every source resolves: Shopify 469 local paths at their observed-sh commit and 36 URLs; Salla 366 at `observed-sa@145f137` and 9 URLs; WooCommerce 91 release paths and 50 URLs; Zid 58 URLs; BigCommerce 61 URLs. A URL resolves through the `cited_in` column of a capture run's `manifest.tsv`, except `SH-S-7284` (`https://www.shopify.com/legal/terms`, cited 6 times), which no manifest lists by its id but whose URL is captured in `20261011T061248Z-q1-shopify-sources`. (Script: `resolve.py` in the scratchpad: `git cat-file -e <commit>:<path>` for local sources, path existence for the release and this repository, `cited_in` for URLs.)

## Findings

### 1. No rule says which concerns belong to a domain, and concerns and Q1's matches cross domains

**The brief's words.** Line 17: "Shopify's and Salla's `concerns.tsv`, whole; take the concerns that belong to your domain". Line 60: "In the anchor pass, a concern you look at and leave for another domain is listed, with that domain, in your notes." PLAN line 216 runs the anchor "one part per domain".

**The problem.** `concerns.tsv` has no area or domain column (header on every platform: `concern_id concern platform_terms inv_ids split_note`). Which concerns are a domain's is each agent's own judgement, made in parallel by seven anchor parts that do not see each other. A concern that two domains can claim is taken twice, or by neither, and the only trace is free text in two `notes.md` files. **Reading:** this is the brief's largest source of wrong rows, because it decides what each part even looks at.

**The evidence.**
- The seed itself puts one grouping in two areas of different domains: Shopify's "gift cards" under SEL (domain B) and LOY (domain D); Salla's "Gifting" under SEL and LOY (`km-areas.tsv`, rows SEL and LOY; script: every `;`-separated label listed under more than one area).
- Concerns span domains: `SA-C-063` "Customer wallet, cashback and gift cards" (SEL and LOY); `SA-C-125` "Recurring payments and subscriptions sold by stores" (SEL and PAY); `SA-C-127` "Charity stores' payment gateways" (the seed's SEL label "Charity stores", and PAY); `BC-C-010` "Marketing: coupons, banners and gift certificates" (MKT and SEL or LOY); `WC-C-104` "Merchandising extensions (bundles, gifts, product options, pricing, display, variations, …)" and `WC-C-105` "Conversion extensions (feedback, promotions, order recovery, loyalty, alerts, upsells)".
- Q1's matches cross domains, so a match can be split between two parts: `M-013` joins `SH-C-025` Gift cards with `SA-C-063` (wallet); `M-074` joins `SH-C-186` Subscriptions and selling plans, `SA-C-125` and `WC-C-100`. Of the 88 matches, 13 touch a concern the inspector reads as domain B's, and 6 of them touch it only through a concern that could belong elsewhere (`M-020`, `M-046`, `M-055`, `M-065`, `M-075`, `M-083`). Of the 84 unclear candidates, 21 touch one (script over `matches.tsv` and `unclear-matches.tsv` with the sets of finding 12).

**Proposed fix.** Before any anchor part runs, the coordinator writes one scope file, for example `studies/class-model/scope.tsv`: `platform · concern_id · domain · reason`, one row for every concern of all five platforms (198 + 152 + 118 + 96 + 88 = 652 rows), each a reading, with one rule for a concern that spans domains (it goes to one domain, named in `reason`, and the other domain's part sees it read-only). The brief then says "take the concerns `scope.tsv` gives your domain", and the "left for another domain" list becomes unnecessary. A checker tests that every concern is in exactly one domain, and that every Q1 match's concerns are in one domain or the split is named.

### 2. The area rule presupposes that the platforms place things in the seed's areas

**The brief's words.** Line 30: "each capability gets one area, the one where the two platforms put it. Each platform's own place goes in its cell." Line 34: "in a new capability that only your platform shows, with its area."

**The problem.** The platforms put a capability in their own admin sections, API groups and app categories, not in the seed's areas; the area is the agent's matching of those places to the seed's labels. The rule gives no answer when the two platforms' places fall in different areas, when only one platform shows the capability, or in the mapping pass, where the seed has no labels for WooCommerce, Zid or BigCommerce (`seed/README.md`: "Its labels are Shopify's and Salla's only"). Nor does the brief say that domain H ("Beyond the references") takes no capabilities, as PLAN line 216 does. **Reading:** within a domain this misfiles rows rather than corrupting them, so it is optional once finding 1 fixes the domain.

**The evidence.** Subscriptions: Shopify's seed label puts "subscriptions" in SEL; Salla's concern `SA-C-125` sits under its "Recurring Payments API" in the docs navigation (`SA-S-1173`), and Salla's SEL labels don't name it. `WC-C-093` "Cost of goods sold" has no seed label at all and could be CAT, INV or ANL.

**Proposed fix.** Area by this order: the seed label that names the platform's own term; where the two platforms differ, the area of the platform whose place is an admin section, with the other area in `note`; in the mapping pass, the area of the anchor capability that is its nearest parent, else the seed label with the same term. Never an area of domain H. A checker tests that `area` is an `area_id` of the part's domain and that `cap_id` carries it.

### 3. The dry run's mapping part has no domain to stay within

**The brief's words.** Line 18: "in the mapping pass: your platform's `concerns.tsv`, whole". Line 32: "In the mapping pass: each of your platform's concerns lands once." Line 34: "or in a new capability that only your platform shows". Line 11: "Your message names the pass and your domain or platform."

**The problem.** In the dry run the anchor holds domain B only. A WooCommerce agent that follows the brief takes all 118 of its concerns and must land each one: every concern outside B (payments, tax, shipping, legal, …) has no anchor capability to land in, so it lands "in a new capability that only your platform shows". That is false for most of them: Shopify and Salla show payments and tax, they are simply not in the anchor yet. **Reading:** as written, the dry run's mapping part produces about a hundred wrong "only WooCommerce" capabilities, and the review of the dry run would review mostly these. This blocks the dry run.

**The evidence.** WooCommerce has 118 concerns (`concerns.tsv`); the inspector reads 5 as clearly domain B's and 9 more as possibly so (finding 12). 71 of the 118 are in a Q1 match with a Shopify or Salla concern (script over `matches.tsv`), so they are certainly not "only WooCommerce".

**Proposed fix.** The mapping part takes the concerns `scope.tsv` (finding 1) gives the domains the anchor already holds, and lists the rest as "not mapped: domain not in the anchor yet". Or the message for the dry run names the domain, and the brief says the mapping part takes only that domain's concerns. Either way the brief says so, not only the message.

### 4. "Lands once" fails where one platform's concern is coarser than the capabilities, and makes false "Q1 holds nothing" cells

**The brief's words.** Line 27: "Join concerns that are the same thing on both platforms … Q1's matches are such joins." Line 29: "Where they cut at different grains, you choose the capabilities, using `parent` where one holds others." Line 32: "each of your platform's concerns lands once." Line 50: "Q1 holds nothing for this platform here: say that in so many words." Line 60: "Every concern you take appears in a cell." PLAN line 216: "checks that each concern lands once".

**The problem.**
- In the mapping pass, a concern that covers several anchor capabilities can land in only one. The cells of the others then say "Q1 holds nothing" for that platform although Q1 holds statements for them inside the coarser concern. Under the plan's rule, a "nothing held" cell is not counted, so a false one lowers the count and can turn `class` into `slot`.
- The anchor pass says "appears in a cell" (no "once"), the mapping pass "lands once", the plan "lands once". Whether a concern whose statements are cited in two capabilities' cells has landed once or twice is not defined, so the coordinator's check has nothing fixed to test.
- A Q1 match with several concerns on one side is a grain difference, but line 27 calls every match a join. Followed literally, `M-011` makes one capability of products, options and variants, categories and brands.
- A capability's statements are not always in one concern, so a "nothing held" written from the concern list alone can be false.

**The evidence.**
- `M-011`: `SH-C-020` against `SA-C-020;SA-C-021;SA-C-022;SA-C-023` against `WC-C-064`. Its own `granularity` note: "Salla splits products (SA-C-020), options and variants (SA-C-021), categories (SA-C-022) and brands (SA-C-023); WooCommerce keeps all in WC-C-064; Shopify keeps variants with products, has no brands concern". 33 of the 88 matches hold more than one concern on one side (13 Shopify, 10 Salla, 10 WooCommerce cells with a list; script).
- `WC-C-064` "Products and catalogue structure (types, variations, attributes, categories, tags, brands)" holds the `where` rows "Products > Categories" (`WC-S-0052`), "Products > Tags" (`WC-S-0053`), "Products > Brands" (`WC-S-0054`) and "Products > Attributes" (`WC-S-0055`). If it lands in a "Products" capability, the WooCommerce cells of categories, tags, brands and attributes say "nothing held".
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
- **Missing cells.** A capability added in the mapping pass gets cells only for the platform that added it and the platforms after it. Shopify and Salla never get one, even where the coarser anchor concern holds statements for it. The plan's count is then biased by the order: the count of a capability BigCommerce adds is at most 1, and the anchor's shape wins by construction. **Reading:** this is a slant toward Shopify's and Salla's shape, beyond the exemplar design the plan chose.
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
- What the notes do have is sizes: for example Salla's "settings | `dashboard-settings-menu/merchant@en` | 23 pages and 4 group headings" (Salla `notes.md`, line 37). That is the menu of one observed store.

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
- **Subscriptions.** `WC-C-100`: `where` "Extensions > Merchandising > Subscriptions" (`WC-S-0739`); `decides` "WooCommerce Subscriptions is a premium extension …" (`WC-S-5351`). That it is Woo-made is stated only under another concern, `WC-C-050` "Developed by Woo" (`WC-S-0697`). Shopify's `SH-C-186`: `where` "Subscription apps" (`SH-S-2657`) and "Subscription apps enable developers and merchants to build subscription experiences" (`SH-S-0763`), with 14 `boundary` rows (the selling-plan and subscription-contract API).
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

**The problem.** PLAN line 353: "A gap stays visible, with the work that would close it." A cell's placement is read from the statements that exist. Where Q1's `where` or `responsible` placement is a gap, nothing in the cell says so, so a `core` read from a plan line alone looks like a `core` read from an admin route. The review is told to check every placement against all of Q1's statements (PLAN line 213), but not against the gaps.

**The evidence.** In domain B's scope:
- `SH-C-038` has a `where` gap ("observation needed");
- all 21 Salla concerns but one (`SA-C-124`) have `responsible` as "page not read", and most also have `reason` as "page not read";
- `ZD-C-101` Gifting has only a `where` row, with its other placements gaps;
- `BC-C-036` Wishlists likewise has only a `where` row.

Script: per concern, statements by placement and gaps with their kind.

**Proposed fix.** Add `gaps.tsv` to the reading list and a `gaps` column to `cells.tsv`, listing the Q1 placements of the cell's concerns that are gaps, with their kind (`where:observation needed`).

### 15. Optional: the commit for URL sources, and what reading more context may produce

**The brief's words.** Line 19: "`citations.tsv` for the commit each source was read at". Line 22: "the structures Q1's citations name, at the commit `citations.tsv` gives, where a statement needs more context."

**The problem.** `citations.tsv` gives a commit only for observed-sh and observed-sa sources. URL sources carry none, and the release carries a version, not a commit. Their copies are in this repository's `evidence/product-class/runs/*/manifest.tsv`, found by URL, and in `/home/user/woocommerce-release/11.2.1`; the brief names neither. The brief also doesn't say whether more context read from a structure may be cited. Line 58 implies it may not ("every cell cites Q1's ids").

**The evidence.** Every Zid citation (1,087) and every BigCommerce citation (481) is a URL. So are 581 of WooCommerce's 1,466, 1,008 of Shopify's 5,055 and 278 of Salla's 2,982. Script: classifying `source` by prefix.

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

