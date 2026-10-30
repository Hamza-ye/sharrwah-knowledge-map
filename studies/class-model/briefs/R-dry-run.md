# Brief: the dry run's review

**What this step is for.** An independent review of the class's model's dry run: domain B (catalogue and inventory), built by the parts `B-anchor` (Shopify and Salla), `B-woocommerce`, and `B-backfill-woocommerce` where it ran. You made none of it. You test it against the evidence, claim by claim, and try to refute it: report counter-evidence and missing evidence, not agreement. What you find sets the conventions and the checker's tests before the other domains run.

**Read:**
- `studies/class-model/briefs/B-extent.md`, the brief the parts followed;
- the parts' files in `studies/class-model/parts/B-*/`, with their `derived.tsv` and `notes.md`;
- the checker's output on each part: run `python3 -I method/check_class_part.py studies/class-model/parts/<part>` yourself, and read its flags;
- the counts and kinds: `python3 -I method/class_kinds.py --domain B --out -`;
- `studies/class-model/scope.tsv`, for the concerns it gives domain B and those that name B under `also`;
- the concern map, only through `python3 -I method/class_slice.py` (its `--help` lists the commands), never whole.

## What to check

1. **Every placement against all of the concern map's statements** for the concerns behind the cell, under all five of Q1's placements, not its `where` rows alone, and against the platform's other statements found by `search`.
   - In particular, take every cell whose `where` statements name only an app store, a marketplace or an extension category. Read the concern's `decides` statements, its plan lines, entitlements and settings, before accepting `extension-point`: a plan line or an admin route can show the platform doing it itself.
   - And every `core` that rests on API objects, scopes or webhook topics: does a statement show the platform doing it, or only apps doing it through the API?
2. **Each `supports` value against the brief's tests** for `core`, `own-service`, `extension-point`, `outside` and `shows`. A merchant's or buyer's responsibility is never `outside`. A product made by the platform's own company is `own-service`.
3. **Each join:** a Q1 match, terms, identifiers, a definition, or role. For a join on role, do both sides' cited definitions show the same thing? For a join on terms, is it the same object, or one word for two things? Every strained fit: should it be split?
4. **Each grain:** the capabilities cut finer or coarser than the concerns, their parents, and a coarse concern's statements cited in its children's cells.
5. **Each `none-held` cell:** search the platform's statements yourself, in every language they use. A statement that shows the capability makes the cell false.
6. **The areas:** is each capability's area what it is about, whatever channel delivers it?
7. **The rulings on Q1's unclear candidates:** does each ruling follow from the cited definitions?
8. **What the parts never cite:** statements of domain B's concerns that no cell cites. List those that bear on a capability, or on its placement.
9. **Qualities and slot fillers:** each one's value, scope and capability.
10. **The kind rule.** For each capability, is the computed kind what the evidence supports?
    - a `class` resting on a placement the statements don't support;
    - a `slot` that some platform's statements show in its core;
    - the `open` cases (a count of 0, with some platform `not-stated`): propose how the rule should treat them, and why.
11. **The conventions:** what the parts did differently from each other, or from the brief, and what the brief should settle before domains A and C to G run.

**Depth.** Check every cell whose kind hinges on one placement (a count of 0 or 1), every join on role, every strained fit and every `none-held` cell. Check the rest by a sample you state, with how you chose it.

## Rules

- **Evidence:** cite every finding by statement key, part file and line. Mark every judgement of yours as a **Reading**, and give counts from scripts you ran.
- **Change nothing** but your own file. Make no commits. Run Python with `python3 -I`.
- **Write as you go,** and keep your context small: print statements per concern, never load the concern map's files whole.

## Output

`studies/class-model/review-dry-run.md`:
- what you read, and at which commit;
- a summary table: number, finding, verdict (`must fix` or `optional`);
- each finding: the rows it concerns, the problem, the evidence, and a proposed fix;
- a section on the kind rule, with your proposal for `open`;
- a section on the conventions the brief should settle;
- the tests the checker should add.

**Report:** the summary table, the must-fix findings in one line each, your proposal on the kind rule, and the conventions.
