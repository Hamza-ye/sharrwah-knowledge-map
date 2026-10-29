# Method

**What this folder is:** the scripts the plan uses. Run each with `python3 -I`.

| Path | What it is |
| --- | --- |
| `capture/` | The tools that make the copies in `evidence/`: raw fetch, browser render, manifest, OCR, and text from pages the founder saved. Its README says how to run them. |
| `check_concern_map.py` | The checker for Q1's output: the six files per platform, ids and references, placement values, and every quote against its source. |
| `q1_gaps_report.py` | Writes `studies/concern-map/gaps-to-close.md` from each platform's gaps. |
| `q1_held_check.py` | Checks every Q1 gap against what is held, and re-routes the gaps that went to the founder (Stage 0). |
| `q1_list_joins.py` | Candidate statements for Q1's Salla and WooCommerce re-passes. |
| `q1_shopify_joins.py` | Candidate statements for Q1's Shopify re-pass. |
| `q1_side_by_side.py` | The combined Q1 map: matched concerns side by side, each platform in its own words. |
| `build_yemen_cases.py` | Builds Stage 1's axes, constants and cases from its pass 2 files, by the rules of `studies/yemen-cases/brief.md`. |
| `test_build_yemen_cases.py` | Tests `build_yemen_cases.py` against those rules. |
| `join_pass1.py` | Joins Stage 1's pass 1 parts. |
| `join_pass2.py` | Joins Stage 1's step 2b files for the build. |
| `check_yemen_cases.py` | Checks Stage 1's output against its brief. |
| `check_subject.py` | Checks a subject's files against its briefs (Stages 2 and 4), with the subject's own bullets (its `bullets.tsv`). |
| `seed_subject.py` | Copies what is already recorded for a subject's concerns, in the concern map and in earlier subjects, into the subject's folder for its phase A agents (Stage 4, "from what is recorded"). |
| `subject_slice.py` | Cuts a subject's phase A files into one slice per root decision, for the agents that work on one decision each, and prints the part of a slice an agent asks for. |
| `merge_slices.py` | Joins the files the agents of one root decision each wrote into the subject's own files, and refuses ids outside a decision's range, a bullet outside it, or more variation points than its cap. |
| `second_pass_list.py` | Writes phase B's second-pass work list per root decision: first the rows gap-closing worked, to revisit, each with its leads, the statements gap-closing found for the point under its bullet; then the statements still to place, from the checker's `unplaced.tsv`, but those leads; then the statements `b/second-pass.md` lists, to read again or to note. `--check` lists the revisit, reread and note tasks without an outcome in their root decision's ledger, `b/<root decision>/done.tsv`. |
| `round_tasks.py` | After a round of gap-closing or an audit adds statements, appends phase B's tasks for that round to the real work lists: the new statements to place, the rows naming a gap since settled, and every revisit whose leads have no other task. |
| `variants_edit.py` | Edits one root decision's phase B files row by row, for the second pass: joins statements to a variant, taking its kind and scope again from all of them; adds, replaces or removes a variant, with the next free id of the decision's range; records a task's outcome in the ledger; adds a platform's words to a point's `x_words`, or a note to a point or a row. It refuses an excerpt not in its statements, a statement outside the slice, and an unknown basis. |
| `point_view.py` | Prints what phase C reads on a variation point: each platform's rows in the brief's three groups, with each row's excerpt and evidence, each statement's kind, scope and release marker, the statements under (h) that condition them, and what a gap asks or an absence says. `--records` prints statements, gaps and absences whole by id, with their kind. |
| `analysis_edit.py` | Writes, shows and checks one root decision's phase C files from S-02 on: a point's keys (the answer each row gives), and from them what each platform does on each key (gives, lacks, open, not stated) and the cause the mechanical tests give; a row per key (`answers.tsv`) and per point (`points.tsv`); and notes under a part's heading. It refuses what the brief's rules exclude, such as a cause outside its tags, a rule outside its tables, a founder decision judged cheap, or `no difference` for a key some platform doesn't give. |
| `schema_type.py` | Prints a GraphQL type in full from a schema the observed repositories hold, with the citation a quote from it takes. |
| `held_index.py` | What observed-sa, observed-sh and this repository's capture runs hold, by address, and in what readable form. |
| `quote_check.py` | Is a quote found, word for word, in its cited source, and, for a web page, in the page as it renders or only in its source? Shared by the checkers, and run alone to test a statement or a quote before it is written, a batch of them at once, or to print a source's text as the checker sees it. |
| `source_kinds.py` | The kind of a cited source, assigned by rule (`PLAN.md`, section 6, the test form). |
| `warc_text.py` | Prints one record of a fetch archive held in git. |
| `corpus_search.py` | Searches a platform's held text in every language it holds, for a claim of absence (`PLAN.md`, section 6). |
| `runs_corpus.py` | The observed repositories' runs, as documents for `corpus_search.py`. |
| `count_tokens.py` | Counts the tokens an agent run processed, once per request (`PLAN.md`, Stage 4). |
| `check_register.py` | Checks every citation in a subject's decision register: ids, paths at a commit, and that each cited line holds what the citation names. |
| `register_items.py` | Lists the founder items of a subject's phase C that its register answers in no row, or in two: every item must be answered, or moved to another subject, exactly once. |
| `check_report.py` | Checks each quote in a report against the line its pinned citation names. |
| `check_surface.py` | Searches the working files for the framings of the work that is now history, and fails where one appears outside the places allowed to name it (`PLAN.md`, risk 14). |
