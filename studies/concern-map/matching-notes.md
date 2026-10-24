# Q1 concern map: matching pass (2026-10-11)

This pass says which concerns are the same across the three platform maps (Shopify, Salla, WooCommerce). It matches only where the platforms' own terms, identifiers or definitions clearly match. Every other likely pair is on the unclear list for the founder, unsettled. The rule is step 4 of "How the run works" in `questions/Q1-concern-map.md`.

The evidence is only `concerns.tsv`, `inventory.tsv` and `statements.tsv` in `studies/concern-map/platforms/{shopify,salla,woocommerce}/`. Nothing else in the repository was read, and nothing from the web.

## Files

- `matches.tsv`: 88 match rows (M-001 to M-088). Each row gives the concern ids per platform, a verbatim `basis` with its source, `granularity`, and a `note` that starts with the basis kind.
- `unclear.tsv`: 84 candidates (U-001 to U-084), each with `why_unclear` and `what_would_settle_it`. When a concern in a candidate is already in a match row, `why_unclear` ends with "Already in match rows: …".
- `scripts/`:
  - `load.py`: reads the three files per platform.
  - `candidates.py`: generates candidate pairs.
  - `dossier.py`, `dossier_lite.py`, `compact.py`: write per-concern reading files.
  - `show.py`, `find.py`: look up statements, and where a quote appears.
  - `decisions.py`: the judged rows.
  - `build.py`: verifies the rows and writes the two tables and `work/stats.json`.
  - `crosscheck.py`: lists generated pairs that no row covers.
  - All scripts run with `python3 -I`.
- `work/`:
  - `candidates.tsv`: 1,870 scored pairs.
  - `phrase-index.tsv`: shared phrases and where each occurs.
  - `dossier-*.txt`: every concern with its terms, inventory and statements.
  - `crosscheck-leftovers.txt`: generated pairs that no row covers.
  - `stats.json`: the counts.

## How candidates were generated

`candidates.py` pairs every concern with every concern on the other two platforms. It uses three generators and records the evidence for each pair:

1. **Shared terms.** It normalises the concern name and its parts, the platform terms and the linked inventory entries. Normalising means lower case, no ®/™/footnote marks, punctuation removed and simple singulars. Pairs that share an exact phrase are scored at 1/(number of concerns holding the phrase). A looser key drops brand words (Shopify, Salla, سلة, WooCommerce, Woo, WC) and a trailing "app(s)", and scores at half weight.
2. **Identifier families.** It reduces each identifier to a resource noun:
   - webhook and event topics: `orders/create`, `order.created`, `woocommerce_…`, Salla's `store.branch.*`
   - access scopes: `read_x`, `write_x`, `customer_`/`unauthenticated_` variants and Salla's bare-noun scopes
   - API resources: `wc/v3 > orders` and Salla's API resource names

   Pairs that share a resource are scored at 1/(number of concerns holding it). Resources held by more than 25 concerns are ignored.
3. **Content-word similarity.** It computes TF-IDF cosine over the words of the name, terms and inventory entries. For each concern it keeps the top 4 on each other platform with a score of at least 0.12.

This gave 1,870 pairs:

- 496 share a normalised phrase.
- 37 share only a brand-stripped phrase.
- 349 share an identifier family.
- 1,306 have a TF-IDF score, and 1,096 of these come from TF-IDF alone.

The candidates were a guide, not the decision. Every concern on all three platforms was read in full in its dossier (terms, inventory entries, statements), and each row was judged by hand into `decisions.py`. As a check:

- 86 of the 88 match rows contain at least one generated pair. M-037 (payment processor) and M-070 (Shopify Functions / App Functions) were found by reading.
- 61 of the 84 unclear rows contain at least one generated pair. The others came from reading, and from searching the words of concerns that were left without a row.
- `crosscheck.py` lists generated pairs that score 0.45 or more and that no row covers. 67 remain (`work/crosscheck-leftovers.txt`). They were set aside because they share only generic words, country lists or identifiers that sit as items in another concern's lists. Examples: Salla's country reference data against Shopify's POS hardware (shared country names); App Functions against Webhooks (shared event names).

## How matches were judged

- **Same term.** The words that name the concern's subject are the same on each platform.
  - Brand words are set aside: "Shopify X", "Salla X" and "WooX" count as X. So are generic words such as "apps", "settings" and "management".
  - A qualifier that only narrows or brands the same head term is accepted and described in `granularity` or `note`. Examples: "EU VAT Number" against "VAT validation…" (M-041); "Shopify Functions" against "App Functions" (M-070).
  - When the head words differ, the pair is unclear even if the subject looks the same. Examples: abandoned checkouts and abandoned carts (U-001); collections and categories (U-002); discount codes and coupons (U-058).
- **Salla's terms.** Salla's English labels are used and its Arabic is quoted. Where Salla's only term is Arabic, a match was made only when a short literal translation gives the other platforms' term, and the row says so. Examples: M-029 رسوم المدفوعات الإلكترونية (e-payment fees); M-046 الاستلام من الفرع (pickup from the branch); M-088 نظام الحماية من الاحتيال (fraud protection system).
- **Identifier family.** The same resource in webhook topics, scopes or API resources. Example: M-019, where Shopify's `customer_groups/*` topics meet Salla's Customer Groups, while Shopify's own concern name is "Segments".
- **Definition.** Each platform's own statement defines the same thing, even though the terms differ. Examples: M-001 (contracting entity), M-026 (the platform's own payment service), M-035 (stored payment methods). The definitions are quoted in `basis`.
- **Bundles and splits.** A concern joins a row only when its headline subject carries the row's term. If it holds that subject only as one part, the pair is unclear. A part can be an inventory entry, a plan line or a Marketplace subcategory.
  - When platforms split a subject differently, all the pieces that carry the term sit in one row and `granularity` says how. 27 rows are one-to-many or many-to-many. Example: Shopify Capital has one concern per country (M-038).
  - App-store and Marketplace categories were matched only headline to headline.
- **One match row per concern.** If a concern could join two rows, it stays in the row of its headline term, and the other overlap becomes an unclear row.
- **Verification.** `build.py` checks every quote verbatim against the cited field: the concern name, its platform_terms, an inventory entry linked to that concern, or a statement of that concern with that cite id. It checks that every concern in a row is quoted. It also checks that no concern is in two match rows and that every row spans at least two platforms. The last build ran clean.
- **Basis kinds** (first words of each note):

  | Basis kind | Rows |
  |---|---|
  | term | 65 |
  | term + identifier | 11 |
  | term + definition | 8 |
  | definition | 3 |
  | identifier | 1 |

- **No choosing.** Nothing here says which platform's way is better or what Sharrwah should do.

## Counts

**Match rows: 88**

| Platforms spanned | Rows |
|---|---|
| All three | 34 |
| Shopify + Salla | 28 |
| Shopify + WooCommerce | 19 |
| Salla + WooCommerce | 7 |
| Two platforms, total | 54 |

**Unclear candidates: 84.** 52 involve all three platforms and 32 involve two.

**Concerns left on one platform only** (in no match row):

| Platform | Concerns | In a match row | Left on one platform only | of which in an unclear row | of which in no row at all |
|---|---|---|---|---|---|
| Shopify | 198 | 100 | 98 | 68 | 30 |
| Salla | 152 | 84 | 68 | 57 | 11 |
| WooCommerce | 118 | 71 | 47 | 35 | 12 |

A concern with no match is a finding. The concerns in no row at all, where no counterpart was found on either other platform, are:

- **Shopify (30):**
  - SH-C-027 Files
  - SH-C-038 Combined listings
  - SH-C-043 Customer marketing consent
  - SH-C-048 Checkout branding and configuration
  - SH-C-053 Cart transform
  - SH-C-073 Shopify Protect
  - SH-C-082 Shop Cash
  - SH-C-087 Cash management at POS
  - SH-C-088 Shopify Balance account
  - SH-C-089 Shopify Balance cards
  - SH-C-090 Shopify Credit
  - SH-C-098 Shopify Bill Pay
  - SH-C-112 Rollouts
  - SH-C-113 Backup region
  - SH-C-117 Shipping insurance
  - SH-C-122 Delivery customization
  - SH-C-123 Fulfillment constraints
  - SH-C-124 Delivery option generators
  - SH-C-128 Discount Functions
  - SH-C-144 POS UI extensions
  - SH-C-147 Shopify Network Intelligence
  - SH-C-159 Scopes that need Shopify's approval
  - SH-C-160 Protected customer data
  - SH-C-161 Mandatory privacy compliance webhooks
  - SH-C-165 Customer account UI extensions
  - SH-C-167 Custom apps developed in the admin
  - SH-C-176 Intellectual property reports
  - SH-C-179 Legal requests for information
  - SH-C-183 Retention and deletion of store data after closure
  - SH-C-201 Shopify Plus contract terms and renewals
- **Salla (11):**
  - SA-C-028 Product restrictions
  - SA-C-043 Order assignment to staff
  - SA-C-078 Reorder reminders
  - SA-C-080 Bank offers (عروض البنك)
  - SA-C-127 Charity stores' payment gateways
  - SA-C-149 Packaging
  - SA-C-150 Quality gateway for shipping complaints (بوابة الجودة)
  - SA-C-173 Salla's affiliate and referral programme terms
  - SA-C-174 App Maker publishing policy
  - SA-C-180 Policy at /policies/nd96 (content not reached)
  - SA-C-207 Report builder for apps
- **WooCommerce (12):**
  - WC-C-025 Core software licence and warranty
  - WC-C-033 Order storage tables (HPOS)
  - WC-C-035 Usage tracking sent to WooCommerce
  - WC-C-036 Remote logging to WooCommerce
  - WC-C-039 WooCommerce Analytics service
  - WC-C-049 WordPress.com / Jetpack connection
  - WC-C-081 Store administration home, setup wizard and onboarding
  - WC-C-083 Store status, tools and system report
  - WC-C-088 Feature settings
  - WC-C-094 Blueprint
  - WC-C-102 Memberships
  - WC-C-117 Store data synced to Automattic for Jetpack-connected services

## Patterns in why matches were unclear

Each unclear row was given one main reason. Many rows show more than one.

1. **Same subject, different words (27 rows).** The platforms name what looks like the same thing differently, and only function links them:
   - U-001 abandoned checkouts / abandoned carts
   - U-002 collections / categories
   - U-004 store credit / customer wallet
   - U-005 metafields / custom fields
   - U-018 drafts / manual orders
   - U-033 selling locations / Markets
   - U-058 discount codes / coupons
   - U-067 emails / notifications
   - U-069 site visibility / maintenance mode
   - U-073 shipments / fulfillments
2. **Sub-part overlaps (28 rows).** The shared term exists, but on at least one side it is only a part of a concern whose headline is something else, often a concern already matched on its headline. The part might be an inventory entry, a plan line, a feature flag or a Marketplace subcategory. Examples:
   - U-003 inventory transfer inside Salla's branches concern
   - U-024 local payment methods
   - U-029 Salla's VAT on its fees
   - U-054 "Sales channels" as a WooCommerce marketing subcategory
   - U-060 wishlists
   - U-082 donations
3. **Extension and app-category taxonomies cut differently (10 rows).** Shopify's App Store category groups, WooCommerce's Marketplace categories and subcategories, and Salla's app categories or core features divide the same ground differently:
   - U-013 search and navigation
   - U-052 Marketplace against App Store
   - U-059 upsell, bundles, pre-orders and options
   - U-063 SEO and store design
   - U-064 accounting and security
   - U-083 automation
4. **Brand-named products whose own definitions only partly align (4 rows):**
   - U-026 Shop Pay / WooPay / quick checkout
   - U-053 Shop / Mahally
   - U-055 Salla Ads / WooAds / Shopify Audiences
   - U-076 Managed Markets / Salla's merchant-of-record partners page
5. **A concern with no platform term or almost no statements (5 rows).** Mostly Salla concerns raised from the question's own list, where the output holds no Salla word for the subject:
   - U-027 who holds funds
   - U-028 settlement currency
   - U-035 sanctions
   - U-042 data residency
   - U-071 processor failure
6. **The same word naming different things (6 rows):**
   - U-034 supported countries
   - U-040 complaints
   - U-044 logs (audit logs against system logs)
   - U-045 rate limit
   - U-062 MCP / UCP and AI assistants
   - U-084 order limit
7. **A legal document as a concern on one platform and as a source on the others (4 rows):**
   - U-036 violations and acceptable use
   - U-037 terms of service
   - U-038 selling policy
   - U-039 licences and compliance

In the `what_would_settle_it` column:

- 59 rows ask only for a founder ruling.
- 6 put a specific question to the founder. Examples: U-029 asks whether Salla's VAT-on-fees statement counts against M-009; U-059 asks how far category groups should be matched.
- 19 name a statement or source that would settle the question or help.

Examples of those sources:

- a Shopify source on whether abandoned checkouts include carts left before checkout
- a WooAds statement defining the service
- a Shopify statement defining what order limit apps limit
- statements defining the web components on each side
