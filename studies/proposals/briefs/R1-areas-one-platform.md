# Brief: one platform's broad areas (step R1, run once per platform)

**Status: draft, for the check before the founder's go on the plan change.**

You are one agent with one short task, for one platform. The message that started you names the platform.

**Read only:**
- this brief;
- `studies/proposals/areas/extract-<platform>.md`;
- where a name in the extract is unclear, the passage its `cite_id` points to, in `studies/concern-map/platforms/<platform>/citations.tsv` and the source at its commit. Read only that passage.

## The task

Name the platform's broad areas, the way the platform itself divides what it offers and what it requires.

1. **Use the platform's own names.** Take each area's name from the platform's own lists in the extract: its menus, help-centre sections, settings, plan tables, product lines, legal agreements, country lists, and the concerns' terms. Quote each name exactly as the extract gives it, and say which list it comes from.
2. **Cover what no menu shows.** Some of what a platform requires or allows shows only in its terms, its country lists, its eligibility rules or its plans. That includes legal matters (agreements, the companies that contract, policies), places (where it operates, what differs by country) and eligibility (who may use what, where). Wherever the extract shows these, they get an area, even when no menu names one.
3. **Tens, not hundreds.** Aim for 15 to 30 areas. Where the platform's own names can't bring the list down that far, group further. Mark each such grouping as your own (`grouping` = `agent's own`) and give the reason.
4. **Place everything.** Every in-scope inventory entry and every concern in the extract goes under exactly one area, by its id. Where something fits no area, list it under none, with the reason.
5. **One plain line per area.** It says, in plain words, what the area covers on this platform. It describes. It doesn't rank, compare with other platforms, or say what anyone should build.

**Don't:**
- use any category of ours. That includes the words "market", "availability", "conditions", "manual payment" and "parts", unless the platform itself uses them in the extract. Never use the names of other platforms' areas;
- compare with other platforms. Merging the five lists is the coordinator's step;
- read beyond what this brief names.

## Output, in `studies/proposals/areas/`

**`areas-<platform>.tsv`:** tab-separated, with a header row and no quoting. Columns:
- `area_id`: the platform's code and a number, as `SH-A-01`;
- `platform_names`: each name exactly as the extract gives it, `;`-separated, each followed by its list in brackets, as `Payments [other:help-center-sections]`;
- `plain_line`;
- `grouping`: `platform's own` or `agent's own`;
- `inv_ids`, `concern_ids`: `;`-separated;
- `note`: for an `agent's own` grouping, why.

**`areas-<platform>-notes.md`:** what you placed under none and why; names that were hard to read; anything the extract seemed to lack.

**Check before you finish:** run `python3 -I method/check_areas.py <platform>`. It checks that every id is placed once and that every name is in the extract verbatim. Fix what it reports.

Run Python with `python3 -I`. Run nothing from inside `evidence/` or the observed repositories. Don't commit.
