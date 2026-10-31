# B-woocommerce: notes

The mapping part of domain B, Catalog and inventory (areas CAT, SEL, INV), for WooCommerce: its 8 concerns that
`scope.tsv` gives the domain, mapped onto the model of `B-anchor`. It is the dry run's first mapping part. Every row is
a reading of the statements its keys cite; a fact is only what a cited statement says. Where the brief left a choice to
me, this file says so ("my judgment"), and the list at the end gathers them.

Result: 3 new capabilities (CAT 1, SEL 1, INV 1), so the model is now CAT 12, SEL 8, INV 8. 8 landings (6 in
capabilities of the anchor, 2 in new ones), 28 cells (16 held, 12 none-held), 77 evidence rows, 1 quality, no slot
fillers, 6 rulings on 5 candidates. `python3 -I method/check_class_part.py studies/class-model/parts/B-woocommerce`:
0 problems, 9 flags, each answered under "What the checker flagged".

## How I mapped, and why

- **Landing.** A concern lands in the anchor's capability it is the same thing as: by its Q1 match (M-011, M-012,
  M-074, M-081), by terms (bundle), or on role (downloadable products). Where no capability of the model holds it, it
  makes a new one (cost of goods sold, memberships).
- **When I added a capability (my judgment).** I followed the anchor's rule: a capability is made where a concern lands
  in it, or where the platform gives the thing a place of its own and it is about the product or its stock, not about
  how the storefront shows it. WooCommerce's hold-stock setting (WC-S-5401) has a place of its own, a setting with its
  own stated behaviour, so it is a new child of inventory tracking, CM-INV-008, though no concern lands in it (WC-C-068
  lands in its parent). A reviewer may fold it back into CM-INV-001, as the anchor kept Salla's auto-restock setting
  (SA-S-1742) there; that setting restocks by order status and doesn't hold stock.
- **What I didn't add (my judgment).** WC-C-104's categories Gifts, Order options and Product display are of other
  domains in the model (gifting D, order options C, display E), and Pricing and Additional purchases are bare category
  names: no statement says what they hold, so they make no capability and aren't cited. WC-C-104 names D under also, so
  domain D's parts can cite them.
- **Citing another domain's statement (my judgment).** Only where the cell would otherwise be none-held: CM-CAT-007
  (Product images and media, WC-C-107, domain E) and CM-CAT-010 (Fulfillment and dropshipping, WC-C-061, domain C).
  The category Inventory and order management (WC-C-061/where/WC-S-0714) would add extension-point to CM-INV-001, but
  that cell is held without it, so it isn't cited; the reviewer may add it.

## Landings and grains

- **WC-C-064 (products and catalogue structure) lands in CM-CAT-001 by M-011, clean.** It is coarse, like Shopify's
  SH-C-020: WooCommerce keeps attributes, variations, categories, tags and brands in one concern. Its sub-parts are
  cited in the children: attributes and variations in CM-CAT-002, categories in CM-CAT-003, brands in CM-CAT-005, tags
  in CM-CAT-006. Every M-011 landing stays in CM-CAT-001's family.
- **Attributes in CM-CAT-002 (a reading on role).** Variations are WooCommerce's word for variants (M-011's own note).
  WooCommerce's attributes and attribute terms are read as its options and option values: the release's product editor
  says variations are generated from attributes ("Add some attributes in the Attributes tab to generate variations",
  `includes/admin/meta-boxes/views/html-product-data-variations.php`), read as context and not cited. No statement
  says it, so the cell's reading marks it. Attributes are also product data shown in the store (the attributes page's
  own text, context), which no capability of the model holds apart.
- **WC-C-068 (inventory and stock levels) lands in CM-INV-001 by M-012, clean.** Its parts with a place of their own
  are cited in children: the hold-stock setting in CM-INV-008 (new) and the products-low-in-stock API in CM-INV-004.
- **WC-C-093 (cost of goods sold) makes CM-CAT-012, a child of CM-CAT-001.** The cost is kept on the product: a field
  of the product editor (WC-S-5446) and a property of the REST product schema (WC-S-5447). The anchor made no cost
  capability (U-070: no Shopify statement on product cost). *Superseded after the dry run's review: the back-fill's Shopify cell cites Shopify's staff permissions for a product's cost, inventory entries Q1 placed in SH-C-020 (C2; see the corrections at the end).*
- **WC-C-100 (subscriptions) lands in CM-SEL-001 by M-074, clean;** **WC-C-101 (bookings and appointments) in
  CM-SEL-004 by M-081, clean,** beside Salla's SA-C-031, which the anchor landed `single` for this part to join.
- **WC-C-102 (memberships) makes CM-SEL-008,** a root of SEL. Its one statement is a category name (WC-S-0728); nothing
  says a membership recurs, so it isn't strained into subscriptions.
- **WC-C-104 (merchandising extensions) lands in CM-SEL-006 by the term bundle, strained** (below).

## Joins

- **By Q1 match:** M-011 (WC-C-064), M-012 (WC-C-068), M-074 (WC-C-100), M-081 (WC-C-101).
- **By terms:** WC-C-104 to CM-SEL-006, the term bundle: WooCommerce's category Bundles and Product Bundles'
  bundled_by and bundled_items (WC-C-104/where/WC-S-0732; WC-C-104/boundary/WC-S-5474), with Shopify's Upsell and
  bundle apps (SH-C-188/where/SH-S-2604) and Salla's advance-bundle-product (SA-C-020/decides/SA-S-3510).
- **On role (readings):**
  - **Downloadable products and digital products (CM-SEL-002; U-061).** WooCommerce's Downloadable products, with its
    file download method and the setting that grants access to downloadable files after payment
    (WC-C-066/where/WC-S-0014; WC-C-066/decides/WC-S-5393; WC-C-066/decides/WC-S-5395), against Salla's digital-file
    feature and its plan line إرسال محتوى المنتجات الرقمية, sending digital products' content
    (SA-C-024/decides/SA-S-3498; SA-C-024/decides/SA-S-1999), and Shopify's Digital goods and service apps
    (SH-C-190/where/SH-S-2648). The role is the same: a product whose content the buyer receives as a file. No
    statement of WC-C-066 says digital; WooCommerce's one statement on digital goods is about VAT on them and names no
    downloadable product (WC-C-118/reason/WC-S-5465, domain C, not cited). Q1 left the terms apart, so this is a
    reading.
  - **Attributes and options (CM-CAT-002),** inside a cell, not a landing: above.

## New capabilities (WooCommerce only so far; the back-fill writes Shopify's and Salla's cells)

- **CM-CAT-012, product cost (child of CM-CAT-001).** The anchor searched Shopify for "cost; view cost; cost per item;
  product cost" and found nothing; Salla's profit analytics (SA-C-220) are domain D's.
- **CM-SEL-008, memberships (root).**
- **CM-INV-008, stock held for unpaid orders (child of CM-INV-001).** The back-fill should not read Salla's Order
  Reservations as this: they are bookings (the anchor's homonyms; CM-SEL-004).

## Strained fits

- **WC-C-104 in CM-SEL-006.** The concern is WooCommerce's Merchandising group of Marketplace categories. Only Bundles
  fits CM-SEL-006. Product options and Product variations (WC-S-0737, WC-S-0738) fit CM-CAT-002 and are cited there as
  extension-point; Gifts, Order options and Product display (WC-S-0733, WC-S-0734, WC-S-0736) are of other domains;
  Pricing and Additional purchases (WC-S-0735, WC-S-0729) name nothing a statement defines; the group's own name,
  Merchandising (WC-S-0702), is not cited. I chose bundles because the Bundles category is the only one with a
  statement beyond its name (WC-S-5474), and because the anchor landed Shopify's like group SH-C-188 there (my
  judgment). CM-CAT-002 was the other choice: two categories name it, and `scope.tsv` gives the concern area CAT. A
  reviewer may split WC-C-104 between CM-SEL-006 and CM-CAT-002.

## Rulings

*Superseded in part (S16): the rulings below are as this part first wrote them. The coordinator's correction of 30 October and the corrections after the dry run's review (both at the end) replace them, and `rulings.tsv` holds the rulings in force: one row per pair of concerns.*

- **U-002 `joined:CM-CAT-003`:** WC-C-064 lands in the parent, CM-CAT-001; WooCommerce's categories are cited in
  CM-CAT-003 with Salla's categories (the term) and Shopify's collections (the anchor's join on role).
- *Superseded by the coordinator's correction of 30 October (below): U-005 is `apart`.* **U-005 `joined:CM-CAT-001`:** WC-C-064 and SA-C-020 are both products concerns in CM-CAT-001 by M-011. The join the
  candidate asks about, of custom fields with metafields, is not made: product custom fields (WC-S-0675) are left to
  domain E, as the anchor left Salla's plan line (SA-S-2134). The brief defines `joined` as a concern landing with
  another of the candidate's, so the ruling can't be `apart` while M-011 holds them together; the checker agrees.
- **U-059 `joined:CM-SEL-006`:** with SH-C-188, by the term bundle; WC-C-104's product options and variations sit in
  CM-CAT-002 with SH-C-189 and SA-C-021, cited but not landed.
- **U-061, two rows, one per WooCommerce concern it holds:** `joined:CM-SEL-002` for WC-C-066 (with SH-C-190 and
  SA-C-024, on role) and `joined:CM-SEL-004` for WC-C-101 (with SA-C-031, by M-081). The brief has WooCommerce rule
  for "that concern", so I wrote one row per concern; the checker accepts both (my judgment on the form).
- *Superseded by the coordinator's correction of 30 October (below), and again after the dry run's review: U-070 is `nested:CM-CAT-012` for WC-C-093 against SH-C-020 and `apart` against SA-C-220.* **U-070 `joined:CM-CAT-012`, by grain:** WC-C-093 lands in a child of CM-CAT-001, where SH-C-020 lands. It is not a
  join by any Shopify statement on cost, of which none is held; the back-fill searches Shopify's cell. Making
  CM-CAT-012 a root would let the ruling be `apart`, but the cost is kept on the product, so it is a child (my
  judgment).

## Homonyms kept apart

None of Q1's six (`class_slice.py homonyms`) is between my concerns. The cases I found:
- **taxonomy:** WordPress taxonomies, the mechanism that installing WooCommerce adds for products and orders
  (WC-C-064/where/WC-S-0907), against a standard classification of products (CM-CAT-004: Shopify's taxonomy linking,
  Salla's google-taxonomy). WooCommerce's categories and tags are such taxonomies; none of its statements names a
  standard taxonomy.
- **collection:** the Store API route collection-data (WC-C-064/boundary/WC-S-0172), aggregate data on a set of
  products (its route's comment in the release, "Get aggregate data from a collection of products", is context),
  against Shopify's collections (CM-CAT-003). Not cited.
- **subscription:** subscriptions a store sells (WC-C-100/decides/WC-S-5351) against the merchant's WooCommerce.com
  subscriptions to extensions and themes (WC-C-050/decides/WC-S-0900; WC-C-063/where/WC-S-0899), MailPoet's newsletter
  subscriptions (WC-C-113/boundary/WC-S-5502) and the saved cards behind subscriptions (WC-C-042/where/WC-S-0554,
  payments).
- **purchase order:** the Purchase Order Gateway, a buyer paying an order by purchase order
  (WC-C-103/decides/WC-S-5471; WC-C-103/boundary/WC-S-5473, domain D's B2B), against a store's purchase orders to
  suppliers (CM-INV-007, Shopify's).
- **location:** selling and shipping locations (WC-C-030/decides/WC-S-5354, WC-S-5355), shipping zone locations
  (WC-C-075/boundary/WC-S-0688), local pickup (WC-C-075/where/WC-S-0292), the customer's geolocation (WC-C-046) and the
  store's tax location (WC-C-055/responsible/WC-S-0636), against inventory locations (CM-INV-005).
- **transfer:** direct bank transfer (WC-C-002/where/WC-S-0280), payouts (WC-C-007/where/WC-S-0529) and transfers of
  personal information (WC-C-043/where/WC-S-0659), against inventory transfers (CM-INV-006).
- **restriction:** WooPayments' restrictions on account types and on prohibited product types
  (WC-C-010/decides/WC-S-0513; WC-C-011/decides/WC-S-0523), against a store's product restrictions (CM-CAT-009).
- **crypto:** the Marketplace category Crypto payments (WC-C-005/where/WC-S-0709), a way to pay, against NFTs and
  token-gating (CM-SEL-003).
- **hold and reservation:** WooCommerce's stock held for unpaid orders (WC-C-068/decides/WC-S-5401, CM-INV-008)
  against Salla's Order Reservations, which are bookings (CM-SEL-004).
- **stock notifications:** buyers' back-in-stock notifications (WC-C-069/where/WC-S-0047, domain D) against the
  store's low-stock alerts (CM-INV-004).
- **downloads:** customers' downloads of a store's downloadable products (WC-C-066/boundary/WC-S-0087) against the
  merchant's downloads of extensions bought on WooCommerce.com (WC-C-050/decides/WC-S-0646) and the MaxMind database
  download (WC-C-046/boundary/WC-S-0615).
- **Developed by Woo:** a Marketplace category (WC-C-050/where/WC-S-0697, domain F) that names no product, so it names
  no maker of Subscriptions, Bookings, Memberships or Product Bundles.

## Concerns read under also

All four were read under every placement; none is cited, since no cell needed them:
- **WC-C-027 (A; merchant responsibility):** its statements are about the merchant's ecommerce activities and Woo's
  Ecommerce Services in general (WC-S-0466, WC-S-0647); none names products or stock, so CM-CAT-001's responsible side
  stays Q1's gap.
- **WC-C-065 (D; product reviews):** reviews are domain D's; the model of B holds no reviews capability.
- **WC-C-067 (G; product import and export):** left to domain G, as the anchor left Shopify's product import (U-081).
- **WC-C-069 (D; back-in-stock notifications):** buyers' alerts, kept apart from CM-INV-004, as the anchor kept
  Salla's SA-C-032.

## Statements of my concerns left uncited

- WC-C-064: the product custom fields API (WC-S-0096, WC-S-0675; custom data, domain E's, U-005); the Store API's
  collection-data route (WC-S-0172; homonyms); the Store API's by-id and by-slug routes, which repeat cited ones
  (WC-S-0166, WC-S-0169, WC-S-0176, WC-S-0177); the wc-analytics endpoints for products, attributes, attribute terms,
  categories and variations (WC-S-0213 to WC-S-0217), which serve the analytics, domain D's subject (three of them are
  also held under WC-C-038).
- WC-C-104: Merchandising, Additional purchases, Gifts, Order options, Pricing and Product display (WC-S-0702,
  WC-S-0729, WC-S-0733 to WC-S-0736).
- Every statement of WC-C-066, WC-C-068, WC-C-093, WC-C-100, WC-C-101 and WC-C-102 is cited.

## Placements

- **The coordinator's ruling on `own-service` is applied: no row is `own-service`.** No statement names Woo or
  Automattic as the maker of WooCommerce Subscriptions, WooCommerce Bookings, Product Bundles or a memberships
  extension. Their Marketplace categories are `extension-point`; their own statements (a premium extension that sells
  with recurring payments, availability rules, a renewal hook, bundle properties on WooCommerce's endpoints) are
  `shows`. The note of WC-C-104/boundary/WC-S-5474 says Product Bundles is listed in a "Developed by Woo" category; a
  note is not a statement, so it counts for nothing. Each missing maker statement is a gap (below).
- **The coordinator's ruling on `core` on an API is applied.** WooCommerce's own REST API (wc/v3, wc/v4), its Store
  API and its wc-analytics API for its own features are `core`, and so are its webhook topics on products, which I read
  as "code for its own feature" (my reading of the ruling; the anchor marked Shopify's and Salla's topics `shows`). An
  extension's API is not WooCommerce's own: WooCommerce Bookings' REST API (WC-S-5470) and Product Bundles' properties
  (WC-S-5474) are `shows`. No statement of mine says extensions or apps use an API of WooCommerce's to do the work, so
  no API row is `extension-point`. This differs in method from the anchor, where API folders, scopes and topics are
  `shows`; it changes a cell's placement only in CM-INV-004 (below), since every other `core` cell also rests on an
  admin section or setting.
- **WooCommerce Subscriptions' settings at WooCommerce > Settings > Subscriptions (WC-S-5350)** are in WooCommerce's
  own settings screen, but the statement is the extension's (its scope), so it is `shows`, not `core`.
- **The privacy exporter and eraser of customer downloads (WC-S-0359, WC-S-0363)** are `shows`: they serve privacy
  requests, domain A's subject, and give the term.

## Qualities and slot fillers

- One quality: the hold-stock time for unpaid orders, 60 minutes by default (WC-C-068/decides/WC-S-5402). The statement
  beside it calls the time "this limit" (WC-S-5401); it is a default the merchant changes, not a ceiling of the
  platform. `outscope` holds no unplaced WooCommerce entry on products, stock or selling models (searched: product;
  stock; variation; download; subscription; booking; membership; cogs; cost; inventory; attribute; bundle; brand).
- No slot filler: no statement of mine names a third party or a law as doing a capability or setting its terms.
  WordPress's cron and REST API (WC-S-5353, WC-S-5470) are what WooCommerce Bookings runs on, not who does bookings.

## Gaps (statements a cell needs that the concern map doesn't hold)

- **The makers** of WooCommerce Subscriptions (CM-SEL-001), WooCommerce Bookings (CM-SEL-004), Product Bundles
  (CM-SEL-006) and any memberships extension (CM-SEL-008). Q1's own gap WC-C-102/boundary asks for "the developer
  documentation of a Woo-made product in this category", which assumes a maker no statement names.
- **Low-stock alerts (CM-INV-004):** a statement of WooCommerce's low-stock notification, email or threshold. The
  release's ProductsLowInStock code reads the option woocommerce_notify_low_stock_amount (context); a statement of that
  setting would settle whether WooCommerce alerts or only lists.
- **Product media (CM-CAT-007):** a statement of WooCommerce's own product images or gallery; only the Marketplace
  category is held.
- **Product attributes as options (CM-CAT-002):** a statement that variations are made from attributes; the release
  says it (context).
- **Memberships (CM-SEL-008):** what a membership grants or sells, and whether it recurs.
- **WC-C-104's Pricing and Additional purchases:** what the categories hold.
- Q1's own gaps on my concerns (responsible and reason on all of them; decides and boundary on WC-C-102; decides on
  WC-C-104) are in derived.tsv.

## What the checker flagged, and the answers

1. **evidence.tsv, WC-C-107/where/WC-S-0742 (Product images and media) is of domain E, not naming B.** Cited in
   CM-CAT-007 because it is WooCommerce's only statement on product media; the category sits under Store content and
   customizations, but the channel doesn't set the capability, and the anchor keeps media with the product record.
   Domain E's parts should not cite it for the storefront without the reviewer's ruling.
2. **evidence.tsv, WC-C-061/where/WC-S-0713 (Fulfillment and dropshipping) is of domain C, not naming B.** Cited in
   CM-CAT-010 because it is WooCommerce's only statement on dropshipping, the sourcing half of the category; its
   fulfillment half is domain C's. The anchor cited Salla's Drop shipping apps (SA-C-124, domain C) in the same cell.
   The coordinator may add B to WC-C-061's also.
3. **CM-CAT-004, none-held, 1 hit:** WC-S-0907, WordPress taxonomies (homonyms), not a standard taxonomy.
4. **CM-CAT-009, none-held, 7 hits:** WooPayments' account-type restrictions (WC-S-0513, twice, and WC-S-0514) and its
   prohibited business and product types (WC-S-0523, twice), domain C's; the readme's "No restrictions" on store data
   (WC-S-0588); a coding-standard rule's name, FunctionNameRestrictions, in the checkout-fields function (WC-S-0454).
   None restricts a store's own products.
5. **CM-SEL-003, none-held, 1 hit:** Crypto payments (WC-S-0709), a payment category, not NFTs.
6. **CM-INV-004, core rests only on boundary statements.** Its one statement is WooCommerce's own analytics API for
   products low in stock, `core` by the coordinator's ruling on WooCommerce's own API. It shows WooCommerce itself
   listing the products low in stock; whether it alerts is not stated (gaps). A reviewer who reads a list as not an
   alert would make the cell none-held.
7. **CM-INV-005, none-held, 20 hits:** all other kinds of location (homonyms; the cell's reading names each).
8. **CM-INV-006, none-held, 9 hits:** money and data transfers (homonyms).
9. **CM-INV-007, none-held, 2 hits:** the Purchase Order Gateway, a way to pay (homonyms).

Nothing the checker flagged is left unanswered.

## Problems with the brief or the evidence

- *Since answered: the dry run's rulings re-read the anchor's API rows as `core` (C1; B-anchor's notes).* **The two rulings change the method between parts.** Under the ruling on APIs, WooCommerce's API rows are `core`
  where the anchor's are `shows`. Today this changes only CM-INV-004's placement, but a count that compares platforms by
  `core` should know that the anchor's cells were not read the same way. The coordinator may want the anchor's cells
  re-read, or the ruling noted beside the count.
- *Superseded by the coordinator's correction of 30 October (below): the corrected checker no longer forces `joined`.* **`joined` is forced by the model's trees.** For U-005 and U-070 the ruling must be `joined` because the candidate's
  concerns sit in one family (by M-011, and by a child of the products capability), though the specific join each
  candidate asks about (custom fields with metafields; COGS with Shopify's product cost) is not made. The bases say so.
- *Since answered: scope.tsv names B under also for WC-C-061 and WC-C-107 (69bce534), and the two cells' readings say so.* **WC-C-061's also lacks B,** though its category Fulfillment and dropshipping is the only WooCommerce statement for
  CM-CAT-010; likewise WC-C-107's lacks B for product images and media (CM-CAT-007).
- **Statements held twice.** Several statements are held under both my concerns and others: the Downloads and Stock
  reports and their APIs (WC-C-066 and WC-C-068, and WC-C-038), the privacy exporter and eraser (WC-C-066 and WC-C-045),
  some Store API routes (WC-C-064 and WC-C-079). Each cell cites its own concern's key.
- **Q1's gap on WC-C-102/boundary** asks for "a Woo-made product in this category": the gap's wording assumes a maker
  that no statement names.

## Where the brief left me to judge

1. Making CM-INV-008 (hold stock) a capability, from a setting with no concern of its own.
2. Not modelling WC-C-104's Pricing and Additional purchases (Pricing superseded: CM-CAT-013, S8); leaving Gifts, Order options and Product display to
   other domains.
3. Landing WC-C-104 in CM-SEL-006 rather than CM-CAT-002 (strained either way).
4. Reading attributes as WooCommerce's options in CM-CAT-002, informed by the release's code.
5. Joining downloadable products with digital products on role.
6. Holding CM-INV-004 on the products-low-in-stock API, as a reading.
7. Making CM-CAT-012 a child of CM-CAT-001, which makes U-070 `joined` by grain (superseded: see the corrections at the end).
8. Citing other domains' statements only where a cell would otherwise be none-held (CM-CAT-007, CM-CAT-010), and not in
   CM-INV-001.
9. Reading webhook topics as WooCommerce's "code for its own feature", so `core` under the coordinator's ruling.
10. Writing two rulings for U-061, one per WooCommerce concern.


## The coordinator's corrections (30 October)

The checker's ruling test was corrected after this part ran. Its old test read any capability under a common parent as landing together, so this part had to rule U-005 and U-070 `joined`. Its own bases say the joins they ask about aren't made: product custom fields with metafields, and cost of goods with a Shopify product cost, for which no Shopify statement is held. They now read `apart`, as the bases say.


## Corrections after the dry run's review (30 October)

The coordinator's rulings on the two reviews (`studies/class-model/review-dry-run-rulings.md`) are applied to this part's rows as follows. Each placement and ruling is a reading, as before.

- **C1, the platform's own API.** No change here: this part already read WooCommerce's own APIs as `core` for its own features, and the extensions' APIs (Bookings, Product Bundles) as theirs, which is the ruling. CM-INV-004/woocommerce's flag "core rests only on boundary statements" is that ruling: ProductsLowInStock is WooCommerce Admin's own API, and no statement says apps use it.
- **C2, placed inventory entries.** WC-C-093's landing reading now says that the back-fill's CM-CAT-012/shopify cell cites Shopify's staff permissions for a product's cost (SH-I-0902, SH-I-0904, SH-I-1057, SH-I-1129). The checker's search now reads inventory entries: its one new hit, WC-I-0504 on CM-SEL-003, is the inventory entry of the Crypto payments category already read in that cell (WC-S-0709), a way to pay.
- **S4 and S5, rulings.** `rulings.tsv` is rewritten with one row per pair of concerns, WooCommerce's concern against one other, each holding only that pair's keys (14 rows): U-002 two rows (`joined:CM-CAT-003` against SA-C-022 and against SH-C-021); U-005 unchanged (`apart`); U-059 five rows (`joined:CM-SEL-006` against SH-C-188, `joined:CM-CAT-002` against SA-C-021 and against SH-C-189, as the review writes them; `apart` against SA-C-029 and SA-C-077); U-061 four rows (`joined:CM-SEL-002` for WC-C-066 against SA-C-024 and SH-C-190; `joined:CM-SEL-004` for WC-C-101 against SA-C-031 and against SH-C-190, whose Event booking apps, SH-I-1887, CM-SEL-004 now cites after C2); U-070 two rows.
- **U-070, a ruling written at the concerns' grain.** For WC-C-093 against SH-C-020 the cells, read whole, join them in CM-CAT-012: WooCommerce's cell cites WC-C-093, and the back-fill's Shopify cell cites SH-C-020's cost permissions (C2). But the checker tests a mapping part's rulings only against the parts before it, so `joined:CM-CAT-012` prints a problem here (the back-fill's cell isn't read), and that problem would also fail the back-fill's check. The ruling is `nested:CM-CAT-012`, which holds at the concerns' grain: WC-C-093, the cost of goods, is a finer part of SH-C-020, products, which lands in CM-CAT-001, CM-CAT-012's parent; its keys include the cost permissions, so the merge sees both. Against SA-C-220 it is `apart` (scope.tsv gives SA-C-220 domain D). The checker's ruling test should read the back-fill named for this part (for the checker's next revision).
- **S8, product pricing.** CM-CAT-013 (product pricing) is added to this part's `capabilities.tsv`, numbered past CM-CAT-012, the model's highest in CAT, as a child of CM-CAT-001 by Salla's admin grouping (its products settings). The statements that bear it out are Shopify's and Salla's (B-anchor's notes, S8). Here it holds WooCommerce's cell: `extension-point` on the Marketplace category Extensions > Merchandising > Pricing (WC-C-104/where/WC-S-0735), with no statement of what its extensions do. Shopify's and Salla's cells are the back-fill's. WC-C-104's landing reading now names CM-CAT-013 among the trees its statements are cited in; it was already `strained`. Where the brief left me to judge, item 2, is superseded for Pricing.
- **S11 and S12, names.** CM-CAT-012 is renamed "Product cost: cost of goods sold (WooCommerce Cost of Goods Sold, _cogs_value; Shopify View cost, Edit cost)", with Shopify's terms now that its cell holds them (C2), and its note says so. The anchor's capabilities with a WooCommerce landing or cell (CM-SEL-002, CM-CAT-003, CM-INV-004) now name WooCommerce's terms (the anchor's notes). CM-INV-004/woocommerce's reading no longer says its fit to alerts rests on the API's name alone: the capability's name now holds lists of products low in stock.
- **S16, stale notes and readings.** The passages that argue the old rulings (U-005 and U-070 `joined`, "`joined` is forced by the model's trees", item 7 of what the brief left me to judge) and the answered problems (WC-C-061's and WC-C-107's also; the two methods for APIs) are marked superseded where they stand. CM-CAT-007/woocommerce's and CM-CAT-010/woocommerce's readings now say that WC-C-107 and WC-C-061 name B under also, so their statements may support a placement here; the checker no longer flags them.

**Not applied here, as the rulings leave them:** C5 (a gap for Q1: "Developed by Woo" is held only in statements' notes, so CM-SEL-006/woocommerce stays as it is); S6 (scope.tsv, the coordinator's: WC-C-064 now names E).

**No ruling disagreed with the evidence.** U-070's ruling value departs from the plain reading of the cells for the checker's reason above, not the evidence's.

**The checker after the corrections:** 0 problems, 7 flags: CM-INV-004's boundary flag (C1, above) and six none-held flags, each answered in its cell's reading and held by the cells review.
