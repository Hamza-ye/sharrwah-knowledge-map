# Concern map (Q1), in progress

The answer to `questions/Q1-concern-map.md` as it is being built. This file says where each part stands and what comes next.

**Since 12 October 2026 the map is the index for `PLAN.md`'s subjects, and it is frozen.** No new concerns, statements or gaps go in unless a subject needs them. Stage 0 checked every gap against what is held and re-routed 215 of them (`held-check.tsv`). `STATE.md` at the repository root says where the work is. The platforms' `notes.md` files are the Q1 runs' working notes: their next steps are as they stood then.

## Where it stands (11 October 2026)

**All three re-passes and the matching pass are done.** What remains is the founder's review.

| Platform | Inventory and concerns | Statements | Gaps | Cells with a statement | Quotes found |
| --- | --- | --- | --- | --- | --- |
| Shopify | 2,610 entries, 198 concerns | 3,005 | 249 | 741 of 990 | 5,055 of 5,055 |
| Salla | 2,627 entries, 152 concerns | 2,560 | 230 | 530 of 760 | 2,982 of 2,982 |
| WooCommerce | 654 entries, 118 concerns | 1,499 | 182 | 408 of 590 | 1,466 of 1,466 |
| BigCommerce (declaration level, no accounts) | 569 entries, 88 concerns | 473 | 161 | 286 of 440 | 481 of 481 |
| Zid (declaration level, no accounts) | 543 entries, 96 concerns | 654 | 156 | 346 of 480 | 1,087 of 1,087 |

**The question's three outputs:**
1. **The table of concerns, with their placements and citations.** Each platform's `statements.tsv` and `gaps.tsv` give these in the platform's own words. `map/side-by-side.md` sets the 88 matched concerns side by side.
2. **The concerns the platforms place differently.** `map/side-by-side.md` shows them for each placement, without categories, and leaves the differences for the reader. `map/stated-or-gap.tsv` marks, per match and placement, which platforms state it and which have a gap. `map/single-platform.tsv` lists the concerns found on one platform only.
3. **The inventory entries left out of scope, with reasons:** `map/out-of-scope.tsv`.

**Matching.** A separate agent saw only the three outputs (`matching-notes.md`, `matching-scripts/`). It found:
- 88 matches on the platforms' own terms (`matches.tsv`): 34 across all three platforms and 54 across two;
- 84 unclear candidates for the founder (`unclear-matches.tsv`).

**For the founder:**
- **Rule on the unclear matches.** 19 of them name the statement or source that would settle them, and 6 put a specific question.
- **Check two matches.** The matching agent flagged M-070 (Shopify Functions and Salla's App Functions) and M-064 (chat with customers and Salla Chat). Both rest on a shared main word.
- **Gaps.** `gaps-to-close.md` is now a reference, not a list of tasks. Under `PLAN.md`, a gap is closed only inside a subject that needs it.
- **Decide on incorporated agreements.** Should an agreement a platform's terms incorporate be read, such as Stripe's Connected Account Agreement under the WooPayments and Shopify Payments terms? 9 WooCommerce gaps wait on that.

**What was not carried forward:** the first runs' placement labels. `measurements-2026-10-11.md` gives the reasons, and each platform's `placements.tsv` keeps them as a record.

## Layout

| Path | What it holds |
| --- | --- |
| `platforms/<platform>/` | Each platform's files: `inventory.tsv`, `concerns.tsv`, `citations.tsv`, `statements.tsv`, `gaps.tsv`, `not-reached.tsv`, `review-log.tsv` and `notes.md`. It also holds `placements.tsv` (the first run's record), scripts and fetch logs. Shopify's folder also keeps the first run's working copies of pages. |
| `map/` | The combined map: `side-by-side.md`, `stated-or-gap.tsv`, `single-platform.tsv` and `out-of-scope.tsv`. |
| `matches.tsv`, `unclear-matches.tsv`, `matching-notes.md`, `matching-scripts/` | The matching pass. |
| `gaps-to-close.md` | The open gaps, who could close them, and how (a reference). |
| `held-check.tsv` | Stage 0's re-routing of gaps whose page or corpus is held, one row per change, with its rule. |
| `checks/` | The checker's output per platform. |
| `measurements-2026-10-11.md` | Why the placement step was reshaped. |

The captured web pages are in `evidence/product-class/runs/`.

## Checking a platform's output

`RUN` is a folder holding one folder per platform. The commands are:
```
python3 -I method/check_concern_map.py RUN OUT
CAPTURE_LANG='en,ar;q=0.8' CAPTURE_WORKERS=2 method/capture/run.sh OUT/urls-to-capture.json evidence/product-class/runs/<UTC time>-q1-<platform>-sources
python3 -I method/check_concern_map.py RUN OUT evidence/product-class/runs/<that run>
```

## If the container was reset

The checker reads local sources through these paths. Environment variables override them.

- **observed-sh:** clone https://github.com/Hamza-ye/observed-sh to `/home/user/observed-sh`, or set `OBSERVED_SH`. The Q1 citations are at `b46731d0`, and the re-pass uses `e49840729`.
- **observed-sa:** clone https://github.com/Hamza-ye/observed-sa to `/home/user/observed-sa`, or set `OBSERVED_SA`. Citations are at `145f137`.
- **WooCommerce 11.2.1:**
  - Download it from https://downloads.wordpress.org/plugin/woocommerce.11.2.1.zip.
  - Check its sha256 against `evidence/product-class/woocommerce-11.2.1/woocommerce.11.2.1.zip.sha256`.
  - Unzip it into `/home/user/woocommerce-release/11.2.1/`, or set `WOO_RELEASE`.
