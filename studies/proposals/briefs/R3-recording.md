# Brief: one question on one platform, in depth (steps R2 and R3)

**Status: draft. It is checked before it runs.**

You are one agent with one short task: one question, on one platform. The message that started you names both. Your folder is `studies/proposals/records/<question>/<platform>/`. It already holds `selection.tsv`. You run at `medium` effort.

**Your task:** record what your platform says and does that bears on your question, in its own words, and what you didn't find. Many of its statements are recorded already, and a script copies them for you. You record only what they don't show. Then you write a short account of what your platform shows for the question.

Don't answer the question in your own words, compare your platform with any other, or judge it.

## Read only

- this brief;
- your question, as `studies/proposals/questions.md` words it: its own section, and "How a run uses its question". Number the question's sentences from 1, across its paragraphs;
- the files in your folder;
- for Q5 only: your platform's folder from the pilot, `studies/subjects/S-01/<platform>/`. Read its `gaps.tsv`, `absences.tsv` and `absence-audit.tsv` for what the pilot didn't find;
- your platform's `studies/concern-map/platforms/<platform>/concerns.tsv`, only to add a concern (step 1);
- your platform's own material, held or live, as the table below gives it. For every platform this includes any agreement its terms incorporate, one its terms name as binding on the seller.

| Platform | Held | Live (declarations only) |
| --- | --- | --- |
| shopify | observed-sh at `c8b5fbee25966372a0475e6ed81f0b7760ac2921`: `structures/shopify/`, including the Help Center in `structures/shopify/help-center/help.shopify.com@en-ar/` (English as `md/en/`, Arabic as `content.html/ar/`), and committed text under `raw/runs/` | help.shopify.com, shopify.dev, shopify.com/legal |
| salla | observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`: `structures/salla/`, including `help-articles/{ar,en}/texts.jsonl`, `com-policies/` and `partners-legal/` | docs.salla.dev, salla.com, help.salla.sa |
| woocommerce | WooCommerce 11.2.1 release files in `/home/user/woocommerce-release/11.2.1/woocommerce`, cited as `woocommerce-11.2.1:<path>` relative to that folder | woocommerce.com docs and legal pages |
| zid | none | docs.zid.sa, zid.sa and Zid's help pages |
| bigcommerce | none | docs.bigcommerce.com, bigcommerce.com and its legal pages, support.bigcommerce.com where it can be read |

**Your platform's own map of its help.** Where your platform's held material includes how it organizes its own help, start there. It shows where the platform itself files each topic, in its own words:
- **Shopify:** in `structures/shopify/help-center/help.shopify.com@en-ar/`:
  - `outline.md` gives the Help Center's menus in their order and nesting, each page with its anchored sections, linked to its `.md`;
  - `pages.jsonl` gives each English page's address, title and place in the menus, and `ar/pages.jsonl` each Arabic page's.
- **Salla:**
  - `structures/salla/help-tree/{en,ar}/items.jsonl` gives the help centre's categories, with their breadcrumbs and subcategories;
  - `structures/salla/help-articles/{ar,en}/items.jsonl` gives the articles in them.

Find in the map the sections and pages where your platform files what your question asks about, and read those pages. Then use the corpus search for what they don't show, and always before you record anything as not found.

**Tools:**
- to search everything held for your platform, in every language, run `python3 -I method/corpus_search.py <platform> <terms>`;
- to find whether an address is held, run `python3 -I method/held_index.py <url>`;
- to read a record held in a fetch archive, run `python3 -I method/warc_text.py <repository root> <location> --text`;
- to read a held file at its commit, run `git --git-dir=<repository root>/.git show <commit>:<path>`, from outside the repository.

**Reading a live page.** Read a `.md` endpoint, the raw file, or the rendered page through `method/capture/page_text.mjs`. A summary returned by a fetching tool is not the page. Don't get around logins, paywalls or bot challenges.

**Don't open:**
- anything else under `studies/`, except your own folder and what this brief names;
- `PLAN.md`, `STATE.md`, `NEXT.md` and `questions/`;
- `register/`, `model/`, `yemen-setup-options/`, `shopify-payments-study/` and `evidence/yemen/`.

## Steps

1. **Choose what to copy.** `selection.tsv` lists the recorded concerns that may bear on your question, each with its terms, its description, and how many statements and gaps it holds.
   - Set each row's `action`:
     - `copy` if the concern bears on your question;
     - `set aside` if it doesn't, with the reason in `reason`.
   - Add a row with action `add`, and its reason, for any other concern of your platform that bears on the question. Take its id and terms from `concerns.tsv`.
   - The description is the concern map's words, not the platform's. Judge by the terms and, where you need to, by the concern's statements.
   - Then run `python3 -I method/copy_statements.py copy <question> <platform>`. It writes `copied.tsv`, `copied-gaps.tsv` and `copied-citations.tsv`, and for Q5 `copied-pilot.tsv`, with every row unchanged.
2. **Read the copies.** They are recorded already, so don't record them again. A copied gap is what an earlier run didn't find. You may close it by reading.
3. **Read for what the copies don't show,** in this order:
   1. what is held: first the pages your platform's own map of its help points to, then the corpus search;
   2. live pages, only where what is held doesn't show it.

   Record each new statement.
4. **Go deep where it bears on the question.** Record the platform's own structure: the things it names, and the levels its settings are set at, such as a store, a market, a plan or an account. Also record the contracts behind its providers, including agreements its terms incorporate.
5. **Record what you don't find,** in `not-found.tsv` (rules 6 and 7).
6. **Write the account** (Output).

## Rules

1. **A statement** is your platform's own words or data, or those of an agreement its terms incorporate, copied verbatim. It carries the platform's identifiers where it has them, such as a key, scope, route, plan name or section heading. Never use a category name of ours, and never the words of your question as a heading or label.
2. **`bears_on`:** the numbers of the question's sentences the statement answers, `;`-separated.
3. **Scope.** A statement holds where the platform says it holds: a store, plan, country, market or role. Record that scope as stated, and leave it empty when the statement is general.
4. **Release marker.** When the source marks a stage of release for what the statement describes, such as beta or sunset, copy that word into `marker`, verbatim.
5. **Lists.** Record a list in full, as one statement, such as the countries where something is offered.
   - Cite each item, or each run of items.
   - Cite the words that present the list as complete, if there are any.
   - A statement may run past 300 characters; only quotes are capped.
6. **Absent.** Absence counts only from a complete list your platform publishes, whose own words present it as the full set.
   - Record it in `not-found.tsv` with `kind` = `absent`.
   - Cite the list in `list_cite_ids`, and the words that make it complete in `complete_cite_ids`.
7. **Not in what was read.** Anything else your platform doesn't show is `not in what was read`.
   - `read` lists what you read looking for it: held paths with their commit, and live URLs with the date you read them. An index or a sitemap doesn't count as reading the pages it lists.
   - Before you record one, run `python3 -I method/corpus_search.py <platform> <terms>`:
     - with your platform's own words for what is missing, in every language it uses;
     - with each country, plan or arrangement your statements name.

     Read each listed document that could show it. Give the commands, and the documents you opened, in `searched`.
8. **Only by signing up.** When something shows only inside a seller's account, such as a dashboard page or a setting behind a login, record it as `not in what was read`, with `who_can` = `founder`. Its `route` says exactly what to capture: the page, and where it is.
   - Before you route anything to the founder, run `python3 -I method/held_index.py` on its address. If it is held and readable, read it instead.
   - These rows make the founder's capture list. Capturing is optional, and the work doesn't wait for it.
9. **Copies.** Don't record again what a copy already says.
   - If your reading shows a copy is out of date, record the new statement, and say in its `note` which copy it updates.
   - If a copy is wrong, say so in `notes.md`, with the source.
10. **Credentials.** Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip, withhold or mask a file because of them. They come from synthetic environments the founder rotates.
11. **No inference, anywhere.** Notes record what was read, what couldn't be read, and problems. They never record inference.
12. **Keep it short.** Stop and report once you pass 120 new statements.

## Quotes and citations

- **Quotes are verbatim,** at most 300 characters, with no ellipses, and within one paragraph of the source. Arabic stays as written. The checker collapses whitespace, removes HTML tags and decodes entities, on both sides.
- **A local source** is `<repository>@<commit>:<path>`, with the full commit from the table, or `woocommerce-11.2.1:<path>`. A record in a fetch archive is cited by its archive path, with the offset as the locator.
- **A live source** is the exact URL you fetched: the `.md` endpoint if that is what you read. The coordinator captures every cited live page after your run, and the checker looks for each quote in that capture.
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
| `not-found.tsv` | `nf_id` (`Q-XX-N01`…) · `bears_on` · `what_is_missing` · `kind` (`not in what was read` or `absent`) · `read` · `searched` · `list_cite_ids` · `complete_cite_ids` · `who_can` (`agent`, `founder` or `either`) · `route` |
| `account.md` | below |
| `notes.md` | what you read; what you couldn't read; copies you found wrong or out of date; problems with the method |

**`account.md`** is a short account of what your platform shows for the question, in its own terms.
- **Its sections:** one for each sentence of the question, headed by the sentence's number.
- **Each point** ends with the ids it rests on: copy ids (such as `Q2-SA-K0012` or `Q5-SA-P0003`), your `stmt_id`s, or your `nf_id`s. A point without an id doesn't belong in it.
- **It adds no claim of its own.** It compares with no other platform, ranks nothing, and recommends nothing.
- **Length:** at most about 1,500 words.

Write the files as you go: if you are interrupted, the next run continues from them.

**Before you finish:** run `python3 -I method/check_proposals.py records <question> <platform>`, and fix what it reports.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/` or the observed repositories.
- Don't commit.
