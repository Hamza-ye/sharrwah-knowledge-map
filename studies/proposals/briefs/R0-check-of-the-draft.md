# Brief: the check of the re-frame's drafts (step R0)

You check drafts you made none of, before their summary reaches the founder. The founder asked for this check in their G1 answer: "an agent that did none of the drafting checks the plan change, the first step's briefs, and the neutral wording of each section B question that later steps will give agents, against this message and against the recorded data, for whether they can work and what they will cost."

**Read:**
- this brief;
- the founder's G1 answer, `founder-messages/2026-10-18-g1-answer.md`, and the G1 rows of `founder-decisions.tsv`, which record its section A;
- the drafts:
  - `studies/proposals/plan-change.md`;
  - `studies/proposals/questions.md`;
  - `studies/proposals/briefs/R1-areas-one-platform.md` and `studies/proposals/briefs/R1-areas-review.md`;
  - `studies/proposals/sizing.md`;
  - `method/areas_extract.py`, `method/check_areas.py`, and the five extracts the first wrote, `studies/proposals/areas/extract-<platform>.md`;
- `PLAN.md`, the plan the change rewrites;
- the recorded data, as far as you need it to test a claim. Sample it; don't read it all:
  - the concern map, `studies/concern-map/platforms/<platform>/`: `inventory.tsv`, `concerns.tsv`, `statements.tsv`, `citations.tsv`;
  - the pilot, `studies/subjects/S-01/`: above all `method-report.md` (its section 12 gives what the pilot cost) and `entry.md`;
  - Stage 1, `studies/yemen-cases/`: `axes.tsv`, `states.tsv`, `cases.tsv`, `review-independent.md`;
  - the held sources the extracts cite, in `/home/user/observed-sh` and `/home/user/observed-sa`, at the commits the extracts give.

The founder's words are a statement of what the founder wants and decided. They are never evidence of what a platform does.

## What to check

### 1. The plan change against the founder's message

- **Every instruction is carried.** Go through the message's sections A and C and Part 2, sentence by sentence. For each instruction, find where the plan change carries it. Report any it drops, weakens or changes.
- **Nothing is added without saying so.** Report anything the plan change adds that the message doesn't ask for, unless the plan change marks it as the coordinator's own.
- **Every part of `PLAN.md` the message doesn't mention.** For each section and stage of `PLAN.md`, and each dated entry in its section 11, say whether the plan change keeps it, replaces it, or drops it, and whether it says so. The message names some of these: the close-out (Stage 5, with each of its parts), the checkpoints after each batch (G3), the Yemen study's pending fixes, and the old question lists (Q3's rows). Report each part whose fate the plan change leaves unclear.
- **Readings.** List each place where the plan change reads the message one way when it could be read another, and the choice changes a step, a cost or what reaches the founder. For each: the words, the reading taken, the other reading, and what the choice changes.
- **The plan stays coherent.** Report any place where a rewritten section conflicts with a section the change leaves standing, or names something the change removes (a subject, a batch, the test form, G3, G4, the register).

### 2. The neutral wording of each question

For each question in `questions.md`:
- **Neutral.** Does it use the founder's working words ("market", "availability", "conditions", "manual payment", "parts", or others from section B) as a category? Does it use one platform's own term as if it were everyone's? Does it fix the level at which something is set, or who sets it? Does its wording lead toward one answer, or toward the founder's expectation?
- **Covers its item.** Does it ask for everything the founder's section B item needs a proposal to answer? Name anything it leaves out.
- **Against the recorded data.** Sample the concern map's concerns and statements on at least two platforms that bear on the question. Would an agent given the question record them? Name recorded material it would miss, and material it would sweep in that bears on no item.

### 3. The first step's briefs, scripts and extracts

- **Can an agent do the task** with only what its brief names? Look for instructions that conflict, rules it can't apply, and an output it can't produce from its reading.
- **The extracts.** Re-run the script into your scratch directory, with `python3 -I method/areas_extract.py <scratch dir>`, and compare its output with the committed extracts. Check, on at least two platforms, that each extract holds the platform's lists from the concern map, its concerns, and its help menus where the brief says it does. Do legal matters, places and eligibility show for each platform, so that the runs can give them areas? Name anything an agent would need that isn't there.
- **The checking script.** Test `method/check_areas.py` on small areas files you write in your scratch directory, passing that directory as its second argument. Does it accept a correct file and reject the errors the brief says it checks? Report what it misses or wrongly rejects.
- **The size of the task.** Is 15 to 30 areas a reachable aim from each extract, given its numbers of lists, entries and concerns? Is placing every in-scope entry and concern by its id workable for the larger platforms within one short run?
- **The review brief.** Does it check everything the founder asked to come with the areas list: what a "won't do" mark removes, what evidence is kept anyway, what the work would leave out and why, and the depth chosen for each question?

### 4. What it will cost

- **The measures.** Check each pilot figure the sizing uses against `method-report.md` section 12, and its arithmetic. Some figures rest on the coordinator's reading of the session's transcripts, which you can't see: the per-run figures not in section 12, the week's limit and the usage window. For those, check that the sizing says where they come from, and that they agree with section 12 where they overlap.
- **The scaling.** For each step: is the pilot run it is sized from a fair match? Is the scaling shown, and does it hold? Is every run counted, including brief checks, audits, re-runs and re-checks, as the founder asked? The pilot re-ran several phases (section 12 says so). Say whether the sizing allows for re-runs, and what a fair allowance would be.
- **The volumes.** Test the sizing's volumes against the recorded data: how many recorded statements bear on each question, so that a script can copy them, and how many new statements each run would need. Use a rough count you can show.
- **The totals.** Does the plan fit about 2 billion agent tokens? If your figures differ from the sizing's, give yours, with the working. Are the cuts it offers real, and in the right order?
- **The calendar.** Do the share of a week's limit, the days and the calendar time follow from the figures?

## Output

Write `studies/proposals/check-of-the-draft.md`. Number its findings from 1. Each finding gives:
- **where:** the file and section;
- **the problem;**
- **the evidence:** the founder's words, the plan's words, or the data, quoted or counted;
- **the fix you propose;**
- **severity:**
  - `must fix`: a step can't work as written, the plan change drops or changes what the founder asked, a question isn't neutral, or a cost is materially wrong;
  - `optional`: anything else.

Then add three short sections:
- **The readings,** listed as section 1 asks;
- **Your cost figures,** step by step, where they differ from the sizing's;
- **A verdict:** whether the drafts, once the must-fix findings are fixed, can go to the founder in summary.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/` or the observed repositories.
- Write scratch files only in the scratch directory the message that started you names.
- Change no file in the repository except your output, and don't commit.
