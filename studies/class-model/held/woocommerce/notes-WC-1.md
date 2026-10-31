# Notes: held pass, WooCommerce, batch WC-1 (`core-profiler-free-extensions`, entries 1 to 75)

**What the batch holds:** the first 75 entries of `woocommerce/core-profiler-free-extensions`. That is items.jsonl lines 1 to 3, the free extensions the set-up offers for a store in US:CA, GB and AE (other-product-class@0d79b794f:woocommerce/structures/core-profiler-free-extensions/items.jsonl). Each country has five bundles (obw/basics, obw/grow, task-list/reach, task-list/grow, obw/core-profiler) and their plugins.

**The rest of the structure:** WC-2 and WC-3 hold items.jsonl lines 4 to 7 (SA, OM, YE, EG). All four lines carry the same answer, `answers/.../b714f634...json`. No batch before this one placed this structure, and WC-2 and WC-3 haven't run yet, so this batch read no placements of theirs. The coordinator aligns them. The same extensions should take the same lines, except where the text differs (PayPal Payments "in full" rather than wallet-only, per `index/runs.tsv`).

**Count:** 75 entries, 156 lines.
- By entry: every entry has at least one `capability` line. No entry is `out`. Three entries' lines are `new` beside their capability lines.
- By line: 147 `capability` and 9 `new`.

## How the runs were decided (rule "a run of entries of one kind")

- **Bundles (15 entries)** are containers whose titles name no capability: Get the basics, Grow your store (three bundles carry this title), Reach out to customers. They go on CM-ONB-004 with `core`, because CM-ONB-004's cell already cites the resource they come from, `wc-admin > onboarding/free-extensions` (WC-S-0196), "for suggesting free extensions" (rule 3; M-13). Each bundle's reading lists its plugins.
- **`is_built_by_wc: true`.** This applies to WooPayments, WooCommerce Shipping, Google for WooCommerce, Pinterest for WooCommerce, MailPoet, WooCommerce Tax, Snapchat Ads, Reddit Ads and ShipStation.
  - Each takes an `own-service` line on what it does, citing `woocommerce-11.2.1:assets/client/admin/chunks/3799.js` and `DefaultFreeExtensions.php`, line 123 (the ruling).
  - Each also takes an `own-service` line on CM-APP-011, apps made by the platform's company. The field is a statement, shown to merchants, that WooCommerce makes the extension. CM-APP-011's cell says "Which extensions are Woo's isn't held as a list", and this list fills part of that gap.
  - The venue each one names (Google, Pinterest, Snapchat, Reddit) is its filler (M-3). The carriers WooCommerce Shipping names (USPS, UPS, DHL) and ShipStation are fillers too.
- **Jetpack (6 entries)** has `is_built_by_wc: false`, which names no maker. The maker comes from held statements instead (M-1): CM-ACC-010's maker evidence names Automattic "the creators of WordPress.com and Jetpack" (WC-S-0594), and Automattic is of the group (WC-S-0461; the checker's `GROUP`). So Jetpack's lines are `own-service`, on:
  - CM-TRU-019 (security);
  - CM-APP-011;
  - the `new` things speed and backups;
  - and, uncertain, CM-OPS-001.
- **Third parties' extensions:** Klaviyo, Mailchimp, Meta Ads & Pixel by Kliken, PayPal Payments for WooCommerce, Print on Demand with Printful. Each has `is_built_by_wc: false`, so no maker is stated. Each is a third party's solution in the platform's own list of extensions to install, and its words name that third party as doing the work, so it is `extension-point` with the third party as filler (M-3, M-7). The missing maker statement is a gap (see below).
- **Scope:** each entry's `within` country, in the source's identifiers: `US:CA`, `GB`, `AE`. The run sets the store's country before each call (`index/runs.tsv`, run 20261029T024814Z-free-extensions-en).
- **Store state:** each store's `is_installed` and `is_activated` go in `reading`, never in scope or quality. So do `is_visible`, `install_external`, `manage_url` and `requires_jpc`.

## New things

| new | entries | place of its own | proposed domain / area / parent | name (English; WooCommerce is held in English only) | terms searched |
| --- | --- | --- | --- | --- | --- |
| `new:speed` | WC-E-bccbdb22, WC-E-887e8d92, WC-E-195080a1 (Jetpack: 'Enhance speed and security') | none: a line of a card | G OPS; parent CM-OPS-003 (hosting of the store), a reading | speed | speed; site speed; page speed; performance; CDN; image optimization |
| `new:backups` | WC-E-f2fcdae0, WC-E-38af54ff, WC-E-e4991b97 (Jetpack: 'Keep your store online with full security and backups') | none: a line of a card | G OPS; parent CM-OPS-001 (continuity), a reading | backups | backup; backups; restore; downtime |
| `new:schedule posts` | WC-E-36e80b8f, WC-E-47964e58, WC-E-c489615e (Kliken: 'schedule a month of posts') | none: a line of a card | D MKT; parent CM-MKT-005 or CM-MKT-010, a reading | schedule a month of posts | social media post; social post; schedule posts; scheduling; posts; Facebook; Instagram |

Each is `shows`, because it has no place of its own (rule 2). The checker's NOTE says these entries have leads, and I read the leads' cells:
- CM-ACC-010 is the WordPress.com and Jetpack connection, not the Jetpack plugin. Its own cell says 'The Jetpack plugin is not required to use WooPayments' (WC-S-5333).
- CM-TRU-001 is sign-in security, not the site's security.
- CM-TRU-010 matches only by name (keep, product).
- CM-PLN-001 matches on 'Plans', which are Kliken's plans, not the platform's.
- CM-DVT-004 matches on free and launch, not on development stores.
- CM-MKT-005 matches on marketing: Kliken's marketing lines are on CM-MKT-010, CM-MKT-006 and CM-MKT-009.

## CHANGES lines, and what I decided on each

- **CM-APP-011 gains own-service** (44 lines). Kept. The maker statement is the `is_built_by_wc` field, which the ruling says names WooCommerce as the maker. For Jetpack the maker is Automattic (WC-S-0594, M-1). The cell's own-service until now was a reading counted once in CM-SFR-003.
- **CM-CHN-004 gains own-service** (Google, Pinterest, Reddit; 21 lines). Kept. The cell was `not-stated` because 'No statement held names the extension's maker' for Google for WooCommerce, and `is_built_by_wc: true` is that statement. Pinterest's cards ('make your entire product catalog browsable', 'Showcase your products with Pinterest') and Reddit's ('sync your products') are listings and feeds for a channel, which is a reading. The basics card for Google names only 'Drive sales with' and the extension. It lands here on the cell's own term, Google for WooCommerce (rule 2: a cell's reading that cites the same term).
- **CM-MKT-010 gains own-service** (Google, Snapchat Ads, Reddit Ads; 12 lines). Kept: each card names ads on the venue, and each is built by WooCommerce.
- **CM-MKT-009 becomes held, extension-point** (Kliken; lines 30, 82, 136). Kept. The card's own name, 'Meta Ads & Pixel by Kliken', names a pixel. The cell searched Meta and Facebook but not this list.
- **CM-TRU-019 gains own-service** (Jetpack; 6 lines). Kept: 'security' for the store, by Automattic's Jetpack. CM-TRU-019 is "Security and legal apps for the store". Its WooCommerce cell so far holds only the Marketplace category.
- **CM-SHP-009 gains own-service** (ShipStation, line 89). Kept, but uncertain. The card's 'Automate your order fulfillment and save on top carriers' names fulfilment, and `is_built_by_wc: true` names WooCommerce as the maker of the integration. Yet the label 'Print discounted shipping labels with ShipStation' names ShipStation as doing it. By M-8, ShipStation's own feature through the platform's integration could be `extension-point` beside the maker's line. I kept one value, the maker's, as for the venue cards. What would settle it: a ruling on whether a group-built integration with a third party's service is `own-service`, `extension-point`, or both.
- **CM-OPS-001 becomes held, own-service** (Jetpack; lines 41, 94, 145). Uncertain: see below.

## Entries I couldn't tell, and what would settle each

- **CM-OPS-001 for Jetpack's 'Keep your store online'** (WC-E-f2fcdae0, WC-E-38af54ff, WC-E-e4991b97).
  - Why I placed it: the words name keeping the store available, which is the capability's thing ("staying available ... through failures").
  - The doubt: CM-OPS-001 is the platform's own reliability, and these words may only state why one keeps security and backups.
  - What would settle it: the coordinator's reading of whether a group company's extension that keeps a self-hosted store online is this capability. Otherwise drop these lines, leaving the store's availability to `new:backups` and CM-TRU-019.
- **Klaviyo's 'consolidated view of customer interactions'** goes on CM-CUS-001 (customer records), a reading. No capability holds a customer's interaction history as such.
- **Kliken's 'Automate Facebook & Instagram marketing'** goes on CM-MKT-006 (marketing automations), a reading resting on the word automate. The cell's own WooCommerce reading rests on the word too.
- **Mailchimp's 'Send targeted campaigns'** goes on the parent CM-MKT-005, not on CM-MKT-007: the card doesn't say email or SMS. Its 'recover abandoned carts' goes on CM-MKT-022, recovery, as CM-CHK-007's note sends recovery there. CM-CHK-007, the first lead whose cell holds nothing, is the carts' records, which the card doesn't name.
- **MailPoet's 'purchase follow-up emails'** stays a term of its CM-MKT-007 line. If the coordinator reads follow-ups as automatic messages, CM-NTF-001 (notifications) would also be a candidate.
- **Snapchat Ads' 'Reach an untapped audience'** stays on CM-MKT-010, not on CM-MKT-011. CM-MKT-011, the first lead whose cell holds nothing, is audiences the platform generates for advertising (Shopify Audiences), and the card builds none.
- **Jetpack and CM-ACC-010.** I gave Jetpack's cards no CM-ACC-010 line, although the lead shares the term Jetpack. That cell is the Jetpack connection, and its own evidence separates it from the plugin (WC-S-5333).
  - `requires_jpc: true` (WooPayments, Jetpack) may name that connection, but the entry doesn't define `jpc`. It is in `reading` only.
  - What would settle it: the release's code that reads `requires_jpc`, which this pass doesn't trace.
- **PayPal Payments for WooCommerce** goes on CM-PAY-013, the child, not on CM-PAY-012 (digital wallets) or CM-PAY-011. The key `:wallet-only` and 'PayPal Wallet' fit CM-PAY-013, which is PayPal Wallet on Shopify.

## Structures whose items and sources disagree

- **None.** For all seven lines, each item's `bundles` equals its answer file exactly (`answers/.../3e673ba9...json` for US:CA, `4558a1e0...` for GB, `44c2ac24...` for AE; checked with `python3 -I`).
- **The answers and the release's fallback list differ.** The answers come from woocommerce.com's remote specs (REGISTER: `_transient_woocommerce_admin_remote_free_extensions_specs`), not from the release's fallback `DefaultFreeExtensions.php`. The fallback's `image_url` is a local `plugins_url(...)`, and its descriptions differ in places. The ruling cites line 123 of the fallback (google-listings-and-ads) for the field's meaning. Each entry's own `is_built_by_wc` value comes from the held answer.

## For the second stage, and gaps

- **No maker is stated for the third parties' extensions:** Klaviyo, Mailchimp, Kliken, PayPal Payments, Printful (`is_built_by_wc: false`). Each card's `learn_more_link` points to a woocommerce.com product page, which the run didn't hold. Those pages would state the makers.
- **Each extension's `manage_url` names its admin page once installed:**
  - `admin.php?page=klaviyo_settings`, `mailchimp-woocommerce`, `mailpoet-newsletters`, `kliken-ads-pixel-for-meta`, `shipstation`;
  - `wc-admin&path=/google/start`, `/pinterest/landing`, `/snapchat/start`, `/reddit/setup`.

  The pages aren't held, since the extensions weren't installed. I didn't put them on CM-APP-007: the entry is the card, not the page.
- **WooCommerce Tax is offered for GB** (WC-E-a2ba4979), beside US:CA, and not for AE. CM-TAX-002's cell holds the countries WooCommerce Tax is available to (WC-S-0635). This is a lead to compare with the list, not read here.
- **WooCommerce Shipping is offered for US:CA only in this batch.** GB gets ShipStation instead, and AE neither. CM-SHP-002's cell holds '(U.S.-only)' (WC-S-0592). The entries agree with it.
- **The run's step pages** (20261029T024814Z-free-extensions-en/steps/001.text.txt and 002.text.txt) are the WooCommerce home with its admin menu (lines 1 to 60 of 002.text.txt: Home, Orders, Customers, Coupons, Reports, Settings, Status, Extensions, ..., Marketing > Overview, Coupons). That menu is `release-admin-menus`' work, so nothing is new here.

## Problems with the brief or the script

- **The checker's quote check doesn't reach the release.** It doesn't search `woocommerce-11.2.1` files, nor the concern map's statement texts: 'Built by WooCommerce' (3799.js) and WC-S-0594's words were each flagged "found nowhere held". I rewrote both as unquoted references with their files.
  - Double quotes can't stand in for them, because the TSV's "no quoting" rule rejects a field containing `"`.
- **The checker's container NOTE counts by title.** "Grow your store holds 44 other entries" joins the three bundles that share that title (obw/grow, task-list/grow, obw/core-profiler) across three countries. Each bundle holds 2, 3, 8, 10 or 11 plugins.
- **`show` truncates long entries with "…".** The full text of the longer entries (most core-profiler plugins) is only in `held/woocommerce/entries.tsv`, which I read for them.
- **B-extent and this brief read the same on every case here**, as far as I found.

## The coordinator's corrections (30 October 2026, after the batch)

- **CM-OPS-001's three lines are dropped** (WC-E-f2fcdae0, WC-E-38af54ff, WC-E-e4991b97, Jetpack). The card's words, 'Keep your store online with full security and backups', name the purpose of the two things it offers, security (CM-TRU-019) and backups (`new:backups`), and each has its line. They name no service that keeps a store available under load or through failures, which is CM-OPS-001's thing, the platform's own reliability. A WooCommerce store's availability is its host's (CM-OPS-003). A lead for the second stage: Jetpack's own product page, if held, would say whether it monitors a site's uptime.
- **ShipStation's label and fulfilment lines are `extension-point`, not `own-service`** (WC-E-0dfbe605, CM-SHP-002 and CM-SHP-009). WooCommerce makes the extension (`is_built_by_wc: true`, the line on CM-APP-011), but ShipStation prints the labels and automates the fulfilment through it, under its own account, not the platform's: a third party's own feature through the platform's interface (M-8). The ad and channel cards stay `own-service`, with their venue as filler (M-3), as BC-1's Feedonomics cards do.
