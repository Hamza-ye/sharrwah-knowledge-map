# Held pass, Salla, batch SA-35: notes

129 entries (effort high), evidence at observed-sa@b0bd0b163: entries 166 to 294 of `portal-app-routes` (items.jsonl lines 166 to 294), all of the app partners-mf v2.0.698, in one bundle record, `raw/runs/20261008T134145Z-portal-bundles/fetch.warc.gz@1510962`:
- 1 to 4: the end of the admin's routes (`/admin/store-management/:id`, `/admin/billings` and its two children);
- 5 to 41: the account and sign-in routes (array `w`), the misc routes (`x`) and the two homes (`S`);
- 42 to 129: the apps (`k`), themes (`A`), subscriptions (`C`), stores (`N`), coupons (`_`), payments (`T`), employees (`$`), message centre (`I`), agency (`P`) and the name-only routes (`E`).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-35`).

**Placed:** 127 entries on capabilities and 2 `new` (37, 41), none `out`, in 140 lines. 11 entries take two lines (20, 21, 24, 45, 120 to 124, 127, 128). Supports: 65 `core`, 63 `extension-point`, 10 `shows` on capabilities, and one `core` and one `shows` new line. No `own-service` or `outside`, no filler, no quality.

**Sources read:** the brief and what it names; SA-34's placements and notes with the coordinator's check, and SA-7's notes; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `portal-app-routes` and `portal-menu-definitions`, `index/ledger/portal-app.tsv`; the selection row. Then, to clarify the routes only:
- **the bundle** @1510962, once, for the route arrays, the guards `b` and `y`, the permission sets (module 9616: `o.Y`, the partner set; `o.C`, the admin set), the features (module 68725, `u.A`), and the English and Arabic locales it carries (modules 44940 and 6084, `JSON.parse`). The partners-mf chunks (`r.e(…)`) aren't held: the portal's chunk waves hold none of partners-mf's files, so a route's page is read from its route object and the locale only;
- **the registry**, `structures/salla/portal-apps/prod/items.jsonl`, for which app serves each path;
- **the partner's menu**, `structures/salla/portal-menu-definitions/ui-partners-portal-layout@prod/items.jsonl`, array `Oe` (the partner's items, positions 54 to 108) and `Li` (the admin's), for each route's title in English and Arabic;
- **the partner account:** `portal-me/partner@en/source.json` (`is_admin` false, `is_theme_allowed` true, `disable_private_apps` true, its permissions) and `portal-private-settings/partner@en/items.jsonl` (its 68 features).

`show --code 300` printed each entry's one item and its code; every item is a route object of partners-mf's router (`new i["default"]({mode:"history",…,routes:[...l,...S,...P,...w,...x,...k,...A,...C,...N,..._,...T,...$,...I,...E]})`), so none is `out` (SA-9's check).

## Rules my route lines follow

SA-34's eight rules, where the things are the same:
1. **The registry first.** It decides which app serves a path partners-mf names.
2. **The partner's own pages** go on the capability whose cell cites the same portal link, with the cell's support for the partner's side. So:
   - My Themes on CM-SFR-003 and Bundles on CM-SFR-005, `extension-point`;
   - App Subscriptions on CM-APP-003, `core`; Theme Purchases and Theme Subscriptions Trials on CM-SFR-003, `extension-point`;
   - Demo Stores on CM-DVT-004, `core`; Ready Stores on CM-DVT-005, `extension-point` (SA-34's choice of the narrower cell);
   - Payouts on CM-PTN-003, Billings and Operation records on CM-PTN-004, Employees and Settings on CM-PTN-002, Dashboard, Message Center and the Help Center on CM-PTN-001, all `core`;
   - Webhooks Log (`/logs`) on CM-API-008, `core`;
   - Orders Center on CM-PTN-005, Campaign Orders and the agency's influencer profiles on CM-MKT-015 and CM-PTN-009, Affiliate Profile on CM-PTN-009, all `extension-point`.
3. **A route's feature gate is its scope:** `partner_resource` (29), `app_delete_reports` (60), `invoices` (111, 112), all held by the partner. For 126 and 128 the gate is the serving app's (`temp-services-redesign`, `temp-influencer-redesign`, not held): `shows`, as SA-34 placed those routes.
4. **Permissions go in `reading`.**
5. **The portal's admin** (1 to 4) is `core` where it manages a partner thing, as the coordinator confirmed: store-management requests on CM-STF-005, partners' billings on CM-PTN-004.
6. **Titles** from the breadcrumb and the menu's `words`, English and Arabic.
7. **Terms** are the path's segments without its parameters (`apps;custom-plans/create`).
8. Not met here (the root config's app objects).

Four more, for what this batch holds and SA-34's didn't:
9. **A name-only route** (`{path, name}`, no element: 5 to 13, 18, 26, 27, 32 to 39, 125 to 129) is still a route of the router: partners-mf names it so it can navigate there. It is placed on the thing of the page the registry serves at its path, citing that app. Five such paths are served by no app of the registry (`/github/callback`, `/error-404`, `/error-500`, `/document-signed`, `/document-declined`): placed by their names, which the reading says.
10. **A guard that picks a component isn't a gate:** the function `b` renders another chunk where the account's features hold `temp-account-settings-redesign` (15, 16, 17, 24). The route opens either way, so the feature goes in `reading`, not `scope`. The guard `y` on 19 sends the form to `account-verification` where the features hold `kyc_id_verification`; the held partner lacks it, so the form opens. I wrote that in `reading`, not as a negative scope.
11. **`requiresThemeAccess`** (`meta`, on the themes' list, new, details, settings and component routes) is a condition on the account, its scope by its own key (M-11). Its value comes from what it reads: the held partner holds `is_theme_allowed` true. That is a reading: the guard that reads the key isn't in this bundle. The reviews, requests and logs routes carry `resource:"User"` instead, and no scope.
12. **An app's sub-page whose thing is another capability's** takes that capability alone, since a path's prefix isn't the entry's words:
    - snippets on CM-SFR-004;
    - settings on CM-APP-010;
    - onboarding steps on CM-APP-006;
    - reports on CM-ANL-006;
    - shipping settings on CM-SHP-015.

    The app's own pages (details, listings, publish, sent, reviews, DNS, deletion analytics, the redirects) stay on CM-APP-002. SA-34 gave the admin's shipping settings two lines (CM-APP-002 `core` for Salla's review, CM-SHP-015 `extension-point`); the partner's side has no review of its own, so one line.

**The partner's apps on CM-APP-002, `extension-point`** (42 to 48, 58 to 66): the menu names `/apps` 'My Apps' / 'تطبيقاتي'. The concern map holds the link in SA-C-194 (`SA-C-194/where/SA-S-1906`), the concern whose app categories CM-APP-002's cell cites, though the cell doesn't cite the link. The partner builds and publishes the apps the App Store lists, and Salla reviews them, as CM-SFR-003 places My Themes. 58's 'App reviews' are merchants' ratings of an app, a homonym of the cell's review by Salla.

## New things

1. **Ideas** (الإقتراحات), entry 37 (`/ideas-auth`).
   - What it is: partners-mf names the route `ideas-auth`, with no element. The registry serves it by ui-partners-portal-login. The locale labels a link 'Ideas' / 'الإقتراحات' (key `ahaLinkLabel`; a key's name isn't the platform's words, so I name no provider).
   - Place of its own: none held. It is an auth route with no page, and the ideas board itself isn't held. So `shows`.
   - Proposed: domain F, area PTN, parent CM-PTN-001.
   - Searched: ideas; suggestion; اقتراح; الإقتراحات; feedback; ideas board; feature request. The hits (CM-SUP-001 and CM-SUP-002 reviews, CM-APP-004 `app.feedback.created`, CM-SHP-022) aren't this.
2. **VIP Partners**, entry 41 (`/home`): SA-34's new thing, by the same name.
   - The route is named `vip-dashboard`, gated by the partner set's `vip-home`. The menu names it 'Home' / 'الرئيسية' for that permission.
   - It is the VIP partner's home: core. The held partner doesn't hold `vip-home`.

## Entries I couldn't tell, and what would settle each

- **53 to 55, private access, CM-APP-009 `shows` (a CHANGES line).** The locale defines private apps: 'Privately built and developed Apps for integration to either larger scaled or individual merchants.' They aren't shown in the App Store, and 'Publish your private app so you can request access for your stores.' That is CM-APP-009's thing (custom distribution for a merchant).
  - The routes are the access a private app's maker requests of a store's owner, who approves. That is what a partner asks of a merchant, so `shows` by the ruling.
  - The private app itself has no route of its own here (it is a type chosen when creating an app). So the cell becomes held with no placement.
  - Alternative: `extension-point`, reading the pages as the partner's own tool for building the merchant's app. The app creation page's chunk would settle it, and it isn't held.
- **57, onboarding steps, CM-APP-006 `extension-point` (a CHANGES line).** 'Add up to 3 steps to guide the merchant through installation and obtaining activation data.' The developer sets the steps the merchant meets on installing, the App Onboarding that CM-APP-006's cell holds as a module of the Embedded SDK.
  - Alternative: CM-APP-010, since the step's form is built with the same configuration builder (chunk 1736) as the app's settings.
  - CM-ONB-004 (the store's setup) is a homonym, as its own cell's reading says.
- **25, `/oauth/authorize`, CM-PTN-002 `shows`.** 'An application is requesting access to your Salla Partners account.' The access it grants covers apps, app functions, embedded apps, snippets, integrations and webhooks, and 'Use CLI-oriented tools, logs, and developer utilities connected to your Partners account.'
  - It is an app's consent on a partner account, so `shows` by the ruling.
  - No capability holds apps acting on a partner's account (a Partner API's authorization). CM-API-002 is a merchant authorizing an app for a store. A `new` thing, or CM-DVT-001 (the Partners Agent Kit), are the alternatives.
- **27, 38, GitHub.** I placed the account's connection to GitHub on CM-PTN-002, beside `/settings/connections`. The locale ties it to themes: 'Salla Partners want to access your GitHub account to start creating your Theme', 'Build check on GitHub'. So CM-SFR-003 or CM-DVT-001 are the alternatives. Where the page is used would settle it, and the chunk isn't held.
- **33, 34 (error pages) and 39 (`/not-authorized`).** I followed SA-7 and SA-8: an error page goes on its app's capability, so the portal (CM-PTN-001) for partners-mf's, and the partner account (CM-PTN-002) for the login app's. `out` is the alternative. 33 and 34 have no element and no app serving them.
- **32, `/welcome`:** CM-PTN-001, by 'Welcome to Salla for Partners' in the locale and its place beside `/dashboard` in the registry. CM-PTN-002 (the account just registered) is the alternative.
- **35, 36, a document signed or declined:** CM-PTN-001, as the app contract's result pages (45's 'App contract'). No page states it.
- **50 to 52, custom plans, CM-APP-003 `core`.** 'Custom Plans enable creating plans for merchants if existing plans do not meet their requirements.' This is a plan of an app for one store, charged through the platform. `core` follows the cell's portal link App Subscriptions; `extension-point` is the alternative (the partner sets the plan).
- **103 to 106, `/coupon`, CM-APP-003 `core`.** As SA-34 placed the admin's coupons: 'Coupons are used for promotions to apply discount on your selected Apps'. The registry also serves `/coupons` (the menu's 'Create Coupons' under Marketing Tools) by ui-partners-portal-affiliate, a later batch's. Whether that is the same thing or the affiliates' coupons, SA-36 to SA-39 will see. `new:App coupons` remains SA-34's alternative.
- **113, `/settings/tax-setting`, CM-PTN-003.** The breadcrumb is 'payout.taxSetting', and the route sits in the payouts array. The locale says 'Add the VAT number (only within Saudi Arabia) to help with transferring App earnings to your account.' CM-PTN-002 (an account setting) is the alternative.
- **59, `/apps/:id/dns-management`, CM-APP-002.** The page manages DNS records (A, MX and others: 'Manage your DNS, or Change DNS data'). Whose domain it is isn't stated. CM-SFR-009 (the store domain's DNS records) or a `new` thing would follow if the domain is a store's or the app's. The chunk would settle it.
- **60, deletion analytics, CM-APP-002.** 'Reasons for App deletion': why merchants removed an app. CM-APP-004 (the uninstall event) is the alternative.
- **24, security settings:** CM-PTN-002 and CM-TRU-001. The locale names two-step verification of the account. CM-TRU-001 is domain A's (the admin's sign-in), but its name covers 'the sign-in methods of the platform's accounts'.
- **129, `/affiliates/profile`:** CM-PTN-009 alone, whose cell cites the link Affiliate Profile. CM-MKT-014 cites only Affiliate Marketplace. SA-36 to SA-39 place ui-partners-portal-affiliate's own route.
- **1 to 4, the admin:** rule 5. The billings routes carry the admin permission `manage-users`, and 4 carries `manage-faq`, while the menu gives `manage-invoices` for both. I wrote the route's permission and the menu's.

## Items against sources

The values agree: each entry stands for one item, a route object of partners-mf's router at the line its locator gives. What the items don't say, or where two sources differ:
- **Name-only routes:** 25 routes carry only `name`. Their pages are other apps' by the registry: login, settings, apps, services and affiliate. Five paths are served by no app of the registry (rule 9).
- **Two apps hold the same paths:**
  - partners-mf declares `/settings`, `/settings/profile`, `/settings/change-password` and `/settings/security-settings` with elements, but the registry excludes them from partners-mf and serves them by ui-partners-portal-login;
  - partners-mf declares `/employee` and serves it, while the menu links `/employees`, which the login app serves;
  - the menu links `/payouts` and `/billing` under `/payments` where a feature holds (`N.PAYMENTS_BILLING`), and ui-partners-portal-payments serves those.
- **`/message-center` (119)** is a partner route, with no admin meta, gated by the admin set's `o.C.MANAGE_NOTIFICATIONS_CENTER`, 'manage-notifications'. The partner holds the partner set's 'manage-notifications-center', which the menu uses. Whether the route opens for the partner isn't stated; the guard isn't in this bundle.
- **The router's own labels differ from the locale's:** the breadcrumb 'Development Stores' is rendered 'Ready Stores' / 'المتاجر الجاهزة' by the locale. I followed the locale and the menu.

## For the second stage: what the sources state that no entry holds

All in partners-mf's locale, bundle @1510962 (English module 44940, Arabic 6084), by key:
- **CM-APP-006:** `myapp.appOnboardingStepsDesc`, 'Add up to 3 steps…': a quality, at most 3 onboarding steps.
- **CM-APP-009:** `myapp.PrivateAppNotes` (the definition above); `privateAppsLimit`, 'يمكنك إنشاء حتى %{limit} تطبيقات مجانية'. The account's `private_apps_limit` 0 and `disable_private_apps` true are in `portal-me`, and the feature `private_app_auto_approval` is in `portal-private-settings`. This is a lead for the cell that held nothing.
- **CM-APP-003:** `customPlans.showInStoreDesc`, 'Show custom plan banner in store'; custom plans' bonus features ('Allow the merchant to select the quantity'); coupons' 'Usage Limit', 'Limit per user', 'Maximum discount amount'.
- **CM-PTN-003:** `payout.taxNumberNotes`, a VAT number only within Saudi Arabia, a scope lead; `payout.durationSnackbarDescription`, payments 'Under Review' take 5 to 7 days to be approved, a quality; `payout.bankSubtitle`, the account holder's name must match the ID card and freelance certificate.
- **CM-PTN-002:**
  - account deletion scheduled after 30 days (`account.deleteModal.step3.subtitle`), refused while subscriptions are active (`account.deleteModal.error.subtitle`);
  - `account.businessTitleNote`, a commercial registration required for businesses in the Kingdom, and two registrations where the UAE is supported (`account.businessTitleNoteMulti`).
- **CM-TRU-001:** the partner's two-factor authentication by a code sent to the email (`account.OtpModalDesc`, `account.otpModalSuccessMsg`), against 'text messages' in `account.protectionandSecurityDesc`.
- **CM-DVT-002, CM-SFR-005:** bundles created with the Salla CLI (`myBundle.createWithCli`, `myBundle.createWithPortalNotes`). GitHub's build checks for themes (`mytheme.buildCheckOnGithub`, `mytheme.authorizeSallaDesc`) are a lead for CM-SFR-003 or CM-DVT-001.
- **Apps acting on a partner's account:** the OAuth grants listed under `account.OAuthPermission*`. A lead for a capability of its own, or for CM-DVT-001.
- **CM-APP-002:** `myapp.publicationCompare*`, the publication request compared with the live version (onboarding steps, functions, service workers, report builder, snippets).
- **CM-SFR-003:** 'You can preview your Theme on one of the demo stores or send a request to preview your Theme on a live store.' (`mytheme.hasNotPreviewStoresNotes`).
- **The menu's partner items with no route in this batch:** `/reviews` 'Reviews & Ratings' under Support Tools (feature `temp-unified-reviews-page`), `/domains/transfer`, `/domains/assignment` and `/conversations`. These are other apps' (ui-partners-portal-widgets, -domains, layout-mf).

## The checker's lines, read again

- **`CHANGES` CM-APP-006@salla gains `extension-point`** (57, onboarding steps): kept. The locale says the developer adds the steps that guide the merchant through installation, so a third party does it through the platform's interface. CM-APP-010 is the alternative (above).
- **`CHANGES` CM-APP-009@salla becomes held** (53 to 55, private access, `shows`): kept. The locale's definition of private apps is the cell's thing; the routes are the maker's access request, `shows` by the ruling. The cell stays without a placement.
- **`NOTE` first lead holds nothing:**
  - CM-OPS-005 on `/logs` (28) and the themes' build logs (86): no. Its reading lists Webhooks Log (SA-C-192) among the logs of particular features, not the entries of a store's logger, and build logs are a theme's;
  - CM-ONB-004 on onboarding steps (57): no, the store's setup, a homonym its own reading names.
- **`NOTE` containers** (20): `admin/billings`, `account`, `settings`, `apps`, `apps/:id`, `apps/:appId/custom-plans`, `apps/:appId/private-access`, `apps/:id/shipping-settings`, `themes`, `themes/bundles`, `themes/new`, `themes/bundles/new`, `themes/:id`, `themes/bundles/:id`, `store-management`, `coupon`, `payouts`, `methods`, `employee`, `agency/profiles`. Each is a page of its own, placed on its thing's capability. Its children are the same capability's, except where rule 12 or a second thing gives them another. `settings` and `account` prefix pages of CM-PTN-002 and CM-PTN-003 (the payout account, the VAT number) and CM-TRU-001 (security). `apps` and `apps/:id` prefix the app's sub-pages of rule 12. None is `out`.
- **`NEW`:** Ideas, 1 line; VIP Partners, 1 line.
- No quote printed 'found nowhere held'.

## Problems with the brief or the script

- **The brief changed during the batch:** the known case of a numeric `parent` now covers a route whose path is a constant. No item of this batch has a `parent`.
- **`show --code 300`** shows 300 characters, which cuts a route's `meta` short where its breadcrumb is long. The bundle's route arrays were enough, read once.
- **The partners-mf chunks aren't held** (`r.e(…)`; none in the portal's chunk waves). So what a page renders is read from the route and the locale only, which leaves 25, 27, 38, 57 and 59 unsure.

The checker's last line, for SA-35: `129 of 129 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **Private apps are `extension-point` on CM-APP-009** (53 to 55), not `shows`. The locale defines them: 'Privately built and developed Apps for integration to either larger scaled or individual merchants.', and 'Publish your private app so you can request access for your stores.' A partner builds the app for a given merchant, through Salla's private publishing and the store owner's approval: a third party doing it through what the platform provides (B-extent). Salla's CM-APP-009 cell, which held nothing, becomes held with `extension-point`; Shopify's cell, `core`, is the merchant's own App development.
- **CM-APP-006 gains `extension-point`** (57): the developer sets up to three onboarding steps that the merchant meets in the admin, beside the App Onboarding the cell holds as `core`. It stands.
- **The other lines stand** by SA-34's rules and the four added here:
  - name-only routes are placed by the page the registry serves;
  - a guard that only chooses which page renders goes in `reading`;
  - `requiresThemeAccess` is the theme routes' scope;
  - an app's sub-page goes on its own thing's capability.
- **New things:** Ideas (37), with no page held, and VIP Partners (41), SA-34's.
- **Cost:** 14.1 million tokens over 73 requests, about 109,000 an entry, with `show --code` from its start (SA-34 cost 152,000). Two cells change: CM-APP-009 from holding nothing, and CM-APP-006.
