# Held pass, Salla, batch SA-21: notes

85 entries (effort high), evidence at observed-sa@b0bd0b163:
- `dashboard-nav`, its last 9 entries (1 to 9):
  - the five sections the coordinator's check after SA-20 added: Orders, Products, Marketing, Store & Channels, Reports (1 to 5);
  - the Reports children Store performance, Smart analytics and Reports (6 to 8);
  - the home segment's Store Summary (9, `prod@segment-home`);
- `dashboard-nav-segments`, its first 76 entries (10 to 85): items.jsonl positions 0 to 75, `@salla.sa/ui-merchant-orders,UpdateOrdersStatus` to `products/trash`.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-21`).

**Placed:** 83 entries on capabilities and 2 `new`, in 93 lines; 0 `out`.
- Supports: 92 `core`, 1 `shows` (channel/chat, 15). No `own-service`, `extension-point` or `outside`.
- No scope, no filler, no quality on any line (the rules below say why).
- Entry 4 (Store & Channels) takes six lines, 40, 41 and 80 two each; every other entry one.

**No batch has placed `dashboard-nav-segments` before.** `SA-22` and `SA-23` hold the rest of it (positions 76 to 156) and haven't run. The rules my segment lines follow are below, so that they can keep to them; the coordinator aligns the three.

## What I read

- The brief and what it names: observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register rows of both structures; `index/ledger-summary.tsv`; both structures' `meta.json` and selection rows; the rulings, their last section included.
- SA-20's placements and notes, with its coordinator's check, first.
- The sources:
  - `dashboard-nav/prod/source.json` (each section's own fields and its children's permissions) and `prod@segment-home/source.json`;
  - every segment answer of my batch, `dashboard-nav-segments/prod/<segment>.json`: each item's Arabic label, `feature`, `permission`, `tags`, `action` and `segment`, which items.jsonl leaves out;
  - `index/run-notes.tsv` for the three segment runs.
- Salla's earlier placements of the same addresses: the routes (SA-7 to SA-12), the nav (SA-20) and the gates (SA-32 to SA-34), joined to their entries' text.
- **To clarify only**, each cited in its reading:
  - the features list, `structures/salla/dashboard-features/demo@en/items.jsonl`, for each page item's feature;
  - `derived/map-steps.tsv` and the sweep steps it names, for the five segments whose page no item names, and for /channel and /marketing, which open the dashboard's 404 page;
  - `20261008T141131Z-sweep-merchant-en/actions.jsonl` step 79 (apps/installed/e-777373355);
  - `20261008T133523Z-sweep-demo-store-en/steps/063.text.txt` (Salla Chat).
- The model: the cells of every capability a line names; `caps --terms` for wallet and verification, the dashboard and its navigation, product sorting, and the partners' messages (below).

## Rules my lines follow

### The navigation's sections (entries 1 to 5)

1. **A section is a container** (rule 3, M-13). It goes on the capability its title names, as the cells show:
   - Orders: CM-ORD-001;
   - Products: CM-CAT-001;
   - Marketing: CM-MKT-005 (its own link Marketing, term التسويق);
   - Reports: CM-ANL-001 (below);
   - Store & Channels names two things, the store and its sales channels (M-6), so two lines: CM-SFR-001 (the online store; the mega menu names the same address Online Store, المتجر الإلكتروني) and CM-CHN-001 (قنوات البيع, as SA-20 placed the child Sales Channels).
2. **Its children are SA-20's entries,** so they take no line on the section entry. The section's address is its first child's page (or, for /marketing and /channel, no page: the dashboard's 404), so it takes no second line.
3. **A permission the section names that no child holds** is read by the ruling on a list of permissions (after ZD-7): `core` on the capability it gates, in a line of its own, its name as the term:
   - Store & Channels: currency_setting_edit (CM-MKS-006), languages_management (CM-MKS-008), store_setting_edit_basic_info (CM-ACC-006), advertisements_browse and advertisements_management (one line, CM-SFR-007);
   - Products: product_sorting_edit. It gates the products' sorting, which no capability holds, so I read it as CM-CAT-001's. Its line would repeat the container's, which the checker refuses, so it is in the container's line: its term and its reading (below, "couldn't tell").
   - Permissions a child holds are a gate on the user: in `reading` (SA-20's rule 4).
   - Orders, Marketing and Reports name none that no child holds; Marketing names none at all.

### The navigation API's answers per segment (entries 10 to 85), for SA-22 and SA-23

1. **An entry is the sub-navigation the dashboard shows at the address its segment names: a container** (rule 3). Its answer names no title. The `segment` its items carry (orders for every orders/* answer) is an identifier like a path's prefix, which the brief says isn't the entry's words.
2. **So it goes on the capability whose page its own path opens** (rule 3's second choice). Where the address is one SA-7 to SA-12, SA-20 or SA-32 placed, I kept to that capability, and to two lines where they gave two (marketing/campaign/retargeting, marketing/carts, products/options).
   - The page is usually one of its own items, whose Arabic label the reading gives.
   - Where it isn't, the reading cites what shows the page: `derived/map-steps.tsv` and its sweep step (customers/settings, marketing/loyalty/points, payments/wallet/store-wallet, products/options/categories), a sweep's action (apps/installed/e-777373355), or the line that placed it (marketing/quick_checkout, marketing/seo/seo-setting).
3. **An address that opens no page** (channel and marketing open the dashboard's 404 page, under their sub-navigation) is a section's address: it goes on the capability the section's title names, as entries 3 and 4. I gave channel only CM-SFR-001: its six items are all the online store's.
4. **The answers that have no page and no section** (main, mega) go to `new:nav`, `core` (M-13's last choice, below).
5. **`supports`:** `core`, as Salla's own admin place, except where the page's own feature is held as not released, or the page says it isn't offered, which makes it `shows` (SA-20's rule 2). In my batch only channel/chat is `shows`: salla_chat is released, but the page says 'Salla Chat is no longer available for new subscriptions.', as SA-8 and SA-32 placed it. SA-22 and SA-23 hold the answers of pages whose features aren't released (customers/register-form, customers/join-requests, feedback/blogs, products/importer, products/metal-pricing, channel/mobile/reports).
6. **No scope.** The answer has no gate of its own; each of its items has its own `feature` (SA-20's rule 6, All products' actions). The page item's feature, with its release, its plans from the features list, its badge and its staff permissions, goes in `reading`, marked "reading, not scope".
7. **Its items are its children, and take no line here** where another entry holds them:
   - every page address an answer lists is a segment of this structure, so an entry of its own, in my batch or SA-22's and SA-23's;
   - each settings drawer (`?settings=/orders`, `/products`, `/customers`, `/coupons`, `/feedback`, `/payments/payment-restrictions`, and `/shipping`, `/markets` in SA-22 and SA-23) is a settings centre section, an entry of `settings-center`, which the reading names by id;
   - the one item no other entry holds is Messages, the drawer `@salla.sa/ui-merchant-salla-chat,ChatListComponent` (feature partners-chat), in manage/experts and marketing/influencers (and their sub-segments in SA-22). I read it as a part of the container's capability, the merchant's conversations with the service providers (CM-PTN-005) or the influencers (CM-MKT-015). It takes no line of its own, since it would repeat the container's. It is named in the reading.
8. **A sub-address that answers its parent's segment byte for byte** (the same sha256) says so in its reading, naming the entry of the first segment that holds the answer. Its items aren't repeated.
9. **`terms`:** the segment itself, and the page item's English label where the entry lists it. The Arabic labels are only in the answer, not in the entry's text, so they are in `reading`.
10. **The two empty answers** (10, `@salla.sa/ui-merchant-orders,UpdateOrdersStatus`; 26, `importer`) go on their address's capability like any other: Bulk status update (CM-ORD-003, as SA-20) and Advanced import (CM-MIG-002, as SA-11). See below.
11. **A tag that is neither New nor Beta** (Salla Point's 'Free Cashier', Merchant Services' 'Essentials', Store design's 'Most Viewed') is a mark, in `reading` only. SA-20 wrote Salla Point's as a price quality on its nav item's line. This line is the sub-navigation's, not the item's, so I wrote none.

## New things

- **`new:nav`**, entries 30 (segment main) and 53 (segment mega), `core`.
  - **What it is:** the dashboard's own navigation as a whole, the sidebar (main: Home and the five sections) and the mega menu (mega: the six sections, Customers among them, and five groups at /more for mobile, Help Desk, Shipping & delivery, Payment, Tools and Logs).
  - **Why `new`:** a container with no title, no group and no page of its own, whose items are many capabilities' places. Named for the API's own path, `ui/v1/nav/prod/nav`; Salla's identifiers are `main` and `mega`. No Arabic name is in either entry or answer.
  - **Its place of its own:** none beyond being the dashboard's navigation answer.
  - **Proposed:** domain A (the merchant's admin), no area, no parent.
  - **Terms searched:** admin; dashboard; navigation; لوحة التحكم; القائمة; mega menu; home page. Homonym: CM-CNT-005 (Navigation menus) is the storefront's menus, not the admin's.
  - **The checker's leads** are the items' capabilities by name or path (CM-ANL-003, CM-CHN-001, CM-SFR-001, CM-SHP-001, CM-SUP-005), each an item's, which its own segment places; CM-AIA-005 and CM-OPS-004 by a word only.
  - **The alternative** is `out`, as a grouping with nothing of its own: each item is placed by its own entry.

## Entries I couldn't tell, and what would settle each

- **10 and 26, the empty answers.** The segment's only words are the address another answer names (the orders and products sub-navigations). By SA-33's check ("a row whose only lines are another page's states nothing of its own"), they could be `out`. I kept them on their capability, so that every segment of the structure places its address; nothing is lost either way, since SA-20 and SA-11 place both addresses.
- **5, Reports: CM-ANL-001 or CM-ANL-002.** The title is Reports / التقارير, CM-ANL-002's term. But the section holds Store performance, Smart analytics and Reports, the three children of CM-ANL-001 (Analytics and reports, whose name holds Salla Reports). I placed it on the parent.
- **2, product_sorting_edit.** It is on CM-CAT-001, by its name, as a part of the products' own thing.
  - The alternative is a new thing, product sorting, with no place of its own (`shows`).
  - The settings centre's section Product sorting options (`products/products.product_sorting`, SA-E-3a948f5b, not yet placed) is the lead.
- **14, channel: CM-SFR-001 alone,** or with CM-CHN-001 as entry 4. Its answer's items are the online store's only, with no channel.
- **64, payments: CM-PAY-001.** The cell cites /payments and Payment methods. SA-32 placed this address's plan gate on CM-PAY-002, the payment service.
- **11, apps: CM-APP-002,** since its page is the App Store (/apps). CM-APP-001's note also names the dashboard app at /apps, so it is the alternative.
- **28, logs/export: CM-MIG-004 alone,** as SA-7's route. SA-32 put the address's gate on CM-TRU-003 too.
- **Messages (33, 45).** I read it as a part of CM-PTN-005 and CM-MKT-015. No capability holds the merchant's chats with partners (caps --terms: messages; المحادثات; محادثة; partners-chat; chat with partners; conversation). If another platform gives partner messaging a place, it is a new thing.

## A structure whose items and sources disagree

- **items.jsonl lists only each answer's top-level urls and English labels.** The answers hold much more:
  - each item's Arabic label, `feature`, `permission`, `tags`, `isNewFeature`, `isBeta` and `action`;
  - for main and mega, every section's nested children with their own features and actions.

  The source governs: I read every answer, and cite each in its line.
- **Each item carries a `segment` naming its own section,** which isn't always the segment asked: the answer for customers/groups carries `customers`, and logs/audit's carries `logs`. This bears out the register's 'a sub-address answers its parent's segment byte for byte'.
- **marketing/carts' items are written without a leading slash** (`marketing/carts`, `marketing/carts/reminders`), as the run note says.

## What a source states that no entry holds (for the second stage, and for SA-17 to SA-19)

- **The mega menu's nested children** (`dashboard-nav-segments/prod/mega.json`) name places the segment answers list nowhere at top level:
  - under Help Desk: Reviews & questions (/feedback), Self-service system (/tickets), Quality gateway (shipping/tickets), Salla Chat and Complaints (/manage/complaints);
  - under Customers: Staff (url #), Staff members (/users), Roles & permissions (/users/roles) and Employees targets (/users/targets, feature app_pos);
  - under Tools: Developer Tools (/manage/webhooks, CM-API-009's term Developer tools) and Referral program (/marketing/referrals, feature affiliate-referral);
  - under Logs: Inventory log, Deleted orders, Deleted products, Digital card history and Translation log beside Activity history, Export log and SMS log. Salla's own grouping puts the deleted items and the inventory and card histories among its logs. That is a lead for CM-TRU-003's and CM-MIG-004's notes.

  `dashboard-main-navigation` (SA-17 to SA-19) holds the rendered menu and may hold them as entries. The segments more and tools (SA-22, SA-23) hold the groups as items, with the same children nested.
- **The channel sub-navigation holds Translation log** (/manage/languages/logs, feature languages), which the main navigation's Store & Channels doesn't list as a child. It bears out the section's permission languages_management (entry 4's CM-MKS-008 line).
- **The Store & Channels and Products permission lists** are placed above. Which page each such permission opens isn't stated.

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that already holds `core`, and channel/chat's `shows` falls on a cell that holds `core`.
- **`NOTE` line 25, core on a product named with the platform's brand (Salla Point):** `core` by Salla's own dashboard link, the cell's /channel/sallapoint, as SA-20 and SA-32 placed it. No maker is needed for `core`.
- **`NOTE` line 11, Reports a container:** yes, rule 3 (above).
- **`NOTE` lines 36 and 61, a new thing whose entry has leads:** read above. Each lead is an item's capability, placed by the item's own segment.
- **`NEW`: nav, 2 lines.**

## Problems with the brief or the script

- **The checker refuses two lines of one entry on one capability.** Products' permission product_sorting_edit, read as CM-CAT-001's, would have repeated the container's line, so the two are one line. Likewise the Messages drawer, a part of the container's capability.
- **A segment answer stands for the page that asks for it and for the section's sub-navigation together.** The brief's rules for containers (title, group, own path) fit it only through the second choice, and the section is placed by its own root segment and by the nav's section entries. A rule for answers shared byte for byte across a section's pages would make the three batches' lines surely the same.
- **items.jsonl's rendering leaves out the Arabic labels,** so a segment line's terms can only be English labels and the segment, though the answer gives both languages.
