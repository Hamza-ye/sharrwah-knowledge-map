# Brief: the review of the held pass's dry run (Stage 4A)

**What this is.** The held pass (`studies/class-model/briefs/H-held.md`) places every entry of the platforms' self-descriptions that the class's model never read. Two batches ran first, at `high` effort: BC-1 (BigCommerce, 147 entries) and ZD-1 (Zid, 153 entries). You made neither. Your findings are the evidence from which the coordinator corrects the two batches, fixes H-held.md and its checker, and sets the other 68 batches' effort (the founder, 30 October: by the quality and completeness of their results). The coordinator checks each finding against its evidence before applying it (`PLAN.md`, section 3).

**Your part.** The review runs in five parts, each by a fresh agent, and a sixth that joins them. Your message names yours:

| Part | Lines | Structures |
| --- | --- | --- |
| R1 | BC-1, lines 2 to 37 | channel-catalog, contracting-entities |
| R2 | BC-1, lines 38 to 96 | payment-gateways |
| R3 | BC-1, lines 97 to 176 | plan-comparison, settings-list, tax-services |
| R4 | ZD-1, lines 2 to 62 | dashboard-page-index, its first part |
| R5 | ZD-1, lines 63 to 144 | dashboard-page-index, its second part; dashboard-route-manifest |
| R6 | the join | the five parts' rows and notes |

**What you read is pinned:**
- BC-1's placements and notes at `ff50bbee`, and ZD-1's at `33946dbc`;
- H-held.md and `held/selection.tsv` at `dc1e6414`, as the agents followed them;
- the model at `13205959`;
- other-product-class at `0d79b794f`, the commit `entries.tsv` names.

`git show <commit>:<path>` reads a file at its commit. Nothing these hold has changed since, but corrections may land while you work.

**Effort:** `max`, or `xhigh` at least. The batches ran at `high`, and this review measures what a closer reading finds (the founder, 30 October).

**Read only this brief and:**
- **what the agents were told to read,** so you can judge whether a miss is the brief's:
  - the evidence map, `studies/class-model/evidence-map.md`, first, by structure (`PLAN.md`, section 6);
  - the held pass's brief, `studies/class-model/briefs/H-held.md`, which states the rules each placement had to follow;
  - `held/selection.tsv`'s rows for your part's structures, and the platform's `structures/REGISTER.tsv` rows for them;
- **the model's rules:** `studies/class-model/briefs/B-extent.md`, "Cells and evidence" and "Conventions from the dry run";
- **your part's lines,** in `studies/class-model/held/<platform>/placements-<batch>.tsv`, and the batch's `notes-<batch>.md`;
- **the entries,** through `python3 -I method/held_entries.py show --platform <p> --batch <b> --from <i> --to <j> --candidates`, and `--meta`;
- **each entry's sources,** at other-product-class `0d79b794f`, through its guides first (`README.md`, then the platform folder's `README.md` and `GAPS.md`):
  - the item, at the file and locator `entries.tsv` gives;
  - the file the structure's `meta.json` names under `source` (`held_as`, `answer`), with the rest of that `meta.json`;
  - the `source.*` file beside `items.jsonl`.

  Where the rendering, the item and the source differ, the source governs;
- **what the agents read to clarify an entry,** so that each reading resting on it can be checked:
  - the platform folder's `index/`, with Zid's `index/ledger/dashboard-routes.tsv` and the run steps it names;
  - the run steps the notes and readings cite;
  - `zid/structures/dashboard-locales/items.jsonl`, which the selection marks `read: no`.

  For each reading that rests on a file beyond the entry's item and source, say whether H-held.md allows it, as a fix to H-held.md. Its rule 1 names only the item and its source;
- **the model:**
  - `method/class_slice.py` (`caps --terms`, `key`, `search`);
  - `method/land_points.py cell <cap_id> <platform>`;
  - `studies/class-model/merged/capabilities.tsv`, read with `cut` or `grep`.

## What to check, for every line of your part

**Try to refute each line** (`PLAN.md`, section 3).
- Name the strongest other placement the entry and its sources allow. Include the one the cell's own reading of the same kind of statement gives (`land_points.py cell`).
- Test the line against it.
- Report counter-evidence and missing evidence, not agreement.
- Look also for what the line leaves out: another capability the entry is, or a thing it states that no line places.

1. **The entry, read against its sources.** Is the entry what its sources say? Where the rendering and the source differ, the source governs.
2. **The placement:**
   - `capability`: is the cap_id the capability whose thing the entry is? Is there one whose thing it is more plainly? Search `caps --terms` with the entry's own words, in English and, for Zid, in Arabic.
   - `new`: is no capability's thing the entry's? Does it have a place of its own, by B-extent's "What a place of its own is"?
   - `out`: is the entry outside what the platform does, by H-held.md's list?
3. **`supports`,** by B-extent.md's "Cells and evidence" and its conventions, which H-held.md's rule 4 says govern. Where H-held.md's restatement reads differently, the verdict follows B-extent.md, and the difference is a fix to H-held.md, with the lines it touches. The restatement leaves out three of B-extent.md's clauses:
   - for `core`, "the platform itself does it for the merchant";
   - for `extension-point`, "the statement shows third parties doing it through something the platform provides";
   - for `own-service`, "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap".
4. **`scope`, `terms`, `filler` and `quality`,** by H-held.md's rule 5:
   - `scope` in the entry's words;
   - each term found in its text;
   - a filler is a third party or a law the entry names as doing it or setting its terms;
   - a quality's value is in the entry's words.

   Is anything the entry states missing?
5. **`reading`:** does it state its source truly? `held_amend.py` writes it into the model's evidence.

**The verdicts.** One row per verdict. A line with two problems takes two rows, and a group whose entries need different verdicts takes a row per entry. Each verdict carries the value it calls for:
- `stands`: the test didn't overturn the line. Its `why` names the alternative tested and why it fails;
- `wrong capability: <cap_id>`;
- `wrong supports: <value>`;
- `should be new: new:<name>`; `should not be new: <cap_id>` or `should not be new: out`; `should be out`;
- `missing line: <cap_id or new:name> <supports>`: the entry is also another capability's, or states a thing no line places;
- `missing <column>: <value>` or `wrong <column>: <value>`, for `scope`, `terms`, `filler` and `quality`;
- `wrong reading: <what the source says>`;
- `entry differs from source: <how>`;
- `can't tell: <what would settle it>`.

Say why, citing the source.

**For every verdict but `stands`:**
- `cause`, one of:
  - `care`: the brief and the evidence named settle it, and the line misses it;
  - `brief`: H-held.md doesn't settle it, or reads two ways (name the rule);
  - `evidence`: the entry and its sources don't settle it;
  - `tool`: the rendering, the leads or the checker misled (name which);
- `effect`: what the correction changes once `held_amend.py` writes it, one of:
  - `count`: a cell gains or loses `core` or `own-service`;
  - `kind`: a cell gains or loses `extension-point` or `outside`;
  - `capability`: a capability made or not made, or the entry moved to another;
  - `filler`: a slot filler added or removed;
  - `column`: scope, terms, quality or reading only.

**The leads.** For each line on a capability, give `in_leads`:
- `yes` or `no`: whether the right cap_id is among the entry's leads, as `show --candidates` prints them now;
- `-` for `new` and `out`.

The leads changed after the batches ran: at `99d429ad`, an identifier that many entries share is skipped, and each lead shows its cell. The agents saw an earlier version, which the brief's inspection measured (`inspection-HR.md`, N-4).

## Then, for your part's structures

**The cases where H-held.md left the agents unsure, or let them read a rule two ways.** Rule on each case in your part from the entries and their sources, weighing every value B-extent.md allows, and look for others. The agents' notes name these:
- **R1:**
  - **BC-1's channel cards (lines 2 to 27):** who each card and its sources show doing the work (the platform, a named third party, or no one). From that, which `supports` each takes, and which of the parties it names are fillers. The notes say of Buy Buttons, Amazon, Walmart and eBay (lines 22 and 24 to 26) that "Who builds these connections isn't stated".
  - **The entries that name a company:** the contracting entities (lines 28 to 37) and the Feedonomics cards (lines 2 to 9 and 14 to 21). Does any name the platform's company, or a company of its group, as the maker or provider of a separate product? Judge by its own words and its sources' only.
- **R2: BC-1's payment-gateways rows (lines 38 to 96).** Which `supports` each takes, from the rows and the article around them. Does H-held.md's rule for a help page's title apply to a row of a table in one? The model's own CM-PAY-011 cell reads the article's "more than 65 pre-integrated online payment solutions" as `core`.
- **R3:**
  - BC-1's plan lines and settings sections;
  - the tax services' `extension-point` (lines 169 to 176), by B-extent.md's definition;
  - the differences its notes find with the model's cells: CM-CHN-007's storefronts, CM-INV-005's limit, and CM-PAY-001's payments page.
- **R4 and R5, in your lines:**
  - ZD-1's containers (Analytics, Settings, Store, Marketing, Logistics, Payments, Channels, Apps, Online store, Communications, Whatsapp);
  - its pages with a release badge;
  - its pages listed only under a store condition.
- **R4:** the pages at an app's address named with the platform's brand, Zid Ads and Zid Voice (lines 13 and 14).
- **R5:**
  - the bank accounts page against CM-PAY-030's cell (line 110);
  - the access requests by the platform's own team (lines 125, 127 and 134);
  - the new Customer Referrals (line 90).
- **Every part:** every other item of the notes' "couldn't tell" and "Problems" that bears on your lines.

Each fix stays within B-extent.md's rules. Where B-extent.md doesn't settle a case either, say so: it is a method ruling for the coordinator, listed at the next report (`PLAN.md`, section 3). For each recurring miss, say whether a test in `held_entries.py check` would catch it, and which test.

**What the batch never placed.** For each of your part's structures, compare its items with its sources (the files above).
- List each thing a source states that no entry holds, with its place in the source, and say whether it would change a cell.
- Say whether the agent, the brief, the selection or the build left it out.
- **R4:** ZD-1's notes name 18 pages of the page index without an entry. The evidence map reads that each has its route in the route manifest, so the model loses nothing: test that reading.
- **R3:** the plan table's `meta.json` holds the plans' prices.

**The notes' claims for your structures.** Check each of them, and give each a verdict and why:
- each new thing's searched terms and proposed place;
- each "couldn't tell";
- each difference from the model's cells;
- each structure whose items and sources disagree.

## R6, the join

R6 reads this brief and the five parts' rows and notes. It re-reads a source only to settle two parts that disagree. It writes `held/review-H.md`:
- the counts of verdicts, per batch and part;
- **the misses by `cause` and `effect`,** each with the lines it rests on:
  - per batch;
  - per structure;
  - per rule of H-held.md;
  - per third of each batch's lines. A miss that grows toward a batch's end points to its size, not its effort;
- which effects it takes as the "important details" of the founder's decision of 30 October, and why;
- **the brief's ambiguities,** each with:
  - a fix in words the coordinator can paste;
  - whether it stays within B-extent.md, or is named as a method ruling;
  - the checker test that would catch it;
- **what the dry run doesn't hold, and so sets nothing for.** Of the 144 structures the 70 batches hold, BC-1 and ZD-1 hold 8. No line is `out` or `outside`, and neither batch holds a flag or a list of staff or partner permissions;
- the judgement on effort, per kind of entry the dry run holds: `high`, `xhigh` or `max`, with the misses it rests on;
- the leads: how often the right capability was among them, per structure;
- what the batches never placed, and the notes' claims, from the parts.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Never decide a maker, a third party or a placement from what you know of the platform: only from what the entry and its sources state.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- other-product-class is read-only: never write, commit or push to it.
- Run Python with `python3 -I`.
- Change no file but your output, and make no commits.

## How to work, keeping your context small

- Read each structure's sources once, before its lines.
- Read each cell once, for the capability placed and for each alternative you test. Keep what it holds in a line of your notes.
- Print your entries 20 to 30 at a time, with `show --from --to --candidates`. Read your placement lines with `sed -n`, never the whole file.
- Never print the help-center run's `001.html`: its text is in `001.text.txt`.
- Write rows as you go.

## Output, in `studies/class-model/held/`

**`review-H-<part>.tsv`, R1 to R5.** Tab-separated, with a header row, no quoting, and no tab or newline inside a field. Its columns:
- `batch`;
- `line`: the placement file's line number, at the batch's commit;
- `entry_id`;
- `cap_id`: the line's, so that a row still finds its line after a correction;
- `verdict`;
- `cause` and `effect`: empty for `stands`;
- `in_leads`;
- `why`: a reading, citing the source.

Every line of your part has at least one row.

**`review-H-<part>.md`, R1 to R5:** the counts of your verdicts, the cases, what the batch never placed, and the notes' claims, as above.

**`review-H.md`:** R6's join.

## Report

Back to the coordinator:
- the counts of verdicts;
- the misses by cause and effect;
- each fix to the brief, in one line;
- R6 also gives its judgement on the effort for the other batches, with why.
