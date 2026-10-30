# Inspection of the held pass: its brief, selection, entries, batches and scripts (30 October 2026)

**What this is:** an inspection, before it runs, of the held pass (`PLAN.md`, Stage 4A): `briefs/H-held.md`; the coordinator's selection `held/selection.tsv` (237 rows); the entries `held/<platform>/entries.tsv` (14,889) built by `method/held_entries.py build`; `held/batches.tsv` (22 batches); and the scripts `method/held_entries.py` and `method/held_vs_read.py`. The inspector wrote none of them and changed no file except this one.
- Commands ran from the repository's root at `ab8d98ff`. The branch moved to `1d213be6` while the inspection ran. `git diff --stat ab8d98ff 1d213be6` touches none of the files above. It adds `method/held_amend.py`, the coordinator's converter from placements to evidence, which B-4, B-6 and C-2 read because it shows what will be done with the output.
- The evidence was read at observed-sh `19a5f6435`, observed-sa `b0bd0b16` and other-product-class `0d79b79`, through their guides first. The WooCommerce release was read at `/home/user/woocommerce-release/11.2.1/woocommerce`.
- Tests that write ran on copies of `studies/class-model/` in the scratchpad, with `CLASS_MODEL_DIR` set.

Severity: **must fix** means an agent following the brief would write wrong placements, or the selection or the build loses evidence. **Should fix** means the output would be less consistent, harder to check, or more expensive than it needs to be. **Note** is for the record.

**In short:** 16 must fix, 21 should fix, 9 notes.
- **The selection** misses four sets of the platforms' own lists: Flow's triggers and actions, Salla's published plans, the `doc` rows, and WooCommerce's release.
- **The build** loses items of selected structures in five ways:
  - a rule that matches nothing (Shopify's 386 plan-requirement notes);
  - a words filter;
  - nested lists and clipping;
  - dropped keys that merge different items;
  - one mispaired BigCommerce table.

  Its entry ids are positions, so every fix renumbers them.
- **The brief's** own list of `supports` departs from `B-extent.md`'s rules, its sub-page rule contradicts `new`, and its "always out" kinds contradict the selection.
- **The checker** passes what the brief forbids.
- **The batches** are about three times the size that keeps a context under 200,000 tokens.

---

## Part 1. The selection (`held/selection.tsv`)

### Must fix

**S-1. Shopify Flow's own catalog of triggers and actions counts as read, and is never selected.**
- *Found:*
  - `shopify/flow-connectors` has no row in `selection.tsv`. `held_entries.py registers --platform shopify` gives it `read 1, items 8, cited 8`, so it looks wholly read.
  - Its 8 citations (`grep "structures/shopify/flow-connectors" studies/concern-map/platforms/shopify/citations.tsv`) quote only each connector's name: `"name": "Shopify"`, `"name": "Flow"`, `"name": "Shop"`, `"name": "Slack"` and the like.
  - The three lines of `structures/shopify/flow-connectors/capture-plus@installed/items.jsonl` (one answer of 170,783 bytes) nest the connectors' tasks. The connector "Shopify" holds `triggerTasks` 82, `actionTasks` 100 and `taskCategories` 15. With Flow's and Shop's, they hold 85 triggers and 108 actions, such as:
    - triggers: "Order created", "Product created", "Fulfillment order split";
    - actions: "Send HTTP request", "Purchase shipping label", "Hold fulfillment order".
  - The read mark is per line (`held_entries.py`, lines 200 to 206; `held_vs_read.py`, line 189). So 193 tasks count as read because the line that names their connector is cited.
  - `flow-templates` is left because its recipes run "over Flow's triggers and actions, which the concern map read through its connectors" (`selection.tsv`, line 99). The concern map didn't read them. It read the connectors' names.
  - **What mitigates it, measured:** 79 of the 85 trigger labels appear in some held entry, mostly Help Center titles under `/manual/shopify-flow/reference/`, which the brief makes `shows` (line 36). 4 appear in the concern map's citations. The platform's own API list, which would support `core`, is read nowhere.
- *Fix:*
  - Add the row `shopify	flow-connectors	yes	nested:triggerTasks,conditionTasks,actionTasks,forEachTasks,waitTasks	Flow's own triggers and actions, nested in each connector: the concern map cited the connectors' names only`.
  - Add a `nested:<key>,…` rule to `items_of`: one item per element of each named list, carrying its connector's `name` and the list's key.
  - Change `flow-templates`' reason to "recipes over the triggers and actions that flow-connectors lists".
  - In both scripts, a cited line reads its nested lists only where the citation's quote or locator names them.

**S-2. Salla's published plans are held but were never registered for selection.**
- *Found:*
  - `structures/salla/com-plans` holds `salla.com/plans` per market and language as `text.txt`, "the page's text nodes in document order, one per line" (its `meta.json`). It has 407 lines in en-sa, 423 in ar-sa, 385 in en-ae and 389 in ar-ae.
  - Example, en-sa lines 100 to 113: "Key features / Unlimited products / Unlimited orders / Lower shipping costs with Salla Shipping Labels / … / Built-in VAT support with ZATCA integration". The plan cards (Basic Free, Plus SAR 990 / year, Pro SAR 2,990 / year) and each plan's lines follow.
  - The concern map cites 44 of its 1,604 lines (ar-sa 27, ar-ae 16, en-sa 1, en-ae 0). `com-specialplan` (306 lines per locale, 1,224 in all) has 16 citations.
  - Neither has a row. `held_vs_read.py` counts a structure's items from `items.jsonl` only (lines 179 to 183), so both show "items 0". A `text.txt` structure can't be built into entries (`items_of`, lines 121 to 165).
  - A plan line is one of the four places of their own (`B-extent.md` at `ab8d98ff`, line 131). Salla's other plan statements are few: `merchant-plans` (2 lines, both cited) and the plans named inside `dashboard-features`.
- *Fix:*
  - Add `salla	com-plans	yes	text:	Salla's published plans per market and language: plan cards and each plan's lines, the 44 cited lines aside`, and the same row for `com-specialplan`.
  - Add a `text:` rule to `items_of`: one item per non-empty line of each `text.txt`, with its label and its line, deduplicated like the others.
  - In `held_vs_read.py`, count the lines of `text.txt`, `pages.jsonl`, `listings.jsonl` and `menu.jsonl` as items too (S-12).

**S-3. The `doc` structures have no reader.**
- *Found:*
  - 15 rows are `doc`, "read whole as documents":
    - Shopify `plan-feature-set`, `sidekick-quotas`, `flow-workflow-limits` and `status-page`;
    - Salla `kyc-schema`, `onboarding-missions`, `onboarding-status`, `portal-apps-iframe-pages`, `importer-schemas`, `salla-complaints`, `salla-academy` and `theme-marketplace-summary`;
    - Zid `plans-offered` and `store-feature-flags`;
    - BigCommerce `standard-formats`.
  - `build` takes only `read == "yes"` (`held_entries.py`, line 175). `batches.tsv` has no batch for them, and the brief never mentions `doc` (`grep -n doc` finds only `docs/READING.md`). So no agent reads them, and `check` can't take a placement for them.
  - Among them are plan lines and features:
    - Shopify's plan × feature data as the admin asks for it (`PlanFeatureSetQuery`, held in many runs' `answers/`, 120 to 172 kB a run);
    - Zid's plans offered, with prices and advantages (a 20 kB answer);
    - Zid's store feature flags.
- *Fix:* build them into entries like the others, or give them a batch.
  - **As entries:** Zid `plans-offered` gives one entry per package and per advantage, `store-feature-flags` one per flag, and Shopify `plan-feature-set` one per section and feature, from one answer per plan.
  - **As a batch,** add to the brief: "**A `doc` structure** (the selection's `doc` rows) is read whole, in a batch of its own (`<PREFIX>-doc` in `batches.tsv`). Write a line per thing it states (a plan, a plan's line, a flag, a step, a limit). Its `entry_id` is `doc:<structure>:<file>#<JSON pointer or line>`, with the same columns." Then let `check --batch <PREFIX>-doc` accept `doc:` ids of that platform's `doc` rows.
  - BigCommerce `standard-formats` is deferred by its own reason (line 16) to Q3's M-04 and the cells pass: mark it `no` with that reason.

**S-4. WooCommerce's own lists in its release were never registered for selection.**
- *Found:*
  - WooCommerce's register (`woocommerce/structures/REGISTER.tsv`) holds 7 structures. Two of them are read from code (`woopayments-supported-countries`, `countries-states`).
  - The release holds WooCommerce's own lists of its places, permissions and events, and none is a structure or a selection row:
    - the settings tabs and their fields, `includes/admin/settings/class-wc-settings-*.php`: about 174 settings ids (`grep -c "'id' *=>"`: advanced 39, products 38, general 29, emails 28, accounts 24, shipping 7, point of sale 7);
    - the admin menus, `includes/admin/class-wc-admin-menus.php` (`add_submenu_page`: Attributes, Reports, Settings, Status, Extensions);
    - the core capabilities, `includes/class-wc-install.php`, `get_core_capabilities()` (line 2414);
    - the webhook topics, `includes/class-wc-webhook.php` from line 1020 (`'order.created' => …`);
    - the REST API's controllers, `includes/rest-api/Server.php` from line 103;
    - the features, `src/Internal/Features/FeaturesController.php`.
  - The concern map read these files in part (`cut -f2 citations.tsv`). The twelve settings classes have 64 citations between them, and `class-wc-settings-checkout.php` none. `class-wc-webhook.php` has 1 citation, at line 366, not the topics. `class-wc-install.php` has 13, `Server.php` 68 and `FeaturesController.php` 55.
  - WooCommerce has 160 of its 347 cells holding nothing (`merged/cells.tsv`), second only to BigCommerce's 175.
- *Fix:*
  - Add a row per list, built by a script that reads the release's PHP arrays: `release-settings` (one entry per settings field: tab, section, id, title, description), `release-admin-menus`, `release-capabilities`, `release-webhook-topics`, `release-rest-controllers` and `release-features`.
  - Each entry cites `woocommerce-11.2.1:<path>`, `line N`, as the concern map does. Its kind is `shipped` (`PLAN.md`, section 6).
  - The lines the concern map cites count as read.

### Should fix

**S-5. The developer docs' navigation is neither selected nor read, though the reasons for leaving the API's own pages rest on it.**
- *Found:*
  - Shopify `docs-front-matter` and `admin-graphql-schema` are left because "its groups are read through the reference navigation" (`selection.tsv`, lines 42 and 43).
    - For the GraphQL Admin API that holds: `admin-graphql-reference-nav` has 28 of 28 items cited.
    - For the other APIs, the groups are in `dev-docs-nav`, each docs area's own sidebar: the REST Admin API ("navItems: 21 items"), App Events, Admin Extensions, Checkout UI extensions, App home and others.
    - `dev-docs-nav` has no row, and 41 of its 48 items are uncited (`registers`: items 48, cited 7). Its lists are nested, so E-3 applies to it too.
  - Salla `docs-index` and `docs-sidebar` are left because "the groups [are] read through the docs' navigation" (lines 203 and 204).
    - `docs-navigation` has no row, and 28 of its 56 items are uncited. It holds the top menu: "Merchant", then its folders.
    - The API's groups are `docs-sidebar`'s folders (`type: apiDetailFolder` and `folder`; `merchant-api@20261009T033553Z` alone has 337 items).
- *Fix:*
  - Add these rows:
    - `shopify	dev-docs-nav	yes	nested:navItems	the docs areas' own sidebars: every API's groups; the items not cited`;
    - `salla	docs-navigation	yes		the developer docs' menu; the items not cited`;
    - `salla	docs-sidebar	yes	where:type=apiDetailFolder|folder	the API's groups, one per folder`, with E-1's `|` in `where:`.
  - Change the four reasons to name the structure that holds the groups.

**S-6. More structures are half read and absent, and two rules are applied two ways.**
- *Found:*
  - **Absent and half read:** Shopify `shopify-com-header-nav` has 31 of 59 items uncited ("Built into every store", "World's best checkout", "Sidekick", "Products / Build your website / Sell anywhere / Marketing & analytics"). Salla `portal-help-center-article` has 6 of 13 uncited.
  - **A reason that doesn't hold:** Shopify `shopify-cli-commands` (133 commands, 16 topics) is left as "developer tooling" (line 106). `B-extent.md`, "The scope part", puts "developer tooling and partners" in domain F.
  - **Third parties, two ways:** `tracking-carriers` (204 carriers) is left as slot fillers for the cells pass (line 91). Salla `shipping-carriers`, BigCommerce `payment-gateways` and `tax-services`, and Salla `marketplace-apps` (815 apps), all third parties, are read entry by entry.
  - **Help titles, two ways:** Salla `help-articles` (2,938 titles with short descriptions) is left for the cells pass (line 187). Shopify `help-section-children` (2,317 entries of the same kind, help pages' titles) is read entry by entry (line 39).
- *Fix:*
  - Add the two half-read structures, `yes`, "the items not cited". Make `shopify-cli-commands` `yes` for its topics and commands.
  - Choose one rule for lists of third parties and one for help titles, apply each to all five platforms, and state it in the reasons:
    - for third parties: "read entry by entry where the list states what the platform connects through an interface of its own; left as slot fillers otherwise";
    - for help titles: "read entry by entry on every platform, or on none".

**S-7. Two reasons presuppose a maker.**
- *Found:*
  - **Salla `shipping-carriers`:** its reason is "the shipping companies a store is offered, Salla's own among them" (line 160).
    - All 25 of its entries carry `type: salla`: Aramex, Smsa, Dhl, Aymakan, Redbox and the rest (`show --structure shipping-carriers`).
    - One carrier's name carries Salla's brand: "سلة - جي اند تي اكسبريس".
    - `B-extent.md` (line 115): "A product's name that carries the platform's brand doesn't name its maker."
  - **Shopify `play-publisher-apps`:** its reason is "Shopify's own Android apps" (line 58).
    - The entries say "desc: Expand content for Shopify Inbox" and the like.
    - The publisher appears only in the capture's label `google-play@pub-shopify-inc`, and in the search query `pub:Shopify Inc.` that the capture typed.
    - `structures/README.md`: labels are "This capture's names for finding things. They are not platform terms."
  - The brief sends the agent to these reasons (line 22), so they steer it to `own-service`.
- *Fix:*
  - Change the two reasons to "the shipping companies a store is offered" and "the Android apps Google Play lists for the publisher query pub:Shopify Inc.".
  - Add to the brief: "A field's value such as `type: salla`, a brand in a product's name, and a capture's label never name a maker."

**S-8. Some `yes` rows are one account's records, one store's, or samples.**
- *Found:* the brief's own rule makes these `out` (line 40):
  - Salla `portal-app-snippets` ("name: dkdf; slug: dkdf; … url: …/snippets/dev/1080110626/831871776.js");
  - Salla `portal-apps-onboarding-steps` ("title: خطوة1");
  - Salla `storefront-api` (15 entries: the demo store's branches and categories);
  - Salla `dashboard-account-actions` ("text: Mushammir");
  - much of Salla `storefront-init` (38 entries: the store's and a guest's values).
- *Fix:* mark them `no`, with "one account's records" or "a sample", and keep `storefront-init` only for the keys that name settings (a `where:` rule).

**S-9. The repositories' derived tables of gates and links are never read.**
- *Found:*
  - `derived/` holds no structures, so the selection never saw it.
  - observed-sa's `docs/READING.md` (line 122) lists `derived/plan-gates.tsv`, `permission-gates.tsv` and `state-gates.tsv` (285, 331 and 348 lines): "What a plan, a permission or a store's state allows, in Salla's words, beside what each store's pages showed".
  - observed-sh's `README.md` lists:
    - `derived/eligibility-by-store.tsv`, each route's stated features and entitlements beside each store's values (11,419 lines);
    - `derived/help-admin-links.tsv`, the Help Center's admin addresses with the routes they reach (4,705 lines);
    - `derived/journey-catalog.jsonl`, the admin's units of work (311 lines).
  - No citation of the concern map names `derived/` (`grep -c "derived/"` gives 0 for Shopify and Salla).
- *Fix:*
  - Read `plan-gates.tsv` and `permission-gates.tsv` as entries, one per row: the address, the feature, the plans or the permission.
  - Use `eligibility-by-store.tsv` and `help-admin-links.tsv` as indexes for the second stage (U-1).
  - They are tables the repository rebuilt from bytes it holds: where a placement rests on one, cite the bytes it names.

**S-10. A later router version's changed routes are left out.**
- *Found:*
  - `admin-router-versions` keeps the items whose id the read version lacks (`new-vs:admin-router`, line 26): 11 entries.
  - `derived/admin-router-changes/router-577b0ff35365..router-dd413330f40a.jsonl` gives 11 routes added, 69 changed (apart from rebuilt file names) and 1 removed.
  - A change of eligibility, such as a beta gate added or dropped, can change a route's placement under the brief's flag rule.
- *Fix:* add the 69 changed routes and the 1 removed as entries, rendered from that file's `before` and `after`, so the agent sees what changed.

### Notes

**S-11. Reasons tested that hold.**
- **`admin-route-titles-en`:** of 650 routes without a static title in the manifest, 1 has a title in the titles file. Its other keys name routes that carry their own titles.
- **`admin-betas`:** all 280 names in both labels are 8-hex hashes. The structure still states which betas are on for each store. That tells an agent whether a beta-gated route is on, a lead for B-1's flag rule.
- **`app-store-taxonomy`:** it has no row, but the concern map cites all 161 category pages' lines, each by its `h1`. Its 2,612 category-feature pages are filters.
- **The fully cited structures absent from the selection** are read item by item, apart from S-1's: `cli-webhook-topics` (230 of 230), `admin-webhook-topics` (99 of 99), `staff-permission-groups` (217 citations for 16 lines), `merchant-plans` (206 citations for 2 lines).
- **The market data rows** (`localization-countries`, `countries-states`, `signup-countries` and the others) are left with reasons that hold.

**S-12. The measure's blind spot.**
- `held_vs_read.py` counts items from `items.jsonl` only (lines 179 to 183), and counts a structure as held only where its status starts with `captured` or `held` (line 177).
- Structures whose items are in `pages.jsonl`, `menu.jsonl`, `listings.jsonl`, `text.txt` or `source.json` show "items 0". That is how S-2 was missed.
- The register's rows that aren't held are left rightly: Shopify's 5 `not held` and 2 `backlogged`, and Zid's `dashboard-api-resources` (backlogged, 1,437 calls counted). Zid's is a lead for the second stage (U-1).

---

## Part 2. The entries (`held_entries.py build`)

### Must fix

**E-1. The help-notes rule matches nothing, so Shopify's plan-requirement notes are lost.**
- *Found:*
  - The rule is `where:class=note-plan` (`selection.tsv`, line 40). The notes' class is `note note-plan`: 193 in English and 193 in Arabic (`structures/shopify/help-notes/*/items.jsonl`).
  - So the exact comparison (`held_entries.py`, line 194) keeps none of the 7,870 notes, and `build` says nothing.
  - Rebuilt on a scratch copy with `where:class=note note-plan`, the structure gives 374 entries.
  - The 193 English notes sit on 176 pages, of which the model read 6. Example: "Plan requirement Generating apps with Sidekick is available only to stores on the Grow plan, Advanced plan, and Shopify Plus plan."
  - Two other classes state what the model needs: `note note-staff-permissions` (45 notes on 39 pages, 3 of them read) states permissions, and `note note-beta` (69 notes on 66 pages, 2 read) states release markers.
- *Fix:*
  - Let `where:` take `|`-separated values, and keep `note note-plan|note note-staff-permissions|note note-beta`.
  - Read the English notes, and the Arabic ones only where a page has no English twin (K-3).

**E-2. The words filter drops whole items of selected structures.**
- *Found:* `build` keeps a rendering only where it starts with a key of `WORDS`, or holds `; <key>:` for one (lines 44 to 46 and 209). Items whose keys aren't in that list, or whose words sit inside a nested dict, are dropped as "nothing to place". The counts come from a re-run of `build`'s steps per structure ("What I ran", item 2):

  | Structure | Renderings | Dropped | What is lost |
  | --- | --- | --- | --- |
  | BigCommerce `contracting-entities` | 5 | 5 | every row: "Country of Residence of Merchant: United States; Commerce Entity: Commerce.com US, Inc. …" |
  | Shopify `billing-subscription-downgrades` | 4 | 4 | `internalName: DORMANT; isDowngrade.monthly: false …` |
  | Salla `dashboard-nav-segments` | 157 | 157 | each segment's sub-navigation: `segment: apps; urls: [/apps, /apps/installed, /apps/settings]; labels_en: [App Store, My apps, Settings]` |
  | Shopify `partners-dashboard-routes` | 246 | 118 | the source maps' routes with their element names: `props: {path: /organizations}; element: Organizations` |
  | Salla `portal-menu-definitions` | 218 | 160 | menu items with their routes, permissions and feature gates, nested in `props` |
  | Salla `docs-event-lists` | 231 | 108 | list rows whose text is in `item`, which `SKIP` drops too (E-4), and table rows in `cells` |

  Three of the four `yes` structures with no entries at all are in this table, and E-1 is the fourth. Shopify `admin-roles` and `plan-comparison-admin` also give none, rightly: their items are read.
- *Fix:*
  - Drop the `WORDS` test. Drop instead a rendering that is empty, or made only of layout keys (`role`, `kind`, `tag`, `type`, `class`, and `id` where it is opaque).
  - Render a nested dict's words (`props.title`, `cells.*`) into the text.
  - Take `item` and `headings` out of `SKIP` (E-4).

**E-3. Nested lists and the 600-character clip hide the entries inside an item.**
- *Found:* `render` shows a list of dicts below the top level as "N items". It shows the first 12 elements of a top-level list, clipped to 300 characters, and clips the whole to 600 (lines 79 to 87). Where one item holds a list of the platform's things, those things never reach an entry:
  - **WooCommerce `core-profiler-free-extensions`:** 7 entries, one per country, each "bundles: [key: obw/basics; title: Get the basics; plugins: 3 items | …]". None holds the 124 plugin listings (WooPayments, WooCommerce Shipping, Jetpack, Google for WooCommerce, Pinterest, MailPoet, Klaviyo, Mailchimp, WooCommerce Tax, Snapchat Ads, Reddit Ads and others).
  - **WooCommerce `payments-providers`:** 8 entries, one per location, all clipped at 600. They cut each location's providers (3 or 4), offline methods (3) and suggestions (0 to 9: Stripe, Square, Mollie, Airwallex, Paymob, Payoneer, N-Genius, KOMOJU, Elavon and others).
  - **WooCommerce `woopayments-onboarding`:** 5 entries, all clipped.
  - **Salla `dashboard-nav`:** 7 entries for menus of 23.9 kB, such as "children: [url: /marketing/ads/v2/dashboard; title: Salla Ads; feature: salla-ads | … …]". 232 of its 291 distinct strings reach no entry.
  - **Salla `help-embedded-tree`:** 10 entries for 619 kB, 5 sections per language. 3,359 of its 3,436 strings reach no entry.
  - **Salla `report-widgets` (124 widgets) and `report-widgets-legacy` (20):** 51 and 12 entries. A widget's name is in `config.container.header.title`, deeper than `render` reaches, so different widgets render alike and merge: "payment_acceptance_rate" and "payment_methods" make one entry.
  - Also Salla `dashboard-restrictions`, `portal-help-center-resource` and `portal-settings`, and BigCommerce `tax-services` (`classes: 5 items`).
- *Fix:*
  - Flatten by rule before rendering: one entry per element of a named list, carrying its parents' names:
    - WooCommerce: per country, bundle and plugin; per location and provider, offline method or suggestion;
    - Salla `dashboard-nav`: per node of `children`;
    - Salla `help-embedded-tree`: per `subSection` node;
    - Salla `report-widgets`: per widget, with `config.container.header.title` rendered.
  - Stop clipping in `build` (keep the clip in `show`), and fail the build where an entry would pass a set length.

**E-4. Dropped keys merge different items, and drop the field a placement needs.**
- *Found:*
  - **`app` is in `SKIP`** (line 40). Salla's `dashboard-app-routes` items are the route literals of 92 micro-frontends, and the app is what names a route's place.
    - 952 distinct (app, path) pairs render as 777 bare paths: "path: /", "path: :id", "path: /new", "path: /home".
    - 65 paths are shared by several apps, and merge. "path: /" stands for 68 items (bridge-sdk, ui-merchant-ads-google and others). "path: /new" stands for ui-merchant-inventory, ui-merchant-localization, ui-merchant-products and others.
    - `portal-app-routes`: 616 pairs render as 348 paths.
    - An agent can't place "path: :id". If it opens the entry's line, it sees the first item's app only.
  - **`item` and `headings` are in `SKIP`.** In `docs-event-lists`, a row such as "`Signed In` - When a user logs into their account" renders as nothing, and the heading that names its list ("Account Events", conditional webhooks) is gone.
  - **`parent`, `within` and `container` are in `SKIP`.** The repositories' `structures/README.md` says these keys record "only order and nesting the source itself states". Without them, a nav item or a permission loses what it sits under: Salla `dashboard-main-navigation` has 252 items with a parent, Shopify `admin-permission-tree` 28.
  - **The opaque-id test drops readable ids** of 24 characters or more (line 43):
    - 244 in Salla `settings-center`, such as "order-statuses-in-reports" and "shipping-label-deduction";
    - 53 permission handles in Shopify `admin-permission-tree`, such as "MANAGE_ORDERS_INFORMATION" and "APPLY_DISCOUNTS_TO_ORDERS". These are the handles the router's `eligibility` names. The `member` field keeps a camel-case form;
    - 17 Shopify route ids, such as "shopify-fulfillment-network" and "customer-segment-templates".
  - **`source` is in `SKIP`.** Shopify `admin-role-permissions` (768 items, 358 entries) drops which role a permission is listed for, and merges the same handle across roles.
- *Fix:*
  - Take `app`, `item`, `headings` and `parent` out of `SKIP`, rendering `parent` as the parent's label or id, and never merge items whose `app` or parent differ.
  - Limit the opaque test to UUIDs, `gid://` ids, hex hashes, and base64 strings with no `_`, `-`, `.` or `/` between runs of letters.
  - For the routes, drop the extractor's strings that aren't routes (K-3).

**E-5. BigCommerce's plan table pairs six rows with another row's name.**
- *Found:*
  - In `bigcommerce/structures/plan-comparison/items.jsonl`, lines 8 to 13 (entries `BC-E-00048` to `BC-E-00053`), `feature` names another row than `feature_text` and the plan cells do. By `meta.json`, `feature` is the accessibility tree's row header. In `source.html`, `feature_text` and the cells go together:

    | Entry | `feature` | the row, by `feature_text` and `source.html` | cells |
    | --- | --- | --- | --- |
    | BC-E-00048 | Custom SSL | Abandoned cart saver | Growth, Scale, Performance |
    | BC-E-00049 | Surcharge rate | Customer groups and segmentation | Growth, Scale, Performance |
    | BC-E-00050 | Shipper HQ shipping rules engine | Custom SSL | Scale and Performance: "Available" |
    | BC-E-00051 | Inventory locations | Google Customer Reviews | Scale, Performance |
    | BC-E-00052 | Online sales per year … | Price lists | Scale, Performance |
    | BC-E-00053 | No additional transaction fees … | Surcharge rate | 2%, 1%, 0.6%, 0% |

  - In `steps/004.aria.yaml` of run `20261029T015915Z-plan-upgrade-en`, six rows have no `rowheader` (lines 144 to 205): Abandoned cart saver, Customer groups and segmentation, Google Customer Reviews, Price lists, Phone support and Faceted search. So the extractor took the next row's header.
  - The brief warns of `settings-list` only (line 29). So an agent will read "feature: Custom SSL; … Growth: [image]" as Custom SSL on the Growth plan.
- *Fix:*
  - Render `plan-comparison` from `feature_text` and the cells only.
  - Add to the brief's warning: "BigCommerce's `plan-comparison`, rows 8 to 13: `feature` names another row; `feature_text` and the cells are the row's own (`source.html`)."
  - Ask the local agent to re-extract it beside H-009.

**E-6. Entry ids are positions, so any rebuild renumbers them.**
- *Found:*
  - An id is the entry's running number across the platform's structures, in the selection's order (`held_entries.py`, lines 211 to 213).
  - Rebuilt on a scratch copy with E-1's rule fixed, Shopify's entries grow from 8,880 to 9,254. Every id after `help-notes` moves by 374: `dev-nav`'s first entry goes from `SH-E-04297` to `SH-E-04671`.
  - Batches are ranges of ids (`batches.tsv`), and `check` and `held_amend.py` find entries by id. Every fix above changes the entries.
  - So a batch placed before a rebuild would then name other entries, and nothing would say so.
- *Fix:*
  - Make an id stable: `<PREFIX>-E-` with a short hash of the structure, the rendering and the first item's file and line. Or freeze `entries.tsv`, and give new entries numbers past the highest.
  - Make `build` refuse to rewrite an `entries.tsv` that a `placements-*.tsv` cites, unless every cited id keeps its text.
  - Apply every fix of Parts 1 and 2 before the first batch runs.

### Should fix

**E-7. `build` reports nothing per structure.**
- *Found:* `build` prints one line per platform, with each structure's entry count (line 221), and a line for a structure with no items at all (line 187). A selected structure that yields no entries for any other reason passes silently. That is how E-1 and E-2 went unseen.
- *Fix:*
  - Print, per structure: its items, how many pass the rule, its renderings, how many are read, how many are dropped and why, and its entries.
  - Exit non-zero where a `yes` structure gives no entry while some of its renderings are unread.
  - Exit non-zero where fewer than 90% of the distinct strings of a structure's unread items reach some entry: "What I ran", item 2, is the test.

**E-8. Salla's settings centre shows translation keys, not the platform's words.**
- *Found:*
  - `settings-center`'s entries carry keys, such as `label: products/filters#show_variants.label` and `description: products/filters#show_variants.description` (`SA-E-00902`).
  - The texts are in `structures/salla/dashboard-translations/en/settings.json` and `ar/settings.json`, such as `"affiliates#attachments.label":"Marketing assets"`. That structure is left as "the dashboard's strings".
- *Fix:*
  - Resolve the keys in the rendering from `dashboard-translations/<en|ar>/settings.json`, in both languages, and cite both files.
  - Change `dashboard-translations`' reason to "read through settings-center".

**E-9. BigCommerce's wrong addresses are rendered into the entries.**
- *Found:*
  - The brief warns that `settings-list` pairs each section with the next one's address (line 29). That is so: `BC-E-00001`, "Store profile", carries `/manage/microapps/localization-settings-ui`, where `steps/002.frame-0.aria.yaml` gives `/manage/microapps/store-profile-ui`.
  - Handoff H-009 (`6209e8d0`, after `ab8d98ff`) asks for a re-extraction. Until it lands, `held_amend.py` would write the wrong address into a cell's evidence, since its `why` quotes the entry's text.
- *Fix:* drop `address` from `settings-list`'s rendering until H-009 lands, or render each section's own address from the step.

### Notes

**E-10. Sampled against their items and sources, and found faithful:**
- Zid `store-plan-policies`: its 633 entries are the 633 keys of `user.store.subscription.policies_v2` in its source answer.
- Zid `dashboard-page-index`, `dashboard-route-manifest` and `store-permissions`.
- BigCommerce `channel-catalog`, against `steps/002.frame-0.aria.yaml` of its run, and `payment-gateways`.
- WooCommerce `options`: 237 of the 576 rows of `options.tsv` match the rule.
- Shopify `dev-changelog` (768 entries, as `meta.json` counts) and `admin-router` (1,364 items, 1,364 renderings, no merge).
- No `items.jsonl` line fails to parse. One rendering merges by case alone: "Settings" and "settings".

**E-11. The read mark ignores the commit.**
- `cited_lines` keys a citation by its file and line, not its commit (lines 100 to 111).
- Today that is harmless. For every citation of a selected structure that names a line (2,311 for Shopify, 979 for Salla, from the concern map and the landed subjects), the line is the same at the cited commit and at the head, and the quote is on it.
- It will mislead once a cited file is regenerated. Salla's `docs-operations/md-openapi/items.jsonl`, for one, was rewritten since `145f137`.
- Compare the line's text at both commits, and treat a changed line as unread.

**E-12. `show` clips at 400 characters by default** (line 337), below the 600 that `build` stores. 584 entries are cut further: Shopify 197, Salla 362, WooCommerce 20, Zid 4, BigCommerce 1.

---

## Part 3. The brief (`briefs/H-held.md`)

### Must fix

**B-1. The brief's own list of `supports` departs from `B-extent.md` in ways that move counts.**
- *Found:* the brief restates the values (lines 32 to 36) and sends the agent to `B-extent.md`'s two sections (line 25). Where the two differ, an agent follows the list in front of it. Line numbers of `B-extent.md` are at `ab8d98ff`.
  - **`core` includes any "permission"** (line 32). `B-extent.md` (line 134, the dry run's S7) says "A partner's permission shows an interface for apps", and only the staff permission is `core`. `check_class_part.py` applies S7 as `shows` (line 383).
    - Selected structures that list partners' and apps' access: Shopify `collaborator-access-permissions` (18 entries), `partner-api-client-permissions` (2), `app-install-consent` (29), and the partner side of `dev-dashboard-scopes` (99).
    - The class checker's guard reads a statement's note ("partner can request"), which a held entry lacks (C-2).
  - **`own-service`** is "only where the entry names the platform's company as the maker or provider" (line 33). `B-extent.md` (line 115) adds three things:
    - "or a company of its group";
    - "of a separate product, app, extension or service";
    - "A product's name that carries the platform's brand doesn't name its maker."

    The entries hold such names: BigCommerce "Payment Gateway: BigCommerce Payments", Salla "Lower shipping costs with Salla Shipping Labels" and "سلة - جي اند تي اكسبريس" (S-7), and BigCommerce "Featured channels by Feedonomics".
  - **`outside`** (line 35) drops "not the merchant, the buyer or the platform's company", and drops "A statement that makes the merchant or buyer responsible is `shows`, never `outside`" (`B-extent.md`, lines 117 and 118).
  - **The flag rule** (line 36) keeps "a feature flag that isn't released is `shows`". It drops "A released flag supports `core`, with its plan or store as its scope" (line 133). Salla's `dashboard-features` (241 entries) and Zid's flags are flags with plans.
  - **The slot-filler rule is gone:** "Slot fillers: … A flag's name isn't one" (line 142). Yet Salla's features list holds released flags named for carriers: "name: aymakan", "barq", "labaih", "mahmool" and others, `type: feature`, on the plans plus, pro and special.
- *Fix:* replace lines 32 to 36 with:

  > `supports` takes `B-extent.md`'s values exactly as "Cells and evidence" and its conventions define them. This pass's entries are statements in that sense. In particular:
  > - a partner's or an app's permission or access is `shows` (the dry run's S7), and the staff permission is `core`. This covers Shopify's collaborator permissions, its Partner API permission sets and an app's install consent, and Salla's partner access requests;
  > - `own-service` needs the entry to name the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service. A brand in a product's name, a field's value or a capture's label doesn't name a maker;
  > - a statement that makes the merchant or the buyer responsible is `shows`, never `outside`;
  > - a released flag supports `core`, with its plans or store as its scope;
  > - a flag named for a third party is the capability's evidence, never a slot filler.

**B-2. "A help page's title, a changelog post … are `shows`" decides placements by structure, against `B-extent.md`'s `core`.**
- *Found:*
  - Line 36 makes every help title and changelog post `shows`: about 3,500 entries, a quarter of the pass, which can then never support a count. They are:
    - Shopify's 2,317 Help Center titles (`help-section-children`);
    - Shopify's 768 and 305 changelog posts (`dev-changelog`, `merchant-changelog`);
    - Salla's 20 changelog entries and 104 help-tree nodes.
  - `B-extent.md` has no such rule. Its `core` (line 114) is "The statement names its own admin section, setting, route or built-in behaviour", and its convention on titles (line 137) is "its words as a whole decide".
  - Titles such as "Configuring customer privacy settings" (`SH-E-03180`), "Discount types" (`SH-E-02180`) and "Remove order tags" (a Flow action) name the platform's own setting or built-in feature.
  - So one agent will follow line 32 ("a built-in feature it states"), and another line 36.
- *Fix:* replace the second sentence of line 36 with:

  > A help page's title or a changelog post supports what its words state, by `B-extent.md`'s rules:
  > - `core` where it names the platform's own admin place, setting, route, plan line or built-in feature;
  > - `extension-point` where it names an app, an extension target or a provider interface;
  > - `shows` where it names only a topic, a guide or a third party.
  >
  > A release marker in it (beta, deprecated, sunset, now available) goes in `reading`. A feature flag that isn't released is `shows`.

  If the coordinator keeps the blanket rule instead, it is a method ruling of its own. It should then be stated as one, with its reason, and listed at the next report (`PLAN.md`, section 3).

**B-3. The sub-page rule contradicts `new`.**
- *Found:*
  - Line 37 makes `new` an entry that gives a thing "a place of its own: an admin section or route". Line 43 says "A sub-page, sub-route or setting of a thing the model holds is that capability's entry, not a new one."
  - Almost every route or section sits under something the model holds: the admin, Settings or a section.
  - Example: BigCommerce `BC-E-00035`, "group: Advanced; section: Early access; description: Try new tools, beta functionality, and upcoming features". It is a settings section, a place of its own, and `class_slice.py caps --terms "early access; feature preview; beta; preview"` finds no capability for it. One agent writes `new:Early access`. Another places it on CM-ACC-006, "Store details and general settings", as a sub-page of Settings.
  - The working tree holds an uncommitted addition to `B-extent.md`'s conventions, "What a place of its own is" (after `inspection-Q3M.md`, Q3M-6). It says "A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not a new one". That is narrower than line 43.
- *Fix:* replace the first sentence of line 43 with:

  > A sub-page, sub-route or setting is a capability's entry when it is that capability's own thing or a part of it: its list, detail, edit or settings page, or one of its settings. A section or route that only sits under a container (Settings, Apps, a menu, the admin), and whose own thing no capability holds as the cells' readings show, is `new`. Name its parent in your notes. A field, a toggle or a line of text inside a page is never a place of its own.

**B-4. A line with several cap_ids and several `supports` doesn't say which goes with which.**
- *Found:*
  - `cap_id` takes several cap_ids "only where the entry is two capabilities' at once", and `supports` several values (lines 31, 73 and 74). Neither says how they pair.
  - `held_amend.py` (`9d1369d3`, `plan`, lines 66 to 72) writes every value for every cap_id. On a scratch copy:
    - the fixture line `BC-E-00136	capability	CM-PAY-001;CM-ACC-006	core;extension-point`, meant pairwise, became four evidence rows: CM-PAY-001 `core` and `extension-point`, and CM-ACC-006 `core` and `extension-point`;
    - `CM-ACC-006;CM-ACC-006` with `core;core` became four identical rows.
- *Fix:*
  - In the brief: "A `capability` line names one cap_id. Where an entry is two capabilities' at once, write two lines with the same `entry_id`, each with its own `supports` and `reading`."
  - In `check`: take the same entry on two lines only where their cap_ids differ, and refuse `;` in `cap_id`.

**B-5. The "always out" kinds contradict the selection.**
- *Found:*
  - Line 40 makes "one store's or one account's own records" always out, and line 41 "market data, such as countries, currencies, languages or formats per country".
  - Selected structures whose every entry is a statement about one store:
    - Shopify `shop-request-details`: 736 entries, "what the admin states about each shop: its plan, features and limits" (line 89);
    - Salla `dashboard-features`: 241 entries, per store;
    - Zid `store-plan-policies`: 633 entries, the demo store's plan with each policy's `available_in`;
    - Salla `merchant-subscriptions`: 15 entries;
    - WooCommerce `options`: 237 entries, "the store's settings".
  - Selected structures whose entries are per country: WooCommerce `payments-providers` (per location) and `core-profiler-free-extensions` (per country), and BigCommerce `contracting-entities` (per country of residence) and `tax-services` (`supported_countries`).
  - One agent will mark these out under lines 40 and 41. Another will place them as the selection's reasons say. That is about 1,900 entries.
- *Fix:* replace lines 40 and 41 with:

  > - one store's or one account's own data: its orders, products, customers, people, ids, timestamps, tokens, and the values typed into it. A setting, feature, flag, plan policy, entitlement or limit the platform lists for a store is the platform's: place it on its capability, with the plan or store it is stated for as its scope. Its value for that store goes in `reading`, if anywhere;
  > - market data: a list of countries, currencies, languages, units or formats, or one country's own values, which are the subjects'. A thing the platform offers for a country or location, such as a payment provider, a free extension or a tax service, is placed on its capability, with that country as its scope.

### Should fix

**B-6. The output lacks what the coordinator needs to amend the model.**
- *Found:* a placement has five columns (lines 70 to 75). To amend a cell by `B-extent.md`, the coordinator also needs:
  - **the scope:** a cell's derived scopes come from its statements' scopes. At `9d1369d3`, `class_slice.py` (`held_items`) gives a held entry its labels as its scope, such as "demo@en,real-merchant@en". That is a store or a language. It is not the plan the entry states (Zid's `available_in: Growth`, Salla's `plans: [plus, pro, special]`), nor its country (WooCommerce's `location: AE`);
  - **the terms:** `cells.tsv`'s `terms` are "the platform's own words for it, each found in a cited statement" (`B-extent.md`, "Output"). `held_amend.py` makes a cell held without them;
  - **slot fillers and qualities,** which `B-extent.md` keeps in files of their own (lines 125 and 126):
    - the fillers are the carriers, gateways, tax services, apps and channels the entries name;
    - the qualities are the limits they state: Zid's policy `config`, BigCommerce's "Storefronts that can be added: 4 5 8 15", Shopify's Flow limits;
  - **for a `new` thing:** its domain and area, its parent, and its name in each language.
- *Fix:*
  - Add four columns:
    - `scope`: the plan, country, market or store the entry states it for, in its words, or empty;
    - `terms`: the platform's words for the thing, `;`-separated, each in the entry's text;
    - `filler`: a third party the entry names as doing it;
    - `quality`: a limit or value the entry states, in its words.
  - For each `new` thing, ask in the notes for its proposed domain, area and parent.
  - Have `held_amend.py` write `scope` and `terms`, and write `filler` and `quality` into the parts' `slot-fillers.tsv` and `qualities.tsv`.

**B-7. The grouping rule, `out`'s grain and "a UI string" will each be read two ways.**
- *Found:*
  - "Group only entries next to each other in one structure" (line 44) can mean consecutive ids, or entries near each other. A fixture group `BC-E-00001;BC-E-00060`, from two structures, passes `check` (C-1).
  - "`out`: … at the grain of the model" (line 38) can make a setting finer than a capability `out`, while line 43 makes it that capability's entry.
  - "A UI string" (line 39) covers every label in a navigation.
- *Fix:*
  - "Group only entries with consecutive ids of one structure."
  - Drop "at the grain of the model".
  - "A UI string: a button, message or prompt that names no place, setting, plan line, permission, event or feature, such as 'Close', 'Dismiss', 'Learn more' or 'Back'."

**B-8. The basis line, the reading list, and two commands.**
- *Found:*
  - **The basis line** (line 7) reads "reaches it by reading, not by search (the founder, 30 October)". The founder's decision (`founder-decisions.tsv`, row 33) says "read through their own reading guides and indexes, not by search alone", and "Search (method/held_index.py, method/corpus_search.py) follows the guides".
  - **The reading list:** the decision lists `docs/OPERATING.md` and `index/`, and, for other-product-class, each platform folder's `index/` and `structures/REGISTER.tsv`.
    - The brief (lines 19 and 20) leaves out `index/` on every platform, and the register for Zid, BigCommerce and WooCommerce. Those agents then read no description of their structures except `meta.json`.
    - `OPERATING.md` is for running captures. This pass sends no capture request, and the brief could say so.
  - **Line 24** names `class_slice.py caps --domain`. `caps` takes `--terms` and `--width` only: `class_slice.py: error: unrecognized arguments: --domain C`.
  - **Line 64** prints entries with `show`, whose default width is 400 (E-12).
- *Fix:*
  - Line 7: "…so that what the platforms show of themselves reaches the model through their own lists, read entry by entry, not by search alone (the founder, 30 October: the repositories' guides and indexes first, then search)."
  - Lines 19 and 20: add `index/`. For Shopify and Salla, that includes `index/ledger/`, for the lists their structures enumerate. For Zid, BigCommerce and WooCommerce, add the platform folder's `structures/REGISTER.tsv` rows for your structures, and its `index/`. Add: "This pass sends no capture request: a gap goes in your notes, for the coordinator."
  - Line 24: `caps --terms "<term>; <term>"`.
  - Line 64: `show --from --to --width 600`.

**B-9. Reading every `meta.json` whole costs up to about 65,000 tokens a batch.**
- *Found:*
  - The brief sends the agent to "each structure's `meta.json`" (line 21).
  - The `meta.json` files of a batch come to: SA-2 227 kB, SA-1 192 kB, SH-10 121 kB, SA-3 106 kB, SA-6 91 kB, SH-3 89 kB. Most of that is lists of fetch-archive records.
  - At about 3.5 characters a token (an assumption), SA-2's files alone are about 65,000 tokens.
- *Fix:* "Read `meta.json`'s descriptive keys only: `structure`, `surface`, `shape` or `shape_observed`, `counts`, `items` and `of`." Or have `show --structure S --meta` print them.

**B-10. Which cells a placement would change is a script's job.**
- *Found:*
  - The notes and the report ask each agent for the "entries whose placement would change a cell the model holds" (lines 79 and 90). That costs a `land_points.py cell` call per capability.
  - `held_amend.py plan` (`9d1369d3`) already computes the evidence rows per cell, and the cells that become held.
- *Fix:*
  - Drop the item from the notes and the report.
  - Have `held_amend.py plan` also print the cells whose supports a placement would change: a `shows`-only cell gaining `core`, or a `none-held` cell gaining any.

**B-11. A thing the model lacks, with no place of its own, has no placement.**
- *Found:*
  - `new` needs a place of its own (line 37), and `out` is for what "isn't something the platform does" (line 38).
  - A single app (one of Salla's 815 `marketplace-apps`), a help page or a released flag can show a thing no capability holds, which has no place of its own.
  - Line 47's "place it where it most plainly belongs" will then put it on the nearest capability, or `out`.
- *Fix:* "An entry that shows a thing no capability holds, without a place of its own (one app, one help page, one flag), is neither `capability` nor `out`. Write `new:<name>` with `supports` `shows`, and say in your notes that it has no place of its own. The coordinator decides it with the others."

### Notes

**B-12.** "none of which the model has read" (line 5): Zid's `dashboard-locales` is cited by what the model reads (`registers --platform zid`: "read 1"), through a landed subject's statement.

**B-13.** `held_amend.py`'s header (`9d1369d3`) names a section of the brief, "After the batches", that the brief doesn't have.

**B-14. What the brief gets right,** as `PLAN.md` requires:
- the founder's words are never evidence;
- every claim is one of the three kinds;
- a maker or a third party comes only from the entry and its source;
- the repositories are read-only, and Python runs with `-I`;
- placements are written as the agent goes;
- the source governs where the items and the source disagree, with a verified example (line 29).

---

## Part 4. The checker (`held_entries.py check`)

### Must fix

**C-1. `check` passes rows the brief forbids.**
- *Found:* on a scratch copy (`CLASS_MODEL_DIR`), I wrote `placements-BC-1.tsv` with 15 careless lines among 127 `out` lines. `check --platform bigcommerce --batch BC-1` refused only three things:
  - a comma-separated id list;
  - an entry placed twice;
  - the header of a copy saved with a byte-order mark and CRLF line ends.

  With those corrected, it printed "142 of 142 entries placed; 0 problems" (exit 0) on these:

  | Line | What was wrong |
  | --- | --- |
  | `BC-E-00001;BC-E-00060` grouped | two structures, not next to each other (line 44) |
  | `CM-ACC-006;CM-PAY-001` with `core` | which cap_id `core` is for (B-4) |
  | `core;own-service;shows` on one cap_id | three values for one entry |
  | `new:Locations` with no `supports` | the brief asks what it supports; `held_amend.py` then makes it `shows` |
  | `new:Pick up methods;CM-ACC-006` | a new thing and an existing cap_id at once |
  | `new:checkout` | an existing capability's name (CM-CHK-001, "Checkout: the step in which the buyer completes the order") |
  | `new:Gift wrapping` and `new:gift-wrapping ` | one thing named two ways in one batch (line 37) |
  | `new:CM-ACC-006` | a cap_id used as a new name |
  | an empty `entry_id` | a line that places nothing |
  | `core; ;` | empty pieces |
  | `CM-ACC-006;CM-ACC-006` with `core;core` | a duplicate, which `held_amend.py` writes four times |
  | `own-service` on "Order notifications" | no maker stated, and not flagged |
  | `new:Returns` with `shows` only | a new capability resting on nothing countable |

  It doesn't check that `notes-<batch>.md` exists.
- *Fix:* in `cmd_check`:
  - refuse an empty `entry_id`, an empty piece in any `;`-separated list, and `;` in `cap_id` (B-4);
  - require a group's ids to be consecutive, and of one structure;
  - for `new`, require exactly `new:<name>` and a `supports` value. Require the name to differ from every capability's name, comparing them casefolded with spaces and hyphens folded. Refuse two names that fold alike unless they are identical;
  - require `notes-<batch>.md` to exist, and to name each new name;
  - print, without failing:
    - every `own-service`, with its entry's text;
    - every `core` on a structure of partners' or apps' permissions (B-1);
    - the batch's new names, with their entry counts.

### Should fix

**C-2. The model's own guards don't see held entries.**
- *Found:* at `9d1369d3`, `class_slice.py` makes held entries citable, with `note` "the held pass" and `placement` "held" (`held_items`). So `check_class_part.py`'s guards never fire on them:
  - the partner-permission problem reads the statement's note: "partner can request" (line 382);
  - the unreleased-flag flag matches `"released":\s*false` (line 407), while a held entry's text renders `released: false`;
  - the boundary flag tests `placement == "boundary"` (line 409).
- *Fix:*
  - Give held entries a `note` from their structure: "a partner can request" for `collaborator-access-permissions`, `partner-api-client-permissions`, `app-install-consent` and Salla's partner access requests.
  - Give them a `placement` from the selection: `boundary` for scopes, topics and API groups; `decides` for plans, flags and permissions; `where` for routes and navigation.
  - Match `released: false` in both forms.

### Notes

**C-3.** At `9d1369d3`, a held entry's citation carries the entry's rendering as its `quote` (`class_slice.py`, `subject_citations`). A rendering joins `key: value` pairs and clips, so it is not the bytes. A report that quotes it would fail `check_report.py` against the cited line. Quote the source line's own words instead.

---

## Part 5. The batches and the cost (`held/batches.tsv`)

### Should fix

**K-1. A 900-entry batch outgrows the context this project keeps.**
- *Found:*
  - `STATE.md` (line 153) and `method-report.md` (sections 4 and 7) keep a context under about 200,000 tokens, since a request costs about its whole context.
  - Printing each batch's entries once, at `show`'s width (an assumption: 3.5 characters a token for Latin text, 2 for Arabic):

    | Batch | SH-6 | SA-3 | SA-4 | SH-4 | SH-1 | SH-3 |
    | --- | --- | --- | --- | --- | --- | --- |
    | Tokens to print its entries | ~83,000 | ~80,000 | ~73,000 | ~69,000 | ~65,000 | ~62,000 |

  - To that, each batch adds the brief and the guides (about 9,000 to 12,000 tokens), `meta.json` (up to about 65,000, B-9), the lookups, and the placements it writes (about 35 tokens a line, an assumption).
  - By that estimate (an assumption), a 900-entry batch ends near 200,000 to 250,000 tokens.
- *Fix:* `batches --size 300`, cut where a structure or a section ends (K-2), so that no batch prints more than about 25,000 tokens of entries. State the cap in the brief.

**K-2. Batches cut a section in two.**
- *Found:*
  - SH-1 ends at `SH-E-00900`, Settings' `setting:legal:privacy`, and SH-2 starts with `setting:legal:refund`.
  - SA-1 ends inside `settings-center`'s `products/filters` (`SA-E-00900`).
  - SH-3 ends inside the Help Center's marketplaces page (`SH-E-02700`).
  - Two agents will place the halves of one section, perhaps differently, and neither can group across the cut.
- *Fix:*
  - Let `batches` end where the `section` (admin-router, settings-center), the `page` (help-section-children) or the `group` changes.
  - Tell the second agent of a split structure to read the first agent's placements for it.

**K-3. What the pass will cost, and how to cut it without losing evidence.**
- *Found:* an estimate. Every figure is an assumption except the counts.
  - **The rates assumed:** about 170 tokens per placed entry across a batch, one request per 8 entries, and a start of about 60,000 tokens.
  - **The pass as cut:** a 900-entry batch then costs about 15 million tokens, and the pass about 180 to 310 million. That is before the `doc` structures, the entries the fixes add (E-1 alone adds 374), re-runs and the review.
  - **The plan's figure:** `PLAN.md` (at `9e59d2ef`, line 633) assumes 80 to 180 million for the held pass and the omission review together.
- *Cuts that lose no evidence,* with the counts measured:
  - **Smaller batches (K-1):** the same entries in 300-entry batches cost about 160 million by the same assumptions, since a batch's cost grows with the square of its context's length.
  - **One entry per thing, not per store or answer set:**
    - Shopify `shop-request-details` renders `set: 0`, `set: 1` and so on, a capture's index, into its text. So its 736 entries hold about 100 distinct section and key pairs;
    - Salla `dashboard-features` repeats, for other stores, 236 of its 241 entries' feature names already read.

    Render the per-store values as the scope of one entry.
  - **Drop by script,** with the reason listed for the agent to confirm in bulk:
    - the 264 Salla "route" entries whose path is a word list or code, such as `path: /Adventure Seekers` or `path: /:pathMatch(.*)*`;
    - `__typename` keys;
    - renderings made only of layout keys.
  - **One entry for twins:**
    - an Arabic and English twin: about 140 pairs in Salla's menus, help tree, portal header and invoice settings, with more in its app categories;
    - Shopify's help notes: the English, with the Arabic only where an English page has no twin (E-1).
  - **Read `plan-page-public` for its plan cards and FAQs only.** Its comparison cells (`tag: td; text: Up to 87% off`) render without their row and column, and repeat the table that `plan-comparison-public` holds, 102 of whose 105 lines are cited.
  - **Print each entry's candidate cap_ids by script,** as `class_slice.py candidates` does for cells: the capabilities whose evidence cites the same identifier (a route id, a permission handle, a scope, a topic, a feature key, a path), or whose cells' `terms` occur in the entry. The agent then confirms, rather than searching for each entry.
  - **Read `meta.json`'s descriptive keys only** (B-9), and drop B-10's per-agent cell lookups.

  With all of these, the pass would cost about 100 to 130 million (an assumption).
- *Fix:* apply the cuts. Re-measure after the dry run (K-4) with `method/count_tokens.py`, and bring the projection to the founder with the next report if it passes the plan's figure.

**K-4. No effort level is stated, and there is no dry run.**
- *Found:*
  - The founder's decision of 30 October (`founder-decisions.tsv`, row 32): "No agent runs at `medium` or `low` for reading evidence, reviewing, or making an engineering judgement: `high`, `xhigh` or `max`. … Whether a level misses is judged by the quality and completeness of its results."
  - Neither the brief nor `batches.tsv` names a level.
  - The pass has no dry run, though the brief is new and the extent's own brief had one (`PLAN.md`, Stage 4A).
- *Fix:*
  - Add to the brief: "Effort: `high` at least (the founder, 30 October)."
  - Run two small batches first, one of admin structures and one of plans or permissions (BC-1 and ZD-3, for example). Have an agent that made none of them review every placement against its source. Set the level for the other batches from that review's misses: `xhigh` where `high` misses.

---

## Part 6. What the pass leaves unread, and how a second stage should read it

**U-1 (should fix). The unread admin pages, help and docs, and a route to them by cell.**
- *Found:* `held-vs-read.tsv` gives, per group, the addresses held readable, and how many of them the model read:

  | Platform | Admin pages and answers | Help and docs |
  | --- | --- | --- |
  | Shopify | `admin.shopify.com/store`, 3,475 browser-step pages; `/settings`, 331; the admin's API answers, 8,277: none read | `help.shopify.com/manual`, 5,143 (123 read); `shopify.dev/docs`, 8,586 (25 read); changelog posts, 827 and 305 (none read) |
  | Salla | `s.salla.sa/marketing`, 112; `/settings`, 97; `demo.salla.sa/marketing`, 98: none read | `help.salla.sa/article`, 2,951 (66 read); `api.salla.dev`, 722, 104 and 70 (none read) |
  | Zid | `dashboard.zid.sa/stores`, 286; `hermod.zid.sa` answers, 243 and 18: none read | `help.zid.sa`, 40 (19 read) |
  | BigCommerce | | `support.bigcommerce.com`, 80 (8 read); `docs.bigcommerce.com/developer`, 149 (122 read) |
  | WooCommerce | the release's code (S-4) | `woocommerce.com/document`, 107 (79 read) |

  658 of the 1,735 cells hold nothing: Shopify 74, Salla 95, Zid 154, BigCommerce 175 and WooCommerce 160 (`merged/cells.tsv`). The held pass fills some of them. The rest are the second stage's (`PLAN.md`, Stage 4A, at `9e59d2ef`).
- *Fix:* a design for the second stage. It is a reading of what the repositories offer.
  1. **Work by cell, not by page.** One batch per platform takes 20 to 30 of the cells still holding nothing after the held pass's amendments, each printed by script with its leads.
  2. **Take the leads from the repositories' own indexes,** read through their guides first (the founder, 30 October):
     - **Shopify:**
       - `index/ledger/admin-route.tsv`: each admin route per store, with the step files that hold it;
       - `derived/journey-catalog.jsonl`: the admin's units of work, with their routes, forms and mutations;
       - `derived/admin-controls.jsonl`: what each route rendered per store;
       - `derived/eligibility-by-store.tsv`;
       - `derived/help-admin-links.tsv`, which joins Help Center pages to the routes they reach.
     - **Salla:**
       - `index/ledger/nav-page.tsv`, `dashboard-app.tsv`, `settings-field.tsv`, `feature.tsv`, `report.tsv`, `webhook-event.tsv` and `docs-operation.tsv`;
       - `derived/map-units.tsv`, `derived/journey-catalog.tsv`, and the gates (S-9);
       - `help-articles`' 2,938 titles and short descriptions, with their texts in `texts.jsonl`.
     - **Zid:**
       - `index/ledger/dashboard-routes.tsv`: each manifest route, whether a run opened it, and its step files;
       - `dashboard-locales`, by namespace;
       - the backlogged `dashboard-api-resources` (1,437 calls, held as bytes), as a lead for the API's groups.
     - **BigCommerce:** `settings-list`'s sections lead to the steps of run `20261029T012951Z-store-settings-en`; then its Help Center runs.
     - **WooCommerce:** the release's settings and REST classes (S-4), then `woocommerce.com/document`.

     A capability's terms come from the other platforms' cells (`class_slice.py candidates`). The platform's own words come from the held pass's placements on neighbouring capabilities.
  3. **Read in order, for each cell:**
     - the admin page first: the route, with its step's `aria.yaml` or `text.txt`;
     - then the help pages the route links to, or the titles that hold its terms, in each language the platform uses;
     - then the docs.
  4. **Record what was read.** A cell still holding nothing records what it read, at a commit (`PLAN.md`, section 6). Before any capture request, its route is checked against what is held (the founder, 30 October).
  5. **Sample what stays unread,** by group, so the rate of misses is measured: the omission review (`PLAN.md`, Stage 4A).

---

## What I ran

All from `/home/user/sharrwah-knowledge-map`, with `python3 -I`. The tests that write ran on copies of `studies/class-model/` under the scratchpad, with `CLASS_MODEL_DIR` set.
1. **The registers against the selection:** `method/held_entries.py registers --platform <p>` for all five platforms, joined with `selection.tsv` and each `entries.tsv`. That gave the structures absent from the selection, and the `yes` structures with no entries.
2. **`build`'s steps re-run for every `yes` structure,** importing `held_entries`. For each structure I counted:
   - its items, how many pass the rule, its renderings, how many are read, how many the words filter drops, and its entries;
   - the renderings that merge items differing beyond the capture's keys, and which keys differ;
   - the share of distinct strings of the unread items that reach some entry;
   - the `SKIP` keys its items carry;
   - the readable ids the opaque test drops;
   - the merges by case alone, and the lines that fail to parse.
3. **The citations of selected structures:** for every citation that names a line, from the concern map and the landed subjects, the line at the cited commit against the line at the head, and whether the quote is on it.
4. **A rebuild:** `build --platform shopify` on a scratch copy, with the help-notes rule fixed.
5. **The checker on fixtures:** `check --platform bigcommerce --batch BC-1` on scratch placements (15 careless lines; then a copy with a byte-order mark and CRLF line ends), and `method/held_amend.py plan --platform bigcommerce` on the same placements.
6. **Items against their sources:**
   - BigCommerce: `plan-comparison`'s items against `source.html` and `steps/004.aria.yaml`; `settings-list` against `steps/002.frame-0.aria.yaml`; `channel-catalog` against its step;
   - Zid: `store-plan-policies` against its answer;
   - WooCommerce: `options` against `options.tsv`, and the nested lists of `payments-providers` and `core-profiler-free-extensions`;
   - Salla: `com-plans`' text; `docs-event-lists`' names against the concern map's citations and the other entries; `settings-center`'s keys against `dashboard-translations`;
   - Shopify: Flow's connectors' nested tasks; `help-notes`' classes and their pages against the pages the model read.
7. **The sizes:** the token size of each batch's `show` output, and of its `meta.json` files.
8. **The repositories' guides:**
   - observed-sh and observed-sa: `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md` and `structures/REGISTER.tsv`, with the names of `index/ledger/`'s files and `derived/`'s;
   - other-product-class: `README.md`, and each platform folder's `README.md`, `GAPS.md` and `structures/REGISTER.tsv`.
9. **The commands the brief names:** `method/class_slice.py caps`, with and without `--domain`, and `method/land_points.py cell`.

## What I didn't check

- I placed no entry, beyond the fixtures, and judged no placement against the model beyond the examples cited.
- I verified the items of 11 structures against their sources ("What I ran", item 6), not every structure's.
- I named WooCommerce's release lists (S-4) from their files. I didn't extract them or count their entries beyond the settings ids.
- I didn't read `docs/OPERATING.md` in either observed repository, nor `index/` beyond the ledgers' names and the head of `ledger-summary.tsv`.
- The cost figures in K-1 and K-3 are assumptions from this project's measured rates and a characters-per-token ratio. They were not measured on a held batch.
- `method/held_amend.py`, and the changes to `class_slice.py` and `check_class_part.py`, came after the inspected commit. I read them for what the coordinator will do with the output, and tested `held_amend.py plan` once.
- While I ran, the working tree held the coordinator's uncommitted changes: `briefs/B-extent.md`'s "What a place of its own is", `briefs/Q3-misses.md`, three scripts, and `inspection-Q3M.md`. B-3 cites the first as uncommitted. I changed none of them.
