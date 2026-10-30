# Brief: the held pass, the platforms' self-descriptions read entry by entry (Stage 4A)

**What this is.** The class's model was built from the concern map, finished on 12 October 2026. The evidence repositories hold far more:
- the platforms' own lists of their places, plans, permissions, catalogs, events and changes, captured since or never read;
- Zid's, BigCommerce's and WooCommerce's admin structures, none of which the model has read.

`studies/class-model/held-vs-read.md` measures the gap. This pass reads every entry of those self-descriptions and places each one on the model, so that what the platforms show of themselves reaches it by reading, not by search (the founder, 30 October). You draft placements. The coordinator checks them, and amends the model from them:
- an entry placed on a capability becomes that platform's cell's evidence;
- a new capability is made with its cells;
- the merge runs again.

**Your batch.** Your message names a platform and a range of entries. `python3 -I method/held_entries.py show --platform <p> --from <n> --to <m>` prints them, each as:
- its id;
- its structure, and the labels (a store, a language) it was held under;
- its text: the fields the platform states, in the source's order.

**Read only this brief and:**
- **the repository's guides, for your platform's evidence, before anything else:**
  - for Shopify, observed-sh (`/home/user/observed-sh`); for Salla, observed-sa (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and `structures/REGISTER.tsv`'s rows for your structures;
  - for Zid, BigCommerce and WooCommerce, other-product-class (`/home/user/other-product-class`): `README.md`, and the platform folder's `README.md` and `GAPS.md`;
  - each structure's `meta.json`, which says what the structure is, what it was read from and how its items were made;
- `studies/class-model/held/selection.tsv`, for your platform's rows: which structures this pass reads and why;
- `method/held_entries.py` (`show`, `check`);
- **the model:** `method/class_slice.py caps` (with `--terms`, `--domain`), `key`, `search`; `method/land_points.py cell <cap_id> <platform>`; and `studies/class-model/merged/capabilities.tsv`, read with `cut` or `grep`, never whole;
- `studies/class-model/briefs/B-extent.md`: "Cells and evidence", and "Conventions from the dry run".

## For each entry

1. **Read it as the platform states it.** Where its text leaves it unclear, read its item at the source and line `entries.tsv` gives, or the structure's own source file, which `meta.json` names. The bytes are the evidence. Where a structure's items and its source disagree, the source governs: say so in your notes. BigCommerce's `settings-list`, for one, pairs each section with the next section's address; its source step `steps/002.frame-0.aria.yaml` gives each section's own.
2. **Place it**, one of three:
   - **`capability`:** the model's capability whose thing the entry is. Give its cap_id (several, `;`-separated, only where the entry is two capabilities' at once) and what the entry `supports` on your platform, by `B-extent.md`'s "Cells and evidence" and its conventions:
     - `core`: the platform's own admin place, setting, route, plan line or permission, its own API for its own feature, or a built-in feature it states;
     - `own-service`: only where the entry names the platform's company as the maker or provider;
     - `extension-point`: an app's page, an app or a category of the platform's app store, an extension target, a provider interface;
     - `outside`: a named third party doing it, with no interface of the platform named;
     - `shows`: the entry names the thing or its terms and supports no placement. A help page's title, a changelog post and a feature flag that isn't released are `shows`.
   - **`new`:** no capability of the model is the entry's thing, and the entry gives it a place of its own: an admin section or route, an API group, a plan line, or an app category (B-extent, "When something becomes a capability"). Before you write `new`, search every domain: `class_slice.py caps --terms "<term>; <term>"`, in English and in Arabic for Salla and Zid. Name it in `cap_id` as `new:<its name in the platform's words>`, and give what it supports. Entries of the same new thing name it the same way.
   - **`out`:** the entry isn't something the platform does for merchants, buyers, partners or developers, at the grain of the model. Leave `cap_id` and `supports` empty, and say why in `reading`. Some kinds are always out:
     - a layout node, a UI string, a sort or filter option, a sample;
     - one store's or one account's own records;
     - market data, such as countries, currencies, languages or formats per country, which is the subjects'.

   A sub-page, sub-route or setting of a thing the model holds is that capability's entry, not a new one. A route under an app's name, open only to the apps permission, is the app's page: `extension-point` (B-extent's convention).
3. **Group:** one line may name several entries, `;`-separated, where all of them have the same placement, cap_ids, supports and reading. Group only entries next to each other in one structure.
4. **`reading`:** a few words, a reading: why it lands there, or why it's out.

**Where you can't tell,** place it where it most plainly belongs, and list it in your notes with what would settle it. Don't leave an entry unplaced.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Never decide a maker, a third party or a placement from what you know of the platform: only from what the entry and its source state.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, the subjects' or the entries. Write only your batch's files, and make no commits.

## How to work, keeping your context small

- Print your entries 150 to 250 at a time with `show --from --to`.
- Keep a short list of the capabilities your platform's entries keep meeting. Check each cap_id against `capabilities.tsv` as you go.
- Write placements as you go, never at the end.

## Output, in `studies/class-model/held/<platform>/`

- **`placements-<batch>.tsv`:** tab-separated, a header row, no quoting, no tab or newline inside a field:
  - `entry_id` (one, or several `;`-separated);
  - `placement`: `capability`, `new` or `out`;
  - `cap_id`: cap_ids `;`-separated, `new:<name>`, or empty;
  - `supports`: values `;`-separated, or empty for `out`;
  - `reading`.
- **`notes-<batch>.md`:**
  - each `new` thing, with its entries, its place of its own and the terms you searched;
  - entries you couldn't tell, and what would settle each;
  - entries whose placement would change a cell the model holds, such as a capability the model places otherwise on your platform, or holds nothing for;
  - a structure whose items and source disagree;
  - problems with this brief or the script.

Check your batch with `python3 -I method/held_entries.py check --platform <p> --batch <batch>`, until it prints no problem.

## Report

Back to the coordinator:
- your entries' count by placement;
- each `new` thing, with its entries;
- the cells whose placement the entries would change, by capability;
- any problem;
- the checker's final line.
