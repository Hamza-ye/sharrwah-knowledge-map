# Inspection of brief A, the class's extent

**What this is:** an inspection (Fagan 1976) of `studies/class-model/briefs/A-extent.md` before any part runs, by an agent that wrote none of it. It looks for what would make an agent following the brief produce wrong or slanted rows. Nothing was changed except this file, and nothing was committed.

**What was read, and at which commits:**
- this repository at `95fd2916`: the brief, `studies/class-model/seed/`, `studies/concern-map/` and `questions/Q1-concern-map.md`, with `reports/intent-review.md` for the step's reason;
- for single checks: `PLAN.md`, `STATE.md` and `founder-decisions.tsv`;
- the evidence repositories, for their layout and commits only: observed-sh at `19a5f6435`, observed-sa at `b0bd0b16`, and other-product-class at `0d79b794`.

Counts come from read-only `python3 -I` scripts over those files. Line numbers are the brief's at `95fd2916`. A judgement of mine is marked **Reading**.

## Summary

| # | Finding | Verdict |
| --- | --- | --- |
| 1 | "Where it lives" would come from placement labels Q1 abandoned, and Zid and BigCommerce have no such values at all | must fix |
| 2 | The joining rule isn't Q1's. "Filling the same role" is the test Q1 refused, and the brief asks agents to rule the founder's unclear list with it | must fix |
| 3 | Zid and BigCommerce were never matched, and `single-platform.tsv` covers three platforms, not five | must fix |
| 4 | "Exactly one capability" contradicts "the smallest unit", given Q1's uneven granularity, and nothing sets how small a capability can be | must fix |
| 5 | The kinds don't cover every case (`outside`, mixed placements), and the vendor's own apps get three different placements | must fix |
| 6 | Commonality counts only "own", so "left to apps everywhere" and "shown nowhere" both score 0, and `not shown` counts against the less-read platforms | must fix |
| 7 | The "Why" tells the agent what the rows are for, and it rests on a handoff not yet recorded as a decision | must fix |
| 8 | The seed's questions pre-answer an unclear candidate and bring in a kind the brief doesn't have | must fix |
| 9 | There's no rule for a concern that spans areas, the seed's own areas overlap, and parts can't reconcile `concern-areas.tsv` | must fix |
| 10 | `absent` has no basis the agent can see. Q1 never records absence, and the brief excludes the files that say where each list stops | must fix |
| 11 | The brief points at other-product-class's `index/` (finding aids), not `structures/`, and pins no commits | must fix |
| 12 | Statements have no ids, and the brief's own example cites another concern's statement | must fix |
| 13 | `decides` is one column for five platforms, Q1 encodes it three ways, and Zid and BigCommerce have no values | must fix |
| 14 | The market rule contradicts the `world` kind, and a market's law in a platform's core can be read two ways | must fix |
| 15 | Qualities recorded as `class` capabilities mix values with capabilities, and Q1 barely holds them | must fix |
| 16 | Excluding every `note` column hides the matching pass's own warnings about weak matches | must fix (a); optional (b) |
| 17 | Several output cells can't be checked as specified, and parallel parts have no protocol for the shared files | must fix |
| 18 | No checker is named. Its tests are listed below | optional |
| 19 | As a product map, the output lacks plan gating and evidence level per cell, and a feature tree | must fix (a, b); optional (c to e) |
| 20 | Size: CAT with STF fits about 40 requests only with the bounds that findings 4, 9 and 11 set | optional |
| 21 | It is unclear whose labels count for WooCommerce areas that WordPress holds, and what "shows an area" means | optional |

## Findings

### 1. "Where it lives" would come from labels Q1 abandoned, and from nothing for Zid and BigCommerce

- **Brief:** line 15, "`placements.tsv` (Shopify, Salla and WooCommerce; Zid's and BigCommerce's placements are in their statements' `placement` column)". Line 29, "Where it lives: … from Q1's placements".
- **Problem:** For three platforms, the brief takes placement values from the first runs' `placements.tsv`. Q1 replaced that file on 11 October because its values were our category names, often resting only on an entry existing. For Zid and BigCommerce, the statements' `placement` column holds the name of the question a statement answers, not a value. So no `core` or `extension point` exists for them anywhere in Q1, and every one of their cells would be a fresh reading presented as "Q1's placement". Kind and commonality, the step's main numbers, would rest on abandoned labels for three platforms and on unmarked readings for two.
- **Evidence:**
  - Q1 (`questions/Q1-concern-map.md`):
    - lines 53 to 63: the reshape, because "95% of the shown values were our category names"; line 63: "The value lists … no longer apply";
    - line 91: `statements.tsv` and `gaps.tsv` "replace `placements.tsv`, which is kept as a record of the first runs";
    - line 88: "No inference goes into a statement".
  - `studies/concern-map/README.md` line 34: "What was not carried forward: the first runs' placement labels."
  - `measurements-2026-10-11.md` §1:
    - "where it lives" values that cite only that an entry exists: Shopify 98 of 196, Salla 92 of 129, WooCommerce 34 of 116;
    - force-fits in the hand sample: "Shopify's 24/7 support and Community filed as 'core' software, Partner Dashboard payouts filed as 'core'".
  - The values as held:
    - Shopify: all 205 `software` rows are free text, such as "core: Products in the admin and the Products API". 9 concerns have two rows, and SH-C-201 and SH-C-202 have none.
    - Salla: 87 of 148 are a listed value exactly. The other 61 include 19 `not shown` and forms such as "core (Salla Partners portal)", "extension point (provider slot)" and "other: حاسبة الرسوم". SA-C-301 to SA-C-304 have no row.
    - WooCommerce: 116 are listed values and 2 are empty.
  - Zid's statement `placement` values: where 130, decides 267, responsible 98, boundary 125, reason 34. BigCommerce's: where 143, decides 126, boundary 132, responsible 49, reason 23.
  - What a Zid or BigCommerce agent would have to classify:
    - ZD-C-083's `where` statement is a docs path, "Merchant APIs > Products > Managing Products";
    - BC-C-001's is "The Catalog API manages products, categories, brands, bulk pricing rules, and more."
  - `where` statements do exist for nearly every concern: Shopify 187 of 198, Salla 144 of 152, WooCommerce 108 of 118, Zid 95 of 96, BigCommerce 87 of 88.
  - `PLAN.md` line 323, risk 2: "A rule, label, example or brief of ours makes the result, as our category names … did".
- **Verdict: must fix.**
  - Derive "where it lives" for all five platforms the same way, from `statements.tsv` rows with placement `where`.
  - In every cell, mark the mapping to the six values as a reading, citing the concern and the statement.
  - Give the mapping as tests:
    - the platform's own admin section, API group or code path: `core`;
    - a separately named product, host or subscription of the platform: `separate service`;
    - an app or extension target, a function or a provider slot: `extension point`;
    - a party the platform names as outside: `outside`.
  - Use `placements.tsv` only as a cross-check, never as a source.

### 2. The joining rule isn't Q1's, and the brief has agents rule the founder's unclear list with it

- **Brief:** line 26, "joining the five platforms by Q1's rule for the same thing: their own terms, the same thing filling the same role". Line 27, "For an unclear candidate, decide by the rule, and mark it as a reading."
- **Problem:** Q1 joined concerns only where terms, identifiers or definitions clearly match. Pairs linked only by function went to the founder, unsettled. "Filling the same role" is the function test Q1 refused, so the brief's rule is a new one presented as Q1's. Unclear candidates are, by construction, the pairs Q1's rule couldn't join. "Decide by the rule" then gives "no" every time under Q1's rule, and "yes" almost every time under the role test. The second raises commonality across the map. The brief also doesn't say which wins when a concern is both in a match and in an unclear candidate.
- **Evidence:**
  - Q1 line 127: "matches concerns only where the platforms' own terms clearly match. Every unclear match stays separate and goes on a list for the founder. Neither that pass nor the coordinating session settles them."
  - `matching-notes.md`:
    - line 3: "It matches only where the platforms' own terms, identifiers or definitions clearly match. Every other likely pair is on the unclear list for the founder, unsettled";
    - line 164: "Same subject, different words (27 rows) … only function links them".
  - `unclear-matches.tsv`: 81 of 84 rows name the founder in `what_would_settle_it`.
  - U-002 (SH-C-021 Collections against SA-C-022 and WC-C-064): "Different terms; only function suggests they are the same."
  - 94 concern ids sit both in a match and in an unclear candidate.
    - SH-C-020 is in M-011 and in U-005, U-013, U-070, U-081 and U-082.
    - SH-C-021 is unclear (U-002) against SA-C-022 and WC-C-064, which M-011 already joins to SH-C-020.
  - `founder-decisions.tsv` has no row that moves these rulings to engineering. Its last row is dated 28 October.
- **Verdict: must fix.**
  - State the rule in full. A join on terms, identifiers or definitions is a fact, citing the statements. A join on role alone is a reading.
  - Record every join in its own file, for example `joins.tsv` with the capability, the concern ids, the basis kind and the statements.
  - Report each row's commonality both with its readings and without them.
  - Set precedence: a match row stands, and a ruling on an unclear candidate may add a concern to a capability but never splits a match without a stated reason.
  - Record before the run who rules Q1's unclear list, the founder or engineering. Until then the agent proposes and doesn't decide.

### 3. Zid and BigCommerce were never matched, and `single-platform.tsv` covers three platforms

- **Brief:** line 16, "`matches.tsv`, `unclear-matches.tsv` and `map/single-platform.tsv`". Line 27, "Use `matches.tsv` where it already joins them."
- **Problem:** The matching pass covers Shopify, Salla and WooCommerce only. Zid's 96 concerns and BigCommerce's 88 have no join at all, so every join to them is new work. `single-platform.tsv` lists concerns left unmatched among three platforms on 11 October, and some of them sit on the unclear list. An agent reading it as "one platform of five" would set commonality to 1 and not search Zid or BigCommerce.
- **Evidence:**
  - `matches.tsv` columns: `match_id`, `shopify`, `salla`, `woocommerce`, `basis`, `granularity`, `note`. No row holds a ZD- or BC- id, and `unclear-matches.tsv` has the same three platforms.
  - `map/single-platform.tsv`: Shopify 98, Salla 68, WooCommerce 47. No Zid or BigCommerce rows.
  - Q1 lines 100 to 116: Zid and BigCommerce were added on 12 October, and each "stops before matching".
  - Unclear candidates in `single-platform.tsv`: SH-C-011 Collaborators (U-010), SH-C-037 Catalogs (U-015), SH-C-189 Custom products (U-059).
- **Verdict: must fix.**
  - Say that the matching covers three platforms.
  - Say that every Zid and BigCommerce join is made by the stated rule (finding 2) and recorded per join.
  - Require each capability's Zid and BigCommerce cells to show the search: a concern, or `not shown` with its gap.
  - Describe `single-platform.tsv` as "unmatched among three, 11 October".

### 4. "Exactly one capability" contradicts "the smallest unit", and nothing sets how small a capability can be

- **Brief:** line 25, "A capability is the smallest unit a store or the platform can have or not have". Line 42, "Every Q1 concern … lands in exactly one capability". Line 51.
- **Problem:** Q1's concerns differ in size between platforms. One coarse concern holds several smallest units, so both rules can't hold:
  - either capabilities stay as coarse as the coarsest concern, and a platform gets credit for parts it lacks;
  - or one concern lands in several capabilities.

  "Smallest unit" also has no lower bound. One agent could make each staff permission a capability, and another make one capability per concern.
- **Evidence:**
  - M-011 joins SH-C-020 with SA-C-020, SA-C-021, SA-C-022 and SA-C-023, and with WC-C-064. Its `granularity`: "Salla splits products (SA-C-020), options and variants (SA-C-021), categories (SA-C-022) and brands (SA-C-023); WooCommerce keeps all in WC-C-064; Shopify keeps variants with products, has no brands concern".
  - WC-C-064 is "Products and catalogue structure (types, variations, attributes, categories, tags, brands)". **Reading:** a single coarse "products" capability would count Shopify as having brands.
  - STF's inventories:
    - Shopify: 283 `other:staff-permissions` entries and 20 `other:staff-roles`;
    - Salla: 217 `other:staff-permissions`;
    - Zid: 57.
  - observed-sh holds `admin-permission-tree`, which `measurements-2026-10-11.md` §3 gives as 142 permissions in 20 categories.
- **Verdict: must fix.**
  - Let a concern land in several capabilities: `concern-areas.tsv` gets one row per concern and capability, and the check becomes "at least one".
  - Mark a partial fill in the cell, for example `core (part) WC-C-064 …`.
  - Set the lower bound: a capability is something one platform's own list names as a feature, setting, plan line or resource that a store can have or lack. Single permissions, scopes or webhook topics are evidence for a capability, never a capability each.

### 5. The kinds don't cover every case, and the vendor's own apps get three different placements

- **Brief:** line 29, with the placement values. Lines 32 to 34, the kinds.
- **Problem:**
  - (a) A capability whose platforms place it `outside`, or that mixes `outside` with `extension point`, has no kind, yet line 42 still forces it into a capability.
  - (b) The vendor's own apps and extensions are installed through its app slot. Depending on which first run labelled them, they are `core`, `separate service` or `extension point`, and that choice decides class against slot.
- **Evidence:**
  - Mixed and `outside` placements:
    - SH-C-188's first-run value: "outside platform: upsell, bundle and pre-order apps; extension point: product configuration extensions";
    - WooCommerce's `placements.tsv` holds 13 "outside the platform".
  - The vendor's own apps:
    - SH-C-141: "core: Shopify Collective, connecting Shopify stores to sell each other's products";
    - SH-C-142: "core: Shopify Point of Sale app and Retail API…";
    - WC-C-006, WooPayments, a "Woo-made extension and service": "separate service or product line", though Q1 line 46 settled that WooPayments "is placed as an extension, not as part of WooCommerce";
    - WC-C-118, EU VAT Number, "a Woo-made extension": "extension point".
- **Verdict: must fix.**
  - Give a full table from the five cells to the kind, covering all-`outside` and mixed rows, for example a kind `outside` that is not extent.
  - Add a placement value for the vendor's own apps, such as `own extension`. Count it with `core` and `separate service` as the vendor's own, but show it apart, so a later reader can count it either way.

### 6. Commonality counts only "own", and `not shown` counts against the less-read platforms

- **Brief:** line 35, "`commonality`: how many of the five establish it as their own, 0 to 5". Line 12, the source types, which the brief names but never uses in a column.
- **Problem:**
  - A capability that every platform leaves to apps and one that no platform shows both score 0.
  - `not shown` counts as "not established", which penalises the platforms read at declaration level, those with unread pages, and those whose lists of extension points are thin.
  - A product map's basic cell is presence per product, and this one loses it.
  - Q1's rule to compare like with like isn't carried over.
- **Evidence:**
  - Concern-map `README.md` lines 16 and 17: Zid and BigCommerce were read "declaration level, no accounts".
  - Salla's gaps: 206 of 230 are `page not read`.
  - Lists of extension points in the inventories: Shopify 326, Salla 389, WooCommerce 50, Zid 4, BigCommerce none.
  - Q1 line 118: "A platform's declaration is compared with another platform's declaration. A statement drawn from observed behaviour … stays marked as observed".
  - `gaps.tsv` isn't on the read list, so a `not shown` cell can't say whether its gap is "searched, not found" or "page not read".
- **Verdict: must fix.**
  - Report counts per row: `own` (core, separate service, own extension), `slot`, `outside`, `not_shown` and `absent`. Alternatively, give commonality as "own of shown".
  - Add `gaps.tsv` to the read list, with `held-check.tsv` (concern-map `README.md` line 5), so each `not shown` cell carries its gap's kind.
  - Add an evidence level per cell, using `km-source-types.tsv`'s codes (DECL, SHIP, OBS), as Q1's like-with-like rule asks.

### 7. The "Why" steers toward inclusion, and it rests on a handoff not yet recorded

- **Brief:** line 3, "Its extent comes from the class, not from its launch: what the class establishes, and the slots it leaves for outside parties, belong to the platform (the founder's handoff of 29 October 2026, `reports/intent-review.md`)". Line 33, the slot rule.
- **Problem:**
  - (a) The line tells the agent what its rows are for: what it finds becomes the platform's extent. **Reading:** that leans an agent toward generous joins and toward `class`.
  - (b) The frame rests on a handoff the founder hasn't had recorded. The review it cites says it records nothing, and its answer lines are open.
  - (c) The brief's slot rule differs from the rule the review put to the founder.
- **Evidence:**
  - `reports/intent-review.md`: line 3, "Nothing here is recorded as your decision". Lines 118 to 123 are the open answer lines.
  - `founder-decisions.tsv` ends at 28 October. `PLAN.md` and `STATE.md` contain no stage for the class model: neither says "extent" or "class model".
  - The commit that added the brief, `95fd2916`, says: "nothing recorded as the founder's yet".
  - `CLAUDE.md`: `founder-decisions.tsv` holds "the founder's decisions in force".
  - The slot rules:
    - review line 82: "what all five leave to third-party apps is a slot";
    - brief line 33: "every platform that shows the capability leaves it to an extension point".

    With `not shown` cells, the two differ: under the brief, a capability one platform shows as an extension point is a slot.
  - `PLAN.md` line 69: a brief is read "for anything that presupposes the answer".
- **Verdict: must fix.**
  - Run the brief once the decision is recorded and `PLAN.md` carries the stage, and cite the decision's row.
  - In the agent's brief, state the task without its purpose: "record, per area, what each of the five platforms shows and where it places it". Keep the "Why" in the coordinator's files.
  - Align the slot rule with the recorded decision.

### 8. The seed's questions pre-answer an unclear candidate and bring in a kind the brief doesn't have

- **Brief:** lines 10 and 11: "`km-areas.tsv`: your areas' rows"; "`km-questions.tsv`: … as leads to what an area covers, never as answers".
- **Problem:** The questions were written from Shopify and Salla, and their examples steer which capabilities an agent looks for. A lead steers even when it is "never an answer".
- **Evidence:**
  - CAT-02: "How are products grouped (collections, categories, brands, tags, a standard taxonomy)". This puts Shopify's collections beside categories, the question U-002 leaves open.
  - CAT-06: "Which catalog capabilities exist in only one platform (product restrictions, option templates, product SEO fields, ...), and is each a class feature or a vendor choice?"
    - The examples are Salla's, and the question assumes they exist on one platform only.
    - "Vendor choice" is a kind the brief's rules don't have.
  - STF-02: "how do the two vocabularies map onto each other": two platforms.
  - STF-06: "POS-only roles, access scoped to a location": Shopify's features.
  - `km-areas.tsv` line 3, STF's Salla groupings: "10 built-in roles; 192 permissions in 16 groups". The count is uncited, and Q1's Salla inventory holds 217 `other:staff-permissions` entries, 18 of them out of scope. The count can't be traced from anything the brief names.
- **Verdict: must fix.**
  - For this breadth step, give agents only each area's id, name and domain.
  - Hold back `km-questions.tsv`, which belongs to the area's later model, or keep only its `facet` column.
  - Say that the seed's groupings are neither labels nor citations.

### 9. There's no rule for a concern spanning areas, the seed's areas overlap, and parts can't reconcile

- **Brief:** line 5, "the areas your message names". Line 42, "or is named as belonging to another area". Line 51.
- **Problem:**
  - Nothing says where a concern that spans areas goes, and the seed's own groupings overlap.
  - Parts run separately, so a concern one part sends to another area is lost if that area's part doesn't take it.
  - `concern-areas.tsv` would get a pointer row from one part and a claim row from another. "Never rewrite another part's" stops anyone reconciling them.
- **Evidence:**
  - Overlaps in `km-areas.tsv`. ACC's Shopify groupings are "Settings > Organization, Users, Billing", STF's are "Settings > Users > Roles, Security", and TRU's include "account Security".
  - Concerns that fit two or more areas (**Reading**, from their names):
    - SH-C-009 "Users and staff accounts": ACC or STF;
    - SH-C-037 "Catalogs (market and B2B product and price catalogs)": CAT, B2B or MKS;
    - SH-C-011 "Collaborators" and SA-C-204 "Partner account, ID verification and employees": STF or PTN;
    - SA-C-095 "Salla Point point of sale", which carries staff permissions: POS or STF;
    - WC-C-067 "Product import and export (CSV)": CAT or MIG.
  - Staff permissions are encoded differently. Shopify's entries carry SH-C-010 plus the concern guarded ("SH-C-010;SH-C-020" on 15 entries). Salla's carry only the concern guarded (SA-C-220 on 30, SA-C-040 on 21), never SA-C-009.
- **Verdict: must fix.**
  - Before any part runs, the coordinator drafts `concern-areas.tsv` for all 652 concerns, as a reading.
  - Give it a tie-break, for example the area of the concern's `where` statement.
  - Parts correct the draft in a separate column, with a reason, and never by dropping rows.
  - The final check is global: no concern left without an area and a capability.

### 10. `absent` has no basis the agent can see

- **Brief:** line 15, "each entry's `list` names the platform's own complete list it comes from". Line 19, "Leave out every `notes*.md` file". Lines 23 and 29.
- **Problem:**
  - Q1 never records absence and never marks a list complete.
  - The `list` column names a type of list, not a complete one.
  - The only place where Q1 says where each inventory stops is the platform's `notes.md`, which the brief excludes.

  So two agents would draw `absent` from different lists.
- **Evidence:**
  - Q1 line 89, rule 6: "A key or value absent from them is a gap, never 'does not exist'."
  - Q1 line 156: `list` is "api-resources, access-scopes, …, or `other:<name>`". Values held include Shopify's `other:help-center-sections` (260), Salla's `other:dashboard-features` (568) and Zid's `other:app-market-categories` (35).
  - Q1 line 161: `notes.md` holds "The lists used and their sizes; where the inventory stops".
  - The nearest Q1 comes to absence is the gap kind "searched, not found": Shopify 182, Zid 97, BigCommerce 86, WooCommerce 106. Even that isn't absence.
- **Verdict: must fix.**
  - The coordinator names, per platform, the lists that count as complete, at a pinned commit, with what shows each one is complete. Two examples:
    - Zid's `structures/dashboard-route-manifest/`, which its `README.md` describes as "Every page of the dashboard, as Zid's code lists it";
    - the WooCommerce 11.2.1 release, for WooCommerce's own code.
  - `absent` then cites that list's path at its commit, and everything else is `not shown`.
  - Correct line 15's description of `list`.

### 11. The brief points at finding aids instead of lists, and pins no commits

- **Brief:** line 17, "`README.md` and `index/` (other-product-class's `zid/`, `bigcommerce/`, `woocommerce/`). Cite it at its commit."
- **Problem:**
  - other-product-class keeps the platforms' lists in `structures/`. `index/` holds ledgers, run lists and instruments, which are finding aids.
  - Zid and BigCommerce have no admin-navigation list in Q1, so step 1's labels for them depend on this pointer.
  - "Its commit" names no commit, and both evidence repositories have moved past the commits Q1 cites.
- **Evidence:**
  - other-product-class at `0d79b794`:
    - `zid/README.md` lines 28 to 35: the route manifest (437 routes), the dashboard's own index of 119 pages with English and Arabic titles, `structures/store-permissions/` and `structures/store-plan-policies/`;
    - `zid/index/` holds `ledger/`, `runs.tsv`, `run-notes.tsv` and `instruments.json`;
    - `bigcommerce/structures/` holds `settings-list`, `plan-comparison`, `channel-catalog` and others.
  - `km-source-types.tsv` line 5: IDX is "A finding aid only, never evidence on its own".
  - Q1's inventory lists: no `admin-navigation` list for Zid or BigCommerce.
  - Q1's citations are at observed-sh `b46731d0` (2,315) and `e49840729` (1,732), and at observed-sa `145f137` (2,704). The clones' heads are now observed-sh `19a5f6435` and observed-sa `b0bd0b16`.
- **Verdict: must fix.**
  - Point at `structures/`, reached through each repository's `README.md`.
  - Pin each repository's commit.
  - Say that Q1's citation ids resolve at Q1's commits.
  - Optionally, name per area the structures to read. That also bounds the work (finding 20).

### 12. Statements have no ids, and the brief's own example cites another concern's statement

- **Brief:** line 15, "`statements.tsv` (by id)". Line 29, "cited by concern id and statement id". Line 50, "such as `core SH-C-012 SH-S-0045`".
- **Problem:** `statements.tsv` has no id column. `SH-S-…` ids are citation ids, and one citation id doesn't pick out one statement. So a checker can't confirm that a cell cites a `where` statement of the concern it names.
- **Evidence:**
  - `statements.tsv` columns, on all five platforms: `concern_id`, `placement`, `structure`, `identifier`, `statement`, `scope`, `cite_ids`, `note`.
  - Shopify's statements use 2,673 citation ids:
    - 842 back more than one pair of concern and placement;
    - 791 back more than one concern;
    - 114 statements carry several citation ids.
  - The brief's example: `SH-S-0045` backs only SH-C-147's `decides` statement. SH-C-012's `where` statements cite `SH-S-5206` and `SH-S-1581`.
- **Verdict: must fix.**
  - Define the reference as a concern id plus a citation id that backs a `where` statement of that concern, which a checker can test. The alternative is statement ids issued by the coordinator, such as line numbers at a pinned commit.
  - Replace the example with a real pair, such as `SH-C-012` with `SH-S-5206`.

### 13. `decides` is one column for five platforms, encoded three ways, and empty for two

- **Brief:** line 30, "Who decides its value: from the same placements, where Q1 holds them". Line 50: one `decides` column.
- **Problem:**
  - One cell can't hold five platforms' deciders.
  - The first runs encode a decision with two deciders in three different ways.
  - Zid and BigCommerce have no first-run values at all.
- **Evidence:**
  - `measurements-2026-10-11.md` §1, "One question, three different encodings":
    - Shopify: one row per party for 75 concerns, and combined values for 42;
    - Salla: combined values;
    - WooCommerce: one party kept, with 26 notes naming a second.
  - Examples:
    - SH-C-010 has three rows: "merchant: administrators manage users and roles"; "platform at build: Shopify defines the permission handles…"; "operator, per plan: custom user groups are a Plus row";
    - SA-C-009: "merchant; operator per plan";
    - WC-C-080: "merchant".
  - `decides` statements are held for Shopify 193 of 198, Salla 140 of 152, WooCommerce 110 of 118, Zid 87 of 96 and BigCommerce 68 of 88.
- **Verdict: must fix.**
  - Record `decides` per platform, from the `decides` statements, as the platform's own identifiers: a plan line, a permission handle or a setting key. Cite them, and use no category names.
  - Alternatively, drop `decides` from this step and leave it to each area's model.

### 14. The market rule contradicts the `world` kind

- **Brief:** line 34, `world`. Line 41, "No market's facts and no market's name shape a row."
- **Problem:**
  - A `world` row is, by definition, a market's providers or law, so line 41 forbids what line 34 asks for.
  - `world` rows go in `capabilities.tsv`, though they are "never the platform's extent", and commonality means nothing for them.
  - A market's law built into a regional platform's core can be read as `class`, with its scope in the citation, or as `world`. Two agents would split.
- **Evidence:**
  - Lists that name providers:
    - WooCommerce: `other:payment-extension-suggestions` (46) and `other:shipping-partner-suggestions` (6);
    - BigCommerce: `other:embedded-payment-providers` (21) and `other:subprocessors` (21);
    - Salla: `other:store-payment-methods` (14).
  - Law in a regional platform's core:
    - `km-areas.tsv` line 13, TAX's Salla groupings: "ZATCA in plans";
    - SA-C-160, "Taxes per market".
- **Verdict: must fix.**
  - Put slot fillers in their own file, with the slot's `cap_id`, the platform, the filler as named, its scope and its citation.
  - Say that a law or provider built into a platform's own core is that platform's `core`, for a capability with a neutral name and its country scope in the citation.
  - Reword line 41 as "No market's facts decide a capability's name or its kind."

### 15. Qualities as `class` capabilities

- **Brief:** line 36.
- **Problem:**
  - A stated limit, certification, uptime or data location is a value, not a capability. Recording it as kind `class` mixes the two and inflates the counts of `class` rows.
  - Q1 holds few of these qualities, and the one catalogue limit it holds sits outside its concerns.
  - The read list doesn't reach the files that state most of them.
- **Evidence:**
  - Concerns that hold qualities: SH-C-171 (API versioning and limits), SH-C-184 (card data security), SA-C-201 (API rate limits), SA-C-234 (platform security and service status), BC-C-028 (PCI DSS), BC-C-057 (API rate limits), WC-C-018 and WC-C-019 (PCI DSS) and WC-C-031 (checkout rate limiting). Zid has none.
  - "Uptime" appears in one Shopify statement and one BigCommerce statement.
  - Shopify's `other:store-resource-limits` entries, `maxProductOptions` and `maxProductVariants`, carry no concern id.
- **Verdict: must fix.**
  - Record qualities in a separate file, `qualities.tsv`, with the area, the quality, the platform, the value as stated, its scope, and its citation at a commit. Write "not stated" where no source states one, never `absent`.
  - Name the sources the agent may read, for example observed-sh's `shop-request-details` and plan tables, Zid's `store-plan-policies` and BigCommerce's `plan-comparison`.
  - Say whether inventory entries Q1 left out of scope may be used.

### 16. Excluding every `note` column hides the matching pass's warnings

- **Brief:** line 19, "Leave out every `notes*.md` file and every `note` column."
- **Problem:**
  - (a) The rule hides how strong each match is and the matching pass's own flags on two weak matches, so agents would take those matches as settled.
  - (b) The brief's own output file, `notes-extent.md`, falls under `notes*.md`, and the rule doesn't say whether `matching-notes.md` is in or out.
- **Evidence:**
  - `matches.tsv`'s `note` column opens with "Basis kind": 84 rows begin "term" (M-070 reads "term+definition"), 3 "definition" and 1 "identifier".
  - Concern-map `README.md` line 30: "The matching agent flagged M-070 (Shopify Functions and Salla's App Functions) and M-064 (chat with customers and Salla Chat). Both rest on a shared main word." That README isn't on the read list.
- **Verdict:**
  - **(a) Must fix.** Allow `matches.tsv`'s `note` column, or list M-064 and M-070 in the brief as flagged.
  - **(b) Optional.** Name `notes-extent.md` as the exception, and say whether `matching-notes.md` is in or out.

### 17. Several outputs can't be checked as specified, and parallel parts have no protocol for shared files

- **Brief:** lines 48 to 52.
- **Problem:**
  - (a) `reading` is one column per row. A row has up to five placement readings and several join readings, so nobody can tell which cell is the reading.
  - (b) `areas.tsv` puts a label and its citation in one cell with no separator, and a platform often has several labels. Shopify's CAT groupings in the seed are "Products, Collections; API category Products and collections".
  - (c) The cell grammar, a placement word followed by ids, has no room for:
    - the path and commit of the list an `absent` cell rests on;
    - two placements on one platform, such as SH-C-188's "outside …; extension point …";
    - a partial fill (finding 4).
  - (d) In `concern-areas.tsv`, one part's pointer rows (with an empty `cap_id`) sit beside another part's claim rows, and "never rewrite another part's" prevents reconciling them.
  - (e) "With a header row … Append" gives no protocol for parts that run at the same time: two of them can both write a header, or interleave rows. No column says which part wrote a row.
- **Verdict: must fix.**
  - Give each platform cell fixed fields, for example `where | concern ids | cite ids | basis (fact or reading) | evidence level`, with `;` between items.
  - Give `areas.tsv` separate label and citation columns, or a fixed separator, and allow several labels.
  - Have the coordinator create the files with headers before any part runs. Then either each part writes `parts/<part>/…` and the coordinator merges, or every row gets a `part` column.

### 18. No checker is named

- **Brief:** line 5, "The coordinator checks your rows".
- **Problem:** The brief names no checker and no tests, so the agent can't write to them, and the coordinator's check would be by hand.
- **What a checker would test, once findings 4, 9, 12 and 17 are fixed:**
  - **Format:** tab-separated, the header exact, the same number of columns on every row, no quotes, and no tab or newline inside a cell.
  - **Ids:**
    - `cap_id` matches `CM-<area_id>-\d{3}`, is unique, and its area matches `area_id`;
    - `area_id` is one of `km-areas.tsv`'s 41;
    - each concern id exists in its platform's `concerns.tsv` and sits in the right column (SH under shopify, SA under salla, ZD under zid, BC under bigcommerce, WC under woocommerce);
    - each citation id exists in that platform's `citations.tsv`.
  - **Placement cells:**
    - the first token is from the closed set;
    - a placed cell names at least one concern and one citation id, and each citation id backs a `where` statement of a named concern;
    - `not shown` names no concern, or names one with a `where` gap in `gaps.tsv`;
    - `absent` cites a list on the coordinator's list of complete lists, at its commit.
  - **Kind and commonality:** recomputed from the five cells by the table from finding 5, and compared with the row.
  - **Coverage:**
    - every concern of the five platforms is in `concern-areas.tsv`;
    - every row with a `cap_id` has its concern in that capability's cell for its platform, and every concern named in a cell has such a row.
  - **Joins:**
    - concerns that one `matches.tsv` row joins land in the same capability, or a stated reason says why not;
    - a capability joining concerns from an unclear candidate, or from Zid or BigCommerce, carries a reading mark.
  - **Exclusions and scope:**
    - no citation points into a `notes*.md` file;
    - a statement scoped to one country keeps that scope in the cell.
  - **What it can't test:** whether a reading is right. A quote check, like Q1's `method/check_concern_map.py`, can test that a label appears verbatim in its cited source.
- **Verdict: optional,** and recommended. Write the checker before the dry run, and name it in the brief.

### 19. As a product map, the output lacks what scoping records at breadth

- **Brief:** line 3 ("a product map of features against products"), lines 25 to 36 and line 50.
- **Problem:** Measured against product-line scoping's product map, and FODA's feature model, the output leaves out five things:
  - (a) whether a store's having the capability depends on its plan: the main variability in this class, and the brief's own definition of a capability ("a store … can have or not have");
  - (b) the evidence level and date of each cell (finding 6);
  - (c) a parent capability, so commonality can be read at two levels, such as "products" and "brands";
  - (d) dependencies between capabilities (requires and excludes);
  - (e) the variability type: whether a capability is optional, or one of several alternatives.
- **Evidence:**
  - SH-C-010's first-run `decides`: "custom user groups are a Plus row".
  - `measurements-2026-10-11.md`:
    - §3: "The shop carries 70 named entitlements, and 29 of them differ between the recording stores by plan", for example "`maximumLocations` is 2, 10 or 200";
    - §2: Salla's registry of 568 features, "349 of them list the plans they are on".
  - Zid's `structures/store-plan-policies/` ("every policy, whether it is enabled, its limits, and the plan it is available in"), and BigCommerce's `structures/plan-comparison`.
  - Dependencies: SH-C-037 is "Catalogs (market and B2B product and price catalogs)", so it depends on markets and on B2B companies.
- **Verdict:**
  - **(a) and (b) must fix,** because they change how commonality reads. Add a per-platform plan-gating field, cited (gated, not gated or not shown), and the evidence level.
  - **(c) to (e) optional.** A `parent` column is cheap now. Dependencies and variability type can wait for each area's model.

### 20. Size: CAT with STF in about 40 requests

- **Brief:** line 54, "Size: your message gives it."
- **The volume, at `95fd2916`:**
  - **Reading,** from concern names: 24 concerns sit squarely in CAT or STF.
    - Shopify: SH-C-020, -021, -037, -038, -189, -009, -010 and -011.
    - Salla: SA-C-020 to -023, -028 and -009.
    - Zid: ZD-C-083, -084, -100 and -094.
    - BigCommerce: BC-C-001 to -003 and -061.
    - WooCommerce: WC-C-064 and -080.
  - Those 24 carry 349 statements (about 120 KB, estimated from Shopify's rate) and about 700 inventory links, 310 of them on SH-C-010 alone.
  - A keyword sweep, with many false hits, gives an upper bound of 110 concerns and about 1,650 statements.
  - 9 unclear candidates touch the 24: U-002, U-005, U-010, U-013, U-015, U-059, U-070, U-081 and U-082.
  - Zid and BigCommerce need first joins (finding 3), and their labels need other-product-class's `structures/` (finding 11).
  - The clause "where a platform's own complete list says more" reaches, for STF alone:
    - observed-sh's `admin-permission-tree` (142 permissions), `admin-role-permissions` and `collaborator-access-permissions`;
    - observed-sa's `staff-permission-groups` and `dashboard-staff-roles`;
    - Zid's `store-permissions`.
- **Reading:**
  - Loading and filtering by script costs a few requests. The cost is judgement: about 15 to 25 capabilities, five cells each, plus joins, labels and qualities.
  - With concerns assigned in advance (finding 9), evidence-repository reads bounded to named structures (finding 11), and permissions not taken as capabilities (finding 4), CAT and STF fit in about 30 to 40 requests.
  - Without those bounds, STF's permission lists alone could use up the budget, and two agents would stop at different places.
  - CAT and STF are lighter than most pairs in concerns. Salla's storefront concerns alone, SA-C-091 (166 statements) and SA-C-090 (46), suggest SFR wouldn't fit beside another area.
- **Verdict: optional.**
  - Size parts from the pre-assignment, for example at most about 30 concerns or 400 statements per part.
  - Make the stop rule per area: finish one area's rows before starting the next, so a part that stops leaves only whole areas.

### 21. Whose labels count for WooCommerce, and what "shows an area" means

- **Brief:** line 23, "name the area in the platform's own words … An area a platform doesn't show is `not shown`".
- **Problem:**
  - WooCommerce runs on WordPress, and some areas, such as users and roles, are WordPress's. The brief doesn't say whether WordPress's words count as WooCommerce's.
  - The brief asks for one label, though platforms show several.
  - "Shows an area" isn't defined: one concern in the area, or a section in the platform's own navigation.
- **Evidence:** M-004's basis for WC-C-080: "WooCommerce adds two user roles—Customer and Shop Manager—and extends the existing Administrator role with store management capabilities."
- **Verdict: optional.**
  - Say that WordPress is the host: its labels go in the WooCommerce cell, marked as WordPress's.
  - Allow several labels per platform.
  - Define "shows an area" as at least one of its concerns, or one entry in one of the platform's own lists.
