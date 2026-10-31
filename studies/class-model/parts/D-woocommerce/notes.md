# D-woocommerce: notes

WooCommerce's concerns of domain D, mapped onto the model D-anchor built. The part runs in two batches. Read through
`class_slice.py` only: `seed`, `model --areas`, `concerns --where`, `statements`, `gaps`, `matches`, `key`, `search`,
`candidates` and `homonyms`. Searches are in English, WooCommerce's only language in the concern map. Every placement
below is a reading of the statements cited.

## Batch 1: CUS, B2B, MKT and LOY

Eleven concerns: WC-C-073, WC-C-103, WC-C-069, WC-C-074, WC-C-084, WC-C-085, WC-C-105, WC-C-110, WC-C-113, WC-C-114 and
WC-C-097. WooCommerce's cell is written for all 45 capabilities of the four areas and for the one this batch adds.

### How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| WC-C-073 Customer accounts | CM-CUS-001 | match:M-018 | strained |
| WC-C-103 B2B selling | CM-B2B-001 | match:M-020 | clean |
| WC-C-069 Back-in-stock notifications | CM-MKT-016 | match:M-080 | clean |
| WC-C-074 Coupons | CM-MKT-002 | match:M-050 | clean |
| WC-C-084 Marketing hub | CM-MKT-005 | match:M-051 | clean |
| WC-C-085 Order attribution | CM-MKT-008 | match:M-053 | clean |
| WC-C-105 Conversion extensions | CM-MKT-021 | terms | strained |
| WC-C-110 Marketing extensions | CM-MKT-005 | match:M-051 | strained |
| WC-C-113 MailPoet | CM-MKT-007 | match:M-052 | strained |
| WC-C-114 WooAds | CM-MKT-010 | role | clean |
| WC-C-097 Shopper lists | CM-LOY-005 | terms | clean |

All eleven joined existing capabilities, and none made a new one. One new capability, CM-MKT-022, holds a statement of
WC-C-105, which lands in CM-MKT-021.

**New capability: CM-MKT-022, abandoned cart and order recovery.** WooCommerce gives it a Marketplace category of its
own, Extensions > Conversion > Recovering orders (WC-S-0719). That is an app category, the dry run's test for a
capability. Nothing in the model held it: Shopify's abandoned checkouts (SH-C-050) and Salla's abandoned carts (SA-C-048)
are domain C in scope.tsv. Both name D under `also`, and both have a recovery part: Shopify's plan includes "abandoned
cart recovery features" (SH-S-7224), and Salla's plan line استهداف السلات المتروكة sends reminder messages to customers
who left a cart (SA-S-2099), at the link /marketing/carts (SA-S-1814). The back-fill may cite them in CM-MKT-022's Shopify
and Salla cells. The capability rests on a category name: no WooCommerce statement held says what recovering an order
is. It has no parent, because no platform's grouping puts it under discounts or campaigns. Domain C's part may build its
own capability for abandoned checkouts as records. The coordinator decides whether the recovery stays a capability of
D's. The checker's flag "CM-MKT-022 has no concern landed in its tree" is expected: WC-C-105 lands in CM-MKT-021 for its
upsells and cross-sells, and the other two concerns are domain C's.

### Grains I chose

- **WC-C-073: one concern for records and accounts.** Q1's M-018 notes that WooCommerce keeps customer records and
  customer accounts in one concern, while Shopify splits them (SH-C-039 in CM-CUS-001, SH-C-041 in CM-CUS-010). The
  concern lands with the match in CM-CUS-001. Its account statements are cited in CM-CUS-010: Accounts & Privacy and its
  settings for account creation and guest checkout, wc/v4 settings-account, and the New account and Reset password
  emails. That makes it strained (S1). The checker's flag that M-018's concerns land in two trees comes from the
  anchor's own split, and this part follows it.
- **WC-C-105 and WC-C-110 are Marketplace category groups.** They are cut the way B-woocommerce cut WC-C-104 and
  G-woocommerce cut WC-C-109. Each lands in one capability, strained, and its subcategories are cited where they belong:
  - WC-C-105, Conversion: Promotions in CM-MKT-001, Recovering orders in CM-MKT-022, Rewards and loyalty in CM-LOY-004,
    Upsells and cross-sells in CM-MKT-021 (its landing, by the terms), and the Back In Stock Notifications extension in
    CM-MKT-016.
  - WC-C-110, Marketing: Extensions > Marketing in CM-MKT-005 (its landing, by M-051), Automation in CM-MKT-006, Email in
    CM-MKT-007, and Advertising and promotions in CM-MKT-010.
- **Promotions sits at the parent.** WooCommerce's category Promotions (WC-S-0718) is cited in CM-MKT-001, not in
  CM-MKT-003 (automatic discounts). No statement says whether its promotions apply without a code. CM-MKT-003's cell is
  `none-held`, and the checker's flag on it (hits WC-S-0718 and WC-S-0755) is answered by this placement.
- **Shopper lists.** Both of WooCommerce's lists, wishlist and saved-for-later (WC-S-5456), are products a buyer saves,
  so the whole concern fits CM-LOY-005. A reviewer who wants saved-for-later apart would need a capability that only
  WooCommerce shows.
- **Coupons.** WC-C-074's Analytics > Coupons statements (WC-S-0071, WC-S-0208, WC-S-0238, WC-S-0239) and WC-C-073's
  customer reports (WC-S-0223, WC-S-0244, WC-S-0245) are left for CM-ANL, which batch 2 maps. If batch 2 cites them
  there, WC-C-074 becomes strained and WC-C-073 stays strained; batch 2 should say so in its notes, and the coordinator
  changes the fit.

### Joins on role (readings)

- **WC-C-114, WooAds, in CM-MKT-010, with Shopify's Advertising apps and Salla Ads.** WooAds' only statements say that
  the merchant authorizes access to "the data from your ad platform APIs about your ad campaigns" (WC-S-0947), synced
  by a Jetpack module (WC-S-0949). This is the merchant's advertising on ad platforms. No statement says whether WooAds
  runs campaigns or only reads them (U-055's own doubt), a gap. Its maker isn't named either: "us" names no company. So
  the WooAds statements are `shows`.
- **CM-CUS-009, address autocomplete as location services for addresses.** The cell reads WooCommerce's Address
  Autocomplete (WC-C-047, domain C, also D) in the role of Salla's map and location services: third-party services
  suggest addresses through WC_Address_Provider (WC-S-0919, WC-S-0445). It is a reading. Two other things are not cited:
  WooCommerce's MaxMind geolocation (WC-C-046, domain E), which locates a customer by IP for tax and shipping, not an
  address, and a domain E statement in `core` here.
- **CM-LOY-006, gifting.** WooCommerce's Marketplace category Gifts (WC-S-0733, WC-C-104, domain B, also D) is cited as
  `extension-point`, resting on its name only, the same standard the anchor used for Shopify's Gift wrap and message apps.
  No statement says whether its gifts are bought for someone else or come with a purchase. The reviewer may drop it.
- **CM-B2B-001 against Salla's wholesale market** (U-016): the role is selling to businesses.

### Homonyms and near-homonyms (none of Q1's six bear on this batch)

- **Notifications:** WooCommerce > Notifications (WC-S-0047) is the admin item Stock Notifications, the back-in-stock
  feature (CM-MKT-016). It is not a notification settings page; that is CM-NTF's subject, batch 2's.
- **Customer Accounts:** the Marketplace category Extensions > Customer service > Customer Accounts (WC-S-0723, WC-C-106)
  is cited in CM-CUS-010 as `extension-point`. WC-C-106 is batch 2's to land. If batch 2 lands it in CM-SUP, it is
  strained by this citation.
- **Promotions:** WooCommerce has two categories that use the word, Conversion > Promotions (WC-S-0718, CM-MKT-001) and
  Marketing > Advertising and promotions (WC-S-0755, CM-MKT-010). The second is cited for advertising, its first word.
- **Automation:** Shopify Flow (SH-C-151, domain F) is a workflow tool. WooCommerce's Marketing > Automation and
  MailPoet's automation sit under marketing. U-083 is ruled apart (below).

### Strained fits

- **WC-C-073:** its account statements are in CM-CUS-010 and its batch API in CM-CUS-003 (above).
- **WC-C-105:** see the grains above.
- **WC-C-110:** Advertising and promotions is in CM-MKT-010. Several of its subcategories are uncited (see below).
- **WC-C-113:** MailPoet's settings for WooCommerce customers' subscriber status and its Customers list (WC-S-5500,
  WC-S-5501, WC-S-5502) are cited in CM-CUS-007 (marketing consent), as `shows` only. MailPoet's maker statement is
  cited in CM-MKT-006 and CM-MKT-007, under one parent.

### Statements of the batch's concerns left uncited, and why

- **WC-C-105:** Customer feedback (WC-S-0717) belongs to CM-SUP, batch 2's. Store alerts (WC-S-0721) is undefined, and
  no capability fits it.
- **WC-C-110:** these have no capability in D, or belong to batch 2:
  - CRM (WC-S-0757): undefined;
  - Reporting and analytics (WC-S-0758): CM-ANL, batch 2;
  - Sales channels (WC-S-0759) and SEO and SEM (WC-S-0760): domain E's subjects;
  - Social (WC-S-0762): no capability;
  - Google for WooCommerce's sync to Google Merchant Center (WC-S-5492, WC-S-5494): product feeds. D-anchor left them to
    domain E (its notes: "Product feeds stay out of this model").

  scope.tsv gives WC-C-110 no `also`, so domain E can't cite these without a flag. The coordinator may add E to WC-C-110's
  `also`.
- **WC-C-103:** the B2B payments category is WC-C-005's (WC-S-0710, domain C) and is not cited. The setting Enable B2B
  Transactions, which forces checkout with a VAT number (WC-S-5463), is WC-C-118's (domain C) and is not cited either.
- **WC-C-084:** none.

### Gaps

- **Maker statements.** Three extensions are listed under "Developed by Woo" only in a statement's note, which never
  counts. Their cells place them as `shows`:
  - the Purchase Order Gateway (CM-B2B-001);
  - Back In Stock Notifications (CM-MKT-016);
  - WooCommerce Points and Rewards (CM-LOY-004).

  A statement naming their maker would make them `own-service`.
- **WooAds** has no definition and no maker statement.
- **Experimental features.** Stock notifications, the wishlist and saved-for-later are experimental and off by default
  (WC-S-5403, WC-S-5457, WC-S-5458), cited as `shows` (C6). The cells' `core` rests on code that ships behind those
  features: an admin item and an email for stock notifications, and a controller and Store API routes for shopper lists.
  The cells say so.
- **Q1 gaps.** Every concern of the batch has its `responsible` placement stated only in general terms, and most have no
  `reason` found. No cell claims a placement those gaps would change.

### Rulings

Each candidate holding a concern of this batch is ruled, one row per pair of WooCommerce concern and Shopify or Salla
concern:

| Candidate | Rulings |
|---|---|
| U-001 | joined:CM-MKT-022 (twice) |
| U-015 | nested:CM-B2B-003, apart |
| U-016 | joined:CM-B2B-001 with SA-C-098; three apart by scope |
| U-017 | joined:CM-CUS-010 (twice), nested:CM-CUS-011 |
| U-054 | three apart by scope |
| U-055 | nested:CM-MKT-011, apart with SH-C-133, joined:CM-MKT-010 (twice) |
| U-057 | joined:CM-MKT-001, joined:CM-MKT-021 (twice) |
| U-058 | joined:CM-MKT-002 (twice) |
| U-059 | joined:CM-MKT-021, four apart |
| U-060 | joined:CM-LOY-005 (twice), apart with SH-C-188 |
| U-063 | four apart |
| U-078 | joined:CM-LOY-004 (twice) |
| U-083 | two apart |

- **U-083,** which F-anchor's notes left to domain D, is apart for both WC-C-110 and WC-C-113: scope.tsv gives Shopify
  Flow (SH-C-151) domain F, without D under `also`.
- **U-001's** two joins are on CM-MKT-022, which this batch adds. They hold once the back-fill writes Shopify's and
  Salla's cells from SH-C-050 and SA-C-048 (the checker's two flags).
- **U-015 with SH-C-045:** the ruling is apart, because no capability here cites SH-C-045. Shopify's payment terms
  (SH-S-0589) and WooCommerce's purchase orders (WC-S-5471, CM-B2B-001) are both ways a business buyer pays.
  SH-C-045 names D under `also`, so a back-fill could cite it in CM-B2B-001, and the ruling would then follow the cells.
- **WooCommerce-only pairs are not ruled here,** because the checker rules WooCommerce's concerns against Shopify's and
  Salla's only. These pairs are WC-C-103 with WC-C-061 (U-016), WC-C-105 with WC-C-104 (U-059), and WC-C-110 with
  WC-C-107 (U-063).

### What the checker flagged, answered

- **`own-service` on MailPoet** (WC-S-0944, WC-S-0458, WC-S-0459). WC-S-0458, in the Terms' "Who's Who: Woo Services",
  says "Woo services include WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet". WC-S-0459 names
  WooCommerce, Inc. as the company for Woo services outside the Designated Countries. Together they name the platform's
  company as MailPoet's provider. WC-S-0944, MailPoet's own listing, supports `own-service` only alongside them; the
  reviewer may move it to `shows`.
- **CM-CUS-003, `core` resting only on boundary statements.** The statement is WooCommerce's own customer API acting on
  "a batch, of customers" (WC-S-0665). That is the platform's own API for its own feature, which the dry run's
  convention makes `core`. No admin bulk action is held.
- **M-018 across two trees, and CM-MKT-022 with no landing:** answered above.
- **The two `joined:CM-MKT-022` flags:** answered under Rulings.
- **`none-held` cells with matching statements** (CM-CUS-002, CM-CUS-004 to CM-CUS-006, CM-CUS-011, CM-CUS-012,
  CM-CUS-014, CM-B2B-002, CM-B2B-003, CM-MKT-003, CM-MKT-004, CM-MKT-009, CM-MKT-013 to CM-MKT-015, CM-MKT-017 to
  CM-MKT-020, CM-LOY-001, CM-LOY-003). Each hit was read, and each cell's `reading` names what they are: payment
  providers' tags and wallets (WC-C-004), WooPayments' fraud rules and balances, editor blocks, Automattic's companies
  as data controllers, usage tracking to Automattic, and the Marketplace's payout calendar. Others are cited elsewhere:
  Promotions in CM-MKT-001, shopper lists in CM-LOY-005, and Rewards and loyalty in CM-LOY-004.
  - WC-S-0950, the setting that reviews can be left only by verified owners, has nothing to do with sign-in (CM-CUS-012).
  - The CM-MKT-019 hits are things that are scheduled: deferred emails, subscription renewals and payouts. None is a
    marketing calendar.

### Proposals for the coordinator

- **Rename CM-MKT-016** to add WooCommerce's terms: "(... ; WooCommerce Stock Notifications, Back in stock notification)".
- **Rename CM-LOY-005** to add "(WooCommerce shopper lists: wishlist, saved for later)".
- **Rename CM-MKT-002:** WooCommerce's term is Coupons, the same as Salla's.
- **Add E to WC-C-110's `also`,** for its Sales channels, SEO and SEM categories and Google for WooCommerce (above).

### Problems with the brief or the evidence

- `candidates` found nothing for CM-MKT-021, although WC-S-0722 ("Upsells and cross-sells") is held. The phrase search
  for Shopify's "Upsell and cross-sell apps" misses WooCommerce's plural, and a direct search found it.
- WooCommerce's coupon webhook topics and Store API cart routes are held twice: under WC-C-074 and under WC-C-077 or
  WC-C-079 (domains F and C). This part cites WC-C-074's keys.

## Batch 2: SUP, ANL and NTF

Five concerns: WC-C-065, WC-C-106, WC-C-038, WC-C-039 and WC-C-076. WooCommerce's cell is written for all 18 capabilities
of the three areas. This batch adds no capability. Searches are in English.

### How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| WC-C-065 Product reviews and review requests | CM-SUP-001 | match:M-065 | clean |
| WC-C-106 Customer service extensions | CM-SUP-005 | terms | strained |
| WC-C-038 Store analytics and reports | CM-ANL-001 | match:M-058 | clean |
| WC-C-039 WooCommerce Analytics service | CM-ANL-001 | terms | strained |
| WC-C-076 Transactional emails | CM-NTF-001 | terms | strained |

All five joined existing capabilities, and none made a new one.

- **WC-C-065:** its reviews are in CM-SUP-001. Its review request is in the child CM-SUP-002: the email Review request,
  the feature customer_review_request and its namespace and route. The feature is a beta, off by default, and merchants
  turn it on under Settings > Advanced > Features (WC-S-5390). Because the statement names that setting, the cell reads it
  as `core`, not as an unreleased flag.
- **WC-C-038:** the cut follows the anchor's children:
  - CM-ANL-001: the menu Analytics, its toggle and settings, the capability view_woocommerce_reports, and the wc-analytics
    namespace with its data resources.
  - CM-ANL-002: WooCommerce > Reports, the report pages under Analytics, and their wc-analytics report resources, with
    import and export.
  - CM-ANL-003: Analytics > Overview, with performance-indicators and leaderboards. Placing those two resources here reads
    their names.
  - CM-ANL-006: the REST API's reports (wc/v3 reports-*, WC-S-0679). This is a join on role (below).
- **WC-C-076:** this batch joins it by its own words, "Enable this email notification" (WC-S-5412). Its customer emails
  are cited in CM-NTF-001, and its staff emails in CM-NTF-002 (below).

### Grains I chose

- **WC-C-106 is a Marketplace category group,** cut the way batch 1 cut WC-C-105 and WC-C-110. It lands in CM-SUP-005
  through its subcategory Support. Its other parts are cited where they belong:
  - Live chat: CM-SUP-004.
  - Managing customers: CM-CUS-001, as `extension-point`, added to batch 1's cell (below).
  - Customer Accounts: CM-CUS-010, cited by batch 1.
  - The Advanced Notifications extension: CM-NTF-001, as `shows`. Its maker and its category appear only in its
    statements' notes, a gap.
- **Post-purchase services (WC-S-0726) is left uncited.** No statement defines it, and no capability of D fits it. It is
  a Marketplace category, so it meets the dry run's test for a capability. The coordinator may add one, but on this
  evidence it would rest on a bare name, with no counterpart on Shopify or Salla. This is the same choice batch 1 made
  for Store alerts and CRM.
- **Customer feedback (WC-S-0717, WC-C-105), which batch 1 left to SUP,** is cited in CM-SUP-001 as `extension-point`.
  That is a reading on the term feedback, which Salla uses for its reviews (its API folder Feedbacks). No statement
  defines the category. The reviewer may move it to CM-SUP-007 (surveys).
- **Staff emails in CM-NTF-002:** New order, Cancelled order, Failed order, Payment gateway enabled and Order withdrawal
  request (WC-S-0294, WC-S-0295, WC-S-0297, WC-S-0307, WC-S-0315). This is a reading on the identifiers:
  - their class names lack Customer, or name Admin, while the customer's emails of the same titles are
    WC_Email_Customer_;
  - New order is also the term of Shopify's staff notification.

  In the release, the class files cited set the recipient's default to the site's admin email. That is context only,
  not cited.
- **The email Review request (WC-S-0313)** is held by WC-C-065 and by WC-C-076. It is cited once, under WC-C-065's key,
  in CM-SUP-002, which makes WC-C-076 strained. New account and Reset password (WC-S-0306, WC-S-0305) are cited in
  CM-NTF-001 under WC-C-076's keys, and by batch 1 in CM-CUS-010 under WC-C-073's.
- **Coupon and customer analytics, left by batch 1.** These statements are held under WC-C-038 and also under WC-C-074
  (WC-S-0071, WC-S-0208, WC-S-0238, WC-S-0239) or WC-C-073 (WC-S-0223, WC-S-0244, WC-S-0245). They are cited in
  CM-ANL-002 under WC-C-038's keys.

### Joins on role (readings)

- **CM-ANL-006:** WooCommerce's REST reports API ("allows you to view all types of reports available", WC-S-0679, and
  wc/v3 reports-*) takes the role of Shopify's read_reports and ShopifyQL. It is `core`, the platform's own API for its
  own feature. No statement says apps do the work through it, and no report builder like Salla's is held.
- **U-041 with SA-C-179:** the role is the store's support to its buyers, through extensions on WooCommerce and built in
  on Salla. This follows the anchor's join on role in CM-SUP-005.
- **CM-NTF-002** rests on identifiers (above).

### Homonyms and near-homonyms (none of Q1's six bear on this batch)

- **WooCommerce Analytics** names two things:
  - the analytics kept in the store, whose setting says "All data stays within your store" (WC-S-0622, WC-C-038);
  - a service the store connects to, which syncs its data through Jetpack Sync (WC-S-0573, WC-S-0574, WC-C-039).

  Q1 split them and matched only the first (M-058). WC-C-039 lands in CM-ANL-001, strained, cited as `shows`: its
  statements name no company ("our service") and don't say what the service shows.
- **Support:**
  - Extensions > Customer service > Support (WC-S-0727) is the merchant's support to buyers, cited in CM-SUP-005.
  - The WooCommerce Support Policy, the support forums (WC-C-062) and Business services > Support (WC-S-0772) are Woo's
    support to merchants. They are not cited.
- **Notifications:** batch 1's Stock Notifications (CM-MKT-016) is the back-in-stock feature. WooCommerce's email
  notifications are CM-NTF-001's.
- **Logs:** Status > Logs (WC-C-037) is the system log, not a log of sent messages (CM-NTF-003 is `none-held`).

### Strained fits

- **WC-C-106:** see the grains above.
- **WC-C-039:** see the homonyms above.
- **WC-C-076:** the email Review request is cited in CM-SUP-002, and New account and Reset password are cited by batch 1
  in CM-CUS-010.

### Statements of the batch's concerns left uncited, and why

- **WC-C-106/where/WC-S-0726,** Post-purchase services: see above.
- **WC-C-038/decides/WC-S-0043, WC-C-039/decides/WC-S-0573 and WC-C-076/where/WC-S-0313:** each is the same statement as
  a key already cited (its `where` key, or WC-C-065's key).

### Cited across domains

- **WC-S-0939, push notifications for the WooCommerce mobile apps "to receive order notifications"** (WC-C-090, domain G,
  also D). It is cited as `core` in CM-NTF-002. G-woocommerce cites it as `core` in CM-SRF-001, so the merge will flag a
  statement in `core` in two domains. Notifying staff of orders is NTF-002's subject. The coordinator may keep one.
- **WC-C-109 (domain G, also D):** Business insights (WC-S-0746, CM-ANL-001) and Admin and notifications (WC-S-0752,
  CM-NTF-001) are cited as `extension-point`, on their names. No G part cites them.
- **WC-C-110:** Reporting and analytics (WC-S-0758), left to ANL by batch 1, is cited in CM-ANL-001 as `extension-point`.

### Rulings

| Candidate | Rulings |
|---|---|
| U-041 | joined:CM-SUP-005 (twice) |
| U-067 | joined:CM-NTF-001 (twice), nested:CM-NTF-004, apart with SH-C-130 |

- **U-067 against SA-C-200:** nested. Salla's Communication Apps are in CM-NTF-004, a child of CM-NTF-001, and no
  WooCommerce statement names a delivery provider of the store's emails.
- **U-067 against SH-C-130:** apart. Shopify Messaging is in CM-MKT-007, as the anchor ruled it against Salla's
  Notifications.
- **U-070** (WC-C-093, cost of goods, domain B also D, with SA-C-220) isn't ruled here. This part doesn't land WC-C-093.

### What the checker flagged, answered

The whole part's final check: `0 problems, 40 flags for the reviewer`.

- **cells.tsv line 61, CM-ANL-006, `core` resting only on boundary statements.** These are WooCommerce's own REST
  resources for its own reports. WC-S-0679 says the API allows you to view all types of reports. That is the dry run's
  convention for `core`.
- **`none-held` with matching statements:** each hit was read, and each cell's `reading` names what it is.
  - CM-SUP-003: Marketing > Social and statements on trusting Marketplace developers.
  - CM-SUP-006 and CM-SUP-008: WooPayments' terms on the merchant's questions, complaints and disputes, and Woo's
    forums.
  - CM-SUP-007: PCI's questionnaire.
  - CM-ANL-004: Live chat, live rates and a live site.
  - CM-ANL-005: Business insights, cited at the parent, because no statement defines it or Salla's Smart analytics.
  - CM-NTF-003: system logs.
  - CM-NTF-004: MailPoet's sending advice (cited by batch 1 in CM-MKT-007), a staff email, and payment gateways.
- **The other flags** are on batch 1's rows, and batch 1's notes answer them.

### For the coordinator: batch 1's rows

- **WC-C-074 (clean in CM-MKT-002):** its Analytics > Coupons statements are now cited in CM-ANL-002, under WC-C-038's
  keys. The checker doesn't flag it, because the keys are WC-C-038's. But batch 1's notes say the fit becomes strained
  if batch 2 cites them in ANL. The coordinator may change it to strained.
- **WC-C-073's landing and CM-CUS-001's reading** say its customer reports are "left to CM-ANL". They are now cited in
  CM-ANL-002, under WC-C-038's keys.
- **CM-CUS-001, WooCommerce's cell:** this batch appended one evidence row, Managing customers (WC-S-0725,
  `extension-point`, WC-C-106). The cell's reading, batch 1's, doesn't name it. The coordinator may add it.
- **No problems** on batch 1's rows.

### Proposals for the coordinator

- **Rename CM-NTF-001** to add WooCommerce's terms: "(... ; WooCommerce Emails, email notifications)".
- **Rename CM-SUP-005** to add "(WooCommerce Customer service > Support extensions)".
- **Rename CM-ANL-001** to add "(WooCommerce Analytics, Reports)".
- **Post-purchase services:** decide whether it becomes a capability (above).

### Gaps

- **WC-C-039:** no statement says what the WooCommerce Analytics service shows, or names its maker.
- **Advanced Notifications:** its maker (Developed by Woo) and its category Customer service are only in its notes.
- **Reports permissions:** the only staff gate held for analytics and reports is view_woocommerce_reports. No
  per-report permission is held.
- **Q1 gaps:** every concern of the batch has `responsible` stated only in general terms, or `reason` not found. No cell
  claims a placement those gaps would change.

## The coordinator's corrections after batch 2 (30 October)

- **WC-C-074 is `strained`.** Its Analytics > Coupons statements (WC-S-0071, WC-S-0208, WC-S-0238, WC-S-0239) are held by WC-C-038 too, and batch 2 cites them in CM-ANL-002 under WC-C-038's keys: another tree, as batch 1 foresaw. The checker tests a citation by its key, so it couldn't see this. The merge now tests by statement id and flags such landings for the final review.
- **WC-C-073's landing and CM-CUS-001's cell** now say that the customer reports are cited in CM-ANL-002, and the cell names the row batch 2 added (Managing customers, WC-S-0725).
- **WC-S-0939 counts once.** It supported `core` here, in CM-NTF-002, and in G's CM-SRF-001, the mobile app for managing the store with push notifications. It stays `core` in G, whose capability names it, and is `shows` here. CM-NTF-002's cell stays `core` on the staff emails.
- **Post-purchase services (WC-S-0726) stays uncited.** It is a Marketplace category, the kind of place the convention admits, but its name doesn't say what it holds (warranties, returns, surveys, tracking), and no statement does. A capability named from it would be a guess. It is listed as a gap: what WooCommerce's category holds.
- **The renames** batch 1 and batch 2 propose (CM-MKT-016, CM-LOY-005, CM-MKT-002, CM-NTF-001, CM-SUP-005, CM-ANL-001) are made at the merge.
- **WC-S-0219,** wc-analytics ProductsLowInStock, is `shows` in CM-ANL-001. It is `core` in B's CM-INV-004, low stock, whose WooCommerce cell rests on it alone, so it counts once. The merge now finds a statement counted twice by its statement id, under whichever concern's key a part cites it.
- **Counted once (the coordinator, at A's merge):** WC-C-073/decides/WC-S-0881 is `shows` in CM-CUS-010: core in A's CM-TRU-006, privacy settings, whose WooCommerce cell rests on it, so it counts once (the coordinator, convention 8).
