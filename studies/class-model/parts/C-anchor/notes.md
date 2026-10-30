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

