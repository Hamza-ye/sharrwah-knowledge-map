# S-01 register entry: who holds the merchant's funds between the buyer's payment and the payout

**For the founder, at G1.** Written by the coordinator on 17 October 2026, from the pilot's files in this folder and Stage 1's in `studies/yemen-cases/`. The ids cite them:
- `S01-…-0nn` is a platform's statement;
- `S01-V-nnn` is a variant;
- `YA`, `YK` and `YE` are Stage 1's axes, constants and citations;
- `Q2` is the frame every Yemen case shares, that the merchant sells in the Yemeni market.

Every recommendation here is the coordinator's, and says so. Every answer is yours. "Defer" is always allowed: the variation point stays open, set per market, at the build cost the item states.

## In short

Phase C found 12 questions that are yours to decide (`analysis.tsv`, column `founder_item`). They aren't independent. One of them decides most of the others: **who holds the merchant's money between the buyer's payment and the payout** (S01-VP-01).

- **The five references use three arrangements,** and most carry several at once (phase C's coexistence letters):
  - **the platform holds a balance for the merchant:** Salla and Zid;
  - **a payment processor holds it:** Shopify, WooCommerce and BigCommerce;
  - **the provider of each payment method holds it:** couriers for cash on delivery, buy-now-pay-later companies, and the gateways the merchant contracts with on BigCommerce.

  Phase C reads the difference as the vendors' choice, not the market's.
- **In Yemen today:**
  - the processors the references use don't serve a merchant in Yemen (YA-62, YK-514);
  - holding others' funds is a licensed activity, reserved to banks in the government's area and licensed by two central banks (YA-102, YA-103, YA-44);
  - what does work is the provider of each payment method: couriers that collect cash on delivery, and licensed local wallets (YA-128, YA-130, YK-203, YA-68, YA-109).
- **The coordinator's recommendation:** for Yemen now, let the provider of each payment method hold the merchant's funds, and let Sharrwah hold none. Build the money flow behind one interface, so that a balance Sharrwah holds can be switched on in a market once Sharrwah, or a licensed partner, holds that market's licence.
  - The other eleven answers follow from that choice, except installments (defer) and currency (several per merchant, with the rial's two editions kept apart).

Phase D marked every Yemen case, and **no case changes any of these marks from today's** (`yemen-marks.tsv`). Yemen's variation across places and time doesn't change how this subject fares.

## What the references do

| Platform | Who holds the merchant's funds | Cited |
| --- | --- | --- |
| Salla | "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها" (the electronic payments balance keeps the store's sales proceeds before they are transferred) | S01-V-016 (S01-SA-056, S01-SA-144) |
| Zid | "محفظة تمكن التاجر من حفظ وإدارة المبالغ الخاصة به والخاصة بمتجره الإلكتروني في منصة زد" (a wallet in which the merchant keeps and manages the store's money on Zid's platform) | S01-V-024 (S01-ZD-057) |
| Shopify | "The Payment Processors may hold funds in your Shopify Payments Account"; for international Managed Markets orders, "Global-e holds the funds" | S01-V-003 (S01-SH-022, S01-SH-033); S01-V-001 (S01-SH-099) |
| WooCommerce | "funds held by Stripe or an applicable Affiliate", "held in one or more Pooled Accounts at one or more Financial Providers" | S01-V-008 (S01-WC-109); S01-V-011 (S01-WC-120) |
| BigCommerce | "all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account" (a PayPal account); with other gateways, "You will control and direct funds in your merchant account with your merchant service provider" | S01-V-027 (S01-BC-051); S01-V-532 (S01-BC-088) |

## What Yemen shows

- **The references' processors aren't available.**
  - YA-62 today: "Unavailable @ Stripe's service", "Not available, a request to add it open @ WooPayments's service", "Unavailable @ Zid Pay Kuwait (Zid)'s service", "Sending from Yemen @ PayPal's service".
  - YK-514: "cannot receive money @ PayPal's service".
  - YK-335: international payment cards are "no longer used".
- **Holding others' money is licensed and split.**
  - Who may provide e-money and electronic payment services: "banks only" in the government's area, "banks and non-bank institutions" in the Houthis' area (YA-102).
  - A payment service provider licence needs "a joint-stock company with paid-up capital of at least 500 million rials" (YA-105).
  - E-money funds are "pre-funded and held in a pooled account at a settlement bank" (YA-106).
  - Banks answer to the Sana'a or the Aden central bank, by area (YA-44).
- **How buyers pay:**
  - cash on delivery dominates: "cash on delivery, preferred by 74 percent @ Aden" (YA-129);
  - couriers collect it, for example "available to business accounts @ Torod's service" (YK-203);
  - local wallets take online payments (YA-68), and offer merchants "receiving payments, paying merchants, cash out, refunds, cash in and transfers to bank accounts" (YA-109, at ONE Cash);
  - electronic transfers between different banks are "none, only cash, cheques or within one institution" in government-controlled areas (YA-126).
- **The rial circulates in two editions at two rates.**
  - YA-15: "old notes only, Aden's new notes barred" in the Houthis' area; "all notes, new and old, legal tender" in the government's area.
  - YA-01's rates differ by area by a factor of about three.
- **US sanctions bear on dealings.**
  - The Houthis are designated "FTO and SDGT" (YA-27).
  - OFAC's assurance that trade with Yemenis isn't targeted is "withdrawn" (YK-22).
  - Sanctions are "named as a limit on e-commerce" (YK-24).

## Decision 1, the root: who holds the merchant's funds (S01-VP-01)

**The question.** Between the buyer's payment and the payout, who should hold a merchant's funds in Sharrwah: a balance Sharrwah keeps for the merchant, the payment processor's accounts, or the provider of each payment method? (`analysis.tsv`, S01-VP-01.)

**Why it is yours.** The cause is vendor choice. Getting it wrong is expensive: "money flows, legal structure and partner contracts: the holder is the party the buyer's money goes to first and that settles it to the merchant" (S01-VP-01, `expensive_because`, citing S01-SA-003 and S01-WC-120). The rule table makes it a decision for the founder, on a recommendation. It also makes it "a variation point behind one interface, bound per market, store or plan".

**Yemen's mark.** Carried unchanged, in every case, through S01-V-024. Its condition is Zid's own wording: "استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية" (the wallet is available to all merchants outside the Kingdom, with the Saudi riyal as base currency; S01-ZD-121, met under Q2).
- So the one reference arrangement marked as working unchanged for a merchant in Yemen is a platform-held balance, held by Zid outside Yemen and in Saudi riyals.
- The processors the other variants name are unavailable to a merchant in Yemen (YA-62, YK-514).

**The options:**

| Option | What it needs built | What it needs from outside |
| --- | --- | --- |
| **A. Sharrwah holds a balance for the merchant** (Salla's and Zid's model) | a ledger of merchant balances; collection into Sharrwah's accounts; payouts; reconciliation | In Yemen: a licence to provide e-money or payment services. That means banks only in the government's area (YA-102); a joint-stock company with 500 million rials paid up for a provider licence (YA-105); and pooled, pre-funded accounts at a settlement bank (YA-106). The licence comes from the central bank of each area (YA-44, YA-103). Or a licensed bank as partner that holds the funds for Sharrwah. |
| **A2. As A, but held outside Yemen under another country's licence** (what Zid does for merchants outside Saudi Arabia) | as A, plus conversion and cross-border payouts | a licensed entity or partner abroad. The merchant's money then sits abroad in a foreign currency, under sanctions screening (YA-27, YK-22) |
| **B. The provider of each payment method holds** (BigCommerce's "merchant account with your merchant service provider"; Salla's and Zid's cash on delivery through couriers) | integrations with each provider: wallets, couriers, bank transfer; one interface over them; showing the merchant each provider's balance | a contract with each provider, between the provider and the merchant: licensed wallets (YA-68, YA-109) and couriers (YK-203, YA-130) |
| **C. A payment processor holds** (Shopify's, WooCommerce's and BigCommerce's processors) | an integration with the processor | a processor that serves merchants in Yemen. None of the references' processors does today (YA-62, YK-514). |
| **Defer** | the interface only | none now |

**The coordinator's recommendation: B for Yemen now, behind one interface that can also carry A.**
- C can't be bound in Yemen today: no reference processor serves a merchant there.
- A in Yemen needs a licence reserved to banks in the government's area, from two split authorities, with heavy capital. If that is wrong after launch, the money flows and the legal structure must change, as phase C's `expensive_because` warns.
- B is what phase D shows working: with a partner for cash on delivery (S01-VP-02 and S01-VP-04's marks), and through licensed wallets that already offer merchants receiving, refunds and transfers to bank accounts.
- A2 works for Zid, but it moves the merchant's money abroad, into a foreign currency.
- The interface keeps A open per market, as phase C's rule says. A can then be switched on where Sharrwah or a licensed partner holds the licence.

**Your answer:** A, A2, B, C or defer.

## Decisions 2 to 12, which mostly follow from Decision 1

Each line gives the question as phase C wrote it, the evidence, Yemen's mark (the same in every case), and the coordinator's recommendation if you choose B. If you choose A, the recommendation in brackets applies instead.

### 2. Who settles the funds to the merchant (S01-VP-02)

**The question:** Sharrwah, a payment processor or acquirer, or the provider of each payment method (a BNPL company, a shipping company for cash on delivery)?

**The evidence:**
- Shopify: "The acquirer subtracts a small fee from the amount, and then transfers the final amount to your merchant account" (S01-V-032, S01-SH-058).
- BigCommerce: BitPay "settles directly to your bank account" (S01-V-042, S01-BC-021).
- Salla: "تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن" (cash on delivery is settled directly between the merchant and the shipping company; S01-V-038, S01-SA-091).

**Yemen:** carried only with a partner, through S01-V-038, with a courier such as Torod (YK-203, YA-130).

**The coordinator's recommendation:** the provider of each payment method settles to the merchant. Under A, Sharrwah settles.

### 3. Who sends payouts to the merchant's bank account (S01-VP-03)

**The question:** Sharrwah, the payment processor, or the provider of each payment method or sales channel?

**The evidence:**
- Salla: "تحوَّل سلة مستحقات المدفوعات الإلكترونية والمدفوعات عند الاستلام إلى حسابك البنكي" (Salla transfers the proceeds to your bank account; S01-V-055).
- Zid: "تقوم زد باي بتحصيل المبالغ المحصلة إلى حسابك البنكي بشكل دوري 3 مرات في الأسبوع" (Zid Pay pays to your bank account three times a week; S01-V-060).
- BigCommerce, standalone PayPal: "Funds are deposited immediately into your PayPal account" (S01-V-616).

**Yemen:** carried only with a partner, through S01-V-059. A card payment is turned into a bank transfer "through the service provider" (S01-SA-113). SabaCard acquires local and international cards (YK-161).

**The coordinator's recommendation:** the provider pays the merchant, or the merchant withdraws from their own wallet. Sharrwah sends no payouts. Under A, Sharrwah sends them.

### 4. Who collects the buyer's payment (S01-VP-04)

**The question:** Sharrwah's own payment service, a payment processor or acquirer, or the provider of each payment method?

**The evidence:**
- Shopify: "All Shopify-supported payment methods rely on third-party providers to process your transactions" (S01-V-068).
- Salla: "خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر" (a Salla service that processes your store's payments directly; S01-V-085).
- Salla, for cash on delivery: amounts "يتم تحصيلها من خلال شركات الشحن" (collected through shipping companies; S01-V-090).

**Yemen:** carried only with a partner, through S01-V-093. The courier collects cash on delivery (S01-SA-090, YK-203).

**The coordinator's recommendation:** the provider of each payment method collects: the wallet, the courier, or the merchant's own account for transfers. Under A, Sharrwah's payment service collects through licensed partners.

### 5. Whether Sharrwah acts as the merchant's agent (S01-VP-06)

**The question:** should Sharrwah act as the merchant's agent towards payment processors and providers, or take no agency role and leave agency to the processor?

**The evidence:**
- Shopify: "You hereby appoint us as your agent to deliver information and instructions on your behalf to one or more payment processors" (S01-V-112, S01-SH-001).
- BigCommerce: "No agency, partnership, joint venture or employment relationship is created by this Agreement or your use of the Services" (S01-V-623, S01-BC-128).

**Yemen:** unknown. No answer variant is shown to work (`yemen-marks.tsv`, S01-VP-06).

**The coordinator's recommendation:** no agency role. Under B, Sharrwah directs no funds, as in BigCommerce's terms. Under A, revisit this with the licence, since the holder would receive and hold funds for the merchant.

### 6. Who deducts fees, refunds and other amounts (S01-VP-09)

**The question:** Sharrwah, the payment processor, or the provider of each payment method?

**The evidence:**
- Shopify: "we may deduct, or request that a Payment Processor deduct, from any accounts associated with your Shopify Payments Account" (S01-V-152).
- Zid: "يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة" (Zid Pay and the service provider may deduct transaction fees directly from collected amounts; S01-V-158).
- Salla, for Tamara: "يتم خصم المبلغ مباشرة من تمارا وليس من رصيد مدفوعات سلة" (deducted from Tamara, not from Salla's balance; S01-V-165).

**Yemen:** carried unchanged, through S01-V-160 (Zid's wallet).

**The coordinator's recommendation:** each provider deducts its own fees. Sharrwah, holding nothing, bills its own fees apart. Under A, Sharrwah deducts.

### 7. Which accounts a merchant holds (S01-VP-11)

**The question:** an account with Sharrwah only, an account with each payment processor or provider opened through Sharrwah, or both?

**The evidence:**
- Shopify: "you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors" (S01-V-173).
- WooCommerce: "This creates a Stripe Express account that is connected to the WooPayments service" (S01-V-180).
- Zid: "رصيد كافي في حسابه لدى زد باي" (a sufficient balance in his account with Zid Pay; S01-V-190).

**Yemen:** carried unchanged, through S01-V-194. Zid's wallet has its own IBAN.

**The coordinator's recommendation:** an account with each provider, linked through Sharrwah. A Sharrwah account serves only Sharrwah's own billing. Under A, both.

### 8. Payout timing (S01-VP-15)

**The question:** one timing Sharrwah sets, or each payment provider's settlement time by country, risk level and payment method?

**The evidence:**
- Shopify: "The minimum settlement time depends on your region, risk level, and the payment method used" (S01-V-329).
- Zid: two to five working days from the wallet to the bank account (S01-V-343).

**Yemen:** carried unchanged, through S01-V-343. Transfers between different banks are hard in Yemen (YA-126).

**The coordinator's recommendation:** follow each provider's settlement time, and show it to the merchant per payment method. Under A, Sharrwah sets one timing per market.

### 9. Deducted before payout, or billed apart (S01-VP-19)

**The question:** should fees, refunds, chargebacks and other amounts owed be deducted from a merchant's funds before payout, or billed apart, and by which party?

**The evidence:**
- Shopify: processing fees "are deducted from your earnings before the payout is sent" (S01-V-452).
- Salla: a withdrawal fee of 8.05 riyals (S01-V-472).
- Zid: a 3-riyal deposit fee per collection (S01-V-477).

**Yemen:** carried unchanged, through S01-V-480: Zid's transfer fee, 50 riyals for a bank outside Saudi Arabia.

**The coordinator's recommendation:** providers net their own fees. Sharrwah bills its fees apart, having no payout to net them from. Under A, Sharrwah deducts before payout.

### 10. Funds held at termination (S01-VP-20)

**The question:** when a merchant's account or payment service ends, should Sharrwah pay the funds it still holds to the merchant's bank account, hold them until refunds, chargebacks and fees are settled, or return them to the buyers?

**The evidence:**
- Zid: "نعم يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي" (yes, the balance is transferred to the bank account; S01-V-496).
- Salla: "إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين" (returning any pending electronic payments to the consumers; S01-V-495).
- Shopify: "a Payment Processor may elect to continue to hold any funds deemed necessary, pending resolution" (S01-V-491).

**Yemen:** unknown. No answer variant is shown to work.

**The coordinator's recommendation:** under B, Sharrwah holds nothing to settle. The funds stay with each provider under its terms, and Sharrwah's terms say so. Under A, this needs a decision with the licence. Zid's terms show one way: hold the funds until pending operations settle (S01-V-498), then transfer the balance to the bank account (S01-V-496).

### 11. Installments: who pays the merchant up front (S01-VP-22)

**The question:** a BNPL provider under its own agreement with the merchant, or the platform's own payment service?

**The evidence:**
- Salla, Tabby: "تقوم تابي بالتحويل لمتجرك أولاً والتحصيل من عملائك لاحقاً" (Tabby pays your store first and collects from your customers later; S01-V-516).
- BigCommerce: "the shopper will owe the money to PayPal while you, the merchant, always get paid" (S01-V-653).
- Shopify: with Shop Pay Installments, "you receive full payment for your order with your other Shopify Payments" payouts (S01-V-514).

**Yemen:** unknown. The references' providers fail there: PayPal can't receive (YK-514), and WooPayments isn't available (YA-62). The Yemen evidence names no installment provider.

**The coordinator's recommendation:** defer. Keep it a variation point, and if it is offered, a BNPL provider pays up front under its own agreement. The other option makes Sharrwah carry the buyers' debt.

### 12. Currency (S01-VP-23)

**The question:** the currency of the merchant's local bank account in each market, one base currency with conversion, or several currencies per merchant?

**The evidence:**
- Salla: the UAE account "بعملة الدرهم الإماراتي" (in UAE dirhams; S01-V-526); and "يتم استقبال جميع المدفوعات بالريال السعودي" (all payments are received in Saudi riyals; S01-V-609).
- WooCommerce: payout currencies listed by country (S01-V-524).
- Zid: amounts in Gulf currencies can't be withdrawn from the wallet (S01-V-528).

**Yemen:** carried unchanged, through S01-V-528. Wallets in Yemen hold "the rial, Saudi riyal and US dollar" (YA-86, at ONE Cash). The rial trades at two rates, in two editions, by area (YA-01, YA-15).

**The coordinator's recommendation:** several currencies per merchant, and the rial's two editions recorded apart, by the area the funds are held in.
- Q2 names "a currency circulating in two editions" as a concern the product class never faced. It is a design decision, not a classification.
- One base currency with conversion would mix two rials at a rate of about three to one.

## Variation points that aren't founder decisions

Phase C's rule table settles these. The `follows` column says what the build does with each.

| Variation point | Cause | What follows |
| --- | --- | --- |
| S01-VP-05, "pay you directly" | no difference | a commonality, carried as the references carry it; Yemen: carried unchanged, by direct bank transfer (S01-V-102) |
| S01-VP-08, "withhold"; S01-VP-18, "held" | market, named rule | the platform carries all the variants at once |
| S01-VP-12, "licensed"; S01-VP-17, "reserve" | market, named rule | a variation point bound per market |
| S01-VP-13, "terms of service" | maturity | kept open as a variation point until evidence settles it |
| S01-VP-14, "payout schedule"; S01-VP-16, "Minimum payout amount" | vendor choice, cheap to change | left to the build |
| S01-VP-07, "Reserve"; S01-VP-10, "security interest"; S01-VP-21, "refunded to your customers" | unknown | kept open as a variation point until evidence settles it |

## What would change this entry

- **The pages still with you:** Salla's payment services contract, and Zid's two dashboard pages (`evidence/product-class/to-save-for-s01.md`). They would close gaps on who settles Salla Payments funds, and on the provider and bank behind Zid Pay and Zid's wallet.
- **Stage 1's faithfulness pass before Stage 4.** It covers every axis. The axes this subject rests on were checked against their quotes before the marks (`studies/yemen-cases/review-independent.md`).
- **A processor that starts serving merchants in Yemen** would make option C possible there.
