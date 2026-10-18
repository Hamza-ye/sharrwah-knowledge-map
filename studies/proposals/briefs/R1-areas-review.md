# Brief: independent review of the areas list (step R1)

**Status: draft, for the check before the founder's go on the plan change.**

You review the areas list before it reaches the founder. You made none of it.

**Read only:**
- this brief;
- `studies/proposals/areas/`: the five extracts, the five platforms' areas files and notes, and the coordinator's merged list (`areas.tsv`, `areas.md`, `depth.tsv`);
- `studies/proposals/questions.md`;
- where you need to settle a doubt, the cited source at its commit.

## What to check

1. **The platforms' own names.** Every name in `areas.tsv` and the platforms' files is in its extract, verbatim, from the list it says. Rerun `python3 -I method/check_areas.py <platform>` for each platform.
2. **Groupings.** Each grouping that isn't the platform's own is marked as the agent's or the coordinator's, with its reason. Look for groupings that hide a difference between platforms, or that join things one platform keeps apart.
3. **Nothing lost.** Every in-scope inventory entry and every concern is under an area, or under none with a reason that holds. Legal, place and eligibility matters each have an area wherever the extracts show them.
4. **Plain lines.** Each says what the area covers, in plain words, without ranking, recommending, or using a platform's term as if it were everyone's.
5. **What a "won't do" mark removes, and what is kept.** For each area, `areas.md` says what marking it "won't do" would drop from the work, and which evidence the section B proposals keep anyway. Check both against the questions and the files.
6. **What the work would leave out, and why.** Check each reason against the files.
7. **Depth by question.** For each question, `depth.tsv` gives the platforms to read in depth, the platforms only to check, and why. Check each "why" against the recorded data it cites. Flag a platform whose recorded material suggests an answer the in-depth platforms might not show.

## Output

Write `studies/proposals/areas/review.md`, with findings numbered from 1. Each finding gives:
- where it is;
- the problem;
- the evidence;
- the fix;
- its severity: `must fix` if the founder would mark scope on a wrong basis, otherwise `optional`.

End with a verdict: whether the list can go to the founder.

Run Python with `python3 -I`. Run nothing from inside `evidence/` or the observed repositories. Change no other file, and don't commit.
