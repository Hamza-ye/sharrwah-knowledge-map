# SH-62: notes

**Batch:** Shopify, `editions-page-data`, 84 entries: Summer '25 (www.shopify.com/editions/summer2025) from its Shop app section to its developer Growth cards, in observed-sh at `e38dc17e3`. Effort `high`.

**What I read:** the brief; the evidence map; observed-sh's `README.md`, `docs/READING.md` (runs, structures, indexes, limits), `docs/GAPS.md` (Published), `structures/README.md`, the structure's `REGISTER.tsv` rows and `selection.tsv` row; B-extent's "Cells and evidence" and "Conventions from the dry run"; the digest `held/rules/editions-page-data.md` whole; `review-H-rulings.md`, its last section, with the ruling after SH-43, which the coordinator sent during the run. The digest sent me to four batches' notes for cases, and I read only those lines: `notes-SH-58.md` (E66 to E68, lines 67 to 71), `notes-SH-59.md` (E71 to E74, lines 108 to 111), `notes-SH-60.md` (E79 to E85, lines 50 to 64) and `notes-SH-61.md` (E95, lines 94 to 96). Earlier batches' lines were read by `earlier`, `makers` and a grep of their placements for a twin or a precedent, each cited by its entry id in the reading.

**Count:** 84 entries; 78 on capabilities only, 4 on capabilities with a new thing, 2 `out`. 145 lines: core 81, shows 18, own-service 17, extension-point 16, core;extension-point 9, own-service;extension-point 2, out 2.

## The ruling after SH-43, applied

The coordinator's message: an app or a separate product with no maker statement held is `shows` on its feature's capability, the maker a gap, whatever its name, replacing E89 and rule 19's 'or one with no maker named'.
- **SH-E-3febc064** (NetSuite ERP connector, `apps.shopify.com/oracle-netsuite`): CM-PAY-028 `extension-point` changed to `shows`. `makers` holds no statement for NetSuite.
- **SH-E-34d0a6d8** (pick lists through the Shopify Order Printer app): CM-ORD-009 changed from `core` (the digest's rule 13, 'core, the maker a gap') to `shows`, since the ruling replaces that wording too and names Order Printer among the lines aligned at the amendment. The card links the App Store's listing, not an admin page, and its title's 'in admin' names no route or section.
- **SH-E-78837e45** (data imported from other platforms, `apps.shopify.com/store-migration`, the Store Importer app SH-43 placed): placed by the ruling from the start, CM-MIG-005 `shows`. `makers` holds nothing for Store Importer or store-migration.
- **SH-E-4f3cc545** ('More B2B-compatible apps') stays CM-B2B-001 `extension-point`: it names no app, and its link is an App Store collection (`apps.shopify.com/stories/guide-selling-b2b`), the clause rule 19 keeps. If the ruling's 'only where the statement shows a third party making it' is meant to cover a collection too, it becomes `shows`.

## New things

1. **`new:View as`** (SH-E-a12e52b6, Markets for B2B, `core`, Plus): 'preview the buyer experience using the “View as” feature in the products section'. A preview, in the admin's products section, of what a market's buyers see.
   - **Place of its own:** none held. It is a feature inside the products section, named in one card.
   - **Proposed:** domain D, area B2B, parent CM-B2B-001; or a part of CM-MKS-001, whose markets it previews.
   - **Name:** English only (the Editions are English only): View as.
   - **Searched:** View as; preview; preview the buyer; buyer experience. The checker's leads: CM-B2B-007 (the buyer's own part of the storefront, not the merchant's preview), CM-DVT-006 (a store's updates previewed before they go live), CM-SFR-002, CM-SFR-012 and CM-MKS-004, none of them a preview of a market's buyers' view.
2. **`new:Web performance dashboard`** (SH-E-45c0e61a, 'New web performance reports', `core`): SH-55's new thing, its name kept (the digest, section 4). The card also takes CM-ANL-002 `core`, since its link opens the admin's Reports.
3. **`new:Admin search`** (SH-E-7a895093, 'Dedicated settings search', `core`): SH-36's new thing, its name kept. I wrote `core`, the platform's own search, where earlier lines wrote `shows`. The digest leaves the support to `held/new.tsv`. The card also takes CM-SRF-001 `core` for 'the Shopify mobile app'.
4. **`new:PIM systems`** (SH-E-0f09acf4, Shopify Collective developer docs, `extension-point`): 'Integrate Shopify Collective with your ERP and third-party PIM systems using new developer documentation'.
   - **Place of its own:** none held. It is named in one card.
   - **Proposed:** domain G or B, beside CM-PAY-028 (accounting and ERP integrations), whose thing is the store's sales and finances, not its product information. CM-PAY-028 could be widened to the merchant's business systems.
   - **Name:** English only: PIM systems.
   - **Searched:** PIM; product information; product information management; product data; catalog sync; product sync; supplier systems. Only CM-CHN-004 (channels' product feeds) answered, a homonym.

## Rules I followed that the digest doesn't hold, from E96

- **E96. An app's sync or import moves the platform's records, and the records take no line.** NetSuite's 'companies, orders, PO numbers, and payment terms' (SH-E-3febc064) and the Store Importer's 'products, customers, and inventory' (SH-E-78837e45) are what the app moves. They take no line on CM-B2B-002, CM-ORD-001, CM-PAY-008 or CM-MIG-001. This is E81's first sub-rule, held for any app, not only the platform's own.
- **E97. The Shopify mobile app's own navigation is CM-SRF-001 `core`** (SH-E-78f28717, 'fewer taps, clearer menus, and redesigned headers'). The ruling after SH-37 makes the web admin's frame no capability's thing, and SH-E-df010e0a (loading) and SH-E-de47a2b3 (back buttons and breadcrumbs) are `out` by it. The mobile app is itself a capability's thing (CM-SRF-001, the admin's mobile client), as SH-51 placed its improvements (SH-E-9e07d217).
- **E98. Guidance inside an admin flow is the flow's capability, not a guide.** 'Connecting third-party domains guide' (SH-E-3efadd80) is 'step-by-step guidance and real-time feedback during setup', in the domain settings its link opens. It takes CM-SFR-008 `core` and no CM-ONB-003 line: rule 39's guides are the platform's guides and help.
- **E99. A 'Get notified' sign-up for 'email updates about this feature', with no docs or admin link, is read as not yet offered: `shows`** (SH-E-5abe5931, the Global Shopify Catalog, beside 'Global Cart (coming soon)'). SH-58 read the Hydrogen Visual Editor's sign-up so (SH-E-6d96e871), but its words said 'will be available soon'. A thing the same card links to its own docs keeps its own support: Checkout Kit, CM-CHK-001 `core`.
- **E100. A developer guide's topics take `shows`, as a merchant guide's do (rule 39).** The AI-first Hydrogen Cookbook's recipes for Bundles, Combined Listings, Subscriptions and Markets (SH-E-271b09ae) give CM-SEL-006, CM-CAT-008, CM-SEL-001 and CM-MKS-001 `shows`. The cookbook is CM-DVT-001 `core`, and Hydrogen CM-SFR-011 `core` (E85).
- **E101. A kind of developer named as the condition is the scope, as E65 has a kind of store.** 'Developers with Built for Shopify status get priority review' (SH-E-fb94d7b6) takes the scope 'Built for Shopify'. A claim about such apps ('61% higher CTR on Built for Shopify apps', SH-E-fa113bab) is no scope.
- **E102. Shop's own features stand on their capabilities, `own-service`, as rule 11 has its sign-in and reviews.**
  - Shoppers' 'collections of saved products' (SH-E-f45e75e6) are CM-LOY-005, beside CM-CHN-002.
  - Shop's package tracking (SH-E-61942060) is CM-SHP-017, beside CM-CHN-002. Its 'easy access to pay customs' is CM-TAX-008 `shows`: the buyer pays, and no collector is named.
  - Store credit 'in the Shop app and in checkout' (SH-E-6f7bd347) follows E95: CM-LOY-001 `core`, CM-CHN-002 `own-service` and CM-CHK-001 `core`. Its 'loyalty points' are CM-LOY-004 `shows`: no programme or app that issues them is named.
- **E103. Order value limits set in Checkout Blocks are CM-CHK-005, `own-service`** (SH-E-fc2d55e0), as CM-ORD-010's note sends Shopify's order limits to CM-CHK-005. The card's 'only B2B customers' takes CM-B2B-001 `own-service`: E78's support of the B2B thing shown, here a first-party app's.
- **E104. A carrier preference card takes the carriers' capability and the route its link opens.** 'Carrier preferences in settings' (SH-E-2bec1599) is CM-SHP-015 `core`, the store's choice of carriers in its settings. Its link, `settings/shipping/carrier-services/create`, is the route Manage preferred carriers, which CM-SHP-004 cites as `core` (SH-S-7133), so it takes CM-SHP-004 `core` too.

Rules the digest holds, applied where a reading may want them checked:
- **E80, each item of an exhaustive list:**
  - SH-E-12db02e4's shipping, local delivery, in-store pickup and pickup points: CM-SHP-001, CM-SHP-008, CM-SHP-007 and CM-SHP-019, with CM-INV-005 for the location;
  - SH-E-feeb7336's sales reports and taxes: CM-ANL-002 and CM-TAX-001;
  - SH-E-e4c2aa8d's subscriptions and pre-orders: CM-SEL-001 and CM-SEL-005;
  - SH-E-a12e52b6's catalogs, currency and theme customizations.
- **The ruling after SH-34's second line per thing:** SH-E-72334c3d's three carriers each take a CM-SHP-002 `core` line and a CM-SHP-015 `shows` line (rule 42), each with its own country and filler.
- **Rule 4, a twin's capabilities kept:**
  - SH-E-a12e52b6 keeps Summer '24's SH-E-cceea16b's four capabilities, now `core` ('Markets now available for B2B').
  - SH-E-fa113bab keeps SH-59's SH-E-14e13b40.

## Entries I couldn't tell, and what would settle each

1. **SH-E-f45e75e6, CM-LOY-005 `own-service`** (CHANGES). Is a shopper's cross-store collection of saved products in Shop the wishlist capability, whose cell holds a store's wishlist apps? The coordinator's reading of CM-LOY-005's scope would settle it.
2. **SH-E-e4c2aa8d, CM-SEL-005 `core`** (CHANGES). The admin now edits orders that contain pre-orders. Does the platform's handling of pre-orders' orders support `core` on pre-orders, whose Shopify cell holds only Pre-order apps? A held statement of Shopify's own pre-order purchase options would settle it. The card's help page, `purchase-options/subscriptions/manage-subscriptions/manage-subscription-orders`, is outside the sources, and I didn't read it. If the line should only name the thing, it is `shows`.
3. **SH-E-fc2d55e0, CM-B2B-001 `own-service`** (CHANGES). Checkout Blocks' limits 'for all customers, or only B2B customers'. Rule 46 gives the line, and E78 its support. If a first-party app's B2B feature should stay out of CM-B2B-001's supports, the line goes.
4. **SH-E-78f28717, CM-SRF-001 `core`** (E97). If the ruling after SH-37 covers the mobile client's own frame, the line is `out`.
5. **SH-E-5abe5931, `shows`** (E99). Whether 'Get notified' alone states that the Global Catalog isn't offered. If it doesn't, the catalog's line is CM-AIA-005 `extension-point`, applications and agents built on it.
6. **SH-E-2bec1599** (E104). Its help link is under `shopify-shipping/shipping-labels/preferred-carriers`, so the carriers meant may be the labels' only. That would add CM-SHP-002 `core`. I put the address in the reading only (rule 53).
7. **SH-E-61942060, CM-TAX-008 `shows`.** Whether 'easy access to pay customs' is a feature of its own or a part of the tracking (CM-SHP-017).
8. **SH-E-4f3cc545** (above): `extension-point` by the App Store collection, unless the ruling after SH-43 reaches collections.

## Leads for the second stage, with no line

- **CM-MKT-023** (product recommendations) for Shop's 'personalized recommendations' in its home feed (SH-E-5e0c5e57) and Collective's supplier recommendations (SH-E-e1c1a469). Both are the app's own, not the storefront's, as SH-59 read Shop's feed (SH-E-76b709c7).
- **Swatches and subscriptions** on Shop's mirrored product pages (SH-E-5e65c62f), left in CM-CHN-002's line by E81.
- **Barcode scanning** (SH-E-ddd96118). No capability holds it as such (CM-CAT-015 is Zid's barcode printing), so it stays in CM-INV-006's line.
- **Shopify Scripts**, which 'migrate away from scripts' leaves (SH-E-3736cc84). No capability holds them.
- **CM-OPS-005** (store logs) against Flow's run logs (SH-E-d0ce4da0), which are Flow's own.
- **CM-AIA-004** (AI connector to the store) against the Shopify.dev MCP Server and 'our Assistant via MCP' (SH-E-0d7af8a7, SH-E-87ff4bd4), which serve the developer's coding environment, not a store.
- **CM-DVT-006** (staging) against 'an isolated environment' for app code (SH-E-f5ffe268).
- **CM-CHN-001's Buy Button** against Storefront Web Components (SH-E-64bfbf00), placed on CM-SFR-011 as a site the merchant builds.
- **QuickBooks** (accounting, CM-PAY-028) in SH-E-4f3cc545's list, which ends 'and more', so it takes no line (E80).
- **The Horizon theme** in SH-E-9e1d9c1c, a condition on the store's own setup, in the reading.
- **What Storefront MCP's agents do** (search, carts, checkout; SH-E-7b683569): the store's things they act on, with no line.

## The structure and its sources

I found no disagreement between the items and the renderings. Two points of the source's text:
- SH-E-ef58d573's `title` holds ASCII double quotes ('Send HTTP request'), which a placements row can't hold, so its terms take the `headlineTitle`'s “Send HTTP request”.
- SH-E-1ce9fb95's 'metobjects' is the platform's own spelling.

## Problems with the brief, the digest or the script

- **The digest's rule 8 says the free themes are `core` on CM-SFR-001 and CM-SFR-007.** CM-SFR-007 is announcement bars, banners and pop-ups. SH-53's lines put the free themes on CM-SFR-001, and only a free theme's announcement bar on CM-SFR-007 (SH-E-8ca9faf9). As written, the rule could send a theme to the wrong capability.
- **The digest's table and rule 13 still read 'core, the maker a gap' for Shopify Forms, Marketplace Connect and Order Printer.** Rule 13's added sentence and the ruling after SH-43 make them `shows`, so the table's row could say so.
- **`earlier` gave SH-E-5abe5931 a 'name headline' twin on CM-TAX-005 (SH-60:25).** It is another card, SH-E-6bb3c973, a B2B tax exemption. A reading: the key matched a heading field the two cards share, not their meaning (the brief: a twin is matched by its meaning).
- **The run cost:** my context reached about 200,000 tokens.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 84 of 84 entries, no problem.
- **The ruling after SH-43 is applied:** the NetSuite connector, Order Printer's pick lists and the Store Importer are `shows`. 'More B2B-compatible apps' stays `extension-point`: it links an App Store collection, which shows third parties' apps (rule 19).
- **The `CHANGES` stand:**
  - Flow, Collective, the Fulfillment Network (its partners `extension-point`), Checkout Blocks' order limits and Shop's package tracking are `own-service`.
  - The platform's development stores are `core`.
  - Shop's saved products on CM-LOY-005 and the pre-order edits on CM-SEL-005 are marked readings, as placed.
- **Two of the digest's lines corrected, as the batch found:**
  - rule 8 now puts a free theme on CM-SFR-001 and only its announcement bar on CM-SFR-007;
  - the first-party table now has Forms, Marketplace Connect and Order Printer as `shows`, by the ruling after SH-43.
- **The rules E96 to E104 stand** and join the digest's section 6. E97 holds: the Shopify mobile app's navigation is the app's own CM-SRF-001, not the web admin's frame.
- **The new things:** View as and PIM systems, named here; Web performance dashboard and Admin search keep their earlier names. Their supports are decided with each thing.
- **Cost:** 19.0 million tokens over 85 requests, about 226,000 an entry. The context reached about 370,000 tokens.
