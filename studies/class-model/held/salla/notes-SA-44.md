# Held pass, Salla, batch SA-44: notes

88 entries (effort high), evidence at observed-sa@b0bd0b163:
- 1 to 68: `portal-private-settings` (`partner@en`), the 68 features of `data.features`, in Salla's order;
- 69 to 78: `portal-report-builder-tags` (`partner@en`), the report creator's 10 tags;
- 79 to 88: `portal-report-builder-widgets` (`partner@en`), the report creator's 10 component types.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-44`). No batch had placed these three structures, and each ends here.

**Placed:** 87 entries on capabilities, 1 `new` (24, dark-mode), none `out`, in 92 lines. Four entries take two lines: 32 (affiliate-show-contacts), 44 (advanced-affiliate-marketplace), 54 (influencer_packages) and 58 (temp-affiliate-marketplace). Supports: 26 `core`, 61 `extension-point`, 5 `shows`. No `own-service` or `outside`, no filler, no quality.

**Sources read:** the brief and what it names. Then:
- SA-34's to SA-37's notes and placements, with each coordinator's check, and the rulings' last section;
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for the three structures, and `index/ledger-summary.tsv`;
- each structure's `source.json` and `meta.json`.

To clarify the entries only, I also read:
- **The portal bundles** of run `20261008T134145Z-portal-bundles`, the records SA-34 to SA-37 read: partners-mf @1510962, layout-mf @1861581, ui-partners-portal-layout @928505, services-mf @1178908 and ui-partners-portal-services @540183. I grepped each for the feature's name, the constant it is held under, and the route or menu item whose `feature` is that constant. That is one step: the bundle's features table and the route that names the constant. I didn't trace the constants further.
- **`portal-menu-definitions`,** both labels, for the 12 features its items name.
- **`portal-me/partner@en/source.json`:** the account's id 1739047897, from the same run and step as the features list, and its permissions.
- **`dashboard-features/demo@en`,** for the six names the merchant stores' features list shares with this one.
- **The other answers of `/partners/v1/api/private-settings`** in `raw/runs/*/responses.jsonl`, for whether the list changes (see "Items against sources").

## The rules my lines follow

1. **Scope:** every feature line takes the account, `partner account 1739047897`, as the coordinator's message gives it. The id is the account's in `portal-me` (same run, step 1). Each feature is listed as on, and its value ('on, its value') goes in `reading`. The report builder's tags and widgets carry no scope: their answers state no account, plan or condition.
2. **A feature that gates a route or menu item SA-34 to SA-37 placed** is that line's thing. It keeps that line's capability, as the coordinator's message asks, and also that line's support. The feature only opens the page for the account; the page is the statement of what is done and by whom. So:
   - the partner's pages are `extension-point`: apps, themes, services, affiliates, influencers, ready stores, Report Creator;
   - the platform's own pages for partners are `core`: billing, resources, conversations, onboarding, account settings, the admin's Featured Apps;
   - the partner's request for store access is `shows` (S7);
   - domains are `shows`, as the coordinator kept them.

   **This is my reading of the flag rule.** The brief's rule reads 'a released flag … supports `core`', and the ruling on the portal's permissions makes them `core` on what they gate. Read that way, the `extension-point` lines would be `core`. Then cells that hold only `extension-point` on Salla, such as CM-ANL-006, would gain `core` from a feature's name alone. I kept each page's support, so the feature lines change nothing the routes didn't. The coordinator may rule the other way.
3. **A feature that no held bundle uses** is placed by its name and by the constant partners-mf or layout-mf holds it under (APPS_REPORTS_BUILDER, APP_PAYMENT_LINK, HIDDEN_PLAN …). The locale strings are cited where the bundle holds them. Each such line says 'a reading of its name' in `reading`, and with a support:
   - the partner side's support, where the thing is a partner's tool;
   - otherwise `core`, by the flag rule;
   - `shows` only where I couldn't tell the thing (29, v3_updates).
4. **A `temp-*` name on for the account** (57 to 62) serves the account the redesigned page. It stays on the page's capability with the page's support. SA-34's rule 3 made such a feature `shows` only where the account lacks it.
5. **The report builder's tags and widgets** go on CM-ANL-006, `extension-point`, the cell's Report Creator. That is the builder through which developers build reports shown on the store's dashboard.
   - A tag is a kind of report, and CM-ANL-002's note keeps Salla's report kinds with the reports, so no tag takes a line on its subject's capability.
   - The leads by subject aren't taken: CM-CUS-001, CM-CHK-007, CM-MKT-022, CM-SHP-001, CM-INV-001, CM-STF-001, CM-PAY-005 and CM-PTN-003. CM-MKS-007 is a homonym ('Conversion rate' is a store's conversion, not a currency's).
   - The other reading is SA-25's ruling for service categories, `shows` on the capability whose work each tag names. It would add 9 or 10 lines, and none of them would change a cell.
   - A widget's description names examples ('such as browsers or channels', 'total sales, active users, or orders'). They aren't the entry's own thing, so they take no line.

## New thing

**Dark mode** (entry 24, `dark-mode`), `new:Dark mode`, `shows`:
- It has no place of its own: one flag, and the header's `dark-Toggler` in layout-mf (@1861581).
- The merchant stores' features list holds the same name, released on plus, pro and special (`dashboard-features/demo@en/items.jsonl`, line 376).
- Proposed: domain A or G, near the admin's own display, no parent. The coordinator may rather make it `out` as the portal's display preference.
- Its Arabic name isn't held in the entry.
- Searched: dark mode; dark; الوضع الداكن.

## Entries I couldn't tell, and what would settle each

The held bundles name none of these, or name only a constant. The lazy chunks the routes load (`r.e(…)`, `p.e(…)`) aren't in the run, and a capture of them, or of the portal with each feature's page, would settle each.
- **1, 23, 46, 2 (recaptcha-accounts, recaptcha, force-otp, dashboard-login):** on CM-TRU-001, the sign-in security of the platform's accounts, `core`.
  - That they guard the portal's own sign-in is a reading of their names.
  - dashboard-login could instead be a partner's sign-in to a store's dashboard (CM-DVT-004).
- **48, merchant-login:** layout-mf's `/api/merchant-login` with a redirect and a callback, beside its GitHub endpoint. I read it as signing in to the portal with a Salla merchant account, on CM-TRU-001. CM-PTN-002 is the alternative.
- **7, live-js** (constant LIVE_EDITOR): placed on CM-SFR-002 as a theme editor, unsure. The app snippets (`portal-app-snippets`, an app's JS on the storefront) are the alternative. The merchant stores hold the same name, released on every plan, which no batch has placed yet.
- **12, publication-offers; 13, apps_store_builder:** on CM-APP-002, `extension-point`, by their names and their place among the app features in Salla's order. services-mf's quotations ('Offer Expires In') make CM-PTN-005 another reading for 12.
- **21, hidden-plan:** on CM-APP-003, as an app's plan not shown. Its constant stands between SHIPPING_CENTERS and DEVELOPMENT_STORE_TEMPLATE, so a hidden plan of a store template is possible too.
- **22, app_bundles:** on CM-APP-002, `core`, as the App Store's collections of apps. The portal admin's kits (SA-34's notes: 'At least 2 apps with a plan are required') may be this. The themes' Bundles (CM-SFR-005) are a homonym.
- **29, v3_updates:** `shows` on CM-API-006, the nearest by its words. Nothing held says what it is.
- **30, react_appstore:** CM-APP-002 `core`. Whether it is the merchant's App Store or the portal's app pages isn't stated.
- **36, national-address:** on CM-PTN-002, by partners-mf's 'Enter your national address details.' among the partner's VAT and tax strings.
  - The feature's gate isn't held.
  - The merchant stores' same-named flag, not released, is the buyers' (CM-CUS-008), a homonym.
- **53, manage-banners:** on CM-PTN-005, `core`, read as the admin's Custom Marketing blocks. services-mf's locale has 'Display Type', 'Banners', 'Cards', 'Select Service', 'Select Influencer'. SA-34 was already unsure of this place.
- **27, intercom-invoice-events; 64, intercom:**
  - on CM-PTN-004 and CM-PTN-001, `core`, by their names and layout-mf's Intercom messenger (`initIntercom`);
  - Intercom, named only in a flag, is no filler (the brief);
  - the maker of the messenger is a third party, but no statement says Intercom does anything for partners beyond the code's call.
- **59, temp-affiliates-products:** on CM-PTN-009. The coordinator's check of SA-36 added CM-PTN-008 to the admin's 'Salla Affiliate Products' (Salla's packages, promoted by partners). If the partner's page is the same thing, 59 takes CM-PTN-008 too. SA-38 and SA-39 hold affiliates-mf's routes and would settle it.

## Items against sources

- **The items hold only `data.features`.** The answer's `settings` object has no entry: `app_invoices []`, `dev_stores_publish_limit 2`, `dev_stores_create_limit 1`, `maximum_plans 4`, `max_trial_days 7` (`source.json`). See the second stage below.
- **The list changes over time.** Of the account's `/partners/v1/api/private-settings` answers:
  - `20261008T123118Z-sweep-partner-portal-ar` step 27 (`responses/0242.json`) has the same features, with `dev_stores_create_limit 0`;
  - `20261028T160451Z-journey-portal-demo-store-new-en` steps 2 and 9 (`responses/0006.json`, `0015.json`) add six features: `domain_requests`, `login-app-info`, `temp-influencer-campaign-redesign`, `temp-influencer-redesign`, `temp-service-orders-redesign` and `temp-services-redesign`.
  - So on 28 October the account held `temp-services-redesign` and `temp-influencer-redesign`. SA-34's rule 3 made their routes `shows` because the 8 October list lacks them. The structure is the 8 October answer, so my lines follow it. The later answers are a lead for the coordinator, for the 16 `shows` lines SA-34 (8), SA-35 (3) and SA-37 (5) scoped by those two features, on CM-PTN-005, CM-MKT-015 and CM-PTN-009.

## For the second stage: what the sources state that no entry holds

- **CM-DVT-004:** the account may publish 2 development stores and create 1 (`dev_stores_publish_limit 2`, `dev_stores_create_limit 1`; 0 in the later answers). The cell holds 'up to ten each' (SA-S-5108). Qualities, in `portal-private-settings/partner@en/source.json`.
- **CM-APP-003:** `maximum_plans 4` and `max_trial_days 7`, an app's plans and trial days by their names, are qualities; `app_invoices []` is the account's own data (same file).
- **CM-SFR-003:** the themes' locale states 'The maximum number of  preview stores are 4 stores' (Salla's two spaces) and 'The maximum number of requested is 10 Requests' (partners-mf, @1510962). These are qualities of a theme's preview stores and requests.
- **CM-APP-003:** partners-mf's locale names 'App Addons Commission Percentage', 'Payment Link Commission Percentage' and 'Influencer Commission Percentage' (@1510962), terms of Salla's commission on what apps charge.
- **The portal's own features that the bundles define and this list doesn't hold:**
  - in partners-mf @1510962: THEME_PRICE_RESTRICTION (`theme_price_restriction`), SHOW_APP_FREE_PLAN (`show_app_free_plan`), APPS_SERVICE_WORKERS (`apps_service_workers`), PAYOUT_BILL (`payout-bill`), SHIPPING_SETTINGS_PAGE (`shipping_settings_page`), SHIPPING_CENTERS (`shipping_centers`), DEVELOPMENT_STORE_TEMPLATE (`development_store_template`), APP_ADDONS_TAXABLE (`app_addons_taxable`), APPS_ACTION_LINKS (`apps_action_links`) and KYC_ID_VERIFICATION (`kyc_id_verification`);
  - in layout-mf @1861581: `temp-ready-stores`, `temp-payments-billing`, `domain-purchase`, `temp-home-page`, `temp-home-page-native-off` and `temp-unified-reviews-page`.

  Each names a place that the second stage may read for its cell, such as CM-SHP-011 for shipping centers.

## SA-45 to SA-47, which haven't run: the lines they would meet

- **`report-widgets`** (SA-45 to SA-47) holds the same 10 type names as entries 79 to 88 (the register: agrid 37, unit 30, ranking 19, distribution 14, plot 11, breakdown 9, calendar, summary, bar, pipe 1 each). `report-catalog` (SA-45) names some of them as its reports' components (`type: agrid`).
  - My lines put the types on CM-ANL-006, as parts of the Report Creator.
  - The dashboard's own reports are CM-ANL-002's: the same component in a report Salla builds is CM-ANL-002 `core`, and in a partner's report CM-ANL-006 `extension-point`. The coordinator aligns them.
- **`report-widget-categories`** (SA-45) holds, among its 19 values, 6 of my tags' values: `sales`, `customers`, `visits`, `abandoned_carts`, `conversion_rate` and `shipping`. Its `payments`, `payments-shipments` and `stock` are near `payouts` and `inventory`. It has no `operations` or `employees`, and adds 'App Widget', the apps' own category.
  - My tags 69 to 78 are CM-ANL-006's.
  - Where SA-45 places a category on CM-ANL-002, or on its subject's capability, the coordinator aligns the two (rule 5 above).

## The checker's lines, read again

- **`CHANGES`:**
  - CM-APP-006 gains `extension-point`, by line 9 (entry 8, apps_onboarding): the developer's onboarding steps;
  - CM-APP-009 gains `extension-point` and becomes held, by line 12 (entry 11, private_app_auto_approval).

  Both are the changes SA-35's routes already make, which the coordinator's check of SA-35 accepted. I read each against its source again and kept them. The account's portal-me holds `disable_private_apps` true and `private_apps_limit` 0, which the line names.
- **`NOTE` "first lead holds nothing":** lines 86 and 92, breakdown and ranking, lead to CM-INV-010 by the words 'Displays' and 'حسب'. That is a word every widget's description holds, so it is no lead.
- **`NEW`:** Dark mode, 1 line.

## Problems with the brief or the script

- **An apostrophe in prose reads as a quote.** I wrote ’ for apostrophes, and rephrased the plural possessives, so that each ' … ' in a reading is a quote. A rule in the brief would help.
- **What a feature does is often held nowhere.** 34 of the 68 names stand in no held bundle, and 17 more only in a features table or as a constant no held route or menu item uses. The brief's limit, not tracing a key through other code, leaves them to a reading of their names, marked as such.
- **Two readings of the flag rule for a partner portal** (rule 2 above). The brief's flag rule was written for a merchant's store. It meets the coordinator's `extension-point` for the partner's pages, and the ruling makes the portal's permissions `core`. I kept the pages' supports; a ruling would settle it for SA-38, SA-39 and the portal's `permission-gates` rows.

The checker's last line, for SA-44: `88 of 88 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **The flag rule as the notes read it is the ruling after SA-44:** a partner's feature takes the support of the page it gates.
- **The features list of 28 October is read for the two redesign features.** The same account's later answer (`raw/runs/20261028T160451Z-journey-portal-demo-store-new-en/responses/0006.json`) lists 74 features, among them `temp-services-redesign` and `temp-influencer-redesign`. So the 20 portal lines that were `shows` behind them, in SA-34, SA-35, SA-37 and SA-38, are `extension-point` now. The other gates (`temp-payments-billing`, `temp-unified-reviews-page`, `temp-home-page`, `domain-purchase`) are still absent, and their lines stay. `evidence-map.md` notes the difference.
- **Dark mode is `out`:** a preference of the interface's display, which places nothing of the class. The portal's interface language stays a new thing (SA-28), since it bears on a market.
- **The report builder's lines stand on CM-ANL-006.** SA-45 to SA-47 place the dashboard's own reports on CM-ANL-002, and keep the partner's Report Creator apart.
- **The account's settings** (`dev_stores_publish_limit 2`, `dev_stores_create_limit 1`, `maximum_plans 4`, `max_trial_days 7`) are qualities for CM-DVT-004 and CM-APP-003, for the second stage.
- **Cost:** 14.2 million tokens over 76 requests, about 161,000 an entry. No cell changes beyond SA-35's.
