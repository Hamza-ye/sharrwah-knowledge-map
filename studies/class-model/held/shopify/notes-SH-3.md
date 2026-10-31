# SH-3: notes (Shopify, the last 6 entries of `admin-main-nav`, the 42 of `admin-metafield-types` and the first 39 of `admin-permission-tree`)

Batch SH-3, effort `high`, read under `briefs/H-held.md` and the coordinator's rulings to the one after SH-2. Evidence: observed-sh at `e38dc17e3`. 87 entries, 97 lines in `placements-SH-3.tsv`:
- 86 entries placed on capabilities, 1 `out`, none `new`;
- 96 capability lines, 1 out line.

## `admin-main-nav`: the new trial store's last six items (SH-2's split)

The entries are the end of `ibx5bt-xy@home`'s navigation (run `20260930T074710Z-m0-account`, step 3, `source.html` beside the items). I kept SH-2's N1 to N9 as the coordinator's check after SH-2 kept them, with its two alignments.
- **The Inbox link** (`apps/shopify-inbox`) takes the three lines the check names: CM-SUP-004 `own-service` (the cell's Google Play publisher, Shopify Inc., SH-S-2758; the ruling after SH-2), CM-CHN-001 `core` (N5), and CM-APP-007 `core` for the app handler's page (SH-8's SH-E-55ef27b1).
- **Pin to your navigation** is `out`: a control of the admin's own navigation (an `s-internal-icon` pin in the Inbox item), the admin's own frame (the ruling after SH-37).
- **Apps** is a container on CM-APP-001, the capability its title names, as the concern map placed the same item (SH-S-1535). On this new store it holds only its button **Add** (a `plus-circle` icon), which I read as adding an app to the store, CM-APP-001, its target not held (SH-1's H5).
- **Settings** is CM-ACC-006, as SH-2's N2 placed the same link on the development store.
- **The plan link** 'Trial ends in 2 days', 'Subscribe for $1', Select a plan is CM-PLN-001 `core` with the store's label as scope (SH-1's H11, SH-2's N8). I read 'Subscribe for $1' as the paid trial that the same store's Home banner states, 'Get 3 months for $1/month' (SH-1's line 189), and wrote it as the quality `paid trial: Subscribe for $1`. That is a reading.

## `admin-metafield-types`: the rules I followed

The structure is the Type list of the page Add product metafield definition (Settings > Metafields and metaobjects > Product metafield definitions, `settings/custom_data/product/metafields/create`), on capture-plus, from run `20261008T035518Z-journey-metafield-definition`, step 4 (`004.aria.yaml`, line 188 on; `004.text.txt`, lines 72 to 119). The list holds 1 listbox, 9 groups and 37 options. Five options stand in Recommended and again in their own group, and each of those five is one entry.
- **T1.** Every entry is CM-CNT-002 `core`. The list is the platform's own setting of its custom data: the types a metafield definition can take. No other capability's cell cites the page, a metafield type or these terms (`caps --terms` on metafield, metaobject, custom field, definition, and the options' words; `search` on the concern map's statements found none).
- **T2.** The listbox, named by its search field (Search), is a container (M-13). Its title names nothing, so it goes on the capability of its page. It isn't the ruling after SA-28's grouping, since it holds one capability's things.
- **T3.** Each group (Recommended, Text, Media, Reference, Number, Link, Date and time, Other, Advanced) is a container whose title names a grouping of types, on CM-CNT-002 (M-13). 'Other' is a grouping over one capability's types, so it is placed, not `out`. Media isn't product media (CM-CAT-007), and Advanced isn't the API or the plan (CM-API-001, CM-PLN-001): their leads are by a word only.
- **T4.** Each option is a type, a kind of the list's thing (M-6 refined), on CM-CNT-002. A form the list names in brackets (Choice list and Email of Single line text, Image and Video of File) is read with its base type.
- **T5.** A reference type (Blog post, Collection, Company, Customer, Order, Page, Product, Product variant) names a record a definition may reference. It is named in a list of what may be used, so it takes no line on that record's capability (the ruling after SA-41). Metaobject is CM-CNT-002's own thing either way.
- **T6.** A type whose word is another capability's isn't that capability: Email isn't email marketing (CM-MKT-007) or delivery (CM-NTF-004), Money no payment or balance, Rating not the store's reviews (CM-SUP-001), URL not the store's address or its redirects (the earlier lines on the word URL, CM-SFR-008 and CM-CNT-009), Language not a list of languages (market data).
- **T7.** Scope is empty. The page states no plan, market or store condition for the list. That it was held on one store (capture-plus, on Plus) and for one owner type (Products) is in `reading` and under 'Entries I couldn't tell'.

## `admin-permission-tree`: the rules I followed (for SH-4)

The structure is the staff permission list in the admin chunk `use-store-options-f948ecd551d0.js` (run `20260929T235133Z-admin-chunks-all`, `source.js`): the categories' permission objects (`xe()`) and the title maps. My 39 entries are the categories Home, Orders, Drafts and Products, positions 0 to 40 of `items.jsonl`. Positions 5 and 24, Set payment terms for orders and drafts, have no entry: the concern map cites them in CM-PAY-008 (SH-S-7152, SH-S-7153). SH-4 holds the rest, from View purchase orders (position 41). It hasn't run, as far as I know: the coordinator aligns the two.
- **P1. Each permission is `core` on the capability it gates** (the ruling after ZD-7). I read its title with its category's and subcategory's titles, as a list item is read with its heading (rule 1): 'Manage' under Abandoned checkouts is CM-CHK-007, and 'View' under Drafts is CM-ORD-005. No permission of mine is over the staff's permissions themselves, so none is on CM-STF-002.
- **P2. Read the cell first.** Nearly every permission here is already cited by the cell of the capability it gates, as a placed inventory entry or by its id (C2, S7): CM-ANL-003, CM-ORD-001, CM-ORD-002, CM-ORD-004, CM-ORD-005, CM-ORD-012, CM-MKT-001, CM-PAY-009, CM-PAY-016, CM-PAY-020, CM-PAY-022, CM-SHP-002, CM-SHP-009, CM-RET-002, CM-RET-003, CM-CHK-007, CM-MIG-001, CM-LOY-001, CM-CAT-001, CM-CAT-012, CM-INV-001 and CM-INV-006. Where a cell cites the same permission, the entry takes that capability, with the cell's support.
  - That includes CM-RET-002's note: Refund to store credit is `core` on CM-LOY-001 and `shows` on CM-RET-002.
  - That also includes the Export permissions, which are on CM-MIG-001 (the cell's 'Orders > Export', 'Drafts > Export', 'Products > Export').
- **P3. A lead that is a route or a mutation the permission gates is not the permission's own thing.** Examples are the shipping-address edit route (CM-ORD-002, SH-S-5221), a dispute-evidence mutation (CM-PAY-009, SH-S-6296), a marketplace mutation (CM-CHN-003, SH-S-6231), and a permission that shares the category or depends on it (CM-PAY-008, CM-INV-007). I named such leads in `reading` and gave them no line.
- **P4. A nested permission** (`parent`) takes its own capability's line. It takes its parent's capability's line too only where it is a kind of the parent's act on the parent's thing, and that capability isn't already its own capability's parent in the model (M-6 refined, read for permissions):
  - Apply discounts, under Edit orders, is CM-MKT-001 (the cell cites it) and CM-ORD-002 (a discount added to a placed order is an edit of it; the cell cites an order-edit mutation's need of `apply_discounts_to_orders`, SH-S-6247);
  - Apply discounts under Drafts' Create and edit is CM-MKT-001 and CM-ORD-005, the same way;
  - Buy shipping labels, under Fulfill and ship, is CM-SHP-002 alone: a label is the label service's own thing, a sibling of fulfilment under shipping, and the nesting follows a dependency;
  - View cost, Edit cost and Edit price are CM-CAT-012 and CM-CAT-013 alone, children of CM-CAT-001 in the model, which carries the parent.
- **P5. A title the code computes from the shop is a statement under its condition** (M-14). It takes a line per title, the condition in the source's identifier as its scope: `shopifyPlus`, and `not shopifyPlus` for the other branch, as SA-10 wrote 'plan not basic'.
  - MARK_ORDERS_AS_PAID is 'Record payments' on Plus and 'Mark as paid' elsewhere. MARK_DRAFT_ORDERS_AS_PAID is 'Mark as paid and record payments' on Plus and 'Mark as paid' elsewhere (the `permissionTitles` map in `source.js`).
  - Each title takes a CM-PAY-016 line (the ruling after SH-34 allows the second line). The permission itself is listed on every store, so its other line has no scope: CM-ORD-015 for orders (the cell cites MARK_ORDERS_AS_PAID), CM-ORD-005 for drafts (the cell cites a draft-order mutation's need of the user's access to mark as paid, SH-S-6196).
- **P6. A permission's `visibleBy` is a listing condition the platform sets for the store** (M-11). Manage disputes is listed only where `shopifyPaymentsRbacEnabled` is true, so that is its scope.
  - For SH-4, a suggestion: a category's `visibleBy` (Flow automations' `automationsPermissionsEnabled`, Users' `userManagementPermissions`, the two Settings by `organizationBilling`) would be the scope of every permission inside it, joined to a permission's own with ` and `, as a gate node's is (the rulings after SA-49 and SA-50, T1).
- **P7. A subcategory or category gives a permission no line of its own.** It says where the permission sits in the selector, as the navigation's groups do (SH-2's N5). The concern map already places the group Orders > Returns and refunds on CM-RET-001 (SH-I-0883), and it has no entry here.
- **P8. Terms** are the permission's id, its translation key and its title, where the title names the thing ('View' and 'Export' are kept beside the id, since the cells' terms name them by 'Category > Title').
- **The checker's container note** names the permissions with nested ones (EDIT_ORDERS, FULFILL_AND_SHIP_ORDERS, REFUND_ORDERS, CREATE_AND_EDIT_DRAFT_ORDERS, PRODUCTS, MANAGE_PRODUCTS, VIEW_INVENTORY_TRANSFERS). Each is a permission of its own, placed on the capability it gates, and each nested permission is placed by its own entry. None is a section or a menu.

## New things

None.

## The cells that change, and why

- **CM-CAT-013, Product pricing, gains `core`** (line 92, Edit price, SH-E-b5bde9d3). The cell holds only `extension-point`, from Shopify's four Pricing app categories, and its reading says 'No statement shows Shopify's own pricing of products'.
  - The source states a staff permission over a product's price: `{id:n.EditProductPrice,parent:n.ManageProducts,dependencies:[n.ManageProducts]}`, `EDIT_PRODUCT_PRICE:"Edit price"`, in Products (`source.js`).
  - A reading: a product's price set in Shopify's own admin is the capability's thing. Salla's cell is `core` on its webhook 'when a product's price information is updated' (SA-S-1599). The cost permissions are CM-CAT-012's in the same way, and the brief sends a narrower thing past the broad lead (CM-CAT-001).
  - I kept it. The alternative is under 'Entries I couldn't tell'.
- **CM-ONB-004, `holds nothing`, would become held, `core`** (line 53, the permission Home > Home, DASHBOARD). SH-1's and SH-2's lines on the Home's setup tasks show the same change, not yet amended.
  - The permission gates the Home, which SH-2's N3 reads as a page that is itself two things (CM-ANL-003 and CM-ONB-004; the ruling after SA-19).
  - CM-ONB-004's reading had left 'the staff permission Home > Home (SH-I-0867)' out because nothing then showed setup tasks on the Home.
  - I kept it, as a reading.
- **No other cell changes.** Every other line is `core` where its cell is already `core`. CM-RET-002 already holds `shows`, and CM-SUP-004 `own-service`.

## Entries I couldn't tell, and what would settle each

- **Edit price (SH-E-b5bde9d3): CM-CAT-013 or CM-CAT-001.** If the coordinator reads Product pricing as pricing tools only (automatic pricing, pricing apps), the line goes to CM-CAT-001, a field of the product record, and no cell changes. What would settle it: the capability's definition, which its note says no platform states.
- **The Home permission's CM-ONB-004 line (SH-E-092b7b88).** It rests on SH-2's N3. If the coordinator keeps the permission on the Home's dashboard alone, as the concern map did (CM-ANL-003's note names DASHBOARD), the line goes and CM-ONB-004 changes only by SH-1's and SH-2's lines.
- **The Apps button Add (SH-E-daea7fcf).** Its target isn't in the step's HTML. I read it as adding an app (CM-APP-001). If it opens the App Store, it would be CM-APP-002, CM-APP-001's child. What would settle it: a step that clicks it.
- **The scope `not shopifyPlus`** (lines 62 and 84, the second titles of the two mark-as-paid permissions). This is my notation for the code's other branch, after SA-10's 'plan not basic'. The coordinator may prefer the plans' words.
- **Delete under Drafts (SH-E-24cbff59): CM-ORD-005, not CM-ORD-012.** A reading: a draft isn't a placed order, and CM-ORD-012's cell is orders' deletion and deleted orders kept.
- **Refund to store credit's `shows` on CM-RET-002 (SH-E-c11c2865)** follows CM-RET-002's note and the cell's two rows. The capability's own name says 'to the original payment or to store credit'. If the coordinator lifts the note, the line becomes `core`.
- **Apply discounts' second line (SH-E-f62cacc7, SH-E-903c694f)** puts the permission `core` in two domains (D's CM-MKT-001 and C's CM-ORD-002 or CM-ORD-005), which the merge flags. P4 says why.
- **The metafield type list's reach.** It was held on one store (capture-plus, Plus) and one owner type (Products); the register says 'other owner types may offer other lists'. A list held on another plan or owner type would say whether any type is conditional.

## A structure whose items and sources disagree

- **`admin-metafield-types`.** Its entries name an option once where the source lists it twice (Single line text, Multi-line text, Integer, Image (File) and Metaobject, in Recommended and in their own group, `items.jsonl` positions 2 to 6, and again 8, 10, 15, 22 and 31). An entry doesn't show its group, so my readings name both. `text.txt` renders 'Image(File)' where the ARIA name is 'Image (File)'. The ARIA tree is the structure's source, so its names govern.
- **`admin-permission-tree`.** For a title the code computes (MARK_ORDERS_AS_PAID, MARK_DRAFT_ORDERS_AS_PAID), the items keep the function and `title: null`. The titles are in the source's `permissionTitles` map, which I quote from `source.js`. The items agree with the source on every other field I read.

## What the sources state that no entry holds (for the second stage)

- **The metafield definition page's other fields** (for CM-CNT-002): Definition pinned, the type's One (one value or a list), Add description, Category assignments with Select categories, Options and Storefront API access (`20261008T035518Z-journey-metafield-definition/steps/004.text.txt`, lines 59 to 69).
- **Single line text's validations** (for CM-CNT-002): Validation, Minimum character count, Maximum character count, Regular expression, Unique values only (`steps/010.text.txt`, lines 75 to 86); the run then saves and deletes a definition (steps 13 to 22).
- **The permission chunk's options enum** (`source.js`, offsets 7,762 to 9,206): `shopifyPlus`, `refundToStoreCreditEnabled`, `balanceViewOnly`, `creditViewOnly`, `organizationBilling`, `userAccessResourceRestriction` and others. The chunk computes `unavailablePermissions` from them, but no permission object of my batch is conditioned by `refundToStoreCreditEnabled`. A deeper read of the code that uses them would say whether Refund to store credit is listed only where the store has it on.
- **The navigation's sortable channels**: the Sales channels items are `aria-roledescription="sortable"`, with the drag instructions 'To pick up a draggable item, press the space bar.' (`ibx5bt-xy@home/source.html`). That is the admin's own frame, for no cell.

## Problems with the brief or the script

- **The checker's container note** counts a permission with nested permissions as a container (rule 3). In a permission list, the nesting follows a dependency, not a menu.
- **`held_entries.py earlier`** found earlier lines for only four of the 39 permission ids. The router batches name a route's permission in `reading` only now and then, so the cells (P2) were the lookup that found the places.
- Nothing in this brief read differently from B-extent.md for these entries.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 87 of 87 entries, no problem.
- **The cell changes stand, each read again, as marked readings:**
  - CM-CAT-013 gains `core` from the permission Products > Edit price (EDIT_PRODUCT_PRICE): Shopify's own control over a product's price, as Salla's cell stands on its webhook `product.price.updated`. No platform defines what 'product pricing' does, so whether the capability is pricing tools or the price itself is for the final review.
  - CM-ONB-004 gains `core` from the permission Home > Home, since the Home is the two things SH-2's N3 reads (the ruling after SA-19).
- **The metafield types** stand on CM-CNT-002, each a kind of the list's thing (M-6). The reference types take no line on the records they reference.
- **P1 to P8 stand for SH-4,** with the suggestion taken: a category's `visibleBy` is the scope of every permission inside it, joined to a permission's own with ` and ` (the ruling after SA-56 on nested gates).
- **The checker's container notes** on permissions with nested permissions are prompts, not problems. Each such permission is placed on its own capability.
- **For the second stage:** the metafield definition page's other fields and Single line text's validations, for CM-CNT-002.
- **Cost:** 14.0 million tokens over 80 requests, about 161,000 an entry. The context reached about 311,000 tokens, not the 150,000 the agent estimated.
