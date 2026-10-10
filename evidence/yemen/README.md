# Yemen evidence

Raw copies of the sources behind the Yemen payment work, kept so that citations keep resolving and changes can be seen. Everything else in this repository is a claim about evidence; this folder is the evidence.

## Rules

- **Runs are not edited.** A run folder is one capture session. After it ends, files are only ever added beside it in a new run, never changed.
- **Each run states where it was fetched from.** A source can look different from inside and outside Yemen, and some Sana'a sites can only be reached from inside.
- **Sources dated before 2023 are historical.** They show what a document said, or what happened then. They do not establish 2025–2026 status, so a current-status claim needs a source from 2023 or later.
  - Each manifest row has an `age_class`. The dates are automatic hints, taken from the URL, the page's metadata or the PDF's metadata, and should be checked whenever a claim depends on one.
  - An undated page captured live shows what its publisher displayed on the capture date, nothing more.
- **No summaries inside a run.** Interpretation belongs in the studies, not next to the source.

## Runs

| Run | What it holds |
| --- | --- |
| `runs/20261010T050304Z-cited-sources/` | The 262 web sources cited in `yemen-setup-options/report.md` and its five Yemen notes. See that run's README. |
| `runs/20261010T051708Z-community-clients/` | The 13 community-written payment client repositories the notes cite, copied at a fixed commit. See that run's README. |
| `runs/20261010T061420Z-sanaa-rules-search/` | The 83 documents found by the Arabic-first search for Sana'a-side rules. 66 were captured; 17 are blocked from outside Yemen. |
| `runs/20261010T072550Z-sanaa-operators-search/` | The 99 pages found by the Arabic-first search for wallets, banks, couriers and Sana'a sellers. 93 were captured; 6 are blocked from outside Yemen. |
| `blocked-evidence-founder/` | 15 pages the founder saved from inside Yemen on 10 October 2026: the Sana'a central bank's list of electronic payment companies, Saba's text of the central bank's May 2024 ban decision, Yemen Kuwait Bank's ONE Cash page, and 12 other sources blocked from outside Yemen. Its `manifest.tsv` maps each file to the fetch list. |

Other folders:

- `finding-aids/` holds the search agents' lists of sources found. These are not evidence.
- `derived/` holds page images and OCR text for scanned PDFs.

## Adding sources fetched inside Yemen

Some Sana'a-side sites refuse or cut connections from outside Yemen. `to-fetch-from-yemen.md` lists them, with exact addresses where known. To add what you fetch:

1. Make a folder `runs/<UTC time>-founder-<short label>/`, for example `runs/20261012T090000Z-founder-sanaa-cby/`.
2. Put each file in it exactly as you received it:
   - PDFs as downloaded;
   - web pages saved as a single file (`.mhtml`), plus a full-page screenshot.
3. Add `sources.tsv` with one line per file, in these columns:

   `file	url	fetched_at	fetched_from	method`

   For example: `cby-circular.pdf	https://…	2026-10-12 09:10 (Sana'a time)	Sana'a, home connection, no VPN	browser download`

4. Write nothing else: no summary and no opinion. Agents add fingerprints when the files arrive.

A single-file browser save also works, like the files in `blocked-evidence-founder/`. Such a file records its own address and save time, so it needs no `sources.tsv` line.

Raw captures that show personal data, such as phone numbers, names or balances, stay in this private repository.

## Attestations

What the founder has seen but not recorded goes in `attestations/`, one file per observation, using `attestations/TEMPLATE.md`. An attestation is a dated claim with a named source, the same standing a seller's confirmation has in Sharrwah's payment model.

- **An attestation can:**
  - confirm a cited source;
  - fill a gap the sources mark as unconfirmed, as provisional, with a capture requested before going live;
  - flag a conflict with a source, which then becomes a capture task.
- **An attestation can never:**
  - settle a type or a range of options on its own;
  - outrank a capture.
