# SH-7: notes (Shopify, 124 entries of `admin-role-permissions`)

**What the batch is.** 124 entries of the role permissions the store `ctcbwa-r1` answered with: the admin's Role operation, 15 answers, one per role (run `20261005T063908Z-journey-roles`, `structures/shopify/admin-role-permissions/ctcbwa-r1/source.0.json` to `source.14.json`). An entry is one handle at one access level; its locator names the first item that holds it. 121 of my entries are held by the organization's Administrator role (`source.8.json`, 317 permissions), many also by the POS roles. The last three (122 to 124) are the Sales associate's (`source.13.json`) at the level `APPROVAL_REQUIRED`.

The Administrator's list falls into blocks, in its own order: organization permissions (positions 0 to 39, SH-6's), user management (40 to 80), store permissions in alphabetical order (81 to 235), the older staff and collaborator permissions (236 to 244), partner permissions (245 to 255), then `COLLABORATOR_STORE_ACCESS`, `INITIALIZE_POS_DEVICES`, `VIEW_ABANDONED_CHECKOUTS` and the POS permissions (259 to 316). My entries are positions 54 to 316 of that list, less SH-5's and SH-6's.

**What I read, beyond the brief's list.** The handles carry no titles. Where a handle's name left its thing open, I read:
- the role's own source: each role's `name`, `description`, `systemRoleHandle` and `pointOfSaleAccess`;
- the run's role pages (`raw/runs/20261005T063908Z-journey-roles/steps/*.text.txt`);
- the admin's own English permission titles. The map `Qn` in the permission tree's source holds titles for many permissions that have no permission object in the tree (`structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/source.js`, offsets 23,936 to 32,750). These are SH-4's "58 titles with no permission object", most of them the POS roles'. I read them as the platform's locale strings for the handles, the brief's rule 1, and each reading quotes the title with its offset. The terms stay the handle, the entry's own text (rule 5).

## SH-6, which runs beside this batch

SH-6's placements were written while I worked, and they hold 35 of my handles at `DENY`. I take SH-6's line (capability, support, scope) for each of them, as my brief asks. Each reading cites SH-6's line by its entry id rather than its line number, since the file may still change.

Where my draft differed from SH-6, I took SH-6's line. The differences, for the coordinator:
- **The POS cart.** SH-6 gives saved carts, custom sales, cart discounts and Ship to customer no CM-CHK-002 line: the POS cart isn't the buyer's cart (CM-CHK-002), whose Shopify cell is the online store's cart. Where a handle names the cart beside another thing, the cart is the POS app's own and takes CM-POS-001 (SH-6's R3, added to its file while I worked): `ADD_DISCOUNTS_TO_CART` is CM-MKT-001 and CM-POS-001. My draft had given each a cart line on CM-CHK-002.
- **Lists in a title.** SH-6 gives a title's list of kinds no line (the ruling after SA-41). So 'Fulfill shipping, pickup, and delivery orders' is CM-SHP-009 alone, and 'Create shipping and delivery orders' is CM-POS-001 alone. My draft had added CM-SHP-007 and CM-SHP-008, and CM-SHP-001.
- **The smart grid.** SH-6 puts 'Customize smart grid' on CM-POS-001, the POS app's home screen, and leaves apps' tiles to CM-POS-004. I had read the cell's term POS smart grid as CM-POS-004's.
- **Restock and unfulfilled items.** SH-6 puts 'Manage item restock' and 'Remove unfulfilled items' on CM-RET-003. It cites a held post that names them among the new return permissions in POS (SH-E-7f303534). I had read them as inventory (CM-INV-001) and order editing (CM-ORD-002).
- **Retail reports.** SH-6's line is CM-ANL-002 alone. I had read 'RETAIL' as CM-POS-001's term Retail.
- **Staff sales attribution.** SH-6 places `SALE_ATTRIBUTIONS_FOR_ORDERS` on `new:Staff sales attribution`, the new thing SH-50 named, with `core`. SH-50's own line on it supports `shows`. The coordinator decides the support with the thing.

The role kin follow SH-6's rule too (see R4 below). My draft had given the role kinds POS, organization and partner a line each on CM-POS-001, CM-ACC-003 and CM-PTN-002, and I dropped those lines.

## The rules I followed

P1 to P8 and S1 to S8 (SH-3's and SH-4's notes), the rule after SH-4 (a role's permission takes its permission's line), and the ruling after ZD-7. For the kinds those rules don't cover:
- **R1. A role permission is `core` on the capability of the thing it gates,** found from its handle and read with its title where `Qn` holds one, whatever channel it is used in.
  - A POS permission's own things go on the capability that holds them: its returns, refunds, discounts, discount codes, store credit, draft orders, fulfilments, transfers, offline card payments, abandoned checkouts and reports.
  - What is the POS app's own goes on CM-POS-001: its devices, custom sales, carts, offline checkout, smart grid, required checkout information and rules.
  - Where a kin of CM-POS-001 holds the thing, it goes there: cash tracking is CM-POS-003, POS UI extensions CM-POS-004.
- **R2. A user-management permission is CM-STF-001's.** That covers inviting, deleting, viewing, activating and updating users and staff accounts, and a user's status.
- **R3. A role-management permission is over the staff's permissions themselves: CM-STF-002.** That covers viewing roles, assigning a role to users or groups, managing who holds a role, a user's POS access, revoking access tokens and manager approval.
  - The POS access is stated on the role itself (`pointOfSaleAccess.hasPosAccess`). It also takes CM-POS-001, the surface it opens, as 'on Shopify mobile' took CM-SRF-001 (S4) and SH-6's Dev Dashboard took CM-PTN-001.
  - Manager approval is approving what another role holds at `APPROVAL_REQUIRED`: SH-6's line, and the Sales associate's description says so.
- **R4. A role assigned `ON_GROUPS` also takes CM-STF-003,** user groups, which exist to receive roles together. That is a second thing (S4).
  - `ON_USERS` takes no CM-STF-001 line, since the user only holds the assignment.
  - The role kind the handle names (POS, store, organization, partner roles) takes no line.
  - A line on another capability goes only where that cell cites the very role, as SH-6 placed the kin: POS full permissions (`point_of_sale_administrator`, SH-I-0853) on CM-POS-001. That is why `MANAGE_POINT_OF_SALE_ADMINISTRATORS_ON_USERS` takes CM-POS-001, and the POS user administrator's and POS device setup's handles don't.
- **R5. A qualifier that says only whose records or where an act is done takes no line.** Examples: another location's drafts, a customer's store credit, sessions ended 'from the admin'. Nor does a parent of the line's own capability (P4, S6), or a route the permission also opens (P3). Those routes are named in `reading`:
  - the organization's security route opens to MFA, SAML and SCIM, audit events, the collaborator request PIN and the collaborator request settings (SH-S-5238);
  - the billing and inactive-account routes open to the billing permissions (SH-S-5087, SH-S-5082, SH-S-5070);
  - the pending-termination payouts route opens to the Shopify Payments permissions (SH-S-5081).
- **R6. `APPROVAL_REQUIRED` is the role's own setting, like ALLOW and DENY.** It goes in `reading`, and the entry takes its handle's line (entries 122 to 124). SH-6 did the same for `ENABLE_OFFLINE_CHECKOUT`.
- **R7. A handle the tree holds without an entry of its own takes the cell's line, with no scope.** The concern map cites these, so the tree gives them no entry. The tree's `visibleBy` is named in `reading` and not taken as scope, since the role's answer states no condition (rule 5). This is SH-6's R6, which I aligned to after drafting with the scopes. The handles and the conditions named:
  - `MANAGE_AUTOMATIONS` and `MANAGE_AUTOMATION_SETTINGS`: `automationsPermissionsEnabled`;
  - `VIEW_ALL_SHOPIFY_CREDIT_TRANSACTIONS`: `creditViewOnly`;
  - `VIEW_BALANCE_BANK_ACCOUNTS`: `balanceViewOnly`;
  - `STAFF_API_PERMISSION_MANAGEMENT`: the Users category's `userManagementPermissions`, listed where it is true or not set (`e==null||e===!0`).

  SH-5's script carried a tree line's scope over. If the coordinator prefers that, these five lines take the four conditions above. No cell's support changes either way.

  `BILLING_SUBSCRIPTIONS`, which SH-4 placed twice under the two Settings categories' opposite conditions, takes one line on CM-PLN-001 with no scope (S1).
- **R8. A partner permission of the organization's role gates the partner's own tools.**
  - It is `core` on what it gates: financials on CM-PTN-003, refunds and credits on CM-APP-003, referrals on CM-PTN-008 (the rulings after SA-30 and SA-44).
  - A tool for a marketplace of third parties is `extension-point`: app listings on CM-APP-002, themes on CM-SFR-003, the Partner Directory on CM-PTN-005.

## New things

- **`new:Beacons`** (SH-E-1e3b825a, `BEACONS`):
  - **Place of its own:** none known. It is a store permission held only by the Administrator. No custom role can be assigned it (`OrganizationAssignableStorePermissions` in the run's answers), and no title is held.
  - **Searched:** beacon, in `caps --terms` and `search`.
  - **Proposed:** domain, area and parent unknown, `shows`.
  - **Name:** `BEACONS` only, since the admin is held in English.
- **`new:Seller health`** (SH-E-39797168, `MANAGE_SELLER_HEALTH`):
  - **Place of its own:** none known. Store permission, Administrator only, no title.
  - **Searched:** seller health, health, seller.
  - **Proposed:** unknown, `shows`. If it is the store's standing with the platform, CM-ONB-002 or CM-TRU-009 might hold it. If it is a channel's seller standards, CM-CHN-002 or CM-CHN-003 might.
- **`new:Partner ads`** (SH-E-0e856b0d `MANAGE_PARTNER_ADS`, SH-E-db9e213d `VIEW_PARTNER_ADS`):
  - **Place of its own:** none known. The only held statement naming partner ads is the billing charge category Partner ads (SH-I-1335), which no cell cites.
  - **Searched:** ads, advertis, App Store ads, app ads, Partner ads. Nothing found is the partner's ads: CM-MKT-010 and CM-MKT-012 are the merchant's.
  - **Proposed:** domain F, area PTN, parent CM-PTN-001, `shows`.
- **`new:Staff sales attribution`** (SH-E-edc04bbe, `SALE_ATTRIBUTIONS_FOR_ORDERS`): SH-6's line and SH-50's new thing (SH-E-ada073f2).
  - **Title:** 'Manage sales attribution for orders' (`Qn`, offset 31,502).
  - **Run pages:** the POS roles' pages offer 'Attribute sales to staff' with POS Pro (`steps/029.text.txt`, line 64).
  - **Proposed:** domain E, parent CM-POS-001. Not CM-MKT-008, which credits orders to marketing: a homonym for CM-MKT-008's note.

## The cells that change

- **CM-POS-004 gains `core`** (line 100, `MANAGE_POS_UI_EXTENSIONS`, 'Manage POS UI extensions', offset 31,647).
  - This is SH-6's line. SH-6's `APPS` ('Use apps that work with Shopify POS') gives CM-POS-004 the same.
  - A reading: the admin's own permission over the POS UI extensions a store uses is the platform's own management of them, as CM-APP-001 holds the apps permissions. The apps that extend POS keep the cell's `extension-point`.
- **CM-PTN-008 becomes held, `core`** (line 84, `VIEW_PARTNER_REFERRALS`).
  - A reading on the handle's word alone: a partner's referrals, the platform's referral programme. The cell's own reading names the seed's Shopify "referrals" as a lead.
  - What isn't held: that the referrals are of the platform's plans, or earn a commission.
  - The other reading: the leads merchants send a partner, which CM-PTN-005's Partner Directory holds.
  - **What would settle it:** the Partner Dashboard's referrals page, or the routes the admin router gates by `VIEW_PARTNER_REFERRALS`. If neither is CM-PTN-008's thing, the line goes to `new:Partner referrals` or CM-PTN-005.

## Entries I couldn't tell, and what would settle each

For every handle below, the admin router's routes gated by it would settle it (`structures/shopify/admin-router/`, its `permissions` and `organizationPermissions`). The admin bundle that titles the organization's and the store's legacy permissions would too: the role pages show none of these titles, and the tree's map holds none of them. Neither was traced: the brief keeps the read to the entry's own sources.
- `CUSTOMER_PRIVATE_DATA`: CM-TRU-005, customers' personal data. It could instead be CM-CUS-001 (the records) or CM-API-004 (protected customer data, for apps).
- `MANAGE_TERMS_OF_SERVICE`: CM-CNT-008, the store's published policies, whose note names terms. The tree's own Manage store policies is `MANAGE_POLICIES`, so this may instead be the store's acceptance of the platform's terms (CM-ACC-001).
- `SQLITE_BULK_DATA_TRANSFER`: CM-MIG-001, a bulk transfer of store data, beside the tree's Bulk data (Export, Import). It is held only by the Administrator, not by a POS role.
- `SUPPORT_METHODS`: CM-ONB-003, the platform's support for the merchant, as SH-6 read the support-request permissions. It could instead be the store's own support for its buyers (CM-SUP-005, which holds only App Store categories).
- `WRITE_OFF_ORDERS`: CM-ORD-001, an act on the store's orders. It could instead be payment terms (CM-PAY-008), an order paid after it is placed.
- `MANAGE_PARTNER_REFUNDS_CREDITS`: CM-APP-003, read as refunds and credits of the charges the platform bills merchants for partners. Whose refunds and credits these are isn't held.
- `CHANNELS` (CM-CHN-001) and `CONTENT` (CM-CNT-002, the category METAOBJECTS titled 'Content'): plain readings with no title of their own.
- `SHOPIFY_PAYMENTS_TRANSFERS`: CM-PAY-005. A reading: 'transfers' are the payouts, since with `SHOPIFY_PAYMENTS_ACCOUNTS` it opens the payouts route `pending-termination:payments:payouts` (SH-S-5081).
- `CONTENT_MODELS_*`: CM-CNT-002, read as metaobject definitions, Content's models beside its entries.
- `RESERVE_ITEMS` and `BYPASS_CUSTOM_RULES`: SH-6's lines and doubts. For the second, the same title map has 'Manage cart rules in POS editor' (`MANAGE_CART_RULES`, offset 31,993).

## A structure whose items and sources disagree

None in the items. Two things to note:
- **My brief's message** says each entry is ALLOW or DENY. The source also holds `APPROVAL_REQUIRED`: three of my entries, and SH-6's `ENABLE_OFFLINE_CHECKOUT`.
- **The structure's label is `ctcbwa-r1`,** while the run's pages are at `admin.shopify.com/store/fake-demo-sharrwah` ('fake-demo-sharrwah.myshopify.com', `steps/001.text.txt`). This is a finding aid, not a fault I can see.

## What the sources state that no entry holds (for the second stage)

All are in run `20261005T063908Z-journey-roles`.
- **The POS Pro card on every POS role's page** (`steps/029.text.txt`, lines 59 to 65; the same in `031.text.txt` and `040.text.txt`):
  - 'Unlock custom POS roles with POS Pro';
  - 'Upgrade to POS Pro and get 3 months for $1/month per location.';
  - 'Unlimited POS staff accounts', 'Restrict user access to certain locations', 'Manager approvals', 'Attribute sales to staff'.

  These are leads for CM-POS-001 (POS Pro's lines), CM-STF-002 (manager approvals, location-limited access) and Staff sales attribution. The organization's answer `OrganizationHasPosProSubscription` reads `hasPosProSubscription: false`.
- **The Administrator role's page** (`steps/019.text.txt`, lines 49 to 60):
  - 'Role managed by Shopify';
  - 'View, add, edit, and delete users, roles, and groups (Plus plan only)';
  - 'Assign and remove groups (Plus plan only) for users';
  - 'Cannot have access conditions attached';
  - 'Unable to transfer organization ownership'.

  These are leads for CM-STF-002 and CM-STF-003 (groups on Plus only; the cell already holds the plan line Custom user groups, Plus).
- **The answer `OrganizationAssignableStorePermissions`** (`answers/admin.shopify.com/OrganizationAssignableStorePermissions/9a0801f40807bfe904d8836c5b46210da0e529ced26ea0ea77742e1aa0922d40.json`): the 124 store permissions a custom role may be given. Of my handles, only the seven billing ones, the two Shopify Payments ones and `VIEW_ROLLOUTS` are among them. A lead for CM-STF-002: what the Administrator holds that no custom role can be given.
- **Each role's description and its `pointOfSaleAccess`** (`hasPosAccess`, `initializePos`) and `accessConditions` (`source.0.json` to `source.14.json`):
  - the Cashier's 'Can perform basic checkout functions, including applying discount codes, editing taxes, adding customers, opening cash drawer, and managing cash tracking sessions.';
  - the Store manager's 'Can perform all POS actions and approve staff tasks.'

  Leads for CM-POS-001 and CM-STF-002.
- **The tree's `Qn` titles for POS permissions not in my batch** (offsets 29,975 to 32,750): 'Switch device's location', 'Log out from the POS app', 'Manage receipt settings', 'Manage cart rules in POS editor', the legacy 'Ship to customer' and 'Fulfill shipping and pickup orders', and others. These are SH-4's 58 titles, for the coordinator's amendment.

## Problems with the brief or the script

- **The checker's quote test resolves a cited file only by its full repository path** (`structures/shopify/admin-permission-tree/…/source.js`). A shorter path failed, and the checker reported 'found nowhere held' until the path was written in full.
- **A batch that runs beside another and must take its lines meets that file while it is still being written.** SH-6's file appeared midway, and its line format changed while I read it. I cite its lines by entry id. The coordinator should check the 35 shared handles once SH-6 is final.
- **Cost:** about 50 requests; the context reached about 220,000 tokens.

The checker's last line, for SH-7: `124 of 124 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 124 of 124 entries, no problem. Its 37 lines shared with SH-6 are the same as SH-6's.
- **The cell changes stand, each read again:**
  - CM-POS-004 gains `core` from MANAGE_POS_UI_EXTENSIONS, as SH-6's line.
  - CM-PTN-008 is held, `core`, a marked reading. VIEW_PARTNER_REFERRALS is the permission over a partner's referrals: the stores a partner brings, which is the cell's referral programme. It rests on the handle's words. SH-86, the Partner Dashboard's routes, is to confirm it from the referrals' own route; if the route says otherwise, the line moves to CM-PTN-005 or a new thing.
- **SH-6's R1 to R8 stand,** with this batch's two rules brought into line with them: a role kind named in a handle takes no line of its own, and a tree-held handle takes no scope.
- **New things:**
  - Beacons, Seller health and Partner ads, each `shows`, with no place of their own;
  - Staff sales attribution.

  They are decided with the others. For Partner ads, the billing charge category of that name (SH-I-1335) is held.
- **Cost:** 28.0 million tokens over 103 requests, about 226,000 an entry. The context reached about 520,000 tokens, against the agent's estimate of 230,000.
