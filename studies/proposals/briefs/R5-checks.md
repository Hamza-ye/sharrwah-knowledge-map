# Brief: checks of what a proposal cites (step R5)

**Status: written on 24 October 2026; to be checked before it runs.**

You are one agent with one short task, at `high` effort. The message that started you names your kind of run, its card file, the file you write, and a scratch directory. Read only this brief and what it names.

## What the checks are for

Eight draft proposals for Sharrwah's design (`studies/proposals/drafts/<question>/draft.md`) rest on records: statements of what five platforms (Shopify, Salla, Zid, WooCommerce and BigCommerce) show, each quoting its source; rows for what a reading didn't find; and Stage 1's facts about Yemen, each with its place and date. Before the proposals are reviewed, everything they cite is checked:
- **facts:** each record holds against its source, and the proposal says of it only what it and its source say;
- **absences:** each "not in what was read" and each "absent" the proposals cite is searched for again, by an agent that made none of the claims;
- **Yemen:** each of Stage 1's facts the proposals use holds against its quotes, with no later state at its place, and each "Yemen's evidence doesn't show" is searched for.

You check and record. You never change a proposal, a record or a card. Your findings go to the coordinator, who decides each fix.

## The cards

`method/r5_cards.py` made a card for each record a proposal cites, in `studies/proposals/checks/R5/cards/`. A card file starts with the points it cites, each by its section and line in the proposal, and then gives one card per record:
- where the proposal cites it ("Cited at");
- the record's fields;
- for a fact, each citation: its source (a held file at a commit, a record of a fetch archive at an offset, or a captured address), locator, date and kind; its quote; whether the script finds the quote in the source ("quote check"); and the quote in its context, between ⟪ and ⟫, with the source's title and the headings above it where the source has them. For a step of an observed run, the step's intent, address, title and time.

The context is the source's text as the script normalizes it, so a table or a list reads as one line. A card decides nothing.

## Your kind of run

### Facts: one proposal on one platform

Your card file is `<question>-<platform>.md`. For each card, in order:
1. **The quote.** "found" means the script found it word for word; "found (markup removed)" or "found (case and diacritics ignored)", with markup or case aside. "not found" or "unresolved": open the source and look for it.
2. **The source.** It is the platform's own material, of the kind the card gives, dated as given:
   - `stated`: the platform's help, docs or other pages; `official page`: its terms, policies, legal or pricing pages; `shipped`: code or a schema the platform ships; `observed`: what a run of a store's admin received or showed;
   - an observed source holds for its store on its date only. A step's store is in its address, as `admin.shopify.com/store/<store>/`, or in the record's scope;
   - a step's text from saved HTML (`derived/step-text-from-html/`) is the saved markup's text of one step, not what the page showed. Text between ⟦hidden⟧ and ⟦/hidden⟧ was hidden by the markup.
3. **The record.** It says what its quote says: its statement is the quote or a part of it; its identifier names what the source names; its scope is the source's. From the context, the headings and the title, note any limit the source puts on it that the record leaves out: a country, a plan, a store, a date, a condition, a kind of seller or buyer.
4. **The point.** Each point the card is cited at says of this record only what the record and its source say:
   - no wider place, plan, time, party or kind of seller than the source's;
   - no "all", "only", "every", "never" or "always" the source doesn't say;
   - the kind of source named rightly, and an observed record said with its store and date, never as what the platform does in general;
   - where a point cites several records for one claim, judge the claim on your platform against all of them together: a record that supports part of it is enough where another supports the rest. Records of other platforms are other runs' to check;
   - matching bases ("basis 4" and the like) and the proposal's reasoning are the review's (step R6), not yours.
5. **Opening a source.** Open one only where the card doesn't settle 1 to 4: read the part around the quote with `grep -n` and `sed -n` (at most 80 lines a time), never a whole page. A held file: `git -C /home/user/<repository> show <commit>:<path>`. A fetch archive's record: `python3 -I method/warc_text.py /home/user/<repository> <archive path>@<offset> --text`. A captured address: its text under `evidence/product-class/runs/*/`, found through that run's `manifest.tsv`. Never run code from inside `evidence/` or an observed repository, and never `cd` into them.

Record one row per card in your file, `studies/proposals/checks/R5/facts/<question>-<platform>.tsv`.

### Absences: one platform, across the proposals

Your card file is `claims-<platform>.md`: each not-found row (N), copied gap (G, H) and pilot absence (A) the proposals cite on your platform. You made none of these claims. For each card:
1. **Read the row:** what it says is missing, what was searched and read, and, for `absent`, the list it rests on and the words that make the list complete.
2. **Search again,** with `python3 -I method/corpus_search.py <platform> TERM ... --max 10`, in every language your platform uses: English and Arabic for Salla, Zid and Shopify; English for WooCommerce and BigCommerce. Use the row's terms, and your own for what it describes, each Arabic term in its shortest form (the search finds Arabic inside words) and each English term in the singular and the plural. Where the row or the point names a country, a plan or an arrangement, run one search with `--with` and those names. For Shopify and Salla the search covers the observed runs; `--runs-only` runs over them alone, in seconds. At most three searches a card.
3. **Read** at most 5 of the documents the searches list, chosen by address and snippet. A snippet is folded for matching: never quote one; quote the document.
4. **For `absent`:** check that the list is the platform's own, that its words make it complete, and that it leaves the thing out.
5. **The point.** Each point the card is cited at says no more than the row: "not in what was read" says what wasn't found in what was read, never that the platform doesn't do it; "absent" only with a complete list.

Record one row per card in `studies/proposals/checks/R5/absences/<platform>.tsv`. Where you find what the row says is missing, give its source, locator and a quote of it, word for word.

### Yemen: Stage 1's facts, and what Yemen's evidence doesn't show

Your card file is `yemen.md`, or the part of it the message names. Stage 1's records are in `studies/yemen-cases/`: `axes.tsv` (`YA-`), `constants.tsv` (`YK-`), `conditions.tsv` (`YQ-`), `citations.tsv` (`YE-`, each quote with its source and date), `places.tsv` (each place and the place it is grouped in) and `unknowns.tsv`. `studies/proposals/yemen-digest.md` gives each axis's today and each constant's places, each with its date: read its "How to read it" first. For each card:
1. **The fact as cited.** Each point gives the id with a state, a place after "@", and a date. They are the digest's for that id: the part of the axis's today, or of the constant, it names.
2. **Its quotes.** The citations of that part say that state, at that place, as of that date. A part rests on the citations written after it in the axis's `states`, or in the constant's `cite_ids`.
3. **A later state.** No later state of the same axis or constant holds at the same place, or at a place that contains it. Only a state whose source says it holds in all of Yemen ("across Yemen") contains every place. Look in the row's `states`, `note` and `today`, and in `conditions.tsv` for its `condition_ids`.
4. **Stage 1's rules for reading a state:** a condition's states are alternatives; a state's place is the scope its source gives it; a proposed state is never today; each part of today is read with its date.
5. **The point.** It says no more than the fact: no wider place, no other time, and "allows" or "forbids" only where the fact's state does.

Then, where the message names them, each point of a proposal's section 6 that says what Yemen's evidence doesn't show (`python3 -I method/check_proposals.py drafts <question> --cited` gives their lines). Search Stage 1's records and the Yemen evidence held (`evidence/yemen/`) for it, with `rg -i` and its terms in Arabic and English: at most three searches a point, and at most 5 files read. Record what you find, with the file, its line and a quote.

Record one row per card, and one per point, in `studies/proposals/checks/R5/yemen/<part>.tsv`.

## Your file

A tab-separated file with these columns, one row per card (and, in a Yemen run, per point):
- `id`: the card's id; for a section 6 point, `<question>:<line>`;
- `verdict`, one of:
  - `holds`: the record and every point citing it stand as they are;
  - `fix point`: a point says more than, or other than, its record and source support. Say which;
  - `fix record`: the record itself doesn't hold against its source (its statement, identifier, scope, date, kind or citation). Say what the source says;
  - `found`: an absence's search, or a "doesn't show" search, finds what the row or the point says is missing;
  - `later state`: a Yemen fact has a later state at its place or a place containing it;
  - `open`: what you read doesn't settle it. Say what would;
- `lines`: the lines of the points concerned, as `Q4:9`, separated by spaces; empty for `holds`;
- `what`: for any verdict but `holds`, in one or two sentences, what the source says against what the record or the point says, quoting the source word for word;
- `fix`: the smallest change to the point or the record that the source supports, in the source's words where it has them. You suggest; the coordinator decides;
- `read`: what you opened or searched beyond the card: each source with its locator, and each search command.

Use one line per row: no tab or line break inside a field. Run `python3 -I method/check_r5.py <your file> <your card file>` before you finish. It checks the columns, the verdicts and that every card has its row.

## Rules

- **Quotes are word for word,** from the source, never from a card's normalized context where they differ, and never from a search snippet.
- **No inference.** A finding says what a source says, scoped as the source scopes it. What the platform might do, or why, is not a finding.
- **The founder's words are never evidence** of what a platform does or of Yemen.
- **Evidence that contains credentials, cookies or tokens** is read and cited like any other evidence. Never skip, withhold or mask a file because of them.
- **Read-only.** `observed-sh` and `observed-sa` are read-only. Write only your file and your scratch directory. Run Python that reads evidence with `python3 -I`.
- **When unsure between `holds` and a fix, choose the fix,** and say what is unsure in `what`.

## Before you finish

Report in a few lines: your file, the count of rows by verdict, the `fix record` and `found` rows by id, and any problem with this brief, the cards or the tools.
