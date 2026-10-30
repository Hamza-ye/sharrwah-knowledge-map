# Brief: the dry run's review

**What this step is for.** An independent review of the class's model's dry run: domain B (catalogue and inventory), built by the parts `B-anchor` (Shopify and Salla), `B-woocommerce`, and `B-backfill-woocommerce` where it ran. You made none of it. You test it against the evidence, claim by claim, and try to refute it. Report counter-evidence and missing evidence as findings. Record what you checked and found to hold in the coverage table, without argument. What you find sets the conventions and the checker's tests before the other domains run.

**Read, in this order:**
1. `studies/class-model/briefs/B-extent.md`, the brief the parts followed.
2. The evidence, before the parts' arguments: for each domain-B concern, its statements under all five placements, through `python3 -I method/class_slice.py` (its `--help` lists the commands), never the concern map's files whole. `studies/class-model/scope.tsv` gives domain B's concerns, and those of other domains that name B under `also`.
3. The parts' rows: `capabilities.tsv`, `landings.tsv`, `cells.tsv`, `evidence.tsv` and the side files in `studies/class-model/parts/B-*/`. Read their `reading` and `why` columns and their `notes.md` only after you have written your own reading of a cell (below).
4. `architecture/plan.md`, line 49, for check 12.

**Run the scripts on a copy.** The checker writes derived files into each part's folder, and you change nothing. So copy the model to your scratchpad (`cp -r studies/class-model "$S/model"`), and run every script with `CLASS_MODEL_DIR="$S/model"`:
- the checker on each copied part, in order (`B-anchor`, then `B-woocommerce`, then `B-backfill-woocommerce`);
- then `method/class_kinds.py --domain B --out -`, and `class_slice.py model --domain B` and `uncited --domain B`.

Then `diff` each copied `derived.tsv` and `derived-qualities.tsv` with the part's own. A difference is a finding. Every flag the checker prints is a row of your coverage table, with how you resolved it.

## What to check

1. **Every placement against all of the concern map's statements.** A cell's concerns are its platform's concerns landed in the capability, its parent or its children, and the concern of every statement it cites. Read them under all five of Q1's placements, not their `where` rows alone, and against the platform's other statements found by `search`. **Write your own placement for the cell first,** in the coverage table, then read the part's reasons and compare.
   - Where a cell's `where` statements name only an app store, a marketplace or an extension category, read its `decides` statements before accepting `extension-point`. The platform's own plan line, setting or admin route can show it doing the work itself. A route or setting that an extension or app adds, as its identifier or scope shows, is the extension's: for example, `WC-C-100/where/WC-S-5350` is scoped to WooCommerce Subscriptions.
   - Where a `core` rests only on API objects, scopes or webhook topics, decide which it is. It may be the platform's own API for its own feature, which is `core`. Or it may be an API whose statements say apps or partners use it to do the work, which is `extension-point`. Quote the words that decide it.
2. **Each `supports` value against the brief's tests.**
   - `own-service` only where a cited statement names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service. A product's name that carries the platform's brand doesn't name its maker. Never decide the maker from what you know.
   - A statement that makes the merchant or buyer responsible is `shows`, never `outside`.
3. **Each join, and the joins not made.**
   - **Joins made:**
     - a Q1 match, terms, identifiers, a definition, or role;
     - for a join on role: do both sides' cited definitions show the same thing?
     - for a join on terms: is it the same object, or one word for two things?
     - every strained fit: should it be split?
   - **Joins not made:** the checker flags each of these for the reviewer:
     - a statement cited by capabilities of two trees;
     - a Q1 match whose concerns landed in more than one tree;
     - a capability with nothing landed in its tree.

     For each, say whether they should be one capability, or one the other's parent, from the cited definitions.
4. **Each grain:** the capabilities cut finer or coarser than the concerns, their parents, and a coarse concern's statements cited in its children's cells.
5. **Each `none-held` cell:** search the platform's statements yourself, in every language they use. `search` matches substrings, with case, diacritics, hamza seats and tatweel ignored, and ة read as ه and ى as ي. A broken plural is another word: for Arabic, search each term's singular and plural, with and without ال. Record each term with its count of hits. A statement that shows the capability makes the cell false.
6. **The areas:** is each capability's area what it is about, whatever channel delivers it?
7. **The rulings on Q1's unclear candidates:** does each follow from the cited definitions? Where `scope.tsv` puts a candidate's other concerns in another domain, the ruling can only be `apart`. Don't test it against the definitions. Test whether `scope.tsv` placed those concerns rightly, and list the cases for the coordinator.
8. **What the parts never cite:** `class_slice.py uncited --domain B` lists the statements of domain B's concerns that no cell cites. Say which of them bear on a capability, or on its placement.
9. **Qualities and slot fillers:** each one's value, scope and capability, and the qualities and slot fillers the statements show that no row records.
10. **The names, and the anchor's shape.**
    - Each capability's name: does it use the terms of every platform landed in it, or a neutral term that names them all? Does it avoid a word that names something else on one of them?
    - Every WooCommerce landing, clean or strained: does WooCommerce's own grouping, in its `where` identifiers, cut the same way as the capability it landed in? If not, say whether to rename it, re-cut it, or mark the fit strained.
11. **The kind rule,** for each capability:
    - a `class` resting on a placement the statements don't support;
    - a `slot` that some platform's statements show in its core;
    - an `open` case: any capability whose count is 0 and that isn't a `slot`, including one where a platform's placements mix `not-stated` with third parties. Say how the rule should treat it, and why.

    The dry run has three of the five platforms, and a placement can hold under one scope only, such as a plan or a country: say where either changes a kind.
12. **What architecture needs** (`architecture/plan.md`, line 49). Each capability's data and events come from its concerns' `boundary` statements, and what decides it from their `decides` statements. Can both be derived from the concerns landed in it and the keys its cells cite, without a part writing more? List the capabilities where they can't, such as children sharing one coarse concern, and say what the merge would need.
13. **Other rows the checks above might miss:**
    - a citation from a concern of another domain without `also`;
    - a concern moved to another domain;
    - a note's inference carried into a placement;
    - a gap Q1 recorded on a cell's concern that changes what the cell can claim.

**Depth.**
- **Checks 1 and 2, in full.** Read each domain-B concern's statements once, under all five placements, and test every cell and evidence row that rests on them.
- **The searches beyond the domain's concerns,** for:
  - every cell under check 1's two bullets;
  - every cell of a capability counted 0 or 1;
  - every `none-held` cell.

  For the other cells, a sample drawn by a command you write into the review, with a fixed seed. The sample takes at least a third of those cells, and at least two per platform and per `supports` value.
- **Checks 3 to 13:** every row.

## Rules

- **Evidence:** cite every finding by statement key, part file and line. Mark every judgement of yours as a **Reading**, and give counts from scripts you ran.
- **Change nothing** in the repository but your own two files. Make no commits. Run Python with `python3 -I`.
- **Write as you go,** and keep your context small: print statements per concern, never load the concern map's files whole.

## Output

- **`studies/class-model/review-dry-run.md`:**
  - what you read, and the repository's commit;
  - a summary table: number, finding, verdict. `must fix` is a finding that makes a row, a count or a kind wrong; otherwise `optional`;
  - per check, the rows checked, the rows that failed, and the share;
  - each finding: the rows it concerns, the problem, the evidence, and the fix, as the rows to change;
  - a section on the kind rule, with your proposal for `open`;
  - a section on the conventions the brief should settle;
  - the tests the checker should add, each stated so it can be coded.
- **`studies/class-model/review-dry-run-coverage.tsv`:** one row per row checked.
  - **Columns:** `part` · `file` · `line` · `row` (the row's key: a `cap_id`, `cap_id/platform`, `cap_id/platform/key`, a `concern_id` or a `candidate_id`) · `check` (its number) · `mine` (your own placement, for check 1) · `result` (`holds`, or the finding's number) · `searched` (each search run for the row: platform, terms, and count of hits).
  - **Every checker flag is a row,** with how it was resolved.

**Report:** the summary table, the must-fix findings in one line each, the rows checked per check, your proposal on the kind rule, and the conventions.
