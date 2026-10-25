# S-01 review: who holds sellers' money

**What this file is:** the review pack for the first subject's result, after the founder answered Decision 1 on 25 October 2026. It follows the five checks the founder set. Every claim is a fact with its link, a reading or an assumption marked as one, or a decision named as one. Arabic quotes carry my translation in brackets.

## In short

- **What the method produced:** [S-01's register](../studies/subjects/S-01/register.tsv), 37 rows:
  - 7 drivers;
  - Decision 1 and its 3 defaults;
  - Decisions 2 to 12, settled by it;
  - 2 decisions moved to later subjects;
  - 9 points that follow by rule;
  - 4 engineering constraints for the design.

  A script checked every citation in it.
- **The five checks, one line each:**
  1. **Trace:** every decision has its drivers, evidence, alternatives, trade-off and recorded rationale.
  2. **Comparison:** Sharrwah's launch path is one every reference also runs. The one real architectural difference is that every reference also has a payment service of its own, and Sharrwah doesn't at launch. That is deliberate.
  3. **Yemen:** what C needs exists there today. What C gives up, Sharrwah holding money, would also need a licence Sharrwah doesn't have.
  4. **Premature constraints:** Decision 1 closes no mature capability for good, as long as the design keeps one rule (E2). Shopify's shipped schema shows that rule is workable. But the wording of two defaults, read literally, would close two capabilities for good.
  5. **Defects:** nine found. Seven are fixed or ruled. Two remain: one needs a line from you, and one goes to the design.
- **What I need from you:** one line on the scope of defaults 2 and 3 (section 4).

## 1. Trace: each decision to what drives it

**The drivers,** the requirements these decisions answer to ([register, first 7 rows](../studies/subjects/S-01/register.tsv)):

| Id | Driver | Source |
| --- | --- | --- |
| [S01-R1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L2) | One platform for many markets; Yemen is the first market, not the design target | [PLAN.md, section 1](../PLAN.md#1-the-aim-and-the-safe-shore) |
| [S01-R2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L3) | No arrangement holding sellers' money goes live without your decision | Your guard, [decisions file](../founder-decisions.tsv) |
| [S01-R3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L4) | Yemen must not define hard-to-change product decisions | [PLAN.md, section 1](../PLAN.md#1-the-aim-and-the-safe-shore) |
| [S01-R4](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L5) | *Reading:* at launch, sellers in the first market are paid the ways that work there | The Yemen facts in section 3 |
| [S01-R5](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L6) | What varies per market sits behind one interface, bound per market | [PLAN.md, section 6, step 5](../PLAN.md#the-test-form-per-subject) |
| [S01-R6](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L7) | Decisions expensive to change are made on evidence; cheap ones are left to the build | [PLAN.md, section 1](../PLAN.md#1-the-aim-and-the-safe-shore) |
| [S01-R7](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L8) | No production code before requirements, an architecture description and engineering documentation | Your decision of 24 October |

**Your decisions:**

| Id | Decision | Drivers | Alternatives | Trade-off | Rationale |
| --- | --- | --- | --- | --- | --- |
| [S01-D1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L9) | C in every market at launch: each provider holds the money, in the seller's own account | R1, R2, R4, R5, R6 | A: Sharrwah holds. B: a processor holds, in accounts opened through Sharrwah. Defer: the interface only | No payment service of Sharrwah's own at launch, so sellers open their own provider accounts. In return, Sharrwah holds no sellers' money and needs no licence to hold it | [Decision 1's page](../studies/subjects/S-01/decision-1.md#recommendation-c-in-every-market-at-launch) |
| [S01-D1.1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L10) | An account a seller requests through Sharrwah is C if it's under the seller's own agreement | R2, R4 | Treat every such account as B | Sharrwah can bring sellers to providers without being party to their money | [the page, edge 1](../studies/subjects/S-01/decision-1.md#three-edges-of-c-each-with-a-default) |
| [S01-D1.2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L11) | Sharrwah's fees are billed apart, never taken from sellers' money at a provider | R2, R6 | Deduct at a provider, which needs Sharrwah to be a party, B's side | Sharrwah carries the risk that invoices go unpaid | [the page, edge 2](../studies/subjects/S-01/decision-1.md#three-edges-of-c-each-with-a-default) |
| [S01-D1.3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L12) | No balance that sellers pay into | R2 | A wallet sellers top up, which is like A | Sellers pay Sharrwah by invoice or card | [the page, edge 3](../studies/subjects/S-01/decision-1.md#three-edges-of-c-each-with-a-default) |

The evidence for each is in its register row. For Decision 1 it is:
- **The references' own services come with conditions, market by market:** Shopify Payments is "only available to online stores in" "certain countries and regions" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/shopify-payments.md?plain=1#L9)).
- **C is open in both Shopify and Salla:** sellers' own providers and payment outside any provider (section 2).
- **Yemen's facts** (section 3).

**Decisions 2 to 12, settled by your answer** ([the pilot's table](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L131-L149)). Each takes column C. Each reopens only if A or B is switched on in a market, and then that column comes to you:
- [S01-D2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L13) who settles;
- [S01-D3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L14) who pays out;
- [S01-D4](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L15) who collects;
- [S01-D5](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L16) no agency role;
- [S01-D6](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L17) who deducts;
- [S01-D7](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L18) which accounts;
- [S01-D8](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L19) payout timing;
- [S01-D9](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L20) deducted or billed apart;
- [S01-D10](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L21) funds at termination;
- [S01-D11](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L22) funds back to buyers;
- [S01-D12](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L23) no security interest.

**Moved to later subjects:**
- **[S01-D13](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L24) instalments.** *Reading:* under C, the seller is paid on the instalment provider's own terms.
- **[S01-D14](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L25) currency.** The pilot's recommendation is not carried, for two reasons. It rests on a variant the ruling on finding 36 removes. And it was shaped by one market: it proposed "the rial recorded apart by the area its funds are held in". *Reading:* under C, Sharrwah holds no funds, so the currency subject asks about prices, orders and records instead.

**My engineering constraints,** for the architecture description. They are cheap to set now, while there's no code. You may veto any:

| Id | Constraint | Why |
| --- | --- | --- |
| [S01-E1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L35) | Who holds the money is a market's setting. It is C everywhere at launch, but not built into the platform | The rule in R5. Shopify and WooCommerce each run more than one arrangement ([S01-VP-01](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/analysis.tsv?plain=1#L2)) |
| [S01-E2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L36) | An order's payment record is the same whoever holds the money. A holder's ledger (balance, holds, payouts) is a separate part, present only where Sharrwah or a processor holds | Section 4: this is the shape that keeps A and B open |
| [S01-E3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L37) | Sharrwah's own fees live in a billing part, separate from sellers' payments | Default 2. Shopify puts transaction fees on its own bill when another provider holds the money ([Shopify's bill](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L8); [Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/getting-paid.md?plain=1#L11)) |
| [S01-E4](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/b1e17b23d9bc23c9d34d06b6d4585adedb499947/studies/subjects/S-01/register.tsv?plain=1#L38) | Refunds, captures and voids are carried out by the provider that took the payment, and its result is recorded on the order | Decision 11. Shopify's interface for outside payment providers works this way: the provider resolves or rejects each refund ([Shopify](https://shopify.dev/docs/api/payments-apps/2026-10/mutations/refundSessionResolve)) |

## 2. Compared with Shopify and the product class

**Who holds the money, in each reference:**

| Reference | Its own payment service, and who holds the money in it | Sellers' own provider accounts | Payment outside any provider |
| --- | --- | --- | --- |
| Shopify | Shopify Payments. "The Payment Processors may hold funds in your Shopify Payments Account" [S01-SH-022](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L23), and Shopify decides "which Payment Processor Account(s) we will facilitate opening on your behalf" [S01-SH-010](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L11). That is B. | "All Shopify-supported payment methods rely on third-party providers" [S01-SH-048](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L49) | Manual payment methods: "you can arrange to receive their payment in a way that works best for them" [S01-SH-103](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L104) |
| WooCommerce | WooPayments: "a Stripe Express account that is connected to the WooPayments service" [S01-WC-019](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L20), with "funds held by Stripe" [S01-WC-109](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L110). That is B. | "Using a Stripe account, you can accept payments" [S01-WC-022](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L23) | Its shipped bank-transfer method: "Make your payment directly into our bank account." [S01-WC-092](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L93) |
| BigCommerce | BigCommerce Payments: "a brand new PayPal platform account dedicated to your BigCommerce store is created" [S01-BC-068](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L69). That is B. | "You will control and direct funds in your merchant account with your merchant service provider." [S01-BC-088](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L89) | "a payment directly into your bank account by setting up a Bank Deposit payment method" [S01-BC-115](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L116) |
| Salla | Salla Payments: "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها" [the e-payments balance keeps the store's sales proceeds before transferring them] [S01-SA-056](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L57). Salla provides it "عبر شركائها" [through its partners] [S01-SA-078](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L79). To the seller, that is A. | "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة" [payments through Tabby are collected through Tabby, not through Salla Payments] [S01-SA-101](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L102) | "يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك" [the customer transfers the order amount directly from their bank account to yours] [S01-SA-098](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L99) |
| Zid | Zid Pay: "المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد" [the amounts in your Zid Pay balance not yet deposited to your bank account] [S01-ZD-034](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L35). To the seller, that is A. | With gateways other than Zid Pay, "يتطلب أن يكون لديك حساب لديهم" [you need an account with them] [S01-ZD-080](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L81) | Bank transfers, for which the seller bears "المسؤولية الكاملة" [full responsibility] [S01-ZD-075](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L76) |
| **Sharrwah at launch** | **None** | **Yes** (Decision 1, default 1) | **Yes** |

**Where the difference is architectural:**
- **It's in one place: who holds the money.** Every reference runs a payment service of its own beside sellers' own providers. Shopify, WooCommerce and BigCommerce use a processor that holds in an account the platform opens (B). Salla and Zid keep a balance of their own (A, as the seller sees it). Sharrwah, at launch, has neither.
- **That one difference carries others with it:** balances and payouts, how the platform collects its fees, reserves and holds, how refunds are funded, and what happens to money when a seller leaves. Each changes the data, the flow of money and the legal position, not just a screen.
- *Reading:* Sharrwah's launch is the path all five references share, without the extra arrangement each adds on top.

**Where the difference is only on the surface,** because the same screen can hide different architectures:
- **Cash on delivery.** On Salla, with Salla's own waybills, "تحوِّل شركة الشحن المبلغ إلى سلة" [the shipping company transfers the amount to Salla] [S01-SA-041](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L42). That is A. With the seller's own courier, "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة" [Salla doesn't collect cash-on-delivery amounts in this case] [S01-SA-090](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L91). That is C. The buyer sees the same thing either way. Sharrwah at launch is the second.
- **Buy now, pay later.** Even inside Salla, Tabby collects, not Salla Payments [S01-SA-101](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L102). Sharrwah can offer the same through default 1.
- **Refund buttons and the order's paid status.** Shopify records every payment the same way, whichever provider took it ([OrderTransaction](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/OrderTransaction)), and marks orders paid outside any provider ([orderMarkAsPaid](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/orderMarkAsPaid)). The admin can look the same under C.

## 3. The Yemen row

What each option needs in Yemen today, and whether it exists. The facts are Stage 1's, read with [its corrections](../studies/yemen-cases/corrections.md):

| What | What it needs there | Exists today? | Verdict |
| --- | --- | --- | --- |
| C, cash on delivery | A courier that collects for sellers | Yes: available to business accounts [YK-203](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L204) | Supported |
| C, transfer | Buyers paying sellers by money transfer | Yes [YA-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L132) | Supported |
| C, wallets | A wallet that takes online payments into the seller's own account | In part. Cash Pay offers its payment service to online stores by API ([YK-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L132), corrected to Cash Pay alone), and a wallet's own page says the amount is "added to your Cash Wallet account" ([YE-E765](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9d0de523f1852ebf7716f0da01b6b619edc5e8fc/evidence/yemen/runs/20261010T050304Z-cited-sources/items/211-cash.com.ye/text.txt?plain=1#L36)). Which wallets a seller may use can depend on the area ([YA-217](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L218), [YA-26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L27)) | Supported, wallet by wallet |
| C, cards | A card gateway or acquirer paying into the seller's own merchant account | Gateways and an acquirer exist ([YA-107](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L108), [YK-161](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L162)). Whose account they pay into isn't shown | Unknown: investigation I1 |
| International processors | A processor that serves businesses in Yemen | No: Stripe doesn't support businesses there ([YA-62](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L63), corrected). PayPal may only send, not receive ([YK-514](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L515), a caution resting on an undated article) | Restricted by the market, not by Sharrwah |
| A: Sharrwah holds | A licence in each area | Sharrwah has none. In each of the two areas, as of February 2026, a licence comes from that area's central bank ([YA-102](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L103), read per area as its caution says). In the internationally recognized government's area, a licence requires a joint-stock company with at least 500 million rials paid up ([YK-515](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L516), corrected) | Excluded by your decision, and out of reach today anyway |
| B: a processor holds through Sharrwah | A processor serving Yemen that holds in accounts a platform opens | None shown | Excluded by your decision. Not available, as far as the evidence shows |
| Fees deducted, a seller wallet, platform-collected cash on delivery | A or B | Neither | Excluded by defaults 2 and 3 and by C: deliberate trade-offs |

**Every restriction rests on evidence or on a stated trade-off:**
- What C needs exists, except card acquiring into the seller's own account, which is unknown.
- What's excluded is excluded by your decision. A and B also lack what they would need.
- Nothing in the row shaped the decision. A test made without Yemen reached the same decision. That is a test, not a source ([Decision 1's page](../studies/subjects/S-01/decision-1.md#recommendation-c-in-every-market-at-launch)).

## 4. Premature constraints

**Could Sharrwah adopt each mature capability later?**

| Capability | Where the references have it | Sharrwah at launch | Later? | What it would need |
| --- | --- | --- | --- | --- |
| A payment service of its own, held by a processor (B) | Shopify, WooCommerce, BigCommerce (section 2) | Off | Yes, if E1 and E2 hold | A processor that serves the market; your decision |
| A balance of its own (A) | Salla, Zid | Off | Yes, if E2 holds | A licence in the market; your decision |
| Fees deducted from payouts | Shopify Payments: fees "deducted from your payouts" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L12)) | Off (default 2) | **Only if default 2 means "at launch"** | B |
| A seller wallet that pays for platform charges | Salla: its wallet pays for "Auto-renewing your subscription plan" ([Salla](https://help.salla.sa/en/article/wallet-invoices-saudi-arabia/g36cl2hlsv256gr55vutx5rv)) | Off (default 3) | **Only if default 3 means "at launch"** | A |
| Cash on delivery collected by the platform | Salla's waybills [S01-SA-041](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L42); Zid collects "نيابة عن التاجر" [on the merchant's behalf] [S01-ZD-069](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L70) | Off | Yes | A |
| Financing repaid from sales | Salla: "Collection amounts are calculated from net Mada and credit card sales" ([Salla's dashboard](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/dashboard-translations/en/payments.json)) | Off | Yes, with A or B. *Reading:* under C, a provider could lend to sellers itself | A or B, or a provider |
| Cross-border sales through a partner that holds the money | Shopify: for international Managed Markets orders, "Shopify Payments processes the transaction and holds the money in a Global-e account" [S01-SH-098](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L99) | Off | Yes | B, and a partner |
| Buy now, pay later through the seller's own account | Salla [S01-SA-101](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L102) and Zid [S01-ZD-077](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L78), with Tabby | **On** (default 1) | | |
| Outside providers, and payment outside any provider | All five (section 2) | **On** | | |
| Refunds through the provider that took the payment | Shopify's interface for outside providers ([refunds](https://shopify.dev/docs/api/payments-apps/2026-10/mutations/refundSessionResolve)); Salla with Tamara [S01-SA-106](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L107); BigCommerce [S01-BC-088](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L89) | **On** (E4) | | |

**The shape that keeps A and B open is in Shopify's shipped schema.** These are facts from Shopify's own API definition, held in observed-sh:
- Every payment on an order is the same kind of record, whichever provider took it, with a field for a manual payment ([OrderTransaction](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/OrderTransaction): `gateway`, `manualPaymentGateway`). Shopify Payments' own details hang off an optional part of that record (`shopifyPaymentsSet`).
- Money Shopify holds through its own service lives in a separate account object, with its balance, balance entries, payouts, payout schedule and disputes ([ShopifyPaymentsAccount](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/ShopifyPaymentsAccount)).
- That account's entries point back to the order's payment record ([ShopifyPaymentsBalanceTransaction](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/ShopifyPaymentsBalanceTransaction): `sourceOrderTransactionId`).
- The held copy is observed-sh's `structures/shopify/admin-graphql-schema/2026-10/items.jsonl` at `febbf6c`, taken from Shopify's own endpoint on 30 September 2026.

**Salla's API shows the other shape,** a balance in the middle:
- an app may "temporarily withhold a specific amount of money for settlement from the Merchant's wallet" ([Salla](https://docs.salla.dev/settlements/create.md));
- refunds need the balance: "The store must have enough balance to process the refund amounts" ([Salla](https://docs.salla.dev/transactions/update.md)).

*Reading:* Shopify's separation is what lets it run its own service beside outside providers. E2 adopts that separation now, before any code, at no cost. It stays a reading until the architecture description shows the design holds to it (R7). That is where I'll check it, before any code.

**Two defaults, read literally, would close two capabilities for good.**
- **The wording:**
  - Default 2 says Sharrwah's fees are "never taken from sellers' money at a provider".
  - Default 3 says there's no balance sellers pay into.
- **If these mean "ever":** even after you switch on B or A in a market, Sharrwah couldn't deduct its fees as Shopify Payments does, or offer a wallet as Salla does. Those are rows 3 and 4 of the table above.
- **The decision page offered all three defaults "for launch".** I recommend reading them that way: at launch, and while a market runs only C. If you switch on A or B in a market, fees and balances there come to you with that decision.
- **Answer:** at launch / in every arrangement

## 5. Defects and deliberate choices

| # | What was found | Kind | Correction or investigation | Status |
| --- | --- | --- | --- | --- |
| 1 | Three Salla gaps sent to you asked for a page we already hold | Defect: routing | Read the held page. It shows the verification requirements, not the payment contract. The rest is needed only if A or B comes back ([gaps](../studies/subjects/S-01/salla/gaps.tsv)) | Fixed |
| 2 | Five statements had a source kind that the rules now give differently | Defect: rules changed after G1 | Kinds regenerated. No open decision rests on them | Fixed |
| 3 | A variant naming only what's excluded from the role (finding 36) | Defect: method | Ruled ([phase B brief](../studies/subjects/S-01/briefs/B-variation-points.md)). Decision 14's pilot reading is not carried | Fixed |
| 4 | Decision 14's pilot recommendation was shaped by Yemen ("the rial recorded apart by the area its funds are held in") | Defect: against R3 | Not carried. The currency subject starts from the references | Fixed |
| 5 | The pilot split one decision into 23 sub-questions and 14 items, and one answer settles 11 of them | Defect: method | Stage 4 starts from root decisions ([PLAN.md](../PLAN.md#stage-4-the-subjects-one-at-a-time-riskiest-first)) | Fixed in the plan |
| 6 | Decision 1's page didn't mention Yemen's local card gateways | Omission | Added to the Yemen row, with investigation I1 | Fixed here |
| 7 | My summary to you on 25 October presented readings as facts | Defect: reporting | Withdrawn the same day | Fixed |
| 8 | "A and B can be added later" was an assumption | Gap: evidence | Now E2, backed by Shopify's shipped schema. Checked when the architecture description is written | Open: design |
| 9 | Defaults 2 and 3 could be read as permanent | Wording | Your one line (section 4) | Open: you |

**Deliberate, evidence-backed choices, not defects:**
- C at launch, with the three defaults;
- Decisions 2 to 12 by C;
- no payment service of Sharrwah's own at launch;
- the cut of Yemen's scenarios.

**Open questions, each with the work that would settle it:**
- **I1:** do Yemen's card gateways and acquirer ([YA-107](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L108), [YK-161](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L162)) pay into the seller's own merchant account? Their merchant terms, captured before the payment-methods subject.
- **I2:** which Yemeni wallets let a platform connect sellers' own wallet accounts, in each area ([YK-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L132), [YA-217](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L218), [YA-26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L27))? Their merchant and API terms, in the payment-methods subject.
- **I3:** does C need any registration for Sharrwah in a market? A lawyer, when each market is set up.
- **I4:** which entity holds Salla Payments' money, and under which licence? Only if A or B comes back.
- **I5:** several sellers in one checkout, a marketplace, would need a processor that splits payments (B). It isn't in S-01's evidence. If G2 puts a marketplace in scope, it becomes a subject.
- **I6:** can PayPal receive money in Yemen ([YK-514](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L515))? PayPal's own country list.

## Risks, and how they're managed

| Risk | How it would show | What controls it | Checked |
| --- | --- | --- | --- |
| The design builds C into orders, and A or B later means rework | A payment record that assumes the provider holds, or posts into a seller balance | E1 and E2, written into the architecture description and checked there | Before any code |
| Defaults 2 and 3 read as permanent | A later B or A can't net fees or offer a wallet | Your one line | Now |
| Sellers find their own provider accounts hard to open | Slow onboarding in the first market | Default 1; the providers' onboarding terms (I2) | In the payment-methods subject |
| Sharrwah's invoices go unpaid | Fees outstanding | A billing part with its own collection rules (E3) | In the design |
| Yemen's licensing or wallet rules change | A dated fact in the Yemen row stops holding | Facts are dated and re-checked at market setup. Switching on A or B is yours anyway | At market setup |
| C still needs a registration somewhere | A lawyer says so | I3, per market | At market setup |
| The method over-produces again | A subject runs past its budget | Root decisions first, a budget per subject, and a stop at a quarter over | Every subject |

## Does the result hold?

- **Where it holds.** *My reading,* on the evidence above:
  - The decision is the path all five references share.
  - It keeps your guard.
  - It fits what Yemen offers today.
  - It closes no mature capability for good, as long as E1 and E2 are kept and the defaults are scoped to launch.
- **Where the method was weak:**
  - The pilot cost about 1.03 billion tokens, half of it rework ([method report](../studies/subjects/S-01/method-report.md#12-what-a-subject-costs)).
  - It split one decision 23 ways.
  - One of its recommendations, on currency, was shaped by Yemen.
  - Its list of what each option needs built was the coordinator's grouping. Tonight's schema evidence now backs it.
- **What isn't tested yet:**
  - the architecture, which isn't designed;
  - whether sellers in Yemen find C workable in practice, which needs the providers' terms (I1, I2).

## What it cost

| Work | Tokens |
| --- | --- |
| The pilot (for reference) | about 1.03 billion |
| Tonight: the independent review of this pack | to be filled in |
| My own session | not metered by `method/count_tokens.py` |

## What I need from you

- **Defaults 2 and 3:** at launch / in every arrangement.
- **E1 to E4:** veto any, or none.
