# SH-82: Shopify's `mobile-app-settings-index`, the first half of its nodes' first occurrences (notes)

**The batch:** platform `shopify`, batch `SH-82`, effort `high`. Its 108 entries are the first occurrence of each node of `mobile-app-settings-index` up to the button of the result Authentication: the Shopify app's (com.shopify.mobile 10.2638.0) search, with the query 'settings' and the filter Settings, on the founder's phone (Xiaomi 21121119SC, Android 11, locale en-AU; `meta.json`, `device` and `packages`), at observed-sh `e38dc17e3`. One label, `search-settings`: run `20261005T022544Z-android-shopify-mobile`, steps 51 to 67 (`source/051.uia.xml` to `067.uia.xml`), the 49 settings results listed twenty at a time ('Show 20 more', steps 58 and 63).

The repeats (SH-84) take these lines by `method/held_mobile_repeats.py`, so each line is written for the node wherever the screens show it. I ran the script's `--help` only. SH-83 holds the structure's second half, from Authentication's title on; it had written no placements when I finished, so the coordinator aligns it with these rules.

**What I read:** the brief; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run"; the rulings' last section; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; `REGISTER.tsv` row 72; `selection.tsv`'s row; the label's `meta.json`, items and step dumps; the run's `actions.jsonl` (steps 37 to 68) and its run note; SH-80's notes with its rules and check; SH-97's settings-panel rules (S97.1 to S97.5) and check, and its 23 settings-panel lines; SH-20's rules R20.1 to R20.3 and its settings-navigation lines. To clarify entries only, I read: `structures/shopify/admin-router/items.jsonl` for the routes and anchors the results' keys name; the router batches' lines on those routes (SH-8:27, SH-12:2 and 9 to 10, SH-14:35, SH-15:13, 94 and 104, SH-16:9, 30, 31, 33 and 34, SH-17:2, 3, 58 and 103, SH-18:29); SH-46's lines on the Shopify app's languages (103, 104); and the run's steps 040 to 047, the same search before the filter and while the query was mistyped. No `index/ledger/` file enumerates this structure: the ledgers count admin routes, controls, mutations, journey units and sitemaps.

## How the structure reads

- **The screen:** a header (`animated-header`, SH-80's entry) holding 'Cancel search', the field 'Search the app' with the capture's query 'settings', 'Clear search', and a filter bar ('Selected: Settings') over the chips All 53, Settings 49, Navigation 4 and All filters; under it the results' container, `Screen.AdminSearch`; the app's tab bar under that (SH-80's entries).
- **A result** is four nodes: a cell with no text, whose id is `Screen.AdminSearch.SearchResult.Cell.gid://shopify/SettingsLink/<key>`; a button 'Settings page titled <title>'; the title; and the description, where it has one.
- **The key is the admin router's id, with `|` for `:`** (a reading). Each key of my batch but `mobile|languages` matches a route or a route's anchor of the same title in `structures/shopify/admin-router/items.jsonl`: `payments|settings|bank-account` is the route `payments:settings:bank-account`, 'Shop Payments Settings'; `customer-privacy|index|marketing` is `customer-privacy:index` with its anchor 'Marketing settings' (path `marketing`); `shipping|list|customization` is `shipping:list` with its anchor 'Delivery customizations' (path `customization`). So the app's settings index lists the admin's own settings routes and anchors, and a result's place of its own is that route's or anchor's.
- **An entry stands for every node with its words, apart from its parent's index** (the script's help). Two descriptions stand for two results each (below, R82.4), and the query 'settings' for its echo in both offers after the results.
- After the first twenty results come two offers: 'Ask Sidekick about settings' and 'Search settings in Shopify App Store', each with a label in three text nodes (steps 52 to 67).

## The rules I set (R82.1 to R82.8), for the coordinator to check and SH-83 to keep

- **R82.1: the search screen's frame is `out`** (R80.1; the ruling after SH-37). That covers:
  - the controls that name no place: 'Cancel search', 'Clear search', and the list's paging 'Show 20 more' with its label;
  - the counts of results for the capture's query ('53', '49', '4'), one session's results, as R80.10 placed the alerts' count;
  - the query 'settings' where the offers' labels echo it, a session's input;
  - the fragments of the offers' labels that name nothing alone: a closing quotation mark, and 'Search' with an opening one.
- **R82.2: the search screen itself is `new:Admin search` `core`** (R80.8). That covers the results' container `Screen.AdminSearch` (M-13), the field 'Search the app' (its value, the capture's query, goes in `reading`), the filter bar, and the filters All, Settings, Navigation and All filters, each chip with its label. A filter's name says which results it shows, not what the filter is, so the filter Settings takes no CM-ACC-006 line (M-6 refined).
- **R82.3: a result is a settings item the app lists, `core` on the capability its title names** (the coordinator's message), read with the route or anchor its key names.
  - It takes, in this order: the line SH-97 and SH-20 gave the settings link of the same title; the line a router batch gave that route or anchor; or the cell that cites the route.
  - Every link to a page that is two things takes both its lines (the ruling after SA-19): Shop Payments Settings (CM-PAY-005 and CM-PAY-002, SH-16:33 and 34), Taxes and duties (CM-TAX-001 and CM-TAX-008, S97.2), Customer privacy policy, Authentication (CM-CUS-011 and CM-CUS-010, SH-12:9 and 10), Language settings (R82.6).
  - The cell, whose text is its id alone, takes a line with its key's words as terms. The button and the title share a line with the title as term, on the same capability and support. The checker tests each term in each grouped entry, so the cell can't join them.
  - The support follows the twin's line. Delivery customizations keeps SH-17:103's `extension-point` (below, entries I couldn't tell).
- **R82.4: a description takes the setting's capability, and a second capability only where it names a second thing** (S97.2; the coordinator's message).
  - What it lists as what the setting lets people do is the setting's own and takes no line (the ruling after SA-41): Customer accounts' 'track orders, view order history, and save addresses'.
  - A description two results share is one entry, and its line fits both: 'Manage customer privacy settings' (Privacy settings, Customer privacy; CM-TRU-006), and 'Manage how sales taxes are collected per region' (Regional tax settings, Taxes and duties, both at step 51; CM-TAX-001).
- **R82.5: the offers after the results take the capability their own words name, `core`:** 'Ask Sidekick about settings' is CM-AIA-002 (R80.8's Sidekick); 'Search settings in Shopify App Store' is CM-APP-002, the platform's own App Store, as its cell holds it. The search only says where they are (M-6 refined), so they take no Admin search line. Each part of their labels takes the line of what its own words name ('Ask Sidekick about', 'in Shopify App Store'), or is `out` (R82.1).
- **R82.6: a result whose key begins `mobile|` is a setting of the Shopify app on the device.** No admin route has that id, and its words say 'your app' and 'this device'. It is CM-SRF-001 `core` (R80.7, E118), with the capability of what it sets where the model holds one.
  - Language settings takes `new:Admin languages` `core`, as SH-46 placed the Shopify app's own interface languages beside CM-SRF-001 (SH-E-ff9a1b45, SH-46:103 and 104).
  - SH-83 meets two more: App security ('Manage biometrics settings for this device') and Store notifications ('Manage store notification settings'). A lead for the second: CM-SRF-001's own name holds the mobile app's push notifications, which its note keeps in that capability.
- **R82.7: a third party's gateway that the app lists as a settings page is the admin's own page for that integration:** CM-PAY-011 `core`, as SH-16:31 placed the route. The provider (Authorize.net) is the filler of the lines whose words name it (M-4). The cell, whose key alone names it ('authorize-net'), names it in `reading`. 'Legacy' is a release marker, in `reading`.
- **R82.8: scope is empty on every line** (R80.12). No entry states a plan, market, store or listing condition. A route's permission is named in `reading` where a line cites the route's gate (MANAGE_POLICIES, ORDERS, PREFERENCES).

**The results and the lines they took** (each with its cell, button and title, and its description where it has one):

| Result (key) | Line | From |
| --- | --- | --- |
| Privacy settings (`customer-privacy\|index\|privacy-settings`) | CM-TRU-006 | SH-17:2, the anchor |
| Marketing settings (`customer-privacy\|index\|marketing`) | CM-CUS-007 | SH-17:3, the anchor |
| Language settings (`mobile\|languages`) | CM-SRF-001; new:Admin languages | R82.6; SH-46:103 and 104 |
| Shop Payments Settings (`payments\|settings\|bank-account`) | CM-PAY-005; CM-PAY-002 | SH-16:33 and 34 |
| Regional tax settings, Global tax settings (`tax-settings\|index\|regions`, `…\|settings`) | CM-TAX-001 | SH-18:29, the anchors |
| Authorize.net Legacy Gateway | CM-PAY-011, Authorize.net the filler | SH-16:31 |
| Taxes and duties (`tax-settings\|index`) | CM-TAX-001; CM-TAX-008 | SH-97, SH-20 (S97.2) |
| Organization | CM-ACC-003 | SH-97, SH-20; SH-15:94 |
| Users | CM-STF-001 | SH-97, SH-20; SH-15:104 |
| Payment reminders | CM-PAY-008 | SH-15:13 |
| Apps | CM-APP-001 | SH-97, SH-20; SH-8:27 |
| Customer privacy | CM-TRU-006 | SH-97, SH-20; SH-17:2 |
| Customer privacy policy (`customer-privacy-policy-modal`) | CM-TRU-006; CM-CNT-008 | CM-TRU-006's cell (SH-S-5253); its words |
| Metafield definitions, Metafields and metaobjects | CM-CNT-002 | SH-14:35; SH-97, SH-20 |
| Delivery customizations (`shipping\|list\|customization`) | CM-SHP-013 `extension-point` | SH-17:103, SH-49:56 |
| Policies (`setting\|legal\|index`) | CM-CNT-008 | SH-97, SH-20 |
| Staff notifications (`notification-settings\|staff`) | CM-NTF-002 | its cell (SH-S-5209); SH-36:18 |
| Customer accounts (`customerAccountsSettings\|customer_accounts`) | CM-CUS-010 | SH-97, SH-20; SH-12:2, without its own-service, which is Sign in with Shop's |
| Shipping to pickup points (`pickup-point\|list`) | CM-SHP-019 | its cell (SH-S-7138) |
| Authentication (`customerAuthenticationSettings`), its cell and button | CM-CUS-011; CM-CUS-010 | SH-12:9 and 10 |

The second things the descriptions name: Shop Payments Settings' description takes CM-PAY-001 and CM-PAY-019 too, and Customer privacy policy's CM-CNT-008 (below).

**Homonyms and leads that aren't the entries' things:**
- CM-TRU-005 leaves the privacy settings to its child CM-TRU-006 (SH-97's note).
- CM-PTN-002's Organization is the Partner Dashboard's.
- CM-CHK-009's custom fields are those the buyer fills in at checkout; 'Add a custom field to your store' is a merchant's metafield (CM-CNT-002's note).
- CM-APP-010 is an app's settings, not a gateway integration's.
- CM-SHP-006 and CM-SHP-007 are the store's own pickup, not pickup points (CM-SHP-019's note).
- CM-MKT-007 is marketing campaigns, not the consent to them.
- The leads by a common word, which name nothing the entries do: CM-PAY-014, CM-PAY-022, CM-TAX-004, CM-ORD-001, CM-B2B-002, CM-CUS-008, CM-API-009, CM-API-002, CM-SFR-012 and CM-SFR-013.

## The new things

- **`new:Admin search`:** 7 lines, `core`, on 11 entries: the field `SH-E-89f38fb2`, the filter bar `SH-E-eac1ed34`, the filters `SH-E-17012f55`, `SH-E-4ff46f08`, `SH-E-aa52b908`, `SH-E-a1983836`, `SH-E-dbee2484`, `SH-E-6d6ac472`, `SH-E-db2b6cbb` and `SH-E-cc0b4ef6`, and the results' container `SH-E-b2b76f19`. It is SH-80's new thing, SH-36's name, kept for the coordinator's decision with Saved views and Zid's and Salla's admin search (the ruling after SH-37).
  - **A place of its own:** yes, the one SH-80 named: the app's tab 'Search the app', which opens `Screen.AdminSearch`. These entries are that screen's field, filters and results; its results are the admin's settings pages, each placed on its own capability.
  - **Proposed:** as SH-36 and SH-80 proposed, domain F, no parent.
  - **Names:** English 'Search the app'; the screen's id names it AdminSearch. No Arabic is held: the phone ran in en-AU, and observed-sh holds no Arabic admin (`docs/GAPS.md`).
  - **Searched:** `caps --terms` with "app search" among the batch's terms: nothing; SH-80 searched "admin search; search the app; app search; AdminSearch; quick search": nothing.
- **`new:Admin languages`:** 3 lines, `core`, on 4 entries: the result Language settings, its cell `SH-E-61c06d73`, button `SH-E-277ba478`, title `SH-E-5e7e4b4d` and description `SH-E-eb426f87`. It is the admin's own interface language, one new thing across the platforms (the ruling after SA-49), under the name Shopify's batches give it (SH-34, SH-45, SH-46, SH-60, SH-67).
  - **A place of its own:** yes, a settings item the app lists with its own title, which B-extent counts as an admin section. It is a setting of the app on the device ('Change your app's language on this device'), not of the store.
  - **Proposed:** as decided in `held/new.tsv` with the others; the app's setting sits under CM-SRF-001, the mobile app, a lead for its parent on Shopify.
  - **Names:** English 'Language settings', 'your app's language'; no Arabic held.
  - **Searched:** `caps --terms` "admin language; interface language; app language": nothing.

## Entries I couldn't tell, and what would settle each

- **Shop Payments Settings' description** (`SH-E-62d0a726`), four lines.
  - Its title and key name the bank-account page: SH-16 read the route `payments:settings:bank-account` as the payout bank account (CM-PAY-005) and its title as Shopify Payments' settings (CM-PAY-002).
  - Its description, 'Manage payment settings and options for the store, including various payment methods and customizations.', reads like the payments settings as a whole. So it takes the setting's two lines (the coordinator's message), CM-PAY-001 for the settings and methods it names, and CM-PAY-019 for 'customizations', read as Payment customizations (a reading).
  - What would settle it: the page the result opens, not held. No run opened settings/payments/bank-account either (SH-16:33).
- **Delivery customizations, `extension-point`** (`SH-E-e2b950c0`, `SH-E-c5409340`, `SH-E-f83ee31a`, `SH-E-871499ff`). The message says a settings item is `core`. But the twin anchor's line, SH-17:103, is `extension-point` alone: the merchant there sets up rules that apps write, as its journey's template 'By Capture app' shows. I kept the twin's support, as the brief's twin rule asks. If the coordinator reads a settings item as `core` whatever its twin, these four lines take `core` and the cell changes nothing (it is `core;extension-point`).
- **Customer accounts' description** (`SH-E-8ed05eff`), one line. 'Customer accounts let customers log in to track orders, view order history, and save addresses for faster checkout' lists what the accounts do, which I read as their own parts (the ruling after SA-41). If tracking orders and saved addresses are second things, they would take a shipment-tracking line (CM-SHP-017) and an addresses line (CM-CUS-008).
- **Customer privacy policy's CM-CNT-008 lines** (`SH-E-15a37ef2`, `SH-E-c638ba0b`, `SH-E-969a7181`, `SH-E-11930b9b`).
  - CM-TRU-006's cell already holds the route `customer-privacy-policy-modal` (SH-S-5253).
  - Its title and description also name the privacy policy, the store's policy, which SH-17:58 placed on CM-CNT-008. The route's gate MANAGE_POLICIES is the policies' (CM-CNT-008's note).
  - What would settle it: the modal's page, which I didn't look for (no line cites a run of it).
- **The filters on `new:Admin search`, not `out`.** A chip such as 'All' names no place by itself. I read the filters as the search's own feature, its way of narrowing results, not its frame. If the coordinator reads them as the frame, the five filter lines go `out`, and the field, the filter bar and the results' container keep the new thing.
- **'Search' with an opening quotation mark** (`SH-E-131765b2`) is `out`, a fragment, while 'in Shopify App Store' (`SH-E-4d6ee296`) takes CM-APP-002. Each part of a label is placed by its own words (R82.5).

## A structure whose items and sources disagree

- **`REGISTER.tsv` row 72 says 'with a description each'.** In my half, Apps has none held, and two results show another's:
  - Apps' cell, button and title are in the tree at step 51 with bounds `[0,0][0,0]` (`source/051.uia.xml`, nodes 63 to 65): off the screen, and scrolled past by step 52, so its description isn't held. This is the register's own limit, 'scrolled lists are held as the windows the steps showed'.
  - Taxes and duties shows Regional tax settings' description, and Customer privacy shows Privacy settings'.
  - Sales channels' first occurrence (step 59, SH-83's) is off the screen too.
  - The register is the capture's description; the bytes govern.
- The items and their dumps agree where I read them (steps 051, 052 and 058). The run's step 040 shows the same results under the filter All.

## What the sources state that no entry holds (for the second stage)

All are in `raw/runs/20261005T022544Z-android-shopify-mobile/steps/`:
- **Apps' description**, not held (above). A capture with a shorter swipe would hold it.
- **The filter Navigation's four results:** no step shows them. Step 040 (filter All) lists the settings first, and steps 041 to 067 are filtered to Settings. They're a lead for what the admin search finds among the app's navigation, `new:Admin search`.
- **'All filters'**: no step opened it.
- **Steps 042 to 047:** the mistyped query 'settings by…' answered 'Settings, 2' and then 'Settings, 1' (the run note). A session's glitch, no lead.

## Problems with this brief or the script

- **The checker's container `NOTE` on line 7 is a false match.** It says '53' holds 3 other entries. Those entries are the three label nodes of 'Ask Sidekick about settings' (`SH-E-6fbbeaca`, `SH-E-e6397341`, `SH-E-a29dc416`), whose `parent: 53` is that button's index at step 52, not the text '53'. The count is placed `out` (R82.1).
- **`held_entries.py earlier` finds no line by a result's key.** It cuts the key at its first `|`, and the router batches cite the ids with `:`. I matched the keys to the router's ids, and searched the placements by hand.
- **The checker tests each term in each grouped entry's text,** so a result's cell can't share a line with its title (R82.3). That gives two lines per result where one would do.
- No rule of the brief read differently from B-extent.md here.

## The checker's lines, read again

- **No `CHANGES` line.** Every capability these lines name already holds the support they give it on Shopify.
- **`NOTE` lines 88 and 90, `core` on a product named with the platform's brand:** 'Search settings in Shopify App Store' and its label's last part. The Shopify App Store is the platform's own marketplace, and CM-APP-002's cell holds it `core`: in shopify.com's header navigation (SH-S-2753), reviewed by Shopify (SH-S-0698). It is a place of the platform, not a separate product that needs a maker statement, and the offer names no app or developer. Kept.
- **`NOTE` line 42, CM-APP-010:** the Authorize.net gateway's integration isn't an app's settings (above).
- **`NOTE` line 68, CM-CHK-009:** 'Add a custom field to your store' isn't a buyer's checkout field (above).
- **`NOTE` line 7:** the false container (above).
- **`NEW`:** Admin search, 7 lines; Admin languages, 3 lines (above).
