---
id: D-004
title: The pilot's Decisions 2 to 12 follow column C
subject: S-01
status: proposed
door: one-way
integrity: 3
outcome: Built
varies_by: —
risks: W-07
evidence: S01-VP-02 S01-VP-03 S01-VP-04 S01-VP-06 S01-VP-09 S01-VP-11 S01-VP-15 S01-VP-19 S01-VP-20 S01-VP-21 S01-VP-10
depends_on: D-001
trigger: —
date: 2026-10-24
---

# The pilot's Decisions 2 to 12 follow column C

The founder's line in D-001 settles these too. The pilot's entry offered exactly this: "You can answer Decision 1 and let it settle those as a standing decision" (`studies/subjects/S-01/entry.md`, "In short").

## Context and problem statement

In the references, the party that holds the money is mostly also the one that settles it, pays it out, collects it, deducts from it, keeps the account and sets the timing. So the pilot's Decisions 2 to 12 follow from Decision 1 (`studies/subjects/S-01/entry.md`, "What Decision 1 implies for the others"). With D-001 at C, what does each become?

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| held through Sharrwah | A or B, as the founder's guard names them; under C, neither | `founder-decisions.tsv` (G1) |
| settlement and payout | Each provider's own, on its own terms; Sharrwah sends no payouts | `GQL:3229`; `SA-en:807`; `HC:payments/getting-paid.md:13` |
| payment provider | The company that processes or receives a payment for a method. A courier is named apart, and "provider or courier" means both | `HC:payments/getting-paid.md:3`; `SA-en:24` |
| seller's own account | An account the seller opened with a provider or courier itself, under its own contract, into which it receives or settles the buyer's payment, linked by the seller's own credentials, keys, account number or email. A bank account that only receives payouts from a platform balance is not C | `HC:payments/third-party-providers/configuring-providers.md:32`; `SA-en:318`; `SA-en:793`; `SA-en:277` |
| cash on delivery | Collected by a courier under the seller's own contract, which settles with the seller | `SA-en:565`; `SA-en:234`; `SA-ar:359` |
| provider fees | Each provider or courier charges its own on its own terms, deducting it from what it settles or invoicing the seller | `SA-en:1241`; `GQL:3605`; `SA-ar:359`; `SA-en:234` |
| Sharrwah's fees | Billed apart from sellers' money, never deducted from it | `HC:payments/getting-paid.md:11` (a precedent) |
| refund and void | Made through each provider, on its own terms; for a manual method, by the seller directly | `HC:fulfillment/managing-orders/refunding-orders.md:16`; `SA-en:804`; `SA-en:994` |
| agency role | Sharrwah is appointed no seller's agent to receive or hold buyers' payments. Sending a provider the seller's instructions with the seller's own keys, such as a capture or a refund, is not an agency role | S01-VP-06 |
| security interest | Sharrwah takes none | S01-VP-10 |

## Scope

**Decides:**
- The pilot's Decisions 2 to 12, each as column C of its table, as listed under the outcome.

**Takes as given:**
- D-001's outcome as proposed: C at launch, with A and B reserved (in `depends_on`). This record is confirmed with D-001, or falls with it.

**Leaves open:**
- Sharrwah's terms with sellers, and the company that offers them — S-08. Carried: the terms say that each provider's terms govern the money it holds, whichever company offers them.
- How Sharrwah sets and bills its fees — S-03. Carried: whatever they are, they are billed apart from sellers' money.
- What the seller is shown of each provider's settlement times and balances — S-07. Carried: showing reads each provider's own records, and changes none of the answers above.
- The terms of each provider Sharrwah integrates — S-07. Carried: whatever a provider's terms say, Sharrwah takes no agency role and no security interest under this record. A provider that required either from Sharrwah would come to the founder.

## Decision drivers

- D-001: C at launch, with A and B reserved.
- The pilot's table, which gives each decision's answer under each option, as the references pair them.
- The pilot's recommendation for each, written under C.

## Considered options

1. **Take column C of the pilot's table for all eleven.**
2. **Decide each one separately.** Each falls back on the same reasoning, because under C Sharrwah holds nothing that it could settle, pay out, deduct from or secure.

## Decision outcome

Chosen option: **1, column C,** with the pilot's recommendation for each:

| Pilot's decision | Under C |
| --- | --- |
| 2. Who settles the funds to the seller (S01-VP-02) | each provider |
| 3. Who sends payouts (S01-VP-03) | each provider, or the seller withdraws from their own account with it; Sharrwah sends no payouts |
| 4. Who collects the buyer's payment (S01-VP-04) | each provider or courier: the wallet, the courier, or the seller's own bank |
| 5. Whether Sharrwah acts as the seller's agent (S01-VP-06) | no agency role |
| 6. Who deducts fees and refunds (S01-VP-09) | each provider or courier its own, on its own terms; Sharrwah bills its own fees separately |
| 7. Which accounts a seller holds (S01-VP-11) | an account with each provider, linked through Sharrwah; a Sharrwah account serves only Sharrwah's own billing |
| 8. Payout timing (S01-VP-15) | each provider's own settlement and payout times, and each courier's transfer days, under its agreement with the seller. Under a manual method the buyer pays the seller directly. What the seller is shown of them is left to S-07 |
| 9. Deducted before payout, or billed apart (S01-VP-19) | each provider or courier charges its own on its own terms, deducting it from what it settles or invoicing the seller; Sharrwah bills its fees separately |
| 10. Funds held when the service ends (S01-VP-20) | Sharrwah holds nothing; its terms say each provider's terms apply |
| 11. When funds go back to buyers (S01-VP-21) | none for Sharrwah; its terms say each provider's terms apply |
| 12. A security interest over the seller's funds (S01-VP-10) | Sharrwah takes none; each provider's terms apply to the funds it holds |

## Consequences

- Sharrwah bills its own fees through its own billing, as entries owed by the seller (D-003). It never nets them from sellers' money.
- Sharrwah's terms with sellers say that each provider's terms govern the money that provider holds. The company's terms are drafted at subject S-08.
- If A or B is switched on in a market later (D-001), each of these is decided again for that arrangement. The pilot's columns A and B give the starting answers.

## The guard

- **Outcome type: Built,** the same in every market: no part of the platform settles, pays out, deducts from or secures sellers' money.
- Which providers serve a market is Configured, behind the payment boundary (D-002).

## Evidence

The pilot's variation points and their statements (`studies/subjects/S-01/variation-points.tsv`), as the entry cites them for each decision. They were checked by the pilot's independent review (`studies/subjects/S-01/review.md`). Under the level 3 checks, the facts each row rests on are checked again with D-001's.

## Confirmation

- **Scenarios:**
  - a refund on a wallet payment;
  - a seller who leaves the platform with payments still pending at their providers;
  - a fee that Sharrwah bills to a seller.

  Each is answered from D-001 to D-004 alone.
- **Checks:** level 3, with D-001.
- **Gaps:** none bears on these answers.
  - Which providers' terms would ask Sharrwah for an agency role or a security interest is read when S-07 proposes each provider.
  - How either platform returns money for a manual method isn't in the held evidence. The work: a capture of each platform's refund page for a bank-transfer order, at S-05.
