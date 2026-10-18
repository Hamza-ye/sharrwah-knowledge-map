# What each step is expected to cost (draft, 18 October 2026)

**Status: draft, for the check before the founder's go on the plan change.**

Costs are tokens processed, counted as the method report counts the pilot's (`studies/subjects/S-01/method-report.md`, section 12): every agent turn's input, cached re-reads and output, summed from the agents' own transcripts. The coordinator's own work is estimated apart, on top.

## The measures this rests on

**Converting tokens to the founder's usage limit.** This is the coordinator's reading of the session's transcripts.
- **A week's limit.** From the weekly reset (17 October, 05:00 UTC) to the founder's report of 33 percent used (17:28 UTC), this session processed 1,977 million tokens: 335 million by the coordinator and 1,641 million by agents. So a week's limit is about **6.0 billion**, and 1 percent is about 60 million. This is rough. The founder's figure may include use outside this session, and the meter isn't a token count.
- **One usage window.** On 17 October, each stretch of work before a session limit stopped it processed 748, 798 and 755 million tokens. So a window holds about **0.77 billion**, and a new one opens about five hours after the last began.
- **The coordinator's share.** Over the pilot, the coordinator processed about 0.2 to 0.3 tokens for each agent token. On 17 October it was 434 million against 1,971 million.

**The pilot's runs, the units each step is sized from:**

| Kind of run | Pilot runs | Tokens (millions) | Volume | Rate |
| --- | --- | --- | --- | --- |
| Recording statements (phases A and A2) | 16 | 884 | 821 statements | 1.08 million per statement |
| Auditing a claim that something isn't there (A3) | 7 | 296 | 61 claims | 4.9 million per claim |
| Checking a brief before it runs | 6 (3 pilot, 3 Stage 1) | 65 | 6 checks | 10.8 million per check |
| Independent review, first pass | 1 (F) | 79 | the entry, its 14 decisions, and the files they rest on | 79 million |
| Independent review, re-check after fixes | 2 (F) | 94 | two rounds of fixes | 47 million per round |
| Synthesis over a subject's records (phase C, first run) | 1 | 40 | 23 questions, about 300 KB of records | 1.7 million per question |
| Re-checking a Yemen fact against its quotes | 2 (Stage 1's targeted checks) | about 60 | about 34 facts | 1.8 million per fact |
| Re-checking a platform fact or quote against its source (F's re-check) | 1 | 73 | about 230 claims, quotes and ids | 0.3 million per item |

## Each step, scaled

The scaling is the volume each run must read and record, over the volume of the pilot run it is sized from.

| Step | Runs | Sized from | Scaling | Agents (millions) |
| --- | --- | --- | --- | --- |
| R0. Check of the plan change, the first briefs and the questions | 1 | brief check, 10.8 | It reads about four times a pilot brief check's material: the founder's message, this plan change, `PLAN.md`, the questions, the R1 briefs, this sizing, and the extracts it samples | 40 |
| R1. Each platform's areas | 5 | phase C's first run: 40 for about 300 KB of records | By extract size: Shopify 184 KB and Salla 200 KB at 0.6 to 0.7 of C's input, 25 each. Zid 73 KB 12, WooCommerce 51 KB 9, BigCommerce 39 KB 8 | 80 |
| R1. Review of the areas list, and one re-check | 2 | F's first review 79; F's last re-check 21 | It reads less than F did: five areas files, the merged list and the extracts, about 0.6 of F's material | 45 + 20 = 65 |
| R2. Check of the recording brief | 1 | brief check | 1 to 1 | 11 |
| R2. The sample: one question on one platform | 1 | recording, 1.08 per statement | About 40 statements beyond those a script copies. At the pilot's rate 43; the founder's bar is under half that, about 22 | 22 to 43 |
| R3. Recording, every question | about 40 | recording, at the rate R2 measures | About 22 in-depth runs at about 40 new statements each, and about 18 checking runs at about 10, so about 1,060 statements. Statements a script copies unchanged cost nothing here | 570 at the bar; 1,145 at the pilot's rate |
| R4. Check of the drafting brief | 1 | brief check | 1 to 1 | 11 |
| R4. Drafting the proposals | 4 (two questions each) | phase C's first run, 40 | Each reads two questions' records, about 1.4 times C's input | 4 × 55 = 220 |
| R5. Checks of the fact-check and audit briefs | 2 | brief check | 1 to 1 | 22 |
| R5. Re-checking each fact a proposal rests on against its source | 4 | F's re-check, 0.3 per item | About 25 facts per question, 200 in all, at 0.4 each for meaning beyond what the script checks | 80 |
| R5. Searching and auditing what a proposal rests on that wasn't found | about 24 claims | A3, 4.9 per claim | About 3 per question | 116 |
| R5. Re-checking the Yemen facts used | about 25 facts | Stage 1's checks, 1.8 to 2 per fact | About 40 facts in all; 15 were re-checked in the pilot at Stage 1's current commit and count as checked | 50 |
| R6. Check of the review brief | 1 | brief check | 1 to 1 | 11 |
| R6. Independent review of the proposals | 2 batches of 4 | F: first review 79, re-checks 47 | Each batch is about 0.75 of the pilot entry's checking. A first review of 60, and re-checks of 35 | 2 × 95 = 190 |

**Agents' total:**
- **About 1.49 billion, if the sample meets the founder's bar** (R2 and R3 at half the pilot's rate per statement). That is within the 2 billion.
- **About 2.08 billion at the pilot's rate.** That is over the 2 billion, but the founder's bar on the sample rules that case out: the work stops at R2 and comes back first.

**If it can't fit, what would be cut, in order** (each for the founder to decide):
1. One in-depth platform fewer for each question: about 200 million less at the bar.
2. Question 8, on parts, from the areas list and what is recorded only, with no recording run: about 60 million less.
3. One review batch instead of two: about 60 million less.

## The coordinator's own work, shown apart

These are estimates, from the pilot's share of 0.2 to 0.3 tokens per agent token and what each step asks of the coordinator.

| Step | What the coordinator does | Millions |
| --- | --- | --- |
| R0 | drafting, the check, the summary for the founder | 80 |
| R1 | the extract script, merging five lists into one, choosing depth by question, the message to the founder | 50 |
| R2 | the script that copies recorded statements, the sample run, the measurement, the re-sizing | 15 |
| R3 | starting and checking about 40 short runs, and the copy scripts for each question | 120 |
| R4 | finishing the drafts, collecting the company decisions | 60 |
| R5 and R6 | handling checks, reviews and fixes, the founder's messages | 80 |
| Throughout | `STATE.md`, commits | 20 |
| **Total** | | **about 425** |

## Each step: tokens, share of a week, days, and when it comes back

"Days" assumes each step starts as soon as the last ends, and that work resumes when a usage window reopens. The founder's own waits are listed apart.

| Step | Agents + coordinator (millions) | Share of a week's limit | Days of work | Comes back to the founder |
| --- | --- | --- | --- | --- |
| R0 | 40 + 80 = 120 | 2% | under 1 | with the plain summary, for the go |
| R1 | 145 + 50 = 195 | 3% | under 1 | with the areas list, for marking (G2) |
| R2 | 33 to 54 + 15 = about 60 | 1% | under 1 | only if the sample misses the bar; otherwise one line in the next message |
| R3 | 570 + 120 = 690 | 12% | 1 to 2 | only if a step runs past its expected cost |
| R4 | 231 + 60 = about 290 | 5% | under 1 | no |
| R5 | 268 + 40 = about 310 | 5% | under 1 | no |
| R6 | 201 + 80 = about 280 | 5% | under 1 | with the proposals and the company decisions, several in one message |
| **Whole plan** | **about 1.49 + 0.43 = 1.92 billion** | **about a third of one week's limit** | **about 3 to 4 of work** | |

**By the calendar, waits included:**
- **Work:** about 2.5 usage windows of compute, spread over 3 to 4 days by the steps' order and the windows' resets.
- **The founder's waits:** the go on the plan change, the areas marks (G2), and the proposals. If each takes up to a day, the plan takes **about 5 to 7 days** from the go to the proposals.
- **The week's limit:** about 40 to 45 percent of this week's limit is used already, so a third more fits before it resets on 24 October, if nothing else uses it.
