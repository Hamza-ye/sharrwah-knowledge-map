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
depends_on: D-001
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

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| order side | The parts of Sharrwah that deal with what a buyer owes and why, as a whole; how they divide is S-05's | `GQL:2306` (nearest) |
| payments side | The part behind the boundary, called "payments" here; F-06's concern of its own | `founder-decisions.tsv` (F-06); `CLI:70`–`CLI:75`; E030 to E032 |
| payment boundary | The line between the two, and the seven elements that cross it | This record |
| payment method | Kinds 1 and 2 of the glossary. Stored value is S-05's (Leaves open) | `HC:payments.md:3`; `SA-en:807`; `GQL:1672`; `SA-en:1066` |
| payment provider | The company that processes or receives a payment for a method | `HC:payments/getting-paid.md:3`; `SA-en:24` |
| manual payment method | A method whose outcome comes from a seller attestation or a courier event | `HC:payments/manual-payments.md:5`; `SA-en:565` |
| cash on delivery | A method whose capabilities allow an order before payment, with a courier event as its outcome | `SA-en:565`; `SA-en:570` |
| amount owed | One amount a buyer owes, with its reference | `GQL:2306`; `SAPI:5` |
| attempt | One try to pay an amount owed, its id the idempotency key, with seven coarse states | `GQL:2453`; `GQL:2450` |
| outcome record | A result posted to the order, of five kinds; Shopify's CHANGE, EMV_AUTHORIZATION and SUGGESTED_REFUND are left out | `GQL:2447`; `GQL:2452` |
| authorization and capture | Outcome kinds, and the capability to hold and capture later. When to capture is S-07's | `HC:payments/payment-authorization.md:11`; `GQL:2452` |
| refund and void | Outcomes that draw on an earlier one, requested through element 4 | `HC:fulfillment/managing-orders/refunding-orders.md:16`; `SA-en:804`; `SAPI:211` |
| manual reversal | A refund made outside the provider, closed by the seller's attestation | `HC:payments/shopify-payments/refunds-troubleshooting.md:91`; `SA-en:994` |
| custodian | Who holds a payment's money now: a provider, a courier or the seller | `GQL:318`; `SA-en:1240`; `SA-en:277` |
| evidence level | Provider's record, courier event, seller attestation or buyer claim | `HC:fulfillment/managing-orders/payments/deferred-payments.md:129`; `GQL:2447`; `SAPI:5`; `SSTAT:3` |
| capability | What a method can do; the list grows with the features that ask | `GQL:2447`; `GQL:2306` |
| verdict | A risk hold, a payment under review, or a dispute's status | `GQL:2306`; `GQL:3209`; `GQL:1441` |
| rules on payment methods | Only rules that hide, reorder or rename methods, applied by the order side's checkout | `HC:checkout-settings/checkout-customization.md:73`; `SA-en:923` |
| payment terms | Only as a capability: an order placed before payment, by a due date the order side sets | `HC:fulfillment/managing-orders/payments/deferred-payments.md:7`; `GQL:2514` |
| provider fees | What providers and couriers charge for payments, recorded as reported. Not Sharrwah's fees | `HC:payments/shopify-payments/payouts/pay-periods-and-fees.md:7`; `GQL:3605`; `SA-en:24` |
| settlement and payout | Payments' records of them; under C, each provider's own | `GQL:3229`; `SA-en:807` |
| live and test | Whether an outcome moved real money | `GQL:2447` |
| reserved, not built | The settlement contract, and stored permissions to charge later | This record; D-001 |

## Scope

**Decides:**
- Payments sits behind a boundary of its own, and the order side and payments meet only through the seven elements.
- What each side owns, as listed under the outcome.
- The order's payment status and the amount still owed are derived from outcome records.
- Every amount carries its currency, and where the amount agreed and the amount charged or settled differ in currency, the record carries both, with the rate.
- How the boundary grows: elements fixed, vocabularies growing with the features that need them.
- Stored permissions to charge later, and the settlement contract, are reserved, not built.

**Takes as given:**
- D-001's outcome: C at launch, with A and B reserved (in `depends_on`).
- F-06, payments as a concern of their own (`founder-decisions.tsv`).
- G1's B7, that the rial's two editions are not part of the core (`founder-messages/2026-10-18-g1-answer.md`), and the market guard (`METHOD.md` section 3a).

**Leaves open:**
- The interfaces of the providers Sharrwah will integrate — S-07. Not carried: the elements were drawn from Shopify's and Salla's own provider contracts, and haven't been walked through a provider Sharrwah would integrate. The first providers may need an element changed. This record stays proposed until S-07 walks them through it (Gaps).
- Gift cards, store credit and customer wallets at checkout — S-05. Carried: if S-05 makes them methods behind the boundary, their outcomes add values to the vocabularies, an evidence level and a custodian for value the seller owes. If it applies them on the order side, as Salla applies a gift card as a coupon, nothing here changes.
- Which methods and providers are offered, manual methods included — S-07. Carried: each plugs in behind the boundary, and a manual method's outcome comes from a seller attestation or a courier event.
- When a payment is captured: at checkout, on fulfilment, per fulfilment, or by hand — S-07. Carried: a capture is a request naming its authorization (element 4), sent when the seller's setting says. Capturing in parts adds a capability, with the feature that asks for it.
- Seller rules that reject a payment or hold an order for review, and whether apps supply rules — S-07, with S-06 for apps. Carried: a rule applied before an attempt is the order side's, which holds the order in its own states or doesn't start the attempt. A rule applied by payments crosses as a rejection category or a verdict.
- The order's payment statuses, and the rules of refunds, returns, edits and cancellations (area A-09) — S-05. Carried: statuses are derived from outcome records whatever their names, and refunds and voids are element 4's requests.
- How the order side divides into modules — S-05. Carried: the boundary is between the order side as a whole and payments, and how the order side divides doesn't touch the elements.
- Payment terms and invoices paid later for business buyers (area A-23) — S-11. Carried: an order placed before payment, with a due date the order side sets, is a capability.
- Selling in person, with cash at the counter or card readers — S-10. Carried: an in-person result is an outcome record naming its custodian. Kinds such as Shopify's CHANGE or EMV_AUTHORIZATION would be values added to a vocabulary.
- Currencies, their minor units and conversion — S-04. Carried: every amount carries its currency as S-04 defines it.

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

Option 1 wins on long-pending and asynchronous outcomes, and on keeping providers out of the order side. Shopify's own order transactions carry what a payment can do, `manuallyCapturable` and `multiCapturable` (`GQL:2447`), and its failure codes are "A standardized error code, independent of the payment provider." (`GQL:2450`). So the order side can ask about capabilities and categories instead of naming providers, which option 2 can't. *The seam's reading,* that some of Shopify's core features check which arrangement was used (shopify-crossings.md:221–228), points the same way. It isn't relied on, because its sources weren't traced.

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

   The order side asks "can this payment do X?" and never names a provider. The list grows when a method can do something the order side gains a feature to ask about.
7. **Context reads.** A few typed calls from payments to the order side:
   - a check that stock and price are still valid before the debit;
   - delivery events, including cash collected or refused at the door;
   - fulfilment evidence for disputes.

**Amounts.** Every amount carries its currency, as the money and currency foundation defines it (subject S-04). Where the amount agreed and the amount charged or settled are in different currencies, the record carries both, with the rate used. Shopify's amounts are "A collection of monetary values in their respective currencies." (`GQL:2263`), in the shop's and the customer's currency. Salla's order carries an exchange rate, with its "Order Exchange Currency" (`SDS:85`).

**How it grows.** The seven elements, and what each side owns, are fixed by this record. The values inside the elements are vocabularies: the states, kinds, reason categories, evidence levels and capabilities. A value is added with the feature that needs it, and an added value never changes what an existing one means.

**The order side owns:**
- what was agreed and what is due, with their terms and schedules;
- the amount still owed;
- the order's states;
- the seller's rules to hide, reorder or rename methods, which its checkout applies.

Payments only reads these.

**Payments owns:**
- provider accounts, onboarding, and the seller's receiving profile;
- provider protocols, including buyer steps such as one-time codes, and status checks;
- provider fees, and tax on them (glossary, *provider fees*). Sharrwah's own fees are not payments' (D-003, D-004);
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

- A new provider, or a provider cut off overnight, changes only what is behind the boundary. So does a new method, unless it can do something the order side doesn't yet ask about. Then the order side gains the feature that asks, and the capability list grows (How it grows).
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
    - on Shopify, "Orders that accept manual payments are marked as unpaid on the **Orders** page." (`HC:payments/manual-payments.md:10`) until the seller marks them paid; on Salla, a bank transfer waits in "بإنتظار المراجعة" (`SSTAT:3`) with the buyer's receipt (`SAPI:5`);
    - Shopify's transactions can be PENDING or UNKNOWN (`GQL:2453`; E033:781–794);
    - a payments app reports results asynchronously (E031:296–298).

    The held sources show providers reporting results to Shopify, and don't show Shopify asking a provider for one. *The seam's reading* agrees (seam.md:86). Polling, if a provider needs it, stays behind the boundary, so only long pending crosses.
  - **Evidence levels,** which the platforms show in part: Shopify's "**Mark as paid** - Use when you've already received payment for the current order" (`HC:fulfillment/managing-orders/payments/deferred-payments.md:129`), and Salla's review state with a receipt (`SSTAT:3`; `SAPI:5`).
  - **Cash held by someone other than a provider:** Shopify's cash drawer, which "Tracks the balance in a cash drawer for a point of sale device over the course of a shift." (`GQL:318`), and Salla's cash-on-delivery ledger with its carriers, with columns for "Carrier" and "Payout details" (`STR:payments.json`).
  - **Manual reversal:** on Shopify, "If the refund can't be completed to the original payment method, then you can resolve the customer outside the original payment method" (`HC:payments/shopify-payments/refunds-troubleshooting.md:91`); on Salla, "Automatic refunds are not supported for cash-on-delivery payments." (`SA-en:994`).

## Evidence

- **Shopify's developer sources:**
  - E030 to E036, in `evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv`, fetched on 10 October 2026: payments extensions, payments apps and their requests, transaction statuses, idempotency, and the Payment Customization Function;
  - E033's kinds of transaction appear only in the finding aid's description.
- **E040:** Active Merchant, pinned at commit `ca45b1b`.
- **The seam study,** a draft of 10 October. This record takes its contract v0 as option 1, and takes no fact from it unless the fact is traced to a held source above. *The seam's own findings,* not relied on: 178 crossings for Shopify and 81 for Salla; Shopify's provider contract is "one query and 16 mutations, with no order id and no line items", while Salla's is wider because of "Salla holding the money" (seam.md, "How the answer was reached").
- **Shopify's and Salla's held structures,** cited by the glossary's short forms (`architecture/12-glossary.md`): the admin schema at observed-sh `febbf6c`, and Salla's help articles, order schema and dashboard strings at observed-sa `4ca2e89`.

## Confirmation

**Scenarios,** each answered from the seven elements alone:
- a wallet payment with a one-time code;
- cash on delivery, with refusal at the door;
- a refund on a method that can't reverse.

**The change scenario:** a second market whose processor holds the funds. It adds B, and the settlement contract beside the seven elements. The elements don't change.

**Checks:** level 2. The independent review is in `decisions/checks/D-002-D-003-review.md`, with what was done about each finding in `decisions/checks/D-002-D-003-dispositions.md`.

**Review** when the first two providers are integrated.

**Gaps:**
- **The elements haven't been walked through a provider Sharrwah would integrate.** The work: walk the first two providers' documented interfaces through the seven elements, on paper. It is needed before this record is accepted, and before S-05 designs the order side against the elements, whichever comes first.
- **Shopify's provider contract** is known here through E030 to E036 and the seam's reading of it. The work: the same walkthrough, with Shopify's payments apps API as one of the two.
