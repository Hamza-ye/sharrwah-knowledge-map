# T-baseline, phase 1: the questions

**What this is.** Phase 1 of the test in `studies/class-model/briefs/T-baseline.md`, which asks what Sharrwah would get wrong if it were built from Shopify's shape alone. It holds the questions only, written before any platform's evidence was read, and answers none of them. Each names a place where building from Shopify's shape alone could make Sharrwah fail in the founder's markets, or force an expensive change later. The founder may cut or add before phase 2, which starts only when the coordinator says so.

**What I read, and only this.** At commit `8e1f5c7`:
- `founder-decisions.tsv`: the first 200 characters of every row's question, and in full lines 3, 8, 16, 18, 19, 20, 22, 25, 26 and 29. The questions rest on lines 8, 16, 19, 20, 25 and 26.
- `studies/yemen-cases/`:
  - in full: `brief.md`, `corrections.md` and `unknowns.tsv`;
  - in part: `axes.tsv` (every axis's name, `today` for 80 axes and the states of 35), `constants.tsv` (the 68 constants a keyword search found, 17 of them in full), `citations.tsv` (about 145 rows, the quotes behind those records; those used here re-read in full), `review-independent.md` (its opening and a few lines) and the first 400 bytes of `notes.md`;
  - the other tables only for their headers.
- The names of the files in `architecture/`, none of them opened.
- No platform's evidence, no captured source under `evidence/`, and nothing else in this repository.

**How the Yemen facts are used.**
- Each Yemen fact used here was checked against its full quote in `citations.tsv`, as `corrections.md` asks of every Yemen fact. Phase 1 reads no evidence, so no captured source was opened. Where a record's quote doesn't settle it, the record is used only as `corrections.md` settles it, or as a reading marked as one. The two records left out for this reason are named where they would have been.
- Records that `corrections.md` corrects are used only as corrected (YA-44, YA-62, YK-124, YK-131, YK-452), and its cautions as cautions (YA-102, YK-514).
- Three questions come from the Yemen cases alone: BT-5, BT-8 and BT-9. Each is marked, so the founder can cut it.

**How each claim is marked.**
- **A fact** carries its source. `D16` is line 16 of `founder-decisions.tsv`. `YA-` ids (axes) and `YK-` ids (constants) are Stage 1's records, and the `YE-` ids after them are the citations whose quotes I checked. "Sources", at the end, gives each one's file at its commit.
- *(reading)*: my reading.
- *(assumption)*: what I take from what I know of commerce in the founder's markets, unchecked here.
- **What I expect of Shopify** is an expectation, not a finding. Phase 2 checks it against Shopify's own evidence.

**Cautions on the Yemen facts.**
- Stage 1's independent review found errors in `today` on 12 of 45 sampled axes (`review-independent.md`). So no fact here rests on an axis's `today`: each is one state, with its own quote and date.
- Much of what is held on how Yemen's wallets' APIs work comes from community-written clients and package pages, not from the providers' own documentation. Each such fact says so.
- Facts carry their sources' dates, and some are old: the card count under BT-7 is for the end of 2019.

## The questions at a glance

| Id | The question, short | Origin | Markets | A late change would touch |
| --- | --- | --- | --- | --- |
| BT-1 | Does an order's payment record stay the same whoever holds the money, with any holder's ledger apart? | D8, D16, D19, D20 | All | how money is held and recorded |
| BT-2 | Can an order show cash on delivery held by the courier, and the courier's settlement with the seller? | D16, D26; Yemen cases; assumption | Yemen; *assumed:* North Africa, Jordan, the GCC | how money is held; how payments and deliveries flow |
| BT-3 | Can an order be placed unpaid, then paid in parts, by several methods, each payment confirmed later? | D16; assumption; Yemen cases | Yemen; *assumed:* Egypt, the Maghreb, Lebanon, the GCC | how orders and payments flow; how money is recorded |
| BT-4 | Can the platform itself run a local provider's API payment (phone number, then a one-time code or PIN) for each seller's own account, credentials kept apart? | D16, D25; assumption; Yemen cases | Yemen; *assumed:* North Africa, Jordan, Lebanon, the GCC's smaller providers | how payments flow; how stores are kept apart |
| BT-5 | Can money say which of two currencies under one ISO code, Yemen's old or new rial, it is in? | **The Yemen cases alone** | Yemen | how money is recorded |
| BT-6 | Can an order keep the currency it was priced in, the one it was paid in, the rate, and the invoice amount the law requires? | assumption; Yemen cases | Yemen; *assumed:* Lebanon, the GCC | how money is recorded; a market's law |
| BT-7 | Can Sharrwah bill sellers who have no card, by payments they push, without deducting or a prepaid balance? | D16, D20; Yemen cases; assumption | Yemen; *assumed:* Algeria, Tunisia, Egypt, Lebanon | how Sharrwah's own money is held and recorded |
| BT-8 | Can a market be an area within a country? | **The Yemen cases alone** | Yemen | a market's law; how payments and deliveries flow |
| BT-9 | Can the platform comply with sanctions area by area? | **The Yemen cases alone** | Yemen | a market's law; where data lives; how stores are kept apart |
| BT-10 | Can one market's stores, or one store, keep their data in the country its law requires? | Yemen cases (a reading); assumption | Yemen *(reading)*; *assumed:* Algeria, Saudi Arabia, Egypt and others | where data lives |
| BT-11 | Can a tax invoice be a record of its own: numbered, fixed once issued, sent to the authority where required? | assumption; Yemen cases | Yemen; *assumed:* Saudi Arabia, Egypt, Jordan, the UAE and others | how money is recorded; a market's law |
| BT-12 | Does the platform keep its own record of who each seller legally is, per market, and whether it was checked? | D16; Yemen cases; assumption | All | identity; a market's law |
| BT-13 | Can a buyer be known by a phone number alone, with an identity per store or across stores? | D26; Yemen cases; assumption | Yemen; *assumed:* all the others | identity |
| BT-14 | Can one basket take goods from several stores, each store's share paid into its own provider account? | D16, D26; Yemen cases | All | how orders and payments flow; how money is held |

## The questions

### BT-1. Who holds the money, and the order's payment record

**The question.** Does an order's payment record stay the same whoever holds the seller's money (its provider, its courier, the seller itself, or later Sharrwah or an account opened through it), with each holder's ledger of balances, holds and payouts kept apart?

**Why it could sink Sharrwah, or cost dearly to change.** The founder chose C in every market at launch, kept A and B off under the guard, and kept room for both: who holds the money is a market's setting, an order's payment record is the same whoever holds it, and a holder's ledger is a separate part, empty under C. A shape that ties the payment record to one holder would make switching a market to A or B a rewrite of its orders' payment history *(reading)*.

**Origin.** The founder's decisions: D16 (Decision 1 and its three defaults), D8 (the guard), D19 (E1 and E2), D20 (default 2 holds while a market runs only C).

**Markets.** All: C in every market at launch (D16); A or B in a market only by the founder's decision (D8, D19), with how Sharrwah's fees are collected there coming to the founder with it (D20).

**What I expect of Shopify** *(an expectation, not a finding)*. An order's transactions take one form whatever the gateway: authorizations, captures, sales and refunds, each naming its gateway, manual ones included. Shopify Payments, an account opened through Shopify (B, in Decision 1's terms), keeps its balance, payouts and disputes as a part of their own, and takes its fees from payouts; with other providers, Shopify's fees go on its own bill.

**What would settle it.** Shopify's developer documentation (an order's transactions; Shopify Payments' balance, payouts and balance transactions), its help (other providers, manual methods, how fees are charged) and its terms (who holds funds under Shopify Payments). Salla's and Zid's developer documentation, help and terms, for the arrangements the region's platforms run. Which arrangements a market allows, and under which licence, is that market's law: in Yemen, per area and with dates, as `corrections.md` states YA-102.

### BT-2. Cash on delivery, held by the courier

**The question.** When a courier collects cash on delivery, can the order show that the courier holds the money, and when and how much it settled to the seller, including deliveries refused or only partly accepted?

**Why it could sink Sharrwah, or cost dearly to change.** Decision 1 names the seller's courier as the holder of cash-on-delivery money until it settles with the seller, and in Yemen it is a main way online buyers pay. If an order knows only "pending" and "paid", sellers can't see what their couriers owe them, and adding a holder between buyer and seller later changes the payment record and the delivery flow together *(reading)*.

**Origin.**
- The founder's decisions: D16 ("for cash on delivery the seller's courier holds it until it settles with the seller"). D26 puts shipping among the services Sharrwah's own company may run; the cash its couriers collected would then be held through Sharrwah, which is A *(reading)*.
- The Yemen cases. YA-129: 74.44% of Bazzarry's customers surveyed in Aden preferred cash on delivery (YE-E622, YE-E623, 2026); most transactions, 61.9 percent of those made online among them, are still made in cash, and cash on delivery is popular (YE-E113, YE-E114, 2025); a blog calls it the most common way to pay (YE-D181, 2025). YA-130: Torod, a delivery service, takes payment on pickup, on delivery or by wallet (YE-E612). Not used: YK-206, whose quote doesn't say which service it is about.
- *Assumption:* cash on delivery is a main way to pay in Egypt, Morocco, Algeria, Tunisia and Jordan, and still common in the GCC.

**Markets.** Yemen; *assumption:* Egypt, Morocco, Algeria, Tunisia, Jordan, the GCC.

**What I expect of Shopify** *(an expectation, not a finding)*. Cash on delivery is a manual payment method: the order stays pending until the merchant marks it paid. Couriers appear only through fulfillment and shipping apps, never as holders of money, and the core keeps no record of a courier's collection or settlement.

**What would settle it.** Shopify's help (cash on delivery, manual payment methods, marking an order paid) and developer documentation (financial status, transactions, fulfillment orders and fulfillment services). Salla's and Zid's help and developer documentation on cash on delivery through their shipping integrations: whether a courier's collection and settlement is recorded, and whether the cash passes through the platform.

### BT-3. Orders paid later, in parts, by several methods

**The question.** Can an order be placed before it is paid, and then be paid in parts, by different methods and at different times, with each payment confirmed later and matched to the order?

**Why it could sink Sharrwah, or cost dearly to change.** Sellers take payment in ways that finish after the order: in Yemen, a transfer before the goods go out, half on ordering and half on arrival, a receipt photo to activate the order, a wallet transfer matched afterwards, and cash on delivery. If the shape assumes payment completes inside checkout, these orders' money sits outside the platform's records, where it can't be reconciled, refunded or reported, and bringing it in later changes the order's payment record and its flow *(reading)*.

**Origin.**
- **Stands without the Yemen cases:** D16 sends money paid by transfer or in cash to the seller, outside any provider's checkout, and leaves cash on delivery with the courier until it settles (BT-2). *Assumption:* buyers pay by reference code at outlets and by instant transfer in Egypt; by transfer, postal account and cash on delivery in Morocco, Algeria and Tunisia; in cash in Lebanon; and by transfer for large or business orders in the GCC.
- **Rests on the Yemen cases:** the particular forms seen there. YA-131: a seller in Sana'a carries out an order only once the buyer has paid its price and shipping into her bank account (YE-E092, YE-E1006, 2025), and a store lists payment through Kuraimi, to a Hasseb point (YE-D400, YE-D401). YA-148: 50% of the order's value on ordering and 50% on arrival (YE-C615, 2022). YA-145: a store asks for a photo of the payment receipt to activate the order (YE-C597, 2022). YA-112: a community-written app confirms buyers' wallet transfers in a store automatically (YE-F104, YE-F105).

**Markets.** Yemen; *assumption:* Egypt, Morocco, Algeria, Tunisia, Lebanon, the GCC.

**What I expect of Shopify** *(an expectation, not a finding)*. Payment is taken in checkout by a payment app or a card, or the order waits as pending under a manual method until the merchant marks it paid. Payment in parts exists in some flows (deposits on draft orders, payment terms for business buyers), and a payment app can leave a payment pending and settle it later.

**What would settle it.** Shopify's developer documentation (financial statuses, transactions, payment sessions left pending, payment terms, recording a manual payment) and help (manual payment methods, deposits, payment in parts). WooCommerce's developer documentation (order statuses for payments still to come). Salla's and Zid's help (payment by bank transfer with a receipt; payment in parts).

### BT-4. Local providers' payments, run by the platform for each seller

**The question.** Can the platform itself run a local wallet's or bank's payment at checkout for each seller's own account with it (asking the buyer for a phone number, then a one-time code or PIN), keeping each seller's credentials apart, where the provider offers only an API?

**Why it could sink Sharrwah, or cost dearly to change.** Under C each seller has its own account with each provider, and Yemen's wallets and banks take online payments through APIs that the merchant's own system drives, with credentials issued to each merchant. If payments can run only as apps the providers build, Yemen gets local payments only if its providers build them, which I don't expect *(assumption)*; running them in the platform instead means holding each seller's credentials apart and answering each provider's calls per seller, which touches how stores are kept apart *(reading)*.

**Origin.**
- **Stands without the Yemen cases:** the question in its general form, a provider that offers an API but no app for the platform. It rests on D16 ("in the seller's own account with that provider"; and by default 1, an account a seller requests through Sharrwah stays C only while Sharrwah is party neither to the money nor to the provider's agreement for it), on D25 (regional fit, through strong support for local ecosystems and partners), and on the assumption that small local providers in the other markets won't build apps for a platform either.
- **Rests on the Yemen cases:** the particular flow in the question (a phone number, then a one-time code or PIN, and a provider that calls into the merchant's system), and the credentials each merchant holds. YK-131, as corrected: Cash offers its Cash Pay payment service to owners of online stores and apps (YE-C062). As community-written clients show them, not the providers' own documentation: Cash Pay texts the buyer a six-digit code, which the merchant's system sends back to confirm the payment (YA-112: YE-F020, YE-F021); Floosak's purchase starts from the buyer's phone number (YA-113: YE-F029); the merchant holds a username, a service-provider ID, an encrypted password and, for release, a certificate at Cash Pay, and a phone, short code, wallet ID and key at Floosak (YA-115: YE-F023, YE-F024, YE-F032); refunds go through Floosak's API (YA-116: YE-F036). A package page on yarnpkg, not the bank's own documentation, says Kuraimi's E-Pay calls a "Verify Customer details API" that the merchant hosts (YK-138: YE-D390, YE-D391).

**Markets.** Yemen; *assumption:* North Africa, Jordan, Lebanon, and the GCC's smaller providers.

**What I expect of Shopify** *(an expectation, not a finding)*. Payments other than Shopify's own run as payment apps that an approved provider builds and runs. The app holds the merchant's credentials and handles the buyer's steps, on its own page or in what checkout lets it add. Some older gateways took the merchant's credentials in Shopify's admin instead.

**What would settle it.** Shopify's developer documentation (the kinds of payment app allowed, and what checkout can ask the buyer for), its terms for payments partners, and its help (adding a provider). BigCommerce's and WooCommerce's developer documentation and help (gateways set up with the merchant's own credentials). Salla's and Zid's developer documentation (how the region's providers are added).

### BT-5. A currency its code doesn't tell apart

**From the Yemen cases alone: the founder may cut it.**

**The question.** Can money be recorded in a currency that its ISO code doesn't tell apart from another (Yemen's old and new rial), so that every price, payment and payout says which one it is?

**Why it could sink Sharrwah, or cost dearly to change.** Both rials go by one code, YER *(assumption)*, yet in 2026 a dollar buys about 531 to 534 of one and about 1,562 of the other, and the central bank in Sana'a calls the notes printed in Aden illegal currency. If money is an amount and a code, a price, refund or report can be off by a factor of about three, and changing the money type later touches every money record *(reading)*.

**Origin.** The Yemen cases:
- YA-01: the rial traded at 531 to 534 to the dollar in Houthi-controlled areas over the second quarter of 2026 (YE-E408), and on 16 September 2026 at 531 buying and 533 selling in Sana'a, against 1,562 and 1,571 in Aden (YE-D071).
- YA-03: the central bank in Sana'a publishes its own rates in a daily statement (YE-B028, March 2026), and the central bank fixed a new rate for Aden and the government's areas, under which the rial trades at about 1,558 to the dollar (YE-E668, YE-E669, February 2026).
- YA-15: the central bank in Sana'a calls the notes printed in Aden illegal currency, and their holding a serious harm (YE-B030, YE-B033, 2019); a statement on cby-ye.com, which Stage 1 places in the government's area, holds all notes of every denomination legal tender in all domestic transactions in the Republic (YE-C048, 2020).
- YK-452, as corrected: a community-written client for Kuraimi's E-Pay has the merchant set the currency zone it accepts: old, new or all (YE-E082, YE-F086).

My own knowledge adds only the premise that ISO 4217 has one code for the rial, YER, and, as a possible further market, Lebanon's dollars held in banks and in cash since 2019 *(assumptions)*; neither would carry the question alone.

**Markets.** Yemen.

**What I expect of Shopify** *(an expectation, not a finding)*. Money is an amount with an ISO 4217 code from a fixed list, and a store has one currency; nothing says which rial.

**What would settle it.** Shopify's developer documentation (its money and currency types; its list of currency codes) and admin (the store's currency). WooCommerce's developer documentation (whether a store can add a currency of its own). Which notes are legal tender where is each central bank's rule, and no platform's evidence settles it.

### BT-6. Priced in one currency, paid in another

**The question.** Can one order keep the currency it was priced in, the currency it was paid in and the rate used, and show on its invoice the amount in the currency the law requires?

**Why it could sink Sharrwah, or cost dearly to change.** In the internationally recognized government's area of Yemen, foreign currency is banned in domestic dealings and a registered seller's foreign-currency invoice must show the rial value, while in practice the Saudi riyal dominates in Aden and stores and wallets name dollars and riyals. An order that holds one currency, or a display currency converted from the store's, can't record what was actually paid, and its tax record would be wrong *(reading)*.

**Origin.**
- **Stands without the Yemen cases:** the question itself, on my own knowledge *(assumption)*: Lebanon (prices in lira and in dollars), stores selling across the GCC's currencies, and markets whose tax invoices must give local-currency amounts for sales made in a foreign currency, as I believe Saudi Arabia's VAT rules require.
- **Rests on the Yemen cases:** that one market has price, payment and invoice currencies apart at once, and the law on each. YA-21: the government banned foreign currency in commercial and service transactions and financial contracts (YE-E443, 2025; YE-E505, 2026), and the consumer law's regulation bars a supplier from obliging a consumer to buy in a non-local currency (YE-B171, 2010). YA-22: the Saudi riyal dominates dealings in Aden and the government's areas (YE-E1283, 2025). YA-149: a store states a coupon in dollars (YE-D171). YA-114: Cash Pay's API takes the rial, the dollar or the Saudi riyal, as a community-written client shows (YE-F022). YA-166: a registered seller issuing invoices in a foreign currency must show their value in rials and the prevailing rate (YE-F356, 2002).

**Markets.** Yemen; *assumption:* Lebanon, the GCC, Saudi Arabia.

**What I expect of Shopify** *(an expectation, not a finding)*. An order holds each amount in the store's currency and in the currency shown to the buyer, and is paid in the latter; the rate is Shopify's or a manual one set for a market. A payment in a third currency, or a rate kept for the invoice, has no place.

**What would settle it.** Shopify's developer documentation (an order's amounts in shop and presentment money; markets' currency settings) and help (selling in several currencies; manual rates). BigCommerce's developer documentation (whether an order keeps the rate used). Salla's and Zid's help (prices in several currencies; invoices in riyals). Which currency a sale must be paid in, and what its invoice must show, is each market's law.

### BT-7. Sharrwah's own fees, from sellers without cards

**The question.** Can Sharrwah bill its own fees to a seller who has no card (paid by wallet, transfer or cash in the market's currency, and left unpaid until the payment is confirmed) without taking them from sellers' money or from a balance sellers pay into?

**Why it could sink Sharrwah, or cost dearly to change.** At launch Sharrwah's fees are billed apart, never taken from sellers' money at a provider, and no balance sellers pay into may hold them; in Yemen few sellers can be charged on a card *(reading)*, so most bills would wait for a payment the seller pushes. A billing shape that only charges a card on file would leave most Yemeni sellers unable to pay Sharrwah at all *(reading)*.

**Origin.**
- The founder's decisions: D16 (default 2, fees billed apart; default 3, no balance that sellers pay into), D20 (default 2 holds while a market runs only C), D26 (prices, the company and its licences are the founder's).
- The Yemen cases. YA-62, as `corrections.md` corrects it: Stripe doesn't support a business in Yemen, which isn't among its supported countries or regions; its quotes here (YE-E586, YE-E587) are the page's headings, so this rests on the check `corrections.md` links. YA-120: about 400,000 active debit cards at the end of 2019 (YE-E163, a source of 2022). YK-514, a caution in `corrections.md`: an undated article of a store platform lists Yemen as able only to send money through PayPal, not receive it, and PayPal's own country list would settle it (YE-D997). YA-107: a lack of reliable online payment gateways (YE-D187, 2025).
- *Assumption:* in Algeria and Tunisia the currency isn't freely convertible, so paying a foreign company is restricted; Egypt has at times limited card spending in foreign currency; Lebanon's banks have restricted payments since 2019.

**Markets.** Yemen; *assumption:* Algeria, Tunisia, Egypt, Lebanon.

**What I expect of Shopify** *(an expectation, not a finding)*. Shopify charges its bills to a card or PayPal on file, or in some countries a bank account, in a set of billing currencies, and freezes a store whose bill goes unpaid; stores on Shopify Payments have its fees taken from payouts.

**What would settle it.** Shopify's help (paying bills: the methods and currencies accepted) and terms (fees; non-payment). Salla's and Zid's help (how they bill merchants). Whether a seller may pay a foreign company, and in which currency, is each market's law.

### BT-8. A market smaller than a country

**From the Yemen cases alone: the founder may cut it.**

**The question.** Can a market be an area within a country, so that the rules, currency, payment methods and delivery that apply can differ between one part of a country and another?

**Why it could sink Sharrwah, or cost dearly to change.** In Yemen two central banks each rule banks, payment providers from Sana'a may work in Aden only with infrastructure in the South, both sides took measures against banks and then agreed to reverse them, and the two areas use different notes and rates. If a market is a country, a store in Sana'a and one in Aden get one set of rules, currency and payment methods, and since who holds sellers' money is a market's setting (E1, D19), splitting a country later touches settings, payments, taxes and delivery everywhere *(reading)*.

**Origin.** The Yemen cases:
- YA-44: the central bank in Sana'a holds banking without its licence a breach of the law (YE-A088, 31 May 2024, a page the founder saved inside Yemen), and the central bank in Aden regulates and supervises private banks and money exchangers (YE-D435, 2024; its source gives no area, as `corrections.md` notes).
- YK-124, as corrected: payment providers from Sana'a may operate in Aden only by investing in separate infrastructure in the South (YE-D521, 2024).
- YA-25: the two sides agreed to reverse recent measures related to banks, among them Aden's revocation of six Sana'a-based entities' licences (YE-E467, a source of October 2024). YA-26: Aden's June 2024 ban on dealing with twelve wallets and other banks in Sana'a was later reversed (YE-D107, 2025).
- YA-177: the Houthi authorities treat their areas as if an independent state, and impose additional customs fees on goods from the government's areas (YE-D606, YE-D607, 2025).
- YA-224: each party runs the telecoms in its area as a monopoly (YE-E135, 2025).
- The rates and notes of BT-5.

D19 makes the question weigh more but doesn't raise it. My own knowledge suggests other places where parts of one country have their own authorities (Libya, the Kurdistan Region of Iraq, the Palestinian territories), if they are among the founder's "others" (D25) *(assumption)*; that alone wouldn't carry the question.

**Markets.** Yemen.

**What I expect of Shopify** *(an expectation, not a finding)*. Markets are made of countries; provinces count for taxes and shipping zones, not for which currency, payment methods or rules apply. A store has one country, and its payment methods are set for the store, with rules at checkout able to hide some.

**What would settle it.** Shopify's developer documentation (what a market can be made of; payment customizations) and help (markets; which providers are available in which country). Which rules apply in each area is Yemen's law, as each authority sets it, and no platform's evidence settles it.

### BT-9. Sanctions, area by area

**From the Yemen cases alone: the founder may cut it.**

**The question.** Can the platform comply with sanctions area by area (screening the parties, and choosing which providers and infrastructure serve each area) so that a designation covering one area doesn't cut the whole market, or the platform, off from its providers?

**Why it could sink Sharrwah, or cost dearly to change.** The United States designates Ansarallah (the Houthis), who control part of Yemen, a Specially Designated Global Terrorist and a Foreign Terrorist Organization, the EU lists them under its Yemen measures, and foreign financial institutions apply stricter checks or stop Yemen-related transactions altogether. A platform that is one undivided stack on providers who refuse whole countries could be shut out of its first market or put at risk everywhere, and separating providers and data by area later touches infrastructure and identity throughout *(reading)*.

**Origin.** The Yemen cases:
- YA-27: the Houthis control part of Yemen ("Houthi-controlled areas", YE-E408). The US designation of Ansarallah (the Houthis) as a Specially Designated Global Terrorist took effect on 16 February 2024 (YE-D840), and it was re-designated a Foreign Terrorist Organization on 4 March 2025 (YE-D798). The EU added the Houthis (Ansarallah) to the list under its Yemen restrictive measures in March 2022, with some of the measure's articles not applying to them (YE-D716, YE-D717, YE-D718).
- YA-31: many financial institutions impose stricter due diligence or cease Yemen-related transactions altogether (YE-E956, 2026).
- Not used: YK-24, whose two quotes, two lines apart in one article, don't by themselves say that sanctions limit e-commerce.

My own knowledge adds only that providers in other markets may apply US or EU sanctions *(assumption)*, which wouldn't carry the question alone.

**Markets.** Yemen.

**What I expect of Shopify** *(an expectation, not a finding)*. Shopify serves a country or doesn't, under its terms, on one global infrastructure; it doesn't serve part of a country apart from the rest.

**What would settle it.** The law: US, EU and UN sanctions, and the authorities' guidance on them, decide what may be done, and no platform's evidence settles it. Shopify's terms and help show only where Shopify draws its own line.

### BT-10. Where a store's data lives

**The question.** Can one market's stores, or one store, keep their data in the country that market's law requires, while the platform stays one platform?

**Why it could sink Sharrwah, or cost dearly to change.** Yemen's sales tax law, as I read its held text, requires a registered seller who keeps its books on computers to keep those systems in Yemen for the tax authority *(reading)*, and other markets restrict sending data abroad *(assumption)*. A platform that keeps every tenant's data in one place can't meet such a rule without being split, among the most expensive changes a platform can make *(reading)*.

**Origin.**
- The Yemen cases, as a reading. YK-290: Stage 1's record says a sales-tax registered seller must keep regular books, with its computer systems kept in Yemen. Its quote (YE-B303), from the General Sales Tax Law as amended by Law 42 of 2005 (YE-B296), is an extraction with doubled letters. Read through them, it says that where a registered person uses computer systems in place of books, the systems and books must be in Yemen for the authority to inspect *(reading)*. Whether that binds a platform that keeps a seller's records is the law's question.
- *Assumption:* Algeria's e-commerce law requires e-commerce sites to be hosted in Algeria, and Saudi Arabia, Egypt, the UAE and others limit sending personal data abroad.

**Markets.** Yemen *(reading)*; *assumption:* Algeria, Saudi Arabia, Egypt, and others whose data-protection laws limit transfers abroad.

**What I expect of Shopify** *(an expectation, not a finding)*. All stores' data lives in Shopify's own infrastructure, where Shopify chooses, with no choice of country for a store or a market.

**What would settle it.** Shopify's terms, including its privacy policy, and its help (where store data is held; any choice of region). Salla's and Zid's terms and privacy policies (where they hold data). WooCommerce, which the merchant hosts, so the merchant chooses: the opposite shape. What must stay in a country is each market's law, and no platform's evidence settles it.

### BT-11. Tax invoices as records of their own

**The question.** Can a seller's tax invoice be a record of its own (numbered in the seller's sequence, fixed once issued, corrected only by credit or debit notes, and sent to the tax authority where the law requires) rather than a printout of the order?

**Why it could sink Sharrwah, or cost dearly to change.** Yemen requires a registered seller to issue a numbered invoice for each sale, and Saudi Arabia, Egypt, Jordan and others require e-invoices from compliant systems, cleared or reported to the tax authority *(assumption)*. If invoices are printed from orders that can still be edited, the money record the authority sees can change after the fact, and moving to fixed records tied to the authority later touches orders, refunds and taxes *(reading)*.

**Origin.**
- My own knowledge *(assumption)*: Saudi Arabia's e-invoicing (ZATCA) requires each invoice to carry a QR code and a cryptographic stamp, to be chained to the one before, and to be cleared (sales to businesses) or reported (sales to consumers); Egypt (e-invoices and e-receipts) and Jordan (JoFotara) run national systems, and the UAE is introducing one.
- The Yemen cases: a registered seller's invoices are issued in an original and at least one copy, the original to the buyer and the copy kept (YA-165: YE-F351), and show a printed serial number and date, and the names, addresses and tax numbers of seller and buyer (YE-F352), under a decision of 2002. Invoices made by computer must carry all the data an invoice needs (YK-288: YE-F357), in Arabic or translated into Arabic (YK-287: YE-F373).

**Markets.** Yemen; *assumption:* Saudi Arabia, Egypt, Jordan, the UAE, Oman, Tunisia, Morocco.

**What I expect of Shopify** *(an expectation, not a finding)*. No tax invoice in the core: orders are numbered per store and can be edited after they are placed, refunds are recorded on the order, and invoices come from apps or templates.

**What would settle it.** Shopify's developer documentation (orders, order editing, refunds) and help (invoices; taxes). Salla's and Zid's help and developer documentation (e-invoicing under Saudi law, which I assume they hold). What an invoice must be is each market's tax law.

### BT-12. Who the seller legally is

**The question.** Does the platform keep its own record of who each seller legally is (a person or a company, its registration and tax numbers in each market, and whether these were checked) apart from any payment provider's checks?

**Why it could sink Sharrwah, or cost dearly to change.** Yemeni law requires a trader to show its register number and trade name, and a seller to identify itself on its documents to consumers, electronic ones included, while under C only the providers check sellers, each for its own account. Without a record of its own, the platform can't show what the law requires or know whom it serves, and adding one later means identifying every store again *(reading)*.

**Origin.**
- The founder's decisions: D16 (each provider holds the money in the seller's own account).
- The Yemen cases: a trader must state its commercial register number and trade name in its business correspondence and on its shopfront (YA-152: YE-F289, 2019); a supplier must put the data that identify it on all the correspondence and documents it issues to consumers, electronic ones included (YK-469: YE-B156, 2010); a merchant account at Floosak needs a commercial register or a work licence (YA-111: YE-C253).
- *Assumption:* Saudi Arabia requires online stores to show a commercial registration or freelance document and a VAT number, and Algeria requires e-commerce sellers to register.

**Markets.** All: Yemen from the cases, the others by assumption.

**What I expect of Shopify** *(an expectation, not a finding)*. A store has a business name and address, and in some countries tax numbers, in its settings. Who the seller is gets checked by Shopify Payments' provider, for payouts. The account owner is a person, and there is no separate, checked record of the seller's legal entity per market.

**What would settle it.** Shopify's developer documentation (the shop's fields), help (store details; verification for Shopify Payments) and terms (who the merchant is). Salla's and Zid's help and terms (what they require of sellers, and check). What a seller must show and have checked is each market's law.

### BT-13. Buyers known by phone

**The question.** Can a buyer be identified by a phone number alone, confirmed by a one-time code, with the choice left open between an identity per store and one across stores?

**Why it could sink Sharrwah, or cost dearly to change.** In Yemen a buyer's payment identity is a phone number and stores take orders by WhatsApp, and a buyer app, one of the services the founder may run, needs an identity across stores. An identity keyed to email would shut out phone-only buyers or need a second key later, and a per-store identity can't become a platform-wide one without merging records *(reading)*.

**Origin.**
- The founder's decisions: D26 (a buyer app among the services; the platform keeps room for each).
- The Yemen cases: Floosak opens a wallet on an active mobile number (YA-79: YE-C251); Floosak's purchase starts from the buyer's phone number, as a community-written client shows (YA-113: YE-F029); a store takes orders by WhatsApp and confirms them with the buyer's name, address and phone number (YA-145: YE-C592, YE-C594, 2022).
- *Assumption:* across the region buyers reach sellers by phone and WhatsApp more than by email.

**Markets.** Yemen; *assumption:* all the others.

**What I expect of Shopify** *(an expectation, not a finding)*. Customers belong to a store. A customer account is signed in to by email, with a code; checkout can take a phone number without an email; the Shop app is a separate identity across stores.

**What would settle it.** Shopify's developer documentation (customers; customer accounts) and help (customer accounts; contact details at checkout). Salla's and Zid's help and developer documentation (signing buyers in by phone).

### BT-14. A basket across stores

**The question.** Can one basket, and the order it makes, take goods from several stores, with each store's share paid into that store's own provider account?

**Why it could sink Sharrwah, or cost dearly to change.** The founder lists a marketplace and a buyer app among the services Sharrwah's company may run, and the platform keeps room for each. If an order belongs to exactly one store, a basket across stores later changes orders and payments, and under C each store's share must reach its own provider account, which one payment to one party wouldn't do *(reading)*.

**Origin.**
- The founder's decisions: D26 ("Sharrwah rules out nothing the class shows; the platform keeps room for each of these, whoever provides it"), D16 (each provider holds the money in the seller's own account).
- The Yemen cases: a delivery app added ordering from several stores in one basket (YA-135: YE-C516, its store listing, 2026).

**Markets.** All (D26).

**What I expect of Shopify** *(an expectation, not a finding)*. A cart and an order belong to one store; the Shop app gathers stores for buyers but checks out store by store.

**What would settle it.** Shopify's developer documentation (carts and orders, and the store each belongs to) and help (the Shop app). Salla's and Zid's help (any marketplace or buyer app across stores).

## Merged, split or dropped

None of the 14 drafts was merged, split or dropped: written out, each still names a place where Shopify's shape alone could make Sharrwah fail in a market or force an expensive change. Two Yemen records in the drafts are left out, because their quotes don't settle them and phase 1 opens no captured source: YK-206 (under BT-2) and YK-24 (under BT-9). Neither question rests on them.

## What was left out

- **A feature that can be added later without changing the core.** Example: free delivery, by coupon or above a set order value, which Yemeni apps offer (YA-137: YE-C701, YE-E038). It is a discount on an order's delivery; adding it later changes no record of money, identity or data, and no flow *(reading)*.
- **An answer that only fills a value, a provider or a partner into a place Shopify's shape already has.** Example: the general sales tax rate, 5 percent in Yemen (YA-160: YE-D012, YE-E982, 2005), fills a rate into the tax-rate place I expect Shopify's shape to have *(expectation)*. BT-11 isn't of this kind: it asks whether the place itself fits.

## Which of the other four platforms each question needs

All of this is expectation, for phase 2 to test. I expect Salla and Zid to be needed most: the founder's intent names them as the class in the region (D26), and they are the two of the four built for its law and payment ecosystem, so a regional practice that Shopify's shape lacks would show there first. I expect them to be needed for BT-1 (whether either holds sellers' money or opens accounts through itself, and whether its payment record changes with the holder), BT-2 (whether their shipping integrations record a courier's cash and its settlement, and whether that cash passes through the platform), BT-3 (bank transfers confirmed after the order), BT-4 (how the region's providers are added), BT-6 (prices in several currencies, invoices in riyals), BT-7 (how they bill merchants), BT-10 (where they keep data), BT-11 (Saudi e-invoicing), BT-12 (what they require and check of sellers), BT-13 (signing buyers in by phone) and BT-14 (any basket or buyer app across stores). WooCommerce is the opposite shape, software the merchant hosts: its payment plugins run in the merchant's own site with the merchant's own credentials, its data lives wherever the merchant puts it, and its list of currencies can, I expect, be extended, so I expect it to be needed for BT-4, BT-5 and BT-10, and perhaps for BT-3, for its order statuses for payments still to come. BigCommerce is the closest of the four to Shopify's shape, and I expect it to add something only where I expect it to differ: gateways set up with the merchant's own credentials in its control panel (BT-4), and an exchange rate kept on each order (BT-6). BT-8 and BT-9 I expect to need none of the four: I expect none of the five platforms to divide a country in its core or to serve part of one apart, so Shopify's evidence and the law decide them; and for BT-7, BT-9, BT-10 and BT-11 the markets' law, not any platform, has the last word on what Sharrwah must do.

## Sources

**The founder's decisions,** `founder-decisions.tsv` at commit `8e1f5c7a5df7a091a8e10f33fe52bbf322c042de`: [D8](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/8e1f5c7a5df7a091a8e10f33fe52bbf322c042de/founder-decisions.tsv?plain=1#L8) (the guard on money), [D16](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/8e1f5c7a5df7a091a8e10f33fe52bbf322c042de/founder-decisions.tsv?plain=1#L16) (Decision 1 and its defaults), [D19](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/8e1f5c7a5df7a091a8e10f33fe52bbf322c042de/founder-decisions.tsv?plain=1#L19) (E1 and E2), [D20](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/8e1f5c7a5df7a091a8e10f33fe52bbf322c042de/founder-decisions.tsv?plain=1#L20) (default 2 at launch), [D25](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/8e1f5c7a5df7a091a8e10f33fe52bbf322c042de/founder-decisions.tsv?plain=1#L25) (the markets), [D26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/8e1f5c7a5df7a091a8e10f33fe52bbf322c042de/founder-decisions.tsv?plain=1#L26) (the intent). They say what Sharrwah needs, never what a platform does.

**Stage 1's records,** at the same commit: `studies/yemen-cases/axes.tsv` (YA-), `constants.tsv` (YK-), `citations.tsv` (YE-) and `corrections.md`.

**The quotes' sources,** all at commit `9d0de523f1852ebf7716f0da01b6b619edc5e8fc`, under `evidence/yemen/`, none of them opened here. In the paths, `FP/` is `blocked-evidence-founder/`; `RU/` is `runs/20261010T061420Z-sanaa-rules-search/items/`; `OP/` is `runs/20261010T072550Z-sanaa-operators-search/items/`; `CS/` is `runs/20261010T050304Z-cited-sources/items/`; `CC/` is `runs/20261010T051708Z-community-clients/`; `DR/` is `derived/20261010T061420Z-sanaa-rules-search/`.

- `FP/ميليشيا الحوثي تحظر التعامل مع بنوك في مناطق الحكومة ردًا على قرارات البنك المركزي في عدن - المصدر أو….html`: YE-A088, line 19
- `RU/020-yemeneco.org/text.txt`: YE-B028, line 59
- `RU/024-althawrah.ye/text.txt`: YE-B030, line 14; YE-B033, line 27
- `RU/044-moit.gov.ye/text.txt`: YE-B156, lines 93-94; YE-B171, lines 266-267
- `RU/066-tax.gov.ye/text.txt`: YE-B296, lines 77-78; YE-B303, lines 252-254
- `OP/003-cby-ye.com/text.txt`: YE-C048, line 25
- `OP/006-cash.com.ye/text.txt`: YE-C062, line 17
- `OP/023-qc-yemen.com/raw.html`: YE-C251, line 1372; YE-C253, line 1372
- `OP/081-play.google.com/text.txt`: YE-C516, line 166
- `OP/087-procorners.com/text.txt`: YE-C592, line 42; YE-C594, line 44; YE-C597, line 110; YE-C615, line 140
- `OP/097-apps.apple.com/text.txt`: YE-C701, line 118
- `CS/004-yemen-nic.info/text.txt`: YE-D012, line 80
- `CS/016-almahriah.net/text.txt`: YE-D071, line 103
- `CS/023-almushahid.net/text.txt`: YE-D107, line 87
- `CS/041-bab-almandab.com/text.txt`: YE-D171, line 234
- `CS/044-blog-it.nano2soft.com/text.txt`: YE-D181, line 100; YE-D187, line 105
- `CS/067-classic.yarnpkg.com/text.txt`: YE-D390, line 27; YE-D391, line 31
- `CS/070-da5m.com/text.txt`: YE-D400, line 24; YE-D401, line 25
- `CS/073-documents1.worldbank.org/text.txt`: YE-D435, line 901; YE-D521, line 6682
- `CS/076-economicmedia.net/text.txt`: YE-D606, line 604; YE-D607, line 867
- `CS/086-eur-lex.europa.eu/text.txt`: YE-D716, line 365; YE-D717, line 373; YE-D718, line 387
- `CS/093-gcaptain.com/text.txt`: YE-D798, line 50
- `CS/115-home.treasury.gov/text.txt`: YE-D840, line 35
- `CS/129-matjari.online/text.txt`: YE-D997, line 98
- `CS/141-play.google.com/text.txt`: YE-E038, line 41
- `CS/149-root.packagist.org/text.txt`: YE-E082, line 109
- `CS/152-sahafahonline.net/text.txt`: YE-E092, line 46; YE-E1006, line 52
- `CS/153-sanaacenter.org/text.txt`: YE-E113, lines 229-233; YE-E114, lines 233-236; YE-E135, lines 482-485
- `CS/154-sanaacenter.org/text.txt`: YE-E163, lines 308-312
- `CS/160-sanaacenter.org/text.txt`: YE-E408, line 177
- `CS/162-sanaacenter.org/text.txt`: YE-E443, line 74
- `CS/163-sanaacenter.org/text.txt`: YE-E467, line 52
- `CS/164-sanaacenter.org/text.txt`: YE-E505, line 53
- `CS/175-stripe.com/text.txt`: YE-E586, line 225; YE-E587, line 285
- `CS/180-torodexpress.com/text.txt`: YE-E612, line 89
- `CS/183-ukrpublisher.com/text.txt`: YE-E622, line 355; YE-E623, line 126
- `CS/197-alaraby.co.uk/text.txt`: YE-E668, line 47; YE-E669, line 49
- `CS/249-theigc.org/text.txt`: YE-E956, lines 1705-1707
- `CS/256-wto.org/text.txt`: YE-E982, lines 156-157
- `CS/270-yemen-press.net/text.txt`: YE-E1283, line 55
- `CC/Alsharie__cash-payment/README.md`: YE-F021, 2. Confirm purchase (lines 59-64); YE-F024, lines 30-31
- `CC/Alsharie__cash-payment/config/cashPay.php`: YE-F023, lines 4-12
- `CC/Alsharie__cash-payment/src/CashPayAttributes.php`: YE-F020, lines 127-128; YE-F022, lines 89-92
- `CC/Alsharie__floosak-payment/README.md`: YE-F029, 1. Purchase (lines 75-81); YE-F036, Refund (lines 112-117)
- `CC/Alsharie__floosak-payment/config/floosak.php`: YE-F032, lines 4-9
- `CC/al-saloul__kurimibanck/README.md`: YE-F086, Usage (line 39)
- `CC/thejulan__yemenpay/README.md`: YE-F104, Features (line 12)
- `CC/thejulan__yemenpay/app/lib/screens/onboarding_screen.dart`: YE-F105, line 20
- `DR/042-moit.gov.ye/ocr.txt`: YE-F289, lines 688-690
- `DR/069-tax.gov.ye/ocr.txt`: YE-F351, lines 20-22; YE-F352, lines 25-28; YE-F356, lines 58-59; YE-F357, lines 89-91
- `DR/071-tax.gov.ye/ocr.txt`: YE-F373, line 122

*Phase 1 stops here.*
