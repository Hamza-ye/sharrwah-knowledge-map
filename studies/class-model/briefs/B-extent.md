# Brief: the class's model, part 2: the extent, area by area

**What this step is for.** For each area, a product map: the capabilities the five reference platforms show, where each platform places each one, whether its plans gate it, and how many of the five establish it as their own. It records what the platforms do. It decides nothing about Sharrwah, ranks nothing, and drafts no design. You are one agent with one part: the areas your message names. The coordinator checks your rows, and an agent that made none of them reviews them later.

**Read only:**
- this brief;
- `studies/class-model/areas.tsv` and `concern-areas.tsv`: your areas' labels and the concerns assigned to them, both primary and `also_in`;
- Q1's concern map, `studies/concern-map/`:
  - per platform, `concerns.tsv`, `inventory.tsv` (your concerns' entries) and `statements.tsv` (your concerns' rows under every placement);
  - `matches.tsv` and `unclear-matches.tsv`, with their `note` columns;
- the structures Q1's statements cite, read at the commit each citation names.

Leave out the seed's questions, and every other `notes*.md` file.

## The task, per area

1. **Capabilities.** A capability is one of Q1's matched groups, or one unmatched concern. Q1 cut each concern as "the smallest piece with a single placement".
   - Where two platforms cut at different grains, the coarser concern covers several capabilities. Its cells say so.
   - Staff permissions, webhook topics, access scopes and plan lines are evidence for a capability, never capabilities themselves.
   - Name each capability neutrally. Each platform's own terms go in its cell.
2. **Joining across the five.**
   - **Q1's matches stand.** They join on the platforms' terms, identifiers or definitions.
   - **The rest get the same test:** Q1's unclear candidates, and every Zid and BigCommerce concern, which Q1 never matched.
   - **A join on role alone,** with different names, needs both platforms' own definitions to state the role. Mark it as a reading and cite both definitions. These rulings are engineering's, and the coordinator checks each one.
   - **A concern in both a match and an unclear candidate** keeps its match.
3. **Cells:** one row per capability and platform, in `capability-cells.tsv`.
   - **`placement`:** read from the platform's `where` statements, as one of:
     - `core`: an admin section or route, an API group, or a code path of the platform itself;
     - `own service`: a separate product, host or line of the platform's company, its own apps and extensions included;
     - `extension point`: a place third parties fill, such as an app category, an extension target or a provider slot;
     - `outside`: the platform states another party does it;
     - `not shown`: Q1 holds no statement on it;
     - two of these joined by `+`, where the platform states both.

     Each placement is a reading of the statements it cites: give the concern id, cite id and identifier of each.
   - **`plan_gated`:**
     - `yes`: a `decides` statement names a plan, tier or entitlement for it;
     - `no`: a `decides` statement shows it on every plan;
     - `not shown`: otherwise.
   - **`depth`:** how deeply Q1 read the platform. Shopify, Salla and WooCommerce are `full`. Zid and BigCommerce are `declaration`, read without accounts. So `not shown` on Zid or BigCommerce isn't absence.
   - **`terms`:** the platform's own words.
4. **Capability rows,** in `capabilities.tsv`:
   - `cap_id` (`CM-<area_id>-nnn`) · `area_id` · `capability` · `parent` (optional) · `note`;
   - and, from the cells, by rule:
     - **`kind`:**
       - `class` if any cell is `core` or `own service`;
       - `slot` if every shown cell is `extension point`;
       - `outside` if every shown cell is `outside`;
     - **`own`, `slot` and `shown`:** how many cells are `core` or `own service`, how many are `extension point`, and how many are not `not shown`.

   Absence isn't recorded: Q1 never states one. A complete list showing a capability missing is named in the cell's evidence, as `not shown (complete list: …)`.
5. **Qualities,** in `qualities.tsv`: where a platform states a limit, a certification, an uptime or a data location for the area. Columns: `area_id` · `platform` · `quality` · `value` · `cite`. These are values, not capabilities.
6. **What fills a slot,** in `slot-fillers.tsv`: where a platform names a provider, partner or law filling a slot. Columns: `cap_id` · `platform` · `filler` · `market` (as stated) · `cite`. These are each market's setup, kept out of the extent.

## Rules

- **Readings and evidence.** Every claim cites ids, and a reading is marked per cell. The founder's words are never evidence of what a platform does.
- **No market's facts.** No market's name shapes a class or slot row. What fills a slot is recorded apart.
- **Your own files only.** Write only your part's files. The coordinator merges the parts. Make no commits, and run Python with `python3 -I`.

## Output, in `studies/class-model/parts/<part>/`

- `capabilities.tsv`;
- `capability-cells.tsv`: `cap_id` · `platform` · `placement` · `plan_gated` · `depth` · `terms` · `evidence` · `reading`;
- `qualities.tsv`;
- `slot-fillers.tsv`;
- `notes.md`: calls you made, every join on role alone, the concerns you couldn't place, and problems.

**Size:** about 20 requests per area. Your message gives the stop.

**Report:**
- per area, its capabilities by kind, and the spread of `own`, `slot` and `shown`;
- the joins on role alone;
- the concerns not placed;
- problems.
