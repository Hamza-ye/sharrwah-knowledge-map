# C-bigcommerce: notes

**What this part is.** Domain C's mapping part for BigCommerce, onto the model so far: C-anchor, C-woocommerce and C-zid (with their back-fills). It runs in three batches: batch 1 maps CHK and ORD, batch 2 PAY and TAX, batch 3 SHP and RET and checks the whole part. `scope.tsv` gives BigCommerce 20 concerns of domain C, and 3 concerns of other domains name C under `also` (BC-C-005 B, BC-C-028 A, BC-C-074 E). Q1 never matched BigCommerce, so there are no matches or unclear candidates, and no rulings. Each row is a reading unless it quotes a statement.

## Batch 1: CHK and ORD

**Concerns:** BC-C-014, BC-C-015, BC-C-016, BC-C-017, BC-C-018. **Areas:** CHK (9 capabilities), ORD (15). **What it holds:** no new capability, 5 landings (all into existing capabilities), 24 cells (BigCommerce's, one per capability of CHK and ORD: 12 `statements`, 12 `none-held`), 41 evidence rows, 1 quality, 8 slot fillers, no ruling.

### How I cut, and why

- **BC-C-014 Carts → CM-CHK-002, terms, clean.** Its Carts and Storefront Carts APIs, scope store_cart and webhook topic store/cart/created are the buyer's cart. **Persistent cart** (BC-S-0084) is a plan line, a place of its own by the dry-run convention, and could be a child capability ("the cart saved to the buyer's account across devices"). I kept it in CM-CHK-002, because no other platform's cell shows it so far and it is a property of the cart; `caps --terms "persistent cart; saved cart; سلة محفوظة"` found nothing in any domain. **For the coordinator:** split it if the class should count it.
- **BC-C-015 Abandoned carts → CM-CHK-007, terms, strained.** Salla's and Zid's term. Its recovery statements (BC-S-0087 to BC-S-0090, BC-I-0501) are cited as core in D's CM-MKT-022 by D-bigcommerce, and by "One thing, one domain" stay there; CM-CHK-007 cites only the webhook topic store/cart/abandoned with its definition (BC-S-0091) and the API group's name (BC-I-0033). The API group's description (BC-S-0087) is the recovery token, which is D's.
- **BC-C-016 Checkouts → CM-CHK-001, terms, clean.** Settings > Checkout (BC-S-0094) is cited twice: in CM-CHK-001 for the page, and in its child CM-CHK-003 for its Custom Checkout choice. Single-page checkout (BC-S-0095) is a plan line; I read it as the checkout's own form, not a quick checkout (CM-CHK-008), and kept it in CM-CHK-001.
- **BC-C-017 Checkout extensions (beta) → CM-CHK-004, terms, clean.** Shopify's term Checkout Extensions. Every statement rests on a closed beta (BC-S-0077, which other parts cite under other concerns' keys; I cite it under BC-C-017's). Its partner Route is a slot filler.
- **BC-C-018 Orders → CM-ORD-001, terms, clean.** The parent: its statements are also cited in CM-ORD-002 (editing), CM-ORD-003 (statuses), CM-ORD-005 (merchant-created orders) and CM-ORD-013 (messages), all in the ORD-001 tree. Its app category BC-I-0480 is also cited in B's CM-CAT-001 and F's CM-APP-002, as `extension-point`; it is an inventory entry, not a statement, so I kept the fit clean, as C-zid did for ZD-I-0263.

### Services of BigCommerce's company

No cell of this batch places a service of BigCommerce's company: no `own-service` row. Two hits bear on it, for batch 2:
- **BigCommerce Payments** ("Built with PayPal's infrastructure, which manages PCI compliance and risk controls", BC-S-0140, BC-S-0146, BC-C-025) came up in the fraud search. I left CM-ORD-006 `none-held`, because the statements name risk controls of the payments infrastructure, not orders flagged for the merchant to review. If batch 2 reads them otherwise, tell the coordinator.
- **Digital wallets** (BC-S-0161, BC-C-027) is cited as `core` in CM-CHK-008: a product line on BigCommerce's own page, with no maker statement for a separate service. **For batch 2:** if you cite BC-S-0161 in a PAY capability too (wallets as payment methods), BC-C-027's fit is strained by this cell. BC-S-0164 (a custom checkout based on checkout-js controls the wallets' shipping options) is uncited here; it bears on CM-CHK-003 and SHP.

### Joins on role

All in cells, not landings:
- CM-CHK-008: the product line Digital wallets "with accelerated checkout options" (BC-S-0161) read as Shopify's accelerated checkout buttons (SH-S-0419).
- CM-ORD-002: Orders V2 managing an order's products and shipping addresses (BC-S-0103) read as order editing, against Shopify's route order:edit:shipping-address (SH-S-5221).
- CM-ORD-005: store/order/created fires for orders created "using the control panel" (BC-S-0107), read as orders the merchant creates; no draft or manual order is named.
- CM-ORD-013: an order's messages (BC-S-0103, BC-I-0168) read as notes and comments on an order (SA-S-1744, WC-S-0668). What an order message is isn't defined.

### Homonyms kept apart

- **archive:** BigCommerce's webhook topic store/order/archived (BC-I-0166) is held without a definition. Shopify's archiving (CM-ORD-010's Shopify cell, "Set up order processing and archiving") is closing processed orders. I didn't read BigCommerce's archive as Shopify's, nor as Salla's deleted orders (CM-ORD-012): BC-I-0166 is cited only in CM-ORD-001, and CM-ORD-012 is `none-held`.
- **invoice:** B2B Edition's invoices (BC-S-0192, BC-S-0194, BC-S-0196, BC-C-031) are named with net terms and credit limits, and BigCommerce's Unified Billing invoice (BC-S-0172) is the platform's bill to the merchant. Neither is shown as the invoice the store issues for an order (CM-ORD-008), so CM-ORD-008 is `none-held`. **For batch 2:** BC-C-031 is yours. If its statements show B2B Edition's invoices as invoices for orders, tell the coordinator, who corrects CM-ORD-008's row.

### Strained fits

- BC-C-015 (above): its recovery statements are in D's CM-MKT-022.

### Concerns read under `also`

BC-C-005 (B), BC-C-028 (A) and BC-C-074 (E) bear on none of this batch's cells. BC-S-0169 (BC-C-028, PCI validation) came up in the validation search and is not the capability.

### Statements of other domains

None cited. Hits named in `none-held` readings are named, not cited.

### Gaps

- BC-C-018/decides is "page not read": no Help Center article or control panel page for orders is held, so CM-ORD-001 has no control panel place but the product line Order management, and CM-ORD-002 to CM-ORD-015 rest on the API and webhook topics only. Orders' cancellation, tags, printed documents, invoices and assignment may be on the pages not read.
- BC-S-0104 says Order Operations "configure order settings" without saying what they are (CM-ORD-010 `none-held`).
- No statement names a maker for Route's checkout extension other than Route (BC-S-0101).

### For the later batches

- **Batch 2 (PAY, TAX):** BC-S-0104 (Order Operations: "order transactions … payment actions such as captures, refunds, and voids") is cited in CM-ORD-001 as `core` for orders and order settings. If you cite it for captures or voids in PAY, BC-C-018's fit becomes strained; tell the coordinator. BC-S-0134 (Stored Instruments, "for a faster checkout experience", BC-C-024) is uncited here; it may bear on CM-CHK-008. CM-ORD-015 (order payment status) is `none-held`: Awaiting Payment is an order status (BC-S-0108, CM-ORD-003). The two points above on BigCommerce Payments, Digital wallets and B2B Edition's invoices.
- **Batch 3 (SHP, RET):** BC-S-0103 is held under BC-C-018 (cited here) and BC-C-019 (yours): it names "shipments, and shipping address quotes" too. Cite it under BC-C-019's key for shipments if you need it, and say so. BC-S-0101 (Route's checkout extension extends the shipping step with package protection) is cited in CM-CHK-004. CM-ORD-009 (packing slips) and CM-ORD-004 (cancellation) are `none-held`. The order metafields (BC-S-0104, BC-I-0172 to BC-I-0174) are E's CM-CNT-002's thing, not cited here as metafields.
- **The slot fillers of CM-CHK-008** are the seven payment methods BC-S-0161 names, as Shopify's cell named its four; the statement doesn't say which have the accelerated checkout options.

### What the checker flagged

The checker's last run on batch 1 (`--concerns BC-C-014,BC-C-015,BC-C-016,BC-C-017,BC-C-018 --areas CHK,ORD`): **1 problem, 14 flags.**

- **The problem is the coordinator's, not this batch's:** "the model so far lacks 29 cells, such as CM-ORD-015 for salla: its back-fill must run before this part". C-zid added capabilities (CM-ORD-015 among them), and C-zid is still running in this repository, so C-backfill-zid hasn't run yet. This batch can't write other parts' cells. Batch 1's own rows pass every other check.
- **One problem I fixed:** a term (Order Operations) that wasn't in a cited statement; I took it out of CM-ORD-001's terms.
- **`none-held` cells whose terms match statements (13 flags):** CM-CHK-005, CM-CHK-006, CM-CHK-009, CM-ORD-004, CM-ORD-006, CM-ORD-007, CM-ORD-008, CM-ORD-009, CM-ORD-010, CM-ORD-011, CM-ORD-012, CM-ORD-014 and CM-ORD-015. Each cell's `reading` names the hits and why none is the capability. CM-ORD-012's 47 matches come from the other platforms' terms (deleted, restore): they delete carts, line items, metafields, shipments, customers, categories, subscribers, users or webhooks, or restore themes. None deletes an order. Two hits are cited elsewhere in this part: BC-S-0082 (CM-CHK-002, for CM-CHK-006) and BC-S-0104 (CM-ORD-001, for CM-ORD-004 and CM-ORD-010). Two are cited in domain D, and I left them there: BC-I-0511 (CM-B2B-005, for CM-ORD-014) and BC-I-0010 (CM-CUS-001, for CM-CHK-009).
- **CM-ORD-005: `core` rests only on a boundary statement.** BC-S-0107 is a webhook topic, but its description says orders are created "using the control panel", which is BigCommerce's own admin doing it. A reading; no draft or manual order page is held (Q1's gap BC-C-018/decides, page not read).

### The coordinator, after batch 1

- **CM-CHK-010, Persistent cart, is a capability of its own,** under CM-CHK-002: BigCommerce gives it a plan line (BC-S-0084), and a plan line is a place of its own (the dry run's test). BC-S-0084's evidence row moved there, and CM-CHK-002's BigCommerce cell names it as its child. The back-fill after BigCommerce writes its Shopify, Salla, WooCommerce and Zid cells.
- **The checker's one problem** is the back-fill after Zid (C-backfill-zid), which runs once C-zid's last batch has: Zid's added capabilities need the earlier platforms' cells.
