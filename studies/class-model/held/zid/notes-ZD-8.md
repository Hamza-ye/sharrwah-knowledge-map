# Notes on ZD-8 (Zid: `store-permissions`, items 58 to 187)

**What the batch holds:** 130 entries, at `high` effort: items 58 to 187 of `store-permissions`' 215, the signed-in user's permissions as the profile answer states them (`other-product-class@0d79b794f:zid/structures/store-permissions/items.jsonl`, lines 58 to 187). The first 57 were ZD-7's; the last 28, with the structure's roles (`meta:roles`), are ZD-9's, which hasn't run.

**Count:** 130 entries, all on a capability: 0 `new`, 0 `out`. That is 168 lines, all `capability` and all `core`.

## How the entries were read

**ZD-7's rules, kept** (its notes and the coordinator's check, now the brief's rule 5):
- each permission is the platform's own staff permission, `core` on the capability of what it gates, as CM-STF-002's note says. None of this batch's permissions is over the staff's permissions, so none is on CM-STF-002. `users.manage` (Add/Remove Users) is on CM-STF-001, as ZD-7's `users.um.view`;
- every `Export` and `Import` permission also takes a line on CM-MIG-001 (entries 4, 6, 64, 74, 97, 98, 120). `exports.requests.*` are CM-MIG-004's, ZD-1's Export requests;
- a permission's `relies_on` names other permissions, not the entry's thing: it takes no line, and is named in `reading`;
- `package_restrictions` is read as the plans the permission is open to, as the coordinator's check of ZD-7 ruled, and its `package_key`s are the `scope` (entries 50, 51, 62, 117);
- where an earlier batch placed the gated page on two capabilities, the permission takes both: Automated Messages (CM-MKT-006 and CM-NTF-001), Abandoned carts (CM-CHK-007 and CM-MKT-022), Orders and products properties (CM-ORD-001 and CM-CAT-001), Store information (CM-ACC-006 and CM-ACC-004), Languages & currencies (CM-MKS-008 and CM-MKS-006), Mokafaa and Qitaf (CM-LOY-004 and CM-PAY-012), Shipping and payment constraints (CM-SHP-001 and CM-PAY-019), the POS invoice templates (CM-POS-001 and CM-ORD-008), the store app's install banner (CM-CHN-006 and CM-SFR-007).

**The pages each permission gates.** `dashboard-page-index/source.js` (the structure's source, `other-product-class@0d79b794f:zid/structures/dashboard-page-index/source.js`) gives each page a `permission` (`one`, `all` or `any` of the code's constants, such as `y.ANALYTICS.viewFinancial` or `_.viewQuantityModificationRecord`). ZD-1's notes say the items leave these out. To keep each permission on the capability of the page ZD-1, ZD-4 or ZD-5 placed, I read the gates there:
- the constants are the code's names, not the slugs. Joining a constant to a slug (`ANALYTICS.viewFinancial` to `analytics.view.financial`, `x.locationsView` to `inventory.locations.view`, `C.view` to `customers.view`) is a reading, made where the words match. The weakest joins are `ie.mobileApp` to `zam.mobile.app` (Store App Orders, entry 83) and `ne.view` to `zidgrowth.view` (entry 78);
- a permission takes a line for each page it alone gates (`one:`), and for a page whose `all:` it is the distinguishing member (`ZIDSHIP.viewShipment` beside the common `ZIDSHIP.view`). A common member (`ZIDSHIP.view`, `ZIDPAY.view`) takes only its own thing's line;
- the lines that come from a gate alone, beyond the permission's own words, are marked "read as this permission": `customer.wallet.view` on CM-LOY-003 (Cashback offers); `coupons.view` on CM-MKT-001 and CM-MKT-018 (Discounts, Bank discounts); `theme.market.store.identity.manage` on CM-CNT-005 and CM-CNT-003 (Menu, Pages), besides CM-SFR-001 (Brand, Themes); `zidship.view.shipment` on CM-SHP-017, CM-SHP-009 and CM-PAY-029 (Shipments tracking, Transactions log); `products.view` on CM-CAT-005 and CM-CAT-002 (Brands, Options library); `customers.view` on CM-LOY-001, CM-CUS-002 and CM-SUP-005 (Customer wallet, groups, Customer Tickets). If the coordinator prefers a permission's line only on what its own name names, these 13 lines are the ones to drop. Only one touches a cell the checker flags: CM-SHP-017's (entry 65), which ZD-1's Shipments tracking already places `core`.

**Other things an entry names** take their own line: the abandoned carts' automatic messages are automatic messages (CM-MKT-006, entries 50, 51, M-6); a POS order's payment method corrected after payment is an order edit (CM-ORD-002, entry 70); the store app's orders are orders (CM-ORD-001, entry 83); the POS's subscription is a subscription to Zid (CM-PLN-001, entry 127).

## Entries I couldn't tell, and what would settle each

- **`ticketing.support.manage`, Manage Ticketing System (entry 1), on CM-ONB-003.** The dashboard's `ticketing` strings are the merchant's tickets to Zid's support: 'Our dedicated support team is just a message away—ready to guide, solve, and support you whenever you need help.' (`dashboard-locales/items.jsonl`, line 1998). ZD-5 placed the Support section's tickets there, and CM-ONB-003's cell holds the plan line Ticketing & Chat System. The customers' tickets page (`customers.support`, ZD-1's Customer Tickets, CM-SUP-005) is gated by `C.view` in `source.js`, not by this permission. What would settle it: the page or route the permission gates in the dashboard's code.
- **`users.logs.view`, View Logs (entry 31), on CM-TRU-003, which held nothing (checker: CHANGES).** It relies on `users.um.view`, so the logs are user management's. I read them as the log of the team's activity, the audit log. No held string names them (searched the locales for activity, logs and history in the settings, team and navbar strings). It could also be a sign-in log of the team's users. What would settle it: the page the permission opens.
- **`zam.install.js.app`, Install JavaScript Apps (entry 40), on CM-APP-001.** What a JavaScript app does in the store isn't stated. If it adds code to the storefront, it is also CM-SFR-004's, which holds nothing on Zid; I didn't place it there on the name alone.
- **`orders.print`, Print (entry 53), on CM-ORD-008.** What it prints isn't stated: the invoice (the cell's Invoice Printing), or the shipping label and packing list (`orders:details.waybillAndPackingList`, ZD-7's notes), which would be CM-ORD-009's.
- **`edit.store.orders.products.price`, Adjust Product Price in the Order (entry 89), on CM-ORD-005.** It relies on `orders.create`, not `orders.edit`, so I read it as pricing a product in an order the merchant creates. It could also be an order edit (CM-ORD-002).
- **`zam.mobile.app`, Store App Orders (entry 83).** The name names the store app's orders; `source.js` gates the Mobile app page by `ie.mobileApp`, which I read as this permission. Placed on CM-CHN-006 and CM-ORD-001.
- **`fostering.charity.view.edit`, Manage Fostering Charity (entry 95), on CM-SEL-007, which held nothing (checker: CHANGES).** This follows ZD-5's line for Charity fostering. The charity-fostering strings show the merchant sponsoring a charity's opportunities and inviting its customers to take part ('Charity campaign information', line 13478). Whether that is buyers' donations, CM-SEL-007's thing, is the coordinator's decision with ZD-5's line.
- **`pos.subscribe`, Manage Subscriptions (entry 127).** The POS strings show packages with cashier licenses (line 311). I placed the subscription on CM-PLN-001, as `subscription.manage`, on which it relies, is. If the coordinator reads ZidPOS's packages as an add-on bought from Zid, it is CM-PLN-004's, as ZD-5's billing add-ons.
- **`view.marketplace.orders.pii`, View marketplace customer data (entry 94), on CM-CHN-003.** The cell's own statements show marketplace orders' customer name, email and phone masked for privacy, which this permission reads. It could also be CM-TRU-005's.

## Source quirks, as the source states them

- **The description of entries 50 and 51** (`abandoned.carts.automatic.messages.manage` and `.view`) is 'Export Abandoned Carts', the name of `abandoned.carts.export` (ZD-7's entry ZD-E-ba77c828). I read it as a copy of that name, not as an export these permissions allow, and gave them no CM-MIG-001 line. What would settle it: Zid's own text for these two permissions.
- **`store.info.manage` relies on itself** (entry 61, `items.jsonl` line 118), as `faqs.manage` does in ZD-7.
- **`zidpay.view` relies on `products.view` and `products.create`** (entry 75, `items.jsonl` line 132), and `customers.view` on `loyalty.view` (entry 119). Stated so; why isn't.

## A structure whose items and sources disagree

None. ZD-7 checked the 215 items against the answer's `user.permissions`, field by field; the 130 here are among them, and their text is the items'.

## What a source states that no entry holds (leads for the second stage)

- `dashboard-page-index/source.js`: each page's permission gate, which the items leave out (ZD-1's notes). The second stage can read them as the pages' own staff permissions. Among them, gates of permissions not in this batch: `te.view` for `logistics.zones`, `any: [PAYMENT_OPTIONS.manage, PAYMENT_OPTIONS.view]` for `payments.bank-accounts`, and `all` of the five analytics views for `analytics.overview`.
- `dashboard-locales/items.jsonl`, `ticketing:*` (lines 1983 to 2029): the merchant's support tickets to Zid, with the attachment limit 'Maximum total size: {{maxSize}} MB per message.' (line 1988), for CM-ONB-003.
- `dashboard-locales/items.jsonl`, `zidpos:subscription.*` (lines 311 to 321): ZidPOS's packages, cashier licenses, and hardware (Cash drawer, Receipt Printer, Barcode Scanner, Tablet), for CM-POS-001 and any POS hardware cell.
- `dashboard-locales/items.jsonl`, `charity-fostering:*` (lines 13475 to 13482) and `pages:charityFostering.title` (line 5709): for CM-SEL-007, beside the charity store's titles the evidence map names.
- `dashboard-locales/items.jsonl`, `whatsapp:messageLogs.*` (lines 1104 to 1167): the log's columns, including the cost and remaining balance per message, for CM-NTF-003 and CM-NTF-004.

## The checker's other lines

- `CHANGES` on CM-LOY-008, CM-MKT-006, CM-NTF-003, CM-SEL-005, CM-SEL-007, CM-SFR-007, CM-SHP-017, CM-SUP-004 and CM-SUP-006: each follows a page an earlier Zid batch already placed on the same capability (ZD-1, ZD-5, ZD-7), whose lines aren't amended into the model yet. CM-TRU-003 is this batch's own reading (above).
- `NOTE` on line 18 (Zid Financing): the staff permission is Zid's own, so `core`, as ZD-1's Financing.
- `NOTE`s on first leads by a common word, not leads (brief, rule 1): CM-B2B-002 for "users" (entries 24, 31), CM-OPS-005 for "logs" (31), CM-OPS-004 for "status" (39, 115), CM-PAY-023 for "balance" (41: the merchant wallet is CM-PLN-006, as CM-PAY-023's own reading says), CM-API-009 for "notifications" (71, 96).

## Problems with the brief or the script

None new. ZD-7's point on permission lists is now the brief's rule 5.

## The coordinator's check (30 October 2026, after the batch)

- **The 12 lines that came from a page's gate alone are dropped.** They rest on joining `dashboard-page-index/source.js`'s permission constants to these slugs. That is another structure's source, read beyond this entry's own, which the brief rules out ("Don't trace a condition, a key or a module through other code or archives"). Each permission keeps the lines its own words name. The dropped lines are `customer.wallet.view` on CM-LOY-003; `coupons.view` on CM-MKT-001 and CM-MKT-018; the store identity's on CM-CNT-005 and CM-CNT-003; `zidship.view.shipment` on CM-SHP-009 and CM-PAY-029; `products.view` on CM-CAT-005 and CM-CAT-002; and `customers.view` on CM-LOY-001, CM-CUS-002 and CM-SUP-005. None changed a cell. The pages' gates are a lead for the second stage, where they are the pages' own staff permissions.
- **`zidship.view.shipment` keeps CM-SHP-002 and CM-SHP-017,** since its own words, View ZidShip Shipments, name ZidShip's shipments and their tracking.
- **The batch changes no cell beyond Zid's earlier batches:** a list of permissions mostly confirms the cells their pages already place.
