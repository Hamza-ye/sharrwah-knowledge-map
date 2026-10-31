# SH-83: Shopify's `mobile-app-settings-index`, the second half of its nodes' first occurrences (notes)

**The batch:** platform `shopify`, batch `SH-83`, effort `high`. Its 107 entries are the first occurrence of each node of `mobile-app-settings-index` from the title of the result Authentication on: the Shopify app's (com.shopify.mobile 10.2638.0) search, with the query 'settings' and the filter Settings, on the founder's phone (Xiaomi 21121119SC, Android 11, locale en-AU; `meta.json`, `device` and `packages`), at observed-sh `e38dc17e3`. One label, `search-settings`: run `20261005T022544Z-android-shopify-mobile`, steps 51 to 67 (`source/051.uia.xml` to `067.uia.xml`).

The repeats (SH-84) take these lines by `method/held_mobile_repeats.py`, so each line is written for the node wherever the screens show it. I ran the script's `--help` only.

**What I read:** the brief; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; the rulings' last section; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; `REGISTER.tsv` row 72; `selection.tsv`'s rows for this structure and for `admin-router`; the label's `meta.json` and items; SH-82's notes with its rules R82.1 to R82.8 and the coordinator's check, and its lines on Authentication's cell and button (SH-82:94 to 97) and on Authorize.net (SH-82:40 to 42); SH-80's rules R80.1 to R80.12 and its check. To clarify entries only, I read: `structures/shopify/admin-router/items.jsonl` for the routes and anchors the results' keys name; the router batches' lines on those routes and anchors (SH-8:4, 8 and 54; SH-10:72 and 74; SH-12:2, 4, 9, 10 and 55; SH-14:39 and 42; SH-16:24 and 29; SH-17:72 to 79, 88 and 96 to 104; SH-18:29 and 30); SH-97's and SH-20's lines on the settings links of the same titles (SH-97:16 to 38, SH-20:12 to 53); the label lines `held_entries.py earlier` printed (SH-23:95, SH-43:122, SH-57:89, SH-62:52 and 53, SH-66:42); the step dumps 058 and 059 for the result whose cell alone is held; and the trial store's Settings pages that SH-17 cited (`raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/477.text.txt` and `484.text.txt`). No `index/ledger/` file enumerates this structure.

## How my half reads

My half holds 27 results and the title and description of a 28th, Authentication, whose cell and button are SH-82's. With SH-82's 22 they make the 49 of the filter's chip 'Settings, 49'. Each result is four nodes, as SH-82 read them: the cell (`Screen.AdminSearch.SearchResult.Cell.gid://shopify/SettingsLink/<key>`), the button 'Settings page titled <title>', the title and the description. One result is its cell alone (below, R83.2).

Every key but the two `mobile|` ones matches a route or a route's anchor of the same title in `structures/shopify/admin-router/items.jsonl`, `|` read for `:` (a reading, R82.3). `customerAccountsSettings|returns` is the route `customerAccountsSettings` (Customer accounts) with its anchor 'Self-serve returns'; `notification-settings|customer|delivery` is `notification-settings:customer` with its anchor 'Local delivery notifications'; `shipping|list|customfufillment` keeps the router's own spelling of the anchor's path.

## The rules I kept, and the ones I set (R83.1 to R83.5)

I kept R82.1 to R82.8 and R80.1 to R80.12 as the coordinator's check after SH-82 kept them. My half holds none of the search screen's frame or its own nodes (R82.1, R82.2): its entries are results only, so no line is `out` and none is `new:Admin search` (R82.5: the search only says where the results are). Scope is empty on every line (R82.8); a route's permission is named in `reading` where a line cites the route's gate.

- **R83.1: the app's two settings of its own** (R82.6). Their keys begin `mobile|`, no admin route has their id, and the words say 'this device'.
  - **App security** (`mobile|settings|security`, 'Manage biometrics settings for this device') takes CM-SRF-001 `core` and CM-TRU-001 `core`. The second is the capability of what the setting sets: biometrics secure the sign-in to the admin through the app, beside the passkeys and two-step authentication CM-TRU-001 holds, and CM-ACC-001's note puts Salla's biometric flags in TRU (a reading). The lead CM-TRU-019 is the App Store's security apps.
  - **Store notifications** (`mobile|settings|store|notifications`, 'Manage store notification settings') takes CM-SRF-001 `core` alone: its name holds the mobile app's push notifications, and its note keeps them there (SH-82's lead). The admin's Settings > Notifications (CM-NTF-001) and Staff notifications (CM-NTF-002) are the store's messages, set in the admin, not the app's on the device (a reading; below, entries I couldn't tell).
- **R83.2: a result whose cell alone is held takes its anchor's line.** `checkout-settings|index|language` is the route `checkout-settings:index` (Checkout) with its anchor 'Checkout language': CM-MKS-008 `core`, as SH-10:74 placed the anchor. The cell occurs twice, at step 58 off the screen (bounds `[0,0][0,0]`, no node under it) and at step 59 as a strip of 22 pixels at the top of the list (`source/058.uia.xml`, node 66; `059.uia.xml`, node 19), so its button, title and description are held nowhere (48 titled buttons for 49 cells).
- **R83.3: a description takes a second line for each other capability's thing it names** (S97.2; R82.4; the coordinator's check after SH-82 kept Shop Payments Settings' four lines). What it lists as the setting's own parts takes none (the ruling after SA-41): Return rules' fees, shipping and final sale items; Brand's logos, colors, slogan and social links; Domains' purchase and connection. The second things:
  - Local delivery notifications: 'local delivery settings', CM-SHP-008 (a reading: the store's own delivery, whose settings are Settings > Shipping and delivery's anchor 'Local delivery');
  - Store details: 'order processing', CM-ORD-001 (the anchor of that title, SH-17:79), and 'company details', CM-ACC-004 (a reading, below);
  - Shipping labels: 'preferred carrier services', CM-SHP-015 (SH-17:99, SH-62:52);
  - Security: 'collaborators', CM-STF-005 (the route's anchor 'Collaborators' and its gates COLLABORATOR_REQUEST_SETTINGS and MANAGE_COLLABORATOR_REQUEST_PIN);
  - Payments: 'Shopify Payments', CM-PAY-002 (below).
- **R83.4: an anchor that is two things takes both its lines on every node** (the ruling after SA-19). 'Shipping labels' (path `preferred-carriers`) is so: SH-17:98 placed the title on CM-SHP-002 and SH-17:99 its path, the preferred carriers, on CM-SHP-015, the page reading 'Buy discounted shipping labels and manage preferred carriers' (`484.text.txt`, line 74). Its cell, button and title take both. The route Manage preferred carriers (`carrier-services`), which CM-SHP-004 cites, is the carriers' calculated rates, a homonym.
- **R83.5: a route no router batch placed takes the cell that cites it and the settings link of the same title.** Three routes the keys name have no `admin-router` entry, since that structure's selection reads 'the routes the concern map didn't cite' (`selection.tsv`): `payments:settings:shop-pay` (items.jsonl line 1019; CM-PAY-014's cell holds it, its term `payments:settings:shop-pay`), `settings:organizations:accounts:security` (line 949; CM-TRU-001's cell, SH-S-5238; SH-97:18 and SH-20:14 and 37 for the link Security) and `order-routing:update` (line 1234; CM-SHP-005's cell, SH-S-7140).

**The results and the lines they took** (each with its cell, button and title, and its description):

| Result (key) | Line | From |
| --- | --- | --- |
| Authentication, its title and description (`customerAuthenticationSettings`) | CM-CUS-011; CM-CUS-010 | SH-12:9 and 10, SH-82:94 to 97 |
| Local delivery notifications (`notification-settings\|customer\|delivery`) | CM-NTF-001; the description also CM-SHP-008 | SH-14:42; R83.3 |
| Return rules (`setting\|legal\|index\|return-rules`) | CM-RET-003 | SH-17:73, SH-57:89 |
| Checkout language, the cell alone (`checkout-settings\|index\|language`) | CM-MKS-008 | SH-10:74; R83.2 |
| Custom order fulfillment (`shipping\|list\|customfufillment`) | CM-SHP-011 `extension-point` | SH-17:104 |
| Organization security (`settings\|organizations\|accounts\|security\|organization-security`) | CM-TRU-001 | its cell; SH-97:18; R83.5 |
| Shop Pay (`payments\|settings\|shop-pay`) | CM-PAY-014 | its cell; R83.5 |
| Shipping and delivery (`shipping\|list`) | CM-SHP-001 | SH-97:26, SH-20:21 and 41; SH-17:96 |
| Pickup in store (`shipping\|list\|localpickup`) | CM-SHP-007 | SH-17:101 |
| Domains (`domains\|list`) | CM-SFR-008 | SH-97:32, SH-20:27 and 47; SH-12:55 |
| App security (`mobile\|settings\|security`) | CM-SRF-001; CM-TRU-001 | R82.6; R83.1 |
| Local delivery (`shipping\|list\|localdelivery`) | CM-SHP-008 | SH-17:100 |
| Order processing (`settings\|general\|inner\|order-processing`) | CM-ORD-001 | SH-17:79 |
| Notifications (`notification-settings\|fallback`) | CM-NTF-001 | SH-97:34, SH-20:29 and 49; SH-14:39 |
| Store details (`settings\|general\|inner\|store-details`) | CM-ACC-006; the description also CM-ORD-001 and CM-ACC-004 | SH-17:77, SH-43:122; R83.3 |
| Sales channels (`apps\|sales_channels_list`) | CM-CHN-001 | SH-97:31, SH-20:26 and 46; SH-8:54 |
| Additional payment methods (`payments\|settings\|index\|other`) | CM-PAY-011 | its cell; SH-16:29; R82.7 |
| Checkout (`checkout-settings\|index`) | CM-CHK-001 | SH-97:24, SH-20:19 and 39; SH-10:72 |
| Login services (`settings-account\|index\|login`) | CM-TRU-001 | SH-8:8 |
| Self-serve returns (`customerAccountsSettings\|returns`) | CM-RET-003 | SH-12:4 |
| Shipping labels (`shipping\|list\|preferred-carriers`) | CM-SHP-002; CM-SHP-015 | SH-17:98 and 99; R83.4 |
| Duties and import taxes (`tax-settings\|index\|duties`) | CM-TAX-008 | SH-18:30 |
| Store notifications (`mobile\|settings\|store\|notifications`) | CM-SRF-001 | R82.6; R83.1 |
| Packing slips (`shipping\|list\|packingslips`) | CM-ORD-009 | SH-17:102 |
| Security (`settings\|organizations\|accounts\|security`) | CM-TRU-001; the description also CM-STF-005 | SH-97:18, SH-20:14 and 37; R83.3; R83.5 |
| Brand (`settings\|general\|brand`) | CM-ACC-006 | SH-17:88 |
| Order routing (`order-routing\|update`) | CM-SHP-005 | its cell; R83.5 |
| Payments (`payments\|settings\|index\|payments`) | CM-PAY-001; the description also CM-PAY-002 | SH-97:23, SH-20:18 and 38; R83.3 |

**Homonyms and leads that aren't the entries' things:** CM-API-002 and CM-SFR-012 (by 'authentication'); CM-API-009, the Notifications page's webhooks; CM-SHP-019, pickup points; CM-SHP-023, BigCommerce's shipping rules engine (Return rules', Order routing's); CM-PLN-003, CM-PAY-007 and CM-PLN-004, the platform's fees (the duties' 'unexpected fees' are the buyer's); CM-SHP-020, international shipping; CM-CHK-009, the buyer's checkout fields; CM-PAY-015, Shop Pay Installments; CM-PAY-022, buyers' saved payment methods; CM-ACC-003 and CM-PTN-002, organizations (Organization security only says whose); CM-TRU-019, security apps; CM-ORD-003, order statuses; CM-ORD-010, Salla's order receiving; CM-SHP-004's Manage preferred carriers (R83.4); CM-INV-005, locations, which Pickup in store and Local delivery only name as where; CM-APP-001 and CM-APP-002, by 'installed' and the category Shipping and delivery; CM-PTN-005, by 'services'; and the leads by a common word (CM-MKT-007, CM-NTF-003, CM-NTF-004, CM-CUS-007, CM-PAY-013, CM-PAY-016, CM-PAY-017, CM-PAY-021, CM-PAY-029, CM-SHP-003, CM-SHP-012, CM-SHP-017, CM-SHP-018, CM-SHP-022, CM-TRU-005, CM-TRU-006, CM-TRU-007, CM-TRU-008, CM-MKS-004, CM-API-013, CM-STF-001, CM-TAX-001, CM-CHK-007).

## The new things

None. Every result's thing is a capability that already holds its route, anchor or settings link on Shopify.

## Entries I couldn't tell, and what would settle each

- **App security's CM-TRU-001 lines** (`SH-E-464e4863`, `SH-E-aef4fc14`, `SH-E-d7ab170c`, `SH-E-5e03254a`). That the biometrics secure the sign-in to the admin through the app is a reading of 'App security' and 'biometrics settings'; the page isn't held (no step opened it; `docs/GAPS.md`: 'The Shopify app's sections and settings pages (beyond its navigation and settings index)'). If the coordinator reads the app's lock as the app's own feature only, the three CM-TRU-001 lines go and CM-SRF-001 stays. Neither changes a cell.
- **Store notifications on CM-SRF-001 alone** (`SH-E-65cc83bc`, `SH-E-d9c069fb`, `SH-E-feedfd84`, `SH-E-728e9b55`). If the coordinator reads the app's store notifications as notices to the store's staff, they take CM-NTF-002 `core` too (no cell changes). Settled by the app's page, not held.
- **Store details' 'company details' on CM-ACC-004** (`SH-E-f2d1dce0`). CM-ACC-004's cell keeps the business entity's details in Settings > General as well as in Organization (its evidence rows 'help names Settings > General', 'creating business details' and 'editing business details'), so I read the company's details as that business's. SH-43:122 placed a post's 'Business information' on the Store details page on CM-ACC-006 alone: on that reading, this line goes. 'order processing' is a separate anchor of the same page with its own line (SH-17:79), so it stays either way.
- **Payments' 'Shopify Payments' on CM-PAY-002** (`SH-E-288dd0e2`). The description names it as an example of the providers the page configures ('payment providers like Shopify Payments'). I gave it a line, as SH-82 gave Shop Payments Settings' 'customizations' one. By the ruling after SA-41, a thing named only in a list of what may be changed takes none: on that reading, the line goes. No cell changes.
- **Additional payment methods `core`, not `extension-point`** (`SH-E-6825172e`, `SH-E-3fd07986`, `SH-E-eb6e3520`, `SH-E-caecc836`). “Accept payments with one of Shopify's approved payment providers” names third parties' providers in the platform's own words ('Shopify's approved'), read as M-4's list, `core`, as R82.7 placed Authorize.net's page and SH-16:29 an alternative provider's page. If the coordinator reads it as the platform's list of third parties' things to connect (M-7), the description takes `extension-point` too; CM-PAY-011 already holds both.
- **Local delivery notifications' description on CM-SHP-008** (`SH-E-4642814e`). 'Manage local delivery settings and notifications' names the local delivery settings beside the notifications; SH-14:42 gave the anchor's title no delivery line, since a notification of a delivery is no kind of delivery. I read the description's 'settings' as a second thing. If they are only the notifications' settings, the line goes.
- **Custom order fulfillment `extension-point` alone**, as SH-17:104 placed the anchor, and as the coordinator's check after SH-82 kept the twin's support for Delivery customizations. If a settings item is `core` whatever its twin, the four lines take `core` (CM-SHP-011 holds both).

## A structure whose items and sources disagree

- **`REGISTER.tsv` row 72 says '49 titles with a description each'.** The items hold 49 cells and 48 titled buttons: Checkout language's title and description are held nowhere (R83.2), the register's own limit, 'scrolled lists are held as the windows the steps showed'. With Apps' description (SH-82), two results lack a held description.
- The items and the dumps agree where I read them (steps 058 and 059). Sales channels' description first occurs at step 60, under that result's button (node 31); no description of my half is shared by two results.

## What the sources state that no entry holds (for the second stage)

- **Checkout language's button, title and description:** `raw/runs/20261005T022544Z-android-shopify-mobile/steps/058.uia.xml` and `059.uia.xml` hold only its cell (R83.2). A capture with a shorter swipe would hold them.
- **The web admin's Order processing choices:** 'After an order has been paid', with 'Automatically fulfill the order‘s line items', 'Automatically fulfill only the gift cards of the order' and 'Don’t fulfill any of the order’s line items automatically' (`raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/477.text.txt`, lines 97 to 104). A lead for CM-SHP-009, automatic fulfilment of paid orders; SH-17:79 placed the anchor on CM-ORD-001 by its archiving.
- **The app's own settings pages App security and Store notifications:** no step of the run opened them. After the results (steps 51 to 67) it cancels the search and opens the Sidekick tab (`raw/runs/20261005T022544Z-android-shopify-mobile/actions.jsonl`, steps 68 and 69). They would settle R83.1.

## Problems with this brief or the script

- **`held_entries.py earlier` finds no line by a result's key,** as SH-82 noted: it cuts the key at its first `|`, and the router batches cite the ids with `:`. It found the two-word titles' lines only. I matched the keys to the router's ids and searched the placements by hand.
- **The router batches never placed three of the keys' routes,** since `admin-router`'s selection leaves out the routes the concern map cited (R83.5). That is by design, but `earlier` can't show it: the cells that cite those routes are the only lead, found by their terms.
- No rule of the brief read differently from B-extent.md here.

## The checker's lines, read again

- **No `CHANGES` line.** Every capability these lines name already holds the support they give it on Shopify.
- **`NOTE` line 95, `core` on a product named with the platform's brand:** 'Shopify Payments' in the Payments description. It is the platform's own payment service, which CM-PAY-002's cell holds `core` ('the only payment gateway designed and operated by Shopify', SH-S-0382), an admin service, not a separate product, as the corrections to the rulings after SH-55 and SH-41 read Shopify Payments beside Shopify Balance. Kept, with the open choice above.
- **`NOTE` line 42, first lead CM-ORD-003 holding nothing:** the lead is order statuses, by the word processing. The Order processing section sets what happens to a paid order (automatic fulfilment, archiving; `477.text.txt`, lines 96 to 108), not an order's statuses. No line.
- **No `NEW` line.**

## The coordinator's check

Measured: 15.9 million tokens over 81 requests, about 149,000 an entry, the repeats left to `method/held_mobile_repeats.py`. The checker prints no problem, no `CHANGES` line and no new thing.
- **Kept:** R83.1 to R83.5, with SH-82's and SH-80's rules, and the open choices as placed (App security's CM-TRU-001, Store notifications alone on CM-SRF-001, Store details' CM-ACC-004, Payments' CM-PAY-002, Additional payment methods `core`, Local delivery notifications' CM-SHP-008, Custom order fulfillment `extension-point` as SH-17:104).
- **SH-84** is placed by the script from SH-80's, SH-82's and this batch's lines; `mobile-app-navigation` and `mobile-app-settings-index` are placed whole.
