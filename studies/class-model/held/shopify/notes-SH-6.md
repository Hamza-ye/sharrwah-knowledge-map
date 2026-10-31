# SH-6: notes (Shopify, 124 entries of `admin-role-permissions`)

Batch SH-6, effort `high`, read under `briefs/H-held.md`, the coordinator's rulings to the last section of `held/review-H-rulings.md`, SH-3's P1 to P8 and SH-4's S1 to S8 as the coordinator's checks keep them, and SH-5's notes. Evidence: observed-sh at `e38dc17e3`. 124 entries, 151 lines in `placements-SH-6.tsv`:
- 123 entries placed on capabilities, 1 `new`, none `out`;
- 150 capability lines and 1 new line, all `core`.

## The structure, and where my entries stand in it

The structure is the admin's Role operation as the store `ctcbwa-r1` answered it, 15 times, once per role (run `20261005T063908Z-journey-roles`; `source.0.json` to `source.14.json` beside `items.jsonl`, each holding one role's name, description, category and permissions).
- **An entry is one handle at one access level.** It stands for every item of that handle and level across the 15 roles. Its locator names the first. `show` doesn't print which roles hold it, so I read them from each item's `source` and the roles' names in `source.N.json`, and every reading names them.
- **The roles, by their own `category`:** POINT_OF_SALE (Associate, Limited permissions, Cashier, POS full permissions, POS device setup, POS user administrator, Sales associate, Store manager); STORE (Customer support, Marketer, Merchandiser, Online store editor); ORGANIZATION (App developer, Administrator, Organization POS administrator).
- **My entries, in order:**
  - 1 to 58 are mostly the POS roles' permissions. Associate and Limited permissions hold most of them at DENY.
  - 59 to 72 are the same handles at their other levels, with the tree's handles that store roles hold (customer data, inventory counts, purchase orders).
  - 73 to 124 are the Administrator's organization permissions: roles, user groups, business entities, stores, billing, collaborators, support, dev stores.
- **118 handles; six stand at two levels:** CASH_TRACKING, APPLY_DISCOUNT_CODES, EDIT_TAXES_IN_CART, OPEN_CASH_DRAWER and MANAGE_INVENTORY_COUNTS at DENY and ALLOW, and ENABLE_OFFLINE_CHECKOUT at DENY and APPROVAL_REQUIRED. Each level is its own entry, with the same lines (the coordinator's message).

## What I read beyond the entry, and why

- **The permissions' titles.** I read them in the admin chunk's title map (`Qn`, offset 23,934 on) in `structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/source.js`, the permission tree's source. SH-4's notes name it as holding 58 titles with no permission object, most of them the POS roles'.
  - 58 of my 118 handles have a title there. The other 60 have none in the chunk, among them every organization permission.
  - I read the map as the admin's own words for the handle, the way a locale is read (rule 1). Each reading quotes the title and cites the file by that path. The checker finds a title only when the path is cited whole.
  - Terms are the handle alone, the entry's own words (rule 5).
- **The roles' descriptions** (`source.N.json`) and **the role pages** of the same run (steps 4 to 31 and 40, `.text.txt`): the role's source and the structure's run (rule 1; the coordinator's message).
- **The held help notes on POS pages** (structure `help-notes`, 22 entries of the held pass, which no batch has placed yet). Each names a POS permission and what it lets staff do, such as 'To create a custom sale, staff members must have the Add custom sales permission.' (SH-E-2637e31f).
  - I read them only to find the capability where a handle's name left it open. I cite them by entry id and quote them exactly. Their own batch places them.
  - Strictly, rule 1's list of what may be read doesn't name another structure's entries. I flag it here for the coordinator.
- **Earlier batches' lines on the same things,** found with grep: SH-34, SH-35, SH-36, SH-38, SH-39, SH-50, SH-53 and SH-55. `earlier` printed nothing for any entry (see the problems below).
- **SH-7,** the other 124 entries of this structure, ran beside this batch. Its files appeared as I finished. I didn't read them: the coordinator aligns the two, by the rules below.
- **Not read:** the Help Center's POS permissions page, `manual/your-account/users/roles/permissions/pos-permissions.md`, held in `structures/shopify/help-center/help.shopify.com@en-ar/md/en/`. The coordinator's message limits what I read to the role's source and the POS runs. That page would settle most of the entries below that I couldn't tell.

## The rules I followed (for the coordinator to align with SH-7)

These are the coordinator's rules (the ruling after ZD-7, S4, M-6, rule 2), read for a role's permissions. Where a rule is mine, it says so.
- **R1. Each permission is `core` on the capability it gates** (the ruling after ZD-7).
  - Only a permission over the staff's permissions themselves goes on CM-STF-002. That covers roles created, updated, deleted and exported; roles assigned to users or groups; manager approval; and, a reading, access tokens.
  - User groups go on CM-STF-003 and users' accounts (deleted, status changed, exported) on CM-STF-001.
- **R2. A POS permission goes on the capability of the thing it gates,** as the cells hold them:
  - cash, cash drawers and payment tracking sessions: CM-POS-003;
  - returns and exchanges: CM-RET-003, and refunds: CM-RET-002;
  - customers: CM-CUS-001;
  - discounts: CM-MKT-001; discount codes: CM-MKT-002;
  - offline card payments: CM-PAY-021;
  - transfers: CM-INV-006; counts: CM-INV-003;
  - gift cards: CM-LOY-002; store credit: CM-LOY-001;
  - fulfilment: CM-SHP-009; draft orders: CM-ORD-005; taxes: CM-TAX-001;
  - POS UI extensions and apps in POS: CM-POS-004;
  - staff sales attribution: SH-50's new thing.

  It goes on CM-POS-001 only where the thing is the POS app's own: its cart and saved carts, custom sales, offline checkout mode, smart grid, receipts, a device's location, logging out, the POS channel's required checkout information, Ship to customer, and basic POS access. This follows the cells: SH-35 placed offline checkout mode on CM-POS-001, SH-39 Ship to customer, SH-34 and SH-36 receipts, and the held pass the smart grid editor.
- **R3. A second thing the permission's own words name takes a second line** (S4, M-6). The cases: the POS cart (ADD_DISCOUNTS_TO_CART, EDIT_TAXES_IN_CART); a customer's metafields (CM-CNT-002 and CM-CUS-001); the device and its location; refund beside return and exchange; and the receipt as a printed order document (CM-ORD-009, as SH-34). A place where the permission is used takes a line, as 'on Shopify mobile' did: the Dev Dashboard (CM-PTN-001). Two cases take none:
  - a second line on the model's parent of the line's own capability (S6): no CM-POS-001 line beside CM-POS-003 or CM-POS-004;
  - a restriction ('at all locations'), or the kinds of order a title lists ('shipping, pickup, and delivery orders', 'shipping and delivery orders'). These are things named only in a list (the ruling after SA-41).
- **R4 (mine). A handle naming user groups as the assignee** (`…_ON_GROUPS`, `MANAGE_GROUP_…_ROLE_ASSIGNMENT`) takes CM-STF-003 beside CM-STF-002. Receiving roles is that capability's own thing ('staff grouped to receive roles together'). `…_ON_USERS` takes no CM-STF-001 line: a role assigned to a user is CM-STF-002's own thing.
- **R5 (mine). A role a permission assigns takes the line of a capability whose cell cites that role** (rule 2: the same term). The cases:
  - the organization administrator, cited in CM-ACC-003 (SH-S-0245);
  - Organization POS administrator and POS full permissions (`point_of_sale_administrator`), cited in CM-POS-001 (SH-I-0851, SH-I-0853);
  - collaborators' store access, CM-STF-005's own term Collaborator access.

  A role category (organization, store, partner, POS roles) only says which roles. So does a role no cell cites: App developer, the user administrators, POS device setup. Neither gives a further line, as M-6 refined gives a group's title none.
- **R6 (mine). The tree's handles.** For a handle the permission tree holds with no line of its own, because the concern map cites it, the line is the cell's: the same capability, with no scope. Those handles are Set payment terms, the inventory counts and purchase orders, and Erase and Request data.
  - The tree's `visibleBy` is named in `reading`: `inventoryCountsPermissionsEnabled` for the counts, `inventoryEnhancedPurchaseOrdersPermissionsEnabled` for the purchase orders. It isn't taken as scope, since the role's answer states no condition (rule 5).
  - SH-5's script carried the tree lines' scopes over (Manage disputes' `shopifyPaymentsRbacEnabled`). If the coordinator prefers that, six lines take those two scopes: the counts' entries 28, 42, 70 and 71, and the purchase orders' 69 and 72. No cell's support changes either way.
- **R7. The access level is each role's own setting, in `reading`.** That holds for ALLOW, DENY and the third level APPROVAL_REQUIRED, which I read as the action needing a manager's approval. No level changes a line.
- **R8. A route or a cell row the permission gates isn't its own thing** (SH-3's P3). The cases: the billing routes the PLN cells cite for MANAGE_BILLING and VIEW_BILLING; the Organization settings route of test drives in CM-ACC-003 (SH-S-5232), so MANAGE_TEST_DRIVE goes to CM-EVO-001, Feature test drives, as SH-34 placed them.

## New things

- **`new:Staff sales attribution`,** with SH-E-68c63b68 (SALE_ATTRIBUTIONS_FOR_ORDERS, DENY, Associate and Limited permissions; titled 'Manage sales attribution for orders').
  - It is the same new thing SH-50, SH-53 and SH-55 named: sales credited to the staff who made them, at the point of sale.
  - It isn't CM-MKT-008, which credits orders to marketing (a homonym).
  - Place of its own: none in this entry, since a staff permission isn't one.
  - The POS role pages' POS Pro panel lists 'Attribute sales to staff' (`20261005T063908Z-journey-roles/steps/005.text.txt`, line 63), among what POS Pro unlocks.
  - Proposed: as SH-50 proposed it, domain A, area STF, under CM-STF-001. The alternative is domain E under CM-POS-001: the Winter 2024 Edition puts it under Channels > Shopify POS (SH-55's line), and this permission is a POS role's.
  - Support: `core`. The staff permission is the platform's own, gating the platform's own feature, and the coordinator's check after SH-54 reads a new thing's support as 'what the platform does with it' (`notes-SH-54.md`), as SH-55's line is. SH-50's and SH-53's lines are `shows`; SH-55's notes ask for the three to be aligned.
  - Names: English only ('Manage sales attribution for orders'; 'Attribute sales to staff'). The admin in Arabic isn't held.
  - Searched: attribution, sales attribution, attribute, staff (`caps --terms`). They found only CM-MKT-008 and CM-MKT-014, the affiliates.

## The cells that change, and why

- **CM-POS-004, App extensions in the POS app, gains `core`** (lines 12 and 36). The cell holds `extension-point` and `shows`: apps extend Shopify's POS through its extension targets.
  - **Line 12:** APPS, titled 'Use apps that work with Shopify POS', ALLOW in eight roles. Receiving transfers on POS needs it (help note SH-E-e1943440).
  - **Line 36:** MANAGE_POS_UI_EXTENSIONS, titled 'Manage POS UI extensions', the capability's own term.
  - I read both again against the title map and the roles: each is the platform's own staff permission over apps in its POS app. By the ruling after ZD-7, a permission is `core` on what it gates. So the cell would hold Shopify's own control of the extensions beside the apps' `extension-point`.
  - I kept them. The alternative for APPS is CM-APP-001, the store's apps (already `core`), if 'apps that work with Shopify POS' are read as the installed apps rather than the POS app's extensions.
- **CM-DVT-004, Development stores, gains `core`** (line 70): DEVELOPMENT_STORE_MANAGEMENT, held by the App developer and the Administrator.
  - The App developer role 'has full access to tools and development stores for building apps' (source.3.json).
  - The merged cell is `not-stated` (one `shows`). SH-36, SH-51, SH-52 and SH-53 already hold `core` lines on it, not yet amended.
  - I kept it.
- **No other cell changes.** Every other line's support is one its cell already holds.

## Entries I couldn't tell, and what would settle each

- **BYPASS_CUSTOM_RULES (SH-E-7a21bd6e), titled 'Skip custom rules': CM-POS-001 or CM-CHK-005.**
  - I read the rules as the POS cart's, since the same map titles MANAGE_CART_RULES 'Manage cart rules in POS editor'.
  - If they are the cart and checkout validation rules apps write, the line goes to CM-CHK-005, and that cell gains `core`.
  - What would settle it: the Help Center's POS permissions page (above), or a POS run that opens the cart rules.
- **RESERVE_ITEMS (SH-E-0511fe33), no title: CM-INV-001.**
  - A held post names 'Reserving inventory for items included in draft orders' (SH-E-3da2c81a), so the reserve may be draft orders' (CM-ORD-005).
  - CM-INV-008 is stock held for unpaid orders, which holds nothing on Shopify; it isn't bookings (CM-SEL-004).
  - What would settle it: the POS permissions page.
- **LIMITED_APPLICATIONS (SH-E-951ee739), no title: CM-POS-001, read as basic POS access.**
  - Every POS role holds it, the Administrator doesn't, and it is the POS user administrator's only permission beside users and POS roles.
  - That role 'has basic Point of Sale access' (source.12.json), and its page grants user management 'along with basic POS access' (step 027).
  - If it is a limited set of apps, it is CM-POS-004's (a further `core` there) or CM-APP-001's.
- **AUTHORIZE_ORGANIZATION_SUPPORT_REQUESTS and AUTHORIZE_STORE_SUPPORT_REQUESTS (SH-E-5c2d9779, SH-E-430ffcf5): CM-ONB-003.**
  - The handle doesn't say whose requests: the user's requests to Shopify's support, or support's requests to reach the store.
  - If the latter, CM-STF-005, where CM-ONB-003's note puts Salla's support team's access requests.
  - Both cells are `core`.
- **MANAGE_ACCESS_TOKENS (SH-E-eaf53b8f): CM-STF-002,** as the model places the staff permission Revoke access tokens (STAFF_API_PERMISSION_MANAGEMENT, SH-S-7166). If the tokens are apps' API tokens, it is CM-API-002's.
- **ONDEMAND_ACCESS_TO_STORES (SH-E-e34d3781): CM-ACC-003,** the organization's stores, between which the owner moves. If it is a grant of access to staff, it is CM-STF-002's.
- **DEVELOP_APPS (SH-E-f1a349e3): CM-APP-009,** App development, as SH-36 placed custom apps built in the Dev Dashboard. If it is read as the developer tools, it is CM-DVT-001's.
- **CREATE_CLIENT_TRANSFER_STORES and TRANSFER_CLIENT_TRANSFER_STORES (SH-E-67132d68, SH-E-435171bc): CM-DVT-003,** a reading: stores a partner prepares for a client and transfers. The held client-transfer runs (observed-sh's `docs/GAPS.md`, runs `20261007T152806Z-journey-client-transfer`, `20261007T154445Z-journey-store-transfer-accept`) would settle it. They are leads for the second stage.
- **SELECT_EXISTING_ORG_LEGAL_ENTITY (SH-E-b6fde1d3): CM-ACC-004 alone.**
  - SH-5's SELECT_EXISTING_LEGAL_ENTITY takes CM-ACC-004 and CM-ACC-005, with the scope `multipleBusinessEntitiesPermissionEnabled`, from its tree title 'Select and assign business entities'.
  - The organization handle has no title held and names no assignment.
- **ACCESS_ORDER_FULFILLMENT and SHIP_CART_TO_CUSTOMERS (SH-E-cc3d8098, SH-E-48bc9e97): one line each,** CM-SHP-009 and CM-POS-001. Their titles list the kinds of order (shipping, pickup, delivery), and these take no line (R3).
  - If the coordinator reads the titles' lists as S4's second things, they take CM-SHP-007 and CM-SHP-008 lines.
  - SH-34 put the POS local delivery post on CM-SHP-008, with these permissions gating it on the user.
  - No cell changes either way.
- **REMOVE_UNFULFILLED_ITEMS (SH-E-7445963a): CM-RET-003 alone,** as a held post names it a 'Return permission' (SH-E-7f303534). It could also be CM-ORD-002, removing items from an order.
- **R6's scope** for the tree's handles, above.

## A structure whose items and sources disagree

- **None in the values I read.** The items agree with `source.N.json` on every handle and level of my entries.
- **The rendering drops which roles hold an entry,** and an entry stands for many items (above).
- **The Administrator's answer (`source.8.json`) lists five handles twice, each with two ids:** CANCEL_ORDERS, DELETE_CUSTOMERS, MANAGE_INVENTORY_COUNTS, PAYMENT_SETTINGS and PERFORM_INVENTORY_COUNTS (317 permissions, 312 distinct). Two are mine (entries 42 and 70), and one entry stands for both items.
- **A third access level is held:** APPROVAL_REQUIRED (ENABLE_OFFLINE_CHECKOUT for Cashier and Sales associate, entry 65). The message said ALLOW or DENY.

## What the sources state that no entry holds (for the second stage)

- **The POS role pages' POS Pro panel** (`20261005T063908Z-journey-roles/steps/005.text.txt`, lines 57 to 64; the same in steps 4, 6, 7, 10, 11 and 28 to 31, and in 040 for Add role's Point of Sale category).
  - It reads 'Unlock custom POS roles with POS Pro' and 'Upgrade to POS Pro and get 3 months for $1/month per location.', with its list 'Unlimited POS staff accounts', 'Restrict user access to certain locations', 'Manager approvals' and 'Attribute sales to staff'.
  - The store's POS roles showed this panel, not their permissions.
  - It is a lead for CM-POS-001 (POS Pro and its trial price), CM-STF-002 (custom POS roles and manager approvals behind POS Pro), Staff sales attribution, and the location restrictions of ORDERS_AT_OTHER_LOCATIONS and MANAGE_DRAFT_ORDERS_AT_OTHER_LOCATIONS.
- **The system roles' pages, their Privileges and Limitations.**
  - **The Administrator** (`019.text.txt`): 'View, add, edit, and delete users, roles, and groups (Plus plan only)' (line 53) and 'Assign and remove groups (Plus plan only) for users' (line 55). That is a Plus scope for the user group lines (CM-STF-003, CM-STF-002), which my entries' sources don't state. Its limitations: 'Unable to transfer organization ownership', 'Cannot have access conditions attached' (lines 58 to 61).
  - **The POS administrator:** 'Set up new or update devices via the POS app' (`021.text.txt`, line 53).
  - **POS device setup:** 'Can only be assigned to users with an email based Shopify account' (`025.text.txt`, line 54).
  - **The POS user administrator:** 'Unable to perform elevated POS actions, such as returns and exchanges, custom discounts, or cash tracking, unless also assigned a POS role that grants them' (`027.text.txt`, line 57).
- **The roles' descriptions.** Sales associate: 'Manager approval needed for custom discounts, sales, returns, and exchanges.' (source.13.json). Store manager: 'Can perform all POS actions and approve staff tasks. Has access to all settings in POS app; POS channel usage of those settings requires admin access.' (source.14.json). They are leads for CM-STF-002 (approvals) and CM-POS-001.
- **The title map's other POS titles,** with no entry of mine: 'Manage cart rules in POS editor' (MANAGE_CART_RULES) and the legacy 'Fulfill shipping and pickup orders' (ACCESS_ORDER_FULFILLMENT_LEGACY). They are for SH-7, if it holds them, or the second stage.
- **The help center's POS permissions page,** for the entries above.

## Problems with the brief or the script

- **`held_entries.py earlier`** keys on an entry's address, route or app name, translation key and label. A role permission's handle is none of these, so it printed nothing for 124 entries. The titles, the earlier lines and the help notes were found by grep.
- **The checker finds a quote from the title map** only when the reading cites `source.js` by its whole path in observed-sh. 'admin-permission-tree source.js' wasn't enough.
- **The message's 'ALLOW or DENY'** leaves out APPROVAL_REQUIRED (above).
- **Rule 1's list of what may be read** to clarify an entry names neither a sibling structure's source (the title map) nor another structure's entries (the help notes). I read both, and say so above.
- Nothing in this brief read differently from B-extent.md for these entries.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 124 of 124 entries, no problem.
- **The cell changes stand, each read again:**
  - CM-POS-004 gains `core` from the admin's own staff permissions over apps in the POS app (APPS, MANAGE_POS_UI_EXTENSIONS), by the ruling after ZD-7. The apps themselves keep the cell's `extension-point`.
  - CM-DVT-004 gains `core` from DEVELOPMENT_STORE_MANAGEMENT, beside SH-36's and SH-51 to SH-53's lines.
- **R1 to R8 stand, and SH-7 keeps them.** No scope on a role's permission: the role's answer states no condition, so the tree's `visibleBy` is named in `reading`. SH-5's script is aligned to it, and SH-5's lines now take no scope.
- **The third access level,** APPROVAL_REQUIRED (a manager's approval), changes no line, as DENY doesn't.
- **What the agent read beyond the role's source** is held evidence the brief lets a batch read to clarify an entry: the permission titles in the tree's own `source.js`, and the help notes, other held entries cited by id.
- **New thing:** Staff sales attribution, decided with the others, whose support differs between batches.
- **Cost:** 33.4 million tokens over 123 requests, about 269,000 an entry. The context reached about 474,000 tokens, with 68 file reads and 12 runs of the checker.
