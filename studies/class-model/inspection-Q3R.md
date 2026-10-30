# Inspection of the briefs for Q3's check and the extent's review (30 October 2026)

**What this is:** an inspection, before they run, of `briefs/Q3-check.md` with `method/q3.py` and `q3/rows.tsv`, and of `briefs/R-extent.md` with `method/review_select.py` and `merged/flags.tsv`. The inspector wrote neither brief and changed no file except this one. All tests ran on a scratch copy of the model (`CLASS_MODEL_DIR`). Commands are run from the repository's root at `765de7c2`, with domains A, B and D to G merged and C's anchor still being written.

Severity: **must fix** means an agent following the brief would write wrong rows. **Should fix** means the output would be less consistent, harder to check, or more expensive than it needs to be. **Note** is for the record.

---

## Part 1. `briefs/Q3-check.md`, `method/q3.py`

### Must fix

**Q-1. `covered` has no grain, so two agents will place the same row differently.**
- *Found:* `covered` is "capabilities of the model answer what the row asks about the class: their cells say how the platforms do it" (line 19). The extent records capabilities and placements, not detail. The model's detail comes after GM ("Then architecture and the model's detail grow together", `PLAN.md`, Stage 4A; founder, 29 October). Many rows ask for that detail:
  - `km:ACC-02` asks which states a store can be in and what each allows. The model has `CM-ONB-002` "Store status in its lifecycle", but its cells don't list the states.
  - `km:PAY-01` asks what contract a provider implements (authorize, capture, refund, void, 3-D Secure).
  - most of the 81 payment rows, such as `pay:PAY-13`, ask which states a payment attempt passes through and which reasons close it.

  One agent will call these `covered`, since a capability exists. Another will call them `partly`, or `candidate miss: not held`, since the cells don't hold the states. Q3's misses would then mix two different things: a capability the extent lacks, and detail the extent never set out to hold.
- *Fix:* replace the definition of `covered` with: "`covered`: every thing the row asks about has a capability of the model, with its cells. The extent holds capabilities and where each platform places them, not their detail. Detail the row asks beyond the cells (states, fields, rules) doesn't make the row `partly` or a miss. Name it under `what_would_settle_it` as `detail: <what>`, for the model's detail at that area." Apply the same grain to `partly`: it is partly covered only where something the row asks about has no capability.

**Q-2. "Held" against "covered" can't be told apart, and nothing shows the agent which capability holds a statement.**
- *Found:*
  - Every concern of every platform lands once (`PLAN.md`, Stage 4A). So any statement a search finds belongs to a concern that already lands in some capability.
  - The brief says "a statement the model already cites in a capability you missed makes the row `covered` or `partly`" (line 26). It doesn't say what holds when the statement's concern lands in a capability but no cell cites the statement, or when that capability is coarser than what the row asks.
  - No tool the brief names answers "which capability cites this statement, or holds its concern". `class_slice.py search` and `key` print a statement and its concern, never its capability. `q3.py` has no such command. The merged `evidence.tsv` and `landings.tsv` aren't on the brief's reading list.
  - The test below shows a held miss passes even when its key is one the model cites. `SA-C-003/where/SA-S-3533` appears in `merged/evidence.tsv` (`grep -c` gives 1), and the checker printed "0 problems" for it.

  So whether a row is called `covered` or `candidate miss: held` depends on how far each agent happens to grep.
- *Fix:*
  1. Add `python3 -I method/q3.py where KEY ...`. For each key, it prints the statement id, every merged evidence row that cites that statement id under any concern's key (cap, platform, supports), and the capability its concern lands in (`merged/landings.tsv`). It works by statement id, as `class_merge.py` does with `sid()`.
  2. Add to step 1: "For each statement a search finds, run `q3.py where`. If a cell cites it, or its concern lands in a capability whose thing is what the row asks, the row is `covered` or `partly` by that capability. If its concern lands only in a coarser capability, the row is `candidate miss: held`: name that capability in `cap_ids` as where the miss would sit, and the keys in `basis`."
  3. Add the test from Q-8 that refuses a held miss whose keys a cell already cites.

**Q-3. `partly` doesn't say what the rest is, so the coordinator can't act on it.**
- *Found:* `partly` says what isn't covered under `what_would_settle_it` (line 20). That rest could be beyond the class (a market's fact or Sharrwah's design), a held miss, or a miss not held. The coordinator acts on only one of these, by amending the model from a held miss (line 86). `q3.py unasked` and the rebuilt Knowledge Map page can't tell the three apart either.
- *Fix:* add a column `rest` after `result`, required for `partly` and empty otherwise. Its value is one of `beyond the class`, `candidate miss: held` (keys in `basis`) or `candidate miss: not held`. The step-1 rules apply to the rest as they apply to a whole row. Add `rest` to `HEAD` in `q3.py`, with a test: it is required for `partly` and must be empty otherwise.

**Q-4. The `when` rule for `founder` contradicts the founder's decisions, and leaves half the list undefined.**
- *Found:* line 38 makes a founder decision `before build` where "the decision binds the architecture's structure (the company, its markets, whether Sharrwah's own company runs a service)". The founder has said the structure keeps room for those decisions instead of waiting for them:
  - 29 October, "Intent (standing)": "Sharrwah rules out nothing the class shows; the platform keeps room for each of these, whoever provides it", and its line (2), "The platform's capabilities for each remain the class's".
  - 26 October, G3 (S-01): "Keep room … Who holds sellers' money is a market's setting, with C everywhere at launch (E1)".
  - 28 October, Scope: the markets "are not necessarily in launch scope … Yemen's present circumstances and today's business capacity don't become permanent product or architectural constraints".

  So the rule sends rows to `before build` that the founder has placed at a market's setup. `km:INT-04` shows it: "Will Sharrwah run its own payments, marketplace or buyer app…", needed `later`, would become `before build` and a `wrong time` time bomb. The rule is marked as the coordinator's own, but it reads against decisions in force. It also gives no time for "which merchants first", "spending" or "licences", which the brief's own list (line 31) includes. `km:INT-01` ("Which market and merchant segments does Sharrwah serve first") would then be read as `before build` by one agent and `unclear` by another.
- *Fix (the coordinator's own rule, a reading, to be marked as such):* "`founder`: `before release` for every decision on the founder's list, since the platform keeps room for each, whoever provides it (`founder-decisions.tsv`, 26, 28 and 29 October). What the structure must keep open for such a decision is engineering's: add `engineering` with `before build` where the row asks how room is kept." If the coordinator holds that some founder decision binds structure, name it, with the founder's row that says so.

**Q-5. The `when` rule for subjects contradicts the architecture plan.**
- *Found:* line 39 gives `before build` only to S-03 and S-09, and "`before release` otherwise, since a subject's answer is bound per market". `architecture/plan.md`, section 3, says otherwise:
  - "An area waits for the subjects that cover its open questions", namely "the payments area after S-04 … tax after S-05 … where data lives after S-08 … delivery after S-10 … what Sharrwah charges after S-11";
  - S-02's entry points (E1, E2) and its business record (D1) are cross-cutting decision 4.

  An area's architecture comes before build. So most of the 81 payment rows, which are S-04's and S-11's, would get the wrong `when`, and their `wrong time` time bombs would come out wrong too. The rule mixes two things: the subject's run, which architecture waits for, and the market's own setup, which is bound per market.
- *Fix:* "`subject:S-NN`: `before build`, since each area's architecture waits for the subjects that cover its open questions, and S-03 and S-09 for every area (`architecture/plan.md`, section 3). Where the row asks only which provider, partner or law fills a slot in one market, add `outside` (or `founder` for a partner), `before release`."

**Q-6. `wrong time` is computed from the model's timing, so it raises false time bombs on rows the model answers.**
- *Found:* `model` is always `before build` (line 36), and `wrong time` fires when `needed_by` and `when` disagree (line 46). So every row the model covers whose `needed_by` is `launch` or `later` becomes a `wrong time` time bomb. That is up to 79 rows: in `q3/rows.tsv`, km has 38 `later` and 15 `launch`, and pay has 10 `later` and 16 `launch` (`cut -f1,3 | sort | uniq -c`). Q3's type, as agreed, is "treated as blocking build when it only blocks release, or the reverse". A row the model answers before build can't go off late, whatever its `needed_by`. The checker doesn't test `wrong time` either way (Q-8), so agents will differ on it too.
- *Fix:*
  - "`wrong time`: the row's `needed_by`, read as above, disagrees with the earliest `when` of its answerers other than `model`. A row only the model answers has none. A `when` of `unclear` raises none."
  - Then have `q3.py check` compute it, and require it exactly where it holds (Q-8).

**Q-7. `bundles` drops Q3's type as the founder agreed it.**
- *Found:* Q3, as agreed on 10 October (`questions/Q3-placing-rows.md`), names the type "it bundles concerns placed differently". The brief redefines it as "its parts have different answerers or different times" (line 44). A row the model alone answers, but which bundles a `class` capability with a `slot`, is then never a bundle. Yet that is exactly Q3's case: one part is the platform's core and another is left to third parties. The brief marks the rule as the coordinator's own. It still replaces an agreed definition, and `PLAN.md`, section 9 is the route for changing one.
- *Fix:* "`bundles`: its parts land on capabilities placed differently: different kinds (`class`, `slot`, `open`), or core on one and left to third parties on another, by `q3.py slice`'s kinds and placements (Q3's type as agreed). Also where its parts have different answerers or different times (the coordinator's own, a reading)." `q3.py check` can then test the first half from the kinds of `cap_ids`.

### Should fix

**Q-8. `q3.py check` passes rows that contradict the brief.** I built a scratch `q3-check.tsv` with 4 good rows and 13 faulty ones, then with 8 more. It refused what it should for 7 kinds of fault:
- `needed_by` not the row's own;
- `CM-PAY-002`, which isn't merged;
- `covered` without `model`;
- `subject:S-12`;
- a duplicate row;
- `when` = `whenever`;
- an empty `basis`.

It raised nothing on any of the rows below. On the first file, its 8 problems were all on other rows. On the second, it printed **"8 rows placed of 8; 0 problems"** (exit 0):

| Row | What was wrong |
| --- | --- |
| `candidate miss: held`, basis `SH-C-999/where/SH-S-0001` | no such key |
| `candidate miss: held`, basis `SA-C-003/where/SA-S-3533` | the model cites this key already |
| `candidate miss: held`, basis `see SH-S-1234 maybe` | free text matches the regex `[A-Z]{2}-[SI]-\d{4}` |
| `beyond the class`, `who_answers` = `model`, `cap_ids` = `CM-PLN-001` | contradicts its own result |
| `candidate miss: not held` naming `CM-TRU-010` | a miss that names a capability |
| `who_answers` = `outside`, `when` = `before build` | against line 40 |
| `who_answers` = `model`, `when` = `later` | against line 36 |
| `who_answers` = `model;founder`, no `bundles` | against line 44 |
| `needed_by` = `launch` (and `pay:PAY-12` = `later`), `when` = `before build`, no `wrong time` | against line 46 |
| `wrong time` where `needed_by` = `model` and `when` = `before build` | flags a time bomb with no disagreement |
| an eleventh field, from a stray tab | silently dropped |
| a field in double quotes | quoting, against line 69 |
| `cap_ids` separated by commas | against line 71 |

*Fix, in `cmd_check`:*
- each line has exactly 10 fields and no `"`;
- `cap_ids`, `who_answers`, `time_bombs` and `basis` are split on `;` only;
- every key in `basis` of the form `XX-C-nnn/<placement>/<cite>`, or an inventory id, exists (`class_slice.items`). For a held miss, at least one does, and no merged evidence row cites its statement id (Q-2);
- `beyond the class`: `model` not in `who_answers`, `cap_ids` empty;
- `candidate miss: not held`: `cap_ids` empty;
- `when` equals the rule's value wherever the answerers determine it (`model` only gives `before build`, `outside` only gives `before release`, a subject gives `before build` after Q-5, several give the earliest of those determined);
- `wrong time` is present exactly where Q-6's comparison says so;
- `bundles` is required where two answerers' `when` differ.

**Q-9. `check --rows` can't be brought to "no problem" for one batch.**
- *Found:*
  - `check --rows km:ACC-01` printed every other line's problems and counted them: "16 rows placed of 1; 8 problems".
  - A bare id takes both sets: `check --rows PAY-01` demanded `km:PAY-01 has no line` for a batch that holds only `pay:PAY-01`.
  - The brief says to check "until it prints no problem" (line 73). An agent whose batch is clean must then either loop or edit another batch's rows.
- *Fix:* with `--rows`, test and count only the listed rows (duplicates still checked across the file), and print "N of your M rows placed". Refuse a bare id that names rows of both sets ("PAY-01 is in both sets: write km:PAY-01 or pay:PAY-01"). Change line 73 to `--rows <set:id,...>`.

**Q-10. Decisions already made: the brief limits reading to one row and gives no result for them.**
- *Found:* the brief lets the agent read only "the row of 29 October ('Intent')" (line 9). Two rows of that date carry the gate "Intent", so which one is meant is ambiguous. Yet `basis` asks for "the founder's decision row by its date" (line 49). Several rows are already answered by decisions in force:
  - who holds sellers' money: Decision 1, 25 October, with the defaults and Decisions 2 to 12;
  - keeping room for A and B: 26 October;
  - S-02's rulings: 30 October;
  - "which capabilities belong in Sharrwah's core" (`km:INT-03`): the intent of 29 October.

  An agent that can't read them will place these as open questions for the founder, with a `when`.
- *Fix:* let the agent read `founder-decisions.tsv` whole (31 rows). Add: "A row a decision in force already answers is `beyond the class` with `who_answers` `founder`, `when` the rule's value, `basis` the decision's date and gate, and `what_would_settle_it` `decided`. It is `wrong party` if it asks the platforms what the founder has decided."

**Q-11. Areas with no capabilities by design, and rows about the method.**
- *Found:*
  - The areas WLD, ENG, INT and MTH (23 km rows) are domain H, which "takes no capabilities" (`PLAN.md`, Stage 4A). `slice` prints "in area WLD: 0 capabilities". LNG (2 rows) has none merged either. The brief doesn't say this, so an agent may read the empty area as a miss.
  - MTH-01 to MTH-05 ask about the knowledge work itself ("What counts as part of the product class…", "What is the stopping rule for capture…"). `PLAN.md` and the founder's decisions answer them, and no `who_answers` value fits.
- *Fix:* add "Domain H's areas (WLD, ENG, INT, MTH) hold no capabilities by design: an empty area there is not a miss." Add a `who_answers` value `plan`, `before build`, with `basis` the `PLAN.md` section or the decision's date, for rows about the method.

**Q-12. A market's fact that no subject covers, and the product gaps Q3 places rows against.**
- *Found:*
  - `km:WLD-01` (the laws that govern online selling in a market) is covered by none of S-01 to S-11. The brief offers `subject:S-NN` only (line 30).
  - Q3, as agreed, places rows against the map "extended by the product gaps from the Yemen test". Since the reset, those are the product gaps the subjects' registers record (`PLAN.md`, the test form: "a need the Yemen row shows that no reference meets: a product gap"). The brief doesn't name them, so a row a register's product gap answers would be called a miss.
- *Fix:*
  - Add `subject:none`, with `what_would_settle_it` naming the subject it would need, for the coordinator to take to Stage 3's list.
  - Add `studies/subjects/S-0N/register.tsv` (product-gap rows) to the reading list. A row one of them answers is `beyond the class`, `subject:S-NN`, with the register row in `basis`.

**Q-13. The search for a miss leaves things out, and its route isn't checked.**
- *Found:*
  - `class_slice.py search` reads statements and *placed* inventory entries only. It doesn't reach Q1's out-of-scope inventory (`outscope`), such as store limits, so a limit or a list entry would be called `not held`.
  - For `not held`, the brief asks for "a capture of named material, or a subject" (line 23). `PLAN.md`, section 6, "Evidence", requires that before a gap goes to anyone its route is checked against what is held ("page not read", reader extended, capture request).
- *Fix:*
  - Add `outscope --platform P --terms` to the search before a miss.
  - Add to `what_would_settle_it` for `not held`: "name the material. The coordinator routes it by `PLAN.md`, section 6, 'Evidence', before any handoff."

**Q-14. The model's amendment from a held miss runs without the cells the method requires.**
- *Found:* line 86 says "the coordinator … amends the model from the held misses". `B-extent.md` runs a moved or added concern as `<domain>-amend`, which writes "every platform's cells for any capability it adds", so that a capability added late is not counted on one platform alone. The brief doesn't say this. Its amendments would also escape the review: `review_select.py` sees only rows marked "(the coordinator" (R-1).
- *Fix:* "amends the model from the held misses through `<domain>-amend` parts, each with every platform's cells (`B-extent.md`, 'The amendment part'). Each amended row is marked '(the coordinator, from Q3's check: <set:row_id>)', and then the merge and `review_select.py` run."

**Q-15. Several batch agents append to one file.**
- *Found:* every batch appends to `studies/class-model/q3-check.tsv` and creates it "with its header if it doesn't exist" (line 65). Two batches running together can both write the header, or interleave lines. With Q-9, one batch's half-written line also blocks the other's check.
- *Fix:* either run the batches one after another (say so in the brief), or have each batch write `studies/class-model/q3/check-<batch>.tsv`, with `q3.py check` and `unasked` reading `q3/check-*.tsv`.

**Q-16. `basis` uses ids the brief never defines, and repeats `cap_ids`.**
- *Found:* `basis` takes "the capabilities and the cell keys" (line 49). A cell has no key. It is a capability and a platform. Agents will write `CM-ACC-001/shopify`, `CM-ACC-001:salla` or statement keys.
- *Fix:* "`basis`: for `covered` and `partly`, the cells as `<cap_id>@<platform>` (`;`-separated), adding statement keys only where a cell's reading is what answers. For a held miss, the statement keys. For a subject, its id. For a decision, `founder-decisions <date> <gate>`." The checker then tests the `@` form against `merged/cells.tsv`.

**Q-17. Rows whose words name no party.**
- *Found:* many payment rows are worded as design: `pay:PAY-03` "Is the amount still owed held as one signed balance … and is every payment status derived from it…?". The brief says to judge by the words (line 45). The words don't say whether the question is about the class or about Sharrwah, so one agent will answer `model`, another `engineering`.
- *Fix:* "A row in the present tense about 'the platform(s)' or 'each platform' asks the class. A row with 'should' or 'Sharrwah' asks engineering (or the founder, by the list). A row naming neither asks both: the class's part goes to the model, the design part to engineering, and the row is a `bundles` time bomb."

**Q-18. The cost of `slice` output.**
- *Found:* `slice` prints the area's capabilities, with their placements, again for every row. `--area TRU` is 7 rows by 21 capabilities, 147 repeated lines and 39,961 characters. PAY has 88 rows, and C-anchor already has 32 PAY capabilities before the mapping. At about 230 characters a line, that is about 88 × 40 × 230 ≈ 800,000 characters (an assumption on C's final size), or roughly 200,000 tokens of repeated lines.
- *Fix:* print each area's capabilities once per call (before its rows). Under each row, print only the "elsewhere" leads. Print the capability's domain, which `class_slice.py model --domain` needs and `slice` doesn't show.

### Notes

- **Q-19.** Under `CLASS_MODEL_DIR`, `q3.py` sets `ROOT = MODEL/../..`, so `subjects.tsv` isn't found. `rows()` then returns `[]`, and the `subject:S-NN` test switches off without a word (`if … subjects and …`). Fail if `subjects.tsv` is missing. (I tested with the copy at `/tmp/claude-0/-home-user-sharrwah-knowledge-map/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/root/studies/class-model`, with `subjects.tsv` copied beside it, which is how the test above refused `S-12`.)
- **Q-20.** `unasked` counts `cap_ids` of every result, `beyond the class` and misses included, and builds `parents` without using them. Count only `covered` and `partly` (and `rest`), and decide whether a row that names a parent asks about its children. Q3's item 3 lists concerns. The brief's capabilities are an adaptation, which the report should say.
- **Q-21.** `slice --area pay` (lower case) prints nothing and exits 0. The "elsewhere" leads are weak for payment rows: for `pay:PAY-01` (roles in commerce money) they are the audit log, product listings and the Storefront API. Lines 26 and 62 already say they are leads, not answers. That holds.
- **Q-22.** I checked `q3/rows.tsv` against `e4d5cee:register/km-questions.tsv` and `pay-questions.tsv`: 179 and 81 rows, 0 mismatches in id, `needed_by` or question. The rows are read only for id, question and `needed_by`, as `PLAN.md`, section 6 says. `needed_by`'s values are defined on the Knowledge Map's page at `e4d5cee` (spine: "to build the capability map and glossary now"; model: "before the area's domain model is written"; slice: "before the area's first build slice"; launch: "before merchants depend on it"; later: "when the area comes up"). The brief's reading of them (line 46) matches. It could cite them.
- The brief keeps the rule that a row never adds a capability, variation point, variant or cause (line 14), and it marks its `when` and time-bomb rules as the coordinator's own. Q-4 to Q-7 are about their content, not their marking.

---

## Part 2. `briefs/R-extent.md`, `method/review_select.py`

`CLASS_MODEL_DIR=<scratch> python3 -I method/review_select.py` printed:
```
cm/review/selection.tsv: 543 items from 1270 cells
  share 1: coordinator 37, flag 25, kind 49, own-service 9, role 37, sample 12
  share 3: coordinator 33, flag 33, kind 44, own-service 10, role 18, sample 10
  share 4: coordinator 52, flag 44, kind 42, own-service 20, role 42, sample 26
```
Domain C is not yet merged. Its 12 coordinator items fall into share 4 (R-12).

### Must fix

**R-1. Q3's check isn't reviewed, though the Q3 brief says it will be.**
- *Found:* `Q3-check.md`, line 86: the coordinator "has the check reviewed with the rest of the extent". `R-extent.md` has no kind of item for Q3's rows, and `review_select.py` doesn't read `q3-check.tsv`. The model's amendments from Q3's held misses are selected only if the coordinator happens to mark them (Q-14).
- *Fix:*
  - Add a kind `q3` to `review_select.py`: every `candidate miss` and `unclear` row, every `beyond the class` row whose answerer excludes `model`, and a seeded 10% of the `covered` rows.
  - Add to the brief: "**q3:** a row of Q3's check. Does its result hold on the model's cells and the concern map (search as `Q3-check.md` asks)? Are its answerer and time those its rules give?"
  - Run `review_select.py` after Q3's amendments have merged.

**R-2. The selection leaves out most cells where an error would change a count, and the brief forbids looking at them.**
- *Found:* by placement, on the merged cells and the selection:

  | Cells | Count | Selected |
  | --- | --- | --- |
  | `none-held` | 506 | 67 |
  | held with statements but no own placement (`not-stated` or `shows` only) | 59 | 18 |
  | held with statements, placed only with third parties | 74 | 28 |

  Every cell of a slot or an open is selected, so the 41 and 46 unselected cells of the last two rows all belong to classes. Each of these, if wrong, changes a capability's count, and for a slot or an open, its kind.
  - The method report promised "every cell whose kind hinges on one placement, every join on role and every `none-held`, then a seeded sample" (section 7).
  - The dry run found one false `none-held`, and a whole part that read the platform's own API as `shows` (55 rows, three counts; section 6). The second sits in exactly the unselected `not-stated` and `shows` cells.
  - The brief says to review "every one of them, and nothing else unless an item leads you to it" (line 5).
- *Fix:*
  - Add a kind `count`: every cell of a `class` held with statements but placed neither `core` nor `own-service` (41 plus 46 now unselected).
  - For `none-held`, select every cell for which `class_slice.py candidates --domain D --platform P` lists a lead holding two or more of the other platforms' terms, a cheap filter run by the script. If the budget allows, select all 439.
  - Add to the brief: "**count:** a cell whose placement, if wrong, changes the count. Does the platform place it in its core after all, by the conventions (its own API, a released flag, a staff permission)? For `none-held`, read the leads `candidates` gives."

**R-3. "Counted twice" asks for one answer where the conventions give two.**
- *Found:* the brief says: "Where do its words belong? It counts there, and shows elsewhere" (line 21). Many of the 36 flags are statements whose words name several things:
  - `SA-C-003/where/SA-S-3533` is a route pattern, `/^/manage/(custom-urls|webhooks|migrate|complaints|violation|currencies|support-access|stores)/`, core in six capabilities of four domains;
  - `WC-C-073/boundary/WC-S-0258`, the webhook topic `customer.created`, is core in customers (D) and in the webhooks API (F). `B-extent.md` asks for this, line 63: "Each … webhook topic … is evidence for a capability. The platform's … webhooks … are themselves capabilities, in their own domains".
  - The E-woocommerce notes add a further rule: "A maker statement may count for each feature of its service … the final review weighs it as maker evidence, not as a feature counted twice."

  One reviewer will demote all but one capability's use to `shows`, and another will keep them. None of the 36 flags is a cell's sole support (`grep "counted twice" merged/flags.tsv | grep -c "rests on it alone"` gives 0). So demoting changes no count today. It still changes placements and readings, and it would change counts later.
- *Fix:* "*counted twice:* does the statement's words name each capability's thing? Where they name several things (a list, a route pattern, a webhook topic that is also an instance of the webhook mechanism, a maker statement for several features of one service), it counts in each. Where they name one thing that two domains each hold, that is one capability: answer as for *one capability?*." Then the 36 flags without a sole support can go into one item for the coordinator to settle by convention 8, rather than 36 agent items.

**R-4. "Ruled differently" asks for one answer where S3 gives two by design.**
- *Found:* the brief says: "Give the one answer the whole model's cells support" (line 22). The dry run's ruling S3 makes each domain rule from its own cells: `joined` where its capability cites both sides, and otherwise `apart`, "with the basis 'scope.tsv gives <concern> domain <X>'". `class_merge.py` re-checks each ruling on its own domain's parts. For `U-006`:
  - A-anchor has `joined:CM-TRU-001`;
  - G-anchor has `apart`, with the basis "scope.tsv gives SH-C-007 domain A, without naming G under also".

  Both follow S3. A reviewer told to give one answer will mark one of them wrong. If the coordinator then changes it, the merge refuses it ("joined:… but no cell … cites keys of both sides").
- *Fix:* "*ruled differently:* does each domain's ruling follow S3 from its own cells? If both do, the pair is one thing in the model wherever it is `joined`, and the verdict is `holds`. It is `wrong` only where a ruling breaks S3, or where the `joined` capability doesn't show both sides as one thing."

### Should fix

**R-5. Strained fits, the checker's flags, and the parts' own leads for the review are not selected.**
- *Found:*
  - Parts marked 161 landings `strained` so that "the reviewer can split it" (`B-extent.md`, line 78). The selection has no kind for them. It includes only the merge's `strained?` flags on clean landings (46).
  - Each part's `check_class_part.py` flags are "for the reviewer" (`B-extent.md`, line 151). A-zid prints 22 and E-anchor 27, among them `own-service` maker questions and "cited … in more than one tree".
  - The parts' notes name items "for the final review". E-anchor's SH-C-144 is "Listed for the final review", and the method report, section 8, says "The final review checks whether each [Zid capability resting on names alone] should fold into its parent".

  The brief doesn't select any of these.
- *Fix:*
  - Add a kind `strained` for each landing whose `fit` is `strained`, grouped one item per capability. The question: should the concern be split out, and where?
  - Add a kind `lead`: each line of a part's `notes.md` that names "the final review" or "the reviewer", and each capability whose cells cite only inventory ids. The question: is it a capability, or does it fold into its parent?

**R-6. Some rows the coordinator wrote or changed are missed.**
- *Found:*
  - `review_select.py` reads only `evidence.tsv`, `landings.tsv`, `cells.tsv` and `capabilities.tsv`. Seven coordinator-marked rows in `parts/E-woocommerce/rulings.tsv` and 36 in `scope.tsv` (`grep -c "(the coordinator\|the coordinator, "`) are not selected, though the docstring promises "every row the coordinator wrote or changed".
  - A deletion leaves no row to mark, such as "Salla's two-factor and biometric flags … leave CM-ACC-001" in A-anchor's notes.
  - The brief points to the reason "under 'The coordinator's corrections'", but D-anchor's corrections sit under "The coordinator's sweep of partner permissions" and "After batch N (the coordinator)". Of the 81 bullets under that heading in all the parts' notes, 13 name ids that no coordinator item names, mostly `scope.tsv` changes.
- *Fix:*
  - Read `rulings.tsv`, `qualities.tsv`, `slot-fillers.tsv` and `scope.tsv` too.
  - Also select each bullet of the notes' coordinator sections (any heading or line containing "the coordinator") as one item. That shows deletions.
  - In the brief, say "the coordinator's reason is in the part's `notes.md`: search it for 'the coordinator'".

**R-7. Joins other than on role, and a join missed inside one domain.**
- *Found:* 110 landings joined on `terms`, 79 of them unselected. A shared term that is a homonym joins two things into one count, and Q1 found six homonyms. Nothing selects a capability of count 1 that duplicates another capability of the same domain (a missed join, which splits one count into two). The `one capability?` flag covers only two domains.
- *Fix:*
  - Select each `terms` join whose join term is in `class_slice.py homonyms`.
  - Add to the brief's **kind** item for a count of one: "Is it another capability's thing, in any domain? Run `caps --terms` with its terms in both languages."

**R-8. The sample can't show a part's gaps.**
- *Found:* the sample is 5% of all unselected cells, with no strata:
  - 9 parts get no sampled cell, among them A-bigcommerce (48 cells), B-woocommerce (29) and E-bigcommerce (43);
  - D-backfill-bigcommerce (24 cells), E-backfill-bigcommerce (8) and D-backfill-woocommerce (2) get no item of any kind.

  The method report, section 9, makes the sample "where a gap in a part's reading shows (the effort rule of 13 October: 'a part whose check or review shows gaps is re-run')". That needs a sample in every part.
- *Fix:* sample per part, at least 2 cells or 5%, whichever is larger. Report each part's sample in the summary.

**R-9. Size and cost: one reviewer per share, no batches, and repeated items.**
- *Found:*
  - There are 543 items before domain C. Share 4 alone has 226, and C's anchor has 118 concerns still to add.
  - The brief has one reviewer per share and no batching, though the method report found that cost grows with the square of a context's length (section 4). The dry run's cells review cost 62.1 million for 84 cells at a context of 455,000 tokens (section 6).
  - 57 cells appear in 127 items (14 cells as two `coordinator` items, 9 as `coordinator` and `role`, and so on).
  - At the mapping's 0.2 to 0.3 million per item, an assumption, 543 items cost about 110 to 160 million, and C's items add to that. The projection is "about 90" for the review and its corrections (section 13).
- *Fix:*
  - Group items per cell, one item with all its reasons.
  - Have the coordinator's message name a share and a batch of about 30 items, each batch run by a fresh agent writing to `coverage-<share>-<batch>.tsv`.
  - Drop the 36 counted-twice items without a sole support (R-3).
  - Re-project the cost after the first batch.

**R-10. The coverage can't be checked, and a correction can't be applied as written.**
- *Found:*
  - No script checks `coverage-<share>.tsv`: one line per item, the values, that `basis` keys exist, a `correction` for `wrong`, and `what_would_settle_it` for `unclear`.
  - The value `severity` has no place for a change of structure: a landing moved, a parent, two capabilities merged or one split, a concern's domain.
  - `correction` is "what the row should say", but it doesn't say which row (part, file, key).
- *Fix:*
  - Add `python3 -I method/review_select.py check --share N [--batch B]` with those tests.
  - Add `structure` to `severity`.
  - Make `correction` "`<part>/<file>`: the row (its `cap_id` and `platform`, or `concern_id`, or `key`) and the new value".

**R-11. Tools left out, and a convention cited wrongly.**
- *Found:*
  - The brief lists `key`, `statements`, `search`, `model` and `caps`. A **kind** check for a slot ("does the platform do it itself after all") also needs `candidates` (its leads), `outscope` (Q1's unplaced inventory, the evidence the dry run found that "no search could see"), `gaps` (the convention says a Q1 gap may change what a cell can claim) and `homonyms` (for role and terms joins).
  - "convention 5" (line 18) is, in `review-dry-run-rulings.md`, "A statement's title against its description". The maker rule is the finding ruling C5, and the last bullet of `B-extent.md`'s conventions.
- *Fix:* add those four commands to "Read only" and "How to work". Change "(convention 5)" to "(the dry run's ruling C5; `B-extent.md`, 'Maker evidence')".

**R-12. Shares and item ids depend on when the script runs.**
- *Found:*
  - A share comes from the capability's domain in the merged model. An item whose capability isn't merged falls to share 4. Today that is the 12 C-anchor coordinator items, which belong to share 2.
  - Item ids `R-nnnn` are renumbered at each run, and the model changes after Q3's amendments and C's merge. A coverage file written against one selection doesn't match a later one.
- *Fix:*
  - Take the share from the part's folder (`d.partition("-")[0]`) for coordinator items, and from the capability's id prefix area through `seed/km-areas.tsv` otherwise.
  - Have the brief say: "the selection is written once, after the last merge, and committed. Its commit is named in your message."

### Notes

- **R-13.** A `class` held only under a beta, a plan or one observed store (convention 11) isn't risk-selected. With convention C6 (an unreleased flag is `shows`), a class whose `class_scope` isn't `general` is a cheap kind to add.
- **R-14.** "For every item, check that each fact traces to its statement at its commit" (line 27) may be read as opening the evidence repositories for every key, which costs. Say "traces to its key. Read the source at its commit only where the statement's words are in doubt."
- The brief's independence ("by an agent that made none of it"), its rule that the founder's words are never evidence, and its rule against changing the model's files follow `PLAN.md`.

---

## What I ran

All from `/home/user/sharrwah-knowledge-map`, with `python3 -I`. Tests that write ran on a copy of `studies/class-model/` under the scratchpad, with `CLASS_MODEL_DIR` set:
- `method/q3.py slice --rows PAY-01` (both sets), `--rows km:ACC-02,TRU-03`, `--rows km:WLD-01`, `--area PAY --set pay --from 3 --to 4`, `--area PAY --from 1 --to 2`, `--area pay`, and `--area` for ACC, PLN, TRU, MKT, SFR, APP and API (output sizes);
- `method/q3.py check` on two hand-built `q3-check.tsv` files (17 rows, then 8), with `--rows` in `set:id` form, a bare id, one row, `;`, and none;
- `method/q3.py unasked`;
- a comparison of `q3/rows.tsv` with `e4d5cee:register/*.tsv`;
- `method/review_select.py`, then counts of its selection by kind, share, part and cell placement against `merged/cells.tsv`, `landings.tsv` and `kinds.tsv`;
- `method/check_class_part.py` on the copies of A-zid and E-anchor (for the flags the parts leave to the reviewer);
- `class_slice.py key` on two flagged statements;
- greps of `merged/flags.tsv`, the parts' `notes.md`, rulings and `scope.tsv` for the coordinator's marks.

## What I didn't check

- I reviewed no item of the selection, and placed no Q3 row against the model, beyond the examples cited.
- Domain C isn't merged, so I couldn't test `slice` on C's areas (114 rows: CHK, ORD, PAY, TAX, SHP, RET) or the selection's share 2. C-anchor's files were being written by its agent while I ran: the working tree shows them modified, by that agent, not by this inspection.
- I didn't run `q3.py rows`, which rewrites `q3/rows.tsv`. I compared its output with the source instead.
- I didn't verify whether each kind and count in `merged/kinds.tsv` is right, or read any statement at its commit.
- I didn't verify whether every notes bullet of the coordinator matches a changed row. The 13 unmatched in R-6 are by id only.
- The cost figures in Q-18 and R-9 are assumptions from the method report's rates, not measured.
