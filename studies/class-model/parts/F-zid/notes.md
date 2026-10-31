# F-zid: notes

Zid's eight concerns of domain F, mapped onto the model so far (F-anchor, F-woocommerce and its back-fill: 44
capabilities). Read through `class_slice.py` only: `seed`, `model`, `concerns --where`, `statements`, `gaps`, `key`,
`search`, `outscope` (nothing unplaced for Zid) and `candidates`. Zid's statements are in Arabic and English; searches
used both, Arabic terms with and without ال and in singular and plural where they differ. Every placement below is a
reading of the statements cited. Zid has no Q1 matches or unclear candidates, so `rulings.tsv` is empty.

## How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| ZD-C-022 App Market subscriptions and partner payouts | CM-APP-003 | definition | strained |
| ZD-C-025 Zid Agent / وكيل زد | CM-AIA-002 | role | strained |
| ZD-C-070 Zid App Market / سوق تطبيقات زد | CM-APP-002 | definition | strained |
| ZD-C-071 OAuth authorization and app scopes | CM-API-002 | terms | strained |
| ZD-C-072 Webhooks | CM-API-008 | terms | clean |
| ZD-C-073 Embedded apps | CM-APP-007 | terms | clean |
| ZD-C-074 Private apps and direct API access | CM-APP-009 | role | strained |
| ZD-C-115 Zid Growth / زد نمو | CM-PTN-005 | role | strained |

All eight joined existing capabilities; none made a new one. No capability is added, so no back-fill is needed for Zid.

### Grains

- **ZD-C-022** holds what the merchant pays Zid for an app and what Zid pays the partner. It lands in CM-APP-003 (app
  charges billed through the platform), where its lead terms are; its payouts (Payments → Payouts, partner rate,
  withholding tax) are cited in CM-PTN-003, and its subscription events in CM-APP-004. Strained for the PTN tree.
- **ZD-C-071** holds OAuth and scopes. The OAuth server and the merchant's approval are in CM-API-002; the scopes in
  CM-API-003; the Authorization and X-Manager-Token headers, required on every request, in CM-API-001 as a convention
  common to the API. All in the API-001 tree; strained only for its topic app.market.application.authorized (ZD-S-0073),
  cited in CM-APP-004 with the app's other lifecycle events, as Salla's app.store.authorize is.
- **ZD-C-072** holds the webhooks and their health tracking. The conditions (ZD-S-0880) go to CM-API-010, conditional
  webhooks. The circuit breaker and its health states stay in CM-API-008: Zid gives them one endpoint, Health Summary,
  in its Webhooks group, not an API group, admin section or plan line of their own, so by the dry run's test they are
  not a capability. If a later platform shows webhook delivery health with a place of its own, the coordinator may split
  it, with ZD-S-0878, ZD-S-0879, ZD-S-0881 and ZD-S-0883.
- **ZD-C-073**'s authentication mechanism and scope (ZD-S-0886, ZD-S-0123) are cited in the parent CM-APP-006, in the
  way Salla's Embedded SDK modules are; the iframe page itself in CM-APP-007.
- **ZD-C-074** holds private apps and the API access a store buys as a plan line or an add-on. Both land in CM-APP-009:
  the add-on (خدمة الربط المباشرة (APIs), Finance > Billing > Add-ons) and the plan line Connect your store with
  external systems (via API) are the gate for installing a private app (ZD-S-0889), as Shopify's plan line Build custom
  apps using Shopify APIs is for custom apps. Its statement that Zid provides the APIs and connection tools (ZD-S-0892)
  is cited in CM-API-001, the only Zid statement found that says Zid provides the API; hence strained. Its My apps page
  (ZD-S-0888) is cited in the parent CM-APP-001.
- **ZD-C-070**'s App Market categories: the AI ones (ZD-I-0430, ZD-I-0431) are cited in CM-AIA-001 as
  `extension-point`, the way an app-store category is evidence for what the apps do; three others stand for the
  categories in CM-APP-002. The rest (ZD-I-0432 to ZD-I-0463) are left uncited: they are evidence for the capabilities
  of the domains whose work the apps do, for their parts to cite. Strained by S1 for these two citations and for the App
  Partner terms (ZD-I-0426) in CM-PTN-001.

### Joins on role (readings)

- **ZD-C-025 → CM-AIA-002.** Zid Agent powers AI-assisted features, including conversational assistance, for the
  merchant (ZD-S-0717): Shopify's Sidekick (SH-S-0736) and Salla's AI agent (SA-S-3577). Strained: no Zid statement
  places it inside the admin; its one place is its own prepaid wallet (ZD-S-0713), and its features (product research,
  store optimization, campaign management) reach beyond an assistant.
- **ZD-C-074 → CM-APP-009.** Zid's private apps (ZD-S-0893) against Shopify's custom distribution for a specific
  merchant (SH-S-0693) and custom apps. Strained also because a Zid private app may be a partner's app granted to
  specific stores, where the capability's definition says the store develops it or has it developed. The capability's
  name could become "Custom and private apps: apps for one store or a few, not listed in the app store" (a rename
  proposed to the coordinator).
- **ZD-C-115 → CM-PTN-005.** Zid Growth, at Dashboard > Growth (ZD-S-1078), lists services that partners provide,
  bought through a cart (ZD-S-1080): Salla's Merchant Services (SA-S-1885, SA-S-0198) and Shopify's Partner Directory
  (SH-S-0760). Strained: its staff permissions name services beyond a partner's expertise (packaging, self-storage
  units, co-working spaces, ZD-I-0487, ZD-I-0525, ZD-I-0534), and a relationship manager on the Professional plan
  (ZD-S-1079) whose provider isn't stated. Q1's gap (responsible, observation needed) leaves who provides each service
  unstated. The name could take Zid's term: "(... Zid Growth, زد نمو)".

### Definition joins

- **ZD-C-070 → CM-APP-002**: a platform owned by Zid that connects stores to the apps it lists and reviews (ZD-S-0861,
  ZD-S-0862, ZD-S-0863), as Salla's and Shopify's app stores (SA-S-0002, SA-S-0023, SH-S-2753, SH-S-0698). The name
  could add Zid's term, App Market (سوق تطبيقات زد).
- **ZD-C-022 → CM-APP-003**: the app's payment goes through the platform (ZD-S-0684, ZD-S-0685; SA-S-0025; SH-S-0282).

## Concerns read under `also`

- **ZD-C-042** (AI data processing, domain A): ZD-S-0797, AI processing only after explicit in-app consent, cited as
  `shows` in CM-AIA-001. Its processor statements repeat ZD-S-0717, cited under ZD-C-025's key.
- **ZD-C-112** (Zid Voice, domain C): ZD-S-1070, AI that communicates on the merchant's behalf, cited as `shows` in
  CM-AIA-001. Its admin place (Orders > Zid Voice, ZD-S-1067) is left to domain C, so that no statement supports `core`
  in two domains.
- **ZD-C-061** (shipping apps, domain C): ZD-S-0853 (Zid uploads an invoice the shipping app's partner pays) cited as
  `core` in CM-PTN-004, and ZD-S-0854 as `shows` and a quality. Its category id 5 and its shipping-app terms are domain
  C's.
- **ZD-C-076** (Theme Market, domain E): ZD-S-0899, the Partner Share formula, cited as `shows` and a quality in
  CM-PTN-003. Q1's note says it is stated for apps, themes and landing pages; the note doesn't count.
- **ZD-C-010** (Zid Payments Open APIs for payment providers, domain C): left uncited. It is the payment feature's own
  provider interface; no capability of domain F is a provider API.

## Homonyms

- **وكيل / agent** (Q1's U-062): Zid Agent is the merchant's AI agent (CM-AIA-002), not buyers' agents
  (CM-AIA-005); Zid Voice's voice agent calls buyers for the merchant (domain C); الوكيل in ZD-S-0981 is a device
  vendor's agent. Kept apart.
- **"rate limit"** (U-045): Zid's hits for limit are plan and order limits, none the API's. CM-API-005 is none-held.
- **Settings**: the other platforms' term for CM-APP-010 and CM-PTN-002 matches dozens of Zid's store-settings
  statements (domains A to E), none an app's or a partner's settings.

## Qualities and slot fillers

Qualities: the Zid Agent wallet's two-hour refund window (CM-AIA-002), a webhook endpoint's broken threshold
(CM-API-008), the events that support conditions (CM-API-010), withholding tax and the Partner Share formula
(CM-PTN-003), and the 0.70 SAR per transaction for shipping apps (CM-PTN-004; that the partner pays it is a reading of
ZD-S-0853 with ZD-S-0854). Slot filler: Google Cloud Vertex AI, which powers Zid Agent (CM-AIA-002).

## What the checker flagged, answered

- **none-held cells whose terms match statements** (CM-AIA-003, AIA-005, API-004, API-005, API-006, API-007, API-009,
  API-011, API-012, APP-005, APP-008, APP-010, APP-011, APP-012, AUT-001, DVT-001, DVT-002, DVT-003, PTN-002, PTN-006,
  PTN-007, PTN-008, PTN-009): each hit was read; each cell's reading names what the hits are. The rest are substring
  hits: CLI inside client and decline (DVT-002), MoR inside more (PTN-007), refer inside prefer (PTN-008), الكاش in
  الكاشير (API-012), and the other platforms' Settings, Stores and Notifications matching Zid's store features
  (APP-010, PTN-002, DVT-003, API-009). Webhook statements (API-009's hits) are Zid's API's, cited in CM-API-008; none
  shows the merchant subscribing from the admin.
- **CM-PTN-004, core rests only on a boundary statement**: ZD-S-0853 says Zid itself creates the record and uploads the
  invoice that the partner pays, so it shows Zid doing it; Q1 placed it under boundary because it is in the shipping
  apps' integration docs.
- **ZD-C-070 clean but cited in other trees**: now strained (above).

## Problems and gaps

- **CM-API-001**: no Zid statement found defines its API as a whole, or names its base URL; the API's resources appear
  only in feature groups (Merchant APIs > ...), cited in their domains.
- **CM-API-006**: the endpoints' paths carry /v1/ and /v2/ (ZD-S-0882, ZD-S-0937), but no statement says what they
  version.
- **CM-PTN-001**: Zid's App Partner terms are held only as an inventory entry's name (ZD-I-0426); no statement found
  defines the programme or the Partner Dashboard as a place, so the cell supports no placement.
- **CM-AIA-002**: no statement found says where in the admin Zid Agent works; the terms page (ZD-I-0414) is held only
  by name.
- **CM-PTN-005**: who provides each Zid Growth service is a Q1 gap (observation needed).
