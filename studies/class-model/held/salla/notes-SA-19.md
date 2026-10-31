# Held pass, Salla, batch SA-19: notes

86 entries (effort high), evidence at observed-sa@b0bd0b163:
- `dashboard-main-navigation`, its last 6 entries (1 to 6): `merchant@ar/items.jsonl` lines 128 to 133, the top bar's link الرئيسية (Home) and its five buttons الطلبات, المنتجات, التسويق, المتجر وقنوات البيع and التقارير. SA-17 and SA-18 placed lines 1 to 127, so the structure is now placed whole;
- `dashboard-menu-marketing`, all 15 links in Arabic (7 to 21) and English (22 to 36);
- `dashboard-menu-orders`, all 11 links in Arabic (37 to 47) and English (48 to 58);
- `dashboard-menu-products`, all 14 links in Arabic (59 to 72) and English (73 to 86).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-19`).

**Placed:** 86 entries on capabilities, in 95 lines; 0 `new`; 0 `out`.
- Nine entries take two lines: 5 (المتجر وقنوات البيع), and the four links whose page is itself two things, in both languages: Pixels & feeds (8, 23), Abandoned carts (9, 24), Campaigns (13, 28) and Categories & options (61, 75).
- Supports: 95 `core`. No `own-service`, `extension-point`, `outside` or `shows`.
- No scope, no filler, no quality on any line (the rules below say why).

## What I read

- The brief and what it names: the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register's rows for the four structures (and `dashboard-nav`'s); `index/ledger-summary.tsv` and `index/ledger/nav-page.tsv`; `show --meta` and the selection rows; the rulings, their last section included; B-extent's "Cells and evidence" and "Conventions from the dry run".
- **The earlier batches first,** each with its coordinator's check: SA-17's and SA-18's notes and placements (the rest of `dashboard-main-navigation`), SA-20's (the reports and store-channels menus, `dashboard-nav`), SA-21's and SA-22's (the nav's sections, the segments, the tools and more menus). Then every earlier line on each of my addresses, joined through `held/salla/entries.tsv`: the routes (SA-7, SA-11, SA-12, SA-14), the edu rows (SA-15), the gates (SA-29, SA-32, SA-33); and SA-4's and SA-23's lines, for how the ruling after SA-4 treats one element in two entries.
- **The sources:**
  - `dashboard-main-navigation/merchant@ar/` and `merchant@en/` `items.jsonl` lines 128 to 133, and `merchant@ar/source.html` (the top bar: the link to / and five `button.nav-button` in `li.has-sub`, each holding an empty `div.header-dropdown`);
  - the three menus' `merchant@ar/` and `merchant@en/` `items.jsonl`, `meta.json` and `source.html` (the open `div.header-dropdown`, links only);
  - run `20261008T113513Z-dashboard-menus`: `actions.jsonl` (steps 1 to 24), `steps/011`, `012`, `013`, `019`, `020`, `021` and `022.text.txt`, and its run note in `index/run-notes.tsv`;
  - `dashboard-nav/prod/source.json`, only to list what the rendered menus leave out (below).
- **The model:** `held_entries.py cells` for every capability a line names, and for the leads whose cell holds nothing (CM-ORD-015, CM-CNT-002, CM-MIG-006); the full notes of the capabilities whose printed notes were cut (`merged/capabilities.tsv`); `caps --terms` for the entries no lead named (Home; الرئيسية; Order settings; إعدادات الطلبات; Product settings; إعدادات المنتجات; Store Summary; ملخص المتجر), which found CM-ANL-003, CM-ORD-001 and CM-CAT-001, the earlier lines' capabilities.

## The rules my lines follow

SA-17's, SA-18's and SA-20's rules, kept where the things are the same:
1. **A menu's link takes the capability of the earlier lines on the same address.** Every address of my three menus was placed before, and every batch placed it on the same capability: the mega-menu's link (SA-17, SA-18), the nav item (SA-20), the segment (SA-21, SA-22), the route (SA-7 to SA-14), the edu row and the gates (SA-15, SA-29, SA-32). Each reading names the mega-menu's entry and the nav item's. The one exception is SA-15's edu row for `/products/quantities/bulk` (CM-INV-002), which five later batches set on CM-INV-001; I kept to the five.
2. **A link in Arabic and in English is one element, in two entries** (SA-20's rule 9; the ruling after SA-4): each takes the same capability, with its own words as its terms, and its reading names the other entry.
3. **A second line is for a page that is itself two things** (the ruling after SA-22), as the earlier lines gave the same four links: Pixels & feeds (CM-MKT-009, CM-CHN-004), Abandoned carts (CM-CHK-007, CM-MKT-022), Campaigns (CM-MKT-005, CM-MKT-007), Categories & options (CM-CAT-003, CM-CAT-002). Both languages' entries take both lines (see "couldn't tell" for أدوات التتبع). SA-20's third line for Pixels & feeds (CM-MKT-010, by the nav item's gate `salla-ads`) isn't taken: the rendered entry holds no gate.
4. **`supports`: `core`,** each link Salla's own admin section, as the cells hold them. No link here is one SA-20 made `shows` (Multi Market, Import from platforms, Blog, Souq Eljomla): the rendered menus leave all four out.
5. **No scope.** The menus' entries carry none (SA-20's rule 3). They are the Basic merchant store's, which each reading names from its own step's text ('بيسك' or 'Basic').
6. **The top bar's five buttons are containers** (rule 3, M-13), each over the menu it opens on hover: its `li.has-sub` holds a `div.header-dropdown`, and the run's steps 11 to 15 and 20 to 24 hold each one open. Each goes on the capability its title names, as SA-21 placed the nav's top-level sections of the same titles and SA-17 and SA-18 the mega-menu's group headings: الطلبات CM-ORD-001, المنتجات CM-CAT-001, التسويق CM-MKT-005, المتجر وقنوات البيع CM-SFR-001 and CM-CHN-001 (its title names two things, M-6), التقارير CM-ANL-001. None is a title that names only a grouping, so the ruling after SA-28 doesn't make it `out`. A button has no address, so none takes a second line. The nav sections' permission lists, which gave SA-21 more lines (product_sorting_edit, currency_setting_edit and the others), aren't in the rendered buttons.
7. **Home (الرئيسية, 1) is a link to one page,** the dashboard's home: CM-ANL-003, as SA-20 placed the nav item Home at / and SA-33 the plan gate of /.
8. **The settings links** (إعدادات الطلبات, إعدادات المنتجات, 38, 49, 60, 74) open a drawer over the home page, the settings centre's sections Orders (SA-E-9edb8f0c) and Products (SA-E-b93ad281), which SA-48 to SA-63 hold. They take the cell that cites the link, CM-ORD-001 and CM-CAT-001, as SA-17 and SA-20 placed them; each reading names the settings-centre entry.

**Leads set aside** (each reading names the one it sets aside):
- by a common word: CM-CHK-008 (link, طلب, شراء), CM-PAY-032 (link, order, عميل), CM-RET-002 (order, status), CM-OPS-004 (status), CM-CHK-002 (cart, السلات), CM-ANL-002 (coupons, categories), CM-PTN-004 (invoice), CM-CAT-006 (tags), CM-SFR-002 (editor), CM-MKT-005 (campaigns, التسويق), CM-TRU-003 (audit), CM-API-001 and CM-PLN-001 (advanced), CM-DVT-003 (stores), CM-POS-001 (retail), CM-CUS-001 (customer, العملاء), CM-PLN-006 (wallet), CM-MKT-001 (promotion), CM-CHK-001 and CM-SFR-012 (checkout), CM-AIA-003 (SEO, تحسين), CM-PTN-005 (the influencers' address), CM-MKT-013, CM-PTN-008 and CM-PTN-009 (affiliate, عمولة);
- a parent where the entry names the narrower thing: CM-MIG-001 (التصدير) for the export templates (CM-MIG-003); CM-INV-001 for the inventory audit (CM-INV-003, as SA-17 and SA-20) and the transfer; CM-ORD-001 for Bulk status update, by the app's name in its address;
- the leads whose cell holds nothing: CM-ORD-015 (an order's payment status, by bulk, status, update), CM-CNT-002 (custom data, by custom fields: its note keeps Salla's custom fields apart), CM-MIG-006 (the store's configuration, WooCommerce's Blueprint, by export and import).

## New things

None. Every entry's thing is a capability the model holds, and its cell already cites the link.

## Entries I couldn't tell, and what would settle each

- **8, أدوات التتبع: two lines or one.** The Arabic words name the tracking tools, the pixels (CM-MKT-009); only the English label of the same element, 'Pixels & feeds' (23), names the feeds (CM-CHN-004). SA-4's practice gave a thing only one language names a line on that language's entry alone (its 'multiple stores' and 'teams' went on the English entry only). The address rule and SA-18, which gave the mega-menu's link of the same Arabic words both lines, give it both. I followed SA-18 and the address, since the page is itself two things. The alternative is CM-MKT-009 alone on 8. Both cells are `core`, so no cell changes either way. A ruling on whether a second line follows the page or the words would settle it for every two-language menu.
- **6, التقارير: CM-ANL-001 or CM-ANL-002.** The title is CM-ANL-002's term, the lead. The menu it opens holds the three children of CM-ANL-001: Store performance, Smart analytics and Reports (SA-20). I placed it on the parent, as SA-21 placed the nav section and SA-18 the mega-menu's heading.
- **67 and 81, جرد المخزون / Inventory audit: CM-INV-003 alone.** CM-INV-001's cell cites the same link (Inventory audit, /products/quantities) beside CM-INV-003's. I kept to SA-17 and SA-20 (the stocktake, the narrower thing). A second line on CM-INV-001 is the alternative, if the coordinator reads the audit page as the quantities' page too.

## A structure whose items and sources disagree

None: each entry's text matches its `items.jsonl` line, and each `items.jsonl` matches its `source.html`. Remarks:
- In the menus' `source.html`, Order settings and Product settings carry `aria-current="page"`, which `items.jsonl` leaves out. The run stood on the home page, whose address the settings drawers share; it states nothing of the link.
- In the main navigation's `source.html`, the top bar's link to / carries `aria-current="page"` and `active`, for the same reason. The five buttons have no accessible name, as the run note says, so the run held each one open by its `li.has-sub` index (`actions.jsonl` steps 11 to 15, 20 to 24).

## Differences between the dropdown menus, the mega-menu and the nav's data (for the coordinator)

- **Bulk status update** (40, 51) is a link in the Orders menu, to `/@salla.sa/ui-merchant-orders,UpdateOrdersStatus`, the address the nav's data gives (SA-20). The mega-menu renders it as a button with no address (SA-17's SA-E-ec345eb2).
- **Salla Ads** (7, 22) links to `/marketing/ads/v2/dashboard` in the Marketing menu, as in the nav's data. The mega-menu links to `/marketing/ads/dashboard`, the address CM-MKT-010's cell cites (SA-18 found the same difference).
- **'Promotional offers'** in the English Marketing menu is 'Promotional Offers' in the mega-menu, as the register says. The Arabic is the same in both.
- **The menus give no quick actions;** the mega-menu gives them under several links (SA-17, SA-18).
- **What the rendered menus leave out** is what the mega-menu leaves out (SA-17, SA-18): the Products menu lacks the nav's Multi-Warehouse Management and Multi Market (`/localization`) and Import from platforms (`/products/importer`); the Marketing menu lacks Blog (`/marketing/blog`). Their features are `multi-warehouse-link` (released on the demo store alone, SA-17), `multi-countries-link`, `products-importer` and `store-blog`, each `released: false` in the Basic store's list (`structures/salla/dashboard-features/merchant@en/items.jsonl` lines 565, 564, 142 and 429). The Orders menu holds all 11 of the nav's Orders items.
- **The order:** each menu lists its links in the nav's data's order and the mega-menu's.
- Customer wallet and Reorder Reminder have a leading slash here, as in the mega-menu; the nav's data writes them without one (SA-18).

## For the second stage: what the sources state that no entry holds

- **The store's setup tasks in Arabic,** for CM-ONB-004, beside the English SA-20 noted from step 14. `20261008T113513Z-dashboard-menus/steps/022.text.txt` lines 27 to 40 (the same texts in `steps/020.text.txt` lines 23 to 36 and `steps/021.text.txt` lines 26 to 39), with the progress '7/8': 'واصل خطواتك الأولى لتدشين متجرك 🚀', 'هوية المتجر', 'رقم خدمة العملاء', 'دومين المتجر', 'إضافة أول منتج', 'موقع استلام الشحنات', 'تصميم المتجر', 'تفعيل سلة بوينت', 'تخطيتها', 'فعِّله الآن', 'توثيق المتجر', 'توثيق'. The English, `steps/013.text.txt` lines 27 to 40: 'Continue setting up your store 🚀', 'Add your branding', 'Add a support number', 'Set up your domain', 'Add your first product', 'Set your pickup location', 'Design your store', 'Set up Salla Point', 'Skipped', 'Set up now', 'Verify your store', 'Verify'.
- **The top bar's other texts,** the same steps' lines 23 to 26: the merchant's name 'Hamza', the plan 'بيسك' / 'Basic', 'ملخص المتجر' / 'Store Summary' (SA-21's SA-E-e0115560 holds it) and 'مشمر' / 'Mushammir' (the AI assistant's panel, which SA-7 read).

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that already holds `core`.
- **`NOTE` line 27, `core` on a product named with the platform's brand (Salla Ads, 22):** `core` by Salla's own dashboard link, the cell's own Salla Ads, as SA-18, SA-20, SA-22 and SA-32 placed the item and the address. The brand names no maker, and `core` needs none. The checker doesn't flag the Arabic line of the same element (7, إعلانات سلة), which is placed the same way.
- **No container note,** though the five buttons are containers (rule 6): nothing in their structure has them as its `parent`, since their menus are structures of their own.
- **No `NEW` line.**

## Problems with the brief or the script

- **The ruling after SA-4 and the address rule can pull apart** on a link whose two languages name different things (8, above). The brief says either language is the platform's statement; SA-4 applied it per entry, SA-18 per element.
- **The selection holds the main navigation in Arabic only,** as SA-17 found, so the top bar's English labels (Home, Orders, Products, Marketing, Store & Channels, Reports) are only in the readings. The menus are held in both languages, so their terms are in both.
- **The checker's brand note reads English only** (above): it flags 'Salla Ads' and not 'إعلانات سلة'.

The checker's last line, for SA-19: `86 of 86 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes.** Every link keeps the capability earlier batches gave its address, as the agent found it.
- **Entry 8 keeps both lines.** A second line follows the page, not the link's words (the ruling after SA-19), as SA-18 placed the same Arabic link.
- **Other points stand as placed:**
  - the Reports button on CM-ANL-001, the parent its menu's three children share;
  - Inventory audit on CM-INV-003 alone;
  - Salla Ads `core`: the brand names no maker, and `core` needs none.
- **The checker's limits are noted and not changed:**
  - Its brand note reads only the English brand. سلة is also the word for a basket, so a note on it would flag every abandoned-cart and cart line.
  - Its container note doesn't reach the top bar's buttons, whose menus are other structures.
- **Lead for the second stage:** the store's setup tasks in Arabic (`steps/022.text.txt`, lines 27 to 40), for CM-ONB-004.
- **Cost:** 17.5 million tokens over 79 requests, about 203,000 an entry. That is the most per entry so far, for a batch that changed no cell. Most of its requests looked up how earlier batches had placed the same addresses: 43 searches of the placements. The coordinator has added `held_entries.py earlier`, which prints those lines for a chunk in one call, and the brief's "How to work" now names it.
