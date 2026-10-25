# Why the method didn't catch what you caught

**25 October 2026.** You asked for this before answering Decision 1. It takes each of your feedback points in turn, says why the gaps escaped, and tests the evidence-completeness pass you proposed on Decision 1 itself. It ends with the smallest addition that fixes what is missing, as amendment 4. Nothing in the method changes unless you approve it.

Part two, `reports/M1-plan-changes.md`, compares the plan's two changes, as you asked afterwards. An independent agent then tried to refute both parts. I checked each of its 29 fixes against the evidence and applied them (`decisions/checks/M1-method-assessment-check.tsv`, with my dispositions in `decisions/checks/M1-method-assessment-dispositions.md`).

## In short

- **Most of what you caught had been caught before, and the fix was then dropped.**
  - A written rule on claims of absence existed from 12 October (`2842819:PLAN.md`:93, :196). With it in place, the pilot still recorded things as "not stated" that held articles stated, and "The founder found it". On 13 October the fix came: an audit of every claim of absence by an agent that made none of them, with a recorded search (`a920665`).
  - The audit then settled 60 claims, of which 10 were wrong in whole or in part (`studies/subjects/S-01/method-report.md`:22–29). The pilot's report of 17 October listed it under "Keep what worked" (:193).
  - The method adopted on 24 October doesn't mention absence at all. The same failure came back that night, in Salla's "under review", and again you found it.
- **A map close to the one you propose exists.**
  - The first plan's Q1 built it on 10 and 11 October from Shopify's and Salla's own lists: webhook topics, extension points, permissions, Help Center sections, API resources, navigation, settings, billing categories and more.
  - It holds 2,610 and 2,627 list entries, grouped into 350 concerns with 5,565 statements, every quote found. From 12 October it was "the index for `PLAN.md`'s subjects" (`studies/concern-map/README.md`:5, :13–14).
  - It is frozen, still waits for your review (:9), and has its own gaps: 249 for Shopify, 230 for Salla.
  - The method mentions neither it nor the Shopify payments study of 10 October. My plan of 24 October counted its concerns as one of "five overlapping question sets" to merge (`founder-messages/2026-10-24-approved-plan.md`:60–66). *Interpretation:* it is an evidence map, and filing it as questions cost it its role.
- **One gap is genuine: no check looks at what a record never mentions.**
  - Checks cover "only the facts a decision rests on" (`METHOD.md`:204), and investigation stops "on risk, not on completeness" (:239).
  - Checkers are asked for "missing evidence" (:221), but only for the claims a record makes.
  - The register names two risks of missing something: W-08 (earlier work lost) and W-15 (a word's extent unknown). Both mitigations work from what a record cites.
- **The rule I wrote from your concern of 24 October narrowed it.**
  - I framed the concern, and you approved the framing: a record "can narrow an area it never examined" (amendment 2's reason, `METHOD.md`:336).
  - The rule I wrote from it checks a term's extent only "against the paths it cites" (:212). So what a record never cites stayed unchecked.
- **Your fear that the plan changes shadowed earlier work holds, with one correction.**
  - Four earlier bodies of work are referenced by neither the method nor any current record.
  - Their content wasn't lost. Between them, the pilot, the concern map and the Shopify study already held every fact the trial below surfaced. It wasn't used.
- **The fix is small.** Amendment 4 restores the safeguards that were dropped, and makes the method's own changes traceable. It adds one script run and one input to an existing check.

## Your feedback points

| # | Your point, as framed | Verdict | Root cause | Where it lands |
| --- | --- | --- | --- | --- |
| 1 | Yemen must not shape hard-to-change design: a very visible guard (24 Oct) | Genuine; handled | The guard of 10 October was lost with PR #3 and left out of the method's first draft | Section 3a and its script |
| 2 | A reliable method: fix root causes with established practice, not new layers (24 Oct) | Genuine; handled in the design, not in the method's own changes | The method was changed without tracing which safeguards it retired | 4c |
| 3 | You fear something is wrong without your knowing (24 Oct) | Genuine; partly handled | The reports show conclusions, not what went unexamined | 4b gives each record a coverage line |
| 4 | A record can narrow an area it never examined (22:04) | Genuine; half handled | The rule checks a term only against the paths a record cites (`METHOD.md`:212) | Terms (done); 4b (coverage) |
| 5 | An evidence standard: claims traced, agents challenging, gaps visible (23:01) | Genuine; handled for claims, not for absences | The absence audit was dropped | 4a, in section 6 |
| 6 | Don't accept at M1 what M2 will supersede (23:01) | Handled, and it works | It held D-002 and D-003 back | Section 6. 4b also completes each record's "Leaves open": D-001 lacked apps (S-06) |
| 7 | The evidence is well indexed, if we know how and when to look (23:01) | Genuine, and accurate | The index-first rule covers the evidence repositories, not this repository's own earlier studies | 4b, and W-08's map finished (4c) |
| 8 | "Are you sure?", on Salla's "under review" (25 Oct) | A real error | A claim of absence with no audit (point 5) | 4a |
| 9 | When an older decision meets focused evidence, establish its reason and surface the conflict (25 Oct) | Handled by practice; carried out late | I applied the guard's words before putting both readings to you | Sections 3 and 10 already say a founder decision changes only by you. No new rule |
| 10 | Not a copy of Salla: examine Shopify, and where they differ, don't default to the stricter way (25 Oct) | Genuine; handled in principle | Choice 2 weighed the deduction variant, with two precedents, and closed it with "never" instead of reserving it. The first plan's rule to keep the general variant had been dropped on 18 October (part two) | 4d |
| 11 | Observed is not complete: the repositories list their own gaps, and "only" is a claim of absence (today) | Genuine | As point 5. M1's records and glossary make 16 claims of absence: 6 about named documents, 10 about the held evidence as a whole. Of those 10, 5 point to searches the inventory recorded, and none names the repositories' gaps (`decisions/checks/M1-absence-claims.tsv`, my reading) | 4a |
| 12 | A completeness pass before decisions (today) | Partly: the map exists; using it is what's missing | Points 4 and 7 | 4b, not a new pass |
| 13 | The plan changes may be shadowing better earlier work (today) | Genuine in part | My consolidations at each plan change; W-08's map in section 13 left four bodies of work out | 4c |

None of your points is a plain misunderstanding. The nearest is point 12: you couldn't have known the map existed, because the method never mentions it.

## Why they escaped

1. **Safeguards were lost each time the method changed (an execution failure).**
   - With PR #3: the market guard, and your decisions F-00 to F-06, restored at M0.
   - At the plan's second change, on 18 October: the variability analysis with its rule to keep the general variant, and the sweep of the inventory's concerns, coarsened to areas (part two).
   - At the third, on 24 October: the absence audit, and the concern map as the subject index.
   - Section 13 of the method listed the founder decisions it changed and two practices it stopped (`METHOD.md`:409–416). It didn't list the absence audit, the concern map, the sweep or the generality rule, and it set none of them against the risk it had controlled.
   - W-08 named the risk of losing earlier work. Its mitigation, the map in section 13, left four bodies of work out.
2. **No check looks at what a record never mentions (a missing safeguard).**
   - IBM's classification of defects separates something missing from something incorrect or extraneous (Orthogonal Defect Classification).
   - M1's checks found the incorrect and the extraneous well: the glossary's narrowing, the posting key, the reversal-twin count, the Tabby quote, and the paragraph that broadened D-002.
   - They found the missing only when a checker happened to search past the text, as with D-002's nine items and Shopify's PayPal case. You found the rest.
3. **The rule I wrote from your concern narrowed it (an execution failure).** Point 4 above.
4. **The author frames the checks.** I write each checker's brief around the claims of a record I also wrote (W-19). Since amendment 3 the checkers try to refute, but they refute what is written.

## Why you still feel responsible

Because, today, you are the method's only check on what isn't there.
- In two days your questions found two real errors, the "under review" claim and the "never" in choice 2. They also changed how a third issue reached you: the reading of B, which became choice 1.
- The pilot's report records the first error of this kind the same way: "The founder found it."
- The feeling reads the record accurately. It is not a misunderstanding.

Two expectations would be mistaken:
- **That observed means complete.** You already say it doesn't, and the repositories list what they don't hold.
  - Every Shopify store captured has a Yemen address, so features tied to a region, payments and markets among them, weren't exercised in the admin (observed-sh `docs/GAPS.md`:28). The Help Center pages that describe them are held: 2,587 of 2,592 English pages (`index/ledger/sitemap--help-shopify-sitemaps.tsv`).
  - Salla's repository holds no paid purchase by card, Tabby or Tamara, and no shipping label. Nor does it hold "the merchant's review of a bank transfer", the ground the "under review" claim stood on (observed-sa `docs/GAPS.md`:11, :16).

  A claim of absence is bounded by such gaps.
- **That a method can make your review unnecessary.** Your review of intent stays: whether a framing says what you meant, and which risk you accept. Your review of whether the evidence was complete should not be needed.

## The completeness pass you proposed

**What already exists:**
- **For capture:** the repositories' denominators (sitemaps, route manifests), their ledgers (599,589 rows for Shopify) and their gap lists.
- **For concerns:** Q1, linked to the 34 areas through R1's platform areas (`studies/proposals/areas/areas-*.tsv`).
- **For the money subject:** the pilot's statements, absences and audits for S-01, and the Shopify payments study, eight reading passes over Shopify's payments, finance and billing (`shopify-payments-study/`).

**What is missing** is using them. A record never asks which entries of its areas it didn't use. A claim of absence never asks what the repository says it doesn't hold.

**A trial on Decision 1,** by script (`method/slice_coverage.py`; output `decisions/checks/M1-slice-coverage-D001.tsv`, re-run identically by the checker):
- **The areas Decision 1's question reaches,** as I chose them for the trial: A-03, A-11, A-12 and A-13. Its subject was assigned only A-12 and A-13. Together they hold 66 concerns and 931 statements. At the version you were sent (`d03af1b`):
  - 35 concerns have a source cited by the records or their checks;
  - 29 more are cited by the pilot that Decision 1 rests on;
  - 2 are cited by neither: Shop Cash, and complaints about financial products. Neither bears on who holds money.
- **The 31 the records don't cite.** Their titles pointed to 6 that bear on choice 2. Their statements show:
  - **Shopify's two ways for fees,** which your question surfaced: a separate bill for its own charges, and deductions from its own payment service's payouts. The pilot had recorded the same variation (S01-VP-19), and its Decision 9 tied it to who holds the money. So did the Shopify study (`shopify-payments-study/E-pos-finance-billing.md`:29, :31).
  - **Partners' cases the records lacked,** beyond the lender's repayment choice 2 already cited:
    - apps' charges on Shopify's bill (`app-charges.md`:1, :5), already in the Shopify study (:32);
    - Salla's financing, collected from the net Mada and credit card sales of each payment (`STR:payments.json`), already in the pilot (S01-SA-130, S01-SA-131);
    - Salla's apps taking amounts from the seller's wallet:
      - dropshipping apps' settlements (`SAPI:64`);
      - shipping waybill amounts, held "from your electronic payments balance" and paid to the carrier (`STR:apps.json`; concern SA-C-145, in A-10).
- **The areas Decision 1 leaves to others** (A-10, A-21, A-22) hold 42 concerns.
  - 6 are cited by neither the records nor the pilot, and none of those bears on who holds the money.
  - I didn't triage the 34 the pilot cites. One of them, Salla's shipping apps (SA-C-145), bears on choice 2.
  - After the check I ran apps (A-24) too: 8 concerns, none cited by the records and 7 by the pilot, none adding to the above.
- **Result:**
  - Nothing changes the line or the three choices. Choice 2 now carries the partners' cases, and apps (S-06) join what Decision 1 leaves open.
  - Everything the trial surfaced was already held in this repository. It hadn't been used.
  - The script runs in seconds. By my account the whole trial took about an hour, most of it writing the script once.

**The practice behind it:**
- **Systematic mapping** (Petersen et al. 2008) builds a classification of a field before reviewing questions within it. Q1 is one. `PLAN.md` cited domain analysis of existing systems (FODA) for it (`PLAN.md`:441).
- **Search evaluation against a known set** (Zhang, Babar and Tell 2011) judges a search by how much of a known collection it finds. The concern map is that collection for each slice, and only as complete as itself.
- **Traceability in both directions** (ISO/IEC/IEEE 24765's definition).
  - The method traces each decision to its evidence.
  - It doesn't trace the evidence back to the decisions. That direction is the one that shows what was never used.

**Better than making claims, then checking them?** Neither replaces the other. Checking claims finds what is wrong; mapping finds what is missing. The trial shows the second is cheap where the map exists, so it belongs inside the checks, not as a pass before every question.

**Its limits:**
- **It works at the level of a concern.** It can't see a miss inside a concern the record already cites: the "under review" error sat inside settings the records cited. Rule 4a catches that kind.
- **The map is frozen at commits of 9 to 11 October.** Some structures are not among its lists, such as Salla's help-center tree and its dashboard translations, though its statements cite the translations. M2's capability map is where it is brought up to date.
- **Choosing the slice and triaging it are judgment.** In this trial I did both, and left an area out. Under 4b the checker does both.

## Earlier work the plan changes shadowed

| Work | Cited by the method or a current record | What it holds | Disposition |
| --- | --- | --- | --- |
| Q1's concern map (`studies/concern-map/`), 10–11 October | No | Choice 2's evidence, and Salla's apps' wallet deductions | The subject index again (4b) |
| The Shopify payments study (`shopify-payments-study/`), 10 October | No | Shopify's bills against its payout deductions, and apps' charges on Shopify's bill (`E-pos-finance-billing.md`:29–32). Also the false "Every type has a reversal twin" (:189). That claim reached D-003 through the seam's notes (`9831536:studies/payment-seam/notes/shopify-crossings.md`:141), on a reviewer's advice (`decisions/checks/D-002-D-003-review.md`:67), and M1's inventory corrected it | Candidate evidence, checked when relied on, like the drafts |
| Yemen setup options (`yemen-setup-options/`), 10 October | No | "Seventeen setup options across five positions" (`report.md`:92), built on Yemen's facts. That makes the first market the design driver, which the market guard now rules out. Stage 1 redid its facts, with checks | Context. Its positions are candidate options for S-07 |
| The obligation-to-payout model (`model/`), 10 October | No, except through the payment seam, which D-002 cites | The model behind the seam | Kept, as the seam's source |

**Your remarks didn't hide this work, and nothing you asked for required dropping it.** On 24 October you asked planning to "understand the current state and the leverage already available" (`founder-messages/2026-10-24-method-accepted.md`:19). My consolidations hid it. I proposed each one, merging the question sets was my own finding, and none listed what it dropped. *(Interpretation: earlier work is often broader and less checked, and later work narrower and better checked. That is why each needs a disposition, not a verdict.)*

## Amendment 4, proposed

It restores the safeguards that were dropped, and makes the method's own changes traceable. Part two gives the evidence for 4c and 4d.
- **4a. Claims of absence** (section 6).
  - A claim that something isn't there ("only", "none", "doesn't show", "not found") is a fact only when it names:
    - its searches: `method/corpus_search.py`, whose header lists what it covers, plus the structures that bear on the claim, found through the repositories' indexes;
    - the repositories' gaps that bound it (`docs/GAPS.md`, the ledgers).

    Otherwise it is written as an interpretation.
  - The checker audits each claim of absence in records at levels 2 and 3, and in the glossary entries they use. This restores the audit of 13 October; the written rule alone, from 12 October, didn't stop the pilot's error.
  - *Fits the method:* the search is targeted to the claim, so "nothing is read broadly" still holds.
- **4b. The omission check** (sections 5 to 7).
  - At verification, the checker names the areas the record reaches, from its question and its Terms.
  - It then receives from `method/slice_coverage.py` the concerns in those areas that the record doesn't cite, and says which bear on a claim or on an item the record leaves open. The coordinator records each disposition.
  - Section 6's sentence becomes: "It covers only the facts a decision rests on, and the concerns of its slice that the record doesn't cite, never everything a document mentions."
  - Section 7's rule 3 gains: "The omission check of section 6 is bounded by the record's slice."
  - It adds one script run and one input to an existing check. In the trial, the run took seconds and the triage minutes.
- **4c. The method's own changes,** checked by function (sections 12 and 13). It widens two things the method already has:
  - **amendment 1's check of what version 1 dropped of your decisions,** applied to the method's own practices. Each amendment names, for each practice it retires, the risk that practice controlled, and either reassigns the risk or records it as accepted;
  - **W-08's map, finished.** Section 13 gives every body of earlier work a disposition, as M0 did for the Knowledge Map.
- **4d. Variants** (section 5, step 3).
  - Where the references differ, or one reference carries more than one variant at once, each variant becomes an option, with how it is bound: together, or one per market, store or plan.
  - When one is a restricted form of another that the general one can reach by configuration, the general one is kept, and the restricted one is bound where needed.
  - These are the first plan's coexistence step and generality rule (Czarnecki, Helsen and Eisenecker 2005). The second change dropped both.
  - Section 2 ties variability to markets; 4d extends it to the references' variants.
  - Choices 2 and 3 follow it since the revision of 25 October. The version sent to you said "never".

**Not proposed:**
- a new mapping pass before each decision: Q1 is the map, and M2 refreshes it;
- a rule on older and newer founder decisions: sections 3 and 10 cover it;
- the first plan's cause labels and per-subject variation points, whose cost was measured;
- more rounds of checks.

**The risks behind it.** W-20 (omissions) is open. The risk of safeguards lost when the method changes is W-08's, whose mitigation failed. W-08 is updated rather than a new risk added.

## What this means for Decision 1

- **Nothing found changes the line or its three choices.**
- **Choice 2 now carries the partners' cases, corrected after the check,** and apps (S-06) join what Decision 1 leaves open. Its page is about 1,700 words.
- **You can answer now.** If you approve amendment 4, it applies to every record put for acceptance from then on, D-001 included. Its claims of absence would get their searches and bounds written in. Most of them are about named documents or the first market's records, and already listed under Gaps.

**Answers:**
- **Amendment 4:** approve / approve with changes: … / not now
- **Decision 1:** as on its page

## Sources

**Inside this repository** (paths as cited above):
- the pilot's method report: `studies/subjects/S-01/method-report.md`;
- Q1: `studies/concern-map/README.md`;
- the plan of 24 October: `founder-messages/2026-10-24-approved-plan.md`;
- the trial: `method/slice_coverage.py` and its output;
- the check of this assessment: `decisions/checks/M1-method-assessment-check.tsv`.

**Practice:**
- Petersen, K., Feldt, R., Mujtaba, S. and Mattsson, M. (2008). [Systematic Mapping Studies in Software Engineering](https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf). EASE 2008.
- Zhang, H., Babar, M. A. and Tell, P. (2011). [Identifying relevant studies in software engineering](https://eprints.lancs.ac.uk/id/eprint/65750). *Information and Software Technology* 53(6), 625–637.
- Chillarege, R. et al. (1992). [Orthogonal Defect Classification](https://www.chillarege.com/node/23). *IEEE Transactions on Software Engineering* 18(11). Its qualifiers, missing, incorrect and extraneous, are as a secondary source gives them; the full paper was not read.
- Bidirectional traceability, as ISO/IEC/IEEE 24765 defines it, quoted in [NASA's Software Engineering Handbook](https://swehb.nasa.gov/x/TYCZD). The standard itself was not read.
- Kang, K. et al. (1990). *Feature-Oriented Domain Analysis (FODA) Feasibility Study.* CMU/SEI-90-TR-21, as `PLAN.md` cites it.
