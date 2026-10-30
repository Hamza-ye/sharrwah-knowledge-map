# F-bigcommerce: notes

BigCommerce's thirteen concerns of domain F, mapped onto the model so far (F-anchor, F-woocommerce and its back-fill,
F-zid: 44 capabilities). Read through `class_slice.py` only: `seed`, `model`, `concerns --where`, `statements`, `gaps`,
`key`, `search` and `candidates`. BigCommerce's statements are in English. Every placement below is a reading of the
statements cited. BigCommerce has no Q1 matches or unclear candidates, so `rulings.tsv` is empty. "Commerce" in the
statements is BigCommerce's company (Commerce.com US, Inc. and its affiliates, BC-S-0425).

## How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| BC-C-029 Unified Billing | CM-APP-003 | definition | strained |
| BC-C-054 GraphQL Admin API | CM-API-001 | terms | clean |
| BC-C-055 Account-level resources (GraphQL Account API) | CM-API-013 (new) | single | clean |
| BC-C-056 API accounts, OAuth scopes and API Terms | CM-API-002 | terms | strained |
| BC-C-057 API rate limits | CM-API-005 | terms | clean |
| BC-C-058 Webhooks | CM-API-008 | terms | clean |
| BC-C-059 Apps and the App Marketplace | CM-APP-001 | terms | strained |
| BC-C-063 MCP server and agentic commerce | CM-AIA-005 | role | strained |
| BC-C-064 AI features | CM-AIA-001 | terms | strained |
| BC-C-066 Powered By (Commerce-as-a-Service) | CM-PTN-010 (new) | single | clean |
| BC-C-076 Staging environments | CM-DVT-006 (new) | single | clean |
| BC-C-084 Third-Party Products and their integration | CM-APP-001 | role | clean |
| BC-C-087 Agents acting for clients | CM-PTN-001 | role | strained |

Ten joined existing capabilities; three made new ones. **The three new capabilities need a back-fill**
(`F-backfill-bigcommerce`) for Shopify, Salla, WooCommerce and Zid.

### New capabilities

- **CM-API-013 Account-level API** (parent CM-API-001). BigCommerce gives it an API group of its own, Account API
  [graphql] (BC-I-0109), over the account rather than one store: control panel users (BC-S-0298), all the account's
  stores (BC-S-0301), scopes account_* (BC-I-0368 to BC-I-0377). Parent CM-API-001: BigCommerce lists account-level
  credentials as one of its three types of API accounts (BC-S-0302).
- **CM-DVT-006 Staging environments** (no parent). A product line of its own (BC-I-0540): test, preview and deploy a
  store's updates without disrupting the live storefront (BC-S-0413); StagingPro for Enterprise-level stores (BC-S-0414).
  Kept apart from CM-DVT-004 (development stores): those are free stores given to developers to build apps and themes,
  this stages a live store's own changes. No statement groups it under the developer tools, so no parent; the coordinator
  may prefer CM-DVT-001.
- **CM-PTN-010 Commerce-as-a-Service for partners** (parent CM-PTN-001). An API group of its own, Beta Powered By > Stores
  and > Plans (BC-S-0359, BC-S-0363, BC-I-0115), "partner-focused APIs" to offer BigCommerce stores to the partner's
  merchants (BC-S-0361), the partner choosing whether to own the billing relationship (BC-S-0362). Kept apart from
  CM-DVT-003 (partner stores, which a partner keeps to build on or prepare) and CM-DVT-005 (ready stores): Powered By
  creates the partner's merchants' live stores, which it resells.

### Grains

- **BC-C-059** holds apps and the App Marketplace together, so it lands in the parent CM-APP-001. Its marketplace review
  (BC-S-0325) and the 21 categories go to CM-APP-002, its uninstall topic to CM-APP-004, unlisted apps to CM-APP-009.
- **BC-C-064** holds Commerce's AI Features as a whole, so it lands in the parent CM-AIA-001; BigCommerce Companion (an AI
  assistant embedded in the control panel, BC-S-0349) goes to CM-AIA-002, BigAI (product descriptions and SEO, BC-S-0350)
  to CM-AIA-003.
- **BC-C-056** holds API accounts, scopes and API Terms. The OAuth accounts land in CM-API-002; the scopes in CM-API-003;
  the API Terms' user-information duty (BC-S-0305) in CM-API-004; the default scope's webhooks (BC-S-0306) in CM-API-008.
  The store-level API accounts a merchant creates in Settings (BC-S-0303) go to CM-APP-009 (custom apps), as Zid's private
  apps and direct API access did: hence strained.
- **BC-C-029** (Unified Billing) lands in CM-APP-003. Its disbursement to partners (BC-S-0175, BC-S-0179) is also cited in
  CM-PTN-003 (partner payouts), its Partner Portal condition (BC-S-0174) in CM-PTN-001 and CM-PTN-002, its Unified Billing
  API's account-level tokens (BC-S-0181) in CM-API-013. Strained, also because no BigCommerce statement says Commerce keeps
  a share: Commerce acts as the Unified Billing Partners' collection agent, which the capability's definition doesn't say.
- **BC-C-063**: BigCommerce's Storefront MCP connects AI agents to storefronts to search products, manage carts and hand off
  to checkout (BC-S-0342). It lands in CM-AIA-005 (agentic commerce), not CM-AIA-004 (AI connector): there Salla's and
  WooCommerce's MCP servers link the merchant's own assistant to the store, under CM-AIA-001, the merchant's tools. Here the
  agents shop for buyers. The protocol is the same; the role differs. CM-AIA-004's BigCommerce cell is `none-held`, with
  the MCP hits named. If the reviewer reads CM-AIA-004 as any MCP server the platform provides, BC-S-0342 to BC-S-0345
  would also support it.

### Joins on role

- **BC-C-063 → CM-AIA-005**: BigCommerce's MCP server for AI agents and Agentic checkout (BC-S-0342, BC-S-0347) against
  Shopify's commerce agents built on its UCP-compliant MCP servers and WebMCP Tools (SH-S-0714, SH-I-0073).
- **BC-C-084 → CM-APP-001**: BigCommerce's Third-Party Products (BC-S-0462, BC-S-0463) against Shopify's Third Party Services
  (SH-S-0060, SH-S-0058) and WooCommerce's (WC-S-0487). The statements are near word for word: the platform may disable
  access at any time; dealings are solely between merchant and provider. The terms differ (Products, Services).
- **BC-C-087 → CM-PTN-001**: the Merchant-Client Terms, for someone using the Services as a client's agent (BC-S-0474,
  BC-S-0477), against the partner terms of Shopify (SH-S-0288) and Salla (SA-S-0213). Strained: no BigCommerce statement
  names a partner programme for such agents. The Merchant-Client Terms are a legal agreement, not an admin section, API
  group, plan line or app category, so by the dry run's convention they make no capability of their own.

### Homonyms and near-homonyms

- **Extension.** BigCommerce's "Extension" is a Commerce Service, not a Third-Party Product (BC-S-0464), contracted with
  Commerce.com entities (BC-S-0428); WooCommerce's extensions include third parties' plugins (WC-S-0852). BigCommerce's
  "Extension" is cited in CM-APP-011 (apps made by the platform's company), not in CM-APP-001's third-party sense.
- **App Extensions** (the scope store_app_extensions_manage, BC-S-0328) is not joined to Shopify's Admin UI extensions
  (CM-APP-008): no statement says what App Extensions extend. Cited in CM-APP-001 and CM-API-003.
- **connector.** BigCommerce's connector apps (an app type by authentication, BC-S-0324) are not Salla's AI Connector
  (CM-AIA-004).
- **Partner.** A Unified Billing Partner is an app vendor selling through the marketplace (BC-S-0179); a Powered By partner
  resells stores (BC-S-0361); the Partner Portal account (BC-S-0174) is the condition for the first.
- **agent.** "Commerce as agent" (BC-S-0175) and "agent of Client" (BC-S-0474) are legal agency, not AI agents (CM-AIA-*).

### Concerns read under `also`

BC-C-013 (product recommendations, Google Vertex AI), BC-C-017 (checkout extensions; "our partner Route has created a
checkout extension", BC-S-0101), BC-C-026 (payment providers), BC-C-044 (Scripts), BC-C-053 (Storefront API tokens),
BC-C-071 (shipping providers), BC-C-073 (tax providers). None is cited: each is its own domain's feature (D, C, E) with its
own API, and none fits a capability of domain F's model without stretching it. Two leads for the coordinator:
- **Provider APIs** (BC-I-0073, BC-S-0395: "BigCommerce calls your app's endpoints to retrieve data on behalf of a store",
  for shipping and tax) are an API group of their own, a mechanism where the platform calls the app during its own
  processing. CM-APP-005 (Functions) requires the platform to host the function, which BigCommerce doesn't, so it isn't
  cited there. If the coordinator wants the mechanism in F, it is a capability; I left it to domain C, where its features
  are.
- **Google Vertex AI** (BC-S-0076) generates product recommendations; it would be a slot filler of an AI capability if
  recommendations were placed in AIA rather than D.

## Statements of other domains cited

- **BC-S-0027** (BC-C-003, domain B) in CM-API-006, `shows`: the only BigCommerce statement held of an API's endpoints
  being deprecated for modern counterparts; nothing in domain F shows versioning beyond the name Webhooks v3.
- **BC-S-0428, BC-S-0432** (BC-C-079, domain A) in CM-APP-011, `own-service`: the legal-entity table naming Commerce.com US,
  Inc. and Commerce.com Pty. Ltd. as contracting for "Ecommerce Platform, Extensions, and certain Professional Services".
  This is the maker evidence the brief asks for: a statement naming the company as provider of Extensions.

## Gaps that bear on the cells

- **StagingPro's maker** (CM-DVT-006): "StagingPro's public API" (BC-S-0416) suggests a product of its own, but no
  statement names who makes it. Placed `core` by what the statements show (a BigCommerce product line, added through the
  BigCommerce representative).
- **BC-C-029/responsible** (Q1: searched, not found): the licence under which Commerce collects and disburses monies.
- **BC-C-054/decides** (searched, not found): who enables the Admin API and on which plans.
- **CM-APP-004**: only store/app/uninstalled is held; no install, authorize or subscription topic.
- **CM-APP-011**: no statement shows what an Extension is or that Extensions have a marketplace category.
- **CM-API-006**: no statement of BigCommerce's versioning policy or change log.
- **Slot fillers**: none written. "Third-party payment processors" (BC-S-0182) and "third-party providers used to provide
  the AI Features" (BC-S-0353) name no one.

## Names (proposals for the coordinator)

- CM-API-001: add BigCommerce's Admin API.
- CM-APP-003: add BigCommerce Unified Billing; "keeps a share for itself" isn't shown on BigCommerce.
- CM-AIA-005: add BigCommerce Storefront MCP, Agentic checkout, AI discovery.
- CM-APP-002: add BigCommerce App Marketplace.

## What the checker flagged, answered

- **Statements of other domains** (BC-S-0027, BC-S-0428, BC-S-0432): see above.
- **own-service on BC-S-0428 and BC-S-0432**: yes, they name Commerce.com US, Inc. and Commerce.com Pty. Ltd., the
  company, as the contracting party for Extensions.
- **Statements in more than one tree**: BC-S-0181, BC-S-0182, BC-S-0174, BC-S-0175, BC-S-0179 (all BC-C-029, strained);
  BC-S-0324 and BC-S-0328 (BC-C-059, strained: an app type defined by authentication; a scope for App Extensions);
  BC-S-0326 (unlisted apps, cited in CM-APP-009 and, as the approved-partner condition, in CM-PTN-002; BC-C-059 strained);
  BC-I-0477 (Ecommerce AI, an App Marketplace category, in CM-APP-002 with the other categories and in CM-AIA-001; BC-C-064
  strained). In each case the statement shows two things, one in each tree; neither capability is the other's parent.
- **BC-C-063 and BC-C-064 clean but cited in another tree**: corrected to `strained` (the shared inventory entries
  BC-I-0473 and BC-I-0477, which Q1 placed in two concerns each).
- **`none-held` with matching statements** (CM-AIA-004, CM-API-007, -009, -010, -011, -012, CM-APP-005, -006, -007, -008,
  -010, -012, CM-AUT-001, CM-DVT-001 to -004, CM-PTN-004 to -009): each cell's reading names the hits and why they don't
  show the capability; most are other domains' statements matched by a common word (settings, control panel, invoice,
  client, function, partner).

## Problems

- The checker matches "CLI" inside "client", so CM-DVT-002's flag lists the client and API-client statements.
- CM-DVT-001: BigCommerce's statements are drawn from its developer documentation (identifiers under /developer/), but no
  statement describes that documentation or its tools, so the cell is `none-held`.
