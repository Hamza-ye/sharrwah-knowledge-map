# B-zid: notes

The mapping part of domain B, Catalog and inventory (areas CAT, SEL, INV), for Zid: its 4 concerns that `scope.tsv`
gives the domain (ZD-C-043, ZD-C-083, ZD-C-084, ZD-C-085), mapped onto the model of `B-anchor`, `B-woocommerce` and
`B-backfill-woocommerce` (29 capabilities). Zid was never matched by Q1, so every landing is my join, by terms, and
every join is a reading. Every row is a reading of the statements its keys cite; a fact is only what a cited statement
says. Where the brief left a choice to me, this file says so ("my judgment").

Result: 4 new capabilities (CAT 2, INV 2), so the model is now CAT 15, SEL 8, INV 10. 4 landings (all 4 in capabilities
of the model so far, none in new ones; 1 strained), 33 cells (22 held, 11 none-held), 67 evidence rows, 5 qualities, no
slot fillers, no rulings (Zid has no unclear candidates). `python3 -I method/check_class_part.py
studies/class-model/parts/B-zid`: 0 problems, 12 flags, each answered under "What the checker flagged".

## How I mapped, and why

- **Landing.** Each concern lands in the model's capability whose terms it shares, with the definition where Zid gives
  one: Products (CM-CAT-001), Product Categories / تصنيف المنتجات (CM-CAT-003), Inventory Management / إدارة المخزون
  (CM-INV-001), Digital Products / المنتجات الرقمية (CM-SEL-002). Each `join_evidence` cites Zid's keys and the other
  platforms' keys that carry the same term.
- **Zid's evidence is mostly names.** Zid's concerns hold few statements (41 across my 4 concerns and the 5 under
  `also`). Most of what Zid shows in the domain is in inventory entries Q1 placed in the concerns: Merchant API groups
  (Product Attributes, Product Variants, Product Brands, Product Images, Product Badge, Product Stock) and the plan
  lines of the group Product & Inventory Management / إدارة المنتجات والمخزون. No statement covers them, so the cells
  cite them by their ids, by the dry run's convention on placed inventory entries (C2). Each is a name, with no
  description, so a cell resting on one says what the name doesn't tell.
- **The plan lines as `core`.** A compare-plans line with `!0` on a plan is a plan line that includes the feature, so
  it supports `core`, scoped to its plans (the statements' own note reads `!0` and `!1`). The plan features without
  their plan flags (the inventory entries) are cited as `core` as lines of Zid's own plan.
- **When I added a capability (my judgment).** By the convention, where Zid gives a thing a place of its own (an API
  group or a plan line) and no capability of the model holds it:
  - **CM-INV-009 Inventory withdrawal priority** rests on a plan line with its own description (ZD-S-0919) and a
    help-center statement (ZD-S-1023). Its parent is CM-INV-001, not CM-INV-005: no statement says the priority is
    among locations.
  - **CM-CAT-014 Product badges** (API group, ZD-I-0011), **CM-CAT-015 Barcode printing** (plan line, ZD-I-0249) and
    **CM-INV-010 Products shown by the customer's city** (plan line, ZD-I-0257, and the plan card ZD-I-0405) rest on
    names only. B-woocommerce made no capability from bare Marketplace category names (Pricing, Additional purchases)
    because no statement said what they held; these names say what the thing is, so I made them, and each capability's
    note says it rests on the name. A reviewer may fold any of the three into its parent.
- **What I didn't add (my judgment).** Bare names that fit an existing capability are cited there: Product Attribute
  Presets in CM-CAT-002, Import, Export and Quick Bulk Edit in CM-CAT-001, Export Full Quantities and Update Product
  Quantities in CM-INV-001, Sales by Inventory Location in CM-INV-005. Left uncited, as names whose capability no
  statement shows: Product Sorting (ZD-I-0015) and Sort Products (ZD-I-0232), Duplicate Product (ZD-I-0231), Product
  Actions (ZD-I-0237), Update Product Weights (ZD-I-0245), Product Export (ZD-I-0018) and Request Inventory via POS
  (ZD-I-0256, placed in ZD-C-085 and ZD-C-108), which may be a transfer request but says nothing of one. Product
  custom fields (ZD-C-100, Custom Fields / حقول مخصصة, ZD-S-0963) are of a domain-C concern about orders and products
  both; no capability of domain B holds them, and I didn't make one from another domain's concern: domain C's parts
  model it, and a reviewer may move it.
- **Citing another domain's statement (my judgment).** Only where the cell would otherwise be none-held, as
  B-woocommerce did: CM-CAT-010 (App Market category إيجاد المنتجات (Dropshipping), ZD-I-0446, ZD-C-070), CM-CAT-012
  (plan line Product Cost Report, ZD-I-0253, ZD-C-105), CM-SEL-001 and CM-SEL-004 (App Market category الحجوزات
  والاشتراكات, ZD-I-0438, ZD-C-070). The App Market categories إدارة المنتجات والمخزون (ZD-I-0444) and مراقبة الأسعار
  والمنافسين (ZD-I-0433) would add extension-point to CM-INV-001 and CM-CAT-013, but those cells are held without
  them, so they aren't cited; the reviewer may add them.

## Landings and grains

- **ZD-C-083 (Products) lands in CM-CAT-001, clean.** It is coarse, like SH-C-020 and WC-C-064: Q1 placed in it Zid's
  API groups for attributes, variants, brands, images and badges and its product plan lines, so its sub-parts are cited
  in CM-CAT-001's children (CM-CAT-002, 005, 007, 013, 014, 015), all in one tree.
- **ZD-C-084 (Product categories) lands in CM-CAT-003, clean.** Zid's categories nest (the endpoint
  /categories/nesting, ZD-S-0099); the capability already holds Salla's categories and WooCommerce's.
- **ZD-C-085 (Inventory and stock) lands in CM-INV-001, strained.** It is coarse: it holds Zid's inventory locations,
  warehouses and their plan limits too. Those are cited in CM-INV-005, which the anchor made a root, not a child of
  CM-INV-001, so ZD-C-085's statements are in two trees. The rest of it (logs, counts, transfers, withdrawal priority,
  display by customer city) is in CM-INV-001's children. A reviewer may split it, or the coordinator may make CM-INV-005
  a child of CM-INV-001; Zid's own grouping (one plan group, Product & Inventory Management, and one API group,
  Inventories, that holds Create Location) puts locations under inventory, as Salla's Warehouses & branches link does
  under products (/products/branches, SA-S-1808), but Shopify's Locations sit under Settings (SH-S-1493), and the
  anchor followed that.
- **ZD-C-043 (Digital products and vouchers) lands in CM-SEL-002, clean.** Zid's Digital Vouchers (ZD-S-0008) are read
  as the capability's digital codes, a reading: no statement defines a voucher. A voucher here is a product's code, not a
  discount coupon (قسائم التخفيض, manage.store.coupons, ZD-S-0520, domain D).

## Joins on role

- **CM-CAT-002:** Zid's Product Attributes and Product Attribute Presets read as its options and option templates, as
  B-woocommerce read WooCommerce's attributes. No statement defines either; the cell cites Zid's keys and the
  capability's other cells cite Salla's and Shopify's.
- **CM-INV-008:** Zid's 30-minute hold of a product while the customer enters card details (ZD-S-0965, ZD-C-100,
  which names B under also) read as WooCommerce's Hold stock (WC-S-5401): stock held while an order's payment is
  pending. Zid's statement doesn't say what happens when the time runs out, and doesn't use the word stock: it says the
  product is held (حجز المنتج).
- **CM-SEL-006:** Zid's Bundle Offers / الحزم التسويقية joined by the term bundle and the definition 'Bundle multiple
  products into one package' (ZD-S-0928). A reading: Zid places the API under Marketing > Bundle Offers, on a discounts
  path (/discounts/bundle-offers, ZD-S-0106), and the plan line under Product & Inventory Management (ZD-I-0242); its
  help center says they 'are not ordinary discounts' (ZD-S-1033). They are statements of ZD-C-089 (domain D), so
  domain D's part may cite them as core too (see the flags).

## Homonyms kept apart

- **حجز:** Zid's حجز المنتج (ZD-S-0965) is a hold of stock during payment (CM-INV-008); Salla's الحجوزات are bookings
  (CM-SEL-004); Zid Pay's حجز مبلغ احتياطي (ZD-S-0582) is a payment reserve (domain C). The search for حجز in CM-SEL-004
  found the first and the last, and neither is cited there.
- **Subscriptions / الاشتراكات:** Zid's manage.store.subscription (ZD-I-0526), the app.market.subscription.* webhooks
  and Subscription Apps (ZD-I-0540, ZD-I-0541) are the merchant's own subscriptions to Zid's plans and apps (domains A
  and F), not subscriptions a store sells (CM-SEL-001). Only the App Market category الحجوزات والاشتراكات, under store
  and customer experience, is cited there, and reading it as subscriptions sold is marked.
- **Stock notifications / إشعارات المخزون:** Zid's stock notifications (ZD-S-1028, ZD-S-1029, ZD-C-087, domain D)
  notify customers when a product that ran out is available again; CM-INV-004's low-stock alerts tell the merchant.
  They aren't joined.
- **Badge:** the Zid Assurance badge (ZD-S-0999, ZD-C-111) is a store's badge; Zid's Product Badge API group
  (CM-CAT-014) is a product's. Apart.
- **Tags:** Zid's tags in the map are of orders, customers and blog posts, never of products (CM-CAT-006, none-held).

## Concerns read under `also`

- **ZD-C-089 Bundle offers (D):** cited in CM-SEL-006.
- **ZD-C-100 Order and product properties (C):** ZD-S-0965 cited in CM-INV-008; Custom Fields not cited (above).
- **ZD-C-086 Product reviews and questions (D)**, **ZD-C-087 Product availability notifications (D)** and **ZD-C-101
  Gifting (D):** no capability of domain B holds them (B-woocommerce put gifting in D), so none is cited.

## What the checker flagged

- **Another domain's statements (4 flags: ZD-I-0446, ZD-I-0253, ZD-I-0438 twice).** Each is cited because its cell
  would otherwise be none-held, and the cell's reading says so. None supports core or own-service: ZD-I-0446 and
  ZD-I-0438 are extension-point (App Market categories), ZD-I-0253 is shows (a report's plan line).
- **ZD-I-0438 in two trees (CM-SEL-001 and CM-SEL-004).** The one App Market category names both bookings and
  subscriptions (الحجوزات والاشتراكات), so it is evidence of both; it is extension-point in each, and neither is the
  other's parent.
- **none-held with matching statements (7 flags: CM-CAT-004, CAT-006, CAT-008, CAT-009, INV-004, INV-007, SEL-007).**
  Each cell's reading names its hits and why none shows the capability: Google Cloud and Google Maps, and 'Create
  Product Types' (CAT-004); order, customer and blog tags (CAT-006); the linked product groups of ZD-S-0916, whose
  definition doesn't show a combined listing (CAT-008, the one a reviewer may want to read again); shipping and payment
  restrictions and payout minimums (CAT-009); Nafath, Zid Alerts, app events and webhook health states, a withdrawal
  priority's aim and customers' stock notifications (INV-004); payment-processing suppliers (INV-007); a charity as a business type (SEL-007).
- **The checker's first run** flagged ZD-S-0023 and ZD-S-0100 in two trees (CM-INV-001 and CM-INV-005). Their words
  are Create Location and POST /v1/locations/, so I cited them in CM-INV-005 only; CM-INV-001 rests on Product Stock and
  the plan lines.

## Gaps and problems

- **Definitions not stated.** Product Badge, Barcode Printing, Display Products by Customer City, Inventory Management
  Logs, Inventory Count, Transfer Inventory Between Branches, Custom Product Pricing and Product Attribute Presets are
  names with no statement in the concern map; the structures that would hold their definitions are Zid's API reference
  pages (docs.zid.sa) and the compare-plans source, whose entries Q1 captured without descriptions.
- **Q1's gaps.** ZD-C-043/where and /reason, 'searched, not found': the region of the Amazon S3 storage and a reason
  for it; CM-SEL-002's quality records only 'upload files directly to Amazon S3 storage'. Amazon S3 is a third party
  that stores the files, not one doing the capability or setting its terms, so it is no slot filler (my judgment).
  ZD-S-0590's service provider (مزود الخدمة) sets terms on digital products for Zid Pay but isn't named, so no filler.
  The responsible placement of ZD-C-083, 084 and 085 is 'stated only in general terms'.
- **Duplicates in the inventory.** ZD-I-0244 and ZD-I-0251, ZD-I-0252 and ZD-I-0255, ZD-I-0254 and ZD-I-0258 are the
  same plan lines captured twice (same cite id); I cite one of each.
- **A statement in two concerns.** ZD-S-0590 is held under ZD-C-043 and ZD-C-009; I cite the ZD-C-043 key.

## Renames proposed

- CM-CAT-003: add Zid's Product Categories / تصنيف المنتجات.
- CM-INV-001: add Zid's Inventory Management / إدارة المخزون.
- CM-SEL-002: add Zid's Digital Products and Digital Vouchers.
- CM-SEL-006: add Zid's Bundle Offers / الحزم التسويقية.
- CM-INV-008: 'Stock held for unpaid orders (WooCommerce Hold stock; Zid حجز المنتج)'.


## The coordinator's corrections (30 October)

- **ZD-I-0229 and ZD-I-0250** (the plan lines Import Products and Export Products) were `core` here and in G-zid's CM-MIG-001, so they counted in two domains. They are import and export, so they count in G; here they are `shows`.
