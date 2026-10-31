# Q3's check, batch Q-13: notes

Rows: `pay:PAY-41` to `pay:PAY-60`, 20 of the 81 payment rows. The file: `check-Q-13.tsv`. The checker: `20 of 20 rows placed; 0 problems`.

| result | count |
|---|---|
| covered | 3 (PAY-41, PAY-49, PAY-50) |
| partly | 1 (PAY-48, its rest beyond the class) |
| beyond the class | 16 |
| candidate miss: held | 0 |
| candidate miss: not held | 0 |
| unclear | 0 |

## What these rows are

Most of this slice asks Sharrwah's launch position in Yemen and the two central banks' law, not what the class does. So most rows go to a decision in force, to the founder's list, to a subject that hasn't run yet, or to outside parties:
- **Wholly answered by Decision 1 (`founder:decided`):** PAY-42, PAY-45, PAY-47. Each asks who holds money, collects cash on delivery or receives buyer money at launch. Decision 1's C, with its defaults and Decisions 2 to 12 (founder-decisions 2026-10-25 G1; the room kept, 2026-10-26 G3 (S-01)), answers each one whole. Each gets `wrong party`, since it asks for a decision a decision in force already settles.
- **Partly decided:** PAY-51 (default 2: at launch, fees are billed apart and never netted; what to charge is still plans and prices); PAY-56 (the platform as collector of cash on delivery is off at launch; the courier's licensing is S-10's and S-06's).
- **Law and licensing (S-06, S-03, S-07, S-08, S-10 with `outside`):** PAY-54 to PAY-60. These ask the regulators' and lawyers' facts directly, so none is a `market fact` by the brief's definition, which needs the row to ask what the product should do.
- **Founder's list:** PAY-43 (markets), PAY-44 (the company and its domicile), PAY-46 (partners), PAY-52 (licences, merger, capital), PAY-53 (markets and timing, an offshore entity).

## Rows that were hard to place

- **PAY-41 (ledgers).** The row asks how Sharrwah should build its ledgers. Each ledger it names is a capability with cells: CM-PAY-020, CM-PAY-004/005, CM-PAY-023, CM-PLN-006, CM-LOY-001/002 and CM-PLN-004. So it is `covered`, and how the ledgers are built is left to engineering (`engineering:build`, architecture/plan.md section 3, item 3). Part of it is bound by the founder's decision of 26 October (S01-E2: a holder's ledger is a separate part) and by S01-E3, which is ruled. Nothing held names a ledger's form: I searched ledger, double-entry, append-only, journal entr and balance transaction, and for Salla and Zid دفتر, قيد, قيود, القيود, كشف حساب and حركات المحفظة. The Arabic hits are order statuses (قيد التنفيذ) and payment rules (قيود الدفع). That is `detail`, not a miss, because the row asks how the records are built, not about a thing the platforms do that the model lacks. I added S-09 because "one per currency" is the currency of records, which binds every area that holds an amount (a reading of architecture/plan.md section 3).
- **PAY-48 (currency).** Pricing currency, conversion timing and who bears the risk are covered by CM-MKS-006, CM-MKS-007 and CM-ACC-005, with S-02's ruling S02-D7. The "currency edition" (two currency areas under one code) is the product gap S-02 already records as S02-D9 and moved to S-09 as S02-M6. Under the brief, a product gap a subject's register answers is `beyond the class`, so this row is `partly` with its rest beyond the class.
- **PAY-49 (refunds on rails without a reversal API; credit across sellers).** Credit usable across sellers looked like a possible miss. It is held: Shopify's Shop Cash, "a Shopify-funded rewards program for Shop app customers" (SH-C-082/where/SH-S-0437), is cited in CM-LOY-004@shopify as own-service. So the row is `covered`. Whether Sharrwah issues such credit is the founder's call (whether its own company runs a balance service). How a refund made outside a provider is recorded is not named by any statement held. I searched manual refund, offline refund, cash refund and refund outside, and for Salla and Zid استرداد, استرجاع المبلغ and إرجاع المبلغ. The nearest is Zid's "refund methods depend on the order's original payment method" (ZD-C-081/boundary/ZD-S-1014, cited in CM-RET-002@zid). That is `detail`.
- **PAY-50 (wallet secrets at checkout).** Covered by the gateway shapes the cells hold:
  - WooCommerce's form-based redirect (WC-C-001/where/WC-S-0624, CM-PAY-011@woocommerce);
  - Zid Payments' encrypted payload or token (ZD-C-010/boundary/ZD-S-0603, CM-PAY-004@zid);
  - BigCommerce's API flow, which doesn't support hosted or offsite providers (BC-C-027/boundary/BC-S-0163);
  - PCI responsibility (CM-TRU-018).

  Shopify's Offsite and Custom onsite extension points (SH-I-1488, SH-I-1487) and paymentSessionRedirect (SH-I-0140) are held and cited by no cell. Their concern lands in CM-PAY-011, the capability that is the thing, so they are not a held miss. Nothing held names a wallet OTP or PIN entered at checkout: Salla's OTP hits are buyers' sign-in. That is `detail`.
- **PAY-43 (zones).** Which zone to serve is the founder's (markets). Whether a seller may sell across zones is law (S-07 with `outside`). The structure is already ruled by S02-D8: rules keyed on an area within a country. I gave it `engineering:build` with `ruled`, since the row's "both as separate ecosystems" is a question about structure (a reading).

## Candidate misses

None. The searches behind the three covered rows are above and in each row's `what_would_settle_it`. Each statement the searches found was checked with `q3.py where`: SH-S-0437, SH-I-1487, SH-I-1488, SH-I-0140, WC-S-0624, BC-S-0163, ZD-S-0603, ZD-S-1014, ZD-S-0809, SH-S-0258, SH-S-0550, SH-S-0452 and SH-S-5165. Each is cited by a cell, or its concern lands in the capability that is the thing the row asks about. I ran no `outscope`, since no row came to a miss.

## Time bombs

- **wrong party:** PAY-42, PAY-45, PAY-47. Each asks for a decision Decision 1 already settles.
- **wrong time:** PAY-46 (slice), PAY-50 (slice), PAY-55, PAY-56, PAY-58, PAY-60 (launch), PAY-53 and PAY-57 (later), all against `before build`. PAY-52 is later against `before release`.
- **market fact:** PAY-43 (selling across zones), PAY-46 (rails refused on sanctions or licensing grounds), PAY-48 (currency edition).
- **bundles:** PAY-43, PAY-44, PAY-46, PAY-49, PAY-51, PAY-53 to PAY-60. In each, the answerers' times differ: a subject's `before build` against `outside`'s or the founder's `before release`.

## Problems with the brief or the evidence

- **A row answered only by `founder:decided` has no `when`.** The brief says a decided part "sets no `when`", and gives `unclear` "where none applies". So PAY-42, PAY-45 and PAY-47 carry `unclear`, which the checker accepts. "Answered now" would describe them better, but `WHEN` has no such value. The coordinator may want one.
- **`founder-decisions.tsv` changed on disk during this run.** A row of 30 October on agent effort ("Method (standing)") was added, uncommitted, with `PLAN.md` also modified. It bears on how the work is run, not on any of these rows' answers. I read it and changed nothing for it.
- **S01-E3 and S01-E4 have the status "proposed, engineering ... the founder may veto".** I read them as engineering's rulings that weren't vetoed, as the brief allows, and cited them as `ruled`.

## The coordinator's changes after the batch

- **A row answered whole by a decision in force now has the `when` `decided`.** The brief and `q3.py check` gained that value, which the checker requires exactly where `founder:decided` is the only answerer. PAY-42, PAY-45 and PAY-47 changed from `unclear` to `decided`, and the sentence on `when` in their `what_would_settle_it` changed with them.
- **Decision citations** are now `founder-decisions <date> <gate>` with ` #<k>` where several rows share that date and gate. This batch's were rewritten to that form from each row's own text, as in Q-12's notes.
- **S01-E3 and S01-E4 are engineering's constraints, listed for the founder's veto in `reports/S-01-review.md` ("E3 and E4 follow from C itself, and are mine. You may veto either").** No veto is recorded in `founder-decisions.tsv`, so reading them as rulings in force is right. Their status in S-01's register still says "proposed". They go into the GM report's list of engineering's rulings for veto, since the founder's answer at G3 (S-01) isn't saved in the repository.
