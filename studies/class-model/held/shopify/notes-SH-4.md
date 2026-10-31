# SH-4: notes (Shopify, the last 72 entries of `admin-permission-tree`)

Batch SH-4, effort `high`, read under `briefs/H-held.md`, the coordinator's rulings to the last section of `held/review-H-rulings.md`, and SH-3's P1 to P8 as the coordinator's check after SH-3 keeps them. Evidence: observed-sh at `e38dc17e3`. 72 entries, 81 lines in `placements-SH-4.tsv`:
- 72 entries placed on capabilities, none `new`, none `out`;
- 81 capability lines: 80 `core`, 1 `shows`.

## The structure, and where my entries stand in it

The structure is the staff permission list in the admin chunk `use-store-options-f948ecd551d0.js` (run `20260929T235133Z-admin-chunks-all`, `source.js` beside the items): the categories' permission objects (`xe()`, offsets 16,081 to 22,917 for my categories), the shared lists `Xn` (View payouts) and `Re` (the ten settings permissions both Settings categories spread), and the title maps `qn`, `Jn` and `Qn` (offset 23,934 on).
- My 72 entries are positions 46 to 141 of `items.jsonl`, from Gift cards to App and sales channel permissions.
- Positions 41 to 45 (purchase orders and inventory counts), 52 and 53 (Erase personal data, Request data), 65 and 66 (Flow automations), 96 to 100 (Users), 103 and 104 (Balance and Shopify Credit activity), 115 and 116 (View billing and receive billing emails, Edit billing payment methods and pay invoices) have no entry: the concern map cites them.
- The two Settings categories (positions 114 to 127 and 128 to 139) list the same permissions but for billing. One entry stands for a permission in both: Manage settings, and the ten of the list `Re`. Manage Shopify plan has two entries, one nested under View billing details (the first category) and one with no parent (the second).

## The rules I followed

P1 to P8 of SH-3's notes, with the coordinator's addition after SH-3 (a category's `visibleBy` is the scope of every permission inside it, joined to a permission's own with ` and `). The rules below are mine, for cases those rules leave open, for the coordinator to align.
- **S1. A permission listed in both Settings categories takes no category scope.** The two categories' `visibleBy` are complementary: `({options:{organizationBilling:e}})=>!e` and `({options:{organizationBilling:e}})=>e`. A permission in both is listed on every store, so its line has no scope, as SH-3's P5 gives no scope to a permission listed under both branches of its title. Its own `visibleBy` stays its scope: Manage payments settings is `shopifyPaymentsRbacEnabled`.
  - This covers 11 entries: Manage settings (SH-E-5c32aa66) and the list `Re` (SH-E-f8e5ef20, SH-E-6feb1fca, SH-E-8ebf0b0e, SH-E-7c51f91d, SH-E-6558b082, SH-E-1760b61f, SH-E-78c0ab62, SH-E-5c398b3f, SH-E-29c9589d, SH-E-3e4309ae).
  - The alternative is the brief's rule 5 read to the letter, where an entry stands for several items whose conditions differ: two lines per entry, one scoped `not organizationBilling` and one `organizationBilling` (Manage payments settings: `not organizationBilling and shopifyPaymentsRbacEnabled`, `organizationBilling and shopifyPaymentsRbacEnabled`). That would add 11 lines and change no cell's support. I didn't take it, since the two scopes together say what no scope says.
- **S2. A permission in one Settings category takes that category's condition.** Manage Shopify plan's two entries are scoped `not organizationBilling` (nested under View billing details, SH-E-b07743ba) and `organizationBilling` (no parent, SH-E-c44f2457). A negated option is written `not <option>`, as SH-3 wrote `not shopifyPlus`, and so is Manage other payment settings' `not shopifyPaymentsRbacEnabled`.
- **S3. A `visibleBy` that is true where any of several options is true** gives those options as alternatives, `;`-separated (the ruling after SA-53): Manage identity providers, `!!(e||t||s)` over `customerAuthenticationThirdPartyEnabled`, `customerAccountsMultipassEligible` and `multipassEnabled`.
- **S4. A permission's own words that name a second thing give it a second line** (M-6), on that thing's capability, even where the model holds the two as parent and child:
  - Marketing's 'View, create, and delete marketing activities and automations': CM-MKT-005 and CM-MKT-006;
  - 'Blog posts and pages': CM-CNT-003 and CM-CNT-004;
  - 'Manage taxes and duties': CM-TAX-001 and CM-TAX-008;
  - 'Manage and install apps and channels': CM-APP-001 and CM-CHN-001;
  - Checkout and customer accounts' 'View and edit', titled by `CHECKOUT_AND_CUSTOMER_ACCOUNTS_SETTINGS`: CM-CHK-001 and CM-CUS-010;
  - 'Use Quick sale on Shopify mobile': CM-POS-001, where the cell keeps Quick sale, and CM-SRF-001, the platform's mobile app;
  - 'Select and assign business entities': CM-ACC-004 (selecting) and CM-ACC-005 (assigning), both cells holding the permission.

  A route the permission also gates, which its words don't name, gets no line (P3): the theme editor under Themes, the checkout and accounts editor under View and edit, the URL redirects under Menus, the settings routes under Manage settings.
- **S5. A company's store credit permission** (Companies > View store credit transactions, Edit store credit) is CM-LOY-001's, store credit held for a business buyer, and CM-B2B-002's, whose cell holds a company location's store credit history with its own permission (SH-S-5118).
- **S6. A nested permission whose parent is on the same capability takes one line** (Edit store credit, Develop, Enable development, Transfer domain, Manage and add custom pixels). A nested permission whose parent's capability is its own capability's parent in the model takes no parent line (P4): Edit code (CM-SFR-001 over CM-SFR-002), Approve app charges (CM-APP-001 over CM-APP-003), Manage identity providers (CM-CUS-010 over CM-CUS-011).
- **S7. A dependency gives no line,** as SH-3 read the nesting as a dependency: View tax documents depends on View payouts, and Merge on Create and edit and Delete.
- **S8. Terms** are the permission's id, its translation key and its title, with its subcategory's title where the title alone names nothing ('View', 'Delete' under Companies, Catalogs, Files and the like), and the part of a title that names a second thing ('automations', 'Blog posts', 'duties', 'channels', 'Shopify mobile').

## The cells that change

None. The checker prints no `CHANGES` line: every line's support is one its cell already holds. The one `shows` (Quick sale on CM-POS-001) keeps to the cell's two `shows` rows on the quick-sale route.

## New things

None.

## Entries I couldn't tell, and what would settle each

- **Manage store credit visibility (SH-E-bb8de15c): CM-LOY-001 alone, or also a parent line.** It is nested under Checkout and customer accounts > View and edit, which I placed on CM-CHK-001 and CM-CUS-010. The visibility could be the checkout's or the customer accounts', and the source doesn't say which, so I gave no parent line. What would settle it: a held page or run step of the setting, in Settings > Checkout or Settings > Customer accounts.
- **Use Quick sale on Shopify mobile (SH-E-2b6e60de): `shows` on CM-POS-001.** The cell keeps the quick-sale route as `shows`, since its words don't name POS. A lead for the second stage: the router's own route `quick-sale` (section QuickSale, title 'Quick Sale', clients web, permission QUICK_SALE, icon `logo-apple-tap-to-pay`, component `QuickSaleLandingPage`; `structures/shopify/admin-router/items.jsonl`, line 1165). If a held page shows Quick sale as selling in person, the line becomes `core`, and no cell changes, since CM-POS-001 is `core` already. Its CM-SRF-001 line reads 'Shopify mobile' as the platform's mobile app for managing the store, a reading.
- **Edit code (Including generating theme blocks) (SH-E-aa46bc05): CM-SFR-002 alone.** The title doesn't say what generates the blocks. Held posts name Shopify Magic (SH-37's line on CM-AIA-003, SH-E-fe4aa8d7) and Sidekick (SH-35's on CM-AIA-002, SH-E-2e8b181c) as generating theme blocks. If the coordinator reads the permission's generation as that feature, it takes a line on one of them, which would change no cell if that cell is `core`. What would settle it: a held statement tying the permission to the AI feature.
- **Checkout and customer accounts > View and edit (SH-E-63dca793): CM-CHK-001 and CM-CUS-010, not CM-CHK-003.** CM-CHK-003's cell cites the same permission as its editor's gate (SH-S-5103) and its configuration API's need. I read the editor as a route the permission gates, a child of CM-CHK-001 (P3). The CM-CUS-010 line rests on the permission's key and its category's title. CM-CUS-010's settings route needs PREFERENCES (SH-S-5131), so which customer accounts pages this permission opens isn't held here.
- **Select and assign business entities (SH-E-10428234): CM-ACC-005's line** reads 'assign' as assigning entities to markets. That rests on the permission's place in Markets, its dependencies on the three Markets permissions and its option `multipleBusinessEntitiesPermissionEnabled`. The source doesn't say to what the entities are assigned.
- **Manage taxes and duties (SH-E-7c51f91d): CM-TAX-008's line** reads the duties in the Taxes and duties settings (the cell's route duties, SH-S-7129) as part of what the permission manages, a reading.
- **Rule S1** (above), and whether the coordinator prefers rule 5's two lines.

## A structure whose items and sources disagree

- **None in the values I read.** The items agree with `source.js` on every id, title, parent, dependency, subcategory and `visibleBy` of my entries.
- **The rendering drops two things the items hold.** An entry's text names `category: SETTINGS` but not which of the two Settings categories it stands in, nor that it stands for two items. The items' positions do (114 to 127 and 128 to 139), and `categories.jsonl` gives each category's `visibleBy`. I read the categories there. A Settings entry's line can't be scoped from its text alone.

## What the sources state that no entry holds (for the second stage, and for the coordinator's amendment)

- **Conditions on permissions the concern map cites, which have no entry here** (`source.js`, the categories' permission objects; `categories.jsonl`). If the cells carry these permissions without the condition, the amendment could scope them:
  - View billing and receive billing emails (VIEW_BILLING_DETAILS, CM-PLN-004's) and Edit billing payment methods and pay invoices (BILLING_PAY_INVOICES, CM-PLN-005's, SH-S-7171) are listed only in the Settings category whose `visibleBy` is `!organizationBilling`. The other category lists neither.
  - VIEW_BILLING_DETAILS's title is computed from the user: `({userType:e})=>e==="collaborator"?"VIEW_BILLING_DETAILS_FOR_COLLABORATORS":"VIEW_BILLING_DETAILS"`, 'View billing details' for a collaborator.
  - Flow automations (MANAGE_AUTOMATIONS, MANAGE_AUTOMATION_SETTINGS): the category's `automationsPermissionsEnabled`.
  - Users (MANAGE_STAFF_PERMISSIONS, ADD_REMOVE_STAFF, AUTHENTICATION_MANAGEMENT, STAFF_API_PERMISSION_MANAGEMENT, MANAGE_COLLABORATORS): the category's `({options:{userManagementPermissions:e}})=>e==null||e===!0`. Their `groupPermissions` (StaffManagementUpdate, StaffAuditLogView, StaffManagementCreate and others) are for CM-STF-002.
  - VIEW_BALANCE_BANK_ACCOUNTS (`balanceViewOnly`) and VIEW_ALL_SHOPIFY_CREDIT_TRANSACTIONS (`creditViewOnly`), in Finance.
  - The purchase orders and inventory counts permissions (`inventoryEnhancedPurchaseOrdersPermissionsEnabled`, `inventoryCountsPermissionsEnabled`), in Products (SH-3's split).
- **58 titles in the permission title map with no permission object in the chunk** (`source.js`, the map `Qn`, offsets 23,934 to 32,786):
  - most are the POS roles' permissions, which observed-sh's `docs/GAPS.md` lists as not held: 'Manager approval', 'Manage orders at all locations', 'Manage offline payments', 'Accept offline credit and debit payments', 'Manage receipt settings', 'Customize smart grid', 'Add custom sales', 'Open drawer', 'Manage payment tracking', 'Manage POS UI extensions', and the keys MANAGE_SAVED_CARTS, ENABLE_OFFLINE_CHECKOUT, GIFT_CARD_CASHOUT and others;
  - others are admin ones: BULK_DATA_EXPORT and BULK_DATA_IMPORT (subcategory Bulk data), VIEW_CUSTOMER_DETAILS, EDIT_CUSTOMER_METAFIELDS, MANAGE_STORE_CREDIT_ACCOUNTS ('Manage a customer's store credit'), REDEEM_STORE_CREDIT, COMPLETE_IN_PROGRESS_RETURNS, VIEW_SHOPIFY_PAYMENTS_PAYOUTS, VIEW_ROLLOUTS, VIEW_ABANDONED_CHECKOUTS, MANAGE_CHECKOUT_VALIDATION_SETTINGS and MANAGE_CART_RULES.

  They are titles only: which selector lists them isn't in this chunk. They are leads for CM-POS-001 and its children, CM-MIG-001, CM-LOY-001 and CM-RET-003.

## Problems with the brief or the script

- **The checker's container note** names the eight permissions with nested ones (VIEW_STORE_CREDIT_ACCOUNT_TRANSACTIONS, VIEW_COMPANY_STORE_CREDIT_ACCOUNT_TRANSACTIONS, MANAGE_CHECKOUT_SETTINGS, THEMES, VIEW_PRIVATE_APPS, DOMAINS, CUSTOM_PIXELS_VIEW, APPLICATIONS). Each is a permission placed on its own capability, as the coordinator's check after SH-3 reads these notes.
- **`held_entries.py earlier`** matched the generic titles ('Create and edit', 'View') to other categories' lines, which are no leads. Its name matches (LINKS, REPORTS, OVERVIEWS, PREFERENCES, BILLING_SUBSCRIPTIONS, APPLICATIONS, BILLING_APPLICATION_CHARGES, VIEW_TAX_DOCUMENTS) were the router batches' routes gated by the permission. I kept to them where the route's thing is the permission's, and named them in `reading` where it isn't (P3).
- **The `show` rendering** doesn't say which Settings category an entry stands in (above).
- Nothing in this brief read differently from B-extent.md for these entries.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 72 of 72 entries, no problem and no `CHANGES`. Every line's support is one its cell already holds.
- **S1, decided: one line, no category scope.** A permission listed under both Settings categories, whose `visibleBy` are each other's negation (`organizationBilling` and `not organizationBilling`), holds on every store, so one line with no category scope says what the source does. Two scoped lines would say the same thing twice. A permission's own `visibleBy` stays its scope.
- **S2 to S8 stand,** with SH-3's P1 to P8:
  - Manage Shopify plan's two entries take the two categories' conditions;
  - a `visibleBy` that holds where any of several options is true is `;`-separated;
  - a permission whose own words name a second thing takes a second line (M-6);
  - the companies' store credit permissions take CM-LOY-001 and CM-B2B-002.
- **For the second stage and the amendment:** the permissions the concern map cites only under a condition its cells may lack (VIEW_BILLING_DETAILS and BILLING_PAY_INVOICES, where `organizationBilling` is false; the Users category's own `visibleBy`), and the 58 titles with no permission object in the chunk, most of them POS roles'.
- **Cost:** 8.0 million tokens over 46 requests, about 111,000 an entry. The context reached about 306,000 tokens.
