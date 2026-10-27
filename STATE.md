# State

**What this file is:** where the work is, on one page (`PLAN.md`, section 9). Updated 27 October 2026.

**The plan:** `PLAN.md`. It is the plan the founder agreed at G0, and on 25 October 2026 the founder reset the work to it, as it stood at G1, with the pilot's own changes and the coordinator's engineering choices (its section 11).

**Where the work is:**
- Stages 0 to 3 are done (`PLAN.md`, section 4).
- **G1 is closed.** The founder answered Decision 1 on 25 October 2026 (C, with the three defaults, in every market at launch), and its two follow-ons on 26 October: E1 and E2 are kept, so the design keeps room for A and B; and default 2's "never" holds at launch (`founder-decisions.tsv`).
- **The pilot, S-01, is closed:** [`studies/subjects/S-01/register.tsv`](studies/subjects/S-01/register.tsv), and its review pack, [`reports/S-01-review.md`](reports/S-01-review.md).
- **G2 is answered:** "evidence" for all ten subjects, so each runs on the evidence, in the order of [`studies/subjects/subjects.tsv`](studies/subjects/subjects.tsv).
- **PR #7** (the reset, G1's close and S-01's review) is merged into `main` on the founder's word of 26 October.

**Open gate:** G3, after each subject. S-02 is under way.

**Waiting on the founder:** to hand the capture requests in [`handoffs/`](handoffs/README.md) (H-001 to H-007) to the local agent. H-005 may need a store on Salla's Special plan, a spending decision that comes with it.

**Stage 4, S-02, what a market is.**
- **Its frame:** [`studies/subjects/S-02/frame.md`](studies/subjects/S-02/frame.md).
  - **Three root decisions,** from the platforms' own top-level statements: the store's own country; the markets a store sells into; and what binds per market, and who sets it.
  - **What it starts from:** 36 concerns of the concern map, and the pilot's statements on where each way of holding money is offered, copied into each platform's `recorded.tsv` by `method/seed_subject.py`.
  - **Its steps:** the pilot's five steps under Stage 4's changes; the Yemen row (step 6) and the scenario walk (step 7) for each root decision; an independent review; the quote check (`method/check_report.py`); and a short report for G3, with its cost against the budget.
- **Budget:** 700 million agent tokens, counted by `method/count_tokens.py` (the founder, 27 October). The first, 200 million, was passed by a quarter in phase A; the founder said to continue, and that the budget never costs evidence about the references (`founder-decisions.tsv`).
- **How its agents run** ([`method-report.md`](studies/subjects/S-02/method-report.md), what each run taught): no more than two at once; each writes as it goes; a long reading list is split into parts, each read by a fresh agent that continues from the files, so no context grows large.
- **The founder's decisions of 10 October, F-01 to F-06 and O-01,** bind nothing (`founder-decisions.tsv`, the reset). What they raise comes with its evidence when a subject reaches it: O-01, which company contracts with sellers, in S-03; F-01, the company's ties, where a subject needs them, such as S-07's sanctions and screening.

**For the founder:** the orientation page, outside the repository: https://claude.ai/artifact/8fLCxo4JGKmGgPjXSpW1BN. It is updated at each milestone.

**Phase A is finished** for all five platforms (`method/count_tokens.py`; [`method-report.md`](studies/subjects/S-02/method-report.md), sections 2 to 4):

| Platform | Statements | How read | Agent tokens |
| --- | --- | --- | --- |
| Shopify | 588 | in full, in four agents: the help pages, the observed runs, the structures and the leads | 232 million |
| Salla | 310 | in full, in two agents | 126 million |
| Zid | 172 | from what is recorded, and the held pages a gap needed | 75 million |
| WooCommerce | 227 | from what is recorded, and the release's files on countries | 48 million |
| BigCommerce | 161 | from what is recorded | 23 million |

The checker finds every quote, 3,193 of them, and no error. With the briefs' inspections (30 million), S-02 has spent about 534 million of its 700 million. **The rest is projected at 350 to 650 million,** so S-02 at about 0.9 to 1.2 billion, past the budget plus a quarter ([the frame's budget](studies/subjects/S-02/frame.md#budget)). The projection is measured again after phase B's first parts, and the cost comes to the founder when the spending passes 875 million (`PLAN.md`, section 8).

**In flight:**
- **Phase B** ([`b/parts.tsv`](studies/subjects/S-02/b/parts.tsv)): six of its ten parts are done, with no checker error. RD1, the store's own country, is through its first pass: 19 variation points and 240 rows, with a row for each platform under each. RD3 has 44 points from Shopify and Salla. RD3-3, for Zid and BigCommerce, is running. Each part's lessons go into the brief ([`method-report.md`](studies/subjects/S-02/method-report.md), section 7).
- **The absence audit** (phase A3; the method report, section 8): Salla's and Shopify's are done. Each found a gap routed to capture answered by what is held, so [H-002](handoffs/H-002-observed-sa-onboarding-countries.md) and [H-007](handoffs/H-007-observed-sh-store-country-sign-up.md) are narrowed. Zid's first part is running; Zid's second part, WooCommerce's and BigCommerce's follow.

**Next:** phase B in ten parts ([`b/parts.tsv`](studies/subjects/S-02/b/parts.tsv)), two at a time, each a fresh agent reading only its part of its root decision's slice. Then gap-closing and the absence audit where a root decision needs them, phase B's second pass, and phase C.

**To resume:** read `PLAN.md`, this file and `founder-decisions.tsv`.
