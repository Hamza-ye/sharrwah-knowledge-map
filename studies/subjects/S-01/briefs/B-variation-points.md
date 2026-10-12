# Brief: S-01, variation points and variants (pilot, step 1, phase B)

This is `PLAN.md` Stage 2, the pilot. You are one agent with one task.

**Read only this brief and:**
- the five platforms' phase A outputs in `studies/subjects/S-01/{shopify,salla,woocommerce,zid,bigcommerce}/`, which hold `statements.tsv`, `terms.tsv`, `absences.tsv`, `gaps.tsv` and `citations.tsv`;
- `studies/subjects/S-01/kinds.tsv`, which gives each statement's kind by rule.

Don't read `notes.md` files or any `note` column.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

Phase A collected what each platform states about the merchant's money between the two ends, under five bullets:
- **(a)** who or what holds or controls it;
- **(b)** under whose account, licence or terms it is held;
- **(c)** when, or on what conditions, it is released to the merchant or held back;
- **(d)** that the platform has no part in it;
- **(e)** where, or for whom, an arrangement under (a) to (c) is offered.

Statements under (e) are conditions, not variants. Phase D reads them.

**Your task:** split the subject into variation points, and place each platform's statements under them as variants. Don't judge the variants, and don't give causes; a later phase does that.

## Rules

1. **Candidates.** Each statement that says who or what fills some X under bullets (a) to (c) gives one candidate for each of those bullets it carries. Its X is quoted from that statement.
2. **Variation points.** Candidates from different statements are one variation point when their X matches on one of the bases in rule 4.
   - Each variation point keeps the bullet of its statements.
   - Its question takes the form "who or what fills X", with X quoted from one of the statements in `raised_by`.
   - `x_words` lists each raising platform's own words for X.
   - **Merging.** Two variation points answered by exactly the same statements are merged. List each merge in `notes-b.md`.
3. **Variants.** For each variation point and each platform, give one row per distinct answer the platform gives, with its own `variant_id`. An answer's `variant` excerpt names the who or what that fills X. Two answers are distinct when their excerpts name a different who or what. A row takes one of four forms:
   - **an answer:** `variant` is an excerpt of one of its statements, verbatim;
   - **`absent`:** the platform's `absences.tsv` shows it absent from a complete list, under the variation point's bullet, with those `absence_ids`. Its `kind` is the kind of the list's citation;
   - **`gap`:** the platform's gaps under the same bullet cover it, with those `gap_ids`;
   - **`not covered`:** the platform has none of these. These rows go back to that platform for gap-closing (phase A2). List them in `notes-b.md`.

   A bullet (d) statement, that the platform has no part, is the platform's variant for each variation point it applies to, with the basis `answers`.
4. **Matching.** Compare each statement with a statement in the variation point's `raised_by`. Record every basis that holds, with the words that show it in `basis_evidence`:
   - `term`: the same term, including a platform's own translation from `terms.tsv`. It fails when the two platforms' definitions in `terms.tsv` differ.
   - `identifiers`: the same key, scope, topic or entitlement;
   - `definition`: the same definition, with both quoted;
   - `answers`: the statement says who or what fills the variation point's X, in words that name the same X.

   A statement goes under a variation point only if at least one basis holds. When it only partly matches, split the variation point rather than force the match.
5. **Kind and scope.**
   - `kind` is copied from `kinds.tsv` for each statement of the variant. List each if they differ.
   - `scope` is as the statements give it.
6. **No inference,** no ranking and no causes, anywhere, including notes.
7. **Stop and report** past 25 variation points.

## Second pass, after phase A2

When the coordinator says phase A2 is done, revisit every row that was `gap` or `not covered`. The second pass adds no variation point and splits none. A statement that fits no existing variation point is listed in `notes-b.md`.
- replace it with variants from the statements A2 added, under the rules above;
- or make it `absent`, with A2's `absence_ids`;
- or keep it as `gap`, with A2's `gap_ids`.

Record what changed in `notes-b.md`.

## Output, in `studies/subjects/S-01/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `variation-points.tsv` | `vp_id` (S01-VP-01…) · `bullet` · `question` · `x_words` · `raised_by` (stmt_ids) · `note` |
| `variants.tsv` | `variant_id` (S01-V-001…) · `vp_id` · `platform` · `variant` (an excerpt, `absent`, `gap` or `not covered`) · `stmt_ids` · `basis` (every basis that holds, `;`-separated) · `basis_evidence` · `kind` · `scope` · `gap_ids` · `absence_ids` · `note` |
| `notes-b.md` | Merges; partial overlaps that were split; `not covered` rows; problems with the method. |

Write the files as you go: if you are interrupted, the next run continues from them.
