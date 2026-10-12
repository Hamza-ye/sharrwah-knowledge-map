# Brief: S-01, the subject in each Yemen case (pilot, step 2)

This is `PLAN.md` Stage 2, the pilot. It carries out Q2's marks for one subject. You are one agent with one task.

**Read only this brief and:**
- Stage 1's output in `studies/yemen-cases/`: `axes.tsv`, `constants.tsv`, `cases.tsv`, `citations.tsv` and `unknowns.tsv`;
- the subject's files in `studies/subjects/S-01/`:
  - `variation-points.tsv`, `variants.tsv` and `analysis.tsv`;
  - the five platforms' phase A outputs in `<platform>/`.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

## The task

For each variation point and each Yemen case, give one mark. The marks are Q2's, as agreed:
- `carried unchanged`: a reference's variant works in the case as the reference places it;
- `carried with configuration`: a reference's variant works in the case once it is set for the market, as that reference's stated scope or settings allow;
- `carried only with a partner`: a reference's variant works in the case only if a party outside the platform takes a role the variant names;
- `no placement`: no reference's variant works in the case;
- `unknown`: the evidence can't show which of the above.

Take the first mark that holds for any reference's variant. Name the variant you used.

## Rules

1. **Two pieces of evidence.** A mark other than `unknown` cites both:
   - **the variant's condition:** the `stmt_ids` of the platform's own statement of what the variant needs or where it holds, such as its scope, eligibility, countries, partners or licence;
   - **the case's evidence:** the Stage 1 ids showing whether the case meets that condition, which are `YA` states, `YK` constants or `YE` citations.

   Without both, the mark is `unknown`. Say what would show it.
2. **No placement** is written a second time as a product gap, so that it still makes sense with Yemen's name removed. This is Q2's rule 3.
3. **Moves.** Where the evidence names a consultation, partnership, licence or regulator's action that would change a mark, record it in `moves`, with its citation. Otherwise leave `moves` empty.
4. **Nothing about what Sharrwah should do.** No inference beyond the mark. A note may hold inference, starting with "Inference:", and it never counts.

## Output, in `studies/subjects/S-01/`

The `.tsv` file is tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `yemen-marks.tsv` | `vp_id` · `case_id` · `mark` · `variant_used` (`<platform>: <stmt_ids>`) · `condition_stmt_ids` · `case_evidence` (YA, YK or YE ids) · `product_gap` (for `no placement`) · `moves` · `what_would_show_it` (for `unknown`) · `note` |
| `notes-d.md` | Marks that were hard to give, and why; problems with the method. |
