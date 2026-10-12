# Subjects

One folder per subject of `PLAN.md` (Stages 2 and 4). A subject is a decision that would be expensive to change, phrased as a question. `S-01`, the pilot, is "who holds the merchant's funds between the buyer's payment and the merchant's payout?"

## How a subject runs

Each step has a brief in `<subject>/briefs/`. A separate agent inspects every brief before it runs. `method/check_subject.py` checks the files after every step.

| Step | Brief | Who | Writes |
| --- | --- | --- | --- |
| 1A. What each platform states | `A-one-platform.md` | one agent per platform, each blind to the others | `<platform>/statements.tsv`, `terms.tsv`, `absences.tsv`, `gaps.tsv`, `citations.tsv`, `notes.md` |
| Capture and kinds | none | the coordinator | captures the cited URLs with `method/capture/run.sh`; the checker writes `kinds.tsv` |
| 1B. Variation points and variants | `B-variation-points.md` | one agent | `variation-points.tsv`, `variants.tsv`, `notes-b.md` |
| 1A2. Gap-closing on the variation points | `A2-close-gaps.md` | one agent per platform | `<platform>/a2.tsv`, with additions to the phase A files |
| Capture and kinds, again | none | the coordinator | captures the URLs A2 cites; the checker rewrites `kinds.tsv` |
| 1B, second pass | `B-variation-points.md` | the same agent as 1B | updates `variants.tsv` |
| 1C. Cause, coexistence, what follows | `C-analysis.md` | one agent | `analysis.tsv`, `notes-c.md` |
| 2. The subject in each Yemen case | `D-yemen-marks.md` | one agent | `bears-on.tsv`, `yemen-marks.tsv`, `notes-d.md` |
| 3. The register entry | none | the coordinator | `entry.md`, in the decision-item form of `PLAN.md` section 5 |
| 4. Independent review | `F-review.md` | one agent that produced none of it | `review.md` |
| 5. Method report | none | the coordinator | `method-report.md`: what broke and what changed |

Step 2 needs Stage 1's `studies/yemen-cases/`. Q3, placing the existing rows, runs once at close-out (`PLAN.md` section 11), so no subject places them.

## Checking

```
python3 -I method/check_subject.py studies/subjects/<subject> OUT [CAPTURE_RUN ...]
```

It writes `OUT/subject-issues.tsv`, `OUT/subject-quotes.tsv` and `OUT/urls-to-capture.json`. It also writes `<subject>/kinds.tsv`, each statement's and each absence's kind by the rules of `method/source_kinds.py`.

Issues are graded:
- **error:** must be fixed;
- **pending capture:** a live page not yet captured;
- **review:** for the coordinator to look at.
