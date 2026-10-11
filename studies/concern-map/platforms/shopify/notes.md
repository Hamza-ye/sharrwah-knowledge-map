# Q1 concern map: Shopify, run notes

Run started 2026-10-10 and continued past midnight UTC into 2026-10-11. Pages fetched before 00:00 UTC carry access date 2026-10-10; the five legal pages rendered after it (Shopify Tax terms, Shopify Tax Automated Filing terms, Shopify Shipping terms, Agentic Storefronts terms, upcoming DPA) carry 2026-10-11 in `fetched/log.tsv` and in `citations.tsv`.

Files: `inventory.tsv` (2,428 entries), `concerns.tsv` (196 concerns), `placements.tsv` (1,120 rows: 862 shown, 258 not shown), `citations.tsv` (3,192 citations: 2,322 local, 486 md, 384 rendered), `not-reached.tsv` (4 URLs). Working copies are in `fetched/` with every fetch logged in `fetched/log.tsv`; scripts are in `scripts/`, and the hand-written citation and placement blocks in `work/cites/` and `work/placements/`. `scripts/build.py` writes the four main TSVs from those blocks and checks every quote against its file.

## Lists used and their sizes

Inventory entries per list (out-of-scope entries in brackets):

| list | entries | out of scope |
|---|---|---|
| access-scopes | 218 | 0 |
| admin-navigation | 104 | 12 |
| api-resources | 175 | 7 |
| extension-points | 326 | 0 |
| legal-agreements | 120 | 17 |
| plan-features | 185 | 23 |
| settings | 25 | 0 |
| webhook-topics | 329 | 0 |
| other:account-destinations | 9 | 2 |
| other:app-store-categories | 161 | 0 |
| other:billing-charge-categories | 37 | 1 |
| other:business-entities | 4 | 0 |
| other:help-center-sections | 260 | 0 |
| other:notification-templates | 68 | 0 |
| other:partner-dashboard | 10 | 0 |
| other:partner-permissions | 4 | 0 |
| other:shopify-apps | 7 | 2 |
| other:shopify-com-products | 28 | 1 |
| other:signup | 11 | 0 |
| other:staff-permissions | 267 | 0 |
| other:staff-roles | 20 | 0 |
| other:translatable-resources | 19 | 0 |
| other:ucp | 37 | 0 |
| other:value-lists | 4 | 0 |

Every list comes from Shopify's own surfaces, read from the observed-sh captures (cited as `observed-sh@b46731d0:<path>`, access `local`) or live from shopify.com and help.shopify.com. Dates: a list's date is the capture date its `meta.json` shows; undated live pages count as current on the day read.

## Where the inventory stops

- API references: one entry per API category or API (the GraphQL Admin API at its 28 categories; small APIs at their root operations), not per object or field.
- Access scopes: one entry per scope name; webhooks: one entry per topic (CLI topic list for API 2026-10 plus the admin's webhook topic list).
- Settings: the union of the settings navigation seen; admin navigation: main navigation items and admin router sections, not individual routes.
- Permissions: one entry per permission handle or collaborator checkbox; staff roles per role.
- Plans: one entry per row of the public pricing table and of the admin plan comparison (both kept, because they differ).
- Legal: the Shopify Legal index links and headings, the tables of contents of the main agreements, and the ToS 9.x subsections; the financial complaint form's product list.
- Extensions: CLI extension templates and UI extension targets at their latest versions; Flow at connector level (Shopify-connector tasks were not expanded one by one).
- Value lists (sign-up countries, tracking carriers, languages, return and inventory reasons) are one entry each, with the option count in the entry.
- Help Center: the "In this section" children of 24 chosen parent pages (payments, finance, taxes, markets, international, fulfillment, compliance, privacy, apps, checkout settings, billing, POS), not the whole Help Center.
- Structures not used as lists: CLI commands, theme files, beta flags, Sidekick streams, Flow templates and step environments, web-route manifests, docs front matter, changelogs, mobile and POS UI dumps, and the webhook sample payloads (a duplicate of the topic list). The app-install consent capture was used only as evidence.

Out-of-scope reasons in `inventory.tsv` cover navigation headings, developer tooling, footnote rows and entries whose function the source does not state.

## Concerns

196 concerns, from accounts and billing through payments, finance, tax, markets, shipping, marketing, channels, data, legal, apps and the needs that the App Store categories cover. Business lines are kept as Shopify shows them (Shopify Payments, Shopify Balance and its cards, Shopify Credit, Shopify Capital by country, Shopify Bill Pay, Shop Pay, Shop Pay Installments, Shopify Protect, Shop Cash, Managed Markets, Shopify Shipping, Shopify Fulfillment Network, Shopify Tax and automated filing, Audiences, Collabs, Shop Campaigns, Marketplace Connect, Collective, POS, Flow, Sidekick, Inbox). Splits made because parts sit differently:

- Shopify Capital is split by country (United States, United Kingdom, Canada, Australia, France, Germany, and Ireland/Netherlands/Spain), because the funding party differs: WebBank (US), YouLend (UK and the three merchant-cash-advance countries), Banking Circle S.A. with YouLend SAS and Shopify Commerce France SAS (France), YouLend GmbH with Shopify Commerce Germany GmbH as credit broker (Germany); no lender is named for Canada or Australia.
- Shopify Payments is split into the service (supplied by a Shopify entity per Designated Country), processing and settlement (Payment Processors), custody of funds, payment facilitation in the EU/EEA and UK, and regulated payment services in Canada.
- Balance account and Balance cards are split (account funds with Stripe Payments Company and Fifth Third Bank; cards issued by Celtic Bank).
- Where one concern's legal placement differs only by the merchant's country (contracting party, Shopify Payments entity), it is kept as one concern with one placement row per entity group.

## What could not be shown

- Reasons: 163 of the 198 reason rows are not shown. Shopify's sources mostly say what a feature does, not why it sits where it does.
- Legal party: 65 legal rows are not shown, mostly for core features where the sources name no entity beyond the Shopify Contracting Party of the Terms.
- Exchange rates: the sources say the rate is mid-market without markup and the fee is "the fee that Shopify charges", but they do not name the source of rates or the party that performs the exchange.
- Shopify Capital in Canada and Australia: no lender named. Local payment methods: no provider named per method. In-person card processing: no processor named on the POS pages read.
- Who handles financial-product complaints; who holds or transmits Collabs payments to creators.
- Shopify Audiences terms and the fee values in the merchant's own Shopify Payments terms sit inside the signed-in admin and were not read (see `not-reached.tsv`).
- The Digital Service Act page linked from the legal index returned 404; the contracting-party country list redirects to the legal index.
- Software placement of sanctions screening: the sources state the rules but not where screening runs.

## Source disagreements recorded

- Retention after a store closes: the privacy policy (updated July 7, 2026) says store information is kept for two years before deletion begins; the Supplementary Terms for EU merchants (last updated February 14, 2022) say personal information is deleted within 90 days of termination. Both are recorded on the data retention concern.
- Binding Corporate Rules: the Help page on onward transfers says the application is in its final stages; the BCR page says the BCRs took effect on July 8, 2026, and the privacy policy says EEA and Swiss transfers follow the BCRs.
- Shopify Capital product type: the financial complaint form lists "Capital - US Merchant Cash Advance (MCA)" and "Capital - Canada Merchant Cash Advance (MCA)", while the US and Canada Help pages describe loans.
- Plan prices: the public pricing page and the admin plan comparison of one captured store show different prices for Basic ($39 and $27 USD a month) and different row groups. Inference: prices vary by store or region; no source read states the rule.
- The legal index link "View fulfillment network terms" points to Terms of Service section 9, which has no fulfillment network subsection (9.1 to 9.14).
- Sign-up country list (233 options) omits Russia, which the business-entity country list (237) includes; neither list includes Cuba, Iran, North Korea or Syria, which the unsupported-regions page names. Inference: the omissions of those four follow that page; no source explains Russia.

## Method notes and problems

- Quotes are verbatim substrings of the fetched or captured files. Quotes from the observed-sh captures are JSON fragments (for example `"label": "Orders"`) with a line locator. Quotes from Help Center `.md` copies can contain markdown links, HTML tags or HTML entities such as `&#39;` exactly as served; where possible a nearby sentence without them was chosen.
- The Shopify Payments terms for different countries (`/legal/terms-payments/us`, `/gb`, `/jp`, `/ae`) were served with identical content (same sha256), so country variants could not be told apart by URL; the rendered `/legal/terms-shopify-payments` page, with its regional parts, was cited instead.
- `/legal/country-list` redirects to `/legal`; `/legal/upcoming-dpa` (linked from the Terms of Service) redirects to `/legal/dpa`.
- Engineering posts (shopify.engineering, 2018 to 2022) were cited from the local capture run `evidence/shopify-engineering/runs/20261010T083026Z-engineering-sources/items/` with their published dates. The run manifest's age labels were not used: after the coordinator's change, older sources count like any other and every placement status is `shown` or `not shown`.
- Notes on placements that mention a citation give its SH-S id.
- A row's value starts with the placement category (for example `operator, per market:` or `separate entity of the platform:`). Values outside the agreed lists start with `other:`.
- https://shopify.dev/docs/agents.md contains install instructions aimed at AI coding tools (for example a plugin install command for Claude Code). It was treated as data; nothing on it was run.
- Rate: about one request per second per host; no proxy refusals were met.

## Where this run stopped

The run was paused at the coordinator's request after the apps and App Store category placements were written. All six files are consistent: every inventory entry is placed or carries an out-of-scope reason, every concern has all five placements, and every SH-I, SH-C and SH-S id resolves (checked after the last build).

- Lists fully inventoried: all 24 lists above (2,428 entries); none is pending.
- Concerns fully placed: all 196 concerns have explicit rows for software, decides, legal, boundary and reason; no placement was defaulted and none is marked pending.
- What remains, in order:
  1. Apply the coordinator's new rule to rows already written: a shown software, decides or legal value names one party or place. A word scan flags 98 shown rows that mention two parties; most mention the second party only as context, but some name two actors and must be split, for example: SH-C-019 decides (developer sets prices, merchant approves), SH-C-049 decides (merchant places extensions, Shopify can disable them), SH-C-052, SH-C-053, SH-C-122, SH-C-123 and SH-C-124 decides (merchant configures, Shopify executes), SH-C-056 decides (buyer requests, merchant approves), SH-C-068 decides other (banking partners and processors), SH-C-072 decides (Shopify enrolls; merchant or Shopify contests), SH-C-088 legal (Stripe Payments Company and Fifth Third Bank), SH-C-110 legal (Global-e; Shopify not a party), SH-C-149 software. Rows written as `other:` must carry the source's own words rather than a paraphrase. The shown `other:` rows are: decides on SH-C-019, SH-C-048, SH-C-065, SH-C-068, SH-C-070, SH-C-157, SH-C-162, SH-C-176 and SH-C-179; legal on SH-C-065, SH-C-070, SH-C-071, SH-C-099, SH-C-109, SH-C-149, SH-C-170, SH-C-179 and SH-C-184. The decides rows on SH-C-157 and SH-C-162 are the former app-developer values.
  2. Read the Shopify Credit Issuing Bank Terms and Shopify Credit Program Terms (https://www.shopify.com/legal/shopify-credit-issuing-bank-terms, https://www.shopify.com/legal/shopify-credit-program-terms) to settle the legal and boundary rows of Shopify Credit.
  3. Where cheap, look for stated reasons for the most-used placements (reason is not shown for 163 rows).
  4. Run `python3 -I scripts/cite.py check` and `python3 -I scripts/build.py`, then hand back the final report (counts per file, lists used, biggest gaps, pages not reached).
- Exact next step: from the output directory, list the shown software, decides and legal rows of `placements.tsv` that name two actors, split each in the matching `work/placements/*.txt` file into one row per party (with the citations that support each part), rewrite `other:` values with quoted source words, and rerun `python3 -I scripts/build.py`.
