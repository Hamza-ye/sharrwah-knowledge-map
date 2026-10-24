# Check of the R3 briefs: recording and checking

**18 October 2026.** A check of `studies/proposals/briefs/R3-recording.md` and `studies/proposals/briefs/R3-checking.md` before they run (PLAN.md, step R2, item 2). Nothing here was run as a task.

**What was checked against.** The briefs are unchanged from commit 681df43 to 33464b9. PLAN.md changed during the check, at 7cc6c78: section 6 now gives agents their questions from `studies/proposals/questions-for-agents.md`, and section 11 names the sample as Q2 on Salla. This check reads PLAN.md as it now stands.

**What was run, outside the repository** (in the scratch directory):
- `copy_statements.py candidates` for Q2 on Salla, Q2 on Shopify, Q7 on Shopify and Q5 on Salla;
- `copy_statements.py copy` with every candidate copied, to size the copies;
- `check_proposals.py records` on those copies and on a small hand-made record;
- the corpus search on Salla, Shopify and WooCommerce;
- the quote checker on list and snippet quotes;
- `page_text.mjs` and curl on one live page.

## What a run starts from

- **Q2 on Salla, the sample:** 53 candidate concerns holding 543 statements and 91 gaps. The file is 12.5 KB, small enough to judge by its terms.
  - Some concerns plainly don't bear on Q2: customers, reviews, Salla Chat, the App Maker policy.
  - Most do, because Q2 asks about "its own choice of partners and providers". One example is SA-C-065, address lookup through Google Maps, HERE, LocationIQ and Nominatim.
  - Five rows have no terms: SA-C-114, SA-C-164, SA-C-231, SA-C-233 and SA-C-235. These are the ones whose descriptions repeat Q2's own words: licences, settlement currency, where data is stored, a partner that is unavailable. SA-C-233 also has no statements.
- **Q7 on Shopify:** 27 candidates holding 396 statements and 32 gaps. Most bear on Q7, such as Markets and store currency. A few plainly don't, such as disputes (SH-C-072) and Shopify Protect (SH-C-073).
- **Q2 on Shopify:** 80 candidates holding 1,105 statements and 91 gaps.
- **Q5:** 97 candidates and 1,242 statements on Shopify. On Salla, 67 candidates and 1,139 statements, plus the pilot's 202.
- **Size of the copies,** with every candidate copied (copied.tsv, copied-citations.tsv and copied-gaps.tsv). Tokens are estimated at 4 characters a token for Latin text and 2.5 for Arabic.

  | Run | copied.tsv | copied-citations.tsv | copied-gaps.tsv | Total |
  | --- | --- | --- | --- | --- |
  | Q2 on Salla | 254 KB | 225 KB | 86 KB | about 135k tokens |
  | Q2 on Shopify | 442 KB | 438 KB | 71 KB | about 237k tokens |
  | Q5 on Salla | 550 KB | 635 KB | 98 KB | about 335k tokens, with the pilot's copies (107 KB) |

## Findings

### Anything that presupposes the answer

**1. The brief hands agents the founder's items and expectations.**
- **Where:** recording brief, "Read only", second item (line 14). The checking brief inherits it.
- **Problem:** the brief points to `studies/proposals/questions.md`, "its own section". That section holds the question, and also the founder's item and notes on what the question carries.
- **Evidence:**
  - **The sample:** Q2's section opens "The founder's item: B2, 'rules land as availability, not as design'" (line 30).
  - **Other questions:**
    - Q1: "one platform, set up per market" (line 20).
    - Q4: "selling without Sharrwah touching the money" (line 44).
    - Q5: "Sharrwah chooses which payment methods are offered" (line 52), and the pilot's Decisions (lines 60 to 65).
    - Q7 states the expected answer: "The founder expects one store currency to be the platforms' norm" (line 79).
    - The file's opening points to `founder-messages/` (line 5), and Q8's section to `sizing.md` (line 89).
  - **The plan:** PLAN.md section 6 (line 303) now says agents get the questions only from `questions-for-agents.md`. `method/agent_questions.py` writes that file without these lines.
  - **Numbering:** a run counting sentences across "its own section" may count the founder's item as a sentence. In-depth and checking runs would then number differently. Q1's fragment "And adding a currency, or a payment provider?" could also be folded into sentence 4 by one run and not by another.
- **Fix:**
  - Read the question from `studies/proposals/questions-for-agents.md`: its section, and "How a run uses its question".
  - Add `founder-messages/` and `founder-decisions.tsv` to "Don't open".
  - Optionally, have `agent_questions.py` print each sentence with its number, so every run numbers alike.
- **Severity:** must fix.

**2. The examples of levels and scopes name "market".**
- **Where:**
  - recording brief, step 4 (line 66): "the levels its settings are set at, such as a store, a market, a plan or an account";
  - rule 3 (line 74): "a store, plan, country, market or role".
- **Problem:** "market" is the founder's working word for B1 ("set up per market"). It is also Shopify's own term (SH-C-106, "Markets; Shopify Markets").
  - The examples hand every platform a ready-made level.
  - For Q1 ("where is it set and by whom") and Q7 ("At what level does the platform set each"), they suggest the answer.
- **Evidence:**
  - questions.md's wording rule (line 9) names exactly these four as what a question never fixes: "It never says where something is set (a store, a market, an account, a plan)".
  - PLAN.md section 6 (line 305) says "'Per market' in the founder's section B is a working description, not a fixed level".
- **Fix:**
  - **Step 4:** "the levels its settings are set at, each named as the platform names it".
  - **Rule 3:** "A statement holds where the platform says it holds. Record that scope in the source's words, and leave it empty when the statement is general."
  - Give no list of examples in either.
- **Severity:** must fix.

**3. The concern map's own words reach the agent unmarked.**
- **Where:** recording brief, step 1 (line 58) and step 2 (line 60); the files the copy writes.
- **Problem:** the brief warns that `selection.tsv`'s description is the concern map's words, but only for judging. Other categories of ours reach the agent without any warning:
  - the copies' `placement` and `structure` values;
  - the copied gaps' wording.
- **Evidence:**
  - Q2 on Salla's descriptions include "Taxes per market" (SA-C-160) and "Markets: per-country versions of a store" (SA-C-165).
  - Copied rows carry `placement` values such as `decides` and `responsible`.
  - The gaps read "says who answers for it" and "is placed and controlled as it is".
  - For Q5 ("Who decides…"), a copy marked `decides` invites an account point that the statement itself doesn't make.
- **Fix:** add to rule 1: "The concern map's descriptions, the copies' `placement` and `structure` values, and the copied gaps' wording are ours, not the platform's. Never use them in a statement, identifier, scope, note or the account."
- **Severity:** optional.

**4. One account section per sentence turns Q3's examples into the account's frame.**
- **Where:** recording brief, `account.md` (line 123): "one for each sentence of the question".
- **Problem:** some sentences ask nothing. One section for each would build the account on them.
  - Q3's sentence 2 is only examples: "opening the store to buyers, taking payments, receiving payouts, or selling particular products". Its section would be organized around those four examples.
  - Q3's sentence 3 only limits the question, so its section has nothing to hold.
- **Evidence:** `questions-for-agents.md`, Q3 (line 24).
- **Fix:** "one section for each sentence that asks something. A sentence that only gives examples or limits the question has no section of its own: its points go under the sentence it serves."
- **Severity:** optional.

### Whether its agent can do it

**5. The selection asks the agent to judge by statements it can't see.**
- **Where:** recording brief, step 1 (line 58): "Judge by the terms and, where you need to, by the concern's statements."
- **Problem:** the concern's statements can't be read before the copy.
  - They sit in the concern map's `statements.tsv`, which is outside "Read only" (line 17 names only `concerns.tsv`) and under "Don't open" (line 47).
  - `copied.tsv` exists only after the copy, and the copy refuses while any row is still `candidate` (`copy_statements.py`, lines 116 to 125).
  - The only way round is to copy everything, read it, set rows aside and copy again. That reads every candidate's statements and renumbers the copies (finding 8).
- **Evidence:** for Q2 on Salla, the five rows with no terms (see "What a run starts from") can only be judged by statements or by the concern map's description.
- **Fix:** have `copy_statements.py candidates` also write `candidates.tsv`, with each candidate concern's `identifier` and `statement`, for the rows whose terms don't decide it. Add it to "Read only", and say: "Set every row before you copy. Copy once."
- **Severity:** must fix.

**6. Copied gaps can't be cited, and mustn't be recorded again.**
- **Where:**
  - recording brief, step 2 (line 60), rule 9 (line 93) and `account.md` (line 124);
  - `copy_statements.py`, lines 136 and 137;
  - `check_proposals.py`, line 233.
- **Problem:** the rules give no way to bring an open copied gap into the account.
  - Copied gaps carry no id: `copied-gaps.tsv` has `source_file`, `source_line`, then the gap's columns.
  - The account may cite only K, P, statement and N ids.
  - Rule 9 says not to record again what a copy says.
  - So a copied gap that is still open, and bears on the question, either can't reach the account, or is recorded again as a new not-found with fresh corpus searches.
  - The same holds for Q5's pilot gaps and absences (line 16).
- **Evidence:** the account pattern in `check_proposals.py` is `K\d{4}|P\d{4}|N\d{2}|\d{3}`.
- **Fix:** give copied gaps ids (`Q2-SA-G…`, numbered as in finding 8), and copy Q5's pilot gaps and absences the same way. Have the checker accept G ids. Say: "A copied gap that is still open and bears on a sentence is cited by its G id. Record a not-found only for what no copied gap covers."
- **Severity:** must fix.

**7. The checker rejects unchanged copies.**
- **Where:** `check_proposals.py`. `read()` strips every field (line 70). `check_copies` compares the joined, stripped fields with the source line (lines 118 to 123).
- **Problem:** a field that starts or ends with a space fails the comparison, so an unchanged copy is reported as changed. "Fix what it reports" (line 130) then can't be done without editing a copy.
- **Evidence:**
  - Five Salla statements start or end with a space or a no-break space: `statements.tsv` lines 958, 1184, 1553, 1883 and 2312.
  - With every candidate copied, the checker reported "not unchanged from … line 1553" for Q2-SA-K0221. For Q5 on Salla it reported the same for K0451, K0669, K0992 and K1128.
  - Every Salla question's candidates hold at least one of the five rows.
  - Line 1553 is under SA-C-111 (e-payments balance and payouts), which the sample is likely to copy.
- **Fix:** compare copies without stripping. Take the copied file's raw line, drop its first three fields (two for gaps), and compare with the raw source line. Then re-run the check on the copies of all Salla candidates.
- **Severity:** must fix.

**8. Copy ids change when the selection changes, and the checker doesn't notice.**
- **Where:** `copy_statements.py`, line 131: copies are numbered in order. Recording brief, step 1 (an `add` row) and line 128 ("the next run continues from them").
- **Problem:** after any change to the selection and a fresh copy, every later id names another statement.
  - This happens when a run adds a concern after reading, when it takes finding 5's way round, or when a run continues another run's files.
  - Account points and rule 9 notes that cite K ids then point at the wrong statements.
- **Evidence:**
  - In scratch, Q7-SH-K0100 was `statements.tsv` line 1320 ("Subscription Fees are paid in advance…").
  - After one concern was set aside and the copy run again, Q7-SH-K0100 was line 1333 ("Transaction fees vary…").
  - An account citing Q7-SH-K0100 passed the checker with "no issues".
- **Fix:** number each copy by its source line, such as `Q2-SA-K1553`. The largest `statements.tsv` (Shopify's) has 3,006 lines, so `K\d{4}` still fits. Do the same for pilot P ids and gap G ids.
- **Severity:** must fix.

**9. "Held: none" for Zid and BigCommerce sends those runs to live pages.**
- **Where:** recording brief, the platform table (lines 24 to 26).
- **Problem:** the table says nothing is held for Zid or BigCommerce, and lists only the release files for WooCommerce.
  - This repository's capture runs hold their pages. The corpus search reads them, and so does `held_index.py`.
  - PLAN.md step R3 says held material comes first.
  - A run following the table reads live instead. On zid.sa a live render can return an empty shell where the held raw page has the text (`corpus_search.py`, lines 217 and 218).
  - The brief doesn't say how to cite a held capture.
- **Evidence:** the manifests in `evidence/product-class/runs/` hold these pages, captured with their text:

  | Platform | Pages captured | Also held |
  | --- | --- | --- |
  | Zid | 209 | |
  | BigCommerce | 212 | the founder's saves under `evidence/product-class/blocked-evidence-founder/bigcommerce/` |
  | WooCommerce | 119, from woocommerce.com, wordpress.org and woo.com | the release files |

- **Fix:**
  - **Zid, BigCommerce and WooCommerce:** list as held "the pages in this repository's capture runs, found by the corpus search and `held_index.py`". For BigCommerce, add the founder's saves.
  - **Citing:** "Cite a captured page by its URL. The checker finds it in the capture."
- **Severity:** must fix.

**10. The corpus search doesn't search WooCommerce's release.**
- **Where:** recording brief, Tools (line 39): "to search everything held for your platform … run `corpus_search.py`"; rule 7.
- **Problem:** for WooCommerce, the search reads only capture runs and the founder's saves. Its held corpora (`corpus_search.py`, lines 34 to 43) cover Salla and Shopify only.
  - A WooCommerce not-found would therefore be recorded without the platform's code ever being searched.
- **Evidence:**
  - `corpus_search.py woocommerce WC_Gateway_COD "Cash on delivery"` found one captured page.
  - `grep -rl WC_Gateway_COD` over the release finds it in 14 files, among them `includes/gateways/cod/class-wc-gateway-cod.php`.
- **Fix:** add the release folder, with its language files, to the search's held corpora for WooCommerce. Until then, have WooCommerce runs also run `grep -rIl -i` over `/home/user/woocommerce-release/11.2.1/woocommerce`, from outside it, and give that command in `searched`.
- **Severity:** must fix.

**11. Step 4 asks for contracts that "Read only" doesn't allow.**
- **Where:** recording brief, step 4 (line 66): "the contracts behind its providers"; "Read only" (line 18): the platform's own material, including any agreement its terms incorporate.
- **Problem:** many providers' contracts aren't incorporated into the platform's terms. A Salla seller's contract with Tabby, Tamara, Moyasar or HyperPay (SA-C-118, SA-C-120) is one example.
  - Step 4 asks for those contracts; "Read only" excludes them.
  - The run either breaks its reading list, reading long legal texts, or can't do the step.
- **Fix:** "Record the contracts behind its providers as your platform's material shows them: what it says of them, and any agreement its terms incorporate or name as binding on the seller, which you may read. Don't read a provider's own terms otherwise. Where your platform names one, record it as not in what was read, with its address."
- **Severity:** must fix.

**12. Rule 12 stops a run before its account.**
- **Where:** recording brief, rule 12 (line 98); Output; "Before you finish" (line 130).
- **Problem:** a run that stops at 120 new statements has no account, and the checker reports it missing. If the sample hits the cap, it is a cut-short run, not a typical one.
- **Fix:** "Once you pass 120 new statements, stop reading. Write the account from what is recorded, list in `notes.md` what you didn't read, run the checker, and report."
- **Severity:** optional.

**13. A list passes the checker only with the source's own markers.**
- **Where:** recording brief, rule 5 (lines 76 to 79); quotes "within one paragraph of the source" (line 102).
- **Problem:** the checker strips Markdown links but keeps list markers.
  - A list recorded "in full, as one statement" therefore passes only if it keeps the source's `- ` markers.
  - "Each run of items" crosses list items, while a quote must stay within one paragraph.
- **Evidence:** on the held page `md/en/manual/payments/shopify-payments/supported-countries.md`, three versions of the same list were checked:

  | Statement | Result |
  | --- | --- |
  | "Shopify Payments for Australia Shopify Payments for Austria …" | not found |
  | the same, joined with semicolons | not found |
  | "- Shopify Payments for Australia - Shopify Payments for Austria …" | found |

- **Fix:** "A list's statement is the source's text from its first item to its last, on one line, keeping the source's own markers, such as `- `. A quote may run over consecutive items of one list."
- **Severity:** optional.

**14. Snippets from the corpus search aren't quotable.**
- **Where:** recording brief, Tools and rule 7. `corpus_search.py`, line 271, prints snippets from folded text.
- **Problem:** folding changes case and diacritics, and the alef, ta marbuta and alef maqsura forms. A quote copied from a snippet fails the check.
- **Evidence:** the snippet "الرسوم وفق عقد خدمات الدفع الموقع اثناء التوثيق" was "not found". With "أثناء" restored, it was found.
- **Fix:** "The corpus search folds its snippets for matching. Never quote one: quote the document."
- **Severity:** optional.

**15. The checker accepts what the brief forbids.**
- **Where:** `check_proposals.py`, lines 227 to 241 and 86 to 98.
- **Problem:**
  - **Account points:** only bullet lines are checked for an id, and only as a warning. A prose point with no id passes silently. So does an account without one section per sentence.
  - **Selection:** a deleted candidate row isn't noticed.
  - **Not-found rows:** a `read` that names only an index or a sitemap passes.
  - **Statements:** `bears_on` numbers aren't checked against the question's sentences, and `scope` and `marker` aren't checked against the quote.
- **Evidence:** in a hand-made record, a prose line without an id raised nothing. A bullet citing only another platform's id raised a warning.
- **Fix:**
  - Check each account paragraph for an id, and the section headings against the question's sentences.
  - Compare `selection.tsv`'s concerns with a fresh `candidates` run.
  - Check `bears_on` against the number of sentences.
- **Severity:** optional.

**16. Live pages are cited before they are captured, in a language the capture may not match.**
- **Where:** recording brief, live sources (line 104). PLAN.md section 6 (line 317): "A page read new is captured and committed before it is cited."
- **Problem:** the run cites live pages that the coordinator captures only after the run. Until then the checker passes their quotes as "pending capture".
  - `page_text.mjs` reads with `Accept-Language: en,ar;q=0.8`. Capture runs default to `ar,en;q=0.8`.
  - The capture README warns that "a quote is only found in a capture made in the language the reader saw".
  - The brief doesn't say where working copies go.
- **Fix:**
  - Record by a dated section 11 entry that R3's live pages are captured after each run, and before any proposal cites them.
  - Have the run list in `notes.md` each live URL it read, with the language it was served in, so the capture matches.
  - Have working copies written outside the repository.
- **Severity:** optional.

**17. A page held but not readable has no instruction.**
- **Where:** recording brief, rule 8 (line 91). PLAN.md section 6: "if it is held but not readable, the reader is extended".
- **Problem:** the brief covers only pages that are held and readable. A run would route a held page that can't be read (such as `cdx-only`) to the founder. The checker flags only readable holdings.
- **Fix:** "If `held_index.py` shows it held but not readable, don't route it to the founder. Record `who_can` = `agent`, with route 'held, not readable: <location>', and say so in `notes.md`."
- **Severity:** optional.

**18. "Scope" means two things.**
- **Where:** recording brief, rule 1 (line 72), "a key, scope, route", and rule 3, "Scope".
- **Problem:** in rule 1 it means an API access scope, an identifier. In rule 3 it means where a statement holds. An access scope may land in the `scope` column.
- **Fix:** in rule 1, say "access scope".
- **Severity:** optional.

### Whether it is short

**19. Reading the copies would cost more than the rest of the run.**
- **Where:** recording brief, step 2 (line 60): "Read the copies". The checking brief inherits it.
- **Problem:** the step sets no bound, and the three copied files are large (table in "What a run starts from").
  - For the sample (Q2 on Salla) they come to about 135k tokens. For Q2 on Shopify, about 237k; for Q5 on Salla, about 335k.
  - `method/count_tokens.py` counts cache reads. Its docstring says a run's tokens are "mostly its context read again on each turn".
  - So copies read whole at the start are re-read on every later request. At 135k tokens over 100 requests, that is about 13.5M tokens. That equals the pilot's cost for 26 statements (at 0.52M each), spent on copies the run doesn't record.
  - Copies of that size also nearly fill the context.
  - Checking runs record at most 60 statements, so the copies' share of their cost per statement is larger still.
- **Fix:** rewrite step 2.
  1. Read only `copy_id`, `concern_id` and `identifier` of `copied.tsv`: about 7k tokens for Q2 on Salla.
  2. Read the copied gaps only of concerns that bear on a sentence.
  3. Before recording a statement, grep `copied.tsv` for a distinctive phrase of it.
  4. When you write the account, read `copy_id`, `identifier`, `statement` and `scope` once: about 31k tokens for Q2 on Salla.
  5. Open `copied-citations.tsv` only by `cite_id`.

  Better still, have the copy write these two views as files.
- **Severity:** must fix.

**20. The help maps can't be read as told.**
- **Where:** recording brief, "Your platform's own map of its help" (lines 28 to 36): "Find in the map the sections and pages … and read those pages."
- **Problem:** the maps are too large to read whole, and the brief sets no bound on how many pages to read.
- **Evidence:**

  | Map | Size |
  | --- | --- |
  | Shopify's `outline.md` | 13,275 lines (1.24 MB); its Payments menu alone is 1,718 lines (176 KB), linking 320 pages |
  | Shopify's `pages.jsonl` | 8.7 MB |
  | Shopify's `ar/pages.jsonl` | 8.3 MB |
  | Salla's `help-tree/{en,ar}/items.jsonl` | 47 categories each (28 to 35 KB): readable |
  | Salla's `help-articles/{en,ar}/items.jsonl`, the step from a category to its articles | 6.0 MB (1,280 rows) and 8.7 MB (1,658 rows) |

  The sample, on Salla, won't meet Shopify's outline. Unless Shopify runs are bounded the same way, the sample's cost per new statement will understate theirs.
- **Fix:**
  - **Shopify:** list the outline's 44 menu entries with their line numbers (`grep -n '^- \['`). For each menu chosen, print only its page lines, titles and addresses: those matching `](md/` between its line and the next entry's.
  - **Salla:** read `help-tree`. Then list a chosen category's articles, with only their address and title, by filtering `items.jsonl` on `section_id`.
  - A small script for both would keep it to one command.
  - Bound the pages read as in finding 21.
- **Severity:** must fix.

**21. Nothing bounds the reading.**
- **Where:** recording brief, steps 3 and 4. Rule 12 is the only stop.
- **Problem:** `questions-for-agents.md` (line 6) says "How far it reads, in what order, and when it stops are set by its brief". The brief sets the order. It sets neither how far the run reads nor when its reading stops.
  - With 543 statements already copied for Q2 on Salla, much of what is read adds nothing new, and the run keeps reading.
  - Step 4's "go deep" carries no limit either. PLAN.md step R3 (line 217) limits depth to "money flows, legal structure, the data model, and partner contracts". The brief drops that limit.
- **Fix:** "For each sentence, read the pages your platform's map files it under, at most 10, chosen by title. Then run one corpus search in your platform's words, and read at most 5 of the documents it lists. Stop reading for a sentence sooner when 5 pages in a row add nothing new. Read each page in one of its languages, and open the other only to quote. Step 4's structure and contracts apply only where the sentence concerns money flows, legal structure, the data model or partner contracts." The coordinator can tune the numbers.
- **Severity:** must fix.

**22. Closing copied gaps has no bound, and follows the concern map's questions.**
- **Where:** recording brief, step 2 (line 60): "You may close it by reading."
- **Problem:** most copied gaps ask the concern map's questions, not the run's. The brief invites the run to close any of them.
- **Evidence:**
  - Q2 on Salla's 91 copied gaps are 37 `reason`, 29 `responsible`, 9 `decides`, 7 `where` and 9 `boundary`.
  - 87 of them are "page not read", for the agent.
  - An example: "A clause of Salla's usage agreement (اتفاقية الاستخدام) that names Customers (Customers / العملاء) and says who answers for it".
- **Fix:** "Close a copied gap only where it bears on a sentence of your question, from pages you read for that sentence. The statement that closes it names the gap's id in `note` (finding 6). Don't read for a gap otherwise."
- **Severity:** must fix.

**23. Each not-found carries searches with no limit.**
- **Where:** recording brief, rule 7 (lines 85 to 89): search "with each country, plan or arrangement your statements name", then "Read each listed document that could show it".
- **Problem:** every search is a request, and its output stays in context. Rule 7 sets no limit on how many searches a not-found needs, or how many listed documents must be read.
- **Evidence:**
  - Searches take time: 57 seconds for "sanctions" on Shopify, 19 seconds for one Salla term.
  - Output is large. A two-term Salla search ("العملة", "currency") printed about 100 KB and listed 173 documents. It matched 34 Arabic and 39 English help articles, 55 dashboard translation files, 370 archive documents (40 listed) and 5 captures.
  - A Q2 run on Shopify will name dozens of countries. The held supported-countries page alone lists 41.
- **Fix:**
  - **For each not-found:** run one search with the platform's words for what is missing, in each language, as alternatives in one call, with `--max 10`. Run one more with the place or plan the row is about. Read at most the 5 listed documents whose title or snippet could show it, and list the rest as not read in `searched`.
  - **The tool:** give the corpus search a required-term option, so one call can search the missing thing with any of the places, plans and arrangements named.
  - **The plan:** if this narrows PLAN.md section 6's "by each country, plan and arrangement it names", record that by a dated entry.
- **Severity:** must fix.

**24. Q5's reading of the pilot's gaps has no bound.**
- **Where:** recording brief, "Read only", Q5 (line 16). The checking brief inherits it.
- **Problem:** Q5 runs read the pilot's `gaps.tsv` and `absence-audit.tsv` whole. For BigCommerce that is about 90k tokens, before any reading for Q5 itself.
- **Evidence:**

  | Platform | gaps.tsv | absence-audit.tsv |
  | --- | --- | --- |
  | BigCommerce | 210 KB | 150 KB |
  | Zid | 29 KB | 96 KB |
  | Salla | 22 KB | 49 KB |

  `absences.tsv` is 70 bytes to 1.2 KB.
- **Fix:** "Read `absences.tsv`. Read `gaps.tsv` only by grepping for the terms of the sentence you are reading for. Read `absence-audit.tsv` only for the absences you rely on."
- **Severity:** must fix.

### The checking brief

**25. Comparing is both forbidden and required.**
- **Where:** recording brief, line 9: "Don't … compare your platform with any other". Checking brief, line 29: "Everything else in the recording brief holds". Item 1 then asks for what differs.
- **Fix:** add to the checking brief: "The recording brief's 'compare with no other platform' holds, except that you sort what your platform shows against the accounts, as below. You don't rank, explain or judge a difference."
- **Severity:** must fix.

**26. "Differs", "the same" and "goes beyond" need a rule for when two things match.**
- **Where:** checking brief, item 1 (lines 11 to 14).
- **Problem:** "differs" presumes the agent knows that two platforms speak of "the same thing". "The same" lets it skip recording. Neither says how to tell.
  - PLAN.md section 6 (lines 328 to 334) allows a match only on one of four bases. It warns that names alone fail on synonyms and homonyms. The agent can't open PLAN.md (recording brief, line 48).
  - The accounts are in the in-depth platforms' terms. A checking run can carry those terms into its own identifiers, scopes and headings.
  - Item 1's examples name only level, setter, condition and place as ways to differ.
- **Evidence:** Shopify's Q7 candidates include "Markets; Shopify Markets" (SH-C-106). Salla's include "Markets / الأسواق المتعددة; Store Scopes" (SA-C-165). A Salla check against a Shopify account point on Markets would match on the name alone, which is the case PLAN.md's rule exists for.
- **Fix:** state the rule in the brief.
  - **The bases:** two things match only on the same term (a platform's own translation included), the same identifier, the same definition with both quoted, or the same role in the question's sentence, each shown in the platforms' own words.
  - **The same:** it matches on a basis, and your source says nothing else about its scope, level, setter, condition or place. Cite your own ids.
  - **Differs:** it matches on a basis, and your source says something else. Record it.
  - **Goes beyond:** it matches no account point on any basis. Record it.
  - **When unsure:** record it as "differs".
  - **Names:** name the point you compare against by its ids. Never use an in-depth platform's term in your statements, identifiers, scopes or headings.
  - **Item 1's examples:** keep them only with "or anything else your platform states differently".
- **Severity:** must fix.

**27. The reading rule can't find what "goes beyond", and follows the in-depth platforms' structure.**
- **Where:** checking brief, item 4 (line 19): reading "goes to what the copies don't show and the accounts suggest may differ"; recording brief, lines 28 to 36: start from the platform's own map of its help.
- **Problem:** what goes beyond is, by definition, what the accounts don't mention, so the accounts can't suggest it.
  - New reading for it is therefore excluded. It can only come from the copies.
  - The run's reading is built from the in-depth platforms' accounts, not from how its own platform files its help. That contradicts the recording brief's map guidance, which the checking brief inherits.
- **Fix:** "Read your platform's own map of its help for the question's topics, and list the titles of the pages it files there. Read the pages whose titles name something no account point names, and those an account point needs, at most a number the coordinator sets. Then, for each account point not yet matched, run one corpus search in your platform's words."
- **Severity:** must fix.

**28. The checking brief inherits "go deep" and the in-depth not-found rules.**
- **Where:** checking brief, line 29. It replaces only steps 1 to 3, rule 12 and the account.
- **Problem:** recording step 4 ("Go deep … contracts behind its providers") and step 5 ("Record what you don't find") still hold for checking runs. That contradicts PLAN.md step R3 ("checked only for anything that differs or goes beyond") and the brief's own "You needn't read everything on the question".
- **Fix:** "Step 4 doesn't apply. Step 5 records only an account point that your platform's reading doesn't show: one row for each point, with its corpus search, naming what is missing in plain words, not in the in-depth platform's term."
- **Severity:** must fix.

**29. The account's four labels can't all be written as defined.**
- **Where:** checking brief, items 1 and 6 (lines 14 and 21 to 27).
- **Problem:**
  - **"The same" needs an id it may not have.** It is cited "with the copy ids that show it". When reading, not a copy, shows the same, item 1 says the run "needn't record it again". It was never recorded for this platform, so the point has no id. The brief then excludes the point, and the checker warns.
  - **"Nothing found" mixes two outcomes.** It means "nothing found that differs, in what was read", with an `nf_id`. Nothing different means "the same"; nothing at all means not found.
  - **No not-found row can be written for "anything that differs".** It has no platform words to search (rule 7), and it would later be audited as if it were a fact about the platform (PLAN.md section 6, checks by risk).
  - **Some sentences need more than one label.** "Each section says one of these" leaves no room for a sentence with a difference and a match.
- **Fix:**
  - **Labels:** each section lists its points, each labelled `differs`, `goes beyond`, `the same` or `not in what was read`, with this platform's ids.
  - **The same, from reading:** "When your reading, not a copy, shows the same, record the statement and cite it. It counts toward the cap."
  - **Not found:** an account point your platform doesn't show gets a not-found row (finding 28).
  - Drop "nothing found".
- **Severity:** must fix.

**30. Opening the in-depth runs' statements has no limit.**
- **Where:** checking brief, item 2 (line 16): "Open their statements only where an account point is unclear."
- **Problem:** "unclear" has no limit, and an account written in another platform's terms is often unclear. In-depth accounts will mostly cite copy ids, which live in the in-depth folder's `copied.tsv`. For Q2 on Shopify, that file is about 110k tokens.
- **Fix:** "Where an account point is unclear, look up only the ids it cites, by grepping for each id, at most 10 for each account. Never open their sources."
- **Severity:** must fix.

**31. The checker can't tell a checking run from an in-depth run.**
- **Where:** `check_proposals.py`, line 240; checking brief, item 6.
- **Problem:** the checker warns only past 1,800 words, but the checking brief allows about 800. It doesn't check the labels either.
- **Fix:** give the checker a `--check` option: warn past 900 words, and check that each point carries one of the four labels.
- **Severity:** optional.

**32. Nothing says what to do if an in-depth account is missing or failed its check.**
- **Where:** checking brief, item 2.
- **Fix:** "If a named account is missing, or its folder fails the checker, stop and report."
- **Severity:** optional.

## Verdicts

**Count:** 32 findings: 21 must fix, 11 optional.

**The recording brief can run once its must-fix findings are fixed:** 1, 2, 5 to 11, and 19 to 24.
- Most are short edits to the brief.
- Five of them need small changes to three of the tools the brief names:
  - `copy_statements.py`: the selection's statements, ids for gaps, and stable copy ids (5, 6, 8);
  - `check_proposals.py`: G ids in the account (6), and the copy comparison (7);
  - `corpus_search.py`: WooCommerce's release (10).
- **Before the sample (Q2 on Salla):** 1, 2, 5, 6, 7, 8, 11, 19, 20 (Salla's part), 21, 22 and 23. Without them, the sample is steered by Q2's founder item and stopped by a false checker error. Its reading of copies, gaps and search results would also outweigh what it records.
- **Before the first Zid, BigCommerce, WooCommerce, Q5 or Shopify run:** 9, 10, 24 and Shopify's part of 20.
- **What the sample doesn't measure:** none of 9, 10, 24 or Shopify's map, so its cost per new statement carries over to those runs only if they are bounded the same way.

**The checking brief can run once its must-fix findings (25 to 30) are fixed,** with the recording brief's, which it inherits.
- Those fixes replace its core: what it reads, when something counts as the same, and what its account says.
- So the rewritten section should be read once more before the first checking run. Checking runs come after the in-depth runs, so this doesn't hold up the sample.
