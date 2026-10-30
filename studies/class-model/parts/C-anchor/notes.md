# C-anchor: notes

Domain C, Selling and order management, anchored on Shopify and Salla. The part runs in twelve batches; each batch appends its section below.

## Batch 1: CHK, Cart and checkout

Concerns: SH-C-046, SH-C-047, SH-C-048, SH-C-049, SH-C-050, SH-C-052, SH-C-053, SA-C-042, SA-C-048, SA-C-079, SA-C-100. Nine capabilities, CM-CHK-001 to CM-CHK-009; all eleven concerns land in new capabilities (the part had none before). Every capability was first searched in every domain with `caps` (terms: cart, checkout, سلة, السلة, الدفع, إتمام الطلب, abandoned, المتروكة, UCP, agentic, extension, extensibility, functions, validation, transform, custom field, حقول مخصصة, order options, خيارات الطلب, quick checkout, الشراء السريع, guest, زائر, thank you, post-purchase, add-to-cart, Shop Pay, accelerated, express, buy it now, dynamic checkout, quick, one-click, direct order, الطلب المباشر).

### How I cut, and the grains

- **Cart and checkout (M-021), a difference of grain.** Shopify splits cart (SH-C-046) from checkout (SH-C-047); Salla keeps them in SA-C-100. CM-CHK-001 Checkout is the parent and CM-CHK-002 Cart its child; SA-C-100 lands in the parent, as the coarser concern. The parent follows Salla's grouping: its Checkout APIs collection "is designed for developers building integrations that need to control cart and checkout-entry flows" (SA-S-5139), and its folders Cart and Cart Items sit in that collection. The folders' place in the collection is a reading from context: the sidebar `structures/salla/docs-sidebar/checkout-apis/sidebarTreeList.json` in observed-sa gives both folders the collection's root as parent. I read it and didn't cite it. Shopify's own grouping keeps Cart apart (its Cart label, its carts webhook topics), so the groupings differ, and I followed the one that groups them.
- **Checkout's children.** CM-CHK-003, checkout customization and branding, sits under checkout because Shopify's own route places it there (settings/checkout/editor, SH-S-5103). CM-CHK-004, checkout UI extensions, sits under it by Shopify's own words: extensions "augment Shopify checkout" (SH-S-0679) and "customize your checkout" (SH-S-0069). I kept the checkout UI extensions in C, not F, following D's CM-CUS-014 (customer account UI extensions) and E's CM-POS-004 (POS extensions): the extension surface of one feature stays with that feature.
- **Validation (CM-CHK-005) and cart transform (CM-CHK-006)** are Shopify Function APIs. F's CM-APP-005 holds functions as such, and its note leaves single features' function APIs to their domains, as D's CM-MKT-004 (discount functions) does. Neither has a parent, because Shopify lists them among its Function APIs, not under its cart or checkout.
- **Abandoned checkouts and carts (CM-CHK-007)** is the records only, as the coordinator directed. The recovery is D's CM-MKT-022. That leaves these statements to D, uncited here: Shopify's SH-S-7224, SH-S-7041, SH-S-5277 and SH-S-5276; Salla's SA-S-2099, SA-S-1814, SA-S-1191 and SA-S-5017. Shopify's App Store category Abandoned cart apps (SH-I-1827) is uncited here too, the same way as Salla's App Store category Abandoned Cart, which D cites. D's back-fill may want it for its Shopify cell.
  - Salla's link Abandoned carts (/marketing/carts, SA-S-1814) is about the records as much as the recovery, and D cites it as core. I cited the dashboard app at the same path instead (SA-S-3591), so that no statement supports core in two domains. The coordinator may prefer to move SA-S-1814 here.
  - No parent: Shopify's staff permission puts the records under Orders (Orders > Abandoned checkouts); Salla's link puts them under marketing.
- **Quick checkout (CM-CHK-008).** Salla names two things, the quick-buy button (زر الشراء السريع, the flag quick-purchase, the component salla-quick-buy) and direct ordering (الطلب المباشر, the flag quick-checkout, the route /marketing/quick_checkout). Neither is defined apart from the other, so one capability holds both.
- **Order options and custom fields (CM-CHK-009)** is Salla only. Its links sit in Salla's Orders section, so it has no parent here. If batch 2 (ORD) makes an orders parent that Salla's grouping fits, the coordinator may want this capability under it.
- **Guest checkout** stays inside CM-CHK-001's Salla cell: its settings page checkout/guest-checkout and the flag guest-checkout. It is not a capability of its own, though the settings page would meet the dry run's test. Domain D's CM-CUS-010 (customer accounts) cites WooCommerce's guest-checkout setting inside its Accounts & Privacy tab, so a separate capability here would split one thing across two domains. The reviewer may want guest checkout as its own capability, in C or D.
- **Add-to-cart limit** stays in CM-CHK-002, as a Shopify setting with no section of its own. Its default is recorded as a quality.

### Joins on role (readings)

- CM-CHK-007 (U-001): Shopify's Abandoned checkouts and Salla's Abandoned Carts, each the store's records of purchases the buyer began and didn't complete. Shopify's entitlement on the same route is abandonedCartRecovery (SH-S-5002), and its App Store category is Abandoned cart apps.
- CM-CHK-008: Salla's quick checkout and Shopify's accelerated checkout buttons. Salla's quick purchase "relies on reducing and speeding up the steps of completing the order" (SA-S-5027). Shopify's accelerated checkouts let returning customers "more quickly complete payment" (SH-S-7287), with buttons on Shopify Checkout (SH-S-0419). Shopify's rests on saved payment and shipping details; Salla's statements don't say what quick purchase rests on.

### Homonyms

- **Checkout and cart in "abandoned":** Shopify's "Abandoned checkouts" against Salla's "Abandoned Carts / السلات المتروكة". Shopify's own entitlement for the same route is abandonedCartRecovery (SH-C-050/decides/SH-S-5002). I joined them on role, not on the term (above). Whether Shopify's abandoned checkouts include carts left before checkout isn't stated.
- **"Checkout" in Salla's Checkout APIs** names a developer collection that also holds the cart (SA-S-5139), not the checkout page alone.
- **Salla's "Thank you message"** (SA-C-030) is a message setting, not Shopify's thank-you page extension target (purchase.thank-you.block.render, SH-S-7229). It is not cited.
- **Salla's App Functions** (SA-C-196) run on store events. They are not Shopify's cart transform or validation functions, and are not cited.

### Strained fits

- SH-C-050 and SA-C-048 are strained in CM-CHK-007, because their recovery statements are cited in D's CM-MKT-022 (listed above).
- SH-C-049 is strained in CM-CHK-004. Q1 placed its inventory entry Order limit apps (SH-I-1816) in both SH-C-049 and SH-C-052. I cite it in CM-CHK-005 (validation), which sits outside CM-CHK-001's tree, because the category's name is about limits on orders. The checker flagged this (S1).

### Statements shared with other domains, cited here only as shows

- SH-S-2530 (dev.ucp.shopping.checkout, under SH-C-047) is cited as core in F's CM-AIA-005, under SH-C-140. It is shows in CM-CHK-001.
- SH-S-2533 (dev.ucp.shopping.cart) is shows in CM-CHK-002. Agentic commerce is F's.
- SH-S-6152 (the headless channel's scopes, under SH-C-046) is cited as core in E's CM-SFR-011, under SH-C-139. It is shows in CM-CHK-002.
- SH-S-0628 (a Participating Channel customizes Shopify Checkout, under SH-C-048) is cited as extension-point in F's CM-AIA-005. It is shows in CM-CHK-003.
- SH-S-0683 (Shopify invokes functions) is cited as core in F's CM-APP-005. It is shows in CM-CHK-005 and CM-CHK-006.
- SH-S-0011 and SH-S-0013 (the merchant is the seller) are shows in A's CM-TRU-010 as well as here.
- Salla's ucp-embedded-checkout flag (SA-S-3124) is shows in CM-CHK-001. F's CM-AIA-005 left it uncited, because SA-C-100 doesn't name F under `also`.

### Concerns of other domains, not cited

- SA-C-091 (E): the Twilight SDK's Cart folder and the theme's cart components. This is the storefront's cart, and SA-C-091 doesn't name C under `also`.
- SA-C-092 (D): Cart & Checkout Events, which are D's CM-MKT-009.
- SA-C-198 (F): App Snippets.
- SA-C-002 (A): the minimum order in Salla Plus's order customization (SA-S-2097).
- SH-C-102 (TAX): the VAT number field in the checkout.
- SH-C-028 (E): metafields.
- SH-C-051 (A, which names C under `also`): bot protection at checkout is A's CM-TRU-004. Nothing of it is needed here.

### Left for later batches

- **U-084** (SH-C-052 against SA-C-047): SA-C-047 is batch 2's (ORD), and that batch rules on the pair. Shopify's Order limit apps (SH-I-1816) is cited as shows in CM-CHK-005, undefined. Salla's side is its daily order limit (تعيين الحد اليومي للطلبات, receiving-orders-limit).
- **U-026** (SH-C-074, Shop Pay, against SA-C-079): SH-C-074 is batch 4's (PAY). CM-CHK-008's Shopify cell cites SH-C-078's accelerated checkout statements (SH-S-0419, SH-S-7287). SH-C-078 (Apple Pay; Google Pay) is batch 4's to land, here or in a PAY capability. If it lands in PAY, the coordinator decides whether CM-CHK-008's Shopify cell keeps those keys, and that fit is strained. Batch 4 rules on U-026's SH-C-074–SA-C-079 pair: CM-CHK-008 is where SA-C-079 lands.
- **Slot fillers on CM-CHK-008** (Apple Pay, Google Pay, Amazon Pay, PayPal, from SH-S-0419) are payment providers, and batch 4 may want them in PAY as well.
- **Salla's dashboard app @salla.sa/ui-merchant-payments** (SA-S-3549) is cited under SA-C-100's key for /checkout. Its path also holds the payments pages, which belong to batches 3 to 8.

### Gaps

- No statement held defines Salla's cart options or an order's custom fields (CM-CHK-009), what an embedded checkout is (SA-S-3114, SA-S-3124), or what Salla's abandoned-cart rule is (SA-S-3248).
- No statement held says what Shopify's cart transform does or what its validation checks, beyond their names (CM-CHK-005, CM-CHK-006).
- No statement held says what Shopify's checkout form options are (SH-I-2107, a help-center title).
- Q1 gaps: SH-C-046, SH-C-048 and SH-C-050 responsible (stated only in general terms); the reasons of SH-C-047, SH-C-048, SH-C-050, SH-C-052 and SH-C-053 (searched, not found); SA-C-042, SA-C-048, SA-C-079 and SA-C-100 responsible, and SA-C-042 reason (page not read).
- SH-C-049's own note says some extension targets are limited by plan. No statement held says so.

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas CHK`) gives "0 problems, 5 flags for the reviewer". The flags and my answers:

- **CM-CHK-002 Salla: core rests only on boundary statements.** They are Salla's own API folders, Cart and Cart Items, in its own Checkout APIs collection, and its own access scope carts. The dry run's convention reads a platform's own API for its own feature as core. Salla's dashboard holds no cart page among the statements held.
- **CM-CHK-004 Salla: none-held, 344 matches.** The matches come from the broad terms (extension, checkout, Checkout UI). I read the leads: an unreleased snapchat-extension flag (SA-C-074, D); an FAQ on international shipping fees added at the checkout page (SA-S-0163, SA-C-146, SHP); App Snippets (SA-C-198, F); and the Thank you message (SA-C-030). None of them is an app's block or page in the checkout.
- **CM-CHK-005 Salla: none-held, 13 matches.** They are the merchant's order settings (SA-C-047's daily limit and hours; SA-C-002's minimum), the e-payments transfer minimum (SA-C-111), and verification codes and complaint statuses that match تحقق (SA-C-161, SA-C-178, SA-C-200). None is app-written validation.
- **CM-CHK-006 Salla: none-held, 54 matches.** These come from "bundle" and "function": the bundle flags (SA-C-020, SA-C-070), Twilight's Component Bundle (SA-C-091) and App Functions (SA-C-196). None changes a cart's lines.
- **CM-CHK-009 Shopify: none-held, 2 matches.** These are SH-I-2107, a help-center title with no definition, and SH-S-0670, the VAT number field (SH-C-102, TAX). Both are answered in the cell's reading.

`uncited --domain C` lists these keys of the batch's concerns, all left to D's CM-MKT-022 on purpose: SH-C-050's SH-S-5276, SH-S-5277, SH-S-7224 and SH-S-7041, and SA-C-048's SA-S-1191, SA-S-1814, SA-S-2099 and SA-S-5017.

## Batch 2: ORD, Orders and order management

Concerns: SH-C-054, SH-C-055, SH-C-056, SH-C-059, SH-C-061, SA-C-040, SA-C-041, SA-C-043, SA-C-044, SA-C-046, SA-C-047. Fourteen capabilities, CM-ORD-001 to CM-ORD-014; all eleven concerns land in new capabilities, since no capability of the part's model was the same thing (the area had none). Every capability was first searched in every domain with `caps` (terms: order, orders, الطلبات, الطلب, draft, quote, عرض سعر, fraud, risk, احتيال, الحماية من الاحتيال, print, طباعة, packing slip, invoice, فاتورة, الفواتير, فواتير, assign, إسناد, cancel, إلغاء, status, حالة, حالات, tag, tags, وسوم, edit, تعديل, timeline, comment, تعليق, notes, ملاحظات, deleted, محذوف, restore, استعادة, archive, hours, أوقات, limit, الحد اليومي, acknowledg, إقرار, reorder, تكرار, product network, write-off, customer notes, bulk, تكرار الطلب, manual order, طلب يدوي, packing, summary, ملخص, trash, محذوفة). What the search found and kept apart: domain D's CM-B2B-004 (quotes), CM-NTF-002 (staff notifications, which cites order_notification), CM-LOY-007 (reorder reminders), CM-B2B-005 (a business buyer's saved lists), CM-CUS-006 (non-serious customers), CM-CUS-014 (customer account UI, whose order-status targets are the buyer's page); domain F's CM-APP-008 (admin UI extensions, which holds the print action admin_print) and CM-AUT-001 (Flow); domain G's CM-MIG-001 (export of orders). None of them is the same thing as a capability added here.

### How I cut, and the grains

- **Orders (M-023), a difference of grain.** M-023 holds SH-C-054 and SH-C-056 against SA-C-040, SA-C-041 and SA-C-046. Shopify keeps cancellation in orders and splits editing; Salla splits statuses and cancellation and keeps editing in orders. CM-ORD-001 Orders is the parent, where both coarse concerns (SH-C-054, SA-C-040) land; each finer thing is a child: editing (CM-ORD-002, SH-C-056), statuses (CM-ORD-003, SA-C-041), cancellation (CM-ORD-004, SA-C-046). The parent follows the grouping both platforms share: Shopify's routes Edit order and Create order sit in its section Orders (SH-S-7095, SH-S-7094), and Salla's links and settings sit under /orders, in its Orders list.
- **Salla's finer things inside SA-C-040,** each given a place of its own by a link or a settings page under orders, are children of CM-ORD-001: manual orders (CM-ORD-005, with Shopify's draft orders), Auto tags (CM-ORD-011, /orders/auto-tags), Deleted orders (CM-ORD-012, /orders/trash, with Shopify's order deletion), Customer notes and order comments (CM-ORD-013, orders/customer-notes) and Reorder (CM-ORD-014, orders/reorder). Order editing is CM-ORD-002 by Shopify's split. The reviewer may prefer to fold CM-ORD-013 and CM-ORD-014, which only Salla's settings pages, plan lines and flags show, back into the parent; I kept them because each has a settings page of its own, the dry run's test.
- **Order statuses (CM-ORD-003)** is Salla only: Shopify's statements hold no statuses an order is set to. Its order-status extension targets are a homonym (below).
- **Draft orders and manual orders (CM-ORD-005),** joined on role: each is the merchant's creating an order in the admin (U-018).
- **Order risk and fraud analysis (CM-ORD-006)** has no parent: Shopify's help puts fraud analysis under managing orders (SH-S-0747), Salla's plan line sits in its payment group (aldfaa, SA-S-1971). Salla's side is SA-C-122, the PAY batch's (below).
- **Order assignment to staff (CM-ORD-007)** is Salla only. It is not Shopify's order routing (SH-C-060, SHP), which assigns orders to fulfillment locations.
- **Invoices (CM-ORD-008) and packing slips (CM-ORD-009) are two capabilities.** Q1's U-019 asks whether Shopify's printing (SH-C-061) is Salla's order invoice (SA-C-044). Salla's invoice is a document with serial numbers, issued to the buyer and passed to accounting services (SA-S-5015); Shopify's packing slip is a fulfilment document in its section Shipping (SH-S-7100). So I cut by document, not by printing. SH-C-061's App Store category Invoice and receipt apps (SH-I-1854) is cited in CM-ORD-008, so U-019 is joined there, on role. SH-C-061 itself lands in CM-ORD-009.
  - CM-ORD-009 has no parent: Shopify places its packing slip and document template routes in its section Shipping, while Salla's print order summary (طباعة ملخص الطلب) sits in its plan group إدارة الطلبات. The SHP batch may want CM-ORD-009 under a fulfilment capability, and to cite Salla's order-print-multi-policy (SA-S-3099, SA-C-144, printing shipping policies) there.
  - CM-ORD-008 is under CM-ORD-001 by Salla's grouping (/orders/invoice-settings). ZATCA e-invoicing, split from SA-C-044 by Q1, and Shopify's VAT invoices for the EU and UK (SH-I-2331) are the TAX batch's.
- **Order receiving settings (CM-ORD-010)** holds the whole of SA-C-047: Accept orders, Ordering hours, the daily order limit, Order acknowledgment, auto-complete and the Order confirmation page. Q1 holds them in one concern, and no statement defines one apart from the others. The acknowledgment before purchase (SA-S-5016) and the confirmation page touch checkout; they stay here because Salla's settings keys put them under orders/processing. The reviewer may want the daily limit and hours apart.
- **Order cancellation (CM-ORD-004)** and **deletion (CM-ORD-012)** cite Shopify's staff permissions and webhook topics, placed inventory entries under SH-C-054, where no statement covers them.

### Joins on role (readings)

- CM-ORD-005 (U-018): Shopify's draft orders, whose new route is titled Create order (SH-S-7094, gated by CREATE_AND_EDIT_DRAFT_ORDERS, SH-S-5214), and Salla's manual order, إنشاء طلب يدوي (SA-S-1989) with the staff permission order_create (SA-S-2273). Whether Salla's manual order has a draft stage isn't stated.
- CM-ORD-008 (U-019): Salla's order invoice (SA-S-1778, SA-S-1987, SA-S-5015) and Shopify's App Store category Invoice and receipt apps (SH-I-1854), which "offer additional document types and advanced customization features" (SH-S-7225). No Shopify statement held defines an invoice issued for an order, so the Shopify side rests on the category's name and that sentence.

### Homonyms

- **"Order status":** Shopify's customer-account.order-status.* extension targets are the buyer's order status page (domain D's CM-CUS-014), not Salla's order statuses (حالات الطلب, /orders/statuses, SA-S-1775). Not cited here.
- **"Invoice":** Shopify's draft orders "send invoices" (SH-S-7225), a draft order's invoice to the buyer, and its notification templates Order invoice and Draft order invoice (SH-I-2016, SH-I-2001, domain D), against Salla's order invoice issued by the store (SA-C-044). Only the App Store category is joined (above).
- **"Order limit":** Shopify's Order limit apps (SH-I-1816), undefined, against Salla's daily order limit (SA-S-1992). Kept apart (U-084).
- **"Assign":** Shopify's order routing assigns orders to fulfillment locations (SH-S-0751), not to staff.
- **"Policy" in Salla's order-print-multi-policy** (SA-S-3099) is a shipping policy, not a store policy. Not cited.

### Strained fits

- SA-C-040 is strained in CM-ORD-001: its plan line طباعة ملخص الطلب and flag order-summary (SA-S-1988, SA-S-3283) are cited in CM-ORD-009, which has no parent.
- SH-C-061 is strained in CM-ORD-009: its inventory entries are cited in domain F's CM-APP-008 (admin_print, SH-I-1432) and in CM-ORD-008 (SH-I-1854), another tree.

### Rulings

- U-018, SH-C-055 against SA-C-040: joined:CM-ORD-005.
- U-019, SH-C-061 against SA-C-044: joined:CM-ORD-008.
- U-084, SH-C-052 against SA-C-047 (left to this batch by batch 1): apart. SH-I-1816 is cited in CM-CHK-005; Salla's limit is cited in CM-ORD-010.

### Left for later batches

- **U-018, SH-C-055 against SA-C-126** (payment links, إرسال رابط الدفع للعميل): SA-C-126 is the PAY batch's. Shopify's draft orders "capture payments" (SH-S-7225, cited in CM-ORD-005). The PAY batch rules on the pair.
- **U-021, SH-C-059 against SA-C-122** (fraud protection): SA-C-122 is the PAY batch's to land. CM-ORD-006's Salla cell cites two of its statements, the plan line نظام الحماية من الاحتيال (SA-S-1971, core) and the message to a merchant carrying out a suspicious order (SA-S-5051, shows). If PAY lands SA-C-122 in CM-ORD-006, U-021's pair is joined:CM-ORD-006; if it makes a payments capability for fraud protection, SA-S-1971 would support core in two capabilities, and the coordinator should choose one. The flag sift (SA-S-3054) and the shopping experience fee's mention of fraud protection (SA-S-0104) are left uncited for PAY. Shopify Payments' blocking of high-risk checkout attempts (SH-S-0750) is cited here only as shows.
- **Uncited SA-C-040 keys,** left on purpose: partial-payments (SA-S-3286), for PAY; the plan line تتبع الطلب عبر محفظة أبل (SA-S-1995), order tracking, for SHP; order_notification (SA-S-2275, SA-S-2492), domain D's CM-NTF-002; the price-quote keys (SA-S-2288, SA-S-2505, SA-S-3361), domain D's CM-B2B-004. SA-S-2682 (request_quote) is cited as shows in CM-ORD-003.
- **Uncited SH-C-054 keys:** the customer account and marketplace order scopes (SH-S-5917 to SH-S-5923, SH-S-6030 to SH-S-6036, SH-S-6227 to SH-S-6253), which are the customer account's (D) and marketplace orders' (E's CM-CHN-003) or general requirements; SH-I-0881 Orders > Export (G's CM-MIG-001).
- **For the coordinator, on batch 1's rows:** batch 1 asked whether CM-CHK-009 (order options and custom fields) belongs under an orders parent. Salla's links Cart options (/orders/options, SA-S-1782) and Custom fields (/orders/custom-fields, SA-S-1780) sit in the same admin list as All orders (list 1, SA-S-1772), so Salla's grouping puts CM-CHK-009 under CM-ORD-001; Shopify's cell is none-held. Not changed here.

### Concerns of other domains, not cited

- SH-C-060 (order routing, SHP) and SH-C-119 (fulfillment orders, SHP): their assignment and cancellation-request topics are not cited.
- SH-C-030 (E): the comments route, a blog's comments.
- SA-C-144 (SHP): order-print-multi-policy.
- SA-C-122 and SA-C-126 (PAY, domain C): above.

### Gaps

- No statement held defines Shopify's product-network-orders route, its orders/pay_by_creditcard_on_mobile route, or its order write-offs (beta).
- No statement held says what Salla's order-estimate, order-advance-management or batch-order-items-save do, what a warehouse invoice is, what the order summary holds, what the auto tags tag by, who writes a customer note or who repeats an order.
- No statement held says how Shopify cancels an order or what its Set up order processing and archiving covers (SH-I-2111, a help-center title).
- No Shopify statement held defines Invoice and receipt apps or Order limit apps.
- Q1 gaps: SH-C-054, SH-C-055, SH-C-056, SH-C-059 and SH-C-061 reason (searched, not found); SH-C-055, SH-C-056 and SH-C-061 responsible (stated only in general terms); SA-C-040, SA-C-041, SA-C-043, SA-C-044, SA-C-046 and SA-C-047 responsible (page not read); SA-C-040, SA-C-041, SA-C-043 and SA-C-046 reason (page not read); SA-C-047 boundary (page not read), so no API resource or event for Salla's receiving settings is held.

### Qualities

- CM-ORD-001 Shopify: an app's default access to orders, "the last 60 days" (SH-S-5932).
- CM-ORD-001 Salla: عدد لا محدود من الطلبات on سلة بلس (SA-S-1950).

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas ORD`) gives "0 problems, 9 flags for the reviewer". The five on CHK rows are batch 1's, answered in its section. Mine:

- **CM-ORD-007 Shopify: none-held, 1 match (SH-I-0931).** It is Customers > Companies > Assign staff to company locations, B2B (domain D), not orders assigned to staff.
- **CM-ORD-011 Shopify: none-held, 99 matches.** Nearly all come from the word "tag" in the JSON of Shopify's plan table rows ("tag": "th"); the rest are script tags, product tags and customer tags (domains E, B and D). None is a tag on an order.
- **CM-ORD-013 Shopify: none-held, 6 matches.** The comments route of the online store (SH-C-030, E), the terms' summary that asks for public-facing contact information and policies (SH-S-0014, "notes" not about orders), and help-center titles on tax filing timelines and credit notes. None is a note on an order.
- **CM-ORD-014 Shopify: none-held, 4 matches.** Payment customization that reorders payment methods (SH-S-0589), the extension target admin.product-details.reorder.render (SH-I-1509) and Pre-order apps (SH-I-1842). None repeats an order.

## The coordinator's corrections after batch 2 (30 October)

- **CM-CHK-009's parent is CM-ORD-001,** by Salla's own grouping (convention 6): its links sit under /orders/ in the same admin list as All orders.
- **For the PAY batches:** U-021 (SH-C-059 against SA-C-122, fraud protection): CM-ORD-006's Salla cell cites SA-C-122's SA-S-1971 as `core`. Where SA-C-122 is the same thing, it lands in CM-ORD-006; a payment capability of its own for fraud would count SA-S-1971 twice. SA-C-122 also holds SA-S-5052, the tag for a customer who isn't serious, from Salla's anti-fraud analysis across its stores, a lead for A's CM-TRU-008. U-018 (SH-C-055 against SA-C-126, payment links) is PAY's to rule. Partial payments (SA-S-3286, of SA-C-040) are left to PAY, and Apple Wallet order tracking (SA-S-1995) to SHP.


## Batch 3: PAY, Payments, payouts and money (first of six)

Concerns: SH-C-045, SH-C-062, SH-C-063, SH-C-064, SH-C-065, SH-C-066, SH-C-067, SH-C-068, SH-C-069, SH-C-070, SH-C-071. Eight capabilities, CM-PAY-001 to CM-PAY-008; all eleven concerns land in new ones, since the area had none and no capability of the part's model was the same thing. Every capability was first searched in every domain with `caps` (terms: payment, payments, payout, المدفوعات, الدفع, verification, KYC, توثيق, fee, رسوم, rates, reserve, processor, payment terms, net terms, bank account, حساب بنكي, settlement, تحويل; then acquirer, facilitator, underwriting, المستحقات, رصيد المدفوعات, payment provider, gateway, بوابة, بوابات الدفع, طرق الدفع, وسائل الدفع, Shopify Payments, مدفوعات سلة, processing, معالجة, حاسبة الرسوم, payment schedule, شروط الدفع, آجل, deferred, due). What the search found and kept apart: A's CM-TRU-002 (identity verification of the people behind a store), CM-TRU-018 (PCI), CM-PLN-003 (the platform's fee on sales through other providers), CM-PLN-004 to -007 (the platform's billing of the merchant, and Salla's prepaid store balance, CM-PLN-006), CM-ACC-004 (business entity); D's CM-LOY-001 and -002 (store credit, gift cards), CM-B2B-001 to -007; E's CM-POS-002, CM-MKS-003 (merchant of record, Global-e) and CM-MKS-007 (currency conversion); F's CM-APP-003 (app charges) and CM-PTN-003 (partner payouts). None is the same thing as a capability added here. Every Shopify and Salla cell is written for the eight.

### How I cut, and the grains

- **The tree.** CM-PAY-001, payment methods and providers (the store's payment settings), is the root. CM-PAY-002, the platform's own payment service, is its child; the service's own parts are CM-PAY-002's children: onboarding and verification (003), the processing, acquiring and fund holding behind it (004), payouts (005, with reserves and holds, 006, under it) and its processing fees (007). Payment terms (008) sits under CM-ORD-001.
- **M-025, a difference of grain.** It joins Shopify's settings page (SH-C-062) and payments apps (SH-C-076) with Salla's external gateways (SA-C-120), and its granularity note puts Salla's Payments settings page in SA-C-110. So CM-PAY-001 is the settings page, where SH-C-062 lands, and its Salla cell cites SA-C-110's settings keys (the links Payments and Payment methods, the staff permissions, the API folder and the scope payments). **For batch 4 and the Salla batches:** SH-C-076 and SA-C-120 are finer, each a kind of provider the merchant connects; I leave it to them to add a child of CM-PAY-001 for third-party providers and gateways, and the children for wallets, instalments, PayPal, manual methods and the rest, rather than add capabilities none of my concerns is.
- **CM-PAY-002 under CM-PAY-001,** by both platforms' grouping: Shopify's route payments:settings:shopify-payments sits in its payment settings (SH-S-5248); Salla's e-payments are activated from its Payment methods tab (SA-S-0051). The methods Salla Payments carries (Apple Pay, STC Pay, Google Pay, KNET, in SA-C-110's plan lines and flags) are left to the batch that lands wallets (SH-C-078, U-023 and U-024). I cite only mada, the card line and KNET as the service's own, as core in CM-PAY-002; the wallet batch may want them in a child.
- **CM-PAY-004, one capability for four Shopify concerns.** SH-C-064 (processing and settlement), SH-C-065 (custody of funds), SH-C-066 (payment facilitation in the EU/EEA and UK) and SH-C-067 (regulated payment services in Canada) are all clauses of the Shopify Payments Terms and its Payment Processor List, with no admin place apart from those pages. Q1's U-027 asks one question of three of them against Salla's SA-C-114 and SA-C-177: who processes, holds the funds and under what licence. So one capability holds them, each statement keeping its country scope. The reviewer may want custody (SH-C-065) apart; I kept it here because the same terms give custody to the Payment Processors and Financial Services Providers that process (SH-S-0093, SH-S-0118). Whether this is a capability at all, rather than the terms of CM-PAY-002, is a question for the reviewer: Shopify's Payment Processor List is a page of its own (www.shopify.com/legal/processor-list), which I read as the dry run's place of its own.
- **CM-PAY-003, onboarding and verification (M-003).** Under CM-PAY-002: Shopify's checks are for "the Payment Services" (SH-S-0132), and Salla's link Store Verification is /payments/kyc (SA-S-1881). Domain A's note on CM-TRU-002 asks that Salla's store verification count once, in domain C, and that this capability not cite SH-C-008's route keys: it doesn't. Shopify's route profile-assessment and section ProfileAssessment also sit under SH-C-068's keys; they are shows here, core in A.
- **CM-PAY-005, payouts (M-027).** The payout bank account stays inside it: Shopify keeps it in SH-C-069 (read_shopify_payments_bank_accounts, the bank account requirements). Salla splits it (SA-C-112), and I cite SA-C-112's SA-S-0094 as core here. **For the Salla batches:** SA-C-111 lands here; SA-C-112 is finer, a part of payouts, and lands here too unless they make a child for the payout account.
- **CM-PAY-006, reserves and holds,** under CM-PAY-005 because Q1 places SH-C-070's where on Shopify's Payouts route (SH-S-6325). That route is core in CM-PAY-005 and shows in CM-PAY-006.
- **CM-PAY-007, fees (M-029),** not A's CM-PLN-003: Shopify's third-party transaction fees and Salla's platform commission are the platform's fee on sales, while these are the payment service's rates on the transactions it processes. Shopify's 1.25% premium where a third-party provider is used alongside (SH-S-0378) is shows here; A may want it in CM-PLN-003.
- **CM-PAY-008, payment terms (SH-C-045), weighed against D's CM-B2B-001.** Shopify's API reference lists payment terms among its B2B resources (SH-I-0004, cited as shows), but its staff permissions put them in the categories ORDERS and DRAFT_ORDERS (SH-S-7152, SH-S-7153), and no statement held limits them to business buyers. So they stay in C, under CM-ORD-001 by the admin grouping. If the coordinator reads the API's grouping as the platform's own, the capability would go to D under CM-B2B-001, and SH-C-045 would land there as `moved:D`.

### Joins

No join on role. The landings use `single`, each naming its Q1 match in the reading: the checker wants a match's other concerns landed before a landing claims it, and M-025, M-026, M-003, M-027 and M-029 hold Salla concerns the Salla batches land later (M-028 and M-037 hold only WooCommerce's). **For the Salla batches:** SA-C-110 lands in CM-PAY-002 by M-026, SA-C-006 in CM-PAY-003 by M-003, SA-C-111 and SA-C-112 in CM-PAY-005 by M-027, SA-C-113 in CM-PAY-007 by M-029, and SA-C-120 under CM-PAY-001 by M-025. The coordinator may then change my landings' joins to the match.

### Homonyms

- **"Payment terms":** Shopify's payment terms on an order (SH-C-045) against Salla's تعيين شروط الدفع عند الاستلام, cash on delivery's conditions (SA-S-2027, SA-C-115 and SA-C-116), its وسائل الدفع الآجلة, buy now pay later (SA-S-0070, SA-C-118), and the merchant's postpaid shipping labels, الدفع الآجل لبوليصات سلة (SA-S-5061, SA-C-140). None is cited in CM-PAY-008.
- **"Wallet":** Salla's link Wallet (/payments/wallet, SA-S-1876) is held in SA-C-005 (A's CM-PLN-006, the store balance, core) and in SA-C-111 (the e-payments balance). Salla says the two balances differ (SA-S-0079, SA-S-0083). Here it is shows. Neither is D's customer wallet (CM-LOY-001).
- **"Payouts":** the payment service's payouts to the merchant (CM-PAY-005), not F's partner payouts (CM-PTN-003).
- **"Settlements":** Salla's scope settlements (SA-S-1564) and its Settlements API (SA-C-124) are settlements withheld by dropshipping apps, not Shopify's "settlement" of transactions by its Payment Processors (SH-S-0082). Not cited.

### Strained fits

- SH-C-068 is strained in CM-PAY-003: its where statements, the route profile-assessment (SH-S-5254) and the section ProfileAssessment (SH-S-1594), are cited as core in domain A's CM-TRU-002 under SH-C-008's keys. Here they are shows.

### Statements shared with other domains, cited here only as shows or outside

- SH-S-5092 (route shopify-payments-accounts) is core in A's CM-PLN-001 and E's CM-MKS-003; SH-S-5080 (payments:settings:setup) is core in A's CM-ONB-002. Both are shows in CM-PAY-002.
- SH-S-0009 (Shopify Payment Activities Inc., Canada) is shows in A's CM-ACC-002; it is own-service in CM-PAY-004. The merge flags core or own-service in two domains only, so this is not a double count.
- SH-S-0123 (funds or data held under legal process) is outside in A's CM-TRU-017 and outside in CM-PAY-004.
- SH-S-0565 (Global-e holds funds for Managed Markets orders) is outside in E's CM-MKS-003 and outside in CM-PAY-004, with SH-S-0566.
- SH-S-0558 (fee values in the Terms) is shows in E's CM-MKS-007 and shows in CM-PAY-007.
- SA-S-1876 (Wallet link) is core in A's CM-PLN-006 and shows in CM-PAY-005. SA-S-1583 (order.payment.updated) is core in CM-ORD-001 and shows in CM-PAY-002.
- SA-S-3549 (dashboard app ui-merchant-payments) is core in CM-CHK-001 under SA-C-100's key and core in CM-PAY-001 under SA-C-110's: the app's path holds both /payments and /checkout. Both are in this domain; the coordinator may prefer one.
- SA-S-0132 (Absher SMS) is shows here and in A's CM-TRU-002. SA-C-006's entity steps (SA-S-0133, SA-S-0142), core in A's CM-ACC-004, and SA-S-0141, core in A's CM-ONB-001, are not cited here.

### Rulings

- U-071, SH-C-064 against SA-C-235 (domain G, which names C under also): apart. Salla's statement is about affiliate commissions after payment-gateway updates (SA-S-0044), landed in G's CM-OPS-001.

### Left for later batches

- **U-027** (SH-C-065, SH-C-066, SH-C-067 against SA-C-114 and SA-C-177): the batch that lands SA-C-114 and SA-C-177 rules on its six pairs. CM-PAY-004's Salla cell cites SA-C-114's SA-S-0081 and SA-S-0088 and the agreement SA-I-2612 (SA-C-177's) as shows, so if they land in CM-PAY-004 the pairs are joined:CM-PAY-004.
- **U-028** (SH-C-069 against SA-C-164, the settlement currency): SA-C-164's batch rules. Shopify's payout currencies are help-center titles in SH-C-069 (SH-I-2238, SH-I-2240, SH-I-2243), uncited; Multi-Currency Payouts' plan limit (SH-S-0365) is shows in CM-PAY-005.
- **M-026, M-003, M-027, M-029** (above, Joins): the Salla side lands later.
- **SH-C-063's SH-S-0022** (a PayPal Express Checkout account created on sign-up) is left uncited for the batch that lands PayPal (SH-C-077, M-032).
- **Salla's SA-S-0104** (the shopping experience fee, which names saved cards, Apple Pay quick purchase and fraud protection) is cited here as shows in CM-PAY-007. Batch 2 left it for PAY in connection with fraud protection; it supports no placement there.
- **From batch 2, still open:** U-018 (SH-C-055 against SA-C-126, payment links), U-021 (SH-C-059 against SA-C-122, fraud protection) and partial payments (SA-S-3286): their Salla concerns land in batches 7 and 8, which rule on them.

### Gaps

- No Salla statement held names who processes or acquires Salla Payments' transactions, who holds the funds or under which licence, nor the parties to the payment services contract (Q1's gaps on SA-C-114 and SA-C-177, all "page not read"). CM-PAY-004's Salla cell is therefore not-stated.
- No Salla statement held names a Salla company as the provider of Salla Payments, so CM-PAY-002's Salla cell claims core only, from its own plan lines, links and definition. The maker statement is a gap.
- No Shopify statement held defines what payment terms it offers (SH-C-045), and Q1's gaps on it are responsible (stated only in general terms) and reason (searched, not found).
- Salla's Kuwait help pages differ on the transfer minimum: one dinar (SA-S-0086) and no minimum (SA-S-0087). Both are cited; the qualities hold the first.
- Q1 gaps: SH-C-065, SH-C-066, SH-C-067 and SH-C-071 reason (searched, not found); SH-C-066 and SH-C-067 where (searched, not found) and SH-C-067 boundary (searched, not found), so no admin place is held for the payment facilitator or the Canadian regulated services.

### Qualities

- CM-PAY-002 Shopify: minimum age 18 for a Shopify Payments account (SH-S-0326).
- CM-PAY-005 Shopify: a minimum payout amount in certain countries (SH-S-0339), a 3-5 business day pause on a new payout bank account (SH-S-0345). Salla: a 100 SAR minimum for a transfer (SA-S-0077), the UAE's Thursday transfers above 250 AED (SA-S-0080), Kuwait's next business day with a one-dinar minimum (SA-S-0086), and the deposit frequency by plan (Plus weekly, Pro every 48 hours, Special daily: SA-S-0071 to SA-S-0073).
- CM-PAY-007 Shopify: online standard card rates per plan (SH-S-7021), online international rates (SH-S-7023), the 1.25% premium (SH-S-0378).

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas PAY`) gives "0 problems, 24 flags for the reviewer". The nine on CHK and ORD rows are batches 1 and 2's, answered in their sections. Mine:

- **Own-service on Shopify's entity statements (13 flags: SH-S-0146 to SH-S-0149, SH-S-0080 twice, SH-S-0081 twice, SH-S-0129, SH-S-0139, SH-S-0140, SH-S-0125, SH-S-0009).** Each names a company of Shopify's group by its legal name (Shopify Inc., Shopify Payments (USA) Inc., Shopify International Limited, Shopify Commerce Singapore Pte. Ltd., Shopify Payments EU Limited, Shopify Payments UK Limited, Shopify Payment Activities Inc.) or "a Shopify affiliate" or "Shopify", as the supplier of the Payments Services, the Payment Facilitator or the registered Payment Service Provider. That is the maker-or-provider statement own-service asks for. The service itself is also core, by its admin section and routes.
- **CM-PAY-006 Salla: none-held, 8 matches.** A frozen annual subscription (SA-S-2085), the scope settlements (SA-S-1564), partner policies' suspensions and a partner's frozen dues (SA-C-205, SA-C-206, SA-C-208), a theme publication step: none is a hold on the merchant's payouts. Answered in the cell's reading.
- **CM-PAY-008 Salla: none-held, 2 matches.** Buy now pay later (SA-S-0070) and postpaid shipping labels (SA-S-5061), homonyms above.

`uncited --domain C` lists for this batch's concerns only SH-C-063's SH-S-0022, left for PayPal on purpose.

## Batch 4: PAY, Payments, payouts and money (second of six)

Concerns: SH-C-072, SH-C-073, SH-C-074, SH-C-075, SH-C-076, SH-C-077, SH-C-078, SH-C-079, SH-C-080, SH-C-081, SH-C-083. Eleven capabilities, CM-PAY-009 to CM-PAY-019; all eleven concerns land in new ones, since none is the same thing as CM-PAY-001 to -008 or any capability of the part. Every capability was first searched in every domain with `caps` (terms: chargeback, dispute, نزاع, النزاعات, اعتراض, fraud, احتيال, Shopify Protect, protect, حماية; then wallet, محفظة, المحافظ, Apple Pay, PayPal, instalment, installment, تقسيط, التقسيط, pay later, الدفع الآجل, Tabby, تابي, manual payment, cash on delivery, الدفع عند الاستلام, bank transfer, التحويل البنكي, crypto, stablecoin, عملات رقمية, local payment, payment customization, قيود الدفع, payment restriction, gateway, بوابة الدفع, payments app, saved card, حفظ البطاقة, Shop Pay, mark as paid, record payment). What the search found and kept apart: C's CM-ORD-006 (fraud analysis for the merchant's review), CM-CHK-008 (quick checkout, made CM-PAY-014's parent); D's CM-LOY-001 to -003 (the buyer's store wallet, gift cards, cashback), CM-MKT-020 (ads wallet), CM-SUP-008; A's CM-PLN-004 and -006 (platform billing, the prepaid store balance), CM-TRU-004, CM-TRU-020 (buyers' complaints about stores); F's CM-API-004 (protected customer data). None is the same thing. Every Shopify and Salla cell is written for the eleven.

### How I cut, and the grains

- **The tree.** Under CM-PAY-001 (payment settings): third-party providers and gateways (011), digital wallets (012, with PayPal, 013, under it), instalments and buy now pay later (015), manual methods (016), cryptocurrency (018) and payment method rules (019). Under CM-PAY-002 (the platform's own service): chargebacks and disputes (009), chargeback protection (010) and local payment methods (017). Under CM-CHK-008 (quick checkout): saved buyer checkout details, Shop Pay (014). Each parent rests on the platforms' own grouping, given in the capability's note: mostly Shopify's admin routes in its section Payments and Salla's payment methods page or its links under /payments/.
- **M-025, the finer side.** As batch 3 left it: SH-C-076 lands in CM-PAY-011, a child of CM-PAY-001, and the Salla batches land SA-C-120 there. Shopify's providers are apps on its Payments Apps API (extension-point); Salla's gateways are integrations it names and switches by flag, with no app interface in the statements held (core where released, shows where not).
- **PayPal under wallets (CM-PAY-013 under CM-PAY-012),** by the grouping both platforms share: Shopify's plan row PayPal Wallet rates (SH-S-7024) and Salla's "PayPal as a digital wallet option" (SA-S-0199). SH-C-063's SH-S-0022, left by batch 3, is cited here under both its keys (SH-C-063 and SH-C-077).
- **Shop Pay (CM-PAY-014) under CM-CHK-008, area PAY.** Shopify's two groupings differ: its Shop Pay Merchant Terms put it under "1. Accelerated Checkout (Shop Pay)" (SH-S-0413), and Shopify's definition of accelerated checkouts, already cited in CM-CHK-008, is that they "save customer payment and shipping information" (SH-S-7287); its admin route sits in its section Payments (SH-S-7111). I followed the terms, since they say what the thing is, and kept the area PAY, since Shop Pay "only enables payment processing through the sharing of payment credentials" (SH-S-0408) and has the Shop Pay Wallet API. The reviewer may prefer CM-PAY-001 as parent, by the admin route; then U-026 would be `apart` unless CM-CHK-008 cited SH-C-074's keys. Named for what it does, not "wallet": Salla's words for its side are saving the customer's card and address.
- **Shop Pay Installments isn't under Shop Pay,** though it needs Shop Pay activated (SH-S-0415): its route is a sibling in section Payments (SH-S-7112), and Salla's instalments stand on its payment methods page. The product's brand doesn't make it a child.
- **Chargebacks and disputes (CM-PAY-009) under CM-PAY-002,** by Shopify's API grouping (the Shopify Payments resources and scopes read_shopify_payments_disputes) and its Shopify Payments Terms' Part I, C; its admin route sits in its section Finances. **Chargeback protection (CM-PAY-010) apart from it,** under CM-PAY-002 ("an add-on to the general Shopify Payments services", SH-S-0402), and apart from CM-ORD-006: Shopify Protect evaluates orders for fraud (SH-S-0404), but what it gives is cover for the chargeback.
- **Manual methods (CM-PAY-016), M-033, a difference of grain.** One capability for Shopify's one concern; Salla's three concerns (cash on delivery by Salla's labels or by the merchant's carrier, and bank transfer) are cited in its cell. **For the Salla batches:** they may add children for cash on delivery and bank transfer. Salla's cash on delivery setting sits under shipping (shipping/shipping.cod, SA-S-1765), its bank account under payment methods (SA-S-0095); I kept the parent CM-PAY-001 by Shopify's route and Salla's plan lines in its payment group.
- **Local payment methods (CM-PAY-017) under CM-PAY-002,** since Shopify's are activated "with Shopify Payments" (SH-S-0420) and Salla's KNET "through Salla Payments" (SA-S-0065). Salla's K net through Tap (SA-S-0130) is a gateway and stays in CM-PAY-011. mada isn't cited: its plan line has no country scope, and no statement makes it region-specific.
- **Payment method rules (CM-PAY-019) under CM-PAY-001,** not without a parent like batch 1's function capabilities (CM-CHK-005, -006): Shopify's own route Payment customizations sits in its section Payments (SH-S-7119), and Salla's link Payment restrictions at /payments/rules (SA-S-1877).
- **Cryptocurrency (CM-PAY-018) under CM-PAY-001,** since it comes both through third-party gateways (SH-S-0428) and through Shopify Payments (SH-S-0433, SH-S-0432).

### Joins on role (readings)

- **CM-PAY-014:** Shop Pay saves the buyer's "email address, payment method, and shipping and billing information, making the checkout process faster" (SH-S-0406); Salla's shopping experience fee includes "the services of saving the customer's card and address" from Salla Payments (SA-S-0104). Whether Salla's saved details serve other stores isn't stated; Salla gives it no admin place.
- **CM-PAY-017:** Shopify's local payment methods, "region-specific ways to pay" through Shopify Payments (SH-S-0420); Salla's KNET through Salla Payments for Kuwait stores (SA-S-0065). Salla doesn't call it local; the region is the statement's scope.
- **CM-PAY-019:** Shopify's Payment Customization hides, reorders or renames the payment methods offered at checkout (SH-S-0589); Salla's payment restrictions are "conditions imposed on payment options", such as restricting a method for some countries or customers (SA-S-5050).

### Homonyms

- **"Reorder":** Shopify's Payment Customization reorders payment methods (SH-C-083/where/SH-S-0589). The checker's flag on CM-ORD-014 (Salla's Reorder, repeating an order) lists it as a match: it is a different thing.
- **"Dispute":** a chargeback dispute (CM-PAY-009) against the dispute resolution clauses of Salla's partner agreements (SA-S-0021, SA-S-0044) and the merchant's disputes with its customers under Shop Pay (SH-S-0410, shows in CM-PAY-014). Salla's Transactions reverse (SA-S-0180, SA-C-123) is the merchant's own reversal, not a chargeback.
- **"Wallet":** Shopify's Shop Pay Wallet API and PayPal Wallet, and Salla's المحافظ الرقمية (payment wallets, CM-PAY-012 and -013), against Salla's Wallet link (the store balance, A's CM-PLN-006), the customer wallet (D's CM-LOY-001) and the ads wallet (D's CM-MKT-020).
- **"الدفع الآجل" / "وسائل الدفع الآجلة":** buy now pay later (CM-PAY-015), not Shopify's payment terms (CM-PAY-008), as batch 3 noted.
- **"Reviews"** in Shopify's legal routes (section Reviews, SH-S-7109, SH-S-7110) names a terms page's section, not product reviews.
- **"Quick purchase through Apple Pay"** (الشراء السريع عبر Apple Pay, in SA-S-0104) uses CM-CHK-008's word for a wallet's button; not cited in CM-CHK-008.

### Strained fits

- **SH-C-078 in CM-PAY-012:** its SH-S-0419 (accelerated checkout buttons) and SH-S-7287 (their purpose) are cited in CM-CHK-008 (batch 1), outside CM-PAY-001's tree. Here SH-S-0419 is shows.
- **SH-C-079 in CM-PAY-016:** its SH-S-5144 (the mobile app's record-payment route) is core in domain E's CM-SRF-001; here it is shows.

### Statements shared with other domains, cited here only as shows

- SH-S-0244 (Shopify as data controller for Shop or Shop Pay) is own-service in E's CM-CHN-002 and shows in A's CM-TRU-013; shows in CM-PAY-014.
- SH-S-0094 (Shopify gives the merchant's customers no dispute rights, SH-C-072) is shows in CM-PAY-009; it is a lead for A's CM-TRU-020, whose Shopify cell is none-held.
- SH-S-5144: above.

### Rulings

- **U-026 (SH-C-074 against SA-C-079): `nested:CM-PAY-014`.** CM-PAY-014 cites Shop Pay's keys and its parent CM-CHK-008 cites Salla's quick checkout. CM-CHK-008's Shopify cell is unchanged: it already names Shop Pay's button among the accelerated checkout buttons (SH-S-0419); its reading's "Shop Pay itself (SH-C-074) is batch 4's" is settled by the child.

### Left for later batches

- **U-022** (SH-C-083 against SA-C-121): CM-PAY-019's Salla cell cites SA-C-121's keys, so if SA-C-121 lands there the ruling is `joined:CM-PAY-019`.
- **U-023** (SH-C-078 against SA-C-110 and SA-C-119): CM-PAY-012's Salla cell cites keys of both (Apple Pay and Google Pay of SA-C-110; stc pay and PayPal of SA-C-119), so each pair is `joined:CM-PAY-012` once they land.
- **U-024** (SH-C-080 against SA-C-110): CM-PAY-017 cites SA-C-110's SA-S-0065, so `joined:CM-PAY-017` once SA-C-110 lands.
- **U-025** (SH-C-081 against WC-C-005) is WooCommerce's part's to rule.
- **The matches' Salla sides:** SA-C-120 in CM-PAY-011 (M-025), SA-C-118 in CM-PAY-015 (M-031), SA-C-119 in CM-PAY-013 or CM-PAY-012 (M-032; its stc pay direct is cited in CM-PAY-012, and its Mokafaa Al Rajhi, paying with loyalty points, SA-S-1966 and SA-S-3140, is uncited, for the Salla batch), SA-C-115, SA-C-116 and SA-C-117 in CM-PAY-016 (M-033). The coordinator may then change my landings' joins to the match.
- **SA-C-127 (charity stores' gateways):** SA-S-0206 and SA-S-5057 (Apple Pay for charities) are uncited, for the Salla batch; CM-PAY-011 or -012 may hold them.
- **For batch 5:** SH-C-085 (saved customer payment methods and payment mandates, vaulted for charging later) is close to CM-PAY-014; whether it is the same thing is batch 5's to read. SH-C-084 (transactions) against SA-C-123: SA-S-0180 (refund, void, reverse) was found by CM-PAY-009's search and left uncited.
- **SA-C-122 (fraud protection):** its plan line قيود الدفع والحماية من الاحتيال (SA-S-2145) is held in SA-C-121 and SA-C-122; I cite it as core in CM-PAY-019 under SA-C-121's key. Under SA-C-122's key it may support CM-ORD-006, as the coordinator directed.

### Gaps

- No statement held names a Shopify company as the maker of Shop Pay Installments; the cell claims core from its route and scopes and outside from Affirm's agreement.
- No Salla statement held gives its saved card and address an admin place, a flag or a definition (CM-PAY-014), names the lender behind its instalment providers (CM-PAY-015), or shows chargebacks, chargeback cover or cryptocurrency (CM-PAY-009, -010, -018, none-held).
- Q1's gaps: reason (searched, not found) on SH-C-072, SH-C-073, SH-C-077, SH-C-079, SH-C-081 and SH-C-083; responsible (stated only in general terms) on SH-C-079 and SH-C-080.
- SH-C-075's SH-S-6147 says only "Requires `unauthenticated_read_checkouts` access scope"; the object it is on (ShopPayInstallmentsFinancingPlan) is in Q1's note, so it is shows, and the object's name isn't claimed.

### Qualities

- CM-PAY-013 Shopify: PayPal Wallet rates, starting at 3.49% + 49¢ (SH-S-7024). CM-PAY-015 Shopify: 0-36% APR (SH-S-7219). CM-PAY-017 Shopify: MB WAY and Bizum rates by plan (SH-S-7025, SH-S-7026). CM-PAY-018 Shopify: USDC rates by plan (SH-S-7028). CM-PAY-019 Shopify: at most 25 payment customization functions per store (SH-S-0590).
- CM-PAY-016 Salla: a 1000 SAR maximum for cash on delivery through Salla's labels (SA-S-0123), and no cash on delivery for a cart under 20 SAR (SA-S-0125).

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas PAY`) gives "0 problems, 30 flags for the reviewer". I fixed one problem in my rows: a term from Q1's note, not the statement (above, Gaps). The 24 flags on CHK, ORD and CM-PAY-001 to -008 are batches 1 to 3's, answered in their sections. Mine:

- **Own-service on SH-S-0401, SH-S-0411 and SH-S-0413.** SH-S-0401 names "the warranty issuer, Shopify Inc." for Shopify Protect. SH-S-0411 is the Shop Pay Merchant Terms' definition of Shopify as "Shopify Inc., and its Affiliates", and SH-S-0413, in those terms under "1. Accelerated Checkout (Shop Pay)", says Shopify "will collect and store certain personal information from the Customer": the platform's company named as the provider of the product, under terms of its own. The reviewer may read SH-S-0413 as shows.
- **CM-PAY-009 Salla, none-held, 10 matches,** and **CM-PAY-010 Salla, none-held, 34 matches:** answered in the cells' readings (the merchant's reversal, partner agreements, subscription refunds; fraud protection with no stated cover, other kinds of protection).
- **SA-C-113/boundary/SA-S-0104 cited in CM-PAY-007 and CM-PAY-014, in two trees.** The statement is the shopping experience fee's description: as a fee it is shows in CM-PAY-007 (batch 3), and it is the only Salla statement held that names saving the customer's card and address, shows in CM-PAY-014. Neither cites it for a placement.

For the coordinator, on earlier rows: SA-S-0065 (KNET through Salla Payments) is now core in CM-PAY-002 (batch 3) and in its child CM-PAY-017; one of them may be shows. CM-PAY-008's Shopify reading names SH-S-0589 as shows, but no evidence row cites it there; it is cited in CM-PAY-019.

## Batch 5: PAY, Payments, payouts and money (third of six)

Concerns: SH-C-084, SH-C-085, SH-C-086, SH-C-088, SH-C-089, SH-C-090, SH-C-091, SH-C-092, SH-C-093, SH-C-094, SH-C-095. Seven capabilities, CM-PAY-020 to CM-PAY-026; all eleven concerns land in new ones, none being the same thing as CM-PAY-001 to -019 or any capability of another domain. Every capability was first searched in every domain with `caps` (terms: transaction, transactions, capture, authorization, authorisation, المعاملات, معاملة, العمليات, refund, استرجاع, void, mark as paid; vault, vaulted, mandate, payment method, saved card, token, البطاقات المحفوظة, حفظ البطاقة, recurring, subscription, الاشتراكات; balance, banking, bank account, credit card, Shopify Credit, financing, funding, capital, loan, cash advance, تمويل, التمويل, رصيد, الرصيد, بطاقة, بطاقات, قرض, in-person, card present, point of sale, Tap to Pay, softpos). What it found and kept apart: A's CM-PLN-004 to -006 (platform billing, Salla's prepaid store balance), D's CM-LOY-001 to -003 (the buyer's wallet and store credit, gift cards, cashback), CM-MKT-018 and -020, B's CM-SEL-001 (subscriptions and recurring payments), E's CM-POS-001 to -003, F's CM-API-002, CM-APP-003 and CM-PTN-003, and C's CM-PAY-005 and CM-PAY-014. Every Shopify and Salla cell is written for the seven.

### How I cut, and the grains

- **CM-PAY-020, payment transactions on an order (M-034),** parent CM-ORD-001. One capability for Shopify's authorization and capture (SH-C-084) and Salla's refund, void and reverse (SA-C-123): M-034 joins them one-to-one on the term transactions, and its note says the two cover different actions. Parent by Shopify's admin grouping (its where is the Orders page, its permissions sit under Orders and Drafts). Salla's grouping differs: its link Transactions sits in the payments list (/payments/transactions), its permission payments_operations_management in the group إعدادات المتجر and its refund permission order_refund_payment in the group الطلبات. The reviewer may prefer no parent, or CM-PAY-001 by Salla's link. **For RET's batch:** Salla's refund of a transaction (SA-S-0180, SA-S-2270, the permission order_refund_payment, SA-S-0181) is cited here, the permission as shows; RET may cite them for the refund.
- **CM-PAY-021, in-person card payments,** parent CM-PAY-001, the grouping both platforms share, a reading: Shopify's run through Shopify Payments (SH-S-0436, SH-S-0047), Salla's through Geidea (SA-S-5040), so CM-PAY-002 would fit Shopify only. As the lead and E's CM-POS-002 note say, the payment's processing, rates and rules are here; the POS and its devices stay in E's CM-POS-001 and -002. SH-C-086's admin route apps/point-of-sale-channel (SH-S-6329) is shows here; E's CM-POS-001 names it in its note, not in its evidence. Salla's side is SA-C-095's statements (domain E, which names C under also for its Geidea card-present payment statements): outside here, outside in E's CM-POS-002 too, so no double placement.
- **CM-PAY-022, saved customer payment methods and payment mandates (SH-C-085), apart from CM-PAY-014.** Batch 4's lead asked whether they are the same thing. A reading: no. CM-PAY-014 is the platform saving the buyer's details "making the checkout process faster" (SH-S-0406), through Shop Pay, across checkouts; SH-C-085 is the store keeping a customer's payment method to "pay for future orders without requiring the customer to manually go through checkout" (SH-S-0592), charged by staff (Charge vaulted payment method) or an app (write_payment_mandate). Q1's M-035 joins it with WooCommerce's payment tokens only. No parent: Shopify's route is on the customer's record (section Customers, domain D's), its permissions under Orders and Drafts.
- **CM-PAY-023 (Shopify Balance), with CM-PAY-024 (its cards) under it; CM-PAY-025 (Shopify Credit); CM-PAY-026 (Capital).** Each has a place of its own (admin sections Banking, Cards, Credit and Capital, with routes and plan rows). Cards under Balance by Shopify's own name for them, Shopify Balance Visa® Commercial cards, and the rule tying the card's use to the Balance account (SH-S-0465). Credit apart from Cards and from Capital: its own section and route, a card account with a credit limit set by the issuing bank (SH-S-7267), not funding repaid from sales. As the lead says, Balance is not A's CM-PLN-006 (Salla's prepaid balance spent on the platform's services) nor D's CM-LOY-001 (the buyer's wallet with the store).
- **No parent for the Finance suite.** Shopify groups Balance, Credit and Capital in its Finance suite ("built into your Shopify admin", SH-S-0454; the admin page finance, cited as shows; the product Finances & Funding, SH-I-1983, uncited). No concern of either platform is the suite as such, so I added no capability for it; the reviewer may want one as parent of CM-PAY-023, -025 and -026. Salla shows only CM-PAY-026 of the three.
- **CM-PAY-026, Capital (M-038), a difference of grain.** One capability for Shopify's seven country concerns (five here, SH-C-096 and SH-C-097 in batch 6), each statement keeping its country scope: they share Capital's section, route, entitlement shopifyFinance.capital, plan row and eligibility statements, and differ by lender and agreement, which go in slot fillers. A capability per country would be cut by a market's facts. The shared statements are cited under each concern's key. Loan against merchant cash advance (SH-S-7218: "either as a loan or merchant cash advance") is a difference of instrument by country; I kept it one capability, since Shopify gives the two no separate place but their legal agreements (SH-I-1410 to SH-I-1414). Salla's side (SA-C-128) is financing collected as 25% of net sales from each payment (SA-S-0111), managed with the fund manager Tanami.

### Joins on role (readings)

None. All eleven landings are `single`: M-034 (SA-C-123) and M-038 (SH-C-096, SH-C-097, SA-C-128) have concerns that later batches land; M-035 and M-036 hold only WooCommerce on the other side.

### Homonyms

- **"Balance":** Shopify Balance, the merchant's money account (CM-PAY-023), against Salla's Wallet and store balance (رصيد المتجر, SA-C-005, A's CM-PLN-006), Salla's e-payments balance (CM-PAY-005), the customer wallet (D's CM-LOY-001), and the store balance a Salla refund needs (SA-S-0181, cited as shows in CM-PAY-020).
- **"Credit":** Shopify Credit, credit to the merchant (CM-PAY-025), against Shopify's store credit for buyers (D's CM-LOY-001), Salla's wallet setting Maximum Credit Usage Limit (SA-S-1766), Salla's marketing credits (SA-S-3574), and the buyer's credit card as a payment method (Salla's credit_card flag, SA-S-3151; الدفع عبر البطاقة الائتمانية, SA-S-1960).
- **"Cards":** Shopify's Balance cards (CM-PAY-024) against Salla's Gift cards (SA-S-1767, D's CM-LOY-002), its gift messages and cards (SA-S-1729), and the cards buyers pay with.
- **"Transactions":** the order's payment transactions (CM-PAY-020) against Shopify Credit's card transactions (VIEW_ALL_SHOPIFY_CREDIT_TRANSACTIONS, CM-PAY-025) and Capital transaction history (finance/capital, CM-PAY-026).
- **"Payment methods":** Shopify's customer route Payment methods, the customer's saved methods (SH-S-7120, CM-PAY-022), against the store's payment settings, Salla's link Payment methods at /payments (SA-S-1875, CM-PAY-001).

### Strained fits

None. No statement of my concerns is cited in another tree of capabilities: SH-S-0347 (payouts into Shopify Balance up to 7 days earlier) is shows in CM-PAY-005 (batch 3, under SH-C-069's key) and in CM-PAY-023 (under SH-C-088's keys), in two trees, cited for no placement in either.

### Statements shared with other domains

- SA-C-095's SA-S-5038, SA-S-5039, SA-S-5040 and SA-S-5042 (domain E, naming C under also) are outside or shows in CM-PAY-021 and in E's CM-POS-002.
- Several of SH-C-085's statements (SH-S-6079, SH-S-6265, SH-S-6266) are also held by SH-C-158 and SH-C-159 (domain F); I cite them only under SH-C-085's keys.
- Found by search and left uncited: SH-C-008/decides/SH-S-0264 (identity verification when applying for Capital or Credit, domain A's), SH-C-182/responsible/SH-S-0204 (Shopify Capital Inc. listed as an affiliated subprocessor, domain A's), SH-C-054/decides/SH-S-6228 (write_marketplace_orders needs the permission capture_payments_for_orders, batch 2's concern; it could be shows in CM-PAY-020), SH-C-098/boundary/SH-S-0501 (Bill Pay paid from the Balance account, batch 6's concern).

### Rulings

None: no unclear candidate holds any of my concerns.

### Left for later batches

- **M-034:** SA-C-123 lands in CM-PAY-020, whose Salla cell cites its keys; the coordinator may then change SH-C-084's join to the match.
- **M-038:** SH-C-096 and SH-C-097 (batch 6) and SA-C-128 (a Salla batch) land in CM-PAY-026, whose Salla cell cites SA-C-128's keys. SH-C-096's and SH-C-097's statements are uncited; batch 6 adds them to CM-PAY-026's Shopify cell (the shared statements under their keys, and their lenders, YouLend GmbH and YouLend, as slot fillers).
- **Salla's flag checkout-save-cards (SA-S-3123, SA-C-110):** it saves cards at checkout. I left it for the Salla batch that lands SA-C-110, for CM-PAY-014's Salla cell, which is now not-stated; it isn't cited in CM-PAY-022 (see that cell's reading).
- **Salla's Recurring Payments (SA-C-125, domain B):** if a Salla statement shows recurring charges to a stored payment method, CM-PAY-022's Salla cell could cite it; none held does.
- **Shopify Bill Pay (SH-C-098), batch 6:** paid from a bank account or the Balance account (SH-S-0501); it may be a capability of its own beside CM-PAY-023.

### Gaps

- No statement held names a Shopify company as the maker or provider of Shopify Balance, its cards, or Capital in the United States, Canada and Australia. The cells claim core from their admin places. Capital's UK and French statements name Shopify and Shopify Commerce France SAS (own-service); Credit's Program Terms name Shopify Capital Inc.
- Q1's gaps: responsible (observation needed) on SH-C-093 and SH-C-094, so Canada's and Australia's lender isn't held; boundary (observation needed) on SH-C-089, the card program's terms and interface; responsible (stated only in general terms) on SH-C-085 and SH-C-086; reason (searched, not found) on SH-C-085, SH-C-086, SH-C-089, SH-C-091 to SH-C-095. On the Salla side: SA-C-123's responsible and reason, SA-C-128's reason (page not read).
- No statement held names a Salla company as the maker or provider of its financing: صندوق سلة carries Salla's name, which doesn't name the maker; the fund manager is Tanami.
- SH-I-1484 (extension point Card present) is cited as extension-point on Q1's inventory category alone; no statement held says what an app does there.
- No Salla statement held shows authorization or capture, in-person payments through Salla Payments, saved payment methods charged outside checkout, a merchant money account, merchant cards or merchant credit.

### Qualities

- CM-PAY-020 Shopify: a 7-day authorization period (SH-S-0391); extended periods only for Plus stores on Shopify Payments (SH-S-0393).
- CM-PAY-021 Shopify: In-person card rates and In-person manual rates per plan (SH-S-7027, SH-S-7029); no Interac offline in Canada (SH-S-0588).
- CM-PAY-023 Shopify: the earnings rate per plan (SH-S-7062); US or Puerto Rico residence (SH-S-0460).
- CM-PAY-025 Shopify: up to 3% cashback (SH-S-7064); repayment over 10 calendar months (SH-S-0468).
- CM-PAY-026 Shopify: the US loan's maximum term of 18 months with 2 minimum payments (SH-S-7218). Salla: 25% of net sales collected from each payment (SA-S-0111).

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas PAY`) gives "0 problems, 38 flags for the reviewer". The 32 on CHK, ORD and CM-PAY-001 to -019 are batches 1 to 4's, answered in their sections. Mine:

- **Own-service on SH-S-7276 and SH-S-7279** (Shopify Credit's Program Terms are an agreement with Shopify Capital Inc., which provides access to the program), **SH-S-0484** ("Shopify provides merchant cash advances in the United Kingdom through our partner YouLend") and **SH-S-0491** ("This application is provided by Shopify Commerce France SAS"). Each names Shopify, or a company of its group by its legal name, as the provider of a financial service separate from the store's own payments. SH-S-0484 is also outside under its boundary key, for YouLend.
- **CM-PAY-022 to CM-PAY-025 Salla, none-held, with 22, 99, 6 and 11 matches:** the matches come from Shopify's terms Payment methods, Balance, Cards and Credit, each a homonym above; answered in each cell's reading.

For the coordinator, on earlier rows: none found wrong. CM-PAY-014's Salla cell (not-stated) may gain SA-S-3123 (checkout-save-cards) when SA-C-110 lands.

## Batch 6: PAY, Payments, payouts and money (fourth of six)

Concerns: SH-C-096, SH-C-097, SH-C-098, SH-C-173, SH-C-191, SA-C-006, SA-C-110, SA-C-111, SA-C-112, SA-C-113, SA-C-114. Two capabilities added, CM-PAY-027 (Bill Pay) and CM-PAY-028 (accounting and ERP integrations); nine concerns land in existing capabilities, two in the new ones. Every capability was first searched in every domain with `caps` (terms: bill pay, bills, vendor, فواتير, سداد الفواتير, accounting, ERP, محاسبة, المحاسبية, prohibited, restricted business, محظور, الممنوعة, selling policy, سياسة البيع, acceptable use). What it found and kept apart: A's CM-PLN-004, -005 and -007 (the platform's bills to the merchant and their taxes), CM-TRU-009 (the platform's Acceptable Use Policy), CM-TRU-010 and -015; B's CM-CAT-009 (product restrictions) and CM-CAT-010; C's CM-ORD-008 (order invoices); D's CM-B2B-001; E's CM-POS-001 (matched "ERP" inside another word); F's CM-APP-003 and CM-PTN-001. None is the same thing. Both platforms' cells are written for the two new capabilities.

### Where each concern landed, and the grains

- **SH-C-096 and SH-C-097 in CM-PAY-026** (Capital, M-038), as batch 5 cut it: the shared statements (section, routes, entitlement, plan row, eligibility, read_capital) under each concern's own key, and the lenders by country: YouLend GmbH (Germany), YouLend (Ireland, the Netherlands, Spain), as outside and slot fillers. Germany's application "made available to you by Shopify Commerce Germany GmbH, which is a registered Credit Broker in Germany" (SH-S-0493) is own-service, as France's SH-S-0491 is, and a quality.
- **SH-C-098 in a new CM-PAY-027, Bill Pay.** It has a place of its own (routes finance:billpay, entitlement shopifyFinance.billPay, plan row). Beside CM-PAY-023, not under it: bills are paid "using a bank account or your Shopify Balance account" (SH-S-0501). No parent, like the other Finance pages (batch 5).
- **SH-C-173 in CM-PAY-002, not a capability of its own,** a reading. Shopify's prohibited and restricted businesses for Shopify Payments have no admin section, route, API group, plan line or app category: Q1's gaps on where, responsible and boundary are all "searched, not found", and what is held is a help page and Part I, B of the Shopify Payments Terms. By the dry run's rule that is no place of its own, so the concern lands in the service whose rule it is. Not A's CM-TRU-009: the categories are "provided by each Payment Processor in your Designated Country" (SH-S-0109) for the payment service, not the platform's own use rules. SH-S-0327 ("business models that, while legal, Shopify Payments can't support") is core under SH-C-173's key; batch 3 cites it as shows under SH-C-063's. The reviewer may prefer a capability of its own under CM-PAY-002, by the WooCommerce side of M-085 and Salla's selling policy (SA-C-172); then SH-C-173 would move there.
- **SH-C-191 in a new CM-PAY-028, accounting and ERP integrations (M-077).** Both platforms give it app categories; Salla also plan lines and released flags. Area PAY by the seed's "balance and finances"; scope.tsv names G under also for both concerns, and no capability of G or any domain holds it.
- **SA-C-006 in CM-PAY-003 by M-003, SA-C-110 in CM-PAY-002 by M-026, SA-C-111 and SA-C-112 in CM-PAY-005 by M-027, SA-C-113 in CM-PAY-007 by M-029,** as batch 3 left them. **SA-C-112 has no child** of its own for the payout account: neither platform gives the account a place of its own (Salla's where is an FAQ, SA-S-0094), and M-027 says Shopify keeps the account inside payouts.
- **SA-C-114 in CM-PAY-004, a join on role** (no Q1 match holds it): who settles the payment service's transactions and on what terms. Shopify names its Payment Processors (SH-S-0082); Salla says only that payments are settled and transferred under the payment services contract (SA-S-0081, SA-S-0088). Salla's cell stays not-stated: no processor, acquirer or licence is held (Q1's gaps, all "page not read").
- **Evidence added to earlier cells from SA-C-110's statements:** the plan line تفعيل الدفع الإلكتروني عبر مدى وأبل باي وتابي وغيرها (SA-S-2106), core in CM-PAY-001, since it activates methods of several providers (Tabby and Tamara among them); the released flag stc-pay (SA-S-3108), core in CM-PAY-012, with stc pay's reason within Salla Payments (SA-S-0128) as shows; the released flag checkout-save-cards (SA-S-3123), core in CM-PAY-014, as batch 5 suggested, a reading from the flag's name: it saves cards at checkout, and for whom isn't stated; the flag knet under SA-C-110 as shows in CM-PAY-017 (core in CM-PAY-011 under SA-C-120's key); the requirements and unreleased flags as shows in CM-PAY-002.

### Earlier `single` landings that can now be written as matches

For the coordinator: SH-C-063 (CM-PAY-002) as `match:M-026`; SH-C-068 (CM-PAY-003) as `match:M-003`; SH-C-069 (CM-PAY-005) as `match:M-027`; SH-C-071 (CM-PAY-007) as `match:M-029`. The Capital landings (SH-C-091 to SH-C-097) wait for SA-C-128 (M-038), and SH-C-191 for SA-C-210 (M-077).

### Joins on role (readings)

- **SA-C-114 in CM-PAY-004** (above): Shopify's processing and settlement "carried out by Payment Processors and Financial Services Providers" (SH-C-064/where/SH-S-0082) against Salla's settlement "under the payment services contract signed during your store verification" (SA-C-114/responsible/SA-S-0081, SA-S-0088).

### Homonyms

- **"Bills":** Shopify Bill Pay, the merchant's bills to its vendors (CM-PAY-027), against the platform's bills to the merchant (A's CM-PLN-004 and -005; Shopify's SH-C-016), Salla's order invoices (فواتير, CM-ORD-008), the billing system of Salla's partners (SA-S-0045) and Salla's key billing_cycle in SA-S-0103, whose text is a transfer day (cited as shows in CM-PAY-005).
- **"Vendors":** Bill Pay's vendors, the merchant's suppliers (SH-S-0501), against Salla's marketplace vendors (SA-C-098, its vendors_* permissions and app ui-merchant-vendors). Not cited.
- **"Prohibited" / "restricted":** Shopify Payments' prohibited businesses (CM-PAY-002), against A's CM-TRU-009 (acceptable use), B's CM-CAT-009 (Salla's product restrictions, قيود المنتج) and Salla's قيود الدفع (payment restrictions, CM-PAY-019).
- **"Integration":** Salla's plan line ربط المتجر بخدمات محاسبية ومالية متكاملة has a description about search engines (SA-S-2152); the words as a whole don't settle it, so it is shows in CM-PAY-028.

### Strained fits

- **SA-C-006 in CM-PAY-003:** its dashboard app SA-S-3549 (held also by SA-C-100 and SA-C-110) is cited in CM-CHK-001.
- **SA-C-110 in CM-PAY-002:** SA-S-3549 in CM-CHK-001, SA-S-1583 (order.payment.updated) in CM-ORD-001, and SA-S-3123 in CM-PAY-014 (under CM-CHK-008).
- **SA-C-113 in CM-PAY-007:** SA-S-0104 in CM-PAY-014 (batch 4).

### Statements shared with other domains

- SA-C-006's SA-S-0133 and SA-S-0142 (entity type, legal entity) are core in A's CM-ACC-004, and SA-S-0141 (store country) core in A's CM-ONB-001: all three are shows in CM-PAY-003, which doesn't rest on them.
- SA-S-0138 (beneficial owners' data) is shows in A's CM-TRU-002 and core here, as A's note asks that Salla's store verification count once, in domain C. SA-S-0136 (UAE licence types accepted in verification) is shows in A's CM-TRU-010 under SA-C-231 and core here. SA-S-0131 and SA-S-0118 (the regulatory reason, the mandatory e-commerce certificate) are shows in both.
- SA-S-0105 (VAT at 15% on the fees) is shows in A's CM-PLN-007 and shows in CM-PAY-007.
- SA-S-3185, the released flag sbc-registration, is core in CM-PAY-003 by the convention on released flags, as Q1 placed it in store verification. Its name doesn't say what it registers; if the coordinator reads it as the e-commerce certificate, it belongs to A's CM-TRU-010, which doesn't cite it.
- SH-C-191's SH-S-0058 and SH-S-7284 are general clauses of Shopify's Terms on Third Party Services; shows only here.

### Rulings

- **U-024 (SH-C-080 against SA-C-110): `joined:CM-PAY-017`,** as batch 4 left it.
- **U-023 (SH-C-078 against SA-C-110): `joined:CM-PAY-012`.** The pair against SA-C-119 is left.
- **U-027 (SH-C-065, SH-C-066 and SH-C-067 against SA-C-114): `joined:CM-PAY-004`,** three rows. They follow the cells; the candidate's question, which licensed entity holds Salla's funds, isn't answered by any statement held.
- **U-007 (SH-C-008), U-011 (SH-C-006) against SA-C-006: `apart`,** scope.tsv gives them domain A with no also. **U-008 (SH-C-004 and SH-C-005 against SA-C-006) and U-029 (SH-C-017 against SA-C-113): `apart`:** domain A names C under also, but no capability here cites their keys; A's CM-ACC-004 and CM-PLN-007 hold the joins.

### Left for later batches

- **U-038 (SH-C-173 against SA-C-172):** SA-C-172's batch rules. SH-C-173 is in CM-PAY-002, whose Salla cell cites SA-C-110's SA-S-0068 (agreeing to the selling policy when activating) as shows; if SA-C-172's keys are cited in CM-PAY-002 too, the ruling is `joined:CM-PAY-002`. The selling policy's text isn't held.
- **U-064 and M-077:** SA-C-210 lands in CM-PAY-028, whose Salla cell already cites its keys, so SH-C-191 against SA-C-210 is `joined:CM-PAY-028`; SH-C-196 against SA-C-210 is `apart` (scope.tsv gives SH-C-196 domain A, no also).
- **U-023, SH-C-078 against SA-C-119;** **U-027, the pairs against SA-C-177** (CM-PAY-004's Salla cell cites only SA-C-177's agreement entry SA-I-2612); **M-038, SA-C-128** in CM-PAY-026.

### For the coordinator, on earlier rows

I added evidence to earlier cells without rewriting their readings, which now don't name it:
- **CM-PAY-003 Salla:** its reading says the entity type and legal entity steps "are not cited here"; they now are, as shows. It could add the core rows SA-S-0136, SA-S-0138 and SA-S-3185.
- **CM-PAY-014 Salla:** its reading says no Salla statement gives a flag; the flag checkout-save-cards (SA-S-3123) is now core, so the cell is no longer not-stated.
- **CM-PAY-026 Shopify:** own-service Shopify Commerce Germany GmbH (SH-S-0493); outside YouLend GmbH and YouLend (SH-S-0492, SH-S-0494 to SH-S-0496).
- **CM-PAY-002 Shopify:** core SH-S-0327 under SH-C-173; outside the Payment Processors' categories and the Payment Network Rules (SH-S-0108, SH-S-0109).
- **CM-PAY-001, -005, -012 Salla:** core SA-S-2106; core the payout account's bank, currency and type (SA-S-0135, SA-S-0139, SA-S-0140) and the Special plan's 24-hour deposit (SA-S-2193, SA-S-0202); core the flag stc-pay (SA-S-3108).
No earlier row was found wrong.

### Gaps

- No statement held names the maker of the Shopify Bill Pay app (SH-S-0500: install from the App Store); Melio "provides" and "powers" it (outside). No own-service is claimed.
- SH-C-173: Q1's where, responsible and boundary gaps (searched, not found). Salla's selling policy (SA-C-172) isn't held (U-038).
- SA-C-114: all four placements "page not read"; SA-C-112 responsible and reason, SA-C-111 and SA-C-113 reason, SA-C-006 responsible, "page not read". SA-C-210: responsible (stated only in general terms), reason (page not read). Q1's reason gaps on SH-C-096, SH-C-097, SH-C-098 and SH-C-191 (searched, not found).
- No Salla statement held shows paying the merchant's own bills (CM-PAY-027, none-held).

### Qualities

- CM-PAY-026 Shopify: Shopify Commerce Germany GmbH, a registered Credit Broker (SH-S-0493). CM-PAY-027 Shopify: United States only (SH-S-0498).
- CM-PAY-005 Salla: the payout account at an Emirati bank in dirhams (SA-S-0135), at a Kuwaiti bank in dinars (SA-S-0139), commercial accounts only in Kuwait (SA-S-0140), the digital stores' transfer on Sunday (SA-S-0103), deposits every 24 hours on سلة سبيشل (SA-S-0202).

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas PAY`) gives "0 problems, 40 flags for the reviewer". I fixed one problem in my rows, U-023's Shopify key (SH-C-078/where/SH-S-0419, a key CM-PAY-012 doesn't cite; now SH-S-0025 and SH-S-0026, which it does), and one flag: SH-I-0805 (Finances) is dropped from CM-PAY-027, since Q1 also places it in SH-C-069 and citing it there made batch 3's SH-C-069 landing read as strained. The flags on CHK, ORD and CM-PAY-001 to -026 are batches 1 to 5's, answered in their sections. Mine:
- **Own-service on SH-S-0493:** it names Shopify Commerce Germany GmbH, a company of Shopify's group by its legal name, as the one that makes the financing application available, as France's SH-S-0491.
- **CM-PAY-027 Salla, none-held, 26 matches:** Salla's marketplace vendors, its postpaid labels and its partners' billing, answered in the cell's reading.
- **SA-S-0104 in CM-PAY-007 and CM-PAY-014:** batch 4's, answered there.
`uncited --domain C` lists none of this batch's concerns' statements.

## The coordinator's corrections after batch 6 (30 October)

- **SH-C-063, SH-C-068, SH-C-069 and SH-C-071** are written as Q1's matches M-026, M-003, M-027 and M-029, now that their Salla sides have landed.
- **Seven cells' readings** name batch 6's rows: Salla's CM-PAY-001, -003, -005, -012 and -014, Shopify's CM-PAY-002 and -026. CM-PAY-014's Salla cell now holds a released flag, so it is no longer not-stated.
- **SA-S-3185, the released flag sbc-registration,** is `core` in CM-PAY-003 on its name; the final review weighs whether it belongs to A's CM-TRU-010.


## Batch 7: PAY, Payments, payouts and money (fifth of six)

Concerns: SA-C-115, SA-C-116, SA-C-117, SA-C-118, SA-C-119, SA-C-120, SA-C-121, SA-C-122, SA-C-123, SA-C-124, SA-C-126. Four capabilities added, CM-PAY-029 to CM-PAY-032; seven concerns land in existing capabilities (one of them, SA-C-122, in ORD's CM-ORD-006), four in the new ones. Every capability was first searched in every domain with `caps` (terms: cash on delivery, الدفع عند الاستلام, COD, bank transfer, التحويل البنكي, سريع, sarie, payment link, رابط الدفع, checkout link, send invoice, quick payment, الدفع السريع, settlement, settlements, تسوية, التسويات, dropshipping, drop shipping, wallet, المحفظة, balance, الرصيد, app billing, app charges, usage charge, withhold, fraud, الاحتيال, risk, sift, عميل غير جاد, loyalty, points, مكافأة, الراجحي, reward, الولاء, نقاط). What it found and kept apart: B's CM-CAT-010 (sourcing by dropshipping apps), F's CM-APP-003 (the platform bills the merchant for an app) and CM-PTN-003 (partner payouts), A's CM-PLN-006 (the store balance) and CM-TRU-008, D's CM-CUS-006, CM-LOY-001 and CM-LOY-004, C's CM-ORD-008 (order invoices), CM-CHK-008 (quick checkout) and CM-PAY-004 (the processors' settlement). Both platforms' cells are written for the four new capabilities.

### Where each concern landed, and the grains

- **SA-C-115 and SA-C-116 in a new CM-PAY-029, cash on delivery; SA-C-117 in a new CM-PAY-030, bank transfer; both children of CM-PAY-016** (M-033). A Q1 match with several concerns on one side is a difference of grain, and Salla gives each method a place of its own: cash on delivery its setting shipping/shipping.cod (SA-S-1765) and its plan lines الدفع عند الاستلام and تعيين شروط الدفع عند الاستلام; bank transfer its plan lines التحويل البنكي and نظام المدفوعات الفورية عبر سريع and its staff permission bank_accounts_management. **SA-C-115 and SA-C-116 share one capability:** Q1 splits them by who collects, and that split is what the placements show (core: Salla transfers the balance from its labels' carriers, SA-S-0122; outside: "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام", SA-S-0120, settled between merchant and carrier, SA-S-0121). Neither gives cash on delivery through the platform's labels a place apart from cash on delivery as such. Shopify's cells cite only SH-S-0322, which names COD and bank transfers among the manual methods, so both are not-stated.
- **SA-C-118 in CM-PAY-015** (M-031) and **SA-C-123 in CM-PAY-020** (M-034), whose Salla cells batches 4 and 5 wrote from these concerns' keys; nothing was left uncited.
- **SA-C-119 in CM-PAY-012, digital wallets** (M-032), not CM-PAY-013. It is coarser than PayPal: PayPal (CM-PAY-013), stc pay direct (CM-PAY-012) and Mokafaa Al Rajhi. A match landing in the parent of its other side's capability passes the checker's family rule. **Mokafaa Al Rajhi** (مكافأة الراجحي, its plan line SA-S-1966 and released flag SA-S-3140) is cited as core in CM-PAY-001. It is a payment method in Salla's payment group (aldfaa), and no statement calls it a wallet. It isn't D's loyalty programme: D's notes keep it apart as a payment method under "Reward". That it pays with loyalty points rests only on the inventory identifier mokafaa_alrajhi_loyalty (SA-I-1697), a reading.
- **SA-C-120 in CM-PAY-011** (M-025). I added its seven unreleased gateway flags (bayan-pay, qpay, benefit, omannet, iyzico, my-fatoorah, paylink) as shows, and SA-S-0099 under responsible as outside.
- **SA-C-121 in CM-PAY-019**, by role, as SH-C-083's landing joined it (U-022).
- **SA-C-122 in CM-ORD-006**, by role, as the coordinator directed if it is the same thing. Both flag orders for the merchant's decision: Shopify's analysis lets the merchant review orders before fulfilling (SH-S-0747); Salla's system asks the merchant to confirm carrying out a suspicious order and makes the merchant answer for the cardholder's complaint (SA-S-5051). Added to CM-ORD-006's Salla cell: the released flag sift (core); the plan line قيود الدفع والحماية من الاحتيال under SA-C-122's key (core; batch 4 cites it core in CM-PAY-019 under SA-C-121's key, since the one plan line names both); and, as shows, SA-S-0104 (fraud protection among Salla Payments' shopping-experience services), SA-S-5052 (the tag عميل غير جاد from Salla's AI anti-fraud analysis across its stores) and SA-S-5053 (its reason). CM-ORD-006 has no PAY capability of its own for fraud, so SA-S-1971 counts once.
- **SA-C-124 in a new CM-PAY-031,** amounts withheld from the merchant's wallet for app partners. It has a place of its own: the API folder Settlements and the scope settlements (إدارة المبالغ المحجوزة). Its API statements say apps do the work (SA-S-0178, SA-S-0179), so they are extension-point. Salla's own transfer under the policy the merchant accepts on installing (SA-S-5054) is core. The capability also cites, as core, SA-C-145's managed settlement for shipping apps (SA-S-5065, SA-S-5066: Salla withholds the labels' amounts from the wallet balance and settles with the carrier). That is a join on role within Salla, a reading. SA-C-145 lands in a later SHP batch, and that batch should read its landing as strained if it lands outside CM-PAY-031. No parent, since the wallet itself is A's CM-PLN-006.
- **SA-C-126 in a new CM-PAY-032,** payment links, under CM-ORD-001. Salla sends the link from the order's actions (SA-S-5143), and its plan line sits in the payment group (SA-S-1968). I chose the parent from the admin place, a reading. Shopify's cell is none-held.

### Joins on role (readings)

- **SA-C-122 in CM-ORD-006** (above): SH-C-059/where/SH-S-0747 against SA-C-122/decides/SA-S-1971 and SA-C-122/responsible/SA-S-5051.
- **SA-C-121 in CM-PAY-019:** SH-C-083/where/SH-S-0589 against SA-C-121/reason/SA-S-5050, as batch 4 read it.
- **Within Salla, CM-PAY-031:** the dropshipping apps' settlements (SA-C-124) and the shipping apps' managed settlement (SA-C-145) are one role: an app's amounts are withheld from the merchant's wallet and settled by Salla.

### Homonyms

- **"Settlement" (تسوية):** Salla's settlements for app partners (CM-PAY-031, SA-S-0178, SA-S-5066) against the processors' settlement of transactions (CM-PAY-004; Shopify SH-S-0082, Salla SA-S-0081, SA-S-0088), cash on delivery settled between merchant and carrier (SA-S-0121, CM-PAY-029), payout settlement times (SH-S-0340) and the MoR's settlements (SA-S-5129, not cited).
- **"Withhold":** an app's amounts withheld from the merchant's wallet (CM-PAY-031) against reserves held back from payouts (CM-PAY-006, Salla none-held; the checker lists SA-S-1564 as a candidate there), Shopify withholding payments to Partners (SH-S-0758, SH-S-0759, F) and the merchant's tax withholding.
- **"Bank account":** the account shown to customers for bank transfers (CM-PAY-030, SA-S-0095) against the payout account tied to store verification (CM-PAY-005, SA-C-112).
- **"Cash on delivery balance":** the wallet's cash-on-delivery summary (SA-S-0106) against the e-payments balance (CM-PAY-005).
- **"Quick payment" (الدفع السريع (المباشر), quick_payment_direct):** a permission in Salla Point's group, held in SA-C-126. It is shows in CM-PAY-032, since no statement says it sends payment links. It isn't the quick checkout of CM-CHK-008 (الشراء السريع).
- **"Invoice":** Shopify's draft-order invoices (SH-S-7225) against a payment link. No statement says the invoice holds a link to pay.

### Strained fits

- **SA-C-121 in CM-PAY-019:** its plan line SA-S-2145, held also by SA-C-122, is cited in CM-ORD-006.
- **SA-C-122 in CM-ORD-006:** SA-S-0104 is cited in CM-PAY-007 and CM-PAY-014 (under SA-C-113), SA-S-2145 in CM-PAY-019 and SA-S-5052 in D's CM-CUS-006. Salla's plan puts the system in its payment group; Shopify's help puts it under orders.
- **SA-C-124 in CM-PAY-031:** its category, endpoint and policy (SA-S-1193, SA-S-0179, SA-S-5054) are cited in B's CM-CAT-010.

### Statements shared with other domains

- **SA-S-5052 (عميل غير جاد), for the coordinator:** it is shows in D's CM-CUS-006 and now shows in CM-ORD-006, under SA-C-122's key. It names Salla's AI anti-fraud system analysing customer data across Salla's stores, so it is a lead for A's CM-TRU-008, the platform's use of customer data across merchants. Citing it there is the coordinator's to do; I haven't.
- SA-C-124's SA-S-1193 and SA-S-0179 are extension-point in B's CM-CAT-010 and here. SA-S-5054 is shows there and core here, and only core here, so the merge's two-domain test isn't met.
- SA-S-1564 (the scope settlements) is held also by SA-C-191 (domain F, app scopes). It is cited here under SA-C-124's key.

### Rulings

- **U-021 (SH-C-059 against SA-C-122): `joined:CM-ORD-006`.** **U-022 (SH-C-083 against SA-C-121): `joined:CM-PAY-019`.** **U-023 (SH-C-078 against SA-C-119): `joined:CM-PAY-012`,** completing the candidate with batch 6's row.
- **U-018 (SH-C-055 against SA-C-126): `apart`.** No Shopify statement held names a payment link. The pair against SA-C-040 is batch 2's `joined:CM-ORD-005`.
- **U-043 (SH-C-182 against SA-C-118 and SA-C-119): `apart`,** two rows. scope.tsv gives SH-C-182 domain A with no also.
- **U-016 (SH-C-141 and SH-C-185 against SA-C-124): `apart`,** two rows. scope.tsv gives SH-C-141 domain E and SH-C-185 domain B, neither naming C. The pairs against SA-C-098 are domain D's.

### Left for batch 8

- **U-028 (SH-C-069 against SA-C-164), U-038 (SH-C-173 against SA-C-172), U-064 and M-077 (SA-C-210), U-027's pairs against SA-C-177, M-038 (SA-C-128):** as batches 3, 5 and 6 left them.
- **SA-C-127 (charity stores' gateways):** CM-PAY-011's Salla cell now holds every SA-C-120 flag. SA-S-0206 and SA-S-5057 (Apple Pay for charities) are still uncited and may go in CM-PAY-011 or CM-PAY-012.

### For the coordinator, on earlier rows

- **CM-PAY-016's Salla cell** cites SA-C-115's, SA-C-116's and SA-C-117's keys from before its children existed. Its qualities (the 1000 SAR maximum and the 20 SAR minimum) and its slot filler SARIE (سريع) now also sit on CM-PAY-029 and CM-PAY-030. To count each once, the parent's copies could go, and its reading could name the children.
- **CM-PAY-009, Salla none-held:** SA-C-122's SA-S-5051 says "قد يُخصم مبلغ العملية من حسابك إذا ثبتت صحة الشكوى", which bears on a cardholder's dispute. I left it in CM-ORD-006 rather than rewrite batch 4's none-held cell.
- **CM-PAY-013's note** says SA-C-119 lands in a Salla batch; it landed in the parent CM-PAY-012. **CM-ORD-006's Salla reading** says SA-S-5052 "is not cited here"; it now is, as shows. **CM-PAY-011's Salla reading** says SA-C-120's other flags are left; they are now cited.
- No earlier row was found wrong.

### Gaps

- SA-C-115 responsible (who holds the cash-on-delivery amounts collected through Salla's labels before payout), SA-C-116 reason, SA-C-117 responsible and reason, SA-C-118, SA-C-119 and SA-C-120 reason, SA-C-121 responsible, SA-C-123 responsible and reason, SA-C-126 responsible and reason: all "page not read".
- No statement says which wallet Salla's settlements are withheld from (CM-PAY-031), nor what quick_payment_direct does (CM-PAY-032).
- No Shopify statement held names a payment link (CM-PAY-032) or a settlement for app partners (CM-PAY-031), and none gives cash on delivery or bank transfer a place of its own (CM-PAY-029, CM-PAY-030, not-stated).

### Qualities

- CM-PAY-029 Salla: the 1000 SAR maximum with Salla's labels (SA-S-0123) and the 20 SAR minimum cart (SA-S-0125), copied from CM-PAY-016 (above).

### Checker

The batch check (`--concerns` for the batch's eleven concerns, `--areas PAY`) gives "0 problems, 42 flags for the reviewer". The flags on CHK, ORD and the own-service rows are earlier batches', answered in their sections. Mine:
- **CM-PAY-031 Shopify, none-held, 36 matches:** processor settlement, payouts, chargebacks, Partner payouts, tax withholding, suppliers, Dropshipping apps and Shopify Collective. All are answered in the cell's reading.
- **CM-PAY-032 Shopify, none-held, 1 match (SH-S-7225):** "send invoices" with draft orders, which isn't stated to carry a link to pay. It is answered in the cell's reading and in U-018.
- **CM-PAY-006 Salla, none-held, lists SA-C-124/boundary/SA-S-1564:** the settlements scope, an app partner's hold, not the payment service's reserve (Homonyms).
`uncited --domain C` lists none of this batch's concerns' statements.

## The coordinator's corrections after batch 7 (30 October)

- **CM-PAY-016's copies** of its children's cash-on-delivery qualities and SARIE slot filler are removed; CM-PAY-029 and -030 hold them.
- **CM-PAY-009's Salla cell** holds SA-S-5051: the merchant answers for a card owner's complaint, and the amount may be deducted from its account if the complaint is proven. Salla's own service carries the chargeback, `core`, a reading.
- **Three readings** name batch 7's rows: Salla's CM-ORD-006 and CM-PAY-011, and CM-PAY-013's note.
- **SA-S-5052** is cited as `core` in A's CM-TRU-008, network protection across stores; SA-C-122 names A under `also`.


## Batch 8: PAY, Payments, payouts and money (last of six)

Concerns: SA-C-127, SA-C-128, SA-C-164, SA-C-172, SA-C-177, SA-C-210. No capability added: all six land in existing ones. Before landing each where no capability yet named it, I searched every domain with `caps` (terms: charity, خيرية, جمعية خيرية, الجمعيات الخيرية, donation, تبرع, التبرعات, nonprofit, selling policy, سياسة البيع, selling-policies, payment services contract, عقد خدمات الدفع; currency, عملة, العملة, عملات, العملات, payout currency, settlement currency; partial payment, partially paid, deposit, دفع جزئي, الدفع الجزئي, عربون). What it found and kept apart: A's CM-ACC-004 (a charity, جمعية خيرية, as the store's entity type), B's CM-SEL-007 (donations), E's CM-MKS-005 to -007 (store currency, prices in the buyer's currency, conversion). None is the same thing as a concern here.

### Where each concern landed, and the grains

- **SA-C-127 (charity stores' gateways) in CM-PAY-011,** `single`. Q1 split it from Salla Payments because Salla's help routes charity stores to gateways such as Moyasar and PayTabs. It has no link, route, API group, plan line or app category of its own: the payments namespace's text for charity stores (SA-S-0206, core, a reading: the dashboard's own text points them to the available gateways), an unreleased flag e-payment-charity (SA-S-3300, shows) and Moyasar's secret key (SA-S-5056, shows, as SA-S-0205 is). A store type doesn't set a capability, so charity stores are its scope, not a child. Its reason, Apple Pay for charities (SA-S-5057), is shows in CM-PAY-012, as batches 6 and 7 suggested; both capabilities are under CM-PAY-001, so the fit is clean. Moyasar is already CM-PAY-011's Salla slot filler (SA-S-0069), so SA-S-5056 adds none.
- **SA-C-128 in CM-PAY-026** by `match:M-038`, and **SA-C-210 in CM-PAY-028** by `match:M-077`. Batches 5 and 6 had cited every statement of both; I added no evidence.
- **SA-C-164 (the currency Salla Payments settles in) in CM-PAY-005,** payouts, by role (a reading): Shopify's payout currency, which Multi-Currency Payouts varies on some plans (SH-S-0365), and Salla's "يتم استقبال جميع المدفوعات بالريال السعودي" under its transfer cycle (SA-S-0067) are the currency of the service's payouts. Not a child: neither platform gives the currency a place of its own in what is held (SA-C-164's where is a Q1 gap, page not read; Shopify's payout currencies are help-centre titles in SH-C-069, SH-I-2238, SH-I-2240, SH-I-2243, still uncited). SA-S-0067 is core and a quality; SA-S-0135 and SA-S-0139, core in the cell under SA-C-112's keys, are shows under SA-C-164's. Not E's CM-MKS-007: no conversion or rate is stated, as E-anchor read it.
- **SA-C-172 (the selling policy accepted when activating e-payments) in CM-PAY-002,** `single`, a reading: it is a condition of activating the platform's own service, so it lands in the service, as batch 6 landed Shopify's prohibited businesses (SH-C-173). Its keys SA-S-0068 and the sitemap entry SA-S-2212 are shows. I claim no join on role with SH-C-173: the policy's text isn't held (Q1's gaps: decides, responsible and reason, page not read), so what it sets can't be compared.
- **SA-C-177 (the payment services contract) in CM-PAY-004,** by role, as SA-C-114's landing joined it: settlement "under the payment services contract" (SA-S-0081, SA-S-0088) against Shopify's processing and settlement by Payment Processors (SH-S-0082). Its fee sentence SA-S-0082 is shows in CM-PAY-007, a sibling under CM-PAY-002. CM-PAY-004's Salla cell stays not-stated: the contract's text, parties and licence are all Q1 gaps (page not read).

### Joins on role (readings)

- **SA-C-164 in CM-PAY-005:** SH-C-069/decides/SH-S-0365 against SA-C-164/decides/SA-S-0067.
- **SA-C-177 in CM-PAY-004:** SH-C-064/where/SH-S-0082 against SA-C-177/decides/SA-S-0081 and SA-S-0088.

### Homonyms

- **"Policy" (سياسة):** Salla's selling policy for e-payments (سياسة البيع, CM-PAY-002) against the store's own policies for its buyers, and Salla's partner and app policies (SA-S-5054, CM-PAY-031). Not cited together.
- **"Charity" (خيرية):** charity stores' payment gateways (CM-PAY-011) against a charity as the store's legal entity type (A's CM-ACC-004) and donations to a cause (B's CM-SEL-007).
- **"Currency" (العملة):** the currency payments are settled and paid out in (CM-PAY-005) against the store's currency and the buyer's display currency (E's CM-MKS-005, CM-MKS-006).

### Strained fits

None of mine. The checker reads all six landings as clean.

### Statements shared with other domains

- SA-C-164 names E under also, and SA-C-172 names A. Neither is cited in E or A; A-woocommerce and E-anchor rule their pairs against them `apart`.

### Rulings

- **U-027 (SH-C-065, SH-C-066 and SH-C-067 against SA-C-177): `joined:CM-PAY-004`,** three rows, completing the candidate with batch 6's three against SA-C-114. They follow the cells; the candidate's question, which licensed entity holds Salla's funds, isn't answered by any statement held.
- **U-028 (SH-C-069 against SA-C-164): `joined:CM-PAY-005`.** **SH-C-109 against SA-C-164: `apart`.** scope.tsv gives SH-C-109 domain E, which names C under also, but no capability here cites its keys. E-anchor's ruling on the same pair is also `apart`.
- **U-038 (SH-C-173 against SA-C-172): `joined:CM-PAY-002`.** This follows the cells, as batch 6 foresaw. Whether the selling policy restricts the same businesses isn't settled, because its text isn't held.
- **U-064 (SH-C-191 against SA-C-210): `joined:CM-PAY-028`;** **SH-C-196 against SA-C-210: `apart`,** because scope.tsv gives SH-C-196 domain A, with no also.

### Left for later batches (TAX, SHP, RET)

- **SA-C-145** (shipping apps' managed settlement), whose SA-S-5065 and SA-S-5066 CM-PAY-031 cites as core: SHP lands it, and should read its landing as strained if it lands outside CM-PAY-031 (batch 7).
- **Apple Wallet order tracking** (SA-S-1995, SA-C-040's plan line), for SHP, from batch 2.

### For the coordinator: PAY is complete

**Earlier `single` landings that can now be written as Q1's matches:** every other side of these matches has landed.
- SH-C-062 (CM-PAY-001) and SH-C-076 (CM-PAY-011) as `match:M-025` (SA-C-120 is in CM-PAY-011, and CM-PAY-001 is its parent).
- SH-C-075 (CM-PAY-015) as `match:M-031` (SA-C-118).
- SH-C-077 (CM-PAY-013) as `match:M-032` (SA-C-119, in the parent CM-PAY-012).
- SH-C-079 (CM-PAY-016) as `match:M-033` (SA-C-115 and SA-C-116 are in its child CM-PAY-029, SA-C-117 in CM-PAY-030).
- SH-C-084 (CM-PAY-020) as `match:M-034` (SA-C-123).
- SH-C-091 to SH-C-097 (CM-PAY-026) as `match:M-038` (SA-C-128).
- SH-C-191 (CM-PAY-028) as `match:M-077` (SA-C-210).

M-028 (SH-C-070), M-030 (SH-C-072), M-035 (SH-C-085), M-036 (SH-C-086), M-037 (SH-C-064) and M-085 (SH-C-173) have no Salla side: they stay `single` for the WooCommerce part. Each of these landings' readings says its join "is single until" a later batch, and should be rewritten with it.

**Readings my rows make out of date:**
- **CM-PAY-026 Salla:** "SA-C-128 lands in a later batch (M-038)". **CM-PAY-028 Salla:** "SA-C-210 lands in a later batch (M-077)".
- **CM-PAY-011 Salla:** it says SA-C-127's charity gateways (SA-S-0206) are left. They are now cited: core SA-S-0206; shows SA-S-3300 and SA-S-5056.
- **CM-PAY-012 Salla:** it now also holds SA-S-5057 as shows, the reason charities find Apple Pay hard to activate.
- **CM-PAY-005 Salla:** it now holds SA-S-0067 as core (all payments received in riyals) and as a quality, with SA-S-0135 and SA-S-0139 as shows under SA-C-164.
- **CM-PAY-002 Salla:** it now holds SA-C-172's SA-S-0068 and SA-S-2212 as shows. Its sentence that the wallets in SA-C-110 "are left to the batch that lands them" was already out of date after batch 6.
- **CM-PAY-004 Salla:** it now holds SA-C-177's keys for SA-S-0081 and SA-S-0088. **CM-PAY-007 Salla:** SA-C-177's key for SA-S-0082.
- **Rulings U-023 (the row against SA-C-110) and U-027 (the row for SH-C-065 against SA-C-114):** each says a pair is left to a later batch. Both are now ruled.
- **Already stale from earlier batches:**
  - CM-PAY-001 Salla: "SA-C-110 itself is a later batch's to land".
  - CM-PAY-013 Salla: "SA-C-119 lands in a Salla batch". It landed in CM-PAY-012.
  - CM-PAY-006 Salla: it calls SA-C-124 "a later batch's concern". It is in CM-PAY-031.
  - CM-PAY-022 Salla: "left to the Salla batches for CM-PAY-014".
  - CM-PAY-016's note: "The Salla batches may add children". They are CM-PAY-029 and -030.

**Still uncited:**
- **Partial payments** (SA-C-040's released flag partial-payments, SA-S-3286, plans plus, pro and special), left to PAY by batch 2. No PAY concern of Salla's holds it, and no statement defines it: a search for partial, جزئي, جزئية, الدفع الجزئي, دفعة مقدمة and عربون finds only the flag and its inventory entry SA-I-2286. One flag isn't a capability (the dry run's rule), and its name alone doesn't show which capability it is: CM-PAY-008 (payment terms) and CM-PAY-020 (an order's payment transactions) are both possible. I leave it uncited for the coordinator, a gap.
- **Shopify's payout-currency help titles** (SH-I-2238, SH-I-2240, SH-I-2243, SH-C-069's), which CM-PAY-005's Shopify cell could cite as shows.

No earlier row was found wrong, and the checker prints no problem on earlier batches' rows.

### Gaps

- SA-C-127: responsible (page not read). SA-C-128: reason (page not read). SA-C-164: where, responsible and reason (page not read), and boundary (observation needed, the settlement statement of a store with Salla Payments). SA-C-172: decides, responsible and reason (page not read), so the selling policy's text isn't held. SA-C-177: all four placements (page not read), so the payment services contract's parties, licence and custody aren't held. SA-C-210: responsible (stated only in general terms), reason (page not read).
- No statement held says what Salla's partial-payments flag does (above).

### Qualities

- CM-PAY-005 Salla: the currency Salla Payments receives payments in, the Saudi riyal (SA-S-0067).

### Checker

The batch check (`--concerns SA-C-127,SA-C-128,SA-C-164,SA-C-172,SA-C-177,SA-C-210 --areas PAY`) gives "0 problems, 42 flags for the reviewer", the same 42 that batch 7 answered. None is on this batch's rows. `uncited --domain C` lists none of this batch's concerns' statements. As the last batch of PAY, but not of the part (TAX, SHP and RET follow), I ran the batch check, not the whole-part check.


## Batch 9: TAX, Taxes, duties and invoicing

Concerns: SH-C-099, SH-C-100, SH-C-101, SH-C-102, SH-C-103, SH-C-104, SH-C-105, SA-C-160, SA-C-161, SA-C-162. TAX had no capability before this batch: nine added, CM-TAX-001 to CM-TAX-009, and every concern lands in one of them. Before adding them I searched every domain with `caps` (terms: tax, ضريبة, ضرائب, VAT, duties, zatca, الزكاة, 1099, tax form, tax document, e-invoic, فوترة, الفوترة الإلكترونية, customs, جمارك, الجمارك, import tax, exemption, إعفاء, tax registration, registration, filing, tax return, tax app, Avalara, هيئة الزكاة, الرقم الضريبي, VAT number, reverse charge, tax-inclusive, duty, import). What it found and kept apart: A's CM-PLN-007 (taxes on the platform's own charges, with Shopify's "Tax registration" for its bills, SH-S-0279) and CM-PLN-004, -006; C's CM-ORD-008 (order invoices); E's CM-MKS-003 (merchant of record, Managed Markets, which handles duties and taxes for the store); B's CM-CAT-013 (product pricing, whose reading leaves Salla's product tax pricing, SA-S-1752, to C); and words matched inside other words (taxonomy, customs in "custom", import in data import). None is the same thing as a concern here.

### Where each concern landed, and the grains

- **CM-TAX-001, taxes on the store's sales, the parent of the area:** SH-C-100 and SA-C-160 by `match:M-040`. Both platforms put the area's other subjects under one tax section: Shopify's Taxes and duties, whose routes add, ioss, vat-number-validation, providers and duties are paths of the Taxes section (SH-S-7124 to SH-S-7129), and Salla's one settings link Taxes at /taxes-and-duties (SA-S-1686). SH-C-100 lands in the parent because it holds both the store's tax settings and default rates and Shopify Tax.
- **CM-TAX-002, the platform's automated tax calculation service (Shopify Tax), a child,** at the grain WooCommerce's own split shows (M-040's granularity: WC-C-054 against WC-C-055). Shopify gives it a plan line, an entitlement, built-in-feature pages and its own terms. Salla's cell is none-held: its rates are entered by the merchant (SA-S-0144, SA-S-0182).
- **CM-TAX-003, tax registrations, a child:** SH-C-101, `single`. Salla's cell cites SA-C-160's keys (the tax-number plan line SA-S-2125 and the ZATCA registration terms SA-S-5073), so U-030's pair is joined here.
- **CM-TAX-004, third-party tax services, a child:** SH-C-103, `single`. Salla's cell holds only the unreleased flag avalara-tax (SA-S-3511): not-stated.
- **CM-TAX-005, VAT number validation, tax exemptions and VAT invoices, a child:** SH-C-102, `single` (Q1's M-041 is with WooCommerce only). One capability at Shopify's grain: its plan line "VAT validation, exemptions, and invoicing" holds the three, and its help centre groups VAT validation and VAT invoices under Shopify Tax's EU and UK features. Shopify's VAT invoices are held only as a help-centre title (SH-I-2331), so I didn't cite them in CM-ORD-008: nothing held says they are the order invoice, and CM-ORD-008's cells are unchanged. This answers batch 1's note that SH-I-2331 and ZATCA e-invoicing were TAX's.
- **CM-TAX-006, automated tax filing, under CM-TAX-002:** SH-C-104, `single`. Shopify calls it "Automated filing with Shopify Tax", available only to US stores that use Shopify Tax (SH-S-0522). Its route and built-in feature are core, and the returns are filed by Sovos Compliance, LLC, the Tax Service Provider (outside, a slot filler). It is closed to new enrollment and ends with sales through December 31, 2026 (qualities).
- **CM-TAX-007, e-invoicing with the tax authority:** SA-C-161, `single`. No parent: no statement held puts it under Salla's tax settings or its invoice settings. The plan line's parent_code mhfth-almtgr-oalfotr has no title held, and reading it as a word would be inference. It is installed as an app, and its flag has the type app, but no statement names the app's maker (a gap). The cell is core on the Pro plan line, the released flag, and SA-S-0148 and SA-S-0152, which name Salla as the one that uploads and manages the invoices.
- **CM-TAX-008, duties and import taxes on cross-border orders, a child:** SH-C-105 and SA-C-162 by `match:M-042`. It is under CM-TAX-001 by both platforms' grouping (Shopify's Taxes section, path duties; Salla's /taxes-and-duties).
- **CM-TAX-009, tax forms the platform issues to the merchant:** SH-C-099, `single` (Q1's M-039 is with WooCommerce only). These are Shopify's 1099-K and 1099-MISC forms. Its routes are in the admin section Banking (CM-PAY-023), but no statement puts the forms under it, so I gave it no parent. The 1099-K is filed by Shopify Payments as a Payment Settlement Entity (SH-S-0502, SH-S-0505). Salla's cell is none-held.

### Joins on role (readings)

- **CM-TAX-003:** Shopify's tax registration number and registration routes (SH-C-101/decides/SH-S-0533, SH-C-101/where/SH-S-7124) against Salla's tax number, الرقم الضريبي, in its plan line, and its ZATCA registration terms (SA-C-160/decides/SA-S-2125, SA-C-160/responsible/SA-S-5073). Both are the store's registration with the authority whose tax it collects. Salla's "سجل ضريبي" (SA-S-0144) is a market's tax record, its rate, not a registration.

### Homonyms

- **"Tax registration":** the store's registrations to collect tax (CM-TAX-003) against Shopify's Tax registration section for the merchant's tax ID on Shopify's own bills (SH-S-0279, A's CM-PLN-007).
- **"Invoice" (فاتورة):** VAT invoices under Shopify Tax (CM-TAX-005), the store's tax invoices reported to ZATCA (CM-TAX-007), the order's invoice as the store issues and prints it (CM-ORD-008), and the platform's invoices to the merchant (A's CM-PLN-004). Shopify Tax's fee "is charged to you with your subscription invoice" (SH-S-0517) is the last of these, cited as shows in CM-TAX-002.
- **"سجل ضريبي" (tax record):** Salla's per-market tax rate (CM-TAX-001), not a tax registration (CM-TAX-003).
- **"Filing" and "reporting":** Shopify's filing of sales tax returns (CM-TAX-006) against its 1099-K reporting of the merchant's receipts (CM-TAX-009) and Salla's reporting of invoices to ZATCA (CM-TAX-007).

### Strained fits

None. The keys of a concern that are cited outside the capability it lands in are all in the same tree, under CM-TAX-001: SA-C-160's in CM-TAX-003 and -004, SH-C-100's in -002 and -004, SH-C-101's in -001 and -002, SH-C-103's in -001 and -002, and SH-C-105's SH-S-0564 in -003. CM-TAX-007 and CM-TAX-009, which have no parent, cite only their own concerns.

### Statements shared with other domains

- **SH-S-0527** (SH-C-137, domain E, which names C under also): marketplace facilitators collect and remit sales tax on marketplace sales, a heading of Shopify's automated filing. It is shows in CM-TAX-006.
- **SH-S-0564** (Global-e provides the tax registration under Managed Markets) is outside in CM-TAX-003, under SH-C-101's and SH-C-105's keys. E's CM-MKS-003 cites it as outside under SH-C-110's key. Neither is core, so the merge won't flag it.
- **SH-S-6130 to SH-S-6134, SH-S-6298 and SH-S-6299** are also held under F's SH-C-158 and SH-C-159 (access scopes). Here they are cited under SH-C-100's and SH-C-103's keys, as core (read_taxes, TaxSettings, TaxAppConfiguration) and extension-point (write_taxes for "a tax calculations app", the tax_services webhooks). F's parts may cite the same statements as core for the scopes mechanism.

### Rulings

- **U-030: SH-C-101 against SA-C-160, `joined:CM-TAX-003`,** on role (above). **SH-C-103 against SA-C-160, `joined:CM-TAX-004`.** This follows the cells: Salla's side is the unreleased flag avalara-tax, so whether Salla offers a third-party tax service isn't settled.
- **U-031: SH-C-102 against SA-C-161, `apart`; SH-C-104 against SA-C-161, `apart`.** No capability cites both sides. Shopify's VAT invoices are only a title, and a filed return isn't an invoice reported one by one. A join on role, "the platform sends the store's tax data to the authority", is possible for SH-C-104, but neither platform's words name the other's object, so I didn't make one.

### Left for later batches (SHP, RET)

- **SA-C-146** (International Shipping Readiness: HS codes, customs; C, with E under also) is SHP's. Q1's M-042 notes that WooCommerce's WC-C-058 also holds product customs data, which Salla keeps in SA-C-146. SHP should land the customs data for a shipment there, not in CM-TAX-008.
- **SA-S-5075:** customs fees on Salla's own labels (بوليصات سلة), settled from the wallet. It is core in CM-TAX-008 under SA-C-162's key. SHP's capability for the platform's own shipping labels may also cite it, as shows.
- No unclear candidate of this batch has a side in SHP or RET.

### Flags answered

The batch check prints 46 flags: batch 8's 42, and four on this batch's none-held cells.
- **CM-TAX-002 Salla (4 matches):** SA-S-2125, SA-S-0182 and SA-I-2511/SA-S-3511 are the merchant-entered rates and the unreleased Avalara flag, cited in CM-TAX-001 and CM-TAX-004. None says Salla computes the rates.
- **CM-TAX-005 Salla (3):** the store's own tax number on its invoices (SA-S-2125, SA-S-0147) and its invoices uploaded to ZATCA (SA-S-0148). None is a buyer's VAT number or an exemption.
- **CM-TAX-006 Salla (4):** acknowledgements (الإقرار) of terms and policies, not tax returns.
- **CM-TAX-007 Shopify (8):** filing and reporting to tax authorities (SH-S-0504, SH-S-0096, CM-TAX-009; SH-S-0606, CM-TAX-006), registration (SH-S-0507, CM-TAX-003), Managed Markets' reason (SH-S-0634, E's SH-C-110: selling without registering for tax), and Saudi VAT on Shopify's own bills (SH-S-0277, SH-S-0278, SH-I-2355, A's CM-PLN-007). None reports the store's invoices to an authority.

### Gaps

- SH-C-101: boundary and reason, searched, not found, so no API or webhook for tax registrations is held. SH-C-102, SH-C-103 and SH-C-104: reason, searched, not found.
- SA-C-160: reason, page not read. SA-C-161: responsible, page not read (the usage agreement on the ZATCA link). SA-C-162: responsible, page not read (Salla's shipping terms), so whether the buyer is charged duties at checkout isn't held.
- Maker statements are missing for Salla's ZATCA app (CM-TAX-007) and for Shopify's Advanced tax platform add-on (CM-TAX-004, billed as Avalara add-on fees, SH-I-1325). No statement held says what the 1099-MISC reports (CM-TAX-009).
- Avalara and Vertex appear only as the names of a billing charge category and help-centre titles (SH-I-1325, SH-I-2342, SH-I-2343), so I recorded neither as a slot filler.

### Qualities and slot fillers

- **Qualities:** CM-TAX-002 Shopify has two: no guarantee of Shopify Tax's uptime (SH-S-0598), and the destinations it calculates for (SH-S-0514). CM-TAX-006 Shopify has two: the end of automated filing (SH-S-0525) and its closure to new enrollment (SH-S-0521). CM-TAX-003 Salla has one: ZATCA's registration threshold of 375,000 riyals a year (SA-S-5073).
- **Slot fillers:** Global-e (CM-TAX-003, scope Managed Markets); ZATCA, هيئة الزكاة والضريبة والجمارك (CM-TAX-003 and CM-TAX-007, Salla); Sovos Compliance, LLC (CM-TAX-006); customs authorities (CM-TAX-008); the IRS and the US tax laws on Payment Settlement Entities (CM-TAX-009, scope United States).

### For the coordinator

No row of an earlier batch is wrong by this batch's evidence. Batch 1's note (line 100) that ZATCA e-invoicing and SH-I-2331 are TAX's is now answered: CM-TAX-007 and CM-TAX-005. CM-CHK-009's Shopify reading, which names SH-S-0670 as TAX's, still holds: SH-S-0670 is core in CM-TAX-005.

### Checker

The batch check (`--concerns SH-C-099,SH-C-100,SH-C-101,SH-C-102,SH-C-103,SH-C-104,SH-C-105,SA-C-160,SA-C-161,SA-C-162 --areas TAX`) gives "0 problems, 46 flags for the reviewer". The four new flags are answered above. `uncited --domain C` lists none of this batch's concerns' statements.
