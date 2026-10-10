# The payment seam

**Question** (item 1 in `NEXT.md`). Can payments be its own part of Sharrwah, with its own questions, research, regulation, consultations and pace, while the rest of the platform depends only on a narrow, stable contract?

**Answer.** Yes, if the line is drawn in the right place. Two things make that possible:

1. **A hard boundary around the rails.** The rails are wallets, banks, couriers' cash, licences, partners and the provider protocols. Everything specific to a rail or a regulator lives behind it and can change on its own schedule.
2. **A narrow, typed contract for the order side.** This covers what the order needs from payments: which methods are on offer, an attempt, the outcomes posted to the order, refunds, and verdicts. These records belong to Sharrwah's commerce model, and the rest of the platform is built against them.

What is owed, when it falls due, and how much is still unpaid are not payments. They are part of the order, and payments only reads them.

## How the answer was reached

| Source | What it shows |
| --- | --- |
| Shopify engineering: 40 sources, `notes/shopify-engineering.md`, captured in `evidence/shopify-engineering/` | Shopify's hard payment boundary follows card-data risk (PCI scope), not team lines. Card data goes to separate services and comes back as a token. Processors sit behind an adapter library, and every attempt carries one idempotency key, with reconciliation as the backstop. Checkout, orders and refunds stay in the monolith (E001–E004, E019). The detailed internal write-ups date from 2019–2022, so they show how Shopify was built then. |
| Shopify product evidence: 178 crossings, `notes/shopify-crossings.tsv` and `.md` | The provider contract is narrow: one query and 16 mutations, with no order id and no line items. The whole payments capability is wide, but its 142 generic crossings pass through eight records. The other 36 exist only because Shopify is also the processor, wallet, lender and biller. |
| Salla: 81 crossings, `notes/salla-crossings.tsv` and `.md` | The seam is wider: deciding which methods to offer reads a lot of core data, and the merchant's balance doubles as a debit rail. Even so, the generic half fits about five messages. The width comes from Salla holding the money, not from commerce itself. |

**Rule for comparing the platforms.** Where Shopify and Salla cross the seam the same way, the crossing is treated as essential to commerce. Where they differ, the crossing is a choice for Sharrwah, listed below. Crossings that neither platform has come from the Yemen evidence. Those have no platform example, so they carry the most risk.

## The contract, version 0

Directions: **core → payments** means core asks payments; **payments → core** means payments tells core; **payments ↔ core** means payments asks core.

| # | Element | What crosses | Direction | Shopify | Salla | Sharrwah and Yemen notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Offer** | For one obligation, core passes a fixed snapshot of context: amount with currency and rial edition, buyer and seller zone, delivery method, a cart summary and the channel. Payments returns the methods on offer, each with display data and its capability profile. | core → payments | S001, S008–S012 | L001, L002, L007–L011 | Payments never reads live core data while deciding; it works from the snapshot. Partner cut-offs per setup option and zone are applied inside payments, so the offer simply changes. |
| 2 | **Attempt** | Start an attempt: attempt id (also the idempotency key), obligation reference and amount. Payments returns coarse states: in progress, buyer action needed, pending, succeeded, failed, unknown. | core → payments, then payments → core | S030–S032 | L004–L006 | The buyer's own steps, such as an OTP, PIN, voucher code or proof upload, happen inside a payments-owned checkout step. Core sees only the state. A pending or unknown state can last a long time, because Yemeni rails have no callbacks and payments has to poll them. |
| 3 | **Outcome record** | A record posted to the order. It carries the kind (sale, authorisation, capture, refund or void), the status and the amount with its edition. It also carries the **outcome source and evidence level**: rail confirmation, rail status query, courier event, seller attestation or buyer claim. It names the custodian (who holds the money now) and the method. It ends with an opaque provider reference and the time. | payments → core | S049, S050, S051 | L017, L018, L042 | Core derives the order's payment status and the amount still owed from these records. Shopify's "mark as paid" and Salla's "under review" bank transfer are precedents for evidence levels; Yemen needs them stated outright. |
| 4 | **Reverse money** | Requests to refund, void or capture, each with its outcome. Where a rail cannot reverse, the outcome is "manual reversal required", and the seller's attestation that they paid back closes it. | core → payments, then payments → core | Refunds S094–S105; capture S066–S070 | L031, L043–L047 | Returns and cancellations stay in core; the movement of money stays in payments. |
| 5 | **Verdicts** | Risk holds, payments under review, and dispute status. Only the verdict crosses; core decides what it does to fulfilment. | payments → core | S045, S046, S075, S109 | L008, L076 | — |
| 6 | **Capabilities** | What each method or setup can do: hold then capture, refund through an API, partial refund, status query, buyer action type, evidence level, currencies, editions and zones. | payments → core, read by core | S005; leaks in `notes/shopify-crossings.md` §5 | — | Core asks "can this payment do X?" and never names a wallet or bank. That stops the leaks Shopify shows, such as instalment orders that can't be edited, or upsells refused for some methods. |
| 7 | **Context reads** | A check that stock and price are still valid just before the debit. Delivery events: delivered, and cash collected or refused at the door. Fulfilment and tracking evidence for disputes. | payments ↔ core | S040, S076, S134 (7 such crossings in total) | L007, L043, and about 25 such crossings in total | These are the reverse dependencies. They stay few and typed, and in Yemen the cash-on-delivery outcome comes in through this path. |

**Owned by core, which the contract relies on.** Obligations: what was agreed and what is due. Terms and schedules. The amount still owed. Order states. Shopify (S051, S089) and Salla ("Partially paid") both keep these on the order.

**Reserved, not built.**
- **Stored permissions to charge later** (mandates, Shopify S086, S090, S120, S128, S129). Neither card networks nor wallets in Yemen support them today.
- **The settlement contract:** holding, netting, payouts and balance debits (Salla L028–L039; Shopify's own processor side). It is needed only when a payment setup's position involves holding or settling funds. That happens with a licensed partner settling per order (stage 2), or with Sharrwah's own reserved holder position, which needs a licence.

## What stays inside payments

Agreed by both platforms, plus Yemen. Details are in the two crossing notes, section (a).

- **Provider accounts:** credentials, onboarding state, and the seller's receiving profile (wallet numbers, accounts, Hasib points).
- **Provider protocols:** session and state machines, buyer-secret steps, status polling, retries and timeouts, and provider references.
- **Fees,** and tax on fees.
- **Settlement and payout ledgers.** Custody ledgers, such as cash held by couriers and sellers.
- **Risk models,** dispute mechanics, and identity checks for the rails.
- **Partner relationships, licences, and Sharrwah's position on each payment setup.**
- **Which partners are available,** per setup option and zone. This is the operational switch for overnight cut-offs.
- **Testing:** simulated outcomes.

## Shared foundations: not payments, settled early

Agreed by both platforms (section (b) in each crossing note):

- **Money and currency:** money with its currency and rial edition, minor units and rounding.
- **Exchange-rate policy,** and the rate service.
- **Zones and markets.**
- **Parties:** customers, merchants and legal sellers, staff and permissions.
- **Tax.**
- **Catalogue facts.**
- **Shipping and delivery.**
- **Platform services:** notifications, the app and event platform, time and calendars, and the test-mode flag.

## Where Shopify and Salla differ: Sharrwah's choices

These defaults are proposals. In the frame's terms, each is a Built decision with provisional certainty, until a decision record settles it.

| Question | Shopify | Salla | Proposed default for Sharrwah |
| --- | --- | --- | --- |
| Who owns the buyer's payment step? | Inside checkout, with provider redirects or on-site steps | Headless checkout hands over to Salla's hosted checkout (L003) | A payments-owned step inside Sharrwah's checkout. Core sees states only. |
| How much does deciding the offer read from core? | Functions over the cart context (S011) | Wide live reads: cart, products, customer, market, delivery, plan (L007–L011) | A fixed snapshot passed in (contract element 1). No live reads. |
| How is a bank transfer confirmed? | Manual method, then "mark as paid" | Native "under review" state with a receipt | A native review state with an explicit evidence level. This matches Yemeni practice: transfer, screenshot, seller check. |
| Stored payment permissions and subscriptions | Rich | Early (a recurring Apple Pay flag) | Reserved |
| Payment terms and deposits | Rich (B2B net terms, deposits) | A deferred-payment window | Minimal: a due date, plus payment on delivery |
| The balance as a debit rail | Yes, for Shopify Payments | Yes | Left out of the contract. Only the settlement contract would need it. |

## Yemen-specific crossings, with no platform example

These carry the most risk and should be the engineer's first review.

1. **Evidence levels on every outcome:** buyer claim, seller attestation, courier event, rail status query, rail confirmation. This is contract element 3.
2. **Long pending and unknown states, with the platform polling the rail.** Shopify never polls (Shopify note, section 6, item 10). The polling stays inside payments, but the contract has to tolerate long pending.
3. **Courier cash custody.** Delivery and refusal events reach payments through element 7, and the custody ledger stays inside payments.
4. **Zone and rial edition** in the offer context and on every amount. This comes from the shared foundations.
5. **Manual reversal on rails that cannot refund** (element 4).

## What this unlocks

- **The core can be built now against this contract.** That covers catalogue, cart, checkout apart from the inside of the payment step, orders, fulfilment, returns, customers, merchants and notifications.
- **Payments for the Sana'a launch can be small.** It means record-only cash on delivery and transfer-with-proof, with outcomes from seller attestation and buyer claims, and no rail integrated. It implements the same contract.
- **Rails come later, behind the same contract.** Wallets, banks and partners plug in without changing core. Regulation, legal consultation and partner talks run in parallel.

## Limits

- **Documents, not live payments.** Every crossing comes from documents, schemas and captured admin screens. None comes from watching a payment run end to end.
- **Shopify's internal architecture evidence is historical.** It dates from before 2023.
- **Salla's help-centre article bodies were fetched live on 2026-10-10.**
- **Neither crossing map is exhaustive.** Each lists the crossings it suspected but could not show.

## Rules added after tagging

Two taggers tagged the 81 rows independently from the first version of this file. They agreed on 78 primary tags and flagged the same gaps on 21 rows. The rules below fill those gaps, and the final tags apply them.

**Parties, roles and the company**
1. **Money roles.** Roles such as merchant of record, custodian, processor and cash collector are attributes of a payment setup, so they stay inside payments. The parties who fill them are a foundation. The outcome record names the custodian (element 3).
2. **Seller verification and sanctions screening.** Sharrwah's own screening and verification of sellers, owners and partners is a foundation, because it gates selling and payments alike. Identity checks a rail requires stay inside payments and read the verified identity from the foundation.
3. **Company-level questions are outside the seam.** Sharrwah's legal entity, domicile and sanctions posture bind both sides. They take the tag **company**, and in the frame they are step 0 for the founder.

**Obligations and the order**
4. **Order states belong to core.** Core owns them and the contract relies on them (element 0). They are not a foundation.
5. **Obligations outside the buyer–seller order are core obligations too.**
   - This covers store credit owed by a seller and Sharrwah's own bills to sellers. They use the same agreed-and-due structure, and they become payments only when money moves, through elements 1 to 4.
   - When Sharrwah bills a seller, Sharrwah is simply the payee.
   - Store value usable across sellers counts as e-money. It is held back as a company decision (PAY-57).
6. **Deadlines have two owners.**
   - The attempt timeout (provider session, voucher validity) stays inside payments. It reaches core as an expired or failed attempt (element 2).
   - The deadline for an unpaid obligation, and what happens when it passes (cancel, release stock, notify), is a core term on core's own clock.
7. **Purchase options that charge later** (pre-order, instalments, subscriptions) are core terms (element 0).
   - Charging later needs either the buyer to pay again, or a stored permission (reserved).
   - Lender-funded instalments are a rail inside payments.

**Offering methods**
8. **Who customises the offer.**
   - Payments decides which methods the buyer may use, and it enforces the platform minimum and zone availability (element 1).
   - The seller's presentation rules (hide, reorder, rename, default) are seller settings that core's checkout applies to the returned list.
9. **Methods published to outside surfaces** (marketplaces, buyer apps, agents) form an offer with no obligation attached. That offer is element 1. Credentials bound to an obligation are element 2.

**Attempts and outcomes**
10. **Split tender.**
    - Core splits one obligation across several attempts, because it owns what is owed.
    - Payments runs each attempt, and the limit on each method comes from its capabilities (element 6).
    - When a part fails, core decides whether to void the completed parts, through element 4.
11. **When an attempt makes an order.** The order is created when the attempt succeeds, or when it is accepted as pending and the method's capabilities allow an order before payment, as with cash on delivery or transfer-with-proof. Rejection and pending reasons cross as a closed set of categories (element 2).
12. **Capture policy.**
    - When held funds are taken is a seller setting held by core.
    - Core sends the capture request (element 4) at the right moment.
    - If a method cannot hold funds (element 6), core falls back to an immediate sale.
13. **Differences between agreed, moved and settled amounts** are recorded as new outcome records (element 3), never as edits. Settlement differences stay inside payments.

**Refunds and blocks**
14. **Refund plans.**
    - Core decides the refund plan: the amount, the destination (original method, store credit or cash) and which outcomes it draws on.
    - Payments enforces the ceiling on each outcome and executes the refund.
    - Going over a ceiling needs a core staff permission. It is carried out as a manual reversal.
15. **Blocks on money actions.**
    - Core enforces business blocks that come from order states, by not making the request.
    - Payments refuses anything its own capabilities or states do not allow.
16. **Complaints and disputes.** A buyer's complaint to Sharrwah is core customer service. If it becomes a dispute with a rail or partner, the mechanics stay inside payments and the status crosses as a verdict (element 5).

**Shared mechanisms and per-market values**
17. **Reconciliation.**
    - Reconciling outcomes against rails, partners and custodians stays inside payments.
    - Sellers' reconciliation reports combine core and payments data through the identifiers that cross: obligation reference, attempt id, outcome id and provider reference.
18. **Per-market values have one owner each.**
    - Zones and markets are a foundation.
    - Payment values per market, such as methods enabled and partner availability, stay inside payments.
    - Other values per market, such as rial edition, rate policy, civil calendar and tax, are foundations.
    - Rail cut-offs and settlement calendars stay inside payments and build on the civil calendar.
19. **The ledger pattern is shared.** Append-only entries, idempotent posting, and reversal instead of edit form a shared foundation used by core's order money and payments' custody and settlement ledgers. Each ledger's content belongs to its owner.
20. **Tax on Sharrwah's own revenue** belongs to the tax foundation. Tax on rail fees stays inside payments.

**Housekeeping**
21. **Reserved parts** (stored permissions, the settlement contract) take the tag contract with element **R**.
22. **Rows that inform several parts.** A field-research row takes as its primary tag the part whose design its answer changes most; the others go in `also`.

## Tagging the 81 register rows

Each row gets one tag:

- **contract:** its answer defines an element above;
- **payments-internal:** its answer stays inside payments;
- **core:** commerce outside payments;
- **foundation:** a shared foundation.
- **company:** outside the seam, binding both sides (rule 3).

Two taggers worked independently from the first version of this file. `rows-tagged.tsv` gives both taggers' tags, the final tag and the rule applied wherever the final tag differs from theirs.

**Result.**

| Tag | Rows | What it means for the order of work |
| --- | --- | --- |
| contract | 24: element 0 ×7, 1 ×3, 2 ×3, 3 ×4, 4 ×2, 6 ×3, 7 ×1, reserved ×1 | Settle early. Most are answerable from the Shopify and Salla evidence already held. The Yemen-specific ones are PAY-49, PAY-75 and PAY-76. |
| foundation | 13: PAY-01, 22, 34, 38, 40, 41, 43, 48, 61, 62, 73, 74, 81 | Settle early. These cover money with its rial edition, rates, zones, calendars, verification, the ledger pattern and tax. |
| payments-internal | 42 | These move at their own pace: rails, partners, licences, custody, regulation and consultations. Nothing in core waits for them. |
| core | 1: PAY-23 | — |
| company | 1: PAY-44 | Step 0, for the founder. |

How the taggers agreed: they matched on 78 of 81 primary tags. The three disagreements were PAY-16, PAY-44 and PAY-61; each had low confidence from at least one tagger, and rules 6, 3 and 2 settle them. Five tags both taggers agreed on were changed by the new rules: PAY-06, PAY-11, PAY-15, PAY-34 and PAY-41.
