# H-009: BigCommerce's settings-list structure, each section paired with the next one's address

**Repository:** other-product-class, `bigcommerce/`. **Instrument:** none. This corrects a structure already held, from its own source. No run is needed.

**What to do:**
1. **Re-extract the structure from its source.** The source is `bigcommerce/structures/settings-list/`, read from the run `20261029T012951Z-store-settings-en`, step 2, `steps/002.frame-0.aria.yaml` (its `meta.json`). Its `items.jsonl` gives each section the address of the link after it:
   - `Store profile` has `/manage/microapps/localization-settings-ui` (line 1);
   - `Localization` has `/manage/microapps/ng-currencies` (line 2);
   - and so on down the list.

   The source gives each link its own `/url` before its heading: `Store profile` has `/manage/microapps/store-profile-ui` (lines 7 to 10), and `Localization` has `/manage/microapps/localization-settings-ui` (lines 12 to 15). Re-extract so that each section carries the `/url` of its own link. Check the last section of each group, and the very last one, which the shift leaves without its own address.
2. Record the correction in the repository's own way: its `docs/OPERATING.md`, and a note in `bigcommerce/index/run-notes.tsv`.

**Stop before:** nothing outside the repository. The correction reads held bytes only.

**Already held:** the source step, whole. The section names, groups and descriptions in `items.jsonl` are right; only the addresses are shifted.

**Why:** the class's model reads BigCommerce's settings as entries of the held pass (`studies/class-model/briefs/H-held.md`; `studies/class-model/held/bigcommerce/entries.tsv`, `BC-E-00001` to `BC-E-00040`). The pass cites the source step for each section's address, until the structure is corrected.

**Needs:** nothing from the founder.

**Done when:** `bigcommerce/structures/settings-list/items.jsonl` gives each of the 40 sections the address its own link holds in the source step, and its `meta.json` says how it was re-extracted.
