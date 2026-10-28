# other-product-class

Evidence of what e-commerce platforms other than Shopify and Salla state and show about themselves, captured at the
source. Shopify is held in observed-sh and Salla in observed-sa. Each platform here has a folder of its own; the
capture tools are shared.

Nothing here interprets a platform. Names written by this capture (run labels, structure ids, run notes) are finding
aids, not platform wording. Where a platform organizes its own offering (a route manifest, navigation, plan
policies, a permission list), that organization is held in the platform's own shape, labels and order.

## Platforms

| Folder | Platform | Start at |
| --- | --- | --- |
| [zid/](zid/) | Zid (zid.sa): its merchant dashboard, seen on the demo store Zid opens to every visitor | [zid/README.md](zid/README.md) |

## Layout

Each platform folder holds:

| Path | Holds |
| --- | --- |
| `<platform>/raw/runs/<run-id>/` | One folder per run, as the run wrote it. A browser run: `run.json` (platform, time range, tools, the network path the platform saw), `actions.jsonl` (one row per step: intent, target, landed URL, title, page language, outcome), `commands.jsonl` (the commands as given), `steps/NNN.aria.yaml`, `NNN.text.txt`, `NNN.html`, `NNN.png` (accessibility snapshot, visible text, rendered HTML and screenshot after each step; `NNN.frame-K.*` for child frames), `trace.zip` (the Playwright trace: DOM snapshots, every request and response with its body), `answers.jsonl` and `answers/` (every JSON answer the pages received and every write they sent, from the trace). A fetch run: `run.json`, `urls.txt`, `fetch.warc.gz` (every response as received), `fetch.cdx`, `wget.log`. |
| `<platform>/structures/REGISTER.tsv` | Every self-description of the platform seen (route manifest, locale files, plan policies, …), with where it was seen and where it is held. |
| `<platform>/structures/<id>/` | One structure: `meta.json` (source, shape as observed, counts), `source.*` (the bytes as received) and `items.jsonl` (one item per line, as the source states it). |
| `<platform>/index/runs.tsv` | Every run: kind, label, time range, steps or URLs, files, size, tool, network path, notes. |
| `<platform>/index/run-notes.tsv` | What is unusual about a run. |
| `<platform>/index/instruments.json` | The accounts, stores and browser the runs used, each fact with the run it came from. |
| `<platform>/index/ledger/` | The platform's own lists (its route manifest, …) entry by entry, each joined to the run steps that hold it. |
| `<platform>/index/SHA256SUMS` | A hash of every file of every finished run. |
| `<platform>/GAPS.md` | What is not held yet, why, and how it can be. |
| `capture/` | The tools that made all of it. |
| `docs/` | [OPERATING.md](docs/OPERATING.md) (how to run captures), [PLAN.md](docs/PLAN.md) (status, and how new work starts), [LOG.md](docs/LOG.md) (dated record of the work). |

## What is in git

Everything a run writes, as written: traces, screenshots, HTML, answers and archives included, with tokens, cookies
and passwords as received. A file over GitHub's 100 MB limit is held as ordered parts (`trace.zip.00`, `trace.zip.01`,
…; `cat trace.zip.?? > trace.zip` gives it back; its hash is in the run's note). Not in git: `.env` (the accounts'
sign-in store), the capture browsers' profiles, `.venv` and `node_modules`.

## Citing

`other-product-class@<commit>:<path>[:<line>]`. Every run's bytes can be checked with
`sha256sum -c <platform>/index/SHA256SUMS` from the repository root. The same commits, with the same ids, are on the
knowledge map's branch `evidence/other-product-class` (github.com/Hamza-ye/sharrwah-knowledge-map), pushed after
every push here (`docs/OPERATING.md`, "After any run").
