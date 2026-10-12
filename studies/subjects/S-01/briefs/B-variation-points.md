# Brief: S-01, variation points and variants (pilot, step 1, phase B)

This is `PLAN.md` Stage 2, the pilot. You are one agent with one task. Read only this brief and the five platforms' phase A outputs:
`studies/subjects/S-01/{shopify,salla,woocommerce,zid,bigcommerce}/`, which hold `statements.tsv`, `terms.tsv`, `gaps.tsv`, `citations.tsv` and `notes.md`.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

**The interval** starts when a buyer pays for an order. It ends when the money reaches an account the merchant holds outside the platform.

**Your task:**
1. Split the subject into variation points.
2. Place each platform's statements under them as variants.

Don't judge the variants, and don't give causes. A later phase does that.

## Rules

1. **Variation point.** A question of the form "who or what fills X". X is one thing that, in the statements, some party or mechanism does, holds, decides or answers for during the interval.
   - A variation point exists only if at least one platform's statement says who or what fills X. That statement raises it.
   - **Merging.** If two candidate variation points are always answered by the same statements, merge them, and list the merge in `notes-b.md`.
   - **One statement, several points.** A statement that answers two variation points is listed under both.
2. **Variant.** For each variation point and each platform, give one of three things:
   - the platform's answer in its own words, as a short excerpt or the identifier, with its `stmt_ids`;
   - `gap`, with the platform's `gap_ids` that cover it;
   - `not covered`, when the platform's phase A outputs neither state it nor record a gap. List these in `notes-b.md` as a coverage problem.
3. **Matching.** A statement goes under a variation point only on one of four bases. Name the basis in the row:
   - `term`: the same term, including a platform's own translation of it, quoted from the platforms' `terms.tsv`;
   - `identifiers`: the same key, scope, topic or entitlement;
   - `definition`: the same definition, with both quoted;
   - `answers`: the statement answers the variation point's question directly.

   **Partial overlap.** When a statement only partly matches, split the variation point rather than force the match.
4. **Kind.** Each variant has a kind, taken from its citations' sources:
   - `observed`: a recorded store or journey (observed-sh or observed-sa run records, and structures recorded from a store's answers);
   - `shipped`: code or a schema the platform ships (the WooCommerce release, API schemas, app bundles);
   - `stated`: docs and help pages;
   - `official page`: terms, policies, legal and pricing pages.

   If a variant's citations differ in kind, list each.
5. **Scope** is as the statements give it.
6. **No inference,** no ranking and no causes. A note may hold inference, starting with "Inference:", and it never counts.
7. **Stop and report** past 25 variation points.

## Output, in `studies/subjects/S-01/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `variation-points.tsv` | `vp_id` (S01-VP-01…) · `question` · `raised_by` (stmt_ids) · `note` |
| `variants.tsv` | `vp_id` · `platform` · `variant` (the platform's own words, `gap` or `not covered`) · `stmt_ids` · `basis` · `kind` · `scope` · `gap_ids` · `note` |
| `notes-b.md` | Merges; partial overlaps that were split; coverage problems; problems with the method. |

Write the files as you go: if you are interrupted, the next run continues from them.
