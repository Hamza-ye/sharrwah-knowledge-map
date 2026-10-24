# Check of the R5 brief and the company decisions' brief, before they run

**An inspection (Fagan 1976), 24 October 2026, at `max`,** of `studies/proposals/briefs/R5-checks.md` with `method/r5_cards.py` and `method/check_r5.py`, and of `studies/proposals/briefs/R4-company-decisions.md` with `method/check_proposals.py decisions`, at commit `b0f0998`. Trial files are in `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/R5-brief-check/` (`cards/`, `cards-all/`, `trial/`, `decisions/`, `scripts/`).

Three commits landed while I worked: `3d56eac` (sizing re-sized after the drafts), `77c4849` (Q7's draft revised) and `20ef4f7` (`r5_cards.py --quotes`). The briefs and the two check scripts are unchanged since `b0f0998`. I judged the scripts as they stand at `b0f0998`, counted Q7 at `77c4849`, and compared costs with both sizings.

## What I read and what I ran

**Read:**
- the two briefs; `r5_cards.py`, `check_r5.py`, and `check_proposals.py` (its `decisions` mode, its `drafts --cited`, and the rules both share);
- the tools the runs call, as far as the briefs use them: `record_ids.py`, `quote_check.py`'s `web_texts`, `warc_text.py`, `source_kinds.py`, `corpus_search.py`'s usage;
- `PLAN.md`: section 4's R4 bullets ("The coordinator finishes each proposal", "Company decisions") and Step R5; section 6's rules on "not in what was read" and "absent" and on Yemen; section 11's 19 October entries on the citing counts;
- `sizing.md`: its R4 and R5 rows and how it counts tokens, and the re-sizing added in `3d56eac`; `costs.tsv`'s measured runs;
- every draft's section 7 (Q1 to Q8), Q4's sections 5 to 7 in full, the "doesn't show" points of all eight, and the points named below;
- Stage 1's files and the digest, as far as the Yemen trial needed.

I did not read `STATE.md`, `founder-messages/` or other studies.

**Ran** (all with `python3 -I`, from the repository root; outputs written only to the scratch directory):
- `r5_cards.py Q4 --out …/cards`: 49 seconds. 98 fact cards in 5 files, 4 claim cards, 10 Yemen cards.
- `r5_cards.py Q1 Q2 Q3 Q4 Q5 Q6 Q8 --out …/cards-all`: 211 seconds. 886 fact cards in 35 files (32 to 259 KB each, about 950K tokens in all); 47 claim cards; `yemen.md` with 50 cards (467 KB, about 124K tokens).
- `check_proposals.py drafts Qn --cited` for all eight drafts (Q7 after `77c4849`). The drafts cite 972 facts (86 to 183 each), 53 not-found rows, copied gaps and absences, 115 Yemen facts by id and place (55 ids), and 16 "doesn't show" points.
- **A facts trial on Q4 on Shopify (8 of 21 cards),** checked with `check_r5.py`, with 18 wrong rows seeded:
  - 3 `holds` (Q4-SH-059, 027, 016);
  - 5 `fix point`: K1740 at Q4:29, 026 at Q4:135, 022 at Q4:73, 062 at Q4:76 and Q4:108, K1491 at Q4:156.
- **An absence trial on Shopify (2 cards),** with three seeds:
  - Q2-SH-A0002 `found`;
  - Q4-SH-N01 `holds`. Its one `corpus_search.py` call took 93 seconds and printed 38 KB, about 9,500 tokens.
- **A Yemen trial (YA-56, YK-203 and the point Q4:146),** with five seeds:
  - YA-56 and YK-203 `fix point`;
  - Q4:146 `holds`, after three `rg` searches of Stage 1's files and `evidence/yemen/` (13 seconds each).
- **A company decisions trial:** D1, where the company is based, from Q1:140, Q2:136, Q4:159, Q5:167, Q6:112 and Q8:190, with its records and source kinds. I checked it with `check_proposals.py decisions` and seeded 15 wrong points.
- Scripts of my own, in `scripts/`:
  - statistics over all fact cards;
  - a comparison of every cited Yemen fact with the digest: in all eight drafts, 155 of 156 match as written; YK-200 adds "the" to its place;
  - counts of duplicates, plan notes, observed sources, claim kinds and section 6 wording.

### What the trial found in the drafts (for the coordinator; the R5 runs would find them too)

- **Q4:29:** it gives Shopify's "you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers" without the sentence's condition, "When you use Shopify Payments". The card's context shows that condition (Q4-SH-K1740). The record's scope is empty too.
- **Q4:135:** it says "Shopify converts it at the live rate". The source makes that conditional: "If you use international sales tools, then the value for **Amount received** is … converted" (Q4-SH-026).
- **Q4:73:** it says "Shopify records part payments on its Shopify Plus plan". The page limits the feature to "orders with payment terms" in its introduction, outside the card (Q4-SH-022).
- **Q3:17 and Q2:11:** the pilot absence's list (captured 12 October) has 40 countries. The supported countries page held at observed-sh `c8b5fbee` (pages dated 16 October), and at `febbf6c9`, lists 41, with "Shopify Payments for China" at line 19. Q3:17 says "beyond the 40". Yemen is in neither list (Q2-SH-A0002, Q3-SH-A0002).

### Where the cards held, and where they misled or left a check unsettled

- **Settled by the card alone:** Q4-SH-K1740, K1491, 027, 016 and 026, from the context. Q4-SH-062's plan came from the step's title, "capture plus · Companies · New company · Shopify Plus", and its intent, "visit route company:create (path from router)".
- **Q4-SH-022 was left unsettled:** the plan note and "for orders with payment terms" sit at the top of the page, outside the 450-character context. I opened the source (finding 13).
- **Q4-SH-059 and 062 were left unsettled:** their points say what the accessibility tree holds, and the card names no `aria.yaml`. I found `steps/006.aria.yaml` and `steps/174.aria.yaml` with `git ls-tree` (finding 13).
- **Q4-SH-026 would be misread under the brief's rule:** its statement runs past its quote, though the context shows it is the source's words (finding 2).
- **Q2-SH-A0002 misled:** its list quotes are from 12 October and the list has since grown. It has no completeness words, and `record_ids.py S01-SH-C146` answers "not found" (finding 4).
- **YA-56 needed lookups:** I had to run `record_ids.py` on its 7 conditions and grep the digest. The card gives neither (finding 14).
- **YK-203 was left unsettled by the brief, not the card:** whether "available to business accounts" lets the point say "allows" (finding 9).
- **Q4:146 has no card:** `rg -i IBAN` also matched "Kuraimibank" and "kibanks" until I added word boundaries (finding 14).

### Cost

The original sizing for R5 is 389M: 88 for facts, 162 for absences, 96 for Yemen, 25 for re-checks and 18 for brief checks. The re-sizing in `3d56eac` puts it at about 275M: 120, 60, 45, 30 and 20. The decisions run was sized at 10M and re-sized to about 20M. From the trial and the card sizes:

- **Facts: 972 cards in 40 runs**, 2.8 times the sizing's 350.
  - Most cards are settled without opening a source: every quote is found by script, 1,287 found and 46 found with markup removed. In the trial 3 of 8 cards needed a source opened.
  - By a model of each turn re-reading the run's context (in `scripts/`), the 40 runs come to about 90M if about 30% of cards need a source opened and to about 165M if half do. That makes the re-sizing's 3M a run plausible.
  - The largest files (Q1 on Shopify, 56 cards, about 50K tokens; Q5 on Shopify, 51; Q3 on Zid and on Salla, about 62K tokens each) would take 6 to 13M each.
  - Finding 2's rules, left as they are, push toward the top of the range.
- **Absences: 53 cards (50 by origin):** Salla 17, Zid 13, Shopify 11, WooCommerce 6, BigCommerce 6.
  - At A3's measured 2.7M a claim, about 140M. The re-sizing's 60M holds only at about two searches and three documents a card.
  - It also needs Salla's run split: at those numbers Salla's run alone carries about 0.5M tokens of search output and documents (finding 7).
- **Yemen: 55 ids and 16 points:** about 50 to 110M, against the re-sizing's 45. The cards are large (finding 14), and each card needs the digest, conditions and places looked up.
- **The decisions run:** about 10 to 20M at `max` for about 180 section 7 ids, plus a few for finding 6's extra reading.
- **Cuts that lose no check:**
  - finding 2's rules;
  - each copied record checked once (finding 15: 79 fact cards, 3 claim cards);
  - Yemen cards deduplicated and given what steps 1 to 3 need (finding 14);
  - Yemen step 1 done by script (finding 9);
  - absence runs capped at about 9 cards, each searching the observed runs first (`--runs-only`) where a row is about what a store's admin shows (finding 7);
  - page leads and `aria.yaml` paths on fact cards (finding 13);
  - the decisions gathered after R5's record fixes, so that R5 checks only their points (finding 1).

## What holds

**R5:**
- **The scope matches PLAN.md's step R5 for the drafts:** facts, absences batched by platform and audited by an agent that made none of the claims, Yemen facts with later states, and "doesn't show" points.
- **The rules repeat section 6's:** languages, `--with` for named countries, plans and arrangements, `absent` only from a complete list, and Stage 1's reading rules.
- **The cards work.** Every fact card has its citations, its kind, its quote check and the quote in context, with title and headings where the source has them. Observed steps carry intent, address, title and time.
  - The context settled most of my trial and exposed real points: Q4:29, Q4:135 and Q4-SH-062's plan.
  - The explanation of saved-markup step text and ⟦hidden⟧ is right.
- **The brief keeps runs from fixing anything:** lines 14 and 83 ("You check and record", "You suggest; the coordinator decides").
- **Snippets are never quoted** (line 51). The kinds of source and the observed-store rule are named (lines 32 and 33).
- **The line-42 instructions open what they name.** `git -C … show` works for observed-sh, observed-sa and this repository. `warc_text.py REPO_ROOT WARC_PATH@OFFSET` matches its own usage. Live addresses are found through the capture runs' `manifest.tsv`, as `quote_check.py` does.
- **`check_r5.py` catches malformed files:** header, field count (a tab in a field), unknown verdicts, empty `what`, `fix point` without lines, malformed lines, unknown or duplicate ids, and cards with no row.
- **The read-only, `python3 -I` and credentials rules are present.**

**R4's company decisions:**
- **It matches the plan's bullet,** and it decides and recommends nothing.
- **It is neutral:** each decision is "one question that presumes no answer", and the holding of sellers' money is "the founder's decision: gather its evidence like any other".
- **Its rules are sound:** the platforms' own words, word for word; scoped as the sources scope them; "not in what was read" and "absent" only with their rows; Yemen facts with their dates; no searches and no new sources.
- **`source_kinds.py` gave every D1 source as `official page`.**
- **The decisions checker caught** an invented quote, a draft's words quoted as a platform's, Arabic not in the records, "not in what was read" and "absent" without their rows, an unknown id, a point with no id, and the decisions' headings.

## Findings

### Must fix

**1. R5 leaves out the company decisions, and the decisions are gathered before R5 fixes the records they repeat.**
- **What the plan asks:** PLAN.md step R5: "Once a proposal or company decision is drafted, and before its review, … everything it cites gets the full checks". `sizing.md`'s R5 rows count "30 for the company decisions" and "a few for the company decisions".
- **What the brief and scripts cover:**
  - The brief (lines 9 to 12) covers only the eight drafts.
  - `r5_cards.py` reads only `drafts/<Q>/<NAME>` (line 35). `cited()` drops every id of another question (line 65). `sections()` knows only `## N.` headings.
  - `check_r5.py` names lines only as `Q1:9` (line 15).
- **Tried:** passing my D1 file to `--file` as an absolute path makes cards, but:
  - every point reads "section 0";
  - the header path is garbled;
  - one decision's 12 records scatter over 12 one-card files;
  - a row's `Q1:9` can't say which file its line 9 is in.
- **The decisions brief (lines 20 and 21) reads the drafts and records as they stand.** So the trial's Q4-SH-K1740, without "When you use Shopify Payments", and the 40-country list would pass into the decisions unchanged.
- **Fix:**
  - Start the decisions run after R5's facts and absence runs and the coordinator's fixes to records.
  - Give `r5_cards.py` a mode for one file citing any question's ids, naming points `D3, line 12`, and let `check_r5.py` accept `D3:12`.
  - In the R5 brief, add a short run kind for the decisions' points. It checks each point against records that already have a row, and opens a record only where none does.

**2. Facts step 3's rules for a record contradict how records were made, and will produce false `fix record` rows at scale.**
- **The rule (line 35):** "its statement is the quote or a part of it; its identifier names what the source names".
- **How records were made:** the recording checker requires a statement verbatim in its first cited source, and caps a quote at 300 characters (`check_proposals.py` lines 272 and 316).
- **Statements:** 135 of 886 fact cards (101 statements, 34 copies; 93 of them over 300 characters) have a statement longer than any one of their quotes, though the source holds it.
  - Q1-SA-095's whole sentence is on line 180 of Salla's terms; its quote stops at the first clause.
  - Q4-SH-026's first sentence is in its card's context.
- **Identifiers:** 395 of 886 have an identifier the card's quotes, context, title and headings don't hold. Most are the recorder's labels:
  - "transaction fees paragraph" (Q4-SH-K1740);
  - a URL (Q4-SH-K1737);
  - "Settings > General > Switch business details" (Q1-SH-114);
  - API fields and translation keys.
- **With line 95** ("When unsure between holds and a fix, choose the fix"), runs would write these up as fixes or open a source for each.
- **Fix:**
  - Statement: "its statement is the source's words, word for word: the quote, or the quote with the text around it (the card's context shows it; open the source where it doesn't reach)."
  - Identifier: "the identifier is the recorder's label; it is a finding only where a point uses it as the platform's term, or where it names something other than what the source describes (another product, plan, place or party)."

**3. The later-state check (Yemen step 3) can't be done as written.**
- **The rule (line 62):** "Only a state whose source says it holds in all of Yemen ("across Yemen") contains every place."
- **How such states appear:** `places.tsv` groups both "Yemen" (the place of 670 conditions) and "across Yemen" under "place not stated", by rule. So `axes.tsv` and the digest show such states "@ place not stated" (270 states in `axes.tsv`). Only YK-494 and four wallet-network states keep the words "across Yemen".
  - A run looking for "across Yemen" passes over the rest.
  - A run treating every "place not stated" as all of Yemen over-reaches.
- **The brief also doesn't say what "contains" means.**
  - `places.tsv`'s `grouped` column mixes spellings of one place with membership by source ("CBY-Aden's area" in "the internationally recognized government's area").
  - The brief doesn't say that geography counts for nothing: Sana'a is not in "Houthis' area" unless a source puts it there.
- **Fix:**
  - State the containment rule: "A later state counts at your place if it is at the same place (a place and the places `places.tsv` groups in it are one), or if it is '@ place not stated' and its quote says it holds in all of Yemen. Read the quote of each later 'place not stated' state of the same axis or constant. Never by geography."
  - Say that an undated state (such as YQ-D621's) can't be judged later or earlier: say so in `what`.

**4. A pilot absence's card lacks the words that make its list complete, and the list it gives can be out of date.**
- **What the absences steps ask:** step 1 (line 49) and step 4 (line 52) need the list and "the words that make the list complete".
- **What is cited:** all five `absent` claims are pilot absences (Q2-SH-A0002, Q3-SH-A0002, Q5-SA-A0002, Q5-WC-A0002, Q5-ZD-A0002). No not-found row of kind `absent` is cited.
- **Why the card lacks them:**
  - `record_ids.py` adds `complete_cite_ids` to what a record rests on only for `not-found.tsv` (lines 73 to 75); a pilot absence gets only `list_cite_ids` (`CITES`, line 46). So `claim_card` (`r5_cards.py` lines 227 to 236) prints the five list citations and not S01-SH-C146 and C147.
  - `record_ids.py S01-SH-C146` answers "not found", though `records/Q2/shopify/copied-citations.tsv` holds both (lines 1321 and 1327).
  - `--quotes` (`20ef4f7`) reads the same list, so these quotes go unchecked by script too.
- **The trial shows the list must be read as held now:** the held page lists 41 countries, China among them, where the row's list has 40.
- **Fix:**
  - In `record_ids.py`, include `complete_cite_ids` for `copied-pilot-absences.tsv`, and have the card label each citation "list" or "complete".
  - Let `record_ids.py` resolve an original's id (`S01-…`, `SH-S-…`) to its copy.
  - In step 4, add: "read the list's page in its latest held copy (the search lists it) and compare it with the row's list."

**5. The company decisions' brief and checker leave out evidence the drafts tie to decisions outside section 7.**
- **The reading rule:** line 20 reads section 7 and the points citing its ids; "the rest of a draft only where a section 7 point refers to it".
- **Section 5 points left out:** these name a decision or the founder and share no id with section 7.
  - Q2:117: "Settled by the company decision on partners", with Q2-SH-064, 072, 073 and YA-62.
  - Q8:170: "settled by the company decision on pricing" (Q8-BC-009).
  - Q5:129 and Q6:89: "The founder settles it", "the founder settles each place".
  - Q5:132: "The providers chosen for each place (section 7) settle it".
- **Section 6 points left out:** the "doesn't show" points that bear on the licence decisions are not read either:
  - Q4:150: whether collecting cash for sellers needs a licence;
  - Q5:150: what a licence requires at the Houthis' area;
  - Q5:155: which central bank licenses wallets;
  - Q8:185: whether collecting app charges is a licensed service.
- **`evidence.md` has no part for them:** the decisions checker errors on any point with no id but "Raised by" and "Bears on" (`check_proposals.py` lines 346 to 356), unlike the drafts mode's exception for section 6 (lines 538 to 549).
- **Fix:**
  - Read also section 5's points that a company decision or the founder settles, and section 6's "doesn't show" points, with their ids.
  - Add a part "Yemen's evidence doesn't show", each point naming its draft line (Q4:150), and exempt it in the checker as the drafts mode does.

**6. A Yemen run on a part of `yemen.md` can't pass `check_r5.py`, and nothing checks that every "doesn't show" point has its row.**
- **The brief:** line 59 ("or the part of it the message names"), line 68 (`<part>.tsv`) and line 86 (run `check_r5.py` before finishing).
- **The checker:** it takes every `### ` of the card file (line 22) and reports each card with no row (lines 51 to 53). My three-row trial on Q4's `yemen.md` drew 8 such problems. A part run can clear them only by doing other parts' cards, or must finish with errors.
- **"Doesn't show" points:** line 40 accepts any `Q1:9` to `Q8:9` id, in any kind of run, and nothing lists the points a run must answer. My seeds `Q4:143` (a point that is not "doesn't show") and `Q4:999` passed.
- **Fix:**
  - `r5_cards.py` writes the Yemen cards in parts (`yemen-1.md` and on, about 40K tokens each).
  - Give each section 6 "doesn't show" point a card of its own (`### Q4:146`, with its text), taken from what `drafts --cited` already computes.
  - `check_r5.py` then needs no exception for `Q:line` ids.

**7. Runs as batched can outgrow one context, and the brief has each write its file only at the end.**
- **Absences:** line 50 allows three searches a card and line 51 five documents. One Shopify search printed about 9,500 tokens.
  - Salla's run has 17 cards. At even two searches and three documents a card, it carries about 0.5M tokens of output by its end. Zid (13) and Shopify (11) carry about 0.3M.
  - A3's audits held about 9 claims a run.
- **Facts:** the files for Q1 on Shopify (56 cards) and Q5 on Shopify (51) start at about 50K tokens.
- **The risk:** a run that compacts its context loses the quotes it gathered, and its cost grows with the square of its length.
- **Fix:**
  - Lines 44, 55 and 68: write each row to the file as soon as its card is done.
  - Cap an absence run at about 9 cards, and split Salla's.
  - Make the first search `--runs-only` where the row is about what a store's admin shows.
  - Run searches with `--max 5`.

### Should fix

**8. Facts step 2 states as given what a run must check, and leaves out two kinds of source the cards hold.**
- **The wording:** line 31's "It is the platform's own material, of the kind the card gives, dated as given" reads as a fact, as do lines 10 to 12.
- **Incorporated agreements:** 28 citations on WooCommerce's cards are Stripe's (`stripe.com/legal/ssa` 21, `ssa-service-terms` 6, `connect-account` 1). Section 6 counts an agreement a platform's terms incorporate as part of its terms. Without that rule, a run flags them, or passes them without checking the incorporation.
- **Observed sources without a store:** 35 observed citations are Salla's dashboard translations (such as Q2-SA-K1653), with no store. "An observed record said with its store and date" (lines 33 and 39) can't be met for them.
- **Fix:**
  - "Check that it is …".
  - Add: "another company's agreement counts as the platform's only where a record shows the platform's terms incorporate it (PLAN section 6); else `open`".
  - Add: "an observed source that is not a store's step, such as the dashboard's strings, is said with its date as what the dashboard held then".

**9. Yemen step 1 presumes its answer, and step 5's "allows" rule meets the drafts' own usage.**
- **Step 1 (line 60):** "They are the digest's for that id" is the check, written as given. By script, 155 of the 156 parts the eight drafts cite match the digest as written; Q3:156's YK-200 has "the Ministry", where the digest has "Ministry". So the card can carry the match, and the run checks only a mismatch.
- **Step 5 (line 64):** "'allows' or 'forbids' only where the fact's state does".
  - 53 of the 67 section 6 points citing a Yemen fact say "allows", "allowed" or "forbids", mostly from states such as "available", "in use" or "accepted". For example, Q4:143: "Cash on delivery is allowed and in use: the store offers it inside Sana'a".
  - PLAN's R4 bullet frames section 6 as "what Yemen's evidence allows, forbids or doesn't show".
  - Read strictly, the rule gives about 50 `fix point` rows; read loosely, none. Two or three runs may split.
- **Fix:**
  - Do step 1 by script, on the card.
  - Decide and state the reading. For example: "a state showing a practice (offered, available, in use) supports 'in use at <place>, as of <date>'; 'allowed' or 'forbidden' needs a state that permits or forbids".

**10. One row and one verdict per card can't carry two findings.**
- **The rule:** lines 74 to 80; `check_r5.py` lines 37 to 39 make a second row an error.
- **Cases it can't carry:**
  - A card can need both `fix record` and `fix point`: Q4-SH-K1740's scope lacks the condition, and Q4:29 repeats the omission.
  - A card can hold at one place and have a later state at another: YA-62 is cited at three services.
- **Fix:** give a precedence (`fix record`, `later state`, `found`, `fix point`, `open`, `holds`), with every affected line in `lines` and `what` naming each finding. Or allow one row per verdict.

**11. `check_r5.py` misses wrong rows that would send a fix to the wrong place.** The following seeds passed:
- a line the card is not cited at (Q4:7 for Q4-SH-061);
- a line of another question (Q5:22 in a Q4 file);
- a line past the draft's end;
- `later state` or `found` in a facts run, and `later state` in an absence run;
- a `Q4:146` row in a facts file;
- `fix point` with an empty `fix`;
- `found` or `later state` with no lines;
- `holds` carrying lines and a finding;
- an absence row with no search in `read`.

**Fix** (lines 40 to 50):
- Require each line to be among the card's "Cited at" lines.
- Take the run's kind from the card file's name and allow only its verdicts: facts `holds`, `fix point`, `fix record`, `open`; absences add `found`; Yemen adds `later state` and `found`.
- Require `fix` on fix rows, and `lines` on every row but `holds` and `open`.
- In an absence file, require `corpus_search.py` in `read`; in a Yemen file, require `rg` in `read` for each point.

**12. The decisions checker raises one false alarm, under-enforces one rule, and misses five checks.**
- **False alarm:** the opening line the brief asks for (line 31, "starts with a line saying what it is") fails as "a point that cites no record" (`check_proposals.py` line 355). My D1 passed only once I made it a `#` heading.
- **Under-enforced:** a Yemen fact without its date is only a warning (line 380), and the brief (line 43) asks the run to fix errors.
- **Not caught** (seeds):
  - a Yemen fact with a wrong place and date (`YK-12 (split @ Aden, as of 2019)`), or with no place;
  - one platform's quote given to another platform;
  - a record no draft cites (Q7-WC-001);
  - "wasn't found" without a row: `NOT_SHOWN` (line 466) has no "found", and Q6:17 and Q6:91 say "was not found";
  - a section 7 point left out of every decision, which nothing checks.
- **Fix:**
  - Skip text before the first `## D` heading.
  - Make an undated Yemen fact an error in this mode.
  - Compare each `Y?-NN (state @ place, as of date)` with the digest's part (my `scripts/yemen_vs_digest.py` shows how), and require "@".
  - Check that each id is cited by a draft or named by a cited record.
  - Add "found" to `NOT_SHOWN`, in both modes.
  - Check that every draft's section 7 line appears in a "Raised by" line or in `notes.md`.

**13. Fact cards lack what some checks need, and one source can't be opened as line 42 says.**
- **Page-level limits:** the context is 450 characters each side (`r5_cards.py` line 41).
  - Of 118 cited Shopify Help Center citations, 9 are on pages with a plan note at the top, and 7 of those notes fall outside the card. Examples: Q4-SH-022, "This feature is available to stores on the Shopify Plus plan."; Q1-SH-043, "Business entities are available on the Plus plan only."; Q8-SH-044; Q2-SH-032.
  - In 6 of the 7 the record's scope is empty.
- **Accessibility trees:** points such as Q4:21 and Q4:27 say what a step's accessibility tree holds. The card names no `raw/runs/<run>/steps/NNN.aria.yaml`.
- **WooCommerce release:** 28 citations name `woocommerce-11.2.1:<path>`. That is a folder (`/home/user/woocommerce-release/11.2.1/woocommerce`, `check_proposals.py` line 66), not a repository at a commit, so `git -C /home/user/<repository> show <commit>:<path>` fails.
- **Fix:**
  - Add to each fact card the source's lead (its first 400 or so characters after the title) and its note boxes.
  - For a step, add the paths of its `aria.yaml` and text files.
  - Name the release folder in line 42.

**14. The Yemen cards are larger than they need to be, miss what steps 1 to 3 read, and the "doesn't show" search is unguided.**
- **Size:** `yemen.md` for seven drafts is 467 KB, 113 KB of it citations printed twice. `record_ids.py` lines 93 and 94 add each state's citations after `today_cite_ids`. Each axis card also prints every state's quotes, at places no point cites.
- **What it lacks:**
  - the digest's part (step 1);
  - the conditions' rows (step 3). YA-21 has 12 condition ids, and `record_ids.py` prints each with all its citations;
  - the place's group (step 3).
- **The "doesn't show" search (line 66) is unguided:**
  - `rg -i IBAN` hits "Kuraimibank";
  - `cases.tsv` has 345 lines over 20,000 characters (up to 65,100);
  - raw HTML lines are long;
  - `rg` folds no Arabic letter forms.
- **Fix:**
  - Deduplicate the citations.
  - Print in full only the cited part's citations and any later state's; give other states one line each.
  - Add the digest part, the conditions without citations, and the place's group.
  - In line 66, give the form `rg -i -l` then `rg -i -o '.{0,150}\bTERM\b.{0,150}'`.
  - Name the files to search: Stage 1's main TSVs and `text.txt`, not `cases.tsv`, `pass1/`, `pass2/` or `raw*.html`.
  - Write Arabic letters as classes: `[اأإآ]`, `[هة]`, `[يى]`.

**15. A copied record cited by several questions is checked in each.**
- **Fact cards:** 59 copy rows are cited by more than one question, so 79 of 886 fact cards repeat one. WC-K0402 appears five times; SH-K1243, WC-K0054 and BC-P0048 four times each.
- **Claim cards:** SH-A0002, SA-G0213 and ZD-G0055 each appear twice.
- **Fix:** mark each repeat "record checked in <file>", so that later runs check its points only. Group a claim's copies into one card with every "Cited at".

**16. PLAN's "What no proposal cites is recorded as read, without audits" has no owner.** Neither brief nor script lists the records no draft cites. **Fix:** `r5_cards.py` writes `uncited.tsv`, every record id no draft or decision cites, for the coordinator to record as read.

**17. The decisions brief points to originals its tools can't reach.**
- **The rule:** line 25 allows a record "where a cited record names it (such as a copy naming its original)".
- **The tools:** line 21's `record_ids.py` answers "not found" for S01-SH-096, held as Q2-SH-P0097. Line 25 forbids `studies/subjects/`.
- **Fix:** as in finding 4, resolve an original's id to its copy. Or tell the run to grep `records/<Q>/<platform>/copied*.tsv`.

### Notes

**18. Two phrases in R4's list lean toward an answer.**
- **Line 10's "which company contracts with sellers at each place"** presumes a contract at each place. Suggested: "whether one company or several contract with sellers, and what decides which".
- **Line 12's "would need"**: suggested "needs, if any".

**19. `--quotes` (`20ef4f7`) answers the plan's "every quote is checked by script" for records, with two gaps.**
- It inherits finding 4's gap.
- It writes a row for each repeated Yemen citation.

The runs' own quotes in `what` and `fix` are not checked by script. The drafts checker would catch a fix whose quoted words are in no cited record.

**20. Absence step 3 doesn't send the run first to the pages a row's `route` or `read` names as held.** Section 6's rule on gaps asks for that. The search usually lists those pages, but not always.

**21. Line 42's "at most 80 lines a time" doesn't bound a one-line JSON answer.** Add "or `grep -o '.{0,300}WORDS.{0,300}'`".

**22. The counts.** All counts above are for seven drafts unless they say eight. Q7's revision (`77c4849`) adds:
- 86 fact cards;
- 6 claim cards (Salla, Shopify 2, WooCommerce, Zid 2);
- 14 Yemen facts by place;
- 2 "doesn't show" points.
