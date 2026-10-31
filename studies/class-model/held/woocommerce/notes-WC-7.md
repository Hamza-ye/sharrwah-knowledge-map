# Notes: held pass, WooCommerce, batch WC-7 (`release-settings`, start)

**What the batch holds:** 130 entries of `release-settings`, every one read from WooCommerce's release 11.2.1, the one `evidence/product-class/woocommerce-11.2.1/` fixes by checksum, unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`. Readings cite it as `woocommerce-11.2.1:<path>, lines …`. The entries come from the settings classes in `includes/admin/settings/`:
- `class-wc-settings-accounts.php` (tab Accounts & Privacy): 24 entries, lines 60 to 282;
- `class-wc-settings-advanced.php` (tab Advanced: Page setup, WooCommerce.com, REST API caching, Blueprint): 39 entries, lines 86 to 504;
- `class-wc-settings-emails.php` (tab Emails, section Email options): 27 entries, lines 107 to 365;
- `class-wc-settings-general.php` (tab General): 26 entries, lines 88 to 391;
- `class-wc-settings-payment-gateways.php` (tab Payments): 1 entry, line 161;
- `class-wc-settings-point-of-sale.php` (tab Point of Sale): 7 entries, lines 51 to 102;
- `class-wc-settings-products.php` (tab Products): 6 entries, lines 82 to 122.

The selection's rule counts the lines the concern map cites as read, so some settings of these classes have no entry here, such as `woocommerce_currency`, `woocommerce_allowed_countries` and `woocommerce_ship_to_countries`.

**No batch has placed `release-settings` before.** WC-8 holds the rest of it (with `release-webhook-topics` and `woopayments-onboarding`) and hasn't run: the coordinator aligns the two.

**Kept to the batches before.**
- WC-3 and WC-4 placed WooCommerce's `options`, the test store's values of many of the same settings. I read their placements and notes to the end, with the coordinator's checks. Each setting here with the same option key takes their line's capability and supports. My readings say so ("as WC-3 places its option").
- WC-6 placed the release's features. Where a section is listed only under a feature (REST API caching, Blueprint, the email template under the block email editor), I followed WC-6's release state for that feature.
- The one place I add to their lines is the email sender settings (CM-NTF-004, below). WC-3's lines on the same options stand as they are; the coordinator may give them the same second line.

**Count:** 130 entries, 158 lines.
- **By entry:** all 130 are `capability`; none `new`, none `out`.
- **By line:** 146 `core`, 11 `shows`, 1 `core;own-service`.
- **Scope:** empty, except where the release lists a section only under a feature (below). These are the release's definitions, not one store's values, so no line carries a store's value. A setting's default, where the source states one, is in `reading`, never in `quality`. No entry states a limit, a fee or a duration of the kind `qualities.tsv` records, so `quality` is empty throughout.

## How the entries were decided

**Each setting** is placed on the capability its own title, description and section name, and on the one the WC-3 or WC-4 line of the same key holds:

| Settings | Capability | Supports |
| --- | --- | --- |
| Guest checkout | CM-CHK-001 and CM-CUS-010 | core |
| Log-in during checkout, account creation (after checkout, during checkout, on My account), account creation options (password link, generated login), My account page, every Account endpoint, Logout | CM-CUS-010 | core |
| Account erasure requests (orders, downloads), bulk personal data removal | CM-TRU-007 | core |
| Registration and checkout privacy policy texts | CM-TRU-006 | core |
| Personal data retention: inactive accounts, refunded and completed orders | CM-TRU-005 | core |
| Retain pending, failed and cancelled orders (trashed) | CM-TRU-005 and CM-ORD-012 | core |
| Checkout page, Pay and Order received endpoints, Secure checkout, Force HTTP when leaving the checkout | CM-CHK-001 | core |
| Secure checkout's 'an SSL Certificate is required' | CM-SFR-010 | shows |
| Terms and conditions page | CM-CHK-001 and CM-CNT-008 | core |
| Add, delete and set default payment method endpoints; the Payment methods endpoint | CM-CUS-010 and CM-PAY-022 | core |
| Downloads endpoint | CM-CUS-010 and CM-SEL-002 | core |
| Cart page, add to cart behaviour, AJAX add to cart | CM-CHK-002 | core |
| Usage Tracking, Enable tracking | CM-TRU-021 | core |
| Marketplace suggestions, Show Suggestions | CM-APP-002 (and CM-PAY-001 for Show Suggestions) | core |
| REST API response cache, its notice and its two settings | CM-API-012 | shows (below) |
| Blueprint's slot | CM-MIG-006 | core |
| Every email notification, sender, template and colour setting | CM-NTF-001 | core |
| The email sender options: From name and address, Reply-to | CM-NTF-004 as well | core (below) |
| Address autocomplete, preferred provider | CM-CUS-009 | core (and own-service, below) |
| Store Address and its lines | CM-ACC-006 | core |
| Sell to all countries except, sell to specific countries | CM-MKS-001 | core |
| Ship to specific countries | CM-SHP-001 core, CM-MKS-001 shows | |
| Default customer location | CM-MKS-004, MaxMind its filler | core |
| Enable taxes | CM-TAX-001 | core |
| Enable coupons, sequential coupon discounts | CM-MKT-002 | core |
| Currency position, separators, decimals | CM-MKS-005 | core |
| Point of Sale's store details | CM-POS-001 | core |
| Shop page | CM-CAT-001 (and CM-CNT-010 for 'product permalinks') | core |
| Placeholder image | CM-CAT-007 | core |

**Containers (rule 3, M-13).** Each section's title entry (`type: title`, or the email colour palette's own type) is a container. It goes on the capability its title names, as the cells' readings show, and each reading names its children:
- **Two sections have an empty title:** `account_registration_options` (Accounts & Privacy) and `checkout_process_options` (Advanced). Each goes on the capability its id and its tab name: CM-CUS-010 and CM-CHK-001.
- **Page setup** takes CM-CHK-001 `core`, since its words name checkout, and CM-CNT-003 `shows`, since that cell cites the same section as `shows` (WC-S-0022).
- **Taxes and coupons** names two things, so it takes two lines: CM-TAX-001 and CM-MKT-002.
- **Store Address's** description, 'Tax rates and shipping rates will use this address.', names two things more. They take CM-TAX-001 and CM-SHP-001, whose cells cite the same address (WC-S-0599).
- **Privacy policy** names the privacy page that must be set: a link to WordPress's `options-privacy.php`. It takes CM-CNT-008 `shows`, since CM-TRU-005's note gives the store's privacy policy page to CM-CNT-008, and WordPress sets the page, not WooCommerce.
- **General options** names only a grouping. It goes on CM-ACC-006, the store's general settings, the tab General's thing.

**Section ends: placed as their section, a choice for the coordinator.**
- 22 entries are `type: sectionend`, the marker that closes a section, naming it only by its id. I placed 20 on their section's capability, with the section's main line (both lines for Taxes and coupons and for Email sender options).
- Reading them as "a layout node that names nothing" (`out`) would be defensible too. They hold no setting, but each names its section's id, and the brief keeps a container from `out`.
- No cell changes either way: every one of these cells holds the same section's title line. If the coordinator rules them `out`, only the `placement` and `reading` columns change, the same way for all 20.

**Two section ends have no section of their own:**
- **`email_recipient_options`** (emails.php, lines 117 to 120) closes a section that no title in the list opens. It names email recipient options by its id only, so I placed it `shows` on CM-NTF-001.
- **The Payments tab's default section** (`payment_gateways_options`, payment-gateways.php, lines 153 to 163) is an empty title element and its closing marker. The source says 'this is needed as <table> tag is generated by this element, even if it has no other content.'. I placed it `core` on CM-PAY-001, the Payments tab's own section, which the cell cites (WC-S-0005, WC-S-0029). `out`, as a layout node, would also fit: see "Entries I couldn't tell".

**Listing conditions taken as scope (M-11).** The release lists three groups of settings only under a feature, so the feature is their scope, in the release's identifiers:
- **`rest_api_caching`:** the section REST API caching is listed only while the feature is enabled (advanced.php, lines 54 to 57). Its 5 entries are 58 to 62.
- **`blueprint`:** the Blueprint (beta) section is listed only while the feature is enabled (lines 67 to 69). Its 1 entry is 63.
- **`block_email_editor not enabled`:** the email template and colour palette settings are listed only while the block email editor is off (emails.php, lines 87, 202 and 203). Their 17 entries are 74 to 90.

Conditions on the store's own site or plugins go in `reading`:
- whether the site already runs on HTTPS, which hides Secure checkout;
- whether a block theme or the checkout block is in use, which shows or hides delayed account creation and the generated login;
- whether an object cache is in use, which shows the REST API cache notice;
- how many address providers are installed, which lists the preferred provider.

**REST API caching's settings are `shows`.**
- Their section is listed only while the feature `rest_api_caching` is on. The release marks that feature `'is_experimental' => true`, off by default (`src/Internal/Features/FeaturesController.php`, lines 649 to 662), as WC-6 places it.
- By the ruling on flags, an unreleased feature is `shows`, so I read the settings it alone lists the same way.
- CM-API-012's cell already holds `core`, on the section (WC-S-0024), so no cell changes. Its reading of the section as `core` is the coordinator's to align with this.

**Blueprint's slot is `core`.** The feature `blueprint` is released, on by default, with a beta badge (WC-6; ruling, D1).

## Where the items and the source differ: the source governs

- **The pattern.** The items give many entries the fields of their neighbours: a title, description, tooltip or type that, in the source, belongs to the array before or after the one whose `id` the entry carries. 51 entries are affected, at least, and each such reading says so.
- **Examples:**
  - WC-E-aa2af11c, the first section of Accounts & Privacy, has an empty title in the source (accounts.php, lines 57 to 61). Its item gives it guest checkout's title, description and tooltip.
  - WC-E-a5c61085 (`woocommerce_delete_inactive_accounts`) carries its section's title, 'Personal data retention'. Its own title is 'Retain inactive accounts ' (line 218).
  - section ends, such as WC-E-01594d63 (`account_registration_options`), carry the next section's title.
  - WC-E-a8deda39 (Cart page) carries the next setting's type.
- **Fields the items leave out.** The items also leave out the descriptions that the source builds with `sprintf`, or with a variable:
  - delayed account creation's tooltip;
  - the Email notifications section's description;
  - the REST API cache notice's text;
  - Address autocomplete's tip naming WooPayments.

  I read each from the source.
- **What the checker can test.** It tests `terms` against the item's text, so I took terms only from what the item holds. Where the item gives an entry another field's title, its terms are its id and the words that are its own, so the corrected titles aren't terms:
  - 'Retain inactive accounts ' (WC-E-a5c61085);
  - 'Enable AJAX add to cart buttons on archives' (WC-E-fe8b62e0);
  - 'Logo' (WC-E-e9f50255).
- **`show --meta` printed nothing** for this structure. It is a `release:` structure with no `meta.json`, and its source is the release file each entry's `source` names, which I read.

## New things

None. Every entry's thing is held by a capability of the model.

## CHANGES lines, and what I decided on each

- **CM-CNT-008 gains `core`** (WC-E-ac65f022, the Terms and conditions page): WC-4 places the same option so (`woocommerce_terms_page_id`). Kept, as WC-4's line, since the store's terms page is one of the store's policies.
- **CM-CAT-007 gains `core`** (WC-E-7def859f, Placeholder image): WC-3 places the same option so. 'used for placeholder images in the product catalog' (products.php, line 118). Kept.
- **CM-CNT-010 becomes held, `core`** (WC-E-d6a47eda, Shop page): its description, 'The base page can also be used in your' 'product permalinks', links WordPress's `options-permalink.php` (products.php, line 87). WC-3 places WooCommerce's permalinks option (`woocommerce_permalinks`, product_base and the rest) on CM-CNT-010 `core`, so the cell changes from WC-3's line already, and this one agrees with it. It is a reading that the shop page's role in the product addresses is the URL structure's.
- **CM-SFR-010 becomes held, `shows`** (WC-E-fc1d6dfd, Secure checkout): 'Force SSL (HTTPS) on the checkout pages', '(… an SSL Certificate is required)' (advanced.php, line 182). The certificate is the merchant's to obtain, and no statement held says WooCommerce provides one. So the line shows SSL on the store's pages and supports no placement. The cell becomes `not-stated`, not `core`.
- **CM-CUS-009 gains `own-service`** (WC-E-7388111e, Address autocomplete):
  - where no provider is available, the setting's tip reads 'Requires a plugin with predictive address search support', 'e.g.' WooPayments, linked to woocommerce.com/products/woocommerce-payments (general.php, lines 82 to 85);
  - WooPayments' maker is held, 'designed by Woo for Woo' (WC-S-0557), as WC-4 and CM-PAY-002's cell read it (M-1);
  - so WooPayments is named as a group company's extension that provides the predictive search, beside the extension-point the cell already holds (WC_Address_Provider, WC-S-0919);
  - the tip shows only where no provider is installed, a condition on the store's own plugins, which goes in `reading`.
- **CM-NTF-004 becomes held, `core` and `shows`** (8 entries): two readings, each marked.
  - **`core`, the Email sender options** (WC-E-45a7fbc7 and the From name, From address and the three Reply-to settings, with the section's end):
    - the section's words are 'Set the name and email address you'd like your outgoing emails to use.' (emails.php, line 124);
    - CM-NTF-004's name includes the sender name, its Shopify cell is `core` on the SMS Sender ID, and its Zid cell on the sender name;
    - so the name and address the store's emails go out under is the cell's thing (M-6: each setting is a kind of the section's thing);
    - WC-3 placed the From address and the Reply-to options on CM-NTF-001 only. Its lines stand, and the coordinator may add this second line to them.
  - **`shows`, the Email notifications section's description** (WC-E-64be89b4), which the item leaves out:
    - 'To ensure your store&rsquo;s notifications arrive in your and your customers&rsquo; inboxes, we recommend connecting your email address to your domain and setting up a dedicated SMTP server.', and, if sending fails, the WP Mail Logging Plugin or the Email FAQ page (emails.php, lines 79 to 84);
    - that is the delivery of the store's emails, made the merchant's to set up, so `shows`, never `outside` (M-9);
    - it is listed only without the block email editor, and stated in `reading`, since the entry's other line holds under both conditions.

## The checker's NOTEs, each read

- **own-service on CM-CUS-009:** above.
- **First leads whose cell holds nothing, and that no line names.** Each was read, and none is the entry's thing:
  - **CM-ORD-015 (WC-E-cc9ecc11):** 'Pending orders are unpaid' states the state of an order status. CM-ORD-015 is a payment status kept apart from the order status (its name).
  - **CM-API-010 (WC-E-ac65f022):** 'conditions', from Terms and conditions, a homonym.
  - **CM-PAY-008 (WC-E-0eb76b09):** payment terms, by the words 'payment' and 'set' only.
  - **CM-CNT-005 (WC-E-65f3ad33):** Logout's description, 'You can add this to your menus via a custom link: yoursite.com/?customer-logout=true', names the menus only as where the merchant may put the link. A lead for the second stage (below).
  - **CM-NTF-004 (the email sender entries):** now placed, above.
  - **CM-AIA-003, CM-APP-004, CM-ACC-004 (the business address lines) and CM-INV-005 (the selling countries):** by their words only.

## Entries I couldn't tell, and what would settle each

- **The 20 section ends,** placed as their sections, or `out` as layout nodes: a ruling on `type: sectionend`, made once for WC-7 and WC-8.
- **WC-E-c1880972** (`payment_gateways_options`): an empty element 'needed as <table> tag is generated by this element'. I placed it `core` on CM-PAY-001 as the Payments tab's default section. `out`, as a layout node that names nothing, settles it otherwise, with the same ruling.
- **REST API caching's settings,** `shows` here by the experimental feature they are listed under, against the cell's `core` on the section: the coordinator's alignment of CM-API-012's reading.
- **The email sender options on CM-NTF-004:** a reading on the cell's name and its other platforms' sender names. If the coordinator keeps CM-NTF-004 to delivery by providers and apps, those 7 lines drop, and only the delivery advice's `shows` remains.
- **The Point of Sale's 'email receipts'** (WC-E-33af695b, 'Details about the store that are shown in email receipts.'): placed on CM-POS-001 only, since they are the point of sale's receipts. No capability of the model is receipts:
  - the search found CM-ORD-008 (order invoices, with Shopify's Invoice and receipt apps category);
  - and CM-NTF-001, since the receipts are emails.

  A held statement saying what a POS receipt is, and when it is sent, would settle it.

## For the second stage: what the sources state that no entry holds

- **The Advanced tab's own sections:** Page setup, REST API keys, REST API caching (under `rest_api_caching`), Webhooks, Legacy API (only 'when an extension has hooked into the `woocommerce_settings_rest_api` filter') and WooCommerce.com (advanced.php, lines 49 to 66; 406 to 426). The Legacy API section is 'an extension point'.
- **The Emails tab's section label** 'Email options' (emails.php, lines 67 to 70), and the email list field with no id (line 110).
- **Delayed account creation's tip** links the site editor's Order confirmation template, 'Customize messaging %1$shere%2$s.' (accounts.php, lines 84 to 89): a lead for the storefront's templates (CM-SFR-002).
- **Logout's description** names the store's menus (advanced.php, line 328): a lead for CM-CNT-005, whose WooCommerce cell holds nothing.
- **The email template's** 'Previewing new template designs' notice, and the 'Revert to legacy template' confirmation, 'Doing so will erase any changes you’ve made to your new email templates' (emails.php, lines 902 to 960), for the email improvements feature (CM-NTF-001).
- **The REST API cache notice** names Redis and Memcached as object cache plugins (advanced.php, line 452): a lead for the cache's providers, not in the item, so not a filler.

## Problems with the brief or the script

- **The items' fields are misaligned** for about 51 of the 130 entries (above). The checker's `terms` test reads the item, so it accepts the misattributed titles as terms and rejects the corrected ones. The structure's build would need to read each array's own keys.
- **The checker rejects a double quote in a field,** so titles such as the From name's and the Reply-to name's are described, not quoted, and aren't terms.
- **`show --meta` prints nothing** for a `release:` structure (as WC-6 found).
- **B-extent and this brief** read the same on everything here, as far as I found.

## The coordinator's check (30 October 2026, after the batch)

- **The misaligned fields were the build's, and are fixed.** `release_items` read each setting's title, description, tip and type from the 8 lines before its `'id'` and the 10 after, so it often took a neighbour's. It now reads only the setting's own `array( … )`, the lines at the id's depth between the array's opening and its close. The rebuild changes 95 of `release-settings`' entries, 75 in this batch and 20 in WC-8, and loses no other. Each old entry maps to its new one by its file and line, and this batch's lines and the WC-7 and WC-8 lists now name the new ids. The batch checks with 0 problems against them. A reading here that speaks of an item carrying a neighbour's field describes the entry before the fix: the source still governs, and the entry now agrees with it.
- **The 22 section ends are `out`.** Rebuilt, each names only its section's id and `type: sectionend`, a layout node that names nothing (the brief's out list), and its section's own entry holds the place.
- **The email sender options are CM-NTF-004's, as this batch read them:** that capability's own name holds the sender name, and its Shopify and Zid cells are `core` on it. WC-3's four From and Reply-to option lines take the same second line, citing the section's 'Set the name and email address you'd like your outgoing emails to use.' (`includes/admin/settings/class-wc-settings-emails.php`, line 124).
- **REST API caching's settings stay `shows`,** under an experimental feature, as WC-6 places it. CM-API-012's WooCommerce cell reads the section `core`, which goes to the final review with these lines.
