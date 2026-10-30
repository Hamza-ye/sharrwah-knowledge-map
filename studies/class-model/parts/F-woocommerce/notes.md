# F-woocommerce: notes

WooCommerce's ten concerns of domain F, mapped onto the model F-anchor built (41 capabilities). Read through
`class_slice.py` only: `seed`, `model`, `concerns --where`, `statements`, `gaps`, `matches`, `key`, `search` and
`candidates`. Searches are in English, WooCommerce's only language in the concern map. Every placement below is a
reading of the statements cited.

## How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| WC-C-059 third-party extensions | CM-APP-001 | match:M-067 | clean |
| WC-C-017 Woo Marketplace sales | CM-APP-002 | role | strained |
| WC-C-050 Developed by Woo | CM-APP-011 (new) | single | clean |
| WC-C-063 WooCommerce.com connection | CM-APP-012 (new) | single | clean |
| WC-C-086 extension framework | CM-APP-006 | role | strained |
| WC-C-077 webhooks | CM-API-008 | match:M-069 | clean |
| WC-C-078 REST API and keys | CM-API-001 | match:M-073 | clean |
| WC-C-095 WooCommerce MCP | CM-AIA-004 | match:M-079 | clean |
| WC-C-096 AI features of Automattic | CM-AIA-001 | role | clean |
| WC-C-112 Business services, agency partners | CM-PTN-005 | role | strained |

Eight concerns joined existing capabilities; two made new ones. A third new capability, CM-API-012, holds statements of
WC-C-078, which lands in its parent.

### New capabilities, and why each is one

- **CM-APP-011, apps made by the platform's company** (parent CM-APP-002). The Marketplace gives Woo's own extensions a
  category of their own, Extensions > Developed by Woo (WC-S-0697): an app category, the dry run's test. Its parent is
  CM-APP-002 because the category's own path puts it under the Marketplace's Extensions. Shopify's "Apps that are made by
  Shopify are usually free and are supported by Shopify" (SH-C-156/responsible/SH-S-0738) is cited as `shows` in
  CM-APP-001; the back-fill decides whether it belongs here.
- **CM-APP-012, marketplace connection** (parent CM-APP-001). WooCommerce gives the link between the store and its
  WooCommerce.com account a settings section, Advanced > WooCommerce.com (WC-S-0027), and an API group, wccom-site/v3
  (WC-S-0085). Landing WC-C-063 in CM-APP-001 would have hidden it: the concern's name leads with the connection, and
  the statements say what it does (install extensions, receive updates and support, manage subscriptions, WC-S-0899).
  Its admin menu WooCommerce > Extensions (WC-S-0046) and the onboarding tasks (WC-S-0421, WC-S-0432) are cited in
  CM-APP-001 and CM-APP-002, so the concern stays in one tree.
- **CM-API-012, API response caching** (parent CM-API-001). A settings section of its own, Advanced > REST API caching
  (WC-S-0024). Its flag is experimental and off by default (WC-S-5414), cited as `shows`. If the reviewer reads one
  experimental section as too thin to be a capability, its two rows move to CM-API-001 and the capability goes.

### Grains

- **WC-C-078** holds the whole REST API. Its statements are split by the anchor's children: the API itself in
  CM-API-001; keys and authentication in CM-API-002; the access levels Read, Write, Read/Write in CM-API-003; the
  namespaces wc/v1 to wc/v4 and the Legacy API section in CM-API-006; caching in CM-API-012. Its settings API
  (WC-S-0684) stays in CM-API-001, the API's own resource for the store's settings.
- **WC-C-086** holds an admin page, settings pages, integration settings, a compatibility declaration and REST
  controllers for wc-admin. It lands in CM-APP-006, app UI in the admin. Its integration settings (WC_Integration, the
  Integration tab) are cited in CM-APP-010 and wc_admin_register_page in CM-APP-007, both in the same tree.
  `FeaturesUtil::declare_compatibility` (WC-S-0455) and `woocommerce_admin_rest_controllers` (WC-S-0449) are uncited:
  no capability of the model is an extension declaring its compatibility with the platform's features, or adding
  controllers to the admin's API, and one function each isn't a place of its own. If a later part shows either as a
  capability, they go there.
- **WC-C-017** holds the Marketplace, its Vendor Agreement, the 70% revenue share and the Refund Policy. The
  Marketplace is cited in CM-APP-002, the share and refund in CM-APP-003, the Vendor Agreement in CM-PTN-001 and the
  payout to the Partner in CM-PTN-003. It is strained: it is cited in the PTN tree, and its category Themes (WC-S-0695)
  is domain E's (U-051), left uncited.
- **WC-S-0580** (the 70% clause) is cited twice, by two keys of the same statement: WC-C-017/decides/WC-S-0580 in
  CM-APP-003 (WooCommerce collects the purchase's revenue and keeps a share) and WC-C-017/responsible/WC-S-0580 in
  CM-PTN-003 (WooCommerce pays the Partner). The checker tests trees by key, so it doesn't flag this; I say it here so
  the reviewer can. It is the same split as the anchor made for Salla's SA-C-195 across the two capabilities.

### Joins on role (readings)

- **WC-C-017 with the App Stores:** the WooCommerce.com Marketplace, which "connects trusted developers and merchants"
  (WC-S-0923), against the Shopify App Store (SH-S-2753) and Salla's App Store (SA-S-1884). Terms differ
  (Marketplace, extensions, vendor).
- **WC-C-086 with the app UI in the admin:** `wc_admin_register_page` (WC-S-0450) against App Home (SH-S-2182) and the
  Embedded SDK (SA-S-0197). An extension runs in the merchant's own install, not in an iframe.
- **WC-C-086's integration settings with Salla's App Settings** (CM-APP-010): WC_Integration (WC-S-0441, WC-S-0922)
  against "custom-made parameters by the Salla App Developer" (SA-S-0210). Where WooCommerce stores them isn't stated.
- **WC-C-096 with AI tools for merchants:** "features that incorporate artificial intelligence (AI) that enable you to
  use AI to help set up or operate your website or store" (WC-S-0486) against Shopify's AI features in the admin
  (SH-S-7488) and Salla's salla_gpt (SA-S-3400).
- **WC-C-112 with partner services:** the Woo Agency Partners' directory (WC-S-5497) against the Partner Directory
  (SH-S-0760) and Salla's service providers (SA-S-0198).
- **WC-C-078's keys with app authorization** (CM-API-002, U-046): API keys the merchant generates and enters in the
  external service (WC-S-0888) against Salla's OAuth 2.0 (SA-S-0176) and Shopify's API authentication (SH-I-0030).
- **WC-C-017's Vendor Agreement with the partner programme** (CM-PTN-001, U-052): both agreements name the third
  party Partner (WC-S-0576, SH-S-0288).

### Homonyms kept apart

- **CLI.** WooCommerce's command `wc com connect` (WC-C-063/boundary/WC-S-5346), whose source is the WC-CLI's
  documentation (the statement's structure, docs/wc-cli), manages a store. Shopify's and Salla's CLIs build apps and
  themes (CM-DVT-002). I cite the command in CM-APP-012 and write CM-DVT-002 `none-held`. If the reviewer reads
  CM-DVT-002 as "the platform's CLI" whatever it works on, the command moves there as `core` and WC-C-063 becomes
  strained.
- **filters.** WordPress filters (`apply_filters`: WC-S-0442, WC-S-0444, WC-S-0447, WC-S-0448) are hooks for code, not
  Salla's conditional webhook filters (CM-API-010).
- **MCP.** WooCommerce's MCP, through which AI assistants work on the store (WC-S-0918), is Salla's AI Connector's role
  (CM-AIA-004), not Shopify's MCP servers for buyers' agents (CM-AIA-005), as the anchor found.
- **batch / bulk.** See CM-API-007 below.
- **Automation.** The Marketplace's category Extensions > Marketing > Automation (WC-S-0756) and MailPoet's automation
  are marketing extensions (domain D), not a workflow tool like Shopify Flow (CM-AUT-001).

### Strained fits

- **WC-C-017 in CM-APP-002:** the Marketplace also sells themes (domain E), and its Vendor Agreement and payout are
  cited in the PTN tree (CM-PTN-001, CM-PTN-003).
- **WC-C-086 in CM-APP-006:** the extension runs in the merchant's install; the concern holds a compatibility
  declaration and admin REST controllers that aren't admin UI.
- **WC-C-112 in CM-PTN-005:** most of the concern is the Marketplace's category Business services and its ten
  subcategories (Insurance, Law, Finance and others). Whether their listings are partners' services or extensions isn't
  stated. If they are extensions, the category belongs in CM-APP-002 as `extension-point`, and the concern splits.

### Placements I want the reviewer to see

- **The Marketplace is `core`, not `own-service`.** The Vendor Agreement names WooCommerce, Inc. as a party and
  "WooCommerce" as the one that collects revenue and pays the Partner (WC-S-0576, WC-S-0580), and the admin has its own
  menu WooCommerce > Extensions (WC-S-0046) and an onboarding tour of the Marketplace (WC-S-0432). I read it as the
  platform's own marketplace, as the anchor read the App Stores. If the reviewer reads WooCommerce.com as a separate
  service of the company, CM-APP-002's and CM-APP-003's `core` rows become `own-service`.
- **CM-APP-011's `own-service`** (the checker's flag) rests on WC-S-0644, whose identifier is "5. Fees, Payment, and
  Renewal: a. Automattic Fees" and which counts "Woo themes or extensions" among "our Services". I read it as naming
  Automattic as their provider. The statement's note says the same, and counts for nothing.
- **CM-AIA-001 has no `core` or `own-service`.** Automattic "may offer" AI features (WC-S-0486), but no statement puts
  them in the plugin, the admin or a named service. `outside` rests on the AI providers: "some of our AI features may be
  powered by Anthropic and OpenAI" (WC-S-5347), and input is shared with third-party AI providers (WC-S-5349). Both
  companies are slot fillers.
- **CM-API-005 cites WC-C-031**, domain A's, which names F under also: rate limiting "is available for Store API
  endpoints. This is optional and disabled by default" (WC-S-5358), as `core`. It limits requests to the platform's own
  public Store API, not an app's calls to the REST API. Its checkout setting (WC-S-0932, WC-S-5360) is left to A, as
  the anchor kept Shopify's bot protection apart from API rate limits (U-045). If domain A's parts cite WC-S-5358 as
  `core`, the merge flags it; the coordinator decides which domain keeps it.
- **CM-API-007, bulk operations, cites a batch.** The webhooks API takes "a batch, of webhooks" (WC-S-0683). Nothing
  held shows WooCommerce's batch as asynchronous, or a topic when it ends, as Shopify's bulk operations are. The same
  batch is stated for products, orders, customers, coupons and others (WC-C-064, WC-C-070, WC-C-073, WC-C-074, and
  more), of other domains without F under also, so I left them uncited. If the reviewer reads a synchronous batch as a
  different thing, the cell becomes `none-held` and "batch" goes among the homonyms.
- **The readme against the Terms on vetting.** The readme says "Our developers [vet each new extension]" (WC-S-0596,
  `core` in CM-APP-002). The Terms say "Third-Party Services aren't vetted, endorsed, or controlled by Automattic"
  (WC-S-0487, `shows` in CM-APP-001). I read the first as the Marketplace's review of what it lists and the second as
  the Terms' general rule for any third-party service. Both are cited as they stand.

### Proposed renames, for the coordinator

- **CM-API-002, "App authorization":** WooCommerce's term is authentication, by API keys the merchant generates. I
  propose "API authentication and app authorization: how an app, or an external service, is allowed to call the
  store's API (Shopify API authentication; Salla Authorization, OAuth 2.0; WooCommerce Authentication, REST API keys)".
- **CM-APP-001, "Apps":** add WooCommerce's terms "extensions, WooCommerce > Extensions".
- **CM-APP-002, "App store":** add "WooCommerce Woo Marketplace, WooCommerce.com Marketplace".
- **CM-PTN-001:** add "WooCommerce Marketplace Vendor Agreement".
- **CM-AIA-004:** add "WooCommerce MCP".

## Concerns read under `also`

- **WC-C-031** (domain A, also C and F), checkout and Store API rate limiting: cited in CM-API-005 (above).
- **WC-C-005, WC-C-056, WC-C-061** (domain C, also F): the Marketplace's categories for payments, tax, and shipping.
  They would be `extension-point` in CM-APP-002 as more categories, but WC-C-017's category Extensions already stands
  for the Marketplace's categories, and their subject is their own domain's work. Left uncited.
- **WC-C-087** (domain C, also F), block and Store API extensibility: storefront and checkout extension points, no
  capability of F's admin or API trees. Left uncited.
- **WC-C-049, WC-C-117** (domain A, also F), the WordPress.com and Jetpack connection and its sync. They resemble
  CM-APP-012 (a connection of the store to a company account), but the connection serves Woo services such as
  WooPayments and Tax (WC-S-0464, WC-S-5335), not extensions from the Marketplace. Left uncited. The coordinator may
  want CM-APP-012 widened to cover both connections.

## Rulings

Every unclear candidate holding a concern I land: U-046, U-048, U-051, U-052, U-062 and U-066, one row per pair of my
concern and each Shopify or Salla concern of the candidate (36 rows). Summary:

- **U-046:** (WC-C-078, SH-C-171) and (WC-C-078, SA-C-190) `joined:CM-API-002`.
- **U-048:** (WC-C-086, SH-C-164) and (WC-C-086, SA-C-197) `joined:CM-APP-007`; (WC-C-086, SA-C-199)
  `joined:CM-APP-010`.
- **U-051:** (WC-C-017, SH-C-029) `apart`, scope.tsv gives SH-C-029 domain E; (WC-C-017, SA-C-208) `apart`: domain E
  with F under also, but no capability of F cites it or the Marketplace's Themes.
- **U-052:** WC-C-017 against SH-C-156 `nested:CM-APP-002`, against SH-C-157 and SA-C-194 `joined:CM-APP-002`, against
  SH-C-168 `joined:CM-PTN-001`, against SA-C-195 `joined:CM-APP-003`. WC-C-050 against SH-C-156, SH-C-157 and SA-C-194
  `nested:CM-APP-011`, against SH-C-168 `apart`, against SA-C-195 `joined:CM-APP-003`. WC-C-063 against SH-C-156 and
  SA-C-194 `joined:CM-APP-001`, against SH-C-157 `joined:CM-APP-002`, against SH-C-168 `apart`, against SA-C-195
  `joined:CM-APP-003`.
- **U-062:** WC-C-095 against SA-C-012 `joined:CM-AIA-004`, against the rest `apart`. WC-C-096 against SH-C-202 and
  SA-C-012 `joined:CM-AIA-001`, against SH-C-152 `nested:CM-AIA-002`, against SH-C-140 and SA-C-100 `apart`.
- **U-066:** (WC-C-112, SH-C-170) and (WC-C-112, SA-C-205) `joined:CM-PTN-005`; (WC-C-112, SA-C-303)
  `nested:CM-PTN-006`.

**Rulings that may change after the back-fill:** (WC-C-050, SH-C-156) becomes `joined:CM-APP-011` if the back-fill
cites SH-S-0738 there. The nested rulings on CM-APP-011 (SH-C-157, SA-C-194) change if the back-fill finds Shopify's or
Salla's own apps as a category of their App Store.

**U-083** (SH-C-151 against WC-C-110 and WC-C-113) holds no concern of mine: scope.tsv gives both WooCommerce concerns
domain D, without F under also, so D's WooCommerce part lands them and rules on it. By the brief's rule its ruling is
`apart`, with the basis "scope.tsv gives WC-C-110 (and WC-C-113) domain D". I wrote no row, since the checker asks a
part to rule only on candidates holding concerns it lands, and a row here would duplicate D's. CM-AUT-001's WooCommerce
cell is `none-held`; the Automation category (WC-S-0756) is the hit it answers (flags, line 31).

## What the checker flagged

**0 problems, 18 flags.**

1. **evidence line 79, `own-service` on WC-S-0644:** see "Placements" above.
2. **cells line 3, CM-AIA-002 none-held (WC-S-0918):** that is MCP access for outside assistants, in CM-AIA-004, not an
   assistant in the admin.
3. **line 4, CM-AIA-003 (WC-S-0931, WC-S-0888, WC-S-0921):** "generate" a webhook signature and API keys.
4. **line 9, CM-API-003, `core` only on boundary statements:** the access levels are WooCommerce's own API's, `core`
   by the dry run's C1.
5. **line 10, CM-API-004 (18 hits):** Marketplace developers get no customers' personal information (WC-S-5340, in
   CM-APP-002); PCI, controllers, remote logging, privacy settings and erasers are domain A's; the Store API's lack of
   sensitive data is domain E's. None is the platform approving an app's access to buyers' data.
6. **line 13, CM-API-007, `core` only on a boundary statement:** the webhooks API's batch (WC-S-0683) is WooCommerce's
   own API, `core` by C1. Whether a batch is a bulk operation at all is the question under "Placements" above.
7. **line 17, CM-API-011 (15 hits):** the store's privacy exporters and erasers (WC-C-045, domain A), not topics sent to
   an app.
8. **line 22, CM-APP-004 (4 hits):** Jetpack features "activated or not", WooCommerce's own installation, and a VAT
   setting "if activated".
9. **line 26, CM-APP-008 (16 hits):** WooPayments, shipping labels, meta boxes, the order actions API, Blueprint: the
   platform's own features, not extensions' blocks or actions on admin pages.
10. **line 31, CM-AUT-001 (9 hits):** the Marketing > Automation category and MailPoet (domain D, U-083), checkout
    "flow", automated tax, notification "triggers" of an extension (WC-C-106, domain D).
11. **line 32, CM-DVT-001 (4 hits):** links to documentation inside settings and a tax guide; none names developer tools.
12. **line 33, CM-DVT-002 (9 hits):** "click" matches "CLI". The WC-CLI command is in CM-APP-012 (homonyms above).
13. **line 34, CM-DVT-003 (12 hits):** "stores" in its ordinary sense (data stores, the Marketplace's "online stores").
14. **line 38, CM-PTN-002 (104 hits):** "Settings", "Verified" and the like in their ordinary senses; the Vendor
    Agreement is in CM-PTN-001.
15. **line 40, CM-PTN-004 (9 hits):** WooPayments' VAT and JCT invoices to merchants, the order email, Xero's invoices.
16. **line 43, CM-PTN-007 (1 hit):** product customs data (domain C).
17. **line 44, CM-PTN-008 (1 hit):** "European Commission".
18. **line 45, CM-PTN-009 (9 hits):** marketing campaigns, order attribution and WooAds (domain D), and "the creators
    of WordPress.com".

`none-held` stands in each.

## For the back-fill

F-backfill-woocommerce writes Shopify's and Salla's cells for CM-APP-011, CM-APP-012 and CM-API-012. Leads, not
evidence: SH-S-0738 (apps made by Shopify) for CM-APP-011.

## Gaps: statements needed and not held

- Where Automattic's AI features sit (in the plugin, the admin, or a separate service), and which they are.
- Which extensions are Woo's: no list is held. Notes on other concerns' statements say some extensions are listed in
  Developed by Woo (for example WC-C-106/decides/WC-S-5481); a note counts for nothing.
- Whether the Business services category's listings are services or extensions, and what the Woo Agency Partner
  programme is, beyond its review and directory.
- A partner dashboard, account or payout record for Marketplace vendors.
- A change log, and when a REST API version is added or retired.
- Any limit on the REST API's requests.
- What `declare_compatibility` and `woocommerce_admin_rest_controllers` are for, in a statement.
- What REST API caching caches, and how long.
- Q1's own gaps on these concerns: no reason found for any of them; who is responsible stated only in general terms
  for WC-C-063, WC-C-077, WC-C-078, WC-C-086, WC-C-095 and WC-C-112; no boundary for WC-C-050.

## Problems with the brief or the evidence

1. **Two keys for one statement.** The checker tests a statement's tree by its key, so citing the same statement under
   two of its keys in two trees (WC-S-0580) passes unflagged. I chose the key whose placement fits each capability and
   reported it here; the anchor noted the same with SH-S-5028.
2. **A mapping part's rulings on capabilities it adds.** The nested rulings on CM-APP-011 rest on Shopify's and Salla's
   cells in its ancestors, because the back-fill hasn't written their cells in it. They are true of the model now and
   may change after the back-fill, which the brief doesn't ask to revisit rulings.


## The coordinator's corrections (30 October)

- **U-052, (WC-C-050, SH-C-156):** `joined:CM-APP-011`, since the back-fill cites SH-S-0738 there. The pairs with SH-C-157 and SA-C-194 stay `nested`.

## The coordinator's correction after E-woocommerce batch 1 (30 October)

- **WC-S-0644 counts once.** Automattic's terms name Woo themes and extensions among its paid Services. It was `own-service` here and in E's CM-SFR-003, the theme marketplace, whose WooCommerce cell rests on it alone. It stays there and is `shows` here; CM-APP-011's WooCommerce cell stays `core` on the category Developed by Woo (WC-S-0697).
