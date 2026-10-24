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
evidence: S01-V-001 S01-V-003 S01-V-006 S01-V-008 S01-V-011 S01-V-015 S01-V-016 S01-V-018 S01-V-023 S01-V-026 S01-V-027 S01-V-038 S01-V-532 S01-V-656 YA-62 YK-514 YK-161 YA-107 YK-131 YE-E765 YA-102 YK-515 YK-87 YA-103 YA-106 YA-217 YA-26 YK-124 YA-68 YA-109 YK-203 YA-131
trigger: —
date: 2026-10-24
---

# Who holds sellers' money at launch

The pilot's Decision 1 (`studies/subjects/S-01/entry.md`, S01-VP-01). The founder answers it.

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
- C is what works there today.

**It also settles Decisions 2 to 12** as column C of the pilot's table (D-004). Decision 13 is deferred (D-005), and Decision 14, currency, moves to the markets subject.

**Risk:** low. Turning on A or B later needs a licence or a processor, and your decision. It doesn't need a change to the order side, if D-002 holds.

**Answer:** confirm / change

## Context and problem statement

**The pilot's question** (phase C): "Between the buyer's payment and the payout, who should hold a merchant's funds in Sharrwah: a balance Sharrwah keeps for the merchant, the payment processor's accounts, or the provider of each payment method?"

**At G1 (18 October) the founder** deferred all 14 of the pilot's decisions, and set a guard: "No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision: whether Sharrwah itself holds it (the entry's option A) or a payment company holds it in an account opened through Sharrwah (option B)" (`founder-decisions.tsv`). That guard already decides what can go live. This record makes it the design's starting point.

## Decision drivers

- The founder's guard of 18 October.
- Holding others' money needs a licence, or a licensed partner that holds it. The references rely on licensed processors; the first market requires a central bank licence.
- One platform for many markets: adding a holding arrangement in a market must not need a redesign (G1's B1 and B2).
- What is shown working in the first market, as Context.

## Considered options

| Option | Where the money sits | What it needs built | What it needs from outside |
| --- | --- | --- | --- |
| **A. Sharrwah holds a balance for the seller** | in accounts in Sharrwah's name, with a balance per seller | a ledger of seller balances; collection into Sharrwah's accounts; payouts; reconciliation | a licence, or a licensed partner that holds the money for Sharrwah |
| **B. A processor holds, in an account the seller opens through Sharrwah** | with the processor, as Stripe, Adyen, Global-e and PayPal hold for Shopify, WooCommerce and BigCommerce | an integration with the processor; onboarding sellers to it; showing its balance | a processor that serves the market and holds funds in accounts opened through Sharrwah |
| **C. Each payment method's provider holds, in the seller's own account with it** | with each provider, as in BigCommerce's "merchant account with your merchant service provider" (S01-V-532) | an integration with each provider; one boundary over them (D-002); showing the seller each provider's balance | a contract between the seller and each provider |
| **Defer** | undecided | the boundary only | nothing now |

## Decision outcome

Chosen option: **C at launch, with A and B reserved and not built.** Each payment method's provider holds the money, in the seller's own account with it. Sharrwah holds none. The payment boundary (D-002) is built so that A or B can be added behind it later, each switched on in a market only by the founder's decision.

## Consequences

- Decisions 2 to 12 follow column C (D-004). Each provider settles, pays out, collects and deducts its own fees, and Sharrwah bills its own fees apart.
- The seller ledger records what is owed, and holds nothing (D-003).
- The settlement contract (holding, netting, payouts) stays reserved and is not built.
- To reverse it:
  - A needs a licence or a licensed partner, plus a ledger of balances, payouts and reconciliation behind the boundary;
  - B needs a processor that holds funds in accounts opened through Sharrwah;
  - neither changes the order side while D-002 holds.
- Decision 13, installments, is deferred (D-005). Decision 14, currency, moves to subject S-04.

## The guard

- **Outcome type: Built.** The arrangement built is C. A and B are named in the range but reserved: they are not built. Once more than one is built, which one is on in a market becomes a Configured value that the founder owns.
- **No market's facts shape the outcome.** Nothing that holds money is built, because Sharrwah has no licence or licensed partner anywhere today, and because of the founder's guard. A market's facts decide only where A or B could later be switched on.

## Evidence

**What the references do** (the pilot's entry, "What the references do"):
- **Shopify:** "The Payment Processors may hold funds in your Shopify Payments Account" (S01-V-003). Elsewhere Global-e (S01-V-001) and Adyen (S01-V-006) hold.
- **WooCommerce:** "funds held by Stripe or an applicable Affiliate" (S01-V-008), in pooled accounts at financial providers (S01-V-011), with the WooPayments balance in front of them (S01-V-015).
- **BigCommerce:**
  - its payments flow through a BigCommerce Payments account (S01-V-027);
  - with the standalone PayPal gateway, funds go to "your PayPal business account" (S01-V-026);
  - "You will control and direct funds in your merchant account with your merchant service provider" (S01-V-532).
- **Salla:**
  - the money "تذهب ... أولاً إلى رصيد المدفوعات الإلكترونية" (goes first to the electronic payments balance) (S01-V-016), and cash on delivery has a balance of its own (S01-V-018);
  - with an outside courier, cash on delivery is settled "مباشرة بين التاجر وشركة الشحن" (directly between the merchant and the shipping company) (S01-V-038).
- **Zid:** the Zid Pay balance, for Saudi Arabia and Kuwait (S01-V-023), and its own courier service's cash on delivery paid to the merchant's wallet (S01-V-656).

**What the first market shows** (Stage 1's facts as the pilot used them, with the R5 checks' corrections in `studies/proposals/checks/R5/yemen/`):
- **Processors:**
  - Stripe is not supported for a business based in Yemen: Yemen is not among its supported countries (YA-62, as corrected). This says nothing about payments to or from Yemen.
  - For WooPayments the source is only an anonymous request of 20 December 2021 to add it for Yemeni businesses, shown as open (YA-62, as corrected). It doesn't show WooPayments as unavailable.
  - PayPal: "Sending from Yemen", and an account there "cannot receive money" (YK-514).
- **Card acceptance and gateways:**
  - a card acquirer offers "acquiring of local and international Visa and Mastercard cards" (YK-161);
  - card gateways are "available through banks, for local and international cards" (YA-107; the R5 check found it holds).
- **Payment APIs that pay into the seller's own account:**
  - With Cash Pay, "the amount is deducted from their account and added to your Cash Wallet account" (YK-131, YE-E765). The R5 check found the Cash Pay part holds.
  - YK-131's Floosak part says more than its quotes, and is not relied on here. Its E-Pay part rests on a community-written client.
- **Who may hold others' money:**
  - e-money and electronic payment services are for "banks and licensed non-bank institutions" in one area, and "banks and non-bank institutions" in the other (YA-102);
  - a provider licence there needs "a joint-stock company with paid-up capital of at least 500 million rials" (YK-515), from the Aden central bank (YA-103);
  - the funds behind e-money are "held at a bank" (YA-106);
  - wallets' licences are split by area (YA-217), and the bar on 12 wallets was reversed (YA-26).
- **Across the two areas:** a payment provider from Sana'a may operate in Aden only with separate infrastructure in the South (YK-124, as corrected: the source gives this one direction only, at Aden, as of 5 April 2024).
- **What works:**
  - wallets take online payments (YA-68, YA-109);
  - a courier collects cash on delivery for business accounts (YK-203);
  - buyers pay into the seller's own account (YA-131).

## Confirmation

**Scenarios**, from the accepted decisions alone:
1. A buyer in Aden orders and pays cash on delivery. The courier collects the cash and pays the seller. Sharrwah bills its own fee apart, and at no point holds the money.
2. A buyer pays by wallet. The wallet takes the money into the seller's own wallet account. Sharrwah records the outcome (D-002) and what is owed (D-003).

**Change scenarios** (`METHOD.md` section 3a):
- **A second market where a processor holds the funds.** B is built behind D-002, and the founder switches it on for that market. Nothing on the order side changes.
- **The company based in Oman.** Nothing changes: Sharrwah holds no money, and each provider contracts with the seller in that market.
- **The first market dropped.** Nothing changes.

**Checks:** level 3. Every fact above is checked against its source by an independent agent, with the conditions the source gives.

**Review** when a licence or a licensed partner becomes available in a market Sharrwah serves, or a processor offers accounts opened through Sharrwah.
