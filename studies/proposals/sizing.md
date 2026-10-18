# What each step is expected to cost (draft, 18 October 2026)

**Status: draft, revised after the check of the drafts (`studies/proposals/check-of-the-draft.md`, findings 34 to 40), and re-counted.** It is checked again before the founder's go.

## How tokens are counted

- **What is counted.** The tokens a run processes: input, output, cache reads and cache writes, summed over its API requests, from its own transcript. Most of it is context read again on each turn.
- **Each request once.** `method/count_tokens.py` counts each request once.
  - A transcript writes a request over several lines, one per block of the reply, and each line repeats the request's whole usage.
  - The method report's first count took every line, and so roughly doubled every figure. Its section 12 is now corrected.
  - All figures here are in the corrected count.
- **The founder's budget and bar** were stated in the first count:
  - the budget, "about the pilot's cost", is about **1.0 billion** agent tokens in this count. The founder's message says 2 billion;
  - the sample's bar, half the pilot's cost per statement for phases A and A2, is about **0.26 million**. The founder's message says 1.1 million halved.
- **The coordinator's own work** is estimated apart, on top.

## The measures this rests on

**The usage limit,** from the session's transcripts, in this count:
- **A week's limit.** From the weekly reset (17 October, 05:00 UTC) to the founder's report of 33 percent used (17:28 UTC), this session processed 936 million tokens: 145 million by the coordinator and 791 million by agents. So a week's limit is about **2.8 billion**, and 1 percent is about 28 million. This is rough: the founder's figure may include use outside this session, and the meter isn't a token count.
- **One usage window.** On 17 October, three stretches of work that a session limit stopped processed about 357, 411 and 381 million tokens, depending on where each is taken to start. So a window holds about **0.38 billion**.
- **This week so far.** From the reset to 20:00 UTC on 18 October, about 1.22 billion, about **43 percent** of the week. The week resets on 24 October at 05:00 UTC.
- **The coordinator's share.** Over the work so far, the coordinator processed about 0.2 tokens for each agent token: 742 million against 3,965 million.

**The pilot's runs, the units each step is sized from:**

| Kind of run | Runs | Tokens (millions) | Volume | Rate |
| --- | --- | --- | --- | --- |
| Recording statements (phases A and A2) | 16 | 427 | 821 statements, 566 of them not taken from the concern map | 0.52 million per statement, 0.75 per new statement; 27 per run |
| Auditing a claim that something isn't there (A3) | 7 | 162 | 61 claims | 2.7 million per claim; 23 per run |
| Checking a brief before it runs | 6 (2 for the pilot, 4 for Stage 1) | 30 | 6 checks | about 5 million per check |
| This plan's check of the drafts (R0) | 1 | 17 | the drafts, the message, `PLAN.md`, the extracts, and samples of the records | 17 million |
| Independent review, first pass (F) | 1 | 38 | the entry, its 14 decisions, and the files they rest on | 38 million |
| Independent review, re-checks after fixes (F) | 2 | 37 and 12 | two rounds of fixes | |
| Drafting from a subject's records (phase C, first run) | 1 | 16 | 23 variation points; its brief named about 780 KB of files | 16 million |
| Phase C, all four runs | 4 | 72 | | re-runs after rulings took 3.5 times the first run |
| Re-checking a Yemen fact against its quotes | 2 (Stage 1's reviewer) | 40 | 32 axes and constants | 1.25 million per fact |
| Re-checking a platform fact or quote against its source (F's first re-check) | 1 | 37 | about 230 claims, quotes and ids | 0.16 million per item |

The per-run figures that section 12 of the method report doesn't give come from the agents' transcripts, counted with `method/count_tokens.py`: the R0 check, F's three rounds, C's first run, and Stage 1's re-checks.

## Each step, scaled

The scaling is what each run must read and record, against the pilot run it is sized from. Re-runs are counted where a check can send work back.

| Step | Runs | Sized from | Scaling | Agents (millions) |
| --- | --- | --- | --- | --- |
| R0. Check of the drafts, and its re-check of the fixes | 2 | measured | The check measured 17, and the re-check 22: continuing the same agent re-reads its long context on every turn | 17 + 22 = **39** |
| R1. Each platform's areas | 5, and re-runs | the R0 check, 17, for about 250 KB read | Shopify 271 KB and Salla 233 KB at about 17 each; Zid 89 KB 8, WooCommerce 67 KB 7, BigCommerce 52 KB 6. A quarter more for re-runs | 55 + 14 = **69** |
| R1. Review of the areas list: its brief's check, a first pass and two re-checks | 4 | brief checks, 5; F's rounds, 38, 37 and 12 | It weighs fewer claims than F, but reads five areas files, the merged list and samples of the records: a first pass of about 30, re-checks of about 12 and 6 | 5 + 30 + 12 + 6 = **53** |
| R2. Checks of the recording and checking briefs | 2 | brief checks, 5 | A little longer than the pilot's | **12** |
| R2. The sample | 1 | the bar | About 45 new statements: 12 at the bar, 23 at the pilot's rate for all its statements, 34 at its rate for new ones | **12** (up to 34) |
| R3. In-depth recording runs | 20 | the bar, once the sample passes | About 945 new statements in all. For each in-depth platform: Q1 50, Q2 70, Q3 45, Q4 30, Q5 60, Q6 30, Q7 35, Q8 40. In-depth platforms: three for Q1, Q2, Q3 and Q5, two for the others | 945 × 0.26 = **246** |
| R3. Checking runs | 20 | what each must read | Each reads the in-depth accounts for its question and its own platform's copies, and records little. About 5 each | **100** |
| R3. Re-runs at `high` | | about a tenth of the runs | | **35** |
| R4. Check of the drafting brief | 1 | brief checks | | **6** |
| R4. Drafting, one run per question | 8 | phase C's first run, 16 | Each reads its question's five accounts, the records they cite, a digest of Stage 1 and the areas list: about 15 each. Q5 also reads the pilot's entry and records: about 25 | **130** |
| R4. Re-runs of drafting | | phase C's re-runs | Fewer than C's, since the rulings are settled: about a third | **40** |
| R4. Gathering the evidence for the company decisions | 1 | | One short run over the drafts and their records | **10** |
| R5. Checks of the briefs for re-checking facts, auditing and Yemen | 3 | brief checks | | **18** |
| R5. Re-checking each fact a proposal rests on | about 300 facts | F's re-check, 0.16 per item | About 35 facts per proposal, and 20 for the company decisions. A fresh run reads more than F did: about 0.25 each | **75** |
| R5. Searching and auditing what a proposal rests on that wasn't found | about 40 claims | A3, 2.7 per claim | About five per proposal | **108** |
| R5. Re-checking the Yemen facts used, and auditing what Yemen's evidence doesn't show | about 45 facts and 8 claims | Stage 1's re-checks, 1.25 per fact; A3 | About 60 facts in all, 15 of them checked in the pilot at Stage 1's current commit | 56 + 22 = **78** |
| R5. Re-checks after fixes | | | | **20** |
| R6. Check of the review brief | 1 | brief checks | | **6** |
| R6. Independent review | 2 batches of four | F's rounds, 38, 37 and 12 | Each batch about F's whole review: a first pass of about 40, re-checks of about 30 and 10 | 2 × 80 = **160** |
| R6. The company decisions' review, in the second batch | | | | **10** |
| R6. How the proposals bear on each other | 1 | brief checks and F | One short run over the eight proposals | **12** |

**Agents' total: about 1.24 billion,** if the sample meets the founder's bar. The range is about 0.9 to 1.6 billion. That is about a fifth over the budget, the pilot's 1.03 billion.

**If the sample comes in below the bar,** step R3 costs less. At two thirds of the bar, R3's in-depth runs cost about 165 million rather than 246.

## If it can't fit: what would be cut, in order

Each cut is the founder's to decide, with what it saves and what it loses.

| # | Cut | Saves (millions) | What it loses |
| --- | --- | --- | --- |
| 1 | A second re-check of a review batch only if the first leaves a must-fix finding open | up to 20 | Little: a second re-check only confirms fixes |
| 2 | Question 8 drafted from the areas list and what is recorded, with no recording runs | about 40 | No new reading on how the platforms add and extend what they offer |
| 3 | Checking runs only where a platform's recorded material suggests an answer the in-depth platforms might not show. The depth choice marks the rest "none", with why | about 40 | A platform's different answer is likelier to be missed (risk 16). The review still checks each "none" |
| 4 | One in-depth platform fewer for each question, checked instead | about 50 | Every proposal rests on fewer platforms read in depth |

**With cuts 1 to 3:** about 1.14 billion. **With all four:** about 1.09 billion.

## The coordinator's own work, shown apart

These are estimates, from the measured share of about 0.2 tokens per agent token, and what each step asks of the coordinator.

| Step | What the coordinator does | Millions |
| --- | --- | --- |
| R0 | drafting, the fixes after the check and re-check, the re-count, the summary for the founder | 80 (55 measured by 20:24 UTC on 18 October) |
| R1 | merging five lists into one, the depth choice, the message to the founder | 30 |
| R2 | the copy script, the checker, the sample, the measurement and the re-sizing | 15 |
| R3 | starting and checking about 40 short runs, and the copies for each question | 50 |
| R4 | finishing the drafts, and writing the company decisions | 30 |
| R5 | handling the re-checks and audits, and the fixes | 20 |
| R6 | the reviews' fixes, and the message to the founder | 25 |
| Throughout | `STATE.md`, commits | 15 |
| **Total** | | **about 265** |

## Each step: tokens, share of a week, days, and when it comes back

"Days" assumes each step starts as soon as the last ends, and that work resumes when a usage window reopens.

| Step | Agents + coordinator (millions) | Share of a week's limit | Days of work | Comes back to the founder |
| --- | --- | --- | --- | --- |
| R0 | 39 + 80 = 119 | 4% | done | with the plain summary, for the go |
| R1 | 122 + 30 = 152 | 5% | half a day | with the areas list, for marking (G2) |
| R2 | 24 + 15 = 39 | 1% | runs during the founder's marking | only if the sample misses the bar |
| R3 | 381 + 50 = 431 | 15% | 1 to 1.5 | only if a step runs past its expected cost; the capture list when recording ends |
| R4 | 186 + 30 = 216 | 8% | half a day | no |
| R5 | 299 + 20 = 319 | 11% | half a day to a day | no |
| R6 | 188 + 25 = 213 | 8% | half a day to a day | with the proposals and the company decisions, several in one message |
| Throughout | 15 | 1% | | |
| **Whole plan** | **about 1.24 + 0.27 = 1.51 billion** | **about 53%** | **about 4 to 5 days of work** | |

**By the calendar:**
- **From the go to the proposals:** about 4 to 6 days. The founder's marking of the areas is the one wait inside that span, and the sample runs during it.
- **Usage windows:** about four windows' worth of work.
- **The week's limit:** about 43 percent of this week's limit is used already, R0's work so far included. What is left of the plan needs about 50 percent more. So it fits before the reset on 24 October only if nothing else uses the limit and no step runs over. Expect a pause at the weekly limit, most likely late in step R5 or R6, until the reset. The cuts above make that less likely.
