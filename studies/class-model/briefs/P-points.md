# Brief: the subjects' variation points on the class's model (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A, "The subjects' points": "After the merge, the coordinator lands S-01's and S-02's variation points on the capabilities their concerns and terms point to, each a reading. [...] Where a point and the model conflict, the point is reopened with its evidence, not forced to fit (the founder, 30 October). An engineering ruling is ruled again on that evidence, and listed for the founder's veto. A founder's own decision, such as S-01's Decision 1, isn't reopened by engineering: the conflict comes to the founder with its evidence." You draft the landings of one batch of points for the coordinator, who checks each and owns its reading. Your message names your batch.

**What a point is.** A subject's variation point is a place where the class varies by market: a question in the platforms' own words, such as S-01's "who or what fills 'holds the funds'" or S-02's "what 'currency' takes its value per". Its variants are each platform's answers, from the subject's statements. The subject's register then rules on it: a founder's decision, an engineering ruling or constraint, a row moved to another subject, or a row that follows by rule.

**What landing it means.** Naming the capability of the model whose thing the point's question is about: where the model carries the point. The architecture reads it there, to see which capabilities vary by market and why.

**Read only this brief and:**
- `method/land_points.py` (`python3 -I method/land_points.py --help`): `show --points <ids>` prints, in one view, a point's question, the register rows that name it with their answer and status, the subject's own analysis of it, its variants per platform, and its leads, each with its cells. A lead is a capability the point's statements point to by one of four routes: `cited` (a cell cites the concern map's statement the subject's statement comes from), `concern` (that statement's concern lands there), `page` (the subject read its statement on a page the concern map's statements of a concern also cite), `terms` (the capability's names or cells hold the point's own terms);
- the model, through `method/class_slice.py` (`model`, `key`, `search`, `caps`) and `method/q3.py where`;
- the subject's own files where the view leaves a variant in doubt: `studies/subjects/<S>/variants.tsv`, `register.tsv`, `analysis.tsv` (S-01) or `answers.tsv` (S-02), and a platform's `statements.tsv` and `citations.tsv`, one row at a time, found by its id. Never load a file whole;
- `founder-decisions.tsv`, whole, for which decisions are the founder's own.

## For each point

1. **`cap_ids`:** the capability whose thing the question names, the main one first. Add others where the point's thing spans capabilities, or where the platforms answer it in different capabilities. A lead is only a lead: the capability must be the thing the question asks about, as its cells' readings and the statements' words show. A point about who fills a role (S-01's) lands on the capability whose cells hold that role. Where no capability is the point's thing, write `none`, with a `structure` conflict.
2. **`route` and `basis`:** the routes that led you there, and their basis: the concern map's keys a cell cites (`concern/placement/cite`), `concern:<id>` for a concern's landing, or `term:<term>`.
3. **`reading`:** why it lands there, in a sentence or two, marked as a reading.
4. **`register`:** the register rows that name the point, as `show` lists them, `; `-separated, in that order.
5. **`conflict`:** compare, platform by platform, what the subject's variants and analysis say each platform does with what the landing capability's cells say. They differ in grain: the subject asks per market, the cells ask who does it and where. A cell that says nothing about markets doesn't conflict with a variant that does. A conflict is one of four:
   - `count`: the subject's statements show a platform doing the thing itself (its own admin, setting, API or terms) or as its company's own service, where the landing capability's cell on that platform is not `core` or `own-service`: `none-held`, `not-stated`, or only `extension-point`, `outside` or `shows`. If they hold, the capability's count changes, and maybe its kind. Name the subject's statement ids and the cell;
   - `placement`: the two say different things about who does it on one platform. One says the platform itself, the other a third party or the merchant; or the subject's variant is a confirmed absence where the cell holds the thing `core`. Name both sides' statements;
   - `structure`: no capability is the point's thing; or the point's variants show that two capabilities are one thing, or that one capability holds two things the platforms tell apart;
   - `premise`: a register row that names the point rests on a claim about the class (what every platform does, or that no reference does a thing) that the model's cells contradict. Name the row and the cells.

   Write `none`, or `<type>: <what>`, several separated by ` | `. Don't decide which side is right: the coordinator reads both. Where the statements plainly bear one side out, say so as a reading. Where a subject holds a platform's statements and the cell holds nothing, that is a `count` conflict only if they show the platform doing the thing itself; otherwise note it for the coordinator, since the subject read sources the concern map didn't hold.
6. **`status`:**
   - `landed`, with conflict `none`;
   - `to the founder`, where a conflict touches a founder's own decision: a register row whose status says the founder settled or decided it (S-01's Decision 1 and its defaults, the rows settled by Decision 1's answer, and the rows the founder decided to keep), or a decision in `founder-decisions.tsv`;
   - `reopened`, for every other conflict. That covers an engineering ruling (S-02's D1 to D9 and E1 to E5 are engineering's rulings, which the founder didn't veto, and S-01's rows "proposed, engineering"), a row moved to another subject, and the model itself.

## Rules

- Every claim is one of three (`PLAN.md`, section 6): a fact traced to its key; a reading, marked as one; an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, say what would settle it.
- Don't change the model's files or the subjects'. Write your batch's files only, make no commits, and run Python with `python3 -I`.

## How to work, keeping your context small

- `show --points` two or three points at a time. Use `class_slice.py model --domain <D> --areas <AREA>` only where a cell's clipped reading doesn't settle it, and `key` for one statement.
- Write your batch's file as you go, a few rows at a time. Don't print it back.

## Output, in `studies/class-model/points/`

- `<batch>.tsv`, tab-separated, a header row, no quoting, no tab or newline inside a field: `subject` · `vp_id` · `question` (exactly as the subject words it) · `cap_ids` (`;`-separated) · `route` (`;`-separated) · `basis` (`;`-separated) · `reading` · `register` · `conflict` · `status`.
- `notes-<batch>.md`: the points that were hard to land and why; each conflict, with both sides' evidence; the leads the checker prints and what you made of them; problems with this brief or the script.

Check with `python3 -I method/land_points.py check --batch <batch>` until it prints no problem. Its `lead:` lines (the subject holds a platform's statements where the landing cell holds none) are for you to read for a `count` conflict: answer each in your notes.

## Report

Back to the coordinator: your points' count by status; each conflict, with its type, point and both sides; any problem; the checker's final line.

## After the batches

The coordinator checks every batch and reads each conflict's evidence. An engineering ruling is ruled again and listed for the founder's veto. The model is amended through `<domain>-amend` parts. A conflict with the founder's own decision goes to the founder at GM, with its evidence. The final review then reads the points with the rest of the extent.
