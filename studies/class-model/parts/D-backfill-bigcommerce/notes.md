# D-backfill-bigcommerce: notes

D-bigcommerce added six capabilities to domain D: CM-B2B-004 (quotes), CM-B2B-005 (shopping lists), CM-B2B-006 (sales
reps for business buyers) and CM-B2B-007 (buyer portal), all children of CM-B2B-001; CM-MKT-023 (product
recommendations); and CM-ANL-007 (commerce data sent to outside analytics platforms and data warehouses), a child of
CM-ANL-001. This back-fill writes their 24 missing cells, for Shopify, Salla, WooCommerce and Zid. It adds no
capabilities and lands no concerns.

## How the cells were found

`candidates --domain D --areas B2B,MKT,ANL` gave nothing for these six capabilities on any platform except "Storefront"
for CM-B2B-007, whose hits are storefront entitlements and scopes, not a buyer's area. BigCommerce's terms (B2B Edition,
Quotes, Shopping List, Sales Staff, Buyer portal, Big Open Data Solutions, Vertex AI) are its own. So I searched each
platform for the thing itself, as the coordinator's message asked: a quote or a request for a quote, a reorder list, a
sales rep or account manager, a business buyer's own account area, recommended or related products, and an export of
the store's data to a warehouse or a BI tool. Each cell's `searched` lists the terms; for Salla and Zid in English and in
Arabic, singular and plural, with and without ال. Every hit was read, and each none-held cell's `reading` says what the
hits were and why they aren't cited.

Result: 5 cells `statements`, 19 `none-held`.
- Shopify: CM-B2B-004 (extension-point), CM-B2B-006 (core), CM-B2B-007 (core).
- Salla: CM-B2B-004 (core), CM-MKT-023 (core).
- WooCommerce and Zid: none-held for all six.

## Joins on role (readings)

- **CM-B2B-006, Shopify:** staff assigned to a company location (SH-I-0931, SH-I-1074) is read as the role of
  BigCommerce's Sales Staff assigned to companies. No statement calls them sales reps or says what they do.
- **CM-B2B-007, Shopify:** the B2B customer account (SH-S-7213) and the Customer Account API's company scopes
  (SH-S-5913, SH-S-5926) are read as the buyer's own part of the storefront, BigCommerce's Buyer portal. "A customized
  B2B storefront" (SH-S-7212) is cited too; it is also cited for CM-B2B-001.
- **CM-B2B-004, Salla:** the order status طلب عرض سعر is read as a request for a quote. Nothing ties it to business
  buyers: it may be a general feature, not a B2B one. The reviewer may judge it belongs under CM-B2B-001's parent only
  loosely; I cite it because it is a request for a quote, the capability's object.
- **CM-B2B-004, Shopify:** the App Store category Pricing quote apps is read from its name as quote apps.

## Statements cited from other domains (the checker's flags)

- **SH-I-1897** (Pricing quote apps): placed in SH-C-020, domain B (also G). It is the only Shopify entry naming a quote.
  B-backfill-woocommerce also cites it, as extension-point, for CM-CAT-013 (product pricing). Both cite it as
  extension-point, not core or own-service.
- **SA-C-041/boundary/SA-S-2682** (order status طلب عرض سعر): SA-C-041 is domain C without D. It is the only statement
  that shows طلب عرض سعر as an order status the buyer is told of. Its staff permission and feature flag are in SA-C-040,
  domain C with D under `also`, so they are cited without a flag.
- **SA-C-002/decides/SA-S-2097** (Salla Plus plan line listing منتجات مقترحة): SA-C-002 is domain A without D. It is the
  only plan line naming suggested products. The setting and the flag are in SA-C-020, domain B with D under `also` for
  its recommendations.

## Concerns read under `also`

SA-C-040 (C, also D), SA-C-020 (B, also D). Shopify's SH-C-041 and SH-C-044 are domain D.

## Homonyms and things kept apart

- **"recommendations" in WooCommerce:** the API marketing/recommendations (WC-S-0188, cited for CM-MKT-005) recommends
  marketing extensions to the merchant. It is not product recommendations to buyers.
- **"account manager" in Salla:** مدير حساب مخصص (SA-S-2196) is Salla's account manager for the merchant, not the
  merchant's sales rep for buyers.
- **"مندوب" in Zid:** مندوب جاهز (ZD-S-1066) is a delivery courier.
- **"مندوب" in Salla:** مندوبي (SA-S-2020) and مندوب متجرك الخاص (SA-S-0084) are couriers.
- **"Super Admin" in WooCommerce:** is_super_admin (WC-S-5448, WC-S-5450) is WordPress's multisite super admin, not
  BigCommerce's B2B Edition Super Admin (a sales rep).
- **Wishlists:** Shopify's Wishlist apps (SH-I-1821), Salla's wishlist notifications (SA-S-1761, SA-S-3173), Zid's
  Customer Wishlist (ZD-I-0339) and WooCommerce's lists (WC-S-5456, WC-S-5457) are wishlists (CM-LOY-005), not lists to
  order again, so CM-B2B-005 doesn't cite them.
- **"Reorder" in Salla:** the route orders/reorder (SA-S-1746), its flag order-reorder (SA-S-3280) and the plan line's
  إعادة الطلب (SA-S-2097) are about reordering an order. Reorder Reminder (SA-C-078) is a reminder to buy again. None is a
  list the buyer keeps, so CM-B2B-005 stays none-held. If the reviewer reads "reordering" in BigCommerce's product line
  Requisition lists & reordering as covering a plain reorder, these are the candidates.
- **Upsell and cross-sell against product recommendations:** the model keeps CM-MKT-021 (upsell and cross-sell offers)
  apart from CM-MKT-023. The cross-sell categories of Shopify (SH-I-1846), WooCommerce (WC-I-0517) and Zid (ZD-I-0451),
  and Zid's linked product groups (ZD-S-0916), are left where they are cited. The shopify, woocommerce and zid cells
  for CM-MKT-023 say so. If the coordinator merges the two capabilities, those cells would change.
- **File exports against data sent to outside platforms:** every platform has CSV or file exports (Shopify's Export
  permissions, Salla's export templates, WooCommerce's report export, Zid's Export Data). CM-ANL-007 is BigCommerce's
  "Connect commerce data to BigQuery and leading analytics platforms". No statement of the four names a warehouse or an
  analytics platform as a file export's destination, so they aren't cited.

## Gaps

- No statement on any of the four platforms defines a quote, a shopping list, a sales rep's role or a buyer portal.
  BigCommerce's own cells say the same: its definitions rest on names.
- Salla CM-B2B-004: no statement says how the store returns the quote, or whether the request is limited to business
  buyers. The flag price-quote is on the plan special only.
- Salla CM-MKT-023: no statement says whether Salla or the merchant chooses the products in "You may also like".
- WooCommerce CM-ANL-007: the Marketplace category Marketing > Reporting and analytics (WC-I-0553) is cited by no cell,
  in this part or before. It may belong to CM-ANL-001's WooCommerce cell (the coordinator's call).

## Checker

The final run: `0 problems, 21 flags for the reviewer`.
- **3 flags on statements of another domain without D under `also`:** SH-I-1897, SA-S-2682 and SA-S-2097. They are
  answered above, under "Statements cited from other domains".
- **18 flags on none-held cells whose searched terms match statements:** I read every hit, and each cell's `reading`
  names them and says why they aren't cited. Most of the large counts come from deliberately broad terms: company,
  شركة, B2B, related, analytics, export, تصدير. They return legal-entity statements, payment and shipping companies, tax
  terms, and the platforms' own analytics and file exports. None of those is the capability's object.

## The coordinator's corrections (30 October)

- **Three concerns now name D under `also`,** since the statements this part cites from them bear on D: SH-C-020 (the category Pricing quote apps, SH-I-1897), SA-C-041 (the order status request_quote, SA-S-2682) and SA-C-002 (the plan line listing recommended products, SA-S-2097). The merge flags any of them that another domain also counts as `core`.
- **WC-I-0553,** the Marketplace category Marketing > Reporting and analytics, is cited in CM-ANL-001 already, through its own statement WC-S-0758 (D-woocommerce).

