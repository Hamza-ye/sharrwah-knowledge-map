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
| `schema_type.py` | Prints a GraphQL type in full from a schema the observed repositories hold, with the citation a quote from it takes. |
| `held_index.py` | What observed-sa, observed-sh and this repository's capture runs hold, by address, and in what readable form. |
| `quote_check.py` | Is a quote found, word for word, in its cited source? Shared by the checkers, and run alone to test a statement or a quote before it is written. |
| `source_kinds.py` | The kind of a cited source, assigned by rule (`PLAN.md`, section 6, the test form). |
| `warc_text.py` | Prints one record of a fetch archive held in git. |
| `corpus_search.py` | Searches a platform's held text in every language it holds, for a claim of absence (`PLAN.md`, section 6). |
| `runs_corpus.py` | The observed repositories' runs, as documents for `corpus_search.py`. |
| `count_tokens.py` | Counts the tokens an agent run processed, once per request (`PLAN.md`, Stage 4). |
| `check_register.py` | Checks every citation in a subject's decision register: ids, paths at a commit, and that each cited line holds what the citation names. |
| `check_report.py` | Checks each quote in a report against the line its pinned citation names. |
| `check_surface.py` | Searches the working files for the framings of the work that is now history, and fails where one appears outside the places allowed to name it (`PLAN.md`, risk 14). |
