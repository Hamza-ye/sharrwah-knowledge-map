# Brief: S-01, auditing one platform's claims of absence (pilot, step 1, phase A3)

This is `PLAN.md` Stage 2, the pilot. It runs after phase A2 and before B's second pass. You are one agent with one task, for one platform. The message that started you names the platform. You made none of the claims you audit.

**Why.** A claim that something isn't there, such as a gap or an absence, is the easiest kind to get wrong. Held articles have already been found that state what earlier agents recorded as missing.

**Read only:**
- this brief;
- `briefs/A-one-platform.md`, whose inputs and rules you follow for anything you record;
- your platform's files in `studies/subjects/S-01/<platform>/`;
- `studies/subjects/S-01/variation-points.tsv`;
- the held and live sources you are pointed to below.

## The task

Audit every claim of absence your platform's files make:
- every gap in `gaps.tsv` except those of kind `page not read`;
- every absence in `absences.tsv`.

For each claim:
1. **Search the held corpora.** Run `python3 -I method/corpus_search.py <platform> <terms>`:
   - with your platform's own words for what is claimed missing, in every language it uses, taken from `terms.tsv` and its statements;
   - again with each country, plan, arrangement or partner its statements name.

   Read the titles and snippets it lists.
2. **Read every listed document** that could state what is claimed missing, and the pages in the gap's `route`.
3. **Settle the claim:**
   - If a source states it, record new statements and citations under phase A's rules, continuing your platform's ids. The result is `contradicted`. Record too anything else the documents you read state on the subject, with the scope they give it.
   - If a source shows that an absence's list isn't complete, the result is `contradicted`.
   - If sources state only part of what the claim says is missing, such as one arrangement of several, record what they state. The result is `partly contradicted`, and `note` says what part still stands.
   - Otherwise the result is `confirmed`.
4. **Don't change existing rows,** with one exception. Under phase A's rule for (e), you may add your new statements' `stmt_id`s to an existing (e) statement's `conditions`.

## Output, in `studies/subjects/S-01/<platform>/`

`absence-audit.tsv` holds one row per claim, written as soon as it is settled. It is tab-separated, with a header row and no quoting. Columns:
- `claim_id`: the gap_id or absence_id;
- `searches`: each corpus_search command you ran, `;`-separated;
- `read`: each document you read, at its commit or with the date you read it;
- `result`: `confirmed`, `partly contradicted` or `contradicted`;
- `stmt_ids`: for either kind of contradiction, the statements you added;
- `note`.

Add a section headed "Absence audit" to `notes.md`, covering:
- what you found;
- searches whose results were too many to read in full, and how you narrowed them;
- problems with the method.
