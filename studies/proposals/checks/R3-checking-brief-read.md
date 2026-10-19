# Read of the R3 checking brief before its first run

**19 October 2026.** A read of `studies/proposals/briefs/R3-checking.md` before the first checking run, as its status line asks. It is read against `studies/proposals/briefs/R3-recording.md` as that brief now stands. The repository is at 7d4e86c, on branch `claude/vibrant-meitner-oh70v4`. Nothing was recorded into the repository: every output went to a scratch folder.

**What was read:**
- the two briefs and `studies/proposals/questions-for-agents.md`;
- the three checks of these briefs;
- the tools the briefs name, as far as needed;
- Q4's two in-depth accounts, with three of their ids looked up, as item 2 allows.

**What was run,** with `python3 -I -B`, so that no bytecode was written into `method/`:
- `copy_statements.py`: `candidates Q4 zid`; `show` for S-01 and five concerns; `copy`, with 14 concerns and S-01 set to copy;
- `check_proposals.py records`: on the Q4 folders of Shopify and Salla, and on 14 hand-made Zid records, with and without `--check`;
- `corpus_search.py`: Zid's search for the question's topics, one Zid search for sentence 3, and one Q4 search each on BigCommerce and WooCommerce;
- `held_index.py` on nine Zid addresses.

No live page was read. Item 6's route "with a map" wasn't tried, since Zid has no map.

## Q4 on Zid, step by step

Zid's ids below are those a Q4 copy gives, such as `Q4-ZD-K0110` for line 110 of Zid's `statements.tsv`. They are written without their `Q4-ZD-` prefix.

| Step | What happened | Findings |
| --- | --- | --- |
| Candidates | 34 concerns and S-01 (158 pilot statements, 19 gaps), in 6.4 KB. | |
| Selection | Judged by terms. `show zid S-01` lists 138 identifiers in 16 KB. Among them are cash on delivery and bank transfer (its lines 70, 72 to 76, 124 to 129, 142 and 150), so S-01 bears on Q4. No candidate is without statements. | 9 |
| Copy | 14 concerns and S-01: 119 K, 23 G, 158 P, 19 H and 4 A copies, in 0.05 seconds. | |
| Views | `copied-index.tsv` is 23.5 KB (about 5k tokens). `copied-view.tsv` is 106 KB (about 23k), 70% of it the pilot's. | 5 |
| Accounts | Shopify's has 34 points (6.4 KB) and Salla's 51 (11.2 KB), about 4.4k tokens together. Both folders pass the checker with "no issues", in 4 and 11 seconds. An id looked up returns about 1 KB. | 4, 6 |
| Bases and labels | Workable where both platforms name the thing the same way. See the cases below. | 4, 7, 8 |
| Reading | The topic search's ten listed documents are all API reference pages, 2.2 MB of text; the help centre comes 19th to 30th. Zid's terms, pricing and payments pages read as an error page. Zid's own name for the question's subject is found only with Shopify's term. | 1, 2, 3 |
| Not-found rows | 76 of the accounts' 85 points rest on statements or copies; 9 record what wasn't found. Each row carries its own searches. | 4, 11, 12 |
| Account | 800 words for the points sorted against 85. The checker counts the accounts' ids as words. | 13 |

**Cases of matching:**

| What Zid shows | Account point | Basis | Label |
| --- | --- | --- | --- |
| الدفع عند الاستلام / Cash on Delivery, turned on or off for each shipping company under لوحة التحكم > اللوجستيات (K0110, K0111, K0113) | Salla [1]: Q4-SA-P0098, K1530. Shopify [2]: Q4-SH-003, 004 | term | differs, from both |
| The bank details shown on the payment page, "مع إمكانية التحكم الكامل في عرض أو إخفاء التفاصيل" (K0124) | Salla [1]: Q4-SA-P0100, K1603, 021 | term (التحويل البنكي) | differs |
| Zid Ship collects cash on delivery for the merchant and pays it into the wallet, its fee deducted first (K0117, K0119, K0122) | Salla [5]: Q4-SA-P0041, P0042, P0039, P0093, K1587. Shopify [5]: Q4-SH-N01, a not-found | role | differs from Salla's. Nothing fits Shopify's (finding 4). |
| `unpaid` "includes `pending`, `refunded`, and `voided` statuses" (K0209) | Shopify [3]: Q4-SH-018, "غير مدفوع" covers authorized, pending, expired and partially paid | term, or a name alone (finding 7) | differs, or goes beyond |
| "Upload bank transfer receipt", under Reverse Orders (K0430) | Salla [3]: Q4-SA-015, the receipt of a payment; or Q4-SA-008 and 009, refunds by transfer | the term points to one, the role to the other (finding 7) | differs |
| تفعيل الدفع اليدوي, on help.zid.sa/orders-properties/ | Shopify [1] and [2]: manual payment methods. Salla [1]: Q4-SA-007 | role | differs. Found only with Shopify's term (finding 3). |
| nothing | Shopify [4]: Q4-SH-027, email money transfers in Canada only | none | not in what was read: one row |

## Findings

### Whether a checking run can do it

**1. Without a map, the searches list Zid's and BigCommerce's developer reference first, and some of those pages are megabytes long.**
- **Where:**
  - checking brief, item 6 (lines 36 and 37): "read at most 10 of the documents it lists" and "Read at most 5 of the documents it lists";
  - rule 7 (recording brief, lines 116 to 121);
  - recording brief, line 28: "read the text file it names";
  - `corpus_search.py` lists documents in the order it reads them (lines 320 to 332). For capture runs, that is each manifest's order (lines 245 to 262).
- **Problem:** the listing isn't by relevance.
  - Zid's and BigCommerce's captures list their developer reference before their help centres, so `--max 10` reaches only the reference.
  - Those pages are long. The brief bounds the reading of map files and release files (lines 30 and 41), not of captured pages.
- **Evidence:**
  - **Zid, the question's topics** (`"الدفع عند الاستلام" "التحويل البنكي" "تحويل بنكي" "Cash on Delivery" "Bank Transfer" "COD" --max 10`): 43 documents.
    - The 10 listed are all docs.zid.sa API pages, with 2.2 MB of text between them. One of them, `get-manager-profile.md`, is 1.7 MB.
    - The 12 help.zid.sa pages come 19th to 30th; help.zid.sa/cod/ is 22nd. zid.sa's 13 pages come last.
  - **Zid, sentence 3** (eight terms for marking an order paid, receipts and refunds): 144 documents. The first 10 are all API reference. They include the 1.7 MB page again, `list-of-orders.md` (301 KB) and `llms.txt` (95 KB).
  - **Zid's captures:** of 253 with text, 15 are over 50 KB and 9 over 100 KB.
  - **BigCommerce** (a Q4 search for offline and manual payments): 67 captured documents.
    - They are listed as 21 from docs.bigcommerce.com, then 6 from bigcommerce.com, then the 40 support.bigcommerce.com articles.
    - `--max 10` lists only developer docs.
  - **Titles:** a captured page shows no title in the listing, so a run can choose only by address and snippet.
  - **WooCommerce** isn't affected in the one search tried: its release code comes first, and 4 captures matched.
  - **Narrowing works today:** with `--with help.zid.sa`, the topic search matched 13 documents, and the 10 listed were all help pages. This works because the search matches the address too (line 313).
- **Fix:**
  - **The tool:** list each corpus's documents by how many of the terms each holds, most first, and then the shorter first. Print the addresses past the cap, one line each.
  - **The brief, item 6 and rule 7:** "Choose the documents by address and snippet. Never read a captured page over 100 KB whole: grep its text for your terms, and read the lines around what you find."
  - **Until the tool changes:** let Zid and BigCommerce runs narrow a search to the help centre with `--with help.zid.sa` or `--with support.bigcommerce.com`.
- **Severity:** must fix, before Zid and BigCommerce checking runs.

**2. Zid's terms, pricing and payments pages read as an error page.**
- **Where:**
  - recording brief, line 28: "run `python3 -I method/held_index.py <url>`, then read the text file it names";
  - `held_index.py`, lines 136 to 142, which count a capture as readable when its text file isn't empty.
- **Problem:** for zid.sa's own pages, the text file the tool names holds only the site's error page.
  - The text is in the raw page beside it. The corpus search and the checker read that page, but the brief never names it.
  - A run that reads as told finds nothing.
  - It can't route the page to the founder either: the page is "held and readable" (rule 8), and the checker refuses that route.
  - Live, zid.sa can render an empty shell (first check, finding 9).
- **Evidence:**
  - **The terms:** `held_index.py https://zid.sa/ar/legal/terms-conditions/` names two captures, both "readable".
    - Each text file is 91 bytes: "عفواً! حدث خطأ. / إعادة تحميل الصفحة / العودة للرئيسية".
    - The raw page beside each is 627 KB. Its text holds the terms, such as "خدمة الدفع عند التوصيل" and its clauses.
  - **How many:** 28 captures of 21 addresses are like this, and none of those addresses is held another way. Their raw pages are 95 to 627 KB. They are:
    - the terms and conditions, in both languages, and the privacy policy;
    - Zid Pay's terms for Saudi Arabia and for Kuwait;
    - the domestic and global shipping terms, and the logistics terms;
    - pricing, the payments pages, three country pages and four other pages.
  - **Zid's Q4 copies** on cash on delivery and bank transfer cite these pages: K0114, K0117 and K0122 cite the Arabic terms, and K0125 the English terms.
  - **The search reads them:** `corpus_search.py` reads the raw page for this reason (lines 256 and 257: "render an error or an empty shell (zid.sa, for one)"). So a search lists these pages with snippets from the terms.
  - **Quoting works:** a hand-made statement passed the checker. It quoted "عند الاشتراك في الخدمة وبناء على طلبك سوف نقوم بتفعيل خدمة الدفع عند التوصيل وذلك باستخدام المعلومات الخاصة بك." and cited the page's URL. Only the reading fails.
- **Fix:**
  - **The tool:** have `held_index.py` print a capture's text as the corpus search and the checker read it, from the text file and the raw page beside it, for example with `--text`.
  - **The brief, until then:** "A zid.sa capture whose text file reads only 'عفواً! حدث خطأ.' or 'Oops! Something went wrong.' keeps its text in the `raw.html` beside it. Grep that file; never read it whole. Cite the page by its URL."
- **Severity:** must fix, before Zid checking runs. It holds for Zid's recording runs too.

**3. Searching "in your platform's words" for points not yet matched misses what the platform names otherwise.**
- **Where:**
  - checking brief, item 6 (line 37): "run one corpus search with the terms of its account points not yet matched, in your platform's words";
  - item 8 and rule 7, for the rows that follow.
- **Problem:** a point not yet matched is one whose words the run hasn't seen in its platform.
  - Its search can only use the words the copies show, and those are the words of what is already matched.
  - Where the platform names the thing otherwise, the search misses it, and the point becomes a "not in what was read" row.
- **Evidence:**
  - **The page:** Zid's help page "خصائص الطلبات والمنتجات | الطلبات ( لوحة التحكم الجديدة )" (help.zid.sa/orders-properties/, updated 3 August 2026) has "تفعيل الدفع اليدوي".
    - It says: "تتيح لك هذه الوسيله إنشاء وتنفيذ الطلبات دون الحاجة إلى وجود عملية دفع إلكترونية فعلية."
    - It is reached from "الطلبات >عند إنشاء طلب يدوي > معلومات الدفع".
    - It bears on Q4's sentences [1] and [2].
  - **The copies:** none of Zid's 277 copied statements says it. The only "يدوي" among them is "استرجاع يدوي", a manual return (K0580).
  - **The searches:**
    - The topic search, in Zid's words from the copies, doesn't list the page.
    - A search with the words of Shopify's term in Arabic ("الدفع اليدوي") lists it, and only it.
  - **The checker:** a hand-made record of both sentences, cited by the page's URL, passes.
- **Fix:** in item 6, "search with each unmatched point's terms, in each language your platform uses, and with plain words for what it describes, as alternatives in one call. These are search terms only: they go in `searched`, and you record only your platform's own words."
- **Severity:** must fix.

**4. Account points that record what wasn't found, and the run's own open gaps, have no rule.**
- **Where:**
  - checking brief, items 4, 8 and 10 (lines 26 to 32, 40 to 42 and 50);
  - recording brief, step 5 (line 93), and the ids an account may cite (lines 162 to 165).
- **Problem:**
  - **The accounts' not-found points.** Some account points say only what the in-depth run didn't find, or which copied gaps stay open.
    - None of the four labels fits them. A match needs each platform's own words (item 3), and these points have none.
    - Item 8 would give each a "not in what was read" row, with its searches, about something neither platform was shown to have. With money flows first, such points come first.
    - Shopify's line 9 carries the concern map's own questions, which are ours (recording brief, line 100).
  - **The run's own open gaps.** The two briefs disagree on them, and the checker accepts either:
    - the recording brief says to cite a copied gap still open by its G or H id, and to record a not-found only for what no gap covers;
    - items 8 and 10 ask for a row for each point not shown, and allow only its `nf_id`.
  - **Absent.** Items 4 and 8 give only "not in what was read". A complete list of the platform that leaves the thing out (rule 6) has no place.
- **Evidence:**
  - **The points:** of the accounts' 85 points, 9 rest only on N, G or H ids.
    - Shopify's: lines 9 (Q4-SH-G0101, G0102), 16 (N03), 44 (N02), 56 (N04) and 61 (N01).
    - Salla's: lines 47 (N02), 69 (N01), 86 (N03) and 95 (G0117, H0008).
  - **Shopify's N01:** "A Shopify service that collects cash on delivery for the seller wasn't in what was read."
    - Zid's copies show Zid Ship collecting it (K0117, K0122).
    - Is that "differs" from N01? Does it "go beyond"? Or does it match Salla's [5] points only?
  - **Shopify's line 9:** "The copied gaps on who is responsible for manual payment methods, and why they are placed as they are, stay open." These are the concern map's "responsible" and "reason".
  - **Salla's line 95** ("who collects and holds cash-on-delivery amounts collected through Salla shipping labels before payout") meets Zid's own open gaps, G0023 and H0004 (H0016 repeats it).
    - Under items 8 and 10, it gets a new row with fresh searches.
    - Under step 5, it is cited by Zid's G and H ids.
  - **Zid's open gaps:** the copy holds 23 G and 19 H gaps still open, five of them on cash on delivery. For Q5, the pilot's H gaps on who holds a seller's money will meet the accounts' points in the same way.
  - **The checker:** a hand-made "the same" point resting only on G0019 and A0002 passed `--check`.
- **Fix:**
  - "An account point that rests only on not-found rows or copied gaps (N, G or H ids) records what the in-depth run didn't find. Don't sort against it, and record no row for it. What your platform shows on the same matter is sorted against the other points, or goes beyond."
  - In items 8 and 10: "Where one of your copied gaps still open covers an account point your platform doesn't show, label the point 'not in what was read' and cite the gap's G or H id. Record a row only for what no copied gap covers. Where a complete list of your platform leaves the point out, record its row as absent (rule 6)."
- **Severity:** must fix.

**5. The copies are sorted only when the account is written, after the reading and the rows that depend on them.**
- **Where:**
  - checking brief, item 5 (line 33), which keeps step 2;
  - recording brief, step 2, item 4 (line 81): "When you write the account, read `copied-view.tsv` once";
  - checking brief, item 6 (line 37), "not yet matched", and item 8, the rows for points not shown.
- **Problem:** which account points the copies match decides the searches of step 3 and the rows of step 5. The copies' statements are read only in step 6.
  - Before that, the run has `copied-index.tsv`: each copy's identifier.
    - An identifier shows a match on a term or identifier.
    - It doesn't show a match on a definition or role, or whether a match is "the same" or "differs".
  - Nothing tells the run to look at the copies before it records a not-found row. Rule 7 searches the corpus, and step 2's grep is for a statement.
  - A row recorded for a point a copy shows stays in `not-found.tsv`, since the checker doesn't ask that each row be cited.
- **Evidence:**
  - Zid's copies on Zid Ship's collection have the identifiers "محفظة التاجر", "زد شب" and "خدمة الدفع عند الاستلام (COD)" (K0117, K0121, K0122). Only their statements show that they play the role of Salla's [5] points.
  - A hand-made account that leaves the folder's only not-found row uncited passed `--check` with "no issues".
  - For Q4 on Zid, `copied-view.tsv` is 106 KB, about 23k tokens.
- **Fix:** "In a checking run, read `copied-view.tsv` once, after the accounts and before step 3, and sort the copies against the account points then. Don't read it again for the account."
  - Read this early, it stays in context through the reading: about 23k tokens for Q4 on Zid.
  - The run can't sort the copies without reading them.
- **Severity:** must fix.

**6. An account point named by one id, and a point that matches points in both accounts.**
- **Where:** checking brief, item 10 (line 49): "names the account point it is sorted against, by that account's ids"; item 4.
- **Problem:**
  - **Ids:** an id doesn't always name one point. 11 ids are cited by more than one point, such as Q4-SH-045, under [1] and [5], and Q4-SA-031, under [1] and [2].
  - **Two accounts:** a point can match points in both accounts, as Zid's cash on delivery matches Salla's and Shopify's. The brief speaks of one point.
    - A run that names one leaves the other account's point unsorted, and may later record it as not shown.
    - Nothing says which label a point takes when it is the same as one account's point and differs from the other's.
- **Fix:** "Name each account point a point matches, in every account, by platform, section and ids, such as 'Salla [1]: Q4-SA-P0098'. A point is 'the same' only if it is the same as each of them. Otherwise it differs, and names first the points it differs from."
- **Severity:** optional.

### Whether it presupposes an answer, or carries one platform's terms into another's record

**7. "The same term" is a basis, and "a name alone" is not.**
- **Where:** checking brief, item 3 (lines 19 to 25).
- **Problem:**
  - Basis 1 matches on the same term, a platform's own translation included.
  - The closing line says the same word can name different things, and that a name alone is no basis.
  - A run can't tell when a shared word is a term that matches and when it is a name that doesn't.
  - Item 4's "When unsure …, use 'differs'" settles a label once there is a match. It doesn't settle whether there is one.
- **Evidence:**
  - **The receipt:**
    - Zid's "Upload bank transfer receipt" sits under Reverse Orders (K0430). The held reverse-orders spec gives `refund_payment_method: bank_transfer` and a `receipt_link`, so it is a receipt for a refund.
    - Salla's "اختر صورة الإيصال البنكي" (Q4-SA-015) is the receipt of the buyer's payment.
    - On the term, Zid's point sorts against Salla's payment receipt. On the role, it sorts against Salla's refunds by transfer (Q4-SA-008, 009).
  - **Unpaid:**
    - Zid's `unpaid` "includes `pending`, `refunded`, and `voided` statuses" (K0209).
    - Shopify's "غير مدفوع", its own translation of "Unpaid", covers authorized, pending, expired and partially paid (Q4-SH-018).
    - It is the same term with other members: "differs" on basis 1, but "goes beyond" if it is a name alone.
  - **The first check:** its finding 26 gave Salla's "Markets" beside Shopify's "Markets" as the match on a name alone that the plan's rule exists to stop. Basis 1, as written, admits it.
- **Fix:**
  - Basis 1: "the same term, used by both platforms for what the question's sentence asks about, each quoted with what it names (a platform's own translation counts)".
  - In place of the closing line: "A word both platforms use for different things is no basis. Different words for one thing match on basis 3 or 4."
  - If this narrows PLAN.md section 6's rule, record it by a dated entry in section 11.
- **Severity:** must fix.

**8. The basis must be shown in both platforms' words, which item 2 forbids, and has no place in the record.**
- **Where:**
  - checking brief, item 2 (line 18): "Never take a word from an account that your own source doesn't use";
  - item 3 (lines 19 and 22): "each shown in the platforms' own words", and "the same definition, with both quoted";
  - item 10.
- **Problem:**
  - **Words:** item 3 asks for the other platform's words, and item 2 forbids them. A run either leaves the basis unshown, or writes the other platform's words into its own account.
  - **No place:** the record has nowhere to put a basis.
    - Neither `statements.tsv` nor `not-found.tsv` has a column for it.
    - The account's format gives only the label and ids.
    - So no one can later tell a match on a role from one on a shared word, which is what item 3 guards against.
- **Evidence:**
  - Zid's cash on delivery and bank transfer match Shopify's [1] and [2] points on their role.
  - Shown in Shopify's words, the basis is "Manual payment methods". None of Zid's 277 copied statements uses that term.
  - Zid's own nearest term, "الدفع اليدوي", was found only by searching (finding 3).
- **Fix:**
  - **Item 3:** "each shown in your platform's own words; the account point's words are found by its ids". Basis 3: "the same definition, yours quoted".
  - **Item 10:** "each 'the same' or 'differs' point gives its basis after its label, such as `- **differs** (role):`". A hand-made point written that way passed `--check`.
  - **Item 2:** "Use only your own platform's words in your statements, identifiers, scopes, headings, account and not-found rows."
- **Severity:** must fix.

**9. The accounts can steer what the run copies.**
- **Where:** checking brief, items 2 and 5. Nothing says whether the run reads the accounts before or after it sets the selection.
- **Problem:** a run that reads the accounts first may set its selection, and its `add` rows, by what the accounts cover rather than by the question.
- **Evidence:**
  - Salla's account files "Gateways and wallets the merchant connects" under [1] (lines 29 to 33).
  - Zid's candidates ZD-C-011 (other gateways) and ZD-C-013 (instalment services) are borderline for Q4's [1]: "no money passing through the platform or a payment service it provides".
- **Fix:** "Set the selection (step 1) before you read the accounts."
- **Severity:** optional.

**10. A route to the founder for an account point presumes the platform has it.**
- **Where:** recording brief, rule 8 (lines 122 to 126), which a checking run's not-found rows inherit.
- **Problem:** rule 8 routes to the founder what "shows only inside a seller's account", naming the page and where it is.
  - For an account point its platform's material doesn't show, a checking run can't know the platform has it at all.
  - A route then names a page the platform may not have, in the in-depth platform's terms, and puts it on the founder's capture list.
- **Evidence:** Shopify's [1] point has the seller pick or create a manual method on "the Payment providers settings page (Settings > Payments)" (Q4-SH-K1735 and others). A Zid row for it, routed to the founder, would name a Zid settings page that no Zid source names.
- **Fix:** "Route a row to the founder only where your platform's own material names the page or setting it would show on, in its own words. Otherwise `who_can` is `agent`, with no route."
- **Severity:** optional.

### Whether it is short

Before it records anything, a checking run on Q4 on Zid reads this much:

| Before the first statement | Size | About |
| --- | --- | --- |
| the two briefs | 24 KB | 6.2k tokens |
| the question's section and "How a run uses its question" | 1.3 KB | 0.3k |
| `selection.tsv` | 6.4 KB | 1.5k |
| `show` for S-01 and five concerns | 21 KB | 4.7k |
| `copied-index.tsv` and the pilot's absences | 25 KB | 5.6k |
| the two accounts | 17.6 KB | 4.4k |
| the checker on both in-depth folders | "no issues", in 15 seconds | |
| up to 20 ids looked up | about 1 KB each | up to 6k |
| the topic search | 5.5 KB | 1.4k |
| **Total** | | **about 24k to 30k** |

**Which bounds hold:**
- **They hold** for statements (60), for item 6's reading (for Q4: 10 documents, 5 for each of five sentences, and 5 live pages), for the ids looked up (10 for each account), and for the rows (20).
- **They don't hold** for the size of a captured page (finding 1), or for the reading behind the rows (finding 11).
- **`copied-view.tsv`** (about 23k tokens) is read once; finding 5 moves that read earlier.
- **The account** allows 800 words for the points sorted against the accounts' 85. At about 50 points, that is about 16 words a point, with its label and ids. The checker counts the accounts' ids as words (finding 13).

**11. Each not-found row repeats the search item 6 already ran.**
- **Where:**
  - checking brief, item 8 (line 40): "one `not in what was read` row for each point, with its corpus search (rule 7)";
  - item 6 (line 37);
  - rule 7 (recording brief, lines 116 to 121).
- **Problem:** the cap is on rows, not on reading.
  - Item 6 searches once for each sentence, with the terms of all that sentence's unmatched points.
  - Rule 7 then runs one or two more searches for each row, and reads up to 5 documents each.
- **Evidence:**
  - **Item 6:** for Q4, it allows 6 searches and 40 documents.
  - **The rows:** 20 rows allow 20 to 40 more searches, and 100 more documents.
  - **Output:** a Zid search prints about 5.6 KB with `--max 10`, so 20 rows add about 110 KB of listings.
  - **Time:** a Shopify or Salla search takes 19 to 57 seconds (first check, finding 23).
  - **Noted before:** the re-check's verification said so: "The cap is on rows."
- **Fix:** "A row's search (rule 7) is item 6's search for its sentence. Give that command in `searched`, and read for the row only among the documents it listed. Run rule 7's `--with` search only where the row is about a place or plan your statements name." If PLAN.md section 6 sets the search behind each not-found, record this by a dated entry.
- **Severity:** must fix.

**12. The order for the 20 rows doesn't choose for Q4.**
- **Where:** checking brief, item 8 (line 41): "first those for points on money flows, legal structure, the data model or partner contracts".
- **Problem:** for Q4, nearly every point concerns money flows, so the order doesn't say which points are checked. Two runs would check different points.
- **Evidence:** these all concern money flows, and the unmatched among the 76 compete for 20 rows:
  - Shopify's points on fees, refunds, payment terms, reports, currencies and the API;
  - Salla's points on the wallet, collection and fees.
- **Fix:** add "then in the order of the question's sentences, and within a sentence in the accounts' order".
- **Severity:** optional.

### The checker's `--check` mode

Each hand-made account below sat in a scratch copy of Q4 on Zid's folder, with one statement, one citation and one not-found row.

| Hand-made account | `--check` |
| --- | --- |
| Each label once, under [1] and [4], with a statement quoted from a held Zid capture and cited by its URL | no issues |
| The same, with a quote held only in a zid.sa raw page | no issues |
| A point with no label | error: "a point starts with its label" |
| A point citing only Q4-SA-K1603 | error: "a point that cites no id of this folder" |
| Sections "## Cash on delivery", "## [6]", "## [2] Names" and "##[3]" | four errors, one for each |
| "**Differs:**", a label inside the point, "**not found:**", "**the sameness**", and a nested item with no label | five errors, one for each |
| "differs:" not in bold, a numbered item, a colon outside the bold, a paragraph point, a nested item with its label, and the basis after the label | no error |
| A table of points | error: read as one point with no label |
| Account ids that don't exist, or of another platform or question; "the same" naming none; "goes beyond" naming one; "not in what was read" on a copy; a point on a G and an A id | no issues |
| "# [4]" and "### [5]" used as sections, a point before any section, [4] before [1], and [1] twice | no issues |
| An account that doesn't cite the folder's not-found row | no issues |
| 45 points, 820 words without ids | warning: "1024 words" |
| A point with no label, without `--check` | no issues |

**13. `--check` leaves the checking brief's own rules unchecked.**
- **Where:** `check_proposals.py`, `check_account` (lines 300 to 322).
- **Problem and evidence:** the checker catches a missing label, a point citing only another platform's ids, and a malformed `##` heading. Each of these passed (table above):
  - "the same" naming no account point, "goes beyond" naming one, and "not in what was read" resting on a copy with no `nf_id`;
  - account ids that don't exist (Q4-SH-999, Q4-SA-K9999), of a platform not read in depth (Q4-WC-001), and of another question (Q5-SA-K0001);
  - "# [4]" and "### [5]" used as sections, a point before any section, sections out of order, and a section twice;
  - a not-found row the account doesn't cite.

  Also, the length counts each id of another platform as three words, and item 10 requires those ids. An account of 45 points and 820 words without ids is counted as 1,024 words, and warned past 900.
- **Fix:**
  - Count words with every id of the question removed.
  - Check that every point but "goes beyond" cites an id of a named in-depth folder, that each such id exists there, and that "goes beyond" cites none.
  - Check that a "not in what was read" point cites an `nf_id` (or a G or H id, with finding 4's fix), and that each row is cited.
  - Report a heading of any level that holds a sentence's number but isn't `## [n]`, a point before the first section, and sections out of order.
- **Severity:** optional.

### Agreement with the recording brief as it now stands

| In the recording brief | The checking brief |
| --- | --- |
| S-01 offered to every question (step 1, line 67) | Agrees: item 5 keeps step 1. For Q4 on Zid, S-01 bears on the question, and its copies are 70% of `copied-view.tsv`. |
| `show` for S-01, and for a concern with no statements (lines 67 and 68) | Agrees. `show zid S-01` prints 138 identifiers in 16 KB. No Q4 candidate on Zid is without statements. |
| Tables and the cap (rules 5 and 12) | Item 9 restates rule 12 without its count for tables and lists (finding 14). Rule 5's "where an absence rests on it" can't arise while a checking run records no absences (finding 4). |
| Subheadings (line 161) | Agrees: item 10 keeps the recording brief's sections, and the checker allows `###`. |
| Fetch-archive citations (line 140) | Agrees. Zid's search reads no fetch archives, so a Zid run doesn't meet them. |
| Nested lists (line 167) | Agrees: each point starts with its label. The checker reads a nested item as its own point, which needs its own label and id. |
| Copied gaps cited by G and H ids (step 5, line 93; line 164) | Disagrees: items 8 and 10 (finding 4). |
| Step 3's last paragraph (line 89) | Unclear whether it holds (finding 14). |

**14. Items 6 and 9 restate step 3 and rule 12 without saying what else of them holds.**
- **Where:** checking brief, item 6 (lines 34 to 38), item 9 (line 45) and item 3 (line 22).
- **Problem:**
  - **Item 6** replaces step 3's reading, but doesn't say whether step 3's last paragraph still holds. That paragraph says:
    - stop after 5 pages in a row add nothing new;
    - read each page in one language;
    - a sentence that only gives examples has no reading of its own.

    Item 6's searches also drop "in each language it uses".
  - **Item 9** gives rule 12 as "stop reading once you pass 60 new statements". It drops two things: that the rows of one table, or the runs of one list, count as one; and that the run then writes its account, runs the checker and reports.
  - **"Scope":** item 3's "a scope" is an identifier, an access scope. Item 4's "its scope" is where a statement holds. The first check's finding 18 fixed the same in the recording brief.
- **Fix:**
  - "Step 3's last paragraph holds, and each search is in each language your platform uses."
  - "Rule 12 holds, with 60 in place of 120."
  - In item 3: "an access scope".
- **Severity:** optional.

## Verdict

**Checking runs can't start yet.** There are 14 findings: 8 must fix and 6 optional.

- **Before any checking run:** findings 3, 4, 5, 7, 8 and 11. Each is a line or two in the brief.
- **Before Zid and BigCommerce checking runs:** finding 1, and for Zid also finding 2. Each wants a small change to a tool (`corpus_search.py`, `held_index.py`), or meanwhile a line in the brief.
- **WooCommerce:** in what was tried, a WooCommerce checking run needs neither finding 1 nor finding 2.
- **What ran clean on Q4 on Zid:**
  - the candidates, `show` for S-01, the copy and its views;
  - the checker on both in-depth folders;
  - the ids looked up, which stay small;
  - statements and quotes from held Zid captures cited by URL, including pages held only as raw pages;
  - `--check`, which catches a missing label, a point citing only another platform's ids, and a malformed `##` heading.
- **The optional findings** can go in with the same edits.
