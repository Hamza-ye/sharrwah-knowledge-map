# SH-32: Shopify's Help Center notes, the third 80 (high)

**What the batch is.** 80 entries of `help-notes` (observed-sh at `e38dc17e3`, `structures/shopify/help-notes/help.shopify.com@en-md/items.jsonl`, lines 2579 to 3297): the asides of the English `.md` pages whose class is `note note-plan` (44), `note note-staff-permissions` (33) or `note note-beta` (3), as `selection.tsv` reads them, from the Launchpad page (`promoting-marketing/create-marketing/launchpad`) to the Tap to Pay on iPhone page (`sell-in-person/shopify-pos/payment-management/tap-to-pay-iphone`). I kept to SH-30's rules H1 to H13 and SH-31's H14 to H20, with H18 as the coordinator narrowed it, and to the rulings in `review-H-rulings.md`'s last section, among them the ruling after SH-43, which came in during the batch (problems, 3).

Each item holds the aside's heading, text and `html`. Its source is the page's record in the run `20260930T003703Z-help-en-md`. I read the page where the note's own words left its feature, its scope or its maker open: 32 pages, cited in the lines that rest on them as `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz@<offset>`. Most of them are POS pages whose only note is 'This feature is available only for locations that are currently on the Shopify POS Pro subscription', whose feature only the page's title and first paragraph name.

**Count.** 86 lines over 80 entries:
- 79 entries on capabilities alone, 1 with a `new` line beside its capability line (SH-E-cb64a6a1, `new:Staff sales attribution`), no `out`;
- supports: `core` 70, `shows` 13, `own-service` 3.

## The rules I added (H21 to H23, for the coordinator to check)

**H21. A note on a page whose plan note states the page's feature for a plan takes that plan as its scope, where its own thing is that feature or a part of it.** This extends H16 (a staff note takes the release state its page states) from a release state to a plan. H14 still holds for a 'Plan requirement' note that names no plan and has no such sibling.
- The cases, all `POS Pro`, each citing its page's plan note by id:
  - staff permission notes: SH-E-d42aaffc (required checkout information), SH-E-f0d5ea87 (cash register sessions), SH-E-7251cbf1 (receipt customization settings), SH-E-e64574be (stock counts, in the section of the plan note), SH-E-e1943440 (receiving transfers), SH-E-607da1d6 (admin discounts on draft orders), SH-E-0c847a43 and SH-E-83091f20 (saved carts), SH-E-d2e515ab (pickup in store orders), SH-E-135a7de6 (ineligible returns);
  - an early access note: SH-E-bbc47079 (Stocky's Store Profit report).
- Not applied where the plan note stands in another section about another thing: Quick count (SH-E-f4287f0a) has its own section on a page whose plan note is about stock counts, so it takes no scope.
- The alternative is no scope on these 11 lines, by H14.

**H22. A first-party app's feature on a page that states the app's end, captured after that date, is `shows`, the plan its scope.** Seven Stocky pages carry, beside their plan note, an aside of class `note` (not selected, so no entry): 'The Stocky app will no longer be available after August 31st, 2026.', asking merchants to move to Shopify's Inventory management features. The pages were captured on 30 September 2026.
- So the feature is stated unavailable where it is listed: `shows` (the ruling after WC-5), as the changelog digest's rule 30 places a retired feature. Stocky's maker statement (SH-E-5b89aa16) makes its features `own-service` while it is offered.
- The cases: SH-E-9e240157 (demand forecasting for purchase orders, CM-INV-007), SH-E-5e0e247a (stock transfers, CM-INV-006), SH-E-28cd3c51 (stocktakes, CM-INV-003), SH-E-a157e340 and SH-E-bd0c90ca (Stocky reports, CM-ANL-002), SH-E-2958ed65 (user profiles, CM-STF-002), SH-E-01c601d4 (vendors and suppliers, CM-INV-007). SH-E-bbc47079 is `shows` by H5 anyway.
- This differs from SH-30's address blocker, which the coordinator kept 'as its page of 30 September states it', because that page didn't state its end; a post did. These pages do (couldn't tell, 1).
- The receiving transfers page (SH-E-a5286894, SH-E-e1943440) names the 'Stocky Transfers POS UI extension' and states no end, so its lines are `own-service`, as SH-E-b96e9a6d's (couldn't tell, 2).

**H23. A POS Pro plan note on a POS page takes its feature's line, and a CM-POS-001 line where the feature is another capability's thing used in POS; both `POS Pro`.** This follows SH-31's SH-E-490f67bf and SH-E-f12a52ea, and the ruling after SH-70, by which a feature that comes with POS Pro takes POS Pro as its scope.
- Two lines: POS Analytics (CM-ANL-002), receipt printing options and the receipt code editor (CM-ORD-009), discount combinations (CM-MKT-001), stock counts (CM-INV-003), receiving transfers (CM-INV-006), draft orders and Email cart (CM-ORD-005), local delivery (CM-SHP-008), pickup in store (CM-SHP-007), return rules (CM-RET-003), delayed payment capture (CM-PAY-020), store credit (CM-LOY-001), staff added to a sale (`new:Staff sales attribution`).
- One line, where the feature is the POS's own: required checkout information, Ship to customer, saved carts, ship from store, ship and carry out (CM-POS-001); cash tracking (CM-POS-003).
- A staff permission note takes its feature's line only, as SH-3's role permission lines placed the same permissions (APPLY_CUSTOM_DISCOUNTS on CM-MKT-001, OPEN_CASH_DRAWER on CM-POS-003, MANAGE_SAVED_CARTS on CM-POS-001 and the like). POS is named in its `reading`.
- Where a note names the feature only as 'This feature', its feature's line has no term. The CM-POS-001 line takes 'Shopify POS Pro subscription', the words the note states.

## The new thing

**Staff sales attribution** (`new:Staff sales attribution`, `core`, scope `POS Pro`; SH-E-cb64a6a1, on the page Adding staff to a sale in Shopify POS):
- The page: 'you can add staff to the sale to credit it to the staff member who makes the sale', from the cart or the Smart Grid (@9128724). The note states it for POS Pro locations.
- It is SH-50's new thing (SH-E-ada073f2), named the same way, beside CM-POS-001, as the corrections with the changelog digest place a post that credits a sale to a staff member. SH-50 proposed domain A, area STF, under CM-STF-001; the terms it searched were 'staff attribution; sales attribution; pos staff'.
- **Place of its own:** none in this entry. The help page is a guide, and its POS role permission is held elsewhere.
- **Its support:** earlier lines on it read `core` (SH-E-ced38862, SH-E-03c207ce) and `shows` (SH-E-1c0bb5d3 and five others). I wrote `core`, the POS's released feature on POS Pro, for the coordinator to decide with the others in `held/new.tsv`.
- **The checker's leads:** CM-POS-001 takes its own line from this entry. CM-INV-005 matched only 'locations', the POS Pro subscription's unit, and CM-PLN-001 only the plan's words: no lead.
- In English only, since this batch reads no Arabic.

## CHANGES, each read again against its source

**CM-MKS-002 gains `own-service`** (line 2: the Launchpad note on its eight pages, SH-E-8f59733c to SH-E-28d3e6c2).
- **The note:** 'The Launchpad app is available only to stores on the Shopify Plus plan.'
- **The page:** 'You can use Launchpad to schedule, coordinate, and execute events, such as sales, product drops, and inventory restocks'. At an event's start and end it changes product pricing, products' availability to sales channels, inventory levels, theme customizations and scripts, and it can password-protect the store (@7388344).
- **Why CM-MKS-002:** its thing is 'scheduled changes to the live store', and its note calls a rollout 'a scheduled set of changes to the main theme, checkout and accounts pages, discounts or product catalogs'. Launchpad's events are that, for sales events.
- **The maker:** `makers` finds “We’ve made creating discount events in Shopify Launchpad easier!” (SH-E-bd544a27, October 27, 2020, area Plus): a 'we' post upgrading the app (the ruling after SH-35). No batch has placed that post yet.
- Kept, with alternatives (couldn't tell, 3).

**CM-INV-006 gains `own-service`** (lines 45 and 47: SH-E-a5286894, SH-E-e1943440, receiving transfers on Shopify POS).
- **The page:** 'Staff can receive incoming transfers from other retail locations on Shopify POS using the Transfers POS UI extension', a transfer created in the admin and displayed 'in the Stocky Transfers POS UI extension at the destination location' (@9014643).
- Stocky's extension, Stocky's maker statement held (SH-E-5b89aa16). SH-E-b96e9a6d's and SH-E-eddcf8ad's lines already give CM-INV-006 `own-service` for Stocky's transfers extension; the checker compares with the concern map's cell.
- Kept, with Stocky's end (couldn't tell, 2).

**CM-TAX-007 holds nothing and becomes held** (line 24: SH-E-464baca7, `shows`, scope Spain).
- **The note:** 'To install the Comply app, staff members must have the Manage and install apps and channels permission', in the section 'Set up the Comply App for fiscal compliance in Spain'.
- **The page** (@8870790, lines 110 to 135 of `warc_text.py`'s print): 'With Comply, Shopify POS operates in compliance with current Veri*Factu obligations in Spain'. 'It automates the generation of invoices, QR codes, and linked digital signatures, and real-time submissions to the Tax Office'. The merchant installs 'the free Comply app from the Shopify App Store', adds it to the POS smart grid and activates its Comply POS UI Assistant through POS UI extensions.
- **Why CM-TAX-007:** the capability is 'the store's tax invoices linked and uploaded electronically to the tax authority through the platform', and the cell's reading says no held statement 'reports the store's invoices to a tax authority electronically'. This one does, for POS sales in Spain.
- **Why `shows`:** no held statement names Comply's maker (`makers` finds only the verb 'comply'), so by the ruling after SH-43 it is `shows`, the maker a gap. I first wrote `extension-point`, an app through the App Store and POS UI extensions. The ruling allows that only where a statement shows a third party making it. The page shows none: its guides at help.complyapp.io are only links.
- The cell becomes held with no placement. Kept.

## The other NOTEs

- **`core` on a product named with the platform's brand** (17 lines: 3, 20, 28, 31 to 33, 38, 39, 42, 46, 58, 61, 64, 66, 71, 74, 84).
  - Line 3 is Shopify B2B, the admin's own B2B features (SH-31's line 89).
  - Line 39 is the store's discounts used in POS ('Shopify POS discounts', CM-MKT-001).
  - The other 15 are CM-POS-001 lines whose term is 'Shopify POS Pro subscription' or the smart grid's. POS is the platform's own sales channel, which the plans include, and stays `core` (the ruling after SH-55).
- **`own-service`** (3 lines): Launchpad (line 2) and Stocky's Transfers POS UI extension (lines 45 and 47), each by a held maker statement.
- **The new thing whose entry has leads** (line 57): see the new thing above.
- No container, footnote mark or app's embedded page is in the batch, and no quote was found missing.

## Entries I couldn't tell, and what would settle each

1. **Stocky's pages** (H22: SH-E-9e240157, SH-E-5e0e247a, SH-E-28cd3c51, SH-E-a157e340, SH-E-bd0c90ca, SH-E-2958ed65, SH-E-01c601d4).
   - Placed `shows` by the pages' own end date.
   - Alternatives:
     - `own-service`, as SH-30's address blocker was kept. That would add `own-service` to CM-INV-003, CM-ANL-002 and CM-STF-002 from a retired app.
     - The replacement's `core` with no scope, as H8 and H19 place Scripts. But the pages name the replacement only as Shopify's Inventory management features, except the stock transfers page, which says they 'have moved to the' admin's Transfers page.
   - Settled by: the coordinator's reading of a page that states its app's end, against the address blocker's check.
   - Stocky's earlier `own-service` lines, from the posts of 2023 and 2024 (SH-E-5b89aa16, SH-E-b96e9a6d, SH-E-22729b77, SH-E-15f4f14d and others), may want the end in their readings at Shopify's amendment.
2. **Receiving transfers** (SH-E-a5286894, SH-E-e1943440).
   - `own-service` on CM-INV-006: its page names the Stocky Transfers POS UI extension and states no end.
   - If the extension ends with Stocky on August 31st, 2026, the lines are `shows`, and CM-INV-006 doesn't change.
   - Settled by: a held statement on whether the Transfers POS UI extension outlives the Stocky app. The stock transfers page's section 'Stocky Transfers migration to the Shopify admin' (@9051943) may say.
3. **Launchpad** (line 2).
   - On CM-MKS-002, scheduled changes to the live store.
   - Alternatives:
     - CM-MKT-005, marketing campaigns, since the page sits under `promoting-marketing/create-marketing`;
     - a new thing for sales events. Launchpad has no admin route or plan line held, only its App Store listing (the page's `note-app` aside, `apps.shopify.com/launchpad`).
   - Settled by: the coordinator's reading of CM-MKS-002 beyond Rollouts' own route.
4. **The Brand settings' secondary colors** (SH-E-9595a8ff).
   - `shows` on CM-ACC-006, scope Starter: stated unavailable on that plan (the ruling after WC-5).
   - The Brand page is the router's `settings:general:brand` (path `branding`, title 'Brand', PREFERENCES), under `settings:general`, which CM-ACC-006's cell cites. No batch has placed that route.
   - Alternative: a new thing, Brand, the store's brand assets (logos, colors, cover image, slogan), which sales channels, themes and apps read through the Brand API (@7588096, line 4). It has an admin route of its own.
   - Settled by: the coordinator's reading of a sub-route of Settings > General with its own title.
5. **Multi-store data in the dashboard and reports** (SH-E-ee9c898c, SH-E-067d45f6).
   - Scope `Plus` by H15: each note's link opens the organization analytics page, whose note says 'Organization analytics are available only for stores and organizations on the Shopify Plus plan.' (SH-E-7bb217d4).
   - The ShopifyQL page states 'the Plus or Enterprise plans' for the same option (SH-E-3ac90435), kept in its own words (H20).
   - The alternative is no scope, by H14.
6. **Grow SEO** (SH-E-5eade9fb).
   - Two `shows` lines: CM-AIA-003 (AI-written SEO titles and descriptions) and CM-CNT-007 (SEO).
   - No maker statement is held, so either way `shows` (H5; the ruling after SH-43).
   - Settled by: whether a note whose app does one thing with AI takes the AI capability's line, the place's, or both (the corrections with the Editions digest: 'AI for merchants outside the admin goes on the place's capability').
7. **Delayed payment capture** (SH-E-a954ad27).
   - On CM-PAY-020, whose thing is 'authorizing, capturing and recording an order's payments'.
   - CM-PAY-021, in-person card payments, is the alternative: the capture is of POS card payments through Shopify Payments.
8. **Unverified returns** (SH-E-a07f0dc1).
   - On CM-RET-003 alone, as SH-E-af7b56a0's return line.
   - The note's 'or refund' could take CM-RET-002. But that is 'returning an order's amount', and an unverified return has no order: the post refunds it to a gift card.
9. **Stocky's user profiles** (SH-E-2958ed65).
   - On CM-STF-002: they 'restrict access to certain parts of the app'.
   - Their 'separate login details for each of your employees' are CM-STF-001's thing, the alternative.

## Items and sources

- The items agree with the pages read. Each item's `text` is its aside's text, and its `html` is the aside as the page holds it.
- As SH-30 and SH-31 found, the text sets a space between a link's words and the punctuation after them ('Shopify POS Pro subscription .', 'Starter plan , then'). My quotes stop before that space, or are split around it.
- The pages are Markdown with HTML asides, so a sentence that holds a link is not one run of text in the record ('transition to Shopify’s <a …>Inventory management</a> features'). My quotes from pages stop at a link's edge.

## For the second stage: stated on the notes' pages, held by no entry

All in `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz`, at the record and the line of `warc_text.py`'s print:
- **The Stocky app's end,** on seven pages, each in an aside of class `note` that `selection.tsv` doesn't select: 'The Stocky app will no longer be available after August 31st, 2026.' (@9031919, @9051943, @9055268, @9076900, @9089335, @9099910, @9104751; line 4 of each). This is for every Stocky line on CM-INV-006 and CM-INV-007.
- **@9051943, for CM-INV-006:** the section 'Stocky Transfers migration to the Shopify admin': stock transfers 'have moved to the' admin's Transfers page.
- **@7388344, lines 10 to 20, for CM-MKS-002:** Launchpad's event tasks: product pricing, channel availability, inventory, theme customizations, line item and shipping scripts, password protection, and its real-time analytic dashboard.
- **@7588096, for CM-ACC-006 or a new Brand thing:**
  - line 4: brand assets used 'across sales channels, themes, and apps that have integrated with the Brand API';
  - the logos, colors, cover image and slogan sections (lines 27 to 122), with the slogan 'up to 80 characters long';
  - line 33: brand assets can't be localized by market or language, and Translate & Adapt is the way to localize logos.
- **@8870790, for CM-TAX-007, CM-ORD-009 and CM-TRU-010:**
  - line 70: KassenSichV in Germany, with its TSE app;
  - lines 74 to 76: Singapore's GTO reports, which Shopify POS doesn't include, with third-party solutions;
  - lines 110 to 118: Spain's fiscalization: printed receipts that show each item's tax rate and a tax summary, no tax overrides, no partially paid or unpaid POS orders, offline payments not fiscally compliant, no bundles at Spanish locations.
- **@9214889, lines 25 to 47, for CM-PAY-020 and CM-PAY-021:** delayed capture's 15-minute window, on by default for POS Pro locations and turned off in the POS editor, not available in Germany or Italy; the payments that can't be canceled in the window.
- **@7691695, for CM-AIA-003 and CM-CNT-007:** Grow SEO's limits: no Hydrogen storefronts, up to 100 suggestions, product and collection pages only, English only.
- **@8076448, for CM-ANL-001 and CM-ANL-002:**
  - lines 1810 to 1828: multi-store queries, 'FROM ORGANIZATION' with `shop_id`, which also require the organization analytics permission;
  - lines 1904 on: the `app_events` dataset, its event names (`shopify.{category}.{event}`) and its fields.
- **@8841127, line 11, for CM-ANL-002:** the POS permission “View analytics for device's location”, which opens the Daily Sales report.
- **@9128724, for `new:Staff sales attribution` and CM-ANL-002:** sales credited per item or per sale, a staff search bar from 12 staff members, and the report 'POS total sales by staff member'.

## Problems with the brief or the scripts

1. **`earlier` found a lead for one of the 80 entries** (SH-E-5e6acfd8, by 'Shopify B2B').
   - The POS Pro notes ('This feature is available only…') and the staff permission notes ('To … , staff members must have …') key on the whole sentence, which no line cites.
   - So I grepped the placements for each feature's own words instead, several at a time: Launchpad, brand, multi-store, app pixels, App events, payment options, cash drawer, Retail markets, multiple entities, Comply, printed receipts, receipt customization, customer profile, pinned, cash tracking, register sessions, smart grid, Quick count, stock counts, Stocky, Staff sales attribution, ship to customer, custom sale, saved and recent carts, draft orders in POS, pickup in store, ineligible, unverified, Tap to Pay, store credit, delayed, ship from store, carry out, cash out, CANCEL_ORDERS and payment capture.
   - SH-3's role permission lines (ADD_CUSTOM_SALES_TO_CART, MANAGE_SAVED_CARTS, OPEN_CASH_DRAWER and the like) were the most useful leads for the staff notes. A key from a staff note's bold permission title, matched to the permission tree's titles, would reach them.
2. **The brand NOTE fires on every line whose term holds 'Shopify POS'**, 16 lines here, beside Shopify B2B's. The ruling after SH-55 already keeps POS `core`.
3. **The rulings file changed during the batch:** the ruling after SH-43, which the coordinator also sent. It moved one line, Comply's, from `extension-point` to `shows`. Launchpad and Stocky have maker statements held, and Grow SEO was `shows` already. No line of mine placed a no-maker app's feature `core`. Quick count is the POS's own extension, activated under Sales channels > Point of Sale in the admin (@8993535, lines 28 to 44), with no app to install.

## Where B-extent and the brief differ

None found in this batch.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem.
- **The `CHANGES` stand:**
  - Launchpad's scheduled events are CM-MKS-002 `own-service`, on its maker statement ('We’ve made creating discount events in Shopify Launchpad easier!').
  - Stocky's transfers are CM-INV-006 `own-service`, as the changelog already places them.
  - Comply in POS makes CM-TAX-007 held, `shows`, since no maker is held (the ruling after SH-43).
- **The rules H21 to H23 stand for SH-33:**
  - a note takes its page's plan note's plan where it is about that page's feature;
  - a POS Pro note on a POS page takes its feature's line and CM-POS-001's;
  - a first-party app's feature on a page that states the app's end, captured after that date, is `shows` (H22).

  H22 follows the principle the check after SH-30 kept for the address blocker: each page's own words govern. That page stated no end; Stocky's pages do.
- **The new thing** keeps SH-50's name, Staff sales attribution. Its support is decided with the thing.
- **Cost:** 21.4 million tokens over 101 requests, about 268,000 an entry. The context reached about 366,000 tokens.
