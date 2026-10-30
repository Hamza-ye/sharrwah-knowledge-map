# Brief: Q3's check for what the class's model misses (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A: "At the end, Q3's reconciliation places the Knowledge Map's 179 questions and the 81 payment rows against the model. A row the model doesn't cover is a candidate miss, checked against the evidence." It carries out Q3 as the founder agreed it (`questions/Q3-placing-rows.md`), on the class's model instead of the concern map. You are one agent with one batch of rows; your message names them.

**Read only this brief and:**
- `studies/class-model/q3/rows.tsv`: the 260 rows, each known by its `set` (`km` for the Knowledge Map's questions, `pay` for the payment rows) and its `row_id` together, since both sets have a `PAY-01`. It holds only each row's id, `needed_by` and question, which is all a row is read for (`PLAN.md`, section 6, "Q3's rows"): their founder lane is not current, and their other columns hold citations that are not trusted. Don't open the rows' original files.
- the class's model, through `method/q3.py slice` and `method/class_slice.py` (`model`, `key`, `statements`, `search`);
- `studies/subjects/subjects.tsv`: the subjects, each a question of the form "who or what fills X" for a market;
- `founder-decisions.tsv`, the row of 29 October ("Intent"), for the founder's list;
- `architecture/plan.md`, section 3, for which subjects bind the architecture's structure.

## What the rows are

Agents wrote these rows on 8 October, from two platforms and a smaller evidence base, as questions they perceived then. They are not Sharrwah's requirements, and they don't steer the model. They are inputs to place. A row never adds a capability, a variation point, a variant or a cause: where it shows something the model lacks, the coordinator decides, from the evidence you name.

## For each row

1. **`result`, one of:**
   - `covered`: capabilities of the model answer what the row asks about the class: their cells say how the platforms do it. Name every capability it needs.
   - `partly`: some of what it asks is covered (name those capabilities), and the rest isn't (say what, under `what_would_settle_it`).
   - `beyond the class`: by its nature, the class's evidence can't answer it, and the model isn't meant to. It asks a market's fact (a subject's), Sharrwah's own design (engineering's), a decision on the founder's list (the founder's), or what a provider, partner or regulator would say.
   - `candidate miss: held`: it asks what the class does, no capability answers it, and the concern map holds statements that do. Name their keys in `basis`. The coordinator amends the model from them.
   - `candidate miss: not held`: it asks what the class does, no capability answers it, and the concern map holds nothing for it. Say what would settle it: a capture of named material, or a subject.
   - `unclear`: the evidence can't settle where it belongs. Say what would.

   Before you call a row a candidate miss, search the concern map for it with `class_slice.py search`: in English, and for Salla and Zid in Arabic too, singular and plural, with and without ال. Read what you find with `key`. A statement the model already cites in a capability you missed makes the row `covered` or `partly`, not a miss.

2. **`who_answers`,** every one that applies, `;`-separated:
   - `model`: the model's capabilities and cells;
   - `subject:S-NN`: a subject of `subjects.tsv`, where the row asks who or what fills something in a market;
   - `founder`: a decision on the founder's list: markets, their order and timing, and which merchants first; plans and prices; commercial agreements and partners; the company, its legal structure and licences; spending; whether Sharrwah's own company runs a service in the merchant's business, where and when (`founder-decisions.tsv`, 29 October);
   - `engineering`: Sharrwah's own design, an architecture or build decision;
   - `outside`: a platform, partner, regulator or lawyer, reached through the founder.

3. **`when`** it must be answered. These rules are the coordinator's own, a reading:
   - `model`: `before build`, since the architecture reads the model before anything is built;
   - `engineering`: `before build` for an architecture decision, `later` for a build detail;
   - `founder`: `before build` when the decision binds the architecture's structure (the company, its markets, whether Sharrwah's own company runs a service), `before release` when it is commercial (plans and prices, agreements and partners);
   - `subject:S-NN`: `before build` where `architecture/plan.md`, section 3, says the subject binds every area (S-03's contracting company, S-09's currency of records), `before release` otherwise, since a subject's answer is bound per market;
   - `outside`: `before release`;
   - with several answerers, the earliest; `unclear` where none of these applies.

4. **`time_bombs`,** by Q3's four types, as these rules decide (the coordinator's own):
   - `bundles`: its parts have different answerers or different times;
   - `wrong party`: as worded, it asks a party that can't answer it. It asks what the platforms do about something only a market, the founder or engineering settles, or it asks for a decision about something the class's evidence already settles. Its lane isn't read, so judge by its words;
   - `wrong time`: its `needed_by` and its `when` disagree, reading `model`, `spine` and `slice` as before build, `launch` as before release, and `later` as later;
   - `market fact`: it asks what the product should do, where the answer is a fact of a market.

5. **`basis`:** the ids each answer rests on: the capabilities and the cell keys that answer it; the statement keys of a held miss; the subject's id; the founder's decision row by its date.

6. **`what_would_settle_it`:** for `partly`, `unclear` and `candidate miss: not held`.

## Rules

- Every claim is one of three (`PLAN.md`, section 6): a fact, traced to its key; a reading, marked as one; an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, the row is `unclear`, with what would settle it.
- A covered row is covered by what the cells hold, whatever their placement: a capability with nothing held on one platform still answers a question about the class, and the cells say who holds what.

## How to work, keeping your context small

- `python3 -I method/q3.py slice --rows <set:id,...>`, or `--area <AREA> --set km|pay --from N --to M`: each row with the capabilities of its area, and others that share the question's rarer words, with each one's kind, count and placements. A lead list, not an answer.
- `python3 -I method/class_slice.py model --domain <D> --areas <AREA>`: the capabilities and their cells, when you need a cell's reading.
- `key <key>` for one statement; `search <terms> --platform <p>` for a candidate miss.
- Append your rows to `studies/class-model/q3-check.tsv` a few at a time; create it with its header if it doesn't exist. Don't print the file back.

## Output

`studies/class-model/q3-check.tsv`, tab-separated, a header row, no quoting; no tab or newline inside a field:

`set` · `row_id` · `needed_by` (the row's own) · `result` · `cap_ids` (`;`-separated) · `who_answers` · `when` · `time_bombs` (`;`-separated, or empty) · `basis` · `what_would_settle_it`

Check your batch with `python3 -I method/q3.py check --rows <your rows>` until it prints no problem.

Add a section for your batch to `studies/class-model/q3/notes.md`: rows that were hard to place and why, the candidate misses with what you searched, and problems with this brief or the evidence.

## Report

Back to the coordinator:
- your rows' count by result;
- each candidate miss, with its keys or what you searched;
- the time bombs;
- any problem;
- the checker's final line.

After the last batch, the coordinator lists the capabilities no row asks about (Q3's item 3, `q3.py unasked`), amends the model from the held misses, and has the check reviewed with the rest of the extent.
