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
