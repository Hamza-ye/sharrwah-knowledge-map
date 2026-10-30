# Brief: the independent review of the class's model's extent (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A: after Q3's check, "an independent review of the whole extent, by an agent that made none of it." You are one reviewer with one batch of one share of the model; your message names the share, the batch and the commit of the selection. You made none of the model, and you check it against the evidence, not against what its parts or its coordinator say.

**The review is by risk, not every row** (`studies/class-model/method-report.md`, sections 7 and 13; the inspection of this brief, `inspection-Q3R.md`, part 2). `method/review_select.py` chose the items where an error would change what the model says, once, after the last merge, and wrote them to `studies/class-model/review/selection.tsv` at the commit your message names. Your items are the rows with your share and batch. Review every one; where an item leads you to a row outside your batch that is wrong, say so in your findings.

**Read only this brief and:**
- `studies/class-model/briefs/B-extent.md`: the rules the parts followed, its conventions and its "Maker evidence" among them;
- `studies/class-model/review-dry-run-rulings.md`: the dry run's rulings (C1 to C7, S1 to S17) and conventions;
- `studies/class-model/method-report.md`, sections 11 to 13: the coordinator's rules since;
- the merged model, `studies/class-model/merged/` (with `flags.tsv`, the merge's questions), and the parts' own files and `notes.md` in `studies/class-model/parts/`, for the readings and the flags each part answered;
- Q3's check, `studies/class-model/q3/check-*.tsv` and `notes-*.md`, and its brief `briefs/Q3-check.md`, for the items of reason `q3`;
- the evidence, through `method/class_slice.py` (`key`, `statements`, `search`, `outscope`, `gaps`, `candidates`, `homonyms`, `model`, `caps`) and `method/q3.py where`; and the evidence repositories' guides (their `README.md` and `docs/READING.md`) where a statement's words are in doubt and its source needs reading at its commit.

## What each reason asks

An item is a cell (a capability on one platform) with every reason it was chosen, or a question that isn't one cell. Answer each reason the item carries.

- **kind:** a cell its capability's kind hinges on. For a class whose count is one: would the cell's statements still make it the platform's own? Is it another capability's thing, in any domain (`caps --terms`, in both languages)? For a cell of a slot or an open: does the platform do it itself after all? Read `candidates` and search, in every language the platform uses (for Salla and Zid, in Arabic too, singular and plural, with and without ال), then `outscope`.
- **count:** a cell of a class held with statements but placed neither `core` nor `own-service`. Does the platform place it in its core after all, by the conventions: its own API for its own feature (C1), a released flag (C6), a staff permission (S7)?
- **none-held:** nothing held, while one of the platform's statements holds two or more of the other platforms' terms. Read the leads `candidates` gives; is the cell right?
- **role**, **terms-homonym:** a landing joined on role, a reading, or on a term Q1 lists as a homonym. Do the two sides play the same part in each platform's own words? If not, where does the concern belong?
- **own-service:** a placement as the platform company's own service. Does a statement name the company as the maker or provider (the dry run's ruling C5; `B-extent.md`, "Maker evidence")? A brand in a product's name doesn't, and a note never counts. A statement naming the company as a service's provider may count for each feature of that service that a cell's own statements show.
- **scope:** a class that holds only under a plan, a beta or one observed store (convention 11). Is its scope right, and is it a class there?
- **strained:** a capability with landings marked strained. Should a concern be split out, and where?
- **flag:** a question the merge leaves (`merged/flags.tsv`):
  - *counted twice:* one statement supports `core` or `own-service` in two domains. Do its words name each capability's thing? Where they name several things (a list, a route pattern, a webhook topic that is also an instance of the webhook mechanism, a maker statement for several features of one service), it counts in each. Where they name one thing that two domains each hold, that is one capability: answer as for *one capability?* (convention 8: nothing counts twice). The flags where no cell rests on the statement alone come as one item: settle them together by this rule.
  - *ruled differently:* two domains rule one pair of Q1's unclear concerns differently. Each domain rules from its own cells (S3). Does each ruling follow S3? If both do, the pair is one thing in the model wherever it is `joined`, and the verdict is `holds`. It is `wrong` only where a ruling breaks S3, or where the `joined` capability doesn't show both sides as one thing.
  - *one capability?:* two capabilities of two domains share terms. Are they one thing? If so, which domain holds it ("One thing, one domain")?
  - *strained?:* a clean landing whose statement, held under another concern too, is cited in another tree. Strained, unless the statement is general.
- **coordinator:** a row the coordinator wrote or changed, or a line of a part's notes that names the coordinator (a correction, a move, a statement counted once, a lead cited, a row taken out). Check it as you would a part's row. The coordinator's reason is in the part's `notes.md`: search it for "the coordinator".
- **lead:** a line of a part's notes that names the final review or the reviewer, or a capability whose cells cite only inventory entries. Answer the question the line raises; for the second, is it a capability, or does it fold into its parent?
- **q3:** a row of Q3's check. Does its result hold on the model's cells and the concern map (search as `Q3-check.md` asks, with `q3.py where`)? Are its answerers and time those its rules give?
- **sample:** a cell chosen at random from its part. Check its placement, its evidence and its reading.

For every item, check that each fact traces to its key, that a reading is marked as one, and that no statement the cell needs is left uncited. Read a statement's source at its commit only where its words are in doubt.

## Rules

- Every claim is one of three (`PLAN.md`, section 6): a fact traced to its source at a commit; a reading, marked as one; an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Don't change the model's files. Write findings; the coordinator corrects.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, say what would settle it.

## How to work, keeping your context small

- `python3 -I method/class_slice.py model --domain <D> --areas <AREA>` prints a capability's cells; `key <key>` reads one statement; `search`, `outscope`, `candidates` and `caps` look further; `q3.py where <key>` says which cells cite a statement.
- Work through your items in order, and append your verdict on each to your coverage file as you go, a few at a time. Don't print files back.

## Output, in `studies/class-model/review/`

- `coverage-<share>-<batch>.tsv`, tab-separated, a header row, no quoting: `item` · `verdict` (`holds`, `wrong` or `unclear`) · `severity` (for `wrong` only: `kind` where a kind or count changes, `structure` where a landing, a parent, a capability or a concern's domain changes, `placement` where a cell's placement changes, `reading` where only a reading or a note does) · `basis` (the keys you read, `;`-separated) · `correction` (for `wrong` only: `<part>/<file>`, the row by its `cap_id` and `platform`, its `concern_id` or its `key`, and the new value) · `what_would_settle_it` (for `unclear`).
- `findings-<share>-<batch>.md`: each `wrong` and `unclear` item, with its evidence and the correction you propose; then any pattern across items (a convention read two ways, a kind of error that recurs); then problems with this brief.

Check your coverage with `python3 -I method/review_select.py check --share <share> --batch <batch>` until it prints no problem.

## Report

Back to the coordinator: your items' count by verdict; each `wrong` item of severity `kind` or `structure`; the patterns; any problem; the checker's final line.
