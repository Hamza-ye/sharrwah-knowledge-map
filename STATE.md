# State

Where the work is, kept by the coordinating session under `PLAN.md` section 9. Updated and committed at every checkpoint.

**Updated:** 19 October 2026, 15:45 UTC.

**Gate G0:** passed on 12 October 2026 (`founder-decisions.tsv`).

**Gate G1:** answered on 18 October 2026: **re-frame.** The founder's message is `founder-messages/2026-10-18-g1-answer.md`. Its section A is recorded in `founder-decisions.tsv` as four decisions:
- plain business words in everything for the founder, several decisions per message, and method rulings listed one plain line each;
- the pilot's Decisions 1 to 14 deferred: they stay open and bind nothing, not even per market;
- the guard: no arrangement that holds sellers' money through Sharrwah goes live without the founder's decision;
- nothing runs before the founder's go on the plan change.

**Step R0, the plan change: done on 18 October 2026, with the founder's go.**
- **observed-sh** was pulled to `c8b5fbee2`: Shopify's Help Center in English and Arabic, organized as Shopify organizes it.
- **The drafts** (commit `103eeb9`), in `studies/proposals/`:
  - `plan-change.md`: the section 11 entry, and the sections it rewrites;
  - `questions.md`: section B's eight items as neutral questions;
  - `briefs/R1-areas-one-platform.md` and `briefs/R1-areas-review.md`, the first step's briefs;
  - `sizing.md`: about 1.49 billion agent tokens if the sample meets the founder's bar, with about 0.43 billion of the coordinator's own on top;
  - `areas/extract-<platform>.md`, written by `method/areas_extract.py`, and `method/check_areas.py` for the first step's runs.
- **The independent check of the drafts** (`briefs/R0-check-of-the-draft.md`): agent `aaa90803d4fe66dba`, at `max`. Its findings, `studies/proposals/check-of-the-draft.md` (commit `4b4ccbe`): 40, 19 of them must fix. It cost 17 million tokens, by its transcript.
- **The token count is corrected** (commit `e75ce9a`). The coordinator's counts took each API request once per line of its transcript, and a request is written over several lines. So every earlier figure was roughly doubled.
  - Counted once per request (`method/count_tokens.py`), the pilot's agents processed about 1.03 billion tokens, not 2.1 billion. Phases A and A2 come to about 0.52 million per statement, not 1.1 million.
  - Section 12 of the method report is corrected. The founder's budget and bar, set from the old figures, are about 1.0 billion and 0.26 million in this count.
  - A week's limit is about 2.8 billion in this count, and about 43 percent of this week's was used by 20:00 UTC on 18 October.
- **The fixes** (commits `11e4e1d`, `e75ce9a`, `d61c08f`, `58edb02`):
  - the first step's scripts, rewritten or new: `areas_extract.py`, `check_areas.py`, `place_entries.py`;
  - both R1 briefs;
  - the questions re-worded;
  - the plan change rewritten in full;
  - the sizing re-counted. It now comes to about 1.22 billion agent tokens at the founder's bar, about a fifth over the pilot, with cuts offered.
- **The re-check of the fixes** (`check-of-the-draft.md`, `## Re-check`, commit `fc98f4b`): 17 of the 19 must-fix findings fixed and 2 partly. Four small new must-fix findings, 41 to 44, and five optional ones.
  - The re-check confirmed the recount from the agents' own transcripts.
  - The coordinator fixed 41 to 48 (commit `2ab910c`), and re-ran the re-check's tests: 52 behave as expected. The one other case was written for the old numbering of the cuts, and passes once its cut is named.
  - The check and re-check together cost 39 million tokens.
- **The summary for the founder** (`studies/proposals/summary-for-the-founder.md`) went in chat at 20:35 UTC.
- **The founder's go, 18 October 2026** (`founder-messages/2026-10-18-go-on-the-plan-change.md`; `founder-decisions.tsv`). Go, with five changes:
  - the sample measures and doesn't stop the work;
  - the budget is 2 billion agent tokens, in the corrected count, with the coordinator's work on top;
  - a step past its expected cost doesn't stop: the coordinator re-sizes the rest and tells the founder in its next message. The work stops only if the re-sized whole would pass 2 billion;
  - checks cover everything a proposal cites;
  - the first build's design starts from the marked areas list as Sharrwah's whole extent, and reads open-source platforms (Saleor, Medusa, Vendure) for structure only.

  Q3's rows are checked at the end. No cuts. The coordinator didn't push back.
- **`PLAN.md` holds the change** (commit `7fec7f0`): the status line and sections 1 to 9 rewritten, Stages 0 to 2 kept as a record, and the dated entry in section 11. Stage 1's fixes "before Stage 4" are replaced, as section 6 says.
- **R0's measured cost** (`studies/proposals/costs.tsv`): agents 39.4 million (expected 39), coordinator 65.5 million (expected 80).
- **The sizing at the go** (`studies/proposals/sizing.md`): about 1.5 billion agent tokens at a planning rate of 0.4 million per new statement, 1.35 to 2.0 billion by what the sample measures. With the coordinator's work, about 62 percent of a week's limit. It will pass this week's limit before the reset on 24 October at 05:00 UTC.

**Running: step R1, the platforms' broad areas** (`PLAN.md` section 4).
- **Expected cost:** agents 122 million (the five platform runs 69 with re-runs; the review 53 with its brief's check and re-checks); coordinator 30 million.
- **The five platform runs are done** (commits `9b359b2`, `66c457a`, `60367cd`): Shopify 29 areas, Salla 28, WooCommerce 28, Zid 29, BigCommerce 30. Every concern is placed, and `check_areas.py` reports no problems on all five.
  - They cost 15.2 million in all, follow-ups included (`costs.tsv`), against 69 sized.
  - The checker now accepts a platform's group headings, out-of-scope entries and bilingual halves as its own names. Zid and Salla then added their headings, and Salla rests four more groupings on them. Shopify and WooCommerce found no heading that names a whole group.
- **The corpus search reads Shopify's Help Center** held in observed-sh (English Markdown and Arabic content), each page under its address (commit `66c457a`). Before, it reached the Help Center only through older fetch archives.
- **The merged list** (commit `c7ce5db`):
  - `areas.tsv`: 29 merged areas over the 144 platform areas, each tied to the questions that draw on it. Products and inventory, and analytics, draw on none, each with its reason;
  - `depth.tsv`: 20 in-depth pairs, each with why and the concerns it cites;
  - `areas.md`: the founder's version.

  `check_areas.py merged` reports no problems.
- **The sample**, by the plan's rule (the in-depth run whose candidate statements are nearest the median, the lower on a tie): **Q2 on Salla**, with 543 candidate statements. The median is 572.5, and Q2 on Salla ties with Q4 on Salla at 29.5 from it.
- **R2's tools and briefs** (commit `681df43`):
  - `copy_statements.py` copies in two phases. Tying whole areas copies over 1,000 statements for several runs, so the recording run marks the candidate concerns first;
  - `check_proposals.py records` is the checker for record folders;
  - `briefs/R3-recording.md` and `briefs/R3-checking.md`, the briefs for the runs.
- **The review brief's check** (`checks/R1-review-brief-check.md`): 13 findings, 3 must fix, all fixed (commit `7cc6c78`). Agents now get the questions from `questions-for-agents.md`, written by `method/agent_questions.py` without the founder's items and expectations. PLAN.md records the method fixes of R1 in section 11.
- **The R3 briefs' check** (`checks/R3-briefs-check.md`, commit `271f105`): 32 findings, 21 must fix. It cost 14.7 million tokens (`costs.tsv`).
- **Its fixes** (commits `e66cee8` for the tools, `d8c2410` for the briefs and `PLAN.md`):
  - `copy_statements.py`: each copy's id is its line in its source (K statements, G gaps; for Q5 the pilot's P, H and A), so ids never move; `show` prints a concern's statements for judging it; the copy writes two views to read instead of the copies;
  - `check_proposals.py`: copies compared byte for byte with their source lines, and their ids with their lines; a deleted candidate reported; `bears_on` within the question's sentences; every account point cites an id; `--check` for checking runs;
  - `corpus_search.py`: WooCommerce's release files searched; `--with` for required terms; `--max` caps a whole corpus;
  - `help_map.py`, new: the Shopify and Salla help maps one part at a time, and one page or article with the line to cite it by;
  - `agent_questions.py`: each question's sentences numbered;
  - both briefs rewritten; the optional findings 3, 12 to 14 and 16 to 18 taken too, and 4 and 15 in part;
  - `PLAN.md` section 11: a dated entry, with two narrowings of the plan (the contracts behind providers; the search behind a not-found) and live pages captured after each run.
- **The review of the areas list** (`areas/review.md`, commit `c613452`): 25 findings, 15 must fix. It cost 41.7 million tokens (`costs.tsv`).
- **Its fixes** (commit `2731962`; `PLAN.md` section 11, the last entry):
  - 34 areas: languages (A-30), currencies (A-31), gift cards, store credit and customer wallets (A-32), catalogs and price lists (A-33) and charity stores (A-34) added;
  - platform areas re-cut, each with its reason: the platforms' own payment services all in A-12, financing in A-13, WooCommerce's account in A-01, Zid's countries in A-16;
  - each question draws on the areas where the review found statements bearing on it, and Q8 on every area;
  - depth reasons corrected; Zid in depth for Q6 (21 in-depth runs, 19 checks); the pilot's statements offered to every question;
  - `check_areas.py merged` checks that each depth cite is reached by its question; `areas.md` shows every name.
- **The sample is now Q3 on Salla:** the same rule, applied to the revised list, gives a median of 875 candidate statements, and Q3 on Salla holds exactly 875.
- **The re-check of the areas list's fixes** (`areas/review-recheck.md`, 34.0 million tokens): 21 of the 25 findings fixed, all 15 must-fix among them; one new must-fix (A-15's heading), fixed with the optional ones (commit `529e48c`). Single concerns the re-check found outside their questions' areas are candidates through `areas/extra-candidates.tsv`; the pointers for the runs' starting messages are in `briefs/R3-starting-messages.md`.
- **Gate G2: the areas list went to the founder** at 23:03 UTC (`areas/message-for-the-founder.md`), with the method rulings since the summary and the steps past their cost: agents re-sized to about 1.54 billion, the coordinator to about 0.34 billion.
- **The sample, Q3 on Salla, is done** (commit `a00a865`): 72 new statements and 3 not-found rows, all from held material, and the checker reports no issues. It cost 18.7 million tokens: **0.26 million per new statement**, against the planning rate of 0.4.
- **Re-sized at the sample** (`sizing.md`, its last section): agents about 1.62 billion (221 measured), the coordinator about 0.33 billion, together about 1.95 billion. The founder hears it in the next message.

**Running: step R3, recording by question.** The in-depth runs' selections are written (commit `f7b6162`). They run in batches, at `medium`, each started from `briefs/R3-recording.md` with the pointers in `briefs/R3-starting-messages.md`.
- **All 21 in-depth runs are done** (commit `144e2b6`): 1,664 new statements, each record passing the checker with no issues, every cited live page captured in the language it was read in. They cost 267.7 million tokens, the sample included: about 0.16 million per new statement, and 12.7 million a run, against 390 million planned.
- **Recording is done** (commit `85fc690`): the 19 checking runs passed `--check` with no issues, and cost 186.3 million tokens with the three continued, about 9.8 million a run. R3's agents came to 462.2 million in all, the sample (R2) apart. Every live page a run read was captured in the language it was read in.
- **The founder's capture list** (`studies/proposals/capture-list.md`, by `method/capture_list.py`): 46 rows routed to the founder or to either, by platform, as pages to capture and questions to ask. Optional; the work doesn't wait for it.
- **R4 is prepared:** the digest of Stage 1 (`yemen-digest.md`, by `method/yemen_digest.py`), the id lookup (`method/record_ids.py`), the drafting brief (`briefs/R4-drafting.md`) and the checker's `drafts` mode.
- **The drafting brief's check** (`checks/R4-drafting-brief-check.md`, 14.2 million tokens): 18 findings, 8 must fix. All but one are fixed, in the brief and the checker; the coordinator adds the last (how far currencies can be set or changed) to Q7's proposal when finishing it. The rulings are in `PLAN.md` section 11, 19 October.
- **Stopped from 05:30 to about 15:00 UTC, by the founder's choice,** to talk before drafting.
- **The founder's answer, 19 October 2026** (`founder-messages/2026-10-19-areas-drafting-and-observed-evidence.md`; five rows in `founder-decisions.tsv`; `PLAN.md` section 11):
  - **G2: no marks.** All 34 areas stay in; when each part is built is decided in the design;
  - **the drafts' citing counts are a guide, not a limit:** the brief and the checker now say so (the checker counts them as notes);
  - **before drafting,** read observed-sh's and observed-sa's own guides and use what they describe; re-check every not-found row and the capture list against the runs, and record what they show;
  - **check every not-found row's wording** against what was read; Q6-SH-N01's filter to be verified;
  - **the capture list: not now.**

  The founder is at about 80 percent of the week's limit: if the work stops on it, it resumes after the reset (24 October, 05:00 UTC). The founder offered, if needed, Shopify's traces (`trace.zip`, not in git) and runs from their own machine in the signed-in stores, for targeted, bounded evidence. Not asked for yet.
- **Done for it** (commit `35b50a8`):
  - **the search covers the observed runs** (`method/runs_corpus.py`, through `corpus_search.py`): observed-sh's answers (97,781 distinct), observed-sa's saved responses (9,537 distinct), every step's page text (15,145 and 4,081 steps), the requests the pages sent, the indexes and derived tables, and the structures' source files. Folded once per commit into `~/.cache/sharrwah-corpus/<repository>-runs-<commit>.txt`; a search adds about a second;
  - **the wording check** (`method/check_not_found_wording.py`, `studies/proposals/checks/not-found-wording.tsv`): 13 of 390 rows had a quoted or labelled phrase not found as written in what they read. The five on Zid are lists whose every item is found. The eight on Shopify and Salla go to their re-check runs. Q6-SH-N01's "Type in your country" is in the held copy of the page it read (the archive record at 41642451), so the founder's doubt is answered: the label is held;
  - **the re-check brief** (`briefs/R3-observed-recheck.md`): one run per question on Shopify and on Salla, 16 in all, at `medium`. Tested by its first runs rather than a separate check.
- **The re-check's first two runs are done** (commit `b08d0b2`): Q6 on Shopify (9 new statements, N02 narrowed) and Q6 on Salla (4 new statements, 4 items narrowed), each about 5 million tokens, both passing the checker. The brief is revised after them: a store the run doesn't name, lists of more than 20 items, routes held as steps. `held_index.py` now lists the runs' steps by the address their page ended at, and the wording check reads archive offsets named in prose and joined lists item by item: 2 of 390 rows stay flagged (Q1-SA-N02, sent to its run; Q6-ZD-N03, whose label is found and whose English words are the run's own).
- **The re-check is done** (commit `6f569ba`): 16 runs, 101.4 million tokens (`costs.tsv`, step `R3b`), each passing the checker with no issues.
  - **181 new statements,** nearly all from the runs' own answers, saved responses and page text (182 statements in the Shopify and Salla folders now rest first on a run's file), each scoped to the store and date its run observed: Shopify's admin answers and pages for stores with a Yemen business entity and address (Shopify Payments, Stripe, Amazon Pay and PayPal Express not eligible; the manual methods; six third-party providers; the store currency YER; a manually paid and refunded order in YER), and Salla's saved responses and pages (the onboarding country question with seven options; the payment methods' four lists, with plan and verification gates; wallets, payouts and currencies).
  - **2 not-found rows closed** (Q1-SH-N04, each store's country; Q8-SA-N02, the platform's updates page), each moved to its folder's `not-found-closed.tsv` with the statements that close it. About 17 rows or copied gaps narrowed; the rest unchanged, each with the re-check's searches and reads added.
  - **Routes to the founder** no longer name an address a run holds: where the held steps show another state of the page (a store not eligible, a closed menu, a staff permission page), the route describes the page instead.
  - **The capture list** is rebuilt from the rows that stay: 45 rows. Not now, by the founder's decision.
  - **The wording check** passes on every row but Q6-ZD-N03, whose label is found and whose English words are the run's own.
- **Running: R4's drafts, one per question at `max`,** each started once its question's Shopify and Salla re-checks were done. **The founder's suggestion (19 October, about 16:45 UTC):** run them one or two questions at a time, so that each finishes within a session's or the week's limit, rather than all at once. Four were near their drafts and run on (Q1, Q2, Q3 and Q6); Q4, Q5, Q7 and Q8 are paused while still reading, and resume two at a time.
- **Drafts done** (commit `e2f1832`), each passing the drafts checker with notes only, for the counts past the citing guide:
  - **Q6:** 21.2 million; 82 platform ids, 4 not-found, 12 Yemen facts, 3 "doesn't show"; about 4,980 words. Its Yemen facts write a place's own brackets as square brackets (the checker then misread them; fixed): restore them when finishing.
  - **Q1:** 30.3 million; 131 platform ids, 5 not-found, 14 Yemen facts, 1 "doesn't show"; 5,461 words. It reworded Yemen places that hold their own brackets (before the checker's fix): restore them when finishing. The checks of Zid, WooCommerce and BigCommerce were made before the re-check added Shopify's and Salla's observed points, so they name none of them; the draft marks "not checked" only where a check lists a point.
  - **Q2:** 33.0 million, stopped once by the session limit; 110 platform ids, 11 not-found, 17 Yemen facts, 2 "doesn't show"; about 4,970 words. It found Q2 on Shopify's account citing some of Q2-SH-027 to 035 one off, in six points; the coordinator corrected them, with the Zid and BigCommerce checks' references (commit `d7259b2`).
  - **Q3:** 33.4 million; 121 platform ids, 7 not-found, 11 Yemen facts, 2 "doesn't show"; about 5,250 words. Its point on Stripe rests on the digest's wording for YA-62, whose quotes `record_ids.py` then cut off (now `--all`): check it when finishing.
- **The founder's note of 17:00 UTC** (`founder-messages/2026-10-19-step-text-from-html.md`; `founder-decisions.tsv`): an agent of the founder's is extracting text from observed-sh's saved step HTML that has no `text.txt` (about 6,100 page steps and 5,700 frames in 88 early runs, 58 of them journeys, such as `20260930T014656Z-journey-order-lifecycle` with its "Collect payment" menu and "Mark as paid"), into `derived/step-text-from-html/`, with an index and a `meta.json` that says how hidden text is marked. It may land only after a limit. **When observed-sh's `main` moves past `c8b5fbee2` with it:**
  1. pull observed-sh (fast-forward; read-only here), read its `docs/READING.md` and the folder's `meta.json`;
  2. add the texts to `runs_corpus.py` as step documents, titled from each run's `actions.jsonl`, and to `held_index.py`; rebuild the cache; the records keep citing `c8b5fbee2`, and new citations of the new texts cite the new commit;
  3. re-check Shopify's records against them, **Q4 and Q5 first:** every not-found row, the capture list's rows, and for each draft already written, each Shopify fact it rests on. One run per question, from `briefs/R3-observed-recheck.md` narrowed to the new texts;
  4. resume the Q4 and Q5 drafts after their re-checks; for drafts already written, revise each where the re-check changes what it rests on, before review.

  The plan and its budget don't change, by the founder's note.
- **For the Yemen facts' check (R5):** Stage 1's YQ-A014 (YA-29) carries the UN measures' end date, 2026-11-14, as its `held_at`; its source is dated 2025-11-14 (the Q3 draft's notes). The digest now reads any `held_at` after the capture as the capture's date, as the build does, with the `held_at` beside it.
- **The checking runs** follow `briefs/R3-checking.md`, made runnable by its last read (14 findings, 8 must fix) and the verification of its fixes. **Twelve are done** (commits `2b5ce9f` to `ff660b5`), each passing `--check` with no issues. With the three continued, they cost 135.9 million tokens, about 11.3 million a run.
- **Fixed after the first runs** (`PLAN.md` section 11, 19 October): some runs chose their search terms before reading and left account points unchecked, about 30 each in Q4 on WooCommerce and on Zid. A run may now search once more for points its first search left out, and records a row for every point its reading doesn't show, up to 20. Q3 and Q4 on WooCommerce and Q4 on Zid are continued under the fix.
- **Noticed by the runs, for the drafting brief:** copies that disagree. In Q2 on BigCommerce, K0132 and P0029 say BigCommerce Payments is offered in the US only, and P0030, P0068 and P0087 say the UK and US (its `notes.md`). The drafting brief should say how a proposal treats statements that disagree: both cited, each with its date.
- **Tool and brief fixes from the runs' notes:** the quote checker reads every capture of a page; the checker doesn't count ids as words, and takes a bold subheading as no point; the brief counts a table's rows as one statement toward the cap, says how to cite a page held only in a fetch archive, and says not to nest lists.
- **Next:**
  1. as each run ends: `check_proposals.py records`, capture the live pages it cites (with the language it read them in), measure it, commit;
  2. the 19 checking runs, about six at a time, as listed under "If the work was interrupted" below;
  3. when recording ends: the founder's capture list, gathered from the not-found rows routed to the founder;
  4. record the founder's marks in `founder-decisions.tsv` when they come, and carry them into `areas.tsv`.

**Agents' effort** is set by step from 13 October 2026 (`PLAN.md` section 11):
- `max`: inspections, Stage 1's step 2a, and the pilot's B, C, D and F;
- `high`: step 2b;
- `medium`: reading and recording evidence, re-run at `high` where checks or review show gaps;
- `low`: one-off mechanical questions.

From 18 October 2026, the re-frame's steps (`PLAN.md` section 11): `max` for brief checks, R1's review, R4's drafting and R6's review; `high` for R1's platform runs, R5's re-checks and audits, and the check of Q3's rows; `medium` for recording (R2 and R3), re-run at `high` where a check shows gaps.

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

**Stage 1, Yemen's axes and cases: done but for the fixes listed "before Stage 4",** which the plan change would replace (see the re-frame above).
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
  - **Stage 1's independent review: not yet usable for D** (`review-independent.md`). In a sample of 45 axes read against their quotes, 12 have an error in `today` or a case, and 6 of the 23 `in force` cases aren't in force. Examples:
    - the July 2024 cancellation of both sides' bank bans doesn't reach today;
    - PayPal shows `Available`, which hides send-only.

    Q2's five example axes are all covered. The internet shutdowns of 2020 and 2022 are recorded nowhere.
  - **Its fixes 1 to 5 and 7 are made and checked** (commit `900c24a`):
    - the 2024 bank bans end at each side's area;
    - PayPal reads "Sending from Yemen", with "only" in the note and quote;
    - the government's exchange rate reads "fixed";
    - the notes withdrawal is `provided for`;
    - YA-40's founder unknown closes from held evidence.

    Now 228 axes, 513 constants and 342 cases. The full check is clean. Precision ties stay disputes, and D marks them `unknown`. D reads each part's date until the method changes;
  - **the targeted check of S-01's axes found four errors, now fixed and checked** (commit `b9928d9`):
    - PayPal's receiving is its own constant, YK-514, "cannot receive money";
    - YK-23 keeps "personal or humanitarian";
    - Zid Pay's "Unavailable" is placed at its Kuwait terms;
    - Wagbat names cash on delivery.

    Now 228 axes, 514 constants and 342 cases. The full check is clean. It also listed eight related items for D to weigh;
  - **next for the pilot:** once D's checkpoint lists the axes S-01 bears on, the independent reviewer checks those against their quotes, and step 2a fixes what it finds, before D marks on;
  - **before Stage 4:**
    - a `within` relation between places, so a later state supersedes the places inside its own;
    - a faithfulness pass over every axis, given the sample's error rate;
    - the review's "can follow" items, including the internet shutdowns;
  - the review stop if past 20 axes (`review-axes.md`), then cases;
  - step 2c, the checker, an independent review, and a comparison with Q2's example axes.

**Stage 2, the pilot (S-01): done.** G1 went to the founder on 17 October 2026 and was answered on 18 October 2026.
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
  - **D is done** (commit `60a9468`), on Stage 1 at `b9928d9`.
    - 122 marks: 62 carried unchanged, 20 carried only with a partner, 40 unknown, and no `no placement`. So there's no product gap and no founder item from the marks, and no moves. No case changes any mark from today's.
    - With PayPal unable to receive (YK-514), today's marks rest on Zid's wallet, "available to all merchants outside the Kingdom" (S01-ZD-121, met under Q2), for VP-01, 09, 11, 14, 15, 18, 19 and 23. VP-02, 03 and 04 are carried with a partner: a courier, or a card acquirer.
  - **The register entry is written** (`entry.md`, commit `0cf1487`). The 12 founder items are one root decision, who holds the funds (S01-VP-01), and eleven that follow. The coordinator recommends, marked as such:
    - for Yemen now, the provider of each payment method holds and Sharrwah holds none, behind one interface that can carry a Sharrwah-held balance where a licence allows;
    - installments: defer;
    - currency: several per merchant, with the rial's two editions apart.
  - **F, the independent review: not yet** (`review.md`, commit `cda5e6b`). Its 14 must-fix items:
    - upstream:
      - phase C's causes for VP-08 (the same-party rule) and VP-05 (test 1);
      - S01-V-550 misplaced. Without it, VP-10 becomes `no placement`, which brings a founder item;
      - 83 variants rest on meaning rather than shared words. Strictly, VP-01's Yemen mark would be `unknown`;
      - the source-kinds rules filed terms pages as `stated`;
    - in the entry:
      - Stage 1 facts not checked against their quotes, and varied by cases;
      - YA-102's "banks only" against Stage 1's own instruments;
      - "no reference processor serves Yemen" (BitPay unsettled);
      - A2 unsupported;
      - the three-way split, which goes against the same-party rule;
      - B's support misstated;
      - no answer lines for items 2 to 12;
      - two misquoted Yemen lines.
  - **The coordinator's rulings, in the briefs and `PLAN.md` section 11:**
    - phase B's `answers` rests on what a statement says: its own words must name the party or thing in X's role in the subject's flow (matching basis 4);
    - a bullet (d) "no part" variant names no one filling X, for test 1.
  - **The source-kinds rules are fixed** (commit `94e973d`): a structure's file takes its nearest `meta.json`, and a captured copy takes its manifest's address.
  - **The fix round:**
    - **Phase B re-checked its variants under the ruling** (commits `7e82f57` and `5abebde`). The ruling now holds whatever a variant's basis, since shared words can be homonyms.
      - Every `answers` row names the role its words fill.
      - 45 variants are removed, among them S01-V-024 (Zid's wallet, which names no sales proceeds) and S01-V-550.
      - Zid's and Salla's wallet holders are added to VP-01, where their words say the wallet holds sales proceeds.
      - The answer sets changed on 15 variation points, and 32 kinds are now `official page`.
    - **Stage 1's facts behind the entry are fixed** (commit `4e3f3dd`):
      - YA-102's government area reads "banks and licensed non-bank institutions";
      - the provider licence is constant YK-515 at 750 million;
      - YA-105's id now names "Which model e-money services follow".

      Now 228 axes, 515 constants and 345 cases.
    - **Running:** phase C re-derives every cause, and phase D redoes `bears-on.tsv` and every mark, in parallel. Then the coordinator rewrites the entry, and F re-checks;
    - **Salla's `not covered` row on S01-VP-06** ("agent", S01-V-655), left by phase B's re-check, goes back to A2 as the B brief says. If A2 records a gap or an absence, A3 audits it. Then phase B places what A2 adds, and phases C and D revisit S01-VP-06;
    - **Done since** (17 October, 17:20 to 18:00 UTC):
      - **phase D's redo** (commit `bd84076`): 183 marks in 30 cases. At `YC-00`, VP-01 is now `unknown`, and VP-10 is `no placement`, with a product gap and a founder item. No case changes any mark from today's;
      - **phase C's third run** (commit `4561770`): VP-08 is `unknown`, VP-21 is a founder item, and VP-22's question is reworded. 13 founder items;
      - **two rulings for phase C** (commit `059f3ef`, `PLAN.md` section 11): a "no part" statement names no one, whatever its bullet, and shows the party isn't in its platform's set; a platform may carry more than one coexistence letter;
      - **Salla's A2 on "agent"** (commit `0b59a65`): S01-SA-190 to 201, and gap S01-SA-G07: no held source says in what capacity Salla holds buyers' payments;
      - **the entry, rewritten** (draft, commits `90fa73b` and `28828a4`): 14 decisions, each with its own answer line, and the links between them marked as the coordinator's reading;
      - **the method report** (draft, commit `50e031f`): F's findings and what changed, what a subject costs, and the proposed changes before more subjects;
    - **Done since** (18:00 to 18:50 UTC):
      - A3 confirmed S01-SA-G07, and added S01-SA-202 (commit `a884d3a`);
      - phase B placed S01-SA-190 to 202: Salla now answers S01-VP-06 with S01-V-660 and the gap (commit `4fff36c`);
      - phase D re-marked the six variation points whose rows changed: S01-VP-04 is now carried with a partner through S01-V-091 (commit `2f42203`);
      - phase C's fourth run: no cause or founder item changed; 55 letters became `A+B`, and 15 rows gained a `follows` row (commit `44e09ab`). So `follows` now separates the variation points by cause only (notes-c problem 18), which goes to the method report;
      - the entry takes these results (commit `4685b61`);
      - the method report's proposals were rewritten after the founder's question on cost (commit `3b59fe3`). It is a draft for G1;
    - **F's re-checks** (commits `f04e525` and `b67bcd2`): the first found 13 of 14 must-fix items fixed, and one new overreach on option B (finding 32). The coordinator fixed it with the optional findings (commit `978e7a9`). The second re-check's verdict: the entry lets the founder decide, with no must-fix item open. Its optional findings 38 to 40 are fixed too;
    - **the method report is complete but for G1:** about 2.1 billion tokens in all, and seven proposals before more subjects;
    - **G1 went to the founder in chat,** with the entry's decisions and G1's own question (scale up, change the method, or re-frame). The founder answered "re-frame" on 18 October 2026;
  - **D's first checkpoint** (commit `2786cb4`):
    - `bears-on.tsv` lists, for each variation point, the axes and constants its variants' conditions bear on;
    - YC-00's marks: 10 carried unchanged, nine of them through PayPal on YA-62's old "Available"; 1 with a partner; 12 unknown;
    - the checker passed the first rows.

    D's brief gap is fixed: a condition naming only countries is checked against Q2's frame, cited as `Q2`, as the coordinator's own (`PLAN.md` section 11);
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

**The usage limit has stopped the running agents nine times:**
- at about 09:50 UTC, when all ten restarted at 10:10 UTC as new agents continuing from their files;
- at about 10:55 UTC, until 15:00 UTC. The six still running were resumed at 18:53 UTC, each from its own transcript;
- at about 20:10 UTC, until 23:50 UTC. Part E, phase B and the third inspection were resumed at 23:58 UTC, each from its own transcript;
- on 13 October 2026 at about 02:05 UTC, the weekly limit, until 17 October 05:00 UTC. The check-in below fired every two hours but could do nothing until the reset. Phase B's second pass and step 2a were resumed at 06:20 UTC, each from its own transcript;
- on 17 October 2026 at about 08:30 UTC, the session limit, until 11:00 UTC. It stopped both second axes reviewers as they started. They were resumed at 11:03 UTC, each from its own transcript;
- on 17 October 2026 at about 14:40 UTC, the session limit, until 16:00 UTC. It stopped pilot phase B's re-check and Stage 1's check of the entry's facts as they started. Both were resumed at 16:02 UTC.
- on 18 October 2026 at about 23:35 UTC, the session limit, until 19 October 00:00 UTC. It stopped five of R3's first six runs. All five were resumed just after midnight, each from its own transcript, and finished.
- on 19 October 2026 at about 02:10 UTC, the session limit, until 05:00 UTC. It stopped five checking runs: Q6 on BigCommerce, Q7 on Salla, WooCommerce and BigCommerce, and Q8 on Salla. Their files were committed as a checkpoint, and all five were resumed at 05:09 UTC, each from its own transcript. The session's worker restarted several times while it waited;
- on 19 October 2026 at about 17:15 UTC, the session limit, until 18:00 UTC. It stopped the drafts of Q2 (as it tallied its ids) and Q7 (just resumed from its pause). Both were resumed at 18:05 UTC, each from its own transcript;
- on 19 October 2026, before 01:17 UTC, the container restarted. It stopped the verification of the checking brief's fixes, which was resumed at 01:17 UTC from its own transcript. The repositories, the scratch directory and the search cache survived.

**Agents running when last checked (19 October 2026, 18:15 UTC):** from `briefs/R4-drafting.md`, at `max`, two drafts: Q7 `aeda761ec1bc30dbc` (resumed at 18:05 UTC after the session limit) and Q8 `abf86971dbb1f91d6` (resumed at 18:12 UTC from its pause). **Still paused** (since 16:45 UTC): Q4 `adacc29a8edd0e708` (7.8 million spent) and Q5 `ab472a77cdbb4ee93` (13.8), each stopped while reading. They resume after their Shopify records are re-checked against observed-sh's new step text (below), each from its own transcript (SendMessage, saying it was paused and continues where it was, and naming the tool changes since: `record_ids.py --all`, a Yemen place may keep its own brackets, the digest's dates after the capture). (The times before 16:12 in today's entries ran ahead of the clock by about 15 minutes.)
- **Done and committed:** all of R3's recording, R4's preparation with the drafting brief's check and fixes, and the founder's decisions of 19 October with the search over the observed runs (`35b50a8`).

**The founder's choice, 19 October 2026, about 05:30 UTC,** near the week's usage limit: finish recording, write the drafting brief and have it checked, then stop and talk. The drafting runs wait for that talk and for the marks on the areas list. The progress report before it (05:15 UTC) gave the sample's rate, the steps past their cost, the re-sized whole (agents about 1.50 billion, the coordinator about 0.45, together about 1.95) and the method rulings since the G2 message.

**A scheduled check-in** (Routine `trig_01QJwaNYp764mJnJLh5n5ago`, every two hours at :09 UTC) wakes this session to resume agents a limit stopped. Paused on 17 October 2026 at 21:05 UTC, while G1 waited for the founder. On from 19:05 to 20:26 UTC on 18 October 2026, while the R0 check ran. On from 21:01 UTC on 18 October 2026 through R1 to R3. Paused at 05:56 UTC on 19 October 2026, while the work waited for the founder's talk. **On again** from 15:40 UTC on 19 October 2026, with the re-check's runs. Delete it when the founder asks.

**To resume:**
1. Commit whatever files are on disk, as an unchecked checkpoint.
2. An agent whose final reply never came didn't finish. Resume it by sending a message to its agent id: it continues from its own transcript. Tell it that the limit stopped it, that its files hold its work, and that it should check its last rows are complete and not redo rows already written.
3. If the id no longer resumes, start a new agent with the same prompt as before, adding: "Your files already hold part of the work. Read them, continue from where they stop, and don't redo rows already written."
4. To check a platform or part, run its checker:
   - for a platform: `python3 -I method/check_subject.py studies/subjects/S-01 OUT`, reading the lines for `<platform>/`;
   - for a part: `python3 -I method/check_yemen_cases.py studies/yemen-cases OUT --pass1 <part>`.
5. Then go on from the "Next" lists above.
