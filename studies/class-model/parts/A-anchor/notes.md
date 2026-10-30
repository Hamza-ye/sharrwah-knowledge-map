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

