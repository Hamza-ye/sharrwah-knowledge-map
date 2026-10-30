# Notes: held pass, WooCommerce, batch WC-5 (`payments-providers`, the rest)

**What the batch holds:** 84 entries of `payments-providers`. Each item is the answer of `POST /wp-json/wc-admin/settings/payments/providers {"location": <code>}` in run 20261029T023051Z-country-change-en (its `meta.json`), at other-product-class@0d79b794f:woocommerce/structures/payments-providers/items.jsonl. Lines 1 to 8 are AE, EG, GB, JP, OM, SA, US and YE. The entries are:
- **each location's offline payment methods** (Direct bank transfer, Check payments, Cash on delivery): 24 entries;
- **each location's suggestion categories** (Wallets &amp; Express checkouts, Buy Now, Pay Later, Crypto Payments, Payment Providers): 32 entries;
- **the rest of the providers and suggestions:** JP's 5 suggestions, and OM's, SA's, US's and YE's providers and suggestions: 28 entries.

The coordinator's corrected rule (`nested:providers,offline_payment_methods,suggestion_categories,suggestions,payment_methods`) added the first two kinds after WC-4.

**The batch before this one.** I read WC-4's placements for this structure, and its notes to the end, "The coordinator's check" included. Where a provider is the same thing, I kept to WC-4's lines: same capabilities, supports, terms, fillers and qualities, with the reading's location and item line changed. That covers WooPayments, PayPal Payments, the offline group, Stripe, Square, Airwallex, Mastercard Merchant Cloud, Paymob, Visa Acceptance Solutions, N-Genius and Elavon. I also kept to WC-1 to WC-3 through WC-4's lines: PayPal Payments on CM-PAY-013 and CM-PAY-011, and WooPayments' wallets on CM-PAY-012, `shows`.

I followed the coordinator's two rulings:
- the suggestions' `made_in_woo` tag names no maker (Stripe, Square and PayPal Payments stay `extension-point`);
- each location's answer is its own list, so each line's scope is the entry's `within`.

**Count:** 84 entries, 137 lines.
- **By entry:** all 84 have `capability` lines. None is `new` and none is `out`.
- **By supports:** extension-point 85, core 44, shows 7, own-service 1.

## How each kind was decided

**The offline payment methods** (`list: offline_payment_methods`, `_type: offline_pm`), 3 per location:
- **Direct bank transfer** (`bacs`): CM-PAY-030, `core`, whose cell cites the same gateway and words (WC-S-0032, WC-S-0603). Also CM-PAY-016, `core`, the parent: the method is in the list `offline_payment_methods`, of type `offline_pm`, a child of the group Take offline payments. So it is a kind of the parent's thing (M-6, refined after the calibration: Bank deposit under OFFLINE PAYMENT METHODS).
- **Check payments** (`cheque`): CM-PAY-016, `core`, alone. The cell cites the same gateway and words (WC-S-0033, WC-S-0606), and no child capability holds checks (`caps --terms "cheque; check payments"` finds only CM-PAY-016).
- **Cash on delivery** (`cod`): CM-PAY-029, `core` (WC-S-0031, WC-S-0605), and CM-PAY-016, `core`, the parent, as for `bacs`.
- **WooCommerce's own:** the release maps `bacs`, `cheque` and `cod` to WooCommerce core's provider (`woocommerce-11.2.1:src/Internal/Admin/Settings/PaymentsProviders.php`, lines 110 to 112). Each item's plugin is `woocommerce`, active, and its settings link is `path=/offline/<id>`. Each reading cites these.
- **The store's state is in the reading:** `cod` enabled, `bacs` and `cheque` not.
- **The same at every location:** the three methods have the same titles, descriptions and state at all eight locations. Only `_order` differs: SA's are 22 to 24, the others' 23 to 25.

**The suggestion categories** (`list: suggestion_categories`), 4 per location. They are a fixed list: the release defines the same four for every location (`PaymentsProviders.php`, lines 999 to 1027). Each is a category of the platform's own list of payment provider suggestions. I read that list as one of the platform's own lists of third parties' solutions to install (M-3, M-7), and placed each category as a container on the capability its title names (M-13). Each is `extension-point` (a reading), as the model reads the Marketplace's subcategories of the same names:
- **`express_checkout`, Wallets &amp; Express checkouts:** CM-PAY-012 (Wallets) and CM-CHK-008 (Express checkouts, 'fast-track the checkout process'). Both cells read the Marketplace subcategory Wallets & express checkouts (WC-S-0707). Apple Pay and Google Pay are the fillers, as WC-4 fills them for WooPayments' description.
- **`bnpl`, Buy Now, Pay Later:** CM-PAY-015, as WC-S-0708.
- **`crypto`, Crypto Payments:** CM-PAY-018, as WC-S-0709.
- **`psp`, Payment Providers:** CM-PAY-011. It holds each location's suggestions, every one of them category `psp`. Its title also shares words with CM-PAY-001, the settings page, but its suggestions are third parties' providers. WC-4 placed none of them on CM-PAY-001, and I kept to that.

**JP's suggestions.**
- Stripe, Square, Airwallex Payments and Visa Acceptance Solutions are as WC-4.
- **KOMOJU Payments** (WC-E-bbc7f4de): 'Easily add popular Japanese payment methods like konbini, PayPay, and more with KOMOJU’s secure extension to optimize checkout.'
  - It goes on CM-PAY-011, `extension-point`, with KOMOJU and PayPay as fillers.
  - **Its Japanese payment methods aren't a CM-PAY-017 line.** CM-PAY-017 is 'region-specific ways to pay, offered through the platform's payment service'. Its note keeps a local method through a third party's gateway in CM-PAY-011 (Salla's KNET through Tap). WC-4 did the same with Airwallex's '60+ local payment methods'.
  - **What konbini and PayPay are isn't stated.** So PayPay takes no CM-PAY-012 line: M-5, the role comes only from the entry and its sources.

**OM, SA, US and YE's providers and suggestions** are as WC-4's, by location. Six things are their own:
- **OM's Paymob and YE's Visa Acceptance Solutions are in `providers`,** `_type: suggestion`, tags `preferred` and `recommended`, with no category. Their readings say so, as WC-4 reads EG's Mastercard Merchant Cloud. SA's Mastercard Merchant Cloud is the same.
- **US's WooPayments** is `own-service`, as at AE, GB and JP. Its onboarding is `supported: true`, and it carries the tag `woopay_eligible`, which the rendering drops. That tag is a lead (below).
- **WooPayments at OM, SA and YE is `shows`, not `own-service`** (the batch's one decision against WC-4's pattern):
  - Each of those items' WooPayments `onboarding`, which the rule drops, states `supported: false`, with the message 'WooPayments is not supported in the selected business location.' (items.jsonl, lines 5, 6 and 8).
  - So the provider listed there shows the service, with its maker evidence as elsewhere, but supports no placement for those locations.
  - The wallets line, CM-PAY-012 `shows`, stays as WC-4.
  - **For the coordinator: EG is the same.** WC-4's EG line (WC-E-d56e3076) is `own-service`, but EG's onboarding also states `supported: false` and 'not_supported' (items.jsonl, line 2). AE, GB, JP and US state `supported: true`. If the coordinator keeps my reading, WC-4's EG line becomes `shows`. If it keeps WC-4's, my three lines become `own-service`. Neither changes the cell, which holds both. What each changes is the scope by location, which the market subjects read. For Sharrwah, YE's reads 'WooPayments is not supported in the selected business location.'
- **YE's answer holds no suggestions.** Its one suggested provider is Visa Acceptance Solutions, in its providers. YE's four categories are still listed, and its `psp` category's reading says it holds none.
- **The PayPal Payments lines** (OM, SA, US) keep Venmo's quality 'Venmo: US only' at every location, as WC-4, since it is the description's words.

## No new things

Every entry's thing is a capability the model holds. Terms searched with `caps --terms`, for a thing no lead named:
- test purchases; test mode; test order; test; sandbox; bogus. No capability holds testing purchases. 'This offline gateway can also be useful to test purchases.' is in the readings, as WC-4 and the CM-PAY-016 cell keep it.
- cheque; check payments: CM-PAY-016 only.
- konbini; PayPay; KOMOJU; Japanese; convenience store: nothing.
- express checkout; wallet; crypto; buy now; pay later; payment provider; offline; suggestion; recommended: the capabilities placed above.

## Entries I couldn't tell, and what would settle each

- **The categories `express_checkout`, `bnpl` and `crypto` hold no suggestion at any held location.** Every suggestion is category `psp`. I placed them `extension-point` (a reading), as the model reads the Marketplace's subcategories of the same names, one of which (Crypto payments) names no extension either. Whether the admin shows an empty category isn't held. If the coordinator reads an empty category as showing only a topic, its lines become `shows`. No cell changes either way: CM-PAY-012, CM-PAY-015, CM-PAY-018 and CM-CHK-008 already hold `extension-point` on WooCommerce. What would settle it: the Payments settings page as rendered for a location, which the run's steps may hold (`20261029T023051Z-country-change-en/steps/`), read in the second stage.
- **WooPayments where it isn't supported** (OM, SA, YE, and WC-4's EG): above.
- **KOMOJU's konbini and PayPay:** above. What would settle it: a held statement that names what they are.

## A structure whose items and sources disagree

- **The items and their answer files agree.** I compared each item's four lists with the answer file it names: all eight are equal.
- **The run holds two answers each for SA and YE.** The items for SA and YE take the answers of steps 24 and 28 (`6b32ad80…`, `f6b7b6621…`). The same run's step 37 holds a second answer for each, with the same body (`e529bdfd…` for SA, `97abe98b…` for YE; `raw/runs/20261029T023051Z-country-change-en/answers.jsonl`). They differ only in `_order`:
  - SA's Mastercard Merchant Cloud is 2 against 19, PayPal Payments 20 against 21, the offline group 21 against 22, and its offline methods 22 to 24 against 23 to 25;
  - YE's Visa Acceptance Solutions is 2 against 18.

  Nothing placed rests on `_order`.
- **The title 'Wallets &amp; Express checkouts' is HTML-escaped in the answer.** The release's string is 'Wallets & Express checkouts', passed through `esc_html__` (`PaymentsProviders.php`, line 1004). The readings quote the entry as held, and the terms avoid the entity (Wallets; Express checkouts).

## For the second stage: what the sources state that no entry holds, or leads

- **WooPayments' support by location:** `onboarding.state.supported` and the message 'WooPayments is not supported in the selected business location.', for EG, OM, SA and YE (items.jsonl, lines 2, 5, 6, 8). It is a lead for the market subjects and CM-PAY-002's scope.
- **WooPayments' recommended methods by location** (`onboarding.recommended_payment_methods`):
  - AE: card, apple_pay, google_pay;
  - GB adds afterpay_clearpay, klarna, bancontact, eps, ideal, multibanco, amazon_pay, alipay, wechat_pay;
  - JP adds bancontact, eps, ideal, alipay, wechat_pay;
  - US adds woopay, affirm, afterpay_clearpay, klarna, bancontact, eps, ideal, multibanco, amazon_pay, alipay, wechat_pay;
  - EG, OM, SA and YE: none.

  It is a lead for CM-PAY-017's and CM-PAY-015's scopes (items.jsonl, lines 1 to 8).
- **US's WooPayments tag `woopay_eligible`** (items.jsonl, line 7): a lead for CM-PAY-014 and CM-CHK-008 (WooPay), if a held statement shown to merchants says what it means.
- **The providers' links,** each a lead for the fillers' terms:
  - KOMOJU's terms 'https://toc.komoju.com/toc/' and pricing 'https://en.komoju.com/pricing/' (line 4);
  - Square's Japanese pricing and terms (line 4);
  - Elavon's terms 'https://developer.elavon.com/terms' (line 7);
  - Paymob's 'https://paymob.com/en/policy' (lines 5, 6).
- **The offline methods' `supports: products`, and WooPayments' `supports`** (products, refunds, tokenization, add_payment_method): dropped by the rule. A lead for CM-PAY-022 (tokenization) and refunds, if a statement says what each means for the merchant.

## CHANGES lines, and what I decided on each

Both are WC-4's lines again, at JP and US. WC-4's lines aren't amended into the model yet, so the checker shows the change again.
- **CM-INV-001 gains extension-point** (lines 43 and 114: Square, 'track sales and inventory in one place'). Kept, as WC-4 and the coordinator's check left it: a reading, by M-8. It is the weakest line of the batch, as WC-4 says. If the coordinator drops WC-4's line, drop these two with it.
- **CM-MKS-007 gains extension-point** (lines 47 and 118: Airwallex, 'save on FX fees'). Kept, as WC-4: a reading, by M-8.

**The other NOTEs, each read:**
- **The `own-service` on CM-PAY-002** (US's WooPayments) rests on the release's mapping of `woocommerce_payments` (line 114) and WC-S-0557, as WC-4's. The onboarding states `supported: true` for US.
- **Lines 90 and 119** (N-Genius at SA, Elavon at US): their first lead, CM-ACC-004, is by 'business' in 'Power your business' and 'Grow your online business'. That is no lead, as WC-4 found.

## Problems with the brief or the script

- **B-extent and this brief read the same for this batch,** as far as I found.
- **The checker's lines count the header:** a reported line N is the file's line N.
- **No other problem found.**

## The coordinator's check (30 October 2026, after the batch)

- **WooPayments is `shows` where the platform says it isn't supported** (ruling). Its onboarding, in each location's item, states `supported` with the location: true in AE, GB, JP and US, and false in EG, OM, SA and YE, with 'WooPayments is not supported in the selected business location.' (items.jsonl, lines 2, 5, 6 and 8). The provider is listed there but stated unavailable, so OM, SA and YE are `shows`, as this batch placed them. WC-4's EG line is aligned to them. The cell doesn't change. What changes is the scope by location that the market subjects read, Yemen's among them.
- **The empty suggestion categories are `shows`** (ruling): express checkout, buy now pay later and crypto. No held location puts a suggestion in them; every suggestion is in `psp`. They show the topic, with no provider offering it. `psp` stays `extension-point`.
- **Square's inventory and Airwallex's FX lines stand** as WC-4's, readings under M-8.
