# Batch P-1: notes for the coordinator

S-01's points S01-VP-01 to S01-VP-10, landed on the model at 9d204b46 (`studies/class-model/briefs/P-points.md`). The file is `P-1.tsv`. The checker's final line: `# 10 points in P-1, 0 problems`, with no `lead:` lines.

Count by status: **4 landed** (S01-VP-01, S01-VP-06, S01-VP-07, S01-VP-10) and **6 conflict** (S01-VP-02, S01-VP-03, S01-VP-04, S01-VP-05, S01-VP-08, S01-VP-09), with 7 conflicts in all.

## 1. The points that were hard to land, and why

**The "who fills" points spread over many capabilities.** S-01 asks who holds, settles, pays out, collects or deducts, and each platform answers per payment flow: its own service, the processor behind it, a connected gateway, a wallet, an instalment provider, cash on delivery, the point of sale, a marketplace. The model gives each flow its own capability, so S01-VP-02, S01-VP-03, S01-VP-04 and S01-VP-09 land on five to eight capabilities, the main one first: CM-PAY-004 where the question is about the role behind the platform's service (hold, settle, collect, agent, security interest), CM-PAY-005 where it is about the balance and its payouts (payouts, deduct), CM-PAY-006 for reserves and holds. A reading: each further capability is one a platform's variant answers in, and I compared each such cell. The coordinator may prefer to keep only the main capability and leave the flows to their own capabilities; the comparisons would then lose the CM-PAY-015 conflicts below.

**CM-PAY-004 against CM-PAY-002, for Salla and BigCommerce.** Salla's "a Salla service that processes payments in your store directly, settling transactions with banks" (S01-SA-139, V-533) and "خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر" (V-085, the concern map's SA-S-0049) name the platform's own service as processing and settling. The model reads SA-S-0049 `core` in CM-PAY-002 (SA-C-110/where/SA-S-0049) and `shows` in CM-PAY-004, whose Salla cell says no statement names who processes, acquires or holds behind the service. I followed the model's grain: the service is CM-PAY-002's, the entity behind it CM-PAY-004's, so Salla's variants answer in CM-PAY-002, where its cell is `core`, and no conflict is raised. The other reading, that S01-SA-139 names Salla itself as the settling party and so would place Salla `core` in CM-PAY-004 (a `count` conflict on a `not-stated` cell), is open to the coordinator. The subject's own gap S01-SA-G03 says no page names who carries out Salla's settlement, and the audit finds it "partly contradicted by S01-SA-139". What would settle it: the text of Salla's payment services contract, عقد خدمات الدفع (SA-I-2612, its text not read). BigCommerce is the same case with the evidence the other way: "Your new BigCommerce Payments account is what processes and settles all transactions" (S01-BC-070) sits beside "a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement" (S01-BC-069) and "PayPal powers the payment processing behind the scenes" (S01-BC-051). So the BigCommerce Payments account is CM-PAY-002's and CM-PAY-005's, and PayPal is CM-PAY-004's `outside`, as the cell has it.

**Holding the funds, S01-VP-01.** The subject's analysis reads "Salla and Zid both name the platform itself as the holder", from "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر" (S01-SA-056) and the Zid Pay balance (S01-ZD-034). A reading: these name the service's balance, which is CM-PAY-005's by its own terms (Salla رصيد المدفوعات الإلكترونية), where Salla and Zid are `core`. Who holds custody behind the balance stays unstated on Salla (CM-PAY-004 `not-stated`) and is the payment service providers on Zid (CM-PAY-004 `outside`, ZD-C-009/where/ZD-S-0589). No register row rests on custody: S01-D1 is C, the provider holding in the seller's own account, which is CM-PAY-011's thing on every platform. S01-E2's two records (the order's payment record and the holder's ledger) match the model's CM-PAY-020 and CM-PAY-005. So no `premise` conflict.

**The agent, S01-VP-06.** The variants are agreement terms (Shopify's appointment as agent, SH-S-0079; Stripe's and Network International's agency in WooPayments' terms; Zid's authorization, ZD-S-0543; BigCommerce's "No agency ... relationship", S01-BC-128), which support no placement under the brief. Landed, no conflict.

**Marketplaces on Zid.** Trendyol collecting the buyer's payment and paying the merchant (S01-ZD-097), and Trendyol and Amazon deducting their fees (S01-ZD-098, S01-ZD-101), land in CM-CHN-003, whose Zid cell is `core` with Trendyol and Amazon as slot fillers. A reading: CM-CHN-003's thing is connecting the marketplace and syncing its orders, which Trendyol doesn't do, so its collecting is no `placement` difference. The payment flow of a marketplace order (the marketplace collects, pays out and deducts) has no capability of its own by name, but CM-CHN-003's Zid cell holds the channel's money terms (Zid's share of Amazon sales, ZD-S-1060; fees from the wallet, ZD-S-1061), so I raised no `structure` conflict. The coordinator may judge otherwise.

**Salla's withholding, S01-VP-08.** "منصة سلّة لها الحق في رفض أو إلغاء أو تعليق عمليات الشراء" (S01-SA-087) and the delay of transfers under the Saudi Central Bank's restrictions (S01-SA-089) are Salla's terms, which support no placement, so CM-PAY-006's Salla cell (`none-held`) gets no `count`. Salla's delay is landed in CM-PAY-005, the balance's payout. A Salla statement in the admin, not the terms, would be needed for a placement in CM-PAY-006.

**Zid Ship's cash on delivery.** "تقوم زد بتحصيل المبلغ نيابة عن التاجر" (S01-ZD-069) is the concern map's ZD-S-0641, which the CM-PAY-029 Zid cell reads `core`. It could also be read as Zid's company providing a separate service, Zid Ship (`own-service`). No maker statement for Zid Ship is in the cell, so I raised no conflict; it is a reading for the coordinator.

## 2. Each conflict, with both sides

1. **S01-VP-02, `placement` (rows: S01-D2, model).** Subject: Tamara settles every payment made through it on Salla (S01-SA-104, V-037). Model: the CM-PAY-015 Salla cell is `core` only (SA-C-118/where/SA-S-0070, the plan line SA-C-118/decides/SA-S-1965, the released flags tamara and tabby). Tabby and Tamara are slot fillers there but are not placed `outside`. Zid's cell places the like statement `outside` (ZD-C-013/responsible/ZD-S-0625).
2. **S01-VP-03, `placement` (rows: S01-D3, model).** Subject: Tabby pays the store first (S01-SA-102, V-056), and Tamara is responsible for paying the merchant (S01-SA-105, V-057). Model: the same CM-PAY-015 Salla cell.
3. **S01-VP-03, `placement` (rows: S01-D3, model).** Subject: Mokafaa Al Rajhi pays the merchant into its own account there (S01-SA-107, V-058). Model: SA-C-119 lands in CM-PAY-012, whose Salla cell is `core` only (SA-C-119/where/SA-S-0129, SA-C-110/decides/SA-S-1962). The cell lists no Mokafaa slot filler, and the plan line مكافأة الراجحي is cited `core` in CM-PAY-001 (SA-C-119/decides/SA-S-1966).
4. **S01-VP-04, `placement` (rows: S01-D4, model).** Subject: payments through Tabby are collected by Tabby, not Salla Payments (S01-SA-101, V-088). Model: the same CM-PAY-015 Salla cell.
5. **S01-VP-05, `count` (rows: S01-VP-05, model).** Subject: BigCommerce's help page Configuring Offline Payment Methods (S01-BC-115 to S01-BC-119) has the merchant set up Bank Deposit, Cash on Delivery, Check, Money Order and Pay in Store methods in the store, which is BigCommerce's own setting and so `core`. Model: CM-PAY-016's BigCommerce cell is `not-stated` (BC-C-022/boundary/BC-S-0129), and its reading says that Help Center page isn't held. CM-PAY-030's BigCommerce cell is `none-held`. CM-PAY-029's BigCommerce cell, which the Cash on Delivery method also bears on, is `not-stated`, but CM-PAY-029 isn't among this point's capabilities: CM-PAY-016 holds cash on delivery as a manual method. The subject cites the page from the run `ct-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine`, item 006. A reading: this is the strongest conflict in the batch, and an amendment to domain C is the likely consequence.
6. **S01-VP-08, `placement` (rows: S01-VP-08, model).** Subject: Salla's dashboard reports the "Percentage of payments held by the issuing bank due to disputes" (S01-SA-180, S01-SA-181, V-546). Model: CM-PAY-009's Salla cell is `core` only (SA-C-122/responsible/SA-S-5051) and lists no issuer, while Shopify's places the cardholder's bank `outside` (SH-C-072/decides/SH-S-0395, SH-S-0396). The strings would also give Salla's cell a statement in its own admin, in a term its search lists (اعتراضات).
7. **S01-VP-09, `placement` (rows: S01-D6, model).** Subject: a refund on a Tamara order is taken from Tamara, not from Salla's balance (S01-SA-106, V-165). Model: the same CM-PAY-015 Salla cell.

Conflicts 1, 2, 4 and 7 are one cell, CM-PAY-015 on Salla, and one amendment would answer all four: an `outside` placement on Tabby's and Tamara's statements beside `core`. In each, the register row (S01-D2, S01-D3, S01-D4, S01-D6, each settled by Decision 1's answer) agrees with the subject's side: each provider does it on its own terms. A reading: none of the seven reopens a founder's decision. Each would end in an amendment to the model if the coordinator finds the cell wrong.

## 3. The checker's leads

The checker printed no `lead:` lines. Every platform whose statements the subject holds on a point has statements in a cell of one of the point's capabilities. The `show` views had flagged "nothing traced" (for BigCommerce on S01-VP-01, S01-VP-03, S01-VP-04 and S01-VP-05; WooCommerce on S01-VP-02 and S01-VP-10; Salla, WooCommerce and BigCommerce on S01-VP-06; Salla on S01-VP-08 and S01-VP-09). For each, I searched the model (`caps`, `search`, `q3.py where`) and landed it, as follows:
- BigCommerce's variants: CM-PAY-004 (PayPal), CM-PAY-002 and CM-PAY-005 (BigCommerce Payments), CM-PAY-011 (the standalone PayPal gateway, Stripe, BitPay, Braintree), CM-PAY-016 and CM-PAY-030 (offline methods);
- WooCommerce's Stripe terms: CM-PAY-004;
- Salla's: CM-PAY-011 (the charity gateway account, S01-SA-195), CM-PAY-012 (Mokafaa Al Rajhi, through `q3.py where`: SA-C-119 lands in CM-PAY-012), CM-PAY-005 and CM-PAY-009.

What I made of the leads I set aside:
- CM-MKS-003 for Global-e: its statements SH-S-0565 and SH-S-0566 are cited `outside` in CM-PAY-004 too;
- CM-PAY-020, CM-RET-002 and CM-PLN-004 on S01-VP-01: single page or cited hits on refunds and billing, not the holder;
- CM-PLN-006 on S01-VP-01: Salla's store balance, which Salla says differs from the e-payments balance (S01-SA-056).

**A key I chose:** CM-PAY-011 came from no lead on S01-VP-01, S01-VP-02 and S01-VP-03. Its basis item BC-C-026/where/BC-S-0151 is a key of the cell that bears out third parties as providers, not a trace of the subject's statement.

## 4. Slot fillers the subject names that `cell` doesn't list

These are leads, not conflicts:
- **CM-PAY-004** (`outside` cells):
  - WooCommerce: Network International, LLC (S01-WC-129, S01-WC-142, S01-WC-145; UAE, Visa and Mastercard processing); Stripe Payments Company, SPC (S01-WC-112, S01-WC-127; United States); Stripe PSP (S01-WC-115; EEA, UK, Switzerland, Gibraltar); the Financial Providers holding Stripe's pooled accounts (S01-WC-120, S01-WC-122); Stripe Japan, for JCB (S01-WC-150, stripe.com/jp/legal/jcb), and JCB. The cell lists only Stripe;
  - Shopify: PayPal UK Ltd. (S01-SH-117; Gibraltar, United Kingdom) and PayPal Pte. Ltd. (S01-SH-118; Switzerland), from the Payment Processor List;
  - BigCommerce: PayPal is listed. The subject's S01-BC-051 and S01-BC-069 fill the cell's gap ("No statement names who processes, acquires or holds the funds"): PayPal processes through the linked PayPal account and handles settlement through a PayPal platform account.
- **CM-PAY-005:**
  - laws: the Saudi Central Bank's restrictions, the Ministry of Commerce and Investment, and the e-commerce regulations, on Salla's transfers (S01-SA-089);
  - Shopify: the unnamed "multiple payment processing partners" (S01-SH-075, United States and France);
  - BigCommerce: PayPal, behind the BigCommerce Payments account (S01-BC-051, S01-BC-069).
- **CM-PAY-006:** WooCommerce: SPC's Reserve Accounts (S01-WC-112) and Network International (S01-WC-145). The cell lists only Stripe.
- **CM-PAY-011:** BigCommerce: BitPay (S01-BC-021), and PayPal's standalone PayPal Checkout (S01-BC-023, S01-BC-090; PayPal Braintree and PayPal Complete Payments are listed, the standalone gateway isn't).
- **CM-PAY-012:** Salla: Mokafaa Al Rajhi, مكافأة الراجحي (S01-SA-107).
- **CM-PAY-009:** Salla: the card's issuing bank (S01-SA-180, S01-SA-181).
- **CM-PAY-029:** Salla: shipping companies outside Salla's labels (S01-SA-091), unnamed.

Already listed, so nothing to add:
- Tabby and Tamara (CM-PAY-015);
- Geidea (CM-PAY-021);
- Paymob (CM-PAY-011);
- Trendyol, Amazon and Jahez (CM-CHN-003);
- Global-e (CM-PAY-004).

## 5. Problems with the brief or the script

- **How many capabilities:** the brief's "Add another only where the platforms answer the question in different capabilities" reaches up to eight capabilities on S-01's "who fills" points, because the platforms always answer per payment flow (section 1). A rule for a main capability against the flows' own would help the other S-01 batch land the same way.
- **The `cited` route:** `check` accepts any key a landing capability's cell holds as a `cited` basis, whether or not a subject's statement traces to it. So `cited` in my rows means "a key of the cell that bears the reading out" where no lead offered the capability (CM-PAY-011, CM-PAY-012, CM-PAY-021, CM-CHN-003, CM-PAY-013, CM-PLN-006, CM-PAY-009).
- **Warnings:** `show` printed no warning that a domain's files changed after the merge.
- **The BigCommerce help pages:** the subject's citations for them (`ct-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/...`) name no repository or commit in the citation's source field. I didn't open them; conflict 5 rests on the subject's quotes as recorded in `studies/subjects/S-01/bigcommerce/citations.tsv` (S01-BC-C200 to S01-BC-C204).
