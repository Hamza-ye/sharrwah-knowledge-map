# State

**What this file is:** where the work is, on one page (`PLAN.md`, section 9). Updated 26 October 2026.

**The plan:** `PLAN.md`. It is the plan the founder agreed at G0, and on 25 October 2026 the founder reset the work to it, as it stood at G1, with the pilot's own changes and the coordinator's engineering choices (its section 11).

**Where the work is:**
- Stages 0 to 3 are done (`PLAN.md`, section 4).
- **G1 is closed.** The founder answered Decision 1 on 25 October 2026 (C, with the three defaults, in every market at launch), and its two follow-ons on 26 October: E1 and E2 are kept, so the design keeps room for A and B; and default 2's "never" holds at launch (`founder-decisions.tsv`).
- **The pilot, S-01, is closed:** [`studies/subjects/S-01/register.tsv`](studies/subjects/S-01/register.tsv), and its review pack, [`reports/S-01-review.md`](reports/S-01-review.md).
- **G2 is answered:** "evidence" for all ten subjects, so each runs on the evidence, in the order of [`studies/subjects/subjects.tsv`](studies/subjects/subjects.tsv).
- **PR #7** (the reset, G1's close and S-01's review) is merged into `main` on the founder's word of 26 October.

**Open gate:** G3, after each subject. Next: S-02.

**Waiting on the founder:** nothing.

**Next: Stage 4, S-02, what a market is.**
- **Budget:** 200 million agent tokens, counted by `method/count_tokens.py`. It is set from the pilot's measured cost (about 1.03 billion, of which about half a billion for a clean run, by its method report, section 12), reduced for the plan's changes: S-02 starts from its root decisions and from the statements the concern map already holds, reads Shopify and Salla in full and the other three from what is recorded, and keeps each agent's run short. At 250 million it stops and comes to the founder (`PLAN.md`, section 8).
- **Its framing adds the concerns its draft row missed.** The row cites Shopify's Managed Markets (SH-C-110), a cross-border service, but not the core markets concerns: Shopify's Markets (SH-C-106) and backup region (SH-C-113), Zid's markets and served countries (ZD-C-034, ZD-C-032), and Salla's country reference data (SA-C-166). The row's grouping was the coordinator's reading; the founder's G2 mark doesn't change.
- **Its steps:** the pilot's five steps under Stage 4's changes; then the Yemen row (step 6) and the scenario walk (step 7) for each root decision; an independent review; the quote check (`method/check_report.py`); and a short report for G3 with its cost against budget.
- **The founder's decisions of 10 October, F-01 to F-06 and O-01,** bind nothing (`founder-decisions.tsv`, the reset). What they raise comes with its evidence when a subject reaches it: O-01, which company contracts with sellers, in S-03; F-01, the company's ties, where a subject needs them, such as S-07's sanctions and screening.

**For the founder:** the orientation page, outside the repository: https://claude.ai/artifact/8fLCxo4JGKmGgPjXSpW1BN. It is updated at each milestone.

**In flight:** nothing. No agent is running.

**Evidence read:** observed-sh at `febbf6c`, observed-sa at `4ca2e89` (the clones' heads on 25 October 2026), and WooCommerce 11.2.1.

**To resume:** read `PLAN.md`, this file and `founder-decisions.tsv`.
