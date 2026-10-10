# G: UCP payment architecture and Shopify's published UCP profile

Reader slice: the Universal Commerce Protocol (ucp.dev, release 2026-08-25), and one real Shopify store profile. Anything marked "Inference:" is mine. Everything else cites a file and a section heading.

**Citation keys.** These files are under `scratchpad/corpus/ucp/`:

| Key | File |
|---|---|
| OV | `raw_specification_overview_.txt` |
| CO | `raw_specification_shopping_checkout_.txt` |
| PG | `raw_payment_guide.txt` |
| TK | `raw_payment_tokenization.txt` |
| PT | `raw_payment_examples_processor-tokenizer-payment-handler.txt` |
| SP | `raw_payment_extensions_split-payments.txt` |
| TE | `raw_payment_extensions_terms.txt` |
| AP | `raw_payment_extensions_ap2-mandates.txt` |
| AU | `raw_payment_extensions_authentication.txt` |

Other keys:

- **SH** is `scratchpad/schema/ucp-profile-capture-plus.json`.
- **PLT, ENC and ORD** were missing from the corpus. I fetched them read-only to stdout from ucp.dev 2026-08-25. They are `/specification/payment/examples/platform-tokenizer-payment-handler/`, `/specification/payment/examples/encrypted-credential-payment-handler/` and `/specification/shopping/order/`.
- **Section 5** names Shopify Admin and Payments Apps types for comparison only, taken from `scratchpad/schema/admin-2026-10-money.md` and `payments-apps-2026-10.md`.

---

## 0. Headline

- UCP is not a payment-methods model. It is a model of **who may hold what form of a credential at each hop**, split three ways:
  - **Instruments**: what the buyer uses to pay.
  - **Handlers**: versioned specifications for acquiring and processing an instrument.
  - **Processing**: done by the business and its PSP. The protocol leaves it opaque. [OV §Payment Architecture; PG §Core Concepts]
- The protocol stops at "order placed". It has no authorization, capture, settlement or payout objects. Payment failure is a message on the checkout. After purchase, money appears only as order `adjustments[]` (refund, dispute, and so on) and the terms extension's `accepted_term`. Order responses carry "No payment handlers needed post-purchase." [CO §Status Values; ORD §Schema/Order, §Adjustment; TE §Order Payment]
- The **business's response is authoritative** for everything that matters to payment: eligible handlers and instruments, totals, status, and the outcome of Actions. The platform executes and renders. [OV §Payment Handlers; PG §Resolving available_instruments; CO §Rendering Contract; OV §Actions]

---

## 1. Roles

| Role | Responsibility | Credential exposure | Cites |
|---|---|---|---|
| **Business** (merchant) | Merchant of Record (MoR). Configures handlers (public keys, merchant IDs) in checkout responses and filters them by cart context. Uses the instrument to "capture funds" through "their backend integration". | Gets opaque tokens, encrypted payloads or mandates, and "MUST NOT echo credentials back". Sees raw data only if it hosts a vault, decrypts (ENC) or calls `/detokenize` (PLT), which puts it in PCI scope. | CO §Overview; OV §Roles & Responsibilities, §Credential Flow & PCI Scope, §Payment in the Checkout Lifecycle; PT §Implementation Guide |
| **Platform** (client or agent surface) | Discovers handlers, runs the handler's acquisition logic, submits checkout, renders totals, processes Actions, and hands off via `continue_url`. It "is not the 'owner' of the funds". It "MAY engage an agent", but the agent "must hand over the checkout session to a trusted and deterministic UI" unless AP2 is negotiated. | "SHOULD NOT touch raw financial credentials". Its *main application* MUST NOT see raw credentials; only its compliant "secure credential provider" or vault may. | OV §The Trust Triangle; CO §Guidelines/Platform; PT §Security Considerations (Scope Isolation); PLT §Token Generation; ENC §Credential Encryption |
| **Payment Credential Provider (PCP)** (wallets and PSPs, e.g. Google Pay, Shop Pay) | "Defines the Spec": it authors the handler (JSON Schemas, config inputs). It collects, protects and validates raw credentials, can run risk checks during acquisition, and must ensure credentials "cannot be used by platforms directly (only by the intended business)". | Holds raw credentials. Typically PCI-DSS Level 1. | OV §Roles & Responsibilities, §Payment Credential Provider Scope, §Security Best Practices, §Fraud Prevention Integration |
| **Tokenizer** and **PSP** (extended participants that a handler may define) | Tokenizer: "Stores raw credentials and issues token credentials". PSP: "Processes payments on behalf of business using the checkout instrument". It also verifies AP2 `payment_mandate`. | See the table in §2. | PG §Participants; AP §PSP Verification |
| **Buyer** | Owns the `buyer` data (self-reported), `context` (provisional, "buyer-asserted" preferences and eligibility claims) and consent. `signals` "MUST NOT be buyer-asserted claims". | None | CO §Buyer, §Context, §Signals; OV §Signals |
| **Credential Issuer** (bank or network, AP2 option 2) | Issues the verifiable digital credential (VDC) whose key the user signs mandates with. | None | AP §Option 2: Digital Payment Credential |

- **Legal and technical relationships** [OV §The Trust Triangle]:
  - Business ↔ PCP: "pre-existing legal and technical relationship". The business holds API keys and the contract.
  - Platform ↔ PCP: the platform tokenizes through the PCP's interface.
  - Platform → Business: the platform passes "the result (a token or mandate)".
- **Who charges.** The business, or its PSP, at Completion. [OV §Payment in the Checkout Lifecycle; PG §Processing: `PROCESSING(identity, checkout_instrument, binding, transaction_context) → processing_result`]
- **Party identity inside a handler.** Each participant gets a `PaymentIdentity` (`access_token`) from out-of-band onboarding ("Prerequisites"). Participants that receive raw credentials "must complete security acknowledgements". [PG §Prerequisites; TK §Binding]

---

## 2. The handler abstraction

**Definition.**
- "Payment Handlers are specifications (not entities) that define how payment instruments are processed. They are the contract that binds the three participants together."
- "Payment Credential Provider = The participant… Payment Handler = The specification the provider authors (e.g., com.google.pay, dev.shopify.shop_pay)." [OV §Payment Handlers]
- Every handler spec must cover five things [PG §Core Concepts]:
  - Participants
  - Prerequisites
  - Handler Declaration
  - Instrument Acquisition (`INSTRUMENT_ACQUISITION(platform_prerequisites_output, handler_declaration, binding, buyer_input) → checkout_instrument`)
  - Processing

**Advertisement.**
- `ucp.payment_handlers` is a registry keyed by reverse-domain handler name. Each value is an array of instances with `id` (instruments refer back to it via `handler_id`), `version` (YYYY-MM-DD, evolving independently of UCP core), `spec` (human-readable URL), `schema` (JSON Schema URL), `available_instruments` and `config`. [PG §Handler Declaration, §Best Practices/Documentation; OV §Profile Structure]
- The registry is required in both business and platform profiles, even when empty. [OV §Profile Structure]
- **Provenance.** "a declared schema URL's origin MUST match the namespace authority in its name". Platforms must reject handlers that fail this check. It "guarantees provenance, not trust". [OV §Authority Binding, §Enforcement]
- **Three declaration variants** [PG §Handler Declaration Variants]:
  - `business_schema`: in `/.well-known/ucp`, carrying merchant settings.
  - `platform_schema`: in the platform profile, carrying platform identity and support.
  - `response_schema`: in checkout and order responses, as runtime config. "Platforms MUST treat this as authoritative."
- Ids "may differ between business and platform".
- Config shapes are per variant. The response config can add runtime state, e.g. `token_ttl_seconds` (PLT §Response Config) or `encryption_algorithm`/`key_id` (ENC §Response Config).

**Selection.**
- "Businesses MUST filter the handlers list based on the context of the cart" (e.g. drop BNPL for subscriptions, or regional methods by address).
- `map_order.payment_handlers` gives a *suggestive* presentation order. The order of `available_instruments` ranks instruments within a handler.
- The buyer's preference arrives in `context.payment[]`, as "Buyer-preferred payment handlers in priority order". "the platform arbitrates between the two." [OV §Payment Handlers, §map_order; CO §Context]
- Eligibility is recomputed on every response. Under terms, "ucp.payment_handlers in this response is the set resolved for the selected term". A handler "that must be initialized with the amount and timing it will charge cannot be prepared before the term is agreed". [TE §Payment instruments and eligibility, §Lodging example]

**Instruments.**
- A submitted **Selected Payment Instrument** has these fields: `id`, `handler_id`, `type` (broad category, constrained to a const by the specific schema), `billing_address`, `credential` (optional), `display`, `selected`. Split payments adds `amount`. [CO §Payment, §Selected Payment Instrument; SP §Schema]
- Only `card` has a normative instrument schema (`card_payment_instrument.json`). Others such as gift_card or loyalty are "handler-defined". [SP Note on examples; PG §Instrument Shapes]
- **Credentials** are a `type`-discriminated union [PG §Credential Shapes]:
  - `token_credential`
  - `pan_credential` ("Raw FPAN… Source only")
  - `network_token_credential` (with cryptogram)
- Token credentials "MUST include an expiration field". [PG §Credential Shapes]
- **Saved instruments.** A business may return display-safe, business-scoped saved instruments (an opaque id plus display fields) on identity-linked responses. It resolves them server-side.
- "Whether the instrument can be charged as-is or still requires credential collection is not distinguished by the base schema today". [CO §Payments]

**Available instruments.**
- Each entry narrows along two axes [PG §Handler Declaration]:
  - `type` plus `constraints`, evaluated against the instrument schema's `$defs/constraint_target`. This covers what the business *derives*, e.g. card `brand`.
  - `ucp.request_constraints` with an explicit JSONPath, for what must be *on the wire*. Example: PAN requires `cvc`; network token requires `cryptogram`/`eci_value`; `billing_address` is required.
- Resolution = platform-declared ∩ business-declared ∩ cart context. The response "is authoritative… MUST NOT attempt to use instrument types or apply constraints that contradict it". In the example, Discover is dropped because "the business's PSP is not configured for Discover". [PG §Resolving available_instruments; OV §Billing address on a submitted card instrument, §Alternative verification requirements]
- When absent, there is no restriction beyond the handler schema.
- Request Constraints are preflight only. "payment authorization remain[s] governed by the operation's existing outcomes and messages". [OV §Request Constraints/Guidelines]

**Credential-flow variants.** "Platform app" below means the platform's main application.

| Variant | Who sees the raw credential | What the business receives | How it is resolved to money | Cites |
|---|---|---|---|---|
| Wallet (Google Pay, Shop Pay) | Wallet provider | Encrypted token (`credential.type: PAYMENT_GATEWAY`) | Gateway named in `tokenization_specification` | OV §Scenario A |
| **Processor tokenizer**, PSP-hosted | Platform's secure credential provider and PSP | `token` | PSP resolves internally; "no API detokenization step" | PT §Introduction, §Comparison |
| Processor tokenizer, business-hosted | Platform's credential provider and business vault | `token` | Business; "High" PCI scope | PT §Comparison |
| **Platform tokenizer** | Platform's credential provider. The business or PSP also sees it after `/detokenize`. | `token` (e.g. `ptok_…`) | Business or PSP calls `/detokenize`, adding `identity` when acting for the business | PLT §Pattern Flow, §Processing Payments |
| **Encrypted credential** | Platform vault. The business sees it after local decryption. | `encrypted_data`, with the binding embedded | Business private key; "no /tokenize or /detokenize" | ENC §Introduction, §Security Considerations |
| Network token direct | No FPAN is shared | `network_token` + cryptogram | PSP or network | TK §Credential Flow; OV §Platform Scope |
| AP2 | Per handler | `payment_mandate` in `credential.token` | PSP verifies the mandate | AP §Mandate Structure |

**Binding and token rules.**
- Binding = `{type, id}` of the capability resource, e.g. `dev.ucp.shopping.checkout` plus the checkout id. It is "a replay guard, not a resource reference".
- Tokenizers must match it by exact equality, treat the `id` as opaque and accept unknown `type` values. Each token is issued to exactly one participant; on detokenize the tokenizer verifies both that participant and the caller's authority to act for it.
- Token lifecycle is single-use (the recommended default), TTL-based, or session-scoped. Tokens need ≥128 bits of entropy and typically a 5–30 minute TTL. [TK §Binding, §Token Lifecycle, §Security Requirements; PG §Key Definitions]
- The guide notes that tokenization "patterns apply to any sensitive credential type—bank accounts, digital wallets, loyalty accounts". [TK §Overview]

**Why the separation exists.** It solves "N-to-N" complexity [OV §Payment Architecture; PG §Purpose] and keeps the platform, and often the business, out of PCI scope [OV §PCI-DSS Scope Management]. `handler_id` routing stops key-confusion attacks [OV §Credential Flow & PCI Scope] and binding stops replay. PCPs can add "Custom Handler Types… to support new payment instruments" without changing core [OV §Payment Architecture Extensions].

---

## 3. Checkout lifecycle and outcomes

**Statuses.** The business sets the status. [CO §Checkout Status Lifecycle, §Status Values]

| Status | Meaning |
|---|---|
| `incomplete` | Something is missing; read `messages` |
| `requires_escalation` | Needs input the API cannot collect, or buyer review; hand off via `continue_url` |
| `ready_for_complete` | No outstanding Action |
| `complete_in_progress` | Accepted. "MUST NOT contain order"; Actions may be outstanding |
| `completed` | `order` present; immutable afterwards |
| `canceled` | "invalid or expired"; can occur from any state |

There is **no "payment failed" status**. A decline returns the checkout to `incomplete` with a `payment_failed` error. [CO §Standard Errors; SP §Partial Failure with Recovery]

**Submitting payment.**
- `payment` is optional on create and update but **Required** on Complete Checkout. [CO §Complete Checkout Inputs]
- Exactly one instrument is allowed unless split payments is active. A violation gets `payment_failed`. [OV §Payment Handlers/Instrument Cardinality]
- Payment runs in three phases: Negotiation (business advertises), Acquisition (platform ↔ PCP; "The business is not involved"), Completion (platform → business; the business captures). [OV §Payment in the Checkout Lifecycle]
- If completion is synchronous, the result is `completed` plus `order {id, label, permalink_url}`. If asynchronous, the result is `complete_in_progress`. [CO §Complete Checkout, §Order Confirmation]
- The default session TTL is 6 hours. [CO §Capability Schema Definition/expires_at]

**Buyer actions: two coexisting mechanisms.**

1. **Escalation.**
   - `requires_escalation`, plus at least one message with severity `requires_buyer_input` (data the API can't collect) or `requires_buyer_review` (policy or regulatory authorization), plus a mandatory `continue_url`. [CO §Error Handling, §Continue URL/Availability, §Guidelines]
   - Scenario B shows a PSP "Soft Decline" returned as `requires_escalation` with `code: requires_3ds` and `continue_url: https://psp.com/challenge/123`. The platform "MUST now open continue_url… then retry the completion". [OV §Scenario B]
2. **Actions.** These are response-only, extension-declared units of outstanding work, keyed by reverse-domain type.
   - Each has an `id` and `config`. Each "gates" an effect.
   - A Message's severity does not decide whether an Action gates.
   - "A Platform MUST NOT assume that the effect gated by an Action succeeded merely because an Action surface… completed". [OV §Actions, §Trust and Execution Boundaries]
   - The **Payment Authentication** extension standardizes `dev.ucp.common.payment.device_data_collection` and `…three_ds_challenge`. `config.payment_instrument_id` and `config.url` identify the instrument and the surface. Surfaces must load from the handler's allowed origins.
   - The surface handshake is `action.ready`, then `action.done` or `action.error`.
   - Each occurrence is single-use. To retry, the business issues a new `id`.
   - After `action.done` the platform polls Get Checkout for at most 30 seconds. "action.done… means only that the Platform-facing surface finished. The Business determines whether… authentication succeeded from its server-side payment-provider state." [AU §Runtime Shape, §Checkout Lifecycle, §Surface Rendering]
   - The business "SHOULD accept Complete Checkout before beginning a payment-authentication interaction… and return complete_in_progress with the Action". [AU §Checkout Lifecycle]
   - Handlers may instead define their own Action types through a Checkout extension. [PG §Payment Actions]

Inference: Scenario B (escalation for 3DS) and the authentication extension (an in-band Action) are older and newer answers to the same need. The Action path keeps the agent in control and keeps the outcome authoritative on the server.

**Errors.**
- `ucp.status` (`success`/`error`) discriminates the response shape. [CO §Error Handling]
- Each message has `type`, `code`, `severity`, `content` and a JSONPath `path`. Severities and what they mean:

| Severity | Meaning |
|---|---|
| `recoverable` | Fix in band and resubmit |
| `requires_buyer_input` | Hand off |
| `requires_buyer_review` | Hand off |
| `unrecoverable` | No resource; retry anew or hand off |

- Standard codes include `payment_failed` and `eligibility_invalid`. [CO §Standard Errors]
- Handler specs "MUST define a mapping for common failures (e.g., 'Declined', 'Insufficient Funds'…) to standard UCP Error definitions". [PG §Error Handling]
- A business can demand signals with a `code: signal` error. [OV §Signals]
- The platform "MUST NOT autonomously complete a checkout with mismatched totals". [CO §Verification]

**Async completion contract.** While `complete_in_progress`, Update is frozen and a new Complete is forbidden. Get Checkout uses bounded backoff until `expires_at`. Cancel comes only after fallback and handoff are exhausted, and "the Platform MUST NOT treat the Checkout as canceled unless the Business reports status: canceled." [CO §Accepted completion]

**Idempotency.**
- Businesses must "Implement idempotency for payment processing (prevent double-charges)". [OV §Security Best Practices]
- HTTP 409 means "Idempotency key reused with different payload". [OV §Error Handling]
- `idempotency-key` is in the signature's covered set. [OV §Identity Resolution Algorithm]
- If a Complete response is lost: call Get Checkout first. Re-send the *identical* request with the *same* key only if state is still unknown. A genuinely new attempt "MUST use a fresh idempotency key, even if the payload is unchanged". [CO §Complete Checkout]
- A changed split-instrument set is a new submission with a fresh key. [SP §Error Handling]

**Order reconciliation.**
- The order carries `checkout_id` "for reconciliation" and the same currency.
- `adjustments[]` hold typed money movements: `refund`, `credit`, `dispute`, `cancellation`, and so on. Status is `pending`/`completed`/`failed`, totals are signed, and an "append-only ledger is preferred".
- Updates are pushed by signed webhook to the platform's `webhook_url`. [ORD §Overview/Key Concepts, §Adjustment, §Events]
- There are no order-level payment-status, authorization or capture fields.
- "Whether a due payment is authorized, captured, or settled at that moment is payment-handler behavior". [TE §Payment Schedule]

---

## 4. Extensions

### Split payments (`dev.ucp.common.payment.split_payments`)

- **Business config.** `allowed_combinations` is an array of combinations. Each combination is an array of *instrument groups* `{types[] (OR), min (default 0), max (default 1)}`. A submission is valid if some assignment of instruments to groups satisfies every group's min and max. [SP §Configuration]
- **Allocation.**
  - Array order is "allocation priority": first claim on the total goes to the first instrument. The business "MAY process payment authorizations in any order" (e.g. gift cards first to minimize reversal cost).
  - A *specified-amount* instrument must be authorized for exactly that amount.
  - An *open-amount* instrument contributes what the business determines, usually the available balance up to the remaining total. A balance of $0 is valid, not a failure.
  - Foreign-currency or points instruments must be converted into checkout currency by the handler. [SP §Overview, §Instrument Processing Model]
- **Failure.**
  - "A split payment either completes fully or has no financial effect." The business must void or reverse partial authorizations and return `payment_failed` per failed instrument (`path` points at it, severity `recoverable`). It may add `info` messages for instruments that succeeded.
  - It is an error if the total is unreachable, specified amounts exceed the total, or the set matches no combination.
  - No state persists between requests. [SP §Error Handling]
- **Response.** `amount` is set only on instruments actually authorized or charged. It is "informational". The platform must not echo it back as state. [SP §Response: Actual Charges]
- **Composition with other extensions.** Split works with a terms term only when that term has exactly one schedule. [TE §Payment instruments and eligibility] With Payment Authentication, there is one attempt and one Action per instrument, keyed by `payment_instrument_id`. [AU §Runtime Shape]

### Payment terms (`dev.ucp.common.payment.terms`, extends checkout and order)

- **What it expresses.** *When* money is due, not how it is collected.
  - `payment.terms[]` (response-only) lists **terms**. Each term has `id`, `title`, `description` and `schedules[]`.
  - Each **schedule** is one payment: `id`, `type` (open vocabulary; only `immediate` is defined, and anything else means "not due at completion"), `description` (a complete buyer-facing statement), optional `due_at` (omitted when it "depends on a future event — 'due on delivery'"), and `amount` (including tax).
  - `selected_term_id` is always present when `terms` is. [TE §Overview, §Payment schedules, §Schema]
- **Invariants.** The selected term's schedules sum to the checkout total; unselected terms are "indicative". A pay-now discount or finance charge appears as its own `totals` entry. Selection happens via Update and is omitted on create and complete. When the term in effect changes, the business emits a `payment_term_changed` warning. The instrument "MUST be capable of every one" of a term's schedules, and a multi-schedule term must be funded by a single instrument. [TE §Amounts, §Selecting a payment term, §Payment instruments and eligibility]
- **Disclosures.** These use a policy (`applies_to` the term) plus a `presentation: "disclosure"` warning. A platform that cannot honor them must escalate via `continue_url`. [TE §Disclosures]
- **On the order.** `payment.accepted_term` "is the agreement, not a running balance". It is immutable. Post-purchase changes go in `adjustments[]`. [TE §Order Payment]
- **Out of scope:** amounts not determinable at checkout ("authorizations and order adjustments"), multiple currencies, recurring commerce, and **payment execution**: "a Platform MUST NOT infer that a deferred payment can be inspected, modified, or cancelled through UCP". [TE §Out of scope]

### AP2 mandates (`dev.ucp.common.payment.ap2_mandate`)

- **What it adds.** "non-repudiable authorization through verifiable digital credentials". Once it is negotiated the session is "Security Locked". [AP §Overview; OV §Transaction Integrity]
- **Business signature.**
  - `ap2.merchant_authorization` is a detached JWS (`alg` ES256/384/512 per AP2 v0.2, plus `kid`).
  - It is computed over the JCS-canonicalized checkout *minus* `ap2`, and covers `ucp` members.
  - The platform must verify it before showing the checkout. [AP §Business Authorization, §Canonicalization]
- **The platform produces two artifacts** (SD-JWT+kb) [AP §Mandate Structure, §Step 3]:
  - `ap2.checkout_mandate` ("Proof bound to checkout terms, protects business"). It contains the *full* checkout including the merchant signature, a nested binding.
  - `payment_mandate`, carried in `payment.instruments[*].credential.token` ("protects funds"). The PSP verifies it.
- **Consent models** [AP §Step 2]:
  - **Trusted Platform Provider**: the platform signs with a server key from its profile `keys[]` after explicit user consent "from trusted, deterministic channels".
  - **Digital Payment Credential**: a bank- or network-issued VDC is presented via OpenID4VP and the user's wallet signs.
- **Business verification.** Missing mandate → `mandate_required`. Then verify the SD-JWT, extract the embedded checkout, verify its own signature, and match id, totals and line items.
- **Error codes**: `mandate_invalid_signature`, `mandate_expired`, `mandate_scope_mismatch`, `merchant_authorization_invalid`, and others. [AP §Business Verification, §Error Codes]
- **Why JCS.** Mandates are durable evidence that may be "verified days or months later" across platform → business → PSP → card network. [AP §Canonicalization]
- **Cart vs intent mandates.** These terms do not appear in the UCP corpus. UCP defines only placement: "The mandate credential structure… is defined by the AP2 Protocol Specification". [AP §Mandate Structure]
  - Outside corpus, from my background knowledge: AP2 itself describes Intent, Cart and Payment mandates.
  - Inference: UCP's `checkout_mandate` plays the cart-mandate role, i.e. the user signs exact terms. UCP 2026-08-25 has no placement for a pre-signed intent mandate (human-not-present delegation).
- The overview's Scenario C example advertises `available_instruments: [{type:"ap2_mandate"}]` but submits `type: "card"`. [OV §Scenario C] This is a spec-example inconsistency.

### Payment authentication (`dev.ucp.common.payment.authentication`)

Covered in §3. Its scope: "It does not re-specify EMV 3DS, carry EMV 3DS messages, report authentication outcomes, or replace payment-handler processing." [AU §Overview]

---

## 5. What this adds to Shopify's internal model

**Facts from Shopify's published profile** [SH]:

- **Versions and transports.** `ucp.version` is 2026-08-25, with `supported_versions` 2026-04-08 and 2026-01-23. The only 2026-08-25 transport is **MCP** (`/api/ucp/mcp`), plus `embedded` at 2026-04-08. There is no REST binding.
- **Capabilities advertised:** checkout, fulfillment (`method_combinations [["shipping"]]`), discount, cart, order, catalog.search and catalog.lookup (plus the vendor extension `dev.shopify.catalog`), identity_linking (`app.shop.accounts` OAuth2) and permalink (`/buy`).
- **Not advertised:** split_payments, terms, ap2_mandate, authentication. There is also no `keys[]` and no `map_order`.
- **Payment handlers** (none declares `available_instruments`):

| Handler | id / version | Config |
|---|---|---|
| `com.google.pay` | `gpay` / 2026-01-11 | `PAN_ONLY` + `CRYPTOGRAM_3DS`; VISA, MASTERCARD, AMEX, DISCOVER; `billing_address_required: true`; `tokenization_specification {type: PAYMENT_GATEWAY, gateway: "shopify", gatewayMerchantId: "101061591336"}` |
| `dev.shopify.card` | `shopify.card` / 2026-01-15 | `spec` points at the generic UCP payment-handler guide. `config.payment_methods[{type:"card", enabled_card_brands:[visa, master, american_express, discover, diners_club]}]` |
| `dev.shopify.shop_pay` | `shop_pay` / 2026-04-08 | `config.shop_id: "101061591336"` |

- Handler versions differ from each other and from the protocol version, consistent with PG §Best Practices ("Version independently").
- **Brand vocabularies are not normalized.** Google uses `MASTERCARD`/`AMEX`. Shopify card uses `master`/`american_express`. UCP examples use `mastercard`/`amex`. [SH; OV §Scenario B]

**Shopify plays several UCP roles at once.**
- Inference: Shopify runs the business's UCP endpoint on the merchant's domain. It is the PCP for Shop Pay and the card vault, and the Google Pay *gateway* (`gateway:"shopify"` with `gatewayMerchantId` = `shop_id`).
- So the "Trust Triangle" collapses on the business side. The platform/agent is the only party outside Shopify.

**Concept mapping.** All rows are Inference.

| UCP | Shopify internal (from the other slices) | Note |
|---|---|---|
| Handler (acquisition spec) + business config | Checkout payment method / gateway / Payments App extension | UCP describes the *buyer-surface acquisition* side. Shopify's gateway and app model describes the *processing* side. |
| `handler_id` routing + `PaymentIdentity` | Shop/gateway merchant identifiers | The same identity appears as `shop_id` and `gatewayMerchantId` |
| Instrument + credential | `PaymentSession` payment method; `OrderTransaction.paymentDetails` (`CardPaymentDetails`, `LocalPaymentMethodsPaymentDetails`) | UCP carries only display fields and an opaque credential |
| Business-owned saved instrument (identity-linked) | `CustomerPaymentMethod`, `CustomerShopPayAgreement` | UCP: "opaque, business-scoped reference" |
| `complete_in_progress` + auth Actions; `requires_escalation` | `PaymentSessionState` `PENDING` (reason `BUYER_ACTION_REQUIRED`), `REDIRECTING`, `CONFIRMING`; `PaymentSessionThreeDSecure*` | Shopify models provider states. UCP exposes only "buyer work outstanding" and the final checkout status. |
| `payment_failed` (+ handler error mapping) | `PaymentSessionStateRejectedReason` (`CARD_DECLINED`, `AUTHENTICATION_FAILED`…), `OrderTransactionErrorCode` | The mapping is required by PG §Error Handling |
| `completed` + `order` | `Order` + `OrderTransaction` (`AUTHORIZATION`/`SALE`/`CAPTURE`/`VOID`/`REFUND`) + `OrderDisplayFinancialStatus` | **UCP deliberately hides the transaction ledger** |
| Order `adjustments[]` | `Refund`, `OrderAdjustment`, disputes | UCP has a typed open-string event list |
| Terms `terms[]` / `accepted_term` | `PaymentTerms` (`PaymentTermsType` RECEIPT/NET/FIXED/FULFILLMENT), `PaymentSchedule` (`dueAt`, `balanceDue`), `DepositConfiguration` | Shopify tracks balance and overdue state. UCP's `accepted_term` is "the agreement, not a running balance". |
| AP2 mandate | `PaymentMandate` (`orderCreateMandatePayment`) | Same word, different meaning. Shopify's is the merchant's standing permission to charge a vaulted instrument. AP2's is cryptographic proof of user consent to one checkout. |
| Split payments | Multiple transactions on one order (gift card + card) | Shopify gift cards are native (`GiftCardDebitTransaction`) |

**What UCP adds.** Inference:
- A seller-published, versioned, provenance-bound catalogue of arrangements that any surface can consume.
- Binding of credentials to a resource and a recipient.
- Per-checkout authoritative eligibility.
- A generic "outstanding buyer work" primitive.
- Cryptographic consent artifacts.
- Disclosure obligations attached to payment timing.

**What UCP does not carry.** Authorization or capture state, settlement, payouts and fees. These stay inside Shopify.

---

## 6. Relevance to a non-card market (Yemen)

All inference except the quoted facts.

- **General fit.**
  - The handler/instrument/credential split is about *how proof travels from buyer to the party that can move money*, so it is not card-bound. TK §Overview says the patterns apply to "bank accounts, digital wallets, loyalty accounts". The instrument `credential` is **Optional**. [CO §Selected Payment Instrument]
  - The weak spot is everything **after** completion. UCP has no payment state on the order, no "awaiting funds", and no collector role other than "PSP".
- **Cash on delivery.**
  - Model it as a Sharrwah handler (e.g. `com.sharrwah.cod`) with an instrument type `cash_on_delivery` and no credential.
  - Timing fits the terms extension: one schedule with a non-`immediate` type (e.g. `on_delivery`), `description` "Pay cash to the courier on delivery", and **no `due_at`**. TE §Due dates uses this exact case.
  - Gaps:
    - The courier is not a protocol participant.
    - Cash remittance, refusal at the door and partial acceptance would have to be order `adjustments[]` or a custom extension.
    - TE forbids inferring that deferred payments can be "inspected, modified, or cancelled through UCP".
- **Mobile wallet with buyer OTP.** There are two clean placements:
  - (a) *During Acquisition*. The platform runs the wallet's handler spec directly with the wallet (the PCP), the buyer enters the OTP there, and a bound, expiring token is returned. The business never sees the OTP. This mirrors Scenario A/B tokenization.
  - (b) *During Processing*. The business accepts Complete, returns `complete_in_progress`, and emits a handler-specific Action (e.g. `com.wallet.otp_confirmation`), which PG §Payment Actions explicitly permits. It then decides the outcome from provider state.
  - Fallback is `requires_escalation` + `continue_url`.
  - Design note: decide per wallet whether the debit is *pull* (merchant-initiated after OTP) or *push* (buyer approves in the wallet app). Push behaves like the bank-transfer case below.
- **Buyer-supplied voucher redeemed by the merchant.** This maps directly to SP's `gift_card`/`store_credit` instrument types:
  - The voucher code goes in `credential.token`.
  - Use open-amount: the business looks up the balance, and $0 is valid.
  - Unwinding is atomic if a co-funding instrument fails.
  - `allowed_combinations` limits stacking.
  - For third-party vouchers, the handler config identifies the issuer and the "processor tokenizer" pattern fits, with the issuer as tokenizer and processor.
- **Bank transfer confirmed later.**
  - `complete_in_progress` is asynchronous but bounded by `expires_at` (default 6h) and Get Checkout polling. It is not meant for days.
  - Better: complete the order with a term whose schedule is `type: "deferred"`, e.g. "Transfer to account X with reference R within 48h". The reference can travel in schedule text, an Action config, or an extension.
  - Confirmation is then a post-order event. UCP's Order has no field for it, so Sharrwah needs its own order payment-state model.
  - The TE rule "instrument… MUST be capable of every one of [the term's schedules]" holds trivially.
- **Marketplace caution.** UCP assumes the business is MoR and the platform "not the 'owner' of the funds". If Sharrwah collects on behalf of sellers, its internal model needs explicit parties and money-ownership hops that UCP intentionally leaves out.

---

## 7. Class-level questions

1. How does a seller advertise the arrangements it accepts, as versioned, provenance-verifiable definitions, so that any buyer surface (its own checkout, a marketplace, an agent) can use them without bespoke integration? — *information / extension*
2. Which arrangements are eligible for *this* obligation, given cart contents, destination, amount, chosen timing and instruments already supplied? Who is authoritative when the surface's capabilities and the seller's configuration disagree? — *rules*
3. How is acquiring a credential or proof separated from moving money, and which party may hold which form of the credential (raw, token, encrypted, signed proof) at each hop? — *actors / scope*
4. How is a credential or proof bound to exactly one obligation and one recipient so it cannot be replayed? What decides its lifetime (single-use, time-limited, session-scoped)? — *rules / quality*
5. When completing payment needs a buyer step the surface cannot do in-band (OTP, bank challenge, physical presence), how is that step represented, sequenced and timed out? Who decides it succeeded? — *lifecycle / events*
6. What are the distinguishable outcome states of a payment attempt (accepted-pending, buyer-work-outstanding, declined-recoverable, unrecoverable, completed, canceled)? Whose record is authoritative for each? — *lifecycle*
7. What identifies "the same attempt" versus "a new attempt", so that lost responses and retries never cause a double charge? — *quality / events*
8. When several arrangements fund one obligation, how are amounts allocated and prioritized? What happens to partial successes when one fails? — *rules / variability*
9. How is *when money is due* expressed separately from *how it is collected*? How does the accepted schedule become a durable agreement on the order, distinct from the running balance? — *information / lifecycle*
10. For a purchase initiated by an agent or third party, what evidence of buyer consent must exist, who signs which part (seller's terms vs buyer's authorization), and how long must it remain verifiable? — *actors / quality*
11. After the order exists, how are later money movements (collection on delivery, transfer confirmation, refund, dispute) recorded against the order and correlated to the originating checkout and arrangement? — *events / information*
12. How are failure reasons from heterogeneous providers normalized into one vocabulary that every surface presents consistently? — *variability / quality*
13. What does an arrangement look like with **no credential at all** (cash on delivery, pay at pickup, invoice)? Who is the collector, and who is liable for remitting to the seller? — *scope / actors*
14. Which disclosure obligations travel with an arrangement (finance charge, deposit forfeiture, fees)? What must a surface do if it cannot honor them? — *rules / quality*
15. Who is merchant of record and who owns the funds at each hop (buyer → collector → platform → seller)? Does the buyer-facing protocol need to know, or only the internal ledger? — *actors / scope*
