# Brief: the subjects' variation points on the class's model (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A, "The subjects' points": "After the merge, the coordinator lands S-01's and S-02's variation points on the capabilities their concerns and terms point to, each a reading. [...] Where a point and the model conflict, the point is reopened with its evidence, not forced to fit (the founder, 30 October). An engineering ruling is ruled again on that evidence, and listed for the founder's veto. A founder's own decision, such as S-01's Decision 1, isn't reopened by engineering: the conflict comes to the founder with its evidence." You draft the landings of one batch of points for the coordinator, who checks each and owns its reading. You record each conflict and the register rows it bears on; the coordinator settles it and routes it. Your message names your batch (`python3 -I method/land_points.py batches`).

**What a point is.** A subject's variation point is a place where the class varies by market: a question in the platforms' own words, such as S-01's "who or what fills 'holds the funds'" or S-02's "what 'currency' takes its value per". Its variants are each platform's answers, from the subject's statements. The subject's register then rules on it: a founder's decision, an engineering ruling or constraint, a row moved to another subject, or a row that follows by rule.

**What landing it means.** Naming the capability of the model whose thing the point's question is about: where the model carries the point. The architecture reads it there, to see which capabilities vary by market. The cause and the binding time stay in the subject's analysis, found by the point's id: don't copy them.

**Read only this brief and:**
- `method/land_points.py` (`python3 -I method/land_points.py --help`):
  - `show --points <ids>` prints a point in one view: its question and terms, the register rows that name it with their answer and status, the subject's own analysis, its variants per platform with how many of each platform's statements trace to the concern map, and its ranked leads, each with the statements behind each route, its basis and its cells' clipped readings. Read each point's view once. If it prints a warning that a domain's files changed after the last merge, stop and tell the coordinator.
  - `cell <cap_id> <platform>` prints one cell whole: its placements, its reading, every evidence row with what each statement supports, and the capability's slot fillers.
  - A lead is a capability the point's statements or terms point to, by one of four routes: `cited` (a cell cites the concern map's statement the subject's statement comes from), `concern` (that statement's concern lands there), `page` (the subject read its statement on a page the concern map's statements of a concern also cite), `terms` (the capability's names or cells hold the point's own terms). A lead is only a lead.
- `studies/class-model/briefs/B-extent.md`, its "Cells and evidence" and "Conventions from the dry run": the model's rules for what places a cell `core` or `own-service`;
- the model, through `method/class_slice.py` (`key`, `search`, `outscope`, `caps`) and `method/q3.py where`;
- the subject's own files where the view leaves a variant in doubt: `studies/subjects/<S>/variants.tsv`, `register.tsv`, `analysis.tsv` (S-01) or `answers.tsv` (S-02), and a platform's `statements.tsv` and `citations.tsv`, one row at a time, found by its id. Never load a file whole;
- `founder-decisions.tsv`, whole, for which decisions are the founder's own;
- `architecture/plan.md`, section 3, for the decisions that cut across every area.

## For each point

1. **`cap_ids`:** the capability whose thing the question names, the main one first. Add another only where the platforms answer the question in different capabilities, or its thing is two capabilities' at once. The capability must be the thing the question asks about, as its cells' readings and the statements' words show: a "what X takes its value per" lands on X, not on Markets, unless X is the market itself. A point about who fills a role (S-01's) lands on the capability whose cells hold that role. Where a platform's statements trace to nothing (`show` says so), search for its thing (`caps`, `search`) before you land. Where no capability is the point's thing, write `none`, with a `structure` conflict.
2. **`reach`,** a reading: `capability`; or `cross-cutting: <decision>`, where the point's own thing is held in every area, as every amount names a currency, every contract a contracting party, every store a country. A point whose value is merely held through the configuration or the market mechanism is `capability`. The decision is one the architecture plan's section 3 names, in its words: `how stores are kept apart`, `identity and permissions`, `money records and currency`, `markets and the seller's country`, `events and extension points`, `configuration`. The main capability is still named in `cap_ids`.
3. **`route` and `basis`:** the routes that led you there, `;`-separated, and their basis, each item one of three: a key (`concern/placement/cite`, or an inventory id) that a cell of a landing capability cites; `concern:<id>`, a concern landed in one of them; `term:<term>`, one of the point's own terms. Each route needs an item of its form, and each item its route: `cited` a key, `concern` and `page` a `concern:`, `terms` a `term:`. For `none`, the basis is the leads you set aside, a `concern:` first where there is one.
4. **`reading`:** why it lands there, in a sentence or two, marked as a reading.
5. **`register`:** the register rows that name the point, as `show` lists them, `; `-separated, in that order.
6. **`conflict`:** compare, platform by platform, what the subject's variants and analysis say each platform does with the cell of the landing capability the platform's variants answer in (`cell` shows it whole). They differ in grain: the subject asks per market, the cells ask who does it and where. A cell that says nothing about markets doesn't conflict with a variant that does. Four types, which don't overlap:
   - `count`: the subject's statements would place the platform `core` or `own-service` by the model's own rules (`B-extent.md`, "Cells and evidence" and its conventions, read as they are written there; `own-service` only on a statement naming the company as the maker or provider), and the cell is placed otherwise or holds nothing. A platform's terms that give the merchant's or buyer's duties, or state the agreement's own terms, support no placement, so they make no `count`. A capability of the kind `open` (one whose cells show it but place it on no platform) is placed so by the model's rule: compare its cells as any other's;
   - `placement`: the cell is `core` or `own-service`, and the subject's statements show a third party doing it, the merchant doing it outside the platform, or a confirmed absence on that platform, where the cell doesn't already place that party `outside` or `extension-point` on that platform;
   - `structure`: no capability is the point's thing; or the point's variants show that two capabilities are one thing, or that one capability holds two things the platforms tell apart;
   - `premise`: a register row that names the point rests on a claim about what the references do or show (that every platform does it, that one does, that none does, or how they carry it) that the model's cells contradict.

   **Who sets a value is not who provides it.** The seller, a staff member or the buyer setting the platform's own setting is the platform's `core`, never a conflict. For a "who sets" point, compare a third party it names (a provider, a gateway, partners, an app) with the capability whose thing that third party does, and only as `placement` defines a difference.

   Write `none`, or each conflict as `<type> (rows: <ids>): <what>`, several separated by ` | `. `<ids>`, comma-separated: the register rows whose answer rests on the subject's side of the conflict, and `model` for the model's side. Name both, unless one side isn't in the comparison: a `premise` conflict names its row, and a `structure` conflict where no row rests on the point's thing names `model`. In `<what>`, name the subject's statement ids and the cell's evidence keys, and say as a reading which side the statements bear out, or what would settle it. Don't decide it: the coordinator does.
7. **`status`:** `landed`, with conflict `none`; or `conflict`.
8. **`outcome`:** leave it empty. The coordinator writes it.

**Notes, for the coordinator:** where a point lands on a capability of the kind `slot`, or one with `outside` cells, list the third parties and laws the subject names as filling it that `cell` doesn't list among the capability's slot fillers. Each is a lead, not a conflict.

## Rules

- Every claim is one of three (`PLAN.md`, section 6): a fact traced to its key; a reading, marked as one; an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, say what would settle it.
- Don't change the model's files or the subjects'. Write your batch's files only, make no commits, and run Python with `python3 -I`.

## How to work, keeping your context small

- `show --points` two or three points at a time, and read each view once. Use `cell` where a clipped reading doesn't settle a comparison, and `key` for one statement.
- Write your batch's file as you go, a few rows at a time. Don't print it back.

## Output, in `studies/class-model/points/`

- `<batch>.tsv`, tab-separated, a header row, no quoting, no tab or newline inside a field: `subject` · `vp_id` · `question` (exactly as the subject words it) · `cap_ids` (`;`-separated) · `reach` · `route` (`;`-separated) · `basis` (`;`-separated) · `reading` · `register` · `conflict` · `status` · `outcome` (empty).
- `notes-<batch>.md`: the points that were hard to land and why; each conflict, with both sides' evidence; the leads the checker prints and what you made of them; the slot fillers above; problems with this brief or the script.

Check with `python3 -I method/land_points.py check --batch <batch>` until it prints no problem. Its `lead:` lines (the subject holds a platform's statements where no landing cell holds any) are for you to read for a `count` conflict, or a capability you missed: answer each in your notes.

## Report

Back to the coordinator: your points' count by status; each conflict, with its type, point, rows and both sides; any problem; the checker's final line.

## After the batches: the coordinator

The coordinator checks every batch, then settles each conflict's fact first, since what a platform does is engineering's to read from the evidence (`PLAN.md`, section 3). Then each conflict on its own:
- where a cell is wrong, the model is amended through a `<domain>-amend` part. A conflict whose only consequence is an amendment to the model goes to no one else;
- where the subject's evidence is wrong, or read wrongly, under an engineering ruling or constraint, the row is ruled again and listed for the founder's veto;
- where the subject's evidence is wrong, or read wrongly, under a founder's decision, the conflict goes to the founder with its evidence, its options and a recommendation, and engineering doesn't reopen the decision. S02-M9's plan items go to the founder with plans and prices;
- under a row moved to another subject, it is carried to that subject as an input, and not ruled now;
- under a row that follows by rule, the rule is applied again;
- where the evidence doesn't settle it, it is kept open, with what would settle it: a capture request in `handoffs/` where a run can capture it (`PLAN.md`, section 6, "Evidence");
- where the conflict doesn't hold, it is dismissed, with why.

The coordinator writes each conflict's outcome, in order, ` | `-separated, each marked "(the coordinator)": `model amended: <part>/<file> <row>`, `re-ruled: <row>, listed for veto`, `to the founder: <item>`, `to the founder with plans: <item>`, `carried to <S-NN>: <what>`, `re-applied: <row>`, `kept open: <what would settle it>`, or `dismissed: <why>`. A conflict the coordinator finds on a point drafted `landed` is added after the drafted ones, marked "(the coordinator)" at its end, with its outcome, and the point's status becomes `conflict`. The drafted conflicts stay as written. `land_points.py check --final` then requires an outcome for every conflict, of a form its rows allow, and the final review reads every point with a conflict, with its outcome.
