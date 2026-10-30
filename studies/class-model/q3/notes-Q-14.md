# Q3's check, batch Q-14: notes

Rows: `pay:PAY-61` to `pay:PAY-81` (21). The rows are in `check-Q-14.tsv`. `q3.py check --batch Q-14` prints: 21 of 21 rows placed; 0 problems.

## Count by result

| result | rows |
|---|---|
| beyond the class | 12: PAY-61 to PAY-72 |
| partly | 8: PAY-73, PAY-74, PAY-75, PAY-77, PAY-78, PAY-79, PAY-80, PAY-81 |
| covered | 1: PAY-76 |
| candidate miss: held | 0 |
| candidate miss: not held | 0 as a whole row; 1 as a partly row's rest (PAY-75) |
| unclear | 0 |

## Rows that were hard to place, and why

- **PAY-61 (sanctions and KYC Sharrwah must run).** The class does screen: a payment service's processor runs KYC, AML and sanctions checks (`CM-PAY-003@shopify`, outside, SH-S-0100), the platform keeps out unsupported regions (`CM-ACC-008`), and BigCommerce has the merchant screen its own parties and customers (`CM-TRU-010@bigcommerce`, BC-S-0438). The row asks what a market's law requires of Sharrwah, though, so I placed it as `beyond the class` with S-07 and outside (a lawyer), not as `partly`. A reading. One point on the evidence: Shopify's statements on sanctions in its payment terms (SH-C-174/decides/SH-S-0122, SH-S-0131, SH-S-0353) are cited in no cell, and their concern lands in `CM-ACC-008`, the countries served. That doesn't make a miss here, because the row's answer is the market's. But the coordinator may want to know that the payment service's own sanctions condition isn't cited where it bears, in `CM-PAY-003`.
- **PAY-64 and PAY-65 (accounts held for sellers, and escrow).** Decision 1 answers part of each, so `founder:decided` with `founder-decisions 2026-10-25 G1 #1` (and, for PAY-64's netting of Sharrwah's fee, `founder-decisions 2026-10-26 G3 (S-01) #2`). The rest is a provider's or bank's answer, `outside`. For PAY-65, my reading is that an escrow releasing funds on Sharrwah's delivery instruction makes Sharrwah party to the provider's agreement for the money, which makes it B, off under the guard. Both rows raise `wrong party`, since each asks for something a decision in force settles.
- **PAY-71 and PAY-72 (how Yemeni sellers and buyers pay today).** These are a market's facts about practice and preference, and no subject in `subjects.tsv` covers them. S-04 covers providers and S-10 covers couriers, not behaviour. So each is `subject:none`, with the subject it would need named in the row, and the `when` is `unclear` by the rules. For PAY-71 I also cite `founder-decisions 2026-10-24 Method #3` (no merchant interviews, ever), because that limits where such a subject's evidence could come from.
- **PAY-73, PAY-74, PAY-78, PAY-80, PAY-81 (zones, rial editions and rates).** Yemen's two zones and two rial editions are what S-02's product-gap rulings already answer: S02-D8 (an area within a country, a dated field) and S02-D9 (a currency area within one code), with S02-D7 for rates per market and S02-E5 for which market carries who holds the money. The founder didn't veto them on 30 October. The class part of each row is covered by its cells. I placed the rest as `beyond the class`, answered by `subject:S-02` and `engineering:build`, with the register row in `basis`. Where S-02 leaves the question to S-09 (S02-M6, and S02-D7 on rate sources), S-09 is added.
- **PAY-75 (outcome sources).** Five of the six sources the row names have a capability, and its "Sharrwah ledger" is decided: a holder's ledger is a separate part, empty under C (`founder-decisions 2026-10-26 G3 (S-01) #1`). I read the evidence each source must carry as a payments-area build detail, so `engineering:detail`. That gives `bundles` and `wrong time` against the row's `model`. A reading.
- **PAY-76 (the adapter's capability profile).** Placed as `covered`. The class's slot is `CM-PAY-011`, an extension point on Shopify, WooCommerce and BigCommerce. The profile's fields are detail beyond the cells, and choosing Sharrwah's profile is engineering's.
- **PAY-79 (secrets and per-seller credentials).** I placed it as `engineering:build`, not `detail`. My reading: where secrets live and how stores are kept apart is the architecture's first cross-cutting decision (`architecture/plan.md`, section 3). That gives `wrong time` against the row's `slice`. If the coordinator reads it as the payments area's build detail, the `when` becomes `at the area's build` and the bomb goes away.

## Candidate misses

- **Not held (PAY-75's rest): a buyer's own claim of payment**, such as a transfer receipt the buyer attaches to a bank-transfer order. I searched, on Salla, Zid, Shopify, WooCommerce and BigCommerce: receipt, proof of payment, payment proof, transfer receipt, upload receipt, إيصال, ايصال, إيصال التحويل, إيصالات, صورة التحويل, إرفاق, إثبات الدفع, اثبات الدفع, إثبات التحويل, الحوالة, حوالة, رفع الإيصال, التحويل البنكي, bank transfer. I also ran `outscope` for receipt, إيصال, إثبات, bank transfer, تحويل.
  - The only hits are a partner paying Salla's invoices with proof of transfer (SA-C-195/boundary/SA-S-0045) and Zid's upload of a bank transfer receipt under reverse orders (ZD-C-081/boundary/ZD-S-0912). Both are about other flows, not a buyer's payment.
  - What would settle it: a capture of Salla's and Zid's checkout with bank transfer chosen, and of their order page for such an order. That the class may hold such a step is an assumption, marked as one. It is why the capture is worth asking for, not a claim that the class holds it.
- **No held miss.** For escrow (PAY-65), I searched escrow, trust account, release of funds, حساب ضمان, الضمان, حسابات الضمان, تعليق المبلغ, until delivery, بعد التسليم, and ran `outscope`. Nothing is held. The row is answered by Decision 1 and a bank, so it isn't a miss.

## Time bombs

- `bundles`: PAY-61, 62, 63, 64, 66, 67, 68, 69, 70 (a subject before build against an outside party before release), and PAY-75 (model against engineering:detail).
- `wrong time`: PAY-61, 62, 67, 68, 70 (launch against before build); PAY-63 and PAY-79 (slice against before build); PAY-65 (later against before release); PAY-66 and PAY-69 (later against before build); PAY-75 (model against at the area's build).
- `wrong party`: PAY-64, 65, 75, 77, 80. Each asks, at least in part, for something a decision in force already settles: Sharrwah's fee netted, Sharrwah party to escrow, a Sharrwah ledger, Sharrwah as a custodian, and Sharrwah's position per setup instance where Decision 1's E1 makes it a market's setting.
- `market fact`: PAY-61 (what screening Sharrwah must run, by a market's law) and PAY-81 (which rate sources a market's currency takes).

## Problems with the brief or the evidence

- None that blocked the work.
- The rows for Yemen's rails and partners (PAY-63, 66, 67, 69, 70) all go to S-04 plus outside parties. That follows from the rule that a subject answers before build and an outside party before release. The result is that every one of them carries `bundles` and, except PAY-64, a `wrong time`. The bombs are mechanical here, not a sign of a mis-asked row beyond what the brief's rules make them.
- S-02's register gives D1 to D9 the kind "founder decision", but their status reads "engineering's ruling ... no veto (the founder, 30 October)". I treated them as engineering rulings in force, as the founder's row of 30 October (G3 (S-02)) and the brief's item 2 read together.

## The coordinator's changes after the batch

- **S-02's rulings answer as engineering's.** S-02's D1 to D9 and E1 to E5 are engineering's rulings, listed for the founder's veto and not vetoed (`founder-decisions 2026-10-30 G3 (S-02)`). The register's `kind` column for D1 to D9 still says "founder decision", from before the intent of 29 October, but their status says engineering's ruling. So a part one of them answers is `engineering:build`, `ruled`, as this batch read it.
- **One convention across the batches.** The brief now says a subject that has run (S-01, S-02) answers only through its register: `engineering:build` or `engineering:detail` for a ruling in force, `founder:decided` for a founder's decision, and the receiving subject for a moved row. `q3.py check` refuses `subject:S-01` and `subject:S-02`. Seventeen rows across Q-01, Q-07 and Q-11 to Q-14 were relabelled:
  - `subject:S-02` became `engineering:build`;
  - `subject:S-01` became `founder:decided` (Decision 1), with `founder-decisions 2026-10-25 G1 #1` added to PAY-01's basis;
  - PAY-38 gained `engineering:build` for S02-D9.

  No row's `when` or time bombs changed, since both labels give `before build`.
- **Shopify's sanctions conditions** (SH-C-174/decides/SH-S-0122, SH-S-0131, SH-S-0353), which no cell cites, are weighed with Q3's other amendments to the model.
