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

## Re-check against the observed runs, 19 October 2026

### What was read

- The guides of `observed-sh` at `c8b5fbee25966372a0475e6ed81f0b7760ac2921`: `README.md` and `docs/READING.md`, whole.
- `index/operations.jsonl`, filtered for the operations named Plus, renewal, plan, beta, feature, subscription or contract; `derived/admin-operations.jsonl`, the `Betas` query only.
- `python3 -I method/held_index.py` on the capture-plus addresses `settings/plan` (held: run 20261007T030938Z-journey-sidekick, steps 46 and 48), `settings/plan/plus/terms` (not held) and `settings/plan/shop_plus_self_renewals` (not held).
- Corpus searches, all with `--max 10`:
  - `"Beta Services" "beta terms" "beta feature" "early access" "ميزة تجريبية" "تجريبي"` (Q8-SH-N01);
  - `"Dependent on contract terms" "Shopify for enterprise" "Commerce Components" "enterprise"` (Q8-SH-N02);
  - `"Shopify Plus Terms" "PlusContractDetails" "currentContractTerms" "RenewalsQuery" "3-year term" "شروط Shopify Plus"` (Q8-SH-G0245, Q8-SH-G0246);
  - `"Choose a plan" "Plan details" "Sales channels" "Apps and sales channels" "اختيار خطة" "قنوات البيع"` (sentences 1 and 2);
  - `"betas" "enabledBetas" "Preview" "Feature previews" "Developer preview" "معاينة"` (sentence 3).
- Run files opened:
  - run 20261007T030938Z-journey-sidekick: `actions.jsonl` (steps 44 to 47), `steps/046.text.txt`, and the answers `PlusContractTerms/6d927459….json` and `OrionRenewalCommitment/f387b825….json` (`{"data":{"orionRenewalCommitment":null}}`, not recorded);
  - run 20261007T033925Z-journey-flow: the Flow answer `flow-core_graphql/7c64cf6b….json` (3.9 MB, read only around `publicDisplayName`) and `actions.jsonl` step 16;
  - run 20261007T010009Z-journey-partner-dashboard: `actions.jsonl` steps 58 to 75, `steps/066.text.txt`, `steps/069.text.txt`, and `steps/064`, `068`, `069.aria.yaml` (no list of plans was shown in any of them);
  - run 20261002T004032Z-sweep-capture-grow: `steps/420.aria.yaml` and its `actions.jsonl` row;
  - run 20261002T003831Z-sweep-capture-plus: the `Betas` answer `d7d6968c….json` (only `enabledFlags` booleans).

### Stores, as the runs name them

- Q8-SH-098: the Flow answer's row in `answers.jsonl` names no store (`"store": null`). Its step's address and page title in the run's `actions.jsonl` name capture-plus, and that row is cited (Q8-SH-C103).
- Q8-SH-099 and Q8-SH-100: the Create store page belongs to no store. The scope names the organization in the page's address, and says the run names no store.

### Open items

- Q8-SH-N01 (beta terms): unchanged. The runs show beta flags only as hashed names with true or false values. The search and the Betas answer were added to the row's `searched` and `read`.
- Q8-SH-N02 (enterprise contract terms): unchanged. No listed run document's title or snippet showed the terms. The search was added to `searched`.
- Q8-SH-G0245 (the Plus agreement): stays open. Store capture-plus's Plan page linked "Plus terms", but did not show them, and `PlusContractTerms` answered `"currentContractTerms":null` (Q8-SH-101, Q8-SH-102). `settings/plan/plus/terms` is not held.
- Q8-SH-G0246 (the Plus term and renewals): stays open. The Plus trial review page of store capture-grow shows the term choice at the end of a trial (Q8-SH-105, Q8-SH-106). No run reached the renewal routes.
- The coordinator listed no phrases for this folder.

### Wording changes (step 4)

- Q8-SH-N01 `route`: "the beta terms shown in the Shopify admin before the store first uses it" became "the additional terms and conditions that Shopify provides before the store's use of the Beta Services". Nothing read uses "beta terms". The new wording is the Terms' own (Q8-SH-061).
- Q8-SH-N02 `route`: "Shopify's enterprise sales team, through the contact form on Shopify's enterprise page: the enterprise agreement or order form that sets these services" became "Shopify for enterprise, through the get in touch link on the Help Center's Shopify for enterprise page". Nothing read names an "enterprise agreement", an "order form" or a "contact form". The commerce-components page shows "get in touch".
- Q8-SH-N02 `what_is_missing` was kept: "Shopify for enterprise" and "*Dependent on contract terms" are in `commerce-components.md` (`*_Dependent on contract terms_`, line 46).

### New statements

There are 9 new statements, Q8-SH-098 to Q8-SH-106, with citations Q8-SH-C102 to Q8-SH-C111.

### Not read

- The listed run documents beyond those above: the ExtensibilityHostUIExtensions, FetchThemeFiles, AnalyticsSchemas, MarketGraphShopProducts and Footer answers; the staff sweeps' Sales channels steps; the Discounts steps; and the GetPlusLeadQuestions and Flow-template answers.
- The pointers on payments and currency (PaymentProviders, ShopifyPaymentsData, MarketsHomeCurrencyOptions, the order-lifecycle journey, the General settings and third-party providers pages). They bear on no sentence of Q8.

### Tools

- The five corpus searches ran together in the background. They took more than ten minutes in all.
