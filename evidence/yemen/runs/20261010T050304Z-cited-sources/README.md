# Run 20261010T050304Z-cited-sources

The web sources cited in `yemen-setup-options/report.md` and its five Yemen notes (regulation and licensing, wallets and e-money, banks and cards, cash and practice, currency and territory). Sources cited only in the analogous-markets note are not included.

- **Fetched from:** a Claude Code cloud container outside Yemen, through the session's egress proxy, on 10 October 2026 (UTC).
- **Fetched by:** Claude Code, with no login and no form submissions.

## How each source was fetched

1. **Raw fetch.** `curl` with a desktop browser user agent and `Accept-Language: ar,en`, following redirects. The body is kept as served (`raw.html`, `raw.pdf`, …), with the response headers (`headers.txt`) and the transfer facts (`fetch.json`).
2. **Browser render.** Chromium (Playwright) loaded every web page and every source the raw fetch could not get:
   - `text.txt` holds the visible text after scripts ran;
   - `render.json` holds the status, final address and title;
   - where only the browser got the page, its body is kept too (`raw-browser.*` or `rendered.html`).
3. **Retry and archive check.** Addresses containing non-ASCII characters were retried percent-encoded. The Wayback Machine was asked for a copy of each source still missing, but it was rate-limiting during this run, so no archive copies were taken.
4. **Finishing.**
   - PDFs got a `text.txt` from `pdftotext -layout`.
   - One PDF cited under two host names was kept once; the second item has `duplicate-of.txt`.
   - Two sources were not fetched at all: a live payment endpoint, and a site whose certificate is not trusted (TLS checks were not bypassed).

## Results

| Result | Count |
| --- | --- |
| captured | 237 |
| blocked from here | 17 |
| gone (404, 410, parked domain or maintenance page) | 6 |
| skipped | 2 |

By date (automatic hints; see `date_source`):

| age_class | Captured | Not captured |
| --- | --- | --- |
| 2025-2026 | 84 | 2 |
| 2023-2024 | 24 | 1 |
| before-2023 (historical) | 21 | 0 |
| undated (live page on capture date) | 108 | — |
| undated | — | 22 |

## manifest.tsv

One row per source. `manifest.json` holds the same rows.

| Column | Meaning |
| --- | --- |
| `n`, `url` | Item number and the address as cited |
| `result` | captured, blocked from here, gone, skipped |
| `age_class`, `date_hint`, `date_source` | Publication date hint and where it came from: URL, page metadata, `<time>` tag, PDF metadata |
| `primary_file`, `text_file` | The main captured file and its readable text, inside `dir` |
| `sha256`, `bytes` | Fingerprint and size of the main file |
| `http_raw`, `http_browser` | Status from the raw fetch and from the browser |
| `final_url`, `content_type` | Where the address ended up, and the served type |
| `fetched_at`, `dir`, `cited_in` | Fetch time, item folder, and file and line of each citation |
| `note` | Why a source is blocked, gone or skipped, or how it was captured |
