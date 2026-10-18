# Brief: independent review of the areas list (step R1)

**Status: draft, revised after the check of the drafts (`studies/proposals/check-of-the-draft.md`). It is checked again before it runs.**

You review the areas list before it reaches the founder. You made none of it. You run at `max` effort.

**Read only:**
- this brief;
- `studies/proposals/questions.md`;
- in `studies/proposals/areas/`:
  - the five extracts;
  - the five platforms' areas files, their notes, and their entries files;
  - the coordinator's merged list, `areas.tsv`, its account for the founder, `areas.md`, and the depth choice, `depth.tsv`;
- the recorded data, only as far as `depth.tsv` cites it, and as far as you sample it to test a claim:
  - `studies/concern-map/platforms/<platform>/concerns.tsv` and `statements.tsv`;
  - the pilot's `studies/subjects/S-01/<platform>/statements.tsv`;
- where you need to settle a doubt, the cited source at its commit. Read a held source from git's objects, from outside its repository: `git --git-dir=/home/user/observed-sh/.git show <commit>:<path>` (or `observed-sa`).

## The coordinator's files

**`areas.tsv`**, tab-separated, no quoting:
- `area_id`: `A-01` and on;
- `heading`, and `heading_source`: either a platform and a label, as `shopify [Help Center]`, when the heading is that platform's own name, or `coordinator's own`;
- `plain_line`;
- `platform_area_ids`: the platform areas it holds, `;`-separated;
- `questions`: the questions (`Q1` to `Q8`) that draw on it. A script copies the statements under its concerns for each of these questions;
- `wont_do_removes`: what a "won't do" mark on it would remove from the work;
- `kept_anyway`: what evidence the questions keep from it even then;
- `left_out`: for an area no question draws on, why the work leaves it out. This is its "line, with the reason";
- `note`: for a heading of the coordinator's own, why.

**`depth.tsv`**: one row per question and platform:
- `question`, `platform`;
- `depth`: `in depth`, `check`, or `none`;
- `why`;
- `cites`: the concern or statement ids the reason rests on.

**`areas.md`**: the same list for the founder, in plain words, with the depth choice and its reasons.

## What to check

1. **The checks by script.** Run `python3 -I method/check_areas.py <platform>` for each platform, and `python3 -I method/check_areas.py merged`. Report anything they find.
2. **Groupings.**
   - Each grouping that isn't the platform's own is marked as the agent's or the coordinator's, with its reason.
   - Look for groupings that hide a difference between platforms, or that join things one platform keeps apart.
   - Each merge of platform areas rests on the platforms' own names, or is marked as the coordinator's own.
3. **Nothing lost.**
   - Every concern is under an area, or under none with a reason that holds.
   - Every inventory entry is placed, and the entries each platform's notes flag are dealt with.
   - Legal, place and eligibility matters each have an area wherever the extracts show them.
4. **Plain lines and plain words.**
   - Each plain line says what the area covers, in plain words. It doesn't rank, recommend, or use a platform's term as if it were everyone's.
   - `areas.md` is in plain business words. Any term it can't avoid is defined in one line.
5. **What each question draws on.**
   - For each question, the areas marked as drawing on it should hold the recorded material that bears on it, and not much else.
   - Sample the recorded statements to test this. Name the areas a question should draw on but doesn't, and those it draws on without need.
   - This decides what a script copies for each question, so a miss here is a miss in every later step.
6. **What a "won't do" mark removes, and what is kept.** For each area, check both against the questions and the files.
7. **What the work would leave out, and why.** Check each `left_out` reason against the files.
8. **Depth by question.**
   - Check each "why" in `depth.tsv` against what it cites.
   - Flag a platform marked `check` whose recorded material suggests an answer the in-depth platforms might not show.

## Output

Write `studies/proposals/areas/review.md`, with findings numbered from 1. Each finding gives:
- where it is;
- the problem;
- the evidence;
- the fix;
- its severity: `must fix` if the founder would mark scope on a wrong basis, or a question would miss what bears on it; otherwise `optional`.

End with a verdict: whether the list can go to the founder.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/` or the observed repositories.
- Change no other file, and don't commit.
