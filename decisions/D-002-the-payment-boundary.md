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

It starts from the payment seam's contract, version 0 (`8946887:studies/payment-seam/seam.md`), written on 10 October with the founder's F-06: payments as their own concern. This record is that contract after the market guard. It answers the Knowledge Map's KM-PAY-01 (how a payment method plugs in), and KM-PAY-02 (payment states, and how they drive the order's payment status).

## Context and problem statement

D-001 builds C: each provider holds the money in the seller's own account. A and B stay reserved. Payments must be able to change on their own schedule as providers, licences and markets change, while the rest of the platform depends on something narrow and stable. Where should the line be drawn, and what crosses it?

## Decision drivers

- A and B can be added later behind the line, without changing the order side (D-001).
- Providers and their protocols change often. The order, its states, and what is owed change rarely.
- The references draw a narrow line:
  - Shopify's contract for payment providers is a payments app with its own requests and states (E030 to E032);
  - its transactions have set kinds and statuses (E033);
  - its money-moving requests carry idempotency keys (E034, E035);
  - payment methods are customized through a function (E036);
  - in Active Merchant, processors sit behind one adapter interface (E040).
- The market guard: nothing on the order side names a market, a currency's local variant, a wallet or a bank.

## Considered options

1. **A narrow typed contract.** Seven elements cross it, and everything specific to a provider stays behind it. This is the seam's contract v0.
2. **The order side calls each provider directly.** This is simpler at first, but every new provider changes the order side. Shopify's experience is the leaks it lists, such as installment orders that can't be edited.
3. **A generic plug-in point with no fixed contract.** Flexible, but nothing stable to build the order side against.

## Decision outcome

Chosen option: **1, a narrow typed contract.** The order side and payments meet only through seven elements:

1. **Offer.** For one amount owed, the order side passes a fixed snapshot: the amount with its currency, the buyer's and the seller's market, the delivery method, a cart summary and the channel. Payments returns the methods on offer, each with display data and its capabilities. Payments never reads live order data while deciding.
2. **Attempt.** The order side starts an attempt with an attempt id, which is also the idempotency key, and the amount. Payments answers with coarse states: in progress, buyer action needed, pending, succeeded, failed or unknown. A pending or unknown state may last a long time. How payments learns the result, by callback or by asking the provider, stays inside payments.
3. **Outcome record.** Posted to the order. It carries:
   - its kind (sale, authorization, capture, refund or void), its status, and the amount with its currency;
   - its source and level of evidence: provider confirmation, provider status query, courier event, seller attestation or buyer claim;
   - the custodian, meaning who holds the money now;
   - the method, an opaque provider reference, and the time.

   The order's payment status and the amount still owed are derived from these records.
4. **Reverse money.** Requests to refund, void or capture, each with its outcome. Where a provider can't reverse, the outcome is "manual reversal required", and the seller's attestation that they paid back closes it.
5. **Verdicts.** Risk holds, payments under review, and dispute status. Only the verdict crosses; the order side decides what it does to fulfilment.
6. **Capabilities.** What each method can do: hold and capture later, refund by API, partial refund, status query, the type of buyer action, the level of evidence, and the currencies and markets it serves. The order side asks "can this payment do X?" and never names a provider.
7. **Context reads.** A few typed calls from payments to the order side:
   - a check that stock and price are still valid before the debit;
   - delivery events, including cash collected or refused at the door;
   - fulfilment evidence for disputes.

**The order side owns** what was agreed and is due, the terms and schedules, the amount still owed, and the order's states. Payments only reads them.

**Payments owns:**
- provider accounts and onboarding;
- provider protocols, including buyer steps such as one-time codes;
- fees;
- the risk models;
- which providers are available, as a switch per market;
- simulated outcomes for testing.

**Reserved, not built:**
- stored permissions to charge later;
- the settlement contract: holding, netting, payouts and balance debits. It is needed only for A or B (D-001).

## Consequences

- A new provider, a new method, or a provider cut off overnight changes only what is behind the boundary.
- Seller and buyer amounts carry a currency and nothing more on the order side. How a provider's own variants of a currency are handled stays behind the boundary (subject S-04).
- Cash on delivery fits as a method whose outcome comes from a courier event, and whose evidence level is set by its source.
- Changing an element later is costly, so each element is reviewed when the first two providers are integrated.

## The guard

- **Outcome type: Built,** the same in every market.
- **Changes from the seam's contract v0:**
  - Its "edition" of a currency, on the offer and on every amount, is removed. G1's B7 says "The rial's two editions are not part of the core".
  - Its column of notes for the first market is not part of this decision.
- **General mechanisms kept, each with a precedent:**
  - **Long-pending payments.** Shopify's manual payment methods, and Salla's bank transfer "under review" (seam, element 3).
  - **Evidence levels.** Shopify's "mark as paid".
  - **A courier holding cash.** Salla's cash-on-delivery remittances with its carriers, and Shopify's cash sessions at the point of sale (seam, "Crossings first met in Yemen").

## Evidence

- **Shopify's engineering and developer sources:**
  - E030 to E036 in `evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv`, fetched on 10 October 2026: payments extensions, payments apps and their requests, transaction kinds and statuses, idempotency, and the Payment Customization Function;
  - E040: Active Merchant's gateway base class, pinned at a commit.
- **The seam study's crossings:**
  - 178 for Shopify (`8946887:studies/payment-seam/notes/shopify-crossings.tsv`) and 81 for Salla (`…/salla-crossings.tsv`);
  - its finding: Shopify's provider contract is "one query and 16 mutations, with no order id and no line items", and Salla's seam is wider because "Salla holding the money" (`8946887:studies/payment-seam/seam.md`, "How the answer was reached").

## Confirmation

- **Scenarios:**
  - a wallet payment with a one-time code;
  - cash on delivery with refusal at the door;
  - a refund on a method that can't reverse.

  Each is answered from the seven elements alone.
- **The change scenario.** A second market whose processor holds the funds adds B behind the boundary, with no change to the elements.
- **Checks:** level 2. A script checks the quotes of the facts it rests on; the coordinator checks their conditions; one independent agent reviews the record.
- **Review** when the first two providers are integrated.
