---
id: D-005
title: When the seller is paid under installments
subject: S-01
status: deferred
door: one-way
integrity: 1
outcome: Configured
varies_by: market (which installment providers serve it)
risks: W-01
evidence: S01-VP-22
depends_on: D-001
trigger: an installment or pay-later provider is offered in a market Sharrwah serves
date: 2026-10-24
---

# When the seller is paid under installments

The pilot's Decision 13 (S01-VP-22).

## Context and problem statement

The pilot asked: "Under instalment or pay-later payments, when should a Sharrwah merchant be paid: in full after capture with the platform's other payouts, up front while the buyer owes the instalment provider, or on the instalment provider's own schedule under its agreement with the merchant?" (`studies/subjects/S-01/entry.md`, Decision 13).

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| installments and pay later | The buyer pays in parts, or later, to a provider who pays the seller | `HC:payments/additional-payment-methods/activate-payment-methods.md:3`; `SA-en:565` |
| settlement and payout | When that provider pays the seller | `GQL:3229`; `SA-en:807` |
| payment provider | The installment company | `SA-en:565` |

## Scope

**Decides:**
- To defer when the seller is paid under installments or pay later, until its trigger.

**Takes as given:**
- D-001's outcome: Sharrwah sends no payouts (in `depends_on`).

**Leaves open:**
- Which installment providers are offered, and their schedules — S-07. Carried: the decision is deferred, and its starting answer, the provider's own schedule, fits C.

## Decision drivers

- No installment provider is shown in the first market (the pilot's entry).
- D-001: Sharrwah sends no payouts.

## Considered options

1. **Decide now.**
2. **Defer until an installment provider is offered in a market Sharrwah serves.**

## Decision outcome

Chosen option: **2, defer.** When this is taken up, the starting answer is the pilot's recommendation: the seller is paid on the provider's own schedule under its agreement with the seller, which fits C (D-001).

## Consequences

- Installment and pay-later providers plug in like any other method, through the payment boundary (D-002).
- No part of the core assumes a payout schedule.

## The guard

- **Outcome type: Configured.** Which installment providers serve a market, and on what schedule, is set per market.

## Evidence

The pilot's Decision 13 and its variation point S01-VP-22.

## Confirmation

Reopened by its trigger.
