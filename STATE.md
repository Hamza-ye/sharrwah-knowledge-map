# State

Where the work is, on one page (`METHOD.md` section 4). The coordinating session keeps it, and commits it at every checkpoint. The text from before 24 October is in the history: `git show a05974a:STATE.md`.

**Updated:** 24 October 2026, 21:05 UTC.

**The method:** `METHOD.md`, adopted on 24 October 2026 with amendment 1.

**Milestone:** M1, the money boundary (subject S-01), at step 4, Verify. M0 closed with PR #6 (`reports/M0.md`).
- **Records, all proposed:**
  - D-001, who holds sellers' money: the founder's line;
  - D-002, the payment boundary;
  - D-003, the seller ledger;
  - D-004, Decisions 2 to 12 under C;
  - D-005, installments, deferred.
- **The guard** flags none of them.
- **The Knowledge Map:** S-01's 8 questions have dispositions.

**Settled** (`founder-decisions.tsv`):
- **The guard on money:** nothing that holds sellers' money through Sharrwah goes live without the founder (G1, 18 October).
- **The extent:** the 34 areas (18 and 19 October).
- **The market guard** (`METHOD.md` section 3a), and F-00: many markets, Yemen first, not the design target.
- **References:** Shopify and Salla are primary, and the others come in only on demand.
- **No merchant interviews.**
- **Code:** spikes are allowed; production code waits for the definition of ready (`METHOD.md` section 5).
- **Restored from 10 October:** F-01 (no US ties), F-05 (the founder's words are attestations) and F-06 (payments as their own concern).
- **Standing rules:** the rule on credentials in evidence, and plain words for the founder.

**Open founder decisions:**
- **Decision 1's line** (S-01): "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours."
- **O-01:** which legal entity and country contracts with sellers and partners (S-08).
- **The form of F-02** (the Sana'a zone first) **and F-03** (both zones), under the guard (S-04).
- **From M2:** the order in which the first version covers the areas, and the business targets for the quality scenarios.

**Superseded or stopped:**
- `PLAN.md` as the method. It is kept as the record.
- R5's checks of everything cited: 16 runs stopped, 17 never started.
- The drafts as deliverables: they are now candidate options.
- The planned review of the drafts, and the company-decisions run.

**In flight:** no agents. The scheduled check-in (`trig_01QJwaNYp764mJnJLh5n5ago`) is off. It is turned on only while a task runs (`METHOD.md` section 9).

**Budget:**
- M0 used one agent: the independent review in planning processed 7.3 million tokens over 51 requests, counted by `method/count_tokens.py`.
- The 2 billion stays as the upper bound. S-01's budget is 20 million agent tokens.

**The backlog:** `python3 -I method/decision_status.py` gives 16 subjects and no decision records yet.

**Next step:**
- the level 3 check of D-001 and D-004, and the level 2 review of D-002 and D-003;
- then fix what they find, and put D-001's line to the founder;
- then the walkthrough, `reports/M1.md`, and the merge.

**To resume:** `METHOD.md` section 9. Read `METHOD.md`, then this file, then the open subject's records.
