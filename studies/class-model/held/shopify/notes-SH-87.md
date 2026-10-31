# Notes on SH-87 (shopify, effort high)

130 entries of one structure, `partners-dashboard-routes`, read at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure the pass reads):
- entries 1 to 12: the bundle label's last twelve path literals (`partners.shopify.com@20261007T065956Z-published-partners-dashboard-js`, literals 111 to 122), all links to shopify.dev's Built for Shopify requirements by app category;
- entries 13 to 130: the label `@source-maps`, its items at positions 0 to 122 (`items.jsonl`, lines 1 to 123), with their files' text in `source.jsonl`. Positions 123 to 127 are SH-88's, except 126 (below).

Placements, by entry:
- 121 on a capability alone;
- 5 on a new thing alone;
- 2 on both (SH-E-63bd2fad, App versions and CM-APP-006; SH-E-594777b0, CM-PTN-008 and Sandbox organizations);
- 2 out.

That is 139 lines: 130 on a capability, 7 new, 2 out.

## How the batch reads its entries

- **SH-86's rules R86.1 to R86.12 and its coordinator's check are kept.** No rule of this batch departs from them.
- **A source-map entry is the twin of SH-86's bundle entry for the same route,** by R86.2's mapping (SH-86's batch positions 20 to 45, 47 to 50, 51 to 100, 101 to 104, 105 to 109 and 110 to 127 against source-map positions 0 to 25, 94 to 97, 33 to 82, 101 to 104, 26 to 30 and 105 to 122). The mapping was checked path by path (a script in the scratchpad, `twins.py`). Each such entry takes its twin's placement, cap_id, supports, scope, terms and filler, and its reading cites the twin. The lines on the source map's catch-alls follow SH-86's lines on their twins.
- **Terms** take the path's own segments, as the twins do, though these entries' text also holds the element's name. The element is named in `reading`, as R86.2 and the admin router digest's rule 2 put a module's name.
- **Routes with no twin** were placed one by one, from their own file in `source.jsonl` and the runs' visits (`index/runs.tsv` joins them; the routes runs `20261007T070336Z-journey-partner-dashboard-routes` and `20261007T213930Z-journey-partner-dashboard-routes-from-source`, and the partner run `20261007T010009Z-journey-partner-dashboard`). These are positions 31 and 32 (Ads), 83 to 88 (Stores), 90 to 92 (Partner Directory), 98 to 100 (Invitations, Memberships) and 126 (SandboxOrganizations' `/new`):
  - **Ads' two generic Routes** (SH-E-aed458b9, SH-E-7495c720). `Ads/index.tsx` makes one Route per route config, spreading the config's `routeProps`. It renders the config's component inside `UserPreferencesProvider` (RouteWithProvider) where `route.canAccess` holds, and `NoAccessPage` with `route.permission` where it doesn't. Both are the five ad routes themselves, so both lines are CM-APP-002 `core` (E86). The user's permission is in `reading` (R86.8).
  - **Stores' sub-pages:**
    - `/:id/team-members` is CM-DVT-003 `core`, a page of one partner store (rule 3);
    - `/new` is CM-DVT-003 `core`. The run opened it as `stores/new?store_type=client_store` and landed on the admin's Create store, with Dev and Client transfer as options (partner run, step 39);
    - `/:id/app_credits`, `/:id/app_discounts` and `/:id/app_trial_extensions` are CM-APP-003 `core`, the app charges the platform bills a store, adjusted by the developer (R86.6). No run visited them (the register says so), so these are readings by their names;
    - the index takes CM-DVT-003 `core` and a second line CM-DVT-004 `core`. Its address, `/:orgId/stores`, is the navigation's Stores before verification, and SH-86 gives that item (SH-E-fd879f29) the same two lines.
  - **The Partner Directory's routes:** the landing page, the partner's profile and the review request are CM-PTN-005 `extension-point`, as their container (SH-E-9750e844). Both visited routes answer “The page you’re looking for could not be found” for the held partner (routes run, step 3; from-source run, step 2). A route with its own page keeps its line (R86.3).
  - **Invitations and Memberships:**
    - `/new_member`, an invitation and a member are CM-PTN-002 `core`, the partner organization's team, as their containers;
    - `/invitations/new_member`, opened, lands on the admin organization's `settings/organization-account/new`, which failed to load (from-source run, step 3). So it takes a second line, CM-STF-001 `shows`, as SH-86 placed the memberships' landing (R86.11). SH-15 places that admin route, Add users, on CM-STF-001 (SH-E-2ee0a0cd).
- **An entry that stands for several items.** This label's entry text leaves out an item's `props.element` expression and its `element_props`. So items with the same path and no element name have one text, and they are one entry whose locator names only the first item. Each item takes its own line, by the brief's rule for a route structure's repeated path:
  - **SH-E-594777b0** (`/new`, line 98) stands for two items:
    - PartnerLeads' `/new` (position 97, element `referralsSection`), whose twin SH-86 placed on CM-PTN-008 `core`;
    - SandboxOrganizations' `/new` (position 126). Its element is `Navigate` to the index for a user whose `useRbacPermissions` holds, and `SandboxOrganizationCreateLoader` otherwise. That is the creation of a sandbox organization, new:Sandbox organizations `core`, with the user's condition in `reading`.

    SH-86's notes give positions 125 to 127 to SH-88. Position 126 is this batch's, through this entry; SH-88 holds 123 to 125 and 127 (SH-E-8ed195c4, SH-E-a200dde4, SH-E-3ae5cec0, SH-E-3cc3dcca, its first four entries).
  - **SH-E-8f500f09** (`*` NotFound, line 76) stands for six catch-alls: the Apps section's three (positions 75, 79 and 82) and those of Stores, the Partner Directory and Payments (positions 89, 93 and 104). All are `out` (R86.5). SH-86 gave four of them twins (SH-E-0d4cf39d, SH-E-ac442a05, SH-E-aaf84c49, SH-E-4c79902a), all `out`.
- **The Built for Shopify links** (entries 1 to 12) follow R86.9.
  - The bundle's code at the offsets (`raw/runs/20261007T065956Z-published-partners-dashboard-js/fetch.warc.gz@1721194`, the AppDistribution bundle) holds FeatureCriteriaList's list of fourteen categories, each a doc link with a translation key. Its `en.json` names them: Product bundles, Subscriptions, Discount, Product reviews, Returns and exchanges, Invoices and receipts, Fulfillment services, Carrier services, Affiliate, Analytics, Ads, Email marketing, Forms, SMS marketing.
  - One grouped line puts the twelve on CM-APP-002 `core;extension-point`, with the term built-for-shopify (rule 6). Each also takes its category's capability, `extension-point`:
    - discount: CM-MKT-001;
    - product reviews: CM-SUP-001;
    - returns and exchanges: CM-RET-003;
    - invoices and receipts: CM-ORD-008;
    - fulfillment services: CM-SHP-011;
    - carrier services: CM-SHP-004;
    - affiliate program: CM-MKT-014;
    - analytics: CM-ANL-001;
    - ads: CM-MKT-010;
    - email marketing and SMS marketing: CM-MKT-007;
    - forms: CM-MKT-005.

## New things

All three are SH-86's new things. This batch adds entries to them and proposes nothing new.
- **`new:Bug Bounty`** (SH-E-3cf1e48f, `/:orgId/bugbounty`, element Bugbounty, position 12).
  - **Place of its own:** the route.
  - **Proposed** as in SH-86's notes: domain F, area PTN, parent CM-PTN-001.
  - **Name:** English only, since the dashboard isn't held in Arabic.
  - **Searched:** SH-86's terms. The source map adds nothing.
- **`new:Sandbox organizations`** (SH-E-3080ebc5, the section `/:organizationId/sandbox_organizations/*`, position 25; SH-E-594777b0's second line, its `/new`, position 126).
  - **Place of its own:** the route.
  - **Proposed** as in SH-86's notes: domain F, area DVT, parent CM-DVT-003.
  - **The leads read:** CM-ACC-003 and CM-PTN-002 hold an owner's several stores and the partner's own organization, not sandboxes (SH-86's notes).
- **`new:App versions`** (SH-E-29fd32aa, SH-E-3dc2fb80, SH-E-f7e03f7c, SH-E-63bd2fad: `/:appId/versions`, `/versions/new`, `/versions/:appVersionId` and an extension in a version, positions 71 to 74).
  - These are SH-86's four routes again, all `core`. SH-E-63bd2fad also takes CM-APP-006.
  - It isn't CM-API-006, the platform's API versions, a homonym. The lead CM-APP-011 (by the word extension) isn't it either.

## Entries I couldn't tell, and what would settle each

- **SH-86's own doubts carry to the twins.** They concern Partner docs, Product docs, Support, Shopify POS, Activity, App history, App audit, Partner certificates and Payment processing. A partner whose pages render would settle them.
- **Ads' NoAccessPage** (SH-E-7495c720).
  - It is placed CM-APP-002 `core`, the ad routes as a user without their permission meets them.
  - `out` is the other reading, a refusal that names no place of its own. The page itself names `route.permission`.
  - The coordinator may prefer `out`, as SH-86 left the billing section's NoAccessPage in a reading.
- **A store's team members** (SH-E-9259321d).
  - It is placed CM-DVT-003 `core`, a page of one partner store. No visit is held.
  - The other readings are CM-STF-005, a partner's collaborator access to a merchant's store, and CM-PTN-002, the partner's employees.
  - The page as a partner with a store sees it would settle it.
- **App credits, app discounts and app trial extensions** (SH-E-0b353aea, SH-E-27df065c, SH-E-b4cc02f3).
  - They are placed CM-APP-003 `core`, by their names under a store of the section Stores, as the developer's adjustments of its app's charges to that store.
  - No visit and no statement of them is held: `search` finds no statement on app credits or trial extensions.
  - Their pages would settle them.
- **The Stores index's second line** (SH-E-3f52cfef, CM-DVT-004 `core`).
  - It rests on the address's landing after verification, as SH-86's SH-E-fd879f29 does.
  - The route's own component, StoresIndexPage, isn't held rendered.
- **The forms apps' category** (SH-E-6a20454c) is placed on CM-MKT-005.
  - The model keeps Shopify Forms there (SH-36 to SH-38), and holds no capability of store forms.
  - The category's criteria on shopify.dev (`requirements#forms-apps`) would say what such apps do.

## What the structure and its sources disagree on

- **The entries' text drops part of an item.**
  - The label's entry text leaves out each item's `props.element` expression and `element_props`. Entries then collapse items with one path and no element name (SH-E-594777b0, SH-E-8f500f09; above), and the locator names only the first item.
  - The text also loses the elements of PartnerLeads' `/success` and `/` (`referralsSection`), and NoAccessPage's `permission` (`route.permission`).
  - The item and `source.jsonl` hold them, and the source governs.
- **Visits that landed elsewhere:**
  - `stores/new?store_type=client_store` landed on `admin.shopify.com/store-create/organization/239421532` (partner run, step 39);
  - `invitations/new_member` landed on the admin's `settings/organization-account/new` (from-source run, step 3).

  Both routes keep their own lines (R86.3).

## What a source or run step states that no entry holds (for the second stage)

- **The kinds of store a partner creates** (`20261007T010009Z-journey-partner-dashboard/steps/039.text.txt`): 'Dev', 'Testing, dev, or staging environments', and 'Client transfer', 'Manage and transfer stores for clients'.
  - CM-DVT-005's cell holds nothing on Shopify, and names the seed's “client transfer” only as a lead.
  - The client transfer runs (`20261007T152806Z-journey-client-transfer`, `20261007T154445Z-journey-store-transfer-accept`, by observed-sh's GAPS.md) would say whether a transferred store is CM-DVT-005's (a store a partner prepares for merchants) or only CM-DVT-003's.
- **Built for Shopify's category review** (the AppDistribution bundle, module `.../BuiltForShopifyRequirements/components/CategorySpecificCriteria/translations/en.json`). Its states are 'unselected', 'assigned', 'reviewer_selected' ('This decision was made during Shopify's review and can't be changed'), 'in_review' ('Shopify will double-check this during our review and apply all related criteria. …') and 'after_review'. They show Shopify's review assigning an app's category criteria, for CM-APP-002's review.
- **The categories this batch's links don't hold, but the same list names:** product bundles and subscriptions are SH-86's links (SH-E-e0f235d8, SH-E-b1a17e2b).

## Problems with the brief or the scripts

- **`show` prints no items under an entry for this structure,** as it does for Salla's `dashboard-app-routes`. So an entry that stands for several items is found only by matching its text against `items.jsonl`, as this batch did.
- **`earlier` matches the Ads route configs' ids** (index, create, report, details, edit) as `name` keys to hundreds of other batches' lines, besides the bare paths ('/new', '/:id', '/bills') the coordinator named. Twins were taken from SH-86's lines.
- **`warc_text.py` read the AppDistribution bundle's record** (`@1721194`) without fault. Its output starts with the record's headers, so offsets into it are shifted, as SH-86 found.
- **The clone's commit:** citations are at `e38dc17e3`, as the entries are. `git diff --stat e38dc17e3 04de369da` is empty for the structure and the six runs this batch read.

## The `CHANGES` lines, read again

- **CM-APP-006 gains `extension-point`** (lines 85, 86, 88, 93, 95, 96, 97: the app's extensions, their creation, an extension type's routes and an extension in a version). This is SH-86's kept `CHANGES` on the twins. Kept.
- **CM-APP-009 gains `extension-point`** (line 67: the distribution page's custom distribution). This is SH-86's kept `CHANGES`. Kept.
- **CM-DVT-004 gains `core`** (line 106: the Stores index's second line). This follows SH-86's kept `CHANGES` on SH-E-fd879f29, the same address. Kept.
- **CM-PTN-008 gains `core` and becomes held** (lines 29, 33, 110 to 113: the affiliate programme, the partner leads' section, `/success`, `/:product`, the index and `/new`). This is SH-86's kept `CHANGES`, the referral programme for the platform's plans. Kept.

## The coordinator's check

Measured: 15.3 million tokens over 80 requests, about 118,000 an entry, SH-86's mapping read once instead of the source maps. The checker prints no problem.
- **Kept:** every line, R86's rules and the check's corrections, the twelve Built for Shopify links on CM-APP-002 `core;extension-point` with each category's capability `extension-point` (CM-MKT-005 for forms apps, a reading), every `CHANGES` line (the same SH-86's check kept) and the new things' added entries.
- **The uncertain placements** (NoAccessPage `core`, a store's team members on CM-DVT-003, the three app-billing routes read from their names, forms on CM-MKT-005): kept as placed, each a marked reading.
- **An entry standing for several items** (one entry per distinct text): SH-E-594777b0 and SH-E-8f500f09 carry a line for each item they stand for; SH-88 holds positions 123 to 125 and 127.
- **The create-store page's 'Client transfer'** goes to `amendment-notes.md`, with the store transfer already there.
