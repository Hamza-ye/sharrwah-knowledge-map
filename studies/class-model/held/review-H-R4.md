# Review of the held pass's dry run, part R4: ZD-1, lines 2 to 62

**What this is.** Part R4 of the review (`briefs/H-review.md` at `f0dd52bd`). It covers ZD-1's first 61 placement lines: the first 58 entries of Zid's `dashboard-page-index`, from Analytics to URL redirects. It also tests the evidence map's reading of the 18 pages the page index drops. The rows are in `review-H-R4.tsv`, one per verdict.

**What was read, pinned:**
- ZD-1's placements and notes at `33946dbc`;
- `briefs/H-held.md` and `held/selection.tsv` at `dc1e6414`;
- the model at `13205959`, through `land_points.py cell`, `class_slice.py caps --terms` and `key`, and `merged/capabilities.tsv`;
- other-product-class at `0d79b794f`:
  - `README.md`, then `zid/README.md` and `zid/GAPS.md`;
  - `zid/structures/REGISTER.tsv`;
  - the structure's `meta.json`, `items.jsonl` and `source.js` (its sha256 matches `meta.json`);
  - `zid/index/ledger/dashboard-routes.tsv`;
  - the run steps the readings cite;
  - `zid/structures/dashboard-locales/items.jsonl`, by `grep`;
  - the extractor `capture/structure_zid_dashboard_page_index.py`, read only for why pages are dropped.

**Abbreviations, as in ZD-1's notes.**
- `source.js` is `zid/structures/dashboard-page-index/source.js`.
- `rest-en#N` is `zid/raw/runs/20261028T160128Z-dashboard-routes-rest-en/steps/NNN.text.txt`. Likewise:
  - `gaps-en` is run `20261028T150740Z-settings-gaps-en`;
  - `en-2` is run `20261028T145901Z-dashboard-routes-en-2`;
  - `api-en` is run `20261028T155108Z-markets-api-en`.

Every quote a reading in my lines cites was found at the step it names, and each step's URL is the entry's route.

## Counts

| | Rows | Lines |
| --- | --- | --- |
| Rows | 65 | 61 |
| `stands` | 41 | 41 lines stand whole |
| `missing scope` | 16 | 16 |
| `missing line` | 3 | 3 (13, 14, 18) |
| `wrong supports` | 2 | 2 (13, 14) |
| `wrong reading` | 2 | 2 (3, 5) |
| `can't tell` | 1 | 1 (42) |
| Misses | 24 | 20 |

**The misses by cause and effect:**

| Cause | `column` | `kind` | Rows | Lines |
| --- | --- | --- | --- | --- |
| `brief` | 19 | 1 | 20 | 5, 7, 12, 13, 14, 17 to 26 (18 twice), 42, 49, 50, 54 |
| `care` | 3 | 0 | 3 | 3; 13 and 14 (`missing line` CM-APP-007) |
| `evidence` | 1 | 0 | 1 | 42 |

- **No `held`, `count`, `capability` or `filler` effect.** The one `kind` is line 13: CM-MKT-010's Zid cell holds nothing, and the line alone would make it held by `extension-point`, where `shows` is what its statement supports.
- **Six standing lines each make a Zid cell held that held nothing:**
  - 6, CM-ANL-004;
  - 13, CM-MKT-010;
  - 17, CM-SEL-005;
  - 39, CM-CHN-004;
  - 40, CM-AIA-005;
  - 41, CM-SUP-006.

  They stand on test. Line 40 is the one with the closest alternative, CM-CNT-007.
- **Seven standing lines fill a gap a cell's reading names.** Each cell's reading has to change when `held_amend.py` writes it:
  - CM-CAT-005, line 16: "no statement defines a product brand";
  - CM-SFR-006, line 29: where the landing page is made;
  - CM-CNT-003, line 35: where the pages are made;
  - CM-INV-002, line 23: what the logs record;
  - CM-SFR-013, line 24: where the filters are set;
  - CM-MKS-008, line 46: the page as a languages setting;
  - CM-APP-007, the missing lines 13 and 14: "No Zid statement found names the dashboard's route for an app".

**The leads** (`show --candidates` now): the right cap_id is among an entry's leads on 37 of the 61 lines, and on 39 of the 65 rows (the three `missing line` rows: one yes, two no). Where it isn't, the entry had either no leads at all (lines 13, 16, 26, 43, 50, 51) or only the parent or a homonym. For example, CM-ANL-001 alone for Live analytics; CM-SFR-001 alone for every Online store child; CM-CNT-003 for the SEO "Store pages".

## The cases

### The containers (lines 2, 18, 27, 32, 36, 43)

- **The ruling, within B-extent.** A container is an admin section by "What a place of its own is": a sidebar group the page index names with its own title. "A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence." So a container goes on the capability whose thing its group is, as the cells' readings show:
  - **Analytics (line 2) on CM-ANL-001.** Its Zid cell reads "its section التحليلات" (ZD-S-0971) as `core`.
  - **Online store (27) on CM-SFR-001,** the role of Shopify's Online Store.
  - **Settings (43) on CM-ACC-006.** Its general group `settings.general` claims the same path (`alternativePaths:[settings]`, title "General", source.js). CM-ACC-006 is the capability of "General" and of Salla's "Settings".
  - **Blog (32) and SEO (36),** the same way.

  None of these is `out`, since each names a place, and none is `new`, since a capability holds each one's thing.
- **A container with a page of its own takes two lines.** Inventory (line 18) is the page `catalog.inventories`:
  - its own page is the inventory addresses (permission `locationsView`, source.js; gaps-en#34): CM-INV-005, as placed;
  - its children are CM-INV-001's and its children's.

  The batch placed it only on its own page's capability, so the row is `missing line: CM-INV-001 core`.
- **Not settled by B-extent:** a container whose group no capability holds. None is in my lines. It is a method ruling.

### The pages with a release badge (lines 4, 5, 14, 16, 49)

- **The badge `new` marks a page as released,** so `core` stands. The badge goes in `reading`, as H-held.md rule 4 has a help page's release marker go.
- **Lines 4, 16 and 49 have it in their readings. Lines 5 (Zid Insights) and 14 (Zid Voice) don't,** and their rows say so.
- **`hasPulseDot`** (Analytics, Marketing, WhatsApp) is a sidebar dot, not a release marker.
- **A `beta` badge** is the case of a page not released (entry 86, R5a's). H-held.md's flag rule makes "a beta" `shows`, but B-extent doesn't name badges, so it is a method ruling.

### The pages listed only under a store condition (lines 7, 12, 13, 14, 17 to 26, 33, 34, 42, 49, 50, 54)

**What source.js states.** Each condition is a spread, and I matched its brackets to know which pages it covers:
- **`...t?[]:[...]`:** the catalog's preorder campaigns, inventory pages, stock changes, filters, custom fields and options (lines 17 to 26), inventory reports (7) and logistics analytics (12). The `t` that hides them also turns the dashboard's titles to Donations, Donation opportunities and Donors (dashboard-locales `navbar:donations`, `navbar:donationOpportunities`, `navbar:donors`). That `t` marks a charity store is a reading.
- **`showNewZones`:** the online store's Settings (42).
- **`hasNewGifting`:** Gifting settings when set (49), Gift options when not (50).
- **`mustUseMarketsPricing`:** Markets (54).
- **`le()`,** which the module doesn't name: Zid Ads (13).
- **The blog's `is_enabled`:** blog categories and tags (33, 34).
- **An installed application that `oe` matches:** Zid Voice (14).

**The ruling.**
- **H-held.md rule 1 makes the source govern.** B-extent gives a released flag "its plan or store as its scope", and a statement's scope "stays its own".
- **A condition the platform sets for a store** (a store flag, or a kind of store) is the entry's scope, in the source's identifier. That covers lines 7, 12, 17 to 26, 42, 49, 50 and 54: 16 `missing scope` rows, cause `brief`, effect `column`.
- **A condition on the store's own data** (the blog the merchant turns on, an app installed) is one store's data by H-held.md's out list. It goes in `reading`, not scope. So lines 33 and 34 stand.
- **B-extent doesn't name listing conditions,** so the rule is a method ruling for the coordinator.
- **The batch recorded none in scope.** It put the condition in `reading` for 17, 42, 49, 50 and 54 and left it out of 7, 12 and 18 to 26. Its notes' list of readings that depend on conditions ("47/48, 51, 72, 81, 88/89, 97, 41") misses these.

### Zid Ads and Zid Voice (lines 13 and 14)

**What source.js states.**
- **Zid Ads.** The dashboard takes application 2812 out of its apps lists. It lists that application's embedded page `apps/2812/embedded` in its own Marketing group, after Affiliates, under its own string `navbar:zidAds` ("Zid Ads" / "إعلانات زد"), and only when `le()` holds.
- **Zid Voice.** It takes the installed application that `oe({appId})` matches out of the installed apps. It lists that application's page `apps/${o.id}/embedded` under Orders, after Abandoned carts, with the badge `new`.
- **Neither page object carries a permission.**

**Weighing every value B-extent allows:**
- **`own-service`:** no statement names Zid's company as either one's maker. A product's name that carries the brand names none.
- **`extension-point`:** B-extent's definition needs "the statement shows third parties doing it through something the platform provides", and no third party is shown. The convention on an app's page needs a route "gated only by the apps permission", and no gate is shown.
- **`core`:** the platform's own place, as CM-MKT-022's Zid cell reads Zid Voice's product line (ZD-S-0452, placed by what it shows, the maker a gap). But an embedded application's page doesn't show who does the advertising or the calling.
- **`shows`:** what the statements support.

**The ruling: `shows`,** with the missing maker statement a gap.
- An App Market listing of app 2812 or of Zid Voice naming its developer would settle it, and so would the route's gate.
- It is a method ruling: B-extent doesn't settle a page the platform's own navigation lists under its brand at an app's address.
- H-held.md rule 4 lists "an app's page" under `extension-point` without B-extent's clause, so the cause is `brief`.
- Both entries are also the dashboard's embedded app pages: CM-APP-007's thing ("Embedded app page"), `core` as the dashboard's own route for an app's page. The batch placed neither there (`care`; the leads didn't offer it).

### Readings that rest on a file beyond the entry's item and its source

- **Run steps** (`page text`): 45 of the 61 lines cite them: lines 4 to 8, 10 to 12, 15 to 21, 23, 24, 26, 28, 30, 36 to 53 and 55 to 61.
- **The ledger:** 3 and 25 cite only it ("not opened").
- **The model's cells:** many readings cite a cell's term.
- **The locales:** no reading in my lines rests on them.

**Whether H-held.md allows them.**
- Rule 1 names only the item and its source. H-held.md's reading list names `index/` "by their rows", and the ledger joins each route to its steps.
- So the brief reads two ways. The batch took run steps as allowed for reading, never as entries.
- Some placements would be `can't tell` from the entry and source.js alone:
  - 5, Zid Insights;
  - 40, llms.txt against SEO;
  - 52 and 53, the split of orders and products;
  - 60, API integrations.
- The rest are settled by the title and source.js.

The run steps hold things no entry does. If the coordinator lets their text be a statement (a method ruling: B-extent's statements are the concern map's and the held entries, and a run step is neither):
- `gaps-en#9`'s toggles would hold three Zid cells that hold nothing:
  - CM-INV-004 (the low stock label and notifications);
  - CM-MKT-023 (similar products on each product page);
  - CM-ORD-014 (the reorder feature).
- `rest-en#91`'s Snapchat, TikTok, Google, Meta, X and OpenAI would be CM-CHN-004's slot fillers, as its WooCommerce cell takes Google Merchant Center.
- `rest-en#163`'s "Free for 3 months" would be a quality.

## What the batch never placed

### The 18 pages the page index drops: the evidence map's reading tested

**Source and items.** `source.js` holds 137 `pageKey` objects and `items.jsonl` 119; the 18 are the ones ZD-1's notes list.

**Why they are dropped.** The extractor's pattern (`capture/structure_zid_dashboard_page_index.py`, line 24) is `` pageKey:`…`,path:`([^`]+)`,title:<fn>(`…` ``. It needs:
- a non-empty literal path, so `dashboard`, whose path is empty, is dropped;
- a title right after the path, so `settings.general`, with `alternativePaths` between them, is dropped;
- a literal title, so the conditional `t?…ngoTitle:…` titles are dropped.

The build left them out, not the agent, the brief or the selection.

**Each has a route, held as an entry of ZD-2 or ZD-3** (found with `show --batch`):

| Page | Route | Entry, batch |
| --- | --- | --- |
| `dashboard` (path empty) | `$lang.stores.$storeId._index` | ZD-E-3151f141, ZD-3 |
| `orders`, `orders.all` | `orders._index` | ZD-E-bea90466, ZD-3 |
| `orders.manual` | `orders.drafts` | ZD-E-61eef07c, ZD-3 |
| `catalog`, `catalog.products` | `catalog.products` | ZD-E-3856594e, ZD-3 |
| `customers`, `customers.all` | `customers._index` | ZD-E-1d93b7d0, ZD-3 |
| `customers.groups` | `customers.groups` | ZD-E-0d89705e, ZD-3 |
| `analytics.sales-reports` | `analytics.reports.sales` | ZD-E-8ed14cad, ZD-3 |
| `analytics.customer-reports` | `analytics.reports.customers` | ZD-E-93d093bf, ZD-3 |
| `analytics.products` | `analytics.products` | ZD-E-93823a61, ZD-3 |
| `settings.general` | `settings.account`; its alternative path `settings._index` | ZD-E-4b448e1a, ZD-E-5155bc0d, ZD-3 |
| `channels.marketplaces` (path computed) | `channels.marketplaces.connect.marketplaces` or `.connect.get-started`; its alternative path `channels/marketplaces` is no route | ZD-E-125a113f, ZD-E-6aac8235, ZD-2 |
| `apps.${e.id}` (path computed) | `apps.$id` or `apps.$id_.embedded` | ZD-E-a99ac50c, ZD-E-30067ca7, ZD-3 |
| `apps.categories` and its two computed levels | `apps.browse`; the categories themselves come from an answer (`categories.apps_by_category`), not from source.js | ZD-E-5d6fc404, ZD-3 |

**The verdict: the reading holds for the routes and for "no request goes out", not for "the model loses nothing".** A route entry holds only its id, parent, path and index. Two things are lost:
1. **The pages' own titles,** in English and Arabic, the platform's terms for them. Examples:
   - "Manual orders" / "الطلبات اليدوية" (route `drafts`);
   - "Customer groups";
   - "Sales reports";
   - "General";
   - "Marketplaces" / "منصات البيع";
   - "Dashboard" / "لوحة التحكم".

   This is `column` in effect, unless a route's batch needs the title to place it.
2. **The charity-store titles, which no kept item and no route holds.** They are in source.js and resolved in dashboard-locales:
   - Donations / التبرعات;
   - All donations;
   - Manual donations / التبرعات اليدوية;
   - Donation opportunities / فرص التبرع;
   - Donors / المتبرعون;
   - Donors groups;
   - Donation reports;
   - Donors reports.

   Read as a statement, they show a store mode whose orders are donations and whose products are donation opportunities (a reading). They would make CM-SEL-007's Zid cell (Donations; none-held) held, so a cell changes.

   Remedy, with no request: the extractor keeps both titles of a conditional title, or the held pass reads them from source.js. The evidence map's line should say so.

The App Market categories in the sidebar aren't lost to the model: the concern map's cells already cite Zid's App Market categories (for example ZD-I-0454 and ZD-I-0463).

### What source.js states of the kept pages that no item holds

- **Each page's permission.** Changes no cell's placements; the staff permissions come from `store-permissions` (ZD-4).
- **Its sidebar badge and `newTitle`.** Reading only.
- **Its listing condition.** Scope, above; and the charity mode, item 2 of the list above.
- **`alternativePaths`.** `settings.general` and `settings`, line 43.
- **Zid Ads' application id 2812 and its condition `le()`.**
- **Zid Voice's match `oe`.**
- **The list of 41 store ids behind the Qitaf condition** (R5a's lines).

Of these, only the conditions bear on a cell, and only as scope, except the charity mode.

## The notes' claims, for my lines

| Claim | Verdict | Why |
| --- | --- | --- |
| Entries 12 and 13 are `extension-point`, "apps' embedded pages"; no `own-service` | partly wrong | `shows` on CM-MKT-010 and CM-MKT-022 (above); no `own-service` is right; both are also CM-APP-007's |
| 4, Zid Insights: CM-ANL-001, or CM-ANL-005, CM-AIA-001 or new; billing apart would settle it | CM-ANL-001 stands | CM-ANL-005 is undefined (its cell: a link only); the page never says AI; CM-ANL-001 holds the thing. The page already shows a separate activation ("Start free trial", "Activate directly", "Cancel at any time", rest-en#163 lines 44 to 115), so what is missing is a maker statement, a gap the reading should name |
| 2, All analytics: placed from its pageKey; a run opening /analytics would settle it | stands, with its reading corrected | the permission is all of five views, not every one (line 3's row) |
| 39, llms.txt: CM-AIA-005, CM-CNT-007 the alternative | CM-AIA-005 stands | the page's words are AI platforms answering customers, not search engines; the SEO grouping decides a parent, not a placement |
| 42 and the containers (1, 26, 42 in my lines): placed on what their children's thing makes them; `out` the alternative for 42 | stand | `out` fails H-held.md's list; CM-ACC-006 holds "General" and Salla's "Settings". Inventory (17) should have had the same treatment, a second line |
| 50, orders and products: CM-ORD-001 and CM-CAT-001, CM-ORD-010 the alternative | stand | CM-ORD-010 is whether or when orders are accepted; the page's toggles are settings of orders and products. The notes miss that CM-CHK-009's Zid cell cites the same page (ZD-S-0962, ZD-I-0138) as custom fields, which the page doesn't show. Zid's custom fields are `catalog/meta-fields` (line 25). A difference with the model for the coordinator |
| 56, API integrations: CM-APP-009, CM-API-002 the alternative | CM-APP-009 stands | its Zid cell reads the direct API connection (خدمة الربط المباشرة (APIs)) as `core`; a manager token isn't an app's OAuth authorization |
| Badges: kept `core`, the badge in reading | stands for `new` | lines 5 and 14 leave the badge out; `beta` is a method ruling (R5a) |
| Items and source disagree: 18 dropped, for the reasons given | right | verified in source.js and by the extractor's pattern; the conditions list misses the charity flag's catalog and analytics pages |
| Qualities seen on pages, left out: Zid Insights' 3-month trial, "4 out of 6" inventory addresses | right by rule 5 | both are on the pages (rest-en#163 lines 45 and 111; gaps-en#34 line 42), not in the entries |
| Product feed platforms: no filler for 38 | right by rule 5 | a filler if a run step's text becomes a statement (CM-CHN-004's WooCommerce cell takes Google Merchant Center) |
| Problems: what may be read; no container or badge rule; store-flag conditions and scope | each confirmed | fixes F1 to F6 below |

The notes name no new thing and no difference with a model cell in my lines. The differences I found are above: CM-CHK-009's reading of the orders and products page, and CM-APP-007's missing route.

## Fixes to H-held.md, and the checker test for each

Each stays within B-extent, except where it is named a method ruling.

- **F1, rule 1, what may be read.**
  - Text to paste: "To clarify an entry you may also read the run steps the platform's ledger joins to its route (`index/ledger/`), cited as `page text <run>#<step>`, and the model's cells. They clarify what the entry is; its scope, terms, filler and quality come from the entry and its source."
  - Whether a run step's text may itself be a statement is a method ruling (above).
  - Test: none needed.
- **F2, rule 4, `extension-point`.**
  - Replace its bullet with: "`extension-point`: the statement shows third parties doing it through something the platform provides: an app store's category, an extension target, a provider interface, or an app's page, a route named for an application and open only to the apps permission (B-extent's convention). An app's page that names no maker and shows no such gate supports `shows` on what the app does; the page itself is CM-APP-007's (Embedded app page)."
  - The `shows` part is a method ruling.
  - Tests:
    - print a NOTE for every `extension-point` line, as the checker does for `own-service`;
    - flag an entry whose text holds `/embedded` and that has no line on CM-APP-007.
  - These catch lines 13 and 14.
- **F3, rule 4, `own-service`.**
  - Add B-extent's clause: "Without a statement naming the company, place it by what its statements show, and say in `reading` that the maker statement is missing, a gap. A name carrying the platform's brand is such a case."
  - Test: a NOTE for a line whose entry's title holds the platform's brand (Zid, زد, Salla, سلة, Shopify, BigCommerce, Woo) and whose reading doesn't say "gap". This catches lines 5, 13 and 14.
- **F4, rule 4, `core`.**
  - Add B-extent's opening, "the platform itself does it for the merchant".
  - It bears here only on lines 13 and 14.
  - Test: none.
- **F5, rule 5, `scope`.**
  - Add: "Where the entry's source lists it only under a condition the platform sets for a store (a store flag such as `mustUseMarketsPricing`, or a kind of store such as a charity store), that condition is its scope, in the source's identifier. A condition on the store's own data (a setting the merchant turns on, an installed app) goes in `reading`."
  - A method ruling: B-extent gives a flag "its plan or store as its scope", but doesn't name listing conditions.
  - Test: the build has to carry the condition into the entry first. Either the extractor or `held_entries.py` adds a `condition` field from source.js's spreads. Then "an entry with a condition and an empty scope" catches the 16 rows.
- **F6, rule 3, containers.**
  - Add: "A container, an entry whose children are other entries of its structure, is placed on the capability whose thing its group is, as the cells' readings show. Where its own page has another thing, it takes a second line."
  - A container whose group no capability holds is a method ruling.
  - Test: a NOTE listing every entry whose `pageKey` prefixes other entries' keys, for a second reading. It catches line 18.
- **F7, release badges.**
  - Add: "A page's badge `new` is a release marker: its `supports` stand and the badge goes in `reading`."
  - Whether `beta` makes it `shows` is a method ruling.
  - Test: needs the badge in the entry (the extractor).

The recurring misses in my lines:
- 16 `missing scope` rows: F5's test;
- 2 `wrong supports` and 2 `missing line` rows on app pages: F2's tests;
- the maker gap: F3's test.

The two `wrong reading` rows aren't recurring; line 3's misquoted permission is `care`, and no test catches it.

## Method rulings for the coordinator (B-extent doesn't settle them)

1. A page the platform's own navigation lists under its brand at an app's address, with no maker or gate stated (Zid Ads, Zid Voice). My verdict is `shows`.
2. Whether a listing condition in the source is a scope (F5).
3. Whether a run step's text can be a statement. It would hold CM-INV-004, CM-MKT-023 and CM-ORD-014 for Zid, CM-CHN-004's fillers, and Zid Insights' trial.
4. A container whose group no capability holds (F6).
5. Whether a conditional title in the source (the charity store's) can be read as a statement of its own. It would hold CM-SEL-007 for Zid.
6. A page's `beta` badge (F7; R5a's entry 86).
