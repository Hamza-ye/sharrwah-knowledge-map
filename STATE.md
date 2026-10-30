# State

**What this file is:** where the work is, on one page (`PLAN.md`, section 9). Updated 29 October 2026.

**The plan:** `PLAN.md`. It is the plan the founder agreed at G0, and on 25 October 2026 the founder reset the work to it, as it stood at G1, with the pilot's own changes and the coordinator's engineering choices (its section 11).

**Where the work is:**
- Stages 0 to 3 are done (`PLAN.md`, section 4).
- **G1 is closed.** The founder answered Decision 1 on 25 October 2026 (C, with the three defaults, in every market at launch), and its two follow-ons on 26 October: E1 and E2 are kept, so the design keeps room for A and B; and default 2's "never" holds at launch (`founder-decisions.tsv`).
- **The pilot, S-01, is closed:** [`studies/subjects/S-01/register.tsv`](studies/subjects/S-01/register.tsv), and its review pack, [`reports/S-01-review.md`](reports/S-01-review.md).
- **G2 is answered:** "evidence" for all ten subjects, so each runs on the evidence, in the order of [`studies/subjects/subjects.tsv`](studies/subjects/subjects.tsv).
- **PR #7** (the reset, G1's close and S-01's review) is merged into `main` on the founder's word of 26 October.

**The founder's intent (29 October 2026).** Sharrwah is a merchant platform of the class that Shopify represents worldwide and Salla and Zid in the region. Its extent comes from the class, not from the launch, and what fills a slot in a market never defines the platform (`founder-decisions.tsv`; the handoff and the go, verbatim, in `founder-messages/`; the review, [`reports/intent-review.md`](reports/intent-review.md)).
- **The founder decides** the items on their list (`PLAN.md`, section 3). Everything else is engineering's, and each ruling is listed for the founder's veto.
- **The plan** now puts the class's model before architecture (`PLAN.md`, Stage 4A). The subjects continue beside it, as the analysis of where the class varies by market.
- **Architecture** has its own plan, written by established practice, which comes to the founder with the extent's report at gate GM. Architecture starts on the founder's go on that plan (30 October). The extent's budget is 250 million agent tokens, and the plan's about 30 million.
- **The founder's change of 30 October** (`founder-decisions.tsv`): line (3) is taken out of the intent's row. What keeping room means is stated in the architecture plan, by established practice, with S-02's D9 as its worked example.
- **The founder's answers before GM (30 October)** (`founder-decisions.tsv`; verbatim in `founder-messages/2026-10-30-before-gm.md`):
  - **S-02:** no veto on D1 to D9 or E1 to E5. RD2's plan items (how many markets a plan allows, which kinds it offers) are plans and prices, and come to the founder with plans: register row S02-M9.
  - **When the subjects' points land on the model,** a conflict is reopened with its evidence, not forced to fit. A founder's own decision isn't reopened by engineering: the conflict goes to the founder.
  - **The architecture plan** grades its sources by the Knowledge Map's source types.
  - **At GM,** the Knowledge Map's page comes too, rebuilt by script from the model's files.

**Open gate:** GM, after the class's model's extent: its report with the Knowledge Map's page rebuilt from the model, and the founder's go on the architecture plan. S-02 has reached its end; the founder vetoed none of its rulings.

**Waiting on the founder:** nothing until GM. The founder may veto any ruling at any time.

*Settled on 28 October:*
- **The founder's evidence is in.** The founder's local agent took Salla and Zid as far as they can be taken:
  - Salla's runs are in observed-sa at `b0bd0b16`;
  - Zid's, BigCommerce's and WooCommerce's are in `other-product-class`, read from the founder's own repository, or from this repository's mirror branch where a session can't reach it (`CLAUDE.md`).
- **The founder's rule for what remains:** a gap is pursued only if closing it could change the class's model or a decision (widened on 29 October), and a proportionate route exists. [`gap-assessment.tsv`](studies/subjects/S-02/gap-assessment.tsv) gives each gap's verdict.
- **The scope:** MENA is the target, and Yemen is one market among those. Neither Yemen's circumstances nor today's capacity becomes a permanent constraint without a justified reason (`founder-decisions.tsv`).

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

**Salla and Zid (28 October).** Two gap-closing parts read the founder's local agent's captures, recording only what the files show:
- **Salla (A2-SA-R):** 75 statements, from the runs for H-001 to H-005 at observed-sa `b0bd0b16`.
  - **Answered:** G03 and G04.
  - **Narrowed:** G01, G05 and G07, into G16 to G18.
  - **Left:** seven. Salla refused the multi-market activation, and the UAE verification waits on Salla's review.
- **Zid (A2-ZD-R):** 39 statements and 13 absences, from a public demo store and a development store, both without Zid's markets screens.
  - **Answered:** 10 gaps. Seven of those answers rest on absences from the dashboard's complete route list: it holds no page under a market for those settings.
  - **Narrowed:** 10 gaps, into G24 to G33. Only G30 (who checks a store's country after it changes) stays open, for RD1's analysis. The others can't change an S-02 decision, or belong to a later subject (S-03, S-05, S-07).
  - **Closed:** 3, which can't change a decision.
- **The audit of Zid's absences (A3-ZD-R):**
  - **Confirmed: 12.** The market's own page and its code hold only its name, countries, currency and publication, and no setting's page names a market.
  - **Contradicted: 1, on countries.** Zid's cities answer covers 173 countries, more than the 162 a store's address offers.
- **Phase B's round is done,** in five parts ([`b/second-pass/parts.tsv`](studies/subjects/S-02/b/second-pass/parts.tsv), [`method-report.md`](studies/subjects/S-02/method-report.md), section 13). The full check finds no error and nothing unplaced: 75 points, 923 rows. The coordinator's rulings are in [`b/second-pass.md`](studies/subjects/S-02/b/second-pass.md).
- **Phase C is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 14). The full check finds no error.
  - **Keys:** 361.
  - **What follows:** 53 commonalities; 17 bound per market; 33 kept open; 116 left to the build; 142 founder items, in 90 wordings (143 after BigCommerce's and WooCommerce's round).
- **Two container restarts on 28 October** stopped two parts each time. Both resumed from their transcripts, and nothing was lost.
  - **What the logs show:** the platform moved the idle session onto a new VM. It wasn't memory, and it wasn't the disk.
  - **The disk** is now at 76% of the allowance, from 86%, after 4.2 GB of obsolete copies and caches were deleted.

**S-02's end (29 October, overnight; [`method-report.md`](studies/subjects/S-02/method-report.md), section 15).** Agents drafted each step from its brief, and the coordinator checked each before the next built on it. Nothing was decided for the founder.
- **The register** ([`register.tsv`](studies/subjects/S-02/register.tsv)):
  - the founder items, 143 after BigCommerce's and WooCommerce's round, asked as nine decisions: 85 items in D1 to D7, and D8 and D9 from the Yemen row's product gaps;
  - 58 items moved to the subjects that own them;
  - five engineering constraints.

  Both checks are clean: every item answered or moved once, and 803 citations.
- **The Yemen row** ([`yemen-row.tsv`](studies/subjects/S-02/yemen-row.tsv)): 49 rows, each fact checked against its quote and read with `corrections.md`.
- **The scenario walk** ([`scenario-walk.tsv`](studies/subjects/S-02/scenario-walk.tsv)): 51 scenarios. 41 cost a setting and 9 one module. 1 is a redesign: data held in-country, a hypothesis for S-08.
- **Designs beyond the references,** for D8 and D9 ([`designs.tsv`](studies/subjects/S-02/designs.tsv)): 11 sources, captured in `evidence/designs/`. They changed both recommendations.
- **The independent review** ([`review.md`](studies/subjects/S-02/review.md)): 24 findings, 9 of them must fix. All are resolved after its re-checks.
- **No container restart while the session worked overnight.** A third restart came at 05:00 UTC on 29 October, while the session sat idle with nothing running. It lost nothing.
- **BigCommerce and WooCommerce (05:00 to 06:40 UTC; [`method-report.md`](studies/subjects/S-02/method-report.md), section 16):** the founder's local agent pushed them (other-product-class at `3f2438f3`). Gap-closing read the ten gaps that could change a decision: 2 answered, 7 narrowed, 1 left ([`gap-assessment.tsv`](studies/subjects/S-02/gap-assessment.tsv)). Phase B placed the 43 statements, and phase C ran again on the 20 points they touched. No decision changed. S-05's question on the tax on Sharrwah's fees takes five options, and Avalara's item is now bound per market: 143 founder items, 85 asked and 58 moved. The round cost 45.5 million.
- **WooPayments with an account (10:45 to 11:15 UTC):** the founder's local agent pushed test and live WooPayments accounts (other-product-class at `0d79b794`). They qualify D2's confirmed fact: an account's country can't change, and a move makes a new account. D2's recommendation stands, and only its wording changed. G09 is answered and G10 narrowed into G13, for S-03. The round cost 10.5 million.

**Earlier:**
- **Phase B's first pass is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 7): 73 variation points, each with a row for every platform, 671 rows, in [`variation-points.tsv`](studies/subjects/S-02/variation-points.tsv) and [`variants.tsv`](studies/subjects/S-02/variants.tsv). The full check gives no error.
- **The absence audit is complete** (section 8): 24 claims; 19 confirmed, 3 partly contradicted, 2 contradicted; 122 statements added. Two capture requests are narrowed ([H-002](handoffs/H-002-observed-sa-onboarding-countries.md), [H-007](handoffs/H-007-observed-sh-store-country-sign-up.md)), and three tools fixed to see held evidence they had missed.
- **Gap-closing (phase A2) is complete** ([`method-report.md`](studies/subjects/S-02/method-report.md), section 9; [`a2-parts.tsv`](studies/subjects/S-02/a2-parts.tsv)): 22 parts, 121 rows, 118 of them given statements and 83 with no gap left; 1,165 statements; 337 million. Its live pages are captured, and every quote is found; twelve are ruled on after review. 49 gaps remain: 15 for the local agent, in H-008 (new) and H-002 and H-005 (extended); 34 for the founder.
- **The render fault:** the browser in this session failed some sites' scripts, so BigCommerce's Help Center and Zid's sites rendered empty or as an error text; agents read zid.eg's Terms from a source that held the Saudi Terms. The tools now fetch each request outside the browser, open what a click shows, and tell a page's source from what it shows. 32 pages are held again as they render; Zid's audit of G03 was redone (for Egypt, the contract is with Zid Egypt, under Egyptian law). Every capture run now has its README.
- **Cost:** 1,638 million agent tokens at 11:15 UTC on 29 October, with the WooPayments round's 10.5. That is 1,582 at the end of the night, inside the projection of 1,500 to 1,600, and 45.5 for BigCommerce's and WooCommerce's round. The coordinating session's own tokens since S-02 began: 975 million ([the frame's budget](studies/subjects/S-02/frame.md#budget)).

**The intent's own work (29 October, from 11:15 UTC):**
- **The plan change** was read by an agent that made none of it ([`reports/plan-change-check.md`](reports/plan-change-check.md)): 26 findings, 15 of them must fix. All 15 are fixed, and 10 of the 11 optional ones; the eleventh, that S-02's re-status ran in the session that folded the change, is said to the founder.
- **S-02's register** is re-statused under the intent: its nine decisions and five constraints are engineering's rulings, listed for the founder's veto; E5 is ruled. [`reports/S-02.md`](reports/S-02.md) is replaced by [`reports/intent-review.md`](reports/intent-review.md).
- **Cost:** agents 19.0 million (the extent brief's inspection 4.2, the plan-change reading 9.6, the register's re-status 5.2); the coordinating session 64.5 million. The coordinating session's own tokens since S-02 began: 1,052 million.
- **PR #8** (S-02 and the intent) is ready to merge on the founder's word. The work continues on the same branch. Once PR #8 is merged, the branch restarts from `main` and Stage 4A goes in a new pull request.

**Stage 4A, in the fresh coordinating session (from 23:41 UTC on 29 October):**
- **The evidence is set up** as "To resume" says: observed-sh and observed-sa cloned since 5 October, with `b46731d0` and `145f137` present; other-product-class cloned whole from the founder's repository, at `0d79b794`, so the mirror branch is no longer needed here (said to the founder); the WooCommerce release checked against its sha256 and unpacked. `method/check_surface.py` exits 0.
- **The orientation page** is rebuilt for the intent and the work's place now, and published to the same URL (version 4); then updated for the founder's change of 30 October, folded at `7ad5cfda` by the session that folded the intent (version 5: GM brings the architecture plan for the founder's go, and line (3) is out). Its 241 links resolve at their commits, and its 41 quotes are found on their pinned lines (`method/check_report.py`, on a markdown rendering of the page).
- **The brief's inspection** ([`inspection-B.md`](studies/class-model/inspection-B.md)): 19 findings, 13 must fix. The coordinator re-ran its counts, which all hold, and took all 19. The brief is rewritten:
  - **a scope step** first: every concern of the five platforms in one domain (`studies/class-model/scope.tsv`);
  - **per domain:** the anchor, then the mapping parts onto the model so far, then a back-fill;
  - **per-statement evidence,** with fixed tokens, keys and placement tests;
  - **rulings** on Q1's unclear candidates.
  Two scripts go with it: `method/class_slice.py`, which prints what a part reads, and `method/check_class_part.py`, which checks a part and derives each cell's places, scopes and gaps. The same inspector is re-inspecting the rewrite before anything runs.
- **The re-inspection** (same file, "Re-inspection (30 October)"): 17 of the 19 findings resolved, 16 new (R1 to R16). The coordinator fixed the seven it set before the dry run, and four of those it set before the full run (R3, R6, R7, R13), and tested each fix on the inspector's own fixtures. Open before the full run: R10, splitting domain C's anchor by area.
- **Running now:** the scope part (every concern to one domain, `studies/class-model/scope.tsv`), and the inspection of the dry run's review brief (`studies/class-model/briefs/R-dry-run.md`). `method/class_kinds.py` computes each capability's count and kind from the parts' cells.
- **Cost so far:** the inspection 19.8 million agent tokens and the re-inspection 21.7 million, so 41.5 million of the extent's 250 million.

**Next:**
1. **A fresh coordinating session** runs Stage 4A (step 1.1 done; 1.2 under way). It reads observed-sh, observed-sa and other-product-class from their own repositories, and runs:
   1. the orientation page, updated to the founder's intent and checked for its links and quotes, since the frame has changed (`PLAN.md`, section 9);
   2. the inspection of `B-extent.md`, which changed after its last inspection; then the anchor's dry run on catalogue and inventory, with WooCommerce mapped onto it;
   3. the review of its output, which checks every placement against all of Q1's statements;
   4. the conventions and a checker, with the architecture plan's first part, what architecture needs to know, drafted alongside so the extent records it (`PLAN.md`, Stage 4A);
   5. the other domains and platforms; the merge, with each capability's kind and count, and S-01's and S-02's variation points landed on the model;
   6. Q3's check for what the model misses, then an independent review of the whole extent;
   7. the architecture plan finished (`architecture/plan.md`), and reviewed by an agent that made none of it;
   8. the extent's report and the architecture plan, with the orientation page updated before they reach the founder at GM.
2. **On the founder's go on the architecture plan:** architecture and the model's detail, in the order the plan sets, beside the subjects.

**For later:** "depth over speed" isn't decided. It was the coordinator's reading, not the founder's decision, and it comes back when a second market is near (`founder-messages/2026-10-29-intent-handoff.md`).

**To resume:** read `PLAN.md`, this file and `founder-decisions.tsv`. A fresh container first sets up the evidence `CLAUDE.md` names, read-only:
- **observed-sh and observed-sa,** each added to the session and cloned at `/home/user/observed-sh` and `/home/user/observed-sa` with its history since 5 October 2026 (`git clone --shallow-since=2026-10-05`). The checkers read evidence at the commits the records cite, back to observed-sh `b46731d0` and observed-sa `145f137`, both of 9 October.
- **other-product-class,** added to the session and cloned whole at `/home/user/other-product-class`, with the fallback `CLAUDE.md` gives.
- **The WooCommerce release:** `https://downloads.wordpress.org/plugin/woocommerce.11.2.1.zip`, checked against `evidence/product-class/woocommerce-11.2.1/woocommerce.11.2.1.zip.sha256` and unpacked at `/home/user/woocommerce-release/11.2.1`. The scripts read `/home/user/woocommerce-release/11.2.1/woocommerce`.
