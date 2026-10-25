---
id: D-001
title: Who holds sellers' money at launch
subject: S-01
status: proposed
door: one-way
integrity: 3
outcome: Built
varies_by: —
risks: W-07 R-07 R-08
evidence: S01-V-001 S01-V-003 S01-V-006 S01-V-008 S01-V-011 S01-V-015 S01-V-016 S01-V-023 S01-V-026 S01-V-027 S01-V-038 S01-V-532 S01-V-656 YA-62 YK-514 YK-161 YA-107 YK-131 YE-E765 YA-102 YK-515 YA-103 YA-106 YK-124 YK-203 YA-131
depends_on: —
trigger: —
date: 2026-10-24
---

# Who holds sellers' money at launch

This is the pilot's Decision 1 (`studies/subjects/S-01/entry.md`, S01-VP-01). The founder answers it.

## For the founder

**The question.** Between a buyer's payment and the seller's payout, who holds the money?

**Your line to confirm:** "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours."

**What it means.** At launch the money stays where each way to pay puts it: with a wallet or other provider, in the seller's own account; with a courier the seller contracts with, collecting cash on delivery, until it settles with the seller; or with the seller, paid by bank transfer or in cash to its own staff. This is the pilot's option C. Sharrwah holds none of it. The line is about sellers' money only. Buyers' money, such as a wallet buyers pay into, is outside it and would come to you on its own.

**Why:**
- your guard of 18 October already keeps A and B from going live without you;
- *on my reading* of the first market's rules, A would need a licence or permission for payment services in each area, or perhaps a licensed partner to hold the money instead. No source read shows which, and the central banks' own definitions are unread (YA-102; Gaps);
- B needs a processor that holds funds in accounts opened through a platform. None is shown for the first market yet: Stripe doesn't serve businesses based there, PayPal's limit there rests on one undated article, and whether a local provider would do it is unknown. The pilot called this need "unsettled, not unmet";
- C is shown working there, as of October 2026: a wallet paying into the seller's own account, a courier collecting on delivery, and transfers into the seller's own account. These show where the money lands. Whether the first market's wallets let a seller link its own account to Sharrwah, or open accounts only through a platform, is asked when S-07 proposes them (Gaps).

**The line's words,** as the glossary defines them from your guard, the pilot's entry, and Shopify's and Salla's own help and structures (`architecture/12-glossary.md`):
- **Sellers' money:** what a buyer pays for a seller's order, until it reaches an account the seller holds under its own agreement, or the seller's own hands. Not Sharrwah's own fees, and not store credit, which is value a seller owes rather than money paid in.
- **Held through Sharrwah:** your guard covers "No arrangement that holds sellers' money through Sharrwah", and names two forms:
  - A, Sharrwah holds it, as Salla presents the balance of its electronic payments;
  - B, "a payment company holds it in an account opened through Sharrwah", the way Shopify Payments is set up inside Shopify.

  C is neither: the seller's own account with a provider, under its own agreement, linked by its own keys, account email or the provider's own app. *My reading, for you to confirm or correct:* the guard also covers arrangements it doesn't name, such as a courier collecting cash under Sharrwah's own contract with it.
- **At launch:** from the day Sharrwah first goes live in any market, and in each market until you switch A or B on there.
- **Reserved, not built:** nothing of A or B is designed, built, integrated or contracted. The payment boundary, as proposed (D-002), leaves room for either. Because your line says "not built", building one is your decision too, not only switching it on, in a record of its own.

**Three choices on the line's extent,** each with my recommendation. In choice 1 your guard's words reach further than its source, so both readings go to you. Choices 2 and 3 are left open by C itself: Sharrwah would hold no sellers' money either way, as the glossary defines it. Each recommendation is for launch. The other way stays reserved, like A and B, and switching it on would be yours.
1. **Where B ends.** Some accounts are set up through a platform, but the money is held under an agreement between the seller and the provider:
   - in Saudi Arabia, a store can ask through Salla for a Tabby or Tamara business account, and Salla passes the store's details on. That article says "Fees depend on the agreement between the merchant and Tabby". Salla's article for the UAE, where stores set their Tabby account up directly, says "Your settlement terms and merchant fees follow your agreement with Tabby". Neither says whose agreement covers an account asked for through Salla;
   - Shopify sets PayPal up with the store's email, paying into the seller's existing PayPal account, or one the seller signs up for. Its help names no agreement.

   By your guard's words these are "opened through Sharrwah", so B. Its source, the pilot's option B, is "A payment processor holds, in an account the merchant opens through Sharrwah", "as Stripe, Adyen, Global-e and PayPal hold for Shopify, WooCommerce and BigCommerce". *My reading:* that is, inside the platform's own payment product, though BigCommerce's runs through the seller's linked PayPal account. The same entry counted an account "opened through Sharrwah" as B or C. **I recommend reading B by its source:** such an account is C when the money is held under the seller's own agreement. One where Sharrwah would be party to the money, or to the provider's agreement for it, stays B and comes to you.
2. **Sharrwah's fees, and anything owed to Sharrwah or its partners,** such as a loan's repayments. Shopify does both, by who holds the money (glossary, *Sharrwah's fees*). From its own Shopify Payments it deducts its card fees, and, for US loans accepted since 9 March 2026, Shopify Capital's repayments. Where another provider holds the money, it bills apart: transaction fees on its bill, and Capital's repayments debited from a bank account. **I recommend billing apart at launch:** it needs nothing from the sellers' providers. Taking them from sellers' money at a provider stays reserved. *On my reading,* it would need that provider's support and an agreement Sharrwah is party to, which choice 1 places on B's side.
3. **A balance sellers pay into.** Salla's wallet lets sellers "Add funds", and its store balance pays for Salla's services, such as "Auto-renewing your subscription plan". Shopify takes its bills by card or PayPal, among others, or from a seller's Shopify Balance account by its card. Such a balance would hold the seller's own funds through Sharrwah, like A, though not sellers' money as defined above, and your guard's source was about sales money. **I recommend none at launch:** Sharrwah bills its fees by invoice or charges the seller's card, through a provider for its own billing. Such a balance stays reserved with A.

**What confirming it settles,** with these choices as recommended. At launch, and until you decide otherwise in a record of its own, Sharrwah has none of the following, and each would hold money through Sharrwah:
- a Sharrwah payment service or balance, like Salla's electronic payments, or a balance sellers pay into;
- Sharrwah shipping that collects cash under Sharrwah's own contract, like Salla's own shipping labels;
- a Sharrwah business account that receives sellers' payouts, like Shopify Balance;
- a marketplace Sharrwah runs that collects buyers' payments for sellers;
- Sharrwah, or a partner of its, holding money as merchant of record, as Global-e does on some Shopify orders.

If you want any of these at launch, say so instead of confirming.

**D-004 comes with it.** Because of this line, the pilot's Decisions 2 to 12 follow column C (D-004): each provider or courier settles, pays out and charges its own fees on its own terms; Sharrwah sends no payouts, is no seller's agent for receiving payments, and takes no security interest in sellers' money; and its terms say each provider's terms govern the money that provider holds. D-004 is a record of its own, and your answer accepts it with this one unless you say otherwise. Decision 13, installments, is deferred (D-005), and Decision 14, currency, moves to S-04, markets and currency.

**What it leaves to later subjects,** none of which can undo it:
- which providers and methods are offered, with any case between B and C coming to you, and what sellers are shown of their providers' balances and payouts (S-07);
- installments, deferred (D-005), and currencies (S-04);
- shipping with cash on delivery (S-05);
- gift cards, store credit and customer wallets (S-05). A wallet buyers pay money into would hold buyers' money: this line doesn't cover it, and it would come to you on its own;
- money products for sellers, such as loans, cash advances and cards (S-02 orders them). A business account that receives payouts through Sharrwah stays off;
- selling in person and on outside marketplaces, where an account opened through Sharrwah comes to you (S-10);
- Sharrwah's prices and plans (S-03);
- the company, and each market's licensing rules, including whether a platform that only links sellers' own providers needs a licence there. That could change where, and by which company, Sharrwah runs, not who holds the money (S-08).

**Door and risk.** Under the method, decisions on money are one-way doors, so this one comes to you. Its risk, in my assessment, is low, because it keeps the arrangement that holds nothing and keeps the way to the others open:
- turning on A later needs a licence or permission, or perhaps a licensed partner, and a ledger of balances, payouts and reconciliation built behind the boundary;
- B needs a processor that holds funds in accounts opened through Sharrwah;
- both need your decision, and neither needs to change the order side if the payment boundary holds, which is still being proven (D-002).

**Answer:** confirm, with choices 1 to 3 as recommended / confirm, with these changes: … / change the line / defer (only the boundary is built, and your guard keeps holding)

## Context and problem statement

**The pilot's question** (phase C): "Between the buyer's payment and the payout, who should hold a merchant's funds in Sharrwah: a balance Sharrwah keeps for the merchant, the payment processor's accounts, or the provider of each payment method?"

**At G1, on 18 October,** the founder deferred all 14 of the pilot's decisions and set a guard: "No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision: whether Sharrwah itself holds it (the entry's option A) or a payment company holds it in an account opened through Sharrwah (option B)" (`founder-decisions.tsv`). That guard already decides what can go live. This record makes it the design's starting point.

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| sellers' money | What a buyer pays for a seller's order, until it reaches an account the seller holds under its own agreement, or the seller's own hands. Money paid out into an account held through Sharrwah is still sellers' money. Not Sharrwah's fees, stored value, or money products such as loans | `founder-decisions.tsv` (G1); `HC:payments/shopify-payments/payouts/view-details.md:3`; `SA-en:1240` |
| held through Sharrwah | Any arrangement that holds sellers' money through Sharrwah. A: Sharrwah holds it. B: a payment company holds it in an account opened through Sharrwah: Sharrwah's own service, or an account where Sharrwah would be party to the money or to the provider's agreement for it (choice 1, the source's reading). A case between B and C comes to the founder | `founder-decisions.tsv` (G1); `studies/subjects/S-01/entry.md`:119, :238; `HC:payments/shopify-payments/onboarding.md:3`; `SA-en:807`; `SA-ar:865` |
| seller's own account | An account the seller holds with a provider or courier under its own agreement, into which it receives or settles the buyer's payment, linked by the seller's own credentials, keys, account number or email, or the provider's own app. It stays the seller's own when asked for through Sharrwah, unless Sharrwah is party to the money or the agreement (choice 1). A payout-only bank account is not C | `HC:payments/third-party-providers/configuring-providers.md:32`; `SA-en:318`; `SA-en:793`; `SA-en:277`; `SA-en:1181`; `SA-ar:865` |
| at launch | From first going live in any market, for as long as the founder hasn't switched A or B on there | This record's line |
| reserved, not built | Nothing of A or B is designed, built, integrated or contracted. Building either, and switching it on in a market, is the founder's decision in a record of its own, which this record provides for | This record; D-002 |
| payment method | Kinds 1 and 2 of the glossary: paid through a provider, or paid outside any provider, to the seller or its courier, and recorded by hand. Stored value is outside this record | `HC:payments.md:3`; `SA-en:807`; `SA-en:921` |
| payment provider | The company that processes or receives a payment for a method, a platform's own service included. A courier is named apart | `HC:payments/getting-paid.md:3`; `SA-en:24` |
| manual payment method | The buyer pays outside any provider, to the seller directly or, for cash on delivery, to a courier that settles with the seller. The seller records it, or the courier reports it where the courier is integrated | `HC:payments/manual-payments.md:5`; `SA-en:565` |
| cash on delivery | Cash to a courier or to the seller's own staff. A courier under the seller's own contract holds it until it settles with the seller (C). Cash a courier collects under Sharrwah's own contract is held through Sharrwah | `SA-en:565`; `SA-en:234`; `SA-ar:359`; `SA-en:570`; S01-V-038 |
| platform balance | A balance a platform keeps for a seller: from its own payment service, or from cash on delivery its own labels collect, which hold sellers' money through Sharrwah; or from money sellers pay in, the seller's own funds, held like A (choice 3) | `GQL:3193`; `SA-en:1240`; `SA-en:570` |
| settlement and payout | Each provider's own, on its own terms | `GQL:3229`; `SA-en:807` |
| Sharrwah's fees | With anything owed to Sharrwah or its partners: billed apart at launch, not taken from sellers' money by a provider (choice 2). Taking them at a provider stays reserved | `HC:payments/getting-paid.md:11` and `HC:your-account/manage-billing/billing-charges/types-of-charges.md:12` (precedents); `HC:finance/shopify-capital/united-states.md:131`, `:179` |

## Scope

**Decides:**
- From the first time Sharrwah goes live, in every market, no sellers' money is held through Sharrwah: neither A nor B is built (C at launch).
- The money for each sale stays where its payment method's arrangement puts it: with a provider, in the seller's own account; with a courier under the seller's own contract, until it settles with the seller; or with the seller, for a manual method.
- The three choices on the line's extent (Decision outcome): where B ends; and, at launch, fees and anything owed to Sharrwah or its partners billed apart, and no balance sellers pay into, with the other way of each reserved.
- A and B stay possible behind the payment boundary. Building either, and switching it on in a market, is the founder's decision in a record of its own, which this record provides for, so neither changes this record. The same holds for the reserved way of choices 2 and 3.
- So at launch Sharrwah has no platform payment service or balance (area A-12); no account that would hold sellers' money through Sharrwah (part of area A-13); no shipping that collects cash under Sharrwah's own contract (part of area A-10); no balance sellers pay into (part of area A-03); no marketplace run by Sharrwah that collects buyers' payments for sellers (part of area A-21); and no merchant-of-record arrangement in which Sharrwah or a partner holds sellers' money. The order of the areas (S-02) takes this as given.

**Takes as given:**
- The founder's guard of 18 October, which names A and B (`founder-decisions.tsv`, G1).
- F-00, one platform for many markets with the first market not the design target, and the market guard (`founder-decisions.tsv`; `METHOD.md` section 3a).

**Leaves open:**
- Which payment methods and providers Sharrwah offers, in which markets, and the contracts with them — S-07. Carried: under C any provider fits that holds the money under the seller's own agreement. One placed in B comes to the founder. Building B and switching it on would be the founder's decision in a record of its own, which this record provides for.
- Where B ends, for a provider or courier whose account would be set up through Sharrwah — S-07. Carried: this record draws the line by who holds the money and under whose agreement (choice 1, as the founder confirms it), and a case on B's side, or between B and C, comes to the founder.
- Shipping with cash on delivery, including any Sharrwah shipping labels — S-05. Carried: a courier under the seller's own agreement is C, even if the seller asked for it through Sharrwah (choice 1). Cash a courier collects under Sharrwah's own contract, into a Sharrwah balance or settled to sellers, is held through Sharrwah and comes to the founder. That rests on the glossary's reading of the guard's leading clause, which the founder confirms with this line.
- Gift cards, store credit and customer wallets — S-05. Carried: they spend value the seller owes and hold no sellers' money. A wallet buyers pay money into would hold buyers' money, which is outside this record and would be a founder decision of its own (`METHOD.md` section 3).
- Money products for sellers, such as loans, cash advances, cards and bill pay (area A-13) — S-02 places them in the first version's order. Carried: a loan or advance repaid apart holds no sellers' money. One repaid from sellers' money at a provider is reserved by choice 2, the founder's decision in a record of its own. A business account receiving payouts through Sharrwah is held through Sharrwah, and stays off.
- Selling in person, and sales channels or marketplaces — S-10. Carried: in person the money goes through the seller's providers, or to the seller in cash. A marketplace Sharrwah runs, collecting buyers' payments for sellers, would be held through Sharrwah, which stays off. An outside marketplace where the seller sells under its own account and contract keeps the money under that contract (C), or comes to the founder if its account would be opened through Sharrwah.
- Sharrwah's prices and plans — S-03. Carried: whatever they are, at launch its fees are billed apart (choice 2), and no balance sellers pay into is kept (choice 3). Taking fees from sellers' money at a provider, or such a balance, is reserved: the founder's decision in a record of its own, which this record provides for.
- What the seller is shown of each provider's balances and payouts — S-07. Carried: showing reads a provider's records and holds nothing.
- The company that contracts with sellers, and each market's licensing rules — S-08. Carried: nothing is held, so no licence to hold sellers' money is needed for C. Whether a market's rules license a platform that only links sellers' own providers is read at S-08. That would change where, and by which company, Sharrwah may run, not who holds the money.
- When the seller is paid under installments (D-005, deferred) — S-07. Carried: under C the installment provider pays the seller.
- Currencies — S-04. Carried: no money is held, so no currency is held either.

## Decision drivers

- The founder's guard of 18 October.
- **Who the references name as holding the money:**
  - payment processors: Shopify's Payment Processors, and Adyen N.V. behind Shopify Payments; Stripe, in its own terms;
  - on Shopify's international Managed Markets orders, Global-e, which acts as the merchant of record (Evidence, B).
- **In the first market:**
  - in the internationally recognized government's area, as of February 2026, payment services need a licence from the central bank (for banks and licensed non-bank institutions);
  - in the Houthis' area, as of 11 February 2026, banks and fintech companies issue e-money in cooperation with the Sana'a central bank. Non-bank institutions there were made eligible in 2020 to obtain a licence to offer e-rial services (YA-102, as corrected).
- **One platform for many markets** (G1's B1 and B2, which the founder gives as intent, not as decisions): "Adding a market, a currency or a provider shouldn't need a redesign", and a market's law, sanctions and licences, and the founder's choice of providers, "should mostly decide what is available there, not how Sharrwah is built". *(The coordinator's reading: adding a holding arrangement in a market shouldn't need a redesign.)*
- **What is shown working in the first market,** as Context.

## Considered options

| Option | Where the money sits | What it needs built | What it needs from outside |
| --- | --- | --- | --- |
| **A. Sharrwah holds a balance for the seller** | in accounts in Sharrwah's name, with a balance per seller, as Salla and Zid present their balances | a ledger of seller balances, collection into Sharrwah's accounts, payouts and reconciliation | in the first market, a licence or permission to provide payment services under each area's rules (YA-102, YK-515). *(The coordinator's reading: other markets have rules of their own, and no cited source shows whether a licensed partner could hold the money for Sharrwah instead.)* |
| **B. A processor holds it, in an account the seller opens through Sharrwah** | with the processor, as Shopify Payments' processors (its Payment Processors; Adyen N.V.) hold, and as Stripe's terms say of funds held by Stripe, within the scopes under Evidence | an integration with the processor, onboarding sellers to it, and showing its balance | a processor that serves the market and holds funds in accounts opened through Sharrwah |
| **C. Each payment method's own arrangement holds it:** a provider, in the seller's own account with it; a courier under the seller's own contract, until it settles with the seller; the seller, for a manual method | with each provider, as in BigCommerce's "merchant account with your merchant service provider" (S01-V-532); with each courier; with the seller | an integration with each provider and courier (none for a manual method), and one boundary over them (D-002) | a contract between the seller and each provider or courier, and, where a provider requires one, Sharrwah's own integration agreement with it: both platforms offer providers from a list they keep (`HC:payments/third-party-providers/configuring-providers.md:30`; `SA-en:807`) |
| **Defer** | undecided | the boundary only | nothing now |

## Decision outcome

Chosen option: **C at launch, with A and B reserved and not built.** Each payment method leaves the money where its own arrangement puts it:
- where a provider keeps accounts, such as a wallet or a bank, in the seller's own account with it;
- for a courier collecting cash on delivery, with the courier until it settles with the seller under their agreement;
- for a manual payment method, where the buyer pays the seller directly, with the seller.

Sharrwah holds none. With it come three choices on the line's extent, set out for the founder above, as recommended:
1. B ends where the money is held under the seller's own agreement with a provider: such an account is C, even when the seller asked for it through Sharrwah, unless Sharrwah would be party to the money or to the provider's agreement for it;
2. at launch, Sharrwah's fees, and anything owed to Sharrwah or its partners, are billed apart, not taken from sellers' money by a provider;
3. at launch, Sharrwah keeps no balance that sellers pay into.

The payment boundary, as proposed (D-002), leaves room for A or B behind it. Building either, and switching it on in a market, is the founder's decision, made in a record of its own. So is the reserved way of choices 2 and 3: fees or repayments taken from sellers' money at a provider, and a balance sellers pay into.

## Consequences

- **Decisions 2 to 12 follow column C** (D-004). Each provider settles, pays out, collects and deducts its own fees, and Sharrwah bills its own fees separately.
- **The seller ledger** records what is owed, and holds nothing (D-003).
- **The settlement contract** (holding, netting and payouts) stays reserved, and is not built.
- **To reverse:**
  - A needs a licence or permission where it is offered (or, in the coordinator's reading, perhaps a licensed partner instead), plus a ledger of balances, payouts and reconciliation behind the boundary;
  - B needs a processor that holds funds in accounts opened through Sharrwah;
  - neither changes the order side while D-002 holds.
- **The pilot's last two decisions:** Decision 13, installments, is deferred (D-005). Decision 14, currency, moves to subject S-04.

## The guard

- **Outcome type: Built.** The arrangement built is C. A and B are named in the range but reserved: they are not built. Once more than one is built, which one is on in a market becomes a Configured value that the founder owns.
- **No market's facts shape the outcome.** Nothing that holds money is built at launch, because this record chooses C. The founder's guard limits only what goes live: it neither requires a proposal to provide for A or B, nor rules one out. A market's facts decide only where A or B could later be switched on.

## Evidence

Each fact carries the conditions its source gives.
- The pilot's statements are in `studies/subjects/S-01/` and `studies/proposals/records/`.
- Stage 1's facts are in `studies/yemen-cases/`, with the R5 checks' corrections from `studies/proposals/checks/R5/yemen/` applied.
- `python3 -I method/record_ids.py ID` shows each one's sources.

**In the references, all three arrangements exist.**
- **A, a balance the platform keeps:**
  - **Salla's help article on electronic payments,** last updated 22 September 2026: "عند قيام العميل بالدفع، تذهب الأموال أولاً إلى رصيد المدفوعات الإلكترونية" (when the customer pays, the money goes first to the electronic payments balance) (S01-V-016: S01-SA-003).
  - **Salla's article for the UAE,** of 12 September 2026: "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها" (the electronic payments balance keeps the store's sales proceeds before they are transferred) (S01-V-016: S01-SA-056). Salla doesn't say which partner holds the money behind the balance.
  - **Zid's help,** of 6 August 2026: "المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد" (the amounts in your Zid Pay account balance that have not yet been deposited to your bank account) (S01-V-023: S01-ZD-034). Zid Pay's terms are published for Saudi Arabia and for Kuwait (S01-ZD-019).
  - **Zid's terms,** of August 2026, for cash on delivery through Zid's own shipping service (Zid Ship, direct shipping): "تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي" (Zid collects the amounts from the end customers and transfers the total dues to the merchant's wallet twice each calendar month) (S01-V-656: S01-ZD-069).
- **B, a processor or another party holds behind the platform's payment product:**
  - **Shopify:**
    - "The Payment Processors may hold funds in your Shopify Payments Account while awaiting the information requested above" (S01-V-003).
    - On international Managed Markets orders, which are available to businesses based in the continental US and to certain stores in Canada and the UK: "Global-e holds the funds to remit the costs to proper authorities that are involved in the cross-border commerce transaction" (S01-V-001).
    - Where Adyen N.V. is the Payment Processor (the EMEA rows of the Payment Processor List; the EU / EEA and UK terms), its terms speak of "amounts held by Processor prior to Settlement of such funds to User" (S01-V-006).
  - **Stripe, in its own terms** (recorded in the pilot with WooCommerce's statements; no cited source says Stripe holds behind WooPayments):
    - "funds held by Stripe or an applicable Affiliate" (S01-V-008);
    - settlement funds are "combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers" (S01-V-011).
- **Where no cited source says who holds the money:**
  - **WooCommerce:** money made with WooPayments "must flow through your WooPayments account balance before it’s paid out into your bank account" (S01-V-015).
  - **BigCommerce,** with BigCommerce Payments, for US customers (blog of 31 March 2026) and for UK and EMEA customers (blog of 6 October 2026), on the Core, Growth and Scale plans: "PayPal powers the payment processing behind the scenes through your linked PayPal account, but all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account" (S01-V-027).
- **C, the seller's own account with each provider:**
  - **BigCommerce's help on payment gateways,** under "Where do I manage my funds?" (13 October 2026): "You will control and direct funds in your merchant account with your merchant service provider" (S01-V-532: S01-BC-088).
  - **BigCommerce's PayPal page:** "Funds credit immediately into your PayPal business account while payments process" (S01-V-026: S01-BC-023). Its help describes PayPal Checkout as "a standalone PayPal integration that allows you to receive payments to your PayPal account" (S01-BC-077).
  - **Salla,** with a shipping company outside Salla's own waybills, as of 31 August 2026: "تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين" (cash-on-delivery amounts are settled directly between the merchant and the shipping company, under the agreement between them) (S01-V-038: S01-SA-091).

**In the first market** (Context):
- **B is not shown:**
  - **Stripe:** "not supported for a business in Yemen (Yemen not among the supported countries/regions)" (YA-62, as corrected). Payments to or from Yemen are not addressed.
  - **WooPayments:** the source is "a user's request of 2021-12-20 to add it for Yemeni businesses, shown as Open (last updated December 20, 2021)" (YA-62, as corrected). It doesn't show WooPayments as unavailable.
  - **PayPal:** an undated article of a store platform (Matjari Online), live on 10 October 2026, lists Yemen among the Arab countries that can only send money through PayPal, not receive it (YK-514, as corrected). PayPal's own country list would settle it.
  - **Local providers serve merchants through banks:**
    - SabaCard offers the banking and financial market in Yemen "acquiring of local and international Visa and Mastercard cards" (YK-161, read 10 October 2026);
    - card gateways are "available through banks, for local and international cards @ e-payment gateway (MEPS Yemen)'s service" (10 October 2026), though a 2025 source gives "lacking @ place not stated" (YA-107).

    Stage 1's records of these providers don't say whether any would hold funds in an account opened through a platform.
- **A needs a licence:**
  - **The internationally recognized government's area,** as of February 2026: payment services need a licence from the central bank, for banks and licensed non-bank institutions (YA-102, as corrected).
  - **The Houthis' area,** as of 11 February 2026: banks and fintech companies issue e-money in cooperation with the Sana'a central bank. Non-bank institutions there were made eligible in 2020 to obtain a licence to offer e-rial services (YA-102, as corrected).
  - **The licence in the government's area** needs "a joint-stock company with paid-up capital of at least 500 million rials, 750 million for a system operator". This is by the central bank's instructions of 13 September 2022, and the central bank may raise or lower it at any time. A news report of 21 September 2022 gives 700 million (YK-515, as corrected).
  - **There,** the licensing authority is "the central bank in Aden @ the internationally recognized government's area" (YA-103, as of 30 June 2024). By the central bank's instructions of 8 August 2023, the funds behind e-money are "held at a bank" (YA-106).
- **Providers across the two areas:** a provider from Sana'a may operate in Aden only with separate infrastructure in the South (at Aden, as of 5 April 2024; YK-124, as corrected). The source gives this one direction only.
- **C is shown working:**
  - **Cash e-wallet's own page:** "As soon as the customer clicks “Pay via Cash Pay”, the amount is deducted from their account and added to your Cash Wallet account" (YK-131's Cash Pay part, YE-E765; the R5 check found it holds). YK-131's Floosak part says more than its quotes, and isn't relied on. Its E-Pay part rests on a community-written client.
  - **A courier** collects payment on delivery: "available to business accounts @ Torod's service" (YK-203, 10 October 2026).
  - **Buyers pay into the seller's own account:** "accepted, by money transfer or to the store's Kuraimi accounts @ Dakhm store's service" (10 October 2026), and "in advance, to the seller's account @ Sana'a" (a report of 14 May 2025) (YA-131).

## Confirmation

**Scenarios,** answered from the accepted decisions alone:
1. A buyer in Aden orders and pays cash on delivery. The courier collects the cash and pays the seller. Sharrwah bills its own fee separately, and at no point holds the money.
2. A buyer pays by wallet. The wallet takes the money into the seller's own wallet account. Sharrwah records the outcome (D-002) and what is owed (D-003).

**Change scenarios** (`METHOD.md` section 3a):
- **A second market where a processor holds the funds:** B is built behind D-002, and the founder switches it on for that market. Nothing on the order side changes.
- **The company based in Oman:** nothing changes. Sharrwah holds no money, and each provider contracts with the seller in that market.
- **The first market dropped:** nothing changes.

**Checks:** level 3. An independent agent checks every fact above against its source, with the conditions the source gives (`decisions/checks/`).

**Review** when a licence or a licensed partner becomes available in a market Sharrwah serves, or a processor offers accounts opened through Sharrwah.

**Gaps.** None of these changes C at launch. The first decides which providers fit it:
- Whether each provider serving a market opens its sellers' accounts itself, or through a platform: Stage 1's records don't say for the first market. The work: ask each provider when S-07 proposes it. It decides which providers are C at launch, since one whose account would be opened through Sharrwah comes to the founder.
- The guard's reach beyond A and B, such as a courier collecting cash under Sharrwah's own contract, is the coordinator's reading of its leading clause. Choice 1 rests on the guard's source as much as its words, and choices 2 and 3 are left open by C itself. The work: the founder confirms or corrects them with this line.
- Whether the first market's wallets let a seller link its own account with its own keys, or connect only under a platform's contract: the held quote shows only where the money lands (YK-131). The work: ask each wallet when S-07 proposes it.
- Whether a market's rules license a platform that only links sellers' own providers: the first market's sources name a licence for "payment services" (YA-102) without saying whether it turns on holding funds. The work: read the central banks' own definitions at S-08.
- PayPal's limit in the first market rests on one undated third-party article (YK-514). The work: capture PayPal's own country list. It is needed at S-07, if PayPal is proposed.
- Whether Salla limits outside gateways to some kinds of store isn't settled by the held articles (glossary, *payment provider*). Nothing here turns on it.
