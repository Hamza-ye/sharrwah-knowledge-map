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
  - **Pass 1 is done and joined**, 13 October 2026, 00:40 UTC. All six parts check clean: 2,532 conditions and 4,052 citations, every quote found. `method/join_pass1.py` wrote `conditions.tsv`, `citations.tsv` and `pass2/wordings.tsv` (870 condition wordings).
    - **Parts:** A 54 conditions, B 190, C 590, D 635, E 897, F 166. Each part's `pass1/notes-<part>.md` lists what it read and couldn't read.
    - **Coordinator errors put right:**
      - Part E restored the 206 quotes the three-digit cap had cut.
      - Part E read items 263 to 280, which no part held.
      - Six held items part B couldn't read were OCR'd, and part F read them.
    - **Dates to check in pass 2's review:** the undated sales tax booklet (F, item 066) takes 2020; the commercial register law "as amended" (F, item 041) takes 1991.
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
  - step 2a (one agent, `max`), then step 2b (four agents by range of groups, `high`), then `method/join_pass2.py` and the build;
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
- **A2 is done** for Salla, WooCommerce, Zid and BigCommerce, at `medium` effort. Shopify had no gap. The four platforms added 72 statements in all.
  - **A miss.** The founder pointed at Salla's help articles on payout settlement. One of them ("Salla Payments Kuwait payouts settlement") is held, but neither phase A nor A2 read it. Salla's A2 is re-running at `high`, with a sweep of every held help article in both languages that uses Salla's own words for the subject. This follows the effort policy's re-run rule.
  - **Captured:** the live pages A2 cites (run `20261013T003518Z-s01-a2-sources`). With them, all 1,209 quotes are found.
    - BigCommerce's Help Center pages render empty even in a browser.
    - The held index now counts an empty capture as held but not readable, so the reader must be extended there.
- **Claims of absence are audited** (step A3, `PLAN.md` section 11), after the founder's note: "agents need to pay attention to what they think isn't there".
  - `method/corpus_search.py` searches a platform's held corpora in every language they hold. Its first run found the UAE and Kuwait settlement articles held since Q1's capture of 10 October.
  - An agent that made none of the claims audits every gap and absence.
  - A "searched, not found" must show its corpus search. The checker enforces both.
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
- **Pilot A2, Salla's re-run: done** (`high`).
  - The sweep listed 597 held articles; 564 had never been cited.
  - It added S01-SA-137 to 177, all scoped by country or bank.
  - Who settles Salla Payments funds is still not stated, and the payment services agreement isn't held.
  - Kuwait's minimum payout differs between the English and Arabic articles. Both are recorded, unresolved.
- **Pilot A3, absence audits:** one agent per platform (`high`), none of whom made the claims. Shopify `a173380272d4ca839`, WooCommerce `a3328139ad72099a3`, Zid `a009ce5ff1f1df173`, BigCommerce `a8e8664707525d3d1`, Salla `a210a6231aa83e30e`.
- **Then:** phase B's agent `a9e10fcc19233f104` is resumed for the second pass.
- **Stage 1 pass 2, step 2a:** one agent (`a4a6021a9605c1efe`, `max`), writing `groups.tsv`, `places.tsv` and `notes.md` in `studies/yemen-cases/`. It is resumed later for step 2c.

**A scheduled check-in** (Routine `trig_01QJwaNYp764mJnJLh5n5ago`, every two hours at :09 UTC) wakes this session to resume agents a limit stopped. Delete it when no agent is running for long stretches, or when the founder asks.

**To resume:**
1. Commit whatever files are on disk, as an unchecked checkpoint.
2. An agent whose final reply never came didn't finish. Resume it by sending a message to its agent id: it continues from its own transcript. Tell it that the limit stopped it, that its files hold its work, and that it should check its last rows are complete and not redo rows already written.
3. If the id no longer resumes, start a new agent with the same prompt as before, adding: "Your files already hold part of the work. Read them, continue from where they stop, and don't redo rows already written."
4. To check a platform or part, run its checker:
   - for a platform: `python3 -I method/check_subject.py studies/subjects/S-01 OUT`, reading the lines for `<platform>/`;
   - for a part: `python3 -I method/check_yemen_cases.py studies/yemen-cases OUT --pass1 <part>`.
5. Then go on from the "Next" lists above.
