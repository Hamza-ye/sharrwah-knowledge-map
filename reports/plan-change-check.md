# The plan change of 29 October: an independent reading

**What this is:** a reading of commit `9cba3217`, the founder's intent recorded and folded, for contradictions before anything builds on it. The reader is an agent that made none of the change.
- **Read whole:** `founder-decisions.tsv`, `PLAN.md`, `CLAUDE.md`, `STATE.md`, the two founder messages of 29 October, `studies/class-model/briefs/B-extent.md` and `studies/class-model/seed/README.md`.
- **Read for single checks:** `reports/intent-review.md`, `reports/S-02.md`, `studies/class-model/inspection-A.md`, `questions/Q3-placing-rows.md`, `studies/subjects/S-01/briefs/E-rows.md`, `method/check_surface.py`, the scripts that read other-product-class, and Q1's `matches.tsv` and `citations.tsv`.

**How it was done:** nothing was changed except this file, and nothing was committed. Counts come from `python3 -I` scripts, and a judgement of mine is marked **Reading**.

**Line numbers and rows:**
- Line numbers are at `9cba3217`.
- The branch moved to `7920f912` while I read. Its two new commits touch only `reports/S-02.md` and `studies/subjects/S-02/`, so every finding holds there too.
- Rows of `founder-decisions.tsv` are named by their line, line 1 being the header:
  - line 26 is the intent, the go's "Row 1";
  - line 27 is architecture;
  - line 28 is quality.

**Counts:** 26 findings: 15 must fix, 11 optional.

## Summary

| # | Finding | Where | Verdict |
| --- | --- | --- | --- |
| 1 | Step 5 still sends vendor choices, expensive to change, to the founder. The intent makes "which shape is better" engineering's | `PLAN.md` 305-307 | must fix |
| 2 | Decision 1's "building or switching on either is the founder's decision" isn't carried, while section 3 now gives everything off the founder's list to engineering | `PLAN.md` 44, 63-66 | must fix |
| 3 | The seed's questions are "leads" in the plan but left out by the brief. As leads they would steer the model they then check, against section 11's own claim | `PLAN.md` 205 | must fix |
| 4 | Section 1's product-gap rule tests "only one market", not "the class doesn't meet" | `PLAN.md` 18 | must fix |
| 5 | Q3 still runs "once, at close-out" in sections 2 and 6, and section 6 still reads the founder lane | `PLAN.md` 35, 350 | must fix |
| 6 | Section 2 keeps Q1's matches "only as hints". The brief makes them joins, and section 11 doesn't list it | `PLAN.md` 36 | must fix |
| 7 | G2 still has the founder mark what Sharrwah "won't do", and Stage 3 isn't marked done | `PLAN.md` 165, 235, 246 | must fix |
| 8 | Section 11 doesn't list three removals, and nothing now keeps an area's architecture from binding a subject not yet run | `PLAN.md` 554-566 | must fix |
| 9 | `CLAUDE.md` describes a clone of other-product-class that this machine doesn't have, and removes the only setup step. `STATE.md` still reads it from the branch | `CLAUDE.md` 9; `STATE.md` 26, 122 | must fix |
| 10 | The rule for which gaps to pursue still serves subjects only, and S-02's decisions in `STATE.md`. The founder said: judge them against this decision | `PLAN.md` 37, 98; `STATE.md` 27 | must fix |
| 11 | The extent's brief has been rewritten twice since its last inspection, and would run without the inspection section 3 requires | `PLAN.md` 79; `STATE.md` 122-124 | must fix |
| 12 | The extent's budget of 250 million has no rule for an overrun, since sections 5 and 8 name subjects only | `PLAN.md` 215, 265, 378 | must fix |
| 13 | Risk 1 and the checkers reject rows tied to no subject, which is what the model's rows are | `PLAN.md` 356, 88 | must fix |
| 14 | The safe shore still places every question row against a subject | `PLAN.md` 24 | must fix |
| 15 | The surface checker now flags the new lines of `CLAUDE.md` and `PLAN.md`, and it was already failing before the change | `method/check_surface.py` 21, 31, 45 | must fix |
| 16 | G4 asks the founder to accept "the model", which is wider than the "model's extent" the founder approved | `PLAN.md` 227, 238, 249 | optional |
| 17 | GM is a gate with nothing to decide, against "nothing reaches the founder without a decision attached" | `PLAN.md` 237, 53, 364 | optional |
| 18 | In line 26, the founder's closing sentence reads as part of the coordinator's line (4) | `founder-decisions.tsv` 26 | optional |
| 19 | Lines 27 and 28 cite "the review, which proposed the added lines", not the S-02 page they answer | `founder-decisions.tsv` 27, 28 | optional |
| 20 | Each area's design weighs shapes with no criteria. The quality order, regional fit, section 14's hypothesis and the scale bands aren't in the plan, and "care" is unordered | `PLAN.md` 214 | optional |
| 21 | Stage 4A doesn't say who computes each capability's kind and count, which domains get parts, or when S-01's and S-02's points land. `STATE.md` skips the extent's review | `PLAN.md` 21, 204-213; `STATE.md` 122-128 | optional |
| 22 | "Depth over speed: bring it back when a second market is near" is in no working file | `STATE.md`; `PLAN.md` section 8 | optional |
| 23 | Section 2 still grounds Q1's "done" in "scoping by what will be built" | `PLAN.md` 32, 423 | optional |
| 24 | The seed's README cites the review for the founder's words, and puts MTH-04 under the intent | `seed/README.md` 3, 8 | optional |
| 25 | `HISTORY.md` has no baseline for the intent | `HISTORY.md` | optional |
| 26 | Step 2 ran before the handover, though the founder's answer was a fresh session after step 1 | `STATE.md` 121-122 | optional |

## What holds

**Line 26 holds the founder's text exactly.**
- **The handoff's text.** The handoff quotes the decision at its lines 20-26. Drop the bold on "Sharrwah" and join its four paragraphs with spaces, and it is the opening of line 26's decision, character for character, by a script comparison.
- **The four added lines.**
  - Lines (1) and (4) are the go's text (go lines 9-10). Line (4) carries the pointer before its full stop, as the go asks: "Point to its row; don't restate it".
  - Lines (2) and (3) are the review's section 10 lines (188 and 190), which the go accepted: "Section 5's additions: all, as edited above".
- **The marking** is what the go's edit 3 asks: "Added on review, in the coordinator's wording, which the founder accepted, with the founder's edits to the first and the fourth". Finding 18 is the one exception.
- **The pointer resolves.** At `537ddb77`, `founder-decisions.tsv` line 25 is the 28 October row, identical to line 25 today. The commit is on `origin/claude/vibrant-meitner-oh70v4`.

**Lines 27 and 28 carry the go.**
- Line 27 carries "go, at 250 million. Step 4 starts once its report has come to me". Step 4 in the review's table (line 114) is architecture.
- Line 28's order is the S-02 page's (`reports/S-02.md`, lines 43-47).

**Three of the leftovers the brief for this check named are gone:**
- G3 holds the founder's list (lines 236, 247);
- step 5 no longer makes a product gap the founder's (line 309);
- the design no longer waits for G4 (lines 28, 227).

Two remain: Q3 "once" (finding 5) and the founder's "scope" (finding 7).

**The go's other asks are carried:**
- the dry run's review checks every placement (`STATE.md` line 124);
- the orientation page is updated at each milestone and before anything is routed to the founder (`PLAN.md` line 398; `STATE.md` lines 39 and 128);
- the check for what the model misses has a time (lines 212, 220).

**No script needs the mirror branch.**
- These scripts read the path `/home/user/other-product-class`, or the variable `OTHER_PRODUCT_CLASS`:
  - `method/check_subject.py` line 36;
  - `corpus_search.py` line 41;
  - `check_register.py` line 22;
  - `quote_check.py` line 256;
  - `source_kinds.py` line 166.
- Stage 4A's extent doesn't read other-product-class at all. Q1's citations for Zid (1,087), BigCommerce (481) and WooCommerce (1,466) name live pages and the WooCommerce release, and none names other-product-class. This is a count over each platform's `citations.tsv`.

## Findings

### 1. Step 5 still sends vendor choices to the founder (must fix)

- **Where:** `PLAN.md` lines 305-307, section 6, the test form's step 5.
- **Problem:** the rule reads "vendor choice or business model: if expensive to change, the founder decides, on a recommendation".
  - By step 3's own definition (line 287), a vendor choice is "platforms in the same market differ". That is which shape is better where the references differ.
  - Section 3 now gives that to engineering (line 65). So does line 26: "Engineering establishes ... which shape is better where they differ ... Everything else is engineering's".
  - From S-03 on, every subject would again turn vendor choices into founder items.
- **Evidence:**
  - This rule produced S-02's "142 founder items, in 90 wordings" (`STATE.md` line 92). The re-status after this commit had to turn them into engineering's rulings (`7920f912`).
  - Stage 4, line 180 ("which of the founder's items depend on which"), follows from it.
- **Fix:** reword step 5:
  - vendor choice, expensive to change: engineering's ruling, with its reason, listed for the founder's veto;
  - business model: the founder decides where it touches the founder's list (plans and prices, or a service Sharrwah's own company operates); otherwise, engineering's ruling;
  - either, cheap to change: left to the build.

  Line 180 then reads "which of the founder's items and engineering's rulings depend on which".

### 2. Decision 1's building clause isn't carried, and section 3 now gives everything off the founder's list to engineering (must fix)

- **Where:** `PLAN.md` line 44 (the guard) and lines 63-66 (not the founder's to settle).
- **Problem:**
  - Line 44 carries only the guard's "goes live".
  - Lines 63-66 give engineering "everything not on the founder's list", including "how the platform keeps room for what is not built yet".
  - Building A or B, that is, filling the holder's ledger that E2 leaves empty under C, is on no list in section 3. As written, it is engineering's. Line 16 says it is the founder's.
- **Evidence:**
  - Line 16 (25 October): "A and B stay off: building or switching on either is the founder's decision (the guard)".
  - Line 8 (18 October): "Whether the design provides for either arrangement is for the work to recommend ..., and for the founder to decide". Line 19 (26 October) settled it: keep room.
  - Line 26 says "Everything else is engineering's", and its line (2) "The platform's capabilities for each remain the class's". It adds: "where an earlier decision differs, this one holds".
  - The handoff, line 43: "Don't: reopen Decision 1 or the guard". The review, line 89: "Decision 1, the guard and 26 October's room for A and B are all kept."
  - **Reading:** a session reading only the four files can let line 26's "where an earlier decision differs" override line 16, because the "Don't" is only in the basis.
- **Fix:** in section 3, item 2, after the guard, add: "Decision 1 (25 October) stands as recorded: A and B stay off, and building or switching on either is the founder's decision. The room for both is the founder's decision of 26 October (E1, E2). The intent of 29 October reopens neither (the founder's handoff: 'Don't reopen Decision 1 or the guard')."

### 3. The seed's questions: the plan calls them leads, the brief leaves them out, and section 11 relies on them not steering the model (must fix)

- **Where:** `PLAN.md` line 205, against `B-extent.md` line 15 and `PLAN.md` lines 212 and 566.
- **Problem:**
  - Line 205 says the seed's questions "are leads, never answers". The brief says "Leave out the seed's questions".
  - They are the Knowledge Map's 179 questions, the same rows that the check for what the model misses places against the model (line 212).
  - Section 11 moves Q3 on the ground that the rows can't steer: "the rows check the model only after its extent is built from the evidence, so they still can't steer it" (line 566). If line 205 is followed, that claim is false and the check is partly circular.
- **Line 205's index doesn't match the brief either.**
  - The index is "41 areas, its kinds and its source types", but the brief reads only `km-areas.tsv`.
  - The kinds are a column of the questions (`seed/README.md` line 14), so they go with them, and so does the timing the handoff named (line 33).
  - No brief reads `km-source-types.tsv`.
- **Evidence:** `inspection-A.md` finding 8 (line 192): "The seed's questions pre-answer an unclear candidate and bring in a kind the brief doesn't have". Its fix (line 206): "Hold back `km-questions.tsv`". The brief followed it; the plan didn't.
- **Fix:**
  - Line 205: "**The seed.** The Knowledge Map's 41 areas, with Shopify's and Salla's own groupings (`studies/class-model/seed/km-areas.tsv`), as the index. Its questions, with their kinds and timing, are left out of the extent's parts: they are its check at the end."
  - Then either fold `km-source-types.tsv` into the brief, as the review proposed (line 48), or drop "its source types".

### 4. Section 1's product-gap rule uses a different test from the decision's (must fix)

- **Where:** `PLAN.md` line 18, last sentence. It is in the frame (section 9, line 387).
- **Problem:** the plan says "A need only one of the founder's markets shows is a product gap". Line 26's line (1), in the founder's own edit, says "A need one of my markets shows that the class doesn't meet is a product gap".
  - The plan's test is how many markets show the need. The decision's test is whether the class meets it.
  - Under the plan's wording, a need that one market shows and the class meets would go to that market's setup, though the class's capabilities belong to the platform.
  - A need that two markets show and the class doesn't meet would be no product gap at all.
- **Evidence:** the go, line 9. Step 5, line 309, says it the decision's way: "that no reference meets".
- **Fix:** "A need one of the founder's markets shows that the class doesn't meet is a product gap: building it goes with that market's setup, and it never defines the platform. How the platform keeps room for it is engineering's."

### 5. Q3 still runs "once, at close-out", and section 6 still reads the founder lane (must fix)

- **Where:** `PLAN.md` line 35 (section 2) and line 350 (section 6, "Q3's rows"). Also `studies/subjects/S-01/briefs/E-rows.md` lines 3 and 42-43, and `questions/Q3-placing-rows.md` line 3.
- **Problem:**
  - Line 35: "Q3 runs once, at close-out. It reconciles the existing rows against the finished register (Stage 5)."
  - Line 350: "They are reconciled once, at close-out, and read only for their `id`, `question`, `needed_by` and `lane`."
  - Stage 4A (line 212) and Stage 5 (line 220) now run Q3 first at the end of the model's extent, and section 11 says it moved (line 566). The go named this exact text: "the plan still runs Q3 once, at close-out" (go line 13).
- **Line 350 has two more problems.**
  - It says the rows are "held outside the working files". The 179 questions are now in `studies/class-model/seed/km-questions.tsv`, without `lane` (`seed/README.md` line 14).
  - It reads `lane`, which the handoff says not to take: "Don't take its founder lane" (line 33). Q3's only brief flags a time bomb from the lane: "its `lane` is `founder`, and `who_answers` has no `founder decision`" (`E-rows.md` line 42).
- **The inputs are stale too.**
  - `E-rows.md` line 3 says "Held for Stage 5. Since 12 October 2026, Q3 runs once, at close-out". It places rows against a subject's variation points, not against the model.
  - Q3's own status line says "`PLAN.md` runs it per subject, with step 3 at close-out", which has been stale since 12 October.
  - `method/check_surface.py`'s allowances give the same reason (lines 45, 62).
- **Fix:**
  - Line 35: "Q3 first runs at the end of the model's extent, as its check for what the model misses (Stage 4A), and again at close-out where the register has changed what it covers (Stage 5). The rows never feed the model's or a subject's analysis."
  - Line 350:
    - the same timing;
    - where each set is held: the 179 questions also in the seed, the 81 payment rows at the pinned link;
    - `lane` read only as the row's old label, never as who decides; "asked of the wrong party" is judged against section 3's list.
  - Mark `E-rows.md` and Q3's status line as replaced, for Stage 4A, by a brief that places the rows against the model.

### 6. Section 2 keeps Q1's matches "only as hints", and the brief Stage 4A names makes them joins (must fix)

- **Where:** `PLAN.md` line 36, against `B-extent.md` lines 20 and 27.
- **Problem:**
  - Line 36: "Retired: the 84 unclear matches, unreviewed. The 88 matches stay only as hints for scoping."
  - The brief has every part read `matches.tsv` and `unclear-matches.tsv`, "with their `note` columns" (line 20). It also says "Q1's matches are such joins" (line 27).
  - Section 11's entry doesn't list the change.
- **Evidence:**
  - Some of the 88 rest on one shared term. One match's `basis` is SH-C-013 platform_terms "General" | SA-C-002 platform_terms "General" (`studies/concern-map/matches.tsv`).
  - Stage 2 records that matching by words failed in the pilot (line 133, U-027).
  - `inspection-A.md`'s disposition (line 714) makes the unclear list engineering's under the intent. That reached neither section 2 nor section 11.
  - **Reading:** a match on a word alone, taken as a join in the anchor, sets a capability's grain before the dry run's review sees it.
- **Fix:** either of two.
  - The brief: "Q1's matches are hints: a join is made only on the platforms' own terms, identifiers or definitions, re-read and cited; the unclear list is leads."
  - Or section 2 says the matches serve as the anchor's joins, and the unclear list as leads for engineering's rulings. Section 11 then says what that removes, and that the dry run's review checks every join.

### 7. G2 still has the founder mark what Sharrwah "won't do" (must fix)

- **Where:** `PLAN.md` line 165 (Stage 3), line 235 (the gate table) and line 246.
- **Problem:** line 165 reads "The founder marks business scope: what Sharrwah certainly won't do, and what it must. Nothing else."
  - Under line 26, "Sharrwah rules out nothing the class shows", and narrowing "needs a decision of mine or an engineering reason with evidence".
  - The handoff's item 1: "'what Sharrwah will and won't be' ... are no longer mine, except where they touch a choice listed above" (line 29).
  - Section 11 itself says the founder's "scope" is reassigned (line 563).
  - Stage 3 isn't marked done, so G2 reads as a live gate for any later change to the subject list.
- **Evidence:** G2 was answered on 26 October: "Evidence for all ten" (line 18; `STATE.md` line 11).
- **Fix:**
  - Mark Stage 3 done: "G2 answered on 26 October: evidence for all ten".
  - Restate G2 in the three places: "A change to the subject list is engineering's, under the narrowing test. Only what touches the founder's list goes to the founder."

### 8. Section 11 doesn't list three removals, and one leaves a risk with no control (must fix)

- **Where:** `PLAN.md` lines 554-566.
- **Problem:** section 9 (line 386) asks each change to list what it removes or weakens, with the risk that part controlled. The entry misses three removals:
  1. **The product gap as "a design decision for the founder"** (step 5, before the change). It is under "Changed" (line 559), not under what the change removes. The founder no longer decides whether the platform provides for a need the class doesn't meet.
  2. **"Then the design of the first version starts, under its own plan"** (section 1), and G4's "start the design" (Stage 5 and the gate table).
     - Architecture now runs inside this plan: after GM, beside subjects not yet run (lines 28, 214, 227). Neither "Changed" nor the removals say so.
     - The old order controlled one risk: an area's architecture binding what a subject not yet run decides.
     - **Reading**, from the subject list:
       - the orders area before S-09, "What currency fills prices, orders and records";
       - identity and stores before S-08, "Where data lives";
       - identity and stores before S-03, "the contracting company", which is on the founder's list.
     - Nothing in Stage 4A says how that risk is held now.
  3. **"its business model"** was in section 3's old item 1: "Scope: what Sharrwah will and won't be, its business model, and which markets come after Yemen". The new list names plans and prices and the services, not the business model. Step 5 still sends business-model variants to the founder (finding 1).

  It also doesn't name two minor additions: the safe shore's item 4 and section 9's reports both gain engineering's rulings for veto.
- **Fix:**
  - Add the three removals, each with its risk and whether that risk is reassigned or accepted.
  - For the second, add a holding rule to Stage 4A, for example: "An area's architecture keeps open, and names, each variation point that a subject not yet run could bind. It binds one only after that subject's G3."

### 9. other-product-class: `CLAUDE.md` describes a clone this machine doesn't have, and says nowhere how to get one (must fix)

- **Where:** `CLAUDE.md` line 9; `STATE.md` lines 26 and 122.
- **Problem:** `CLAUDE.md` says "It is the founder's repository `Hamza-ye/other-product-class`, cloned read-only at `/home/user/other-product-class`".
  - **On this machine, that path is the old mirror.** Its `.git` file points to `/home/user/sharrwah-knowledge-map/.git/worktrees/other-product-class`, and its origin is this repository. `git worktree list` shows it as a detached worktree at `0d79b794`, the tip of `origin/evidence/other-product-class`.
  - **The setup step is gone.** The command that made the worktree was removed, and nothing replaces it: no clone, no access step and no fallback.
  - **Access already failed once.** S-02's method report (line 723) records why the mirror existed: "this session's GitHub access couldn't reach the new repository".
  - **The founder asked about this.** The go (line 23): "i do not know how the other session will get access to the repositories".
  - **`STATE.md` contradicts the new `CLAUDE.md`.** Line 26 still says this session reads other-product-class "from this repository's branch `evidence/other-product-class` (`CLAUDE.md`)". Line 122 says the fresh session reads all three repositories "from their own repositories", without saying how.
  - **The sentence breaks.** After the insertion, "...so a citation at either holds; and the WooCommerce release ..." joins the release to the branch's sentence.
- **Evidence:**
  - The branch holds `3f2438f3` and `0d79b794`, the commits `STATE.md` cites (`git merge-base --is-ancestor`).
  - **Reading:** this doesn't block the extent, since Q1 cites no other-product-class file (What holds). It does block the subjects, and checking a candidate miss against held evidence.
  - A fresh container also needs three more sources, and `CLAUDE.md` gives their paths but not how to get them:
    - observed-sh and observed-sa, clones here of `Hamza-ye/observed-sh` and `Hamza-ye/observed-sa`;
    - the WooCommerce release, whose folder `evidence/product-class/woocommerce-11.2.1/` holds its checksum and `plugin-info.json`.
- **Fix:** in `CLAUDE.md`:
  - For each of the four sources, say how a session gets it read-only: attach the repository and clone it to its path, or point the scripts' variable (such as `OTHER_PRODUCT_CLASS`) at a copy. For the release, fetch it and check its checksum.
  - Give other-product-class's fallback: this repository's branch, up to `0d79b794`, with the same commit ids, through the old worktree command. Say that a citation after `0d79b794` needs the founder's repository.
  - Put the release in its own clause.

  In `STATE.md` line 26, use the past tense: "read then from the branch; now as `CLAUDE.md` says".

### 10. The rule for which gaps to pursue wasn't widened to the model (must fix)

- **Where:** `PLAN.md` lines 37 and 98; `STATE.md` line 27.
- **Problem:**
  - Line 37: "Gaps are closed only where a subject needs them."
  - Line 98: "No new concerns, statements or gaps go into the five platform folders unless a subject needs them."
  - `STATE.md` line 27: "a gap is pursued only if closing it could change an S-02 decision".
  - The founder's answer of 29 October: "Judge them against this decision, not only S-02's" (handoff line 41). The review: "widened to 'could change the model or a decision'" (line 58).
  - Stage 4A's check has each candidate miss "checked against the evidence" (line 212), which line 37 doesn't allow unless a subject needs it.
- **Fix:**
  - Line 37: "Gaps are closed only where the model or a subject needs them".
  - Line 98: the same, or say that the model's candidates are checked against held evidence and recorded in the model, not in Q1's folders.
  - `STATE.md` line 27: add the answer of 29 October.

### 11. The extent's brief would run without the inspection section 3 requires (must fix)

- **Where:** `PLAN.md` line 79; `STATE.md` lines 122-124.
- **Problem:** line 79 says "Before a brief runs, a separate agent reads it for anything that presupposes the answer (inspection: Fagan 1976)". `STATE.md`'s next steps start with the dry run, with no inspection.
  - The brief in its present form hasn't been inspected. The re-inspection read `B-extent.md` at `79ae9c27` (`inspection-A.md` line 470). The brief was then rewritten twice, according to `git log`:
    - `a1ddbf87`: one brief;
    - `a55fc022`: two passes.
  - The coordinator's disposition chose a dry run reviewed on its output instead (`inspection-A.md` lines 684-715). Neither Stage 4A nor section 11 says that the dry run stands in for the inspection.
- **Fix:** either of two.
  - Add "an inspection of `B-extent.md` as it now stands" before `STATE.md`'s step 3.1.
  - Or state in Stage 4A that the dry run, reviewed on its output, stands in for the inspection, and list that in section 11 as a weakening.

### 12. The extent's budget has no rule for an overrun (must fix)

- **Where:** `PLAN.md` line 215; lines 265 and 378.
- **Problem:** Stage 4A sets 250 million agent tokens, the founder's figure (line 27). The overrun rules name only a subject's budget.
  - Line 265: "each subject's budget ... an overrun by a quarter is reported to the founder (section 8)".
  - Line 378: "A subject runs past its budget by a quarter".
  - The founder's decision behind them is "A standing decision for every subject" (line 23).
- **What a fresh session can't tell:**
  - whether to stop at 250 million, re-plan, or report at 312.5 million;
  - whether the check for what the model misses and the extent's independent review are inside the 250. The review's sizing (line 113: "170 to 240 million, budget 250") predates the check, which its section 12 added (line 230).
- **Fix:**
  - Line 378: "A subject, or the model's extent, runs past its budget by a quarter". Line 265 the same.
  - Stage 4A: say which steps the 250 million covers.

### 13. Risk 1 and the checkers reject what the model is for (must fix)

- **Where:** `PLAN.md` line 356 (risk 1) and line 88.
- **Problem:**
  - Risk 1 reads "The analysis grows past what decisions need | A row or file tied to no subject ... | The checker rejects untied rows; growth goes to the next gate".
  - Line 88 says the checkers enforce that "every row is tied to a subject".
  - The model holds what no decision needs, by design: "Every concern of every platform lands once, so the model stays the union of the class" (line 210). Line 26: "Its extent comes from the class, not from the launch".
  - Its rows are tied to areas, not to subjects.
- **Fix:**
  - Scope risk 1 and line 88 to the subjects.
  - Add a risk for the model, held by its budget, by breadth first and by the dry run's checker. Examples: depth growing before GM, or a capability with no citation.

### 14. The safe shore still places every question row against a subject (must fix)

- **Where:** `PLAN.md` line 24.
- **Problem:** item 3 reads "every existing question row is placed against a subject, or listed as unplaced with its reason".
  - Q3 now places the rows against the model (line 212), and at close-out runs again only "where the register has changed what it covers" (line 220).
  - A row that the model covers and no subject reaches would leave item 3 unmet. Only a full re-run at close-out would meet it, and Stage 5 now says there isn't one.
- **Fix:** "every existing question row is placed against the model or a subject, or listed as unplaced with its reason".

### 15. The surface checker now fails on `CLAUDE.md` and `PLAN.md` themselves (must fix)

- **Where:** `method/check_surface.py` lines 21 and 31 (its terms) and line 45 (an allowance). It flags `CLAUDE.md` line 14, `PLAN.md` lines 205-206 and `founder-messages/2026-10-29-intent-handoff.md` line 33.
- **Problem:** risk 14's guard (line 369) searches the working files for history's framings. I ran it on clean exports of `48bde100` and `9cba3217`: the hits go from 128 to 132.
  - **The four new hits.**
    - The pattern `\bmodel/`, for "the obligation model", matches `class-model/` in `CLAUDE.md` line 14 and `PLAN.md` lines 205-206.
    - The patterns `register/` and `km-questions`, for "the Knowledge Map", match the handoff's line 33.
  - **The stale allowance.** `PLAN.md`'s allowance still reads "Q3's rows, agreed at G0 and read once at close-out".
  - **It was failing already.** For example, S-02's ids S02-M1 to S02-M8 match "the milestone reports". As it stands, it can't tell history returning from today's files.
- **Fix:**
  - Narrow the pattern, for example `(?<![\w-])model/`.
  - Allow the Knowledge Map's terms in `founder-messages/` and `studies/class-model/`, each with its reason, and update the stale reasons.
  - Clear the earlier false positives, so the checker passes before Stage 4A builds on the change.

### 16. G4 asks the founder to accept "the model" (optional)

- **Where:** `PLAN.md` lines 227, 238 and 249.
- **Problem:** G4 reads "The founder accepts the register and the model".
  - Section 3 makes the class's model engineering's, with the founder's veto (lines 63-68).
  - Line 13 (25 October): the founder "is not asked to audit lists of practices or decisions".
  - The review the founder approved said "G4 accepts the model's extent and the register" (review line 218). That is narrower than "the model", which by G4 holds the detail grown area by area.
- **Fix:** "accept the register and the model's extent; engineering's rulings on the model's detail come listed for veto".

### 17. GM is a gate with nothing to decide (optional)

- **Where:** `PLAN.md` line 237; lines 53 and 364.
- **Problem:**
  - Under "What the founder decides", GM's row reads "Its report, with engineering's rulings for veto. Architecture starts after it".
  - Line 53: "Nothing reaches the founder without a decision attached". Risk 9: "each gate brings only decisions".
  - A session could hold architecture back waiting for an answer. Line 27 says "Architecture starts once the extent's report has come to the founder".
- **Fix:**
  - GM's row: "The extent's report, with engineering's rulings for veto: nothing to decide. Architecture starts once it has come to the founder."
  - Make line 53 and risk 9 except reports and veto lists.

### 18. Line 26: the founder's closing sentence reads as part of the coordinator's line (4) (optional)

- **Where:** `founder-decisions.tsv` line 26, the decision column, after "(4) ... #L25)."
- **Problem:** the sentence "It takes in the scope decision of 28 October; where an earlier decision differs, this one holds." is the founder's own, from the handoff's instruction (line 18), outside the quoted decision. It comes after the line the row marks as the coordinator's wording, so it reads as part of (4).
- **Evidence:** the rest of line 26 is as asked (What holds).
- **Fix:** move the sentence to just after the verbatim text, before "Added on review", and mark it as the founder's: "(From the founder's handoff:) It takes in ...".

### 19. Lines 27 and 28 cite a basis that doesn't fit them (optional)

- **Where:** `founder-decisions.tsv` lines 27 and 28, the basis column.
- **Problem:** both repeat line 26's "the coordinator's review, which proposed the added lines: reports/intent-review.md, sections 5 and 10". Neither row has added lines.
  - The proposals the founder answered are on the S-02 page, which neither row cites: architecture alongside the subjects, and the order of qualities.
  - On that page the order's first item reads "trustworthiness: money and data are never wrong, and each store is kept apart from the others" (`reports/S-02.md` at `9cba3217`, lines 43-47). Line 28 keeps the word and drops its meaning.
- **Fix:** cite `reports/S-02.md`, section 1, as what the founder answered, beside the review's sections 6 and 10.

### 20. What each area's design weighs isn't in the plan (optional)

- **Where:** `PLAN.md` line 214 (Stage 4A).
- **Problem:** line 214 reads "Where the references' shapes differ, each area's design weighs which is better, and states why". It names no criteria.
  - `PLAN.md` nowhere carries line 28's quality order, or line 25's regional fit and product quality. It holds no "quality", "trustworth" or "regional".
  - Two more things are only in the review:
    - the hypothesis the go asks each area's design to test (go line 12; review lines 252-267);
    - the scale bands engineering states until the founder's numbers come (review line 64; line 28: "Scale numbers come later").
  - Line 28 leaves "care", the sixth of line 25's qualities, unordered, as the S-02 page did (its line 43).
- **Fix:** add to the architecture bullet: "It weighs by the founder's quality order (line 28) and regional fit (line 25), tests the hypothesis in `reports/intent-review.md` section 14, and states scale bands as assumptions until the founder's numbers come." Say whether "care" is ordered.

### 21. What a fresh session would miss in Stage 4A (optional)

- **Where:** `PLAN.md` lines 21 and 204-213; `STATE.md` lines 122-128.
- **Problem:**
  - **The kind and the count.**
    - The safe shore's item 0 asks "how many establish it as their own" (line 21), and section 6 defines the kinds. The brief records neither.
    - Only `inspection-A.md` (line 712) says they "are computed by the coordinator from the cells after the merge, by one rule applied to all", and it gives no rule.
  - **Which domains get parts.**
    - The seed's domain H, "Beyond the references" (WLD, ENG, INT, MTH), holds the old founder-lane areas.
    - The disposition's "Areas beyond the references take no capabilities" (`inspection-A.md` line 695) is in neither the brief nor the plan.
  - **The extent's independent review** (line 213) isn't among `STATE.md`'s steps 3.1 to 3.6.
  - **S-01's and S-02's variation points** "land in the model's areas" (line 204), but no step says when.
- **Fix:**
  - Add a Stage 4A bullet on the rule for the kind and the count, and on which domains get parts.
  - In `STATE.md`, add the independent review before step 3.6, and say when S-01's and S-02's points are landed.

### 22. "Depth over speed" has no working file to come back from (optional)

- **Where:** `STATE.md`; `PLAN.md` section 8.
- **Problem:** the founder said "Depth over speed: not decided. ... Bring it back when a second market is near" (handoff line 45). It is rightly not a row. But no working file carries it, and `reports/S-02.md`, which held it, is now marked replaced.
- **Fix:** add one line to `STATE.md`'s open items, or a trigger to section 8: "when a second market is near, bring back 'depth over speed'".

### 23. Section 2 still grounds Q1's "done" in scoping by what will be built (optional)

- **Where:** `PLAN.md` line 32, and line 423 (Schmid 2002: "Scoping by what will be built").
- **Problem:** section 2 says "Known practice scopes analysis by what will be built and by risk".
  - **Reading:** next to line 26's "Its extent comes from the class, not from the launch", this can be read as scoping by the launch.
  - The model now covers every concern (line 210). What is scoped is each subject's depth.
- **Fix:** "Known practice scopes each subject's depth by risk; the model's extent is the class's (Stage 4A)."

### 24. The seed's README attributes to the founder what is the review's (optional)

- **Where:** `studies/class-model/seed/README.md` lines 3 and 8.
- **Problem:**
  - Line 3 cites the review's section 8 for "The founder gave it as a seed". The founder's own words are now saved: the handoff's item 5 (line 33).
  - Line 8 puts MTH-04 under "the founder's intent". The handoff names INT-02, INT-03, MTH-01 and ENG-02 (line 33). MTH-04 is the review's reading (line 141).
- **Fix:** cite `founder-messages/2026-10-29-intent-handoff.md`, item 5, and mark MTH-04 as the coordinator's reading.

### 25. `HISTORY.md` has no baseline for the intent (optional)

- **Where:** `HISTORY.md`, the section "The reset of 25 October, and what followed".
- **Problem:** the table ends at "G2 answered" (`4787069`).
  - The intent changes the frame with the founder's go, as the reset did.
  - Neither the intent nor the decision points of 27 and 28 October has a row, though the file defines a baseline as "the commit at one of the founder's decision points".
- **Fix:** add a row for `9cba3217`, the intent recorded and folded, and one for the fixes that follow this reading.

### 26. Step 2 ran in this session, though the founder's answer was "a fresh coordinating session after step 1" (optional)

- **Where:** `STATE.md` lines 121-122.
- **Problem:**
  - The go (line 21): "A fresh coordinating session after step 1: yes".
  - In the review's table, step 1 ends with this reading (line 111). Its timing note says "I'd run steps 2 and 3 from a fresh coordinating session" (line 116).
  - `STATE.md`'s next steps put step 2, S-02's re-status, before the handover, as the review's section 12 does (line 227). Commits `40df4a3f` and `7920f912` ran it.
  - The founder's reason for a fresh session was the coordinating session's cost (review line 66).
- **Fix:** the work needs no change. Say in the next report that step 2 ran before the handover, and why.
