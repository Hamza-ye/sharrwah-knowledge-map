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
evidence: E031 E032 E034 E035 E040
trigger: —
date: 2026-10-24
---

# The seller ledger records what is owed, and holds no money

It answers the Knowledge Map's KM-ENG-05 (`register/km-questions.tsv`) for money in the ledger. How currencies, their minor units and rounding are defined, and time zones, are taken up at subject S-04.

**Its sources:**
- the payment seam (`8946887:studies/payment-seam/seam.md`, below "seam.md"), and its Shopify note (`8946887:studies/payment-seam/notes/shopify-crossings.md`);
- E031 to E035 (`evidence/shopify-engineering/`);
- E040, Active Merchant at commit `ca45b1b`.

## Context and problem statement

Under D-001 Sharrwah holds no sellers' money. Sellers and Sharrwah still need one record of what each seller is owed and owes: sales, refunds, and Sharrwah's own fees. Who owns that record, what form does it take, and how does it stay true to what providers report?

## Decision drivers

- It must not become a balance Sharrwah holds (D-001; the founder's guard of 18 October).
- **Money records edited in place lose their history and break reconciliation.** Shopify's settlement ledger gives each type of balance transaction "a reversal twin" (shopify-crossings.md:141). Shopify's payments-app ids are idempotency keys that don't expire (E032:198; E031:277). Its Admin API keys expire after 24 hours (E034:109, 137).
- **The seam's rule 19:** "The ledger pattern is shared. Append-only entries, idempotent posting, and reversal instead of edit form a shared foundation used by core's order money and payments' custody and settlement ledgers. Each ledger's content belongs to its owner." (seam.md:163)
- **The references keep payouts and fees with payments.** Settlement, payout and custody ledgers stay inside payments (seam.md:49), and reconciling against providers stays there too (seam.md:156). Shopify keeps its settlement ledger, payouts and fees inside payments (shopify-crossings.md:141–142).

## Considered options

1. **One ledger** that records what is owed, and also payouts and provider fees.
2. **A balance per seller, updated in place.** This is simpler, but it reads as money Sharrwah holds, and it loses history.
3. **No ledger: read each provider's balance when needed.** Then nothing answers what Sharrwah's own fees are, or what is owed across providers.
4. **Two ledgers, one per owner,** as rule 19 says.
   - The order side keeps what is owed.
   - Payments keeps custody, payouts and provider fees.
   - The two are joined by the identifiers that cross the payment boundary (D-002).

## Decision outcome

Chosen option: **4, two ledgers, one per owner.** This record decides the order side's ledger: **the seller ledger.**

- **What it records:** what is owed, and who owes whom.
  - Sales and refunds come from D-002's outcome records.
  - Sharrwah's own fees are added to them, as amounts the seller owes Sharrwah, billed separately (D-004).
  - Provider fees, payouts and custody stay in payments' own records.
- **When an entry is posted:**
  - only from a live outcome that moved money and succeeded: a sale, a capture or a refund;
  - authorizations, and pending or unknown outcomes, post nothing;
  - a later failure or reversal posts a reversing entry.
- **What each entry carries:**
  - the outcome id;
  - the provider's reference;
  - the level of evidence;
  - the custodian.

  A provider is named as custodian only on the provider's own record.
- **Posting once:**
  - the posting key comes from the source (the outcome id, or the provider's reference, with the type of entry), and it never expires;
  - a second posting with the same key and different content is refused, and raised for review;
  - entries are never edited, and a mistake is corrected by a reversing entry.
- **How amounts are summed:**
  - per seller, counterparty, custodian and currency;
  - never netted across counterparties or custodians, and never added across currencies.
- **Currencies:**
  - the ledger converts nothing;
  - where a custodian converts money and reports it, both amounts and the custodian's rate are recorded as reported;
  - amounts are kept in the currency's minor units, as the currency foundation defines them (S-04);
  - a provider's amounts are recorded exactly as reported, never recomputed, and never passed through floating point. Active Merchant also works in integer minor units (AM `README.md`:59; `lib/active_merchant/billing/gateway.rb`:263).

## Consequences

- **Reconciliation:** payments reconciles its records with each provider's reports. A seller's statement joins the seller ledger and payments' records through the reference of the amount owed, the attempt id, the outcome id and the provider reference (D-002).
- **Cash a courier holds** stays apart from money a provider holds, because sums are kept per custodian. No market needs naming for this.
- **If A or B is built later** (D-001), its holding balances sit in payments' settlement ledger, and the seller ledger is unchanged.
- **Store credit a seller owes a buyer** is set aside to subject S-05 (area A-32), under the guard on money.

## The guard

- **Outcome type: Built,** the same in every market.
- **The Q7 draft proposed** to "keep cash collected on delivery apart from electronic amounts in the seller ledger" (`studies/proposals/drafts/Q7/draft.md`:129). The guard script flags that line (`python3 -I method/decision_status.py --guard studies/proposals/drafts/Q7/draft.md`).
  - It isn't adopted here. Keeping sums per custodian answers the same need without naming a market.
  - Whether cash and electronic amounts of one currency differ is a question for S-04.

## Evidence

- E031, E032, E034 and E035, in `evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv`: Shopify's idempotency, for payments-app requests and for creating refunds.
- E040, Active Merchant, pinned at commit `ca45b1b`.
- The seam's rule 19, and where it places the ledgers (seam.md:49, 156–157, 163).

## Confirmation

**Scenarios:**
- a sale, its fee and a partial refund, each posted twice by mistake, give one set of entries;
- a provider's corrected report line with the same key is refused and raised;
- a seller's statement reconciles with payments' records through the identifiers.

**The change scenario:** with the first market dropped, nothing changes.

**Checks:** level 2. The independent review is in `decisions/checks/D-002-D-003-review.md`, with what was done about each finding in `decisions/checks/D-002-D-003-dispositions.md`.
