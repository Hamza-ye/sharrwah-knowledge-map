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
