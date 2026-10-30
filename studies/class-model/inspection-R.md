# Inspection of the dry run's review brief (`R-dry-run.md`)

An inspection in Fagan's sense (1976): the brief is read before any agent runs it, for what would make a reviewer that follows it produce a wrong, slanted or uncheckable review. The inspector wrote none of it. Every judgement below is marked as a **Reading**; facts cite a file and line at the commit named here.

## What was read, at which commit

- **The brief,** `studies/class-model/briefs/R-dry-run.md`, whole (50 lines; sha256 `46fe6830…2911`). The inspection began at `aaf68c80`, with the brief untracked, and ended at `96439cc5`. The brief's bytes are the same throughout, and are committed at `aaa4b3fc`.
- `studies/class-model/briefs/B-extent.md`, whole (135 lines; sha256 `48e1017d…82ad`, unchanged throughout).
- **The scripts,** whole: `method/class_slice.py`, `method/check_class_part.py` and `method/class_kinds.py`.
  - `class_slice.py` changed at `23461ca6`: `--concerns` now takes several arguments, and lines after 76 moved down by 2. Its line numbers below are at `96439cc5`.
  - The other two are unchanged.
  - Commands were run on SH-C-020, SA-C-021, WC-C-064 and the other domain-B concerns.
- **For single checks:** `PLAN.md` lines 204 to 240, `STATE.md` line 148, `studies/class-model/inspection-B.md`'s headings, its proposed tests (lines 448 to 496), the coordinator's lines 539 and 541, and the re-inspection's last findings and verdict (lines 817 to 858), and `architecture/plan.md` line 49, committed at `4d32c086` during this inspection.
- **`studies/class-model/scope.tsv`,** as the coordinator committed it at `23461ca6`, for domain B's concerns. It gives domain B 40 concerns, of which the dry run's three platforms hold 30: Shopify 11, Salla 11, WooCommerce 8.
- **The inspector's fixtures** are in its scratchpad: `model/`, a copy of `studies/class-model/` with a header-only `B-anchor`, and `fx/`, two fixture parts. They test the scripts and the proposed commands. They are not readings of the evidence.

## Summary

| # | Finding | Verdict |
|---|---|---|
| 1 | Running the checker as told (line 8) rewrites the parts' derived files, against "change nothing" (line 37), and hides stale ones | must fix |
| 2 | The depth rule (line 32) samples what `PLAN.md` line 216 requires in full. Its own terms name no checked set, and leave out rows the brief and the checker mark as risky | must fix |
| 3 | Joins the parts didn't make are never tested. The re-inspection's tests 24 and 25 are in neither the checker nor the brief | must fix |
| 4 | The output records only failures. There is no coverage record and no sample method, and the checker's flags need only be read | must fix |
| 5 | No check of the capabilities' names, or of WooCommerce's clean fits into the anchor's shape | must fix |
| 6 | Check 2 restates `own-service` without "the statement names" and "separate", so the maker can come from the reviewer's own knowledge | must fix |
| 7 | Check 1's two bullets each push one way, and leave out B-extent's tests: an extension's admin route, and an own API for an own feature | must fix |
| 8 | Arabic searches: `search` matches substrings, so a singular misses its broken plural, and ة misses ه | must fix |
| 9 | `architecture/plan.md` line 49 leaves a check to this review that the brief doesn't hold | must fix |
| 10 | Other things no check reaches: qualities and slot fillers left out, citations across domains, moves, a note's inference, recorded gaps | optional |
| 11 | The kind-rule check: `open` is defined more narrowly than computed, the question invites judging the rule, three of five platforms, scoped placements | optional |
| 12 | The reading order puts the parts' arguments before the evidence | optional |
| 13 | Check 8 has no command and no stated set of concerns | optional |
| 14 | The output's form: a criterion for verdicts, fixes as rows, runnable tests, the state read, the checker's problems, context, `--help` | optional |
| 15 | Check 7 tests cross-domain rulings against the definitions, though the checker allows only `apart` for 9 of them | must fix |

**Where each question asked is answered:**
- what presupposes an answer or steers: 5, 6, 7, 11 and 12;
- checks that can't be carried out as written, or at a reasonable size: 1, 2, 8 and 13;
- missing checks: 3, 5, 9, 10 and 15;
- the depth rule: 2, with 3 and 5 for what it would still miss;
- whether the output can be acted on: 4 and 14.

**Reading:** none of the fixes needs a change to the plan or to the scripts before the review can run. Each is a sentence or a command in the brief. Three would also be better in the checker, for every later part: finding 1 (an option to write the derived files elsewhere), finding 3 (tests 24 and 25 as flags) and finding 13 (the statements no cell cites).

## Findings

### 1. Running the checker as told changes the parts' files (must fix)

**The brief's words.** Line 8: "the checker's output on each part: run `python3 -I method/check_class_part.py studies/class-model/parts/<part>` yourself". Line 37: "**Change nothing** but your own file."

**Problem.** The two can't both be followed. The checker writes into the folder it checks, so the reviewer's run rewrites each part's `derived.tsv` and `derived-qualities.tsv`. Where a part's rows changed after its own last check (a coordinator's correction, or a part that didn't re-run), the rewrite also erases the one sign of it: the reviewer can no longer see that the part's derived files were stale.

**Evidence.**
- `method/check_class_part.py` lines 496 to 512 open `os.path.join(d, "derived.tsv")` and `os.path.join(d, "derived-qualities.tsv")` for writing, where `d` is the part's folder given on the command line.
- `method/class_kinds.py` lines 39 to 41 read `derived.tsv` from each part's folder, and exit if it is missing, so the kinds (brief, line 9) depend on those files.
- The scripts can run on a copy: `class_slice.py` line 41 takes the model's folder from `CLASS_MODEL_DIR`, and both other scripts import it (`check_class_part.py` line 18, `class_kinds.py` line 20). `python3 -I` ignores only `PYTHON*` variables, so the variable still applies. Tested: with `CLASS_MODEL_DIR` set to a copy in the inspector's scratchpad, and a `B-anchor` there holding only headers, the checker read the copy's `scope.tsv` (22 problems: the 22 anchor concerns not landed) and wrote both derived files into the copy. `git status` showed nothing changed in the repository but this file.

**Fix.** Replace line 8 with: "Copy `studies/class-model/` to your scratchpad (`cp -r studies/class-model $S/model`), and run every script with `CLASS_MODEL_DIR=$S/model`: the checker on each copied part in order (`B-anchor`, `B-woocommerce`, `B-backfill-woocommerce`), then `class_kinds.py` and `class_slice.py model`. Then `diff` each copied `derived.tsv` and `derived-qualities.tsv` with the part's own. A difference is a finding." Line 37 then holds as written. For every later part, the checker could instead take an option to write its derived files elsewhere.

### 2. The depth rule samples what the plan requires in full (must fix)

**The brief's words.** Line 15: "**Every placement against all of the concern map's statements** for the concerns behind the cell, under all five of Q1's placements". Line 32: "Check every cell whose kind hinges on one placement (a count of 0 or 1), every join on role, every strained fit and every `none-held` cell. Check the rest by a sample you state, with how you chose it."

**Problem.** Line 32 turns line 15's "every placement" into a sample for every capability with a count of 2 or 3. That departs from the plan, which the brief can't change. And the count, not only the kind, is what the model reports: a wrong `core` in a capability counted 2 leaves the kind unchanged, but puts a wrong count and a wrong placement on the founder's page (`PLAN.md` line 222: "which platforms establish each and where"). **Reading:** the sample saves little. The domain's own statements are small enough to read whole, once per concern. What costs is the search beyond them.

**Evidence.**
- `PLAN.md` line 216: "The review checks every placement against all of Q1's statements for the concern, not its `where` rows alone." `STATE.md` line 148: "the review of its output, which checks every placement against all of Q1's statements".
- The size, from `scope.tsv` at `23461ca6` and `class_slice.py statements`, run by the inspector: domain B gives Shopify 11 concerns with 190 statements (35,594 bytes as printed), Salla 11 with 214 (52,120 bytes), and WooCommerce 8 with 93 (12,019 bytes). That is 497 statements and about 100 KB for the dry run's three platforms. The concerns of other domains that name B under `also` add 255 statements (Shopify 109, Salla 119, WooCommerce 27).
- The cost of `search`, also run by the inspector: `product` finds 226 Shopify statements, `product;منتج` 301 Salla statements, `product` 159 WooCommerce statements, and `inventory` 98 Shopify statements. Each such search prints more than one platform's whole domain.

**The rule's own terms are also unsound. Reading:**
- **It names no checked set.** A cell has no kind; a capability does. For a capability counted 1, "every cell whose kind hinges on one placement" may mean its one placing cell, or all its cells, so two reviewers would check different rows.
- **Its "every" leaves out rows the brief and the checker mark as risky:**
  - check 1's own "take every cell whose `where` statements name only an app store…" and "every `core` that rests on API objects" (lines 16 and 17);
  - every `own-service`, which the checker flags for the reviewer (`check_class_part.py` lines 368 and 369);
  - joins on terms. Domain B has one word for two things that Q1's homonym list doesn't hold (finding 5).
- **What it does catch, it catches only for the kind.** With a sample for the rest, a count can be wrong while its kind is right.

**Fix.** Replace line 32 with:
> **Depth.** Every cell's placement against every statement of its concerns (checks 1 and 2): read each domain-B concern's statements once, under all five placements, and test every cell and evidence row that rests on them. The searches beyond the domain's concerns: for every cell listed under check 1's two bullets, every cell of a capability counted 0 or 1, and every `none-held` cell; for the other cells, a sample drawn as the output section says. Checks 3 to 9: every row.

"The concerns behind the cell" (line 15) should also be defined, since a back-fill cell and a `none-held` cell may have no concern of their platform landed in the capability: "the concerns of its platform landed in the capability, its parent or its children, and the concern of every statement it cites".

### 3. Joins that weren't made are never tested (must fix)

**The brief's words.** Line 19: "**Each join:** a Q1 match, terms, identifiers, a definition, or role. For a join on role, do both sides' cited definitions show the same thing? For a join on terms, is it the same object, or one word for two things? Every strained fit: should it be split?"

**Problem.** Check 3 tests the joins a part made, and asks only whether to split. Nothing asks whether two capabilities should be one: a concern landed `single`, or apart from the other concerns of its Q1 match, while another platform's concern is the same thing. **Reading:** a missed join changes kinds, not only names. If one platform's concern sits in capability X with `core`, and the other's in capability Y with only `extension-point`, Y comes out a `slot` that, joined, would have been one `class` capability. The dry run is where that would first show.

**Evidence.**
- The re-inspection proposed the two tests that would catch it: `inspection-B.md` line 494 ("no two capabilities whose cells cite the same statement key, unless one is the other's `parent` or `reading` names the split") and line 495 ("Every Q1 match's concerns land in one capability, or in a parent and its children"). The coordinator's check put tests 1 to 19 and 21 in the checker and said "The review adds what it finds" (line 541).
- Neither is in the checker. `check_class_part.py` lines 319 to 327 test a landing against its match's other concerns only where that landing's `join` is `match:`. A concern held by a match but landed `single`, or by `terms`, in another capability is not tested. No line compares the keys cited in different capabilities' cells. Line 409 computes `caps_new` and never uses it, so a capability with no concern landed in it or its family also passes.
- Domain B shows the kind of join at risk. `class_slice.py matches --concerns SH-C-021 SA-C-022` prints U-002: "Shopify groups products in 'Collections'; Salla and WooCommerce use 'Categories' (matched together in M-011). Different terms; only function suggests they are the same. Shopify also has 'Product categories' (its product taxonomy) inside SH-C-020." M-011 holds SH-C-020, SA-C-020 to SA-C-023 and WC-C-064, but not SH-C-021. Q1 listed this pair as unclear, so check 7 reaches its ruling. A pair with different terms that Q1 listed nowhere has no check at all. Neither have Zid's and BigCommerce's concerns, which Q1 never matched (B-extent line 28), when their parts run.

**Fix.** Add to check 3:
> - **Joins not made.** Every pair of capabilities, outside one line of parents, whose cells cite the same statement key; every Q1 match whose concerns landed outside one family; every capability with no concern landed in it or its family; every `single` landing whose capability holds statements for another platform. For each: should they be one capability, or one the other's parent? Say what the cited definitions show.

The first list comes from a command the reviewer can run (tested by the inspector on a fixture of two parts):
```
python3 -I -c '
import csv, glob, collections as C
rd = lambda f: csv.DictReader(open(f, encoding="utf-8", newline=""), delimiter="\t", quoting=csv.QUOTE_NONE)
par = {r["cap_id"]: r["parent"] for f in glob.glob("parts/B-*/capabilities.tsv") for r in rd(f)}
up = lambda c: {c} | (up(par[c]) if par.get(c) else set())
cites = C.defaultdict(set)
for f in glob.glob("parts/B-*/evidence.tsv"):
    for r in rd(f): cites[r["key"]].add(r["cap_id"])
for k, cs in sorted(cites.items()):
    cs = sorted(cs)
    apart = [(a, b) for i, a in enumerate(cs) for b in cs[i+1:] if a not in up(b) and b not in up(a)]
    if apart: print(k, "cited by", " ".join(cs), "outside one family:", apart)'
```
run from the model's folder (the scratchpad copy of finding 1). Tests 24 and 25 should also go into the checker as flags, for every later part.

### 4. The review records only what fails, so what wasn't checked can't be told from what holds (must fix)

**The brief's words.** Line 3: "report counter-evidence and missing evidence, not agreement." Line 32: "Check the rest by a sample you state, with how you chose it." Lines 42 to 48: the output is findings, the kind rule, the conventions and the tests. Line 8: "read its flags".

**Problem.** Nothing in the output says which rows were checked, by which check, and what was found. A cell with no finding may be right, or may not have been looked at, and a checker of the review can't tell which. The sample has no size and no method, so a reviewer may pick easy rows, and two reviewers would check different things. The checker's flags, which B-extent line 113 makes "for the reviewer", need only be read. **Reading:** "not agreement" is right for the findings, but read literally it also stops the reviewer from recording what held. And the dry run's purpose (line 3: "What you find sets the conventions and the checker's tests") needs the rate of each kind of error, such as how many `none-held` cells were false, to choose which tests to add. Only a record of what was checked gives that rate.

**Evidence.** The brief's lines above. B-extent line 113: "Its flags are for the reviewer: answer each one you can in your notes." The checker prints four kinds of flag: a statement of another domain cited without `also` (`check_class_part.py` lines 365 to 367), every `own-service` (368 to 369), a `none-held` cell whose terms find statements (386 to 387), and `core` resting only on boundary statements (390 to 392).

**Fix.**
- Line 3: "report counter-evidence and missing evidence as findings. Record what you checked and found to hold in the coverage table, without argument."
- Add to the output: **`studies/class-model/review-dry-run-coverage.tsv`**, with `part` · `file` · `line` · `row` (the row's own key: `cap_id`, `cap_id/platform`, `cap_id/platform/key`, a `concern_id` or a `candidate_id`) · `check` (its number) · `result` (`holds`, or the finding's number) · `searched` (the terms and platform of each search run for the row, with its count of hits). Every checker flag is a row, with how it was resolved.
- Line 32: the sample is drawn by a stated command with a fixed seed, at least a third of the rows it covers and at least two per platform and per `supports` value, and the command is in the review.
- The summary then gives, per check, the rows checked, the rows that failed, and the share.

### 5. Nothing checks the capabilities' names, or whether the mapping was forced into the anchor's shape (must fix)

**The brief's words.** Checks 1 to 11 (lines 15 to 30) test placements, joins, grains, cells, areas, rulings, uncited statements, side files, kinds and conventions. None tests a capability's name. Check 3 (line 19) tests strained fits, but not clean ones.

**Problem.** B-extent's rule on names has no check: "**The name** uses both platforms' terms, or a neutral term that names both" (B-extent line 64). The anchor's names are what every later part reads to land its concerns (B-extent line 76, through `class_slice.py model`, which prints each capability's name with its cells' terms), and what the founder's page shows (`PLAN.md` line 222). **Reading:** a name in one platform's word carries that platform's shape into the mapping of WooCommerce, Zid and BigCommerce. That is where the model leans toward one platform, and the review is the last place before domains A and C to G run where it can be caught. And WooCommerce is mapped onto a structure that "follows [Shopify's and Salla's] own groupings" (B-extent line 8). Its clean fits, not only its strained ones, are where that structure is imposed, and there are only 8 of its concerns in domain B.

**Evidence.** U-002, quoted in finding 3: Shopify says "Collections" where Salla and WooCommerce say "Categories", and "category" also names Shopify's product taxonomy inside SH-C-020. A capability named "Collections" takes Shopify's word, and one named "Categories" takes Salla's and WooCommerce's while also naming a different Shopify object. Q1's list of the same word naming different things holds six cases, none of them domain B's (`class_slice.py homonyms`: supported countries, complaints, logs, rate limit, MCP / UCP, order limit), so it gives the reviewer no lead here. The size: `scope.tsv` at `23461ca6` gives WooCommerce 8 domain-B concerns.

**Fix.** Add a check:
> **The names, and the anchor's shape.** Each capability's name: does it use the terms of every platform landed in it, or a neutral term that names them all, and does it avoid a word that names something else on one of them? Every WooCommerce landing, clean or strained: does WooCommerce's own grouping, in its `where` identifiers, cut the same way as the capability it landed in? If not, say whether to rename, re-cut, or mark the fit strained.

### 6. Check 2 restates `own-service` more loosely than B-extent, in a way that can change counts (must fix)

**The brief's words.** Line 18: "A product made by the platform's own company is `own-service`."

**Problem.** B-extent's test is narrower: "the statement names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service that does it" (B-extent line 95). The paraphrase drops "the statement names", so the maker can come from what the reviewer knows rather than from a statement. It also drops "separate", so the platform's core, which is also a product its company makes, fits the words. `own-service` counts as `core` does (`class_kinds.py` line 22: `OWN = {"core", "own-service"}`). **Reading:** a reviewer following line 18 can turn an `extension-point` into `own-service` on its own knowledge, and so a `slot` into a `class`. That is the founder's question (slot or class), decided by what is not evidence.

**Evidence.** Four of WooCommerce's 8 domain-B concerns are marketplace extensions: WC-C-100 (Subscriptions), WC-C-101 (Bookings and appointments), WC-C-102 (Memberships) and WC-C-104 (Merchandising: bundles, gifts, product options and others). Their `where` statements are marketplace categories, such as WC-C-100/where/WC-S-0739 ("Extensions > Merchandising > Subscriptions") and WC-C-104/where/WC-S-0732 ("Extensions > Merchandising > Bundles"). The inspector printed all four concerns' statements at 300 characters, and none holds "woo.com", "developed by", "by woo" or "automattic". The nearest is WC-C-100/decides/WC-S-5351: "WooCommerce Subscriptions is a premium extension that allows you to sell products and services with recurring payments". It gives the product's name, which carries the platform's brand, and no maker. WC-C-050/where/WC-S-0697 ("Extensions > Developed by Woo") names a category, not which extensions are in it, and is a statement of domain F.

**Fix.** Replace line 18's last two sentences with: "`own-service` only where a cited statement names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service (B-extent line 95). Never decide the maker from what you know. Whether a product's name that carries the platform's brand names its maker is a convention for the coordinator: list those cases. A statement that makes the merchant or buyer responsible is `shows`, never `outside` (line 98)."

### 7. Check 1's two bullets each push one way, and leave out B-extent's tests (must fix)

**The brief's words.** Line 16: "Read the concern's `decides` statements, its plan lines, entitlements and settings, before accepting `extension-point`: a plan line or an admin route can show the platform doing it itself." Line 17: "every `core` that rests on API objects, scopes or webhook topics: does a statement show the platform doing it, or only apps doing it through the API?"

**Problem.**
- **Line 16 makes an example into a rule.** An extension's or app's own settings often sit under the platform's admin. Read as written, such a route moves an `extension-point` to `core`, though it shows the extension, not the platform, doing the work.
- **Line 17 leaves out B-extent's test.** B-extent counts "its own API for its own feature" as `core` (line 94). An API is `extension-point` only where "its statements say apps or partners use it to do the work" (line 96). Line 17 asks instead whether "a statement show[s] the platform doing it". Read literally, that demands a statement beyond the API, and demotes `core` that B-extent's test supports.

**Reading:** both bullets are good questions, but each names only one direction's evidence. Followed as written, they move placements by the bullet's wording, not by the test the parts were given.

**Evidence.**
- For line 16, WC-C-100/where/WC-S-5350: "WooCommerce > Settings > Subscriptions", an admin route with `[scope: WooCommerce Subscriptions]`, the premium extension of WC-S-5351.
- For line 17, domain B's evidence leans on API statements. WC-C-064 has 39 of its 51 statements under `boundary`, such as WC-C-064/boundary/WC-S-0100 (`'products' => 'WC_REST_Products_Controller'`). SA-C-021 has 6 of 11, such as SA-C-021/boundary/SA-S-1051 ("Product Option Templates", a folder of Salla's API reference). SH-C-020 has 13 of 35, such as SH-C-020/boundary/SH-S-6098 (the `products/create` topic). Counts are from `class_slice.py statements`, run by the inspector.

**Fix.**
- Line 16: "…before accepting `extension-point`: the platform's own plan line, setting or admin route can show it doing the work itself. A route or setting that an extension or app adds, as its identifier or scope shows (such as WC-C-100/where/WC-S-5350, scoped to WooCommerce Subscriptions), is the extension's."
- Line 17: "every `core` that rests only on API objects, scopes or webhook topics: is it the platform's own API for its own feature (`core`, B-extent line 94), or an API whose statements say apps or partners use it to do the work (`extension-point`, line 96)? Quote what decides it."

### 8. "In every language they use" doesn't say how to search Arabic, and the script matches only substrings (must fix)

**The brief's words.** Line 21: "**Each `none-held` cell:** search the platform's statements yourself, in every language they use."

**Problem.** `search` matches substrings, after folding case, diacritics, hamza seats and tatweel (`class_slice.py` `fold`, lines 70 to 73, and `cmd_search`). An Arabic singular doesn't match its broken plural, and ة doesn't match ه. The checker's own re-search of a `none-held` cell (`check_class_part.py` lines 383 to 387) runs the part's terms and the other platforms' terms, mostly English, so it doesn't cover this either. **Reading:** a reviewer that searches one form of each Arabic word will confirm `none-held` cells that are false, on Salla, one of the two anchor platforms.

**Evidence.** Searches the inspector ran on Salla:

| term | statements |
|---|---|
| نوع المنتج (product type) | 0 |
| أنواع المنتجات (product types) | 4, among them SA-C-020/decides/SA-S-1952, the Salla Plus plan line "إضافة كل أنواع المنتجات" |
| كمية (quantity) | 3 |
| كميه | 0 |
| فرع (branch) | 11 |
| فروع (branches) | 8, of which 7 are not among the 11 |

All 6 statements that "أنواع" (types) finds are missed by "نوع" (type), which finds 10 others.

**Fix.** Add to check 5: "`search` matches substrings, with case, diacritics, hamza seats and tatweel ignored. For Arabic, search each word's singular and its broken plural, and its spellings with ة or ه and ى or ي. Record each term with its count of hits."

### 9. The architecture plan waits on this review for a check the brief doesn't hold (must fix)

**The brief's words.** None: no line of the brief names `architecture/plan.md` or what architecture needs from the model. Check 11 (line 30) asks only what the parts did differently, and what the brief should settle.

**Problem.** The architecture plan was committed after the brief (`4d32c086`, after `aaa4b3fc`), and leaves one of its claims to this review. **Reading:** if the brief isn't changed, no one confirms the claim, and the plan's section 1 rests on it. The claim can fail in domain B itself. A coarse concern landed in a parent, such as SH-C-020 ("Products and variants") with its 13 `boundary` statements, holds webhook topics and scopes that its landing alone can't divide among the children.

**Evidence.**
- `architecture/plan.md` line 49: "The data and events, and what decides each capability, come from the statements of each capability's concerns, so the merge derives them per capability: no part writes more. *To confirm with the dry run's review.*"
- `PLAN.md` line 235: "Its first part, what architecture needs to know, is drafted with the dry run's conventions, so the extent records what architecture will need before the other domains run."
- `check_class_part.py` lines 496 to 506: `derived.tsv` holds each cell's `placed_as`, `where`, scopes and gaps, but not its `boundary` or `decides` statements.

**Fix.** Add check 12: "**What architecture needs** (`architecture/plan.md` line 49). For each capability, can its data and events (its concerns' `boundary` statements) and what decides it (their `decides` statements) be derived from the concerns landed in it and the keys its cells cite, without a part writing more? List the capabilities where they can't, such as a parent's children sharing one coarse concern, and say what the merge would need." Add `architecture/plan.md` line 49 to the brief's reading list.

### 10. Other things the parts could get wrong that no check reaches (optional)

**Problem, evidence and fix**, one by one:
- **Qualities and slot fillers left out.** Check 9 (line 25) checks "each one's value, scope and capability": the rows that exist. The checker tests only that their `cap_id` and key resolve (`check_class_part.py` lines 424 to 442). A limit in a cited statement with no quality row passes both. Domain B states such limits: SH-C-020/decides/SH-S-7214 ("Your Shopify plan comes with everything you need to create up to 100 variants for each of your products"), and SH-C-024/decides/SH-S-5762 to SH-S-5764 (`maximumLocations` 2, 10 and 200, each scoped to its plans). **Fix:** add to check 9: "and the ones missing: a limit, certification, uptime or data location in a cited statement with no quality row; a third party or law named as doing it or setting its terms with no slot filler; a third-party filler on a cell with no `extension-point` or `outside`."
- **Citations across domains.** The checker flags a statement of another domain cited without `also` (lines 365 to 367). B-extent line 42 asks that the cell's `reading` say why, "since one statement shouldn't support capabilities in two domains". No check takes these up, and their harm shows only once the other domains run. **Fix:** add to check 11: "every such citation, whether its reading says why, and the convention to set before domains A and C to G cite the same statements."
- **Moves.** A `moved:<domain>` landing takes a concern's statements out of domain B's cells. No check asks whether the move is right. **Fix:** add to check 3: "each `moved:` landing: is the concern's main subject in the named domain?"
- **A note's inference.** `class_slice.py statements` flags a statement whose note holds inference, and B-extent line 110 says "A note's inference never counts". No check asks whether a placement rests on the note rather than the statement. Domain B has one: WC-C-100/decides/WC-S-5351, with "Inference: as a premium extension, it runs only where the merchant has bought and installed it." **Fix:** add to check 2: "a placement on a statement flagged `[note: inference]`: does the statement's own text support it?"
- **Gaps recorded.** B-extent line 42 puts "a statement you need that isn't held" in the notes as a gap. No check reads those gaps. **Fix:** add to check 8: "and the gaps the parts' notes record: is each a gap, or held under a statement the part didn't find?"

### 11. The kind-rule check: what `open` covers, how many platforms, and what the question invites (optional)

- **`open` is defined more narrowly than the script computes it.** Line 29 says "the `open` cases (a count of 0, with some platform `not-stated`)". `class_kinds.py` line 59 also gives `open` where no platform's cell holds statements (`shows` is 0). Could that happen in domain B?
  - Not from a landing: every domain-B concern has statements. The inspector counted, and only SA-C-233, of domain A, has none.
  - Yes from a capability with nothing landed in it, which the checker lets through (finding 3).
  
  The proposal "then applies to all" (`PLAN.md` line 218). **Fix:** "the `open` cases: a count of 0, where some platform's cell is `not-stated`, or where no platform's cell holds statements".
- **The question invites judging the rule, not its inputs.** Line 26: "For each capability, is the computed kind what the evidence supports?" The kind is computed from the cells by the plan's one rule (`PLAN.md` line 218), so it can be wrong only through its cells. **Reading:** asked this way, a reviewer may weigh kinds by its own sense of what a slot is, such as "most platforms leave it to apps", against a rule under which one platform's `core` makes a `class`. **Fix:** "For each capability, would the kind change if its cells were corrected as your findings propose? Apply your proposed fixes to the scratchpad copy (finding 1), recompute, and list each change of count or kind. An objection to the rule itself goes in the kind-rule section, with its cases."
- **Three of the five platforms.** The dry run maps Shopify, Salla and WooCommerce only. `class_kinds.py` prints `no cell` for Zid and BigCommerce, a count is at most 3, and a `slot` or `open` can change when they are mapped. The brief doesn't say so, nor whether to search Zid's and BigCommerce's statements. **Fix:** say both: the kinds are over three platforms, and the review searches those three.
- **Scoped placements count as unscoped ones.** `derived.tsv` keeps each statement's scope (`check_class_part.py` line 503), and `class_kinds.py` never reads it. A `core` resting only on one plan's or one extension's statement counts as fully as any other. B-extent line 111 says "No market's facts decide a capability or its area". Domain B has such statements:
  - SA-C-020/decides/SA-S-1952, the plan line "إضافة كل أنواع المنتجات", scoped to Salla Plus;
  - WC-C-100/where/WC-S-5350, scoped to WooCommerce Subscriptions;
  - SH-C-024/decides/SH-S-5762 to SH-S-5764, scoped to plans and stores.
  
  **Fix:** in the kind-rule section, list every count that rests only on statements scoped to a plan, market or extension, and propose whether, and how, it counts.

### 12. The reading order puts the parts' arguments before the evidence (optional)

**The brief's words.** Line 7: "the parts' files in `studies/class-model/parts/B-*/`, with their `derived.tsv` and `notes.md`", read before the checker's output and the concern map.

**Problem.** **Reading:** the reviewer meets each cell's `reading` and `why`, and the part's notes, before it has read the statements. Its own reading then starts from the part's, a pull toward agreement that line 3's "try to refute it" counters only by intent.

**Fix.** "For each cell under check 1, write your own placement from the concern's statements into the coverage table first (finding 4). Then read the cell's `reading`, its `why`s and the part's notes, and compare."

### 13. Check 8 has no command, and doesn't say which concerns it covers (optional)

**The brief's words.** Line 24: "**What the parts never cite:** statements of domain B's concerns that no cell cites."

**Problem.** No script lists them. "Domain B's concerns" doesn't say whether the 255 statements of the concerns that name B under `also` are in. **Reading:** two reviewers would list different sets, and the coordinator couldn't re-run either.

**Evidence and fix.** Give the command. Run in the scratchpad copy of finding 1 (`R` is the repository's root), it printed all 497 keys of the three platforms' domain-B concerns, as expected with a fixture that cites none:
```
for p in shopify salla woocommerce; do
  ids=$(awk -F'\t' -v p=$p 'NR>1 && $1==p && $3=="B" {print $2}' scope.tsv)
  python3 -I $R/method/class_slice.py statements --platform $p --concerns $ids --width 1 | grep -v '^#' | cut -f1
done | sort > all-B.txt
cut -f4 parts/B-*/evidence.tsv | grep -v '^key$' | sort -u > cited-B.txt
comm -23 all-B.txt cited-B.txt
```
Say that check 8 covers domain B's own concerns, and the `also` concerns' statements only where a search finds them bearing on a domain-B capability. The checker could print the same list, as a count per concern, as a flag for every later part.

### 14. The output's form: verdicts, fixes, tests, and the state read (optional)

- **Verdicts.** Line 44 asks for `must fix` or `optional` with no criterion. **Fix:** "`must fix`: it changes a cell's `held`, `placed_as` or `terms`, a landing, a ruling, a capability's existence, name, parent or area, or a count or kind. `optional`: notes, wording, conventions."
- **Fixes the coordinator can apply.** B-extent line 12 has corrections made "in the part's own files and noted in its `notes.md`". A fix in prose has to be re-derived row by row. **Fix:** add `studies/class-model/review-dry-run-fixes.tsv`: `finding` · `part` · `file` · `row` (its own key) · `field` · `from` · `to`. The coordinator then applies it, and a checker confirms that each row now reads `to`.
- **Tests a checker can run.** Line 48: "the tests the checker should add". **Fix:** "each test as a rule the checker can apply to the parts' files, with the dry run's rows it flags, so it can be written and confirmed on them."
- **The state read.** Line 43 asks for the commit. The parts are written by agents that make no commits, and are committed by the coordinator as they write, as this inspection's own file was. **Fix:** "record the commit, and `git status --short studies/class-model/parts`; if any part file is uncommitted, its sha256."
- **Problems, not flags.** The brief says what to do with the checker's flags, but not with a problem it prints. **Fix:** "a problem the checker prints on a part is a `must fix` finding; go on with the review."
- **Context beyond the statements.** B-extent line 42 lets a part read "context … in the structures they cite", which "informs a reading". The reviewer may read only what its brief names, and the copies aren't named. **Reading:** a part's reading that rests on context can't then be tested. **Fix:** name the copies behind a cited statement (`citations.tsv`, at its commits) as readable where a part's reading says it rests on context.
- **`--help`.** Line 11 says "its `--help` lists the commands". It lists their names only: `argparse` takes the docstring's first line as the description (`class_slice.py`, `main`). What each does is in the docstring (lines 1 to 33) and in B-extent lines 32 to 40. **Fix:** point there.

### 15. Check 7 asks whether each ruling follows from the definitions, but across domains the checker allows only `apart` (must fix)

**The brief's words.** Line 23: "**The rulings on Q1's unclear candidates:** does each ruling follow from the cited definitions?"

**Problem.** Where an unclear candidate holds a domain-B concern and a concern of another domain, the anchor must rule on it, and the checker accepts only `apart`. The ruling then follows from `scope.tsv`'s split, not from the definitions. **Reading:** a reviewer following line 23 will find those rulings unsupported by their definitions, and blame the part for what the scope decided. Or, seeing that `joined` was impossible, it won't ask the real question: whether the scope split the candidate rightly.

**Evidence.**
- `check_class_part.py` lines 467 to 477: `joined:` needs a concern of each side landed in the capability's family, from this domain's landings (`where_landed`). A concern of another domain is never landed here.
- For `apart`, lines 478 to 482 test only the pairs landed here.
- B-extent line 72 makes the anchor rule on every candidate "that holds a Shopify and a Salla concern, one of which you land".
- The inspector's count, from `unclear-matches.tsv` and `scope.tsv` at `23461ca6`: 10 candidates hold a domain-B concern and a concern of another domain:
  - U-005, U-013, U-016, U-020, U-057, U-059, U-060, U-070, U-081 and U-082;
  - for instance U-082 (SH-C-187 in D, SA-C-020 in B) and U-020 (SH-C-060 in C, SA-C-026 in B);
  - in all but U-059, every concern on one side of the Shopify–Salla pair is outside domain B, so the anchor can only rule `apart` on 9 of them;
  - U-070's WooCommerce concern, WC-C-093, is in B, so the WooCommerce part can still join it.

**Fix.** Add to check 7: "Where a candidate's concerns on one side are all in another domain, the ruling can only be `apart`: don't test it against the definitions. Test instead whether `scope.tsv` placed the candidate's concerns rightly, and list those cases for the coordinator." B-extent line 72 could also say what basis such a ruling gives: "`apart`: scope.tsv gives <concern> domain <X>".

