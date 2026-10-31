# Held pass, Salla, batch SA-43: notes

100 entries (effort high), evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-43`).
- **All 100 are `portal-menu-definitions`, `ui-partners-portal-layout@prod`:** `items.jsonl` lines 10 to 109, the rest of the other bundle's menu. Entry n is line n + 9 (position n + 8). The same item's permission row is SA-31's entry n + 23 (`derived/permission-gates.tsv`, line n + 231).
  - 1 to 45: the admin's menu (array `Li`), positions 9 to 53, from Apps Requests to the admin's Help Center and its Categories;
  - 46 to 100: the partner's menu (function `Oe`), positions 54 to 108, from Dashboard to Support.
- **Each item's twin in layout-mf** is SA-42's (its entries 28 to 72 for the admin's items, and 18, 19 and 73 to 121 for the partner's), but for the partner's Domains and its three items (90 to 93 here, layout-mf's lines 90 to 93), which have no entries in layout-mf, since the concern map cites them (SA-S-5116, SA-S-5117, SA-S-5153, SA-S-5154).

**`portal-menu-definitions` is now placed whole** (SA-42, SA-43).

**Placed:** 97 entries on capabilities, 2 on earlier batches' new things (2, 47), 1 `out` (93, the header Others), in 123 lines. 23 entries take two lines. No line groups entries.
- **Supports over the 122 lines that aren't `out`:** 77 `core` (2 of them the new lines), 38 `extension-point`, 7 `shows`. No `own-service`, no `outside`.
  - the admin's menu: 55 lines, all `core` but Bundles Requests' second line (7, CM-SFR-005 `extension-point`);
  - the partner's menu: 68 lines, 22 `core` on capabilities and 1 new, 37 `extension-point`, 7 `shows` (Store management, Domains and its three items, Support Tools, Reviews & Ratings), and the 1 `out`.
- **No filler and no quality:** no entry names a third party doing the thing, a limit or a price.
- **Scope** on 18 lines, each the item's own `feature`:
  - `app-store-ads` (36);
  - `influencer_packages` (55, two lines);
  - `expert` (57);
  - `advanced-affiliate-marketplace` (63, two lines);
  - `affiliate-active-merchants` (64, 66);
  - `affiliate-orders` (65);
  - `development_store` (79, two lines);
  - `store-management` (80);
  - `domain-purchase` (81);
  - `invoices` (88, 89);
  - `temp-unified-reviews-page` (90, 91);
  - `partner_resource` (98).

## Sources read

- **The brief and what it names:**
  - `H-held.md`;
  - the evidence map;
  - B-extent's "Cells and evidence" and "Conventions from the dry run";
  - the coordinator's rulings, `held/review-H-rulings.md`, to its last section (the ruling after SA-19).
- **observed-sa's guides:** `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`; the register's rows for `portal-menu-definitions` and `portal-private-settings`; `index/ledger-summary.tsv` and `index/ledger/portal-app.tsv`.
- **The structure:** `show --meta` (it prints layout-mf's descriptive keys), so also `ui-partners-portal-layout@prod/meta.json`; the selection row (`where`, the note "the items not cited").
- **The batches before mine:**
  - SA-42's notes (M1 to M13 and the coordinator's check) and its placements: the twins' lines, and its lines 151 to 159 for this bundle's first nine items;
  - SA-31's notes (R1 to R8 and its check) and its lines for the same 100 items;
  - SA-34's notes on its two new things;
  - the lines of SA-28, SA-29, SA-30 and SA-34 to SA-39 that cite each item's address or key, found as below, read where SA-42's twin line cites them (SA-29's lines 8, 15, 16 and 21 read whole).
- **The items and their source:**
  - `ui-partners-portal-layout@prod/items.jsonl`, lines 1 to 109, raw;
  - its `source.jsonl` declarations `Ii` and `Oi` (the words, offsets 77938 and 71346), `h` (83086), `N` (84807) and `Oe` (91235);
  - a check that every item's words are the `Ii`/`Oi` strings for its key (all 100 agree) and that every word key, permission constant and feature constant is used by an item (all are);
  - `layout-mf@prod/items.jsonl` for each twin's title and route.
- **The partner's features**, for the addresses the code chooses (M7):
  - 8 October: `structures/salla/portal-private-settings/partner@en/source.json`, 68 features;
  - 28 October: `raw/runs/20261028T160451Z-journey-portal-demo-store-new-en/responses/0006.json`, 74 features (the evidence map; the ruling after SA-44).

  Both hold `temp-affiliates-profile` and `temp-affiliates-products`. Only the later holds `temp-services-redesign` and `temp-influencer-redesign`. Neither holds `temp-home-page`, `temp-ready-stores`, `temp-payments-billing`, `temp-unified-reviews-page` or `domain-purchase`.
- **The model:**
  - the cells of every capability I placed on: CM-APP-002, -003; CM-SFR-003, -005, -008; CM-PTN-001 to -005, -008, -009; CM-MKT-014, -015; CM-DVT-003 to -005; CM-STF-005; CM-API-008;
  - the cells of the leads I set aside: CM-SFR-009 (DNS records, which SA-37 gave one of the domains' pages), CM-OPS-004, CM-CAT-012, CM-ACC-003, CM-SEL-006, CM-MKT-005, CM-MKT-010, CM-MKT-020, CM-API-009, CM-NTF-001, CM-SUP-001, CM-SUP-004, CM-SUP-005, CM-TRU-003, CM-APP-001, CM-INV-006, CM-ORD-002, CM-SHP-021;
  - the leads' names for the rest;
  - `caps --terms` for the entries no lead named: contract, recommended app, featured app, packages list, influencer package, opportunit, active merchant, app action, administrative action, العقود, التطبيقات الموصى, قائمة الباقات, فرصي, المتاجر النشطة, عمليات;
  - `caps --terms` for narrower things the entries name: app review, service review, partner review, chat, conversation, محادث, domain transfer, domain assignment, التنازل, theme trial, trial, تجريبي, custom marketing, app store ad, marketing block.

  No search found a capability the earlier lines hadn't. CM-SUP-004 (Salla Chat) is a homonym for Chats (95).
- The concern map's citations of `portal-menu-definitions` (`studies/concern-map/platforms/salla/citations.tsv`, lines 2945, 2946, 2982 and 2983), to confirm the four statements on layout-mf's Domains.

I read no run step. The one answer I read is the partner's features of 28 October, above.

**Finding the earlier lines.** `held_entries.py earlier` printed "(no earlier line cites a key of it)" for all 100 entries (see the problems below). So I searched the platform's other placements with a script of my own, `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/SA-43/bin/lookup.py`. It looks in their readings and terms for:
- each item's `to`;
- both addresses of a `to` the code chooses;
- the Payments items' template paths;
- the title key.

It also prints SA-31's row for the same item. `bin/twins.py` beside it prints SA-42's lines for the layout-mf twin.

## Rules my lines follow

SA-42's M1 to M13, as the coordinator kept them, and SA-31's R1 to R8 where M3 to M10 leave them standing. In particular:
- **Same item, same thing (M1).** Each line takes the capability and support its address's earlier lines give it. Its reading cites:
  - the route (SA-34 to SA-39);
  - the rendered link or group (SA-28, SA-29), where the held partner's menu shows the item;
  - SA-42's line for the layout-mf twin;
  - SA-31's permission row.

  The item's address is its `to` and its words are its `words` (SA-31's R1).
- **The admin's menu (M2)** keeps SA-34's rule 5: `core` where it manages a partner or marketplace thing.
  - This bundle's admin items here are all such. The admin's own Dashboard and Admins are SA-42's (122, 125).
  - The array `Li` sets `admin: true` only on its top-level items. Each child's reading names its admin group.
- **A permission is a gate on the portal's user (M3).** Each reading names it, and no line, term or scope rests on one. This bundle's groups carry no permission (SA-31's R2), so no second line could rest on one anyway (SA-31's R3).
- **A second line where the page or title is itself two things (M4).** These are the only second lines:
  - Bundles Requests (7, CM-SFR-005);
  - the admin's Influencers and its four items (13 to 17, CM-PTN-009);
  - Salla Affiliate Products (20, CM-PTN-008);
  - Merchants Live Products (24, CM-MKT-014);
  - the admin's Categories (39, CM-SFR-003);
  - every agency item (52 to 56), and the Influencer group and its items (67 to 69): CM-MKT-015 and CM-PTN-009;
  - the Affiliate Marketplace (63, CM-MKT-014);
  - My Subscriptions (73, CM-APP-003 and CM-SFR-003);
  - Payments (86, CM-PTN-003 and CM-PTN-004).
- **A child that is a kind of its group's thing takes the group's line (M5):**
  - the admin's Ready Stores (26), which SA-31's row lacks;
  - the partner's Demo Stores (78);
  - the partner's Ready Stores (79).

  Requests (27) and store management (28, 80) aren't kinds of store. Bundles (51) aren't a kind of theme, and coupons (71) aren't the Marketing Tools group's thing.
- **Scope is the item's own `feature` (M6).** A group's feature goes in its children's readings: My Services' `expert` (58 to 60), and Domains' `domain-purchase` (82 to 84, M13).
- **An address the code chooses goes in `reading` (M7):**
  - Dashboard by `temp-home-page` (46);
  - Services and the portfolio by `temp-services-redesign` (58, 60);
  - the affiliate profile by `temp-affiliates-profile` (62);
  - My Profile by `temp-influencer-redesign` (68);
  - Add Affiliate Product by `temp-affiliates-products` (72);
  - Ready Stores by `temp-ready-stores` (79);
  - the Payments items' prefix `/payments` by `temp-payments-billing` (87 to 89).

  Each line takes the page the rendered menu opens, with its support. Where the feature's page is another route, both routes are the same capability's in the earlier lines (the feature's own page is `shows` where the held partner lacks the feature, as /dashboards and /payments/* are in SA-36 and SA-37), so no line rests on the choice.
- **Terms (M8)** are the item's key and its English and Arabic words. A permission is never a term (SA-31's lines had them; mine don't).
- **A badge is a release badge (M10):** `navigation.new`, 'NEW' / 'جديد', on 64, 66, 70 and 81. It goes in `reading`, and the item keeps its support.
- **The header Others is `out` (M11):** 93.
- **Containers (M12):** the 20 groups with `items` here are placed as containers, on their title's capability with the support their children's routes took. None carries a permission. The bundle's other two, Users and Apps, are SA-42's (123, 129).
  - the admin's: 4, 8, 13, 19, 25, 30, 33, 42;
  - the partner's: 49, 53, 57, 61, 67, 70, 73, 77, 81, 86, 90, 97.
- **Store management, Domains and Support Tools (M13):**
  - the partner's Store management stays `shows` (80);
  - Domains (81 to 84) stay `shows`, behind `domain-purchase`, which the held partner lacks on both dates. The group takes the scope, its items none;
  - Support Tools and Reviews & Ratings stay `shows` behind `temp-unified-reviews-page` (90, 91), which it also lacks.
- **A key that titles two items:** `navigation.admin_profile_requests` (17, 22), `navigation.admin_categories` (39, 45) and `navigation.message_center` (40, 96), and the admin's and the partner's `navigation.help_center` (42, 97) and `navigation.help_resources` (43, 98). Each item is placed by its own address, as SA-31's notes say.

## Each new thing

None of my own. Two entries take SA-34's new things, under the same names:
- **`new:VIP Partners`** (`core`): 47, Home, 'Home' / 'الرئيسية', at `/home` (permission `vip-home`). It is the home page of VIP partners, as SA-35 and SA-37 placed the route vip-dashboard at `/home`.
  - Earlier lines of the same new thing: SA-42's 19, 24 and 127, SA-31's 20 and 70, and SA-34's 86 and 87.
  - Its place of its own: the admin menu's VIP Partners (`/admin/vip-partners`) and its routes.
  - Proposed, as SA-34: domain F, area PTN, parent CM-PTN-001. SA-34 names CM-PTN-010 (Commerce-as-a-Service) as the nearest capability.
  - Names: VIP Partners / الشركاء الـVIP (the other bundle's line 6).
- **`new:Transfer Requests`** (`core`): 2, the admin's Transfer Requests, 'Transfer Requests' / 'طلبات نقل', at `/admin/applications/transfer-requests`. These are requests to transfer an app between partner accounts.
  - Earlier lines of the same new thing: SA-42's 29, SA-31's 25, and SA-34's 93 and 94.
  - Its place of its own: the admin menu's Apps > Transfer Requests and its routes (SA-34, SA-36).
  - Proposed, as SA-34: domain F, area APP or PTN, parent CM-PTN-002 or CM-APP-001.
  - Names: Transfer Requests / طلبات نقل. This entry is the Arabic name SA-42's notes point to.

Searched again: VIP; الشركاء الـVIP; app transfer; ownership transfer; طلبات نقل; نقل ملكية; transfer request. No capability matched. The checker's leads for 2 (CM-INV-006, CM-ORD-002, CM-SHP-021) are inventory transfers, order editing and packaging: I read their cells.

## Entries I couldn't tell, and what would settle each

- **26, the admin's Ready Stores on CM-DVT-003 too (M5).** SA-31's row for the same item has CM-DVT-005 alone, as SA-30's has for layout-mf's twin. SA-42's notes leave the alignment to the coordinator, and its check keeps M5. No cell changes either way.
- **90, Support Tools: CM-PTN-005 `shows`,** a heading over one capability's page (the ruling after SA-2, which SA-31's check kept). M-13's `new:Support Tools` with `core` is the alternative. The page behind it isn't held: the partner lacks `temp-unified-reviews-page`.
- **91, Reviews & Ratings:** opened for `manage-services` or `manage-influencers`. A second `shows` line on CM-PTN-009 (influencers' reviews) is SA-37's alternative. The page would settle it.
- **41, Custom Marketing on CM-PTN-005:**
  - its address is under `/admin/services`, and SA-34 placed the route unsure;
  - its permission `manage-notifications` is the admin's messaging permission, the same as the admin's Message Center (40);
  - where its content shows isn't stated.
- **37, App Store Ads on CM-APP-002:** who buys these ads isn't stated (SA-30's notes). CM-MKT-010, a store's advertising, is a homonym.
- **47, Home on VIP Partners:** the held partner's `/me` lacks `vip-home`, the repository's observation (SA-30's and SA-31's notes). The page isn't held.

## Structures whose items and sources disagree

- **The entries' text leaves out the address of the three Payments items (87 to 89).** Their `to` is a template literal: `` `${t}/payouts` ``, `` `${t}/billing` `` and `` `${t}/billing/operations` ``, with `t=e(N.PAYMENTS_BILLING)?"/payments":""`. The items hold this (`items.jsonl`, lines 96 to 98) and so does `Oe` in `source.jsonl` (offset 91235).
  - The source governs: each reading names both addresses.
  - The rendering also leaves out every item's `icon` (41 items), which names nothing.
- **SA-42's line 78 cites this bundle's 'Recommended Apps' at `items.jsonl` line 46.** The item is at line 45 (position 44); line 46 is App Store Ads. This is a slip in that reading: my entry 36 is line 45.
- **One Arabic title stands for several English ones.** 'طلبات النشر' titles Apps Requests (1), Themes Requests (6) and both Profile Requests (17, 22). Each is placed by its address.
- **Salla's spelling is kept as written:**
  - Demo Stores' Arabic, 'المتاجر التجريبة' (78), without the ي of التجريبية;
  - the admin's 'Affiliater' / 'المسوقين بالعموله' (19, 21), with ه for ة.
- **The two bundles title some items differently.** The rendered menu follows this bundle (SA-42's notes). Each reading names layout-mf's title where it differs:
  - Applications Requests / Apps Requests;
  - Services Requests / Services Publication Requests;
  - Development Stores / Ready Stores, for the admin's and the partner's;
  - Coupons Admin / Coupons;
  - Featured Apps / Recommended Apps;
  - Messages Center / Message Center;
  - My Applications / My Apps;
  - My Themes Bundles / Bundles;
  - Theme Subscriptions / Theme Purchases;
  - Event Logs / Webhooks Log;
  - Conversations / Chats.

  layout-mf's locale-key titles (help.helpCenter, agency.*, influencer.*, supportTools, settings) are named as keys.
- **This bundle's Settings (92) holds no `alert` and no `target`,** unlike layout-mf's (SA-42's 113). The partner's unverified-account alert is layout-mf's alone.

## What the sources state that no entry holds (for the second stage)

- **Two uses of the menu's function** (`ui-partners-portal-layout@prod/meta.json`, `uses_of_binding`):
  - `return[...Oe([]),...Oe(Object.values(N))]` (offsets 96952 and 96962) composes the menu with no features and with every feature;
  - `Pt(Oe(u),{features:u,permissions:d??[],isAdmin:g})` (offset 97430) filters it, as SA-31 noted.

  The code around them isn't among the held declarations. It would say whether a group with no permission shows when any child is permitted (SA-31's R2), and how the admin's array `Li` is shown.
- **Two redesign features of 28 October that no structure holds:** `temp-influencer-campaign-redesign` and `temp-service-orders-redesign` are in the partner's later answer (`raw/runs/20261028T160451Z-journey-portal-demo-store-new-en/responses/0006.json`), not in the 8 October structure, and no item of this bundle (0.134.0) names them.
  - They are leads for which campaign-orders and service-orders pages a later portal shows. The other redesign features no item names (`temp-affiliate-marketplace`, `temp-affiliates-store-details`, `temp-affiliates-opportunity-creation`, `temp-account-settings-redesign`) are in the 8 October structure, which SA-44 placed.
  - The register says the 9 October bundles, layout-mf v0.0.344 and ui-partners-portal-layout 0.137.0, aren't held.

## Problems with this brief or the script

- None that blocked.
- **`held_entries.py earlier` finds nothing for this bundle's entries.** It printed "(no earlier line cites a key of it)" for all 100, and does the same for SA-42's entries 122 to 130. Earlier lines do cite them:
  - SA-31's and SA-42's readings cite their `to`, title keys and quoted words;
  - SA-34 to SA-38's terms hold the same paths without the leading slash (`admin/applications/requests`).

  The command doesn't read an item's `to`, its `navigation.*` title key or its `words`. I searched with my own script instead (see "Sources read").
- **`show` drops a `to` that is a template literal** (87 to 89), so the entry's text names no address for them.
- **The checker prints no container `NOTE`** for an item with `items`, as SA-42 found for `children`. M12 places all 20 here as containers.
- **The `NOTE` on line 114** (Support Tools, first lead CM-OPS-004) stays though the line's reading names the lead as a homonym. The checker seems to look for a line on the lead, not a reading that names it.

## The checker's lines, read again

- **`CHANGES`:** none. Every line falls on a cell that already holds its support.
- **`NOTE` core on a product named with the platform's brand,** lines 27 and 28 (20, 'Salla Affiliate Products' / 'منتجات سلة'). Both are core by what the entry shows:
  - Salla's own admin page of the products affiliates promote, on CM-PTN-009;
  - its second thing, Salla's packages affiliates promote, its referral programme for its plans, on CM-PTN-008 (SA-36's check, SA-38, SA-42's M4).

  The brand names no maker, and no line rests on one.
- **`NOTE` a new thing whose entry has leads,** line 3 (2, Transfer Requests). I read the three leads' cells:
  - CM-INV-006 is inventory transfers, by transfer;
  - CM-ORD-002 is order editing, by request;
  - CM-SHP-021 is packaging, by request.

  None is an app's transfer between partner accounts.
- **`NOTE` a first lead that holds nothing,** line 114 (90, Support Tools). CM-OPS-004 is a store's system status report and tools (WooCommerce's Status: System status, Tools), a lead by the word "tools". The entry's tools are the partner's, over the reviews of its services. A homonym, so no line.
- **`NEW`:** Transfer Requests, 1 line; VIP Partners, 1 line. Both are SA-34's.
- No quote prints 'found nowhere held'.

The checker's last line, for SA-43: `100 of 100 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes.** With SA-42, `portal-menu-definitions` is now placed whole. Each item keeps its address's earlier lines (M1).
- **The open points stand as placed:**
  - **26:** the admin's Ready Stores takes CM-DVT-003 by M5, and SA-31's permission row is left as it is. A permission row places what the permission gates, not the menu's groups, as SA-30's row for Development Stores is left after SA-42.
  - **90:** Support Tools stays on CM-PTN-005 `shows`. Its page isn't held, so a new thing would rest on nothing but its title.
  - **91, 41 and 37** stay as placed. Who buys App Store Ads (37) is a lead for the second stage.
- **SA-42's line 78 is corrected.** 'Recommended Apps' is at line 45 of the other bundle's `items.jsonl`, not 46.
- **`held_entries.py earlier` now reads this bundle's keys:** `to:` addresses, key-like titles (`navigation.*`), and the `en` and `ar` words. Run on this batch it finds earlier lines for all 100 entries, where it found none for the agent.
- **Cost:** 22.7 million tokens over 94 requests, about 227,000 an entry. Most of it went on looking up earlier lines, which the agent did with its own script because `earlier` missed this format.
