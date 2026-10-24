# Cards: what the proposals cite as not found or absent, on bigcommerce

6 records, from Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8.

## The points cited

- **Q1, section 1, line 48:** - Shopify's payments terms let it "add a new Designated Country"; BigCommerce says "Additional regions and countries will be launching soon"; WooCommerce ranks "new countries and currencies" partly by store owners' requests. What adding a country involves on the platform's side was not in what was read for Shopify or BigCommerce. Q1-SH-K1604, Q1-BC-P0030, Q1-WC-K0403, Q1-SH-N02, Q1-BC-N04
- **Q1, section 5, line 123:** - Where store data is kept. New Shopify merchants in Europe have their data at rest in Europe, a BigCommerce store's data region is a copied gap, and Yemen's evidence bears on it (section 6). Keep each store's data location, set at creation from its operating place; a company decision with a lawyer settles it. Q1-SH-K2321, Q1-BC-G0154
- **Q1, section 7, line 145:** - Where sellers' data is stored. Q1-SH-K2321, Q1-BC-G0154, YK-290 (regular books, computer systems kept in Yemen @ the unified Republic's area, as of 2005)
- **Q4, section 1, line 51:** - **Shopify and BigCommerce.** A service of either that collects cash on delivery for the seller was not in what was read. For sellers in Italy, Shopify's Help Center points to App Store apps related to COD. Q4-SH-N01, Q4-BC-N16, Q4-SH-046
- **Q4, section 2, line 93:** - Why: rule 4 (the last responsible moment), because who holds the cash is unsettled (section 5); rule 2, its own part. A service of this kind of Shopify's or BigCommerce's own was not in what was read. Q4-SH-N01, Q4-BC-N16
- **Q5, section 1, line 37:** - Money held when a merchant leaves the own service is paid out: WooPayments' remaining balance "will still be paid out as per your usual schedule"; Zid's, "يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي", though not before its financing is repaid. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-BC-H0040
- **Q5, section 1, line 38:** - What checkout does when a provider is down was not in what was read on BigCommerce or Salla. Shopify routes cards to a third-party provider, with Shopify Payments as backup, when the two run alongside. Q5-BC-G0048, Q5-SA-G0224, Q5-SH-041
- **Q5, section 5, line 135:** - What checkout does when a provider is down, which was not in what was read on BigCommerce or Salla: the design keeps room for a backup provider per method, as Shopify has. Providers' service terms and testing settle it. Q5-BC-G0048, Q5-SA-G0224, Q5-SH-041
- **Q5, section 7, line 160:** - Which payment providers Sharrwah works with at each place, and on what terms: notice before withdrawal, refunds after it, settlement time, and service when a provider is down. Q5-BC-102, Q5-SH-064, Q5-WC-033, Q5-BC-G0048
- **Q5, section 8, line 200:** - Records: Shopify's funds in custody are paid out "subject to the Payment Processor Terms"; WooPayments' and Zid's balances are paid out, Zid's not before its financing is repaid; Salla may stop the service and close the store for a breach. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. S01-VP-20, Q5-SH-P0033, Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-SA-P0083, Q5-BC-H0040
- **Q8, section 1, line 23:** - Named conditions of this kind were not in what was read on Zid or BigCommerce. Q8-ZD-N03; Q8-BC-N05

## The cards

### Q1-BC-N04

**Cited at:** Q1, section 1, line 48

**Record** (`studies/proposals/records/Q1/bigcommerce/not-found.tsv`):
- nf_id: Q1-BC-N04
- bears_on: 4
- what_is_missing: What BigCommerce says adding a country or region where BigCommerce Payments, or the platform itself, is offered involves, beyond that additional regions and countries "will be launching soon"
- kind: not in what was read
- read: https://www.bigcommerce.com/payments/bigcommerce-payments/ (held, captured 2026-10-12); https://www.commerce.com/press/commerce-delivers-bigcommerce-payments-by-paypal-to-simplify-payments-and-accelerate-merchant-growth/ (held, line read); https://www.commerce.com/terms/jurisdiction-specific-terms/ (held, captured 2026-10-12)
- searched: python3 -I method/corpus_search.py bigcommerce "launching soon" "expand internationally" "additional regions" "new countries" --max 10 (2 documents, both opened)
- who_can: agent
- route: read https://www.bigcommerce.co.uk/payments/ and https://www.commerce.com/press/ for later announcements

### Q1-BC-G0154

**Cited at:** Q1, section 5, line 123; Q1, section 7, line 145

**Record** (`studies/proposals/records/Q1/bigcommerce/copied-gaps.tsv`):
- concern_id: BC-C-082
- placement: decides
- what_would_show_it: A statement of which region a store's data is stored in, and whether a merchant can choose it
- means: commit the held archive
- who_can: founder
- route: https://security.bigcommerce.com/ held only in an index: sharrwah-knowledge-map:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/010-security.bigcommerce.com/text.txt (capture, 403)
- why_not_held: Stage 0, 17 October 2026: the page is held, but its archive is not in git. Before: page not read, founder, save a page from a browser. The Platform Trust Center returns a Cloudflare security check (HTTP 403) to this session. The DPA, Privacy Policy and subprocessor list were read: they allow storage in regions where Commerce.com or its subprocessors operate, and list hosting in the USA, Germany or Australia, but state no per-store region or merchant choice.
- gap_kind: page not read

### Q4-BC-N16

**Cited at:** Q4, section 1, line 51; Q4, section 2, line 93

**Record** (`studies/proposals/records/Q4/bigcommerce/not-found.tsv`):
- nf_id: Q4-BC-N16
- bears_on: 5
- what_is_missing: A BigCommerce service, or an app it names, that collects cash on delivery or another offline payment for the merchant and pays it out
- kind: not in what was read
- read: https://support.bigcommerce.com/s/article/Offline-Payment-Methods?language=en_US (held capture, read 2026-10-19); https://support.bigcommerce.com/s/article/Processing-Refunds (held capture, read 2026-10-19); https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US (held capture, read 2026-10-19); https://docs.bigcommerce.com/developer/docs/admin/checkout-and-cart/payments/overview.md (held capture, read 2026-10-19); https://docs.bigcommerce.com/developer/api-reference/rest/b2b/management/payment.md (held capture, read 2026-10-19)
- searched: command: python3 -I method/corpus_search.py bigcommerce "cash on delivery" "COD" "collect cash" "collects cash" "remit" "remittance" --max 10 | opened: Offline-Payment-Methods, Processing-Refunds, Available-Payment-Gateways, payments/overview.md, b2b/management/payment.md | listed, not read: the three Unified Billing terms pages, bigcommerce.com/apps/
- who_can: agent

### Q5-BC-H0040

**Cited at:** Q5, section 1, line 37; Q5, section 8, line 200

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot-gaps.tsv`):
- gap_id: S01-BC-G39
- bullet: c
- what_is_missing: What happens to the merchant's funds when BigCommerce Payments or a provider is disconnected, or the store or account is closed: the BigCommerce Payments article says how to disconnect it and to contact BigCommerce support to "discontinue the service", and says nothing of the funds.
- read: sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt (Connecting with BigCommerce Payments, read in full); sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/002-support.bigcommerce.com/text.txt (Available Payment Gateways, read in full); sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/003-support.bigcommerce.com/text.txt (Connecting with PayPal, read in full); sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/004-support.bigcommerce.com/text.txt (Connecting with Stripe OCS, read in full); sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/005-support.bigcommerce.com/text.txt (Connecting with Braintree, read in full); sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt (Offline Payment Methods, read in full); sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013 … (3924 characters; `record_ids.py --all` prints it whole)
- gap_kind: searched, not found
- who_can: founder
- route: a question to BigCommerce support or PayPal support; the BigCommerce Payments settings and Balance dashboard of a US or UK store using BigCommerce Payments (http://login.bigcommerce.com/deep-links/manage/balance)

### Q5-BC-G0048

**Cited at:** Q5, section 1, line 38; Q5, section 5, line 135; Q5, section 7, line 160

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-gaps.tsv`):
- concern_id: BC-C-026
- placement: decides
- what_would_show_it: A BigCommerce statement of what a store's checkout does when a connected payment provider is unavailable or fails
- means: read the held page
- who_can: agent
- route: https://support.bigcommerce.com/s/article/Available-Payment-Gateways held at sharrwah-knowledge-map:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/002-support.bigcommerce.com/text.txt (capture, 200)
- why_not_held: Stage 0, 17 October 2026: the page is held, and the run could not read it. Before: page not read, founder, save a page from a browser. The Help Center (support.bigcommerce.com) renders blank in this session: its script bundles return HTTP 400 to the headless browser and its llms.txt redirects to a login page, so no Help Center article was read. The Payments API page lists error code 10000 ("We're experiencing difficulty processing your transaction. Please try again later.") but states no fallback.
- gap_kind: page not read

### Q8-BC-N05

**Cited at:** Q8, section 1, line 23

**Record** (`studies/proposals/records/Q8/bigcommerce/not-found.tsv`):
- nf_id: Q8-BC-N05
- bears_on: 2
- what_is_missing: Named conditions that decide which parts of the control panel or which features a store can reach, according to its plan, place or beta enrolment
- kind: not in what was read
- read: sharrwah-knowledge-map@f37eb8796cd351c46011ba4f9c2f4eb71a2c5fb1:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/103-bigcommerce.com/text.txt, sharrwah-knowledge-map@f37eb8796cd351c46011ba4f9c2f4eb71a2c5fb1:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/097-bigcommerce.com/text.txt, sharrwah-knowledge-map@f37eb8796cd351c46011ba4f9c2f4eb71a2c5fb1:evidence/product-class/runs/20261012T0426Z-q1-bigcommerce-sources-2/items/010-docs.bigcommerce.com/text.txt, sharrwah-knowledge-map@f37eb8796cd351c46011ba4f9c2f4eb71a2c5fb1:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/119-commerce.com/text.txt, sharrwah-knowledge-map@f37eb8796cd351c46011ba4f9c2f4eb71a2c5fb1:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/060-docs.bigcommerce.com/text.txt
- searched: python3 -I method/corpus_search.py bigcommerce Services "new features" edition editions "release notes" "product update" "product updates" "additional services" add-on add-ons composable component components "control panel" international market markets category categories extension extensions function functions entitlement entitlements "feature flag" "feature flags" "open source" open-source "paid services" package packages experimental theme themes "agency partner" "agency partners" "technology partner" "technology partners" certified badge badges integration integrations --max 10 ; opened: https://docs.bigcommerce.com/developer/docs/beta/checkout-extensions/overview.md, https://www.commerce.com/terms/store-terms/, https://www.bigcommerce.com/apps/, https://www.bigcommerce.com/product/, https://docs.bigcommerce.com/developer/api-reference/rest/integrations/tax-provider.md; not read: the other documents it listed
- who_can: agent
