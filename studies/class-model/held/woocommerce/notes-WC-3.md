# Notes: held pass, WooCommerce, batch WC-3 (`core-profiler-free-extensions`, end; `options`, start)

**What the batch holds:** 195 entries.
- **8 of `core-profiler-free-extensions`:** the rest of the item labelled EG (items.jsonl line 7, other-product-class@0d79b794f:woocommerce/structures/core-profiler-free-extensions/items.jsonl): its bundle obw/core-profiler (WC-E-2ff8e034) and its seven plugins (WC-E-ac0481a4 to WC-E-385a7b40).
- **187 of `options`:** the store's options table, rows `wc_blocks_db_schema_version` to `woocommerce_ship_to_destination` (other-product-class@0d79b794f:woocommerce/raw/runs/20261029T023745Z-db-after-country-change/options.tsv, by the selection's rule `^(woocommerce|wcpay|wc_|_wc)`).

**No batch has placed `options` before this one.** WC-4 holds its other 50 entries, from `woocommerce_shipping_*` on, then `payments-providers`. WC-4 hasn't run, so I read no placements of it; the coordinator aligns the two. The things WC-4 will meet again are the same settings pages: General, Products, Shipping, Accounts & Privacy, Emails, Advanced and Tax. Their placements here are in the table under "How the options were decided".

**Count:** 195 entries, 237 lines.
- **By entry:** 147 have only `capability` lines, 1 has a `new` line beside its capability lines (Jetpack, as WC-2), 3 are `new` only, and 44 are `out`.
- **By line:** 189 `capability`, 4 `new`, 44 `out`.
- **By supports, on the 193 lines that aren't out:** core 137, shows 34, own-service 14, extension-point 5, extension-point;shows 2, outside 1.

## The EG item's rest (8 entries): as WC-2

- **I read WC-2's placements and its notes to the end**, its coordinator's rulings included.
- **Checked:** items.jsonl lines 6 (YE) and 7 (EG) hold the same `answer` file, `b714f634…json`, and the same `bundles`, compared field by field with `python3 -I`.
- **So each EG entry takes the YE entry's lines** for the same bundle and plugin (WC-E-b42904aa, WC-E-7f863f6e, WC-E-edc29269, WC-E-eacd2a00, WC-E-1dc47c8c, WC-E-f2e277b5, WC-E-a9263e9f, WC-E-bb7e24b8), with scope `YE`.
  - Each keeps the YE entry's reading, with the reason added: the run's POST of EG was refused, `rest_setting_value_invalid`, so the store stayed at YE.
  - That includes PayPal Payments' CM-PAY-011 line, as the coordinator ruled after WC-2.
- **Egypt's list isn't held.** A capture that sets an Egyptian state would hold it. That is a gap for the market subjects, as the evidence map says.

## How the options were decided

**What an option is.** Each option is one store's value of something WooCommerce, WooPayments or WordPress keeps. I placed them by the rules in rule 2's "out" and its "A setting, feature, flag…" paragraph:
- **Out (44):** a schema or database version, a migration's done-marker, a cache, a stored state or count, an install, activation or opt-in time, an id or key.
- **Placed on its capability:** a setting, a feature's flag, a gateway's or a shipping method's settings, an endpoint. The store's value goes in `reading`, never in `quality`.

**Scope: left empty for every option.**
- The structure gives its entries no label (`labels` is `.`), and the options are one store's: the capture's test store (`index/instruments.json`).
- A setting that every WooCommerce store has isn't stated "for" this store, so I wrote the store's value in each reading and no scope.
- **The one exception:** `wcpay_recommended_payment_methods` states its own country, `__country_code JP`, which is its lines' scope.
- If the coordinator wants the store as scope, it is the same store for every line.

**What each option is, read in the release.**
- The option names don't say what the settings are. So, to clarify an entry only, I read each option's own title and description where the release's settings classes declare it, and each feature flag's definition (`name`, `is_experimental`, `enabled_by_default`) in `src/Internal/Features/FeaturesController.php`.
- The release is the one `evidence/product-class/woocommerce-11.2.1/` fixes by checksum, unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`.
- Each reading cites the file and lines, as `woocommerce-11.2.1:<path>, lines …`, and quotes them exactly.
- `terms` come only from the entry's own text: the option's name, and the visible part of its value.
- I traced nothing further: no conditions, hooks or callers.

**Flags (`woocommerce_feature_*_enabled` and the flags with their own option keys).**
- I read each flag's release state in FeaturesController, as the ruling on flags asks.
  - `'is_experimental' => true` gives `shows`, whatever the value. That covers Save for Later, Back in Stock Notifications, MCP, Clear Customer Sessions, product gallery videos, Cache Product Objects (whose value is `yes`), REST API Caching, colour swatches, HPOS full-text indexes, Wishlists and Unified block editor assets.
  - `false` is a released flag: `core`, with the value in `reading`. That covers Blueprint, cost of goods sold, Customer review request, Deferred emails, Email improvements, Order Attribution, Order withdrawal, Rate limit Checkout, Remote Logging and HPOS Data Caching.
- **Block Email Editor (alpha)** states no `is_experimental`, so I read it by its value, `no`: `shows`.

**The settings and where they went.**

| Settings | Capability | Supports |
| --- | --- | --- |
| Downloadable products settings, the approved directories' mode, file download method, the My account Downloads endpoint | CM-SEL-002 | core |
| Selling location(s) and its "all except" list | CM-MKS-001 | core |
| Shipping location(s) | CM-MKS-001, as the cell cites it as shipping's | shows |
| Shipping location(s), Shipping destination, the shipping calculator, the Free shipping method's settings | CM-SHP-001 | core |
| Currency, and the Currency options section: position, separators, decimals | CM-MKS-005 | core |
| Tax settings | CM-TAX-001 | core |
| Personal data retention (completed and refunded orders, inactive accounts) | CM-TRU-005 | core |
| Erasure and bulk removal of personal data | CM-TRU-007 | core |
| The checkout and registration privacy policy texts | CM-TRU-006 | core |
| Accounts settings, My account endpoints and page, Logout | CM-CUS-010 | core |
| Guest checkout | CM-CHK-001 and CM-CUS-010, both of whose cells cite it | core |
| Checkout and cart pages and endpoints | CM-CHK-001, CM-CHK-002 | core |
| The checkout's address 2, company and phone field options, and the Customizer's "highlight required fields" | CM-CHK-003 | core |
| Every email template and sender setting | CM-NTF-001 | core |
| The low stock, out of stock and backorder notifications | CM-INV-004, CM-INV-001 and CM-NTF-002 | core |
| The Point of Sale tab's store details | CM-POS-001 | core |
| The onboarding profile | CM-ONB-004 | core |
| The onboarding profile's progress, a stored state that names the profiler's steps | CM-ONB-004 | shows |

## What differs between the items and their source: entries cut short

- **The entries' text is cut at about 480 characters** (entries.tsv). The source, options.tsv, holds the whole value, and the source governs (rule 1). This matters for:
  - WC-E-070c80d9 (`wcpay_recommended_payment_methods`);
  - WC-E-02053ee0 (`woocommerce_marketplace_suggestions`, 20,940 characters);
  - WC-E-149582cb (`woocommerce_gateway_order`);
  - WC-E-0885489e (`woocommerce_paypal_settings`);
  - WC-E-59aa9f0b (`wcpay_woopay_checkout_appearance`).
- **Where a line rests on the part that is cut:**
  - its `terms` hold only what the visible text holds, often only the option's name;
  - the source's names (Apple Pay, Bancontact, ShipStation, Zapier and the others) are in `reading`, never in `filler`, because the checker tests a filler against the entry's text;
  - each reading cites `other-product-class@0d79b794f:woocommerce/raw/runs/20261029T023745Z-db-after-country-change/options.tsv`.
- **So the fillers the source names are missing from the filler column.** For the coordinator:
  - Apple Pay, Google Pay, Alipay, WeChat Pay, Bancontact, EPS and iDEAL (`wcpay_recommended_payment_methods`, JP);
  - ShipStation, Zapier, Printful and Envia (`woocommerce_marketplace_suggestions`).
- **I decoded the values** with a PHP-unserialize reader of my own, kept in the scratchpad, never in the repository.

## Two entries read in full from their source

- **`wcpay_recommended_payment_methods` (WC-E-070c80d9), scope JP.** It holds the recommended methods fetched for `__country_code JP`.
  - Lines: the card on CM-PAY-002, `own-service`; Apple Pay, Google Pay, Alipay and WeChat Pay on CM-PAY-012, `shows`; Bancontact, EPS and iDEAL on CM-PAY-017, `own-service`, as that cell places WooPayments' local methods.
  - **The own-service lines rest on a reading:** the prefix `wcpay` is WooPayments', since the store holds WooPayments 11.2.0 (`index/instruments.json`). The maker statements are the cells' own (WC-S-0557, WC-S-0459, M-1).
  - The store's country is US:CA, so JP is presumably the last business location the country-change run set (runs.tsv names JP among its locations). That is a reading.
  - **What would settle it:** a statement held that names `wcpay_` as WooPayments' prefix.
- **`woocommerce_marketplace_suggestions` (WC-E-02053ee0).** It holds the Marketplace's in-admin suggestions: three headers, a "Discover more options" link to the admin's Extensions page, and 22 extensions.
  - **Lines:** one on CM-APP-002, `core`, as their container; then one on each suggested extension's capability.
  - **Supports, my decision against M-3's literal text, for the coordinator:**
    - The four suggestions that name a third party take `extension-point`: ShipStation, Zapier Integration, Printful and Envia, by M-3 and M-7.
    - The 18 that name no maker take `shows`, not `core`. These are Memberships, Bookings, Bundles, Composite Products, Add-Ons, Dynamic Pricing, Quantity Discounts, Wholesale, Bulk Order, Gift Cards, Product Recommendations, Table Rate Shipping, Shipment Tracking, Conditional Shipping and Payments, Pick List, AutomateWoo, Print Invoices and Packing Lists, and Subscriptions.
    - M-3 says a catalog card that names no one is `core` by what it shows. But these are separately sold extensions, and the model already places the same extensions' statements as `shows` with "no maker named": CM-SEL-001's WooCommerce Subscriptions and CM-SEL-004's WooCommerce Bookings. B-extent says to place by what the statements show, and `core` would claim that the platform itself does bookings, gift cards and the rest.
    - "the official WooCommerce extension" (Bookings, Gift Cards) names no maker.
    - **What would settle it:** the coordinator's reading of M-3 for an extension marketplace's suggestions. If it is `core`, the 18 `shows` lines become `core` with no other change.
  - "It's a paid annual extension with a 30-day money-back guarantee" (Bookings, Gift Cards, Subscriptions) is a price statement. It is in `reading`, not `quality`, since the visible text doesn't hold it.

## New things

No WooCommerce place of its own for any of these: each is one feature flag. All are proposed for the coordinator's decision with the others.

| new | entries | place of its own | proposed domain / area / parent (a reading) | name (English; WooCommerce is held in English only) | terms searched |
| --- | --- | --- | --- | --- | --- |
| `new:backups` | WC-E-a21963fb (EG, scope YE). Jetpack: 'Keep your store online with full security and backups' | none: a line of a card | G OPS; parent CM-OPS-001 | backups | as WC-1 and WC-2: backup; backups; restore; downtime |
| `new:Unified block editor assets` | WC-E-2d05854b (`woocommerce_feature_block_editor_unified_assets_enabled`, no; experimental, FeaturesController.php lines 709 to 714) | none: one flag | G OPS, or out as the software's own loading of its editor's assets. What it does isn't stated beyond its name | Unified block editor assets | caps: performance; cache; caching; session (no capability; CM-SFR-002 is the theme editor, not the block editor's assets) |
| `new:Clear Customer Sessions When Empty` | WC-E-0b24dc60 (`woocommerce_feature_destroy-empty-sessions_enabled`, no; experimental, lines 624 to 630) | none: one flag | G OPS; no parent found | Clear Customer Sessions When Empty | caps: session; sessions (finds only CM-PAY-011 and CM-POS-001, on other senses) |
| `new:Cache Product Objects` | WC-E-28fc6ec8 (`woocommerce_feature_product_instance_caching_enabled`, yes; experimental, lines 687 to 692) | none: one flag | G OPS; or beside CM-API-012, which is the API's responses | Cache Product Objects | caps: cache; caching; performance (CM-API-012 only) |

The last three could equally be `out`, as the software's own performance and storage. I placed them `new` because the release lists them as features a merchant switches on (rule 2: "A setting, feature, flag … that the platform lists for a store … is the platform's").

## CHANGES lines, and what I decided on each

**From the EG entries (WC-2's again):**
- CM-APP-011, CM-CHN-004, CM-MKT-010 and CM-TRU-019 gain `own-service`.
- Kept, for WC-1's and WC-2's reasons: `is_built_by_wc: true` under the ruling, and Jetpack's maker through WC-S-0594 and WC-S-0461.

**From the options:**
- **CM-CHK-003 becomes held, `core`** (address 2, company and phone fields, and the highlight of required fields).
  - Kept. These are WooCommerce's own settings of the checkout's configuration, the cell's "settings for the checkout's look and configuration".
  - The field options are read in `src/Blocks/Utils/CartCheckoutUtils.php`, lines 238 to 240, where the checkout block's attributes set them. That they show in an editor is a reading.
- **CM-SFR-007 becomes held, `core`** (`woocommerce_demo_store`, the Customizer's 'Enable store notice', shown as 'Store notice' across the storefront). Kept: a storefront notice bar is the cell's thing.
- **CM-SFR-013 gains `core`** (the product attributes lookup table, 'Use the product attributes lookup table for catalog filtering.'). Kept: WooCommerce's own setting of its catalog filtering, where the cell had only a Marketplace category.
- **CM-CNT-010 becomes held, `core`** (`woocommerce_permalinks`: product_base, category_base, tag_base). Kept: the format of the store's product and category addresses.
- **CM-CNT-008 gains `core`** (`woocommerce_refund_returns_page_id`, with the note 'We have created a sample draft Refund and Returns Policy page for you.'). Kept, as a reading: the platform makes the policy page.
- **CM-CAT-007 gains `core`** ('Placeholder image'; 'Match images' by SKU). Kept: WooCommerce's own settings of product images.
- **CM-PAY-014 gains `core`** (the My account endpoints Add, Delete and Set default payment method, and Payment methods). Kept, as a reading: the buyer's saved payment methods in WooCommerce's own account page.
  - What would settle it: a statement that WooCommerce itself saves them for faster checkout. Today the cell's own-service rests on WooPay.
  - If the coordinator reads the cell as Shop Pay-like services only, these lines go to CM-CUS-010 alone, where each already has a line.
- **From the Marketplace suggestions, cells that hold nothing become held:**
  - with `shows`: CM-LOY-002, CM-MKT-023, CM-SHP-017, CM-ORD-008, CM-ORD-009, CM-B2B-004, CM-B2B-006;
  - with `extension-point`: CM-AUT-001 (Zapier);
  - and CM-SHP-009 gains `extension-point` (ShipStation, as WC-1's corrected ShipStation lines).
  - Kept, as above. The B2B-004 and B2B-006 lines rest on two words of one description ('quotes', 'sales agents'): the weakest of them.

**The other NOTEs, each read:**
- Line 2 is the container obw/core-profiler, as WC-2.
- Line 5 is Jetpack's `new:backups`, whose leads WC-1 and WC-2 read.
- Line 14: CM-MKT-011 for Snapchat, as WC-2.
- Line 31: CM-PAY-025 is a lead only by "credit" in 'Credit/debit card', and no lead.

## Entries I couldn't tell, and what would settle each

- **`woocommerce_private_link` (WC-E-0ae77c90), on CM-ACC-009.** It is updated with `woocommerce_coming_soon` (`src/Admin/Features/LaunchYourStore.php`, lines 39 to 42), but what it does isn't stated. What would settle it: its setting's label in the Site visibility page (not read here).
- **`wcpay_multi_currency_store_currency` (WC-E-3bdcbba6), out as a stored state.** It could instead be CM-MKS-006 `shows`, as WooPayments' multi-currency. The cell already holds WooPayments' multi-currency.
- **`wcpay_fraud_services_data` (WC-E-b3d40570), CM-ORD-006 `outside`.** stripe and sift are named as fraud services, with no interface named. If the coordinator reads the WooPayments option as WooPayments' own statement, it becomes `own-service` with Sift as filler.
- **`woocommerce_email_from_address` and the reply-to settings, on CM-NTF-001.** CM-NTF-004's name holds "sender name", but its cell is about delivery providers, so I didn't place them there.
- **`woocommerce_default_country` (WC-E-e1bc4682), on CM-ACC-006** (the section Store Address). CM-TAX-001 also cites the store address that tax and shipping rates use (WC-S-0599). I gave it one line, on the store's details.

## For the second stage: what the sources state that no entry holds, or leads

- **WooPayments' incentive for stores that never had it:** `woocommerce_admin_pes_incentive_woopayments_store_had_woopayments` (options.tsv), a lead for CM-PAY-002's offers. The option itself is out.
- **`wc_connect_options` `tos_accepted: true`** names no service. A lead: WooCommerce Tax 3.7.3 is installed (`index/instruments.json`).
- **Zapier's suggestion** names 'plain-English store management through Claude or ChatGPT'. That is a lead for CM-AIA-004 or CM-AIA-005, as Zapier's own feature (M-8), not placed.
- **WooPay's checkout appearance** (`wcpay_woopay_checkout_appearance`) is a cache of the store's styles. It is a lead that WooPay's checkout takes the store's theme (CM-PAY-014).
- **`woocommerce_gateway_order`** lists 26 ids, each WooPayments method and suggestion among them. The gateways themselves are the `payments-providers` entries of WC-4 and WC-5, so I gave the order one line on CM-PAY-001.
- **Product Bundles' copy** ends with a no-break space ('assembled products' in options.tsv). My quote stops before it.

## Problems with the brief or the script

- **entries.tsv cuts long option values at about 480 characters**, and the checker tests `terms` and `filler` against the cut text. A line that rests on the rest of the source can't name its filler. I named the fillers in `reading`, as the checker asks for a party known only from a source.
- **The quote check finds a quote in a run's file only if the reading cites it as `other-product-class@<commit>:woocommerce/raw/runs/…`.** `<run_id>/options.tsv`, the form the brief gives for run steps, wasn't found.
- **The checker rejects a field with a double quote in it** ("9 tab-separated fields, no quoting"). WooCommerce's own titles hold them: "From" address, "Reply-to", "verified owner", "My account". So those readings describe the titles rather than quoting them.
- **`show --meta` printed only `core-profiler-free-extensions`'s keys.** `options` is a `rows:` structure with no `meta.json`. Its source is the rule's file, which I read.
- **B-extent and this brief:** on the Marketplace suggestions I read M-3 against B-extent's "place the cell by what its statements show", and followed the model's own placement of the same extensions (above). Elsewhere they read the same, as far as I found.

## The coordinator's check (30 October 2026, after the batch)

- **The My account payment-method endpoints are CM-PAY-022's, not CM-PAY-014's** (WC-E-35ed6310, WC-E-f041f9f6, WC-E-2334a807, WC-E-3bab05eb). CM-PAY-022's WooCommerce cell cites the Payment Token API, 'Users can also manage these tokens from their account settings' (WC-S-0943), and its note sets it apart from CM-PAY-014, checkout details saved for speed. The cell already places `core`, so it doesn't change, and CM-PAY-014 gains nothing.
- **The fillers the cut entries hid are in their column now.** The checker tests a line's terms and filler against the entry's whole source line as well (`whole_text`), where the build cut a long value: Apple Pay, Google Pay, Alipay and WeChat Pay (CM-PAY-012), Bancontact, EPS and iDEAL (CM-PAY-017), Envia (CM-SHP-001), ShipStation (CM-SHP-009), Zapier (CM-AUT-001) and Printful (CM-CAT-010).
- **The `wcpay_` options are WooPayments', by the release.** Its WooPayments provider reads `WCPAY_VERSION_NUMBER` and calls `wcpay_get_container` (`src/Internal/Admin/Settings/PaymentsProviders/WooPayments.php`, lines 63 and 579 to 582). Its welcome page names the `$skip_wcpay_active` check 'the check for the WooPayments plugin being active' (`src/Internal/Admin/WcPayWelcomePage.php`, line 60). The `own-service` line cites both.
- **The marketplace suggestions that name no maker stay `shows`,** as the batch placed them. M-3 is refined to say so (`review-H-rulings.md`): `core` is for a card of the platform's own catalog of connections.
- **The quotes and sales agents lines** (CM-B2B-004, CM-B2B-006) stand as `shows`, readings marked, since the suggestion's own words name them among a wholesale extension's features.
- **The four new things wait for WooCommerce's other batches.** Backups is WC-1's. Unified block editor assets, Clear Customer Sessions When Empty and Cache Product Objects are flags of the software's own loading, sessions and cache, which the brief's out list names ("the software's own bookkeeping: … a cache, a stored state"): `out` is the likely decision, made with the others.
