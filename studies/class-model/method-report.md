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

