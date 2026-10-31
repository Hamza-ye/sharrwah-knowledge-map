# Notes: held pass, Salla, batch SA-25 (`docs-event-lists`, rest; `docs-navigation`; `docs-sidebar`; `expert-service-categories`; `export-columns`, first part)

## What I read

- The brief, `H-held.md`; the evidence map; the coordinator's rulings, `held/review-H-rulings.md`, to its last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run".
- observed-sa (at `b0bd0b16`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the `structures/REGISTER.tsv` rows of my five structures; `index/ledger-summary.tsv`.
- The five structures' `meta.json` (`show --meta`) and their `selection.tsv` rows.
- SA-24's notes and placements (the rules its event lines follow, and the coordinator's check), and the placements of the other Salla batches where an entry of mine is the same thing as one of their lines: SA-1's App Store categories, the changelog categories and SA-6/SA-7/SA-32's lines on CM-PTN-005.
- **Sources:**
  - `docs-event-lists @webhooks`: `webhooks/source.md`, lines 236 to 368, and its record `raw/runs/20261005T234928Z-docs-md/fetch.warc.gz@29604`.
  - `docs-navigation @v2@20261005T233540Z`: its `items.jsonl` (all 28 items, for the menus my folders sit under) and its record `raw/runs/20261005T233540Z-docs-sections/fetch.warc.gz@1122` (https://docs.salla.dev/welcome).
  - `docs-sidebar`: `checkout-apis/items.jsonl` (lines 1 to 30), record `…20261005T233540Z-docs-sections/fetch.warc.gz@838339`; `shipments-fulfillment-apis@20261006T003648Z/items.jsonl` (lines 1 to 16), record `raw/runs/20261006T003648Z-docs-dataschema-html/fetch.warc.gz@3104127`.
  - `expert-service-categories @merchant@ar`: `source.json`, the answer `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1917.json` (step 79), read whole: its 15 categories and its 100 `sub_categories`, joined by `parent_id`.
  - `export-columns @orders@demo-en`: `source.json`, the answer `raw/runs/20261008T155401Z-journey-export-templates-demo/responses/0018.json` (step 1); to clarify it, that run's `actions.jsonl`, `steps/001.text.txt`, `steps/005.text.txt` and its `index/run-notes.tsv` row.
- The cells of every capability my lines name (`held_entries.py cells`, and `land_points.py cell` for CM-SHP-009 and CM-SHP-002), SA-C-145's statements, and `caps --terms` for the things no lead named (below).

## The batch, and the batches beside it

- **`docs-event-lists`:** SA-25 holds the Webhooks page's rows 3 to 58 of 'List of Salla Store Events' (`order.status.updated` to `review.added`), the rest of the structure's uncited entries after SA-24. SA-24's rules are kept (below). With SA-24, the structure is now placed whole.
- **`docs-navigation`, `docs-sidebar`, `expert-service-categories`:** placed whole here, the first batch to place them.
- **`export-columns`:** SA-25 holds the orders' columns 1 to 24 (section `order`). **SA-26 holds the rest and hasn't run:** the orders' section `customer_details` (Customer Name, Mobile Number, City, Country, Customer Address, Customer Location Map Link) and the products' 31 columns (sections product_info, product_options, match_columns, seo_improvements). The rules my lines follow, for SA-26, are below.
- **SA-23 (`dashboard-webhook-events`) hasn't run.** Its events meet my Webhooks rows on the same names, as SA-24's notes list them. My shipping.zone lines (27, 28) now take CM-SHP-015 as well as CM-SHP-001, which SA-24's notes suggested SA-23 might want for its labels 'انشاء تسعيرة شركة شحن' and 'تعديل تسعيرة شركة شحن'.

## Rules my lines follow

### The Webhooks page's events (SA-24's rules, kept)

1. Each event is `core` on the capability of what it is about, Salla's own API for its own feature, with the same capabilities SA-24 gave the same events on the App Functions pages and Conditional Webhooks (its rule 5). Its row's Description is quoted in `reading`; the page is cited at its record.
2. Each row adds CM-API-008 `core`, the list 'List of Salla Store Events' being Salla's webhook topics (SA-24's rule 2, as WC-8).
3. No scope: the page states no plan, store or country.
4. The leads SA-24 named for my rows are taken: product.price.updated CM-CAT-013; product.category.updated CM-CAT-003; product.brand.updated CM-CAT-005; product.tags.updated CM-CAT-006; product.image.updated CM-CAT-007; store.branch.setDefault and .activated CM-INV-005.
5. **What I added, row by row:**
   - **product.status.updated** (22): CM-CAT-001 `core`, a product record's own state. What a product's statuses are isn't stated on the page. Searched: product status; حالة المنتج; visibility; hidden; draft; مخفي; publish; availability; out of stock; نفذ. Its first lead, CM-OPS-004, is WooCommerce's system status report, not this.
   - **The struck rows** (17 `~~product.updated~~`, 19 `~~product.available~~`): `shows` on CM-CAT-001 and CM-INV-001, and `shows` on CM-API-008, the strike in `reading`, as SA-24's rule 6 proposed. I read the strike as the page no longer offering the topic in this list. The cells keep their own placements from the unstruck lists (Conditional Webhooks, App Functions).
   - **shipping.zone.created and .updated** (27, 28): CM-SHP-001 `core`, as SA-24, and CM-SHP-015 `core`, since the row names the zone's owner, 'a custom shipping company', as the cell's shipping.company.* topics.
   - **invoice.created** (53): CM-ORD-008 `core`, as SA-24, and CM-ORD-003 `shows`, for the statuses the row names, `completed` and `restored`.
   - **order.shipment.created and .cancelled** (10, 11): CM-SHP-009 `core` by the events' names, as SA-24 and the cell, and CM-RET-003 `shows`, since their descriptions name 'an order shipment return' (below).
   - **order.coupon.updated** (7): CM-ORD-001 and CM-MKT-002, both `core`, as SA-24.

### The docs' navigation and sidebar

- A navbar folder or a sidebar folder is a container (rule 3). It goes on the capability its title names, with the support the cell already gives the same folder:
  - Merchant API: CM-API-001 `core`;
  - Twilight Engine: CM-SFR-002 `core`;
  - Shipments & Fulfillment APIs: CM-SHP-009 `shows`;
  - Salla AWB, in both structures: CM-SHP-002 `extension-point`;
  - Salla CLI: CM-DVT-002 `core`.
- The menu a folder sits under (Merchant, Storefront, Partner APIs, Dev Tools) gives it no line: it is a group the entry only sits under.

### Expert service categories

- Each category is one of Salla's Merchant Services categories, under which partners' services are listed for the merchant. It takes CM-PTN-005 `extension-point`: the platform's own list of third parties' services (M-3, M-7), as the cell's partners' side and its service providers, independent parties (SA-S-0198).
- Where the category's name names a capability's thing, the category also takes that capability, `extension-point`. That follows B-extent's "an app-store or marketplace category" and SA-1's App Store categories. The sub-categories in the same answer, which the category's description 'يشمل هذا التصنيف على:' introduces, settle which capability. They are quoted in `reading` but aren't placed:
  - التسويق والإعلانات: CM-MKT-005 and CM-MKT-010;
  - التسويق عبر UGC: CM-MKT-005;
  - تخصيص الثيمات: CM-SFR-002;
  - سياسات وعقود قانونية: CM-CNT-008;
  - تجهيز المنتجات: CM-CAT-001.
- **خدمات التوثيق** takes CM-PAY-003 `shows`. Its sub-category توثيق المتجر في سلة is the cell's Store Verification, which Salla's own team reviews, so a partner's service only prepares it (a reading).
- The other categories name no capability's thing, and take CM-PTN-005 only. They are:
  - تجهيز وتخصيص المتجر, التصاميم الإبداعية, الفيديو والصوتيات, إدارة وصناعة المحتوى, خدمات التقنية والربط, خدمات الذكاء الاصطناعي, التدريب والاستشارات, خدمات مالية and خدمات أخرى.
  - Searched: store setup; تجهيز المتجر; إنشاء متجر; UGC; creator; influencer; مؤثر; logo; شعار; هوية بصرية; brand identity; video; فيديو; content writing; محتوى; كتابة; integration services; ذكاء اصطناعي; AI; توثيق; verification; KYC; سجل تجاري; training; تدريب; consulting; استشارات; legal; قانونية; accounting; محاسبة; financial; مالية; photography; تصوير.
  - What the searches found isn't the thing: CM-ONB-004 is the platform's own setup wizard, which holds nothing on Salla; CM-AIA-001 is the platform's own AI tools; CM-ONB-003 is the platform's own support and learning; CM-PAY-028 is accounting integrations, not accounting services.
- **Scope:** none. The answer is the merchant store's (run `20261008T122729Z-sweep-merchant-menus-ar`), and the source names no plan or store. `services_count` and `requires_city` (true for التسويق عبر UGC) are in `reading`. A count of listed services is the marketplace's data at capture, not a quality.

### Export columns (for SA-26)

- **E1.** Each column is CM-MIG-003 `core`, a column Salla's export templates can take. The cell says 'What a template holds isn't stated': these lines state it. The column takes no CM-MIG-001 line, since a column isn't a kind of export (M-6, refined).
- **E2.** Where the column's title names a thing that a capability other than the exported entity's own record holds, it takes a `shows` line on that capability. Such a line supports no placement: the export shows the order carries the field.
  - My E2 lines:
    - Order Status: CM-ORD-003;
    - Order Tracking Link: CM-SHP-017;
    - Discount: CM-MKT-001;
    - Policy Creation Date and Policy Number: CM-SHP-002, since بوليصة / policy is Salla's word for a shipping label (the cell's homonym note);
    - Shipping Cost: CM-SHP-001;
    - Payment Method: CM-PAY-001;
    - Cash on Delivery Commission: CM-PAY-029;
    - Tax: CM-TAX-001;
    - Shipping Company / Branch: CM-SHP-015;
    - Product Names with SKU and SKU: CM-CAT-001;
    - Tags: CM-ORD-011;
    - Internal Notes: CM-ORD-013;
    - Invoice Number: CM-ORD-008;
    - Order Source (`utm_source`): CM-MKT-008;
    - Bank / Payment Reference: CM-PAY-030 and CM-PAY-020.
  - The order's own fields take E1 only: Order ID, Cart Total, Order Total, Order Date, Date of Last Order Update, Order Reference Number and Order User. The section the column sits under (`order`, drawn 'Order') is a group, and gives no line.
- **E3.** Terms are the column's `title` and `name`. There is no scope: the answer is the demo store's (Pro), and the source names no plan. The cell's flags order-export-templates and product-export-templates are released on plans plus, pro and special. There is no quality.
- **For SA-26, a proposal:**
  - customer_details: Customer Name and Mobile Number go on CM-CUS-001 `shows`; City, Country, Customer Address and Customer Location Map Link on CM-CUS-008 `shows`. A column named Country is the platform's field, not a list of countries, so it isn't market data.
  - The products' columns: product_options on CM-CAT-002 `shows`; seo_improvements on CM-CNT-007 `shows`; match_columns ('Other columns') by each column's own title.

## Entries I couldn't tell, and what would settle each

- **10 and 11, order.shipment.created and .cancelled.** Their descriptions name 'an order shipment return', the words of order.shipment.return.created and .cancelled (`webhooks/source.md`, lines 265 and 266, against 268 and 269). I read this as a slip of the page, as SA-24 did.
  - I placed them by their names on CM-SHP-009, as the cell's topics. The return reading is recorded as CM-RET-003 `shows`.
  - The Order webhook model page (`doc-433804`) or a delivery of the event would settle it.
- **17 and 19, the struck rows:** `shows`, as above. The model page `doc-433805#product-webhook-events-model` would say whether the topics are deprecated.
- **53, invoice.created:** the Webhooks page says it fires 'when the order status is either `completed` or `restored`', and the App Functions page says 'when an invoice is created for an order' (SA-24). restored is the store's status مسترجع, which CM-RET-003's cell holds as shows. I gave CM-RET-003 no line.
- **59, Shipments & Fulfillment APIs:** `shows`, as the cell's own line for the same folder (SA-S-1171).
  - Its sidebar tree holds Shipping Management and Order Fulfilment folders, each with App Cycle, Create App, Setup App and Test App (`shipments-fulfillment-apis@20261006T003648Z/items.jsonl`, lines 5 to 14): apps doing the shipping.
  - A reading of those pages would make it `extension-point` on CM-SHP-009, and perhaps CM-SHP-015, whose cell holds the Shipping App type 'for shipping companies' (SA-S-1185).
- **62, the nameless schema folder of the Checkout APIs tree:** a container with no title, holding the collection's data schemas (SuccessEnvelope, CartTotals, CartItem, …). I placed it on the capability of its tree, CM-CHK-001 `core`, the cell's docs collection Checkout APIs. `out` as a layout node that names nothing is the alternative.
- **The categories' second lines, and the four CHANGES they make** (CM-CAT-001, CM-CNT-008, CM-MKT-010, CM-SFR-002, below):
  - I read a Merchant Services category as a marketplace category, B-extent's extension-point: partners do the named work for the merchant through Salla's marketplace.
  - The alternative is that a services marketplace isn't an interface through which the work is done, only a place to hire someone. Then each second line is `shows`, and only CM-PTN-005 is `extension-point`.
  - The coordinator decides the reading for all five lines together.
- **66, التسويق عبر UGC:** CM-MKT-005 only. Who makes the UGC (creators, influencers) isn't stated. CM-MKT-015 (creator and influencer marketing) is the alternative.
- **92, Shipping Company / Branch:** CM-SHP-015 `shows` for the shipping company. What 'Branch' is isn't stated: a carrier's branch, or the store's branch an order is collected from. CM-SHP-006's note keeps الفرع as a carrier's branch in the economy shipping line, so I gave the branch no line. CM-INV-005 or CM-SHP-007 are the alternatives.
- **97, Order User:** E1 only. Whose user it is (the buyer's account, or the staff member who created the order) isn't stated. An export holding the column would settle it.
- **101, Order Source:** CM-MKT-008 `shows`, by the column's name `utm_source`, a marketing source. It makes the cell held with no placement (CHANGES, below).
- **102, Bank / Payment Reference:** CM-PAY-030 and CM-PAY-020, both `shows`, one for each reading of the slash.

## Structures whose items and sources disagree

- **`docs-event-lists @webhooks`:** the items agree with `source.md`. The page's own slips are the descriptions of 10 and 11 (above) and invoice.created's trigger (53).
- **`expert-service-categories`:** the items leave out each category's `id`, `parent_id`, `icon` and `image`, and the answer's `sub_categories`, as the register says. The sub-categories carry `services_count` 0 each, against their categories' counts (777, 772, …). The source doesn't say whether the count isn't kept by sub-category.
- **`docs-navigation`:** the first-level menu's title is 'Merchant ', with a trailing space (`items.jsonl` line 1).

## What the sources state that no entry holds (for the second stage)

- **The export templates' page** (`20261008T155401Z-journey-export-templates-demo/steps/001.text.txt`, lines 21, 22 and 29): 'Create your first export template', 'Select only the fields you want to include in your export file, like name, price, and more.' and 'Start by adding the items you need in your export.' This is the definition of what a template holds, for CM-MIG-003. The save answered 'تم حفظ القالب بنجاح' (its run note).
- **The expert services' 100 sub-categories** (`responses/1917.json`, `data.sub_categories`). Leads:
  - تفعيل طرق الدفع (تابي، تمارا...): CM-PAY-015 and CM-PAY-001; it names Tabby and Tamara;
  - نقل متجر إلكتروني: CM-MIG-005;
  - تجهيز وتصميم تطبيق على صانع التطبيقات: CM-CHN-006;
  - إنشاء صفحات الهبوط: CM-SFR-006;
  - تحسينات (SEO) والتسويق بالمحتوى: CM-CNT-007;
  - حجز وربط ونقل دومين المتجر: the store's domain;
  - الربط مع جوجل ميرشنت and the pixel and catalog links: CM-CHN-004 and CM-MKT-010;
  - الربط مع جوجل اناليتكس and جوجل تاجز مانجر: analytics;
  - الربط مع مخازن ومنصات دروب شيبينج: dropshipping;
  - الربط مع زابير: automation;
  - خدمات الضريبة المضافة: CM-TAX-001;
  - خدمة عملاء المتجر: support;
  - تصوير المنتجات (requires_city: true) and تعديل فيديوهات UGC (requires_city: true).
  - The register also says the same path answers a list of 16 when asked with `?type` (step 30 of the same run): another shape, not held as items.
- **The Shipments & Fulfillment APIs tree** (`shipments-fulfillment-apis@20261006T003648Z/items.jsonl`, lines 1 to 14): Getting Started, Migration to the New API, Publish App, Change Log, and the folders Shipping Management and Order Fulfilment, each with its app cycle. These are leads for CM-SHP-009, CM-SHP-015 and CM-API-006.
- **The Webhooks page's delivery terms** (lines 236 and 240): SA-24's notes already list them for CM-API-008.

## The checker's lines, read again

- **`CHANGES` CM-CAT-001 gains extension-point** (line 147, تجهيز المنتجات): a Merchant Services category whose sub-categories are adding products, pricing them, writing their descriptions, and making and editing their images. Partners do the work through Salla's services marketplace. Kept, with the alternative above.
- **`CHANGES` CM-CNT-008 gains extension-point** (line 144, سياسات وعقود قانونية): its sub-categories name the store's return policy, terms and privacy policy. Kept, as above. Its contracts (partnership, NDA, SLA) aren't the store's policies.
- **`CHANGES` CM-MKT-010 gains extension-point** (line 130, التسويق والإعلانات): its sub-category إنشاء وإدارة حملات إعلانية لعدة منصات. Kept, as above.
- **`CHANGES` CM-SFR-002 gains extension-point** (line 134, تخصيص الثيمات): its sub-categories are editing the store's design through CSS and JS, its colours and theme support. Kept, as above.
- **`CHANGES` CM-MKT-008 becomes held** (line 187, Order Source, `utm_source`): a `shows` line, which supports no placement. The coordinator may drop it, the cell staying empty, as SA-24's CM-SFR-016.
- **`NOTE` 'core on a product named with the platform's brand'** (the Webhooks lines): the brand is in the page's heading 'List of Salla Store Events', not in a product's name. These lines are `core` by what the rows show, Salla's own webhook topics, as SA-24's check let stand.
- **`NOTE` first leads that hold nothing:** none of them is the entry's thing.
  - Lines 47 and 150, CM-OPS-004: by 'status', WooCommerce's system status report.
  - Line 155, CM-MKT-004: apps' discount functions, for the Discount column.
  - Line 161, CM-PAY-022: saved payment methods, for Payment Method.
  - Line 169, CM-ORD-015: order payment status, matched by 'order' and 'update', for Date of Last Order Update.
- **`NEW`:** none.

## Problems with this brief or the script

- None that blocked.
- The selection gives `docs-sidebar` the rule `where:type=apiDetailFolder|folder`. One of its two entries, the Checkout APIs' schema folder (62), is an `apiDetailFolder` with no name, and its `folderType` is `apiSchemaFolder`. The rule may mean to leave such folders out.

## The coordinator's check (31 October 2026, after the batch)

- **The expert categories' second lines are `shows`,** by the ruling after SA-25: a services marketplace's category is `extension-point` on CM-PTN-005 only. So CM-CAT-001, CM-CNT-008, CM-MKT-010 and CM-SFR-002 gain no `extension-point`.
- **Order Source (`utm_source`) is `core` on CM-MKT-008.** An order's export carries the source its buyer came from, so Salla records each order's source. WooCommerce's Order Attribution, joined to this capability by M-053, records the same. This is a reading. It makes Salla's attribution cell held, `core`, where it held nothing; the unreleased flag `utm-campaign` stays beside it.
- **The event lines, the docs folders and the export columns stand** as SA-24's rules place them. SA-26 keeps to the export columns' rules.
- **Cost:** 13.7 million tokens over 71 requests, about 134,000 an entry. One cell changes, CM-MKT-008, held with `core`.
