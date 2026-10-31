# A-bigcommerce: notes

Domain A, Merchant and platform: BigCommerce mapped onto the model of A-anchor, A-woocommerce, A-backfill-woocommerce and
A-zid. The part runs in two batches. Read through `class_slice.py` only: `seed`, `model --areas`, `concerns --where`,
`statements`, `gaps`, `matches`, `key`, `search`, `caps`, `outscope` and `candidates`. BigCommerce's statements are in
English only, so every search is in English. Every placement below is a reading of the statements cited. Nothing outside
the concern map is cited.

## Batch 1: ACC, STF, PLN and ONB

Concerns: BC-C-047, BC-C-079, BC-C-086, BC-C-061 and BC-C-030. BigCommerce's cell is written for all 27 capabilities of
the four areas (11 ACC, 5 STF, 7 PLN, 4 ONB): 13 cite statements, 14 are `none-held`. No capability is added; none of the
five concerns is moved.

### How the concerns landed

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| BC-C-047 Store profile and storefront settings | CM-ACC-006 | terms | strained |
| BC-C-079 Contracting entity and governing law | CM-ACC-002 | terms | clean |
| BC-C-086 Stores and merchant materials | CM-ACC-001 | role | strained |
| BC-C-061 Staff accounts and control panel users | CM-STF-001 | terms | clean |
| BC-C-030 Fees and billing (subscription, GMV and plan) | CM-PLN-004 | terms | strained |

All five joined existing capabilities; none made a new one.

### Grain and strained fits

- **BC-C-047** holds the whole Settings API, so it is coarser than CM-ACC-006. Its Storefront SEO (BC-S-0266) is domain E's
  CM-CNT-007, which E's part already cites, and is left there, as "One thing, one domain" asks. E also cites BC-S-0263 core
  in CM-CNT-007 and CM-SFR-013 and BC-S-0262 as shows in CM-SFR-008. BC-S-0263 is cited core here too, for the store's
  name and contact information it names. The merge will flag one sentence supporting `core` in two domains; the
  sentence names settings of both domains, so a reviewer may keep both citations.
- **BC-C-086** is the MSA's Store Terms. It defines the Store (BC-S-0469) and makes the merchant responsible for its Stores
  (BC-S-0471): this is the Store Owner's responsibility in Shopify's CM-ACC-001 (SH-S-0228), a join on role. The rest of
  the concern is trust's: content removal (BC-S-0470), the merchant's privacy policy (BC-S-0472) and its users' agreement
  (BC-S-0473). The reviewer may move the concern to CM-TRU-010, the merchant's legal compliance as the seller.
- **BC-C-030** is the Fees and Billing Terms, joined by terms with CM-PLN-004. Its plan side (GMV cap, automatic
  upgrades) is cited in CM-PLN-001, and its Open Payment Provider Fee, through the plan line BC-I-0423, in CM-PLN-003. Both
  are in CM-PLN-001's tree, not CM-PLN-004's. BC-S-0184 (the list of fees) is cited only in CM-PLN-004, so that it stays
  in one tree.

### Joins on role, homonyms

- One join on role: BC-C-086 with Shopify's Store Owner (above).
- No new homonym. "Store" in BigCommerce's MSA is the merchant's store. Multi-Storefront (BC-C-039, domain E's
  CM-CHN-007) is several storefronts in one store, not CM-ACC-003's several stores under one owner. BC-S-0301 (account-level
  credentials reach "all the account's stores") is the one statement CM-ACC-003 cites.
- The governing law's place is a reading: the Contracting Entity table's rows come as single strings (BC-S-0428 to
  BC-S-0432). BC-S-0426 says the law is the one the table gives, and the inventory rows (BC-I-0542 to BC-I-0546) show the
  third column. The slot fillers name the law of each row.

### Concerns read under `also`

BC-C-055 (F, the Account API): BC-S-0300 and BC-S-0301 are cited as shows in CM-ACC-001 and CM-ACC-003. F's part cites
them core in CM-API-013, so here they show only the account and its stores. BC-C-066 (F, Powered By): BC-S-0077 is cited
as shows in CM-ONB-003 and BC-S-0363 as shows in CM-PLN-001; F's part cites BC-S-0363 core in CM-PTN-010. BC-C-029 (F,
Unified Billing): BC-S-0178 is cited as shows in CM-PLN-004. BC-C-087 (F, Agents) is read for CM-STF-005 and not cited:
it states an agent's authority to bind its client, which F holds in CM-PTN-001, not access granted to a store's admin.
BC-C-060, BC-C-078 and BC-C-084 bear on no capability of these areas.

### Unclear candidates

Q1 never matched BigCommerce, so no unclear candidate holds these concerns, and `rulings.tsv` has only its header.

### The checker's flags, answered

- `BC-C-063/decides/BC-S-0344` (F, not naming A), in CM-ACC-001: the one statement naming the store owner as a role. It
  is cited as shows; F cites it core in CM-AIA-005.
- `BC-C-059/boundary/BC-S-0329` (F, not naming A), in CM-ONB-002: the one statement of a store being cancelled on the
  platform. It is cited as shows; F cites it core in CM-APP-004, the app's lifecycle.
- `BC-C-026/decides/BC-S-0154` (C, naming F, not A), in CM-PLN-003: the one statement saying BigCommerce charges the Open
  Payment Provider Fee and on which plans. It is cited core, as Shopify's third-party transaction fees are. C's BigCommerce
  part hasn't run. If it cites the sentence core in CM-PAY-007 (payment processing fees of the platform's payment
  service), the merge will flag it. The fee is charged on orders through providers other than the platform's own, so the
  reading here is that it is CM-PLN-003's.
- **The 13 `none-held` flags** (CM-ACC-004, -005, -007, -009, -010, -011, CM-ONB-004, CM-PLN-002, -006, CM-STF-002 to
  -005): each flag lists the statements that match the searched terms or the other platforms' terms. They were read, and
  the cell's `reading` names the ones that come nearest. None shows the capability. The matches are generic words:
  business and Company (PayPal Braintree's US-business eligibility BC-S-0157, B2B Edition's companies BC-S-0193 and
  BC-S-0354, Companion BC-S-0349), entities (the Inventory API BC-S-0031, Commerce's own entities), closed (closed betas
  BC-S-0077 and BC-S-0289), OAuth and API accounts (domain F), set up (settings sections of domains C and E), monthly and
  annual (cited elsewhere), wallets and balance (domain C), Customer and roles (buyers, the DPA), groups (customer groups,
  domain D), quota (API limits) and agent (BC-C-087, Unified Billing, AI agents). CM-ACC-007 and CM-ACC-009 match
  Storefront Status (BC-S-0265, BC-I-0395); see Gaps.

### Gaps

- Storefront Status (BC-S-0265) is a setting whose statement doesn't say what it holds. A capture of the store's v3
  settings/storefront/status in other-product-class (`bigcommerce/raw/runs/20261029T023811Z-channels-en`, read for
  context, never cited) holds `down_for_maintenance_message`, `prelaunch_message` and `prelaunch_password`. With a
  statement holding them, CM-ACC-007 (maintenance mode) and CM-ACC-009 (before launch) could be cited. Both are
  `none-held` until then.
- BC-C-047/responsible and BC-C-061/responsible are "stated only in general terms"; every concern's `reason` is
  "searched, not found".
- No statement gives the plans' prices, the GMV overage fee's or the Open Payment Provider Fee's amount, a billing page or
  invoice list in the control panel, a support plan line, staff permissions, or the country given at sign-up.
- The plan line Open Payment Provider Fee (BC-I-0423) and the scopes account_users_read and account_users_delete
  (BC-I-0375, BC-I-0377) are cited as placed inventory entries, because no statement covers them.

### For batch 2 (TRU)

- **The part's other concerns of domain A:** BC-C-028, BC-C-037, BC-C-080, BC-C-081, BC-C-082, BC-C-083, BC-C-085 and BC-C-088.
- **BC-C-080 (sanctions):** batch 1 cites BC-S-0437 as shows in CM-ACC-008 and BC-S-0436 as shows in CM-ONB-002.
  WooCommerce's sanctions concerns WC-C-028 and WC-C-029 landed in CM-ACC-008 by M-084, WC-C-029 strained towards
  CM-TRU-010. BC-C-080 is mostly the merchant's own compliance programme (BC-S-0438, BC-S-0439), so it may be CM-TRU-010's,
  with its sanctions list read against CM-ACC-008.
- **BC-C-086's trust statements:** BC-S-0470 (content removal) bears on CM-TRU-009, BC-S-0473 (the users' agreement) and
  BC-S-0471 on CM-TRU-010, and BC-S-0472 (the merchant's privacy policy, cited by E in CM-CNT-008) on CM-TRU-005 or
  CM-TRU-013. Batch 2 may cite them there; BC-C-086 stays landed in CM-ACC-001.
- **BC-S-0421 (Tier 1 certifications):** domain E's BigCommerce part recorded it as a quality of E's CM-SFR-010 and left it
  to A's TRU to weigh, for CM-TRU-018 (PCI DSS) or a certification quality of the platform's security.
- **TRU candidates seen in passing:** BC-S-0169 (annual PCI DSS validation, BC-C-028) for CM-TRU-018; BC-S-0442 and
  BC-S-0443 (processor and controller) for CM-TRU-013; BC-S-0445 and BC-S-0447 (data transfer and hosting) for CM-TRU-014;
  BC-S-0456 and BC-S-0458 (subprocessors) for CM-TRU-015; BC-S-0467 (the disclaimer on the legality of the merchant's
  products, BC-C-085) for CM-TRU-009 or CM-TRU-010; BC-S-0480 (Intellectual Property Agent, BC-C-088) for CM-TRU-011.
- BC-C-060 (G, store logs, naming A) is for CM-TRU-003, the audit log. BC-S-0331 says the System Logs endpoint is for
  "debugging, auditing, and monitoring".

## Batch 2: TRU

Concerns: BC-C-028, BC-C-037, BC-C-080, BC-C-081, BC-C-082, BC-C-083, BC-C-085 and BC-C-088. BigCommerce's cell is written
for all 21 capabilities of TRU: 12 cite statements, 9 are `none-held` (CM-TRU-001, -002, -004, -008, -012, -016, -017,
-020, -021). No capability is added; none of the eight concerns is moved. Searches are in English only.

### How the concerns landed

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| BC-C-028 Payment card security (PCI DSS) | CM-TRU-018 | terms | clean |
| BC-C-037 Storefront cookie consent | CM-TRU-006 | terms | clean |
| BC-C-080 Anti-corruption, export and sanctions compliance | CM-TRU-010 | role | strained |
| BC-C-081 Personal data processing roles | CM-TRU-013 | terms | strained |
| BC-C-082 Data transfer and storage location | CM-TRU-014 | terms | strained |
| BC-C-083 Subprocessors and hosting services | CM-TRU-015 | terms | strained |
| BC-C-085 Acceptable use and highly regulated products | CM-TRU-009 | terms | strained |
| BC-C-088 Infringing materials | CM-TRU-011 | terms | clean |

All eight joined existing capabilities; none made a new one. For the whole part: 13 concerns, all joined existing
capabilities, none new.

### Grain, strained fits and what batch 1 left

- **BC-C-080** lands in CM-TRU-010, not CM-ACC-008. Its own words are the merchant's representations and covenants: a
  risk-based compliance programme with sanctions screenings (BC-S-0438), cooperation with Commerce on ABAC laws
  (BC-S-0439), under the clause's heading (BC-S-0435). That is the role of Shopify's merchant who answers for its
  transactions and researches import and export laws (SH-S-0236, SH-S-0667): a join on role. Strained: its sanctions
  list (BC-S-0437) is cited by batch 1 in CM-ACC-008 and here, and its termination for cause (BC-S-0436) by batch 1 in
  CM-ONB-002. WooCommerce's WC-C-029, the merchant's own sanctions compliance, landed in CM-ACC-008 by M-084, strained
  towards CM-TRU-010; the reviewer may want the two platforms' sanctions concerns in one capability. Zid's sanctions lists
  sit in CM-TRU-009 (Zid Pay's prohibited activities), a third home; the class's sanctions statements are spread over
  CM-ACC-008, CM-TRU-009 and CM-TRU-010.
- **BC-C-081**: strained because its Shopper requests (BC-S-0444) are cited in CM-TRU-007 (CM-TRU-005's tree). It is
  cited there only, not also in CM-TRU-013, so the sentence stays in one tree.
- **BC-C-082** and **BC-C-083**: strained by domain G. G's BigCommerce part cites BC-S-0450 (availability zones) core and
  BC-S-0455 (uptime, with its quality) in CM-OPS-001, and BC-S-0457 (hosting services) outside in CM-OPS-003. BC-S-0450 and
  BC-S-0455 are left to G, as "One thing, one domain" asks. BC-S-0457 is cited here as shows, since it names no third
  party; G reads the same words as outside. The subprocessor rows BC-S-0446 to BC-S-0448 are cited in CM-TRU-014 (their
  locations) and CM-TRU-015 (the subprocessor), children of one parent, as Shopify's rows are.
- **BC-S-0459** (Backup Storage: backing up the merchant's files and data on Commerce servers is solely the merchant's
  duty) is cited by no capability of domain A. No capability of any domain is about backups (`caps --terms backup`). It
  is a lead for G's CM-OPS-001 (reliability and continuity), which G's part didn't cite; the coordinator may give it there.
- **BC-C-085** lands in CM-TRU-009 by its first term, Acceptable Use Policy. Three of its four statements (BC-S-0466 to
  BC-S-0468, Highly Regulated Products and the disclaimer) are cited in CM-TRU-010, so it is strained; the reviewer may
  split it or move it to CM-TRU-010.
- **BC-C-086's trust statements** (batch 1's lead): BC-S-0470 (content removal) is cited in CM-TRU-009 as well as batch
  1's CM-ONB-002; BC-S-0472 (the merchant's privacy policy) in CM-TRU-005, as E cites it in CM-CNT-008; BC-S-0473 (the
  merchant's agreement with Your Users) in CM-TRU-010. BC-S-0471 stays only in batch 1's CM-ACC-001, so that it stays in
  one tree. BC-C-086 is now cited in the trees of CM-ACC-001, CM-ONB-002, CM-TRU-005, CM-TRU-009 and CM-TRU-010; batch 1
  marked it strained, which still holds.
- **BC-S-0421, the Tier 1 certifications** (domain E's lead): cited as shows in CM-TRU-018, with its words as a quality
  of CM-TRU-018. It names PCI among ISO, SOC, FIPS, RH-ISAC, GDPR and CCPA. No capability of the model is the platform's
  security certifications as a whole (`caps --terms "certification; ISO; SOC 2; security certifications"` finds none),
  and CM-TRU-018 is the one capability that is a certification of the platform's security, so it is weighed here. E
  records the same sentence as a quality of CM-SFR-010 (SSL); both cite it as shows, so the merge flags nothing. The
  coordinator may keep one of the two qualities.
- **CM-TRU-003**: BC-S-0331's second sentence is the Staff Action Logs endpoint, "to audit the actions staff users
  performed in the store's control panel", cited core here. Its first sentence (the System Logs endpoint) is G's
  CM-OPS-005, where G's part cites the statement core. The merge will flag one statement supporting core in two domains;
  the sentence names two endpoints, one per domain, so both citations may stand.

### Joins on role, homonyms

- One join on role in this batch: BC-C-080 with Shopify's merchant who answers for its transactions and researches import
  and export laws (CM-TRU-010).
- No new homonym. "Security Settings" is the title of BC-S-0216, the storefront's cookie-consent setting, not the admin's
  sign-in security (CM-TRU-001); "Customer Login (SSO)" (BC-S-0201) is shoppers' sign-in, domain D's.

### Concerns read under `also`

BC-C-060 (G): BC-S-0331 cited core in CM-TRU-003 (above). BC-C-078 (E): BC-S-0421 cited as shows in CM-TRU-018; its
Storefront Security settings (BC-S-0422, BC-S-0424) are the storefront's and are named in CM-TRU-001's reading. BC-C-059
(F): BC-I-0490 (Payments & Security) cited extension-point in CM-TRU-019, as F cites it in CM-APP-002; both
extension-point, so no flag. BC-C-055 (F): BC-S-0298 (auditing who the control-panel users are) read for CM-TRU-003 and
not cited. BC-C-026, BC-C-029, BC-C-063, BC-C-066, BC-C-084 and BC-C-087 bear on no capability of TRU.

### Unclear candidates

None: Q1 never matched BigCommerce. `rulings.tsv` keeps only its header.

### The checker's flags, answered

- `BC-C-080/responsible/BC-S-0437` in CM-ACC-008 (batch 1) and CM-TRU-010: the merchant's covenant that its parties and
  customers are not of sanctioned regions. Read as the merchant's compliance, it is CM-TRU-010's; batch 1 read it as
  shows for the countries the platform serves, for want of any list of them. Both cite it as shows. The coordinator may
  keep only one; the reading here is CM-TRU-010.
- `BC-C-086/decides/BC-S-0470` in CM-ONB-002 (batch 1) and CM-TRU-009: content removal for violating Laws or the
  Agreement. It is acceptable-use enforcement (CM-TRU-009); batch 1 cited it as an event of the store's lifecycle. Both
  shows.
- **The 9 `none-held` flags of TRU**: each flag's statements were read; the cell's reading names the nearest. CM-TRU-001:
  shoppers' SSO (domain D), storefront security (E) and the PCI statements' "security". CM-TRU-004: Cloudflare's DDoS row,
  the API's rate limits (F), "fraud". CM-TRU-008: BigCommerce Analytics for the store's own ML models (D), No Input
  Training (BC-S-0353), aggregated stock (B). CM-TRU-012 and CM-TRU-020: "dispute" in the governing law and the DMCA
  protocol. CM-TRU-016: a cancelled app setting (BC-S-0074), the store/app/uninstalled topic (BC-S-0329, batch 1's
  CM-ONB-002), the scope account_subscriptions_cancel (BC-I-0374). CM-TRU-017: the merchant's privacy policy.
  CM-TRU-021: Unified Billing's "collection" (F), pickup ("collect"), analytics (D). None shows the capability.
- The 14 flags on batch 1's `none-held` cells are answered in batch 1's section.

### Gaps

- Which region a store's data is stored in, and whether a merchant can choose it, is "page not read" (BC-C-082/decides):
  CM-TRU-014 holds the subprocessors' locations only.
- No statement holds a notice of new subprocessors or a right to object to one (CM-TRU-015), a retention period after the
  store closes (CM-TRU-016), requests from public authorities (CM-TRU-017), admin sign-in security (CM-TRU-001), or where
  acceptable use is enforced (BC-C-085/where: searched, not found).
- Whether BigCommerce itself screens merchants, partners or shoppers against sanctions lists is "searched, not found"
  (BC-C-080/responsible).
- Who turns System Logs and Staff Action Logs on, or limits them by plan, is "page not read" (BC-C-060/decides).
- The subprocessor list's entries other than Google, Amazon and Cloudflare (BC-I-0550, BC-I-0552, BC-I-0554 to
  BC-I-0569) are cited as placed inventory entries, because no statement covers them; the data-processors page
  (BC-S-0454) would hold what each does and where.

### Problems on batch 1's rows, for the coordinator

The whole part's check prints 0 problems. Two of batch 1's citations now share a statement with this batch's cells
(BC-S-0437, BC-S-0470; above). Batch 1's landing of BC-C-086 says the reviewer may move it to CM-TRU-010; with this
batch's cells its statements are spread over five trees, so a move would not make it clean.

### The coordinator, after C-bigcommerce batch 2

- **CM-PLN-003** cites BC-C-026's four fee statements that C-bigcommerce left for it, by "One thing, one domain": the plan line's values by plan (BC-S-0152) and the $0 fee through Embedded Payment Providers (BC-S-0153), and the terms' fees charged by Commerce, not by the provider (BC-S-0158), as `core`; no payment fees through eligible Embedded Payment Providers (BC-S-0159) as `shows`.
