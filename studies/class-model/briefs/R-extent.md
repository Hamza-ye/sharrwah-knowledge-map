# Brief: the independent review of the class's model's extent (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A: after Q3's check, "an independent review of the whole extent, by an agent that made none of it." You are one reviewer with one share of the model; your message names it. You made none of the model, and you check it against the evidence, not against what its parts or its coordinator say.

**The review is by risk, not every row** (`studies/class-model/method-report.md`, sections 7 and 13). `method/review_select.py` chose the items where an error would change what the model says, and wrote them to `studies/class-model/review/selection.tsv`. Your share's items are the rows with your share's number. Review every one of them, and nothing else unless an item leads you to it.

**Read only this brief and:**
- `studies/class-model/briefs/B-extent.md`: the rules the parts followed, its conventions among them;
- `studies/class-model/review-dry-run-rulings.md`: the dry run's rulings and conventions;
- `studies/class-model/method-report.md`, sections 11 to 13: the coordinator's rules since, a statement counted once, one thing in one domain;
- the merged model, `studies/class-model/merged/`, and the parts' own files and `notes.md` in `studies/class-model/parts/`, for the readings and the flags each part answered;
- the evidence, through `method/class_slice.py` (`key`, `statements`, `search`, `model`, `caps`), and the evidence repositories' guides (their `README.md` and `docs/READING.md`) where a statement's source needs reading at its commit.

## What each kind of item asks

- **kind:** a cell its capability's kind hinges on. Is its placement right, on its statements? For a class with a count of one, would the cell's statements still make it the platform's own? For a cell of a slot or an open, does the platform do it itself after all: search for it, in every language the platform uses (for Salla and Zid, in Arabic too, singular and plural, with and without ال), and read what you find.
- **role:** a landing joined on role, a reading. Do the two sides play the same part in each platform's own words? If not, where does the concern belong?
- **own-service:** a placement as the platform company's own service. Does a statement name the company as the maker or provider (convention 5)? A brand in a product's name doesn't, and a note never counts.
- **flag:** a question the merge leaves for you:
  - *counted twice:* one statement supports `core` or `own-service` in two domains. Where do its words belong? It counts there, and shows elsewhere.
  - *ruled differently:* two domains rule one pair of Q1's unclear concerns differently, each from its own cells. Give the one answer the whole model's cells support.
  - *one capability?:* two capabilities of two domains share terms. Are they one thing? If so, which domain holds it ("One thing, one domain")?
  - *strained?:* a clean landing whose statement, held under another concern too, is cited in another tree. Strained, unless the statement is general.
- **coordinator:** a row the coordinator wrote or changed between batches: a correction, a move, a statement counted once, a lead cited. Check it as you would a part's row; the coordinator's reason is in the part's `notes.md`, under "The coordinator's corrections".
- **sample:** a cell chosen at random. Check its placement, its evidence and its reading.

For every item, check that each fact traces to its statement at its commit, that a reading is marked as one, and that no statement the cell needs is left uncited.

## Rules

- Every claim is one of three (`PLAN.md`, section 6): a fact traced to its source at a commit; a reading, marked as one; an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Don't change the model's files. Write findings; the coordinator corrects.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, say what would settle it.

## How to work, keeping your context small

- `python3 -I method/class_slice.py model --domain <D> --areas <AREA>` prints a capability's cells; `key <key>` reads one statement; `search` and `caps` look further.
- Work through your items in order, and append your verdict on each to your coverage file as you go, a few at a time. Don't print files back.

## Output, in `studies/class-model/review/`

- `coverage-<share>.tsv`, tab-separated, a header row, no quoting: `item` · `verdict` (`holds`, `wrong` or `unclear`) · `severity` (for `wrong`: `kind` where the kind or count changes, `placement` where a cell's placement changes, `reading` where only a reading or a note does) · `basis` (the keys you read) · `correction` (for `wrong`: what the row should say) · `what_would_settle_it` (for `unclear`).
- `findings-<share>.md`: each `wrong` and `unclear` item, with its evidence and the correction you propose; then any pattern across items (a convention read two ways, a kind of error that recurs); then problems with this brief.

## Report

Back to the coordinator: your items' count by verdict; each `wrong` item that changes a kind or a count; the patterns; any problem.
