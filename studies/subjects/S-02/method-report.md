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
