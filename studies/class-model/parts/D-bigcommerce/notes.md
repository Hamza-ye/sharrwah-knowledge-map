# D-bigcommerce: notes

Domain D, Customers and growth: BigCommerce mapped onto the model of D-anchor, D-woocommerce, D-backfill-woocommerce and
D-zid. The part runs in two batches.

## Batch 1: areas CUS, B2B, MKT and LOY

Concerns: BC-C-032, BC-C-033, BC-C-034, BC-C-007, BC-C-065, BC-C-009, BC-C-010, BC-C-013, BC-C-035 and BC-C-036. Cells:
BigCommerce's, for every capability of the four areas (46 of the model so far, and 5 new: 51).

### How the concerns landed

- **Joined existing capabilities (9):** BC-C-032 Customers in CM-CUS-001 (terms); BC-C-033 Customer login (SSO) and
  current customer in CM-CUS-010 (terms); BC-C-034 Customer groups and segmentation in CM-CUS-002 (terms); BC-C-007
  Price lists in CM-B2B-003 (role, strained); BC-C-065 B2B Edition in CM-B2B-001 (terms); BC-C-009 Promotions in
  CM-MKT-001 (role); BC-C-010 Marketing: coupons, banners and gift certificates in CM-MKT-001 (terms, strained);
  BC-C-035 Subscribers in CM-CUS-007 (role, strained); BC-C-036 Wishlists in CM-LOY-005 (terms).
- **New capabilities (1 concern, 5 capabilities):** BC-C-013 Product recommendations in the new CM-MKT-023. B2B
  Edition's finer parts, each with an API group of its own (and webhook topics or a product line), made four new
  children of CM-B2B-001: CM-B2B-004 Quotes, CM-B2B-005 Shopping lists, CM-B2B-006 Sales reps for business buyers,
  CM-B2B-007 Buyer portal. BC-C-065 lands in their parent.
- **Moved:** none.

### Grains chosen

- **BC-C-065 (B2B Edition)** is the whole add-on, so the parent CM-B2B-001. Its API groups and product lines are cited in
  the children: Company Management, Users, Addresses, Companies and Users and Company account hierarchy in CM-B2B-002;
  Customer-specific pricing and Customer-specific catalogs in CM-B2B-003; Quotes, Shopping List, Sales Staff and Super
  Admin, the Storefront group and Buyer portal in the new ones. Not cited: the Authentication, Channels and Store Settings
  groups (BC-I-0079, BC-I-0090, BC-I-0091, BC-I-0086) and B2B's Catalog storefront group (BC-I-0080), not defined;
  B2B invoices and payments are BC-C-031 (domain C), read, not cited.
- **CM-B2B-007 Buyer portal** rests only on a product line's name and an API group's: the weakest of the new ones. The
  reviewer may fold it into CM-B2B-001 or nest it with CM-CUS-010. Product lines (`other:product-lines`) are cited as
  core, as B-bigcommerce did (CM-CAT-001).
- **BC-C-033** is SSO and Current Customer, coarser than CM-CUS-011, so it lands in CM-CUS-010; its SSO statements are in
  CM-CUS-011, the same tree.
- **Promotions against discounts:** BigCommerce's promotions are its discount engine by its own words (BC-S-0063:
  discount options are its promotions tools), and Marketing > Promotions holds a list Automatic (BC-S-0057), so BC-C-009
  lands in CM-MKT-001; the Automatic list and a promotion's condition (BC-S-0055) are cited in CM-MKT-003 too.
- **BC-C-010** (Marketing API: coupons, banners, gift certificates; plan line Coupons, discounts, and gift cards) lands in
  CM-MKT-001; its coupons in CM-MKT-002, its gift certificates and gift cards in CM-LOY-002. Its banners fit no capability
  of D; scope.tsv names E under `also`, so domain E's BigCommerce part may cite BC-S-0062 for them.
- **Customer groups and segments** are cited together in CM-CUS-002, at the anchor's grain; BigCommerce names both
  (BC-S-0209, BC-I-0532, BC-S-0207) without saying how they differ. Price lists assigned to customer groups (BC-S-0048,
  BC-S-0050) are in CM-B2B-003 only.
- **Product recommendations** (CM-MKT-023) are kept apart from CM-MKT-021 Upsell and cross-sell offers, which no
  platform defines; the reviewer may nest one in the other.
- **BODL** (BC-C-062, batch 2's concern) is cited in CM-MKT-009, read on role as customer events that scripts subscribe
  to (Shopify's SH-S-0708).
- **Feedonomics Surface** (BC-C-067, domain E, naming D) is cited in CM-MKT-010 as core: a plan line that includes it.

### Joins on role

- **CM-B2B-003 / BC-C-007:** Price Lists with Shopify's Catalogs "with wholesale pricing" (SH-S-7212): both set the
  prices a group of buyers sees. Strained (below).
- **CM-MKT-001 / BC-C-009:** Promotions as BigCommerce's discounts (above).
- **CM-CUS-007 / BC-C-035:** newsletter subscribers as email marketing consent, with Shopify's
  customerEmailMarketingSubscribe (SH-S-0881) and WooCommerce's MailPoet subscriber status (WC-S-5500).
- **CM-CUS-011:** the Customer Login API, where "your application" makes the JWT that signs the shopper in (BC-S-0205), as
  Shopify's Multipass. No identity provider is named.
- **CM-B2B-002:** B2B Edition's company users and addresses as Shopify's company contacts and locations.
- **CM-MKT-009:** BODL events (above). **CM-MKT-010:** Feedonomics Surface's ad channels as Salla's linking with ad
  services (SA-S-2149).

### Strained fits

- **BC-C-007 in CM-B2B-003:** a price list holds prices, not which products a buyer sees, and is assigned to customer
  groups and channels; only the plan line's tooltip (BC-S-0049) ties it to B2B. The reviewer may split prices from
  catalogs.
- **BC-C-010 in CM-MKT-001:** its gift certificates and gift cards (BC-S-0062, BC-S-0063) are cited in CM-LOY-002,
  tree CM-LOY-001; its banners are uncited.
- **BC-C-035 in CM-CUS-007:** subscribers are their own records, not stated to be customers, where the capability is
  customers' consent.

### Homonyms kept apart

- **Customer:** in Commerce's legal terms "Customer" is the merchant ("Customer may opt out ... by notifying Commerce",
  BC-S-0346; BC-S-0442, BC-S-0451), and "Shopper" the buyer (BC-S-0443). In the APIs "customer" is the buyer
  (BC-S-0197). The legal hits weren't cited in CUS.
- **Subscriptions:** Storefront Subscriptions (BC-I-0009) are newsletter subscriptions (cited in CM-CUS-007), not
  recurring orders.
- **Super Admin:** B2B Edition's Super Admin is read as a sales rep (its storefront path is sales-rep, BC-I-0084), not the
  store's own administrator.
- **Gift certificates / gift cards:** the Marketing API says gift certificates (BC-S-0062) and the plan line gift cards
  (BC-S-0063); read as one in CM-LOY-002, a reading.
- **Catalog:** B2B Edition's storefront Catalog group (BC-I-0080) isn't the Catalog API (domain B); not cited.
- **Automatic:** BigCommerce's Automatic promotions (BC-S-0057) against automatic plan upgrades (BC-S-0186, BC-S-0187) and
  the default webhook scope (BC-S-0306): only the first is cited.

### Concerns read under `also`

- **BC-C-015 Abandoned carts (C):** BC-S-0087, BC-S-0088, BC-S-0089, BC-S-0090 and BC-I-0501 cited as core in CM-MKT-022.
  The carts API (BC-I-0033) and the topic store/cart/abandoned (BC-S-0091) are the carts themselves, not recovery: not
  cited. If C's BigCommerce part cites BC-S-0090 or BC-S-0089 as core, the merge flags it.
- **BC-C-067 Feedonomics (E):** BC-S-0365 cited as core in CM-MKT-010, with five ad channels as slot fillers and the basic
  plan's SKU limit as a quality. BC-S-0364, BC-S-0366, BC-S-0367 and BC-I-0547 name Feedonomics Holdings, LLC as the
  party of its own agreement; no statement says it is BigCommerce's group company, so no own-service (a maker gap).
- **BC-C-024 Stored payment instruments (C):** read; payment methods, not a store credit balance. Not cited.
- **BC-C-031 B2B invoices and payments (C):** read; not cited. Its credit limits (BC-S-0194) are named in CM-LOY-001's
  reading as a hit that isn't a buyer's balance.
- **BC-C-044 Scripts (E):** read; adding client-side code to storefront pages (BC-S-0247) says nothing of tracking: not
  cited in CM-MKT-009.
- **BC-C-081 Personal data processing roles (A):** read; its shopper statements (BC-S-0443, BC-S-0444) are Commerce as a
  processor, not consent to marketing. Not cited.

### Qualities and gaps

- **Recommended active promotions** (BC-S-0059, CM-MKT-001): "less than 100 active promotions ... at most ten rules per
  promotion".
- **Feedonomics Surface basic plan** (BC-S-0365, CM-MKT-010): "free for up to 100,000 SKUs".
- **Plan lines without plans:** Price Lists (BC-S-0049) and Advanced promotions management (BC-S-0058) carry the plan
  table as scope; which plans include them rests on Q1's notes marked as inference, which don't count.
- **No control panel section held** for customers, customer login or subscribers (Q1's gaps BC-C-032/decides,
  BC-C-033/decides, BC-C-035/decides, all "page not read"), nor for wishlists (BC-C-036/decides; its boundary searched,
  not found).
- **Not defined by BigCommerce in a statement held:** quotes, shopping lists, sales staff, the buyer portal,
  customer-specific catalogs, BODL, gift certificates against gift cards, and how customer groups differ from segments.

### Rulings

None. BigCommerce's concerns are in no Q1 match or unclear candidate (`concerns` prints none, and the brief says
BigCommerce has none), so `rulings.tsv` holds its header only.

### Proposed renames (for the coordinator)

- CM-B2B-001: add BigCommerce's B2B Edition. CM-B2B-002: add B2B Edition's Company Management, company users.
- CM-B2B-003: add BigCommerce's Price Lists and Customer-specific catalogs.
- CM-CUS-002: add BigCommerce's Customer groups and segmentation. CM-CUS-007: add BigCommerce's newsletter subscribers.
- CM-CUS-011: add BigCommerce's Customer Login (SSO).
- CM-MKT-001: add BigCommerce's Promotions. CM-MKT-003: add BigCommerce's Automatic promotions.
- CM-MKT-022: add BigCommerce's Abandoned cart saver.

### What the checker flagged (batch 1)

0 problems, 25 flags.
- **own-service on BC-S-0354 (CM-B2B-001):** the statement reads "B2B Edition — BigCommerce's add-on for
  business-to-business commerce": it names BigCommerce as the maker of a separate add-on. B2B Edition's APIs and scope
  are cited as core besides (C1).
- **CM-MKT-009, core only on boundary statements:** BC-S-0341 names the control panel as well as the GraphQL Admin API's
  mutation for enabling BODL, BigCommerce's own setting.
- **BC-S-0062 and BC-S-0063 in two trees** (CM-MKT-001/002 and CM-LOY-002): each names coupons or discounts and gift
  certificates or gift cards in one sentence; each part is cited where it belongs. BC-C-010 is strained for it.
- **`none-held` with matches:** each cell's reading names its hits for the searched terms and why none is the capability:
  CM-CUS-003, -005, -006, -009, -014; CM-MKT-004, -006, -007, -008, -011, -013, -014, -016, -017, -018, -019, -020;
  CM-LOY-001, -004, -006, -007. The other hits the checker lists come from the other platforms' terms matching words in
  unrelated statements: "automatically" (plan upgrades BC-S-0186, BC-S-0187; stored cards BC-S-0135; default scope
  BC-S-0306) for CM-MKT-006; "source" and "order" words across 121 statements for CM-MKT-008; "availability" and
  "notify" (BigCommerce Payments availability BC-S-0143, availability zones BC-S-0450, Third-Party Products BC-S-0462,
  PCI in-product notifications BC-S-0166, Agentic Search opt-out BC-S-0346, data transfer BC-S-0451, IP notices
  BC-S-0480) for CM-MKT-016 and -017; "bank" (late payments BC-S-0189, transactional currency BC-S-0408, Bank of New
  Zealand BC-I-0440) for CM-MKT-018; the tax API (BC-S-0383) for CM-MKT-019; "points" only in "endpoints" for
  CM-LOY-004; the login-access topic (BC-S-0204, cited in CM-CUS-010) for CM-CUS-005; BigCommerce's built-in content
  (BC-S-0257) for CM-CUS-014. None is the capability.

### What batch 2 (areas SUP, ANL and NTF) needs

- **Its concerns:** BC-C-012 Product ratings and reviews, BC-C-046 Email templates and transactional emails, BC-C-062
  Reporting and analytics. Under `also`: BC-C-015, BC-C-024, BC-C-031, BC-C-044, BC-C-067, BC-C-081.
- **Already cited by batch 1 from batch 2's concerns:** BC-C-062/decides/BC-S-0340 (extension-point) and
  BC-C-062/boundary/BC-S-0341 (core) in CM-MKT-009, BODL. By S1, BC-C-062 lands `strained` unless it lands in
  CM-MKT-009's tree; its Settings V3: Analytics, "Identifies and updates Web analytics providers" (BC-S-0337), is left to
  batch 2 and may bear on CM-MKT-009 too.
- **Left for SUP:** the App Marketplace category CRM & Customer Service (BC-I-0483) is cited in CM-CUS-001 only; it names
  customer service too, so batch 2 may cite it in CM-SUP-004 (the checker will flag the two trees, as D-zid's did).
- **Left for ANL:** BC-S-0081 (Product Recommendations train on BigCommerce Analytics' data, cited as `shows` in
  CM-MKT-023) names "the native BigCommerce Analytics", which batch 2 may cite in CM-ANL-001 as well.
- **Left for NTF:** the transactional emails and templates (BC-C-046: BC-S-0258 to BC-S-0261, Marketing › Transactional
  Emails) are named in CM-MKT-005's and CM-MKT-007's readings but not cited; the Abandoned Cart Saver notifications
  (BC-S-0089) and abandoned cart emails (BC-S-0088) are cited in CM-MKT-022 and bear on NTF; the notification topics
  store/channel/{channel_id}/notifications/order/updated (BC-I-0248, D) and abandonedCart (BC-I-0246, C) aren't cited.
- **App Marketplace category for ANL:** Analytics & Reporting (BC-I-0478, placed in BC-C-059 and BC-C-062).
