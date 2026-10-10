# The payments seam on Shopify: notes for S_crossings.tsv

Sharrwah study, 2026-10-10. The question: can payments be its own part of the system behind a narrow, stable contract, so the rest of the platform can be built independently?

The companion table `S_crossings.tsv` lists 178 crossings between payments and the rest of the Shopify platform. This file gives:

- how to read the table;
- what stays inside payments;
- the foundations both sides share;
- a short summary of how narrow the seam is;
- the crossings I suspect exist but could not evidence.

Statements are facts with a citation unless marked **Inference**.

---

## 1. How to read the table

### Path prefixes in the `evidence` and `notes` columns

| Prefix | Location | What it holds |
|---|---|---|
| `corpus/` | `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/corpus/` | Help Center and shopify.dev pages fetched 2026-10-09 |
| `observed-sh/` | `/home/user/observed-sh/` | Captured structures and derived files (date per row) |
| `study/` | `/home/user/sharrwah-knowledge-map/shopify-payments-study/` | The eight reading passes, 2026-10-10 |
| `live/` | `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/seam_live/` | Local copies of four live pages fetched 2026-10-10 for gaps. The row cites the URL. |

### Columns

- **direction**
  - `core asks payments`: core starts the crossing. It sends a command or a query, or it hands over context.
  - `payments tells core`: payments starts the crossing. It sends an outcome, an event, a status or a constraint.
  - `payments asks core`: payments starts the crossing and needs an answer from core. I added this third value because seven rows are reverse dependencies, and they matter for isolating payments: S003, S004, S040, S076, S134, S155, S170.
- **what_crosses**: data, command or event.
- **mechanism**: one of field, mutation, webhook, Function, setting or session. The concrete name (mutation, topic, field, extension target) is given in brackets.
- **essential_or_specific**: always **Inference**, labelled as such.
  - *Essential*: the crossing would exist in any commerce platform that separates payments, whoever processes the money.
  - *Shopify-specific*: the crossing exists because of Shopify's business. Examples are Shopify Payments as processor and holder of funds, Shop Pay as its own wallet and identity network, Shopify Protect, Capital and Credit, plan tiers, platform billing, and product features such as post-purchase upsells.
- **quote**: a verbatim extract of at most 25 words. A script checked every quote against the cited line. The check normalised markdown links, HTML entities, backticks, JSON `\n` escapes and whitespace, then required the quote to appear on that line. All 178 quotes pass. The script is `scratchpad/seam_work/build.py`.
- **notes**: start with `Fact:` (cited) or `Inference:`. Line references inside the notes were also checked against their files.

### Source versions used

| Source | Version or date |
|---|---|
| Admin GraphQL | 2026-10, introspection captured 2026-09-30 |
| Payments Apps API | 2026-10, from dev-mcp 1.16.0, captured 2026-09-30 |
| payment_customization Function schema | 2026-10, from dev-mcp 1.16.0, captured 2026-09-30 |
| Customer Account API | 2026-10, from dev-mcp 1.16.0, captured 2026-09-30 |
| Storefront API | 2026-10, captured 2026-09-30 |
| App webhook topics (CLI) | 2026-10, run 2026-10-07 |
| Admin webhook topic list | Run 2026-10-07 |
| Webhook sample payloads | shopify.dev latest, labelled 2026-07, captured 2026-09-30 |
| Checkout UI extension targets | 2026.7.1 |
| Customer-account UI extension targets | 2026.7.1 |
| CLI extension templates | templates.json and GitHub main, both captured 2026-10-07 |
| Admin router and route titles | Admin bundle of 2026-09-29 |
| Admin controls | Sweeps and journeys 2026-09-30 to 2026-10-08 |
| Staff gates | Customer-support sweep 2026-10-05 |
| Assignable permissions | Run 2026-10-05 |
| Notification templates | Run 2026-10-07 |
| Flow connectors | Run 2026-10-07 |
| UCP profile | ucp 2026-08-25, captured 2026-10-04 |
| Web pixel events | Captured 2026-09-30 |
| Help Center and shopify.dev corpus | Fetched 2026-10-09 |
| Order reference page | api_version 2026-10 |
| Live pages | Fetched 2026-10-10: OXXO, duties fees, store permissions, email variables |

---

## 2. Counts

**Totals.** There are 178 crossings: 142 essential and 36 Shopify-specific (both labels are inference).

**By direction.**
- payments tells core: 92
- core asks payments: 79
- payments asks core: 7

**By what crosses.** Data 101, command 43, event 34.

**By area.**

| Area | IDs | Essential | Shopify-specific |
|---|---|---|---|
| Store setup and method catalogue | S001-S007 | 6 | 1 |
| Checkout: offering methods | S008-S029 | 17 | 5 |
| Payment attempt and buyer steps inside a method | S030-S048 | 18 | 1 |
| Order creation and recording | S049-S065 | 17 | 0 |
| Capture timing and fulfilment | S066-S077 | 9 | 3 |
| Terms, deposits, due dates, drafts, invoices | S078-S088 | 11 | 0 |
| Order editing | S089-S093 | 4 | 1 |
| Returns and refunds | S094-S104 | 10 | 1 |
| Cancellations and voids | S105-S110 | 6 | 0 |
| Point of sale and cash | S111-S119 | 8 | 1 |
| Subscriptions, mandates, vault | S120-S130 | 10 | 1 |
| Fraud, risk, disputes | S131-S136 | 5 | 1 |
| Markets, currencies, entities | S137-S144 | 5 | 3 |
| Taxes and duties | S145-S148 | 2 | 2 |
| Payouts, balance, finance products | S149-S156 | 0 | 8 |
| Merchant billing | S157-S163 | 1 | 6 |
| Apps, automation, other surfaces | S164-S167 | 3 | 1 |
| Staff permissions | S168-S173 | 5 | 1 |
| Notifications | S174-S178 | 5 | 0 |

**Webhooks as a mechanism.** Webhooks are a mechanism, not an area of their own. The 2026-10 topics that carry payment facts are listed below (`observed-sh/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl`, by line):

| Topic | Line(s) |
|---|---|
| order_transactions/create | 141 |
| orders/paid | 148 |
| tender_transactions/create | 224 |
| refunds/create | 174 |
| disputes/create, disputes/update | 63-64 |
| payment_terms/create, update, delete | 154-156 |
| payment_schedules/due | 153 |
| customer_payment_methods/create, revoke, update | 42-44 |
| subscription_billing_attempts/challenged, failure, success | 207-209 |
| orders/risk_assessment_changed | 150 |
| orders/shopify_protect_eligibility_changed | 151 |
| finance_kyc_information/update | 75 |
| finance_app_staff_member/* | 71-74 |
| app_subscriptions/*, app_purchases_one_time/update | 3-5 |

Fact: the `WebhookSubscriptionTopic` enum has 236 values and no payout or balance topic (`observed-sh/structures/shopify/admin-graphql-schema/2026-10/items.jsonl:3704`). Settlement events never reach apps as events.

---

## 3. (a) What stays inside payments and never reaches the order or checkout

The fact column cites where the material shows the item stays inside. Inference is marked.

| # | Inside payments | Fact or pointer |
|---|---|---|
| 1 | **Provider credentials and the merchant's provider account.** Only a ready flag and a display handle cross. | `observed-sh/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl:70`; study/C-provider-slot.md:202-205 |
| 2 | **Provider processing.** This covers authorization requests to issuers and networks, acquirer routing ("smart" routing to the processor most likely to authorize), automatic retries and "payment recovery", network tokens and 3-D Secure server traffic. Only results cross: the outcome, a normalised reason, AVS/CVV codes and the liability shift. | study/A2-processor.md:28; study/A1-arrangements.md:345; study/C-provider-slot.md:91-103 |
| 3 | **Raw card data.** It is encrypted to the provider certificate. The order keeps only display fields (brand, last digits). | study/C-provider-slot.md:31, 371 |
| 4 | **Vaulted instruments.** Core sees mandate ids, scopes and display data, never the instrument. | `observed-sh/structures/shopify/admin-graphql-schema/2026-10/items.jsonl:1949`; study/D-money-model.md:186-198 |
| 5 | **Provider-side references and receipts.** Examples are the PSP reference and Adyen's reference. Shopify keeps one payment id per attempt; `receiptJson` "is gateway-specific and not a stable contract". | study/A1-arrangements.md:405; study/D-money-model.md:130; study/C-provider-slot.md:352 |
| 6 | **Session state machine internals.** The states REDIRECTING, CONFIRMING and BUYER_ACTION_REQUIRED, timers, idempotent retries (18 tries over 24 h) and the first-writer-wins rule all stay inside. Only resolved, pending, rejected or timed-out reaches the order. | study/C-provider-slot.md:105-121, 177-185 |
| 7 | **The settlement ledger.** This is 114 balance-transaction types, each with a reversal twin, plus payouts (DEPOSIT or WITHDRAWAL), payout schedules, settlement delays, minimum payouts, reserves, holds, negative-balance recovery by bank debit or offset, bank accounts, payout descriptors and multi-currency payouts. An order sees at most a payout breakdown (S149). | study/A2-processor.md:214-291; study/D-money-model.md:134-152 |
| 8 | **Fees and tax on fees.** This covers processing rates, conversion fees, the extended-authorization fee and VAT/GST on fees. `OrderTransaction.fees` is "Only present for Shopify Payments transactions". | study/A2-processor.md:162-178; study/D-money-model.md:126 |
| 9 | **Risk models and monitoring.** This covers the fraud ML, card-testing detection, IP blocklists, chargeback-rate computation, VAMP, EFW and ECP programmes, NDRP enrolment, the merchant standing ladder and MATCH/VMSS listing. Only verdicts cross: a risk level, a block, or a hold that stops orders. | study/A2-processor.md:75-84, 352-378 |
| 10 | **Dispute mechanics with networks.** This covers evidence submission, deadlines, network reason codes, chargeback fees and holds, and auto-resolution. Only a dispute summary and its status cross (`Order.disputes`). | study/A2-processor.md:293-371 |
| 11 | **KYC and KYB.** This covers identities, documents, liveness checks, beneficial owners and registry matching. Only requests and status cross (S153, S151). | study/A2-processor.md:23-73; study/F-country-variability.md:142-159 |
| 12 | **Relationships behind the processor.** This covers Stripe, PayPal and Adyen as partners, banking partners, card-network rules, and creditor holds that only the processor can lift. | study/A2-processor.md:25-27, 83, 382-389 |
| 13 | **Governance of payments partners.** This covers invitation-only approval, revenue share on GMV, SLAs, PCI attestation, encryption certificates and listing states. | study/C-provider-slot.md:221-262 |
| 14 | **Finance products' own ledgers.** This covers Capital and Credit accounts, Balance accounts and cards, auto-transfers and retail cash-in. They cross only where they read sales or debit the balance (S154, S155). | study/E-pos-finance-billing.md:175-253 |
| 15 | **Test instruments and simulated outcomes.** Only the `test` flag crosses (S017). | study/A1-arrangements.md:201-204; study/A2-processor.md:158 |
| 16 | **Payout rails to the merchant's bank.** This covers ACH, SEPA and similar rails, trace ids and failed-payout handling. | study/A2-processor.md:258-268, 418 |

**Inference: cash custody.** Cash custody (drawer sessions, counts, discrepancies) sits on the payments side of the seam for Sharrwah, because it is a custody ledger. Shopify files it under POS. S112 is the crossing.

---

## 4. (b) Foundations shared by both sides that are not payments

| # | Foundation | Evidence |
|---|---|---|
| 1 | **Money representation.** Every amount is a `MoneyBag` (shop and presentment), with ISO currency codes, minor units, immutable allocation of remainders across lines, and rounding rules per currency. | study/D-money-model.md:263, 723; S137 |
| 2 | **Currencies and exchange-rate policy.** This covers the store currency, the presentment currencies a market enables, the rate source (automatic or manual) and when a rate is fixed. Pricing uses it, and so do capture, refund and payout. | S137, S138, S141; study/B-order-obligations.md:403-430 |
| 3 | **Markets and localization.** Buyer country and language, and the market that groups them. Both method eligibility and pricing read them. | S008, S009, S003 |
| 4 | **Legal sellers.** The business entity, merchant of record, store country and address, and tax registrations. | S002, S142, S143 |
| 5 | **Customers and B2B parties.** Customer accounts and authentication, companies, company locations and contacts. Privacy, merge and redaction events reach the vault. | S087, S088, S125, S126 |
| 6 | **Staff identity, roles and permissions, store owner, two-step authentication, devices and locations.** | S168-S172 |
| 7 | **The order and its records.** Agreements and sales lines (what was agreed), terms and schedules (what is due), order states, fulfilment orders and holds, returns. Payments reads them but does not own them. | study/D-money-model.md:270-293 |
| 8 | **Tax engine and tax lines.** These cover tax on the sale and estimated versus finalised tax. Tax on processing fees is internal to payments. | S145, S146 |
| 9 | **Inventory reservation.** | S044, S059, S061 |
| 10 | **Time.** Store time zone, UTC timestamps, business-day calendars. Dispute deadlines use the store time zone; settlement counts business days in UTC. | study/A2-processor.md:259, 312 |
| 11 | **Platform plumbing.** Idempotency keys, API versioning, the webhook and event bus, Flow automation, the app platform (OAuth scopes, extensions, Functions), notification templates, the order timeline and audit trail, file uploads used as evidence, reports. | S049, S164, S174-S178 |
| 12 | **Test-mode flag.** Carried on orders, transactions and balance entries. | S017 |

---

## 5. How narrow is the seam on Shopify?

**The provider contract is narrow.** These are facts.
- A provider gets one query and 16 mutations (`observed-sh/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl:26, 73`).
- Shopify sends it payment, refund, capture and void requests and a confirmation callback, plus a balance check for redeemables (study/C-provider-slot.md:55-68).
- It works from closed lists of states and reasons.
- It never sees an order id, a checkout id or line items.
- It may call no other Shopify API apart from mandatory webhooks (S030, S126).

**The whole payments capability is wide.** These are facts. It meets the rest of Shopify in 178 places, at every stage:
- the offer at checkout;
- buyer steps inside a method;
- creating, recording, capturing, collecting, refunding and cancelling;
- POS, subscriptions, risk, markets, tax, payouts, billing, staff and notifications.

**Inference: why the 178 do not make the seam wide.** Most of them (142) are generic commerce needs, and they pass through a small set of records:
1. the list of eligible methods;
2. the payment attempt (one id, one amount, one outcome);
3. the transaction posted on the order;
4. the signed amount still owed;
5. terms and schedules;
6. stored-payment permissions (mandates);
7. refund, capture and void commands with their outcomes;
8. dispute and risk verdicts.

A contract built around these eight records would let the rest of the platform be built independently.

**Inference: why Shopify's own seam is wider.** Shopify is also the processor, the wallet, the lender and the biller. That adds 36 crossings that exist only because Shopify holds the money:
- payouts shown on orders;
- labels, duties, bills and loans netted from the balance;
- account holds that can switch checkout off;
- forced refunds;
- tax reporting by the processor;
- plan-priced fees;
- Shop Pay ranking and identity;
- Shopify Protect.

**Inference: where isolation is hardest.** Two kinds of crossing make isolation harder than the provider contract suggests.

1. **Reverse dependencies.** In seven rows payments needs answers from core:
   - stock and discount validity before debit;
   - fulfilment and tracking for disputes and protection;
   - markets for auto-enabled methods;
   - store policies for some schemes;
   - all paid sales for lender claims;
   - store owner and two-step authentication.
2. **Leaks.** Core features check which arrangement was used:
   - installment orders can't be edited;
   - upsells are excluded for some methods;
   - subscriptions and pre-orders need named gateways;
   - store credit is refused on drafts;
   - capture per fulfilment needs multi-capture.

   A capability profile per arrangement would let core ask "can this payment do X?" instead of naming gateways.

**Inference: verdict.** Payments can sit behind a narrow, stable contract. It will be wider than Shopify's provider API, because it has to carry:
- capabilities;
- the confirm step;
- evidence access for disputes;
- the signed balance;
- mandates.

The settlement side (holding, netting, payouts) is a second contract, needed only if Sharrwah ever holds funds.

---

## 6. Crossings I suspect exist but could not evidence

| # | Suspected crossing | What the held material shows | What would settle it |
|---|---|---|---|
| 1 | Price change by payment method (surcharge, cash-on-delivery fee, pay-now discount) | Fact: the 2026-10 Function schemas for discounts, cart validation, cart transform and delivery customization contain no payment field (`observed-sh/structures/shopify/functions-graphql-schema/{discount,cart_checkout_validation,cart_transform,delivery_customization}/2026-10/items.jsonl`). UCP's terms extension allows a pay-now discount as a totals line (study/G-ucp-protocol.md:225), but Shopify's profile doesn't advertise terms. Inference: Shopify may not support it natively. | A checkout journey selecting cash on delivery with a fee app |
| 2 | Payout and balance events to apps | Fact: no payout or balance topic among 236 webhook topics (`observed-sh/structures/shopify/admin-graphql-schema/2026-10/items.jsonl:3704`). Inference: apps must poll `shopifyPaymentsAccount`, or internal events exist but aren't exposed. | — |
| 3 | Zero-total checkout skipping payments entirely (order fully covered by discount, or by a gift card before tax) | No held page describes the path | — |
| 4 | Automatic fulfilment hold on high risk | Fact: `HIGH_RISK_OF_FRAUD` is a hold reason (S075). Who places it, and when, is not documented in the held material. | — |
| 5 | Write-off of an unpaid balance | Fact: seen only as admin route titles and admin mutations (S065). No public API or Help Center page in the held material. Its effect on financial status and reports is unknown. | — |
| 6 | Card-present payments extension | Fact: seen only as a beta CLI template with `sync_terminal_transaction_result_url` (S007). The request and response contract is not held. | — |
| 7 | Market-to-entity mapping in the API | Fact: no `Market.businessEntity` field in Admin GraphQL 2026-10, although the guide says markets are assigned an entity (S009). The mechanism may be REST-only or admin-only. | — |
| 8 | Inventory on authorization expiry | Pending expiry releases stock for single-tender OXXO orders (S061). Whether an expired card authorization releases stock is not stated. | — |
| 9 | Cash-on-delivery refund and refusal at the door | No explicit flow for refunding an offline tender or for a buyer refusing on delivery (study/B-order-obligations.md:234). Inference: recorded as a manual refund or a cancel, with cash outside Shopify (S103). | — |
| 10 | Platform pull of payment status from a provider | Fact: Shopify never polls (study/C-provider-slot.md:185). Inference: the crossing doesn't exist on Shopify, but rails without callbacks need it. | — |
| 11 | Courier or agent custody of cash between buyer and seller | Fact: no Shopify crossing; the cash model ends at the drawer (study/E-pos-finance-billing.md:171). | — |
| 12 | Exchange payments linked to the return they settle | Fact: online exchange payments are matched by amount and timestamp (S097). A direct link may exist internally. | — |
| 13 | Lost chargeback reflected as an order adjustment | Fact: the payout is debited and the order isn't refunded (S110). Whether the order's money fields change after a loss is not stated. | — |
| 14 | Tax on processing fees reaching the merchant's tax reports | Fact: fee tax exists (`TransactionFee.taxAmount`) and monthly fee invoices are issued (study/F-country-variability.md:187). Inference: the link to core tax reporting is not documented. | — |
| 15 | Product-type eligibility of methods (digital goods, gift-card products, subscription lines hiding some methods) | Partly visible: Function input has lines and selling plans (S011); Shop Pay Installments thresholds; gift cards can't buy gift cards. No complete rule list is held. | — |
| 16 | Live behaviour behind the documents | Every row is what Shopify states or ships. None was observed by running a payment end to end. Observed-sh journey runs (e.g. 20260930T014656Z-journey-order-lifecycle) hold some admin behaviour but no provider traffic. | Journey runs |
