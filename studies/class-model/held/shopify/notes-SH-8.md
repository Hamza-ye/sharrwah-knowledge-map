# SH-8: Shopify's admin router, its first 117 entries (notes)

**What this batch is.** It is the first held-pass batch on Shopify, and the first on `admin-router`, the admin's route manifest. No batch had placed this structure before it. SH-1 to SH-7 haven't run, and `held_entries.py earlier` printed no earlier line for any key of the batch but one: a word match, on a homonym (section 6). SH-9 to SH-18 hold the rest of the structure, about 930 entries. They may run side by side once this batch is checked, so section 2 writes the rules these lines follow, for them.

- **Entries:** 117, in the manifest's order, from six sections: AbandonedCheckouts (2), Account (2), Agentic (1), Analytics (11), Apps (37) and Banking (64).
- **Placements:** 117 `capability`, no `new`, no `out`. There are 126 lines, since eight entries take two lines or more. By support, counting each entry of a grouped line: 114 `core`, 13 `shows` (the redirects, 2.4) and 1 `extension-point`.
- **The checker's last run:** no problem, no `CHANGES` line and no `NEW` line. Every cell the lines touch already holds `core` (CM-PAY-011 holds `core;extension-point`), so no single line changes a cell.
- **What I read:**
  - observed-sh at `e38dc17e3`: its `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and `REGISTER.tsv`'s rows `shopify/admin-router` and `shopify/admin-router-versions`;
  - `index/ledger-summary.tsv` and `index/ledger/admin-route.tsv`: each route's joined path, its status by store, and the step that visited it;
  - the structure's `meta.json`. Its `source` is `router-577b0ff35365.js`, run `20260929T234254Z-admin-bundles`, of 29 September 2026;
  - its `items.jsonl` and `source.jsonl`, and the selection row (`drop:intent,action,model,form`, placement `where`);
  - the run steps the ledger names. Runs before `20261004T235142Z` have their text in `derived/step-text-from-html/`;
  - `structures/shopify/admin-betas/` (both held stores), for the betas the routes name;
  - `structures/shopify/admin-route-titles-en`, for the untitled routes. It holds no title the manifest lacks for this batch;
  - `derived/intents.tsv`, for the intents (2.8).

## 1. Lines by capability

| Capability | Lines (entries) | Entries |
| --- | --- | --- |
| CM-PAY-023, the Balance account | 51 `core`, 3 `shows` | the Banking routes, apart from those below |
| CM-PAY-024, its cards | 3 `core`, 4 `shows` | request, order and activate a card; the card routes that redirect to `/finance/cards` |
| CM-TAX-009, tax forms | 3 `core` | `finance:tax-forms` (container), a 1099-MISC form's view, the 1099-MISC forms under `account_review` |
| CM-TRU-002, identity verification | 3 `core` | `balance:verify-identity`, `shopify-balance:profile-assessment` and its remediation, beside CM-PAY-023 |
| CM-APP-001, apps | 9 `core`, 2 `shows` | Settings > Apps and its routes; `apps` (old address), `apps/installing`, two redirects |
| CM-APP-009, custom apps | 7 `core`, 2 `shows` | App development and a custom app's pages; two redirects |
| CM-CHN-001, sales channels | 8 `core`, 1 `shows` | Settings > Apps > Sales channels, Settings > Sales channels and its routes; a channel's address that redirects |
| CM-APP-007, an app's page | 3 `core` | `apps/:handleOrKey` and its two deeper routes |
| CM-APP-005 and CM-APP-006 | 2 `core` each | an installed app's or channel's functions and extensions tabs |
| CM-PAY-011, payments apps | 1 `extension-point` | an installed app's payments tab (section 3) |
| CM-API-001, CM-API-002, CM-SFR-012 | 1 `core` each | a custom app's Admin API, credentials and Storefront API pages |
| CM-ANL-001 | 5 `core` | the Analytics index page, the Targets container and its three routes |
| CM-ANL-002 | 5 `core` | Reports, a report, New exploration, ShopifyQL Query Preview, Finances summary |
| CM-ANL-003 | 2 `core` | the guard `analytics:overview:eligibility`, and the Analytics index page as a dashboard |
| CM-CHK-007 | 2 `core` | the abandoned checkouts list and one checkout's page |
| CM-STF-001, CM-STF-002, CM-STF-005, CM-ACC-001, CM-TRU-001 | 1 `core` each (CM-STF-005: 2) | Users and permissions with its four anchors; the collaborator review route |
| CM-AIA-005 | 1 `shows` | `agentic:catch-all`, a redirect |

## 2. The rules these lines follow, for SH-9 to SH-18

### 2.1 What an entry is

- **An entry is one route object** of the admin's router bundle, `router-577b0ff35365.js`, as `items.jsonl` holds it, with its own keys only. Its children are other entries, joined by `parent`: the nesting is the source's `children` arrays.
- **Its text drops `intent`, `action`, `model` and `form`** (the selection's rule). The item holds them. Read `intent` to clarify the route's thing, and quote it in `reading` as "the item". Never take a term from it.
- **Keys that are code, not statements:** `sliceName`, `sliceId`, `loader`, `component`, `titleLoader`, `action`, `form`, `model`, `errorBoundary`, `ErrorBoundary`, `HydrateFallback`, `lazy`, `handle`, `icon`, `titleHidden`, `position` and `array_offset`.
  - The name of a component or loader module may clarify an untitled route's thing, as the brief allows Zid's modules: `AccountCollaboratorReview`, `AppPaymentsConfigPage`, `EmbeddedAppLoading`. Mark it as "a reading of the module's name".
  - `source.jsonl` gives each route's code, with its default `component` beside any `eligibilityMatch` one.
- **The concern map already cites some routes,** and those are not in the batches.
  - A concern-map statement's note often names other routes that share its eligibility ('the same eligibility on 3 more route(s): …'). Those routes are entries, and the statement's placement is their lead.
  - Here, SH-S-5043, SH-S-5044, SH-S-5051 and SH-S-5028 named routes of this batch. Read them with `class_slice.py key`.

### 2.2 Its address

- **`path`** is relative to the parent's path.
  - The full address is the parents' paths joined. The ledger gives it in `index/ledger/admin-route.tsv`, column `note`, where `` {`${o.settings()}/*`} `` stands for `settings/`.
  - Write the full address in `reading`.
- **`index: true`:** the route is its parent's page, at the parent's address.
- **A pathless route** has no `path` and no `index`.
  - It wraps its children with an `eligibility`, a `context` or an `eligibilityMatch`.
  - Some have a page component of their own: a layout, such as `shopify-balance:onboarded-page`'s `OnboardedPage`.
- **`modal: true`:** a dialog over the parent's page, and a part of that page.
- **`anchors`:** sections within the route's page, each with its own title and path. Each is a place of its own (B-extent, "What a place of its own is").

### 2.3 What bears on its capability

**The route's own words, in this order:**
1. its `title`;
2. its `anchors`, each taking its own line (2.7);
3. its own path segments, and its id's words after the section's namespace (`apps:`, `balance:`, `shopify-balance:`, `analytics:`);
4. its `resource`, where the whole section doesn't share it. Most Banking routes carry `balance` and most Apps routes `apps`: those say where the route is;
5. failing all of these, the module's name (2.1).

**What says where the route is, and gives no line (M-6 refined):**
- the `section`, the router's grouping;
- the parent's path and words, and the path's prefix, such as `access_account/…` and `account_review/…`;
- the namespace of the id, and a resource the whole section shares.

**What names other places, not the route's thing (rule 2):** `nextRoutes`, `breadcrumbs` and `redirect`.

**What says what kind of page the route is:** `actionType`, one of `list`, `update`, `review`, `overview`, `settings`, `transaction_show`, `app_handler`, `installing`, `redirect_to_…`. It marks a list, a detail, a step or a redirect for the route's thing, and names no capability by itself.

**What may clarify the route's thing:** `intent`'s `type`, such as `shopify/Report`, `shopify/AnalyticsTarget` or `shopify/AppExtensions`.

**Then the brief's lookups:**
- the parent's id in the cells: the parent is often cited, and a part of a page whose words name nothing new is the page's capability's;
- the capability's note;
- `class_slice.py caps --terms` for every narrower thing the words name.

### 2.4 Its support

- **`core`:** every route is the platform's own admin route, so its line is `core`, with its gates in `scope` and `reading` (2.5).
- **`shows`, for a route whose only content is a redirect.**
  - It is redirect-only where it has a `redirect` key, or where its component or loader is named for a redirect (`RedirectApps`, `AppManageDetailsRedirectToOverview`, `redirect.loader`, `BankingRedirectToStatements-loader`), or its `actionType` is (`redirect_to_overview`, `redirect_to_statements`).
  - It keeps an address and opens no page of its own, as the concern map placed the legacy route agentic (SH-S-5026, `shows`).
  - It goes on the capability its own words name, not on its target's: `sales_channels:details` redirects to `/apps/agentic` and stays CM-CHN-001's.
  - The concern map placed `balance:inactive:redirect-statements` `core` (SH-S-5044), cited for its permission as a `decides` statement. That is unsettled (section 4).
- **A loader-only route** with no component, whose names don't say redirect (`shopify-balance:activate-card`), stays `core`. Its reading says that whether it shows a page isn't stated.
- **Hashed betas** (`eligibility.betas`, or a `oneOf` alternative of betas only): the brief's rule. Read `structures/shopify/admin-betas/<store>/items.jsonl`.
  - `enabled: true` in a held store makes the route `core`, with that store as its `scope`.
  - `false` in both held stores (`2jiwxs-gr` and `fake-demo-sharrwah`) makes it `shows`.
  - A beta in `eligibilityMatch` gates nothing (2.5). The route stays `core`, with the beta and its value in `reading`.
- **An app's page.**
  - The routes at `apps/:handleOrKey…`, under `apps:embedded_parent` (SH-S-5034), are where any app opens in the admin: `core` on CM-APP-007.
  - A route named for one application and open only to the apps permissions `APPLICATIONS` or `LIMITED_APPLICATIONS` is `extension-point` on what the app does. That is B-extent's convention, as the concern map placed the Agentic section (SH-S-5027, SH-S-5028).
  - The admin's own pages for managing apps and channels (Settings > Apps, Settings > Sales channels) are open to the same permissions, but they are named for apps in general, not for one. They are `core`, as the concern map placed the apps list (SH-S-5028).
- **An intent:** 2.8.

### 2.5 Its scope: the gates

- **The route's own `eligibility` gates on the store go in `scope`,** in the source's identifiers, bare, as other batches write a feature: `features`, `entitlements`, `regions`, `plans`, `organizationFeatures` and `organizationFlags`, with `betas` as `beta <hash>`.
  - Several in one object, all required, join with ` and `, as in `hasInitiatedOnboardingToBanking and balanceCheckDepositEnabled`.
  - `oneOf` alternatives are `;`-separated, as in `existingMerchantEligibleForBanking;netNewMerchantEligibleForBanking;hasInitiatedOnboardingToBanking`.
  - An `excluded` condition is written `not <identifier>`. For instance, `settings-account:edit`'s `excluded: {oneOf: [rbacEnabled, hasOrgSettings]}` is `not rbacEnabled and not hasOrgSettings`.
  - Empty arrays and `eligibility: {}` state no gate.
- **The gates on the user go in `reading`, never in `scope`,** and give no CM-STF-002 line (rule 5). They are `permissions` and `organizationPermissions`, written as in 'the staff permission BALANCE_BANK_ACCOUNTS_MANAGEMENT'.
- **`clients`** (`web`, `native`) names the admin client the route is for, and goes in `reading`. A route for `native` only belongs to the mobile app (`docs/GAPS.md`: product SEO, publications, barcodes, shipping), and its reading says so.
- **`oneOfFailureStatus`** (403) is what the router answers where no alternative holds, and goes in `reading`.
- **Only the route's own gates go in `scope`.** An ancestor's gate is the ancestor's statement. Name it in `reading`, by the ancestor's id, where it bears: 'under balance:root (entitlement shopifyFinance.balance with region US, or GB under a beta, SH-S-5046)'. This is unsettled (section 4).
- **`eligibilityMatch`** is an alternative loader and component under a condition. The route keeps a default of its own: `analytics:dashboard-details` loads `DashboardDetails`, and `Dashboard` under beta 29ece4dc. It gates nothing, so its condition goes in `reading`, never in `scope`.
- **`context`** (`organizationFeatures`, `organizationFlags`, `appStoreGraphql`, `bourgeoisGraphql`, `merchantRiskGraphql`, `reportify`) reads as the data the route loads, from its values.
  - It isn't a gate: `apps:details_about` carries `context: [organizationFeatures, …]` with only permissions in its eligibility.
  - At most it goes in `reading`. This is a reading, unsettled (section 4).
- **A feature's value per store isn't the route's statement** (`derived/eligibility-by-store.tsv`).
  - The concern map placed those values `shows` on the capability: CM-PAY-023's SH-S-5394 to SH-S-5502.
  - Don't place them from a route. A route gated by a feature that is false on every held store stays `core`, with the feature as its scope.
  - Unlike a hashed beta, a feature such as `hasInitiatedOnboardingToBanking` is a store's state, not a release.
  - A visit that answered 'There's no page at this address' on a store where the feature is false agrees with the gate and changes nothing.

### 2.6 Containers (rule 3, M-13)

- **What a container is:** a route with children, a pathless route wrapping others, or a route whose path begins other routes' paths (the checker's `NOTE … a container`).
- **Where it goes:** on the capability its title names; failing a title, the capability its id's words or its own path name. It is `core`, its children are named in `reading`, and each child is placed by its own entry. Examples:
  - `finance:tax-forms` on CM-TAX-009;
  - `analytics:targets:eligibility` on CM-ANL-001;
  - `apps:settings_parent`, at `settings/apps`, on CM-APP-001;
  - `balance:ensure-terms-of-service` on CM-PAY-023.
- **A pathless guard** is placed as the concern map placed `shopify-balance:ensure-terms-of-service` (SH-S-5059) and `analytics:overview:eligibility` (SH-S-5023): `core`, on the capability its words and children name.
- **A container by its path alone keeps its own support.** Its path begins other routes' paths, but those routes are its siblings in the nesting. A redirect at the shared prefix stays `shows`: `apps:redirect_to_overview`, at `:appId`, whose siblings are the custom app's pages.
- **A second line** goes only where the container's own page is another thing.
- **A container that names only a grouping is `out`.** Such a container holds several capabilities' sections, and its words name none of them. This follows the coordinator's rulings after SA-21 and SA-22.
  - Later batches hold three candidates: `root` (path `/*`, SH-E-1ba467f4), `settings-modal` (SH-E-39a1431f) and `settings` (SH-E-66492d29).
  - The batch that holds them decides them, after searching the cells for the admin's Settings as a place.

### 2.7 Second things

- **A route takes a line on each capability whose thing its own words name** (2.3), each with its own reading.
  - `settings-account:index`'s title and four anchors gave five lines: CM-STF-001, CM-STF-002, CM-STF-005, CM-ACC-001 and CM-TRU-001.
  - 'Admin API Integration Configuration' gave CM-APP-009 and CM-API-001.
- **A part of a page** (a tab, a modal, a step, an index) is placed by its words.
  - Where its words name nothing new, it takes the page's capability alone.
  - Where its words name another thing, it takes that thing's capability alone. An installed app's `extensions` tab goes on CM-APP-006, and its `functions` tab on CM-APP-005, not also on CM-APP-001.
- **Banking.** Every route of the section is CM-PAY-023's, as that cell's reading cites the section's routes, except:
  - a card's route, which goes on CM-PAY-024, the child, alone, as the concern map keeps `finance/cards` there;
  - a tax form's route, which goes on CM-TAX-009 alone, as its note keeps the forms apart from the section;
  - identity verification and profile assessment, which take CM-TRU-002 beside CM-PAY-023. The concern map places Balance's profile-assessment interview on CM-PAY-023 (SH-S-5060), and these words name CM-TRU-002's thing.
- **What gives no line:** a gate's permission (no CM-STF-002 line), a gate's feature, `nextRoutes`, `breadcrumbs`, a redirect's target, the section, a shared resource, and an intent (2.8).

### 2.8 Intents

- **What the manifest holds:** 115 routes carry an `intent`, with an `action`, a `type` and a `release`. The releases are `public` 37, `protected` 14, `private` 18, and none 46.
- **SH-8's six intents:** edit, create and preview `shopify/Report`; create and edit `shopify/AnalyticsTarget`; open `shopify/AppExtensions`.
- **None of the six is documented.** `derived/intents.tsv` joins each intent to shopify.dev's Intents API pages, and none of SH-8's six has a page there.
- **An undocumented intent** clarifies the route's thing and gives no line.
- **Proposed, unsettled (section 4):** a `public` intent that the Intents API documents would be the platform's interface by which apps open the route. It would take an `extension-point` line on the route's capability, beside its `core`.

### 2.9 Out

A route is `out` only where it names no place and no thing:
- it has no title, no path of its own, no gate and no resource, and its id names only its role in the code (a layout node, an error boundary, a scaffold); or
- it is a container that names only a grouping (2.6).

None of SH-8's 117 entries is one.

### 2.10 Terms and readings

- **`terms`:** the title, then the id. For an untitled route, the id and its own path segment. Never a permission, a feature, a module or an intent's value.
- **`reading`** gives:
  - the full address, and what the route is: a list, a detail, a modal, a step, a container or a redirect;
  - its gates by kind: 'gated by the feature … and the staff permission …';
  - the concern-map statement it follows (SH-S-…);
  - any module or run step it rests on, cited at its file.

## 3. Entries I couldn't tell, and what would settle each

- **SH-E-75fac257, `apps:details_payments`,** is placed `extension-point` on CM-PAY-011.
  - Its only words are `payments`, under an installed app's page, and its component is `AppPaymentsConfigPage`. I read it as the configuration of a payments app on the Payments Apps API.
  - It might instead be CM-APP-001's (a tab of the app's page) or CM-APP-003's (the app's charges).
  - What would settle it: the page's text. No run opened it (computed path on all 13 stores), and the admin's UI strings are backlogged (REGISTER: `shopify/admin-ui-copy`).
- **SH-E-79c45b71, `apps:settings` ('App Settings'),** is placed `core` on CM-APP-009 alone. The checker's NOTE asks whether CM-APP-010 is its thing, since that cell holds nothing on Shopify.
  - CM-APP-010 is parameters an app's developer defines, held by the platform for each store and read through its API (Salla's App API Settings). This route is a custom app's own page in App development.
  - I read the same words as a homonym.
  - What would settle it: the page's text. No run opened any route under `settings/apps/development/:appId`.
- **SH-E-28718695, `apps:api_credentials`,** has its line on CM-API-002 as a reading of its title.
  - CM-API-002's note kept the grant routes in CM-APP-001 'so one statement doesn't support two trees'. Both capabilities are domain F, so the merge flags nothing.
  - The checker's NOTE here (lead CM-APP-010, by 'app api') is a word lead: Salla's App API.
- **SH-E-b16b7f2a, `analytics:dashboard-details`,** has its CM-ANL-003 line as a reading. Its id names a dashboard, and its page shows the store's performance metrics. The coordinator may judge that CM-ANL-001's line is enough.
- **SH-E-3693f4fd, `analytics:overview:eligibility`,** is placed on CM-ANL-003, as the concern map cites it (SH-S-5023).
  - Its only child in this version is `analytics:live`, Live View (CM-ANL-004).
  - So the staff permission OVERVIEWS gates Live View, and CM-ANL-003's reading, 'the route analytics:overview gated by OVERVIEWS', rests on a guard over Live View alone. That is a reading of the source's nesting.
  - What would settle it: the coordinator's view of whether this evidence belongs on CM-ANL-004 instead.
- **The Targets routes** (SH-E-6f0d30a4, SH-E-3921af91, SH-E-44cc59e8, SH-E-f48293b7) are placed on CM-ANL-001.
  - That cell holds analytics targets through its API: 'mutation analyticsTargetCreate requires write_reports'. So under rule 2 they are its evidence, not `new`.
  - Targets has a place of its own: the route `analytics/targets`, titled Targets, with Create target, Edit target and the intents `shopify/AnalyticsTarget`. The coordinator may make it a child of CM-ANL-001.
  - Searched: 'goal; goals; sales target; analytics target; AnalyticsTarget; targets'. CM-STF-004, Staff targets (Salla's Employees targets), is another thing.
- **SH-E-d822bd34, `settings-account:review`,** is placed on CM-STF-005 from its module's name alone (`AccountCollaboratorReview`). No run opened it, and its title comes from a `titleLoader`.
- **SH-E-c4e05ca1, `apps:installing`,** is placed on CM-APP-001: the page shown while an app installs. This reads its `actionType` and `EmbeddedAppLoading`, and a visit showed only 'Loading'.
- **SH-E-5f443900, `shopify-balance:activate-card`,** is `core` on CM-PAY-024. It has a loader only, and whether it shows a page or redirects isn't stated.

## 4. Cases for the coordinator: rules I couldn't settle

1. **Redirect-only routes.** I made them `shows`, after SH-S-5026, the legacy route agentic. That covers 13 entries here, and many more will follow in SH-9 to SH-18.
   - The concern map placed `balance:inactive:redirect-statements` `core` (SH-S-5044), cited as a `decides` statement on its permission.
   - The alternative is `core` for every route, the redirect in `reading`. No cell changes either way in SH-8.
2. **An ancestor's gates.** I put only the route's own gates in `scope`, and the ancestor's in `reading`.
   - Under `balance:root` (US, or GB under a beta), most Banking lines carry only a feature, or no scope at all.
   - The router's code isn't read. That a parent's eligibility gates its children is an assumption from the nesting.
   - Should a child's line carry its ancestors' store gates?
3. **`context`.** I read it as the data a route loads, not as a gate (2.5).
4. **Intents.** Should a `public` intent that the Intents API documents take an `extension-point` line (2.8)? SH-8 has none, so later batches will meet this.
5. **Hashed `organizationFlags`,** in `eligibility` or `excluded`. I didn't look for a held list of an organization's flags, like `admin-betas` for betas. A later batch with such a gate should, or should write the hash as its scope, with its value a gap.
6. **Banking's two exceptions** (2.7). Cards go on CM-PAY-024 alone, and identity verification and profile assessment take CM-TRU-002 beside CM-PAY-023. Both follow the concern map's placements, which differ from each other (SH-S-5060 on CM-PAY-023; `finance/cards` on CM-PAY-024 alone).

## 5. What sources state that no entry holds, for the second stage

- **`20261005T073116Z-journey-analytics/steps/001.text.txt`, line 30,** the Analytics page: 'Beginning Sept 21, 2026, sessions and related metrics may shift as Shopify Analytics enables better visibility into real shopper activity.' A lead for CM-ANL-001.
- **`20261005T073116Z-journey-analytics/steps/031.text.txt`,** Targets:
  - suggested targets ('Oct gross sales', 'Oct conversion rate', 'Oct orders');
  - line 68, 'Work with Sidekick': a lead for the admin's AI assistant on the targets page.
- **The Banking routes the development stores' sweeps visited** answered 'There's no page at this address'. Examples are `derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/031.html.txt` to `055.html.txt` (steps 31, 33, 34, 38, 44, 46, 51 and 55 read).
  - This agrees with the entitlement balance being false on development stores (SH-S-5380), which CM-PAY-023 already holds.
  - A store with Shopify Balance (US) would show these pages. That is a gap at the first level, not a request: the cell is `core` already.

## 6. Homonyms and leads

- **'balance':**
  - `earlier` matched the Banking routes, on the word `balance`, to SH-34's line 50 (unchecked): the Shopify Payments activity report, 'your Shopify Payments balance', on CM-PAY-005.
  - That is the payment service's balance, not the Shopify Balance account (CM-PAY-023). I kept my placements.
- **A recipient's 'payout method'** (`balance:recipients:update:payout-method:*`) is where money sent from Balance is paid. It is not CM-PAY-005's payouts.
- **'Dispute transaction' and 'Report suspected fraud'** are the merchant's report on its own account's transaction. They are not CM-PAY-009, a buyer's dispute of a payment to the store, nor CM-ORD-006, order fraud.
- **'Send money' and recipients** are the Balance account spending. They are not CM-PAY-027's Bill Pay, which pays vendors' bills through Melio.
- **`sales_channels:details`,** at `settings/sales_channels/:channelHandle`, redirects to `/apps/agentic`. A channel's settings address opens the Agentic section: a lead for CM-AIA-005 and CM-CHN-001, not a line.
- **`access_account` and `account_review`** are the addresses of CM-ONB-002's inactive-account and pending-termination routes.
  - The Balance statements and the 1099-MISC forms there open for a store in restricted access or pending termination. That is a reading of the parents' paths.
  - They give no line: the prefix is the parents'.
- **The two routes titled with the brand,** 'Shopify Balance' and 'Shopify Balance monthly statements' (the checker's NOTE on lines 75 and 110), are `core` because they are the admin's own routes, not on any maker. No `own-service` is claimed. CM-PAY-023's reading notes that no held statement names a Shopify company as its provider.

## 7. This brief, B-extent.md and the scripts

- **B-extent.md:** no rule of this brief read differently from it on these entries.
  - One reading: B-extent's 'An admin route named for an application, and gated only by the apps permission, is the app's page: extension-point'. I read 'named for an application' as one application's name (Agentic), not the Apps section's own pages, as the concern map placed `apps:list` (SH-S-5028).
- **`show`'s text leaves out `intent`** (the selection's rule), while intents bear on the routes. Read them from `items.jsonl`, at the entry's locator.
- **`earlier`'s keys for this structure** are a route's resource, or the first segment of its path (`checkouts`, `apps`, `analytics`, `shopify-balance`, `finance`), and a name word (`balance`).
  - Once SH-8 is checked, every route of SH-9 to SH-18 with the same resource will print SH-8's lines on that key: for instance, every `apps` route.
  - Read those lines by route id, not by key.
- **No problem with the checker.** Its container `NOTE`s are each answered by 2.6, and its two `NOTE`s on CM-APP-010 by section 3.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes and no new things.** The rules in section 2 stand for SH-9 to SH-18, with section 4's open cases settled:
  - **Redirects:** a redirect-only route is `shows` on its target's capability (the ruling after SH-8). SH-S-5044's `core` is read again at Shopify's amendment.
  - **Ancestors' gates:** only the route's own gates are its scope. The coordinator added each route's ancestors' gates on the store to 49 lines of 48 routes, in their reading, by `method/held_router_gates.py`. Most were under `balance:root` (US, or GB under a beta) or `balance:inactive`. Later batches leave this step to the coordinator.
  - **`context`** is data the route loads, not a gate.
  - **Intents:** one that the Intents API documents takes an `extension-point` line. An undocumented one, such as this batch's six, is named in `reading`.
  - **Hashed `organizationFlags`** are written as they stand.
- **Leads for the amendment and the final review:**
  - Analytics Targets (four routes on CM-ANL-001) may be a child capability.
  - `analytics:overview:eligibility` guards Live View alone, so SH-S-5023 may be CM-ANL-004's rather than CM-ANL-003's.
  - Whether a custom app's 'App Settings' page is CM-APP-010's is unsettled: its page wasn't opened.
- **`held_entries.py earlier`** now matches a route id whole (`balance:root`, never 'balance' alone). The 40 Banking lines it tied to SH-34's line on the Payments balance came from that cut.
- **Cost:** 18.2 million tokens over 78 requests, about 156,000 an entry.
