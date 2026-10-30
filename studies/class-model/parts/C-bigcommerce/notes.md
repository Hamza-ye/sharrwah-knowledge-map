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

## Batch 2: PAY and TAX

**Concerns:** BC-C-020, BC-C-022, BC-C-023, BC-C-024, BC-C-025, BC-C-026, BC-C-027, BC-C-031, BC-C-072, BC-C-073. **Areas:** PAY (32 capabilities), TAX (9). **What it holds:** no new capability, 10 landings (all into existing capabilities: 6 strained, 4 clean), 41 cells (BigCommerce's, one per capability of PAY and TAX: 21 `statements`, 20 `none-held`), 101 evidence rows, 4 qualities, 26 slot fillers, no ruling (BigCommerce has no unclear candidates). Each row is a reading unless it quotes a statement.

### How I cut, and why

- **BC-C-020 Order transactions → CM-PAY-020, terms, clean.** Its Transactions API, scope store_v2_transactions and webhook topics are an order's payment transactions. All its statements are in CM-PAY-020.
- **BC-C-022 Payment processing (Payments API) → CM-PAY-020, definition, strained.** "Charge customers and process refunds" (BC-S-0121), with authorization only and capture later "using the control panel or the Capture API" (BC-S-0125): authorizing and capturing an order's payment. I didn't make it a capability of its own: no other platform shows a payments API apart from its order transactions, and the capability's definition already covers charging and capturing. Strained: BC-S-0130 (a 3D Secure card "charged as a stored payment instrument") is cited in CM-PAY-022; BC-S-0129 (offline payment methods "such as cash on delivery") in CM-PAY-016 and CM-PAY-029; BC-S-0124 (compatible gateways) in CM-PAY-011.
- **BC-C-023 Payment methods → CM-PAY-001, terms, clean.** No control panel page for payment settings is held (searched Settings > Payments, payment settings).
- **BC-C-024 Stored payment instruments → CM-PAY-022, definition, strained.** The grain is split across two trees. The concern's API, scope, webhook topic, vaulting and payments server are a customer's stored instruments, which the Payments API charges server to server (BC-S-0130): CM-PAY-022, like Shopify's customer payment methods and WooCommerce's Payment Token API. Its plan line Stored credit cards (BC-S-0135), with returning customers' details "automatically filled", and the API's stated purpose, "for a faster checkout experience" (BC-S-0134), are CM-PAY-014's (saved buyer checkout details, under CM-CHK-008), as Salla's saved card and address is. I landed it where most of its statements are. **For the coordinator:** if the class should count the plan line in CM-PAY-014 as this concern's landing, move it; either way one side is strained.
- **BC-C-025 BigCommerce Payments → CM-PAY-002, role, clean.** All its statements are in the CM-PAY-001 tree: CM-PAY-002, CM-PAY-004 (PayPal's infrastructure), CM-PAY-005 (Money Dashboard), CM-PAY-007 (card rates), and CM-PAY-011 (the provider list, BC-S-0142).
- **BC-C-026 Embedded and Open Payment Providers → CM-PAY-011, terms, strained.** Strained by domain A: A-bigcommerce cites its Open Payment Provider Fee (BC-S-0154, BC-I-0423) as core in CM-PLN-003, the platform's fee on the merchant's sales. By "One thing, one domain" I left the other fee statements uncited and say so here: **BC-S-0152** (the fee per plan, 2.0% to 0.0%), **BC-S-0153** ($0 on orders through Embedded Payment Providers), **BC-S-0158** (Open Payment Provider Fees "charged by Commerce, not by Customer's payment gateway") and **BC-S-0159** (no BigCommerce fee through Embedded Payment Providers; the provider's own fees still apply). **For the coordinator:** they are A's CM-PLN-003's evidence, and A-bigcommerce doesn't cite them. Its app category Financing (BC-I-0486) is cited in CM-PAY-026.
- **BC-C-027 Digital wallets → CM-PAY-012, terms, strained.** BC-S-0161 is core in CM-CHK-008 (batch 1) and in CM-PAY-012: it names both, the wallets and "accelerated checkout options". It is `shows` in CM-PAY-013 (PayPal) and CM-PAY-015 (PayPal Pay Later, Klarna, Afterpay). BC-S-0164 (wallet interfaces and shipping options) is cited as `shows` in CM-PAY-012; batch 3 may cite it for SHP.
- **BC-C-031 B2B Edition invoices and payments → CM-PAY-008, role, strained.** Net terms read as payment terms. Its company payment methods (BC-S-0193, BC-S-0195) are in CM-PAY-019 (payment method rules), read on role against Salla's customer-payment-white-list: a method enabled or disabled per company restricts what that buyer is offered. I searched D for a B2B payments capability (`caps --terms "B2B; company; companies; net terms; credit limit; invoice"`): D's B2B capabilities hold none.
- **BC-C-072 Tax configuration → CM-TAX-001, terms, clean.**
- **BC-C-073 Tax providers → CM-TAX-004, terms, strained.** Its app category Accounting & Tax (BC-I-0476) names accounting too, and is cited in CM-PAY-028 (its own tree) as well as in F's CM-APP-002. The route Settings > Setup > Tax > *TaxProviderName* (BC-S-0389) is named for the provider: `extension-point`, by the dry run's convention on routes named for an application.

### Services of BigCommerce's company

- **BigCommerce Payments:** no held statement names BigCommerce's company as its maker or provider. "BigCommerce Payments by PayPal" and "Built with PayPal's infrastructure" (BC-S-0140, BC-S-0146) name PayPal. I placed CM-PAY-002 by what its statements show, `core` (native in the admin, BC-S-0149; its availability rule, BC-S-0143), and noted the missing maker statement: Q1's gap BC-C-025/responsible (page not read) names the pages that would say who holds the funds and who the merchant contracts with. No `own-service` for it.
- **B2B Edition:** D-bigcommerce read "BigCommerce's add-on for business-to-business commerce" (BC-S-0354, D's concern BC-C-065) as naming the maker. Following the coordinator's message (a maker statement counts for each feature its service shows), I cite it as `own-service` in CM-PAY-008 and CM-PAY-019, beside the `core` rows for B2B Edition's own APIs. The checker flags both (another domain's statement; maker): the reading is "BigCommerce's".
- **The fraud question from batch 1:** I agree CM-ORD-006 stays `none-held`. BC-S-0140 and BC-S-0146 name PayPal's "risk controls" behind BigCommerce Payments, cited as `outside` in CM-PAY-004, not orders flagged for the merchant.

### Batch 1's open points

- **BC-S-0104** (Order Operations: "perform payment actions such as captures, refunds, and voids", BC-C-018) is cited as `core` in CM-PAY-020. CM-PAY-020's parent is CM-ORD-001, where BC-C-018 landed, so by the checker's tree rule BC-C-018's fit stays clean. But it's a citation in PAY, so **for the coordinator:** if CM-PAY-020 is read as a tree of its own, BC-C-018's landing becomes strained.
- **BC-S-0161** (Digital wallets, cited in CM-CHK-008) is cited in CM-PAY-012, CM-PAY-013 and CM-PAY-015. The concern it belongs to, BC-C-027, lands in CM-PAY-012 and is strained by CM-CHK-008. **For the coordinator:** batch 1's CM-CHK-008 row stands; the earlier landing's fit becomes strained.
- **BC-C-031's invoices:** no statement shows B2B Edition's invoices as invoices for orders. BC-S-0192 says "API for Invoices, Payments, and Receipts in BigCommerce B2B Edition", and BC-S-0194 "invoices, net terms, credit limits", and neither names an order. **CM-ORD-008 stays `none-held`.** No correction is needed.
- **BC-S-0134** is cited in CM-PAY-014 and CM-PAY-022 (`core`, it names both) and CM-PAY-013 (`shows`), not in CM-CHK-008 itself: its saving for a faster checkout is CM-PAY-014's, a child of CM-CHK-008. **BC-S-0164** is cited as `shows` in CM-PAY-012.

### Joins on role

- BC-C-025 → CM-PAY-002: BigCommerce Payments as the platform's own payment service, against Shopify Payments (SH-S-0325) and Salla Payments (SA-S-0049).
- BC-C-031 → CM-PAY-008: net terms as payment terms, against Shopify's Set payment terms (SH-S-7152) and payment_schedules/due (SH-S-6081).
- In cells: CM-PAY-019's company payment methods as payment method rules (SA-S-3164, SA-S-1877); CM-PAY-022's stored instruments charged by the Payments API (BC-S-0130) as payments charged without the buyer at checkout (SH-S-0592).

### Homonyms kept apart

- **BigCommerce Payments Gateway** (BC-S-0123, BC-C-022) is the Payments API's server, "a different server than our other REST APIs". It isn't the product **BigCommerce Payments** (BC-C-025). Cited in CM-PAY-020, not CM-PAY-002.
- **credit limits:** B2B Edition's (BC-S-0194) are a business buyer's limit, not CM-PAY-025's credit to the merchant (Shopify Credit). CM-PAY-025 is `none-held`.
- **tax documents:** BigCommerce submits the store's tax documents "to third-party tax providers" (BC-S-0396, CM-TAX-004). They aren't CM-TAX-009's tax forms the platform issues to the merchant, nor CM-TAX-006's filing.
- **balance:** the Money Dashboard's "Balance and payout reporting" (BC-S-0141, CM-PAY-005) is BigCommerce Payments' balance, not CM-PAY-023's business money account (Shopify Balance).

### Strained fits

BC-C-022, BC-C-024, BC-C-026, BC-C-027, BC-C-031 and BC-C-073, each as above and in its `reading`.

### Concerns read under `also`

BC-C-074 (E): BC-S-0400 ("local payment methods through the provider of your choice") is cited as `shows` in CM-PAY-017. BC-S-0403 (settlement currency through the provider) and BC-S-0406, BC-S-0408 and BC-S-0409 are named in `none-held` readings. BC-C-028 (A): its PCI statements are A's; BC-S-0167, BC-S-0168 and BC-S-0170 are named in none-held readings only. BC-C-005 (B) bears on nothing here.

### Statements of other domains

- **BC-I-0485** (App Marketplace category ERP, F's BC-C-059) is cited as `extension-point` in CM-PAY-028: the cell's ERP side rests on it alone (F-bigcommerce cites it in CM-APP-002 too).
- **BC-C-065/where/BC-S-0354** (D) is cited as the maker in CM-PAY-008 and CM-PAY-019 (above).
- BC-I-0476, BC-I-0486 and BC-I-0490 are placed in this batch's concerns and cited in A's and F's cells too, as `extension-point`. That isn't the core or own-service the merge flags.

### Qualities and slot fillers

- **Qualities:** BigCommerce Payments' card rate per plan (CM-PAY-007), who can use it (CM-PAY-002), the 65 pre-integrated solutions in 150+ countries (CM-PAY-011), and the tax estimate timeout of four seconds (CM-TAX-004).
- **Slot fillers:** PayPal behind BigCommerce Payments (CM-PAY-004). The embedded payment providers that are gateways (CM-PAY-011): Adyen, PayPal Braintree, Stripe, Worldpay and others, most by inventory id, since only BC-S-0142 names three of them. The wallets (CM-PAY-012, CM-PAY-013). PayPal Pay Later, Klarna, Afterpay, Affirm and Clearpay (CM-PAY-015). Sezzle and Zip Money (BC-I-0451, BC-I-0455) are left out: no held statement or other platform's cell names what they do.

### Gaps

- BC-C-025/responsible (page not read): who holds the funds for BigCommerce Payments, under which licence, and who the merchant contracts with. CM-PAY-002, CM-PAY-003 and CM-PAY-004 can't claim more.
- BC-C-026/decides (page not read): what checkout does when a provider fails. BC-C-026/responsible (searched, not found): who holds funds with Embedded or Open providers.
- The Help Center page on offline payment methods that BC-S-0129 points to isn't held: CM-PAY-016, CM-PAY-029 and CM-PAY-030 can show only that cash on delivery is an offline method.
- No control panel page for payment settings, or for the store's own tax rates, is held: CM-PAY-001 and CM-TAX-001 rest on the API and product lines.
- The product lines Tax (BC-I-0530) and Payment freedom (BC-I-0499) are undefined.

### For batch 3 (SHP, RET)

- BC-S-0111 (Transactions API: "capture, void, and refund") and BC-S-0121 (Payments API: "process refunds"), cited in CM-PAY-020, name refunds. If RET cites them, BC-C-020's fit becomes strained, and BC-C-022's is already strained.
- BC-S-0164 (custom checkout controls shipping options in wallet interfaces, BC-C-027) is cited as `shows` in CM-PAY-012. If SHP cites it, BC-C-027 is already strained.
- BC-S-0120 (Order V3 refunds against settled payments, BC-C-021) is named in CM-PAY-031's reading only.
- BC-S-0103's "taxes" (Orders V2) is named in CM-TAX-008's reading; it is cited in CM-ORD-001.

### What the checker flagged

The run on this batch (`--concerns BC-C-020,…,BC-C-073 --areas PAY,TAX`) gives **0 problems and 40 flags.** The coordinator's back-fill problem didn't appear for PAY and TAX. Batch 2's flags:
- **Another domain's statements (3):** BC-I-0485 (F) and BC-S-0354 (D, twice), answered above.
- **Own-service on BC-S-0354 (2):** the maker is read from "BigCommerce's add-on", D-bigcommerce's reading too.
- **`none-held` cells whose terms match statements:** CM-PAY-003, 006, 009, 010, 021, 023, 024, 025, 030, 031, 032, and CM-TAX-002, 003, 008, 009. Each cell's `reading` names the hits and why none is the capability. CM-PAY-030's 51 matches come from the other platforms' term "check" (checkout) and "bank"; none is a bank transfer payment.
- **Statements cited in more than one tree (6):** BC-S-0129, BC-S-0124 (BC-C-022, strained), BC-S-0134 (BC-C-024, strained), BC-S-0161 (BC-C-027, strained), BC-S-0354 (D's, as maker in CM-PAY-008 and CM-PAY-019), BC-I-0476 (BC-C-073, strained). Each is a statement that names several things, or a maker statement.

The rest of the flags are batch 1's, answered in its section: the CHK and ORD `none-held` cells, and CM-ORD-005's core on a boundary statement. Batch 1's rows show no new problem.
