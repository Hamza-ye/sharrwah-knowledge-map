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
trigger: —
date: 2026-10-24
---

# Who holds sellers' money at launch

This is the pilot's Decision 1 (`studies/subjects/S-01/entry.md`, S01-VP-01). The founder answers it.

## For the founder

**The question.** Between a buyer's payment and the seller's payout, who holds the money?

**Your line to confirm:** "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours."

**What it means.**
- At launch, each way to pay keeps the money in the seller's own account with its provider: a wallet, the seller's bank, or a courier for cash on delivery. This is the pilot's option C.
- Sharrwah holds none of it, and bills its own fees separately.
- A (Sharrwah holds a balance) and B (a processor holds it, in an account opened through Sharrwah) are not built. The payment boundary (D-002) leaves room to add either later without redesigning the rest.

**Why:**
- your guard of 18 October already keeps A and B from going live without you;
- A needs a licence or a licensed partner, which Sharrwah doesn't have;
- B needs a processor that would hold funds in accounts opened through Sharrwah, and none is shown to serve the first market;
- C is what is shown working there today.

**It also settles Decisions 2 to 12** as column C of the pilot's table (D-004). Decision 13 is deferred (D-005), and Decision 14, currency, moves to the markets subject.

**Risk:** low. Turning on A or B later needs a licence or a processor, and your decision. It doesn't need a change to the order side, if D-002 holds.

**Answer:** confirm / change

## Context and problem statement

**The pilot's question** (phase C): "Between the buyer's payment and the payout, who should hold a merchant's funds in Sharrwah: a balance Sharrwah keeps for the merchant, the payment processor's accounts, or the provider of each payment method?"

**At G1, on 18 October,** the founder deferred all 14 of the pilot's decisions and set a guard: "No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision: whether Sharrwah itself holds it (the entry's option A) or a payment company holds it in an account opened through Sharrwah (option B)" (`founder-decisions.tsv`). That guard already decides what can go live. This record makes it the design's starting point.

## Decision drivers

- The founder's guard of 18 October.
- **Who the references name as holding the money:** where they name anyone behind the platform's product, it is a payment processor (Evidence, B).
- **In the first market,** providing payment services needs a central bank licence (YA-102).
- **One platform for many markets** (G1's B1 and B2): adding a holding arrangement in a market must not need a redesign.
- **What is shown working in the first market,** as Context.

## Considered options

| Option | Where the money sits | What it needs built | What it needs from outside |
| --- | --- | --- | --- |
| **A. Sharrwah holds a balance for the seller** | in accounts in Sharrwah's name, with a balance per seller, as Salla and Zid present their balances | a ledger of seller balances, collection into Sharrwah's accounts, payouts and reconciliation | a licence, or a licensed partner that holds the money for Sharrwah |
| **B. A processor holds it, in an account the seller opens through Sharrwah** | with the processor, as processors do behind Shopify's, WooCommerce's and BigCommerce's payment products, within the scopes under Evidence | an integration with the processor, onboarding sellers to it, and showing its balance | a processor that serves the market and holds funds in accounts opened through Sharrwah |
| **C. Each payment method's provider holds it, in the seller's own account with that provider** | with each provider, as in BigCommerce's "merchant account with your merchant service provider" (S01-V-532) | an integration with each provider, one boundary over them (D-002), and showing the seller each provider's balance | a contract between the seller and each provider |
| **Defer** | undecided | the boundary only | nothing now |

## Decision outcome

Chosen option: **C at launch, with A and B reserved and not built.** Each payment method's provider holds the money, in the seller's own account with it. Sharrwah holds none. The payment boundary (D-002) is built so that A or B can be added behind it later. Each would be switched on in a market only by the founder's decision.

## Consequences

- **Decisions 2 to 12 follow column C** (D-004). Each provider settles, pays out, collects and deducts its own fees, and Sharrwah bills its own fees separately.
- **The seller ledger** records what is owed, and holds nothing (D-003).
- **The settlement contract** (holding, netting and payouts) stays reserved, and is not built.
- **To reverse:**
  - A needs a licence or a licensed partner, plus a ledger of balances, payouts and reconciliation behind the boundary;
  - B needs a processor that holds funds in accounts opened through Sharrwah;
  - neither changes the order side while D-002 holds.
- **The pilot's last two decisions:** Decision 13, installments, is deferred (D-005). Decision 14, currency, moves to subject S-04.

## The guard

- **Outcome type: Built.** The arrangement built is C. A and B are named in the range but reserved: they are not built. Once more than one is built, which one is on in a market becomes a Configured value that the founder owns.
- **No market's facts shape the outcome.** Nothing that holds money is built, because Sharrwah has no licence or licensed partner anywhere today, and because of the founder's guard. A market's facts decide only where A or B could later be switched on.

## Evidence

Each fact carries the conditions its source gives.
- The pilot's statements are in `studies/subjects/S-01/` and `studies/proposals/records/`.
- Stage 1's facts are in `studies/yemen-cases/`, with the R5 checks' corrections from `studies/proposals/checks/R5/yemen/` applied.
- `python3 -I method/record_ids.py ID` shows each one's sources.

**In the references, all three arrangements exist.**
- **A, a balance the platform keeps:**
  - **Salla's help article on electronic payments,** as read on 22 September 2026: "عند قيام العميل بالدفع، تذهب الأموال أولاً إلى رصيد المدفوعات الإلكترونية" (when the customer pays, the money goes first to the electronic payments balance) (S01-V-016: S01-SA-003).
  - **Salla's article for the UAE,** of 12 September 2026: "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها" (the electronic payments balance keeps the store's sales proceeds before they are transferred) (S01-V-016: S01-SA-056). Salla doesn't say which partner holds the money behind the balance.
  - **Zid's help,** of 6 August 2026: "المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد" (the amounts in your Zid Pay account balance that have not yet been deposited to your bank account) (S01-V-023: S01-ZD-034). Zid Pay's terms are published for Saudi Arabia and for Kuwait (S01-ZD-019).
  - **Zid's terms,** of August 2026, for cash on delivery through Zid's own shipping service (Zid Ship, direct shipping): "تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي" (Zid collects the amounts from the end customers and transfers the total dues to the merchant's wallet twice each calendar month) (S01-V-656: S01-ZD-069).
- **B, a processor holds behind the platform's payment product:**
  - **Shopify:**
    - "The Payment Processors may hold funds in your Shopify Payments Account while awaiting the information requested above" (S01-V-003).
    - On international Managed Markets orders, which are available to businesses based in the continental US and to certain stores in Canada and the UK: "Global-e holds the funds to remit the costs to proper authorities that are involved in the cross-border commerce transaction" (S01-V-001).
    - Where Adyen N.V. is the Payment Processor (the EMEA rows of the Payment Processor List; the EU / EEA and UK terms), its terms speak of "amounts held by Processor prior to Settlement of such funds to User" (S01-V-006).
  - **WooCommerce:**
    - Stripe's terms speak of "funds held by Stripe or an applicable Affiliate" (S01-V-008).
    - Settlement funds are "combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers" (S01-V-011).
    - Money made with WooPayments "must flow through your WooPayments account balance before it’s paid out into your bank account" (S01-V-015).
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
  - **Local providers serve merchants:**
    - SabaCard offers "acquiring of local and international Visa and Mastercard cards" (YK-161, read 10 October 2026);
    - card gateways are "available through banks, for local and international cards @ e-payment gateway (MEPS Yemen)'s service" (10 October 2026), though a 2025 source gives "lacking @ place not stated" (YA-107).

    Stage 1's records of these providers don't say whether any would hold funds in an account opened through a platform.
- **A needs a licence:**
  - **The internationally recognized government's area,** as of February 2026: payment services need a licence from the central bank, for banks and licensed non-bank institutions (YA-102, as corrected).
  - **The Houthis' area,** as of 11 February 2026: banks and fintech companies issue e-money in cooperation with the Sana'a central bank. Non-bank institutions there were made eligible in 2020 to obtain a licence to offer e-rial services (YA-102, as corrected).
  - **The licence in the government's area** needs "a joint-stock company with paid-up capital of at least 500 million rials, 750 million for a system operator". This is by the central bank's instructions of 13 September 2022, and the central bank may raise or lower it at any time. A news report of 21 September 2022 gives 700 million (YK-515, as corrected).
  - **There,** the licensing authority is "the central bank in Aden @ the internationally recognized government's area" (YA-103). The funds behind e-money are "held at a bank" (YA-106).
- **Providers across the two areas:** a provider from Sana'a may operate in Aden only with separate infrastructure in the South (at Aden, as of 5 April 2024; YK-124, as corrected). The source gives this one direction only.
- **C is shown working:**
  - **Cash e-wallet's own page:** "As soon as the customer clicks “Pay via Cash Pay”, the amount is deducted from their account and added to your Cash Wallet account" (YK-131's Cash Pay part, YE-E765; the R5 check found it holds). YK-131's Floosak part says more than its quotes, and isn't relied on. Its E-Pay part rests on a community-written client.
  - **A courier** collects payment on delivery: "available to business accounts @ Torod's service" (YK-203, 10 October 2026).
  - **Buyers pay into the seller's own account:** "accepted, by money transfer or to the store's Kuraimi accounts @ Dakhm store's service", and "in advance, to the seller's account @ Sana'a" (YA-131).

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
