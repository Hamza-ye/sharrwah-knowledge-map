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

