# The dry run's reviews: the coordinator's check and rulings (30 October 2026)

**What this file is:** the coordinator's check of the two reviews of the dry run (`review-dry-run-cells.md`, `review-dry-run-structure.md`), and its rulings on their findings and proposed conventions. Each ruling is engineering's method ruling, listed for the founder's veto at the next report.

## The check

- **C2:** the inventory entries the cells review names are as it says. SH-I-0902 "Products > View cost", SH-I-0904 "Products > Edit cost", SH-I-1057 `EDIT_PRODUCT_COST` and SH-I-1129 `VIEW_PRODUCT_COSTS` are placed in SH-C-020, each with its citation. SH-I-1842 "Pre-order apps" and SH-I-1887 "Event booking apps" are placed in SH-C-188 and SH-C-190. No statement covers them.
- **C1:** the anchor's own notes say it read API-only rows as `shows`. The brief's test reads "its own API for its own feature" as `core`, and so does the ruling given to WooCommerce's part. The two methods are as the review says.
- **S3:** the extent brief does say that a candidate whose other concern is in another domain is `apart`, while the coordinator corrected U-016 and U-082 to `joined`. The two rules contradict each other, as the review says.
- **Both reviews' derived files matched the parts' own,** and both ran the checker on a copy.

## Rulings on the findings

| # | Ruling |
| --- | --- |
| C1 | Taken. A platform's own API (its folder, object, scope, webhook topic, or a mutation's requirement) is `core` for its own feature. It is `extension-point` where the API's statements say apps or partners do the work. A guide addressed to app developers about the platform's own API for its own feature is still `core`. The 55 rows are re-placed |
| C2 | Taken, by allowing evidence to cite a placed inventory entry by its id, where its citation holds and no statement covers it, rather than writing new statements into the frozen concern map. `search` now reads inventory entries, so a `none-held` search covers them. The three cells are rewritten |
| C3 | Taken. A capability named in a platform's own words (a plan line, a dashboard link) is shown by it, by the same standard for every platform in a join. Salla's stocktake cell is `core` |
| C4 | Taken as a convention. An admin route named for an application, and gated only by the apps permission, is the app's page: `extension-point` |
| C5 | Taken as a gap: maker evidence counts only as a statement naming the company. A note never counts |
| C6 | Taken. A feature flag that isn't released shows the platform names the feature, `shows`, not `core`. A released flag supports `core`, with its plan or store as its scope |
| C7 | Taken where cheap: the staff permission is cited where it decides a placement (S7) |
| S1 | Taken. A landed concern whose statements are cited in another tree is marked `strained`, and its reading names where else it is cited |
| S2 | Taken as a convention. `parent` means the platforms' own grouping puts the child under the parent, as a statement shows. Where the platforms' groupings differ, follow the one they share. Failing that, follow the anchor platforms' admin grouping, with the other in the note. Transfers and purchase orders are re-parented by it |
| S3 | Taken, by changing the briefs as the review proposes. Where the other side's concern is in another domain and names this one under `also`, a capability here may cite it, and the ruling is `joined`, with the basis naming that concern's domain. Otherwise it is `apart`, with the basis "scope.tsv gives <concern> domain <X>". U-016 and U-082 stay `joined` |
| S4 | Taken. One ruling row per pair of concerns, holding only that pair's keys, as the review writes them out |
| S5 | Taken. A ruling's keys come from the candidate's own concerns; the checker refuses others |
| S6 | Taken. SH-C-187 names B, and WC-C-064 names E, under `also` |
| S7 | Taken. Where Salla lists a permission for staff and for partners, the staff permission is cited for `core`. A partner's permission shows an interface for apps |
| S8 | Taken. A capability the uncited statements show and the model lacks is added: pricing, if its statements bear it out. The other uncited statements are cited where they bear on a placement |
| S9 to S12 | Taken: the quality's capability, the slot fillers' basis, and names that use every landed platform's terms and avoid a word that means something else on one of them |
| S13 and S14 | Taken: each kind that rests on another domain's statements, on one convention or on one gap is listed with the extent's report |
| S15 | Taken: see the architecture plan, below |
| S16 and S17 | Taken: the notes are corrected, and a reading names a Q1 gap that changes what its cell can claim |

## Rulings on the conventions

These go into the extent's brief before domains A and C to G run:
1. **Rulings:** `joined`, `nested` or `apart`, one row per pair, on keys from the candidate's own concerns, with S3's rule for another domain's concern.
2. **When something becomes a capability:** where at least one platform gives it a place of its own: an admin section or route, an API group, a plan line, or an app category. A single feature flag isn't enough.
3. **What counts as `core`:** C1's rule for APIs, C6's for feature flags, S7's for permissions, and C4's for an app's route.
4. **Statement or inventory entry:** evidence cites a statement by its key, or a placed inventory entry by its id where no statement covers it (C2).
5. **A statement's title against its description:** the statement's words as a whole decide. Where its description narrows its title, the description governs, the same way for every platform in a join.
6. **`parent`:** S2's rule.
7. **Names:** a mapping part proposes a rename in its notes; the coordinator renames at the merge. Homonyms go in the capability's note.
8. **Another domain's statements:** a concern that names this domain under `also` may support a placement here. The merge flags any statement that supports `core` or `own-service` in two domains, so nothing counts twice.
9. **Slot fillers:** a third party or a law that a statement names as doing the capability or setting its terms. A flag's name isn't one. Its market comes only from a market scope.
10. **What architecture reads:** each capability's data, events and deciding statements, derived by the merge in two grades. The keys its cells cite are attributed exactly. The other statements of the concerns landed in it are attributed "by landing", a coarse attribution that each area's design refines. Parts write nothing more. This keeps the parts' cost where it is, and says plainly what is coarse.
11. **Kinds carry their scope:** a `class` that holds only under a plan, a beta or one observed store says so.
12. **`open`:** never folded into `class` or `slot`. It is reported as "third parties where stated", where some platform places it with third parties and another is `not-stated`, or as "unplaced", where every platform that shows it is `not-stated`. Each is listed with the gap that would place it. With three of five platforms mapped, a `class` stays a class, while a `slot` or an `open` is provisional until Zid and BigCommerce are in.

## The checker's new tests

Taken now:
- inventory ids in evidence;
- a ruling's keys from its candidate's concerns, one concern on each side;
- `core` resting only on flags that aren't released, as a flag;
- a landed concern whose statements are cited in another tree, as a flag;
- `search` and the `none-held` re-search reading inventory entries.

The reviews' other proposed tests (20 in all) are recorded in the two review files for the checker's next revision, before domains A and C to G run.
