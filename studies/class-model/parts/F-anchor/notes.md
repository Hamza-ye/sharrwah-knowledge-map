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
