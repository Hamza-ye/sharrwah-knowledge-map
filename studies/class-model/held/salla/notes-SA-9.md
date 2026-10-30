# Held pass, Salla, batch SA-9: notes

94 entries of `dashboard-app-routes` (items.jsonl lines 1163 to 1383: the apps app-maker-editor, bridge-sdk, themes-editor, `ui-merchant-ads-app-notification` and `ui-merchant-ads-google`). Evidence at observed-sa@b0bd0b163.

**Placed:** 87 entries on capabilities, in 112 lines; 0 `new`; 7 `out`, in 7 lines. 25 entries take two lines. 119 lines in all.
- Every line supports `core` except five `shows`: the two lines of the app-notification module (76, 78, on CM-MKT-007), and the second lines of the themes editor's marketplace suggestions (67 on CM-PTN-005, 68 on CM-APP-002, 69 on CM-SFR-005).
- No `own-service`, no `extension-point`, no quality.
- Filler: `google`, on the Google ads routes (82 to 94), as SA-8 wrote the ad platforms.
- Scope on 18 entries, all store gates read from the bundles (SA-8's rule):
  - `has_editor_enhancements` (19 to 21, 30, 31);
  - `landing-pages` (44);
  - `internal-pages` (48 to 51);
  - `kyc_country SA` (54);
  - `plan not basic` (66, 82 to 87);
  - `plan not basic;ai-bundles` (70).

Entry numbers below are the batch's order (`held_entries.py show --batch SA-9`). Bundles are cited by their record:
- the app maker editor: `raw/runs/20261008T115555Z-dashboard-bundles/fetch.warc.gz@35701216`;
- the other four: `raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz`, at 43645 (bridge-sdk), 606957 (themes-editor), 2149888 (ads-app-notification) and 4195591 (ads-google).

`held_index.py` gives the offsets. Both editors read the locale `editor` (`structures/salla/dashboard-translations/en/editor.json`); its `page_headers` give each route's title and description.

## How I read the entries

I kept SA-7's eight rules and SA-8's additions. Two of them did most of the work here.

**Rule 2: a route stays on the place its cell cites.**
- The app maker editor's routes all go on CM-CHN-006, whose cell cites `@salla.sa/app-maker-editor`.
- The themes editor's routes all go on CM-SFR-002, whose cell cites `themes-editor` at /themes/editor.

**Every thing a route names as its own takes a second line** (H-held rule 2), where the bundle and the locale show the route edits another capability's thing:
- the announcement bar on CM-SFR-007 (17, 18, 59, 60), in both editors, whose announcement-bar components take the same props (`ARTICLES_URLS`, `SallaApi`, `deleteConfirm`);
- the store's menus on CM-CNT-005 (19 to 21, 56 to 58). The app editor's menus are the store's: 'Adding, editing, reordering, or deleting custom menu items will automatically apply to all themes.';
- the store's pages on CM-CNT-003 (40, 50, 51);
- the landing pages on CM-SFR-006 (44);
- the social media accounts on CM-ACC-006 (52);
- the customer support channels and the Saudi Business Center certificate on CM-TRU-010 (53, 54). CM-TRU-010's core row reads 'store data the merchant updates: the Business platform certificate and customer-service channels';
- the store's own app on CM-CHN-006 (55, the footer's app links; 66, the store app banner);
- the store's details and branding on CM-ACC-006 (71);
- the AI section generator on CM-AIA-001 (70);
- the storefront wizard on CM-ONB-004 (73);
- the marketplace suggestions on CM-PTN-005, CM-APP-002 and CM-SFR-005 (67 to 69, below).

The app editor's own screens took no second line: splash, onboarding, tabs, product card, promotion title, background, loader and rating message are the app's, not another capability's things. The lead CM-ONB-004 on its `splash-and-onboarding` routes is the buyer's welcome screens in the app, not the merchant's setup.

**Store gates read from the bundle, as scope:**
- **App maker editor, `has_editor_enhancements`:** its menus, app background and loader routes render only where `initialData?.feature?.has_editor_enhancements`. CM-CHN-006's cell holds the released flag app-editor-enhancements, which this reads as.
- **Themes editor, `landing-pages` and `internal-pages`:** it guards its landing pages and its product, categories, pages and page-content routes with these flags (`window.Salla?.flags?.getObjectValue?.(…)`). In the demo store's features (`structures/salla/dashboard-features/demo@en/items.jsonl`), landing-pages is released for Plus, Pro and Special, and internal-pages on every plan.
- **Themes editor, `kyc_country SA`:** it renders `footer/sbc` only where the merchant's `kyc_country` is SA, or not set (the function `hP`). The condition has no name of its own, so I named it by what it is computed from (M-11).
- **Themes editor, `plan not basic`:** it renders `app-settings` only where `initialData.store.plan` isn't `basic`.
- **Google app, `plan not basic`:** it sends a basic store to /billing, as the YouTube app does (SA-8). Its breadcrumb labels (88 to 94) sit outside that gate and carry no scope, as SA-8's did.
- **AI generator (70), `plan not basic;ai-bundles`:** the route's own condition is a build setting (`VITE_WITHOUT_AI`). Its page offers the generator only where the plan isn't basic and the feature `ai-bundles` (`Ty.AI_BUNDLES`) is on, and shows an upgrade notice otherwise. I took that as the scope, as SA-8 took the YouTube app's in-page gate.

**Editor state isn't scope:**
- Many themes editor routes sit inside `!r`, where `r` is the URL holding `landing-N`, that is, the editor open on a landing page. That is the editor's state, not a store condition, so it goes in `reading` only.
- The flags' `hostname.endsWith('.test')` alternative is a test host. I left it out.

**Objects that are not routes, `out`:**
- 36, 74 and 80: cookie helpers' default options `{path:'/'}`;
- 75 and 81: a spreadsheet export's VML shape path;
- 79: a progress bar's class names;
- 77: the unserved app-notification module's catch-all 404 placeholder (SA-7's rule 3).

## Entries I couldn't tell, and what would settle each

- **76 and 78, `ui-merchant-ads-app-notification` v0.4.0.**
  - The import map names this module, but the registry serves /marketing/ads/app-notification-ads with another module, `@salla.sa/ui-merchant-app-notification` (import map v0.10.1). That is the one CM-MKT-007's cell cites (SA-S-3575), and the one the sweeps opened (`derived/map-steps.tsv`, e.g. `20261008T133523Z-sweep-demo-store-en` step 195).
  - So this module's routes are listed and not served. I placed them `shows` on CM-MKT-007, as SA-7 placed `marketing-camping`.
  - Its locale (`ads-app-notification.json`) holds app-notification campaigns ('App notification', 'Scheduling & frequency') beside a scaffold's 'Create Item'.
  - The alternative is `core`. A statement of which module serves the address would settle it.
- **67 to 69, the themes editor's marketplace suggestions:**
  - Merchant Services, read from `api.salla.dev/experts/v1/services`;
  - Recommended apps, from `api.salla.dev/marketplace/v1/search`;
  - the Section Store of bundles, 'Purchased add-on section'.

  Each name no maker or provider. By M-3, as refined after WC-3, a suggestion to buy or install from the platform's marketplace that names no maker is `shows`, so each second line is `shows`, and each first line is `core` on CM-SFR-002, as the editor's own page. My first write had them `core`, which gave CM-SFR-005 a core it doesn't hold; I changed it.
- **73, `themes/editor/onboarding-wizard`.** 'Design your storefront', in four steps: layout, brand, trust (social accounts, the SBC number) and homepage.
  - I gave it CM-SFR-002 and CM-ONB-004 (the setup wizard): the route's own word is an onboarding wizard for the store's first design.
  - This is a `CHANGES` line: CM-ONB-004 holds nothing yet. SA-7 (`/persona/*`) and SA-8 (`/gamification/*`) already make that cell held and core, but neither has been applied.
  - The alternative is CM-SFR-002 alone. A statement that the wizard is part of the store's setup (an onboarding step pointing to it) would settle it.
- **71, `themes/editor/main-info`.** 'Store details & branding': logo, fonts and colour schemes. I placed it on CM-SFR-002 and on CM-ACC-006 (store details). The alternative is CM-SFR-002 alone, if the coordinator reads branding as the theme's.
- **53, `footer/customer-service`.** Placed on CM-TRU-010, whose core row names customer-service channels. The page also shows 'Discover chat apps in the Salla App Store for faster, easier communication.' (second stage).
- **65, `themes/editor/page-options/:page_id`.** It renders the settings of a group of the theme, its header or footer: 'Menus in', 'Customize your store menus to make navigation easier.'. I placed it on CM-SFR-002 only, since its menus are /themes/editor/menus. CM-CNT-005 is the alternative.
- **85, the Google Shopping campaign.** Placed on CM-MKT-010. The bundle links a Merchant Center account for it ('ads-google:ad-design.your-merchant-center-account-has-been-successfully-linked'). That is a lead for CM-CHN-004 (product feeds), which I didn't trace.
- **94, `/reports/keywords`.** A breadcrumb label with no route in this app. Placed with the app's own thing, CM-MKT-010, unsure (SA-7's rule 4).
- **Leads set aside as common words:**
  - CM-CAT-003 and CM-ANL-002 (categories), CM-CAT-001 (product settings), CM-ACC-006 (the app's general settings), CM-MKT-001 (promotion title);
  - CM-SFR-005 (component), CM-SRF-001 (mobile app), CM-APP-010 (app settings), CM-SFR-015 (display), CM-SFR-013 (search), CM-PLN-001 (performance), CM-ANL-003 and CM-ANL-006 (reports, overview);
  - CM-MKT-012 (campaign), CM-CHK-003 (customization), CM-AIA-005 (channel, product), CM-SEL-006 (bundles: sections here, not product bundles).

## What a source or run step states that no entry holds (for the second stage)

- **CM-AIA-001:** the released flag `ai-bundles`, plans special, pro and plus (`structures/salla/dashboard-features/demo@en/items.jsonl`, position 425); the locale's 'Available on Plus & Pro' and 'AI-created sections' (`editor.json`, `ai.*`).
- **CM-SFR-002:**
  - the locale's plan alerts 'Design your store with more freedom using CSS' and 'Build more powerful stores with JavaScript' (`css_pro_alert`, `js_pro_alert`);
  - the custom font notice, 'By uploading a custom font to your store, you confirm that you have the license or permission required to use it for commercial purposes.', which makes the merchant responsible (`shows`);
  - the 'Try Twilight' link to docs.salla.dev from the customization page (themes-editor bundle, `C7e`).
- **CM-TRU-010:**
  - the SBC FAQ in `editor.json`: 'Store verification has moved from Maroof to the Saudi Business Center', and 'Your store must be certified through the Saudi Business Center to comply with Ministry of Commerce regulations.';
  - the Saudi Business Center and the Ministry of Commerce as fillers.
- **CM-SUP-004 and CM-APP-002:** 'Discover chat apps in the Salla App Store for faster, easier communication.' (`header_and_footer.footer.customerService.widget-desc`).
- **CM-CHN-006:**
  - the app editor previews the store's app through Appetize ('https://js.appetize.io/embed.js', with device 'iphone16promax', in the app maker bundle), a third party's service the editor uses;
  - 'Enable Liquid Glass for iOS devices' (`page_headers.tabs.liquid_glass_label`).
- **CM-CHN-004:** the Google app's Merchant Center catalog for Shopping campaigns (above).

## A structure whose items and sources disagree

None in the values. But the selection keeps one entry per app and path, so a second object with the same path has no entry. For this batch:
- the app-notification module's real `/` route (items.jsonl line 1340, `keys: element`, a redirect to /marketing/ads/app-notification-ads) has none. Its entry, 74, is the cookie library's `{path:'/'}` at line 1316, which I placed `out`;
- likewise, the themes editor's `/themes/editor/product`, `/categories` and `/pages` keep their page-switcher objects (37 to 40) and their route objects (48 to 50) as separate entries only because one path has a leading slash.

The coordinator may want the selection to say which object an entry of a repeated path stands for.

## Problems with the brief or the script

- **A repeated path:** above.
- **The checker's container NOTE** fires on every editor route that prefixes others, since both editors' paths are flat strings (`channel/mobile/editor/...`, `themes/editor/...`). Each is placed on the editor's capability, which is also its children's, as SA-7 placed containers by path.
