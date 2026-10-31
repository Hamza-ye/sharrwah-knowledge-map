# Review of the architecture plan, before GM (31 October 2026)

**What this is:** the review `PLAN.md`, Stage 4A, asks for before the architecture plan goes to the founder: it "is written by established practice before architecture starts, reviewed by an agent that made none of it, and brought to the founder at GM with the extent's report" (`PLAN.md` line 226). The reviewer made none of the plan, and changed no file except this one. As `PLAN.md` section 3 asks of a review, it tries to refute the plan claim by claim.

**What was read, and at which commits:**
- `architecture/plan.md` at `d9524f74`. Line numbers are the plan's at that commit.
- While the review ran, `HEAD` moved to `843d118a`. The new commits change only `STATE.md`, `reports/GM-rulings.md` (GM's veto list, drafted) and `studies/class-model/held/shopify/amendment-notes.md`. The plan, `PLAN.md`, `founder-decisions.tsv` and the merged model are unchanged, so the findings hold at `843d118a`. `STATE.md` and `reports/GM-rulings.md` are cited at `843d118a`.
- `PLAN.md`: Stage 4A (lines 205 to 240), and sections 1, 3, 5, 6, 8 and 9 where the plan relies on them. `founder-decisions.tsv` lines 8 to 34, and the founder's two messages of 30 October behind lines 29 to 31. `studies/class-model/seed/km-source-types.tsv`. `reports/intent-review.md`, sections 1 and 14. S-02's `decisions.md` (D1, D6, D7, D9, the engineering constraints) and `register.tsv` (S02-D9, S02-M6), and `studies/subjects/subjects.tsv`.
- `studies/class-model/review-dry-run-rulings.md` (S15, conventions 9 and 10), `review-dry-run-structure.md` (S15), `briefs/B-extent.md` (qualities), and `briefs/V-veto.md` and `reports/GM-rulings.md`, for whether the plan's decisions reach GM's veto list. `STATE.md` only where cited.
- The merged model, `studies/class-model/merged/` (`interfaces.tsv`, `qualities.tsv`, `slot-fillers.tsv`, `kinds.tsv`, `cells.tsv`, `capabilities.tsv`, `evidence.tsv`), by script, with `method/class_merge.py`, `class_slice.py` and `source_kinds.py` read, and run read-only.
- The evidence at observed-sh `04de369da`, observed-sa `b0bd0b163` and other-product-class `0d79b794f`, for the kinds of a few structures and the registers' descriptions, and `evidence/shopify-engineering/README.md`.
- The model's counts are as merged at `d9524f74`. The held pass's second stage (620 cells that hold nothing), the omission review, the final review and Q3's check are still to run (`PLAN.md` Stage 4A; `STATE.md` lines 255 and 265), so the counts will move.

What this review says of the books (Cervantes & Kazman; Kazman, Klein & Clements; Nygard; ISO/IEC/IEEE 42010 and 42020; Parnas; Evans; Baldwin & Clark; Sullivan et al.; Pohl et al.; Svahnberg et al.; Ford et al.) is a reading. I couldn't open them, and each reading names what it relies on.

Severity: **must fix** means the founder would approve something other than what the plan says, or the plan breaks a rule or a founder's decision. **Should fix** means the plan is less exact, complete or checkable than its sources ask, or leaves a go's consequences unsaid. **Note** is for the record.

**What holds:**
- The plan has a part for each of the five things `PLAN.md` lines 227 to 231 say it states. It carries the three rules of lines 234 to 236 and the founder's decision on code (`founder-decisions.tsv` line 10). Where it falls short is below.
- Its two grades of data, events and deciding statements are as convention 10 rules them (`review-dry-run-rulings.md` line 48), and as the merge computes them (`method/class_merge.py` lines 244 to 261):
  - `exact` where a cell cites a `boundary` or `decides` statement;
  - `by landing` for a landed concern's other such statements that no cell of its domain cites.

  `interfaces.tsv` holds 14,236 rows: 12,480 exact and 1,756 by landing.
- The worked example follows D9's text in its option, trigger, closing commitment, step and costs (`studies/subjects/S-02/decisions.md` lines 155 to 170). It writes the need without the market's name, as the guard asks (`PLAN.md` line 18).
- The Shopify engineering row matches its README: E001 to E040, captured on 10 October 2026, with the payment write-ups dated 2019 to 2022 (`evidence/shopify-engineering/README.md`).
- S-02's D1, D6, E1 and E2 are cited for what they say.
- These are the file's or the founder's own:
  - the DEC row and IDX's "never evidence" (`km-source-types.tsv` lines 15 and 5);
  - PRAC's line on merchants (`founder-decisions.tsv` line 11);
  - the scale row's "later" (`founder-decisions.tsv` line 28).
- The page (lines 5 to 23) is in plain words. The body's terms are in APR-17.

---

## Must fix

**APR-1. The plan says it decides no part of the architecture. It decides what every money record holds, changes S-02's D9 to do it, and lists nothing for the founder's veto.**
- *Found:*
  - Line 14: "It decides no part of the architecture itself." Line 16: "Every other decision is engineering's, and each is listed for your veto at the next report."
  - Lines 117 and 121 decide what every amount holds, and when: "every amount refers to a currency record, one per code at launch", and it "is taken with the cross-cutting decisions (section 3, item 3) rather than waiting for S-09". Line 86 makes it item 3 of the first decisions.
  - S-02 left that choice to S-09:
    - "Amounts refer to a currency record, one per code at launch, so naming an area later is a new record; that choice is S-09's" (`decisions.md` line 166);
    - the register calls it a currency record "which S-09 decides (S02-M6)", and S02-M6 moves to S-09 "what identifies a currency in money records" (`register.tsv` lines 21 and 27).

    The founder vetoed none of D1 to D9 (`founder-decisions.tsv` line 30), so line 121 changes an engineering ruling the founder passed. S02-D9's `kind` reads "founder decision", while its `status` reads "engineering's ruling (the founder's intent, 29 October), listed for the founder's veto; no veto". So a reader can take the change for a founder's decision reopened, which engineering may not do (`PLAN.md` line 220).
  - Line 79 decides how the platform is divided, and who owns the records: "Architecture's parts are cut by what changes together and by what data they own ... each part owns its model and its language". A reading of Evans' bounded contexts and of common practice: each part owning its records, so that no other part writes them, is a structural decision with an alternative (one shared set of records, behind modules), not a method only.
  - Neither is listed for veto, in any form:
    - GM's veto list leaves them to the plan. Its brief: "Not: ... the architecture plan's decisions, which the coordinator lists after the plan's review" (`briefs/V-veto.md` line 17). The draft: "The architecture plan's own decisions are listed with the plan" (`reports/GM-rulings.md` line 15). The plan lists none.
    - The founder's message asks of this plan: "Its decisions stay engineering's, each listed for my veto" (`founder-messages/2026-10-30-architecture-plan.md` line 17).
    - On 31 October the founder asked, of rulings listed by their codes, "how i can veto something i do not know what it means?" So each ruling comes saying what it decides, why, what it risks and its alternative (`V-veto.md` lines 3 to 7; `STATE.md` line 254).
  - D9's need "comes from the Yemen row alone" (`decisions.md` line 166). The guard asks that "each decision page says whether its recommendation comes out the same without Yemen" (`PLAN.md` line 18). Line 121 doesn't say.
  - So the founder would give a go on a plan that says it decides nothing, while it settles what every money record holds, before the subject that was to settle it.
- *Fix:*
  - Line 14: "It decides two things of the architecture, each listed for your veto in section 7. The rest is how the work is done."
  - Line 121, add: "This changes S-02's D9 and its move to S-09 (S02-M6), engineering's rulings you passed on 30 October. It is listed for your veto (section 7)." Then reconcile it with line 136 (APR-2).
  - Add before "Sources" the text below. Once the plan holds it, `reports/GM-rulings.md` line 15 points to it.
  - Outside the plan, S02-D9's `kind` in S-02's register could read as its `status` does.

```
## 7. What this plan decides, for your veto

### Every amount points to a currency entry, decided now
- **Decides:** every amount in the platform's money records (prices, stored amounts and reports) points to an entry in one table of currencies, instead of holding a bare currency code such as SAR. At launch the table has one entry per code. This is decided with the first decisions, before S-09 (the currency subject) runs; S-09 then decides which currencies and currency areas the table holds. It changes S-02's D9, which left this choice to S-09.
- **Why:** now it costs one reference per amount and one table. If amounts held bare codes and a market later needed two currency areas under one code, every money record, rate and report would have to change: a redesign (S-02's D9).
- **Risks:** it settles part of S-09's question before S-09 has looked at it; if S-09 finds that a currency needs more than a table entry holds, the entry's shape changes. Each provider that takes only a code needs the entry mapped back to it. The need came from one market alone (S-02's D9). Without that market, the step would rest on other needs of the same form, such as a currency that changes its unit, which one ledger design read for D9 keeps as a new record. Whether they alone would justify it is a reading.
- **Instead:** keep D9 as ruled. The first decision on money records keeps "what identifies a currency" open, and S-09 decides it; until then, a review rule stops any record from storing a bare code. It costs a wait, and a placeholder in every money record's design until S-09 has run.

### Each part of the platform owns its records
- **Decides:** the platform is divided into parts, each owning its records and its own words for them. Another part reads or changes them only through the part that owns them (section 3).
- **Why:** a decision likely to change is then held in one place (Parnas 1972), and each word keeps one meaning inside its part (Evans 2003).
- **Risks:** a report or a search across parts needs a path to each part's records; a part cut wrongly means moving records between parts later.
- **Instead:** one shared set of records for every part, with the decisions likely to change hidden behind modules. It is simpler at first; a change to a shared record then reaches every part that uses it.
```

**APR-2. The first decisions bind questions of subjects not yet run, against the rule the plan carries. The plan's copy of the rule drops its two examples, which are the two the plan then departs from, and two subjects gate nothing.**
- *Found:*
  - `PLAN.md` line 236: "an area's architecture that would bind a question a subject not yet run covers, such as S-09's currency of records or S-03's contracting company, keeps that variation point open until the subject has run." The plan's line 136 copies it without "such as S-09's currency of records or S-03's contracting company".
  - Line 98 says S-03's and S-09's questions "are settled with the cross-cutting decisions, or kept open there as variation points until the subject has run (`PLAN.md`, Stage 4A)". Stage 4A gives only the second.
    - S-03 asks "Who fills 'the contracting company' for sellers in each market, and under which law?", which `subjects.tsv` line 4 calls "a company question for the founder, with a lawyer".
    - It is on the founder's list: "the company, its legal structure and licences" (`founder-decisions.tsv` line 26). Engineering can't settle it.
  - Line 84 puts "where their data lives" in the first decision, and line 94 "where data lives after S-08". S-08 asks "Where do sellers' and buyers' data live and get processed, under which law, and for how long after a store closes?" (`subjects.tsv` line 9).
  - Lines 117 and 121 take S-09's currency record before S-09 runs (APR-1).
  - The other first decisions meet subjects not yet run too (a reading of the questions in `subjects.tsv`):
    - money records (item 3) meet S-04's payments, S-05's tax and invoices, and S-11's charges;
    - events and extension points (item 5) meet S-04's "how does a seller connect it, and what happens when one fails", and S-10's couriers;
    - identity (item 2) and markets (item 4) meet S-07's "Who verifies sellers, ... and which countries are served?".

    The plan names none of these.
  - Lines 92 to 98 place S-03, S-04, S-05, S-08, S-09, S-10 and S-11. S-06 (licences) and S-07 (verification and screening) come before nothing, though the founder asked "which subjects must land before which area" (`founder-messages/2026-10-30-architecture-plan.md` line 15; `PLAN.md` line 229).
  - The subjects run "in the list's order" (`founder-decisions.tsv` line 18), with S-03 next. So every first decision comes before S-03 to S-11 have run (a reading of that order).
- *Fix:*
  - Line 136: restore "such as S-09's currency of records or S-03's contracting company".
  - Line 98: "S-03's contracting company and S-09's currency of records bind every area that holds a contract or an amount. Each is kept open in the first decisions, as a variation point, until its subject has run. The contracting company is yours to decide (the company), so the design only keeps a place for it, and decides nothing of who it is."
  - After line 89, add the text and table below.
  - Lines 92 to 96, add: "licences (S-06) before any part that runs a regulated activity; seller verification and screening (S-07) before onboarding (ONB) and trust (TRU)". Or say why neither gates one.
  - If the currency decision of APR-1 stands, `PLAN.md` line 236 needs an exception, made as its section 9 says (a fix to the method, listed at the next report with what it weakens): "The cheapest step that keeps a subject's variation point open may be taken before the subject runs, where it closes only what a ruling in force already rules out. It is listed for the founder's veto." For D9 that holds: a bare code in every amount is already "S-09's to avoid" (`register.tsv` line 21, `closes`).

Each first decision keeps open what a subject not yet run will decide:

| First decision | Subjects it meets | Kept open until they run |
| --- | --- | --- |
| 1. How stores are kept apart, and where their data lives | S-08 | where data lives and is processed, and under which law |
| 2. Identity and permissions | S-07 | who verifies sellers, and how |
| 3. Money records and currency | S-04, S-05, S-09, S-11 | what identifies a currency (unless section 7's first decision stands); the payment, tax and charge records' own fields |
| 4. Markets and the seller's country | S-03, S-07 | the contracting company in each market; which countries are served |
| 5. Events and extension points | S-04, S-10 | how a payment provider or a courier connects, and what happens when one fails |
| 6. Configuration | S-11 | what Sharrwah charges, and each plan's limits (plans and prices are yours) |

**APR-3. The page's list of what is the founder's is shorter than the founder's own.**
- *Found:*
  - Line 16: "markets, plans and prices, agreements and partners, the company and its licences, spending, and whether Sharrwah's own company runs a service."
  - The founder's list also holds:
    - "which markets, in what order and when, and which merchants Sharrwah goes after first", and "the company, its legal structure and licences" (`founder-decisions.tsv` line 26; `PLAN.md` line 42);
    - "whether Sharrwah holds funds" (`PLAN.md` line 43);
    - the guard: "no arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision ... Building or switching on either arrangement, A or B, is the founder's decision too" (`PLAN.md` line 44; `founder-decisions.tsv` lines 8, 16 and 19).
  - The page then says "Nothing else in it is yours". The guard bears on the first decisions: money records (line 86) include what the founder's E2 calls "a holder's ledger of balances, holds and payouts ... a separate part, empty under C" (`founder-decisions.tsv` line 19).
- *Fix:* line 16, replace the list with: "which markets, in what order and when, and which merchants Sharrwah goes after first; plans and prices; commercial agreements and partners; the company, its legal structure and licences, and whether Sharrwah holds funds; spending; and whether Sharrwah's own company runs a service in the merchant's business, where and when. Building or switching on an arrangement that holds sellers' money, A or B, is yours too, under your guard: the design keeps room for both, empty while C holds (your decisions of 18, 25 and 26 October)."

**APR-4. The source grades depart from the Knowledge Map's file the founder chose. REF is redefined against the file's own examples, ECO is in neither list, and "what each can't tell" is in the plan's words, not the file's.**
- *Found:*
  - The founder: "use the Knowledge Map's source types, with what each can't tell" (`founder-messages/2026-10-30-before-gm.md` line 13; `founder-decisions.tsv` line 31). Line 27 says the plan does.
  - Line 48 says REF "means a platform beyond the five, such as Adobe Commerce".
    - The file's REF row gives "Zid, BigCommerce, Adobe Commerce, WooCommerce docs and APIs" as its examples, graded "One more vote on commonality; read at declaration level" (`km-source-types.tsv` line 6).
    - The plan grades Zid's and WooCommerce's sources by their type instead (line 27). A reading: that suits a model that counts the five alike (`PLAN.md` Stage 4A, "The kind and the count").
    - But it changes the founder's chosen scale without saying so, and line 48 tells the founder that the file says what it doesn't.
  - ECO is neither in the table (lines 34 to 43) nor under "Left out" (lines 46 to 48). The file defines it as "Third-party ecosystem", with examples "App listings and reviews, community forums, partner sites" (`km-source-types.tsv` line 11).
    - The model cites such sources. Salla's dashboard App Store holds "30 app entries in all" (observed-sa's `structures/REGISTER.tsv`, `salla/app-store-tabs`). Cells cite 29 of its held-pass entries, and 109 rows of `merged/qualities.tsv` are those apps' prices and trials. Cells also cite 26 entries of Salla's theme marketplace.
    - `source_kinds.py` calls both "observed", so by lines 28 to 30 they read as OBS.
  - "What that can't tell" is the plan's own words, row by row. Rows 1 and 3 (lines 34 and 36) carry neither of the two limits that bear most on the model's placements (`km-source-types.tsv` lines 2 and 3):
    - DECL's "Whether it behaves that way", graded "check against OBS, because declarations disagree with what is served";
    - SHIP's "What the server allows for a given store, plan or role", graded "Strong for existence, weak for availability".
- *Fix:*
  - After line 30, add "Each type's limits, in the Knowledge Map's own words:" and the table below. Keep it beside the per-row column, which then says only what a row adds.
  - Line 48: "**REF:** the Knowledge Map's file names Zid, BigCommerce and WooCommerce as further references: one more vote, read at declaration level. Here they are three of the five references, which the model counts alike (`PLAN.md`, Stage 4A), so their sources are graded by type, as Shopify's and Salla's are. REF is kept for a platform beyond the five, such as Adobe Commerce, read only where a decision needs one more comparison. This reading of the file is engineering's, listed for your veto." Add it to the plan's section 7 (APR-1), in the same four parts.
  - Add a row to the table: "| What merchants add through apps and partners | The app and theme stores' listings the model cites, read where a slot's design needs them | ECO | The platform's intent; weak one by one, strong in aggregate |". Or list ECO under "Left out", with why.

| Type | What it can't tell | Its grading |
| --- | --- | --- |
| DECL | Whether it behaves that way, or why it exists | Authoritative on intent; check against OBS, because declarations disagree with what is served (sa.readme) |
| SHIP | What the server allows for a given store, plan or role | Strong for existence, weak for availability |
| OBS | Whether it generalises to other stores, plans or regions | Strongest for behaviour; always cite the instrument it was seen with (sh.instruments) |
| ECO | The platform's intent | Weak one by one, strong in aggregate |
| OSS | Product completeness, or what SaaS merchants actually get | Strong for internals; check the fit with the product class |
| STD | Product behaviour | Normative wherever it is adopted |
| LAW | How platforms implement it (Salla shows one implementation for its market) | Normative; cite the instrument and its date |
| PROV | The platform's own behaviour | Authoritative for the provider; changes often |
| LIT | Facts about this product | Strong for method; a vendor blog is one company's account |
| EXP | The reference product | Strongest for engineering questions |
| DEC | Nothing about the world: a decision is not evidence | Recorded with date and rationale (an ADR) |

## Should fix

**APR-5. The reconciliation with section 6's kinds isn't one to one, and three rows' grades follow neither scheme.**
- *Found:*
  - Lines 28 to 30 map observed to OBS, shipped to SHIP, and stated and official page to DECL. A reading: the file sorts by what a source is, and section 6 by how it was obtained. So they part on two kinds of source (`method/source_kinds.py`, run on held structures):
    - **an API's published schema** is "shipped" (`PLAN.md` line 303, "code or a schema the platform ships"; `source_kinds.py` line 3). The script gives Shopify's `admin-graphql-schema` "shipped". The file puts "API schemas" under DECL (`km-source-types.tsv` line 2).
    - **a list or menu the admin served in a recorded session** is "observed". The script gives Shopify's `dev-dashboard-scopes` and `admin-main-nav`, and Salla's `dashboard-webhook-events`, "observed": "built from a recorded session". The file puts "served navigation trees" under SHIP (line 3).
  - Line 35 grades data and events "SHIP, DECL". Of the 506 held-pass `boundary` entries in `interfaces.tsv`, 259 come from two "observed" structures: Shopify's scopes (196) and Salla's webhook events (63). They are OBS by the plan's mapping, and SHIP by the file's sort.
  - Line 36 grades the subjects' registers "DECL, OBS".
    - S-02's own statements include 322 of kind "shipped" (`studies/subjects/S-02/kinds.tsv`).
    - A register also holds engineering's rulings, readings of cause and the founder's decisions (its `status` column: "engineering's ruling", "founder's, in force"). None of those is evidence.
  - Line 37 grades slot fillers "PROV, LAW".
    - The model's fillers are a platform's own statements naming a provider or a law (convention 9, `review-dry-run-rulings.md` line 47). Of 2,476 rows, 2,116 cite a held-pass entry and 343 a concern-map statement. By their source they are DECL, SHIP or OBS.
    - PROV and LAW are the providers' and regulators' own documents, the row's third source.
  - Line 38 grades qualities "DECL". Of the 3,654 quality rows that cite a held-pass entry, 517 come from structures `source_kinds.py` calls "observed", such as Shopify's plan page in the admin and Zid's plans offered.
  - The model records no grade: no file in `merged/` has a kind or a type column.
- *Fix:*
  - Replace lines 28 to 30 with: "Each citation's type follows section 6's kind, which `method/source_kinds.py` assigns by rule: observed is OBS, shipped is SHIP, and stated and official page are DECL. Where the two schemes sort a source differently, the Knowledge Map's sort holds, and section 6's kind is kept beside it, so that like is still compared with like:
    - an API's published schema is DECL, though section 6 calls it shipped;
    - a list or menu the admin served in a recorded session is SHIP, though section 6 calls it observed.

    The model records no type: each design grades the citations it uses."
  - Line 35 then holds as "SHIP, DECL".
  - Line 36: "DECL, SHIP, OBS, as each cited statement's kind. A register's causes are readings, and its rulings engineering's: neither is evidence."
  - Line 37: "The model's slot fillers: a platform's statement naming a provider or a law (DECL, SHIP, OBS). Providers' and regulators' own documents (PROV, LAW)."
  - Line 38: "DECL, SHIP".

**APR-6. The model's data and events are much coarser than section 1 says: nearly half the held cells have none.**
- *Found:*
  - Line 50 says "Each capability's data, events and deciding statements are derived by the merge", and line 54 that "what is coarse is said plainly". Lines 51 and 52 say how they are derived, not how much is missing.
  - In `merged/interfaces.tsv`, by script:
    - of the 1,215 cells that hold statements, 572 (47%) have no `boundary` row of their own platform, so no data or events, and 260 (21%) have no `decides` row. 165 have neither;
    - of the 367 capabilities, 74 have no `boundary` row from any platform. Among them are customers' personal data in the store (CM-TRU-005), the merchant's country at sign-up (CM-ONB-001) and the platform's fee on sales (CM-PLN-003);
    - 9 capabilities have no row at all: CM-ANL-007, CM-APP-013, CM-B2B-005, CM-CAT-014, CM-CHK-012, CM-ONB-005, CM-SRF-003, CM-SUP-007 and CM-TRU-022.
  - The dry run found the same, in 27 of 56 held cells (48%). Its review said "The capabilities with no boundary statement at all are gaps to record, not derivations" (`review-dry-run-structure.md` line 194).
  - It found the exact grade incomplete too: "The parts cite a sample of each family of topics, so a merge by citation misses the rest of the families they cite from" (line 192). Line 51 calls the grade "exact" without that caveat.
  - A held-pass entry takes `boundary` or `decides` from its structure as a whole (`held/selection.tsv`'s `placement`; `class_slice.py` line 203), not from what the entry says. All 7,524 exact `decides` rows from the held pass are placed so.
- *Fix:* after line 54, add the paragraph below, and with it APR-7's.

```
As merged at `d9524f74`, what is missing is a gap, not a derivation (the dry run's review, S15):
- 572 of the 1,215 cells that hold statements have no data or events of their own platform, and 260 nothing that decides them; 74 of the 367 capabilities have no data or events from any platform. A design that needs them reads the evidence for them, through the evidence map (`PLAN.md`, section 6);
- the exact grade is incomplete too: a part cites a sample of a family of topics or scopes, and the rest goes by landing to the parent, or nowhere;
- a held-pass entry is `boundary` or `decides` by its structure, not by what it says.

The held pass's second stage, the omission review and the final review may close some of these before GM; the counts are measured again then.
```

**APR-7. The model's qualities, slot fillers and scopes are coarser than section 1's rows say.**
- *Found:*
  - **Qualities.** Line 38 reads "The qualities the class states: limits, certifications, uptime, where data lives | The model's qualities". `merged/qualities.tsv` holds 3,881 rows:
    - 3,297 are Shopify's, and 2,609 come from one structure, Shopify's pricing pages (`pricing-page-data`);
    - about 2,490 are prices, fees, rates or trials (a reading, by a pattern on the label).

    The brief names four kinds of quality (`briefs/B-extent.md` line 125). Few rows hold them:
    - **uptime:** Shopify's "99.9%", Salla's "100% uptime" and BigCommerce's Cyber Week figure, on CM-OPS-001. Zid's cell holds nothing, and WooCommerce's is `not-stated`;
    - **where data lives:** one Shopify row and three BigCommerce rows, on CM-TRU-014. Salla's cell holds nothing;
    - **card-data certification:** Shopify, WooCommerce's payments service and BigCommerce, on CM-TRU-018. Salla's and Zid's cells hold nothing.

    The first decision is how stores are kept apart and where their data lives (line 84). `reports/intent-review.md` section 1 asked that "Architecture then starts from evidence in those areas, not blind". For the two regional platforms, it starts with almost none.
  - **Slot fillers.** Line 37 reads "What fills a slot in a market". `merged/slot-fillers.tsv` has no market column, and convention 9 says a filler's "market comes only from a market scope".
    - Of its 2,476 rows, 1,310 cite a statement with any scope.
    - 606 cite a scope that names a country or a region (a reading, by a pattern): Salla 13, Zid 13, BigCommerce 12.
  - **Scopes.** Line 36 reads "the model's `decides` statements and scopes".
    - A cell's `scopes` are each statement's own words in one field: plans, countries, stores, staff permissions and feature gates together. CM-ACC-001's Shopify cell, for one, holds "support.inboundPhone and not appDevelopment.cliAppDev" and "Basic;Grow;Advanced;www.shopify.com" (`merged/cells.tsv`). 789 of 1,835 cells have them.
    - Nothing types a scope as a market, a plan or a store. Section 14's test of the hypothesis reads "A capability's own scope, in its cells" (`reports/intent-review.md` line 266).
- *Fix:* after APR-6's paragraph, add:

```
- **Qualities:** most rows are Shopify's plan prices. Of what the first decisions need, little is held: uptime from Shopify, Salla and BigCommerce; where data lives from Shopify and BigCommerce; card-data certification from Shopify, WooCommerce's payments service and BigCommerce. Salla holds nothing on where data lives or on card data, and Zid nothing on uptime or on card data. The first decisions read the evidence for these, and say so.
- **Slot fillers** carry no market. A filler's market is its statement's scope, where one is stated; what fills a slot in a given market comes from the subjects.
- **Scopes** are the statements' own words, untyped. A design that needs a market's, a plan's or a store's scope (configuration, item 6, and the test of `reports/intent-review.md`, section 14) types them as it reads them.
```

**APR-8. What a go commits the founder to is unsaid: the cost, what starts first, and when and how the founder sees a decision.**
- *Found:*
  - **Cost.** The plan names no budget for architecture: the word isn't in the file.
    - `PLAN.md` section 8 brings a stage to the founder when it "runs past its budget by a quarter" (line 413), and each subject's budget is "set before it starts" (line 191). Without a budget, that check can't fire.
    - For scale: the extent's budget was 250 million agent tokens (`PLAN.md` line 240), and its projection is "about 5.4 to 5.6 billion" (`STATE.md` line 272).
    - A reading of ISO/IEC/IEEE 42020, relying on its account of architecture management: a plan of this kind states the work's resources and how they are watched.
  - **What starts first** is unclear.
    - The page's step 1 is the six decisions (line 19).
    - The body groups capabilities into candidate parts "once the model has its extent" (line 80).
    - It weighs every decision against "the quality scenarios it must meet (section 5)" (line 61), which nothing says are written first.
  - **When and how the founder sees decisions.** Line 23 says "at each milestone", and the first milestone comes "After the cross-cutting decisions" (line 127).
    - So all six first decisions, the costliest to change, are made, reviewed and built on before the founder sees one.
    - The page doesn't say the decisions come in plain words, as the founder asked on 31 October (APR-1).
    - Nor does it say that a decision on the founder's list may be deferred: `PLAN.md` line 281, "Defer is always allowed".
- *Fix:* replace lines 18 to 23 with:

```
**What happens on your go,** in this order:
1. The quality scenarios and the scale bands are written (section 5), and the model's capabilities are grouped into candidate parts (section 3). They come to you in a first short report, before any decision builds on them: the bands stand in for your scale numbers, so you can correct them.
2. The six decisions that cut across every area (section 3). Each keeps open what a subject not yet run will decide.
3. Then the parts, in the order section 3 sets, each after the subjects it waits for, beside the subjects still to run.
4. The whole is evaluated after step 2, and after each group of parts (section 5).

**What it costs.** Each step has a budget, set before it starts from measured cost, and recorded in `STATE.md`. Past a quarter over it, the cost comes to you with a projection, and the work goes on, re-planned to cost less (`PLAN.md`, section 8).

**What you'll see:** at each report:
- each decision made, in plain words, for your veto: what it decides, why, what it risks and its alternative;
- the options kept open, with their cost;
- the evaluation's findings;
- any decision on your list, with its evidence, its options and a recommendation, or defer;
- the cost against the budget.

A veto reverses a decision as section 2 says.
```

**APR-9. How the model's areas become parts, and what the second step designs, is unclear. The order of areas isn't stated.**
- *Found:*
  - Line 79: "The model's areas aren't architecture's parts." Yet line 91 and the page's step 2 (line 20) then say "Then the areas".
  - Line 91's "when the model's parts are known" can be read as the extent's parts (`studies/class-model/parts/`), which are known now.
  - Line 80 groups capabilities "by the data and events they share and the decisions that would change them".
    - A reading of Parnas (1972), relying on its two decompositions of one system: its criterion hides each decision likely to change behind one module, and it argues against modules cut by the data they share.
    - The two criteria can disagree, as D9 shows: the currency record is one decision, used by every part that holds an amount. No grouping by shared data gives it.
    - The plan doesn't say which governs, who groups, or how the grouping is checked.
  - The founder asked "which areas come first" (`founder-messages/2026-10-30-architecture-plan.md` line 15). The plan gives a rule (line 91), and defers the order until the parts are known.
  - Lines 92 to 96 name areas loosely. "Where data lives" is no area of the model, but a capability (CM-TRU-014), beside OPS's hosting (CM-OPS-003).
- *Fix:*
  - Line 80: "So once the model has its extent, the coordinator groups its capabilities into candidate parts. A decision likely to change gets a module of its own first, even where several parts use it, as the currency record does (Parnas). Then the capabilities that share and change the same records form a part (Evans). Each part records which capabilities and areas it holds, and what it hides. An agent that made none of it reviews the grouping against the model before any decision builds on it."
  - Line 91 and line 20: "Then the parts". In line 91: "The order is set when the candidate parts are known, and it comes to you in the first report."
  - Lines 92 to 96, by the model's areas: "the parts that hold payments (PAY) after S-04; taxes and invoicing (TAX) after S-05; where data is stored and processed (CM-TRU-014), and hosting (CM-OPS-003), after S-08; shipping and delivery (SHP) after S-10; the platform's plans and billing (PLN) after S-11."

**APR-10. The definition of keeping room weighs an option's cost but not its worth. Its check can't exist before code, and the worked example lacks its binding time.**
- *Found:*
  - **Worth.** Line 111: "This guards both failures: an option closed by a default nobody examined, and one built before it is worth its cost." The five conditions (lines 105 to 109) state the cost to hold and to exercise, and nothing of how likely the trigger is, or what exercising it would be worth.
    - A reading of Baldwin & Clark (2000) and Sullivan et al. (2001), relying on their account of a module's option value: it grows with the uncertainty it covers, and is weighed against its cost. Costs alone show that an option is cheap, not that it is worth holding.
    - The founder's intent asks room for each thing the class shows (`founder-decisions.tsv` line 26), which is 367 capabilities. Nothing in the five conditions stops every cheap step from being taken.
  - **Grain.** The plan doesn't say at what grain options are named: per capability (367), per variation point, or per part, whose interface keeps room for what it holds. That grain sets most of the cost.
  - **The check.** Line 109 says it is "a test that fails when the step is undone (a fitness function), or a review rule". Production code waits for the description (line 137; `founder-decisions.tsv` line 10).
    - A reading of Ford, Parsons & Kua (2017), relying on their fitness functions running against a system: until there is code, only the review rule can run.
    - So line 120's test can't exist during architecture.
  - **Binding time.** Condition 3 names "a declared variation point with its binding time" (line 107), which `PLAN.md` line 230 asks the definition to carry (Pohl et al.; Svahnberg et al.). The worked example (lines 113 to 121) names none, though D9's own text has one: "naming an area is built with the setup of the market that needs it" (`decisions.md` line 166).
- *Fix:*
  - Line 108: "4. what it costs to hold, what it would cost to exercise later, and how likely its trigger is, and why (a reading, where no evidence states it), are stated. A step costlier than an interface is taken only where its trigger is likely enough to be worth it. Otherwise the option is named, with what would close it, and left to the build."
  - Line 109, add: "Until code exists, the check is a review rule, applied to each record by its reviewer. The test is written with the first code that could undo the step."
  - After line 104, say at what grain options are named. For example: "Options are named per part: a part's interface keeps room for every capability it holds. An option gets a record of its own only where a step beyond that interface is needed: a variation point, a reference such as the currency record, or a part kept empty, as a holder's ledger is under C."
  - After line 119, add: "- **Its binding time:** when a market that needs it is set up: a new currency record and its mappings. That is a setting, not a release."

**APR-11. The evaluation uses half of ATAM's utility tree, names no one to evaluate, and drops a clause of the founder's order.**
- *Found:*
  - **The tree.** Line 125: "Each quality gets scenarios with a stimulus, a response and a measure, in a utility tree ranked by that order". A reading of ATAM's report (CMU/SEI-2000-TR-004), relying on its account of the utility tree:
    - its scenarios name a stimulus, the environment it comes in, and a response;
    - each leaf is rated twice, by how much it matters and by how hard it is to achieve, and analysis goes to the leaves high on both.

    The plan keeps one rating, the founder's order. The second is how "Effort follows risk" (`PLAN.md` section 1) reaches the evaluation.
  - **Who evaluates.** Line 127: "the architecture as a whole is walked through the scenarios". Who walks it isn't said. ATAM's evaluation team is apart from the architects (the same reading). Each record has an agent that made none of it (line 73); the whole has none.
  - **When, and who sets the measures.**
    - Nothing says when the tree is written, though every decision is weighed against it (line 61).
    - Nothing says who sets each measure. The bands are assumptions until the founder gives numbers (line 126), but the measures aren't said to be.
    - A measure such as an uptime promised to merchants would be a commercial promise, on the founder's list ("plans and prices; commercial agreements", `founder-decisions.tsv` line 26). That is a reading.
  - **The founder's order.** It reads "completeness, read as what each release delivers, never what the model covers" (`founder-decisions.tsv` line 28). Line 125 drops "never what the model covers".
  - **Regional fit.** It is how Sharrwah competes, beside quality (`founder-decisions.tsv` line 25). It is weighed in each design (line 134), but has no scenario, so no milestone can test it.
- *Fix:*
  - Replace line 125 with: "**Quality scenarios.** Your order (trustworthiness; then coherence and user experience; then performance; then completeness, read as what each release delivers, never what the model covers) is a ranking. Architecture needs measurable scenarios. Each quality gets scenarios with a stimulus, the conditions it comes in, a response and a measure, in a utility tree (Kazman, Klein & Clements 2000). Each leaf is rated twice: how much it matters, by your order, and how hard it is to meet, by engineering's estimate. The design and the evaluation start with the leaves high on both. The tree is written before the first decision, and comes to you with the first report. Each measure is engineering's assumption, marked as one, like the bands. A measure that would become a promise to merchants, such as an uptime, comes to you."
  - Line 127, add: "The walk is made by an agent that made none of the architecture. It records risks, non-risks, sensitivity points and trade-offs."
  - Line 129, add: "and regional fit's: a market's local payment provider or courier plugs into its slot with no change to the core."

**APR-12. How a decision is reversed isn't said, whether by the founder's veto, a subject's result or a change in the model, and the record has no status.**
- *Found:*
  - **The record's form.** Lines 65 to 69 give it its context and drivers, its options and evidence, the decision and why, and what it keeps open, closes and what would reopen it.
    - A reading of Nygard (2011), relying on its account of a record's parts (title, context, decision, status, consequences): a record carries a status, and a reversed decision is kept and marked superseded, not edited.
    - The plan's record has no status. Its options and evidence come from later forms of the record, not Nygard's (the same reading), which is no fault.
  - **A veto.** The founder vetoes "at the next report" (line 16), after the record has been reviewed and built on (line 73). Nothing says what a veto does to the records built on it. GM's veto list says it for the model's rulings: "A vetoed ruling stops. Engineering then takes its alternative, or the one you name, amends the model where the ruling placed lines, and tells you what moved" (`reports/GM-rulings.md` line 17).
  - **A subject's result.** A subject that runs later can find a record wrong.
    - Stage 4A says what happens when a subject's point conflicts with the model (`PLAN.md` line 220). Nothing says what happens when one conflicts with a record.
    - Line 62 makes "the subjects' rulings" constraints, while line 121 changes one (APR-1).
  - **A change in the model.** The model changes after GM: the subjects' points land as each ends, and amendments follow (`PLAN.md` line 220).
    - A record that cites a capability doesn't say at which commit, and nothing checks it again when the capability changes.
    - `PLAN.md` section 7, risk 7, lists the subjects whose citations changed. Nothing does so for records.
- *Fix:*
  - Lines 65 to 69, add:
    - "its status: proposed, accepted on its review, vetoed, or superseded by a later record, which it names. An accepted record is never edited: a change is a new record that supersedes it (Nygard 2011);"
    - "what it builds on: the records, rulings and capabilities it rests on, the capabilities at the model's commit."
  - After line 75, add:

```
- **How a decision is reversed:**
  - your veto: the record is marked vetoed. Engineering takes its alternative, or the one you name; each record that builds on it is listed and ruled again on its evidence, and the list comes with the next report;
  - a subject's result: a record that conflicts with a subject's ruling is reopened with the subject's evidence, not forced to fit, and ruled again for your veto. A conflict with your own decision comes to you (`PLAN.md`, Stage 4A, for the subjects' points);
  - a change in the model: when a capability a record cites changes, the records that cite it are listed and checked again (`PLAN.md`, section 7, risk 7).
```

**APR-13. The description's views and stakeholders, and when it is enough for the build, aren't stated.**
- *Found:*
  - Line 71: "The architecture description gathers the records into views of the whole (ISO/IEC/IEEE 42010:2022)." A reading of 42010, relying on its account of an architecture description:
    - it names its stakeholders and their concerns;
    - each view is governed by a viewpoint that frames named concerns;
    - decisions and their rationale are recorded beside the views, and the views aren't made by gathering records.

    The plan names no stakeholder, concern or view.
  - Production code waits for "requirements, an architecture description and engineering documentation" to validate it against (line 137; `founder-decisions.tsv` line 10). At the shore, "the first version's build is planned on the architecture written by then" (`PLAN.md` section 1). The plan doesn't say what the description must hold for either.
  - ISO/IEC/IEEE 42020:2019 is named as the plan's practice in `PLAN.md` (line 238) and in the plan's sources (line 145), but used nowhere in its text.
- *Fix:*
  - Replace line 71 with the text below.
  - For 42020, either map the plan's sections to its processes in one line (governance: section 2; management: the cost and the order, on the page; conceptualization: section 3; evaluation: section 5; elaboration: the description), or drop it from the sources.

```
The architecture description names its stakeholders and their concerns (ISO/IEC/IEEE 42010:2022): you (your list and your quality order), engineering, the teams who set up each market, the developers of apps and providers, and the build that validates against it. Each view answers named concerns:
- parts: each part, the capabilities and areas it holds, and what it hides;
- records: which part owns each record, and how the others reach it (Evans 2003, the context map);
- variation: each variation point, its variants and its binding time (Pohl, Böckle & van der Linden 2005);
- where data lives: per market and store, once S-08 has run;
- slots and events: how apps, providers and couriers plug in, from the model's data and events.

The records sit beside the views, and each view names the records it rests on. The description is enough for the first version's build when each capability that version needs sits in a part, each first decision is accepted, and each option kept open has its check. The build's requirements and engineering documentation are planned with it, at the shore (`PLAN.md`, section 1).
```

**APR-14. The founder's decisions that bind the design aren't named, and the plan doesn't apply its definition to A and B, as `PLAN.md` says it does.**
- *Found:*
  - Line 62 gives the constraints as "the founder's decisions, the subjects' rulings, and the law". None is named. First decision 3 is money records, yet the plan never mentions:
    - Decision 1: C in every market at launch, with three defaults (`founder-decisions.tsv` line 16);
    - E1 and E2 (line 19), and default 2 at launch (line 20);
    - the guard (line 8);
    - RD2's plan items (line 30).
  - `PLAN.md` line 44: "The platform keeps room for both (26 October), as the architecture plan defines keeping room (Stage 4A)." Section 4 works D9 only.
    - The founder's E1 and E2 are already a form of room: "Who holds sellers' money is a market's setting ... a holder's ledger of balances, holds and payouts is a separate part, empty under C" (`founder-decisions.tsv` line 19).
    - Nothing says the definition takes them as given, or what happens if a condition disagrees with them. Stage 4A sends such a conflict to the founder (`PLAN.md` line 220).
  - Section 6 carries neither the narrowing test (`PLAN.md` line 338) nor the guard on the first market (`PLAN.md` line 18). Both bind every decision the plan governs.
- *Fix:*
  - Line 62, replace with: "- its constraints: the law where a market's law binds; the subjects' rulings, which a design may rule again on evidence, listed for your veto; and your decisions in force, which engineering doesn't reopen: Decision 1 (C in every market at launch, with its three defaults); E1 and E2 (who holds sellers' money is a market's setting; an order's payment record is the same whoever holds it; a holder's ledger is a separate part, empty under C); default 2, at launch; the guard on A and B; and RD2's plan items, which are yours."
  - After line 111, add: "**A and B, under your guard,** are kept by your E1 and E2 (26 October). The first decision on money records shows E1 and E2 against the five conditions above. Where a condition disagrees with what you decided, the conflict comes to you with its evidence."
  - Section 6, add:
    - "**the narrowing test:** a design that leaves out what the class establishes, or its room, needs a reason with evidence (`PLAN.md`, section 6);"
    - "**the guard on the first market:** a need only one market shows is written without its name, and each record says whether it comes out the same without that market (`PLAN.md`, section 1)."

**APR-15. How architecture reads evidence the model doesn't hold isn't said, and the plan closes practitioners as a source, which is the founder's to open.**
- *Found:*
  - Designs read sources "for each decision that needs them" (line 41), and "as it reads its capabilities in depth" (line 54). Nothing says how, though three rules say it:
    - `PLAN.md` section 6 makes the evidence map "every reader's entry point" (line 360);
    - the founder requires each repository's guides and indexes first (`founder-decisions.tsv` line 33);
    - what isn't held goes as a capture request in `handoffs/` (line 24).
  - Line 47 leaves out capture indexes as "a finding aid, never evidence". Yet they are how evidence is found: the file calls them authoritative for "Where to look, coverage and joins" (`km-source-types.tsv` line 5). "Left out" can be read as not reading them.
  - Line 46 leaves out practitioners because "the agencies and former platform engineers it also names could be reached only by the founder".
    - `PLAN.md` line 381 sends a question that documents can't settle "to the platforms, partners, regulators or a lawyer, through the founder".
    - Contacting third parties, and paying for advice, are the founder's (`PLAN.md` section 3, items 3 and 4).
    - The founder ruled out merchants only (`founder-decisions.tsv` line 11). Closing the route is a narrowing the founder didn't make.
- *Fix:*
  - Line 47: "**capture indexes (IDX):** how evidence is found, never what is cited (below)."
  - Line 46: "**Practitioners (PRAC):** merchants are never asked (`founder-decisions.tsv`, 24 October). Agencies and former platform engineers aren't planned. Where documents can't settle a decision, a request to reach one may come to you, since contacting them, and paying for advice, are yours (`PLAN.md`, section 3)."
  - After line 48: "**Where a decision needs more than the model holds,** its design reads the evidence through the evidence map and each repository's own guides and indexes first, then searches (`PLAN.md`, section 6; your decision of 30 October). What isn't held goes as a capture request in `handoffs/`, not to you (your decision of 27 October)."

**APR-16. The plan names no risks of its own, nor how they are watched.**
- *Found:*
  - `PLAN.md` section 7 lists the work's risks. None is about designing the architecture.
  - Several show in this review: first decisions that bind subjects not yet run (APR-2), designs resting on a model with no data or events for 47% of held cells (APR-6), qualities drawn from one platform (APR-7), an architecture with no budget (APR-8), and checks that can't run before code (APR-10).
  - A reading of ATAM and ADD, relying on their outputs (ATAM's risks and risk themes; ADD's analysis at each iteration): a plan of this kind says which risks it watches, and how.
- *Fix:* add a section after section 5:

```
## 5A. Risks, and how they are watched

| Risk | How it shows | What happens |
| --- | --- | --- |
| A first decision binds a question a subject hasn't run | A record decides what `subjects.tsv` gives a subject not yet run | The review refuses it; the question is kept open as a variation point (section 6) |
| A design rests on what the model doesn't hold | A record cites a capability with no data or events of its own, or only "by landing" | The design reads the evidence for it, and the record says so |
| One platform shapes the qualities | A measure or a band rests on one platform's statements | The record says so, and the measure stays an assumption |
| The cost grows unseen | A step's projection passes its budget | It is re-planned; past a quarter over, it comes to you (`PLAN.md`, section 8) |
| An option erodes before code exists | A record adds a field or a path that undoes a step | The review rule refuses it; the test comes with the first code |
| One market's need shapes a core decision | A record's reason comes from one market alone | The record says whether it comes out the same without that market |
```

**APR-17. Terms a go depends on aren't defined.**
- *Found:*
  - `PLAN.md` line 55: "Everything for the founder is in plain business words, and a term that can't be avoided is defined in one line." The founder's question of 31 October shows that a go needs these terms understood (`V-veto.md` line 3).
  - Used without a definition:
    - "variation points" (line 102), "binding time" and "indirection" (line 107);
    - "utility tree" (line 125), and "sensitivity points and trade-offs" (line 128);
    - "attribute-driven design" (lines 59 and 83).
  - "Fitness function" (line 109) and "bounded contexts" (line 79) are defined where they are used.
- *Fix:* after the page, add:

```
**Words used below:**
- **variation point:** a place in the design where markets, stores or plans can differ;
- **binding time:** when that difference is set: at build, when a market is set up, or by a store's setting;
- **indirection:** a reference that lets what it points to change without changing the records that use it;
- **utility tree:** your qualities in your order, each broken into tests with a measure;
- **sensitivity point:** a design choice that a quality depends on;
- **trade-off:** a choice that helps one quality and costs another;
- **attribute-driven design:** designing step by step, each step settling the decisions that the highest-ranked qualities depend on.
```

## Notes

- **APR-18.** "The 41 areas" (line 79) are the seed's (`seed/km-areas.tsv`). 36 of them hold the model's 367 capabilities. H's four (WLD, ENG, INT, MTH) take none by design (`PLAN.md` Stage 4A), and LNG ("Vocabulary and Arabic") holds none. Say "the 41 areas, 36 of which hold capabilities".
- **APR-19.** The status (line 3) says the plan was finished "once the held pass was in the model". In `PLAN.md`, the held pass includes its second stage: "each cell still holding nothing is read against the held pages" (Stage 4A, line 222). That stage hasn't run on its 620 cells (`STATE.md` lines 255 and 265). Say "once the held pass's first stage was in the model", and measure section 1's claims again before GM (APR-6, APR-7).
- **APR-20.** A reading of Cervantes & Kazman (2016), relying on ADD 3.0's inputs: its drivers are the design purpose, the primary functionality, the quality scenarios, architectural concerns and constraints.
  - Lines 59 to 62 name three of them. The six first decisions are architectural concerns in ADD's sense, and the design purpose is in `PLAN.md` section 1 (one platform, many markets; the first version's build planned at the shore).
  - The order "of their dependencies" (line 91) is the coordinator's own rule, which is what `PLAN.md` line 5 calls a rule without a source.

  Name both.
- **APR-21.** Spikes appear only as a source (line 43) and in the rule on code (line 137). The founder's decision has architecture grow "with spikes for the questions the model raises" (`founder-decisions.tsv` line 27). Say who decides a spike, from which budget, and that its result is cited, as EXP, in the record it serves.

---

## What I ran

All from `/home/user/sharrwah-knowledge-map`, with `python3 -I`, reading only.

**The repository:** `git log` and `git show --stat` on `d9524f74` and `27ba96d2`, and `git diff --stat d9524f74 843d118a`.

**The merged model,** by inline scripts over `studies/class-model/merged/`:
- `interfaces.tsv`, by grade, by placement and by the kind of key (concern-map statement, held-pass entry, subject's statement). Then per capability, and per held cell for its own platform's rows.
- `qualities.tsv`, by platform, by capability, and by a pattern on the label: prices, fees, rates and trials; certification, uptime and data location.
- `slot-fillers.tsv`, by the kind of key.
- `cells.tsv`'s `held`, `scopes` and `own_scopes`; `kinds.tsv`'s `kind` and `class_scope`.
- `capabilities.tsv`'s areas, against `seed/km-areas.tsv`.
- The held pass's `boundary` structures in `held/selection.tsv`, against the entries the cells cite.

**Three scratchpad scripts,** which import the repository's own `class_slice.py` and `source_kinds.py` as modules:
- `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/review/scopes.py`: the scope of each slot filler's statement, by `class_slice.citable`;
- `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/review/bkinds.py`: the held pass's `boundary` entries in `interfaces.tsv`, by structure and kind;
- `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/review/qkinds.py`: the quality rows, by the kind of their held entry's structure.

**`method/source_kinds.py`,** on held files of:
- observed-sh's `admin-router`, `admin-webhook-topics`, `admin-graphql-schema`, `admin-main-nav`, `dev-dashboard-scopes`, `admin-role-permissions`, `billing-plans`, `admin-betas` and `cli-webhook-topics`;
- observed-sa's `dashboard-webhook-events`, `docs-event-lists` and `docs-sidebar`.

**Greps:**
- the concern map's `citations.tsv`, for app listings, forums and archives, and WooCommerce's statements on its Marketplace, against `merged/evidence.tsv` and `merged/slot-fillers.tsv`;
- observed-sh's and observed-sa's `structures/REGISTER.tsv`, for the app and theme stores;
- `reports/GM-rulings.md`, for the architecture plan.

**The quotes:** `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/review/quotes.py` checks 86 of this review's quotes against the file and line each names. Three line numbers were wrong, and are corrected above (`PLAN.md` lines 42, 43 and 222). `method/check_report.py` doesn't apply: it needs pinned links, and this review cites files by line.

## What I didn't check

- **The books.** Every account of them here is a reading.
- **The kinds of the concern map's own `boundary` statements.** APR-5 rests on the held pass's structures, read at the structure's level.
- **The pattern counts** (prices, countries) are readings of a pattern, not a classification of each row.
- **The merge itself.** I didn't run `class_merge.py`: the merged files are read as committed at `d9524f74`.
- **What I read only in part.** `STATE.md` only where cited. `reports/GM-rulings.md` only for what it says of the plan (lines 1 to 25).
- **What I didn't read.** The Knowledge Map's rebuilt page, the orientation page, and architecture records (none exist).
- **No architecture is proposed here.** The plain-words entries in APR-1 state what the plan already decides; their risks and alternatives are readings.
- **Some fixes propose a rule of the reviewer's own,** for the coordinator to rule on: the grouping order in APR-9, the grain and the worth test in APR-10, the second rating in APR-11, the first report in APR-8, and the sort of the two schemes in APR-5.
