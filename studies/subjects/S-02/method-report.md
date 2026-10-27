# S-02: what each run taught

**What this file is:** what each of S-02's runs taught about running the agents and planning the work, and what changed for the next run (`PLAN.md`, Stage 4, "Each run's lessons"). Costs are by `method/count_tokens.py`, on the agents' transcripts.

## 1. The briefs' inspection (26 October)

- **Cost:** 27.9 million tokens over two rounds (112 requests), against the 5 million the frame set.
- **What it found before any agent ran:** three must-fix points in phase A's brief and one in phase B's, among them held evidence the reading lists missed: nine of Shopify's runs and Salla's markets sweep. The coordinator had built the lists from searches; the inspector went through each repository's run notes and ledgers.
- **What changed:** a reading list starts from each repository's `index/run-notes.tsv` and ledgers, not from searches alone.

## 2. Phase A, Shopify and Salla (26 October, 22:21 to 23:30 UTC)

**What it produced:** 319 statements for Shopify and 304 for Salla, 216 and 220 of them from new reading; every quote found, and no checker error on either.

**What it cost:** 104.7 million tokens for Shopify (226 requests) and 117.8 million for Salla (276), against the 60 million the frame set for both. S-02 stopped at 250.4 million (`PLAN.md`, section 8), and the founder said to continue (`founder-decisions.tsv`, 27 October).

**What it taught:**
- **An agent's context is what it costs.** Each request reads the whole context again. Shopify's context grew from 183 thousand tokens to 746 thousand, with a median of 477 thousand; Salla's reached 781 thousand. An average request cost 0.45 million.
- **A long reading list in one agent grows its context without end.** Both agents passed their stop at 300 statements, and resuming either meant re-reading a context of 750 thousand tokens on every turn.
- **Two agents at once didn't hit the usage limit.** They ran for about an hour together; in the pilot, five at once stopped within 35 minutes (S-01's method report, section 12).
- **Agents copy what is recorded selectively,** and say why: Shopify left out 52 of its 139 recorded rows, each with its reason in its notes.
- **The agents found faults in the tools,** each fixed in the run:
  - Shopify's held schema cuts descriptions at their first line break (`method/schema_type.py` reads them in full);
  - quotes from JSON in a fetch archive didn't match (`method/quote_check.py`);
  - the search listed help articles by a position one less than their line (`method/corpus_search.py`);
  - each check against the schema read the 7 MB record again (`method/quote_check.py` keeps it by offset).
- **Gaps that only an observation would close** went to the founder (Salla's four). Each is a run the local agent could make, so each became a handoff (`handoffs/`; the founder, 27 October).

**What changed for the next runs:**
- **Each remaining reading list is split into parts,** each read by a fresh agent that continues from the files and notes, so no context grows past a few hundred thousand tokens. The paused agents' work is in their files, so nothing is read twice.
- **Phases B and C and the review run per root decision,** three agents each, each reading only the statements its decision's bullets hold.
- **Agents look up rows in large files with scripts,** instead of loading them whole.
- **The budget is 700 million tokens** for S-02 (the founder, 27 October), and it never costs evidence.

## 3. Phase A finished by fresh agents (27 October)

**What it produced:**
- **Salla:** 310 statements, 585 citations; no checker error.
- **Shopify part 1:** 85 new observed statements, from seven runs, the admin's route ledger and controls, and six more stores' general settings. That makes 404 statements and 880 citations, with no checker error.

**What it cost:** Salla's finisher 8.0 million (65 requests). Shopify's part 1, 59.8 million (237 requests).

**What it taught:**
- **A fresh agent with a short task costs far less per request:** Salla's finisher about 0.12 million, against 0.43 million before.
- **A long run still grows its context,** even from a fresh start, because every tool output stays in it. Shopify's part 1 ran 237 requests at about 0.25 million each. So each part is kept to about a hundred requests.
- **A container restart stopped two agents.** Both had written as they went, so nothing was lost, and both were resumed from their transcripts.
- **Agents shared one scratch folder,** and one overwrote another's script. That one had already finished. Each agent now gets its own folder (phase A brief, rule 12).
- **The quote tester read a large file again for each quote,** nine seconds a call on Shopify's 8.8 MB admin controls. It now tests a batch in one process (`method/quote_check.py --batch`).
- **"No ellipses" turned away the platform's own text,** such as a field's "Search countries…". An ellipsis is now refused only where its source doesn't hold it (`method/check_subject.py`). The pilot's check is unchanged.

**What changed for the next runs:**
- Shopify's remaining reading is split in two parts: the observed runs not yet read, then the plan tables, the leads and the gaps' re-check.
- Each agent writes only in its own scratch folder.

## 4. Phase A finished: Shopify parts 2 and 3, Zid, WooCommerce and BigCommerce (27 October)

**What it produced:** phase A for all five platforms, 1,458 statements: Shopify 588, Salla 310, WooCommerce 227, Zid 172 and BigCommerce 161. The checker found every quote, 3,193 of them, and no error. Seven gaps that only an observation would close went to the local agent as capture requests (`handoffs/`, H-001 to H-007).

**What it cost:**

| Run | Requests | Millions | Per request |
| --- | --- | --- | --- |
| Shopify, part 2 | 168 | 39.6 | 0.24 |
| Shopify, part 3 | 112 | 27.8 | 0.25 |
| Zid | 198 | 74.7 | 0.38 |
| WooCommerce | 137 | 47.6 | 0.35 |
| BigCommerce | 98 | 23.1 | 0.24 |

Phase A cost 504 million in all, against the 325 to 375 million the frame set for it. The coordinating session processed 144 million more over the same time, outside the budget, which counts the agents.

**What it taught:**
- **Parts of about a hundred requests held their cost at about 0.25 million a request** (Shopify's parts 2 and 3, and BigCommerce).
- **Zid and WooCommerce each ran in one agent,** and their contexts grew: 0.38 and 0.35 million a request.
- **Reading "from what is recorded" went well past the recorded rows,** to the held pages their gaps needed: Zid wrote 172 statements from 72 recorded rows, WooCommerce 227 from 87, and BigCommerce 161 from 81.
- **The frame's estimates were low.** It set 45 to 75 million for Zid, WooCommerce and BigCommerce, which cost 145 million, and 30 to 50 million to finish Shopify and Salla, which cost 135 million.

**What changed for the next runs:**
- **Phase B runs in nine parts** (`b/parts.tsv`), each a root decision's bullets, or one bullet for some of its platforms. Each part's size is counted in statement-bullet pairs before it runs, and its cost is measured after it.
- **An inspector tries each brief on a sample before it runs.** For phase B, a dry run of 30 statements gives the rate each part's size is checked against.
