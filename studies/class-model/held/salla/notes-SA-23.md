# Held pass, Salla, batch SA-23: notes

132 entries (effort high), evidence at observed-sa@b0bd0b163:
- `dashboard-nav-segments`, its last entry (1): `shipping/setting`, items.jsonl position 156;
- `dashboard-quick-actions` (2 to 4), the icon bar;
- `dashboard-restrictions` (5 to 27): the five restriction groups the build now gives entries of their own (5, 12, 14, 18, 25; SA-20's check) and their options;
- `dashboard-settings-menu @merchant@ar` (28 to 54), the settings panel's Arabic list;
- `dashboard-staff-roles` (55 to 69);
- `dashboard-webhook-events` (70 to 132).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-23`).

**Placed:** 126 entries on capabilities, 1 `new`, 5 `out`, in 144 lines.
- Supports: 132 `core`, 11 `shows`. No `own-service`, `extension-point` or `outside`.
- Scope on 3 lines only: the market restriction, a store's value (10: store-sherawya; 27: dandye-dandy-ksa). No filler, no quality.
- No batch had placed five of the six structures. For `dashboard-nav-segments` I kept to SA-21's and SA-22's rules and the coordinator's checks after them.

## What I read

- The brief and what it names: observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register rows of my six structures; their `meta.json` (`show --meta`) and selection rows; the rulings, their last section included; B-extent's "Cells and evidence" and conventions; the evidence map.
- SA-21's and SA-22's notes and their checks (the segment rules); SA-20's check (the restriction groups); SA-24's and SA-25's notes and placements (each docs event's capability), SA-13's line for the route /shipping/setting, and SA-8, SA-21 and SA-32's lines for /channel/chat.
- **The sources:**
  - `dashboard-nav-segments/prod/shipping~setting.json` (its sha256 against `shipping.json`: the same) and `more.json` (the more menu's nested Shipping Settings);
  - `dashboard-quick-actions/merchant@en/source.html` and items;
  - `dashboard-restrictions/demo@en/source.json` and `real-merchant@en/source.json`, whole, the option values included (the selection drops them from the entries; I read them to clarify only);
  - `dashboard-settings-menu/merchant@en/items.jsonl` beside the Arabic one, and the concern map's statements for the English links (SA-S-1677 to SA-S-1702) with the cells that cite them (`merged/evidence.tsv`);
  - `dashboard-staff-roles/*/source.json`;
  - `dashboard-webhook-events/demo@en/source.json` (the same bytes as real-merchant@en's).
- **To clarify only**, each cited in its reading: `derived/map-steps.tsv` and `20261008T133523Z-sweep-demo-store-en/steps/263.text.txt` (the page /shipping/setting) and `steps/228.text.txt` (/manage/webhooks/new, where the event list is fetched) and `steps/063.text.txt` (Salla Chat); `20261008T210339Z-journey-staff-demo/steps/001`, `002`, `003` and `005.text.txt` (staff, roles, a role, a new role); `docs/PLAN.md`'s instruments, for the stores behind the labels (demo@en is store-sherawya, Pro; real-merchant@en is dandye-dandy-ksa, Pro); `dashboard-translations/en/products.json` (pinning a product); `docs-event-lists/webhooks/source.md`, lines 293 and 294.
- The model: the cells of every capability a line names, and `caps --terms` for restrictions, staff access, product types, pinned products, search, settings and domains (below).

## Rules my lines follow

### The segment (1)

SA-21's rules, with the checks after SA-21 and SA-22: a container on the capability of the page its own address opens, no scope, its items no line. `shipping/setting` answers the shipping segment byte for byte, and no item of the answer names its page, so the line rests on the sweep's step for the address (SA-22's rule 5): 'Shipping settings', the cell's term, as SA-13 placed the route (SA-E-bdd0d1e4). CM-SHP-001 `core`.

### The icon bar (2 to 4)

- **2, the search button's tooltip 'Use ⌘ + F for quick search':** it names a feature, a search of the admin, so it isn't a bare UI string. No capability holds it: `new:quick search`, `shows` (below).
- **3, the icon link to /channel/chat:** CM-SUP-004 `shows`, as every earlier line for Salla Chat ('Salla Chat is no longer available for new subscriptions.').
- **4, Settings at /?settings=%2Fprofile:** a container, the settings panel, on the capability its title names. CM-ACC-006's cell holds Salla's Settings: the access scope Settings / الاعدادات (SA-S-1565), the dashboard app serving /settings (SA-S-3586) and the plan line searching the store's settings. The profile page it opens takes no second line: the panel's own link places it (29), and the page isn't itself two things (the ruling after SA-22).

### The restrictions (5 to 27)

1. **What they are:** what a staff role's permission can be narrowed by (the register; GET /admin/v2/users/restrictions), on a role's page. The five groups' ids are permissions' names (orders.view, orders.create, orders.edit, products.view, users.dashboard); each option narrows one by a dimension (status, branch, market, …).
2. **Each group is a container** (the coordinator's message; rule 3) on the capability its title names: عرض الطلبات CM-ORD-001, إنشاء الطلبات CM-ORD-005, تعديل الطلبات CM-ORD-002, عرض المنتجات CM-CAT-001, الوصول الى لوحة التحكم CM-STF-001.
3. **Each option is `core` on the capability it gates,** by the ruling on a list of permissions (after ZD-7): a restriction narrows a permission, and isn't a permission over the staff's permissions, so it takes no CM-STF-002 line. The alternative is below ("couldn't tell").
4. **A dimension that is a capability of its own takes a `shows` line** (M-6): the order's status (CM-ORD-003), the branch or warehouse (CM-INV-005, for orders and for products), the market (CM-MKS-001), the order's sales channel (CM-CHN-001), the product's category (CM-CAT-003) and brand (CM-CAT-005). That follows SA-25's export columns, whose named things took `shows` lines. A dimension that is a field of the record, with no capability apart, is in the record's own line: the product's status, pinned mark and type (CM-CAT-001); the order's country and city (one store's data and market data, CM-ORD-001 only).
5. **15, edit orders to a given status:** two `core` lines, order editing (its words تعديل الطلبات and its group) and order statuses (what it gates, the cell's own permission order_edit_status_all).
6. **26, منع الوصول, blocking a role's access to the dashboard:** CM-STF-001, the staff account's access to the admin, the cell's 'the people other than the owner who work in the store's admin'.
7. **The market restriction, a store's value** (H-held rule 4, flags): `is_available` true on store-sherawya (10), so `core` with that store as scope; false on dandye-dandy-ksa (27), with no option values, so `shows`, that store as scope. Both stores are on Pro, so the plan doesn't decide it. I read it as the store's own markets (store-sherawya has one market, 'متجر Saudi Arabia'), a reading.
8. **No scope on the rest:** both stores answer the same groups and options; their option values (each store's statuses, branches, categories and brands) are one store's data, quoted in `reading` only.
9. `isDisabled: true` on every group isn't explained by the answer; it is in `reading`.

### The settings panel's Arabic list (28 to 54)

1. **Each link is the same element as the English list's link** at the same place and address, which the concern map holds (SA-S-1677 to SA-S-1702). One thing in two languages (the ruling after SA-4): the same capability as the cell that cites the English one. `core`, as those cells.
2. **Two lines where the Arabic words or the page name two things:**
   - 34, الرصيد والفواتير: CM-PLN-004 (billing), as the English line, and CM-PLN-006 (the store's balance, الرصيد). Both languages name the balance ('Balance & billing'); the concern map's line gave the English link CM-PLN-004 only;
   - 38, الضرائب at /taxes-and-duties: CM-TAX-001 and CM-TAX-008, as the concern map cites SA-S-1686 on both, the page's own address naming duties.
3. **One line where the concern map gave two but the words name one:** 44, الشحن والتوصيل, CM-SHP-001 only. The concern map's SA-S-1692 is also `shows` on CM-SHP-002 (the platform's labels), which the link's words don't name.
4. **The badge جديد** (42, 48, 49) is a release badge: in `reading` (D1). The terms are the link's words without it (المنتجات, برنامج الولاء, نظام الإهداء).
5. **46, التسويق at /coupons:** CM-MKT-005, as the English line. The address opens the coupons' settings (CM-MKT-002), which I didn't take as a second line: the words name marketing.
6. **The group headings are containers** (rule 3, M-13), with no address:
   - الحساب (28) on CM-ACC-001, the account its title names;
   - المتجر (33), العمليات (41) and المزيد (52) name only a grouping of several capabilities' settings, and no capability is the store itself. M-13 places a container on what "its title or its group names": their group is the settings panel, Settings, CM-ACC-006's (rule 2 above). So CM-ACC-006 `core`. See "couldn't tell" for the alternatives.
   - The English list's headings (Account, Store, Operations, More, positions 0, 5, 13, 24) have no statement in the concern map, and no entry: only the Arabic ones are entries.

### The roles (55 to 69)

1. **The ten default roles** (type default, on both stores) are Salla's built-in roles: CM-STF-002 `core` each. The cell's reading says its statements name no built-in role and their number isn't held; these ten name them (the demo store's list shows the same ten, `steps/002.text.txt`).
2. **Their permissions aren't held** (the register: each role's own answer, /admin/v2/users/roles/<id>, not held), so a role's name is all it states of what it gates. I gave no role a line on the capability its name points to (finance, design, technical, marketing, products, orders). The ruling on a list of permissions places permissions, and these entries are roles.
3. **64, التاجر (slug user):** CM-STF-002 and CM-ACC-001, the store's owner: the staff list shows the owner with the role 'Store Owner' (`20261008T210339Z-journey-staff-demo/steps/001.text.txt`, line 40).
4. **65 to 69, type custom, on dandye-dandy-ksa only:** `out`, one store's own data, roles its merchant made and named (one holds a person's name, 'يونس مسوق'). That merchants make roles is CM-STF-002's already (New role, `steps/005.text.txt`).

### The webhook events (70 to 132)

1. **Each event is `core` on the capability of what it is about** (SA-24's rule, its check), with the capability SA-24 and SA-25 gave the same event of the docs' lists. Every event of this list is in theirs but these, which I placed by the cells' own terms or the event's resource:
   - abandoned.cart.purchased (74) and abandoned.cart.update (117): CM-CHK-007, the cell's terms;
   - wallet.action and wallet.expiry.reminder (79, 80): CM-LOY-001, the customer wallet;
   - product.variant.updated and product.option.updated (97, 98): CM-CAT-002;
   - product.quantity.updated (100): CM-INV-001;
   - product.channels.changed, product.publish, product.unpublish (105, 107, 108): CM-CHN-001, the cell's terms;
   - category.deleted (110): CM-CAT-003;
   - category.channels.changed (111): CM-CHN-001 and CM-CAT-003;
   - store.owner.changed (132): CM-ACC-001, the cell's term.
2. **shipping.zone.created and .updated** (86, 75) take CM-SHP-015 too, as SA-25 did, since their labels name a carrier's pricing ('انشاء تسعيرة شركة شحن', 'تعديل تسعيرة شركة شحن'), which SA-24's notes suggested.
3. **The subscription events** (81 to 85) are `core` on CM-SEL-001 here. SA-24 placed the docs' Recurring Payments events `extension-point`, by the docs' 'authorized third-party apps'. Here the list is the merchant's own webhook in the admin, Salla's topic for its own feature.
4. **product.updated and product.available** (101, 103) are `core`: this list offers them unstruck, where the Webhooks page strikes them (SA-25's `shows`).
5. **The list's own line: CM-API-009 `core`, one line for all 63** (rule 6: consecutive, one structure, the same placement). It is the Event type list of the dashboard's new webhook ('The event that triggers the webhook notification.', `steps/228.text.txt`, line 24), at Store management > Webhooks, the cell's /manage/webhooks. I gave no CM-API-008 line: SA-24's notes put this list on CM-API-009 alone, its child.
6. **No scope:** the answer states no plan. Both stores are on Pro, and the cell's flag webhooks is for pro and special (reading).

## New things

- **`new:quick search`**, entry 2 (SA-E-ac20d921), `shows`.
  - **What it is:** the search button of the dashboard's icon bar, with the tooltip 'Use ⌘ + F for quick search' (`dashboard-quick-actions/merchant@en/source.html`, the icon hgi-search-01). What it searches (pages, orders, products, settings) isn't stated: the register says 'what each unlabelled button opens is not recorded yet'.
  - **Its place of its own:** none. It is one button of the icon bar, with no route or section.
  - **Proposed:** domain A (the merchant's admin), no area, no parent. If it searches the settings only, it is CM-ACC-006's plan line ميزة البحث في إعدادات المتجر (SA-S-2087), and not new.
  - **Names:** quick search. No Arabic name is held in the entry; the dashboard's translations may hold one.
  - **Terms searched:** search; البحث; بحث; quick search; admin search; keyboard shortcut; shortcut. Nearest: CM-SFR-013 (the storefront's search and filters, the checker's lead by the word search) and CM-ACC-006 (the settings search).

## Entries I couldn't tell, and what would settle each

- **The restrictions: on the capability gated, or on CM-STF-002.**
  - A restriction is part of how a role is defined: it narrows a role's permission by the data it reaches (statuses, branches, countries, markets, channels, categories, brands, product types).
  - I read it as the ruling on a list of permissions reads a permission: on the capability it gates, since it isn't a permission over the staff's permissions.
  - The alternative is a line on CM-STF-002 for each group, as the role system's own narrowing. CM-STF-002's note keeps 'the platform's permission system itself' there, and a role's restrictions could be read as that.
  - Neither the model's cells nor the rulings name restrictions of a role. Shopify's staff restricted to locations, if a cell holds it, would show how the class reads it.
- **The settings headings المتجر, العمليات, المزيد (33, 41, 52): CM-ACC-006,** by M-13's "its group".
  - The first alternative is M-13's last choice, `new:<title>` `core`.
  - The second is `out`, by the rulings after SA-21 and SA-22, as a container naming only a grouping across several sections. Those rulings limit themselves to a container 'with no title of its own', and these have titles, so I didn't take it.
  - الحساب (28) is on CM-ACC-001 by its title, the account. CM-ACC-006 is the alternative there too, by its group.
- **4, Settings, the icon bar's link: CM-ACC-006.** If the coordinator reads the settings panel as a container over the whole admin, it is `out` by the ruling after SA-21. The cell's own Settings (access scope, app) is why I didn't.
- **The roles' areas** (56 to 61): CM-STF-002 only. If a role named for an area is read by M-6 as naming that area's thing, each takes a `shows` line (finance: CM-PLN-004 or CM-PAY-*; design: CM-SFR-001; technical: unclear; marketing: CM-MKT-005; products: CM-CAT-001; orders: CM-ORD-001). The roles' own answers, with their permissions, would settle it.
- **20, pinned products:** in CM-CAT-001's line. If pinning a product (Pin product, `dashboard-translations/en/products.json`) is the products' sorting, it goes with the new-thing decision on product sorting that SA-21's check left open (product_sorting_edit).
- **80, wallet.expiry.reminder:** CM-LOY-001 only. Its label says the wallet's balance nears its end (انتهاء). Whether that is an expiry date of the balance, and its period, isn't stated: a lead for a quality on CM-LOY-001.
- **13, draft only:** CM-ORD-005. The option value 'إنشاء مسودة فقط' says the merchant's orders can be created as drafts, which the cell's note says isn't stated ('Whether Salla's manual order passes through a draft stage … isn't stated'). The coordinator may want the note changed.

## A structure whose items and sources disagree

- **`dashboard-restrictions`:** the entries leave out the option values (the selection's `drop:`), which are each store's data. On dandye-dandy-ksa the market option has `is_available: false` and no values key at all, which is why it is an entry of its own (27).
- **`dashboard-nav-segments`:** as SA-21 and SA-22 found, items.jsonl lists only the top-level urls and English labels. `shipping/setting` answers the shipping segment byte for byte, and no item of it names /shipping/setting. The more menu nests it as 'Shipping Settings' / 'إعدادات الشحن' (`more.json`).
- **`dashboard-webhook-events`:** the dashboard's list holds no order.* event at all (none of its 63 names begins `order.`), where the docs' lists and the Partners portal's catalog hold many. The register notes 79 in the portal; `derived/links.tsv` compares the three. I didn't trace why: it may be that orders' events are offered elsewhere, or not to a merchant's own webhook. The admin page that held the select (`steps/228.text.txt`) doesn't say.
- **`dashboard-settings-menu`:** the Arabic text runs the badge into the label ('المنتجاتجديد', 'برنامج الولاءجديد', 'نظام الإهداءجديد'), as the English does ('ProductsNew').

## What a source states that no entry holds (for the second stage)

- **The new webhook's form** (`20261008T133523Z-sweep-demo-store-en/steps/228.text.txt`):
  - lines 26 to 28: 'Webhook version', 'Salla supports v1 as well as the more advanced v2 version.' This is a lead for CM-API-008 and CM-API-006;
  - lines 30 and 31: 'Advanced condition (optional)', 'Send event data only when specific conditions are met.' This is the conditional webhooks, CM-API-010, in the merchant's admin, as SA-24's notes found the docs say.
- **The shipping settings page** (`20261008T133523Z-sweep-demo-store-en/steps/263.text.txt`), toggles no entry of mine holds. The settings centre's entries may hold them (SA-48 to SA-63):
  - line 21, 'Validate recipient mobile number by shipping country';
  - line 23, 'Cash on delivery' rules (CM-PAY-029);
  - line 26, 'Allow carriers to update order status' (CM-ORD-003 and CM-SHP-015);
  - line 28, 'Allow carriers to sync inventory' (CM-INV-001);
  - line 34, 'Auto-assign warehouse by customer city' (CM-INV-005);
  - line 36, 'Allow carriers to generate shipping labels for new orders' (CM-SHP-002);
  - line 38, 'Display carriers using Salla’s recommended order';
  - line 40, 'Require identity details for customs' (CM-TAX-008 and CM-SHP-020).
- **The restrictions' option values** (`dashboard-restrictions/*/source.json`), dropped from the entries:
  - the sales channels an order comes from: 'مستعرض جوال', 'مستعرض كمبيوتر', 'تطبيق محلي' (Mahally, CM-CHN-002), 'تطبيق نقاط البيع' (the point of sale), 'سوق الجملة' (the wholesale market) and 'صفحات الهبوط' (landing pages, CM-SFR-006);
  - the product types: Physical Product, Custom Service, Group of Products, Digital Card, Digital Product, Food & Beverage, Bookings. These are leads for the cells of digital products, bookings and bundles;
  - the order-edit options, 'إضافة كوبون خصم للطلب' (CM-MKT-002 on an order, CM-ORD-002) among them, and the order-information options, edit all but the customer's, shipping or payment data.
- **The roles' permissions:** not held (the register). A role's own answer would say what each default role gates.

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that already holds `core`, and each `shows` line on a cell that holds `core`.
- **`NOTE` line 3, a new thing whose entry has leads (CM-SFR-013):** read. CM-SFR-013 is the storefront's search and filters (Product filter settings, salla-search). The entry is the admin's search, so not that cell's thing.
- **`NOTE` line 12, the first lead CM-INV-010 holds nothing (9, العرض حسب المدينة):** a lead by the words حسب and مدينة only. CM-INV-010 is Zid's products shown to a buyer by the buyer's city. The entry narrows a staff role's view of orders by city, so it isn't that thing.
- **`NOTE` lines 6, 17, 19, 24, 34, containers:** yes, the five restriction groups (rule 2 above), each on the capability its title names.
- **`NEW`:** quick search, 1 line.

## Problems with the brief or the script

- **A restriction is neither a permission nor a setting,** and the brief's rules name neither case. I followed the ruling on a list of permissions by analogy (above). One ruling for a role's restrictions would settle all five groups.
- **The selection's `drop:` takes the option values out of the entries,** so the restrictions' words that name the sales channels and product types can't be terms or lines here. They are in the notes for the second stage.
- **The settings-menu structure's English headings have no statements,** and its Arabic headings are entries. The two lists are one element in two languages, so the Arabic entries are the only place the headings are placed.

The checker's last line, for SA-23: `132 of 132 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **The restrictions take a new thing as well: `new:Staff access restrictions`** (entries 5 to 27, 23 lines). A restriction limits a staff role to a subset of the store's records: orders by status, branch, market or sales channel; products by category or brand.
  - Roles and permissions (CM-STF-002) say what a role may do; a restriction says which records it may do it on. No capability of the class holds that.
  - Architecturally, it is a filter on the records every page and API call reads.
  - The lines on what each restriction gates stand beside it, as the notes placed them. The new line takes each entry's own support and scope (the market option's store values).
  - It is proposed under CM-STF-002 and decided with every platform's new things. Shopify's staff limited to locations, and Zid's employees by branch, are the leads to look for.
- **The settings panel's headings stand** on CM-ACC-006, by M-13's group: الحساب on CM-ACC-001, and المتجر, العمليات and المزيد on CM-ACC-006. Each is titled and over one part of the admin, so the rulings after SA-21 and SA-22 don't make them `out`.
- **The roles stand:** the ten default roles on CM-STF-002, and the five custom roles `out` as one store's own.
- **The webhook events stand,** each `core` on what it is about, with the form's grouped CM-API-009 line. That the dashboard's list holds no `order.*` event is a lead for the second stage.
- **New things:** quick search (2), and Staff access restrictions.
- **Cost:** 14.3 million tokens over 73 requests, about 108,000 an entry. No cell changes.
