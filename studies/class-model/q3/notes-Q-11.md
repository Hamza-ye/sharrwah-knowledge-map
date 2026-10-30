# Q3's check, batch Q-11: notes

Rows: `pay:PAY-01` to `pay:PAY-20`, the payment set's first twenty. Model at 513aebd8. Written first to the brief as it stood, then brought to its revision of 7f6d2060 (`engineering:build` and `engineering:detail`; engineering only where a row asks a choice of Sharrwah's own; rulings in force cited) then to the clarification of 68fc7eaf (a subject or the founder answers wherever the row's thing is theirs, whatever its wording), and checked with the current `q3.py check`. Its final line is `20 of 20 rows placed; 0 problems`.

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

## Subjects and the founder (the clarification of 68fc7eaf)

Ten rows touch a thing a subject or the founder holds, whatever their wording. Each subject's part is named in `what_would_settle_it`. In `basis`, a subject that has run is cited by its register row and one that hasn't by `subjects.tsv S-NN`.

| row | added | why |
|---|---|---|
| PAY-01 | `founder`; `subject:S-01`, `S-04`, `S-06`, `S-10` | Who fills the roles in a market: who holds the money (S-01, decided: C, `S-01 S01-D1`), each method's provider (S-04), the licence for each regulated role, which bounds the roles one organization may hold (S-06), and the cash collector (S-10). Whether Sharrwah's own company fills a role is the founder's, decided for launch by Decision 1. |
| PAY-02 | `subject:S-05` | What an invoice records, and duties added to what a buyer owes. |
| PAY-04, PAY-05 | `subject:S-04` | Instalments, which S-04 carries: the pilot's Decision 13 moved to it (`S-01 S01-D13`). |
| PAY-06 | `founder`; `subject:S-11` | The seller's debts to Sharrwah are S-11's. Whether Sharrwah's own company holds stored value or lends is on the founder's list. |
| PAY-07 | `subject:S-05`, `S-09` | The tax a market fixes at the time of the order (S-05), and the currency and exchange rate an order records (S-09). |
| PAY-08 | `subject:S-01`, `S-04` | Who may hold the funds in a market (S-01, decided). Each method's provider, and what happens when one fails (S-04). |
| PAY-09 | `founder`; `subject:S-02`, `S-04` | Ruled in part by `S-02 S02-E1` and `S02-E2`. What a market requires to be offered is S-04's: Shopify names a local regulation that requires a pay-on-delivery method (`SH-C-084/reason/SH-S-0394`, cited at `CM-PAY-020@shopify`). Which methods a plan allows is plans and prices, the founder's. |
| PAY-14 | `subject:S-10` | The courier who collects cash on delivery, and so confirms its outcome. |
| PAY-19 | `subject:S-04`, `S-05` | What a provider credits net of fees (S-04). The invoice a market's law makes the record of what was agreed (S-05). |

The founder's part makes PAY-01, PAY-06 and PAY-09 `bundles`, since `before release` sits beside `before build`. No row has `wrong time`: every subject's time is before build, and those rows' `needed_by` is `model` or `spine`.

Some readings here can be argued:
- PAY-12's surfaces include "a marketplace, a buyer app", both on the founder's list. The row asks how a seller publishes its arrangements to such surfaces, not whether Sharrwah's own company runs one, so I left it `model`.
- PAY-11, PAY-15 and PAY-16 might touch a market's rules on stored credentials or authorization periods. No statement or subject points there, so I left them `model`.

## Rows that were hard to place, and why

- **Most rows are design questions asked in the abstract.** Eighteen of the twenty name neither "the platform" nor "Sharrwah" as the party asked (PAY-14 and PAY-17 name the platform only as one party among others). Under the revised rule they ask the model, with engineering added only where the row also asks a choice of Sharrwah's own:
  - `engineering:build`, an architecture decision, on six rows whose words propose a shape for Sharrwah's records: PAY-02 (each change recorded as its own agreement, apart from the money), PAY-03 (one signed balance, statuses derived), PAY-06 (one money model for every obligation), PAY-08 (arrangements as points in one space), PAY-19 (differences stored as their own records), PAY-20 (payment status derived from the money records);
  - `engineering:detail` on PAY-10 alone: the order in which parts of a split payment are allocated, and their caps, are a policy Sharrwah sets when the area is built. With `model` before build, that makes it `bundles`;
  - every other row asks what the class does, and is `model` alone. The line between "asks what the class does" and "asks a choice of Sharrwah's own" is a reading. PAY-07 (what is frozen when an order is accepted) and PAY-16 (each waiting state's deadline) could be read as asking a policy too; I read their words as asking the class.
- **Decisions in force that bind a covered row's design part.** This applies to PAY-01 (which party fills each role), PAY-06 (one money model), PAY-08 (who holds the funds) and PAY-19 (which record is authoritative). Decision 1 (C, 25 October) and the G3 (S-01) answer of 26 October already bind Sharrwah's side: a holder's ledger is a separate part, and an order's payment record is the same whoever holds the money. The brief has no way to record this for a covered row:
  - adding `founder` would set `before release` and raise `wrong time` and `bundles`, though the decision is taken;
  - `founder … decided` is only for a whole row that is beyond the class.

  I cited the decision in `basis` and marked how it binds as a reading. The revised brief's `S-NN <row id>` with `ruled` is for engineering's rulings; I used it for two that weren't vetoed: `S-01 S01-E3` (Sharrwah's fees in a billing part apart from sellers' payments) on PAY-06, and `S-01 S01-E4` (whoever holds the money carries out a refund, its result recorded on the order) on PAY-19. S01-E1 and S01-E2 are the founder's decisions of 26 October, so they are cited as `founder-decisions 2026-10-26 G3 (S-01)`. PAY-01 asks the class's roles, not which roles Sharrwah's own company fills (the founder's, decided for launch by Decision 1), so it is `model` alone, with Decision 1 named only in its text.
- **PAY-12 (publishing payment arrangements to other surfaces).** Shopify's UCP profile names the store's payment handlers: `SH-I-1776` com.google.pay, `SH-I-1777` dev.shopify.card, `SH-I-1778` dev.shopify.shop_pay. No cell cites them. Their concern `SH-C-140` lands in `CM-AIA-005` (agentic commerce), and two of them also land in `CM-PAY-001` and `CM-PAY-014`. I read `CM-AIA-005` as the capability the row asks about, so the row is covered and the handlers are its detail. A stricter reading would make "publishing the accepted arrangements" its own held miss, with `CM-AIA-005` as the coarser capability. The coordinator may judge it otherwise. No statement holds credentials bound to one obligation and recipient.
- **PAY-10 (several arrangements on one obligation).** Shopify's "Collecting and recording partial payments" (`SH-I-2202`) is cited by no cell, and its concern lands in `CM-PAY-020`. I read `CM-PAY-020` (recording an order's payments) as the thing the row asks about, not a coarser capability, so the row is covered. No statement holds split tender at a counter.
- **PAY-08 (vouchers).** No statement held names a cash-voucher method. I read vouchers as local payment methods under `CM-PAY-017`, a reading, rather than calling them a miss. If the coordinator wants vouchers as their own arrangement, they would be a miss that isn't held.
- **PAY-14 (a buyer's proof of a bank transfer).** No statement holds it. Zid's "Upload bank transfer receipt" (`ZD-C-081/boundary/ZD-S-0912`) is for reverse orders, not payments. Bank transfer itself is `CM-PAY-030`, so the proof is detail.
- **Five rows have time bombs, all `bundles`.**
  - PAY-18: `CM-CHK-005` (cart and checkout validation) is a `slot` and the rest are `class`.
  - PAY-10: the model's part is before build, engineering's detail at the area's build.
  - PAY-01, PAY-06 and PAY-09: the founder's part is before release.

  No row has `wrong time`. The six with `engineering:build` have a `needed_by` of `model` or `spine`, which is before build too. PAY-10's `slice` matches `engineering:detail`. PAY-12's `later` is answered by the model alone.

## Problems with the brief or the scripts, for the coordinator before the other twelve batches

1. **`search` and `outscope` split `--terms` on `;` only, and a comma list silently finds nothing.** My first search, `--terms "tip,tipping,tips"`, printed "0 statements … match". The same terms separated by `;` found `SH-I-2109`. Neither the brief nor `--help` says the separator. An agent who uses commas will call a held thing "not held". Document `;` in the brief and in the help, or split on commas too.
2. **`class_slice.py model` doesn't print the cells' readings.** The first brief said it did. Before the revision, I looked once at the `reading` column of `merged/cells.tsv` for `CM-PAY-020`. The revised brief points to `land_points.py cell` instead, and I used it to confirm two cells, `CM-PAY-029@salla` and `CM-ORD-015@shopify`. This is settled by the revision.
3. **`q3.py slice` for payment rows lists only the PAY area.** Its "elsewhere" leads, chosen by rarer words, missed most of what answers these rows:
   - `CM-INV-008` (stock held for unpaid orders) never appeared;
   - `CM-SEL-005` (pre-orders) didn't appear for PAY-05;
   - `CM-ORD-015` (order payment status) didn't appear for PAY-03 or PAY-20;
   - leads like `CM-SHP-012` (fulfilment network) for PAY-16 were noise.

   I found the answers with `caps --terms` and with `model` on ORD, CHK, RET, LOY, SEL and INV. A fixed companion list of areas for the `pay` set (ORD, CHK, RET, LOY, INV, SEL), or a `--areas` option on `slice`, would save the other batches this work.
4. **A held-miss rest can't sit beside a cited key in `basis`.** The checker refuses any cited statement key in a row whose rest is `candidate miss: held`, even when that key backs the covered part. On PAY-02, I had to drop `SA-C-115/decides/SA-S-0126` (Salla's cash-on-delivery fee, cited at `CM-PAY-029@salla`) and name only the cell. Better: test only the keys given for the miss, or give the miss its own column.
5. **The brief doesn't say where an uncited key goes when its concern lands in the capability that answers the row.** Examples: `SH-I-2202` in `CM-PAY-020`, `SH-I-2027` (Shopify's Payment reminder template) in `CM-NTF-001`, `SH-I-1776` to `1778` in `CM-AIA-005`. Such a row is covered by the brief's rule, but `basis` is for cells, adding keys only "where a cell's reading is what answers". I named these keys in `what_would_settle_it`, under `detail:`, so `q3.py unasked` and the amendment step can still see them. The brief could say this.
6. **No slot for a founder's decision in force that binds a covered row's design part.** This is the second point under "hard to place". The revision gives engineering's rulings a form, `S-NN <row id>` and `ruled`, but not the founder's decisions that rule a design part, such as S01-E2, decided at G3. I cited them as `founder-decisions <date> <gate>`, with the binding in the text. A line in the brief would make the other batches do the same.

## Evidence

No problem with the evidence itself. Every key in the file was checked with `q3.py where`. Each key in `basis` either is cited by the cell it backs or, for the held miss, is cited by none.
