# State

Where the work is, kept by the coordinating session under `PLAN.md` section 9. Updated and committed at every checkpoint.

**Updated:** 17 October 2026, 12:29 UTC.

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
- **Step 2a is done**, 13 October 2026, 02:00 UTC. It made 561 groups over the 2,532 rows, 213 of them joining rows from more than one part. It listed 346 places, 148 grouped with another (37 by rule, 45 as variants, 66 on a source), so the rows fall in 198 places.
  - Its notes showed two checker faults, both fixed:
    - groupings may chain, each link with its own basis, and the rows take the place the chain ends at;
    - a seat named in either language is one seat.
  - `method/join_pass2.py` follows a chain through every link and refuses a cycle. The build reads places only from the joined `states.tsv`.
  - Its agent then added the chains and translated names it had held back: 155 of the 346 places are grouped, so the rows fall in 191. The checker reports no issues.
- **Step 2b is done,** 17 October 2026, by four agents at `high`, one per range of groups.
  - All 2,532 rows are labelled: 2,505 `held`, 12 `ended` and 15 `proposed`. Each range checks clean.
  - The ranges added 59 places, which make 46 once joined.
  - **A ruling, now in the brief:** a forecast or projection of a future value is `proposed`. My first wording also took in estimates. It was narrowed: an estimate of a present value says the state holds. The ranges put back the rows they had moved.
- **The first join and a trial build:** 253 axes and 308 constants.
  - 28 axes have a disputed part, 34 places in all.
  - The step 2b agents traced these to states that can hold together:
    - one state at different detail, such as a rate against a buying and selling pair that includes it;
    - lists that add up, such as a party's pages captured on one day;
    - two rules in one group.

    These break rule 2 (states are alternatives). The review stop returns them to step 2a, as the brief provides.
- **Next:**
  - step 2c grouped the places step 2b added; the join and build stop for review at 253 axes, 28 with a disputed part (commit `40a11e7`);
  - **the first axes review returned 128 of 253 groups to step 2a** (142 returns: rule 2 96, rule 1 19, rule 4 14, the label rule 11, rule 5 2). It is recorded in `review-axes.md`, with the drafts in `review/`. Most states add up rather than replace each other, so today dropped facts that still hold, such as earlier bans and designations. Two rulings from rule 2 are in the brief and `PLAN.md` section 11;
  - **step 2a's fix round is done** (commit `71ab056`). 86 groups split into 167 new conditions (YG-562 to 728), and 157 labels and 25 places changed. The returns it didn't follow are reasoned in `notes.md`.
    - Now 728 groups, 241 axes and 487 constants. Disputed parts of today fall from 34 to 11.
    - Checked clean. `axes.tsv` has sha256 `0b7ef7ad…03aa`.
    - A trial build past the review gives 379 cases: today's, 27 `in force` and 351 `occurred`. Most change one axis.
  - **the second review returned 38 rows on 37 axes** (21 label, 11 rule 2, 3 rule 1, 2 rule 4, 1 rule 5). Every first-round return was followed or reasoned. Two disputed parts that no source makes are among them: Cash's hours and the wallet counts of 11 July 2026. Recorded in `review-axes.md`;
  - **step 2a's second fix round is done** (commit `f3ed2df`): 739 groups, 227 axes, 512 constants. `axes.tsv` has sha256 `02850db5…2375`. The 10 disputed parts in today are each made by their sources, or a tie under the precision rule. Checked clean;
  - **the third review let the axes through** (commit `42c392c`). It returned one label, which the coordinator checked once fixed. `review-axes.md` names `axes.tsv` sha256 `47b5c642…c735` in full;
  - **the build wrote 350 cases:** today's, 23 `in force` and 326 `occurred`. 227 axes and 512 constants. 21 part D citations with an empty `source_date` take "no date", as the others do;
  - **step 2c is done** (commit `e894f8d`). `unknowns.tsv` has 5 rows: 4 `agent`, and 1 `founder` (YA-40, the anti-usury law; saba.ye answers 403 from outside Yemen). The full check is clean, with all 4,052 quotes found;
  - **Stage 1's independent review is running** (`max`). It writes `review-independent.md`, including the comparison with Q2's example axes;
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
  - **A miss.** The founder pointed at Salla's help articles on payout settlement. One of them ("Salla Payments Kuwait payouts settlement") is held, but neither phase A nor A2 read it. Salla's A2 was re-run at `high`, with a sweep of every held help article in both languages that uses Salla's own words for the subject. This follows the effort policy's re-run rule.
    - The sweep listed 597 held articles, of which 564 had never been cited. It added S01-SA-137 to 177, all scoped by country or bank.
    - Who settles Salla Payments funds is still not stated, and the payment services agreement isn't held.
    - Kuwait's minimum payout differs between the English and Arabic articles. Both are recorded, unresolved.
  - **Captured:** the live pages A2 cites (run `20261013T003518Z-s01-a2-sources`). With them, all 1,209 quotes are found.
    - BigCommerce's Help Center pages render empty even in a browser.
    - The held index now counts an empty capture as held but not readable, so the reader must be extended there.
- **Claims of absence are audited** (step A3, `PLAN.md` section 11), after the founder's note: "agents need to pay attention to what they think isn't there".
  - `method/corpus_search.py` searches a platform's held corpora in every language they hold. Its first run found the UAE and Kuwait settlement articles held since Q1's capture of 10 October.
  - An agent that made none of the claims audits every gap and absence.
  - A "searched, not found" must show its corpus search. The checker enforces both.
- **A3 is done for all five platforms**, at `high`.
  - Results: Shopify 2 confirmed; WooCommerce 2 confirmed and 1 partly contradicted; Zid 23 confirmed; BigCommerce 9 confirmed and 2 contradicted; Salla 4 confirmed and 3 partly contradicted.
  - A2 and A3 together added 157 statements (588 to 745). Every quote is found (1,390).
  - `corpus_search.py` also reads raw pages (zid.sa keeps its content there) and the fetch archives, through a text cache in `~/.cache/sharrwah-corpus`.
  - The Paylink lead (from the founder's search) isn't supported by held evidence: the held Paylink posts tie its licence to no Salla Payments funds.
- **For the founder:** `evidence/product-class/to-save-for-s01.md`, raised in chat on 13 October 2026. It asks for:
  - eight BigCommerce Help Center articles (HTTP 400 to automated browsers): **done**;
  - Salla's payment services contract;
  - Zid Pay's provider and the wallet's bank.

  Until they're saved, those gaps stand as recorded.
- **BigCommerce's Help Center is held,** captured by the founder from their own machine on 13 October 2026 with `method/capture/run.sh`. It holds 51 of 52 addresses, including the pilot's eight articles: run `20261013T053949Z-s01-bigcommerce-help-founder-machine`, merged on 17 October.
  - It made 21 BigCommerce gaps' pages readable, and the checker reported 42 routes to the founder for pages now held.
  - The checker now counts such a page as read once A2 or A3 names its held copy in `read`. An address alone doesn't count, because BigCommerce's first A2 listed the addresses it was refused.
  - A "page not read" gap left open after every page it waited on was read is an error.
  - **BigCommerce's A2 re-run on the capture is done** (`medium`). It added S01-BC-066 to 124, from items 1 to 8 and 40.
    - G01, G04, G06, G07 and G13 close in full, and eight more gaps in part. G24 to G40 record what is still not stated.
    - BigCommerce Payments holds funds in "a brand new PayPal platform account" that "will handle all settlement". A new account's initial payments are held up to 21 days. The service is offered in the UK as well as the US, which contradicts S01-BC-028 ("only US").
    - The checker reports no error in BigCommerce's files, and all 1,521 quotes are found.
  - **A3 audited its 14 new claims of absence** (`high`): 11 confirmed, 3 partly contradicted (G25, G28, G38). It added S01-BC-125 to 128, all from held captures.
    - BigCommerce's terms name no PayPal agreement as binding, so none was read.
    - The Master Services Agreement says no agency is created by it or by using the Services (S01-BC-128). The first audit of G08, on the same question, missed it, so the coordinator corrected G08's row to `partly contradicted` and said so in its note.
    - It found two faults in `corpus_search.py`, both fixed:
      - an address held more than once showed its first copy, so an empty older capture hid the founder's full one;
      - the founder's saves (`blocked-evidence-founder/<platform>/`) weren't searched. They are now, including PDFs through `pdftotext`.
  - **Phase B's follow-up for BigCommerce is done.** BigCommerce's rows go from 46 to 88: 72 answers and 16 gaps.
    - All platforms now have 653 variants: 616 answers, 2 `absent` and 35 `gap`.
    - Four BigCommerce rows changed from `gap` to an answer, where A2 left the variation point no gap. They rest on a general statement, S01-BC-088: "You will control and direct funds in your merchant account with your merchant service provider". Its scope is general, so C's scope rule applies.
    - The checker's one review line is the 11 statements that fit no variation point. All 1,528 quotes are found.
- **Phase C's first run is done** (`max`), at commit `34a32b9`.
  - Step 0: the subject is about the product.
  - Causes: vendor choice 14, market named rule 4, unknown 3, maturity 1, no difference 1. 12 founder items.
  - Its notes showed why vendor choice dominated. The rule for "same" named the merchant as one party everywhere, but each platform's own name as a different party, so two platforms that each name themselves "differed".
  - The brief now counts the merchant, the buyer and the platform itself (its name, payment product or company) as one party on every platform. "Names a law" means a particular law or regulator. Both are marked as the coordinator's own and recorded in `PLAN.md` section 11.
  - **Phase C's second run, under the amended rule, is done** (checkpoint `803b19f`, verified at `3815d46`). It moved the readings of nine variation points, but no cause, letter, rule or founder item. The differences come from third parties only some platforms name (Global-e, BitPay, Tamara, Trendyol), or from gaps. So the 12 founder items stand on the evidence:
    - 01 who holds the funds before payout; 02 who settles; 03 who sends payouts; 04 who collects;
    - 06 whether to act as the merchant's agent; 09 who deducts; 11 which accounts merchants hold;
    - 15 one payout timing of its own, or each provider's settlement time; 19 deduct before payout, or bill separately;
    - 20 what happens to held funds at termination; 22 who pays up front for installments; 23 which payout currency.
  - **They reach the founder in the register entry** (pilot step 3), after D marks the subject against Yemen's cases. Each comes with its evidence, options and the coordinator's recommendation (`PLAN.md` section 4).
- **Next:**
  - test the checker's step 2 (marks) on D's first rows before D runs on;
  - **B's second pass is done.** It placed the statements A2 and A3 added, up to S01-BC-065 for BigCommerce.
    - There are 611 variants: 571 answers, 2 `absent`, 38 `gap` and none `not covered`.
    - It rechecked the first pass's comparisons against another platform's statement, and 106 rows changed basis.
    - Ten statements fit no variation point. All are peripheral, such as where to track cash-on-delivery amounts or a dashboard's name, so no variation point is missing.
    - Its notes on the brief: different words in one language, empty definitions, partly contradicted gaps, and the scope separator. They go to the method report. The B brief's reading list now names `absence-audit.tsv`.
  - C is done; its 12 founder items wait for the register entry, after D;
  - **D is running** (`max`), in parallel with Stage 1's independent review. It stops after `bears-on.tsv` and YC-00's marks, so the coordinator can test the checker's step 2 on its first rows;
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

**The usage limit has stopped the running agents five times:**
- at about 09:50 UTC, when all ten restarted at 10:10 UTC as new agents continuing from their files;
- at about 10:55 UTC, until 15:00 UTC. The six still running were resumed at 18:53 UTC, each from its own transcript;
- at about 20:10 UTC, until 23:50 UTC. Part E, phase B and the third inspection were resumed at 23:58 UTC, each from its own transcript;
- on 13 October 2026 at about 02:05 UTC, the weekly limit, until 17 October 05:00 UTC. The check-in below fired every two hours but could do nothing until the reset. Phase B's second pass and step 2a were resumed at 06:20 UTC, each from its own transcript;
- on 17 October 2026 at about 08:30 UTC, the session limit, until 11:00 UTC. It stopped both second axes reviewers as they started. They were resumed at 11:03 UTC, each from its own transcript.

**Agents running when last checked (17 October 2026, 06:40 UTC):**
- **Pilot phase C's agent,** `adc0057894ed0a4d9`, is done.
- **Pilot phase B's agent,** `a9e10fcc19233f104`, is done, and can be resumed for the pilot's variation points.
- **Stage 1, the independent review:** agent `a0755eeb78b50b2c8` (`max`), writing `studies/yemen-cases/review-independent.md`.
- **Pilot phase D:** agent `a279f7e700e54e76b` (`max`), writing `bears-on.tsv`, `yemen-marks.tsv` and `notes-d.md` in `studies/subjects/S-01/`. It stops at a checkpoint after YC-00's marks.
- **Done, and resumable:** Stage 1 step 2a `a4a6021a9605c1efe`; the axes reviewers `ac1ab6f9db5c9443e` and `a9826e37d14145ed2`.
- **Stage 1 step 2b's agents,** done. They can be resumed for their ranges: range 1 `a2697a25622282d23`, range 2 `afd16cf2925a43e1f`, range 3 `a1c52ff4913f2ba6c`, range 4 `abfbdaaac8cd9a9b3`.

**A scheduled check-in** (Routine `trig_01QJwaNYp764mJnJLh5n5ago`, every two hours at :09 UTC) wakes this session to resume agents a limit stopped. Delete it when no agent is running for long stretches, or when the founder asks.

**To resume:**
1. Commit whatever files are on disk, as an unchecked checkpoint.
2. An agent whose final reply never came didn't finish. Resume it by sending a message to its agent id: it continues from its own transcript. Tell it that the limit stopped it, that its files hold its work, and that it should check its last rows are complete and not redo rows already written.
3. If the id no longer resumes, start a new agent with the same prompt as before, adding: "Your files already hold part of the work. Read them, continue from where they stop, and don't redo rows already written."
4. To check a platform or part, run its checker:
   - for a platform: `python3 -I method/check_subject.py studies/subjects/S-01 OUT`, reading the lines for `<platform>/`;
   - for a part: `python3 -I method/check_yemen_cases.py studies/yemen-cases OUT --pass1 <part>`.
5. Then go on from the "Next" lists above.
