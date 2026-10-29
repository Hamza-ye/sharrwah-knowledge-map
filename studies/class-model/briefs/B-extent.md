# Brief: the class's model, its extent

**What this step is for.** A product map of what the five reference platforms establish: Shopify, Salla, Zid, BigCommerce and WooCommerce. It lists their capabilities, and for each, what each platform shows and where it puts it. It records what the platforms do, in their own words. It decides nothing about Sharrwah, ranks nothing, and drafts no design.

**How it is built, in two passes.**
1. **The anchor: Shopify and Salla, one domain per part.** Shopify and Salla are the deepest evidence: 3,005 and 2,560 statements, read in full. The structure follows their own groupings.
2. **The mapping: one platform per part,** WooCommerce first, then Zid, then BigCommerce. Each is mapped onto the anchor's capabilities. Where a platform shows something the anchor doesn't, it adds a capability, so the model stays the union of the class.

This is exemplar-based domain analysis: the model is built from representative systems, then checked and extended against others.

You are one agent with one part. Your message names the pass and your domain or platform. The coordinator checks your rows and merges the parts. An agent that made none of them reviews them.

**Read:**
- this brief;
- `studies/class-model/seed/km-areas.tsv`, for the areas and their Shopify and Salla labels. Leave out the seed's questions;
- Q1's concern map, `studies/concern-map/`:
  - **in the anchor pass:** Shopify's and Salla's `concerns.tsv`, whole; take the concerns that belong to your domain;
  - **in the mapping pass:** your platform's `concerns.tsv`, whole, and the anchor's merged `studies/class-model/capabilities.tsv` and `cells.tsv`;
  - **for the concerns you take,** the platform's `statements.tsv` rows under every placement, its `inventory.tsv` entries, and `citations.tsv` for the commit each source was read at;
  - `matches.tsv` and `unclear-matches.tsv`, with their `note` columns;
  - each platform's `notes.md`, only where it says how complete one of its lists is;
- the structures Q1's citations name, at the commit `citations.tsv` gives, where a statement needs more context.

## What to produce

**In the anchor pass: capabilities.** A capability is something a store or the platform can have or not have. Build them from Shopify's and Salla's concerns in your domain.
- **Join** concerns that are the same thing on both platforms, by their own terms, identifiers or definitions. Q1's matches are such joins.
- **Where the two platforms' definitions show the same role under different names,** you may join them. Mark the join as a reading, and cite both definitions.
- **Where they cut at different grains,** you choose the capabilities, using `parent` where one holds others. Say in your notes why.
- **The area:** each capability gets one area, the one where the two platforms put it. Each platform's own place goes in its cell.

**In the mapping pass: each of your platform's concerns lands once.** Either:
- in an anchor capability, where it is the same thing by terms, identifiers or definitions. A join on role is a reading, citing both definitions; or
- in a new capability that only your platform shows, with its area.

Where a fit is strained, list it in your notes, so the reviewer can split it.

**In both passes:** staff permissions, webhook topics, access scopes and plan lines are evidence for a capability, not capabilities themselves.

**Cells:** one row per capability and platform, for your pass's platforms.
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
- **Every concern you take** appears in a cell. In the anchor pass, a concern you look at and leave for another domain is listed, with that domain, in your notes.
- **Your own files only:** write only your part's files, make no commits, and run Python with `python3 -I`.

## Output, in `studies/class-model/parts/<part>/`

Tab-separated files, with a header row and no quoting:
- `capabilities.tsv`: `cap_id` (`CM-<area>-nnn`; in the mapping pass, new ones only) · `area` · `capability` · `parent` · `join` (`match`, `terms`, `role, a reading`, or `single`) · `note`;
- `cells.tsv`: `cap_id` · `platform` · `concern_ids` · `terms` · `where` (its own words, with ids) · `placement` · `scope` · `evidence` (cite ids and identifiers) · `reading` (what in the cell is a reading);
- `qualities.tsv`: `area` · `platform` · `quality` · `value` · `evidence`;
- `slot-fillers.tsv`: `cap_id` · `platform` · `filler` · `market` · `evidence`;
- `notes.md`: how you cut or placed, every join on role, strained fits, concerns left for other domains, and problems with the brief or the evidence.

**Size:** your message gives it.

**Report:**
- capabilities per area;
- in the mapping pass, how many of your concerns joined anchor capabilities, and how many made new ones;
- the joins on role;
- strained fits;
- problems.
