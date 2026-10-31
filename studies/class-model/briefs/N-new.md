# N-new: the held pass's new things, proposed across the platforms

**What this is.** The held pass's batches named things no capability of the class's model holds: the lines whose `cap_id` is `new:<name>` in `studies/class-model/held/<platform>/placements-*.tsv`. The coordinator decides each in `studies/class-model/held/new.tsv` (`briefs/H-held.md`, "After the batches"): the capability it is, made in an amendment part; an existing capability it turns out to be; or out. This brief's agent proposes those decisions for all five platforms at once, so that one thing held by two platforms becomes one capability with a cell for each, and the coordinator decides from the proposals.

**Read, in this order:**
1. `briefs/B-extent.md`: what a capability is, the test of a place of its own ("an admin route, an admin section, an API group, a plan line or an app category"), and the supports.
2. `held/new.tsv`: its columns, and BigCommerce's seven decided rows as examples of each kind of decision. `parts/E-amend/notes.md`: how a capability made from the held pass is written, and why each is one.
3. `merged/capabilities.tsv`: the model's capabilities, their definitions, areas and parents. A cell's reading is in `merged/cells.tsv`.
4. Each new thing's lines across the platforms' placements, and the batch notes (`held/<platform>/notes-<batch>.md`) where a batch names it: its place of its own if it found one, its proposed domain, area and parent, and its alternatives. The checker's `NEW` lines name the things per batch: `python3 -I method/held_entries.py check --platform <p> --batch <b>`.
5. `held/shopify/amendment-notes.md`, its section "For the new things' decision" and the items that name a new thing; `held/review-H-rulings.md`, its last section, for the rulings on new things and on makers.
6. To see whether another platform holds the thing: `python3 -I method/class_slice.py search --platform <p> "<words>"`, in English and, for Salla and Zid, in Arabic.

**Do:**
1. List every new thing: its platform, its name, its lines and entries, their supports, and the place of its own a batch found, cited.
2. Group the same thing across platforms by what it is, not by its name (one name may be two things, and two names one).
3. Propose one decision for each group:
   - **an existing capability** (`capability:CM-…`), where that capability's definition holds the thing: quote the definition's words that hold it;
   - **a new capability**, where at least one platform gives the thing a place of its own and no capability holds it: its domain and area, a definition in the model's form (what it is, then each platform's own names), its parent if any, and the amendment part that makes it (`<domain>-amend`, as `parts/E-amend/` made BigCommerce's);
   - **out**, where it has no place of its own and is no thing of the class (a screen's frame, a tool no merchant or app uses on a store), with the reason.
   A thing with no place of its own on any platform isn't a new capability: propose the existing capability nearest to it, or out, as BigCommerce's Extensions was decided.
4. Mark each proposal's grounds as the repository's rules do: a fact traced to its source, a reading marked as one.

**Write** only these two files:
- `held/new-proposals.tsv`, one row per new thing per platform: `group`, `platform`, `name`, `lines` (batch:line, `;`-separated), `place` (the place of its own, cited, or empty), `decision` (`capability:CM-…`, `new`, or `out`), `area`, `parent`, `definition` (for a new capability), `reading`. A row can't hold a double quote (`"`).
- `held/new-proposals.md`: the groups, each with its reasoning, and the cases you couldn't settle, each with what would settle it.

Don't edit `new.tsv`, the placements, the parts or the merged files. Make no commits. Keep your context under about 200,000 tokens: list the new things by script, read each batch's note on a thing once, and decide a run of one domain's things at once.

**Report** to the coordinator: the count of new things and groups, the count of each kind of decision, the groups that join platforms, and the open cases.
