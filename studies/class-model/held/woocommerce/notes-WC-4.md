# Notes: held pass, WooCommerce, batch WC-4 (`options`, end; `payments-providers`, start)

**What the batch holds:** 80 entries.
- **50 of `options`:** the rest of the store's options table, rows `woocommerce_shipping_cost_requires_address` to `woocommerce_woocommerce_payments_wechat_pay_settings` (other-product-class@0d79b794f:woocommerce/raw/runs/20261029T023745Z-db-after-country-change/options.tsv, by the selection's rule `^(woocommerce|wcpay|wc_|_wc)`).
- **30 of `payments-providers`:** items.jsonl lines 1 to 4 (AE, EG, GB, and JP's three providers), other-product-class@0d79b794f:woocommerce/structures/payments-providers/items.jsonl. Each item is the answer of `POST /wp-json/wc-admin/settings/payments/providers {"location": <code>}` in run 20261029T023051Z-country-change-en (its `meta.json`).

**The batches beside this one.**
- `options`: I read WC-3's placements and its notes to the end, "The coordinator's check" included, and kept to them where the things are the same. The table below says where each kind of setting went.
- `payments-providers`: no batch placed it before this one. WC-5 holds its other 28 entries (JP's suggestions, then OM, SA, US and YE) and hasn't run, so I read no placements of it. The coordinator aligns the two. WC-5 will meet the same things again: WooPayments' provider, PayPal Payments, the offline group, and Stripe, Square, Airwallex and Visa Acceptance Solutions among the suggestions.
- **WC-1 to WC-3's free extensions:** I kept to their lines where a provider is the same thing.
  - PayPal Payments: CM-PAY-013 and CM-PAY-011, `extension-point`, PayPal the filler (WC-2, with the coordinator's CM-PAY-011 line).
  - WooPayments: CM-PAY-002, `own-service`.
  - WooPayments' methods: as WC-3 places the store's recommended methods (`wcpay_recommended_payment_methods`).

**Count:** 80 entries, 126 lines.
- **By entry:** 76 have `capability` lines, 1 has a `new` line beside its capability line (GoCardless), and 3 are `out`.
- **By line:** 122 `capability`, 1 `new`, 3 `out`.
- **By supports, on the 123 lines that aren't out:** extension-point 50, core 38, own-service 22, shows 13.

## The options (50 entries)

**Read as WC-3 read them.**
- Each option is one store's value of a setting. I read each setting's title and description where the release's settings classes declare it, to clarify the entry only. The release is the one `evidence/product-class/woocommerce-11.2.1/` fixes, unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`.
- Each reading cites `woocommerce-11.2.1:<path>, lines …` and quotes the release exactly.
- The store's value goes in `reading`, never in `quality`. Scope is empty, as in WC-3: the structure has no labels, and every line is the capture's one test store.

| Settings | Capability | Supports |
| --- | --- | --- |
| Shipping settings: hide costs until an address is entered, hide rates when free shipping is available, debug mode | CM-SHP-001 | core |
| Ship to specific countries | CM-SHP-001 core, CM-MKS-001 shows (as WC-3's Shipping location(s)) | |
| Sell to specific countries | CM-MKS-001 | core |
| Store Address: address lines 1 and 2, city, postcode | CM-ACC-006 (as WC-3's Country / State) | core |
| Tax options: calculate based on, shipping tax class, rounding, additional tax classes, the three display settings | CM-TAX-001 | core |
| Shop page, weight unit | CM-CAT-001 (as WC-3's dimensions unit) | core |
| Main image width, thumbnail width (Customizer, Product Images) | CM-CAT-007 (as WC-3's placeholder image) | core |
| Stock notification recipient(s) | CM-INV-004 and CM-NTF-002 (as WC-3's low stock notification) | core |
| Stock display format | CM-INV-001 | core |
| Terms and conditions page | CM-CNT-008 (as WC-3's refund and returns page) and CM-CHK-001 (accepted at checkout) | core |
| Retain pending, failed, cancelled orders | CM-TRU-005 (Personal data retention, as WC-3), and CM-ORD-012 (the orders are trashed) | core |
| Show Suggestions | CM-PAY-001, whose cell cites the same setting (WC-S-5009), and CM-APP-002 (Marketplace suggestions, as WC-3) | core |
| `woocommerce_store_pages_only` | CM-ACC-009, whose cell cites it (WC-S-5421) | core |
| The task list's completed tasks and actions, stored states that name the setup tasks | CM-ONB-004 (as WC-3's profiler progress) | shows |
| Store id, WooCommerce's and WooPayments' versions | out | |

**WooPayments' options (18 entries).**
- **The maker.** The options `woocommerce_woocommerce_payments_*_settings` are the settings of the gateway `woocommerce_payments`. The release keeps a gateway's settings under `'woocommerce_' . id . '_settings'` (`includes/abstracts/abstract-wc-settings-api.php`, line 106). It maps the id `woocommerce_payments` to its WooPayments provider (`src/Internal/Admin/Settings/PaymentsProviders.php`, line 114). WooPayments' maker is the cell's own evidence: 'designed by Woo for Woo' (WC-S-0557, M-1). So the lines are `own-service`.
- **Each method's settings take two lines:**
  - the parent's, on CM-PAY-002: the option names the method as one of WooPayments' gateways (M-6). Entries 33 to 47 share one grouped line; WeChat Pay (50) has its own, since the version (49) sits between them;
  - the method's own line, on its capability, by the cells' own evidence:
    - Affirm, Afterpay / Clearpay and Klarna: CM-PAY-015, `own-service`. The cell holds 'Affirm, Afterpay and Klarna with WooPayments' (S02-WC-318).
    - Bancontact, EPS, iDEAL, GrabPay, Multibanco, p24 and sepa_debit: CM-PAY-017, `own-service`. The cell's chart of WooPayments' local payment methods lists each (S02-WC-321): Bancontact, EPS, GrabPay, iDEAL, Multibanco, Przelewy24 (P24), SEPA Direct Debit, Alipay and WeChat Pay.
    - Alipay and WeChat Pay: CM-PAY-012, `shows`, as WC-3 places them, a digital wallet by the store's recommended methods. They also take CM-PAY-017, `own-service`, since the same chart lists them.
    - Apple Pay and Google Pay: CM-PAY-012, `shows`, as WC-3.
    - `link`: CM-CHK-008, `shows`, read as the Link by Stripe that the cell cites as an express checkout method (WC-S-5339). It is a reading on the id alone.
- **`au_becs_debit` (WC-E-a984e946) has only the parent's line.** No held source I may read names what it is. The cell's chart doesn't list it, and the store's recommended methods don't hold it. What would settle it: a WooPayments statement held that names BECS Direct Debit.
- **WooPayments' own settings (WC-E-b306752a)** take five lines:
  - CM-PAY-002;
  - CM-PAY-014: saved_cards, the setting the cell cites (WC-S-5468), and WooPay;
  - CM-CHK-008: the express checkout methods and the payment request button;
  - CM-PAY-012, `shows`: amazon_pay among the express checkout methods;
  - CM-PAY-020: `manual_capture`.

  `test_mode`, `enable_logging` and `account_statement_descriptor` are fields with no capability of their own, so they are in the reading (see "For the second stage").
- **Fillers.** A method's name is its filler: Affirm, Afterpay, Clearpay, Klarna, Alipay, Apple Pay, Bancontact, EPS, Google Pay, GrabPay, iDEAL, Multibanco, P24, SEPA and WeChat Pay. Each is written as the platform's own name, where the entry's text holds only the id (`afterpay_clearpay`, `wechat_pay`, `p24`, `sepa_debit`). The checker accepted them. If the coordinator wants the ids instead, only the filler column changes.

## The payment providers (30 entries)

**What the structure is.** For each business location, the Payments settings list:
- `providers`: WooPayments, the suggestions WooCommerce shows first, and the group of offline methods;
- `suggestions`: the other providers, each `_type: psp` and `category: psp`. The answer's own `suggestion_categories` names that category 'Payment Providers', 'Give your shoppers additional ways to pay.'.

The scope of each line is the entry's `within`, the location the call asked for (AE, EG, GB, JP).

**How each kind was decided.**
- **WooPayments** (`woocommerce_payments`, `_type: gateway`, 'Accept payments with Woo', 'Credit/debit cards, Apple Pay, Google Pay, and more.'), 4 entries:
  - CM-PAY-002, `own-service`. The maker is the release's mapping of the id (as above), its plugin `woocommerce-payments` (the item's own `plugin`, which the rendering leaves out) and WC-S-0557. The name's "Woo" is a brand and names no maker.
  - CM-PAY-012, `shows`, for the Apple Pay and Google Pay its description names, as WC-3. Apple Pay and Google Pay are the fillers.
  - The store's state (enabled false, needs_setup true) is in the reading.
- **PayPal Payments** (`_wc_pes_paypal_full_stack`, `_type: suggestion`, in `providers`), 4 entries:
  - CM-PAY-013 and CM-PAY-011, `extension-point`, PayPal the filler, as WC-2;
  - CM-PAY-012 for Venmo, quality 'Venmo: US only', and CM-PAY-015 for Pay Later: the third party's own features its listing names (M-8), each `extension-point`.
- **Take offline payments** (`_wc_offline_payment_methods_group`, `_type: offline_pms_group`), 4 entries: a container, on CM-PAY-016, `core`, whose cell cites Payments > offline (WC-S-0030). Its children are Direct bank transfer, Check payments and Cash on delivery (the item's `offline_payment_methods`), which aren't entries (below). Its 'These can also be used to test purchases.' is the cell's own 'useful to test purchases' (Check payments), so it is in the reading, not a line of its own.
- **The suggestions** (`category: psp`, and Mastercard Merchant Cloud in EG's `providers`), 18 entries:
  - Each is `extension-point` on CM-PAY-011, the provider its filler. That is M-3 and M-7, as refined after WC-3: a suggestion that names a third party's product.
  - What a description names besides the provider takes its own `extension-point` line, with the provider as filler (M-8):
    - Stripe: CM-MKS-006 ('135+ currencies', quality 'currencies: 135+'), CM-PAY-012 (Alipay, Apple Pay) and CM-CHK-008 ('one-touch checkout');
    - Paymob: CM-PAY-021 ('in-store');
    - Square: CM-PAY-021 ('Sell in store') and CM-INV-001 ('track sales and inventory');
    - Airwallex: CM-PAY-012 (Apple Pay, Google Pay) and CM-MKS-007 ('save on FX fees');
    - Viva.com: CM-MKS-006 ('multiple currencies');
    - Kustom Checkout: CM-PAY-015 (Pay Later, Financing, Installments) and CM-CHK-001 ('A full checkout experience embedded on your site');
    - GoCardless: `new:Direct Debit`.
  - Counts and rates the descriptions state are qualities, on the provider's line: Mastercard's '35+' payment methods, Airwallex's '60+' local payment methods, Viva.com's 'over 25' countries, Square's rate.
  - **Fillers:** N-Genius Online's filler is Network, from 'N-Genius Online by Network'. Visa Acceptance Solutions' is its own name: the entry names no other party.

**The tags `made_in_woo`: a maker statement I didn't take, for the coordinator.**
- The items' `tags`, which the selection drops, mark these with `made_in_woo`: WooPayments, PayPal Payments, Stripe and Square.
- The release defines the tag as 'For extensions developed by Woo.' (`src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php`, line 105).
- That is a code comment. No file of the release's admin assets uses the tag, so the admin doesn't show it to merchants. The ruling counts a field as a maker statement only where the admin shows it, as `is_built_by_wc` shows as Built by WooCommerce. So I placed PayPal Payments, Stripe and Square by what the entries show, as third parties' solutions (`extension-point`). WooPayments is `own-service` on other evidence.
- **It conflicts with held statements:** CM-PAY-013 cites 'PayPal Payments by PayPal' (WC-S-0911), and CM-PAY-011 cites a "Stripe by Stripe" extension.
- **What would settle it:** a ruling on whether a release's code comment that defines a tag counts as maker evidence (M-1). If it does, Stripe's, Square's and PayPal Payments' lines would also take `own-service` on CM-PAY-011 and CM-APP-011.

**EG here is Egypt's own list.**
- This isn't like the core profiler's EG item (the evidence map). Each location's answer here is a file of its own: AE's `1f65d465…`, EG's `dbd31edd…`, and so on, for all eight.
- The run's answers.jsonl holds a request whose body is `{"location":"EG"}`.
- EG's list differs from AE's: Mastercard Merchant Cloud among the providers, and Paymob at priority 20.
- So the EG entries are scoped EG.

## New things

| new | entries | place of its own | proposed domain / area / parent (a reading) | name (English; WooCommerce is held in English only) | terms searched |
| --- | --- | --- | --- | --- | --- |
| `new:Direct Debit` | WC-E-c68a575e (GoCardless, GB): 'Accept Direct Debit, ACH Pull, and open banking payments.' | none: a line of a suggestion's description | C PAY; parent CM-PAY-001, or CM-PAY-016 if the coordinator reads bank-account payments with bank transfer | Direct Debit (with ACH Pull, open banking payments) | caps: direct debit; open banking; ach; mandate (finds CM-PAY-022, payment mandates, whose note sets it apart as methods the store keeps and charges without checkout); bank; debit |

- **The leads, read:**
  - CM-PAY-023 (by banking) is the merchant's money account with the platform, not a way the buyer pays.
  - CM-PAY-017 (by accept, payment) is local methods through the platform's own service, which GoCardless isn't.
- **Lines that touch the same thing:** WooPayments' `sepa_debit` and `au_becs_debit`. `sepa_debit` is on CM-PAY-017 by the cell's chart (SEPA Direct Debit). If the coordinator makes Direct Debit a capability, both could take a line on it too.

## CHANGES lines, and what I decided on each

- **CM-CAT-007 gains core** (lines 9 and 32: Main image width, Thumbnail width). Kept: WooCommerce's own settings of product images, as WC-3's placeholder image and image matching. WC-3's lines aren't amended into the model yet, so the checker shows the change again.
- **CM-CNT-008 gains core** (line 30: the Terms and conditions page). Kept, as a reading, as WC-3's Refund and Returns Policy page: the store's terms page, a policy the capability's note names.
- **CM-PAY-020 gains own-service** (line 61: WooPayments' `manual_capture`). Kept, as a reading on the key alone: a WooPayments setting for capturing a payment, the capability's "capturing". What would settle it: WooPayments' own label for the setting, which the held sources I may read don't hold.
- **CM-INV-001 gains extension-point** (line 107: Square's 'track sales and inventory in one place'). Kept, as a reading, by M-8. It is the weakest of them: it rests on four words of a provider's description, and doesn't say that the store's own stock is synced. If the coordinator reads it as Square's own POS, out of the store, the line goes and the cell stays `core`.
- **CM-MKS-007 gains extension-point** (line 112: Airwallex, 'save on FX fees'). Kept, as a reading, by M-8: currency conversion through a third party the platform's list names.
- **CM-CHK-001 gains extension-point** (line 119: Kustom Checkout, 'A full checkout experience embedded on your site'). Kept, as a reading, by M-8: a third party's checkout in the store through the platform's list of providers.

**The other NOTEs, each read:**
- **Each `own-service` line** rests on WooPayments' maker: the release's mapping of `woocommerce_payments` and WC-S-0557, as above. The CM-PAY-015 and CM-PAY-017 lines also rest on the cells' own S-02 evidence, which the coordinator added. They cite that evidence as a reading; they don't cite the subject's statements as a part's keys.
- **Lines 82 and 120** (N-Genius, Elavon): their lead CM-ACC-004 is by 'business' in 'Power your business' and 'Grow your online business', no lead.
- **Line 115** is GoCardless's provider line, followed by its new thing (line 116). Their leads are read above.

## Entries I couldn't tell, and what would settle each

- **`au_becs_debit`:** above.
- **`link` (WC-E-b0c36f13), on CM-CHK-008 `shows`:** read as Link by Stripe on the id alone. What would settle it: a WooPayments statement held that names the method `link`.
- **The store address settings (lines 1, 2, city, postcode):** on CM-ACC-006 alone, as WC-3 placed Country / State. The section's description, 'Tax rates and shipping rates will use this address.', is cited by CM-TAX-001 and CM-SHP-001 (WC-S-0599), so they could take lines there too. I kept to WC-3's one line. The coordinator decides the four with WC-3's.
- **The trash settings on CM-ORD-012:** 'They will be trashed after the specified duration.' A reading: WordPress's trash keeps an order for restoring, but the held words don't say so.

## A structure whose items and sources disagree, and a problem with the selection

- **The offline methods aren't entries.** `selection.tsv`'s rule for `payments-providers` names `nested:providers,offline_methods,suggestions,payment_methods`. The items' keys are `providers`, `offline_payment_methods`, `suggestions` and `suggestion_categories`. So `offline_methods` and `payment_methods` match nothing, and the 58 entries are only `providers` (27) and `suggestions` (31).
  - **What no entry holds:** each location's Direct bank transfer, Check payments and Cash on delivery (`offline_payment_methods`), and the four categories (`suggestion_categories`): 'Wallets &amp; Express checkouts', 'Buy Now, Pay Later', 'Crypto Payments' and 'Payment Providers'.
  - Their cells already hold the offline methods (CM-PAY-029, CM-PAY-030, CM-PAY-016), so nothing is lost but their scope by location.
  - For the coordinator: the rule's key would be `offline_payment_methods`.
- **The rendering drops `plugin`, `tags` and `links`.** I read them in the item to clarify only: the plugin's slug, as a maker reading for WooPayments, and the tags above. No line takes its terms from them.

## For the second stage: what the sources state that no entry holds, or leads

- **WooPayments' onboarding** (dropped by the rule, in each WooPayments provider's `onboarding`):
  - the steps payment_methods, wpcom_connection and business_verification, with their status;
  - the recommended methods for the location (card, Apple Pay, Google Pay for AE);
  - the WordPress.com connection's state.

  The `woopayments-onboarding` structure holds the same, for CM-PAY-003 and CM-ACC-010.
- **Each provider's links:** pricing, about, terms, documentation and support (items.jsonl). For example, Stripe's terms are 'https://stripe.com/legal/connect-account', and Mastercard's are developer.mastercard.com's terms of use. These are leads for the fillers' terms.
- **WooPayments' fields with no capability:**
  - `test_mode` and `dev_mode`, the test mode of the payment service;
  - `account_statement_descriptor`, the name on the buyer's card statement;
  - `enable_logging`, a lead for CM-OPS-005 only if a statement says WooPayments' logs are the store's logs.

  All are in options.tsv, line 570.
- **WooPay's checkout message** in the same row: 'By placing this order, you agree to our [terms] and understand our [privacy_policy].' It is a lead for CM-PAY-014 and CM-TRU-006.

## Problems with the brief or the script

- **The selection rule's keys** (above).
- **`show --meta` printed only `payments-providers`' keys.** `options` is a `rows:` structure with no `meta.json`, as WC-3 found.
- **B-extent and this brief read the same, as far as I found.** One place calls for care: B-extent's `extension-point` needs "something the platform provides". Each M-8 line rests on the platform's list of providers, which M-3 and M-7 count as that.

## The coordinator's check (30 October 2026, after the batch)

- **The selection rule missed two lists, now built.** `payments-providers`' rule named `offline_methods`, where the items' key is `offline_payment_methods`, and didn't name `suggestion_categories` at all. With both in the rule, the build adds 56 entries, each location's offline methods and its suggestion categories, and loses none placed. They join WC-5, which the coordinator cut again with the structure's rest.
- **`made_in_woo` is not taken as a maker statement,** as the batch decided (ruling). The release defines it only in a constant's comment, `const TAG_MADE_IN_WOO = 'made_in_woo'; // For extensions developed by Woo.` (`src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php`, line 105). No admin asset shows it to merchants, which is what made `is_built_by_wc` a maker statement. For PayPal Payments it contradicts what merchants are shown, 'PayPal Payments by PayPal' (WC-S-0911). The brief says so (3.4), for WC-5.
- **This structure's EG is Egypt's own list,** with its own answer and a request for `{"location":"EG"}`, unlike the free extensions' EG item. So its entries are scoped EG (`evidence-map.md`).
- **Direct Debit** (GoCardless: 'Accept Direct Debit, ACH Pull, and open banking payments.') holds no capability of the model. It is decided with WooCommerce's other new things.
- **The four cells that gain a placement stand as readings,** each from the provider's or the setting's own words: manual capture (CM-PAY-020), Square's inventory (CM-INV-001), Airwallex's FX (CM-MKS-007) and Kustom's checkout (CM-CHK-001).
