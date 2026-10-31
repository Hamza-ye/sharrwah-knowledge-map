# Notes: held pass, Salla, batch SA-31 (`permission-gates`, last part)

123 entries, effort high, evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-31`). Entry n is `derived/permission-gates.tsv` line n + 208.

**Placed:** 116 entries on capabilities, 3 `new` (earlier batches' new things), 4 `out`, in 145 lines. Supports over the lines: 94 `core`, 38 `extension-point`, 9 `shows`. No filler and no quality: no entry names a third party, a limit or a price. Scope only where the menu code gives the item a feature of its own (23 lines).

| Part | Entries | Table lines | Source items | Lines | Placement |
| --- | --- | --- | --- | --- | --- |
| layout-mf's last items (Payouts to Support) | 1 to 14 | 209 to 222 | `layout-mf@prod/items.jsonl`, positions 95 to 108 | 13 | 13 capability, 1 out (7, the header Others) |
| ui-partners-portal-layout, the admin's menu (array `Li`) | 15 to 68 | 223 to 276 | `ui-partners-portal-layout@prod/items.jsonl`, positions 0 to 53 | 63 | 50 capability, 2 new, 2 out (15 Dashboard, 18 Admins) |
| ui-partners-portal-layout, the partner's menu (function `Oe`) | 69 to 123 | 277 to 331 | positions 54 to 108 | 69 | 53 capability, 1 new, 1 out (116, the header navigation.others) |

## What I read

- The brief, `H-held.md`; the coordinator's rulings, `held/review-H-rulings.md`, to its last section (the ruling after SA-30); SA-29's and SA-30's notes and placements, with each one's coordinator's check.
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register's rows for `portal-menu-definitions` and `portal-private-settings`; `selection.tsv`'s row for `permission-gates` (`decides`, rule `rows:derived/permission-gates.tsv:.`). `show --meta` prints nothing for this structure.
- `derived/permission-gates.tsv`, lines 114 to 331 (SA-30's portal rows, for each twin, and mine); `capture/gates.py`, lines 25 to 27 and 194 to 226 (what a portal row holds, and how it is written).
- **The rows' sources:** `structures/salla/portal-menu-definitions/layout-mf@prod/items.jsonl`, positions 0 to 108, and `ui-partners-portal-layout@prod/items.jsonl`, all 109 items (title key, the bundle's own English and Arabic words, `to`, permissions, feature, `admin`, badge, header, items), with `ui-partners-portal-layout@prod/meta.json` and the declarations `h`, `v`, `N` and `Oe` in its `source.jsonl` (offsets 83086 to 96928).
- **For each item's line:** the placements of SA-28 and SA-29 for the rendered side menu, and of SA-34 to SA-39 for each route the items open, matched by route name (layout-mf) or path (ui-partners-portal-layout), and SA-30's line for each item's twin in layout-mf.
- The cells of the leads that weren't already the placed capability (`held_entries.py cells`): CM-OPS-005, CM-API-008, CM-PTN-001, CM-PTN-005, CM-SUP-005, CM-ACC-003.

## The structure's split

- **SA-29** holds table lines 2 to 78, **SA-30** lines 79 to 208. I hold lines 209 to 331, the rest: layout-mf's last 14 items (from Payouts) and all 109 items of ui-partners-portal-layout.
- Both bundles define the same menu in nearly the same order. ui-partners-portal-layout puts the admin's 54 items first (array `Li`), then the partner's 55 (function `Oe`). Each of my ui items has a twin in layout-mf, which SA-30 placed (entries 36 to 130) or which this batch places (entries 1 to 14). Each reading names its twin.

## Rules my lines follow

SA-29's P1 to P8 and SA-30's Q1 to Q7 hold, with the ruling after SA-30: a permission of the partners' portal takes the support of the page it gates. Where the second bundle's item differs from its twin, these apply:

- **R1. The ui item's address is its `to`.** The table writes 'route None' for all 109 ui items and 'not in the rendered side menu' for all of them. `capture/gates.py` (line 222) reads an item's `route` and `title`, while this bundle's items have their address in `to` (86 of them) and an i18n key for a title (`navigation.admin_users`). So the route column is empty and no title matches the rendered menu's words. Both are the repository's. I placed each item by its `to` and its bundle's own words (`words` in `items.jsonl`), and cite them in each reading.
- **R2. A container with no permission is still a container (M-13).** In this bundle a group (`items`) carries no permissions, and only the 19 top-level admin items carry `admin: true`. So 22 rows state no permission (their `held` is '-'). Each is placed as a container on the capability its title names, as its twin and the rendered group were. It isn't `out` like SA-30's `/tools`: that row's menu is `out` (the ruling after SA-22), and these groups each name a capability.
- **R3. A second line that rested on a container's permission isn't taken where the item carries none.** SA-30 gave three layout-mf containers a second line for a permission they carry:
  - Themes, CM-SFR-005 for manage-bundles;
  - Marketing Tools, CM-APP-003 for manage-coupons;
  - the admin's Stores, CM-DVT-005 for manage-development-stores.

  Their ui twins (72, 93, 48) carry no permission, so they take the title's capability alone, as SA-28 and SA-29 placed the rendered groups Themes and Marketing Tools. No cell changes either way.

  A second line that the title names stays: the admin's Influencers (36), the agency's Influencers (76), Influencer (90), My Subscriptions (96) and Payments (109).
- **R4. Scope is the item's own feature only.** In ui-partners-portal-layout, Domains' children (105 to 107) and My Services' children (81 to 83) carry no feature: their group does (domain-purchase, expert). The line takes no scope, and the reading names the group's feature. The support is the route's, as SA-30's Q1 has it, so Domains' children stay `shows` (SA-37).
- **R5. A menu permission goes on what it gates.** Both bundles gate Billings (2, 111) by manage-payouts, where its route asks manage-invoices (SA-35, SA-37). The permission gates the Billings item, so it is CM-PTN-004's (the ruling after ZD-7), with no line on payouts (CM-PTN-003).
- **R6. A path the code chooses by a feature goes in `reading` (SA-30's Q6).** The line takes the route the rendered menu opens:
  - Dashboard (69): /dashboards under temp-home-page;
  - Services (81) and the portfolio (83): temp-services-redesign;
  - the affiliate profile (85): temp-affiliates-profile;
  - Add Affiliate Product (95): temp-affiliates-products;
  - My Profile (91): temp-influencer-redesign;
  - Ready Stores (102): temp-ready-stores;
  - the payments' prefix /payments (110 to 112): temp-payments-billing. layout-mf chooses between route names by the same feature (1 to 3).
- **R7. The header Others is `out`** (7, 116), by the ruling after SA-28, as SA-29 placed the rendered روابط مساعدة.
- **R8. The admin's items** keep SA-30's Q3: `core` where they manage a partner or marketplace thing, and `out` for the admin's own Dashboard (15) and Admins (18).

## Each new thing

None of my own. Three entries take earlier batches' new things, under the same names:
- `new:VIP Partners`: 20 (the admin's VIP Partners, /admin/vip-partners) and 70 (Home, /home, vip-home), SA-34's;
- `new:Transfer Requests`: 25 (/admin/applications/transfer-requests), SA-34's.

The checker's notes on their leads come from CM-STF-002 by the field's name `permissions`, which is no lead.

## Entries I couldn't tell, and what would settle each

- **Support Tools (4, 113), a container whose title names no capability.** I placed it on CM-PTN-005 `shows`, the capability of its one page, Reviews & Ratings, by the ruling after SA-2, which gives a heading whose links are one capability's pages that capability's line. M-13's fallback for a container whose title names no capability is `new:Support Tools` with `core`, its child Reviews & Ratings (/reviews). The words are 'Support Tools' / 'الأدوات المساندة' (ui-partners-portal-layout). layout-mf's title is the locale key supportTools, whose locale chunk isn't held (the register's note). The page behind it isn't held either: the sweep's request ended at /not-authorized, since the partner lacks temp-unified-reviews-page (SA-37). That page would settle it.
- **Reviews & Ratings (5, 114) for influencers.** The menu opens it for manage-services or manage-influencers. I kept SA-37's one line on CM-PTN-005. A second `shows` line on CM-PTN-009 (influencers' reviews) is SA-37's alternative. The page would settle it.
- **The 22 containers with no permission (R2).** If the coordinator reads a permission row that states no permission as stating nothing, they become `out`, like `/tools`. No cell would change: each capability holds its twin's line.
- **Billings' manage-payouts (R5).** If a permission is placed by the thing its name names, as SA-29's P2 placed the dashboard's, Billings would take a CM-PTN-003 line too. That cell already holds `core`.
- **SA-30's open questions carry to the twins:** 64 (Custom Marketing on CM-PTN-005); 70 (Home on VIP Partners, since the held partner's /me lacks vip-home, which is the repository's observation); 48 (the admin's Stores).

## Structures whose items and sources disagree

- **The table's route and rendered-menu columns for ui-partners-portal-layout** (R1). Every one of the 109 rows reads 'route None' and 'not in the rendered side menu', though 86 items have an address (`to`) and many are shown in the partner's rendered menu under the same English words. The cause is `capture/gates.py`, line 222, which reads `route` and `title` only.
- **The rendered-menu column for layout-mf** still matches by title alone (SA-30's note). My rows Event Logs (8), Conversations (9) and settings (6) read 'not in the rendered side menu', since the rendered titles are 'Webhooks Log', 'Chats' and 'Settings'. Payouts, Billings, Operation records, Message Center, Help Center, Partners Resources, FAQ and Support read 'in'.
- **The `admin` column** is set only on the 19 top-level admin items in ui-partners-portal-layout. Their 35 children carry no `admin` but sit in the same array `Li`. layout-mf sets `admin: true` on every admin item. My readings name each child's admin group.
- **Billings' permission.** Both menus gate Billings by manage-payouts, while the route billing asks manage-invoices (SA-35's and SA-37's readings of the routes).
- **The admin's and the partner's permission sets share names.** The admin's Message Center is manage-notifications (`v.MANAGE_NOTIFICATIONS_CENTER`), the partner's manage-notifications-center (`h`). Both bundles title them Message Center, under the same key `navigation.message_center` (63, 119). The keys `navigation.admin_profile_requests` (40, 45) and `navigation.admin_categories` (62, 68) each stand for two items too. I placed each by its own address.

## What the sources state that no entry holds (for the second stage)

- **The settings item's alert** (`layout-mf@prod/items.jsonl`, line 101: `alert: t=>!t.verified`). The menu marks Settings while the partner account isn't verified. This is a lead for CM-PTN-002, on the partner's verification.
- **The menu's filter** `Pt(Oe(u),{features:u,permissions:d??[],isAdmin:g})` (`ui-partners-portal-layout@prod/meta.json`, `uses_of_binding`, offset 97430). The code that hides an item by feature, permission and admin flag isn't among the held declarations. It would say whether a group with no permission shows when any child is permitted (R2).
- **The feature constants** `N` (`source.jsonl`, offset 84807) name the portal's temporary redesigns: temp-home-page, temp-services-redesign, temp-influencer-redesign, temp-affiliates-profile, temp-affiliates-products, temp-ready-stores, temp-payments-billing and temp-unified-reviews-page. Each is a lead for which page a partner sees.

## Problems with this brief or the script

- None that blocked.
- The brief's known case on derived tables says which of a portal row's columns are Salla's. It doesn't say that, for ui-partners-portal-layout's rows, the route column is always None and the title is a locale key, so the item's `to` and `words` in `portal-menu-definitions` are where the address and the words are (R1).

## The checker's lines, read again

- **`CHANGES`:** none. Every line falls on a cell that already holds its support.
- **`NOTE`:**
  - line 9, entry 8 (Event Logs, /logs): the first lead CM-OPS-005 holds nothing. It is a store's logger, and its note names Webhooks Log as another log, so it isn't the entry's thing. The line is CM-API-008's, as the rendered link and the route were.
  - lines 21, 26 and 80: new things whose entries have leads. These are the earlier batches' new things, and the leads (CM-STF-002) come by the field's name.
- **`NEW`:** Transfer Requests and VIP Partners, both SA-34's.
- **The checker's final line:** '123 of 123 entries placed; 0 problems'.

## The coordinator's check (31 October 2026, after the batch)

- **The second bundle's rows are placed by their own `to` and words (R1),** as the brief's known case now says. The table's 'route None' comes from the extractor (`capture/gates.py`, line 222).
- **Rules R2 to R8 stand:**
  - groups that state no permission are containers;
  - a parent's feature goes in `reading`;
  - Billings carries `manage-payouts`.
- **Support Tools is CM-PTN-005 `shows`,** a heading over one capability's page, by the ruling after SA-2 and SA-5.
- **`permission-gates` is placed whole** (330 entries over SA-29 to SA-31).
- **Cost:** 8.8 million tokens over 53 requests, about 72,000 an entry. No cell changes.
