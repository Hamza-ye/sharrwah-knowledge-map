# Check of the R1 review brief

**18 October 2026.** A check of `studies/proposals/briefs/R1-areas-review.md` before it runs, by an agent that wrote none of it. The brief is read at commit `7fec7f0`. HEAD moved to `681df43` during the check. The brief, `method/check_areas.py`, `method/place_entries.py`, `questions.md` and `PLAN.md` are the same there. Two things the brief relies on changed:
- the name rule in `method/areas_extract.py`, in `66c457a` (finding 7);
- the copy script, which became two-phase in `681df43` (finding 13).

**What I read:**
- the brief, and its diff since the re-check (`git diff fc98f4b..7fec7f0`);
- `PLAN.md`: step R1, section 6, and the lines of sections 1 to 3, 7 and 9 that the brief's wording rests on;
- `method/check_areas.py`, and the two scripts it depends on or follows: `areas_extract.py` (its `own_names`) and `place_entries.py`. I also read the docstring of `copy_statements.py` at `681df43`, the script that acts on the `questions` column;
- `studies/proposals/questions.md` and `briefs/R1-areas-one-platform.md`;
- `check-of-the-draft.md`: findings 26 to 33 (31 and 32 among them), 43 and 44, and the Re-check;
- `sizing.md` and `costs.tsv`, for the review's expected cost and the runs' measured costs;
- the recorded data the brief names, for their columns and counts: the concern map's `concerns.tsv`, `statements.tsv`, `inventory.tsv`, `citations.tsv`, `gaps.tsv` and `fetch-log.tsv`, and the pilot's `statements.tsv`.

**What I didn't read:** `STATE.md`, `founder-decisions.tsv`, the founder's messages, and what the platform runs and the coordinator wrote. Of their files I took only sizes, the commit messages, and the checker's one-line summary for the four platforms first committed.

**How.** I used scripts of my own, in my scratch directory, run with `python3 -I`. They:
- ran `check_areas.py merged`, as committed, on 13 test files built to the brief's column spec;
- ran `check_areas.py` on the four platforms committed at `9b359b2`;
- counted the volumes, the out-of-scope entries, and the citations by where their sources are held.

I tested held sources with `git --git-dir ... cat-file`, from outside the observed repositories. Nothing ran in `evidence/` or in the observed repositories. No file but this one was changed.

**In short:** 13 findings, 3 of them must fix:
1. The reviewer reads the founder's items and the founder's expected answer to Q7, because the brief gives it all of `questions.md`.
2. "Nothing lost" now means Sharrwah's whole extent. But the brief doesn't say whether the 411 entries the concern map put out of its scope count, and the step has no way to place them.
3. Nothing tells the review to look for our words or the founder's in the list the founder marks.

## What changed since the re-check

- **Finding 31** (the review couldn't read the recorded data): fixed. The concern map's `concerns.tsv` and `statements.tsv`, and the pilot's statements, are on the list. The route to a cited source still lacks `citations.tsv` (finding 5).
- **Finding 32** (the merged files unspecified): fixed. The columns are given, and `check_areas.py merged` checks them. Separators and value forms are missing (finding 6).
- **Finding 44** ("none"): settled by the go. A depth is `in depth` or `check`, and check 1 runs the merged check without `--cuts`. My test confirms that the checker then rejects "none". Check 8's "none" bullet went with it. Brief and checker agree.
- **The go's two additions:** the opening sentence of check 3, and the severity's new clause. They widen what counts as lost without widening the checks under it (finding 2). They also give "leave out" two meanings (finding 9).

## Findings

### 1. The reviewer reads the founder's items and the founder's expected answers

- **Where:** "Read only", second bullet (`studies/proposals/questions.md`); checks 5 and 8.
- **The problem:**
  - The brief gives the reviewer the whole file, not only the eight questions.
  - Beside each question, the file gives the founder's item in the founder's words. For Q7 it also gives the founder's expected answer.
  - Checks 5 and 8 ask the reviewer to judge what bears on each question, and whether a checked platform suggests an answer the in-depth platforms might not show. Those are the judgments these lines would tilt.
  - PLAN.md section 6 says agents get section B's items "only as the neutral questions".
- **The evidence:**
  - `questions.md` line 79: "The founder expects one store currency to be the platforms' norm, and asks the work to confirm or correct that. The question doesn't say so, so as not to lead the agent." The reviewer is an agent. For Q7, check 8's test of "an answer the in-depth platforms might not show" would be made against this expectation.
  - Line 30: "The founder's item: B2, 'rules land as availability, not as design'." The earlier check found that this expectation, written into Q2, led toward "availability" (its finding 18). It also found that a line beside the questions steers "the R1 reviewer, who reads `questions.md`" (finding 43). Only the tax line was removed.
  - Lines 20, 36, 44, 52, 69 and 85 give the other items in the founder's words. One is B5's "Sharrwah chooses which payment methods are offered", which the earlier check found built into Q5's first wording (its finding 21).
  - PLAN.md line 300: "Agents get section B's items only as the neutral questions in `studies/proposals/questions.md`."
- **The fix:**
  - Give the reviewer only the eight questions as quoted, that is the blockquotes under Q1 to Q8. Put them in the brief, or in a file that holds only them, made by script from `questions.md` so the wording can't drift. R3's runs will need the same file.
  - Q8's note that "much of this comes from the areas list" is neutral and can go with Q8. Its line on the second cut is out of date, since no cuts were taken.
  - `areas.md` is written for the founder and may name the founder's items. Either ask the coordinator to name questions by number and by `questions.md`'s section titles, or have the reviewer read `areas.md` only after it has done checks 5 and 8 from `areas.tsv` and `depth.tsv`.
- **Severity:** must fix.

### 2. "Nothing lost" now means the whole extent, but what it counts is unsettled, and the script places only in-scope entries

- **Where:** check 3: its new opening sentence, "Every inventory entry is placed", and "Legal, place and eligibility matters each have an area wherever the extracts show them"; the severity's new clause; `method/place_entries.py`; PLAN.md step R1, item 2.
- **The problem:**
  - The brief says "every inventory entry", and PLAN.md says "each inventory entry" (line 173). But `place_entries.py` says "Place each in-scope inventory entry", and it skips the others. The platform runs place only concerns. So an entry the concern map put out of its scope can't be under any area, and it isn't in the entries files at all.
  - The extracts still show these entries, under each list, as "Out of the concern map's scope: ...". Check 3's third bullet asks for an area for legal, place and eligibility matters "wherever the extracts show them", and some of these entries are exactly that.
  - The brief doesn't say which reading holds, and either one goes wrong:
    - A reviewer that reads "every inventory entry" plainly must, under the new framing ("a loss here is a loss there") and the new severity ("the list would leave out something the platforms record"), call each one a must-fix loss. The step has no way to place them.
    - A reviewer that reads it as "in scope" drops them, without a word, from what becomes Sharrwah's whole extent.
  - The same holds for Shopify's Help Center menus and Salla's help-centre categories, which the extracts also carry. They are tied to no concern or entry. The checks don't say whether a topic that only they show must be under an area.
- **The evidence:**
  - 411 entries are out of the concern map's scope: Shopify 117, Salla 263, WooCommerce 9, Zid 8, BigCommerce 14.
  - By their stated reasons, about 180 are headings, buttons, containers or boilerplate.
  - The rest include 52 Shopify keys, each marked "Unplaced: no Shopify source held ties this key to a concern". Among them are `threeDSecureEligibilityForCountry`, `perMarketIncoterms`, `subCountryMarketsEnabled`, `multiCurrencyGatewayEnabled`, `dutiesAndImportTaxes`, `shopifyPaymentsEnabled` and `posEnabled`. They also include BigCommerce's support levels sold with its plans, and Zid's tools that act across its whole dashboard.
  - Every in-scope entry has at least one concern. In the four runs I checked, as committed at `9b359b2`, no concern is under none, so every in-scope entry there is placed. The open question is only the out-of-scope entries and the menus.
- **The fix:**
  - Decide what "nothing lost" covers, and say it in check 3. For example: "Every entry the extracts show is under an area. The exceptions are those the concern map put out of its scope as headings, buttons, containers or boilerplate. Report each other out-of-scope entry that names something the platform offers or requires and is under no area. Do the same for a Help Center or help-centre topic that no area's names or concerns cover."
  - Say how the coordinator places such an entry, since no concern can carry it there. For example, it could name it under an area in `areas.md`, or in the area's `note`. Since `66c457a`, `own_names` accepts out-of-scope entries as names, so such an entry can also be one of an area's names. But a name isn't a placement: `place_entries.py` still skips these entries, and check 3 doesn't say a name counts.
  - If the coordinator decides instead that these entries stay out, say so in the brief and in `areas.md`, so the founder knows what the extent leaves out.
- **Severity:** must fix.

### 3. Nothing tells the review to look for our words or the founder's in the list

- **Where:** check 4; `check_areas.py`.
- **The problem:**
  - The plan makes this review the place where a word of ours or the founder's is caught. Section 7, risk 2 says: "The independent review looks for it". Section 9 names R1's review as one of the two independent reviews.
  - Check 4's test for words is narrower. A plain line "doesn't rank, recommend, or use a platform's term as if it were everyone's". A heading of the coordinator's own, or a plain line, that uses "availability", "conditions" or "parts" breaks none of these, because these aren't platform terms.
  - The checker can't catch it either. It reads plain lines only for being non-empty, in both modes. A heading of the coordinator's own needs only a reason in `note`.
  - So the headings the founder marks at G2 could carry the founder's own categories, and nothing in R1 would catch it. This is the failure the plan names first among its risks.
  - Today the reviewer would happen to see the founder's working words listed in `questions.md` (line 10), but nothing tells it to look for them. Finding 1's fix takes that file away.
- **The evidence:** PLAN.md lines 371 and 421; the brief's line 52; `check_areas.py` lines 151 and 152, 200 to 204, and 211 to 213. The platform runs worked under a "Don't" list (`R1-areas-one-platform.md`, line 43) that the review brief doesn't carry, and the checker doesn't test their plain lines against it.
- **The fix:**
  - Add to check 4: "No heading of the coordinator's own, no plain line (in the platforms' files and in `areas.tsv`), and no area's name in `areas.md` uses a category of ours. That includes the founder's working words 'market', 'availability', 'conditions', 'manual payment' and 'parts', unless a platform uses the word for that thing, and then only as that platform's term."
  - Name the one-platform brief's "Don't" list as the rule the platforms' files were made under.
- **Severity:** must fix.

### 4. The status line names a file that holds the founder's expectations

- **Where:** the brief's line 3.
- **The problem:**
  - The status line names `studies/proposals/check-of-the-draft.md`.
  - `CLAUDE.md` tells an agent working from a brief to read "only your brief and what it names". So a reviewer could take the status line as leave to open that file.
  - The file states the founder's expectations on four of the questions, and an earlier checker's view of which areas bear on question 2.
- **The evidence:** `check-of-the-draft.md`:
  - line 297: B2, "Rules land as availability";
  - line 335: B5, "Sharrwah chooses ..., by its own criteria";
  - line 357: B7, "one store currency";
  - line 371: B8, a modular platform;
  - line 911: tax and question 2.
- **The fix:** before the run, remove the status line, or replace it with one that names no file.
- **Severity:** optional. The "Read only" list leaves the file out.

### 5. The route to a cited source can't be followed as written, and three platforms' sources aren't in the observed repositories

- **Where:** "Read only", last bullet; check 8.
- **The problem:**
  - The concern map's statements carry only cite ids. A cite's source, commit and quote are in each platform's `citations.tsv`, which the brief doesn't name. Without it, the reviewer can't find the `<commit>:<path>` its `git show` needs. The one-platform brief names `citations.tsv` for exactly this.
  - The pilot's statements cite ids in the pilot's own `citations.tsv`, which isn't named either.
  - The brief gives only the observed repositories' route. All of Zid's, BigCommerce's and WooCommerce's sources, and some of Shopify's and Salla's, are held in this repository instead: web pages captured under `evidence/product-class/runs/`, or the WooCommerce package.
  - `cites` may name a citation that no statement uses, since the checker accepts any citation id. The reviewer can't read such a citation within its list.
- **The evidence:**
  - Of 11,071 citations, 6,751 are held in the observed repositories: 4,047 in observed-sh and 2,704 in observed-sa.
  - The other 4,320 are:
    - all of Zid's: 1,087 web addresses;
    - all of BigCommerce's: 481;
    - all of WooCommerce's: 885 paths in `woocommerce-11.2.1` and 581 web addresses;
    - 1,008 of Shopify's;
    - 278 of Salla's.
  - Each platform's `fetch-log.tsv` maps a web address to its captured file. The package is at `evidence/product-class/woocommerce-11.2.1/`.
  - 2,382 of Shopify's 5,055 citations are used by no statement.
  - Where the git route applies, it works. `observed-sh` at `b46731d0:structures/shopify/admin-roles/...` and `observed-sa` at `145f137:salla.com/llms-full.txt` both resolve.
- **The fix:**
  - Add the concern map's and the pilot's `citations.tsv`, as far as the reviewer follows a cite.
  - Say that a source held in this repository is read from its capture, whose file the platform's `fetch-log.tsv` names, or from the WooCommerce package. It is read only, and nothing is run there.
- **Severity:** optional. Statements carry their verbatim text, so most doubts can be settled without the source.

### 6. The column spec leaves out what the checker requires

- **Where:** "The coordinator's files". PLAN.md's step R1 makes this brief the spec for them ("as `briefs/R1-areas-review.md` describes them").
- **The problem, with my tests of the committed checker:**
  - `questions` and `cites` must be separated by ";". The checker rejects "Q1, Q2" and "Q1 Q2" as unknown questions, and "SH-C-001, SH-C-002" as an unknown id. The brief gives the separator only for `platform_area_ids`.
  - The platform in `depth.tsv`, and in `heading_source`, must be written in lower case, as `shopify`. "Shopify" is rejected. The brief gives only one example.
  - The brief describes `cites` as "the concern or statement ids". The concern map's statements have no ids of their own. The checker:
    - accepts concern ids;
    - accepts the concern map's citation ids, such as `SH-S-5001`;
    - accepts the pilot's statement ids, such as `S01-SH-001`;
    - rejects the pilot's citation ids, such as `S01-SH-C001`.

    A concern-map citation id can stand for several statements: 844 of the 2,673 citation ids Shopify's statements use are shared by more than one.
  - Check 3 asks that "the entries each platform's notes flag are dealt with". Neither `areas.tsv` nor `areas.md` has a place to say how.
- **The fix:**
  - State the separators and the lower-case platform names.
  - Say that a concern-map statement is cited by its citation id, which may cover several statements, and a pilot statement by its `stmt_id`.
  - Give a place for how each flagged entry was dealt with, such as a line in `areas.md`.
- **Severity:** optional. The checker catches the first three before the review runs.

### 7. The name rule changed during R1, and the brief doesn't say so

- **Where:** check 1; check 2's first and third bullets.
- **The problem:**
  - Check 1 runs whatever checker is in the tree, and its name rule comes from `own_names` in `areas_extract.py`. That rule changed while R1 ran. The brief doesn't tell the reviewer which rule each platform's names passed under, or what the rule now accepts.
  - Check 2 asks whether each merge "rests on the platforms' own names". Under the wider rule, a name can now be a group heading the concern map put out of its scope, or one level of a menu path. Whether such a heading fairly names a whole area is a judgment the checker can't make, and the reviewer isn't told to make it.
  - In the platforms' files, `grouping` allows only `platform's own` or `agent's own`. If the coordinator changed a platform's file while merging, its change would show as the agent's or the platform's own.
- **The evidence:**
  - `9b359b2` recorded four platform runs as passing under the first rule.
  - `66c457a` widened `own_names`. It now also accepts each part of an entry's path, each half of an English / Arabic pair, and entries out of the concern map's scope. The same commit changed `areas-zid.tsv` (20 lines): "Zid's run added ten of its list headings to its areas' names".
  - `60367cd` says Zid, Shopify and WooCommerce then checked their groupings against the headings now accepted.
- **The fix:**
  - Name the commit at which the reviewer runs the checker.
  - Tell the reviewer what the name rule accepts, and that it changed in `66c457a`. Add to check 2: "A heading used as an area's name, including one out of the concern map's scope, names what the platform itself groups under it."
  - Tell the reviewer to compare each platform's files with the commits that recorded its run, and to treat any other change as the coordinator's.
- **Severity:** optional.

### 8. Check 2 looks only for groupings that join too much

- **Where:** check 2, second bullet.
- **The problem:**
  - Check 2 asks for groupings "that hide a difference between platforms, or that join things one platform keeps apart". Both are merges that join too much.
  - It doesn't ask for the converse: one thing left in separate merged areas because the platforms name it differently. The founder could then mark one of those areas "won't do" and the other "must do", for the same thing. The brief's own severity calls that marking scope on a wrong basis.
  - Merging rests on the platforms' own names (PLAN.md line 43). Section 6 says why names alone fail: "synonyms and homonyms" (line 331). Check 2 covers only the homonyms.
- **The fix:** add "or that leave one thing in separate areas under different platforms' names".
- **Severity:** optional.

### 9. Wording that raises the stakes in one direction

- **Where:** check 3's opening sentence; the severity's new clause; check 5's last line.
- **The problem:**
  - **"Leave out" now means two things.**
    - In the severity, "the list would leave out something the platforms record" is an omission, and must fix.
    - In `left_out` and check 7, "why the work leaves it out" is an area that is on the list but that no question draws on. That is a designed outcome, which the founder marks.
    - A reviewer can read every `left_out` area as a must-fix loss. That pushes it to tie every area to some question.
  - **"Sharrwah's whole extent for the design of its first build" invites the reviewer to judge what Sharrwah needs.** Scope is the founder's at G2 (PLAN.md line 50). The brief doesn't tell the reviewer to leave it alone.
  - **"A miss here is a miss in every later step" overstates.** R3's runs "may add concerns or statements that bear on the question" (PLAN.md line 204), and the two-phase copy lets a run add a concern from outside the question's areas (finding 13). The line weights misses over drawing on too much. Only check 5's "and not much else" balances it, and the severity gives drawing on too much no weight.
- **The fix:**
  - Word the severity as "something the platforms record would be under no area".
  - Add: "Whether Sharrwah should do an area is the founder's to mark. Don't judge it."
  - Write: "A concern under no area the question draws on is no candidate for its runs, and is found later only if a run adds it."
- **Severity:** optional.

### 10. Nothing checks that `areas.md` says what `areas.tsv` says

- **Where:** check 4; the brief's line 38 ("the same list for the founder").
- **The problem:**
  - The founder marks from `areas.md`, but the scripts copy from `areas.tsv` and `depth.tsv`. Check 4 reads `areas.md` for plain words only.
  - `areas.md` might drop an area, or state differently what a "won't do" mark removes, what is kept, a left-out line or a depth choice. Then the founder marks on a different basis from the one the work runs on, which is the brief's first ground for must fix. No check would find it.
- **The fix:** add to check 4 or 6: "`areas.md` holds every area in `areas.tsv`, with the same effect of a 'won't do' mark, the same evidence kept, the same left-out line, and the same depth choice and reasons."
- **Severity:** optional.

### 11. Check 8 doesn't say how to weigh a thin record, or the gaps

- **Where:** check 8, second bullet; "Read only".
- **The problem:**
  - Check 8 flags "a platform marked `check` whose recorded material suggests an answer the in-depth platforms might not show". But the recorded material differs by platform, both in its kind of source and in how much of it there is.
  - A thin record suggests little. So the platforms most likely to be left at `check` are the ones least able to raise the flag. That is risk 16 (a checked platform's different answer is missed), arising through risk 5 (depth differs by kind of source).
  - The gaps recorded under each concern are the record of what wasn't found, and the copies carry them (PLAN.md line 42). The brief doesn't name them.
- **The evidence:**
  - Statements recorded: Shopify 3,005, Salla 2,560, WooCommerce 1,499, Zid 654, BigCommerce 473.
  - Gaps recorded: Zid 156 for 96 concerns and BigCommerce 161 for 88, against Shopify's 249 for 198.
  - PLAN.md section 6 says kinds of source are compared "like with like". Section 7 lists risks 5 and 16.
- **The fix:**
  - Add: "A thin record isn't a sign that a platform answers the same way. Weigh what each platform's material can show, by its kind of source, and read the gaps recorded under the question's concerns."
  - Add `gaps.tsv` to the reading, as far as the reviewer samples.
- **Severity:** optional.

### 12. What a run will read, and what would make it long

- **Where:** "Read only"; checks 3, 5, 6 and 8; `sizing.md`, R1's review.
- **The problem:**
  - The brief names about 1.45 MB before any statement is sampled, the coordinator's three files included. The table below gives the parts.
  - The sizing's basis for the review is "five areas files, the merged list and samples of the records". It leaves out the extracts and the entries files, which are 87 percent of what is named.
  - Read whole, those two hold the same 6,592 entries twice.
- **The evidence:** the table below; R0's measured runs in `costs.tsv`.
- **What would make it long:**
  1. **Reading the extracts and the entries files whole.** That is about 0.34 million tokens by a rough count, and more once ids are tokenized. Every request after that re-reads it.
  2. **Checks 5 and 8.** The reviewer must:
     - judge, for each of 8 questions, which areas bear on it;
     - check the "why" of each of 40 depth rows against what it cites;
     - for each `check` row, set the checked platform's material against the in-depth platforms'.

     Each of these samples statements from 2.8 MB.
  3. **Checks 6 and 7.** Each of the 29 merged areas (by the message of the commit that wrote them) has an effect of "won't do", what is kept, and maybe a left-out line. Each is checked against the questions and the files.
  4. **Re-checks.** PLAN.md and the sizing provide for two. R0's re-check resumed the same agent and measured 22.5 million, against 10 sized (`check-of-the-draft.md`, finding 47). This review's context would be larger.
- **The estimate:**
  - R0's check averaged about 0.25 million tokens a request, over 69 requests.
  - A first pass that reads the large files whole would then hold about 0.35 to 0.45 million tokens on every request. Over the 100 to 150 requests that eight checks are likely to take, that comes to about 40 to 60 million, against 30 sized.
  - Re-checks that resume it would cost about 20 and 10, against 12 and 6.
  - So the review comes to about 75 to 95 million, against 53. That is a few percent of the plan, but it would be a step past its expected cost.
  - The four platform runs came in well under their sizing: 8.5 million against about 40. So the review may too, if it reads by script.
- **The fix:**
  - Have the reviewer check placement by script: compare each entries file's `area_ids` with its areas file's `concern_ids`, and count the entries under none and split.
  - Have it read the extracts' concern lines and menus whole, but their lists only where a check needs them.
  - Bound the sampling:
    - for check 5, start from the extracts' concern lines, which give each concern's terms, statements by placement and scopes, and read statements only for concerns whose tie is in doubt;
    - for check 8, read the statements that `cites` names, and for each `check` row a stated number of concerns.
  - Run each re-check in a fresh agent that reads the review, the fixes' diffs and the files they touch, or re-size the re-checks.
  - Re-size the review's first pass in `sizing.md` from what the brief names.
- **Severity:** optional.

### 13. The brief describes the copy as it was before it became two-phase

- **Where:** the line for `questions` ("A script copies the statements under its concerns for each of these questions"); check 5's last line ("This decides what a script copies for each question"); PLAN.md section 2 (line 42), step R1 (item 3) and step R3 ("A script copies first").
- **The problem:**
  - Since `681df43`, `copy_statements.py` works in two phases:
    - `candidates` lists the concerns of the areas a question draws on;
    - the recording run marks each one `copy` or `set aside`, with a reason, and may `add` a concern from outside those areas;
    - `copy` then copies only the concerns chosen.
  - So tying an area to a question now decides which concerns a run starts from, not what is copied. Drawing on too much now costs each run a reason for every concern it sets aside. Missing an area means its concerns reach a run only if the run adds them.
  - Check 5 weighs both kinds of error by what the brief says the tie decides, and the brief still describes a direct copy.
  - PLAN.md says the same as the brief, and has no dated entry for the change.
- **The evidence:** the docstring of `copy_statements.py` at `681df43`. The commit's message gives the reason: "Tying whole areas to a question would have copied over 1,000 statements for several runs".
- **The fix:**
  - Re-word the line for `questions`: "A script lists its concerns as candidates for each of these questions. The recording run copies, sets aside or adds."
  - Re-word check 5's last line to match.
  - Give PLAN.md its dated entry in section 11, and change sections 2 and R1 and R3 to say the same.
- **Severity:** optional. The review can be done either way, but check 5 is judged against the wrong consequence.

## What a run will read

| What the brief names | Size | Note |
| --- | --- | --- |
| The five extracts | 712 KB | Lists 401 KB; concern lines 256 KB; Shopify's and Salla's menus 52 KB |
| The five entries files | 539 KB | The same 6,592 in-scope entries as the extracts' lists, each with its areas |
| The five areas files and their notes | 111 KB | |
| `areas.tsv`, `areas.md`, `depth.tsv` | 70 KB | Written at `c7ce5db`, after this check began. `areas.md` alone is 43 KB |
| `questions.md` and the brief | 14 KB | |
| Recorded data, as sampled | from 2.8 MB | 8,191 statements in the concern map; the pilot's 821 statements, 0.4 MB |

The sizes are taken at `c7ce5db`.

## Verdict

**Yes, the brief can run once findings 1 to 3 are fixed.**
- **Finding 1** needs a file, or a section of the brief, that holds only the eight questions as quoted.
- **Finding 2** needs the coordinator to decide first whether the concern map's out-of-scope entries, and the help-centre topics tied to no concern, belong to the whole extent. The brief then says so, and says how such an entry is placed.
- **Finding 3** is a sentence in check 4.

The brief and the checker agree on everything that changed since the re-check. The brief no longer allows a "none" depth. The checker, run as the brief runs it (without `--cuts`), rejects one, and my tests of the committed checker confirm it.

**Also worth taking now, at a line each:** findings 4, 5, 6 and 13. Finding 13 matters because the copy changed while this check ran, and check 5 should be judged by what the tie now decides. Finding 12 changes what the review costs more than what it finds. Its reading guidance would keep the first pass near the sizing.

The fixes are small, so a separate check can confirm them from their diff.
