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
- **observed-sh's 70 fetch archives** weren't in git at Stage 0. They landed later the same day, at `36a6319e`.

**Running: Stage 1, Yemen's axes and cases.**
- **First run: stopped by its brief.** It hit the cap on axes after reading 23 of 262 items, and never reached the other runs or the founder's pages. It is kept in `studies/yemen-cases/first-run-stopped/` as a record.
- **The brief is reworked** into two passes:
  - every source is read first, recording conditions at the size of an act or availability;
  - axes come after.

  The cap is now a stop for review. The change is recorded in `PLAN.md` section 11. A focused inspection found 7 must-fix items, all fixed.
- **Pass 1 is split across six agents by part** (A to F), so that every source is read. It started on 12 October 2026 at commit `9d0de52`.
- **Next:**
  - join the parts' files into `conditions.tsv` and `citations.tsv`;
  - pass 2, one agent: axes, constants, cases;
  - the checker;
  - an independent review;
  - compare with Q2's example axes.

**Running: Stage 2, the pilot (S-01).**
- **Briefs:** `studies/subjects/S-01/briefs/`.
  - Brief A was inspected three times, with all findings fixed.
  - Briefs B to F and A2 were inspected twice. A third check follows before B runs.
  - The method fixes this needed are recorded in `PLAN.md` section 11.
- **Phase A started on 12 October 2026:** five agents, one per platform, each blind to the others.
- **Next:**
  - capture the URLs phase A cites;
  - check, with `kinds.tsv`;
  - B, A2, B's second pass, C;
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

**The usage limit stopped every running agent at about 09:50 UTC on 12 October 2026.** All ten were restarted at 10:10 UTC, each continuing from its files, as below. BigCommerce's phase A had already finished.

**Agents running when last checked (12 October 2026, 10:10 UTC):**
- **Pilot phase A:** four agents on `studies/subjects/S-01/briefs/A-one-platform.md`, each writing `studies/subjects/S-01/<platform>/`.
  - Salla and WooCommerce are finishing: checker and fixes.
  - Shopify and Zid are starting fresh, because nothing had been written.
  - BigCommerce is done.
- **Stage 1 pass 1:** six agents, parts A to F, on `studies/yemen-cases/brief.md`. Each writes `studies/yemen-cases/pass1/{conditions,citations,notes}-<part>.*`, using the commit `9d0de523f1852ebf7716f0da01b6b619edc5e8fc` in every `source`.

**To resume:**
1. Commit whatever files are on disk, as an unchecked checkpoint.
2. For each platform or part, run its checker:
   - for a platform: `python3 -I method/check_subject.py studies/subjects/S-01 OUT`, reading the lines for `<platform>/`;
   - for a part: `python3 -I method/check_yemen_cases.py studies/yemen-cases OUT --pass1 <part>`.
3. An agent whose final reply never came didn't finish. Start a new agent with the same prompt as before, adding: "Your files already hold part of the work. Read them, continue from where they stop, and don't redo rows already written."
4. Then go on from the "Next" lists above.
