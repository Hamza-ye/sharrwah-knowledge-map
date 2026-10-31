# Q3's check, batch Q-12: notes

Rows: `pay:PAY-21` to `pay:PAY-40`, twenty of the payment set's rows. I wrote them to the brief as it stands and checked them with `q3.py check`. Its final line is `20 of 20 rows placed; 0 problems`.

## Count by result

- covered: 13 (PAY-21 to 29, 32 to 35)
- partly: 3
  - PAY-36, rest `candidate miss: held`;
  - PAY-30 and PAY-31, rest `candidate miss: not held`.
- beyond the class: 4 (PAY-37 to 40, the Yemen rows)
- candidate miss as a whole row, unclear: 0

## Candidate misses

**A payment test mode (`pay:PAY-36`, held).** The row asks how every payment outcome can be simulated without touching live sales, balances or reports.
- What the model covers: testing apart from the live store, in Salla's development stores (`CM-DVT-004@salla`) and BigCommerce's StagingPro (`CM-DVT-006@bigcommerce`).
- What it doesn't: a test mode inside a store, with test orders and simulated outcomes kept out of its balances and reports.
- What the map holds: Shopify's help-centre section "Placing a test order" (`SH-I-2120`). No cell cites it, and its concern `SH-C-047` lands only in `CM-CHK-001`, the coarser capability where the miss would sit.
- What I searched:
  - in English on all five: test mode, Bogus, test payment, test order, sandbox, test card, simulate, testing payments;
  - in Arabic too for Salla and Zid: وضع الاختبار, الوضع التجريبي, وضع تجريبي, بيئة الاختبار, اختبار الدفع, دفع تجريبي, تجريبية, بطاقة تجريبية, البطاقات التجريبية;
  - `outscope` on all five. It found only Shopify's store feature `sandbox` (`SH-I-2607`, unplaced), and nothing ties that to payments.

That the section is about test payments is a reading from its title.

**A buyer refusing a cash-on-delivery order at the door (`pay:PAY-30`, not held).** The other ways a buyer contests a payment are covered: card chargebacks and inquiries and a provider's dispute process (`CM-PAY-009`), the platform's complaint handling (`CM-TRU-020`, `CM-SUP-008`) and refunds (`CM-RET-002`). Nothing in the map is a refusal at delivery.
- What I searched:
  - on Shopify, WooCommerce and BigCommerce: refused, return to sender, returned to sender, undeliverable, failed delivery, delivery attempt;
  - on Salla and Zid: رفض, رفض الاستلام, رفض استلام, رفض العميل, مرتجع, المرتجع, إرجاع الشحنة, فشل التوصيل, تعذر التوصيل, لم يتم التسليم;
  - `outscope` on all five.
- What would settle it: Salla's and Zid's help-centre pages on cash-on-delivery shipments the buyer refuses (the shipment's return and its charges), captured into observed-sa. That both platforms document this is an assumption.

**Strong buyer authentication moving a fraud loss off the seller (`pay:PAY-31`, not held).** The other ways a loss leaves the seller are covered:
- Shopify Protect (`SH-S-0404`, at `CM-PAY-010`);
- a buy-now-pay-later provider that pays the store directly (Tabby, `ZD-S-0625`, at `CM-PAY-015`);
- a claim against the carrier for a lost shipment (`ZD-S-0840`, at `CM-SHP-022`), and shipping insurance (`CM-SHP-003`).

Two held statements name 3D Secure, but neither says a loss moves:
- a subscription billing attempt challenged under 3D Secure (`SH-S-6071`). No cell cites it, and its concerns land in `CM-API-003` and `CM-SEL-001`;
- a 3D Secure card that must first be saved for the Payments API (`BC-S-0130`, at `CM-PAY-022@bigcommerce`).

I didn't count these as holding the thing, so this miss is not held. A stricter reader might call it held through `SH-S-6071`.
- What I searched:
  - on Shopify, WooCommerce and BigCommerce: liability, liability shift, authenticated, authentication, strong customer authentication, 3D Secure, 3DS, guarantee, fraud protection;
  - on Salla and Zid: 3D Secure, 3DS, OTP, رمز التحقق, تتحمل, يتحمل, ضمان, مخاطر, الاحتيال;
  - `outscope` on all five.
- What would settle it: Shopify's help-centre and developer pages on 3D Secure and the chargeback liability it shifts, captured into observed-sh.

## Time bombs

- **`wrong time`, six rows:**
  - PAY-37 to PAY-40: their `needed_by` is `launch`, but the subjects that answer them come before build;
  - PAY-34 (`slice`): S-04 and S-07 come before build;
  - PAY-29 (`slice`): which identifiers cross every boundary is an architecture decision, before build.
- **`bundles`, six rows:**
  - PAY-37 to PAY-40: a subject's part is before build, and the part for providers, partners or a regulator (`outside`) is before release;
  - PAY-29: engineering's architecture part and its build detail fall at different times;
  - PAY-36: the model is before build, and engineering's build detail is at the area's build.
- **`wrong party`, `market fact`:** none. The Yemen rows ask a market's facts directly, not what the product should do. PAY-39 asks who may hold sellers' money in Yemen. Decision 1 decides who holds it, not what the law allows, so I didn't count the row as asking a decision already taken. The coordinator may read it otherwise.

## Rows that were hard to place, and why

- **Decision 1 answers parts of nine rows.** These are PAY-22, 24 to 28, 32, 35, 39 and 40. Under C, each provider or courier holds the money, settles it, pays it out, deducts its own fees, and keeps any reserve or hold. I used `founder:decided` and named the decision in `basis`, as the brief says.
  - Each answers the class's question as well, so each stays `covered`, with `model` among its answerers. PAY-39 and PAY-40 are the exceptions: they are beyond the class.
  - S01-E2 (the G3 decision of 26 October) makes a holder's ledger a separate part, empty under C. That bears on PAY-25's question about ledger entries. I added `engineering:build` there for how that part is shaped while it waits for A or B. That is a reading.
- **Rulings in force.** These are cited as `S-02 <row>` with `ruled` and `engineering:build`:
  - PAY-22: S02-D7 (amounts in two currencies, with the rate held per market) and S02-E4 (no payout currency of Sharrwah's own);
  - PAY-35: S02-E1, S02-E2, S02-E5 and S02-D6 (how a per-market setting is read and keyed).

  S-02's moved rows serve as the basis for subjects that haven't run: S02-M2 for S-04, S02-M3 for S-05, S02-M4 for S-07 and S02-M6 for S-09.
- **Engineering's part, as the words of each row read.**
  - PAY-29 says "must", so it asks Sharrwah's design: `engineering:build` for the identifiers and `engineering:detail` for the reports.
  - PAY-33 asks what contract a provider must implement. That is the extension point of `architecture/plan.md`, section 3, so `engineering:build`.
  - PAY-36 asks how a simulator is built, so `engineering:detail`.
  - PAY-21, 23, 28, 30 and 31 name neither Sharrwah nor "should", so the model answers them alone. Some of their parts could be read as asking a policy: PAY-21's override, and PAY-28's recording without rewriting orders.
- **"Cash handed to an agent" (PAY-28) and Yemen's vouchers and agents (PAY-37).** No statement names cash handed to an agent. I read it as one more method paid outside the online flow, `CM-PAY-016`'s (a reading), not as a miss. Zid lists سداد among its payment methods (`ZD-S-0618`, at `CM-PAY-016@zid` and `CM-PAY-017@zid`).
- **Uncited keys whose concern lands in the capability that answers the row.** Shopify's Payments Apps session mutations (`SH-I-0134` to `SH-I-0144`) land in `CM-PAY-011`, and so do the session states and buyer interaction PAY-33 asks about. Following Q-11's practice, I named them under `detail:` rather than in `basis`.
- **PAY-23's blocking rules.** The model has every state on both sides: order status, payment status, disputes, cancellation, fulfilment, refunds, the POS cash session, imported orders and marketplace orders. No statement held states which state blocks which action. The row is `covered`, and the rules are `detail:` for after GM.

## Problems with the brief or the evidence

1. **Q-11's fourth problem no longer stands.** `q3.py check` now refuses a held rest only when every key in `basis` is already cited, so cited keys can sit beside the miss's key. I didn't need it here: PAY-36 names only `SH-I-2120`.
2. **`founder-decisions` rows aren't unique by date and gate.** `founder-decisions 2026-10-25 G1` covers three rows: Decision 1, Decisions 2 to 12, and the G1 row on whether to return to the plan. `2026-10-26 G3 (S-01)` covers two. The text of `what_would_settle_it` says which one is meant (for example "Decisions 2 to 12"). A row number or the decision's name in the brief's form would make the citation exact.
3. **`q3.py slice` for payment rows lists only the PAY area, as Q-11 found.** The leads it gave by rarer words were mostly noise for these rows, among them `CM-SHP-022` for PAY-25 and `CM-CUS-010` for PAY-33. I found the answers with `caps --terms` and by reading the cells of `CM-PAY-005`, `006`, `009`, `011` and `020`, `CM-MKS-007` and `CM-POS-003`.
4. **No problem with the evidence itself.** Every key in `basis` was checked with `q3.py where`. Every named cell holds statements, and every key in a covered row's `basis` is cited by a cell.

## The coordinator's changes after the batch

- **Problem 1 is fixed in the brief and the checker.** A decision is now cited as `founder-decisions <date> <gate>`, with ` #<k>` where several rows share that date and gate, `k` its place among them from the top. `q3.py check` now refuses a citation that matches no row, or several without `#k`. This batch's citations were rewritten to that form from each row's own text: Decision 1 is `2026-10-25 G1 #1`, the pilot's Decisions 2 to 12 `#2`, and the room kept for A and B (S01-E1, S01-E2) `2026-10-26 G3 (S-01) #1`. Where a row's text names "Decision 1 (C)" and what each provider settles, pays out or deducts, it cites both `#1` and `#2`.
- **The candidate misses, checked against the evidence.** `SH-S-6071`, the one held statement on 3D Secure, is a webhook topic: a bank challenging a subscription billing attempt under 3D Secure. It says nothing of a loss shifting, so PAY-31's rest stays not held. `SH-I-2120` is the help centre's section "Placing a test order": a title only, with no admin section, API group, plan line or app category of its own. How PAY-36's held rest enters the model is settled with Q3's other held misses, after the last batch.
