# SH-27: notes

**The batch:** 90 entries of three Shopify structures (observed-sh, cited at `e38dc17e3` as the entries are; read at `04de369da`). Effort `high`.
- **`dev-nav`, entries 1–54, the last 54 of its 102:** the Apps sidebar's items 11 to 44 (`structures/shopify/dev-nav/shopify.dev_docs_apps_build/`, Building blocks to Marketing and growth) and the Storefronts sidebar's first 20 (`shopify.dev_docs_storefronts/`). Both sidebars' Full index are SH-26's SH-E-69ebb72b, which stands for all three.
- **`dev-store-feature-previews`, entries 55–60, all:** the list 'Select feature preview' on the organization's store-create page (run `20261007T010009Z-journey-partner-dashboard`, step 65).
- **`document-template-config`, entries 61–90, all:** the Pick list template's editor on capture-plus, by order (step 1) and by product (step 4) of run `20261007T225846Z-journey-document-template`.

**Counts:** 90 entries: 85 on a capability, 0 `new`, 5 `out`. They make 99 lines: 94 on a capability (52 `core`, 7 `core;extension-point`, 25 `extension-point`, 10 `shows`) and 5 `out`.

**What I read beyond each entry's item, to clarify it** (the reads SH-25's and SH-26's checks accepted; each reading cites what it rests on):
- for a `dev-nav` button, its children in `dev-docs-nav`'s loader data for the same docs (`structures/shopify/dev-docs-nav/shopify.dev@2026-10-07/items.jsonl`, line 47 for the Apps docs, line 48 for the Storefronts docs), and its first page's description in `structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl`, by position;
- where a description left the thing open, the page itself in `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz`: AI and agents (`@21409058`), Analytics (`@21416260`), App quality (`@21854326`) and About marketing your app (`@24612743`);
- for the feature previews, the step's own text (`steps/065.text.txt`, `065.html`), shopify.dev's Feature previews page (`fetch.warc.gz@24315784` of the same `-shopify-dev-md` run), and `derived/eligibility-by-store.tsv` for whether a held store has the feature;
- for the document template, the run's steps 1, 4 and 10 (`.text.txt`, the preview frame `001.frame-0.text.txt`) and its `actions.jsonl`.

## `dev-nav` (entries 1–54): SH-25's and SH-26's rules, kept

- **R26.1, headings:** Building blocks, Design and quality, App surfaces, Use cases and Selling and growing your app take their loader-data twins' `out` (SH-E-df971a94, SH-E-0440fb5a, SH-E-676ffe45, SH-E-cf8026fb, SH-E-9d3c974b). Themes is CM-SFR-001 `core`, Headless CM-SFR-011 `core`, Mobile CM-CHN-006 `extension-point` (SH-E-3f75bea6, SH-E-2f98826b, SH-E-757fb147).
- **R26.3, Overview links:** `/docs/storefronts` takes the top bar's Storefronts line (SH-E-126c336a); `/docs/storefronts/themes`, `/headless` and `/mobile` take their headings' lines. Their term is left empty.
- **R26.5, buttons:** each collapsed button is a container, read with its children and its first page's description; its children's own things are named in passing.
- **App surfaces' buttons** take their extension capabilities, `extension-point`, as SH-26 forecast: Admin CM-APP-008, App Home CM-APP-007, Checkout CM-CHK-004, Customer accounts CM-CUS-014, Online store CM-SFR-004, Point of Sale CM-POS-004. The earlier lines on the labels Customer accounts, Online store and Point of Sale (`core` on CM-CUS-010, CM-SFR-001, CM-POS-001) are the things themselves, not their app surfaces, as each reading says.
- **R26.7:** Developer Tools (Themes) is CM-DVT-001 `core`, the platform's tools for building themes, with the CLI and dev stores named in passing.

**Where I extended them, for the coordinator to check:**
- **R27.6, the Use cases buttons.** Each page says apps do the use case's work ('Build apps that help Shopify merchants sell directly to other businesses.'; 'Build apps that manage the product catalog…'; 'Create fulfillment apps…'). So each is `extension-point` on the capability its title names, by B-extent's 'an API whose statements say apps or partners use it to do the work'. A title that names two things takes a line for each (R25.5): Marketing and web pixels (CM-MKT-005, CM-MKT-009), Orders and fulfillment (CM-ORD-001, CM-SHP-009) and Products and pricing (CM-CAT-001, CM-CAT-013). Two buttons read their page:
  - **AI and agents** names the agents 'that merchants and buyers use', so it takes CM-AIA-002 (Sidekick, 'Your app connects to it with app extensions') and CM-AIA-005;
  - **Analytics** takes CM-ANL-001 `extension-point` ('Shopify Analytics is a platform your app can build on to put your data in front of merchants') and CM-ANL-006 `core` for its whole content, ShopifyQL through the GraphQL Admin API (R25.6).

  Flow is CM-AUT-001 `extension-point`, third parties' connectors to a first-party app (the ruling after SH-55).
- **R27.7, Design and quality's buttons.**
  - Design guidelines is CM-DVT-001 `core`, as SH-50 and SH-53 placed the App Design Guidelines.
  - Security ('the security requirements that your app needs to meet before you submit it for review by Shopify') and App performance (its page: 'to list your app for public distribution, it must meet the' App Store requirements) are the App Store's review requirements, CM-APP-002 `core;extension-point`, as SH-61 placed the Built for Shopify requirements.
  - **Built for Shopify** is CM-APP-002 `core;extension-point`. This departs from SH-26's forecast ('no capability found: `new`, or `out`'). `held_entries.py earlier` prints 14 earlier lines on the label, all on CM-APP-002 `core;extension-point` (SH-50:86 to SH-62:136), and I kept to them.
- **R27.8, Selling and growing your app's buttons.** Shopify App Store is CM-APP-002 `core;extension-point` and Billing CM-APP-003 `core`, as SH-26 forecast. Marketing and growth is CM-APP-002 `core;extension-point`: an app's listing, search ads, traffic and reviews on the App Store, as SH-53 and SH-59 placed the App Store's ads. The developer's own marketing outside the platform (press releases, webinars) is no capability's thing.
- **Building blocks' buttons:**
  - APIs is CM-API-001 `core`, Authentication CM-API-002 `core` and Events and webhooks CM-API-008 `core`;
  - Custom data is CM-CNT-002 `core;extension-point`, as SH-51 placed the Winter '23 group Custom data;
  - Extensions is CM-APP-001 `extension-point`, an app's extensions as part of the apps developers build;
  - Functions is CM-APP-005 `extension-point`, as SH-25's Function APIs.
- **The Storefronts docs' buttons:**
  - Getting started, Key concepts, Best practices and Theme features are CM-SFR-001 `core` containers, all their items being a theme's. The first three take no term, since their labels don't name the thing.
  - Sell themes is CM-SFR-003 `core;extension-point`.
  - Headless's buttons are CM-SFR-011 `core`. Hydrogen and Oxygen holds both of that cell's terms, so it takes one line.
  - Checkout Kit is CM-CHK-001 `core`, as SH-62 and SH-65 placed it; Accelerated checkouts is CM-CHK-008 `core`; Mobile storefronts is CM-CHN-006 `extension-point`.

## `dev-store-feature-previews` (entries 55–60): the rules I set (R27.1 to R27.3)

The list stands under 'Test a feature preview on this store' and “Preview changes to Shopify and APIs before they're generally available”, on the store-create page with the store type Dev selected ('Testing, dev, or staging environments', `storeType` `development`). shopify.dev's Feature previews page (30 September) describes each preview by its handle: 'Only one feature preview may be enabled on a dev store.'

- **R27.1, the feature's own line.** A preview is a feature in early access: `shows` on each capability its description names, the preview's words in `reading` (the brief's flags rule; R48.5). Its scope is the store type, `Dev`. A condition the label states for the feature is that line's own scope: 'available to Plus merchants' gives `Dev and Plus merchants` (the ruling after SH-69). Where a held store has the feature, the preview is a second line beside the released feature's own lines (E150).
  - **Ship and pickup in one order:** CM-SHP-007, beside SH-30's feature test drive for Plus and Enterprise (SH-E-0e1c25b9, `core`). No held store's eligibility names the feature.
  - **Market-driven shipping** ('Moves shipping configuration into Markets…') takes CM-SHP-001 and CM-MKS-001, as SH-14 and SH-19 placed its routes. Its routes' feature `marketDrivenShipping` is true on 2jiwxs-gr, capture-client-store-vny2vy5w and capture-plus-dev, and false on the other held stores (`derived/eligibility-by-store.tsv`).
  - **The pair** (`market_driven_split_delivery`) takes all three lines. The docs' table of 30 September doesn't list it.
  - **Physical inventory** ('Adds bins, counts, and purchase orders to the unstable GraphQL Admin API.') takes CM-INV-003 (counts, beside SH-36's released Stock counts), CM-INV-007 (purchase orders) and CM-INV-005 (bins, a reading: no capability names bins).
  - **Liquid July '26 changes** is CM-SFR-002, the theme's code (its term Liquid).
- **R27.2, the dev store.** Every preview takes CM-DVT-004 `core`, the platform's own development store and its option to test a preview, as SH-99 placed the CLI's dev store with its feature preview flag. This is one line for the six entries.
- **R27.3, the admin's new design** ('Applies the new visual design to the Shopify admin…') is the admin's own look, no capability's thing (the ruling after SH-37; SH-30's lines on the refreshed design). It takes only the CM-DVT-004 line. The App Home surfaces it lets developers check are named in passing.

**How I read the coordinator's 'shows where the held stores don't have it':** the preview's own line is `shows` in every case. Where a held store has the feature, that store's own lines (the routes') carry the released feature, and the preview stands beside them (E150). If the coordinator meant that a feature a held store has takes `core` from the preview, Market-driven shipping's two lines (and the pair's) would change. Their cells are `core` either way.

## `document-template-config` (entries 61–90): the rules I set (R27.4, R27.5)

The Pick list's 'Configuration' in 'Edit template' (Settings > Shipping and delivery > Documents) holds Pick by (Order, Product), Sort by (4 options by order, 10 by product), Fulfillment status (7) and Columns (9). The editor is the route `document-template-editor` that CM-ORD-009's cell holds (SH-S-5261). Its gate, `fulfillmentBatchingEligible` or a beta, is the route's own, so it is named in `reading` and isn't these settings' scope (the ruling after SH-8).

I read the order (CM-ORD-001), fulfilment (CM-SHP-009, CM-SHP-010), invoice (CM-ORD-008), order status (CM-ORD-003) and document (CM-ORD-009) cells, and SH-85's R85.4.
- **R27.4, the document's line.** Each setting is CM-ORD-009 `core`, the admin's own printed document for its record. The line is grouped by setting: Pick by, Sort by by order, Fulfillment status, Columns, and Sort by by product.
- **R27.5, the record's line,** where a setting names a thing of the record:
  - **Fulfillment orders:**
    - Pick by Order (`fulfillment_order`) and the Quantity keys (`remaining_quantity`, and the column Quantity) name the fulfillment order and its lines;
    - the seven fulfillment statuses are its states, CM-SHP-009's and not CM-ORD-003's, whose note puts fulfillment orders' On hold in the SHP area;
    - each is `core`, since the pick list does fulfilment's picking (R85.4's (a)), as SH-36's batches place picking (SH-E-95970ba3).
  - **A column or sort key** that names a field the platform keeps on a record is `core` on that field's capability, as the ruling after SA-25 and SA-26 places an export's column:
    - Order ID and Order name: CM-ORD-001;
    - Product and Product title: CM-CAT-001;
    - Variant, Variant name, SKU and Pick by Product (`product_variant`): CM-CAT-002;
    - Variant image: CM-CAT-007;
    - Product tag: CM-CAT-006;
    - Order tag: CM-ORD-011;
    - Bin location: CM-INV-005 (a reading: a bin is a place within a location; its sort value is `fulfillment_order_line_item_inventory_group_names`, and its preview column reads 'Bin name').
  - **The alternative** is R85.4's (b): a column that only shows a record's field supports `shows`. It changes only CM-ORD-011, below.

## The `CHANGES` lines, and what I decided

- **CM-B2B-001@shopify gains `extension-point` (line 26, B2B, SH-E-7f2e9fd2): kept.** The page says 'Build apps that help Shopify merchants sell directly to other businesses.', and its children are apps' work on companies, B2B catalogs, draft orders and B2B checkout UI. That is third parties doing it through the platform's APIs. The alternative is `core`: the platform's own B2B API, a guide to developers included.
- **CM-CAT-001@shopify gains `extension-point` (line 34, Products and pricing, SH-E-38b556bc): kept, on the same reading.** The page reads 'Build apps that manage the product catalog'. The alternative is the same.
- **CM-DVT-004@shopify gains `core` (line 62, the six previews' dev store line): kept.** The organization's store-create page for a Dev store is the platform's own place for its development stores. The cell's reading ('no place … of a development store is held') predates the held pass, and SH-99 (SH-E-7e316942) and E151 already place dev stores `core`.
- **CM-ORD-011@shopify becomes held and gains `core` (line 94, the column Order tag, SH-E-363dd40c): kept.** The pick list prints each order's tags. Its preview shows 'tag1, tag2' for the sample order #9999 (`steps/001.frame-0.text.txt`), so the platform keeps tags on its orders: the ruling after SA-25 and SA-26. The alternative is `shows` (R85.4's (b)), which would leave the cell held with no placement. The cell's note expects Shopify's tagging, if any, under Flow (CM-AUT-001). This column is the tag itself, not an automation.

## The checker's `NOTE`s

- **Line 38, core on a product named with the platform's brand (Shopify App Store):** the App Store is the platform's own marketplace, as CM-APP-002's cell reads it ('Shopify's App Store is its own', shopify.com's header, reviewed by Shopify). The line is not about a separate product.
- **The containers** (Building blocks, Design and quality, App surfaces, Use cases, Selling and growing your app, Themes, Headless, Mobile) are placed by R26.1 and R25.1, as above.
- **Line 78, CM-ORD-003 (on hold) holds nothing:** line 78 is the Fulfillment status group's CM-ORD-009 line, which covers On hold (SH-E-d52d012b). That entry's CM-SHP-009 line (line 85) names CM-ORD-003 and says why it isn't the thing: On hold is a fulfillment order's hold, which CM-ORD-003's own note places in the SHP area.

## Entries I couldn't tell, and what would settle each

- **Extensions (SH-E-36a7a81a):** CM-APP-001 `extension-point`. The alternatives are `out`, as a grouping over the surfaces' extension capabilities, or a new thing, app extensions as such. What would settle it: whether CM-APP-001 holds an app's extensions in general (CM-APP-006 holds only the admin's).
- **Security and App performance (SH-E-583af9a8, SH-E-e44289ee):** CM-APP-002 `core;extension-point`, as the App Store's review requirements. The alternative is CM-DVT-001 `core`, as guides. A ruling on standards documented for app developers would settle it.
- **Marketing and growth (SH-E-b6024d24):** CM-APP-002 `core;extension-point`. The alternative is `out`, a grouping of the App Store's tools and the developer's own marketing.
- **AI and agents' CM-AIA-005 line and Analytics' second line (SH-E-72640ba6, SH-E-aee8b65a):** each rests on the page the button opens. The coordinator may keep one line for each.
- **Theme features (SH-E-34e68cc6) and Headless APIs (SH-E-070d7583):** `core` containers of CM-SFR-001 and CM-SFR-011. The alternative for each is `out`, a grouping of several capabilities' things (the features a theme can enable; the Storefront API and the Customer Account API).
- **Physical inventory's bins (SH-E-6ecc4eac) and the pick list's Bin location (SH-E-d8f2f921, SH-E-1d380ca6, SH-E-39aad239):** read as CM-INV-005. The alternative is `new:Bin locations`. I searched 'bin; bins; bin location; warehouse; shelf; storage location' and found no capability naming bins. A held definition of a bin would settle it; the physical-inventory preview's page (`/docs/apps/build/orders-fulfillment/inventory-management-apps/physical-inventory-feature-preview`) isn't read here.
- **Pick by Order (SH-E-95664736):** CM-SHP-009 by its value `fulfillment_order`. The label reads Order, so the alternative is CM-ORD-001.
- **Variant image (SH-E-ad810dec):** CM-CAT-007, the media. The alternative is CM-CAT-002, as the variant's.
- **SKU (SH-E-1731c971, SH-E-2fe62278, SH-E-8417daa9):** CM-CAT-002, by the sort's value `product_variant_sku`. No capability names SKU. The alternative is CM-INV-001, where Shopify keeps a SKU on the inventory item; no held statement read here says so.

## The structures' items against their sources

- **`dev-store-feature-previews`:** the items agree with step 65. Every choice is unchecked there too ('[ ]'). The list of 7 October and the docs' table of 30 September differ:
  - only the docs list Increased variants (`extended_variants`);
  - only the store-create page lists Market-driven shipping and ship & pickup in one order (`market_driven_split_delivery`).
- **`document-template-config`:**
  - The items' `checked` reads false throughout, as the register says. The step text shows the state on capture-plus: Pick by Order, Open and In progress, and all nine columns checked; by product, Sort by 'Quantity (lowest to highest)' selected (step 4).
  - The label Canceled has the value `cancelled`.
  - The preview frame names the columns otherwise: Order, Product Title, Variant, Image, Qty, SKU, Bin name, Order tag, Product tag.
- **`dev-nav`:** no disagreement beyond SH-26's notes.

## What the sources state that no entry holds, for the second stage

- **The Feature previews page** (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@24315784`):
  - Increased variants: 'Raises the number of variants that a product can have.', a lead for CM-CAT-002's variant limit;
  - the timeline: a feature tied to a backwards-incompatible change reaches users nine months after its stable API version, a lead for CM-API-006;
  - 'Only one feature preview may be enabled on a dev store.'
- **The store-create page** (`raw/runs/20261007T010009Z-journey-partner-dashboard/steps/065.text.txt`, lines 1–19):
  - the store types Dev and Client transfer ('Manage and transfer stores for clients');
  - the Shopify plan picker ('Test plan features for free');
  - 'Generate test data for store' ('Preload your store with a bogus gateway and sample data').

  These lead to CM-DVT-004.
- **The Documents table** (`raw/runs/20261007T225846Z-journey-document-template/steps/010.text.txt`, lines 91–99): Pick list, Packing Slip and Invoice. A built-in Invoice template would be `core` evidence for CM-ORD-008, whose Shopify cell holds only the App Store's Invoice and receipt apps. The register: 'Packing slip and Invoice not yet held'.
- **The template editor** (`steps/001.text.txt`): 'Name' [Pick list], 'Design', and the button 'Add metafield' after Columns, a column from a metafield, a lead for CM-CNT-002.
- **The Apps docs' pages:**
  - Analytics (`@21416260`): 'App Events in Analytics is in developer preview. The preview is available to approved apps…', a release marker for CM-ANL-001 and the App Events API;
  - AI and agents (`@21409058`): Sidekick's two kinds of app extension, app data and app actions (CM-AIA-002).
- **The loader data:**
  - line 47 holds the Orders and fulfillment group's Market-driven shipping (with 'Feature preview for market-driven shipping'), and Purchase options and Shopify Collective under Products and pricing;
  - line 48 holds the Theme Store's requirements and review process (CM-SFR-003), the 'Hydrogen developer preview' (“The next version of Hydrogen is a framework-agnostic SDK…”, CM-SFR-011), checkout.liquid under Layouts, mock.shop, and Buy Button JS and the JS Buy SDK.

  SH-26's notes list the rest.

## Problems with the brief or the script

- **`held_entries.py earlier` prints no twin for a `dev-nav` heading.** The rendered headings' loader-data twins (R26.1) are found by label in SH-26's placements, not by the script.
- **The checker's first-lead `NOTE` persists** where a line's reading names that capability and says why it isn't the thing (line 78, CM-ORD-003).
- **SH-26's forecast for Built for Shopify** ('no capability found') was written before `earlier` was consulted for it. The 14 earlier lines govern, as the brief says, so I followed them.
- **'shows where the held stores don't have it'** in the coordinator's message can be read two ways; my reading is above. Holding a feature is read here from `derived/eligibility-by-store.tsv`, the repository's own table from the router's eligibility and the RequestDetails answers. It is cited as a reading, not quoted.

## The coordinator's check

Measured: 20.3 million tokens over 90 requests, about 226,000 an entry. The checker prints no problem.
- **Kept:** R25's and R26's rules for `dev-nav`'s last 54, so it is placed whole, and R27.1 to R27.8; every `CHANGES` line (CM-B2B-001 and CM-CAT-001 `extension-point` by their pages' 'Build apps that…'; CM-DVT-004 `core` for the dev store; CM-ORD-011 `core` by the pick list's column Order tag, as the export-column ruling places a column, beside SH-28's `shows`).
- **The feature previews:** the reading is the one meant. A preview is `shows`, and where a held store has the feature it stands beside the released feature's own lines (E150).
- `dev-store-feature-previews` and `document-template-config` are placed whole, and with this batch every one of Shopify's 104 batches is placed and checked.
