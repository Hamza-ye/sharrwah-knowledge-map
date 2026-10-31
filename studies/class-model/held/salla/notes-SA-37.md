# Held pass, Salla, batch SA-37: notes

130 entries (effort high), evidence at observed-sa@b0bd0b16: entries of `portal-app-routes` at items.jsonl lines 437 to 566, all of the app layout-mf v0.0.337 (`app.js`), in one bundle record, `raw/runs/20261008T134145Z-portal-bundles/fetch.warc.gz@1861581`. They are the partner's routes of layout-mf's router, the arrays after the homes (`ko`): apps (`Oo`), domains (`Io`), themes (`_o`), subscriptions (`To`), stores (`Po`), coupons (`zo`), payments (`jo`), employees (`Mo`), message centre (`Ro`), services (`Fo`, `Uo`), from `/home` to `/services/:id(\d+)`.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-37`).

**Placed:** 129 entries on capabilities and 1 `new` (1), none `out`, in 131 lines. One entry takes two lines (6, the app contract, as SA-35 gave it). Supports: 31 `core`, 70 `extension-point`, 29 `shows` on capabilities, and one `core` new line. No `own-service` or `outside`, no filler, no quality.

**Sources read:** the brief and what it names; SA-34's, SA-35's and SA-36's placements and notes, with each coordinator's check; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, the register's row for `portal-app-routes`, `index/ledger/portal-app.tsv`; the selection row. Then, to clarify the routes only:
- **layout-mf's bundle** @1861581, once, for the route arrays of this batch, the partner's permission set `Wi` and the features `io`;
- **the registry**, `structures/salla/portal-apps/prod/items.jsonl`, for which app serves each path. Each pattern was tested on the path with its parameters replaced by a number;
- **the React menu**, `structures/salla/portal-menu-definitions/ui-partners-portal-layout@prod/items.jsonl`, for the partner's items My Apps, Create Coupons, Domains Management, Transfer Domain, Domain Assignment, Employees, the Payments items and Reviews & Ratings, in English and Arabic;
- **the partner account:** `portal-me/partner@en/source.json` and `portal-private-settings/partner@en/items.jsonl` (its 68 features). It holds `expert`, `assign-orders`, `invoices`, `app_delete_reports`, `development_store` and `store-management`. It lacks `domain-purchase`, `temp-ready-stores`, `temp-payments-billing`, `temp-unified-reviews-page`, `temp-services-redesign` and `vip-home`;
- **for the paths no batch had placed** (apps served by ui-partners-portal-apps, -domains, -affiliate, -payments, -widgets and -login, which SA-38 and SA-39 hold):
  - ui-partners-portal-apps' index @137911 in `20261008T134248Z-portal-bundles-chunks1`, and its chunks for the fulfillment centers (@818372) and store events (@808074) in `20261008T134315Z-portal-bundles-chunks2`;
  - ui-partners-portal-payments' index @586322 (chunks1), for its routes' feature;
  - the partner routes sweep `20261008T145200Z-sweep-partner-portal-routes-en` (`actions.jsonl`; steps 004, 005, 014, 042 to 053), which the ledger joins to these apps.

`show --code 600` printed each entry's one item and its code. Every item is a route object of layout-mf's router with `name` and `meta` (or, for 22 to 27, a `redirect`), so none is `out` (SA-9's check).

## Rules my lines follow

SA-34's eight rules and SA-35's four, with SA-36's three, where the things are the same:
- **Rule 9:** each route goes on the thing of the page the registry serves at its path, citing that app, and keeps the line SA-34, SA-35 or SA-36 gave the same route. Almost every entry here is a route partners-mf (SA-35) or services-mf and ui-partners-portal-services (SA-34) already holds, and its reading names that batch.
- **Rule 3, with SA-36's rule 2:** a feature gate is the route's scope, whether layout-mf states it or the serving app does:
  - `app_delete_reports` (21), `development_store` (76 to 79), `store-management` (82 to 84), `invoices` (97 to 99, 106, 107) and `expert` (114, 115, 119 to 124) are held, and keep the support;
  - `assign-orders` (116) is the serving app's gate, by SA-34's line, and is held.
- **A temporary redesign the partner lacks makes the line `shows`** (SA-34's rule 3):
  - `temp-services-redesign` (120, 124, 126, 129, 130);
  - `temp-unified-reviews-page` (113);
  - `temp-payments-billing` (103 to 107).

  For 120 and 124 the serving app's gate is the redesign and layout-mf's is `expert`, so the scope names both.
- **Rule 10:** `/stores` (77) has a `beforeEnter` that opens it where `temp-ready-stores` holds and sends to `/store` otherwise. Both are the development stores, so the guard goes in `reading`, not `scope`.
- **Rule 11:** `requiresThemeAccess` is the theme routes' scope where their meta carries it; the reviews, requests and logs routes carry `resource:"User"` and no scope, as SA-35 placed them.
- **Rule 12:** an app's sub-page goes on its own thing's capability: snippets (10), settings (17), onboarding steps (18), reports (28, 29), shipping settings (30 to 32), and two that no batch had placed:
  - fulfillment centers (33 to 35) on CM-SHP-011;
  - store events (36) on CM-API-008.

  The domain's DNS page (48) goes on CM-SFR-009 by the same rule.
- **Redirects (22 to 27):** each sends to `/apps/:id`. They go on the capability of the place they send to, as SA-35 and SA-36 placed them.
- **Paths served by no app** (115, 119, 121, 127, 128): services-mf's pattern is anchored (`…|\/service|…)$`), so `/service/create`, `/service/:id`, `/service/:id/reviews` and the portfolio's add and edit project paths match no app of the registry. SA-34 placed services-mf's same routes, and I kept its lines, as SA-36 did for its six such paths.

## Lines no batch had placed

- **`/apps/list` and `/apps/list/:id` (3, 37):** ui-partners-portal-apps renders the partner's apps list (`AppsPage`) and an app's details (`AppDetailsPage`). The sweep opened `/apps/list`: 'Apps', 'App name', 'Status', 'Type' (step 042). They go on CM-APP-002 `extension-point`, as SA-35's `/apps`.
- **Fulfillment Centers (33 to 35):** `extension-point` on CM-SHP-011, whose cell holds Salla's app category Fulfillment and the unreleased dashboard flag `shipping-fulfillment-centers`. The breadcrumbs are 'Fulfillment Centers', 'Create Fulfillment Center' and 'Edit Fulfillment Center', under an app's details. The chunk lists centers by name, city and status (keys only: the apps' locale isn't held in these records).
  - partners-mf's pattern also matches these paths (its negative look-ahead excludes `shipping-settings`, not `shipping-centers`), but partners-mf declares no such route. ui-partners-portal-apps does.
- **Store events (36):** `core` on CM-API-008. The page's keys are `apps.details.webhooksEvents.*` (chunk @808074): the store events the app receives by webhook. That the page chooses the app's webhook events is a reading of its keys; the breadcrumb 'Store events' is the platform's word.
- **Domains (38 to 52), on CM-SFR-008, `shows`:**
  - The partner's menu names them 'Domains Management' / 'إدارة النطاقات', 'Transfer Domain' / 'نقل نطاق' and 'Domain Assignment' / 'التنازل عن النطاق'.
  - CM-SFR-008's cell holds this section (SA-C-301) and its feature `domain-purchase` as `shows`. I kept the cell's support for the partner's side (SA-34's rule 2).
  - The scope is `domain-purchase`, the route's gate in layout-mf. The held partner lacks it, yet the sweep opened `/domains`, `/domains/transfer` and `/domains/assignment` (steps 043, 045 to 047), served by ui-partners-portal-domains, whose own routes carry only a breadcrumb.
  - 48 (DNS management) goes on CM-SFR-009 `shows`. 50 (`/domains/actions/:action`, public, no gate) has no scope.
- **Create Coupons (`/coupons`, 89 to 92):** `core` on CM-APP-003, the same thing as `/coupon` (SA-34, SA-35). The sweep opened `/coupons/new` with 'Included Apps' and 'Beneficiary stores' (step 048). This settles SA-35's question: ui-partners-portal-affiliate's `/coupons` are app coupons, not affiliates' coupons.
- **Payments (103 to 107):** CM-PTN-003 (payouts) and CM-PTN-004 (billing), `shows`, scope `temp-payments-billing`, with `invoices` on billing.
  - ui-partners-portal-payments gates every route by `temp-payments-billing` and otherwise sends to `/payments/payouts`.
  - The sweep's requests of the other three paths ended there (steps 050 to 052).
- **`/employees` (108):** `core` on CM-PTN-002, as SA-35's `/employee`. It is served by ui-partners-portal-login, and the menu links it 'Employees' / 'الموظفين'.
- **`/reviews` (113):** `shows` on CM-PTN-005, scope `temp-unified-reviews-page`. The sweep's request ended at `/not-authorized` (step 053).
- **`/billing/operations/:id` (99):** `core` on CM-PTN-004, scope `invoices`, as SA-35's list.

## New things

No new thing of this batch's own. **VIP Partners**, entry 1 (`/home`, `vip-dashboard`, permission `vip-home`), is SA-34's, by the same name, `core` as SA-35 placed partners-mf's same route. The sweep's request of `/home` ended at `/not-authorized` (step 014): the held partner lacks `vip-home`.

## Entries I couldn't tell, and what would settle each

- **Domains (38 to 52), `shows` or `core`.** The pages show Salla itself selling and registering domains to partners:
  - 'After completing the purchase, the domain is reserved for you for 48 hours only to complete the registrant verification; otherwise, the domain will become available to other partners.', 'Browse domains store', 'Launch your first Saudi domain' (step 043);
  - 'transfer an existing domain from another registrar to Salla' (step 045).

  That reads as `core`. But CM-SFR-008 is the store's own domain, and whose store a partner's domain serves isn't stated. So I kept the cell's `shows` for the partner's side. The alternative is `core`, or a new thing (domains a partner buys from Salla). The domains app's locale and its domain store page would settle it; they aren't in what I read.
- **48, DNS management, on CM-SFR-009 `shows`.** CM-SFR-009 is the store domain's DNS records, `core` in its cell. Whether the partner's domain is a store's is the same question as above. The alternative is CM-SFR-008 alone.
- **33 to 35, Fulfillment Centers, CM-SHP-011.** CM-SHP-015 (shipping apps' settings, beside which the route sits) is the alternative. The apps' locale (`fulfillment.title`) would settle what a center is.
- **36, store events, CM-API-008 `core`.** CM-APP-004 (the app's lifecycle events) is the alternative, if the events are the app's own. The locale's `webhooksEvents.pageSubtitle` would settle it.
- **113, Reviews & Ratings.** The menu opens it for `manage-services` or `manage-influencers`, and the route requires `manage-services`. I placed it on CM-PTN-005, as SA-34 placed service reviews. CM-PTN-009 or CM-MKT-015 for influencer reviews could take a second line; ui-partners-portal-widgets' page (its app not reached, `index/ledger/portal-app.tsv`) would settle it.
- **The rest** carry SA-34's and SA-35's doubts for the same routes: 11 to 13 (custom plans), 20 (an app's DNS), 85 to 92 (coupons on CM-APP-003, `new:App coupons` the alternative), 100 (tax setting).

## Items against sources

The values agree: each entry stands for one route object of layout-mf's router at the line its locator gives, one item each. Where layout-mf and the serving apps differ:
- **`/apps/:id/shipping-centers`** matches both partners-mf's and ui-partners-portal-apps' patterns. Only ui-partners-portal-apps declares it.
- **`/coupons`** matches partners-mf's prefix `\/coupon` (its pattern has no end anchor) and ui-partners-portal-affiliate's. Only the affiliate app declares it.
- **Feature gates differ between the routers for the same path:**
  - layout-mf gates the domains by `domain-purchase`, which the partner lacks, while the page opened;
  - layout-mf gates `/payments/billing` by `invoices`, while ui-partners-portal-payments gates it by `temp-payments-billing`;
  - layout-mf gates `/services/:id/edit` and `/services/:id` by `expert`, while ui-partners-portal-services gates them by `temp-services-redesign` (SA-34).
- **`/message-center` (112)** carries here the partner set's `manage-notifications-center`, where partners-mf's carries the admin set's (SA-35's notes).
- **130's code** runs on into the next array's influencer breadcrumbs (`Vo`). Its own breadcrumb is 'Services' > 'Service Details'.

## For the second stage: what the sources state that no entry holds

- **CM-SFR-008:**
  - a purchased domain is reserved 48 hours for the registrant's verification (`20261008T145200Z-sweep-partner-portal-routes-en/steps/043.text.txt`, line 25);
  - 'This transfer includes a mandatory 1-year renewal added to the domain's current expiry date, billed now.' (step 045, line 25);
  - an assignment is of 'a .sa or .السعودية domain', and the current administrative coordinator must approve it (step 047, lines 26 and 31);
  - the partner's features `domain_dnssec` and `domain_variants` (`portal-private-settings/partner@en/items.jsonl`, positions 66 and 67).

  These are qualities and scope leads (Saudi domains).
- **CM-APP-003:** the app coupon form's fields: 'Minimum order amount', 'Maximum discount amount', 'Usage limit', 'Limit per user', 'Included Apps', 'Beneficiary stores' (step 048, lines 31 to 48).
- **CM-SHP-011:** the fulfillment centers' list keys (name, city, status), chunk @818372; the apps' locale isn't held.
- **The partner's menu group titles** for Domains, Marketing Tools, Payments and Support Tools are `portal-menu-definitions` items (parents 89, 78, 94, 98), with no route of their own here.

## The checker's lines, read again

- **`CHANGES` CM-APP-006@salla gains `extension-point`** (18, onboarding steps): the same line SA-35 gave partners-mf's same route, which the coordinator kept. Kept.
- **`CHANGES` CM-APP-009@salla gains `extension-point` and becomes held** (14 to 16, private access): the coordinator's ruling after SA-35, placing private apps `extension-point`. Kept.
- The two cells aren't amended yet, so the checker prints these again. Neither change is this batch's own.
- **`NOTE` first lead holds nothing:**
  - CM-ONB-004 on onboarding steps (18): the store's setup, a homonym, as SA-35 found;
  - CM-OPS-005 on `/themes/:id/logs` (67): a theme's build logs, not a store's logger, as SA-35 found.
- **`NOTE` containers** (29): `apps`, `apps/list`, `apps/:id`, `apps/:appId/custom-plans`, `apps/:appId/private-access`, `apps/:id/shipping-settings`, `apps/:id/shipping-centers`, `domains`, `domains/assignment`, `domains/:id`, `themes`, `themes/bundles`, `themes/new`, `themes/bundles/new`, `themes/:id`, `themes/bundles/:id`, `stores`, `store-management`, `coupon`, `coupons`, `payouts`, `methods`, `billing`, `payments/payouts`, `employee`, `service`, `services/:id`, `services-provider-portfolio`, `services`.
  - Each is a page of its own (a list or a details page), placed on its thing's capability as SA-34 and SA-35 placed the same paths.
  - Its children are the same capability's, except where rule 12 gives them another: `apps/:id`'s sub-pages, and `domains/:id/dns-management` on CM-SFR-009.
  - None is `out`.
- **`NEW`:** VIP Partners, 1 line.
- No quote printed 'found nowhere held'.

## Problems with the brief or the script

- **The brief changed during the batch:** an entry standing for several items whose conditions differ now gives each line its own item's scope. Every entry of this batch stands for one item, so no line changes.
- **The serving apps' locales** (ui-partners-portal-apps, -domains) aren't in the records I read. So the fulfillment centers, the store events and the domains' purpose are read from routes, keys and the sweep's pages.

The checker's last line, for SA-37: `130 of 130 entries placed; 0 problems`.
