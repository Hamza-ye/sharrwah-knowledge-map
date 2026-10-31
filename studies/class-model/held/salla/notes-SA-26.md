# Notes: held pass, Salla, batch SA-26 (`export-columns`, rest; `importer-schema-fields`; `importer-schemas`; `invoice-settings`, first part)

## What I read

- The brief, `H-held.md`; the evidence map; the coordinator's rulings, `held/review-H-rulings.md`, to its last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run".
- observed-sa (at `b0bd0b16`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the `structures/REGISTER.tsv` rows of my four structures; `index/ledger-summary.tsv`, and the `journey-unit`, `nav-page` and `feature` ledger rows for the invoice settings, the export templates and the importer.
- The four structures' `meta.json` (`show --meta`) and their `selection.tsv` rows (all `decides`; `importer-schemas` by the rule `nested:schemas,types,fields`).
- SA-25's notes and placements (its rules E1 to E3 for the export columns, its proposal for SA-26 and the coordinator's check), and SA-20's lines for the navigation's product types (SA-E-03c97d5b), which are the same things as the import schemas' types. ZD-11's notes for its new thing Shipment receipt by another person.
- **Sources:**
  - `export-columns @orders@demo-en`: `source.json`, the answer `raw/runs/20261008T155401Z-journey-export-templates-demo/responses/0018.json` (step 1); the Add item list at `steps/005.text.txt`, lines 27 to 34 (drawn 'Customer details').
  - `export-columns @products@demo-en`: `source.json`, the answer `raw/runs/20261008T173124Z-journey-product-export-templates-demo/responses/0016.json` (step 1); the Add item list at `steps/003.text.txt`, lines 32 to 67; the run's `index/run-notes.tsv` row.
  - `importer-schema-fields @products.physical@demo-en`: `source.json`, `raw/runs/20261008T171647Z-journey-advanced-import-demo/responses/0051.json` (step 5), read whole: its 36 fields, their sub-fields and its 7 groups. Also the `source.json` of `brands@demo-en` (step 19) and `branch_warehouse@demo-en` (step 23), which hold no items.
  - `importer-schemas @demo@en`: `source.json`, `…/responses/0038.json` (step 2); the run's `actions.jsonl` and `steps/002.text.txt`, `015.text.txt` and `015.aria.yaml` (the Data type list).
  - `invoice-settings`: both `source.json` files, `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/0035.json` (merchant@ar, step 2) and `raw/runs/20261009T022751Z-sweep-public-demo-en/responses/0205.json` (public-demo@en, step 5); the pages `20261008T122729Z-sweep-merchant-menus-ar/steps/006.text.txt` and `20261009T022751Z-sweep-public-demo-en/steps/009.text.txt`, and the demo store's `20261008T154824Z-journey-invoice-settings-demo/steps/001.text.txt` (the journey-unit ledger row).
- The cells of every capability my lines name, and `caps --terms` and `search` for the things no lead named (below).

## The batch, and the batches beside it

- **`export-columns`:** SA-26 holds the rest after SA-25: the orders' section `customer_details` (entries 1 to 6) and the products' 31 columns (7 to 37). With SA-25 the structure is now placed whole.
- **`importer-schema-fields` and `importer-schemas`:** placed whole here, the first batch to place them. `importer-schema-fields` has entries only for `products.physical`'s 7 groups (38 to 44); `brands` and `branch_warehouse` hold no items, so no entries. `importer-schemas` has entries only for the 7 product types (45 to 51).
- **`invoice-settings`:** SA-26 holds 43 of its 52 entries (52 to 94): the fields both stores share, the merchant store's Arabic fields, and the public demo's English fields up to order-status. **SA-27 holds the rest and hasn't run:** the public demo's watermark-opacity (value 69), product-weight, show-product-id, auto-send-invoice, invoice-title, show-GTIN, show-MPN, show-zero-tax and show-delegate-details. Each is the English counterpart of one of my merchant@ar entries (71, 76 to 83). The rules my lines follow, for SA-27, are below (I1 to I4).

## Rules my lines follow

### Export columns (SA-25's E1 to E3, kept)

- **E1.** Each column is CM-MIG-003 `core`. Its reading cites the answer and the Add item list step, and names the section with the name the list draws it under ('Customer details', 'Product info', 'Product options', 'Other columns', 'SEO improvements'). The section is a group the column sits under, and gives no line.
- **E2.** A column whose title names a thing that a capability other than the exported entity's own record holds takes a `shows` line there. The exported entity's own fields take E1 only, as SA-25's order fields did. For the products' export, that means the product record's own fields take no CM-CAT-001 line.
- **E3.** Terms are the column's `title` and `name`. No scope (the demo store, Pro; the source names no plan). No quality.
- **SA-25's proposal for SA-26 is followed:** Customer Name and Mobile Number on CM-CUS-001; City, Country, Customer Address and Customer Location Map Link on CM-CUS-008; Product Options on CM-CAT-002; the SEO columns on CM-CNT-007; the match_columns by each title.
- **What I added:**
  - Customer Location Map Link also takes CM-CUS-009 (map and location services for addresses), `shows`.
  - The products' E2 lines: Product Category CM-CAT-003; Product Image CM-CAT-007; Does shipping require? CM-SHP-001; Sale End Date and Sale Price CM-MKT-001; Hide Quantity Option, Unlimited Quantity and Quantity CM-INV-001; Brand CM-CAT-005; Taxable? CM-TAX-001; Price CM-CAT-013 (the cell's product.price.updated).
  - **Cost Price** is CM-CAT-012 `core`, not `shows` (below, under CHANGES).
  - The product's own fields, E1 only: Product Name, Product Type, Description, Maximum Quantity Per Customer, Add Image Upon Request, Weight, Weight Unit, Product Status, Promotional Title, Install Product, Calories, Product SKU, Barcode, MPN, GTIN.
  - Sale Price and Sale End Date are discounts because the importer itself groups `sale_price`, with `sale_start` and `sale_end`, under 'Discounts' (entry 44). That is a reading.

### The importer's fields and types

- **F1.** Each group of `importer-schema-fields` is CM-MIG-002 `core`: a group of the fields Salla's Advanced import (/importer, its Match fields step) takes for a physical product. The cell's note says Salla doesn't state what the Advanced import takes. These lines and the types' lines state it.
- **F2.** Each thing the group's title or its fields name takes a `shows` line on its capability, the same capability as the export column for the same field:
  - image, images on CM-CAT-007; price on CM-CAT-013; categories on CM-CAT-003; brand on CM-CAT-005;
  - Shipping and require_shipping on CM-SHP-001;
  - Inventory on CM-INV-001; notify_subscribers on CM-MKT-016 (a reading);
  - Product Options on CM-CAT-002;
  - Quantities on CM-INV-001; branch_code on CM-INV-005;
  - SEO Data on CM-CNT-007;
  - Discounts and sale_price on CM-MKT-001.
- **cost_price** is CM-CAT-012 `core`, as the export's Cost Price.
- The product's own fields take no line beyond F1, as in the export: name, description, weight, sku, barcode, mpn, gtin, maximum_quantity_per_order and local_category.
- **F3.** Each type of `importer-schemas` is CM-MIG-002 `core`, and `shows` on the capability SA-20 placed the navigation's same product type on:
  - Physical Product, Custom Service and Food & Beverages on CM-CAT-001;
  - Digital Product and Digital Card on CM-SEL-002;
  - Product Bundle on CM-SEL-006;
  - Reservations on CM-SEL-004.

  A type's description that names shipping or pickup takes CM-SHP-001 ('can be shipped', 'special handling or shipping') and CM-SHP-007 ('picked up'), `shows`. I gave the types `shows` rather than SA-20's `core`, since here they are the kinds of record the import takes, as E2's fields are. Their cells already hold `core`, so nothing changes either way.
- **F4.** No scope (the demo store, Pro). `field_count`, `required_fields` and `paid` are in `reading`. A count of a schema's fields is the schema's own data, not a limit, so not a quality.

### Invoice settings (for SA-27)

- **I1.** Each field is CM-ORD-008 `core`: a setting of Salla's own invoice settings at /orders/invoice-settings, the cell's dashboard link.
  - Its reading gives the field's label, description and tooltip, quoted; its type, default_value and its value on that store; and the answer and the page step it was read from. The page step clarifies a field that has no label (invoice-type, order-status, the design options, store-prefix, invoice-title).
  - The field's `group` (control-elements, design-options) is a group it sits under, and gives no line. So are the page's sections (Invoice content, Product information, Order and Invoice Information, Store & contact information, Design & branding).
- **I2.** What the label or description names, where another capability holds it, takes a `shows` line, as SA-25's E2:
  - product image: CM-CAT-007;
  - product description, barcode, weight, stock number (الرقم المخزني, 'product inventory number', read as the SKU, as SA-25 placed the order export's SKU), GTIN and MPN: CM-CAT-001;
  - contact information and store address: CM-ACC-006 (the store's details; a reading);
  - the acknowledgment's 'order summary' / ملخص الطلب: CM-ORD-009;
  - the return and exchange policy's barcode: CM-CNT-008, whose cell already cites the information page marked as that policy for its barcode on the invoice (SA-S-5034);
  - the order note the customer entered: CM-ORD-013;
  - the order statuses of order-status: CM-ORD-003;
  - the invoice sent automatically to the customer (auto-send-invoice): CM-NTF-001 (a reading);
  - the invoice's tax fields (show-zero-tax): CM-TAX-001;
  - the delegate assigned to receive the order (show-delegate-details): `new:Shipment receipt by another person`, `shows`.
- **I3.** Settings that name only the invoice take I1 alone:
  - invoice-type, invoice-barcode, english-version (the cell's plan line طباعة فاتورة الطلب بالعربي والانجليزي, Salla Plus), invoice-title, store-prefix;
  - the design options logo-alignment, logo-size, the fonts' colours and styles, watermark and its opacity, stamp, its opacity and alignment.
- **I4.** No scope. The answers are the merchant store's and the public demo's, and the source names no plan. Values and defaults go in `reading`, never in `quality`. Terms are the label (or the option labels) and the name, and the words of the thing an I2 line names, each found in the entry's text.
- **For SA-27:** each of its nine entries is the same thing as one of my merchant@ar entries. Its lines should take the same capabilities: product-weight, show-product-id, show-GTIN and show-MPN take CM-CAT-001; auto-send-invoice takes CM-NTF-001; show-zero-tax takes CM-TAX-001; show-delegate-details takes `new:Shipment receipt by another person`. The terms are its English words.

## Each new thing

**`new:Shipment receipt by another person`:** one entry, SA-E-e083d60c (83, show-delegate-details, merchant@ar). SA-27's SA-E-212804a4 is the same field in English.
- **What it is:** 'في حال تعيين مستلم مفوض لاستلام الطلب، سيتم عرض بياناته في الفاتورة بدلاً من بيانات صاحب الطلب الأصلي.' A delegate is assigned to receive the order in place of its owner. The invoice setting only chooses whose details the invoice shows. The delegate itself is a thing of the order, which no capability holds.
- **Its name:** I named it as Zid's new thing (ZD-E-c5337f63, ZD-11), whose setting is 'Show feature for shipment receipt by another person.' (a shipment received by a different consignee). That they are one thing is a reading. Salla's words are مستلم مفوض, المستلم المفوض, and the English page's 'delegate'.
- **Its place of its own on Salla:** none held. It is a line inside a setting's description. How a delegate is assigned (by the buyer at checkout, or by the merchant) isn't stated in what I read.
- **Proposed domain, area and parent:** domain C, under CM-ORD-001 or beside the checkout, as ZD-11 proposed. It isn't gifting (CM-LOY-006), which is buying for someone else, nor CM-ORD-010.
- **Searched:** delegate; مفوض; المستلم; مستلم; recipient; receiver; استلام الطلب. The concern map holds only order.customer.updated, 'تحديث بيانات مستلم الطلب' (SA-S-1585), the order's own recipient, not a delegate.

## Entries I couldn't tell, and what would settle each

- **30 and 38, Cost Price and cost_price, on CM-CAT-012 `core`** (the CHANGES, below). The alternative is `shows`, as E2. The coordinator's ruling on CM-MKT-008 would settle whether a record's field in an export makes its own capability `core`.
- **45 to 51, `paid`:** physical is `paid: false`, the six others `paid: true`. The page shows no mark for it (`steps/015.text.txt`, lines 26 to 40; `015.aria.yaml`, its list of types). It may mean a paid plan, a fee, or something else.
  - The navigation's actions for the same types sit behind the feature product-advance-management (SA-20). That may be the same gate, a reading.
  - I put it in `reading` only. The feature's plans in `dashboard-features` would settle whether the paid types are a plan's.
- **3 to 6, the order's customer address:** the columns sit in `customer_details`. CM-CUS-008's note keeps the order's shipping address apart, as the order's. Whether the export takes the customer's saved address or the order's shipping address isn't stated. An export file holding the columns would settle it.
- **22, Install Product (`product_pinned`):** I read the name as pinning the product, and the English title 'Install Product' as a rendering of that (Arabic تثبيت names both). It is a reading. The Arabic title in `dashboard-translations` would settle it. No capability holds pinned products.
- **16, Add Image Upon Request (`enable_upload_image`):** the importer's ungrouped field of the same name says 'Specify whether the customer can upload an image' (not an entry; below). Read with it, the buyer uploads an image when ordering the product. No capability holds that. CM-CHK-009's order options are the order's fields at checkout, not a product's. The coordinator may want it as a new thing; I placed it E1 only, as a field of the product.
- **14, Maximum Quantity Per Customer, and 40's maximum_quantity_per_order ('…in a single order'):** a limit on one product's quantity. It isn't Zid's new Minimum and maximum order limit, which is on the order, by value or quantity unstated. Nor is it CM-CAT-009's product restrictions, whose statements don't say what they limit. E1 only.
- **38, local_category ('Local Category', no description):** it may be the store's own category or Salla's taxonomy (CM-CAT-004's salla-taxonomy). No line. A description would settle it.
- **40, notify_subscribers:** the source lists it in the group Inventory and also as a sub-field of quantity, labelled 'Notify Subscribers' with no description. I read it as back-in-stock subscribers (CM-MKT-016, `shows`). It may instead be the low-stock notice (CM-INV-004), which the sibling sub-field notify_quantity ('Notify at Quantity Threshold') suggests.
- **55, 59, 86, 90, contact information and store address on CM-ACC-006:** a reading. That CM-ACC-006 holds the store's address isn't stated in its cell's reading; its permissions cover basic info and contact details.
- **77, show-product-id (الرقم المخزني, 'product inventory number'):** read as the SKU, so CM-CAT-001. CM-INV-001 is the alternative.
- **83:** a new thing, or the order's own recipient (CM-ORD-001's order.customer.updated)? I read the delegate as another person than the order's owner, so not the same thing.

## Structures whose items and sources disagree

- **`importer-schema-fields @products.physical`:** the items follow the source's `groups`. The source's `fields` also hold:
  - twelve fields in no group, so in no entry: status, subtitle, promotion_title, enable_upload_image, enable_note, category_metadata_title, _url and _description, brand_id, with_tax (with tax_reason), tags and new_quantity;
  - `notify_subscribers`, listed in the group Inventory, defined only as a sub-field of `quantity`.

  The register's count, '36 fields in 7 groups', holds: the groups name 24 of the 36 fields, and notify_subscribers.
- **`invoice-settings`:** the items agree with the sources. Three things to note:
  - The English page's line under Upload watermark and Upload stamp, 'If you're using a custom template, we’re happy to help via customer support.', isn't the Arabic page's. That one reads 'لاستيراد طلباتك عبر نموذج من خارج سلة، تواصل مع خدمة العملاء وسنسعد بخدمتك.', which is about importing orders through a template from outside Salla (`20261008T122729Z-sweep-merchant-menus-ar/steps/006.text.txt`, lines 77 and 86, against `20261009T022751Z-sweep-public-demo-en/steps/009.text.txt`). One element, two texts.
  - The public demo's order-status value, [164858023, 1181093211], names ids that aren't among its options. Its page shows 'Select order statuses' with none chosen.
  - The merchant store's show-product-id description has a double space, 'عرض  الرقم المخزني للمنتج', which `show` prints as one. My quote keeps the source's.
- **`export-columns @products`:** the title 'Install Product' against the name `product_pinned` (above). The answer lists match_columns after the other sections; the page draws 'Other columns' first, as the register says.

## What the sources state that no entry holds (for the second stage)

- **The import page** (`20261008T171647Z-journey-advanced-import-demo/steps/002.text.txt`):
  - lines 28 to 31: 'Import faster with Mushammir', 'Auto-detects your data types', 'Maps your columns to the right fields', 'Supports importing multiple files at once'. These are leads for CM-MIG-002 and for Mushammir, Salla's AI assistant (SA-7).
  - line 38: 'Supported formats: XLSX and CSV. Maximum size: 2 MB.', a limit for CM-MIG-002.
- **The Data type step** (`steps/015.text.txt`): line 43, that Products can't be selected while an import for Products is in progress; lines 44 and 45, 'Show products in sales channels' and 'Imported products will appear automatically in all active sales channels.', with Store app and Store website. These are leads for CM-MIG-002 and the sales channels.
- **The import schemas** (`responses/0038.json`) beyond the types:
  - the schema products, 'Import product data including names, descriptions, prices, images, and more', with 294 fields and 21 required;
  - brands, 'Import brand data including basic information and contact details' (7 fields, 2 required), for CM-CAT-005;
  - branch_warehouse, Branches & Warehouses (22 fields, 4 required), for CM-INV-005;
  - languages ar and countries sa, each selected.
- **The brands and branches' fields** (`schema-fields/brands`, step 19; `schema-fields/branch_warehouse`, step 23; no items):
  - brands: logo, banner and meta fields;
  - branches: type, address parts, 'Branch Contact Info', 'Preparation Time', 'Cash on Delivery Support' and 'Cash on Delivery Cost' (a lead for CM-PAY-029 and CM-SHP-007), working hours per day, and branch_code.
- **The physical products' ungrouped fields** (`responses/0051.json`):
  - enable_note, 'Specify whether the customer can add a note';
  - tags, 'Tags that don't exist in your store will be created automatically.', for CM-CAT-006;
  - category SEO, for CM-CNT-007 and CM-CAT-003;
  - with_tax's tax_reason, for CM-TAX-001;
  - status's accepted values ('published', 'hidden', …), for CM-CAT-001;
  - quantity's notify_quantity, 'Notify at Quantity Threshold', for CM-INV-004.
- **The invoice settings page** (`20261008T154824Z-journey-invoice-settings-demo/steps/001.text.txt`):
  - lines 97 to 99: Save, 'Export PDF' and 'Reset to default';
  - lines 100 to 154, the sample invoice: 'Tax/VAT number', 'View tax invoice', and the acknowledgment 'I, the customer, acknowledge receiving the product upon payment. In case of a return or exchange request, the store’s terms and conditions will apply.' These are leads for CM-TAX-005 and CM-TAX-007 (tax invoices) and for CM-RET-001.
- **The product export templates' banner** (the run's note): 'Custom Product Export Templates / Available on your plan', for CM-MIG-003.

## The checker's lines, read again

- **`CHANGES` CM-CAT-012 becomes held, with `core`** (lines 50 and 65; entries 30, Cost Price, and 38, cost_price):
  - The product's export carries its cost price, and the Advanced import takes it onto the product. So Salla keeps a cost on each product: the cell's note's 'A product's cost, entered on the product'.
  - I placed it `core` as the coordinator's check of SA-25 read the order's Order Source on CM-MKT-008. That is a reading.
  - If the coordinator holds such fields to E2's `shows`, both lines become `shows`, and the cell becomes held with no placement.
  - The cell's own reading had searched cost and found only shipping costs and profit reports. These two are the first statements of a cost entered on a Salla product.
- **`NOTE` first leads that hold nothing:** none is the entry's thing.
  - Line 32, CM-OPS-004 (Product Status): WooCommerce's system status report.
  - Line 93, CM-PAY-024 (Digital Card, by 'cards'): the merchant's business cards.
  - Line 95, CM-CAT-012 (Product Bundle, by 'sold'): the bundle's 'sold as a single item' is not a cost. Its cell is named by lines 50 and 65.
- **`NOTE` line 145, the new thing whose entry has leads CM-ORD-008 and CM-ORD-003:**
  - ORD-008 is the setting's own line (144).
  - ORD-003 matched only the words حال and طلب.
  - Both cells were read. Neither holds a delegate.
- **`NEW`:** Shipment receipt by another person, one line (above).

## Problems with this brief or the script

- None that blocked.
- `show` collapses a double space in a field's value (77, above). A quote copied from the print alone would not match the source.
- The brief's rule that every thing an entry names takes a line multiplies `shows` lines on a settings list like this one (I2: 20 lines, none changing a cell). I wrote them, as the rule asks.

## The coordinator's check (31 October 2026, after the batch)

- **The CHANGES line stands: CM-CAT-012, product cost, becomes held with `core`.** It rests on the export's Cost Price (30) and the importer's `cost_price` (38): Salla keeps a cost on each product, as WooCommerce's Cost of Goods Sold does. The ruling after SA-25 and SA-26 makes an export's column or an importer's field `core` on the capability whose data it holds. SA-27 keeps to it.
- **The new thing joins Zid's:** 'Shipment receipt by another person' (83), Salla's show-delegate-details, is ZD-11's thing by the same name. Both are decided with every platform's new things.
- **Four fields have no capability yet:** Add Image Upon Request, Install Product, Calories and Maximum Quantity Per Customer. The last goes to the new-thing decisions beside Zid's minimum and maximum order limit. The others are leads for the second stage, with the 12 importer fields outside every group.
- **The other lines stand:**
  - the export columns and importer groups on CM-MIG-003 and CM-MIG-002, the second now stating what the advanced import holds;
  - the product types on SA-20's capabilities;
  - the invoice settings on CM-ORD-008.
- **Cost:** 15.6 million tokens over 86 requests, about 166,000 an entry. One cell changes: CM-CAT-012, from holding nothing to `core`.
