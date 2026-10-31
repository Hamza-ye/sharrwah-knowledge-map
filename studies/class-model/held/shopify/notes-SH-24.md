# SH-24: notes

**The batch:** Shopify, 53 entries of `dev-dashboard-scopes`, the Dev Dashboard's scope picker for an app (Create an app > Select scopes, run `20261004T174545Z-journey-dev-dashboard-app`, step 4), in observed-sh at `e38dc17e3`, at effort `high`:
- the resource headings after SH-23's part: 40 under the Admin API, from Marketing Campaigns to Web Pixels; 8 under the Storefront API, from Bulk Operations to Shop Pay Installments Pricing Api; O Auth Access under the Shop API;
- the Shop API's one scope, `shop_app:oauth`, which the concern map doesn't cite;
- the picker's last three entries: 'No scopes found', Cancel and Done.

The API labels under the headings ('Admin API; parent: <heading>') are SH-104's, which `method/held_scope_apis.py` places from these lines once SH-24 is checked. I ran it only with `--help` and with no argument (it printed `SH-24 53 entries for an agent; SH-104 62 API labels for the script`).

**Counts:** 53 entries in 58 lines. By entry, 50 `capability`, no `new`, 3 `out`. By line, 49 `core`, 4 `extension-point`, 2 `own-service`, 3 `out`.

**What I read:** the brief and the coordinator's message; the evidence map; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `dev-dashboard` and `dev-dashboard-scopes`; the selection row and the structure's `meta.json`; SH-23's notes and its 85 lines on the picker; the rulings' last section; B-extent's "Cells and evidence" and "Conventions from the dry run"; the Editions digest's rules 11 and 17, which the message and SH-23's notes name. For the model: the structure's `items.jsonl` and `source.html`; the concern map's 174 citations of this file (`studies/concern-map/platforms/shopify/citations.tsv`), to map each scope name to its picker statement (SH-S-0940 to SH-S-1113), as SH-23 did; the model's evidence rows that name each of my headings' scope names (`merged/evidence.tsv`, read with a script that greps each name in `why`), and the cells' terms (`merged/cells.tsv`); the cells of every capability placed or led to (`held_entries.py cells`). `held_entries.py earlier` found one key: Purchase Options (SH-17, line 41, the admin's own route, `core`).

## The rules I kept

R23.9 to R23.11 and the coordinator's check after SH-23:
- a resource heading is a scope group, on the capability where the model keeps its scopes;
- with the support the model gives the same scopes: `extension-point` for apps' work (an app proxy, the Function APIs, the Editions digest's rule 17), `core` for the platform's own resources;
- a title that names an API takes no CM-API-001 line (E157): Navigation Api, Online Store Pages GraphQL Api, Payment Notification Api, Translations GraphQL Admin Api, Shop Pay Installments Pricing Api.

Each reading is worded for the heading and for its API label, which takes the line: 'the resource X of the picker, with the API it lists under it, the Admin API, through which apps reach its scopes …'. No line takes a scope: the picker is held on one organization's dashboard, and its source states no condition.

## The rules I set (R24.1 to R24.6)

- **R24.1. A heading the picker lists under several APIs is one entry, and each of its items is placed.**
  - **Why:** the structure's entries are its items' distinct texts, and `entries.tsv` locates the first item only. So 'Orders' stands for the Admin API's heading (position 199) and the Customer Account API's (position 329), and 'Metaobjects' for three. Seven of my entries are such: Markets, Metaobjects, Orders, Product Information, Store Content, Store Credit Account Transactions and Store Credit Accounts.
  - **The test:** each item is a scope group placed by R23.9. R23.10's clause for SH-24 then applies to it: an API whose scopes the model keeps on the API's own capability goes there.
  - **One line where every item lands on one capability.** Its reading says it fits every label:
    - Markets on CM-MKS-001: read_markets (SH-S-6042), write_markets (SH-S-6232) and customer_read_markets (SH-S-5919);
    - Metaobjects on CM-CNT-002: read_metaobjects (SH-S-6056); no cell cites customer_read_metaobjects or unauthenticated_read_metaobjects;
    - Store Credit Account Transactions on CM-LOY-001: SH-S-6128, SH-S-6297 and SH-S-5924;
    - Store Credit Accounts on CM-LOY-001: SH-S-6129 and SH-S-5925.
  - **A line per capability otherwise.** Each such line's reading names the API whose item it is for:
    - Orders: CM-ORD-001 for the Admin API's item (the picker's own read_orders, SH-S-1034); CM-CUS-010 for the Customer Account API's (customer_read_orders, SH-S-5921). These are R23.10's own examples.
    - Product Information: CM-CHN-004 for the Admin API's item (read_product_listings, SH-S-6090); CM-SFR-012 for the Storefront API's (unauthenticated_read_product_listings, SH-S-6155).
    - Store Content: CM-CNT-004 for both items (read_content, SH-S-6062; write_content, SH-S-6178; unauthenticated_read_content, SH-S-6148, which the model cites on both cells); CM-SFR-012 for the Storefront API's item alone (SH-S-6148).
- **R24.2. Where the model places a heading's scopes on more than one capability, the heading takes each one whose thing its words name.**
  - **The case:** Shipping Rates takes CM-SHP-001 and CM-SHP-004. The model places the picker's own write_shipping on CM-SHP-001 (SH-S-1067) and its own read_shipping on CM-SHP-004 (SH-S-1066). Both are the store's shipping rates, and both lines fit its one API label.
  - **Where a placement rests on another feature's requirement** (a mutation or a topic of another resource that needs the scope), it isn't the heading's thing, and the reading names it:
    - Reports' write_reports on CM-ANL-001: analytics targets (SH-S-5911). Reports goes on CM-ANL-006, apps' reports through the API (read_reports, SH-S-5905);
    - Metaobjects' write_metaobjects on CM-CAT-004: taxonomy linking (SH-S-6240);
    - Navigation Api's write_online_store_navigation on CM-CNT-009: a URL redirect mutation;
    - the requirement rows of read_orders (CM-SHP-001, CM-SHP-009, CM-RET-003, CM-CHN-003), read_order_edits (CM-RET-003) and read_online_store_pages (CM-CNT-004).
- **R24.3. The support is the model's for the same scopes** (the coordinator's check after SH-23).
  - **`extension-point`:**
    - Payment Customizations: SH-S-1043 and SH-S-6076;
    - Purchase Options: write_purchase_options, SH-S-6286, the scope an app adds to create selling plans. The admin's own route for purchase options stays `core` on the same cell (SH-17);
    - Script Tags: SH-S-6112 and SH-S-6291, as SH-23's App Proxy;
    - Web Pixels: write_pixels, SH-S-5958.
  - **`core`:** where no cell cites the heading's scopes (rule 4). That includes Selling Plans, though its cell's other API rows are `extension-point`: no held statement says apps do the work through unauthenticated_read_selling_plans.
  - **`own-service`:** the Shop API's O Auth Access and its scope, as SH-23 placed the Shop API (R23.11; the ruling after SH-34).
- **R24.4. A heading that no cell cites or holds is placed by its words, a reading.**
  - **By what its words name:**
    - Markets Home on CM-MKS-001;
    - Payment Notification Api on CM-PAY-001;
    - Sensitive Information Of The Shopify Payments Provider Account on CM-PAY-002, beside its sibling's read_shopify_payments_accounts (SH-S-1068);
    - Bulk Operations on CM-API-007;
    - Customer Tags on CM-CUS-001, whose terms hold customer.tags_added;
    - Product Inventory on CM-INV-001;
    - Selling Plans on CM-SEL-001;
    - O Auth Access on CM-CHN-002.
  - **Resource Feedback,** whose words name no capability's thing, goes on the list it groups: access scopes, CM-API-003 (R23.11).
- **R24.5. A heading that names a second thing takes a line for it** (rule 2).
  - **The case:** Shopify Payments Account, Settings, And Banking Details takes CM-PAY-002, its scope's (SH-S-1068), and CM-PAY-005 for its banking details: the bank account the payouts go to, which CM-PAY-005 holds with the picker's own read_shopify_payments_bank_accounts (SH-S-1070).
  - **Homonyms:** CM-PAY-023's Shopify Balance and its section Banking. They are named in the readings of the Banking Details line and of Balance & Payouts. That heading's balance is the payment service's, CM-PAY-005.
- **R24.6. The picker's last entries are `out`:**
  - 'No scopes found': the filter's empty state, hidden until a search matches nothing (`source.html`, line 4495);
  - Cancel: it only closes the dialog (line 4504, `altair--modal#close`);
  - Done: it copies the checked scopes into the app's form and closes the dialog (line 4511, `syncFromCheckboxes`).

## For SH-104: which lines each API label takes

The script gives each label its heading's lines. That is right for every label but six. The line numbers below count the header as line 1.

| Label | Its lines |
| --- | --- |
| 'Admin API; parent: Orders' | line 12 only (CM-ORD-001) |
| 'Customer Account API; parent: Orders' | line 13 only (CM-CUS-010) |
| 'Admin API; parent: Product Information' | line 20 only (CM-CHN-004) |
| 'Storefront API; parent: Product Information' | line 21 only (CM-SFR-012) |
| 'Admin API; parent: Store Content' | line 38 only (CM-CNT-004) |
| 'Storefront API; parent: Store Content' | lines 38 and 39 |

If the script copies every line of a heading to each of its labels, these six need routing by the API that each line's reading names, by the script or by the coordinator's hand.

**SH-23's headings with other APIs' items.** SH-23's entries Companies, Customer, Draft Orders and Checkouts also stand for the picker's headings under the Customer Account and Storefront APIs. Their lines read only the Admin API's item, and SH-104's labels under the other items would take them. The model places those items' scopes so:

| SH-23's heading | Its other item | The model's placement | SH-23's line |
| --- | --- | --- | --- |
| Companies | Customer Account API | customer_read_companies and customer_write_companies on CM-B2B-007, `core` (SH-S-5913, SH-S-5926) | CM-B2B-002 |
| Customer | Customer Account API | customer_read_customers on CM-CUS-010 and CM-API-003, `core` (SH-S-5914); customer_write_customers on no cell | CM-CUS-001 |
| Customer | Storefront API | unauthenticated_write_customers on CM-SFR-012, `core` (SH-S-6164); unauthenticated_read_customers on no cell of its own | CM-CUS-001 |
| Draft Orders | Customer Account API | customer_read_draft_orders on CM-ORD-005, `shows` (SH-S-5918; the model's reason names the buyer's account) | CM-ORD-005 |
| Checkouts | Storefront API | below | CM-CHK-001 |

By R24.1, each would take a line of its own, worded for its item: Companies' on CM-B2B-007, Customer's on CM-CUS-010 and CM-SFR-012. They are SH-23's entries, so I wrote no line on them: the coordinator aligns them.

**The check on `unauthenticated_write_checkouts`.**
- **Whose entry it is:** the Storefront API's Checkouts isn't in my batch. Its text is SH-23's entry SH-E-e91d91a0, Checkouts, placed on CM-CHK-001 `core`, and SH-104's label 'Storefront API; parent: Checkouts' will take that line.
- **What the model holds:**
  - on CM-CHK-002 (Cart), `shows`: the picker's own SH-C-046/boundary/SH-S-1101, whose reason in the model is the access scope held in Q1's cart concern, and SH-S-6152, a headless channel or custom app holding it;
  - on CM-PAY-015, `shows`: unauthenticated_read_checkouts, as a Shop Pay Installments object's requirement (SH-S-6147).
- **My reading:** the `shows` belongs to the cart's cell. Q1 put the checkout scope in its cart concern, and the anchor gave the cart no placement from a scope that names checkouts. It isn't a reading that the scope group supports no placement.
- **So:** the Storefront API's Checkouts group is `core` on CM-CHK-001, Shopify's own API for its own checkout (rule 4), where SH-23's line already places the heading. Only that line's reading, which names the Admin API's write_checkouts and read_checkouts alone, should name the Storefront API's item too. I didn't take `shows` from the model's row.

## New things

None.

## Entries I couldn't tell, and what would settle each

A definition held for the scope would settle each of the first five; the picker states only names.
- **Markets Home** (SH-E-42c29986): CM-MKS-001 by its words. What the home of Markets is, a page or a market, isn't stated.
- **Payment Notification Api** (SH-E-c9550cc1): CM-PAY-001 by its words. CM-PAY-011, `extension-point`, would fit if the notifications are payments apps'. CM-NTF-001 would fit if they are messages to people.
- **Resource Feedback** (SH-E-31dc39dd): CM-API-003 by R24.4's fallback. Whose feedback, on which resources, isn't stated.
- **Sensitive Information Of The Shopify Payments Provider Account** (SH-E-5a2f0f2a): CM-PAY-002. CM-PAY-003, verification and KYC, would fit if the information is the account's identity details.
- **O Auth Access and `shop_app:oauth`** (SH-E-06ffe7e4, SH-E-c01b6130): CM-CHN-002 `own-service`. Other readings fit if the Shop API's page on shopify.dev defines the access so:
  - if it is Shop's sign-in, CM-CUS-010 `own-service` (the Editions digest's rule 11);
  - if it is Shop's sign-in offered for developers' apps, `own-service;extension-point` (R49.2);
  - if it is app authorization, CM-API-002.
- **Theme Templates** (SH-E-13da5a27): CM-SFR-002, where the model places write_themes (SH-S-6201). CM-SFR-001, the plan row Themes and templates, would fit read_themes, which no cell cites.
- **Third Party Fulfillment** (SH-E-857eeee8): CM-SHP-009, as the model keeps the third-party fulfillment-order scopes (SH-S-6139). CM-SHP-011 would fit if its words are read as the fulfillment services' own thing. The model keeps that cell's own scopes apart, as SH-23's Assigned Fulfillment shows.
- **Banking Details** (SH-E-76b70850's second line, R24.5): a reading of the heading's words.
- **Reports** (SH-E-a6d3a182): CM-ANL-006 alone (R24.2). A line on CM-ANL-001 for write_reports would change nothing in that cell.
- **Selling Plans** (SH-E-e20f19c7): `core` (R24.3). It is `extension-point` if the coordinator reads the storefront's selling plans as subscription apps' work.
- **Bulk Operations** (SH-E-3675cbf1): CM-API-007, whose cell holds the Admin API's bulk operations. The Storefront API's could instead be CM-SFR-012's.

## Items against their sources

- **The text:** `items.jsonl` holds every text node of `source.html`, in order, with each scope's and API label's `parent` as the markup nests them. They agree.
- **One entry, several items:** the entries join items of one text, so seven of mine stand for two or three headings (R24.1), which the rendering of an entry doesn't show.
- **The resources' numbers:** the source numbers the resources in its checkbox ids (`select_scopes-40-read_markets`, `select_scopes-41-read_markets_home`), which the items leave out. This states nothing.

## What the source states that no entry holds, for the second stage

- The list's label 'Available scopes' (`source.html`, line 68, the list's `aria-label`), for CM-API-003.

## Problems with the brief or the script

- **The script:** `held_scope_apis.py` gives each label its heading's lines (its `--help`). A heading that stands for items under two or three APIs needs its lines routed by API (above).
- **SH-23's twins:** SH-23's four headings that stand for other APIs' items carry readings of the Admin API's item alone (above).
- **The brief's rule 1:** it doesn't name the concern map's `citations.tsv` or the model's `evidence.tsv` among what an agent reads. The scope names' own statements are only there: `class_slice.py search` found the picker's statement for one of my 101 scope names (SH-S-1014) and returned the inventory entries for the rest. I read both by grep, as SH-23 did.

## The checker's lines, read again

- **No `CHANGES` line:** every line lands on a cell that already holds its support.
- **NOTE, `core` on a product named with the platform's brand** (lines 30 and 33 to 37: the Shopify Payments resources): kept. Shopify Payments is the platform's own payment service, which CM-PAY-002's cell reads `core` ('the only payment gateway designed and operated by Shopify', SH-S-0382) beside its `own-service`. The scope groups are its own API, `core` (rule 4), as the model places the picker's own scopes of them (SH-S-1068, SH-S-1069, SH-S-1070).
- **NOTE, `own-service` on CM-CHN-002** (lines 55 and 56): Shop's maker is held, 'Shop is a Shopify application' (SH-S-0056; the ruling after SH-34), and the cell is already `own-service`.
- **NOTE, a container** (line 55): O Auth Access holds its scope `shop_app:oauth`, which takes its own line (56), on the same capability.

## The coordinator's check

Measured: 15.2 million tokens over 82 requests, about 287,000 an entry. The checker prints no problem and no `CHANGES` line.
- **Kept:** R24.1 to R24.6, the `extension-point` lines by the model's support for the same scopes, the two splits beyond R23.9 and the headings placed by their words, as the marked readings they are.
- **Problem 1, settled:** `method/held_scope_apis.py` now gives an API label only its heading's lines that name its own API's item ('under the <API>', 'over the <API>', or an API a 'lists twice' or 'lists three times' names), so Orders, Product Information and Store Content route as this batch's table has them.
- **Problem 2, settled:** SH-23's shared headings take lines for their other items, by the model's placements of those scopes: Companies under the Customer Account API on CM-B2B-007, Customer under it on CM-CUS-010 and under the Storefront API on CM-SFR-012 (SH-23's lines 141 to 143). Draft Orders' and Checkouts' other items fall on the same capability as their Admin API item, so their one line names both (the checker allows one line per capability); Draft Orders' Customer Account item is `core` by rule 4, where the model's scope is `shows`, and the cell is `core` either way.
- **Problem 3, `unauthenticated_write_checkouts`:** CM-CHK-001 `core` stands, as this batch reads the model's `shows` on CM-CHK-002.
- **SH-104** is placed by the script, 69 lines for its 62 labels.
