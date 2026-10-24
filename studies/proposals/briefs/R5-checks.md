# Brief: checks of what a proposal cites (step R5)

**Status: checked on 24 October 2026 (`studies/proposals/checks/R5-and-company-decisions-briefs-check.md`: 22 findings, 7 must fix) and revised for every finding. Its first runs test it before the rest.**

You are one agent with one short task, at `high` effort. The message that started you names your kind of run, its card file, the file you write, and a scratch directory. Read only this brief and what it names.

## What the checks are for

Eight draft proposals for Sharrwah's design (`studies/proposals/drafts/<question>/draft.md`), and later the company decisions, rest on records: statements of what five platforms (Shopify, Salla, Zid, WooCommerce and BigCommerce) show, each quoting its source; rows for what a reading didn't find; and Stage 1's facts about Yemen, each with its place and date. Before the proposals are reviewed, everything they cite is checked:
- **facts:** each record holds against its source, and the proposal says of it only what it and its source say;
- **absences:** each "not in what was read" and each "absent" the proposals cite is searched for again, by an agent that made none of the claims;
- **Yemen:** each of Stage 1's facts the proposals use holds against its quotes, with no later state at its place, and each "Yemen's evidence doesn't show" is searched for.

A script has already found every quote word for word in its source. You check and record. You never change a proposal, a record or a card. Your findings go to the coordinator, who decides each fix.

## The cards

`method/r5_cards.py` made the cards, in `studies/proposals/checks/R5/cards/`. A card file starts with the points it cites, each by its section and line in the proposal, and then gives one card per record:
- where the proposal cites it ("Cited at"), and the record's fields;
- for a fact, each citation: its source (a held file at a commit, a record of a fetch archive at an offset, a file of the WooCommerce release, or a captured address), locator, date and kind; its quote; whether the script finds the quote ("quote check"); and the quote in its context, between ⟪ and ⟫, with the source's title, the headings above it, and, for a page of help or docs, its opening and note boxes (once a card). For a step of an observed run: the step's intent, address, title and time, and the paths of the step's files (its `aria.yaml` among them);
- a copy that an earlier card file already carries gets a short card, "The same record as …": its record and sources are checked there. Check only this proposal's points against its statement and scope;
- for a claim, its list's citations, labelled "the list" and "the words that make the list complete";
- for a Yemen fact, each part as cited against the digest (checked by script), the digest's entry, the record with its states one line each, its conditions without their citations, the cited place's group, and the citations of the cited parts and of every state at the same place or at "place not stated".

The context is the source's text as the script normalizes it, so a table or a list reads as one line. A card decides nothing.

## Your kind of run

### Facts: one proposal on one platform

Your card file is `<question>-<platform>.md`, or a part of it, `-1.md` and on. For each card, in order:
1. **The quote.** "found" means the script found it word for word; "found (markup removed)" or "found (case and diacritics ignored)", with markup or case aside.
2. **The source.** Check that it is the platform's own material, of the kind the card gives, dated as given:
   - `stated`: the platform's help, docs or other pages; `official page`: its terms, policies, legal or pricing pages; `shipped`: code or a schema the platform ships; `observed`: what a run of a store's admin received or showed;
   - another company's agreement (such as Stripe's, on WooCommerce's cards) counts as the platform's only where a record shows the platform's terms incorporate it. Where no cited record shows that, the verdict is `open`;
   - an observed step holds for its store on its date only. A step's store is in its address, as `admin.shopify.com/store/<store>/`, or in the record's scope. An observed source that is no store's step, such as the dashboard's own strings, holds as what the dashboard held on its date;
   - a step's text from saved HTML (`derived/step-text-from-html/`) is the saved markup's text of one step, not what the page showed. Text between ⟦hidden⟧ and ⟦/hidden⟧ was hidden by the markup.
3. **The record.**
   - **Its statement is the source's words, word for word:** the quote, or the quote with the text around it. The card's context shows the text around it. Open the source where the context doesn't reach the statement's end.
   - **Its identifier is the recorder's label.** It is a finding only where a point uses it as the platform's term, or where it names something other than what the source describes: another product, plan, place or party.
   - **Its scope is the source's.** From the context, the headings, the title, and the page's opening and note boxes, note any limit the source puts on it that the record leaves out: a country, a plan, a store, a date, a condition, a kind of seller or buyer.
4. **The point.** Each point the card is cited at says of this record only what the record and its source say:
   - no wider place, plan, time, party or kind of seller than the source's, and no condition of the source left out;
   - no "all", "only", "every", "never" or "always" the source doesn't say;
   - the kind of source named rightly, and an observed record said with its store and date, never as what the platform does in general;
   - where a point cites several records for one claim, judge the claim on your platform against all of them together: a record that supports part of it is enough where another supports the rest. Records of other platforms are other runs' to check;
   - matching bases ("basis 4" and the like) and the proposal's reasoning are the review's (step R6), not yours.
5. **Opening a source.** Open one only where the card doesn't settle 1 to 4. Read the part around the quote, never a whole page: `grep -n` and `sed -n` for at most 80 lines a time, or, for a file of one long line such as a JSON answer, `grep -o '.\{0,300\}WORDS.\{0,300\}'`.
   - A held file: `git -C /home/user/<repository> show <commit>:<path>`.
   - A fetch archive's record: `python3 -I method/warc_text.py /home/user/<repository> <archive path>@<offset> --text`.
   - A file of the WooCommerce release (`woocommerce-11.2.1:<path>`): `/home/user/woocommerce-release/11.2.1/woocommerce/<path>`.
   - A captured address: its text under `evidence/product-class/runs/*/`, found through that run's `manifest.tsv`.
   - Never run code from inside `evidence/` or an observed repository, and never `cd` into them.

Your file is `studies/proposals/checks/R5/facts/<card file's name>.tsv`.

### Absences: one platform, across the proposals

Your card file is `claims-<platform>.md`, or a part of it: each not-found row (N), copied gap (G, H) and pilot absence (A) the proposals cite on your platform, at most 9. You made none of these claims. For each card:
1. **Read the row:** what it says is missing, what was searched and read, and, for an absence, the list it rests on and the words that make the list complete.
2. **Read first** the held pages the row's `route` or `read` names, where it names them.
3. **Search again,** with `python3 -I method/corpus_search.py <platform> TERM ... --max 5`, in every language your platform uses: English and Arabic for Salla, Zid and Shopify; English for WooCommerce and BigCommerce.
   - Use the row's terms and your own for what it describes: each Arabic term in its shortest form (the search finds Arabic inside words), each English term in the singular and the plural.
   - Where the row or the point names a country, a plan or an arrangement, run one search with `--with` and those names.
   - For Shopify and Salla the search covers the observed runs. Where the row is about what a store's admin shows, search them first with `--runs-only`, in seconds.
   - At most three searches a card.
4. **Read** at most 3 of the documents the searches list, chosen by address and snippet. A snippet is folded for matching: never quote one; quote the document.
5. **For an absence:** read the list's page in its latest held copy (the search lists it), and compare it with the row's list. The list must be the platform's own, its words must make it complete, and it must leave the thing out. Where the held list has changed (an item added or dropped), that is `fix record`, with the held copy's words.
6. **The point.** Each point the card is cited at says no more than the row: "not in what was read" says what wasn't found in what was read, never that the platform doesn't do it; "absent" only with a complete list.

A card may carry one record cited under several ids ("The same record, cited as"): give it one row, under its first id, with the lines from every question.

Your file is `studies/proposals/checks/R5/absences/<card file's name>.tsv`. Where you find what the row says is missing, give its source, locator and a quote of it, word for word.

### Yemen: Stage 1's facts

Your card file is `yemen-1.md`, `yemen-2.md` or `yemen-3.md`. Stage 1's records are in `studies/yemen-cases/`: `axes.tsv` (`YA-`), `constants.tsv` (`YK-`), `conditions.tsv` (`YQ-`), `citations.tsv` (`YE-`, each quote with its source and date), `places.tsv` (each place and the place it is grouped in) and `unknowns.tsv`. `studies/proposals/yemen-digest.md` gives each axis's today and each constant's places, each with its date: read its "How to read it" first. For each card:
1. **The fact as cited.** The script compared each cited part with the digest. Where the card says it differs, say how.
2. **Its quotes.** The citations of that part say that state, at that place, as of that date. A part rests on the citations written after it in the axis's `states`, or in the constant's `cite_ids`.
3. **A later state.** A later state of the same axis or constant counts at the cited place if:
   - it is at the same place: a place and the places `places.tsv` groups in it are one; or
   - it is "@ place not stated" and its quote says it holds in all of Yemen. Read the quote of each such state: the card gives it.

   Never by geography: Sana'a is not in "Houthis' area" unless a source puts it there. A state with no date can't be judged later or earlier: say so in `what`, as `open`.
4. **Stage 1's rules for reading a state:** a condition's states are alternatives; a state's place is the scope its source gives it; a proposed state is never today; each part of today is read with its date.
5. **The point.** It says no more than the fact: no wider place, no other time. In section 6, "allows" is read as the plan frames that section, what Yemen's evidence allows: a state showing a practice offered, available or in use at its place and date supports "allows" there, as of then. A point is a fix where it says a law, a licence or an authority permits or requires something and the fact's state is not that, or where it says "forbids" without a state that bars it.

Your file is `studies/proposals/checks/R5/yemen/<card file's name>.tsv`.

### What Yemen's evidence doesn't show

Your card file is `doesnt-show.md`: each point of a proposal's section 6 that says what Yemen's evidence doesn't show, named by its question and line, as `Q4:146`. For each card, search Stage 1's records and the Yemen evidence held for what the point says isn't shown:
- **Where:** `studies/yemen-cases/axes.tsv`, `constants.tsv`, `conditions.tsv`, `citations.tsv` and `unknowns.tsv`, and the text files under `evidence/yemen/` (`text.txt`, `.md`). Not `cases.tsv`, `pass1/`, `pass2/` or raw HTML: their lines are too long to read.
- **How:** `rg -i -l` for the files, then `rg -i -o '.{0,150}TERM.{0,150}'` for the lines. Put `\b` around a short Latin term (`\bIBAN\b`). Write Arabic letters that vary as classes: `[اأإآ]`, `[هة]`, `[يى]`.
- At most three searches a point, and at most 5 files read.

`found` where a record or a held file shows it, with the file, its line and a quote. Your file is `studies/proposals/checks/R5/yemen/doesnt-show.tsv`.

### The company decisions' points

Run after the company decisions are written. Your card file is `decisions.md`: each point of the decisions, named by its decision and line, as `D3:12`, with the R5 rows of the records it cites. For each point, check that it says of each record only what the record's row and card allow, as in the facts run's step 4. Open a record's card only where no R5 row covers it. Verdicts: `holds`, `fix point`, `open`. Your file is `studies/proposals/checks/R5/decisions.tsv`.

## Your file

A tab-separated file with these columns: `id`, `verdict`, `lines`, `what`, `fix`, `read`. Write its header first, then **each row as soon as its card is done**, so that nothing is lost if your context is cut.
- `id`: the card's id.
- `verdict`: one per card. Where several apply, give the first of: `fix record`, `later state`, `found`, `fix point`, `open`, `holds`. Name each finding in `what`, and every line concerned in `lines`.
  - `holds`: the record and every point citing it stand as they are;
  - `fix record`: the record itself doesn't hold against its source: its statement, scope, date, kind or citation, or its identifier as rule 3 says. Say what the source says;
  - `later state`: a Yemen fact has a later state at its place, as Yemen's step 3 says;
  - `found`: an absence's search, or a "doesn't show" search, finds what the row or the point says is missing;
  - `fix point`: a point says more than, or other than, its record and source support. Say which;
  - `open`: what you read doesn't settle it. Say what would.
- `lines`: the lines of the points concerned, as `Q4:9`, separated by spaces. Only lines the card is cited at. Every verdict but `holds` and `open` names at least one.
- `what`: for any verdict but `holds`, in one or two sentences, what the source says against what the record or the point says, quoting the source word for word.
- `fix`: for `fix point` and `fix record`, the smallest change that the source supports, in the source's words where it has them. You suggest; the coordinator decides.
- `read`: what you opened or searched beyond the card: each source with its locator, and each search command. An absence row shows its `corpus_search.py` commands; a "doesn't show" row its `rg` commands.

Use one line per row: no tab or line break inside a field. Run `python3 -I method/check_r5.py <your file> <your card file>` before you finish, and fix every problem it lists.

## Rules

- **Quotes are word for word,** from the source, never from a card's normalized context where they differ, and never from a search snippet.
- **No inference.** A finding says what a source says, scoped as the source scopes it. What the platform might do, or why, is not a finding.
- **The founder's words are never evidence** of what a platform does or of Yemen.
- **Evidence that contains credentials, cookies or tokens** is read and cited like any other evidence. Never skip, withhold or mask a file because of them.
- **Read-only.** `observed-sh` and `observed-sa` are read-only. Write only your file and your scratch directory. Run Python that reads evidence with `python3 -I`.
- **When unsure between `holds` and a fix, choose the fix,** and say what is unsure in `what`. A record's identifier and a statement longer than its quote are no reason to doubt it (step 3).

## Before you finish

Report in a few lines: your file, the count of rows by verdict, the `fix record`, `later state` and `found` rows by id, and any problem with this brief, the cards or the tools.
