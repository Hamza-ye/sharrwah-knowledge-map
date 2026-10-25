---
id: D-006
title: The first market's row for who holds sellers' money
subject: S-01
status: proposed
door: one-way
integrity: 3
outcome: Configured
varies_by: market (Yemen)
risks: W-07 R-07
evidence: YA-62 YK-514 YK-161 YA-107 YK-131 YE-E765 YA-102 YK-515 YA-103 YA-106 YK-124 YK-203 YA-131
depends_on: D-001
trigger: —
date: 2026-10-25
---

# The first market's row for who holds sellers' money

D-001 decides for every market:
- at launch, the money stays where each payment method's own arrangement puts it (C);
- A and B are a switch per market, which only the founder turns on.

This record is the first market's row for that decision: the condition each arrangement needs, what holds in Yemen, and what the row binds there. It is the one place where D-001's question meets Yemen's conditions. The facts below were D-001's, checked twice at level 3, and moved here unchanged on 25 October 2026 (the founder's test: `reports/M1-market-binding.md`).

## Context and problem statement

Yemen is the first market, not the design target (F-00; `METHOD.md` section 3a). Its conditions are Context: they bind values in that market, and never shape a Built outcome. A decision made from the references alone, without the first market, reaches D-001's line (`decisions/checks/M1-blind-decision-1.md`). So Yemen's conditions decide only what is on in Yemen.

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| held through Sharrwah | A and B, as D-001 and the founder's guard define them | `founder-decisions.tsv` (G1) |
| seller's own account | An account the seller holds with a provider or courier under its own agreement | `HC:payments/third-party-providers/configuring-providers.md:32`; `SA-en:318` |
| cash on delivery | Cash to a courier or to the seller's own staff | `SA-en:565` |
| manual payment method | The buyer pays outside any provider, to the seller or its courier | `HC:payments/manual-payments.md:5`; `SA-en:565` |
| payment provider | The company that processes or receives a payment for a method | `HC:payments/getting-paid.md:3`; `SA-en:24` |

## Scope

**Decides:**
- In Yemen at launch, C is on, as in every market: the money for each sale stays with the seller's own provider, the seller's own courier, or the seller. Offline methods are shown there now; the seller's own providers count once a provider serving sellers there is integrated with Sharrwah (S-07).
- Neither A nor B can be switched on in Yemen until its condition in the row below holds, and the founder decides it in a record of its own.

**Takes as given:**
- D-001's outcome (in `depends_on`).

**Leaves open:**
- Which of Yemen's wallets and providers let a seller link its own account, and which open accounts only through a platform — S-07. Carried: under D-001's choice 1, such a wallet is C where the money is held under the seller's own agreement, and B where Sharrwah would be party to the money or to the provider's agreement for it. A case between them, or one whose account would be opened through Sharrwah, comes to the founder.
- Whether Yemen's licence for "payment services" covers a platform that only links sellers' own providers — S-08. Carried: it would change where, and by which company, Sharrwah may run there, not who holds the money.
- Yemen's two areas, and whether a seller in one may sell to buyers in the other (F-02, F-03; PAY-43) — S-04. Carried: who holds the money is the same in both.
- PayPal's own country list — S-07. Carried: PayPal would be C under the seller's own agreement. If its account were opened through Sharrwah, choice 1 places it, and it comes to the founder.

## Decision drivers

- D-001's line, and the founder's guard of 18 October.
- The row below.

## The row

The conditions are the references-only decision's own words (`decisions/checks/M1-blind-decision-1.md`, section 6), each for one of its options: O1 and O2 are C, O3 is B, O4 is A. What holds in Yemen comes from Stage 1, as corrected by the R5 checks.

**The pilot's marks come first.** Its phase D marked this variation point, S01-VP-01, in six of Yemen's cases (YC-00, YC-120 to YC-123, YC-156), each `unknown`: "No answer variant is shown to work" (`studies/subjects/S-01/yemen-marks.tsv`). The references' own arrangements either fail there or state no condition:
- Stripe's, WooPayments' and Zid Pay's variants fail on YA-62;
- Shopify's and BigCommerce's conditioned variants fail on Q2, "the places named in the conditions leaving out the Yemeni market";
- the rest "state no condition".

What would show it is a platform statement of where those variants hold. The rows below add what Stage 1 shows of Yemen's own providers.

| Option | Its condition, in any market | In Yemen | Sources |
| --- | --- | --- | --- |
| O1, the seller's own provider (C) | "a provider integrated with Sharrwah serves sellers established there and settles to them directly" | Providers settle to sellers there: a wallet pays into the seller's own wallet account, and buyers pay into the seller's own accounts. None is integrated with Sharrwah yet (S-07) | YE-E765 (YK-131's Cash Pay part); YA-131 |
| O2, offline (C) | "each listed offline method may be accepted there, paid to the seller or the seller's own courier" | Shown: a courier collects on delivery, and buyers pay by transfer to the seller | YK-203; YA-131 |
| O3, a payment company through the platform (B) | "a payment company permitted there to hold sellers' funds in platform-opened accounts accepts Sharrwah; sellers can pass its verification; the founder has decided" | None shown. The pilot called this need "unsettled, not unmet" (`studies/subjects/S-01/entry.md`:119) | YA-62; YK-514; YK-161; YA-107 |
| O4, the platform holds (A) | "Sharrwah holds any authorisation required there to hold others' funds; the founder has decided" | The government's area licenses payment services through the central bank in Aden. In the Houthis' area, non-bank institutions may obtain a licence to offer e-rial services. Whether either covers holding sellers' funds isn't shown (Gaps). *Assumption:* Sharrwah holds no licence; none is recorded. No licensed holder is shown | YA-102; YK-515; YA-103; YA-106 |

## Considered options

| Option in Yemen | Its condition there |
| --- | --- |
| **C** | Offline methods hold; the seller's own providers hold once one is integrated (S-07) |
| **B** | Not shown |
| **A** | Not met by Sharrwah; no licensed holder shown |

## Decision outcome

Chosen: **C in Yemen at launch, as in every market.** A and B stay off there until their conditions hold, and the founder switches one on.

## Consequences

- Nothing changes in D-001 or in any Built record.
- Switching A or B on in Yemen later needs its condition in the row, and the founder's record.

## The guard

- **Outcome type: Configured,** varying by market. This record names Yemen because it is Yemen's row.
- No Built record restates these facts. D-001 points here from its Confirmation.

## Evidence

Each fact carries the conditions its source gives. Stage 1's facts are in `studies/yemen-cases/`, with the R5 checks' corrections from `studies/proposals/checks/R5/yemen/` applied. `python3 -I method/record_ids.py ID` shows each one's sources.

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

**Scenarios in Yemen,** answered from D-001 to D-003 and this row:
1. A buyer in Aden orders and pays cash on delivery. The courier collects the cash and pays the seller. Sharrwah bills its own fee separately, and at no point holds the money.
2. A buyer pays by wallet. The wallet takes the money into the seller's own wallet account. Sharrwah records the outcome (D-002) and what is owed (D-003).

**Checks:** level 3. These facts were checked twice as part of D-001 (`decisions/checks/M1-terms-scope-dispositions.md`). This record's wording was checked with D-001's revision (`decisions/checks/M1-market-binding-check.tsv`), and its findings applied (`decisions/checks/M1-market-binding-dispositions.md`).

**Review** when a licence, a licensed holder, or a payment company that holds through platforms appears in Yemen.

**Gaps:**
- Whether Yemen's wallets let a seller link its own account with its own keys, or connect only under a platform's contract: the held quote shows only where the money lands (YK-131). The work: ask each wallet when S-07 proposes it.
- Whether Yemen's licence for "payment services" turns on holding funds: the sources name the licence (YA-102) without saying. The work: read the central banks' own definitions at S-08.
- PayPal's limit rests on one undated third-party article (YK-514). The work: capture PayPal's own country list, at S-07 if PayPal is proposed.
