# Held pass, Salla, batch SA-38: notes

81 entries (effort high), evidence at observed-sa@b0bd0b16: entries of `portal-app-routes` at items.jsonl lines 567 to 818:
- 1 to 38: the end of layout-mf v0.0.337's router (`app.js`, bundle `raw/runs/20261008T134145Z-portal-bundles/fetch.warc.gz@1861581`). They are the arrays `Yo` (influencer), `Ho` (redesigned influencer), `Go` (affiliates) and `qo` (agency), then the router's own `/` and `*`, and an item of its native mobile navigation;
- 39 to 54: affiliates-mf v0.9.264 (`main.js`, @2098236), the admin's affiliate routes (`et`) and the partner's (`tt`);
- 55: ui-partners-payment-package v0.7.0 (`raw/runs/20261008T134248Z-portal-bundles-chunks1/fetch.warc.gz@15553`);
- 56 to 60: ui-partners-portal-affiliate v0.136.0's routes with a string path (chunks1@75945);
- 61 to 70: ui-partners-portal-apps v0.84.1's router `PH` (chunks1@137911);
- 71: ui-partners-portal-domains (chunks1@422550);
- 72 to 77: ui-partners-portal-login (chunks1@458454);
- 78, 79: ui-partners-portal-settings v0.9.1 (chunks1@735201);
- 80, 81: two page chunks of ui-partners-portal-affiliate (`raw/runs/20261008T134315Z-portal-bundles-chunks2/fetch.warc.gz@332658`, @536755).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-38`).

**Placed:** 79 entries on capabilities, none `new`, 2 `out` (55, 71), in 115 lines. 34 entries take two lines:
- 1 to 11 and 29 to 35, the influencer and agency pages, on CM-MKT-015 and CM-PTN-009;
- 38, the mobile navigation's Influencer item, on the same two;
- 21, 24 to 26, 51 to 53, 80 and 81, the Affiliate Marketplace, on CM-PTN-009 and CM-MKT-014;
- 41 to 44, Salla's affiliate products, on CM-PTN-008 and CM-PTN-009;
- 46, merchants' affiliate products, on CM-PTN-009 and CM-MKT-014;
- 75, security settings, on CM-PTN-002 and CM-TRU-001.

Supports: 30 `core`, 79 `extension-point`, 4 `shows`. No `own-service` or `outside`, no filler, no quality.

**Sources read:** the brief and what it names, and before the entries:
- SA-34's to SA-37's notes, with each coordinator's check, and their placements for the same paths, which I read through `entries.tsv`;
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `portal-app-routes` and `portal-apps`, `index/ledger-summary.tsv`;
- the selection row, and `show --meta`.

Then, to clarify the routes only:
- **the bundles above,** once each, for the route arrays, their guards and features (layout-mf's `io` and `Wi`; ui-partners-portal-affiliate's `Mt`, its route constants and its wrapper `dl`; the login app's `le`, `Ds`, `p0` and `x0`);
- **partners-mf's bundle @1510962,** for its locale on the App Details Builder and the Service Workers;
- **for the meaning of the apps' sub-pages:** four chunks of ui-partners-portal-apps in chunks2, @791855 (BuilderEditor), @796629 (BuilderHome), @822308 (the service workers' editor) and @866710 (the snippet editor);
- **the registry,** `structures/salla/portal-apps/prod/items.jsonl`. I tested each pattern on each path, with its parameters replaced by a number;
- **the React menu,** `structures/salla/portal-menu-definitions/ui-partners-portal-layout@prod/items.jsonl`, for the partner's groups Affiliates, Influencer and Marketing Tools, the agency items, and the admin's group Affiliater, in English and Arabic;
- **the partner account:** `portal-me/partner@en/source.json` (type person, `is_admin` false, its permissions) and `portal-private-settings/partner@en/items.jsonl` (its 68 features);
- **the sweeps the ledger joins to these apps:**
  - `20261008T124250Z-sweep-partner-portal-en`, steps 012 to 017, 019, 020, 031, 039, 040, 043;
  - `20261008T145200Z-sweep-partner-portal-routes-en`, steps 002, 003, 006 to 008, 033 to 035, 042, 048, 054 to 058, 061;
  - the app page `20261009T003855Z-journey-portal-app-pages-en/steps/016.text.txt` (`/apps/list/1080110626`).

`show --code 600` printed each entry's items and code. Entries 62 to 70 and 79 printed no code: they are child routes, which I read in their parent's array (items.jsonl positions 692 to 711, 805 to 807).

## Rules my lines follow

SA-34's eight rules, SA-35's four and SA-36's three, with SA-37's lines for the serving apps' own routes (its coordinator's check):
- **Rule 9:** each layout-mf route goes on the thing of the page the registry serves at its path, citing that app. It keeps the line SA-34, SA-35 or SA-36 gave the same route:
  - the influencer pages (services-mf, ui-partners-portal-services) on CM-MKT-015 and CM-PTN-009, `extension-point`;
  - the agency pages on the same two, as SA-35;
  - the admin's affiliate routes as SA-36, whose lines the coordinator kept.
- **SA-37's lines for the serving apps:**
  - `/apps/list` and an app's details on CM-APP-002, `extension-point`;
  - store events on CM-API-008, `core`;
  - coupons (ui-partners-portal-affiliate's `/coupons`, 57 to 60) on CM-APP-003, `core`, by the form's 'Included Apps' and 'Beneficiary stores';
  - the settings and employees pages of the login app on CM-PTN-002.
- **Rule 12:** an app's sub-page goes on its own thing's capability:
  - reports (64, 65) on CM-ANL-006, as SA-35 and SA-37;
  - snippets (69) on CM-SFR-004;
  - functions (67) on CM-APP-005, as SA-34 placed the app's function.

  Two had no line before: the builder (66) and the service workers (68), below.
- **Rule 3 with SA-36's rule 2:** a feature gate that layout-mf states is the route's scope:
  - `influencer_packages` (7 to 9), `affiliate-orders` (14), `advanced-affiliate-marketplace` (21) and `affiliate-active-merchants` (22, 23, and ui-partners-portal-affiliate's own 56);
  - `temp-affiliates-profile` (18, 19) and `temp-affiliates-products` (20, 28). These two are named as temporary, but the held partner holds both, so the line keeps its support, as SA-34's rule 3 keeps a held feature.

  `temp-influencer-redesign` (10, 11), which the partner lacks, makes those lines `shows`, as SA-34 and SA-35 placed the same routes.
- **Permissions go in `reading`.** The held partner holds manage-affiliates, manage-influencers, manage-orders, manage-coupons and manage-apps. It lacks manage-agency-profiles, and the sweep's requests of the agency pages ended at `/not-authorized`. The lines keep SA-34's and SA-35's support, with the permission in `reading`.

## The affiliate pages: what the sources show

No batch had placed the partner's affiliate pages except `/affiliates/profile` (SA-35, CM-PTN-009). The sweeps show three things:
- **The Affiliate Marketplace** (21, 24 to 26, 51 to 53, 80, 81), 'Promote the apps, themes and services' with 'Discover store affiliate opportunities and pick what fits your audience and content.' (`…-sweep-partner-portal-en/steps/013.text.txt`), and the filter 'Stores', 'Products', 'Services', 'Themes', 'Apps' (`…-routes-en/steps/058.text.txt`). It offers partners' products and stores' opportunities. CM-PTN-009's cell and CM-MKT-014's both cite the link Affiliate Marketplace, so each takes both lines, as SA-34 gave the influencer links both cells.
- **The partner's own affiliate products** (12, 15, 16, 20, 27, 28, 48, 54), the menu's 'Add Affiliate Product' / 'سوق لمنتجاتك بالعمولة' under Marketing Tools: 'Every opportunity you create gives marketers an incentive to promote your products for a commission' (step 020). The create form says 'Select a product from a Salla partner for affiliate marketing.' (routes-en step 056). The partner offers its own apps, themes or services to affiliate marketers. I placed these on CM-PTN-009 alone: the cell is the partners' side of the affiliate programme.
- **The partner as an affiliate marketer:** the profile, link statistics, My Opportunities, Affiliate Orders and Active Merchants (13, 14, 17 to 19, 22, 23, 49, 50, 56). They go on CM-PTN-009 alone, as SA-35 kept the profile.

**affiliates-mf's old addresses open the new pages.** The sweep's requests of `/affiliate`, `/affiliate/profile` and `/affiliate/marketplace` ended at `/affiliates`, `/affiliates/profile` and `/affiliates/marketplace` (routes-en steps 054, 055, 057). The menu chooses the address by the features `temp-affiliates-products` and `temp-affiliates-profile`, which the partner holds. This is like SA-35's rule 10: the page differs, not whether it opens. So I wrote it in `reading`, with no scope on affiliates-mf's routes. Which code makes the redirect isn't in what I read.

## New things

None. Every entry's thing is a capability the cells already hold.

The two sub-pages no batch had placed were searched first, with `class_slice.py caps --terms "service worker; service-workers; app function; snippet; builder; app blocks; store builder; apps_store_builder"`:
- **Builder** (66, `/apps/:appId/builder/block/:blockId`): partners-mf's locale has 'App Details Builder' and 'Customize your App details view for the merchants via the builder' (@1510962). The route's own chunks offer 'builder.home.add_component' and blocks. CM-APP-002's cell holds the App API's folder App Details Builder, so the entry goes there, `extension-point`.
- **Service Workers** (68): the app page says “Use Service Workers to create Custom Logic that works on Merchant's Store.” (`20261009T003855Z-journey-portal-app-pages-en/steps/016.text.txt`, line 87). The editor's files are named 'service-worker.js' and 'serviceworker.js' (@822308). I read it as code the app adds to the storefront, so CM-SFR-004, `extension-point`. No capability is named for service workers.

## Entries I couldn't tell, and what would settle each

- **80, 81, the breadcrumb events.** Each item is `{path, breadcrumb}`, the detail of the event by which a page chunk of ui-partners-portal-affiliate announces its own address and title. It is not a route object. The routes that render those chunks hold their paths in constants, which the structure holds with `path` null (items.jsonl positions 631, 632), so no other entry stands for them.
  - I placed them on the page they announce, the Affiliate Marketplace and its All Opportunities list. For 81 the scope is the rendering route's feature `temp-affiliate-marketplace` (held).
  - **`out` is the alternative, by SA-9's check** ('It is `out` only where none of them is'). If the coordinator rules so, both go `out`. `/affiliates/marketplace` keeps its lines through entry 21. `/affiliates/marketplace/opportunities-list` then has none in this structure.
- **38, `/influencer`:** an item of layout-mf's native mobile navigation (`mobileNavigationItems`, labels Home, Services, Influencer, Affiliate), not a route. No app of the registry serves `/influencer`, and no router declares it, so layout-mf's catch-all would send it to error-404. I placed it as a menu item, never `out` (rule 3), on the influencer pages' two cells. `out` (a link to no page) is the alternative.
- **68, Service Workers, CM-SFR-004.** CM-APP-005 (functions Salla hosts and runs) is the alternative, if the workers run on Salla's side rather than in the storefront. The partners docs' 'Learn more about Service Workers' page would settle it; it isn't in what I read.
- **66, the builder, CM-APP-002.** That ui-partners-portal-apps' `/builder` is partners-mf's 'App Details Builder' is a reading, by the two names and the blocks. The apps' locale isn't held in these records (SA-37's notes).
- **36 and 76, `/`:** on CM-PTN-001, the portal's root.
  - layout-mf's redirect sends a signed-out user to sign-in and each account to its home: the admin to dashboard-analytics, a `vip` account to 'vip-dashboard', an `agency` account to 'agency-list'.
  - The login app's own `/` only redirects to `/login`, and the registry serves `/` by layout-mf, so 76 follows 36 (rule 9). CM-PTN-002 (sign-in) is the alternative for 76.
- **37 and 77, `*`:**
  - layout-mf's catch-all (37) goes on CM-PTN-001, as SA-35 and SA-36 placed the portal's error pages;
  - the login app's (77) sends an address under its own addresses to `/login`, so CM-PTN-002.

  `out` is the alternative for both.
- **12 and 48, `/affiliate`, CM-PTN-009 alone.** The partner's products offered to marketers could also take CM-MKT-014, if its Affiliate Marketplace line is read to cover what partners list there. I kept the marketplace pages on both and the partner's own product pages on CM-PTN-009.
- **22, 56, Active Merchants:** the page failed to load in the sweep ('Something went wrong loading this page.', step 016). So what it lists is read from its title and its feature only. The same holds for Affiliate Orders (14, step 015).
- **41 to 44:** SA-36's reading, that Salla's affiliate products are its packages (CM-PTN-008), stands on affiliates-mf's locale, 'Promote Salla packages to new and existing merchants…'. The page's chunk (`r.e(138)`) isn't in what I read.

## Items against sources

The values agree with the bundles. Where an entry stands for more than one item, or an item isn't a route:
- **12:** its second item (line 609) is the mobile navigation's item for `/affiliate`, not a route. The entry is placed for its route.
- **61:** its other items (lines 1307, 1308, 1399, 1400) are a cookie library's defaults in other chunks of the app (`index-K-brZzzx.js`, `ui-reports-engine.es-CxdsX7vh.js`). The entry is placed for the root route.
- **55, 71:** both items are a cookie library's defaults (path /, sameSite strict): `out`, by SA-9's check.
- **80, 81:** breadcrumb events, not routes (above).
- **ui-partners-portal-affiliate** declares 18 routes, but 13 of them take their path from a constant the extractor didn't resolve (positions 631 to 633 and 635 to 644, `path` null). They have no entries, though they are the app's main pages: the marketplace, opportunities list, plans, my opportunities, orders, link stats, profile, affiliate products, create, store details, product, edit and details. Their places are held through layout-mf's same routes (13 to 28) and through 80 and 81.
- **Gates differ between routers for the same path:**
  - layout-mf gates `/affiliates/my-opportunities` by `affiliate-active-merchants`, while ui-partners-portal-affiliate's route carries no feature;
  - ui-partners-portal-affiliate gates the opportunities list by `temp-affiliate-marketplace`, which layout-mf doesn't name.
- **Paths served by no app:** `/influencer` (38) matches no pattern. `/agency/*` matches both services-mf's and partners-mf's patterns, as SA-34 and SA-35 found.

## For the second stage: what the sources state that no entry holds

- **CM-PTN-009, CM-MKT-014:** the marketplace's commission and discount figures per store ('Commission up to', 'Discount up to', with percentages such as '15%' and '10%', `…-sweep-partner-portal-en/steps/013.text.txt`, lines 60 to 105). These are stores' own values, so not qualities of the platform. The create form's commission types, 'Percent' and 'Fixed Price', with 'Add Discount Coupon' (routes-en step 056), are terms.
- **CM-PTN-009:** affiliates-mf's locale (@2098236) holds, under the key `affiliationTypeSubText`, a choice between “Public”, to display affiliates on the Marketplace, and “Private”, to send invitations by email to chosen individuals, a private affiliation by invitation. Its 'Get your products published. In the partner marketplace to increase sales and earnings' (`affiliateMarketplaceFooterDesc`) is the partner's own products. The partner's features `affiliates-gmv`, `affiliate-reports`, `affiliate-show-contacts` and `affiliates-stats-filter` (`portal-private-settings`, positions 30 to 32, 41) name parts of the programme with no route here, except `affiliates-gmv`, which gates the plans route (`${Xe}/plans`, constant path).
- **CM-SFR-004 or CM-APP-005:** the service workers' editor reads parameters from `/api/app/<id>/worker/parameters` (@822308). Their docs page would settle the capability.
- **CM-APP-002:** the builder's API, `/api/apps/<id>/builder/blocks` and `/blocks/init` (@137911), and partners-mf's 'Review App Details Builder', 'The current App details builder customization (if exists) will be submitted with this publication request.' (@1510962). The builder's customization is reviewed with the app's publication.
- **The portal's account types:** the root redirect names the types `vip` and `agency` (@1861581, the router's `/`). The held partner is of type `person`. This is a lead for VIP Partners and the agency pages.

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that already holds its support.
- **No `NOTE` on a first lead that holds nothing, and no quote found nowhere held.**
- **`NOTE` containers** (18 lines): `influencer/profile`, `agency/influencer-packages`, `agency/profiles`, `affiliate`, `affiliates`, `admin/affiliates`, `admin/affiliates/salla-products`, `influencer`, `coupons`, `apps/list`, `settings`, and the six roots `/` (36, 61, 76, 78, with 55 and 71 `out` holding no line).
  - Each is a page of its own, or a layout root whose children are one thing's pages. Each is placed on its thing's capability, as SA-34 to SA-37 placed the same paths.
  - Their children take the same capability, except where rule 12 gives an app's sub-page another: reports, builder, functions, service workers, snippets, store events.
  - None is `out`, except the two cookie objects 55 and 71, which aren't routes.
- **`NEW`:** none.

## Problems with the brief or the script

- **Child routes print no code.** For entries 62 to 70 and 79 (`parent:` a path or a position), `show --code 600` printed neither an items line nor code. I read them in their parent's array, as the brief's known case for a numeric `parent` says.
- **A page's breadcrumb event becomes an entry** (80, 81) while the route that renders the page doesn't, because its path is a constant the extractor didn't resolve. The coordinator may want the extractor to resolve ui-partners-portal-affiliate's constants (`Xe=B("s","/affiliates/marketplace")` and the others, which are plain strings in the same file), or to mark breadcrumb events.

The checker's last line, for SA-38: `81 of 81 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **`show` now finds a child route's items.** An entry under a parent renders as `…; parent: <its path>`, and `show` had read the parent into the path, so it printed nothing for entries 62 to 70 and 79. It also listed, under an entry with no parent, the items of entries that have one, as SA-14's notes found. `show` now keys each item by its app, path and parent's path, and every one of the 1,321 route entries finds its items (`method/held_entries.py`). The lines it had misled agree with the earlier batches', as the notes on SA-14 and here say, so none changes.
- **The breadcrumb events (80, 81) stand** on the Affiliate Marketplace's cells. A page that announces its own address and title is placed where its page goes, as SA-7's rule 4 places breadcrumb labels with their routes. They are not SA-9's cookie objects.
- **13 of ui-partners-portal-affiliate's 18 routes have no entry:** the extractor left their paths, constants in the same file, unresolved. The sweep's affiliate pages (steps 013 and 020) are placed here, so their things are held. The rest is a lead for the second stage, not a capture: the bundle is held, and only the extractor's reading is short.
- **The other lines stand,** by SA-34's to SA-37's rules, with layout-mf's features as scope.
- **Cost:** 16.5 million tokens over 77 requests, about 204,000 an entry. No cell changes.
