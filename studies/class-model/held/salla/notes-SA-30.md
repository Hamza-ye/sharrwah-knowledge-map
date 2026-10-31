# Notes: held pass, Salla, batch SA-30 (`permission-gates`, second part)

130 entries, effort high, evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-30`). Entry n is `derived/permission-gates.tsv` line n + 78.

**Placed:** 122 entries on capabilities, 5 `new` (each an earlier batch's new thing), 3 `out`, in 163 lines. Supports over the lines: 115 `core`, 39 `extension-point`, 6 `shows`. No filler and no quality: no entry names a third party, a limit or a price. Scope only on portal items whose menu code names a feature (16 lines).

| Part | Entries | Table lines | Lines | Placement |
| --- | --- | --- | --- | --- |
| dashboard rows | 1 to 35 | 79 to 113 | 46 | 32 capability, 2 new, 1 out (35, /tools) |
| portal rows, the admin's menu (`admin: true`) | 36 to 91 | 114 to 169 | 73 | 51 capability, 3 new, 2 out (36 Dashboards, 41 Admins) |
| portal rows, the partner's menu | 92 to 130 | 170 to 208 | 44 | 39 capability |

## What I read

- The brief, `H-held.md`; the coordinator's rulings, `held/review-H-rulings.md`, to its last section; SA-29's notes and placements (P1 to P8 and the coordinator's check).
- observed-sa's `README.md`, `docs/GAPS.md`, `structures/README.md`, and `docs/READING.md` where it names the derived tables; the register's row and `selection.tsv`'s row for `permission-gates` (`decides`, rule `rows:derived/permission-gates.tsv:.`).
- `capture/gates.py`, its header and the part that writes the permission rows: a dashboard row is the union of the navigation entries' `permission` at one address; a portal row is one item of `structures/salla/portal-menu-definitions/<label>/items.jsonl` (title, route, permissions, feature, `admin`), beside whether the held partner's `/me` holds each permission, whether its private-settings hold the feature, and whether the rendered side menu shows the title.
- **For each address's line:** the placements of SA-7 to SA-14, SA-20 to SA-23 and SA-32 to SA-34 for each dashboard address, and of SA-28, SA-29 and SA-34 to SA-38 (and SA-44's check) for each portal route the menu items name, with each batch's coordinator's check.
- **Sources, to clarify only:** `structures/salla/dashboard-nav-segments/prod/more.json` and `tools.json` (the groups at /more and /tools); `structures/salla/portal-menu-definitions/layout-mf@prod/items.jsonl` (each item's children, feature and `admin`); `structures/salla/staff-permission-groups/demo@en/items.jsonl` (the permissions' groups); `structures/salla/partners-portal-navigation/partner@en/items.jsonl` (the rendered titles); the two demo-store steps whose lines the table quotes (`raw/runs/20261008T133523Z-sweep-demo-store-en/steps/086.text.txt` and `raw/runs/20261009T000815Z-sweep-nav-unreached-demo-en/steps/001.text.txt`, found through each run's `actions.jsonl`).
- The cells of every capability I placed on, or a lead named (`held_entries.py cells`), and `class_slice.py caps --terms` for the permissions no lead named.

## The structure's split

- **SA-29** holds table lines 2 to 78 (dashboard rows to /marketing/carts/reminders). I hold lines 79 to 208: the rest of the dashboard rows and layout-mf's first 95 portal items, to Payments (route None).
- **SA-31 holds lines 209 to 331 and hasn't run:** layout-mf's last 14 items (from Payouts) and ui-partners-portal-layout's 109 items, the same menu again from the other bundle, titled by locale keys (`navigation.admin_users` and so on). Its items stand for the same routes, so the rules below should hold for them; the coordinator aligns the two.

## Rules my lines follow

### Dashboard rows: SA-29's P1 to P8, kept

- **P1.** Each row goes on its address's capability, with the support the address's batches gave it, cited by entry id in `reading`. The section's general permission (shipping_options_management, products_management, customer_management, users_management, order_management) is in that line.
- **P2.** A permission that names another capability's thing takes its own `core` line there, on the capability whose cell holds the permission:
  - shipment_history_management on CM-SHP-002;
  - list_epayments on CM-PAY-005;
  - wallet_and_invoices_management on CM-PLN-004, and payments_operations_management on CM-PAY-020, on /payments/wallet;
  - products_stock_management on CM-INV-001;
  - customer_block on CM-CUS-005;
  - campaign_browse and campaign_management on CM-MKT-005, on the influencer campaigns' archive.
- **P3.** /users/roles is Roles & permissions, a page over the staff's permissions themselves, so its line is CM-STF-002's, as every earlier batch placed the address. /users and /users/targets keep CM-STF-001 and CM-STF-004.
- **P4.** /shipping/delivery-promises stays `shows`: its feature isn't released (SA-13, SA-32).
- **P5.** No scope on a dashboard row.
- **P6.** Two rows quote the demo store's 'Access restricted' lines, and both stand on the page's own view, under its breadcrumb:
  - /products/card-logs, step 086, lines 25 and 26, under 'Digital card history';
  - /products/certificates, step 001 of the nav-unreached sweep, lines 20 and 21, under 'Certificate templates'.

  No row of mine is a drawer over the home page with store lines. The two drawer rows (/?settings=/shipping, /?settings=/payments/payment-restrictions) quote no store's lines, so SA-33's case doesn't arise. The plan gate's row at /?settings=/shipping is SA-33's `out` for that reason, and its permission row isn't.
- **P7.** `held`, '(not swept)' and the portal rows' /me, private-settings and rendered-menu columns are the repository's observations. None is a term, a scope or a quote.

### Two dashboard rows that are menus

- **/more (8):** its permissions are the mobile menu's group Customers (العملاء, id 287, `more.json`), and its `{}` is the empty permission of the menu's other five groups. The menu itself is `out` (the ruling after SA-22). A group whose address is the menu's keeps M-13 where an entry is about it, as SA-32 placed the Shipping group's gate. So the row goes on CM-CUS-001, with customer_block on CM-CUS-005.
- **/tools (35):** its only permission is `{}`, the empty permission of all five groups at /tools. The row states no permission, and the menu is `out`, so the row is `out`.

### Portal rows

- **Q1. The route's line.** Each menu item takes the capability and support that SA-34 to SA-38 gave its route, and that SA-28 and SA-29 gave the same link in the rendered menu. I matched a route name (`applications-requests-index`) to its path through those batches' readings, which name both.
- **Q2. Support (the coordinator's message for SA-30).** I kept each row's support as its route's line has it:
  - `extension-point` for the partner's own tools (apps, themes, bundles, services, affiliates, influencers, agency);
  - `shows` for store management (a partner's access requests) and domains (behind domain-purchase, which the held partner lacks);
  - `core` for the rest.

  The brief's ruling says a permission of the Partners portal is `core` on what it gates. I read that as saying the permission isn't `shows` or `out`, like SA-29's reading of D1, and the ruling after SA-44 reads a partner's feature the same way. If `core` is meant literally, see "Entries I couldn't tell".
- **Q3. The admin's menu** (items with `admin: true` in the menu code) is Salla's own admins' place: `core` where it manages a partner or marketplace thing, by SA-34's rule 5, which the coordinator confirmed. Two items are `out`: Dashboards (dashboard-analytics, /admin/dashboard, `out` in SA-34 and SA-36) and Admins (admins-index, /admin/admins, Salla's admin team).
- **Q4. Containers.** An item with route None and children is a container (M-13). It goes on the capability its title names, which is also the one its children's routes took. A second line goes on a capability that the title, or a permission, names as a second thing:
  - the admin's Influencers and the partner's Influencer and agency.influencerProfiles take CM-MKT-015 and CM-PTN-009;
  - Themes (route myThemes) takes CM-SFR-005 for manage-bundles;
  - Marketing Tools takes CM-APP-003 for manage-coupons;
  - the admin's Stores takes CM-DVT-005 for manage-development-stores;
  - My Subscriptions and Payments take SA-29's two lines.
- **Q5. Scope.** A feature the menu code gives the item is its scope, in the code's identifier, as SA-36's check had for layout-mf's features. Whether the held partner's private-settings hold the feature is the repository's observation. I write it in `reading` only as such, and it sets no support, except where the route's batch already set it: domains stay `shows`.
- **Q6.** The code's choice between two routes (`reports-dashboard or user-dashboard`, `services-list or my-services`) only chooses a page. It goes in `reading` (SA-35's check), and the line takes the route the rendered menu opens.
- **Q7.** A route's own gate that the menu item doesn't state, such as `requiresThemeAccess` on /themes or `assign-orders` on /services/orders, isn't this entry's scope. I name it in `reading` where it helps.

## Each new thing

None of my own. Five entries take earlier batches' new things, under the same names:
- `new:Bullet Delivery` (13, /shipping/bullet-delivery), SA-13's;
- `new:Product certificates` (33, /products/certificates), SA-22's;
- `new:VIP Partners` (38 Home at vip-dashboard; 43 VIP Partners), SA-34's;
- `new:Transfer Requests` (48), SA-34's.

The checker's notes on their leads (CM-STF-002, CM-SHP-001, CM-CAT-001, CM-INV-006 and others) come by a field's name or a common word. None of those cells is the new thing's.

## Entries I couldn't tell, and what would settle each

- **The support of the partner's rows (Q2).** If the ruling's `core` is meant literally, the 39 `extension-point` lines (38 of entries 92 to 130, and 53's second line) and the 5 `shows` lines (124 to 128) become `core`. Only one cell would change: CM-SFR-005, whose Salla cell is `extension-point` alone (entries 93 and 95, and 53's second line). Every other cell on those lines already holds `core`. The coordinator's message for this batch asked for the address's support, and I followed it.
- **11, /shipping/operations, two lines (CM-ANL-001 and CM-SHP-002),** as SA-13 placed the page. SA-22 and SA-32 placed CM-ANL-001 alone. No cell changes either way.
- **1, the influencer campaigns' archive, on CM-MKT-005 too.** campaign_browse and campaign_management gate it. I read an influencer campaign as a marketing campaign. The alternative is that they are the campaigns section's general permissions, in the address's line alone.
- **21, /payments/wallet.** The address is CM-PLN-006 (SA-21), and CM-PAY-005's cell holds the Wallet link as `shows`. I placed payments_operations_management on CM-PAY-020, its cell's capability. On the Wallet page it may gate the e-payments balance's operations (CM-PAY-005).
- **25, /payments/kyc:** its permissions payment and epayment are in no staff permission group (the repository's `held`). Whether a role can grant them isn't stated.
- **30 and 33, the 'Access restricted' lines:** whether they rest on the demo account's permissions or on the page's gate isn't stated (SA-29's same question). The account's permissions on the demo store would settle it.
- **71, the admin's Stores, two lines.** Its children are Development Stores, Stores Requests and Store management. Store management (CM-STF-005) isn't a kind of store, so it gives the group no line.
- **87, Custom Marketing on CM-PTN-005,** as SA-34 placed /admin/services/blocks, unsure. Its permission here is manage-notifications, a messaging permission. Where the content shows isn't stated.
- **38, Home (vip-dashboard), on VIP Partners:** the held partner's /me lacks vip-home, which agrees with a page for VIP partners only. That is the repository's observation, not a statement.

## Structures whose items and sources disagree

- **The table's rendered-menu column matches a title alone.** `gates.py` tests `title in rendered`, with the rendered titles from `partners-portal-navigation/partner@en`. So these admin items read 'in the rendered side menu' because the partner's own menu has an item with the same title: Themes (50), Services (54), Stores (71), Store management (74), Billings (76, 77), Operation records (78) and Partners Resources (89). The held partner's `is_admin` is false (SA-34). The other way round, the partner's own Marketing Tools (114), My Opportunities (108) and Active Merchants (110) read 'not in the rendered side menu' because the rendered titles carry the badge, 'Marketing Tools NEW'. Theme Subscriptions (119) and Demo stores (122) read the same because the rendered titles differ ('Theme Purchases', 'Demo Stores'). None of my lines rests on the column.
- **The held partner's /me holds several of the admin's permission values** (show-dashboard, manage-apps, manage-themes, manage-services and others), because the partner set and the admin set share values (SA-35's note on `o.Y` and `o.C`). The `held` column can't tell which set an item checks.

## What the sources state that no entry holds (for the second stage)

- **The admin's menu groups as a list of Salla's review work** (`portal-menu-definitions/layout-mf@prod/items.jsonl`, positions 3 to 55): verification, app, theme, bundle, service, portfolio, influencer profile, store and domain requests. These lead to the platform's review in CM-APP-002, CM-SFR-003, CM-PTN-002, CM-PTN-005 and CM-DVT-005, and the pages behind them aren't held (SA-34: partners-mf's chunks aren't held).
- **The admin's permissions manage-recommendations and manage-kits** (positions 46 and 47) gate Featured Apps and App Store Ads. They lead to whether the App Store sells ads or placements to partners (CM-APP-002, or CM-MKT-010's homonym). No held statement says who pays.

## Problems with this brief or the script

- None that blocked.
- The brief's known case on derived tables names the columns that quote the platform only for a dashboard row. On a portal row, `merchant_or_feature` holds the menu code's feature, which is the platform's, beside the repository's 'in/not in private-settings'. `demo_or_admin` holds the code's `admin: true`. `public_demo_or_shown` is wholly the repository's. I read them so (Q5, P7). The brief could say so for SA-31.
- The checker printed no container `NOTE` for this structure's route-None items. They are containers by their `children` in the menu code, and Q4 places them as such.

## The checker's lines, read again

- **`CHANGES`:** none. Every line falls on a cell that already holds its support.
- **`NOTE`:**
  - lines 81 and 82, core on a product named with the platform's brand: Salla Affiliate Products (66) is Salla's own packages that partners promote, CM-PTN-008's referral programme, as SA-36's check placed it. Core by what it shows.
  - lines 48 and 49, the first lead CM-B2B-002 (users): a partner's users, not business buyers, as SA-34 found. No line.
  - lines 17, 42, 47, 52 and 57, new things whose entries have leads: the earlier batches' new things, as above.
- **`NEW`:** Bullet Delivery, Product certificates, Transfer Requests, VIP Partners, all earlier batches'.

## The coordinator's check (31 October 2026, after the batch)

- **The portal rows' supports stand,** by the ruling after SA-30: a permission or feature of the partners' portal takes the support of the page it gates. So the partner's tools stay `extension-point`, and no line becomes `core` from the brief's rule for staff permissions.
- **`/more` on its group Customers stands,** by the ruling after SA-22's second clause: the row's permissions are the Customers group's, whose own address is the menu's. `/tools` is `out`: its only permission is empty.
- **The brief's known case now names the portal rows' columns:** `merchant_or_feature` and `demo_or_admin` are Salla's, and the rendered-menu column, matched by title only, is the repository's.
- **The other lines stand** by SA-29's rules and the portal's route lines. SA-31 keeps to the rules in the notes (P1 to P7, Q1 to Q7).
- **Cost:** 8.2 million tokens over 54 requests, about 63,000 an entry. No cell changes.

## The coordinator's correction after SA-42 (31 October 2026)

- **Three group lines that rested only on the group's permission are dropped:**
  - Stores, CM-DVT-005, `manage-development-stores`;
  - Themes, CM-SFR-005, `manage-bundles`;
  - Marketing Tools, CM-APP-003, `manage-coupons`.

  A permission is a gate on the portal's user, so it goes in `reading` (the brief's rule 5; SA-42's M3). Each group's remaining line now names its permission there. The children's own lines stand, so no cell changes.
