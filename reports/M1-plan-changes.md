# The plan's two changes, and what they hid

**25 October 2026.** Part two of the assessment you asked for before Decision 1 (part one: `reports/M1-method-assessment.md`). You asked whether `PLAN.md`'s second change brought in rules or constraints that hide the gaps your feedback points to. Neither version is assumed right here: each rule is traced to the text that brought it in and the reason given.

## The versions compared

| Version | Commit, date | Unit of work | Where coverage was checked |
| --- | --- | --- | --- |
| **The first plan** | `questions/`, `NEXT.md`, 10 October | Three questions. Q1, the concern map, inventories each platform's own lists | Q1 itself: every list entry placed in a concern, or out of scope with a reason |
| **First change:** `PLAN.md` | `2842819`, 12 October; as it stood before G1, `099e555`, 17 October | Subjects: "decisions that are expensive to change first, the map as their index". It produced the pilot's 14 decisions and G1 | Each subject's test form, then at close-out "A last sweep of the inventory's remaining concerns" (`099e555:PLAN.md`:171) |
| **Second change:** the re-frame | `7fec7f0`, 18 October (`studies/proposals/plan-change.md`, Part 1) | Questions from your intent, "not subjects"; the 34 areas as the extent | One line for each *area* no question draws on: "This replaces Stage 5's last sweep" (`7fec7f0:PLAN.md`:178) |
| **Third change:** `METHOD.md` | `7a97224`, 24 October | Subjects again, each assigned areas by me | None before M8. At M8, against the Knowledge Map's 179 questions and the 81 payment rows (`METHOD.md`:256), not the platforms' own lists. Checks cover "only the facts a decision rests on" |

## What the second change added, removed and constrained

The change's own record lists what it stopped, kept, added and replaced, and which parts are "the coordinator's own" (`plan-change.md`:16–78). Set against the first change:

| Change | Reason given | Evidence or practice behind it | Effect on finding gaps |
| --- | --- | --- | --- |
| **Questions from your intent, not subjects from evidence.** Before, subjects "come from evidence only", ranked by cost of change (`099e555:PLAN.md`:133, :146) | Your G1 choice to re-frame | Your decision. Your intent's items were turned into neutral questions | Units of work came from intent, not from the evidence map. A concern outside every question could surface only through the area line below |
| **Stopped "labelling why platforms differ":** the test form's cause step (3) and its rules for what follows (5) | Cost: the pilot's 23 variation points multiplied every phase (method report, proposal 1) | The cost is measured. Nothing weighed what the step protected | **Removed the variability analysis.** The coexistence step went with it: whether a platform carries both variants at once. Only its rulings are listed as lapsing (`plan-change.md`:56–57). So did its rule, listed nowhere: "When one variant is a restricted form of another, and the general one can reach it by configuration, keep the general one" (`099e555:PLAN.md`:239), from Czarnecki, Helsen and Eisenecker (2005). That is your variability point, written down on 12 October and dropped on 18 October |
| **The last sweep became one line per area** (`plan-change.md`:207) | None given | Drafted by me in the change's text, not among your five changes | **Coverage moved from concerns to areas.** An area any question drew on counted as covered, whatever its concerns |
| **The 34 areas** (R1), as the extent, with your marks (G2) | Your intent; the platforms' own areas | Built per platform from each one's own top-level areas, in its own words, and re-checked. 17 of the 34 headings are mine, merging platforms' areas; 17 are a platform's (`studies/proposals/areas/areas.tsv`) | Better for the whole extent: every area has a subject. Worse within one, once areas became the scope of each subject (below) |
| **Kept:** quotes at a pinned commit; "the search and audit behind anything a proposal cites that was not found, or is recorded absent"; absence only "from a complete list the platform publishes" (`7fec7f0:PLAN.md`:309) | — | The pilot's own failure and fix (method report, section 1) | **The absence rule survived this change.** It was lost at the third |
| **Added:** "the platforms' own words", never our categories (`7fec7f0:PLAN.md`:300–301); the budget, the sample, your guard on money, plain words | Your go; Q1's rule of 11 October | Rahm and Bernstein (2001) for matching; the pilot's costs | Guards against forcing concerns into categories of ours |
| **Constrained:** about 40 platform facts per proposal (19 October) | Cost | None | You made it a guide the same day (`founder-decisions.tsv`, 19 October) |

**What the third change did with these.** `METHOD.md` dropped the absence rule. It replaced "everything a proposal cites is checked", your choice of 18 October, with "only the facts a decision rests on", and said so (section 13), as it did for two practices it stopped. It didn't list the absence audit, the concern map or the sweep, and it never mentions the concern map. It assigned each subject areas: S-01, the money boundary, got A-12 and A-13 (`decisions/subjects.tsv`).

## Do the areas help, or force concerns into categories?

Both, and the difference lies in how they are used.
- **They help as an extent.** They come from the platforms' own top-level areas, and the concern map's concerns sit beneath them through R1 (`areas-<platform>.tsv`). So no area of either platform is forgotten. `method/decision_status.py` confirms "34 of 34 have a subject".
- **They mask as a unit of scope.** A subject is assigned areas, and its evidence is what its decisions "turn on". Nothing then opens the concerns beneath the areas, or looks past them.
  - Decision 1's question, who holds sellers' money, reaches every place money moves: fees (A-03), methods and providers (A-11), cash on delivery (A-10), marketplaces (A-21), point of sale (A-22) and apps (A-24). Its subject was given two areas.
  - The trial in part one found the missed evidence for choice 2 in A-03, A-12 and A-13, below the area labels. Salla's financing sits in A-13, one of the subject's own two areas, so part of the miss was inside them.
- *Interpretation:* the masking comes from coarseness and from where the boundary is drawn, not from invented categories. The concerns beneath are the platforms' own; the method never looks at them.

## Can the order in which the method meets its rules keep gaps hidden?

Yes. In the method a subject meets, in this order:
1. its assigned areas;
2. its decisions;
3. the evidence "each decision turns on", with "nothing read broadly";
4. checks of "only the facts a decision rests on".

Each step narrows and none widens. The first plan ended with a widening step, the sweep of the inventory. The second plan kept a coarser one, the area line. The third has none before the end of the work (M8), and that one is against agent-written questions, not the platforms' own lists. So a gap outside a subject's areas, or inside them below the area labels, is found only by a checker's own initiative, or by you.

## Your concerns in this message

| Concern | Verdict | Evidence |
| --- | --- | --- |
| The second change brought in rules or constraints that hide gaps | **Genuine in part.** Two choices of mine did: dropping the variability analysis with its generality rule, for cost, and coarsening the sweep to areas, with no reason given. The areas themselves are sound, and the absence rule survived this change | Table above |
| The areas force concerns into predefined categories | **Partly.** They are built from the platforms' own areas, so they aren't invented. Used as each subject's scope, they hide the concerns beneath them and the decisions that cross them | Decision 1's reach against its two areas; part one's trial |
| The order of the rules can stop gaps being detected | **Genuine.** Scope is fixed first, and nothing afterwards widens it | The four steps above |

## Root cause

**Each change re-cut the unit of work: concerns, then subjects, then questions, then subjects in areas.** It carried over steps, not the functions those steps served. A safeguard tied to the old unit went with it, or was coarsened, and nobody asked what risk it had controlled:
- the variability analysis went with the test form;
- the concern-level sweep became one line per area;
- the absence audit and the concern map went with `PLAN.md`.

The second change's record at least listed what it stopped, kept and replaced, step by step. The third listed the founder decisions it changed and two practices it stopped, but not the absence audit, the concern map or the sweep. The register already named this risk, W-08, "Earlier work is lost or redone"; its mitigation failed.

*Established practice:* a change to a process is assessed for the hazards its removed parts controlled, and each one is reassigned or accepted on purpose. Process safety calls this management of change: OSHA's process safety standard requires written procedures for changes to procedures, covering "the technical basis" for a change and its impact on safety and health (29 CFR 1910.119(l), as OSHA's [VPP Supplement A](https://www.osha.gov/vpp/supplement-a-questions) describes it; the regulation's text was not read). *Interpretation:* applying it to a design method is my reading.

## The smallest justified correction

It refines amendment 4 in part one:
- **4b, the omission check, takes its slice from what the record reaches,** that is, the areas its question and Terms touch, named by the checker, not the areas its subject was assigned. That restores the first plan's sweep at the level it was planned for, concerns, and moves it from the end of the work to each record.
- **4c, change control for the method, works by function.**
  - An amendment names, for each practice it retires, the risk that practice controlled, and either reassigns it or records it as accepted.
  - W-08's map of earlier work, in section 13, is finished.
- **4d, variants, restores the coexistence step and the generality rule** to step 3 (Propose):
  - where the references differ, or one reference carries more than one variant at once, each variant becomes an option, with how it is bound;
  - when one is a restricted form of another that the general one can reach by configuration, the general one is kept, and the restricted one is bound where it is needed (Czarnecki, Helsen and Eisenecker 2005, as the first plan cited it).

  Section 2 already names variability and binding time as a practice, tied there to markets. On fees, each reference carries both variants at once, so only the coexistence trigger catches choice 2's "never". Choices 2 and 3 follow 4d since the revision of 25 October; the version sent to you said "never".

**Not proposed:** bringing back the test form's cause labels or the per-subject variation points. Their cost was measured, and the coexistence step with the generality rule carries the part your concern needs.
