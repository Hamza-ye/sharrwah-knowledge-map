# SH-22: notes (Shopify, the held pass)

**The batch:** 110 entries of five structures, read at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure the pass reads):
- `app-store-built-in-features`, entries 1 to 20, the last 20 of its 201: the end of Shopify Tax for the United States (its card 'Set up automated filing'), and the pages Shopify Theme Store, Sidekick and Store credit;
- `app-store-registration`, entries 21 to 34: the form 'Register for the Shopify App Store' at partners.shopify.com/5236935/apps/register, in its two states (run `20261007T010009Z-journey-partner-dashboard`, steps 079 and 080);
- `billing-charge-categories`, entries 35 to 69: the 35 options of the expense report's picker 'Charge categories' that nothing cites, at settings/organization-billing/expense-report on fake-demo-sharrwah (run `20261005T102756Z-journey-organization-billing`, step 12);
- `billing-subscription-downgrades`, entries 70 to 73: the four subscription downgrades of the trial store 2jiwxs-gr, in the answer NewAccountPricing (run `20261006T232216Z-journey-signup-new-account`);
- `bulk-editor-columns`, entries 74 to 110: the Columns panels of the collection and variant bulk editors on capture-plus (run `20261005T133736Z-journey-bulk-editors`, steps 016 and 002).

**Counts:** all 110 entries are on capabilities: none `out`, none `new`. They take 117 lines:

| Support | Lines |
| --- | --- |
| `core` | 84 |
| `shows` | 28 |
| `extension-point` | 3 |
| `core;extension-point` | 1 |
| `own-service` | 1 |

**Effort:** high, as the message names.

**Twins:** `held_entries.py earlier` prints no earlier line and no twin for any of the 110 entries. Two kinds of twin are held outside the held pass, and I took their lines:
- the charges table's filter (step 042) holds the same charge categories, which the concern map holds as inventory entries SH-I-1322 to SH-I-1358; 14 of them are placed in the model (`merged/evidence.tsv`);
- SH-86's line on the registration's route (SH-E-97246369, CM-APP-002 `core`), and earlier lines on the bulk editor's fields (SH-14, SH-34, SH-36, SH-37, SH-43, SH-46, SH-96), each named in its reading.

## `app-store-built-in-features` (entries 1 to 20): what I kept

- **Each page's feature** is the one SH-20's table gives it: shopify-tax-us CM-TAX-002 (its card on filing CM-TAX-006), shopify-theme-store CM-SFR-003, sidekick CM-AIA-002, store-credit CM-LOY-001.
- **R20.10:** a tagline or point goes on its page's feature, `core`, read with its paragraph and link; a second thing its words or paragraph name takes its own line; what a paragraph lists in passing takes no line.
- **R21.2:** a card takes the capability of the tool it names: 'Customizing themes' CM-SFR-002, 'Page builder apps' CM-SFR-006, 'Set up new customer accounts' CM-CUS-010.
- **R21.4, the makers:** Shopify Flow `own-service` on CM-AUT-001 (“Today we’re introducing test runs in Shopify Flow”, SH-E-0678ff26).
- **R21.5:** 'Peace of mind' names no topic, so it takes no claim-of-effect line.
- **R21.8:** a link's page decides a second line where a cell holds that page:
  - 'Edit store design' opens themes/editor, CM-SFR-002's route (SH-S-5211);
  - Store credit's Get started opens settings/customer_accounts, CM-CUS-010's settings page.
- **R21.1:** none of these pages' lists marks a thing an entry names Not supported. The Theme Store, Sidekick and Store credit pages have no list.
- **R20.11:** none of my entries is a frame heading.

Three readings of mine on these pages:
- **Sidekick is `core`, not `own-service`.** The tagline says 'Your free AI assistant from Shopify—right in your admin.', and 'from Shopify' is a maker's cue (the ruling after SH-55). But Sidekick is the admin's own assistant at its own route (sidekick), on the plan line for every plan, not an app of its own. So it stays `core`, as Shopify Balance does (the corrections with the Editions digest).
- **Flow's card takes CM-APP-007.** The card 'Automate workflows the simple way' links admin.shopify.com/apps/flow, the admin's page for the app, which CM-AUT-001's cell holds as the admin link Flow. So it takes CM-APP-007 `core` (M-10; the ruling after SH-43). SH-21's Flow links opened App Store listings, so they took none.
- **Loyalty apps issuing store credit are `extension-point` on CM-LOY-001.** The card 'Build brand loyalty with store credit' says 'Use loyalty and rewards apps to automatically issue store credit to customers…'. Third parties' apps issue the store's credit through the App Store's category, so the card takes CM-LOY-001 `extension-point` beside CM-LOY-004's (M-8). See CHANGES.

## The rules I set, for the coordinator to check

- **R22.1: the App Store registration form's questions, options, fields and checkbox are the registration's own, `core` on CM-APP-002.** This is how SH-86 places the route /:orgId/apps/register (SH-E-97246369; E86) and how the message reads it, as the platform's own step for developers.
  - What the developer answers or types is its own data and goes in `reading`. That covers the Partner IDs, emails and business names the run typed (step 080).
  - The form's conditions go in `reading`, since they depend on the form's own values. 'I have other accounts' opens 'Associated accounts'. 'This the first of my accounts that I’m registering' opens 'About your associated developer accounts'. 'I already registered at least one…' opens the Partner ID field.
  - Consecutive entries with one reading are grouped: 21 to 23, 24 to 26, 27 and 28, and 31 to 34.
  - The form's 'organization' isn't CM-PTN-002's Partner Dashboard Organization or CM-ACC-003's organization of stores. Those are homonyms.
- **R22.2: a form section's paragraph is the words of the fields under it** (rule 1). Where the paragraph names another thing, those fields take its line:
  - **Revenue share (entries 27 and 28).** The 'Associated accounts' paragraph, “You have to register each account … to take advantage of 0% revenue share up to $1 million USD (15% on additional sales over $1M).”, names the revenue share. The model holds that revenue share on CM-PTN-003 as the App Plan's, for 'An App Developer that has met certain registration requirements' (SH-S-0287). So the two options take CM-PTN-003 `shows`, with the share as their quality.
  - **Account verification (entries 31 to 34).** The paragraph 'To claim your accounts … it may take a day or two for Shopify to verify that each account belongs to you.' names the platform checking the partner's accounts. That is CM-PTN-002's, whose reading finds no verification of the partner held, so these fields take CM-PTN-002 `core`.
- **R22.3: the checkbox 'I verify that this information is correct and meets all the Associated Accounts requirements outlined in the Partner Program Agreement.'** It takes CM-APP-002 `core`, as the registration's own step. It also takes CM-PTN-001 `shows`: the agreement is the programme's terms, which its cell holds as `shows` (SH-S-0288), and the developer verifying that it meets them makes the developer responsible.
- **R22.4: a charge category takes two lines.**
  - **(a) The billing line.** One line for all 35 entries, CM-PLN-004 `core`: the picker is the platform's own billing's list of its charges. The cell holds the organization settings page Billing, and the expense report is at settings/organization-billing/expense-report.
  - **(b) The thing charged for, `shows` on its own capability.** This is how the model places the charges filter's twins: 13 of the 14 placed twins are `shows` (SH-I-1324 to SH-I-1354). A category gives the thing's terms, in that the bill charges for it, and shows that the platform has the thing. It names neither the thing's maker nor who does it.
  - **Categories that name no thing.** Four categories name no thing that the held sources define: Add-on fees, Other fees, Platform fees and Shopify Buyers fees. They take line (a) alone, and their things are gaps (below).
  - **Fillers.** A category that names a third party takes it as filler: 'Avalara add-on fees', Avalara, on CM-TAX-004.
- **R22.5: a category whose thing is itself one of the billing capabilities' own charges is `core` there.** The platform's bill charging its own plan, fee or app charge is the platform doing that thing:
  - Subscription charges and Subscription discount: CM-PLN-001;
  - Transaction fees (ORDER_COMMISSION) and Transaction fees discount: CM-PLN-003, whose cell holds the fees on Shopify's own billing page (SH-S-6314);
  - App fees: CM-APP-003, whose cell holds app charges added to the merchant's Shopify invoice (SH-S-0281).

  'Tax transaction fees' (SHOPIFY_TAX) is Shopify Tax's fee, so it goes on CM-TAX-002 as its twin does. It isn't CM-PLN-007, which is the tax on the platform's own charges.
- **R22.6: a twin's line is kept.** The Tap to Pay twin is `core` in the model (SH-I-1352 on CM-PAY-021, whose reading has 'Shopify bills Tap to Pay transaction fees' under core). I kept `core` for it. Every other twin is `shows`. The coordinator may align the two ways (below).
- **R22.7: a category naming a first-party product stays `shows`.** The cases:
  - Messaging (value SHOPIFY_EMAIL), CM-MKT-007;
  - Shopify collabs commission and processing fee, CM-MKT-013;
  - Shop Campaigns, CM-MKT-012;
  - the three Shopify Fulfillment Network categories, CM-SHP-012.

  A maker statement is held for each: Messaging (the ruling after SH-37), Collabs' publisher Shopify Inc. (SH-S-2760), the Fulfillment Network's 'our network…' (the corrections after SH-41), and Shop Campaigns' own terms (CM-MKT-012's cell). But a charge line states no feature of the product. A plan line that includes an app stays `core` whatever its maker (the ruling after SH-55), and in the same way a charge line keeps what the charge shows. The twins of Messaging, Collabs commission and Shopify Logistics are `shows` too.

  If the coordinator reads the ruling after SH-37 ('every line about it') to cover charge lines, seven lines become `own-service`: entries 49, 58, 60, 61, 62, 63 and 64. The model's twins SH-I-1333, SH-I-1345 and SH-I-1349 would be aligned at Shopify's amendment.
- **R22.8: a subscription downgrade is CM-PLN-001 `core`, the plan its scope** (the message). It is the platform's own billing API on its own plans, a plan policy it lists for an account (rule 2's out list).
  - The scope is the source's own identifier: DORMANT, BASIC, PROFESSIONAL or UNLIMITED. The same answer's planSummaries give BASIC, PROFESSIONAL and UNLIMITED the plans Basic, Grow and Advanced, by internalName basic, professional and unlimited. A reading: the downgrade's upper-case name is the same identifier.
  - The values go in `reading`. They are false for every cycle, since 2jiwxs-gr is a store on its trial.
  - The eligibility also names the billing cycles monthly, yearly, biennial and triennial (BillingBillingCycleDowngradeEligibility). Those are the subscription's billing period and term, CM-PLN-002's, so each entry takes a CM-PLN-002 `core` line with the same scope.
  - No downgrade names what the plan keeps or loses.
- **R22.9: a bulk editor column is a field of the record the editor edits, `core` on the field's capability** (the message). A group heading is a container on the capability its title names (M-13). The fields by capability:
  - the collection's title and sort order: CM-CAT-003;
  - its template, a theme template: CM-SFR-001;
  - sales channels, the publish date and the Online Store's schedule: CM-CHN-001, with CM-SFR-001 for the Online Store that 'Online store schedule' names;
  - SEO's page title, meta description and URL handle: CM-CNT-007;
  - the variant's title and barcodes: CM-CAT-002 (SH-34:42);
  - price, unit price and compare-at price: CM-CAT-001, a price kept on the product record (the corrections with the changelog digest; SH-14:6);
  - cost per item: CM-CAT-012 (the ruling after SA-25; SH-46:89);
  - charge taxes: CM-TAX-001;
  - SKU, continue selling when out of stock and track quantity: CM-INV-001 (SH-43:131);
  - package, weight, packed dimensions and physical product: CM-SHP-001 (SH-36:206);
  - harmonized system code and country of origin: CM-SHP-020. CM-TAX-008's note sends a product's customs data for shipping there, and SH-37:168 places the same fields there.

  Two choices in it:
  - **'General'** is placed on the record each editor edits, CM-CAT-003 and CM-CAT-002, as that record's general fields. It names a grouping of one record's fields, not several capabilities' pages, so I didn't read it as out (the ruling after SA-28).
  - **'Pricing'** is CM-CAT-001's. CM-CAT-013, 'Product pricing', holds only pricing apps on Shopify, and no statement defines what its pricing is, so its name alone gave no line. This is listed below.

  **No bulk-editor line.** The message asks for the bulk editor's own capability where the cells hold one, and no cell holds these two editors. CM-CAT-001 holds only the product editor, bulk/product (SH-S-5009). The variant editor's route, product_variant:bulk-edit at bulk/product_variant, is in the concern map (SH-S-5177 and SH-S-5010, SH-C-022, section Inventory) but no cell cites it. bulk/collection is cited by nothing. So no column takes a line for the editor itself. The coordinator may give the two routes their cells (CM-CAT-002 or CM-INV-001, and CM-CAT-003) at amendment.
- **R22.10: a group of columns that the store's own data names.**
  - **Locations.** 'Quantities by location' has one column for each of the store's locations: 'My Custom Location', 'Shop location' and 'Snow City Warehouse'. Each column is the platform's own field, the variant's quantity at that location, so it takes CM-INV-001 and CM-INV-005 `core`, as its group's title does (M-6 refined). The labels are the store's own data, as SH-96:38 reads 'Shop location', so they go in `reading`, never in `terms`.
  - **Region catalogs.** The heading is CM-B2B-003 `core`, whose note holds catalogs for region markets (SH-S-5101). Its one column, 'Catalog for Canada', is `disabled` in the source (`steps/002.html`). The platform lists it but doesn't offer it to this store to choose, with no reason stated, so it is `shows`.
  - **Bins.** 'Bin names by location' takes CM-INV-001 `core`, as SH-36:211 places the Bin name column that the Inventory CSV and the Inventory Bulk Editor hold 'for each variant–location row'. It also takes CM-INV-005 `core` for the locations its title names.

## CHANGES, with what I decided

- **CM-AUT-001@shopify gains `own-service`, by line 19** (Flow, on Sidekick's card). The ruling after SH-55 aligned 38 Flow lines to `own-service`, SH-21 had the same CHANGES, and the cell isn't amended from them yet. I kept it.
- **CM-LOY-001@shopify gains `extension-point`, by line 30** (entry 20). The card says loyalty and rewards apps 'automatically issue store credit to customers', and its link opens the App Store's category Loyalty and reward apps (SH-I-1820, CM-LOY-004's). Third parties do a thing of store credit's, issuing it, through something the platform provides (B-extent; M-8). I kept it.
  - The other reading is that the apps do only the loyalty programme (CM-LOY-004) and the store credit is the platform's, already `core`. On that reading the line would go, and no other cell would change.
- **CM-SHP-020@shopify gains `core`, by lines 109 and 110** (entries 102 and 103, 'Harmonized system code' and 'Country of origin'). The cell is `not-stated` on Shopify: its reading says no Shopify statement held names an HS code or a country of origin.
  - The variant bulk editor offers both as columns under Shipping, the platform's own admin keeping the product's customs data.
  - SH-34, SH-36, SH-37, SH-42 and SH-46 already place HS codes and country of origin on CM-SHP-020 `core`, and the cell isn't amended from them yet.
  - I kept it.

## The checker's NOTE lines, answered

- **`own-service` on CM-AUT-001:** R21.4, as above.
- **Line 33, first lead CM-API-013 (Account-level API) holds nothing, and no line names it.** The lead matched only the words 'account', 'all' and 'one' (`by name`). Entries 27 and 28 are the registration's answers on the developer's other accounts, not an API over accounts. It is no lead.

## New things

None. I searched before each line that no lead named:
- image generation and AI image;
- add-on and addon;
- POS Pro;
- Shopify Buyers and buyers program;
- partner ads, app ads and App Store ads;
- application commission;
- platform fee;
- shipping insurance and insurance;
- subscription discount and expense report;
- pause, dormant, Pause and build and deactivate;
- downgrade, plan change, switch plan, billing cycle and billing period;
- bulk editor, bulk edit, bulk actions and the editors' routes;
- collection, sort order, template, publish date, schedule, page title, meta description and URL handle;
- compare-at price, unit price, cost per item and charge taxes;
- SKU, barcode, continue selling, oversell, backorder and track quantity;
- package, weight, dimensions, physical product and digital product;
- harmonized system code, HS code, country of origin and customs;
- bin, bin name, storage location and shelf;
- region catalog and catalog.

Each found an existing capability or a homonym, or nothing (the charge categories that name no thing, below).

## Entries I couldn't tell, and what would settle each

1. **The four charge categories that name no thing** (R22.4):
   - Add-on fees (ADDON_FEE): which add-ons. Shopify Protect is 'offered as an add-on to the general Shopify Payments services' (SH-S-0402), but the category names none;
   - Other fees (OTHER);
   - Platform fees (PLATFORM_FEE). CM-PLN-003 is a 'Platform fee' on sales by its name, but the category doesn't say it is on sales, and ORDER_COMMISSION is its own category;
   - Shopify Buyers fees (SHOPIFY_BUYERS). No held statement I may read names Shopify Buyers. The run's steps hold it only in the picker and the filter.

   Shopify's help on the bill's charges would settle each. It isn't among what the brief lets me read.
2. **Partner ads and Partner application commission** (entries 51 and 52). I placed them by their names alone:
   - Partner ads: the ads partners run on the App Store, CM-APP-002 `shows`, as SH-86 places App ads (E86);
   - Partner application commission: the platform's share of partners' app charges, CM-APP-003 `shows`.

   Why a store's organization bill lists them isn't stated. The same help would settle it.
3. **DORMANT** (entry 70): the answer's planSummaries name no such plan, so what it is, and what it keeps or loses, isn't stated.
4. **The Tap to Pay twin** (R22.6): `core` in the model, against `shows` for the other 13 placed twins. One reading should hold for all: `shows`, which R22.4 gives, or `core` throughout.
5. **'Pricing'** (entry 86): CM-CAT-001 by the cells' readings, or CM-CAT-013 by its name. If the coordinator reads CM-CAT-013 as the merchant setting product prices, the heading would make its Shopify cell gain `core`.
6. **'General'** (entry 74): placed on the editors' records (R22.9). Read as a title naming only a grouping (the ruling after SA-28), it would be `out`. No cell changes either way.
7. **The location and catalog columns** (R22.10): placed as the platform's fields per location and per catalog. Read as the store's own data, as SH-96 reads a location's name, they would be `out`, with their headings carrying the fields. No cell changes either way.
8. **Bins:** SH-64 keeps the Editions' 'Bin locations in the Order Printer app' as `new:Bin locations`, `shows`, with no place of its own and parent CM-INV-005. SH-36 places the changelog's Bin name column on CM-INV-001 `core`, and I kept to SH-36, since this is the admin's own bulk editor. The coordinator may merge the two: either the new thing joins CM-INV-001 or CM-INV-005, or this batch's and SH-36's lines join the new thing.
9. **Entry 15's second line** (R21.8): Store credit's Get started opens the customer accounts settings. Store credit's own settings may be on that page, but no held statement I read says so.

## Items and sources that disagree

- **`bulk-editor-columns`, capture-plus@product_variant:** the item list leaves out the switch 'Show bin names' under 'Bin names by location'. It is an `s-internal-switch` (`raw/runs/20261005T133736Z-journey-bulk-editors/steps/002.html`; `002.text.txt`, line 85), and the extractor takes `s-checkbox` elements, by the register. The source governs: I read the heading with its switch.
- **The items leave out the source's `disabled` marks:** 'Title' in both editors, which the text shows checked and so always chosen, and 'Catalog for Canada' (`002.html`, `016.html`). R22.10 reads the second.
- **`billing-charge-categories`:** the picker and the filter label two values differently, as the register says:
  - MANAGED_MARKETS_SHIPPING_FEE is 'Managed Markets' in the picker and 'Managed Markets shipping fees' in the filter;
  - the picker labels both SHOPIFY_FULFILLMENT and SHOPIFY_LOGISTICS 'Shopify Fulfillment Network charges', and the filter labels the second 'Shopify Logistics'.

  Each entry's reading names the filter's label where it differs.

## What a source states that no entry holds (leads for the second stage)

- **The registration page** (`20261007T010009Z-journey-partner-dashboard/steps/079.text.txt`; SH-86's notes hold the same from step 041):
  - 'Register for the Shopify App Store' and 'Unlock 0% revenue sharing (15% on additional sales over $1 million USD annually) and create unlimited public apps.': the revenue share is a quality for CM-PTN-003 (SH-S-0287), and 'unlimited public apps' is a lead for CM-APP-002's distribution;
  - 'One-time app store registration fee: $19' and 'Add payment method': a fee for CM-APP-002, and for CM-PTN-004, whose bill covers 'paying to register' (SH-86's line 135);
  - the 'Add credit card' modal (step 073): card number, expiry, CVV and a billing address whose Country reads Yemen.
- **The expense report itself** (`20261005T102756Z-journey-organization-billing/steps/012.text.txt`): 'Create expense report', 'Customize your report by selecting specific stores, charge categories, and dates.', with a date range. CM-PLN-004's cell lists the billing routes it holds, and no expense report is among them. The page and its route, settings/organization-billing/expense-report, are a lead for that cell.
- **The picker's other options**, 'All' and 'Taxes' (TAXES, SH-I-1358), aren't entries. 'Taxes' is CM-PLN-007's, the tax on the platform's charges.
- **The downgrades' answer, NewAccountPricing** (`structures/shopify/billing-subscription-downgrades/2jiwxs-gr/source.0.json`), states plan summaries that no entry holds:
  - the plans Starter (starter_2022, 'For selling on social', $5 a month), Basic, Grow, Advanced and Plus, with monthly and annual prices;
  - **biennial and triennial monthly prices** on every plan: Basic 20 and 18, Grow 56 and 52, Advanced 235 and 219, Plus 2,500 and 2,300 USD. CM-PLN-002's Shopify cell holds Pay monthly, Pay yearly and Plus's 3-year term only, so this is its lead for two- and three-year terms below Plus;
  - a paid trial of 3 months at $1;
  - staff account limits: Grow 5, Advanced 15, Plus unenforced;
  - each plan's feature summaries;
  - a POS Pro add-on, 'Try POS Pro free for 3 months' (retailAddonSubscriptionPlan pro_v1, 89 USD every 30 days).

  The pricing pages may hold most of these already. Starter isn't among CM-PLN-001's named plans.
- **The variant editor's rows** (step 002) are capture-plus's own products, its data.
- **The built-in features pages:** their 'Learn more' links (blog posts, the Help Center's 'Considerations for using Shopify Tax', shopify.com/sidekick) name no feature. The two cards' App Store categories are placed: Page builder apps, and Loyalty and reward apps. Store credit's card names 'referring friends' among the reasons apps issue it. That is a lead for CM-LOY-008 (customer referral programme), which holds nothing on Shopify and takes no line from a reason listed in passing (the ruling after SA-41).

## Problems with the brief or the scripts

- **`held_entries.py earlier` finds no twin outside the held pass.** The charges filter's twins are concern-map inventory entries (SH-I-1322 to SH-I-1358), and I found their placements in `merged/evidence.tsv`. The variant editor's route statements (SH-S-5177) I found with `class_slice.py search`.
- **The brief has no rule for a field that a store's own data names** (R22.10), or for a control the source marks `disabled` (entry 109). I read both as the nearest rules have them.

## The coordinator's check

Measured: 26.6 million tokens over 104 requests, about 242,000 an entry. The checker prints no problem.
- **Kept:** R22.1 to R22.10, every `CHANGES` line (Flow `own-service`; the loyalty apps' store credit on CM-LOY-001 `extension-point`, a reading; the variant editor's customs columns on CM-SHP-020 `core`, as five earlier batches placed them), Sidekick `core` as the admin's own assistant, and the first-party products' charge categories `shows`, since a charge line states no feature.
- **The downgrades' scope, aligned:** BASIC, PROFESSIONAL and UNLIMITED are named Basic, Grow and Advanced, as the same answer maps them and as SH-88's check has the plans; DORMANT keeps the source's name.
- **The bins:** SH-64's `new:Bin locations` against SH-36's and this batch's CM-INV-001 goes to `amendment-notes.md` with the other differing lines. The open choices (Tap to Pay's twin `core`, Pricing on CM-CAT-001, General and the location columns, the partner charges by their names) are kept as placed.
- `app-store-built-in-features`, `app-store-registration`, `billing-charge-categories`, `billing-subscription-downgrades` and `bulk-editor-columns` are placed whole.
