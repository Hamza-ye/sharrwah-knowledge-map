# SH-95: Shopify's `play-publisher-apps` and `pos-app-navigation` (notes)

**The batch:** platform `shopify`, batch `SH-95`, effort `high`. Its 117 entries are two structures, both read from Android accessibility trees (uiautomator) on the founder's phone (Xiaomi 21121119SC, Android 11, locale en-AU; `meta.json`, `device`), at observed-sh `e38dc17e3`:
- entries 1 to 21, `play-publisher-apps` (`structures/shopify/play-publisher-apps/google-play@pub-shopify-inc/items.jsonl`, 60 rows): Google Play's page of the apps its publisher Shopify Inc lists, run `20261005T013953Z-android-play-shopify-apps`, steps 1 and 2 (one dump: `meta.json`, `dumps_sha256`);
- entries 22 to 117, `pos-app-navigation` (`structures/shopify/pos-app-navigation/fake-demo-sharrwah/items.jsonl`, 149 rows): the POS app's Home, Orders, Products and More screens, run `20261005T021253Z-android-pos-walk`, steps 1 to 4, on the store fake-demo-sharrwah (Advanced, the run's note), POS 11.15.0 (`meta.json`, `packages`).

**No batch had placed either structure.** `held_entries.py earlier` printed only SH-96's lines on the POS's frame nodes and bottom tabs, SH-2's label Point of Sale, and SH-96's 'Shop location'. The rules below are mine, for the coordinator to check.

**What I read:** the brief; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run"; the rulings, whole; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; `REGISTER.tsv`'s rows 68 and 73; `index/runs.tsv` and `index/run-notes.tsv` for the two runs; `selection.tsv`'s two rows; both structures' `meta.json` and items; SH-96's placements and notes with its coordinator's check, and SH-38's coordinator's check (the Customer View app). To clarify entries only, I read the two runs' `actions.jsonl` and these steps, which the runs join to the structures: the Play run's listing pages (steps 3, 5, 7, 10, 13, 16, 19) and the POS walk's pages opened from the More sheet (steps 5, 8, 11, 38). No `index/ledger/` file enumerates these structures: the ledgers count admin routes, controls, mutations, journey units and sitemaps, not Play pages or the POS app's screens.

## How the structures read

- **An entry stands for every item with its words, and its `parent` is an index within its step**, as SH-96 found. The build drops ids of the form `android:id/…`, `com.android.vending:id/…` and `com.shopify.pos:id/…` from the entries' text, so frame nodes read as bare classes. I read each entry's item at its locator's line.
- **`play-publisher-apps`: the app cards have no entries.** Each app is two sibling rows of the list (parent 4): its card, whose `desc` holds the app's name, its developer 'Shopify Inc.', its categories, rating, size and downloads on separate lines (`items.jsonl`, lines 6, 8, 10, 12, 14, 16 and 18 for step 1, and 36 to 48 for step 2), and its card's control 'Expand content for <app>' (lines 7 to 19). Only the controls are entries. So each app's entry is its control, read with its card as its row (rule 1), and each line cites the card's line for the maker statement. See "Problems".
- **`pos-app-navigation`:** one entry can stand for nodes on two screens. `SH-E-166a1a8e` (the search bar's `Component.SearchBar` group) and `SH-E-fd25738e` ('Scan Barcode') are the Orders screen's (step 2) and the Products screen's (steps 3 and 4); the bottom tabs, the cart button and the frame nodes stand for all four steps.

## The rules I followed (for the coordinator to check)

**`play-publisher-apps`:**
1. **The page's frame is `out`** (the coordinator, for SH-95; the ruling after SH-37): its layout nodes, 'Navigate up', the search field's query 'pub:Shopify Inc.', 'Search Google Play', 'Voice Search', the tabs 'Games', 'Apps', 'Search' and 'You', and the status and navigation bars. The query names the publisher whose apps the page lists, but as an entry it's the store's search field; the publisher is read on each app's line.
2. **Each listed app takes one line, on the capability of what the app does**, read with its card and its listing page. The listing names Shopify Inc. as the developer, a maker statement (the ruling after SH-2), so the line is `own-service`, with these exceptions:
   - **the POS** (`SH-E-b1f2eef3`), the platform's own sales channel that its plans include, stays `core` on CM-POS-001 (the ruling after SH-55);
   - **Customer View** (`SH-E-a2d99b39`), 'a customer facing display for your POS', stays `core` on CM-POS-001 as part of Shopify POS. That's the coordinator's check after SH-38, which kept the Customer View app `core` on CM-POS-001, and SH-37's and SH-38's lines on its posts;
   - **the Shopify app** (`SH-E-f0211ff6`), the admin on a phone, is the admin's own, `core` on CM-SRF-001 (the coordinator, for SH-95).
3. **The others:**
   - Shop on CM-CHN-002 (Shop's things are `own-service`, the ruling after SH-34);
   - Shopify Inbox on CM-SUP-004 (the ruling after SH-2 names it);
   - Collabs: Content commerce on CM-MKT-013;
   - Tinker by Shopify, which no capability holds, `new`.

   The cells of CM-CHN-002, CM-POS-001, CM-SUP-004 and CM-MKT-013 already cite the same listing for four of these apps, from the concern map (SH-S-2756, SH-S-2757, SH-S-2758, SH-S-2760). The Shopify app, Tinker and Customer View are 'the ones not cited' (`selection.tsv`).
4. **What a listing's short description names in a list takes no line** (the ruling after SA-41): the POS's 'inventory system and cash register', the Shopify app's 'store, sales, marketing, marketplace', and Shop's title verbs Track, Pay and Discover.
5. **Ratings, review counts, sizes, install counts, content ratings and screenshots aren't capabilities and aren't qualities** (the coordinator, for SH-95). No line has a scope: the page names no plan, country, store or account. The concern map wrote these statements' scope as 'Google Play (publisher Shopify Inc.)', which is the venue, not a scope in the brief's sense.
6. **No CM-APP-011 line.** CM-APP-011 is the platform's own extensions in a category of its own in its marketplace, and Google Play isn't Shopify's marketplace. The coordinator's message asks for one line per app, on what it does. Earlier batches gave apps that Editions cards call 'An App From Shopify' a CM-APP-011 line as well (SH-50's Planet, Audiences, Dovetale and Collabs). If the coordinator reads a store listing of Shopify Inc.'s apps the same way, each of the seven takes a CM-APP-011 `own-service` line too. The cell is already `own-service`, so nothing changes.

**`pos-app-navigation`** (SH-96's rules, which the coordinator's check confirmed, applied here):
1. **The frame is `out`:** a layout node with no text, no description and no id that names a thing. That covers the action bar root, the content frame, the tab navigator's boundary, the active indicator and the navigation bar, as SH-96 has them. It also covers the Home header `Component.SmartGridHeaderView`, the tiles' `Component.FadeIn.animatedView`, the cart's `Component.CartIsland.Scrim` and `…ContentSlot`, the More sheet's 'Card controller, partial screen' and 'Bottom Sheet', the sheet's header `Component.AppNavigation.MoreMenu.Header` and `undefined.Default`, and the heading wrappers `Screen.OrdersScreen.Default` and `Screen.ProductsIndex.Default` (SH-96's `Component.Heading.Default`).
2. **A screen is a container on its own capability, `core` (M-13).** Each node that bears a screen's own id counts, its header node included: `Screen.Home` on CM-POS-001; `Screen.OrdersScreen` ×2 on CM-ORD-001; `Screen.ProductsIndex` ×2 and `Screen.ProductsList` on CM-CAT-001. A screen's title ('All orders', 'All products') takes the screen's line.
3. **The More sheet is `out`**, its screen (`Screen.More` ×2) and its list (`Screen.More.IndexScreen.Container`) included. Its title names only a grouping over several capabilities' places (the ruling after SA-28), as SH-96 placed the tab More. Each of its six items is placed on the page it opens, read with the walk's step that opened it:
   - Customers on CM-CUS-001 (step 5, 'All customers');
   - Register on CM-POS-003 (step 8, 'Session', 'Cash tracking', 'Drawer', 'Open session');
   - Staff on CM-STF-001 (step 11);
   - Settings on CM-POS-001 (step 14, SH-96's screen);
   - Support on CM-ONB-003 (step 38, 'Learn about POS', 'Report a bug', 'Diagnostics', 'Contact support');
   - Upgrade to Pro on CM-POS-001 (POS Pro, 'Add POS Pro for Shop location', the run's note).
4. **The bottom tabs take SH-96's lines:** Home CM-POS-001, Orders CM-ORD-001, Products CM-CAT-001, More `out`.
5. **A control goes on what it does, `core`.** A list's search, filters, sort and scan button are parts of the list (rule 3): CM-ORD-001 on the Orders screen, CM-CAT-001 on the Products screen. A Home screen control whose object the screen doesn't state goes on CM-POS-001, as a control of POS alone (SH-34's rule 8): the search bar, 'Scan barcode', the connectivity status and the cart button. The cart button is POS v11.15's persistent cart button on phones (SH-E-79b32248), the staff's cart, not CM-CHK-002's buyer's cart.
6. **A smart grid tile goes on what it does.** The grid it sits in gives it no line (a group it sits under):
   - 'Apply discount' on CM-MKT-001, beside the cell's staff permission APPLY_DISCOUNTS_TO_ORDERS;
   - 'Add staff to sale' on `new:Staff sales attribution`, SH-50's new thing;
   - 'Add custom sale' on CM-POS-001;
   - the card reader tile on CM-POS-002, the device that takes the buyer's card;
   - 'Add tile' on CM-POS-001 (the changelog's Add tile flow).

   The smart grid itself (`Component.SmartGridView`) is CM-POS-001's container, as the changelog's smart grid lines are.
7. **A filter's value takes its filter's line, with the value in `reading`** (SH-96's rule for a setting's value): 'Point of Sale' under 'Filtered by Channel'. A value that is one store's data is `out`: 'Shop location', the store's location's name.
8. **One store's or one account's own data is `out`:** the product row (its id, 'demo-fake-product', '2 variants', its price), the signed-in staff member's name, the store's name 'My Store', and the empty state 'No orders for this location'.
9. **An entry that stands for nodes on two screens of different capabilities takes a line on each:** `SH-E-166a1a8e` and `SH-E-fd25738e`, on CM-ORD-001 and CM-CAT-001.
10. **Scope is empty on every line,** as in SH-96: no entry states a plan, store, market or listing condition.

## New things

- **`new:Tinker by Shopify`** (`SH-E-e95ada94`), 1 line, `own-service`.
  - **What is held:** its card names the developer 'Shopify Inc.' and the category 'Productivity' (`items.jsonl`, line 14). Its listing reads 'From idea to asset' and 'In-app purchases' (`20261005T013953Z-android-play-shopify-apps/steps/019.uia.xml`, nodes 39 and 18). No held words say what kind of asset it makes; the listing's 'Learn more About this app' wasn't opened.
  - **A place of its own:** none. A separate app's store listing isn't one of B-extent's kinds (an admin route or section, an API group, a plan line, or a category of the platform's own app store). By the brief's rule, a new thing with no place of its own is `shows`. I wrote `own-service`, following the coordinator's message for this batch ('each listed app … `own-service`, with the listing as its maker statement') and SH-50's `new:Planet`, which is `own-service` with its maker statement. The coordinator decides which.
  - **Proposed:** domain F, area APP, under CM-APP-011, a reading: the only held statement about it is that the platform's company publishes it. If the second stage reads its full description, it may belong with media (CM-CAT-007) or AI generation (CM-AIA-003), whose cells hold nothing of it. Otherwise it is likely `out` for want of a place of its own.
  - **Names:** English 'Tinker by Shopify'. No Arabic is held: the phone ran in en-AU, and Google Play's page is in English.
  - **Searched:** `caps --terms` for Tinker; asset; image generation; generate images; image; images; photo; video; media; generative; AI-generated; content generation; design; brand assets; display; screen; app made by; mobile app. `class_slice.py search --platform shopify` for Tinker and 'From idea to asset' found nothing. `makers` found only this entry.
- **`new:Staff sales attribution`** (`SH-E-4dccc82d`, `SH-E-eae376a3`: the tile 'Add staff to sale' and its label), 2 lines, `core`. This is SH-50's new thing (SH-E-ada073f2), with SH-53's 'attribute a sale to a staff member' and SH-6's and SH-7's role permission SALE_ATTRIBUTIONS_FOR_ORDERS.
  - **A place of its own:** none from these entries: a tile is a control inside the Home screen.
  - **Proposed:** as SH-50 proposed, domain A, area STF, under CM-STF-001.
  - **Names:** English 'Add staff to sale'.
  - **Searched:** attribution; sales attribution; staff attribution; attribute; commission. CM-MKT-008 credits orders to marketing (a homonym, as SH-50 found), and CM-B2B-006 (the entry's lead) is staff assigned to business buyers' companies.

## Entries I couldn't tell, and what would settle each

- **Customer View (`SH-E-a2d99b39`): `core` or `own-service` on CM-POS-001.** Its listing names Shopify Inc. as the developer of a separate app (package `com.shopify.pos.customerview`), and the ruling after SH-2 reads a listing so. The coordinator's check after SH-38 keeps the app `core` as part of Shopify POS, and the POS stays `core` (the ruling after SH-55). I followed the check. If the coordinator reads the listing as making a separate service, the line is `own-service`.
- **The POS's listing (`SH-E-b1f2eef3`): `core`, against the concern map's own reading of the same listing.** CM-POS-001's cell holds `own-service` only from SH-S-2757, 'POS app on Google Play, publisher Shopify Inc.'. By the ruling after SH-55 that row is `core`. If the coordinator reads it again, CM-POS-001's `own-service` rests on nothing held, with Customer View as above.
- **Shop's title (`SH-E-19de3ddc`): one line on CM-CHN-002.** 'Track, Pay, Discover' could also be read as naming shipment tracking for the buyer (CM-SHP-017) and Shop Pay (CM-PAY-014), whose Shopify cells are `core;extension-point` and `core;own-service`. The title names neither tracking information nor Shop Pay, and the concern map reads the same statement on CM-CHN-002 alone. A line on CM-SHP-017 would add `own-service` there.
- **Collabs (`SH-E-5470fac1`): CM-MKT-013 only.** The concern map gives the same listing to CM-MKT-014 and CM-MKT-015 as well. The entry names the app only, and CM-MKT-013 is its capability by name and terms.
- **The Home screen's search (`SH-E-c889febd`, `SH-E-07ecc3b9`, `SH-E-b906d9d5`): CM-POS-001, or `new:Admin search`.** The screen doesn't say what it searches. The admin's own search is a new thing (the ruling after SH-37). This one is the POS app's. Settled by a step that types into it.
- **'Scan barcode' and 'Scan Barcode' (`SH-E-4144b772`, `SH-E-fd25738e`):** what the barcode identifies (a product's barcode, an order's receipt) isn't stated. I placed each with its search bar.
- **'Add custom sale' (`SH-E-b30aaa7c`, `SH-E-62cc7ad5`): CM-POS-001, or a new thing.** No capability holds custom sales or custom items (searched: custom sale, custom item, custom line item, custom product). A tile isn't a place of its own, so a new thing would be `shows`. CM-CHK-009, the entry's first lead, is the buyer's order options at checkout: not its thing.
- **The Orders screen's filters:** 'Filtered by Sale location' and 'Filter by Fulfillment status' each take one line on CM-ORD-001, as parts of the orders list. Their dimensions are CM-INV-005's locations and CM-SHP-009's fulfilment. I read a filter as the list's own thing, not a kind of what it filters by (M-6 refined). CM-OPS-004, the fulfilment filter's first lead, is the store's system status: not its thing. The channel filter's value 'Point of Sale' (`SH-E-1dcbb6b7`) is on CM-ORD-001 as the filter's value. The earlier line on the same label (SH-2, CM-POS-001) is the admin's navigation item for the POS channel, another place.
- **The header nodes `Screen.OrdersScreen` and `Screen.ProductsIndex` (the second of each pair):** they sit where SH-96's `Component.Heading` sits, which was `out`, but they bear the screen's own id. I placed them with their screen (rule 2). Either way no cell changes.
- **Upgrade to Pro (`SH-E-fc2aacb2`, `SH-E-27bf8ab3`): CM-POS-001**, where POS Pro's offer lines are (SH-68 to SH-70). The page it opens wasn't captured (steps 41 and 42 held no tree). A plan or add-on capability (CM-PLN-001) is the alternative, if the coordinator reads an add-on's purchase there.
- **Staff (`SH-E-21e74ed9`, `SH-E-0686c718`): CM-STF-001.** The walk's step 11 lists the staff with their POS roles. The role, 'Point of Sale Administrator', is CM-STF-002's thing and is named only in `reading`.

## The checker's lines, read again

- **`CHANGES CM-POS-002@shopify gains core, by lines 28, 29, 30`:** the Home tile 'Take payments anywhere, anytime, Connect a card reader', its heading and its line. Read again: the tile connects the card reader, the device that takes the buyer's card at the point of sale (CM-POS-002's note), from the platform's own POS app. That's `core`, as the coordinator's check after SH-96 made the POS app's own device settings `core` on CM-POS-002. CM-PAY-021's note leaves the device to CM-POS-002 and keeps the payment's processing and rates, which the tile doesn't name. Kept.
- **`NOTE own-service`** on CM-CHN-002, CM-SUP-004, CM-MKT-013 and `new:Tinker by Shopify`: each rests on its card's developer 'Shopify Inc.' (the ruling after SH-2), cited by line.
- **`NOTE line 5: core on a product named with the platform's brand`:** the POS app. Its listing does name a maker, but the POS stays `core` (the ruling after SH-55).
- **`NOTE` new things whose entry has leads:**
  - Tinker's lead CM-CNT-003 comes from the word 'content' in 'Expand content for', which every app's entry holds: no lead.
  - Staff sales attribution's lead CM-B2B-006 is sales reps assigned to business buyers' companies, read in its cell: a homonym.
- **`NOTE` first leads that hold nothing:** CM-CHK-009 for 'Add custom sale' and CM-OPS-004 for the fulfilment filter, each read in its cell and named in the line's reading. Neither is the entry's thing.
- **`NOTE` quotes found nowhere held** (lines 3 to 9, 77, 78 and 81): every one is quoted from a run step's `.uia.xml`, which the checker doesn't read. I checked each against the cited file's node text and description, with the XML's escapes undone, and each is there exactly. To avoid the escaped `&amp;`, the Shopify app's listing is quoted only in part.
- **No `NOTE` on containers** printed. My containers are the POS's Home, Orders and Products screens, the product list and the smart grid.

## A structure whose items and entries disagree

- `play-publisher-apps`: the seven app cards (`items.jsonl`, lines 6 to 18 even, and 36 to 48 even) have no entry. Their `desc` holds several lines ('Shopify Inbox\nShopify Inc.\nBusiness\nCRM\n21 MB\nDownloaded 500 thousand plus times\n'), and the build seems to leave out an item whose text holds a newline, a reading. The items and their source step agree. Each card is the statement that names the developer, so each app's maker statement is held in an item that no entry holds. Giving each card an entry would let the line cite the maker in its own entry. The run's note, 'each installed from its listing', and the concern map's SH-S-2756, SH-S-2757, SH-S-2758 and SH-S-2760 read the same cards.

## What the sources state that no entry holds (for the second stage)

The step files are single-line XML, so each is cited by node, in document order.
- **Each app's listing page,** run `20261005T013953Z-android-play-shopify-apps`, which no structure holds (`REGISTER.tsv` row 68 holds steps 1 and 2). Each page has its developer, its rating and review count, 'Content rating Rated for 3+', its 'About this app' line and its tags:
  - step 3, the Shopify app: nodes 19, 21, 22, 37, and 39 and 45 ('Business tag', 'Widgets tag');
  - step 5, the POS: nodes 42, 44 and 50 ('Point of sale tag'), and 29 ('Install on more devices');
  - step 7, Shop: nodes 42, 44 and 49 ('Online marketplace tag');
  - step 10, Inbox: node 36;
  - step 13, Customer View: node 36;
  - step 16, Collabs: node 37;
  - step 19, Tinker: nodes 18 and 39.

  These are leads for CM-SRF-001, CM-CHN-002, CM-SUP-004, CM-MKT-013 and Tinker. The Customer View app's package (`raw/runs/20261005T020136Z-android-apks/apks/com.shopify.pos.customerview/`) is held and not read; SH-38 named it.
- **The POS walk's pages opened from the More sheet,** run `20261005T021253Z-android-pos-walk`, which no structure holds (`pos-app-navigation` holds steps 1 to 4, `pos-settings` steps 14 to 35):
  - **step 5, All customers:** 'Search customers' (node 44), 'Add a new customer' (`Screen.CustomersList.AddButton`, node 49), 'Filter by Tags' (node 56), 'Sorted by Sort' (node 66) and the list (node 82). Leads for CM-CUS-001 and its customer tags;
  - **step 8, Register (`Screen.TrackingSessionDetails`):** 'Open session' (node 49), 'Settings' (node 51), 'Session' (node 62), 'Status, Closed' (node 63), 'Cash tracking, On' (node 66) and 'Drawer, N/A' (node 69). A lead for CM-POS-003, whose cell holds only the API's scopes and query: this is the POS app's own cash session page;
  - **step 11, Staff:** 'Sorted by Name (A-Z)' (node 42), and the staff row with its role 'Point of Sale Administrator' (node 58). A lead for CM-STF-001 and CM-STF-002;
  - **step 38, Support:** 'Learn about POS' (node 34), 'Report a bug' (node 44), 'Diagnostics' (node 54) and 'Contact support' (node 62), as SH-96 noted. A lead for CM-ONB-003;
  - **steps 41 to 43:** Add POS Pro, which held no tree while it loaded, and the PIN lock screen at step 43 (the run's note).

## Problems with this brief or the script

- **The cards' missing entries** (above).
- **The checker doesn't read Android steps' `.uia.xml`,** so a quote from one is reported as found nowhere held. A reading can cite only the step, since Android runs have no `.text.txt`.
- `show` prints an entry's `parent` without its step, as SH-96 noted. The entries' text also drops system ids (`android:id/…`, `com.android.vending:id/…`, `com.shopify.pos:id/…`), so the frame's entries can't be told apart without their items.
- **Where this brief and the coordinator's message read differently:** the brief makes a new thing with no place of its own `shows`, and the message makes each listed app `own-service`. This applies to Tinker only; I followed the message (above). No rule of the brief read differently from B-extent.md here.
