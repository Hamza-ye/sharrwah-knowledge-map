# Concern map (Q1), in progress

The answer to `questions/Q1-concern-map.md` as it is being built. The work is paused, and this file says where each part stands and how to resume.

## Where it stands

**Paused** on 11 October 2026, at the founder's request, before the cross-platform matching pass. The founder was close to a usage limit, and work must not be cut off halfway through a step.

| Platform | State | Concerns | Quotes checked against their sources |
| --- | --- | --- | --- |
| WooCommerce | Complete and checked. | 118 | 963 of 963 found |
| Salla | Complete and checked. A split pass is paused before it began. | 148 | 2,828 of 2,828 found |
| Shopify | Paused mid-run. Its `notes.md` ends with "Where this run stopped". | see its files | its pages are not captured yet |

**Salla's split pass.** 100 of Salla's placements name two parties in one value, usually "merchant; operator per plan". Under the question's rule, a concern whose parts sit with different parties is split. WooCommerce has no such values. The rows are listed in `checks/salla-multi-party.tsv`, and Salla's `notes.md` says the pass hasn't changed any of them yet.

**Not started yet:**
- the capture of Shopify's cited pages and the check of its quotes;
- the matching pass across the three platforms;
- the combined map: the table of concerns, the concerns placed differently, and the entries left out of scope.

## Layout

| Path | What it holds |
| --- | --- |
| `platforms/<platform>/` | Each run's six files (`inventory.tsv`, `concerns.tsv`, `placements.tsv`, `citations.tsv`, `not-reached.tsv`, `notes.md`), its scripts and its fetch log. Shopify's folder also holds its working files (`work/`) and its working copies of pages (`working-copies/`). Working copies are not evidence. They are kept only until Shopify's cited pages are captured. |
| `checks/` | The checker's output per platform: `<platform>-issues.tsv` and `<platform>-quotes.tsv`. Also `salla-multi-party.tsv`. |

The captured web pages are in `evidence/product-class/runs/`, one run per platform.

## How to resume

1. **Shopify.** In the same session, send its agent "continue". Otherwise, start a new agent with `questions/Q1-concern-map.md`, the files in `platforms/shopify/` and the "Where this run stopped" section of its `notes.md`. The run must also apply the one-party rule: a shown `software`, `decides` or `legal` value names one party or place.
2. **Salla.** Resume the split pass from the "Where this run stopped" section of its `notes.md`.
3. **Check, capture and check again,** per platform. `RUN` is a folder holding one folder per platform.
   ```
   python3 -I method/check_concern_map.py RUN OUT
   CAPTURE_LANG='en,ar;q=0.8' CAPTURE_WORKERS=2 method/capture/run.sh OUT/urls-to-capture.json evidence/product-class/runs/<UTC time>-q1-<platform>-sources
   python3 -I method/check_concern_map.py RUN OUT evidence/product-class/runs/<that run>
   ```
4. **Matching pass.** This is step 4 of "How the run works" in the question. A separate pass that sees only the three outputs matches concerns only where the platforms' own terms clearly match. Every unclear match goes on a list for the founder.
5. **The combined map,** then the founder's review.

## If the container was reset

The checker reads local sources through these paths. Override them with environment variables.

- **observed-sh** at commit `b46731d0`: clone https://github.com/Hamza-ye/observed-sh to `/home/user/observed-sh`, or set `OBSERVED_SH`.
- **observed-sa** at commit `145f137`: clone https://github.com/Hamza-ye/observed-sa to `/home/user/observed-sa`, or set `OBSERVED_SA`.
- **WooCommerce 11.2.1:** download https://downloads.wordpress.org/plugin/woocommerce.11.2.1.zip, check its sha256 against `evidence/product-class/woocommerce-11.2.1/woocommerce.11.2.1.zip.sha256`, and unzip it into `/home/user/woocommerce-release/11.2.1/`, or set `WOO_RELEASE`. The cited files are also kept in `evidence/product-class/woocommerce-11.2.1/files/`.
