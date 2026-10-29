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

## Re-inspection of A-assign and B-extent

**What this is:** brief A was replaced by two briefs, written against findings 1 to 21:
- `briefs/A-assign.md`, part 1: each concern's area, and each area's labels;
- `briefs/B-extent.md`, part 2: each area's product map.

This section says, for each finding, whether it is resolved, then gives the new problems, above all where part 1's output feeds part 2. It was read at `79ae9c27`, with the same rules as above. "A" and "B" give the two briefs' line numbers at that commit. The governing files are unchanged since `95fd2916`: `git diff` shows nothing for `founder-decisions.tsv`, `PLAN.md`, `STATE.md`, `CLAUDE.md` or `studies/concern-map/`, and the last decision is still dated 28 October.

**Counts:**
- **Findings 1 to 21:** 7 resolved, 13 partly resolved, 1 not resolved.
  - Six of the partly resolved still need a fix before either part runs: 4, 5, 7, 11, 14 and 16.
  - The other seven leave only an optional remainder, or a remainder now carried by a new finding.
- **New problems:** 13, of which 12 are must fix. N1 to N7 sit where part 1 feeds part 2.

### Findings 1 to 21: resolved or not

| # | Status | Why |
| --- | --- | --- |
| 1 | resolved | B lines 27 to 35: placement is read from `where` statements into six defined values, and "Each placement is a reading". `placements.tsv` is on neither read list. |
| 2 | partly | B lines 22 to 25 state Q1's rule (terms, identifiers or definitions), require both platforms' definitions for a join on role alone, mark it as a reading, and keep a match over an unclear candidate. Two things remain. "These rulings are engineering's" (B line 24) rests on no recorded decision, which is now finding 7. Joins on role alone go only to free-text `notes.md`, and no count is given without them; that part is optional. |
| 3 | resolved | B line 23 gives every Zid and BigCommerce concern the same test, and `single-platform.tsv` is on neither read list. But part 1's areas now limit which concerns those joins can reach (N4). |
| 4 | partly | B line 17 sets the lower bound, and line 19 makes permissions and the like evidence. But lines 17 and 18 contradict each other for a matched group whose members differ in grain. Must fix, below. |
| 5 | partly | (b) is resolved: `own service` includes "its own apps and extensions" (B line 29). (a) isn't: a row that mixes `extension point` and `outside` still has no kind, and the new `+` cells (B line 33) are counted by no rule. Must fix, below. |
| 6 | partly | `own`, `slot` and `shown` (B line 49) and `depth` (B line 40) answer the finding. `gaps.tsv` is still unread, so a `not shown` cell can't carry its gap's kind; that part is optional. B line 40's wording is a new problem (N8). |
| 7 | partly | (a) is resolved: both briefs state the task neutrally (A lines 3 to 5; B line 3, "It records what the platforms do"). (b) isn't resolved. (c) is moot, since neither brief cites the founder's slot rule any more. Must fix, below. |
| 8 | resolved | The seed's questions are left out (A line 9, B line 13). The seed's groupings are still given (A line 9), but A line 34's citation rule would catch an uncited copied label. Optional: say they are leads, not labels. |
| 9 | partly | Each concern gets one primary area from its `where` statements and own terms (A lines 19 to 21), with `also_in` for the others (A line 24). Per-part files remove the clash between one part's pointers and another's claims. What remains is new: N2, N3 and N12. |
| 10 | partly | Absence isn't recorded (B line 51), and `list` is described correctly (A line 12). But B line 51's "complete list" has no basis in part 2 (N6). |
| 11 | partly | The wrong pointer is gone: both briefs read only Q1 and the structures its statements cite (A line 36; B line 11, "at the commit each citation names"). But those commits sit in a file neither brief lists. Must fix, below. |
| 12 | resolved | A statement is now its concern id, cite id and identifier (A line 34, B line 35). That key is unique on Zid and BigCommerce. On Shopify (58 keys), Salla (64) and WooCommerce (47), a key can sit on two rows under two placements, such as `where` and `boundary`, so a checker can still find the key's `where` row. |
| 13 | resolved | `decides` is dropped, and `plan_gated` is recorded per cell (B lines 36 to 39). Its rule is a new problem (N9). |
| 14 | partly | Slot fillers are kept apart (B line 53), and "No market's name shapes a class or slot row" (B line 58). But scope is dropped from the cells. Must fix, below. |
| 15 | partly | `qualities.tsv` holds values, not capabilities (B line 52). Optional remainder: there's no `not stated`, and the limits Q1 holds outside its concerns can't be reached. Shopify's `maxProductVariants` and `maxProductOptions` carry no concern id, and their reason for being out of scope reads "values per store in notes.md, Unplaced keys". B line 13 excludes that file, and B line 9 reads only "your concerns' entries". |
| 16 | partly | (a): the `note` columns are now read (A line 14, B line 10), but they don't carry the README's flags, and B line 22 makes the two flagged matches stand. Must fix, below. (b) is resolved by B line 13. |
| 17 | partly | (a) `reading` per cell (B line 64), but its meaning is now unclear (N10). (b) labels, one row each with their own `cite` (A line 42): resolved. (c) `+` cells and `not shown (complete list: …)`: resolved. (d) and (e): per-part files and the coordinator's merge (A line 38, B line 59), but the merge is unspecified (N1). Optional: the `evidence` field's format, and an order for `capabilities.tsv`'s columns, which are listed across B lines 43 to 49. |
| 18 | not resolved | Neither brief names a checker or its tests. Optional, as before. |
| 19 | partly | (a) `plan_gated` (B line 36), though its rule slants (N9). (b) `depth`, per platform rather than per cell (B line 40). (c) `parent` (B line 43): resolved. (d) and (e) are deferred, which is optional. |
| 20 | resolved | Part 2 is bounded: part 1 assigns the concerns first, reads are limited to Q1 and the structures it cites, permissions are evidence, and the size is about 20 requests per area (B line 69). Optional remainder: part 1's 60 requests (A line 45) fit one or two platforms, not three. Shopify alone has 198 concerns and 495 `where` rows, and Salla 152 and 465. |
| 21 | resolved | Several labels are allowed (A line 28), WordPress has a rule (A line 29), and `not shown` is defined (A line 30). Optional remainder: A line 27 takes labels from four kinds of list, but A line 30 tests any list. |

### What still needs fixing from findings 1 to 21

**4. One capability per matched group, or one per concern at the finest grain?**
- **Brief:** B line 17, "A capability is one of Q1's matched groups, or one unmatched concern". B line 18, "Where two platforms cut at different grains, the coarser concern covers several capabilities."
- **Problem:** For a matched group whose members differ in grain, line 17 gives one capability and line 18 gives several. Two agents following the brief would build different rows.
- **Evidence:** M-011 is one matched group: SH-C-020, SA-C-020 to SA-C-023, and WC-C-064. Its `granularity` reads "Salla splits products …, options and variants …, categories … and brands …; … Shopify … has no brands concern".
  - As one capability, Shopify's cell is `core`, and Shopify counts for brands.
  - As four capabilities, Shopify's cell for brands is `not shown`.
- **Verdict: must fix.** Say which grain wins. For example: a matched group splits into one capability per concern of its finest platform, and each coarser concern appears in all of them, marked `(part)`.

**5. Rows and cells that no kind or count covers.**
- **Brief:** B line 33, "two of these joined by `+`". B lines 46 to 49, the kinds and counts.
- **Problem:**
  - A row whose shown cells mix `extension point` and `outside`, with no `core` or `own service`, has no kind.
  - B doesn't say whether a `+` cell such as `core+extension point` counts as `core`, as `extension point` or as both, either for `kind` or for `own` and `slot`.
- **Evidence:** B's own rules at lines 46 to 49: "any cell is `core` or `own service`", "every shown cell is `extension point`", "every shown cell is `outside`".
- **Verdict: must fix.** Give the full table. A `+` cell counts toward each of its parts. A row with only `extension point` and `outside` cells gets a kind of its own, such as `mixed`.

**7(b). The step still rests on no recorded decision, and B now hands the founder's unclear list to engineering.**
- **Brief:** B line 24, "These rulings are engineering's, and the coordinator checks each one."
- **Problem:** Q1 reserves its unclear candidates for the founder, and no recorded decision moves them. The step itself has no stage in `PLAN.md`.
- **Evidence:**
  - Q1 line 127: "Every unclear match … goes on a list for the founder. Neither that pass nor the coordinating session settles them."
  - 81 of the 84 unclear candidates name the founder in `what_would_settle_it`.
  - `founder-decisions.tsv`, `PLAN.md` and `STATE.md` are unchanged since `95fd2916`. The last decision is dated 28 October.
- **Verdict: must fix.** Before either part runs:
  - record the founder's decision of 29 October, with what it says about the unclear list;
  - add the stage to `PLAN.md`.

  Until then, B line 24's rulings are proposals for the founder.

**11. The commit to read a structure at is in `citations.tsv`, which neither brief lists.**
- **Brief:** B line 11, "the structures Q1's statements cite, read at the commit each citation names". A line 36.
- **Problem:** `statements.tsv` gives the structure but not the commit, and Shopify's citations use two commits. Without `citations.tsv`, an agent reads whatever commit the clone has checked out, which is a later one.
- **Evidence:**
  - Shopify's `structure` values never carry a commit (0 of 3,005 rows). For example, `structures/shopify/admin-router` appears without one, while its citation SH-S-5006 is `observed-sh@e49840729:structures/shopify/admin-router/items…`.
  - Shopify's citations are at `b46731d0` (2,315) and `e49840729` (1,732). The clone's head is `19a5f6435`.
  - Only Salla's `structure` values carry the commit (2,244 rows, `observed-sa@145f137:…`).
- **Verdict: must fix.** Add each platform's `citations.tsv` to both read lists, and say: "read a structure at the commit in its citation's `source`, with `git show <commit>:<path>`".

**14. Cells carry no scope.**
- **Brief:** B line 64, the columns of `capability-cells.tsv`. B line 58.
- **Problem:**
  - Brief A's rule, "A capability scoped to one country by a platform keeps that scope in its citation", isn't in B, and the cells have no `scope`. A capability a platform states for one country, plan or store would read as general.
  - Nothing says that a market's law built into a platform's own core is a scoped `core` cell, not a slot filler.
- **Evidence:**
  - Q1 line 74: scope is recorded "as stated: a store, plan, country or role".
  - Statements with a scope: Shopify 445 of 3,005, Salla 841 of 2,560, Zid 175 of 654, BigCommerce 60 of 473, WooCommerce 379 of 1,499.
- **Verdict: must fix.**
  - Add `scope` to `capability-cells.tsv`, from the cited statements' `scope` column.
  - Say that a market's law or provider in a platform's own core is `core`, with its scope, and goes in `slot-fillers.tsv` only where it fills a slot.

**16(a). "Q1's matches stand" settles the two matches the README put to the founder.**
- **Brief:** B line 22, "Q1's matches stand". B line 10, the `note` columns.
- **Problem:** The README's flags aren't in the `note` column, so reading the column doesn't surface them, and B line 22 then makes both matches stand.
- **Evidence:**
  - Concern-map `README.md` line 30: "The matching agent flagged M-070 … and M-064 … Both rest on a shared main word."
  - M-064's note reads only "Basis kind: term. Each is the platform's own chat with customers."
- **Verdict: must fix.** Name M-064 and M-070 in B as flagged, and give them B line 24's test, both platforms' definitions, before they stand.

### New problems

**N1. The merge between the parts is unspecified.**
- **Brief:** A lines 38, 41 and 42: part 1 writes `parts/<part>/concern-areas.tsv` and `area-labels.tsv`. B line 7: part 2 reads `studies/class-model/areas.tsv` and `concern-areas.tsv`.
- **Problem:** The file names differ (`area-labels.tsv` against `areas.tsv`), the merged files' columns are given nowhere, and nothing says how the merge settles:
  - two parts that put matched concerns in different areas;
  - new areas a part proposes, which part 2's messages would have to name;
  - assignments marked `reading: yes`.
- **Evidence:** the briefs' own lines, as cited.
- **Verdict: must fix.** Specify the merge before part 1 runs:
  - the merged files' names and columns;
  - how a conflict is settled, and by whom;
  - how a new area is accepted;
  - a check after the merge: each concern has exactly one primary area, and every area part 2 will be sent exists.

**N2. Part 1 is split by platform, but its rule for matched concerns needs all of them.**
- **Brief:** A lines 10, 19 and 27, "your part's platforms". A line 25, "Matched concerns … share an area, unless their platforms' own organizations put them apart."
- **Problem:** An agent with one platform can't see the area another part gave the other members of a match, so it can't apply the rule.
- **Evidence:** `matches.tsv` joins Shopify, Salla and WooCommerce in 88 groups. In 27 of them, one platform's cell holds several concerns.
- **Verdict: must fix.** Give Shopify, Salla and WooCommerce to one part, or have the coordinator apply A line 25 at the merge (N1).

**N3. Assigning by "where the platform puts it" scatters matched groups and moves slots out of their subject's area.**
- **Brief:** A lines 19 and 20, "by where the platform itself puts it: its `where` statements: an admin section or route, an API group, an app category, a help section". A line 25's exception.
- **Problem:** Where a platform places a concern differs from what the concern is about.
  - Assigning by placement sends the platform that leaves a capability to apps into APP, while the platforms that build the same capability land in its subject's area.
  - Part 2 then sets the subject area's `core` cells against `not shown` for the platform that leaves it to apps. That platform's slot becomes a single-platform row in APP.
  - A line 25's exception allows exactly this split.
  - Nothing breaks a tie when one concern's `where` rows point to different areas.
- **Evidence:**
  - M-065 joins three platforms' product reviews:
    - SH-C-154 (Shopify), every one of whose `where` rows comes from the app store;
    - SA-C-030 (Salla);
    - WC-C-065 (WooCommerce), whose `where` row reads "Products > Reviews", from `src/Internal/Admin/ProductReviews/Reviews.php`.
  - Zid's ZD-C-086 `where` row reads "Merchant APIs > Products > Product Questions & Answers".
  - The seed puts Shopify's "Reviews" and Salla's "Reviews & questions" in SUP (`km-areas.tsv` line 20).

  So this one capability could land in APP, CAT and SUP. 14 Shopify concerns are placed only through the app store, among them SH-C-111, -126, -137, -154, -185 and -187. Salla and Zid have 2 each, and BigCommerce 1.
- **Verdict: must fix.**
  - Assign by subject: what the concern is about, from its own terms and the section it serves. `where` statements are evidence of the subject, never the area themselves.
  - APP keeps only the app mechanism: the app store, app billing and the extension frameworks.
  - A matched group takes one area, with the others in `also_in`.
  - Give a tie-break, for example the subject of the concern's first `where` row in the platform's admin or API organization.

**N4. Zid's and BigCommerce's joins can happen only inside the area part 1 chose.**
- **Brief:** B line 7, "the concerns assigned to them, both primary and `also_in`". B line 23.
- **Problem:** Zid and BigCommerce were never matched, so the area part 1 gives each of their concerns decides which concerns part 2 can join it with. A Zid concern placed in a different area from its counterpart is never compared, and each becomes a capability with one platform. **Reading:** the error would lower `own` and `shown`, and nothing would show it.
- **Evidence:** Q1 line 116, "stops before matching". `matches.tsv` holds no ZD- or BC- id.
- **Verdict: must fix.** Either let part 2 search all five platforms' `concerns.tsv` for counterparts, by terms, identifiers or definitions, and record each concern it brings in from another area. Or have the coordinator run one pass across areas for Zid and BigCommerce before part 2.

**N5. A concern under `also_in` has no owner in part 2.**
- **Brief:** B line 7.
- **Problem:** Each part 2 agent receives its areas' primary and `also_in` concerns, but nothing says whether an `also_in` concern builds a capability in its second area. The same concern can then become a capability in two areas, counted twice in `own`, `slot` and `shown`, or in neither.
- **Evidence:** SH-C-037, "Catalogs (market and B2B product and price catalogs)", fits CAT, B2B and MKS.
- **Verdict: must fix.**
  - The part for the concern's primary area owns its capability.
  - A part for a second area refers to that capability by `cap_id`, or builds a separate capability from a part of the concern, marked `(part)`.
  - The merge checks that no concern sits in two capabilities without that mark.

**N6. What part 1 reads about lists never reaches part 2.**
- **Brief:**
  - A line 15: each platform's `notes.md`, "only for where each of its lists stops";
  - B line 13, which excludes `notes*.md`;
  - B line 51: `not shown (complete list: …)`.
- **Problem:** Part 1 reads where each list stops, but neither of its outputs records it. Part 2 is asked to name complete lists, and can't read the files that say where they stop.
- **Evidence:** all five `notes.md` say where their inventory stops. Shopify, Salla, Zid and WooCommerce have a section "Where the inventory stops", and BigCommerce has a paragraph so headed in "Lists used and their sizes" (line 35).
- **Verdict: must fix.** Have part 1 write `lists.tsv` for part 2 to read, with the platform, the list, whether it is complete (`yes`, `no` or `not stated`), where it stops, and the citation. Or drop B line 51's clause.

**N7. `not shown` mixes "no concern" with "a concern with no `where` statement".**
- **Brief:** B line 32, "`not shown`: Q1 holds no statement on it". B line 49, `shown`.
- **Problem:** A platform that has the concern but no `where` row for it shows the capability. Yet its placement can only be `not shown`, and `shown` counts it as not showing.
- **Evidence:** concerns with no `where` row: Shopify 11, Salla 8, WooCommerce 10, Zid 1, BigCommerce 1.
- **Verdict: must fix.** Define `not shown` as "no concern of the platform in the capability". A concern without a `where` row gets `where not stated`, and counts as shown.

**N8. "So `not shown` on Zid or BigCommerce isn't absence" implies that on the other three it is.**
- **Brief:** B line 40.
- **Problem:** The sentence invites reading `not shown` on Shopify, Salla or WooCommerce as absence. That contradicts Q1's rule 6 (Q1 line 89) and B's own line 51. Salla is marked `full`, though most of its gaps are pages not read.
- **Evidence:** 206 of Salla's 230 gaps are `page not read`.
- **Verdict: must fix.** Write: "`not shown` is never absence, on any platform. `depth` says how much of the platform Q1 read." Consider giving each platform's count of gaps by kind beside its depth.

**N9. `plan_gated: yes` fires when a statement names a plan or entitlement, not when the plan gates the capability.**
- **Brief:** B lines 36 to 39.
- **Problem:** Shopify's admin router names an entitlement for most pages, including features every plan has. So `yes` fires where `no` also applies, and B gives no precedence between them. **Reading:** Shopify would read as plan-gated far more often than the platforms whose plan tables list only what differs. WooCommerce has no plans, so it can only be `not shown`.
- **Evidence:**
  - On 43 Shopify concerns, a `decides` row names an entitlement.
  - SH-C-020, products: `"eligibility":{"permissions":["PRODUCTS"],"entitlements":["products"]}`, and `entitlements.products` is `true`, scoped to recording stores including a trial store (`2jiwxs-gr (trial); capture-adv…`).
  - `measurements-2026-10-11.md` §2: "WooCommerce. No plans".
- **Verdict: must fix.**
  - `yes` only where a statement shows a value that differs between plans, or a plan without the capability.
  - `no` where statements show it on every plan.
  - `n/a` for a platform with no plans.
  - `partly` where only part of the capability is gated. For example, Shopify's first run recorded "custom user groups are a Plus row" for SH-C-010.

**N10. The `reading` column has no meaning left.**
- **Brief:** B line 35, "Each placement is a reading". B lines 57 and 64.
- **Problem:** Every placement is a reading, so `reading` would be `yes` on every cell, or some agents would use it only for joins on role alone.
- **Evidence:** the brief's own lines.
- **Verdict: must fix.** Say that `reading` marks the join: `no` for a Q1 match or a join on terms, identifiers or definitions, and `yes` for a join on role alone. The placement is always a reading.

**N11. No column ties concerns to capabilities, and part 2 has no coverage rule.**
- **Brief:** B lines 43 and 64. B line 74, "the concerns not placed".
- **Problem:** Concern ids appear only inside the free-form `evidence` field, and nothing requires every concern assigned to a part's areas to land in a capability. Coverage can't be checked without parsing prose.
- **Evidence:** the brief's own lines.
- **Verdict: must fix.**
  - Add `concern_ids` to `capability-cells.tsv`.
  - Require every primary concern of a part's areas to be in at least one capability, or listed in `notes.md` as not placed.
  - Check coverage across the merged parts.

**N12. The seed's areas beyond the references can absorb concerns, and drop them from the extent.**
- **Brief:** A line 19, "one area from the seed". A line 35, "No market's facts shape an area".
- **Problem:** The seed's 41 areas include WLD ("World and market context"), ENG, INT and MTH, none of which is an area of the platforms. A concern that no commerce area names could be given WLD, and so could a market's law built into a regional platform's core. If no part 2 message names WLD, those concerns fall out of the extent.
- **Evidence:**
  - `km-areas.tsv` lines 39 to 42.
  - M-001 joins the contracting entity and governing law: SH-C-002, SA-C-230, WC-C-023 and WC-C-026.
- **Verdict: must fix.** Allow areas from domains A to G only. A concern that fits none of them gets a proposed new area.

**N13. `area-labels.tsv` has no `reading` column.**
- **Brief:** A lines 34 and 42.
- **Problem:** Placing a platform's label under a seed area is a reading, which A line 34 asks to be marked, but the file has no column for it.
- **Verdict: optional.** Add `reading`.

## The coordinator's disposition (29 October 2026)

Two inspections found 39 problems a run would have hit. Most of the new ones came from the rules added to fix the old ones. The worst came from splitting the work into two parts:
- areas assigned per platform before the platforms were joined (N2 to N5);
- a merge between the parts that was never specified (N1).

That is the founder's point about process machinery, seen in this brief. So the step changes shape rather than gaining more rules.

**One brief, one domain per part, all five platforms at once.**
- Each part reads all 652 concerns, about 22,000 tokens, and takes its domain's.
- Joining and choosing the area happen together, so matched concerns can't be scattered (N2 to N5), and Zid and BigCommerce are joined where the others are (finding 3).
- The coordinator merges the parts with a check that each concern is taken exactly once (N1, N5, N11). Areas beyond the references take no capabilities (N12).

**The rules kept are the ones that tie claims to evidence:**
- **Words and citations:** the platform's own words, and each claim cited by concern id, cite id and identifier (finding 12).
- **Readings:** each one marked (N10).
- **Scope:** each statement's scope kept (finding 14).
- **Absence:** "Q1 holds nothing" never means absence (findings 10, N7 and N8).
- **Commits:** sources are read at the commits in `citations.tsv` (finding 11).

**Left to the part's judgment, as readings explained in its notes:**
- the grain of capabilities (finding 4);
- joins on role (finding 2);
- the area where platforms differ (N3).

A dry run on one domain shows how the judgments come out. Its output is reviewed against the evidence by an agent that made none of it. The conventions are codified from that, with a checker, before the other domains run (finding 18).

**Answered elsewhere:**
- **The kind and the counts** are computed by the coordinator from the cells after the merge, by one rule applied to all (findings 5 and 6).
- **Plan gating** waits for each area's detail, so the extent doesn't claim it from a named entitlement (N9).
- **The matches the concern map flagged for the founder,** M-064 and M-070, and Q1's unclear list, become engineering's under the founder's intent, once it is recorded (finding 16a; 7b). Each join on role is listed for the coordinator to check.
- **The founder's decision and the plan's stage** come first, on the founder's go (finding 7). The dry run doesn't start before them.
