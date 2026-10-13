# State

Where the work is, kept by the coordinating session under `PLAN.md` section 9. Updated and committed at every checkpoint.

**Updated:** 12 October 2026, 18:55 UTC.

**Gate G0:** passed on 12 October 2026 (`founder-decisions.tsv`).

**Agents' effort** is set by step from 13 October 2026 (`PLAN.md` section 11):
- `max`: inspections, Stage 1's step 2a, and the pilot's B, C, D and F;
- `high`: step 2b;
- `medium`: reading and recording evidence, re-run at `high` where checks or review show gaps;
- `low`: one-off mechanical questions.

Agents started earlier keep their effort.

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
- **observed-sh's 70 fetch archives** weren't in git at Stage 0. They landed later the same day, at `36a6319e`.

**Running: Stage 1, Yemen's axes and cases.**
- **First run: stopped by its brief.** It hit the cap on axes after reading 23 of 262 items, and never reached the other runs or the founder's pages. It is kept in `studies/yemen-cases/first-run-stopped/` as a record.
- **The brief is reworked** into two passes:
  - every source is read first, recording conditions at the size of an act or availability;
  - axes come after.

  The cap is now a stop for review. The change is recorded in `PLAN.md` section 11. A focused inspection found 7 must-fix items, all fixed.
- **Pass 1 is split across six agents by part** (A to F), so that every source is read. It started on 12 October 2026 at commit `9d0de52`.
  - Part A is done: 54 conditions and 112 citations, every quote found.
  - Part B is done: 190 conditions and 420 citations, every quote found.
    - It read 61 of its 83 items.
    - Not readable:
      - centralbank.gov.ye (001–010, connection reset or 503);
      - saba.ye (011, 021–023, 035, 037, 061; 403);
      - scans whose OCR is part F's.
    - Six more were OCR'd on 12 October 2026 (`evidence/yemen/derived/README.md`), and part F has read them: three photographs of documents (016, 026, 030) and three PDFs with a shifted font encoding (041, 047, 066).
  - Part F is done, including those six: 166 conditions and 482 citations, every quote found.
    - It notes that the Aden and Sana'a central banks' texts both name their area "Republic of Yemen". Pass 2's authority rule keeps the two apart.
    - Two dates to check in pass 2's review:
      - the undated sales tax booklet (066) takes 2020, the latest amendment it names;
      - the commercial register law "as amended" (041) takes its 1991 decree date.
  - Part C is done: 590 conditions and 705 citations, every quote found. Six pages couldn't be fetched (005, 033, 092, 034, 035, 099).
  - Part D is done: 635 conditions and 999 citations, every quote found.
    - It read 96 of its 115 items. Its scanned PDFs' OCR is part F's.
    - It couldn't read 2, 15, 18–20, 24, 25, 28, 75 and 130 (404s, Cloudflare checks, TLS, maintenance).
    - It records US dollar and Saudi riyal exchange rates: a long series of states, so many cases.
  - Part E is done for items 132 to 262: 847 conditions and 995 citations, every quote found. Two problems were the coordinator's, and both are being put right:
    - **The cap.** The checker's three-digit ids capped a part at 999 citations. Part E trimmed 1,246 to fit, so details were lost. The checker now takes four-digit ids, and part E is restoring what it trimmed. Part D ends at exactly 999 by coincidence and lost nothing.
    - **The split.** Items 263 to 280 were in no part, because the run's numbering skips. Part E is reading them now.
- **Pass 2 is reworked before it runs**, given pass 1's size (`PLAN.md` section 11, brief's pass 2).
  - Its first inspection found 12 must-fix items, all fixed. The place model changed most:
    - places are scopes: an authority's area, a party's service, or a named area;
    - name variants are one place, but an ambiguous name never groups;
    - today's parts may overlap.
  - The build bugs it found are fixed, and `method/test_build_yemen_cases.py` now tests every rule.
  - The second inspection found 12 more, all fixed:
    - the `ended` state;
    - an across-Yemen state supersedes only when strictly later;
    - labels name the parties when they are what differs;
    - a body named without its seat groups only on a source;
    - `method/join_pass2.py` joins step 2b's files.
  - The third and last inspection found 7, all fixed. Among them, the join would have turned every across-Yemen state into `place not stated`. The method is ready to run.
  - Agents make the judgments: step 2a groups conditions and places, and step 2b labels states, several agents by range of groups.
  - `method/build_yemen_cases.py` applies the rules and writes axes, constants and cases.
  - The checker has `--groups` and `--states` modes and compares the build's output.
  - Part A's four notes on the brief are settled there:
    - a `held_at` that isn't a date is undated;
    - dates after the capture count as the capture date;
    - the "same role" conflict is settled by "states are alternatives";
    - the commit given in the agents' prompts is the one cited.
- **Next:**
  - when B to F finish: `python3 -I method/join_pass1.py studies/yemen-cases`;
  - step 2a (one agent), then step 2b (four agents by range of groups), then join the states and build;
  - the review stop if past 20 axes (`review-axes.md`), then cases;
  - step 2c, the checker, an independent review, and a comparison with Q2's example axes.

**Running: Stage 2, the pilot (S-01).**
- **Briefs:** `studies/subjects/S-01/briefs/`.
  - Brief A was inspected three times, with all findings fixed.
  - Briefs B to F and A2 were inspected twice. A third check follows before B runs.
  - The method fixes this needed are recorded in `PLAN.md` section 11.
- **Phase A is done** on all five platforms: 588 statements and 16 gaps. With every capture run, the checker finds all 1,125 quotes and reports no issues.
  - The pages phase A cites were captured in `evidence/product-class/runs/20261012T104936Z-s01-sources/` (130) and `20261012T190225Z-s01-sources-zid/` (1).
- **Briefs B, A2, C, D and F: third inspection done.** It found 14 must-fix items, all fixed. The main ones:
  - the matching words "same" and "agree" are defined;
  - "market, pattern" follows `PLAN.md` section 6 as written;
  - D marks only the cases that change an axis a variation point bears on (`bears-on.tsv`). Every other case carries today's mark.
- **Phase B's first pass is done** (agent `a9e10fcc19233f104`). The checker reports no issues.
  - 23 variation points: 10 under (a), 3 under (b) and 10 under (c).
  - 531 variants: 491 answers, 2 absent, 28 gaps and 10 not covered.
  - Its notes led to brief changes:
    - A2 also takes the arrangements a platform leaves unanswered: who settles Salla Payments funds, and BigCommerce's payouts beyond BitPay;
    - B matches against another platform's statement;
    - B may rest an answer on its own translation, marked as its own.
- **A2 started** on 13 October 2026 at `medium` effort, for Salla, WooCommerce, Zid and BigCommerce. Shopify has no gap.
- **Next:**
  - test the checker's step 2 (marks) on D's first rows before D runs on;
  - B, A2, capture and kinds again, B's second pass, C;
  - D, after Stage 1;
  - the entry (Q3's rows are no longer a pilot step: they are reconciled once, at close-out, per `PLAN.md` section 11);
  - F;
  - the method report;
  - G1.

**Evidence heads:**
- **observed-sa `4ca2e896`.** It now holds items 6, 7, 9, 10 and 11:
  - the help centre's 2,938 articles as text;
  - the eleven pages about Salla's terms as text;
  - the fetch archives in git, except five over GitHub's size limit.
- **observed-sh `36a6319e`.** Its 70 fetch archives, mostly online docs, landed on 12 October. The held index reads them. Re-running `method/q1_held_check.py` changed no gap, because none had been routed to the founder for a page they hold. The Shopify phase A agent was told it may cite them.
- **The map's citations** are at observed-sa `145f137` and observed-sh `b46731d0` / `e49840729`.

**Q3's rows:** both sets, by the founder's answer (`founder-decisions.tsv`).
- The 81 payment rows are in `register/pay-questions.tsv`.
- The Knowledge Map's 179 questions are in `register/km-questions.tsv`, copied from the founder's artifact with `KM-` ids.
- `register/README.md` says what the rows are and why they need care.

## If the work was interrupted

**The usage limit has stopped the running agents three times on 12 October 2026:**
- at about 09:50 UTC, when all ten restarted at 10:10 UTC as new agents continuing from their files;
- at about 10:55 UTC, until 15:00 UTC. The six still running were resumed at 18:53 UTC, each from its own transcript;
- at about 20:10 UTC, until 23:50 UTC. Part E, phase B and the third inspection were resumed at 23:58 UTC, each from its own transcript.

**Agents running when last checked (12 October 2026, 23:58 UTC):**
- **Pilot A2:** one agent per platform on `studies/subjects/S-01/briefs/A2-close-gaps.md`, adding to `studies/subjects/S-01/<platform>/` and writing its `a2.tsv`. Agents: Salla `a92dbea8578aa9b2b`, WooCommerce `ab2f2d0581429efb0`, Zid `a5878c46f612c28d8`, BigCommerce `a3036ef0ce778c6b2`. Phase B's agent `a9e10fcc19233f104` is resumed for the second pass after A2.
- **Stage 1 pass 1:** part E, restoring trimmed quotes and reading items 263–280. Parts A to D and F are done.
  - Agent: E `aa722ff96ec8f64a4`.
  - Brief: `studies/yemen-cases/brief.md`. Each writes `studies/yemen-cases/pass1/{conditions,citations,notes}-<part>.*`, using the commit `9d0de523f1852ebf7716f0da01b6b619edc5e8fc` in every `source`.

**A scheduled check-in** (Routine `trig_01QJwaNYp764mJnJLh5n5ago`, every two hours at :09 UTC) wakes this session to resume agents a limit stopped. Delete it when no agent is running for long stretches, or when the founder asks.

**To resume:**
1. Commit whatever files are on disk, as an unchecked checkpoint.
2. An agent whose final reply never came didn't finish. Resume it by sending a message to its agent id: it continues from its own transcript. Tell it that the limit stopped it, that its files hold its work, and that it should check its last rows are complete and not redo rows already written.
3. If the id no longer resumes, start a new agent with the same prompt as before, adding: "Your files already hold part of the work. Read them, continue from where they stop, and don't redo rows already written."
4. To check a platform or part, run its checker:
   - for a platform: `python3 -I method/check_subject.py studies/subjects/S-01 OUT`, reading the lines for `<platform>/`;
   - for a part: `python3 -I method/check_yemen_cases.py studies/yemen-cases OUT --pass1 <part>`.
5. Then go on from the "Next" lists above.
