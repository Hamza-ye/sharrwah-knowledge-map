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

## Batch 2: areas SUP, ANL and NTF

Concerns: BC-C-012, BC-C-046 and BC-C-062. Cells: BigCommerce's, for every capability of the three areas (18 of the
model so far, and 1 new: 19).

### How the concerns landed

- **Joined existing capabilities (3):** BC-C-012 Product ratings and reviews in CM-SUP-001 (terms); BC-C-046 Email
  templates and transactional emails in CM-NTF-001 (terms); BC-C-062 Reporting and analytics in CM-ANL-001 (terms,
  strained).
- **New capability (no concern of its own):** CM-ANL-007 Commerce data sent to outside analytics platforms and data
  warehouses, child of CM-ANL-001, for Big Open Data Solutions (BC-S-0336, product line BC-I-0541). BC-C-062 lands in
  the parent.
- **Moved:** none.

### Grains chosen

- **BC-C-062** is coarser than CM-ANL-001's children: Professional reporting tools (BC-S-0338) in CM-ANL-002 Reports,
  Big Open Data Solutions in CM-ANL-007, the Commerce Analytics Service (BC-S-0339), Settings V3 Analytics (BC-S-0337),
  the product line Reporting & analytics and the App Marketplace category Analytics & Reporting in CM-ANL-001 itself. So
  it lands in the parent. Its BODL statements are batch 1's, in CM-MKT-009.
- **Big Open Data Solutions** has a place of its own (a product line), so it is a capability; it is not CM-ANL-006, which
  is apps reading reports through the platform's API. Its parent CM-ANL-001 is a reading (see the capability's note).
- **Settings V3: Analytics** ('Identifies and updates Web analytics providers', BC-S-0337) is cited in CM-ANL-001 as
  extension-point, a reading: a setting for outside providers that do the analytics. It isn't cited in CM-MKT-009: no
  statement says the providers track customer events on the storefront. Which providers isn't stated. A reviewer reading
  it as BigCommerce's own settings API for its own feature (C1) would make it core.
- **BigCommerce Analytics against Commerce Analytics:** 'the native BigCommerce Analytics' (BC-S-0081) and 'the Commerce
  Analytics Service' (BC-S-0339) are both cited in CM-ANL-001; no statement says whether they are one product.
- **Professional reporting tools in CM-ANL-002:** a reading, that reporting tools are the store's reports. No control
  panel section for reports or analytics is held.
- **Transactional emails** are the store's automatic messages, so CM-NTF-001, though BigCommerce puts the page under
  Marketing (BC-S-0259); the channel doesn't set the area. The topic notifications/order/updated (BC-I-0248, placed in
  BC-C-046) is cited there too; its recipient isn't stated, so it is not in CM-NTF-002.
- **Abandoned Cart Saver** emails and notifications (BC-S-0088, BC-S-0089, BC-S-0090; BC-C-015, domain C) stay in
  CM-MKT-022 (batch 1); citing them in CM-NTF-001 too would put a domain C statement in two trees for one feature.
- **Google customer reviews** (BC-I-0415, placed in BC-C-012) is cited in CM-SUP-001 as a plan line; what it does isn't
  stated, and Google is named only in the line's name, so it is no slot filler.
- **CRM & Customer Service** (BC-I-0483) is cited in CM-SUP-005 for its customer service, as batch 1 left it; it is in
  CM-CUS-001 for its CRM.

### Joins on role

None in this batch: the three joins are on terms. Readings within cells: Settings V3 Analytics as a provider interface
(CM-ANL-001); CRM & Customer Service as support apps (CM-SUP-005, on its name).

### Strained fits

- **BC-C-062 in CM-ANL-001:** its BODL statements (BC-S-0340, BC-S-0341) are cited in CM-MKT-009, Customer events and
  tracking pixels, another tree. The reviewer may split BODL from reporting.

### Earlier batch's rows that no longer hold (for the coordinator)

The checker flags two of batch 1's landings as needing `strained` (S1), because of this batch's citations, which follow
the cells as the brief says:
- **BC-C-013 in CM-MKT-023:** its BC-S-0081 ('the native BigCommerce Analytics') is now cited as core in CM-ANL-001, as
  batch 1's notes proposed. Its fit should be `strained`, with the reading naming CM-ANL-001.
- **BC-C-032 in CM-CUS-001:** BC-I-0483 (CRM & Customer Service, placed in BC-C-032) is now cited as extension-point in
  CM-SUP-005, as batch 1's notes proposed. Its fit should be `strained`, with the reading naming CM-SUP-005.

### Homonyms kept apart

- **Notifications:** the abandoned cart notifications (BC-I-0246, BC-S-0089) and inventory notifications (BC-S-0033,
  BC-I-0247, domain B) are not the store's transactional messages; only BC-I-0248 (order) is cited in CM-NTF-001.
- **Logs:** System Logs and Store logs (BC-S-0331, BC-S-0332, domain G) are debugging and audit logs, not a log of sent
  messages (CM-NTF-003).
- **Dashboard:** the Money Dashboard (BC-S-0141, domain C) is payments' balances and payouts, not a store performance
  overview (CM-ANL-003).
- **Reviews:** PayPal Braintree reviewing its accounts (BC-S-0156), the Marketplace team reviewing apps (BC-S-0325) and
  reviewing MCP terms (BC-S-0345) are not product reviews; not cited.
- **Messages:** order messages (BC-S-0103, BC-I-0168, BC-I-0254) aren't stated to be a chat with buyers (CM-SUP-004).

### Concerns read under `also`

BC-C-015, BC-C-024, BC-C-031, BC-C-044, BC-C-067 and BC-C-081 were read by batch 1; none bears on SUP, ANL or NTF
beyond the abandoned cart emails (above). Statements of other domains are named only in `none-held` readings, not cited.

### Qualities, slot fillers and gaps

- **Slot fillers:** BigQuery, Tableau, Power BI and Looker (BC-S-0336), the platforms Big Open Data Solutions sends data
  to, in CM-ANL-007.
- **No quality** stated: the Commerce Analytics fees are 'charged in advance based on your store plan' (BC-S-0339), with
  no amount.
- **Gaps:** BC-C-012's boundary is 'searched, not found' (no scope or webhook topic for reviews), though BC-S-0072 names
  the GraphQL Storefront API; no statement held shows product questions. No control panel section is held for reviews,
  reports or analytics. Not defined in a statement held: Google customer reviews, Commerce Analytics against BigCommerce
  Analytics, which web analytics providers, which transactional emails are sent and to whom, what notifications/order
  is, and the product line Conversational shopping (BC-I-0516). Which plans include Big Open Data Solutions isn't stated.
  The responsible placements of all three concerns are stated only in general terms, and no reason is held.

### Rulings

None: BigCommerce's concerns are in no Q1 match or unclear candidate (`concerns` prints none).

### Proposed renames (for the coordinator)

- CM-SUP-001: add BigCommerce's Product ratings and reviews. CM-NTF-001: add BigCommerce's Transactional Emails, Email
  Templates. CM-ANL-001: add BigCommerce's Reporting & analytics, Commerce Analytics. CM-ANL-002: add BigCommerce's
  Professional reporting tools.

### What the checker flagged (the whole part, after batch 2)

0 problems, 42 flags. Batch 1's flags are answered in its section; those still standing are the same. This batch's:
- **BC-C-013/reason/BC-S-0081 in CM-ANL-001 and CM-MKT-023:** it names the native BigCommerce Analytics (core here) as
  the source of the recommendations' training data (shows there); each part is cited where it belongs. Batch 1's landing
  of BC-C-013 should be strained (above).
- **BC-I-0483 in CM-CUS-001 and CM-SUP-005:** the category's name holds CRM and customer service; each half is cited
  where it belongs. Batch 1's landing of BC-C-032 should be strained (above).
- **Landings BC-C-032 and BC-C-013 clean with statements in another tree:** batch 1's rows, for the coordinator (above).
- **`none-held` with matches:** each cell's reading names its hits for the searched terms and why none is the
  capability: CM-SUP-002, -003, -004, -006, -007, -008; CM-ANL-003, -004, -005, -006; CM-NTF-002, -003, -004. The other
  hits the checker lists come from the other platforms' terms matching words in unrelated statements: "overview" in API
  overview pages and "performance" or "dashboard" across 26 statements (Catalyst BC-S-0281, storefront tokens BC-S-0292,
  payment statements BC-S-0145, plan upgrades BC-S-0187) for CM-ANL-003; "reviews", "reports" and "query" words (product
  reviews BC-S-0072, recommendations BC-S-0080, BC-S-0081, segmentation BC-S-0207, storefront tokens BC-S-0293) for
  CM-ANL-006; "staff" and "order" in Sales Staff (BC-I-0098), Staff accounts (BC-S-0334, BC-I-0402) and System Logs
  (BC-S-0331) for CM-NTF-002; "email" and "sent" in transactional emails (cited in CM-NTF-001), abandoned cart emails
  (CM-MKT-022), stored cards (BC-S-0135) and webhook deactivation (BC-S-0318) for CM-NTF-003 and CM-NTF-004. None is the
  capability.

## The coordinator's corrections after batch 2 (30 October)

- **BC-C-013 and BC-C-032 are `strained`.** Batch 2 cites BC-S-0081 in CM-ANL-001 and BC-I-0483 in CM-SUP-005, other trees (S1).
- **Six capabilities added** (CM-B2B-004 to CM-B2B-007, CM-MKT-023, CM-ANL-007): `D-backfill-bigcommerce` writes their cells for the other four platforms.

