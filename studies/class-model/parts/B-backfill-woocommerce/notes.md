# B-backfill-woocommerce: notes

## What this part did

B-woocommerce added three capabilities to domain B: CM-CAT-012 (product cost), CM-SEL-008 (memberships) and CM-INV-008
(stock held for unpaid orders). This part writes the six cells they lacked, for Shopify and Salla. Each platform's
statements were searched with `class_slice.py search`, Salla's in English and in Arabic, each Arabic term in its
singular and its plural, with and without ال. The hits were read and none shows the capability, so all six cells were
`none-held` (CM-CAT-012/shopify is no longer, after the dry run's review: the corrections at the end), with the terms searched in `searched`. `evidence.tsv` holds its header only. `none-held` means only that
the concern map holds nothing found by those terms; it never means the platform lacks the capability.

## The readings

- *Superseded for Shopify (C2): the cell now cites Shopify's staff permissions for a product's cost, placed inventory entries (the corrections at the end).* **CM-CAT-012, product cost.** Shopify: its cost hits are the costs of its own fees and services (transaction fees,
  app charges, shipping insurance, Shop Campaigns, Shop Pay Installments, AI features), not a product's cost; the 'Products > View cost' permission is an
  inventory entry in Q1's candidate U-070, with no statement (the anchor's gap, which stands). Salla: the cost hits are
  shipping costs and its report plan lines. SA-C-220's 'تحليلات الأرباح' (SA-S-2044) and 'تقرير تكاليف وأرباح الشحن'
  (SA-S-2045) are reports, of domain D, and no statement says a cost is entered on a product, so they aren't cited.
  A reading: profit analytics may rest on a product cost, but no held statement says so.
- **CM-SEL-008, memberships.** Both platforms' hits are staff members, payment-network terms and loyalty. Shopify's
  App Store category Customer loyalty apps (SH-C-187/where/SH-S-2581) and Salla's loyalty program (SA-C-064) are
  points and rewards; no statement calls either a membership, and WooCommerce's cell is only a category name
  (WC-C-102/where/WC-S-0728), so no join on role can rest on the statements. Not cited.
- **CM-INV-008, stock held for unpaid orders.** Shopify's hits are payment reserves and holds, abandoned checkouts and
  unpaid manual-payment orders. Salla's are bookings (Order Reservations, SA-C-031; the anchor's homonyms), the order
  status بإنتظار الدفع (SA-S-2672), cancellation and the setting 'Auto restock based on order status'
  (SA-C-025/where/SA-S-1742), with the feature flag status-return-to-stock (SA-C-025/decides/SA-S-3289). They are
  read as not this capability: their words return stock by order status and say nothing of holding stock for an unpaid
  order for a time (WC-C-068/decides/WC-S-5401). They stay in CM-INV-001.

## Gaps (statements a cell needs that the concern map doesn't hold)

- Shopify: a statement on a product's cost (the 'Products > View cost' permission of U-070 is an inventory entry, now cited by its id, C2; no statement says where the cost is entered);
  a statement on whether checkout or an unpaid order holds stock; any statement on memberships.
- Salla: a statement on whether a product carries a cost price, and on what its profit analytics (SA-S-2044) compute
  from; what 'Auto restock based on order status' (SA-S-1742) does, and what the feature flag inventory-order
  (SA-S-3495) means; any statement on memberships.

- **WooCommerce's own terms** (Cost of Goods Sold, _cogs_value, cost_of_goods_sold, Memberships, Hold stock,
  woocommerce_hold_stock_minutes) were also searched on both platforms: no statement holds them but the general words
  already read above.

## What the checker flagged

*As first run; after the corrections, see the end.* `check_class_part.py`: 0 problems, 6 flags. Each flag is one of the six none-held cells: statements match its searched
terms or WooCommerce's terms for the capability. Every match was read (with `search` and, where unclear, `key`), and the
cell's `reading` names what they are: fees and service costs, shipping costs, reports, staff members, loyalty, payment
reserves, bookings, order statuses, cancellation, and stock returned by order status. None shows the capability, so
none is cited. The match counts are high because the searched terms are general words (member, stock, cost, hold,
إلغاء, المخزون), searched so that nothing would be missed.


## Corrections after the dry run's review (30 October)

The coordinator's rulings on the two reviews (`studies/class-model/review-dry-run-rulings.md`) are applied to this part's cells as follows. Each placement is a reading.

- **C2, product cost for Shopify.** CM-CAT-012/shopify is now `statements: core` on Shopify's staff permissions for a product's cost: Products > View cost and Products > Edit cost (SH-I-0902, SH-I-0904), and EDIT_PRODUCT_COST and VIEW_PRODUCT_COSTS (SH-I-1057, SH-I-1129). They are inventory entries Q1 placed in SH-C-010 and SH-C-020, in its staff-permissions list, each with its citation, which no statement covers, so the cell cites them by their ids, as the rulings allow. No statement says where the cost is entered or what it is used for. CM-CAT-012's count goes from 1 to 2. The checker flags the four rows as statements of SH-C-010, domain A, without B under also: it reads an entry's first concern, and each entry is also SH-C-020's, which is domain B, so the citation is of this domain.
- **S8, product pricing (CM-CAT-013).** The capability is added in B-woocommerce (its notes say why it is there). This part writes its Shopify and Salla cells. Shopify: `extension-point` on the App Store's categories Pricing apps, Pricing optimization apps, Pricing - Other and Pricing quote apps (SH-I-1894 to SH-I-1897, inventory entries placed in SH-C-020); the store currency 'used within your Shopify admin for pricing products' (SH-S-0361, SH-C-107, domain E) isn't cited. Salla: `core` on its setting Automatic pricing under its products settings (SA-S-1751) and its own webhook product.price.updated (SA-S-1599, C1), and `shows` on the metal-pricing flag, which isn't released (SA-S-3515, C6). No statement of any platform says what the pricing does: a gap.
- **Searched:** pricing; price list; priceList; compare at price; compare-at; compareAtPrice; product price; price of; prices; price; priced (Shopify); pricing; auto_pricing; تسعير; التسعير; تسعيرة; التسعيرة; تسعيرات; التسعيرات; سعر المنتج; أسعار المنتجات; اسعار المنتجات; price; سعر (Salla). The other hits are Shopify's plans and its App Pricing (an app's billing), currencies, taxes and shipping rates, and Salla's shipping pricing, taxes, exchange rates and theme prices: none is a product's pricing.

**Not applied here, as the rulings leave them:** none of the other findings touches this part's cells.

**No ruling disagreed with the evidence.**

**The checker after the corrections:** 0 problems, 9 flags: the four SH-C-010 flags (above) and the five remaining none-held cells, each read as before.
