# Held pass, Salla, batch SA-20: notes

82 entries (effort high), evidence at observed-sa@b0bd0b163:
- `dashboard-menu-reports`, all 3 items, in Arabic and English (entries 1 to 6);
- `dashboard-menu-store-channels`, all 10 items, in Arabic and English (7 to 26);
- `dashboard-nav`, its first 56 entries (27 to 82): Home, then the children of Orders, Products, Marketing and Store & Channels (items.jsonl lines 1 to 5).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-20`).

**Placed:** 82 entries on capabilities, in 93 lines; 0 `new`; 0 `out`. Eight entries take more than one line: 28, 41, 50, 52, 58 and 62 take two, 57 takes three and 39 takes four.
- Supports: 88 `core`, 5 `shows`. No `own-service`, `extension-point` or `outside`.
- The 5 `shows` lines are the nav items whose gate the features list holds as not released: 46 (Multi Market), 50 (Import from platforms, two lines), 70 (Blog) and 82 (Souq Eljomla).
- No filler.
- One quality, on the three Salla Point lines (13, 23, 78): `price: Free Cashier` / `price: كاشير مجاني`, from the item's tag.
- Scope only on nav items: each item's own `feature`, the route's store gate, in Salla's identifier (39 entries). The menu entries carry no scope.

**No batch has placed these three structures before.**
- `SA-21` holds the rest of `dashboard-nav` and hasn't run. That is the Reports children (`SA-E-4df9d1af`, `SA-E-add7df1f`, `SA-E-04e8eeb0`), the home segment's Store Summary (`SA-E-e0115560`), then `dashboard-nav-segments`.
- `SA-19` holds the other dashboard menus (main navigation, marketing, orders, products) and hasn't run either.
- The rules my lines follow are below, so that both can keep to them. The coordinator aligns them.

## What I read

- The brief and what it names: the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register rows of the three structures; `index/ledger-summary.tsv` and `index/ledger/nav-page.tsv` (the nav pages), with `index/ledger/feature.tsv` for the features each nav item names; the three structures' `meta.json` and selection rows; the rulings, their last section included.
- The sources:
  - for the menus, `merchant@en/` and `merchant@ar/` `items.jsonl` and `source.html` (the open `div.header-dropdown`), and run `20261008T113513Z-dashboard-menus`, `actions.jsonl` steps 14, 15, 23 and 24, and `steps/014.text.txt`;
  - for the nav, `dashboard-nav/prod/source.json` (the answer of `api.salla.dev/ui/v1/nav/prod/nav`), which holds each item's `icon`, `sort` and `id` beside what the entry renders, and the top-level items' own fields.
- Salla's earlier batches: SA-7 to SA-10 (the routes), SA-32 and SA-33 (the plan gates of the same addresses), each with its coordinator's check.
- The model: the cells of every capability a line names, and `caps --terms` for the product types (`service; خدمة; food; digital card; bundle; product type; options; size guide`).
- **To clarify only:** the features list, `structures/salla/dashboard-features/demo@en/items.jsonl`, for each nav feature's `released` and `plans`. Each reading cites it by position.
  - The ledger's `feature.tsv` joins each feature to its nav item.
  - SA-32 read the same list for the same addresses.
  - It gives the `shows` lines and the plans in `reading`, never the scope.

## Rules my lines follow, for SA-21 and SA-19

1. **A menu link or nav item is the capability whose cell already cites the same link or address.** The cells name Salla's links by path. Where SA-7 to SA-10, SA-32 or SA-33 placed the same address, I kept to their capability: /localization (CM-INV-005 for Multi-Warehouse Management, CM-MKS-001 for Multi Market), /products/quantities (CM-INV-003), /products/quantities/bulk (CM-INV-001), /marketing/carts (CM-CHK-007 and CM-MKT-022), /marketing/integration-tools/snapchat (CM-MKT-009 and CM-MKT-010), /marketing/campaign/retargeting (CM-MKT-005 and CM-MKT-007, SA-7's two lines), / (CM-ANL-003, SA-33).
2. **`supports`:**
   - a menu link or nav item is Salla's own admin section: `core`;
   - except where the item's `feature` is held as not released in the features list. Then it is `shows`, by the ruling on flags, as SA-32 placed the same gates: multi-countries-link, products-importer, store-blog and app_vendor;
   - a `New` badge (`isNewFeature: true`, a `جديد / New` tag) or a `Beta` tag is a release badge with no limit stated, so it stays `core`, the badge in `reading` (D1). The only exception is Import from platforms, whose gate isn't released;
   - a tag that is neither (Store design's 'Most Viewed', `visible_days: 0`) is a mark, in `reading` only.
3. **`scope`:**
   - for a nav item, its `feature`: the route's store gate, in Salla's identifier, as SA-32's rule 4 fell back to the nav feature. The plans the features list states for it go in `reading`;
   - an item with no `feature` has no scope;
   - the menus' entries carry no scope. They are the Basic merchant store's, which each reading names.
4. **Staff permissions** (`permission: [...]`) are a gate on the user. They go in `reading`, never `scope` and never a line of their own (SA-7's rule 6; the brief's rule 5).
5. **An item's `actions`** are things the item names:
   - an action that is another capability's thing takes a line there: All orders' New Order (CM-ORD-005); All products' Digital product and Digital card (CM-SEL-002), Product bundle (CM-SEL-006) and Bookings (CM-SEL-004); Categories & options' New option (CM-CAT-002); Import & export's Add a new template (CM-MIG-003);
   - an action that creates the item's own thing (New campaign, New link, Add New Page) or adds a field inside its page (Cart options' Text, Number, Select and Date fields) takes no line, and is named in `reading`.
6. **One scope per entry, with gates on actions:** All products (39) has no gate of its own. Its actions carry `product-advance-management` and `product-booking`. I left the entry's scope empty and named each action's gate in its line's `reading`.
7. **Containers** (rule 3, M-13): the menu's group label قنوات البيع / Sales Channels (12, 22, an `h3` in the dropdown) and the nav item Sales Channels (77, url `#`) go on CM-CHN-001, the capability their title names.
   - The links after it take no CM-CHN-001 line of their own: in the nav's data they are its siblings, not its children, and the heading says where they are.
   - These are Salla Point, Mobile app, Landing pages, Mahally and Souq Eljomla. Each one's capability already sits under CM-CHN-001 in the model, Landing pages and Souq Eljomla excepted.
8. **The top-level nav items have no entries of their own.** Orders, Products, Marketing, Store & Channels and Reports appear only as each child's `within` (below). I placed no line for them. A group the entry sits under gives it no line (M-6, refined).
9. **A menu link in Arabic and in English is one element, in two entries.** Each takes its own line on the same capability with its own terms (the ruling after SA-4).
10. **Leads set aside as common words or names** (none is the entry's thing):
    - CM-ANL-006 (reports), CM-APP-002 (marketplace), CM-SRF-001 (mobile app), CM-CNT-003 (landing pages);
    - CM-PAY-021 and CM-POS-002 (Salla Point, by name), CM-PLN-001 (performance), CM-PLN-004 (invoice);
    - CM-ORD-015, CM-CAT-015, CM-CNT-010, CM-PTN-010, CM-MIG-006 and CM-INV-010, each holding nothing, by name only;
    - CM-SFR-002 (editor), CM-PAY-019 (restriction), CM-SHP-007 (branch), CM-B2B-003 (retail), CM-PTN-005 and CM-PTN-009 (influencers), CM-PTN-008 (affiliate), CM-ORD-014 (reorder);
    - the many leads by a staff permission's name.

## New things

None. Every entry's thing is a capability the model holds, and the cells already cite nearly every link.

## Entries I couldn't tell, and what would settle each

- **39, All products, its actions Custom service and Food & beverages.** These are product types with their own creation address (`/products/new?type=service`, `?type=food`, behind product-advance-management), each with a description: 'Design, writing, printing, and other custom services' and 'Food products that require special shipping'.
  - No capability holds service products or food products; `caps --terms` found none.
  - I placed them in CM-CAT-001's line as kinds of the catalog product. The cell holds the plan line إضافة كل أنواع المنتجات (adding all kinds of products).
  - A field value in a creation form isn't a place of its own, so I wrote no `new`.
  - The coordinator may want them as new things if another platform gives service or food products a place.
- **39, Digital card** ('Prepaid cards or licensed subscriptions', `type=codes`). I placed it on CM-SEL-002 with the digital codes. Its child CM-SEL-003 is NFTs and holds nothing on Salla; this isn't it.
- **50, Import from platforms.** Two `shows` lines:
  - CM-MIG-001, as SA-32 placed the address;
  - CM-MIG-005, since its words name the import from other platforms, as SA-7 placed `/persona/scrapper` and SA-3 and SA-4 placed the FAQ on moving a store. observed-sa's `docs/GAPS.md` holds the Shopify import form under Products > Import from platforms > Shopify.

  The alternative is CM-MIG-001 alone. The feature's release would turn both lines to `core`.
- **57, Pixels & feeds.** Three lines: CM-MKT-009 (the pixels, its cell's link), CM-CHN-004 (the feeds, which CM-MKT-009's note leaves to it, and whose terms hold Pixels & feeds) and CM-MKT-010 (its gate salla-ads, as SA-32 placed the address).
  - Its path opens on Snapchat, `/marketing/integration-tools/snapchat`. I wrote no filler, since only the path names Snapchat, and SA-32 wrote none for the same address.
- **62, Campaigns, gate `sweply`.** sweply isn't in the features list. SA-7 placed this route `core` on CM-MKT-005 and CM-MKT-007, as a route rendering the embedded page `/campaign`, with no CM-APP-007 line (only `/marketing/campaign` embeds the app sweply). I kept both lines.
- **55, Retail stores.** Its feature, manage-products-by-branches, is of type `app`, with an app id (503213483) and an install link, and names no maker: a gap. It is `core` on CM-INV-005 by its own nav item, as SA-32 placed it. Whose app it is would settle whether it also takes CM-APP-001 or CM-APP-011.
- **81, Mahally:** released (plus, pro, special) but enabled on none of the three stores, the Pro one included. `core`, the value in `reading`, as SA-32 found.
- **13, 23, 78, Salla Point's tag 'Free Cashier' / 'كاشير مجاني'.** I wrote it as a price quality, as the model records Zid's 'Completely free Zid POS - two cashiers' on CM-POS-001. The alternative is a mark in `reading` only.

## A structure whose items and sources disagree

- **The menus' `text`** joins a link's title and its tag with no space ('Store designMost Viewed', 'سلة بوينتكاشير مجاني'). In `source.html` the tag is its own `s-tag` element inside the link, and `aria_label` holds the title alone. I took the title from `aria_label` and the tag from the source.
- **The rendered Store & Channels menu leaves out Souq Eljomla,** which the nav lists last under Store & Channels. Its gate app_vendor isn't released (features list, position 439). The register says the nav holds items a store's menu doesn't show.
- **Sales Channels is a heading in the menu but a sibling in the nav's data.** In `source.json` it is the sixth child of Store & Channels, url `#`, beside the items that follow it. The menu renders it as an `h3` over them.

## What a source states that no entry holds (for the second stage)

- **The top-level nav items** (`dashboard-nav/prod/source.json`, `data[1]` to `data[5]`) hold the dashboard's own sections, each with its own address:
  - Orders (`/orders`), Products (`/products`), Marketing (`/marketing`, `options.visibility: desktop`), Store & Channels (`/channel`, `visibility: desktop`) and Reports (`/reports/performance`);
  - the Arabic labels الطلبات, المنتجات, التسويق, المتجر وقنوات البيع and التقارير;
  - each section's permission list.

  No entry holds them. The selection's rule `nested:children` gives each child an entry and the parent none. They are containers that would go on CM-ORD-001, CM-CAT-001, CM-MKT-005, CM-SFR-001 or CM-CHN-001, and CM-ANL-001 (a reading).
- **Store & Channels' permission list** names permissions that none of its children holds: currency_setting_edit, languages_management, store_setting_edit_basic_info, advertisements_browse and advertisements_management. Products' list names product_sorting_edit. These are leads for the store's currencies and languages (CM-MKS-006, CM-MKS-008), its store details (CM-ACC-006), the storefront's advertisements (CM-SFR-007) and product sorting. Which page each opens isn't stated.
- **The Reports parent's permissions** name every report (report_sales to report_selling_channels). SA-21's Reports children carry the same list.
- **The menu run's step 14** (`20261008T113513Z-dashboard-menus/steps/014.text.txt`, lines 20 to 37) shows the merchant store's plan, 'Basic', and its setup tasks: 'Continue setting up your store 🚀', 'Set up Salla Point', 'Verify your store'. These are leads for CM-ONB-004, which SA-7 to SA-9 placed from the routes.

## The checker's lines, read again

- **No `CHANGES` line:** every line falls on a cell that already holds `core`, or adds `shows` beside it.
- **`NOTE` lines 21, 64 and 90,** core on a product named with the platform's brand (Salla Point, Salla Ads): each line is `core` by Salla's own dashboard link and its cell's link, not by the product's name. No maker is stated for either, and none is needed for `core`.
- **No `NEW` line.**

## Problems with the brief or the script

- **One scope per entry, with gates on an item's actions** (39): see rule 6 above. The brief says an entry's lines share one scope. Its lines on CM-SEL-002, CM-SEL-006 and CM-SEL-004 rest on actions gated by features the item itself doesn't carry, so their gates are in `reading` only.
- **The parents of a nested structure have no entries** (above). Five dashboard sections of Salla's own navigation reach no entry. A rule that also gave each parent an entry would place them.
- **The brief doesn't name the features list** among what may clarify an entry. Without it, a nav item's `feature` can't be read as released or not. SA-32 read it as a source of `plan-gates`. I read it to clarify `supports` only, and cite it in each reading.

The checker's last line, for SA-20: `82 of 82 entries placed; 0 problems` (after this file was written).
