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

**Waiting on the founder:**
- **the local agent's runs, and the founder's word on how they went** (27 October, evening). Its runs for H-006, H-007 and H-008 are in progress in observed-sh. The founder said they would pass H-001 to H-003 and H-005's step 1 for observed-sa. RD1's phase C waits for that word. Held evidence already answers part of each request (below);
- the answers in [`reports/S-02-evidence-requests.md`](reports/S-02-evidence-requests.md), for the evidence only the founder can get: a Zid store, a BigCommerce trial, a WooCommerce test store, and questions to four platforms. Nothing waits on them: the second pass and phase C go on.

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

At phase A's end, the checker found every quote, 3,193 of them, and no error. With the briefs' inspections (30 million), S-02 had then spent about 534 million of its 700 million. The latest measure of its cost is under **Cost**, below ([the frame's budget](studies/subjects/S-02/frame.md#budget)).

**Since the evening of 27 October** ([`method-report.md`](studies/subjects/S-02/method-report.md), sections 9 to 11):
- **The second pass's parts are done:** RD1-S1 to RD1-S4, RD2-S1, RD3-S1 to RD3-S8. The coordinator ruled on the parts' candidates for a new point: two `who sets` points raised (S02-VP-91, S02-VP-92), and the rest left noted ([`b/second-pass.md`](studies/subjects/S-02/b/second-pass.md)).
- **Held evidence first.** The founder's local agent showed that the search tool had never read Shopify's admin and sign-up code, held in tracked archives. The tool now reads code bundles. Three parts read held files before any run:
  - **Shopify (A2-SH-H):** 35 statements, and its five gaps narrowed to what the runs in progress can show.
  - **Salla (A2-SA-H, A2-SA-S):** the dashboard's own definitions show which of its settings take a value per market. Seven sections do, each behind the feature `multi-countries`, on the Special and Pro plans.
  - **WooCommerce (A2-T):** its settings code.
- **Phase B is complete:** 75 points and 904 rows, every statement placed or noted, and the full check finds no error. The audit of the late parts' absences (A3-2) confirmed five and partly contradicted two.
- **Phase C compares the platforms on each answer of a point, one at a time,** after two dry runs ([`briefs/C-analysis.md`](studies/subjects/S-02/briefs/C-analysis.md)). Its parts are in [`c/parts.tsv`](studies/subjects/S-02/c/parts.tsv):
  - RD2 is done;
  - RD3's first three parts are done, and its fourth is running;
  - RD1's two parts wait for the founder's word on the handoffs.

  Most founder items ask one question, setting by setting: does it take a value per market, or once for the whole store? The register asks it once.
- **The usage limit stopped two parts at about 20:40 UTC;** their work was saved. The founder moved to Max x20, and both were resumed.

**Earlier:**
- **Phase B's first pass is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 7): 73 variation points, each with a row for every platform, 671 rows, in [`variation-points.tsv`](studies/subjects/S-02/variation-points.tsv) and [`variants.tsv`](studies/subjects/S-02/variants.tsv). The full check gives no error.
- **The absence audit is complete** (section 8): 24 claims; 19 confirmed, 3 partly contradicted, 2 contradicted; 122 statements added. Two capture requests are narrowed ([H-002](handoffs/H-002-observed-sa-onboarding-countries.md), [H-007](handoffs/H-007-observed-sh-store-country-sign-up.md)), and three tools fixed to see held evidence they had missed.
- **Gap-closing (phase A2) is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 9; [`a2-parts.tsv`](studies/subjects/S-02/a2-parts.tsv)): 22 parts, 121 rows, 118 of them given statements and 83 with no gap left; 1,165 statements; 337 million. Its live pages are captured, and every quote is found; twelve are ruled on after review. 49 gaps remain: 15 for the local agent, in H-008 (new) and H-002 and H-005 (extended); 34 for the founder.
- **The render fault:** the browser in this session failed some sites' scripts, so BigCommerce's Help Center and Zid's sites rendered empty or as an error text; agents read zid.eg's Terms from a source that held the Saudi Terms. The tools now fetch each request outside the browser, open what a click shows, and tell a page's source from what it shows. 32 pages are held again as they render; Zid's audit of G03 was redone (for Egypt, the contract is with Zid Egypt, under Egyptian law). Every capture run now has its README.
- **Cost:** 1,285 million agent tokens by 19:04 UTC on 27 October, past the budget plus a quarter (875 million); the cost came to the founder at 09:55 ([the frame's budget](studies/subjects/S-02/frame.md#budget)). S-02 is projected at about 1.45 to 1.55 billion. The work goes on; no higher plan is needed yet. The coordinating session's own tokens: 606 million since S-02 began.

**Next:**
1. When C-RD3-4 reports: RD3's phase C is done. Merge and check phase C's files.
2. When the founder's local agent pushes: read its runs, and close or narrow the gaps they answer. Then place the new statements and run the keys they touch again. With the founder's word on how the handoffs went, RD1's phase C.
3. Then the Yemen row and the scenario walk, for each root decision; the register; the independent review; and S-02's report for G3.

**To resume:** read `PLAN.md`, this file and `founder-decisions.tsv`.
