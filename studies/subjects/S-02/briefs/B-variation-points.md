# Brief: S-02, variation points and variants (step 1, phase B)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task: one root decision, which the message that started you names. Two other agents work on the other two, each in its own folder.

**Read only this brief and, in `studies/subjects/S-02/`:**
- `bullets.tsv`, the questions phase A asked of each platform;
- your root decision's slice, `slices/<root decision>/`, cut from the five platforms' phase A files by `method/subject_slice.py`:
  - `statements.tsv`: every statement under one of your decision's bullets, with its `platform` and its `kind` (by rule, from `kinds.tsv`);
  - `gaps.tsv` and `absences.tsv`: those under your decision's bullets, with their platform (and an absence's kind);
  - `terms.tsv`: every platform's terms;
- in the second pass, each platform's `a2.tsv` and `absence-audit.tsv`.

Don't read the platforms' own folders (apart from `a2.tsv` and `absence-audit.tsv` in the second pass), `notes.md` files, `recorded.tsv` files, or any `note` column. The slices hold no notes.

**Large slices:** look rows up with grep or a short script where you can, rather than reading a slice whole more than once.

## The subject

> What fills "a market": which settings bind per market, and who sets each?

**Its three root decisions** (`PLAN.md`, section 6, step 1):
- **RD1, the store's own country:** what fills a store's country; who sets, checks and changes it; what binds to it; and the countries a platform serves.
- **RD2, the markets a store sells into:** what defines one, how many a store can hold, and who creates them.
- **RD3, what binds per market, and who sets it:** which settings take a value per market, which hold for the whole store, and which the platform sets and which the seller.

Phase A collected what each platform states under eight bullets. Each bullet belongs to a root decision, as `bullets.tsv` says:
- **(a)** to **(d)**, RD1: what fills the store's own country; who sets, checks or changes it; what the platform binds to it; the countries the platform serves;
- **(e)**, RD2: what defines a market a store sells into, how many it can hold, and who creates one;
- **(f)**, RD3: a setting that takes its value per market, whether the store's own country (as in (a)) or a market it sells into (as in (e)), or per buyer's country; and who sets that value;
- **(g)**, RD3: that a setting holds for the whole store, or that the platform has no market of the kind in (e);
- **(h):** where, or for whom, what a statement under (a) to (f) describes is offered.

Statements under (h) are conditions, not variants: a variant rests on at least one statement under (a) to (g). A later step reads the conditions.

**Lists.** Where a source holds a list's items apart, phase A made one statement per run of items, each with the list's own identifier. Read a list's statements together by that identifier.

**Your task:** split each root decision into the facets that can change it, as variation points, and place each platform's statements under them as variants. Don't judge the variants, and don't give causes; a later phase does that.

## Rules

0. **Same.** In these rules, two things are the same when they use the same words, or a platform's own translation of them in `terms.tsv`, or name the same party or identifier. Quote what shows it. Two platforms agree on a variation point when their sets of answers are the same.
   - **Without the platform's translation,** `answers` may rest on your translation of the platform's words. Quote them, and mark the translation as yours in `basis_evidence`.
1. **Candidates.** Each statement that says who or what fills some X under bullets (a) to (f) gives one candidate for each of those bullets it carries. Its X is quoted from that statement.
   - Under (b), the party, time or condition the statement gives is what fills its X.
   - Under (c), X is the thing the platform binds, in the statement's own words, such as a contracting party, documents, or a payment service; and the variant names what decides it: the store's country, its location, its billing address, the business's registered country or a business entity, in the statement's own words.
   - Under (f), X is the setting, in the statement's own words, and the variant names what it takes its value per, among three kinds: the store's own country, a market the store sells into, or the buyer's country; or who sets it.
2. **Variation points.** Candidates from different statements under the same bullet are one variation point when their X matches on one of the bases in rule 4.
   - Each variation point keeps the bullet of its statements, and so its root decision.
   - Its question takes the form `who or what fills "X"`, with X in double quotes, quoted from one of the statements in `raised_by`. Under (c), it takes the form `what decides "X"`: what fills the role of deciding the thing bound, which is how a platform's binding to a store's country shows.
   - `x_words` lists each raising platform's own words for X.
   - **Merging.** Two variation points under the same bullet, answered by exactly the same statements, are merged. List each merge in `notes-b.md`.
   - **Facets of a root decision** (`PLAN.md`, Stage 4). Every variation point is a facet that can change its root decision: its answers, as its bullet asks, could change what the root decision must hold. A candidate that isn't goes in `notes-b.md` with its statement ids, as a note. Apply this to every candidate, matched or not.
3. **Variants.** For each variation point and each platform, give one row per distinct answer the platform gives, with its own `variant_id`. An answer's `variant` excerpt names the who or what that fills X. Two answers are distinct when their excerpts name a different who or what. A row takes one of four forms:
   - **an answer:** `variant` is an excerpt of one of its statements, verbatim;
   - **`absent`:** the platform's `absences.tsv` shows it absent from a complete list, under the variation point's bullet, with those `absence_ids`. Its `kind` is the kind `kinds.tsv` gives for those absences;
   - **`gap`:** the platform's gaps under the same bullet cover it, with those `gap_ids`;
   - **`not covered`:** the platform has none of these. These rows go back to that platform for gap-closing (phase A2). List them in `notes-b.md`.

   A bullet (g) statement, that a setting holds for the whole store, or that the platform has no market of the kind in (e), is the platform's variant for each variation point it applies to, with the basis `answers` alone.
4. **Matching.** Compare each statement with a statement in the variation point's `raised_by` from another platform, where there is one. Record every basis that holds, with the words that show it in `basis_evidence`:
   - `term`: the same term, including a platform's own translation from `terms.tsv`. It fails when the two platforms' definitions in `terms.tsv` differ.
   - `identifiers`: the same key, scope, topic, field or entitlement;
   - `definition`: the same definition, with both quoted;
   - `answers`: the statement says who or what fills the variation point's X, in words that name the same X.
     - `answers` rests on what the statement says, not on shared words. Its own words must name what fills X in X's role in the root decision: under (a) to (d), the store's own country and what the platform holds, checks or binds to it; under (e), a market the store sells into; under (f), the value a setting takes per market, or who sets it. `basis_evidence` quotes those words and says which role they name. One that names something outside that role doesn't answer: a country a buyer ships to is not the store's own country, and a setting of the platform's own account is not a store's setting. The role test holds whatever a variant's basis, since shared words can be homonyms: "market", "country" and "region" name different things on different platforms.
     - A variant whose words name only what is kept out of X's role is not an answer variant. It goes in the variation point's `note`, and if no other variant of the platform answers, the platform's answer is a `gap` (the pilot's ruling of 25 October 2026, on its review's finding 36).

   A statement goes under a variation point only if at least one basis holds. When it only partly matches, split the variation point rather than force the match.
5. **Kind and scope.**
   - `kind` is copied from `kinds.tsv` for each statement of the variant. If they differ, list each, `;`-separated.
   - `scope` is as the statements give it. If they differ, list each scope with its `stmt_ids`, `;`-separated.
6. **No inference,** no ranking and no causes, anywhere, including notes.
7. **Write as you go.** Write each variation point and variant to the files as soon as it is placed. If you are stopped, your files must hold everything done so far, and the next run continues from them.
8. **Stop and report** past 15 variation points of your own.

## Second pass, after phase A2

When the coordinator says phases A2 and A3 are done, read each platform's `a2.tsv` and `absence-audit.tsv`. Revisit every row that was `gap`, `absent` or `not covered`, and each arrangement A2 was given. Recheck, under rule 4, any row you compared with a statement of its own platform. The second pass adds no variation point and splits none. A statement that fits no existing variation point is listed in `notes-b.md`. For each row revisited:
- replace it with variants from the statements A2 added, under the rules above;
- or make it `absent`, with A2's `absence_ids`;
- or keep it as `gap`, with A2's `gap_ids`.

Record what changed in `notes-b.md`.

## Output, in `studies/subjects/S-02/b/<root decision>/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. Each root decision has its own range of ids, so the three folders can be joined:

| Root decision | Variation points | Variants |
| --- | --- | --- |
| RD1 | S02-VP-01 to S02-VP-29 | S02-V-001 to S02-V-299 |
| RD2 | S02-VP-30 to S02-VP-49 | S02-V-300 to S02-V-499 |
| RD3 | S02-VP-50 to S02-VP-79 | S02-V-500 to S02-V-899 |

| File | Columns |
| --- | --- |
| `variation-points.tsv` | `vp_id` · `bullet` (one of your decision's bullets from `a` to `f`) · `question` · `x_words` · `raised_by` (stmt_ids) · `note` |
| `variants.tsv` | `variant_id` · `vp_id` · `platform` (`shopify`, `salla`, `woocommerce`, `zid` or `bigcommerce`) · `variant` (an excerpt, `absent`, `gap` or `not covered`) · `stmt_ids` · `basis` (every basis that holds, `;`-separated) · `basis_evidence` · `kind` · `scope` · `gap_ids` · `absence_ids` · `note` |
| `notes-b.md` | Merges; partial overlaps that were split; candidates kept as notes; `not covered` rows; problems with the method. |

**Before you finish,** check your files on a copy:
1. Copy `studies/subjects/S-02` to `<a folder in your scratchpad>/S-02`.
2. Run `python3 -I method/merge_slices.py <that folder>/S-02 b`, which joins whatever `b/` folders exist into the copy's `variation-points.tsv` and `variants.tsv`.
3. Run `python3 -I method/check_subject.py <that folder>/S-02 <an output folder> $(ls -d evidence/product-class/runs/*)` from the repository's root.
4. Fix, in your own `b/<root decision>/` folder, every line of level `error` on one of your ids. Lines on the other decisions' ids, and the line listing statements under no variation point, are for the coordinator, who joins the three when all are done.
