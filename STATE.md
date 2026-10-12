# State

Where the work is, kept by the coordinating session under `PLAN.md` section 9. Updated and committed at every checkpoint.

**Updated:** 12 October 2026.

**Gate G0:** passed on 12 October 2026 (`founder-decisions.tsv`).

**Stage 0, repair and freeze: done on 12 October 2026.**
- **Gaps re-routed** by `method/q1_held_check.py` (`studies/concern-map/held-check.tsv`): 215, none closed.
  - Salla, 206:
    - 134 pages held in observed-sa that had been routed to the founder;
    - 64 "searched, not found" rows that never searched the help-centre articles;
    - 8 KYC rows sent to the held `kyc-schema` structure.
  - WooCommerce, 9: the incorporated Stripe agreement may now be read (G0).
  - Shopify, Zid and BigCommerce: none needed. Each of their "searched, not found" rows names what it read.
- **The founder's save list:** 94 of its 147 addresses are held and now ticked. 53 are not held, and none is asked of the founder until a subject needs it.
- **The checker** now enforces the Stage 0 rules. Run on Salla's gaps before Stage 0, they flag 134, 64 and 1 rows. The checker passes on all five platforms, with statements and quotes identical to before.
- **New tools:**
  - `method/held_index.py` (what is held, by address);
  - `method/warc_text.py` (reads a record in a fetch archive);
  - `method/quote_check.py` (the shared verbatim check).
- **Noted, not asked:** observed-sh's 70 fetch archives aren't in git. A page held only there is readable from this repository only if a subject needs it and the founder commits the archive.

**Running: Stage 1, Yemen's axes and cases.**
- The brief (`studies/yemen-cases/brief.md`) was inspected by a separate agent: 11 must-fix and 3 optional findings, all addressed. It is being re-inspected before the run.
- Then:
  - one agent reads `evidence/yemen/`;
  - `method/check_yemen_cases.py` checks the output;
  - a separate agent reviews it;
  - the coordinator compares Q2's example axes with what the evidence showed, and logs any example it didn't show as an unknown.

**Evidence heads:**
- **observed-sa `4ca2e896`.** It now holds items 6, 7, 9, 10 and 11:
  - the help centre's 2,938 articles as text;
  - the eleven pages about Salla's terms as text;
  - the fetch archives in git, except five over GitHub's size limit.
- **observed-sh `e49840729`.** Its fetch archives aren't in git.
- **The map's citations** are at observed-sa `145f137` and observed-sh `b46731d0` / `e49840729`.

**Open for the founder:** Q3's rows, both sets or one, needed at the pilot's step 3. The 81 payment rows are in `register/pay-questions.tsv`. The Knowledge Map's 179 questions are in no repository this work holds, so the founder will be asked where they are when the pilot reaches step 3.
