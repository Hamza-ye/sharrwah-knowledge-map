# The dry run's review: the cells (checks 1, 2 and 5)

One of two independent reviews of domain B's dry run, under `studies/class-model/briefs/R-dry-run.md`. This one takes the cells: check 1 (every placement against all of the concern map's statements), check 2 (each `supports` value against the brief's tests) and check 5 (each `none-held` cell). The other reviewer takes checks 3, 4 and 6 to 13. I made none of the parts.

## What I read, and at which commit

- **Repository:** `sharrwah-knowledge-map`, branch `claude/vibrant-meitner-oh70v4`, read at `82868b7b` (the back-fill's commit). The coordinator's commit `4fdfcda2`, made while I worked, changes only `STATE.md` and `method-report.md`: the parts, the concern map and the scripts are the same at both.
- **Briefs:** `studies/class-model/briefs/R-dry-run.md`; `studies/class-model/briefs/B-extent.md`.
- **Evidence:** each cell's concerns' statements under all five placements, through `python3 -I method/class_slice.py statements --platform P --concerns ID --width 160`, once per concern; whole statements through `key`; the platforms' other statements through `search`. The concern map is `studies/concern-map/` at `f93737ef` (its last change).
- **The parts:** `studies/class-model/parts/B-anchor/`, `B-woocommerce/`, `B-backfill-woocommerce/`: `cells.tsv`, `evidence.tsv`, `landings.tsv`, `capabilities.tsv`; their `reading`, `why` and `notes.md` only after my own placement of each cell was written in the coverage table.
- **Scripts, on a scratchpad copy** (`CLASS_MODEL_DIR=<scratchpad>/class-model-copy`), so the repository is unchanged: `check_class_part.py` on `B-anchor`, `B-woocommerce`, `B-backfill-woocommerce` in that order (0 problems; 7, 7 and 6 flags); `class_kinds.py --domain B --out -` (class 27, slot 1); `class_slice.py model --domain B` and `uncited --domain B`. Each copied `derived.tsv` and `derived-qualities.tsv` is identical to the part's own (`diff`: no difference, 6 files).

(Sections below are filled in as the review goes.)

## Findings, as established (drafts; the summary table and counts come at the end)

### C1. The anchor reads its platforms' own APIs as `shows`; the brief makes them `core` (must fix)

- **Rows:** every `B-anchor/evidence.tsv` row whose statement is Shopify's or Salla's own API for its own feature (a Merchant API folder, a GraphQL object or category, an access or app scope, a webhook topic, an API mutation's requirement) and whose `supports` is `shows`. They are listed in the coverage table with result `C1` and `mine` = `core`.
- **Problem:** the brief's test (`B-extent.md`, Cells and evidence) makes `core` "its own API for its own feature". The anchor's notes (line 191) read API folders, objects, scopes and webhook topics as `shows`, so that no `core` rests on boundary statements alone; the WooCommerce part reads WooCommerce's as `core` (`B-woocommerce/notes.md`, line 178). `method-report.md` (lines 39 and 46) names the two methods and leaves the choice to this review. Under the brief's test, two cells change their placement and their capability's count:
  - `CM-CAT-004/shopify` (`B-anchor/cells.tsv` line 8; `evidence.tsv` line 54): `SH-C-028/boundary/SH-S-6240` gives `write_metaobjects` "for taxonomy linking". The words name an access scope of Shopify's own Admin API for a feature of Shopify's products; they don't say apps or partners do the linking. **Reading:** `core`. The cell goes from `not-stated` to `core`, and CM-CAT-004's count from 1 to 2.
  - `CM-CAT-006/shopify` (`B-anchor/cells.tsv` line 12; `evidence.tsv` line 65): `SH-C-020/boundary/SH-S-6160` "Requires `unauthenticated_read_product_tags` access scope", from the Storefront API's `productTags` query (its note). **Reading:** Shopify's own Storefront API for its own product tags: `core`. The cell goes from `not-stated` to `core`, and CM-CAT-006's count from 2 to 3.
  - Every other C1 row changes its value only: its cell has other `core` rows.
- **Also:** the anchor applies its own method unevenly. Salla's partner-requestable permissions (for example `SA-C-020/decides/SA-S-2471`, `SA-C-020/decides/SA-S-2612`, whose notes say "Permission a partner can request on a merchant's store") are read `core`, while Salla's app scopes (`SA-C-020/boundary/SA-S-1552`) are `shows`. Both are the platform's own permission system; under the brief's test both are `core`.
- **Fix:** in `B-anchor/evidence.tsv`, set `supports` to `core` on each C1 row, with its `why` naming the API; in `B-anchor/cells.tsv` lines 8 and 12, rewrite the `reading` as `core` on the platform's own API, quoting the words; the brief states the rule once for every part: an API statement is `core` unless its words say apps or partners use it to do the work, and then it is `extension-point`.
