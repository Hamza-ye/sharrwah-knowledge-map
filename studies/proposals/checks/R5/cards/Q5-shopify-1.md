# Cards: Q5 on shopify

22 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - The merchant turns methods on, from those offered to its store: Shopify's buyers pay with "any of the methods that you've activated"; Salla's merchant presses (تفعيل) on its طرق الدفع page; BigCommerce's uses Settings › Payments; WooCommerce's gateways carry an "Enable/Disable" box; Zid's merchant turns networks on in إدارة زد باي. They match by role, on stated pages and WooCommerce's shipped code. Q5-SH-K1524, Q5-SA-017, Q5-BC-066, Q5-WC-K0032, Q5-ZD-K0041
- **section 1, line 8:** - Staff need a payments permission, matching by role: `MANAGE_PAYMENTS_SETTINGS` (Shopify's admin code), `payment_methods_activation` (Salla's partner portal, as captured on 8 October 2026, observed), `manage_woocommerce` (WooCommerce's code), and a right Zid's owner grants (stated); at Shopify "Only the store owner can add a payment provider". Q5-SH-K0193, Q5-SA-K1509, Q5-WC-001, Q5-ZD-002, Q5-SH-009
- **section 1, line 9:** - The merchant's own rules then decide what a buyer sees, matching by role: Salla's قيود الدفع hide a method or reject or review the order by amount, country, customer group or category; Zid's restrictions hide a method; Shopify's Payment Customization lets an app "rename, reorder, hide the payment methods"; WooCommerce keeps cash on delivery to chosen shipping methods (shipped code); BigCommerce's merchant ticks "the countries where this payment method is available at checkout". Q5-SA-043, Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 1, line 10:** - Shopify, Zid and Salla limit methods by the store's country, matching by role: Shopify filters providers "based on your store's address"; Zid offers options "حسب دولتك", and زد باي only in Saudi Arabia and Kuwait; Salla's مدى and فيزا are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط". WooCommerce goes by country only in its suggestions, "The payment extension list for each country" (shipped code), and BigCommerce by the shopper's "geolocation" for local methods (stated; not checked on WooCommerce). Q5-SH-012, Q5-ZD-001, Q5-ZD-P0113, Q5-SA-036, Q5-WC-K0054, Q5-BC-081
- **section 1, line 11:** - Plans decide too, matching by role: Salla's electronic methods are "متاحة ضمن الباقات المدفوعة فقط"; Zid's Starter plan has only "Basic payment methods (bank transfer, cash on delivery)"; Shopify's custom payment extensions are "limited to eligible Shopify Plus Merchants only". A plan level that decides which methods a store can use was not in what was read on WooCommerce. Q5-SA-P0068, Q5-ZD-P0150, Q5-SH-K1700, Q5-WC-N09
- **section 1, line 12:** - The platform's own service checks the business first, matching by role: Salla's dashboard text, as captured on 8 October 2026, reads "مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه" (observed); زد باي needs the owner to pass نفاذ; "Only eligible merchants can use Shopify Payments". Q5-SA-K0091, Q5-ZD-P0117, Q5-SH-K1532
- **section 1, line 13:** - The own service and other gateways, matching by role: Shopify allows "only one credit card payment provider activated at a time"; Zid's terms say "عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر" (official page); Salla's dashboard text, as captured on 8 October 2026, blocks its own service "لوجود ربط فعَّال مع تاب" (observed). WooCommerce differs: WooPayments and the Stripe plugin can run "at the same time", which "does cause a few issues". Q5-SH-008, Q5-ZD-P0109, Q5-SA-K1653, Q5-WC-031
- **section 1, line 14:** - The platform approves what plugs in, matching by role: at Shopify "Only approved Partners can build payments extensions", and a new method "must be submitted for review and approval"; Zid reviews apps "before publishing it to the public"; "The Marketplace team reviews all app submissions" (BigCommerce). These are stated pages but Shopify's partner terms (official). Q5-SH-K1696, Q5-SH-062, Q5-SH-058, Q5-ZD-K0363, Q5-BC-K0316
- **section 1, line 15:** - Fees can follow the provider: BigCommerce's Open Payment Provider fee falls on orders not processed through its Embedded list; in Shopify's store fake-demo-sharrwah (countryCode YE), observed on 5 October 2026, ONERWAY (Direct) in test mode showed a "0.6% transaction fee". A fee that depends on the provider was not in what was read on WooCommerce or Zid. Q5-BC-085, Q5-SH-086, Q5-WC-N08, Q5-ZD-N10
- **section 1, line 17:** - Providers decide on the merchant and the buyer, matching by role: at BigCommerce "Each provider has its own application process"; at Salla a provider can reject the merchant's request (dashboard text as captured on 8 October 2026, observed), and "تحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة"; Zid's electronic payment needs the gateway's approval; Shopify's Adyen needs "an existing Adyen approval". Q5-BC-P0048, Q5-SA-057, Q5-SA-066, Q5-ZD-K0003, Q5-SH-071
- **section 1, line 18:** - Law, card networks and processors bar some sellers, matching by role: Shopify's restrictions "may be imposed by law or through the Payment Network Rules"; Zid bars زد باي for activities forbidden "من زد باي أو المملكة العربية السعودية أو بلد النشاط". Both are official pages. Q5-SH-K2262, Q5-ZD-P0111
- **section 1, line 19:** - In Shopify's store ibx5bt-xy (countryCode YE), observed on 30 September 2026, Shopify Payments was answered `"eligible":false`, and the saved Third-party payment providers page listed six, ONERWAY (Direct) and Tap Payments among them. Q5-SH-078, Q5-SH-094
- **section 1, line 23:** - Each platform has a payment service of its own, run through other companies, matching by role: Shopify Payments, processed and settled by "one or more Payment Processors"; WooPayments, "powered by Stripe"; Salla's, provided "عبر شركائها"; BigCommerce Payments, "powered by PayPal"; and زد باي, through "مقدمي خدمات الدفع". These are official pages but BigCommerce's (stated). Q5-SH-K1555, Q5-WC-K0008, Q5-SA-P0079, Q5-BC-P0055, Q5-ZD-P0003
- **section 1, line 24:** - Other companies' gateways, matching by role: Shopify's "over 100 credit card payment providers"; Salla's بوابات الدفع الأخرى (not checked on WooCommerce); Zid's بوابات الدفع الأُخرى; BigCommerce's providers on and off its Embedded list; WooCommerce's gateways, "created as additional plugins". Q5-SH-006, Q5-SA-K1638, Q5-ZD-K0084, Q5-BC-036, Q5-WC-K0007
- **section 1, line 25:** - Methods recorded outside any provider: Shopify's "manual payments"; BigCommerce's "offline payment methods"; WooCommerce's Offline type, where "No online payment is made"; Salla's طرق دفع أخرى; Zid's bank transfer. BigCommerce and WooCommerce match by the same term, offline; the others by role. In Shopify's store ibx5bt-xy (countryCode YE), observed on 30 September 2026, Cash on Delivery (COD), Money Order and Bank Deposit each carried `"group":"MANUAL"`. Q5-SH-027, Q5-BC-060, Q5-WC-016, Q5-SA-015, Q5-ZD-P0075, Q5-SH-083
- **section 1, line 26:** - Providers plug in as add-ons, matching by role: Shopify's "payments extensions"; WooCommerce's gateway classes, added "through traditional plugins"; Zid's Open APIs model for "partners / payment service providers (PSPs)"; BigCommerce's "app payment processors"; Salla's apps, through "the Recurring Payments API". Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-SA-064
- **section 1, line 27:** - Where the buyer pays: Shopify's "direct providers and external providers", the latter on a page outside the store; WooCommerce's Direct type, with payment fields "directly on the checkout page"; Zid's Open APIs, where in one checkout type "Zid will draw the payment form"; BigCommerce's gateways that "redirect shoppers to a hosted payment page". Shopify and WooCommerce match by the same term, direct; Zid and BigCommerce by role. Q5-SH-007, Q5-WC-016, Q5-ZD-K0080, Q5-BC-068
- **section 2, line 55:** - **Payment method**: in Sharrwah's proposed design, a way a buyer can pay an order, such as a card network, a wallet, pay later, bank transfer or cash on delivery: either a **provider method**, which a payment provider processes, or a **manual method**, which the buyer pays to the merchant outside any provider and the merchant records; an order paid by a manual method waits, unpaid, until then. Q5-SH-027, Q5-BC-P0115, Q5-WC-016
- **section 2, line 56:** - It draws on the five platforms' split between provider and manual methods, and on the waiting order of Shopify, BigCommerce and WooCommerce. Q5-SH-083, Q5-BC-060, Q5-SA-015, Q5-ZD-P0075, Q5-SH-K1736, Q5-WC-K0037
- **section 2, line 61:** - **Provider integration**: the code through which a provider plugs into Sharrwah, behind one payments interface: a **built-in integration**, which Sharrwah builds and keeps, or a **payments add-on**, which a provider or partner builds to Sharrwah's published interface, and which merchants can activate only once Sharrwah has reviewed it and it reports itself ready, a new method in it being reviewed again. The interface serves payment on Sharrwah's checkout and on the provider's page. Q5-BC-105, Q5-SH-K1696, Q5-SH-058
- **section 2, line 62:** - It draws on BigCommerce's Embedded Providers; Shopify's approved payments extensions, review of new methods and readiness step; Zid's Open APIs and app review; and the direct and hosted payment of Shopify, WooCommerce and BigCommerce. Q5-BC-105, Q5-SH-062, Q5-ZD-K0077, Q5-ZD-K0363, Q5-SH-007, Q5-WC-016, Q5-BC-068
- **section 2, line 63:** - Why: rule 2, each provider behind its own part; rule 1, one interface for every place. Q5-SH-K1694, Q5-ZD-K0077
- **section 2, line 68:** - **Place payment list**: Sharrwah's list, for each place it serves, of the providers and methods a store there may activate, each with its conditions: plan, verification, business type and amount limits. A store sees only its place's list, filtered by its conditions. Q5-SH-012, Q5-ZD-001, Q5-SA-036
- **section 2, line 69:** - It draws on Shopify's, Zid's and Salla's methods by the store's address or country, and, for conditions, on their plans, Salla's verification, Zid's كي نت for institutions and companies only, and Salla's limits by country. Q5-SH-012, Q5-ZD-001, Q5-SA-036, Q5-SA-P0068, Q5-ZD-P0150, Q5-SA-K0091, Q5-ZD-K0042, Q5-SA-048
- **section 2, line 70:** - Why: rule 1; what differs between places is set up as data, not built apart. Q5-SH-012, Q5-ZD-001
- **section 2, line 72:** - **Store payment settings**: per store, the methods the merchant has activated from its place's list and, for each, the one provider it goes to; changed only by staff holding a payments permission, a change of provider kept to the store owner, and each change logged. Where a store keeps separate markets or currencies, its settings follow them. Q5-SH-K1524, Q5-SH-008, Q5-SH-009
- **section 2, line 73:** - It draws on the activation and payments permissions the platforms show, Shopify's owner-only provider change and one card provider at a time, BigCommerce's change log, Salla's market selector and BigCommerce's methods per currency. Q5-SH-K0193, Q5-SA-K1509, Q5-BC-072, Q5-SA-016, Q5-BC-074
- **section 2, line 77:** - It draws on Salla's قيود الدفع, Zid's restrictions, Shopify's Payment Customization, WooCommerce's cash on delivery by shipping method and BigCommerce's countries per offline method. Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 2, line 78:** - Why: rule 3; they are cheap to change, so they come late, as data the checkout reads. Q5-SA-043, Q5-SH-K1761
- **section 2, line 86:** - Not taken, for the first build: an own service that shuts other card gateways out once active, as Shopify's and Zid's do, since it would be a held route. Q5-SH-008, Q5-ZD-P0109
- **section 3, line 98:** - Payment providers plug in, through a built-in integration or a payments add-on, as on all five platforms. Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-BC-105
- **section 3, line 100:** - Checkout payment rules can come from apps, as at Shopify, or from the merchant's settings. Q5-SH-K1761, Q5-SA-043
- **section 3, line 103:** - Which providers and methods are offered is set per place, by Sharrwah; the records go by the store's address or country, or where the business is registered. Q5-SH-012, Q5-ZD-001, Q5-WC-K0402
- **section 3, line 106:** - Restrictions on businesses are set by law, card networks, processors and the platform (Shopify), and per country of activity (Zid). Q5-SH-K2262, Q5-ZD-P0111
- **section 3, line 107:** - Activated methods, and the one provider for each, are set per store, and per market or currency where the store has them, by staff holding the payments permission. Q5-SH-K1524, Q5-SA-016, Q5-BC-074, Q5-SH-K0193
- **section 3, line 114:** - Approval of an add-on, and of each new method in it, is set by Sharrwah. Q5-SH-062, Q5-ZD-K0363
- **section 5, line 130:** - What a place is: the platforms go by the store's address or country, or where the business is registered. The design keys the place payment list by a place that may be narrower or wider than a country. Q1's proposal settles it. Q5-SH-012, Q5-WC-K0402, Q5-ZD-001
- **section 5, line 132:** - How a payment is completed: on Sharrwah's checkout, on the provider's page, or, as at YemenPay, by a transfer the buyer makes from its own wallet, matched afterwards. The design keeps the payments interface open to a payment confirmed after checkout. The providers chosen for each place (section 7) settle it. YA-112 (the buyer's own transfer, matched by an app on the merchant's phone @ YemenPay's service, as of 2026-08-22), Q5-SH-007, Q5-BC-068
- **section 7, line 159:** - Whether Sharrwah offers a payment service of its own in which sellers' money is held, by Sharrwah or by a payment company in an account opened through Sharrwah, and with which company: for the founder, under the guard. Q5-SH-K1555, Q5-WC-P0121, Q5-BC-P0069, Q5-SA-H0002, Q5-ZD-H0002
- **section 7, line 161:** - Whether providers and partners may build payments add-ons, and under what agreement and review. Q5-SH-K1696, Q5-SH-063, Q5-WC-K0353, Q5-ZD-K0077
- **section 7, line 162:** - Whether Sharrwah charges a fee that depends on the provider an order was paid through, and whether its fees are taken from payments or billed apart. Q5-BC-085, Q5-SH-086, Q5-WC-N08, Q5-ZD-N10
- **section 8, line 176:** - Records: Shopify Payments' processors, Stripe for WooPayments, and BigCommerce Payments' PayPal platform account settle; Zid's terms credit "المبلغ المستحق لرصيد التاجر" after fees; who settles Salla's payments was not in what was read. S01-VP-02, Q5-SH-K1555, Q5-WC-P0122, Q5-BC-P0070, Q5-ZD-P0024, Q5-SA-H0004
- **section 8, line 182:** - Records: the own services' processors (Shopify Payments; BigCommerce Payments, "powered by PayPal"); a connected gateway, at Salla "بدلًا من مدفوعات سلة" (dashboard text as captured on 8 October 2026, observed); the merchant, for Salla's bank transfer; and Zid, for cash on delivery through its shipping. S01-VP-04, Q5-SH-K1555, Q5-BC-P0055, Q5-SA-K1639, Q5-SA-P0099, Q5-ZD-P0070

## The cards

### Q5-SH-K1524

**Cited at:** section 1, line 7; section 2, line 72; section 3, line 107

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-062
- placement: decides
- structure: https://help.shopify.com/en/manual/payments.md
- identifier: help.shopify.com/en/manual/payments.md
- statement: When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the
- cite_ids: SH-S-0319
- note: first run's citation

**Citation SH-S-0319:** `https://help.shopify.com/en/manual/payments.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/047-help.shopify.com/text.txt` (3685 bytes), fetched 2026-10-11T06:13:00Z, captured
- quote: When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the
- title: Payments
- the page opens: Make sure that you understand the payment process. When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the Payment providers area of your Shopify admin. You can activate a variety of payment methods using Shopify. If you want to let your customers pay using a credit card, then you can use Shopify Payments, a third-party provider, or both together. There are also several ways for customers to pay online without using a credit card, …
- a note box: Note For customers based in Finland, a payment method won't be selected by default during checkout to comply with regulations.
- a note box: Note If you sell subscription products, then you need to use Shopify Payments as your primary payment gateway. To learn more about subscriptions, refer to Subscriptions.
- headings: Payments
- in context: # Payments Make sure that you [understand the payment process](/manual/payments/getting-paid). ⟪When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the⟫ [**Payment providers**](https://admin.shopify.com/settings/payments) area of your Shopify admin. You can activate a variety of payment methods using Shopify. If you want to let your customers pay using a credit card, then you can use [Shopify Payments](/manual/payments/shopify-payments), a [third-party provider](/manual/payments/third-party-providers), or [both together](/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party…

### Q5-SH-K0193

**Cited at:** section 1, line 8; section 2, line 73; section 3, line 107

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-062
- placement: decides
- structure: structures/shopify/admin-router
- identifier: payments:settings:index
- statement: "eligibility":{"oneOf":[{"permissions":["MANAGE_PAYMENTS_SETTINGS"]},{"permissions":["GIFT_CARDS"]},{"permissions":["SHOPIFY_PAYMENTS_TRANSFERS"]}]}
- cite_ids: SH-S-5246
- note: section Payments

**Citation SH-S-5246:** `observed-sh@e49840729:structures/shopify/admin-router/items.jsonl` | line 1004 (payments:settings:index) | 2026-09-29 | kind: shipped | quote check: found
- quote: "eligibility":{"oneOf":[{"permissions":["MANAGE_PAYMENTS_SETTINGS"]},{"permissions":["GIFT_CARDS"]},{"permissions":["SHOPIFY_PAYMENTS_TRANSFERS"]}]}
- in context: {"id":"payments:settings:index","parent":"payments:settings","position":0,"array_offset":2189924,"section":"Payments","title":{"value":"Payments"},"resource":"payment:settings","index":true,"context":["merchantRiskGraphql","organization","organizationFlags","organizationGraphql","completenessEngineGraphql","intents"],⟪"eligibility":{"oneOf":[{"permissions":["MANAGE_PAYMENTS_SETTINGS"]},{"permissions":["GIFT_CARDS"]},{"permissions":["SHOPIFY_PAYMENTS_TRANSFERS"]}]}⟫,"anchors":[{"title":"Payments","path":"payments"},{"title":"Apple Wallet Passes","path":"applewalletpasses"},{"title":"Gift card expiration","path":"giftcardexpiration","intent":{"action":"edit","type":"settings/GiftCardExpiration","release":"public","schema":{"output":{"success":{"mapTo":"manual","type":"boolean/plain"}}}}},{"title":"Manual payment methods","path":"manual"},{"title":"Additional payment methods","path":"other"},{"title":"Payment…

### Q5-SH-009

**Cited at:** section 1, line 8; section 2, line 72

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-009
- bears_on: 1
- identifier: Activate a credit card payment provider
- statement: Only the store owner can add a payment provider.
- cite_ids: Q5-SH-C012
- from: held

**Citation Q5-SH-C012:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md` | Activate a credit card payment provider, note | undated | kind: stated | quote check: found (markup removed)
- quote: Only the store owner can add a payment provider.
- title: Configuring third-party payment providers
- the page opens: If you're not using Shopify Payments and you want to accept credit cards, then you can choose from over 100 credit card payment providers for your Shopify store. You can activate or change a payment provider from the Payments page of your Shopify admin. Depending on the requirements of the payment provider, you might be required to submit and verify your bank account information with them so that your store can complete transactions. Contact your payment provider to confirm whether or not you ca…
- a note box: Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner.
- a note box: Note Only the store owner can add a payment provider.
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Configuring third-party payment providers > Activate a credit card payment provider {#activate-credit-card-provider}
- in context: …re providing your bank account information. Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner. Activate a credit card payment provider {#activate-credit-card-provider} You can have only one credit card payment provider activated at a time. If you already have a provider activated, then you can change your credit card payment provider. Note ⟪Only the store owner can add a payment provider.⟫ Steps: Desktop From your Shopify admin, go to Settings > Payments. Do one of the following: If you have Shopify Payments active, then in the Shopify payments section, click Manage. At the bottom of the page, click Switch to a third-party provider, and then click Switch to a third-party provider again to confirm. If you don't have Shopify Payments active, then in the Shopify payments section, click See all other providers. If Shopify Payments isn…  (matched markup removed)

### Q5-SH-K1761

**Cited at:** section 1, line 9; section 2, line 77; section 2, line 78; section 3, line 100

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-083
- placement: where
- structure: https://shopify.dev/docs/api/functions/latest/payment-customization.md
- identifier: shopify.dev/docs/api/functions/latest/payment-customization.md
- statement: enables you to rename, reorder, hide the payment methods available to customers during checkout, set payment terms, and add a review requirement for a specific order.
- cite_ids: SH-S-0589
- note: first run's citation

**Citation SH-S-0589:** `https://shopify.dev/docs/api/functions/latest/payment-customization.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/109-shopify.dev/text.txt` (136500 bytes), fetched 2026-10-11T06:13:07Z, captured
- quote: enables you to rename, reorder, hide the payment methods available to customers during checkout, set payment terms, and add a review requirement for a specific order.
- title: Payment Customization Function API
- the page opens: A payment customization enables you to rename, reorder, hide the payment methods available to customers during checkout, set payment terms, and add a review requirement for a specific order. Examples of payment methods that you can customize include credit cards, gift cards, and wallets such as Shop Pay, Apple Pay, and Google Pay. Payment terms allow buyers to pay for their order at a later date instead of at checkout, and can be set as fixed, net, or event-based terms with optional deposits. To…
- headings: Payment Customization Function API
- in context: …yers during checkout, set payment terms, and add a review requirement. api_version: 2026-10 source_url: html: 'https://shopify.dev/docs/api/functions/latest/payment-customization' md: 'https://shopify.dev/docs/api/functions/latest/payment-customization.md' api_type: functions api_name: payment-customization --- # Payment Customization Function API A [payment customization](https://help.shopify.com/manual/checkout-settings/checkout-customization) ⟪enables you to rename, reorder, hide the payment methods available to customers during checkout, set payment terms, and add a review requirement for a specific order.⟫ Examples of payment methods that you can customize include credit cards, gift cards, and wallets such as Shop Pay, Apple Pay, and Google Pay. [Payment terms](https://help.shopify.com/manual/fulfillment/managing-orders/payments/deferred-payments) allow buyers to pay for their order at a later date instead of at checkout, and can be set as fixed, net, or event-based terms with optional deposits. To customize payment methods and payment terms in ch…

### Q5-SH-012

**Cited at:** section 1, line 10; section 2, line 68; section 2, line 69; section 2, line 70; section 3, line 103; section 5, line 130

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-012
- bears_on: 1
- identifier: Settings > General
- statement: The third-party provider list in your Shopify admin is filtered based on your store's address in Settings > General
- cite_ids: Q5-SH-C015
- from: held

**Citation Q5-SH-C015:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md` | Troubleshoot a missing payment provider > Troubleshoot buy now, pay later and alternative payment methods | undated | kind: stated | quote check: found (markup removed)
- quote: The third-party provider list in your Shopify admin is filtered based on your store's address in Settings > General
- title: Configuring third-party payment providers
- the page opens: If you're not using Shopify Payments and you want to accept credit cards, then you can choose from over 100 credit card payment providers for your Shopify store. You can activate or change a payment provider from the Payments page of your Shopify admin. Depending on the requirements of the payment provider, you might be required to submit and verify your bank account information with them so that your store can complete transactions. Contact your payment provider to confirm whether or not you ca…
- a note box: Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner.
- a note box: Note Only the store owner can add a payment provider.
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Configuring third-party payment providers > Troubleshoot a missing payment provider {#troubleshoot-missing-provider}
- in context: … PayPal account. PayPal Wallet is available to merchants in the United States and France who use Shopify Payments. If you're in one of these regions and have Shopify Payments active, then PayPal isn't available in the Additional payment methods section, it's integrated through Shopify Payments instead. Learn more about PayPal Wallet for the United States or PayPal Wallet for France. Troubleshoot buy now, pay later and alternative payment methods ⟪The third-party provider list in your Shopify admin is filtered based on your store's address in Settings > General⟫. If a provider you expect to find isn't listed, then verify that your store address matches the country or region where the provider operates. Some providers, including regional payment methods, are also configured in the Additional payment methods section rather than through the third-party provider selector. To add these providers, follow the steps to activate additional payment methods. Troubleshoot credit card payment providers The path to a…  (matched markup removed)

### Q5-SH-K1700

**Cited at:** section 1, line 11

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-076
- placement: decides
- structure: https://shopify.dev/docs/apps/build/payments.md
- identifier: Extensions for payments, note
- statement: The option to build a custom payment extensions is limited to eligible Shopify Plus Merchants only.
- scope: eligible Shopify Plus merchants
- cite_ids: SH-S-0441
- note: first run's citation

**Citation SH-S-0441:** `https://shopify.dev/docs/apps/build/payments.md` | Extensions for payments, note | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The option to build a custom payment extensions is limited to eligible Shopify Plus Merchants only.
- title: Extensions for payments
- the page opens: Payments extensions integrate with the Shopify admin and checkout to provide customized payment processing services for merchants. Only approved Partners can build payments extensions on Shopify's Payments Platform. Payments extensions provide merchant stores with the following features: * provide additional payment methods * perform specific operations on payment methods * control payment security for buyers * automate payment services, such as reoccurring payments * decide if they want to capt…
- headings: Extensions for payments
- in context: …ns) * control [payment security](https://shopify.dev/docs/apps/build/payments/requirements#payment-security) for buyers * automate payment services, such as reoccurring payments * decide if they want to capture funds at the time of purchase or at the time of fulfillment. For more information, refer to [Payment authorization](https://help.shopify.com/en/manual/payments/payment-authorization#set-up-manual-capture-of-credit-card-payments) **Note:** ⟪The option to build a custom payment extensions is limited to eligible Shopify Plus Merchants only.⟫ Contact Shopify Plus Support to confirm eligibility. *** ## How it works You can [create a payments extension](https://shopify.dev/docs/apps/build/payments/offsite/use-the-cli) to provide customized payment processing services for merchants, and install your payments extension on a dev store to test it. Only [approved Partners](https://shopify.dev/docs/apps/build/payments/payments-extension-review) can build payments extensions on Shopify's Paym…

### Q5-SH-K1532

**Cited at:** section 1, line 12

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-063
- placement: where
- structure: https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/eligibility.md
- identifier: help.shopify.com/en/manual/payments/shopify-payments/onboarding/eligibility.md
- statement: Shopify Payments is an integrated payment gateway offered by Shopify. Only eligible merchants can use Shopify Payments.
- cite_ids: SH-S-0325
- note: first run's citation

**Citation SH-S-0325:** `https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/eligibility.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/065-help.shopify.com/text.txt` (6616 bytes), fetched 2026-10-11T06:13:02Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/034-help.shopify.com/text.txt` (6616 bytes), fetched 2026-10-12T10:50:12Z, captured
- quote: Shopify Payments is an integrated payment gateway offered by Shopify. Only eligible merchants can use Shopify Payments.
- title: Shopify Payments eligibility
- the page opens: Shopify Payments is an integrated payment gateway offered by Shopify. Only eligible merchants can use Shopify Payments. To be eligible for Shopify Payments, you must meet the following criteria: * Your business is located in a supported country. * Your business type and products aren't prohibited. * You comply with all applicable laws, regulations, and the Shopify Payments terms and conditions for your country and industry. * You must be at least 18 years old to set up a Shopify Payments account…
- headings: Shopify Payments eligibility
- in context: # Shopify Payments eligibility ⟪Shopify Payments is an integrated payment gateway offered by Shopify. Only eligible merchants can use Shopify Payments.⟫ To be eligible for Shopify Payments, you must meet the following criteria: * Your business is located in a [supported country](/manual/payments/shopify-payments/supported-countries/index). * Your business type and products aren't prohibited. * You comply with all applicable laws, regulations, and the [Shopify Payments terms and conditions](https://www.shopify.com/legal) for your country and industry. * You must be at least 18 years old to set up…

### Q5-SH-008

**Cited at:** section 1, line 13; section 2, line 72; section 2, line 86

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-008
- bears_on: 1
- identifier: Activate a credit card payment provider
- statement: You can have only one credit card payment provider activated at a time.
- cite_ids: Q5-SH-C011
- from: held

**Citation Q5-SH-C011:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md` | Activate a credit card payment provider | undated | kind: stated | quote check: found
- quote: You can have only one credit card payment provider activated at a time.
- title: Configuring third-party payment providers
- the page opens: If you're not using Shopify Payments and you want to accept credit cards, then you can choose from over 100 credit card payment providers for your Shopify store. You can activate or change a payment provider from the Payments page of your Shopify admin. Depending on the requirements of the payment provider, you might be required to submit and verify your bank account information with them so that your store can complete transactions. Contact your payment provider to confirm whether or not you ca…
- a note box: Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner.
- a note box: Note Only the store owner can add a payment provider.
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Configuring third-party payment providers > Activate a credit card payment provider {#activate-credit-card-provider}
- in context: … confirm whether or not you can accept payments from your customers before providing your bank account information. <aside class="note note-growth"><h4>Grow your business</h4><p>If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about <a href="/en/manual/partner-directory">hiring a Shopify Partner</a>.</p> </aside> ## Activate a credit card payment provider {#activate-credit-card-provider} ⟪You can have only one credit card payment provider activated at a time.⟫ If you already have a provider activated, then you can [change your credit card payment provider](#change-credit-card-provider). <aside class="note"><h4>Note</h4><p>Only the <a href="/en/manual/your-account">store owner</a> can add a payment provider.</p> </aside> #### Steps: <div class="sections"><details open><summary id="desktop">Desktop</summary><ol> <li><p>From your Shopify admin, go to <strong>Settings</strong> > <a href="https://admin.sho…

### Q5-SH-K1696

**Cited at:** section 1, line 14; section 2, line 61; section 7, line 161

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-076
- placement: decides
- structure: https://shopify.dev/docs/apps/build/payments.md
- identifier: Extensions for payments, introduction
- statement: Only approved Partners can build payments extensions on Shopify's Payments Platform.
- cite_ids: SH-S-0440
- note: first run's citation

**Citation SH-S-0440:** `https://shopify.dev/docs/apps/build/payments.md` | Extensions for payments, introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: Only approved Partners can build payments extensions on Shopify's Payments Platform.
- title: Extensions for payments
- the page opens: Payments extensions integrate with the Shopify admin and checkout to provide customized payment processing services for merchants. Only approved Partners can build payments extensions on Shopify's Payments Platform. Payments extensions provide merchant stores with the following features: * provide additional payment methods * perform specific operations on payment methods * control payment security for buyers * automate payment services, such as reoccurring payments * decide if they want to capt…
- headings: Extensions for payments
- in context: --- title: Extensions for payments description: >- Learn how to build payment processing extensions for Shopify's Payments Platform. source_url: html: 'https://shopify.dev/docs/apps/build/payments' md: 'https://shopify.dev/docs/apps/build/payments.md' api_name: payments-apps --- # Extensions for payments Payments extensions integrate with the Shopify admin and checkout to provide customized payment processing services for merchants. ⟪Only approved Partners can build payments extensions on Shopify's Payments Platform.⟫ Payments extensions provide merchant stores with the following features: * provide additional [payment methods](#supported-payment-methods) * perform specific [operations on payment methods](#supported-payment-operations) * control [payment security](https://shopify.dev/docs/apps/build/payments/requirements#payment-security) for buyers * automate payment services, such as reoccurring payments * decide if they want to capture funds at the time of…

### Q5-SH-062

**Cited at:** section 1, line 14; section 2, line 62; section 3, line 114

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-062
- bears_on: 1;3
- identifier: New Payments Application Feature Approval
- statement: New Payments Application Feature Approval. Any updates or changes to an existing Payments Application, including the addition of new product features or new payment methods, must be submitted for review and approval.
- cite_ids: Q5-SH-C097
- from: held

**Citation Q5-SH-C097:** `https://www.shopify.com/partners/terms` | C.4. Additional Terms Applicable to Payments Developers, New Payments Application Feature Approval | 2026-02-27 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/152-shopify.com/text.txt` (137217 bytes), fetched 2026-10-11T06:13:12Z, captured
- quote: New Payments Application Feature Approval. Any updates or changes to an existing Payments Application, including the addition of new product features or new payment methods, must be submitted for review and approval.
- title: Shopify Partner Program - Partner Program Agreement - Shopify
- in context: … Developer Guidelines and best practices that Payments Developers must follow. Every Payments Developer must adhere to these guidelines and every Payments Application must meet the technical and other specifications that it describes. Sync Data to Shopify. All payments and order data received from transactions processed on the Payments Application must be automatically synced to Shopify as specified in the Payments Platform Developer Guidelines. ⟪New Payments Application Feature Approval. Any updates or changes to an existing Payments Application, including the addition of new product features or new payment methods, must be submitted for review and approval.⟫ Merchant Flexibility. Payments Applications must allow for Shopify Merchants to terminate their agreement with the payment provider within 7 days' notice, without any penalty, fine, or other consequence. Settlements. All Payments Applications must settle transactions for the Merchants within a maximum of 5 days, as outlined in the Payments Platform Developer Guidelines. Wind Down Period. If Payments Developer wishes to no longer support the Paym…

### Q5-SH-058

**Cited at:** section 1, line 14; section 2, line 61

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-058
- bears_on: 1
- identifier: How a merchant installs a payments extension
- statement: 1. The payments app is installed by merchants directly through an installation link that's shared by the payments developer, or through Shopify's public list of payment gateways in the Shopify admin. 2. The merchant installs the app on the OAuth grant page. 3. The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. The app marks itself as ready by calling the Shopify API. 6. Shopify enables the app to be activated by the merchant in the Shopify admin. 7. The merchant activates the app. 8. The merchant deactivates the legacy payment gateway to avoid duplicate payment methods during checkout, if applicable.
- cite_ids: Q5-SH-C082;Q5-SH-C083;Q5-SH-C084;Q5-SH-C085;Q5-SH-C086;Q5-SH-C087;Q5-SH-C088;Q5-SH-C089
- from: held

**Citation Q5-SH-C082:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found (markup removed)
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The payments app is installed by merchants directly through an installation link that's shared by the payments developer, or through Shopify's public list of payment gateways in the Shopify admin.
- title: Extensions for payments
- the page opens: Payments extensions integrate with the Shopify admin and checkout to provide customized payment processing services for merchants. Only approved Partners can build payments extensions on Shopify's Payments Platform. Payments extensions provide merchant stores with the following features: * provide additional payment methods * perform specific operations on payment methods * control payment security for buyers * automate payment services, such as reoccurring payments * decide if they want to capt…
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …you publish your payments extensions, your extensions becomes available, and merchants can install and use them in their Shopify stores. How a merchant installs a payments extension The following diagram describes the different phases of the onboarding cycle for payments extensions: A diagram showing the lifecycle of a payments app 1. ⟪The payments app is installed by merchants directly through an installation link that's shared by the payments developer, or through Shopify's public list of payment gateways in the Shopify admin.⟫ 2. The merchant installs the app on the OAuth grant page. 3. The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. The app marks itself as ready by…  (matched markup removed)

**Citation Q5-SH-C083:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The merchant installs the app on the OAuth grant page.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …irectly through an [installation link](https://shopify.dev/docs/apps/build/payments/onboard-a-merchant-payments-extension#payments-app-installation-url) that's shared by the payments developer, or through [Shopify's public list of payment gateways](https://help.shopify.com/manual/payments/alternative-payments) in the Shopify admin. 2. ⟪The merchant installs the app on the OAuth grant page.⟫ 3. The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. The app marks itself as ready by calling the Shopify API. 6. Shopify enables the app to be…

**Citation Q5-SH-C084:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …/docs/apps/build/payments/onboard-a-merchant-payments-extension#payments-app-installation-url) that's shared by the payments developer, or through [Shopify's public list of payment gateways](https://help.shopify.com/manual/payments/alternative-payments) in the Shopify admin. 2. The merchant installs the app on the OAuth grant page. 3. ⟪The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments.⟫ 4. The merchant configures the payments app. 5. The app marks itself as ready by calling the Shopify API. 6. Shopify enables the app to be activated by the merchant in the Shopify admin. 7. The merchant activates the app. 8. The merchant [deactivates the legacy payment gateway](https://help.shopify.com/manual/payments/alternative-paym…

**Citation Q5-SH-C085:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The merchant configures the payments app.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …/help.shopify.com/manual/payments/alternative-payments) in the Shopify admin. 2. The merchant installs the app on the OAuth grant page. 3. The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. ⟪The merchant configures the payments app.⟫ 5. The app marks itself as ready by calling the Shopify API. 6. Shopify enables the app to be activated by the merchant in the Shopify admin. 7. The merchant activates the app. 8. The merchant [deactivates the legacy payment gateway](https://help.shopify.com/manual/payments/alternative-payments) to avoid duplicate payment methods duri…

**Citation Q5-SH-C086:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The app marks itself as ready by calling the Shopify API.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …-payments) in the Shopify admin. 2. The merchant installs the app on the OAuth grant page. 3. The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. ⟪The app marks itself as ready by calling the Shopify API.⟫ 6. Shopify enables the app to be activated by the merchant in the Shopify admin. 7. The merchant activates the app. 8. The merchant [deactivates the legacy payment gateway](https://help.shopify.com/manual/payments/alternative-payments) to avoid duplicate payment methods during checkout, if applicable. *** ## Where you can build Paymen…

**Citation Q5-SH-C087:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: Shopify enables the app to be activated by the merchant in the Shopify admin.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: … app on the OAuth grant page. 3. The merchant is redirected to the payments app page to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. The app marks itself as ready by calling the Shopify API. 6. ⟪Shopify enables the app to be activated by the merchant in the Shopify admin.⟫ 7. The merchant activates the app. 8. The merchant [deactivates the legacy payment gateway](https://help.shopify.com/manual/payments/alternative-payments) to avoid duplicate payment methods during checkout, if applicable. *** ## Where you can build Payments extensions integrate with Shopify checkout to process payments during the cust…

**Citation Q5-SH-C088:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The merchant activates the app.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …age to configure the payments app settings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. The app marks itself as ready by calling the Shopify API. 6. Shopify enables the app to be activated by the merchant in the Shopify admin. 7. ⟪The merchant activates the app.⟫ 8. The merchant [deactivates the legacy payment gateway](https://help.shopify.com/manual/payments/alternative-payments) to avoid duplicate payment methods during checkout, if applicable. *** ## Where you can build Payments extensions integrate with Shopify checkout to process payments during the customer's purchase flow. [Checkout\ \ …

**Citation Q5-SH-C089:** `https://shopify.dev/docs/apps/build/payments.md` | How it works > How a merchant installs a payments extension | 2026-10-11 | kind: stated | quote check: found (markup removed)
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: The merchant deactivates the legacy payment gateway to avoid duplicate payment methods during checkout, if applicable.
- title, opening and note boxes: as for this source's citation above
- headings: Extensions for payments > How it works > How a merchant installs a payments extension
- in context: …ettings. Until configuration is complete, a banner indicates that the provider isn't ready to process payments. 4. The merchant configures the payments app. 5. The app marks itself as ready by calling the Shopify API. 6. Shopify enables the app to be activated by the merchant in the Shopify admin. 7. The merchant activates the app. 8. ⟪The merchant deactivates the legacy payment gateway to avoid duplicate payment methods during checkout, if applicable.⟫ * Where you can build Payments extensions integrate with Shopify checkout to process payments during the customer's purchase flow. Checkout Provide payment processing services for merchants on checkout, including credit card, alternative, offsite, and redeemable payment methods. * Build options There are five types of payments extensi…  (matched markup removed)

### Q5-SH-086

**Cited at:** section 1, line 15; section 7, line 162

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-086
- bears_on: 1;5
- identifier: Payments
- statement: ONERWAY (Direct) Test mode 0.6% transaction fee • Card rates set by ONERWAY (Direct)
- scope: store fake-demo-sharrwah, observed 2026-10-05; countryCode YE, currencyCode YER
- cite_ids: Q5-SH-C130;Q5-SH-C128
- from: held

**Citation Q5-SH-C130:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/steps/376.text.txt` | step 376 | 2026-10-05 | kind: observed | quote check: found
- step 376: visit route payments:settings (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:index,payments:settings:secondary-gateways) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/payments | "My Store · Payments · Shopify" | 2026-10-05T04:40:05.144Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/376.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/376.html`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/376.text.txt`
- quote: ONERWAY (Direct) Test mode 0.6% transaction fee • Card rates set by ONERWAY (Direct)
- in context: …Customers Growth Discounts Content Markets Analytics Sales channels Apps Settings MS Settings [Search] My Store fake-demo-sharrwah.myshopify.com MS General Plan Billing Users Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com Payments Payments Submit ⟪ONERWAY (Direct) Test mode 0.6% transaction fee • Card rates set by ONERWAY (Direct)⟫ Payment methods +4 Testing ONERWAY (Direct) transactions. No actual transactions will be processed. More ways to pay Offer methods processed offsite or through custom checkout integrations Add Payment configuration Payment capture method Manual payment methods Payment method customizations Gift card expiration Apple Wallet passes Learn more about payments Recents Where should we begin? Work with Sidekick

**Citation Q5-SH-C128:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/PaymentProviders/cc5519fabb7661cc9b8bdb071e16e1af58ad4ab46536df9a12a0e37f20c3ba5a.json` | operation PaymentProviders, store fake-demo-sharrwah, step 376 | 2026-10-05 | kind: observed | quote check: found
- quote: "url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …tedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"GIFT_CARDS_ONLY","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"FORCED_MIGRATION","accountOwner":{"id":"gid://shopify/StaffMember/165290082519","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":false,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings"…

### Q5-SH-071

**Cited at:** section 1, line 17

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-071
- bears_on: 1
- identifier: Adyen
- statement: Only organizations with an existing Adyen approval can use Adyen on Shopify. Approved organizations keep their current access with no change to how they process payments. Organizations without an approval can't activate Adyen.
- cite_ids: Q5-SH-C110
- from: held

**Citation Q5-SH-C110:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/adyen-gateway.md` | Eligibility requirements for Adyen on Shopify | undated | kind: stated | quote check: found
- quote: Only organizations with an existing Adyen approval can use Adyen on Shopify. Approved organizations keep their current access with no change to how they process payments. Organizations without an approval can't activate Adyen.
- title: Using Adyen on Shopify
- the page opens: Adyen is a payment gateway that you can use to accept payments in Shopify. Access to the Adyen payment app is limited to organizations with an existing Adyen approval. If your organization has approval, then you can use your Adyen account as your payment processor directly within Shopify. You can integrate Shopify, including Adyen's payments data, with your Enterprise Resource Planning (ERP) software to ensure smoother data management and synchronization between your systems. Caution Shopify Sup…
- a note box: Caution Shopify Support can help you configure and use Adyen with Shopify, but can't provide advice on legal, tax, or compliance matters. For questions about regulations, payouts, chargebacks, or fraud prevention strategies, contact Adyen directly or consult a qualified professional.
- a note box: Caution Activating Adyen as your primary payment gateway deactivates Shopify Payments. Make sure this aligns with your payment strategy before proceeding.
- a note box: Note If you don't have an Adyen account when you add the Adyen payment integration to your Shopify store, then you can't activate it or process payments. Reach out to your Shopify Sales Representative or Customer Success Manager (CSM) for more details.
- headings: Using Adyen on Shopify > Eligibility requirements for Adyen on Shopify {#eligibility}
- in context: …t and synchronization between your systems. <aside class="note note-caution"><h4>Caution</h4><p>Shopify Support can help you configure and use Adyen with Shopify, but can't provide advice on legal, tax, or compliance matters. For questions about regulations, payouts, chargebacks, or fraud prevention strategies, contact Adyen directly or consult a qualified professional.</p> </aside> ## Eligibility requirements for Adyen on Shopify {#eligibility} ⟪Only organizations with an existing Adyen approval can use Adyen on Shopify. Approved organizations keep their current access with no change to how they process payments. Organizations without an approval can't activate Adyen.⟫ [Shopify Payments](/manual/payments/shopify-payments) is the recommended payment solution for those merchants. If your organization has an existing Adyen approval, then your store must also meet the following requirements: * You must have an existing [Adyen account](https://www.adyen.com/) set up before activating the integration. * Your store must use [Shopify Checkout](/manual/checkout-settings). ## Incompatible or unavailable features for Ady…

### Q5-SH-K2262

**Cited at:** section 1, line 18; section 3, line 106

**The same record as Q2-SH-K2262,** whose card is in `Q2-shopify-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers.
- scope: 

### Q5-SH-078

**Cited at:** section 1, line 19

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-078
- bears_on: 1;2
- identifier: ShopifyPaymentsData: businessEntity.shopifyPayments.eligible
- statement: "shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","name":"Shopify Payments","eligible":false
- scope: store ibx5bt-xy, observed 2026-09-30; countryCode YE, currencyCode YER
- cite_ids: Q5-SH-C119;Q5-SH-C121
- from: held

**Citation Q5-SH-C119:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/ShopifyPaymentsData/abc0847e84ab6807c3f42c30ef058d058e4b7f15c1f7feb9a7044d4d5930323e.json` | operation ShopifyPaymentsData, store ibx5bt-xy, step 21 | 2026-09-30 | kind: observed | quote check: found
- quote: "shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","name":"Shopify Payments","eligible":false
- in context: {"data":{"businessEntity":{"id":"gid://shopify/BusinessEntity/43774968021",⟪"shopifyPayments":{"id":"gid://shopify/PaymentProvider/87","name":"Shopify Payments","eligible":false⟫,"cardPresentSupported":false,"transactionFee":0.0,"discountedTransactionFee":0.0,"discountedTransactionFeeEndedAt":"2026-10-02T06:00:00Z","idVerificationForOnboardingRequired":false,"idVerificationOutcome":null,"missingAttributesInfo":null,"paymentMethods":[{"name":"visa","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"mastercard","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"american_express","type":"CREDIT_CARD","__ty…

**Citation Q5-SH-C121:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/PaymentProviders/4ae7c72495e354101e770599f12d4bdd21130619d0db42a5d30074fe74ff94c4.json` | operation PaymentProviders, store ibx5bt-xy, step 22 | 2026-09-30 | kind: observed | quote check: found
- quote: "url":"https://ibx5bt-xy.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …:{"unprotectedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"AUTO","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://ibx5bt-xy.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/165097275605","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":true,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings":{"id":"g…

### Q5-SH-094

**Cited at:** section 1, line 19

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-094
- bears_on: 1;3
- identifier: Payments · Third-party payment providers
- statement: (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]
- scope: store ibx5bt-xy, observed 2026-09-30; countryCode YE, currencyCode YER
- cite_ids: Q5-SH-C142;Q5-SH-C143;Q5-SH-C144;Q5-SH-C145;Q5-SH-C146;Q5-SH-C147;Q5-SH-C121
- from: held
- note: In the saved HTML of step 387 of run 20260930T045741Z-sweep-trial2. The step's aria.yaml shows the same six provider names and Supports 3DS, but not the card labels.

**Citation Q5-SH-C142:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt` | run 20260930T045741Z-sweep-trial2, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T07:58:14.608Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt`
- quote: (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club]
- in context: …stomer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Third-party payment providers] [accessibilitylabel: Payments] [label: Search] [placeholder: Filter third-party payment providers] ⟪(for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club]⟫ [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [acce…

**Citation Q5-SH-C143:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt` | run 20260930T045741Z-sweep-trial2, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T07:58:14.608Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt`
- quote: [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay]
- title, opening and note boxes: as for this source's citation above
- in context: …[accessibilitylabel: Payments] [label: Search] [placeholder: Filter third-party payment providers] (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] ⟪[accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay]⟫ Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [a…

**Citation Q5-SH-C144:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt` | run 20260930T045741Z-sweep-trial2, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T07:58:14.608Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt`
- quote: Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro]
- title, opening and note boxes: as for this source's citation above
- in context: …s] (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] ⟪Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro]⟫ ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessi…

**Citation Q5-SH-C145:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt` | run 20260930T045741Z-sweep-trial2, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T07:58:14.608Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt`
- quote: ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro]
- title, opening and note boxes: as for this source's citation above
- in context: …] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ⟪ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro]⟫ PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibility…

**Citation Q5-SH-C146:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt` | run 20260930T045741Z-sweep-trial2, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T07:58:14.608Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt`
- quote: PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper]
- title, opening and note boxes: as for this source's citation above
- in context: …iscover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] ⟪PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper]⟫ Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit] Learn more about third-party payment providers Close

**Citation Q5-SH-C147:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt` | run 20260930T045741Z-sweep-trial2, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T07:58:14.608Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/387.html.txt`
- quote: Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]
- title, opening and note boxes: as for this source's citation above
- in context: …can Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] ⟪Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]⟫ Learn more about third-party payment providers Close

**Citation Q5-SH-C121:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/PaymentProviders/4ae7c72495e354101e770599f12d4bdd21130619d0db42a5d30074fe74ff94c4.json` | operation PaymentProviders, store ibx5bt-xy, step 22 | 2026-09-30 | kind: observed | quote check: found
- quote: "url":"https://ibx5bt-xy.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …ttings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"AUTO","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://ibx5bt-xy.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/165097275605","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":true,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEnt…

### Q5-SH-K1555

**Cited at:** section 1, line 23; section 7, line 159; section 8, line 176; section 8, line 182

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-064
- placement: where
- structure: https://www.shopify.com/legal/terms-shopify-payments
- identifier: Part I, A. The Payment Processor
- statement: The processing and settlement of Transactions ("Payment Processing") is carried out by one or more Payment Processors and any of its Financial Services Providers under the separate terms of service identified in the Payment Processor List (the "Payment Processor Terms").
- cite_ids: SH-S-0082
- note: first run's citation

**Citation SH-S-0082:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, A. The Payment Processor | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (90053 bytes), fetched 2026-10-11T06:13:11Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (90053 bytes), fetched 2026-10-12T10:51:25Z, captured
- quote: The processing and settlement of Transactions ("Payment Processing") is carried out by one or more Payment Processors and any of its Financial Services Providers under the separate terms of service identified in the Payment Processor List (the "Payment Processor Terms").
- title: Shopify Payments Terms of Service - Shopify
- in context: …f this Agreement, and you agree to the Payment Facilitator Terms by accepting this Agreement. The Payment Processor. The Payment Processor under this Agreement may be one or more of the entities identified for your Designated Country in the Payment Processor list available here (the "Payment Processor List"). Each Payment Processor may offer their services as an agent of one or more financial institutions (each, a "Financial Services Provider"). ⟪The processing and settlement of Transactions ("Payment Processing") is carried out by one or more Payment Processors and any of its Financial Services Providers under the separate terms of service identified in the Payment Processor List (the "Payment Processor Terms").⟫ By accepting this Agreement, you are also accepting and agreeing to be bound by all of the Payment Processor Terms applicable in your Designated Country, which, in each case, is a legal agreement between you and the applicable Payment Processor. Shopify is not a party to any of the Payment Processor Terms and is not liable to you in respect thereof. By accepting this Agreement and the Payment Processor Terms for your Designated Country you are a…

### Q5-SH-006

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-006
- bears_on: 1;3
- identifier: Third-party payment providers
- statement: To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store. You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods.
- cite_ids: Q5-SH-C006;Q5-SH-C007
- from: held

**Citation Q5-SH-C006:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers.md` | Third-party payment providers | undated | kind: stated | quote check: found (markup removed)
- quote: To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store.
- title: Third-party payment providers
- the page opens: To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store. You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods. Shopify supports two different types of credit card payment providers: direct providers and external providers. If you're using a direct provider, then your …
- a note box: Note Third-party transaction fees apply to all transactions processed through third-party and alternate payment gateways, even when Shopify Payments is activated. However, if you elect to use Shopify Payments as your primary payment provider, then PayPal transactions are exempt from third-party tran
- a note box: Tip To see more videos, visit our YouTube channel.
- headings: Third-party payment providers
- in context: Third-party payment providers ⟪To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store.⟫ You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods. Shopify supports two different types of credit card payment providers: direct providers and external providers. If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a…  (matched markup removed)

**Citation Q5-SH-C007:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers.md` | Third-party payment providers | undated | kind: stated | quote check: found (markup removed)
- quote: You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods.
- title, opening and note boxes: as for this source's citation above
- headings: Third-party payment providers
- in context: Third-party payment providers To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store. ⟪You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods.⟫ Shopify supports two different types of credit card payment providers: direct providers and external providers. If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a third-party checkout. If you're using an external provider, then your customers must complete their purchases on a checkout page that's hosted outside of your online store. Note Third-party transa…  (matched markup removed)

### Q5-SH-027

**Cited at:** section 1, line 25; section 2, line 55

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-027
- bears_on: 3;5
- identifier: Manual payments
- statement: You can accept manual payments outside of your online checkout, such as money orders or bank transfers.
- cite_ids: Q5-SH-C031
- from: held

**Citation Q5-SH-C031:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/getting-paid.md` | How you get paid | undated | kind: stated | quote check: found (markup removed)
- quote: You can accept manual payments outside of your online checkout, such as money orders or bank transfers.
- title: Getting paid
- the page opens: All Shopify-supported payment methods rely on third-party providers to process your transactions. These providers might charge extra fees and enforce rules about what products you can sell using their service. When you set up a payment method, check with the company providing the service to make sure you understand their rules and fees. How you get paid When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the c…
- a note box: Note Payouts aren't sent on bank holidays.
- headings: Getting paid > How you get paid
- in context: …ayments, each payment must be processed, so there's usually a delay between when the customer pays for their order and when you receive the payment. After the payment is processed, the purchase amount is transferred to your merchant account. Some payment providers, such as PayPal Express Checkout, have their own methods of transferring funds from your customer to you. Check with the payment provider that you're using to confirm how they pay you. ⟪You can accept manual payments outside of your online checkout, such as money orders or bank transfers.⟫ If you don't activate Shopify Payments as your payment provider, then you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify. This includes all orders that go through Shopify's checkout system. If you've activated Shopify Payments, then you receive payouts when customers pay using Shopify Payments or specific accelerated checkouts. If customers pay using third-party payment gateways, then you can't…  (matched markup removed)

### Q5-SH-083

**Cited at:** section 1, line 25; section 2, line 56

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-083
- bears_on: 3
- identifier: PaymentProviders: businessEntity.manualProviders
- statement: "manualProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/140","name":"Cash on Delivery (COD)","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/141","name":"Money Order","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/142","name":"Bank Deposit","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"}],"__typename":"PaymentProviderConnection"}
- scope: store ibx5bt-xy, observed 2026-09-30; countryCode YE, currencyCode YER
- cite_ids: Q5-SH-C125;Q5-SH-C126;Q5-SH-C127;Q5-SH-C121
- from: held

**Citation Q5-SH-C125:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/PaymentProviders/4ae7c72495e354101e770599f12d4bdd21130619d0db42a5d30074fe74ff94c4.json` | operation PaymentProviders, store ibx5bt-xy, step 22 | 2026-09-30 | kind: observed | quote check: found
- quote: "manualProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/140","name":"Cash on Delivery (COD)","group":"MANUAL"
- in context: …d50be1c61c0a540b0c01ad6c21256b"},"transactionFee":0.0,"url":"https://www.paypal.com/us/home","configuration":null,"__typename":"PaymentProvider"},"stripe":{"id":"gid://shopify/PaymentProvider/67","available":false,"eligible":false,"configuration":null,"__typename":"PaymentProvider"},"thirdPartyPaymentProviders":{"edges":[],"__typename":"PaymentProviderConnection"},"additionalPaymentProviders":{"edges":[],"__typename":"PaymentProviderConnection"},⟪"manualProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/140","name":"Cash on Delivery (COD)","group":"MANUAL"⟫,"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/141","name":"Money Order","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/142","name":"Bank Deposit","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"}],"__t…

**Citation Q5-SH-C126:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/PaymentProviders/4ae7c72495e354101e770599f12d4bdd21130619d0db42a5d30074fe74ff94c4.json` | operation PaymentProviders, store ibx5bt-xy, step 22 | 2026-09-30 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/141","name":"Money Order","group":"MANUAL"
- title, opening and note boxes: as for this source's citation above
- in context: …ligible":false,"configuration":null,"__typename":"PaymentProvider"},"thirdPartyPaymentProviders":{"edges":[],"__typename":"PaymentProviderConnection"},"additionalPaymentProviders":{"edges":[],"__typename":"PaymentProviderConnection"},"manualProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/140","name":"Cash on Delivery (COD)","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/141","name":"Money Order","group":"MANUAL"⟫,"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/142","name":"Bank Deposit","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"}],"__typename":"PaymentProviderConnection"},"entityCustomPaymentMethods":{"edges":[],"__typename":"CustomPaymentMethodConnection"},"__typename":"BusinessEntity"},"legacySubscriptionGa…

**Citation Q5-SH-C127:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/PaymentProviders/4ae7c72495e354101e770599f12d4bdd21130619d0db42a5d30074fe74ff94c4.json` | operation PaymentProviders, store ibx5bt-xy, step 22 | 2026-09-30 | kind: observed | quote check: found
- quote: {"node":{"id":"gid://shopify/PaymentProvider/142","name":"Bank Deposit","group":"MANUAL"
- title, opening and note boxes: as for this source's citation above
- in context: …s":{"edges":[],"__typename":"PaymentProviderConnection"},"manualProviders":{"edges":[{"node":{"id":"gid://shopify/PaymentProvider/140","name":"Cash on Delivery (COD)","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},{"node":{"id":"gid://shopify/PaymentProvider/141","name":"Money Order","group":"MANUAL","configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"},⟪{"node":{"id":"gid://shopify/PaymentProvider/142","name":"Bank Deposit","group":"MANUAL"⟫,"configuration":null,"__typename":"PaymentProvider"},"__typename":"PaymentProviderEdge"}],"__typename":"PaymentProviderConnection"},"entityCustomPaymentMethods":{"edges":[],"__typename":"CustomPaymentMethodConnection"},"__typename":"BusinessEntity"},"legacySubscriptionGateway":null,"customPaymentMethods":{"edges":[],"__typename":"CustomPaymentMethodConnection"},"resourceAlerts":[]},"extensions":{"cost":{"requestedQueryCost":109,"actualQueryCost"…

**Citation Q5-SH-C121:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T074710Z-m0-account/answers/admin.shopify.com/PaymentProviders/4ae7c72495e354101e770599f12d4bdd21130619d0db42a5d30074fe74ff94c4.json` | operation PaymentProviders, store ibx5bt-xy, step 22 | 2026-09-30 | kind: observed | quote check: found
- quote: "url":"https://ibx5bt-xy.myshopify.com","countryCode":"YE","currencyCode":"YER"
- title, opening and note boxes: as for this source's citation above
- in context: …:{"unprotectedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"AUTO","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://ibx5bt-xy.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/165097275605","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":true,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings":{"id":"g…

### Q5-SH-K1694

**Cited at:** section 1, line 26; section 2, line 63; section 3, line 98

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-076
- placement: where
- structure: https://shopify.dev/docs/apps/build/payments.md
- identifier: Build options
- statement: There are five types of payments extensions:
- cite_ids: SH-S-0445
- note: first run's citation

**Citation SH-S-0445:** `https://shopify.dev/docs/apps/build/payments.md` | Build options | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt` (9416 bytes), fetched 2026-10-11T06:13:08Z, captured
- quote: There are five types of payments extensions:
- title: Extensions for payments
- the page opens: Payments extensions integrate with the Shopify admin and checkout to provide customized payment processing services for merchants. Only approved Partners can build payments extensions on Shopify's Payments Platform. Payments extensions provide merchant stores with the following features: * provide additional payment methods * perform specific operations on payment methods * control payment security for buyers * automate payment services, such as reoccurring payments * decide if they want to capt…
- headings: Extensions for payments > Build options
- in context: …ent methods during checkout, if applicable. *** ## Where you can build Payments extensions integrate with Shopify checkout to process payments during the customer's purchase flow. [Checkout\ \ ](https://shopify.dev/docs/apps/build/checkout) [Provide payment processing services for merchants on checkout, including credit card, alternative, offsite, and redeemable payment methods.](https://shopify.dev/docs/apps/build/checkout) *** ## Build options ⟪There are five types of payments extensions:⟫ * **Credit card payment extensions**: Allows merchants to accept credit card purchases on their checkout. This extension type also support 3D Secure Authentication. * **Credit card with UI extensibility:** Allows Partners to define additional fields required for processing credit card payments. Partners can collect information, such as installment details, directly on checkout before a payment is initiated. * **Custom credit card payment extensi…

### Q5-SH-007

**Cited at:** section 1, line 27; section 2, line 62; section 5, line 132

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-007
- bears_on: 3;5
- identifier: direct providers; external providers
- statement: Shopify supports two different types of credit card payment providers: direct providers and external providers. If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a third-party checkout. If you're using an external provider, then your customers must complete their purchases on a checkout page that's hosted outside of your online store.
- cite_ids: Q5-SH-C008;Q5-SH-C009;Q5-SH-C010
- from: held

**Citation Q5-SH-C008:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers.md` | Third-party payment providers | undated | kind: stated | quote check: found (markup removed)
- quote: Shopify supports two different types of credit card payment providers: direct providers and external providers.
- title: Third-party payment providers
- the page opens: To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store. You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods. Shopify supports two different types of credit card payment providers: direct providers and external providers. If you're using a direct provider, then your …
- a note box: Note Third-party transaction fees apply to all transactions processed through third-party and alternate payment gateways, even when Shopify Payments is activated. However, if you elect to use Shopify Payments as your primary payment provider, then PayPal transactions are exempt from third-party tran
- a note box: Tip To see more videos, visit our YouTube channel.
- headings: Third-party payment providers
- in context: Third-party payment providers To accept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store. You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods. ⟪Shopify supports two different types of credit card payment providers: direct providers and external providers.⟫ If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a third-party checkout. If you're using an external provider, then your customers must complete their purchases on a checkout page that's hosted outside of your online store. Note Third-party transaction fees apply to all transactions processed through third-party and alternate payment gateways, even when Sho…  (matched markup removed)

**Citation Q5-SH-C009:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers.md` | Third-party payment providers | undated | kind: stated | quote check: found (markup removed)
- quote: If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a third-party checkout.
- title, opening and note boxes: as for this source's citation above
- headings: Third-party payment providers
- in context: …cept credit cards through a provider other than Shopify Payments, choose from over 100 credit card payment providers for your Shopify store. You can use a third-party provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods. Shopify supports two different types of credit card payment providers: direct providers and external providers. ⟪If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a third-party checkout.⟫ If you're using an external provider, then your customers must complete their purchases on a checkout page that's hosted outside of your online store. Note Third-party transaction fees apply to all transactions processed through third-party and alternate payment gateways, even when Shopify Payments is activated. However, if you elect to use Shopify Payments as your primary payment provider, then PayPal transactions are exempt from third-party tr…  (matched markup removed)

**Citation Q5-SH-C010:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers.md` | Third-party payment providers | undated | kind: stated | quote check: found (markup removed)
- quote: If you're using an external provider, then your customers must complete their purchases on a checkout page that's hosted outside of your online store.
- title, opening and note boxes: as for this source's citation above
- headings: Third-party payment providers
- in context: …rty provider as your sole credit card processor, or you can use it alongside Shopify Payments to access additional payment methods such as Shop Pay and local payment methods. Shopify supports two different types of credit card payment providers: direct providers and external providers. If you're using a direct provider, then your customers can complete their purchases directly on your online store without having to pay at a third-party checkout. ⟪If you're using an external provider, then your customers must complete their purchases on a checkout page that's hosted outside of your online store.⟫ Note Third-party transaction fees apply to all transactions processed through third-party and alternate payment gateways, even when Shopify Payments is activated. However, if you elect to use Shopify Payments as your primary payment provider, then PayPal transactions are exempt from third-party transaction fees. Learn more about third-party transaction fees. To check the transaction fee rates for your location, refer to the Shopify pricing page …  (matched markup removed)
