# Verification of the fixes for the R3 briefs' re-check

This checks the fixes for the 11 new findings of `studies/proposals/checks/R3-briefs-recheck.md`: commit `5fd5079` against `20600b6`, on branch `claude/vibrant-meitner-oh70v4`.
- **How:** each fix was tested the way its finding's evidence was gathered, on observed-sh at `c8b5fbe`, observed-sa at `4ca2e89` and the WooCommerce 11.2.1 release files.
- **Where:** every output went to a scratch folder outside the repository.
- **Old tools:** the pre-fix tools were run from scratch copies of `20600b6`, to show that each test catches its problem.

**Result:**
- All 11 findings are fixed.
- The fixes bring 4 new problems, all optional.
- The recording brief can run the sample, Q3 on Salla.

## The findings

### 1. `--max 10` on the reading searches: fixed
- **Fix:** the recording brief's step 3 (line 86) and the checking brief's item 6 (lines 36 and 37) now say "with `--max 10`", as rule 7 does (line 115). No other search in either brief lacks it.
- **Test:** the finding's Salla search for licensing terms, run with `--max 10`, printed 29 KB and 46 documents. These are the finding's figures, so the changes to `corpus_search.py` leave Salla's search as it was.

### 2. Salla's map in both languages: fixed
- **Fix:**
  - `help_map.py salla <category>` lists both languages, merged by article id.
  - `salla page` prints Arabic unless given `en`.
  - The brief says the Arabic help centre is the fuller one (line 37).
- **Test:**
  - **The sample's category:** `help_map.py salla asqsa2licbq3qbaigkvepipo` lists 34 articles, each with its Arabic title, 9 with an English title too.
    - The list includes both central articles: "متطلبات توثيق المتجر في سلة وأسباب رفض الطلب" and "أسباب رفض توثيق المتجر في سلة وطريقة حل كل حالة".
    - The finding's other two categories list 14 articles (4 in English) and 22 (10 in English). These are the counts in its table.
  - **The merge:** 1,246 article ids are in both languages, 412 only in Arabic and 34 only in English. Every id listed has its text, so `salla page <id>` finds it.
  - **`salla page`:**
    - `salla page evrib312myg7282hjg7nlrje` prints the Arabic article. With `en`, it reports no English article, since the article has no English version.
    - `salla page v6ymzcrb4i7euybyuta4cfad` prints the article in each language.
  - **The checker:** all 114 lines printed of the first article pass the quote checker, against the source the tool prints.
- **Left as it was:**
  - The category list still defaults to English. Both trees hold the same 47 categories, so none is lost.
  - Its subcategory counts are English counts, though: 9 for the sample's category, against 34 in Arabic.
  - An English-only article needs `en`. Without it, the tool reports no article in the Arabic file.

### 3. Rows with no terms or no statements: fixed
- **Fix:**
  - `copy_statements.py show` takes S-01. It prints the pilot's statements, each cut to 160 characters.
  - For a concern with no statements, `show` prints its gaps, marked as the concern map's words.
  - The brief says so (lines 67 and 68).
- **Test:**
  - **S-01:** `show salla S-01` prints 202 rows and exits 0. No character is cut in two.
  - **SA-C-233:** `show salla SA-C-233` prints its 5 gaps, `gaps.tsv` lines 218 to 222. Each is marked "(no statements; a gap, in the concern map's words)".
  - **All platforms:** both work on all five platforms.
  - **Every row:** across every question's candidates on every platform, SA-C-233 is the only concern with no statements, and it has gaps. So `show` now prints something for every row a run judges.
  - **The sample:** Q3 on Salla has six rows with no terms: SA-C-114, -164, -231, -233, -235 and S-01. All can now be judged.
- **New:** S-01's output is large (new problem 3).

### 4. WooCommerce cite ids separated by spaces: fixed
- **Fix:** `copy` splits cite ids on commas, spaces and ";", as the checker does.
- **Test:**
  - **WooCommerce:** for each of Q2, Q5 and Q8, `candidates` ran, then `copy` with every row set to copy, then `check_proposals.py records <question> woocommerce --dir <folder>`.
    - Each time, the only error was the missing `account.md`, as for any folder not yet recorded.
    - No citation is missing.
  - **The old script:** on Q5, the pre-fix script gives "22 citations the copies cite are missing, such as WC-S-5471", as the finding found.
    - The fix adds exactly those 22 rows to `copied-citations.tsv`.
    - Every other file it writes is the same, byte for byte.
  - **All platforms:** on all five, every cite id in the concern map's and the pilot's rows is now in that platform's citations.
    - Under the old split, 18 entries didn't resolve, all in WooCommerce's statements.
    - So no question, on any platform, can miss a citation this way.
  - **The sample:** Q3 on Salla, with every row copied, gets only the missing `account.md` from the checker.

### 5. The WooCommerce release search: fixed
- **Fix:**
  - The platform's code (`includes/`, `src/` and `templates/`) is listed first.
  - Built bundles and bundled libraries (`assets/`, `packages/`, `vendor/` and `lib/`) are listed last.
  - The `.pot` is searched one entry at a time, each with its line.
  - The brief says never to read a release file whole (line 41).
- **Test:** `corpus_search.py woocommerce WC_Gateway_COD "Cash on delivery" --max 10`:
  - **Now:** it lists 10 PHP files from `includes/` and `src/`, in 4.4 KB. `includes/gateways/cod/class-wc-gateway-cod.php` comes 5th.
  - **Before the fix:** it listed 5 bundles, the whole `.pot` and 4 PHP files, without the cod gateway, as the finding found.
  - **With `--max 40`:** 15 code files, then 12 `.pot` entries, each with its line, then the 5 bundles. Line 13324 starts the entry that names the cod gateway's file.
- **`packages/`:** it holds Action Scheduler, Blueprint, the email editor and a one-file `woocommerce-admin`, and now goes last with the bundles. It sorted after `assets/` before the fix too, so nothing moved back.

### 6. Quotes from the founder's PDF saves: fixed, with a new problem in the brief's command
- **Fix:**
  - `quote_check.py` reads a `.pdf` through pdftotext, at a commit or in the working tree.
  - The brief says how to read and cite a save (line 43).
- **Test:**
  - **The finding's sentence:** "Commerce maintains substantial infrastructure and platform data security safeguards.", from "Commerce Data Protection & Transfer Impact Summary (9.16.2025).pdf".
    - It is found at `5fd5079`, at `7f7fdb3` (the commit that added the saves) and with no commit.
    - The pre-fix checker doesn't find it, with a commit or without.
  - **All 21 PDFs:** each gives the same text read from the file, as the brief reads it, and read from git through stdin, as the checker reads it.
    - Of their 5,982 non-blank lines, 5,976 pass.
    - The other 6 hold only a zero-width space.
  - **A hand-made record:** a BigCommerce record cites the PDF at a commit, and without one. It passes the whole checker: its quotes, its statements (which are checked verbatim too) and their source kind.
- **New:** the brief's command fails on every PDF (new problem 1).

### 7. A checking run's work: fixed
- **Fix:**
  - **Item 6:** one search for each sentence, with the unmatched points' terms as alternatives and `--max 10`, reading at most 5 documents.
  - **Item 8:** at most 20 not-found rows, those on money flows, legal structure, the data model or partner contracts first. The other points go in `notes.md` as not checked.
  - **`nf_id`:** it takes three digits, in the checker and in the recording brief's table (line 154).
- **Test:** a hand-made record has `Q3-BC-N01`, `Q3-BC-N100` and `Q3-BC-N1000`, each cited in `account.md`.
  - The first two pass in both files.
  - The four-digit one is still refused in both.
- **The cap:** each of the 20 rows still carries rule 7's own search, as before. The cap is on rows.
- **New:** the points past 20 aren't kept out of the account (new problem 4).

### 8. Arabic Shopify pages as the checker reads them: fixed
- **Fix:**
  - `help_map.py` prints Arabic pages through `quote_check.html_text`.
  - The brief (line 34) and the tool give the Arabic path.
- **Test:**
  - **The finding's page:** `help_map.py shopify page content.html/ar/manual/international/pricing/dynamic-tax-inclusive-pricing.html` prints the countries on their own lines.
    - "ألبانيا غرينلاند الفلبين" is found against the page's source. The old "ألبانياغرينلاندالفلبين" is not.
    - All 126 non-blank lines printed pass. From the pre-fix tool, 32 of 64 failed.
  - **More pages:** the 791 Arabic pages that hold table cells, and 60 others drawn at random.
    - Of their 103,638 printed lines, 103,632 pass.
    - The other 6 hold only zero-width spaces.
  - **The path:** the stated path holds for 2,670 of the 2,674 English pages.
  - **Size:** across all 2,697 Arabic pages, the output grows by about 3% in bytes, mostly in blank lines.
- **New:** the output now shows HTML entities (new problem 2).

### 9. Reading for sentences that ask nothing: fixed
- **Fix:** step 3 (line 89) now says "A sentence that only gives examples, limits or restates the question has no reading of its own: it shares the reading of the sentence it serves."
- **Check:** this is the finding's own fix. It only narrows the plan's per-sentence maxima. There is nothing to run.

### 10. The capture rule, wherever the plan states it: fixed
- **Fix:** the entry in PLAN.md section 11 (line 593) now changes the rule "wherever the plan states it (sections 2, 3, 6 and 9)".
- **Test:** the rule's wording sits at PLAN.md lines 44, 96, 317 and 419. These are in sections 2, 3, 6 and 9: the sections the entry names, and no others.

### 11. Words the in-depth platform shares: fixed
- **Fix:** the checking brief's item 2 (line 18) now says "Use only your own platform's words in your statements, identifiers, scopes and headings. Never take a word from an account that your own source doesn't use."
- **Check:**
  - This is the finding's own fix. There is nothing to run.
  - It no longer conflicts with item 3's first basis, "the same term": a Salla run may record Salla's own "Markets / الأسواق المتعددة".

## New problems

**1. The brief's command to read a PDF save fails on every PDF.**
- **Where:** recording brief, line 43: `pdftotext -q '<file>' -`.
- **Problem:** all 21 PDFs sit in the folder "Commerce's Trust Center documentation", and its apostrophe ends the single quotes. With a real path filled in, bash reports a syntax error and runs nothing.
- **Fix:** `pdftotext -q "<file>" -`.
- **Severity:** optional. A run that hits the error can quote the path again, and nothing wrong is recorded. Best fixed before BigCommerce runs.

**2. `help_map.py` now prints HTML entities on Arabic Shopify pages.**
- **Where:** `help_map.py`, line 48. The pre-fix code unescaped entities, and `quote_check.html_text` doesn't.
- **Problem:** 1,437 of the 2,697 Arabic pages print them, 15,049 in all.
  - Most are `&gt;` in settings paths, such as "الإعدادات &gt; نطاقات المواقع". The rest are `&lt;`, `&quot;`, `&amp;` and `&nbsp;`.
  - Quotes and statements pass either way, because the checker unescapes both sides.
  - But a run reads `&gt;` where the page shows ">". An identifier copied from the output keeps it, and identifiers aren't checked.
  - Unescaping the output would break some quotes. In 150 such pages, 3 of 17,022 lines would then fail, where the page escapes its text twice (`&amp;#8230`).
- **Fix:** add a line to the brief: "Arabic pages show some characters as HTML entities, such as `&gt;` for >. A quote may keep them; an identifier doesn't."
- **Severity:** optional.

**3. `show S-01` prints 27 to 52 KB.**
- **Where:** `copy_statements.py`, lines 151 to 155.
- **Problem:** it prints all the pilot's statements: 128 to 202 rows, depending on the platform.
  - On Salla, that is 52 KB: 2.6 times the largest concern of Q3, SA-C-020, at 20 KB.
  - S-01 has no terms, so every run but Q5's runs `show` for it once. The sample does too.
- **Fix:** print S-01's distinct identifiers instead: 148 on Salla, in 9.6 KB. Or cut each statement shorter.
- **Severity:** optional. It costs the sample one large call, but doesn't stop it.

**4. The points past 20 aren't kept out of the account.**
- **Where:** checking brief, item 8 (lines 41 and 42).
- **Problem:** the points past the 20 rows go to `notes.md` as not checked. Nothing keeps them out of `account.md`.
  - Item 4 gives every account point a label.
  - Item 10 says a "not in what was read" point ends with its `nf_id`, and these points have none.
  - A run that writes them into `account.md` gets "a point that cites no id of this folder" from the checker.
- **Fix:** add "Leave them out of `account.md`."
- **Severity:** optional.

## Verdict

**The recording brief can now run the sample, Q3 on Salla. Nothing must change first.**
- The three findings that stood in its way are fixed, and tested on Salla:
  - `--max 10` on step 3's search (1);
  - Salla's categories listed in both languages, with the central Arabic-only articles (2);
  - `show` for S-01 and for SA-C-233 (3).
- With every row copied, Q3 on Salla passes the checker. The help map's articles pass the quote checker, and the corpus search is as it was.
- Only new problem 3 touches the sample: one 52 KB call to judge S-01. It is optional.

**All 11 findings are fixed, the 7 must-fix findings among them.** By the runs they affect:
- **WooCommerce:** findings 4 and 5.
- **BigCommerce:** finding 6. The brief's PDF command (new problem 1) is best fixed before BigCommerce runs.
- **Checking runs:** finding 7. New problem 4 can go with the checking brief's reading before its first run (its line 3).
