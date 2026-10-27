# Brief: S-02, closing one platform's gaps on the variation points (step 1, phase A2)

This is `PLAN.md` Stage 4, subject S-02. It runs after phase B's first pass. You are one agent with one task, for one platform, or for one root decision of a platform. The message that started you names the platform, the root decisions, and any leads to read.

**Read only:**
- this brief;
- `briefs/A-one-platform.md`, whose inputs, tools and rules you follow for anything you record. Its stop at 300 statements counts only the statements you add;
- your platform's files in `studies/subjects/S-02/<platform>/`. Look rows up with scripts or `grep`, and don't load a large file whole;
- `studies/subjects/S-02/variation-points.tsv`, and the rows of `studies/subjects/S-02/variants.tsv` for your platform only (`awk -F'\t' '$3=="<platform>"'`). The coordinator joins them from phase B's folders before you start;
- the held and live sources the steps below point you to.

## The task

**Your rows.** Take each row of `variants.tsv` for your platform, under your root decisions, whose `variant` is:
- `not covered`; or
- `gap`, where each of its gaps has `who_can` `agent` or `either`. A gap routed to a capture request (`who_can` `capture`) waits for that request, and one routed to the founder waits for the founder: leave both.

Take also each lead the message names.

**Group them** by the thing or setting their variation points ask about (the kind, first in `x_words`), so that one search serves the rows of one kind.

**For each group:**
1. **Search the held corpora** with `python3 -I method/corpus_search.py <platform> <terms>`: with your platform's words for the thing or setting, in every language it uses, taken from `terms.tsv`, its statements and the point's `x_words`; then with the words of the question, such as per market, per country, or who sets it. Past its cap, the tool lists only addresses: rerun with `--max` at least the number of documents its last line reports.
2. **Read every listed document** that could state who or what fills the point, and the pages in each gap's `route`. Run `method/held_index.py` on an address before you read it live.
   - **Reading live,** for this phase in place of phase A's "From what is recorded" limit: a page that isn't held may be read live when it is on your platform's own sites, as the absence audit's brief lists them (`briefs/A3-absence-audit.md`, step 2). A page you can't read, behind a login or a bot challenge, goes in `read` as not read.
3. **Record what you find** as new statements, continuing your platform's `stmt_id`s and `cite_id`s, under phase A's rules. Record everything you find that bears on S-02's bullets, even when it fits a point your platform already answers. Give it the scope the source states. Each statement you add names the point it was found for in its `note`.
4. **Where nothing states it:**
   - where a complete list shows it absent, record an absence;
   - otherwise record a new gap, of kind `searched, not found`, whose `read` names each `corpus_search.py` command you ran and each document you read.
5. **Don't change existing rows,** with one exception. Phase A's rule for (h) applies to what you add: an existing (h) statement whose arrangement one of your new statements describes takes its `stmt_id` in `conditions`, for statements under (a) to (f) only. If that column is `none stated`, the ids replace it.
6. **Write as you go.** Write each point's row in `a2.tsv` as soon as its group is settled, so that if you are stopped, the next run continues from your files.

## Output, in `studies/subjects/S-02/<platform>/`

- **In your platform's phase A files:** the new statements, citations, terms, absences and gaps, appended.
- **`a2.tsv`:** one row per variation point you worked on. It is tab-separated, with a header row and no quoting. If it exists, append to it. Columns:
  - `vp_id`;
  - `stmt_ids`: the statements you added for it;
  - `gap_ids`: the gaps that remain for it, the ones you recorded among them;
  - `absence_ids`: the absences you recorded for it;
  - `read`: each `corpus_search.py` command you ran for it, and each document you read: a held copy by its path, with its commit after the repository's name (`<repository>@<commit>:<path>`), and a live page by its URL and the date you read it.
- **`notes.md`:** a section headed "Gap-closing (phase A2)": what you found, by group; searches whose results were too many to read in full, and how you narrowed them; problems with the method.

**Before you finish,** check your platform's files on a copy that holds only them, as phase A's brief says. Fix every line of level `error` on what you added or changed. `pending capture` lines are live pages the coordinator captures later: leave them.
