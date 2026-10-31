# Inspection of the final review's brief and selection, brought up to the held pass (31 October 2026)

**What this is:** an inspection, before they run, of `briefs/R-extent.md` (revised on 31 October), its design `briefs/R-extent-design.md` (the coordinator's decisions in section 8) and `method/review_select.py`, all read at `9195b096`. `PLAN.md`, section 3: "Before a brief runs, a separate agent reads it for anything that presupposes the answer". The inspector made none of them and changed no file except this one.

**How it was run.** Other agents committed while I worked: HEAD moved from `9195b096` to `5ba8a4e6`, then `d0fb7f82`. So the runs used a frozen copy of the repository at `9195b096`, made with `git archive 9195b096 method studies reports`. The model there is the one the design measured: `git diff --stat c7224109 9195b096` touches only the brief, the design, the script and `method/README.md`. `at_since`'s files of `9d204b46` came through `--since-dir`, from `git show 9d204b46:studies/class-model/merged/<file>`. One run on the working tree at `d0fb7f82` is reported where it differs. Tests that write ran on a copy of `studies/class-model` with `CLASS_MODEL_DIR` set. The scratch folder is `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/R-inspect/`, written `<scratch>` below. `studies/class-model/review/` doesn't exist after any run.

On the frozen copy, `python3 -I method/review_select.py --out <scratch>/out/sel-commit.tsv --since-dir <scratch>/since` printed the design's figures:
```
../out/sel-commit.tsv: 1599 items (1201 on one platform, 398 on a capability or no capability) from 1835 cells
  share 1: 343 items in 12 batches   share 2: 386 in 13   share 3: 276 in 10   share 4: 479 in 16   share 5: 115 in 4
```
It also printed 141 ruling lines over 25 rulings with lines.

Severity: **must fix** means a reviewer following the brief would write wrong verdicts, or the selection would miss a risk it claims to take. **Should fix** means the output would be steered, less consistent, harder to check, or dearer than it needs to be. **Note** is for the record.

---

## Must fix

**R2-1. The omission review's `held` verdicts can't be read blind: the item prints their basis.**
- *Found:*
  - The brief, line 77: "Read the item yourself first, and decide what it states, before you read the row's basis (ruling, proposed: `R-R2`)". R-R2's own why (design, line 147): "Without it, the measured miss rate is biased low."
  - The script writes the basis into the item's detail (lines 611 to 612), which the reviewer reads first to find the item: `does the model hold the item's thing here, on {r.get('basis', '') or 'its basis'}?`.
  - I wrote a fixture of 20 `held` rows, `<scratch>/class-model/omission/OM-ZD-items.tsv`. The selection's item R-0061 reads: "held verdict (a seeded tenth, counted as the omission review's own miss rate): does the model hold the item's thing here, on ZD-E-0c261652@ZD-4?"
- *Fix:*
  - In `review_select.py`, line 612, end the detail at: "… counted as the omission review's own miss rate): read the item first (R-R2); the row's basis is in its items file, to read after your own reading".
  - In the brief, add to the `held` verdict: "Your item shows the row's capability, never its basis. Read the item's own source and write what it states in your findings. Only then open the items row."

**R2-2. A `held` verdict shares its item with other reasons. It can't have its own line, and `rates` counts the other reasons' verdicts as the omission review's misses.**
- *Found:*
  - The brief, line 77: "These verdicts are counted as the omission review's own miss rate (`review_select.py rates`), so give each one its own line, never one for several."
  - The script puts a `held` verdict on its cell's item (`add_cell`, lines 613 to 616), alongside every other reason of that cell.
  - 834 of the 1,215 held cells (69%) already carry an item at `9195b096`: a count from `<scratch>/out/sel-commit.tsv` against `merged/cells.tsv`. A `held` verdict is always on a held cell, so most of the tenth will share an item (an assumption: their cells are like the others).
  - Two `held` rows on one cell become one item, and `check` refuses a second line for an item: "line 32: R-0002 again" (test 21, below).
  - `rates` (lines 853 to 858) counts an item's one verdict under every reason it carries. It also counts it as the omission review's verdict wherever the detail has "held verdict (a seeded tenth".
  - A test: on a selection where one tenth item also carries `kind`, I wrote that item `wrong`, severity `kind`, for its kind. `rates` printed "the omission review's held verdicts, a seeded tenth: 2 read, 1 wrong, 0 unclear: its own miss rate 50.0%".
  - That rate goes to the founder at GM as a measure (`O-omission-design.md`, section 7.3: "so the founder sees what was missed as a measure, not an assumption").
- *Fix:*
  - In `review_select.py`, make each `held` row of the tenth an item of its own, never merged into a cell's or a capability's item: `add(item(("om-held", part, i), c, plat, ""), "omission", d)`.
  - In `rates`, take the omission review's rate from those items only.
  - In the brief, add: "A `held` verdict is an item of its own. Its verdict answers the omission review's row alone, whatever the cell's other questions: `holds` where the model holds the thing as the item states it, `wrong` where it doesn't."

**R2-3. The loose counted-twice flags are one item of 2,309 statements, given to one reviewer.**
- *Found:*
  - `inspection-Q3R.md`, R-3, made the counted-twice flags with no cell resting on them alone into one item when there were 36: "for the coordinator to settle by convention 8, rather than 36 agent items". The design keeps "one item, as the inspection's R-3 asked" (line 12).
  - At `9195b096` there are 2,309 of them. `merged/flags.tsv` has 2,324 `counted twice`, 15 of them "rests on it alone"; 2,257 of the 2,309 name a held entry.
  - The selection makes them item R-1485, share 5, batch 1, one of a reviewer's 30 items (script, lines 401 to 402 and 418 to 419): "counted twice: 2309 statements that support core or own-service in two domains with no cell resting on them alone (merged/flags.tsv): settle them together by the brief's rule".
  - The brief tells the reviewer to "settle them together by this rule" (line 56), and to stop at about 200,000 tokens (line 94). 2,309 statements join 1,025 sets of capabilities.
  - At the design's 120,000 to 250,000 tokens an item, that is the reading of tens of items in one (an assumption). A reviewer will write `holds` or `unclear` without reading them.
  - The risk inside them: 97 of those sets share five or more counting statements. 399 of their 673 pairs aren't flagged `one capability?`, so no other `flag` question reads them. A statement that names one thing two domains each hold is a duplicate capability (brief, line 56), and a duplicate doubles a count.
- *Fix:* in `review_select.py`, drop the loose item.
  - Print the 2,309 for the coordinator to settle by script, as R-3 asked.
  - For the review, make each set of capabilities sharing five or more counting statements a `flag` item on its first capability: "counted twice: N statements on CM-A and CM-B: are they one thing? (as for *one capability?*)". There are 97 such sets now. Add a seeded tenth of the other sets.
  - In the brief, line 56, replace the last sentence with: "Capabilities that share five or more such statements come as one item: are they one thing? The coordinator settles the rest by script."

**R2-4. `none-held` drops `absent` cells and superseded rows, and then no one reads them.**
- *Found:*
  - The script drops a none-held cell wherever `held/<platform>/s2-outcomes.tsv` gives it the outcome `not-found`, `absent` or `not-held` (lines 331 to 332). It doesn't read that file's `superseded` column. `s2_held.py` gives the column (line 100, `OUT_HEAD`) and says what it means (lines 71 to 73): "a row a later batch changes, or whose subject it finds, is marked `superseded` by that batch".
  - R-R3's why (design, line 151): "the second stage reads every such cell, and the omission review measures its misses". The omission review's group 5 samples only "the rows of `held/<platform>/s2-outcomes.tsv` of outcome `not-found` or `not-held` whose cell is still `none-held`" (`O-omission-design.md`, section 2.5).
  - A test: I wrote a fixture `s2-outcomes.tsv` on five selected Zid cells (removed after).
    - CM-CAT-004 (`absent`) left `none-held` and had no item at all.
    - CM-CHK-004 (a `not-found` superseded by a later `unclear`) also left `none-held`.
    - The summary still said: "4 cells the second stage read and left holding nothing are left to the omission review's sample".
  - `absent` is the one outcome that says the platform lacks the thing. `PLAN.md`, section 6 (the test form, step 2), allows that only "from a complete list the platform publishes". The second stage's first part already has two at `d0fb7f82` (`held/zid/s2/S2-ZD-1.tsv`: CM-PLN-003 and CM-PAY-010).
  - CM-PAY-010's rests on Zid Pay's terms making chargebacks "the merchant's". B-extent places such a statement `shows`: "A statement that makes the merchant or buyer responsible is `shows`" (line 118). That is a reading, for the review to settle, not settled here.
- *Fix:*
  - In `review_select.py`, lines 331 to 332, take `if r.get("outcome") in ("not-found", "not-held") and not r.get("superseded")`, and count only those in the note.
  - Add to the `none-held` reason, in the script and the brief: "and every cell the second stage wrote `absent`: is the list its row cites the whole of what the platform publishes, and does it leave the thing out? `PLAN.md`, section 6: 'Absence counts only from a complete list the platform publishes … Otherwise it is a gap.'"
  - Correct R-R3 to match (R2-15).

**R2-5. The Flags ruling is never sampled on Zid, whose rule its own table states.**
- *Found:*
  - The brief, line 69: a `ruling` line is "chosen at random from that ruling's lines so that each ruling's application is tested on each platform it reaches".
  - `RULING_PATTERN` (lines 96 to 98) finds the Flags table's lines by words of the drafter's choosing. I ran that pattern over the 24,456 listed lines: its 526 are Salla's 277, Shopify's 172 and WooCommerce's 77. None is Zid's or BigCommerce's, and the 11 lines sampled are Salla's, Shopify's and WooCommerce's.
  - The table's rule "A store's flag by its value" is Zid's: "Zid's `feature_flags`: `true` is built in, the store the scope; `false` is shown only; a pilot, preview or test name (`is_mazeed_pilot`) is shown only while `false`" (`GM-rulings.md`, line 1352).
  - Zid's batch ZD-7 applies it in other words: 152 lines, 88 `core` and 64 `shows`, 82 of them naming "value true" or "value false". An example: "a pilot flag for Mazeed, the cell's Mazeed (ZD-5's mazeed routes); value false" (`held/zid/placements-ZD-7.tsv`, line 6, `shows`).
  - ZD-1's "sidebar badge new (source.js)" lines apply the badge rule D1 without naming it.
  - 886 lines name a flag's words outside the pattern. Examples: Salla's "is not released: shows" (`placements-SA-33.tsv`) and WooCommerce's "a flag not released (ruling)" (`placements-WC-6.tsv`).
- *Fix:* in `review_select.py`, sample the Flags table by its rows: one line per row and per platform its words reach, then the usual rate. Find each row's lines by its own words. On the frozen copy, these find 754 lines, every one of the 526 among them, and 93 of Zid's:
  - Not released: `released\W{0,3}false|is_experimental|\bnot released\b|\bunreleased\b` (219: Shopify, Salla, WooCommerce);
  - Released: `released\W{0,3}true` (199: Salla);
  - Off by default, no toggle: `disable_ui` (25: WooCommerce);
  - A store's flag by its value: `feature_flags|\bvalue (?:true|false)\b|pilot flag` (120: Salla 38, Zid 82);
  - Early access, previews: `early access|\bin (?:a )?(?:preview|beta)\b` (106: Shopify);
  - Shopify's hashed betas: `hashed beta|admin-betas|\bbetas?\W{0,3}(?:enabled|true|false|on|off)` (42);
  - A release badge (D1): `\bD1\b|\bbadge (?:new|beta)\b` (59: Shopify, Salla, WooCommerce, Zid);
  - Before release, by the merchant: `feature test drive` (25).

  Print each row's lines by platform in the summary. None of these reaches BigCommerce's Early access section (`BC-E-76df3315`, placed `core` on CM-EVO-001). The coordinator adds it by its id if it applies the rule (a reading).

**R2-6. A Q3 row found wrong can't be corrected.**
- *Found:*
  - The brief asks of a `q3` item: "Does its result hold …? Are its answerers and time those its rules give?" (line 61). 93 items carry `q3`.
  - Its list of corrections (line 98) has no form for Q3's rows, and `check` refuses one. The correction `q3/check-Q-01.tsv: km:ACC-02: result partly` gave "line 3: a correction names <part>/<file> (or held/…" (test 6, below).
  - A reviewer who finds a `q3` row wrong must write it `unclear`, or point the correction at another file, to pass the checker.
  - The version inspected on 30 October refused it too (`git show 589c6930^:method/review_select.py`, line 257). So R-1's fix was never finished.
- *Fix:*
  - In the brief, line 98, add: "A Q3 row: `q3/check-<set>.tsv`, by its `set` and `row_id`".
  - In `review_select.py`, line 790, add `|^q3/check-Q-\d+\.tsv` to the pattern and to its message.

## Should fix

**R2-7. Two pattern rulings take lines that don't apply them and miss lines that do, and every item says "applies".**
- *Found:*
  - "Once a new thing is a capability, each line's support is what its entry shows" decides that "lines placed as shown only just because the thing had no place of its own become built in …" (`GM-rulings.md`, line 712).
    - Its pattern (script, line 559) takes the 408 `new:` lines whose thing was decided onto a capability.
    - It also takes 54 lines that later batches placed directly on a made capability, which never had that condition.
    - One of its 10 sampled lines is such a line: R-1431, `held/salla/placements-SA-48.tsv line 115 (SA-48 SA-E-c3362232: capability CM-SFR-015 core)`.
  - The cards ruling's handle is "M-3, M-7; refined after WC-3" (`GM-rulings.md`, line 632).
    - `HANDLE_STOP` (line 104) cuts at ";", so the refinement has no line in the pool. The refinement: "the platform's suggestion to buy an extension from its marketplace, naming no maker … is shown only".
    - 29 lines name WooCommerce's marketplace suggestions, 18 of them placed `shows` and 6 `core`. 25 of the 29 name neither M-3 nor M-7.
  - The detail reads "applies '<title>'" for every match (line 577), the pattern's included. A reviewer told that a line "applies" a ruling is steered to judge the line by it.
- *Fix:* in `review_select.py`:
  - at line 559, keep only `L["placement"] == "new"`;
  - give the cards ruling a `RULING_PATTERN` entry beside its handle: `\bM-3(?!\d)|\bM-7(?!\d)|marketplace_suggestions|marketplace suggestion`;
  - at line 577, write "names '<title>'" for a handle's match, and "matched to '<title>' by its words" for a pattern's.

  In the brief, after the `ruling` reason's two questions, add: "If the line doesn't apply the ruling at all, say so in your findings, and give the verdict by the supports alone."

**R2-8. One verdict, one severity and one correction answer up to six reasons, and `rates` credits each reason with them.**
- *Found:*
  - 454 of the 1,599 items carry two reasons or more, up to six (R-1108, CM-AUT-001 on Shopify: `kind,own-service,coordinator,ruling,s2-lead,batch`, 30 questions in its detail).
  - The brief says "Answer each reason the item carries" (line 35). It doesn't say which verdict an item takes when one reason holds and another is `unclear`, which severity when two differ, or how to write two corrections. Two reviewers will write such items differently.
  - `rates` prints each reason's verdicts as if each had its own (lines 855 to 856).
- *Fix:*
  - In the brief, under Output: "An item's verdict is `wrong` if any of its reasons' answers is wrong, otherwise `unclear` if any is unclear, otherwise `holds`. Its severity is the highest of `kind`, `structure`, `placement` and `reading`. `correction` names each change, separated by ` ; `, each with its file. Your findings give each reason's answer by its name."
  - In `rates`, print by reason only the items that carry that reason alone, and say so in its heading.

**R2-9. A `ruling` item's two answers have no column, and their order lets the ruling frame the entry.**
- *Found:*
  - The brief, line 69: "Answer two things, each in your coverage's `basis` and your findings". But `basis` is "the keys and entry ids you read, `;`-separated" (line 98), and `check` accepts free text there (test 9).
  - The brief has the ruling read first, then asks whether the line holds by B-extent. R-R1 tests whether a ruling departs from B-extent. A reviewer who has just read the ruling is least placed to see that (a reading).
- *Fix:* replace the `ruling` reason's lines 69 to 71 with: "First read the entry and its sources, and decide by the supports above (and `B-extent.md`'s conventions) what the line should take. Then read the ruling's entry in `GM-rulings.md` and the source its **Source** links, and answer: is the ruling applied as its source words it? Does the entry's text meet the ruling's condition, and does the line take what the ruling gives? Write both answers in your findings under the item. `basis` holds keys and entry ids only."

**R2-10. Three reasons' words steer one way.**
- *Found:*
  - `count` (brief, line 49; detail, script line 319): "Does the platform place it in its core after all …?"
    - It quotes the three conventions that make a cell `core` (its own API, a released flag, a staff permission), and none of those that keep it `shows`.
    - Those are: B-extent's "A statement that makes the merchant or buyer responsible is `shows`" (line 118); H-held's "a flag the source states isn't released (`released: false`, `is_experimental: true`) is `shows`, whatever its value for the store" (line 119); and its "What a partner or an app asks of a merchant or of the platform … is `shows`" (line 117).
    - 161 items carry `count`, 150 of them on cells placed `not-stated` or `extension-point`.
  - `kind` for a slot or an open (brief, line 48; detail, line 314): "a missed core would change the kind". A wrong `extension-point` or `outside` changes a slot's kind too (to `open`), and the reason doesn't ask about it. 45 cells.
  - `coordinator` on a held line: the detail quotes the coordinator's own reasoning before the reviewer reads the entry (lines 537 to 538). An example is R-0635: "the coordinator's check after SH-34: core by D1, a feature the merchant can enable before its release (Feature test drives) is offered to".
- *Fix:*
  - `count`: "Is its placement right by the supports above? It changes the count if it should be `core` or `own-service`. The conventions that give `core`: [the three quoted now]. Those that keep `shows`: 'A statement that makes the merchant or buyer responsible is `shows`, never `outside`' (`B-extent.md`, line 118); 'a flag the source states isn't released … is `shows`' (`H-held.md`, line 119); 'What a partner or an app asks of a merchant or of the platform … is `shows`' (line 117)." Its detail: "held, but placed neither core nor own-service: is its placement right?"
  - `kind`, for a slot or an open: "Is each placement right? A missed `core` or `own-service` makes it a class. An `extension-point` or `outside` its statements don't show makes it open." Its detail: "a cell of a slot: its kind moves if a placement is wrong".
  - `coordinator`: give the line's reference only in the detail. In the brief: "Read the entry and its sources first, then the coordinator's reason."

**R2-11. The checker accepts much of what the brief forbids.**
- *Found:* run on the copy with `check --share 1 --batch 1` (tests below).
  - It refuses what it should: a fake statement key, inventory id or held id; a bad severity; `holds` with a severity; `unclear` without what would settle it; `wrong` without a correction; a correction to `merged/`; an item twice; a stray item; a missing item; a double quote.
  - It accepts what the brief forbids:
    - in `basis`: free text ("the cell's reading"); a capability id alone; a bare statement id (`SH-S-2520`); a subject's statement id that doesn't exist (`S01-SA-999`); a held id without its batch; a real held id at a batch that doesn't hold it (`ZD-E-29f102f6@ZD-99`);
    - in `correction`: the file alone, with no row and no value (`A-anchor/cells.tsv`); a part that doesn't exist (`Z-nowhere/cells.tsv`); a batch that doesn't exist (`placements-ZD-99`); a points file that doesn't exist (`points/P-01.tsv`, for `P-1.tsv`); a held line on another platform than the item's.
  - The brief asks for "the keys and entry ids you read … a held line as `<entry id>@<batch>`", and a correction giving "the file, the row and the new value" (line 98). The check (lines 788 to 803) tests only a correction's prefix, and only those basis tokens that look like keys.
- *Fix:* in `coverage_problems`:
  - `basis` must hold at least one key, inventory id, held id or subject's statement id, and each must exist (a subject's statement through `class_slice.subject_items`);
  - a held id must have `@<batch>`, and that batch's placements file must hold it;
  - a correction's file must exist under `CLASS_MODEL_DIR`, and be followed by a row (a `cap_id`, an entry id, a `concern_id`, a key, an `item`, a `vp_id` or `line N`), a colon and a new value;
  - a held correction must be on the item's platform.

  Test each case below.

**R2-12. `absorbed` is read from any field of a row, its reading included.**
- *Found:* the script takes a row as `absorbed` where the word is in any field (line 597). In my fixture, a `held` row read "a reading: the walk's flag absorbed doesn't apply here; the place is this capability's thing" (item `1-ZD-aaaaaaaa`). It was taken as `absorbed`: put on CM-CNT-008 with the absorbed question (R-1176), and taken out of the tenth's pool, so its verdict can never count in the miss rate. The design's open question 8 leaves the column to `om_sample.py`'s builder, and decision 8 leaves it to the omission review's inspection.
- *Fix:* in `review_select.py`, line 597, read only the column the builder names (until then, every field but `reading`, `read` and `basis`). A walked place that is `held` stays in the tenth's pool as well as in its `absorbed` item.

**R2-13. `s2-note` and `ql-note` depend on a note's form that no brief prescribes, and fail silently.**
- *Found:*
  - `note_bullets` (lines 228 to 257) takes only `-` or `*` bullets under a heading matching `S2-R2|held cell|final review` (`QL-R8|placement|final review` for `ql-note`). The S2 and QL briefs ask for "what a passage states that would change a held cell's placement (`S2-R2`)" (`S2-held.md`, Output), but prescribe no form for it, and neither stage's checker reads it.
  - Tested with the script's own patterns (`<scratch>/notes_test.py`):
    - a heading with "(S2-R2)" and `-` bullets: 2 taken;
    - a bold label over bullets: 0;
    - numbered items: 0;
    - a table: 0;
    - a heading in other words ("Placements a passage would change"): 0;
    - a "Problems" bullet naming the final review: 1, taken as a note.
  - The summary says nothing when a file yields none: it prints a note only where no notes file exists at all (line 685). At `5ba8a4e6`, `held/zid/s2/S2-ZD-1.md` held only "(notes in progress)". A run then would have printed neither a note nor an item (a reading of lines 670 to 686).
  - The first real part shows the form held this time. At `d0fb7f82`, `held/zid/s2/S2-ZD-1.md` line 43 is "## What would change a held cell's placement (S2-R2), and leads for other parts", and `s2-note` takes 11 items from it.
  - That section also carries leads for other parts: bullets on cells already `core` (CM-CHK-001, CM-ORD-005, CM-PAY-009, CM-SHP-018) and one on CM-ACC-003, which holds nothing. All of them are taken.
- *Fix:*
  - In `select`, print each notes file's count of bullets taken, and a `PROBLEM` line where a file names S2-R2 or QL-R8 but none is taken. Take numbered items and table rows too, and add `placement` to `s2-note`'s heading pattern, as `ql-note`'s has.
  - In the coordinator's message to the later parts: "Under a heading naming S2-R2 (QL-R8), one `-` bullet per passage, each beginning with the cell's cap_id. Leads for other parts go under a heading of their own."

**R2-14. R-R1 doesn't say what its `wrong` does, or what "departs" means.**
- *Found:*
  - The brief, line 71: where the line applies its ruling faithfully and the ruling departs from B-extent, "the verdict is `wrong`, its correction the line, and your findings name the ruling, so the coordinator can bring it to the founder's veto". Line 86: "Write findings; the coordinator corrects."
  - So a sampled line would be corrected against a ruling in force, one line at a time, before the founder rules, while the ruling's other lines stay as they are.
  - The brief gives no test of "departs". Many held-pass rulings decide what B-extent leaves open, such as a card that names no maker. Two reviewers will read a ruling that fills a gap differently, one as a departure and one as a refinement (a reading).
  - The design's R-R1 (lines 140 to 144) and its entry in the veto list (`GM-rulings.md` at `27ec3797`, line 1878) name neither.
- *Fix:* in the brief, replace the second question's last sentence with: "Where the line applies its ruling as worded and B-extent's quoted words give another support for the same statement, the ruling departs from B-extent. Where B-extent is silent and the ruling decides, it doesn't. For a departure: verdict `wrong`, severity as the change would be, correction `pending the founder's veto of '<ruling title>': <the line's value by B-extent>`. The coordinator applies none of these until the founder rules." In `rates`, count corrections beginning `pending the founder's veto` apart. R-R1's Risks: as in the table below.

**R2-15. R-R3, R-R4 and R-R5 say what the script doesn't do, and the design gives three rulings without all four parts.**
- *Found:*
  - R-R3's why, "the omission review measures its misses", is untrue for `absent` cells and superseded rows (R2-4).
  - R-R4:
    - Its why, "the other 701 sit on cells that count through lines the coordinator didn't touch", holds for 563 of them. 95 are lines placed `out`, and 43 are lines placed on new things (`<scratch>`'s count with the script's own regexes).
    - Its risk in the veto list, "where no count rests on it", is untrue for an `out` line that should count.
    - Its alternative, "about 70 items more", measured 82: `--coord-rest 1` gave 1,681 items.
  - R-R5's alternative, "all 1,038, about 900 items more", measured 26 items more (`--one-cap-terms 1` gave 1,625). The pairs join items already selected: 809 more pairs, 37 items with ten or more, up to 41 in one item. Its cost is in the pairs within items, not in items.
  - The design's section 6 has no Risks for R-R2 and R-R4, and neither Why nor Risks for R-R5. The veto list's entries, written after the commit (`27ec3797`), give all four.
- *Fix:* the words in the table below, in the design's section 6 and in `GM-rulings.md`'s five entries.

**R2-16. The omission review's decision 13 has no step that applies it.**
- *Found:* "The final review's sample … is raised for a platform whose group 5 bound passes 10%" (`O-omission-design.md`, section 11, decision 13). The script has `--platform-sample P=F`, but nothing reads `omission/rates.tsv`. The design's decision 6, on when the selection runs, gives no command to pass it.
- *Fix:* add to decision 6: "The selection's command takes `--platform-sample <platform>=<fraction>` for each platform whose group 5 bound in `omission/rates.tsv` passes 10%, and the commit records the command." Or have `select` read `omission/rates.tsv` and print what it raised.

**R2-17. Some items hold many questions, and the estimate prices them as one.**
- *Found:*
  - `one capability?` flags join their capability's item: 92 items carry 229 pairs, up to 17 in one. R-1108 holds 30 questions in a detail of 7,680 characters: 17 coordinator's held lines, 5 batch lines, 4 ruling lines, 2 leads, and its `kind` and `own-service`.
  - The design prices every item at 120,000 to 250,000 tokens (section 3), and the brief stops a reviewer at about 200,000 tokens and has it finish the item first (line 94). One such item can pass the stop on its own (an assumption).
- *Fix:* in `review_select.py`, split a capability's `one capability?` pairs into items of at most five pairs, and a cell's held lines into items of at most ten. Print the ten longest items in the summary. In the design's section 3, price the items by their questions where they hold more than five (an assumption to measure on batch 1).

**R2-18. A handle that names a second-stage ruling would match every second-stage line.**
- *Found:* `ruling_pattern` takes `\bS\d+\b` from any handle (line 210), meaning the dry run's S1 to S17. A handle "S2-R3" gives `\bS2\b`, which matches the reading `s2_held.py land` writes on every landed line ("the second stage: s2/S2-ZD-1.tsv line 4"): my test printed `True`. No second-stage ruling is high today: run against `GM-rulings.md` at `d0fb7f82`, the frozen script found 25 high entries, R-R1 among them, and listed R-R1 harmlessly as having no handle. But the selection runs on the report as it will stand then (decision 6), while rulings are still being added to it.
- *Fix:* line 210: `re.findall(r"\bS(?:[1-9]|1[0-7])\b(?!-)", h)`.

## Notes

- **R2-19. The made capabilities.**
  - The brief says "Sixteen capabilities were made from the held pass's new things" (line 7), and the design "16 from the held pass's new things, 4 from the points' and Q3's amendments" (line 50).
  - All 20 capabilities made since `9d204b46` are decisions in `held/new.tsv` (a count of its `capability:CM-…` decisions against the capabilities new since the merge). Four of them are the 30 October group: CM-SFR-015, CM-SFR-016 and CM-CNT-010 in `E-amend`, and CM-LOY-008 in `D-amend`.
  - Say "Twenty", and drop "from the points' and Q3's amendments".
- **R2-20. The report's high rulings that `ruling` doesn't parse, and its counts.**
  - `GM-rulings.md` counts "21 of them high, and 270 table rows, 21 of them high" (line 61). The parser finds the 22 high entries from the held pass on, Flags among them, and 3 high table rows, the Editions digest's.
  - The other 18 high rows are the "New capabilities" table, high by its shared weight: "each new capability is high, since it adds a capability with its count" (line 1100). `new-cap` reads every cell of each of them, so they are covered. The design and the summary should say so.
  - The counts:
    - "over 500 lines" for the cards ruling is 330 lines naming M-3 plus 204 naming M-7 (line 634); the script's 348 is their union;
    - S7's 235 includes one line of a calibration batch the script rightly leaves out (234);
    - Editions rule 17's "about 93 lines" is 82 in the Editions batches (the 312 lines naming "rule 17" include the router digest's own rule 17, which `ruling_batches` rightly excludes).
- **R2-21. "Which `ruling` samples" isn't so for 191 lines.** The docstring (line 30) leaves a line that only cites a coordinator's ruling out of `coordinator`, "which `ruling` samples". Of the 321 such lines, 130 match a high ruling's pattern. The other 191 cite rulings of medium weight, or "which the coordinator confirmed" (150). Neither reason can draw them. By the report's weights none can move a count (a reading), so their being unread is in proportion. Say so in the docstring.
- **R2-22. `batch` can draw an `out` line the omission review read.** `om_entries` holds the items rows' `item` ids and their `held` basis (lines 589 to 590). The items' ids are hashes, `<group>-<PREFIX>-<8 hex>` (`O-omission-design.md`, section 8.1), never entry ids. A group 6 item names its entry in `source` only on a miss or `unclear`. Add each row's `source` where it is an entry id, and `omission/sample.tsv`'s group 6 entries.
- **R2-23. Small facts in the brief.**
  - Its example "held/zid/placements-ZD-4.tsv line 12 (ZD-4 ZD-E-29f102f6: capability CM-ACC-001 core)" (line 35) is on line 2.
  - Its "24,704 placement lines" (line 7) includes 248 lines of four calibration batches (BC-CH, BC-CX, ZD-CH, ZD-CX). `held/batches.tsv` doesn't list them, and the script reads the other 24,456.
- **R2-24. Line numbers go stale between batches.** The design corrects the model share by share between batches (section 4), so a placements file can change after the selection is committed. Add to the brief: "Find a held line by its entry id and `cap_id` (`grep -n`). Its line number is the one it had at the selection's commit."
- **R2-25. Proportion, beyond R2-3, R2-5 and R2-17.**
  - `new-cap`: 55 of its 109 items are cells holding nothing. They are in the second stage's parts (`held/s2-parts.tsv`), and the omission review's group 5 samples their rows. By R-R3's own reasoning they could leave `new-cap` once the second stage has read them, saving up to 55 items (an assumption on overlap). Or keep them, and say why.
  - `s2-lead`: 41 of the selection's 103 lead details are chosen as qualities. Whether `qualities/` holds each is a lookup the coordinator can script before the selection runs, sending only the unheld ones.
  - `coordinator`: a tenth of the 701 instead of a third saves only 23 items (`--coord-rest 0.1` gave 1,576). R-R4 isn't a lever on cost.
  - `s2-note`: about half the bullets of the first real part are on cells already `core` (R2-13). Taking only bullets whose cell lacks the support the passage states, as `s2-lead`'s `lacks` test does, would set it better.
- **What holds, as tested:**
  - `kind` (123), `count` (161), `own-service` (135), `changed` (130) and `new-cap` (109) select exactly their words, recomputed from the merged files and `9d204b46`'s.
  - `batch` reaches all 181 listed batches. `sample` leaves out the cells the omission review names (1 such cell sampled before my fixture, 0 with it).
  - The `ruling` counts by handle match the report's own wherever it gives one, but for S7's one calibration line (R2-20). The batch filter keeps a digest's row to its batches. The `llms`, route-gate and maker-field patterns find their rulings' lines: 13 on Zid and Salla, 479 on Shopify and 287 on WooCommerce, the last two the report's own counts.
  - The brief's quotations match their sources, and the lines it cites in `B-extent.md` (67, 111, 114 to 118, 131, 152) hold what it says.
  - Independence is by construction and by record (design, section 4).
  - `--out` writes nothing in the repository.

---

## The five rulings, R-R1 to R-R5: do their plain words say truly what each does?

Read in the design's section 6 at `9195b096`, and in the veto list's entries added by `27ec3797` (`GM-rulings.md`, lines 1878 to 1917 at `d0fb7f82`).

| Ruling | Decides | Why | Risks | Instead |
| --- | --- | --- | --- | --- |
| `R-R1`, a ruling applied faithfully can still be wrong | True, but it omits that the verdict carries "its correction the line", against a ruling in force (R2-14) | Its quote is exact (`PLAN.md`, line 82: "55% of its misses came from a brief that restated the model's rules loosely"); "so a ruling can carry an error into every line it places" is a reading, and should be marked as one | Incomplete. Add: "a sampled line corrected against a ruling still in force, while its other lines stay; reviewers reading 'departs' differently where B-extent is silent and the ruling decided" | True |
| `R-R2`, `held` verdicts read blind | Not true of the script, which prints the basis (R2-1) | True: `O-omission-design.md`, section 6, "`reveal` shows the second stage's row only after the agent's own verdict is written" | Missing in the design. The veto list's "more reading per item" misses the real one: "the measured miss rate is biased low wherever the item shows the answer first, and a shared item mixes other reasons' verdicts into it (R2-2)" | True |
| `R-R3`, none-held cells the second stage read | Too wide: "left holding nothing" takes in `absent` and superseded rows (R2-4) | Not true for `absent` and superseded rows, which group 5 doesn't sample | True as far as it goes. Add: "an `absent`, the one outcome that says the platform lacks the thing, is read by no one" until R2-4's fix | "about 146 items more" is today's count, before the second stage lands. Say "the cells the second stage read, about 146 at most" |
| `R-R4`, the coordinator's held lines by risk | True (39 read; 34% of 701) | Holds for 563 of the 701. Say: "563 sit on cells that count through lines the coordinator didn't touch; 95 are `out` lines, which the omission review's group 6 samples; 43 are lines on new things, whose capabilities `new-cap` reads where they became one" | Missing in the design. The veto list's "where no count rests on it" isn't so for `out` lines | "about 70 items more" measured 82 |
| `R-R5`, `one capability?` by shared terms | True | Missing in the design. The veto list's is a reading, marked | Missing in the design. The veto list's is true | Not true: 26 items more, carrying 809 more pairs (37 items with ten or more). Say: "all 1,038 pairs, 809 more, on 26 more items and in items already selected" |

---

## What the rewrite kept of `inspection-Q3R.md`, part 2, and what it undid

- **Kept:**
  - R-1 (a `q3` reason), though R2-6 shows its corrections still can't be written;
  - R-2's `count` and `none-held` with leads;
  - R-4's `ruled differently` text (brief, line 57);
  - R-5's `strained` and `lead`;
  - R-6's coordinator rows, notes and `scope.tsv`;
  - R-7's homonym joins and `caps --terms`;
  - R-8's sample in every part;
  - R-11's commands (brief, line 29);
  - R-12's shares and a selection committed once;
  - R-13's `scope`;
  - R-14's "traces to its key".
- **Undone:**
  - **R-3** at scale: one item for 2,309 flags, given to a reviewer rather than the coordinator (R2-3).
  - **R-2**, in part: `none-held` with leads now leaves out cells the omission review won't sample (R2-4).
  - **R-9**'s per-cell grouping, carried up to capabilities, makes items of up to 30 questions under one verdict (R2-8, R2-17).
  - **R-10**'s correction "`<part>/<file>`: the row … and the new value" was never enforced beyond the file's name, and still isn't (R2-11).

---

## What I ran

All with `python3 -I`, the scripts at `9195b096`, from the frozen copy `<scratch>/snap` unless named:
- `method/review_select.py --out <scratch>/out/sel-commit.tsv --since-dir <scratch>/since`: 1,599 items, as above;
- the same with `--coord-rest 1` (1,681 items), `--one-cap-terms 1` (1,625), `--coord-rest 0.1` (1,576), and with `GM_RULINGS` set to `reports/GM-rulings.md` at `d0fb7f82` (the ruling table's last line is R-R1, "no handle");
- `method/review_select.py --out <scratch>/out/sel-real.tsv` on the working tree at `d0fb7f82`: 1,605 items, `s2-note` 11, from `held/zid/s2/S2-ZD-1.md`. `studies/class-model/review/` was absent before and after;
- with `CLASS_MODEL_DIR=<scratch>/class-model` (a copy of the frozen model):
  - `select`, which gave the same selection as the frozen run;
  - an omission fixture (`omission/parts.tsv`, `omission/OM-ZD-items.tsv`: 20 `held`, a `held` row naming the flag, a `support` miss, a `cell` miss, an `unclear` and a walked `absorbed`), giving `<scratch>/out/sel-om.tsv`;
  - a `held/zid/s2-outcomes.tsv` fixture (removed after);
  - `check --share 1 --batch 1` on 30 coverage files, each of the batch's 30 items with one fault (`<scratch>/check_tests.py`; the list below);
  - `rates` on a selection where a tenth item also carries `kind` (`<scratch>/out/sel-rates.tsv`, `<scratch>/out/rev/`);
- my own recomputations, from the merged files at `9195b096` and `9d204b46`: `changed` and `new-cap` (`<scratch>/chk_changed.py`), `kind`, `count`, `own-service`, `batch`'s reach;
- my own counts with the script's functions:
  - each high ruling's handle, pattern and lines (`<scratch>/rulings_pat.py`, `count_h.py`);
  - the Flags pattern's sample, its misses and the per-row patterns (`pat_sample.py`, `flag_recall.py`);
  - the `llms`, route-gate, maker-field and `new-caps` reach (`pat_reach.py`, `newlines.py`);
  - the coordinator's 701 by kind;
  - the loose flags by capability set;
  - `note_bullets` on six note forms (`notes_test.py`);
- `reports/GM-rulings.md`, parsed by my own script (`<scratch>/gm_list.py`) for its high entries and rows;
- `git show` of the earlier `review_select.py` (`589c6930^`), of `s2_held.py`, `O-omission.md`, `O-omission-design.md`, `S2-held.md`, `QL-qualities.md` and `PLAN.md` at `9195b096`, and of `held/zid/s2/S2-ZD-1.tsv` and `.md` at `5ba8a4e6` and `d0fb7f82`.

The drafter's fixtures (`R-revise/tests/`) were read, not run. They write a `## … (S2-R2)` heading with `-` bullets, the one form R2-13 shows is taken.

**The checker's tests.** Each is a coverage file for share 1, batch 1, of the batch's 30 items, all `holds` with the basis `SH-C-001/where/SH-S-2520`, but for one fault, on R-0002 (CM-ACC-001 on BigCommerce). "Should" is what the brief asks.
1. Every item `holds`: accepted (should accept).
2. `wrong`, correction `A-anchor/cells.tsv` alone: accepted (should refuse).
3. A correction to `Z-nowhere/cells.tsv`: accepted (should refuse).
4. A correction to `held/zid/placements-ZD-99.tsv`: accepted (should refuse).
5. A correction to `points/P-01.tsv` (the file is `P-1.tsv`): accepted (should refuse).
6. A correction to `q3/check-Q-01.tsv: km:ACC-02: result partly`: refused (should accept; R2-6).
7. A correction to `merged/cells.tsv`: refused (should refuse).
8. A correction to `held/zid/s2-outcomes.tsv`: refused (should refuse).
9. `basis` "the cell's reading": accepted (should refuse).
10. `basis` `ZD-E-deadbeef@ZD-4`: refused (should refuse).
11. `basis` `ZD-E-29f102f6@ZD-99`: accepted (should refuse).
12. `basis` `S01-SA-999`: accepted (should refuse).
13. `basis` `SA-I-9999`: refused (should refuse).
14. `basis` `SH-C-001/where/SH-S-0000`: refused (should refuse).
15. `basis` `SH-S-2520`, a bare statement id: accepted (should refuse).
16. `basis` `CM-ACC-001`: accepted (should refuse).
17. Severity `count`: refused (should refuse).
18. `holds` with severity `reading`: refused (should refuse).
19. `unclear` without what would settle it: refused (should refuse).
20. `wrong` without a correction: refused (should refuse).
21. R-0002 twice, as for two `held` verdicts on one cell: refused, "line 32: R-0002 again" (the brief asks for it; R2-2).
22. An item of another batch (R-0100): refused (should refuse).
23. A correction to `held/new.tsv`: accepted (should accept).
24. A correction to `omission/OM-ZD-items.tsv`: accepted (should accept).
25. A correction to `qualities/zid/QL-ZD.tsv`: accepted (should accept).
26. A correction to Zid's `placements-ZD-4.tsv` on a BigCommerce item: accepted (should refuse, a reading of the brief).
27. A correction to `held/zid/s2/S2-ZD-1.tsv`: accepted (should accept).
28. A double quote in `basis`: refused (should refuse).
29. R-0030 left out: refused, "R-0030 has no line" (should refuse).
30. `basis` `ZD-E-29f102f6` without its batch: accepted (should refuse).

## What I didn't check

- I reviewed no item of the selection and placed no line, beyond the examples cited. CM-PAY-010's `absent` against B-extent's `shows` (R2-4) is a reading for the review.
- The omission review's and the qualities pass's real files don't exist yet, and `om_sample.py` isn't built. The `omission` and `ql-note` reasons were tested on my fixtures and the briefs' formats only.
- I didn't run `s2_held.py`, `held_amend.py` or any landing. The second stage's `s2-outcomes.tsv` format is taken from `s2_held.py` at `9195b096` (`OUT_HEAD`, lines 100 to 101).
- I didn't verify the design's token estimate (section 3), the agents' split or the time. The counts that bear on cost (R2-15, R2-17) are item and pair counts, not tokens.
- I didn't read the evidence repositories. No claim here rests on a platform's own words beyond what the held lines and entries quote.
- The working tree moved while I worked (`5ba8a4e6`, then `d0fb7f82`). Facts are at `9195b096` unless another commit is named.
