# Run 20261010T061420Z-sanaa-rules-search

The 83 documents found by the Arabic-first search for Sana'a-side rules on online selling and payments. The search's own list is `evidence/yemen/finding-aids/20261010-sanaa-rules-search.tsv`, rows A001–A083. Each item here cites its row.

The documents come from:

- the Sana'a central bank;
- the Ministry of Economy, Industry and Investment, whose site `moit.gov.ye` now carries law PDFs;
- the Tax Authority;
- Saba and other Sana'a outlets;
- national laws that predate the split.

**Fetched from:** a Claude Code cloud container outside Yemen, on 10 October 2026 (UTC). The method was the same as the cited-sources run: a raw fetch, then a Chromium render, then PDF text extraction and date hints.

## Results

| Result | Count |
| --- | --- |
| captured | 66 |
| blocked from here | 17: ten on `centralbank.gov.ye` (connection reset or 503) and seven on `saba.ye` (403) |

By date hint: 29 from 2025–2026, 11 from 2023–2024, 8 from before 2023 (historical), 18 undated live pages, and 17 undated because they were not captured.

## Notes

- **Scanned PDFs.** Several PDFs from the ministry and the Tax Authority are scans with no text layer. `evidence/yemen/derived/` holds their page images and OCR text.
- **One PDF not stored.** Item 057, the ministry's guide to registering a trade name and issuing a commercial register (amended), is a 93 MB PDF. The original is not stored; `not-stored.txt` gives its address and fingerprint, and its pages are in `derived/`.
- **The blocked pages are the ones only someone inside Yemen can fetch.** They include the Sana'a central bank's list of licensed electronic payment companies, its decisions index and its circulars. `evidence/yemen/to-fetch-from-yemen.md` lists them.
