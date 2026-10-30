# Brief: Q3's check for what the class's model misses (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A: "At the end, Q3's reconciliation places the Knowledge Map's 179 questions and the 81 payment rows against the model. A row the model doesn't cover is a candidate miss, checked against the evidence." It carries out Q3 as the founder agreed it (`questions/Q3-placing-rows.md`), on the class's model instead of the concern map. You are one agent with one batch of rows; your message names the batch and its rows.

**Read only this brief and:**
- `studies/class-model/q3/rows.tsv`: the 260 rows, each known by its `set` (`km` for the Knowledge Map's questions, `pay` for the payment rows) and its `row_id` together, since both sets have a `PAY-01`. It holds only each row's id, `needed_by` and question, which is all a row is read for (`PLAN.md`, section 6, "Q3's rows"): their founder lane is not current, and their other columns hold citations that are not trusted. Don't open the rows' original files.
- the class's model, through `method/q3.py` (`slice`, `where`) and `method/class_slice.py` (`model`, `key`, `statements`, `search`, `outscope`, `caps`);
- `founder-decisions.tsv`, whole: the decisions in force, and the founder's list (the row of 29 October whose gate is "Intent (standing)");
- `studies/subjects/subjects.tsv`, and the subjects' registers (`studies/subjects/S-0N/register.tsv`) for their product gaps: a need a market shows that no reference meets;
- `architecture/plan.md`, section 3, for which subjects each area's architecture waits for.

## What the rows are

Agents wrote these rows on 8 October, from two platforms and a smaller evidence base, as questions they perceived then. They are not Sharrwah's requirements, and they don't steer the model. They are inputs to place. A row never adds a capability, a variation point, a variant or a cause: where it shows something the model lacks, the coordinator decides, from the evidence you name.

A row's `needed_by` is its own, from the Knowledge Map's page at `e4d5cee`: `spine` "to build the capability map and glossary now", `model` "before the area's domain model is written", `slice` "before the area's first build slice", `launch` "before merchants depend on it", `later` "when the area comes up".

## For each row

1. **`result`, one of:**
   - `covered`: every thing the row asks about has a capability of the model, with its cells. The extent holds capabilities and where each platform places them, not their detail. Detail the row asks beyond the cells (states, fields, rules, the steps of a flow) doesn't make the row `partly` or a miss: name it under `what_would_settle_it` as `detail: <what>`, for the model's detail at that area after GM.
   - `partly`: some thing the row asks about has a capability, and some thing has none. Say what the rest is in `rest` (below).
   - `beyond the class`: by its nature, the class's evidence can't answer it, and the model isn't meant to. It asks a market's fact (a subject's), Sharrwah's own design (engineering's), a decision on the founder's list (the founder's), the method itself (the plan's), or what a provider, partner or regulator would say. A row that a decision in force already answers is `beyond the class`, answered by `founder`, with the decision in `basis` and `decided` in `what_would_settle_it`. A row a subject's register answers as a product gap is `beyond the class`, answered by that subject, with the register row in `basis`.
   - `candidate miss: held`: it asks about a thing the class does, no capability is that thing, and the concern map holds statements that are. Name their keys in `basis`, and in `cap_ids` the capability their concern lands in, where the miss would sit.
   - `candidate miss: not held`: it asks about a thing the class does, no capability is that thing, and the concern map holds nothing for it. Name the material that would settle it in `what_would_settle_it`: the page or the capture. The coordinator routes it by `PLAN.md`, section 6, "Evidence", before anything goes to anyone.
   - `unclear`: the evidence can't settle where it belongs. Say what would.

   **Before you call a thing a miss, search for it**: `class_slice.py search`, in English, and for Salla and Zid in Arabic too, singular and plural, with and without ال; then `outscope`, for entries Q1 left out of its concerns. **For each statement a search finds, run `q3.py where`.** If a cell cites it, or its concern lands in a capability that is the thing the row asks about, the row is `covered` or `partly` by that capability. If its concern lands only in a coarser capability, the thing is a held miss.

   **`rest`,** for `partly` only, and empty otherwise: what the uncovered part is, one of `beyond the class`, `candidate miss: held` (its keys in `basis`) or `candidate miss: not held`. The rules above apply to it as to a whole row.

   Domain H's areas (WLD, ENG, INT, MTH) hold no capabilities by design: an empty area there is not a miss.

2. **`who_answers`,** every one that applies, `;`-separated:
   - `model`: the model's capabilities and cells;
   - `subject:S-NN`: a subject of `subjects.tsv`, where the row asks who or what fills something in a market; `subject:none` where a market's fact is covered by no subject, with the subject it would need named in `what_would_settle_it`, for the coordinator to take to Stage 3's list;
   - `founder`: a decision on the founder's list: markets, their order and timing, and which merchants first; plans and prices; commercial agreements and partners; the company, its legal structure and licences; spending; whether Sharrwah's own company runs a service in the merchant's business, where and when (`founder-decisions.tsv`, 29 October, "Intent (standing)"); where a decision in force already answers part of a covered row, `founder` is among its answerers, the decision is in `basis` as `founder-decisions <date> <gate>`, and `what_would_settle_it` says `decided`;
   - `engineering:build` or `engineering:detail`: Sharrwah's own design, an architecture decision (`build`) or a build detail, decided as the area is built (`detail`). Where an engineering ruling already in force answers part of the row (a subject's register row that is engineering's and wasn't vetoed), name the row in `basis` as `S-NN <row id>` and say `ruled` in `what_would_settle_it`;
   - `outside`: a platform, partner, regulator or lawyer, reached through the founder;
   - `plan`: the method itself, which `PLAN.md` or a decision on it answers.

   **Whom a row's words ask:** a row in the present tense about "the platform(s)" or "each platform" asks the class, the model. A row with "should" or "Sharrwah" asks engineering, or the founder where its subject is on the founder's list. A row that names neither asks the model what the class does; add engineering only where it also asks a choice that is Sharrwah's own, such as which of the platforms' shapes to take, a limit or a policy, which the class's evidence can show but not make. These words decide engineering's part only. A subject or the founder answers wherever the row's thing is one they hold, whatever its wording: a market's rules (what a merchant must declare in each market, how long a market requires data kept) are the subject's that covers them, and a thing on the founder's list (how many staff a plan allows, as plans and prices) is the founder's.

3. **`when`** it must be answered. These rules are the coordinator's own, a reading:
   - `model`: `before build`, since the architecture reads the model before anything is built;
   - `engineering:build`: `before build`; `engineering:detail`: `at the area's build`, the time a row's `needed_by` `slice` names;
   - `founder`: `before release`, for every decision on the founder's list, since the platform keeps room for each, whoever provides it (`founder-decisions.tsv`, 26, 28 and 29 October). What the structure must keep open for such a decision is engineering's: add `engineering:build` where the row asks how room is kept;
   - `subject:S-NN`: `before build`, since each area's architecture waits for the subjects that cover its open questions, and S-03's and S-09's bind every area (`architecture/plan.md`, section 3). Where the row asks only which provider, partner or law fills a slot in one market, add `outside`, `before release`;
   - `subject:none`: gives no time of its own;
   - `outside`: `before release`;
   - `plan`: `before build`;
   - with several answerers, the earliest; `unclear` where none applies.

4. **`time_bombs`,** by Q3's four types:
   - `bundles`: its parts land on capabilities placed differently: of different kinds (`class`, `slot`, `open`), as `q3.py slice` shows them (Q3's type, as agreed). Also where its parts have different answerers' times (the coordinator's own addition, a reading);
   - `wrong party`: as worded, it asks a party that can't answer it: it asks what the platforms do about something only a market, the founder or engineering settles; or it asks for a decision the class's evidence or a decision in force already settles. Its lane isn't read, so judge by its words;
   - `wrong time`: its `needed_by` disagrees with the earliest `when` of its answerers other than `model`, reading `model` and `spine` as before build, `slice` as at the area's build, `launch` as before release and `later` as later. A row only the model answers has none, and a `when` of `unclear` raises none (the coordinator's own reading of Q3's type);
   - `market fact`: it asks what the product should do, where the answer is a fact of a market.

   `q3.py check` computes `bundles` and `wrong time` from your other columns and requires them exactly where they hold.

5. **`basis`,** `;`-separated: for `covered` and `partly`, the cells that answer, as `<cap_id>@<platform>`, adding statement keys only where a cell's reading is what answers; for a held miss, the statement keys; for a subject, its id and its register row, or, for a subject that hasn't run, `subjects.tsv <S-NN>` or the register row that moved the question to it; for a decision, `founder-decisions <date> <gate>`; for the plan, its section.

6. **`what_would_settle_it`:** for `partly`, `unclear` and `candidate miss: not held`; and `detail: <what>` where a covered row asks detail beyond the cells.

## Rules

- Every claim is one of three (`PLAN.md`, section 6): a fact, traced to its key; a reading, marked as one; an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, the row is `unclear`, with what would settle it.
- A covered row is covered by what the cells hold, whatever their placement: a capability with nothing held on one platform still answers a question about the class, and the cells say who holds what.

## How to work, keeping your context small

- `python3 -I method/q3.py slice --rows <set:id,...>`, or `--area <AREA> --set km|pay --from N --to M`: each area's capabilities once, with each one's domain, kind, count and placements, then each row with the capabilities elsewhere that share its rarer words. A lead list, not an answer.
- `python3 -I method/q3.py where <key or statement id> ...`: which cells cite a statement, and where its concern lands.
- A row's thing may sit outside its own area (a payment row's answer in orders, checkout or returns): run `class_slice.py caps --terms "<its words>"`, the terms `;`-separated, before you settle on its area's capabilities.
- `python3 -I method/class_slice.py model --domain <D> --areas <AREA>` for an area's cells and their placements; `python3 -I method/land_points.py cell <cap_id> <platform>` for one cell whole, its reading and every statement it cites; `class_slice.py key <key or statement id>` for one statement; `search` and `outscope` for a candidate miss.
- Write your batch's own file, `studies/class-model/q3/check-<batch>.tsv`, with its header, a few rows at a time; don't print it back. Other batches write their own.

## Output

`studies/class-model/q3/check-<batch>.tsv`, tab-separated, a header row, no quoting; no tab or newline inside a field:

`set` · `row_id` · `needed_by` (the row's own) · `result` · `rest` · `cap_ids` (`;`-separated) · `who_answers` · `when` · `time_bombs` (`;`-separated, or empty) · `basis` · `what_would_settle_it`

Check it with `python3 -I method/q3.py check --batch <batch> --rows <set:id,...>` until it prints no problem. It checks and counts only your rows.

Write `studies/class-model/q3/notes-<batch>.md`: rows that were hard to place and why, the candidate misses with what you searched, and problems with this brief or the evidence.

## Report

Back to the coordinator:
- your rows' count by result;
- each candidate miss, with its keys or what you searched;
- the time bombs;
- any problem;
- the checker's final line.

## After the last batch

The coordinator runs `q3.py check` on every batch together, and `q3.py unasked`: the capabilities no covered or partly row names (Q3's item 3, read on capabilities instead of concerns). The coordinator amends the model from the held misses through `<domain>-amend` parts, each with every platform's cells (`B-extent.md`, "The amendment part"), marking each amended row "(the coordinator, from Q3's check: <set:row_id>)". The merge then runs, and the final review reads Q3's check with the rest of the extent.
