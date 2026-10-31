# Held pass, Salla, batch SA-39: notes

86 entries (effort high), evidence at observed-sa@b0bd0b16:
- 1 to 40: the last entries of `portal-app-routes` (items.jsonl lines 848 to 1419): three page announcements of ui-partners-portal-domains v0.79.1 (1 to 3), 36 request objects of a search client in ui-partners-portal-affiliate (4 to 39) and a drawing path in ui-partners-portal-apps (40);
- 41 to 56: all 16 entries of `portal-apps`, the portal's registry (`structures/salla/portal-apps/prod/items.jsonl`, positions 0 to 15);
- 57 to 86: the first 30 of `portal-help-center-article` (`partner@en`): the 23 articles of General questions (57 to 79), the category Apps Publishing and its one article (80, 81), and the categories Access Token, Webhooks, Shipping Apps, Influencers Service Information and Influencers Services Listing (82 to 86).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-39`).

**Placed:** 42 entries on capabilities only, 4 on capabilities and a new thing (41, 56, 58, 71), 1 on a new thing only (75), 39 `out` (4 to 40, 45, 48), in 106 lines: 96 on capabilities, 6 new, 4 `out` (the 36 search-client entries are one grouped line). 20 entries take more than one line. Supports, by line: 44 `core`, 35 `extension-point`, 27 `shows` on capabilities (a line of two values counted in each); 3 `core` and 3 `shows` on new lines. No `own-service` or `outside`, no filler. Five qualities, on four entries: 60 (registration, and app administration, free: two lines), 62 (at most 10 demo stores), 67 (payouts after the financial cycle), 74 (an app is rated 14 days after install).

**Sources read:** the brief and what it names; SA-34's to SA-38's notes with each coordinator's check, and SA-44's check and the rulings' last section (both changed during the batch: a partner's feature takes the support of the page it gates, and the account's answer of 28 October governs for `temp-services-redesign` and `temp-influencer-redesign`); the evidence map (it also changed: its line on `portal-private-settings`); observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for the three structures, `index/ledger-summary.tsv`, `index/ledger/portal-app.tsv`; the selection rows and `show --meta`. Then, to clarify only:
- **the domains app:** its index `raw/runs/20261008T134248Z-portal-bundles-chunks1/fetch.warc.gz@422550` (its router and its guards, once) and its English locale `raw/runs/20261008T134315Z-portal-bundles-chunks2/fetch.warc.gz@1775997`, which is held (SA-37 had found no locale of this app);
- **the registry's apps no route entry stands for:** @portal/utils (`raw/runs/20261008T134145Z-portal-bundles/fetch.warc.gz@2468579`), @portal/utils-api (@2432005) and ui-partners-portal-container (@989889), with the portal's importmap (`structures/salla/portal-importmap/prod/source.json`) for their files;
- **the routes' placements:** every `portal-app-routes` entry's lines in SA-34 to SA-38, matched to the registry's 16 patterns (each path with its parameters replaced by a number), so that each app's lines name the capabilities its routes were placed on;
- **the partner's features of 28 October** (`raw/runs/20261028T160451Z-journey-portal-demo-store-new-en/responses/0006.json`): it holds the two redesign features and still lacks `domain-purchase`, `temp-payments-billing`, `temp-unified-reviews-page` and `temp-home-page`;
- **the FAQ's own source**, `structures/salla/portal-help-center-article/partner@en/source.json`, for entry 66 (below), and the concern map's citations of the same FAQ (`studies/concern-map/platforms/salla/citations.tsv`, SA-S-5107, 5108, 5110, 5111, 5113, 5131, 5137).

## portal-app-routes, 1 to 40: the structure is placed whole

- **1 to 3, the domains app's page announcements.** Each item is `{path, breadcrumb}`, the address and title a page of ui-partners-portal-domains announces (`/domains`, `/domains/assignment/new`, `/domains/assignment`), not a route object. The app's own routes take their path from a constant (`U=q("b","/domains")`, items.jsonl positions 719 to 734, `path` null), so they have no entries. By the coordinator's check of SA-38 (a page that announces its own address is placed where its page goes), each goes on SA-37's line for the same path: CM-SFR-008, `shows`, scope `domain-purchase`, as the coordinator kept for the serving app's own routes. The domains app's own router wraps its pages in no guard; the scope is layout-mf's gate for the same paths, which the partner lacks on 8 and on 28 October.
- **4 to 39, a search service's API client** (its code names 'algoliaAgents', an appId and an apiKey; `/1/indexes/*/queries`, `/2/abtests`, `/1/keys` and the rest), bundled twice in ui-partners-portal-affiliate's chunk @18637 of `20261008T134525Z-portal-bundles-chunks3`. They are the vendor's API, not the portal's addresses, which the register already says. `out` by SA-9's check, in one line.
- **40, a VML drawing path** (`m@4@5l@4@11@9@11@9@5xe`) in a document library bundled with ui-partners-portal-apps: `out`.

`portal-app-routes` is now placed whole (SA-34 to SA-39).

## portal-apps, 41 to 56: rules my lines follow

1. **Each app goes on the capabilities its routes were placed on.** An app of the registry is a micro-frontend that serves a pattern of addresses. The entry names those addresses, so every capability of the pages served there takes a line (rule 2), on the support SA-34 to SA-38 gave the routes. Where an app's routes on one capability carry two supports (the partner's side `extension-point`, the admin's `core`), the line carries both.
2. **No scope.** The registry states no gate: a route's feature is its own line's scope, and the app's line names it in `reading` only. The line's support follows the routes' lines, so where every route is behind a gate the partner lacks (payments, widgets, domains), the app's line is `shows`.
3. **The redesign features of 28 October** (the coordinator's check of SA-44): ui-partners-portal-services' routes behind `temp-services-redesign` and `temp-influencer-redesign` are `extension-point`, and so are its lines.
4. **Paths the admin's own team uses only** (`/admin/dashboard`, `/admin/admins`, `/admin/permissions`, `/admin/roles`) give partners-mf no line, as SA-34 placed them `out`.
5. **An app with no page** is `out`: @portal/utils (45) and @portal/utils-api (48) carry the pattern `/^(/integration.*|/)$/`, but their files are shared code. partners-utils.js exports the session, the permissions, the shared context and HTTP clients with its own bootstrap and unmount; partners-api.js holds the base addresses of Salla's services. No route of the portal is at `/integration`, and `/` is layout-mf's root. The brief's nearest `out` kind is the software's own bookkeeping; CM-PTN-001, as the portal's root, is the alternative.
6. **ui-partners-portal-container (51),** at `/new-design`, mounts two pages, 'Overview' and 'Apps' (permission 'apps.read'), and names itself 'New design — Overview'. No run reached it. I placed it `shows` on CM-PTN-001 and on CM-APP-002, as a new design shown but not shown offered. `core`, as the portal's own place, is the alternative.

The lines, by app:
- **partners-mf (41):** 20 capability lines (CM-PTN-001 to -004, CM-APP-002, -003, -006, -009, -010, CM-SFR-003, -004, -005, -008, CM-SHP-015, CM-DVT-004, -005, CM-STF-005, CM-API-008, CM-MKT-015, CM-PTN-009) and the new things VIP Partners and Transfer Requests.
- **services-mf (42):** CM-PTN-005, CM-MKT-015, CM-PTN-009, `core;extension-point`.
- **layout-mf (43):** CM-PTN-001 `core`, for `/` and `/conversations` (Chats).
- **affiliates-mf (44):** CM-PTN-009 and CM-MKT-014 `core;extension-point`, CM-PTN-008 `core`.
- **ui-partners-portal-apps (46):** CM-APP-002, CM-ANL-006, CM-SFR-004, CM-APP-005, CM-APP-006, CM-SHP-015, CM-SHP-011 `extension-point`; CM-API-008 `core`. The onboarding step (`app.onboarding.step.creating`) has no route entry of this app; its line rests on the pattern's words, as SA-35 and SA-37 placed onboarding steps.
- **ui-partners-portal-affiliate (47):** CM-PTN-009 and CM-MKT-014 `extension-point`, CM-APP-003 `core` (coupons).
- **ui-partners-portal-domains (49):** CM-SFR-008 and CM-SFR-009 `shows`.
- **ui-partners-portal-services (50):** CM-PTN-005, CM-MKT-015, CM-PTN-009 `extension-point`.
- **ui-partners-portal-payments (52):** CM-PTN-003, CM-PTN-004 `shows` (`temp-payments-billing`).
- **ui-partners-portal-widgets (53):** CM-PTN-001 `shows` (`/dashboards`, `temp-home-page`), CM-PTN-005 `shows` (`/reviews`, `temp-unified-reviews-page`).
- **ui-partners-portal-settings (54):** CM-PTN-002 `core`. **-stores (55):** CM-DVT-005 `extension-point`. **-login (56):** CM-PTN-002, CM-TRU-001, CM-DVT-002 `core`, and Ideas `shows`.

## portal-help-center-article: no batch had placed it; rules for SA-40 and SA-41

**SA-40 and SA-41 hold the rest of `portal-help-center-article` and haven't run.** The coordinator aligns them with these rules, which my lines follow:
1. **An article is its question and its answer.** The structure holds both (`title`, `content`, in English and Arabic); I read them as one FAQ entry, by what its words say the platform does (the brief's rule 4 on a FAQ):
   - `core` where the answer states the platform's own place, rule or built-in feature (the App Store's ratings, its suspension of apps, the pricing options, the payout schedule, ID verification);
   - `extension-point` where it states developers doing the thing through what the platform provides (building and publishing apps, listing one with a video);
   - `shows` where it gives only a term (who sets the price, the developer's duty of support, a condition of publishing), a guide (the icons' standards, how to speed up publishing) or a topic.
2. **Every thing the answer names takes a line,** on its own capability. A thing no capability holds is `new` (App statistics).
3. **A category is a container** (rule 3, M-13): it goes on the capability its title names, `shows`, since a help centre's category names a topic (rule 4). It takes no line for the Help Center itself, which is only the group it sits under. The influencers' categories take both CM-MKT-015 and CM-PTN-009, as SA-34 and SA-38 placed the influencer pages.
4. **The partners' side keeps the portal's lines:** an app's page in the portal is CM-APP-002 `extension-point`, as SA-35 and SA-37 placed My Apps; the App Store's own rules are CM-APP-002 `core`.
5. **Homonyms:** an app's rating by merchants is the App Store's (CM-APP-002), not buyers' reviews (CM-SUP-001, CM-SUP-002); complaints about an app are not a store's customers' complaints (CM-SUP-008); an app's ownership transfer is not inventory transfers (CM-INV-006); a partner that is an individual or a company is the partner account's eligibility (CM-PTN-002), not a store's business entity (CM-ACC-004).
6. **Terms and quotes** are the article's own words, in both languages; a quote names the structure's file. Links (salla.dev's blog, t.ly, bit.ly, docs.salla.dev) aren't held, so they clarify nothing.

**Seven categories have no entry:** General questions (its 23 articles are 57 to 79), Apps Testing, Twilight Themes Engine, Services Support, Influencers, Influencers Basic Information and Ready Stores. Only six of the 13 were given entries (80, 82 to 86), though the coordinator's message speaks of the build giving the categories entries of their own (SA-20's check). Whether the others were dropped by the selection's 'the items not cited', or by the nested rule, I didn't trace. If they are meant to have entries, General questions is the FAQ's own catch-all (a title naming only a grouping, `out` by the ruling after SA-28), and the others go on their topics' capabilities.

## New things

1. **App statistics** (إحصائيات التطبيق), entries 58 and 71, `shows`.
   - What the entries state: the portal lets a developer 'follow up on app revenue, downloads, and more' (58), and 'You can follow the application statistics through the application’s dashboard on the portal.' (71).
   - Place of its own: none held. It is a part of an app's page in the portal, which SA-37 placed on CM-APP-002.
   - Proposed: domain F, area APP or PTN, parent CM-APP-002 or CM-PTN-001.
   - Searched: app statistics; app installs; downloads; app analytics; installs; install count; statistics; app dashboard; app insights; partner analytics; app performance; إحصائيات; إحصائيات التطبيق; تحميل. The hits (CM-ANL-001 and CM-ANL-002, a store's reports; CM-ANL-006, an app's reports in a store's dashboard; CM-APP-001, a store's installed apps; CM-APP-004, an app's lifecycle events, which 71's link names) aren't this thing. CM-APP-002, as the App Store's statistics for a developer, is the alternative to a new thing.
2. **VIP Partners** (41) and **Transfer Requests** (41, 75): SA-34's, by the same names. 75 is the FAQ's 'App ownership transfer feature in the [Partners Portal]', the partner's side of the same transfer.
3. **Ideas** (56): SA-35's, by the same name.

## Entries I couldn't tell, and what would settle each

- **66: the article's answer isn't its question's.** The title asks whether an app can be updated after it is published; the answer, in both languages, is the Pay-As-You-Go text that 76 and 77 hold too. `source.json` holds it so (article 576261038). I gave the title CM-APP-002 `shows` (a topic) and the answer CM-APP-003 `core`. The platform's own page, `/help/faq`, would show whether the portal renders it so.
- **64, 68, 78's second line: `shows` or `core`.** Who sets an app's price, the developer's duty to support its app, and a verified ID before publishing are terms the platform sets. I placed them `shows` (they give the terms). `core` on CM-APP-002 and CM-APP-003 is the alternative, reading the platform's rule as its own feature.
- **61, the API (CM-API-001 `core`).** 'the main and only interaction is going to be through APIs' could read as apps doing the work through the API, `extension-point`. I kept the brief's rule 4: the platform's own API, a guide addressed to developers.
- **76, 77, Pay-As-You-Go, CM-APP-003 `core`.** The answers say merchants pay only for the features they use; whether the platform bills it or the developer sets it isn't stated beyond the link (not held). `shows` is the alternative.
- **70, CM-APP-002 `core`.** The suspension of an app for complaints could also be CM-TRU-009's (acceptable use and enforcement), whose reading leaves the app suspension (SA-S-0028) to CM-APP-002. I followed that.
- **45, 48 `out`, 51 `shows`:** rules 5 and 6 above.
- **1 to 3:** the scope `domain-purchase` is layout-mf's gate, not stated by the domains app's own code; I kept the coordinator's line. With no gate of its own, the domains app's page might read with no scope.

## Items against sources

- **1 to 3:** the items are page announcements, not routes; the domains app's 15 routes have no entries (path constants unresolved), as SA-38 found for ui-partners-portal-affiliate.
- **4 to 39:** each entry stands for two items, the same client bundled twice in one record.
- **portal-apps:** the items agree with `source.json`. The partners-mf pattern's prefixes without an end anchor (`\/dashboard`, `\/coupon`) also match `/dashboards` and `/coupons`, which the registry serves by widgets and the affiliate app as well (SA-36, SA-37); I gave those paths to the apps that declare them.
- **portal-help-center-article:** article ids repeat category ids (General questions' first article is 1617628556, the category's own id; the demo stores article is 1984760154, Shipping Apps' id), so the concern map's citation SA-S-5108, 'line 1 (article 1984760154)', names the demo stores article, not the category. Salla's numbers recur across lists (observed-sa's `docs/READING.md`).

## For the second stage: what the sources state that no entry holds

- **CM-SFR-008:** the domains locale (@1775997): 'Domain assignment request', 'Complete the information below to request the assignment of a .sa or .السعودية domain.', the acknowledgment that a request grants no right before the current administrative coordinator approves it; restoring a deleted domain for a fee, and 'This domain was deleted within five days of being registered, so the deletion is permanent and it cannot be restored.' Qualities and a scope lead (Saudi domains).
- **CM-PTN-001:** ui-partners-portal-container's 'New design', a redesign of the portal with Overview and Apps (@989889).
- **@portal/utils-api's base addresses** (@2432005): `api.salla.dev/partners/v1`, `/experts/v1/`, `/marketing/v1/`, `/marketplace/v2`, `/partner-reports/v1/`: the services behind the portal, a lead for the partner API's groups.
- **The FAQ's links** (salla.dev's blog posts on the portal and on creating an app, the Pay-As-You-Go article at t.ly, the docs' App Events) aren't held; `held_index.py` finds none.

## The checker's lines, read again

- **`CHANGES` CM-APP-006@salla gains `extension-point`** (lines 13 and 42: partners-mf's and ui-partners-portal-apps' onboarding steps) and **CM-APP-009@salla gains `extension-point` and becomes held** (line 14: partners-mf's private access). These are SA-35's changes, which the coordinator's check accepted; the cells aren't amended yet. Kept.
- **`NOTE` core on a product named with the platform's brand** (lines 66, 76, 78, 79, 91, 94): 'Salla Partner Portal', 'Salla APIs', 'Salla App Store', 'Salla Apps'. Each names Salla's own portal, API, App Store or the apps on it, which the cells already hold as the platform's own (`core`); no line rests on a maker.
- **`NOTE` containers:** `/domains` (line 2), placed on its capability as SA-37's; the search client's paths (line 5), not routes, `out`.
- **`NOTE` first lead holds nothing:** CM-API-007 (by 'batch') and CM-OPS-004 (by 'status') on the search client's paths: words of a vendor's API, no lead.
- **`NOTE` new thing whose entry has leads:**
  - 41: CM-ACC-003 (by store-management, the partner's access requests, CM-STF-005's), CM-DVT-003 and CM-DVT-004 (demo stores: CM-DVT-004 holds its line; CM-DVT-003's cell places the same Ready Stores link as CM-DVT-005, the model's difference SA-34 noted), CM-SHP-015 (its line), CM-PTN-010 (by name: no API shown);
  - 56: CM-CUS-010 (a buyer's sign-in), CM-MKT-007 and CM-NTF-004 (by email), CM-PAY-003 (a payment service's verification), CM-TRU-021: none is the thing;
  - 58: CM-PTN-001 (its line), CM-ACC-004 (a homonym, rule 5 above), CM-ACC-006, CM-DVT-003, CM-DVT-004 (by words);
  - 71: CM-ACC-006, CM-API-003 (by 'read', from 'Read more'), CM-PAY-003, CM-SHP-014: no lead;
  - 75: CM-INV-006, a homonym; CM-PTN-001 and CM-DVT-001 by words.
- **`NEW`:** App statistics, 2 lines; Ideas, 1; Transfer Requests, 2; VIP Partners, 1.
- No quote printed 'found nowhere held'.

## Problems with the brief or the script

- **The rulings and the evidence map changed during the batch** (SA-44's check: the features of 28 October; a partner's feature takes its page's support). My lines follow the new text.
- **A registry entry gives many lines.** partners-mf's one entry takes 22. The brief's rule 2 asks a line for every thing an entry names, and the coordinator's message to keep each app on its routes' capabilities; a coordinator's rule for a registry (one line per app, on the portal) would shorten it.
- **The checker reads a term inside a regular expression's text,** so a path with `/` isn't found where the registry escapes it (`\/`). I wrote the paths' segments as terms.
- **Seven of the FAQ's 13 categories have no entry** (above).

The checker's last line, for SA-39: `86 of 86 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **Seven of the FAQ's 13 categories have no entry by design.** The concern map already cites them: `held-vs-read.tsv` gives the structure 13 items, 7 of them cited. The held pass lists only what the model hasn't read. Their articles are entries, as each article is an item of its own (132 entries in all), and SA-40 and SA-41 place them.
- **`portal-app-routes` is placed whole** (1,193 entries over SA-34 to SA-39). The domains app's pages announcing themselves are placed where SA-37 put their paths. The search service's client and the drawing path are `out`.
- **The registry's lines stand,** by the ruling after SA-39: from the next registry on, one line an app. The services app's lines are `extension-point`, after SA-44's check.
- **Entry 66's mismatched answer** is placed as the source holds it: the question on CM-APP-002 `shows`, the answer, Pay-As-You-Go, on CM-APP-003 `core`.
- **The article rules stand for SA-40 and SA-41:** an article's question and answer are read together by what they say the platform does.
- **New things:** App statistics (58, 71), with the others already named.
- **Cost:** 17.5 million tokens over 84 requests, about 203,000 an entry. No cell changes beyond SA-35's.
