# Brief: the class's model, part 1: each concern's area, and each area's labels

**What this step is for.** The model of what the five reference platforms establish is built area by area. First, every concern Q1 recorded gets one area, and every area gets each platform's own labels. Then each later part reads a bounded set of concerns, and coverage can be checked.

This step records where the platforms put things, in their own words. It decides nothing about Sharrwah, and drafts no design. You are one agent with one part, named in your message. The coordinator checks your rows.

**Read only:**
- this brief;
- the seed's `studies/class-model/seed/km-areas.tsv`: the 41 areas with Shopify's and Salla's own groupings. Leave out its questions: they carry answers;
- Q1's concern map, `studies/concern-map/`, for your part's platforms, under `platforms/<platform>/`:
  - `concerns.tsv`;
  - `inventory.tsv`, where each entry's `list` names the kind of list it comes from;
  - `statements.tsv`, mainly its `where` rows, which give where the platform puts each concern in its own organization;
- `matches.tsv`, with its `note` column, which says how strong each match is;
- each platform's `notes.md`, only for where each of its lists stops.

## The task

1. **Each concern's area.** Give every concern of your platforms one area from the seed (`area_id`), by where the platform itself puts it:
   - its `where` statements: an admin section or route, an API group, an app category, a help section;
   - its own terms.

   Rules:
   - **A concern spanning areas:** list the others in `also_in`.
   - **Matched concerns** in `matches.tsv` share an area, unless their platforms' own organizations put them apart. Then say so.
   - **A concern no area fits:** propose a new area, with the evidence.
2. **Each area's labels.** For each area and each of your platforms, give the platform's own label or labels, from its own lists: admin navigation, settings groups, API resource groups, plan table sections. Cite each label apart.
   - Several labels are allowed, one row each.
   - For WooCommerce, a WordPress menu counts only where WooCommerce puts its own pages there.
   - An area with no entry from a platform's lists is `not shown` for that platform.

## Rules

- **Readings and evidence.** A reading is marked as one. Every row cites the statement (concern id, `cite_ids` and `identifier`) or the inventory entry (`inv_id` and its `list`).
- **No market's facts** shape an area.
- **Your own files only.** Read no evidence beyond Q1 and the structures its statements cite. Make no commits, and run Python with `python3 -I`.

## Output, in `studies/class-model/parts/<part>/`

Tab-separated files, with a header row and no quoting:
- `concern-areas.tsv`: `concern_id` · `platform` · `area_id` · `also_in` · `basis` (the cite id and identifier, or the inventory id and list) · `reading` (`yes` or `no`);
- `area-labels.tsv`: `area_id` · `platform` · `label` · `cite` (one row per label);
- `notes.md`: calls you made, proposed new areas, and problems.

**Size:** about 60 requests. At about 90, write what you have and say what is left.

**Report:**
- concerns per area for each platform;
- concerns you couldn't place;
- proposed new areas;
- problems.
