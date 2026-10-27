# Brief: S-02, auditing one platform's claims of absence (step 1, phase A3)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task, for one platform. The message that started you names the platform. You made none of the claims you audit.

**Why.** A claim that something isn't there, such as a gap or an absence, is the easiest kind to get wrong. In the pilot, held articles were found that state what earlier agents had recorded as missing.

**Read only:**
- this brief;
- `briefs/A-one-platform.md`, whose inputs, tools and rules you follow for anything you record. Its stop at 300 statements counts only the statements you add;
- your platform's files in `studies/subjects/S-02/<platform>/`. Look rows up with scripts or `grep`, and don't load a large file whole: Shopify's `statements.tsv` and `citations.tsv` hold 588 and 1,802 rows;
- the held and live sources the steps below point you to.

## The task

Audit every claim of absence your platform's files make:
- every gap in `gaps.tsv` except those of kind `page not read`, including the gaps routed to a capture request (`who_can` `capture`);
- every absence in `absences.tsv`.

For each claim:
1. **Search the held corpora.** Run `python3 -I method/corpus_search.py <platform> <terms>`:
   - with your platform's own words for what is claimed missing, in every language it uses, taken from `terms.tsv` and its statements;
   - again with each country, plan, setting or party its statements name.

   Read the titles and snippets it lists.
2. **Read every listed document** that could state what is claimed missing, and the pages in the gap's `route`. Run `method/held_index.py` on an address before you fetch it live.
3. **Settle the claim:**
   - If a source states it, record new statements and citations under phase A's rules, continuing your platform's ids. The result is `contradicted`. Record too anything else the documents you read state under S-02's bullets, with the scope they give it.
   - If a source shows that an absence's list isn't complete, the result is `contradicted`.
   - If sources state only part of what the claim says is missing, record what they state. The result is `partly contradicted`, and `note` says what part still stands.
   - Otherwise the result is `confirmed`.
   - **A gap routed to a capture request** (`handoffs/`) that you contradict or partly contradict: say so in `note`, naming the request, so the coordinator can withdraw or narrow it.
4. **Don't change existing rows,** with one exception. Under phase A's rule for (h), you may add your new statements' `stmt_id`s to an existing (h) statement's `conditions`. If that column is `none stated`, the ids replace it.
5. **Write as you go.** Write each claim's row as soon as it is settled, so that if you are stopped, the next run continues from your files.

## Output, in `studies/subjects/S-02/<platform>/`

`absence-audit.tsv` holds one row per claim. It is tab-separated, with a header row and no quoting. Columns:
- `claim_id`: the gap_id or absence_id;
- `searches`: each corpus_search command you ran, `;`-separated;
- `read`: each document you read, at its commit or with the date you read it;
- `result`: `confirmed`, `partly contradicted` or `contradicted`;
- `stmt_ids`: for either kind of contradiction, the statements that show it: those you added, or ones already recorded;
- `note`.

Add a section headed "Absence audit" to `notes.md`, covering:
- what you found;
- searches whose results were too many to read in full, and how you narrowed them;
- problems with the method.

**Before you finish,** check your platform's files on a copy that holds only them, as phase A's brief says, and fix every line of level `error` on your ids.
