# Review of the held pass's dry run, part R6: the join

**What this is.** Part R6 of the review that `studies/class-model/briefs/H-review.md` sets: the join of the six parts' rows and notes. It gives:
- the counts;
- the misses by cause and effect;
- the important details;
- where the parts disagree;
- the brief's ambiguities with their fixes and tests;
- what the dry run doesn't hold;
- the judgement on effort;
- the leads;
- what the batches never placed, and the notes' claims.

**What was read, pinned:**
- the six parts' rows and notes, `held/review-H-R1.tsv` to `review-H-R5b.tsv` and their `.md`, at `e18e5588`: R1 at `853dc57b`, R2 at `f0dd52bd`, R3 at `3c35d5cd`, R4 at `abfaeb98`, R5a at `689f8ff3`, R5b at `e18e5588`. The 458 rows were counted by script, with no `why` field rewritten;
- to settle where two parts disagree:
  - `briefs/B-extent.md`, "Cells and evidence" and "Conventions from the dry run";
  - `briefs/H-held.md` at `dc1e6414`. It is unchanged at `e18e5588`, so none of the fixes below is applied yet;
  - the placements' `quality` fields at the batches' commits (`ff50bbee`, `33946dbc`). Both placement files are unchanged at `e18e5588`;
- to say what the dry run doesn't hold: `held/batches.tsv` and `held/selection.tsv`;
- the checker, `method/held_entries.py check`, at `e18e5588`, with the tests `1ac89d6e` added. It was run on BC-1 and ZD-1, and it writes nothing;
- the founder's decision of 30 October on effort (`founder-decisions.tsv`, "What effort the agents run at, where the coordinator sets it").

No evidence source was re-read: B-extent's and H-held's own words settle each disagreement.

**A commit landed during the join:** `ccbb3037`. It turns BigCommerce's plan prices into one entry, `BC-E-f167af9a`, under the `meta:` rule, and adds it to BC-1 as its entry 101, for the batch's corrections. BC-1 now lists 148 entries, so its entry numbers after 100 run one higher than at `ff50bbee`. Below, BC-1's entries are numbered at `ff50bbee`, and lines are the placement file's. The check was run at `e18e5588`, before it. It changes nothing else this join reads: placements, notes, H-held.md and the checker are as above.

**The costs are facts from the session's records** (`method/count_tokens.py`), given with the request for this part:
- **BC-1:** 7.9 million tokens for 147 entries, its context growing from 49,347 to 257,452 tokens over 51 requests;
- **ZD-1:** 13.8 million for 153 entries, from 49,373 to 297,153 over 76 requests;
- **the review's parts:** R1 11.4, R2 19.1, R3 23.9, R4 17.5, R5a 16.1, and R5b about the same, in millions.

Every claim below that isn't a count or a quoted text is a reading.

## 1. Counts of verdicts

**Rows, by verdict:**

| Verdict | R1 | R2 | R3 | BC-1 | R4 | R5a | R5b | ZD-1 | All |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stands | 14 | 12 | 71 | 97 | 41 | 40 | 29 | 110 | 207 |
| wrong supports | 16 | 46 | 1 | 63 | 2 | 0 | 0 | 2 | 65 |
| missing terms | 0 | 44 | 0 | 44 | 0 | 0 | 0 | 0 | 44 |
| missing line | 5 | 18 | 3 | 26 | 3 | 10 | 2 | 15 | 41 |
| wrong reading | 5 | 22 | 0 | 27 | 2 | 0 | 3 | 5 | 32 |
| missing scope | 1 | 0 | 0 | 1 | 16 | 4 | 7 | 27 | 28 |
| can't tell | 7 | 1 | 3 | 11 | 1 | 1 | 4 | 6 | 17 |
| wrong filler | 16 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 16 |
| wrong capability | 0 | 0 | 2 | 2 | 0 | 0 | 1 | 1 | 3 |
| wrong quality | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| missing filler | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| should not be new | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| wrong terms | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| **rows** | **64** | **143** | **84** | **291** | **65** | **55** | **47** | **167** | **458** |
| **misses** | **50** | **131** | **13** | **194** | **24** | **15** | **18** | **57** | **251** |

**Lines:**

| | R1 | R2 | R3 | BC-1 | R4 | R5a | R5b | ZD-1 | All |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lines | 36 | 59 | 80 | 175 | 61 | 41 | 41 | 143 | 318 |
| stand whole | 14 | 9 | 67 | 90 | 41 | 28 | 27 | 96 | 186 |
| carry a miss | 22 | 50 | 13 | 85 | 20 | 13 | 14 | 47 | 132 |

Every line of both batches has at least one row. No line was placed `out` or `outside` (fact: the supports and `cap_id` columns of both placement files). ZD-1's lines 104 and 133 carry only a `missing line` row: their own placements stand, by R5b's notes.

**What the rows don't count, though the join finds it** (section 4):
- by D4, 50 more lines carry a mark kept as a quality: BC-1 38 to 62 but 43 and 53, 70 to 91, 169, 172, 173, 175 and 176. They are `brief`, `column`. The checker already prints them;
- by D2, 10 lines take a missing scope for a condition the rows leave out: ZD-1 80, 84, 86, 91, 92 and 99 to 103. 91 and 100 already carry a missing scope for another. They are `brief`, `column`.

## 2. The misses by cause and effect

**The effect lists differ.**
- R1, R2 and R3 worked from the brief at `2316f3ab`, which had no `held` effect. R4, R5a and R5b had it (`f0dd52bd`) and used it on no row.
- Under the definitions the brief gives now, 19 rows read `held`: R2's 15 CM-SEL-001 rows, given as `capability`, and R3's lines 112 (`column`) and 140, 157 and 168 (`count`). Each is a cell that held nothing becoming held, or a cell that the line alone holds holding nothing once the line moves.
- R2's lines 92, 94 and 96, given as `capability`, read `column`: their cells, CM-PAY-016 and CM-B2B-001, already hold `core`.
- Both counts are given below.

**Both batches:**

| Cause | held | count | kind | capability | filler | column | All |
| --- | --- | --- | --- | --- | --- | --- | --- |
| care | 0 → 3 | 2 → 0 | 0 | 2 | 11 | 85 → 84 | 100 |
| brief | 0 → 15 | 6 | 11 | 28 → 10 | 8 | 85 → 88 | 138 |
| evidence | 0 → 1 | 7 → 6 | 0 | 1 | 0 | 5 | 13 |
| tool | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **All** | **0 → 19** | **15 → 12** | **11** | **31 → 13** | **19** | **175 → 177** | **251** |

Each cell gives the effect as the rows give it, then under the brief's `held`. The brief's cause is the largest: 138 of 251 rows (55%).

**No row names the tool, though the leads lacked the right capability on 162 of 313 lines.** The parts couldn't see the leads the agents saw: the version before `99d429ad`, which inspection-HR's N-4 measured, and whose first-letter bug was fixed at `ff50bbee` (R2). So the tool's share is unknown, not nil (a reading).

### Per batch, with the lines

**BC-1: 194 misses on 85 of its 175 lines.**

| Cause | Effect (under `held`) | Rows | Lines |
| --- | --- | --- | --- |
| care | held | 3 | 112 (given `column`); 157, 168 (given `count`) |
| care | capability | 1 | 161 |
| care | filler | 9 | 14 to 21 (Feedonomics, known only from the step), 99 |
| care | column | 68 | 38 to 42, 44 to 52, 54 to 61, 70 to 91 (the term "Payment Gateway", 44 rows; the misquote, 22 on 70 to 91); 141, 148 |
| brief | held | 15 | 38, 39, 45 to 47, 52, 57, 62, 70, 71, 73, 75, 76, 81, 89 (CM-SEL-001; given `capability`) |
| brief | count | 6 | 4, 5, 9, 16, 17, 21 (CM-MKT-010 gains `own-service`) |
| brief | kind | 10 | 2, 3, 6 to 8, 14, 15, 18 to 20 (CM-CHN-004 gains `extension-point` it shouldn't) |
| brief | capability | 10 | 29, 31, 33, 35, 37, twice each (CM-APP-011's Extensions; Professional Services) |
| brief | filler | 8 | 2 to 9 (Feedonomics, a group company) |
| brief | column | 58 | 11; 29, 31, 33, 35, 37 (the definition left out); 38 to 62 but 53, 70 to 91 (the gateways' supports); 92, 94, 96 (given `capability`); 113, 119; 132 |
| evidence | held | 1 | 140 (given `count`) |
| evidence | count | 4 | 2, 14, 53, 153 |
| evidence | column | 1 | 125 |

**ZD-1: 57 misses on 47 of its 143 lines.**

| Cause | Effect | Rows | Lines |
| --- | --- | --- | --- |
| care | capability | 1 | 130 |
| care | filler | 2 | 91, 92 (Mokafaa and Qitaf, also CM-PAY-012's) |
| care | column | 16 | 3; 13, 14, 66, 69, 71, 72, 75, 82, 87, 102, 104 (a second capability); 116, 117, 141 (readings); 143 (a term) |
| brief | kind | 1 | 13 |
| brief | column | 30 | 7, 12, 17 to 26, 42, 49, 50, 54, 76, 85, 91, 100, 111, 116 to 120, 143 (scope, 27 rows); 5, 14, 18 |
| evidence | count | 2 | 126, 129 (CM-MIG-005, if a move is offered) |
| evidence | capability | 1 | 135 |
| evidence | column | 4 | 42, 100, 129, 133 |

### Per structure

| Structure | Lines | Misses | Lines with a miss | Cause and effect (under `held`) | What |
| --- | --- | --- | --- | --- | --- |
| channel-catalog | 2 to 27 (26) | 35 | 17 | care filler 8; brief count 6, kind 10, filler 8, column 1; evidence count 2 | Feedonomics of the group, read as a third party; a filler only the step names |
| contracting-entities | 28 to 37 (10) | 15 | 5 | brief capability 10, column 5 | Extensions a homonym; Professional Services unplaced; the definitions in the page beyond the segment |
| payment-gateways | 38 to 96 (59) | 131 | 50 | care column 66; brief held 15, column 49; evidence count 1 | Eight choices, most made for a whole table (R2): the supports, BigCommerce Payments, the marks' feature, the term, the misquote, the parent, the footnote, PayPal |
| plan-comparison | 97 to 123 (27) | 4 | 4 | care held 1, filler 1; brief column 2 | A tooltip's second thing (112) and wallets (99); "Available" as a quality |
| settings-list | 124 to 168 (45) | 9 | 9 | care held 2, capability 1, column 2; brief column 1; evidence held 1, count 1, column 1 | A capability where another's cell cites the place (157, 161, 168); second things in a description |
| tax-services | 169 to 176 (8) | 0 | 0 | — | — |
| dashboard-page-index | 2 to 123 (122) | 48 | 40 | care filler 2, column 14; brief kind 1, column 29; evidence column 2 | Store conditions not in scope; second capabilities; app pages |
| dashboard-route-manifest | 124 to 144 (21) | 9 | 7 | care capability 1, column 2; brief column 1; evidence count 2, capability 1, column 2 | Routes known by their names only |

### Per rule of H-held.md (`dc1e6414`)

Each miss is counted under the rule its verdict tests:
- wrong supports: rule 4;
- scope, terms, filler and quality: rule 5;
- a second capability, a wrong capability, `new`, and a `can't tell` over the capability: rule 2;
- R4's line 18, a container: rule 3;
- BC-1's lines 29 to 37 (a definition in the source page) and 96 (a footnote): rule 1;
- BC-1's 153 and ZD-1's 42 and 100 (`can't tell` over supports): rule 4;
- ZD-1's 5 (own-service's gap): rule 4;
- the other readings: rule 7.

| Rule | Rows | Care | Brief | Evidence | Lines |
| --- | --- | --- | --- | --- | --- |
| 1, read it as the platform states it | 6 | 0 | 6 | 0 | BC-1 29, 31, 33, 35, 37, 96 |
| 2, place it | 57 | 20 | 27 | 10 | BC-1 2, 14, 29 to 37 (odd), 38, 39, 45 to 47, 52, 53, 57, 62, 70, 71, 73, 75, 76, 81, 89, 92, 94, 112, 125, 140, 141, 148, 157, 161, 168; ZD-1 13, 14, 66, 69, 71, 72, 75, 82, 87, 91, 92, 102, 104, 126, 129 (twice), 130, 133, 135 |
| 3, sub-pages and containers | 1 | 0 | 1 | 0 | ZD-1 18 |
| 4, `supports` | 69 | 0 | 66 | 3 | BC-1 2 to 9, 14 to 21, 38 to 62 but 53, 70 to 91, 132, 153; ZD-1 5, 13, 14, 42, 100 |
| 5, the other columns | 92 | 54 | 38 | 0 | scope: BC-1 11; ZD-1 7, 12, 17 to 26, 42, 49, 50, 54, 76, 85, 91, 100, 111, 116 to 120, 143. Filler: BC-1 2 to 9, 14 to 21, 99. Terms: BC-1 38 to 61 but 43 and 53, 70 to 91; ZD-1 143. Quality: BC-1 113, 119 |
| 7, `reading` | 26 | 26 | 0 | 0 | BC-1 70 to 91; ZD-1 3, 116, 117, 141 |

**Rule 1 holds few rows, but every part names it.**
- Whether a run step, a run's answer, a locale string or another source of the batch may be read is the ambiguity all six parts raise.
- Verdicts in every part rest on such files (fix FX-1).
- Rules 4 and 5 carry most of the brief's misses: rule 4 by its restatement of B-extent, rule 5 by its scope.

### Per third of each batch's lines

**Lines:**
- BC-1's thirds are lines 2 to 59, 60 to 117 and 118 to 176;
- ZD-1's are 2 to 48, 49 to 96 and 97 to 144.

"Important" is the sense of section 3: the effects but `column`, under `held`, and a second capability left without its line.

| Third | Misses | Lines with a miss | Care | Brief | Evidence | Care misses of an important detail |
| --- | --- | --- | --- | --- | --- | --- |
| BC-1, 1st (58 lines) | 99 | 44 (76%) | 28 | 68 | 3 | 14 to 21: one choice |
| BC-1, 2nd (58) | 85 | 31 (53%) | 48 | 37 | 0 | 99, 112 |
| BC-1, 3rd (59) | 10 | 10 (17%) | 5 | 2 | 3 | 141, 148, 157, 161, 168 |
| ZD-1, 1st (47) | 21 | 17 (36%) | 3 | 17 | 1 | 13, 14: one choice |
| ZD-1, 2nd (48) | 15 | 14 (29%) | 9 | 6 | 0 | 66, 69, 71, 72, 75, 82, 87, 91, 92 |
| ZD-1, 3rd (48) | 21 | 16 (33%) | 7 | 8 | 6 | 102, 104, 130 |

**A reading: the misses don't grow toward either batch's end.**
- BC-1's fall from 76% of lines to 17%. ZD-1's stay at about a third.
- The care misses of an important detail are few: 20 distinct choices in all. Counted as choices, they are 1, 2 and 5 on BC-1, and 1, 8 and 3 on ZD-1. They are fewer in the first third than after it, in both batches.
- Each later third is also another kind of entry:
  - on BC-1, the settings-list's one-line descriptions, which R3 says need the most judgement;
  - on ZD-1, the settings, notification and marketing pages whose descriptions name more than one thing.
- On ZD-1 the later third is also another reviewer. The same kind of page, settings pages described on `gaps-en#2`, shows no care miss in R4's lines 43 to 62 and five in R5a's lines 63 to 75.
- The placing agent's own behaviour doesn't fall with position. ZD-1 wrote lines on two capabilities for 4 of its 153 entries, 1, 2 and 1 by third (fact, from the placement file). BC-1 did so for 14, 3 and 7.
- So position can't be told from kind or reviewer, and the thirds don't point to size.
- **What would settle it:** one fresh batch of the entries on ZD-1's lines 43 to 80 (the settings pages on both sides of R4's and R5a's boundary), placed at `high` and reviewed by one agent.

## 3. The important details

The founder's decision of 30 October reads: "Where `high` or `xhigh` consistently misses important details for a type of task, evidence review above all, that type runs at `xhigh` or `max`", judged "by the quality and completeness of their results".

**R6 takes as important a miss that changes what the model says a platform does, or who does it:**
- **`held`, `count`, `kind` and `capability`:**
  - whether a cell holds anything;
  - its `core` and `own-service`;
  - its `extension-point` and `outside`;
  - which capability holds the entry, or whether one is made.

  These are "what the coordinator's count of the class reads" (B-extent, Cells and evidence).
- **`filler`:** the third party or law that does the work or sets its terms, from which "the coordinator computes the kind" of slot (B-extent). A company of the group taken for a third party, as Feedonomics was (R1), also turns maker evidence the wrong way.
- **A second capability the entry is, left without its line, whatever its effect.** It is evidence a cell lacks, and whether it changes the cell depends on the cell, not on the miss:
  - it is `column` on ZD-1's lines 13, 14 and 66 to 104, whose cells already held `core`;
  - the same miss is `held` on BC-1's lines 38 to 89 and 112, whose cells held nothing.

**Not important on its own:** the rest of `column`, that is scope, terms, quality and readings. Two of these matter for quality, not for effort:
- **a reading that misstates its source** goes into the model's evidence as `held_amend.py` writes it: BC-1 70 to 91; ZD-1 3, 116, 117 and 141. The checker's quote test now notes the quoted ones;
- **a scope a store condition sets** says for which stores the model holds a page (27 rows on ZD-1). Every one of these misses is the brief's.

**So counted: 92 of the 251 misses are important details.** By cause:
- **brief:** 54;
- **evidence:** 9;
- **care:** 29, on 29 lines. These are the misses effort can bear on:
  - BC-1 14 to 21, 99, 112, 141, 148, 157, 161, 168;
  - ZD-1 13, 14, 66, 69, 71, 72, 75, 82, 87, 91, 92, 102, 104, 130.

## 4. Where the parts disagree, and what settles each

**D1. A listed page's `beta` badge.**
- **The two readings:**
  - R4 calls it a method ruling and leans to `shows`, by H-held's flag clause, which counts "a beta" as not released;
  - R5a keeps `core` with the badge in `reading`, within B-extent. Line 90, Customer Referrals, stands.
- **B-extent settles it, for R5a.**
  - Its one release clause is "A feature flag that isn't released (`"released": false`) is `shows`".
  - Its `core` names "its own admin section, setting, route".
  - A page the page index lists is the platform's own route. Its badge is a release marker, which H-held's own help-page clause sends to `reading` ("A release marker in it (beta, deprecated, sunset, now available) goes in `reading`").
  - H-held's "a beta" is a restatement that reads differently from B-extent, and the review brief makes B-extent govern.
- A method ruling would remain only for a badged page the platform states can't be used. The dry run holds none.
- Fix FX-11.

**D2. A page listed only under a store condition.**
- **Three readings:**
  - **R4:** a condition the platform sets for a store (a flag, a kind of store) is `scope`, in the source's identifier. One on the store's own data (a blog turned on, an app installed) goes in `reading`. A method ruling;
  - **R5a:** a named condition (`customerWallets`, `showNewZones`) is `scope`. A computed one (`be`, `xe`, the `nt` store list, `s`) goes in `reading`. A method ruling;
  - **R5b:** every condition is `scope`, a minified one named by the module it is imported from (`use-is-ngo-store`), marked as a reading. Within B-extent.
- **What settles it.**
  - B-extent settles named store flags: "A released flag supports `core`, with its plan or store as its scope." These are `customerWallets`, `showNewZones`, `hasNewGifting`, `mustUseMarketsPricing` and `hasPos`.
  - It says nothing of a kind of store, a store's state or a computed condition. Those are method ruling M-11.
- **R6's lean, a reading:** R4's split with R5b's naming. A condition left in `reading` reaches the cell only as text, since `class_slice.py` reads an entry's scope from its placement's `scope` (fact, `held_amend.py`, its header).
- **The counts:**
  - under R4's and R5b's rule, 10 more lines carry a missing scope: R5a's lines under the donation condition (80, 86 and 99 to 103; 100 adds it to its `showNewZones`), and its computed ones (84, 91, 92);
  - under R5a's rule, R4's 12 charity-condition rows (7, 12, 17 to 26) and R5b's 111 would be missing readings instead.
  - Every such row is `brief`, `column`, and no count changes either way.
- Fix FX-14.

**D3. A container that no capability holds.**
- **The readings:** R4 makes it a method ruling. R5a writes `new:<title>`, `shows`. R5b writes `new`, and `core` for a container placed on a capability.
- **B-extent's reading is `new:<title>`, `core`:**
  - a section the navigation names with its own title is a place of its own;
  - a place of its own whose thing no capability holds makes one;
  - `core` names "its own admin section".
- R5a's `shows` isn't B-extent's.
- No container in the dry run lacks a capability (each part says so), so the dry run sets nothing here.
- What stays a method ruling (M-13) is whether a section whose title names only a grouping ("Store", "Channels") is a thing at all, or only its children's `parent`.
- Fix FX-7.

**D4. A mark as a quality.**
- **The readings:**
  - R2 lets the gateways' marks ("Recurring Payments: ✔") stand as qualities, by H-held's rule 5, as the review brief told it to judge qualities. Its M3 names the question;
  - R3 rules that a mark of inclusion is never a quality (its F2, within B-extent). Its lines 113 and 119 are `wrong quality`;
  - the checker at `1ac89d6e` follows R3.
- **B-extent settles it, for R3:** a quality is "a limit, a certification, an uptime or a data location", and a mark is none of these.
- **So 50 lines carry a miss no row counts:**
  - R2's 45 marked lines (38 to 62 but 43 and 53, and 70 to 91);
  - R3's five tax lines with `document_submission supported: true` (169, 172, 173, 175, 176).

  They are `brief`, `column`.
- **The checker:** it prints them, 165 PROBLEMs on 50 lines. It misses R3's own two lines, "Custom SSL: Available (Scale), Available (Performance)" and the Shipper HQ line (113, 119), because it compares the whole value, plans and all (fact, `held_entries.py`, `MARKS`).
- Fix FX-16.

**D5. The effect of a missing line on a capability that exists.**
- **The parts' values:**
  - R2 gave `capability` to its 18;
  - R3 gave `column` and `count` where the cell held nothing (112; 140, 157, 168);
  - R4, R5a and R5b gave `column` where the cell holds the value.
- **The brief's definitions settle it:**
  - `held` where a cell that held nothing becomes held, or would hold nothing;
  - `column` where the cell keeps its placements;
  - `capability` only for a capability made or not, or an entry moved.
- Section 2 gives both counts.

**D6. A scope or quality from a page beyond the entry.**
- **The readings:**
  - R5a's line 91 takes "Saudi Arabia" from the run page as a missing scope (`brief`), and its notes hold the Mokafaa and Qitaf rates from the page as qualities in waiting;
  - R4's F1 keeps scope, filler and quality to the entry and its source.
- **B-extent settles it, for R4:** "a statement's scope stays its own", and the statement is the entry.
- Line 91's row is a miss only if the coordinator rules that a run page's text can be a statement (M-12).

**D7. What rule 1 allows as written.**
- **The readings:**
  - R4 says it reads two ways, since the reading list names `index/` and the ledger joins routes to steps;
  - R3, R5a and R5b say run steps aren't allowed as written.
- **H-held's text settles it, for the three:**
  - rule 1 names "its item at the source and locator `entries.tsv` gives";
  - the reading list names `index/` "by their rows" among the repository guides, and never `raw/runs/`, a run's answers or the locales.
- All four propose the same fix (FX-1).

**D8. The platform's own list of third parties' services.**
- **The readings:**
  - R1 makes it method ruling M2 whether the channel catalog is "something the platform provides";
  - R3 reads the Tax page's list, which installs each service as an app, as `extension-point` within B-extent.
- They don't conflict:
  - where an item installs an app (an `app_id`, an App Marketplace link: BC-1's tax services, line 27, R2's table 2), B-extent's "app-store or marketplace category" covers it;
  - where a card shows neither an app nor an interface (line 13, DEITY), R1's M2 remains (M-3).
- Fix FX-13.

**D9. `in_leads` on a `can't tell` row.**
- R1 answers for the capability the row names; R3 for the line's own.
- Section 8 counts each line's own capability, or the one a `wrong capability` or `should not be new` row names.

## 5. The brief's ambiguities: the fixes, their standing, and the checker

### Fixes to H-held.md

Each fix gives its words to paste, the lines it touches, whether it stays within B-extent, and the checker test. A test marked "at `1ac89d6e`" is in the checker now.

**FX-1, rule 1: what else may be read** (all six parts: R1 F3, R3 F3, R4 F1, R5a F1, R5b; D6, D7). Add to rule 1:
> **What else you may read to clarify it.** The structure's source is the file its `meta.json` names under `source` (`held_as`; `url` with `held_in`; `answer`) and the `source.*` file beside `items.jsonl`. Where `source.*` is a segment of a page, read the page around it for the definitions and the clause its words sit under, and compare its rows with the page's. You may also read the run steps `index/` names for the structure or the entry's route (`index/runs.tsv`, `index/ledger/`), the answers received at those steps, and, for a route no run opened, the locale strings of its own namespace. Cite each by file and line, or by run and step, quote it exactly, and mark the reading as one. They clarify what the entry is and whom it names. They never become entries, and the entry's `scope`, `filler` and `quality` come from its own words and its structure's source.
- **The lines whose verdicts rest on such files:**
  - BC-1 2 to 9 and 14 to 21 (the terms page, for the group), 29 to 37 (its definitions), 169 and 171 (steps 43 and 45);
  - ZD-1: 45 of R4's 61 readings and 39 of R5a's 41 (run pages); 7, 12 and 17 to 26 (the locales, for the charity condition); 104 and 110 (run steps); 125, 127, 130, 133, 134 and 142 (the locales).
- **B-extent:** within it, the entry staying the statement. Two method rulings remain: M-12, and M-1 (FX-9).
- **Test:** the quote NOTE (at `1ac89d6e`) searches the entry, the structure's sources and the run pages. Add the locales and the runs' answers, and check each quote against the file the reading cites. It then catches ZD-1 141, which cites steps whose text lacks the words, and clears 125 and 142, whose quotes are true.

**FX-2, rule 1: footnotes** (R2's fix 6). Add:
> A footnote that a mark of the entry points to (an asterisk on a value or a name) is part of the entry's text: place what it states.
- **Lines:** BC-1 96, and 91.
- **B-extent:** within it.
- **Test:** the footnote NOTE, at `1ac89d6e`, prints line 96.

**FX-3, rule 2: every thing the entry's words name** (R1 F5, R2 fix 4, R3 F4, R5a F2). Replace "Where the entry is two capabilities' at once, write two lines with the same `entry_id`, each with its own `supports` and `reading`" with:
> Read each thing the entry's words name: its title, its description or tooltip, a feature it marks, the page it opens. Where the entry is two or more capabilities' at once, write a line for each, with the same `entry_id` and its own `supports` and `reading`, even where that cell already holds `core`. Before you write one line, read the entry's leads and the cells of the capabilities its words name: where a cell's reading cites the same page, place or term, the entry is that capability's too. A second thing no capability holds takes its own `new` line.
- **Lines** (the 41 `missing line` rows):
  - BC-1 29 to 37 odd, 38 to 89 (CM-SEL-001), 92, 94, 96, 112, 141, 148;
  - ZD-1 13, 14, 18, 66, 69, 71, 72, 75, 82, 87, 91, 92, 102, 104, 133.
- **B-extent:** within it.
- **Test:** none at `1ac89d6e` catches a missing line. Two of its tests point at some:
  - the mark PROBLEM's message ("a statement of the marked thing") points at the 15 CM-SEL-001 lines;
  - the footnote NOTE points at 96.

  New: a NOTE for each lead that matched a word of the entry's own text (not an identifier) and whose capability no line of the entry places, with the lead's cell. It reaches the 24 of the 36 missing lines on a capability that exists whose capability is among the leads now.

**FX-4, rule 2: the cells that cite the same place** (R3 F5, R5a F2). Add:
> Before you place a section, a route or a setting, search the model for its own place, as the navigation names it ("Settings > API and MCP > MCP") and by its path. Where another capability's cell already cites that place, the entry is that capability's.
- **Lines:** BC-1 168; ZD-1 69 and 71.
- **B-extent:** within it ("A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence").
- **Test:** the CHANGES print (at `1ac89d6e`) puts 157 and 168 in front as cells one line makes held. New: a NOTE for an entry whose place or path another capability's cell cites (`class_slice.py search`).

**FX-5, rule 2: `new` against its parent's cells** (R3 F6). Add:
> Where you would name a capability as a new thing's parent, read that capability's cells first: a place whose thing it already holds is its evidence, not a new thing.
- **Line:** BC-1 161 (CM-CNT-001).
- **B-extent:** within it; this is its own last sentence of "What a place of its own is".
- **Test:** new: a NOTE for a `new` line whose parent, named in the notes, is among the entry's leads.

**FX-6, rule 2: homonyms** (R1 F7, R5a F6). Add:
> Before you place a term on a capability that uses the same word, read the term's definition where the entry's source holds one, and the capability's note. Where the note names a homonym whose words the entry holds, place the entry where the note sends it, and say so in `reading`.
- **Lines:** BC-1 29 to 37 (Extensions; M-2); ZD-1 91 (CM-LOY-004's note on مكافأة الراجحي).
- **B-extent:** within it ("Names").
- **Test:** new: a NOTE for each line whose capability's note holds "Homonym" and a term the entry's text holds. It catches 91. It doesn't catch 92, or BC-1's Extensions, which no note names.

**FX-7, rule 3: containers** (R4 F6, R5a F3, R5b; D3). Replace rule 3's second point with:
> A container (an entry its structure gives children, such as Settings, Payments, Marketing or Apps) is a place of its own where the navigation or page index names it with its own title, and never `out`. Place it on the capability whose thing its title names, as the cells' readings show; where its title names only a grouping, on the capability whose page its own path opens. Where its own page holds another capability's thing, write that line too. Where no capability holds its thing, write `new:<title>`, `core`, and list its children in your notes.
- **Line:** ZD-1 18 (Inventory).
- **The containers that stand:** ZD-1 2, 27, 32, 36, 43, 63, 68, 81, 94, 99, 106, 113 and 121.
- **B-extent:** within it, with `core` for a `new` container as R6's reading of D3. M-13 remains.
- **Test:** new: a NOTE for each entry whose key prefixes other entries' keys in its structure, for a second line. It catches 18. With the build's container mark (B-4), a NOTE for every container line.

**FX-8, rule 4: B-extent's own clauses** (R1 F1, R2 fix 2, R3 F1, R4 F2 to F4). Replace rule 4's `core`, `own-service` and `extension-point` bullets with:
> - `core`: the platform itself does it for the merchant: its own admin place, setting, route, plan line or staff permission, its own API for its own feature, or a built-in feature it states;
> - `own-service`: the entry names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service that does it. A brand in a product's name, a field's value such as `type: salla`, and a capture's label never name a maker. Without a statement naming the company, place the line by what the entry shows, and say in `reading` that the maker statement is missing, a gap;
> - `extension-point`: the entry shows third parties doing it through something the platform provides: an app store's category, an extension target, a provider interface, or an app's page (a route named for an application and open only to the apps permission).
- **Lines:** BC-1 2 to 9, 14 to 21, 62, 132, 153; ZD-1 5, 13, 14.
- **B-extent:** within it: its clauses, in its words.
- **Tests at `1ac89d6e`:**
  - the NOTE for `extension-point` or `outside` on an entry naming a group company (BC-1 2 to 9);
  - the NOTE for `core` on a product named with the brand (BC-1 62; ZD-1 5);
  - CHANGES (BC-1 2 to 21; ZD-1 13).
- **New tests:**
  - a NOTE for every `extension-point` line, as the checker prints one for `own-service` (ZD-1 13, 14);
  - a NOTE for `core` on a capability whose name gives the work to third parties (R3's T2: BC-1 132, 153).

**FX-9, rule 4: a company of the group named outside the entry** (R1 F1; M-1). Add to `own-service`:
> A company that a held statement places in the platform's group, in the entry, in another source of your batch (a terms page's parties or contracting entities) or in the cell's own maker evidence, is the platform's: cite that statement in `reading`. A named company that no held statement places in or out of the group is not a third party for that reason: place the line by what the entry shows, and note the gap.
- **Lines:** BC-1 2 to 9, 14 to 21. The terms page names Feedonomics Holdings, LLC among Commerce's affiliates and subsidiaries, and as a Contracting Entity.
- **B-extent:** the gap clause is within it. Maker evidence from another source of the batch is method ruling M-1, which the model's own CM-CHN-004 cell already follows for BC-S-0366.
- **Test:** at `1ac89d6e`, the checker's `GROUP` list, the companies each platform's CM-ACC-002 cell names, gives:
  - a PROBLEM for a group company as a filler;
  - a NOTE on `extension-point` that names one.

  The list is fixed per platform. A group company that a batch's own terms name and CM-ACC-002 doesn't escapes it, so the batch's notes name it and the coordinator adds it.

**FX-10, rule 4: a row of a table in an article** (R2 fixes 1 and 2; M-4). Add:
> A row of a table, or an item of a list, inside an article (a help page, a plan page, a guide) is read with the words the article gives it: its table's heading, the paragraph before it, its columns' definitions, and the footnotes its marks point to. The help-page clause covers an entry that is only a page's title. A list of third-party providers that the platform's own words call its integrations is `core`, each provider its filler; one the words call apps, or that links to the app store, is `extension-point`; a bare list of names is `shows`.
- **Lines:** BC-1 38 to 61 but 53, and 70 to 91.
- **B-extent:** within it. It is the model's own reading of BC-S-0150 (`core`) and BC-S-0142 (`shows`). Table 3, "payment gateway integrations" that BigCommerce "supports" with no builder named, is M-4.
- **Test:** none decides supports. A NOTE for each `shows` line whose term is one of a `core` cell's terms on the platform (R2) would have put the 44 lines in front.

**FX-11, rule 4: flags and badges** (R4 F7, R5a F4; D1). Replace the flags bullet with:
> **flags:** a released flag supports `core`, with its plans or store as its `scope`. A flag the platform states isn't released (`released: false`, `is_experimental: true`) is `shows`. A page or route the source lists with a badge (`new`, `beta`) or a dot is the platform's own: its `supports` stand, and the badge goes in `reading`. A flag named for a third party is the capability's evidence, never a slot filler.
- **Lines:** ZD-1 5 and 14 (badge `new` left out of the reading) and 90 (`beta`, stands).
- **B-extent:** within it (D1).
- **Test:** none, while the entries don't carry the badge (B-4). With it, a PROBLEM for a badged entry whose reading doesn't name its badge.

**FX-12, rule 4: an app's page with no maker or gate** (R4 F2; M-10). Add:
> An app's page that names no maker and shows no apps-permission gate (an embedded app page the navigation lists under the platform's brand) supports `shows` on what the app does. The page itself is CM-APP-007's (Embedded app page), `core`.
- **Lines:** ZD-1 13 (Zid Ads) and 14 (Zid Voice).
- **B-extent:** the `shows` is M-10; the CM-APP-007 line is within it.
- **Test:** new: a PROBLEM for an entry whose text holds `/embedded` and has no line on CM-APP-007.

**FX-13, rule 4: a catalog or list of third parties' services** (R1 F6, R3 F1; D8). Add:
> A card or item of the platform's own catalog of channels or services takes its supports from whom it names doing the work: no one, or only the venue (a marketplace, an ad platform), `core` with the maker gap noted; a third party it installs as an app or connects through the platform's interface, `extension-point`; a company of the platform's group, `own-service`. The venue is the slot filler.
- **Lines:** BC-1 2 to 27, 169 to 176.
- **B-extent:** within it where the item installs an app or names an interface. For a card that shows neither (BC-1 13), M-3.
- **Test:** none.

**FX-14, rule 5: `scope`** (R1 F4, R4 F5, R5a F5, R5b; D2). Replace the `scope` bullet with:
> `scope`: the plan, country, market, store or store condition the entry states it for, in its words or its source's. Where the source lists the entry only under a condition the platform sets for a store, write the condition in the source's identifiers: a store flag (`customerWallets`, `showNewZones`, `hasPos`), a store's state (`subscription.is_trial`, a parent route `$lang.suspended.$storeId`) or a kind of store (`use-is-ngo-store`). A condition named only by a minified variable takes the name of the module it is imported from or of what it is computed from, and the reading says so. A condition on the store's own data (a blog the merchant turns on, an app installed) goes in `reading`. Where your reading rests on the source's words for a plan, a country or a store (a region's "with paid plan"), put them in `scope`.
- **Lines:**
  - the 28 `missing scope` rows: BC-1 11; ZD-1 7, 12, 17 to 26, 42, 49, 50, 54, 76, 85, 91, 100, 111, 116 to 120, 143;
  - by D2, ZD-1 80, 84, 86, 91, 92 and 99 to 103.
- **B-extent:** within it for named store flags. For kinds, states and computed conditions, M-11.
- **Test:** none can, while the entries don't carry the condition. Once B-4 renders it as `listed_if`, a PROBLEM for a conditioned entry with an empty `scope`. For the manifest, a NOTE for a line whose entries' `parentId` names a store state and whose `scope` is empty (ZD-1 143).

**FX-15, rule 5: `filler`** (R1 F2, R3's T5). Replace the `filler` bullet with:
> `filler`: a third party or a law the entry's own words name as doing it or setting its terms. A party known only from the source (a link, a sibling card, a region's heading) goes in `reading`, never in `filler`, and a company of the platform's group is never a filler. A party the entry names whom the cell already holds as a filler for the same kind of line is a filler here too.
- **Lines:** BC-1 2 to 9, 14 to 21, 99.
- **B-extent:** within it.
- **Tests:** at `1ac89d6e`, the two filler PROBLEMs catch all 16 of lines 2 to 9 and 14 to 21. New: a NOTE for an empty `filler` where the entry names a party the same cell holds as a filler (99).

**FX-16, rule 5: `quality`** (R3 F2; D4). Replace the `quality` bullet with:
> `quality`: a limit, a certification, an uptime or a data location the entry states, as `<what>: <value in its words>`, by plan where the entry gives one. A mark that a thing is included or supported (a check mark, "Available", "Included", "Yes", `true`) is never a quality: on a plan table it gives the line its `scope`, the plans marked; on a provider's row it is a statement of the marked feature, placed on that feature's capability (rule 2).
- **Lines:** BC-1 113, 119; by D4, also 38 to 62 but 43 and 53, 70 to 91, 169, 172, 173, 175 and 176.
- **B-extent:** within it; these are its words.
- **Test:** at `1ac89d6e`, the mark PROBLEM catches a bare mark. To catch 113 and 119, drop each parenthesized plan from the value and test each comma-separated piece.

**FX-17, rule 5: `terms`** (R5b). Add:
> A term is the platform's word for the thing, never the store's state or a parent route's name.
- **Line:** ZD-1 143 (`suspended`).
- **B-extent:** within it.
- **Test:** new: a NOTE for one term on lines of different capabilities in one structure.

**FX-18, rule 7: `reading`** (R2 fix 5, R5b). Add:
> A quote in `reading`, in single quotes, is copied exactly from the entry's text or from the file the reading cites, which it names. A reading that says what a cell holds quotes the cell.
- **Lines:** BC-1 70 to 91; ZD-1 3, 116, 117, 141.
- **B-extent:** within it ("No claim goes beyond what a cited statement says").
- **Test:** at `1ac89d6e`, the quote NOTE catches BC-1 70 to 91 and ZD-1 141. Nothing catches 3, 116 or 117, whose claims carry no quote.

### The checker, per recurring miss

Run at `e18e5588` on the batches' placements:
- **BC-1:** 189 PROBLEMs, 37 NOTEs and 23 CHANGES lines;
- **ZD-1:** no PROBLEM, 4 NOTEs and 24 CHANGES lines.

| Recurring miss | Lines | Caught at `1ac89d6e`? | New test that would catch it |
| --- | --- | --- | --- |
| A company of the group read as a third party | BC-1 2 to 9, 14 to 21 (32 rows) | yes: a group filler is a PROBLEM on all 16; the group NOTE on 2 to 9; CHANGES on all 16 | add to `GROUP` each group company a batch finds (FX-9) |
| A filler the entry doesn't name | BC-1 14 to 21 | yes (PROBLEM) | — |
| A second capability without its line | 41 rows; care: BC-1 112, 141, 148; ZD-1 13, 14, 66, 69, 71, 72, 75, 82, 87, 91, 92, 102, 104 | no; the mark PROBLEM and the footnote NOTE point at BC-1 38 to 89 and 96 | the unplaced-lead NOTE (FX-3, 24 of 36); `/embedded` without CM-APP-007 (13, 14); the container NOTE (18); a line's term that is another cell's term (92, 94) |
| A store condition not in scope | ZD-1 27 rows; up to 10 more by D2 | no: the entries don't carry it | `listed_if` (B-4), then a PROBLEM for an empty scope; the `parentId` NOTE (143) |
| A reading that misquotes or misstates its source | BC-1 70 to 91; ZD-1 141; and 3, 5, 116, 117; BC-1 29 to 37 | the quoted ones: yes (NOTE on 70 to 91, 141); ZD-1 5 by the brand NOTE | the quote test against the cited file, the locales and the answers (FX-1); none for unquoted claims |
| The supports of an article's table rows | BC-1 38 to 61, 70 to 91 | no | a NOTE for `shows` on a `core` cell's term (FX-10) |
| A mark as a quality | BC-1 113, 119; by D4, 50 more lines | the 50: yes (165 PROBLEMs); 113 and 119: no | strip plans in parentheses before the mark test (FX-16) |
| A capability or `new` where a cell holds the place or thing | BC-1 157, 161, 168; ZD-1 130 | 157, 168 as CHANGES; 161 printed as NEW; 130 no | the place-cited NOTE (FX-4); the parent-lead NOTE (FX-5) |
| An app's page read as `extension-point` | ZD-1 13, 14 | 13 as CHANGES | a NOTE for every `extension-point` line (FX-8) |
| A brand-named product's supports, or its gap | BC-1 62; ZD-1 5 | yes (the brand NOTE) | — |
| A footnote | BC-1 96 | yes (NOTE) | — |
| The term "Payment Gateway" | BC-1 44 lines | no | none reliable (R2); one choice down a table |

**What CHANGES prints is a prompt, not a verdict.** Of its 47 lines on both batches, the review finds a miss behind:
- BC-1 2 to 21 (CM-CHN-004, CM-MKT-010), 140, 153, 157 and 168;
- ZD-1 13, and 126 and 129, which are `can't tell`.

The rest stand.

### The build, not H-held.md

- **B-1, channel-catalog** (R1): label each entry with the store it was shown to (`meta.json`'s `source.store`: trial store, Oman, OMR). The list follows the store's country, and the 11 fillers on lines 2 to 27 then get a market.
- **B-2, tax-services** (R3's F8): label each entry with the store's default countries under which the list was offered: the United States, Oman, the United Kingdom and Saudi Arabia, one answer.
- **B-3, plan-comparison** (R3's F7):
  - the `meta:` rule for `prices_above_the_table` is done at `ccbb3037`, during this join: the prices are BC-1's entry `BC-E-f167af9a`, to be placed in its corrections;
  - the billing toggle ("Annual (Save 25%)", "Monthly") and the GST line are in neither the items nor `meta.json`, which is the extractor's, read-only here. Under FX-1 the pass reads step 4's text as the structure's `held_as`.
- **B-4, dashboard-page-index** (R4, R5a F7, R5b): carry into each entry:
  - each page object's permission;
  - its badge;
  - its listing condition (`listed_if`);
  - both titles of a conditional title (the charity store's);
  - a container mark (`children`).

  This makes FX-7, FX-11 and FX-14 testable, and CM-SEL-007's titles reachable (M-14).
- **B-5, dashboard-route-manifest** (R5b): render each route's module and its imports' names, without their hashes.
- **B-6, contracting-entities** (R1): the segment ends at the byte where the grid's Feedonomics cell begins. The grid's last two rows are in `TERMS` only, as the evidence map records since `853dc57b`.
- **B-7, payment-gateways** (R2): the items hold the four tables only. The article's prose, 19 things in R2's list, is reachable only through FX-1 (the `held_as` text).

### The review brief, for any later review

- **H-review, "What to check", 4:** qualities are judged by B-extent's definition, as `supports` is (D4).
- **`in_leads`:** say which capability it answers for on a `can't tell` row (D9).
- **A line whose own placement stands beside a `missing line`** carries a `stands` row too (ZD-1 104 and 133 have none).
- **Already corrected at `f0dd52bd`:** the R2 premise (the "65" phrase is BC-S-0150, not the article's) and the `held` effect.

### Method rulings for the coordinator's next report

| # | Question | Lines | From | R6's lean, a reading |
| --- | --- | --- | --- | --- |
| M-1 | Does maker evidence held in another source of the batch (a terms page) count for an entry's line? | BC-1 2 to 9, 14 to 21 (32 rows rest on it) | R1 M3 | yes, as CM-CHN-004's cell reads BC-S-0366 |
| M-2 | Does CM-APP-011, "Apps made by the platform's company", hold Extensions "developed by a third party but implemented and provided by Commerce"? | BC-1 29 to 37; CM-APP-011's own cell | R1 M1 | — |
| M-3 | Is the platform's own catalog of channels "something the platform provides" for `extension-point`, where a card shows no app? | BC-1 13 | R1 M2; D8 | — |
| M-4 | Open Payment Providers, "payment gateway integrations" with no builder named: `core` or `shows`? | BC-1 70 to 91 | R2 M1 | `core`, as R2 rules |
| M-5 | May an entry take a provider's role (instalments, crypto) from other platforms' cells? | BC-1 40, 41, 49, 51, 54, 61, 72 | R2 M2 | no, as H-held says |
| M-6 | Is an entry on a child capability cited on its parent too? | BC-1 92, 94 | R2 M4 | — |
| M-7 | Accounting at `/admin/apps/accounting`: `core` or `extension-point`? | BC-1 153 | R3 M1 | — (the page would settle the fact) |
| M-8 | A third party's own feature in its listing (Avalara's filing) on CM-TAX-006? | BC-1 170 | R3 M2 | — |
| M-9 | Does a plan tooltip's "or even a loyalty program" include it? | BC-1 112 | R3 M3 | — |
| M-10 | A page the navigation lists under the brand at an app's address, no maker or gate stated | ZD-1 13, 14 | R4 MR1 | `shows`, as R4 rules |
| M-11 | A listing condition other than a named store flag (a kind of store, a store's state, a computed condition) as `scope` | ZD-1 7, 12, 17 to 26, 80, 84, 86, 91, 92, 99 to 103, 111, 116 to 120, 143 | R4 MR2, R5a; D2 | `scope`, as FX-14 |
| M-12 | Can a run step's or a locale's text itself be a statement? | It would hold CM-INV-004, CM-MKT-023 and CM-ORD-014 on Zid; fillers for CM-CHN-004; Zid Insights' trial; line 91's Saudi Arabia; the Mokafaa and Qitaf rates | R4 MR3; D6 | — |
| M-13 | Is a section whose title names only a grouping a thing, or only its children's `parent`? | none in the dry run | R4 MR4; D3 | — |
| M-14 | Can a conditional title, the charity store's, be read as a statement of its own? | CM-SEL-007 on Zid | R4 MR5 | — |

Two questions are settled within B-extent here, not method rulings: the `beta` badge (D1) and a mark as a quality (D4).

## 6. What the dry run doesn't hold, and so sets nothing for

**Of the 144 structures the 70 batches hold, BC-1 and ZD-1 hold 8** (fact, `held/batches.tsv`). One of the 8 only in part: ZD-1 holds 34 of the route manifest's routes, all outside a store. Its in-store routes are ZD-2 to ZD-4's. The other 68 batches hold 14,580 entries.

**Values and rules the dry run never tests:**
- **`out` and `outside`:** no line takes either. H-held's out list and the `outside` value are untested.
- **Flags:** none held. They are in ZD-4, WC-2, SH-14, SA-8, SA-12 and SA-21. The flag clause is untested, and D1's badge is the nearest case.
- **Lists of staff or partner permissions:** none held. They are in SH-2, SH-3, SH-11, SH-12, SH-20, SA-11, SA-12, SA-15, ZD-4 and WC-2. S7 is untested, and ZD-1's access requests by Zid's own team (125, 127, 134) are the nearest case.
- **`boundary` structures:** none held. These are scopes, extension targets, webhook events, API groups and REST controllers: SH-12, SH-27, SA-12, SA-13, WC-2 and WC-3. B-extent's API conventions are untested.
- **Changelogs and help notes:** none held. They are in SH-15 to SH-17 and SA-1. The help-page clause is tested only by R2's finding that it doesn't reach a table row.
- **Renderings:** none of the selection's `nested:`, `json:`, `text:`, `translate:`, `rows:`, `release:`, `changes:` or `new-vs:` rules. The dry run's structures use `drop:` or none.

**Platforms and places the dry run never tests:**
- **Platforms:** no Shopify, Salla or WooCommerce entry. These are 63 of the 68 other batches: Shopify 27, Salla 33, WooCommerce 3.
- **Route manifests beyond ZD-1's 34 routes outside a store:** Shopify's admin router (SH-4 to SH-10), Salla's dashboard app routes (SA-4 to SA-8) and its Partners portal's (SA-17 to SA-19), and Zid's routes in a store (ZD-2 to ZD-4).
- **Partner portals and developer documentation.**
- **Batches larger than 153 entries:** 50 of the 68 are larger, 30 above 200 and 16 above 300 (ZD-5 390, SA-15 381, SA-8 378, SH-3 373). The dry run's contexts reached 257,452 and 297,153 tokens with no growth of misses (section 2). Nothing is measured above that.

## 7. Effort for the other batches, per kind of entry

**The rule** (`founder-decisions.tsv`, 30 October, "Method (standing)"): `high` at least. A type of task moves to `xhigh` or `max` where `high` or `xhigh` "consistently misses important details", judged "by the quality and completeness of their results". The dry run ran `high` only, and its review ran at `max`. The judgement is a reading, resting on the misses named. A kind is named by what carries an entry's meaning, so that the coordinator can class the other batches' structures by it.

| Kind of entry | Held in the dry run | Judgement | The misses it rests on |
| --- | --- | --- | --- |
| **1. Fields of a row, card or answer:** a table row with its marks, a catalog card's name and line, a grid row, an answer's fields | channel-catalog, contracting-entities, payment-gateways, tax-services (103 lines) | `high` | One care miss of an important detail, a single choice: the Feedonomics fillers on BC-1 14 to 21, which the checker now refuses. The rest is the brief's (R1 40 of 50 rows, R2 64 of 131, each with a fix above) or the evidence's (2, 14, 53), or two choices down a table that change no cell (the term on 44 lines; the misquote on 22, which the quote test now notes). The tax services have none |
| **2. Words that name what the entry is:** a section's or page's description, a plan row's tooltip, a page read through its run text | plan-comparison, settings-list, dashboard-page-index (194 lines) | `xhigh` | 20 care misses of an important detail on 20 lines (10%), in both batches and by four reviewers (R3, R4, R5a, R5b); see below |
| **3. A name and a path only:** a route no run opened | dashboard-route-manifest's 21 routes outside a store | `high`, on a thin sample | One care miss of an important detail (130), two of a column (141, 143). Four `can't tell` (126, 129 twice, 135) and one missing line (133) only evidence settles, which effort doesn't. The sample sets little for the in-store routes |
| **Any kind at `max`** | — | none | The dry run ran nothing at `xhigh`, so nothing shows `xhigh` missing |

**Kind 2's misses:**
- a capability, or `new`, where a cell already holds the place or the thing: BC-1 157, 161, 168;
- a second capability the words name, left without its line: BC-1 112, 141, 148; ZD-1 13, 14, 66, 69, 71, 72, 75, 82, 87, 91, 92, 102, 104;
- a filler the words name: BC-1 99; ZD-1 91, 92.

Six of them change a cell or its slots: 99, 112, 157, 161, 168, and 91 and 92 as one. The checker prints only 157 and 168. The miss is consistent, not a matter of position: ZD-1's agent wrote lines on two capabilities for 4 of its 153 entries, in every third.

**Why kind 2 and not kind 1:**
- In kind 1, `high` made one choice per table, which a test now catches or which changes nothing.
- In kind 2, `high` misses one judgement in ten lines on what a few words name, and no test at `1ac89d6e` catches most of them.
- FX-3 and FX-4, with the unplaced-lead NOTE, will catch some (24 of 36 missing lines have their capability among the leads). `xhigh` is for what they leave.

**What would move kind 2 back to `high`:**
- Place one slice of kind 2 again at `high`, with the fixed brief and checker: ZD-1's entries 59 to 100 (R5a's lines 63 to 103) and BC-1's 101 to 140 at `ff50bbee` (the settings list, R3's lines 124 to 168), 82 entries. Compare its care misses with R5a's and R3's rows.
- If its important care misses fall to kind 1's, kind 2 runs at `high`.
- At the measured 54,000 to 90,000 tokens an entry, that is about 4.4 to 7.4 million tokens. This assumes the per-entry cost of a smaller batch is no higher.

**The other judgements:**
- **The review of any later batch:** `max`, as this one. The founder names "evidence review above all", and this review's findings are the measure the batches are judged by.
- **Size, a reading:** the dry run shows no miss growing with position up to 153 entries and 297,153 tokens of context, and it measures nothing above. 50 of the other 68 batches are larger, and kind 2 at `xhigh` will grow its context faster (an assumption). Keep kind 2's batches within the dry run's size, or read the thirds of the first larger batch's review before running the rest.
- **Cost, facts and one assumption.**
  - **At `high`:** BC-1 cost 7.9 million tokens (about 54,000 an entry), and ZD-1 13.8 million (about 90,000 an entry).
  - **The review at `max`:**
    - R1 to R3 cost 54.4 million on 147 entries, about 6.9 times the batch;
    - R4 to R5b cost about 50 million on 153 entries, about 3.6 times;
    - in all, about 104 million against the batches' 21.7.
  - **`xhigh`'s cost isn't measured.** An assumption: it costs more per entry, mostly through more requests on a growing context, since a batch's cost is its requests times its context.

## 8. The leads

Whether the right capability was among the entry's leads, as `show --candidates` prints them now (after `99d429ad`), not as the agents saw them. The count is per line on a capability: the line's own capability, or the one a `wrong capability` or `should not be new` row names. The `new` lines are left out.

| Structure | Lines on a capability | Right capability among the leads | Missing lines with their capability among the leads |
| --- | --- | --- | --- |
| channel-catalog | 26 | 5 (19%) | — |
| contracting-entities | 10 | 10 (100%), and they carried the homonym (R1) | — |
| payment-gateways | 59 | 32 (54%) | 17 of 18 |
| plan-comparison | 27 | 12 (44%) | 1 of 1 |
| settings-list | 41 | 24 (59%) | 1 of 2 |
| tax-services | 8 | 0 | — |
| **BC-1** | **171** | **83 (49%)** | **19 of 21** |
| dashboard-page-index | 121 | 66 (55%) | 5 of 14 |
| dashboard-route-manifest | 21 | 2 (10%) | 0 of 1 |
| **ZD-1** | **142** | **68 (48%)** | **5 of 15** |
| **All** | **313** | **151 (48%)** | **24 of 36** |

**Where the leads fail, from the parts:**
- **No lead at all:**
  - ZD-1's containers and many pages: 6 lines of R4's, 8 entries of R5a's, 8 of R5b's 20 pages;
  - 30 of the manifest's 34 routes;
  - BC-1's entries 106, 120 and 126.
- **A word of the entry takes the three places:**
  - "payment methods" and "recurring payments" push CM-PAY-011 out on the gateways;
  - "Access" leads to API scopes, "Amazon" to marketplaces;
  - "performance", the plan column's name, leads 10 of 19 plan entries to CM-PLN-001.
- **The parent or a homonym only:** CM-SFR-001 for every Online store page; CM-CNT-003 for the SEO "Store pages".
- **No CM-TAX lead for any tax service.**
- **On BC-1 the leads held 19 of the 21 missing lines' capabilities.** 17 of those 19 misses were the brief's (marks kept as qualities, parents), and 2 were care (112, 141).

## 9. What the batches never placed, and the notes' claims, from the parts

### What the sources state that no entry holds

| Structure | What, and where | Would it change a cell? | Left out by |
| --- | --- | --- | --- |
| channel-catalog | The store the catalog was shown to (Oman, OMR), so the fillers have no market; the Channel Manager's own place; the Storefronts block ("enable multi-geo selling", paid plans); the 19 Learn more links, which carry the maker evidence; "View more storefront platforms" (R1's table, at the catalog's source `002.frame-0.aria.yaml`) | column only (CM-CHN-001, CM-MKS-001, CM-CHN-007) | the build |
| contracting-entities | The preamble's "any of Commerce’s affiliates, subsidiaries, including, but not limited to Feedonomics Holdings, LLC"; the definitions (Extension in full, Ecommerce Platform, Feedonomics Platform, Services, Affiliate); the Contracting Entity clause; the grid's last two rows | **count:** CM-MKT-010@bigcommerce gains `own-service`. **capability:** CM-APP-011's join (M-2). The rows: none (BC-S-0366, BC-S-0285 hold them) | the build (a segment) |
| payment-gateways | The features' definitions with the marks; Paysafe, which sets USA ePay's terms; Accelerated Checkout's PayPal and Stripe; "Settings › Payments"; the funds held by the merchant service provider; fees, APMs, hosted gateways, Level 2 and 3 data, regulated products, notifications and Staff Action Logs, further resources (`001.text.txt`, lines 73 to 219) | **held:** CM-SEL-001@bigcommerce (with the 15 missing lines). **filler:** CM-TRU-010, CM-CHK-008. Readings: CM-PAY-001, CM-PAY-011's Q1 gap. The rest none | the build (tables only) |
| plan-comparison | The billing period ("Annual (Save 25%)", "Monthly", "Billed Annually"); the prices; GST for Australia; Performance by quote; "Current plan: Free Trial" (step 4) | **count:** CM-PLN-002@bigcommerce, none-held, gains `core`. Readings: CM-PLN-001 (prices, an entry since `ccbb3037`), CM-PLN-007 (GST, scope Australia) | the build and the extractor |
| settings-list | Each section's own address (the selection drops it; the agents took it from the source); the "new" marks on Search and MCP | none | the selection |
| tax-services | Empty values; tax class codes; the store's default countries | none (the countries: scope, B-2) | the build |
| dashboard-page-index | The 18 dropped pages' own titles in English and Arabic; the charity store's titles (Donations / التبرعات, Donation opportunities, Donors…); each page's permission, badge, listing condition and `alternativePaths`; Zid Ads' application 2812; Zid Voice's match; the Qitaf store list; what a donation store isn't given (stock notifications, bundle offers, Logistics) | **held:** CM-SEL-007@zid (M-14). The conditions: scope. The rest: column or none | the build (the extractor's pattern drops an empty path, a computed path or key, and a title that isn't literal) |
| dashboard-route-manifest | Each route's module and imports; in the locales, the suspended store's "Your store information will be stored for 2 years." and the access request's duration in hours | none: a lead for CM-TRU-016@zid (not-stated), a quality for CM-STF-005@zid | the tool (the rendering); the selection (`dashboard-locales`, `read: no`) |

**The evidence map's reading of the 18 dropped pages**, "the model loses nothing":
- R4 refutes it for the pages' titles and for the charity store's titles, which would hold CM-SEL-007;
- R5a confirms that refutation for the six in its stretch;
- R5b holds it for placements, but not for the titles, the marketplaces page's permission or its condition.

The evidence map was corrected at `71fda2d8`.

### The notes' claims that fail or hold only in part

| Notes | Claim | Verdict (part) |
| --- | --- | --- |
| BC-1 | Couldn't tell 3: the Feedonomics cards are `extension-point`, "Not `own-service`" | wrong in its outcome: the terms make it of the group (R1) |
| BC-1 | Couldn't tell 6: CM-APP-011 `own-service`; "The terms' definition would settle it" | the definition unsettles it (R1; M-2) |
| BC-1 | Couldn't tell 6: "certain Professional Services" left unplaced | the search stands, the omission doesn't: `new`, `shows` (R1) |
| BC-1 | Items against source: contracting-entities not listed | missed: two rows and the definitions (R1) |
| BC-1 | BigCommerce Payments `core` | refuted: `shows` (R2) |
| BC-1 | Amazon Pay; PayPal's second line | the supports are wrong (`core`); can't tell (R2) |
| BC-1 | payment-gateways "items and source disagree" | partly: they leave things out, seven of which the notes don't list (R2) |
| BC-1 | No difference with the model's cells from payment-gateways | incomplete: CM-SEL-001 none-held; line 62 against BC-S-0148 (R2) |
| BC-1 | `new:File access (WebDAV)` | refuted: CM-CNT-001 (R3) |
| BC-1 | CM-CHN-007's storefronts: "one counts the first storefront" | the difference holds, the explanation fails (R3) |
| BC-1 | Couldn't tell 8, 9 and 13 | a line missing (CM-ORD-001); CM-TRU-001 can't tell; CM-CUS-008, not CM-CHK-009 (R3) |
| BC-1 | Cells gaining a placement | CM-CHK-009 and CM-AIA-004 refuted; leaves out CM-LOY-006, CM-SFR-009, CM-TRU-001, CM-TAX-006, CM-PAY-028 (R3) |
| ZD-1 | Entries 12 and 13 `extension-point` | partly wrong: `shows`, and CM-APP-007's (R4) |
| ZD-1 | The readings that depend on conditions | short: they miss the charity condition's pages (R4), lines 80, 86 and 99 to 103 (R5a), and 111 and 116 to 120 (R5b) |
| ZD-1 | Customer Referrals' parent, CM-MKT-005 | doesn't stand: Zid's own category is "Loyalty and rewards", so CM-LOY-004 (R5a) |
| ZD-1 | 62 and 83 (lines 66 and 87) | a second line each: CM-NTF-002, CM-NTF-001 (R5a) |
| ZD-1 | Store flags in `reading` | ruled otherwise: scope (R4, R5a, R5b; M-11) |
| ZD-1 | Bank accounts contradicts CM-PAY-030's cell | half right: the page is CM-PAY-030's; ZD-C-004 stays on CM-PAY-005 (R5b) |
| ZD-1 | 133, reset-password (line 130) | wrong capability: CM-ACC-001 (R5b) |
| ZD-1 | "No capability holds merchant sign-up as such" | partly wrong: CM-ACC-001 holds SH-S-0017 and SA-S-3534 (R5b) |
| ZD-1 | create-store on CM-ONB-004 | business-type also CM-ACC-004; where-do-you-sell, platform-switch and platform-switch-call can't be told (R5b) |

**The other claims the parts checked stand.** These include:
- R1: the entries' ranges, couldn't tell 4 and 5, CM-ACC-002, CM-MKT-013;
- R2: couldn't tell 1, whose `core` reading was right, the app processors, and the BNPL refusal;
- R3: Display, Share and URL structure, most couldn't-tell items, CM-INV-005 and CM-PAY-001, and items against source;
- R4: Zid Insights, llms.txt, the containers, API integrations, badge `new`, and why 18 pages drop;
- R5a: Customer Referrals as new (its thing, place and searches), 84, the containers, the badges and the rates;
- R5b: the 34 routes, no `own-service`, the access requests, the subscription routes, item 1, Zid Financing's terms, the two-year lead, and the clean run.

### Differences with the model's cells the parts found, for the coordinator

**BigCommerce:**
- CM-CHN-004, CM-MKT-010 and CM-SFR-006 read that no held statement puts Feedonomics or Makeswift in the group. The terms page does: count on CM-MKT-010 (R1).
- CM-APP-011's cell rests its `own-service` on the homonym (R1).
- CM-SEL-001 is none-held, with 15 statements in the marks (R2).
- CM-PAY-001's "no control panel page" reading is refuted by Settings › Payments (R2, R3).
- CM-PAY-011's funds gap is answered by the article (R2).
- CM-PLN-001's prices, CM-PLN-002's billing period and CM-PLN-007's GST are held in the plan page (R3).

**Zid:**
- CM-CHK-009's Zid cell cites the orders and products page as custom fields (R4).
- CM-APP-007 lacks the dashboard's embedded app route (R4).
- CM-LOY-004's homonym note meets Mokafaa and Qitaf, which are both reward and payment (R5a).
- CM-MKT-013's Salla cell holds `marketing/referrals` as an affiliate app's path; observed-sa's routes would settle whether Customer Referrals has a Salla cell (R5a).
- CM-PAY-030's reading should say that the Bank accounts page holds the accounts shown at checkout. CM-PAY-005's note could gain Zid's homonym الحسابات البنكية (R5b).
- CM-STF-005's name, "Third-party access", doesn't fit the platform's own team: a rename for the coordinator, by B-extent's "Names" (R5b).
