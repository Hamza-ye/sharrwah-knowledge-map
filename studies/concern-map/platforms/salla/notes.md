# Q1 concern map: Salla, run notes

Run on 2026-10-10 (UTC). Platform: Salla. Ids are prefixed `SA`.

## Files

| File | Rows |
| --- | --- |
| `inventory.tsv` | 2,620 entries from 20 lists (2,357 placed in a concern, 263 out of scope with a reason) |
| `concerns.tsv` | 148 concerns |
| `placements.tsv` | 740 placements (148 concerns × 5): 431 shown, 309 not shown |
| `citations.tsv` | 2,828 citations: 218 hand-picked (`SA-S-0001` to `SA-S-0218`) and 2,610 generated, one per inventory entry built from the held lists (`SA-S-1001` to `SA-S-3610`) |
| `not-reached.tsv` | 85 URLs (84 on salla.com, 1 on salla.sa) |

Working copies of fetched pages are in `fetched/` (rendered text from `page_text.mjs`, or the `.md` and raw files as served); every fetch is logged in `fetched/log.tsv`. There were 112 requests: 49 docs.salla.dev, 52 help.salla.sa, 7 partners.salla.com, 1 salla.dev, 1 status.salla.sa (redirected to status.salla.com), and 1 each to salla.com and salla.sa, both refused. Requests were sequential, at least 1.5 seconds apart per host. These copies are working copies, not captures. The held page `observed-sa/salla.com/ai-info` has no file extension; it was copied to `fetched/local-copies/salla.com-ai-info.html`, which has the same sha256, and rendered offline with `saved_page_text.mjs` so it could be read. Its quotes are cited against the held file, where each one appears verbatim.

Scripts are in `scripts/`. `build_inventory.py` builds the inventory from the held lists. `assemble.py` writes the four main tables and refuses any quote that is not a verbatim substring of its file. `check.py` re-reads the outputs and checks every quote, id and status. `not_reached.py` takes the salla.com URLs from the held sitemaps. The last run of `check.py` reported 0 errors.

## Lists used and their sizes

All lists come from `observed-sa@145f137:structures/salla/` unless a URL is given.

| `list` in inventory.tsv | Source | Size of the source list | Rows |
| --- | --- | --- | --- |
| api-resources | `docs-sidebar/merchant-api@20261009T033553Z` (Merchant API navigation) | 56 folders under "APIs", 14 top-level docs, the Webhooks folder and its 14 event pages | 72 |
| api-resources | `docs-sidebar/<nav>` for App API, App Functions, Checkout APIs, Ecommerce Events, Embedded SDK, Partners Agent Kit, Recurring Payments API, Salla Apps Playbook, Salla AWB, Salla CLI, Shipments & Fulfillment APIs, Twilight Engine, Twilight SDK, Web Components | folders (`apiDetailFolder`) only | 83 |
| extension-points | `docs-navigation/v2@20261009T001017Z` (the docs navbar) | 28 | 28 |
| extension-points | `portal-app-categories/partner@en` (app types: General, Shipping, Communication) | 3 | 3 |
| extension-points | `app-categories/api@en` and `api-app-impact@en` (App Store categories and goals) | 19 and 15 | 34 |
| extension-points | `portal-categories/` app, app_impact, theme | 10, 14, 18 | 42 |
| extension-points | `docs-event-lists/app-functions.supported-events` | 76 | 76 |
| extension-points | `docs-event-lists/ecommerce-events.*` and `ecommerc-events.*` (10 lists) | 64 | 64 |
| extension-points | `twilight-components/docs-json@2.14.587` | 142 | 142 |
| access-scopes | `portal-app-scopes/partner@en` | 24 | 24 |
| webhook-topics | union of `portal-webhook-events/partner@en` (79), `docs-event-lists/webhooks` (58, all also in the portal list), `partner-apis.app-events` (13), `recurring-payments.webhook-events` (5), `webhook-events.communciation-apps` (18) and `comm-apps.event-payload-reference` (3) | 176 rows, 107 distinct topics | 107 |
| settings | `dashboard-settings-menu/merchant@en` | 23 pages and 4 group headings | 27 |
| settings | `settings-center/merchant@en` sub-pages and Markets, named by `dashboard-translations/en/settings.json` | 67 | 67 |
| admin-navigation | `dashboard-main-navigation/merchant@en` | 133 | 133 |
| admin-navigation | `partners-portal-navigation/partner@en` | 45 | 45 |
| plan-features | `merchant-plans/merchant@ar` (Salla Plus and Salla Pro, features and sub-features) | 206 lines | 206 |
| plan-features | `com-plans/ar-sa`, `com-plans/ar-ae` ("المزايا الأساسية" block and table sections) | 19 and 15 | 34 |
| plan-features | `com-specialplan/ar-sa` (feature headings; the ar-ae page is identical) | 13 chosen lines | 13 |
| legal-agreements | `salla.com/sitemap_*.xml` (held), policy and terms URLs | 9 per sitemap × 4 | 36 |
| legal-agreements | salla.com footer (`com-plans/ar-sa` text) | 4 | 4 |
| legal-agreements | agreements named on pages read: help.salla.sa (3), partners.salla.com legal pages (5), dashboard translations (1), Partners portal app record (1) | 10 | 10 |
| other:staff-permissions | `staff-permission-groups/demo@en` | 16 groups, 201 permissions | 217 |
| other:partner-access-permissions | `portal-stores-access-requests-permissions/partner@en` | 15 groups, 195 permissions | 210 |
| other:order-statuses | `order-statuses/merchant@ar` | 13 | 13 |
| other:store-payment-methods | `showcase-store-payments/com-en-sa` (methods on 51 showcased stores) | 14 distinct methods | 14 |
| other:app-supported-countries | `portal-apps-supported-countries/partner@en` | 7 | 7 |
| other:portal-countries | `portal-countries/partner@en` | 240 | 240 |
| other:partner-payout-statuses | `portal-payouts-filters/partner@en`, status options | 7 | 7 |
| other:partner-id-types, other:partner-id-statuses | `portal-settings-verification-id[-profile]/partner@en` | 2 and 7 | 9 |
| other:dashboard-features | `dashboard-features/merchant@en` (feature flags with plans and countries) | 568 | 568 |
| other:dashboard-apps | `dashboard-apps/prod` (the dashboard's registry of its bundles) | 82 | 82 |
| other:footer-markets | salla.com footer "مدعوم في:" list (`com-plans/ar-sa`) | 3 | 3 |

## Where the inventory stops

- **APIs.** The API reference is inventoried at the level of its navigation folders, not its 285 operations (`docs-operations`) or its 409 schema definitions (`docs-dataschemas`). Operations are cited where a sentence in them matters: settlements, transactions, taxes, customer wallet and store scopes.
- **Settings.** Settings are inventoried as pages and sub-pages, not as individual fields; the settings centre has 796 nodes in merchant@en. Sub-page names come from the dashboard's settings translations, which carry both the section key and its label. The locator also gives the settings-centre line.
- **Permissions.** Permissions are inventoried one by one, with group headings marked out of scope.
- **Plans.** Plan lines are inventoried as Salla lists them. The plans page's comparison table appears in the held text only as section headings, so those headings are out of scope with that reason.
- **Webhook topics.** These are a union across lists: the first list that shows a topic is cited. The docs' conditional-webhooks list (35 rows) and the recurring-payments changelog (5) name topics already inventoried, so they were not added again. The App Functions welcome page's 18 summary lines repeat the supported-events list.
- **Flags.** Feature flags are inventoried one by one. 48 flags whose names do not identify a concern (rollout, UI or internal toggles) are out of scope with that reason.
- **Lists held but not inventoried.** Each is below the inventory level, repeats a list that is inventoried, or is not a list of platform parts:
  - **Used only to find sources:** `docs-operations` and `docs-dataschemas` (cited where relevant); `dashboard-translations` (used for settings names and as a cited source of UI statements); `dashboard-app-routes` (used to find `/manage/violation`).
  - **Overlap with the main navigation:** `dashboard-nav`, `dashboard-nav-segments` and `dashboard-menu-*`.
  - **Engineering registries:** `dashboard-importmap`, `portal-importmap`, `canvas-apps`, `portal-apps` and `portal-app-routes`.
  - **Storefront data:** `storefront-init`, and `storefront-api`, whose endpoint names appear only in capture metadata.
  - **Field-level UI lists:** `theme-design-components`, `theme-marketplace`, `performance-reports`, `report-widgets`, `report-widget-categories`, `report-catalog`, `export-columns`, `importer-schemas`, `importer-schema-fields` and `dashboard-filter-components`.
  - **Small or account-specific dashboard lists:** `dashboard-quick-actions`, `dashboard-account-actions`, `onboarding-status` and `dashboard-edu`.
  - **Taxonomies of products and posts, not platform parts:** `mahally-*` and `community-*`.
  - **Third-party app listings:** `marketplace-apps`.
  - **Help-centre taxonomy:** `help-tree`, `help-embedded-tree`, `help-sitemaps` and `help-article-redirects`, used to find articles.
  - **Small, account-specific or UI lists from the Partners portal:**
    - subscriptions and development-store filters;
    - experts and influencer profiles;
    - affiliate filters;
    - notifications, me, settings, private-settings, employees, dashboard, app, app-meta and app-select;
    - partner reports;
    - help-centre articles and resources;
    - onboarding steps, iframe pages, snippets and report builder.
  - **The test account's own function:** `portal-app-builder-functions` holds one function belonging to the account used for capture.
  - **Other captures:** `app-webhook-deliveries`, `help-self-descriptions`, `apps-route-manifest` and `apps-sitemap`. `dashboard-features` was captured for other accounts too (demo, public-demo, signed-out); only merchant@en was inventoried.

## How placements were made

- **Overrides.** Each placement is either `shown`, with citations, or `not shown`; no other status is used. For 81 concerns at least one placement is written by hand from the sources read; `scripts/placements_spec.py` holds these.
- **Defaults.** The other placements are filled from the concern's own inventory rows, as readings of Salla's own lists:
  - **software: core.** The concern is a group of Salla's Merchant API (api.salla.dev/admin/v2), a bundle in the merchant dashboard's registry of its own bundles, or a page of the merchant dashboard or settings.
  - **decides: merchant.** The concern is a page of the merchant's own settings or dashboard.
  - **decides: operator per plan.** The concern appears among a plan's features in the dashboard's plan list, or behind a feature flag limited to plans.
  - **boundary.** The concern's API groups, scopes, webhook topics and settings page.
  - **legal and reason.** These are `not shown` unless a source says so.
- **Product lines.** "Separate service or product line" is used only where Salla names the product as its own (llms-full.txt, help pages, dashboard text). Examples: Salla Payments (مدفوعات سلة), Salla Ads, Mahally, Salla Point, App Maker, the App Store, Salla shipping labels (بوليصات سلة) and صندوق سلة.
- **Concerns without inventory rows.** Four concerns have none; their split notes start "Not in the platform's lists:". Three come from the question's list of architecture concerns: payment processor and licence, settlement currency, and data location. The fourth is the storefront API, which comes from Salla's status page: its held lists name their endpoints only in capture metadata, so they were not inventoried.
- **Concerns named only by agreements.** No list entry of its own names legal entities, licences or partner failure. Their inventory entries are the agreements on partners.salla.com that state them: the company owning Salla, the licences partners must hold, and what happens when a partner's app or theme fails or is withdrawn, or when payment gateway changes stop commission calculation. The placements were made from the sources before these links and do not change with them.

## What could not be shown

- **The contracting entity per market.**
  - **Shown.** Partner-facing legal pages name the owning company. Footers name شركة سلة القابضة.
  - **Not shown.** No source read names:
    - the entity that contracts with merchants in Saudi Arabia, the UAE or Kuwait;
    - the counterparty of the "payment services contract" (عقد خدمات الدفع) that UAE and Kuwait help pages say governs settlement and fees.
  - **Not reached.** The merchant terms on salla.com.
- **Licences and who processes payments.**
  - **Shown.** Salla describes online payments as a service it provides, and a balance held before payout.
  - **Not shown.** Any licence held by Salla, or any acquirer, bank or payment partner behind Salla Payments.
- **Who holds the funds legally.**
  - **Shown.** The help pages show:
    - the flow, buyer → e-payments balance → payout;
    - the per-market schedules;
    - that the e-payments balance "holds" (يحتفظ) the store's sales proceeds before transfer.
  - **Not shown.** The legal holder.
- **Sanctions.** No source read mentions sanctions lists or sanctions screening. What is shown:
  - store verification, with an Absher check for Saudi owners and beneficial owners for Kuwait;
  - store violations with a 24-hour deadline before suspension;
  - cash on delivery hidden from customers banned in other Salla stores;
  - payouts blocked while a complaint is open.
- **Where data lives.** Not shown in any source read. The privacy pages that would say were not reached.
- **Partner failure.** No source read describes a fallback when a payment gateway or carrier is down. What is shown:
  - carrier auto-assignment trying the next carrier when the first does not deliver to the area;
  - communication apps reporting delivery failure to the store;
  - an affiliate-plan clause that disclaims gaps caused by payment gateway outages;
  - a status page that lists only Salla's own components.
- **Customs duties.** Who sets or pays them is not shown. The settings page path (`/taxes-and-duties`) and an IOSS tip are the only traces.
- **Currency conversion.** The rate source is not named. A dashboard string says market prices follow "the current exchange rate". Help pages say Salla Payments receives all payments in SAR in Saudi Arabia, and that UAE and Kuwait payout accounts must be in AED and KWD.
- **Legal placement.** Legal placement is not shown for most concerns (126 of 148), because the merchant terms and privacy policy were not reached.
- **Stated reasons.** Reasons are rare: 13 concerns have one.

## Salla's product lines, as Salla shows them

| Product line | Concern | Where Salla names it |
| --- | --- | --- |
| Salla Payments (مدفوعات سلة) | SA-C-110 | help pages for Saudi Arabia, the UAE and Kuwait; dashboard text ("Salla Payments") |
| Salla shipping labels (بوليصات سلة) | SA-C-140 | plan lines; help pages on COD and international shipping |
| Sandouk Salla (صندوق سلة), with the fund manager Tanami | SA-C-128 | dashboard payments text |
| Salla Ads (إعلانات سلة) | SA-C-073 | llms-full.txt |
| Mahally (محلي) | SA-C-096 | llms-full.txt |
| Salla Point (سلة بوينت) | SA-C-095 | llms-full.txt |
| App Maker | SA-C-094 | llms-full.txt |
| App Store | SA-C-194 | llms-full.txt; App Store terms |
| Wholesale market (سوق الجملة) | SA-C-098 | plan lines; staff permissions |
| Merchant services (Experts) | SA-C-205 | dashboard and Partners portal |
| Salla Chat | SA-C-099 | dashboard |
| Salla Special plan | SA-C-004 | com-specialplan |

Each is placed as "separate service or product line" only where a cited source names it as Salla's own product.

## Languages read

Arabic sources were read in Arabic and quoted in Arabic: help.salla.sa articles, partners.salla.com legal pages, the dashboard's Arabic UI strings, the dashboard plan list and the Arabic plans pages. The merchant dashboard's navigation, settings menu, settings sub-page labels, feature flags and Partners portal lists were inventoried from their English (merchant@en, partner@en) captures. I checked the main navigation (133 items) and the settings menu (27 items): their Arabic captures (merchant@ar) have the same addresses in the same order. The English names are Salla's own English labels. The docs are in English and quoted in English.

## Where Salla's own sources disagree (recorded, not resolved)

- **Owning company.** The App Store terms name شركة تطبيق سلة لتقنية المعلومات with registration 4031200589. The partners joining policy names the same company with 7011845513. The themes terms name شركة منصة سلة للاتصالات وتقنية المعلومات with 7011845513. The affiliate agreement names شركة منصة سلة للاتصالات وتقنية المعلومات (شركة شخص واحد) with 4031200589. Footers name شركة سلة القابضة.
- **Payout frequency in Saudi Arabia.** An older help page ties frequency to plan: Plus weekly, Pro every 48 hours, Special daily. The newer page lets the merchant choose a cycle. Dashboard text says faster options are locked on some plans. The Special plan page says "every 24 hours".
- **Kuwait payout minimum.** The Kuwait settlements page says both "a minimum of one Kuwaiti dinar" and "no minimum".
- **Currencies.** A plan line offers payment in "+33" currencies. The ai-info page (last updated November 2025) says "more than 15 currencies".
- **Kuwait BNPL providers.** The Kuwait payment-methods page lists "ديما، تالي" in its table and "تابي و ديما" in its text and FAQ. The concern cites the FAQ.

## Problems with method, and facts about the sites

- **salla.com and salla.sa.** Both answer HTTP 403 with a bot-challenge page ("Just a moment..."). I tested one URL on each, logged both, and went no further. Every needed salla.com page is listed in `not-reached.tsv` with its exact URL from the held sitemaps. Two more URLs, `/uae` and `/uae/store-checklist`, are named in the held llms-full.txt but missing from the sitemaps.
- **Text addressed to AI systems.** Some text is aimed at AI systems; it was read as data and not followed.
  - **`salla.com/llms-full.txt`:** answer guidance and a source hierarchy for AI answers.
  - **`salla.com/ai-info`:** a section "إرشادات مساعدي الذكاء الاصطناعي" with a prescribed summary and citation format.
  - **help.salla.sa's `llms.txt`:** a section-link convention.
- **Quotes.** Quotes are verbatim, including no-break spaces (U+00A0) that help.salla.sa pages use inside sentences. While matching, the assembler treated a no-break space as a space and compared Arabic diacritics in canonical order; it then copied the exact original characters from the file. The capture step should compare against the page text as rendered.
- **Dates.**
  - **help.salla.sa:** each article's "تاريخ اخر تحديث".
  - **salla.dev tutorial:** its publication date.
  - **llms-full.txt and ai-info:** the review or update dates they state.
  - **Undated live pages** (docs.salla.dev, partners.salla.com, the status page): dated 2026-10-10, the day read.
  - **Held structures:** the capture date in their metadata.
- **Help article versions.** Some help articles exist in an old and a new version; an old page carries "هذه المقالة قديمة". Both are cited where they disagree.
- **The capture account's own data.** Some Partners portal records belong to the account used for capture. One is the app's contract record, named "SaaS contract _ individual _.docx_…". They are cited only to show that the record type exists.
- **Mid-run change.** The coordinator relayed a rule change during the run: sources dated before 2023 are no longer treated as historical, and the status is only `shown` or `not shown`. No placement used `historical`. No cited source in this map is dated before 2023 anyway; the oldest is 2025-11.
- **Capture tools changed on disk.** `ocr.sh`, `finalize.py`, `render.mjs` and `fetch_raw.py` changed during the run. This run used only `page_text.mjs` and `saved_page_text.mjs`.

## Where this run stopped

- **Split pass on `salla-multi-party.tsv`: paused before any row was changed.** Done: none (0 split, 0 kept as joint, 0 false hits). The six files are as they were after the previous fixes, and `check.py` reports 0 errors (148 concerns, 740 placements).
- **Remaining: all 100 rows.**
  - `decides` (93 rows): SA-C-001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 040, 041, 042, 043, 044, 045, 047, 048, 060, 061, 062, 063, 064, 065, 066, 070, 071, 072, 073, 074, 075, 076, 077, 078, 079, 081, 082, 090, 091, 093, 094, 095, 096, 097, 110, 111, 112, 113, 115, 117, 118, 120, 121, 123, 124, 140, 142, 143, 144, 146, 150, 160, 161, 163, 165, 179, 191, 192, 194, 195, 196, 199, 200, 205, 220, 231, 232.
  - `software` (2 rows): SA-C-063, 194.
  - `legal` (5 rows): SA-C-146, 176, 190, 194, 231.
- **Also remaining from the same request.** SA-C-116/legal's `other:` value is still an English rendering; it is to be replaced with the source's own words. The `decides` values that begin with "app developer" (SA-C-091, 124, 191, 192, 196, 199, 200) are among the listed rows above.
- **Working files.** `scripts/build/prev2/` holds a copy of the outputs and scripts taken when the pass began. `scripts/split/analyse.py` prints each listed concern's inventory rows and placements; it writes nothing.
