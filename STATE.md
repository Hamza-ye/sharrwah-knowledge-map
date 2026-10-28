# State

**What this file is:** where the work is, on one page (`PLAN.md`, section 9). Updated 28 October 2026.

**The plan:** `PLAN.md`. It is the plan the founder agreed at G0, and on 25 October 2026 the founder reset the work to it, as it stood at G1, with the pilot's own changes and the coordinator's engineering choices (its section 11).

**Where the work is:**
- Stages 0 to 3 are done (`PLAN.md`, section 4).
- **G1 is closed.** The founder answered Decision 1 on 25 October 2026 (C, with the three defaults, in every market at launch), and its two follow-ons on 26 October: E1 and E2 are kept, so the design keeps room for A and B; and default 2's "never" holds at launch (`founder-decisions.tsv`).
- **The pilot, S-01, is closed:** [`studies/subjects/S-01/register.tsv`](studies/subjects/S-01/register.tsv), and its review pack, [`reports/S-01-review.md`](reports/S-01-review.md).
- **G2 is answered:** "evidence" for all ten subjects, so each runs on the evidence, in the order of [`studies/subjects/subjects.tsv`](studies/subjects/subjects.tsv).
- **PR #7** (the reset, G1's close and S-01's review) is merged into `main` on the founder's word of 26 October.

**Open gate:** G3, after each subject. S-02 is under way.

**Waiting on the founder:**
- **access to the repository `other-product-class`,** where the founder's local agent holds its Zid evidence (`zid/`, commit `2b8920b`), and will hold BigCommerce's and WooCommerce's. This session's GitHub access is fixed to the repositories it started with, so it can't clone it (28 October). Its 23 Zid answers wait on it.
- *Done on 28 October:* the Salla capture requests ran at observed-sa `b0bd0b16`, and part A2-SA-R is reading them. The founder's report on them lifts RD1's wait. The founder asked that each remaining gap be pursued only if closing it could change an S-02 decision and a proportionate route exists: [`gap-assessment.tsv`](studies/subjects/S-02/gap-assessment.tsv) gives each gap's verdict;
- the answers in [`reports/S-02-evidence-requests.md`](reports/S-02-evidence-requests.md), for the evidence only the founder can get: a Zid store, a BigCommerce trial, a WooCommerce test store, and questions to five platforms, Shopify's added on 28 October. Nothing waits on them: phase C goes on.

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
  - RD2 and RD3 are done: 56 points, 247 keys;
  - RD1's two parts wait for the founder's word on the handoffs.

  Most founder items ask one question, setting by setting: does it take a value per market, or once for the whole store? The register asks it once.
- **The usage limit stopped two parts at about 20:40 UTC;** their work was saved. The founder moved to Max x20, and both were resumed.

**The capture round (27 and 28 October)** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 12). The founder's local agent ran H-006, H-007 and H-008, and observed-sh holds the runs at `19a5f6435`. The founder relayed its notes, which went to the parts as leads. The parts recorded only what the run files and pages show:
- **Gap-closing, two parts (A2-SH-R1, A2-SH-R2):** 125 Shopify statements.
  - G10 and G11 are answered. A sign-up that chose the United States from a network traced to Yemen made an American store. The checkout's address form is held for five more countries.
  - G09, G12 and G13 are narrowed to G14 to G16, which only Shopify can answer: whether a change of country is checked after it saves; markets per plan; business types for Managed Markets. Shopify Payments stops at a valid SSN or ITIN.
  - The local agent's five pointers to held evidence are recorded.
- **Phase B's capture round, three parts:** every new statement placed or noted, 906 rows, and the full check finds no error.
- **A method ruling:** a key that every platform lacks or doesn't state is `no difference`, a commonality the references don't carry (the local agent's recommendation, and C-RD2's problem 3).
- **Phase C again on the touched keys (part C-R), done.** Four keys changed: two `the whole store` keys (S02-VP-57, S02-VP-63) and S02-VP-26's `a group of customers` became commonalities, and an app's value per market became a founder item (S02-VP-86). RD2 and RD3 hold 247 keys. 72 founder items, 61 of them S-02's own, in 46 wordings; 20 keys are kept open.
- **Handoffs:** H-006 to H-008 are marked done, at the commit, in [`handoffs/README.md`](handoffs/README.md).

**Earlier:**
- **Phase B's first pass is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 7): 73 variation points, each with a row for every platform, 671 rows, in [`variation-points.tsv`](studies/subjects/S-02/variation-points.tsv) and [`variants.tsv`](studies/subjects/S-02/variants.tsv). The full check gives no error.
- **The absence audit is complete** (section 8): 24 claims; 19 confirmed, 3 partly contradicted, 2 contradicted; 122 statements added. Two capture requests are narrowed ([H-002](handoffs/H-002-observed-sa-onboarding-countries.md), [H-007](handoffs/H-007-observed-sh-store-country-sign-up.md)), and three tools fixed to see held evidence they had missed.
- **Gap-closing (phase A2) is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 9; [`a2-parts.tsv`](studies/subjects/S-02/a2-parts.tsv)): 22 parts, 121 rows, 118 of them given statements and 83 with no gap left; 1,165 statements; 337 million. Its live pages are captured, and every quote is found; twelve are ruled on after review. 49 gaps remain: 15 for the local agent, in H-008 (new) and H-002 and H-005 (extended); 34 for the founder.
- **The render fault:** the browser in this session failed some sites' scripts, so BigCommerce's Help Center and Zid's sites rendered empty or as an error text; agents read zid.eg's Terms from a source that held the Saudi Terms. The tools now fetch each request outside the browser, open what a click shows, and tell a page's source from what it shows. 32 pages are held again as they render; Zid's audit of G03 was redone (for Egypt, the contract is with Zid Egypt, under Egyptian law). Every capture run now has its README.
- **Cost:** 1,408 million agent tokens by 00:39 UTC on 28 October, past the budget plus a quarter (875 million). The cost came to the founder at 09:55 on 27 October ([the frame's budget](studies/subjects/S-02/frame.md#budget)). The capture round cost 55 million. S-02 is projected at about 1.5 to 1.6 billion. The work goes on on the founder's Max x20 plan. The coordinating session's own tokens: 719 million since S-02 began.

**Next:**
1. With the founder's word on the Salla capture requests: read any runs they made, close or narrow their gaps, place the statements, then RD1's phase C (C-RD1-1, C-RD1-2).
2. Then the Yemen row and the scenario walk, for each root decision; the register; the independent review; and S-02's report for G3.

**To resume:** read `PLAN.md`, this file and `founder-decisions.tsv`.
