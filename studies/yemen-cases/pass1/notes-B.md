# Pass 1, part B: the Sana'a rules run

Run: `evidence/yemen/runs/20261010T061420Z-sanaa-rules-search/`, 83 items. Its `README.md` says it was fetched from a container outside Yemen on 10 October 2026, so every citation has `fetched_from` = `outside Yemen`. Each citation cites the item's `text.txt` (the manifest's `text_file`) at commit 9d0de523f1852ebf7716f0da01b6b619edc5e8fc, with the item's address from the manifest as `url`. Locators are line numbers in that `text.txt`.

Date conventions in `conditions-B.tsv`, column `date_basis`: `source says it held` (the source gives when the state held), `source date: effective`, `source date: published`, `source date: shown`, `live page: capture date` (a party describing its own current service or rule, captured 2026-10-10), `no date`. In `citations-B.tsv`, `date_basis` names what `source_date` is: `published` (from the page's own date), `effective`, `shown`, `capture date`, or `none`.

## What was read

One line per item, in the run's order: the item, its date, and the rows it gave.

- 001–010 (centralbank.gov.ye): not readable; see below.
- 011 (saba.ye): not readable; see below.
- 012 althawrah.ye, published 2024-06-01: read, 99 lines; conditions YQ-B001–YQ-B006, citations YE-B001–YE-B005.
- 013 yemeneco.org, published 2025-06-22: read, 136 lines; conditions YQ-B007–YQ-B010, citations YE-B006–YE-B012. Lines 1-41 are the site's news ticker, identical on all 23 yemeneco.org pages in the run (checked by hash); its one Yemen commerce statement (line 16, Lahj transport levies) is recorded once, here (YQ-B010).
- 014 whjnews.com, published 2025-06-22: read, 55 lines; conditions YQ-B011–YQ-B012, citations YE-B013–YE-B016. It reports the same Kuraimi decision as 013 with a different issuer, start date and period; both are recorded as given.
- 015 yemeneco.org, published 2025-11-13: read, 141 lines; conditions YQ-B013–YQ-B014, citations YE-B017–YE-B020.
- 017 yemeneco.org, published 2025-12-08: read, 127 lines; condition YQ-B015, citation YE-B021.
- 018 yemeneco.org, published 2026-03-14: read, 129 lines; condition YQ-B016, citations YE-B022–YE-B023.
- 019 yemeneco.org, published 2026-01-21: read, 138 lines; conditions YQ-B017–YQ-B018, citations YE-B024–YE-B026.

## Same condition: identifications within the part

- "Which banks institutions and individuals may deal with": YQ-B001 (Sana'a central bank's decision 4 of 1445) and YQ-B002 (the Aden bank's decision to stop dealing with a number of banks), both in item 012.
- "Rate at which rials buy and sell one US dollar": YQ-B005, YQ-B006 (item 012).
- "Which banks and exchange firms exchange companies and money-transfer networks may deal with": YQ-B007, YQ-B009 (item 013).
- "Which identity documents a customer must show to carry out a financial transaction or money transfer": YQ-B013 (item 015), YQ-B015 (item 017).

## Place groupings within the part

## What couldn't be read

- 001–007, 009, 010 (centralbank.gov.ye): blocked from here, connection reset; no text file.
- 008 (centralbank.gov.ye): HTTP 503; its text.txt holds only the error message (upstream connect error).
- 011, 021, 022, 023, 035, 037, 061 (saba.ye): HTTP 403; each text.txt holds only a Cloudflare security-check page.
- 016, 026, 030 (yemeneco.org): JPEG images with no text_file in the manifest; no readable text to quote.
- Scanned PDFs with no text layer: 042, 046, 051, 069, 070, 071 (text.txt empty), 050 (text.txt holds only the title, قانون الاستثمار 2025م-1446هـ), 068 (page numbers only), 057 (PDF not stored; text.txt empty). The run's README says their OCR text is in evidence/yemen/derived/, which the brief gives to part F; part B didn't read it.

## Problems
