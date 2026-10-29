# Brief: the class's model, its extent, one domain at a time

**What this step is for.** A product map of what the five reference platforms establish: Shopify, Salla, Zid, BigCommerce and WooCommerce. It lists their capabilities, and for each, what each platform shows and where it puts it. It records what the platforms do, in their own words. It decides nothing about Sharrwah, ranks nothing, and drafts no design.

You are one agent with one part: the domain your message names, from the seed's areas. The coordinator checks your rows and merges the parts. An agent that made none of them reviews them.

**Read:**
- this brief;
- `studies/class-model/seed/km-areas.tsv`, for your domain's areas and their Shopify and Salla labels. Leave out the seed's questions;
- Q1's concern map, `studies/concern-map/`:
  - **all five platforms' `concerns.tsv`, whole:** 652 rows, about 22,000 tokens. Take the concerns that belong to your domain;
  - **for the concerns you take,** the platform's `statements.tsv` rows under every placement, its `inventory.tsv` entries, and `citations.tsv` for the commit each source was read at;
  - `matches.tsv` and `unclear-matches.tsv`, with their `note` columns;
  - each platform's `notes.md`, only where it says how complete one of its lists is;
- the structures Q1's citations name, at the commit `citations.tsv` gives, where a statement needs more context.

## What to produce

**Capabilities.** A capability is something a store or the platform can have or not have. Build them from the concerns you take, across all five platforms.
- **Join** concerns that are the same thing on two platforms, by their own terms, identifiers or definitions. Q1's matches are such joins.
- **Where two platforms' definitions show the same role under different names,** you may join them. Mark the join as a reading, and cite both definitions.
- **Where platforms cut at different grains,** you choose the capabilities, using `parent` where one holds others. Say in your notes why.

Staff permissions, webhook topics, access scopes and plan lines are evidence for a capability, not capabilities themselves.

**The area.** Each capability gets one area. Choose the one where the class as a whole puts it. Each platform's own place for it goes in its cell, so nothing is lost when platforms put it in different places.

**Cells:** one row per capability and platform.
- **What the platform shows, in its own words:** its terms, and where it puts the capability (an admin section, an API group, an app category, a separate product), with each statement's concern id, cite id and identifier.
- **Placement,** as your reading of those statements:
  - `core`: part of the platform itself;
  - `own service`: a separate line of the platform's company, such as a payments, shipping or buyer app of its own;
  - `extension point`: where third parties plug in;
  - `outside`: the platform says another party does it.

  More than one may apply.
- **The statements' scope, as stated:** a country, a plan, a store, a role.
- **Q1 holds nothing for this platform here:** say that in so many words. It never means the platform lacks it. A complete list showing it missing is named, with where that list is described as complete.

**Qualities and slot fillers,** each in its own file:
- **Qualities:** a limit, a certification, an uptime or a data location a platform states.
- **Slot fillers:** a provider, partner or law a platform names as filling a slot. These are each market's setup, not the platform's extent.

## Rules

- **Evidence:** every cell cites Q1's ids, and every reading is marked. No claim goes beyond what a cited statement says.
- **No market's facts** decide a capability or its area. A statement scoped to one market keeps that scope.
- **Every concern you take** appears in a cell. A concern you look at and leave for another domain is listed, with that domain, in your notes.
- **Your own files only:** write only your part's files, make no commits, and run Python with `python3 -I`.

## Output, in `studies/class-model/parts/<part>/`

Tab-separated files, with a header row and no quoting:
- `capabilities.tsv`: `cap_id` (`CM-<area>-nnn`) · `area` · `capability` · `parent` · `join` (`match`, `terms`, `role, a reading`, or `single`) · `note`;
- `cells.tsv`: `cap_id` · `platform` · `concern_ids` · `terms` · `where` (its own words, with ids) · `placement` · `scope` · `evidence` (cite ids and identifiers) · `reading` (what in the cell is a reading);
- `qualities.tsv`: `area` · `platform` · `quality` · `value` · `evidence`;
- `slot-fillers.tsv`: `cap_id` · `platform` · `filler` · `market` · `evidence`;
- `notes.md`: how you cut the capabilities, every join on role, concerns left for other domains, and problems with the brief or the evidence.

**Size:** your message gives it.

**Report:**
- capabilities per area;
- how many have one, two, three, four or five platforms showing them;
- the joins on role;
- concerns left for other domains;
- problems.
