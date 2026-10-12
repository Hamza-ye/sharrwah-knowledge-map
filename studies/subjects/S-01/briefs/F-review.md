# Brief: S-01, independent review (pilot, step 5)

This is `PLAN.md` Stage 2, the pilot. You review what other agents and the coordinator produced for one subject. You did not produce any of it. You change nothing; you report.

**Read only this brief and:**
- everything in `studies/subjects/S-01/`, and of `briefs/` only `C-analysis.md`, for its rule table;
- the row files E placed, `register/pay-questions.tsv` and `register/km-questions.tsv`, only the columns `id`, `question`, `needed_by` and `lane`;
- Stage 1's output in `studies/yemen-cases/`;
- the sources those files cite, to check them.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

## What to check

1. **Readings.** Does each cause reading in `analysis.tsv` follow from the statements it cites? Read the statements, and their sources where the excerpt is short.
2. **Coexistence and what follows.** Do they follow from the cited statements, and is every rule in `follows` one that applies under the rule table in `briefs/C-analysis.md`, with none missing?
3. **Marks.** Do the two pieces of evidence for each mark in `yemen-marks.tsv` show what the mark claims?
4. **Rows.** Q3 runs at close-out, not in the pilot, so there is nothing to check here.
5. **The register entry, `entry.md`.**
   - Does every claim trace to the files?
   - Is every recommendation marked as the coordinator's?
   - Does every founder item come from the rule table, or from a `no placement` mark?
   - Is anything decided there that is the founder's to decide?
6. **Coverage.** Is any statement in the platforms' phase A outputs that bears on the subject left out of every variation point?
7. **Matching.** Does each variant's `basis_evidence` show the bases it claims? Is any variant placed under a variation point that names a different X?
8. **Kinds.** For the statements the analysis cites, is the rule `kinds.tsv` gives for each one right for that source?

## Output

`studies/subjects/S-01/review.md` holds:
- a numbered list of findings, each with:
  - the file and id;
  - the problem;
  - the evidence for it;
  - `must fix` or `optional`;
- at the end, the count of items checked under each heading above.
