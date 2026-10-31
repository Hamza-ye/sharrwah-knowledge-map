# B-backfill-zid: notes

## What this part did

B-zid added four capabilities to domain B: CM-CAT-014 (product badges), CM-CAT-015 (barcode printing), CM-INV-009
(inventory withdrawal priority) and CM-INV-010 (products shown by the customer's city). This part writes the twelve
cells they lacked, for Shopify, Salla and WooCommerce. `class_slice.py candidates` found no statement holding Zid's own
terms on any of the three platforms, so each platform's statements were searched with `class_slice.py search`, Salla's
in English and in Arabic, each Arabic term in its singular and its plural, with and without ال. The hits were read, and
with `key` where the first 200 characters didn't settle them.

Result: one cell holds statements (CM-INV-009/salla, `core`, joined on role, a reading); eleven are `none-held`, with
the terms searched in `searched`. `none-held` means only that the concern map holds nothing found by those terms; it
never means the platform lacks the capability.

## Definitions not stated

Three of the four capabilities rest on Zid's names only: Product Badge (ZD-I-0011), Barcode Printing (ZD-I-0249) and
Display Products by Customer City (ZD-I-0257, ZD-I-0405). B-zid's notes say no statement defines them. By the dry run's
convention, the other platforms' `none-held` cells say the definition isn't stated. A shared word (badge, barcode,
city) can't join where no cited statement shows what Zid's object is, so the leads below are named and not cited.
CM-INV-009 has a definition: 'Set inventory withdrawal priority to avoid stockouts and ensure quick order fulfillment.'
(ZD-C-085/decides/ZD-S-0919).

## The readings, cell by cell

- **CM-CAT-014, product badges.** The leads are Shopify's App Store category Badge and icon apps (SH-I-1906, placed in
  SH-C-193, domain E), Salla's web components salla-badge and salla-trust-badges (SA-C-091, domain E) and WooCommerce's
  On-Sale Badge block (WC-C-087/boundary/WC-S-0800, domain C). None of these concerns names B under also, and each
  statement is a name only: none says the badge is shown on a product as a thing the merchant sets. Context read beyond
  the statements, not cited: the Shopify category's page puts it under Store design > Design elements, with the intro
  'Build customer confidence with visual icons that draw attention to your products, social links, and major selling
  points.' (observed-sh, `structures/shopify/app-store-taxonomy/apps.shopify.com_categories/pages.jsonl` line 105), which
  is wider than a product's badge. WooCommerce's On-Sale Badge is the nearest lead, a badge shown on a product on sale;
  a reviewer who reads Zid's Product Badge as including it could cite WC-S-0800 as `core`, flagged as domain C's.
  Salla's product tags (وسوم المنتجات, SA-S-1982; Product Tags, SA-S-1024) are tags, and its flag
  promotion-title-and-subtitle (SA-C-071/decides/SA-S-3096, domain D) doesn't say what it titles: neither is cited.
- **CM-CAT-015, barcode printing.** No statement on the three platforms names printing a barcode. Shopify's barcode
  hits are the route products:variants:update:barcodes (SH-C-020/decides/SH-S-5021, editing the field) and the App
  Store category SKU and barcode apps (SH-I-1872, SH-C-142, domain E; its page's intro, context: 'Assign products
  barcodes and SKUs to run stock checks and monitor inventory', which doesn't say printing). Its admin print-action
  targets on product pages (SH-I-1538, SH-I-1540, SH-I-1574, SH-C-164, domain F) don't name barcodes. Salla's
  inventory::print_export (SA-S-3094) prints and exports inventory, and its only barcode is on the invoice
  (SA-S-5034). WooCommerce's Label printing category (WC-S-0715) sits under Shipping, delivery and fulfillment.
- **CM-INV-009, inventory withdrawal priority.**
  - **Salla, joined on role (a reading).** Salla's setting Branch and warehouse priority order
    (products/products.branch_sorting, SA-C-026/where/SA-S-1755), under its products settings, and Zid's plan line
    Inventory Withdrawal Priority (ZD-S-0919) are both a priority order the merchant sets on where the store's stock
    is drawn. The join has two limits, each a reason a reviewer may undo it: Zid's statement doesn't say among what its
    priority is (B-zid's notes, which is why CM-INV-009's parent is CM-INV-001, not CM-INV-005), and Salla's statement
    is a label that doesn't say the order decides which stock an order draws. Context read beyond the statement, not
    cited: the setting's description in the same dashboard translations, 'Once branch-based inventory is enabled,
    orders are fulfilled based on product availability and the priority order of branches and warehouses.'
    (`products#products.branch_sorting.description`, observed-sa `structures/salla/dashboard-translations/`). It isn't
    in the concern map: a gap. SA-C-026 is landed in CM-INV-005; this cell cites another of its statements, which no
    other cell cites (B-anchor's CM-INV-005/salla cites Branches Allocations, SA-S-1043).
  - **Shopify, none-held.** Order routing, 'You can set up order routing to automatically assign orders to fulfillment
    locations based on configured rules.' (SH-C-060/decides/SH-S-0751), with Order Routing Location Rule and the
    webhook fulfillment_orders/order_routing_complete, is the analogue of Salla's setting, but weaker: its statements
    name rules, not a priority, and SH-C-060 is domain C's (which location fulfils), with B under also. Citing it as
    `core` here would put a core statement in two domains. A reviewer who accepts Salla's join may decide whether
    order routing joins too.
  - **WooCommerce, none-held.** No statement names more than one stock location.
  - **Homonym:** withdrawal. Zid's أولوية السحب من المخزون is stock drawn from inventory. WooCommerce's order withdrawal
    (WC-C-091, WC-C-076: a customer's request to withdraw from an order, a legal right) and Shopify's EU right of
    withdrawal (SH-I-2129) are another thing, as are payout withdrawals (SH-C-088, WC-C-116, Salla's سحب رصيد المتجر,
    SA-C-005).
- **CM-INV-010, products shown by the customer's city.** No statement on the three platforms shows products shown by
  the customer's city. Shopify's Markets control 'product availability' by market (SH-C-106/decides/SH-S-0541, domain
  E), and markets are countries and regions in its statements. Salla's Multiple markets make store copies 'لكل دولة
  تستهدفها أو منطقة أو مدينة' (SA-C-165/decides/SA-S-0157), and its setting Market selection
  (markets/browse_product_method, SA-S-1730) is of the same concern, domain E without B under also; neither statement
  names products. Context read beyond the statements, not cited: the Market selection page in observed-sa's settings
  centre also opens from the inventory (`from=inventory`), titled 'Customize Store browsing experience', with options
  such as 'Inventory will be deducted from an automatically selected branch or warehouse, with no option to switch
  locations.' and 'Choose how branches or warehouses are shown to customers on their first visit.'
  (`structures/salla/settings-center/merchant@en/markets~browse_product_method.json` and the dashboard translations).
  That reads like browsing by the customer's branch, close to Zid's capability, but none of it is a statement in the
  concern map: a gap. WooCommerce's geolocation sets tax rates and shipping methods (WC-C-046), not products.

## Gaps (statements a cell needs that the concern map doesn't hold)

- Zid: definitions of Product Badge, Barcode Printing and Display Products by Customer City (B-zid's notes); without
  them no other platform's cell can join.
- Salla: the description of the setting products.branch_sorting (dashboard translations,
  `products#products.branch_sorting.description`), which would say what the priority order decides; the inventory
  options of Market selection (`markets/browse_product_method#option.warehouses_ip-address`,
  `#warehouses-view`, `markets/browse_product_method_warehouses`), which would bear on CM-INV-010 and CM-INV-009.
- Shopify: the definition of the App Store categories Badge and icon apps and SKU and barcode apps (their intros are in
  the captured category pages, not in the concern map); any statement on order routing's priority among locations.
- WooCommerce: the On-Sale Badge block's README, which the index entry WC-S-0800 links and the concern map doesn't hold.

## What the checker flagged

`check_class_part.py`: 0 problems, 11 flags. Each flag is one of the eleven none-held cells: statements match its
searched terms or the other platforms' terms for the capability. The counts are high because the searched terms
include general words (label, tag, print, priority, location, availability, region) and because Zid's terms hold
common words; on Salla, 'label' and 'tag' also match the JSON keys of its permission lists and web components. Every
hit that isn't such a key was read, and each cell's `reading` names what they are. The leads are set out above; none
is cited, for the reasons given.
