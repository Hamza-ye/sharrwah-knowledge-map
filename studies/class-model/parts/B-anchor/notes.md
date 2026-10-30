# B-anchor: notes

The anchor part of domain B, Catalog and inventory (areas CAT, SEL, INV), from Shopify's and Salla's concerns that
`scope.tsv` gives the domain: 11 Shopify and 11 Salla. It is the dry run's first part. Every row is a reading of the
statements its keys cite; a fact is only what a cited statement says. Where the brief left a choice to me, this file
says so ("my judgment").

Result: 25 capabilities (CAT 11, SEL 7, INV 7), 22 landings, 50 cells, 220 evidence rows, 15 qualities, 2 slot
fillers, 13 rulings. `python3 -I method/check_class_part.py studies/class-model/parts/B-anchor`: 0 problems, 7 flags,
answered under "What the checker flagged".

## How I cut, and why

**The rule I used for a capability (my judgment).** The brief says a capability is something a store or the platform
can have or not have, and that the structure follows the two platforms' own groupings. I made one where:
1. a concern lands in it; or
2. both platforms show the same thing, though each keeps it inside a coarser concern (tags, media, taxonomy, inventory
   history); or
3. one platform gives it a place of its own: an admin section or route, a permission, a webhook topic, a plan line or
   an entitlement (inventory counts, NFTs, low-stock alerts, size guides, donations), and it is about the product or
   its stock, not about how the storefront shows it.

*Superseded in part after the dry run's review: automatic pricing (SA-S-1751) is now cited in CM-CAT-013, product pricing (S8; the corrections at the end).* A single feature flag was not enough on its own, and nor was a setting of how the storefront displays products. So
these parts of Salla's products concern (SA-C-020) have no capability and are not cited: product filters
(SA-S-1756, SA-S-2135, SA-S-3479), sorting (SA-S-1759, SA-S-1983, SA-S-2475, SA-S-3357), "You may also like" and
recommendations (SA-S-1749, SA-S-1979, SA-S-3181), the purchase count (SA-S-1753, SA-S-1977), sold-out products at the
end of the page (SA-S-1978), product templates (SA-S-3478), certificates (SA-S-3473), metal pricing (SA-S-3515),
automatic pricing (SA-S-1751), the product score (SA-S-3517), the sale start (SA-S-3490), the default weight and SKU
display (SA-S-3501, SA-S-3502), AI features (SA-S-3377, SA-S-3518) and product custom fields (SA-S-2134). Filters,
sorting and recommendations are how the storefront shows and finds products; custom fields are custom data (Shopify's
metafields, SH-C-028, are domain E). See "Problems" for what this leaves out of the class. From Shopify's products
concern (SH-C-020) the product scan routes (SH-S-5006, SH-S-5008, behind betas), the product import routes (SH-S-5011,
SH-S-5017) and the storefront listing scopes (SH-S-6152 to SH-S-6157) are not cited: import is domain G's (U-081), and
the scopes are the storefront's.

**The trees.**
- CAT: CM-CAT-001 Products holds options and variants (002), groupings (003, which holds the standard taxonomy, 004),
  brands (005), tags (006), media (007), combined listings (008), restrictions (009) and size guides (011). Product
  sourcing (010) stands alone: it is where products come from, not what the product record holds.
- SEL: subscriptions (001), digital products (002, which holds NFTs and token-gating, 003), bookings (004),
  pre-orders (005), bundles (006) and donations (007), each on its own.
- INV: *superseded (S2): inventory tracking (001) now holds history (002), counts (003), low stock (004), transfers (006) and purchase orders (007), and inventory locations (005) stand alone.* As first written: inventory tracking (001) holds inventory history (002), counts (003) and low-stock alerts (004); inventory
  locations (005) hold transfers (006), which hold purchase orders (007).

## Grains chosen

- **M-011 (products) is a difference of grain**, as the brief says: Shopify's one concern (SH-C-020, products and
  variants) against Salla's four (SA-C-020 products, SA-C-021 options and variants, SA-C-022 categories, SA-C-023
  brands). Shopify's lands in the parent CM-CAT-001 with Salla's products; Salla's other three land in its children.
  Every landing by M-011 sits in CM-CAT-001's family, as the checker requires.
- **Options and variants (CM-CAT-002)** is a child of products: Shopify keeps variants inside SH-C-020 (SH-S-7214,
  SH-S-5021), Salla gives them their own API folders and plan line. Shopify's App Store group for custom products and
  product options (SH-C-189) lands here; I did not make a separate "product customization" capability, since
  Shopify's own sentence puts customization among the features product variant apps add (SH-S-7214).
- **Groupings (CM-CAT-003) and the taxonomy (CM-CAT-004).** Salla's categories concern holds both its store
  categories and its taxonomy features (google-taxonomy, salla-taxonomy); a standard taxonomy is a different thing from
  the store's own groupings, so it is a child, following Salla's own grouping.
- **Tags, media, size guides (CM-CAT-006, -007, -011)** are children of products with no concern landed: both
  platforms (tags, media) or Salla alone (size guides) keep them inside their products concerns.
- **Product sourcing (CM-CAT-010)** holds Shopify's App Store group (SH-C-185) and, in its cells, Shopify Collective
  (SH-C-141, domain E), Salla's Drop shipping apps (SA-C-124, domain C) and the buying side of its wholesale market
  (SA-C-098, domain D). Only SH-C-185 lands here.
- **Selling plans stay inside subscriptions (CM-SEL-001).** The seed lists Shopify's purchase options and selling
  plans under SEL. No Shopify statement shows selling plans used for anything but subscriptions (pre-orders and
  deferred purchases have no statement), so I made no separate purchase-options capability (my judgment).
- **Bundles and pre-orders are in SEL**, as ways of selling a product (the scope part's reason for SH-C-188). Shopify's
  group SH-C-188 holds upsell, cross-sell, bundles and pre-orders; its statements are all about bundles, so it lands in
  CM-SEL-006, marked strained.
- **Digital products and NFTs.** SH-C-190 (digital goods, events and token-gating) lands in CM-SEL-002 with Salla's
  digital products by M-076; its Blockchain route (SH-S-5094) is in the child CM-SEL-003, following Shopify's own
  grouping of NFT and token-gating apps with digital goods. Its event booking part has no statement (strained).
- **Inventory (M-012) is one to one**, but both concerns are coarse: Shopify's holds history and counts, Salla's holds
  its log and its low-quantity alert. The parent CM-INV-001 takes both concerns; the children take the sub-parts each
  platform gates on its own. Shopify's four inventory entitlements (SH-S-5334: enabled, counts, purchaseOrders,
  transferLocation) mark the same cut: tracking (001), counts (003), purchase orders (007), transfers (006).
- *Superseded (S2): transfers and purchase orders are now children of CM-INV-001, by Shopify's inventory entitlement; SH-C-023 lands in CM-INV-001, and SA-C-026 is strained (the corrections at the end).* **Locations, transfers, purchase orders (CM-INV-005 to -007).** Salla's SA-C-026 holds branches, warehouses and
  inventory transfer; Shopify's SH-C-024 holds locations and SH-C-023 transfers, shipments and purchase orders (Q1's
  U-003). Transfers are a child of locations, so SA-C-026 lands cleanly in the parent. Purchase orders are a child of
  transfers because Shopify's own permission tree makes them depend on the transfer permissions
  (SH-C-023/decides/SH-S-7156: View purchase orders depends on VIEW_INVENTORY_TRANSFERS; SH-C-023/decides/SH-S-7157:
  Manage purchase orders depends on CREATE_AND_EDIT_INVENTORY_TRANSFERS) and a transfer links related purchase orders
  (SH-S-6221); so SH-C-023 lands in their parent, CM-INV-006. This dependency is Shopify's alone (my judgment): a
  reviewer may prefer purchase orders as a child of CM-INV-001, with SH-C-023 then strained.
- *Superseded (C3): Salla's plan line and Inventory audit link are now cited in CM-INV-003 as well (the corrections at the end).* **Inventory counts (CM-INV-003) apart from tracking.** Shopify gates counts by their own entitlement
  (inventory.counts), routes and three staff permissions. Salla's "Inventory audit" and its plan line جرد المنتجات
  والمخزون are read as its inventory view (CM-INV-001), not as counts, because the plan line's own description is
  tracking stock status and the numbers of products sold, remaining and nearly out (SA-C-025/decides/SA-S-2096). That
  is a reading, and the flag on it is answered below.

## Joins

- **By Q1 match:** M-011 (SH-C-020; SA-C-020 to SA-C-023), M-012 (SH-C-022; SA-C-025), M-074 (SH-C-186; SA-C-125),
  M-076 (SH-C-190; SA-C-024). M-081 (SA-C-031 with WooCommerce) holds no Shopify concern, so SA-C-031 lands `single`:
  a landing by a match needs another of its concerns landed, which WooCommerce's part will do.
- **By terms:**
  - SH-C-189 to SA-C-021 (CM-CAT-002), the term variant: Shopify's "Product variant apps" and its 100 variants per
    product (SH-C-020/decides/SH-S-7214; SH-C-189/where/SH-S-2644) and Salla's Product Variants and Product Options
    (SA-C-021/boundary/SA-S-1031; SA-C-021/where/SA-S-1025).
  - SH-C-023 to SA-C-026's transfer part (CM-INV-006), the term inventory transfer: Shopify's Transfers behind the
    inventory.transferLocation entitlement (SH-C-023/where/SH-S-1513; SH-C-023/decides/SH-S-5188) and Salla's
    Inventory transfer link and inventory_transfer permissions (SA-C-026/where/SA-S-1798;
    SA-C-026/decides/SA-S-2520).
- **On role (readings):**
  - **Collections and categories (CM-CAT-003; U-002).** Both are the store's own groupings of its products under
    different names. Shopify: a product is added to or removed from a collection by hand or by the collection's rules
    (SH-C-021/boundary/SH-S-6097), and a staff permission adds products to a collection (SH-C-021/decides/SH-S-6278).
    Salla: a product's category (تصنيف المنتج) is updated (SA-C-020/boundary/SA-S-1597); its plan line names product
    categories (SA-C-022/decides/SA-S-1974). No statement on either side defines the other's term, and Q1 left it to a
    founder ruling or a Shopify source; I joined them because the role the statements show is the same, and a model
    that kept them apart would show Shopify with no product groupings.
  - **Locations and branches or warehouses (CM-INV-005; U-003).** Both are where a store's stock is held. Shopify:
    "Inventory locations" in its plan table (SH-C-024/decides/SH-S-7010) and Settings > Locations
    (SH-C-024/where/SH-S-1493). Salla: a branch or warehouse (فرع / مستودع) in its webhooks
    (SA-C-026/boundary/SA-S-1616), branch inventories (SA-C-025/decides/SA-S-3504) and quantity by branch
    (SA-C-026/decides/SA-S-3516). Q1 asked for a Salla Branches API definition calling a branch an inventory location;
    the concern map holds none, so this stays a reading.

## Homonyms kept apart

None of Q1's six (`class_slice.py homonyms`) is between my concerns; two touch them: U-044 (logs) beside Salla's
inventory log, and U-084 (order limit) beside product restrictions. The cases I found:
- **category:** Salla's store categories (SA-C-022/decides/SA-S-1974) against Shopify's "product categories" that
  Shopify Tax reads (SH-C-100/decides/SH-S-7221, domain C). Whether Shopify's are a standard taxonomy isn't stated, so
  they are cited nowhere; Shopify's collections, not its product categories, join Salla's categories.
- **subscription:** subscriptions a store sells (SA-C-125/boundary/SA-S-1642; SH-C-186/responsible/SH-S-0762) against
  the merchant's own subscriptions to apps and themes (SA-C-195/where/SA-S-1927; SA-C-193/boundary/SA-S-1572;
  SH-C-019/boundary/SH-S-0269). Salla's app scope "subscriptions" (SA-S-1567) is held under both SA-C-125 and SA-C-191
  (app scopes), so I didn't cite it.
- **reservation:** Salla's Order Reservations are bookings (SA-C-031/where/SA-S-1779, the Bookings link to
  /orders/reservations; SA-C-031/where/SA-S-1023), not stock held for an order. A mapping part should not land stock
  reservation in CM-SEL-004.
- **bundle:** product bundles (SA-C-020/decides/SA-S-3510; SH-C-188/where/SH-S-2604) against a theme component bundle
  (SA-C-091/reason/SA-S-5033) and a compiled UI extension bundle (SH-C-144/decides/SH-S-7485).
- **transfer:** inventory transfers (SH-C-023/where/SH-S-1513; SA-C-026/where/SA-S-1798) against money transfers
  (SH-C-088/decides/SH-S-5042; SH-C-062/decides/SH-S-5246) and domain transfers (SH-C-033/decides/SH-S-5154).
- **options:** product options (SA-C-021/where/SA-S-1025) against order options the buyer fills at checkout
  (SA-C-042/where/SA-S-1019, domain C).
- **wholesale:** Shopify's "Wholesale apps" in its sourcing group (SH-C-185's platform term, no statement) against its
  "Wholesale apps" for B2B pricing (SH-C-044/decides/SH-S-7212, domain D); Salla's wholesale market has a selling side
  (SA-C-098/boundary/SA-S-5047) and a buying side (SA-C-098/decides/SA-S-2456); only the buying side is cited
  (CM-CAT-010).
- **audit and log:** Salla's "Inventory audit" (SA-C-025/where/SA-S-1803) and "Inventory log" at
  /products/quantities/audit (SA-C-025/where/SA-S-1891) against its audit logs, "Activity history" at /logs/audit
  (SA-C-010/where/SA-S-1889); and Salla's جرد (SA-C-025/decides/SA-S-2096) against Shopify's inventory counts
  (SH-C-022/decides/SH-S-7160), kept apart (CM-INV-003).
- **vendor:** the vendors a Shopify merchant pays through Bill Pay (SH-C-098/boundary/SH-S-0501) and Salla's
  wholesale-market vendors (SA-C-098/decides/SA-S-2456); neither is a product's brand or a purchase order's supplier.
- **location:** inventory locations (SH-C-024/decides/SH-S-7010) against the customers' locations Shopify Tax reads
  (SH-C-100/decides/SH-S-7221).
- **collection:** Shopify's collections against "Billing and Collection" (SH-C-002/responsible/SH-S-0008).
- **limit:** Shopify's store-wide add-to-cart limit (SH-C-046/reason/SH-S-7489) against Salla's product restrictions
  (SA-C-028/where/SA-S-1801): kept apart (CM-CAT-009).

## Strained fits

- *Updated (C2, S1): the inventory entries Event booking apps (SH-I-1887) and Pre-order apps (SH-I-1842) are now cited in CM-SEL-004 and CM-SEL-005, and both landings' readings name them.* **SH-C-190 in CM-SEL-002**, by M-076: its platform term "Event booking apps" is bookings (CM-SEL-004) and has no
  statement. Its NFT part fits the child CM-SEL-003. A reviewer may split the event part, though nothing of it is held.
- **SH-C-188 in CM-SEL-006:** its statements are all bundles (SH-S-2604, SH-S-2207, SH-S-1100), but the concern also
  names upsell and cross-sell (domain D's offers, U-057) and "Pre-order apps" (no statement; CM-SEL-005).

## Concerns read under also

Read and cited: SH-C-028 (E; SH-S-6240 for taxonomy linking and media), SH-C-141 (E; Shopify Collective,
CM-CAT-010), SA-C-098 (D; the wholesale market's plan line and buying permission, CM-CAT-010), SA-C-124 (C; Drop
shipping apps, the dropshipping endpoint and the partner policy, CM-CAT-010). Read and not cited: SH-C-037 catalogs (D;
market and B2B catalogs, not the product catalog) and SH-C-053 Cart Transform (C; its statements don't name bundles,
though their source page, per the statements' notes, is Shopify's bundles guide). The others were read only as far as
their names, terms and the search hits they gave, since no capability of mine needed more: SH-C-025 gift cards and
SA-C-077 gifting (domain D's; I made no gift-card capability in SEL, though Shopify's seed lists gift cards there),
SH-C-035 search and filters (E), SH-C-060 order routing (C), SH-C-154 and SA-C-030 reviews (D), SH-C-175 compliance
(A), SH-C-202 and SA-C-012 AI tools (F), SA-C-027 import and export (G), SA-C-032 back-in-stock alerts (D; kept apart
from CM-INV-004). Outside also: SH-C-187 (D, not naming B) is cited once, in CM-SEL-007 (flagged); SH-C-046 (C),
SH-C-079 (C) and SH-C-100 (C) are named in readings and not cited.

Other statements of my own concerns left uncited, besides SA-C-020's above: Shopify's UCP catalog search in a store's
UCP profile (SH-C-020/boundary/SH-S-2535, agent-facing, domain E's or F's), its bin details route behind a beta
(SH-C-024/decides/SH-S-5201: bins inside a location, too thin for a capability), its ServerIntent rows (SH-S-7193,
SH-S-7194, SH-S-7245, SH-S-7231, SH-S-7236, SH-S-7237, SH-S-7238), Salla's restriction-product-type flag
(SA-C-020/decides/SA-S-3351, whose meaning isn't stated; it may belong to CM-CAT-009), its product display setting
(SA-C-025/where/SA-S-1750), its print and export of inventory (SA-S-3094) and its hiding of sold-out products
(SA-S-3482).

## Placements

- The coordinator's ruling on `own-service` is applied: no row is `own-service`. "Shopify Combined Listings" (plan
  row SH-S-7071) and "Shopify Collective" (plan row SH-S-7013) carry the brand, but no statement names Shopify as the
  maker of a separate product, so both are placed `core` by their plan rows. Salla's features of type app with an
  install link, whose maker isn't stated (three-dimension-image SA-S-3475, virtooal SA-S-3476, size-guides SA-S-3461,
  manage-products-by-branches SA-S-3468), are `shows`. Each missing maker statement is a gap (below).
- `core` rests on admin sections, routes, settings, permissions, entitlements, feature flags and plan lines.
  *Superseded (C1): the platform's own API is `core` for its own feature, and `extension-point` where its statements say apps do the work.* As first written: API folders, objects, scopes and webhook topics are `shows`, so no `core` rests on boundary statements alone.
- `extension-point` rests on App Store categories (Shopify's and Salla's), Shopify's product_configuration extension
  template (SH-S-2207), the API guides that give apps their scopes (SH-S-6257, SH-S-6286), the fulfillment-service
  apps that edit their own locations (SH-S-6206, a reading; fulfillment services are domain C's), Salla's endpoint for
  dropshipping applications (SA-S-0179), and SA-S-0195, where authorized third-party apps can enable recurring
  payments (a reading: enabling it through the API is the apps' part). *Superseded (C6): SA-S-0195 is now read `core`, and the Recurring Payments API and its webhooks `extension-point`.*
- *Superseded (C1): both cells are now `core` on Shopify's own API.* Two cells hold statements with no placement (`not-stated` in derived.tsv): CM-CAT-004 for Shopify (taxonomy linking
  named in a scope line) and CM-CAT-006 for Shopify (the product-tags scope).
- *Superseded (C4): the route is the app's page, `extension-point`.* CM-SEL-003 for Shopify is `core` by the rule (its own admin section and route), though the route needs the apps
  permission (SH-S-5095), which reads as a page apps fill; a reviewer may prefer `shows`.

## Qualities and slot fillers

- Three qualities are unplaced inventory entries with no value in the concern map: maxProductVariants (SH-I-2520) and
  maxProductOptions (SH-I-2519), store resource limits, and tagsPerProductLimitEnabled (SH-I-2598), a store feature
  key. The structure that holds their values is the stores' resourceLimits and features in Shopify's admin answers;
  Shopify's `notes.md` keeps the values per store under "Unplaced keys". A gap: they would be statements once tied to a
  concern. SH-C-020/decides/SH-S-7214's note records that the built-in feature page's 100 variants differs from the
  maxProductVariants value (2048); the note is not a statement, so only the 100 is a quality.
- *Superseded (S10): a flag's name isn't a slot filler, so both rows are removed from slot-fillers.tsv.* The two slot fillers are readings of feature-flag names: Google, whose taxonomy google-taxonomy names
  (SA-C-022/decides/SA-S-3506), and Apple Pay, which recurring-apple-pay names (SA-C-125/decides/SA-S-3302). Neither
  statement has a market scope.

## Gaps (statements a cell needs that the concern map doesn't hold)

- *Superseded in part (C2): placed inventory entries are now cited by their ids where no statement covers them: Pre-order apps, Event booking apps, NFT and tokengating apps, and the product-cost permissions (in the back-fill).* Platform terms with no statement: Shopify's "Pre-order apps" (SH-C-188), "Event booking apps" and "NFT and
  tokengating apps" (SH-C-190), "Product bundle apps" (SH-C-188; cited as a term only through SH-C-188's statements),
  and in Q1's candidates "Stock alert apps" (U-060), "Store data importer apps" and the "Products > View cost"
  permission (U-081, U-070), "Digital product apps" (SH-I-1886, M-076). They are inventory entries, so CM-SEL-004 and
  CM-SEL-005 are none-held for Shopify.
- The maker of Shopify Combined Listings and of Shopify Collective, and of Salla's app-type features above.
- A Salla statement saying what a product restriction limits (SA-C-028; its help page, read as context only, speaks of
  quantities and the number of purchases), and what the feature flag inventory-order means (SA-S-3495).
- A Salla statement saying whether its "Inventory audit" counts stock against the records.
- A Shopify statement on brands or a product's vendor, and on product cost (U-070; the cost permissions are now cited as inventory entries, C2, but no statement says where the cost is entered).
- Shopify's "Order limit apps" (U-084, inside SH-C-052, domain C) has no statement, and Q1 notes that what they limit
  isn't defined; it might bear on CM-CAT-009.
- Q1's own gaps on these concerns are in derived.tsv (responsible and reason, mostly).

## What the checker flagged, and the answers

1. **SH-C-187/where/SH-S-2583 (Donation apps) is of domain D, not naming B.** It is the only Shopify statement on
   donations, cited in CM-SEL-007 as an App Store category. Whether donations are a domain B capability (Salla keeps
   quick donation in its products settings, SA-S-1760, and the seed names Salla's charity stores under SEL) or a
   domain D one (Shopify keeps donation apps with loyalty and wishlists) is the reviewer's to decide; I chose B.
2. **CM-CAT-005 for Shopify, none-held, 9 hits:** checkout branding (SH-C-048, SH-C-140, SH-C-158) and Bill Pay's
   vendors (SH-C-098). Neither is a product's brand.
3. **CM-CAT-009 for Shopify, none-held, 3 hits:** the add-to-cart limit (SH-C-046, domain C): one store-wide cart
   setting, "to protect your inventory information" (SH-S-7489). Read as not product restrictions, which Salla keeps
   as a section of its products; since Salla's statements don't say what a restriction limits, a join on role can't
   rest on them. A reviewer who reads them as the same role would cite SH-C-046 from another domain.
4. **CM-SEL-004 for Shopify, none-held, 1 hit:** a manual payment method's example of "booking a service and paying in
   person" (SH-C-079/decides/SH-S-0583), not a booking capability.
5. **CM-INV-003 for Salla, none-held, 2 hits:** the Inventory audit link (SA-S-1803) and the plan line جرد المنتجات
   والمخزون (SA-S-2096), read as the inventory view of CM-INV-001, where both are cited (see Grains).
6. **CM-INV-007 for Salla, none-held, 13 hits:** all for "vendor": the wholesale market's vendors (SA-C-098) and a
   dashboard path that excludes /channel/vendors (SA-C-093, SA-C-097, SA-S-3551). Buying from the wholesale market is
   cited in CM-CAT-010; it isn't a purchase order received into stock.
7. **CM-SEL-007 has no concern landed in its tree:** both platforms keep donations inside concerns about other things
   (Salla's products, SA-C-020, landed in CM-CAT-001; Shopify's loyalty, wishlist and donation apps, SH-C-187, domain
   D). Making it a child of CM-CAT-001 would follow Salla's grouping and clear the flag, but donations are a way of
   selling, not part of the product record (my judgment). The reviewer may move or drop it.

Nothing the checker flagged is left unanswered.

## The coordinator's notes, applied

- Arabic searches: every none-held search on Salla was run with each Arabic term in its singular and plural, with and
  without ال (CM-CAT-008, CM-SEL-003, CM-INV-003, CM-INV-007). Bare "جرد" also matches بمجرد and bare "audit" Salla's
  audit logs, and "nft" alone matched only letters inside four ids of the developer docs navigation (SA-S-1161,
  SA-S-1162, SA-S-1163, SA-S-1167), so the narrower forms were searched; the cells say so. Shopify's statements are in
  English, and its none-held searches are in English.
- `own-service`: applied as above.

## Problems with the brief or the evidence

- **SA-C-020 names no other domain under also,** though it holds Salla's product filters (U-013, Shopify's side in
  domain E), sorting, recommendations and product custom fields (U-005, Shopify's metafields in domain E). Domain E's
  and D's parts can cite those statements only with a flag, and this part, which doesn't model storefront display,
  leaves them out. The coordinator may add E (and D) to SA-C-020's also.
- **`class_slice.py matches` clips why_unclear at 300 characters.** For the 13 candidates I rule on I printed the full
  rows through class_slice's own `rows()` function, one row per candidate, not the file whole.
- **The checker changed during the run** (new flags on trees of capabilities); the part passes the version at the end
  of the run.
- **One statement, two keys.** Salla's "Categories & options" link (SA-S-1794) is held under both SA-C-021 and SA-C-022,
  and Shopify's inventory entitlement (SH-S-5334) under SH-C-022 and SH-C-023; each cell cites its own concern's key.
  Many Shopify scope lines are held a second time under SH-C-158 (access scopes, domain F); the cells cite the keys of
  domain B's concerns.
- **Seed leads not modeled:** Shopify's gift cards (SH-C-025) and Salla's gifting (SA-C-077) are domain D's in
  scope.tsv, so no SEL capability holds them; a mapping part that finds gift cards sold as products should look in
  domain D first.


## The coordinator's corrections (30 October)

The checker's ruling test was corrected after this part ran: a ruling is now tested on its own keys, and `joined:<cap_id>` means one capability's cells cite keys of both sides. U-016 and U-082 were ruled `apart` because their concerns can't land together (other domains, or a coarse concern), while this part made one capability holding both sides' statements: product sourcing (CM-CAT-010) and donations (CM-SEL-007). The rulings now say `joined` on those capabilities, which is what the cells show. The concerns' landings are unchanged.


## Corrections after the dry run's review (30 October)

The coordinator's rulings on the two reviews (`studies/class-model/review-dry-run-rulings.md`) are applied here, finding by finding. Each placement below is a reading, as before; the statements are cited by key, and placed inventory entries by their ids.

- **C1, the platform's own API.** The 55 rows the cells review lists are re-placed: 49 from `shows` to `core` (Shopify's and Salla's own API folders, objects, scopes, webhook topics and mutations' requirements, for their own features), and 6 from `shows` to `extension-point` (CM-SEL-001's subscription APIs: Shopify's webhook topics SH-S-1351 and SH-S-6073, since "Subscription apps enable developers and merchants to build subscription experiences" (SH-S-0763); Salla's Recurring Payments API folder SA-S-1173, listed under the developer docs' extension points, and its webhooks SA-S-1642, SA-S-1643, SA-S-1645). Each row's `why` names the API and the ruling. Three cells change placement: CM-CAT-004/shopify and CM-CAT-006/shopify from `not-stated` to `core` (SH-S-6240's write_metaobjects "for taxonomy linking"; SH-S-6160's unauthenticated_read_product_tags), and CM-SEL-006/shopify from `extension-point` to `core;extension-point` (SH-S-1100, unauthenticated_read_bundles). The readings of every cell whose API rows changed are rewritten (CM-CAT-001, -002, -003, -005, -006, -007, CM-INV-001, -004, -005, -006, -007, CM-SEL-002, -004 and -006, on the platforms concerned, and CM-CAT-008/shopify and CM-SEL-001 on both). The checker's three flags "core rests only on boundary statements" (cells.tsv lines 8, 12, 34) are these cells: the ruling makes such a statement `core`, and no statement says apps or partners do the work.
- **C2, placed inventory entries.** CM-SEL-005/shopify is `statements: extension-point` on the App Store's Pre-order apps (SH-I-1842, placed in SH-C-188), and CM-SEL-004/shopify on Event booking apps (SH-I-1887, placed in SH-C-190). CM-SEL-003/shopify also cites NFT and tokengating apps (SH-I-1888), with C4. The product-cost cell is the back-fill's (its notes). Digital product apps (SH-I-1886) is not cited: CM-SEL-002/shopify is already `extension-point` on Digital goods and service apps (SH-S-2648), and it would change nothing.
- **C3, Salla's stocktake.** CM-INV-003/salla is `statements: core` on the plan line جرد المنتجات والمخزون (SA-S-2096, Salla Plus) and the dashboard link Inventory audit (SA-S-1803), read by their names, as Shopify's counts are; both stay cited in CM-INV-001 too.
- **C4, Shopify's NFT route.** CM-SEL-003/shopify: the route nft-application (SH-S-5094), named for an application and gated only by APPLICATIONS (SH-S-5095), is `extension-point`; the section Blockchain (SH-S-1550) is `shows`. With SH-I-1888 the cell is `extension-point` only, and the capability's count falls from 1 to 0.
- **C6, unreleased flags.** Eight flags with `"released": false` move from `core` to `shows`: salla-taxonomy (SA-S-3507, CM-CAT-004), upload-gif-image and promote-product-video (SA-S-3483, SA-S-3463, CM-CAT-007), recurring-payment and recurring-apple-pay (SA-S-3301, SA-S-3302, CM-SEL-001), bundle-zero-price-guard (SA-S-3297, CM-SEL-006), multi-warehouses and unlimited-quantity-by-branch (SA-S-3341, SA-S-3516, CM-INV-005). CM-SEL-001/salla's `core` now rests on SA-S-0195 ("By default, Recurring Payments are disabled for all stores. Only merchants or authorized third-party apps can enable this feature."), re-read from `extension-point` to `core` as Salla's own feature the merchant enables (a reading; the review's C6 names it); the API rows carry the `extension-point`. The reading of CM-SEL-006/salla had called ai-bundles not released; its statement says `"released": true`, and the reading is corrected.
- **C7 and S7, staff permissions.** Where a cell cited Salla's permission from the list a partner can request, the staff permission of the same name is now cited as `core` beside it, and the partner row is `shows` ("shows an interface for apps"): CM-CAT-001 (SA-S-2254), CM-CAT-003 (SA-S-2255), CM-CAT-005 (SA-S-2260, SA-S-2259), CM-CAT-011 (SA-S-2395), CM-SEL-002 (SA-S-2261), CM-SEL-004 (SA-S-2291), CM-SEL-005 (SA-S-2262), CM-SEL-007 (SA-S-2399), CM-INV-001 (SA-S-2256, SA-S-2403), CM-INV-002 (SA-S-2252), CM-INV-005 (SA-S-2405). CM-INV-006 already cited the staff permission (SA-S-2303); its partner row SA-S-2520 is `shows`. CM-CAT-011's count now rests on the staff permission. C7's other leads aren't cited, since the ruling takes C7 only for staff permissions: Shopify's variant bulk-edit route (SH-S-5177, of SH-C-022, which would cite SH-C-022 in another tree), Salla's restriction-product-type flag (SA-S-3351, not released; a gap below) and Shopify's fulfillment-service apps (SH-S-0702, domain C).
- **S1, strained fits.** SA-C-020 (cited in CM-SEL-006 and CM-SEL-007), SH-C-022 (its route products:update:locations, SH-S-5024, cited in CM-INV-005) and SA-C-026 (its transfer statements, cited in CM-INV-006, now in CM-INV-001's tree) are `strained`, and each reading names where else it is cited. SH-C-188's and SH-C-190's readings name their inventory entries now cited in CM-SEL-005 and CM-SEL-004 (C2).
- **S2, the INV tree.** By the brief's rule for `parent`: Shopify's inventory entitlement holds counts, purchaseOrders and transferLocation as siblings (SH-S-5334), and its purchase-order permission sits in the subcategory Inventory (SH-S-7156); Salla's Inventory management, Inventory transfer and Warehouses & branches are siblings in one flat list under /products (SA-S-1797, SA-S-1798, SA-S-1808), so the two groupings share no parent for transfers, and the anchor platforms' admin grouping, Shopify's, decides. CM-INV-006 (renamed, S12) and CM-INV-007 are now children of CM-INV-001. SH-C-023 (transfers, shipments and purchase orders) is coarser than either, so it now lands in their parent, CM-INV-001, whose Shopify cell cites SH-C-023/decides/SH-S-5334 for it (the brief's rule for a coarser concern; the review left its landing unchanged, and the alternative is SH-C-023 strained in CM-INV-006). Counts and kinds don't change.
- **S4 and S5, rulings.** `rulings.tsv` is rewritten with one row per pair of concerns, each holding only that pair's keys, from the candidate's own concerns (20 rows). U-002 drops SA-C-020's SA-S-1597 and cites SA-C-022's SA-S-1053; U-003 is two rows (CM-INV-005, CM-INV-006); U-016 is two rows, one for SH-C-185 against each Salla concern, both `joined:CM-CAT-010` (S3); U-059 is five rows; U-061 two; U-070's Shopify keys are now the cost permissions SH-I-0902 and SH-I-1129 (S5: SH-S-5016 didn't stand for cost). Two rows differ from the review's: U-059's SH-C-188 against SA-C-029 is `joined:CM-SEL-005` and U-061's SH-C-190 against SA-C-031 is `joined:CM-SEL-004`, not `apart`, because after C2 those capabilities' cells cite both sides (SH-I-1842, SH-I-1887): the ruling follows the cells. The pairs of SH-C-141 (domain E) with SA-C-098 and SA-C-124 join two concerns of other domains that this part doesn't land; CM-CAT-010 cites all three, and those domains' parts rule them.
- **S8, uncited statements.** Cited where they bear on a placement: the staff permissions inventory_browse and inventory_management of the group نقل المخزون (SA-S-2307, SA-S-2308) in CM-INV-006/salla, `core`; product_browse (SA-S-2253) in CM-CAT-001/salla, `core`; the app scope subscriptions (SA-S-1567) in CM-SEL-001/salla, `extension-point`, as the Recurring Payments API's. A pricing capability is borne out by Shopify's and Salla's statements: Salla's setting Automatic pricing under its products settings (SA-S-1751) and its webhook product.price.updated (SA-S-1599), and Shopify's four App Store pricing categories (SH-I-1894 to SH-I-1897, placed in SH-C-020). It is CM-CAT-013, product pricing, numbered past the model's highest in CAT (CM-CAT-012). It is written in B-woocommerce's `capabilities.tsv`, since a CM-CAT-013 here would put the anchor's numbers past WooCommerce's CM-CAT-012 and fail that part's numbering test; its Shopify and Salla cells are the back-fill's. The leads with no stated meaning stay uncited and are gaps (below).
- **S9, the quality.** max_inventory_types (SA-S-3504) moves from CM-INV-001 to CM-INV-005: it sits beside enable_branch_inventories, which reads as a number of inventories (a reading). The statement doesn't say what an inventory type is (a gap).
- **S10, slot fillers.** Both rows are removed: Google (SA-S-3506) and Apple Pay (SA-S-3302) were readings of feature-flag names, which aren't fillers, and neither statement has a market scope. virtooal (SA-S-3476) is not added, for the same reason. `slot-fillers.tsv` holds its header only.
- **S11 and S12, names.** CM-SEL-002: "Digital products: downloadable files and digital codes (... WooCommerce downloadable products)". CM-INV-003: "Inventory counts and stocktakes (Shopify inventory counts; Salla جرد المنتجات والمخزون, Inventory audit)", with C3. CM-INV-004: "Low stock: alerts and lists (...; WooCommerce ProductsLowInStock)". CM-INV-006: "Inventory transfers and shipments (...)". CM-CAT-003: "Store product groupings ... WooCommerce Product categories". With the same rule (names use every landed platform's terms), CM-SEL-004 adds WooCommerce's Bookings and appointments and Shopify's Event booking apps, CM-SEL-005 Shopify's Pre-order apps, and CM-SEL-006 WooCommerce's Bundles and Product Bundles; the notes of CM-CAT-005, CM-SEL-004 and CM-SEL-005 no longer say "Salla only so far". The homonyms go in the capabilities' notes: WooCommerce's collection-data route and Shopify's tax 'product categories' (CM-CAT-003), WordPress taxonomies (CM-CAT-004), WooPayments' prohibited product types (CM-CAT-009). The coordinator renames at the merge (convention 7); these are the review's names, applied by the rulings.
- **S16 and S17, notes and readings.** CM-CAT-008/shopify's reading names Q1's gap SH-C-038/where ("observation needed"), which could move the cell to own-service or extension-point and the capability to slot. CM-CAT-011/salla's reading says which permission is the partner's and that its core rests on the staff permission. CM-SEL-007/shopify's reading no longer says SH-C-187 lacks B (scope.tsv names it since S6). CM-CAT-009/shopify's and CM-INV-004/shopify's readings name the inventory entries the checker's search now finds (Order limit apps, SH-I-1816; Stock alert apps, SH-I-1844). The passages above that these corrections supersede are marked.

**Not applied here, as the rulings leave them:** C5 (a gap for Q1: the maker of WooCommerce's extensions); S3 (U-016 and U-082 stay `joined`, now with bases naming the other domains); S6 (scope.tsv, the coordinator's); S13 to S15 (listed with the extent's report and the architecture plan).

**No ruling disagreed with the evidence.** The two ruling values above that differ from the review's rows follow C2's evidence, which the rulings take.

**Gaps added (S8, S9):** what the feature flags restriction-product-type (SA-S-3351, for CM-CAT-009), inventory-order (SA-S-3495, for CM-INV-007 or CM-INV-001) and product-sale-start (SA-S-3490, a scheduled sale) mean; what bins inside a location are (SH-C-024/decides/SH-S-5201, behind a beta, for CM-INV-005); what allow_negative_quantities inside SA-S-3504 allows (selling below zero stock; no capability holds it); what an inventory type is (max_inventory_types); and what Salla's automatic pricing computes (CM-CAT-013).

**The checker after the corrections:** 0 problems, 8 flags. The three boundary flags are C1's cells (above). CM-SEL-007's tree has no concern landed: it holds as a root (the structure review's resolution). The four none-held flags (CM-CAT-005, CM-CAT-009, CM-INV-004 for Shopify, CM-INV-007 for Salla) hold as the cells review resolved them; two now name the inventory entries they match.
