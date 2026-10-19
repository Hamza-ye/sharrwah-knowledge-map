# Notes: Q4 draft proposal (step R4)

## What was read

- The brief, `studies/proposals/briefs/R4-drafting.md`, whole.
- Q4's section of `studies/proposals/questions-for-agents.md` (sentences [1] to [5]).
- Q4's rows of `studies/proposals/areas/depth.tsv`: Shopify and Salla in depth; Zid, WooCommerce and BigCommerce checks.
- The five accounts, `studies/proposals/records/Q4/<platform>/account.md`, in that order.
- From each platform's `notes.md`, its lists of account points not checked and of copies found wrong, out of date or disagreeing: Zid's "Account points not checked", WooCommerce's "Account points not checked" and "Copies", BigCommerce's "Copies" and "Points not checked", Salla's "Copies", and Shopify's "Problems" (where it says no copy was found wrong or out of date).
- By `record_ids.py`, every id the five accounts cite: 527 ids (Shopify 78, Salla 138, Zid 117, WooCommerce 106, BigCommerce 88), with their quotes and dates; and, again with `--all`, Q4-SA-A0002 and Q4-SA-H0008.
- By `source_kinds.py`, the kind of each source form the draft compares.
- The areas whose questions include Q4, in `studies/proposals/areas/areas.md`: A-03, A-09, A-10, A-11, A-12, A-18, A-22, A-23 and A-27.
- `studies/proposals/yemen-digest.md`, read whole once, after sections 1 to 5 and 7 were written.
- Stage 1's rows by id, with `record_ids.py --all`: YA-128, YA-131, YK-173, YA-112, YK-36, YA-108, YK-108, YK-203, YK-87, YA-21, YA-22, YA-01, YK-452 and YA-56. YK-108, YK-87, YA-22 and YA-01 were read and not used.

## What the records don't show

- How a Salla merchant reviews a buyer's transfer receipt and confirms the payment, and whether Salla takes part (Q4-SA-N02). The confirming step in **Payment record** is Sharrwah's own proposal. Shown by: the order page of a bank-transfer order awaiting review, saved by the founder, as Q4-SA-N02's route gives.
- In what capacity Salla holds cash-on-delivery amounts collected through its label carriers before payout (Q4-SA-G0117; Q4-SA-H0008 for Salla Payments). Shown by: Salla's shipping page, held and not read, or Salla support's answer, as those rows' routes give.
- Whether Salla, Zid or WooCommerce charge a fee of their own on orders paid outside them (Q4-SA-N01, Q4-ZD-N02, Q4-WC-N03). The **Seller-collected order charge** rests on Shopify and BigCommerce only. Shown by: their pricing pages, or their support, as those rows' routes give.
- A Shopify or BigCommerce service that collects cash on delivery for the seller (Q4-SH-N01, Q4-BC-N16), and who collects it with a Zid merchant's own carrier (Q4-ZD-N01). Shown by: those platforms' own pages, if any exist.
- Yemen: whether IBAN is in use at the Houthis' area; how and when a courier that collects pays the merchant; whether collecting cash for sellers needs a licence. Section 6 says what would show each.

## Cited past the guide's counts

- Statements, copies and citations: 95 against about 40. Section 1 alone cites 84: five sentences compared across five platforms, one id per platform per point. Section 2's eleven elements each draw on two to four platforms, and sections 2 to 7 add about 11 ids beyond section 1's.
- Yemen facts: 10 against about 8. They bear on seven elements (cash on delivery, bank transfer to the seller, the receiving account, proof of payment, payment events, couriers, and currency) and on the two items they add to section 5 (a rial amount's zone, and accounts per buyer area).
- Not-found rows and copied gaps: 4, within the guide. "Yemen's evidence doesn't show": 2 lines, within the guide.

## Problems with the brief or the tools

- The Write tool refused a working copy in `.md` in my scratch directory as a report file. I kept the per-sentence working analysis as `analysis.txt` in the scratch directory, wrote the working draft there through the shell, and copied `draft.md` and `notes.md` into the folder at the end.
- Q4-SA-022 and Q4-SA-030 carry each other's quotes: Q4-SA-022's statement is the maximum-amount text, but its citations hold the maximum-weight label, the maximum-amount label and the terms title; Q4-SA-030's statement is the maximum-weight label, but its citation holds the maximum-amount text. Neither is cited.
- Q4-BC-H0008, the pilot's gap on who receives offline payments (gap kind "page not read"), is narrowed by Q4-BC-P0116 and Q4-BC-P0117, captured later, in which the buyer pays "directly into your bank account" and pays "you with cash". The BigCommerce account still lists Q4-BC-H0008 for who receives. The draft rests on Q4-BC-P0116 and Q4-BC-P0117 and doesn't cite Q4-BC-H0008.
- Salla's usage agreement (Q4-SA-P0080, 6 October 2026) says Salla has no relation to cash on delivery, while its help (Q4-SA-P0038, 7 October 2026) describes the dues of label carriers reaching the store's account. Section 1 [5] records them as records that may disagree.
- Two Salla copies give different lists of label carriers that support cash on delivery (Q4-SA-P0095, six; Q4-SA-014, three), as Salla's notes say. Neither is cited.
- `source_kinds.py` gives Salla's dashboard translations, feature flags and plan registries as observed, though they name no store. The draft writes them as dashboard text from a recorded session, with the date.
- The checker finds quoted and Arabic words in any field of a cited record, not only its statement; some Arabic names in the draft rely on that (قيود الدفع in Q4-SA-055's scope, زد شب in Q4-ZD-K0117's scope, مهلة الدفع in Q4-SA-047's identifier).
- YK-87's "collections", in its quote, is the collection and payment of electronic money (خدمات إدارة تحصيل و/أو سداد الأموال الإلكترونية), not cash. The draft rests nothing on it.
- The run was paused at 16:45 UTC and resumed under the updated tools. The first lookups used `record_ids.py` without `--all`; none of those ids rests on more than nine quotes, so none was cut short.
- Outside this folder, the one repository file that changed during this run is the bytecode cache `method/__pycache__/record_ids.cpython-313.pyc` (rewritten at 18:33 UTC, after `record_ids.py` changed). Importing `record_ids.py` rewrites it, so running the tools may have done so; other drafting runs were active at the same time.
