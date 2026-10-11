# Q1 concern map: WooCommerce (notes)

Run date 2026-10-10. Platform WooCommerce, id prefix WC. All six files are in this directory; working copies and the fetch log are in `fetched/`, scripts in `scripts/`.

## Files

| File | Rows |
| --- | --- |
| inventory.tsv | 654 entries (645 placed on concerns, 9 out of scope) |
| concerns.tsv | 118 concerns |
| placements.tsv | 590 placements (118 × 5): 467 shown, 123 not shown |
| citations.tsv | 963 citations (514 from the release, 449 from 102 web sources), each quote checked against its working copy |
| not-reached.tsv | 4 pages |

Shown or not shown, by placement: software 116/2, decides 114/4, legal 108/10, boundary 106/12, reason 23/95.

Following the coordinator's correction during the run, placement status takes only `shown` or `not shown`. No row says `historical`, and no source is discounted for its date. Every citation still carries `source_date` and `date_basis`. No cited source is dated before 2023.

## Sources

- **WooCommerce 11.2.1**, the release on WordPress.org, read as text from `/home/user/woocommerce-release/11.2.1/woocommerce/`. The zip's sha256 matched the brief (`5317434cb381b5fdc7c1dd6ee258324f08c390976aaf8d1199f2a0e9a3ab8586`). The release date, 2026-10-09, comes from the WordPress.org plugin record. No PHP or JS was executed. Python that read the release ran with `-I`.
- **Live pages**: 215 fetches of 132 URLs, all logged in `fetched/log.tsv` (123 with curl, 92 rendered with `method/capture/page_text.mjs`). Hosts: woocommerce.com (docs, legal and policy pages, Marketplace), raw.githubusercontent.com (developer docs, from developer.woocommerce.com/llms.txt), woocommerce.github.io (REST API reference), wordpress.org (plugin page), wordpress.com and en.support.wordpress.com (Terms of Service and support policies), automattic.com (Privacy Policy, Privacy Notice), jetpack.com (what Jetpack syncs).
- WebFetch and WebSearch were not used. URLs came from sitemaps, llms.txt indexes and links on pages already fetched.

## Lists used and their sizes

From the release (455 rows; each row cites the source line that names the entry):

| List | Rows | Where it comes from |
| --- | --- | --- |
| settings | 35 | 11 tabs from `WC_Admin_Settings::get_settings_pages()`; 24 sections from each tab's `get_own_sections()`, the Payments tab's section constants, and the two tax classes created on install |
| admin-navigation | 40 | `add_menu_page`/`add_submenu_page` and `wc_admin_register_page` calls, post type menu labels, Status page tabs |
| api-resources (release) | 178 | 10 namespaces; wc/v3 controllers (45); wc/v4 controllers (17, behind the `rest-api-v4` feature flag); Store API routes (34 in wc/store/v1, 1 in wc/private); wc-admin (24) and wc-analytics (42) controllers from `Admin/API/Init.php`; wccom-site/v3 (4); wc-telemetry (1) |
| webhook-topics | 17 | topic select in `html-webhooks-edit.php` |
| access-scopes | 9 | roles and capabilities in `WC_Install::create_roles()` and `get_core_capabilities()`; REST API key permissions |
| other:core-payment-gateways | 4 | `WC_Payment_Gateways` load list |
| other:core-shipping-methods | 9 | shipping method classes, including legacy methods and the Blocks pickup location |
| other:core-integrations | 1 | `WC_Integrations` load list (MaxMind) |
| other:emails | 23 | `WC_Emails::init()` |
| other:order-statuses | 8 | `wc_get_order_statuses()` and the Blocks draft status |
| other:features | 32 | `FeaturesController` definitions plus HPOS and COGS |
| other:privacy-exporters-erasers | 8 | `WC_Privacy` |
| other:payment-extension-suggestions | 46 | constants in `PaymentsExtensionSuggestions` (the Settings > Payments list) |
| other:shipping-partner-suggestions | 6 | `DefaultShippingPartners` |
| other:onboarding-tasks | 17 | `OnboardingTasks/Tasks/*::get_title()` |
| extension-points (release) | 22 | abstract classes, registration filters, Blocks and Store API PHP interfaces |

Live (199 rows):

| List | Rows | Where it comes from |
| --- | --- | --- |
| api-resources (REST API reference) | 33 | top-level navigation groups of woocommerce.github.io/woocommerce-rest-api-docs |
| extension-points (developer docs) | 28 | the 21 `block-development/extensible-blocks` docs and 7 `apis/store-api/extending-store-api` docs listed in developer.woocommerce.com/llms.txt (369 entries in all) |
| other:marketplace-categories | 79 | rendered category filters: 3 top sections, 9 extension categories, 57 subcategories, 10 business-services categories |
| other:woopayments-doc-topics | 16 | topic pages listed in the WooPayments documentation |
| other:plugin-page-features | 13 | feature lines and headings on wordpress.org/plugins/woocommerce |
| other:tos-woo-services | 5 | the "Woo services include" sentence in the Terms of Service |
| legal-agreements | 25 | footer legal links, policies the Terms and docs refer to, WooPayments-related terms, page-sitemap policy pages, the GPLv3 licence |

## Where the inventory stops

- Settings are taken to section level. Individual fields, such as currency position or guest checkout, are not inventory rows; some are cited inside placements. Sections built at run time are not listed one by one: one per integration, one per email, one per shipping method with settings, and one per extra tax class.
- REST controllers are listed for wc/v3 and wc/v4. wc/v1 (20 controllers) and wc/v2 (31 controllers) are earlier versions of the same resources and appear only as namespaces. Store API route patterns are kept verbatim, regexes included.
- Capabilities are listed as the platform groups them: three core capabilities, plus one row for the three capability types. Each type expands to 17 capabilities from a template; these are not listed separately.
- The 21 Blocks extensibility docs are one row each. The slot and filter names inside them are not expanded.
- Value lists are not inventoried: countries, states, currencies, locales and the 247-country payment suggestion map. They are used as evidence. The count of 247 country codes, with WooPayments listed for 38, comes from a script over the map.
- Marketplace: themes subcategories (12 of the 93 category URLs in the product-category sitemap) are not inventoried. Individual extensions are not inventoried either.
- woocommerce.com docs: 73 of the 3,715 document URLs in the docs sitemap were fetched: WooPayments, core settings, tax, shipping, privacy, Marketplace and connection docs. Extension vendors' own docs on woocommerce.com were not used as WooCommerce statements.
- Two concerns are not named by any entry in the lists, so they have no inventory rows: WC-C-034 (hosting) and WC-C-118 (EU VAT Number). Their split notes start "Not in the platform's lists:" and name the page each comes from.

Nine inventory rows are out of scope, each with a reason: trademark and brand guidelines, the code of conduct, the customer research agreement, three WooPayments promotion terms, the WooCommerce.com Cookie Policy, and a scalability claim on the plugin page.

## How values were assigned

- **WooPayments** is placed as a separate service delivered through an extension, not as WooCommerce core. Its parts are separate concerns where they sit in different places: processing, balance and payouts, reserves (decided by Stripe), KYC, country availability, restricted businesses, fees, merchant-set fraud rules, Radar screening (managed by the WooPayments team), disputes (started by the cardholder), in-person payments, PCI, and Stripe dependence.
- **Woo-made extensions** such as "Developed by Woo", EU VAT Number and WooCommerce Shipping are extensions or separate services. Their legal placement is a Woo entity.
- **"platform company"** is used for Automattic Inc. **"separate entity of the platform"** is used for WooCommerce, Inc. and WooCommerce Ireland Ltd., the Woo-services contracting entities named in the Terms of Service. It is also used where the Terms speak of the Automattic group collectively.
- **Core WooCommerce concerns** have legal placement "merchant". This cites the Terms naming WooCommerce among Woo services and making the merchant "solely responsible for all of your ecommerce activities". The core plugin itself is GPLv3 with no warranty (WC-C-025).
- Values that fit none of the listed placements use `other:` with the source's own words, e.g. Stripe's reserve decision and the 70% Marketplace revenue share.
- Where a value would rest only on inference, the placement is "not shown" and the note starts with "Inference:".

## Where sources disagree (both recorded)

- **WooPayments countries**: the WooPayments countries doc (updated 2026-09-25) lists 38. The 11.2.1 readme and plugin page name 10. The release's suggestion map lists WooPayments for the same 38 country codes as the doc (WC-C-010).
- **Tax calculation partner**: Jetpack's sync page says WooCommerce Tax calculations "are provided by TaxJar". The Terms give Taxamo as an example ("tax calculations may be provided by Taxamo") (WC-C-055).
- **Vetting of extensions**: the Terms say Third-Party Services "aren't vetted, endorsed, or controlled by Automattic". The readme says Woo's developers "vet each new extension" for the Marketplace (WC-C-059).
- **Requirements** (no placement depends on this): the release header requires WordPress 7.0 and PHP 7.4. The server recommendations doc lists WordPress 6.9 and PHP 8.3 for WooCommerce 10.8 and later.

## What could not be shown

- **Licence and holder of WooPayments funds.** No WooCommerce or Automattic source read names the licence, the licensed entity or the regulator under which WooPayments balances are held or moved (WC-C-020). The docs show the following:
  - payments go to a "WooPayments account balance" backed by a Stripe Express account;
  - Stripe sends payouts, applies reserves, and its Connected Account Agreement is accepted at signup;
  - Stripe Capital loans are issued by Celtic Bank.

  The Connected Account Agreement is Stripe's own document and was not read, because the brief limits sources to the platform's own material.
- **Where Woo services store data.** No server location is given for WooCommerce.com, WooPayments, WooCommerce Tax, WooCommerce Shipping or WooCommerce Analytics. The sources show only these points:
  - Jetpack syncs site data to "Automattic's servers";
  - EU and UK data may be accessed outside the EEA under standard contractual arrangements;
  - payment and shipping extensions send data to their providers, not to WooCommerce.com.
- **Hosting.** No source states who is legally responsible for hosting a self-hosted store (WC-C-034). Nor do the sources read say whether a data processing agreement is offered for self-hosted stores: the DPA page speaks of "WordPress.com site owners" (WC-C-044).
- **Partner failure.** The sources say what happens in only a few cases:
  - the WordPress.com connection is broken, so WooPayments cannot take payments until it is reconnected;
  - the merchant declines Stripe's updated terms, so WooPayments use ends and the balance is still paid out;
  - the Terms allow an alternative processor;
  - remote payment suggestions fail, so core falls back to bundled defaults;
  - an IP lookup service fails, so core tries the others in turn. This is shown only by the code, as a loop over the services.

  Nothing read says what happens when WooCommerce Tax, WooCommerce Shipping or a third-party gateway is unavailable, beyond reconnecting.
- **Sanctions screening of buyers in core.** None was found (WC-C-029). The Terms put sanctions compliance of the merchant's own transactions on the merchant. Automattic's own access restrictions are in Terms section 18, which lists Cuba, Crimea, Iran, North Korea, the Donetsk and Luhansk People's Republics, and Syria.
- **Stated reasons** are rare: 23 of 118 concerns. Most core features carry no reason for their placement.
- **Legal placement not shown** for: remote logging, mobile app, multi-currency, WooPayments payout currency, address autocomplete providers, Radar screening, reference data and the payment suggestion list.

## Problems with method

- **Bot check on wordpress.com.** The headless browser (`page_text.mjs`) gets a 403 "Checking your browser" page on wordpress.com and en.support.wordpress.com, while curl receives the pages with 200. The check was not worked around. Citations from these four pages are checked against the curl copy, and the pages are listed in not-reached.tsv for capture. woocommerce.com/terms-conditions/ redirects to wordpress.com/tos/, which is cited as the Terms of Service. Its "Last Updated: October 6, 2026" is the source date.
- **Quote checks.** For HTML pages, quotes are checked against the rendered text where a rendered copy exists. Otherwise they are checked against the served HTML with tags removed (block tags as line breaks, inline tags dropped) and entities decoded. Whitespace is folded. Release quotes are whole or partial source lines.
- **Live developer docs.** These are read from `trunk` on raw.githubusercontent.com, a moving target, and are dated as read (undated pages count as current on 2026-10-10). Marketplace category names come from rendered pages. The category pages build their filters with JavaScript, so curl copies do not contain them.
- **Some release lists depend on runtime state**, such as sections per tax class, integration or email, and emails or REST routes behind feature flags. The inventory takes what the code names statically and notes the flag.
- **Crawling rules and agent text.** robots.txt files were recorded: woocommerce.com disallows /wp-json/, /?s= and similar paths; developer.woocommerce.com allows all. llms.txt files were recorded: developer.woocommerce.com's lists the docs as raw GitHub markdown; woocommerce.com's (Yoast-generated) describes itself as "meant for consumption by LLMs". These were used only as indexes and did not limit the scope. No page text read tried to instruct agents.

## Re-pass, 11 October 2026

This section follows "Changed on 11 October 2026: the placement step" in `questions/Q1-concern-map.md`. The inventory (654 entries) and the 118 concerns stand unchanged. `placements.tsv` is kept as the first run's record; `statements.tsv` and `gaps.tsv` replace it. Scripts are in `q1r/woocommerce/scripts/`, working copies and `fetched/log.tsv` in `q1r/woocommerce/fetched/`.

### Sources used

- **WooCommerce 11.2.1**, read as text from `/home/user/woocommerce-release/11.2.1/woocommerce/`; no PHP or JS was executed, and Python that read it ran with `-I`. The structures read include: the setting arrays in `includes/admin/settings/` (ids, types, defaults); the gateway form fields in `includes/gateways/`; the admin page registrations and the capability each requires (`includes/admin/class-wc-admin-menus.php`, `src/Internal/Admin/*`, `src/Admin/PageController.php`); the post type capability types (`includes/class-wc-post-types.php`); roles and capabilities in `includes/class-wc-install.php`; the feature definitions in `src/Internal/Features/FeaturesController.php` (enabled_by_default, disable_ui, is_experimental, option_key); the per-country payment suggestion map in `src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php`; the shipping partner visibility rules in `src/Admin/Features/ShippingPartnerSuggestions/DefaultShippingPartners.php`; and hooks, REST routes and classes in the code paths of each concern.
- **The first run's captured pages** (`evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/`, 102 sources). New quotes from those pages (Terms of Service, privacy policy, WooPayments docs, PCI doc and others) are checked against that capture.
- **Pages read in the re-pass**: 29 curl fetches, logged in `fetched/log.tsv`: the four woocommerce.com documentation sitemaps (used only to find URLs), 22 candidate pages, and 3 more. 19 of them are cited and were captured in `q1r/woocommerce/fetched/capture/20261011T084016Z-q1r-woocommerce-more/` with `method/capture/run.sh`, `CAPTURE_LANG='en,ar;q=0.8'` and one worker (the capture's 38 requests are appended to the log). The cited new pages are: eight developer docs on raw.githubusercontent.com (Store API rate limiting, product customs data, customer review request, coming soon integration, enabling HPOS, data stores, GDPR guidelines for extensions, `wc com` CLI; the Cart and Checkout blocks README cited too is in the first run's capture); woocommerce.com docs on order withdrawal, HPOS, WooPay for merchants, WooPayments settings, Marketplace developers, the Mobile App support guide, WooCommerce Subscriptions (introduction and action reference), WooCommerce Bookings (introduction and REST API reference); and Automattic's AI Guidelines.
- **Follow-up (same day)**, for the 13 gaps of kind "page not read" that an agent could close: 43 more curl fetches (32 on woocommerce.com, 11 on kb.mailpoet.com), one render of the Memberships category page and 46 requests to the Marketplace search API, all logged in `fetched/log.tsv`. The 23 pages cited were captured in `q1r/woocommerce/fetched/capture/20261011T090749Z-q1r-woocommerce-more-2/` in the same way; that capture's 46 requests are appended to the log. See "Follow-up: Marketplace products and MailPoet" below.
- Fetched but not cited: `woocommerce.com/gdpr/` (linked from the privacy policy as "Woo and the GDPR") redirects to the woocommerce.com home page; the Cost of Goods doc describes a separate extension, not the core Cost of Goods Sold feature; the Back In Stock Notifications doc describes the plugin, not a core feature (the follow-up cites it for the Conversion category, WC-C-105); the Marketplace suggestions settings doc.
- WebFetch and WebSearch were not used.

### Counts

| File | Rows |
| --- | --- |
| inventory.tsv | 654 (unchanged) |
| concerns.tsv | 118 (unchanged; no concern added) |
| citations.tsv | 1,466: the first run's 963 plus 503 new (WC-S-5001 to WC-S-5503; 371 from the release, 132 from 63 web sources) |
| statements.tsv | 1,499: 987 reviewed candidates and 512 new statements (24 of them from the follow-up) |
| gaps.tsv | 182 |
| not-reached.tsv | 4 (unchanged; every page fetched in the re-pass answered curl with 200) |
| review-log.tsv | 501: 81 moves and 420 drops |
| placements.tsv | 590 (the first run's record, unchanged) |

Statements by placement: where 345, decides 502, responsible 107, boundary 502, reason 43. The decides count includes 273 statements quoting the per-country payment suggestion lists, one per country for all 247 countries in the map (23 long lists are quoted in two or more parts; lines that hold only pricing and terms links between the parts are not quoted).

Concern × placement cells (590): 408 have a statement, 182 have a gap.

| Placement | Cells with a statement | Gaps |
| --- | --- | --- |
| where | 108 | 10 |
| decides | 110 | 8 |
| responsible | 52 | 66 |
| boundary | 101 | 17 |
| reason | 37 | 81 |

### The review of the 1,407 candidates

- **Kept**: 906 as they were; **moved**: 81 (to decides 35, responsible 22, boundary 14, where 9, reason 1); **dropped**: 420. Every move and drop is in `review-log.tsv` with its reason and the candidate's row in `candidates.tsv`.
- **List-entry candidates (740)** were judged by their list; 137 were dropped. Lists that are location structures (settings tabs and sections, admin navigation, Marketplace categories, the emails in Settings > Emails, onboarding tasks, the core gateway and shipping method lists) keep their entries under where. Boundary structures (API resources, webhook topics, REST key permissions, extension points, privacy exporters and erasers) keep theirs under boundary; two base classes in `includes/gateways` were moved from where to boundary. Entries of lists that are neither, or that only name a thing, were dropped: feature names (63), payment suggestion id constants (47), shipping partner names (6), bare role and capability tokens (10) and order status values (10). The control those lists hold was then quoted directly as new decides statements (feature defaults, the per-country lists, the partners' country rules where held, the capability lines). One REST reference heading ("Introduction") was dropped.
- **First-run candidates (667)** were read one by one; 283 were dropped. The reasons: the Terms' general clauses on "Ecommerce Services" and "Third-Party Services" applied to concerns they do not name (122; each such cell is now a statement from a clause that names the concern, or a gap of kind "stated only in general terms"); the same quote kept under the placement it answers (77) or an exact duplicate (12); sentence fragments (20); bare names, ids, labels, headings and descriptions that answer no placement (52).
- Where a Terms clause names the concern's subject, it was kept or added: refunds, taxes, PCI DSS, sanctions, chargebacks, Store Guidelines, shipping and customs, WooPay, WooPayments, MailPoet. Its scope is recorded as stated, for example "Ecommerce Services (Terms 8.j)".
- No statement text was edited. Kept statements whose identifier was only a line locator (56) were given the platform's identifier: the hook, option id, class, feature id or readme section heading.

### New statements, by kind

- **Who decides**: setting definitions with their defaults (selling and shipping locations, currency, taxes, coupons, reviews, downloads, inventory, guest checkout, erasure, geolocation, address autocomplete, tracking, Marketplace suggestions, shipping calculator, logging defaults); the capability each admin page or action requires (WooCommerce menu `edit_others_shop_orders`, Settings and Status `manage_woocommerce`, Reports `view_woocommerce_reports`, Home `read`, Marketing `manage_woocommerce`, refunds `edit_shop_orders`, import and export `edit_products` with `import`/`export`, Blueprint import `manage_woocommerce` and `manage_options`); post type capability types (`product`, `shop_order`, `shop_coupon`); the core capabilities assigned at installation; feature flag defaults for 14 features, with the class's own statement that features 'can be enabled and disabled by admin users' and the values a definition gets when it sets none; the per-country payment suggestion lists and the store-state rule for Square; WooPayments and WooPay eligibility and fee rules from Woo's docs.
- **Who is responsible**: Terms clauses that name the concern (listed above), the PCI doc's "PCI DSS compliance is ultimately the responsibility of the store owner", the order withdrawal doc's "does not guarantee compliance", the DPA page's statement that a WordPress.com store owner acts as data controller (scope as stated), Woo's statements on Marketplace developers' and extension developers' obligations.
- **How it meets the rest**: hooks (for example `woocommerce_countries_allowed_countries`, `woocommerce_*_process_payment_order_status`, `woocommerce_product_import_pre_insert_product_object`, `woocommerce_order_save_attribution_data`, `woocommerce_shop_manager_editable_roles`, `woocommerce_store_api_rate_limit_options`), REST routes and schema fields (Blueprint export, MCP route, the Cost of Goods Sold product field), remote endpoints (the WooCommerce.com payment suggestion data source, the PayPal Standard WordPress.com proxy base), and the interfaces named in docs (dispute notifications, the Stripe Express dashboard, DPA request flow, AI providers).
- **Stated reasons**: 16 new, for example reserves protecting the processor, Store API rate limiting's purpose, the coming-soon cache header, POS capabilities granted per user, the Blueprint multisite rule, customs fields not calculating duties.
- **Follow-up**: 24 more statements from Woo-made products' docs in seven Marketplace categories and from MailPoet's knowledge base, listed under "Follow-up: Marketplace products and MailPoet" below.

### Gaps

By kind: searched, not found 106; stated only in general terms 63; page not read 9; observation needed 4.

| Kind | where | decides | responsible | boundary | reason |
| --- | --- | --- | --- | --- | --- |
| searched, not found | 7 | 4 | 1 | 14 | 80 |
| stated only in general terms | | 3 | 60 | | |
| page not read | 1 | 1 | 5 | 1 | 1 |
| observation needed | 2 | | | 2 | |

By who can close them: either 103 (all "searched, not found"); founder 79 (the 63 "stated only in general terms", which only the platform could settle; 9 "page not read" that turn on whether Stripe's own documents may be read as WooPayments' terms; 4 "observation needed"; 3 "searched, not found": two Marketplace categories whose products are all third-party, and MaxMind's licence); agent 0. The 13 agent gaps of the first version of this re-pass were closed in the follow-up: 11 now hold statements and 2 are "searched, not found".

- The 4 observations need a store with WooPayments: the onboarding journey (where and how a business's country is set and checked, WC-C-010), the payout and currency settings (WC-C-051) and the fraud protection settings with a Radar-blocked test payment (WC-C-115). The founder can set these up; they need a WordPress.com account.
- Stripe's Connected Account Agreement (stripe.com/connect-account/legal) is named in the gaps for WC-C-008, 009, 010, 020, 051 and 115. It is Stripe's document, accepted at WooPayments signup; whether it may be read as part of WooPayments' terms is for the founder.

### What could not be shown, and why

- **Legal responsibility for core features.** The Terms list WooCommerce among the Woo services and make the user "solely responsible for all of your ecommerce activities", and the core plugin is GPLv3 with no warranty, but no term, policy or doc read names most core concerns (products, orders, coupons, emails, APIs, roles, analytics and others). Applying the general clauses to each concern would be inference, so these are gaps of kind "stated only in general terms" (60 under responsible).
- **The licence and licensed holder of WooPayments funds** (WC-C-020): still not shown; see the Stripe agreement above.
- **Stated reasons** are rare. A search of the captured and fetched pages and the code comments for reason sentences found 16 new ones, and the follow-up 2 more; 81 reason cells remain gaps.
- **Marketplace categories** (WC-C-100 to WC-C-112): where is answered by the category name. Woo's documentation of Woo-made products answers some cells for those products only, with the product recorded as scope: WooCommerce Subscriptions and WooCommerce Bookings in the main pass, and one or two products in each of seven more categories in the follow-up. Memberships (WC-C-102) and International and localization (WC-C-108) list no Woo-made product, so their boundary cells are "searched, not found". Who is legally responsible stays "stated only in general terms" for every category.
- **Where data lives** for Woo services: as in the first run, no server location is given for WooCommerce.com, WooPayments, WooCommerce Tax, WooCommerce Shipping or WooCommerce Analytics. The re-pass adds that WooCommerce Analytics in core says "All data stays within your store" (feature description) and that order attribution stores no data unless an order is placed. The follow-up adds MailPoet: account data of MailPoet users who send with it or buy a plan is collected "on our servers in the United States of America" (WC-C-113, scope as stated). The same MailPoet page lists the third-party services that process subscriber data, with their locations; that table is not quoted.

### Sources that disagree (new)

- WooCommerce Shipping: the privacy-shipping doc says it needs Jetpack "to connect with other services and provide live shipping rates" (WC-S-0567); the WooCommerce Shipping doc says "It does not provide live shipping rates at checkout" (WC-S-0906). Both are recorded.
- WooPayments countries: the per-country suggestion map in the release lists WooPayments for the same 38 country codes as the WooPayments countries doc; the readme still names 10 (first-run finding, kept).

### Follow-up: Marketplace products and MailPoet

- **Finding the products.** The Marketplace category pages build their product grids with JavaScript; the captured copies, and a new render of the Memberships page, show "No extensions found". The products in each category were listed from the Marketplace's own search API, the one the release's Extensions screen calls (`assets/client/admin/app/index.js` names `https://woocommerce.com/wp-json/wccom-extensions/1.0/search`). Each category's listing was compared with the listing for "Developed by Woo" (63 products). The API was used only to find products and is not cited. A product counts as Woo-made when its Marketplace page lists it in "Developed by Woo"; vendors' own docs are still not used, as in the first run.
- **What the listings hold.** Memberships (11 products) and International and localization (18) list no Woo-made product. Business services (17) lists one with Woo as vendor, Woo Agency Partners. The other categories list several Woo-made products each, for example 12 in Conversion and 15 in Marketing.
- **Statements added (24).** Each statement about a product has the product as scope. Its second citation is the product's Marketplace page, quoting the "Categories" list, which shows the category and "Developed by Woo"; for Woo Agency Partners it quotes the breadcrumb and the heading "Woo Agency Partners by Woo".
  - WC-C-103 B2B, WooCommerce Purchase Order Gateway: the `_po_number` order meta key (boundary); disabling the gateway in its settings (decides).
  - WC-C-104 Merchandising, Product Bundles: the `bundled_by` and `bundled_items` properties it adds to the `/products/` and `/orders/` REST responses (boundary).
  - WC-C-105 Conversion: Back In Stock Notifications queues its e-mails with Action Scheduler (boundary), and sign-ups need out-of-stock products to stay visible (decides); WooCommerce Points and Rewards' `wc_points_rewards_action_settings` filter (boundary).
  - WC-C-106 Customer service, Advanced Notifications: the order status transitions it uses, such as `pending_to_processing` (boundary); triggers decide which products and orders notify (decides).
  - WC-C-107 Store content and customizations, Checkout Field Editor: it works with the legacy checkout only (boundary), and the page gives the reason, that the block checkout will include native field customization (reason); field names are the meta keys (boundary); required address fields follow the locale, not the settings (decides).
  - WC-C-109 Store management, Xero: the connection through an OAuth 2.0 app (boundary); the Send Invoices setting (decides).
  - WC-C-110 Marketing, Google for WooCommerce: product data synced to Google Merchant Center (boundary); products missing required fields are not synced (decides).
  - WC-C-112 Business services, Woo Agency Partners: the merchant contacts an agency through its own website (boundary); partners pass Woo's review (decides).
  - WC-C-113 MailPoet, from MailPoet's knowledge base (MailPoet is named among the Woo services in the Terms, WC-S-0458): free use up to 500 subscribers, and WooCommerce customers' subscriber status set in MailPoet > Settings > WooCommerce (decides); the WooCommerce Customers list and the `mailpoet_subscription_before_subscribe` action (boundary); the reason given for not sending from one's own host (reason); where account data is kept (where, added because "where data lives" is one of the question's architecture concerns).
- **Decides and reason.** Where a page read for a boundary cell also states a product setting or a reason, that statement was added too, as for Subscriptions and Bookings in the main pass. This closed 7 decides gaps and 1 reason gap. The Product Bundles REST reference states no setting, so Merchandising's decides cell stays "stated only in general terms".
- **Read but not cited.** One or two products answer each cell; other pages of the same kind were read and not cited: the Product Add-Ons, Gift Cards and Composite Products REST references, the Bundles actions reference, EU VAT Number developer snippets, AutomateWoo custom triggers, One Page Checkout, Product CSV Import Suite, Order Barcodes, Product Vendors, Pinterest for WooCommerce, Xero invoice customization; the product pages of AutomateWoo, Order Barcodes, MailPoet and EU VAT Number; MailPoet's articles on the 500-subscriber limit, the Sending Service and its acquisition by WooCommerce.

### Problems with method

- **Inventory not extended.** The release names structures outside the lists the first run used (REST controllers registered outside `Server.php`, such as the WooPayments onboarding, Payments settings, push notifications, order actions, receipt rendering, email editor and POS catalog routes; newer modules such as customer email verification, abilities, product feed). Each belongs to an existing concern, so no concern was added; some are cited as statements.
- **Whitespace.** Release quotes fold runs of whitespace to one space, as in the first run; the checker folds whitespace the same way.
- **One quote contains "…"** (WC-S-5436): the character is in the source's own comment, not an elision. The checker warns on it.
- **review-log.tsv** carries one column beyond those asked for, `candidate_row`, the row of the candidate in `candidates.tsv`.
- **Live developer docs** are read from `trunk` and dated as read (2026-10-11).
- Inference: the per-country suggestion lists set what the Settings > Payments page suggests; whether a suggested provider is available to a store is stated only by each provider's own pages, which were not read.
- **The Marketplace search API and robots.txt.** woocommerce.com's robots.txt disallows `/wp-json/`. As the brief says, this was recorded and did not limit the scope. The API was called at about one request per 1.2 seconds (46 requests).
- **kb.mailpoet.com and the browser.** The knowledge base answered curl with 200 and the full article, and the headless browser with a 403 "Checking your browser" page. The check was not worked around. The six MailPoet citations are checked against the raw HTML in the capture. The pages show no date; their dates are the `lastmod` values in the site's own sitemap.
- **Category lists on product pages.** The order of the "Categories" list differs from one product page to another; quotes are as captured.
- **Capture pace.** With one worker, the capture tool's raw phase sends its requests back to back. The first re-pass capture made 19 requests in about 5 seconds; the follow-up capture made 23 in about 6 seconds, 17 of them to woocommerce.com in about 4 seconds. That is faster than the brief's one request per second per host. The render phase ran at about one page every 4 seconds.
- **A page changed between reading and capture.** Google for WooCommerce's product page showed dateModified 2026-10-10 when read and 2026-10-11T09:06:52Z when captured; the captured date is recorded.
