# Q3's check, batch Q-11: notes

Rows: `pay:PAY-01` to `pay:PAY-20`, the payment set's first twenty. Model at 513aebd8. The checker's final line is `20 of 20 rows placed; 0 problems`.

## Count by result

- covered: 18 (PAY-01, 03, 04, 06 to 20)
- partly: 2 (PAY-02, rest `candidate miss: held`; PAY-05, rest `candidate miss: not held`)
- beyond the class, candidate miss as a whole row, unclear: 0

## Candidate misses

**Tips (`pay:PAY-02`, held).** The row lists "adding a fee, tip or duty" among the events that change what a buyer owes. Fees are in the model: Salla lets the merchant raise or lower the cash-on-delivery fee, cited at `CM-PAY-029@salla`. Duties are `CM-TAX-008`. No capability covers tipping. What the map holds:
- Shopify's help-centre section "Setting up tipping options for online orders" (`SH-I-2109`). No cell cites it.
- Its concern, `SH-C-047`, lands only in `CM-CHK-001` (checkout). That is the coarser capability where a tipping capability would sit.

What I searched:
- `search`: in English (tip, tips, tipping, gratuity) on all five platforms; in Arabic too for Salla and Zid (إكرامية, الإكرامية, إكراميات, بقشيش, البقشيش);
- `outscope` on all five.

Nothing else was found.

**Try before you buy (`pay:PAY-05`, not held).** Pre-orders (`CM-SEL-005`), subscriptions (`CM-SEL-001`), instalments (`CM-PAY-015`) and stock held for unpaid orders (`CM-INV-008`) are all in the model. Try before you buy has no capability and no statement. What I searched:
- in English: try before you buy, try before, TBYB, deferred purchase, deferred payment;
- in Arabic for Salla and Zid: جرب قبل, جرب ثم ادفع, الدفع المؤجل, دفع مؤجل;
- `outscope` on all five.

What would settle it: Shopify's developer and help-centre pages on try-before-you-buy purchase options, captured into observed-sh. That Shopify documents it there, as a kind of selling plan, is an assumption.

## Rows that were hard to place, and why

- **Most rows are design questions asked in the abstract.** Eighteen of the twenty name neither "the platform" nor "Sharrwah" as the party asked (PAY-14 and PAY-17 name the platform only as one party among others), for example "Is the amount still owed held as one signed balance" (PAY-03) or "does one money model hold them all" (PAY-06). The brief's rule for such rows ("names neither asks both") gives each one `model;engineering`. Only PAY-09 and PAY-16 ask "the platform", so only they are `model` alone. What the class shows goes to `detail:`, and the design to engineering, before build.
- **Decisions in force that bind a covered row's design part.** This applies to PAY-01 (which party fills each role), PAY-06 (one money model), PAY-08 (who holds the funds) and PAY-19 (which record is authoritative). Decision 1 (C, 25 October) and the G3 (S-01) answer of 26 October already bind Sharrwah's side: a holder's ledger is a separate part, and an order's payment record is the same whoever holds the money. The brief has no way to record this for a covered row:
  - adding `founder` would set `before release` and raise `wrong time` and `bundles`, though the decision is taken;
  - `founder … decided` is only for a whole row that is beyond the class.

  I cited the decision in `basis` and marked how it binds as a reading.
- **PAY-12 (publishing payment arrangements to other surfaces).** Shopify's UCP profile names the store's payment handlers: `SH-I-1776` com.google.pay, `SH-I-1777` dev.shopify.card, `SH-I-1778` dev.shopify.shop_pay. No cell cites them. Their concern `SH-C-140` lands in `CM-AIA-005` (agentic commerce), and two of them also land in `CM-PAY-001` and `CM-PAY-014`. I read `CM-AIA-005` as the capability the row asks about, so the row is covered and the handlers are its detail. A stricter reading would make "publishing the accepted arrangements" its own held miss, with `CM-AIA-005` as the coarser capability. The coordinator may judge it otherwise. No statement holds credentials bound to one obligation and recipient.
- **PAY-10 (several arrangements on one obligation).** Shopify's "Collecting and recording partial payments" (`SH-I-2202`) is cited by no cell, and its concern lands in `CM-PAY-020`. I read `CM-PAY-020` (recording an order's payments) as the thing the row asks about, not a coarser capability, so the row is covered. No statement holds split tender at a counter.
- **PAY-08 (vouchers).** No statement held names a cash-voucher method. I read vouchers as local payment methods under `CM-PAY-017`, a reading, rather than calling them a miss. If the coordinator wants vouchers as their own arrangement, they would be a miss that isn't held.
- **PAY-14 (a buyer's proof of a bank transfer).** No statement holds it. Zid's "Upload bank transfer receipt" (`ZD-C-081/boundary/ZD-S-0912`) is for reverse orders, not payments. Bank transfer itself is `CM-PAY-030`, so the proof is detail.
- **Only one row has a time bomb.** PAY-18 has `bundles`, because `CM-CHK-005` (cart and checkout validation) is a `slot` and the rest are `class`. With `engineering` as the only answerer besides `model`, the checker raises no `wrong time`. So the rule above leaves these rows without that bomb, even PAY-12, whose `needed_by` is `later`.

## Problems with the brief or the scripts, for the coordinator before the other twelve batches

1. **`search` and `outscope` split `--terms` on `;` only, and a comma list silently finds nothing.** My first search, `--terms "tip,tipping,tips"`, printed "0 statements … match". The same terms separated by `;` found `SH-I-2109`. Neither the brief nor `--help` says the separator. An agent who uses commas will call a held thing "not held". Document `;` in the brief and in the help, or split on commas too.
2. **`class_slice.py model` doesn't print the cells' readings,** though the brief says it gives "a capability's cells and readings". It prints each cell's terms and placement, and the evidence keys that landed. To confirm, I looked once at the `reading` column of `merged/cells.tsv` for `CM-PAY-020`, which isn't among the scripts the brief names. Either print the reading, perhaps with a `--readings` flag, or correct the brief.
3. **`q3.py slice` for payment rows lists only the PAY area.** Its "elsewhere" leads, chosen by rarer words, missed most of what answers these rows:
   - `CM-INV-008` (stock held for unpaid orders) never appeared;
   - `CM-SEL-005` (pre-orders) didn't appear for PAY-05;
   - `CM-ORD-015` (order payment status) didn't appear for PAY-03 or PAY-20;
   - leads like `CM-SHP-012` (fulfilment network) for PAY-16 were noise.

   I found the answers with `caps --terms` and with `model` on ORD, CHK, RET, LOY, SEL and INV. A fixed companion list of areas for the `pay` set (ORD, CHK, RET, LOY, INV, SEL), or a `--areas` option on `slice`, would save the other batches this work.
4. **A held-miss rest can't sit beside a cited key in `basis`.** The checker refuses any cited statement key in a row whose rest is `candidate miss: held`, even when that key backs the covered part. On PAY-02, I had to drop `SA-C-115/decides/SA-S-0126` (Salla's cash-on-delivery fee, cited at `CM-PAY-029@salla`) and name only the cell. Better: test only the keys given for the miss, or give the miss its own column.
5. **The brief doesn't say where an uncited key goes when its concern lands in the capability that answers the row.** Examples: `SH-I-2202` in `CM-PAY-020`, `SH-I-2027` (Shopify's Payment reminder template) in `CM-NTF-001`, `SH-I-1776` to `1778` in `CM-AIA-005`. Such a row is covered by the brief's rule, but `basis` is for cells, adding keys only "where a cell's reading is what answers". I named these keys in `what_would_settle_it`, under `detail:`, so `q3.py unasked` and the amendment step can still see them. The brief could say this.
6. **No slot for a decision in force that binds a covered row's design part.** This is the second point under "hard to place". A `basis` convention, or a `who_answers` value such as `founder (decided)` that sets no time, would keep such decisions visible without raising false time bombs.

## Evidence

No problem with the evidence itself. Every key in the file was checked with `q3.py where`. Each key in `basis` either is cited by the cell it backs or, for the held miss, is cited by none.
