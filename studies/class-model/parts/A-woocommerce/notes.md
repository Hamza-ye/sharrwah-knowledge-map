# A-woocommerce: notes

WooCommerce's concerns of domain A, Merchant and platform, mapped onto the model A-anchor built. The part runs in two
batches: batch 1 takes the areas ACC, STF, PLN and ONB, batch 2 the area TRU. Read through `class_slice.py` only: `seed`,
`model --areas`, `concerns --where`, `statements`, `gaps`, `matches`, `key`, `search`, `caps`, `candidates` and
`homonyms`. Searches are in English, WooCommerce's only language in the concern map. Every placement below is a reading of
the statements cited.

## Batch 1: ACC, STF, PLN and ONB

Nine concerns: WC-C-023, WC-C-025, WC-C-026, WC-C-049, WC-C-080, WC-C-057, WC-C-062, WC-C-081 and WC-C-082. WooCommerce's
cell is written for all 23 capabilities of the four areas and for the four this batch adds: 27 cells, 17 with statements
and 10 none-held. 79 evidence rows, 2 qualities, 6 slot fillers, 3 rulings.

### Landings

Five concerns joined existing capabilities, all by a Q1 match:
- **WC-C-023 and WC-C-026** in **CM-ACC-002** by M-001. WooCommerce splits the contracting entity from governing law and
  courts (M-001's granularity note); CM-ACC-002 holds both, as Shopify's SH-C-002 does, so both land in it rather than in
  two children. The terms are Automattic's Terms of Service, covering WordPress.com, WooCommerce.com, WooPay and the Woo
  services (WC-S-0643, WC-S-0458), not the WooCommerce software, which is under GPLv3 (CM-ACC-011).
- **WC-C-080** in **CM-STF-002** by M-004 (strained, below).
- **WC-C-057** in **CM-PLN-007** by M-009, as A-anchor's notes said it could.
- **WC-C-062** in **CM-ONB-003** by M-066.

Four made new capabilities, numbered past the model's highest in their areas:
- **CM-ACC-009, site visibility before launch** (WC-C-082), under CM-ACC-006: WooCommerce's Site visibility is a section of
  its settings (WC-S-0009; the inventory lists it under settings, WC-I-0009), as Salla's maintenance mode is a route under
  General. Not landed in CM-ACC-007 (Salla Maintenance mode): see "Joins not made".
- **CM-ACC-010, connecting the store to the platform company's account for its services** (WC-C-049): the WordPress.com
  account and Jetpack connection that WooPayments, WooCommerce Tax and WooCommerce Shipping need. Searched every domain
  (`caps`: Jetpack, WordPress.com, connection, connect, ربط, اتصال). Domain F's CM-APP-012 is the connection to
  WooCommerce.com for marketplace extensions, another account for another purpose (WC-S-0899 against WC-S-5335), so it is
  not the same thing. Not CM-ACC-001 either: the statements show a connection of the site to services, not the account the
  store is owned and signed into (reading).
- **CM-ACC-011, licence of the platform's software** (WC-C-025): GPLv3 and its disclaimer of warranty. `caps` on licence,
  license, GPL, open source found only CM-TRU-010 and CM-TRU-011, the merchant's own licences and IP infringement, other
  things. ACC because it is the terms the merchant runs the platform under, beside the merchant agreement (CM-ACC-002), a
  reading; the reviewer may prefer another area.
- **CM-ONB-004, store setup in the admin** (WC-C-081): the setup wizard, the onboarding profile and the setup tasks. No
  capability of any domain held it (`caps`: setup, wizard, profiler, task list, onboarding).

### WordPress, and Automattic's services, not WooCommerce

The task asks to say where WordPress or a service of Automattic's does a thing. Placed by what the statements show:
- **WordPress:** the users and the Administrator role (CM-ACC-001, CM-STF-001: WC-S-0883 "extends the existing
  Administrator role", WC-S-0884 "Users > All Users in the WordPress admin"), cited as `shows`, since the statement shows
  WordPress, not WooCommerce, doing it. WooCommerce's own roles and capabilities are `core` in CM-STF-002. WordPress
  multisite in CM-ACC-003 (WC-S-5450), `shows`. The forum on WordPress.org for the free core plugin (WC-S-5344), `shows`
  in CM-ONB-003.
- **Automattic's services:** the WordPress.com account and Jetpack connection (CM-ACC-010), WooPayments' fees, invoices and
  their taxes (CM-PLN-004, CM-PLN-007), and support for WooCommerce and products sold on WooCommerce.com (CM-ONB-003) are
  `own-service`. The maker statements, cited in the same cells: WC-S-0594 "WooCommerce is developed and supported by
  Automattic, the creators of WordPress.com and Jetpack", and WC-S-0458 "Woo services include WooCommerce, WooPayments,
  WooCommerce Shipping, WooCommerce Tax", whose entities are WooCommerce, Inc. and WooCommerce Ireland Ltd., collectively
  Automattic (WC-S-0459 to WC-S-0461, cited in CM-ACC-002). The terms governing WordPress.com and Woo (CM-ACC-002), the
  sanctions on Automattic's Services (CM-ACC-008) and WordPress.com plans (CM-PLN-001) are Automattic's, cited as `shows`.
- No plan, bill, platform fee, prepaid balance or store lifecycle of the WooCommerce software itself is held
  (CM-PLN-001 to CM-PLN-003, CM-PLN-006, CM-ONB-002): the cells are none-held or `shows`, with the hits named.

### Grains

- **WC-C-081** is coarser than CM-ONB-004: store administration as a whole. Only its setup statements are cited there; its
  WooCommerce > Settings (WC-S-0044) is CM-ACC-006's `core`. Its top menu (WC-S-0039), Home (WC-S-0040, WC-S-5420), inbox
  notes (WC-S-0206, WC-S-0207) and the wc-admin options, plugins, features, experiments and notice resources (WC-S-0192,
  WC-S-0195, WC-S-0184, WC-S-0185, WC-S-0183) are cited nowhere in domain A: they aren't setup, and no capability of A is
  the admin as such. Features are domain G's CM-EVO-001 by its terms. A capability for the admin's home or its inbox would
  need a split; the reviewer may make it.
- **Launch your store** (WC-S-0423, WC-S-0248) is cited in CM-ACC-009, not CM-ONB-004: it ends coming-soon mode, the
  capability's subject, though it is also an onboarding task (reading).

### Joins not made, and why

- **WC-C-082 against Salla's Maintenance mode (CM-ACC-007, U-069): apart.** WooCommerce defines Coming soon mode: it
  "controls who can visit your site while you prepare it for launch" (WC-S-0891). Salla's maintenance mode is held only as
  a route and a plan line (SA-S-1726, SA-S-2084), with nothing on what it does to the storefront (the anchor's cell says so).
  A join on role needs both platforms' definitions, so none is made. If a definition of Salla's mode is held, the two may be
  joined on role (a storefront closed to visitors), and the ruling would become joined; a back-fill citing SA-S-1726 in
  CM-ACC-009 would make it so.

### Strained fits

- **WC-C-023** (CM-ACC-002): its WC-S-0458 is also cited in CM-PLN-004 and CM-PLN-007, as the maker statement for
  WooPayments' fees. Strained by citation only; the concern itself fits.
- **WC-C-025** (CM-ACC-011): its WC-S-0594 is also cited in CM-ACC-010 and CM-ONB-003, as the maker statement for
  WordPress.com and Jetpack and for support.
- **WC-C-080** (CM-STF-002): the Customer role is a buyer's (domain D's CM-CUS-001, cited there under WC-C-073's key of
  WC-S-0883); WC-S-0883 is also cited in CM-ACC-001 for WordPress's Administrator role, and WC-S-0884 in CM-STF-001.
- **WC-C-081** (CM-ONB-004): coarser, above.

### Statements cited from concerns of other domains without A under also

Each `shows` only, so that it supports no placement in two domains, and each answers a flag:
- WC-S-0880 (WC-C-030, E) in CM-ACC-006: the general settings page with the business address; domain E's CM-MKS-001 cites it
  as `core`.
- WC-S-5450 (WC-C-094, G) and WC-S-0089 (WC-C-070, C) in CM-ACC-003: WordPress multisite and the network-orders resource,
  the only held statements on several sites in one network.
- WC-S-0644 (WC-C-050, F) in CM-PLN-001: Automattic's Paid Services, among them certain WordPress.com plans.
- WC-S-0538 (WC-C-012, C) in CM-PLN-005: WooPayments' fees deducted from each payment, the means its fees are paid.

No concern under `also` was cited in batch 1.

### Homonyms

- **Inbox:** WooCommerce's inbox is the admin's notes to the merchant (wc-analytics > admin/notes, WC-S-0206); Shopify Inbox
  is chat with customers (CM-SUP-004). In CM-ONB-004's note.
- **Account:** WooCommerce's statements use account for the WooPayments account (WC-C-009, domain C), the WordPress.com
  account (CM-ACC-010) and the WooCommerce.com account (CM-APP-012); none is the merchant account of CM-ACC-001.
- **Supported countries** (Q1's U-034, the anchor's note): CM-ACC-008 cites Automattic's sanctions on its Services, not
  WooPayments' supported countries (WC-C-010, domain C).

### Rulings

- **U-029:** WC-C-057 against SH-C-017 and against SA-C-113, both `joined:CM-PLN-007` by the cells; the second as the
  anchor ruled SH-C-017 against SA-C-113, SA-C-113 being domain C's and cited in CM-PLN-007 as `shows` only.
- **U-069:** WC-C-082 against SA-C-002, `apart` (above).

### Gaps

- WooCommerce's onboarding profile (WC-S-0198) is held as a resource only: what it asks, the store's country among others,
  isn't stated, so CM-ONB-001 is none-held.
- WC-C-080/responsible, WC-C-081/responsible and WC-C-082/responsible are "stated only in general terms"; the reason
  placements of WC-C-023, WC-C-026, WC-C-057, WC-C-062, WC-C-080 and WC-C-081 are "searched, not found". The cells say so
  where it bears.
- No statement names the maker of WooPayments' Payments > Documents menu in the dashboard (WC-S-5309) beyond WC-S-0458's list
  of Woo services; the cells rest on that list.

### What the checker flagged (0 problems, 35 flags), answered

- **Statements of other domains' concerns** (5 rows): above.
- **own-service without a company's name in the statement** (WC-S-0594, WC-S-5335, WC-S-0464, WC-S-0555, WC-S-5334,
  WC-S-5332, WC-S-0634, WC-S-0549, WC-S-5309, WC-S-0458, WC-S-0548, WC-S-0833, WC-S-0646): WC-S-0594 names Automattic as the
  developer and supporter of WooCommerce and the creator of WordPress.com and Jetpack; WC-S-0458 lists WooPayments,
  WooCommerce Shipping and WooCommerce Tax among the Woo services whose entities WC-S-0459 to WC-S-0461 name as WooCommerce,
  Inc. and WooCommerce Ireland Ltd., collectively Automattic. Each own-service cell cites one of them. The others are
  Automattic's documents and terms speaking as we or our (reading).
- **none-held with matching statements** (CM-ACC-004, CM-ACC-005, CM-STF-003, CM-STF-004, CM-STF-005, CM-PLN-002,
  CM-PLN-003, CM-PLN-006, CM-ONB-001, CM-ONB-002): each cell's reading names the hits and why none is the capability:
  WooPayments' eligibility and Automattic's controllers (CM-ACC-004), the merchant's duties to its customers and the
  European Commission's contractual clauses (CM-ACC-005: WC-S-0468, WC-S-0499), settings groups (CM-STF-003), an HTML
  target attribute (CM-STF-004), the agency partner directory (CM-STF-005), the support year and GPL term (CM-PLN-002),
  WooPayments' processing fees (CM-PLN-003), WooPayments' account balance and wallet payment methods (CM-PLN-006),
  WooPayments' sign-up countries and the Designated Countries (CM-ONB-001), suspension of WooPayments accounts or of
  access to Automattic's Services (CM-ONB-002).
- **A statement in more than one tree** (WC-S-0458, WC-S-0594, WC-S-0883): the maker statements and WordPress's
  Administrator role, above under strained fits. WC-S-0644 is cited in CM-PLN-001 only.

### For batch 2 (TRU)

- Every capability of ACC, STF, PLN and ONB has a WooCommerce cell; batch 2 writes cells for TRU and adds evidence here
  only where its concerns' statements bear on these.
- **WC-C-028** (US sanctions on Automattic's Services): CM-ACC-008's WooCommerce cell already cites WC-S-0490, WC-S-0491,
  WC-S-0648 and WC-S-0493 as `shows`. M-084 holds WC-C-028 with SH-C-174, which the anchor landed in CM-ACC-008, so batch
  2 can land WC-C-028 there by `match:M-084`; if it lands it in a TRU capability instead, it is strained by these
  citations. WC-C-029 (the merchant's own sanctions compliance) is M-084's too; its WC-S-0648 is the same sentence.
- **WC-C-019** (the merchant's PCI scope) uses "store owner" (WC-S-5303); batch 1 didn't cite it in CM-ACC-001.
- **WC-C-022** (Store guidelines on WordPress.com) and **WC-C-027** (merchant responsibility): U-036, U-037, U-038 and U-039
  are batch 2's. U-037 holds SH-C-001 and SA-C-170, both cited in CM-ACC-001; CM-ACC-001's WooCommerce cell cites only
  WC-S-0883, so U-037's pair with WC-C-027 follows wherever batch 2 cites WC-C-027. U-036 holds SH-C-014 (CM-ONB-002),
  whose WooCommerce cell is none-held.
- **WC-C-011's WC-S-0478** (Automattic may suspend an account or the use of WooPayments) is named, not cited, in
  CM-ONB-002's reading; if TRU cites it as enforcement, the reading stands.
- WC-C-024, WC-C-043, WC-C-044, WC-C-045, WC-C-117 and the data concerns are TRU's; batch 1 cited none of them.

## Batch 2: TRU

Sixteen concerns: WC-C-018, WC-C-019, WC-C-022, WC-C-024, WC-C-027, WC-C-028, WC-C-029, WC-C-031, WC-C-032, WC-C-035,
WC-C-040, WC-C-041, WC-C-043, WC-C-044, WC-C-045 and WC-C-117. WooCommerce's cell is written for all 20 capabilities of
TRU and for the one this batch adds: 21 cells, 14 with statements and 7 none-held (CM-TRU-001, 003, 008, 011, 012, 017,
020). 89 evidence rows (three of them added to batch 1's CM-ACC-008 cell), 2 qualities, 5 slot fillers, 24 rulings.

### Landings

Fourteen concerns joined existing capabilities:
- **By a Q1 match (9):** WC-C-018 and WC-C-019 in **CM-TRU-018** by M-062 (WooCommerce splits WooPayments' card data
  security from the merchant's own PCI scope; Shopify's SH-C-184 holds both, so both land in it); WC-C-024 and WC-C-044 in
  **CM-TRU-013** by M-060 (Automattic as controller, and as processor under the DPA; Shopify's SH-C-180 holds both roles);
  WC-C-027 in **CM-TRU-010** by M-086; WC-C-028 and WC-C-029 in **CM-ACC-008** by M-084, as batch 1 proposed; WC-C-043 in
  **CM-TRU-014** by M-061; WC-C-045 in **CM-TRU-005** by M-059, at the match's coarser grain (export, erasure and
  retention), as Salla's SA-C-066, its parts cited in the children CM-TRU-006 and CM-TRU-007.
- **On role (5), each a reading citing both sides:** WC-C-022 in **CM-TRU-009** (Store guidelines against Shopify's AUP
  and Salla's violations); WC-C-031 in **CM-TRU-004** (Rate limit Checkout against Bot protection); WC-C-032 in
  **CM-TRU-014** (the site's own WordPress database against Shopify's data hosting locations); WC-C-040 and WC-C-041 in
  **CM-TRU-013**, the parent (data passed to the payment and shipping providers the merchant uses, under Automattic's terms,
  against Shopify's Terms on processing customers' personal data).

Two made one new capability: **CM-TRU-021, store data sent from the merchant's own site to the platform company**
(WC-C-035, usage tracking; WC-C-117, Jetpack Sync). A grain chosen: usage tracking has a place of its own (the settings
section Advanced > WooCommerce.com, the opt-in woocommerce_allow_tracking, the REST namespace wc-telemetry); Jetpack Sync
has none held, so it isn't a capability by itself (C1), and the two are the same kind of thing, the store's data leaving
the merchant's own installation for Automattic. Searched every domain first (`caps`: telemetry, usage tracking, sync,
tracker, data store, database, hosting): none holds it. Not CM-TRU-008, whose subject is the platform's use of customer
data across merchants (a reading); not CM-ACC-010, the connection itself, which Jetpack Sync presupposes (WC-S-0953 says
the sync is "part of the required connection to WordPress.com"; not cited there, to keep the flow in one place). Domain
G's Remote Logging (WC-C-036, CM-OPS-005) and domain D's WooCommerce Analytics syncing (WC-C-039, CM-ANL-001) are related
flows already placed; the reviewer may gather them.

### WordPress, and Automattic's services, not WooCommerce

Placed by what the statements show:
- **WordPress:** the export and erasure requests are WordPress's personal data tools; WooCommerce registers its own
  exporters and erasers with them (CM-TRU-007, core for WooCommerce's registrations; the hook is read in the release's
  abstract-wc-privacy.php, context only, not cited). WordPress's Options API and wp_options table (WC-S-0632, CM-TRU-014)
  is `shows`. Sign-in to the admin is WordPress's users', and nothing of WordPress's sign-in security is held
  (CM-TRU-001).
- **Automattic's services, `own-service`:** WooPayments' PCI DSS Level 1 compliance and Automattic's responsibility for
  the cardholder data it handles (CM-TRU-018); WordPress.com's Store guidelines (CM-TRU-009, scoped to WordPress.com
  sites); Automattic's controllers for Woo services and its DPA for WordPress.com site owners (CM-TRU-013); its transfers
  outside the EEA and UK (CM-TRU-014); Jetpack Sync (CM-TRU-021). Automattic's Terms that make the merchant responsible
  (CM-TRU-010, CM-ACC-008's WC-S-0470 and WC-S-0492) are `shows`.
- **WooCommerce itself, `core`:** Rate limit Checkout (CM-TRU-004), the Accounts & Privacy settings with Personal data
  retention and privacy policy notices (CM-TRU-005, CM-TRU-006), the exporters, erasers and the erasure setting
  (CM-TRU-007), storage in the site's own database (CM-TRU-014), usage tracking (CM-TRU-021). The plugin itself handles
  no card data (WC-S-5304, WC-S-5307), so CM-TRU-018 holds no `core` for it.
- **A difference from batch 1, a reading:** batch 1 cited Automattic's Terms as `shows` in CM-ACC-002 (the agreement's
  parties and law). Here Automattic's privacy statements show its services processing data, as controller for Woo services
  and processor for WordPress.com sites (WC-S-0497, WC-S-0498, WC-S-0658), so CM-TRU-013 and CM-TRU-014 are `own-service`,
  each with a statement naming Automattic in the same cell. The coordinator may want one rule for both.

### Strained fits

- **WC-C-029** (CM-ACC-008): by M-084, but WC-S-0470 makes the merchant responsible for its own sales' export, import and
  sanctions compliance, nearer CM-TRU-010 (where Shopify's SH-S-0667, import and export laws, is cited). The reviewer may
  move it; CM-ACC-008's reading (batch 1) doesn't yet name WC-S-0470.
- **WC-C-031** (CM-TRU-004): it limits requests rather than detecting bots; the Store API's rate limiting in general
  (WC-S-5358, WC-S-5361 to WC-S-5363) is domain F's CM-API-005, which cites WC-S-5358 and WC-S-5363. Only the checkout
  setting (WC-S-0932, WC-S-5359, WC-S-5360) is cited here. The anchor's note on CM-TRU-004 keeps API rate limits out; this
  is the checkout's own limit (Q1's U-045: "an anti-abuse checkout limit in WooCommerce").
- **WC-C-032** (CM-TRU-014): the place is the merchant's own database on its own hosting (domain G's CM-OPS-003); WC-S-0586
  and WC-S-0588 are cited in CM-ACC-011 and domain G's CM-MIG-001.
- **WC-C-035** (CM-TRU-021): its WC-S-0027 (Advanced > WooCommerce.com) is cited, under WC-C-063, in domain F's CM-APP-012.
- **WC-C-040, WC-C-041** (CM-TRU-013): the recipients are providers the merchant chooses (Stripe or PayPal, a shipping
  provider), not the platform's processors, consistent with the anchor's reading of Salla's consent text (U-043). No
  capability of any domain is data passed to the merchant's own providers, and WooCommerce gives it no place of its own
  (a section of its documentation only), so none is added (C1); the reviewer may split one.
- **WC-C-045** (CM-TRU-005): WC-S-5467 (the site owner as Data Controller) is cited in CM-TRU-013, as the anchor cites
  Salla's SA-C-066 there; WC-S-0006 and WC-S-0881 are cited, under WC-C-073, in domain D's CM-CUS-010 as `core`, and
  WC-S-0359 and WC-S-0363, under WC-C-066, in CM-SEL-002.
- **WC-C-117** (CM-TRU-021): WC-S-0502, shared with WC-C-044, is cited in CM-TRU-013.

### Statements cited from concerns of other domains

- **Under `also` (A named):** WC-C-009 (C) in CM-TRU-002 (WC-S-0504, WC-S-0522: WooPayments' KYC with Stripe) and CM-TRU-016
  (WC-S-0558: a deleted WooPayments account's information retained), `shows` only, since KYC and WooPayments accounts are
  domain C's; WC-C-109 (G) in CM-TRU-019 (WC-S-0750, the Marketplace category Policy and security, `extension-point`).
- **Without A under `also`** (flagged): WC-S-0503 (WC-C-034, G) in CM-TRU-015, `shows`: Automattic's privacy policy's
  third-party vendors, the only held list of those Automattic shares data with; G cites it in CM-OPS-003 for the hosting
  provider.
- Left to their domains: Business services > Law and Compliance (WC-S-0769, WC-S-0766), cited in F's CM-PTN-005; WooPayments'
  prohibited businesses (WC-C-011, C, M-085 with SH-C-173); the Store API's rate limiting (F's CM-API-005).

### Homonyms

- **Rate limit:** API request limits on Shopify and Salla (domain F's CM-API-005), and WooCommerce's anti-abuse limit on
  checkout requests (CM-TRU-004). Q1's U-045 names it.
- **Log:** WooCommerce's Logs are the logger's entries (G's CM-OPS-005), not an audit log of admin activity (CM-TRU-003,
  none-held for WooCommerce), as batch 1's G counterpart ruled on U-044.
- **Retention:** WooCommerce's Personal data retention is the store's own retention of its customers' data (CM-TRU-005);
  Shopify's retention after a store closes is the platform's (CM-TRU-016).

### Rulings

24 rows, one per pair: U-035 (WC-C-028: joined CM-ACC-008 with SH-C-174, apart from SA-C-232); U-036 (WC-C-022: joined
CM-TRU-009 with SH-C-172 and SA-C-232, apart from SH-C-014 and SA-C-170); U-037 (WC-C-027: apart from SH-C-001 and
SA-C-170, which are CM-ACC-001's); U-038 (WC-C-022: apart from SH-C-173 and SA-C-172, both domain C's; the pair with
WC-C-011 is two WooCommerce concerns and isn't ruled); U-039 (WC-C-027: joined CM-TRU-010 with SH-C-175 and SA-C-231);
U-042 (WC-C-032: joined CM-TRU-014 with SH-C-181, apart from SA-C-233, which has no statements); U-043 (WC-C-040 and
WC-C-041: nested CM-TRU-015 against SH-C-182, the cells citing them in the parent CM-TRU-013 and SH-C-182 in the child;
apart from SA-C-118 and SA-C-119, domain C's); U-045 (WC-C-031: joined CM-TRU-004 with SH-C-051, apart from SH-C-171 and
SA-C-201, domain F's).

### Proposed renames (for the coordinator)

- CM-TRU-004: "Checkout protection against bots and abusive requests (Shopify Bot protection, CommerceProtection;
  WooCommerce Rate limit Checkout)".
- CM-TRU-009: add "WooCommerce: WordPress.com Store guidelines". CM-TRU-010: add "WooCommerce: Your responsibilities".
- CM-TRU-013: add "WooCommerce: Automattic's Controllers and Responsible Companies, Data Processing Agreement".
- CM-TRU-018: add "WooCommerce: WooPayments, Level 1 service provider".
- CM-ACC-008: add "WooCommerce: US Economic Sanctions" (the countries are those Automattic's Services may not be reached
  from).

### Gaps

- WC-C-018/decides, WC-C-024/where, boundary and reason, WC-C-027/where and boundary, WC-C-043/decides and boundary,
  WC-C-045/reason and WC-C-117/reason are searched, not found; WC-C-031/responsible is stated only in general terms. The
  cells say so where it bears.
- No subprocessor list of Automattic's, no data hosting location of its own, no legal-request policy and no
  intellectual-property policy are held (CM-TRU-014, CM-TRU-015, CM-TRU-017, CM-TRU-011).
- No statement names the maker of WooPayments beyond WC-S-0458's list of Woo services (cited in CM-TRU-018, as batch 1
  did in CM-PLN-004 and CM-PLN-007), or of WordPress.com beyond WC-S-0594 (cited in CM-TRU-009).
- The mobile app's QR login (WC-S-0204, domain G) is held as a resource name only; what it does isn't stated.

### What the checker flagged on batch 2's rows, answered

The whole part's check: **0 problems, 62 flags.**
- **own-service without the company's name** (evidence lines 101 to 103, 112 to 118, 132 to 134, 138 to 140, 164 to
  167): each own-service cell cites a statement naming Automattic: CM-TRU-009 WC-S-0594 ("developed and supported by
  Automattic, the creators of WordPress.com"); CM-TRU-013 WC-S-0497 and WC-S-0498 (Automattic Inc., WooCommerce, Inc.)
  and WC-S-5331 (privacypolicyupdates@automattic.com); CM-TRU-014 WC-S-0942 ("Automattic's Services"); CM-TRU-018
  WC-S-0458 (Woo services, whose entities WC-S-0459 to WC-S-0461 name, cited in CM-ACC-002); CM-TRU-021 WC-S-0954
  ("Automattic's servers") and WC-S-0962 ("we, at Automattic ... the services we provide through ... Jetpack"). The rest are
  Automattic's documents speaking as we or our (reading).
- **none-held with matching statements** (CM-TRU-001, 003, 008, 011, 012, 020): each cell's reading names the hits and why
  none is the capability.
- **WC-S-0503 of a domain G concern without A under also** (line 136): above.
- **A statement in more than one tree:** WC-S-0458 (now also CM-TRU-018) and WC-S-0594 (now also CM-TRU-009), the maker
  statements; WC-S-0883 is batch 1's.

### For the coordinator: batch 1's rows

No checker problem is on batch 1's rows. Readings that no longer say all, after batch 2's citations:
- landings.tsv, **WC-C-023** (CM-ACC-002, strained): its reading names CM-PLN-004 and CM-PLN-007 as the other places
  WC-S-0458 is cited; it is now also cited in CM-TRU-018.
- landings.tsv, **WC-C-025** (CM-ACC-011, strained): WC-S-0594 is now also cited in CM-TRU-009 (batch 1's strained-fits
  note names CM-ACC-010 and CM-ONB-003).
- cells.tsv, **CM-ACC-008** WooCommerce: its reading and terms are batch 1's and don't name WC-C-029's WC-S-0470 or
  WC-C-028's WC-S-0657 and WC-S-0492, which batch 2 added as `shows` (and a slot filler, the export, import and sanctions
  laws).
- **WC-C-019's WC-S-5303** ("store owner") was left uncited in CM-ACC-001, as batch 1 did: it speaks of PCI
  responsibility, not the account.

## The coordinator's corrections after batch 2 (30 October)

- **Batch 1's readings** name batch 2's rows: CM-ACC-008's WooCommerce cell, and the landings of WC-C-023 and WC-C-025, whose maker statements are cited in CM-TRU-018 and CM-TRU-009 too.
- **Automattic's Terms, `shows` in CM-ACC-002 and `own-service` in CM-TRU-013 and -014:** both stand for now. A maker statement supports `own-service` for each feature of the company's service that a cell's own statements show (the ruling of 30 October on WC-S-0476); whether the merchant's agreement with Automattic is the platform's merchant agreement, for software the merchant runs itself, is the final review's.
- **The part is complete,** with five capabilities added (CM-ACC-009 to -011, CM-ONB-004, CM-TRU-021): `A-backfill-woocommerce` writes their Shopify and Salla cells.

