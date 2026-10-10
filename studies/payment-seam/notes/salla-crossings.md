# Payments seam on Salla: notes for L_crossings.tsv

Prepared on 2026-10-10 for Sharrwah's question: can payments be its own part of the system behind a narrow, stable contract?

The companion table `L_crossings.tsv` has 81 crossings (L001 to L081). I judge 41 of them essential to commerce in general and 40 specific to Salla's business. Every judgement is marked "(inference)".

## How to read the table

- **Facts and inference.** The `evidence` and `quote` columns are facts. In `notes`, statements that start "Fact:" are facts and statements that start "Inference:" are my judgement. The `essential_or_specific` column is always inference.
- **Direction.** You asked for two values: "core asks payments" and "payments tells core". Many crossings had a different shape, so I added two more:
  - **payments asks core** means payments starts a read of core data, such as the cart, the customer, the plan or the market.
  - **core tells payments** means core pushes an event that payments consumes, such as a delivery that releases a COD payout.

  One row (L056) is navigation and code ownership only. Counts: core asks payments 28, payments tells core 27, payments asks core 21, core tells payments 4, neither 1.
- **Evidence paths** are relative to `/home/user/observed-sa`. Each source shows its capture date.
  - **Dashboard translation files** (`structures/salla/dashboard-translations/{ar,en}/<ns>.json`) are minified one-line JSON. They are cited as `:1 key <json path>`. Arabic quotes from them have Salla's own English string as the translation, marked "EN (Salla's own)".
  - **docs.salla.dev `.md` pages** are cited by URL and line. They are held in `raw/runs/20261005T234928Z-docs-md/fetch.warc.gz`, captured 2026-10-05/06. Five of them were re-fetched live on 2026-10-10 and were byte-identical: webhooks.md, transactions/update.md, payments/available-methods.md, webhook-events/orders.md and checkout-apis/overview.md.
  - **help.salla.sa article bodies** are not held in the repository: the run `20261008T121629Z-help-pages` kept only CDX and URL lists. I fetched 44 articles live on 2026-10-10. They are cited as `https://help.salla.sa/article/x/<id>`, which resolves (the slug is ignored). Canonical URLs and each page's own "last updated" date are in the table at the end. In notes I refer to an article by the first four characters of its id, for example "help lwd3".
- **Quotes** are at most 25 words in the original language. Arabic for dashboard and help sources, English for docs and the /en storefront. Each quote ends with a translation, or "original English". JSON quotes keep Salla's own formatting.
- **Personal data is left out.** No buyer names, phone numbers, IBANs or account numbers are quoted. Run steps that contain them are cited only by the line numbers that hold non-personal text.

## Sources and their dates

| Source | Date |
|---|---|
| docs.salla.dev pages, event lists and data schemas | captured 2026-10-05 and 2026-10-06; schemas through 2026-10-09; live check 2026-10-10 |
| Twilight web components 2.14.587; storefront config and API | 2026-10-06 |
| Dashboard registry, routes, navigation, translations, settings centre, order statuses, onboarding, staff permissions, report catalogue | 2026-10-08 (settings sweep also 2026-10-09) |
| Feature flags (`dashboard-features`) | 2026-10-09 |
| Partners portal: scopes and webhook catalogue | 2026-10-09 |
| Partners portal: navigation | 2026-10-08 |
| Webhook deliveries received by the capture app | 2026-10-09 |
| Storefront journeys: COD guest order (Al Dakheel Oud), bank-transfer order (Khyma Toys), Mahally handoff, merchant-created order on the demo store | 2026-10-09 |
| `derived/*-gates.tsv`, `index/rest-endpoints.tsv` | rebuilt from runs of 2026-10-08 and 2026-10-09 |
| help.salla.sa, 44 articles | fetched live 2026-10-10; each page's own "last updated" date is between 14 Mar 2026 and 7 Oct 2026 |
| salla.com/payments | tried live 2026-10-10; it answered 403 "Just a moment..." (Cloudflare challenge), so it is not used |

## (a) What stays inside payments and never reaches the order or checkout

Each item is a fact with its pointer. The last line of each item, marked "Inference", is my judgement about why it stays inside.

1. **Gateway and provider credentials, and provider onboarding state.** This covers merchant and public keys for Tamara, Tabby, Apple Pay, Tap and the charity gateways (PayTabs etc.), plus the Mokafaa merchant token. It also covers the application status: applied, under review, rejected or failed.
   - Pointer: `dashboard-translations/en/payments.json` keys `gateway_settings.*`, `charity_payments.*`.
   - Inference: the order only ever sees `gateway` and the method slug.
2. **Card entry, 3-D Secure and the saved-card vault.** The order holds `payment_method` and `transaction_reference`, never card data.
   - Pointers: in the run steps, card fields are masked as `[hidden field]` inside the hosted checkout. Saved cards are capped at 5 (help bkg4).
3. **Payment-restriction rule storage and evaluation, and fraud scoring.** Only the outcome crosses: hide, reject with a message, or review (L008). Rejected attempts are listed in the e-payment transactions log, not as orders (help d9me).
4. **Transaction records and their own life cycle.**
   - Statuses: initiated, pending, paid, canceled, refunded, partial_refunded, wallet_refunded.
   - Actions: void and reverse.
   - Fields: `available_actions` and card brand, number and country.
   - Pointers: docs `transactions/details.md`; `payments.json` `common.status.*`.
5. **The merchant's e-payments balance and its fees.**
   - Method fees (Mada, Visa/Mastercard, stc pay), the "checkout experience fee", VAT on fees, and the fee calculator.
   - Pointer: `payments.json` `fees_calculator.*`, `wallet.epayment.*`.
6. **Payouts.**
   - Payout cycle, minimum payout (SAR 100, help da2e), payout invoices with UTI reference numbers, "confirm receipt", and transfers to the payout account.
   - The payout account is tied to verification and is never shown to buyers (help bhrr).
   - Pointer: `payments.json` `wallet.transfer_cycle_invoices.*`.
7. **The COD remittance ledger with carriers.** Collected amounts, carrier COD fees, VAT on fees, and net payouts on Sundays and Wednesdays (help koda; `payments.json` `wallet.cod.*`).
8. **The store wallet's own mechanics.** Top-ups, withdrawal batches on Tuesdays, the daily withdrawal cap and withdrawal fees (help g36c; `payments.json` `wallet.withdraw.*`). What crosses is only the debits and credits listed in L032 to L035.
9. **Transaction-limit tables by country and product type.** Only the limit outcome crosses (L009).
10. **Sandouk Salla financing.** Offers, contracts, the collection rate and statements (`payments.json` `capital.*`). Only the payout deduction is visible elsewhere.
11. **Salla Payments activation and review.** This includes the GCC activation review banner and the rule that Salla Payments cannot run alongside Tap (`payments.json` `gcc_banner.*`).
12. **Chargeback and dispute handling.** Only the liability notice and any deduction surface (L076).
13. **Apple Pay merchant validation.** Only the "connect a domain" prerequisite crosses (L080).
14. **Partner (app developer) payouts and the portal's billing records.** These are Payouts, Billings and Operation records in the Partners portal.
15. **Verification documents (KYC).** IDs, IBAN certificate, commercial registration and the Absher check (help ig4b). Only the status and the verified payout account cross.
    - Inference: in Salla this lives in the payments app. See (b).

Inference: these are about half of what the payments area does, and none of them needs to appear in an order or checkout contract.

## (b) Foundations shared by both sides that are not payments

1. **Money and currency.**
   - Amount-with-currency objects, store currencies, market currency and exchange rates.
   - Pointer: order `amounts`, `currency`, `exchange_rate`, `scope_exchange_rate`; storefront `currencies`.
2. **Tax.**
   - VAT rates per country, tax-inclusive pricing, the product taxable flag with VATEX exemption codes, tax on shipping, tax by market country, tax profiles, and the store VAT number.
   - Fact: `/payments/taxes` is served by `@salla.sa/ui-merchant-shipping`, not the payments app (`dashboard-apps` items.jsonl:14, :21).
3. **Order identity and the order-status catalogue.**
   - Order id, reference_id, cart id, checkout id, and statuses, including the two payment-driven ones.
   - Also order history and refunded-items records.
4. **Customer identity.**
   - Shared Salla Login across stores, guest flag, customer groups, ban list and whitelist flag, and national address.
5. **Merchant and store identity.**
   - Legal entity, commercial registration, VAT number, default branch address, store country, domain, and verification status.
   - Inference: Salla files verification under payments; a shared merchant-identity service would serve payments, ZATCA, Mahally and launch alike.
6. **Plans and entitlements.** Feature flags carrying plans and countries, from the GrowthBook payload in `dashboard-features`.
7. **Staff roles and permissions.** Used by both sides (`staff-permission-groups`, `permission-gates.tsv`).
8. **Markets (scopes)** and the settings framework (`PUT settings/fields/{slug}`).
9. **Product catalogue facts.** Type (product, digital, codes, booking, donating, food, service), categories, weight. Read by COD rules, BNPL eligibility, limits and auto-complete.
10. **Shipping platform.** Carriers, zones (with COD flags and fees), branches (with `is_cod_available`) and shipments.
11. **Documents.** Order invoice templates and rendering, the external invoice provider option, and the ZATCA link.
12. **Notifications.** SMS, email and WhatsApp, used for payment links, refund SMS and wallet notifications.
13. **The app platform and event bus.** OAuth scopes, webhooks, conditional webhooks and App Functions.
14. **Reporting and analytics pipeline.** Store-performance reports, exports and Jitsu e-commerce events.
15. **Stored-value ledgers.** The customer wallet (cashback, gift cards, refunds, manual entries) and loyalty points.
    - Fact: customer-wallet balances do not touch the store's payments balance (help aa3i).
    - Inference: treat them as a shared store-credit ledger, not as payments.
16. **Complaints and compliance.** Open complaints block wallet withdrawals; buyers escalate refund disputes through Salla's complaints platform (help jfqq).

## How narrow is the seam on Salla (plain-language summary)

**Not narrow.** I found 81 places where payments and the rest of Salla touch. Most of them are small, and they fall into six bundles:

1. **What can this buyer pay with, and how much?**
   - Core hands payments a finished amount (L002) and gets back a list of methods (L001).
   - To build that list, Salla's payments side reads a lot of core context: cart value and weight, products and categories, customer group and ban status, market, phone and IP country, delivery choice, plan and verification.
   - This "context-hungry eligibility" is the widest part (L007 to L011, L022 to L023, L027, L049, L052, L069).
2. **What happened?** Payments reports success, failure, review hold or deferred payment. The order turns that into a status (L004 to L006, L017 to L018, L042).
3. **Refunds.** Core decides to refund, usually after a return status. Payments decides whether it can, by which rail, and whether the balance covers it (L031, L043 to L047).
4. **Money after the sale.**
   - Settlement is where Salla is most Salla-specific.
   - The merchant's payments balance doubles as the debit source for shipping labels, platform services, financing repayments, dropshipping holds and affiliate dues (L028 to L039).
5. **Telling the outside world.** Apps see payments almost only through the order: the order payload's payment block and order webhooks. There are no transaction, payout or settlement events among the 79 catalogued (L060 to L068).
6. **Gates.** Plans, staff permissions and store verification decide who may do what (L040 to L041, L069 to L073).

**Where Salla is already narrow.**
- Headless checkout cannot submit payments at all: it hands over to a hosted checkout (L003).
- Apps can read but not change payment configuration (L064).
- Provider identity reaches the order only as identifiers (L055).
- Taxes are owned outside payments (L056).

**What follows for Sharrwah (inference).** A narrow, stable contract looks achievable for the essential half. It would need about five messages:
1. **Payment request.** Order reference, amount breakdown, currency, buyer reference, a cart summary (product types, categories, quantity, weight), market and channel. The reply is the eligible methods.
2. **Payment result events.** Authorised, captured, failed, pending, under review, with transaction references.
3. **Refund command and result.**
4. **Settlement report per order.**
5. **A generic ledger debit/credit API** for anything else that wants the merchant's balance.

What makes Salla's seam wide is mostly business choices, not commerce needs:
- COD settled through Salla's own carriers.
- The merchant balance used as a universal payout and debit rail.
- Plan-gated payment features.
- A cross-store fraud network.
- Financing.
- The Mahally and Salla Point channels.

Sharrwah can add these later as consumers of the contract instead of building them into it.

## Crossings I suspect exist but could not evidence

1. **Expiry of the deferred-payment window.** `pending_payment_ends_at` exists, but nothing held says whether an unpaid or bank-transfer order is cancelled, reminded or left alone at expiry.
2. **Stock reservation while payment is pending**, and its release on failure or expiry. There is no evidence either way.
3. **Card refunds on cancellation.** Help aa3i shows wallet refunds on cancellation. Whether a cancelled card-paid order is refunded to the card automatically is not stated.
4. **Chargebacks back into the order.** Only the liability warning and possible deduction are evidenced. No dispute event, status or webhook was found.
5. **Failed payment feeding abandoned-cart recovery.** Checkout analytics emits "Payment Failed", and abandoned-cart webhooks carry a checkout URL. The link between them is not evidenced.
6. **A payment restriction on phone country.**
   - At Rasasi, payment submission was refused with "نعتذر على اكمال الطلب بسبب خطا في رقم الجوال الرجاء التاكد من ان رقم الجوال رقم سعودي" (raw/runs/20261009T112238Z-journey-storefront-account-order-en/steps/043.text.txt:47, 2026-10-09).
   - This looks like a restriction of type country-phone, or a store rule, but the source of the rule is not visible.
7. **BNPL capture or settlement per shipment for split shipments.** Tamara amounts fall due "after shipment". Behaviour with multiple shipments is not evidenced.
8. **Settlement currency for orders in other currencies.** Orders carry exchange rates. The currency in which Salla settles AED, KWD or USD orders is not evidenced.
9. **Tax credit notes for refunded orders**, and their upload to ZATCA. Merchant billing has credit notes (help gbc2), and orders have refund receipts. A tax credit note for a buyer refund is not evidenced.
10. **Settlement with carriers outside Salla labels.** A `shipping-company-settlement` feature flag exists but is not released (`dashboard-features` demo@en items.jsonl:65). Today help koda says that COD is settled off-platform.
11. **Other unreleased or unexplained flags.**
    - `orders-bulk-remove-products-refund` (items.jsonl:334): automatic refunds when products are removed in bulk.
    - `restriction-online-payment-activation` (items.jsonl:391): unclear gating of online-payment activation.
    - `recurring-apple-pay` (items.jsonl:343).
    - The meaning of each is inferred from its name only.
12. **Pay later from the buyer's order page.** The order model has `actions.payable`, but no "pay now" button for a pending order was observed on the buyer side. Only "Pay difference" (salla-edit-order-button) was seen.
13. **Payment-link and payment-reminder messages on communication apps.** `communication.whatsapp.send` exists, but which payment messages it carries is not evidenced.

## Inconsistencies noticed in the held material (facts)

1. **The customer-wallet permission is missing from the staff list.** The `/wallet` settings section requires the permission `customer_wallet_browse` (settings-center demo@en items.jsonl:227). It is not among the 201 staff permissions held.
2. **The verification page asks for permissions that do not exist.** `/payments/kyc` asks for `payment epayment` (derived/permission-gates.tsv:103), which are also absent from the staff list.
3. **Three sources disagree on online payments for the Basic plan.**
   - On the Basic store, the `mada` and `credit_card` flags carry no plan restriction (dashboard-features merchant@en items.jsonl:190-191).
   - Help dcrw says online methods need a paid plan.
   - `payments.json` mentions a Salla Payments free-order trial for Basic.
4. **The same store offered different methods through Mahally.**
   - On its own storefront, Khyma Toys offered Bank transfer and COD.
   - Through Mahally's handoff, it offered only Mada, card, STCBank, Tamara and Tabby (2026-10-09).
5. **A bank-transfer order showed "Partially paid" while awaiting review.** The buyer-side order page showed "Partially paid 30.31" (steps/096.text.txt:38).

## Help-centre articles used

All were fetched live on 2026-10-10. `https://help.salla.sa/article/x/<id>` also resolves to each article.

| id (prefix used in notes) | title (Arabic, as served) | page last updated | canonical URL |
|---|---|---|---|
| aa3i0jwmlgph6itbobkyiohq (aa3i) | تفعيل التاجر لمحفظة العميل | الأربعاء 7 أكتوبر 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A7%D9%84%D8%AA%D8%A7%D8%AC%D8%B1-%D9%84%D9%85%D8%AD%D9%81%D8%B8%D8%A9-%D8%A7%D9%84%D8%B9%D9%85%D9%8A%D9%84/aa3i0jwmlgph6itbobkyiohq |
| ax2rekqr10n3h850km0dzjqy (ax2r) | تفعيل بوابة (PayTabs) للجمعيات الخيرية | السبت 29 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A8%D9%88%D8%A7%D8%A8%D8%A9-paytabs-%D9%84%D9%84%D8%AC%D9%85%D8%B9%D9%8A%D8%A7%D8%AA-%D8%A7%D9%84%D8%AE%D9%8A%D8%B1%D9%8A%D8%A9-1/ax2rekqr10n3h850km0dzjqy |
| ay1qhg9rjda8fuicppazwdgl (ay1q) | مستر تحصيل - لتحصيل المبالغ المعلقة والمرتجعات | الجمعة 21 أغسطس 2026 | https://help.salla.sa/article/%D9%85%D8%B3%D8%AA%D8%B1-%D8%AA%D8%AD%D8%B5%D9%8A%D9%84-%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D9%84%D8%BA-%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%82%D8%A9-%D9%88%D8%A7%D9%84%D9%85%D8%B1%D8%AA%D8%AC%D8%B9%D8%A7%D8%AA/ay1qhg9rjda8fuicppazwdgl |
| b9n1lwr9h3maclprk4tecukh (b9n1) | عزز مبيعات متجرك من خلال بطاقات الهدايا | السبت 22 أغسطس 2026 | https://help.salla.sa/article/%D8%B9%D8%B2%D8%B2-%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA-%D9%85%D8%AA%D8%AC%D8%B1%D9%83-%D9%85%D9%86-%D8%AE%D9%84%D8%A7%D9%84-%D8%A8%D8%B7%D8%A7%D9%82%D8%A7%D8%AA-%D8%A7%D9%84%D9%87%D8%AF%D8%A7%D9%8A%D8%A7/b9n1lwr9h3maclprk4tecukh |
| bhrrwm3oexjhzqjibwnic7dg (bhrr) | إعداد الحساب البنكي واسترداد رصيد متجرك | الإثنين 5 أكتوبر 2026 | https://help.salla.sa/article/-%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF-%D8%A7%D9%84%D8%AD%D8%B3%D8%A7%D8%A8-%D8%A7%D9%84%D8%A8%D9%86%D9%83%D9%8A/bhrrwm3oexjhzqjibwnic7dg |
| bkg4fsbz4b2yfq4q9rqua722 (bkg4) | تفاصيل صفحة الدفع للعميل | الأحد 20 سبتمبر 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84-%D8%B5%D9%81%D8%AD%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D9%84%D9%84%D8%B9%D9%85%D9%8A%D9%84/bkg4fsbz4b2yfq4q9rqua722 |
| bqrpidrk4v27bhquze2a9blo (bqrp) | حدود معاملات الدفع الإلكتروني | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AD%D8%AF%D9%88%D8%AF-%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/bqrpidrk4v27bhquze2a9blo |
| bx4sc8a84fxh1c0spsp5rrsx (bx4s) | تخصيص حالات الطلب | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5-%D8%AD%D8%A7%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D8%B7%D9%84%D8%A8/bx4sc8a84fxh1c0spsp5rrsx |
| d9me3k8vqi09hdiun8r2ngfr (d9me) | إعدادات قيود الدفع | الثلاثاء 29 سبتمبر 2026 | https://help.salla.sa/article/%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF%D8%A7%D8%AA-%D9%82%D9%8A%D9%88%D8%AF-%D8%A7%D9%84%D8%AF%D9%81%D8%B9/d9me3k8vqi09hdiun8r2ngfr |
| da2e9uegf65escc1f731mrwz (da2e) | -دورة تحويل المدفوعات الإلكترونية | السبت 22 أغسطس 2026 | https://help.salla.sa/article/-%D8%AF%D9%88%D8%B1%D8%A9-%D8%AA%D8%AD%D9%88%D9%8A%D9%84-%D8%A7%D9%84%D9%85%D8%AF%D9%81%D9%88%D8%B9%D8%A7%D8%AA-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A%D8%A9/da2e9uegf65escc1f731mrwz |
| dcrwxldslve7spa8eqdgii8g (dcrw) | تفعيل طرق الدفع في المتجر | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%B7%D8%B1%D9%82-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D9%81%D9%8A-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1/dcrwxldslve7spa8eqdgii8g |
| dsw3leig1h4jocdmnengiw8s (dsw3) | إنشاء طلب جديد يدوياً | السبت 14 مارس 2026 | https://help.salla.sa/article/%D8%A5%D9%86%D8%B4%D8%A7%D8%A1-%D8%B7%D9%84%D8%A8-%D8%AC%D8%AF%D9%8A%D8%AF-%D9%8A%D8%AF%D9%88%D9%8A%D8%A7/dsw3leig1h4jocdmnengiw8s |
| dtdojcntv3f4lwqzj4h0jvij (dtdo) | - إدارة طرق الدفع وتفعيل المدفوعات الإلكترونية | السبت 22 أغسطس 2026 | https://help.salla.sa/article/-%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%B7%D8%B1%D9%82-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D9%88%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A7%D9%84%D9%85%D8%AF%D9%81%D9%88%D8%B9%D8%A7%D8%AA-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A%D8%A9/dtdojcntv3f4lwqzj4h0jvij |
| dy7yvan3npix92pammram3jv (dy7y) | تفعيل وسيلة الدفع الآجل تابي Tabby | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%88%D8%B3%D9%8A%D9%84%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A7%D9%84%D8%A2%D8%AC%D9%84-%D8%AA%D8%A7%D8%A8%D9%8A-tabby/dy7yvan3npix92pammram3jv |
| g36cl2hlsv256gr55vutx5rv (g36c) | صفحة المحفظة | الأربعاء 7 أكتوبر 2026 | https://help.salla.sa/article/%D8%A7%D9%84%D9%85%D8%AD%D9%81%D8%B8%D8%A9-%D9%88%D8%A7%D9%84%D9%81%D9%88%D8%A7%D8%AA%D9%8A%D8%B1/g36cl2hlsv256gr55vutx5rv |
| gbc2ct0nerndys7sk4l2rvc1 (gbc2) | إدارة باقة المتجر: الاشتراكات، الفواتير، والترقية | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A8%D8%A7%D9%82%D8%A9-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A7%D9%84%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83%D8%A7%D8%AA-%D8%A7%D9%84%D9%81%D9%88%D8%A7%D8%AA%D9%8A%D8%B1-%D9%88%D8%A7%D9%84%D8%AA%D8%B1%D9%82%D9%8A%D8%A9/gbc2ct0nerndys7sk4l2rvc1 |
| gdjqu4y69dhgd0924nho4y7x (gdjq) | كيف تقلل الاعتماد على الدفع عند الاستلام وتزيد الدفع الإلكتروني في متجرك؟ | السبت 29 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%82%D9%84%D9%8A%D9%84-%D8%B7%D9%84%D8%A8%D8%A7%D8%AA-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%B9%D9%86%D8%AF-%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%84%D8%A7%D9%85-1/gdjqu4y69dhgd0924nho4y7x |
| goka3pendumlu3su9qorkjkj (goka) | تفعيل وسيلة الدفع الآجل تمارا | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%88%D8%B3%D9%8A%D9%84%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A7%D9%84%D8%A2%D8%AC%D9%84-%D8%AA%D9%85%D8%A7%D8%B1%D8%A7/goka3pendumlu3su9qorkjkj |
| ho3182vb4jj8qmhar6ll3uor (ho31) | العمليات والإجراءات على الطلب | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%A7%D9%84%D8%B9%D9%85%D9%84%D9%8A%D8%A7%D8%AA-%D9%88%D8%A7%D9%84%D8%A5%D8%AC%D8%B1%D8%A7%D8%A1%D8%A7%D8%AA-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%B7%D9%84%D8%A8/ho3182vb4jj8qmhar6ll3uor |
| hy4mv5r6yqoyjifiy7659nzk (hy4m) | تفعيل الدفع بالبطاقة في كاشير سلة بوينت / كاشير مجاني | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A8%D8%A7%D9%84%D8%A8%D8%B7%D8%A7%D9%82%D8%A9-%D9%81%D9%8A-%D8%B3%D9%84%D8%A9-%D8%A8%D9%88%D9%8A%D9%86%D8%AA/hy4mv5r6yqoyjifiy7659nzk |
| i31g2awy4qa2ifu6bp352zoy (i31g) | إدارة التاجر لمحفظة العميل وعروض الكاش باك | الإثنين 14 سبتمبر 2026 | https://help.salla.sa/article/%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%AA%D8%A7%D8%AC%D8%B1-%D9%84%D9%85%D8%AD%D9%81%D8%B8%D8%A9-%D8%A7%D9%84%D8%B9%D9%85%D9%8A%D9%84-%D9%88%D8%B9%D8%B1%D9%88%D8%B6-%D8%A7%D9%84%D9%83%D8%A7%D8%B4-%D8%A8%D8%A7%D9%83/i31g2awy4qa2ifu6bp352zoy |
| ig4b4l5hc542j4bcd2tp82bz (ig4b) | توثيق متجرك الجديد في السعودية | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%88%D8%AB%D9%8A%D9%82-%D9%85%D8%AA%D8%AC%D8%B1%D9%83-%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF-%D9%81%D9%8A-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/ig4b4l5hc542j4bcd2tp82bz |
| ijbdgpr5m5qzda14qbqx8mal (ijbd) | تخصيص فواتير المتجر / محرر الفواتير | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5-%D9%81%D9%88%D8%A7%D8%AA%D9%8A%D8%B1-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D9%85%D8%AD%D8%B1%D8%B1-%D8%A7%D9%84%D9%81%D9%88%D8%A7%D8%AA%D9%8A%D8%B1/ijbdgpr5m5qzda14qbqx8mal |
| isgb9vw6l95n9cexu36jrqpt (isgb) | إعدادات الفوترة في المتجر | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF%D8%A7%D8%AA-%D8%A7%D9%84%D9%81%D9%88%D8%AA%D8%B1%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1/isgb9vw6l95n9cexu36jrqpt |
| itdzlot4huy9zpfw3o342j6k (itdz) | إعداد ضريبة القيمة المضافة | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF-%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9-%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9-%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9/itdzlot4huy9zpfw3o342j6k |
| jfqqyp72i8hfci4riwvxcci3 (jfqq) | الاسترجاع والاستبدال: حقوقك كمشترٍ من متجر في سلة | الثلاثاء 29 سبتمبر 2026 | https://help.salla.sa/article/returns-and-refunds-for-shoppers/jfqqyp72i8hfci4riwvxcci3 |
| jpuire3zxn5ayv0mg6zum636 (jpui) | تفعيل الشراء السريع | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A7%D9%84%D8%B4%D8%B1%D8%A7%D8%A1-%D8%A7%D9%84%D8%B3%D8%B1%D9%8A%D8%B9/jpuire3zxn5ayv0mg6zum636 |
| k4j1z7b3c8lzqh16g8r2hsxn (k4j1) | الإجراءات على بطاقة العميل | الإثنين 21 سبتمبر 2026 | https://help.salla.sa/article/%D8%A7%D9%84%D8%A5%D8%AC%D8%B1%D8%A7%D8%A1%D8%A7%D8%AA-%D8%B9%D9%84%D9%89-%D8%A8%D8%B7%D8%A7%D9%82%D8%A9-%D8%A7%D9%84%D8%B9%D9%85%D9%8A%D9%84/k4j1z7b3c8lzqh16g8r2hsxn |
| koda8pykc6pdhylg7zb2iu0g (koda) | تفعيل وإدارة الدفع عند الاستلام مع بوليصات سلة | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%88%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%B9%D9%86%D8%AF-%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%84%D8%A7%D9%85-%D9%85%D8%B9-%D8%A8%D9%88%D9%84%D9%8A%D8%B5%D8%A7%D8%AA-%D8%B3%D9%84%D8%A9/koda8pykc6pdhylg7zb2iu0g |
| lwd3jzhb0qs7v51b50rcc50a (lwd3) | إدارة استرجاع الطلبات | الخميس 3 سبتمبر 2026 | https://help.salla.sa/article/%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D8%B3%D8%AA%D8%B1%D8%AC%D8%A7%D8%B9-%D8%A7%D9%84%D8%B7%D9%84%D8%A8%D8%A7%D8%AA/lwd3jzhb0qs7v51b50rcc50a |
| mhbnge668ms3i46zvi7cwvl3 (mhbn) | آلية استرجاع طلب وإضافة قيمته إلى محفظة العميل | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%A2%D9%84%D9%8A%D8%A9-%D8%A7%D8%B3%D8%AA%D8%B1%D8%AC%D8%A7%D8%B9-%D8%B7%D9%84%D8%A8-%D9%88%D8%A5%D8%B6%D8%A7%D9%81%D8%A9-%D9%82%D9%8A%D9%85%D8%AA%D9%87-%D8%A5%D9%84%D9%89-%D9%85%D8%AD%D9%81%D8%B8%D8%A9-%D8%A7%D9%84%D8%B9%D9%85%D9%8A%D9%84/mhbnge668ms3i46zvi7cwvl3 |
| mwmsy60840mp73dpv7n0wd4s (mwms) | طريقة تفعيل خدمات التقسيط / الدفع الآجل في متجرك | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%AE%D8%AF%D9%85%D8%A7%D8%AA-%D8%A7%D9%84%D8%AA%D9%82%D8%B3%D9%8A%D8%B7-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A7%D9%84%D8%A2%D8%AC%D9%84-%D9%81%D9%8A-%D9%85%D8%AA%D8%AC%D8%B1%D9%83/mwmsy60840mp73dpv7n0wd4s |
| n53zyxfv29z0pujrwswnqxqm (n53z) | الأسئلة الشائعة حول استرجاع الطلبات | الخميس 3 سبتمبر 2026 | https://help.salla.sa/article/%D8%A7%D9%84%D8%A3%D8%B3%D8%A6%D9%84%D8%A9-%D8%A7%D9%84%D8%B4%D8%A7%D8%A6%D8%B9%D8%A9-%D8%AD%D9%88%D9%84-%D8%A7%D8%B3%D8%AA%D8%B1%D8%AC%D8%A7%D8%B9-%D8%A7%D9%84%D8%B7%D9%84%D8%A8%D8%A7%D8%AA/n53zyxfv29z0pujrwswnqxqm |
| nfb8hjhk7x5md5y16n789ner (nfb8) | تقارير المدفوعات | الثلاثاء 1 سبتمبر 2026 | https://help.salla.sa/article/%D8%AA%D9%82%D8%A7%D8%B1%D9%8A%D8%B1-%D8%A7%D9%84%D9%85%D8%AF%D9%81%D9%88%D8%B9%D8%A7%D8%AA/nfb8hjhk7x5md5y16n789ner |
| nysbqdb4hj4sqpniinmrwmkh (nysb) | مراحل إدارة الطلب وعملية البيع | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%B7%D9%84%D8%A8-%D9%88%D8%B9%D9%85%D9%84%D9%8A%D8%A9-%D8%A7%D9%84%D8%A8%D9%8A%D8%B9/nysbqdb4hj4sqpniinmrwmkh |
| qguabxrm5zhr2i4h7ww68i0h (qgua) | الفواتير الضريبية الالكترونية | الثلاثاء 22 سبتمبر 2026 | https://help.salla.sa/article/%D8%A7%D9%84%D9%81%D9%88%D8%A7%D8%AA%D9%8A%D8%B1-%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9-%D8%A7%D9%84%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A%D8%A9/qguabxrm5zhr2i4h7ww68i0h |
| t0kf3e7l4skv6raa7b9yq2ov (t0kf) | الربط مع هيئة الزكاة والضريبة | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-%D9%87%D9%8A%D8%A6%D8%A9-%D8%A7%D9%84%D8%B2%D9%83%D8%A7%D8%A9-%D9%88%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9/t0kf3e7l4skv6raa7b9yq2ov |
| v5jrh4oz46bfkh8u0dnnlk8v (v5jr) | تخصيص إعدادات الطلبات | الثلاثاء 1 سبتمبر 2026 | https://help.salla.sa/article/%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5-%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF%D8%A7%D8%AA-%D8%A7%D9%84%D8%B7%D9%84%D8%A8%D8%A7%D8%AA/v5jrh4oz46bfkh8u0dnnlk8v |
| vjomgg9wqhz87cfjvqg54gzr (vjom) | تفعيل الدفع عبر برنامج الولاء - مكافأة الراجحي | الثلاثاء 6 أكتوبر 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%B9%D8%A8%D8%B1-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC-%D8%A7%D9%84%D9%88%D9%84%D8%A7%D8%A1-%D9%85%D9%83%D8%A7%D9%81%D8%A3%D8%A9-%D8%A7%D9%84%D8%B1%D8%A7%D8%AC%D8%AD%D9%8A/vjomgg9wqhz87cfjvqg54gzr |
| vnmcb3lad5fiwd7xnrmbteql (vnmc) | تفعيل أبل باي Apple Pay | الأحد 27 سبتمبر 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D8%A3%D8%A8%D9%84-%D8%A8%D8%A7%D9%8A-apple-pay/vnmcb3lad5fiwd7xnrmbteql |
| wv9wyqrnhwpm6m2rp3cmg653 (wv9w) | تفعيل وإدارة الأسواق المتعددة | الأحد 27 سبتمبر 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%88%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%A3%D8%B3%D9%88%D8%A7%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%B9%D8%AF%D8%AF%D8%A9/wv9wyqrnhwpm6m2rp3cmg653 |
| wwcywu3o0idvepigpbsvk5a1 (wwcy) | إرسال عرض السعر من متجرك | السبت 22 أغسطس 2026 | https://help.salla.sa/article/%D8%A5%D8%B1%D8%B3%D8%A7%D9%84-%D8%B9%D8%B1%D8%B6-%D8%A7%D9%84%D8%B3%D8%B9%D8%B1-%D9%85%D9%86-%D9%85%D8%AA%D8%AC%D8%B1%D9%83/wwcywu3o0idvepigpbsvk5a1 |
| xiu0yycxeuii6wrdn0hfyowh (xiu0) | نصائح لحماية متجرك من الاحتيال | الأربعاء 19 أغسطس 2026 | https://help.salla.sa/article/%D9%86%D8%B5%D8%A7%D8%A6%D8%AD-%D9%84%D8%AD%D9%85%D8%A7%D9%8A%D8%A9-%D9%85%D8%AA%D8%AC%D8%B1%D9%83-%D9%85%D9%86-%D8%A7%D9%84%D8%A7%D8%AD%D8%AA%D9%8A%D8%A7%D9%84/xiu0yycxeuii6wrdn0hfyowh |
| xv4salemauzwaoov97ccuvwf (xv4s) | تفاصيل العنوان والهوية في صفحة الدفع لطلبات الشحن الدولي | الإثنين 31 أغسطس 2026 | https://help.salla.sa/article/%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84-%D8%A7%D9%84%D8%B9%D9%86%D9%88%D8%A7%D9%86-%D9%88%D8%A7%D9%84%D9%87%D9%88%D9%8A%D8%A9-%D9%81%D9%8A-%D8%B5%D9%81%D8%AD%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D9%84%D8%B7%D9%84%D8%A8%D8%A7%D8%AA-%D8%A7%D9%84%D8%B4%D8%AD%D9%86-%D8%A7%D9%84%D8%AF%D9%88%D9%84%D9%8A/xv4salemauzwaoov97ccuvwf |
