# A-anchor: notes

The anchor part of domain A, Merchant and platform (areas ACC, STF, PLN, ONB, TRU), from Shopify's and Salla's concerns
that `scope.tsv` gives the domain. It runs in 7 batches. Every row is a reading of the statements its keys cite; a fact
is only what a cited statement says. Where the brief left a choice to me, this file says so ("my judgment").

## Batch 1: ACC, Accounts, organizations and stores

Concerns: SH-C-001, SH-C-002, SH-C-003, SH-C-004, SH-C-005, SH-C-013; SA-C-001, SA-C-002, SA-C-003, SA-C-167.
Result: 9 capabilities (CM-ACC-001 to CM-ACC-009), 10 landings, 18 cells, 137 evidence rows, 2 qualities, 1 slot
filler, 3 rulings. Every capability has a Shopify and a Salla cell, so batch 2 writes no cell for them; it adds evidence
where SA-C-170 and SA-C-230 bear on one.

### How I cut, and why

- **CM-ACC-001, merchant account and store owner** (SH-C-001, SA-C-001, by M-002). Shopify holds the account mostly in
  its Terms of Service (Account Terms, Store Owner) and in the account's store list; Salla in Your profile and its
  sub-pages, the Merchant API folder and store.owner.changed.
- **CM-ACC-002, the merchant agreement's contracting party and governing law** (SH-C-002; SA-C-230, batch 2's, by M-001).
  One capability for the entity and the law, because Shopify keeps both in one concern and section 13 of its Terms;
  WooCommerce splits them (M-001's granularity note), and its part may make a child. The Salla cell already cites
  SA-C-230's statements.
- **CM-ACC-003, several stores under one owner** (SH-C-003, SA-C-003), joined on role (below).
- **CM-ACC-004, business entity**, and its child **CM-ACC-005, selling with multiple entities** (SH-C-004, SH-C-005).
  Grain: Shopify splits the two concerns because the second is limited to Shopify Payments and Plus and Enterprise
  (its split note); the second is a finer part of the first, so it is a child. Its route sits under Payments
  (SH-S-7083), but its help names the entities of CM-ACC-004 and links Organization (SH-S-6311), so I kept it in ACC
  and under CM-ACC-004 (my judgment). CM-ACC-004 has no parent: Shopify puts entities under Organization settings and
  General, Salla inside store verification (payments), so the platforms share no grouping, and I didn't follow
  Shopify's alone.
- **CM-ACC-006, store details and general settings** (SH-C-013, SA-C-002, by M-006), with its child **CM-ACC-007,
  maintenance mode**: Salla gives it a route of its own under General (`general/maintenance-mode`, SA-S-1726) and a
  plan line (SA-S-2084), and the route puts it under General. Shopify holds none.
- **CM-ACC-008, countries where the platform offers its service** (SA-C-167), joined on role (below).
- **CM-ACC-009, store management app on mobile devices.** Salla's plan line (SA-S-2082, in SA-C-001) gives it a place of
  its own, and it is not the account. No concern lands in it (the checker's flag, below).
- **What stays inside a coarser cell (my judgment).** Plan lines and permissions that are features of a page, not
  places of their own: settings search, cache clearing, store options customisation, Made in KSA (permission and
  flag), store-status (all in CM-ACC-006); saving recently opened accounts at sign-in (CM-ACC-001). Store activity is a
  sub-page of General with no definition held, so it stays in CM-ACC-006.
- **Statements read and not cited:** SA-S-1467 `salla-maintenance-alert` (SA-C-091, domain E, which doesn't name A):
  a storefront component, so maintenance mode's storefront side isn't cited here. SA-C-001/boundary/SA-S-1545 (the
  access scope settings, "Basic Information / البيانات الأساسية"): Q1 placed the statement in SA-C-001 and SA-C-002; I
  cite it once, by SA-C-002's key, in CM-ACC-006, because its name matches the store's basic info permission
  (store_setting_edit_basic_info, "تعديل بيانات المتجر الأساسية"), a reading. SH-C-001/boundary/SH-S-0076 (the Terms'
  list of incorporated policies) is not needed beyond SH-S-0229.

### Joins on role

- **CM-ACC-003** (U-009): Shopify's Organization and Salla's Manage stores / linked stores. Both hold several stores
  under one owner: Shopify creates stores from Organization settings (SH-S-5228) and its Terms let a Store Owner have
  several stores (SH-S-0238); Salla lists the linked stores and merges their accounts under one email (SA-S-5150). The
  terms differ, and Shopify's organization also carries organization-scoped settings, users and billing, that Salla's
  statements don't show for its linked stores.
- **CM-ACC-008**: Salla's markets ("Primary markets are Saudi Arabia first, followed by the GCC", SA-S-0003) and
  Shopify's unsupported countries and regions (SH-S-0298, SH-S-0289). Each is where the platform offers itself, stated
  positively by one and negatively by the other.
- **CM-ACC-004** is joined by definition, not role: Shopify's "registered business, or the individual, that your store
  operates as" (SH-S-0248) against Salla's "الكيان القانوني حدد كيان متجرك" and its type "فرد" (SA-S-0142, SA-S-0133).

### Homonyms kept apart

- **"Supported countries"** (Q1's U-034): WooCommerce's WooPayments supported countries (WC-C-010) are a payment
  service's. CM-ACC-008 cites only Shopify's platform-wide statements, not Shopify Payments' sanctions clauses
  (SH-S-0122, SH-S-0131). In the capability's note.

### Strained fits

- **SH-C-001** in CM-ACC-001: its "A Store Owner may have multiple Shopify Stores" (SH-S-0238) is also cited in
  CM-ACC-003.
- **SA-C-001** in CM-ACC-001: its plan line for the store management app (SA-S-2082) is cited in CM-ACC-009; its
  two-factor and biometric flags (SA-S-3182, SA-S-3365), cited here as shows, are sign-in security, which the TRU batch
  will likely cite too.

### Concerns of other domains read under `also`

- **SA-C-006** (domain C, Store Verification, names A): its entity steps SA-S-0142 and SA-S-0133 are cited as core in
  CM-ACC-004. The merge may flag them if domain C cites them as core for verification: they are the step in Salla's own
  verification that records the store's legal entity, which is this capability.
- **SA-C-004** (domain A, PLN batch): SA-S-2083 cited as shows in CM-ACC-009.
- **SH-C-174** (domain A, TRU batch): its platform-wide statements are the Shopify cell of CM-ACC-008.

### Rulings, and the pairs left for later batches

Ruled here: U-009 (joined:CM-ACC-003); U-008 for SH-C-004 against SA-C-006 (joined:CM-ACC-004) and SH-C-005 against
SA-C-006 (nested:CM-ACC-005). SA-C-006 lands in domain C and names A under also, so the rulings follow the cells.

Left, with the batch that lands the other side:
- **U-037, SH-C-001 against SA-C-170** (batch 2). SA-C-170, Salla's usage agreement, has no statements held. Shopify's
  agreement statements of SH-C-001 (SH-S-0229, SH-S-0019, SH-S-0017) are cited in CM-ACC-001, and the agreement's party
  and law in CM-ACC-002. Where batch 2 lands SA-C-170 decides it: in CM-ACC-001, joined; in CM-ACC-002, apart unless a
  cell there cites both sides.
- **M-001, SH-C-002 against SA-C-230** (batch 2): a match, not an unclear candidate. SH-C-002 landed by `definition`
  on M-001's own basis (SH-S-0001, SA-S-5001), because the checker refuses `match:M-001` until another of the match's
  concerns has landed; batch 2 can land SA-C-230 by `match:M-001` in CM-ACC-002. The coordinator may set SH-C-002's
  join to `match:M-001` once it has.
- **U-006, SH-C-007 against SA-C-001** (TRU batch, sign-in security). SA-C-001's two-factor and biometric flags are
  cited in CM-ACC-001 as shows; if TRU makes a sign-in security capability and cites them there, the pair is apart,
  or nested if that capability is a child of CM-ACC-001.
- **U-011, SH-C-006 against SA-C-167** (ONB batch, location at sign-up). SA-S-0141 (the store's country chosen at
  registration) is cited in CM-ACC-008 as shows; SH-C-006's SH-S-0304 is also SH-C-174's, cited there. If ONB lands
  SH-C-006 in CM-ACC-008, joined; otherwise apart unless its capability cites SA-C-167.
- **U-034, SH-C-174 against SA-C-167** (TRU batch). CM-ACC-008's Shopify cell cites SH-C-174's keys, so landing
  SH-C-174 there makes it joined:CM-ACC-008; landing it in a sanctions capability makes it strained (its keys are
  cited here) and the ruling then follows the cells (joined:CM-ACC-008 still, since CM-ACC-008 cites both sides).
- U-068 (SA-C-001 against WC-C-090) and U-069 (SA-C-002 against WC-C-082) are WooCommerce's part's.

### What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/A-anchor --concerns SH-C-001,SH-C-002,SH-C-003,SH-C-004,SH-C-005,SH-C-013,SA-C-001,SA-C-002,SA-C-003,SA-C-167 --areas ACC`:
0 problems, 3 flags.
- *CM-ACC-009 shopify none-held, 6 statements match:* SH-S-6059 is the access scope for `AndroidApplication` and
  `AppleApplication` objects (SH-C-158, SH-C-159, SH-C-195), SH-S-0723 is Shop, the buyers' app (SH-C-136), and
  SH-S-2701 / SH-I-1937 are the app-store category Mobile app builder apps (SH-C-195): the store's apps for buyers, not
  an app for managing the store. None shows Shopify's own admin app.
- *SH-S-0238 cited in CM-ACC-001 and CM-ACC-003:* intended. One clause states both that a store has one Store Owner
  (the account) and that a Store Owner may have several stores (the stores under one owner). SH-C-001 is marked
  strained for it.
- *CM-ACC-009 has no concern landed in its tree:* intended. Salla's plan line gives it a place of its own; its
  statement is SA-C-001's, landed in CM-ACC-001 (strained for it). Mapping parts may land a platform's mobile admin app
  here.

### Problems and gaps

- **Salla's merchant agreement isn't held:** SA-C-170 has no statements, and SA-C-230's where, decides, boundary and
  reason are "page not read". So Salla's contracting entity per market and its governing law aren't held; its held
  terms name two companies and two registration numbers across its partner-facing agreements (SA-S-0015 to SA-S-0019,
  SA-S-5121).
- **Salla's account responsibility:** SA-C-001/responsible, SA-C-002/responsible and SA-C-003/responsible are "page not
  read".
- **Shopify's organization API:** SH-C-003/boundary is "searched, not found"; no API resource for organizations is
  held.
- **Countries:** SA-C-167/where is "page not read" and /boundary "observation needed"; the footer lists only two
  markets (SA-I-1206, SA-I-1207).
- **Maker of Salla's store management app:** no statement names its maker or route beyond the plan lines.

## The coordinator's correction after batch 1 (30 October)

- **CM-ACC-009 is removed.** The store management app on mobile devices is domain G's CM-SRF-001, the mobile app for managing the store, which already has a cell for every platform and cites Salla's plan line SA-S-2082 as `core`. Kept here, the line would have counted in two domains for one capability. No concern landed in CM-ACC-009, so nothing else moves; SA-C-001 stays `strained`, its plan line now cited in G's tree. Salla's subscription line in the iOS app (SA-S-2083), cited here as `shows`, is the PLN batch's to weigh.


## Batch 2: ACC's last two Salla concerns, and STF, Staff, roles and permissions

Concerns: SA-C-170, SA-C-230 (ACC); SH-C-009, SH-C-010, SH-C-011, SA-C-009, SA-C-013 (STF).
Result: 5 capabilities (CM-STF-001 to CM-STF-005), 7 landings (2 in batch 1's capabilities, 5 in new ones), 10
cells, 59 evidence rows (56 in STF, and 3 added to batch 1's cells CM-ACC-001 and CM-ACC-002), 3 qualities, 2 rulings.
`caps` across every domain found no staff, role, user-group, staff-target or collaborator capability elsewhere
(the nearest: F's CM-PTN-002, the partner's own account and its employees, which is the partner's side, not the
store's).

### ACC: SA-C-170 and SA-C-230

- **SA-C-230 lands in CM-ACC-002 by `match:M-001`**, as batch 1 left it. Its statements were already cited there; I
  added the footer's 2026 line (SA-S-0020). SA-S-0010 (Salla's headquarters, Mecca) is left uncited: a headquarters
  isn't the contracting party or the governing law. The coordinator may now set SH-C-002's join to `match:M-001`.
- **SA-C-170 lands in CM-ACC-001, joined on role, `strained`.** Batch 1's notes say SA-C-170 has no statements; it has
  two: the agreement's page in the sitemap (salla.com/terms, SA-S-2208) and the registration step that binds the
  merchant to the usage policy (SA-S-0143). The second has the same role as Shopify's SH-S-0229 ("signing up for a
  Shopify Account" binds the merchant to the Terms), which batch 1 cites in CM-ACC-001. So both are cited there as
  shows. Strained, my judgment: the concern is the whole merchant agreement, and its party clause, which would be
  CM-ACC-002's, is "page not read". The reviewer may prefer a capability of its own for the merchant agreement; no
  platform gives it an admin place, only a legal page, so I didn't make one.
- **For the coordinator (batch 1's rows):** CM-ACC-001's Salla cell's `terms` and `reading` don't yet name SA-C-170's
  statements (اتفاقية الاستخدام, سياسة الاستخدام على منصة سلة; SA-S-0143, SA-S-2208), and CM-ACC-002's Salla
  reading doesn't name SA-S-0020 and still says "which batch 2 lands". I appended evidence only, as the brief asks.

### STF: how I cut, and why

- **CM-STF-001, staff accounts** (SH-C-009, SA-C-009, by M-004), and its child **CM-STF-002, roles and permissions**
  (SH-C-010, by M-004). Grain: M-004 holds two Shopify concerns against one Salla concern. Both platforms give roles
  a route of their own under staff (Shopify settings:organizations:accounts:roles, SH-S-5234, under
  settings:organizations:accounts, SH-S-5233; Salla /users/roles, SA-S-1851, under /users, SA-S-1849), so roles are a
  child of staff accounts, and SA-C-009, the coarser concern, lands in the parent.
- **CM-STF-003, user groups** (child of CM-STF-001): Shopify gives it a route (SH-S-5237) and a plan line (Custom user
  groups, SH-S-7077), so it is a capability by the dry run's convention. No concern lands in it; its statements are
  SH-C-010's, a sibling in the same tree, so SH-C-010 stays clean.
- **CM-STF-004, staff targets** (child of CM-STF-001): Salla's link Employees targets (/users/targets, SA-S-1853) is
  a route of its own. No concern lands in it; it is SA-C-009's, landed in the parent. Nothing held defines it.
- **CM-STF-005, third-party access to the merchant's admin** (SH-C-011, SA-C-013), joined on role (below). No parent:
  Shopify routes collaborators under its users (SH-S-7151) and files the permission under USER_MANAGEMENT (SH-S-7167);
  Salla serves support access from its manage pages (SA-S-3533), beside webhooks and migration. The groupings differ,
  so, as batch 1 did for CM-ACC-004, I followed neither.
- **What stays inside a coarser cell (my judgment):** the staff permissions ADD_REMOVE_STAFF, MANAGE_STAFF_PERMISSIONS
  and STAFF_API_PERMISSION_MANAGEMENT ("Revoke access tokens"); the flags store-team and user-advance-management; the
  store feature rbacEnabled (cited in CM-STF-002, my reading of "rbac" as role-based access control, so marked a
  reading). Shopify's 20 built-in staff roles (inventory entries SH-I-0846 to SH-I-0865) aren't cited: SH-S-0247, the
  Administrator role, already shows built-in roles, and the POS roles among them bear on E's point of sale.
- **Staff of other features stay in their domains:** order assignment to staff (SA-C-043, domain C), Salla Point's
  staff (SA-C-095, SA-S-2442, domain E), and the partner portal's Employees (SA-C-204, SA-S-1934, domain F).

### Joins on role

- **CM-STF-005** (U-010): Shopify's collaborators and Salla's support access requests. On both, a party outside the
  store's staff asks for access to the merchant's admin, and the merchant grants and bounds it: Shopify's Terms let the
  merchant allow Third Party Providers into parts of its Admin and control their access levels (SH-S-0239), with a
  staff permission to manage the requests (SH-S-7167); Salla's partner asks from its service's page (SA-S-5131), the
  staff permission is support_access_requests (SA-S-2404), and the partner may not use the permissions the merchant
  granted beyond the agreed work (SA-S-5008). The differences: Salla's concern also names its own support's access,
  which no held statement describes; Shopify's collaborator access is on every plan (SH-S-7012).
- **CM-ACC-001** for SA-C-170 (above): each platform's agreement accepted when the account is opened.

### Homonyms kept apart

- **"groups":** Salla's Customer groups (SA-C-061, domain D's CM-CUS-002) are buyers' groups, not Shopify's Custom
  user groups of staff. In CM-STF-003's note and the Salla cell.
- **"Employees":** Salla's API folder Employees (SA-S-1066) is the store's staff; its partner portal's Employees link
  (SA-C-204, SA-S-1934) is a partner's own staff, F's.

### Strained fits

- **SA-C-170** in CM-ACC-001 (above). Its statements are cited only there; it is strained for what doesn't fit, the
  agreement's party clause, a gap.

### Statements read and not cited

- SH-C-009/boundary/SH-S-6142: the scope read_users or read_financial_kyc_information on FinanceAppAccessPolicy, a
  finance app's object, not the store's staff.
- SH-S-5291 and SH-S-5292 (hasOrgSettings): batch 1 cites them in CM-ACC-003 under SH-C-003's keys; citing them again
  under SH-C-009's would put one statement in two trees.
- SH-S-0245 (the organization administrator "can manage all users and roles", SH-C-003): cited by batch 1 in
  CM-ACC-003 as shows. It bears on CM-STF-002 too; I didn't cite it twice. The coordinator may move it.
- SA-C-013/where/SA-S-1933, the link Store management (/store-management, list 9): Q1 placed it in SA-C-013, but
  nothing held ties the link to support access. It isn't Manage stores (/stores, SA-S-1680). Left uncited; the
  reviewer may know which list it belongs to.
- SA-C-009/boundary/SA-S-1066 is the same statement as SA-C-009/where/SA-S-1066, cited once.

### Rulings, and the pairs left for later batches

Ruled here: U-037 (joined:CM-ACC-001), U-010 (joined:CM-STF-005). M-001 is a match: SA-C-230 landed by it.

Left, with the batch that lands the other side:
- **U-036, SH-C-014 against SA-C-170** (ONB batch) and **SH-C-172 against SA-C-170** (TRU batch). SA-C-170 is in
  CM-ACC-001, citing the registration step that binds the merchant to the usage policy (SA-S-0143). The policy's
  text, which U-036 asks about (violations, termination), isn't held. If the later batch's capability cites no
  SA-C-170 key, the pair is apart.

### What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/A-anchor --concerns SA-C-170,SA-C-230,SH-C-009,SH-C-010,SH-C-011,SA-C-009,SA-C-013 --areas ACC,STF`:
0 problems, 2 flags.
- *CM-STF-003 salla none-held, 27 statements match:* all are buyers' groups (Customer groups, customer-group,
  تصنيف العملاء إلى مجموعات), coupon groups (coupon-group, إنشاء مجموعة كوبونات) and batch actions on orders or
  customers (إدارة مجموعة طلبات كدفعة واحدة, إدارة مجموعة عملاء كدفعة واحدة). None is a group of staff.
- *SH-S-0238 in CM-ACC-001 and CM-ACC-003:* batch 1's, answered in its section.

### Problems and gaps

- **Salla's built-in roles and its permission count** (the seed's "10 built-in roles; 192 permissions in 16 groups")
  aren't held as statements: the permission list's group headings are unplaced inventory entries (SA-I-1244 to
  SA-I-1440, "a group heading"), and no statement names a built-in role.
- **Salla's staff-account limit:** only "more users, for extra fees" on سلة بلس (SA-S-2078) is held; no number.
- **Who answers for staff** on Salla: SA-C-009/responsible is "page not read". Shopify's reasons for SH-C-009 and
  SH-C-010 are "searched, not found".
- **Staff targets** have no definition on either platform.

## The coordinator's corrections after batch 2 (30 October)

- **SH-C-002 is written as Q1's match M-001,** now that SA-C-230 has landed in CM-ACC-002.
- **CM-ACC-001's and CM-ACC-002's Salla cells** name batch 2's rows at the end of their readings.
- **Batch 1's note that SA-C-170 has no statements is wrong:** it has two, its usage agreement (SA-S-0143) and SA-S-2208, which batch 2 cites.


## Batch 3: PLN, Plans, entitlements and platform billing

Concerns: SH-C-015, SH-C-016, SH-C-017, SH-C-018, SH-C-201, SA-C-004, SA-C-005. Seven capabilities, CM-PLN-001 to
CM-PLN-007, in two trees: the plan (001, with 002 and 003) and the platform's billing (004, with 005, 006 and 007).
Searched every domain first (`caps` with plan, باقة, subscription, اشتراك; billing, فوترة, invoice, فاتورة; balance,
رصيد, wallet, محفظة; transaction fee, commission, عمولة, رسوم; tax, ضريبة, VAT; renew, تجديد, term, contract, عقد;
entitlement, feature, beta, preview, مزايا; iOS, iTunes, آيتونز, mobile app). No domain holds the platform's own plans
or billing: the nearest are F's app charges billed through the platform (CM-APP-003), partner billing (CM-PTN-004)
and the plans' referral programme (CM-PTN-008), D's ads wallet (CM-MKT-020) and customer wallet (CM-LOY-001), and G's
feature settings (CM-EVO-001) and mobile app for managing the store (CM-SRF-001), each a different thing.

### How I cut, and why

- **Plans (CM-PLN-001)** by Q1's M-007: Shopify's Plan, Plus and subscribe routes and its ShopPlan object; Salla's
  Store plan and its plans flag.
- **Entitlements are not a capability of their own.** I first wrote one (what each plan includes) and removed it
  before the check, renumbering this batch's own capabilities. Reasons: every plan line and plan-scoped flag names a
  capability of its own, in its own domain, so the cell would either cite other capabilities' plan lines (making
  their concerns strained by S1: SH-C-003's SH-S-7073 and SA-C-009's SA-S-3084, which the first check showed) or rest
  on nothing but the plans flag; and neither platform gives entitlements a place apart from the plan pages. What a
  plan includes is therefore read in CM-PLN-001, with Salla's features_count per plan (SA-S-3528) as a quality there.
  Shopify's route eligibility carries "entitlements" keys (such as "entitlements":["products"], SH-C-020's SH-S-5016),
  but no held statement says they come from the plan; not cited. If the coordinator wants an entitlement capability,
  it would need a statement defining it.
- **Term and renewal (CM-PLN-002)** under the plan: Shopify gives the Plus contract and its renewals a place of their
  own (plus/renew, plus/terms, contractmanagement: SH-C-201) and the plan's period a route (pick_period). It lands
  SH-C-201 as single. Salla's cell cites the annual subscription's freeze (SA-S-2085) and the plan's automatic renewal
  from the store balance (SA-S-0089).
- **Platform fee on sales (CM-PLN-003)** under the plan: Shopify's third-party transaction fees, and Salla's سلة سبيشل
  plan line "no platform commission on your sales". Both platforms show it as a plan line, the grouping they share;
  Shopify also shows it on the bill (settings/billing, the Transaction fees charge category). Payment processing fees
  are C's.
- **Platform billing (CM-PLN-004)** by M-008, with three children: **paying the bills (CM-PLN-005)**, which Shopify
  gives a permission and routes of its own (Edit billing payment methods and pay invoices; delete-payment-method;
  pay-bills; payment authentication); **the prepaid store balance (CM-PLN-006)**, which Salla gives a navigation link
  (Wallet), a plan line and help pages, and groups with billing (the plan-feature heading محفظة المتجر والفوترة,
  SA-I-1061, and Settings > Balance & billing); and **taxes on the platform's own charges (CM-PLN-007)**, which
  Shopify gives the billing page's Tax registration section. M-008's note already says Salla's concern also holds the
  balance; it is a difference of grain, landed in the parent.
- **Purchases from Salla's store** (store_setting_purchase_from_salla_store, الشراء من متجر سلة) and pay-as-you-go
  usage billing (payg-usage-billing) are read in CM-PLN-004: each is a permission or a flag, not a place of its own.
- **SH-C-017 lands as single,** not by M-009: M-009's other concern is WooCommerce's WC-C-057, which no part has
  landed, and batch 1 found that the checker refuses a match until another of its concerns has. WooCommerce's part can
  land WC-C-057 in CM-PLN-007 by M-009.

### The coordinator's lead: SA-S-2083

Salla's سلة بلس plan line "managing the subscription in Salla's iOS app with iTunes balance" is cited in CM-PLN-005,
paying the platform's bills, as core (a plan line that includes it), with Apple's iTunes balance as the slot filler
(reading: the means of payment there is Apple's; the statement names iTunes, not Apple, as a company, and no maker
statement is needed since nobody makes the capability for Salla). It makes SA-C-004 strained: SA-C-004 lands in
CM-PLN-001 and this statement is cited in the billing tree. The iOS app itself, as Salla's merchant app, is G's
(CM-SRF-001 holds WooCommerce's mobile app for managing the store); if G's back-fill cites SA-S-2083 for Salla's
merchant app as core, the merge will flag it in two domains, and one of the two should be shows.

### Joins on role

- **CM-PLN-003:** Shopify's third-party transaction fees, "fees relating to the value of sales made through your
  Store when using all payment providers other than Shopify Payments" (SH-S-0032), varying by plan (SH-S-0273,
  SH-S-7030), against Salla's "بدون عمولة منصة على مبيعاتك" (SA-S-2198). Both are a fee the platform takes on the
  merchant's sales, set by plan. The difference: Shopify's is conditional on the payment provider; Salla's statement
  only says one plan doesn't carry it, so its cell is shows, not-stated. SH-C-018 lands by role.
- **CM-PLN-005:** what the platform's bills are paid from. Shopify charges a payment method on file (SH-S-7171,
  SH-S-0035); Salla draws on the store balance (SA-S-0089) and, in the iOS app, iTunes balance (SA-S-2083).

### Homonyms kept apart

- **Balance:** Salla's store balance (رصيد المتجر, SA-C-005), prepaid and spent on Salla's services, against Shopify
  Balance (SH-C-088, domain C), a money account receiving the merchant's sales (SH-S-0347, SH-S-0460). CM-PLN-006's
  Shopify cell is none-held, which the checker flags (86 statements match "balance"): they are Shopify Balance, Shop
  Pay Wallet and PayPal Wallet, none a balance that pays Shopify.
- **Wallet:** Salla's Wallet page (/payments/wallet, SA-S-1876) holds both the store balance and the e-payments
  balance (SA-S-0089's heading, SA-S-0091); only the store balance is here. Salla's customer wallet (محفظة العميل) is
  D's CM-LOY-001.
- **Commission (عمولة):** Salla's platform commission on sales (SA-S-2198) against affiliate commissions (SA-C-072,
  SA-C-173, D's), app and partner commissions (SA-C-194, SA-C-195, SA-C-208, F's) and Salla's commission on shipping
  settlements (SA-C-145). Only the first is cited here.

### Strained fits

- **SA-C-004** (in CM-PLN-001): SA-S-2083 is cited in CM-PLN-005 and SA-S-5002 (a plan refund goes back to the store
  balance) in CM-PLN-006, both in the billing tree.
- **SA-C-005** (in CM-PLN-004): SA-S-0089 (the store balance renews the plan automatically) is cited in CM-PLN-002,
  in the plan tree. The checker flags SA-S-0089 and SA-S-5002 as cited in two trees; the strained fits answer them.
  The two trees meet in Salla's own words: its balance pays its plan.

### Concerns of other domains read under `also`

Read and not cited: SH-C-019 (F, app charges on the Shopify bill: CM-APP-003's), SH-C-033 (E, domain fees),
SA-C-195 (F, app billing and partner payouts). SH-C-016's charge categories (SH-I-1322 to SH-I-1358) list fees for
apps, domains, themes, shipping, Shopify Fulfillment Network, POS and others; each category is evidence for the
service it bills for, in that service's domain, and none is cited here.

**SA-C-113** (domain C, not naming A) is cited once: its tooltip giving VAT at 15% on the total of the fees
(SA-S-0105), in CM-PLN-007's Salla cell, as shows only, so that it supports no placement here and stays C's for its
fees. The checker flags it. It is the only held statement of tax on Salla's own charges; none states tax on Salla's
plan or bills.

### Rulings, and the pairs left for later batches

Ruled here:
- **U-077** (SH-C-018 against SA-C-004): joined:CM-PLN-003.
- **U-029** (SH-C-017 against SA-C-113): joined:CM-PLN-007. **For the coordinator:** the brief says a pair whose
  other concern is in another domain that doesn't name A is apart, with the basis "scope.tsv gives SA-C-113 domain C";
  the checker, following "a ruling follows the cells", refuses apart while CM-PLN-007 cites both sides. I first wrote
  apart and the checker printed a problem. I kept the citation, since the brief also says never to leave a statement
  uncited to keep a ruling apart, and wrote joined, with the domain in the basis. If the coordinator prefers apart, the
  Salla cell would become none-held and SA-S-0105 would go uncited here.

Left for later batches:
- **The ONB batch** takes trials and the inactive and pending-termination states. This batch cites SH-C-015's and
  SH-C-016's inactive-account routes (access_account/plus, reactivate:pick-plan, inactive-account pick_period,
  invoices, billing history, pay-bills: SH-S-5091, SH-S-5071, SH-S-5086, SH-S-5072 to SH-S-5077) for the plan and
  billing they reach, and Salla's unreleased plan-free-trial flag (SA-S-3452) in CM-PLN-001 as shows. If ONB cites
  them for an account-state capability, the checker will flag them in two trees; the routes' own names put them in
  the plan and billing (reading).
- No unclear candidate of this batch's concerns waits on ONB or TRU.

### What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/A-anchor --concerns SH-C-015,SH-C-016,SH-C-017,SH-C-018,SH-C-201,SA-C-004,SA-C-005 --areas PLN`:
0 problems, 6 flags.
- *SA-S-0105 of SA-C-113, domain C without A:* answered above.
- *CM-PLN-006 shopify none-held, 86 statements match:* the homonym Balance, answered above.
- *SA-S-5002 and SA-S-0089 in two trees:* the strained fits, answered above.
- *CM-STF-003 salla none-held* and *SH-S-0238 in CM-ACC-001 and CM-ACC-003:* batches 1 and 2's, answered there.

No problem found on earlier batches' rows.

### Problems and gaps

- **Salla's commission on sales:** only the Special plan's line saying it carries none is held; no statement gives the
  commission on other plans or its rate.
- **Tax on Salla's plan or bills** isn't held; only VAT on the e-payments fees (SA-C-113).
- **Shopify Plus's agreement** (term, renewal clauses) is "observation needed" (SH-C-201's responsible, boundary and
  reason); the 3-year term is only a page title.
- **Salla's billing** has no who-answers or reason statement (SA-C-005's responsible and reason are "page not read"),
  and no statement names a card or other payment method for Salla's bills.
- **Prices** (Shopify's Pay monthly and Pay yearly rows) and fee rates (Third-party transaction fees: 2%, 1%, 0.6%,
  0.2%) are cited as evidence, not as qualities: the brief's qualities are limits, certifications, uptimes and data
  locations.

## The coordinator's correction after batch 3 (30 October)

- **SA-C-113 names A under `also`.** Its statement that VAT at 15% applies to Salla's own fees (SA-S-0105) is the only held statement of tax on Salla's charges, and CM-PLN-007 cites it. With A under `also`, the citation and U-029's `joined:CM-PLN-007` both follow convention S3.
- **For the ONB batch:** batch 3 cites Shopify's inactive-account plan and billing routes (SH-S-5071 to SH-S-5077, SH-S-5086, SH-S-5091) and Salla's unreleased plan-free-trial flag (SA-S-3452). Where ONB's capabilities need them, cite them there too and mark the fit by the cells.


## Batch 4: ONB, Onboarding and store lifecycle

Concerns: SH-C-006, SH-C-014, SH-C-155; SA-C-014. Result: 3 capabilities (CM-ONB-001 to CM-ONB-003), 4 landings, 6
cells, 38 evidence rows (one of them added to CM-STF-005's Salla cell), 2 qualities, no slot filler, 3 rulings.

### How I cut, and why

- **CM-ONB-001, the merchant's country at sign-up.** Shopify gives it a place of its own, the sign-up page's "I'm
  located in:" (SH-S-7174); Salla's registration asks the store's country (SA-S-0141). I kept it apart from
  CM-ACC-008 (my judgment): CM-ACC-008 is where the platform offers its service, this is the one merchant's own
  location. Nor is it CM-ACC-006's store details: Shopify's duty to keep the location current in the admin
  (SH-S-0038) is SH-C-006's own statement, so it is cited here as shows.
- **CM-ONB-002, the store's lifecycle states.** Shopify places restricted access, the inactive account, pending
  termination and reactivation in admin routes of their own (store-unavailable, access_account, account_review,
  reactivation), so they are one capability with its routes, not one per state (my judgment: Salla shows only one
  state, suspension, so a finer cut would leave Salla's side empty on every child but one, and no statement defines
  the states apart). The enforcement that leads to them (acceptable use, violations) is TRU's: SH-C-172 and SA-C-232.
- **CM-ONB-003, the platform's support and learning for merchants,** Q1's M-066, one-to-one. The account manager
  (Salla's مسؤول الحساب, مدير حساب مخصص, on سلة سبيشل) stays inside it (my judgment): Shopify's counterpart is a
  level of the same plan row (Priority support on Plus, SH-S-7015), so both platforms grade support by plan rather
  than giving the account manager a capability of its own across both.
- **Trials and onboarding steps.** No statement of either platform holds a store's trial: Shopify's trial is only in
  the plan table's header text (scopes "Start for free", "Try for $399") and in app billing (SH-S-0285, domain F);
  Salla's plan-free-trial flag is unreleased (SA-S-3452, in CM-PLN-001 as shows). No statement holds Shopify's
  onboarding question or home setup, or Salla's onboarding vocabulary, and no Salla concern of the seed's ONB leads
  (help: New store; store_status) is in my batch beyond SA-C-014. So no trial or setup capability (gap).
- **Batch 3's inactive-account routes** (SH-S-5071 to SH-S-5077, SH-S-5086, SH-S-5091, under SH-C-015's and SH-C-016's
  keys) are not cited again: CM-ONB-002 rests on SH-C-014's own route keys (the inactive-account root, its list and its
  checkout, reactivate and reopen routes, SH-S-5068 to SH-S-5070), and the routes batch 3 cites are named for the plan
  or bill they reach (reading). Salla's annual-subscription freeze (SA-S-2085) and plan cancellation (SA-S-5003) stay
  in PLN: they freeze or cancel the plan, and no statement says the store's state changes.

### Joins on role

- **CM-ONB-001:** Shopify's "I'm located in:" on its sign-up page (SH-S-7174) and Salla's دولة المتجر, "choose from
  which country you register your store" (SA-S-0141): different names, the same role, the country the merchant gives
  when creating the store. A reading.

### Homonyms kept apart

- **"Store status":** domain G's CM-OPS-004 is WooCommerce's system status report and tools, not a store's lifecycle
  state; Salla's store-status flag (SA-S-3353) is cited by batch 1 in CM-ACC-006 and no statement says what it is.
- **"Self-service system":** SA-C-014's name carries it, but Salla's Self-service system (نظام التذاكر) is the
  merchant's ticket system for its own customers (SA-C-179, domain D's CM-SUP-005). No SA-C-014 statement holds it.
- **"Shopify Support"** in access-scope statements (SH-S-6001, SH-S-6058, SH-S-6243 and others: contact Shopify Support
  to request a scope) is support to app developers, domain F's, not cited.

### Strained fits

- **SH-C-006 in CM-ONB-001:** its sentence barring sign-up from unsupported countries and regions (SH-S-0304) is also
  SH-C-174's, cited under that key in CM-ACC-008; Salla's SA-S-0141 is cited in both trees.
- **SA-C-014 in CM-ONB-003:** its statement that support's temporary access requests appear on /manage/support-access
  only with the merchant's approval (SA-S-5132) is cited in CM-STF-005, as core: it is the empty state of Salla's own
  page for third-party access to the admin, which is that capability's subject.

### Concerns of other domains read under `also`

- **SA-C-006** (Store Verification, domain C, A under also): its copy of SA-S-0141, scoped to the article on creating a
  store in the UAE, is cited in CM-ONB-001 beside SA-C-167's copy. The same sentence is held under both concerns; I
  cite both keys so the cell keeps the article's scope and both of U-011's pairs follow the cells (batch 2 cited a
  statement held twice under one concern once; here the two keys are two concerns).
- **SA-C-232** (violations, domain A, the TRU batch's): its warning that an uncorrected violation suspends the store
  within 24 hours (SA-S-0115) is CM-ONB-002's only Salla statement, cited as shows, with its 24 hours as a quality.
  If TRU cites it in its enforcement capability too, the checker will flag it in two trees; the suspension is this
  capability's subject, the violation TRU's (reading).
- Not cited: SA-S-5061 (postpaid shipping dues paid late may suspend the postpaid service or some store features,
  SA-C-140), SA-S-5079 (the App Maker policy's disclaimer on suspension in Google's and Apple's stores, SA-C-174) and
  SA-S-0028 (Salla may suspend an app, SA-C-232): none is the store's own state.

### Rulings, and the pairs left for later batches

Ruled here:
- **U-011, SH-C-006 against SA-C-167:** joined:CM-ONB-001. **SH-C-006 against SA-C-006:** joined:CM-ONB-001, the
  ruling following the cells (SA-C-006 names A under also).
- **U-036, SH-C-014 against SA-C-170:** apart. SA-C-170's held statements (SA-S-0143, SA-S-2208) show the agreement's
  registration step and page, not termination; the policy's text isn't held.

Left for the TRU batches:
- **U-036, SH-C-014 against SA-C-232:** CM-ONB-002 cites SA-C-232's SA-S-0115 as shows, so wherever TRU lands SA-C-232
  the pair is joined:CM-ONB-002 by the cells, unless the coordinator moves SA-S-0115 to TRU's capability, in which case
  it follows that capability's cells. **SH-C-172 against SA-C-232 and SA-C-170** are TRU's.
- M-066's third concern, WC-C-062, is WooCommerce's part's.

### What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/A-anchor --concerns SH-C-006,SH-C-014,SH-C-155,SA-C-014 --areas ONB`:
0 problems, 8 flags.
- *SA-C-167/decides/SA-S-0141 in CM-ACC-008 and CM-ONB-001,* and *SA-C-167 clean in CM-ACC-008, its statements cited
  in CM-ONB-001:* see below, for the coordinator.
- *SH-C-016 clean in CM-PLN-004, its statements cited in CM-ONB-002:* the inventory entry SH-I-2350, the help section
  "Understanding billing implications before pausing or deactivating your Shopify store", is placed in both SH-C-014
  and SH-C-016. I cite it in CM-ONB-002 as shows, as the only held mention of pausing or deactivating a store; batch 3
  doesn't cite it. See below.
- *CM-STF-003, CM-PLN-006, SA-S-5002, SA-S-0089, SH-S-0238:* batches 1 to 3's, answered there.

### For the coordinator: earlier batches' rows

- **CM-ACC-008's Salla cell (batch 1)** cites SA-S-0141 as shows. Its subject is the one store's country at
  registration, CM-ONB-001's; for CM-ACC-008 it adds only that a country is chosen. Either drop it there, or mark
  SA-C-167 strained in CM-ACC-008 (the checker's flag).
- **SH-C-016 (batch 3)** is now strained by SH-I-2350, cited in CM-ONB-002; or drop SH-I-2350 from CM-ONB-002 if the
  section's billing subject is judged to govern.
- **CM-STF-005's Salla cell (batch 2):** I added SA-C-014/boundary/SA-S-5132 as core; its reading should name it.

### Problems and gaps

- **Salla's store lifecycle:** no statement holds an inactive, pending-termination, closed or reactivated store, or
  Salla's terms on suspension and termination (SA-C-170's policy text isn't held).
- **Trials** of either platform aren't held as statements (above).
- **Makers:** no statement names the maker of Shopify Community, Learn or Academy, or of Salla's help centre; they are
  placed by what the statements show.
- **Shopify's sign-up location:** SH-C-006/boundary and /reason are "searched, not found". **Shopify's support:**
  SH-C-155/responsible is "stated only in general terms". **Salla's support:** SA-C-014/responsible and /reason are
  "page not read".

## The coordinator's corrections after batch 4 (30 October)

- **SA-C-167 and SH-C-016 are `strained`:** batch 4 cites SA-S-0141 in CM-ONB-001, and SH-I-2350 (placed by Q1 in SH-C-016 and SH-C-014) in CM-ONB-002, other trees (S1). Both citations bear on their capabilities, so both stay.
- **CM-STF-005's Salla reading** names the row batch 4 added (SA-S-5132).


## Batch 5: TRU, Security, privacy, trust and audit (the first of three batches on it)

Concerns: SH-C-007, SH-C-008, SH-C-012, SH-C-051, SH-C-147, SH-C-148, SH-C-149, SH-C-172, SH-C-174, SH-C-175. Result:
10 capabilities (CM-TRU-001 to CM-TRU-010), 10 landings (9 in new capabilities, SH-C-174 in batch 1's CM-ACC-008), 20
cells, 117 evidence rows (two of them added to CM-ACC-008's Shopify cell), 2 qualities, 5 slot fillers, 6 rulings.
Every capability has a Shopify and a Salla cell, so batches 6 and 7 find them ready.

### How I cut, and why

- **CM-TRU-001, sign-in security.** Shopify gives it Settings > Security and the organization's accounts:security
  routes (SH-S-1484, SH-S-5238); Salla states two-factor sign-in to the dashboard as mandatory (SA-S-5115). No parent
  (my judgment): Shopify's route is under the organization's accounts, for every user, and Salla's heading under platform
  security (SA-C-234), so neither grouping puts it under CM-ACC-001. The sign-up page's options (Continue with Google,
  Apple, Facebook, WhatsApp, email) are inventory entries cited as core; I wrote no slot fillers for them, since a button
  naming a company doesn't say the company does the sign-in (reading).
- **CM-TRU-002, identity verification of the people behind a store.** Shopify gives it a route and sections of its own
  (profile-assessment, Trust, ProfileAssessment). Salla's only held statements are steps of its store verification
  (Absher SMS to the owner, SA-S-0132; beneficial owners' data, SA-S-0138), cited as shows so that the verification counts
  once, in domain C. Shopify Payments' KYC (SH-C-068) shares the ProfileAssessment section (its platform_terms); domain C
  should check that its verification capability doesn't cite SH-C-008's route keys as well.
- **CM-TRU-003, the audit log,** Q1's M-005. Salla's Logs section also holds the export log, domain G's CM-MIG-004 (G
  cites SA-S-2122, SA-S-2423, SA-S-2640, SA-S-3234); I cite only the audit rows, and SA-S-3548, the Logs app at /logs,
  which G doesn't cite. The webhook audit_events/admin_api_activity stays here: it is Shopify's own API for this feature.
- **CM-TRU-004, bot protection,** Shopify only so far (Settings > Bot protection, a Plus plan line).
- **Privacy, Q1's M-059, at two grains.** Salla keeps cookies, export and deletion in SA-C-066; Shopify splits SH-C-148
  from SH-C-149. So CM-TRU-005 is the parent, for SA-C-066 (batch 7, by match:M-059 once it lands), with CM-TRU-006
  (privacy settings, cookie consent, the consent API) and CM-TRU-007 (data requests and erasure) for Shopify's two. The
  parent's cells hold the statements on the merchant's privacy duties as a whole and the API category Privacy (SH-I-0019,
  placed by Q1 in both Shopify concerns).
- **CM-TRU-008, Shopify Network Intelligence (Enhanced Services),** under CM-TRU-006 because Shopify puts its setting in
  the Customer privacy settings (SH-S-6326). More than a flag (my judgment, for the convention on when something is a
  capability): it has its own section of the Terms (9.2 Enhanced Services), its own controller role in the DPA
  (SH-S-0192), and other features depend on it (Shop, managed payment methods). The reviewer may judge it a setting of
  CM-TRU-006 instead and land SH-C-147 there.
- **CM-TRU-009, acceptable use and enforcement.** Salla's /manage/violation gives it a place; Shopify's AUP and its report
  form. The store states that enforcement leads to stay in CM-ONB-002: SH-C-172's restricted-access, appeal and
  termination statements are held under SH-C-014 too and cited there by batch 4, so I don't cite them again.
- **SH-C-174 lands in CM-ACC-008,** whose Shopify cell already rests on its keys; I add its two remaining platform-wide
  restrictions (products from, and orders to, unsupported regions: SH-S-0306, SH-S-0307). No sanctions capability: no
  statement gives sanctions screening a place of its own, and Salla holds no sanctions term (Q1's U-035). Its Shopify
  Payments sanctions clauses (SH-S-0122, SH-S-0131), the processors' KYC/AML duties (SH-S-0099, SH-S-0100) and the
  sanctions account hold (SH-S-0353, which doesn't say whose account) are left uncited for domain C's Payments
  eligibility, and the app developer's export classification (SH-S-0296) for domain F. scope.tsv names C under SH-C-174's
  `also`, so domain C may cite them; domain F, not named, would cite SH-S-0296 only with a reason (the brief's rule).
- **CM-TRU-010, the merchant's legal compliance as the seller,** Q1's M-086. Shopify's help Compliance section and its
  product disclosures give it a place. Salla's cell holds the e-commerce laws' requirements (SA-S-0160, SA-S-0118) as
  shows. The help sections naming laws (GPSR, the European Price Indication Directive, CPSC eFiling, TSE in Germany) are
  inventory entries, not statements, so I wrote no slot fillers for them; three are cited as shows.

### Joins on role

- **CM-TRU-001:** Shopify's two-step authentication against Salla's المصادقة الثنائية (two-factor), each a second step at
  sign-in to the admin (SH-S-0260, SH-S-5238; SA-S-5115, SA-S-3182). Q1's U-006.
- **CM-TRU-002:** Shopify's identity verification, completed by the store owner (SH-S-0263), against Salla's Absher check
  of the store owner and its beneficial owners' data (SA-S-0132, SA-S-0138): the platform checks the identity of the
  people behind the store. Q1's U-007.
- **CM-TRU-006:** Shopify's consent banner and privacy settings against Salla's website-cookies flag and its consent to
  the privacy policy at buyers' registration (SA-S-3372, SA-S-5023).
- **CM-TRU-007:** Shopify's Request data and Erase personal data against Salla's flags customer-data-export and
  customer-account-deletion, on the flags' names only.
- **CM-TRU-009:** Shopify's AUP report and enforcement against Salla's violations page (SA-S-0116, SA-S-0115).
- **CM-TRU-010:** Shopify's Your Responsibilities against Salla's e-commerce law requirements (SA-S-0160, SA-S-0118).
- **CM-ACC-008:** SH-C-174's unsupported regions against SA-C-167's markets (batch 1's join; SH-C-174 now lands there).
- SH-C-012 lands by `terms` (audit), not `match:M-005`, because SA-C-010 hasn't landed; the coordinator may set M-005
  once batch 7 lands it.

### Homonyms kept apart

- **"Log"** (Q1's U-044): WooCommerce's and BigCommerce's store logs (domain G's CM-OPS-005) are a logger's entries, not
  an audit of admin actions. In CM-TRU-003's note.
- **"Rate limit"** (Q1's U-045): API rate limits on Shopify and Salla (domain F) against WooCommerce's checkout limit;
  bot protection is neither. In CM-TRU-004's note.
- **Bot protection against reCAPTCHA:** Salla's reCAPTCHA verification (SA-S-1715, SA-S-3100) guards buyers' sign-in and
  registration, domain D's CM-CUS-012, not the checkout.
- **"Consent":** customers' marketing consent is domain D's CM-CUS-007; CM-TRU-006 is visitors' privacy and cookie consent.
- **"Complaint"** (Q1's U-040, for batch 7): Salla's complaints platform (منصة الشكاوى, SA-C-178, buyers complaining
  about stores to Salla) is not domain D's CM-SUP-008 (Complaints / إدارة الشكاوى, the merchant handling its own
  customers' complaints, at /manage/complaints). Batch 6 or 7 should search `caps` for complaints before adding one.

### Strained fits

- **SH-C-147** in CM-TRU-008: SH-S-0725 (a Shop feature needs SNI) is also cited in domain E's CM-CHN-002.
- **SH-C-148** in CM-TRU-006: SH-S-0067 (Pixel Manager consents) is also cited in domain D's CM-MKT-009; SH-S-5031, one
  eligibility statement Q1 holds for several routes, is cited in domains D and E for theirs.
- **SH-C-149** in CM-TRU-007: its topic customers/data_request (SH-S-1197) is domain F's CM-API-011, not cited here.
- **SH-C-172** in CM-TRU-009: its restricted-access, appeal and suspension statements are CM-ONB-002's; SH-S-0031 is also
  in domain B's CM-CAT-001.
- **SH-C-174** in CM-ACC-008: SH-S-0304 is also in CM-ONB-001; SH-S-0297 in domain F's CM-PTN-002.
- **SH-C-175** in CM-TRU-010: SH-S-0236 is also in domain B's CM-CAT-001.

### Concerns of other domains read under `also`

- **SA-C-234** (domain G, platform security): its two-factor heading SA-S-5115 is CM-TRU-001's Salla core; G doesn't cite
  it. SA-C-234 lands in G's CM-OPS-002, so G's landing is now strained by it.
- **SA-C-006** (domain C, Store Verification): SA-S-0132 and SA-S-0138, cited as shows in CM-TRU-002 under both SA-C-006's
  and SA-C-232's keys, as batch 4 did for a statement held under two concerns. Its SA-S-0118 is cited in CM-TRU-010 under
  SA-C-231's key only.
- **SH-C-161** (domain F, privacy webhooks) is CM-API-011's; SH-C-160 (protected customer data) and SH-C-042 (customer
  identity providers) weren't needed.

### Rulings, and the pairs left for later batches

Ruled here: U-006 twice (SH-C-007 against SA-C-001 and against SA-C-234, both joined:CM-TRU-001); U-007 (joined:CM-TRU-002,
following the cells for SA-C-006); U-034 (joined:CM-ACC-008); U-036 for SH-C-172 against SA-C-170 (apart: SA-C-170's
held statements are the registration step and the agreement's page, cited in CM-ACC-001, and the usage policy's text
isn't held); U-045 for SH-C-051 against SA-C-201 (apart: scope.tsv gives SA-C-201 domain F).

Left for batch 7 (Salla's TRU concerns):
- **U-035, SH-C-174 against SA-C-232:** SH-C-174 is in CM-ACC-008; if no CM-ACC-008 cell cites an SA-C-232 key, apart.
- **U-036, SH-C-172 against SA-C-232:** CM-TRU-009's Salla cell cites SA-C-232's SA-S-0116 and SA-S-0115, so joined:CM-TRU-009
  by the cells. **SH-C-014 against SA-C-232:** CM-ONB-002 cites SA-S-0115 too, so joined:CM-ONB-002 as batch 4 said.
- **U-007's other side, SH-C-008 against SA-C-232** isn't a candidate pair (U-007 holds SA-C-006 only), but CM-TRU-002
  cites SA-C-232's keys, so landing SA-C-232 elsewhere makes it strained.
- **U-039, SH-C-175 against SA-C-231:** CM-TRU-010's Salla cell cites SA-C-231's SA-S-0160 and SA-S-0118, so
  joined:CM-TRU-010 wherever SA-C-231 lands.
- **U-040, SH-C-172 against SA-C-178:** CM-TRU-009 cites no SA-C-178 key yet; Shopify's report form (SH-S-7258) and
  "Report an issue with a merchant" (SH-I-1374, not cited) are the side to weigh against Salla's complaints platform.
- **U-044, SH-C-012 against SA-C-010:** CM-TRU-003 cites both sides, so joined:CM-TRU-003 once SA-C-010 lands (by
  match:M-005). SA-C-010 will be strained: its export-log statements are cited in domain G's CM-MIG-004.
- **M-059:** SA-C-066 lands in CM-TRU-005 by match. Its cells there and in CM-TRU-006 and CM-TRU-007 already cite it.
- **M-060 (batch 6's SH-C-180, batch 7's SA-C-171):** the merchant as controller (SA-S-0168) and Shopify as controller for
  Enhanced Services (SH-S-0192, cited in CM-TRU-008) bear on data-protection roles. Placing that capability under
  CM-TRU-005 keeps them in one tree.
- U-080 (SH-C-175 against WC-C-091) and M-084's and M-086's WooCommerce concerns are WooCommerce's part's.

### What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/A-anchor --concerns SH-C-007,SH-C-008,SH-C-012,SH-C-051,SH-C-147,SH-C-148,SH-C-149,SH-C-172,SH-C-174,SH-C-175 --areas TRU`:
0 problems, 13 flags.
- *CM-TRU-004 salla none-held, 24 statements match:* reCAPTCHA at buyers' sign-in (SA-S-1715, SA-S-3100, SA-S-3368,
  domain D's CM-CUS-012), the PDPL's protection of data (SA-S-0168, SA-S-0169), payment restrictions and fraud protection
  (قيود الدفع والحماية من الاحتيال, نظام الحماية من الاحتيال: SA-S-2145, SA-S-1971, SA-S-0104, SA-S-5050, domain C), store
  content protection (SA-S-2035), the affiliate and theme-publishing plan lines (SA-S-2144, SA-S-2034) and partners'
  confidentiality (SA-S-5097, SA-S-0029). None blocks bots from the checkout.
- *CM-TRU-006 salla: core rests only on boundary statements:* SA-S-5023 is Salla's help describing the store's own
  registration window, not an API object; Q1 placed it under boundary because the window is where the store meets the
  buyer.
- *CM-TRU-008 salla none-held, 5 statements match:* SA-S-5052 and SA-S-0110 (answered in the cell), SA-S-0168 (the
  controller's obligations), and the flag ai-driven-personalized-product (SA-S-3377, SA-I-2377), which names
  personalization of products and doesn't say whose data or across which stores.
- *SA-S-3182 and SA-S-3365 in CM-ACC-001 and CM-TRU-001:* see below.
- *SA-S-0115 in CM-ONB-002 and CM-TRU-009:* intended, as batch 4 foresaw: the violation is this capability's subject,
  the suspension CM-ONB-002's.
- *SH-C-014 clean in CM-ONB-002, its statements cited in CM-TRU-009:* SH-I-2134, the help section "Resolving terms
  violations", is placed by Q1 in SH-C-014 and SH-C-172; batch 4 doesn't cite it. See below.
- *CM-STF-003, CM-PLN-006, SA-S-5002, SA-S-0089, SA-S-0141, SH-S-0238:* earlier batches', answered there.

### For the coordinator: earlier batches' rows

- **CM-ACC-001's Salla cell (batch 1)** cites the two-factor and biometric flags (SA-S-3182, SA-S-3365) as shows. Their
  subject is CM-TRU-001's, as batch 1 foresaw: drop them from CM-ACC-001 (and its reading), or keep both and the flag.
  CM-ACC-001's note ("Sign-in security ... is the TRU batch's") can now name CM-TRU-001.
- **CM-ACC-008 (batch 1):** its Shopify reading should name the two rows I added (SH-S-0306, SH-S-0307), and its note
  ("Shopify's sanctions concern (SH-C-174) ... the TRU batch's to land") that SH-C-174 has landed there.
- **SH-C-014 (batch 4)** is now strained by SH-I-2134, cited in CM-TRU-009 (S1); or drop SH-I-2134 there if its subject is
  judged the store's state rather than the violation.
- **CM-ONB-002's Salla reading (batch 4)** says SA-C-232 is the TRU batch's to land; CM-TRU-009 now cites SA-S-0115 as core.

### Problems and gaps

- **Salla's usage policy** (سياسة الاستخدام على منصة سلة, SA-I-2613) isn't held as text, so Salla's acceptable-use rules,
  and any sanctions or restricted-country rules (U-035's "what would settle it"), aren't held.
- **Shopify's boundaries:** SH-C-007/boundary, SH-C-008/boundary and SH-C-051/boundary are "searched, not found";
  SH-C-174/where and /boundary are "observation needed" (where the sanctions restriction applies, and its screening
  interface).
- **Salla's privacy and erasure:** only flags are held for data export and account deletion, with no statement of what
  they do; no cookie banner, per-region privacy setting or erasure process is held.
- **Salla's identity verification** apart from store verification isn't held; nor is a Salla statement on bot protection.
- **Makers:** none needed; every placement here rests on the platforms' own pages, routes and APIs.

## The coordinator's corrections after batch 5 (30 October)

- **Salla's two-factor and biometric flags** (SA-S-3182, SA-S-3365) leave CM-ACC-001: they are CM-TRU-001's subject, and batch 5 cites them there. SA-C-001 stays `strained`, its reading naming CM-TRU-001 and G's CM-SRF-001.
- **SH-C-014 is `strained`:** batch 5 cites SH-I-2134 in CM-TRU-009.
- **CM-ACC-008's Shopify reading** names SH-C-174, which lands there, and batch 5's two rows; **CM-ONB-002's Salla reading** names SA-S-0115, now `core` in CM-TRU-009.
- **SA-C-234, G's,** is cited here through SA-S-5115 (two-factor authentication mandatory at sign-in): its landing in G names CM-TRU-001.
- **SH-C-012** is written as Q1's match M-005 once batch 7 lands SA-C-010.


## Batch 6: TRU, Security, privacy, trust and audit (the second of three batches on it)

Concerns: SH-C-176, SH-C-177, SH-C-178, SH-C-179, SH-C-180, SH-C-181, SH-C-182, SH-C-183, SH-C-184, SH-C-196. Result:
9 capabilities (CM-TRU-011 to CM-TRU-019), 10 landings (all in the new capabilities; SH-C-177 and SH-C-178 share
CM-TRU-012), 18 cells (a Shopify and a Salla cell for each, so batch 7 finds them ready), 78 evidence rows (two of them
added to batch 1's CM-ACC-002 Shopify cell), 4 qualities, 14 slot fillers (one on CM-ACC-002), 3 rulings. `caps` was
searched for every new capability (intellectual property, complaint, legal request, controller and processor, hosting
and data location, subprocessor, retention and deletion, PCI and card data, security and legal apps, in English and
Arabic): only domain D's CM-SUP-008 (complaints), G's CM-OPS-001 and CM-OPS-003 (reliability, hosting environment) and
batch 5's CM-TRU-005 and CM-TRU-008 came near, and none is the same thing.

### How I cut, and why

- **CM-TRU-011, intellectual property infringement,** under CM-TRU-009: Shopify's Terms make infringing content a
  violation of its Acceptable Use Policy (SH-S-7260), and give it a report and forms of its own (SH-S-7259, SH-S-7480,
  SH-I-1382). Salla's side is a rule in the App Maker's publishing policy (SA-S-5114, held under SA-C-232, as CM-TRU-009's
  Salla cell is). Salla's store content protection (حماية محتوى المتجر, content-copyright) guards the store's own content,
  domain E's SA-C-090, and stays out.
- **CM-TRU-012, merchants' complaints to the platform about its own services,** for SH-C-177 and SH-C-178: the P2B
  complaint form and internal complaint-handling system, and the form for complaints about Shopify's financial
  products, are each a merchant's complaint to the platform about it (reading). Two concerns in one capability: one
  form each isn't a place enough for two capabilities (my judgment); the reviewer may split them.
- **Data protection, at two levels.** CM-TRU-013 is the platform's data protection terms (privacy policy and DPA, with
  the controller and processor roles), Q1's M-060 for SH-C-180. Its four children are the parts of those terms that
  Shopify gives a place of their own: CM-TRU-014 where data is stored and transferred (Data hosting locations, BCRs),
  CM-TRU-015 subprocessors (its page and notification sign-up), CM-TRU-016 retention after closure, CM-TRU-017 legal
  requests (the Legal Access Request form). The parent rests on Shopify's grouping: each child's statements sit in the
  DPA or the privacy policy (SH-S-0188, SH-S-0189, SH-S-0182, SH-S-7290, SH-S-0185). I didn't put CM-TRU-013 under
  CM-TRU-005, as batch 5 suggested: CM-TRU-005 is the store's customers' data, and the privacy policy and DPA also cover
  the merchant's own data (SH-S-0182, SH-S-0185). The reviewer may judge otherwise; CM-TRU-008 (Enhanced Services) then
  joins the same tree, and SH-S-0192, cited in both, stops crossing trees.
- **CM-TRU-018, payment card data security,** Q1's M-062: Shopify's PCI DSS responsibility and its Level 1
  certification. Following the coordinator: Stripe's P2PE service (SH-S-0089) stays in E's CM-POS-002 only. SH-S-0097
  is the same PCI DSS responsibility stated in the Shopify Payments terms; I cite it here as core, as card data security
  rather than payment processing (reading), so **domain C's part should not cite it as core** for a payments capability.
- **CM-TRU-019, security and legal apps:** Shopify's App Store categories, by their headings only. What the apps do
  isn't stated, so I didn't spread them across CM-TRU-004, CM-TRU-006 or CM-TRU-010.
- **Added to CM-ACC-002 (batch 1):** the EU Terms' contracting entity (SH-S-0207, Shopify International Limited) and
  governing law (SH-S-0211, Ireland, with its slot filler), from SH-C-177.

### Joins on role

None: no Salla concern landed in this batch, and no Shopify concern joined an existing capability.

### Homonyms kept apart

- **"Complaint"** (Q1's U-040): CM-TRU-012 is merchants' complaints about the platform. Salla's complaints platform
  (منصة الشكاوى, SA-C-178) is buyers' complaints about stores with Salla as mediator (SA-S-5087); D's CM-SUP-008 is the
  merchant handling its own customers' complaints; Salla's quality gateway (بوابة الجودة, SA-C-150, domain C) is
  merchants' complaints about shipping companies, escalated to Salla after 5 days. In CM-TRU-012's note.
- **"Hosting":** CM-TRU-014 is where the platform keeps data; G's CM-OPS-003 is the environment a store runs on; Salla's
  hosting of themes and partners' apps (SA-S-0039, SA-S-0037) is neither.
- **"Deleted":** CM-TRU-016 is store data after closure; Salla's deleted orders and products (/orders/trash,
  /products/trash) are items deleted within a live store.
- **"Copyright":** Salla's remove-salla-copyright and content-copyright flags are the storefront's notice and content
  protection, not infringement reports.

### Strained fits

- **SH-C-177** in CM-TRU-012: SH-S-0207 and SH-S-0211 are cited in CM-ACC-002; its Digital Services Act statement
  (SH-S-0656, EU recipients below the VLOP threshold) fits no capability and is left uncited, for the reviewer.
- **SH-C-180** in CM-TRU-013: SH-S-0186 is also in D's CM-CUS-001 (shows), SH-S-0244 in E's CM-CHN-002 (own-service; here
  shows), SH-S-0192 in CM-TRU-008 (under SH-C-147's key). SH-S-0046 is left to CM-TRU-008.
- **SH-C-181** in CM-TRU-014: its pods statements are G's CM-OPS-001 (SH-S-0673, SH-S-0674 cited there). **SH-S-0672**
  (a pod's isolated datastores) is uncited: G's CM-OPS-001 should cite it.
- **SH-C-183** in CM-TRU-016: shop/redact (SH-S-1356) and apps' 30-day deletion (SH-S-0219) are F's CM-API-011.
- **SH-C-184** in CM-TRU-018: SH-S-0089 is E's CM-POS-002.
- **SH-C-196** in CM-TRU-019: the general app statements (SH-S-0755, SH-S-0058, SH-S-7284), cited for every app category.

### Concerns of other domains read

None under `also` was needed. Searching found SA-C-118 and SA-C-119 (C, the consent to share store data with a payment
company), SA-C-150 (C, quality gateway), SA-C-090 (E, content protection) and SA-C-234 (G, TLS); none is cited.

### Rulings, and the pairs left for batch 7

Ruled here: U-043 twice (SH-C-182 against SA-C-118 and against SA-C-119, apart: scope.tsv gives both domain C); U-064
(SH-C-196 against SA-C-210, apart: scope.tsv gives SA-C-210 domain C).

Left for batch 7:
- **M-060, SA-C-171** lands in CM-TRU-013 by match. Its Salla cell already cites SA-C-171's SA-S-2209 (core) and
  SA-S-0029 (shows). The coordinator then writes SH-C-180's join as match:M-060 (it is `single` until then).
- **U-042, SH-C-181 against SA-C-233:** SA-C-233 has no statement, so CM-TRU-014's Salla cell is none-held and no
  capability cites both sides: apart, whatever SA-C-233 lands in (CM-TRU-014 is its subject, by its name).
- **U-040, SH-C-177 and SH-C-178 against SA-C-178:** CM-TRU-012 cites no SA-C-178 key (its reading says why), so apart
  unless batch 7 lands SA-C-178 in CM-TRU-012. With batch 5's SH-C-172 pair (CM-TRU-009), U-040 has three pairs.
- **SA-C-232** (batch 7's) is now cited in CM-TRU-011 too (SA-S-5114), with CM-TRU-009 and CM-TRU-002: wherever it
  lands, the fit follows the cells.
- **SA-C-066** (batch 7's, M-059) is now also cited in CM-TRU-013 (SA-S-0168, the merchant as controller), in another
  tree than CM-TRU-005 unless the reviewer puts CM-TRU-013 under it.
- Q1's M-061 (WC-C-043), M-062 (WC-C-018, WC-C-019) and M-060's WooCommerce side (WC-C-024, WC-C-044) are WooCommerce's
  part's.

### What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/A-anchor --concerns SH-C-176,SH-C-177,SH-C-178,SH-C-179,SH-C-180,SH-C-181,SH-C-182,SH-C-183,SH-C-184,SH-C-196 --areas TRU`:
0 problems, 17 flags. Mine are the none-held Salla cells of CM-TRU-012 and CM-TRU-014 to CM-TRU-019, each with
matches; every cell's reading says what its matches are and why none shows the capability. The other ten flags are
earlier batches' (CM-STF-003, CM-PLN-006, CM-TRU-004, CM-TRU-006, CM-TRU-008, SA-S-5002, SA-S-0089, SA-S-0141,
SA-S-0115, SH-S-0238), answered in their notes.

### For the coordinator: earlier batches' rows

- **CM-ACC-002's Shopify reading (batch 1)** should name the two rows I added (SH-S-0207, SH-S-0211), the EU Terms'
  entity and Irish law; SH-C-002 itself is untouched.
- **Domain G's CM-OPS-001** may add SH-C-181/where/SH-S-0672 (a pod's isolated datastores), which I leave to it.

### Problems and gaps

- **Salla's privacy policy isn't held as text** (SA-C-171/decides, /boundary, /reason and all of SA-C-233 are 'page not
  read'): Salla's own controller or processor role, where it stores data, its processors, its retention and its answer
  to legal requests aren't stated, so CM-TRU-014 to CM-TRU-017 are none-held for Salla on that gap, not on a search.
- **Shopify's gaps:** SH-C-176/reason, SH-C-177/reason, SH-C-178/decides, /responsible and /reason, SH-C-179/responsible,
  SH-C-180/where and /reason, SH-C-182/reason, SH-C-183/where, SH-C-184/where, /boundary and /reason, SH-C-196/reason are
  'searched, not found'.
- **The DSA statement SH-S-0656** has no capability: a disclosure of the platform's own regulatory status. The reviewer
  may want a home for the platform's regulatory notices, or none.
- **Makers:** none needed; every placement rests on Shopify's own legal pages, forms and App Store categories.

## The coordinator's corrections after batch 6 (30 October)

- **CM-ACC-002's Shopify reading** names batch 6's two rows (SH-S-0207, SH-S-0211).
- **SH-S-0672** is cited in G's CM-OPS-001, which also left it to A.
- **For domain C:** SH-S-0097, Shopify's PCI responsibility under the Payments terms, is `core` in CM-TRU-018; C's parts cite it as `shows` unless a C cell rests on it.

## Batch 7: TRU, Security, privacy, trust and audit (the last of three batches on it, and the part's last)

Concerns: SA-C-010, SA-C-066, SA-C-171, SA-C-178, SA-C-180, SA-C-231, SA-C-232, SA-C-233. Result: 1 capability
(CM-TRU-020), 8 landings (7 in existing capabilities, SA-C-178 in the new one), 2 cells (CM-TRU-020's), 10 evidence rows
(4 in CM-TRU-020; 1 added to CM-TRU-009's Salla cell, 4 to CM-TRU-010's, 1 to batch 3's CM-PLN-001 Salla cell), 1 slot
filler, 10 rulings. `caps` was searched for complaints and mediation (complaint, شكوى, شكاوى, الشكاوى, الشكاوي, dispute,
نزاع, mediat, وسيط), for licences and partners, for banned customers and cash on delivery, for app suspension and the
app store, and for store policies and the privacy page.

### How I cut, and why

- **SA-C-010 in CM-TRU-003,** by Q1's M-005: CM-TRU-003's Salla cell already cites its audit rows; its export log is
  domain G's CM-MIG-004.
- **SA-C-066 in CM-TRU-005,** by Q1's M-059: it is coarser than Shopify's SH-C-148 (CM-TRU-006) and SH-C-149 (CM-TRU-007),
  so it lands in their parent, as batch 5 cut it. Every statement but SA-S-5022 was already cited. SA-S-5022 (the privacy
  page as an information page) is domain E's CM-CNT-008, store policies: I leave it to E, uncited.
- **SA-C-171 in CM-TRU-013,** by Q1's M-060. Both its statements were already cited there (batch 6).
- **SA-C-178, Salla's complaints platform, in a new capability, CM-TRU-020:** the platform's handling of buyers'
  complaints about stores, as mediator between buyer and merchant. The customer opens a complaint on Salla's complaints
  system page, Salla's team reviews it first, Salla mediates, and only the customer closes it (SA-S-5085, SA-S-5088,
  SA-S-5087, SA-S-5086). It isn't CM-TRU-012, merchants' complaints about the platform, and it isn't CM-TRU-009, the
  platform's action on violations, because neither one mediates between a buyer and a merchant. My message says it isn't D's CM-SUP-008. `caps` does
  find CM-SUP-008, "Customer complaints about the store", though. D-anchor built it from Salla's merchant-side
  Complaints page (/manage/complaints, complaint_management), and **D-zid then landed Zid Assurance there**: Zid
  handles complaints against stores (ZD-S-0998, ZD-S-0935, own-service). That is the same role as Salla's mediation. I followed the
  message and kept SA-C-178 in A, which is where scope.tsv puts it, with D under its also. Under the brief's "One thing, one domain", the coordinator may
  judge CM-TRU-020 the same thing as CM-SUP-008. In that case SA-C-178 lands as `moved:D` and CM-TRU-020's rows go.
- **SA-C-180 in CM-PLN-001, `single`, strained.** Q1 holds only the page's URL (SA-S-2213), with its content "not
  reached". As context, not cited: observed-sa at b0bd0b16 holds the page's text
  (structures/salla/com-policies/policies-nd96/text.txt). It is the terms of Salla's Saudi National Day 96 campaign:
  discounts on annual and two-year Plus and Pro subscriptions, with a five-orders guarantee for new subscribers. That is
  a reading for the plans capability, not for TRU. The checker requires the cell to cite one of the concern's statements, so I
  cite SA-S-2213 as `shows` in CM-PLN-001's Salla cell, and its `why` marks the reading. It supports no placement.
- **SA-C-231 in CM-TRU-010,** on role with SH-C-175, as batch 5 foresaw (Q1's U-039). I added to the Salla cell:
  - SA-S-5147 as `core`, a reading: Salla's own store data, which the merchant updates and which hold the Business
    platform certificate and the customer-service channels that the e-commerce laws require (SA-S-0118, SA-S-0160). This
    is the counterpart of Shopify's Disclosures metafield (SH-S-7257), which is `core` there;
  - SA-S-0131, SA-S-0136 and SA-S-0142 as `shows`: store verification's regulatory reason, the UAE trade licences it
    accepts, and the UAE legal entity it needs.

  Its partners' licences belong to F's partner capabilities, so I don't cite them here.
- **SA-C-232 in CM-TRU-009,** on role with SH-C-172 (Q1's U-036). I added SA-S-3533 to the Salla cell as `core`: the
  dashboard app whose paths include manage/violation, as the other batches cite it for their paths. SA-C-232 holds no
  sanctions term (Q1's U-035). I left these uncited:
  - SA-S-0028, Salla's suspension of apps: this is F's CM-APP-002, the app store's review of apps;
  - SA-S-0110, cash on delivery hidden for customers banned in other Salla stores: it bears on CM-TRU-008, whose cell is
    batch 5's (see "For the coordinator").
- **SA-C-233 in CM-TRU-014,** by its name: it holds no statement. Its fit is clean, because nothing of it is cited
  elsewhere. The cell stays none-held on Q1's gap.

### Joins on role

- **CM-TRU-009:** SA-C-232's violations page against Shopify's AUP and its report (SA-S-0116, SA-S-0115; SH-S-7258,
  SH-S-0166).
- **CM-TRU-010:** SA-C-231's e-commerce certificate and customer-service information against Shopify's Your
  Responsibilities (SA-S-0118, SA-S-0160; SH-S-0236, SH-S-0012).

These are the joins batch 5 wrote for the Shopify side. Batch 7 adds the Salla landings.

### Homonyms kept apart

- **"Complaint"** (Q1's U-040) has four meanings, each in CM-TRU-020's note:
  - CM-TRU-020: buyers' complaints about stores, with the platform as mediator;
  - CM-TRU-012: merchants' complaints to the platform;
  - D's CM-SUP-008: the store's complaints record that the merchant manages;
  - C's quality gateway (SA-C-150): merchants' complaints about shipping companies.

  Shopify's disputes are payment chargebacks.
- **"Log"** (Q1's U-044): WooCommerce's store logs (WC-C-037) are WooCommerce's part's. The export log (SA-C-010's) is
  G's CM-MIG-004. The two are not the same thing.
- **"Policies":** Salla's /policies/nd96 is a campaign's terms (CM-PLN-001). Shopify's Policies (SH-C-034) is the
  store's own policy pages (E's CM-CNT-008).

### Strained fits

- **SA-C-010** in CM-TRU-003: its export log rows are cited in G's CM-MIG-004.
- **SA-C-066** in CM-TRU-005: SA-S-0168 is cited in CM-TRU-013, another tree, and SA-S-5023 in D's CM-CUS-010. SA-S-5022
  is left to E's CM-CNT-008.
- **SA-C-180** in CM-PLN-001: nothing cited shows it, because the page's text isn't held.
- **SA-C-231** in CM-TRU-010:
  - SA-S-0035 and SA-S-0036 are cited in F's CM-PTN-002, and SA-S-0142 in CM-ACC-004 (under SA-C-006's key);
  - SA-S-5113 (the Mawthooq licence for influencer partners) and SA-S-5112 (the store-growth programme's partners'
    licences) are left uncited for F's CM-PTN-002 and CM-PTN-006.
- **SA-C-232** in CM-TRU-009:
  - SA-S-0115 is also cited in CM-ONB-002, SA-S-0132 and SA-S-0138 in CM-TRU-002, and SA-S-0173 in F's CM-API-005;
  - SA-S-3533 is cited in many capabilities, for their paths;
  - SA-S-0028 and SA-S-0110 are left uncited (see above).
- SA-C-171, SA-C-178 and SA-C-233 are clean.

### Concerns of other domains read

- None was cited.
- I read D's CM-SUP-008 (SA-C-179's statements and its Zid cell) to rule on SA-C-178.
- scope.tsv names D under SA-C-178's also, so D's CM-SUP-008 may cite SA-C-178's statements.

### Rulings, and the matches

**Rulings** (10 rows):

| Candidate | Pair | Ruling | Basis |
|---|---|---|---|
| U-035 | SH-C-174 against SA-C-232 | apart | No capability cites both sides. |
| U-036 | SH-C-172 against SA-C-232 | joined:CM-TRU-009 | |
| U-036 | SH-C-014 against SA-C-232 | joined:CM-ONB-002 | Batch 4's SA-S-0115. |
| U-039 | SH-C-175 against SA-C-231 | joined:CM-TRU-010 | |
| U-040 | SH-C-172 against SA-C-178 | apart | SA-C-178 lands in CM-TRU-020, whose Shopify cell is none-held. |
| U-040 | SH-C-177 against SA-C-178 | apart | Same. |
| U-040 | SH-C-178 against SA-C-178 | apart | Same. |
| U-042 | SH-C-181 against SA-C-233 | apart | SA-C-233 has no statement. |
| U-044 | SH-C-012 against SA-C-010 | joined:CM-TRU-003 | |
| U-012 | SH-C-034 against SA-C-066 | apart | scope.tsv gives SH-C-034 domain E, and no capability of A cites it. |

**Matches:** SA-C-010 is written as match:M-005, SA-C-066 as M-059 and SA-C-171 as M-060. Each sits with its match's
Shopify concerns, in the same capability or in its children.

If CM-SUP-008 takes SA-C-178, U-040's rulings stay apart. CM-SUP-008's Shopify cell is none-held.

### What the checker flagged

The whole part: `python3 -I method/check_class_part.py studies/class-model/parts/A-anchor`.

- **First run, 1 problem:** no CM-PLN-001 Salla evidence cited SA-C-180. I fixed it with the `shows` row above.
- **Final, 0 problems and 19 flags.**

Mine:
- *CM-TRU-020 shopify none-held, 10 statements match:* the cell's reading answers it. The matches are merchants'
  complaints to Shopify (CM-TRU-012), the AUP's enforcement principle, a Balance card rule, an identity remediation
  endpoint, and Report an issue with a merchant, which is held by its title only.
- *CM-TRU-010 salla: core rests only on boundary statements:* my row SA-S-5147. It isn't an API object. It is Salla's
  dashboard text (basic_settings.main_store_data.description) listing the store data the merchant updates from the theme
  editor page, the Business platform certificate among them. Q1 placed it under boundary, so it shows Salla's own
  setting (reading).

Earlier batches', which my rows bear on:
- *CM-TRU-008 salla none-held, 5 statements match:* SA-S-0110 is SA-C-232's (see "For the coordinator").
- *CM-TRU-012 salla none-held:* the matches include SA-S-3533 and the quality gateway, which batch 6's reading answers.
  SA-C-178 is now in CM-TRU-020.
- *SA-S-0115 in CM-ONB-002 and CM-TRU-009:* intended, as batch 5 says.

The other flags were answered by their batches:
- CM-STF-003, CM-PLN-006, CM-TRU-004, CM-TRU-006, CM-TRU-014 to CM-TRU-019;
- SA-S-5002, SA-S-0089, SA-S-0141, SH-S-0238;
- the flag "core rests only on boundary statements" on CM-TRU-006's Salla cell (SA-S-5023, batch 5).

No problem was found on earlier batches' rows.

### For the coordinator: earlier batches' rows

- **CM-TRU-008's Salla cell (batch 5)** is none-held. SA-C-232/decides/SA-S-0110 is the setting
  disable_cod_for_banned_customers: cash on delivery hidden from customers banned in other Salla stores. My reading:
  Salla uses other merchants' data in this store's checkout, under the merchant's setting. That is CM-TRU-008's role, the
  counterpart of Shopify's Enhanced Services. I'd make the cell statements, with SA-S-0110 as `core` (reading). Batch 5
  set it aside as "a feature's input", and the cell's row is batch 5's, so I left it uncited.
- **The Salla readings of these cells should name my rows, or the batch 7 landings:**
  - CM-TRU-009 names SA-S-3533; SA-C-232 has landed, and SA-S-0028 is left to F;
  - CM-TRU-010 names SA-S-5147, SA-S-0131, SA-S-0136 and SA-S-0142, and the new slot filler; SA-C-231 has landed;
  - CM-TRU-003, CM-TRU-005 and CM-TRU-013 each say "batch 7's to land": SA-C-010, SA-C-066 and SA-C-171 have now landed;
  - CM-PLN-001 (batch 3) names SA-S-2213 (`shows`) and SA-C-180's landing.
- **The Shopify landings' joins:** SH-C-012 becomes match:M-005, and SH-C-180 becomes match:M-060 (each is
  `terms`/`single` until now).
- **CM-TRU-020 against D's CM-SUP-008:** decide whether they are one thing (see "How I cut").
- **For other domains:**
  - E's CM-CNT-008 may cite SA-C-066/where/SA-S-5022 with a reason, since SA-C-066 names only D;
  - F may cite SA-S-0028 (CM-APP-002), SA-S-5113 and SA-S-5112 (CM-PTN-002, CM-PTN-006) with a reason;
  - SA-S-5147's list of store data is also CM-ACC-006's subject (store details), where it is uncited.

### Problems and gaps

- **SA-C-180:** Q1's concern map holds none of /policies/nd96's text, although observed-sa holds the page. The plan
  campaign's terms need Q1 to place its statements before any cell can rest on them.
- **Salla's privacy policy** (SA-C-171, SA-C-233) and its usage policy (SA-I-2613) aren't held as text, so CM-TRU-014 to
  CM-TRU-017 and the sanctions side of U-035 stay unstated for Salla.
- **SA-C-178/reason** is "page not read". Whether Salla's complaints platform has a dashboard or API side, apart from
  D's /manage/complaints, isn't stated.
- **Makers:** none needed. Every placement rests on Salla's own pages, settings and help.

## The coordinator's corrections after batch 7 (30 October)

- **CM-TRU-020 stays.** It is the platform as mediator between a buyer and a store (Salla's complaints platform), not D's CM-SUP-008, the store's own complaints record, whose Salla cell cites SA-C-179's statements, not SA-C-178's. Zid Assurance, Zid handling complaints against stores itself, is the same role: ZD-C-111 now names A under `also`, for A's Zid part to cite it here.
- **CM-TRU-008's Salla cell holds a statement:** SA-S-0110, cash on delivery hidden from customers banned in Salla's other stores, `core`, a reading. SA-S-5052 is C's lead.
- **SH-C-012 and SH-C-180** are written as Q1's matches M-005 and M-060. The Salla readings of CM-TRU-003, -005, -009, -010, -013 and CM-PLN-001 name batch 7's rows.
- **The leads to other domains are cited there:** SA-S-5022 in E's CM-CNT-008; SA-S-0028, SA-S-5112 and SA-S-5113 in F; SA-S-5147 in CM-ACC-006 here.
- **The part is complete:** 43 capabilities. A's WooCommerce, Zid and BigCommerce parts follow.

- **SA-S-5052** (Salla's tag for a customer who isn't serious, from its anti-fraud analysis across its stores) is cited in CM-TRU-008's Salla cell as `core`, a reading, its concern SA-C-122 now naming A (the coordinator, after C-anchor batch 7).
