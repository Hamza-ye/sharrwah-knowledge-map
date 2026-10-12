# Question rows: what they are

Two sets of questions that agents wrote before `PLAN.md`. **They are not Sharrwah's requirements.** Q3 and `PLAN.md` place them against the subjects, as inputs only, and each placement is read from its question text. Some may still be genuine questions. Their context is set out below.

| File | What it is |
| --- | --- |
| `pay-questions.tsv` | **The 81 payment rows, PAY-01 to PAY-81.** Earlier work expanded them while thinking about how to model payments. The founder's artifact "Obligation to Payout" (claude.ai/artifact/Af44iTiRyauqt7bhr8KrP8) shows them, and `model/obligation-to-payout.html` is a copy. |
| `km-questions.tsv` | **The Knowledge Map's 179 questions.** They were copied on 12 October 2026 from the founder's artifact "Sharrwah Knowledge Map" (claude.ai/artifact/Wj9kpisrCUiRUCmeCzRRZM, version 1791419535-9835). Their ids are prefixed `KM-`, because the map's PAY-01 to PAY-07 are different questions from the payment rows' PAY-01 to PAY-07. `km_id` keeps the original id. |
| `km-artifact-1791419535-9835.html` | The page as read, with sha256 `b7c82dc930e32139c26193cb234f87e23f8fa653d30c70d840f34d32b806a24d`. The rows were taken from its embedded data. |
| `pay-evidence-additions.tsv` | Evidence entries the payment rows cite. |

**Why they need care:**
- Agents wrote both sets from earlier, smaller states of observed-sh and observed-sa, at old commits.
- Their `evidence`, `pointers` and `other_sources` columns are not trusted, and no study cites them.
- A question can carry a frame or an answer inside it. Read as a requirement, it would steer the work.

So a brief that places rows reads only `id`, `question`, `needed_by` and `lane`.
