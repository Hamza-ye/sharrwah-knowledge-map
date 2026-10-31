# Held pass, Salla, batch SA-7: notes

85 entries: the one entry of `dashboard-account-actions` (Mushammir), then the first 84 of `dashboard-app-routes` (items.jsonl lines 10 to 151: the apps `ui-merchant-{app-name}`, wallet, ticketing-system, template, setup, services, persona, organization, notifications, marketing-credits, marketing-camping, marketing-campaign, mahally, logs and login). Evidence at observed-sa@b0bd0b163.

**Placed:** 78 entries on capabilities, in 86 lines; 0 `new`; 7 `out` (the scaffold's five routes, the template app's `/home`, the login app's start location), in 3 lines. Eight entries take two lines (19, 37, 38, 53, 54, 55, 78, 81: see below); 89 lines in all. Every line supports `core` except three `shows`: 19 (setup, on CM-ACC-009 and CM-ACC-007) and 51 (the beta app `marketing-camping`), and 53's line on CM-MKT-005. No `own-service`, no `extension-point`, no filler, no quality, no scope: no item of this batch carries a `condition`, and no route's own item states a plan, a flag or a store gate.

Entry numbers below are the batch's order (`held_entries.py show --batch SA-7`).

## How I read the entries

A route entry gives only its app and path. Its structure's sources are the bundles `meta.json` lists under `reads` (archive records of run `20261008T115555Z-dashboard-bundles`, printed with `warc_text.py`). Where the path left the thing unclear I read, in this order:
- **the registry** (`structures/salla/dashboard-apps/prod/items.jsonl`), for the address each app is served at. Several apps declare paths relative to that address: the template app's `/list` is `/marketing/ads/template/list`, ticketing's `/*` and `/settings` are under `/tickets`.
- **the bundle**, at the route object: what it renders (an embedded page or app, a redirect, a placeholder), the staff permissions it is gated by, and, for the login app, each route's `name` (Auth, AutoLogin, ForgotPassword, Register, WaitingList, ...). Readings cite it as `bundle <run>/fetch.warc.gz@<offset>`.
- **the page as a run opened it**, through `derived/map-steps.tsv` (the module serving each step), cited as `<run_id>/steps/<NNN>.text.txt`.
- **the dashboard's locales** (`structures/salla/dashboard-translations/en/`) for a page that rendered nothing: marketing-credits (41 to 50) and setup (19).

**Leads.** The leads read each path's segments. I took the ones that name the entry's thing by its own path (customer_wallet, manage/experts, marketing/influencers, marketing/calendar, marketing/seo/*, channel/mahally, logs/*, quick access) and set aside the rest, which came from a common word: CM-TRU-017 for `request-form` (twice: a top-up request, not a legal request), CM-TRU-013 for `service-provider`, CM-API-001 and CM-PLN-001 for `advanced`, CM-CNT-003 for `page`, CM-ANL-002 for the template app's `/reports` breadcrumb, CM-API-003 for `access`, CM-ONB-002 for `access-restricted` (below).

## Rules my route lines follow, for SA-8 to SA-14

`SA-8` to `SA-14` hold the rest of `dashboard-app-routes` (items.jsonl line 152 onwards: localization, gamification, feedback, devstore, chat, ...) and haven't run. These are the rules I kept, so the coordinator can align them:
1. **The app's address first.** Read the registry's `path` for the app before reading a route: a relative path is the app's address plus the route.
2. **One line on the capability whose cell already cites the same link, route or app** (the cells' readings name Salla's links by path). A route that is the list, detail, form, settings or a step of that place stays on it, one by one.
3. **What the route renders decides, where the bundle states it:**
   - an embedded settings page (`EmbeddedPage`, `mode:"page"`) is the capability of the page it embeds (40: Notifications);
   - an embedded app (`mode:"app"`, such as `sweply`) with no maker stated: `shows` on what it does and `core` on CM-APP-007 (M-10), the maker a gap (53);
   - a redirect (`Navigate to=`) is the capability of its target, the redirect in `reading` (56, 58, 59, 61);
   - a route whose only element is a placeholder that names nothing (`"Harshal"`) is `out` (10); one whose element is `Coming soon` is listed and not offered: `shows`, its thing from the app's locale (19).
4. **A breadcrumb label object** (an item whose `keys` are only `label`, such as marketing-credits' `/xio`, `/request-form`) is the title of a route of the same app: it goes where its route goes, the label's locale in `reading` (41 to 45). Where the app has no such route (the template app's `/sales`, `/traffic`, `/reports`, `/campaign/reciept`), I placed it with the app's own thing and marked it unsure (15 to 18).
5. **`out`:** the scaffold `ui-merchant-{app-name}` (its bundle is a demo of placeholders: `{app-name}:btn.create-item`, a demo customers list, `/page-demo`), and a router's own objects (Vue Router's start location in the login app, 71). The engage app's `/home` (`/marketing/ads/engage/home`, also 'Harshal' on its page, `20261008T133523Z-sweep-demo-store-en/steps/217.text.txt`) will meet the same rule.
6. **A staff permission a route is gated by** (`permission:[...]` in the bundle) goes in `reading`, never `scope` (rule 5). The route's own `condition`, where an item has one, is its scope, by the module's name where it has none of its own (M-11).
7. **A page's plan or store condition read only from a run step** (organization's 'available to store owners on the Special plan') goes in `reading`, not `scope`: run steps clarify, and scope comes from the entry and its structure's sources.
8. **Sign-in routes** (`/auth/*`): the account's pages on CM-ACC-001, as its cell's sign-in app on /auth; the sign-in methods and checks (token sign-in, the verification code, passkeys, a sign-in restricted for unusual activity) on CM-TRU-001; the store chooser on CM-ACC-003; the country waiting list on CM-ACC-008.

## Entries I couldn't tell, and what would settle each

- **1, Mushammir** (`dashboard-account-actions`). The register says its panel wasn't opened. Later runs opened it: 'New chat', 'Welcome! How can I help you today?', 'Responses are AI-generated. Verify what matters most.' (`20261028T150337Z-journey-store-country-merchant-en/steps/010.text.txt`), and it answers through `api.salla.dev/ai-gateway/v1/api/copilotkit` (that run's note). Placed on CM-AIA-002, the AI assistant in the admin, `core`. The structure's item holds only the text, so the coordinator may want CM-AIA-002's Salla term "Mushammir" / "مشمر" (the Arabic sweep's header, `20261008T125139Z-sweep-merchant-routes-ar/steps/029.text.txt`). CM-AIA-001 holds the released flag `suggested-by-moshamer`, the same name.
- **2 to 6, the scaffold `ui-merchant-{app-name}`.** `out`, by the brief's rule. But CM-APP-007's Salla cell reads the registry's `/{app-name}` (SA-S-3581) as "the dashboard route named for each app", `extension-point`. Its bundle (`fetch.warc.gz@6824423`) is a template of an app, not a page for each app. The coordinator may want to read that cell's evidence row again.
- **10, the template app's `/home`.** Its element is the literal `"Harshal"`. `out`; the alternative is CM-MKT-007 with the app's other routes.
- **11 to 18, the template app** (`/marketing/ads/template`, under Salla Ads: its breadcrumbs are Marketing > Engage > Template, and its create button goes to `/marketing/ads/platform` with the feature `salla-ads`). Its templates are for WhatsApp, in-app notifications, email and SMS (email and SMS marked `templates.soon` on the page), approved by review. I placed them on CM-MKT-007, campaigns by message. The alternative is CM-MKT-010 (Salla Ads) by its address, or CM-NTF-004 (message delivery, its templates). Many of its page strings are untranslated keys (`templates.whatsapp`), which may mean it isn't finished; the success page reads in full. 15 to 18 are breadcrumb labels, unsure (rule 4 above). The engage app's own pages (`/marketing/ads/engage/*`, a later batch) would settle what sales, traffic, reports and receipt are.
- **19, `/setup/*`.** Its only element is 'Coming soon'. The `setup` locale describes 'Store Setup Mode', a waiting page with a waiting list, a launch date counter and a launch notice. Placed `shows` on CM-ACC-009 (site visibility before launch, whose Salla cell holds nothing, a CHANGES line) and CM-ACC-007 (maintenance mode). That the app reads this locale is a reading: the bundle inits i18n with the namespace `setup`, but renders none of its keys.
- **35, `/persona/qna`.** Its first question is the business's country ('Where is your business based?', 'Your country selection sets the legal requirements for your store.', `20261008T133523Z-sweep-demo-store-en/steps/133.text.txt`). That is CM-ONB-001's thing, but only the run step says so; I left it for the second stage.
- **39, `/organization`.** Placed on CM-ACC-003 (several stores under one owner). Its page calls them Companies, for 'store owners on the Special plan', managed by a company admin; the bundle gives it employees, roles and settings of its own (`ht`, `pt`, `kn`, unresolved paths). If the coordinator reads a company as a level above the store (Shopify's organization with its own users and billing), CM-ACC-003's note already says Salla's linked stores didn't show that; this route does.
- **51, `ui-merchant-marketing-camping` v0.1.3-beta-5.** The import map names it; the registry doesn't serve it (the registry routes `/marketing/campaign` to `ui-merchant-marketing-campaign`). Its page is a scaffold listing `/admin/v2/marketing/campaign` with 'Actions Bar Title' and `NAMESPACE:` keys. `shows` on CM-MKT-005; `out` as a scaffold is the alternative.
- **53, `/marketing/campaign`.** It embeds the app `sweply` (mode app), gated by the campaign permissions. CM-MKT-010 and CM-MKT-020 hold Sweply as the ads wallet's on Meta, with 'who Sweply is isn't stated'. Placed `shows` on CM-MKT-005 and `core` on CM-APP-007 (M-10). A statement of Sweply's maker would settle it.
- **54, 55, retargeting.** Both render the embedded page `/campaign`: 'SMS & app-push marketing campaigns'. Two lines each: CM-MKT-005 (its cell's link Campaigns is `/marketing/campaign/retargeting`) and CM-MKT-007.
- **62, `/marketing/settings`.** Placed on CM-MKT-005 as the marketing section's settings page. Its settings are coupons', promotions' and cashback's (second stage, below).
- **72 to 85, sign-in.** 82 (`/auth/message`, the cookies message) and 85 (`/auth/error`) are pages of the sign-in app with no thing of their own; I placed them on CM-ACC-001, `out` being the alternative. 84 (`/auth/access-restricted`) is on CM-TRU-001: the account's sign-in restricted for unusual activity. CM-ONB-002 (the store's restricted access) is the alternative the lead named; its Salla cell is `not-stated`. 78 (`/auth/register/:id?`) takes CM-STF-001 too, since its id is a staff invitation's (docs/GAPS.md and the bundle's 'Verifying your invitation details.').
- **60, `llms.txt`.** Placed on CM-CNT-007 with the SEO pages it sits among. No capability holds a file for AI crawlers (`caps --terms "llms"` finds nothing).

## The CHANGES lines

- **CM-ONB-004@salla becomes held, core** (34 to 38, `/persona/*`). The app is the new merchant's onboarding profile: welcome, questions, industries, plan and store transfer (the onboarding run `20261028T174130Z-journey-new-merchant-onboarding-en` and the sweeps). The cell's note had only onboarding to apps. Kept.
- **CM-MIG-005@salla gains core** (38, `/persona/scrapper`): 'Transfer your store data in one step', 'Your main store data will be imported to Salla while your current store stays unchanged.' The cell is `own-service` from the service's terms; this is the same move offered in Salla's own dashboard. Kept. CM-MIG-001 (import and export) is the alternative.
- **CM-ACC-009@salla becomes held** (19, `/setup/*`), by a `shows` line only, so the cell stays without a placement. Kept, unsure (above).

## Checker notes I read again

- Five quotes 'found nowhere held': each is copied exactly from a bundle the reading cites by its archive record (`{app-name}:btn.create-item`, the notifications embed's address, 'Actions Bar Title', 'Verifying your invitation details.', 'Manage all your stores from one account'). The checker doesn't read the bundles' archive records. `python3 -I method/warc_text.py /home/user/observed-sa raw/runs/20261008T115555Z-dashboard-bundles/fetch.warc.gz@<offset>` prints them (6824423 for the scaffold, 7529253 notifications, 19567248 marketing-camping; the login app's record is in the same file, its offset from `held_index.py` on `.../ui-merchant-login/v0.40.4/app.js`).
- Containers by path (`manage/experts`, `marketing/influencers`, `marketing/influencers/:id`, `marketing/ads/xio`, `marketing/seo`, `auth`): each is placed on the capability its own page opens, which is also the capability of all its children here.
- CM-TRU-017 as a lead (42, 48): no; `request-form` is the ad account's top-up request.

## What a source or run step states that no entry holds (for the second stage)

- **CM-MKT-010 or CM-MKT-020, qualities of the X top-up** (`structures/salla/dashboard-translations/en/marketing-credits.json`): 'Minimum amount: 5,000 SAR' (`form.minimum-amount-5000-sar`), 'VAT 15%', 'The recharge amount will be renewed in your ad account on X within 24 business hours, after verifying the information you provided.', 'Top-ups are calculated based on approved orders only.'; the page: 'Top up your account within 24/48 hours', 'Pay directly via Salla Wallet' (`20261012T010906Z-sweep-real-merchant-full-en/steps/244.text.txt`). Paying from Salla Wallet is a lead for CM-PLN-006.
- **CM-PTN-005:** 'All service providers are verified, and Salla ensures mutual commitment.', 'Get a refund if no agreement is reached in the initial order stages.' and the service categories with counts (`20261008T133523Z-sweep-demo-store-en/steps/129.text.txt`, `079.text.txt`); the order states (`128.text.txt`).
- **CM-MKT-015, CM-PTN-009:** 'Do you want to offer your services as an influencer? Join Salla's partners …' (`20261008T133523Z-sweep-demo-store-en/steps/132.text.txt`); an influencer's 'Trusted License' number and own terms (`20261008T184553Z-journey-influencers-demo/steps/002.text.txt`).
- **CM-ACC-003:** 'Companies are available to store owners on the Special plan and are managed by the company admin only.' (`20261008T133523Z-sweep-demo-store-en/steps/138.text.txt`), a plan scope.
- **CM-ONB-001:** the onboarding's country question and its countries (Saudi Arabia, UAE, Kuwait, Qatar, Oman, Bahrain, Other country) (`20261008T133523Z-sweep-demo-store-en/steps/133.text.txt`).
- **CM-PLN-001:** the onboarding's plan cards, 'Salla Basic … Free', 'Salla Plus … 99.00 SAR Month', 'Save 16%' annually (`20261008T141131Z-sweep-merchant-en/steps/137.text.txt`).
- **CM-MKT-002, CM-MKT-003, CM-LOY-003, CM-MKT-021:** the marketing settings' 'Show coupon field in cart', 'Enable coupons', 'Suggest products bought together', 'Show offers on product page', 'Automatically add free product to cart', 'Limit free items in cart', 'Offer priority', 'Cashback eligibility' (`20261008T133523Z-sweep-demo-store-en/steps/152.text.txt`).
- **CM-CNT-007:** the permalink choice 'Product ID(Recommended)' or 'Product name', and 'Any change in the settings (store link structure - Robots.txt file) may cause your store link to disappear from Google.' (`…/steps/149.text.txt`); SEO templates per product, category and brand (`…/steps/147.text.txt`); title 0/60 and description 0/160 limits (`…/steps/148.text.txt`), qualities.
- **CM-CHN-002:** 'Your store is currently hidden on Mahally' while maintenance mode is on (`…/steps/049.text.txt`), a link between Mahally and CM-ACC-007.
- **CM-SUP-005:** 'Give customers a self-service widget to submit support requests.' (`…/steps/117.text.txt`).
- **CM-MKT-007:** WhatsApp templates 'under review and will take about one to two hours for approval' (`…/steps/122.text.txt`); the locale's `note-customizing-require-whatsapp-re-approval` (in the template bundle).
- **CM-TRU-001:** quick access 'Works with iOS 17.1 and later', 'Works with Android 9.0 and later' (`index/run-notes.tsv`, `20261008T112402Z-stage0-merchant-quick-access`).
- **CM-ACC-008:** 'شكرًا لتسجيلك! … سنتواصل معك فور إطلاق الخدمة في منطقتك.' (`20261008T125139Z-sweep-merchant-routes-ar/steps/056.text.txt`).

## A structure whose items and sources disagree

None. The items hold only each object's keys, not their values, so a route's name, element, redirect and permission are in the bundle alone. Item 108 (entry 71) has a `path` of `/` but is the router's start location, not a route.

## Problems with the brief or the script

- **The checker doesn't search the bundles** (archive records in `meta.json`'s `reads`), so every quote from a route's own bundle prints a NOTE. Routes need those quotes more than anything else, since the items keep only keys.
- **The register's description of `dashboard-account-actions`** ('its own panel not opened yet') is out of date: later runs opened Mushammir's panel (above).

## The coordinator's check (30 October 2026, after the batch)

- **Every quote is found now.** The checker reads an archive record a reading cites as `<archive>@<offset>`, and the two lines that named the login bundle without its record cite it, `raw/runs/20261008T115555Z-dashboard-bundles/fetch.warc.gz@19713479`. SA-8 to SA-14 cite a bundle by its record, as this batch's other lines do.
- **CM-APP-007's Salla cell** reads the registry's `/{app-name}` as each app's own page. The bundle shows that entry is a scaffold, so the cell's evidence row is read again at Salla's amendment.
- **The register's description of Mushammir is out of date:** observed-sa's register says its panel wasn't opened, and later runs opened it (`evidence-map.md`).
- **The cells this batch changes stand:** Salla's onboarding profile (CM-ONB-004), its store transfer from another platform (CM-MIG-005), and its setup mode, `shows` (CM-ACC-009).
