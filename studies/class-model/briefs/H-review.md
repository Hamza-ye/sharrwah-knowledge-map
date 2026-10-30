# Brief: the review of the held pass's dry run (Stage 4A)

**What this is.** The held pass (`studies/class-model/briefs/H-held.md`) places every entry of the platforms' self-descriptions that the class's model never read. Two batches ran first: BC-1 (BigCommerce, 147 entries) and ZD-1 (Zid, 153 entries). You made neither. Your review decides how the other 68 batches run, at what effort and with what changes to the brief (`PLAN.md`, section 3: after a brief runs, a separate agent reviews the result against its sources).

**Read only this brief and:**
- the held pass's brief, `studies/class-model/briefs/H-held.md`, which states the rules each placement had to follow;
- `studies/class-model/briefs/B-extent.md`, "Cells and evidence" and "Conventions from the dry run", the model's rules that H-held.md applies;
- the two batches' files, `studies/class-model/held/<platform>/placements-<batch>.tsv` and `notes-<batch>.md`;
- the entries, through `python3 -I method/held_entries.py show --platform <p> --batch <b>`, and each entry's source, at the file and locator `entries.tsv` gives, in other-product-class (`/home/user/other-product-class`, read-only), through its guides first;
- **the model:** `method/class_slice.py` (`caps --terms`, `key`, `search`), `method/land_points.py cell <cap_id> <platform>`, and `studies/class-model/merged/capabilities.tsv`, read with `cut` or `grep`.

## What to check, for every placement line of both batches

1. **The entry, read against its source.** Is the entry what the source says? Where the rendering and the source differ, the source governs.
2. **The placement:**
   - `capability`: is the cap_id the capability whose thing the entry is? Is there one whose thing it is more plainly? Search `caps --terms` with the entry's own words, in English and, for Zid, in Arabic.
   - `new`: is no capability's thing the entry's? Does it have a place of its own, by B-extent's "What a place of its own is"?
   - `out`: is the entry outside what the platform does, by H-held.md's list?
3. **`supports`,** by B-extent's "Cells and evidence" and its conventions, as H-held.md restates them: `core`, `own-service` (only on a maker statement), `extension-point`, `outside` (never for the merchant or the buyer), `shows`.
4. **`scope`, `terms`, `filler` and `quality`:** are they in the entry's own words, and is anything the entry states missing?

For each line, give a verdict:
- `agree`;
- `wrong capability: <cap_id>`;
- `wrong supports: <value>`;
- `should be new`, `should not be new` or `should be out`;
- `missing: <column>`;
- `can't tell: <what would settle it>`.

Say why, citing the source.

## Then, across both batches

- **What kind of miss recurs:** by kind of entry (a route, a page, a plan line, a permission, a gateway, a channel, a flag), and by rule.
- **Where H-held.md left the agents unsure or let them read a rule two ways,** with a fix in words the coordinator can paste. The agents' notes name some cases:
  - a help page that lists third parties' providers, where the help-page rule meets the `outside` rule;
  - a card in the platform's own channel catalog, where a third party is the venue or the provider;
  - an entry naming one of the platform's group companies as a provider.
- **Whether `high` effort missed what a closer reading finds.** Name the misses that more care would have caught, and those no effort would have, because the brief or the evidence didn't settle them.
- **The leads** printed by `show --candidates`: how often the right capability was among them.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Never decide a maker, a third party or a placement from what you know of the platform: only from what the entry and its source state.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- other-product-class is read-only: never write, commit or push to it.
- Run Python with `python3 -I`.
- Change no file but your output, and make no commits.

## Output

- `studies/class-model/held/review-dry-run.tsv`, one row per placement line, tab-separated, with a header row and no quoting:
  - `batch`;
  - `line`: the placement file's line number;
  - `entry_id`;
  - `verdict`;
  - `why`: a reading, citing the source.
- `studies/class-model/held/review-dry-run.md`:
  - the counts of verdicts per batch;
  - the recurring misses;
  - the brief's ambiguities, each with a fix;
  - the effort judgement;
  - the leads.

## Report

Back to the coordinator:
- the counts of verdicts;
- the misses by kind;
- each fix to the brief, in one line;
- your judgement on the effort for the other batches, with why.
