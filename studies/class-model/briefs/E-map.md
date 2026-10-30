# Brief: the evidence map, how the held evidence is organized and how far it reaches (Stage 4A)

**What this is.** The work reads five reference platforms through what the evidence repositories hold:
- observed-sh, for Shopify;
- observed-sa, for Salla;
- other-product-class, for Zid, BigCommerce and WooCommerce;
- this repository's own captures and saves, in `evidence/`.

Each repository records how it captured what it holds, what each platform lists as existing (its **denominators**: sitemaps, route manifests, navigation, plans, catalogs), and what is held against each list (its **ledgers**). Agents that read the evidence have relied too much on keyword search, and missed what is held (the founder, 30 October; `studies/class-model/held-vs-read.md`).

The evidence map gives every later reader, capture plan and coverage judgement the same entry point. For each platform, it says:
- **which surfaces exist**, and how the platform lists them;
- **what is held of each**, how it was captured, in what readable form, and where;
- **how the surfaces relate**, such as a help page naming an admin route, a route gated by a permission, an API object behind a page, or a plan line naming a feature;
- **how to find a thing in them**, by structure first;
- **what is out of reach**, and why.

It records the repositories' own words and numbers. It judges no platform, places nothing on the class's model, and requests no capture.

**Read only this brief and:**
- **observed-sh** (`/home/user/observed-sh`) and **observed-sa** (`/home/user/observed-sa`):
  - read whole: `README.md`, `docs/READING.md`, `docs/GAPS.md`, `docs/OPERATING.md`, `structures/README.md`;
  - read by their rows and counts: `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, `index/ledger-summary.tsv`, `index/denominators/SUMMARY.tsv` where it exists, and the headers and a sample of rows of each `index/ledger/*.tsv`;
- **other-product-class** (`/home/user/other-product-class`):
  - read whole: `README.md`, `docs/OPERATING.md`, and each platform folder's (`zid/`, `bigcommerce/`, `woocommerce/`) `README.md` and `GAPS.md`;
  - read by their rows: each platform folder's `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, and `zid/index/ledger/`;
- **this repository's evidence:**
  - `evidence/product-class/README.md`, and each run's `manifest.tsv` under `evidence/product-class/runs/`, by its rows;
  - `evidence/product-class/blocked-evidence-founder/`, by its file list;
  - `evidence/shopify-engineering/README.md`;
  - `evidence/product-class/woocommerce-11.2.1/`;
- the tools, from their headers: `method/held_index.py`, `method/corpus_search.py`, `method/runs_corpus.py`, `method/quote_check.py`, `method/schema_type.py`, `method/held_vs_read.py`, `method/held_entries.py`;
- `studies/class-model/held-vs-read.md`, `held-vs-read.tsv` and `held/selection.tsv`: what the class's model has read so far.

## What to write, per platform

For each surface the platform has (its admin, its admin's API, its help centre, its developer docs, its legal terms, its plans and pricing, its app store, its partners' portal, its storefront, its mobile apps, its changelog, and any other the repositories name), write:

1. **What it is,** and the platform's own list of it, its denominator:
   - its name and what it holds, such as a sitemap's URLs, a route manifest's routes, or a schema's types;
   - where it's held, at the repository's commit;
   - its size.

   Where the platform publishes no complete list, say so.
2. **What is held against it:**
   - the ledger's statuses and counts, or the register's;
   - the runs that captured it, and their kind (fetch, browser sweep, journey, answers);
   - what form each holds and how it reads (text in git, an archive record, a step's page text, a saved answer, a structure).

   Name what is held but not readable from the repository, and why.
3. **How it was captured, and its limits:**
   - the instrument: the store or account, its plan, its country, the language;
   - what the guard or the operator stopped before;
   - what GAPS.md says isn't held, and why: a paid plan, a document, a country, an instance never made.
4. **How it relates to the other surfaces,** as the platform's own bytes or the capture's indexes show it:
   - a help page naming an admin route;
   - a route gated by a permission or a plan;
   - a page calling an API operation;
   - a plan line naming a feature;
   - an app category for a function.

   Cite where each relation is recorded.
5. **How to find a thing in it, by its structure:**
   - which list to read first;
   - which index joins it to the others;
   - which tool reads it, and with what arguments;
   - what a keyword search there misses, such as Arabic forms, titles that don't hold the term, or an archive held in parts.

   One worked path per surface, from a capability's name to the page or entry that holds it, using a thing of your choice that no row of `held/selection.tsv` or Q3's misses names.
6. **What the class's model has read of it,** from `held-vs-read.tsv` and `held/selection.tsv`, without judging what it should read.

End each platform with **coverage**, from the repositories' own numbers. For each surface:
- its denominator;
- what is held;
- what is readable;
- what the model has read.

Say which of these can't be counted, and why.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- A repository's own descriptions (its README, its register's columns) are its words about itself: cite them as such. Where they and the bytes disagree, the bytes are the evidence; say so.
- The founder's words are never evidence of what a platform does.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Write only the files below, and make no commits.

## How to work, keeping your context small

- Read the guides whole once, at the start. Read registers, run indexes and ledgers by their counts and a few rows, with `cut`, `awk` and `grep`, never whole.
- Write each platform's part as you finish it, never at the end.

## Output, in `studies/class-model/evidence-map/`

- **`<platform>.md`,** one per platform, as above.
- **`README.md`:**
  - what the map is;
  - the repositories, their commits, and how a reader starts;
  - the relations that cross platforms, such as this repository's captures of Zid's, BigCommerce's and WooCommerce's public pages beside other-product-class's admin captures;
  - the tools, each with what it reads, what it misses, and the cost of a run.
- **`coverage.tsv`:** one row per platform and surface:
  - `platform`, `surface`;
  - `denominator`: what lists it, and where;
  - `listed`, `held`, `readable` and `read_by_model`: counts, or `not countable: <why>`;
  - `held_where`: repositories and paths;
  - `note`.

## Report

Back to the coordinator:
- for each platform, its surfaces with their coverage, in one line each;
- what is out of reach, and why;
- the tools' faults you met;
- anything in the repositories' guides that contradicts their bytes.
