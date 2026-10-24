---
id: D-003
title: The seller ledger records what is owed, and holds no money
subject: S-01
status: proposed
door: two-way
integrity: 2
outcome: Built
varies_by: —
risks: W-07
evidence: E034 E035
trigger: —
date: 2026-10-24
---

# The seller ledger records what is owed, and holds no money

It answers the Knowledge Map's KM-ENG-05 for money in the ledger (amounts, currencies, and computing without rounding errors). Rounding rules, currency conversion and time zones are taken up at subject S-04.

## Context and problem statement

Under D-001 Sharrwah holds no sellers' money. Sellers and Sharrwah still need one record of what is owed to and by each seller: sales, fees, refunds, and what each provider has paid out. What form should it take?

## Decision drivers

- It must not become a balance Sharrwah holds (D-001; the founder's guard of 18 October).
- Money records that are edited in place lose their history and break reconciliation. Shopify makes money-moving requests idempotent (E034, E035).
- The seam study found "the ledger pattern is shared": "append-only entries, idempotent posting, and reversal instead of edit" (`8946887:studies/payment-seam/seam.md`, rule 19).

## Considered options

1. **An append-only ledger of what is owed,** separate from who holds the money.
2. **A balance per seller, updated in place.** This is simpler, but it reads as money Sharrwah holds, and it loses history.
3. **No ledger: read each provider's balance when needed.** Nothing then answers what Sharrwah's own fees are, or what is owed across providers.

## Decision outcome

Chosen option: **1, an append-only ledger of what is owed.**
- Each amount owed to or by a seller is one entry: for a sale, a fee, a refund or a payout reported by a provider. Each entry is in one currency, and amounts are kept in the currency's minor units.
- Entries are posted once, by an idempotency key, and never edited. A mistake is corrected by a reversing entry.
- Balances are per currency, and never added across currencies. They move between currencies only by a recorded conversion.
- Each entry names the custodian, meaning who holds the money it concerns (a provider, a courier or the seller), from the outcome records of D-002. The ledger records what is owed; it does not hold money.
- Sharrwah's own fees are entries owed by the seller to Sharrwah, billed separately (D-004).

## Consequences

- Reconciliation compares the ledger with each provider's reports.
- If A or B is built later (D-001), its holding balances sit behind the payment boundary, and this ledger is unchanged.
- How cash and electronic amounts of one currency are told apart, where a provider prices them differently, is not decided here. It goes to subject S-04 under the guard.

## The guard

- **Outcome type: Built,** the same in every market.
- The Q7 draft's proposal to "keep cash collected on delivery apart from electronic amounts in the seller ledger" was flagged by the guard (`studies/proposals/drafts/Q7/draft.md`:129). It is not adopted here, and goes to S-04.

## Evidence

- E034 and E035, in `evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv`: Shopify's idempotency for money-moving requests.
- The seam study's rule 19, and the Q7 draft's "seller ledger" (`studies/proposals/drafts/Q7/draft.md`:78–80), are candidate options. Their platform facts are checked at level 2.

## Confirmation

- **Scenarios:**
  - a sale, its fee and a partial refund, posted twice by mistake, give one set of entries;
  - a provider's payout report reconciles with the entries.
- **The change scenario:** the first market dropped. Nothing changes.
- **Checks:** level 2.
