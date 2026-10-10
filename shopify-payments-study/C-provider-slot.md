# C — The provider slot: Payments Apps, payment customization Functions, payment terms

Reader C. Scope: how a third-party provider plugs into Shopify checkout, and how merchants and apps customise the method list and set terms. All claims cite a source. "Inference:" marks my own reasoning.

## Source keys
Corpus-relative (root `corpus/`, `dev/X.md` maps to `https://shopify.dev/X`):
- [OV] dev/docs/apps/build/payments.md · [API] dev/docs/api/payments-apps/latest.md
- [REF] dev/docs/apps/build/payments/request-reference.md · [PROC] .../payments/processing.md · [CONS] .../payments/considerations.md · [CONF] .../payments/configuration.md · [REQS] .../payments/requirements.md · [REV] .../payments/payments-extension-review.md · [ONB] .../payments/onboard-a-merchant-payments-extension.md
- [ALT] .../payments/alternative/build-an-alternative-payment-extension.md · [CC] .../payments/credit-card/use-the-cli.md · [CERT] .../credit-card/manage-encryption-certificates.md · [TCERT] .../credit-card/test-certificate.md
- [CPAY] dev/docs/apps/build/checkout/payments.md · [CPF] .../checkout/payments/create-payments-function.md · [TERMS] .../payment-terms.md · [REVW] .../review-requirements.md · [CFG] .../add-configuration.md · [UI] .../build-ui.md · [UX] .../ux-for-payments.md · [CHK] dev/docs/apps/build/checkout.md · [CAP] dev/docs/apps/build/checkout/capabilities.md
- [MOFF] dev/docs/storefronts/mobile/checkout-kit/offsite-payments.md · [MACC] .../checkout-kit/accelerated-checkouts-overview.md · [TACC] dev/docs/storefronts/themes/pricing-payments/accelerated-checkout.md (+ /multiple-product-checkout.md) · [INST] .../pricing-payments/installments.md
- Schemas: [S:Type] = schema/payments-apps-2026-10.md · [FN:Type] = schema/fn-payment-customization-2026-10.md · [ADM:Type] = schema/admin-2026-10-money.md

Missing from the corpus and fetched read-only (marked *): [OFF*] shopify.dev/docs/apps/build/payments/offsite/use-the-cli.md · [RED*] .../payments/redeemables/build-a-redeemables-payment-extension.md · [MUT*:name] = shopify.dev/docs/api/payments-apps/latest/{mutations|enums|objects|input-objects}/name.md · [AREF*:name] = shopify.dev/docs/api/admin-graphql/latest/... (enum and field descriptions).

---

## 0. The model in one paragraph

A Shopify "payments extension" makes the provider a remote state machine. Shopify **commands** it over HTTPS (mTLS), with one "session" per financial operation: `payment`, `refund`, `capture`, `void`, plus the `confirm` callback and the redeemable `balance` request. The provider answers synchronously only with "accepted" (2xx/201, or a `redirect_url`). It reports the **outcome** later through idempotent GraphQL mutations (`paymentSessionResolve`/`Reject`/`Pending`/`Redirect`/`Confirm`/`Modal`, `refund|capture|voidSessionResolve`/`Reject`) [PROC][CONS]. Each session has its own idempotency `id`. Payment attempts for one checkout share a `group`, and attempts with the same payment details share a `session_id` [REF]. Once a session is resolved or rejected it is final [PROC]. Shopify keeps the order, the inventory and discount checks, the buyer UI and the method list. The provider keeps the credentials, the processing, the risk work, settlement to the merchant, and the duty to always report back [REQS]. Merchants (and non-provider apps) customise which methods appear and set deferred payment terms through a separate Function. Providers are forbidden from using that Function [REQS][CPAY].

---

## 1. Extension kinds

Every kind is `type = "payments_extension"`. The kind is chosen by the `[[extensions.targeting]] target` [CONF]. Only approved Payments Partners can build them [OV][REV]. The `write_payment_gateways` and `write_payment_sessions` scopes are restricted and granted through the extension [CONS][CONF].

| Kind (target) | Purpose | Who collects credentials / where the buyer goes | Shopify controls / provider controls | Must support |
|---|---|---|---|---|
| **Offsite** `payments.offsite.render` | "redirect their buyers to an app-hosted website to complete the payment process" [OV][CONF] | Provider, on its own page. Shopify redirects the buyer to the `redirect_url` returned synchronously, and the provider "collects the customer's payment credentials" [PROC] | Shopify: checkout, `cancel_url`, the return after `nextAction`. Provider: the whole payment UX [PROC][OFF*] | `payment_session_url`, `refund_session_url` (required). Capture/void URLs only if manual capture is offered. `confirmation_callback_url` if it does inventory confirmation [CONF] |
| **Credit card** `payments.credit-card.render` | card purchases "directly in Shopify checkout … while the customer remains on the storefront" [CC] | **Shopify** collects the card. The PAN is sent ECIES-encrypted to the provider's certificate (`encrypted_message`, `ephemeral_public_key`, `tag`, `fingerprint`) [REF]. The buyer goes elsewhere only for 3DS, in an iframe through `paymentSessionRedirect` [PROC] | Shopify: card form, encryption, iframe, CSP `frame-ancestors 'none'` [CC]. Provider: decrypts in a PCI DSS environment, authorizes [REF] | Payment, refund, capture **and** void URLs are all required. `encryption_certificate_fingerprint` is required. Confirmation URL is required when 3DS is supported. PCI AOC is needed before access [CONF][CC][CERT] |
| Credit card "with UI extensibility" | extra checkout fields, e.g. installment details, collected "before a payment is initiated" [OV] | Shopify card form plus partner fields | — | — |
| **Custom credit card** `payments.custom-credit-card.render` | "define the specific credit card hosted fields needed to process custom credit cards" [OV] | Shopify hosted fields `checkout_hosted_fields` ∈ {`name`,`expiry`,`verification_value`,`issue_date`,`issue_number`}, rendered with the partner's checkout UI extension [CONF] | as for credit card | as for credit card, plus `ui_extension_handle` and `checkout_payment_method_fields` [CONF] |
| **Alternative / custom onsite** `payments.custom-onsite.render` (closed beta) | non-card methods with fields gathered "upfront, directly on the checkout page" and "with or without redirecting" [ALT][OV] | Buyer types into the partner's checkout UI extension at target `purchase.checkout.payment-option-item.details.render`. Values reach the provider as `payment_method.data.attributes` [ALT]. A redirect is optional ("It isn't necessary to specify a redirect URL unless additional information is required") [ALT]. A post-"Pay now" challenge goes through `paymentSessionModal` [ALT] | Shopify renders the extension and owns the modal UI ("not customizable by partners") [ALT]. The fields must match the declared `checkout_payment_method_fields` [ALT] | like offsite. Modal needs extra scopes `write_payment_session_modals`/`read_payment_session_modals` [ALT] |
| **Redeemable** `payments.redeemable.render` (closed beta, Plus only) | third-party gift cards, store credit [RED*][OV] | UI extension at `purchase.checkout.gift-card.render` calls `applyRedeemableChange`. Shopify calls `balance_url` before checkout completes, then a normal payment session [RED*] | Shopify applies the balance to the checkout and "owns displaying errors to buyers" [RED*]. `supported_payment_methods` only `gift-card`. `supports_3ds` and other card props don't apply. `confirmation_callback_url` is "Not implemented" [CONF] | `balance_url`, `ui_extension_handle`, `checkout_payment_method_fields` [CONF] |
| Card present / POS | **None in this slice.** Admin has `EMV_AUTHORIZATION` [ADM:OrderTransactionKind] and `PointOfSaleDevicePaymentSession`, which is cash-drawer accounting [ADM]. Payment customization Functions "don't currently run" in POS [CPAY] | — | — | — |

Notes:
- "The option to build a custom payment extensions is limited to eligible Shopify Plus Merchants only" [OV].
- Supported method families: cards, BNPL/installments/financing, bank transfers and online banking, crypto, cash and ATM, and wallets with limits [OV].
- Supported operations: Charge, Refund, Authorize, Capture, Void [OV].
- Inference: the five kinds really vary along two axes. (1) Where buyer input is captured: Shopify-owned card form, Shopify-hosted declared fields, or the provider's page. (2) Whether a pre-payment provider call exists (`balance_url`). The asynchronous outcome protocol is identical across all kinds.

---

## 2. The contract

### 2.1 Transport, trust, versioning
- **Shopify → app:** HTTP POST to the per-operation URL from the extension config, over **mTLS**. Shopify presents its client certificate. The app validates it against Shopify's self-signed CA and presents a trusted-CA certificate [CONS]. Payment operation requests carry **no `hmac`**; HMAC applies only to install redirects [REQS].
- Headers: `Shopify-Shop-Domain`, `Shopify-Request-Id`, `Shopify-Api-Version` [REF].
- **App → Shopify:** GraphQL at `https://{shop}/payments_apps/api/{version}/graphql.json` with an OAuth token in `X-Shopify-Access-Token` [API]. Rate limit: 27,300 points/s, or 54,600 on Plus [API].
- The app must send mutations in the same API version it chose to receive [REQS]. `unstable` is not allowed in production [REQS].
- "The Payments Apps API doesn't support sending additional information back to Shopify" [API]. The only query is `publicApiVersions` [S:QueryRoot].

### 2.2 Session types

| Session | Request (Shopify → app) | Synchronous reply | Async finalisation | Allowed final states |
|---|---|---|---|---|
| Payment (offsite) | full payment payload [REF] | HTTP 2xx + `{"redirect_url"}` (<8192 bytes) [REF] | resolve / reject / pending, optionally after confirm | `RESOLVED`, `REJECTED`. `PENDING` is non-final [S:PaymentSessionStateCode][PROC] |
| Payment (card) | payload + encrypted card + `client_details` when 3DS is on [REF] | 2xx, empty body [REF] (template returns 201 [CC]) | redirect → confirm → resolve/reject. **Pending not allowed** (`UNSUPPORTED_PAYMENT_METHOD`: "Pending is not supported for credit card payment methods") [MUT*:PaymentSessionPendingUserErrorCode] | same |
| Payment (custom onsite) | payload with `payment_method.type: custom-onsite`, `data.attributes[]`, `cancel_url` [ALT] | 2xx with an optional `redirect_url` [ALT] | modal / confirm / resolve / reject / pending | same |
| Payment (redeemable) | `payment_method.type: redeemable`, attributes such as `card_number`, `pin` [RED*] | 2xx | resolve/reject (documented reject code: `PROCESSING_ERROR`) [RED*] | same |
| Balance (redeemable) | `id` (idempotency key), `currency`, `test`, `merchant_locale`, `payment_method{type:"redeemable", data.attributes}` [RED*] | **synchronous outcome**: 2xx with `{"result":"success","balance":{"value","currency"}}`, or 2xx with `{"result":"failure","reason": REDEEMABLE_INVALID / _INSUFFICIENT_BALANCE / _EXPIRED / _DISABLED, "message"}` [RED*] | none | — |
| Refund | `id`, `gid`, `payment_id`, `amount`, `currency`, `test`, `merchant_locale`, `proposed_at` [REF] | **HTTP 201** with empty body [REF] | `refundSessionResolve` / `refundSessionReject` [PROC] | `RESOLVED`/`REJECTED` only [S:RefundSessionStateCode] |
| Capture | same fields; `payment_id` is the authorized payment [REF] | 201 | `captureSessionResolve`/`Reject` | `RESOLVED`/`REJECTED` [S:CaptureSessionStateCode] |
| Void | `id`, `gid`, `payment_id`, `test`, `merchant_locale`, `proposed_at` (no amount) [REF] | 201 | `voidSessionResolve`/`Reject` | `RESOLVED`/`REJECTED` [S:VoidSessionStateCode] |
| Confirm callback | `id`, `gid`, `confirmation_result: Boolean` [REF] | 200/201. "Shopify doesn't read the response body"; any other status "is treated as a provider error that fails the payment attempt" [ALT][CC] | resolve/reject/pending | — |
| Verification | No request reference in the corpus. Mutations only: `verificationSessionRedirect`/`Resolve`/`Reject` [S] | — | resolve can carry `VerificationSessionCardInput` (`bin`, `last4`, `expirationMonth/Year`, `networkTransactionId`, `wallet`, `descriptor`…) [S][MUT*:VerificationSessionCardInput] | `REDIRECTING`/`REJECTED`/`RESOLVED`. User error `VERIFICATION_SESSION_TIMEOUT` [S] |

Inference: Verification is card verification with optional 3DS, used to put a card on file (for example deferred or B2B vaulted cards [TERMS]). It is a zero-amount sibling of the payment session.

### 2.3 Payment request fields [REF]
- `id`: "Unique identifier for the payment attempt. Used as the idempotency key… must be surfaced to the merchant so that they can correlate Shopify orders with payments".
- `gid`: used in mutations.
- `group`: "shared across payment sessions, representing attempts to complete the same checkout or deferred payment capture".
- `session_id`: shared by sessions in the same group, buyer session and payment details (2024-10+).
- `amount`: decimal string with a "." separator.
- `currency`: ISO 4217.
- `test`.
- `merchant_locale`: BCP 47.
- `payment_method{type,data}`.
- `proposed_at`: orders attempts within a group.
- `customer{email|phone_number (at least one), locale, billing_address, shipping_address (not for digital)}`.
- `transaction_metadata{shipping{price,discount}, tax_amount, order_level_discount, localized_fields[{key,country_code,value}]}`: each item is included only if the app has access to that data. Example: Brazil CPF.
- `kind`: `sale` | `authorization`. With `sale` you "capture the funds instantly". With `authorization` you "place a hold on the funds and capture them later". The value is "set based on the merchant's configuration", and is always `sale` if the provider doesn't support separate auth/capture.
- `client_details{ip_address,user_agent,accept_language}`: card, when 3DS is supported.
- Card `moto` flag (2024-07+).
- **Not sent:** order ID, checkout ID, line items. "Shopify doesn't include an order ID"; merchants match through the payment `id`, which appears in the **Payment References** export column [REF][REQS].
- A sample payload also shows an undocumented `fx_reconciliation{currency}` [ALT].

### 2.4 Outcome mutations [S][MUT*]
- `paymentSessionResolve(id, authorizationExpiresAt?, networkTransactionId?, authentication?, paymentDetails?)`
  - `authorizationExpiresAt` "must be provided if the payment session request `kind` is `authorization`".
  - `networkTransactionId` "must provide… if available".
  - `authentication` is the 3DS data, required "if and only if the Redirect mutation has been called and the payment method is credit card" [CC][MUT*:paymentSessionResolve].
  - `paymentDetails.cardNotPresent{avsResultCode, cvvResultCode}` [S:PaymentSessionCardNotPresentInput].
- `paymentSessionReject(id, reason{code, merchantMessage?, source?}, authentication?, paymentDetails?)`.
- `paymentSessionPending(id, pendingExpiresAt!, reason!)`. `pendingExpiresAt` is "recommended to be within 3 days". Both `sale` and `authorization` payments may pend. Pending must later be finalised with resolve/reject [MUT*:paymentSessionPending].
- `paymentSessionRedirect(id, redirectUrl)`: card 3DS only. Offsite and onsite get `REDIRECT_NOT_SUPPORTED_FOR_OFFSITE` / `_ONSITE` [MUT*:PaymentSessionRedirectUserErrorCode].
- `paymentSessionConfirm(id)`: "Shopify determines if the payment can be authorized and sends a POST request… delivering the confirmation result" [MUT*:paymentSessionConfirm].
- `paymentSessionModal(id, action{qrCode{code,data} | external{data}}, expiresAt?)` [S:ModalAction][S:QrCode][S:External].
- `refundSessionReject(reason{code: PROCESSING_ERROR, merchantMessage})`. Same shape for void. Capture codes are `AUTHORIZATION_EXPIRED` | `PROCESSING_ERROR` [S]. `merchantMessage` is "a localized error message presented to the merchant" [ALT].
- `paymentsAppConfigure(externalHandle?, ready!)` (see §3).

### 2.5 Payment session state machine
States: `REDIRECTING`, `CONFIRMING`, `BUYER_ACTION_REQUIRED`, `PENDING`, `RESOLVED`, `REJECTED` [S:PaymentSessionStateCode]. Transitions as documented:

```
(open, after 2xx) ──redirect(card 3DS)──▶ REDIRECTING ──confirm──▶ CONFIRMING ──(Shopify POST confirmation_result)──▶ resolve|reject|pending
(open) ──modal(onsite)──▶ BUYER_ACTION_REQUIRED ──▶ resolve|reject|pending     (or Shopify expires it)
(open) ──confirm(offsite/onsite inventory)──▶ CONFIRMING ──▶ resolve|reject|pending
(open) ──resolve|reject|pending
PENDING ──▶ RESOLVED | REJECTED        (pend again ⇒ PENDING_INVALID_STATE only if already final)
RESOLVED, REJECTED: final, "can't be changed" [PROC]
```

- `INVALID_STATE_TRANSITION` is a user error on confirm, modal and redirect [S].
- With confirmation enabled, "Shopify fails the `Resolve` and `Reject` mutation calls if Shopify hasn't yet sent a confirmation result". Once it has sent one, it won't fail them, "even if Shopify hasn't received a response from the partner" [PROC].
- **Which states create an order:** "If the payment is successful or pending, Shopify creates an order". "Shopify creates the order only after the buyer completes verification and your payment app resolves or marks the payment as pending" [ALT]. A rejection sends the buyer back to checkout [ALT].
- Pending orders: "merchants might be restricted from editing, canceling, or manually capturing payment for the order until the payment is finalized" [ALT][OFF*].

### 2.6 Rejection semantics
- `PaymentSessionStateRejectedReason` has 36 codes [S]. They cover:
  - amount/currency: `AMOUNT_TOO_LARGE`, `AMOUNT_TOO_SMALL`, `INVALID_AMOUNT`, `INVALID_CURRENCY`
  - authentication: `AUTHENTICATION_FAILED`, `AUTHENTICATION_REQUIRED`
  - issuer: `CALL_ISSUER`, `DO_NOT_HONOR`, `PICK_UP_CARD`, `INSUFFICIENT_FUNDS`, `TRANSACTION_LIMIT_EXCEEDED`
  - instrument: `INVALID_PAYMENT_METHOD`, `INSTRUMENT_DECLINED`, `INCORRECT_PIN`…
  - risk: `FRAUD_SUSPECTED`, `HIGH_RISK_FRAUD_SUSPECTED`, `CARD_TESTING`, `MERCHANT_RULE`
  - process: `CANCELLED_PAYMENT`, `CONFIRMATION_REJECTED`, `INVALID_REQUEST`, `MERCHANT_ACCOUNT_ERROR`, `PROCESSING_ERROR`, `RETRY_DECLINED`, `INVALID_PURCHASE_TYPE`, `PAYMENT_METHOD_UNSUPPORTED`
  - `RISKY` is deprecated [MUT*:PaymentSessionStateRejectedReason]
- `source` ∈ {`NETWORK` ("payment network or the issuer"), `PROVIDER`} [MUT*:PaymentSessionStateRejectedSource].
- **Reject means the attempt is over, not the buyer.**
  - "Rejecting a payment is final… The payments app should retry a failed user attempt and complete the payment before calling `paymentSessionReject`". For example, don't reject when the user doesn't interact, cancels, or mistypes a CVV [ALT].
  - Buyer cancellation goes through `cancel_url`: "Don't use the `paymentSessionReject` mutation to cancel the payment; otherwise, the customer will be unable to pay again with your provider" [ALT][OFF*].
- Refund, capture and void rejections should be used "only… in the case of final and irrecoverable errors. Otherwise… re-attempt" [ALT][CC].

### 2.7 Pending, expiry, authorization windows
- Pending reasons: `BUYER_ACTION_REQUIRED`, `MERCHANT_ACTION_REQUIRED`, `NETWORK_ACTION_REQUIRED`, `PARTNER_ACTION_REQUIRED` [MUT*:PaymentSessionStatePendingReason].
- "Some payments can take several days to complete" [ALT].
- Expiry bounds: `EXPIRED_PENDING_EXPIRES_AT` (in the past), `OUT_OF_RANGE_PENDING_EXPIRES_AT` ("exceeded the default pending expiry limit") [MUT*:PaymentSessionPendingUserErrorCode].
- The corpus does not say what Shopify does when `pendingExpiresAt` passes.
- `authorizationExpiresAt` is stored on the session [S:PaymentSession] and mirrored on `OrderTransaction.authorizationExpiresAt` [ADM:OrderTransaction]. Inference: this is the same datum. A capture after expiry is rejected with `AUTHORIZATION_EXPIRED` [S:CaptureSessionStateRejectedReason].
- `multiple_capture` lets merchants "partially capture an authorized payment multiple times, up to the full authorization amount" [CONF]. It surfaces as `OrderTransaction.multiCapturable` [ADM] (Inference: linked).

### 2.8 3-D Secure and liability
- `PaymentSessionThreeDSecureAuthentication` takes exactly one of:
  - `authenticationData{authenticationFlow: CHALLENGE|FRICTIONLESS|UNKNOWN, chargebackLiability: MERCHANT|UNKNOWN, transStatus: A|I|N|R|U|Y, transStatusReason?, version: V1_0…V2_3|UNKNOWN, dsTransactionId?}`
  - `partnerError: PROCESSING_ERROR` [S]
- `chargebackLiability: MERCHANT` means the merchant stays liable, for example after an SCA exemption. `UNKNOWN` "cannot be used if trans_status is N or R" [MUT*:PaymentSessionThreeDSecureChargebackLiability].
- `transStatus I` can't be combined with `CHALLENGE` [MUT*:PaymentSessionThreeDSecureTransStatus].
- On `R` or an error the app may reject with `AUTHENTICATION_FAILED`, without calling confirm [PROC][MUT*:PaymentSessionStateRejectedReason].
- The redirect must arrive "within a given timeout". After that the buyer is sent back and later redirects fail with `BUYER_ALREADY_REDIRECTED_BY_SHOPIFY` [CC].
- The app must navigate back "using the parent browsing context" [PROC].
- 3DS is mandatory where the country mandates it [REQS][CONF].

### 2.9 Next action
- Resolve, reject and pending return `nextAction{action: REDIRECT, context: PaymentSessionActionsRedirect{redirectUrl}}`, or `nil` when "no next action is expected" [ALT][S:PaymentSessionNextAction].
- After pending, "you must redirect the customer back to Shopify, using `redirectUrl` in `nextAction`" [MUT*:paymentSessionPending].
- After confirm, Shopify returns a null `nextAction`; the app "must wait for Shopify to confirm" [ALT].
- Inference: Shopify, not the provider, owns where the buyer goes next, even after an offsite step.

### 2.10 Buyer action modal (onsite, API 2025-07+) [ALT]
- Shopify "presents a verification challenge to the buyer on their checkout". Example: scanning a QR code, or `external` "message for buyers to take an action on an external device" [S:External].
- `expiresAt` must be ≤ Shopify's maximum: "default maximum timeout of `7 minutes`" plus a 5 s buffer. On expiry "Shopify marks the payment as expired" and returns the buyer to checkout.
- If the buyer closes the modal they go back to checkout. A re-attempt with the same method makes Shopify "initiate a new payment session".
- The modal UI is "controlled by Shopify and is not customizable". User errors include `UNSUPPORTED_PAYMENT_METHOD_FOR_MODAL` and `OUT_OF_RANGE_MODAL_EXPIRES_AT` [MUT*:PaymentSessionModalUserErrorCode].
- **The modal displays; it does not collect input.** Inference, since there is no input-capture field in [S:ModalAction].

### 2.11 The confirming step (inventory and business re-validation) [PROC][ALT][OFF*][CC]
- The app calls `paymentSessionConfirm` once the buyer has done their part, before it processes funds.
- Shopify checks "that inventory is still available and that discount codes are still valid", then POSTs `confirmation_result` to `confirmation_callback_url`.
- If the result is `false`, the app must reject with `CONFIRMATION_REJECTED`.
- Inventory checks only work if the merchant tracks inventory and disables "Continue selling when out of stock" [PROC].
- **3-minute window:** "Shopify expects the payment to be resolved/rejected within 3 minutes of the successful confirmation callback". After that Shopify re-runs confirmation on resolve, and "may issue a refund/void request". For this reason `refund_session_url` is enforced for apps that set `confirmation_callback_url` [ALT][CONF].
- It is only available with one-page checkout or Extensions in Checkout [PROC].

### 2.12 Idempotency, retries, timeouts, unknown outcomes [CONS][REF][CC]
- Inbound idempotency: requests with the same `id` "are identical". "Regardless of how many requests with the same idempotency key are sent, the result must be the same". "Idempotency keys don't expire".
- Outbound idempotency is per mutation per `id`: a repeat returns the same response. Mutually exclusive mutations (resolve vs reject) are **first-writer-wins**, and later incompatible calls fail with `user_error`. A later identical resolve "will succeed, but the `Details` argument will be ignored" [MUT*:paymentSessionResolve].
- Inbound timeouts: all Shopify→app requests (payment, refund, capture, void, balance) "are subject to timeouts… Shopify retries the request several times".
  - Payment that keeps failing: "the customer needs to retry their payment through Shopify checkout".
  - Refund, capture or void that keeps failing: "the user needs to manually retry… in the Shopify admin" [REF].
- Outbound retry policy (mandatory): on 5xx or disruption, retry up to 18 times over 24 h on the schedule [0 s, 5 s, 10 s, 30 s, 45 s, 1 m, 2 m, 5 m, 12 m, 38 m, 1 h, 2 h] + [4 h]×5. Meanwhile, tell the buyer "Their payment is processed, but Shopify is unreachable" and that they will be notified [CONS].
- **Unknown outcome at checkout (card):** "customer is redirected to the order confirmation page when a payment times out… the order status is automatically set to Pending… You should still finalize the payment" [CC].
- Inference: Shopify never polls the provider. Closing an in-doubt attempt is entirely the provider's push duty. Shopify degrades to "order exists, payment pending" or "buyer retries as a new session in the same `group`".

---

## 3. Merchant onboarding and configuration

**Lifecycle** [OV][ONB]:
1. Install via the installation URL or the public gateway list.
2. OAuth grant.
3. Redirect to the app's configuration page, with a "provider isn't ready" banner.
4. Merchant configures the provider account.
5. App calls **`paymentsAppConfigure(ready: true, externalHandle)`**.
6. Redirect to `https://{shop}.myshopify.com/services/payments_partners/gateways/${api_key}/settings`.
7. Merchant activates and picks the methods shown as icons.
8. Merchant deactivates any legacy gateway.

Details:
- `externalHandle`: "A username or identifier associated with the account that the merchant has used with the partner. It displays in the Payments section in the Shopify admin" [MUT*:PaymentsAppConfiguration].
- "If you set `ready: false` after the app is installed and activated… the request will fail" [ALT][RED*].
- Deactivation: buyers can't select the method, but "merchants can still manage refunds and captures". **Uninstall "breaks order management"**, and reinstalling needs `paymentsAppConfigure` again [ONB].
- Inference: merchant credentials never reach Shopify. Shopify only knows `ready`/`externalHandle`.

**Declarable configuration** (`shopify.extension.toml`) [CONF][ALT][CC][RED*]:
- Identity: `api_version`, `name` (translatable `t:`), `handle`, `type`, `uid`, `merchant_label` (≤50 chars, admin search), `buyer_label` + `[[extensions.buyer_label_translations]]{label, locale}`.
- Endpoints: `payment_session_url`, `refund_session_url`, `capture_session_url`, `void_session_url`, `confirmation_callback_url`, `balance_url`.
- Coverage: `supported_countries` (ISO alpha-2; must match the listing), `supported_payment_methods` (activemerchant payment_icons names; redeemable only `gift-card`).
- Capabilities: `supports_3ds`, `supports_installments`, `supports_deferred_payments`, `test_mode_available`, `multiple_capture`, `supports_moto`.
- Card crypto: `encryption_certificate_fingerprint`. The value `"Test Certificate"` makes Shopify send a fixed test payload [TCERT].
- Checkout UI: `ui_extension_handle`, `[[extensions.checkout_payment_method_fields]]{key, type, required}`, `checkout_hosted_fields`.
- `[[extensions.targeting]] target`.

**Not declarable in this slice:** supported currencies, min/max amounts, fees, partial-refund support, refund-unsupported. Inference: these are enforced per session by rejecting (`INVALID_CURRENCY`, `AMOUNT_TOO_SMALL/LARGE`) or are left to contracts.

- Discovery: "the payment methods and locations offered… is the only information that's used to surface the extension to merchants" [REQS].
- Merchant-side switches outside the app: test mode, activation, and the payment capture method (automatic, manual, or "Automatically when order is fulfilled"), which decides `kind` [REF][RED*][ALT].

**Encryption certificates** (card) [CERT]: EC prime256v1 CSR → Shopify-signed certificate. States: `Waiting for approval` (up to 2 weeks), `Usable`, `About to expire` (≤30 d), `Expired`, `Revoked`, `Rejected`. Valid 1 year. The private key must live in a PCI environment, and an expired or revoked certificate means the app "won't be able to process payments".

---

## 4. Requirements, review, and what Shopify reserves

**Approval** [REV]:
- Invitation-only Payments Partner application.
- Revenue-share agreement signed before app review, or the app is rejected.
- App review.
- App states:
  - `Development`: dev stores, test mode only.
  - `Hidden`: installable by URL.
  - `Generally Available`: listed. Criteria: "at least 50 Shopify stores and has processed over 1,000,000 USD".
  - `Not Installable`: failing requirements; existing shops keep working.
- Card extensions also need a PCI AOC [CC].

**Provider duties** [REQS]:
- "Securely collecting a customer's payment information… PCI requirements", "Processing the payment according to parameters specified by Shopify", "Redirecting the customer to Shopify", "**Settling transactions within five days**".
- Risk and fraud monitoring is the Partner's job; Shopify may delist.
- Features: "Merchants can charge, refund, and process test transactions", plus SCA compliance.
- Technical: idempotency, retry policy, mTLS, HMAC on install, rate limits, a supported API version, 3DS where mandated, compliance webhooks.
- Merchant experience: "99.95%" availability 24/7, "respond within 2 hours" to outages, support for all merchants.
- Commercial: transparent pricing, no teaser rates, no calling fees "Shopify fees", merchants may terminate "with a 7-day notice period without penalty".
- Revenue share on total GMV. Monthly invoices, converted daily to USD via xe.com. Waived until monthly volume first exceeds $150,000 USD.

**Prohibited / reserved to Shopify** [REQS]:
- Using any Shopify API other than the Payments Apps API and mandatory webhooks.
- Using **payment customization functions**.
- Requesting network-access or protected-customer-data scopes.
- Storing credentials beyond the original transaction.
- Reselling access; fake merchants or orders.
- Processing **Apple Pay, Google Pay, Shop Pay, PayPal, Alipay** ("Shopify has a direct connection with these providers").
- Limitations: "Line items, order ID, and checkout ID aren't available". Extensions aren't in the App Store.

Also reserved to Shopify:
- The buyer-facing modal UI [ALT] and the error display for redeemables [RED*].
- The decision to proceed (confirm) [PROC].
- Accelerated wallet buttons: closed shadow DOM, for Shop Pay, Apple Pay, Google Pay, PayPal and Amazon Pay [TACC].
- Mobile accelerated checkout with Shop Pay and Apple Pay [MACC].

---

## 5. Checkout customisation: the payment customization Function

- **Target / entry point:** `cart.payment-methods.transform.run` → `CartPaymentMethodsTransformRunResult{operations}` [CPF][FN].
- The merchant activates it by creating a `PaymentCustomization` (Admin `paymentCustomizationCreate`, scope `write_payment_customizations`). It is configured through metafields on that owner and edited in an app UI at `[ui.paths]` under **Settings > Payments > Payment method customizations** [CPF][CFG][UI][UX][ADM:PaymentCustomization].

**Inputs** [FN:Input]:
- `cart`:
  - `cost{subtotal,total,totalTax,totalDuty}`
  - `lines` (merchandise, `sellingPlanAllocation`, parent relationship)
  - `deliveryGroups`, including `selectedDeliveryOption.deliveryMethodType` ∈ SHIPPING / PICK_UP / RETAIL / LOCAL / PICKUP_POINT / NONE
  - `buyerIdentity`: `customer` with tags, `numberOfOrders`, `amountSpent`, metafield; `purchasingCompany` (B2B company, location, contact); email/phone; `isAuthenticated`
  - `billingAddress`, `localizedFields`, `discountApplications`, `poNumber`, `retailLocation`, cart `attribute`/`metafield`
- `localization{country, language, market}`
- `paymentCustomization.metafield` (config)
- **`paymentMethods[{id, name, placements}]`**, with placement ∈ `ACCELERATED_CHECKOUT` | `PAYMENT_METHOD` [FN:PaymentCustomizationPaymentMethod]
- `presentmentCurrencyRate`
- `shop{localTime, metafield, metaobject}`

Inference: a method is identified only by an opaque id and display name. The Function sees no provider kind, capabilities or fees. The tutorial matches by name substring ("Cash on Delivery") [CPF].

**Operations** [FN:Operation]:
- `paymentMethodHide{paymentMethodId, placements?}`
- `paymentMethodMove{paymentMethodId, index}`
- `paymentMethodRename{paymentMethodId, name}`
- `paymentTermsSet{paymentTerms?}` (§6)
- `orderReviewAdd{reason}`: B2B checkout is "submitted as a draft for review" [REVW]

**Fixed by Shopify** [CPAY][CPF]:
- Plan and geography restrictions. When restricted, the input still lists all methods but operations "will not take effect".
- Hiding by placement is Plus only; elsewhere hide removes the whole method.
- Methods with logo names (Shop Pay, Apple Pay, Google Pay, all wallets, the native gift card field) can't be renamed.
- Wallets can be removed but not reordered.
- Not run in POS. In Shop Pay only the gift card field is affected.
- At most 25 active functions per store.
- Review requirement applies to B2B only; not to orders, draft-order invoices or draft calculations.

**Delegation in summary:** visibility, order, naming, terms and review are delegated to merchant-installed apps. Which methods exist, wallet behaviour, and provider processing are not. Providers themselves may not customise the list [REQS].

---

## 6. Payment terms and deferred collection at checkout

**`PaymentTerms` input** (exactly one) [FN]:
- `fixed{dueAt, deposit?}`
- `net{dueInDays, issuedAt?, deposit?}`
- `event{trigger: INVOICE_SENT | ORDER_FULFILLED | FULFILLMENT_CREATED, deposit?}`

`Deposit{percentage}`. `PaymentTermsSetOperation` is "a request to set, modify, or remove payment terms" and `paymentTerms` is nullable [FN]. Tutorial: B2B carts ≥ $500 get fixed terms with a 50% deposit [TERMS].

**What checkout does** [TERMS][CPAY]:
- Terms "only apply to the specific order" and don't change the buyer's defaults.
- Existing terms aren't in the input.
- Plus only; not on accelerated checkouts.
- **D2C with terms: "don't support any pay now options… only see the option to defer"**. B2B also gets vaulted cards.
- If no function sets terms, B2B uses the company location's terms (e.g. net 45) [TERMS].
- Event terms plus **Automatically when fulfilling**: D2C captures per fulfillment (`FULFILLMENT_CREATED`) or on full fulfilment (`ORDER_FULFILLED`). B2B has no auto-capture; the merchant captures manually.
- Deferred purchase options (pre-order, try before you buy) follow their own rules for due dates and deposits [TERMS].

**Order-side record** [ADM]:
- `PaymentTerms{paymentTermsType: RECEIPT|NET|FIXED|FULFILLMENT|UNKNOWN, dueInDays, due, overdue, paymentSchedules}`
- `PaymentSchedule{amount, balanceDue, totalBalance, issuedAt, dueAt, completedAt, due}`
- `DepositConfiguration = DepositPercentage`
- Admin `paymentTermsCreate/Update/Delete`

Inference: `INVOICE_SENT` ↔ `RECEIPT` and both fulfillment triggers ↔ `FULFILLMENT`. This is not stated.

**Provider link:**
- `supports_deferred_payments` flag [CONF].
- `group` covers "deferred payment capture" attempts [REF].
- Inference: a later collection against terms or a deposit balance arrives at the provider as an ordinary payment session in the same `group`.
- Installments are a separate idea: `supports_installments` [CONF]. Shop Pay Installments covers 50–3,000 USD in 4 interest-free payments, with the Liquid `payment_terms` banner [INST].

---

## 7. How provider outcomes become order records

| Provider-side | Order-side (`OrderTransaction` [ADM]) |
|---|---|
| payment session `kind=sale`, resolved | `kind: SALE`, `status: SUCCESS` (Inference) |
| `kind=authorization`, resolved + `authorizationExpiresAt` | `AUTHORIZATION`, `authorizationExpiresAt`, `manuallyCapturable`, `multiCapturable` (Inference) |
| capture session resolved | `CAPTURE` with `parentTransaction` = authorization ("for example the authorization of a capture") [AREF*:OrderTransaction]. The order shows **Paid** [ALT] |
| void session resolved (triggered by order cancel [ALT]) | `VOID` = "cancelation of an authorization". The order shows **Voided** [ALT][AREF*:OrderTransactionKind] |
| refund session resolved (`payment_id` = original authorization id for captured payments [REF]) | `REFUND`. The order shows **Refunded** [ALT] |
| pending | order created with pending payment [ALT][CC]. `OrderDisplayFinancialStatus.PENDING` exists [ADM] (Inference: status `PENDING`) |
| rejected | `FAILURE` + `errorCode`. Inference: `OrderTransactionErrorCode` contains every `PaymentSessionStateRejectedReason` except `CONFIRMATION_REJECTED`, `HIGH_RISK_FRAUD_SUSPECTED`, `INVALID_REQUEST`, `RISKY`. It adds `AUTHORIZATION_EXPIRED`, `PAYMENT_PROVIDER_ERROR`, `GENERIC_ERROR`… [S vs ADM, compared] |
| timeout at checkout | order exists with status Pending [CC]. `AWAITING_RESPONSE`/`UNKNOWN` statuses exist [AREF*:OrderTransactionStatus] |

- Shopify's correlation key is the payment session `id`. It is shown to merchants and exported as **Payment References** [REF]. Inference: it is `OrderTransaction.paymentId` ("The payment ID associated with the transaction") [AREF*].
- **The provider's own reference has no place to go.** The API accepts only `networkTransactionId`, card AVS/CVV and 3DS data [S]. `receiptJson` is "gateway-specific and not a stable contract" [AREF*].
- `test` flows through to `OrderTransaction.test` [ADM].
- **Money movement:** the provider settles to the merchant directly, "within five days" ("help merchants handle settlement and payouts") [REQS]. Shopify takes a revenue share on GMV from the **Partner**, invoiced monthly [REQS].
- Provider fees aren't sent. Inference: `OrderTransaction.fees`/`TransactionFee` only reflects what Shopify knows.
- `settlementCurrency`/`settlementCurrencyRate` exist on the transaction [ADM] but can't be set by payments apps (Inference).

---

## 8. Invariants and rules worth copying

1. **Command/outcome split:** the synchronous reply only acknowledges receipt; the outcome is a separate, idempotent, retried message [PROC][CONS].
2. **Attempt identity = idempotency key that never expires.** Attempts group per checkout (`group`) and are ordered by `proposed_at`. Same-details attempts share `session_id` [REF][CONS].
3. **Finality:** resolve and reject are terminal and mutually exclusive, first writer wins, and repeats are harmless [PROC][CONS][MUT*].
4. **Reject ≠ cancel:** buyer abandonment keeps the method retryable; reject closes it [ALT].
5. **Every waiting state has a deadline:** redirect timeout, modal ≤7 min, pending (recommended ≤3 days with a hard limit), authorization expiry, a 3-minute confirm→finalise window [CC][ALT][MUT*].
6. **Re-validate before the irreversible step** (confirm), with a compensating refund/void if the window lapses [ALT].
7. **Only resolved or pending creates the order.** Rejected never does [ALT].
8. **Follow-on operations reference the original payment** (`payment_id`) and have only RESOLVED/REJECTED outcomes [REF][S].
9. **Capabilities are declared statically**; merchant readiness is a runtime flag [CONF][S:PaymentsAppConfiguration].
10. **Merchant credentials stay with the provider.** The platform holds only a display handle [MUT*:PaymentsAppConfiguration].
11. **Card data is encrypted end-to-end to the provider certificate**, so the platform never sees decrypted PAN downstream [REF][CERT].
12. **Providers can't steer the method list or use other platform APIs** [REQS].
13. **Deactivate, don't uninstall:** reversals stay possible for existing orders [ONB].
14. **Closed vocabularies** for reject, pending, liability, 3DS and user errors, so the platform can reason across providers [S].

---

## 9. Class-level questions (provider-agnostic)

1. **[lifecycle]** What is the minimum asynchronous contract a provider must honour so that every attempt reaches a definite outcome, including after timeouts? Who drives an in-doubt attempt to closure: provider push (Shopify) or platform pull?
2. **[information]** Which identifier is the idempotency key end to end (platform → adapter → rail)? What does the adapter owe when the rail can't accept an external key?
3. **[lifecycle]** Which attempt states are terminal, which intermediate states are enough to create the order (Shopify: resolved **or** pending), and which never create one?
4. **[rules]** May an order (the obligation) exist while the financial outcome is unknown? What can the merchant do to such an order (edit, cancel, capture)?
5. **[events]** What must the platform re-validate (stock, discounts, price) between buyer authentication and irreversible debit? How long is the "go" signal valid, and what compensates when it lapses?
6. **[actors]** For each credential (card, OTP, voucher/payment code, phone, PIN), who collects it (platform UI, declared field, provider page, external device), and who carries the regulatory and PCI liability?
7. **[variability]** What capability profile must a provider declare: countries, currencies, amount limits, auth/capture, multi-capture, partial or no refunds, 3DS/SCA, deferred, installments, vouchers/balance, test mode? Which items are per provider, and which per merchant account?
8. **[extension]** How does a merchant bind their own provider account (credentials, readiness, display handle) without the platform storing provider secrets? What happens on reinstall?
9. **[information]** What provider evidence must the transaction record (provider reference, network id, authentication result, liability shift, rejection source, AVS/CVV) to support reconciliation and disputes?
10. **[rules]** What closed vocabulary of reject and pending reasons must providers map into? How is "buyer abandoned, may retry" kept apart from "attempt rejected"?
11. **[lifecycle]** How do capture, void and refund reference the original attempt, and which partial or multiple operations are allowed against one authorization?
12. **[quality]** What delivery guarantees (retry schedule, idempotent outcome messages, first-writer-wins) prevent double charges and contradictory outcomes?
13. **[scope]** Which methods and wallets does the platform reserve to itself, and which method-list decisions are delegated to merchants or apps but forbidden to providers?
14. **[variability]** What does the method-selection logic see per checkout (cart, buyer, B2B, market, delivery type, method identity and capabilities)? Is the method opaque, as in Shopify (`id`, `name`)?
15. **[rules]** What deferred arrangements (net, fixed, event terms, deposits) can an order carry? What triggers collection, and how does a terms checkout restrict pay-now methods?
16. **[events]** What happens when a provider can't reverse funds (no refund API, or non-reversible wallet debit)? Is "refund settled outside the provider" a modelled outcome?
17. **[lifecycle]** For each waiting state (redirect, buyer action, pending, authorization, confirmation), what is the expiry and the platform's default action when it expires?
18. **[actors]** Who can operate on past payments after a provider is deactivated or uninstalled, and how are orphaned obligations prevented?
19. **[quality]** Which SLA, settlement window, incident response and support duties bind a provider? How is non-compliance enforced (listing states, not-installable)?
20. **[information]** What order and buyer context does the platform disclose to providers (Shopify: no line items or order id; tax, shipping and discounts only by data access)? On what basis?
21. **[extension]** How can a provider add buyer interaction inside checkout (declared fields, hosted fields, display-only modal) without running arbitrary code or network calls in checkout?
22. **[variability]** How are test and live mode carried end to end (request flag, transaction flag, merchant toggle) and kept from mixing?
23. **[scope]** Does the platform ledger learn settlement, FX and provider fees, or only the gross outcome (Shopify: gross only, provider settles directly)?

---

## 10. Fit test: Yemeni provider shapes

Common facts:
- `YE` is in `CountryCode` and `YER` is in `CurrencyCode` [FN].
- `supported_countries = ["YE"]` is declarable [CONF]. There is no currency declaration, so non-YER sessions would be rejected with `INVALID_CURRENCY` [S].
- None of these rails fit `payments.credit-card.*` or `redeemable` cleanly. The candidates are **offsite** and **custom onsite**.
- In every case the merchant's rail credentials (SpId and certificate, tokens, terminal) live in the app. Shopify only sees `externalHandle` (e.g. SpId or terminal id) and `ready` [MUT*:PaymentsAppConfiguration].
- No refund API means `refundSessionReject(PROCESSING_ERROR, merchantMessage)` and manual settlement. Shopify still requires that "merchants can … refund" [REQS], and treats refunds as required, enforced for confirm-enabled apps [CONF]. **Gap.**
- No auth/capture split means `kind` is always `sale` and no capture/void URLs are configured [REF][CONF].

**(a) CashPay** (SpId + client certificate; init(requestId, phone, amount, currency) → ref; confirm(requestId, ref, OTP)).
- Best fit: **offsite**. The start session returns `redirect_url` to an app page. The page collects the phone, calls init with **`requestId := payment session id`**. That matches the Shopify idempotency key directly [REF]. The page then shows an OTP box, optionally calls `paymentSessionConfirm` and waits for `confirmation_result`, then confirms with CashPay and calls `paymentSessionResolve`, then redirects to `nextAction.redirectUrl`.
- Alternative: **custom-onsite**, with `phone` as a `checkout_payment_method_fields` entry (arriving in `data.attributes`) and init called at session start. The OTP still needs the `redirect_url` page, because the modal can't take input [ALT][S:ModalAction].
- Wrong OTP: retry on the page, don't reject [ALT]. OTP expiry or abandonment: `cancel_url`. Insufficient funds: `INSUFFICIENT_FUNDS`, source `PROVIDER`.
- **Doesn't fit:** an OTP field inside Shopify checkout. The CashPay reference has nowhere to go on the Shopify transaction [S][API]. A rail timeout on confirm with no status call leaves only `PENDING(PARTNER_ACTION_REQUIRED)` and manual reconciliation.

**(b) Jawali** (system token → wallet token; buyer-made voucher; inquire voucher → cash-out).
- The buyer **pushes** a pre-funded token. Closest Shopify analogue is **redeemable**: field `voucher`, `balance_url` = inquiry returning `{value, currency}`, then a payment session runs cash-out [RED*].
- It fails on several counts:
  - Redeemables are gift-card-only (`supported_payment_methods` = `gift-card`), closed beta and Plus only [CONF][RED*].
  - Gift-card semantics apply a partial balance, but a voucher is usually consumed whole. Overpayment would need change, i.e. `CHANGE` exists only for cash [AREF*:OrderTransactionKind].
- Practical fit: **custom-onsite** with field `voucher_code`. At session start: inquire → check `amount == session.amount && currency` → cash-out → resolve. Otherwise reject with `INVALID_AMOUNT`/`AMOUNT_TOO_SMALL`/`INVALID_PAYMENT_METHOD`/`INVALID_CURRENCY`.
- The buyer must make the voucher for the exact total (including shipping and tax) **before** "Pay now". The `external` modal could show an instruction, but it can't receive the code back [S:External].
- Inference: inquiry-then-cash-out is structurally **authorization (buyer-held) → capture**. You could map `kind=authorization` → inquiry with `authorizationExpiresAt` = voucher expiry → `captureSession` does cash-out (`AUTHORIZATION_EXPIRED` on failure). But the buyer, not the provider, controls the hold, so it can vanish before capture.
- The two-layer token is invisible to Shopify; it's app-internal.

**(c) Saba Cash** (init(amount, currency, beneficiaryTerminal, phone) → adjustment id; confirm(adjustment id, OTP) → transaction id; status query by transaction id).
- Same as CashPay. `beneficiaryTerminal` is per-merchant config (the `externalHandle` candidate). The rail does not take Shopify's id, so the app must keep `session id ↔ adjustment id ↔ transaction id`.
- The **status query** is how the app turns an in-doubt confirm into a definite resolve/reject. In between: `paymentSessionPending(NETWORK_ACTION_REQUIRED or PARTNER_ACTION_REQUIRED, pendingExpiresAt)`. This creates the order with pending payment [ALT].
- **Doesn't fit:** Shopify has no pull channel. It never asks "what happened?", so all polling is the app's job, bounded by its own retry policy [CONS].

**(d) Al-Qutaibi Bank** (RequestPayment(phone, payment code, amount, currency); ConfirmPayment(same + OTP) → transaction id).
- Two buyer secrets arrive at different times: the payment code (buyer-obtained, pushed) before, and the OTP after RequestPayment.
- Fit: **custom-onsite**, with fields `phone` and `payment_code` in checkout. The start session calls RequestPayment and returns a `redirect_url` to an OTP page. The app must persist all request parameters keyed by session `id`, because ConfirmPayment repeats them.
- With no rail reference and no idempotency key, a retried ConfirmPayment risks a **double debit**. Shopify's idempotency stops at the app [CONS].
- With no status query, a timed-out ConfirmPayment is a true unknown. The only representation is `PENDING(MERCHANT_ACTION_REQUIRED)` until someone reconciles by hand, and if no one does, the session hits its pending limit.

**The abstraction the fit test implies (for Sharrwah):**
- Keep Shopify's core:
  - a platform-owned **Attempt** with its own id passed to adapters as the request/idempotency id;
  - attempts grouped per checkout;
  - a single outcome vocabulary {resolved, rejected(reason, source), pending(reason, expiry)} with terminal finality and first-writer-wins;
  - a platform **confirm gate** before irreversible debit. This matters more for rails without refunds.
- Add what Shopify omits:
  1. A first-class **buyer-interaction step** that can *collect* input inside checkout (OTP, voucher, payment code), not just display a QR or instruction. Its order (before or after rail init) is declared by the adapter.
  2. A **platform-pull reconciliation** hook (`inquire(attempt)`) for adapters with status queries, plus a modelled `in_doubt → manual_reconciliation` path for adapters without one.
  3. **Provider reference storage** on the transaction (rail reference, rail transaction id, voucher id).
  4. A **capability profile** per adapter: credentials schema; initiation style (platform-pull by phone vs buyer-push token); buyer verification (OTP, voucher, none); outcome discovery (callback, query, none); reversal (refund API, manual, none); hold semantics (provider-held vs buyer-held); currencies and limits.
  5. A **"refund outside provider"** outcome so obligations close even when the rail can't reverse funds.

---

### Gaps / unread
- The corpus has no request reference for verification sessions and doesn't say what happens when `pendingExpiresAt` lapses.
- The offsite and redeemable tutorials were missing and were fetched.
- Help Center pages (pending payments, payment authorization) were not read.
