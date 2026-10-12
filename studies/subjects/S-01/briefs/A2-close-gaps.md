# Brief: S-01, closing one platform's gaps on the variation points (pilot, step 1, phase A2)

This is `PLAN.md` Stage 2, the pilot: the gap-closing inside the subject. It runs after phase B. You are one agent with one task, for one platform. The message that started you names the platform.

**Read only:**
- this brief;
- `briefs/A-one-platform.md`, whose inputs and rules you follow;
- your platform's phase A files in `studies/subjects/S-01/<platform>/`;
- `studies/subjects/S-01/variation-points.tsv`;
- `studies/subjects/S-01/variants.tsv`, only the rows for your platform.

## The task

Take each row of `variants.tsv` for your platform whose `variant` is `gap` or `not covered`. For each variation point it belongs to:
1. Read the held or live sources likely to state who or what fills it on your platform. Run `method/held_index.py` on an address before you fetch it live.
2. Record what you find as new statements, continuing your `stmt_id`s and `cite_id`s, under phase A's rules.
3. Where a complete list shows it absent, record an absence. Where nothing states it, record a new gap, listing what you read. Don't change existing rows.

## Output

**In your platform's phase A files:**
- add the new statements, citations and gaps there;
- don't change existing rows.

**`a2.tsv`** in `studies/subjects/S-01/<platform>/`, one row per variation point you worked on. Columns:
- `vp_id`;
- `stmt_ids` (the statements you added for it);
- `gap_ids` (the gaps that remain for it);
- `read` (each path at its commit, and each URL with the date you read it).

The file is tab-separated, with a header row and no quoting.
