# Brief: S-01, the subject in each Yemen case (pilot, step 2)

This is `PLAN.md` Stage 2, the pilot. It carries out Q2's marks for one subject. You are one agent with one task.

**Read only this brief and:**
- Stage 1's output in `studies/yemen-cases/`: `axes.tsv`, `constants.tsv`, `cases.tsv`, `citations.tsv` and `unknowns.tsv`;
- the subject's files in `studies/subjects/S-01/`:
  - `variation-points.tsv`, `variants.tsv` and `analysis.tsv`;
  - the five platforms' phase A outputs in `<platform>/`.

Don't read `notes*.md` files or any `note` column.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

## The task

For each variation point and each Yemen case, give one mark. The marks are Q2's, as agreed:
- `carried unchanged`: a reference's variant works in the case as the reference places it;
- `carried with configuration`: a reference's variant works in the case once it is set for the market, as that reference's stated scope or settings allow;
- `carried only with a partner`: a reference's variant works in the case only if a party outside the platform takes a role the variant names;
- `no placement`: no reference's variant works in the case;
- `unknown`: the evidence can't show which of the above.

Go down the list, and take the first mark that holds for any reference's variant. Name that variant by its `variant_id`.

## Rules

1. **Two pieces of evidence.** A mark other than `unknown` cites both:
   - **the variant's condition:** the `stmt_ids` of the platform's own statement of what the variant needs or where it holds. It is one of three:
     - a statement under bullet (e) whose `conditions` names the variant's statements;
     - a statement under (e) marked `none stated`, whose `identifier` appears in the variant's statements;
     - the scope of the variant's own statements;
   - **the case's evidence:** the Stage 1 ids showing whether the case meets that condition, which are `YA` states, `YK` constants or `YE` citations.

   Without both, the mark is `unknown`. Say what would show it.
2. **No placement** is a claim about every variant of the variation point.
   - In `per_variant`, give each variant's condition and the case evidence that it fails, as `<variant_id>: <condition stmt_ids> / <case evidence ids>`, separated by `;`.
   - If any variant's failure can't be shown, the mark is `unknown`.
   - Write it a second time as a product gap, in a way that still makes sense with Yemen's name removed. This is Q2's rule 3.
   - Write the founder's design decision it raises in `founder_item`, as `PLAN.md` section 6 says.
3. **Moves.** Where the evidence names a consultation, partnership, licence or regulator's action that would change a mark, record it in `moves`, with its citation. Otherwise leave `moves` empty.
4. **Nothing about what Sharrwah should do.** No inference beyond the mark, anywhere, including notes.

## Output, in `studies/subjects/S-01/`

The `.tsv` file is tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `yemen-marks.tsv` | `vp_id` · `case_id` · `mark` · `variant_id` (the variant used) · `condition_stmt_ids` · `case_evidence` (YA, YK or YE ids) · `per_variant` (for `no placement`) · `product_gap` (for `no placement`) · `founder_item` (for `no placement`) · `moves` · `what_would_show_it` (for `unknown`) · `note` |
| `notes-d.md` | Marks that were hard to give, and why; problems with the method. |
