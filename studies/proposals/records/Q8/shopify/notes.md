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

## Re-check against the step text from saved HTML, 19 October 2026

### What was read

- observed-sh at `51626891aa711ee9c3ef2d05ce63c95396dca949`: `docs/READING.md`, the entry for `derived/step-text-from-html/`, and that folder's `meta.json`.
- Corpus searches, all with `--only "step text from saved HTML" --max 10`:
  - `"Beta Services" "beta" "early access" "تجريبي"` (Q8-SH-N01; sentence 3, release stage);
  - `"Dependent on contract terms" "Shopify for enterprise" "Commerce Components"` (Q8-SH-N02): no document listed;
  - `"Plus terms" "Choose a plan" "Plan details" "اختيار خطة"` (Q8-SH-G0245, Q8-SH-G0246; sentences 2 and 3, by plan);
  - `"feature preview" "test drive" "Developer preview" "معاينة"` (draft ids Q8-SH-043, Q8-SH-044, Q8-SH-051, Q8-SH-073);
  - `"Sales channels" "Apps and sales channels" "قنوات البيع"` (draft ids Q8-SH-014, Q8-SH-015, Q8-SH-K2063);
  - `"Shopify Balance" "Locations" "Custom apps" "App extensions"` (draft ids Q8-SH-K0041, Q8-SH-K2591, Q8-SH-033, Q8-SH-081);
  - `"Feature test drives" "test drive" "Shopify Editions" "Plus terms"` (Q8-SH-043, Q8-SH-044, Q8-SH-064): only the Plus review pages were listed, no test drive page;
  - `"Shopify Balance" "Shopify Capital" "not available in your country" "غير متاح"` (Q8-SH-K0041, Q8-SH-055): only the Capital pages of run 20260930T045741Z-sweep-trial2 were listed;
  - `"Custom apps" "Develop apps" "App extensions" "Built for Shopify"` (Q8-SH-033, Q8-SH-081, Q8-SH-029): App Store category pages and the admin Apps pages.
- Texts opened under `derived/step-text-from-html/`, with each step's row in its run's `actions.jsonl` and, for comparison, its `steps/NNN.aria.yaml`:
  - `20261002T003831Z-sweep-capture-plus/321.html.txt` (plan choice) and `024.html.txt` (Sales channels settings);
  - `20260930T232928Z-journey-dev-stores/010.html.txt` (Create a dev store);
  - `20261002T004032Z-sweep-capture-grow/420.html.txt` (Plus trial review) and `277.html.txt` (Growth);
  - `20260930T045741Z-sweep-trial2/423.html.txt` (Plus upgrade review) and `128.html.txt` (Capital offers).

### Stores, as the runs name them

- Q8-SH-108: the Create a dev store page belongs to no store. As for Q8-SH-099, the scope names the organization in the page's address (`store-create/organization/238086467`) and says the run names no store.
- The other new statements' stores are as the runs' `answers.jsonl` name them (capture-plus, capture-grow).

### Open items

- Q8-SH-N01 (beta terms, routed to the founder): unchanged. The texts show "Early access" for Campaign Autopilot on the Growth page (Q8-SH-111), but no terms. The search and the text read were added to `searched` and `read`.
- Q8-SH-N02 (enterprise contract terms, routed to the founder): unchanged. The search listed nothing; it was added to `searched`.
- Q8-SH-G0245 (the Plus agreement): stays open. The Plus review pages' markup holds only the link "Plus terms" (and "Plus trial terms"), not the terms.
- Q8-SH-G0246 (the Plus term and renewals): stays open. The review pages add the organization move (Q8-SH-109) and the term prices already in their accessibility trees; no renewal route is among the texts listed.

### Wording changes (step 4)

None. The two rows' wording was checked in the last re-check, and nothing read here bears on it.

### New statements

There are 5 new statements, Q8-SH-107 to Q8-SH-111, with citations Q8-SH-C112 to Q8-SH-C119. Each says in its `note` that it is from the saved HTML and whether the step's `aria.yaml` shows the same words:
- Q8-SH-107: the aria tree holds the same plan headings and items, but not the prices;
- Q8-SH-108: the aria tree holds neither the plan options nor the feature-preview options; they are the select's options as the markup states them;
- Q8-SH-109 and Q8-SH-111: the aria tree holds the same words;
- Q8-SH-110: the aria tree holds only the footnote "¹ Variable fees may apply for larger businesses."; the Variable fees text is in the markup, likely a dialog that wasn't open.

None is between `⟦hidden⟧` and `⟦/hidden⟧`.

Not recorded:
- The feature preview list in `20260930T232928Z-journey-dev-stores/010.html.txt` (30 September) is the same six previews as Q8-SH-100 (7 October).
- Run 20260930T045741Z-sweep-trial2, step 423 (store ibx5bt-xy, 30 September) says the same as Q8-SH-109 in other words ("When you subscribe to the Plus plan, this store will move out of the My Store organization into a new organization.").
- The Capital offers page of store ibx5bt-xy (step 128): "There are no funding offers at the moment", with amounts in YER. It doesn't bear on how Shopify organizes what it offers.
- Sales channels settings (capture-plus, step 024): the settings list already recorded as Q8-SH-103, and "My Store 5 stores Organization Users Billing".

### For the draft

- Q8-SH-001 (several plans): Q8-SH-107 adds the plan choice page's offer on store capture-plus, Basic, Grow and Advanced with their prices and features.
- Q8-SH-K2743 (staff accounts by plan): Q8-SH-107 shows the same page saying "Up to 5 staff accounts" for Grow and "Up to 15 staff accounts" for Advanced.
- Q8-SH-051 and Q8-SH-073 (dev stores and feature previews): Q8-SH-108 adds that the Create a dev store page's markup held Basic, Grow, Advanced and Plus as plans to preview.
- Q8-SH-046 and Q8-SH-047 (expansion stores, organization): Q8-SH-109 adds that a store moving onto Plus moves out of its organization into a new one, keeping its payment method and user roles.
- Q8-SH-060 and Q8-SH-061 (Beta Services): Q8-SH-111 adds a feature the admin marks "Early access" (Campaign Autopilot). The page doesn't call it a Beta Service, and Q8-SH-N01 stays open.
- Q8-SH-110 (variable platform fees on Plus) bears on the draft's plan points but changes no id it cites.

The other draft ids (Q8-SH-014, 015, 016, 029, 030, 033, 035, 036, 040, 043, 044, 054, 055, 058, 064, 068, 069, 070, 081, 085, 095, K0041, K0175, K0191, K1243, K1930, K2063, K2169, K2183, K2591, K2696, K2812, N01) are unchanged by the texts read.

### Not read

- The other listed documents: the Growth page in other stores and runs; the Plus review pages of capture-advanced and sweep-dev; the reactivation plan pages (step 098); the domains `Developer preview` pages (step 227); the Capital pages beyond step 128; the Locations and Companies pages; the App Store category pages and the admin Apps pages.

### Tools

- Nothing got in the way. Each `--only` search took a few seconds.
