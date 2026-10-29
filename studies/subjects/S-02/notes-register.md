# S-02, the register's draft: notes (REG-1)

**What this file is:** the drafting agent's notes on `register.tsv` and `decisions.md`, under `briefs/D-register.md`: the calls I made, and the problems I found with the brief or the evidence. Each call is mine, for the coordinator's check and the review.

## The register's shape

The register has 41 rows:
- 11 drivers (S02-R1 to S02-R11);
- 7 founder decisions: RD1 has 3 (D1 to D3), RD2 has 2 (D4, D5) and RD3 has 2 (D6, D7), all within the brief's four per root decision;
- 8 moved rows (S02-M1 to S02-M8), one for each of S-03, S-04, S-05, S-07, S-08, S-09, S-10 and S-11;
- 10 follows-by-rule rows (S02-F1 to S02-F10). RD2 has no key bound per market and none kept open, so it has two such rows;
- 5 engineering constraints (S02-E1 to S02-E5).

Of the 142 founder items:
- 85 go to the seven decisions;
- 57 go to the moved rows.

Some items sit in a decision of another root decision: see call 1.

Read per row: D1 has 6, D2 7, D3 10, D4 16, D5 8, D6 34 and D7 4; M1 has 9, M2 17, M3 5, M4 19, M5 1, M6 1, M7 2 and M8 3.

## Calls I made

1. **Grouping by the question the founder answers.** Most items are grouped within their own root decision. A few went to the decision whose question they ask:
   - **RD3's "store's own country" keys** go to D3, since they ask what the seller's country decides: S02-VP-41, S02-VP-55 and S02-VP-57.
   - **RD3's keys for channels, points of sale and customer groups "outside its markets"** go to D4, since whether those are kinds of market is D4's question: S02-VP-47|a channel, S02-VP-47|a location, S02-VP-49|a group of customers, S02-VP-67|a channel and S02-VP-68|a location.
   - **S02-VP-73** (placing a buyer in a market; which customers may enter one) goes to D5.
   - **S02-VP-85** (a country per market, shown as the store's) goes to D1. D1 answers it as a display value only, held under D6.
   - **S02-VP-49|the buyer's country** (a price per country within a market) goes to D7.
   - **S02-VP-55|the buyer's country** (checkout fields) goes to D6, as a narrower key of the same interface.
2. **What stands apart:**
   - **D1 stands apart from D3.** Changing D1 later is a redesign, since the data model changes; changing D3 is one module once the interface exists.
   - **D7 stands apart from D6.** Its later change reaches every money record, and S-09's decision follows from it.
   - **Payment methods, tax and shipping per market stay in D6.** S-04, S-05 and S-10 decide their values. Their holding is D6's mechanism, and changing that later costs a setting once D6's interface exists.
3. **Moved rows.**
   - I kept phase C's own subject label for every item whose wording carries one.
   - I assigned the unlabelled items by the brief's list:
     - S02-VP-11, S02-VP-12 and S02-VP-13 go to S-04;
     - S02-VP-14 goes to S-11;
     - S02-VP-15 goes to S-05;
     - S02-VP-19 goes to S-08;
     - S02-VP-05's assessors and government bodies, S02-VP-10, and S02-VP-07's two verification keys go to S-07.
   - **S02-VP-81** (the platform setting a store's status, by default for a new store or by closing a store under its terms) goes to S-03. My reading is that closing a store is a term of the merchant's contract, while the status itself is held under D6. A reviewer may prefer to keep it in S-02.
4. **S02-VP-07|a billing currency supported for the billing address's country** stays with S-09, phase C's label, though S-11 meets it through S02-VP-14 (the currency of Sharrwah's fees). The two subjects should read both rows.
5. **Columns.**
   - For moved rows, what S-02 settles is in `recommendation`, not `answer`, because it rests on D1 and D3, which are the founder's to accept.
   - `answer` is empty on every decision and moved row. It holds text only on drivers (the founder's decisions in force) and on follows-by-rule rows, as S-01's register does.
6. **Follows-by-rule rows list their keys in `vp_id`,** as `vp_id|key`. The brief names no column for them, and `method/register_items.py` counts any name in `answers_items` that isn't a founder item as an error.
7. **S02-E5 is a reading.** It says which market carries S-01's holding arrangement: the seller's own country, through the business entity that takes the payment.
   - The frame asks S-02 to say this, but no founder item covers it.
   - So it is an engineering constraint the founder may veto, not a decision.
8. **No market in a recommendation.** Recommendations name platforms, never a market or a market's facts. Market names appear only as phase C's keys, in `answers_items` and in the follows rows' `vp_id`, as data.
9. **Kinds and causes.** The kinds in `alternatives` come from `variants.tsv`, for the variants each option cites. The causes come from `c/<RD>/answers.tsv`.

## Problems with the brief or the evidence

1. **Section name.** The brief cites the frame's "How S-02 relates to other subjects"; the frame calls that section "Where it meets other subjects".
2. **Subjects the frame doesn't name.** The frame's section names S-01, S-03, S-04, S-05, S-07, S-09 and S-10, but not S-08 (data) or S-11 (what Sharrwah charges). The brief adds both, and I followed the brief.
3. **A commonality with no platform.** S02-VP-26|a group of customers is recorded as a commonality with an empty `gives` (`c/RD2/answers.tsv`). S02-F5 lists it as phase C has it. A reviewer should check whether it is a common absence.
4. **One key, two things.** S02-VP-06|the platform joins two different things:
   - Shopify's support changing a store's billing address or default entity on request (S02-V-064, S02-V-269);
   - WooCommerce's code migrating a stored location's state code (S02-V-276).

   My first draft of D2 read both as staff acting under a contract; I corrected it, and D2 now cites them apart.
5. **D6's size.** D6 answers 34 items, which ask one question of 18 settings. Apart from currency (D7), I found no setting among them whose later change costs more in kind once the interface exists.
6. **Inconsistent labels.** Phase C labelled some moved items with their subject and not others, so call 3 is mine. The review should check it.
7. **Length.** `decisions.md` is about 2,900 words, within six pages.
