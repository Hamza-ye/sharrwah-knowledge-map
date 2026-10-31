# Held pass, Salla, batch SA-34: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163:
- 1 to 24: the last 24 rows of `plan-gates` (`derived/plan-gates.tsv` lines 262 to 285, `/?settings=/orders/orders.weight_threshold` to `/?settings=/wallet/max-credit-usage`);
- 25: the one entry of `portal-app-builder-functions` (`partner@en`);
- 26 to 130: the first 105 of `portal-app-routes` (items.jsonl lines 1 to 165, the apps ui-partners-portal-stores, ui-partners-portal-services, services-mf, portal and the first part of partners-mf, up to `/admin/store-management`).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-34`).

**Placed:** 93 entries on capabilities, 4 `new` (86, 87, 93, 94), 33 `out` (1 to 24, 73 to 76, 102, 104 to 107), in 125 lines. 21 entries take two lines (25, 27 to 30, 49 to 55, 64 to 72, 91, 98, 117). Supports: 75 `core`, 38 `extension-point`, 8 `shows`. No `own-service` or `outside`, no filler, no quality.

**Sources read:** the brief and what it names; SA-32's and SA-33's notes (plan-gates) and SA-7's to SA-10's (dashboard routes), with each coordinator's check; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `index/ledger-summary.tsv`, `index/ledger/portal-app.tsv`, and the register's rows for the structures. Then the steps and records below.
- **The five bundles**, read once each for their routes, their guards and their locales: `raw/runs/20261008T134145Z-portal-bundles/fetch.warc.gz` at @441623 (ui-partners-portal-stores v0.5.0), @540183 (ui-partners-portal-services v0.52.0), @1178908 (services-mf v0.0.264), @1503921 (portal root config v0.235.0) and @1510962 (partners-mf v2.0.698). partners-mf and services-mf carry their English and Arabic locales inside the bundle.
- **To clarify the routes only:**
  - the portal's registry, `structures/salla/portal-apps/prod/items.jsonl`, for the paths each app is served at;
  - the portal's menu, `structures/salla/portal-menu-definitions/ui-partners-portal-layout@prod/items.jsonl`, whose array `Li` is the admin's menu, with English and Arabic titles. I cite its bundle record, @928505, beside it: the checker didn't find quotes in the structure's path, probably because of the `@` in `ui-partners-portal-layout@prod`;
  - the partner account: `portal-me/partner@en/source.json` (`is_admin` false, its permissions) and `portal-private-settings/partner@en/items.jsonl` (its features);
  - `portal-categories`, for the types of the portal's categories;
  - the partner sweep's steps `20261008T124250Z-sweep-partner-portal-en/steps/009, 010, 011, 017, 018` and `20261008T145200Z-sweep-partner-portal-routes-en` (step 1 and its `actions.jsonl`).
- **For the coordinator's message:** after it came, `show --code 300` printed each route entry's items and code. They agree with what I had read: every entry here stands for one item, a route or, for `portal`, an app object, in the record I cite.

## plan-gates, 1 to 24: `out`, by SA-33's check

Every one of these rows is the kind SA-33's check made `out`. The columns `nav_features`, `features_list_plans`, `enabled_*`, `edu_allowedPlans`, `merchant` and `demo` are empty. The only lines are the public demo's 'Not included in your plan / Upgrade your plan to use this feature.'.

In each step the table names, those lines stand under the home page's widget 'Abandoned carts', behind the settings drawer:
- `20261009T033607Z-sweep-settings-public-demo-en/steps/042` to `075`, lines 51 to 53;
- step 050, lines 44 to 46.

That is SA-33's entry 95 (SA-E-24e071db). So each row is `out`, its reading naming entry 95, grouped in one line. The Basic merchant store's and the Pro store's steps (`20261008T141131Z-sweep-merchant-en` steps 332 to 365, `20261009T033607Z-sweep-settings-demo-en` steps 40 to 73) hold no plan line at all.

`plan-gates` is now placed whole (SA-32, SA-33, SA-34).

## portal-app-builder-functions, 25

The one function of the app SharrywahCad, 'Shipping Zone Created Function', on the trigger `shipping.zone.created`. It takes two lines:
- **CM-APP-005, `extension-point`:** the partner writes the function and Salla runs it on its trigger, as the cell's extension-point row holds;
- **CM-SHP-001, `core`:** the trigger is Salla's own event for its shipping zones, which the cell holds as a topic.

The function's name is the partner's own. The structure's other capture, `custom_scripts_events@partner-en`, holds no item.

## portal-app-routes: no batch has placed it before

**SA-35 to SA-39 hold the rest of `portal-app-routes` and haven't run.** They hold the rest of partners-mf (`/admin/store-management/:id` on: billings, sign-in, account, settings, apps, themes, subscriptions, stores, coupons, payouts, employees, agency profiles) and the other apps (layout-mf, affiliates-mf, ui-partners-portal-apps, -affiliate, -domains, -settings, -login, -payments, ui-partners-payment-package).

I kept SA-7's eight rules where a portal route is the same kind of thing as a dashboard route: the app's address from the registry, the cell that cites the same link, what the route renders, and a permission in `reading`. These are the rules my portal lines follow, so the coordinator can align the later batches.

1. **The registry first.** `portal-apps/prod/items.jsonl` gives each app's paths as a regular expression. Two apps can serve near paths:
   - services-mf serves `/service`, `/influencer/profile` and `/services-orders/:id`;
   - ui-partners-portal-services serves `/services`, `/services/orders` and `/influencers/*`.

   The sweep shows which one a page came from (`derived/map-steps.tsv`).
2. **The partner's own pages** (menus My Services, Influencer, Stores) go on the capability whose cell cites the same portal link, with the cell's support for the partner's side:
   - Services, Orders Center and Service Provider Portfolio on CM-PTN-005, `extension-point`;
   - My Profile and Campaign Orders on both CM-MKT-015 and CM-PTN-009, `extension-point`, since both cells cite the Influencer links;
   - Ready Stores on CM-DVT-005, `extension-point`, as its cell places the portal link. CM-DVT-003's cell places the same link `core`: the model differs between the two, and I followed the narrower one.
3. **A route's feature gate is its scope** (SA-8's rule, read here for the partner account). ui-partners-portal-services guards routes with `feature` and `permission` (the functions `_8` and `k8` send to `/dashboard` when either is missing); services-mf states `meta.feature`.
   - A feature the held partner's features list holds (`assign-orders`, `expert`, in `portal-private-settings`) keeps the line's support. The feature is the scope, and its value goes in `reading`.
   - A feature it doesn't hold, named as a temporary redesign (`temp-services-redesign`, `temp-influencer-redesign`), makes the line `shows`. The ruling on flags gives this: a pilot or test name off, as the Shopify beta case off in every held store. The pages the held partner is served instead are services-mf's (29, 30, 33, 34, 37, 38).
4. **Permissions go in `reading`** (`manage-services`, `services-update`, `manage-influencers`, `manage-agency-profiles`, `manage-orders`).
5. **The portal's admin** (`meta: {admin:!0, permissions:[o.C.…]}` in partners-mf and services-mf; the menu array `Li`, its top items `admin: true`) is the place of Salla's own admins. The held partner's `is_admin` is false.
   - A route there that manages a thing of partners or of the platform's marketplaces is `core` on that thing's capability: the platform itself reviews, verifies, lists or sets it.
     - apps, their publication requests and changes on CM-APP-002, whose cell holds Salla's team reviewing apps;
     - themes and their requests on CM-SFR-003;
     - bundle requests on CM-SFR-003, and on CM-SFR-005 `extension-point` as that cell places partners' bundles;
     - services and their requests on CM-PTN-005;
     - influencers, packages and campaigns on CM-MKT-015 and CM-PTN-009;
     - partner accounts, users and identity verification on CM-PTN-002;
     - contracts, help centre and message centre on CM-PTN-001;
     - ready stores on CM-DVT-005;
     - domains on CM-SFR-008;
     - webhooks and their categories on CM-API-008;
     - store-management requests on CM-STF-005.

     The admin permission (`o.C.MANAGE_*`, the admin set, not the partner set `o.Y`) goes in `reading`, never `scope`.
   - Routes that manage only Salla's own admin team are `out`: its admins, their permissions and roles (104 to 107), and the admin's own analytics page (102). They are not something offered to merchants, partners or developers. The brief's list of `out` kinds doesn't name this one; it is the nearest reading.
6. **Every route's title** comes from the bundle (`meta.title`, the breadcrumb) and the menu's `words`, English and Arabic, quoted in `reading`.
7. **Terms** are the path's segments, as SA-7 to SA-10 wrote them.
8. **The root config's app objects** (`portal`, 73 to 76) are `out`. They are `{name, path, env:"local"}`, used only on a local build, 'Using local development apps configuration'. Otherwise the root config fetches the registry from `https://api.salla.dev/ui/v1/apps/prod/portal`, which is structure `portal-apps`.

## New things

1. **VIP Partners** (الشركاء الـVIP), entries 86 and 87 (`/admin/vip-partners`, `/admin/vip-partners/create`).
   - What it is, in the locale (bundle @1510962): an institution under a contract ('Name of VIP Partner', 'Initial Contract Details', 'Number of Stores', 'Signed Contract') that invites users to set up stores ('Send invitation emails to invite users to set up their stores.', 'You have %{count} store to disperse at your convenience'), 'Typically used for Schools, Universities, and Companies' or 'Typically used for Government VIP Partners, sometimes big companies'. The partner set of permissions also holds `VIP_HOME: vip-home`.
   - Its place of its own: an admin menu item and its routes.
   - Proposed: domain F, area PTN, parent CM-PTN-001.
   - Searched: VIP; institution; invite stores; sponsored stores; الشركاء الـVIP.
   - The nearest capability is **CM-PTN-010** (Commerce-as-a-Service: a partner offers the platform's stores to its own merchants, which holds nothing on Salla). Its definition rests on partner APIs, and nothing here shows an API, so I left it `new`. The coordinator may join them.
2. **Transfer Requests** (طلبات نقل), entries 93 and 94 (`/admin/applications/transfer-requests/` and its details).
   - What it is, in the locale: the transfer of an app's ownership from one partner account to another, which the receiver accepts ('A request to transfer App ownership has been sent.', 'The App ownership has been transferred to your account successfully.', 'Your request is currently in review by reciever' (Salla's spelling)).
   - Its place of its own: the admin menu's Apps > Transfer Requests and its routes.
   - Proposed: domain F, area APP or PTN, parent CM-PTN-002 or CM-APP-001.
   - Searched: transfer request; app transfer; ownership transfer; app ownership; نقل التطبيق.
   - The checker's leads, CM-APP-001 (a store's installed apps) and CM-INV-006 (inventory transfers, by "transfer"), aren't this thing.

## Entries I couldn't tell, and what would settle each

- **The admin routes as a whole** (39 to 55, 77 to 130). I read them as the platform doing the thing, so `core`. Two other readings:
  - `out`, as the operator's back office;
  - `shows`, the operator's tools stating its processes.

  The capabilities' own definitions hold the platform's review (CM-APP-002 'its review of the apps it lists'; CM-DVT-005 'each reviewed by the platform'), which is why I chose `core`. The guard that reads `meta.admin` isn't in these bundles; the shared layout would settle it, and I didn't trace it (the brief: don't trace further).
- **39 to 41, Custom Marketing** (`/admin/services/blocks`): 'Manage Custom Marketing' under Services, permission manage-services in the route and manage-notifications in the menu. Where the content shows, and what it markets, isn't stated. I placed it on CM-PTN-005, unsure; the chunk (`r.e(244)`, `r.e(421)`) would settle it.
- **95, App Actions:** 'Run administrative actions on applications.', among them 'Cancel order and refund' (an app subscription's order) and 'Allowlist shipping scopes'. I placed it on CM-APP-002. CM-APP-003 (app charges, for the refund) and the scopes are the alternatives.
- **91, an app's shipping settings:** CM-APP-002 `core` and CM-SHP-015 `extension-point`. The settings, 'Service Types', 'COD Enabled', 'Geographic Coverage', are a shipping company's services set through its Shipping App.
- **117, Categories:** the portal's categories come in types, theme and app among them (`portal-categories`), so the line goes on CM-APP-002 and CM-SFR-003. Which ones this page sets isn't stated.
- **122 to 124, Coupons:** 'Coupons are used for promotions to apply discount on your selected Apps', 'This coupon was created by Salla Admin'. These are coupons on what merchants pay for apps. I placed them on CM-APP-003; `new:App coupons` is the alternative. The partner's own `/coupon` routes (SA-35 onwards) are the same thing.
- **127 to 129, `/admin/stores`:** the route is titled 'Development Stores', and the menu names it 'Ready Stores' / 'المتاجر الجاهزة' with 'Stores Requests'. I followed the menu and the review, CM-DVT-005; CM-DVT-004 is the alternative.
- **130, `/admin/store-management`:** 'Store management requests', partners' requests for access to merchants' stores ('Request Store Access'). I placed it on CM-STF-005 `core`. CM-STF-005's note keeps the partner's own side in domain F; this is Salla's side, not the partner's.
- **100, 101, domains:** CM-SFR-008's cell holds the portal's domain section as `shows`; the admin's approval of registrations is `core` here. What the partner registers a domain for (its own, or a merchant's store) isn't stated in these sources.
- **102, `/admin/dashboard`:** `out`, its chunk not held. If it holds the partner programme's measures, CM-PTN-001 is the alternative.

## Items against sources

None in the values: each entry stands for one item, and each item is the route or app object the bundle holds at that path. Two points on what the items don't say:
- the admin flag (`meta.admin`) and the `feature` guard are in the bundle only;
- the `portal` app's four items are a development configuration, not routes.

## For the second stage: what the sources state that no entry holds

- **CM-APP-005:** App Functions 'currently free', and 'Learn About App Function' (`20261009T003855Z-journey-portal-app-pages-en/steps/001.text.txt`, lines 209 to 211). The cell already holds 'free of charge'.
- **CM-APP-011:** the App Store's kits include 'Apps Made By Salla' (partners-mf locale `kits.appsMadeBySalla`, @1510962). Read with the App Store's own pages, this may be a category of apps the platform's company makes, a maker lead.
- **CM-APP-002:** a kit needs 'At least 2 apps with a plan are required' and allows 'Max is 10 Apps'. Featured apps are promoted 'for categories and stores' with a plan and beneficiary stores (locale `kits.*`, `featuredApps.*`). These are qualities and terms.
- **CM-MKT-015, CM-PTN-009:** an agency's influencer packages are shown on 'the influencer’s card in the Merchant' platform, targeted by store plan ('Supported Store Packages': All, Pro, Basic, Special, Plus) (services-mf locale `agency.*`, @1178908).
- **CM-PTN-002:** the verification workflow's states and actors ('Approved', 'Revision requested', 'Company reassigned', 'Access links revoked'; actors Partner, Admin, System, Webhook), in partners-mf locale `actions`, `actors`.
- **CM-SFR-008:** the states of a domain registration ('Awaiting payment', 'Awaiting data completion', 'Under review', 'Awaiting admin coordinator approval'), in partners-mf locale `domains.status`.
- **CM-SHP-015:** a shipping app's settings fields (country, service types, COD, tax responsibility, delivery duration, origin and destination cities, product and packaging types, service level agreement), in partners-mf locale `shippingSetups`.
- **CM-PTN-005:** a service's limits, in ui-partners-portal-services' validation (`maxPrice`, `maxDeliveryIn`, milestones, add-ons, items.jsonl lines 3 to 55, its zod paths); their values aren't stated in the items.
- **The portal's own features list** (`portal-private-settings`, 68 features). Several name places of later batches: `app-store-ads`, `apps_function`, `custom_plan`, `private_app_auto_approval`, `publication-offers`, `communication_app`.

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that already holds its support, or on a new thing.
- **`NOTE` "first lead holds nothing":**
  - CM-EVO-001 on the plan-gates line comes by "feature", "included" and "merchant", which every row of the table holds: no lead, as SA-32 and SA-33 found;
  - CM-B2B-002 (B2B companies) on `/admin/companies` and `/admin/users` comes by the words "companies" and "users": a partner's account, not a buyer business. No lead.
- **`NOTE` containers** (18): `services`, `services/:id`, `service`, `influencer/profile`, `services-provider-portfolio`, `agency/influencer-packages`, and the admin's `admin/services`, `admin/services/blocks`, `admin/influencers`, `admin/companies`, `admin/users`, `admin/verification-requests`, `admin/applications`, `admin/themes`, `admin/featured-apps`, `admin/app-store-ads`, `admin/coupons`, `admin/stores`. Each prefixes routes of the same thing and is placed on that thing's capability, as SA-7 placed containers by path. None of them is `out`.
  - The admin menu's groups with no page of their own (Users, Apps, Themes, Services, Influencers, Stores, Billings, Webhooks, Help Center) have no entry in `portal-app-routes`. They are `portal-menu-definitions`' items.
- **`NOTE` new thing with leads** (93, 94): CM-APP-001 and CM-INV-006, read above, are not the thing.
- **`NEW`:** VIP Partners, 2 lines; Transfer Requests, 2 lines.

## Problems with the brief or the script

- **A structure's path with `@` isn't searched for quotes.** Quotes cited from `structures/salla/portal-menu-definitions/ui-partners-portal-layout@prod/items.jsonl` and from `portal-me/partner@en/source.json` printed "found nowhere held", though they are there. Citing the menu's bundle record (@928505) settled the menu's quotes, and I wrote `is_admin` without quotes. The checker probably reads `…@prod/…` as an archive record.
- **The brief's known case changed during the batch** (`show --code`, the coordinator's message). My reading had already listed every item and read the bundles, and the new output agrees with it.
- **Admin routes:** the brief's `out` list and its supports don't name an operator's back office. The rule my lines follow (5 above) is a reading, for the coordinator to confirm before SA-35 to SA-39, which hold the admin's billings and affiliates.

The checker's last line, for SA-34: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **Rule 5 stands: the portal's admin routes are `core`** where they manage a partner or marketplace thing. Examples are app review on CM-APP-002, theme review on CM-SFR-003, and partner verification on CM-PTN-002. They are Salla's own staff's pages (`meta admin:!0`), and they show the platform doing the thing itself. The pages that manage only Salla's admin team are `out`. SA-35 to SA-39 keep to rule 5.
- **The plan gates' rows 1 to 24 are `out`,** as SA-33's check settled: the same widget behind the settings drawer. `plan-gates` is placed whole.
- **The checker now finds quotes in paths with `@`:** a structure's label folder, such as `ui-partners-portal-layout@prod`, now matches the cited-file pattern (`method/held_entries.py`).
- **New things, decided with every platform's:** VIP Partners (86, 87) and Transfer Requests (93, 94).
- **Cost:** 19.8 million tokens over 93 requests, about 152,000 an entry. It used `show --code` only after the coordinator's message. No cell changes.
