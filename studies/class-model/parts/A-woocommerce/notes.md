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
