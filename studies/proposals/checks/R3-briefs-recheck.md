# Re-check of the R3 briefs after their fixes

**18 October 2026.** A re-check of `studies/proposals/briefs/R3-recording.md`, `studies/proposals/briefs/R3-checking.md`, the tools they name, and the PLAN.md entry for their fixes. It follows the check in `studies/proposals/checks/R3-briefs-check.md`. Nothing here was run as a task.

**What was checked.** The repository at 20600b6:
- the tools as changed in e66cee8;
- the briefs and PLAN.md as changed in d8c2410;
- 2731962, which came while this re-check ran. It changed the recording brief and `copy_statements.py` so that the pilot's row, S-01, is offered to every question, and it made **Q3 on Salla** the sample (PLAN.md section 11, last entry). The verdict covers Q3 on Salla, and Q2 on Salla as the coordinator asked.

**What was run,** in the scratch directory only, with `python3 -I -B` so that no bytecode was written into `method/`:
- `copy_statements.py`:
  - `candidates` for Q3 on Salla and Q2 on Salla;
  - `show`;
  - `copy`, with every candidate copied, for all 40 question and platform pairs;
  - for Q5, every concern of each platform copied.
- `check_proposals.py`:
  - on all those copies;
  - on tampered copies;
  - on hand-made records for Q2 and Q3 on Salla, with and without `--check`.
- `corpus_search.py` on Salla, Shopify and WooCommerce, with and without `--with` and `--max`.
- `help_map.py`:
  - Shopify's menus, one menu, and one page in English and in Arabic;
  - Salla's categories in both languages, one category, and one article in both languages.
- `quote_check.py` on quotes taken from `help_map.py` output and from a founder's PDF save.

## What the sample starts from now

**Q3 on Salla.** The selection has 71 candidate concerns, holding 875 statements and 123 gaps, plus the S-01 row (202 pilot statements and 7 gaps). The file is 18 KB, small enough to judge by its terms.

With every row copied:

| File | Size | About | When the brief has it read |
| --- | --- | --- | --- |
| `copied-index.tsv` | 60 KB | 14k tokens | whole |
| `copied-view.tsv` | 286 KB | 66k tokens | once, for the account |
| copies, gaps, citations and the pilot's copies | 1.2 MB | | never whole |

A hand-made Q3 record passed the checker with "no issues". It had:
- a statement and quote from the Arabic article that `help_map.py` printed, cited by the source and locator it printed;
- a not-found row;
- an account citing a pilot id (P).

## The 32 findings of the first check

| # | Finding | Status | Evidence |
| --- | --- | --- | --- |
| 1 | The founder's items through `questions.md` | Fixed | Recording brief, line 14: the question comes from `questions-for-agents.md`. Line 51 forbids `questions.md`; line 52 forbids `founder-messages/` and `founder-decisions.tsv`. The sentences are numbered in brackets, and for Q1 to Q8 the file's numbers and texts equal the checker's (`agent_questions.sentences`). |
| 2 | "Market" in the example levels and scopes | Fixed | Step 4 (line 86) and rule 3 (line 97) give no examples. A search of both briefs finds no "market". |
| 3 | The concern map's own words | Fixed | Rule 1 (line 95). |
| 4 | One account section per sentence | Fixed, as the coordinator chose | Line 154: a section only for a sentence the points answer, each point under the first sentence it answers. The checker requires `## [n]` within the question's sentences (tested). The reading budget is still per sentence: new finding 9. |
| 5 | Judging a concern by statements it can't see | Fixed | `copy_statements.py show` (lines 133 to 144, tested) and brief line 62. The S-01 row, added since, can't be shown: new finding 3. |
| 6 | Copied gaps had no ids | Fixed | G, H and A ids. The checker accepts `[KPGHA]` (`check_proposals.py`, line 304); an account citing Q2-SA-G0007 passed. Brief lines 88 and 157. |
| 7 | The checker rejected unchanged copies | Fixed | Raw lines compared (`check_proposals.py`, lines 146 to 150). Every candidate of all 40 pairs, and every concern of each platform for Q5, copied with no copy error, Salla's line 1553 included. The tampering tests below were all caught. |
| 8 | Copy ids shifted | Fixed | Ids are source lines. Q7-SH-K1333 stayed line 1333 after a concern was set aside and the copy run again, and an account citing a copy that had been set aside was reported. |
| 9 | "Held: none" for Zid and BigCommerce | Fixed | Table, lines 22 to 26, and line 28. `held_index.py` named a captured Zid page's text file. The founder's PDF saves can't be quoted: new finding 6. |
| 10 | WooCommerce's release not searched | Fixed | `corpus_search.py`, lines 211 to 219: a COD search found 21 release files. New findings 4 and 5. |
| 11 | Contracts beyond the reading list | Fixed | Step 4 (line 87), and the PLAN.md entry records the narrowing. |
| 12 | Rule 12 stopped a run before its account | Fixed | Line 126. |
| 13 | Lists and the checker | Fixed | Rule 5 (lines 100 and 101). |
| 14 | Corpus-search snippets quoted | Fixed | Line 42, and `corpus_search.py`'s docstring. |
| 15 | The checker accepted what the brief forbids | Partly fixed (optional) | Now checked, and tested: account points and sections, deleted candidate rows, and `bears_on` within the sentences. Not checked: a `read` naming only an index or sitemap; `scope` and `marker` against the quote. |
| 16 | Capture timing and language | Fixed | PLAN.md section 11; brief lines 48, 135 and 151. The entry names section 6 only: new finding 10. |
| 17 | Held but not readable | Fixed | Rule 8 (line 118). |
| 18 | "Scope" with two meanings | Fixed | Rule 1 (line 93): "an access scope". |
| 19 | Reading the copies whole | Fixed | Step 2 (lines 72 to 78) reads the views. For the sample: 14k tokens whole and 66k once, against 1.2 MB of copied files. |
| 20 | The help maps too large to read | Fixed | `help_map.py`: the Shopify menus are 3 KB, the Payments menu 31 KB, Salla's categories 9 KB, and each page prints with its source. New findings 2 and 8. |
| 21 | Nothing bounded the reading | Fixed | Steps 3 and 4 (lines 79 to 87), and PLAN.md section 11. The bound is per sentence: new finding 9. |
| 22 | Closing copied gaps without a bound | Fixed | Step 2, item 3 (line 75), and rule 9 (line 123). |
| 23 | Searches behind a not-found without a limit | Fixed | Rule 7 (lines 107 to 114). With `--with`, a test search matched 21 documents instead of 503. Step 3's own search has no limit: new finding 1. |
| 24 | Q5's reading of the pilot's gaps | Fixed | Lines 16, 75 and 78. The pilot's gaps are copied, and grepped rather than read whole. |
| 25 | Comparing both forbidden and required | Fixed | Checking brief, item 1 (lines 12 and 13). |
| 26 | No rule for when two things match | Fixed | Items 3 and 4 (lines 19 to 32), and item 2 (line 18). There is a wording problem: new finding 11. |
| 27 | Reading couldn't find what "goes beyond" | Fixed | Item 6 (lines 34 to 38). Its searches for each account point have no cap: new finding 7. |
| 28 | "Go deep" and the in-depth not-found rules inherited | Fixed | Items 7 and 8. |
| 29 | The account's labels couldn't all be written | Fixed | Items 4, 9 and 10. |
| 30 | Opening the in-depth records without a limit | Fixed | Item 2 (line 16). |
| 31 | The checker couldn't tell a checking run | Fixed | `--check` (`check_proposals.py`, lines 316 to 320, tested). |
| 32 | No rule for a missing account | Fixed | Item 2 (line 15). A WooCommerce folder for Q2, Q5 or Q8 fails the checker today, which would stop every checking run against it: new finding 4. |

**Tampering tests.** The checker caught each of these, in a scratch copy of the Q2 on Salla folder or the Q5 on Salla folder:
- one character changed in a statement;
- a copy id changed;
- a copied row deleted;
- the no-break space stripped from Q2-SA-K1553;
- a gap row changed;
- a citation changed, and one deleted;
- a candidate row deleted from the selection;
- S-01 set aside with the pilot's copies left in place;
- a pilot statement and a pilot absence changed.

## New findings

### Before the sample runs

**1. The reading search in step 3 has no `--max`.**
- **Where:** recording brief, step 3, item 2 (line 81); checking brief, item 6 (lines 36 and 37). Only rule 7 (line 110) sets `--max 10`.
- **Problem:** without it, a search lists up to 40 documents for each corpus. The run makes one search for each sentence, and its output stays in context for the rest of the run.
- **Evidence:** a Salla search for licensing terms ("ترخيص" "رخصة" "license" "licence" "licensed"):
  - without `--max`, it printed 82 KB, listing 123 documents;
  - with `--max 10`, 29 KB and 46 documents.

  Q3 has four sentences: about 330 KB against 120 KB.
- **Fix:** add "with `--max 10`" to step 3's search, and to both searches in the checking brief's item 6.
- **Severity:** must fix.

**2. Salla's map is listed in English by default, and the English help centre lacks a quarter of the articles.**
- **Where:** recording brief, lines 36 to 38; `help_map.py`, line 100, where the default language is `en`.
- **Problem:** the Arabic help centre holds 1,658 articles and the English 1,280; 412 have no English version. A category listed in English leaves out its Arabic-only articles, and the brief doesn't say which language to list. As written, the listing can't give "the articles that category files".
- **Evidence:**

  | Category | English | Arabic |
  | --- | --- | --- |
  | Store verification tips (`asqsa2licbq3qbaigkvepipo`) | 9 | 34 |
  | First-time store setup | 4 | 14 |
  | The older payments category | 10 | 22 |

  The Arabic-only articles in the first include "متطلبات توثيق المتجر في سلة وأسباب رفض الطلب" and "أسباب رفض توثيق المتجر في سلة وطريقة حل كل حالة": the sample's central topic.
- **Fix:** have `help_map.py salla <category>` list both languages, merged by article id, or default to Arabic. Say in the brief that Salla's Arabic help centre is the fuller one.
- **Severity:** must fix.

**3. Some selection rows can't be judged as the brief says.**
- **Where:** recording brief, step 1 (lines 62 and 63); `copy_statements.py show` (lines 133 to 144).
- **Problem:** two kinds of row are left to the concern map's description, which the brief says is ours.
  - **S-01:** it is now a candidate for every question but Q5, to be judged "like the others". It has no terms, and `show` refuses it.
  - **A concern with no statements:** `show` prints only its header. In the sample this is SA-C-233, which has no terms either.
- **Evidence:**
  - `copy_statements.py show salla S-01` prints "not concerns of salla: S-01" and exits 1;
  - `show salla SA-C-233` prints the header only.
- **Fix:** let `show` take S-01, printing the pilot's identifiers and statements, and print a concern's gaps when it has no statements. Or say: "Copy S-01, and any concern with neither terms nor statements."
- **Severity:** must fix.

### Before the runs they affect

**4. Some WooCommerce citations aren't copied, and the checker reports them missing.**
- **Where:** `copy_statements.py`: `split()` (line 71, used at line 184) splits cite ids on ";" only. `check_proposals.py`: `ids()` (line 82, used at line 157) also splits on spaces.
- **Evidence:**
  - 18 WooCommerce statements separate their cite ids with spaces, such as `statements.tsv` line 1399, "WC-S-5471 WC-S-5472". They sit under WC-C-103 to WC-C-112.
  - With every candidate copied, the checker reported "citations the copies cite are missing, such as WC-S-5471" for Q2 (3 missing), Q5 (22) and Q8 (27) on WooCommerce.
  - A run can't fix this: the brief covers only a copy reported as changed.
  - The checking brief's item 2 stops every checking run whose in-depth folder fails the checker.
- **Fix:** split cite ids in `copy_statements.py` as the checker does: `re.split(r"[,\s;]+", …)`.
- **Severity:** must fix, before WooCommerce runs on Q2, Q5 or Q8, and any checking run against them.

**5. The WooCommerce release search lists built bundles and a 2.3 MB `.pot` before the code.**
- **Where:** `corpus_search.py`, lines 211 to 219, which list files in path order; rule 7's `--max 10`, and "read at most the 5 listed documents".
- **Problem:** path order puts `assets/` (1,032 files, mostly built bundles) before `includes/` and `src/`. The code the search exists to reach falls past the cap, while the documents listed first are the most costly to read.
- **Evidence:** `corpus_search.py woocommerce WC_Gateway_COD "Cash on delivery" --max 10` listed 10 of 21 release files:
  - five bundles from `assets/`, among them `settings-embed.js` (268 KB) and `homescreen.js` (90 KB);
  - `i18n/languages/woocommerce.pot` (2.3 MB);
  - four PHP files.

  `includes/gateways/cod/class-wc-gateway-cod.php` came 11th.
- **Fix:**
  - Leave built bundles out of the search, or list `includes/`, `src/` and `templates/` first.
  - Search the `.pot` one entry at a time, each with its line.
  - Say in the brief: "Never read a release file whole: grep it."
- **Severity:** must fix, before WooCommerce runs.

**6. Quotes from the founder's PDF saves can't pass the checker.**
- **Where:** recording brief, table line 26, which lists the founder's saves as held for BigCommerce; `quote_check.py`, `local_texts` (lines 87 to 110), which reads a local file as text and extracts no PDF.
- **Evidence:**
  - 21 of the 23 saves are PDFs.
  - pdftotext gives this sentence from "Commerce Data Protection & Transfer Impact Summary (9.16.2025).pdf": "Commerce maintains substantial infrastructure and platform data security safeguards." The quote checker reported it "not found", both at a commit and in the working tree.
  - The corpus search reads these PDFs through pdftotext, so a run finds them and then can't cite them.
- **Fix:** have `quote_check.py` extract a local `.pdf` with pdftotext, as the corpus search does. Say in the brief how to read and cite a save: pdftotext, and `sharrwah-knowledge-map@<commit>:<path>`.
- **Severity:** must fix, before BigCommerce runs.

**7. A checking run's work grows with the accounts' points, with no cap.**
- **Where:** checking brief, item 6 (line 37): one search and up to 3 documents "for each account point not yet matched"; item 8 (line 40): one not-found row for each point not shown. These follow my own proposed fixes to findings 27 to 29.
- **Problem:** a checking run may sort against two or three accounts of up to 1,500 words each, with dozens of points between them.
  - Each point not matched costs a search, up to three documents and a not-found row.
  - `nf_id` allows only N01 to N99 (`check_proposals.py`, lines 233 and 304).
  - The PLAN.md entry says "A checking run reads less" (line 589); the brief doesn't make sure of it.
- **Fix:**
  - Run one search for each sentence, with the unmatched points' terms as alternatives and `--max 10`, and read at most 5 documents.
  - Record at most 20 not-found rows, first for points on money flows, legal structure, the data model or partner contracts. List the rest in `notes.md` as not checked.
  - Allow three digits in `nf_id`.
- **Severity:** must fix, before the first checking run.

### Optional

**8. `help_map.py` prints Arabic Shopify pages differently from the checker.**
- **Where:** `help_map.py`, lines 38 to 42; `quote_check.html_text`.
- **Problem:**
  - **Line breaks:** `help_map.py` breaks lines only at `br`, `/p`, `/li`, `/h`, `/tr` and `/div`. The checker also breaks at `td`, `th`, `ul`, `aside`, `blockquote` and other block tags. Where table cells sit side by side, `help_map.py` runs them together, and a quote copied from its output fails.
  - **Arabic paths:** the brief doesn't say how to find an Arabic page. 2,670 of the 2,674 English pages map by swapping `md/en/` for `content.html/ar/` and `.md` for `.html`.
- **Evidence:** in `content.html/ar/manual/international/pricing/dynamic-tax-inclusive-pricing.html`, a list of countries, `help_map.py` prints "ألبانياغرينلاندالفلبين", which is "not found". The checker finds "ألبانيا غرينلاند الفلبين". 30 Arabic pages hold such cells: 5,048 in all.
- **Fix:** use `quote_check.html_text` in `help_map.py`. State the path mapping, or print it in the menu listing.
- **Severity:** optional.

**9. The reading budget is per sentence, including sentences that ask nothing.**
- **Where:** recording brief, steps 3 and 4 (lines 79 to 87); the PLAN.md entry.
- **Problem:** each sentence gets up to 10 map pages, 5 search documents and 5 live pages, and 5 more for depth. Some sentences only limit or restate:
  - Q3's [3]: "Record any such requirement … but not the permissions of the seller's staff or of apps";
  - Q5's [2];
  - Q8's [2].

  For the sample, Q3's four sentences allow up to 80 pages before depth. The stop after five pages in a row with nothing new limits this in practice.
- **Fix:** read for the sentences that ask something. A sentence that only gives examples, limits or restates shares the budget of the sentence it serves.
- **Severity:** optional.

**10. The PLAN.md entry changes the capture rule in section 6 only.**
- **Where:** PLAN.md section 11, the entry for the R3 fixes (line 593). The same rule stands in section 2 (line 44), section 3 (line 96) and section 9 (line 419).
- **Fix:** say that the change holds for R3's runs wherever the plan states the rule.
- **Severity:** optional.

**11. "Never use an in-depth platform's terms" is unclear when both platforms use the term.**
- **Where:** checking brief, item 2 (line 18), and item 3's first basis (line 20).
- **Problem:** the first basis is "the same term". When the checked platform uses the same word, the rule could keep the run from recording its own platform's word: Salla's "Markets / الأسواق المتعددة" beside Shopify's "Markets" is one case.
- **Fix:** "Use only your own platform's words. Never take a word from an account that your source doesn't use."
- **Severity:** optional.

## Verdict

**The first check's findings:** of the 32, 31 are fixed and one is partly fixed (15, optional).

**New findings:** 11, of which 7 are must fix and 4 optional.

**The recording brief can't run the sample yet.** Q3 on Salla, and equally Q2 on Salla, needs new findings 1, 2 and 3 fixed first:
- `--max 10` in step 3's search;
- Salla's categories listed in Arabic, or in both languages;
- a way to judge S-01, and the concerns with no statements.

Each is a line in the brief or a few lines in a tool. Nothing else stands in the sample's way: on Salla, the copies, the checker, the help map, the corpus search and a hand-made record all ran clean.

**Before the runs they affect:**
- **WooCommerce:** findings 4 and 5;
- **BigCommerce:** finding 6;
- **checking runs:** finding 7.

The checking brief otherwise has its first check's fixes. It should be read once more with finding 7's fix, before the first checking run.
