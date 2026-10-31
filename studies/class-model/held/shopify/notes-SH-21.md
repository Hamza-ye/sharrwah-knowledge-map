# SH-21: notes (Shopify, the held pass)

**The batch:** 130 entries of `app-store-built-in-features`, its entries 52 to 181 of 201, read at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure the pass reads). They are the App Store's pages on features 'Included with Shopify':
- Draft orders, Gift cards, Inventory management;
- Shopify Magic for blog posts and for product descriptions;
- Managed Markets, Shopify Markets, Metafields and metaobjects, Order tracking;
- Payments, Product variants, Shop Pay Installments, Shop Pay;
- Shopify Balance, Shopify Capital, Shopify Payments, Shipping;
- Shopify Tax for the EU and the United Kingdom, and for the United States up to its fourth point. SH-22 has the rest of that page.

**Counts:** all 130 entries are on capabilities: none `out`, none `new`. They take 201 lines:

| Support | Lines |
| --- | --- |
| `core` | 177 |
| `core;own-service` | 3 |
| `own-service` | 13 |
| `shows` | 7 |
| `extension-point` | 1 |

**Effort:** high, as the message names.

**Twins:** `held_entries.py earlier` prints no earlier line and no twin for any of the 130 entries. The concern map holds 23 of these pages' own statements (SH-S-7203 to SH-S-7225). Where an entry heads one of them, its line takes the model's placement of it, and the reading names the statement.

## What I kept from SH-20

- **Each page's feature** is the capability SH-20's table gives it (R20.9). Every page of this batch is in that table.
- **R20.10:**
  - a tagline, point, section heading, list heading or card goes on the capability of the feature it is about, `core`, read with its paragraph and its link;
  - a second thing its words or its paragraph name takes its own line (rule 2);
  - what a paragraph lists in passing takes no line (the ruling after SA-41);
  - a shared point takes one line per page.
- **What SH-20 made second-stage leads (M-12), and I did too:**
  - the items of the pages' lists, each marked Supported or Not supported. They are `li` and aren't entries (`selection.tsv` reads h3, h4, h5 and span);
  - the section paragraphs' sentence on apps, with its link to an App Store category.

  Both are listed below.
- **No frame headings:** none of this batch's entries is one of the four headings every page repeats (R20.11). They are all SH-20's.

## The rules I set

- **R21.1: a 'Not supported' item states that the built-in feature lacks the thing.** So where an entry's own words name a thing its list marks Not supported, that word supports no `core` for the thing. The cases:
  - **'Invoice and receipt features'** (draft orders, entries SH-E-f3dd14e7 and SH-E-062020c4). The list marks 'Not supported Receipts', so the receipts take `shows` on CM-ORD-008. This is how the model places the section's paragraph (SH-S-7225; the ruling after WC-5).
  - **Registering for VAT** (SH-E-91b0ddc1). Its paragraph names where to register, and the lists mark 'Not supported Tax registration'. The line rests on liability tracking alone (CM-TAX-003), and the registering stays the merchant's.
  - **VAT number validation** (SH-E-cf65e40b). The EU and UK lists mark 'Not supported Tax number validation', so the entries on CM-TAX-005 rest on VAT invoices and exemptions only.
  - **VAT invoices on the US page** (SH-E-6a3f2d12). The US list marks 'Not supported VAT invoices', so the CM-TAX-005 line takes the EU and UK pages only.

  If the coordinator wants the items themselves placed, the ruling after WC-5 would make each 'Not supported' item `shows` on its thing's capability, and a Supported item that names another capability's thing `core` there. The items, page by page, are below.
- **R21.2: a card under 'Do more with Shopify tools' takes the capability of the tool it names,** as SH-20's cards do (companies, catalogs, returns). It doesn't always take the page's feature. Examples:
  - Markets Reporting goes on CM-MKS-001 and CM-ANL-002;
  - the translate cards go on CM-MKS-008;
  - the finance cards go on each product's capability.

  Where the card's own words name the page's feature, it takes that line too ('Automate inventory workflows', CM-INV-001).
- **R21.3: one entry that stands for several pages of one feature takes one line, the pages' markets `;`-separated as its scope.** The Shopify Tax entries take 'EU;United Kingdom' or 'EU;United Kingdom;United States', in each page's own words, as SH-20's R20.9 has them. Where a page's paragraph names another thing, that line takes only its own page's market (the ruling after SH-69). Examples:
  - generating invoices: CM-TAX-005, EU and UK;
  - filing and remitting: CM-TAX-006, US.

  SH-E-35c4d4bc stands for four pages with different features, so it takes one line per page, as R20.10 has it.
- **R21.4: the makers.** Each case follows the rulings' last section, and `held_entries.py makers` printed each maker statement:
  - **Shopify Flow** is `own-service` on CM-AUT-001. Its maker statement is “Today we’re introducing test runs in Shopify Flow” (SH-E-0678ff26; the ruling after SH-55).
  - **Translate & Adapt** is `own-service` on CM-MKS-008. The page's possessive 'Shopify’s Translate & Adapt app' names its provider (the ruling after SH-43), and a post names its maker: “we've added automatic translation updates to Translate & Adapt” (SH-E-04551fad).
  - **Shop**, Shopify's consumer app, is `own-service` for its own things (the ruling after SH-34):
    - its real-time order tracking (CM-SHP-017);
    - selling on Shop (CM-CHN-002).
  - **Shop Pay** is the store's checkout, `core` (the correction after SH-45).
  - **Shopify Capital** is a separate product whose own features are `own-service`, as SH-20's R20.9 reads it (the ruling after SH-41; SH-55's E35). The post 'We've just released Shopify Capital for merchants in France.' (SH-E-136aca69) names its maker.
    - The admin's own Capital offers and application stay `core` (the ruling after SH-43).
    - So the tagline and 'Hassle-free application' are `core;own-service`.
  - **Shopify Credit** is `own-service` (the ruling after SH-41; SH-E-e3a378a2).
  - **Shopify Balance and Shopify Bill Pay** are `core`, the admin's own, as their cells read them. No held statement makes Bill Pay a separate product, and its provider Melio isn't named on these pages.
  - **Managed Markets** is the admin's own service, `core` (the correction with the changelog digest). CM-TAX-008's note keeps a merchant of record's duties on CM-MKS-003.
  - **No CM-APP-007 lines.** The links 'Get the app' and 'Turn on fraud prevention' open App Store listings (apps.shopify.com/flow, apps.shopify.com/translate-and-adapt), not the admin's page for the app.
- **R21.5: a claim of effect in the entry's own words takes `shows` on its topic** (R20.10's 'Enhanced SEO' rule). There are four cases:
  - 'Build stronger B2B relationships': CM-B2B-001;
  - 'Improve discoverability with keywords in metafields': CM-CNT-007 (search engines) and CM-SFR-013 (site visitors);
  - 'Reduce cart abandonment': CM-CHK-007.

  A claim made only in a paragraph takes no line, such as 'Fewer disputes, fewer returns' and 'decrease cart abandonment'. 'To build customer loyalty' takes none either: it names no loyalty programme (CM-LOY-004).
- **R21.6: a footnote an entry's paragraph points to is part of the entry** (rule 1). Its limits go in `quality`, and its own conditions in `scope`:
  - Shopify Balance's marks 1, 2 and 3 point to the footnotes at lines 23, 24 and 25;
  - Shopify Payments' asterisk points to line 25;
  - Shipping's asterisk points to line 86. That footnote's condition, 'If you're in the US … on the Grow, Advanced, or Plus plan', becomes the insurance line's scope, `US and Grow;Advanced;Plus`, with 'have Shopify Payments activated' in its reading.
- **R21.7: a party named only in a paragraph goes in `reading`, never in `filler`.** These are UPS, DHL and FedEx in Managed Markets' rates, and the carriers in Shipping's discounts. The checker holds `filler` to the entry's own text, a heading.
- **R21.8: a link's page decides a second line where a cell already holds that page** (rule 2's search for a place's own capability; the ruling after SA-19). There are three cases:
  - **Built-in rate calculator:** its link opens settings/shipping/shipping-calculator, a route CM-SHP-001's cell holds.
  - **'Set up notification emails':** its link opens the customer notifications settings, which the model holds as Order tracking's place (SH-S-7208). So it takes CM-SHP-017 beside CM-NTF-001.
  - **'Add variants to a product':** its link opens products/new, so it takes CM-CAT-001.

## CHANGES, with what I decided

- **CM-INV-008@shopify becomes held and gains `core`, by line 9** (SH-E-d197e1d4, 'Give customers confidence with locked-in prices and reserved inventory'). This is a reading:
  - the draft order's reserved inventory, which 'Guarantee[s] product availability', is stock held for an order not yet paid. That is CM-INV-008's thing (its note: WooCommerce's Hold stock, for a pending order);
  - the platform's own draft orders do it, so `core`.

  I kept it. The other reading is that the reservation is a stock state of CM-INV-001, which would change no cell. What would settle it is listed below.
- **CM-B2B-004@shopify gains `core`, by line 15** (SH-E-ae3e8482, 'Create sales quotes to close more deals'). The card states:
  - that the draft order makes B2B sales quotes, 'Grow B2B sales using personalized sales quotes with customized discounts and payment terms.';
  - in the admin's own draft order route, through its link 'Create quote'.

  The list also marks 'Supported Quotes'. CM-ORD-005's note says 'whether Shopify's drafts serve quotes, isn't stated', and this card states it. The quote the store returns is half of CM-B2B-004's definition, and the buyer's request isn't named. I kept it.
- **CM-SHP-017@shopify gains `own-service`, by lines 94 and 133.** These are Shop's order tracking, in 'Order status updates by email or through the Shop app' and in Shop Pay's 'Improve the post-purchase experience' (“Shop's centralized, real-time order tracking feature”). Shop does its things as `own-service` (the ruling after SH-34), and SH-20 placed Shop's sign-in the same way. I kept it.
- **CM-AUT-001@shopify gains `own-service`, by lines 46 and 169** (Shopify Flow, on Inventory's and Shopify Payments' cards). The ruling after SH-55 aligned 38 Flow lines to `own-service`, and the cell isn't amended from them yet. I kept it.
- **CM-MKS-008@shopify gains `own-service`, by lines 55 and 60** (Translate & Adapt). The ruling after SH-55 aligned its line, and the cell isn't amended yet. I kept it.

## The checker's NOTE lines, answered

- **`own-service` on CM-AUT-001, CM-MKS-008, CM-SHP-017, CM-CHN-002, CM-PAY-025 and CM-PAY-026:** R21.4. CM-PAY-026's cell already holds `own-service`, CM-PAY-025's too.
- **Line 145, `core` on a product named with the platform's brand** (Shopify Balance, on its own card): it is `core` by what the entry and the cell show. It is the admin's own money account (the correction after SH-41), and the brand names no maker. Bill Pay's two lines rest the same way, on its cell's admin routes.
- **First leads whose cells hold nothing, which no line names.** Each matched only a word:
  - line 4: CM-ORD-003 (order statuses), by 'customize, order';
  - line 73: CM-MKS-009 (countries reference data), by 'countries';
  - line 75: CM-B2B-005 (shopping lists), by 'buyer, shopping';
  - line 76: CM-SFR-014 (BigCommerce's headless sites and routes), by 'route, site';
  - lines 91 and 187: CM-OPS-004 (system status and tools), by 'tools';
  - line 134: CM-APP-010, by 'integration';
  - line 142: CM-LOY-003. It is the buyer's cashback into a wallet, and Balance's cashback is the merchant's card's (CM-PAY-024).

## New things

None. I searched before each line that no lead named:
- payment terms;
- reserve inventory;
- quote;
- invoice, receipt, credit note and packing slip;
- Shopify Flow, workflow, automation and bulk edit;
- blog, article, translate and product description;
- product content and tone;
- metaobject and metafield;
- product category, collection and storefront search;
- order status page, Shop app, tracking page and post-purchase.

Each found an existing capability, or a homonym.

## Entries I couldn't tell, and what would settle each

1. **Reserved inventory** (SH-E-d197e1d4, CHANGES). It is CM-INV-008's stock held for an unpaid order, or CM-INV-001's stock state. The draft orders help page the card links would settle it: help.shopify.com/en/manual/fulfillment/managing-orders/create-orders (`apps.shopify.com_built-in-features_draft-orders/items.jsonl`, line 60). That page isn't among what the brief lets me read.
2. **Shopify Capital's own features as `own-service`** (seven lines). I followed SH-20's R20.9 and the ruling after SH-41's reference to SH-55's E35. But SH-35 placed the post 'We've just released Shopify Capital for merchants in France.' as `core` (SH-35:57). If the coordinator reads Capital as the admin's own service, as Balance's correction does, the lines become `core`. CM-PAY-026's cell would still hold `own-service` from other rows.
3. **Shopify Capital's asterisk.** The card's paragraph ends 'admin.* Available in US only' (line 17). I read the asterisk as carrying its own note, so the card's other products take 'US' as scope. The page's footnote at line 22 also begins '* Funding through Shopify Capital…' (SH-S-7218). If the line 17 mark points there instead, the 'US' scopes go, and WebBank's lending joins the card's reading.
4. **CM-SHP-015 `core` for Managed Markets' negotiated carrier rates** (SH-E-dd3f0bf6). The carriers are under the platform's contracts, which CM-SHP-015's definition holds. The model gives 'labels from Shopify supported carriers' only `shows` there (core in CM-SHP-002). No cell changes either way.
5. **The order status page's capability.** I placed the buyer's tracking page and order status pages on CM-SHP-017, and their customization at settings/checkout on CM-CHK-003. No capability names the order status page itself: CM-ORD-003's note calls it a homonym and points to CM-CUS-014's extension targets. A capability for the buyer's post-purchase pages would settle it.

## Items and sources that disagree

- **The pages' lists contradict one another:**
  - **Low stock alerts:** Inventory marks 'Not supported Low stock alerts' (`apps.shopify.com_built-in-features_inventory/items.jsonl`, line 50). Product variants marks 'Supported Low stock alerts' (`apps.shopify.com_built-in-features_product-variants/items.jsonl`, line 53).
  - **Branded tracking page:** Order tracking marks 'Supported Branded tracking page' (`apps.shopify.com_built-in-features_order-tracking/items.jsonl`, line 21). Shipping marks 'Not supported Branded tracking page' (`apps.shopify.com_built-in-features_shopify-shipping/items.jsonl`, line 41).
  - **Pre-orders:** Inventory marks 'Supported Pre-orders' (line 45). SH-20's notes have B2B's 'Pre-orders' not supported.
  - **Multi-language and Translation:** the blog's list marks both Supported (`apps.shopify.com_built-in-features_magic-blog-posts/items.jsonl`, lines 28 and 29). The product content list marks both Not supported (`apps.shopify.com_built-in-features_magic-product-descriptions/items.jsonl`, lines 43 and 44). The second may be the AI's generation only, a reading.
- **Tax number validation against the model's VAT validation.** The EU and UK lists mark 'Not supported Tax number validation' (line 32). CM-TAX-005's cell holds VAT validation `core`: business customers enter a VAT number at checkout to claim the reverse charge (SH-S-0535). The two may be different things, validating against a registry or only collecting the number. Nothing I may read settles it.
- **A point whose paragraph is about something else:** on the EU and UK pages, the point 'Generate VAT invoices' has the paragraph 'Easily accommodate tax exemptions for specific customers or products, ensuring compliance with local tax requirements.' Both are CM-TAX-005's.
- **The platform's own typos** in the tax lists' groups, quoted as written: 'Tax calcluation' and 'Exemption managment'.
- **A help page linked on the admin's host:** the card 'Activate VAT invoices' links admin.shopify.com/manual/taxes/shopify-tax/vat-invoices (line 47).

## What a source states that no entry holds (leads for the second stage)

**The lists' items** (`li`, each marked Supported or Not supported). Each 'Not supported' is the platform stating what the built-in feature doesn't do, and the item's file is the page's `items.jsonl`.

The 'Not supported' items, page by page:

| Page | Lines | Supported | Not supported, with notes |
| --- | --- | --- | --- |
| draft-orders | 21 to 54 | 3 | 29: every document type but Invoices, Quotes and Draft orders, and every customization and file management item. Among them are Receipts, Credit notes, Order confirmations, Packing slips, Shipping labels, Refunds, Returns, Multi-currency, Multi-language and PDF generation |
| gift-cards | 21 to 43 | 16 | 5: Bulk, Reloadable, Store credit (as a card type; store credit is CM-LOY-001's own built-in feature), Reminders, Gift card import |
| inventory | 21 to 56 | 28 | 6: Auto-restock, Forecasting, Restock notifications, Back-in-stock alerts, Replenishment reminders, Low stock alerts. CM-INV-004 (low stock) holds nothing on Shopify; this item and the variants page's 'Supported Low stock alerts', 'Supported Threshold alerts' and 'Supported Out of stock notifications' (inventory, lines 51 and 52) are its leads |
| magic-blog-posts | 21 to 58 | 10 | 26: among them Templates, Author bio, Embedded products, Shoppable links, Rich snippets, Alt tags, Permalinks, URL optimization, XML sitemap, Featured posts, Related posts. Supported are Comments, Article tags, Meta tags, Auto-scheduling, Custom code and others: leads for CM-CNT-004 |
| magic-product-descriptions | 21 to 58 | 5 | 31: every content type but Descriptions and Blog posts, and most creation and SEO items |
| metafields-and-metaobjects | 21 to 49 | 25 | 3: Bulk import and export, Versioning, Backups |
| order-tracking | 21 to 40 | 18 | 1: Carrier masking |
| product-variants | 21 to 59 | 27 | 10: Checkboxes, Conditional logic, Fonts, Dates, Multi-select, Radio buttons, Gift wrap, Custom CSS, Custom HTML, Preview |
| shopify-shipping | 21 to 78 | 47 | 3: Barcode scanning, Branded tracking page, Customer-based (rates) |
| shopify-tax-eu, shopify-tax-uk | 21 to 43 | 11 | 9: Tax registration, Tax number validation, India (GST), Canada (HST, PST, GST), US (Sales tax), Compliance reporting, Multi-state filing, SST filing, Local tax returns. For CM-TAX-003 and CM-TAX-006, these are the platform stating that Shopify Tax neither registers nor files in the EU and the UK |
| shopify-tax-us | 21 to 43 | 10 | 10: VAT invoices, Custom invoices, Tax registration, Tax number validation, IOSS and OSS (EU), EU (VAT), India (GST), Canada (HST, PST, GST), SST filing, Local tax returns |

**The section paragraphs' apps, and their App Store categories.** These are `extension-point` leads, as SH-20 kept them. 'Already held' means the cell already holds that category.

| Page | Category | Capability |
| --- | --- | --- |
| draft-orders | invoice and receipt apps (`orders-and-shipping-orders-invoices-and-receipts`) | CM-ORD-008, already held |
| gift-cards | gift card apps (`marketing-and-conversion-gifts-gift-cards`) | CM-LOY-002, already held |
| inventory | inventory optimization apps (`orders-and-shipping-inventory-inventory-optimization`) | CM-INV-001, whose cell is `core` only |
| magic-blog-posts | blog apps (`store-design-content-blogs`) | CM-CNT-004, already held |
| magic-product-descriptions | product content apps (`store-design-content-product-content`) | CM-AIA-003, `core` only |
| metafields-and-metaobjects | metafield apps (`store-design-content-metafields`) | CM-CNT-002, already held |
| order-tracking | order tracking apps (`orders-and-shipping-orders-order-tracking`) | CM-SHP-017, already held |
| product-variants | product variant apps (`selling-products-custom-products-product-variants`) | CM-CAT-002 |
| shopify-shipping | shipping apps (`orders-and-shipping-shipping-solutions-shipping`) | CM-SHP-002 |
| shopify-shipping | shipping rate apps (`…-shipping-rates`) | CM-SHP-001 |
| tax pages | tax apps (`store-management-finances-taxes`) | CM-TAX-004, already held |

The tax pages' apps sentence also names what the apps add:
- on the EU and UK pages: 'Tax apps offer additional features, like registrations and filing.' This is a lead for CM-TAX-003 and CM-TAX-006;
- on the US page: 'registrations and tax compliance management outside the US, EU and UK.'

**Other lines no entry holds:**
- **Managed Markets' fees** (`apps.shopify.com_built-in-features_managed-markets/items.jsonl`, line 25, under Learn more): 'Transaction fees apply. See Managed Markets pricing for details.' A fee lead for CM-MKS-003's qualities.
- **Shopify Payments' tagline** lists what the service accepts: 'cards, Shop Pay, wallets, installments, agentic payments and crypto'. I placed it on CM-PAY-002 alone, as a list of what may be used (the ruling after SA-41). Two of its words are leads:
  - 'agentic payments', for agents paying through Shopify Payments, which no capability holds as such (CM-AIA-005 holds agents' channels);
  - 'crypto', which CM-PAY-018 already holds through Shopify Payments.
- **The disclaimers the model already holds:** Shopify Balance's partners (line 22, SH-S-7217), Shopify Capital's lenders (line 22, SH-S-7218) and Shop Pay Installments' (line 21, SH-S-7219). No entry of mine names them.

## Problems with the brief or the scripts

- **The checker tests `terms` and `filler` against the entry's own text, here a heading.** So the things a paragraph names can't be terms or fillers: the carriers, and the finance products on the cards. I left those terms empty and named the parties in `reading` (R21.7). This follows the brief's rule 5, but this structure's entries carry almost all their words in their paragraphs.
- **The brief has no rule for a list's 'Not supported' marks.** It has one for a ✔ under a row (rule 2), and the ruling after WC-5 for an offer stated unavailable. R21.1 is how I read them for this structure. Whether the items should be placed through their list heading is the coordinator's to decide with SH-20's four lists and SH-22's.

## The coordinator's check

Measured: 21.8 million tokens over 95 requests, about 168,000 an entry. The checker prints no problem.
- **Kept:** every line and every `CHANGES` line: CM-INV-008 by the draft orders' reserved inventory (a marked reading), CM-B2B-004 by the card's sales quotes, and Shop's tracking, Flow and Translate & Adapt `own-service` by their makers held. R21.1 to R21.4 stand for SH-22.
- **Shopify Capital:** this batch's lines follow the router digest's table: the admin's Capital section and its application `core`, Capital's own features `own-service`, its maker held (SH-S-0484, SH-S-0491, SH-S-0493). SH-35:57, an application 'directly through their Shopify admin', stays `core`, as the changelog digest's table has it. The Editions digest's rule 21 and E156 still name Capital `shows` by its brand alone; that predates the maker the router batches found, so those lines go to Shopify's amendment with the other no-maker lines (`amendment-notes.md`).
- **The lists' Supported and Not supported items** stay second-stage leads, as SH-20 had them; the contradictions between pages (low stock alerts, branded tracking, pre-orders, translation) and the tax number validation against CM-TAX-005 are leads in this batch's notes.
