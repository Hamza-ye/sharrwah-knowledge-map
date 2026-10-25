# Brief: S-01, the subject in each Yemen case (pilot, step 2)

*Since 25 October 2026 this brief is not used for later subjects: one Yemen row per decision replaces the marks (the founder's decision; `PLAN.md`, section 6, step 6). It stays as the record of how the pilot was marked.*

This is `PLAN.md` Stage 2, the pilot. It carries out Q2's marks for one subject. You are one agent with one task.

**Read only this brief and:**
- Stage 1's output in `studies/yemen-cases/`: `axes.tsv`, `constants.tsv`, `cases.tsv`, `citations.tsv` and `unknowns.tsv`;
- the subject's files in `studies/subjects/S-01/`:
  - `variation-points.tsv` and `variants.tsv`;
  - the five platforms' phase A outputs in `<platform>/`.

Don't read `notes*.md` files or any `note` column.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

## The task

For each variation point and each Yemen case, give one mark. The marks are Q2's, as agreed:
- `carried unchanged`: a reference's variant works in the case as the reference places it;
- `carried with configuration`: a reference's variant works in the case once it is set for the market, as that reference's stated scope or settings allow;
- `carried only with a partner`: a reference's variant works in the case only if a party outside the platform takes a role the variant names, and the case's evidence shows a party that can take that role;
- `no placement`: no reference's variant works in the case;
- `unknown`: the evidence can't show which of the above.

Go down the list, and take the first mark that holds for any reference's variant. Name that variant by its `variant_id`. If several variants qualify, name the lowest `variant_id`.

## First, what each variation point bears on

A case differs from today's case, `YC-00`, only on the axes its `name` lists. So a variation point's mark can change only in cases that change an axis its variants' conditions bear on.

1. **List them.** Before any mark, write one row of `bears-on.tsv` for each variation point. Give the axes (`YA` ids) and constants (`YK` ids) that its variants' conditions bear on. In `basis`, quote each condition's words and the state labels it is checked against.
2. **Which cases to mark.** Mark `YC-00`, and every case whose `name` lists one of the variation point's axes.
3. **Every other case** has the same states on those axes as `YC-00`, so it carries `YC-00`'s mark. Write no row for it.

## Rules

1. **Two pieces of evidence.** A mark other than `unknown` cites both:
   - **the variant's condition:** the `stmt_ids` of the platform's own statement of what the variant needs or where it holds. It is one of three:
     - a statement under bullet (e) whose `conditions` names the variant's statements;
     - a statement under (e) marked `none stated`, whose `identifier` appears in the variant's statements;
     - the scope of the variant's own statements. An empty scope is no condition.
   - **the case's evidence:** the Stage 1 ids showing whether the case meets that condition. These are `YA` axis ids, whose state is the one `cases.tsv` gives the case; `YK` constants; or `YE` citations. Cite only the axes and constants listed for the variation point in `bears-on.tsv`, and their `YE` ids.
     - *(The coordinator's own:)* every case shares one frame, Q2's: the merchant sells in the Yemeni market. A condition that names only countries or regions, such as "merchants in Saudi Arabia" or "outside the Kingdom", is checked against that frame, and cited as `Q2`.

   Without both, the mark is `unknown`. Say what would show it. If the case's state on an axis the mark needs is `disputed` or `unknown`, the mark is `unknown`.
2. **No placement** is a claim about every answer variant of the variation point: every variant that isn't `gap`, `absent` or `not covered`.
   - **`per_variant`:** give each answer variant's condition and the case evidence that it fails, as `<variant_id>: <condition stmt_ids> / <case evidence ids>`.
     - Separate the entries with `;`.
     - Inside an entry, separate ids with commas.
   - **`condition_stmt_ids` and `case_evidence`** hold all the ids the entries give.
   - **If any variant's failure can't be shown,** the mark is `unknown`.
   - **The product gap.** Write the failure a second time as a product gap, in a way that still makes sense with Yemen's name removed. This is Q2's rule 3.
   - **The founder item.** Write the founder's design decision it raises in `founder_item`, as `PLAN.md` section 6 says.
3. **Moves.** Where the evidence names a consultation, partnership, licence or regulator's action that would change a mark, record it in `moves`, with its citation. Otherwise leave `moves` empty.
4. **Nothing about what Sharrwah should do.** No inference beyond the mark, anywhere, including notes.

## Output, in `studies/subjects/S-01/`

The `.tsv` files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. Write the files as you go: if you are interrupted, the next run continues from them.

| File | Columns |
| --- | --- |
| `bears-on.tsv` | `vp_id` · `axis_ids` · `constant_ids` · `basis` (each condition's words, quoted, with the state labels it is checked against) · `note` |
| `yemen-marks.tsv` | `vp_id` · `case_id` · `mark` · `variant_id` (the variant used) · `condition_stmt_ids` · `case_evidence` (YA, YK or YE ids) · `per_variant` (for `no placement`) · `product_gap` (for `no placement`) · `founder_item` (for `no placement`) · `moves` · `what_would_show_it` (for `unknown`) · `note` |
| `notes-d.md` | Marks that were hard to give, and why; problems with the method. |
