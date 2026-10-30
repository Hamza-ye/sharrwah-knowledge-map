# A-zid: notes

Domain A, Merchant and platform: Zid mapped onto the model of A-anchor, A-woocommerce and A-backfill-woocommerce. The part
runs in two batches. Read through `class_slice.py` only: `seed`, `model --areas`, `concerns --where`, `statements`, `gaps`,
`matches`, `key`, `search`, `caps` and `candidates`. Searches are in English and Arabic, singular and plural, with and
without ال. Every placement below is a reading of the statements cited. Nothing outside the concern map is cited.

## Batch 1: ACC, STF, PLN and ONB

Concerns: ZD-C-030, ZD-C-031, ZD-C-032, ZD-C-035, ZD-C-077, ZD-C-094, ZD-C-020, ZD-C-021, ZD-C-026 and ZD-C-114. Zid's
cell is written for all 27 capabilities of the four areas (11 ACC, 5 STF, 7 PLN, 4 ONB): 18 cite statements, 9 are
`none-held` (CM-ACC-003, CM-ACC-005, CM-ACC-009, CM-ACC-010, CM-ACC-011, CM-ONB-004, CM-PLN-003, CM-STF-004,
CM-STF-005). No capability is added.

### How the concerns landed

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| ZD-C-030 Zid's contracting entity and governing law | CM-ACC-002 | role | clean |
| ZD-C-031 Zid Egypt | CM-ACC-002 | role | strained |
| ZD-C-032 Countries Zid serves | CM-ACC-008 | terms | clean |
| ZD-C-035 Store business data and verification | CM-ACC-004 | role | clean |
| ZD-C-077 Store account and profile | CM-ACC-001 | terms | strained |
| ZD-C-094 Team members and permissions | CM-STF-001 | role | clean |
| ZD-C-020 Subscription plans and fees | CM-PLN-001 | terms | strained |
| ZD-C-021 Purchases from Zid and their payment processing | CM-PLN-005 | role | clean |
| ZD-C-026 Value added services (VAS) | CM-PLN-004 | role | strained |
| ZD-C-114 Merchant support | CM-ONB-003 | terms | clean |

All ten joined existing capabilities; none made a new one; none moved.

### Grains and cuts

- **ZD-C-077 at CM-ACC-001, strained.** Zid's concern holds both the user's account (Account > Me, account settings:
  email and password) and the store's own record (Account > Store, "the store's core details", third_store_details_read
  and _write, manage.store.settings). The anchor cuts these apart (CM-ACC-001 account, CM-ACC-006 store details), so the
  store's statements are cited in CM-ACC-006 and the concern lands in the account, its name's first subject.
- **ZD-C-031 Zid Egypt at CM-ACC-002, strained.** Zid Egypt has its own commercial registration, tax ID and address. No
  statement says it is the party merchants in Egypt contract with (Q1's gap), so the fit to "contracting party" is a
  reading; its expansion statements are cited in CM-ACC-008. The reviewer may prefer CM-ACC-008.
- **ZD-C-026 VAS at CM-PLN-004, strained.** VAS has no place of its own beyond a section of the Terms (ZD-I-0421), so by
  the dry run's convention it does not become a capability. Its statements are about Zid's charges (prices revised after
  notice, refunds by ticket), so it lands in platform billing. Its refund statement ZD-S-0718 names the subcategory
  "refund of a new or current package"; Q1's note on it says it is where VAS refunds are requested, so it is cited in
  CM-PLN-004, not in CM-PLN-001, where Salla's plan refunds are. If the reviewer reads it as a plan refund, it moves to
  CM-PLN-001.
- **ZD-C-020 at CM-PLN-001, strained,** because its fee clauses are cited in CM-PLN-004 and its VAT clause in CM-PLN-007.
- **ZD-C-035 at CM-ACC-004.** Zid's activity type (نوع النشاط: فرد، مؤسسة، شركة، جمعية خيرية) holds the business entity's
  role. The Saudi Business Center verification (ZD-S-0752) and the KYC endpoint (ZD-S-0757) are the business's data and
  are cited here, not in CM-TRU-002, whose subject is the identity of the people behind the store.

### Joins on role

- ZD-C-030 and ZD-C-031: the companies Zid's Terms name, with Shopify's Contracting Party and Salla's owning company.
- ZD-C-035: Zid's activity type with Shopify's business entity (SH-S-0248) and Salla's entity type (SA-S-0133).
- ZD-C-094: Zid's team (فريق العمل) with Shopify's Users and Salla's Staff members.
- ZD-C-021: purchases from Zid through a third-party processor with Shopify's billing payment methods and Salla's store
  balance paying the plan.
- ZD-C-026: VAS as one of the platform's charges (above).
- Cells, not landings: CM-ACC-007 (Zid's temporary closure of the store with Salla's maintenance mode) and CM-STF-003
  (Zid's team groups with Shopify's Custom user groups, on the name only, since no statement defines a team group).

### Homonyms

None new. Two words to watch: Zid's فرع / branches are inventory locations (domain B), not stores (CM-ACC-003 stays
`none-held`); and Zid's package (باقة) is its plan, as in "refund of a new or current package".

### The two leads from E-zid (ZD-C-033)

ZD-C-033 names A under `also` in scope.tsv (the coordinator's correction, 30 October).
- ZD-S-0746, changing the store's country in its settings with the wallet balance zeroed first, is cited in CM-ACC-006
  (`core`).
- ZD-S-0747, "set your location or your stock's location", is cited in **CM-ONB-001**, not CM-ACC-006 or B's CM-INV-005:
  its citation's context is the registration stage (مرحلة التسجيل) of the help article on creating a store for GCC users
  (https://help.zid.sa/gcc-merchants/), so it is the location given when the store is created, as Shopify's "I'm
  located in:". The context is read, not cited. B's CM-INV-005 is not cited.

### Concerns read under `also`

- ZD-C-017, Zid Wallet (domain C, A under also): cited in CM-PLN-006 (the wallet) and CM-PLN-005 (the wallet pays
  Zid's services and plans; Zid deducts its dues from it). **For the coordinator:** CM-PLN-006 is the same thing, a prepaid
  balance with the platform, topped up, spent on its services and withdrawn (Salla's Store balance and Wallet). By "one
  thing, one domain", ZD-C-017 belongs here; when domain C maps Zid it should land it as `moved:A`, or the coordinator
  moves it, rather than cite these statements as `core` in C.
- ZD-C-033 (domain E, A under also): above.
- ZD-C-022 (domain F), ZD-C-037 (C), ZD-C-039 (E), ZD-C-096 (E), ZD-C-111 (D): read; nothing cited in these areas.

### What the checker flagged, answered

- **evidence.tsv line 36, ZD-S-0970 (ZD-C-104, domain C, also E, not A).** Cited in CM-ACC-007 because it is the only
  statement held that takes the store offline for a time ("إغلاق المتجر بشكل كلي مؤقتاً", from Settings > Store > working
  hours), and no capability of any domain holds closing the store (`caps`: working hours; أوقات العمل; close the store;
  إغلاق المتجر; store closed). If domain C's Zid part lands ZD-C-104 in a working-hours capability and cites ZD-S-0970 as
  `core`, the merge flags it in two domains; the reviewer decides which keeps it. Q1's gap ZD-C-104/decides is
  "observation needed".
- **`none-held` cells whose terms match statements** (CM-ACC-003, CM-ACC-005, CM-ACC-009, CM-ACC-010, CM-ACC-011,
  CM-ONB-004, CM-PLN-003, CM-STF-004, CM-STF-005): each match was read; the cell's reading names the ones that come
  nearest and why they are not the capability. In short: CM-ACC-003, store-wide clauses and inventory branches;
  CM-ACC-005, sanctioned and public entities, service providers, the account API; CM-ACC-009, services needing an activated
  store (cited in CM-ONB-002) and unrelated "activated" settings; CM-ACC-010, app OAuth and embedded apps (F), payment
  linking (C); CM-ACC-011, an invoice "kept as is" (ZD-S-1009); CM-ONB-004, a payment provider's onboarding (C) and app
  setup (F); CM-PLN-003, Zid Pay's transaction fees and commission (ZD-C-006, domain C, not naming A) and affiliate
  commission (D); CM-STF-004, customer targeting (D) and stated aims; CM-STF-005, "you can reach X from" phrases and a
  partner's access through app scopes (F).

### Names (proposals for the coordinator)

- CM-ACC-004: add Zid's activity type (نوع النشاط, بيانات المتجر).
- CM-ACC-007: Zid gives no maintenance mode; if the reviewer keeps ZD-S-0970 here, the name could read "Maintenance mode
  or temporary closure of the store", with Zid's إغلاق المتجر مؤقتاً.
- CM-STF-001: add Zid's Team (فريق العمل, Add Team Members); CM-STF-003: add Zid's team groups (مجموعات الفريق).
- CM-ACC-008: add Zid's "ZID is available in" (زد متاحة في).

### Gaps that bear on the cells

- No billing page or list of Zid's bills is held (CM-PLN-004 rests on the Terms and the refund ticket).
- The third-party processor of purchases from Zid is not named (ZD-C-021/responsible), so CM-PLN-005 has no slot filler.
- No statement of plan renewal, contract term or freeze (CM-PLN-002).
- No store statuses beyond "activated" (CM-ONB-002); no help centre or academy (CM-ONB-003).
- No statement names the store owner as a role, or a change of owner (CM-ACC-001).

### Rulings

None: Q1 never matched Zid, so no unclear candidate holds a Zid concern (`matches` confirms). `rulings.tsv` holds its
header only.

### For batch 2 (area TRU)

- Your concerns are the rest of Zid's domain A: ZD-C-036, ZD-C-038, ZD-C-040, ZD-C-041, ZD-C-042 and ZD-C-095. Write
  Zid's cell for every TRU capability, and run the checker on the whole part without options.
- Statements of batch 1's concerns that bear on TRU, already cited here: ZD-S-0902 (the merchant protects its account,
  CM-ACC-001, `shows`); ZD-S-0752 and ZD-S-0757 (business verification and KYC, CM-ACC-004); ZD-S-0653 (no wallet
  withdrawal before the account's verification, CM-PLN-006). Citing any of them in TRU would make the landing that holds
  it strained by another tree: say so in your notes for the coordinator rather than avoid the citation.
- Leads: Nafath (ZD-C-038, the store owner's identity, ZD-S-0775, ZD-S-0778) for CM-TRU-002; Security Settings (ZD-C-095,
  ZD-S-0944, ZD-S-0945) for CM-TRU-001; licences of regulated goods (ZD-S-0761, ZD-C-036) for CM-TRU-010; Zid Pay's
  prohibited activities (ZD-C-037, domain C, A under also) for CM-TRU-009; Zid Assurance (ZD-C-111, domain D, A under
  also) where a TRU capability holds it.
- Files: append to every file; `capabilities.tsv` and `rulings.tsv` hold their headers only.

## The coordinator's corrections after batch 1 (30 October)

- **ZD-C-017, Zid's wallet, lands here,** in CM-PLN-006, moved from domain C: it is the merchant's prepaid balance with the platform, and batch 1 cites all its statements in CM-PLN-006 and -005. scope.tsv now gives it domain A, with C under `also`.
- **ZD-C-104 names A under `also`,** for ZD-S-0970 (closing the store temporarily), cited in CM-ACC-007.


## Batch 2: TRU

Concerns: ZD-C-036, ZD-C-038, ZD-C-040, ZD-C-041, ZD-C-042 and ZD-C-095. Zid's cell is written for all 21 capabilities of
TRU: 12 cite statements, 9 are `none-held` (CM-TRU-003, -004, -006, -007, -008, -011, -018, -019, -021). No capability is
added. With batch 1, Zid has a cell for all 48 capabilities of domain A (11 ACC, 5 STF, 7 PLN, 4 ONB, 21 TRU).

### How the concerns landed

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| ZD-C-095 Security settings (اعدادات الامان) | CM-TRU-001 | terms | clean |
| ZD-C-038 Nafath identity verification | CM-TRU-002 | role | clean |
| ZD-C-036 E-commerce store regulations (ضوابط المتجر الإلكتروني) | CM-TRU-010 | terms | clean |
| ZD-C-040 Privacy and personal data | CM-TRU-013 | terms | clean |
| ZD-C-041 Cross-border data transfer | CM-TRU-014 | terms | clean |
| ZD-C-042 AI data processing | CM-TRU-015 | role | strained |

All six joined existing capabilities; none made a new one; none moved.

### Grains and cuts

- **ZD-C-040 across CM-TRU-013 and its children.** The Privacy Policy's clauses are cited by subject: processor role,
  DPO, consent and partners in CM-TRU-013; service providers (ZD-S-0791) in CM-TRU-015; retention (ZD-S-0786) in
  CM-TRU-016; disclosure to public entities (ZD-S-0792) in CM-TRU-017. All are one tree under CM-TRU-013, so the fit is clean.
- **ZD-C-042 at CM-TRU-015, strained.** Its section has no place of its own beyond the Privacy Policy, so by the dry run's
  convention it isn't a capability. It names one processor, Google Cloud Vertex AI, for one feature, Zid Agent; it gives
  no list of subprocessors and no notice of changes. ZD-S-0717 is also held under ZD-C-025 (Zid Agent, domain F,
  CM-AIA-002), which this part doesn't cite. `caps` (AI; الذكاء الاصطناعي; Vertex; assistant; data processor) finds no
  capability for AI data processing as such. The reviewer may prefer CM-TRU-013 for its consent and control clauses.
- **ZD-C-038 at CM-TRU-002.** Every statement is scoped by its words to Zid Pay's activation (the store owner passes
  Nafath to receive electronic payments). The subject is the owner's identity, so it is A's CM-TRU-002, as Shopify's
  identity verification for Capital and Credit is; not a payment capability of C.
- **ZD-C-036 at CM-TRU-010.** Its footer statement (ZD-S-0763: the CR number, email and phone shown at the foot of the
  store page) is the one built-in behaviour, `core`; the rules are `shows`, as Salla's rules are. Its statement ZD-S-0762
  (Zid not a party between consumer and merchant) also bears on CM-TRU-020, but it makes the merchant responsible, so it
  stays `shows` in CM-TRU-010.
- **ZD-C-095 at CM-TRU-001.** The security levels (ZD-S-0945) are sign-in security of the same settings page; the session
  timeout is recorded as a quality.

### Joins on role

- ZD-C-038: Zid's Nafath check of the store owner with Salla's Absher check (SA-S-0132) and Shopify's identity
  verification (SH-S-0264).
- ZD-C-042: Google Cloud as Zid Agent's processor with Shopify's third-party subprocessors (SH-S-0184, SH-S-0195).
- Cells, not landings: CM-TRU-009 (Zid Pay's prohibited activities with Shopify's AUP and Salla's violations, scoped to Zid
  Pay); CM-TRU-012 (a merchant's objection by ticket, ZD-S-1077, with Shopify's complaint-handling system, a reading: the
  statement doesn't say what the objection is against); CM-TRU-020 (Zid Assurance's complaint handling with Salla's
  complaints platform).

### Homonyms

None new. Watch: Zid's توثيق الحساب (account verification before a wallet withdrawal, ZD-S-0653) and Zid Pay's KYC
documents (ZD-S-0659) are not cited in CM-TRU-002, because neither says a person is verified, and Zid's KYC endpoint reads
the commercial registration and business details (ZD-S-0757, CM-ACC-004). ZD-S-0613 (ZD-C-011, domain C) is a payment
provider's own Nafath check, not Zid's.

### Zid Assurance and complaints: which cell (for the coordinator)

CM-TRU-020's Zid cell cites ZD-C-111's ZD-S-0998 ("we … handle any complaints or inquiries", `core`), ZD-S-0996 (the
setting, `core`), ZD-S-0997 and ZD-S-1000 (`shows`), and ZD-C-092's ZD-S-0935 (a complaint against a store through Zid's
link or support, `core`) and ZD-I-0413 (the legal page Zid Stores' Customer Complaints, `shows`). D-zid's CM-SUP-008 cites
all six, ZD-S-0998 and ZD-S-0935 as `own-service`. **They belong in CM-TRU-020.** CM-SUP-008 is the store's own management
of its customers' complaints (Salla إدارة الشكاوى); what these statements show is Zid itself taking buyers' complaints
about stores, which is the platform as mediator, CM-TRU-020's role (Salla's SA-S-5087). Counted once, Zid's CM-SUP-008
would keep only what is the merchant's (none of these statements is), so it would fall to `none-held` or to Zid Assurance's
WhatsApp order updates (ZD-S-0999), which D may place elsewhere. ZD-C-092 doesn't name A under `also` in scope.tsv; if the
coordinator keeps ZD-S-0935 and ZD-I-0413 here, ZD-C-092's row should name A.

### Concerns read under `also`

- ZD-C-037 (domain C), Zid Pay's prohibited activities: cited in CM-TRU-009 (ZD-S-0765, -0769, -0770, -0772 `core`; the
  lists `shows`). **For the coordinator:** when domain C maps Zid, these shouldn't also be `core` in a C capability; no
  capability of C holds prohibited businesses (`caps`: prohibited; restricted; محظورة; sanctions; عقوبات).
- ZD-C-039 (domain E): ZD-S-0781 and ZD-S-0782 cited in CM-TRU-005 (`shows`).
- ZD-C-111 (domain D): above.
- ZD-C-017, ZD-C-022, ZD-C-033, ZD-C-096, ZD-C-104: read; nothing cited in TRU.

### Statements of other domains not cited

- ZD-S-0933 (ZD-C-091, domain D, not naming A): Zid collects the merchant's customers' information as the merchant
  directs; CM-TRU-013 doesn't need it, since ZD-S-0788 says the same.
- ZD-S-0612 (ZD-C-011, domain C): Zid not responsible for stores' or carriers' performance; bears on CM-TRU-010, not cited.
- ZD-S-0987 (ZD-C-109, Mazeed, domain E): a rule on prohibited activities for Mazeed only.

### What the checker flagged, answered

- **evidence.tsv lines 142 and 146, ZD-S-0935 and ZD-I-0413 (ZD-C-092, domain D, not naming A):** cited in CM-TRU-020,
  because they are the only statements held of Zid taking a complaint against a store; see above.
- **cells.tsv line 38, CM-TRU-010, `core` on a boundary statement only:** ZD-S-0763 says the CR number, email and phone
  "ستظهر للعملاء في أسفل صفحة المتجر": Zid's storefront shows them, a built-in behaviour, not an API object.
- **cells.tsv line 45, CM-TRU-017, `core` on a boundary statement only:** ZD-S-0792 is the Privacy Policy's rule for when
  Zid itself discloses data to a public entity, Zid's own action.
- **ZD-S-0902 in CM-ACC-001 and CM-TRU-001:** the merchant's duty to protect its account with a strong password is shown in
  both, as Shopify's SH-S-0230 is in CM-TRU-001. ZD-C-077 is already `strained`; **for the coordinator,** its reading
  should also name CM-TRU-001.
- **ZD-S-1077 in CM-ONB-003 and CM-TRU-012, and landings line 11, ZD-C-114 `clean`:** batch 1's row. The ticket is
  Zid's support channel (CM-ONB-003) and the one place held where a merchant files an objection to Zid (CM-TRU-012).
  **For the coordinator:** ZD-C-114 should be `strained`, its reading naming CM-TRU-012; or, if the reviewer reads the
  objection as support only, the CM-TRU-012 cell goes to `none-held`.
- **`none-held` cells whose terms match statements** (CM-TRU-003, -004, -006, -007, -008, -011, -018, -019, -021): each
  match was read; the cell's reading names them and why they aren't the capability.
- **One citation dropped, by the convention on placed inventory entries:** ZD-I-0406 (the Terms & Conditions page) was
  first cited in CM-TRU-010 and taken out, because statements cover the cell (ZD-S-0759 is the regulations' own where);
  the checker had shown it is placed in ZD-C-030 and ZD-C-021 too, so it would have marked batch 1's ZD-C-030 and ZD-C-021
  `strained` on the whole Terms page. The reviewer may restore it; if so, those two landings become strained.

### Names (proposals for the coordinator)

- CM-TRU-001: add Zid's Security Settings (اعدادات الامان, التحقق بخطوتين).
- CM-TRU-002: add Zid's Nafath (التحقق من نفاذ).
- CM-TRU-009: add Zid Pay's Prohibited Activities (الأنشطة المحظورة).
- CM-TRU-010: add Zid's E-commerce store regulations (ضوابط المتجر الإلكتروني).
- CM-TRU-014: add Zid's نقل البيانات عبر الحدود; CM-TRU-020: add Zid Assurance (ضمان زد) and Zid Stores' Customer Complaints.

### Gaps that bear on the cells

- Where Zid stores and processes data (ZD-C-041/where: searched, not found; observation needed), and where Vertex AI
  processes Zid Agent's data (ZD-C-042/where): CM-TRU-014 holds transfers only, with no data location as a quality.
- No data processing addendum, subprocessor list, cookie consent, customer data request or erasure, audit log, PCI DSS
  statement or security apps category is held.
- No acceptable-use rule for the platform beyond Zid Pay's (CM-TRU-009 is scoped to Zid Pay).
- A reason for requiring Nafath (ZD-C-038/reason) and a named responsibility for security settings (ZD-C-095/responsible,
  stated only in general terms).

### Rulings

None: Zid was never matched, so no unclear candidate holds a Zid concern (`matches`). `rulings.tsv` holds its header only.

### The whole part's check

`python3 -I method/check_class_part.py studies/class-model/parts/A-zid`: 0 problems, 25 flags for the reviewer (the
batch 1 flags answered in its section, and the batch 2 flags answered above).

## The coordinator's corrections after batch 2 (30 October)

- **ZD-C-111, Zid Assurance, lands here** in CM-TRU-020, moved from D: its complaint handling is the platform's mediation. D's CM-SUP-008 cites the same statements as `shows`. ZD-C-092 names A under `also`, for ZD-S-0935 and ZD-I-0413.
- **ZD-C-114 is `strained`** (ZD-S-1077 in CM-TRU-012), and ZD-C-077's reading names CM-TRU-001.
- **The part is complete,** with no capability added: domain A needs no Zid back-fill. BigCommerce maps next.

