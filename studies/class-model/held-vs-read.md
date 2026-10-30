# What the evidence repositories hold, against what the class's model read (30 October 2026)

**What this is:** the measure of the gap between the evidence held and the evidence the model read, made after the founder's decision of 30 October on reading what is held (`founder-decisions.tsv`, "Method (standing)"). It comes from `python3 -I method/held_vs_read.py`, which writes `held-vs-read.tsv` (one row per platform, kind and group).

**Why there is a gap:**
- The model's cells cite the concern map, and the landed subjects' statements that the points amended in.
- The concern map was finished on 12 October 2026 (commit `8df2a239`). It read observed-sh at `b46731d0` and `e49840729` (9 and 11 October), observed-sa at `145f137` (9 October), and the public pages of Zid, BigCommerce and WooCommerce, captured in this repository.
- Captures after 12 October never reached the model. That includes observed-sh to `19a5f6435` and observed-sa to `b0bd0b16` (both 28 October), and all of other-product-class: Zid's dashboard from 28 October, BigCommerce's and WooCommerce's from 29 October.
- The extent's plan built the model from the concern map without checking it against what the repositories hold today. That was the coordinator's miss.

## The measure, at observed-sh `19a5f6435`, observed-sa `b0bd0b16` and other-product-class `0d79b79`

| | Shopify | Salla | Zid | BigCommerce | WooCommerce |
|---|---|---|---|---|---|
| Structures in the register, held | 125 | 137 | 8 | 8 | 7 |
| … that what the model read cites | 47 | 31 | 1 | 0 | 0 |
| … their items, and the items cited | 38,538; 3,384 | 10,161; 1,855 | 33,722; 0 | — | — |
| Structures never cited, and their items | 78; 48,640 | 106; 23,598 | 7; 1,404 | 8; 637 | 7; 364 |
| Addresses held readable (pages, admin pages, saved answers) | 30,913 | 8,641 | 1,039 | 381 | 175 |
| … that what the model read cites | 175 | 102 | 203 | 156 | 120 |
| Cells of the merged model with nothing held | 74 of 347 | 95 | 154 | 175 | 160 |

**How to read the measure:**
- An item is a line of a structure's `items.jsonl`, in every label (store or language) it is held under, so one item held for three stores counts three times.
- An address counts each held page, admin page, browser step and saved answer once. Those include the admin's own API answers, such as Shopify's 8,277 under `admin.shopify.com/api`. Not every address bears on the extent.
- `held-vs-read.tsv` gives the groups behind each count.

## What is closed, and how

1. **Every self-description is read entry by entry.** These are the structures that list each platform's own places (routes, sections, menus, settings, page indexes), its plans (plan lines, features, policies), its permissions and roles, its catalogs (app categories, channels, carriers, gateways, tax services, report catalogs, webhook events) and its change records. Each is selected from the register, its entries are listed by script, and each entry is placed: on a capability, as a new capability, or out of scope with a reason.
2. **Each cell still with nothing held** is read against the held pages: the admin as captured, then help and docs, through each repository's guides and indexes first.
3. **The coordinator amends the model** from both and merges again. Q3's candidate misses are checked against the result, and the independent review reads all of it.
