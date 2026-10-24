# Brief: one platform's broad areas (step R1, run once per platform)

**Status: draft, revised after the check of the drafts (`studies/proposals/check-of-the-draft.md`). It is checked again before it runs.**

You are one agent with one short task, for one platform. The message that started you names the platform. You run at `high` effort.

**Read only:**
- this brief;
- `studies/proposals/areas/extract-<platform>.md`;
- where a name in the extract is unclear, the one passage its `cite_id` points to. Find the cite id's source in `studies/concern-map/platforms/<platform>/citations.tsv`. If the source is held in an observed repository, read it from git's objects, from outside the repository: `git --git-dir=/home/user/observed-sh/.git show <commit>:<path>` (or `observed-sa`). Read only that passage.

## Whose words are whose

- **The platform's own words:** the names of a list's entries, each concern's terms ("The platform's terms"), the Shopify Help Center's menu names, and the Salla help centre's category names.
- **The concern map's words:** list labels, such as `legal-agreements`, and each concern's description ("The concern map's description"). They say where a list came from and what a concern is about. They are never area names.

## The task

Name the platform's broad areas, the way the platform itself divides what it offers and what it requires.

1. **Use the platform's own names.** Take each area's names from the platform's own words in the extract: its menus, help-centre sections, settings, plan tables, product lines, legal agreements, country lists, and the concerns' terms.
   - Copy each name exactly as the extract gives it.
   - Follow it with its label in brackets:
     - a list entry takes its list's label, as `Payments [settings]`;
     - a concern's term takes `[term]`;
     - a Shopify Help Center menu name takes `[Help Center]`;
     - a Salla help-centre name takes `[help centre]`.
2. **Cover what no menu shows.** Some of what a platform requires or allows shows only in its terms, its country lists, its eligibility rules, its plans, or the scopes its statements give. That includes:
   - legal matters: agreements, the companies that contract, policies;
   - places: where it operates, and what differs by country;
   - eligibility: who may use what, and where.

   Wherever the extract shows these, they get an area, even when no menu names one.
3. **Tens, not hundreds.** Aim for 15 to 30 areas.
   - Where the platform's own names can't bring the list down that far, group further.
   - Mark each such grouping as your own (`grouping` = `agent's own`), and give the reason in `note`. Its names are still the platform's own names for what it holds.
4. **Place every concern.** Each concern in the extract goes under exactly one area, by its id.
   - Where a concern fits no area, list it under none, in your notes, with the reason.
   - You don't place the inventory's entries: a script places each entry under the area of its concerns.
5. **One plain line per area.** It says, in plain words, what the area covers on this platform. It describes. It doesn't rank, compare with other platforms, or say what anyone should build.

**Don't:**
- use any category of ours, in a name or a plain line. That includes the words "market", "availability", "conditions", "manual payment" and "parts", unless the platform itself uses the word for that thing in the extract. Never use the names of other platforms' areas;
- compare with other platforms. Merging the five lists is the coordinator's step;
- read beyond what this brief names.

## Output, in `studies/proposals/areas/`

**`areas-<platform>.tsv`:** tab-separated, with a header row and no quoting. Columns:
- `area_id`: the platform's code and a two-digit number, as `SH-A-01`. The codes are SH, SA, WC, ZD and BC;
- `platform_names`: the names, `;`-separated, each with its label in brackets;
- `plain_line`;
- `grouping`: `platform's own` or `agent's own`;
- `concern_ids`: `;`-separated;
- `note`: for an `agent's own` grouping, why.

**`areas-<platform>-notes.md`**, with these headings:
- `## Under none`: one line per concern under no area, as `- SH-C-123: <the reason>`;
- `## Names that were hard to read`: what you read to settle each;
- `## What the extract seemed to lack`.

## Before you finish

1. Run `python3 -I method/check_areas.py <platform>`. It checks that:
   - every name is one of the platform's own names, whole, under the label you gave it;
   - every concern is under one area, or under none with a reason;
   - the columns, ids, groupings and plain lines are well formed.

   Fix what it reports, until it reports no problems.
2. Run `python3 -I method/place_entries.py <platform>`. It writes `areas-<platform>-entries.tsv`, placing each inventory entry under the area of its concerns. It prints how many entries each area holds, and how many fall in more than one area or in none.
   - If an area holds entries that don't fit its plain line, or many entries fall in more than one area, say so in your notes, under `## Entries`.
   - Don't edit the entries file.

**Constraints:**
- Run Python with `python3 -I`.
- Run nothing from inside `evidence/` or the observed repositories.
- Don't commit.
