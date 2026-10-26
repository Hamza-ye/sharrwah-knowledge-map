# S-01 review: who holds sellers' money

**What this file is:** the review pack for the first subject's result, after the founder answered Decision 1 on 25 October 2026. It follows the five checks the founder set. Every claim is one of four:
- a fact, with its link;
- a reading, marked as one;
- an assumption, marked as one;
- a decision, named as one.

Arabic quotes carry my translation in brackets. An independent reviewer tried to break the first draft of this pack, and its findings are applied ([how each was handled](../studies/subjects/S-01/review-2.md)).

## In short

- **What the method produced:** [S-01's register](../studies/subjects/S-01/register.tsv), 37 rows:
  - 7 drivers;
  - Decision 1 and its 3 defaults;
  - Decisions 2 to 12, settled by it;
  - 2 decisions moved to later subjects;
  - 9 points that follow by rule;
  - 4 constraints for the design.

  `python3 -I method/check_register.py studies/subjects/S-01/register.tsv` checks its 201 citations, and finds no problem.
- **The five checks, one line each:**
  1. **Trace:** every decision has its drivers, evidence, alternatives, trade-off and recorded rationale.
  2. **Comparison:** *my reading* is that Sharrwah's launch path is the one the references also offer: sellers' own providers, and payment outside any provider. The one architectural difference is that every reference also has a payment service of its own, and Sharrwah doesn't at launch. That is deliberate.
  3. **Yemen:** cash on delivery and transfers are shown working. Wallets are shown in part. Card payments into the seller's own account are unknown. What's excluded is excluded by your decision.
  4. **Premature constraints:** *my reading* is that Decision 1 closes no mature capability for good. That holds if the design keeps A and B possible, and keeping them possible is your decision to make. One word, "never" in default 2, could close two capabilities for good if read beyond launch.
  5. **Defects:** the review checked 71 claims in the first draft. 16 didn't hold, and 6 held only once a dropped scope or date was put back. A script then checked every quote against the line it cites, and found 4 more slips. All are corrected here.
- **What I need from you:** two answers, and G2 when convenient. They're in the last section.

## 1. Trace: each decision to what drives it

**The drivers,** the requirements these decisions answer to:

| Id | Driver | Source |
| --- | --- | --- |
| [S01-R1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L2) | One platform for many markets; Yemen is the first market, not the design target | [PLAN.md, section 1](../PLAN.md#1-the-aim-and-the-safe-shore) |
| [S01-R2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L3) | No arrangement that holds sellers' money through Sharrwah goes live anywhere without your decision | Your guard, [decisions file](../founder-decisions.tsv) |
| [S01-R3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L4) | Yemen must not define hard-to-change product decisions | The plan's rule, from your request of 24 October ([PLAN.md, section 1](../PLAN.md#1-the-aim-and-the-safe-shore)) |
| [S01-R4](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L5) | *Reading:* at launch, sellers in the first market can be paid in ways that work there | Tested by the Yemen row (section 3). It drives no decision |
| [S01-R5](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L6) | What varies per market sits behind one interface, bound per market | [PLAN.md, section 6, step 5](../PLAN.md#the-test-form-per-subject) |
| [S01-R6](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L7) | Decisions expensive to change are made on evidence; cheap ones are left to the build | [PLAN.md, section 1](../PLAN.md#1-the-aim-and-the-safe-shore) |
| [S01-R7](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L8) | No production code before requirements, an architecture description and engineering documentation | Your decision of 24 October |

**Your decisions.** Each id opens its row in the register, which also carries its evidence:

| Id | Decision | Drivers | Alternatives | Trade-off | Rationale |
| --- | --- | --- | --- | --- | --- |
| [S01-D1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L9) | C in every market at launch: each provider holds the money, in the seller's own account | R1, R2, R5, R6 | A: Sharrwah holds. B: a processor holds, in accounts opened through Sharrwah. Defer: the interface only | No payment service of Sharrwah's own at launch, so sellers open their own provider accounts. In return, Sharrwah holds no sellers' money, and carries none of the duties of holding it | [Decision 1's page](../studies/subjects/S-01/decision-1.md#recommendation-c-in-every-market-at-launch) |
| [S01-D1.1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L10) | An account a seller requests through Sharrwah is C if it's under the seller's own agreement | R2 | Treat every such account as B | Sharrwah can bring sellers to providers without being party to their money | [the page, edge 1](../studies/subjects/S-01/decision-1.md#three-edges-of-c-each-with-a-default) |
| [S01-D1.2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L11) | Sharrwah's fees are billed apart, never taken from sellers' money at a provider | R2, R6 | Deduct at a provider, which needs Sharrwah to be a party, B's side | Sharrwah carries the risk that invoices go unpaid | [the page, edge 2](../studies/subjects/S-01/decision-1.md#three-edges-of-c-each-with-a-default) |
| [S01-D1.3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L12) | No balance that sellers pay into, at launch | R2 | A wallet sellers top up, which is like A | Sellers pay Sharrwah by invoice or card | [the page, edge 3](../studies/subjects/S-01/decision-1.md#three-edges-of-c-each-with-a-default) |

**What Decision 1 rests on.** Its page gives four reasons:
1. the pilot's analysis;
2. the conditions both references put on their own services;
3. what every market shares;
4. Yemen's facts.

The first three come from the references. The fourth is Yemen's, so it is a check rather than a driver. A test made without Yemen reached the same decision (a test, not a source: [the page](../studies/subjects/S-01/decision-1.md#recommendation-c-in-every-market-at-launch)). *My reading:* Yemen's facts confirm the decision but don't decide it.

**Decisions 2 to 12, settled by your answer** ([the pilot's table](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L131-L149)). Each takes column C. Each reopens only if A or B is switched on in a market, and then that column comes to you:
- [S01-D2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L13) who settles;
- [S01-D3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L14) who pays out;
- [S01-D4](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L15) who collects;
- [S01-D5](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L16) no agency role;
- [S01-D6](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L17) who deducts;
- [S01-D7](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L18) which accounts;
- [S01-D8](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L19) payout timing;
- [S01-D9](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L20) deducted or billed apart;
- [S01-D10](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L21) funds at termination;
- [S01-D11](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L22) funds back to buyers;
- [S01-D12](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L23) no security interest. Shopify's terms take one: "a first priority lien and security interest" [S01-SH-023](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L24). Under C, Sharrwah has nothing to take one in.

**Moved to later subjects:**
- **[S01-D13](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L24) instalments.** *Reading:* under C, the seller is paid on the instalment provider's own terms.
- **[S01-D14](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L25) currency.** The pilot's recommendation is not carried, for two reasons:
  - it rests on a variant that the ruling on finding 36 removes;
  - it was shaped by one market: it proposed "the rial recorded apart by the area its funds are held in" ([the pilot's entry](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L340)).

  *Reading:* under C, Sharrwah holds no funds, so the currency subject asks about prices, orders and records instead.

**Four constraints for the design** ([S01-E1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L35) to [S01-E4](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L38)):
- **E1 and E2 keep A and B possible.**
  - **E1:** who holds the money is a market's setting, not built into the platform.
  - **E2:** an order's payment record is the same whoever holds the money, and a holder's ledger is a separate part.
  - These are building ahead: whether a variation point stays open or is bound now. [The plan makes that yours](../PLAN.md#3-who-does-what) (section 3, item 3), and so does your guard. So they are a decision for you, in section 4, not a veto.
- **E3 and E4 follow from C itself,** and are mine. You may veto either.
  - **E3:** Sharrwah's own fees live in a billing part, separate from sellers' payments.
  - **E4:** a refund is carried out by whoever holds the money (the provider, or the seller for payment outside any provider), or goes to the seller's store credit. The result is recorded on the order.

## 2. Compared with Shopify and the product class

**Who holds the money, in each reference.** Which option each one resembles is my reading:

| Reference | Its own payment service | Sellers' own provider accounts | Payment outside any provider |
| --- | --- | --- | --- |
| Shopify | Shopify Payments: "The processing and settlement of Transactions ... is carried out by one or more Payment Processors" [S01-SH-006](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L7), in accounts Shopify will "facilitate opening on your behalf" [S01-SH-010](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L11). *Reading:* B | "Enter your account credentials for the provider that you selected" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md?plain=1#L32)). Where Shopify Payments is supported, "Stripe won't be available for you to activate" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/third-party-providers/payment-gateway-availability.md?plain=1#L17)) | Manual methods: "you can arrange to receive their payment in a way that works best for them" [S01-SH-103](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L104) |
| WooCommerce | WooPayments: "a Stripe Express account that is connected to the WooPayments service" [S01-WC-019](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L20). "User appoints Stripe as User's agent for the limited purpose of directing, receiving, holding and settling funds" [S01-WC-120](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L121). *Reading:* B | "Using a Stripe account, you can accept payments" [S01-WC-022](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L23) | Its shipped bank-transfer method: "Make your payment directly into our bank account." [S01-WC-092](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/woocommerce/statements.tsv?plain=1#L93) |
| BigCommerce | BigCommerce Payments, offered under beta terms [S01-BC-059](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L60): "a brand new PayPal platform account dedicated to your BigCommerce store is created" [S01-BC-068](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L69). *Reading:* B | "You will control and direct funds in your merchant account with your merchant service provider." [S01-BC-088](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L89) | "a payment directly into your bank account by setting up a Bank Deposit payment method" [S01-BC-115](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/bigcommerce/statements.tsv?plain=1#L116) |
| Salla | Salla Payments, in the UAE: "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها" [the e-payments balance keeps the store's sales proceeds before transferring them] [S01-SA-056](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L57). Provided "عبر شركائها" [through its partners] [S01-SA-078](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L79). Who holds the money behind the balance isn't shown (I4). *Reading:* A, as the seller sees it | In the UAE, Tabby: "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة" [payments through Tabby are collected through Tabby, not through Salla Payments] [S01-SA-101](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L102) | On the Basic plan: "يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك" [the customer transfers the order amount directly from their bank account to yours] [S01-SA-098](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L99) |
| Zid | Zid Pay: "المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد" [the amounts in your Zid Pay balance not yet deposited to your bank account] [S01-ZD-034](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L35). *Reading:* A, as the seller sees it | Only two run beside Zid Pay: "لا يمكن تفعيل أي بوابة دفع أخرى مع زد باي باستثناء تمارا و تابي" [no other gateway can be activated with Zid Pay except Tamara and Tabby] [S01-ZD-109](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L110). For Tabby, Zid requests the seller's own account: "سنقوم بطلب إنشاء الحساب لك" [we'll request the account to be created for you] [S01-ZD-077](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L78) | Bank transfers, for which the seller bears "المسؤولية الكاملة" [full responsibility] [S01-ZD-075](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L76) |
| **Sharrwah at launch** | **None** | **Yes**, and Sharrwah may request accounts for sellers (default 1), as Zid does with Tabby | **Yes** |

**Where the difference is architectural** (each point is my reading):
- **It's in one place: who holds the money.**
  - Every reference offers a payment service of its own, and outside providers too.
  - Some limit which outside providers can run beside their own: Zid allows only Tabby and Tamara beside Zid Pay, and Shopify doesn't offer Stripe where Shopify Payments is supported.
  - Sharrwah, at launch, has no service of its own, so it has nothing to limit them with.
- **That one difference carries others with it:** balances and payouts, how the platform collects its fees, reserves and holds, how refunds are funded, and what happens to money when a seller leaves.

**Where the difference is only on the surface,** because the same screen can hide different architectures:
- **Cash on delivery.** The buyer sees the same thing either way, but on Salla it can run two ways:
  - with Salla's own waybills, "تحوِّل شركة الشحن المبلغ إلى سلة" [the shipping company transfers the amount to Salla] [S01-SA-041](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L42), under the concern for cash on delivery through Salla's labels [SA-C-115](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L77);
  - with a courier outside Salla's waybills, "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة" [Salla doesn't collect cash-on-delivery amounts in this case] [S01-SA-090](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L91).

  Sharrwah at launch works the second way.
- **Buy now, pay later.** Even inside Salla, Tabby collects, not Salla Payments [S01-SA-101](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L102). Sharrwah can offer the same through default 1.
- **The order's payment record.** Shopify's schema has one record type for an order's payment, with the provider as a field and a flag for manual payments ([OrderTransaction](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/OrderTransaction); held: [observed-sh, line 2447](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2447)). It also has a way to mark an order paid outside any provider ([orderMarkAsPaid](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/orderMarkAsPaid); held: [line 2268](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2268)). *Reading:* an order's paid status and refund button can look the same under C.

## 3. The Yemen row

What each option needs in Yemen today, and what the evidence shows, with dates. I checked each fact against its quotes tonight, and read it with [Stage 1's corrections](../studies/yemen-cases/corrections.md):

| What | What it needs there | What the evidence shows | Verdict |
| --- | --- | --- | --- |
| C, cash on delivery | Someone who collects cash from the buyer for the seller | A store takes cash on delivery inside Sana'a ([YE-C536](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/citations.tsv?plain=1#L1069), its own page, captured 10 October 2026). A courier, Torod Express, gives business accounts "إمكانية تحصيل الأموال من المستلمين" [the ability to collect money from recipients] ([YK-203](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L204); held: [line 141](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9d0de523f1852ebf7716f0da01b6b619edc5e8fc/evidence/yemen/runs/20261010T050304Z-cited-sources/items/180-torodexpress.com/text.txt?plain=1#L141), captured 10 October 2026). Its page describes its services as "في اليمن" [in Yemen] ([the page's source, line 20](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9d0de523f1852ebf7716f0da01b6b619edc5e8fc/evidence/yemen/runs/20261010T050304Z-cited-sources/items/180-torodexpress.com/raw.html?plain=1#L20)), without naming an area. On connecting an online store: "جاري العمل على توفير الخدمة قريباً" [work is under way to provide the service soon] ([line 145](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9d0de523f1852ebf7716f0da01b6b619edc5e8fc/evidence/yemen/runs/20261010T050304Z-cited-sources/items/180-torodexpress.com/text.txt?plain=1#L145)) | Supported in Sana'a. One courier in Yemen collects for business accounts; its area isn't stated, and connecting online stores is still to come (I7) |
| C, transfer | Buyers paying sellers by money transfer | Stores take transfers, and a 2025 report describes buyers paying in advance by transfer ([YA-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L132), quotes of 2025 and captures of 10 October 2026) | Supported |
| C, wallets | A wallet that takes online payments into the seller's own account | Cash Pay offers its payment service to online stores by API ([YK-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L132), corrected to Cash Pay alone). Its page says the amount is "added to your Cash Wallet account", and gives an address in Sana'a ([YE-E765, lines 36 and 56](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9d0de523f1852ebf7716f0da01b6b619edc5e8fc/evidence/yemen/runs/20261010T050304Z-cited-sources/items/211-cash.com.ye/text.txt?plain=1#L36-L56)). Providers from Sana'a may work in Aden only with separate infrastructure there ([YK-124](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L125), corrected, as of 5 April 2024) | Supported for Cash Pay. *Reading:* whether it serves sellers in Aden's area is unknown (I2) |
| C, cards | A card gateway or acquirer paying into the seller's own merchant account | MEPS Yemen lets banks offer card acceptance to merchants, for local and international cards. A 2025 blog in the same record says reliable gateways are lacking ([YA-107](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L108)). SabaCard acquires cards for Yemen's banking market ([YK-161](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L162), captured 10 October 2026). Whose account a merchant's card payments land in isn't shown | Unknown (I1) |
| International processors | A processor that serves businesses based in Yemen | Stripe doesn't support businesses in Yemen ([YA-62](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L63), corrected). WooPayments has an open request to add Yemen. PayPal may only send, not receive ([YK-514](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L515), a caution resting on an undated article). Two outside services say they make such services available ([YA-62](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L63)) | Not shown directly. Restricted by the market, not by Sharrwah |
| A: Sharrwah holds | *The pilot's reading:* a licence in each area | In the internationally recognized government's area (as of February 2026), payment services need a licence from the central bank. The licence requires a joint-stock company with at least 500 million rials paid up, under the central bank's instructions of 13 September 2022, which it may raise or lower at any time ([YK-515](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L516), corrected). In the Houthis' area (as of 11 February 2026), banks and fintech companies issue e-money with the central bank in Sana'a, and non-bank institutions were made eligible in 2020 to obtain a licence for e-rial services ([YA-102](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L103), read as [its caution](../studies/yemen-cases/corrections.md) states it) | Excluded by your decision. *Assumption:* Sharrwah holds no such licence today |
| B: a processor holds through Sharrwah | A processor serving Yemen that holds in accounts a platform opens, and perhaps the platform's own registration | None shown. Elsewhere, Shopify is "registered as a Payment Facilitator" where those terms apply [S01-SH-105](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L106) | Excluded by your decision. Not available, as far as the evidence shows |
| Fees deducted, a seller wallet, platform-collected cash on delivery | A or B | Neither | Excluded by defaults 2 and 3, and by C: deliberate trade-offs |

**In short:**
- Of C's ways to pay, cash on delivery and transfers are shown, wallets in part, and card payments into the seller's own account are unknown.
- What's excluded is excluded by your decision, and A and B also lack what they would need there.
- Yemen's facts confirm the decision without deciding it (section 1).

## 4. Premature constraints

**Could Sharrwah adopt each mature capability later?** "Yes" means the decision leaves it open. It doesn't mean it would be easy.

| Capability | Where the references have it | Sharrwah at launch | Later? | What it would need |
| --- | --- | --- | --- | --- |
| A payment service of its own, held by a processor (B) | Shopify Payments and WooPayments; BigCommerce Payments, under beta terms | Off | Yes, if A and B are kept possible (your decision below) | A processor that serves the market. Perhaps Sharrwah's own registration, as Shopify is "registered as a Payment Facilitator" [S01-SH-105](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L106). And your decision |
| A balance of its own (A) | Salla, Zid | Off | Yes, if A and B are kept possible | A licence in the market, and your decision |
| Fees deducted from payouts | Shopify Payments: fees "deducted from your payouts" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L12)) | Off (default 2) | **Only if "never" means at launch** | B |
| A seller wallet that pays for platform charges | Salla's wallet pays for "Auto-renewing your subscription plan" ([Salla](https://help.salla.sa/en/article/wallet-invoices-saudi-arabia/g36cl2hlsv256gr55vutx5rv); held: [observed-sa, record 1240](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/help-articles/en/texts.jsonl?plain=1#L1241)) | Off (default 3, at launch) | Yes | A |
| Cash on delivery collected by the platform | Salla's waybills [S01-SA-041](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L42). Zid collects "نيابة عن التاجر" [on the merchant's behalf] and deducts its fees from what it collects [S01-ZD-069](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L70) | Off | Yes. Its fees deducted from what's collected **only if "never" means at launch** | A |
| Financing repaid from sales | Salla: "Collection amounts are calculated from net Mada and credit card sales" ([Salla's dashboard](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/dashboard-translations/en/payments.json)). Shopify Capital: "Loan repayments are made from a daily percentage rate of your daily sales" ([SH-C-091](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1820)), and it is "available to eligible merchants who either use Shopify Payments or approved third-party payment providers" ([SH-C-091](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1818)). Zid's lender is repaid "عن طريق الاستقطاع من عمليات بيع التاجر المنفذة على منصة زد لحلول الدفع" [by deduction from the merchant's sales made on Zid's payment platform] ([ZD-C-023](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/zid/statements.tsv?plain=1#L176)) | Off | Yes. Zid's way needs its own payment service, so A. Shopify offers Capital beside outside providers too, so a lender may not need A or B; how it collects then isn't shown. Taken from sellers' money at a provider **only if "never" means at launch** | A lender, and how it collects; your decision |
| Apps withholding from the seller's balance | Salla, for dropshipping apps only: "temporarily withhold a specific amount of money for settlement from the Merchant's wallet" ([Salla](https://docs.salla.dev/settlements/create.md); held: [observed-sa, line 64](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/docs-operations/md-openapi/items.jsonl?plain=1#L64)) | Off | Yes | A |
| A money account for sellers through the platform | Shopify Balance ([SH-C-088](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/shopify/concerns.tsv?plain=1#L89)) | Off: at launch, a Sharrwah account serves only its own billing ([S01-D7](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L18)) | Yes | A, or a partner; your decision |
| Cross-border sales through a partner that holds the money | For international Managed Markets orders, "Shopify Payments processes the transaction and holds the money in a Global-e account" [S01-SH-098](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/shopify/statements.tsv?plain=1#L99) | Off | Yes | B, and a partner |
| Store credit and customer wallets | A refund can go to Shopify's store credit ([RefundMethodInput](https://shopify.dev/docs/api/admin-graphql/2026-10/input-objects/RefundMethodInput); held: [observed-sh, line 2820](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2820)). Salla and Zid have customer wallets ([SA-C-063](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L42), [ZD-C-019](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/zid/concerns.tsv?plain=1#L20)) | *Reading:* on, as the seller's own credit. A wallet holding buyers' money through Sharrwah: off | Yes | Whose money a wallet holds (I8). If Sharrwah's, A |
| Selling on a marketplace that collects and pays the seller | Zid with Trendyol: "يتم الدفع إلى ترينديول ثم تقوم ترينديول بتحويل الأموال إليك" [payment goes to Trendyol, then Trendyol transfers the money to you] [S01-ZD-097](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L98), into the seller's own Trendyol account [S01-ZD-100](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L101) | *Reading:* on, as C. The marketplace holds, in the seller's own account | | |
| Buy now, pay later through the seller's own account | Salla [S01-SA-101](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L102) and Zid [S01-ZD-077](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/zid/statements.tsv?plain=1#L78), with Tabby | **On** (default 1) | | |
| Outside providers, and payment outside any provider | All five (section 2) | **On** | | |
| Refunds by whoever holds the money | Shopify's interface for outside providers lets them resolve or reject refunds ([refundSessionResolve](https://shopify.dev/docs/api/payments-apps/2026-10/mutations/refundSessionResolve); held: [observed-sh, line 26](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl?plain=1#L26)). In Salla, Tamara refunds come "من تمارا وليس من رصيد مدفوعات سلة" [from Tamara, not from Salla Payments' balance] [S01-SA-106](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/salla/statements.tsv?plain=1#L107) | **On** (E4) | | |

**Shopify's shipped schema shows a shape that keeps A and B open.** These are facts from Shopify's own API definition, held in observed-sh at `febbf6c` as taken from Shopify on 30 September 2026:
- **One payment record per order, whichever provider:** there is one record type for an order's payment ([OrderTransaction](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/OrderTransaction); held: [line 2447](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2447)). It has the provider as a field (`gateway`) and a flag for manual payments (`manualPaymentGateway`). Shopify Payments' own details sit in an optional part (`shopifyPaymentsSet`).
- **A separate account for its own service:** money held through Shopify Payments, by its processors, is tracked in a separate account object, with its balance, balance entries, payouts, payout schedule and disputes ([ShopifyPaymentsAccount](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/ShopifyPaymentsAccount); held: [line 3193](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3193)).
- **That account's entries point back to the order's payment** ([ShopifyPaymentsBalanceTransaction](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/ShopifyPaymentsBalanceTransaction), `sourceOrderTransactionId`; held: [line 3197](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3197)).

**Salla's API shows the other shape,** with a balance in the middle:
- **Dropshipping apps can withhold:** they may "temporarily withhold ... money for settlement from the Merchant's wallet" ([Salla](https://docs.salla.dev/settlements/create.md); held: [line 64](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/docs-operations/md-openapi/items.jsonl?plain=1#L64)).
- **Refunds need the balance:** "The store must have enough balance to process the refund amounts" ([Salla](https://docs.salla.dev/transactions/update.md); held: [line 211](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/docs-operations/md-openapi/items.jsonl?plain=1#L211)).

*Reading:* Shopify's separation is what lets it run its own service beside outside providers. E1 and E2 adopt it before any code. It stays a reading until the architecture description shows a design that holds to it. That check comes before any code (R7).

**A decision for you: keep A and B possible in the design?** ([S01-E1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L35), [S01-E2](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/studies/subjects/S-01/register.tsv?plain=1#L36)). It is building ahead, which the plan makes yours.

| Option | What it costs | What it gives |
| --- | --- | --- |
| **Keep them possible: E1 and E2** | A second kind of record in the design, the holder's ledger, left empty at launch. No code yet | A or B later adds a part, not a rework of orders and refunds |
| **Bind C now** | The simplest design | A or B later means reworking orders, refunds and fees |
| **Decide when the architecture description is written** | The decision waits a little | The design starts without this constraint |

**My recommendation:** keep them possible. The guard keeps A and B off either way. This only keeps your future decision cheap.

**One word in default 2.** Your recorded answer scopes everything "in every market at launch". Default 2 alone says "never": Sharrwah's fees are "never taken from sellers' money at a provider" ([your answer](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/6326d0c57509f053e332ef2dccc47d2dd5845d2a/founder-decisions.tsv?plain=1#L16)).
- **If "never" means at launch,** and while a market runs only C, three capabilities above stay open: fees deducted from payouts, a platform's cash-on-delivery fees taken from what it collects, and financing repaid from sales. Each would come to you with A or B.
- **If it means in every arrangement,** those three close for good.

## 5. Defects and deliberate choices

**Found and fixed tonight:**

| # | What was found | Correction |
| --- | --- | --- |
| 1 | Three Salla gaps sent to you asked for a page we already hold | Read the page. It shows the verification requirements, not the payment contract. The rest is needed only if A or B comes back |
| 2 | Five statements had a source kind the rules now give differently | Kinds regenerated. No open decision rests on them |
| 3 | A variant naming only what's excluded from the role (finding 36) | Ruled. Decision 14's pilot reading is not carried |
| 4 | Decision 14's pilot recommendation was shaped by Yemen | Not carried. The currency subject starts from the references |
| 5 | The pilot split one decision into 23 sub-questions and 14 items, and one answer settles 11 of them | Stage 4 starts from root decisions |
| 6 | Decision 1's page quoted Shopify's fees without the quote's condition ("If you don't activate Shopify Payments ...", [held](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/getting-paid.md?plain=1#L11)) | Corrected on the page and in the register. Default 2's support stands |
| 7 | The first draft of this pack: 16 of 71 checked claims didn't hold, and 6 more had dropped a scope or date. Among them: Yemen named as a driver of Decision 1; E1 and E2 put to you as a veto; a Yemen fact (YA-26) cited for the opposite of what it says; E4 tied to the wrong decision | All applied. [Each finding, and how it was handled](../studies/subjects/S-01/review-2.md) |
| 8 | Found while checking the Yemen facts: the courier page behind cash on delivery doesn't state its area, and its online-store connection is still to come | Stated in the Yemen row, with the store in Sana'a as firmer evidence, and investigation I7 |
| 9 | After the review, a script checked every quote in this pack against the line it cites. 4 of 38 didn't match: one line number was off by two, and three cited a summary row instead of the line that holds the quote. Tracing them also showed that one of my own findings was half wrong: I had written that the courier page doesn't name its country, but its description says "in Yemen" | Each quote now cites the line that holds it, and the check passes ([`method/check_report.py`](../method/check_report.py)). The same line slip is fixed on Decision 1's page and in the register |

**Deliberate, evidence-backed choices, not defects:**
- C at launch, with the three defaults;
- Decisions 2 to 12 by C;
- no payment service of Sharrwah's own at launch;
- the cut of Yemen's scenarios.

**Open questions, each with the work that would settle it:**
- **I1:** do Yemen's card gateways and acquirers ([YA-107](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L108), [YK-161](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L162)) pay into the seller's own merchant account? Their merchant terms, in the payment-methods subject (S-04).
- **I2:** which Yemeni wallets let a platform connect sellers' own wallet accounts, in which area ([YK-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L132), [YK-124](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L125))? Their merchant and API terms, in S-04.
- **I3:** does C, or B later, need any registration for Sharrwah in a market? A lawyer, when each market is set up.
- **I4:** who holds Salla Payments' money, and under which licence ([SA-C-177](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L118))? Only if A or B comes back.
- **I5:** several sellers paid from one checkout, which would need a processor that splits payments. No such processor is in S-01's evidence. Marketplace channels are in it, such as Trendyol, and work as C. If a marketplace of Sharrwah's own is in scope (Salla has one, [SA-C-096](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L66)), it becomes a subject.
- **I6:** can PayPal receive money in Yemen ([YK-514](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L515))? PayPal's own country list.
- **I7:** which couriers collect cash on delivery for online sellers, and where ([YK-203](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L204))? Their terms, in the delivery subject (S-10).
- **I8:** whose money does a customer wallet hold ([SA-C-063](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L42), [ZD-C-019](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/zid/concerns.tsv?plain=1#L20))? If Sharrwah's bill collects partners' charges, such as apps or shipping labels, and pays them out ([SH-C-019](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/shopify/concerns.tsv?plain=1#L20), [SH-C-169](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/shopify/concerns.tsv?plain=1#L170), [SA-C-195](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L127)), Sharrwah holds third parties' money. That goes to the licences subject (S-06) and the charging subject (S-11).

## Risks, and how they're managed

| Risk | How it would show | What controls it | Checked |
| --- | --- | --- | --- |
| The design builds C into orders, and A or B later means rework | A payment record that assumes the provider holds, or that posts into a seller balance | Your decision on E1 and E2. If kept, it's written into the architecture description and checked there | Before any code |
| "Never" in default 2 read as permanent | A later A or B can't net fees, take cash-on-delivery fees or recover financing | Your one line | Now |
| A provider becomes unavailable ([SA-C-235](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/concern-map/platforms/salla/concerns.tsv?plain=1#L149)), and under C the money's path goes with it | Sellers can't take a payment method | More than one provider per method where possible, and S-04's question of what happens when one fails | In S-04 |
| Sellers find their own provider accounts hard to open | Slow onboarding in the first market | Default 1; the providers' onboarding terms (I2) | In S-04 |
| Sharrwah's invoices go unpaid | Fees outstanding | A billing part with its own collection rules (E3) | In the design |
| Yemen's licensing or wallet rules change | A dated fact in the Yemen row stops holding | Facts are dated and re-checked at market setup. Switching on A or B is yours anyway | At market setup |
| C or B still needs a registration somewhere | A lawyer says so | I3, per market | At market setup |
| My drafts outrun my checks again | Claims that don't hold | An independent review of every pack before it reaches you; this one found 16. Then a script checks every quote against the line it cites ([`method/check_report.py`](../method/check_report.py)); it found 4 more | Every report |

## Does the result hold?

- **Where it holds.** *My reading,* on the evidence above:
  - Decision 1 is the path the references all offer beside their own services.
  - It keeps your guard.
  - It fits what Yemen offers today.
  - It closes no mature capability for good, if A and B are kept possible and "never" means at launch.
- **Where the method was weak:**
  - The pilot cost about 1.03 billion tokens, very roughly half of it one-time or rework ([method report](../studies/subjects/S-01/method-report.md#12-what-a-subject-costs)).
  - It split one decision 23 ways.
  - One of its recommendations, on currency, was shaped by Yemen.
  - My first draft of this pack had 16 claims that didn't hold. The independent review caught them. That is the method working, but it shows the review can't be skipped. The quote check then caught 4 slips the review hadn't, so it stays too.
- **What isn't tested yet:**
  - the architecture, which isn't designed;
  - whether sellers in Yemen find C workable in practice, which needs the providers' terms (I1, I2, I7).

## What it cost

| Work | Tokens |
| --- | --- |
| The pilot, for reference | about 1.03 billion |
| The independent review of this pack | 0.27 million |
| My own session | not metered by `method/count_tokens.py` |

## What I need from you

1. **Default 2's "never":** at launch / in every arrangement
2. **Keep A and B possible in the design (E1, E2):** keep them / bind C now / decide at the architecture description
3. **G2,** when convenient: [its page](G2.md)
