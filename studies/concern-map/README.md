# Concern map (Q1), in progress

The answer to `questions/Q1-concern-map.md` as it is being built. This file says where each part stands and what comes next.

## Where it stands (11 October 2026)

| Platform | Inventory and concerns | Quotes checked against their sources |
| --- | --- | --- |
| WooCommerce | 654 entries, 118 concerns | 963 of 963 found |
| Salla | 2,620 entries, 148 concerns | 2,828 of 2,828 found |
| Shopify | 2,610 entries, 198 concerns. The re-pass is done: 3,005 statements and 249 gaps, with 741 of 990 cells stated | 5,055 of 5,055 found |

**What stands:**
- the inventories, built from the platforms' own lists;
- the concern names, in the platforms' own words;
- the citations and their checked quotes.

**What is not carried forward: the placement labels.** These are "where it lives in the software", "who decides" and "legally responsible". `measurements-2026-10-11.md` shows the problem:
- they are our vocabulary for 95% of values;
- many rest only on a list entry existing;
- the three runs encoded one question three different ways.

**Shopify's own sources were barely used.** The platforms state these things in their own structures. Shopify's admin router states, route by route, the staff permissions and plan entitlements each page requires, and the Q1 Shopify placements barely used it. The files stay here as a record of what was tried.

**Withdrawn:**
- Salla's split pass;
- the Shopify run's one-party split step;
- the proposal to restructure "who decides" into a chain.

None of them changed any file.

## Next, in order

1. **Capture Shopify's cited pages and check its quotes.** Done: all 152 pages are captured, and all 3,192 quotes are found.
2. **The founder decides how Q1's placement step is reshaped.** The proposal: each concern's placement is recorded as what the platform states in its own structures, with no fixed value lists. Examples are a route's stated permissions and entitlements, each store's values for them, a plan line, an access line, or a clause in the terms, each quoted with its identifiers.
3. **Shopify re-pass, against observed-sh at `e49840729`.** Done. `gaps-to-close.md` lists the gaps that someone can close.
   - First, joins by script on Shopify's own identifiers:
     - concern to router sections and routes, then to stated eligibility, then to store values;
     - concern to API resources, then to access lines;
     - concern to help pages, through `help-admin-links`.
   - Then the agent reads the text sources (terms, help) for responsibility and stated reasons, quoting them word for word.
4. **Salla and WooCommerce re-passes, with the same step against their own structures.**
   - **Salla:** the dashboard feature registry with its plan lists, staff permission groups, app scopes and settings.
   - **WooCommerce:** the 11.2.1 release's capabilities, settings, hooks and extension APIs.
5. **The matching pass across the three platforms.** It matches only on the platforms' own terms. Unclear matches go to the founder.

**Separate from these steps:**
- **The Salla pages for the founder** (`evidence/product-class/to-save-from-browser.md`) can be saved at any time.
- **The Shopify answers for stores registered in Yemen** are noted for Q2.

## Layout

| Path | What it holds |
| --- | --- |
| `platforms/<platform>/` | Each run's six files, notes, scripts and fetch log. Shopify's folder also holds its working files (`work/`) and its working copies of pages (`working-copies/`). Working copies are not evidence. Shopify's cited pages are now captured, so these copies can go once the founder agrees. |
| `checks/` | The checker's output per platform, Shopify's list of pages to capture, and `salla-multi-party.tsv`. |
| `measurements-2026-10-11.md` | The measurements behind the reshaping. |

The captured web pages are in `evidence/product-class/runs/`, one run per platform.

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
