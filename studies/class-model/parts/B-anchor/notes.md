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

A single feature flag was not enough on its own, and nor was a setting of how the storefront displays products. So
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
- INV: inventory tracking (001) holds inventory history (002), counts (003) and low-stock alerts (004); inventory
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
- **Locations, transfers, purchase orders (CM-INV-005 to -007).** Salla's SA-C-026 holds branches, warehouses and
  inventory transfer; Shopify's SH-C-024 holds locations and SH-C-023 transfers, shipments and purchase orders (Q1's
  U-003). Transfers are a child of locations, so SA-C-026 lands cleanly in the parent. Purchase orders are a child of
  transfers because Shopify's own permission tree makes them depend on the transfer permissions
  (SH-C-023/decides/SH-S-7156: View purchase orders depends on VIEW_INVENTORY_TRANSFERS; SH-C-023/decides/SH-S-7157:
  Manage purchase orders depends on CREATE_AND_EDIT_INVENTORY_TRANSFERS) and a transfer links related purchase orders
  (SH-S-6221); so SH-C-023 lands in their parent, CM-INV-006. This dependency is Shopify's alone (my judgment): a
  reviewer may prefer purchase orders as a child of CM-INV-001, with SH-C-023 then strained.
- **Inventory counts (CM-INV-003) apart from tracking.** Shopify gates counts by their own entitlement
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

- **SH-C-190 in CM-SEL-002**, by M-076: its platform term "Event booking apps" is bookings (CM-SEL-004) and has no
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
  API folders, objects, scopes and webhook topics are `shows`, so no `core` rests on boundary statements alone.
- `extension-point` rests on App Store categories (Shopify's and Salla's), Shopify's product_configuration extension
  template (SH-S-2207), the API guides that give apps their scopes (SH-S-6257, SH-S-6286), the fulfillment-service
  apps that edit their own locations (SH-S-6206, a reading; fulfillment services are domain C's), Salla's endpoint for
  dropshipping applications (SA-S-0179), and SA-S-0195, where authorized third-party apps can enable recurring
  payments (a reading: enabling it through the API is the apps' part).
- Two cells hold statements with no placement (`not-stated` in derived.tsv): CM-CAT-004 for Shopify (taxonomy linking
  named in a scope line) and CM-CAT-006 for Shopify (the product-tags scope).
- CM-SEL-003 for Shopify is `core` by the rule (its own admin section and route), though the route needs the apps
  permission (SH-S-5095), which reads as a page apps fill; a reviewer may prefer `shows`.

## Qualities and slot fillers

- Three qualities are unplaced inventory entries with no value in the concern map: maxProductVariants (SH-I-2520) and
  maxProductOptions (SH-I-2519), store resource limits, and tagsPerProductLimitEnabled (SH-I-2598), a store feature
  key. The structure that holds their values is the stores' resourceLimits and features in Shopify's admin answers;
  Shopify's `notes.md` keeps the values per store under "Unplaced keys". A gap: they would be statements once tied to a
  concern. SH-C-020/decides/SH-S-7214's note records that the built-in feature page's 100 variants differs from the
  maxProductVariants value (2048); the note is not a statement, so only the 100 is a quality.
- The two slot fillers are readings of feature-flag names: Google, whose taxonomy google-taxonomy names
  (SA-C-022/decides/SA-S-3506), and Apple Pay, which recurring-apple-pay names (SA-C-125/decides/SA-S-3302). Neither
  statement has a market scope.

## Gaps (statements a cell needs that the concern map doesn't hold)

- Platform terms with no statement: Shopify's "Pre-order apps" (SH-C-188), "Event booking apps" and "NFT and
  tokengating apps" (SH-C-190), "Product bundle apps" (SH-C-188; cited as a term only through SH-C-188's statements),
  and in Q1's candidates "Stock alert apps" (U-060), "Store data importer apps" and the "Products > View cost"
  permission (U-081, U-070), "Digital product apps" (SH-I-1886, M-076). They are inventory entries, so CM-SEL-004 and
  CM-SEL-005 are none-held for Shopify.
- The maker of Shopify Combined Listings and of Shopify Collective, and of Salla's app-type features above.
- A Salla statement saying what a product restriction limits (SA-C-028; its help page, read as context only, speaks of
  quantities and the number of purchases), and what the feature flag inventory-order means (SA-S-3495).
- A Salla statement saying whether its "Inventory audit" counts stock against the records.
- A Shopify statement on brands or a product's vendor, and on product cost (U-070).
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
