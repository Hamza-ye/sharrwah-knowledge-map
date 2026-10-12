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
- 020 yemeneco.org, published 2026-03-17: read, 130 lines; conditions YQ-B019–YQ-B021, citations YE-B027–YE-B029.
- 016 (yemeneco.org image), 021–023 (saba.ye): not readable; see below.
- 024 althawrah.ye, published 2019-12-24: read, 131 lines; conditions YQ-B022–YQ-B040, citations YE-B030–YE-B049. A history of the banknote split, with the Sana'a side's measures of 2017–2019 and exchange rates from 2016 on.
- 025 yemeneco.org, published 2026-01-07: read, 130 lines; conditions YQ-B041–YQ-B042, citations YE-B050–YE-B052.
- 026 (yemeneco.org image): not readable; see below.
- 027 yemeneco.org, published 2026-01-04: read, 137 lines; condition YQ-B043, citations YE-B053–YE-B054.
- 028 yemeneco.org, published 2026-09-17: read, 98 lines (a one-line news item); condition YQ-B044, citation YE-B055.
- 029 yemeneco.org, published 2025-12-25: read, 136 lines; condition YQ-B045, citations YE-B056–YE-B058.
- 030 (yemeneco.org image): not readable; see below.
- 031 yemeneco.org, published 2026-05-18: read, 98 lines (a one-line news item); condition YQ-B046, citation YE-B059.
- 032 yemen-yba.com (Yemen Banks Association report, dated 2026/02/11 in its byline, raw.html line 468; the manifest classes it as an undated live page): its text.txt (81 lines) holds only menus and the title, so part B read the report in the item's raw.html (lines 459-649) and cites that file; conditions YQ-B047–YQ-B056, citations YE-B060–YE-B074.
- 033 althawrah.ye, published 2018-10-30: read, 119 lines; conditions YQ-B057–YQ-B058, citations YE-B075–YE-B081.
- 034 yemeneco.org, published 2024-11-24: read, 132 lines; condition YQ-B059, citations YE-B082–YE-B083.
- 035 (saba.ye): not readable; see below.
- 036 yemeneco.org, published 2025-04-27: read, 131 lines, including its own related-headlines block (lines 71-91); conditions YQ-B060–YQ-B062, citations YE-B084–YE-B089.
- 037 (saba.ye): not readable; see below.
- 038 yemeneco.org, published 2023-03-21: read, 127 lines, including its related-headlines block (headlines only); condition YQ-B063, citations YE-B090–YE-B091.
- 039 yemen-nic.info, law 17 of 2013 amending the anti-money-laundering law 1 of 2010, issued 12 September 2013 and in force from issue: read, 593 lines; conditions YQ-B064–YQ-B066, citations YE-B092–YE-B099. Definitions, the national committee and unit, confiscation and penalties were read and not recorded, as they aren't conditions of selling or paying.
- 040 moit.gov.ye/legislations, the ministry's live archive of legislation (capture date 2026-10-10): read, 148 lines; condition YQ-B067, citations YE-B100–YE-B101. It lists, as in force (ساري): the investment law 3 of 2025, the Prime Minister's boycott decision 10, the commercial register regulation, the consumer protection law 46 of 2008 and its regulation, the internal trade law 5 of 2007 and its regulation, the foreign trade law 16 of 2007, the trade names law 20 of 2003, the financial leasing law and others. A law's status isn't itself a condition, so only the boycott decision, whose text this run doesn't hold in readable form, is recorded.
- 041 moit.gov.ye PDF, commercial register law (decree-law 33 of 1991, as amended; in force from issue in 1991; the text gives no dates for the amendments): read, 189 lines; conditions YQ-B068–YQ-B073, citations YE-B102–YE-B111. Its text layer is damaged; see Problems.

## Same condition: identifications within the part

- "Which banks institutions and individuals may deal with": YQ-B001 (Sana'a central bank's decision 4 of 1445) and YQ-B002 (the Aden bank's decision to stop dealing with a number of banks), both in item 012.
- "Rate at which rials buy and sell one US dollar": YQ-B005, YQ-B006 (item 012).
- "Which banks and exchange firms exchange companies and money-transfer networks may deal with": YQ-B007, YQ-B009 (item 013).
- "Which identity documents a customer must show to carry out a financial transaction or money transfer": YQ-B013 (item 015), YQ-B015 (item 017).
- "Which printed rial banknotes may be dealt in": YQ-B003 (item 012); YQ-B024–YQ-B027, YQ-B030, YQ-B032–YQ-B035 (item 024).
- "What holders of rial banknotes withdrawn from dealing must do": YQ-B004 (item 012, notes printed before 2016, Aden side) and YQ-B022 (item 024, notes printed by the Aden bank, Sana'a side).
- "Which printed rial banknotes banks and exchange firms may accept": YQ-B028, YQ-B031 (item 024).
- "Rate at which rials buy and sell one US dollar": also YQ-B036–YQ-B040 (item 024). The central bank's ceilings (YQ-B019–YQ-B021, item 020) are kept as separate conditions, since they are limits an authority sets, not reported rates.
- "Whether network and pyramid marketing companies may be dealt with": YQ-B045 (item 029, warning to citizens), YQ-B046 (item 031, warning to citizens and financial establishments).
- "Which electronic money services are available to pay with": YQ-B023 (item 024), YQ-B055 (item 032), YQ-B057 (item 033).
- "Whether Starlink equipment may be sold, held or used": YQ-B060, YQ-B061, YQ-B062 (item 036).

## Place groupings within the part

- Aden bank's area = Aden central bank's area: item 024 calls the same bank بنك عدن (line 42) and البنك المركزي اليمني التابع لحكومة المرتزقة في عدن / المركزي بعدن (lines 57-58, 60).
- Sana'a central bank's area and 'Sana'a and the governorates under the Supreme Political Council and the National Salvation Government': item 024 line 14 says the Sana'a central bank's December 2019 decision is carried out at agents in صنعاء والمحافظات الواقعة تحت سلطة المجلس السياسي الأعلى وحكومة الإنقاذ الوطني. Part B uses that name for the 2017–2019 Sana'a-side decisions item 024 lists (lines 46-53), which line 46 attributes to the National Salvation Government and the central bank. YQ-B031 (line 59) keeps 'Sana'a central bank's area', as that statement names only the bank.
- Yemen: rows a source states of Yemen as a whole have place 'Yemen', with the source's words in the note (first in item 032).

## What couldn't be read

- 001–007, 009, 010 (centralbank.gov.ye): blocked from here, connection reset; no text file.
- 008 (centralbank.gov.ye): HTTP 503; its text.txt holds only the error message (upstream connect error).
- 011, 021, 022, 023, 035, 037, 061 (saba.ye): HTTP 403; each text.txt holds only a Cloudflare security-check page.
- 016, 026, 030 (yemeneco.org): JPEG images with no text_file in the manifest; no readable text to quote.
- Scanned PDFs with no text layer: 042, 046, 051, 069, 070, 071 (text.txt empty), 050 (text.txt holds only the title, قانون الاستثمار 2025م-1446هـ), 068 (page numbers only), 057 (PDF not stored; text.txt empty). The run's README says their OCR text is in evidence/yemen/derived/, which the brief gives to part F; part B didn't read it.

## Problems

- Item 032: the manifest's text_file holds only the page's menus and the report's title; the body is in raw.html, which part B cites instead (the checker reads .html files with tags removed).
- Item 041 (commercial register law): the PDF's text layer is damaged in three ways. Art. 11 (lines 104-110) is clean. Arts. 3-9 (lines 36-96) render some letters wrongly (e.g. ل for و, ط for ب, د for ق) but stay legible; part B quotes them as in the file and gives its reading in the state. Arts. 1-2, 6, 10, 12-15 and 20-28 (lines 1-34, 78-82, 98-103, 113-131, 154-184) are in a fully shifted encoding, and arts. 16-19 (penalties, lines 133-153) drop letters and their digits are unreliable; part B didn't record conditions from these. Among them is art. 12(2) (lines 119-120), which appears to bar bodies dealing with merchants from processing their business without proof of registration; a reader of the PDF itself could confirm it.
