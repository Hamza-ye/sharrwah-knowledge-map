# The check of the method assessment: what was done with each finding

The coordinator's record of the independent check of `reports/M1-method-assessment.md` and `reports/M1-plan-changes.md` at commit `79d8135` (`M1-method-assessment-check.tsv`: 70 rows). Each finding was tested against its evidence before it was applied (`METHOD.md` section 6). The checker re-ran `method/slice_coverage.py` and matched the saved output exactly.

**Counts.** Part one: 20 hold, 21 fix, 8 open. Part two: 11 hold, 8 fix, 2 open. All 29 fixes were verified and applied. The 10 open rows are answered below. No finding was rejected.

**The evidence checked first:**
- the pilot's absence audit: commit `a920665`, 13 October; the method report is dated 17 October (`studies/subjects/S-01/method-report.md`:3); the written rule dates from 12 October (`2842819:PLAN.md`:93, :196);
- the quoted concern of 24 October is the coordinator's framing (`METHOD.md`:335, "The founder's concern, framed:"); the rule written from it checks extent "against the paths it cites" (:212);
- the founder's words of 24 October: "understand the current state and the leverage already available" (`founder-messages/2026-10-24-method-accepted.md`:19);
- Salla's financing: "Collection amounts are calculated from net Mada and credit card sales after payment fees and VAT on fees." (`STR:payments.json`); the pilot already held it (`studies/subjects/S-01/salla/statements.tsv`, S01-SA-130, S01-SA-131);
- Salla's apps: `STR:apps.json` holds shipping waybill amounts held from the wallet and request costs deducted from it, not dropshipping, which is `SAPI:64` only;
- the area line's place in the plan change: `studies/proposals/plan-change.md`:207, with no reason given;
- management of change: OSHA 29 CFR 1910.119(l), as OSHA's VPP Supplement A describes it.

**Applied, part one:**

| Finding | What was done |
| --- | --- |
| MA-01, MA-03 | The absence rule dates from 12 October; the pilot's error came with it in place; the audit of 13 October fixed it. W-20's date corrected |
| MA-06 | "A map close to the one you propose": frozen, waiting for the founder's review, with its own gaps |
| MA-10, MA-43 | W-08 and W-15 named; W-21 folded into W-08, whose mitigation is recorded as failed |
| MA-11 | The quoted words are the coordinator's framing, approved by the founder; the narrowing is in the rule (`METHOD.md`:212) |
| MA-15 | Choice 2 weighed the deduction variant and closed it with "never"; the evidence was not ignored |
| MA-16 | The 16 claims are listed in `M1-absence-claims.tsv` |
| MA-17 | The founder's remarks didn't require dropping the work; the consolidations were the coordinator's own |
| MA-18, MA-19 | Losses at each change, at least five; section 13 listed two stopped practices, but not these |
| MA-20 | Checkers are asked for missing evidence, but only for a record's claims |
| MA-24, MA-26 | The trial's areas were the coordinator's choice; A-24 run afterwards (8 concerns, nothing new); the 34 pilot-cited concerns of A-10, A-21 and A-22 not triaged, one of which (SA-C-145) bears on choice 2 |
| MA-28, MA-30, MA-31 | Partners' cases corrected in the report, D-001 and the glossary: the lender's repayment was already cited; apps' billing was in the Shopify study; Salla's financing collects from net Mada and card sales; dropshipping is `SAPI:64` only, shipping waybills are `STR:apps.json` |
| MA-41, MA-42 | 4b amends sections 6 and 7 in the same text; the checker names the slice |
| MA-45 | 4d triggers when one reference carries more than one variant, restoring the coexistence step |
| MA-47 | Choices 2 and 3 follow 4d since the revision of 25 October; the version sent said "never" |

**Applied, part two:** MA-52 (the third change checks coverage only at M8, against agent-written rows); MA-54 (coexistence's rulings listed as lapsing, the generality rule nowhere); MA-63 (the miss lay in A-03, A-12 and A-13, partly inside the subject's own areas); MA-65 (the area line had no reason given); MA-67 (the third change listed two stopped practices); MA-68 (management of change cited, its use here marked as interpretation); MA-69 ("the level it was planned for"); MA-70 (as MA-47).

**Open rows answered:**
- MA-32: the hour is marked as the coordinator's account.
- MA-35: the lineage holds: `caad5aa` (the study) to `9831536:studies/payment-seam/notes/shopify-crossings.md`:141, to `decisions/checks/D-002-D-003-review.md`:67 and D-003 at `b9ff59d`.
- MA-36: cited to `yemen-setup-options/report.md`:92.
- MA-37: two errors found, and a third issue's handling changed (the reading of B).
- MA-38: the pilot held Salla's financing (S01-SA-130, S01-SA-131).
- MA-39: 4a says what the search covers: the corpus search, whose header lists it, plus the structures that bear on the claim.
- MA-46: 4b stays at verification, where new claims are made (choice 2 came after framing); its cost is stated.
- MA-49: answered by `M1-absence-claims.tsv`.
- MA-56: `plan-change.md`:207 gives no reason.
- MA-62: the script is `method/decision_status.py`.
