# The class's model: what each run taught

**What this file is:** the lessons of each run of Stage 4A, the class's model, about running the agents and planning the work (`PLAN.md`, Stage 4: "Each run's lessons"). Costs are agent tokens, counted by `method/count_tokens.py` over each agent's transcript.

## 1. The brief's inspections (30 October, 23:53 to 00:46 UTC)

- **The inspection** of `briefs/B-extent.md` (19.8 million, 95 requests) found 19 problems, 13 of them must fix. As written, the dry run would have produced wrong rows: a WooCommerce part with no domain to stay within, false "nothing held" cells from coarse concerns, placements with no test, rows no checker could test.
- **The re-inspection** of the rewrite and its two new scripts (21.7 million, 46 requests) resolved 17 of the 19 and found 16 new problems. Seven were checker faults that would have let wrong rows pass a part's own check. The inspector found them by running the scripts on fixtures it built, and on faulty copies of those.
- **Lesson:** an inspector that runs the scripts finds what reading the brief can't. Ask for it in every inspection of a brief that comes with scripts.
- **Lesson:** most new problems came from the fixes, as inspection A found before (`inspection-A.md`, "The coordinator's disposition"). A re-inspection after a large rewrite is worth its cost. A fix the inspector specified exactly can be applied, then tested on the inspector's own fixtures, without a third round.

## 2. The scope part (01:00 to 01:09 UTC)

- **3.8 million, 27 requests,** for all 652 concerns. One agent read compact output (each concern's name, terms, `where` identifiers and Q1 matches) and wrote the file platform by platform.
- **Lesson:** a judgment over many small items costs little when the script prints only what the judgment needs. The scope part recorded an area in nearly every reason, which lets domain C be split by area without another run.

## 3. The review brief's inspection (01:10 to 01:30 UTC)

- **9.1 million, 60 requests:** 15 findings, 10 must fix. Two reached beyond the review:
  - Arabic search: a broken plural isn't a substring, and ة against ه missed matches. The search now reads ة as ه and ى as ي, and the briefs ask for singular and plural.
  - `own-service` on a brand-named product: a brand in a product's name doesn't name its maker.

  Both were sent to the running `B-anchor` by message, and it applied them.

## 4. B-anchor (01:07 to 01:46 UTC)

- **33.9 million, 122 requests,** for 22 concerns (Shopify 11, Salla 11): 25 capabilities, 50 cells, 220 evidence rows; its own check passed with 7 flags for the reviewer.
- **Where the cost went.** The context grew from about 86,000 tokens to 516,000. By quarter of its requests:

  | Quarter | Requests | Tokens | Mean context |
  | --- | --- | --- | --- |
  | 1 | 30 | 2.9 million | 96,000 |
  | 2 | 31 | 6.5 million | 210,000 |
  | 3 | 30 | 9.9 million | 331,000 |
  | 4 | 31 | 14.3 million | 462,000 |

  The last quarter cost five times the first, for the same number of requests.
- **Lesson,** as in S-02 (`studies/subjects/S-02/method-report.md`): a part's cost grows with the square of its length, since every request re-reads the whole context. So a part is cut small enough that its context stays under about 250,000 tokens: one area per part where a domain is large, and a fresh agent that continues from the files when a part runs long. By this part's own first half (9.4 million for 61 requests), two fresh agents doing half each would have cost about 19 million together, not 34.
- **What it read as `shows`:** Shopify's tags and taxonomy shown only through Shopify's own API scopes, where the brief counts the platform's "own API for its own feature" as `core`. This is one of the dry run review's checks.

## 5. B-woocommerce and B-backfill-woocommerce (01:47 to 02:14 UTC)

- **B-woocommerce: 12.8 million, 80 requests,** for 8 concerns and a WooCommerce cell for each of the model's 28 capabilities (3 added). Its context stayed under about 256,000 tokens: the prompt asked it to append rows in small batches and not print files back.
- **B-backfill-woocommerce: 2.0 million, 23 requests,** for six cells, all `none-held` with their searched terms.
- **A checker fault, found by the mapping part.** The ruling test read any capability under a common parent as "together", so `apart` became impossible for a candidate holding a coarse concern such as products. Two rulings were forced to `joined`. The test is now on each ruling's own keys: `joined` where one capability's cells cite keys of both sides, `nested` where a finer part sits under a coarser, `apart` where none does. Four rulings were corrected to what the cells show, and the corrections are noted in each part's notes.
- **Two placement methods.** The anchor read Shopify's API-only evidence as `shows`. WooCommerce's part, told the brief's test (the platform's own API for its own feature is `core`), read WooCommerce's as `core`. The review settles which, and the anchor's cells are corrected to it.
- **Lesson:** most of a mapping part's cost is its cells, one per capability, more than its landings. `class_slice.py candidates` now lists each capability's candidate statements on a platform, from the terms the other platforms' cells use, so a part judges a short list instead of designing every search.

## 6. The dry run's review (02:15 to 02:52 UTC)

Split in two, so each context stays small: the cells (checks 1, 2 and 5) and the structure (checks 3, 4 and 6 to 13), each with its own findings and coverage table.
- **The cells: 62.1 million, 242 requests,** to a context of 455,000 tokens. It checked every cell (84) and every evidence row (297), and searched beyond the domain for 59 cells. It found 7 findings, 3 must fix:
  - the anchor's own-API rows read as `shows` (55 rows, three counts);
  - inventory entries placed without statements, which no search could see;
  - one false `none-held`.
- **The structure: 26.7 million, 107 requests.** 17 findings, 3 must fix: rulings that contradicted the brief, rulings mixing pairs, and a count resting on a partner's permission. It also proposed 12 conventions.
- **Lesson: the review found what the checker couldn't.** Two placement methods, an evidence source no search reached, and readings no test can make. The conventions and the checker's new tests now carry them, so the full run's review can be risk-based: every cell whose kind hinges on one placement, and a seeded sample of the rest.
- **Lesson: a review that reads every row is the most expensive part of all.** The cells review cost almost twice the anchor it reviewed. Its cost came from its length, as the anchor's did.

## 7. What the dry run says about the full run's cost

**Measured on domain B** (three of five platforms; 22 Shopify and Salla concerns, 8 WooCommerce, 28 capabilities):
- the parts cost 48.7 million: the anchor 33.9, the mapping 12.8 and the back-fill 2.0;
- the reviews cost 88.8 million;
- the inspections, the scope part and the review brief's inspection before them cost 54.4 million.

**What remains:**
- the anchor: 328 Shopify and Salla concerns in domains A and C to G;
- the mapping: 294 concerns of WooCommerce, Zid and BigCommerce;
- a cell for every capability and mapped platform: about 1,500 more for the mapping parts. That assumes about 500 capabilities: a little over one per anchor concern, as in domain B, plus those the mapping adds.

At the dry run's own rates (1.5 million per anchor concern, 0.46 million per mapping cell), that is about 500 million for the anchors and 650 to 700 million for the mapping, before the back-fills, the final review and Q3's check.

**Re-planned to read the same evidence at less cost:**
- **Parts small enough that no context passes about 200,000 tokens:** one area per anchor part (domain C's six areas, A's five, and so on). Where a part runs long, a fresh agent continues from its files. By the anchor's own first half, this alone cuts a part's cost by close to half.
- **The candidates script:** a mapping or back-fill part judges a short list of candidate statements per capability, instead of designing every search.
- **The conventions and the checker's new tests,** so fewer readings need re-doing.
- **A risk-based final review,** not every row: every cell whose kind hinges on one placement, every join on role and every `none-held`, then a seeded sample.

**The projection, an assumption to be measured after the first domains:**

| Item | Million tokens |
| --- | --- |
| Spent to the dry run's corrections | about 200 |
| Anchors | 200 to 300 |
| Mapping | 200 to 350 |
| Back-fills | 20 to 40 |
| Final review | 40 to 80 |
| Q3's check | 15 to 30 |
| The architecture plan's review | about 10 |
| **The extent, in all** | **about 700 to 1,000** |

That is about three to four times the budget of 250 million. By `PLAN.md`, section 8, and the founder's standing decision of 27 October, the work goes on, re-planned to cost less and never cut short of the evidence. The projection is re-measured after the first two domains.

## 8. After the dry run: B-zid (03:25 to 03:34 UTC)

- **6.0 million, 48 requests,** for Zid's 4 domain-B concerns and a Zid cell for each of the model's 33 capabilities (4 added): about 0.18 million per cell, against WooCommerce's 0.46 in the dry run. The candidates script gave it each capability's leads, the conventions removed the dry run's open questions, and it ran at `high` effort.
- **Lesson:** most of Zid's domain-B evidence is names in its inventory, with no statement describing them, so many of its cells cite inventory entries by id. Three of its four new capabilities rest on such names alone (a plan line, an API group). The convention admits them as capabilities. The final review checks whether each should fold into its parent.

## 9. B-backfill-zid, B-bigcommerce and G-anchor (03:25 to 04:00 UTC)

- **B-backfill-zid: 5.0 million,** twelve cells. **B-bigcommerce: 4.1 million,** six concerns and 33 cells, about 0.12 million per cell; it added no capability, so it needs no back-fill. Domain B is complete for all five platforms, and merges with no problem.
- **G-anchor: 18.0 million, 96 requests,** for Salla's four concerns (Shopify has none in G): 7 capabilities. A cross-cutting domain's concerns are thin, so the part searched across the whole concern map for every capability, at `max` effort. That is 4.5 million per concern, against B's 1.5.
- **A method ruling, for the founder's veto:** anchors now run at `high` effort, as the mapping parts already do. The conventions are settled, and the checker carries the dry run's tests. The final review's sample is where a gap in a part's reading shows (the effort rule of 13 October: "a part whose check or review shows gaps is re-run").
- **Spent:** 247.0 million of the extent's 250 million.

## 10. A quarter past the budget (30 October, about 04:55 UTC)

The extent passed 312.5 million, a quarter past its budget of 250 million, at 316.9 million. By `PLAN.md`, section 8, the cost comes to the founder with a new projection, and the work goes on.

**Where it stands:**
- Domains B and G are complete for all five platforms: 33 and 13 capabilities.
- Domain F's anchor is complete: 41 capabilities from 41 concerns, in four batches.
- Domain D's anchor is three batches of six in: 35 capabilities.

**The rates measured since the dry run, at `high` effort:**
- **Anchors:** F's batches 2 to 4 cost 23.7 million for 29 concerns, and D's batches 1 to 3 cost 19.0 million for 29: about 0.75 million per concern, against the dry run's 1.5.
- **Mapping cells:** B-zid 0.18 million per cell, B-bigcommerce 0.12, G-woocommerce 0.27, G-zid 0.15, G-bigcommerce 0.14: about 0.18.
- **Back-fill cells:** about 0.35 million each.

**The projection, re-measured** (an assumption, to be measured again after domain E):

| Item | Million tokens |
| --- | --- |
| Spent | 317 |
| Anchors still to run: 254 concerns of D, E, A and C | about 190 |
| Mapping: about 1,140 cells in D, E, A, C and F | about 205 |
| Back-fills: about 170 cells | about 60 |
| Final review, by risk | about 60 |
| Corrections after it | about 30 |
| Q3's check | about 20 |
| The architecture plan's review | about 10 |
| **The extent, in all** | **about 890, within 750 to 1,000** |

That is inside the projection of 30 October's milestone (700 million to a billion), and about three and a half times the budget. No higher plan has been needed so far: the usage limit hasn't stopped an agent.

## 11. Domain D's mapping, and one statement under two concerns (30 October, 05:18 to 05:45 UTC)

- **D-woocommerce: 9.6 million** in two batches (5.6 and 4.0), for 16 concerns and 64 cells: about 0.15 million per cell. One capability added, abandoned cart and order recovery, from a Marketplace category.
- **The concern map holds one statement under several concerns,** each time with its own key and the same statement id: 548 of Shopify's statement ids, 124 of Salla's, 145 of WooCommerce's. The checker tests a citation by its key, so it could not see one statement cited under two concerns' keys:
  - twice as `core`, in two domains;
  - or under one concern's key in a tree where another concern holding it has landed.

  The merge now finds both by statement id. Of 25 statements counted in two domains, three were the sole support of a cell. One showed a duplicate capability across domains: E's first storefront batch had put hosting with SSL, while G already held hosting of the store. Each was corrected so that it counts once, `core` where the capability names it. The other 22 change no count and go to the final review, with 26 landings whose shared statement is cited in another tree.
- **An agent launched without its effort setting** inherited the coordinating session's `max`. It was stopped after 3.2 million, before it had written a row, and relaunched at `high`, as the anchors run (section 9).
- **Lesson:** a test that reads a key is blind to what the key's statement is shared with. Where a source reuses one statement under several concerns, test by the statement's id as well.

## 12. One thing, one domain (30 October, about 07:00 UTC)

- **A capability made twice, in two domains.** A-anchor's first batch made a capability for the merchant's mobile app for managing the store, which domain G already held, with a cell for every platform, on the same Salla plan line. Each anchor reads its own domain's model, so nothing showed it the other. The merge would have flagged the plan line as counted in two domains, but only after the part had built cells on it.
- **What changed:** `class_slice.py caps` searches every domain's capabilities, their notes and their cells' terms. The extent's brief now asks an anchor to search with it before adding a capability, and to leave a thing another domain holds to that domain. The coordinator removed the copy.
- **Lesson:** a part that can see only its own domain can duplicate another's. A cheap search at the point of adding costs less than a correction after the cells are built.

## 13. Domain E complete, and the projection re-measured (30 October, about 08:00 UTC)

**Where it stands:** domains B, D, E, F and G are complete for all five platforms and merge with no problem: 206 capabilities, 1,030 cells, 3,599 evidence rows. Domain A's anchor is in its last batch (38 concerns landed, 42 capabilities); domain C's anchor has begun, in twelve batches.

**The rates measured since section 10, at `high` effort:**
- **Anchors:** E's seven batches cost 30.5 million for 52 concerns (0.59 a concern), A's first six 37.1 million for 48 (0.77): about 0.7 million a concern, as section 10 found.
- **Mapping cells:** D's three platforms 33.6 million for 198 cells (0.17), E's 29.1 million for 124 (0.23): about 0.2 million a cell.
- **Back-fills:** about 0.3 million a cell where there are twenty or more, and about 2 million for a part of two or three cells, which pays its fixed cost of reading the brief.
- **The coordinator's corrections** between batches cost no agent tokens. They caught a duplicate capability, eight statements counted in two domains, and some thirty fits and readings that later batches made stale.

**The projection, re-measured** (an assumption, measured again after domain C's anchor):

| Item | Million tokens |
| --- | --- |
| Spent | 509 |
| A's last anchor batch | about 5 |
| A's mapping, about 130 cells, with its back-fills | about 35 |
| C's anchor, 118 concerns | about 85 |
| C's mapping, about 360 cells, with its back-fills | about 90 |
| Q3's check, with its brief's inspection | about 35 |
| Final review, by risk, and its corrections | about 90 |
| The architecture plan's review | about 10 |
| **The extent, in all** | **about 860, within 750 to 1,000** |

That is a little under section 10's 890, and about three and a half times the budget. No higher plan has been needed: the usage limit hasn't stopped an agent.

## 14. The inspection of Q3's check and the final review (30 October, 09:20 to 09:40 UTC)

- **10.0 million.** The inspector ran both briefs' scripts on the merged model and on fixtures it built, and found 11 must-fix faults (`inspection-Q3R.md`):
  - **Q3's check:** covered had no grain; a held miss couldn't be told from a covered row; partly didn't say what its rest was; the time rules for the founder's decisions and for subjects contradicted the founder's decisions and the architecture plan; `wrong time` came from the model's own timing; `bundles` had drifted from Q3 as agreed;
  - **the review:** Q3's check wasn't reviewed; the selection left out most cells where an error changes a count; "counted twice" and "ruled differently" asked for one answer where the conventions give two.
- **What changed:** both briefs and both scripts were rewritten to the inspector's fixes, which were exact. `q3.py` gains `where` (which cells cite a statement, by its id), a `rest` column, one file per batch, and a check that computes `bundles` and `wrong time` and refuses a held miss on a key already cited. `review_select.py` groups the items by cell, adds the count-changing cells, the strained landings, the parts' leads, Q3's rows and every coordinator row and note, samples every part, splits each share into batches of 30, and checks the reviewers' coverage. Tested on the inspector's cases.
- **The review's size:** 862 items before domain C is merged, about 1,100 after. At the mapping's rates it may cost about 150 to 200 million, against section 13's 90 for the review and its corrections; it is re-projected after its first batch. That would put the extent near the top of its range, about a billion. By the standing decision of 27 October, the budget never costs evidence; the figure goes to the founder with the next report.
- **Lesson:** a brief the coordinator writes alone, without a run on real data, carries the coordinator's blind spots. An inspector who runs the scripts finds them, as in section 1.


## 15. Domain C, the merge of every domain, and the subjects' points brief (30 October, 09:20 to 12:45 UTC)

- **Domain C is complete for all five platforms, in 27 parts and batches, 177.0 million.** The anchor ran in 12 batches: 89 capabilities, CHK 9, ORD 14, PAY 32, TAX 9, SHP 22, RET 3. WooCommerce ran in 5 and added order withdrawal requests (CM-RET-004); Zid in 4, adding order payment status (CM-ORD-015); BigCommerce in 3, adding the shipping rules engine (CM-SHP-023). A back-fill followed each, as the brief requires. C holds 93 capabilities: 89 `class`, and 4 `slot` (checkout UI extensions, cart and checkout validation, cart transform, and the fulfilment network offered in the admin).
- **The merge of every domain** (`9d204b46`): 347 capabilities, every one of the 652 concerns landed once, 1,735 cells (each capability on all five platforms), 7,427 evidence rows and 397 rulings, with no problem. Across the model: 328 `class`, 16 `slot`, 3 `open: unplaced`. A class's count runs from one platform (83 capabilities) to all five (44). The merge leaves 175 flags for the final review: 87 `strained?`, 55 counted twice, 15 `one capability?` and 18 pairs ruled differently by two domains. The coordinator read the five counted twice where a cell rests on the statement alone. Each names several things or is a provider's statement, so each counts in each capability by the rules already set.
- **The coordinator's rules applied in C, each a reading listed for the founder's veto:**
  - **A statement that names several things counts in each:** a section titled for two subjects, a fee on a label, a scope pair, a list. A landing that holds one stays clean.
  - **A Q1 match whose other side lands in a later part is written by that part.** The earlier side stays `single`, since a part's checker sees only its own landings.
  - **A concern whose thing another domain holds is moved there,** by "One thing, one domain". WooCommerce's address autocomplete and Zid Voice went to D, and Zid's wallet deduction from Zid Pay to A.
  - **A plan line is a place of its own,** so BigCommerce's Persistent cart became a capability under the cart, as the dry run's test says.
  - **Maker evidence decided the services' placements:** Zid Pay is Zid's own service, on its terms, "العقد المبرم بين مستخدمي زد باي وشركة زد"; BigCommerce Payments is `core`, since no statement names BigCommerce's company as its maker; WooCommerce Shipping is Automattic's, on its terms.
- **The subjects' points brief** (`briefs/P-points.md`, `method/land_points.py`) was inspected twice, at 45.8 million (`inspection-P.md`). The first inspection found 8 must-fix findings and 12 optional ones; the re-inspection resolved 18 of them and found 5 must-fix and 11 optional new ones. All were taken.
  - **The routing:** the drafter records each conflict and the register rows it bears on, and the coordinator settles the fact first. Only a conflict that questions the evidence under the founder's own decision goes to the founder, with options and a recommendation.
  - **The conflicts:** `count` and `placement` follow the model's own rules and don't overlap; a cell that already places the third party is no conflict.
  - **The leads:** a page that is a corpus gives none, and the subjects' copies of help pages trace as the concern map cites them.
  - **The outcomes**, `kept open` among them, are checked against the rows their conflict names.
  - **The batches:** eight, each small enough to read whole.
- **Lesson:** the first inspection's own wording brought one new fault, N2: a `placement` conflict on cells that already place the third party. An inspector's fix is a proposal, read again like the rest.
- **Cost:** 789.7 million agent tokens by 12:45 UTC. The coordinating session's own tokens since 09:20: about 117 million. The projection to the end of the extent:
  - the subjects' points, about 50;
  - Q3's check, about 60;
  - the final review, 150 to 200;
  - its corrections, about 30;
  - the architecture plan's review, about 10.

  That is about 1.1 billion for the whole extent, within 1.05 to 1.2, and above section 14's "near a billion". By the standing decision of 27 October the budget never costs evidence, and the figure goes to the founder on the orientation page.

## 16. The subjects' points on the model (30 October, 12:15 to 14:00 UTC)

- **All 98 points are placed** (`studies/class-model/points/P-1.tsv` to `P-8.tsv`, at `fe0503ed`): S-01's 23 in two batches, S-02's 75 in six. 61 landed with no conflict, and 37 carry 50 conflicts: S-01's 8 points 11 of them, S-02's 29 points 39. `land_points.py check --final` passes on all eight batches.
- **The coordinator settled each conflict's fact first,** then wrote its outcome: 43 model amendments (S-01 11, S-02 32), 4 dismissed and 3 kept open, with what would settle each. None needed the founder: no conflict questioned the evidence under a founder's decision. Decision 1's rows rest on statements the amendments only added to.
- **The model now cites the subjects' own statements,** by their ids, in these amendments only (`B-extent.md`, "Conventions"; `briefs/P-points.md`, "After the batches"). The checker, the merge and the page generator resolve them. In almost every conflict, the subject held what Q1's concern map didn't:
  - observed runs (Salla's onboarding refusing other countries, Zid's plan checkout charging VAT);
  - the WooCommerce release's code (its own onboarding, email locale and address formats);
  - help pages Q1 never placed (Tabby and Tamara, BigCommerce's offline methods and its Multi-Storefront).
- **What moved:** 21 capabilities changed kind or count. One `open` became a class: CM-ACC-008, the countries a platform serves, now in Salla's core on its onboarding. Twenty counts rose, among them markets, store languages, staff roles and notifications, platform billing and the tax on it, customer addresses and their autocompletion, reserves, local and manual payment methods, and returns. The merge stays clean: 347 capabilities, 7,538 evidence rows, no problem.
- **What stays open:**
  - whether Zid or the Saudi Business Center makes the business check (twice);
  - whether maintenance mode and visibility before launch are one capability, which goes to the final review's `one capability?` question.
- **Lessons:**
  - **The coordinator's first amendment ran while two S-02 drafters were reading the model.** Both stopped on the brief's warning and resumed from their drafts. From then on, amendments ran only between drafting rounds.
  - **The concern map understated counts wherever the evidence sat outside the pages Q1 placed:** runs, released code, and help articles. A final review that samples cells should expect more of the same.
  - **A commit message slipped:** `fe0503ed`'s says 38 conflicts, 30 amendments and 4 kept open for S-02; the counts above are the files'.
- **Cost:** 129.5 million, measured by `method/count_tokens.py`: the brief's two inspections 45.8 and the eight drafting batches, with their resumptions, 83.7. The coordinator's settlement ran in this session.

## 17. The held pass, from the gap to its third brief (30 October, about 14:50 to 21:00 UTC)

- **The gap.** Q3's check led to a measure of what the evidence repositories hold against what the model read (`held-vs-read.md`). The model had read the concern map, finished on 12 October, and nothing captured after it. Shopify, for one, holds 31,269 readable addresses, of which the model cites 176. The extent's plan never checked the model against what the repositories hold today: the coordinator's miss. The held pass reads every entry of the platforms' self-descriptions the model never read, guides and indexes first (the founder, 30 October), and places each on the model (`PLAN.md`, Stage 4A, at `9e59d2ef`).
- **Its inspection** (`inspection-H.md`: 16 must fix, 21 should fix, 9 notes), all taken. It estimated the pass at 100 to 310 million tokens, an assumption: one request per 8 entries, about 170 tokens of context per entry, and a start of about 60,000.
- **The dry run,** at `high`, measured it (`held/review-H.md`, section 7):
  - BC-1, 147 entries: 7.9 million, about 54,000 an entry, its context growing from 49,347 to 257,452 tokens over 51 requests;
  - ZD-1, 153 entries: 13.8 million, about 90,000 an entry, from 49,373 to 297,153 over 76.

  That is one request per 2 to 3 entries, and about 1,400 tokens of context per entry: each about eight times the estimate's assumption. A batch's cost is its requests times the context each reads again, so the two multiply.
- **Its review,** at `max`, in six parts and a join, by agents that made neither batch, on a brief inspected first (`inspection-HR.md`, 25.4 million): 119.7 million. In 458 rows on 318 lines, 186 lines stood whole. The misses were 55% the brief's, 40% care and 5% the evidence, and 92 rows were important details. The coordinator ruled on 14 cases the model's rules left open (`held/review-H-rulings.md`, M-1 to M-14, each for the founder's veto) and corrected both batches.
- **The rewritten brief's inspection** (`inspection-H2.md`: 8 must fix, 15 should fix, 12 notes): 50.2 million.
- **The calibration** (`held/calibration.md`): 82 entries placed again under the rewritten brief, at `high` and at `xhigh`, for 47.0 million. `xhigh` cost 1.6 and 2.4 times as much and missed the same important details, or others like them. Each was a capability whose cell held nothing and that no lead showed.
- **The third brief** (`briefs/H-held.md` at `71d4f013`) takes the second inspection whole. Its leads also come from capabilities' own names, print in a stable order, and read an Arabic word without its article, joined conjunction or feminine plural. Its lookups always run, and M-6 is narrowed to a child that is a kind of its parent's thing.
- **BigCommerce is in the model** (`0814b925`): 193 evidence rows for 76 cells, 14 cells that held nothing now held, 15 changed in placement, and four capabilities new from held entries.
- **Lessons:**
  - **Measure a batch before projecting a pass, and multiply the two rates.** The estimate assumed each factor of the cost about eight times too low, and they multiply. The dry run was planned to measure them, and did.
  - **A review at `max` costs about five times the batches it reviews** (104 million against 21.7). It was worth it once, to find the brief's faults: more than half the misses were the brief's. After it, the checker and a calibration on a sample take its place.
  - **More effort didn't buy the missed details.** Both levels missed the same capabilities whose cells held nothing, because no lead or search reached them. The fixes are in the tool (leads by name) and the brief (lookups that always run), not in effort.
  - **An agent reads what a tool prints, in the order it prints it.** The leads printed in Python's set order, so the checker's first-lead note came and went between runs. Everything a script shows an agent is sorted now.
  - **A rule needs its own case named.** "The parent's thing where the entry's own words name it" was read as every section's group, BigCommerce's General, and gave lines that change no cell. M-6 now names its case: a child that is a kind of the parent's thing.
- **Cost of this section's agents,** measured by `method/count_tokens.py`: 242.3 million (the review's inspection 25.4, the review 119.7, the second inspection 50.2, the calibration 47.0), after the dry run's 21.7. The coordinator's work ran in this session.

## 18. The held pass's first batches, and the projection measured (30 October, 20:45 to 21:40 UTC)

**The first batches under H-held.md's third version,** at `high`, each checked by the coordinator before the next pair ran:

| Batch | Kind | Entries | Tokens | Per entry | Cells it would change, beyond earlier batches | New things |
| --- | --- | --- | --- | --- | --- | --- |
| ZD-4 | Zid's routes | 195 | 7.5 million | about 38,000 | 5, 4 of them from holding nothing | 1 |
| WC-1 | WooCommerce's free extensions, by country | 75 | 5.7 million | about 76,000 | 7, 1 from holding nothing | 3 |
| WC-2 | the same, for SA, OM, YE and the item labelled EG | 76 | 4.2 million | about 55,000 | none beyond WC-1: each country's scope | none beyond WC-1's |
| ZD-5 | Zid's routes, more of their pages opened and read | 194 | 14.4 million | about 74,000 | 3 more from holding nothing | 2 |

**What each check found,** each fixed before the next pair:
- the routes had no leads at all, since a change to what the leads read had dropped a route's path; with its segments read again, 176 of ZD-4's 195 entries have leads;
- the checker's quote test didn't reach the files a reading cites (the release, the dashboard's locales, a statement);
- two calls on WC-1 that the coordinator corrected: Jetpack's 'Keep your store online' is no reliability line, and ShipStation's labels and fulfilment are `extension-point`, a third party's feature through WooCommerce's own extension (M-8);
- two of ZD-4's readings, settled by the dashboard's locale strings;
- WC-2's own find, confirmed in the run's answers: the structure's item labelled EG is the YE store's list again, since the request to set the country to EG was refused, so Egypt's list isn't held (`evidence-map.md`).

**Where the tokens go.** A batch's cost is its requests times the context each request reads again. Every agent starts at about 49,000 tokens, the harness's own, and its reading of the brief, the rules, the guides and the previous batch adds 60,000 to 100,000 before it places an entry. ZD-4 made one request per four entries, WC-1 one per two and ZD-5 one per 2.4, with a mean context of about 150,000, 135,000 and 175,000. That start is a fixed cost per batch, so a long batch of a light kind costs least per entry, and the kind of list matters far more than the effort. Zid's routes cost 38,000 an entry where their pages were seldom opened (ZD-4) and 74,000 where many were (ZD-5); WooCommerce's cards 55,000 to 76,000; the calibration's pages with descriptions 190,000.

**The projection, re-measured** (an assumption for the kinds not run yet; each kind is measured on its first batch, and the projection again with it):

| Item | Million tokens |
| --- | --- |
| Spent, by about 21:30 UTC: 1,187 at 19:25, measured then, and 129 since (the second inspection 50.2, the calibration 47.0, the four batches 31.8) | about 1,320 |
| The held pass's other batches, 15,245 entries, at the kind's rate: routes and navigation 4,976 at 38,000 to 74,000 an entry; help, changelog and editions 2,715 at 40,000 to 80,000; plans, policies and gates 2,547 at 50,000 to 80,000; settings 2,478 at 55,000 to 80,000; catalogs of providers and extensions 817 at 55,000 to 76,000; permissions and scopes 656 and developer surfaces 377 at 30,000 to 50,000; the other 679 at 40,000 to 60,000 | 650 to 1,150 |
| Its second stage: the cells still holding nothing, read against the held pages, with Q3's 13 candidate misses | 100 to 200 |
| The omission review | about 50 |
| The final review, by risk, and its corrections | 180 to 230 |
| The architecture plan's review | about 10 |
| **The extent, in all** | **about 2.3 to 3.0 billion** |

That is more than twice section 15's 1.1 billion, which didn't hold the held pass, and above the 1.8 to 2.4 billion the coordinator told the founder at 19:25, which had put the re-planned held pass at 250 to 500 million: the batches under the rewritten brief cost more per entry than that assumed. The plan had put the held pass and the omission review at 80 to 180 million, an assumption to be measured on the first batches (`PLAN.md`, section 11, 30 October): measured, they are about ten times that. By the founder's standing decision of 27 October the budget never costs evidence, and the figure goes to the founder.

**Re-planned to read the same evidence at less cost:**
- each batch is checked by the checker and the coordinator, not by a review at `max`, which cost five times the batches it read (section 17);
- each batch follows the one before it on its structure, so a run of the same kind costs less: WC-2 followed WC-1's lines at 55,000 an entry against WC-1's 76,000;
- effort stays `high`, as calibrated: `xhigh` cost 1.6 to 2.4 times as much and missed the same details;
- version 3.1's cuts: a compact view of a lead's cell, no reading of the scripts' code, and leads for routes, so fewer searches;
- the batches not yet run are cut again at about 100 entries, at most 130 (Salla's 63 run from 80 to 130): an entry's reading stays in the context every later request reads, so a batch's cost grows faster than its length, most where it reads pages, while each batch's start is a fixed cost;
- the platforms where cells hold nothing most often run first: Zid, WooCommerce, Salla, then Shopify after the founder's pushes.

**The yield so far:** about one cell changed per million tokens, from none (WC-2, the same cards as WC-1 in other countries) and 0.2 (ZD-5) to 2.5 (BC-1), besides the new things and each country's scope. It will fall as cells fill, and the second stage and the omission review then read less.

**A higher plan:** none needed so far; the usage limit hasn't stopped an agent. Two agents at once run about 70 million tokens an hour, so the held pass takes about 9 to 16 hours of running. More at once would shorten that, not cost less; two stay, since each check so far found something the next batch needed.

**Lessons:**
- **The kind of list sets the cost, not the effort.** Light lists cost a fifth of pages with descriptions, at the same effort.
- **A change to what the leads read is tested on each kind before it runs.** Leaving field names out of the term leads was right for settings and wrong for routes, whose path is their only words.
- **Check every batch before the next.** Each of the first checks found something the next batch would have repeated.

**Re-measured at about 22:00 UTC,** after five more batches, each the first of its kind:

| Batch | Kind | Entries | Tokens | Per entry |
| --- | --- | --- | --- | --- |
| WC-3 | settings: WooCommerce's options, read with the release's titles | 195 | 18.4 million | about 94,000 |
| ZD-6 | plans: Zid's offered plans, with the last routes | 87 | 7.8 million | about 90,000 |
| ZD-7 | flags and permissions | 130 | 7.3 million | about 56,000 |
| WC-4 | payment providers, read with the release's code, and the last options | 80 | 14.4 million | about 180,000 |
| ZD-8 | permissions | 130 | 6.5 million | about 50,000 |

Plans and settings cost more than assumed, permissions less. The 14,747 entries left come to about 710 million to 1.2 billion at the measured rates, about 1,374 million is spent, and the extent comes to **about 2.4 to 3.1 billion**. A list of permissions changes almost no cell beyond its pages' (ZD-8: none), while plans and settings change the most per batch.

**Re-measured at about 23:45 UTC** (`method/count_tokens.py --since 2026-10-30T22:00`, over this session's transcript and its agents'). Since 22:00, 316.7 million tokens: the agents 231.7 million and the coordinator's own checks 85.0 million, over 202 requests that each read again a context of about 420,000 tokens. 1,901 entries were placed: Zid's last five batches, WooCommerce's last four, and Salla's SA-1 to SA-3 and SA-5 to SA-10 and SA-32. Zid, WooCommerce and BigCommerce are all placed. 12,846 entries are left: Salla's 5,232 and Shopify's 7,614.

| Batch | Kind | Entries | Tokens | Per entry | Cells changed beyond earlier batches |
| --- | --- | --- | --- | --- | --- |
| SA-2 | the App Store's routes, the changelog, the plans page | 130 | 17.5 million | about 135,000 | 1 (`shows` only) |
| SA-5 | the Special plan's page | 130 | 13.8 million | about 106,000 | 1 (`shows` only) |
| SA-8 | dashboard routes | 104 | 15.5 million | about 149,000 | 1 (`shows` only) |
| SA-9 | dashboard routes | 94 | 12.2 million | about 130,000 | none |
| SA-10 | dashboard routes | 82 | 12.8 million | about 156,000 | none |
| SA-32 | plan gates | 130 | 16.5 million | about 127,000 | none, and 3 new things |
| SA-3 | the plans page | 130 | 8.5 million | about 65,000 | none |
| SA-6 | the Special plan's page, in English | 112 | 5.0 million | about 45,000 | none |
| ZD-13 | plan policies | 142 | 12.5 million | about 88,000 | none beyond earlier batches, and 2 new things |

**What it changes.** Salla's lists cost 45,000 to 156,000 an entry, more than the kinds' assumed rates. After SA-1 they change almost no cell, since the concern map read most of what Salla's pages say. Their yield is their corrections and new things: three rulings, the plans pages' market differences, and five new things. The coordinator's checks were not projected forward before. At this context they cost about a third of the agents' tokens.

| Item | Million tokens |
| --- | --- |
| Spent, by about 23:45 UTC: 1,374 at 22:00 and 317 since | about 1,690 |
| The held pass's other 12,846 entries, at the measured rates: Salla's 5,232 at 100,000 to 140,000 an entry; Shopify's 7,614 at 70,000 to 130,000 | 1,060 to 1,730 |
| The coordinator's checks of those batches: 15 to 35 percent of the agents' tokens, lower once its context is compacted | 200 to 600 |
| The second stage, the omission review, the final review and its corrections, the architecture plan's review (as above) | 340 to 490 |
| **The extent, in all** | **about 3.3 to 4.5 billion** |

**Re-planned to cost less:**
- the coordinator checks with fewer requests and filtered output;
- each route batch reads an app's bundle once, for all its routes and gates (from SA-11);
- Shopify's batches are cut again by kind after the founder's pushes, and each kind is measured on its first batch.

No higher plan is needed so far: no agent has been stopped by the usage limit.

**Re-measured at about 02:45 UTC on 31 October**, after Shopify's new evidence was selected. The counts are from `method/count_tokens.py --since 2026-10-30T23:45`, over this session's transcript and its agents'.
- **Spent since 23:45:** 669 million tokens, about 3 hours' work. The agents spent 522 million, the selection agent's 33.5 million among them. The coordinator's own work was 147 million over 326 requests.
- **Measured rate:** 68 held-pass batches have run, holding 7,470 entries, at 111,000 tokens an entry on average. Salla's 48 batches ran at 131,000 an entry.
- **What costs most:** batches whose entries repeat addresses earlier batches placed. SA-19 cost 203,000 an entry and SA-42 195,000. Most of their requests looked those earlier lines up, and their contexts reached 365,000 and 470,000 tokens.

**Shopify's selection**, decided by the coordinator on the selection agent's tested proposal:
- **Editions:** read from each page's own data, 1,608 features. The rendered text held 2 of summer 2023's 143. Fall 2026 is read from its rendered page.
- **Merchant changelog:** every post since 2018, 1,646 of them.
- **Pricing:** the pages of the 18 English-language sites and the 3 Arabic ones, 1,056 entries. All 61 sites would have given 8,230.
  - The other 40 sites state the same lines in their own languages. Every POS page has the same lists, lengths and identifiers, 83 of 84 international pages have one shape, and every plan feature a site names, an English or Arabic site names too.
  - Their prices are held for a subject to read as a table (`evidence-map.md`). Which comparison rows each of them lists isn't matched, a gap for the second stage.
- **Versions:** the CLI and the extension targets in their latest words.
- **The build:** the selection agent's nine new rules were reviewed and taken. The coordinator added `long:` for prose a platform publishes whole, a post or a dialog. Over-long entries are accepted under it.
- **Kept as they are:**
  - Editions' section descriptions are not entries. Each feature names its section.
  - A nested entry's doubled parent name ('Basic > Basic') is left as it is, a fault of the build. The fix would change the ids of 222 placed entries.
- **Size:** Shopify holds 10,286 entries (7,749 before), cut into 103 batches. A structure of 300 entries or more has batches of its own (`batches --alone 300`), so 22 can start at once and none waits on another structure's.

| Item | Million tokens |
| --- | --- |
| Spent, by about 02:45 UTC: about 1,690 at 23:45 and 669 since | about 2,360 |
| The held pass's other 11,110 entries (Shopify's 10,286; Salla's 824 after SA-48, its settings centre rebuilt from 1,298 entries to 715), at 90,000 to 140,000 an entry | 1,000 to 1,560 |
| The coordinator's checks of those batches: 20 to 30 percent of the agents' tokens (28 percent since 23:45) | 210 to 490 |
| The amendments and new things, the second stage, the omission review, the final review and its corrections, the architecture plan's review | 390 to 590 |
| **The extent, in all** | **about 4.0 to 5.0 billion** |

**Re-planned to cost less:**
- **The settings centre rebuilt:** each entry carries what its section's answer states beside it, and a setting held in each store's answer is one entry. That is 583 fewer entries, and none of them needs its section's body read. SA-48 cost 455,000 an entry reading those bodies.
- **Pricing on 21 sites, not 61:** about 7,200 entries are not read, the same lines in other languages, about 650 million to 1 billion tokens.
- **One lookup of earlier lines:** `held_entries.py earlier` prints, for a chunk of entries, the lines earlier batches gave the same address, route or label, in one call. SA-19 and SA-42 spent most of their requests on these lookups.
- **A large structure's batches side by side:** once its first batch is checked, its other batches run in parallel, each keeping to the first batch's rules, and the coordinator aligns them at its checks. This saves hours, not tokens.

No agent has been stopped by the usage limit.

**Re-measured at about 04:05 UTC, by structure** (`method/count_tokens.py --since 2026-10-31T02:45`, and each checked batch's transcript).
- **Spent since 02:45:** 282 million tokens: the coordinator 53 million over 113 requests, the agents the rest.
- **Each large structure's first batches cost more than the projection's 90,000 to 140,000 an entry.** A structure's first batch writes the rules its later batches keep to, and its entries hold more:

| Structure | Entries left | Checked batches | Tokens an entry |
| --- | --- | --- | --- |
| Shopify `merchant-changelog` | 1,516 | SH-34 | about 219,000 |
| Shopify `editions-page-data` | 1,478 | SH-50 | about 250,000 |
| Shopify `admin-router` | 844 | SH-8, SH-9 | about 176,000 |
| Salla `settings-center` | 470 | SA-48 to SA-50 | 455,000, 526,000, then 248,000 with the narrowed prompt |
| Shopify's other 6,320 entries (pricing, permissions, plans, the mobile app, help notes and the rest) | 6,320 | none yet | not measured |

| Item | Million tokens |
| --- | --- |
| Spent, by about 04:05 UTC: about 2,360 at 02:45 and 282 since | about 2,640 |
| The measured structures' 4,308 entries, at their rates, the settings centre at about 230,000 | 850 to 1,060 |
| The other 6,320 entries, at 120,000 to 200,000 | 760 to 1,260 |
| The coordinator's checks, about a fifth of the agents' (19 percent since 02:45) | 330 to 460 |
| The amendments and new things, the second stage, the omission review, the final review and its corrections, the architecture plan's review | 390 to 590 |
| **The extent, in all** | **about 5.0 to 6.0 billion** |

**Re-planned to cost less, since 02:45:**
- **Every prompt narrows what its agent reads.** Each entry already carries what its source states, so a section's body or a run page is read only for an entry whose text leaves its capability, support or scope open. Lookups are made together, and context is kept under about 250,000 tokens. On the settings centre this halved the cost, from 526,000 an entry to 248,000.
- **The build renders what governs a settings entry,** its gates included (`nodes:section`, `if:`).
- **`earlier` reads more formats:** a portal's `to:` and keys, the en and ar words, headings and whole route ids.
- **The router's ancestors' gates are added by script** (`method/held_router_gates.py`), not looked up by each agent.
- **The coordinator checks with fewer requests:** the checker's lines, the batch's open cases and a measure, with a sample against the sources only where a cell changes.

No agent has been stopped by the usage limit.

**Re-measured at about 06:55 UTC, by structure** (`method/count_tokens.py --since 2026-10-31T04:05`, and each checked batch's transcript).
- **Spent since 04:05:** 528 million tokens: the coordinator 93 million over 223 requests (18 percent), the agents the rest.
- **Salla is placed whole:** 57 batches, 5,750 entries, each checked. Shopify's checked batches are SH-1, SH-8 to SH-10, SH-34 to SH-38, SH-50 to SH-54 and SH-68 to SH-74.
- **Recent batches' contexts reached about 420,000 to 440,000 tokens,** against the 250,000 their prompts ask, and cost 144,000 to 372,000 an entry: SH-38 144,000, SH-74 248,000, SA-57 372,000 (Salla's carriers and themes, whose App Store listings it read). SH-1, the first of Shopify's other structures, cost 105,000.

| Structure | Entries left (the four running batches' among them) | Tokens an entry, on its checked batches |
| --- | --- | --- |
| Shopify `editions-page-data` | 1,124 | about 220,000 |
| Shopify `merchant-changelog` | 996 | about 193,000 |
| Shopify `admin-router` | 760 | about 173,000 |
| Shopify `pricing-page-data` | 434 | about 181,000 |
| Shopify's other 4,786 entries (permissions, plan pages, the mobile app, help notes and the rest) | 4,786 | not measured, but for SH-1's 105,000 |

| Item | Million tokens |
| --- | --- |
| Spent, by about 06:55 UTC: about 2,640 at 04:05 and 528 since | about 3,170 |
| The measured structures' 3,328 entries, at their rates | about 650 |
| The other 4,786 entries, at 120,000 to 220,000 | 570 to 1,050 |
| The coordinator's checks, about a fifth of the agents' (18 percent since 04:05) | 220 to 340 |
| The amendments and new things, the second stage, the omission review, the final review and its corrections, the architecture plan's review | 390 to 590 |
| **The extent, in all** | **about 5.0 to 5.8 billion** |

The extent stays within the 5.0 to 6.0 billion brought to the founder at 04:05, so no new projection goes to the founder. No agent has been stopped by the usage limit.

**Re-measured at about 08:35 UTC** (`method/count_tokens.py --since 2026-10-31T06:55`, and each checked batch's transcript).
- **Spent since 06:55:** 369 million tokens: the coordinator 74 million over 141 requests (20 percent), the agents the rest. In all about 3,540 million.
- **Checked since 06:55:** SH-1 to SH-7 (SH-5 by script, `method/held_role_permissions.py`), SH-11 to SH-13, SH-38 to SH-40, SH-55 and SH-56, SH-74 to SH-76. The first batches of Shopify's other structures cost 105,000 to 269,000 an entry, about 180,000 on average. The agents' contexts still reach 400,000 to 520,000 tokens, against the 250,000 asked, and their own estimates of it are half the measure.

| Item | Million tokens |
| --- | --- |
| Spent, by about 08:35 UTC | about 3,540 |
| The measured structures' 2,460 entries left, at their rates (Editions 247,000, changelog 202,000, router 195,000, pricing 191,000 an entry) | about 535 |
| The other 4,203 entries, at 120,000 to 250,000 | 500 to 1,050 |
| The coordinator's checks, about a fifth of the agents' | 210 to 320 |
| The amendments and new things, the second stage, the omission review, the final review and its corrections, the architecture plan's review | 390 to 590 |
| **The extent, in all** | **about 5.2 to 6.0 billion** |

**Re-planned to cost less.** The top of the range has reached the 6.0 billion of the founder's band. So structures whose entries repeat pages already placed are placed by script, as SH-5 and SH-52 were, wherever the repeat is exact. Candidates:
- the public plan page, which renders the pricing data's www.shopify.com page;
- the rendered Editions, which twin their page data;
- lists of one kind, such as the tracking carriers.

Each script's lines are checked like a batch's, and what it can't match goes to an agent.

**Re-measured at about 09:45 UTC** (`method/count_tokens.py --since 2026-10-31T08:35`, and each checked batch's transcript).
- **Spent since 08:35:** 240 million tokens: the coordinator 57 million over 138 requests (24 percent), the agents the rest. In all about 3,780 million.
- **Checked since 08:35:** SH-41, SH-57, SH-77 to SH-79, SH-95, SH-96, SH-102 (by script) and SH-30.
  - All of `pricing-page-data` is placed.
  - The last batches cost 126,000 to 368,000 an entry. Their contexts reached 335,000 to 513,000 tokens.
- **Cost cut since 08:35:**
  - The Editions rules digest (11.6 million) replaces seven batches' notes for SH-58 to SH-67.
  - The tracking carriers are placed by script (203 entries).
  - 99 rendered row headings of the public pricing page are read: the concern map cites their rows from the same record.

| Item | Million tokens |
| --- | --- |
| Spent, by about 09:45 UTC | about 3,780 |
| The measured structures' 2,199 entries left, at their rates (Editions 258,000, changelog 201,000, router 195,000, help notes 227,000 an entry) | about 495 |
| The other 3,347 entries, at 120,000 to 250,000 | 400 to 840 |
| The coordinator's checks, a fifth to a quarter of the agents' | 200 to 330 |
| The amendments and new things, the second stage, the omission review, the final review and its corrections, the architecture plan's review | 390 to 590 |
| **The extent, in all** | **about 5.3 to 6.0 billion** |

The top stays at the band's 6.0 billion, so no new projection goes to the founder. The re-plan goes on:
- digests for the changelog and the router;
- scripts where a structure repeats placed rows exactly;
- the coordinator's requests fewer, since at its context each costs about 400,000 tokens.

**Re-measured at about 11:40 UTC** (`method/count_tokens.py --since 2026-10-31T09:45`, and each checked batch's transcript).
- **Spent since 09:45:** 296 million tokens: the coordinator 43 million over 98 requests (15 percent), the agents the rest. In all about 4,080 million.
- **Checked since 09:45:** SH-14, SH-30 to SH-32, SH-42, SH-43, SH-58 to SH-61, SH-79 and SH-92 to SH-94. The pricing data and the public plan page are placed whole.
- **The digests cut the cost an entry:**
  - Editions from 329,000 (SH-57) to 164,000–244,000 (SH-58 to SH-61);
  - the changelog from 189,000 (SH-41) to 152,000–172,000 (SH-42, SH-43).

  The router's first batch with its digest, SH-14, cost 252,000, so its next prompt narrows what it reads.
- **The selection read 197 more entries as the model's own:** the public pricing page's table, its row headings and its mobile copy, which repeat rows the concern map cites from the same record.

| Item | Million tokens |
| --- | --- |
| Spent, by about 11:40 UTC | about 4,080 |
| The measured structures' 1,337 entries left, at their rates (Editions, changelog, router, help notes) | about 290 |
| The other 3,125 entries, at 120,000 to 250,000 | 375 to 780 |
| The coordinator's checks, a fifth to a quarter of the agents' | 135 to 270 |
| The amendments and new things, the second stage, the omission review, the final review and its corrections, the architecture plan's review | 390 to 590 |
| **The extent, in all** | **about 5.3 to 6.0 billion** |

The top stays at the band's 6.0 billion, so no new projection goes to the founder.
