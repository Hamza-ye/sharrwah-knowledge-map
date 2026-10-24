# State

Where the work is, on one page (`METHOD.md` section 4). The coordinating session keeps it, and commits it at every checkpoint. The text from before 24 October is in the history: `git show a05974a:STATE.md`.

**Updated:** 24 October 2026, 23:56 UTC.

**The method:** `METHOD.md`, adopted on 24 October 2026 with amendments 1, 2 and 3. Amendment 3 (the founder, 23:01 UTC) sets the evidence standard, checks that try to refute, and the acceptance rule: no record is accepted while something it leaves open could reverse it. Amendment 2 adds Terms and Scope to every decision record, and the rule that a record rests on evidence and accepted outcomes, never on another record's wording.

**Milestone:** M1, the money boundary (subject S-01). The founder chose to finish amendment 2's pass while it stays productive (23:01 UTC).
- **Done:**
  - the glossary (`architecture/12-glossary.md`);
  - Terms and Scope in D-001 to D-005;
  - a level 3 check of D-001 and D-004, and a level 2 review of D-002 and D-003, each trying to refute.

  Their findings were verified against the evidence and applied (`decisions/checks/M1-terms-scope-dispositions.md`). The largest: the glossary had narrowed the founder's guard. B now follows the guard's words, so accounts a platform opens or requests for a seller with another company, such as Salla's Tabby requests, are B.
- **Running:** a fresh check of D-001 and D-004 as they now stand. Decision 1 comes back after it.
- **Under the acceptance rule:** D-001 and D-004 carry everything they leave open. D-002 doesn't carry nine items, and D-003 four, among them the buyer data Shopify's payment request sends a provider (E032:146–163) and stored permissions for B2B and edits. Both stay proposed, as the working basis, until those items are decided at S-05, S-07, S-10, S-11 and S-03 and the records are revised.
- **Records D-001 to D-005:** their earlier checks were D-001 and D-004 at level 3, D-002 and D-003 at level 2. The guard flags none, and `decision_status.py` finds no fault in their Terms and Scope. The inventory the pass used is `decisions/checks/M1-terms-inventory.md`.
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
- **Whether amendment 2's pass goes on** after its overrun (S-01; `reports/M1.md`, item 1).
- **Decision 1's line** (S-01), after the pass: "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours."
- **O-01:** which legal entity and country contracts with sellers and partners (S-08).
- **The form of F-02** (the Sana'a zone first) **and F-03** (both zones), under the guard (S-04).
- **From M2:** the order in which the first version covers the areas, and the business targets for the quality scenarios.

**Superseded or stopped:**
- `PLAN.md` as the method. It is kept as the record.
- R5's checks of everything cited: 16 runs stopped, 17 never started.
- The drafts as deliverables: they are now candidate options.
- The planned review of the drafts, and the company-decisions run.

**In flight:** one read-only checker, re-checking D-001 and D-004 at commit `3e5ba3f` without the earlier checks' findings, and writing `decisions/checks/M1-terms-scope-recheck-D001-D004.tsv`. It is capped at 35 tool calls. The scheduled check-in is on while it runs.

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
- **The pass's agents so far:** the terms inventory 23.8 million (106 steps, its context growing from 49 thousand to 375 thousand tokens: risk W-17), the level 3 check 3.3 million, the level 2 review 4.7 million. That is 31.8 million for the pass, and 54.2 million for S-01, past the stop line, under the founder's go of 23:01 to continue while productive.

**The backlog:** `python3 -I method/decision_status.py` gives 16 subjects and 5 decision records: 4 proposed, 1 deferred.

**Next step:**
- the founder's answer on the pass (`reports/M1.md`, item 1). If it goes on: the glossary (`architecture/12-glossary.md`) and Terms and Scope in D-001 to D-005 from the inventory, written by the coordinator with no decision broadened; then one capped independent check of the terms Decision 1 and D-004 rest on;
- then Decision 1's line goes back to the founder;
- on the founder's line: accept D-001 and D-004; D-002 and D-003 stand after their veto window;
- merge PR #7 with `reports/M1.md` as its description, and add the row to `HISTORY.md`;
- then M2, the spine, with the feasibility test first.

**To resume:** `METHOD.md` section 9. Read `METHOD.md`, then this file, then the open subject's records.
