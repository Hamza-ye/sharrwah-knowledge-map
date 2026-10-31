# Inspection of the held pass's second stage: its brief, design and tools (31 October 2026)

**What this is:** an inspection, before it runs, of `briefs/S2-held.md`, its design `briefs/S2-held-design.md` with the coordinator's decisions and the plain words of the rulings `S2-R1` and `S2-R2`, the tool `method/s2_held.py`, and this stage's changes to `class_slice.py`, `held_entries.py`, `held_amend.py` and `q3_misses.py` (`git diff 0b5a37d0 3d0f032f -- method/`), as `PLAN.md`, section 3 asks. The inspector wrote none of them, and changed no file except this one.

**What was read, and at which commits:**
- The brief, the design and the tools at `3d0f032f`. None of them changed up to `843d118a`, while this inspection ran (nine commits, to `STATE.md`, the veto list, the architecture plan and `held/shopify/amendment-notes.md`).
- The evidence at observed-sh `04de369da`, observed-sa `b0bd0b163`, other-product-class `0d79b794f`, and WooCommerce's release 11.2.1.
- Every test that writes ran on scratch copies of `studies/class-model` (`CLASS_MODEL_DIR`), with fixtures that cite real held files at those commits ("What I ran").

The findings are numbered S2I-n, so they don't read as parts (`S2-ZD-1`) or rulings (`S2-R1`).

Severity: **must fix** means an agent following the brief would write wrong rows, or the coordinator's landing or amendment would write a wrong model. **Should fix** means the output would be less consistent, harder to check or act on, or costlier than it needs to be. **Note** is for the record.

**What holds:**
- **The brief takes the earlier inspection's findings** as the design's table says, in each one I checked against `inspection-Q3M.md`: this repository's captures and the founder's saves are citable (Q3M-1); a miss is read part by part (Q3M-3); `absent`, `unreadable` and `unclear` exist (Q3M-4); a capture names `needs:` (Q3M-7); no example comes from a miss (Q3M-8); the rests carry a label (Q3M-9); the commits are fixed (Q3M-13); an archive's offset goes in `locator` (Q3M-17).
- **The checker,** on a baseline of four parts (14 rows of every outcome, three misses and a `new` row on Zid; rows on Salla and Shopify), passes it, and refuses 52 of 72 one-fault variants. It refuses every fault this inspection was asked to try:
  - a quote not in its source;
  - a quote at the wrong line, 7 and 4 lines off (3 off passes, as the brief allows);
  - a `found` row with no source;
  - two outcomes for one cell, and two `not-found` rows for one cell;
  - a cell with no row, and a miss's part with no row;
  - a cap_id not in the model;
  - a wrong commit: an older other-product-class, and this repository's HEAD as `corpus_search.py` prints it;
  - a column filled that its outcome doesn't take (`supports`, `source`, `locator`, `quote`, `capture`, `could_change`, `place`, `as`, `scope`);
  - a double quote.

  The 20 that pass: 8 are right to pass, 3 are harmless, 7 are gaps (S2I-6, S2I-9, S2I-12, S2I-13, S2I-14) and 2 pass with a false note (S2I-9).
- **The within-three-lines test works on markup** (`s2_held.source_problems`, as the checker calls it), each at its own line:
  - HTML in Arabic: a paragraph; a list item with inline tags and `&gt;`; a word quoted without its shadda; the `<h1>` title. The same item cited 4 lines off is refused;
  - Markdown: a sentence with a bold link, quoted as rendered and as the raw Markdown; an HTML table's row whose cells sit on separate lines;
  - a pretty-printed JSON answer, a JSONL article across a `\n`, and `woocommerce.pot` entries, one-line and split over lines.
- **End to end on the copy** (Zid's fixture part):
  1. `land`: 6 entries in `entries-s2.tsv`, 5 in the batch, 5 placement lines, 1 row to `s2-keys.tsv`, 7 outcomes, 3 capture leads;
  2. `held_entries.py check --batch S2-ZD`: 0 problems;
  3. `held_amend.py plan`, then `apply --batch S2-ZD`: 6 evidence rows for 6 cells in 5 parts, 4 cells that held nothing become held, 5 cells still holding nothing take the outcome sentence;
  4. `check_class_part.py` on each of the 5 parts: 0 problems. Its flags went 37, 4, 18, 16, 96 to 37, 4, 17, 15, 97, each change from the fixture's own lines;
  5. `class_merge.py --complete`: 0 problems, 3,469 flags. The unchanged copy gave 3,467, as the real model does. The 2 new flags both come from the fixture's term `shipments` on CM-SHP-013 ("CM-APP-005 (domain F) and CM-SHP-013 (domain C) share terms shipments, shopify functions: one capability?", and the same with CM-INV-006). No flag came from the outcome sentences or the searched terms.

  A correction batch ran the same way: `land` refused the applied batch ("S2-ZD was applied … --batch S2-ZD-R1"), `--batch S2-ZD-R1` landed 1 line, and every check and the merge gave 0 problems (3,469 flags).
- **A second landing writes the same files:** the md5 of all eight was unchanged.
- **An id that `entries.tsv` already holds** is lengthened: `COLLISION s2/S2-ZD-1.tsv line 2: ZD-E-c2c81d024f (10 digits)`, and `held_entries.py check` passes.

---

## Must fix

**S2I-1. A passage that a capture holds outside its `text.txt` can't be cited as the brief says, so an agent will record held passages as not found.**
- *Found:*
  - The brief: "`sharrwah-knowledge-map@<commit>:<path>`, the path as `corpus_search.py` prints it (`evidence/product-class/runs/<run>/items/<n>-<host>/text.txt`, …)" (line 154).
  - `corpus_search.py` searches a capture's `text.txt` with its `expanded.txt` ("the lines a click shows, such as FAQ answers") and the extra lines of its `rendered.html` (lines 316 to 327), and its `raw*.html` (lines 330 to 335). It still prints `text.txt` as the path (line 346), or `<item>/raw`, which is no file (line 350), or `text.txt (and the raw page beside it…)` (line 343).
  - Two real cases:
    - `corpus_search.py zid "suited to the Syrian market" --brief --max 3` printed `…/20261027T135846Z-s02-a2-sources-batch-4/items/002-zid.sa/text.txt`. The sentence 'We provide shipping and delivery solutions suited to the Syrian market through:' is in that item's `expanded.txt`, line 2. `quote_check.py` on `text.txt`: "not found; 0.00 of its six-word runs"; on `expanded.txt`: "found". The checker refused the `text.txt` citation and passed the `expanded.txt` one.
    - The Zid search for `ملفات تعريف الارتباط` printed `…/20261027T121854Z-s02-a2-sources-batch-3/items/016-zid.eg/raw (the page as served…)`. Cited at that path: "the source doesn't resolve: git show 3d0f032f6:…/016-zid.eg/raw failed". At `text.txt`: not found. At `raw.html`: found.
  - How many captures this touches: 17 items hold an `expanded.txt` (9 of zid.sa, 5 of woocommerce.com, 3 of developer.woocommerce.com). 190 hold a `text.txt` of under 1,500 characters besides spaces, where `corpus_search.py` points to the raw page: 55 of help.zid.sa, 42 of docs.bigcommerce.com, 34 of zid.sa, 10 of help.shopify.com and others.
  - Neither the brief, the evidence map ("This repository's own evidence") nor `evidence/product-class/README.md` says which file of a capture holds what.
  - A reading: Zid runs first because it "exercises the most source forms in one part", this repository's captured help.zid.sa, docs.zid.sa and zid.sa pages among them (design, section 4). An agent following line 154 gets a refusal for a passage that is held, and may write `not-found` or `unclear` for it.
- *Fix:*
  - In `corpus_search.py`: print the file of the capture whose text matched (`text.txt`, `expanded.txt`, `rendered.html` or `raw.html`), never `<item>/raw`.
  - Until then, in the brief, "Sources and locators": "A capture's item holds several files: `text.txt` (the page as rendered), `expanded.txt` (what a click shows), `rendered.html` and `raw.html` or `raw-browser.html` (the page's markup). Where `corpus_search.py` prints `text.txt (and the raw page beside it…)` or `<item>/raw`, or the quote isn't in `text.txt`, cite the file of the item that holds it. `quote_check.py SOURCE LOCATOR TEXT` on each says which."

**S2I-2. `not-held` takes a gap register's row that names a whole surface, so nearly any Zid or BigCommerce cell can be `not-held`, and two agents will split the same cell between `not-found` and `not-held`.**
- *Found:*
  - The brief, lines 86 to 91: `not-held` is "as `not-found`, and the place where your platform would state the thing isn't held. That means one of these: … a `GAPS.md` row; …".
  - Zid's register, line 18: "Zid's other surfaces: help.zid.sa, docs.zid.sa, zid.sa, the app and theme markets, the mobile apps | not captured here; sharrwah-knowledge-map holds some of their pages". Lines 11 and 12 cover "The dashboard routes the ledger marks `not opened`" and "The routes whose path takes an id (… 112 of the manifest's 437)".
  - The fixture's `not-held` row citing only "zid/GAPS.md row 18" passed the checker.
  - What hangs on the split:
    - every `not-held` row carries a capture lead, and `could_change` routes most of them to a handoff (S2I-11);
    - the omission review samples this stage's `not-found` rows (the coordinator's decision 9), so a cell written `not-held` leaves its sample.
  - A reading: on Zid, where help and docs are held only in part, one careful agent writes `not-found` (it searched what is held), another `not-held` (the help centre isn't captured). Both follow the brief.
- *Fix:* replace the three cases with: "`not-held`: as `not-found`, and you name the place, by its address or row, where your platform would state the thing and that isn't held: a ledger row marked `not attempted` or `not opened`; a sitemap entry not captured; a held page's link to a page not held; or a `GAPS.md` row that names that place. A `GAPS.md` row that names a whole surface, such as `zid/GAPS.md`'s 'Zid's other surfaces', isn't enough: write `not-found`, with the row in `read`. That the named page would state the thing is an assumption: say so."

**S2I-3. Two rows that put one passage on one capability land as one line with the first row's supports, so a second row's `core` is dropped, and every check passes.**
- *Found:*
  - `land` keys a line by entry, capability, scope and filler (`s2_held.py` lines 1098 to 1104). A second row with the same key adds only its reference: its `supports`, `terms` and `quality` are dropped.
  - Tested on a copy: CM-PAY-033's cell row with `shows` (line 4) and M-12's first part with `core` (line 12), on the same passage, the miss decided as CM-PAY-033. The batch got one line, `ZD-E-9e7d3ce8 capability CM-PAY-033 shows`, its reading still ending "(core)", with both references. `s2_held.py check` and `held_entries.py check` gave 0 problems.
  - This is the case the design builds in: a miss's part and a cell of the same part are one thing for M-01 and CM-CHK-012, M-04 and CM-SRF-003, and M-12 and CM-PAY-033 (design, section 5). The same agent reads both, and nothing asks it to give them one support.
  - A reading: with the cell's row first and `shows`, the cell doesn't count, though the stage found `core`. That changes a count.
- *Fix:*
  - In `check`: refuse two rows of a part that cite one passage (or one id) on one capability, the cell's own or the miss's proposal, with different `supports`, `terms`, `filler` or `quality`. The message: "rows N and M cite one passage on CAP: give them the same supports, terms and quality".
  - In `land`, for rows of two parts: union the supports, terms and qualities into the one line, and print each merge.
  - In the brief, "Q3's misses": "Where a part of a miss is the thing of one of your cells, its row and the cell's cite the same passage with the same supports."

**S2I-4. A miss's `found` row lands on the coordinator's capability with the reading and supports its agent wrote for its own proposal.**
- *Found:*
  - `land` takes the capability from `held/s2-misses.tsv` (lines 1080 to 1089), and the line's `supports`, `scope`, `terms`, `filler`, `quality` and `reading` from the row (lines 1104 to 1106, the reading's suffix at line 1149; `s2-keys.tsv`'s `why`, lines 1112 to 1113). Nothing names the miss or the decision.
  - Tested on a copy: M-13 decided as `its thing` of CM-ORD-005, where the row proposed `feature` of CM-PAY-030. `s2-keys.tsv` got `CM-ORD-005 … ZD-C-081/boundary/ZD-S-0912 (the held pass's second stage, S2-ZD, S2-ZD-1 line 14) A reading: the API reference lists 'Upload bank transfer receipt' under Merchant APIs > Reverse Orders, already a statement of the concern map.`, with the row's `core`.
  - A reading: the decision is one per miss and the proposals are five, so on some platforms they will differ. The model's evidence row then gives a reason written for another capability, and a support judged for it.
- *Fix:*
  - In `land`, for a miss's row: append to the line's reading "(M-nn: <part>, landed as <as> of <capability> by held/s2-misses.tsv: <its reading>)".
  - Where the decision differs from the row's proposal, take the row out of the batch and print it: "decided otherwise than proposed: give its supports in s2-misses.tsv". Add a `supports` column to `s2-misses.tsv` for those rows.

---

## Should fix

**S2I-5. A miss must be decided before any landing, and a decision sticks once its batch is applied, while nothing waits for the five platforms' rows.**
- *Found:*
  - `land` stops at a miss's `found` row with no decision: "decide it first (check-misses)" (lines 1083 to 1084).
  - `check-misses` doesn't test that each platform has its rows: `misses-join` shows "no row yet", but nothing refuses a decision made then.
  - The design's order lands `S2-ZD-1` end to end first, then the other parts four at a time. The parts that hold most misses' cells (`S2-SA-1`, `S2-WC-1`) run in the last round (design, section 4).
  - Once a batch is applied, a correction batch only adds lines (lines 1044 to 1047, 1098 to 1100). A reading of the code: a decision changed after Zid's batch is applied lands Zid's passage on the new capability too, and the line on the first capability stays in the model.
  - This works against the coordinator's decision 5: "the coordinator decides each miss once, from the five platforms' rows side by side".
- *Fix:*
  - In `land`: hold a miss's `found` rows back, as "waiting for the miss's decision", instead of stopping. They land in a correction batch once `s2-misses.tsv` holds the decision.
  - In `check-misses`: refuse a decision while `misses-join` shows a platform with no row for the miss.

**S2I-6. The line test reads only the quote's first five words, so a quote cited 45 lines from where it stands passes.**
- *Found:*
  - `near_problem` takes `" ".join(loose(quote).split()[:5])` (line 272).
  - Zid's `mokafaa.json` holds 'Overview of customers’ points rule (earn & redeem).' at line 29 and 'Overview of customers’ points rule (earn & redeem) and your plan usage fees.' at line 74. The second, cited at `line 29`, passed the checker, as it did at `line 74`.
  - Other pairs like it, far apart, in Zid's English locales alone: `analytics.json` lines 138 and 1083, `payments.json` 186 and 1217, `settings.json` 930 and 934.
  - A reading: `held_entries.py check` runs the same test on a landed entry. The page then links a wrong line, and the coordinator reads the wrong place.
- *Fix:* test that the whole quote, as `loose()` folds it, begins within the window, or that its first 12 words do (all of them where it is shorter). Message: "the quote begins at line M, not within three lines of N".

**S2I-7. `line N` in `quote_check.py --text`'s output isn't the line the checker counts.**
- *Found:*
  - The brief: "Read a long document in parts, with `quote_check.py --text`, `sed -n` or `grep -n`" (line 185), and "`line N`: the line where the quote begins" (line 152).
  - `--text` drops blank lines (`quote_check.py` line 248). For HTML it prints the markup's text, broken at block tags. The checker counts the file's own lines (`file_lines()`, `s2_held.py` line 248).
  - Measured:
    - the Zid help page's 3D Secure sentence: `text.txt` line 98, `--text` line 52;
    - Shopify's Arabic tipping page, its second 'من مسؤول Shopify، انتقل إلى': line 81 of the file, line 63 of `--text`;
    - BigCommerce's saved "AI Management Policy.pdf": line 32 of `pdftotext`'s output, which the checker reads, and line 23 of `--text`. At `line 23` the checker refused it ("not within three lines").
  - For a PDF, no tool the brief names prints the checker's numbering.
- *Fix:* in "Sources and locators": "`line N` counts the file's own lines. Find N with `grep -n` on the file, or for a PDF with `pdftotext -q FILE - | grep -n`, never in `quote_check.py --text`'s output, which drops blank lines." Or make `--text --lines` print the file's lines with their numbers.

**S2I-8. Three quote forms the brief names can't pass the checker as one quote, and the checker suggests a fourth that fails.**
- *Found:*
  - The brief: "That is a sentence, a table row with its heading, a list item with the heading it sits under, or a locale string with its key" (line 160). A quote is tested as one run of the source's text (`quote_check.check_quote`).
  - A list item with the heading it sits under is one run only where it is the first item:
    - 'Considerations for tipping options in your online store: The Subscription API doesn't support tipping.' (`tips.md`): "not found (0.33 of its six-word runs)";
    - 'Order Properties Enable reorder feature' (Zid's step 009): not found.

    A table row with its header row passed only for the first row of an HTML table in Markdown.
  - A locale string with its key:
    - 'enableLowStockAlert: Enable low stock notifications': not found;
    - '“enableLowStockAlert”: “Enable low stock notifications”' passed, since `quote_check.norm` reads “ ” as `"`.
  - A passage with a straight double quote:
    - the row can't hold it ("holds a double quote (\"), which these files can't carry: quote with ' or “ ”", `s2_held.py` lines 139 to 140);
    - 'Automatically change paid new orders status to “completed”' passed;
    - with `'` in place of `"` it failed ("not found (0.67 …)").
- *Fix:*
  - In the brief, line 160: "A table row or a list item is quoted alone. Its heading goes in `identifier`, or in `reading` as a quote of its own. A locale string is quoted with its key as “key”: “value”. A straight double quote in the passage is written as “ or ”, which the checker reads as the same."
  - In the checker's message: drop "'".

**S2I-9. The Arabic-search note tests a label, not Arabic, and only on `not-found`.**
- *Found:*
  - `check` notes "not-found on <p> with no Arabic search" where no `searched` piece matches `\bar:` (lines 698 to 699).
  - On Salla's fixture:
    - `corpus_search ar: barcode, print`, English words under `ar:`: no note;
    - Arabic only in `class_slice search ar: باركود`, the concern map, not the held pages: no note;
    - a `not-held` row with no Arabic search: no note;
    - `corpus_search arabic: باركود` and `corpus_search AR: باركود`: the note, though Arabic was searched.
  - The brief asks for every language the platform holds, "English, and Arabic too for Salla and Zid" (line 70). `not-held` is "as `not-found`" (line 86).
- *Fix:* for Salla and Zid, note each `not-found`, `not-held` and `absent` row with no piece that names `corpus_search` and holds a term in Arabic script (`[؀-ۿ]`), whatever its label. Message: "no corpus_search in Arabic: the held pages' Arabic was not searched".

**S2I-10. `searched`: the form of `nothing` isn't given, and a chunk's search recorded in each row would put other cells' terms in each cell's `searched` in the model.**
- *Found:*
  - The brief: "A search that printed nothing is recorded as `nothing`" (line 145).
    - `nothing` as a piece of its own is refused: "each search is `<tool> <language>: <terms>` …: 'nothing'".
    - `corpus_search en: tip, tipping (nothing)` passes, and `held_amend.search_terms` strips "(nothing)", ": nothing" and "→ nothing" (lines 178 to 190).
  - The brief asks for "one `corpus_search.py --brief` per language, with all the chunk's terms in one call" (line 181). It doesn't say whether a row records that call or the cell's terms in it.
  - `apply` adds every term of a still-empty cell's `searched` to the cell's own `searched` (`held_amend.py` lines 279 to 282). `check_class_part.py` flags a cell holding nothing whose `searched` terms match statements (lines 399 to 403). The page prints them under "Searched" (template line 345).
  - A reading: a row that records the chunk's call gives the cell 10 to 20 cells' terms. The omission review, which samples these rows, couldn't tell which were the cell's.
- *Fix:* line 145: "Record only this cell's terms, from a chunk's search, as `corpus_search ar: <term>, <term>`. A search that found nothing for the cell ends in ` (nothing)`, such as `corpus_search ar: إكرامية, بقشيش (nothing)`."

**S2I-11. `could_change`: `decision` covers two thirds of the cells, `no` is undefined, and the triage sends rows that aren't capture requests to a handoff.**
- *Found:*
  - `decision`: "a Q3 row or a subject's point names the cell or its capability (`cells` prints them)" (line 101).
    - Over the 620 cells, `cells` prints a Q3 row or a point for 415 (67%).
    - Of the Q3 lines it prints, 729 are `covered`, 131 `partly` and 2 `beyond the class`; no Q3 row names a cell itself (`CM-…@<platform>`).
    - Counting only rows not `covered`, and the points: 160 cells (26%).
  - `kind` applies to the 28 cells whose capability is `slot` (24) or `open` (4). Of the rest, `count` and `no` aren't told apart: "`no`." alone (line 102). A reading: a core passage on a cell holding nothing always changes its count, so `no` has no case.
  - Where two values apply, nothing says which wins.
  - `decision` doesn't record which row or point, which a handoff's "Why: the subject, root decision and gap ids it answers" needs (`handoffs/README.md`).
  - The triage (decision 6) sends `kind` and `decision` to `handoffs/` for `not-held`, `unreadable` and `unclear` alike. `PLAN.md`, section 6: "if it is held but not readable, the reader is extended", which is no capture.
  - With S2I-2, a reading: most `not-held` rows on Zid and BigCommerce would go to a handoff. Against `STATE.md`: "Capture stays the exception, only where a gap could change the model or a decision".
- *Fix:*
  - Line 101: "`decision: <id>`: a Q3 row whose result isn't `covered`, or a subject's point, names the cell or its capability; name it."
  - Line 102: "`no`: the cell's count and kind can't change, because …, said in `reading`."
  - Add: "Where several apply, write the first of `kind`, `decision`, `count`."
  - Decision 6: "a handoff for `not-held` only; `unreadable` extends the reader; `unclear` goes to the coordinator".

**S2I-12. `capture`: another platform's repository passes, the handoff's "Done when" has no place, and Salla has no `index/instruments.json`.**
- *Found:*
  - The checker tests the repository against all three evidence repositories (line 705). `observed-sh; ibx5bt-xy; a journey; stop at save; needs: nothing` passed on a Zid row.
  - `handoffs/README.md`: "Every file has the same parts: Repository and instrument … What to capture … Already held … Why … Needs … Done when". The capture has no "done when". `s2-captures.tsv` carries neither the row's `read` and `searched` (already held) nor which Q3 row or point (why).
  - The brief: "<instrument, from index/instruments.json>" (line 106). observed-sa's `index/` holds none. Its instruments are in `docs/PLAN.md`, "Instruments", which `docs/READING.md` (lines 40 to 41) points to.
- *Fix:*
  - In `check`: the capture's repository is the platform's (`observed-sh` for Shopify, `observed-sa` for Salla, `other-product-class` for the other three).
  - The form: `…; stop at <…>; needs: <…>; done when: <what the run must hold>`.
  - `s2-captures.tsv` takes `read`, `searched` and the `could_change` id.
  - Line 106: "from `index/instruments.json`, or for Salla `docs/PLAN.md`, 'Instruments'".

**S2I-13. A miss's agent must propose a capability even where its platform holds nothing of the miss, and `not a capability` passes on a row that found nothing.**
- *Found:*
  - The brief: "the capability you propose for the miss from what your platform holds" (line 115).
  - `check` refuses a miss's row with no `as` (lines 613 to 614). The fixture's `not-found` row with an empty `as` and `cap_id` was refused ("a miss's row carries as: one of its thing, feature, new, not a capability").
  - `not a capability` is defined as "it is held, but it isn't 'something a store or the platform can have or not have'" (line 119). On a `not-found` row it passed.
  - A reading: an agent that found nothing proposes from the model, not from its platform, and `misses-join` prints it as a proposal beside the platforms that found something.
- *Fix:* allow `as` `none` with an empty `cap_id` on every row of a miss whose parts are all `not-found`, `not-held`, `unreadable` or `unclear` ("no proposal: nothing held"). Refuse `not a capability` on a miss whose parts aren't held.

**S2I-14. A `new` row with `place` `none` and `supports` `core` passes, where the brief says `shows`.**
- *Found:* "A thing with no place of its own is still written as `new:<name>`, with `supports` `shows` and `place` `none`" (line 125). The fixture's `new` row with `place` `none` and `supports` `core` passed.
- *Fix:* in `check`: a `new` row whose `place` is `none` takes `supports` `shows` only.

**S2I-15. The misses' rests are stale, and their "settled by" pages are named as if they exist.**
- *Found:*
  - `misses` prints each rest under the label "Q3's batch, from the concern map only: its 'none held' and 'not held' are what this check tests" (`q3_misses.REST_LABEL`). The label covers held and not held, not the rest's other claims.
  - Stale, since the held pass made CM-CHK-012, CM-PAY-033 and CM-SRF-003 (design, section 5):
    - M-01: "the coordinator decides whether tipping is a capability or a setting of CM-CHK-001";
    - M-12: "no capability is it".
  - Pages named as if they exist:
    - M-04: "a capture of Salla's and Zid's dashboard language switch";
    - M-06: "the label-buying screens of Salla and Zid";
    - M-07: "Salla's and Zid's returns settings";
    - M-08: "Salla's Partners portal Ready Stores and Store management pages, and BigCommerce's Partner Portal docs on client stores";
    - M-09: "Zid's and BigCommerce's developer changelogs";
    - M-12: "Shopify's help-centre and developer pages on 3D Secure and the chargeback liability it shifts". That presupposes M-12's second part on Shopify.

    M-10, M-11 and M-13 mark theirs as assumptions.
  - A reading: an agent may stop at the named page, propose `feature` of CM-CHK-001 for M-01 or `new` for M-12, or write `not-held` for a page no held source names.
- *Fix:*
  - Make the label: "Q3's batch, from the concern map only, before the held pass made CM-CHK-012, CM-PAY-033 and CM-SRF-003: its 'none held' and 'not held' are what this check tests, and the pages it says would settle a miss are its agent's assumptions, not evidence that they exist."
  - Or print each rest's "settled by" clause as "Q3's guess at where it is held: an assumption".

**S2I-16. Three misses' parts read wider or narrower than their thing.**
- *Found* (`q3_misses.py`, `PARTS`):
  - **M-12's second part,** "the shift of a fraud loss or chargeback liability away from the seller", reads alone as any shift. Q3's rest calls the others covered ("Shopify Protect covers fraudulent chargebacks on eligible orders (SH-S-0404)"). A reading: one agent writes `found` from chargeback protection, another reads it as the shift by 3D Secure, the thing's words ("strong buyer authentication (3D Secure) shifting a fraud loss").
  - **M-11's parts** keep "the shipment's return" and "what is charged", and drop "as a way to contest a payment, whatever the payment method". PAY-30 asks "Which channels can a buyer use to contest a payment (… refusal at delivery)". A reading: a cash-on-delivery refusal page would make both parts `found`, though the row asks about contesting a payment already made.
  - **M-04's** "numerals", "date formats" and "mixed-direction text" don't say whose. LNG-02 asks of "translated admin, RTL layout, Arabic storefront, numerals, dates, mixed-direction text". BigCommerce's `standard-formats` holds the store's date formats per country, not the admin's.
- *Fix:*
  - M-12's second part: "the shift of a fraud loss or chargeback liability away from the seller when the buyer is authenticated (3D Secure)".
  - M-11's first: "the shipment's return when the buyer refuses it at the door, on a prepaid order as on cash on delivery".
  - M-04's: "right-to-left layout of the admin and the storefront", "numerals shown to merchants and buyers", "date formats, the Hijri calendar among them", "mixed-direction text".

**S2I-17. Leads that set a capability aside print as leads under the cell they name.**
- *Found:*
  - The held pass's "Leads no line takes, each a homonym or named in passing" sit in sections whose heading names the second stage. So `leads` prints them in group 1, and `cells` prints each under every cell it names as "lead:". Examples:
    - `notes-SH-53.md` line 147: "CM-CAT-005 (brands, holds nothing), the checker's first lead for Collective: 'Shopify brands' are merchants";
    - `notes-SH-54.md` line 177;
    - `notes-WC-7.md` line 147: "First leads whose cell holds nothing … none is the entry's thing".
  - Of Shopify's 16 group-1 leads, 6 set capabilities aside. WooCommerce's parts each have one.
  - The brief: "A lead is only a lead: what it says a file states, you read in the file" (line 22). That covers what a file states, not a held-pass agent's judgment that it isn't the thing.
  - The cut, as asked:
    - Shopify: 16 leads name its cells, 256 name no capability (printed whole: 89,683 characters with group 1), 272 name only cells already held;
    - Salla: `S2-SA-1` 4, 106 and 267, and `S2-SA-2` 5, 106 and 266. The 106 that name no capability print in both parts;
    - a run's label paragraph prints as a lead of its own, apart from its bullets, such as `notes-ZD-CH.md` line 85, "Run 20261028T150740Z-settings-gaps-en:". A bullet naming a held cell then prints in `--held` without its run. Its `batch:line` leads back to it.
- *Fix:*
  - In the brief, line 22: "A lead that sets a passage aside (a homonym, 'no lead', 'none is the entry's thing') is the held pass agent's reading: read the passage yourself before you agree."
  - In `leads`: mark such bullets "set aside by <batch>", and print a lead's nearest label paragraph with it.

**S2I-18. `cells` prints the concern map's reading and the other platforms' held lines unlabelled, and the brief doesn't carry M-5.**
- *Found:*
  - `cells` prints "<platform> reading:" (line 499) with no label, where `misses` labels the rests. Most readings say they are the concern map's ("none-held means only that the concern map holds nothing found by these terms"). One presupposes its answer with no source: CM-ACC-011 on Zid, "A reading: Zid is a hosted service, and the search finds no licence of its software."
  - `cells` prints "the held pass on <platform>, N rows: …" (line 510).
  - H-held's rule: "A provider's role that only another platform's cell states (instalments, cryptocurrency) is a lead for your notes, not evidence (M-5)" ("Rules"). The brief cites only "Never decide a maker, a third party or a placement from what you know of the platform (H-held.md, 'Rules')" (line 84). Its reading list (lines 29 to 33) doesn't include H-held's "Rules".
- *Fix:*
  - In `cells`: "<platform>'s reading, from the concern map only:" and "the held pass on <platform> (leads for your search, never evidence for your platform):".
  - In the brief, line 84: add M-5's sentence.

**S2I-19. The held pass's selection sends twelve structures to "the second stage". The brief names two, and one serves cells already held, which S2-R2 leaves out.**
- *Found:*
  - `held/selection.tsv` sends these to the second stage:
    - Shopify's `dev-changelog`, `help-section-children` ("Help titles are read in the second stage, by cell, on every platform"), `status-page`, `legal-documents`, `compliance-reports` and `dev-mcp-instructions`;
    - Salla's `help-articles`, `help-tree`, `help-embedded-tree` and `marketplace-apps` ("third parties' listings … by cell in the second stage");
    - BigCommerce's `standard-formats`: "Read by the second stage for Q3's miss M-04 and the cells that need it".
  - The brief names only the Help Center and Salla's help articles ("Where the held pages are").
  - `compliance-reports`: "certifications, read as the qualities of the trust and payments cells in the second stage". CM-TRU-018 (PCI DSS) is held on Shopify (`core`), so S2-R2 puts it out of this stage.
  - A reading: BigCommerce's formats are held as fields (`display_date_format`, `decimal_token`, `standard-formats/items.jsonl`). A search for "date format" listed no structure (`corpus_search.py bigcommerce "date format" "decimal separator" "thousands separator" --brief`).
- *Fix:*
  - In "Where the held pages are", per platform: "and the structures `held/selection.tsv` sends to the second stage: <the list>, read where your cells or misses need them".
  - For `compliance-reports`: say in `STATE.md` who reads the held cells' qualities, since this stage doesn't.

**S2I-20. The brief applies the rulings in `held/review-H-rulings.md` but doesn't list the file, and some of its leads for this stage are outside `leads`.**
- *Found:*
  - Line 31: "the rulings they name (M-1 to M-14, and the rulings in `held/review-H-rulings.md`) apply to it". The reading list (lines 15 to 41) doesn't include the file (37,842 characters).
  - Its section "What the corrections leave for the second stage" (lines 36 to 43), and the lead "for CM-APP-011, the platform's own apps, which holds nothing on Salla. The App Store's listing is read with the second stage" (line 97), aren't in `notes-*.md`, the only files `leads` reads (line 392).
  - The two cells that section names are held now (CM-PLN-002 on BigCommerce, CM-SEL-007 on Zid). CM-APP-011 holds nothing on Salla.
- *Fix:*
  - Add to item 4: "`held/review-H-rulings.md`, its sections 'Who does it, and `supports`' and 'What an entry is, and where its other things go'".
  - Add the file's second-stage leads to `leads`' inputs.

**S2I-21. The rulings' plain words leave out what each risks most, and S2-R1 conflicts with the line before it.**
- *Found:*
  - **S2-R1** (design, line 367): "cites the passage showing the strongest support first, and a further passage only where it shows a support or a scope not cited yet; then it stops. *What it risks:* fewer sources per cell for a later reviewer to cross-check …".
    - A reading: stopping also drops what later passages state that isn't a support or a scope: a quality (a limit, a fee, a price), a slot filler (a provider, a law) and the platform's other terms. The model records those in `qualities.tsv` and `slot-fillers.tsv` (B-extent, "Qualities and slot fillers").
    - The brief puts two orders side by side: "Quote the passage that states it most plainly … a help page or an API reference over a title or a list entry" (line 82), then "Write first the passage that shows the strongest placement" (line 83).
  - **S2-R2** (line 369): "this stage reads only the cells that hold nothing. A passage that would correct a cell already held is noted, not placed, and the final review reads those notes. *What it risks:* such a correction waits for the final review, which reads by risk …".
    - Its scope: 1,215 cells are held. 85 of them hold only `shows` or no placement that counts (`placed_as` `not-stated`: BigCommerce 20, Salla 12, Shopify 8, WooCommerce 29, Zid 16), and this stage never searches them. A passage for one is noted only if an agent meets it while reading another cell.
    - Decision 7 has the notes read at the final review. Decision 1 has the leads naming held cells go to its selection by risk. The plain words say both.
    - A miss's `found` row lands on the capability decided, held or not. That is the one place the stage adds to held cells.
    - The qualities the selection sends here for held cells fall out of the stage (S2I-19).
- *Fix:*
  - S2-R1's risk: add "and the limits, fees, prices, providers and the platform's own terms that only a later passage states aren't collected". Make the rule "a support value, a scope, a quality or a slot filler not shown yet".
  - The brief's line 82: "the strongest placement first; among passages of one placement, the plainest".
  - S2-R2's plain words: "This stage doesn't search the 1,215 cells already held, among them 85 that hold only a mention (`shows`) or no placement that counts, whose count a held page could raise. A passage met by chance is noted for the final review, whose selection takes it by risk. Q3's misses are the exception: their passages land on the capability decided, held or not. Shopify's compliance reports, sent here for held cells' qualities, aren't read."

**S2I-22. A correction batch updates `s2-captures.tsv` but not `s2-outcomes.tsv` or the model, and nothing says which capture leads are new.**
- *Found* (a copy, after `S2-ZD` was applied; `S2-ZD-1`'s rows corrected, `S2-ZD-2` added, then `land --batch S2-ZD-R1` and `apply`):
  - Outcome rows are compared by part, subject and outcome alone (line 1048). CM-CAT-016's corrected capture ("…, corrected") reached `s2-captures.tsv`, which `land` rewrites whole for the platform (line 1156). `s2-outcomes.tsv` kept the old capture, and so did the cell's reading in the model.
  - `s2-captures.tsv` held 4 leads, no duplicate, and has no batch column (`CAPTURES_HEAD`, line 88). The coordinator can't tell which leads arrived since its last handoff.
  - CM-CHK-012, corrected from `not-found` to `found`, kept its `not-found` row (batch `S2-ZD`) in `s2-outcomes.tsv`. That is the file the omission review samples. A reading: it would sample a row the model no longer holds.
- *Fix:*
  - Compare an outcome row whole. A changed one lands in the correction batch, and `apply` replaces that cell's sentence (it knows the reference, `ref + ")"`).
  - Add `batch` to `s2-captures.tsv`: the batch in which the lead first landed.
  - Drop, or mark `superseded`, the `s2-outcomes.tsv` row of a subject a later batch finds.

**S2I-23. On an id collision after a batch is applied, a new passage can take the applied passage's id, silently.**
- *Found:*
  - `passage_id` lengthens an id only where `entries.tsv` holds it, or where this run's `taken` gives it to another passage (lines 967 to 979). `taken` starts empty on each run (line 1041), so `entries-s2.tsv`'s existing ids aren't in it. The design: "On a collision with an id of `entries.tsv` or `entries-s2.tsv` that names another passage, it is lengthened" (section 3.2).
  - Tested on a copy, with `sha1` wrapped to force one 8-digit collision and the tool's code unchanged. After `S2-ZD` was landed and applied, a correction row above the low-stock row took `ZD-E-c2c81d02`, and the applied passage became `ZD-E-c2c81d024f`. `entries-s2.tsv` now says `ZD-E-c2c81d02` is 'Enable reorder feature'. `placements-S2-ZD.tsv` and the model's evidence still cite it on CM-INV-004.
  - `held_entries.py check --batch S2-ZD-R1` gave 0 problems ("CM-INV-004@zid … becomes held", a second line for the same passage). Only a check of the applied batch shows it: "term 'Low stock' is not in the text of each of its entries".
  - An assumption, from the birthday bound: with about a thousand entries a platform, a collision in a correction batch is near one in 10,000. When it happens, the page shows another passage under a cell.
  - `held_entries.cited_text()` finds entry ids with `\b[A-Z]{2}-E-[0-9a-f]{8}\b` (line 1575), so a lengthened id in a reading isn't read. The design says `cited_text()` takes the form "as it is".
- *Fix:*
  - Seed `taken` from `entries-s2.tsv`, each id with its passage (repository and path without the commit, locator, folded text), before the rows are read.
  - Refuse a landing that would give an id named in an applied batch to another passage.
  - Make `cited_text()`'s pattern `[0-9a-f]{8,40}`.

**S2I-24. The Knowledge Map's page gives the second stage's citations of this repository no link, and its fixed line for a cell holding nothing contradicts the reading the second stage writes.**
- *Found* (`km_page.py` on the amended copy, its merged files committed in a scratch repository):
  - `source()` links `sharrwah-knowledge-map:<path>` but not `sharrwah-knowledge-map@<commit>:<path>` (`km_page.py` line 55), the only form the brief allows. In the page's data, `ZD-E-9e7d3ce8`, the Zid help page, has the label `sharrwah-knowledge-map@3d0f032f6:…/183-help.zid.sa/text.txt line 98` and an empty link, where `ZD-E-c2c81d02` links to other-product-class's blob at `#L827`.
  - A cell holding nothing always shows "Nothing held: the part searched the concern map for this capability on Zid and found nothing that shows it." (template line 353), with "Searched" and the reading under it. After the second stage the reading says, for CM-CAT-016: "The held pass's second stage (S2-ZD) read the held pages at other-product-class@0d79b794f, sharrwah-knowledge-map@3d0f032f6 (held/zid/s2/S2-ZD-1.tsv line 7): not held: the place that would state it isn't held; capture: other-product-class; demo_entry; …; stop at any save; needs: nothing. It read: zid/GAPS.md row 18; …".
    - For an `unclear` cell (CM-TRU-006) the reading quotes the passage that may show it, under "found nothing that shows it".
    - For an `absent` cell (CM-PAY-008): "absent from a complete list the platform publishes, from ZD-E-c4c22f6b, …". The coordinator's decision 2 allows that.
    - "Searched" now mixes the concern map's terms with the held pages' (S2I-10).
  - `apply` copies the whole `read` into the sentence, unclipped (`held_amend.py` line 203).
- *Fix:*
  - In `source()`: match `sharrwah-knowledge-map(?:@([0-9a-f]+))?:(.+)`, linking at its own commit, with `#L<n>`.
  - In the template: where the cell's reading holds "The held pass's second stage", say "Nothing held: the concern map holds nothing for it, and the held pass's second stage read the held pages (its reading says what it found)".
  - In `outcome_sentence()`: clip `read` to about 200 characters, and leave the capture's raw form in `s2-outcomes.tsv`, writing "capture requested" instead.

**S2I-25. `found` is defined as "states that your platform has the thing", while its supports include a third party doing it.**
- *Found:* line 82 defines `found` as "a held passage states that your platform has the thing". Line 83 orders its supports, `extension-point` and `outside` among them. B-extent's `outside`: "the statement names a third party, not the merchant, the buyer or the platform's company, as the one that does it". A reading: one agent writes `found` with `outside` for a third party's own service; another writes `not-found`, since the platform doesn't have it.
- *Fix:* "`found`: a held passage states the thing on your platform, in any of B-extent's values: the platform does it, its company's service does it, third parties do it through the platform, or a third party does it outside it, or the platform names it (`shows`)."

---

## Notes

- **S2I-26.** `cells --left` lists only the cells with no row (line 464), not a miss's parts. A fresh agent continuing a part wouldn't see which parts of its misses are left. Add them, as `M-nn: <part>`.
- **S2I-27.** `corpus_search.py` prints this repository's `HEAD` (line 292), which moved nine times during this inspection. The checker refuses it with a clear message ("sharrwah-knowledge-map@02932549… is not a commit allowed here: the run fixed sharrwah-knowledge-map@3d0f032f6"). The brief could say so in "Sources and locators": "corpus_search prints the current commit: write the one your message names."
- **S2I-28.** `PLAN.md`, section 3: "A rule it adds is marked as a ruling and listed for the founder's veto." The brief marks S2-R1 and S2-R2. It doesn't mark the rules the design lists for veto, or others the brief adds:
  - `not-held`'s three cases;
  - `unclear`;
  - `could_change`'s values;
  - "A cell's rows are one or more `found` rows, or exactly one row of another outcome";
  - the misses' parts, which are in the tool only.
- **S2I-29.** `held_amend.py` prints "check it with python3 -I method/check_class_part.py <part>". `check_class_part.py` takes the part's path (its usage: `studies/class-model/parts/<domain>-<part>`), and with the name alone it failed ("No such file or directory: 'A-zid/derived.tsv'"). The message predates this stage (`0b5a37d0`).
- **S2I-30.** A cell that a correction batch makes held loses the earlier batch's outcome sentence and the concern map's reading. `apply` writes "Nothing in the concern map; …" over a cell holding nothing (`held_amend.py` line 271), as the held pass did. CM-CHK-012 on the copy: "Nothing in the concern map; the held pass's second stage (S2-ZD-R1) adds 1 shows …". The record of what was searched, at which commit, stays in `s2-outcomes.tsv` (S2I-22).
- **S2I-31.** `held_amend.py`'s `searched` for a cell holding nothing keeps its pieces' language prefixes (`en: payment terms`), while the second stage's terms come bare. So 'payment terms' was added beside 'en: payment terms' on CM-PAY-008. It is harmless, and the cell's list grows.
- **S2I-32.** For the record: the brief's guide sizes are right (observed-sh 53,247 characters, observed-sa 49,855, Zid 20,624, BigCommerce 18,953, WooCommerce 18,011). The part list matches the brief: 620 cells in 9 parts, 56, 51 and 35, 62 and 76, 75 and 86, 97 and 82.

---

## What I ran

All from `/home/user/sharrwah-knowledge-map`, with `python3 -I`. Everything that writes ran on copies of `studies/class-model` in `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/S2-inspect/` (`studies/class-model`, `before/`, `colA/`, `colB/`), with `CLASS_MODEL_DIR` set and `studies/concern-map` linked beside each.

**The agents' side, on the real model (read only):**
- `s2_held.py parts`; `leads --part P` and `leads --part P --held`, `cells --part P` and `misses --part P` for all nine parts. The outputs are in `…/S2-inspect/out/`.
- A count over the `cells` outputs: the cells with a Q3 row or a point, by result, and by kind.
- `corpus_search.py` on Zid (`"3D Secure" "cookie" "ملفات تعريف الارتباط" "إكرامية" "بقشيش" "tip"`, and `"suited to the Syrian market"`) and on BigCommerce (`"date format" "decimal separator" "thousands separator"`), all with `--brief`.
- `quote_check.py` and `quote_check.py --text` on captured pages (`text.txt`, `expanded.txt`, `raw`, `raw.html`, `rendered.html`), a Shopify HTML page, a Zid help page and a BigCommerce PDF save.
- `class_slice.py search` and `caps --terms`.

**The checker:**
- The baseline is `…/S2-inspect/fx.py`.
- The 72 one-fault variants are `…/S2-inspect/variants.py`, with their results in `…/S2-inspect/out/variants.txt`.
- The markup cases are `…/S2-inspect/markup.py`, with their results in `…/S2-inspect/out/markup.txt`.

**The coordinator's side:**
- On the copy:
  - `check-misses`, `mark`, `land --dry-run` and `land`;
  - `held_entries.py check --batch S2-ZD`;
  - `held_amend.py plan` and `apply --batch S2-ZD`;
  - `check_class_part.py` on A-zid, B-amend, B-zid, C-amend and C-zid, and the same on a fresh copy for the counts before;
  - `class_merge.py --complete` before and after;
  - then the correction: `land --batch S2-ZD-R1`, `held_entries.py check`, `plan` and `apply`, `check_class_part.py` on C-amend, D-backfill-bigcommerce and D-zid, and the merge.
- `misses-join --miss M-12`.
- A second landing compared by md5.
- The id collisions: `…/S2-inspect/collide.py A` (an id of `entries.tsv`) and `B` (a correction after an applied batch, `sha1` wrapped for one forced collision).
- A miss decided against its proposal, and two rows giving one passage two supports, each landed on `colA`.
- `km_page.py --out …/S2-inspect/out/km.html` on the amended copy, its merged files committed in a scratch repository at `…/S2-inspect`, and its data read for three citations and one reading.

## What I didn't check

- I settled no cell and no miss. The evidence quoted shows what the brief's steps meet, not any row's answer.
- I ran no agent on the brief, so its cost per row is not measured.
- I didn't run a Shopify or Salla search, nor `--runs-only`, `held_index.py` or `schema_type.py`. The Shopify and Salla tests read their files directly.
- I didn't check that each miss's parts cut its thing completely, beyond the three in S2I-16.
- I read B-extent's sections the brief names, H-held's rules 4 and 5 with its "Rules", output and notes, and `review-H-rulings.md`'s second-stage section and one ruling, not the rest. I didn't read `STATE.md`.
- I built the Knowledge Map's page and read its data, but didn't view it in a browser.
- The collision's likelihood in S2I-23 is an assumption.
