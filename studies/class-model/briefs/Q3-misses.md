# Brief: Q3's candidate misses, checked against what is held (Stage 4A)

**Superseded before it ran** (the coordinator, 30 October, after its inspection, `studies/class-model/inspection-Q3M.md`). The held pass runs first, and Q3's 13 candidate misses are checked in its second stage, which reads the held pages for the cells that still hold nothing. That stage's brief takes every finding of the inspection. This file stays as the record of what was inspected.

**What this is.** `PLAN.md`, Stage 4A, "The check for what it misses": "A row the model doesn't cover is a candidate miss, checked against the evidence." Q3's batches searched the concern map: its statements and placed inventory entries (`class_slice.py search`, `outscope`). The evidence repositories hold far more: pages, schemas, structures and runs the concern map never read. Shopify's return rules, for one, are held in its Help Center and its admin API schema, and the concern map has no statement on them. This check reads the repositories themselves for each candidate miss. `PLAN.md`, section 6, Evidence: before a gap goes to anyone, its route is checked against what is held, through each repository's own reading guides and indexes first, then by search (the founder, 30 October).

What you find decides what follows: a new capability, a cell's evidence, or a capture request. You draft; the coordinator checks every line and decides.

Your message names your batch, `A` or `B`. `python3 -I method/q3_misses.py misses --batch <batch>` prints its misses. For each it gives the Q3 rows, each row's question, and its rest: what the batch searched, what it found and what would settle it. It also prints the row's basis.

**Read only this brief and:**
- **each evidence repository's own reading guides and indexes, first, before any search:**
  - observed-sh (`/home/user/observed-sh`, Shopify) and observed-sa (`/home/user/observed-sa`, Salla): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `docs/OPERATING.md`, `index/` (`runs.tsv`, `run-notes.tsv`, `instruments.json`), `structures/README.md`, `structures/REGISTER.tsv`;
  - other-product-class (`/home/user/other-product-class`, Zid, BigCommerce and WooCommerce): `README.md`, `docs/OPERATING.md`, and each platform folder's (`zid/`, `bigcommerce/`, `woocommerce/`) `README.md`, `GAPS.md`, `index/` and `structures/REGISTER.tsv`;
  - WooCommerce's release, unpacked at `/home/user/woocommerce-release/11.2.1` (`evidence/product-class/woocommerce-11.2.1/` fixes it by checksum);
- **the tools:**
  - `method/held_index.py`, for what is held by address;
  - `method/corpus_search.py`, for a platform's held text in every language. Its header says how;
  - `method/quote_check.py`, to test each quote before you write it. `--text SOURCE` prints a source's text as the checker reads it;
  - `method/schema_type.py`, for a GraphQL type in full;
- **the model:** `method/class_slice.py` (`caps`, `search`, `key`, `outscope`), `method/q3.py where`, and `method/land_points.py cell <cap_id> <platform>`;
- **`studies/class-model/briefs/B-extent.md`**, its "Cells and evidence" and "Conventions from the dry run": what makes a capability ("When something becomes a capability") and what places a cell.

## For each miss, on each of the five platforms

1. **Read the guides first.** Find where the platform's evidence would hold the thing:
   - which structures (`REGISTER.tsv` names each and what it holds);
   - which runs (`index/runs.tsv`, `run-notes.tsv`);
   - which help, docs or API corpora;
   - what `GAPS.md` says isn't held.

   Record what you read in `guides`.
2. **Search.** Use `corpus_search.py` in every language the platform holds: English, and Arabic too for Salla and Zid, and for Shopify's Arabic help pages where it helps. Search with the thing's own words and the platform's names for it. Use `held_index.py` for an address you expect. Search the concern map with `class_slice.py search` too, with terms Q3's batch didn't use. Record each search in `searched`: the tool, the terms and the platform.
3. **Where it's held,** read the document at its place, and record a statement for each thing it shows that bears on the miss: what the platform does, where it puts it, who does it, its limits.
   - Quote verbatim and cite at a commit (below). Test each quote with `quote_check.py` before you write it.
   - Prefer the document that states most: a help page or an API reference over a title or a list entry.
4. **A place of its own.** Say whether the platform gives the thing a place of its own, by B-extent's rule: an admin section or route, an API group, a plan line, or an app category. A single feature flag, or a setting on a page, isn't one. Name the kind and the statement that shows it, or write `none`.
5. **The capability.** Name the model's capability whose thing it is. Find it with `class_slice.py caps --terms`, with `q3.py where` on a statement of the same page, or with `land_points.py cell`.
   - Where no capability is its thing and some platform gives it a place of its own, write `new`.
   - Where no platform gives it a place of its own, it is a feature of the capability whose thing contains it: name that capability.
6. **Where it isn't held,** after the guides and the searches, name the run that could capture it, from the repository's own catalog: a journey, a held store or instrument, or the docs or help pages its `GAPS.md` lists as not held. Where no run can, write `none: <why>` (a paid plan, a document, a country). That a page exists that would hold it is an assumption: say so.

Something held in a repository but in no statement of the concern map is held. Say so in the reading.

## Statements and citations

Write them in `studies/class-model/q3/statements/<batch>/<platform>/`, one folder for each platform with something held.

**`statements.tsv`:**
- `stmt_id`: `Q3-<XX>-<n>`. XX is the platform's prefix: SH, SA, WC, ZD or BC. n runs from 100 to 199 in batch A and from 200 to 299 in batch B.
- `miss`: the miss's id.
- `placement`: what the statement tells:
  - `where`: the place the platform gives it;
  - `decides`: a rule, a setting, or who sets it;
  - `responsible`: who does it or answers for it;
  - `boundary`: a limit, condition or exception;
  - `reason`: why.
- `identifier`: the page's title, or the API's name.
- `statement`: verbatim, a sentence or the shortest whole part that says it.
- `scope`: a store, plan, country or release condition the source states, or empty.
- `cite_ids`.
- `note`: empty, or what a reader needs, such as "inference" where the statement is read from a name.

**`citations.tsv`:**
- `cite_id`: `Q3-<XX>-C<n>`, in the same range.
- `source`:
  - a held file, as `<repository>@<commit>:<path>`, at the repository's current commit (`git -C <repo> rev-parse --short=9 HEAD`);
  - a record of a fetch archive, as `<repository>@<commit>:<path to fetch.warc.gz>`, with the record's offset as the locator;
  - WooCommerce's release, as `woocommerce-11.2.1:<path>`.
- `locator`: `line N` for a file, or the record's offset for an archive.
- `quote`: verbatim, holding the statement.
- `source_date`, `date_basis`, `accessed`, `access_path`: as the source shows them, or empty.

Every file is tab-separated, with a header row, no quoting, and no tab or newline inside a field.

## Output

**`studies/class-model/q3/misses-<batch>.tsv`**, one line per miss and platform, every platform, held or not:
- `miss`, `platform`.
- `held`: `yes` or `no`.
- `statements`: its statement ids, `;`-separated, for `yes`.
- `place`: `none`, or `<kind>: <statement id>`, `;`-separated, the kind one of admin route, admin section, API group, plan line or app category.
- `capability`: a cap_id, `new` or `none`. `none` only where it isn't held and no capability is its thing.
- `guides`, `searched`.
- `capture`: for `no` only.
- `reading`: a reading, marked as one: what the platform does with the thing, in a sentence or two.

**`studies/class-model/q3/notes-misses-<batch>.md`:**
- for each miss, what each platform holds, and what you made of it: a capability, a feature of one, or detail;
- problems with this brief or the scripts.

Check with `python3 -I method/q3_misses.py check --batch <batch>` until it prints no problem. It tests every quote against its source.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, Q3's batch files or the subjects'. Write only your batch's files, and make no commits.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, say what would settle it.

## How to work, keeping your context small

- `corpus_search.py`'s caches are built. A search takes seconds to a minute. Keep its output short with `--max`, and narrow it with `--with`.
- Read a long document in parts, with `quote_check.py --text`, `sed -n` or `grep -n`, never whole.
- Write your files as you go.

## Report

Back to the coordinator:
- for each miss, what each platform holds, with statement ids;
- its place of its own, if any;
- the capability, or `new`;
- the capture, where it isn't held;
- any problem;
- the checker's final line.
