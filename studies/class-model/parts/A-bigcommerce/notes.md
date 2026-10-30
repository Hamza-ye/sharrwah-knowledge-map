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
