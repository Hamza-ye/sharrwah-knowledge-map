# State

Where the work is, on one page (`METHOD.md` section 4). The coordinating session keeps it, and commits it at every checkpoint. The text from before 24 October is in the history: `git show a05974a:STATE.md`.

**Updated:** 25 October 2026, 15:40 UTC.

**The method:** `METHOD.md`, adopted on 24 October 2026 with amendments 1, 2 and 3. Amendment 3 (the founder, 23:01 UTC) sets the evidence standard, checks that try to refute, and the acceptance rule: no record is accepted while something it leaves open could reverse it. Amendment 2 adds Terms and Scope to every decision record, and the rule that a record rests on evidence and accepted outcomes, never on another record's wording.

**Milestone:** M1, the money boundary (subject S-01). Amendment 2's pass is finished. Before answering Decision 1, the founder asked for an assessment of their feedback and of an evidence-completeness pass (`founder-decisions.tsv`, 25 October): part one is `reports/M1-method-assessment.md`, part two `reports/M1-plan-changes.md`.
- **Done:**
  - the glossary (`architecture/12-glossary.md`);
  - Terms and Scope in D-001 to D-005;
  - four refuting checks: D-001 and D-004 at level 3, twice; D-002 and D-003 at level 2; and D-001's page for the founder at level 3.

  Their findings were verified against the evidence and applied (`decisions/checks/M1-terms-scope-dispositions.md`).
- **Decision 1's page** puts the line and three choices on its extent to the founder, each recommended for launch: (1) where B ends, by the guard's source rather than its words: an account held under the seller's own agreement is C, even when asked for through Sharrwah; (2) Sharrwah's fees, and anything owed to it or its partners, billed apart; (3) no balance sellers pay into. The other way of choices 2 and 3 stays reserved, like A and B. D-004 is accepted with D-001 unless the founder says otherwise.
- **The founder's remarks of 25 October** are assessed there, point by point, and an independent check tried to refute both parts: 29 fixes, all verified and applied (`decisions/checks/M1-method-assessment-dispositions.md`). Its findings: the absence audit of 13 October and the Q1 concern map as the subject index were dropped when `METHOD.md` was adopted; the plan's second change had dropped the coexistence step with its generality rule, and coarsened the inventory sweep to areas; no check looks at what a record never mentions. A trial of the omission check on Decision 1 (`method/slice_coverage.py`) changed no part of its line; it added partners' cases to choice 2 and apps (S-06) to what it leaves open, all of them already held in the repository. Amendment 4 (4a to 4d) is proposed, not adopted. W-20 is open, and W-08 records its failed mitigation.
- **Under the acceptance rule:** D-001 and D-004 carry everything they leave open. D-002 doesn't carry nine items, and D-003 four, among them the buyer data Shopify's payment request sends a provider (E032:146–163) and stored permissions for B2B and edits. Both stay proposed, as the working basis, until those items are decided at S-05, S-07, S-10, S-11 and S-03 and the records are revised.
- **Records D-001 to D-005:** the guard flags none, and `decision_status.py` finds no fault in their Terms and Scope. The glossary's quotes are checked by `method/inventory_quotes.py`. The inventory the pass used is `decisions/checks/M1-terms-inventory.md`.
- **M0** closed with PR #6. M1's pull request is PR #7.

**Settled** (`founder-decisions.tsv`):
- **The guard on money:** nothing that holds sellers' money through Sharrwah goes live without the founder (G1, 18 October).
- **The extent:** the 34 areas (18 and 19 October).
- **The market guard** (`METHOD.md` section 3a), and F-00: many markets, Yemen first, not the design target.
- **References:** Shopify and Salla are primary, and the others come in only on demand.
- **No merchant interviews.**
- **Code:** spikes are allowed; production code waits for the definition of ready (`METHOD.md` section 5).
- **Restored from 10 October:** F-01 (no US ties), F-05 (the founder's words are attestations) and F-06 (payments as their own concern).
- **Standing rules:** the rule on credentials in evidence, and plain words for the founder.
- **The founder's messages are framed first;** the framing is recorded, not the message, and messages are no longer saved (`METHOD.md` section 3).
- **Amendment 2** (24 October, 22:11 UTC).

**Open founder decisions:**
- **Decision 1's line and its three choices** (S-01; `reports/M1.md`): "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours."
- **Amendment 4** (`reports/M1-method-assessment.md`; `reports/M1-plan-changes.md`): approve, change or not now.
- **O-01:** which legal entity and country contracts with sellers and partners (S-08).
- **The form of F-02** (the Sana'a zone first) **and F-03** (both zones), under the guard (S-04).
- **From M2:** the order in which the first version covers the areas, and the business targets for the quality scenarios.

**Superseded or stopped:**
- `PLAN.md` as the method. It is kept as the record.
- R5's checks of everything cited: 16 runs stopped, 17 never started.
- The drafts as deliverables: they are now candidate options.
- The planned review of the drafts, and the company-decisions run.

**In flight:** nothing. The scheduled check-in is off.

**M2's feasibility test** is done (read-only; 8.2 million tokens). Its report is in the coordinator's scratchpad, and goes into M2's pull request once M1 merges. Its verdict is **partly feasible:**
- **Within each platform,** the structures say which permission gates which page.
- **Between the two,** nothing joins them automatically:
  - a hand-made crosswalk of about 80 to 120 terms would let events and API groups join by rule (an estimate);
  - permissions join only by hand;
  - placing the platforms' groups into the 34 areas is hand work.
- **A full map** would take about 18 to 26 agent hours (an estimate). M2's scope and budget are set at its framing, with options for the founder.

**Budget:**
- M0 used one agent: the independent review in planning processed 7.3 million tokens.
- M1's agents processed 22.4 million tokens against its budget of 20 million, under the stop line of 25 million. Both are counted by `method/count_tokens.py`.
- The 2 billion stays as the upper bound. S-01's budget is 20 million agent tokens, and the founder added about 5 million for amendment 2's pass (stop line 6.25 million).
- **The pass's agents:** the terms inventory 23.8 million (106 steps, its context growing from 49 thousand to 375 thousand tokens: risk W-17), then four capped checks of 3.3, 4.7, 2.6 and 1.0 million. That is 35.4 million for the pass, and 57.8 million for S-01, past the stop line, under the founder's go of 23:01 to continue while productive.
- **The assessment of 25 October:** one independent check, 4.1 million (38 requests). S-01 in all: 61.9 million.

**The backlog:** `python3 -I method/decision_status.py` gives 16 subjects and 5 decision records: 4 proposed, 1 deferred.

**Next step:**
- the founder's answers on amendment 4 and on Decision 1. Frame their message first;
- if amendment 4 is approved, enter it in `METHOD.md` section 12, with its changes to sections 5, 6, 7 and 13, and apply it from the next record put for acceptance;
- on the answer: accept D-001 and D-004 with the founder's choices. D-002 and D-003 stay proposed until the subjects that decide their open items have done so (acceptance rule);
- merge PR #7 with `reports/M1.md` as its description, and add the row to `HISTORY.md`;
- then M2, the spine: frame it with options for its scope and budget, starting from its feasibility test.

**To resume:** `METHOD.md` section 9. Read `METHOD.md`, then this file, then the open subject's records.
