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
- The scripts can run on a copy: `class_slice.py` line 41 takes the model's folder from `CLASS_MODEL_DIR`, and both other scripts import it (`check_class_part.py` line 18, `class_kinds.py` line 20). `python3 -I` ignores only `PYTHON*` variables, so the variable still applies. The test below confirms it.

**Fix.** Replace line 8 with: "Copy `studies/class-model/` to your scratchpad (`cp -r studies/class-model $S/model`), and run every script with `CLASS_MODEL_DIR=$S/model`: the checker on each copied part in order (`B-anchor`, `B-woocommerce`, `B-backfill-woocommerce`), then `class_kinds.py` and `class_slice.py model`. Then `diff` each copied `derived.tsv` and `derived-qualities.tsv` with the part's own. A difference is a finding." Line 37 then holds as written.

