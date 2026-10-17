# S-01 register entry: who holds the merchant's funds between the buyer's payment and the payout

**For the founder, at G1.** Written by the coordinator on 17 October 2026, and rewritten the same day after the independent review (`review.md`). It rests on the pilot's files in this folder and on Stage 1's in `studies/yemen-cases/` at commit `4e3f3dd`.

**The ids:**
- `S01-SA`, `S01-ZD`, `S01-SH`, `S01-WC` and `S01-BC` are statements of Salla, Zid, Shopify, WooCommerce and BigCommerce;
- `S01-V` is a variant, and `S01-VP` a variation point;
- `YA`, `YK`, `YE` and `YC` are Stage 1's axes, constants, citations and cases;
- `Q2` is the frame every Yemen case shares: the merchant sells in the Yemeni market.

**How to read it:**
- Every recommendation is the coordinator's and is headed so. A reading of the coordinator's that groups the evidence, or links one decision to another, is marked *(the coordinator's reading)*.
- Every answer is yours. "Defer" is always allowed: the variation point stays open and is set per market, at the build cost the item states.
- English in brackets after Arabic is the coordinator's translation.

## In short

- **14 decisions are yours.** Phase C found 13 (`analysis.tsv`, column `founder_item`). Phase D found one more: a security interest over the merchant's funds, where no reference arrangement works for a merchant in Yemen (`yemen-marks.tsv`, S01-VP-10). Each decision below has its evidence, its options, a recommendation and its own answer line.
- **Most of them hang on the first** *(the coordinator's reading)*. In the references, the party that holds the merchant's funds is mostly also the one that settles them, pays them out, collects them, deducts from them, keeps the merchant's account and sets the timing. So Decisions 2 to 12 follow from Decision 1 in most cases. The table "What Decision 1 implies for the others" gives each one's answer under each option. You can answer Decision 1 and let it settle those as a standing decision (`PLAN.md` section 5), or answer each one.
- **The references.** All five keep the merchant's funds in a balance under their own name or their payment product's. Behind it, Shopify, WooCommerce and BigCommerce name the processors that hold the money. Salla and Zid name partners without saying who holds. BigCommerce also leaves funds in the merchant's own account with their provider.
- **Yemen,** from Stage 1, checked against its quotes:
  - none of the references' processors that Stage 1 covers serves a merchant in Yemen. Stage 1 has nothing on the others;
  - holding others' funds needs a licence from each area's central bank, and a non-bank can hold one in either area. In the government's area, a provider must be a joint-stock company with at least 500 million rials paid up;
  - buyers mostly pay cash on delivery, couriers collect it for business accounts, wallets take online payments, and sellers take transfers into their own accounts.
- **Phase D's marks.** No reference arrangement for who holds the funds is shown to work in Yemen, so that mark is `unknown`. What is shown working there is a courier that collects and settles cash on delivery, a card acquirer that pays out, and the buyer paying into the merchant's own bank account. No Yemen case changes any mark from today's.
- **The coordinator's recommendation:** for Yemen now, the provider of each payment method holds the merchant's funds, in the merchant's own account with it, and Sharrwah holds none. Build the money flow behind one interface that can also carry a balance Sharrwah holds, or a processor's, switched on per market where a licence or a processor allows it. Installments: defer. Currency: several per merchant, with the rial kept apart by area.

## What the references do (S01-VP-01)

| Platform | What its words say holds the funds | Cited |
| --- | --- | --- |
| Salla | When the buyer pays, "تذهب الأموال أولاً إلى رصيد المدفوعات الإلكترونية" (the money goes first to the electronic payments balance). That balance "يحتفظ ... بمستحقات مبيعات المتجر قبل تحويلها" (keeps the store's sales proceeds before they are transferred). Cash on delivery has a balance of its own. Salla provides payment "عبر شركائها" (through its partners), without saying which partner holds the money. | S01-V-016 (S01-SA-003, S01-SA-056); S01-V-018; S01-SA-078 |
| Zid | "المبالغ المتوفرة في رصيد حسابك في زد باي" (the amounts in your Zid Pay account balance), for Saudi Arabia and Kuwait. For its own courier service's cash on delivery, Zid collects the dues and transfers them "إلى محفظة التاجر" (to the merchant's wallet). Zid Pay works "من خلال مقدمي خدمات الدفع" (through payment service providers), unnamed. Who holds for Zid's other gateways is a gap. | S01-V-023 (S01-ZD-034); S01-V-656 (S01-ZD-069); S01-ZD-002; S01-V-025 |
| Shopify | "The Payment Processors may hold funds in your Shopify Payments Account". For international Managed Markets orders, "Global-e holds the funds". In Europe, Adyen: "amounts held by Processor prior to Settlement of such funds to User". | S01-V-003 (S01-SH-022); S01-V-001 (S01-SH-099); S01-V-006 (S01-SH-127) |
| WooCommerce | "Money that you’ve made with WooPayments must flow through your WooPayments account balance before it’s paid out into your bank account". Behind it, "funds held by Stripe or an applicable Affiliate", "held in one or more Pooled Accounts at one or more Financial Providers". | S01-V-015 (S01-WC-024); S01-V-008 (S01-WC-109); S01-V-011 (S01-WC-120) |
| BigCommerce | "all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account", for which "a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement". With the standalone PayPal gateway, funds go to "your PayPal business account". Its help article "Where do I manage my funds?" answers: "You will control and direct funds in your merchant account with your merchant service provider". | S01-V-027 (S01-BC-051); S01-V-612 (S01-BC-069); S01-V-026 (S01-BC-023); S01-V-532 (S01-BC-088) |

*(The coordinator's reading, set against phase C's.)*
- **Phase C reads the cause as vendor choice.** Salla and Zid both name the platform itself, and Zid's gap stops them being shown to agree. Shopify names Global-e and BigCommerce a PayPal business account, each missing from the other's set.
- **Every platform names the platform itself.** Each puts the funds in a balance or account under its own name or its payment product's. Phase C's rule for "same" counts all of these as one party, the platform itself.
- **Three also name who holds behind it:** Stripe, Adyen, Global-e, PayPal, and pooled accounts at financial providers. For Salla and Zid, who holds behind the balance is not stated. The pages that would say so are with you (see the last section).
- **So the options below aren't groups of platforms.** They are where the money sits, and the references combine them: phase C gives Salla, Zid and Shopify letter `A` (their holders coexist in one store), and BigCommerce and WooCommerce `B` (one per market, store or plan).

## What Yemen shows

These are Stage 1's states for today, at `4e3f3dd`. Stage 1's independent reviewer checked each one against its quotes, and each was fixed where it was wrong (`studies/yemen-cases/review-independent.md`, "Check of S-01's axes" and "Check of the S-01 entry's axes").

**Processors:**
- The references' processors that Stage 1 covers don't serve a merchant in Yemen (YA-62):
  - "Unavailable @ Stripe's service";
  - "Not available, a request to add it open @ WooPayments's service";
  - "Unavailable @ Zid Pay Kuwait (Zid)'s service";
  - "Sending from Yemen @ PayPal's service", and PayPal "cannot receive money" (YK-514).
- Stage 1 has nothing on the references' other processors, such as Adyen, Global-e, Braintree, Network International and BitPay.
- A card acquirer works in Yemen: SabaCard offers "acquiring of local and international Visa and Mastercard cards" (YK-161).

**Who may hold others' money:**
- Who may provide e-money and electronic payment services (YA-102):
  - "banks and licensed non-bank institutions @ the internationally recognized government's area";
  - "banks and non-bank institutions @ Houthis' area".

  A third part, "banks only @ Central Bank of Yemen's area", is the undivided central bank's rule of 2014. Both areas' later rules replace it.
- A provider licence in the government's area needs "a joint-stock company with paid-up capital of at least 500 million rials, 750 million for a system operator" (YK-515). Such a provider may offer "Transfers, collections, prepaid cards, remittances, payment instruments and e-money" (YK-87).
- Who licenses: "the central bank in Aden @ the internationally recognized government's area" (YA-103). The funds behind e-money are "held at a bank" (YA-106).
- Banks answer to "The Sana'a central bank's" licence and rules in the Houthis' area, and to "The Aden central bank's" in the government's area. Institutions working in both answer to "Both central banks'" (YA-44).

**Wallets:**
- Licences are split by area (YA-217): "ONE Cash licensed by CBY-Sana'a @ Houthis' area"; "ONE Cash's licence request not accepted by CBY-Aden @ the internationally recognized government's area".
- In June 2024 the Aden central bank barred dealing with 12 named wallets. Today, "the ban on the 12 wallets reversed" (YA-26). The reversal lifts the bar. It doesn't say that Aden licensed them.
- So in the government's area, Stage 1 shows no non-bank wallet licensed by the Aden central bank. This is the reviewer's reading.
- Wallets take online payments at many sellers (YA-68). ONE Cash offers merchants "receiving payments, paying merchants, cash out, refunds, cash in and transfers to bank accounts" (YA-109).

**How buyers pay:**
- Cash on delivery is available at most sellers Stage 1 records (YA-128). One survey gives "cash on delivery, preferred by 74 percent of 180 Bazzarry users surveyed @ Aden" (YA-129).
- A courier collects for merchants: "available to business accounts @ Torod's service" (YK-203).
- Buyers pay sellers into the seller's own account: "accepted, by money transfer or to the store's Kuraimi accounts @ Dakhm store's service"; "in advance, to the seller's account @ Sana'a" (YA-131).
- Between banks, electronic payments are "none, only cash, cheques or within one institution @ government-controlled areas" (YA-126).

**Currency:**
- The rial's notes differ by area (YA-15): "old notes only, Aden's new notes barred @ Houthis' area"; "all notes, new and old, legal tender @ the internationally recognized government's area".
- Its rate differs about threefold: "YER 1,562 buying, 1,567 selling @ Aden" against "YER 533 @ Sana'a" (YA-01).
- Wallets hold several currencies, such as "the rial, Saudi riyal and US dollar @ ONE Cash's service" (YA-86).

**Sanctions:**
- The Houthis are designated "FTO and SDGT @ the United States' area" (YA-27).
- OFAC's assurance that trade with Yemenis isn't targeted is "withdrawn" (YK-22). Personal or humanitarian transfers are "allowed if the recipient is not on a sanctions list" (YK-23).
- Sanctions are "named as a limit on e-commerce" (YK-24).

## Decision 1: who holds the merchant's funds (S01-VP-01)

**The question** (phase C): "Between the buyer's payment and the payout, who should hold a merchant's funds in Sharrwah: a balance Sharrwah keeps for the merchant, the payment processor's accounts, or the provider of each payment method?"

**Why it is yours.** Phase C's cause is vendor choice. Getting it wrong is expensive: "money flows, legal structure and partner contracts: the holder is the party the buyer's money goes to first and that settles it to the merchant" (S01-SA-003, S01-WC-120). So the rule table gives "a decision for the founder, on a recommendation". It also gives "the platform carries all the variants at once" and "a variation point behind one interface, bound per market, store or plan".

**The evidence:** "What the references do", above.

**Yemen's mark: `unknown`,** in every case (`yemen-marks.tsv`).
- **Shown to fail:**
  - Stripe's variants (S01-V-009, S01-V-010, S01-V-012 to S01-V-014) and WooPayments' (S01-V-015), on YA-62;
  - Zid Pay's balance (S01-V-023), on Q2 and YA-62: Zid Pay is for merchants in Saudi Arabia and Kuwait;
  - Global-e (S01-V-001, S01-V-002), Adyen (S01-V-006) and BigCommerce Payments (S01-V-027), on Q2: the places they name leave out the Yemeni market.
- **Can't be shown either way,** because some or all of their statements state no condition:
  - Shopify's processors and financial services providers (S01-V-003 to S01-V-005);
  - Stripe's pooled accounts (S01-V-008, S01-V-011);
  - Salla's balances and wallet (S01-V-016, S01-V-018, S01-V-020, S01-V-021, S01-V-657);
  - BigCommerce's PayPal business account, and "merchant account with your merchant service provider" (S01-V-026, S01-V-532).
- **Zid's wallet, for its courier service's cash on delivery** (S01-V-656), turns on whether that service, زد شب, serves a merchant in the Yemeni market. Nothing settles it. Its cash on delivery is "غير متاح" (not available) for international shipping (S01-ZD-126).
- **The marks are about each arrangement, not about the platform.** Salla's platform, for one, is "متاحة حاليًا في السعودية والإمارات فقط" (currently available only in Saudi Arabia and the UAE; S01-SA-189).

**The options** *(the coordinator's grouping of phase C's three answers)*:

| Option | Where the money sits | What it needs built | What it needs from outside, in Yemen |
| --- | --- | --- | --- |
| **A. Sharrwah holds a balance for the merchant** | in accounts in Sharrwah's name, with a balance per merchant, as Salla's and Zid's balances present it | a ledger of merchant balances; collection into Sharrwah's accounts; payouts; reconciliation | A licence, or a licensed partner that holds the money for Sharrwah. In the government's area: a joint-stock company with 500 million rials paid up (YK-515), licensed by the Aden central bank (YA-102, YA-103), with the funds held at a bank (YA-106). In the Houthis' area: a licence from the Sana'a central bank (YA-102, YA-217). One area's licence hasn't carried to the other (YA-217). |
| **B. A payment processor holds, in an account the merchant opens through Sharrwah** | with the processor, as Stripe, Adyen, Global-e and PayPal hold for Shopify, WooCommerce and BigCommerce | an integration with the processor; onboarding merchants to it; showing its balance | A processor that serves merchants in Yemen. None that Stage 1 covers does (YA-62, YK-514). |
| **C. The provider of each payment method holds, in the merchant's own account with it** | with each provider: as BigCommerce's "merchant account with your merchant service provider" (S01-V-532), and Salla's cash on delivery through an outside courier, settled "مباشرة بين التاجر وشركة الشحن" (directly between the merchant and the shipping company; S01-V-038) | an integration with each provider; one interface over them; showing the merchant each provider's balance | A contract between the merchant and each provider: wallets that take online payments (YA-68, YA-109), couriers that collect (YK-203), and the merchant's own bank account (YA-131). Which wallets a merchant can use may depend on their area (YA-217, YA-26). |
| **Defer** | not decided | the interface only | none now |

**The coordinator's recommendation: C for Yemen now, behind one interface that can also carry A or B, bound per market.**
- **What phase D shows working in Yemen is C's arrangement.** A courier collects and settles cash on delivery (Decisions 2 and 4). A card acquirer pays out (Decision 3). The buyer pays into the merchant's own bank account (S01-VP-05 and Decision 7). Phase D shows no arrangement for who holds the funds working there.
- **B** needs a processor that serves merchants in Yemen. None that Stage 1 covers does, and Stage 1 has nothing on the rest.
- **A** is open to a licensed non-bank in both areas. But it needs a joint-stock company with 500 million rials paid up, a licence from each area's central bank, and the funds held at a bank. If A turns out wrong after launch, the money flows and the legal structure must change, which is why phase C rates this item expensive.
- **The interface** keeps A and B open per market, as phase C's rule gives. Either can then be switched on where Sharrwah or a partner holds a licence, or where a processor serves the market.

**Your answer:** A, B, C or defer. Say if your answer should also settle the decisions that follow from it.

## What Decision 1 implies for the others

*(The coordinator's reading.)* Each row is a later decision. Each column gives its answer under one option of Decision 1, as the references pair them. You can let your answer to Decision 1 settle these, or answer each one below.

| Decision | A. Sharrwah holds | B. A processor holds | C. Each provider holds | Defer |
| --- | --- | --- | --- | --- |
| 2. Who settles | Sharrwah | the processor | each provider | set per market |
| 3. Who sends payouts | Sharrwah | the processor | each provider, or the merchant withdraws from their own account with it | set per market |
| 4. Who collects | Sharrwah's payment service | the processor | each provider | set per market |
| 5. Agency | Sharrwah receives and holds funds on the merchant's behalf: decide with the licence | the merchant appoints the processor; Sharrwah may be appointed to instruct it | no agency role | set per market |
| 6. Who deducts | Sharrwah | the processor, Sharrwah's fees included | each provider its own; Sharrwah bills its own fees apart | set per market |
| 7. Accounts | an account with Sharrwah | an account with the processor, opened through Sharrwah | an account with each provider, linked through Sharrwah | set per market |
| 8. Payout timing | one timing Sharrwah sets | the processor's | each provider's | set per market |
| 9. Deducted or billed apart | Sharrwah deducts before payout | the processor deducts before payout | each provider deducts its own; Sharrwah bills its fees apart | set per market |
| 10. Funds at termination | Decision 10 applies | the processor's terms | each provider's terms | set per market |
| 11. When funds go back to buyers | Decision 11 applies | the processor's terms | each provider's terms | set per market |
| 12. Security interest | Decision 12 applies | the processor's terms | each provider's terms; Sharrwah takes none | set per market |

Decisions 13 (installments) and 14 (currency) don't follow from Decision 1.

## Decisions 2 to 12

Each takes the form of Decision 1. Under every one, "defer" is also open, and each option needs what Decision 1's option of the same letter needs.

### 2. Who settles the funds to the merchant (S01-VP-02)

- **The question** (phase C): "Which party should settle a merchant's funds to the merchant in Sharrwah: Sharrwah, a payment processor or acquirer, or the provider of each payment method (a BNPL company, a shipping company for cash on delivery)?"
- **Why it is yours:** vendor choice, and expensive: "money flows and partner contracts: the settling party moves the funds to the merchant under its own terms" (S01-SH-019, S01-WC-115).
- **The evidence:**
  - the platform itself: Salla's own English, "Electronic payments is a Salla service that processes payments in your store directly, settling transactions with banks and your approved payment methods automatically" (S01-V-533, S01-SA-139). For its courier service, Zid: "تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر" (Zid collects the amounts from the end customers and transfers the total dues to the merchant's wallet; S01-V-658, S01-ZD-069);
  - a processor: "The Payment Processor retains sole and exclusive responsibility for Payment Processing, including the settlement of funds" (S01-V-028, S01-SH-019);
  - the provider of each payment method: for a courier outside Salla's shipping labels, "تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين" (cash on delivery is settled directly between the merchant and the shipping company, under their agreement; S01-V-038, S01-SA-091). For Tamara, "تتم تسوية كافة المدفوعات من قبل تمارا" (all payments are settled by Tamara; S01-V-037, S01-SA-104).
- **Yemen's mark: carried only with a partner,** through S01-V-038. In Yemen a courier collects for business accounts: Torod, "وإمكانية تحصيل الأموال من المستلمين" (and the possibility of collecting money from recipients; YK-203, YE-E613).
- **The options:** A. Sharrwah; B. a payment processor or acquirer; C. the provider of each payment method.
- **The coordinator's recommendation: C,** as Decision 1's recommendation implies, and as phase D shows working in Yemen with a courier.
- **Your answer:** A, B, C or defer.

### 3. Who sends payouts to the merchant's bank account (S01-VP-03)

- **The question** (phase C): "Which party should send payouts to a merchant's bank account in Sharrwah: Sharrwah, the payment processor, or the provider of each payment method or sales channel?"
- **Why it is yours:** vendor choice, and expensive: "money flows and partner contracts: the sender of payouts is the party that pays the merchant's bank account" (S01-SA-038, S01-ZD-035).
- **The evidence:**
  - the platform itself: "تحوَّل سلة مستحقات المدفوعات الإلكترونية والمدفوعات عند الاستلام إلى حسابك البنكي" (Salla transfers the proceeds of electronic payments and cash on delivery to your bank account; S01-V-055). "تقوم زد باي بتحصيل المبالغ المحصلة إلى حسابك البنكي بشكل دوري 3 مرات في الأسبوع" (Zid Pay moves the collected amounts to your bank account three times a week; S01-V-060);
  - a processor: "After a payout is issued by the payment processor" (S01-V-045, S01-SH-074);
  - the provider of each payment method or sales channel: "تقوم تابي بالتحويل لمتجرك أولاً والتحصيل من عملائك لاحقاً" (Tabby pays your store first and collects from your customers later; S01-V-056). "يتم الدفع إلى ترينديول ثم تقوم ترينديول بتحويل الأموال إليك" (payment goes to Trendyol, which then transfers the money to you; S01-V-064). For the standalone PayPal gateway, "Funds are deposited immediately into your PayPal account. You can request a withdrawal to your bank at any time" (S01-V-616).
- **Yemen's mark: carried only with a partner,** through S01-V-059. When a card payment on Salla's point-of-sale app succeeds, it becomes a bank transfer "من خلال مزود الخدمة مثل جيديا" (through the service provider, such as Geidea; S01-SA-113). In Yemen, SabaCard offers "acquiring of local and international Visa and Mastercard cards" (YK-161).
- **The options:** A. Sharrwah; B. the payment processor; C. the provider of each payment method or sales channel.
- **The coordinator's recommendation: C.** The provider pays the merchant, or the merchant withdraws from their own account with it. Sharrwah sends no payouts.
- **Your answer:** A, B, C or defer.

### 4. Who collects the buyer's payment (S01-VP-04)

- **The question** (phase C): "Which party should collect the buyer's payment in Sharrwah: Sharrwah's own payment service, a payment processor or acquirer, or the provider of each payment method (a BNPL company, a shipping company for cash on delivery)?"
- **Why it is yours:** vendor choice, and expensive: "partner contracts and money flows: the collector of the buyer's payment is the processor or provider the merchant contracts with" (S01-SH-007, S01-SA-101).
- **The evidence:**
  - the platform itself: "خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر" (a service Salla provides to process your store's payments directly; S01-V-085). For its courier service, Zid: "حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم" (where Zid collects the amount from the customer on delivery, on the merchant's behalf; S01-V-096, S01-ZD-069);
  - a processor: "The Payment Processor's role in relation to the Payments Services is to accept and process payment transactions" (S01-V-069). "All Shopify-supported payment methods rely on third-party providers to process your transactions" (S01-V-068);
  - the provider of each payment method: "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة" (payments made through Tabby are collected through Tabby, not through Salla Payments; S01-V-088, S01-SA-101). For a courier outside Salla's shipping labels, "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة" (Salla doesn't collect cash on delivery amounts in this case; S01-V-093, S01-SA-090).
- **Yemen's mark: carried only with a partner,** through S01-V-093: the courier collects, and in Yemen Torod does so for business accounts (YK-203).
- **The options:** A. Sharrwah's own payment service; B. a payment processor or acquirer; C. the provider of each payment method.
- **The coordinator's recommendation: C.** The wallet, the courier, or the merchant's own bank account collects.
- **Your answer:** A, B, C or defer.

### 5. Whether Sharrwah acts as the merchant's agent (S01-VP-06)

- **The question** (phase C): "Should Sharrwah act as the merchant's agent towards payment processors and providers, or take no agency role and leave agency to the processor?"
- **Why it is yours:** vendor choice, and expensive: "legal structure and partner contracts: an agent receives, holds or gives instructions on the merchant's funds on the merchant's behalf" (S01-WC-120, S01-SH-001).
- **The evidence:**
  - Shopify: "You hereby appoint us as your agent to deliver information and instructions on your behalf to one or more payment processors" (S01-V-112, S01-SH-001);
  - WooCommerce's Stripe terms: "User appoints Stripe as User’s agent for the limited purpose of directing, receiving, holding and settling funds" (S01-V-117);
  - Zid's own English, for Saudi Arabia: "Merchants authorize Zid to execute payment processes on their behalf upon using the service." (S01-V-122, S01-ZD-007);
  - BigCommerce: "No agency, partnership, joint venture or employment relationship is created by this Agreement or your use of the Services" (S01-V-623, S01-BC-128).
- **Yemen's mark: `unknown`.** Stripe's variants fail on YA-62, and Adyen's and Shopify's processors' on Q2. Shopify's appointment of itself, WooCommerce's Stripe clause and BigCommerce's "No agency" state no condition (S01-V-112, S01-V-117, S01-V-120, S01-V-623). Zid's (S01-V-122) turns on its courier service's conditions, which nothing settles.
- **The options:**
  - act as the merchant's agent. This needs a legal structure in which Sharrwah receives, holds or instructs on the merchant's funds on the merchant's behalf, set with the licence or the processor;
  - take no agency role, and leave agency to the processor or provider. This needs nothing from outside.
- **The coordinator's recommendation: no agency role,** under C, as in BigCommerce's terms. Under A, decide this with the licence. Under B, the processor's terms set it.
- **Your answer:** act as agent, no agency role, or defer.

### 6. Who deducts fees, refunds and other amounts owed (S01-VP-09)

- **The question** (phase C): "Which party should deduct fees, refunds and other amounts owed from a merchant's funds in Sharrwah: Sharrwah, the payment processor, or the provider of each payment method?"
- **Why it is yours:** vendor choice, and expensive: "money flows and partner contracts: the deducting party takes fees and amounts owed out of the merchant's funds before payout" (S01-SH-025, S01-ZD-023).
- **The evidence:**
  - the platform itself: "يحق لزد الخصم الآلي والمباشر من أي مبالغ تُودع أو تُدخل في محفظة التاجر" (Zid may deduct automatically and directly from any amounts deposited in the merchant's wallet; S01-V-160);
  - the platform or a processor: "we may deduct, or request that a Payment Processor deduct, from any accounts associated with your Shopify Payments Account" (S01-V-152);
  - a processor: "At the Stripe Connect Platform’s request, Stripe may deduct from User’s Stripe Account balance" (S01-V-155);
  - the provider of each payment method: "يتم خصم المبلغ مباشرة من تمارا وليس من رصيد مدفوعات سلة" (the amount is deducted directly from Tamara, not from the Salla Payments balance; S01-V-165). "تقوم أمازون بخصم الرسوم والعمولات مباشرة من مبلغ البيع" (Amazon deducts fees and commissions directly from the sale amount; S01-V-163).
- **Yemen's mark: carried unchanged,** through Zid's wallet (S01-V-160). The wallet's own conditions for merchants outside the Kingdom are met under Q2 (S01-ZD-121, S01-ZD-122). That is all the mark shows. It doesn't show that a buyer's payment reaches the wallet for such a merchant: Zid Pay is for merchants in Saudi Arabia and Kuwait (S01-ZD-112), and Zid's courier service doesn't take cash on delivery for international shipping (S01-ZD-126). The same holds for every mark below that rests on Zid's wallet.
- **The options:** A. Sharrwah; B. the payment processor; C. the provider of each payment method.
- **The coordinator's recommendation: C.** Each provider deducts its own fees, and Sharrwah, holding nothing, bills its own fees apart.
- **Your answer:** A, B, C or defer.

### 7. Which accounts a merchant holds (S01-VP-11)

- **The question** (phase C): "Which accounts should a Sharrwah merchant hold for payments: an account with Sharrwah only, an account with each payment processor or provider opened through Sharrwah, or both?"
- **Why it is yours:** vendor choice, and expensive: "data model, legal structure and partner contracts: the accounts decide who owns the merchant's balance and which party the merchant contracts with" (S01-SH-021, S01-WC-019).
- **The evidence:**
  - Shopify: "you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors for Payment Processing" (S01-V-173);
  - WooCommerce: "This creates a Stripe Express account that is connected to the WooPayments service." (S01-V-180);
  - Zid: "رصيد كافي في حسابه لدى زد باي" (a sufficient balance in his account with Zid Pay; S01-V-190);
  - Salla: "لا يتطلب تفعيل مدفوعات سلة توقيع عقود مع طرف ثالث أو فتح حساب في بنك محدد" (turning on Salla Payments needs no contract with a third party, and no account at a particular bank; S01-V-188);
  - BigCommerce: "You will control and direct funds in your merchant account with your merchant service provider" (S01-V-554).
- **Yemen's mark: carried unchanged,** through S01-V-195. The merchant runs Zid's bank transfer service "بصفتك مالك الحساب" (as the account's owner; S01-ZD-075), and in Yemen buyers pay sellers into the seller's own account (YA-131). Between banks, though, electronic payments are "none, only cash, cheques or within one institution" in government-controlled areas (YA-126). So the mark doesn't show that a buyer at any bank can pay.
- **The options:** an account with Sharrwah only (A); an account with each processor or provider, opened through Sharrwah (B or C); or both.
- **The coordinator's recommendation:** an account with each provider, linked through Sharrwah (C). A Sharrwah account serves only Sharrwah's own billing.
- **Your answer:** Sharrwah only, each provider, both, or defer.

### 8. Payout timing (S01-VP-15)

- **The question** (phase C): "Should the time from a buyer's payment until funds can be paid out be one timing Sharrwah sets for its merchants, or follow each payment provider's settlement time by country, risk level and payment method?"
- **Why it is yours:** vendor choice, and expensive: "partner contracts and money flows: the time until funds are available is set by the settling processor by country, risk level and payment method" (S01-SH-063, S01-WC-032).
- **The evidence:**
  - Shopify: "The minimum settlement time depends on your region, risk level, and the payment method used." (S01-V-329);
  - WooCommerce: "The time those funds take to flow through your account is called the “pending period”, and its length depends on your WooPayments account country." (S01-V-336);
  - Zid: "الوقت الذي يستغرقه تحويل المبالغ من المحفظة إلى حساب التاجر البنكي من يومين إلى خمسة أيام عمل" (the time a transfer from the wallet to the merchant's bank account takes is two to five working days; S01-V-343);
  - BigCommerce, for Braintree: "Funds should appear in your bank account 2-5 days after the transaction has settled" (S01-V-637).
- **Yemen's mark: carried unchanged,** through Zid's wallet (S01-V-343), on the wallet's own conditions only.
- **The options:** one timing Sharrwah sets (A); each provider's settlement time (B or C).
- **The coordinator's recommendation:** each provider's settlement time, shown to the merchant per payment method (C).
- **Your answer:** one timing, each provider's, or defer.

### 9. Deducted before payout, or billed apart (S01-VP-19)

- **The question** (phase C): "Should fees, refunds, chargebacks and other amounts owed be deducted from a merchant's funds before payout in Sharrwah, or billed apart, and by which party?"
- **Why it is yours:** vendor choice, and expensive: "money flows and data model: what is netted from a payout and what is billed apart changes how the merchant's balance is computed" (S01-SH-094, S01-BC-124).
- **The evidence:**
  - deducted before payout: "Each transaction incurs processing fees that are deducted from your earnings before the payout is sent." (Shopify; S01-V-452). "Stripe will transfer settlement funds for Transactions, net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe" (S01-V-467);
  - fees on moving the funds: "في حال سحب رصيد من المحفظة، سيتم احتساب رسوم تحويل لحسابكم البنكي والبالغة 8.05 ريال شاملة الضريبة" (a withdrawal from the wallet carries a transfer fee to your bank account of 8.05 riyals, tax included; S01-V-472). Zid takes a deposit fee "بقيمة 3 ريال لكل عملية تحصيل" (of 3 riyals for each collection; S01-V-477);
  - billed apart: BigCommerce's own fee, "billed monthly in arrears (after the service period) as a separate line item on your invoice" (S01-BC-124, cited by phase C).
- **Yemen's mark: carried unchanged,** through Zid's wallet transfer fee (S01-V-480), on the wallet's own conditions only. The variant's words give "9 ريال ... في حال كانت الحوالة داخل السعودية" (9 riyals, for a transfer inside Saudi Arabia). The same statements give 50 riyals for a transfer outside Saudi Arabia (S01-ZD-058). Zid's automatic deduction from wallet deposits (S01-V-481) also qualifies.
- **The options:** A. Sharrwah deducts before payout; B. the processor deducts before payout; C. each provider deducts its own, and Sharrwah bills its fees apart.
- **The coordinator's recommendation: C.** Sharrwah has no payout to net its fees from, so it bills them apart.
- **Your answer:** A, B, C or defer.

### 10. Funds held when the service ends (S01-VP-20)

- **The question** (phase C): "When a merchant's account or payment service ends, what should Sharrwah do with funds it still holds: pay them to the merchant's bank account, hold them until refunds, chargebacks and fees are settled, or return them to the buyers?"
- **Why it is yours:** vendor choice, and expensive: "money flows and legal structure: at termination the funds still held go to the merchant, stay held, or go back to the buyers" (S01-SH-033, S01-ZD-024).
- **The evidence:**
  - paid out: Zid's answer on turning Zid Pay off, "نعم يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي" (yes, the amount in the merchant's balance is transferred to the bank account; S01-V-496). Shopify: "Any funds in the Financial Services Provider's custody will be paid out to you subject to the Payment Processor Terms." (S01-V-492);
  - held: Shopify, "a Payment Processor may elect to continue to hold any funds deemed necessary, pending resolution of any other terms or obligations defined in this Agreement" (S01-V-491). Zid, for its مزيد service, "يحق لشركة زد احتجاز الأموال ليتم تسوية العمليات المعلقة" (Zid may hold the funds so that pending operations are settled; S01-V-498);
  - returned to the buyers: Salla, "إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين" (returning any pending electronic payments to the consumers; S01-V-495).
- **Yemen's mark: `unknown`.** Zid Pay's variants fail on Q2 and YA-62, and Adyen's and Shopify's reserve terms (S01-V-493, S01-V-605) on Q2. Shopify's and Salla's others state no condition (S01-V-491, S01-V-492, S01-V-495). WooCommerce's (S01-V-494) and Zid's مزيد (S01-V-498) turn on conditions nothing settles.
- **The options:** pay the funds to the merchant's bank account; hold them until refunds, chargebacks and fees are settled; or return them to the buyers. They arise for Sharrwah only under Decision 1's A. Under B or C, the processor's or provider's terms apply.
- **The coordinator's recommendation:** under C, Sharrwah holds nothing at the end, and its terms say each provider's terms apply. Under A: hold what pending refunds, chargebacks and fees need, and pay the rest to the merchant's bank account, as Shopify's terms do (S01-V-491, S01-V-492).
- **Your answer:** pay out, hold until settled, return to the buyers, or defer.

### 11. When funds go back to the buyers (S01-VP-21)

- **The question** (phase C): "On what conditions should funds Sharrwah holds go back to the buyers instead of to the merchant: a breach of the platform's terms, verification or registration not completed in time, payments whose legitimacy is not shown, or a demand by a processor or regulator?"
- **Why it is yours:** vendor choice, and expensive: "money flows and legal structure: the funds go back to the buyers instead of to the merchant, under the platform's or the processor's terms" (S01-ZD-024, S01-SH-106).
- **The evidence:**
  - a breach of the terms: Salla, on a breach of the first clause of its Article Ten, may take steps including "إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين" (returning any pending electronic payments to the consumers; S01-V-504, S01-SA-082);
  - details not corrected: Zid, "وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين" (if they are not corrected, the account is disabled and all amounts returned to the end customers; S01-V-505);
  - registration not completed within 14 days: Zid, "وستعاد المبالغ المحصلة لمصادرها -العميل النهائي-" (and the collected amounts will be returned to their source, the end customer; S01-V-510, S01-ZD-024);
  - a check not passed: Shopify, "If you do not pass, funds may be held or refunded to your customers, in accordance with applicable law and Network Rules." (S01-V-502).
- **Yemen's mark: `unknown`.** Zid Pay's variants fail on Q2 and YA-62, and Shopify's on Q2. Salla's (S01-V-504) states no condition, and WooCommerce's (S01-V-503) turns on a condition nothing settles.
- **The options:** any of the conditions in the question. They arise for Sharrwah only under Decision 1's A. Under B or C, the processor's or provider's terms apply.
- **The coordinator's recommendation:** under C, none for Sharrwah, and its terms say each provider's terms apply. Under A, decide this with the licence.
- **Your answer:** the conditions you choose, or defer.

### 12. A security interest over the merchant's funds (S01-VP-10), from phase D

- **The question** (phase D): "Who, if anyone, holds a security interest over the merchant's funds between the buyer's payment and the payout, where Shopify Payments and Stripe, which hold one in the references, are not offered."
- **Why it is yours.** Phase D's mark is `no placement` in every case, and its brief then makes it a product gap and a founder item: "Where neither Shopify Payments nor Stripe is offered, no reference places a security interest over the merchant's funds held between the buyer's payment and the payout: every reference's lien or security interest belongs to one of those two services." Phase C's cause is `unknown`, because Salla, Zid and BigCommerce have only gaps. It rates the item expensive: "legal structure and partner contracts: a lien or security interest gives a party rights over the merchant's funds" (S01-SH-023, S01-WC-112).
- **The evidence:**
  - Shopify Payments: "you grant us a first priority lien and security interest on all funds processed and deposited" (S01-V-167);
  - Stripe, for users in the United States: "User grants the security interest to SPC" (S01-V-169);
  - Stripe, for users in Singapore: "User acknowledges that Stripe also has a lien over all funds Stripe holds on User’s behalf" (S01-V-549).
- **Yemen's mark: `no placement`.** Shopify Payments' lien fails on Q2: Shopify Payments is for a business located in its Designated Countries, none of which takes in the Yemeni market. Stripe's fail on Q2 and on YA-62, "Unavailable @ Stripe's service".
- **The options:** no one; Sharrwah; or the provider of each payment method, under its own terms.
- **The coordinator's recommendation:** under C, Sharrwah takes none, and each provider's terms apply to the funds it holds. Under A, decide this with the licence.
- **Your answer:** no one, Sharrwah, each provider, or defer.

## Decisions that don't follow from Decision 1

### 13. When the merchant is paid under installments (S01-VP-22)

- **The question** (phase C): "Under instalment or pay-later payments, when should a Sharrwah merchant be paid: in full after capture with the platform's other payouts, up front while the buyer owes the instalment provider, or on the instalment provider's own schedule under its agreement with the merchant?"
- **Why it is yours:** vendor choice, and expensive: "partner contracts and money flows: when the merchant is paid is set by the agreement with the instalment provider (S01-SA-101, S01-SA-104) or by the platform's own payouts (S01-SH-054)".
- **The evidence:**
  - Shopify: "After you capture the payment for an order placed using Shop Pay Installments, you receive full payment for your order with your other Shopify Payments transactions excluding the fee incurred for using Shop Pay Installments." (S01-V-514);
  - BigCommerce: "Allow customers to pay in installments with Pay in 4 and Pay Monthly3 while you get paid up front" (S01-V-512). "This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid" (S01-V-653);
  - Salla, for Tabby: "تقوم تابي بالتحويل لمتجرك أولاً والتحصيل من عملائك لاحقاً" (Tabby pays your store first and collects from your customers later; S01-V-516). For Tamara: "كما تتم تسوية كافة المدفوعات من قبل تمارا حسب الجدول الزمني المتفق عليه مع المتجر" (and all payments are settled by Tamara on the schedule agreed with the store; S01-V-518).
- *(The coordinator's reading.)* In every reference, the merchant is paid the full amount rather than in installments, and the installment provider carries the buyer's debt. The options differ in who pays and when.
- **Yemen's mark: `unknown`.** PayPal (S01-V-653) fails on YK-514 and YA-62, WooPayments (S01-V-515) on YA-62, and BigCommerce's Pay in 4 and Tabby in the UAE (S01-V-512, S01-V-519) on Q2. Shop Pay Installments, Tabby and Tamara (S01-V-514, S01-V-516 to S01-V-518) turn on conditions nothing settles, and S01-V-513 states none. The Yemen evidence names no installment provider.
- **The options:**
  - in full after capture, with the platform's other payouts. This needs Sharrwah or a processor to pay out (Decision 1's A or B);
  - up front, while the buyer owes the installment provider;
  - on the provider's own schedule, under its agreement with the merchant.
- **The coordinator's recommendation: defer.** No installment provider is shown in Yemen. If one is offered, pay the merchant on the provider's own schedule under its agreement with the merchant, which fits C.
- **Your answer:** one of the three, or defer.

### 14. Currency (S01-VP-23)

- **The question** (phase C): "In which currency should Sharrwah hold and pay out a merchant's funds: the currency of the merchant's local bank account in each market, one base currency with conversion, or several currencies per merchant?"
- **Why it is yours:** vendor choice, and expensive: "data model and money flows: the currency of the held funds and of the payout decides balances per currency and any conversion" (S01-WC-048, S01-BC-014).
- **The evidence:**
  - the local account's currency: Salla in the UAE, "الحساب لدى بنك إماراتي و بعملة الدرهم الإماراتي" (the account at a UAE bank, in UAE dirhams; S01-V-526). Shopify: "You need a Hong Kong SAR dollar bank account for receiving payouts" (S01-V-608);
  - one base currency: "عند تفعيل التاجر لبوابة دفع سلة، يتم استقبال جميع المدفوعات بالريال السعودي" (when a merchant turns on Salla's payment gateway, all payments are received in Saudi riyals; S01-V-609). WooPayments: "it will be converted into your default currency" (S01-V-522);
  - several per merchant: WooPayments lists several payout currencies in some countries (S01-V-524).
- **Yemen's mark: carried unchanged,** through Zid's wallet (S01-V-528), on the wallet's own conditions only: "لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني)" (the amounts in the wallet can't be withdrawn in these currencies: the Omani rial, the UAE dirham, the Kuwaiti dinar and the Bahraini dinar). The Yemen facts are under "Currency" above: the rial's notes and rate differ by area (YA-15, YA-01), and wallets hold several currencies (YA-86).
- **The options:** the currency of the merchant's local bank account in each market; one base currency with conversion; or several currencies per merchant.
- **The coordinator's recommendation: several currencies per merchant,** with the rial recorded apart by the area its funds are held in.
  - The rial's notes differ by area, and its rate by about three times. One base currency with conversion would mix the two.
  - Q2 names "a currency circulating in two editions" among the things with no product-class precedent, which are "named as design decisions for the founder".
- **Your answer:** local account currency, one base currency, several per merchant, or defer.

## Variation points that aren't founder decisions

Phase C's rule table settles these. "What follows" gives every rule each one takes.

| Variation point | Cause | What follows | Yemen's mark (phase D) |
| --- | --- | --- | --- |
| S01-VP-05, "pay you directly" | no difference | a commonality, carried as the references carry it; the platform carries all the variants at once | carried unchanged, by direct bank transfer into the merchant's own account (S01-V-102, YA-131) |
| S01-VP-07, "Reserve" | unknown | a variation point behind one interface, bound per market, store or plan; kept open as a variation point until evidence settles it | unknown |
| S01-VP-08, "withhold" | unknown | the platform carries all the variants at once; kept open as a variation point until evidence settles it | unknown |
| S01-VP-12, "licensed" | market, named rule | a variation point behind one interface, bound per market, store or plan | unknown |
| S01-VP-13, "terms of service" | maturity | the platform carries all the variants at once; a variation point behind one interface, bound per market, store or plan; kept open as a variation point until evidence settles it | carried unchanged, through WooCommerce, Inc. for residents outside its Designated Countries (S01-V-244) |
| S01-VP-14, "payout schedule" | vendor choice, cheap to change | a variation point behind one interface, bound per market, store or plan; left to the build | carried unchanged, through Zid's wallet (S01-V-579), on its own conditions only |
| S01-VP-16, "Minimum payout amount" | vendor choice, cheap to change | a variation point behind one interface, bound per market, store or plan; left to the build | unknown |
| S01-VP-17, "reserve" | market, named rule | a variation point behind one interface, bound per market, store or plan | unknown |
| S01-VP-18, "held" | market, named rule | the platform carries all the variants at once | carried unchanged, through Zid's wallet (S01-V-445), on its own conditions only |

## What this entry rests on, and what would change it

**The Yemen facts were checked.**
- Every Stage 1 fact above was checked against its quotes by Stage 1's independent reviewer, and fixed where it was wrong (`studies/yemen-cases/review-independent.md` and `review-axes.md`).
- Phase D later added axes to `bears-on.tsv` that those checks didn't cover: YA-28, YA-120, YA-122, YA-124 and YA-125. No mark rests on them.

**Which Yemen cases vary these facts.**
- Phase D marked every case that changes an axis a variation point bears on, and no case changes any mark from today's.
- The facts behind the options that no variation point bears on are varied only by past states (`occurred`):
  - YA-102 in YC-184, YC-185 and YC-311;
  - YA-26 in six cases, among them the June 2024 bar (YC-119);
  - YA-44 in YC-146 and YC-342;
  - YA-86 in YC-178 and YC-285.
- Two exceptions:
  - YA-15's YC-101 is `provided for`: the government's area withdrawing notes printed before 2016;
  - three of YA-01's 80 rate cases are `in force` (YC-53, YC-54, YC-57).
- No case varies YA-103, YA-106, YA-109, YA-217 or YK-515.

**What would change this entry:**
- **The pages still with you:** Salla's payment services contract, and Zid's two dashboard pages (`evidence/product-class/to-save-for-s01.md`). They would say who holds behind Salla's and Zid's balances, and which bank holds Zid's wallet.
- **A processor that serves merchants in Yemen** would open option B.
- **A licence, or a licensed partner, for Sharrwah** would open option A.
- **Evidence that an arrangement for who holds the funds serves a merchant in the Yemeni market,** such as Zid's courier service, would settle Decision 1's `unknown` mark.
- **BitPay:** BigCommerce says "cryptocurrency payments are enabled for all merchants" (S01-BC-033). Read as met, BitPay would carry Decisions 2 and 3 unchanged (`notes-d.md`). Stage 1 doesn't settle it.
- **Stage 1's faithfulness pass over every axis,** planned before Stage 4.
