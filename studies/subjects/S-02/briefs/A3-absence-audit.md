# Brief: S-02, auditing one platform's claims of absence (step 1, phase A3)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task, for one platform. The message that started you names the platform, and the claims, if you audit only some of them. You made none of the claims you audit.

**Why.** A claim that something isn't there, such as a gap or an absence, is the easiest kind to get wrong. In the pilot, held articles were found that state what earlier agents had recorded as missing.

**Read only:**
- this brief;
- `briefs/A-one-platform.md`, whose inputs, tools and rules you follow for anything you record. Its stop at 300 statements counts only the statements you add;
- your platform's files in `studies/subjects/S-02/<platform>/`. Look rows up with scripts or `grep`, and don't load a large file whole: Shopify's `statements.tsv` and `citations.tsv` hold 588 and 1,802 rows;
- in `handoffs/`, the capture requests your gaps' routes name;
- the held and live sources the steps below point you to.

## The task

Audit every claim of absence your platform's files make:
- every gap in `gaps.tsv` except those of kind `page not read`, including the gaps routed to a capture request (`who_can` `capture`);
- every absence in `absences.tsv`.

For each claim:
1. **Search the held corpora** with `python3 -I method/corpus_search.py <platform> <terms>`:
   - **first, with your platform's own words** for what is claimed missing, in every language it uses, taken from `terms.tsv`, the claim, and the statements the claim names;
   - **then, for each kind of name** the claim and those statements give (countries, plans, settings or parties), one search with those names as its terms, and the platform's general word for what is claimed after `--with`, such as `--with الدولة country`.

   Read the titles and snippets it lists. Past its cap, it lists only addresses: rerun with `--max` at least the number of documents its last line reports, or narrow the terms. A Zid help page is matched on its article alone, without the help centre's menu.
2. **Read every listed document** that could state what is claimed missing, and the pages in the gap's `route`. Run `method/held_index.py` on an address before you read it live.
   - **Reading live.** A page that isn't held may be read live when it is on your platform's own sites:
     - for Shopify and Salla, the hosts phase A names;
     - for Zid, zid.sa with its help and docs, and zid.eg;
     - for WooCommerce, woocommerce.com and Automattic's legal pages;
     - for BigCommerce, bigcommerce.com with its docs and support pages, and commerce.com's legal pages.

     Read it as phase A says ("Reading a live page"). A page you can't read, behind a login or a bot challenge, goes in `read` as not read.
3. **Settle the claim:**
   - If a source states it, record new statements and citations under phase A's rules, continuing your platform's ids. The result is `contradicted`.
   - If a source shows that an absence's list isn't complete, record the statement that shows it. The result is `contradicted`.
   - If sources state only part of what the claim says is missing, record what they state. The result is `partly contradicted`, and `note` says what part still stands.
   - Otherwise the result is `confirmed`.
   - **A gap routed to a capture request** (`handoffs/`) that you contradict or partly contradict: say so in `note`, naming the request, so the coordinator can withdraw or narrow it.
4. **Whatever the result,** record too anything else the documents you read state under S-02's bullets, with the scope they give it. Each statement you add names its claim in its `note`.
5. **Don't change existing rows,** with one exception. Phase A's rule for (h) applies to what you add: an existing (h) statement whose arrangement one of your new statements describes takes its `stmt_id` in `conditions`, for statements under (a) to (f) only. If that column is `none stated`, the ids replace it.
6. **Write as you go.** Write each claim's row as soon as it is settled, so that if you are stopped, the next run continues from your files.

## Output, in `studies/subjects/S-02/<platform>/`

`absence-audit.tsv` holds one row per claim. It is tab-separated, with a header row and no quoting. Columns:
- `claim_id`: the gap_id or absence_id;
- `searches`: each corpus_search command you ran, `;`-separated;
- `read`: each document you read. Give a held copy by its path at its commit, as `held_index.py` prints it, and a live page by its URL and the date you read it;
- `result`: `confirmed`, `partly contradicted` or `contradicted`;
- `stmt_ids`: every statement you added for the claim; for either kind of contradiction, also the recorded statements that show it;
- `note`.

Add a section headed "Absence audit" to `notes.md`, covering:
- what you found;
- searches whose results were too many to read in full, and how you narrowed them;
- problems with the method.

**Before you finish,** check your platform's files on a copy that holds only them, as phase A's brief says. Fix every line of level `error` on what you added or changed:
- your new statements, citations and terms;
- your audit rows, keyed by claim id;
- the (h) statements whose `conditions` you changed.

No line may remain saying a claim of yours isn't settled. `pending capture` lines are live pages the coordinator captures later: leave them.
