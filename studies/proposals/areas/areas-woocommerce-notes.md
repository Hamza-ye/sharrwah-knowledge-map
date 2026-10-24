# woocommerce (WC): notes on the broad areas

## Under none

No concern is under none: each of the 118 concerns in the extract is placed under one of the 28 areas.

## Names that were hard to read

- `wooads-policy` [legal-agreements]: the extract gives only this slug. Its citation, WC-S-0842 in `studies/concern-map/platforms/woocommerce/citations.tsv`, is the page sitemap entry `https://woocommerce.com/wooads-policy/`, so it is the policy page for WooAds (concern WC-C-114). I named the area by the concern's term `WooAds [term]` instead of the slug.
- `WooCommerce` [other:tos-woo-services] and its four siblings: the list's name alone did not say what the list was. Its citation, WC-S-0458 (wordpress.com/tos, "1. Who's Who: Woo Services"), says "Woo services include WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet, and other products or services available at WooCommerce.com." So the list names the Woo services the Terms of Service cover, and I used its entries as names for those services.
- `You created %s` [other:onboarding-tasks]: its citation, WC-S-0429, is the onboarding task that fills `%s` with the site's name. It says the store was created; it belongs with WC-C-081 (Home and setup) and needed no name of its own.
- "Designated Countries" (scopes of WC-C-006, WC-C-023, WC-C-113): the extract does not list them. The plain line of WC-A-08 uses the platform's phrase without naming the countries. I did not look further, as the brief allows only the passage behind a name.

## What the extract seemed to lack

- The extract gives cite ids only for list entries (the `WC-S-` ids), not for concerns' terms, so a term that is unclear can't be traced to its passage from the extract alone.
- The extract prints the entries of `api-resources`, `extension-points`, `webhook-topics` and `access-scopes` without their concern ids, so I could not see where they would fall until the script ran. The script did find concerns for all of them and placed every one.
- The extract does not say which countries are the "Designated Countries" that decide which Woo company contracts, nor does it list the countries WooPayments serves or the store countries behind the payment suggestions (only the twelve most frequent scopes of WC-C-004). WC-A-06 names these lists without being able to say what is in them.
- WC-C-088 (Features) sits on all 32 entries of `other:features`, beside each entry's own concern, so 30 of those 32 entries fall in two areas (see `## Entries`).

## Entries

`place_entries.py` placed 645 entries (the 654 in the inventory less the 9 out of the concern map's scope), with 0 under none. 143 of them (22%) fall in more than one area. The split comes mostly from entries that the concern map gives both a subject concern and a mechanism concern, and so it follows from placing each concern under one area:
- `api-resources` (52): an endpoint carries its subject's concern (products, orders, customers, coupons) and also the REST API or Store API (WC-C-078, WC-C-079; 32 entries) or Analytics (WC-C-038; 19 entries). They fall in WC-A-22 or WC-A-19 and in their subject's area.
- `other:features` (30): every feature carries WC-C-088 (Features, in WC-A-21) beside its own concern. So WC-A-21 holds all 32 features, including ones that its plain line covers only as "features a merchant turns on or off" (Wishlists, Point of Sale, Cost of Goods Sold and so on).
- `webhook-topics` (16): each topic carries Webhooks (WC-C-077, WC-A-22) and its subject (products, orders, customers, coupons).
- `other:emails` (12): emails about refunds, accounts, POS, fulfillments, reviews and withdrawals carry Emails (WC-A-18) and their subject's area.
- A few entries spread wide: `Terms of Service` [legal-agreements] carries 14 concerns and falls in seven areas (WC-A-01, 02, 07, 08, 09, 10, 11); `Our Policies` [other:woopayments-doc-topics] falls in five (WC-A-01, 02, 03, 07, 10); `Integration` [settings] falls in WC-A-06 (MaxMind Geolocation) and WC-A-22 (the integration framework).

What sits oddly against the plain lines:
- WC-A-06 holds the 46 payment provider suggestions (through WC-C-004) and also `Compatibility` [other:woopayments-doc-topics], through WC-C-010. Its plain line covers the suggestions by store country.
- WC-A-10 holds `Our Policies`, `Terms of Service` and `wooads-policy` because they carry WC-C-049 or WC-C-117 among others; the area's plain line covers only their passages on data sent to Woo.
- WC-A-20 holds most `wc-admin` endpoints (notices, features, experiments, options, plugins, onboarding) through WC-C-081, which its plain line covers as "onboarding tasks and inbox".

## Re-cut after the review

The coordinator re-cut these areas after the review of the areas list (`review.md`, findings 3 and 6), on 18 October 2026. Each area's note says why.
- WC-A-29 holds merchant financing through Stripe Capital (from WC-A-03).
- WC-A-30 holds the WordPress.com account and Jetpack connection (from WC-A-10).
- The counts of areas and entries given above predate the re-cut. `areas-woocommerce.tsv` and `areas-woocommerce-entries.tsv` hold the current areas and placing.
