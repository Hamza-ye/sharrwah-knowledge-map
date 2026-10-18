# Check of the re-frame's drafts (step R0)

**18 October 2026.** An independent check, by an agent that drafted none of what it checks, working from `studies/proposals/briefs/R0-check-of-the-draft.md`. The drafts are at commit `178d313`. They are unchanged at `675a660`, which changes only `STATE.md`.

**What I read:**
- the brief;
- the founder's G1 answer, and the G1 rows of `founder-decisions.tsv`, with the G0 row on Q3's rows;
- the drafts: `plan-change.md`, `questions.md`, the two R1 briefs, `sizing.md`, `method/areas_extract.py`, `method/check_areas.py`, and the five extracts;
- `PLAN.md`;
- recorded data, sampled:
  - the concern map's `inventory.tsv`, `concerns.tsv`, `statements.tsv` and `citations.tsv` on all five platforms;
  - the pilot's `method-report.md`, `entry.md`, its `briefs/C-analysis.md` (for phase C's input) and its per-platform `statements.tsv`, `citations.tsv` and `absence-audit.tsv`;
  - Stage 1's `axes.tsv`, `review-independent.md` and `review-axes.md`;
  - the held sources the extracts cite, read with `git show` at the commits the extracts give: observed-sh's Help Center outline at `c8b5fbee` and observed-sa's help tree at `4ca2e896`.

**What I did not read:** `STATE.md`, Q1's rules, the pilot's A brief, and the session transcripts. The transcripts aren't available to me, so figures that rest only on them are checked for their arithmetic and against section 12 of the method report, not at their source.

**How.** I used scripts of my own, kept in my scratch directory outside the repository and run with `python3 -I`. They:
- re-ran the extract script;
- tested the checker on 31 small areas files;
- counted the volumes.

Nothing ran from inside `evidence/` or the observed repositories, and no file but this one was changed.

**In short:** 40 findings, 19 of them must fix. The verdict is at the end.

---

## Findings

### The plan change against the founder's message

I went through sections A and C and Part 2 sentence by sentence. Each instruction is carried somewhere in the plan change, except where findings 1 to 16 say otherwise. Here is what the change does to each part of `PLAN.md`. Each row whose fate is unclear is a finding below.

| Part of `PLAN.md` | What the plan change does | Says so? |
| --- | --- | --- |
| Status line and opening paragraph | Kept. They still say "agreed ... (gate G0)" and "safe shore" | No (15) |
| §1, aim and safe shore | Replaced by "The aim and the end". Safe shore condition 5 is kept | Yes |
| §1, "Before building, the decisions that would be expensive to change later have to be made on evidence ..." | Dropped. The principles are kept | No (16) |
| §1, "a thin slice for Yemen, with each variation point behind its own module" | Dropped ("the first build's design starts under its own plan") | No (16) |
| §2, Q1's "done" changes; the test form is the main instrument | Dropped (no subjects; questions don't take the test form) | Yes, in effect |
| §2, Q2 splits | Stage 1 reused; phase D's marks stopped | Yes |
| §2, Q3 at close-out | Proposed for dropping | Yes |
| §2, the 84 unclear matches retired, and the 88 matches kept "only as hints for scoping" | Not said | No (16) |
| §2, gaps closed only where a subject needs them | Replaced by "new reading where needed". The route check is kept | Yes |
| §3, who does what | Amended, text given in full. Drops "Nothing reaches the founder without a decision attached", and the purpose of the brief check ("for anything that presupposes the answer") | No (16) |
| §4, Stages 0, 1 and 2 | Kept as a record. Stage 0's freeze ends | Yes |
| §4, Stage 3 | Replaced by R1 and G2. Its seven Q1 concerns, which were candidates, go too | Partly (7) |
| §4, Stage 4 | Replaced by R2 to R6 and the proposals gate. "The founder's decisions go in `founder-decisions.tsv`" isn't carried | Partly (16) |
| §4, Stage 5's interactions | Not said | **No (1)** |
| §4, Stage 5's Q3 | Dropped, or reconciled after R6 if the founder prefers | Yes |
| §4, Stage 5's last sweep | Not said | **No (1)** |
| §4, Stage 5's G4 | Replaced by the proposals gate | Yes |
| §5, gates, when the founder is needed, and the decision item | Replaced or rewritten | Yes |
| §5, defer | Rewritten as "binds nothing", and made general | Yes, but made general (10) |
| §5, standing decisions and spending | "Stay as they were", with no text given | Yes (15) |
| §6, the test form | Dropped, except for kinds of source and absence. Part 1 names only step 3 and the step 5 rows that use it | Partly (15) |
| §6, matching | Rewritten, and basis 4 changed | **No (4)** |
| §6, evidence | Kept | Yes |
| §6, Q3's rows | Proposed for dropping | Yes |
| §7, risks | Rows 1 and 2 changed, 15 to 17 added, 3 to 12 and 14 stand, 13 met. But rows 5 to 8 name removed things | Yes (15) |
| §8, stops | Three stops added; the others stand. Two of those name subjects | Yes (**3**) |
| §9 | Amended. "the subject" and "one subject or one batch" still stand | Yes (15) |
| §10 | Unchanged | Yes |

Each dated entry in `PLAN.md` section 11:

| Entry | Fate | Says so? |
| --- | --- | --- |
| 12 Oct: proposed; section 5's additions; G0 | Kept as a record | Yes |
| 12 Oct: method fixes from inspecting the pilot's briefs | The test-form fixes lapse. Kinds of source by rule are kept. The E-rows mapping and the time-bomb types go with Q3's rows | Only kinds of source (§6) |
| 12 Oct: Q3 moves to close-out | Superseded by the proposal to drop the rows | In effect (§6) |
| 12 Oct: Stage 1's method, and pass 2's rules | Kept as a record. But pass 2's rules still govern how any Yemen fact is read: states are alternatives, a place is the scope its source gives, only an all-Yemen state supersedes others, and a proposed state is never today | **No (2)** |
| 13 Oct: agents' effort by step | Names only the old steps, and its "re-run at `high`" rule has a cost | **No (2)** |
| 13 Oct: claims of absence (A3, the corpus search, the checker) | Replaced by R5's search and audit. The corpus search is kept for reading | Partly |
| 17 Oct: Stage 1's axes review | Kept as a record | Yes |
| 17 Oct: phase C, same party; "names a law" | Same party is kept (§6). "Names a law" lapses with causes | Partly |
| 17 Oct: phase D, the Q2 frame | Phase D stops. Whether the Yemen part of each proposal keeps the frame isn't said | **No (2)** |
| 17 Oct: Stage 1, `within` and the faithfulness pass | Replaced, with the risk each addressed | Yes |
| 17 Oct: the pilot's review, the role test and "no part" | "No part" is kept (§6). The role test isn't mentioned | **No (2, 4)** |
| 17 Oct: phase C's third run, "no part" and several letters | "No part" is kept. Several letters lapse | Partly |
| 17 Oct: the flow ends at the payout to the merchant's bank, and when a wallet is in the flow | Bears on question 5's last sentence and Decisions 1 to 14. Not said | **No (2)** |

#### 1. Stage 5's interaction check and its last sweep have no stated fate

- **Where:** `plan-change.md`, Part 1, "Replaced", and section 4, "(Stages 3 to 5 replaced)".
- **The problem:** the change says what happens to Stage 5's Q3 and G4, but not to its other two parts. The proposals will bind into each other, and nothing checks whether the bindings conflict. For example: which payment methods each place has (Q5), the store's currency (Q7), the payout currency (Q5 and Decision 14), what must be met before taking payment (Q3), and the guard.
- **The evidence:**
  - The founder asks the summary to say "what happens to every part of the plan this message doesn't mention, including the close-out"; Part 2 says "the close-out is Stage 5".
  - `PLAN.md` Stage 5: "**Interactions.** Subjects that touch each other, such as currency, payments and tax, are checked for bindings that conflict (Calder et al. 2003)", and "**A last sweep** of the inventory's remaining concerns, for anything expensive to change that the subject list missed".
  - Neither the plan change nor the sizing mentions interactions or a sweep.
- **The fix:**
  - Add an interaction check across the drafted proposals, as a named part of R6's review brief or a short step of its own. Name the pairs to check, and size it at about 20 to 40 million.
  - Or drop the check, and give the reason.
  - Say that the last sweep is replaced by the areas list (R1) and "the rest gets a line each", if that is the intent.
- **Severity:** must fix.

#### 2. The plan change doesn't say which method rulings still bind

- **Where:** `plan-change.md`, Part 2, introduction: "Sections 10 and 11's earlier entries are unchanged".
- **The problem:** the founder's summary must list "the method rulings that still shape the result". The change keeps section 11 as a record, but doesn't say which of its rulings still govern the new steps. See the table above. In particular:
  - **Effort.** The 13 October effort ruling names only the old steps (A, A2, B, C, D, F, and Stage 1's 2a and 2b). No R step has an effort level. Its rule "A part whose check or review shows gaps is re-run at `high`" adds cost the sizing doesn't count.
  - **Where money goes.** The 17 October ruling that "the subject's flow ends at the payout to the merchant's own bank account", and when a wallet is in the flow, defines the ground of question 5's last sentence.
  - **Yemen.** Stage 1's pass-2 rules, and phase D's Q2 frame ("the merchant sells in the Yemeni market"), decide how R4 reads Yemen's evidence.
  - **Comparing.** The role test (17 October) governs what counts as answering the same thing (finding 4).
- **The evidence:** the founder's summary requirement, and the dated entries named in the table above.
- **The fix:** add to the section 11 entry a short list:
  - the rulings that still bind, each with the step it governs;
  - the rulings that lapse with the test form or the subjects;
  - each R step's effort level.

  That is the list the founder's summary needs.
- **Severity:** must fix.

#### 3. Two of the stops that "stand as they were" name subjects

- **Where:** `plan-change.md` section 8: "The other stops stand as they were."
- **The problem:** two of `PLAN.md` section 8's stops can no longer fire as written, because the change removes subjects. The founder said: "The plan's existing stops still apply".
- **The evidence:** `PLAN.md` section 8:
  - "A founder decision blocks the next subject";
  - "New evidence changes more than one finished subject";
  - and "A stage overruns its expected size twice", which is about stages, while the new work runs in steps.
- **The fix:** re-word them:
  - "a decision that is genuinely the founder's blocks the next step or a proposal";
  - "new evidence changes more than one finished proposal or recorded question";
  - "a step overruns its expected cost": the budget's first-overrun stop now comes before the old "twice".
- **Severity:** must fix.

#### 4. Matching basis 4 now reads "answering the same question", which the founder agreed differently at G0

- **Where:** `plan-change.md` section 6, "Comparing platforms".
- **The problem:** the four matching bases were agreed at G0. The change rewrites basis 4 without saying so. A section B question is broad, so two different things both "answer" it. For example, Salla's bank transfer and Shopify Payments both answer question 5. Under the new wording, they would count as the same concept.
- **The evidence:**
  - `PLAN.md` section 6 (agreed at G0): "4. both answer the same variation point."
  - Plan change: "two concepts are the same only on a shared term, identifier or definition, or by answering the same question".
  - The method report, section 11: "Rules that let a judgment rest on meaning drift". The 17 October role test tied basis 4 to "what a statement's own words name in the variation point's role".
- **The fix:** keep basis 4 at the level of one role: "both fill the same role in what the question asks, by their own words". Say that the 17 October role test still holds. Or drop basis 4. Mark the rule as the coordinator's own.
- **Severity:** must fix.

#### 5. The company decisions reach the founder without an independent review

- **Where:** `plan-change.md`, step R4, "Company decisions", and step R6.
- **The problem:** the coordinator collects the company decisions and writes their recommendations. R6's review covers only the proposals, and the company decisions "come with them". The founder kept "one independent review of each result before it reaches me".
- **The evidence:**
  - R6: "An agent that did none of the work reviews the proposals, in two batches. ... The company decisions come with them."
  - The pilot's lesson: "The coordinator's own work needs the agents' checks" (method report, section 11). Seven of the review's 14 must-fix findings were the coordinator's.
- **The fix:** R6's review covers the company decisions too, and each fact one rests on gets R5's checks. Add about 20 million to the sizing.
- **Severity:** must fix.

#### 6. No rule says which recorded statements "bear on" a question, though a script is to copy them

- **Where:** `plan-change.md` section 2 ("A script copies a recorded statement unchanged, with its citation, wherever a question needs it") and step R3 ("it copies the recorded statements that bear on the question").
- **The problem:** which statements bear on a question is a judgment, not something a script can work out by itself.
  - No brief, check or cost covers making that judgment.
  - If the coordinator makes it, the coordinator decides what every recording run starts from.
  - R1 already needs it: the founder wants to be told "what evidence the section B proposals keep" when an area is marked "won't do".
- **The evidence:** my rough count (finding 36) maps concerns to questions by their names and terms. Between 148 (Q4) and 1,439 (Q5) recorded statements bear on each question, and 3,617 of the 8,191 bear on at least one.
- **The fix:**
  - Define the selection as a rule a script can apply. For example: a table that maps concern ids to questions, or a recorded corpus-search query for each question.
  - Have it made from a checked brief, or by the coordinator and reviewed with the areas list.
  - Keep it in `records/<question>/selection.tsv`.
  - Size it: about 80 million, if agents make it.
- **Severity:** must fix.

#### 7. Depth "where a wrong guess would be expensive" has no home for the data model or partner contracts

- **Where:** `plan-change.md`, step R3, last bullet.
- **The problem:** the change repeats the founder's sentence, but applies depth only as a choice of which platforms to read in depth for each question.
  - No question asks how the platforms structure their data. Examples: Shopify's Market and Catalog objects, Salla's "Store Scopes", BigCommerce's channels and Multi-Storefront.
  - No question asks what the partner contracts behind payments and shipping say. An example is the agreements that platforms' terms incorporate.
  - Two of the seven concerns that `PLAN.md` Stage 3 took from Q1, "where data lives" and "partners, and what happens when one fails", now have no question. Both are recorded: SH-C-181, BC-C-082, ZD-C-041, SA-C-233, SA-C-235.
- **The evidence:** the founder: "Go deep where a wrong guess would be expensive to change after launch: money flows, legal structure, the data model, partner contracts. Give every section B item enough to propose from."
- **The fix:**
  - Say how depth reaches each of the four topics. For example, in-depth recording runs read the platform's own structure (its objects and the levels its settings are set at), and the contracts behind each provider, where they bear on the question.
  - Say what happens to the seven Q1 concerns.
  - Put the reading to the founder (reading 1).
- **Severity:** optional.

#### 8. "The rest gets a line each": the change doesn't say who writes the lines or when the founder sees them

- **Where:** `plan-change.md`, step R3, last bullet.
- **The problem:** the lines are part of what reaches the founder, but no step produces them.
- **The fix:** say that the coordinator writes them, either with the areas list (R1) or with the proposals (R6), and that they are reviewed with them.
- **Severity:** optional.

#### 9. What a "must do" mark changes isn't said

- **Where:** `plan-change.md`, step R1 and gate G2.
- **The problem:** the change says what a "won't do" mark removes, but not what a "must do" mark adds. An area the founder marks "must do" that no question covers might get no reading at all.
- **The evidence:** the founder: "I mark what Sharrwah won't do or must do. Anything unmarked stays in."
- **The fix:** say what follows from "must do": for example, the area gets reading and a proposal, or a decision item, even if no section B item asks for it. Size that, or state that "must do" only confirms the area stays in.
- **Severity:** optional (reading 6).

#### 10. "Defer binds nothing" is made general

- **Where:** `plan-change.md` section 5: "Defer is always allowed. A deferred item stays open and binds nothing, unless the founder says otherwise."
- **The problem:** Part 2 defines defer "here", for Decisions 1 to 14. The change applies it to every later item. That may be what the founder wants, but it is a reading, and it isn't marked as one.
- **The fix:** mark it as the coordinator's reading, for the founder's go, or limit it to Decisions 1 to 14.
- **Severity:** optional (reading 2).

#### 11. Decisions 1 to 14 all go to the money proposals; Decision 14 is about currency

- **Where:** `plan-change.md`, step R4 ("The money proposals (questions 4 and 5) take up the pilot's deferred Decisions 1 to 14"), and the note after question 5 in `questions.md`.
- **The problem:**
  - The entry's Decision 14 asks "In which currency should Sharrwah hold and pay out a merchant's funds". That is question 7's ground.
  - Question 5's added sentence asks only "Where the money from each method goes". No question asks about agency (Decision 5), deductions (6, 9), timing (8), funds at termination (10), refunds (11), a security interest (12) or installments (13). They can be framed only from the pilot's records.
  - The founder's B7 says "The rial's two editions are not part of the core". The pilot's recommendation on Decision 14 kept "the rial recorded apart by the area its funds are held in".
- **The evidence:** `entry.md`: "Decisions 13 (installments) and 14 (currency) don't follow from Decision 1".
- **The fix:**
  - Route Decision 14 to question 7's proposal.
  - Say that Decisions 5 to 13 are framed from the pilot's records, and what new reading, if any, question 5's runs do for them.
  - Note B7's line about the rial where Decision 14 is framed.
- **Severity:** optional (reading 7).

#### 12. Additions the change doesn't mark as the coordinator's own

- **Where:** across `plan-change.md`.
- **The problem:** these are additions the message doesn't ask for, and none is marked as the coordinator's own, as the pilot's briefs marked theirs:
  - the checker's six rules (section 3);
  - per-platform agent runs that group areas, marked "agent's own". The founder said "the coordinator groups further";
  - the sample fixed as "question 3 on Shopify";
  - "two questions per run" in drafting, and "two batches" in review;
  - section 5's form for a decision item;
  - section 6's kinds of source, kept as the pilot assigned them;
  - risks 15 to 17;
  - the reasons for dropping Q3's rows;
  - "Stage 1's other open items are done only if a proposal uses them".
- **The fix:** mark each as the coordinator's own, so the founder's summary lists them with the method rulings.
- **Severity:** optional.

#### 13. The case for dropping Q3's rows leaves out what the founder said at G0

- **Where:** `plan-change.md` section 6, "Q3's rows".
- **The problem:** the case answers the risk of the rows returning as requirements inside this work. It doesn't say what dropping them loses.
- **The evidence:** `founder-decisions.tsv`, G0: "They are agent-written and must not be taken as Sharrwah's requirements, though some may be genuine questions". The plan change: "Under this change, nothing reads them".
- **The fix:** add one line. If the rows are dropped, nothing shows whether a genuine question among the 260 rows goes unanswered. The reconciliation, at about 30 to 40 million, is what would show it.
- **Severity:** optional.

#### 14. The change doesn't say how new material is captured and pinned at a commit

- **Where:** `plan-change.md` section 2 ("New reading is allowed") and section 9's file list.
- **The problem:** the founder kept "verbatim quotes at a pinned commit". New reading means quoting pages nobody holds yet. The change doesn't say where those captures go, or that they are committed before they are cited. The pilot's citations of live pages were captured: "Cited web pages | 146, all captured".
- **The fix:** add the capture place and rule to section 9, and to the recording brief.
- **Severity:** optional.

#### 15. Standing text still names what the change removes, and some "full" sections aren't full

- **Where:** `PLAN.md`'s status line, opening paragraph, risks 5 to 8 and section 9; `plan-change.md` Part 1 and Part 2.
- **The problem:**
  - Risk 5 ("A cause resting on absence ... the cause is unknown") is about causes, which the change stops. Risk 6 ("A match on none of the four bases") refers to bases that are rewritten. Risk 7 ("The subjects whose citations changed") and risk 8 ("with a commit per subject") name subjects.
  - Section 9 still says "STATE.md says where the work is: the stage, the subject" and "Every unit ends with a commit, whether one subject or one batch".
  - The status line still says "agreed by the founder on 12 October 2026 (gate G0)".
  - Part 1 says sections 7 and 8 are "rewritten", but Part 2 gives only rows "changed or added" and "added to".
  - Part 2 says the sections are given "in full", but section 5 says "Standing decisions and spending stay as they were" without their text. So whoever applies the change must merge by hand, and could lose those paragraphs.
- **The fix:** re-word these lines, and give sections 5, 7, 8 and 9 as the full text they will have.
- **Severity:** optional.

#### 16. Other parts whose fate is unclear

- **Where:** see the table above.
- **The problem:** the change doesn't say what happens to:
  - the 88 matches ("stay only as hints for scoping") and the 84 retired unclear matches. Using them to merge the five areas lists would bring back the matching faults;
  - the concern map's `gaps.tsv`;
  - "The founder's decisions go in `founder-decisions.tsv`", which was in Stage 4;
  - section 3's "Nothing reaches the founder without a decision attached";
  - the first build as "a thin slice for Yemen";
  - Part 2's "Section B's items are not standing decisions under PLAN.md section 5. A proposal that answers one becomes a decision only when I accept it". This isn't carried.
- **The fix:** add one line for each.
- **Severity:** optional.

### The questions

For each question, I sampled the concern map's concerns and statements on at least two platforms. Finding 36 shows the volumes.

#### 17. Question 1 misses how the platform itself is set up for each place

- **Where:** `questions.md`, Q1.
- **The problem:** the question asks about a seller who "sells to, or operates from, more than one place". The founder's B1, "One platform, set up per market", is mostly about the platform being set up differently for sellers based in different places, and about the platform adding a place. A run given this question would record cross-border selling for one store. It would likely miss:
  - Shopify's contracting party by billing address (SH-C-002: "You are contracting with the Shopify Contracting Party ... based on the billing address of your Store");
  - Salla's "دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها" (SA-C-167, SA-S-0141: choose which country you register your store from, because that decides the government documents your store is set up under);
  - Salla's own expansion: "GCC expansion is the next priority ... where payment, shipping, legal, tax, or terminology needs differ" (SA-S-0004);
  - Zid's "حاليًا زد يخدم التجار المتواجدين في السعودية ودول الخليج فقط" (ZD-S-0742: Zid currently serves only merchants located in Saudi Arabia and the Gulf).

  These would fall to questions 2 and 6, so question 1's proposal would draft without them.
- **Neutral:** mostly.
  - It names "a market" among the ways a platform names a place. That is the founder's working word, and also the term Shopify ("Markets"), Salla ("Markets / الأسواق المتعددة") and Zid ("الأسواق") use. The questions' own rule says the questions "name no platform's term".
  - "where is it set and by whom, as the platform shows it" fixes no level.
- **Would it record the recorded material?** It would record Shopify Markets, its currencies and domains (SH-C-106 to 113) and Zid's "خاصية الأسواق" (ZD-C-034). It would miss the platform-level material above.
- **The fix:**
  - Add: "What does the platform set up differently for sellers based in different places, and what does it say about adding a place where it operates?"
  - Replace "a market" with "or however the platform names it".
- **Severity:** must fix.

#### 18. Question 2 leads toward "availability"

- **Where:** `questions.md`, Q2.
- **The problem:** the question asks how laws, sanctions and licences "show in what a seller can use or do there". That is the founder's expectation, "Rules land as availability", put into plain words. Other ways a rule can land come second, as "some other way". The founder asked the work to test B2, not to look for it.
- **Would it record the recorded material?** It would record what is offered or withheld by place:
  - BC-S-0143: "Initially, BigCommerce Payments is available only to US-based merchants";
  - SH-S-0298: "Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships ...".

  The places where a law lands as design are weaker under this framing:
  - Salla's and Zid's ZATCA e-invoicing integrations (SA-C-161, ZD-C-053);
  - Shopify's separate Canadian payments company (SH-C-067: "registered with the Bank of Canada ... under the Retail Payment Activities Act");
  - where data is stored by region (SH-S-0638: "New merchants in Europe ... have their store data ... stored at rest in Europe by default").
- **The fix:** ask for every way equally. "What does the platform offer, restrict, withhold, require or do differently because of a place's laws, sanctions or licensing, or because of its own choice of partners and providers? Record each: in what it offers, in its terms, in which company contracts, in how the product behaves, in where data is held, and the reasons it gives."
- **Severity:** must fix.

#### 19. Question 3's opening fixes the platform as the one who lets, and it sweeps in staff and app rules

- **Where:** `questions.md`, Q3.
- **The problem:**
  - "before the platform lets them" makes the platform the gatekeeper, though the question later asks "who sets it". Providers set requirements too. Zid Pay requires "متطلبات التفعيل حسب الكيان التجاري" (activation requirements by business entity) for approval "لدى بوابة الدفع" (with the payment gateway) (ZD-S-0528).
  - "record any such requirement the platform states" sweeps in material that bears on no section B item:
    - staff permissions (Shopify's list has 283 entries);
    - the access scopes apps need Shopify's approval for (SH-C-159, 77 statements, about app developers rather than sellers);
    - every plan-gated feature (162 Shopify and 206 Salla plan-table entries are in scope).
- **Covers its item:** yes. It would record SA-C-006 (توثيق المتجر, store verification), ZD-S-0775 (Nafath verification before Zid Pay) and SH-C-068 (KYC). It doesn't ask whether a requirement differs by place, plan, product or payment method, but scopes are recorded anyway.
- **The fix:** "What must a seller do, provide or meet before they can do particular things?" Add: "about the seller, not the seller's staff or apps".
- **Severity:** optional.

#### 20. Question 4 uses "conditions", and its definition hides the contrast its item needs

- **Where:** `questions.md`, Q4.
- **The problem:**
  - "What limits or conditions apply?" uses one of the founder's working words. It is used in its plain sense, not as a category, but the questions' own rule forbids it.
  - "with no money passing through the platform or a payment service it provides" excludes cash on delivery that the platform itself collects. Examples are Salla's COD through its shipping labels (SA-C-115) and Zid's: "تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر" (ZD-S-0636: Zid collects from end customers and transfers the dues to the merchant's wallet). B4's proposal needs that contrast.
- **Would it record the recorded material?** It would record SH-C-079 ("Orders that accept manual payments are marked as unpaid", SH-S-0386), WC-C-002 (bacs, cheque, cod), SA-C-116 and SA-C-117, and SH-S-0276 ("Transaction fees don't apply ... for manual payment methods").
- **The fix:** "What limits apply?" Add: "Record also where the platform, or a service it provides, collects such payments itself."
- **Severity:** optional.

#### 21. Question 5 presupposes that the platform decides, by criteria

- **Where:** `questions.md`, Q5.
- **The problem:** "What does the platform itself decide, by what criteria ... What can the seller choose?" builds the founder's B5 expectation ("Sharrwah chooses ..., by its own criteria") into the question. It names two setters in advance, though the question rules say "It fixes no level and no setter". Providers, apps, law and the buyer's location also decide. For example:
  - WooCommerce suggests providers per store country (WC-C-004, 286 statements);
  - Shopify approves payment apps (SH-C-076);
  - Salla's merchant sets payment restrictions (SA-C-121, "تعيين قيود الدفع").

  "Where the money from each method goes before it reaches the seller" also presumes that the money stops somewhere first.
- **The fix:** "Who decides which payment methods a seller can offer buyers, and on what basis, as the platform shows it? Record each party it names as deciding. Where does the money from each method go on its way to the seller, including directly to the seller?"
- **Severity:** must fix.

#### 22. Question 6 is neutral and covers its item; one phrase can be plainer

- **Where:** `questions.md`, Q6.
- **The problem:** "a place the platform doesn't fully support" assumes a platform supports places in degrees, and echoes Shopify's "Unsupported countries and regions". Otherwise the question would record the material:
  - SH-S-0304: "Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account";
  - WC-S-0512: "the relevant country is the one where your business is registered";
  - ZD-S-0742 and SA-C-167.
- **The fix:** "a place where the platform, or part of what it offers, isn't available".
- **Severity:** optional.

#### 23. Question 7 fixes the level as the store, and leads toward one store currency

- **Where:** `questions.md`, Q7.
- **The problem:** "In what currency or currencies does a store hold its prices" names the store as the level prices are held at. That is the founder's expectation ("one store currency"). The questions' own rule says a question "never says where something is set (a store, a market, an account, a plan)". The recorded data shows other levels:
  - Zid's markets each carry a currency: "عملة السوق: حدّد العملة التي سيتم اعتمادها لعرض أسعار المنتجات داخل هذا السوق" (ZD-S-0750: the market's currency, used to show product prices in that market);
  - Shopify's catalogs hold prices per market (SH-C-037);
  - Salla's settlement currency depends on the country of the bank account (SA-S-0135, SA-S-0139).

  The recorded data also holds WooCommerce's "WooCommerce only allows for one base currency per store" (WC-S-0874) and Shopify's store currency (SH-S-0361). So the question would record the store level fully and the other levels less surely.
- **The fix:** "In what currency or currencies are a seller's prices held, shown to buyers, paid in and paid out, and at what level does the platform set each?"
- **Severity:** must fix.

#### 24. Question 8 uses "parts", and several platforms' own terms

- **Where:** `questions.md`, Q8.
- **The problem:**
  - "How does the platform divide what it offers into parts", and "each part", "the parts", "parts added", use one of the founder's working words as the category. The questions' own rule lists "parts" as not to be used.
  - It also presupposes a modular platform, which is B8's expectation.
  - The examples "apps, extensions, channels or plans" are platform terms: "extensions" is WooCommerce's, "channels" is Shopify's and BigCommerce's.
  - It doesn't ask how a platform brings in new things in stages, which is B8's "built gradually". The recorded data shows stages: Salla's feature flags with `released`, `plans` and `countries` (SA-S-3011), Shopify's Rollouts (SH-C-112), and BigCommerce's "(beta)" and "(closed beta)" scopes.
- **The fix:** "How does the platform organize what it offers, in its own names? What does each piece depend on and share, how are pieces added or extended, and how does the platform introduce new ones (for example by plan, place or release stage)?"
- **Severity:** must fix.

#### 25. "A run records every statement ... that bears on the question" has no bound

- **Where:** `questions.md`, "How a run uses its question".
- **The problem:** a short run can't record "every statement in the platform's material". Questions 2 and 5 each have more than 1,000 recorded statements bearing on them before any new reading (finding 36).
- **The fix:** leave the bound to the recording brief, and say so here: for example, record what isn't among the copied statements, read in the order the brief gives, and stop at the brief's budget.
- **Severity:** optional.

### The first step's briefs, scripts and extracts

**What I confirmed:**
- Re-running `python3 -I method/areas_extract.py` into my scratch directory gives five files, each byte-identical to the committed extract.
- On all five platforms, the extracts hold every inventory list, every in-scope and out-of-scope entry, and every concern line ("Terms: ...").
- The Shopify Help Center section reproduces the outline's two levels (70 top-level and 308 second-level items) from observed-sh at `c8b5fbee`. The working-tree file equals the blob at that commit.
- Salla's help tree is reproduced from observed-sa at `4ca2e896`, with 47 categories in English and 47 in Arabic.

#### 26. The area runs must place ids the extract doesn't show, and too many of them for a short run

- **Where:** `briefs/R1-areas-one-platform.md`, task 4 and "Read only"; `method/areas_extract.py` (`COMPACT`); `method/check_areas.py`.
- **The problem:** the brief asks for "every in-scope inventory entry ... by its id", and the checker requires every in-scope id. But the extract shows eight technical lists as "Entries: name; name; ..." with no ids, and the brief doesn't let the run read `inventory.tsv`. Some names in those lists also repeat, so the run can't recover the ids by name.
  - The run would have to break the brief by reading `inventory.tsv`, or pass the checker by listing 1,444 ids "under none". The checker accepts any mention of an id in the notes (finding 28).
  - Even with ids shown, placing 2,691 ids (Shopify) or 2,516 (Salla) one by one is mechanical work. The founder asked for that to go to scripts.

| Platform | In-scope entries | Shown without ids | Names repeated in one list | Concerns | Ids to place |
| --- | --- | --- | --- | --- | --- |
| Shopify | 2,493 | 1,444 | 7 | 198 | 2,691 |
| Salla | 2,364 | 1,005 | 57 | 152 | 2,516 |
| WooCommerce | 645 | 287 | 0 | 118 | 763 |
| Zid | 535 | 184 | 0 | 96 | 631 |
| BigCommerce | 555 | 371 | 1 | 88 | 643 |

- **The evidence:** every in-scope entry links to at least one concern. Shopify has 1,323 entries with exactly one concern and 1,170 with two or more; Salla has 2,238 and 126.
- **The fix:**
  - Let the run name the areas and place the concerns.
  - Have a script place each entry under the area of its concern or concerns. It lists for the run only the entries whose concerns fall in different areas, or places them under each area.
  - Or show each compact entry's id in the extract.

  Either way, the brief and the checker must agree.
- **Severity:** must fix.

#### 27. The checker accepts names that aren't the platform's, including the founder's words

- **Where:** `method/check_areas.py`: `if name and name not in extract:`.
- **The problem:** a name passes if it is a substring of anything in the extract. That includes:
  - fragments of other words;
  - the extract's own headings and framing text;
  - list labels, which are the concern map's own;
  - the concern map's own descriptions of concerns, which sit beside the platform's terms on every concern line.

  Neither the R1 brief nor the extract says those descriptions aren't the platform's names. The R1 run's self-check and the review's check 1 both rely on this script.
- **The evidence:** my tests (BigCommerce, with a correct file as the base):

  | Name tried | Should be | Result |
  | --- | --- | --- |
  | "market" | rejected | accepted: it occurs in "Marketing" and "marketplace". It is accepted the same way on all five platforms |
  | "availability" | rejected | accepted on Salla and WooCommerce, where it occurs only in identifiers such as `product_availability_notify_management` |
  | "conditions" | rejected | accepted on Zid and WooCommerce |
  | "Pay" | rejected | accepted |
  | "Concerns recorded for this platform" (the extract's heading) | rejected | accepted |
  | "Anti-corruption, export and sanctions compliance" (BC-C-080's description, not a platform term) | rejected | accepted |
  | A real name, given the wrong list in brackets | rejected | accepted (the list isn't checked) |
  | "Selling Everywhere Hub" (not in the extract) | rejected | rejected |
- **The fix:**
  - Check each name against the set of the platform's own names, matched whole: inventory entries, terms split on their separators, Help Center and help-centre names, and list labels only where the brief allows them.
  - Check that it comes from the list named in brackets.
  - Tell the run in the brief that concern descriptions are the concern map's words.
- **Severity:** must fix.

#### 28. The checker's other misses

- **Where:** `method/check_areas.py`.
- **The problem:** of 31 test files, the checker rightly rejected:
  - an id placed twice, or placed nowhere;
  - a concern placed nowhere;
  - a name not in the extract;
  - wrong columns;
  - an unknown grouping;
  - "agent's own" with no reason;
  - no plain line;
  - another platform's id, an out-of-scope id, or an id in lower case.

  It wrongly accepted:
  - an id mentioned in the notes only as "hard to read". `if i not in notes` counts any mention as "under none", and no reason is required;
  - an area with no `platform_names`, marked "platform's own";
  - two areas with one `area_id`;
  - an inventory id in `concern_ids`;
  - one area holding everything. The "15 to 30" aim isn't checked.

  A plain line that opens a quotation mark without closing it is rejected, but reported as "1 areas; 644 problems", starting with "grouping is 'None'". The reader honours quotes, though the brief says "no quoting", so the report points away from the cause.
- **The fix:**
  - Require a "## Under none" section in the notes, with a reason for each id.
  - Require at least one name per area, unique `area_id`s, and ids in their own column.
  - Read with `quoting=csv.QUOTE_NONE`.
  - Optionally warn outside 15 to 30 areas.
- **Severity:** optional.

#### 29. The extract leaves out what the statements show about places and plans

- **Where:** `method/areas_extract.py`; `plan-change.md`, step R1 ("So legal, place and eligibility matters show too").
- **The problem:** legal matters, places and eligibility do show for every platform, through concern names:
  - legal: legal agreements on all five, BC's contracting entities, SH-C-002, SA-C-230, ZD-C-030, WC-C-023;
  - places: Salla's 240 portal countries, Zid's 5 countries, and concerns such as SH-C-174, WC-C-010, BC-C-079;
  - eligibility: plan tables on all five, and the verification concerns.

  So the runs can give them areas. But what differs by country or plan sits in the statements' `scope` column, and the extract has no statements. Shopify, WooCommerce and BigCommerce have no country list at all. Examples of what is left out:
  - Salla's 24 statements scoped "الإمارات" (UAE) and 12 scoped "الكويت" (Kuwait);
  - Zid's 38 scoped "Zid Pay, Saudi Arabia" and 5 scoped "Zid Pay, Kuwait";
  - BigCommerce's "United States, United Kingdom, and Canada".

  The founder asked for the areas to be built "from all that is recorded".
- **The evidence:** statements carrying a scope: Shopify 445, Salla 841, Zid 175, WooCommerce 379, BigCommerce 60.
- **The fix:** add to each concern's line in the extract the distinct scopes of its statements, compactly.
- **Severity:** optional (reading 10).

#### 30. Small gaps in the R1 brief and the extract script

- **Where:** `briefs/R1-areas-one-platform.md`; `method/areas_extract.py`.
- **The problem:**
  - The brief gives the "[list]" form only for inventory lists. It doesn't say what to put in brackets for a concern's term, a Help Center menu or a Salla help-centre category.
  - It asks the run to read "the source at its commit" but forbids running anything in the observed repositories. It doesn't say how to read a source there: for example, with `git --git-dir=... show <commit>:<path>`, run from outside.
  - The script reads the observed repositories' working tree and labels the files with HEAD. They matched today, but reading with `git show <commit>:<path>` would guarantee the cited commit.
  - The script inserts a space before the colon after each Help Center path. That is harmless.
  - Its docstring omits Salla's help tree.
- **The fix:** define the labels; say how to read a held source; read held files from the commit.
- **Severity:** optional.

#### 31. The review can't check the depth choice against recorded data it isn't allowed to read

- **Where:** `briefs/R1-areas-review.md`, "Read only" and check 7.
- **The problem:** check 7 asks the reviewer to "Check each 'why' against the recorded data it cites. Flag a platform whose recorded material suggests an answer the in-depth platforms might not show." The reading list names only the areas folder, `questions.md` and "the cited source at its commit". The extracts hold concern names and terms, but no statements. Without the concern map's statements and the pilot's records, check 7 can't be done.
- **The fix:** add to the reading the concern map's `concerns.tsv` and `statements.tsv`, and the pilot's `statements.tsv`, limited to what `depth.tsv` cites and what the reviewer samples.
- **Severity:** must fix.

#### 32. The merged list's files are unspecified and unchecked

- **Where:** `briefs/R1-areas-review.md` (`areas.tsv`, `areas.md`, `depth.tsv`).
- **The problem:**
  - No draft gives the columns of the coordinator's three files.
  - No script checks names in `areas.tsv`; check 1 says "Every name in areas.tsv ... is in its extract".
  - Nothing checks that the merged list is "tens, not hundreds".
  - Nothing checks that `areas.md` is in plain words for the founder.
- **The fix:** specify the three files' columns, and extend `check_areas.py` to the merged list.
- **Severity:** optional.

#### 33. The sample is chosen before the depth choice that decides what R3's runs are

- **Where:** `plan-change.md`, step R2: "That is question 3 on Shopify, a typical run rather than the cheapest."
- **The problem:** the sample measures the cost per new statement. Shopify's concern map is the richest. About 317 recorded statements fall under the concerns I'd map to question 3, so the run may record fewer new statements and show a higher cost for each. It may also turn out that `depth.tsv` makes Shopify a checking platform for question 3. Then the sample would measure a run R3 never makes.
- **The fix:** choose the sample after `depth.tsv`, from the in-depth runs, by a stated rule. For example, the run whose expected new statements are nearest the median.
- **Severity:** optional (reading 4).

### What it will cost

**The pilot's figures, against section 12 of the method report:**
- **A and A2:** 636 + 248 = 884 million, for 16 agents. Matches section 12. 884 / 821 = 1.08 million per statement.
- **A3:** 296 million. Matches. The audit files hold 61 claims (51 confirmed, 7 partly contradicted, 3 contradicted), so 4.85 million per claim. Section 1 of the method report says 60.
- **The brief inspections:** section 12 gives three pilot inspections at 40 million, 13.3 each. The sizing averages them with three Stage 1 checks at 25 million from the transcripts, which gives 10.8.
- **F:** 79 + 73 + 21 = 173 million, matching section 12's F. The split comes from the transcripts.
- **C's first run (40 million) and Stage 1's targeted checks (60 million)** come from the transcripts. Section 12 gives C's four runs together as 172.
- **The week's limit:** 1,977 / 0.33 = 5.99 billion. The usage window: (748 + 798 + 755) / 3 = 767 million.
- **Arithmetic:** the sizing's rows and totals add up, apart from the coordinator figures in finding 39.

#### 34. Re-runs aren't counted, and several runs are missing

- **Where:** `sizing.md`, "Each step, scaled".
- **The problem:** the founder said "Count every agent run, including brief checks, audits and re-runs". The sizing allows one re-check in R1 and one in each R6 batch, and nothing else for re-runs.
- **The evidence on re-runs:**
  - The method report: "Rework is a large share. A2 and A3 together cost nearly as much as phase A. B, C and D each ran again after the review, and C four times in all"; "Very roughly half of the pilot's cost was one-time or rework".
  - C's first run cost 40 million of C's 172.
  - F needed two re-checks, at 73 and 21 million, not one.
  - The 13 October rule re-runs a part at `high` when its check shows gaps.
- **Runs no step counts:**
  - a re-check of the R1 briefs, extract script, checker and questions once they are revised after this check ("a separate check of each brief before it runs");
  - the selection of what bears on each question (finding 6);
  - reading Stage 1 for each proposal's Yemen part. Nobody is named to do it, and the R4 runs read only "two questions' records";
  - a brief and a check for the checking runs, which record "only what differs", if they differ from the in-depth brief;
  - the review of the company decisions (finding 5);
  - the search and audit behind a "Yemen's evidence doesn't show" that a proposal rests on.
- **Checking runs:** the sizing prices them at 10 statements × 0.54 million = 5.4 million each. But a checking run must first read the in-depth platforms' records and its own copied statements. That reading, not the few statements it records, drives its cost: about 10 million a run.
- **The cost of the omission:** with the budget's stop at the first overrun, a routine re-run will look like an overrun, and the work will stop and come to the founder.
- **The fix:** add a re-run allowance to each step that a check can send back: about 25 percent for R1, R3 and R4, and a second re-check per review. Add the missing runs, and price checking runs by what they read. My figures are under "My cost figures".
- **Severity:** must fix.

#### 35. The pilot's rate per statement counts statements taken from the concern map

- **Where:** `sizing.md`, "Recording statements (phases A and A2) ... 1.08 million per statement"; step R2, and the "at the pilot's rate" case.
- **The problem:** the sample is measured "not counting statements a script copies unchanged". The pilot's 1.08 million is A and A2's cost over all 821 statements. In the pilot's files, 255 of the 821 came from the concern map ("from" = `index:...`), and 205 of those carry exactly the concern map's quote. A3, whose cost isn't in the 884, also recorded some of the 821.

  Counted the way the sample will be counted, A and A2 cost 884 / 566 = 1.56 million per new statement, or 1.44 if the 50 index statements with changed quotes count as new. So:
  - the founder's bar (0.55 million) is about 35 to 38 percent of the pilot's like-for-like rate, not half;
  - the sizing's "at the pilot's rate" case understates R3 by about 500 million: 1,060 × 1.5 = about 1,600, against 1,145.

  This is the founder's bar, and the plan rightly keeps it. The founder should know the comparison before the go.
- **The fix:** state both rates in the sizing and in the founder's summary, and say which one the bar uses (reading 3).
- **Severity:** must fix.

#### 36. Phase C's input is misstated, and drafting's input is far below what bears on the questions

- **Where:** `sizing.md`: R1 and R4 are sized from "phase C's first run: 40 for about 300 KB of records"; R4 says "Each reads two questions' records, about 1.4 times C's input".
- **The problem, in two parts:**
  1. **C's input.** C's brief named `variation-points.tsv`, `variants.tsv`, and each platform's `statements.tsv`, `terms.tsv` and `absences.tsv`. At C's first run (`34a32b9^`), those files total 796,580 bytes, about 780 KB, not 300 KB.
     - If 300 KB is what C actually read, according to its transcript, the sizing should say so.
     - If not, the per-KB rate is 0.051 million, not 0.133. R1's five runs would then scale to about 28 million rather than 80.
     - The small platforms' R1 figures (12, 9, 8) don't follow the stated ratio either (9.7, 6.8, 5.2). A fixed allowance seems to have been added without being shown.
  2. **R4's volume.** "1.4 times C's input" is about 420 KB for two questions on the sizing's base. My rough count of what bears on each question is in the table below. I mapped each concern to questions by its name and terms, and counted all statements under the mapped concerns, in every placement, with their cited quotes. Statements under unmapped concerns can also bear, and some mapped concerns are broad, so it is rough both ways.

     | Question | Shopify | Salla | Zid | WooCommerce | BigCommerce | Statements | KB with quotes |
     | --- | --- | --- | --- | --- | --- | --- | --- |
     | Q1 | 291 | 156 | 90 | 422 | 89 | 1,048 | 575 |
     | Q2 | 556 | 122 | 104 | 210 | 75 | 1,067 | 631 |
     | Q3 | 317 | 140 | 64 | 72 | 41 | 634 | 399 |
     | Q4 | 32 | 32 | 24 | 46 | 14 | 148 | 80 |
     | Q5 | 425 | 257 | 171 | 516 | 70 | 1,439, plus the pilot's 821 | 794, plus about 1,000 |
     | Q6 | 75 | 58 | 39 | 56 | 24 | 252 | 132 |
     | Q7 | 129 | 52 | 33 | 20 | 29 | 263 | 163 |
     | Q8 | 121 | 175 | 101 | 226 | 62 | 685 | 350 |
     | Any question | 1,251 | 719 | 411 | 999 | 237 | 3,617 of 8,191 | |

     Concern ids per question (SH, SA, ZD, WC, BC):
     - Q1: SH 2-3, 5-6, 24, 32, 37, 63, 80, 100-101, 105-111, 113-114; SA 3, 8, 65, 142, 146, 160, 162-167, 230, 304; ZD 5, 9-10, 30-34, 50-51, 60, 62-63; WC 4, 10, 23, 30, 46, 51-55, 58, 75, 99, 108; BC 7, 25-26, 38-39, 48, 70, 72-75, 79.
     - Q2: SH 2, 17, 63, 66-67, 80, 88, 90-105, 148-149, 160-161, 172-175, 177-182, 184; SA 6, 66, 114, 127, 160-162, 167, 170-172, 177-178, 230-233, 235; ZD 9, 30-32, 35-42, 51, 53-54, 98; WC 9-11, 18-29, 40-45, 54-58, 91, 112, 118; BC 25, 28, 37, 72-73, 79-83, 85.
     - Q3: SH 8, 14-15, 68, 70, 73, 75, 88, 90-97, 172-174; SA 2, 4, 6, 110, 112, 118, 128, 172, 177, 232; ZD 1, 20, 23, 35-38, 98; WC 8-9, 11, 16, 22, 28, 81-82; BC 25, 30, 47, 80, 85-86.
     - Q4: SH 18, 79, 84, 87; SA 115-117; ZD 14-16, 28; WC 2, 70-71; BC 20, 23, 31.
     - Q5: SH 18, 62-86, 88; SA 63, 80, 110-127, 164, 177; ZD 1-19, 21, 24, 63; WC 1-16, 18, 20, 40, 42, 48, 51, 98, 103, 115-116; BC 20, 22-28, 30-31.
     - Q6: SH 1-2, 4, 6, 8, 174; SA 1, 6, 167, 230, 232; ZD 30, 32-33, 35, 38, 77; WC 23, 25, 28, 34, 49, 81; BC 55, 79-80, 86.
     - Q7: SH 16, 37, 69, 106-110; SA 5, 163-165; ZD 3, 17, 50; WC 51-53, 108; BC 7-8, 30, 74.
     - Q8: SH 15, 135, 142, 156-157, 163-168; SA 4, 94-98, 194, 205; ZD 20, 26, 60, 70, 73-74, 76, 108-110, 115-116; WC 5, 17, 49-50, 59, 63, 86-89, 104-114; BC 29-30, 38, 59, 65-69, 84.

     So each question has 80 to 800 KB of copies before any new statement. Question 5 adds the pilot's records, which are about 1 MB with their citations. The Yemen part needs Stage 1's `axes.tsv` and `constants.tsv`, another 330 KB. A pair of questions is 0.6 to 2.2 MB, not 420 KB.

     The sizing says "Statements a script copies unchanged cost nothing here". That holds for recording them, not for the runs that must read them.
- **The cost:**
  - At C's named-files rate, eight one-question drafting runs over these volumes cost about 390 million. At the sizing's own rate they would cost about 1,000 million.
  - "Two questions per run" puts question 5 and its pair at about 2 MB, which is not a short run.
- **New statements:** the sizing's 1,060 (22 in-depth runs × 40, plus 18 checking runs × 10) is plausible as a floor. In-depth runs on questions 2 and 5 may need 60 to 100 new statements each, for country rules, licences, entities and methods per country.
- **The fix:**
  - State C's input as measured.
  - Draft one question per run.
  - Either size drafting from these volumes (about 500 million with re-runs), or have each R3 run end with a short account of what its platform shows for the question (ids only, no new claims), draft from those accounts, and open records only to cite them (about 250 million).
- **Severity:** must fix.

#### 37. R5's counts of facts, absences and Yemen facts are low

- **Where:** `sizing.md`, step R5.
- **The problem:** the sizing assumes about 25 facts per question (200 in all), about 3 not-found claims per question (24), and about 40 Yemen facts, 15 of them already checked. The pilot shows more for one subject:
  - The pilot's entry, the model for the money proposals and Decisions 1 to 14, cites 121 variants, 61 statements and 51 Stage 1 ids (23 axes, 16 constants and 12 cases).
  - The pilot's 614 variants included 36 `gap` and 2 `absent` ones.
  - A3 audited 61 claims for one subject.

  Questions 2, 4 and 6 ask about things platforms "withhold", "do and not do" or "don't fully support", which produce not-found claims.
- **My estimate:**
  - about 350 platform facts × 0.4 = 140 million;
  - about 50 to 64 not-found claims at 4.85, batched by platform, about 230 million;
  - about 45 Yemen facts not yet checked × 1.8 = 80 million, plus about 20 million for searching and auditing "doesn't show" claims;
  - about 30 million for re-checks after fixes;
  - with the brief checks, about 520 million, against 268.
- **The fix:** re-size R5 from the pilot's entry, or put the reading of "each fact it rests on" to the founder (reading 8).
- **Severity:** must fix.

#### 38. One of the cuts isn't real, and the order should change

- **Where:** `sizing.md`, "If it can't fit, what would be cut, in order".
- **The problem:**
  - **Cut 3**, "One review batch instead of two: about 60 million less", is shown without working. One review of eight proposals is a longer run over the same material. The method report says cost grows with run length ("An agent re-reads its whole history on every turn"), so the saving is doubtful.
  - **Cut 1**, one in-depth platform fewer for each question, is real: 8 runs × 30 fewer statements × 0.54 = about 130, rising to about 180 with smaller drafting and checks. Against the stated 200, that is close. But it thins every proposal (risk 16), so it should come last.
  - With the figures corrected (findings 34 to 37), the plan doesn't fit 2 billion at the founder's bar. So the cuts are a choice for the founder now, not a contingency.
- **The fix:** offer these, in this order, with savings at my figures:
  1. Question 8 from the areas list and what is recorded, with no recording run: 60 to 80.
  2. Entries placed by script through their concerns in R1: 20 to 40.
  3. Drafting from the R3 runs' short accounts (finding 36): 200 to 250.
  4. Checking runs merged by platform, one run checking one platform for several questions: 60 to 90.
  5. The search and audit only for not-found claims a recommendation turns on, if the founder accepts that reading: 100 to 150.
  6. One in-depth platform fewer where the concern map already holds most (questions 4, 6 and 7): 50 to 80.
  7. Last, one in-depth platform fewer for every question: 130 to 180.

  Cuts 1 to 5 bring about 2.5 billion down to about 2.0 to 2.1.
- **Severity:** must fix.

#### 39. Where the figures come from, and small inconsistencies

- **Where:** `sizing.md`.
- **The problem:**
  - **Sources not marked.** The sizing marks only the usage-limit conversion as "the coordinator's reading of the session's transcripts". Several pilot figures also come from the transcripts but aren't marked:
    - C's first run, 40;
    - F's split, 79, 73 and 21;
    - Stage 1's brief checks, 25, and its targeted checks, about 60;
    - "about 40 to 45 percent of this week's limit is used already".
  - **Where they meet section 12, they agree:** F's parts sum to 173, and A and A2 to 884.
  - **The brief-check rate.** Using the pilot's own inspections (13.3 each) rather than the mix (10.8) adds about 2.5 million per brief check.
  - **The coordinator's table.** It gives "R5 and R6" together as 80, but the per-step table gives R5 40 and R6 80. The per-step coordinator figures sum to 445, plus 20 "throughout", not 425.
  - **A3's claims.** The sizing's 61 matches the audit files. The method report's section 1 says 60.
- **The fix:** mark each figure's source, and reconcile the coordinator's figures.
- **Severity:** optional.

#### 40. The calendar's waits and the week's limit

- **Where:** `sizing.md`, "By the calendar, waits included".
- **The problem:**
  - "If each takes up to a day, the plan takes about 5 to 7 days from the go to the proposals" counts the go and the proposals' answers as waits. Both lie outside "from the go to the proposals". Only G2's wait falls inside.
  - With my figures (about 3.1 billion with the coordinator, about 52 percent of a week's limit), and with 40 to 45 percent of this week already used, the plan would use nearly all that is left before the 24 October reset. Any overrun would stop at the weekly limit, as every agent did from 13 to 17 October.
- **The fix:** count only the waits inside the span. Say that the plan either starts after the reset, or expects a pause at the weekly limit.
- **Severity:** optional.

---

## The readings

Each is a place where the drafts read the founder's message one way when it could be read another, and the choice changes a step, a cost or what reaches the founder.

1. **"Go deep where a wrong guess would be expensive to change after launch: money flows, legal structure, the data model, partner contracts. ... The rest gets a line each, with the reason."**
   - **The drafts' reading:** depth comes only through the questions, as the choice of in-depth platforms. "The rest" is what lies outside the questions.
   - **The other reading:** the four topics get deep reading in their own right, even where no section B item asks. "The rest" is the areas left in that no question needs.
   - **What it changes:** under the other reading, there are a few more recording and drafting runs (about 100 to 250 million), and the founder sees the data model and partner contracts treated explicitly.
2. **"'Defer' here means the decision stays open and binds nothing."**
   - **The drafts' reading:** this holds for every later deferred item (section 5).
   - **The other reading:** "here" means only Decisions 1 to 14, and the founder sets what defer binds later.
   - **What it changes:** what a "defer" answer on any proposal means for the first build's design.
3. **"If the sample's cost per statement isn't below half the pilot's 1.1 million for phases A and A2, stop."**
   - **The drafts' reading:** a fixed bar of 0.55 million per new statement.
   - **The other reading:** half the pilot's rate counted as the sample is counted, without the statements taken from the concern map. That is 1.44 to 1.56 million, so half is 0.72 to 0.78.
   - **What it changes:** whether the work stops at R2. A sample at 0.6 to 0.75 million stops under the first reading and passes under the second. It also changes R3's expected cost: about 570 against about 760 to 830 million.
4. **"Run a sample of it: one platform and one question."**
   - **The drafts' reading:** question 3 on Shopify, fixed now.
   - **The other reading:** one of the runs R3 will actually make, chosen after `depth.tsv`.
   - **What it changes:** whether the measurement represents R3, and so whether the work stops at R2.
5. **"Where the platforms' own names can't bring the list down to tens, the coordinator groups further, marking each such grouping as its own."**
   - **The drafts' reading:** agents also group on each platform, marked "agent's own", and the coordinator then groups the merged list.
   - **The other reading:** only the coordinator groups. The per-platform step only collects names, by agent or by script.
   - **What it changes:** agents' groupings reach the founder at G2, and the five agent runs cost about 80 million.
6. **"I mark what Sharrwah won't do or must do. Anything unmarked stays in."**
   - **The drafts' reading:** "must do" has no stated effect.
   - **The other reading:** a "must do" area gets reading and a proposal even if no section B item covers it.
   - **What it changes:** the steps and cost after G2, and what reaches the founder.
7. **"Decisions 1 to 14 ... come back to me as proposals once the work in section C has framed them."**
   - **The drafts' reading:** questions 4 and 5 carry all 14, through question 5's added sentence.
   - **The other reading:** each decision comes back with the question it belongs to. Decision 14, on currency, goes with question 7.
   - **What it changes:** which proposal carries which decision, and question 7's scope.
8. **"each fact it rests on gets the full checks"**
   - **The drafts' reading:** about 25 facts and 3 not-found claims per question.
   - **The other reading:** every fact and not-found claim the proposal cites. The pilot's entry cited 121 variants and 61 statements.
   - **What it changes:** R5's cost (about 270 against about 520 million) and how much of each proposal is fully checked.
9. **"one independent review of each result before it reaches me"**
   - **The drafts' reading:** the areas list and the proposals.
   - **The other reading:** also the company decisions.
   - **What it changes:** one more review, about 20 million, and whether company decisions reach the founder unreviewed.
10. **"Build them from all that is recorded"**, with Part 2's "concerns.tsv and statements.tsv ... in every placement".
    - **The drafts' reading:** the areas extract uses the inventory, the concerns and two help menus.
    - **The other reading:** it also uses what statements show, at least their scopes by country and plan.
    - **What it changes:** whether country and plan differences show at G2 and in the depth choice.
11. **"Re-size the steps that record or audit statements from that measurement."**
    - **The drafts' reading:** checking runs are priced per statement, at 10 each.
    - **The other reading:** checking runs are priced by what they must read.
    - **What it changes:** R3's cost, by about 80 million more.
12. **"From the Yemen study, record what Yemen's evidence allows, forbids or doesn't show for each proposal."**
    - **The drafts' reading:** from Stage 1's output, with "doesn't show" read off Stage 1.
    - **The other reading:** a "doesn't show" that a proposal rests on gets the search and audit, like any not-found claim. Stage 1's review found held evidence that wasn't recorded (its finding 8).
    - **What it changes:** R5's cost (about 20 to 40 million), and whether a "Yemen doesn't show" reaches the founder unaudited.
13. **"Keep each agent's task short ... and give mechanical work to scripts."**
    - **The drafts' reading:** recording runs are short. Drafting takes two questions per run, and the area runs place every id by hand.
    - **The other reading:** every run is short, and placement goes to a script.
    - **What it changes:** R4's and R1's cost, and whether they can be done at all (findings 26 and 36).
14. **"A step that runs past its expected cost stops and comes to me."**
    - **The drafts' reading:** section 8 doesn't say whether "expected cost" is the agents' cost or includes the coordinator's.
    - **The other reading:** it is the agents' cost only, as the budget counts it.
    - **What it changes:** when the stop fires.

## My cost figures

These are in millions of tokens, for the agents, at the founder's bar, and only where they differ from the sizing's. They are rough. The working is in findings 34 to 37.

| Step | Sizing | Mine | Why |
| --- | --- | --- | --- |
| R0 | 40 | 60 | Adds a re-check of the revised R1 briefs, script, checker and questions before they run (finding 34) |
| R1, area runs | 80 | 80 | No change. On C's named input, the sizing's own method gives about 28, so 80 covers a re-run |
| R1, review | 65 | 85 | Adds a second re-check; F needed two (73 and 21) |
| R2 | 33 | 33 | No change |
| R3 | 570 | about 850 | In-depth runs: 475 to 575, since questions 2 and 5 may need 60 to 100 new statements a run. Checking runs priced by what they read: 18 × about 10 = 180, not 97. Selection of what bears: about 80. Re-runs at `high`: about 75. A brief check for the checking runs: 11 |
| R4 | 231 | about 500 | Brief check 11. Eight one-question runs over the volumes in finding 36, at C's named-files rate: about 390. Re-runs, as C's ran four times: about 100. With short accounts from R3: about 250 |
| R5 | 268 | about 520 | About 350 facts × 0.4 = 140; about 50 to 64 claims, batched, about 230; Yemen facts about 80, plus "doesn't show" audits about 20; re-checks about 30; brief checks 22 |
| R6 | 201 | about 340 | Each batch is at least the pilot entry's material, so a first review of about 90 per batch, and two re-checks of about 70 per batch. Plus the company decisions' review, 20, and the brief check, 11 |
| Company decisions' evidence | 0 | about 30 | No step gathers it now |
| **Agents' total** | **1,488** | **about 2,500 (2,000 to 3,000)** | At the pilot's like-for-like rate per new statement, about 3,400 |
| Coordinator | 425 (445 to 465 by the per-step table) | about 600 | The pilot's 0.2 to 0.3 per agent token, with more runs to start, check and fix |
| **Whole plan** | **1.92 billion; a third of a week; about 2.5 usage windows** | **about 3.1 billion; about 52 percent of a week's limit; about 4 usage windows** | |

**Per step, agents and coordinator together, as a share of a week's limit of 6.0 billion:**
- R0: about 2 percent;
- R1: about 4 percent;
- R2: about 1 percent;
- R3: about 17 percent;
- R4: about 10 percent;
- R5: about 10 percent;
- R6: about 7 percent.

**By the calendar:** about 5 to 7 days of work. With G2's wait inside the span, that is about 6 to 8 days from the go to the proposals. It doesn't fit in what is left of this week's limit before 24 October without a likely pause at the limit.

With the cuts in finding 38, items 1 to 5, the agents' total comes to about 2.0 to 2.1 billion.

## Verdict

**Yes, the drafts can go to the founder in summary once the 19 must-fix findings are fixed, on two conditions:**
1. **A separate check before anything runs.** What changes as a result goes through its own separate check first, as the founder's kept rule requires: the R1 briefs, the extract script and checker, and the questions.
2. **The summary gives the re-sized cost.** At the founder's bar, the agents' work is more likely about 2.5 billion than 1.5. The summary should say so, give the like-for-like comparison behind the sample's bar (reading 3), and offer the cuts in finding 38 for the founder to choose before the go.

**What works as written:**
- The plan change carries almost everything in the founder's sections A and C and Part 2.
- The extract script reproduces its output exactly.
- The extracts hold every list, entry and concern.
- The questions are close to neutral. Five need re-wording.
