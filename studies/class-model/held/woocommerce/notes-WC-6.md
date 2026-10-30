# Notes: held pass, WooCommerce, batch WC-6 (`release-admin-menus`, `release-capabilities`, `release-features`, `release-rest-controllers`)

**What the batch holds:** 101 entries, every one read from WooCommerce's release 11.2.1, the one `evidence/product-class/woocommerce-11.2.1/` fixes by checksum, unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`. Readings cite it as `woocommerce-11.2.1:<path>`.
- **3 of `release-admin-menus`:** `includes/admin/class-wc-admin-menus.php`, lines 113, 123 and 251.
- **17 of `release-capabilities`:** `includes/class-wc-install.php`, lines 2429 to 2447, the per-type capabilities of `get_core_capabilities()`.
- **29 of `release-features`:** `src/Internal/Features/FeaturesController.php`, lines 319 to 718, the definitions of `init_feature_definitions()`.
- **52 of `release-rest-controllers`:** `includes/rest-api/Server.php`, lines 103 to 163 (the wc/v1 and wc/v2 controllers) and 271 (wc-telemetry's tracker).

The selection's rule counts the lines the concern map cites as read, so the structures' other lines aren't entries here: the menus' WooCommerce > Reports and Settings rows, the three core capabilities (`manage_woocommerce`, `create_customers`, `view_woocommerce_reports`), the Variation gallery definition (an inventory entry, WC-I-0341), and the wc/v3 and wc/v4 controllers.

**No batch has placed these structures before.** WC-1 to WC-5 placed the free extensions, the options and the payment providers. I read their placements and notes to the end, each with the coordinator's check, and kept to their capability where a feature is the same thing as one of their lines:
- WC-3 placed the flags it met among the options by their release state (`is_experimental`) in this same FeaturesController. Each feature here takes the capability and the supports of its option's line in WC-3.
- That includes WC-3's three new things.

**Count:** 101 entries, 164 lines.
- **By entry:** 98 have `capability` lines only; 3 are `new` only, beside their CM-EVO-001 line; none are `out`.
- **By line:** 161 `capability`, 3 `new`.
- **By supports:** core 147, shows 16, extension-point 1.

## How each structure was decided

**Admin menus (3).**
- **Sales reports** (WC-E-e77c6f4c): CM-ANL-002, `core`. It is the Reports page `wc-reports`, which the release adds as WooCommerce > Reports, the cell's WC-S-0043, for a user with `edit_others_shop_orders`, and as the top-level menu Sales reports for a user without it (lines 109 to 114, 140 and 141).
  - The title is conditional, so it is a statement of its own (M-14).
  - Its condition is a gate on the user, not on the store, so it goes in `reading`, not `scope` (rule 5).
- **Settings, "WooCommerce settings"** (WC-E-d1ca07f7): a container (M-13), so it takes two lines, both `core`:
  - CM-ACC-006, whose cell cites the same menu item, WooCommerce > Settings (WC-S-0044);
  - CM-APP-006, whose cell cites the same page as the one extension settings pages are added to (WC-S-5430). Rule 2: a cell already cites the place.
  - The entry itself names no app. If the coordinator reads CM-APP-006's cell as resting on the filter (WC-S-0444) and not on the page, the second line goes.
  - Its children, the settings tabs, are WC-3's and WC-4's options, the release-settings structure and the concern map's settings rows.
- **WooCommerce extensions** (WC-E-0727f55d): CM-APP-001, `core`, as the cell's WooCommerce > Extensions (WC-S-0046).
  - Its function `addons_menu()` is marked '@deprecated 10.5.0 The marketplace feature is now always enabled. Use the Extensions menu instead.' (line 241), a release marker in `reading`.
  - The page `wc-addons` is still registered, its submenu item hidden, by `addons_my_subscriptions()` (lines 260 to 263).
  - A lead for the coordinator: the deprecation names the marketplace, so the page may also be CM-APP-002's. I didn't place it there, since the entry's words name extensions, not the Marketplace.

**Capabilities (17), 3 lines each.**
- **What each one is:** each entry is a template, `edit_{$capability_type}` and the rest. The same function fills it for each capability type of line 2423: `product`, `shop_order` and `shop_coupon`. The install gives each one to the administrator and shop_manager roles (lines 2402 to 2404).
- **So it isn't a scaffold for no place** (rule 2, out). It is three staff permissions, one per post type.
- **Each permission is `core` on what it gates** (ruling, after ZD-7):
  - CM-CAT-001 for `product`;
  - CM-ORD-001 for `shop_order`;
  - CM-MKT-002 for `shop_coupon`.
  - Each of those cells already cites its post type's capability type.
- **No line on CM-STF-002:** none of these is a permission over the staff's permissions themselves, and the roles they are given to are the source's context, not the entry's thing.
- **`terms`** hold the template as the entry states it. The checker tests terms against the entry's text, and the concrete names, such as `edit_shop_order`, aren't in it. Each reading names them.
- **The four `_terms` permissions** (WC-E-7a47461c to WC-E-333c14a3) are placed on the type's capability only. This source doesn't state which taxonomies they gate (see the second stage, below).

**Features (29).**
- **Release state.** I read each definition in full in the source, the release state with it (ruling on flags):
  - `'is_experimental' => true` gives `shows`;
  - `false` is a released flag, `core`;
  - a definition that states no `is_experimental` takes the definitions' default, `'is_experimental' => true` (`add_feature_definition()`, lines 226 to 236), the same file. Only Block Email Editor (alpha) does that, so it is `shows`, as WC-3 placed its option, now with the reason stated.
- **Deprecated, always on.** Marketplace (10.5.0), Point of Sale (11.0.0) and Push Notifications (10.9.2) state `deprecated_since` with `deprecated_value` true, which `feature_is_enabled()` returns (lines 948 to 950). They are released, on, with their toggle hidden: `core`, with the deprecation in `reading` as a release marker.
- **A second line on CM-EVO-001, `core`, for 22 of them** (M-6). The cell's thing is 'the WooCommerce features that can be enabled and disabled by admin users' (WC-S-5433), each definition with `is_experimental` and `enabled_by_default` (WC-S-5434).
  - Each feature whose definition doesn't set `'disable_ui' => true` is listed with its toggle on the Features page (lines 1442 to 1496).
  - Experimental ones are listed too, under 'Experimental features', the cell's "experimental ones included". So the EVO-001 line is `core` for them as well, while their own capability's line is `shows`.
  - The 7 with `disable_ui` true have no toggle, so they take no EVO-001 line: Cart & Checkout Blocks, Marketplace, Site visibility badge, Point of Sale, POS staff, Order Fulfillments and Push Notifications.
  - **None of these lines changes a cell.** If the coordinator reads the structure's "feature" as a field every entry holds, and so no parent's term (rule 2's "a word every entry of your structure holds"), the 22 lines go and nothing else changes.
- **Second things the descriptions name**, read in the source, since the items leave most descriptions out (below):
  - Cart & Checkout Blocks: CM-CHK-002, the cart block, `core`.
  - Marketplace's 'extensions and themes': CM-SFR-003, `extension-point`, as the cell places the Marketplace's Themes category (WC-S-0695). No maker is named.
  - Remote Logging: CM-TRU-021, `core`. It sends the store's error logs and diagnostic data to WooCommerce, and 'requires … usage tracking' (line 438).
  - Point of Sale 'in the WooCommerce mobile apps': CM-SRF-001, `core`.
  - POS staff, 'POS staff management, roles': CM-STF-002, `shows`.
  - Push Notifications: CM-NTF-002, `core`, which the cell cites.
- **Analytics' description, 'All data stays within your store.',** is a data location: it goes in `quality` (rule 5).

**One feature against the ruling, for the coordinator: Order Fulfillments** (WC-E-ea53849e).
- It is `'is_experimental' => false`, off by default, with `'disable_ui' => true` (lines 604 to 614).
- The ruling would make it `core`. CM-SHP-009's cell reads the same definition as `shows`: 'off by default, with its toggle hidden from the admin' (WC-S-0938, WC-S-5444). I kept to the cell's reading, `shows`.
- **The same holds for Cart & Checkout Blocks** (lines 339 to 345): released, its toggle hidden, and no default stated, so the definitions' default, off, applies (line 229). Yet CM-CHK-001's cell reads it `core` (WC-S-5431), and I kept that too.
- The two cells read like definitions differently. What would settle it: the coordinator's reading of a released feature that is off by default with no toggle. The release's `feature_is_enabled()` (from line 940) may treat these two differently; I didn't trace it.

**REST controllers (52).**
- **Each v1 and v2 controller is `core`** on the capability whose cell cites the same endpoint in wc/v3 or wc/v4. It is the older version of WooCommerce's own API for its own feature (rule 4).
- The namespace loads where `wc_rest_should_load_namespace()` allows it (lines 77 and 78). That is a condition I didn't trace.
- **`network-orders`** (WC-E-25ab4fa8) is `shows` on CM-ACC-003, as that cell reads wc/v3's network-orders: WordPress multisite, not one merchant's several stores (WC-S-0089).
- **`settings` and `settings-options`** go to CM-API-001, whose cell cites the settings API (WC-S-0684). wc/v3's own `settings` rows (WC-S-0111, WC-S-0112) are cited by no cell.
- **`webhook-deliveries`** goes to CM-API-008, on its name, a reading: wc/v3 lists no such controller (lines 174 to 218).
- **wc-telemetry's `tracker`** goes to CM-TRU-021, `core`, the resource the cell cites (WC-S-0253).
- **No line on CM-API-006.** Each controller's namespace, `api: v1`, is the group it sits under, which CM-API-006 already places through the namespaces themselves (WC-S-0076, WC-S-0077). It is not the entry's own thing (rule 2, a group the entry only sits under).

## New things

WC-3 named all three, and they have no place of their own: each is one feature, with no route or section. Here they are the feature definitions behind WC-3's options, so they take the same `new:` names.

| new | entries | place of its own | proposed domain / area / parent (a reading) | name (WooCommerce is in English only) | terms searched |
| --- | --- | --- | --- | --- | --- |
| `new:Clear Customer Sessions When Empty` | WC-E-93d083d4 (lines 624 to 634, experimental) | none: one flag | G OPS, or `out`, as the coordinator's check on WC-3 expects | Clear Customer Sessions When Empty | WC-3's: session; sessions. Its leads CM-CUS-001 and CM-STF-002 come by "customer" only: the buyers' records and the Customer role, not sessions |
| `new:Cache Product Objects` | WC-E-c228b5cc (lines 687 to 697, experimental) | none: one flag | G OPS, or `out` | Cache Product Objects | WC-3's: cache; caching; performance. Its leads CM-CAT-001 ("product") and CM-TRU-013 ("controller") aren't caching |
| `new:Unified block editor assets` | WC-E-5bea2973 (lines 710 to 718, experimental) | none: one flag | G OPS, or `out` | Unified block editor assets | WC-3's: performance; cache; editor. Its leads CM-PLN-001 ("performance"), CM-SFR-002 ("editor": the theme editor), CM-SFR-004 ("scripts") and CM-SEL-006 ("bundle") are other senses |

The descriptions of the first two begin '[Performance]', which supports the coordinator's likely `out` as the software's own bookkeeping.

## The checker's NOTEs, each read

- **Lines 57, 58 and 97:** `core` on WooCommerce Analytics and WooCommerce MCP, named with the platform's brand. Each is a feature of WooCommerce's own code, defined in its FeaturesController, not a separate product. So `core` rests on what the definition shows, not on a maker. MCP's own line (CM-AIA-004) is `shows`, since it is experimental. Line 97 is its CM-EVO-001 line.
- **Lines 98, 108 and 112:** the three new things. I read their leads' cells, as the table says.
- **No `CHANGES` line was printed:** every line falls in a cell that already holds its placement.

## Entries I couldn't tell, and what would settle each

- **The Settings container's CM-APP-006 line** (above). What would settle it: the coordinator's reading of that cell's core statement, WC-S-5430.
- **Order Fulfillments and Cart & Checkout Blocks,** released and with no toggle (above).
- **The `_terms` permissions for `shop_order` and `shop_coupon`.** The install gives them, but this source names no taxonomy of orders or coupons. They are placed on CM-ORD-001 and CM-MKT-002 as permissions over those types. What would settle it: the release's post types file, which isn't this structure's source.
- **WooCommerce extensions:** CM-APP-001 or CM-APP-002 as well (above).

## Where the items and the source differ (the source governs)

The `release-features` items keep only some of each definition's fields:
- **Descriptions.** The items hold a description only where the source writes it on one line: Analytics, Product gallery videos, Cart & Checkout Blocks, Order withdrawal and Unified block editor assets. Every other description, the `sprintf` ones and those that open `__(` on a line of their own, is missing from its item, Marketplace's and Order Attribution's among them. The readings quote them from the source, and the `terms` keep to the items' text.
- **`is_experimental`.** It is missing from the items of Remote Logging (line 455), Email improvements (line 509) and Blueprint (line 530), which state `false` after a comment block or a nested array. So these three read as if their state weren't stated. The source makes them released.
- **`enabled_by_default`.** Block Email Editor (alpha)'s `false` (line 550) is missing too.
- **Missing from every item:** `disable_ui`, `deprecated_since`, `deprecated_value` and `option_key`, which decide the toggle, the deprecations and the option WC-3 placed.

## For the second stage: what the sources state that no entry holds

- **Variation gallery** (`FeaturesController.php`, lines 552 to 562): 'Add multiple images per product variation.', released, deprecated since 11.1.0 and always on. The concern map holds it only as an inventory entry (WC-I-0341), and no cell cites it. CM-CAT-007's WooCommerce cell holds only `extension-point` (a Marketplace category), so it would gain `core`.
- **The product taxonomies' permissions** (`includes/class-wc-post-types.php`, lines 130 to 133, 176 to 179, 217 to 220 and 307 to 310): `manage_product_terms`, `edit_product_terms`, `delete_product_terms` and `assign_product_terms` gate product categories, tags, shipping classes and attributes. These are leads for CM-CAT-003, CM-CAT-006, CM-SHP-001 and CM-CAT-002, whose cells hold `core` already. I read the file only to see what the entries' `_terms` permissions name; I didn't place it.
- **The Attributes submenu** under Products (`class-wc-admin-menus.php`, line 101), gated by `manage_product_terms`. It is a menu with no entry, and a lead for CM-CAT-002.
- **The features defined in other classes:** `CustomOrdersTableController` and `CostOfGoodsSoldController` add definitions of their own (`FeaturesController.php`, lines 281 and 282). They aren't in this structure. CM-ORD-001 and CM-CAT-012 already cite them.
- **wc/v3's settings controllers** (WC-S-0111, WC-S-0112) are cited by no cell. A lead for CM-API-001 or CM-ACC-006.
- **The Features page's own header,** 'Start using new features that are being progressively rolled out to improve the store management experience.' (`FeaturesController.php`, line 1437). A lead for CM-EVO-001's reading.

## Problems with the brief or the script

- **`show --meta` printed nothing** for these four structures. They are `release:` structures with no `meta.json`. Their source is the release's file in each entry's `source`, which I read.
- **The checker tests `terms` against the item's text,** and the items leave most descriptions out (above). So a second thing named only in a description, such as the mobile apps of Point of Sale or the themes of Marketplace, can carry only the feature's id and name as its terms.
- **The checker rejects a double quote in a field,** so readings that would quote a PHP string with one describe it instead.
- **B-extent and this brief** read the same on everything here, as far as I found. The one tension is the ruling on a released flag against the two cells' readings of a released feature with no toggle (above). It is within the brief's rulings, not B-extent's.

## The coordinator's check (30 October 2026, after the batch)

- **Order Fulfillments and Cart & Checkout Blocks are defined alike, so their flag lines are alike: `shows`** (ruling). Both are `is_experimental` false and `disable_ui` true, and both leave `enabled_by_default` at its default, false (`FeaturesController.php`, lines 339 to 345 and 604 onwards; the defaults at line 229). Released, but off by default with no toggle in the admin, so the platform doesn't offer them to merchants to turn on. CM-SHP-009 already reads Order Fulfillments so. Cart & Checkout Blocks' two lines are now `shows`. CM-CHK-001's WooCommerce cell stays `core` on its other evidence, the Store API's checkout endpoints and the guest-checkout setting. Its reading of the flag as released goes to the final review, with this line.
- **WooCommerce > Extensions also takes CM-APP-002,** the app store: its function's deprecation note calls the page 'The marketplace feature'.
- **The Settings page's line on CM-APP-006** stands: that cell cites the same page (WC-S-5430), as rule 2 asks.
- **No cell changes.** The release's own lists confirm what the model holds for WooCommerce, which is what a release read twice should do.
