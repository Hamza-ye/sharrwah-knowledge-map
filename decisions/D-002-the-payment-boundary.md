---
id: D-002
title: The payment boundary between the order side and payments
subject: S-01
status: proposed
door: two-way
integrity: 2
outcome: Built
varies_by: —
risks: W-07 R-06
evidence: E030 E031 E032 E033 E034 E035 E036 E040
trigger: —
date: 2026-10-24
---

# The payment boundary between the order side and payments

**Where it starts.** The payment seam's contract, version 0 (`8946887:studies/payment-seam/seam.md`, written on 10 October; below, "seam.md" with its line numbers). It came out of the founder's direction F-06, that payments are a concern of their own (`8946887:decisions/founder.md`; restored in `founder-decisions.tsv`). This record is that contract after the market guard and an independent review (`decisions/checks/D-002-D-003-review.md`).

**What it answers.** KM-PAY-01, how a payment method plugs in, and KM-PAY-02, payment states and how they drive the order's payment status (`register/km-questions.tsv`).

**Its other sources:**
- the seam's two crossing notes, `8946887:studies/payment-seam/notes/shopify-crossings.md` and `…/salla-crossings.md`;
- E030 to E036, in `evidence/shopify-engineering/runs/20261010T083026Z-engineering-sources/`;
- E040, Active Merchant at commit `ca45b1b`, in `evidence/shopify-engineering/runs/20261010T083203Z-repositories/activemerchant__active_merchant/`.

## Context and problem statement

D-001 builds C: each provider holds the money in the seller's own account. A and B stay reserved. Payments must be able to change on their own schedule as providers, licences and markets change, while the rest of the platform depends on something narrow and stable. Where should the line be drawn, and what crosses it?

## Decision drivers

- A and B can be added later without changing the order side (D-001).
- **Providers' interfaces change often:**
  - Shopify's payments-app requests gained fields in API versions 2024-01, 2024-07 and 2024-10 (E032:207, 321, 532);
  - E035 is a breaking change for 2026-04 (E035:24–30).
- **Shopify's contract with payment providers is a payments app:**
  - it sends requests, and the app resolves or rejects them (E030 to E032);
  - results come back asynchronously, with retries for up to 24 hours (E031:296–298);
  - its transactions can be pending or unknown (E033:781–794);
  - the payment, refund, capture and void requests each carry an id used as the idempotency key, and those keys don't expire (E032:198, 867, 952, 1033; E031:277).
- **Its Admin API** makes idempotency mandatory for creating refunds (E034, E035).
- **The seller's rules on payment methods** are applied through a function (E036).
- **The market guard:** no rule or type on the order side refers to a particular market, currency variant, wallet or bank.

## Considered options

1. **A narrow, typed, asynchronous contract.** Seven elements cross it, and everything specific to a provider stays behind it. This is the seam's contract v0.
2. **The order side calls each provider directly.** Simple at first, but every new provider then changes the order side.
3. **One uniform adapter library, called in process.** Active Merchant, "a simple and unified API to access dozens of different payment gateways" (AM `README.md`:5–7), has one base class for purchase, authorize, capture, void, refund and verify (AM `lib/active_merchant/billing/gateway.rb`:9–18). It is simpler than 1, but it is synchronous, and it has no offer, no verdicts and no evidence levels. Shopify's own contract with providers is asynchronous (E031:296).

Option 1 wins on long-pending and asynchronous outcomes, and on keeping providers out of the order side. Shopify's "leaks" support its element 6, the capabilities, not option 2: they are core features checking which arrangement was used, and the remedy the note gives is a capability profile (shopify-crossings.md:221–228).

## Decision outcome

Chosen option: **1.** The order side and payments meet only through seven elements.

1. **Offer.** For one amount owed, the order side passes a fixed snapshot:
   - the amount, in its currency;
   - the buyer's and the seller's market;
   - the delivery method, a cart summary and the channel.

   Payments returns the methods on offer, each with its display data and its capabilities. Payments never reads live order data while deciding.
2. **Attempt.** The order side starts an attempt with:
   - an attempt id, which is also the idempotency key;
   - the reference of the amount owed;
   - the amount.

   Payments answers with coarse states: in progress, buyer action needed, pending, succeeded, failed, expired or unknown. Rejection and pending reasons cross as a closed set of categories.
   - **A pending or unknown state may last a long time.** How payments learns the result, by callback or by asking the provider, stays inside payments.
   - **When an attempt makes an order:** the order is created when the attempt succeeds, or when it is accepted as pending and the method's capabilities allow an order before payment.
3. **Outcome record.** Posted to the order. It carries:
   - its outcome id, and the attempt it belongs to;
   - for a capture, refund or void, the outcome it draws on;
   - its kind (sale, authorization, capture, refund or void), its status, and the amount in its currency;
   - **the source and level of its evidence:** the provider's record, a courier event, a seller attestation or a buyer claim;
   - the custodian, meaning who holds the money now;
   - the method, an opaque provider reference, the time, and whether it is test or live.

   The order's payment status and the amount still owed are derived from these records.
4. **Reverse money.** Requests to refund, void or capture, each naming the outcome it draws on, and each with its outcome. Where a provider can't reverse, the outcome is "manual reversal required", and the seller's attestation that they paid back closes it.
5. **Verdicts.** Risk holds, payments under review, and dispute status. Only the verdict crosses; the order side decides what it does to fulfilment.
6. **Capabilities.** What each method can do:
   - hold and capture later;
   - refund by API, and partial refund;
   - the type of buyer action;
   - the level of evidence its outcomes carry;
   - whether an order may be placed before payment succeeds: paid on delivery, or by a due date the order side sets;
   - the currencies and markets it serves.

   The order side asks "can this payment do X?" and never names a provider.
7. **Context reads.** A few typed calls from payments to the order side:
   - a check that stock and price are still valid before the debit;
   - delivery events, including cash collected or refused at the door;
   - fulfilment evidence for disputes.

**Amounts.** Every amount carries its currency, as the money and currency foundation defines it (subject S-04). Where the amount agreed and the amount charged or settled are in different currencies, the record carries both, with the rate used. Shopify's amounts carry the shop's and the presentment currency (shopify-crossings.md:160). Salla's orders carry exchange rates (salla-crossings.md:77).

**The order side owns:**
- what was agreed and what is due, with their terms and schedules;
- the amount still owed;
- the order's states;
- the seller's rules to hide, reorder or rename methods, which its checkout applies.

Payments only reads these.

**Payments owns:**
- provider accounts, onboarding, and the seller's receiving profile;
- provider protocols, including buyer steps such as one-time codes, and status checks;
- fees, and tax on fees;
- settlement, payout and custody ledgers, including cash held by couriers;
- reconciliation against providers, partners and custodians;
- risk models, dispute mechanics, and identity checks for providers;
- partner relationships, licences, and Sharrwah's position on each payment setup;
- which providers are available, as a switch per market;
- simulated outcomes for testing.

**Reserved, not built:**
- stored permissions to charge later;
- the settlement contract: holding, netting, payouts and balance debits. It is needed only for A or B (D-001).

## Consequences

- A new provider, a new method, or a provider cut off overnight changes only what is behind the boundary.
- Sellers' statements join the order side's data and payments' data through the identifiers that cross: the reference of the amount owed, the attempt id, the outcome id and the provider reference.
- Cash on delivery fits as a method whose capabilities allow an order before payment, and whose outcome comes from a courier event.
- Changing an element later is costly, so the elements are reviewed when the first two providers are integrated.

## The guard

- **Outcome type: Built,** the same in every market.
- **Changes from the seam's contract v0:**
  - **The currency "edition"** on the offer, on every amount and among the capabilities (seam.md:28, 30, 33) is removed. Amounts carry their currency as the money and currency foundation defines it, and S-04 decides that under the guard. The founder's G1 answer says "The rial's two editions are not part of the core" (`founder-messages/2026-10-18-g1-answer.md`, B7).
  - **The "status query" capability is removed,** and "rail confirmation" and "rail status query" become one level of evidence, the provider's record. How payments learns a result stays behind the boundary. Neither reference shows a platform polling a provider (seam.md:86).
  - **Its column of notes for the first market** is adopted only where it is restated without the market: "never reads live order data", partner cut-offs, long pending, the derived payment status, and "never names a provider".
- **Adopted from the seam's rules:**
  - rule 6: a timed-out attempt reaches the order side as expired;
  - rule 8: the seller's rules on methods are applied by the order side's checkout;
  - rule 11: when an attempt makes an order, and closed categories for reasons (seam.md:119–121, 127–129, 137).

  The seam's other rules are taken up when their subject comes up.
- **General mechanisms kept, each with a precedent:**
  - **Long pending:**
    - on Shopify, a bank transfer is a manual method that is then marked as paid; on Salla, it has a native "under review" state with a receipt (seam.md:76);
    - Shopify's transactions can be pending or unknown (E033:781–794);
    - a payments app reports results asynchronously (E031:296–298).

    The seam found no precedent for long pending combined with polling (seam.md:86). Polling stays behind the boundary, so only long pending crosses.
  - **Evidence levels,** which the platforms show in part: Shopify's "mark as paid", and Salla's "under review" with a receipt (seam.md:76, 85).
  - **Cash held by someone other than a provider:** Shopify's cash at the counter (seam.md:87), and Salla's cash-on-delivery remittances with its carriers (salla-crossings.md:60).
  - **Manual reversal:** Shopify records refunds made outside any provider (seam.md:89).

## Evidence

- **Shopify's developer sources:**
  - E030 to E036, in `evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv`, fetched on 10 October 2026: payments extensions, payments apps and their requests, transaction statuses, idempotency, and the Payment Customization Function;
  - E033's kinds of transaction appear only in the finding aid's description.
- **E040:** Active Merchant, pinned at commit `ca45b1b`.
- **The seam study:**
  - its crossings: 178 for Shopify and 81 for Salla;
  - its finding that Shopify's provider contract is "one query and 16 mutations, with no order id and no line items", while Salla's is wider because of "Salla holding the money" (seam.md, "How the answer was reached").

## Confirmation

**Scenarios,** each answered from the seven elements alone:
- a wallet payment with a one-time code;
- cash on delivery, with refusal at the door;
- a refund on a method that can't reverse.

**The change scenario:** a second market whose processor holds the funds. It adds B, and the settlement contract beside the seven elements. The elements don't change.

**Checks:** level 2. The independent review is in `decisions/checks/D-002-D-003-review.md`, with what was done about each finding in `decisions/checks/D-002-D-003-dispositions.md`.

**Review** when the first two providers are integrated.
