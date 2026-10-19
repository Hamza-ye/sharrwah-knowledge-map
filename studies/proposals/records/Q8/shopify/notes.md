# Notes: Q8, shopify

## Selection

178 concerns were copied and 21 were set aside, with the reasons in `selection.tsv`. The copy holds 2,416 statements and 220 gaps. S-01 was set aside. No concern was added.

## What was read (all held; read 2026-10-19)

The Help Center map, read through `method/help_map.py`:
- the menus list;
- the pages listed under Intro to Shopify, Apps and Organization settings;
- 8 pages from those menus:
  - `intro-to-shopify/pricing-plans/plans-features.md`;
  - `.../features-on-all-plans.md`;
  - `.../shopify-agentic-plan.md`;
  - `.../commerce-components.md`;
  - `apps/about-apps.md`;
  - `apps/extensions-and-functions.md`;
  - `organization-settings/test-drive.md`;
  - `organization-settings/expansion-stores.md`.

The Terms of Service, held as a capture of https://www.shopify.com/legal/terms (`evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/143-shopify.com`). I read the preamble, sections 1, 3 and 9.1 to 9.10, and section 15.

From shopify.dev:
- `docs/api/usage/versioning.md`, held as a capture (items/112);
- four records in the shopify-dev-md fetch archive: `feature-previews.md` (offset 24315784), `app-extensions.md` (21488927), `list-of-app-extensions.md` (21500063) and `location-rules.md` (23590692);
- `DiscountCustomers.md` (7162144), opened only to check a search snippet.

Other held pages:
- `www.shopify.com/editions` (published-web-route-manifests archive, offset 975903);
- `help.shopify.com/en` (help-en-md archive, offset 3185), whose topic list I didn't record;
- `www.shopify.com/enterprise` (shopify-com-pages archive, offset 12767941).

`observed-sh` at `c8b5fbee`: the three admin-betas lines for the beta names 749e4f05, 4d3efaac and a2abf0ea, in `structures/shopify/admin-betas/2jiwxs-gr@20261006T232216Z-journey-signup-new-account/items.jsonl`. Each gives only the name and `"enabled": false`. No held page I read says which feature a beta name stands for, so nothing was recorded from them.

**Live pages:** none were read.

## Corpus searches

All were run with `--max 10`:
- `"Beta Services" "developer preview" "feature previews" "Shopify Editions" "النسخة التجريبية"`;
- `"Beta Services"`;
- `"beta terms" "Beta Services" "beta program" "برنامج تجريبي"`;
- `"Commerce Components" "enterprise agreement" "Dependent on contract terms" "Shopify for enterprise"`;
- `"749e4f05" "a2abf0ea" "4d3efaac"`.

## Tables recorded in part

`list-of-app-extensions.md` has 24 rows, so I recorded only the rows that bear on the question (11). I left out these 13 rows:
- Product configuration;
- Admin link extensions;
- Discount function settings;
- Navigation links;
- Purchase options extensions;
- Subscription link;
- Web pixel (in the admin, checkout and online store areas);
- Triggers, Actions and Lifecycle Events (Flow);
- Theme app extensions, whose row is in the copies' concern SH-C-166.

## Not read

- The rest of the Help Center pages under Intro to Shopify, such as the individual plan pages, Choosing the right plan, the Shopify Plus plan and Local Pricing.
- The pre-approved expansion store types, past the start of that section.
- The shopify.dev changelog items found by the first search.

## Copies, method and tools

- I found no copy wrong or out of date. The checker reported no copy as changed.
- The help-center statements cite pages that show no date. Their `source_date` is the date of the held capture, and `date_basis` says so.
- I read `copied-view.tsv` filtered: its JSON route rows were left out, except the pricing-table rows and the rows that name regions, plans, betas or entitlements. The full file is 479 KB because Q8 copies 178 concerns.
- The versioning capture is stored under its `.md` URL, so it is cited by that URL. The URL without `.md` resolves in `held_index.py` but not in the checker.
- Corpus searches with several terms took over two minutes, past the shell's default timeout, so they were run in the background.
