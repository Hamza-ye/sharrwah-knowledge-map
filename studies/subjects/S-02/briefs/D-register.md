# Brief: S-02, the register's draft (step 4)

This is `PLAN.md` Stage 4, subject S-02, step 4: the decision register. You are one agent with one task: draft it from phase C's results. The coordinator checks your draft, and an agent that made none of it reviews it later.

**Why.** Phase C gave 361 keys under 75 variation points. 142 of them follow as "a decision for the founder, on a recommendation", in 90 wordings. Most ask one question, setting by setting or decider by decider. The founder can answer a handful of questions, not 90. The register asks each question once, with what the evidence shows and an engineering recommendation, and lists what follows by rule.

**Read only:**
- this brief;
- `PLAN.md`, sections 1 and 6 (the aim, and the test form: cause, coexistence and what follows);
- `founder-decisions.tsv` (the decisions in force: among them Decision 1 and its follow-ons of 25 and 26 October, and the scope of 28 October);
- `studies/subjects/S-02/frame.md` (the root decisions, and "How S-02 relates to other subjects");
- `studies/subjects/S-01/register.tsv` (its shape, and the drivers and decisions S-02 builds on);
- S-02's phase C files: `c/RD1/`, `c/RD2/` and `c/RD3/` (`answers.tsv` and `points.tsv`), and `variation-points.tsv`. Print them with short scripts, not whole. Leave out every `note` column, and `notes*.md`;
- statements and variants by id, as your evidence needs them: `python3 -I method/subject_slice.py studies/subjects/S-02 --print RD --ids ...`, and `variants.tsv` filtered by `variant_id`.

## The task

1. **Drivers** (kind `driver`): the founder's decisions and S-01's drivers that bear on S-02, each cited by its row in `founder-decisions.tsv` or its id in S-01's register. Add none of your own.
2. **Founder decisions** (kind `founder decision`). Group the 142 founder items:
   - **One decision per question the founder would answer once.** Items that ask the same question of different settings, keys or deciders join one decision, which lists them. An example is "does this setting take a value per market, or once for the whole store?"
   - **A setting stands apart only when its later change costs more in kind:** a data model, a contract or another subject's decision follows from it. Say why.
   - **Aim for at most four decisions per root decision.** If you need more, say why in the row.
   - **Each decision row holds:**
     - `question`: one sentence the founder can answer;
     - `alternatives`: each option, with the platforms that take it, their causes and kinds, citing `vp_id` and key;
     - `recommendation`: engineering's, marked as such, with the rule it follows (`PLAN.md` section 6, steps 4 and 5: generality, and a variation point behind one interface; section 1: hide what is likely to change);
     - `trade_off`;
     - `closes`: what the recommendation rules out, and why, by one of three reasons: a confirmed fact, the founder's choice, or an engineering cost greater than the option's value;
     - `cost_later`: the cost of changing course later: `a setting`, `one module` or `a redesign`, with why;
     - `answers_items`: every founder item it answers, as `vp_id|key`, `;`-separated;
     - `depends_on`, `reopens_when`;
     - `status`: `for the founder`.
3. **Moved** (kind `moved`): founder items whose question another subject owns, by the frame's "How S-02 relates to other subjects":
   - S-03: the contracting company;
   - S-04: payment providers;
   - S-05: tax;
   - S-07: verification, sanctions and the countries served;
   - S-08: data;
   - S-09: currency;
   - S-10: delivery;
   - S-11: what Sharrwah charges.

   Write one row per subject. List its items in `answers_items`, and say what S-02 settles for them: where the binding is held, and what it keys on.
4. **Follows by rule** (kind `follows by rule`): per root decision, one row for each outcome among the other keys:
   - commonalities;
   - bound per market;
   - kept open;
   - left to the build.

   Each row lists its keys as `vp_id|key`, with one line on what it means for the design.
5. **Engineering constraints** (kind `engineering constraint`): where the results imply a constraint on the design, such as one interface behind which a set of settings resolves, state it with its rule and the keys it rests on.

## Rules

- **Every claim cites ids:** `vp_id`, key, `variant_id`s and `stmt_id`s. A reading is marked as one. The founder's words are never evidence of what a platform does.
- **No market's facts, and no market's name, in any recommendation.** The Yemen row and the scenario walk test the recommendations afterwards (`PLAN.md` section 6, steps 6 and 7). Sharrwah's markets are the founder's of 28 October.
- **Nothing is decided.** A decision's `answer` stays empty. A recommendation is engineering's, for the founder to accept or not.
- **Keep fields short.** `decisions.md` is at most six pages.

## Output, in `studies/subjects/S-02/`

- `register.tsv`: tab-separated, with a header row and no quoting; no tabs or newlines inside a field. Columns: `id` (S02-R1… for drivers, S02-D1… for founder decisions, S02-M1… moved, S02-F1… follows by rule, S02-E1… constraints) · `kind` · `vp_id` · `question` · `answer` · `alternatives` · `recommendation` · `trade_off` · `closes` · `cost_later` · `answers_items` · `depends_on` · `drivers` · `evidence` · `rationale_at` (the section of `decisions.md`) · `status` · `reopens_when`.
- `decisions.md`, the founder's page. Per root decision:
  - its decisions, each with its question, its options and who takes them, the recommendation and why, what it closes, and the cost of changing course later;
  - then, in a few lines, what follows by rule, and what moved to other subjects.
- Your notes in `notes-register.md`: calls you made, and problems with the brief or the evidence.

**Before you finish,** run `python3 -I method/register_items.py studies/subjects/S-02`. It lists every founder item that no row's `answers_items` names, and every item two rows name. Fix both lists to empty. Then run `python3 -I method/check_register.py studies/subjects/S-02/register.tsv` and fix each problem it lists.

**Size:** about 60 requests. At about 90, write what you have, run the two checks, and stop, saying what is left.

**Report:** the decisions, by root decision, each with its question and recommendation in one line; what moved, by subject; the checks' results; and problems with the brief.
