# The dry run's review: the structure

**What this is.** One of the two independent reviews of the class's model's dry run (domain B), made by an agent that made none of it, from `studies/class-model/briefs/R-dry-run.md`. The review is split in two. This half is the structure: the brief's checks 3, 4, 6, 7, 8, 9, 10, 11, 12 and 13. The other reviewer holds checks 1, 2 and 5 (each cell's placement, each `supports` value, each `none-held` cell). Where a finding here touches a cell's placement, it is listed for the other reviewer at the end and not pursued.

Every judgement of mine is marked **Reading**. Counts come from the scripts named. Statement keys are the concern map's; part rows are cited as `part/file line N`, the line in the file counting its header as line 1.

## What I read, and at which commit

- **Repository:** `sharrwah-knowledge-map`, branch `claude/vibrant-meitner-oh70v4`, commit `82868b7bac943a439705db77e457432a7ddd518d`. The branch moved to `42d78d62` while I worked; the two commits since change only `STATE.md`, `method-report.md` and the two reviews' own files (`git diff --stat 82868b7b HEAD` on the parts, briefs, scope, seed, `method/`, `architecture/` and the concern map is empty), so every row cited here is as it was read.
- **Briefs:** `studies/class-model/briefs/R-dry-run.md`; the parts' brief `studies/class-model/briefs/B-extent.md`.
- **Evidence, before the parts' arguments:** each domain-B concern's statements under all five placements, once each, through `python3 -I method/class_slice.py statements --platform P --concerns C --width 160` (Shopify 190 statements in 11 concerns, Salla 214 in 11, WooCommerce 93 in 8), with each line tagged by the cells that cite it (cap and `supports` only); every statement the parts cite from other domains' concerns (SH-C-028, SH-C-141, SH-C-187, SA-C-098, SA-C-124, WC-C-061, WC-C-107), whole, and all of SA-C-098's, SA-C-124's and SH-C-187's statements; `concerns --domain B --where`, `matches`, `gaps`, `search`, `outscope`, `key`, `uncited --domain B`, `model --domain B`; scope.tsv's rows for every concern the rulings' candidates hold.
- **The parts' rows:** `capabilities.tsv`, `landings.tsv`, `cells.tsv`, `evidence.tsv`, `rulings.tsv`, `qualities.tsv`, `slot-fillers.tsv`, `derived.tsv`, `derived-qualities.tsv` of `studies/class-model/parts/B-anchor/`, `B-woocommerce/` and `B-backfill-woocommerce/`. Their `reading`, `why`, `basis` columns and `notes.md` were read after my own reading of each join, ruling and tree.
- **`architecture/plan.md`,** line 49, for check 12.

## The scripts, run on a copy

The model was copied to my scratchpad (`class-model-copy`) and every script run with `CLASS_MODEL_DIR` set to the copy; `git status` showed the repository unchanged after each run.

| Script | Result |
|---|---|
| `check_class_part.py` on `B-anchor` | 25 capabilities, 22 landings, 50 cells, 220 evidence rows; 0 problems, 7 flags |
| `check_class_part.py` on `B-woocommerce` | 3 capabilities, 8 landings, 28 cells, 77 evidence rows; 0 problems, 7 flags |
| `check_class_part.py` on `B-backfill-woocommerce` | 6 cells, 0 evidence rows; 0 problems, 6 flags |
| `diff` of each copied `derived.tsv` and `derived-qualities.tsv` with the part's own | identical, all six files |
| `class_kinds.py --domain B --out -` | 28 capabilities: class 27, slot 1 (CM-SEL-008), open 0 |
| `class_slice.py model --domain B` | 28 capabilities; 11 with nothing landed in themselves |
| `class_slice.py uncited --domain B` | 270 statements uncited: Shopify 105, Salla 89, WooCommerce 18, and 58 of Zid and BigCommerce, whose parts haven't run |

The 20 flags are rows of the coverage table, each with how it was resolved (below, "The checker's flags"). B-woocommerce's notes answer 9 flags; my run prints 7, because scope.tsv now names B under `also` for WC-C-061 and WC-C-107 (commit 69bce534), which cleared two.

## Summary

| # | Finding | Check | Verdict |
|---|---|---|---|
| S1 | SA-C-020 lands `clean` in CM-CAT-001, but its bundle and donation statements are cited in CM-SEL-006 and CM-SEL-007, roots of other trees | 3 | optional |
| S2 | Transfers and purchase orders hang under locations, though Shopify's own grouping (one statement held under two keys, cited in two trees) puts them under inventory, and the parent of purchase orders rests on a permission dependency | 4 (3) | optional |
| S3 | U-016 and U-082 are ruled `joined`, though both briefs say a candidate whose other concerns scope.tsv puts in other domains can only be `apart` | 7 | must fix |
| S4 | U-003, U-059 (both parts) and U-061 (anchor) each ask about two or three pairs; one row names one capability, while some of its keys stand for another pair, joined elsewhere or apart | 7 | must fix |
| S5 | U-070's Shopify key doesn't stand for product cost; three rulings hold keys of concerns outside their candidate, which the checker ignores | 7 | optional |
| S6 | scope.tsv: SH-C-187 lacks B under `also` (cited in CM-SEL-007); WC-C-064 lacks E for its product custom fields | 7, 13 | optional |
| S7 | CM-CAT-011's count rests on one row, a permission a partner can request (SA-S-2612); Salla's staff permission of the same name is uncited, and 12 more Salla `core` rows cite the partner list while the staff one stays uncited | 8, 11 | must fix |
| S8 | Uncited statements that bear on a capability the model lacks or on a cell: pricing, restriction by product type, inventory-order, bins, sale start, negative stock, Salla's subscriptions scope, the transfer group's inventory permissions | 8 | optional |
| S9 | The quality `max_inventory_types` sits on CM-INV-001, though its statement sets it beside `enable_branch_inventories` | 9 | optional |
| S10 | The two slot fillers rest on feature-flag names (one unreleased) with no market in their scope; the same reading would make `virtooal` a filler, and it isn't | 9 | optional |
| S11 | CM-SEL-002's name lacks WooCommerce's term, though WC-C-066 lands in it | 10 | optional |
| S12 | Names using a word that names something else on one platform: "stocktakes", "alerts", "between locations", "collections", "categories", "taxonomy" | 10 | optional |
| S13 | CM-CAT-010's count of 2 rests only on statements of other domains' concerns (SH-C-141, E; SA-C-098, D): without them it is a slot | 11 | optional |
| S14 | Kinds that turn on one convention or one gap: CM-CAT-004 and CM-SEL-006 (feature flags only), CM-SEL-003 (a route behind the apps permission), CM-CAT-008 (a Plus-only plan line, Q1's `where` gap), CM-SEL-008 (the maker gap) | 11 | optional |
| S15 | Architecture's claim (plan line 49) doesn't hold as written: for 27 of 56 held cells the data and events, or what decides the capability, can't be derived from the concerns landed in it and the keys its cells cite; derivation by landing gives a coarse concern's statements to its parent, other domains' subjects included | 12 | optional (blocks the plan's claim) |
| S16 | B-woocommerce's notes still argue the old rulings (U-005, U-070 `joined`) in four places | 13 | optional |
| S17 | Q1's gaps that change what a cell can claim are not named in two cells' readings (CM-CAT-008, CM-CAT-011's app type) | 13 | optional |

**Must fix, in one line each:**
- **S3:** B-anchor/rulings.tsv lines 6 (U-016) and 14 (U-082) contradict B-extent.md line 72 and R-dry-run.md check 7; revert to `apart` or change the briefs' rule (proposal under "Conventions").
- **S4:** B-anchor/rulings.tsv lines 3, 9, 11 and B-woocommerce/rulings.tsv line 4 need one row per pair, each with only that pair's keys (rows given below).
- **S7:** B-anchor/evidence.tsv line 95 is CM-CAT-011's only `core`, a partner-access permission; cite the staff permission SA-C-020/decides/SA-S-2395 in the cell, or the kind is `open` under the anchor's own rule for scopes.

## Per check: rows checked, failed, share

| Check | Rows checked | Failed | Share failed | Of which must fix |
|---|---|---|---|---|
| 3. Joins made and not made | 39 (30 landings, 5 Q1 matches, 4 cross-tree citations; the flag on CM-SEL-007 is with the flags) | 4 | 10% | 0 |
| 4. Grains | 28 capabilities | 2 | 7% | 0 |
| 6. Areas | 28 capabilities | 0 | 0% | 0 |
| 7. Rulings | 19 ruling rows (13 anchor, 6 WooCommerce) | 8 | 42% | 6 |
| 8. What the parts never cite | 270 statements (212 of the three platforms, 58 of Zid and BigCommerce) | 24 | 11% of 212 | 1 (SA-S-2395; S7's other 12 rows change no count) |
| 9. Qualities and slot fillers | 18 rows (16 qualities, 2 slot fillers) | 3 | 17% | 0 |
| 10. Names and the anchor's shape | 36 (28 names, 8 WooCommerce landings) | 7 | 19% | 0 |
| 11. The kind rule | 28 capabilities | 7 | 25% | 1 |
| 12. What architecture needs | 56 held cells | 27 | 48% | 0 |
| 13. Other rows | 385 (297 evidence rows, 84 cells, 4 passages of notes) | 7 (1 evidence row, 2 cells, 4 passages) | 2% | 0 |
| The checker's flags | 20 | (resolved below) | | |

A row "failed" when it carries a finding of either verdict. The coverage table, `studies/class-model/review-dry-run-structure-coverage.tsv`, holds every row with its result (927 rows: 907 of the checks above and the 20 flags). No sample was drawn: the brief's depth rule takes every row for checks 3 to 13, and its sample is for check 1's searches, the other reviewer's.

## The findings

### S1. SA-C-020's fit is strained, not clean (check 3; optional)

- **Rows:** B-anchor/landings.tsv line 3 (`salla SA-C-020 CM-CAT-001 match:M-011 clean`).
- **Problem:** SA-C-020 is coarser than CM-CAT-001's tree. Its bundle flags are cited in CM-SEL-006 (B-anchor/evidence.tsv lines 137 to 140: SA-C-020/decides/SA-S-3510, SA-S-3385, SA-S-3297, SA-S-3522) and its donation setting and flags in CM-SEL-007 (lines 142 to 145: SA-C-020/where/SA-S-1760, SA-C-020/decides/SA-S-2616, SA-S-3118, SA-S-3481), two roots of the SEL area. Its filters, sorting, recommendations and custom fields are other domains' (scope.tsv line 214 names D and E under `also`). The brief asks a strained fit to be marked, "and say what doesn't fit" (B-extent.md line 77); the landing reads clean.
- **Evidence:** the cited keys above; `evtab.py` (my scratchpad script) lists SA-C-020 as the only landed concern of domain B whose statements are cited in two other trees.
- **Fix:** B-anchor/landings.tsv line 3: `fit` = `strained`, `reading` adding "its bundle flags are cited in CM-SEL-006 and its donation setting and flags in CM-SEL-007, outside CM-CAT-001's tree". The same holds, more weakly, for SH-C-022, one of whose routes (SH-C-022/decides/SH-S-5024, products:update:locations) is cited in CM-INV-005 (B-anchor/evidence.tsv line 183): a **Reading**: one route, about stock at a location, needs no mark.

### S2. The INV tree: transfers and purchase orders under locations (check 4, with check 3; optional)

- **Rows:** B-anchor/capabilities.tsv line 25 (CM-INV-006, parent CM-INV-005) and line 26 (CM-INV-007, parent CM-INV-006).
- **Problem:** the parent is "a finer part of a coarser thing" (B-extent.md line 72). Shopify's own grouping puts transfers and purchase orders under inventory, beside counts:
  - its entitlement `inventory` holds `enabled`, `counts`, `purchaseOrders` and `transferLocation` as siblings (SH-S-5334). The statement is held under two keys, SH-C-022/decides/SH-S-5334 (cited in CM-INV-001, B-anchor/evidence.tsv line 150) and SH-C-023/decides/SH-S-5334 (cited in CM-INV-006, line 204), so one statement is cited in two trees; the checker compares whole keys and doesn't flag it;
  - the purchase-order permission sits in the subcategory Inventory (`"subCategory":"INVENTORY","subCategoryTitle":"Inventory"`, SH-C-023/decides/SH-S-7156).
  - The anchor's own notes use the entitlement to say it "mark[s] the same cut: tracking (001), counts (003), purchase orders (007), transfers (006)" (B-anchor/notes.md, "Grains chosen"), a cut under inventory, yet hang 006 under locations.
  - Salla's admin links for inventory management, inventory transfer and warehouses and branches are siblings in one flat list (SA-C-025/where/SA-S-1797, SA-C-026/where/SA-S-1798, SA-C-026/where/SA-S-1808: each `"parent": 0, "list": 2`). Only Q1's concern SA-C-026 groups transfer with branches.
  - Purchase orders hang under transfers because their permissions depend on the transfer permissions (`"dependencies":["PRODUCTS","VIEW_INVENTORY_TRANSFERS"]`, SH-S-7156; SH-S-7157). **Reading:** a dependency between permissions isn't a part-of relation, and a purchase order is from a supplier, not "between locations" (S12).
- **Fix (the coordinator's choice; counts and kinds don't change):** B-anchor/capabilities.tsv line 25: parent `CM-INV-001`; line 26: parent `CM-INV-001`. SA-C-026 stays in CM-INV-005, its transfer statements are cited in CM-INV-006 of another tree, so its landing (B-anchor/landings.tsv line 22) is marked `strained`, and U-003 rules two pairs (S4). The alternative is to keep the tree and record in the notes that Shopify's grouping is overridden by Q1's concern.

### S3. U-016 and U-082 can only be `apart` under both briefs (check 7; must fix)

- **Rows:** B-anchor/rulings.tsv line 6 (U-016 `joined:CM-CAT-010`) and line 14 (U-082 `joined:CM-SEL-007`).
- **Problem:** "Where `scope.tsv` puts the candidate's other concern in another domain, the ruling is `apart`, with the basis 'scope.tsv gives <concern> domain <X>'" (B-extent.md line 72); "the ruling can only be `apart`. Don't test it against the definitions" (R-dry-run.md check 7). U-016's Salla side is SA-C-098, domain D (scope.tsv line 266), and SA-C-124, domain C (line 284); U-082's Shopify side is SH-C-187, domain D (line 188). Both were ruled `apart` and changed to `joined` by the coordinator on 30 October "after the checker's ruling test was corrected" (the rows' own bases; B-anchor/notes.md, last section); the corrected test makes `apart` a problem whenever one capability cites keys of both sides. The checker's test and the briefs' rule now contradict each other whenever a capability cites an `also` concern of another domain.
- **Scope's placement of those concerns, tested as check 7 asks:** it holds. SA-C-098's own words are selling: "اعرض منتجاتك في سوق الجملة من سلة، وحدد تسعيرات خاصة لتجار التجزئة" (SA-C-098/boundary/SA-S-5047), at `/channel/vendors` (SA-C-098/where/SA-S-3553), a plan line under the parent code `knoat-albyaa` (SA-C-098/decides/SA-S-2069); its buying side is a staff permission (SA-C-098/decides/SA-S-2456). D with `also` B;E holds. SA-C-124 is money withheld from the merchant's wallet (SA-C-124/boundary/SA-S-0178): C holds. SH-C-187 is loyalty, wishlist and donation apps (SH-C-187/where/SH-S-2581, SH-S-2583): D holds, but it lacks B under `also` (S6).
- **Fix:** either B-anchor/rulings.tsv line 6 → `apart`, basis "scope.tsv gives SA-C-098 domain D and SA-C-124 domain C; the capability CM-CAT-010 cites their sourcing statements under also", and line 14 → `apart`, basis "scope.tsv gives SH-C-187 domain D", with the checker exempting such candidates from its `apart` test; or the briefs change the rule. My proposal is the second (Conventions, 1), since `joined` says what the cells show; until the briefs change, the rows contradict them.

### S4. A candidate of several pairs, ruled in one row (check 7; must fix)

- **Rows and problem:**
  - **B-anchor/rulings.tsv line 3, U-003 `joined:CM-INV-005`.** The candidate asks about SH-C-024 (locations) and SH-C-023 (transfers) against SA-C-026. Its keys include SH-C-023/where/SH-S-1513 and SA-C-026/where/SA-S-1798, cited by CM-INV-006, not CM-INV-005; and SA-C-025/decides/SA-S-3504, of a concern outside the candidate, cited by CM-INV-001. The basis itself says SH-C-023 is "joined by the term inventory transfer with SA-C-026's transfer part" in CM-INV-006.
  - **B-anchor/rulings.tsv line 9, U-059 `joined:CM-CAT-002`.** Its keys include SA-C-029/where/SA-S-1799 (cited by CM-SEL-005) and SH-C-188/where/SH-S-2604 (cited by CM-SEL-006), which stand for pairs the basis says "stay apart"; and SH-C-020/decides/SH-S-7214, of a concern outside the candidate.
  - **B-anchor/rulings.tsv line 11, U-061 `joined:CM-SEL-002`.** Its keys include SA-C-031/where/SA-S-1779 (cited by CM-SEL-004), the bookings pair, which the basis says "lands apart".
  - **B-woocommerce/rulings.tsv line 4, U-059 `joined:CM-SEL-006`.** Its keys include WC-C-104/where/WC-S-0737 and SA-C-021/where/SA-S-1025, cited by CM-CAT-002, not CM-SEL-006. By the checker's own definition, CM-CAT-002's cells cite both sides (B-woocommerce/evidence.tsv lines 30 and 31, WC-S-0737 and WC-S-0738; B-anchor/evidence.tsv line 33, SA-S-1025; line 28, SH-S-2644), so that pair is `joined:CM-CAT-002`.
  - The checker passes all four because it needs only one key of each side cited by the named capability. B-woocommerce already wrote U-061 as two rows (B-woocommerce/rulings.tsv lines 5 and 6), which the checker accepts.
- **Fix: one row per pair, each holding only its pair's keys.**
  - U-003: `joined:CM-INV-005`, keys SH-C-024/decides/SH-S-7010; SH-C-024/where/SH-S-1493; SA-C-026/boundary/SA-S-1616; SA-C-026/decides/SA-S-3516; and `joined:CM-INV-006`, keys SH-C-023/where/SH-S-1513; SH-C-023/decides/SH-S-5188; SA-C-026/where/SA-S-1798; SA-C-026/decides/SA-S-2520.
  - U-059 (anchor): `joined:CM-CAT-002`, keys SH-C-189/where/SH-S-2644; SA-C-021/boundary/SA-S-1031; SA-C-021/where/SA-S-1025; and `apart` for SH-C-188 against SA-C-029, keys SA-C-029/where/SA-S-1799, basis "no Shopify statement holds pre-orders ('Pre-order apps' is a platform term of SH-C-188 only)"; and `apart` for SA-C-077, basis "scope.tsv gives SA-C-077 domain D".
  - U-061 (anchor): `joined:CM-SEL-002`, keys SH-C-190/where/SH-S-2648; SA-C-024/where/SA-S-1029; and `apart` for SH-C-190 against SA-C-031, keys SA-C-031/where/SA-S-1779, basis "SH-C-190's 'Event booking apps' has no statement".
  - U-059 (WooCommerce): `joined:CM-SEL-006`, keys WC-C-104/where/WC-S-0732; WC-C-104/boundary/WC-S-5474; SH-C-188/where/SH-S-2604; and `joined:CM-CAT-002`, keys WC-C-104/where/WC-S-0737; WC-C-104/where/WC-S-0738; SA-C-021/where/SA-S-1025; SH-C-189/where/SH-S-2644.

### S5. Keys that don't stand for what the candidate asks (check 7; optional)

- **U-070, B-anchor/rulings.tsv line 12 and B-woocommerce/rulings.tsv line 7.** Each holds SH-C-020/decides/SH-S-5016, the products route's eligibility (`"permissions":["PRODUCTS"],"entitlements":["products"]`). The candidate asks about "Products > View cost", which no statement holds: my search of Shopify's statements for "cost per item; product cost; View cost; cost of goods; COGS; unitCost; unit cost; costs" found 1 hit, a Global-e flow of funds (SH-C-065/responsible/SH-S-0566); `outscope` for "cost" found only SH-I-2578 (landedCostIncoterms). Both bases say so; the key stands for the absence. **Fix:** drop the Shopify key from both rows and name the gap in the basis, as both already do. The rulings stay `apart`.
- **Keys of concerns outside the candidate** (the checker filters them out unread): U-002, B-anchor/rulings.tsv line 2 (SA-C-020/boundary/SA-S-1597; the candidate holds SA-C-022); U-003, line 3 (SA-C-025/decides/SA-S-3504); U-059, line 9 (SH-C-020/decides/SH-S-7214). **Reading:** a statement of another concern can stand for the candidate's object (a product's category being updated stands for Salla's categories), so this needs a convention, not a change (Conventions, 2).

### S6. scope.tsv: two `also` entries missing (checks 7 and 13; optional, for the coordinator)

- **SH-C-187** (scope.tsv line 188, domain D, `also` empty) is cited in CM-SEL-007 (B-anchor/evidence.tsv line 141, SH-C-187/where/SH-S-2583, "Donation apps"), the checker's flag. Its domain holds (S3), and its donation part is domain B's subject (Salla's quick donation sits in SA-C-020, domain B). **Fix:** scope.tsv line 188: `also` = `B`.
- **WC-C-064** (scope.tsv line 415, `also` empty) holds WooCommerce's product custom fields API (WC-C-064/boundary/WC-S-0096, WC-S-0675), which the WooCommerce part leaves to domain E (B-woocommerce/rulings.tsv line 3). Domain E's parts can cite it only with a flag. **Fix:** scope.tsv line 415: `also` = `E`.
- **The other cases where scope.tsv puts a candidate's concerns in another domain,** tested from their `where` statements, all hold: SH-C-028 E (metafields under `content`, SH-C-028/where/SH-S-5119); SA-C-042 C (`/orders/custom-fields`, SA-C-042/where/SA-S-1780); SH-C-035 E (Search, SH-C-035/where/SH-S-0867); SH-C-141 E (online sales channels, SH-C-141/where/SH-S-0729); SA-C-098 D; SA-C-124 C (S3); SH-C-060 C (section Shipping, SH-C-060/where/SH-S-7140); SA-C-143 C (`/shipping/setting/routes`, SA-C-143/where/SA-S-1872); SH-C-127 D (Discounts and marketing, SH-C-127/where/SH-S-0776); SA-C-071 D (`/marketing/offers`, SA-C-071/where/SA-S-1817); SA-C-077 D (`/marketing/gift`, SA-C-077/where/SA-S-1825); SA-C-032 D (back in stock alerts to buyers, SA-C-032/where/SA-S-1754); SA-C-220 D (Reports, SA-C-220/where/SA-S-1857); SA-C-302 G (migration terms, SA-C-302/where/SA-S-5119); WC-C-105 D (Extensions > Conversion, WC-C-105/where/WC-S-0700).

### S7. CM-CAT-011's count rests on a partner-access permission; the staff permissions go uncited (checks 8 and 11; must fix)

- **Rows:** B-anchor/evidence.tsv line 95 (CM-CAT-011 salla `core` SA-C-020/decides/SA-S-2612), CM-CAT-011's only `core` row; B-anchor/cells.tsv line 23 ("core: a permission for size guides").
- **Problem:** Salla's permissions are held twice. The statement cited is "Permission a partner can request on a merchant's store, group إعدادات المتجر" (the note of SA-S-2612); the same permission as a staff permission, "Staff permission, group إعدادات المتجر" (the note of SA-C-020/decides/SA-S-2395), is uncited. The anchor's own rule is that API folders, objects and scopes are `shows`, "so no `core` rests on boundary statements alone" (B-anchor/notes.md, "Placements"); a grant an app requests is nearer a scope than an admin setting (**Reading**). The cell's other row is the size-guides flag of `"type": "app"` with an install link (SA-C-020/decides/SA-S-3461, line 96, `shows`). If the partner permission is `shows`, Salla's cell is `not-stated`, the count is 0 and the kind `open`.
- **The same pattern, without a change of count:** 12 more Salla `core` rows cite the partner list while the staff permission of the same key is uncited: B-anchor/evidence.tsv line 20 (SA-S-2471; staff SA-C-020/decides/SA-S-2254), 48 (SA-S-2472; staff SA-C-022/decides/SA-S-2255), 58 and 59 (SA-S-2477, SA-S-2476; staff SA-C-023/decides/SA-S-2260, SA-S-2259), 117 (SA-S-2478; staff SA-C-024/decides/SA-S-2261), 127 (SA-S-2508; staff SA-C-031/decides/SA-S-2291), 132 (SA-S-2479; staff SA-C-029/decides/SA-S-2262), 143 (SA-S-2616; staff SA-C-020/decides/SA-S-2399), 161 (SA-S-2473; staff SA-C-025/decides/SA-S-2256), 163 (SA-S-2620; staff SA-C-025/decides/SA-S-2403), 171 (SA-S-2469; staff SA-C-025/decides/SA-S-2252), 189 (SA-S-2622; staff SA-C-026/decides/SA-S-2405). CM-INV-006 cites both lists (lines 209 to 213), and CM-CAT-010 the staff one (line 93).
- **Fix:** B-anchor/evidence.tsv: add `CM-CAT-011 salla core SA-C-020/decides/SA-S-2395` ("staff permission, size guides, store settings"), and for each of the 12 rows above add the staff key beside the partner key. Whether the partner keys stay `core` or become `shows` is the other reviewer's (check 2); the convention is in "Conventions", 4.

### S8. Uncited statements that bear on a capability or a cell (check 8; optional)

Of the 212 uncited statements of the three platforms, 188 hold (duplicates of cited statements, events and scopes of their landing's capability, other domains' subjects, general third-party terms: each is a coverage row with its reason); 13 are S7's staff permissions; the 11 below bear on the model, and the parts' notes name most of them without a row:
- **Product pricing, a capability the model lacks:** Salla's settings entry "Automatic pricing" (SA-C-020/where/SA-S-1751) and its `metal-pricing` flag (SA-C-020/decides/SA-S-3515); WooCommerce's Marketplace category Pricing (WC-C-104/where/WC-S-0735). B-anchor's rule for making a capability (B-anchor/notes.md, "How I cut", rule 3) admits "an admin section or route ... a plan line or an entitlement", which SA-S-1751, a settings entry, meets (**Reading**). **Fix:** the coordinator rules whether a pricing capability is made (a root of CAT, Salla `core`, WooCommerce `extension-point`), and the brief states the rule (Conventions, 3).
- **Leads with no stated meaning, to record as gaps in the notes:** `restriction-product-type` (SA-C-020/decides/SA-S-3351, for CM-CAT-009); `inventory-order` (SA-C-025/decides/SA-S-3495, for CM-INV-007 or CM-INV-001); `product-sale-start` (SA-C-020/decides/SA-S-3490, scheduled sale, no capability); bins inside a location (SH-C-024/decides/SH-S-5201, behind a beta, for CM-INV-005); `allow_negative_quantities` inside SA-C-025/decides/SA-S-3504 (selling below zero stock, no capability; my search for "backorder; oversell; continue selling; negative quantit; out of stock; out-of-stock; low stock; low_stock; notify_low" found nothing on Shopify and one WooCommerce statement, on hiding out-of-stock items, WC-C-105/decides/WC-S-5476; Salla's "backorder; negative; allow_negative; out of stock; نفد; نفاد; نفاذ; الكمية السالبة" found 4, none beyond SA-S-3504's value).
- **Cells' evidence:** the staff permissions `inventory_browse` and `inventory_management` sit in the group نقل المخزون (SA-C-025/decides/SA-S-2307, SA-S-2308, "Staff permission, group نقل المخزون"), which bears on CM-INV-006's decides, not CM-INV-001's; the staff permission `product_browse` (SA-C-020/decides/SA-S-2253) bears on CM-CAT-001 as permission evidence; Salla's app scope `subscriptions` (SA-C-125/boundary/SA-S-1567), left uncited as held under two concerns, bears on CM-SEL-001's boundary (check 12).
- **Not citable, a gap:** Shopify's unplaced store feature `sellsSubscriptions` (SH-I-2594, `outscope`), which bears on CM-SEL-001's Shopify cell; an inventory entry may be cited only for a quality (B-extent.md line 42).
- **Zid and BigCommerce:** 58 uncited statements of ZD-C-043, ZD-C-083 to 085 and BC-C-001 to 008 are for their mapping parts; none is read here.

### S9. `max_inventory_types` may bear on locations (check 9; optional)

- **Row:** B-anchor/qualities.tsv line 10 (CM-INV-001 salla `max_inventory_types` 5, SA-C-025/decides/SA-S-3504).
- **Problem:** the flag's value holds `"max_inventory_types": 5, "allow_negative_quantities": false, "enable_branch_inventories": true`. **Reading:** the limit beside "branch inventories" reads as a number of inventories, which is CM-INV-005's subject; no statement says which.
- **Fix:** keep it, with the cell's note naming the doubt, or move it to CM-INV-005; and record in the notes that the statement doesn't say what an inventory type is.

### S10. Slot fillers read from feature-flag names (check 9; optional)

- **Rows:** B-anchor/slot-fillers.tsv line 2 (CM-CAT-004 Google, SA-C-022/decides/SA-S-3506) and line 3 (CM-SEL-001 Apple Pay, SA-C-125/decides/SA-S-3302).
- **Problem:** neither statement names a third party "as doing the capability, or as setting its terms" (B-extent.md line 106) beyond a flag's name; SA-S-3302's flag is `"released": false`. Neither has a market in its scope ("plans: plus, pro, special"; "the answering store"), and a filler "is each market's setup". The same reading of a name would make `virtooal` (SA-C-020/decides/SA-S-3476, an app-type feature for CM-CAT-007) a filler, and no row records it.
- **Fix:** a convention (Conventions, 9): either a flag's name is not a statement that a third party does the capability, and both rows go to the notes; or it is, and `virtooal` is added. The checker should derive a filler's scope as it does a quality's.
- **Qualities the statements show that no row records:** none found. Plan restrictions such as "the store must not be on the Starter or Retail plans" (SH-C-021/decides/SH-S-6278, SH-S-6280) are scopes, which derived.tsv holds, not qualities.

### S11. CM-SEL-002's name lacks WooCommerce's term (check 10; optional)

- **Row:** B-anchor/capabilities.tsv line 14 ("Digital products (Shopify digital goods; Salla Digitals Product, digital codes and files)").
- **Problem:** WC-C-066 lands in it (B-woocommerce/landings.tsv line 3), and its term is "Downloadable products" (WC-C-066/where/WC-S-0014). WooCommerce's one statement saying "digital" is about VAT (B-woocommerce/notes.md, "Joins"), so "Digital products" is the other two platforms' word, not a neutral one. Every other capability with a WooCommerce landing names WooCommerce's term or a shared one.
- **Fix:** "Digital products: downloadable files and digital codes (Shopify digital goods; Salla Digitals Product, digital codes and files; WooCommerce downloadable products)". Who renames after a mapping part is a convention (Conventions, 6).

### S12. Words that name something else on one platform (check 10; optional)

| Capability (B-anchor/capabilities.tsv line) | Word | What it names elsewhere | Fix |
|---|---|---|---|
| CM-INV-003 (line 22) | "stocktakes" | Salla's جرد المنتجات والمخزون, literally a stocktake, which the anchor reads as its inventory view (SA-C-025/decides/SA-S-2096: "تتبّع حالة المخزون وعدد المنتجات المباعة والمتبقية") | "Inventory counts (Shopify inventory counts)" |
| CM-INV-004 (line 23) | "alerts" | WooCommerce's cell is a list of products low in stock (WC-C-068/boundary/WC-S-0219) | "Low stock: alerts and lists", if the cell stands (the other reviewer's) |
| CM-INV-006 (line 25) | "between locations" | Shopify's transfers link purchase orders (SH-C-023/decides/SH-S-6221), and its child CM-INV-007 is purchase orders from suppliers | "Inventory transfers and shipments" |
| CM-CAT-003 (line 4) | "collections", "categories" | WooCommerce's Store API collection-data route (WC-C-064/boundary/WC-S-0172); Shopify's product categories read by its tax (SH-C-100/decides/SH-S-7221, per B-anchor/notes.md "Homonyms") | "Store product groupings ..." and both homonyms in `note` |
| CM-CAT-004 (line 5) | "taxonomy" | WordPress taxonomies (WC-C-064/where/WC-S-0907) | the homonym in `note` |
| CM-CAT-009 (line 10) | "restrictions" | WooPayments' prohibited product types (WC-C-011/decides/WC-S-0523, per B-woocommerce/notes.md) | the homonym in `note` |

**The anchor's shape, for every WooCommerce landing:** WooCommerce's `where` groupings cut as the capability does for seven of eight. WC-C-064 (Products > Categories, Tags, Brands, Attributes) cuts as CM-CAT-001's tree; WC-C-066 (Products > Downloadable products) is a product type, which is what SEL holds ("Product types and selling models"); WC-C-068 (Products > Inventory), WC-C-093 (`_cogs_value`), WC-C-100, WC-C-101, WC-C-102 (Extensions > Merchandising > each) cut as their capabilities, the channel aside. WC-C-104 (Extensions > Merchandising and its eight subcategories) cuts across CM-SEL-006, CM-CAT-002 and other domains' subjects: it is marked `strained`, which is right; no rename or re-cut, since a Marketplace group is a channel, which never sets a capability.

### S13. CM-CAT-010's count rests only on other domains' statements (check 11; optional)

- **Rows:** B-anchor/evidence.tsv lines 87 and 88 (Shopify `core`: SH-C-141/decides/SH-S-7013, the Collective plan row; SH-C-141/where/SH-S-0729), lines 92 and 93 (Salla `core`: SA-C-098/decides/SA-S-2069, SA-S-2456).
- **Problem:** every `core` row of CM-CAT-010 is a statement of a concern of another domain (E and D) cited under `also`; the B concern landed in it, SH-C-185, holds only App Store categories (`extension-point`). Without those four rows the cells are `extension-point` on all three platforms and the kind is `slot`. **Reading:** the same plan rows are what domain E's channel capability (Collective) and domain D's B2B one (the wholesale market) would cite as `core`, so one statement would count in two domains. The brief allows the citation (B-extent.md line 42) and is silent on the count.
- **Fix:** a convention (Conventions, 8). The rows can stay; class_kinds.py should print, for each count, whether it rests only on `also` concerns.

### S14. Kinds that turn on one convention or one gap (check 11; optional)

See "The kind rule" below for each capability. The fragile ones: CM-CAT-004 (Salla's two flags, B-anchor/evidence.tsv lines 55 and 56, one unreleased); CM-SEL-006 (Salla's four flags, lines 137 to 140, one unreleased, all scoped to plans or the answering store); CM-SEL-003 (an admin route that needs the APPLICATIONS permission, lines 122 and 123; the cell's reading itself says a reviewer may prefer `shows`), which becomes `open`; CM-CAT-008 (a plan row included on Plus only, line 80, with Q1's gap "observation needed" on SH-C-038's `where`); CM-SEL-008 (a slot until a statement names WooCommerce Memberships' maker, Q1's gap WC-C-102/boundary). **Fix:** settle the flag convention (Conventions, 4) and report each kind with the scope it holds under (Tests, 9).

### S15. What architecture needs (check 12; optional, but the plan's claim doesn't hold)

- **The claim:** "The data and events, and what decides each capability, come from the statements of each capability's concerns, so the merge derives them per capability: no part writes more. *To confirm with the dry run's review.*" (`architecture/plan.md` line 49).
- **What I found** (my scratchpad script `arch.py`, per held cell: the boundary and decides statements of the concerns of its platform landed in the capability, and the boundary and decides keys its cells cite). Of 56 held cells, 27 fail, 48%:
  - **18 cells have no boundary statement by either route,** so no data or events: CM-CAT-004 salla; CM-CAT-007 woocommerce; CM-CAT-009 salla (SA-C-028 holds none: Q1's gap "page not read"); CM-CAT-010 salla and woocommerce; CM-CAT-011 salla; CM-INV-002 shopify and salla; CM-INV-003 shopify; CM-INV-006 salla; CM-INV-007 shopify; CM-INV-008 woocommerce; CM-SEL-003 shopify; CM-SEL-005 salla (SA-C-029: "page not read"); CM-SEL-006 salla; CM-SEL-007 shopify and salla; CM-SEL-008 woocommerce. These are children sharing a coarse concern landed in their parent (CM-CAT-004, CM-CAT-011, CM-INV-002, -003, -006 salla, -007, -008, CM-SEL-003), capabilities resting on other trees' or other domains' concerns (CM-CAT-010, CM-SEL-006 salla, CM-SEL-007), and concerns holding no boundary statement (SA-C-028, SA-C-029, WC-C-102).
  - **9 more cells have no decides statement by either route:** CM-CAT-002, -003, -005, -006 woocommerce; CM-CAT-004, -006, -007 shopify; CM-INV-004 woocommerce; CM-SEL-006 woocommerce. (Four of the 18 above lack both: CM-CAT-007 and CM-CAT-010 woocommerce, CM-SEL-007 shopify, CM-SEL-008 woocommerce.) WooCommerce's attributes, for example, are gated by `manage_product_terms`, which sits in a `where` statement (WC-C-064/where/WC-S-0055), not a `decides` one.
  - **11 cells get their events only from cited keys,** having no concern of their platform landed in them (CM-CAT-002, -003, -005, -006 woocommerce; CM-CAT-004, -006, -007 shopify; CM-CAT-006, -007 salla; CM-INV-004 salla and woocommerce). The parts cite a sample of each family of topics, so a merge by citation misses the rest of the families they cite from, and a merge by landing gives them to the parent: for example SA-C-020/boundary/SA-S-1592 and SA-S-1593 (product.updated, product.deleted), SA-C-023/boundary/SA-S-1614 and SA-S-1615 (brand.updated, brand.deleted), SA-C-026/boundary/SA-S-1617 to SA-S-1620 (the branch topics).
  - **A merge by landing over-attributes:** WC-C-064's 39 boundary statements would all go to CM-CAT-001; its children cite 17, CM-CAT-001 cites 10, and the 12 uncited include the analytics endpoints (WC-S-0213 to WC-S-0217) and the product custom fields API (WC-S-0096, WC-S-0675) that the WooCommerce part judged other domains' (B-woocommerce/notes.md, "Statements of my concerns left uncited"); SH-C-020's storefront listing scopes (SH-S-6152 to SH-S-6157) likewise.
- **What the merge would need:** an attribution rule, so that a statement goes to every capability whose cells cite it, and an uncited statement of a landed concern goes to the capability where the concern landed; and, for that rule to be right, either every part cites each boundary and decides statement that bears on a capability (as `shows` where it supports no placement), or it records each uncited statement with where it bears (a structured `uncited.tsv`: key, capability or domain, reason) in place of the prose the notes hold now. Either is a part writing more. The capabilities with no boundary statement at all are gaps to record, not derivations. **Fix:** the plan's line 49 is changed to say which, and the brief adds it (Conventions, 10).

### S16. Stale notes in B-woocommerce (check 13; optional)

- **Rows:** B-woocommerce/notes.md line 97 (U-005 `joined:CM-CAT-001`), line 106 (U-070 `joined:CM-CAT-012`), line 248 ("`joined` is forced by the model's trees"), and item 7 under "Where the brief left me to judge" ("which makes U-070 `joined` by grain").
- **Problem:** B-woocommerce/rulings.tsv lines 3 and 7 now read `apart`; only the coordinator's note at the end of the file says so. A later part reading "Rulings" is misled.
- **Fix:** mark each passage "superseded by the coordinator's correction of 30 October (below)".

### S17. Q1's gaps a cell's reading should name (check 13; optional)

- **B-anchor/cells.tsv line 16 (CM-CAT-008 shopify):** Q1 records SH-C-038/where as "observation needed: Where Shopify places combined listings (the Shopify Combined Listings app and the admin pages it adds)" (`gaps`). The cell's `core` rests on a Plus plan row, which the brief allows; the reading names the maker gap but not this one, which is the gap that could move the cell to `own-service` or `extension-point` and the capability to `slot`.
- **B-anchor/cells.tsv line 23 (CM-CAT-011 salla):** the reading says "a permission" without saying it is one a partner can request (S7).
- **Held:** WC-C-102's gaps are named in its cell (B-woocommerce/cells.tsv line 21); SA-C-028's and SA-C-029's "page not read" on `boundary` change no claim the cells make (they claim no boundary) but leave check 12's data empty (S15).

## What holds, where no finding is made

- **Check 3, joins made.** The four Q1 matches landed (M-011, M-012, M-074, M-076) and M-081 each sit in one tree. The joins on role hold as readings: collections and categories (B-anchor/landings.tsv line 7) both show a grouping the store defines and fills with products (SH-C-021/boundary/SH-S-6097: "a product is manually added or removed from the collection"; SA-C-020/boundary/SA-S-1597, a product's category updated); locations and branches (lines 21 and 22) both show where stock is held (SH-C-024/decides/SH-S-7010, "Inventory locations"; SA-C-026/decides/SA-S-3516, `unlimited-quantity-by-branch`); downloadable and digital products (B-woocommerce/landings.tsv line 3) both show a product whose content the buyer receives as a file (WC-C-066/decides/WC-S-5395; SA-C-024/decides/SA-S-3498, `digital-file`), Shopify's side being a category heading only. The joins on terms name one object on both sides: variant (B-anchor/landings.tsv line 5), inventory transfer (line 23), bundle (B-woocommerce/landings.tsv line 9). The three strained fits (B-anchor/landings.tsv lines 15 and 18; B-woocommerce/landings.tsv line 9) are rightly strained and needn't be split: their other parts have no statement ("Event booking apps", "Pre-order apps") or are other domains' subjects (upsell, gifts, order options, display).
- **Check 6, areas.** All 28 hold. CM-CAT-009's is a **Reading**: no statement says what a product restriction limits (scope.tsv line 222 reads "limits on buying a product"); CM-SEL-004 stays SEL though Salla's link sits under orders (`/orders/reservations`, SA-C-031/where/SA-S-1779), since the channel doesn't set the area.
- **Check 13, the other bullets.** No landing is `moved:`, and no landed concern reads as another domain's (each scope.tsv reason holds against its `where` statements). Every citation of another domain's concern names B under `also` except SH-C-187's (S6). One cited statement holds inference in its note, WC-C-100/decides/WC-S-5351 ("Inference: as a premium extension, it runs only where the merchant has bought and installed it"); the cell cites it as `shows` and rests its `extension-point` on the Marketplace category (B-woocommerce/cells.tsv line 14, evidence.tsv lines 49 and 50), so the inference is not carried into a placement.

## The checker's flags, and how each was resolved

| Part, file, line | Flag | Check | Resolution |
|---|---|---|---|
| B-anchor evidence.tsv 141 | SH-C-187/where/SH-S-2583 is of domain D without B under also | 13 | Holds as cited; scope.tsv should name B (S6); its ruling U-082 (S3) |
| B-anchor cells.tsv 10 | CM-CAT-005 shopify none-held, 9 hits | 5 | The other reviewer's |
| B-anchor cells.tsv 18 | CM-CAT-009 shopify none-held, 3 hits | 5 | The other reviewer's |
| B-anchor cells.tsv 30 | CM-SEL-004 shopify none-held, 1 hit | 5 | The other reviewer's; for check 4, SH-C-190's "Event booking apps" has no statement (S4) |
| B-anchor cells.tsv 43 | CM-INV-003 salla none-held, 2 hits | 5 | The other reviewer's; for check 10, the name's "stocktakes" (S12) |
| B-anchor cells.tsv 51 | CM-INV-007 salla none-held, 13 hits | 5 | The other reviewer's; for check 8, `inventory-order` (S8) |
| B-anchor capabilities.tsv 19 | CM-SEL-007 has no concern landed in its tree | 3 | Holds as a root: neither CAT-001 (donations aren't part of the product record) nor any SEL capability is its parent, from the cited statements (B-anchor/evidence.tsv lines 141 to 145). Its data are S15's, its ruling S3's |
| B-woocommerce cells.tsv 5 | CM-CAT-004 woocommerce none-held, 1 hit | 5 | The other reviewer's; the hit is a homonym (S12) |
| B-woocommerce cells.tsv 10 | CM-CAT-009 woocommerce none-held, 7 hits | 5 | The other reviewer's |
| B-woocommerce cells.tsv 16 | CM-SEL-003 woocommerce none-held, 1 hit | 5 | The other reviewer's |
| B-woocommerce cells.tsv 25 | CM-INV-004 woocommerce core rests only on boundary statements | 1 | The other reviewer's; for check 10, the name (S12) |
| B-woocommerce cells.tsv 26 | CM-INV-005 woocommerce none-held, 20 hits | 5 | The other reviewer's |
| B-woocommerce cells.tsv 27 | CM-INV-006 woocommerce none-held, 9 hits | 5 | The other reviewer's |
| B-woocommerce cells.tsv 28 | CM-INV-007 woocommerce none-held, 2 hits | 5 | The other reviewer's |
| B-backfill cells.tsv 2 | CM-CAT-012 shopify none-held, 9 hits | 5 | The other reviewer's; my own search for U-070 found no product cost (S5) |
| B-backfill cells.tsv 3 | CM-CAT-012 salla none-held, 18 hits | 5 | The other reviewer's; my search ("تكلفة; التكلفة; cost; سعر التكلفة", 12 hits) found shipping costs and fees, no product's cost |
| B-backfill cells.tsv 4 | CM-SEL-008 shopify none-held, 52 hits | 5 (11) | The other reviewer's; for the kind, my search found 0 (below) |
| B-backfill cells.tsv 5 | CM-SEL-008 salla none-held, 48 hits | 5 (11) | The other reviewer's; for the kind, my search found 0 (below) |
| B-backfill cells.tsv 6 | CM-INV-008 shopify none-held, 30 hits | 5 | The other reviewer's |
| B-backfill cells.tsv 7 | CM-INV-008 salla none-held, 92 hits | 5 | The other reviewer's |

## The kind rule (check 11)

**The rule as coded** (`method/class_kinds.py` lines 9 to 12 and 59): the count is the number of platforms whose held cell places the capability `core` or `own-service`; `class` where the count is at least 1; `slot` where every platform with statements places it only `extension-point` or `outside`; otherwise `open`. `none-held` and `no cell` never count as lacking it.

**Each capability.** Count and kind from `class_kinds.py`; what the count rests on from my script `countbasis.py` (the `core` rows, their concerns' domains and their scopes).

| Capability | Count | Kind | What the count rests on | Holds? |
|---|---|---|---|---|
| CM-CAT-001 | 3 | class | admin routes, settings, plan lines, WooCommerce's menus and API | holds |
| CM-CAT-002 | 3 | class | Shopify's 100-variant line and barcode route; Salla's link, plan line, flags; WooCommerce's attributes menu and API | holds |
| CM-CAT-003 | 3 | class | admin routes and entitlements; Salla's link, plan line, permission (partner list, S7), flag | holds |
| CM-CAT-004 | 1 | class | two Salla flags, plans plus, pro, special; `salla-taxonomy` unreleased | holds under the flag convention (S14) |
| CM-CAT-005 | 2 | class | Salla's settings entry, permissions (partner list), flag; WooCommerce's menu and Store API | holds |
| CM-CAT-006 | 2 | class | Salla's plan line and flag (scoped); WooCommerce's menu and API | holds |
| CM-CAT-007 | 2 | class | Shopify's `try-media-gen` route (a media generation route: the other reviewer's); Salla's flags (scoped) | holds by Salla alone |
| CM-CAT-008 | 1 | class | one Shopify plan row, Plus only | holds under Plus; Q1's `where` gap (S14, S17) |
| CM-CAT-009 | 1 | class | Salla's admin link, plan line (سلة برو), flag (pro, special) | holds |
| CM-CAT-010 | 2 | class | only statements of SH-C-141 (E) and SA-C-098 (D) | turns on S13 |
| CM-CAT-011 | 1 | class | one Salla permission a partner can request | **fails** until the staff permission is cited (S7) |
| CM-CAT-012 | 1 | class | WooCommerce's product field, setting and REST schema | holds |
| CM-INV-001 | 3 | class | admin sections, settings, permissions, plan lines | holds |
| CM-INV-002 | 2 | class | Shopify's history route (behind a beta, SH-S-5193); Salla's link, permission, flag | holds; Shopify's under a beta |
| CM-INV-003 | 1 | class | Shopify's count routes (behind a beta, SH-S-5194, SH-S-5196) and three staff permissions | holds |
| CM-INV-004 | 2 | class | Salla's flag (scoped); WooCommerce's analytics API (the flag on line 25) | holds by Salla alone |
| CM-INV-005 | 2 | class | admin sections, plan rows, permissions | holds |
| CM-INV-006 | 2 | class | admin routes, entitlement, staff and partner permissions | holds |
| CM-INV-007 | 1 | class | Shopify's routes, permissions (shown by an option, SH-S-7156's `visibleBy`), entitlement | holds |
| CM-INV-008 | 1 | class | WooCommerce's setting | holds |
| CM-SEL-001 | 2 | class | Shopify's admin routes; Salla's two flags, both unreleased in the answering store (SA-S-3301, SA-S-3302) | holds by Shopify alone |
| CM-SEL-002 | 2 | class | Salla's link, plan line, permission, flags; WooCommerce's setting and API | holds |
| CM-SEL-003 | 1 | class | Shopify's route behind the APPLICATIONS permission | turns on S14; `open` if `shows` |
| CM-SEL-004 | 1 | class | Salla's link, plan line, permission, flag | holds |
| CM-SEL-005 | 1 | class | Salla's link, permission, flag | holds |
| CM-SEL-006 | 1 | class | four Salla flags, scoped; one unreleased | turns on S14; `open` if flags are `shows` |
| CM-SEL-007 | 1 | class | Salla's settings entry, permission, flags | holds |
| CM-SEL-008 | 0 | slot | WooCommerce's Marketplace category only | holds: my searches for "membership; members only; member-only; members-only; paid member; member pricing; exclusive access" (Shopify, 0 hits) and "membership; عضوية; العضوية; عضويات; العضويات; اشتراك العضوية; للأعضاء; الأعضاء" (Salla, 0 hits) found nothing that shows it in a core |

**Scopes and the missing platforms.** A count of 1 that holds under one plan (CM-CAT-008, Plus), one beta (CM-INV-003's routes) or flags read in one answering store (CM-SEL-006) is still the platform's own; the kind doesn't change, but the table above should travel with it (Tests, 9). With three of five platforms, a `class` can only stay `class` as Zid and BigCommerce are mapped (the count can only grow), while a `slot` (CM-SEL-008) or an `open` is provisional until all five are read: one `core` cell of Zid or BigCommerce makes CM-SEL-008 a class.

**No `open` case occurs in the dry run.** Three would occur under one changed reading each: CM-SEL-003 (Shopify's route read as `shows`: one platform `not-stated`, the others `none-held`), CM-SEL-006 (Salla's flags read as `shows`: Salla `not-stated`, Shopify and WooCommerce `extension-point`, the mixed case), CM-CAT-011 (S7).

**My proposal for `open`.** An `open` capability is one the statements show while placing it nowhere on at least one platform that shows it. The rule should:
1. **Never fold it into `class` or `slot`.** `not-stated` means the statements give the capability's terms and no placement; reading it as third-party makes a `slot` from silence, and reading it as core makes a `class` from silence. Both claim more than the statements say, which the plan's three kinds of claim forbid.
2. **Report two kinds of `open`:** `open: third parties where stated` (some platform places it `extension-point` or `outside`, another is `not-stated`), and `open: unplaced` (every platform that shows it is `not-stated`). The first leans to `slot` and the second to nothing; both say which statement would settle them.
3. **List, for each `not-stated` cell, the gap that would place it:** Q1's gap on that concern's `where` or `decides`, or a handoff for capture (`handoffs/`), so the review of the next domain or a capture run can close it. An `open` is closed only by a statement, never by the coordinator's judgment.
4. **Count it apart** in the class's counts: class, slot and open each with their numbers, so a reader never takes an `open` for a gap in the class or for a slot.

Why: the count reads only placements that rest on cited statements, and `open` is exactly the set where they don't; keeping it visible, with the statement that would settle each, is what keeps the count a fact rather than a reading.

## Conventions the brief should settle

1. **Rulings and other domains (S3).** Today the briefs say `apart` and the checker says `joined`. Proposal: a ruling says what the cells show: `joined:<cap>` where one capability's cells cite keys of both sides, even when one side is an `also` concern of another domain; its basis then names that concern's domain ("scope.tsv gives SA-C-098 domain D; cited under also"). A concern of another domain that doesn't name the domain under `also` is cited as the brief allows now, with its flag, and the coordinator then adds the domain to its `also` (S6). Both briefs' sentence is then changed, and the reviewer tests the scope placement as now.
2. **One ruling row per pair (S4, S5).** A candidate holding several concerns on a side gets one row per pair of concerns it asks about (or per concern of the part, as B-woocommerce did), each with only that pair's keys. A side with no statement for the object gets no key, and the basis names the gap and the terms searched. A key may be a statement of a concern outside the candidate only where the basis says why.
3. **What makes a capability (S8; B-anchor's rule 3, B-woocommerce's CM-INV-008).** The brief should state the anchor's rule, so every part applies it: a capability is made where a concern lands in it, or where a platform gives the thing a place of its own (an admin section or route, a setting, a permission, a webhook topic, a plan line, an entitlement) and it is about the product or its stock, not how the storefront shows it; a single feature flag alone is not enough. Then Salla's "Automatic pricing" is decided by the rule, not by each part.
4. **`core` from Salla's permissions and flags (S7, S14).** Which list is cited: the staff permission (an admin setting the merchant's staff are granted) as `core`, the permission a partner can request as `shows`, like a scope. Whether a feature flag alone supports `core`, and an unreleased one (`"released": false`). And one rule on API rows for every part: the anchor reads them `shows`, WooCommerce's part `core` (B-woocommerce/notes.md, "Problems"); the other reviewer's checks test the cells, the brief settles the rule.
5. **`strained` covers spills (S1).** A concern whose statements are cited outside its landing's tree is `strained`, with the capabilities that cite it named.
6. **Names after mapping (S11).** A mapping part that lands a concern in an existing capability adds its platform's term to the name where the name doesn't already hold it or a neutral word for it, and says so in its notes; or the coordinator does it when merging. Each homonym a part finds goes in the capability's `note`.
7. **Parents (S2).** `parent` means a finer part of a coarser thing, shown by a platform's own grouping (an entitlement, a permission subcategory, an admin section); a dependency between permissions isn't one. Where the platforms' own groupings and Q1's concerns cut differently, the brief should say which wins (the brief's line 8 says the structure follows the platforms' own groupings).
8. **Counts from `also` concerns (S13).** Whether a statement of an `also` concern of another domain may make a capability's count here, when its own domain's capability will count it too. Proposal: it may, and `class_kinds.py` marks such counts, so the class's count says how many rest only on statements another domain also counts.
9. **Slot fillers (S10).** Whether a flag's name naming a third party is a statement that it does the capability; and a filler's market comes from a market scope only, so a plan or "the answering store" gives none.
10. **What the merge reads (S15).** Either parts cite every boundary and decides statement that bears on a capability, as `shows` where it supports no placement, or they record their uncited statements in a structured file; and the merge's attribution rule (cited, else landing) is written in the plan.
11. **Kinds carry their scope (S14).** A kind resting on one plan, beta, country or answering store is reported with it.
12. **`open`** as proposed above.

## Tests the checker should add

Each is stated so it can be coded against the part's files and the concern map.

1. **A joined ruling's keys:** for `joined:<cap>`, every key of the row must be cited by `<cap>`'s cells (any platform); for `nested:<cap>`, every key by `<cap>` or one of its ancestors. A key cited by neither is a problem naming the capability that does cite it.
2. **Keys of the candidate's concerns:** a ruling key whose concern is not among the candidate's concerns is a flag ("not of the candidate: say why in basis").
3. **Other domains:** where every concern of the candidate's other side is of another domain in scope.tsv, the ruling must be `apart` with a basis naming "scope.tsv gives" (as the briefs stand), or, under Convention 1, its basis must name those concerns' domains; either way the current `apart` test must not contradict it.
4. **Several pairs:** where a candidate holds more than one concern of a side and the part rules it in one row, flag "one row per pair?" when the row's keys are cited by more than one capability, or by none.
5. **One statement, two keys:** group evidence keys by their statement id (the last part of the key); a statement id cited by capabilities of two trees under any keys is the same flag as today's "cited in more than one tree".
6. **Spills:** a statement of a landed concern cited by a capability outside the tree where the concern landed is a flag ("strained?"), unless the landing's fit is `strained`.
7. **Counts resting on other domains:** `class_kinds.py` marks a count that rests only on rows of concerns of other domains (CM-CAT-010).
8. **Fragile counts:** `class_kinds.py` marks a count of 1 that rests on a single `core` row, or only on feature flags (identifier with a `"type": "feature"` value), or only on Salla's partner-access permissions (statements whose note begins "Permission a partner can request").
9. **Kind scope:** for each count-making cell, `class_kinds.py` prints whether every `core` row is scoped (from `derived.tsv`'s `scopes`), and the scopes.
10. **Partner and staff permissions:** a Salla `core` row citing a partner-access permission where the staff permission of the same `name` is held uncited is a flag ("cite the staff permission").
11. **Names:** a capability in which a concern of platform P lands, whose name holds neither "P" (Shopify, Salla, WooCommerce, Zid, BigCommerce) nor any term of P's cell, is a flag.
12. **Architecture:** a held cell with no boundary statement by landing (a concern of its platform landed in the capability, with a boundary statement) or by citation is a flag for the merge ("no data or events").
13. **Slot fillers' scope:** derive each filler's scope into a `derived-slot-fillers.tsv`, and flag a filler whose scope names no market.
14. **Stale rulings:** a ruling id and value named in `notes.md` (pattern "U-nnn `joined:...`" or "`apart`") that differs from `rulings.tsv` is a flag.

## For the other reviewer (placements noticed, not pursued)

- CM-CAT-011 salla and 12 other Salla `core` rows rest on partner-access permissions (S7).
- CM-CAT-007 shopify: its only `core` is the route `product:try-media-gen` (SH-C-020/where/SH-S-5025), a media generation route, not the product's media.
- CM-SEL-001 salla: both `core` rows are flags unreleased in the answering store (SA-C-125/decides/SA-S-3301, SA-S-3302).
- CM-SEL-003 shopify: the route needs the APPLICATIONS permission (SH-C-190/decides/SH-S-5095); the cell's own reading allows `shows`.
- CM-INV-004 woocommerce: a list of products low in stock (WC-C-068/boundary/WC-S-0219), not an alert; and the anchor and WooCommerce read API rows differently (Conventions, 4).
- CM-INV-003 salla: the plan line's description ("تتبّع حالة المخزون وعدد المنتجات المباعة والمتبقية والتي قاربت على الانتهاء", SA-C-025/decides/SA-S-2096) also bears on CM-INV-004.
