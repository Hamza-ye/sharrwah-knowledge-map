# Verification of the fixes to the checking brief

**19 October 2026.** A check of the fixes made in 73588ac to the 14 findings of `studies/proposals/checks/R3-checking-brief-read.md`. The fixes are read in the diff from 9a1736f: `studies/proposals/briefs/R3-checking.md`, `R3-recording.md`, `method/corpus_search.py`, `method/check_proposals.py`, and PLAN.md section 11's entry of 19 October.

The repository is at 8be116e (73588ac and two STATE.md updates), on branch `claude/vibrant-meitner-oh70v4`. Only this file was added to it. Every command ran with `python3 -I -B` from the repository's root, and its outputs went to a scratch folder.

**What was run:**
- **`corpus_search.py` on Zid and BigCommerce:**
  - the read's Zid topic search, and a Zid search for sentence 3;
  - the read's BigCommerce search, rebuilt to its 67 documents;
  - item 8's search for Q4's [1], with 12 single forms and 5 calls.
- **The same matches re-sorted three ways,** through `corpus_search.py`'s own functions: as the tool now sorts, by density alone, and as the read proposed.
- **Zid's captures:** `held_index.py` and `grep` on them, and a scan of the 28 zid.sa captures whose text file holds only the error page.
- **The checker in checking mode:** `copy_statements.py copy Q4 zid` into scratch, with 14 concerns and S-01 copied. Then `check_proposals.py records Q4 zid --dir … --check` on 28 hand-made accounts.
- **The checker in recording mode:** `check_proposals.py records Q P`, without `--check`, on the 21 in-depth folders.

| Finding | The read's severity | Now |
| --- | --- | --- |
| 1. The search's order, and long pages | must fix | fixed |
| 2. zid.sa's error pages | must fix | partly fixed (new problem 1) |
| 3. Searching for points not yet matched | must fix | partly fixed |
| 4. Points of what wasn't found, and open gaps | must fix | fixed |
| 5. When the copies are sorted | must fix | fixed |
| 6. Naming the points sorted against | optional | fixed |
| 7. "The same term" and "a name alone" | must fix | fixed |
| 8. The basis, and in whose words | must fix | fixed |
| 9. The selection before the accounts | optional | fixed |
| 10. Routes to the founder | optional | fixed |
| 11. The search behind each row | must fix | fixed |
| 12. The order of the 20 rows | optional | fixed |
| 13. The checker's `--check` | optional | partly fixed |
| 14. Step 3 and rule 12, restated | optional | fixed |

## The findings

### 1. The search's order, and long pages: fixed

- **The fix:**
  - `corpus_search.py` now sorts each corpus's documents: those holding two or more of the terms first, then the densest. It prints up to 30 addresses past the cap.
  - The recording brief (line 30) forbids reading a captured page over 100 KB whole.
  - Item 8 chooses by address and snippet.
- **Zid, the read's topic search** (`"الدفع عند الاستلام" "التحويل البنكي" "تحويل بنكي" "Cash on Delivery" "Bank Transfer" "COD" --max 10`): 43 documents, as before.
  - help.zid.sa/cod/ is now 1st; it was 22nd.
  - 4 of the first 10 are help pages, where none were.
  - The 1.7 MB `get-manager-profile.md` is now 39th.
  - The other 8 help pages come 28th to 42nd (new problem 3).
- **Zid, sentence 3:** the read doesn't give its eight terms, and no set tried gives its 144 documents.
  - With `"تم الدفع" "مدفوع" "إيصال" "استرجاع" "mark as paid" "paid" "receipt" "refund"`, 150 documents match.
  - 6 of the first 10 are help pages.
  - `llms.txt`, `list-of-orders.md` and `get-manager-profile.md` come 26th, 28th and 35th.
- **BigCommerce,** the read's search rebuilt to its 67 documents (`"offline payment" "offline payments" "manual payment" "manual payments" "Cash on Delivery" "Bank Deposit" "Check" "Money Order"`):
  - 9 of the first 10 are support.bigcommerce.com articles, led by Offline-Payment-Methods. Before, all 10 were developer docs.
  - The three looked up have a readable capture of 8 to 21 KB each: Offline-Payment-Methods, Creating-a-Manual-Order and Processing-Refunds.
- **Long pages:** Zid's 7 reference pages over 100 KB have no line over 458 characters, so the rule's `grep` works on them. On zid.sa's raw pages it doesn't (new problem 1).
- **The listing's size:** the lines past the cap add about 3 KB. The topic search prints 8.8 KB in all.

### 2. zid.sa's error pages: partly fixed

- **The fix:** the recording brief (line 29) now says that such a capture's text is in the `raw.html` beside it, and to search that file with `grep`. `held_index.py` is unchanged.
- **What works:** the brief names the file, and the checker finds quotes held only there.
  - A hand-made folder quoted "Basic payment methods (bank transfer, cash on delivery)" from zid.sa/en/pricing/, and "تفعيل فوري لخيارات دفع متعددة مثل مدى، آبل باي، الدفع عند الاستلام، تقسيم المدفوعات ونقاط الولاء" from zid.sa/ar/paymob/.
  - It passed `--check`.
- **What doesn't:** a plain `grep` prints whole lines. Each of these raw pages holds a line of 89,000 to 333,000 characters, and nearly any term matches it.
  - All 28 such captures, of 21 addresses, have one.
  - **Text only on that line:** on 10 of the 21 addresses, 99 to 100% of the text is only on such lines. They are pricing, both payments pages, the Egypt, Syria and UAE pages, paymob, zid-voice, zid-assurance and partner-payouts. There are no "lines around what you find".
  - **The Arabic terms:** `grep 'خدمة الدفع عند التوصيل'` prints 378,566 bytes, 377,019 of them on its line 16.
  - **Pricing:** `grep -i 'Cash on Delivery'` prints 337,611 bytes, all on one line.
  - **In the topic search:** 3 of its first 10 are such captures. On two of them (uae and pricing) the text is all on the long line.
  - **What works instead:** a bounded `grep -o '.\{0,150\}<term>.\{0,150\}' raw.html` gives readable passages on both, and the quotes above come from it.

### 3. Searching for points not yet matched: partly fixed

- **The fix:** item 8's search for each sentence now takes the unmatched points' "terms in each language your platform uses, and plain words for what each describes". It records only the platform's own words.
- **The test:** does that search reach help.zid.sa/orders-properties/? The page has "تفعيل الدفع اليدوي", reached from "الطلبات > عند إنشاء طلب يدوي > معلومات الدفع".
- **Each form alone,** with `--max 10`:
  - **The forms the accounts give match no Zid document:**
    - Shopify's own Arabic, "طرق الدفع اليدوية" (its account, line 13);
    - Salla's "إنشاء طلب جديد يدوياً" (its account, line 25);
    - "manual payment" and "Manual payment methods".
  - **Other forms that match nothing:** "الدفع اليدوية", "دفع يدوي", "طرق دفع يدوية", "طلب جديد يدوي" and "طلبات يدوية".
  - **Three forms reach the page:** "الدفع اليدوي" (it alone), "إنشاء طلب يدوي" (2 documents) and "طلب يدوي" (4).
- **Calls of several terms:**
  - A call for [1] of 8 terms, with Shopify's Arabic and no shorter form, matched no document at all.
  - A 20-term call for [1] that held "الدفع اليدوي" listed the page 4th.
- **Why:**
  - **Arabic:** the search matches an Arabic term as written, inside words but not across them. A shorter form finds the longer: "الدفع اليدوي" finds "الدفع اليدوية", but not the reverse.
  - **English:** words in Latin letters match whole, so a singular doesn't find its plural. On BigCommerce, "manual payment" lists 3 documents and "manual payments" 1.
- **Still needed, must fix:** a line in item 8, below.

  > The search matches a term as written: Arabic inside words, Latin letters as whole words. Search each Arabic term in its shortest form, such as الدفع اليدوي for طرق الدفع اليدوية and طلب يدوي for إنشاء طلب جديد يدوياً, and each English term in the singular and the plural.

### 4. Points of what wasn't found, and open gaps: fixed

- **The fix:**
  - Item 3: an account point resting only on N, G or H ids is not sorted against, and gets no row.
  - Item 10: a copied gap still open is cited before any row is recorded, and `absent` has its place. Recording step 5 and item 10 now agree.
- **The test:** applied mechanically, the rule picks out exactly the read's 9 points.
  - They are Shopify's lines 9, 16, 44, 56 and 61, and Salla's lines 47, 69, 86 and 95.
  - Salla's line 33 rests on a pilot absence (A0002), and stays sorted against.
- **The checker:**
  - It accepts a "not in what was read" point that cites the run's own G id (G0023) or the pilot's H id (H0004).
  - It refuses one resting only on an A id, a copy or a statement.
- An `absent` row has no label of its own in the account (new problem 4).

### 5. When the copies are sorted: fixed

- **The fix:** item 2's order of work and item 7 read `copied-view.tsv` once, right after the accounts, and sort the copies then. A point the copies match needs no search. Item 7 amends the recording brief's step 2, so the two agree.
- **The view:** `copied-view.tsv` holds statements only: in the scratch copy, 116 K and 158 P, 107 KB. The copied gaps that item 10 now cites are still read by step 2's `grep`, which item 7 keeps.
- **The checker:** the read found that a not-found row no point cites passed. It is now refused (finding 13).

### 6. Naming the points sorted against: fixed

- **The fix:** item 6 names every matched point, in each account, by platform, section and ids. A point is "the same" only if it is the same as each of them.
- **The test:** 11 ids are cited by more than one point, and the section tells 10 of them apart.
  - Q4-SA-K1604 is cited by two points of Salla's [2] (lines 37 and 38). Named by that id alone, it names both.
  - Optional: "by platform, section and the ids that name it alone".

### 7. "The same term" and "a name alone": fixed

- **The fix:**
  - Basis 1 is now "the same term, used by both platforms for what the question's sentence asks about".
  - The closing line is the read's: "A word both platforms use for different things is no basis. Different words for one thing match on basis 3 or 4."
  - PLAN.md section 11's entry of 19 October records the narrowing.
- **The read's cases now decide:**
  - **The receipt:** Zid's "Upload bank transfer receipt" is a refund's receipt. Salla's "اختر صورة الإيصال البنكي" is a payment's. The word names different things, so the term is no basis. On its role, Zid's point matches Salla's refunds by transfer (Q4-SA-008, 009), and differs.
  - **Unpaid:** both platforms use it for the order's payment status, with other members. That is basis 1, and differs.
  - **Markets:** the first check's "Markets" beside "Markets" is no basis.

### 8. The basis, and in whose words: fixed

- **The fix:**
  - Item 4 shows each basis "in your platform's own words; the account point's own words are found through its ids".
  - Basis 3 quotes only the run's own definition.
  - Item 12 puts the basis after the label.
- **The test:** hand-made points written `- **differs** (term):` and `- **differs** (role):` passed `--check`.
- Item 3's widened rule on words now contradicts three other items (new problem 2).

### 9. The selection before the accounts: fixed

- **The fix:** item 2 sets step 1, the selection, before the accounts are read.

### 10. Routes to the founder: fixed

- **The fix:** item 10 routes a row only where the platform's own material names the page or setting. Otherwise `who_can` is `agent`, with no route.
- It narrows recording rule 8 without contradicting it.
- **The test:** the checker accepts such a row: the scratch folder's N01.

### 11. The search behind each row: fixed

- **The fix:** item 10 makes a row's search item 8's search for its sentence. The row is read for only among the documents that search listed. Rule 7's `--with` search runs only for a place or plan the statements name.
- PLAN.md's entry records this as narrowing the entry of 18 October.
- **For Q4:** beyond item 8's 6 searches, the rows add only `--with` searches.
- **The test:** the checker accepts a row whose `searched` gives item 8's command.

### 12. The order of the 20 rows: fixed

- **The fix:** item 10 adds "then in the order of the question's sentences, and within a sentence in the accounts' order".
- **Ambiguity left, optional:**
  - **Where the cap falls:** the accounts give 76 points to sort against: 19 in [1], 5 in [2], 35 in [3], 11 in [4] and 6 in [5]. So the cap of 20 can fall inside a sentence. Inside [3], whether Shopify's 16 or Salla's 19 come first decides which points are checked, and "the accounts' order" doesn't say.
  - **The first group:** "first …; then in the order of" can also be read as ordering only the points outside the first group.
  - **Wording that closes both:** "the points of the first group, then the rest, each in the order of the question's sentences, and within a sentence account by account, in the order the message names them".

### 13. The checker's `--check`: partly fixed

- **Done:**
  - ids of any platform are no longer counted as words;
  - a "not in what was read" point must cite its own N, G or H id;
  - every not-found row must be cited by a point;
  - three kinds of section are reported: a heading of any level that starts with a sentence's number but isn't `## [n]`, a point before the first section, and sections out of order or repeated.
- **Not done:** checking that every point but "goes beyond" cites ids of a named in-depth folder, that those ids exist there, and that "goes beyond" cites none.
- **The 21 in-depth folders** all pass `check_proposals.py records Q P` without `--check`: "no issues", exit 0, in 3 to 35 seconds each.
- **The test:** each account below sat alone in the scratch copy of Q4 on Zid's folder, with one statement quoted from help.zid.sa/cod/, one citation and one not-found row.

| Hand-made account | `--check` |
| --- | --- |
| Valid by the new brief: bases after labels, points of both accounts named, "not in what was read" on N01 and on G0023 | no issues |
| [4] before [1]; [1] twice | one error each |
| "# [4]" or "### [5]" as a section; a "### [2] Names" subheading | one error each |
| A point before the first section | error |
| "not in what was read" resting only on a copy, a statement or an A id | one error each |
| "not in what was read" on the pilot's H id | no issues |
| The folder's not-found row cited by no point | error |
| 45 points, 895 words without ids (1,294 as counted before) | no issues |
| 45 points, 1,027 words without ids | warning |
| Sections [1], [3], [2], [3] | one error, for [2]; the repeated [3] passes |
| "the same" naming no point; "goes beyond" naming one; Q4-SH-999, Q4-SA-K9999, Q4-WC-001 or Q5-SA-K0001 | no issues: not done |
| Caught before: no label; only another platform's id; "## Cash on delivery", "## [6]", "## [2] Names", "##[3]"; "\*\*Differs:\*\*", "\*\*not found:\*\*", "\*\*the sameness\*\*"; a table | still caught: 1, 1, 4, 3 and 1 errors |

### 14. Step 3 and rule 12, restated: fixed

- **The fix:**
  - Item 8 adds "in each language it uses" to both of its searches.
  - It adds: "Step 3's last paragraph in the recording brief holds".
  - Item 11: "Rule 12 holds, with 60 in place of 120."
  - Basis 2 says "an access scope", and the label "differs" says "where it holds".

## New problems

**1. The `grep` the recording brief now gives for zid.sa's raw pages prints whole pages.** Must fix, before Zid's checking runs. It holds for Zid's recording runs too.
- **Where:** recording brief, lines 29 and 30: "Search that file with `grep`" and "read the lines around what you find".
- **Problem:** each of the 28 captures' raw pages holds a line of 89,000 to 333,000 characters that nearly any term matches. On 10 of the 21 addresses, the text is only on such lines.
- **Evidence:** finding 2, above.
- **Fix:** replace "Search that file with `grep`" with this.

  > Search it with a bounded `grep -o`, such as `grep -o '.\{0,200\}<term>.\{0,200\}' raw.html`: a plain `grep` prints whole lines, and these pages hold lines of up to 333,000 characters.

  Or have `held_index.py` print a capture's text as the corpus search reads it, as the read proposed, and search that.

**2. Item 3's rule on words contradicts items 6, 8 and 10.** Optional.
- **Where:** checking brief, item 3 (line 24): "Use only your own platform's words in your statements, identifiers, scopes, headings, account and not-found rows. Never take a word from an account that your own source doesn't use."
- **Problem:**
  - item 8 puts the accounts' terms in `searched`, a column of the not-found rows;
  - item 10 writes `what_is_missing` "in plain words", which are no platform's words;
  - item 6 names "Salla [1]: …" in the account.

  A run will most likely follow the more specific item. Read literally, item 3 would keep the accounts' terms out of the very search finding 3's fix rests on.
- **Fix:** replace item 3's sentence with this.

  > Use only your own platform's words in your statements, identifiers, scopes, headings and account points. The only exceptions are the other platforms' names and ids (item 6), the search terms in `searched` (item 8), and the plain words of `what_is_missing` (item 10).

**3. The corpus search's "two or more of the terms" key outranks density.** Optional.
- **Where:** `corpus_search.py`, line 339. PLAN.md's entry describes the order by density alone.
- **Problem:** a page holding two terms comes before every page holding one, however densely the one holds it. The two can be a name and its abbreviation ("Cash on Delivery", "COD"). Long reference pages hold many terms.
- **Evidence,** the same matches sorted as the tool does and by density alone:
  - **Topic search:** Zid's FAQ on how cash-on-delivery amounts are collected is 28th. By density alone it would be 2nd.
  - **Sentence 3:** help.zid.sa/orders-properties/ (finding 3's page) is 39th. By density alone it would be 8th.
  - **The 20-term call for [1]:** the first 10 hold 4 reference pages over 100 KB and 1 help page. By density alone they would hold 2 and 3.
  - **BigCommerce:** 9 of the first 10 are support articles either way.
- **Fix:**
  - Sort by density alone.
  - In item 8, say whether a run may choose by address among the addresses printed past the cap, within the same count.

**4. An `absent` row has no label in the account.** Optional.
- **Where:** checking brief, item 10 (line 50) gives a row the kind `absent` where a complete list leaves the point out. Item 5 has no matching label, and item 12 cites rows only under "not in what was read".
- **Problem:** the account labels a point that a complete list shows absent as "not in what was read". That says less than its row does. The checker accepts it.
- **Fix:** "Label such a point `- **not in what was read** (absent):`." A hand-made point written that way passed `--check`.

## Verdict

**Checking runs can't start yet, but they can after two short changes, both in the briefs.** 11 of the 14 findings are fixed and 3 are partly fixed: findings 2 and 3, both must fix, and 13, which is optional. The fixes bring 4 new problems: 1 must fix and 3 optional.

- **Before any checking run:** finding 3's last line in item 8. Search each Arabic term in its shortest form, and each English term in the singular and the plural. Without it, the terms the accounts themselves give can match nothing.
- **Before Zid's checking runs:** new problem 1. A bounded `grep -o` for zid.sa's raw pages, or `held_index.py` printing their text. BigCommerce's and WooCommerce's runs don't meet these pages.
- **What ran clean:**
  - the search now reaches Zid's help centre and BigCommerce's support articles before the long reference pages;
  - `--check` catches each case its new checks were written for, and everything it caught before;
  - the 21 in-depth folders pass the checker;
  - quotes from zid.sa's raw pages pass the checker.
- **The optional items** can go in with the same edits: new problems 2 to 4, the last words of findings 6 and 12, and the id checks of finding 13.
