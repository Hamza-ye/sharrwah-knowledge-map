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
