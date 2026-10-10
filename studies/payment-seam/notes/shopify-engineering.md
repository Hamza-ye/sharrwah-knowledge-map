# E notes: how Shopify built payments beside checkout, orders, fulfilment, returns, POS, finance and apps

Prepared 2026-10-10 for the Sharrwah study. The question: can payments be its own part of the system, with its own pace, research and regulation, while the rest of the platform depends only on a narrow, stable contract?

## How to read these notes

- **Sources:** 40 in total (E001–E040). The table is in `E_sources.tsv`.
- **Labels:** "Fact" means the source says it. The quote is verbatim, at most 25 words, and was checked against the downloaded text. "Inference" is my reading and is not stated by the source.
- **Locations:** Each quote gives a section heading, a slide number or a transcript section. The InfoQ transcript (E001) has section headings but no timestamps, so those headings are used.
- **Dates:** Sources dated before 2023 are marked **historical**: they show how Shopify was built then, not necessarily now.
  - Shopify developer docs and help pages (E030–E034, E036, E037) are live pages with no date. They are marked "undated, accessed 2026-10-10".
  - These docs describe Shopify's external contract with providers and apps, not its internals.
- **Reachability:** All URLs were tested from this container on 2026-10-10 at 08:13Z and 08:17Z, using the prescribed curl command, at most 4 at a time.
  - Every page returned HTTP 200 except the three github.com repository pages, which returned 403.
  - Their READMEs were read through raw.githubusercontent.com (HTTP 200).
- **Search method:**
  - I listed all 432 posts in the Shopify Engineering sitemap (https://shopify.engineering/sitemap.xml) and the Rails at Scale index.
  - I also searched for InfoQ/QCon, RailsConf, RubyConf and Rails World talks.
  - **Not found:**
    - any 2023–2026 conference talk with a transcript on Shopify's payments architecture;
    - any engineering post on Shop Pay's payment internals, the Shopify Payments ledger or payouts, returns, or POS payment internals;
    - any engineering source naming the processor behind Shopify Payments. The sources say "financial partners" or "payment processor".

---

## E001 — Shopify's Architecture to Handle the World's Biggest Flash Sales (talk, transcript)

- **Speaker:** Bart de Water, manager on the Shopify Payments team.
- **Where:** InfoQ video with full transcript, the founder's seed. InfoQ shows "Recorded at: Oct 07, 2022" and tags it "QCon Plus May 2022". The same talk was given at QCon London on 2022-04-04 (E002).
- **Era of the content:** It quotes BFCM 2021 figures. In the Q&A, Ruby 3.1 is "due to be released this Christmas", so parts of the recording may date from late 2021.
- **Status:** historical (pre-2023).

**1. Where payments lives**
- Fact: "Shopify Payments is our built-in payment processing solution that we offer to merchants in 17 countries around the world." (Transcript, opening)
- Fact: "We also support many payment integrations from third parties." (Transcript, opening)
- Fact: The card fields are iframes on a separate domain. "This is how we keep the Shopify monolith out of scope. We just don't let it see any card data in the first place." (§ Shopify's Payment Methods)
- Fact: "a background job in the Shopify monolith passes the token and payment metadata to an app we call CardServer." (§ Shopify's Payment Methods)
- Fact: "Checkout is still part of the monolith, because it is tied to so many other systems." (§ Questions and Answers)
- Fact: "things that pertain to a single shop, like an order or a chargeback or a refund, it's just easier to keep it in a monolith." (§ Questions and Answers)
- Fact: Inside the monolith there is "something in the payment processing component talking to something in the order component". (§ Questions and Answers)
- Fact: Features that work across shops live outside the monolith. "things that do need to work across multiple shops need to be either built in a separate application, or use our data warehouse" (§ Shopify's Product Architecture)
- Fact: The example given is "An example of such an app is Shop Pay, that's our one-click checkout solution". (§ Shopify's Product Architecture)
- Inference: Payments is a mix of four parts:
  1. A payments component inside the Rails monolith. It sits next to orders and owns shop-scoped payment records, chargebacks and refunds.
  2. Separate apps that hold card data and call processors: CardSink and CardServer.
  3. External processors and acquirers.
  4. Third-party gateways.
- Inference: The line that separates out the card apps was drawn by PCI scope, not by team autonomy.

**2. What crosses between checkout, orders and payments**
- Fact: "The checkout code then submits this token alongside all the other checkout data to the main Shopify application." (§ Shopify's Payment Methods)
- Fact: CardServer looks up and decrypts the card in CardSink by token, then calls the processor. Then: "Assuming the charge is authorized, a success response is returned back and the checkout is converted to an order." (§ Shopify's Payment Methods)
- Fact: After conversion, "There's also confirmation emails sent, any webhooks for apps are fired." (§ Shopify's Payment Methods)
- Fact: Checkout "needs to store the fact that the payment happened from the checkout, create an order object, create shipping orders." (§ Questions and Answers)
- Fact: Checkout also has to update finance state: "The balance that needs to be paid out to the merchants needs to be updated." (§ Questions and Answers)
- Fact: Packwerk is used to flag the payments component "directly using the order object without going through the order public API to update the amount." (§ Questions and Answers)
- Fact: The reason given: "If I, from the payments component, just start updating one little number, their internal consistency is all messed up" (§ Questions and Answers)
- Inference: Card data never crosses into core.
  - From core to the card app, the hand-off is a token plus payment metadata.
  - Back from the card app comes a success or failure, which the monolith turns into an order.
  - Inside the monolith, payments may change orders only through the orders public API.

**3. Consistency when things fail**
- Fact: While the job runs, "At this point, the buyer is presented with a waiting screen with a little spinner". (§ Shopify's Payment Methods)
- Fact: "for processing payments, we want exactly-once semantics when we send this type of request." (§ Idempotent Request and Action)
- Fact: This is done by "including an idempotency into requests that uniquely identifies this payment attempt." (§ Idempotent Request and Action)
- Fact: Resumption, an internal library, records "each step of progress made is recorded in the database". (§ Resumption)
- Fact: On a retry, "we first look up the progress stored in the database. We find it and then we run through the recover steps first". (§ Resumption)
- Fact: Circuit breakers protect "both internal and external APIs". (§ Circuit Breaker)
- Fact: Current work is to "defer some of the work to be after the payment has been done" so that transaction time is shorter. (§ Questions and Answers)
- Inference: The unit of retry is the payment attempt, which the idempotency key names, not the order. An unknown outcome is resolved by retrying with the same key against a stored step log. The talk does not mention reconciliation.

**4. What varies by provider or market, and how it is isolated**
- Fact: CardServer uses metadata "to find the right payment processor to talk to using an adapter library. It transforms the standardized call into the processor specific API call." (§ Shopify's Payment Methods)
- Fact: "Payments, for example, have a country dimension to them. Of course, there's regulation, but also acquiring done is at the local level" (§ Circuit Breaker)
- Fact: The fix is "By adding the country to the circuit breaker identifier". The aim is that a Canadian outage does not block others: "we don't want the open circuit to affect American or Mexican merchants". (§ Circuit Breaker)
- Fact: For load tests, "we have set these stores up with a simple benchmark gateway, also a Go app." (§ Load Testing in Production)
- Inference: Provider differences sit in the card app's adapter layer, behind one standardized call. Market differences appear in the failure-isolation key. Neither leaks into checkout.

---

## E002 — Shopify's architecture to handle the world's biggest flash sales (QCon London 2022 slides)

- **Speaker:** Bart de Water.
- **Format:** 57-slide PDF. Slide 1 reads "QCon London - April 4, 2022". It goes with the E001 transcript.
- **Status:** historical.

**1. Where payments lives**
- Fact: Slide 9 has three columns. Under "Checkout" it lists "Write heavy", "Consistency", "External services". Under "Storefront" it lists "Read heavy", "Availability", "Cacheable".
- Fact: Slide 20 shows "Payments" as one of the components around "Checkout", with Pricing, Merchandise, Inventory, Shipping and Taxes.
- Fact: Slide 25 shows the browser form posting to "CardSink" and getting back a "Card token".
- Fact: Slide 26 shows three hops between Shopify, CardSink, CardServer and "Processor": "Authorize + card token", "Get card", "Authorize card", then "Success".

**2. What crosses**
- Fact: Slide 51, "Idempotent request", shows these body fields: `amount {value, currency}`, `"clientAccountId"`, `"clientBuyerId"`, `"clientTransactionId"`, `"test"`, `"idempotencyKey"`.
- Inference: The payment app is called with the caller's own identifiers (account, buyer, transaction) plus an idempotency key, not with order objects. The "client" prefix suggests a multi-client service, but the slides do not say so.

**3. Consistency on failure**
- Fact: Slide 52, "Idempotent action", shows `class CreateCharge` / `include Resumption::Processor`, with recovery points `create_incoming_records`, `create_outgoing_records` and `call_remote_api`. The last is marked `transactional: false`, followed by `handle_remote_response`.
- Fact: Slides 53–54 replay a failed `call_remote_api` with the same `idempotency_key`. On the retry, `recover_local_records` and `recover_outgoing_records` run before the remote call.
- Fact: Slide 50 shows the Semian defaults `error_threshold: 3`, `error_timeout: 10`.

**4. Provider/market variance**
- Fact: Slide 44, "Load testing setup", shows four labels in a row: "Genghis", "Shopify", "CardServer", "Benchmark gateway".
- Fact: Slide 50 shows the default circuit name `"#{host}_#{port}"`. E001 explains that the payments circuits add the country to it.
- Inference: The benchmark gateway plugs in at CardServer's processor side. So the provider seam lies behind CardServer, not inside checkout.

---

## E003 — 10 Tips for Building Resilient Payment Systems

- **Author:** Bart de Water, staff developer on payment infrastructure.
- **Published:** 2022-07-28, Shopify Engineering blog.
- **Status:** historical.

**1. Where payments lives**
- Fact: A checkout correlation id is passed on: "This identifier is passed along to a background job that makes the API call to the payment service that handles sensitive credit card data". (§ 5. Implement Structured Logging)
- Fact: "Our centralized payment service can track attempts" (§ 6. Use Idempotency Keys)
- Fact: "Merchants’ livelihoods are dependent on us if they pick Shopify Payments for accepting payments online or in-person" (§ Scratching the Surface)
- Inference: This is the same shape as E001: a checkout background job in core calls a separate, centralized payment service, which calls external "financial partners". The same service covers online and in-person payments, which is an inference from "online or in-person".

**2. What crosses**
- Fact: "a correlation_id is generated by our Rails controller". It travels through the job to the payment service, "which contains the correlation identifier in the API parameters and SQL query comments". (§ 5)
- Fact: The idempotency key per attempt "makes sure we send only a single request to our financial partners". (§ 6)

**3. Consistency on failure**
- Fact: "I found that an open timeout of one second with a write and read or query timeout of five seconds is a decent starting point." (§ 1. Lower Your Timeouts)
- Fact: "In payments, we distinguish between payment failures and errors." (§ 4. Add Monitoring and Alerting)
- Fact: "An idempotency key needs to be unique for the time we want the request to be retryable, typically 24 hours or less." (§ 6)
- Fact: The keys are ULIDs: "In one high-throughput system at Shopify we’ve seen a 50 percent decrease in INSERT statement duration" after switching from UUIDv4. (§ 6)
- Fact: "With reconciliation we make sure that our records are consistent with those of our financial partners." (§ 7. Be Consistent With Reconciliation)
- Fact: "We reconcile individual records such as charges or refunds, and aggregates such as the current balance not yet paid out to a merchant." (§ 7)
- Fact: Records also feed finance: "they’re also used as input for tax forms". (§ 7)
- Fact: "In case of a mismatch, we record the anomaly in our database." One example is "MismatchCaptureStatusAnomaly". Another: "We should rely on anomalies to fix things as a last resort". (§ 7)
- Fact: When load exceeds capacity, "we place these buyers on a waiting queue" before payment. (§ 8. Incorporate Load testing)
- Inference: Correctness is layered:
  - timeouts and circuit breakers limit how long a call waits;
  - idempotency keys make retries safe;
  - reconciliation with recorded anomalies catches whatever slips through, at both charge level and balance level.
- Inference: The balance-level reconciliation is where payments meets finance.

**4. Provider/market variance**
- Fact: "Worldwide payment processing typically uses a single endpoint, but often payment gateways use local acquirers behind the scenes" (§ 2. Install Circuit Breakers)
- Fact: "For Shopify Payments credit card transactions, we add the merchant's country code to the endpoint host and port to create a more fine-grained Semian identifier" (§ 2)
- Fact: "the test and staging environments of our financial partners don’t have the same capacity or latency distribution as production." So a benchmark gateway is used. (§ 8)

---

## E004 — Building Resilient GraphQL APIs Using Idempotency

- **Author:** Todd Jefferson.
- **Published:** 2019-08-27.
- **Status:** historical. This is the oldest design write-up of Shopify's Payment Service.

**1. Where payments lives**
- Fact: "Shopify’s new Payment Service, which centralizes payment processing for certain payment methods". (subtitle and intro)
- Fact: The service is "owned by the Money Infrastructure team which is responsible for the code that moves money, handles and records the interactions with various payment providers". (§ Shopify’s New Payment Service)
- Fact: "The service provides a GraphQL interface that’s used by Shopify and our Billing system." (§ Shopify’s New Payment Service)
- Inference: By 2019, money movement for some payment methods ran in a separate service with at least two clients: the core platform and Billing. That is a narrow, multi-client payments API for part of the payment surface.

**2. What crosses**
- Fact: "the Payment Service has a ChargeCreate mutation which creates a payment using the buyer’s chosen payment method" (§ The Issues With Non-resilient Payment Services)
- Fact: "One of the parameters to every mutation is an idempotency-key". It is part of the GraphQL input: "we’re not using an HTTP header for middleware". (§ Name the Request: Use Idempotency Keys)

**3. Consistency on failure**
- Fact: "When an API request can’t be re-attempted and an error happens during a payment attempt, the outcome is unknown." (§ The Issues With Non-resilient Payment Services)
- Fact: Automatic reconciliation was weighed and not chosen as the primary fix, because "introducing new payment methods and providers would require new reconciliation work". (§ Possible Solutions)
- Fact: On a concurrent duplicate, the service will "reject the request with an HTTP code of 409, meaning that the client may try again shortly". (§ Lock the API Call)
- Fact: "Each model instance is uniquely identified by the client and idempotency key." The model is IncomingRequest. (§ Track Requests)
- Fact: Steps are separated by the kind of side effect, for example "Remote side effects: Calls to service providers, loggers, analytics." (§ Using Steps Explained)
- Fact: The cost: "Storing the progress of a request requires extra database writes, this will add overhead to every API call." (§ Drawbacks of API Idempotency)

**4. Provider/market variance**
- Fact: "Here is the handler class implementation for the Sofort payment method." (§ Using Steps Explained)
- Fact: "if remote service providers APIs are not idempotent, it will be very hard to implement an idempotent API." (§ Creating an Idempotent API)
- Inference: Each payment method gets its own handler class inside the service, and all of them sit behind the same idempotent mutation contract. Callers do not see per-provider differences.

---

## E005 — Navigating Recurring Payments in India: A Backend Perspective

- **Author:** Yash Kapadia, Money Infrastructure.
- **Published:** 2022-06-29.
- **Status:** historical.
- **Caveat:** This is about Shopify billing merchants, not buyers paying merchants in checkout.

**1. Where payments lives**
- Fact: "Since the payment service at Shopify is an API serving as the internal mechanism for products such as Billing to move money around" (§ Building Resiliency)
- Fact: "From a backend perspective, all these complexities meant a few things for our internal payment service." (intro)

**2. What crosses**
- Fact: "With the registration of an e-mandate, Shopify’s payment service would receive a token from the payment provider." (§ Conceptualizing an E-Mandate)
- Fact: The service's model: "a source is an object that encapsulates the underlying payment method". A verification charge is created for audit, and then "This charge would then be automatically refunded through an asynchronous background job". (§ Conceptualizing an E-Mandate)

**3. Consistency on failure**
- Fact: "Our payment provider’s new APIs were not idempotent by default." (§ Building Resiliency)
- Fact: The workaround: "orders were unique by the value passed in the Orders API’s receipt field". Then: "This would essentially function as our idempotency key." (§ Building Resiliency)
- Fact: UPI is asynchronous: "the payment service would be relying heavily on webhooks from our payment provider" (§ Implementing UPI)

**4. Provider/market variance**
- Fact: The regulation shaped the internal model: "we plan to explicitly define the concepts of an e-mandate object and tokenized card payment instrument within the payment service". (§ Make Better Abstractions for the Future)
- Fact: UPI limits could not be read at runtime: "there was no way for our system to determine these limits at runtime". So the team set ₹5,000, the lowest bank and app limit at the time, as the e-mandate maximum. (§ Implementing UPI)
- Fact: The provider code was shared: "we decided to abstract these Shopify-specificities into an internal Ruby on Rails gem and de-duplicate code across multiple repositories". (§ Extract Obvious Cases of Shared logic Into a Dependency)
- Fact: The provider was also called directly elsewhere: "we had a few systems communicating with our payment provider’s API". (same §)
- Fact: "Each provider has different UX philosophies for their APIs". Also: "we have to better abstract our systems for long-term simplicity and become versatile with providers as we scale across local markets". (§ Expect New Patterns to Emerge as Payment Providers Change)
- Fact: Users saw a change: "the user would get a notification that they’ll be charged in 24-48 hours" when buying a theme. (§ Handling Recurring and One-Time Payments)
- Inference: This is the closest Shopify evidence that payments can absorb a market's regulation at its own pace. The RBI rules landed in the payment service and a provider gem, while Billing kept calling the same service.
- Inference: The boundary was not airtight in two ways:
  - The regulation changed what users experienced.
  - Several other applications talked to the provider directly. They shared a gem, not a service.

---

## E006 — High Availability by Offloading Work Into the Background

- **Author:** Kerstin Puschke.
- **Published:** 2021-07-08.
- **Status:** historical.
- **Caveat:** General guidance on background jobs, not a payments design document.

**1.** Not covered.

**2. What crosses**
- Fact: "Breaking changes to the job parameters need to roll out through a sequence of changes that preserve backward compatibility" (§ Breaking Changes to Job Parameters)
- Inference: Per E001 and E003, the hand-off from checkout to payment is a background job. Its parameters therefore act as a versioned contract between code running at different versions.

**3. Consistency on failure**
- Fact: The intro names "slow requests to a third-party payment gateway" as one cause of overload.
- Fact: The job can be retried safely "if every charge is carefully tracked and the job checks those states before attempting a charge". Then: "The job is idempotent, allowing us to safely choose at-least once delivery." (§ No Exactly-once Delivery)
- Fact: "The outbox pattern can be used to create transactionally staged job queues." (§ Non-Transactional Queuing)
- Fact: "The SAGA pattern can be used to guarantee eventual consistency." (§ Local Transactions)
- Inference: Shopify's job system delivers at least once, so payment jobs must be idempotent. The post offers the outbox and SAGA patterns but does not say payments uses them.

**4.** Not covered.

---

## E007 — Performance Testing At Scale—for BFCM and Beyond

- **Author:** Jordan Neufeld.
- **Published:** 2023-01-27.
- **Status:** current (2023).

**1. Where payments lives**
- Fact: Shopify is "a hybrid model with a monolithic ruby application in the center (Shopify Core) that’s supported by a variety of services". The services listed include "fraud analysis pipelines, payment processing infrastructure, webhook-sending services, and many more". (§ What is BFCM Scale Testing?)
- Inference: In early 2023 Shopify still describes payment processing as infrastructure outside Core. This fits CardServer and the payment service in E001 and E003.

**3. Consistency/operations**
- Fact: Load flows end by "checking out via a mock payment gateway with test credit card details". (§ Running Load Tests)
- Fact: Load is measured in "Checkouts Completed Per Minute (CCPM)". (§ Determining How Far Do We Push the Platform)

**2, 4.** Not covered.

---

## E008 — How we prepare Shopify for BFCM

- **Authors:** Kyle Petroski and Matthew Frail.
- **Published:** 2025-11-20.
- **Status:** current.

**3. Consistency/operations**
- Fact: "We spent extra time on the most business-critical user paths through Shopify, like checkout, payment processing, order creation, and fulfillment" (§ Game Days)
- Fact: "Toxiproxy, an open-source framework we built for simulating network conditions, injects network failures and partitions" (§ Load testing)
- Fact: "Scale Test 1-2: Under heavy load, core operations threw errors and checkout queues backed up." (§ The scale testing program)
- Inference: Payment processing is tested as one step in a journey that spans systems, alongside order creation. The post gives no new detail on the boundary itself.

**1, 2, 4.** Not covered.

---

## E009 — We replaced Redis with MySQL for inventory reservations—and it scaled

- **Author:** Emilie Noel.
- **Published:** 2026-05-12.
- **Status:** current.

**2. What crosses**
- Fact: "Our oversell protection system handles this by reserving inventory during payment processing—a short hold that prevents two concurrent checkouts from claiming the same unit." (intro)
- Fact: "Reserve: When payment starts, we mark items as reserved (a short hold, e.g. several minutes)." (§ What is oversell protection?)
- Fact: "Claim: When payment succeeds, we permanently deduct quantity from the inventory ledger (source of truth)." (§ What is oversell protection?)
- Fact: Checkout completion is tagged as a business process in SQL: `/* conn_tag:checkout_completion */`. (§ Following the symptoms)

**3. Consistency on failure**
- Fact: Before the change, "reservations and the inventory ledger lived in two different systems" (§ The Redis model and its limits)
- Fact: Moving them into one database meant "fixing classes of bugs that were possible with Redis (e.g. payment succeeds but inventory isn't claimed, or the reverse)." (§ Core idea: one row per unit, bounded by design)
- Fact: The cutover ran in shadow mode "with Redis remaining the source of truth". Then "The rollout was gradual, pod by pod". (§ The cutover)
- Fact: "The cleanup of the checkout path removed 50% of reads and 33% of transactions on the primary database." (§ What we found)
- Inference: In 2026 the checkout-completion path brackets the payment with a time-boxed inventory hold and a claim that the payment success triggers.
- Inference: Shopify fixed consistency by putting reservation and ledger in one ACID store on the order and inventory side. The payment itself stays an external step that is not part of that transaction. Its result drives the claim, and the hold's expiry covers abandoned or unknown attempts. The expiry is implied by "short hold" and not spelled out.

**1, 4.** Not covered.

---

## E010 — Powering Shopify's High-Performance, PCI DSS v4 Compliant Checkout with Sandboxing

- **Author:** Ilya Grigorik, Distinguished Engineer.
- **Published:** 2025-02-11, Shopify Partners blog.
- **Status:** current.

**1. Where payments lives (front end)**
- Fact: "The backend is hosted on Shopify servers and is battle-tested to scale to the largest sales on the internet". The front end is a Shopify-managed runtime. (§ Sandboxing: future-proof Shopify Checkout architecture)
- Fact: The usual PCI v3 pattern is that the payment iframe "the content is loaded by and handled by a PCI-compliant service (typically called a “cardholder data environment”)". (§ TL;DR on PCI DSS v4 requirements)
- Fact: Shopify's listed protections include "Load and isolate payment form via ("payment page") iframe for defense-in-depth". (§ Shopify Checkout will provide PCI DSS v4 compliance, no work required)

**2. What crosses (front end)**
- Fact: App code runs in sandboxes: "no custom code is executed in the parent page, all communication is sanitized by a managed bridge". (§ Sandboxing…)
- Fact: "UI Extensions and Web Pixels are implemented against APIs instead of DOM selectors and events". (§ Sandboxing…)

**4. Variance and regulation**
- Fact: PCI DSS v4's script controls mean "the above applies to both the "parent" and "payment" pages." (§ TL;DR on PCI DSS v4 requirements)
- Fact: "The use of sandboxing is a strict requirement of Shopify Checkout." (§ Sandboxing…)
- Inference: The iframe-to-card-vault design of 2022 (E001) continues in 2025 as a "payment page" iframe.
- Inference: A regulatory change (PCI v4) was absorbed in the checkout host page and the sandbox rules, without changing what reaches the backend. The post does not name CardSink.

**3.** Not covered.

---

## E011 — Google Pay inside sandboxed iframe for PCI DSS v4 compliance

- **Authors:** Dominik Mengelt and Matthew Class, both at Google.
- **Published:** 2025-06-10, Google Developers Blog.
- **Status:** current.
- **Caveat:** Third-party post that quotes Shopify.

**1 and 4.**
- Fact: "Shopify was able to successfully pass the PCI DSS v4 audit by using a sandboxed iframe to display the Google Pay button." (§ Shopify successfully certified for PCI DSS v4)
- Fact: Ilya Grigorik is quoted: "We’ve built Shopify Checkout in such a way that Google Pay code executes in a secure sandboxed environment". (§ Shopify successfully certified for PCI DSS v4)
- Inference: Each wallet provider's front-end code is isolated in its own sandbox inside checkout.

**2, 3.** Not covered.

---

## E012 — Building the Universal Commerce Protocol

- **Author:** Ilya Grigorik.
- **Published:** 2026-01-11.
- **Status:** current.
- **Caveat:** This is an open protocol co-developed with Google for agents and merchants. It is an external contract, not a description of Shopify's internals.

**2. What crosses**
- Fact: "Shopping service defines core transaction primitives: checkout session, line items, totals, messages, status" (§ Capabilities and extensions)
- Fact: A checkout moves through states that include "incomplete: missing required information; agent should attempt to resolve via API" and "ready_for_complete: all information collected; agent can finalize programmatically". (§ Commerce demands collaboration)
- Fact: For hand-off, "ECP establishes a JSON-RPC 2.0 channel (state updates from merchant, credentials and context from agent)". (§ Handoff is an invitation for collaboration)

**3. Consistency**
- Fact: "requires_escalation: buyer input required; agent should attempt API resolution and, if unable, hand off via continue_url" (§ Commerce demands collaboration)
- Inference: Partial automation is handled by an explicit state plus a hand-off URL, not by failing. Unknown payment results are not discussed.

**4. Provider/market variance**
- Fact: "payment options and rules differ based on properties of the cart, buyer, and market" (intro)
- Fact: "Handlers vary based on cart contents, buyer location, or transaction amount." (§ Payments are a two-sided negotiation)
- Fact: "each provider—whether it’s Google, Shopify, or a regional PSP—publishes their own handler specification." (§ Payments are a two-sided negotiation)
- Fact: "New payment methods grow into the ecosystem without committee votes or core version bumps." (§ Payments are a two-sided negotiation)
- Fact: Of extensions: "It versions independently; core stays stable." (§ Capabilities and extensions)
- Inference: This is Shopify's clearest recent statement of the principle Sharrwah is testing: a small stable core, with payment methods and providers supplying their own versioned specifications. Nothing in the post says Shopify's internal boundary is built this way.

**1.** Not covered.

---

## E013 — Introducing the commerce payments protocol

- **Authors:** Conner Swenberg and Amie Corso (Coinbase), with Simon Lacoursière (Shopify).
- **Published:** 2025-06-12, republished from the Base blog.
- **Status:** current.

**2. What crosses**
- Fact: "this protocol powers Shopify’s new USDC payment method, which is rolling out to millions of stores using Shopify Payments." (intro)
- Fact: The model copies cards: "Traditional payments handle this with a two-step “authorize and capture” process". It defines authorize, capture, charge, void, reclaim and refund. (§ Commerce: The Missing Piece; § Payment Operations)

**3. Consistency on failure**
- Fact: "Commercial payments involve race conditions between checkout, settlement, and fulfillment." (§ Commerce: The Missing Piece)
- Fact: "Inventory can sell out between completing checkout and payment processing." (§ Commerce: The Missing Piece)
- Fact: "the protocol rejects attempts at using a signed payment more than once." (§ Operators)
- Fact: "If the authorization expires and the operator has not yet captured or voided the payment, the payer is able to reclaim funds directly" (§ Operators)
- Fact: "The protocol enforces that payment transitions only occur in the valid time window defined by the payment’s various expiries." (§ Payment Operations)

**4. Provider/market variance**
- Fact: "Captures can be made in multiple partial increments to support merchants that may fulfill goods in multiple deliveries." (§ Capture)
- Inference: A new payment rail was made to fit the same authorize/capture/void/refund vocabulary that orders already use (E030, E033). That is what lets the rest of the platform stay unchanged. The post does not describe how USDC is wired into Shopify Payments internally.

**1.** Not covered.

---

## E014 — Supporting Passkeys in Shop's Authentication Flows

- **Author:** Abraão (Abe) Lourenço.
- **Published:** 2023-03-24.
- **Status:** current.

**1. Where payments lives**
- Fact: "Shop Pay, like Shopify, is built on Ruby on Rails." (intro)
- Fact: "we were initially building passkeys support for our main flows on the Shop domain". The team then "offered passkeys from within an iframe". (intro)
- Fact: "Given Shop Pay is available on storefronts as an embedded user experience" (§ Conditional UI Support)
- Inference: Shop Pay, the buyer wallet and identity, is a separate application on its own domain and is embedded in storefronts and checkout through an iframe. This agrees with E001.
- Not stated: how Shop Pay hands payment credentials to checkout.

**2, 3, 4.** Not covered.

---

## E015 — Horizontally scaling the Rails backend of Shop app with Vitess

- **Author:** Hammad Khalid.
- **Published:** 2024-01-17.
- **Status:** current.

**1. Where payments lives**
- Fact: "Shop app has different properties than the rest of Shopify." (§ Preparing for Vitess)
- Fact: "Most of the tables in our database are associated with a user, so naturally user_id was chosen as the sharding key." (§ Choosing our sharding key)

**3. Consistency**
- Fact: "We limited transactions to update only a single user's data" (§ Types of Verifiers)
- Fact: "For transactions that crossed between the sharded and unsharded keyspaces, we carefully split them up and analyzed their atomicity to ensure partial failures could self-heal." (§ Setting up query verifiers)
- Inference: Buyer-centric systems are partitioned by user, not by shop. This is the Shop app, and by inference Shop Pay (E001, E014). So they cannot share a database transaction with shop-sharded orders, and any link between a buyer wallet and an order crosses a service boundary.
- Caveat: the post does not mention payments.

**2, 4.** Not covered.

---

## E016 — A Packwerk Retrospective

- **Authors:** Gannon McGibbon and Chris Salzberg.
- **Published:** 2024-01-26 on Rails at Scale; cross-posted on Shopify Engineering on 2024-02-07.
- **Status:** current.

**1. Where payments lives (code organisation)**
- Fact: "Shopify organizes its monolith into code units called “components”." (§ Domain versus Function in Packages)
- Fact: "The monolith’s codebase was thus divided into directories with names like “Delivery”, “Online Store”, “Merchandising” and “Checkouts”." (§ Domain versus Function in Packages)
- Fact: "A checkout flow is a function defined as the code required for a customer to initiate a checkout and pay for their order." (§ Domain versus Function in Packages)
- Fact: Shopify now uses components "as top-level organizational tools for grouping one or more packages, rather than a singular code unit". (§ Domain versus Function in Packages)
- Fact: "Given these issues, privacy checks were removed from Packwerk with the release of version 3.0." (§ Packwerk as a Privacy Enforcer)
- Fact: The reason: "privacy checks had transformed Packwerk into something it was never intended to be: an API design tool." (§ Packwerk as a Privacy Enforcer)
- Fact: "a package that is well-defined according to Packwerk (has no violations left to resolve) may actually crash with name errors". (§ Weaknesses and Blind Spots of Packwerk)
- Fact: "Even for this relatively simple case of a package with no dependencies, our effort to reach full isolation had taken many months of hard work." (§ A Package with Zero Violations)
- Fact: "We have discussed removing Packwerk from our monolith". (§ Packwerk is a Sharp Knife)
- Fact: "running code, more than any metric, will always be the best indicator of real progress". (§ Packwerk is a Sharp Knife)

**2. What crosses**
- Fact: Isolation needed indirection: "We relied heavily on inversion of control". (§ A Package with Zero Violations)
- Inference: The 2022 claim that Packwerk stops payments from bypassing the order public API (E001) relied on the privacy (public-API) check.
  - Packwerk 3.0 removed that check from Packwerk itself in March 2023 (release date from E038). It now lives in the separate packwerk-extensions gem.
  - The retrospective does not say whether Shopify still runs it. The payments↔orders API boundary inside the monolith should therefore be treated as weakly enforced from 2023 on.
- Inference for Sharrwah: in Shopify's case, a component boundary inside one codebase did not by itself produce an independently evolvable unit.

**3, 4.** Not covered.

---

## E017 — One engine, many tools — Introducing Rubydex

- **Author:** Vinicius Stock.
- **Published:** 2026-05-12, Rails at Scale.
- **Status:** current.

**1. Boundary tooling, 2026**
- Fact: "Packwerk relies heavily on constant resolution to identify package violations." (§ Packwerk)
- Fact: "In our initial exploration of replacing Packwerk’s logic with Rubydex as" the engine, the team reports "Significantly more violations found thanks to correct constant resolution", with "about 3x more constant references resolved" in the monolith. (§ Packwerk)
- Fact: A related post, the Rubydex linter (Stan Lo, 2026-09-08), lists rules such as "Enforce dependency boundaries: files under app/domain/**/*.rb must not reference constants under Web::*." (example rule list)
- Inference: In 2026 Packwerk still guards the core monolith's dependency graph. Earlier violation counts under-reported references by a wide margin, so the boundary data of 2020–2024 was incomplete.

**2, 3, 4.** Not covered.

---

## E018 — The Myth of the Modular Monolith (Rails World 2024 keynote)

- **Speaker:** Eileen Uchitelle, Senior Staff Engineer at Shopify.
- **Date:** 2024-09-27.
- **Status:** current.
- **Format:** Video only, on the Rails World 2024 YouTube playlist. No transcript was found and I did not review the spoken content.
- **What I used:** The session abstract, and the slide text on Speaker Deck. Locations are item numbers in the Speaker Deck slide-text list, which may not match slide numbers exactly.

**1. Where things live**
- Fact (abstract): "At Shopify we went down the path of modularizing our monolith and since then GitHub, Gusto, and others have followed our lead." It continues: "But after 6 years it’s time to ask ourselves" whether it fixed the problems.
- Fact: "Modular monolith: Path to package isolation." (item 34)
- Fact: Item 43 shows a sample `package.yml` with "enforce_dependencies: strict".
- Fact: "Code is less tightly coupled? No." (item 63)
- Fact: "Deploys are more scalable? Not yet." (item 69)
- Fact: "You cannot solve human problems with modularity." (items 77 and 100)
- Fact: "Modularization: Functional isolation." (item 91)

**2. What crosses**
- Fact: "New Challenges: Primitive obsession." The code example is commented "# passing primitives instead of the cat AR object". (items 47–48)
- Fact: "New Challenges: Circular dependencies." (item 55)
- Inference: Inside one codebase, passing ids instead of objects is the visible cost of boundaries. A Shopify engineer judged that six years of modularization had not reduced coupling.
- Caveat: the slides have no payments-specific content.

**3, 4.** Not covered.

---

## E019 — Under Deconstruction: The State of Shopify's Monolith

- **Author:** Philip Müller.
- **Published:** 2020-09-16.
- **Status:** historical.

**1. Where payments lives**
- Fact: "We currently have 37 components in our main monolith, each with public entrypoints covering large parts of its responsibilities." Also: "Packwerk is used on about a third of the components". (§ What We’re Building Right Now)
- Fact: "We are very deliberate about when to split functionality out into separate services, and we only do it for good reasons." (§ What We’re Building Right Now)
- Fact: "Credit card vaulting is a separate service because it processes sensitive data that shouldn’t flow through other parts of the system." (§ What We’re Building Right Now)

**2. What crosses**
- Fact: "The public interface is what other components depend on; if a lot of components depend on it, it’s hard to change." (§ Balance Encapsulation With A Simple Dependency Graph)
- Fact: To invert dependencies: "This can be done for example through a publish/subscribe mechanism like ActiveSupport::Notifications." (§ Balance Encapsulation With A Simple Dependency Graph)
- Fact: On Sorbet: "Now it’s our go-to tool for expressing input and output contracts on component boundaries." (§ Define and Enforce Contracts)
- Fact: "One of the most problematic outdated assumptions is that all Active Record models are OK to access everywhere" (§ Understand Developer Behaviour)
- Fact: An open problem: "efficiently querying data across components without coupling them too tightly". (§ What We’re Building Right Now)
- Inference: In 2020 the only payment-related piece named as a separate service is card vaulting, justified by data sensitivity. Their advice for a stable boundary has three parts:
  - keep widely used interfaces abstract;
  - invert dependencies with events;
  - type the inputs and outputs.

**3, 4.** Not covered.

---

## E020 — Enforcing Modularity in Rails Apps with Packwerk

- **Author:** Maple Ong.
- **Published:** 2020-09-23.
- **Status:** historical.

**1. Where payments lives**
- Fact: "Each of the component folders at Shopify represent domains of commerce, such as orders and checkout." (§ Rails Is Like an Open-concept Living Space)
- Fact: "Cross-component calls are still being made, and Active Record models are shared across domains." (§ Rails Is Like an Open-concept Living Space)
- Fact: On microservices: "Distributing code over multiple machines is a topology change, not an architectural change." (§ Creating Microservices?)
- Fact: "Within the core codebase, we have 48 packages with 30 boundary enforcements within those packages." (§ How Shopify Is Using Packwerk)

**2. What crosses**
- Fact: "Privacy violations occur when an external constant references a package’s private constants." (§ Packwerk: Creating Our Own Solution)
- Fact: "We added a test case that rejects any PRs that introduce Active Record associations across components" (§ Using Tests to Prevent Cross-component Associations)
- Fact: The violation list doubled as an extraction plan: "the Shipping team at Shopify found success using this list to extract a domain out of their main application into its own service". (§ Enforcing Boundaries in Existing Codebases)
- Inference: In 2020, a narrow contract inside the monolith meant three things:
  - public constants only;
  - declared dependencies;
  - no Active Record associations across components.
- Inference: Shipping shows that a domain inside the monolith could later be extracted as a service along that line. E016 later removed privacy checks from Packwerk's core.

**3, 4.** Not covered.

---

## E021 — Deconstructing the Monolith

- **Author:** Kirsten Westeinde.
- **Published:** 2019-02-21.
- **Status:** historical.

**1 and 2.**
- Fact: Before componentization, a new developer "would also need to understand how orders are created, how we process payments, and much more since everything was so intertwined." (§ Disadvantages of Monolithic Systems)
- Fact: Code was reorganized by "real-world concepts (like orders, shipping, inventory, and billing)". (§ Code Organization)
- Fact: "Each component defined a clean dedicated interface with domain boundaries expressed through a public API and took exclusive ownership of its associated data." (§ Isolating Dependencies)
- Fact: "Cross-component associations are always violating componentization". Progress was tracked by "We developed a tool called Wedge in-house, which tracks the progress of each component towards its goal of isolation." (§ Isolating Dependencies)
- Inference: The intended contract between components, including payments and orders, was a public API plus exclusive ownership of data. E022 shows the shared database and the links to Shop remained in 2021.

**3, 4.** Not covered.

---

## E022 — Shopify-Made Patterns in Our Rails Apps

- **Author:** Ioana Surdu-Bob, a developer on the Shopify Payments team.
- **Published:** 2021-07-13.
- **Status:** historical.

**1. Where payments lives**
- Fact: "every table in a podded database is connected to a shop" (§ Pods)
- Fact: "But our database is still common for all domains, and everything is still linked to the Shop." (§ Domain Driven Design)
- Fact: "every time we’re instantiating a model outside our domain, we’re ignoring component boundaries and we receive a warning for it." (§ Domain Driven Design)
- Fact: "we don’t enforce any relationships between tables on the database layer" (§ Domain Driven Design)

**2. What crosses**
- Fact: "Monorail enforces schemas for widely used events. It creates contracts between Kafka producers and consumers". Also: "If it changes, it has to be done through versioning." (§ Standardizing How We Write code)
- Inference: Inside core, payments shares a shop-keyed database with orders, and the boundaries are code-level warnings. Where Shopify needs a stable contract between teams (events), it uses explicit, versioned schemas.

**3, 4.** Not covered.

---

## E023 — Capturing Every Change From Shopify's Sharded Monolith

- **Author:** John Martin.
- **Published:** 2021-03-12.
- **Status:** historical.

**2. What crosses**
- Fact: The output is "a kafka topic per logical table, such that the source database sharding is isolated from the consumers of the topic". (§ Building a Log-Based Change-Data Capture Platform)
- Fact: "One of the unfortunate aspects of CDC is the tight coupling of the external event consumers to the internal data model of the source." (§ Schemas and Schema Changes)
- Fact: "Breaking schema changes are extremely disruptive for our downstream consumers" (§ Schemas and Schema Changes)
- Inference: Table-level change streams from core are not a safe contract for a separately evolving payments unit, and Shopify itself names the coupling.

**1, 3, 4.** Not covered.

---

## E024 — A Pods Architecture To Allow Shopify To Scale

- **Author:** Xavier Denis.
- **Published:** 2018-03-02.
- **Status:** historical.

**1 and 3.**
- Fact: "A pod consists of a set of shops that live on a fully isolated set of datastores." (intro)
- Fact: "we don’t allow any actions to reach across pods". (intro)
- Fact: "we decided to assign every unit of work (web request and delayed job) to a single pod." (intro)
- Fact: "Sorting Hat matches every request to a pod and adds a header to that request." (§ Request Lifecycle)
- Inference: Payment work inside core, such as the E001 background job, is scoped to one shop and one pod. Anything that needs a view across shops (Shop Pay, analytics) must live outside core. A pod outage limits payment failures to that pod's shops.

**2, 4.** Not covered.

---

## E025 — Componentizing Shopify's Tax Engine

- **Authors:** Chris Inch and Vignesh Sivasubramanian.
- **Published:** 2019-07-05.
- **Status:** historical.
- **Caveat:** About tax, a neighbouring domain, not payments.

**2. What crosses**
- Fact: "During the creation of an order, the tax engine is invoked by three distinct parts of Shopify Cart -> Checkout -> Order." (§ Understand Existing Tax Logic)
- Fact: "When Checkout changed how it used Taxes, it might have unknowingly broken how Cart was using it." (§ Understand Existing Tax Logic)
- Fact: "Everything that requires tax information will pass a set of defined parameters, and expect a specific response when requesting tax rates." The schemas are named "TaxesRequestSchema and TaxesReponseSchema" (sic). (§ Define the Interface)
- Fact: "we added GitHub bot triggers to notify our team on any commits pushed against source files under tax component" (§ Executing the Plan)

**4. Jurisdictional variance, and how the new boundary was rolled out**
- Fact: "Literally, we calculated taxes twice and measured any discrepancies between the two calculations". (§ The Experimental Code Path)
- Fact: Then "we slowly scaled up the number of shops whose checkouts used the new tax component". (§ The Experimental Code Path)
- Inference: This is a Shopify precedent for the Sharrwah question in a domain heavy with jurisdiction rules. It has one entry point with plain-data request and response schemas, used by cart, checkout and order, and it was rolled out shop by shop after a shadow comparison.

**1, 3.** Not covered.

---

## E026 — How We Enable Two-Day Delivery in the Shopify Fulfillment Network

- **Author:** Linda Damus.
- **Published:** 2022-08-18.
- **Status:** historical.
- **Caveat:** A fulfilment analogue, not payments.

**2. What crosses**
- Fact: Core gained "a new set of GraphQL APIs that any 3PL can use to upload their delivery dates to the Shopify platform". (§ A Platform Solution)
- Fact: At checkout, "it’s a direct, fast lookup (under 100 ms) to find the pre-computed date for that item to the destination address". (§ Looking Up Delivery Dates in Real Time)
- Fact: "The date the buyer sees at checkout is sent back to SFN during order fulfillment". (§ Looking Up Delivery Dates in Real Time)
- Inference: For a separately built fulfilment service, Shopify avoided a synchronous call from checkout. The service pushes data into core, and the promise made at checkout travels back with the order.
- Inference: Payments cannot use this pattern, because authorization is inherently a live external call. That is one reason the payment hand-off differs from other hand-offs out of checkout.

**1, 3, 4.** Not covered.

---

## E027 — Creating a Flexible Order Routing System with Shopify Functions

- **Author:** Ebun Segun.
- **Published:** 2023-04-13.
- **Status:** current.

**4. Variance isolation pattern (orders and fulfilment)**
- Fact: "we dogfooded our own Shopify Functions feature to give merchants the ability to create their own routing rules" (intro)
- Fact: "A Shopify Function consists of three parts: the input, the logic, and the output." Also: "The input is shaped as a GraphQL query of pieces of information that the function logic needs". (§ Using Shopify Functions)
- Fact: "Stay within the destination market prioritizes shipping from locations in the same country as the destination address." (§ Using Shopify Functions)
- Inference: Shopify's general way to handle market- or merchant-specific rules is a pure function with a declared GraphQL input and a constrained output, executed by core. E036 shows the same mechanism for payment-method rules.

**1, 2, 3.** Not covered.

---

## E028 — Five Years of React Native at Shopify

- **Author:** Mustafa Ali.
- **Published:** 2025-01-13.
- **Status:** current, but a thin source.

**3. Consistency (POS)**
- Fact: The Point of Sale app "downloads and syncs a ton of data in the background so that it can process transactions even when offline". (§ Native code is crucial)
- Inference: POS must take payments without the backend. E037 describes the result: the order exists before the payment outcome is known.

**1, 2, 4.** Not covered.

---

## E029 — Building Reliable Mobile Applications (Shopify POS)

- **Author:** Mustafa Ali.
- **Published:** 2020-08-14.
- **Status:** historical, and a thin source.

**4. Variance (POS)**
- Fact: Dashboards show, for example, "the % of successful chip transactions made using a VISA credit card with the Tap, Chip & Swipe reader in the UK". (§ Automated Monitoring and Alerts)
- Fact: "Some areas, like payments, for instance, need a lot of domain knowledge to investigate issues." So payments has dedicated on-call. (§ Air Traffic Control)
- Inference: In-person payments vary by country, card network and reader hardware, and Shopify monitors each of these separately.

**1, 2, 3.** Not covered.

---

## E030 — Extensions for payments (Payments Platform overview)

- **Source:** shopify.dev product docs, undated, accessed 2026-10-10.
- **Caveat:** External contract, not internals.

**1. Where payments lives**
- Fact: "Only approved Partners can build payments extensions on Shopify's Payments Platform." (§ Extensions for payments)
- Fact: "Payments extensions integrate with Shopify checkout to process payments during the customer's purchase flow." (§ Where you can build)
- Fact: When onboarding, "The merchant deactivates the legacy payment gateway to avoid duplicate payment methods during checkout, if applicable." (§ How a merchant installs a payments extension)

**2 and 4.**
- Fact: "There are five types of payments extensions". One is "Offsite payment extension: Allows merchants to redirect their buyers to an app-hosted website to complete the payment process." (§ Build options)
- Fact: The supported operations are Charge, Refund, Authorize, Capture and Void, for example "Void: Merchants can cancel a previously authorized amount." (§ Supported payment operations)
- Inference: Third-party providers sit entirely outside Shopify, behind a fixed set of operations. The mention of "legacy" gateways shows an older integration path being replaced; no dates are given.

**3.** See E031.

---

## E031 — Payments apps: implementation considerations

- **Source:** shopify.dev product docs, undated, accessed 2026-10-10. The page references API version 2025-10.

**2. What crosses**
- Fact: "Payments apps need to implement mTLS" when Shopify calls them. (§ mTLS configuration)

**3. Consistency on failure**
- Fact: "Payments Apps APIs support idempotency, which allows Shopify to safely retry requests without accidentally performing the same operation twice." Also: "Idempotency keys don't expire." (§ Idempotency)
- Fact: "Some mutations are mutually exclusive, such as paymentSessionResolve and paymentSessionReject, where only one can be processed for a given id." (§ GraphQL requests from your payments app to Shopify)
- Fact: When reporting results back, apps retry "up to a total of 18 retries over 24h". Meanwhile buyers may be told "Their payment is processed, but Shopify is unreachable." (§ Retry policy › Outbound)
- Fact: "If your endpoint doesn't respond in time, Shopify retries the request several times." (§ Retry policy › Inbound)

**4. Provider variance**
- Inference: The contract is asynchronous in both directions:
  - Shopify starts a session over HTTP.
  - The provider reports the final result later through GraphQL.
  - Both sides retry, keyed by the session id.
  - Between resolve and reject, the first one to arrive wins.
- Inference: Shopify explicitly accepts a window in which money has moved but Shopify does not yet know.

**1.** See E030.

---

## E032 — Payments app request reference

- **Source:** shopify.dev product docs, undated, accessed 2026-10-10. Some fields are marked as added in API versions 2024-01 to 2024-10.

**2. What crosses**
- Fact: `id`: "Unique identifier for the payment attempt. Used as the idempotency key." (§ Start session › Request body)
- Fact: `group`: "The identifier that's shared across payment sessions, representing attempts to complete the same checkout or deferred payment capture." (§ Request body)
- Fact: `kind`: "Either sale or authorization." (§ Request body)
- Fact: "Shopify doesn't include an order ID in the payment session request." (§ Request body, note)
- Fact: Header: "The API version selected in the payments app configuration." (§ Request headers)

**3. Consistency**
- Fact: For refunds, `payment_id` is described as "For captured payments, this ID corresponds to the original authorization ID rather than the capture ID." (§ Refund › Request body)
- Fact: "Shopify must receive an HTTP 201 (Created) response for the refund session creation to be successful." (§ Refund › Response body)
- Inference: The identifiers that reach a provider are scoped to the payment: the attempt, the group (which stands for the checkout) and the session. They are not scoped to the order, and the link to the order is kept inside Shopify. The contract is versioned per app.

**1, 4.** See E030 and E031.

---

## E033 — OrderTransactionStatus and OrderTransactionKind enums (GraphQL Admin API)

- **Source:** shopify.dev product docs, API "latest" (2026-10), accessed 2026-10-10.
- **Caveat:** The public projection, not the internal model.

**2. What crosses (how a payment appears on an order)**
- Fact: "The different states that an OrderTransaction can have." The values are AWAITING_RESPONSE, ERROR, FAILURE, PENDING, SUCCESS and UNKNOWN. (§ OrderTransactionStatus)
- Fact: The kinds include AUTHORIZATION: "Money does not change hands until the authorization is captured." (§ OrderTransactionKind)
- Fact: Also EMV_AUTHORIZATION: "An authorization for a payment taken with an EMV credit card reader." (§ OrderTransactionKind)

**3. Consistency**
- Fact: AWAITING_RESPONSE: "Awaiting a response." UNKNOWN: "The transaction status is unknown." (§ OrderTransactionStatus)
- Fact: REFUND: "A refund can happen only after a capture is processed." (§ OrderTransactionKind)
- Inference: On the order side, payments are modelled as a list of typed transactions with explicit pending and unknown states. That is the stable vocabulary that orders, refunds and returns, POS and apps read.

**1, 4.** Not covered.

---

## E034 — Implementing idempotency (GraphQL Admin API)

- **Source:** shopify.dev product docs, undated, accessed 2026-10-10.

**2 and 3.**
- Fact: "Shopify tracks idempotency keys for 24 hours from the original request." (§ How idempotency protection is implemented on the server-side)
- Fact: "Shopify returns IDEMPOTENCY_CONCURRENT_REQUEST to subsequent requests instead of processing them." (same §)
- Fact: "any duplicate requests with the same idempotency key receive the cached GraphQL response without reprocessing the operation" (same §)
- Fact: "only the client is aware if they're intending to perform a separate operation or not." (§ Core principles)
- Inference: This is the 2019 internal pattern (E004: lock on key, stored response) offered to the public. The 24-hour window matches E003.

**1, 4.** Not covered.

---

## E035 — Making idempotency mandatory for inventory adjustments and refund mutations

- **Source:** Shopify developer changelog, dated 2025-12-12, version 2026-04, flagged "Breaking API Change".
- **Status:** current.

**2 and 3.**
- Fact: "We're making the idempotent directive introduced here mandatory for the following mutations in version 2026-04:" The list starts with `refundCreate`, followed by inventory mutations.
- Fact: "calling these mutations without an idempotency directive will result in an error at runtime."
- Inference: In 2025–2026 Shopify made retry safety part of the contract with apps for refunds, the main path from returns into payments, and for inventory. Before, it was a convention.

**1, 4.** Not covered.

---

## E036 — Payment Customization Function API

- **Source:** shopify.dev product docs, API "latest", accessed 2026-10-10.

**4. Provider/market variance**
- Fact: "A payment customization enables you to rename, reorder, hide the payment methods available to customers during checkout" (§ Payment Customization Function API)
- Fact: One use case: "Hide payment methods based on the customer's country." (§ Use cases)
- Fact: "The target returns an ordered list of operations to be applied to payment methods, payment terms, and review requirements." (§ Run target)
- Fact: "Your function receives only the fields that you request in the input query." (§ Input)
- Inference: Merchant and market rules about which methods are offered live in sandboxed functions, with a declared input and a closed set of output operations. They are separate from processing, so the processing contract does not change.

**1, 2, 3.** Not covered.

---

## E037 — Offline payments (Shopify POS)

- **Source:** Shopify Help Center, undated, accessed 2026-10-10.

**2 and 3.**
- Fact: "Offline transactions aren't routed to the payment processor." The guidance is to "reconnect to the internet as soon as possible, ideally within 24 hours." (§ Considerations for using offline payments)
- Fact: "Transaction limits automatically convert to local currencies for locations in different countries." (§ Considerations for using offline payments)
- Fact: Offline, "card payment orders display in the Orders tab with a Payment pending badge." Later, "If the payment is declined, then the order displays a Card declined badge." (§ Reconnect to the internet to process card payments)
- Inference: In POS offline mode, an order exists before its payment outcome is known, and the payment settles later. Order state and payment state are therefore separable. The merchant carries the risk, and limits bound the exposure.

**1, 4.** Not covered.

---

## E038 — Shopify/packwerk (repository)

- **Source:** README read 2026-10-10 through raw.githubusercontent.com, because github.com returned 403 here.
- **Releases (RubyGems):** 3.0.0 on 2023-03-01; 3.3.1 on 2026-08-26.

**1. Boundary tooling**
- Fact: "Packwerk is a Ruby gem used to enforce boundaries and modularize Rails applications." (README, intro)
- Fact: "Method calls and objects passed around the application are completely ignored. Packwerk only cares about static constant references." (README § Limitations)
- Fact: The public-API check now lives in packwerk-extensions: "a checker for packwerk that allows you to enforce public API boundaries. This was originally extracted from `packwerk` itself." (README § Ecosystem)
- Inference: Packwerk checks static references to constants. It cannot see runtime coupling such as shared tables or objects passed between components (compare E016, E022).

**2, 3, 4.** Not covered.

---

## E039 — Shopify/semian (repository)

- **Source:** README read 2026-10-10 through raw.githubusercontent.com.
- **Latest release:** 0.28.4 on 2026-09-07.

**3 and 4.**
- Fact: "Semian is a library for controlling access to slow or unresponsive external" services, "to avoid cascading failures". (README, intro)
- Fact: In the Net::HTTP adapter section: "Two requests to shopify.com can use two different semian resources," when a dynamic sub-resource name is set. `"#{host}_#{port}"` "is a good default `name`". (README § Net::HTTP)
- Inference: The dynamic sub-resource mechanism is what per-country payment circuits need (E001, E003). The README itself does not mention payments.

**1, 2.** Not covered.

---

## E040 — activemerchant/active_merchant (repository)

- **Source:** README read 2026-10-10 through raw.githubusercontent.com.
- **Latest gem:** 1.137.0 on 2024-08-02.
- **Maintainers:** Shopify and Spreedly.

**4. Provider variance**
- Fact: "Active Merchant is an extraction from the ecommerce system", followed by a link to Shopify. (README, intro)
- Fact: It was designed around Shopify's need for a "simple and unified API to access dozens of different payment" gateways. (README, intro)
- Fact: "ActiveMerchant accepts all amounts as Integer values in cents". The usage example calls `gateway.purchase(amount, credit_card)`. (README § Usage)
- Inference: This is Shopify's long-standing approach to provider differences: one gateway interface (purchase, authorize, capture, void, refund) with an adapter per gateway. No source says that CardServer's "adapter library" (E001) is Active Merchant; that link is inference only.

**1, 2, 3.** Not covered.

---

## What the sources agree on and where they differ

**Where payments lives: a mix, with the line drawn by card-data risk.**

The sources agree that Shopify did not make all of payments a service. They also agree it did not keep all of it in the monolith.

- **Inside the Rails monolith:**
  - checkout, orders, refunds and chargebacks;
  - a payments component that sits next to orders (E001, E020, E021, E022).
- **Outside it:**
  - card capture and vaulting: the CardSink and the vault service (E001, E002, E010, E019);
  - the app or service that holds card data and calls processors: CardServer and the "centralized payment service" (E001, E003, E004, E007);
  - buyer-wide products such as Shop Pay (E001, E014, E015).
- **Beyond Shopify:**
  - processors and acquirers, called "financial partners" (E003);
  - third-party providers built as payments apps (E030).

The stated reasons are PCI scope and sensitive data (E001, E019), plus the rule that work spanning several shops cannot live in shop-sharded core (E001, E024). Team autonomy is not the reason given. On splitting out services, Shopify says "we only do it for good reasons" (E019), and it calls microservices "a topology change" (E020).

**What crosses the line.**

The sources describe the same narrow hand-off:

- a card token rather than card data;
- payment metadata;
- caller-side ids;
- one idempotency key per payment attempt.

Where it appears:

- At the core-to-card-service boundary, the key is sent from a background job (E001, E002, E003).
- The result is a success or failure. Core turns a success into an order, and checkout completion also updates the merchant's payable balance (E001).
- Third-party providers see payment-scoped identifiers (attempt, group per checkout, session), and the payment session request carries no order ID (E032).
- Orders see payments as typed transactions with explicit pending and unknown states (E033).

Neighbouring flows hang off payment events: inventory is reserved when payment starts and claimed when it succeeds (E009). The sources show no domain-event or CDC contract between payments and orders. Shopify warns that table-level CDC couples consumers to internals (E023), and it uses versioned schemas where event contracts matter (E022).

**How consistency is kept.**

The sources agree on the same toolkit:

- short timeouts and circuit breakers (E001, E003, E039);
- an idempotency key per attempt, backed by a stored step log that can recover after a crash (E001, E002, E004);
- background jobs that run at least once, which is safe only because charges are idempotent (E006);
- reconciliation against partners, with recorded anomalies, as the backstop, covering individual charges and refunds and also the merchant balance (E003).

Unknown outcomes are named, not hidden:

- "the outcome is unknown" (E004);
- an UNKNOWN transaction status (E033);
- payment providers retry their result for up to 24 hours, and meanwhile may tell the buyer the payment went through but Shopify is unreachable (E031);
- POS creates orders as "Payment pending" (E037).

Recent public APIs push the same discipline out to apps. Refund idempotency became mandatory in API version 2026-04 (E035), with a 24-hour key window (E034).

**How provider and market variation is contained.**

The sources agree that variation is pushed below a standard call:

- an adapter library that turns one standardized call into processor-specific calls (E001);
- one handler class per payment method (E004);
- one internal gem per provider (E005);
- an Active Merchant lineage (E040; the link to E001 is inference).

Market failures are isolated by adding the country to the circuit key (E001, E003). Regulation was absorbed inside the payment service: India's e-mandates (E005), and PCI v4 inside the checkout host page and sandboxes (E010, E011). Rules about which methods to show are kept out of processing, as merchant or app functions (E036; compare E027). The newest designs make this explicit: providers publish their own handler specifications, and core "stays stable" (E012). New rails are fitted to the same authorize/capture/void/refund vocabulary (E013, E030, E033).

**Where they differ.**

- **How hard the boundaries inside the monolith are.**
  - 2019–2020 posts promise public APIs, exclusive data ownership and privacy enforcement (E019, E020, E021). In 2022, Packwerk was said to stop payments from bypassing the orders API (E001).
  - Later sources walk this back:
    - Payments and orders shared one shop-keyed database (E022).
    - Privacy checks were removed from Packwerk itself in 3.0, released March 2023, and moved to packwerk-extensions; whether Shopify still uses them is not stated. Domain components did not match how the code ran, and Shopify considered dropping Packwerk (E016, E038).
    - A Shopify keynote judged that coupling had not fallen (E018).
    - In 2026 Packwerk is still used but under-counted references (E017).
  - Plain reading: the strong boundary is the PCI-driven service boundary. The payments↔orders boundary inside the monolith is a soft convention.
- **Reconciliation as a primary or secondary tool.**
  - In 2019 the Money Infrastructure team chose idempotency over automatic reconciliation, because each new provider would need its own reconciliation work (E004).
  - The 2022 post treats reconciliation as standing practice (E003).
  - These fit together: idempotency keeps each request correct, and reconciliation keeps the records in step with partners and with balances.
- **Key formats and lifetimes.**
  - Random UUIDs (E004).
  - ULIDs, unique for 24 hours or less (E003).
  - Admin API keys kept for 24 hours (E034).
  - Payments-app keys that never expire (E031).
- **Which "payment service".**
  - E004 and E005 describe a GraphQL Payment Service used by Shopify and Billing for "certain payment methods".
  - E001 describes CardServer for card checkout.
  - E003 describes a "centralized payment service" that holds card data.
  - No source says whether these are one system or several, or whether merchant billing and buyer checkout share it.
- **Direct provider access.**
  - E005 says "a few systems" talked to the Indian provider directly, sharing a gem rather than a service.
  - So in 2022, sending every provider call through one service was not a universal rule.
- **Internal design versus external protocols.**
  - UCP and the payments-app contract describe a cleaner model than any internal source: a versioned core, provider-owned specifications, payment-scoped ids and asynchronous resolution (E012, E031, E032).
  - Whether Shopify's internal boundary now matches them is not stated.

**What the sources do not settle (gaps).**

- No 2023–2026 engineering source describes the internal Shopify Payments boundary directly. The detailed internal picture (E001–E005) is from 2019–2022.
- No source covers:
  - the internals of returns;
  - POS card processing, beyond help pages and two thin posts;
  - the Balance and payout ledger, beyond the remark that "The balance that needs to be paid out to the merchants needs to be updated." at checkout (E001), and balance-level reconciliation (E003);
  - how Shop Pay credentials reach checkout.
- No engineering source names Stripe or any other processor behind Shopify Payments.

**For Sharrwah, a plain reading of the evidence.**

- Shopify got a separately paced and separately regulated payments unit where it drew a hard line around card data and provider calls:
  - The rest of the platform hands over a token, metadata and an idempotency key.
  - It gets back a typed result.
  - Providers and markets vary behind an adapter.
- It did not get that independence for the payment logic that stayed inside the monolith next to orders. Those boundaries stayed soft and needed years of tooling.
