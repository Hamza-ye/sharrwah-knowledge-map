# Brief: the class's model, its extent (one part, some areas)

**Why.** Sharrwah is a merchant platform of the class that Shopify, Salla, Zid, BigCommerce and WooCommerce represent. Its extent comes from the class, not from its launch: what the class establishes, and the slots it leaves for outside parties, belong to the platform (the founder's handoff of 29 October 2026, `reports/intent-review.md`). This step states that extent, area by area, from evidence already held, before any architecture is drafted (domain analysis before architecture: FODA, Kang et al. 1990; a product map of features against products, in product-line scoping).

You are one agent with one task: the areas your message names. You decide nothing for the founder, and you design nothing. The coordinator checks your rows, and an agent that made none of them reviews them later.

**Read only:**
- this brief;
- `studies/class-model/seed/`:
  - `km-areas.tsv`: your areas' rows;
  - `km-questions.tsv`: your areas' questions, as leads to what an area covers, never as answers;
  - `km-source-types.tsv`: how each kind of source is graded;
  - the seed's `README.md`: what the seed isn't;
- Q1's concern map, `studies/concern-map/`:
  - per platform under `platforms/<platform>/`: `concerns.tsv`, `inventory.tsv` (each entry's `list` names the platform's own complete list it comes from), `statements.tsv` (by id), and `placements.tsv` (Shopify, Salla and WooCommerce; Zid's and BigCommerce's placements are in their statements' `placement` column);
  - `matches.tsv`, `unclear-matches.tsv` and `map/single-platform.tsv`;
- where a platform's own complete list in the evidence repositories says more than Q1 held, that list, through the repository's `README.md` and `docs/READING.md` (observed-sh, observed-sa), or `README.md` and `index/` (other-product-class's `zid/`, `bigcommerce/`, `woocommerce/`). Cite it at its commit.

Leave out every `notes*.md` file and every `note` column.

## The task, per area

1. **The area's own labels.** For each of the five platforms, name the area in the platform's own words, from its own lists: admin navigation, settings, plan tables, API resource groups. An area a platform doesn't show is `not shown`, and `absent` only where a complete list shows it is not there.
   - Where the evidence shows the seed's area doesn't fit, propose a split, a merge or a new area, with the evidence, as a reading.
2. **The capabilities.** A capability is the smallest unit a store or the platform can have or not have. Name it neutrally, then give each platform's own term.
   - Build the capabilities from Q1's concerns and inventory entries that fall in the area, joining the five platforms by Q1's rule for the same thing: their own terms, the same thing filling the same role.
   - Use `matches.tsv` where it already joins them. For an unclear candidate, decide by the rule, and mark it as a reading.
3. **For each capability and each platform:**
   - **Where it lives:** `core`, `separate service` (the platform's own product line), `extension point` (an app, function or provider slot), `outside`, `not shown`, or `absent` (from a complete list only), from Q1's placements, cited by concern id and statement id.
   - **Who decides its value:** from the same placements, where Q1 holds them.
4. **Kind and commonality,** by the coordinator's ruling. This is engineering's, as the Knowledge Map's MTH-01 asked it; the founder may veto it.
   - **`class`:** at least one platform establishes the capability as its own, in its core or a separate service of its own.
   - **`slot`:** every platform that shows the capability leaves it to an extension point. The slot belongs to the platform, and what fills it doesn't.
   - **`world`:** a market's providers, partners or law that fill a slot. Record a `world` row only where a platform names one as filling a slot, and never as the platform's extent.
   - **`commonality`:** how many of the five establish it as their own, 0 to 5.
5. **Qualities the class states.** Where a platform states a limit, a certification, an uptime or a data location for the area, record it as a capability of kind `class`, with the stated value and its citation.

## Rules

- **Every claim cites ids:** Q1's concern and statement ids, or an evidence path at a commit. A reading is marked as one. The founder's words are never evidence of what a platform does.
- **No market's facts.** No market's facts and no market's name shape a row. A capability scoped to one country by a platform keeps that scope in its citation.
- **Coverage.** Every Q1 concern of the five platforms that falls in your areas lands in exactly one capability, or is named as belonging to another area. Record the area in `concern-areas.tsv`, so coverage can be checked.
- **Breadth, not depth.** State that a capability exists and where it is placed. Its fields, states and rules are the area's later model.
- **Your own files only.** Make no commits, and run Python with `python3 -I`.

## Output, in `studies/class-model/`

Tab-separated files, with a header row and no quoting. Append your areas' rows, and never rewrite another part's.
- `areas.tsv`: `area_id` · `domain` · `area` · `shopify` · `salla` · `zid` · `bigcommerce` · `woocommerce` (each the platform's own label and its citation, or `not shown` or `absent`) · `seed_change` (empty, or the split, merge or new area, with its evidence).
- `capabilities.tsv`: `cap_id` (`CM-<area_id>-nnn`) · `area_id` · `capability` · `kind` · `commonality` · `shopify` · `salla` · `zid` · `bigcommerce` · `woocommerce` (each: where it lives, then the concern and statement ids, such as `core SH-C-012 SH-S-0045`) · `decides` · `reading` · `note`.
- `concern-areas.tsv`: `concern_id` · `area_id` · `cap_id` (empty where the concern belongs to another area, named in `area_id`).
- Your notes in `notes-extent.md`, under your part's heading: calls you made, and problems with the brief or the evidence.

**Size:** your message gives it. At its stop, write what you have and say which areas are left.

**Report:**
- per area, its labels, its count of capabilities by kind, and its commonality spread;
- the concerns you couldn't place;
- proposed changes to the seed's areas;
- problems.
