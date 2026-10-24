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
trigger: an installment or pay-later provider is offered in a market Sharrwah serves
date: 2026-10-24
---

# When the seller is paid under installments

The pilot's Decision 13 (S01-VP-22).

## Context and problem statement

The pilot asked: "Under instalment or pay-later payments, when should a Sharrwah merchant be paid: in full after capture with the platform's other payouts, up front while the buyer owes the instalment provider, or on the instalment provider's own schedule under its agreement with the merchant?" (`studies/subjects/S-01/entry.md`, Decision 13).

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
