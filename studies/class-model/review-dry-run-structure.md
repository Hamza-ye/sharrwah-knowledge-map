# The dry run's review: the structure

**What this is.** One of the two independent reviews of the class's model's dry run (domain B), made by an agent that made none of it, from `studies/class-model/briefs/R-dry-run.md`. The review is split in two. This half is the structure: the brief's checks 3, 4, 6, 7, 8, 9, 10, 11, 12 and 13. The other reviewer holds checks 1, 2 and 5 (each cell's placement, each `supports` value, each `none-held` cell). Where a finding here touches a cell's placement, it is noted for the other reviewer and not pursued.

## What I read, and at which commit

- **Repository:** `sharrwah-knowledge-map`, branch `claude/vibrant-meitner-oh70v4`, commit `82868b7bac943a439705db77e457432a7ddd518d`.
- **Brief:** `studies/class-model/briefs/R-dry-run.md`; the parts' brief `studies/class-model/briefs/B-extent.md`.
- **Evidence:** each domain-B concern's statements, under all five placements, through `python3 -I method/class_slice.py statements --platform P --concerns C --width 160`, once each; `concerns --domain B --where`, `matches`, `gaps`, `search`, `key`, `uncited --domain B`, `model --domain B`, `homonyms`.
- **The parts:** `studies/class-model/parts/B-anchor/`, `B-woocommerce/`, `B-backfill-woocommerce/`: their rows first, their `reading` and `why` columns and `notes.md` after my own reading.
- **`architecture/plan.md`,** line 49, for check 12.
- **Scripts, on a copy:** the model copied to my scratchpad, every script run with `CLASS_MODEL_DIR` set to the copy (results below).

(Sections follow as the checks are done.)
