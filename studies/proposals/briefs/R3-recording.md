# Brief: one question on one platform, in depth (steps R2 and R3)

**Status: revised after its check (`studies/proposals/checks/R3-briefs-check.md`). It is re-checked before it runs.**

You are one agent with one short task: one question, on one platform. The message that started you names both, and a scratch directory. Your folder is `studies/proposals/records/<question>/<platform>/`. It already holds `selection.tsv`. You run at `medium` effort.

**Your task:** record what your platform says and does that bears on your question, in its own words, and what you didn't find. Many of its statements are recorded already: you choose which bear on the question, and a script copies them. You record only what they don't show. Then you write a short account of what your platform shows for the question.

Don't answer the question in your own words, compare your platform with any other, or judge it.

## Read only

- this brief;
- your question, in `studies/proposals/questions-for-agents.md`: its own section, and "How a run uses its question". Its sentences are numbered in square brackets. Use those numbers;
- the files in your folder;
- if you copy the pilot's row (S-01): the pilot's `studies/subjects/S-01/<platform>/absence-audit.tsv`, only for the absences you rely on (step 2);
- your platform's `studies/concern-map/platforms/<platform>/concerns.tsv`, only to add a concern (step 1);
- your platform's own material, held or live, as the table below gives it. For every platform this includes any agreement its terms incorporate, or name as binding on the seller.

| Platform | Held | Live (declarations only) |
| --- | --- | --- |
| shopify | observed-sh at `c8b5fbee25966372a0475e6ed81f0b7760ac2921`: `structures/shopify/`, including the Help Center in `structures/shopify/help-center/help.shopify.com@en-ar/`, and committed text under `raw/runs/`; and the pages in this repository's capture runs | help.shopify.com, shopify.dev, shopify.com/legal |
| salla | observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`: `structures/salla/`, including the help centre's articles in `help-articles/{ar,en}/`, `com-policies/` and `partners-legal/`; and the pages in this repository's capture runs | docs.salla.dev, salla.com, help.salla.sa |
| woocommerce | the WooCommerce 11.2.1 release files in `/home/user/woocommerce-release/11.2.1/woocommerce`, cited as `woocommerce-11.2.1:<path>` relative to that folder; and the pages in this repository's capture runs | woocommerce.com docs and legal pages |
| zid | the pages in this repository's capture runs | docs.zid.sa, zid.sa and Zid's help pages |
| bigcommerce | the pages in this repository's capture runs, and the founder's saves in `evidence/product-class/blocked-evidence-founder/bigcommerce/` | docs.bigcommerce.com, bigcommerce.com and its legal pages, support.bigcommerce.com where it can be read |

**The pages in this repository's capture runs** are found by the corpus search and by `held_index.py`. To read one, run `python3 -I method/held_index.py <url>`, then read the text file it names. Cite it by its URL: the checker finds it in the capture.

**Your platform's own map of its help.** Where your platform's help is held with its map, start there. The map shows where the platform itself files each topic, in its own words. Read it only through `method/help_map.py`. Never read a map file whole: `outline.md`, `pages.jsonl`, `items.jsonl` and `texts.jsonl` are too large.
- **Shopify:**
  - `python3 -I method/help_map.py shopify` lists the Help Center's menus, each with its line number;
  - `python3 -I method/help_map.py shopify <line>` lists the pages that menu files: level, title and path;
  - `python3 -I method/help_map.py shopify page <path>` prints one page, after the source to cite it by. English pages are `md/en/…`. A page's Arabic version is at the same path with `md/en/` changed to `content.html/ar/` and `.md` to `.html`. An Arabic page may show HTML entities, such as `&gt;` in a settings path: in an identifier, write the character it stands for (`>`).
- **Salla:**
  - `python3 -I method/help_map.py salla [ar|en]` lists the help centre's categories, in Arabic unless you give `en`: id, breadcrumb and subcategories;
  - `python3 -I method/help_map.py salla <category id>` lists the articles that category files, with their Arabic and English titles. The Arabic help centre is the fuller one: about a quarter of its articles have no English version;
  - `python3 -I method/help_map.py salla page <article id> [ar|en]` prints one article, in Arabic unless you give `en`, after the source and locator to cite it by.
- **WooCommerce, Zid and BigCommerce:** no map is held. Start from the corpus search.

**WooCommerce's release files** are code and built files, some of them megabytes long. Never read one whole: search it with `grep`, from outside the folder, and read the lines around what you find.

**BigCommerce's founder's saves** are mostly PDFs. Read one with `pdftotext -q "<file>" -`, in double quotes, since some names hold an apostrophe, and cite it as `sharrwah-knowledge-map@<commit>:<path>`: the checker reads it the same way.

**Tools:**
- to search everything held for your platform, in every language, run `python3 -I method/corpus_search.py <platform> <terms> [--max N] [--with <terms>]`. A document matches when it holds any of the terms, and, with `--with`, also any of the terms after `--with`. Its snippets are folded for matching: never quote one, quote the document;
- to find whether an address is held, run `python3 -I method/held_index.py <url>`;
- to read a record held in a fetch archive, run `python3 -I method/warc_text.py <repository root> <location> --text`;
- to read a held file at its commit, run `git --git-dir=<repository root>/.git show <commit>:<path>`, from outside the repository;
- to see the statements of a concern, run `python3 -I method/copy_statements.py show <platform> <concern id> [<concern id> ...]`.

**Reading a live page.** Read a `.md` endpoint, the raw file, or the rendered page through `method/capture/page_text.mjs`. Write any working copy in your scratch directory, never in the repository. A summary returned by a fetching tool is not the page. Don't get around logins, paywalls or bot challenges.

**Don't open:**
- anything else under `studies/`, except your own folder and what this brief names. This includes `studies/proposals/questions.md`;
- `PLAN.md`, `STATE.md`, `NEXT.md`, `questions/`, `founder-messages/` and `founder-decisions.tsv`;
- `register/`, `model/`, `yemen-setup-options/`, `shopify-payments-study/` and `evidence/yemen/`.

## Steps

1. **Choose what to copy.** `selection.tsv` lists the recorded concerns that may bear on your question, each with its terms, its description, and how many statements and gaps it holds.
   - Set every row's `action` before you copy:
     - `copy` if the concern bears on your question;
     - `set aside` if it doesn't, with the reason in `reason`.
   - Add a row with action `add`, and its reason, for any other concern of your platform that bears on the question. Take its id and terms from `concerns.tsv`.
   - Judge by the terms. Where they don't decide it, run `copy_statements.py show` for that concern, and judge by its statements. The description is the concern map's words, not the platform's.
   - The last row, `S-01`, is the pilot's statements, gaps and absences on who holds a seller's money. For Q5 it is set to `copy` already. For other questions, judge it like the others: `show` prints its identifiers.
   - For a concern with no statements, `show` prints its gaps instead. Their wording is the concern map's: judge by what they say is missing.
   - Then run `python3 -I method/copy_statements.py copy <question> <platform>`. It copies every row unchanged:
     - `copied.tsv`, the statements, with ids such as `Q2-SA-K1553`;
     - `copied-gaps.tsv`, the gaps: what an earlier run didn't find, with ids such as `Q2-SA-G0007`;
     - `copied-citations.tsv`, their citations;
     - if S-01 is copied, the pilot's statements (`copied-pilot.tsv`, P ids), gaps (`copied-pilot-gaps.tsv`, H ids) and absences (`copied-pilot-absences.tsv`, A ids);
     - two views of the statements: `copied-index.tsv` and `copied-view.tsv`.

     A copy's id is its line in its source. If you add a concern later, add its row and copy again: the ids already copied don't change.
2. **Read the copies through their views.** They are recorded already, so don't record them again. Never read `copied.tsv`, `copied-gaps.tsv` or `copied-citations.tsv` whole.
   1. Read `copied-index.tsv` whole: each copy's id, concern and identifier.
   2. Before you record a statement, search `copied-view.tsv` with `grep` for a distinctive phrase of it. If a copy already says it, don't record it.
   3. Read the copied gaps only of the concerns that bear on a sentence of your question, with `grep` for the concern's id in `copied-gaps.tsv`. If S-01 is copied, search `copied-pilot-gaps.tsv` with `grep` for the terms of the sentence you are reading for.
   4. When you write the account, read `copied-view.tsv` once.
   5. Open `copied-citations.tsv` only for a `cite_id`, with `grep`.
   6. If S-01 is copied, read `copied-pilot-absences.tsv`. Read the pilot's `absence-audit.tsv` only for the absences you rely on.
3. **Read for what the copies don't show,** one sentence of your question at a time, in this order:
   1. your platform's map of its help, if it has one: at most 10 pages, chosen by their titles;
   2. one corpus search in your platform's own words, in each language it uses, as alternatives in one call, with `--max 10`. Read at most 5 of the documents it lists, or 10 if your platform has no map;
   3. live pages, only where what is held doesn't show it: at most 5.

   Stop reading for a sentence sooner once 5 pages in a row add nothing new. A sentence that only gives examples, limits or restates the question has no reading of its own: it shares the reading of the sentence it serves. Read each page in one of its languages, and open the other only to quote it. Record each new statement.
4. **Go deep only where a sentence concerns money flows, legal structure, the data model or partner contracts.** For those sentences, and within at most 5 more pages each:
   - record the platform's own structure: the things it names, and the levels its settings are set at, each named as the platform names it;
   - record the contracts behind its providers as your platform's material shows them: what it says of them, and any agreement its terms incorporate or name as binding on the seller, which you may read. Don't read a provider's own terms otherwise. Where your platform names such terms, record them as not in what was read, with their address.
5. **Record what you don't find,** in `not-found.tsv` (rules 6 and 7). A copied gap that is still open and bears on a sentence is cited by its G id, or the pilot's H id. Record a not-found only for what no copied gap covers.
6. **Write the account** (Output).

## Rules

1. **A statement** is your platform's own words or data, or those of an agreement its terms incorporate, copied verbatim. It carries the platform's identifiers where it has them, such as a key, an access scope, a route, a plan name or a section heading.
   - Never use a category name of ours, and never the words of your question, as a heading or label.
   - The concern map's descriptions, the copies' `placement` and `structure` values, and the copied gaps' wording are ours, not the platform's. Never use them in a statement, identifier, scope, note or the account.
2. **`bears_on`:** the numbers of the question's sentences the statement answers, `;`-separated.
3. **Scope.** A statement holds where the platform says it holds. Record that scope in the source's words, and leave it empty when the statement is general.
4. **Release marker.** When the source marks a stage of release for what the statement describes, such as beta or sunset, copy that word into `marker`, verbatim.
5. **Lists.** Record a list in full, as one statement, such as the countries where something is offered.
   - The statement is the source's text from the list's first item to its last, on one line, keeping the source's own markers, such as `- `.
   - Where the items aren't consecutive in the source, or the list is a table, record each run of consecutive items, or each row, as its own statement, so that each is verbatim in its source.
   - Cite each item, or each run of items. A quote may run over consecutive items of one list.
   - Cite the words that present the list as complete, if there are any.
   - A statement may run past 300 characters; only quotes are capped.
6. **Absent.** Absence counts only from a complete list your platform publishes, whose own words present it as the full set.
   - Record it in `not-found.tsv` with `kind` = `absent`.
   - Cite the list in `list_cite_ids`, and the words that make it complete in `complete_cite_ids`.
7. **Not in what was read.** Anything else your platform doesn't show is `not in what was read`.
   - `read` lists what you read looking for it: held paths with their commit, and live URLs with the date you read them. An index or a sitemap doesn't count as reading the pages it lists.
   - Before you record one, search:
     - run one corpus search with your platform's own words for what is missing, in each language it uses, as alternatives in one call, with `--max 10`;
     - if the row is about a place, plan or arrangement your statements name, run one more with `--with` and their names;
     - read at most the 5 listed documents whose title or snippet could show it, and list the others as not read.

     Give the commands, and the documents you opened, in `searched`.
8. **Only by signing up.** When something shows only inside a seller's account, such as a dashboard page or a setting behind a login, record it as `not in what was read`, with `who_can` = `founder`. Its `route` says exactly what to capture: the page, and where it is.
   - Before you route anything to the founder, run `python3 -I method/held_index.py` on its address:
     - if it is held and readable, read it instead;
     - if it is held but not readable, don't route it to the founder. Record `who_can` = `agent`, with `route` "held, not readable: <location>", and say so in `notes.md`.
   - These rows make the founder's capture list. Capturing is optional, and the work doesn't wait for it.
9. **Copies.** Don't record again what a copy already says.
   - If your reading shows a copy is out of date, record the new statement, and say in its `note` which copy it updates.
   - If a copy is wrong, say so in `notes.md`, with the source.
   - Close a copied gap only where it bears on a sentence of your question, from pages you read for that sentence. The statement that closes it names the gap's id in its `note`. Don't read for a gap otherwise.
10. **Credentials.** Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip, withhold or mask a file because of them. They come from synthetic environments the founder rotates.
11. **No inference, anywhere.** Notes record what was read, what couldn't be read, and problems. They never record inference.
12. **Keep it short.** Once you pass 120 new statements, stop reading. Write the account from what is recorded, list in `notes.md` what you didn't read, run the checker, and report.

## Quotes and citations

- **Quotes are verbatim,** at most 300 characters, with no ellipses, and within one paragraph of the source. Arabic stays as written. The checker collapses whitespace, removes HTML tags and decodes entities, on both sides.
- **A local source** is `<repository>@<commit>:<path>`, with the full commit from the table, or `woocommerce-11.2.1:<path>`.
  - A Help Center page or a help article is cited by the source, and for an article the locator, that `help_map.py` prints.
  - A record in a fetch archive is cited by its archive path, with the offset as the locator. A page that `held_index.py` shows held only in a fetch archive is cited this way, not by its URL.
- **A captured page** is cited by its URL, with `from` = `held`.
- **A live source** is the exact URL you fetched: the `.md` endpoint if that is what you read. The coordinator captures every cited live page after your run, and before any proposal cites it. Until then the checker reports its quotes as "pending capture".
- **`locator`** is the heading, anchor or line.
- **`source_date`** is the date the source shows: published, updated or effective. For an undated live page, it is the date you read it. `date_basis` says which.
- **`accessed`** is the date you read it.

## Output, in your folder

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. `Q` is your question's id, such as `Q2`, and `XX` your platform's code: SH, SA, WC, ZD or BC.

| File | Columns |
| --- | --- |
| `selection.tsv` | as the script wrote it, with `action` and `reason` set by you (step 1) |
| `statements.tsv` | `stmt_id` (`Q-XX-001`…) · `bears_on` · `identifier` · `statement` · `scope` · `marker` · `cite_ids` · `from` (`held` or `live`) · `note` |
| `citations.tsv` | `cite_id` (`Q-XX-C001`…) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `accessed` · `access_path` (`md`, `raw`, `rendered` or `local`) |
| `not-found.tsv` | `nf_id` (`Q-XX-N01`…, three digits past 99) · `bears_on` · `what_is_missing` · `kind` (`not in what was read` or `absent`) · `read` · `searched` · `list_cite_ids` · `complete_cite_ids` · `who_can` (`agent`, `founder` or `either`) · `route` |
| `account.md` | below |
| `notes.md` | what you read; each live URL you read, with the language it was served in; what you couldn't read; copies you found wrong or out of date; problems with the method |

**`account.md`** is a short account of what your platform shows for the question, in its own terms.
- **Its sections:** one for each sentence your points answer, in order, headed by the sentence's number, as `## [2]`. A point that answers several sentences goes under the first.
- **Each point,** a list item or a paragraph, ends with the ids it rests on:
  - copy ids, such as `Q2-SA-K1553`, and the pilot's, such as `Q5-SA-P0003`;
  - copied gap ids, such as `Q2-SA-G0007`, and the pilot's H and A ids;
  - your `stmt_id`s and `nf_id`s.

  A point without an id doesn't belong in it. Don't nest lists: each list item is a point, and carries its own ids.
- **It adds no claim of its own.** It compares with no other platform, ranks nothing, and recommends nothing.
- **Length:** at most about 1,500 words.

Write the files as you go: if you are interrupted, the next run continues from them.

**Before you finish:** run `python3 -I method/check_proposals.py records <question> <platform>`, and fix what it reports. If it reports a copy as changed, don't edit the copy: say so in `notes.md`.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/`, the observed repositories or the WooCommerce release folder. Read them only.
- Write working copies only in your scratch directory.
- Don't commit.
