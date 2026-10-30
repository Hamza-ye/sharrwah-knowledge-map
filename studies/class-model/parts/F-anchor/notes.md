# F-anchor: notes

The anchor part of domain F, Platform and ecosystem (areas APP, API, DVT, PTN, AUT, AIA), from Shopify's and Salla's
concerns that `scope.tsv` gives the domain: 19 Shopify and 22 Salla. It runs in four batches
(`class_slice.py batches --domain F --platforms shopify,salla`). Every row is a reading of the statements its keys cite;
a fact is only what a cited statement says. Where the brief left a choice to me, this file says so ("my judgment").

## Batch 1: area APP (apps and extensibility)

**Concerns:** SH-C-019, SH-C-156, SH-C-157, SH-C-163, SH-C-164, SH-C-167; SA-C-175, SA-C-193, SA-C-194, SA-C-195,
SA-C-196, SA-C-197. This batch created the part's files.

**Result:** 9 capabilities, all in APP and all in one tree under CM-APP-001; 12 landings (8 joined by a Q1 match, 1 by
identifier, 2 on role, SH-C-164 into the parent CM-APP-006 and SA-C-197 into CM-APP-007, and 1 single); 18 cells (16 held, 2 none-held, both Salla's);
134 evidence rows; 4 qualities; no slot fillers; 5 rulings. Check:
`python3 -I method/check_class_part.py studies/class-model/parts/F-anchor --concerns <the twelve> --areas APP`:
0 problems, 3 flags, answered below.

### How I cut, and why

**One tree under apps.** CM-APP-001, a store's apps, is the parent of the other eight. Both platforms keep a store's apps
as one admin place (Shopify's Apps section, apps routes and the permissions APPLICATIONS and LIMITED_APPLICATIONS;
Salla's dashboard app @salla.sa/ui-merchant-apps at /apps, with My apps at /apps/installed and the permission
marketplace_apps_management), and their own groupings put the rest under it, which is the dry run's rule for `parent`:
- Shopify: the admin's Apps section holds App development (SH-S-7143, `"section":"Apps"`); the staff permission group
  Apps and channels holds Approve app charges (SH-I-1008); the help center's apps manual holds Finding and choosing apps
  and App extensions and functions (SH-I-2101, SH-I-2104); an App Store app contains its functions (SH-S-0682);
  admin UI extensions embed "your app's functionality" (SH-S-0711).
- Salla: /apps is the App Store and /apps/installed is My apps (SA-S-1884, SA-S-1883); its App API holds an app's
  Subscriptions (SA-S-1077) beside its Settings and App Details Builder; App Functions and the Embedded SDK are named for
  apps (SA-S-0187, SA-S-0197); App Events are "about the apps you develop" (SA-S-5093).

The two platforms' groupings differ only for the app store, which Shopify keeps on its own site (SH-S-2753) and Salla in
the dashboard; both still place finding apps under apps, so CM-APP-002 is a child.

**The capabilities.** Each has a place of its own on at least one platform (the dry run's rule):
- CM-APP-001 apps: the admin sections above, a Shopify plan line (SH-S-7052).
- CM-APP-002 app store: Shopify's App Store and Partner Dashboard App distribution; Salla's App Store link and its policy page.
- CM-APP-003 app charges billed through the platform: Shopify's Billing API and billing routes; Salla's App Subscriptions
  and the App API's Subscriptions folder.
- CM-APP-004 app lifecycle events: Shopify's webhook topics and Partner API App Events API; Salla's App Events.
- CM-APP-005 functions: Shopify's API group Shopify Functions and a plan line; Salla's docs section App Functions and its
  event folders.
- CM-APP-006 app UI in the admin, parent of CM-APP-007 (an app's own page) and CM-APP-008 (extensions on the admin's
  own pages): Shopify's App Home APIs and app_home target, its admin extension targets; Salla's Embedded SDK folder.
- CM-APP-009 custom apps: Shopify's App development routes, permissions and plan line.

**Grains I chose (my judgment):**
1. *M-067* (SH-C-156, SH-C-157; SA-C-194, SA-C-175). Shopify splits apps in general from the App Store; Salla splits the
   App Store with the store's installed apps (SA-C-194) from its publishing policy (SA-C-175). I made apps (CM-APP-001)
   and the app store (CM-APP-002) two capabilities, parent and child: SH-C-156 lands in CM-APP-001, SH-C-157 in
   CM-APP-002; SA-C-194, holding both the App Store and My apps, is coarser and lands in the parent, its App Store link
   and categories cited in the child; SA-C-175 lands in CM-APP-002. I made no capability for app review and publishing
   terms: neither platform gives review a place of its own (Shopify's is a passage of its docs, SH-S-0698; Salla's an
   article of its policy, SA-S-0023), so both are cited in CM-APP-002. App distribution (Shopify's Partner Dashboard
   item, SH-S-2852) is in CM-APP-002; its custom distribution (SH-S-0693) in CM-APP-009.
2. *M-010* (SH-C-019, SH-C-169; SA-C-195). Shopify keeps app charges (SH-C-019) apart from partner payouts (SH-C-169,
   area PTN, batch 3); Salla keeps both in SA-C-195. CM-APP-003 is the charge: the platform bills the merchant for an app
   and keeps a share. SA-C-195 lands there, strained (below), and its partner finances are left uncited for batch 3's
   partner payouts. The developer's share being paid out is cited here only as a term of the charge (SH-S-0282).
3. *M-070* (SH-C-163; SA-C-196). One to one, CM-APP-005. The definitions differ in what triggers the function (Shopify:
   invoked within the customer journey, SH-S-0683; Salla: on a store's events, some synchronous and blocking,
   SA-S-0187, SA-S-0189); both have the platform host and call app-written code, which is the capability. The function
   APIs of single features (Shopify's discount, delivery, payment, validation and cart transform functions, SH-C-052,
   SH-C-053, SH-C-083, SH-C-122 to SH-C-124, SH-C-128) are their domains' (C and D, F under also), not cited here.
4. *SH-C-164 against SA-C-197* (U-048). Shopify's concern holds two forms, App Home and admin UI extensions on core
   admin pages; Salla's Embedded SDK is an app's own page in an iframe. I made a parent (CM-APP-006) and two children:
   SH-C-164 lands in the parent, SA-C-197 in CM-APP-007, an app's own page, joined on role with Shopify's App Home.
   CM-APP-008, extensions on the admin's own pages, is Shopify's only.
5. *SA-C-193* (App Events) lands in CM-APP-004 by identifier, not by M-071. M-071 joins it to Shopify's Partner Program
   (SH-C-168) because Shopify keeps its App Events API inside that concern, a difference of grain. SH-C-168 is area
   PTN's (batch 3). A landing by `match:M-071` would fail the checker's match test once SH-C-168, SA-C-204 and SA-C-176
   land in PTN, so I joined on the identifiers both sides share (Salla's app.uninstalled and Shopify's app/uninstalled;
   app.subscription.started and app_subscriptions/update) and cite SH-C-168's App Events API entries in CM-APP-004's
   Shopify cell (SH-I-0075, SH-I-0171). Both platforms place app events on the partner's side (SA-S-5093, "partner
   portal events"; Shopify's Partner API); I put the capability under apps, which its events are about, as the partner
   programme has no capability yet in this part.

**Placements in APP (my judgment).** Every capability here is itself a means the platform gives third parties, so I read
the four values this way, the same for both platforms:
- `core`: a statement naming the platform's own admin section, route, staff permission, plan line, API group, webhook
  topic or runtime for the capability (the dry run's rule on the platform's own API, a guide to developers included);
- `extension-point`: a statement showing third parties doing the capability's work through it (developers writing
  functions, an app's functionality on admin pages, a third-party application in an iframe, apps by third-party
  developers, partners' apps hosted on the infrastructure), an app-store category, an extension target, or a route
  named for each application;
- `shows`: terms, responsibilities, consent, reasons and unreleased gates.

I read "Apps that are made by Shopify are usually free and are supported by Shopify" (SH-S-0738) as `shows`, not
`own-service`: those apps do other domains' work, and CM-APP-001 is the means of installing apps, which they don't
provide. "Salla also offers connected products such as … an app marketplace" (SA-S-0002) is `shows`: it names the
platform's name as offering it, not the company as the maker of a separate product, and Salla's dashboard link already
places its App Store as `core`.

### Joins on role

- **CM-APP-006 and CM-APP-007:** Shopify's App Home (the app_home target and the App Home (iframe) API, SH-S-2182,
  SH-I-0054) and Salla's Embedded SDK page (a third-party application running in an iframe in the Merchant Dashboard,
  SA-S-0197, at /{app-name}, SA-S-3581). Neither side defines the other's term; both are an app's own page inside the
  admin. SH-C-164's landing in the parent is joined on the same role with the same keys.

### Homonyms kept apart

- **"App" for the store's own mobile app.** Salla's app maker (SA-C-094: app_builder_management, صانع التطبيقات, the
  plan line تطبيق خاص بمتجرك, SA-S-2192) and its publishing policy for Google's and Apple's stores (SA-C-174, domain E,
  and SA-S-5114, سياسة نشر التطبيق في متجر التطبيقات, a statement of SA-C-232, domain A) are about the store's own
  shopping app, the app maker of domain E. "متاجر التطبيقات" there
  means Google's and Apple's app stores, not Salla's App Store (CM-APP-002). Not cited.
- **"Widget" on Salla** names storefront web components (SA-C-091: salla-filters-widget, SA-S-1445), not extensions in the
  admin. Not cited.

### Strained fits

- **SA-C-195 in CM-APP-003.** It holds app charges and the partner's finances. Cited here: a paid app's payment through
  Salla, Salla's share, App Subscriptions and the App API's Subscriptions folder (SA-S-0025, SA-S-0026, SA-S-1927,
  SA-S-1077). Not cited, for batch 3's partner payouts: Payouts, Billings and Operation records (SA-S-1936 to
  SA-S-1938), the Billing System Salla partners with its monthly invoices for apps, paid by bank transfer (SA-S-1174,
  SA-S-0046, SA-S-0045), payout after the 15-day refund period and Salla's periodic reports (SA-S-0027, SA-S-0034), and
  the payout statuses (SA-I-1946 to SA-I-1951). What the partner invoices charge for isn't stated (a gap below).

### Concerns read under also, and other concerns cited

- Cited across concerns of domain F: SH-C-168 (batch 3's) for its App Events API entries (SH-I-0075, SH-I-0171) in
  CM-APP-004; SH-C-019, SH-C-156 and SH-C-157 in sibling capabilities under CM-APP-001.
- Read, not cited: SA-C-199 (App settings, batch 2's), to rule on U-048 (below); SA-C-094, SA-C-174, SA-C-232 and
  SA-C-091, which my searches found (homonyms above). No statement of another domain is cited.

### Rulings

- **U-048:** (SH-C-164, SA-C-197) `joined:CM-APP-007`. The pair (SH-C-164, SA-C-199) is left to batch 2, which lands
  SA-C-199: a ruling follows the cells, and SA-C-199's are not written. Its statements (SA-S-0210: "The App Settings are
  custom-made parameters by the Salla App Developer"; SA-S-1076, the App API's Settings folder) are not an app's page or an
  extension on the admin's pages, so I see no join with CM-APP-007 or CM-APP-008; whether app settings nest under
  CM-APP-001 or CM-APP-006 is batch 2's cut.
- **U-052:** (SH-C-156, SA-C-194) `joined:CM-APP-001`; (SH-C-157, SA-C-194) `joined:CM-APP-002`; (SH-C-156, SA-C-195)
  `nested:CM-APP-003`; (SH-C-157, SA-C-195) `joined:CM-APP-003`. The pairs (SH-C-168, SA-C-194) and (SH-C-168, SA-C-195)
  are left to batch 3, which lands SH-C-168. The checker asks for one ruling per candidate, so it won't report these
  pairs missing.

### What the checker flagged

1. *cells.tsv line 12, CM-APP-006 for Shopify: core rests only on boundary statements.* It rests on Polaris references
   (SH-S-0817), Shopify's own reference of UI components for apps in its admin: its own API for its own feature, `core`
   by the dry run's rule. Shopify hosting an app's UI is also shown in the child CM-APP-007 (the admin route
   apps:embedded_parent, a `where` statement, and the App Home APIs).
2. *cells.tsv line 17, CM-APP-008 for Salla, none-held with 8 matches.* Six are storefront web components found by
   "widget" (SA-C-091: SA-S-1420, SA-S-1445, SA-S-1448, SA-S-1529, SA-S-1537, SA-I-0445), not admin extensions. Two are
   the flag app-actions-history (SA-S-3419, SA-I-2419), found by "app-action": a released flag whose name doesn't say
   what it records or where, so not evidence. none-held stands.
3. *cells.tsv line 19, CM-APP-009 for Salla, none-held with 2 matches.* تطبيق خاص بمتجرك (SA-S-2192, SA-I-1192) is the
   app maker's own-store mobile app, a homonym (above). none-held stands.

### For the later batches

- **Batch 2 (APP, API).** It may add evidence to this batch's cells where its concerns bear on them. SH-C-158's
  app/scopes_update (SH-C-158/boundary/SH-S-1152) is the counterpart of Salla's app.store.authorize, in CM-APP-004.
  CM-APP-001 cites SH-C-156's grant routes (SH-S-5035, SH-S-5039) and the merchant's approval of scopes at install
  (SH-S-0755); CM-APP-002 cites SH-C-157's approval of protected customer data (SH-S-0694) as `shows`. If an API
  capability cites these keys too, SH-C-156 or SH-C-157 becomes strained (S1), and the coordinator corrects the landing
  here. The pair (SH-C-164, SA-C-199) of U-048 is batch 2's.
- **Batch 3 (DVT, PTN).** SH-C-169 (partner payouts) can't land by `match:M-010` unless its capability is in
  CM-APP-003's tree; outside it, a join by terms (Payouts) with SA-C-195's payout statements, left uncited for it, keeps
  the checker's match test. SH-C-168 can land by M-071 with SA-C-204 and SA-C-176; since CM-APP-004 cites its App Events
  API, its fit is strained, and the checker will flag M-071 across two trees (a difference of grain, answered here).
  The pairs (SH-C-168, SA-C-194) and (SH-C-168, SA-C-195) of U-052 are batch 3's.

### Gaps: statements needed and not held

- Salla: nothing on apps' extensions on the dashboard's own pages, or on apps a store develops for itself (the two
  none-held cells).
- Salla: what the Billing System Salla partners' monthly invoices for apps charge the partner for (SA-S-0046, SA-S-0045
  say only that they are generated and paid).
- Salla: which navigation holds My Apps at /apps (SA-S-1906, list 2) and App Subscriptions at /subscriptions/apps
  (SA-S-1927): the merchant's dashboard or the Partners portal. The statements don't say, and I didn't read their
  structures. SA-S-1906 is not cited for that reason; SA-S-1927 is cited as Salla's own navigation either way.
- Salla: the plan-feature entries ربط الخدمات الإضافية and الربط مع الخدمات الإضافية (SA-I-1098, SA-I-1147), placed in
  SA-C-194, hold no plan and no definition; the plan table that lists them would show both. Not cited.
- Shopify: the App Store's categories, its App Home APIs and its admin extension targets are held only as inventory
  entries, cited by id.
- Shopify: the store entitlement appDevelopment (SH-I-2551, unplaced) bears on CM-APP-009 but is an entitlement, not a
  limit, so not a quality; its values per store are in Q1's notes on unplaced keys. Not cited.
- Uncited by choice: SA-C-196's 75 event rows (its folders Merchants Events and Customers Events are cited); SA-C-194's
  flags other than SA-S-3208, whose names don't define what they gate; SH-C-019's route SH-S-5063 and its client gate
  SH-S-5067; SH-C-156's error route SH-S-5036 and the API license's preamble (SH-S-0214, the API area's); and keys that
  repeat a statement already cited under another concern's key.

### Problems with the brief or the evidence

1. **Pairs across batches.** The brief has each batch rule on its concerns' candidates, one row per pair, and a ruling
   follows the cells. A pair whose other concern lands in a later batch can't be tested on cells that don't exist yet, and
   a later batch can't rewrite this batch's rows. I left those pairs to the batch that lands the other concern (three
   pairs, above). The checker asks for one ruling per candidate, so only these notes keep track of them.
2. **Matches across areas.** M-010 and M-071 join concerns that this part puts in different areas (APP and PTN). The
   checker's test that a landing by match sits with another of the match's concerns runs on the whole part at the end,
   so a batch landing by such a match can pass now and fail later. That is why SA-C-193 lands by identifier.
3. **Placements in APP** are readings for nearly every cell, since each capability is the platform's means for third
   parties; my rule for them is above, for the reviewer to confirm or correct.

## Batch 2: areas APP and API (apps' settings; APIs, webhooks and events)

**Concerns:** SH-C-158, SH-C-159, SH-C-160, SH-C-161, SH-C-162, SH-C-171; SA-C-190, SA-C-191, SA-C-192, SA-C-199,
SA-C-201, SA-C-202. Appended to the part's files; no earlier row rewritten.

**Result:** 12 capabilities: CM-APP-010 in APP, under CM-APP-001; CM-API-001 to CM-API-011 in API, one tree under
CM-API-001. 12 landings, all in new capabilities (6 by a Q1 match, 2 by terms, 4 single); 24 cells (19 held, 5 none-held);
92 evidence rows (one added to batch 1's cell CM-APP-004 for Shopify, below); 4 qualities; no slot fillers; 5 rulings.
Check: `python3 -I method/check_class_part.py studies/class-model/parts/F-anchor --concerns <the twelve> --areas APP,API`:
0 problems, 9 flags (3 of them batch 1's, answered there), the others answered below; a tenth, on SH-C-162, went once I
made it strained.

### How I cut, and why

**One tree under the API.** CM-API-001, the developer API, is the parent of the other ten. Both platforms list the API's
conventions and its webhooks as entries of one list (the platforms' shared grouping, the dry run's rule for `parent`):
- Shopify's API resources: GraphQL Admin API, API authentication, Access scopes, Limits, Versioning, Bulk operations,
  Webhooks (SH-I-0044, SH-I-0030, SH-I-0031, SH-I-0036, SH-I-0029, SH-I-0006, SH-I-0027), and the docs labels Access
  scopes, Versioning, Bulk operations, Webhooks (SH-S-0795, SH-S-0793, SH-S-0770, SH-S-0791);
- Salla's API docs pages, each with `parentId` 841847: Authorization, Rate Limiting, Versioning, Change Log, Webhooks,
  Conditional Webhooks (SA-S-1013, SA-S-1001, SA-S-1002, SA-S-1014, SA-S-1008, SA-S-1009).

I didn't put the API under apps (CM-APP-001), though both platforms address it to apps (SH-S-0757; SA-S-0186): their
own grouping of it is the API's list, not their apps sections. Scopes and authorization could be read either way, since
Shopify's admin grant routes (app/grant, oauth/request_grant, SH-C-156's) sit in its apps routes and Salla's App Scope is
set in an app's setup in the Partners Portal (SA-S-5090); I followed the grouping both share (my judgment). The cost is
two strained fits (below), where batch 1 cites app-lifecycle topics.

**The capabilities.** Each has a place of its own on at least one platform:
- CM-API-001 developer API: Shopify's Admin API resources; Salla's Merchant API (an extension point).
- CM-API-002 app authorization: Shopify's API authentication; Salla's Authorization page and its link Salla OAuth 2.0.
- CM-API-003 access scopes: Shopify's Access scopes; Salla's App Scope and App Scopes Setup.
- CM-API-004 protected customer data, under scopes: Shopify's protected-customer-data page, Partner Dashboard request and
  its entry in the access scopes list (SH-I-2428).
- CM-API-005 rate limits: Shopify's Limits and two plan lines; Salla's Rate Limiting.
- CM-API-006 versioning and change log: Shopify's Versioning; Salla's Versioning and Change Log.
- CM-API-007 bulk operations: Shopify's Bulk operations and its topic bulk_operations/finish.
- CM-API-008 webhooks, parent of CM-API-009 (webhooks set up in the admin: Shopify's route under Settings > Notifications,
  Salla's Developer tools at /manage/webhooks with its plan line), CM-API-010 (conditional webhooks: Salla's page) and
  CM-API-011 (privacy compliance webhooks: Shopify's three mandatory topics).
- CM-APP-010 app settings, under CM-APP-001: Salla's App API folder Settings.

**Grains I chose (my judgment):**
1. *M-073* (SH-C-171; SA-C-201, SA-C-202). Shopify keeps all the API's conventions in one concern; Salla splits rate limits
   and versioning. SH-C-171 lands in the parent CM-API-001, its entries cited in the children; SA-C-201 and SA-C-202 land
   in CM-API-005 and CM-API-006. SH-C-171's Global IDs and GraphQL pagination are conventions with no place on Salla
   beyond its unplaced Responses and Pagination pages (SA-I-0003, SA-I-0004, outside Q1's concerns), so they stay in the
   parent's cell, not capabilities of their own. Bulk operations has a place of its own (an API resource, a webhook topic),
   so it is one, Shopify's only so far.
2. *M-068* (SH-C-158; SA-C-191), one to one, CM-API-003. SH-C-159 (scopes that need Shopify's approval) is finer, and lands
   in CM-API-003 too, by terms: its only place is a type in the scopes' legend and a sentence on where it is requested
   (SH-S-0756, SH-S-7248), not a place of its own. SH-C-160 (protected customer data) has its own page, request and scope
   entry, so it is a child, CM-API-004.
3. *M-069* (SH-C-162; SA-C-192), CM-API-008. Both concerns also hold a merchant's webhooks set up in the admin without an
   app; both platforms give that an admin route, and Salla a plan line, so it is a child, CM-API-009. Both concerns land in
   the parent, being coarser. SA-C-192 also holds Conditional Webhooks (CM-API-010).
4. *SA-C-190 against SH-C-171* (U-046). Authorization has a page of its own on both (Shopify's API authentication, Salla's
   Authorization), so it is a capability, CM-API-002, and SA-C-190 lands there by the term authentication (SA-S-0176: "the
   primary method for authorization and authentication"; SH-I-0030: "API authentication").
5. *SH-C-161* (mandatory compliance webhooks) is a child of webhooks, in API, though it is about apps' privacy duties: its
   place is the webhook topics list and the app's webhook configuration (SH-I-0433, SH-S-7256).
6. *SA-C-199* (app settings) is in APP, under CM-APP-001: Salla's App API holds Settings beside the Subscriptions that
   batch 1 cites in CM-APP-003, and the App Events include app.settings.updated. It isn't under CM-APP-006 (an app's UI in
   the admin): its statements say what the settings are (parameters the developer makes) and where the API holds them,
   not where they are shown.

**Placements (my judgment, the same rule as batch 1's).** The platform's own API resource, docs page, route, scope,
webhook topic, plan line or staff permission is `core`, a guide addressed to app developers included: Shopify's "your app
... can subscribe to Shopify webhook topics" (SH-S-0685) is Shopify delivering events, so `core`, not `extension-point`.
`extension-point` only where third parties do the work: Salla's App Settings, "custom-made parameters by the Salla App
Developer" (SA-S-0210). Reasons, responsibilities, the merchant's approval and a partner's permission are `shows`.
Salla's released flag webhooks (SA-S-3078, plans pro and special) supports `core`, by the dry run's rule, with its plans as
its scope; the flag webhook-channel (SA-S-3390) is not cited, since its name doesn't say what it gates.

### Joins on role

None. The two joins by terms (SH-C-159 into CM-API-003; SA-C-190 into CM-API-002) rest on the platforms' own words, but
each is a reading of what the shared word names, and the readings say so.

### Homonyms kept apart

- **"Settings" on Salla.** SA-C-199's Settings is the App API's folder for an app's settings; Salla's scope settings
  (SA-S-1545) and store-settings (SA-S-1565) are scopes of the API for the store's own settings, and its many admin
  settings routes are other domains'. Only SA-C-199's are cited in CM-APP-010.
- **"Bulk" on Salla** names the merchant's bulk edits in the dashboard (bulk-seo, customers-bulk-actions, Bulk status
  update), not bulk operations of the API (CM-API-007). Not cited.
- **"Conditional" on Shopify** names an admin extension target, Conditional admin action (SH-I-1436 to SH-I-1438), not a
  webhook (CM-API-010); on Salla, conditional offers and fields are storefront and marketing features. Not cited.

### Strained fits

- **SH-C-158 in CM-API-003.** Its topic app/scopes_update (SH-C-158/boundary/SH-S-1152) is cited in batch 1's CM-APP-004,
  app lifecycle events, in the apps tree: it is the counterpart of Salla's app.store.authorize there, as batch 1's notes
  asked. I added it as one evidence row to that cell; the cell's `terms` and `reading`, batch 1's rows, don't name it.
- **SH-C-162 in CM-API-008.** The checker found it: batch 1 cites two inventory entries Q1 placed in SH-C-162,
  app_purchases_one_time/update and app_subscriptions/approaching_capped_amount (SH-I-0390, SH-I-0391), in CM-APP-004.
  The webhook mechanism is CM-API-008's, the topics on an app's own lifecycle CM-APP-004's. If the reviewer prefers one
  tree, CM-APP-004 could be a child of CM-API-008; I left batch 1's tree as it is.

### Concerns read under also, and other concerns cited

- Cited across concerns: SA-C-193's app.settings.updated (SA-S-1656) in CM-APP-010, the same tree as its landing.
- The same statement under two concerns' keys, each key cited in its own concern's tree (no checker flag, for the
  reviewer): SH-S-0755 (the merchant approves scopes at install) under SH-C-156 in CM-APP-001 and under SH-C-158 in
  CM-API-003; SH-S-0694 (Shopify approves protected customer data) under SH-C-157 in CM-APP-002 and under SH-C-160 in
  CM-API-004; SA-S-0185 under SA-C-190 and SA-C-191, both in the API tree.
- Not cited, by choice: SH-C-156's grant routes (SH-S-5035, SH-S-5039) in CM-API-002, so that a key isn't cited in two
  trees; SH-C-161's rejection on review (SH-S-0698), cited by batch 1 under SH-C-157's key in CM-APP-002.
- Read, not cited: SA-C-171 (Salla's privacy policy, domain A without F under also), SA-C-066 (a store's privacy policy)
  and SA-C-234 (Merchant APIs - Operational on Salla's status page, SA-S-0047), which my searches found.

### Rulings

- **U-045:** (SH-C-171, SA-C-201) `joined:CM-API-005`; (SH-C-051, SA-C-201) `apart`: scope.tsv gives SH-C-051 domain A.
- **U-046:** (SH-C-171, SA-C-190) `joined:CM-API-002`.
- **U-047:** (SH-C-171, SA-C-203) `apart` for now: SH-C-171's only entry for it, Shopify.dev, Dev docs, CLI, and more
  (SH-I-1990), is cited nowhere, and the Salla CLI is batch 3's (DVT). The pair (SH-C-171, SA-C-209) has no ruling: the
  candidate's Shopify side for demo stores is the Partner Dashboard's Stores, in SH-C-168, and SH-C-171 holds nothing for
  it. The pairs (SH-C-168, SA-C-203) and (SH-C-168, SA-C-209) are batch 3's.
- **U-048:** (SH-C-164, SA-C-199) `apart`, batch 1's pair left to me: no capability cites both (SH-S-2182 in CM-APP-007,
  SA-S-0210 in CM-APP-010).

### What the checker flagged

1. *cells.tsv line 20, CM-APP-010 for Shopify, none-held with 255 matches.* They come from Salla's terms "Settings" and
   "App API": Shopify's admin settings routes and their eligibility (such as SH-S-5003, SH-S-5084), not app settings. My own
   searches found app-owned metaobjects (SH-S-6237), an app's own data, which needs no scope: not parameters the platform
   holds for an app (a reading). none-held stands.
2. *cells.tsv line 29, CM-API-004 for Salla, none-held with 26 matches:* privacy policies of the store and of Salla
   (SA-C-066, SA-C-171), the Maḥallī platform's privacy terms (SA-C-096), partner identity terms (SA-C-204) and a customer
   webhook (SA-C-060). None approves or bounds an app's access to buyers' data. none-held stands.
3. *cells.tsv line 35, CM-API-007 for Salla, none-held with 15 matches:* the dashboard's bulk edits (homonyms above).
   none-held stands.
4. *cells.tsv line 40, CM-API-010 for Shopify, none-held with 4 matches:* Conditional admin action and Filters (homonyms
   above). none-held stands.
5. *cells.tsv line 41, CM-API-010 for Salla: core rests only on boundary statements.* SA-S-1009 is Salla's own page of its
   API docs, Conditional Webhooks: its own API for its own feature, `core` by the dry run's rule. Q1 placed it as boundary.
6. *cells.tsv line 43, CM-API-011 for Salla, none-held with 21 matches:* privacy policies (SA-C-066, SA-C-171, SA-C-096,
   SA-C-174's consent label), not webhooks or requirements passing data subject requests to apps. none-held stands.
7. *landings.tsv, SH-C-162 clean with statements cited in CM-APP-004:* made strained (above), so the final check no
   longer prints it.
8. Lines 12, 17 and 19 are batch 1's cells, answered in its section.

### For the later batches

- **Batch 3 (DVT, PTN).** If a CLI or developer-docs capability cites SH-C-171's SH-I-1990 beside SA-C-203's keys, this
  batch's U-047 row (apart) no longer holds: the checker will report it, and the coordinator corrects it here; and SH-C-171
  becomes strained. Shopify's CLI, GitHub app, Stores and Libraries are unplaced API-resources entries (SH-I-0039 to
  SH-I-0043), which `outscope` reads; a cell can't cite them.
- Salla's Webhooks Log (SA-S-1941) and My Apps (SA-S-1906) are both in list 2 of a navigation whose owner isn't stated;
  batch 3's Partners portal cells may settle which navigation list 2 is.

### Gaps: statements needed and not held

- Salla: the table of rate limits by plan that SA-S-0171 introduces ("Use the table below for details"): the values
  aren't in the concern map, so CM-API-005 holds no quality for Salla. Q1's gap: where the limits are enforced (page not
  read).
- Salla: what a conditional webhook is; only the page's title is held (SA-S-1009).
- Shopify: what its API authentication is (OAuth, tokens): only the resource's name is held (SH-I-0030). Its grant routes
  are SH-C-156's.
- Shopify: no change log found (searched changelog; change log), and no definition of a bulk operation beyond the names.
- Salla: any approval of an app's access to buyers' personal data, and any topic that passes data subject requests to
  apps: none found (the none-held cells).
- Both: who answers for scopes, webhooks, authorization, settings and versioning is stated only in general terms on Salla
  (Q1's gaps); for Shopify, no reason is stated for scopes, approval scopes, protected data or webhooks.

### Problems with the brief or the evidence

1. **A batch 1 description to check.** CM-APP-001's Salla evidence calls marketplace_apps_management (SA-S-2629) "the staff
   permission"; the statement's note says it is a permission a partner can request on a merchant's store. Salla's staff
   permissions list is a separate list (as SA-S-2408 is for webhook_management, beside SA-S-2625, its partner twin). I
   didn't change batch 1's row; the coordinator may want the staff permission's own key there, if one is held.
2. **Rulings across batches** again: U-047 holds a concern of this batch and two of batch 3's. The checker asks for a ruling
   on the candidate, so I ruled the one pair I can test now and left the rest to batch 3, as batch 1 did for U-052.
3. **Trees and the strain test.** The checker tests strain by the concern of each cited key and of each inventory entry,
   so the same statement cited under two concerns' keys in two trees (SH-S-0755, SH-S-0694) isn't flagged, while an
   inventory entry Q1 placed in a concern is (SH-I-0390, SH-I-0391). I listed both kinds above for the reviewer.


## The coordinator's corrections (30 October)

- **CM-APP-001, Salla:** SA-S-2629 (marketplace_apps_management) is a permission a partner can request, by the statement's note, not a staff permission. By the dry run's S7 it is `shows`. The cell stays `core` on its other rows. (Batch 2's notes, problem 1.)

## Batch 3: areas DVT and PTN (developer tooling; partners and services)

**Concerns:** SH-C-168, SH-C-169, SH-C-170; SA-C-173, SA-C-176, SA-C-203, SA-C-204, SA-C-205, SA-C-206, SA-C-209, SA-C-303,
SA-C-304. Appended to the part's files; no earlier batch's row rewritten.

**Result:** 14 capabilities: CM-DVT-001 to CM-DVT-005 in DVT, in two trees (CM-DVT-001 with its child CM-DVT-002;
CM-DVT-003 with CM-DVT-004 and CM-DVT-005); CM-PTN-001 to CM-PTN-009 in PTN, one tree under CM-PTN-001. 12 landings, all in
new capabilities (5 by a Q1 match, 2 by terms, 1 on role, 4 single); 28 cells (23 held, 5 none-held, all Shopify's);
123 evidence rows; 4 qualities; no slot fillers; 10 rulings. Check:
`python3 -I method/check_class_part.py studies/class-model/parts/F-anchor --concerns <the twelve> --areas DVT,PTN`:
1 problem, on batch 2's U-047 row (below, for the coordinator), and 16 flags: 9 are batch 1's and 2's cells, answered in
their sections; the other 7 are answered below.

### How I cut, and why

**DVT: two trees.**
- *Developer tools and docs* (CM-DVT-001), parent of the CLI (CM-DVT-002). Salla's developer docs have a top-level menu Dev
  Tools whose folders are Partners Agent Kit, Salla Apps Playbook and Salla CLI (SA-S-1176 to SA-S-1179); Shopify's list
  of its products names Shopify.dev, "Dev docs, CLI, and more" (SH-I-1990). The CLI has a docs folder of its own with its
  commands (SA-S-1106, SA-S-1107, SA-S-1109), so it is a capability. The Agent Kit and the Playbook are held only as folder
  titles, with no definition: kept in the parent (my judgment), not made capabilities whose content no statement gives.
  I didn't put the tree under CM-API-001: Salla's Dev Tools is a menu of its own, not an entry of the API's folder 841847
  that batch 2 used for the API's tree, and Shopify's CLI is in its API resources list only as an unplaced entry
  (SH-I-0039), which a cell can't cite. If the reviewer reads the API resources list as the shared grouping, CM-DVT-001
  could be a child of CM-API-001.
- *Partner stores* (CM-DVT-003), parent of development stores (CM-DVT-004) and ready stores (CM-DVT-005). Salla's Partners
  portal has an item Stores whose children are Demo Stores, Ready Stores and Store management (SA-S-1931, SA-S-1932,
  SA-S-1933, each "parent": 27); Shopify's Partner Dashboard has an item Stores (SH-I-2086). Demo and ready stores each
  have a link of their own, so each is a capability; neither is shown under the other, so they are siblings (the rule for
  `parent`). SA-C-209 holds both, so it lands in the parent. The item Stores itself (SA-S-1930) is placed in no concern;
  Store management is SA-C-013's (domain A, F under also), not cited, since partner access to a merchant's store is that
  domain's capability.

**PTN: one tree under the partner programme** (CM-PTN-001). Both platforms keep a partner's work in one dashboard under
one agreement: Shopify's Partner Dashboard (Home, Stores, Payouts, Organization, Partner settings, Dev dashboard) and the
Partner Program Agreement; Salla's Partners portal (Dashboard, My Services, Affiliates, Influencer, Payments, Employees,
Settings, Chats, Help Center) and its joining policy. Its children each have a place of their own on at least one platform:
- CM-PTN-002 partner account: Shopify's Organization, Partner settings and the Partner API's Organization; Salla's
  Employees, Settings and its lists of identity types and statuses;
- CM-PTN-003 partner payouts: Shopify's Payouts and route partner-payouts; Salla's Payments > Payouts;
- CM-PTN-004 partner billing: Shopify's route partner-billing; Salla's Payments > Billings and Operation records, and its
  docs link Billing System Salla partners;
- CM-PTN-005 partner services for merchants, parent of CM-PTN-006 (the agencies' store-growth programme) and CM-PTN-007
  (the global selling programme): Shopify's plan subscription routes and the Partner Directory; Salla's Merchant Services,
  My Services and the two programmes' own pages;
- CM-PTN-008 the referral programme for the platform's plans, and CM-PTN-009 partner affiliates and influencers: Salla's
  agreement and help article, and its Partners portal menus Affiliates, Influencer and Marketing Tools.

**Grains I chose (my judgment):**
1. *M-071* (SH-C-168; SA-C-204, SA-C-176, SA-C-193). Shopify keeps the programme, its terms, the dashboard and the Partner
   API in one concern; Salla splits the partner account, the joining contract and app events. SH-C-168, SA-C-204 and
   SA-C-176 land in CM-PTN-001: SH-C-168 and SA-C-204 are coarser than the children (SA-C-204 holds the portal as well as
   the account); SA-C-176 is the programme's terms. SA-C-193 is in batch 1's CM-APP-004 (its section, grain 5).
   SA-C-176's SaaS contract is tied to an app and signable at publication (SA-S-0213, SA-S-0214), so it bears on app
   publishing (CM-APP-002); I cited it in CM-PTN-001 as the programme's terms so that SA-C-176 isn't cited in two trees.
2. *Identity verification and employees* are kept inside the partner account (CM-PTN-002), not capabilities of their own:
   only Salla shows either, and both are parts of the account in its portal.
3. *M-010* (SH-C-019, SH-C-169; SA-C-195), as batch 1 foresaw. Partner payouts are a capability of the partner programme,
   not of app charges: what Shopify distributes is the "Fees owing to its Partners" as well as what merchants owe them
   through the Billing Resource (SH-S-0295), and Salla's reports cover "commissions, earnings or amounts due" (SA-S-0034).
   SH-C-169 lands in CM-PTN-003 by the term Payouts with SA-C-195's Payouts link (SA-S-1936), not by M-010, whose other
   concerns are in CM-APP-003 (the match test). SA-C-195's payout and billing statements, left uncited by batch 1, are cited
   in CM-PTN-003 and CM-PTN-004. Billing has a place of its own on both (Shopify's partner-billing route; Salla's Billings),
   so it is a sibling of payouts. Salla's Payments menu (SA-S-1935, placed in no concern) groups the two; Shopify's routes
   share one eligibility (SH-S-5241). I didn't add a parent for them.
4. *M-072* (SH-C-170; SA-C-205), one to one, CM-PTN-005. Its parent is CM-PTN-001 by the grouping both share on the
   partner's side: Shopify's Partner Directory is set by the Partner Program Agreement (SH-S-0760, from partners/terms by
   citations.tsv), and Salla's My Services is in the Partners portal. The merchant's side is in each admin.
5. *SA-C-303 and SA-C-304* (U-066, U-076) have pages of their own on partners.salla.com, so each is a capability, under
   partner services for merchants: both are programmes in which the platform brings partners to merchants. Shopify's
   statements hold neither.
6. *SA-C-173 and SA-C-206.* Q1 split Salla's affiliate and referral programme for its own plans (SA-C-173) from the
   partners' affiliate and influencer menus in the Partners portal (SA-C-206). Both have places of their own, so I kept
   them as two capabilities, both under CM-PTN-001: SA-C-173's agreement is one of the Partners portal's legal pages
   (SA-S-0019, from partners.salla.com/legal/privacy-affiliate) and addresses "the partner member of the programme"
   (SA-I-2619). The two meet: the commission clause of the same agreement (SA-S-0043) is a statement of SA-C-206, cited in
   CM-PTN-009. What the Partners portal's affiliates market, a merchant's products or Salla's plans, isn't stated, so
   the reviewer may find CM-PTN-008 and CM-PTN-009 one capability; I left them apart, as Q1 did.

**Placements (my judgment, batches 1 and 2's rule).** The platform's own dashboard item, route, docs folder, API object,
released flag or its own act (reviewing, assigning, paying) is `core`. `extension-point` where third parties do the work
through what the platform provides: partners' services via the Partner Directory (SH-S-0760) or the Partners platform
(SA-S-0198, SA-S-0032), the Partners portal's places where partners list services, publish stores or market (SA-S-1911 to
SA-S-1913, SA-S-1932, SA-S-1915 to SA-S-1922), accredited agencies (SA-S-5125, SA-S-5126), and Salla connecting partners
with brands (SA-S-5130). Terms, conditions, responsibilities and unreleased flags are `shows`. I read the Salla CLI,
"developed by Salla team" (SA-S-5096), as `core`, the platform's own tool for building on it, like its own API, not
`own-service`: it does no merchant's work as a separate product. The reviewer may read it as maker evidence.

**Which navigation is Salla's "list 2".** citations.tsv traces SA-S-1903 to SA-S-1947 to
structures/salla/partners-portal-navigation (observed-sa@145f137), and SA-S-1883 to SA-S-1885 to the merchant dashboard's
navigation. So list 2 is the Partners portal's (batch 2's question, and batch 1's gap): My Apps (SA-S-1906), App
Subscriptions (SA-S-1927, cited by batch 1 in CM-APP-003 as core) and the Webhooks Log (SA-S-1941, cited by batch 2) are
the partner's side, not the merchant's. Batch 1's cell stays right ("Salla's own navigation either way"), but its terms
are the partner's view of the subscriptions, for the coordinator.

### Joins on role

- **CM-DVT-003 (SA-C-209's landing; U-047's pair (SH-C-168, SA-C-209)).** Shopify's Partner Dashboard item Stores
  (SH-I-2086) and Salla's Partners portal Stores, held through its children Demo Stores and Ready Stores (SA-S-1931,
  SA-S-1932). Each is the partner dashboard's own item for the partner's stores; neither side defines the other's term,
  and what Shopify's item lists isn't stated. Q1 named this pair in U-047's why_unclear.

### Homonyms kept apart

- **"Affiliate" on Shopify** names Shopify's own group companies and payment providers' affiliates in legal terms
  (SH-C-064, SH-C-066, SH-C-100, SH-C-181 and others), not affiliate marketing. Not cited.
- **"Accelerated" on Shopify** names accelerated checkouts (SH-C-074, SH-C-078), not Salla's growth acceleration
  programme (CM-PTN-006). Not cited.
- **"Stores" on Salla's Partners portal** holds Store management (SA-S-1933, SA-C-013), a partner's access to a merchant's
  store, beside the partner's own demo and ready stores. Not cited.
- **"Billing" on Shopify** names the merchant's bill with Shopify (SH-C-016, its billing charge categories) as well as the
  partner's (partner-billing). Only the partner's route is cited in CM-PTN-004; the charge categories Expert services fees
  and Professional services fees, placed in SH-C-016 and SH-C-170, are cited in CM-PTN-005 as `shows`.

### Strained fits

- **SH-C-168 in CM-PTN-001.** Its App Events API entries are cited in batch 1's CM-APP-004 (SH-I-0075, SH-I-0171) and its
  Partner Dashboard item Stores in CM-DVT-003 (SH-I-2086), two other trees.
- **SH-C-171 in CM-API-001 (batch 2's landing, clean).** The checker flags it: its entry Shopify.dev (SH-I-1990) is cited
  in CM-DVT-001 and CM-DVT-002. For the coordinator: it should be strained.
- **SH-C-158 in CM-API-003** (batch 2's, strained already): its key SH-C-158/boundary/SH-S-6300 is cited in CM-DVT-004.

### For the coordinator: an earlier batch's ruling that no longer holds

- **rulings.tsv line 10, U-047 (SH-C-171, SA-C-203), `apart`** (batch 2's). The checker prints it as a problem: CM-DVT-002
  cites both sides' keys, SH-I-1990 (Shopify.dev, "Dev docs, CLI, and more") and SA-C-203/where/SA-S-1179 (Salla CLI). The
  row foresaw this. The ruling should be `joined:CM-DVT-002`, with the same keys; I didn't rewrite it. It is this batch's
  only remaining problem.
- **Partner API.** CM-PTN-001's Shopify cell cites the Partner API (SH-S-0838, SH-I-0074) as the programme's own API. The
  seed (area API: "Admin, Storefront, Customer Account, Partner, Payments Apps APIs") and Shopify's API resources list put it
  beside the other APIs; area API isn't this batch's, so a child of CM-API-001 for it is the coordinator's choice. Salla's
  statements hold no partner API (searched Partner API; partners api).

### Concerns read under also, and other concerns cited

- Cited across concerns of domain F: SH-C-171's SH-I-1990 (CM-DVT-001, CM-DVT-002); SH-C-158's SH-S-6300 (CM-DVT-004);
  SA-C-195's payout and billing statements (CM-PTN-003, CM-PTN-004).
- The same statement under two concerns' keys, each in its own concern's tree (no checker flag, for the reviewer):
  SH-S-0282 and SH-S-0287 (SH-C-019's keys in CM-APP-003; SH-C-169's in CM-PTN-003); SH-S-0215 (SH-C-157's in CM-APP-002;
  SH-C-168's in CM-PTN-002); SA-S-0033 (SA-C-194's in CM-APP-001; SA-C-206's in CM-PTN-009).
- Read, not cited: SH-C-134 (Shopify Collabs) and SH-C-194 (Affiliate program apps), domain D without F under also, which
  my searches found for CM-PTN-009 (U-056 rules both apart); SH-C-110 (Managed Markets, domain E) and SH-C-065 (Global-e),
  for CM-PTN-007; SH-C-008 (the store owner's identity verification) and SH-C-009 (staff accounts), for CM-PTN-002;
  SA-C-013 (Store management, domain A, F under also), for CM-DVT-003. Of the concerns naming F under also, none but these
  bears on DVT or PTN: SA-C-208 (themes sold by partners, domain E) and SA-C-207 (Report Builder, domain D) are their
  domains' features delivered by partners; SA-C-235 (a partner unavailable, domain G) is operations.

### Rulings

- **U-047:** (SH-C-168, SA-C-203) `apart`: what they share is a prerequisite, a partner account (SH-S-0215, SA-S-5095), not
  the tool; (SH-C-168, SA-C-209) `joined:CM-DVT-003`, on role; (SH-C-171, SA-C-209) `apart`, the pair batch 2 left without
  a ruling. (SH-C-171, SA-C-203) is batch 2's row, which no longer holds (above).
- **U-052:** (SH-C-168, SA-C-194) `apart`; (SH-C-168, SA-C-195) `joined:CM-PTN-003`, on the Partner API's Transactions
  (SH-I-0175) and Salla's Payouts (SA-S-1936). With batch 1's four rows, the candidate's six Shopify–Salla pairs are ruled.
- **U-056:** (SH-C-134, SA-C-206) and (SH-C-194, SA-C-206) `apart`: scope.tsv gives both Shopify concerns domain D without F
  under also. A first draft cited Collabs (SH-S-0731, SH-S-0732) in CM-PTN-009's Shopify cell as `shows`; the brief's rule for
  such pairs ("Otherwise the ruling is apart") and the checker's apart test made me take them out, so the cell is
  none-held. Whether Collabs and Salla's partner affiliates are one capability is for the merge of D and F.
- **U-066:** (SH-C-170, SA-C-205) `joined:CM-PTN-005`; (SH-C-170, SA-C-303) `nested:CM-PTN-006`.
- **U-076:** (SH-C-110, SA-C-304) `apart`: scope.tsv gives SH-C-110 domain E without F under also.

### What the checker flagged

1. *rulings.tsv line 10* (a problem): batch 2's U-047 row, above.
2. *cells.tsv line 68, CM-PTN-006 for Shopify, none-held with 6 matches:* accelerated checkouts (homonyms above). none-held
   stands.
3. *cells.tsv line 69, CM-PTN-007 for Shopify, none-held with 34 matches:* Shopify's own selling abroad and its terms
   (Managed Markets' Global-e flow of funds, SH-S-0566; "Shopify is not the seller or merchant of record", SH-S-0013),
   VAT validation, multiple entities, and an export route of the merchant's billing (SH-S-5073). None is a programme for
   partners. none-held stands.
4. *cells.tsv line 70, CM-PTN-008 for Shopify, none-held with 10 matches:* "referred to as", "preferred", Collabs'
   commissions (SH-C-134, domain D), the charge category Partner application commission (SH-I-1336, SH-C-016, undefined).
   None is a referral programme for Shopify's plans. none-held stands.
5. *cells.tsv line 71, CM-PTN-009 for Shopify, none-held with 24 matches:* Shopify's group companies and payment providers'
   "affiliates" (homonyms above) and Collabs and Affiliate program apps, domain D's (Rulings, U-056). none-held stands.
6. *M-010's concerns land in more than one tree* (SH-C-169 in CM-PTN-003; SH-C-019 and SA-C-195 in CM-APP-003): a
   difference of grain, grain 3 above, as batch 1 foresaw.
7. *M-071's concerns land in more than one tree* (SA-C-193 in CM-APP-004): batch 1's grain 5; the other three are here.
8. *landings.tsv line 19, SH-C-171 clean with statements cited in CM-DVT-001 and CM-DVT-002:* batch 2's landing; it should
   be strained (above).
9. Lines 12, 17, 19, 20, 29, 35, 40, 41 and 43 are batch 1's and 2's cells, answered in their sections.

### For batch 4 (AUT, AIA)

- Salla's dashboard app @salla.sa/ui-merchant-partner-marketing (SA-S-3550, cited in CM-PTN-009) also routes experts and
  marketplace; no automation or AI statement among this batch's concerns. Partners Agent Kit (SA-S-1177, in CM-DVT-001) is
  held only as a title: if batch 4's statements define it as an AI kit (the seed's area AIA names Salla's "AI Agent Kit"),
  the coordinator may move its citation.

### Gaps: statements needed and not held

- Shopify: what its CLI does (only the words "Dev docs, CLI, and more", SH-I-1990; the entries Shopify CLI and Shopify GitHub
  app, SH-I-0039 and SH-I-0040, are unplaced); what a development store is and where it is created (only SH-S-6300 names
  one); what the Partner Dashboard's Stores lists.
- Salla: what the Partners Agent Kit and the Salla Apps Playbook hold (titles only); what a ready store holds, who prepares
  it and who buys it (only its review, SA-S-5111).
- Shopify: no statement names Hyperwallet, a term of SH-C-169; nothing on who the expert of the intro call is (Q1's gap:
  observation needed); nothing on what Shopify bills a partner for under partner-billing.
- Salla: what the partner invoices charge for (batch 1's gap); the global selling programme's FAQ answers (Q1's gap:
  observation needed); the reasons for the contract's, the agencies' and the referral programme's placements (pages not
  read); what the Partners portal's affiliates market.
- Both: no reason stated for the partner programme's placement (Shopify: searched, not found).
- Salla names two owning companies: شركة تطبيق سلة لتقنية المعلومات, CR 7011845513, in the joining policy (SA-S-0016), and
  شركة منصة سلة للاتصالات وتقنية المعلومات, CR 4031200589, in the affiliate agreement (SA-S-0019); the App Store policy
  (SA-S-0015, a statement of SA-C-195) gives the first name with the second number. Both are Salla's by their statements, so not slot
  fillers; which entity is the counterparty of each agreement is the coordinator's to read.

### Problems with the brief or the evidence

1. **An earlier batch's ruling in a later batch's check.** The checker tests every row of the part, so batch 2's U-047
   row prints a problem in this batch's check that this batch may not fix. The brief says to fix every problem; the
   coordinator's message says not to rewrite an earlier batch's rows. I followed the message.
2. **Rulings and other domains.** The brief's rule for a pair whose other concern is in a domain that doesn't name F under
   also ("the ruling is apart") sits uneasily with its rule that a cell may cite such a statement "where the cell needs
   it": a `shows` citation in the cell makes the checker read the pair as joined. I chose apart and none-held.
- **After batch 3:** U-047's pair (SH-C-171, SA-C-203) is `joined:CM-DVT-002`, since batch 3 cites SH-I-1990 there beside SA-C-203's keys. SH-C-171's landing is `strained` for the same citation. Both as batch 3's notes asked.

## Batch 4: areas AUT and AIA (automation and workflows; AI and agentic commerce)

Concerns landed: Shopify SH-C-151, SH-C-140, SH-C-152, SH-C-202; Salla SA-C-012. No capability existed in AUT or AIA, so all
six are new: CM-AUT-001, CM-AIA-001 to CM-AIA-005. Every reading below is mine, from the statements its keys cite.

### How I cut, and why

1. **CM-AUT-001, workflow automation (Shopify Flow).** One capability: Flow's admin permissions (category AUTOMATIONS), its
   product line Workflow Automation, its extension targets and its App Store category. The targets Flow trigger, Flow action,
   Flow template and the trigger lifecycle callback are how apps reach Flow, not a capability apart: a single platform shows
   them, and they have no place of their own beside Flow's.
   - **Maker:** no statement names Shopify's company as Flow's maker. "Shopify Flow" is a brand in a product's name, and
     Flow is installed from the Shopify App Store (SH-S-0753), so the cell claims no own-service. That is a gap.
   - **The admin link apps/flow:** no statement gives its eligibility, so the dry run's C4 can't place it; it is `shows`.
   - **Salla, none-held.** The seed's Salla leads for AUT are Auto assignment, Auto tags and Conditional Webhooks. Auto
     assignment is SA-C-043 (domain C, F under also), Auto tags is SA-C-040 (domain C) and Conditional Webhooks is SA-C-192
     (area API). Each is one feature's own automatic rule, not a tool where the merchant builds automations from triggers and
     actions, so none is the same object as Flow (a reading). The coordinator may want an amend part to test whether an
     order-rule capability belongs in C instead.
2. **CM-AIA-001, AI tools for merchants: a parent, a grain I chose.** Salla's one concern SA-C-012 holds its AI Connector,
   its AI agent app, its generators and other flags; Shopify cuts the same ground into Sidekick (SH-C-152) and Shopify Magic
   (SH-C-202). SA-C-012 is the coarser side, so it lands in the parent.
   - **The grouping (S2):** Shopify's help center keeps both Sidekick and Shopify Magic in its manual section ai-powered-tools.
     SH-S-0736's identifier is the path ai-powered-tools/sidekick.md; SH-S-7488's citation is ai-powered-tools/shopify-magic.md.
   - **Salla:** no Salla statement groups its AI features. Each is a flag, a setting or a dashboard app on its own; that is a
     gap.
   - **The children:** CM-AIA-002 (assistant), CM-AIA-003 (content generation) and CM-AIA-004 (AI connector). They keep
     SA-C-012 clean, since every key it cites is in one tree.
3. **CM-AIA-004 (AI connector) and CM-AIA-005 (agentic commerce) are apart.** Both platforms use the term MCP, but the
   statements don't show the same object:
   - **Shopify:** its UCP-compliant MCP servers serve commerce agents "that securely act on behalf of buyers" (SH-S-0714).
   - **Salla:** its AI Connector is a setting in the merchant's settings, whose ChatGPT step adds "a custom MCP server from
     Salla" (SA-S-5005). No statement says whom the assistant acts for, or what it reads or does.

   I put CM-AIA-004 under CM-AIA-001 because its setting is the merchant's own (a reading). CM-AIA-005 is top-level, since
   Shopify's grouping puts agentic commerce under apps (apps/agentic), not under its AI tools.
4. **CM-AIA-005, one capability for Shopify's agentic commerce.** It covers Agentic Storefronts, Sell in AI chats, the
   admin's Agentic section and UCP. They are one concern on one platform, and the terms of service tie them together
   (SH-S-0071, SH-S-0621), so I kept the grain coarse.
   - **The Agentic section:** it sits at apps/agentic, open only to APPLICATIONS or LIMITED_APPLICATIONS (SH-S-5028). By C4
     I read it as an app's page, `extension-point`.
   - **The plan line** Sell in AI chats, the UCP profile and Shopify's own channels are `core`.

### Joins on role

- **CM-AIA-002:** Shopify's Sidekick ("an AI-enabled commerce assistant in your Shopify admin", SH-C-152/where/SH-S-0736) is
  joined with Salla's dashboard app @salla.sa/ui-merchant-ai-agent at /ai-agent (SA-C-012/where/SA-S-3577). The Salla side
  also has the unreleased flag merchant-multi-agent-assistant (SA-S-3187). Salla names an AI agent and an assistant for the
  merchant but defines neither, so the role is a reading of the names and the place, the merchant's dashboard.
- **CM-AIA-001:** the landing of SA-C-012 is joined on role with Shopify's AI features in its admin (SH-S-7488).
- **CM-AIA-003:** this is a join by terms, not role: "AI-generated product descriptions" (SH-S-7206) against
  ai-description-generator (SA-S-3488).

### Homonyms kept apart

- **"Agent":** Shopify's "commerce agents" act on behalf of buyers (SH-C-140/where/SH-S-0714). Salla's "ai-agent" and
  "multi-agent-assistant" are the merchant's (SA-C-012/where/SA-S-3577, SA-C-012/decides/SA-S-3187). The capability notes
  of CM-AIA-002 and CM-AIA-005 say so.
- **"MCP":** this case is not shown to be a homonym, only not shown to be the same: SH-C-140/where/SH-S-0714 and
  SH-I-0073 (WebMCP Tools) against SA-C-012/boundary/SA-S-5005 and SA-C-012/decides/SA-S-3188. What would settle it is a
  Salla statement on whom the AI Connector's assistant acts for.
- **"Automations":** Shopify's Create marketing automations (SH-C-129, domain D, SH-S-7040) and the permission Marketing >
  View, create, and delete marketing activities and automations (SH-I-0936) are marketing's own. I didn't cite them in
  CM-AUT-001.

### Strained fits

None in this batch. Earlier I cited SH-I-1495 (App action) in CM-AIA-002. Q1 places that entry in SH-C-164 too, which
batch 2 landed in CM-APP-006, so the citation made that landing strained. I dropped it: the cell rests on SH-C-152's own keys
for App data and App action link.

### Concerns read under also, and other concerns cited

- **Read under also:** SA-C-043 (Auto assignment, domain C, F under also). I left it uncited (point 1 above).
- **Cited from other domains:** none.
- **Found but left uncited:**
  - SA-C-100's ucp-embedded-checkout (SA-C-100/decides/SA-S-3124, unreleased): domain C, without F under also. The ruling is
    apart and the cell none-held, as batch 3 did for such a case.
  - SA-C-020's ai-driven-personalized-product, ai-bundles and product-ai-enhance (domain B): they bear on products, not on
    this domain.
  - SA-C-220's Smart analytics (domain D): the seed's lead for AIA, but its statements don't say it uses AI.
- **Shared with SA-C-033 (SEO, domain E):** Salla's SEO plan line SA-S-2133 and the flag ai-seo-generator SA-S-3489 are
  statements of SA-C-033 as well. CM-AIA-003 cites SA-C-012's keys, and cites the plan line as `core`. If domain E's parts
  cite SA-C-033/decides/SA-S-2133 as `core`, the merge will flag one statement supporting core in two domains. The
  generation of SEO text with AI is both an SEO feature and an AI tool; the coordinator decides which domain keeps the
  `core`.

### Rulings

U-062 holds three Shopify concerns (SH-C-140, SH-C-152, SH-C-202) and two Salla concerns (SA-C-012, SA-C-100), so it needs
six rows:

| Pair | Ruling | Why |
|---|---|---|
| SH-C-140, SA-C-012 | apart | MCP, point 3 above |
| SH-C-152, SA-C-012 | joined:CM-AIA-002 | |
| SH-C-202, SA-C-012 | joined:CM-AIA-003 | |
| SH-C-140, SA-C-100 | apart | scope.tsv gives SA-C-100 domain C |
| SH-C-152, SA-C-100 | apart | the same |
| SH-C-202, SA-C-100 | apart | the same |

U-083 (SH-C-151 with WooCommerce's WC-C-110 and WC-C-113) holds no Salla concern, so the WooCommerce part rules on it.

### What the checker flagged

The whole part's check: **0 problems, 18 flags.** This batch's are lines 73, 81 and 83; the rest are earlier batches',
answered in their sections.

1. **Line 73, CM-AUT-001 for Salla, none-held with 156 matches.** The other platform's terms (Flow, workflow, trigger and
   others) match broadly: login and wallet "automatically", kyc_new_workflow, roles, rules, Auto tags and Auto assignment.
   None is a tool for building automations (point 1 above). none-held stands.
2. **Line 81, CM-AIA-004 for Shopify, none-held with 2 matches** (SH-S-0714, SH-I-0073). These are Shopify's MCP for
   buyers' agents, cited in CM-AIA-005 (point 3 above). none-held stands.
3. **Line 83, CM-AIA-005 for Salla, none-held with 6 matches:**
   - the audit log;
   - the Partners policies' word المحادثات ("conversations" between partner and merchant);
   - SA-C-100's ucp-embedded-checkout (SA-S-3124 and its entry SA-I-2124), of domain C;
   - the AI Connector's ChatGPT step (SA-S-5005), in CM-AIA-004.

   None shows buyers buying through AI. none-held stands.

### For the coordinator

- **SH-S-5028 is under two capabilities.** CM-APP-001 cites SH-C-156/decides/SH-S-5028, the apps list route, as `core`.
  CM-AIA-005 cites SH-C-140/decides/SH-S-5028, the route agentic:list, as `extension-point`. Both statements have the same
  first citation, SH-S-5028, which Q1's citations give as the admin router's line 14 (agentic:list). SH-C-156's note says the
  same eligibility is on more apps routes. The two keys are different statements with the same eligibility text. Whether
  CM-APP-001's citation should rest on an apps route's own cite is Q1's matter; neither row breaks the checker.
- **Partners Agent Kit (SA-C-203/where/SA-S-1177, in CM-DVT-001):** the statement's own field "to" is
  /ai-agent-kit/overview, so its route names an AI agent kit, as batch 3 asked. What it holds, and whether its agents are
  commerce agents like Shopify's "Build commerce agents with UCP" (SH-S-0714), isn't stated. I left it in CM-DVT-001, which
  holds developer tooling. A citation in AIA would make SA-C-203 strained.
- **SA-I-0198, AI-Driven Solutions** (an extension-points entry of SA-C-194): the concern map doesn't say what it is,
  possibly an App Store category. I left it uncited. If a statement shows it is an app category, it supports
  `extension-point` in CM-AIA-001, and SA-C-194's landing becomes strained.

### Gaps: statements needed and not held

- **Shopify:**
  - who makes Shopify Flow (no statement names the company);
  - Flow's responsible statement (Q1: stated only in general terms);
  - the eligibility of apps/flow;
  - what the plan features Millions of tokens and Website builder (SH-I-1162, SH-I-1161, placed in SH-C-152) are;
  - the interface through which Shopify Magic generates text (Q1: observation needed);
  - the reasons for Sidekick's, Magic's, agentic commerce's and Flow's placements (searched, not found).
- **Salla:**
  - what the AI agent app at /ai-agent, salla_gpt, ai-product and suggested-by-moshamer do;
  - whom the AI Connector's assistant acts for, and what it may read or change;
  - the usage agreement's clause on AI tools, and the reason for their placement (Q1: page not read);
  - any statement grouping Salla's AI features.

### Problems with the brief or the evidence

1. **One inventory entry in two concerns.** Q1 places SH-I-1495 (App action) in SH-C-152 and in SH-C-164. Citing it under
   one concern strains a landing of the other: the checker reads an inventory id's concern from Q1's placements, not from
   the cell. I avoided it by citing SH-C-152's own statement keys.
2. **Batch 3's problem 2 comes back with SA-C-100.** The brief allows a cell to cite another domain's statement "where the
   cell needs it". Its rule for a pair whose other concern is in a domain without F under also is that the ruling is apart.
   The two still pull against each other, and I followed batch 3: none-held and apart.
