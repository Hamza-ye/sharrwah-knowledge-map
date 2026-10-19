# Brief: one question's records on Shopify or Salla, re-checked against the observed runs (step R3, re-check)

**Status: written 19 October 2026, for the founder's decision of that day; revised after its first two runs (Q6 on Shopify and on Salla).**

You are one agent with one task: one question, on Shopify or Salla. The message that started you names both, and a scratch directory. Your folder is `studies/proposals/records/<question>/<platform>/`, which a recording run filled. You run at `medium` effort.

**Why you run.** The recording run read your platform's published material: help pages, documents, legal pages, fetch archives. It didn't read what the observed repository's runs hold: what the platform's own admin answered, and what each step's page showed, in stores used for real, in sweeps and journeys alike. The corpus search now covers them.

**Your task:** re-check your folder's open items against the runs, record what the runs show as new statements, check the wording of every not-found row against what was read, and update the account.

Don't answer the question in your own words, compare your platform with any other, or judge it.

## Read only

- this brief;
- `studies/proposals/briefs/R3-recording.md`, its sections "Rules", "Quotes and citations" and "Output, in your folder". They hold here, except where this brief says otherwise. If your folder is a check (its account's points start with labels such as "the same" or "goes beyond"), also `studies/proposals/briefs/R3-checking.md`, for how a check's account labels its points;
- your question, in `studies/proposals/questions-for-agents.md`: its own section, and "How a run uses its question";
- the files in your folder;
- your observed repository's own guides, at its commit: `README.md` and `docs/READING.md`. Read both whole, first;
- the runs' files and the indexes and tables the guides describe, at the commit;
- a page of your platform's published material, held or live as `R3-recording.md`'s table gives it, only where a run's step names or links it and you need its words.

| Platform | Repository | Root | Commit |
| --- | --- | --- | --- |
| shopify | observed-sh | `/home/user/observed-sh` | `c8b5fbee25966372a0475e6ed81f0b7760ac2921` |
| salla | observed-sa | `/home/user/observed-sa` | `4ca2e896a729215f422a137a364e7e9488610ba3` |

**Finding what the runs hold.** `python3 -I method/corpus_search.py <platform> <terms> [--max N] [--with <terms>]` lists, besides the published material, these corpora:
- `observed-sh: answers`: every distinct answer the Shopify admin's own API gave a run's pages, each with its operation, store, run and steps;
- `observed-sa: saved responses`: every distinct JSON answer Salla's hosts gave a run's pages, each with its method, address, status, store, run and step;
- `<repository>: run steps`: what each step's page showed (`steps/NNN.aria.yaml`, `NNN.text.txt` and its frames), titled with the step's page title and the capture's intent; a terminal run's transcript; a step's downloaded files;
- `<repository>: run requests`: what a run's pages sent (observed-sh's `guard.jsonl`, observed-sa's `writes.jsonl`), one line each;
- `<repository>: indexes and derived tables`: observed-sh's `index/operations.jsonl` and `derived/`, observed-sa's `index/rest-endpoints.tsv` and `derived/`, one line each;
- `<repository>: structures`: the structures' `source.*` files, and Salla's `items.jsonl` lines.

A run document is listed by its own place, never merged with another store's or run's. The same answer received in several runs is one document, listing each place.

**Reading a run's file.** Run `git --git-dir=<root>/.git show <commit>:<path>` from outside the repository.
- Answers and saved responses are JSON, often one long line. Never print one over 20 KB whole.
- Some saved responses write Arabic as `\uXXXX` escapes. Quote such Arabic as the letters it stands for: the checker reads a JSON file with its escapes decoded. To see them, pipe the file to `python3 -I -c 'import json,sys; print(json.dumps(json.load(sys.stdin), ensure_ascii=False))'`. Print the part you need: pipe it to `python3 -I -c '<code>'` that reads stdin and prints the keys or items you want, or use `grep -o '.\{0,200\}<term>.\{0,200\}'`.
- A step's files are `raw/runs/<run>/steps/NNN.aria.yaml` and `NNN.text.txt`. The search lists them as `raw/runs/<run>/steps/ (NNN.aria.yaml, NNN.text.txt, …)`: cite the one file that holds your quote. The run's `actions.jsonl` gives each step's address and page title.
- What an operation asks: observed-sh's `derived/admin-operations.jsonl` prints each operation's query. `index/operations.jsonl` lists the runs and steps that called it. For Salla, `index/rest-endpoints.tsv` lists each endpoint the pages called.

**Pointers.** These places have been pointed at. They are places to read, not evidence. Read one only where it bears on a sentence of your question, and record only what its files show:
- **Shopify:**
  - the answers of the operations `PaymentProviders`, `ShopifyPaymentsData` and `MarketsHomeCurrencyOptions`;
  - the journey run `20260930T014656Z-journey-order-lifecycle`;
  - each store's General settings page (`/settings/general`) in the sweeps;
  - the third-party payment providers pages (`/settings/payments/third-party-providers`), and any journey that installs one.
- **Salla:**
  - the onboarding question pages (`/persona/qna`) and their saved responses (`/admin/v2/onboarding/…`);
  - the payments module's saved responses, with its list of gateways.

**Don't open:** what `R3-recording.md` forbids, and in the observed repository its `docs/LOG.md`, `docs/PLAN.md`, `index/run-notes.tsv` and `index/instruments.json` beyond the stores' names. They are the capture's own notes.

## Steps

1. **Read the two guides.**
2. **List your open items,** in your scratch directory:
   - every row of `not-found.tsv`;
   - every copied gap (`G`, and the pilot's `H`) that `account.md` cites;
   - the phrases the starting message lists, if any. The coordinator's check didn't find them in what their rows read.
3. **Re-check each open item against the runs.** Run one corpus search in your platform's own words for what is missing, in each language it uses, as alternatives in one call, with `--max 10`. If the item is about a store, plan, country or provider, add `--with` and their names. Read at most 3 of the run documents it lists whose title or snippet could show it.
   - **If what you read shows what is missing,** record it as statements (rules below), and close the item:
     - **a not-found row:** move it, unchanged, from `not-found.tsv` to `not-found-closed.tsv`, which has the same columns and one more at the end, `closed_by`: the ids of the statements that close it, `;`-separated;
     - **a copied gap:** the closing statement's `note` names the gap's id. Copies are never edited.
   - **If it shows a part,** record that part, and narrow the row's `what_is_missing` to what is still missing.
   - **If it shows nothing,** add your search to the row's `searched`, and the run documents you opened to its `read`, with their commit.
   - **A row routed to the founder or to either** (`who_can`): if a run shows the page or setting it asks for, read it there. Then the row closes or narrows, and any row that stays is routed as what is still missing. `python3 -I method/held_index.py <url>` now also lists the runs' steps whose page ended at an address, and the checker reports a route to the founder whose address a step holds.
4. **Check each row's wording.** For every not-found row that stays, every name, label, path or phrase it gives as the platform's must be in what its `read` names or in your folder's records:
   - keep a detail only if one of them shows it, and word it as they do;
   - a detail nothing read shows comes out of the row;
   - list each change in `notes.md`.
5. **Read the runs for each sentence of your question.** For each sentence, run one corpus search in your platform's own words, in each language it uses, as alternatives in one call, with `--max 10`. Read at most 3 of the run documents it lists, and the pointers that bear on the sentence.
   - Before you record a statement, search `copied-view.tsv` and `statements.tsv` with `grep` for a distinctive phrase of it. If a copy or statement already says it, don't record it again.
   - A sentence that only gives examples or limits, or restates the question, shares the reading of the sentence it serves.
6. **Update `account.md`:**
   - add a point for what the new statements show, each point ending with its ids;
   - change or remove each point that rested on a closed item, and add the new ids to points they bear on;
   - in a check, label each new point as `R3-checking.md` says. "the same" and "differs" name the in-depth point they match, and the basis.

   The account may grow to about 2,300 words.
7. **Write `notes.md`'s new section** (Output), run the checker, and fix what it reports.

## Rules for what the runs show

These add to `R3-recording.md`'s rules 1 to 12, which hold.
- **A statement from a run** is the platform's own data or words as the run holds them: the keys and values of an answer or saved response, or a step's page text. Copy it verbatim from the file, as `git show` prints it. Keep its keys, so that each value says what it is, such as `"eligible":false`.
  - Its `identifier` is the operation or endpoint, and the keys that lead to the value, as the answer names them, such as `ShopifyPaymentsData: shopifyPaymentsAccount.eligible`.
  - A list in an answer, such as the providers a page offered, is recorded in full, as one statement (rule 5).
  - A list of more than 20 items, such as countries: record it in full only where an absence rests on it. Otherwise record the items that bear on your question, such as Yemen or the places your records name, each with the list's own key or heading, and say in `notes.md` how many items the list holds.
- **Its scope** is the store and the date the run observed it: `store <the store as the run names it>, observed <date>`. Where an answer or a page of the same store states its country, plan or currency, add it in the platform's words, and cite that file too.
  - The run names its store in `answers.jsonl` (observed-sh) or `run.json`'s `extra.store` (observed-sa). Where it names none, or where an answer's own address or variables name another store, name the store as a saved answer or page of the same run states it (its handle, name or id), cite that file, and say so in `notes.md`. If none states it, write `store not named by the run`.
- **An observation shows what one store's pages showed, in what the run did, on that date.** Record it as that, never as what the platform does for every store or country.
  - A run that didn't show something shows nothing about it.
  - "Absent" still needs a complete list whose own words present it as the full set (rule 6).
- **The capture's own words are not the platform's.** The steps' `intent`, the titles the capture gave its runs, the run notes and the guides' descriptions are never a statement, identifier or scope.
- **Citing a run's file:**
  - `source` is `<repository>@<commit>:raw/runs/<run>/<file>`, with the full commit;
  - `locator` gives the operation, store and step for an answer; the method, address and step for a saved response; and the step for a step's file;
  - `quote` is verbatim from the file, at most 300 characters;
  - `source_date` is the date of the call or step (from `answers.jsonl`, `responses.jsonl` or `actions.jsonl`), and `date_basis` "observed in run <run>, step <n>";
  - `access_path` is `local`, and `from` is `held`.
- **Credentials** (rule 10): the runs' answers carry tokens and test data. Read and cite them like any other evidence.
- **Keep it short:** at most 60 new statements. A list's items, or a table's rows, count as one. Then stop reading, and list what you didn't read in `notes.md`.

## Output

- Your folder's files, as `R3-recording.md`'s "Output" gives them. New statements and citations continue the folder's ids, from the next number.
- **`not-found-closed.tsv`:** the rows you closed (step 3).
- **`notes.md`,** a new section at its end, `## Re-check against the observed runs, 19 October 2026`:
  - what you read: the guides, each search, each file;
  - each open item and what became of it: closed (by which statements), narrowed, or unchanged;
  - each wording change (step 4);
  - problems with this brief or the tools.

**Before you finish:** run `python3 -I method/check_proposals.py records <question> <platform>`, adding `--check` if your folder is a check, and fix what it reports. Then report in a few lines: items closed, narrowed and unchanged; new statements; and anything that got in your way.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/` or the observed repositories, and never change directory into them, even for `grep`, `wc` or `awk`. Read them only.
- Write working copies only in your scratch directory.
- Don't commit.
