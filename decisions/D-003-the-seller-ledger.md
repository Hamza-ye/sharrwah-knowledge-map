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
depends_on: D-001 D-002
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

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| seller ledger | The order side's record of what each seller is owed and owes. It holds no money | This record; `GQL:3197` (nearest) |
| order side | The parts of Sharrwah that deal with what a buyer owes, as a whole | D-002; `GQL:2306` (nearest) |
| payments side | The part behind the payment boundary, which keeps custody, payouts and provider fees | D-002 |
| outcome record | D-002's results; only live sales, captures and refunds that succeeded post here | D-002; `GQL:2447`; `GQL:2452` |
| custodian | Who holds a payment's money now; sums are kept per custodian | D-002; `GQL:318`; `SA-en:1240` |
| posting key | The outcome id, or the provider's reference, with the entry's type; it never expires | This record; E032:198; E031:277 |
| live and test | Only live outcomes post | `GQL:2447` |
| provider fees | Kept in payments' records, not in this ledger | `GQL:3605`; `SA-en:24` |
| Sharrwah's fees | Amounts the seller owes Sharrwah, billed apart | D-004; `HC:payments/getting-paid.md:11` (a precedent) |
| settlement and payout | Kept in payments' records, not in this ledger | `GQL:3223`; `SA-en:807` |
| stored value | Set aside to S-05; not money held | `GQL:3283`; `SA-en:36` |

## Scope

**Decides:**
- Two ledgers, one per owner. This record decides the order side's, the seller ledger: what it records, when it posts, what each entry carries, posting once, how sums are kept, and that it converts nothing.

**Takes as given:**
- D-001's outcome, that Sharrwah holds no sellers' money, and D-002's outcome records and identifiers (both in `depends_on`).
- The founder's guard of 18 October (`founder-decisions.tsv`, G1).

**Leaves open:**
- How currencies, minor units and rounding are defined — S-04. Carried: amounts are kept in minor units as S-04 defines them, and never converted.
- Gift cards, store credit and customer wallets — S-05. Carried: the ledger's rules hold for any entry. Recording store credit would add a type of entry, or it would live in S-05's own record.
- How Sharrwah's fees are set and billed — S-03. Carried: whatever they are, they post as amounts the seller owes Sharrwah.
- Where the ledger sits among the order side's modules — S-05. Carried: its rules don't depend on where it sits.
- Payments' own records of custody, payouts and provider fees, and reconciliation with providers — S-07. Carried: they stay in payments, joined to this ledger by the identifiers that cross the boundary (D-002).
- Sellers' statements and reports — S-12. Carried: they read this ledger and payments' records.

## Decision drivers

- It must not become a balance Sharrwah holds (D-001; the founder's guard of 18 October).
- **Money records edited in place lose their history and break reconciliation.** Shopify's ledger for its payment service records reversals as entries of their own: of its 114 types of balance transaction, 38 are reversals, and 36 of those are named as the reversal of another type (`GQL:3240`, counted by script). *Corrected 24 October:* this record used to say, after the seam's note, that every type has "a reversal twin" (shopify-crossings.md:141). The schema doesn't support that. Shopify's payments-app ids are idempotency keys that don't expire (E032:198; E031:277). Its Admin API keys expire after 24 hours (E034:109, 137).
- **The seam's rule 19** proposed one ledger pattern for both sides: "Append-only entries, idempotent posting, and reversal instead of edit form a shared foundation used by core's order money and payments' custody and settlement ledgers. Each ledger's content belongs to its owner." (seam.md:163). This record takes it up as option 4, on the evidence in these drivers, not on the seam's authority.
- **Shopify keeps its ledger, payouts and processing fees inside its payment service.** A balance transaction "Includes the gross amount, processing fees, and resulting net amount that affects the account balance." (`GQL:3197`), and a payout is "A transfer of funds between a merchant's Shopify Payments balance and their" bank account (`GQL:3223`). The seam's contract placed settlement, payout and custody ledgers, and reconciliation, inside payments too (seam.md:49, 156). That is an option this record takes up, not evidence.

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
  - Other types of entry can be added with the features that need them, under the same rules.
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
- **Store credit a seller owes a buyer** is set aside to subject S-05 (area A-32). It is value the seller owes, not money held, so the guard on money doesn't reach it (glossary, *stored value*). *Corrected 24 October:* this record used to place it "under the guard on money".

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

**Gaps:**
- **It depends on D-002,** which stays proposed until the first providers are walked through it. This record is accepted no earlier than D-002 (`depends_on`).
- **How a provider reports a corrected line:** whether with the same reference, a new one, or a reversal. The work: read it in the first providers' documented interfaces, in the same walkthrough as D-002.
