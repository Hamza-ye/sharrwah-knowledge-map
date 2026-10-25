# The check of part three: what was done with each finding

The coordinator's record of the independent check of `reports/M1-evidence-and-model.md`, with its edits to D-002, D-003, `decisions/subjects.tsv` and amendment 4, at commit `8aebcde` (`M1-evidence-and-model-check.tsv`: 53 rows; 16 hold, 29 fix, 8 open). Each finding was tested against its evidence before it was applied (`METHOD.md` section 6). The check processed 3.0 million tokens in 22 requests (`method/count_tokens.py`).

**Counts:**
- 29 fixes: all verified, and applied, two of them in part (EM-28, EM-44);
- 8 open rows: answered below;
- no finding rejected.

**The evidence checked first:**
- **The seam's tagging of the model's rows:**
  - `8946887:studies/payment-seam/rows-tagged.tsv` has the 81 rows, PAY-01 to PAY-81;
  - `seam.md`:104–106: "Two taggers tagged the 81 rows independently from the first version of this file. … The rules below fill those gaps";
  - `caad5aa` (04:11 UTC) filed `register/pay-questions.tsv` with the model, before the seam's commits (`9831536` at 08:36, `8946887` at 09:44).
- **The reversal-twin chain:**
  - `A2-processor.md`:242 reads "Nearly every non-core type has a `_REVERSAL` twin.";
  - "38 are reversals" entered D-003 in `24961d6`, the Terms and Scope pass, and the terms inventory doesn't mention it.
- **The study's inferences:** 96 lines carry the word.
- **The model's visible header:** "payments study · read from Shopify's help center, developer docs and shipped schemas · 2026-10-09".
- **Section 13's heading:** "Kept as evidence and inputs, not as deliverables" (`METHOD.md`:391).
- **F-06's restored row** (`founder-decisions.tsv`:43): the founder's words are "payments be its own concern, with its own questions, research and pace". The line naming the seam's contract v0 as the first subject's starting draft is the coordinator's annotation.
- **The decision of 12 October** (`founder-decisions.tsv`:5): the 81 rows and the 179 questions "are agent-written and must not be taken as Sharrwah's requirements". It is never revoked.
- **Stage 1's brief** barred `yemen-setup-options/` (`studies/yemen-cases/brief.md`:194).

**Applied:**

| Finding | What was done |
| --- | --- |
| EM-03 | "about 90 passages marked as inference" |
| EM-06, EM-07, EM-08 | The chain starts at `A2-processor.md`:242. The seam's note made it absolute, cited at `8946887`. "Steps 2 to 4 each cited the agent before them" |
| EM-11 | Corrected by M1's Terms and Scope pass (`24961d6`), in parts one and three |
| EM-13 | The model came first: the seam tagged its 81 rows, and took its Shopify facts from the study and the engineering sources. Part three's "In short" and table, and part one's table |
| EM-14 | The visible header quoted, not the page's layout comment |
| EM-15, EM-16 | "At least four of the eight". The rows are S-01's, tagged by the seam, reconciled at M8 |
| EM-20, EM-21, EM-22 | Section 13 counts agents' writing as evidence; its not-safe list names the drafts and the seam's edition only; 4c moved to "Proposed with this" |
| EM-24, EM-25 | D-002 mostly applies its rule (D-002:193, :207). The coordinator's unchecked application of a reviewer's suggestion is named as the second cause |
| EM-26 | The order after ADD (Cervantes and Kazman 2016) and ATAM, with views sketched as decisions are made, then again |
| EM-27, EM-31 | D-001's drivers listed as they are. The subjects that hold D-002 and D-003: S-03, S-05, S-06, S-07, S-10, S-11 |
| EM-28 | In part, and differently. The report's reading is marked, and the boundary rests on both references' own words (glossary, *payments side*), not on F-06, after the founder's note of 25 October. D-001 doesn't take F-06 as given, and D-002 no longer does |
| EM-29, EM-32, EM-37 | The route put the seam's v0 first (section 14). The acceptance rule already covered the scenarios, and the gap was the two records' Scope. "One thing to decide": 4e. Section 14 is left as it is: it governed S-01 only, and D-002 took the contract as one option of three |
| EM-33, EM-34 | Evidence includes this repository's `evidence/`. The model is part of the description, not a separate artifact |
| EM-39, EM-41 | D-002 and D-003: "before M2's quality scenarios and the founder's targets existed"; D-003's Gaps name what holds D-002 |
| EM-44, EM-45, EM-46, EM-49, EM-50 | 4e rewritten: 2c widened to studies, notes, models and checks; section 13's heading relabelled; the level 2 and 3 checker confirms each fact resolves to a source, and a checker cites the source of any precedent it recommends. The "evidence repositories" restriction, which would have barred E030 to E036, is gone. EM-44 is moot in the rewrite |
| EM-51 | Part one's disposition of the study: "Candidates and pointers, never evidence" |

**Open rows answered:**
- **EM-18:** Stage 1 worked from the captured sources, including those the options cited, and its brief barred it from the options themselves. The options' own claims were never checked one by one. Part three says so.
- **EM-40:** applied. D-002's and D-003's S-02 items name the outcomes that could change them, and D-002's Confirmation holds the walkthrough.
- **EM-42:** D-002 is not added to D-001's or D-004's `depends_on`. D-001's reversal path is conditional, "if the payment boundary holds, which is still being proven (D-002)". The boundary rests on the references' evidence, not on F-06.
- **EM-43:** applied. The scenarios are written by an agent whose brief names neither D-002, D-003 nor the seam (`decisions/subjects.tsv` S-02; D-002, Confirmation).
- **EM-47:** moot. 4e now concerns agents' wording, not which company counts as "a platform". The sources Stage 1 quotes stay evidence.
- **EM-48:** applied. The script flag is dropped, and the check is left to the level 2 and 3 checker.
- **EM-52:** applied. The decision of 12 October is in part three's "Already covered".
- **EM-53:** applied as interpretation. PAY-73 is quoted as the question it is.
