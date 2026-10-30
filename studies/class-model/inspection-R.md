# Inspection of the dry run's review brief (`R-dry-run.md`)

An inspection in Fagan's sense (1976): the brief is read before any agent runs it, for what would make a reviewer that follows it produce a wrong, slanted or uncheckable review. The inspector wrote none of it. Every judgement below is marked as a **Reading**; facts cite a file and line at the commit named here.

## What was read, at which commit

- The repository at `aaa4b3fc` (branch `claude/vibrant-meitner-oh70v4`), which commits the brief. The inspection began at `aaf68c80`, with the brief untracked; its bytes are the same at both (sha256 `46fe6830…2911`).
- `studies/class-model/briefs/R-dry-run.md`, whole (50 lines).
- `studies/class-model/briefs/B-extent.md`, whole (135 lines; sha256 `48e1017d…82ad`).
- `method/class_slice.py`, `method/check_class_part.py` and `method/class_kinds.py`, whole, and commands run on SH-C-020, SA-C-021 and WC-C-064.
- `PLAN.md` lines 204 to 240 (Stage 4A), and the end of `studies/class-model/inspection-B.md`, for single checks.
- `studies/class-model/scope.tsv` was untracked and being written by the scope part while this inspection ran. It is used below only for size estimates, marked as provisional.

(Findings are written as they are found; the summary table is at the end of the work, above the findings.)

## Findings

### 1. Running the checker as told changes the parts' files (must fix)

**The brief's words.** Line 8: "the checker's output on each part: run `python3 -I method/check_class_part.py studies/class-model/parts/<part>` yourself". Line 37: "**Change nothing** but your own file."

**Problem.** The two can't both be followed. The checker writes into the folder it checks, so the reviewer's run rewrites each part's `derived.tsv` and `derived-qualities.tsv`. Where a part's rows changed after its own last check (a coordinator's correction, or a part that didn't re-run), the rewrite also erases the one sign of it: the reviewer can no longer see that the part's derived files were stale.

**Evidence.**
- `method/check_class_part.py` lines 496 to 512 open `os.path.join(d, "derived.tsv")` and `os.path.join(d, "derived-qualities.tsv")` for writing, where `d` is the part's folder given on the command line.
- `method/class_kinds.py` lines 39 to 41 read `derived.tsv` from each part's folder, and exit if it is missing, so the kinds (brief, line 9) depend on those files.
- The scripts can run on a copy: `class_slice.py` line 41 takes the model's folder from `CLASS_MODEL_DIR`, and both other scripts import it (`check_class_part.py` line 18, `class_kinds.py` line 20). `python3 -I` ignores only `PYTHON*` variables, so the variable still applies. Tested: with `CLASS_MODEL_DIR` set to a copy in the inspector's scratchpad, and a `B-anchor` there holding only headers, the checker read the copy's `scope.tsv` (22 problems: the 22 anchor concerns not landed) and wrote both derived files into the copy. `git status` showed nothing changed in the repository but this file.

**Fix.** Replace line 8 with: "Copy `studies/class-model/` to your scratchpad (`cp -r studies/class-model $S/model`), and run every script with `CLASS_MODEL_DIR=$S/model`: the checker on each copied part in order (`B-anchor`, `B-woocommerce`, `B-backfill-woocommerce`), then `class_kinds.py` and `class_slice.py model`. Then `diff` each copied `derived.tsv` and `derived-qualities.tsv` with the part's own. A difference is a finding." Line 37 then holds as written.

### 2. The depth rule samples what the plan requires in full (must fix)

**The brief's words.** Line 15: "**Every placement against all of the concern map's statements** for the concerns behind the cell, under all five of Q1's placements". Line 32: "Check every cell whose kind hinges on one placement (a count of 0 or 1), every join on role, every strained fit and every `none-held` cell. Check the rest by a sample you state, with how you chose it."

**Problem.** Line 32 turns line 15's "every placement" into a sample for every capability with a count of 2 or 3. That departs from the plan, which the brief can't change. And the count, not only the kind, is what the model reports: a wrong `core` in a capability counted 2 leaves the kind unchanged, but puts a wrong count and a wrong placement on the founder's page (`PLAN.md` line 222: "which platforms establish each and where"). **Reading:** the sample saves little. The domain's own statements are small enough to read whole, once per concern. What costs is the search beyond them.

**Evidence.**
- `PLAN.md` line 216: "The review checks every placement against all of Q1's statements for the concern, not its `where` rows alone." `STATE.md` line 148: "the review of its output, which checks every placement against all of Q1's statements".
- The size, from `scope.tsv` at `23461ca6` and `class_slice.py statements`, run by the inspector: domain B gives Shopify 11 concerns with 190 statements (35,594 bytes as printed), Salla 11 with 214 (52,120 bytes), and WooCommerce 8 with 93 (12,019 bytes). That is 497 statements and about 100 KB for the dry run's three platforms. The concerns of other domains that name B under `also` add 255 statements (Shopify 109, Salla 119, WooCommerce 27).
- The cost of `search`, also run by the inspector: `product` finds 226 Shopify statements, `product;منتج` 301 Salla statements, `product` 159 WooCommerce statements, and `inventory` 98 Shopify statements. Each such search prints more than one platform's whole domain.

**Fix.** Replace line 32 with:
> **Depth.** Every cell's placement against every statement of its concerns (checks 1 and 2): read each domain-B concern's statements once, under all five placements, and test every cell and evidence row that rests on them. The searches beyond the domain's concerns: for every cell listed under check 1's two bullets, every cell of a capability counted 0 or 1, and every `none-held` cell; for the other cells, a sample drawn as the output section says. Checks 3 to 9: every row.

"The concerns behind the cell" (line 15) should also be defined, since a back-fill cell and a `none-held` cell may have no concern of their platform landed in the capability: "the concerns of its platform landed in the capability, its parent or its children, and the concern of every statement it cites".

