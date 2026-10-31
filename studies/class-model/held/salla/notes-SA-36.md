# Held pass, Salla, batch SA-36: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163: entries of `portal-app-routes` at items.jsonl lines 302 to 436, all of the app layout-mf v0.0.337 (`app.js`), in one bundle record, `raw/runs/20261008T134145Z-portal-bundles/fetch.warc.gz@1861581`:
- 1 to 84: the admin's routes (arrays `Ji`, `Xi`, `Qi`, `Zi`, `to`, `ro` and the admin's own list);
- 85 to 130: the account and sign-in routes (`bo`), the misc routes (`xo`) and the homes (`ko`).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-36`).

**Placed:** 120 entries on capabilities, 5 `new` (10, 11, 17, 18, 118), 5 `out` (49, 54 to 57), in 145 lines. 18 entries take two lines (15, 22, 33 to 39, 42 to 45, 47, 67, 103, 104, 108). Supports: 134 `core`, 2 `extension-point`, 2 `shows` on capabilities; 4 `core` and 1 `shows` on new lines. No `own-service` or `outside`, no filler, no quality.

**Sources read:** the brief and what it names; SA-34's and SA-35's placements and notes, with each coordinator's check; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `portal-app-routes`, `portal-menu-definitions` and `portal-private-settings`, `index/ledger/portal-app.tsv`; the selection row. Then, to clarify the routes only:
- **layout-mf's bundle** @1861581, once, for its router (`new Gi["default"]({mode:"history",…,routes:[{path:"/",redirect:…},{path:"/dashboard",redirect:…},...oo,...ko,...qo,...bo,...xo,…,{path:"*",redirect:{name:"error-404"}}]})`), the permission sets `Wi` (the partner's) and `Ki` (the admin's), the features `io`, the function `wo` and its own menu (`navMenuItems:Pa`, structure `portal-menu-definitions/layout-mf@prod`). layout-mf's locale chunks aren't held (the register says so), so titles are read from the routes' `title` and `breadcrumb`, and the Arabic from the React menu;
- **the registry**, `structures/salla/portal-apps/prod/items.jsonl`, for which app serves each path (tested with each pattern, a parameter replaced by a number);
- **the React menu**, `structures/salla/portal-menu-definitions/ui-partners-portal-layout@prod/items.jsonl`, for the admin's Affiliater group and the partner's Chats, in English and Arabic;
- **the partner account:** `portal-me/partner@en/source.json` (`is_admin` false, its permissions) and `portal-private-settings/partner@en/items.jsonl` (its features: `new-login`, `salla-chat`, `partner-onboarding`, `partner_resource`, `app-store-ads` held; `temp-home-page` not);
- **for the paths no batch had placed:** affiliates-mf's bundle @2098236 (the app the registry serves `/admin/affiliates*` by: its routes and its locale on Salla's packages), and ui-partners-portal-login's bundle `raw/runs/20261008T134248Z-portal-bundles-chunks1/fetch.warc.gz@458454` (its routes `/onboarding` and `/merchant/callback`); partners-mf's bundle @1510962 for its featured-apps and billings routes, to compare.

## What layout-mf's routes are

layout-mf is the portal's Vue layout. Its router holds a route for nearly every page of the portal, but the registry serves layout-mf only at `/` and `/conversations.*`. Each entry stands for one route object of that router (`show --code 300`); none is a non-route object, so none is `out` for that reason (SA-9's check).
- **Admin and account routes with `name` and `meta` only** (1 to 84, 94 to 106, 109, 113, 120, 124 to 127, 129, 130): layout-mf names them so its menu (which links by route name) and its guard (`beforeEach`, reading `meta`) work. I placed them by SA-35's rule 9: on the thing of the page the registry serves at the path, citing that app.
- **Routes with an element** (85 to 93, 107, 110 to 112, 114 to 119, 121 to 123, 128): layout-mf carries its own page, but for all but `/conversations` the registry serves the path by another app (mostly ui-partners-portal-login). Placed the same way.
- **`/conversations` (128)** is layout-mf's own page: the registry serves it by layout-mf.

So almost every entry is the same route as one SA-34 or SA-35 placed in partners-mf or services-mf, and I kept their lines: rule 5 for the admin (`core` on the thing managed; the admin team's own pages `out`), rule 9 for name-only routes, rule 10 for a guard that picks a component, rule 3 for a feature gate. Each reading names the earlier batch.

## Rules my lines follow, beyond SA-34's and SA-35's

1. **The new-login wrapper (85 to 93, 112).** layout-mf wraps the auth pages' elements in `wo`: where the features from `api/private-settings` hold `new-login`, it loads another chunk (865). The held partner holds `new-login`. By SA-35's rule 10 this chooses the page, not whether it opens, so it goes in `reading`, not `scope`.
2. **A feature gate that only layout-mf states** is still the route's scope (rule 3): `app-store-ads` on the featured apps (61 to 63; partners-mf's same routes carry no feature, so SA-34's lines have no scope), `partner-onboarding` (113), `partner_resource` (124), `salla-chat` (128), `temp-home-page` (130).
3. **A redirect-only route** (94 `/account-settings`, 99 `/settings/id-verification`, 106 `/account-setting`, 127 `/support`) is placed on the thing of the place it sends to, since its own path names an old address of that thing. The brief: a redirect names another place, not its own thing; the route still has its place, the old address.

## New things

No new thing of this batch's own. The new lines are earlier batches' things, by the same names:
1. **VIP Partners**, entries 10 and 11 (`/admin/vip-partners`, `/create`): SA-34's, permission manage-vip.
2. **Transfer Requests**, entries 17 and 18 (`/admin/applications/transfer-requests/` and its details): SA-34's. The checker's leads CM-APP-001 and CM-INV-006 aren't the thing, as SA-34 found.
3. **Ideas**, entry 118 (`/ideas-auth`): SA-35's, `shows`, with no place of its own held. Here the route has an element (chunk 539); the registry serves it by ui-partners-portal-login, whose route renders a provider sign-in with provider 'ideas' (bundle @458454).

## Entries I couldn't tell, and what would settle each

- **42 to 45, Salla Affiliate Products (منتجات سلة), on CM-PTN-008 and CM-PTN-009.** The admin manages Salla's own affiliate products. affiliates-mf, which serves these paths, says 'Promote Salla packages to new and existing merchants and earn sustainable commissions based on their sales performance.' and 'Use this link to promote Salla packages in general.' (@2098236). I read the products as Salla's packages promoted for a commission, so CM-PTN-008 (the referral programme for the platform's plans), beside CM-PTN-009 (partner affiliates) for the affiliate products. That the admin's "Salla products" are the packages is a reading. The page's chunk (`r.e(138)`) would settle it. I didn't look for it in the chunk waves (the brief says not to trace further).
- **47, Merchants Live Products (منتجات التجار):** CM-PTN-009 and CM-MKT-014, both `core`. These are the merchants' products offered to affiliate marketers. Salla oversees them for its affiliate marketplace, and CM-MKT-014's cell holds that marketplace (as `extension-point`, for the partners' side) and the store's own affiliate marketing (`core`). CM-PTN-009 alone is the alternative.
- **40, 41, 46, 48, the admin's affiliates:** CM-PTN-009 `core`, by rule 5, as SA-34 placed the admin's influencers. Unlike the influencer routes, these take no CM-MKT-014 line: SA-35 kept the affiliate profile on CM-PTN-009 alone, since CM-MKT-014 cites only Affiliate Marketplace.
- **112, `/merchant/callback`:** CM-PTN-002 `core`. ui-partners-portal-login's login page has an option, whose key is named `sign_in_as_merchant`, that sends the user to a merchant address and back here with a code and state (@458454). A key's name isn't the platform's words, and the page's words aren't in that bundle. CM-TRU-001 (the sign-in methods of the platform's accounts) is the alternative. The login app's locale would settle it.
- **113, `/onboarding`:** CM-PTN-002 `core`, scope `partner-onboarding`, read as the partner account's onboarding after registration. The page's words aren't held. CM-ONB-004 (the first lead) is the store's setup, a homonym.
- **122, `/pages/miscellaneous/under-maintenance`, and 123, `/pages/miscellaneous/error`:** CM-PTN-001 `core`, as SA-35 placed error pages. They are the portal's own pages; `out` is the alternative. 122 isn't a store's maintenance mode (CM-ACC-007). partners-mf, which the registry serves `/pages` by, doesn't declare these paths.
- **130, `/dashboards`:** CM-PTN-001 `shows`. The route is gated by `temp-home-page` (a temporary redesign the held partner lacks) or by a native app (`featureOverride: No`, with `temp-home-page-native-off`, also not held). Both partners-mf's pattern (a prefix `\/dashboard`, no end anchor) and ui-partners-portal-widgets' (`/dashboards`) match the path. I named widgets, whose own pattern names it.
- **The rest** carry the doubts SA-34 and SA-35 listed for the same routes: 19 (App Actions), 67 (Categories), 72 to 74 (coupons), 77 to 79 (Ready Stores), 80 and 81, 82 to 84 (Custom Marketing), 107, 109, 111, 114, 116, 117, 119, 121.

## Items against sources

The values agree: each entry stands for one route object of layout-mf's router at the line its locator gives. Some items list further objects, and the entry is placed for its route:
- 105's second object (line 408) is the redirect target `{path:"/settings/connections",hash:""}` inside 106's route;
- 107's first object (line 409) is the same kind of target (`/error-404`);
- 124's extra objects (lines 428 to 432) are breadcrumb items `{text, path}`;
- 129's extra objects are the router's own `{path:"/dashboard",redirect:…}` (line 604) and a menu-like `{label, icon}` (line 606).

Where layout-mf and the other apps differ:
- **Two apps hold the same paths.** layout-mf declares pages for `/login`, `/register` and the other auth routes, for `/auth/cli`, `/ideas-auth` and others. The registry serves them by ui-partners-portal-login, and serves layout-mf only at `/` and `/conversations.*`.
- **Permissions differ from partners-mf's for the same route:**
  - the admin's billings carry `manage-invoices` here and `manage-users` in partners-mf (SA-35's notes);
  - `/authorize/github` carries `manage-themes` here.
- **Paths served by no app:** six paths match no pattern of the registry. They are `/admin/influencers/packages/:id` (services-mf's pattern has the list but not the detail), `/error-404`, `/error-500`, `/github/callback`, `/document-signed` and `/document-declined`. SA-35 placed the last five by their names; I placed all six by the earlier batches' lines.
- **`/settings/id-verification` (99)** redirects to `/account`; no other app declares it.

## For the second stage: what the sources state that no entry holds

- **CM-PTN-008:** affiliates-mf's locale on Salla's packages (@2098236):
  - 'Market and earn 10% profit for each subscription' (`affiliatePackagesBannerDesc`), a quality, 10% a subscription;
  - 'The new unified commission system for Salla packages is now available.';
  - the per-package commission for monthly and yearly subscriptions (`commissionByPackageDescription`);
  - the terms of marketing Salla's packages (`acceptConditionsSallaPackages`, 'الشروط والأحكام الخاصة … بتسويق باقات سلة').

  A lead for the cell, which holds no rate.
- **CM-PTN-009, CM-MKT-014:** affiliates-mf's 'Your Affiliate Product is Now Live in the Marketplace!' and 'By confirming, you commit to paying marketers their sales commission.'. The product's program types are 'Subscription' and 'GMV' (`programType`).
- **layout-mf's menu** (`portal-menu-definitions/layout-mf@prod`) holds the partner's Affiliates items gated by `advanced-affiliate-marketplace`, `affiliate-orders` and `affiliate-active-merchants`, two of them tagged 'new'. They are later batches' routes (ui-partners-portal-affiliate, affiliates-mf).
- **The root redirect** (line 604 area) sends an admin to `dashboard-analytics`, a `vip` account to `vip-dashboard` and an `agency` account to `agency-list`. The account types `vip` and `agency` are a lead for VIP Partners and for the agency pages (CM-MKT-015, CM-PTN-009).

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that already holds its support, or on a new thing.
- **`NOTE` first lead holds nothing:**
  - CM-B2B-002 on the admin's companies and users (1 to 4, 8, 9, 75, 76) comes by the words "companies" and "users". These are partners' accounts, not buyer businesses, as SA-34 found: no lead.
  - CM-ONB-004 on `/onboarding` (113): the store's setup, a homonym (above).
  - CM-OPS-005 on `/logs` (120): the webhooks log of the partner's apps, not a store's logger, as SA-35 found.
- **`NOTE` new thing with leads** (17, 18): CM-APP-001 and CM-INV-006 aren't the thing (SA-34).
- **`NOTE` containers** (15):
  - the admin's `admin/companies`, `admin/users`, `admin/verification-requests`, `admin/applications`, `admin/themes`, `admin/services`, `admin/influencers`, `admin/affiliates`, `admin/affiliates/salla-products`, `admin/billings`, `admin/featured-apps`, `admin/app-store-ads`, `admin/coupons`, `admin/stores` and `admin/services/blocks`;
  - the partner's `account` and `settings`.

  Each is a page of its own (a list), placed on its thing's capability as SA-34 and SA-35 placed the same paths. Their children are the same capability's, except where a second thing gives them another line: 15 (shipping settings), 22 (bundles), 42 to 45 (CM-PTN-008), 47 (CM-MKT-014), 103 and 104 (payouts), 108 (security). None is `out`.
- **`NEW`:** Ideas, 1 line; Transfer Requests, 2 lines; VIP Partners, 2 lines.
- No quote printed 'found nowhere held'.

## Problems with the brief or the script

- **`show --code 300` cuts a route at 300 characters,** before the `feature` key where the breadcrumb is long. Reading the router's arrays once from the bundle was enough.
- **A route object's nested objects become items of their own.** A redirect's target `{path, hash}` and breadcrumb items `{text, path}` carry a path, so they are items, and `show` lists them under the route of the same path. The rule "place the entry for each item that is a route" handles it, but the coordinator may want the extractor to mark them.

The checker's last line, for SA-36: `130 of 130 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **layout-mf's routes go on the page the registry serves at each path** (SA-35's rule 9). Almost all keep SA-34's and SA-35's lines, so no cell changes.
- **The admin's affiliate routes (40 to 48) stand** on CM-PTN-009 by rule 5. 'Salla Affiliate Products' (42 to 45) also takes CM-PTN-008, since affiliates-mf's locale has partners 'Promote Salla packages to new and existing merchants…': the referral programme for Salla's plans.
- **A feature gate that only layout-mf states is the route's scope** (`app-store-ads`, `partner-onboarding`, `partner_resource`, `salla-chat`). `temp-home-page`, which the held partner lacks, makes its line `shows`. The `new-login` wrapper, which only chooses a page, stays in `reading`.
- **`show --code 300` can stop before a long route's `feature` key.** SA-37 to SA-39 print with `--code 600`.
- **Cost:** 9.3 million tokens over 58 requests, about 72,000 an entry. No cell changes, and the new things are SA-34's and SA-35's.
