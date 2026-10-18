# Brief: independent review of the areas list (step R1)

**Status: revised after its check (`studies/proposals/checks/R1-review-brief-check.md`).**

You review the areas list before it reaches the founder. You made none of it. You run at `max` effort.

The list is for the founder to mark what Sharrwah won't do and what it must. With the founder's marks, it becomes Sharrwah's whole extent for the design of its first build. It also decides what each question's recording runs start from.

## Read

- this brief;
- `studies/proposals/questions-for-agents.md`, the questions as agents get them;
- in `studies/proposals/areas/`:
  - the coordinator's merged list, `areas.tsv`, the depth choice, `depth.tsv`, and the founder's version, `areas.md`;
  - each platform's areas file, `areas-<platform>.tsv`, and its notes, `areas-<platform>-notes.md`;
  - the five extracts and the entries files, **only to settle a particular doubt**, by searching them. Don't read them whole: the scripts check the names and the placing;
- the recorded data, only as far as `depth.tsv` cites it and as far as you sample it:
  - the concern map's `concerns.tsv`, `statements.tsv` and `gaps.tsv`, in `studies/concern-map/platforms/<platform>/`;
  - its `citations.tsv`, only for the citation ids you need;
  - the pilot's statements, `studies/subjects/S-01/<platform>/statements.tsv`.

**To read a cited source:**
- a source in an observed repository is read from git's objects, from outside the repository: `git --git-dir=/home/user/observed-sh/.git show <commit>:<path>`, or `observed-sa`;
- a live page is usually held in this repository's capture runs. Run `python3 -I method/held_index.py <url>` to find it.

## The files you review

All are tab-separated, with a header row, no quoting, and `;` between items in a field. Platform names are lower case (`shopify`, `salla`, `woocommerce`, `zid`, `bigcommerce`).

**`areas.tsv`:**
- `area_id`: `A-01` and on;
- `heading`, and `heading_source`. The source is either a platform and a label, as `shopify [Help Center]`, when the heading is that platform's own name, or `coordinator's own`;
- `plain_line`;
- `platform_area_ids`: the platform areas it holds;
- `questions`: the questions (`Q1` to `Q8`) that draw on it. A question's recording runs start from the concerns of these areas as candidates. Each run marks which candidates bear on its question, sets the others aside with a reason, and may add concerns from other areas. Only then are the statements copied;
- `wont_do_removes`: what a "won't do" mark would remove;
- `kept_anyway`: what evidence the questions keep from it even then;
- `left_out`: for an area no question draws on, why the work doesn't read it. This is about the work's reading, not Sharrwah's extent: only the founder's marks decide what is outside Sharrwah;
- `note`: for a heading of the coordinator's own, why.

**`depth.tsv`:** one row per question and platform:
- `question`, `platform`;
- `depth`: `in depth` or `check`. The founder took no cuts, so every platform is read for every question;
- `why`;
- `cites`: concern ids (`SH-C-001`), citation ids (`SH-S-0001`) or pilot statement ids (`S01-SH-001`).

**`areas.md`** is written from these files by `method/render_areas.py`.

**A platform's own names** (`method/areas_extract.py`, `own_names`) include:
- a list's entries, and each part of an entry's path (" › " or " > ");
- each half of an English / Arabic pair;
- entries out of the concern map's scope;
- concerns' terms;
- Shopify's Help Center menus and Salla's help-centre categories.

## What to check

1. **The checks by script.** Run `python3 -I method/check_areas.py <platform>` for each platform, `python3 -I method/check_areas.py merged`, and `python3 -I method/render_areas.py` into a scratch copy, comparing it with `areas.md`. Report anything they find.
2. **Groupings.**
   - Each grouping that isn't the platform's own is marked as the agent's or the coordinator's, with its reason.
   - Look for groupings that hide a difference between platforms, or that join things one platform keeps apart.
   - Look also for one thing split across areas: the same platform feature, or the same kind of thing on two platforms, put in different merged areas.
   - Each merge of platform areas should rest on the platforms' own names, or be marked as the coordinator's own.
3. **Nothing lost.** A loss here becomes a loss in Sharrwah's extent. "Nothing lost" counts:
   - **every concern:** under an area, or under none with a reason that holds;
   - **every in-scope inventory entry:** the entries files place them by script, so check only the entries the platforms' notes flag;
   - **the entries out of the concern map's scope:** they aren't placed, and each carries the concern map's reason. Sample about 20 across the platforms, including Shopify's "Unplaced" store-feature keys. Report any that holds something the platforms offer which no area covers;
   - **Shopify's top-level Help Center menus and Salla's help-centre categories:** each falls in some area, by name or by the area's plain line;
   - **legal, place and eligibility matters:** each has an area wherever the extracts show them.
4. **Plain lines and plain words.**
   - Each plain line says what the area covers, in plain words. It doesn't rank, recommend, or use one platform's term as if it were everyone's.
   - No heading or plain line of the coordinator's or an agent's uses a category of ours or the founder's working words: "market", "availability", "conditions", "manual payment", "parts", or others like them. The exception is a platform's own name, marked as the platform's.
   - `areas.md` is in plain business words. Any term it can't avoid is defined in one line.
5. **What each question draws on.**
   - For each question, the areas tied to it should hold, as candidates, the recorded concerns that bear on it.
   - Sample about 10 statements for each question and platform, from the concerns of areas tied to it and of areas not tied to it. Name the areas a question should draw on but doesn't.
   - Name the ties that would only add candidates for runs to set aside. These matter less: a run can set aside, and can add from other areas.
6. **What a "won't do" mark removes, and what is kept.** For each area, check both against the questions and the files.
7. **What the work doesn't read, and why.** Check each `left_out` reason against the files.
8. **Depth by question.**
   - Check each "why" in `depth.tsv` against what it cites. Sample about 5 statements for each row.
   - Weigh each platform's recorded statements and gaps for the question: thin records, or many gaps, on a platform read only as a check is a finding.
   - Flag a platform marked `check` whose recorded material suggests an answer the in-depth platforms might not show.

## Output

Write `studies/proposals/areas/review.md`, with findings numbered from 1. Each finding gives:
- where it is;
- the problem;
- the evidence;
- the fix;
- its severity:
  - `must fix`: the founder would mark scope on a wrong basis, something the platforms offer would be missing from the list, or a question would start without what bears on it;
  - `optional`: otherwise.

End with a verdict: whether the list can go to the founder.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/` or the observed repositories.
- Write scratch files only in the scratch directory the message that started you names.
- Change no other file, and don't commit.
