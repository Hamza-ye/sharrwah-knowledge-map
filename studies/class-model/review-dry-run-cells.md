# The dry run's review: the cells (checks 1, 2 and 5)

One of two independent reviews of domain B's dry run, under `studies/class-model/briefs/R-dry-run.md`. This one takes the cells: check 1 (every placement against all of the concern map's statements), check 2 (each `supports` value against the brief's tests) and check 5 (each `none-held` cell). The other reviewer takes checks 3, 4 and 6 to 13. I made none of the parts.

## What I read, and at which commit

- **Repository:** `sharrwah-knowledge-map`, branch `claude/vibrant-meitner-oh70v4`, read at `82868b7b` (the back-fill's commit). The coordinator's commits made while I worked change only `STATE.md` and `method-report.md` (`4fdfcda2`) and save the two reviews in progress (`42d78d62`): the parts, the concern map and the scripts are the same throughout. I made no commits.
- **Briefs:** `studies/class-model/briefs/R-dry-run.md`; `studies/class-model/briefs/B-extent.md`.
- **Evidence:** each cell's concerns' statements under all five placements, through `python3 -I method/class_slice.py statements --platform P --concerns ID --width 160`, once per concern; whole statements through `key`; the platforms' other statements through `search`. The concern map is `studies/concern-map/` at `f93737ef` (its last change).
- **The parts:** `studies/class-model/parts/B-anchor/`, `B-woocommerce/`, `B-backfill-woocommerce/`: `cells.tsv`, `evidence.tsv`, `landings.tsv`, `capabilities.tsv`; their `reading`, `why` and `notes.md` only after my own placement of each cell was written in the coverage table.
- **Scripts, on a scratchpad copy** (`CLASS_MODEL_DIR=<scratchpad>/class-model-copy`), so the repository is unchanged: `check_class_part.py` on `B-anchor`, `B-woocommerce`, `B-backfill-woocommerce` in that order (0 problems; 7, 7 and 6 flags); `class_kinds.py --domain B --out -` (class 27, slot 1); `class_slice.py model --domain B` and `uncited --domain B`. Each copied `derived.tsv` and `derived-qualities.tsv` is identical to the part's own (`diff`: no difference, 6 files).
- **Beyond the statements, for C2 only:** the concern map's `inventory.tsv` and `citations.tsv` for Shopify, Salla and WooCommerce, through a script that prints only the inventory entries whose citation no statement carries; and, in observed-sh at `b46731d0`, the cited lines of `structures/shopify/admin-assignable-permissions/ctcbwa-r1/items.jsonl` (49, 121), `structures/shopify/collaborator-access-permissions/org-239421532@request-access/items.jsonl` (41, 43) and `structures/shopify/app-store-taxonomy/apps.shopify.com_categories/pages.jsonl` (41, 43, 86), with `git show`.
- **Every judgement below is a Reading** unless it quotes a statement's words or gives a count from a script I ran. Counts of hits are from `class_slice.py search` (substring, case, diacritics, hamza seats and tatweel ignored, ة as ه, ى as ي), one search per term; the coverage table gives each term with its count.

## Summary

| # | Finding | Verdict |
|---|---|---|
| C1 | The anchor reads Shopify's and Salla's own APIs (API folders, objects, scopes, webhook topics) as `shows`; the brief's test makes "its own API for its own feature" `core`. 55 evidence rows; three cells change placement (CM-CAT-004/shopify and CM-CAT-006/shopify from `not-stated` to `core`, CM-SEL-006/shopify gains `core`), and three counts rise: CM-CAT-004 1→2, CM-CAT-006 2→3, CM-SEL-006 1→2. | must fix |
| C2 | Inventory entries that Q1 placed in domain-B concerns, with citations, but never wrote as statements, are invisible to `search`, `outscope` and the checker; four show capabilities on `none-held` cells: Shopify's own permissions to view and edit product cost (CM-CAT-012/shopify, count 1→2), and the App Store's Pre-order apps and Event booking apps (CM-SEL-005/shopify, CM-SEL-004/shopify, `extension-point`). | must fix (in Q1's statements, then the cells) |
| C3 | CM-INV-003/salla is `none-held`, but Salla's plan line جرد المنتجات والمخزون (stocktake of products and inventory) and its dashboard link Inventory audit name a stocktake in Salla's own words; the anchor reads Shopify's inventory counts by their names and Salla's by a description. Count 1→2. | must fix (Reading) |
| C4 | CM-SEL-003/shopify (NFTs) is `core` on an admin route named `nft-application`, gated by the apps permission `APPLICATIONS`, whose maker isn't stated. Read as an application's place, the count falls 1→0 and the kind changes. | optional (convention) |
| C5 | The maker of WooCommerce's extensions ("Developed by Woo") is held only in statements' notes, as second citations, so no cell can read it; with a statement tying it to WooCommerce's company, CM-SEL-006/woocommerce could be `own-service`. | optional (gap for Q1) |
| C6 | CM-SEL-001/salla's `core` rests only on two feature flags that are not released; the statement that the merchant can enable recurring payments (SA-S-0195) is read `extension-point`. | optional (convention) |
| C7 | Statements that bear on a cell and aren't cited, none changing a placement: Salla's staff permission for size guides (the cell cites the partner one), Shopify's variant bulk-edit route, Salla's restriction-product-type flag, and in other domains Shopify's fulfillment-service apps (warehousing, print on demand) and Salla's storefront size-guide component. | optional |

**Must fix, in one line each:**
- **C1:** set `supports` to `core` on 49 anchor rows and to `extension-point` on 6 (CM-SEL-001's API rows), and re-place CM-CAT-004/shopify, CM-CAT-006/shopify and CM-SEL-006/shopify (`B-anchor/cells.tsv` lines 8, 12, 34).
- **C2:** have Q1 write statements for SH-I-0902, SH-I-0904, SH-I-1057, SH-I-1129, SH-I-1842 and SH-I-1887, then rewrite CM-CAT-012/shopify (`B-backfill-woocommerce/cells.tsv` line 2), CM-SEL-005/shopify and CM-SEL-004/shopify (`B-anchor/cells.tsv` lines 32, 30); make `search` and the checker read inventory entries without a statement.
- **C3:** make CM-INV-003/salla (`B-anchor/cells.tsv` line 43) `statements`, citing SA-C-025/decides/SA-S-2096 and SA-C-025/where/SA-S-1803 as `core`.

## Per check: rows checked, failed, share

| Check | Rows checked | Failed (must fix) | Share | Optional findings on the same rows |
|---|---|---|---|---|
| 1. Every placement against all of the concern map's statements | 56 cells held by `statements` (84 cells less 28 `none-held`) | 3 (C1: CM-CAT-004/shopify, CM-CAT-006/shopify, CM-SEL-006/shopify) | 5.4% | C4 (1 cell), C6 (1 cell), C7 |
| 2. Each `supports` value against the brief's tests | 297 evidence rows (220 anchor, 77 WooCommerce, 0 back-fill) | 55 (C1, all in `B-anchor/evidence.tsv`) | 18.5% (25.0% of the anchor's 220) | none |
| 5. Each `none-held` cell | 28 cells | 4 (C2: CM-CAT-012/shopify, CM-SEL-004/shopify, CM-SEL-005/shopify; C3: CM-INV-003/salla) | 14.3% | none |
| Checker flags | 20 (7, 7, 6) | 1 resolved against the part (C3) | 5% | 2 left to the other reviewer (checks 3 and 13) |

- **Check 2's own tests, row by row:** no row is `own-service` or `outside`. No cited statement names Shopify's, Salla's or WooCommerce's company as the maker of a separate product, so no row should be `own-service` (C5 is the one lead, held only in notes). Every statement that makes the merchant or the buyer responsible is `shows`: SH-C-020/responsible/SH-S-0236, SH-C-185/responsible/SH-S-0058, SH-C-186/responsible/SH-S-0762, SA-C-124/responsible/SA-S-5054 (which also disclaims Salla's part between the merchant and the partner). The other 18 `shows` rows hold: platform rights (SH-S-0031), conditions (SH-S-0593), reasons (SA-S-5011, SA-S-5012), Salla's app-type flags whose maker isn't stated (SA-S-3461, SA-S-3475, SA-S-3476, SA-S-3468), the APPLICATIONS permission (SH-S-5095), the statements of WooCommerce extensions scoped to the extension (WC-S-5350, WC-S-5351, WC-S-5469, WC-S-5352, WC-S-5353, WC-S-5470, WC-S-5474) and WooCommerce's privacy exporter and eraser (WC-S-0359, WC-S-0363).
- **Check 1's two bullets:**
  - *App-store, marketplace or extension-category `where` statements*, read against their concerns' `decides` statements: CM-CAT-002/shopify and /woocommerce, CM-CAT-007/woocommerce, CM-CAT-010 on all three, CM-SEL-001 on all three, CM-SEL-002/shopify, CM-SEL-004/woocommerce, CM-SEL-006/shopify and /woocommerce, CM-SEL-007/shopify, CM-SEL-008/woocommerce. Where a `decides` statement shows the platform doing it (Shopify's plan line for variants SH-C-020/decides/SH-S-7214; Shopify Collective's plan row SH-C-141/decides/SH-S-7013; Salla's wholesale-market plan line SA-C-098/decides/SA-S-2069; Shopify's admin routes SH-C-186/decides/SH-S-5019 and SH-S-5144), the cell holds `core` beside `extension-point`; elsewhere no `decides` statement does, and `extension-point` alone holds. WooCommerce's extension settings and hooks are scoped to the extension (WC-C-100/where/WC-S-5350, WC-C-101/decides/WC-S-5352) and are not read as core, as the brief's example says.
  - *A `core` resting only on API objects, scopes or webhook topics:* one cell, CM-INV-004/woocommerce (flagged). The words that decide it: `'Automattic\WooCommerce\Admin\API\ProductsLowInStock'`, a class of WooCommerce Admin's own API, with no statement saying apps or partners use it: `core` holds (the fit of "products low in stock" to alerts is a matter for check 10, below). Under C1, the anchor's API rows meet the same test; the subscription APIs are the ones whose statements say apps do the work (SH-C-186/where/SH-S-0763 "Subscription apps enable developers and merchants to build subscription experiences"; SA-C-125/decides/SA-S-0195 "Only merchants or authorized third-party apps can enable this feature"), so their rows are `extension-point`, not `core`.

## Depth: which cells were searched beyond their concerns

- **Searched in full:** every cell under check 1's two bullets (12 cells: the 11 with an `extension-point` row and CM-INV-004/woocommerce); every cell of a capability counted 0 or 1 (14 capabilities; 19 cells held by `statements`); every `none-held` cell (28). That is 59 cells.
- **The sample of the other 25 cells** (held by `statements`, capability counted 2 or 3, under neither bullet): 10 cells, at least a third, with at least two per platform (Shopify 2, Salla 5, WooCommerce 3) and per `supports` value (`core` 10, `shows` 6), drawn with seed 20261030 by this command, run from the repository root with the class kinds' output (`CLASS_MODEL_DIR=<copy> python3 -I method/class_kinds.py --domain B --out - > kinds.txt`):

```
python3 -I sample.py kinds.txt
```

```python
import sys, os, random
P = "studies/class-model/parts"
count = {}
for ln in open(sys.argv[1], encoding="utf-8"):
    c = ln.rstrip("\n").split("\t")
    if c[0].startswith("CM-"):
        count[c[0]] = int(c[5])
cells, ev = [], {}
for part in ("B-anchor", "B-woocommerce", "B-backfill-woocommerce"):
    for fn in ("cells.tsv", "evidence.tsv"):
        lines = open(os.path.join(P, part, fn), encoding="utf-8").read().split("\n")
        hdr = lines[0].split("\t")
        for i, ln in enumerate(lines[1:], start=2):
            if not ln.strip():
                continue
            r = dict(zip(hdr, ln.split("\t")))
            if fn == "cells.tsv":
                cells.append((part, i, r["cap_id"], r["platform"], r["held"]))
            else:
                ev.setdefault((r["cap_id"], r["platform"]), []).append((r["supports"], r["key"].split("/")[1]))
sup = lambda c: sorted({s for s, _ in ev.get((c[2], c[3]), [])})
def core_only_boundary(c):
    cores = [pl for s, pl in ev.get((c[2], c[3]), []) if s == "core"]
    return bool(cores) and all(pl == "boundary" for pl in cores)
other = [c for c in cells if c[4] != "none-held" and count[c[2]] > 1
         and "extension-point" not in sup(c) and not core_only_boundary(c)]
order = other[:]
random.Random(20261030).shuffle(order)
def ok(s):
    if any(sum(1 for c in s if c[3] == p) < 2 for p in ("shopify", "salla", "woocommerce")):
        return False
    return all(sum(1 for c in s if v in sup(c)) >= 2 for v in {v for c in other for v in sup(c)})
k = -(-len(other) // 3)
while not ok(order[:k]) and k < len(order):
    k += 1
for c in order[:k]:
    print(c[0], c[1], f"{c[2]}/{c[3]}", ";".join(sup(c)))
```

  Its output: CM-INV-001/salla, CM-CAT-003/woocommerce, CM-INV-004/salla, CM-INV-002/salla, CM-SEL-002/woocommerce, CM-INV-006/salla, CM-CAT-001/shopify, CM-CAT-001/woocommerce, CM-CAT-007/salla, CM-INV-001/shopify. Every sampled cell holds. I also searched one unsampled cell, CM-CAT-006/shopify, since C1 turns on it.
- **Read once, under all five placements:** the domain's 30 concerns (Shopify 11, Salla 11, WooCommerce 8) and every other domain's concern a cell cites (SH-C-028, SH-C-141, SH-C-187, SA-C-098, SA-C-124, WC-C-061, WC-C-107); the platform's other statements only through `search`.

## Findings

### C1. The anchor reads its platforms' own APIs as `shows`; the brief makes them `core` (must fix)

- **Rows:** 55 rows of `B-anchor/evidence.tsv`, each in the coverage table with result `C1` and my value in `mine`:
  - to `core` (49): CM-CAT-001/shopify lines 9, 10, 11; CM-CAT-001/salla 23, 24, 25; CM-CAT-002/salla 33–37; CM-CAT-003/shopify 42–45; CM-CAT-003/salla 50–53; CM-CAT-004/shopify 54; CM-CAT-005/salla 61–64; CM-CAT-006/shopify 65; CM-CAT-006/salla 68, 69; CM-CAT-007/shopify 71; CM-CAT-007/salla 78, 79; CM-CAT-008/shopify 81; CM-INV-001/shopify 152–154; CM-INV-001/salla 166, 167; CM-INV-004/salla 179; CM-INV-005/shopify 184; CM-INV-005/salla 196–198; CM-INV-006/shopify 205–207; CM-INV-007/shopify 220, 221; CM-SEL-002/salla 121; CM-SEL-004/salla 129; CM-SEL-006/shopify 136;
  - to `extension-point` (6), the APIs whose statements say apps do the work: CM-SEL-001/shopify lines 105, 106; CM-SEL-001/salla 110–113.
- **Problem:** the brief's test (`B-extent.md`, Cells and evidence) makes `core` "its own API for its own feature", and `extension-point` "an API whose statements say apps or partners use it to do the work". The anchor's notes (line 191) read "API folders, objects, scopes and webhook topics are `shows`, so no `core` rests on boundary statements alone"; the WooCommerce part reads WooCommerce's own as `core` (`B-woocommerce/notes.md` line 178). `method-report.md` (lines 39 and 46) names the two methods and leaves the choice to this review. The brief's words decide it: `core`. `shows` is right only where the statement gives a term and supports no placement, and an API scope or topic of the platform's own feature does support one. Three cells change:
  - **CM-CAT-004/shopify** (`B-anchor/cells.tsv` line 8): SH-C-028/boundary/SH-S-6240 gives "`write_metaobjects` for taxonomy linking". The words name an access scope of Shopify's own Admin API for a feature of Shopify's products, and don't say apps or partners do the linking. **Reading:** `core`. The cell goes from `not-stated` to `core`; CM-CAT-004's count goes from 1 to 2.
  - **CM-CAT-006/shopify** (line 12): SH-C-020/boundary/SH-S-6160 "Requires `unauthenticated_read_product_tags` access scope", from the Storefront API's productTags query (its note). **Reading:** Shopify's own Storefront API for its own product tags: `core`. The cell goes from `not-stated` to `core`; CM-CAT-006's count goes from 2 to 3.
  - **CM-SEL-006/shopify** (line 34): SH-C-188/boundary/SH-S-1100 "unauthenticated_read_bundles", a Storefront API scope for Shopify's bundles; no statement says apps use that API to make bundles (the App Store category SH-S-2604 and the extension target SH-S-2207 stay `extension-point`). **Reading:** `core`. The cell goes from `extension-point` to `core;extension-point`; CM-SEL-006's count goes from 1 to 2.
  - No kind changes: all three capabilities are `class` already.
- **Also:** the anchor applies its own method unevenly. It reads Salla's partner-requestable permissions as `core` (SA-C-020/decides/SA-S-2471, SA-S-2612; SA-C-022/decides/SA-S-2472; SA-C-023/decides/SA-S-2476, SA-S-2477; their notes say "Permission a partner can request on a merchant's store"), while it reads Salla's app scopes as `shows` (SA-C-020/boundary/SA-S-1552). Both belong to Salla's own permission system; under the brief's test both are `core`, and the fix makes them agree.
- **Fix:** in `B-anchor/evidence.tsv`, set `supports` on the 55 rows as listed, with a `why` that names the API; in `B-anchor/cells.tsv` lines 8, 12 and 34, rewrite the `reading` to place the cell on the platform's own API and quote the words; note the change in `B-anchor/notes.md`. In the brief, state the rule once for every part (see Conventions, 1).

### C2. Placed inventory entries without a statement show capabilities on `none-held` cells (must fix, in Q1's statements)

- **Rows:** `B-backfill-woocommerce/cells.tsv` line 2 (CM-CAT-012/shopify); `B-anchor/cells.tsv` line 30 (CM-SEL-004/shopify) and line 32 (CM-SEL-005/shopify). The same gap touches CM-SEL-002/shopify and CM-SEL-003/shopify, without changing their placement.
- **Problem:** Q1's inventory places entries in domain-B concerns, each with a citation, but no statement carries their citation. `class_slice.py search` reads statements only and `outscope` reads only unplaced entries, so neither finds them, and neither does the checker's `none-held` test. Of the inventory entries placed in a domain-B concern, 208 have no statement carrying their citation (a script over `inventory.tsv` and `statements.tsv`: Shopify 201, Salla 4, WooCommerce 3); most repeat what a statement made from another citation holds (the webhook topics and access scopes, for example). Searching them with each `none-held` cell's own terms finds these:
  - **CM-CAT-012/shopify (product cost):** SH-I-0902 "Products > View cost" and SH-I-0904 "Products > Edit cost" (cite SH-S-1666, SH-S-1668: `observed-sh@b46731d0:structures/shopify/collaborator-access-permissions/org-239421532@request-access/items.jsonl` lines 41 and 43, which I read: `"label": "View cost", "value": "products_view_product_costs"` and `"label": "Edit cost", "value": "products_edit_product_cost"`, in the section `products`); SH-I-1057 EDIT_PRODUCT_COST and SH-I-1129 VIEW_PRODUCT_COSTS (cite SH-S-1821, SH-S-1893: `observed-sh@b46731d0:structures/shopify/admin-assignable-permissions/ctcbwa-r1/items.jsonl` lines 49 and 121, which I read: `{"value": "EDIT_PRODUCT_COST", ...}`, `{"value": "VIEW_PRODUCT_COSTS", ...}`). All four are placed in SH-C-010;SH-C-020. Shopify's own staff permissions for a product's cost are `core`; the cell would be `statements: core`, and CM-CAT-012's count would go from 1 to 2. The anchor's and the back-fill's notes record the gap (`B-anchor/notes.md` lines 218–219, 225; `B-backfill-woocommerce/notes.md` lines 15–16, 33).
  - **CM-SEL-005/shopify (pre-orders):** SH-I-1842 "Pre-order apps" (cite SH-S-2606, `observed-sh@b46731d0:structures/shopify/app-store-taxonomy/apps.shopify.com_categories/pages.jsonl` line 41, which I read: the App Store category at `.../marketing-and-conversion-upsell-and-bundles-pre-orders`), placed in SH-C-188, whose own name is "Upsell, cross-sell, bundles and pre-orders". The cell would be `statements: extension-point`; the count stays 1.
  - **CM-SEL-004/shopify (bookings):** SH-I-1887 "Event booking apps" (cite SH-S-2651, the same file, line 86: `.../selling-products-digital-goods-and-services-event-booking`), placed in SH-C-190. The cell would be `statements: extension-point`; the count stays 1.
  - Not this capability, by its own page: SH-I-1844 "Stock alert apps" (line 43 of the same file, its intro: "Sometimes things sell out fast. Notify customers when their favorite products are back and ready to buy."), customers' back-in-stock alerts, so CM-INV-004/shopify stays `none-held`.
- **Fix:** the coordinator has Q1 write statements for SH-I-0902, SH-I-0904, SH-I-1057, SH-I-1129 (under SH-C-020, `decides`), SH-I-1842 (SH-C-188, `where`) and SH-I-1887, SH-I-1886, SH-I-1888 (SH-C-190, `where`), or the brief lets a cell cite a placed inventory entry by its id; then `B-backfill-woocommerce` rewrites CM-CAT-012/shopify and the anchor rewrites CM-SEL-004/shopify and CM-SEL-005/shopify. `class_slice.py search` and the checker's `none-held` test should also read inventory entries that no statement carries (Tests, 2).

### C3. Salla's stocktake is read away from CM-INV-003 (must fix, Reading)

- **Rows:** `B-anchor/cells.tsv` line 43 (CM-INV-003/salla, `none-held`), flagged by the checker; the anchor's notes lines 84–87, 142–145, 244–245.
- **Problem:** the cell's own searched terms find SA-C-025/decides/SA-S-2096, the Salla Plus plan line "جرد المنتجات والمخزون" (the stocktake of products and inventory), and SA-C-025/where/SA-S-1803, the dashboard link "Inventory audit" (`/products/quantities`). The anchor reads both as CM-INV-001's inventory view, because the plan line's description is "تتبّع حالة المخزون وعدد المنتجات المباعة والمتبقية والتي قاربت على الانتهاء" (tracking stock status and the numbers of products sold, remaining and nearly out), "not as counting stock against the records". But no Shopify statement says counting against the records either: Shopify's cell rests on names, "View inventory counts", "Manage inventory counts", "Perform inventory counts" (SH-C-022/decides/SH-S-7158, SH-S-7159, SH-S-7160) and the routes `products:inventory:counts`. **Reading:** جرد and "Inventory audit" are Salla's own words for a stocktake, and the description, the numbers sold and remaining, is what a stocktake reconciles; read by the same standard as Shopify's, they show the capability, and a `none-held` cell is false when a statement shows it. CM-INV-003's count goes from 1 to 2. The anchor's reading is the alternative, and the anchor asked the reviewer to judge it.
- **Fix:** in `B-anchor/cells.tsv` line 43, `held` `statements`, terms جرد المنتجات والمخزون;Inventory audit, a `reading` that says why; in `B-anchor/evidence.tsv`, rows for CM-INV-003/salla citing SA-C-025/decides/SA-S-2096 (`core`: plan line, Salla Plus) and SA-C-025/where/SA-S-1803 (`core`: dashboard link); both stay cited in CM-INV-001 as well. If the coordinator holds the description over the name, the convention should say so for both platforms (Conventions, 3).

### C4. Shopify's NFT route serves an application (optional, convention)

- **Rows:** `B-anchor/cells.tsv` line 28; `B-anchor/evidence.tsv` lines 122–124 (CM-SEL-003/shopify).
- **Problem:** the cell is `core` on SH-C-190/where/SH-S-5094 (`"path":"nft-application"`, section Blockchain) and SH-C-190/where/SH-S-1550 (`"section":"Blockchain"`), with SH-C-190/decides/SH-S-5095 (`"eligibility":{"permissions":["APPLICATIONS"]}`) as `shows`. The route's identifier names an application, and the permission is the one Shopify's admin uses for apps: `search` for `"APPLICATIONS"` finds 10 statements of routes, among them `apps:list`, `apps:extension_details`, `apps:development_list` and `shopify-fulfillment-network`. The brief's test makes an admin route `core`, and also says "a route or setting that an extension or app adds, as its identifier or scope shows, is the extension's". **Reading:** the statements don't say who fills the route, so `core` holds on the brief's first test, borderline. Read as an app's page, the cell becomes `extension-point` and CM-SEL-003's count falls from 1 to 0, with the kind `slot` (no platform places it in core; Shopify places it with third parties). The App Store category "NFT and tokengating apps" is an inventory entry without a statement (SH-I-1888, C2).
- **Fix:** the brief settles whether a route gated only by an apps permission, with an identifier naming an application, is the platform's or the app's (Conventions, 4); the anchor re-reads the cell by it.

### C5. The maker of WooCommerce's extensions is held only in notes (optional, gap for Q1)

- **Rows:** `B-woocommerce/evidence.tsv` line 69 (WC-C-104/boundary/WC-S-5474, Product Bundles, CM-SEL-006/woocommerce); the same pattern on WC-C-103, WC-C-105, WC-C-106, WC-C-107, WC-C-109 and WC-C-110 in other domains.
- **Problem:** the statement's citations include the Marketplace page's categories list (WC-S-5475), and its note says "Product Bundles is listed in the categories 'Merchandising', 'Bundles' and 'Developed by Woo' (second citation ...)". The words "Developed by Woo" are in the note only, so no cell can cite them, and no statement ties "Woo" to WooCommerce's company (WC-C-023/responsible/WC-S-0461 names "Automattic Inc., Aut O'Mattic A8C Ireland Ltd., WooCommerce, Inc., and WooCommerce Ireland Ltd."). The part is right to leave it `shows` with a gap. If Q1 held both as statements, CM-SEL-006/woocommerce would be `own-service`, and its count would rise again (1→2, or 2→3 with C1). WooCommerce Subscriptions, Bookings and Memberships hold no such listing.
- **Fix:** Q1 writes each "Developed by Woo" listing as its own statement (`where` or `responsible`), with a statement naming the company that "Woo" stands for, if a source states it; the WooCommerce part then re-reads the cell.

### C6. Salla's recurring payments: `core` rests only on flags not released (optional, convention)

- **Rows:** `B-anchor/cells.tsv` line 25; `B-anchor/evidence.tsv` lines 107–109 (CM-SEL-001/salla).
- **Problem:** both `core` rows are feature flags with `"released": false` (SA-C-125/decides/SA-S-3301 `recurring-payment`, SA-S-3302 `recurring-apple-pay`). A script over every cell's `core` rows finds this is the only cell whose every `core` row is a flag not released. SA-C-125/decides/SA-S-0195, "By default, Recurring Payments are **disabled** for all stores. Only merchants or authorized third-party apps can enable this feature.", is read `extension-point`; its first half shows the merchant enabling Salla's own feature, a `core` reading. If unreleased flags don't count, CM-SEL-001's count falls from 2 to 1 unless SA-S-0195 is read `core`.
- **Fix:** the brief says whether a flag that is not released supports `core` (Conventions, 6); if it doesn't, the anchor re-reads SA-S-0195, whose one row can carry one value.

### C7. Statements that bear on cells and aren't cited (optional; overlaps check 8)

None changes a placement; each would make the cell's evidence complete:
- CM-CAT-011/salla cites the partner-requestable permission SA-C-020/decides/SA-S-2612 as its only `core`; the staff permission SA-C-020/decides/SA-S-2395 (`size_guides_management`, its note "Staff permission, group إعدادات المتجر") shows Salla's own dashboard holding size guides, and the feature itself is of type app (SA-S-3461). Outside domain B, Salla's storefront component `salla-product-size-guide` (SA-C-091/boundary/SA-S-1502, domain E, no `also` B).
- CM-CAT-002/shopify: SH-C-022/where/SH-S-5177, the admin route `bulk/product_variant`.
- CM-CAT-009/salla: SA-C-020/decides/SA-S-3351, the feature `restriction-product-type` (enabled, not released).
- CM-CAT-010/shopify and CM-INV-005/shopify: SH-C-119/where/SH-S-0702, "Fulfillment service apps provide third-party warehousing, print on demand, or fulfillment services" (domain C), a further `extension-point` for both.

## The checker's flags

| Part, file, line | Flag | Resolution |
|---|---|---|
| B-anchor evidence.tsv 141 | SH-C-187 (domain D, no `also` B) cited | left to the other reviewer (check 13); the placement `extension-point` holds on its words |
| B-anchor cells.tsv 10 | CM-CAT-005/shopify none-held, 9 matches | holds: checkout branding and a Bill Pay vendor |
| B-anchor cells.tsv 18 | CM-CAT-009/shopify, 3 matches | holds (Reading): the Add-to-cart limit is one store-wide cart setting (SH-C-046, domain C), and Salla's statements don't define a product restriction |
| B-anchor cells.tsv 30 | CM-SEL-004/shopify, 1 match | holds on statements: SH-S-0583 is a payment example; the App Store category is C2 |
| B-anchor cells.tsv 43 | CM-INV-003/salla, 2 matches | **C3** |
| B-anchor cells.tsv 51 | CM-INV-007/salla, 13 matches | holds (Reading): all the wholesale market's vendors (CM-CAT-010) |
| B-anchor capabilities | CM-SEL-007 has no concern in its tree | left to the other reviewer (check 3) |
| B-woocommerce cells.tsv 5 | CM-CAT-004/woocommerce, 1 match | holds: WordPress taxonomies, the mechanism of categories and tags |
| B-woocommerce cells.tsv 10 | CM-CAT-009/woocommerce, 7 matches | holds: WooPayments' account and business restrictions, a readme, a function name |
| B-woocommerce cells.tsv 16 | CM-SEL-003/woocommerce, 1 match | holds: Crypto payments is a way to pay |
| B-woocommerce cells.tsv 25 | CM-INV-004/woocommerce, core only on boundary | holds: WooCommerce Admin's own API, no statement of apps using it |
| B-woocommerce cells.tsv 26 | CM-INV-005/woocommerce, 20 matches | holds: customers', selling, shipping and tax locations |
| B-woocommerce cells.tsv 27 | CM-INV-006/woocommerce, 9 matches | holds: bank, payout and data transfers |
| B-woocommerce cells.tsv 28 | CM-INV-007/woocommerce, 2 matches | holds: the Purchase Order Gateway is a buyer's way to pay (WC-C-103, domain D) |
| B-backfill-woocommerce cells.tsv 2 | CM-CAT-012/shopify, 9 matches | holds on statements (service fees and costs); the product-cost permissions are C2 |
| B-backfill-woocommerce cells.tsv 3 | CM-CAT-012/salla, 18 matches | holds (Reading): shipping costs, fees, partner earnings; profit analytics (SA-S-2044) names no product cost |
| B-backfill-woocommerce cells.tsv 4 | CM-SEL-008/shopify, 52 matches | holds: staff members, loyalty apps, B2B |
| B-backfill-woocommerce cells.tsv 5 | CM-SEL-008/salla, 48 matches | holds: staff members and loyalty points |
| B-backfill-woocommerce cells.tsv 6 | CM-INV-008/shopify, 30 matches | holds: payment reserves, abandoned checkouts, unpaid manual payments |
| B-backfill-woocommerce cells.tsv 7 | CM-INV-008/salla, 92 matches | holds (Reading): restock by order status (SA-S-1742, SA-S-3289) says nothing of holding stock for an unpaid order |

## Problems noted for the other reviewer's checks (not pursued)

- **Check 13, stale readings:** CM-CAT-007/woocommerce and CM-CAT-010/woocommerce (`B-woocommerce/cells.tsv` lines 8 and 11) say WC-C-107 and WC-C-061 are cited "without naming B" and are flagged; `scope.tsv` now names B under `also` for both (commit `69bce534`), and the checker no longer flags them.
- **Check 10 or 4, a fit on a name:** CM-INV-004/woocommerce rests on an API for "products low in stock" (WC-C-068/boundary/WC-S-0219); its own reading says the fit to alerts rests on the API's name, and no low-stock notification is held.
- **Check 13, context carried into a placement:** CM-INV-005/salla reads SA-C-026/decides/SA-S-2190 (إدارة مخزون متقدمة, Special) "with its page's text, as context". The statement is SA-C-026's, so the cell holds, but the placement of that row rests on what the statement doesn't say.
- **Check 11, scopes:** several `core` placements hold under one scope only: a beta (CM-INV-002/shopify, CM-INV-003/shopify), one plan (CM-CAT-008/shopify, Plus), plans Pro and Special (CM-CAT-009/salla, CM-SEL-005/salla).

## Conventions the brief should settle on placements

1. **A platform's own API** (folder, object, scope, webhook topic, an API mutation's requirement) is `core` for the feature it serves, unless the statements about that API say apps or partners use it to do the capability's work for the merchant; then it is `extension-point`. An API guide written to app developers ("Your app has the ... scope") is still the platform's own API. A scope or topic takes its API's reading. (C1)
2. **Inventory entries:** either Q1 writes a statement for every placed entry with a citation, or a cell may cite a placed inventory entry by its id; either way, a `none-held` cell's search covers them. (C2)
3. **Names and descriptions:** when a statement's own words name the capability and its description says more or less, say which governs, and apply it to every platform of a join alike. (C3)
4. **Routes that host apps:** an admin route whose identifier names an application and whose only gate is the apps permission is the app's place (`extension-point`) or the platform's (`core`); decide one. (C4)
5. **The maker:** a marketplace's "developed by" listing is maker evidence only as a statement, and only with a statement naming the company it stands for; Q1 writes such listings as statements, not notes. (C5)
6. **Feature flags:** whether a flag with `"released": false` supports `core`; that a flag of `"type": "app"` with an install link and no maker is `shows`, with the maker as a gap (the anchor's practice, applied to SA-S-3461, SA-S-3468, SA-S-3475, SA-S-3476). (C6)
7. **Which permission to cite:** where a platform lists a permission both for staff and for partners (Salla), cite the staff permission for `core`; the partner one is an app scope and falls under 1. (C7)
8. **A capability its own platform names but never defines** (CM-CAT-009 product restrictions, CM-SEL-008 memberships): the other platforms' cells are `none-held` "on the terms searched", and their readings say the capability's definition isn't stated, so a reviewer doesn't read a join on role into a near term (the Add-to-cart limit) or out of one.

## Tests the checker should add

1. **`shows` on the platform's own API:** for every evidence row with `supports` `shows` whose statement is a `boundary` statement, or a `where` statement whose identifier is an API folder, scope or webhook topic, print it; where the cell has no other `core`, `own-service` or `extension-point` row, print that the cell's placement rests on it.
2. **`none-held` against the inventory:** for every `none-held` cell, search the platform's inventory entries whose citation no statement carries, placed or not, with the cell's searched terms and the other platforms' terms, and print each hit with its concerns.
3. **A match cited elsewhere in the tree:** when a `none-held` cell's search matches a statement that the part cites in the capability's parent, child or sibling, print where it is cited (CM-INV-003/salla and CM-INV-001).
4. **Flags not released:** print every cell whose `core` rows are all feature flags whose statement holds `"released": false`.
5. **App-type flags and app-gated routes:** print every `core` row whose statement holds `"type": "app"`, and every `core` row resting only on routes whose eligibility names only an apps permission (`APPLICATIONS`), for the reviewer.
6. **Maker held in a note:** print every cited statement whose note names a "Developed by" listing or a second citation of a maker, so the cell's `own-service` gap is recorded.
