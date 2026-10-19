# Check of the R4 drafting brief (an inspection, Fagan 1976)

**19 October 2026, at commit 6bfb8d2d2e04e86e58526b940a96a9e93c986235.** The brief checked is `studies/proposals/briefs/R4-drafting.md`, with the checker's `drafts` mode in `method/check_proposals.py`.

**What I read.** The brief, and what it names for Q7: its question, its `depth.tsv` rows, its five accounts and `notes.md` files, about 40 ids through `record_ids.py`, its ten areas in `areas.md`, `areas.tsv`'s columns, the Yemen digest (lines 1 to 444 read, the rest searched), and Decision 14's section of `entry.md`. For Q5, the pilot's pieces only as far as needed. The tools the brief names, and `copy_statements.py`'s copy table. In `PLAN.md`: sections 1, 2, 4 (R4, R5), 6 and 7, and one line of section 11 that a search returned. In `founder-decisions.tsv`: the G1 rows for the deferral and the guard. In `sizing.md`: the R4 and R5 rows, and the phase C measure they rest on.

**What I ran.** The brief's order of work on Q7, through step 6. In my scratch directory (`/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/R4-brief-check/`, one folder per case), I wrote a partial draft (section 1's [4], two points of section 2, and section 6), then six more drafts holding about 40 deliberately wrong points, named below as W01 and so on. I checked each with `python3 -I -B method/check_proposals.py drafts Q7 --dir <case> --cited`. The partial draft passed with `no issues` (17 facts, 2 not-found, 5 Stage 1 ids, 2 "doesn't show", 834 words).

**What holds.** The guard is worded as `founder-decisions.tsv` gives it, and so is the deferral, except for "not even for one country" (finding 1). Sentence numbering agrees between the checker and `questions-for-agents.md` for all eight questions. The checker catches invented quotes, quotes from records the point doesn't cite, unknown and other questions' ids, an area cited as a point's only id, missing sections, and the limits.

**18 findings, 8 of them must fix.**

## Must fix

**1. Must fix. The brief fixes "country" as the level Sharrwah is set up at.** Brief lines 9, 141, 36 and 69.
The plan says "each market is set up on it" (PLAN line 20), and calls "per market" "a working description, not a fixed level" (line 305). The brief turns this into "set up for each country it serves" and "What differs between countries is set up, not built apart". The deferral becomes "not even for one country", and section 3's list of levels names "per country". That fixes a level in advance, against the brief's own line 146. For Q7 it points away from the evidence. Yemen's currency differs by area within the country: YA-01 gives "YER 533 @ Sana'a" against "YER 1,562 buying, 1,567 selling @ Aden", YA-15 "old notes only, Aden's new notes barred @ Houthis' area", and YK-12 "split". The platforms set currencies per market, storefront, business entity or bank account, not per country.
*Fix:* "built once and set up for each place it serves; what a place is, and the level at which things differ, come from the evidence". Give no level priority in section 3's list.

**2. Must fix. The pilot's entry reaches the drafts with its holder, its levels and its recommendations.** Lines 26 to 27 and 96.
Items 7 and 8 have Q5 and Q7 read their decisions whole, and line 96 lets "its questions and options frame yours". Decision 14 asks "In which currency should Sharrwah hold and pay out a merchant's funds" (entry line 331), which presupposes that Sharrwah holds them: the guard neither requires that nor rules it out. Its options fix levels, "in each market" and "per merchant" (line 339), and Decision 1 gives "bound per market, store or plan" (line 97). Each decision then gives the coordinator's recommendation. Q7's is "several currencies per merchant, with the rial recorded apart by the area its funds are held in" (line 340). "Bind nothing" doesn't keep an agent from being led to them (the plan's risk 2).
*Fix:* give the runs a checked extract with each decision's heading, question and options only, leaving open who holds and at what level, and without the recommendation, "Why it is yours", "Yemen's mark" or "Your answer". Have them read it after drafting sections 2 to 5.

**3. Must fix. Q7 doesn't read the pilot's open findings, though section 8 asks how they bear, and one of them concerns Decision 14.** Lines 27 and 95.
Only Q5 reads the method report's "Still open after the re-check". Its first item, finding 36 (method-report line 147), says Zid's S01-V-528 "names only what doesn't fill the role" and that "the currency question's reading and Yemen mark rest on it". That is Decision 14's mark, "carried unchanged, through Zid's wallet (S01-V-528)" (entry line 338). Q7's agent reads that mark with no warning, and has nothing to write line 95's bullet from.
*Fix:* add the list to item 8, or mark line 95 "Q5 only" and have the coordinator bring finding 36 in when finishing Q7.

**4. Must fix. "The pilot's statements are among Q5's copies" is wrong for Q7.** Line 93.
Every Q7 platform copied S-01 (each `selection.tsv` has `S-01 ... copy`), so Q7's records hold the pilot's statements under Q7's own P ids (Q7-ZD-P0122, Q7-SA-P0168). Citing a Q5 id gets `an id of another question` (W07). "By id only" (line 21) also leaves no route to a pilot statement no account cites: of Decision 14's seven quotes, Shopify's "Hong Kong SAR dollar bank account" is only under Q7-SH-P0157, which no account cites.
*Fix:* "among your question's copies, as `P` ids". Optionally, allow `grep -F` in the question's own `copied-view.tsv`, the view the copy script made "to read instead of the copies".

**5. Must fix. "Like with like" is narrowed from four kinds to two.** Line 136.
PLAN line 311 assigns four kinds by rule (observed, shipped, stated, official page) and compares "like with like". Section 11 (line 549) applies this to R4. The brief groups docs, help, terms, pricing and shipped code together as "declare". So Shopify's terms set against Zid's help wouldn't be called mixed. Separately, `source_kinds.py` gives Shopify's Admin GraphQL schema as `stated` (`structures/shopify/admin-graphql-schema ... -> stated`), though the plan calls "a schema the platform ships" shipped. My own test point called that schema shipped, and the tool says otherwise.
*Fix:* "compare within one kind, as `source_kinds.py` gives it; where a comparison mixes kinds, name them." The schema's rule is for the coordinator to look at.

**6. Must fix. The checker takes a variation point as a record, and its words as a platform's quote.** `check_proposals.py` lines 435 to 450; `record_ids.py` `other_rows`.
A point that quotes "settle in your store's default currency" and cites only S01-VP-23 passes (W11). So does a section 2 proposal resting only on S01-VP-23 (W17). The quote is found in the variation point's `x_words`, which is the pilot's table, not a Q7 record. `--cited` doesn't count VP ids among facts, so R5 would never re-check such a quote. That goes against PLAN line 323: "Everything a proposal cites gets the full checks". Areas are already refused as a point's only id (W14), but variation points aren't.
*Fix:* check quotes and Arabic only against platform and Stage 1 texts. A VP id alone doesn't count as citing a record outside section 8.

**7. Must fix. A "not in what was read" that cites no not-found row passes, and isn't counted.** Lines 56 and 112.
"BigCommerce's reading didn't show a point-of-sale rule on local currency, which Shopify shows. Q7-SH-072" passes, and `--cited` reports `not found or absent 0` (case R01). That claim would get no search and no audit. PLAN's risk 4 (line 376) has the checker reject a "not in what was read" without its list and search. The `records` mode does this for accounts (`a 'not in what was read' point cites its not-found row or copied gap`), but the `drafts` mode doesn't. Line 56 also invites such points ("where a platform's reading didn't show it"), while line 112 says to leave them out unless the proposal rests on them.
*Fix:* in `drafts` mode, a point saying "not in what was read", "didn't show" or "not shown" must cite an N, G or H id. Section 6 and "not checked on" points are excepted. In line 56, add "where your proposal rests on it, citing its row".

**8. Must fix. Two rules disagree on where "doesn't show" goes, and nothing limits how many there are.** Lines 83 and 161; sizing.md, R5.
Section 6 covers elements "that Yemen's evidence bears on" (line 83). The Yemen rules say "Where no fact bears, write 'Yemen's evidence doesn't show'" (line 161), which reads as one for every element without a fact. Each such claim gets R5's search and audit, at about 2.7 million tokens each. R5 sizes 15 in all, about 2 a proposal. My partial draft wrote two for two elements (`doesn't show (section 6 lines) 2`). A full draft has 10 to 15 elements. The checker lists these claims but never warns.
*Fix:* one rule: "doesn't show" only where an element's set-up for Yemen depends on a fact the digest doesn't give, with what would show it. Allow at most about 2 (Q5 about 3), and have the checker warn past that.

## Optional

**9. Optional. The citing limits sit above R5's sizing, and Yemen is counted by id.** Lines 107 to 109; `LIMITS`.
At the limits, the drafts cite 7 × 45 + 70 = 385 facts, against the 320 that R5 sizes (40 a proposal). They cite 7 × 8 + 12 = 68 Stage 1 ids, against about 60 Yemen facts. R5 re-checks a Yemen fact by state and place, and one id often carries several: my section 6 cited YA-01 at Sana'a and at Aden, two facts under one id.
*Fix:* set about 38 facts (Q5 about 60), or re-size R5. Count Yemen parts (id and place), not ids.

**10. Optional. The "absent" check rejects true sentences and accepts unrelated absences.** Line 113; checker lines 457 to 461.
It rejects "not recorded as absent, only as not in what was read" (W06), and Stage 1's own state, YA-49's "Largely absent" (case abs). It accepts "a wallet in US dollars is absent from Zid" citing Q7-ZD-A0002, an absence about the countries مدفوعات زد serves (W05).
*Fix:* skip the word inside quotation marks and in Stage 1 states. R5's audit covers the rest.

**11. Optional. The checker's exemptions are wider than the brief's.** Line 104; checker lines 439 to 443 and 462.
Any section 4 point passes without ids, including one that states a platform fact (W21). A section 6 point with "doesn't show" anywhere in it passes, even when it also asserts an "allows" with no id (W24). The Yemen date warning applies only in section 6 (W19 passes in section 2), and any year satisfies it (W27, "the law of 2010").
*Fix:* a section 4 point without ids must name a bold element of sections 2 and 3. A section 6 point without ids must have no "allows" or "forbids". Check dates in every section, after the id.

**12. Optional. There are traps in quoting.** Lines 120 and 158.
Single quotes aren't checked: 'all balances are held in US dollars' passes (W12). The brief's own Yemen example fails if it is kept in its quotation marks (F02). A Yemen id in backticks fails, with `quoted words not found ... ya-01` (W23). A quote shortened with an ellipsis can't be found, since the check is a substring match.
*Fix:* "double or angled quotation marks only, around words that stand together in the record; ids never quoted". Show the Yemen example without quotation marks, and check single quotes at word boundaries.

**13. Optional. The structure the checker wants should be said plainly.** Lines 53 to 96.
The brief shows the draft's sections at `###`, under its own `## draft.md`. If an agent copies that level, the checker reports only `sections []` (case hdr). Sentences answered together must be adjacent: `[1] [3]` then `[2]` fails. Each nested list item is its own point. So a section 2 element line whose sources are in sub-items fails, and so do section 8's "the question in one line" and "whether sections 2 to 5 settle it" lines, which have no natural id (case fmt, W30). "Settle" also sits oddly with "Your draft decides nothing".
*Fix:* write the headings literally (`## 1. How the platforms handle it`), and say that pairs are adjacent and that an element line cites its ids. Let the question line cite the decision's S01-VP id, and exempt the "answers it, keeps it open or leaves it" line as section 4 is exempt.

**14. Optional. Some inputs carry earlier framings, and the brief doesn't mark them.** Lines 17 and 23.
`depth.tsv`'s reason for Zid says "a different level from Shopify's store currency". Yet Zid's account shows a store-level العملة الأساسية, and Shopify's shows market currencies. `areas.md` is written to the founder and says what a mark would mean ("A store would have one currency", A-31). `record_ids.py` prints the copies' `placement` ("decides", "where"), `bullet` and `conditions`, which are earlier runs' working fields.
*Fix:* add one line: these are the coordinator's or earlier runs' words. They are never evidence, and never the basis for a level or a setter.

**15. Optional. Citations to the entry and to derived paths pass.** Line 93; PLAN risk 14 (line 386).
"the account at a UAE bank, in UAE dirhams. S01-V-526 Q7-SA-K1558" passes (W10). So do `studies/subjects/S-01/entry.md` and `register/...` cited beside a real id (R02). Risk 14 has the checker reject citations to derived or excluded paths.
*Fix:* reject `S01-` ids other than `S01-VP`, and paths under `studies/subjects/`, `register/` and `founder-messages/`.

**16. Optional. Nothing says what to do with a copy found wrong.** Line 22.
The agent reads each list of copies found wrong, but no rule follows. Q7-SH-K1936 can be cited alone (W13), though Shopify's notes give two pages that contradict it.
*Fix:* "Don't rest a point on a copy found wrong or out of date: cite the statement that corrects it, or both, under 'Records that disagree'."

**17. Optional. Q7 isn't told what the plan leaves for the design.** PLAN lines 15 and 27.
The plan names "How far currencies can be set or changed" as an item left open, to come to the founder during the design. Q7's sentence [3] asks exactly that, and nothing tells the draft to keep it open.
*Fix:* add to Q7's message "how far currencies can be set or changed is decided during the design: section 5 keeps it open". Otherwise, record that the coordinator adds it.

**18. Optional. The digest is read whole, before anything is proposed.** Line 25 and step 5.
The digest is 80,029 tokens by the Read tool's count, four reads at its 25,000-token cap, for about 8 facts used. Read at step 5, it stays in context for every turn of writing and fixing (see Cost). Read before sections 2 and 3, it also lets Yemen shape the design, which line 9 says it isn't.
*Fix:* read it after drafting sections 2 and 3, or read "How to read it" and each entry's first line, then whole only the entries that bear.

## Cost

**A drafting run.** Q7's inputs as the brief names them, in tokens. These are estimated at about 3 bytes a token, except the digest, which is the tool's count:

| Input | Size | Tokens |
| --- | --- | --- |
| The system prompt, the brief, the question and its `depth.tsv` rows | | about 25,000 |
| Five accounts | 48 KB | about 16,000 |
| `notes.md` files, read whole to find the lists | 22 KB | about 7,000 |
| Ten areas | 17 KB | about 6,000 |
| Record lookups: 1.0 KB an id on average (measured over the accounts' 511 ids, 497 KB), about 150 looked up | about 150 KB | about 50,000 |
| The digest | 204 KB | 80,029 |
| Stage 1 lookups: 5 to 9 KB an axis (YA-01 9.4, YA-21 8.3, YA-86 6.6), about 10 | about 60 KB | about 20,000 |
| Decision 14, and the agent's own scratch notes, draft and `notes.md` | | about 22,000 |

Over about 90 turns, the context grows to about 130,000 tokens by step 4, then holds about 225,000 for the 40 or so turns from step 5 on. That makes **about 11 to 14 million tokens for Q7**, against about 15 sized, about 3 million of it the digest's.

Q7 is the smallest question. Q2 (788 ids in its accounts) and Q8 (all 34 areas) come to about 15 to 18 million each. **Q5 comes to about 24 to 30 million**, against about 25 sized: 878 ids, 38 KB of areas, about 64 KB of pilot pieces, and a peak of about 300,000 tokens. Taken together, the drafting runs sit at the 130 million sized, with no headroom.

With a 200,000-token window, every run crosses it during step 5, and Q5's by half. A run would then compact, and copy exact quotes from summaries of them. With a 1-million-token window, the runs fit.

**What the drafts hand the later checks, at the brief's limits, for all eight:**

| Kind | At the limits | R5 sized | Rate (sizing.md) | Difference |
| --- | --- | --- | --- | --- |
| Facts | 385, plus 30 for the company decisions | 350 | 0.25 million each | about +16 million |
| Not-found and absent | 59, plus a few | about 60 | 2.7 million each | about +8 million |
| Yemen facts | 68 ids; about 100 facts if an id carries 1.5 places | 60, 15 of them already checked | 1.25 million each | +10 to +50 million |
| "Doesn't show" | no limit; 3 to 8 a draft, so about 25 to 65 | 15 | 2.7 million each | +27 to +135 million |
| "Not in what was read" without its row | not counted (finding 7) | | | never checked |

At these figures, R5 comes to about 410 to 555 million, against the 346 million sized (88 + 162 + 96). The "doesn't show" claims are most of the gap. A limit of about 2 a draft (finding 8) brings R5 to about 385 to 425 million. Limits in R5's own units (finding 9) bring it to about 360 million.

## The coordinator's fixes

**19 October 2026.** Each finding, and what was done (`briefs/R4-drafting.md` and `check_proposals.py drafts`). The check's own test drafts were run again on the fixed checker: each wrong point it named is now caught, and its good draft still passes.

- **1. Fixed.** Sharrwah is set up "for each place it serves"; what a place is, and the level at which things differ, come from the evidence. The deferral reads "not even for one place". Section 3 names no level.
- **2. Fixed.** Q5 and Q7 no longer read the entry. The brief lists each decision's topic with its variation point, worded to presume no holder and no level, and the runs read only the variation points' `vp_id`, `question` and `x_words`. Section 8 is written after sections 1 to 6. The entry's framings and recommendations reach the proposal when the coordinator finishes it.
- **3. Fixed.** Both open findings, 36 and 29, are stated in the brief, in its own words, for Q5 and Q7.
- **4. Fixed.** "among your question's copies, as `P` ids", with `grep -F` in the question's own `copied-view.tsv` for pilot statements no account cites.
- **5. Fixed.** Like with like is within one of the four kinds `source_kinds.py` gives; a mixed comparison names its kinds. The tool's kind for Shopify's Admin GraphQL schema is left for the coordinator, since changing a rule changes earlier records' kinds.
- **6. Fixed.** Quotes and Arabic are checked only against platforms' and Stage 1's records. A variation point counts as an id only in section 8.
- **7. Fixed.** A point saying a reading didn't show something must cite a not-found row or copied gap, outside section 6 and "not checked on" points. Section 1 asks for such points only where the proposal rests on them.
- **8. Fixed.** One rule: "doesn't show" only where an element's set-up for Yemen depends on a fact the digest doesn't give. At most about 2 (Q5 about 3), with a warning past that.
- **9. Fixed.** Facts at most about 40 (Q5 about 60). Yemen facts are counted by axis or constant and place.
- **10. Fixed.** "absent" is skipped inside quotation marks and where a point cites no platform record.
- **11. Fixed.** A section 4 part with no id names its elements in bold; a section 6 point with no id may not say "allows" or "forbids"; a Yemen fact's date is checked in every section, beside its id.
- **12. Fixed.** Single quotation marks are checked; an id in quotation marks is an error; the brief's Yemen example is written without quotation marks.
- **13. Fixed.** The headings are given literally; pairs of sentences are adjacent; an element's own line ends with its ids; section 8's points cite the decision's variation point.
- **14. Fixed.** One paragraph: `depth.tsv`'s reasons, `areas.md`'s text and the copies' working fields are earlier words, never evidence, and never the basis for a level or a setter.
- **15. Fixed.** The checker rejects `S01-` ids other than variation points, and paths under `studies/subjects/`, `register/` and `founder-messages/`.
- **16. Fixed.** A copy found wrong or out of date is cited only with the statement that corrects it.
- **17. Left to the coordinator.** How far currencies can be set or changed is an item the plan leaves to the design. The coordinator adds it to Q7's section 5 when finishing, so that no founder's item reaches a run.
- **18. Fixed.** The digest is read once, after sections 1 to 5, so that Yemen's evidence tests the design rather than shaping it, and stays out of the context for most of a run.
