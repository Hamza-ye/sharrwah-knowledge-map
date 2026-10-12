# Brief: S-01, the existing question rows on this subject (pilot, step 3)

This is `PLAN.md` Stage 2, the pilot. It carries out Q3 for one subject. You are one agent with one task.

**Read only this brief and:**
- `register/pay-questions.tsv`, and in it only the columns `id`, `question`, `needed_by` and `lane`. The other columns hold citations that are not trusted: don't use them.
- the row files the coordinator's message names, as the founder chose at Q3. That is the 81 payment rows, the Knowledge Map's 179 questions, or both.
- `studies/subjects/S-01/variation-points.tsv`, `variants.tsv`, `analysis.tsv` and `yemen-marks.tsv`.

Don't read `notes*.md` files or any `note` column.

## What the rows are

Agents wrote these rows earlier, from a smaller evidence base, as gaps they perceived at the time. They are not Sharrwah's requirements. They are inputs to place.

## The task

For each row:
1. **Say whether it touches the subject:** `yes`, `no` or `unclear`.
   - A row touches the subject when its question asks who or what fills one of the subject's variation points, or asks something a variation point's variants, analysis or marks answer.
   - Rows that don't touch it are listed with `no`, and nothing more.
2. **For each row that touches it,** record:
   - the variation points it belongs to;
   - **who answers it,** every one that applies:
     - `founder decision`: when `analysis.tsv` or `yemen-marks.tsv` gives a `founder_item` on it;
     - `partner`: when a mark on it is `carried only with a partner`;
     - `regulator`: when its cause is `market, named rule`, or a mark's `moves` names a regulator;
     - `Yemen evidence`: when its marks answer it;
     - `platform evidence`: when its variants answer it;
   - **when** it must be answered. This comes from the variation point's `follows` in `analysis.tsv`, by this mapping, which is the coordinator's own:
     - **`before build`:** when `follows` includes "a decision for the founder, on a recommendation", or a mark gives a `founder_item`;
     - **`before release`:** when it includes "kept open as a variation point until evidence settles it", "a variation point behind one interface, bound per market, store or plan" or "a variation point bound per market";
     - **`later`:** when it holds only "the platform carries all the variants at once", "bound per product", "a commonality, carried as the references carry it" or "left to the build";
     - **`unclear`:** when it reads `none applies`.

     Where a row's variation points give different times, take the earliest.
3. **Flag each time bomb** in it, by Q3's four types, as these rules decide *(the rules are the coordinator's own)*:
   - `bundles`: its variation points' `follows` differ.
   - `wrong party`: either of these:
     - its `lane` is `founder`, and `who_answers` has no `founder decision`;
     - its `lane` is `analyst`, `researcher` or `spike`, and `who_answers` holds only `founder decision`, `partner` or `regulator`.
   - `wrong time`: its `needed_by` and its `when` disagree, reading `needed_by` this way:
     - `model`, `spine` and `slice` mean before build;
     - `launch` means before release;
     - `later` means later.
   - `market fact`: `who_answers` is only `Yemen evidence`, yet the question asks what the product should do.
4. **Leave unclear rows unresolved,** with what would settle them. Nothing gets settled that the evidence didn't settle.

## Rules

- Every placement and flag cites the ids it rests on: `vp_id`, or `vp_id` plus `case_id`.
- No inference beyond the placement, anywhere, including notes.

## Output, in `studies/subjects/S-01/`

The `.tsv` file is tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `rows.tsv` | `row_id` · `touches` · `vp_ids` · `who_answers` · `when` · `time_bombs` (`;`-separated, or empty) · `basis` (the ids each answer rests on) · `what_would_settle_it` (for `unclear`) · `note` |
| `notes-e.md` | Rows that were hard to place, and why; problems with the method. |
