# Pass 1, part D: notes

Part D is the cited-sources run, `evidence/yemen/runs/20261010T050304Z-cited-sources/`, items 1 to 131 by the `n` column of its `manifest.tsv`. The run's README says it was fetched outside Yemen, so every citation has `fetched_from` = `outside Yemen`. Every `source` uses commit 9d0de523f1852ebf7716f0da01b6b619edc5e8fc.

## Status

Complete. All 115 items of the part were read, in order of `n`. The files hold 635 condition rows (YQ-D001 to YQ-D635) and 999 citations (YE-D001 to YE-D999), from 90 items.

## The part

- The manifest has 115 rows with `n` from 1 to 131. The numbers 29, 30 and 94 to 107 have no row in `manifest.tsv` and no folder in `items/`.
- Every citation quotes the item's `text.txt`, the file the manifest names in `text_file`. Where `text.txt` held only a block or error page, `raw.html`, and `raw-browser.html` where there is one, were read too (items 18, 19, 20, 24, 75, 111, 130).
- Items 49 to 53, 55, 56 and 58 are scanned PDFs whose `text.txt` holds no text. Their OCR text in `evidence/yemen/derived/` belongs to part F and was not read here.

## Read, by item

`conditions recorded` counts the rows whose first citation is from the item; `citations` counts the item's citations.

| n | result | text read | conditions recorded | citations |
| --- | --- | --- | --- | --- |
| 1 | captured | text.txt | 1 | 1 |
| 2 | gone (404) | text.txt holds only the 404 page | 0 | 0 |
| 3 | captured | text.txt | 8 | 10 |
| 4 | captured | text.txt | 9 | 11 |
| 5 | captured | text.txt; the page also carries three later, unrelated articles (Gaza, a military operation, blood drives), with no condition | 4 | 3 |
| 6 | captured | text.txt; the page also carries later, unrelated articles (Iran, US, Sudan), with no condition | 8 | 7 |
| 7 | captured | text.txt; later articles on the page (Saudi Arabia, UN, FlyDubai) have no condition | 5 | 6 |
| 8 | captured | text.txt (live page of the bank's own service) | 1 | 1 |
| 9 | captured | text.txt | 10 | 9 |
| 10 | captured | text.txt (post dated 8 September 2025 at line 287, though the manifest calls it undated) | 3 | 6 |
| 11 | captured | text.txt | 6 | 6 |
| 12 | captured | text.txt | 6 | 4 |
| 13 | captured | text.txt | 5 | 4 |
| 14 | captured | text.txt | 1 | 2 |
| 15 | gone (404) | text.txt holds a not-found page of an unrelated site | 0 | 0 |
| 16 | captured | text.txt | 4 | 2 |
| 17 | captured | text.txt | 4 | 5 |
| 18 | blocked from here | text.txt, raw.html and raw-browser.html hold only a Cloudflare check page | 0 | 0 |
| 19 | blocked from here | text.txt, raw.html and raw-browser.html hold only a Cloudflare check page | 0 | 0 |
| 20 | blocked from here | text.txt, raw.html and raw-browser.html hold only a Cloudflare check page | 0 | 0 |
| 21 | captured | text.txt | 5 | 5 |
| 22 | captured | text.txt | 5 | 6 |
| 23 | captured | text.txt | 30 | 24 |
| 24 | blocked from here | text.txt, raw.html and raw-browser.html hold only a Cloudflare check page | 0 | 0 |
| 25 | blocked from here | no text file: the TLS connection failed for both fetches | 0 | 0 |
| 26 | captured | text.txt | 4 | 5 |
| 27 | captured | text.txt | 1 | 1 |
| 28 | gone | text.txt holds only a maintenance notice | 0 | 0 |
| 31 | captured | text.txt (App Store listing; live page) | 3 | 5 |
| 32 | captured | text.txt (App Store listing; live page) | 3 | 4 |
| 33 | captured | text.txt (App Store listing; live page) | 3 | 3 |
| 34 | captured | text.txt (App Store listing; live page) | 7 | 8 |
| 35 | captured | text.txt (App Store listing; live page) | 2 | 2 |
| 36 | captured | text.txt (App Store listing; live page) | 6 | 8 |
| 37 | captured | text.txt (App Store listing; live page) | 6 | 7 |
| 38 | captured | text.txt (App Store listing; live page) | 5 | 3 |
| 39 | captured | text.txt (App Store listing; live page) | 7 | 7 |
| 40 | captured | text.txt (App Store listing; live page) | 6 | 4 |
| 41 | captured | text.txt (the store's own site; live page) | 3 | 5 |
| 42 | captured | text.txt | 3 | 4 |
| 43 | captured | text.txt | 1 | 1 |
| 44 | captured | text.txt; dated by the 'Sep 12, 2025' the page shows (its JSON-LD gives published 2024-01-15, modified 2024-01-20) | 9 | 15 |
| 45 | captured | text.txt; source date 2025-01-16 from its JSON-LD; the table rows carry their own dates; its gold prices are not recorded | 5 | 15 |
| 46 | captured | text.txt; the BTI 2026 country report, dated by the edition year in its title | 44 | 39 |
| 47 | captured | text.txt; about e-commerce platforms in Africa (June 2019), nothing on Yemen | 0 | 0 |
| 48 | captured | text.txt; raw.html read to tell the two rate lines of each block apart (`flags/us.jpg`, `flags/rs.png`); the Central Bank in Aden's own page (live page) | 27 | 56 |
| 49 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 50 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 51 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 52 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 53 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 54 | captured | text.txt; dated by the PDF's creation date (2025-01) | 7 | 25 |
| 55 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 56 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 57 | captured | text.txt; dated by the PDF's creation date (2025-12) | 7 | 30 |
| 58 | captured | text.txt holds only form feeds (a scanned PDF); its OCR text in `derived/` belongs to part F and was not read here | 0 | 0 |
| 59 | captured | text.txt holds only '2026' and the numbers 1 to 232 (a 20-page PDF of images) | 0 | 0 |
| 60 | captured | text.txt (the Central Bank in Aden's own news item); its headline ticker repeats item 48's and was not recorded again | 1 | 3 |
| 61 | captured | text.txt (the Central Bank in Aden's own news item); its headline ticker repeats item 48's and was not recorded again | 1 | 5 |
| 62 | captured | text.txt (the Central Bank in Aden's own news item); its headline ticker repeats item 48's and was not recorded again | 3 | 4 |
| 63 | captured | text.txt (the Central Bank in Aden's own news item); its headline ticker repeats item 48's and was not recorded again | 5 | 6 |
| 64 | captured | text.txt (the Central Bank in Aden's own news item); its headline ticker repeats item 48's and was not recorded again | 1 | 1 |
| 65 | captured | text.txt (the Central Bank in Aden's own page; live page); ticker as on item 48 | 7 | 9 |
| 66 | captured | text.txt: only a list of monthly report titles; ticker as on item 48 | 0 | 0 |
| 67 | captured | text.txt; dated by the date it shows | 2 | 5 |
| 68 | captured | text.txt; same text as item 69 | 1 | 3 |
| 69 | captured | text.txt; same text as item 68 (row YQ-D295 cites both) | 0 (row YQ-D295, first citing item 68, cites it) | 2 |
| 70 | captured | text.txt (the store's own payment page; live page) | 6 | 11 |
| 71 | captured | text.txt | 1 | 2 |
| 72 | captured | text.txt; the page is marked edited 24 April 2025 (line 22); some steps name Syrian pounds and the Sham Cash wallet (lines 142, 152, 158) | 4 | 10 |
| 73 | captured | text.txt (World Bank, Yemen Financial Sector Diagnostics, dated April 5, 2024 at line 42) | 81 | 107 |
| 74 | captured | text.txt; a two-column PDF, quoted line by line; dated by the PDF's creation date (2026-05); analysis as of end-March 2026 (lines 173-175) | 32 | 68 |
| 75 | captured | text.txt shows only a data-loading error ('خطأ في تحميل البيانات'); raw.html has no article text | 0 | 0 |
| 76 | captured | text.txt; policy paper dated December 2025 | 50 | 74 |
| 77 | captured | text.txt; a payment plugin for Sudan, nothing on Yemen | 0 | 0 |
| 78 | captured | text.txt | 4 | 6 |
| 79 | captured | text.txt; dated by the date the page shows, though the manifest calls it undated | 10 | 12 |
| 80 | captured | text.txt; dated by the date the page shows, though the manifest calls it undated | 4 | 9 |
| 81 | captured | text.txt; dated by the date the page shows, though the manifest calls it undated | 1 | 2 |
| 82 | captured | text.txt; dated by the date the page shows, though the manifest calls it undated | 2 | 6 |
| 83 | captured | text.txt; the Central Bank in Aden's own news item, dated by the date it shows | 1 | 2 |
| 84 | captured | text.txt; the Central Bank in Aden's own announcement, dated by the date it shows | 1 | 5 |
| 85 | captured | text.txt | 3 | 2 |
| 86 | captured | text.txt; EU implementing decision, marked 'In force' (live page) | 1 | 5 |
| 87 | captured | text.txt (rates 'last updated: today'); its AED, BHD, EUR, KWD and OMR rates are not recorded | 3 | 5 |
| 88 | captured | text.txt: a currency-converter form with no rates | 0 | 0 |
| 89 | captured | text.txt; Consumer Protection Law No. 46 of 2008; Arabic presentation forms and direction marks quoted as they are in the file | 15 | 41 |
| 90 | captured | text.txt | 9 | 16 |
| 91 | captured | text.txt; bulletin issued 15 March 2026 (line 10) | 8 | 14 |
| 92 | captured | text.txt; a method note with a blank price form; dated by the PDF's creation date (2024-03) | 1 | 1 |
| 93 | captured | text.txt | 4 | 7 |
| 108 | captured | text.txt | 5 | 7 |
| 109 | captured | text.txt (Mellow's own help page, updated July 23, 2024; live page) | 2 | 3 |
| 110 | captured | text.txt; Salla's (Saudi) cash-on-delivery help, nothing on Yemen | 0 | 0 |
| 111 | captured | text.txt holds only a verification page (the browser got 403); raw.html holds Shopify's manual-payments help, nothing on Yemen | 0 | 0 |
| 112 | captured | text.txt (the provider's own page; live page) | 1 | 3 |
| 113 | captured | text.txt; dated by the release's own date (the manifest's 2026-06-23 is a page time tag) | 2 | 8 |
| 114 | captured | text.txt; dated by the release's own date (the manifest's 2026-06-23 is a page time tag) | 2 | 7 |
| 115 | captured | text.txt; dated by the release's own date (the manifest's 2026-06-23 is a page time tag) | 5 | 11 |
| 116 | captured | text.txt; dated by the release's own date (the manifest's 2026-06-23 is a page time tag) | 6 | 14 |
| 117 | captured | text.txt | 10 | 18 |
| 118 | captured | text.txt (the provider's own page; live page) | 7 | 8 |
| 119 | captured | text.txt (the provider's own page; live page) (terms and conditions) | 11 | 16 |
| 120 | captured | text.txt (the provider's own page; live page); rows YQ-D588 to YQ-D594 also cite item 121 | 7 | 6 |
| 121 | captured | text.txt (the provider's own page; live page); English version of item 120 (rows YQ-D588 to YQ-D594 cite both) | 0 (rows YQ-D588 to YQ-D594, first citing item 120, cite it) | 6 |
| 122 | captured | text.txt (the provider's own page; live page); the rates table has city tabs, and the text does not say which tab its figures are for; its AED rate is not recorded | 18 | 41 |
| 123 | captured | text.txt (the provider's own page; live page) | 3 | 9 |
| 124 | captured | text.txt (the provider's own page; live page) | 2 | 5 |
| 125 | captured | text.txt (the provider's own page; live page) | 2 | 9 |
| 126 | captured | text.txt (the provider's own page; live page) | 1 | 3 |
| 127 | captured | text.txt; undated article | 8 | 11 |
| 128 | captured | text.txt; undated directory page (a third party's profile of WeCash) | 5 | 9 |
| 129 | captured | text.txt; undated article | 1 | 1 |
| 130 | blocked from here | text.txt, raw.html and raw-browser.html hold only a Cloudflare check page; no archived copy | 0 | 0 |
| 131 | captured | text.txt (MWM's independent editorial page on the Ki Bank app) | 1 | 2 |

## Conventions used in this part

- `date_basis` in `conditions-D.tsv`: `stated` (the source says when it held); `still holds (source date)`; `range end`; `source date (effective)`, `source date (published)`, `source date (shown)`; `live page (capture date)`; `no date`.
- `held_at` is `no date` when `date_basis` is `no date`, and `before <date>` where the source says only that a state held before a dated one.
- `date_basis` in `citations-D.tsv` says what `source_date` is: `effective`, `published`, `shown`, `capture date (live page)`, or `none` (an undated source, with `source_date` empty).
- A live page is one in which a party describes its own current service or rule; the state it presents as current is dated 2026-10-10, the capture date. Where such a page shows its own date (items 72 and 109), its citations carry that date as `shown`.
- `locator` is the line in the cited file where the quote starts. Quotes from two-column PDFs (items 74 and 91) are taken line by line, one column at a time.
- The place is as the source names it; where the source names only the authority, it is `<authority>'s area`, with the authority named as that source names it (so `Central Bank in Aden's area`, `CBY-Aden's area` and `Aden-CBY's area` come from different sources; see the groupings below).
- Rial prices are recorded for the US dollar and the Saudi riyal. Not recorded: item 87's AED, BHD, EUR, KWD and OMR rates, item 122's AED rate, item 45's gold prices, and the second rate line of each block on item 48, whose flag image is `flags/rs.png` and whose currency the text does not name.
- Item 48's rate blocks give two rate lines each, with no currency in the text; the HTML marks the first line of each block with `flags/us.jpg` and the second with `flags/rs.png` (checked for all 25 blocks). Only the first lines are recorded, as US dollar rates, with that explanation in each row's note.
- Item 48's headline ticker (licence suspensions, the import committee) is recorded once, with no date; items 60 to 66 carry the same ticker, which was not recorded again.
- Items 68 and 69 hold the same text, and one row (YQ-D295) cites both. Items 120 and 121 are the same page in Arabic and English, and rows YQ-D588 to YQ-D594 cite both.

## Identifications within the part

Rows given the same `condition` wording, because they name the same act or availability for the same role:

- `availability of electronic payment means`: YQ-D049, YQ-D516
- `availability of foreign currency`: YQ-D217, YQ-D402, YQ-D464
- `cost of shipping and insuring imports`: YQ-D285, YQ-D419
- `currency in which remittances from abroad are paid out`: YQ-D033, YQ-D034
- `fee for domestic money transfers`: YQ-D478, YQ-D627
- `fee for e-wallet transactions`: YQ-D569, YQ-D583
- `fee for sending money between areas held by different parties`: YQ-D076, YQ-D621, YQ-D622, YQ-D626
- `fee for sending remittances to Yemen`: YQ-D229, YQ-D304
- `how buyers fund an e-wallet`: YQ-D125, YQ-D141, YQ-D153, YQ-D160, YQ-D165, YQ-D562, YQ-D592, YQ-D602, YQ-D632
- `how domestic money transfers can be made`: YQ-D276, YQ-D278, YQ-D357, YQ-D450, YQ-D474, YQ-D486, YQ-D605
- `how e-wallet users withdraw cash`: YQ-D145, YQ-D154, YQ-D161, YQ-D166, YQ-D561, YQ-D580, YQ-D591, YQ-D601, YQ-D631
- `how imports are regulated and financed`: YQ-D235, YQ-D404, YQ-D468, YQ-D526
- `how many ATMs are available`: YQ-D261, YQ-D268, YQ-D372, YQ-D609
- `how many bank payment cards are in issue`: YQ-D264, YQ-D270
- `how many card terminals (POS) merchants have`: YQ-D271, YQ-D371
- `how many money exchangers operate`: YQ-D347, YQ-D348, YQ-D351, YQ-D352, YQ-D427, YQ-D429, YQ-D430, YQ-D431, YQ-D432
- `how merchants receive e-wallet payments`: YQ-D133, YQ-D142, YQ-D152, YQ-D159, YQ-D164, YQ-D576, YQ-D590, YQ-D603, YQ-D614, YQ-D616
- `how merchants set prices`: YQ-D060, YQ-D628
- `how money transfers can be made`: YQ-D028, YQ-D447, YQ-D449, YQ-D476
- `how remittances from abroad can reach Yemen`: YQ-D303, YQ-D343, YQ-D362, YQ-D378, YQ-D441, YQ-D443, YQ-D444, YQ-D529, YQ-D545, YQ-D606
- `how taxes, fees and fines can be paid electronically`: YQ-D111, YQ-D233
- `how the central bank oversees exchange companies`: YQ-D459, YQ-D525
- `how the central bank sells foreign currency`: YQ-D226, YQ-D323, YQ-D332, YQ-D333, YQ-D436
- `how widely e-wallets are used`: YQ-D265, YQ-D272, YQ-D375, YQ-D570
- `levies businesses must pay beyond ordinary taxes`: YQ-D191, YQ-D228, YQ-D555
- `payer's liability for unauthorized electronic debits`: YQ-D007, YQ-D585
- `reliability of internet access`: YQ-D044, YQ-D101, YQ-D179, YQ-D190, YQ-D517
- `rial price of one Saudi riyal`: YQ-D058, YQ-D059, YQ-D062, YQ-D064, YQ-D070, YQ-D071, YQ-D186, YQ-D188, YQ-D481, YQ-D482, YQ-D498, YQ-D596
- `rial price of one US dollar`: YQ-D020, YQ-D040, YQ-D041, YQ-D042, YQ-D056, YQ-D057, YQ-D068, YQ-D069, YQ-D078, YQ-D079, YQ-D185, YQ-D187, YQ-D218, YQ-D219, YQ-D221, YQ-D222, YQ-D223, YQ-D236, YQ-D237, YQ-D238, YQ-D239, YQ-D240, YQ-D241, YQ-D242, YQ-D243, YQ-D244, YQ-D245, YQ-D246, YQ-D247, YQ-D248, YQ-D249, YQ-D250, YQ-D251, YQ-D252, YQ-D253, YQ-D254, YQ-D255, YQ-D256, YQ-D257, YQ-D258, YQ-D259, YQ-D260, YQ-D388, YQ-D389, YQ-D392, YQ-D406, YQ-D407, YQ-D408, YQ-D409, YQ-D410, YQ-D411, YQ-D412, YQ-D413, YQ-D414, YQ-D415, YQ-D416, YQ-D417, YQ-D458, YQ-D479, YQ-D480, YQ-D497, YQ-D524, YQ-D595
- `share of firms with a bank account`: YQ-D367, YQ-D384, YQ-D385
- `share of people with a bank account`: YQ-D043, YQ-D088, YQ-D099, YQ-D213, YQ-D312, YQ-D365
- `what a buyer needs to open an e-wallet`: YQ-D521, YQ-D566, YQ-D586, YQ-D593
- `what a merchant needs to take electronic payments through a bank`: YQ-D294, YQ-D597, YQ-D617
- `what a money exchanger may do under the exchange law`: YQ-D353, YQ-D433
- `what banks must do to keep access to international payments`: YQ-D331, YQ-D457, YQ-D490
- `what collateral lenders require`: YQ-D386, YQ-D611
- `what electronic payment services let users do`: YQ-D092, YQ-D522, YQ-D564, YQ-D573, YQ-D578, YQ-D589, YQ-D633, YQ-D635
- `what exchange companies must do with unclaimed transfers`: YQ-D358, YQ-D487
- `where banks keep their head offices`: YQ-D001, YQ-D035, YQ-D053, YQ-D085, YQ-D207, YQ-D456, YQ-D461, YQ-D471, YQ-D488, YQ-D489, YQ-D492, YQ-D493, YQ-D533, YQ-D552
- `where formal banking services are available`: YQ-D310, YQ-D335, YQ-D398, YQ-D499, YQ-D519, YQ-D608
- `where importers obtain foreign currency`: YQ-D216, YQ-D361, YQ-D439, YQ-D445, YQ-D463, YQ-D465
- `where merchants and households keep their savings`: YQ-D025, YQ-D325
- `whether Yemeni banks have correspondent banking relationships`: YQ-D346, YQ-D396, YQ-D437
- `whether Yemeni banks issue international payment cards`: YQ-D097, YQ-D543, YQ-D598
- `whether a bank account is needed to use an e-wallet`: YQ-D103, YQ-D130, YQ-D520, YQ-D574, YQ-D588, YQ-D630
- `whether an e-wallet can be used without internet access`: YQ-D124, YQ-D149, YQ-D565, YQ-D579
- `whether an instant (fast) payment system is available`: YQ-D175, YQ-D282, YQ-D377
- `whether authorities confiscate merchants' property and bank accounts`: YQ-D193, YQ-D227, YQ-D341, YQ-D473, YQ-D551, YQ-D554
- `whether banks and exchange companies may deal at a rate of their own`: YQ-D065, YQ-D390, YQ-D466, YQ-D467
- `whether banks can use the SWIFT network`: YQ-D345, YQ-D472, YQ-D534, YQ-D550
- `whether banks may deal in interest`: YQ-D208, YQ-D318, YQ-D340
- `whether buyers can open an e-wallet without visiting an office`: YQ-D139, YQ-D567, YQ-D575, YQ-D594
- `whether buyers can pay cash on delivery`: YQ-D121, YQ-D129, YQ-D137, YQ-D176, YQ-D297
- `whether buyers can pay foreign websites`: YQ-D098, YQ-D102, YQ-D132, YQ-D158
- `whether buyers can pay online sellers by transfer through an exchange company`: YQ-D177, YQ-D300
- `whether buyers can pay with a mobile e-wallet`: YQ-D036, YQ-D045, YQ-D051, YQ-D093, YQ-D126, YQ-D135, YQ-D138, YQ-D144, YQ-D151, YQ-D156, YQ-D163, YQ-D178, YQ-D277, YQ-D299, YQ-D342, YQ-D563, YQ-D571, YQ-D600, YQ-D619
- `whether buyers can pay with the electronic rial`: YQ-D209, YQ-D381
- `whether buyers rely on cash`: YQ-D115, YQ-D307, YQ-D393, YQ-D405
- `whether buyers use electronic payment`: YQ-D086, YQ-D087, YQ-D212, YQ-D515
- `whether depositors can draw their bank deposits`: YQ-D024, YQ-D313, YQ-D315, YQ-D329, YQ-D330, YQ-D394, YQ-D442, YQ-D541
- `whether e-wallets can send and receive remittances through exchange networks`: YQ-D131, YQ-D143, YQ-D560, YQ-D572
- `whether e-wallets hold more than one currency`: YQ-D150, YQ-D155, YQ-D167, YQ-D581
- `whether e-wallets issue international payment cards`: YQ-D148, YQ-D157
- `whether electronic funds transfer is an accepted means of payment`: YQ-D002, YQ-D095
- `whether exchange companies may open accounts and take deposits`: YQ-D023, YQ-D324, YQ-D434
- `whether exchange shops are licensed`: YQ-D080, YQ-D211, YQ-D356, YQ-D428, YQ-D469
- `whether financial consumers are protected by rules`: YQ-D289, YQ-D321
- `whether firms can get bank credit`: YQ-D337, YQ-D366, YQ-D395, YQ-D610
- `whether foreign payment platforms move money to and from Yemen`: YQ-D542, YQ-D544, YQ-D634
- `whether goods can be shipped between governorates`: YQ-D047, YQ-D067
- `whether goods may be traded between areas held by different parties`: YQ-D424, YQ-D425
- `whether imports can reach Yemen's ports`: YQ-D399, YQ-D418, YQ-D531
- `whether money can be moved between areas held by different parties`: YQ-D215, YQ-D350
- `whether money can move between different e-wallets`: YQ-D104, YQ-D134, YQ-D140, YQ-D146, YQ-D162, YQ-D281
- `whether one central bank and one currency serve the whole country`: YQ-D192, YQ-D308, YQ-D422, YQ-D527, YQ-D540
- `whether one may deal in virtual assets or cryptocurrencies`: YQ-D286, YQ-D435
- `whether one may deal with unlicensed e-wallets`: YQ-D052, YQ-D081, YQ-D108, YQ-D109, YQ-D275, YQ-D491
- `whether online stores can accept payments online`: YQ-D096, YQ-D123, YQ-D147, YQ-D183, YQ-D293, YQ-D523, YQ-D599, YQ-D613, YQ-D618, YQ-D620
- `whether orders can be delivered to the buyer's door`: YQ-D048, YQ-D122, YQ-D127, YQ-D136, YQ-D181, YQ-D184
- `whether rial banknotes are in short supply`: YQ-D066, YQ-D100, YQ-D283, YQ-D328, YQ-D483
- `whether roads between areas are open to traffic`: YQ-D173, YQ-D232
- `whether the government controls prices of basic goods`: YQ-D061, YQ-D195, YQ-D391, YQ-D513
- `which Yemeni banks are under US sanctions`: YQ-D295, YQ-D460, YQ-D470, YQ-D536, YQ-D548, YQ-D549
- `which Yemeni exchange companies are under US sanctions`: YQ-D359, YQ-D546
- `which Yemeni parties are under US sanctions`: YQ-D535, YQ-D547, YQ-D553, YQ-D557
- `which banknotes merchants accept`: YQ-D021, YQ-D296, YQ-D426
- `which banks one may deal with`: YQ-D055, YQ-D083, YQ-D494, YQ-D495, YQ-D537, YQ-D538, YQ-D539
- `which central bank's rules banks follow`: YQ-D206, YQ-D309, YQ-D320
- `which currencies can be withdrawn at ATMs`: YQ-D262, YQ-D274
- `which exchange companies may operate`: YQ-D234, YQ-D403, YQ-D462, YQ-D484, YQ-D485
- `which goods may not be imported`: YQ-D201, YQ-D400, YQ-D530, YQ-D559
- `which intermediaries firms mainly use`: YQ-D374, YQ-D387
- `which rial banknotes may be used`: YQ-D037, YQ-D054, YQ-D077, YQ-D084, YQ-D172, YQ-D220, YQ-D224, YQ-D314, YQ-D327, YQ-D420, YQ-D421, YQ-D528, YQ-D623, YQ-D624
- `who controls imports into Yemen`: YQ-D203, YQ-D204, YQ-D558
- `who may obtain an exchange company licence`: YQ-D339, YQ-D354, YQ-D355, YQ-D452
- `who may provide electronic payment services`: YQ-D089, YQ-D090, YQ-D116
- `who offers electronic payment services`: YQ-D094, YQ-D379, YQ-D577, YQ-D629
- `who performs banking tasks`: YQ-D210, YQ-D317
- `who provides internet access`: YQ-D230, YQ-D231
- `who provides payment services`: YQ-D316, YQ-D344
- `who takes part in the unified money network (الشبكة الموحدة للأموال)`: YQ-D029, YQ-D120, YQ-D279, YQ-D284, YQ-D451, YQ-D475, YQ-D477

Identifications that joined rows whose sources word the act differently:

- `which banks one may deal with`: the central bank in Aden's suspension of dealings with six banks (YQ-D055, YQ-D083, YQ-D494, YQ-D495) with item 108's bans on dealing with banks on each side and their cancellation (YQ-D537 to YQ-D539).
- `whether one may deal with unlicensed e-wallets`: the central bank in Aden's bans on dealing with twelve named wallets and on unlicensed entities, wallets and payment services (YQ-D052, YQ-D081, YQ-D108, YQ-D109, YQ-D275, YQ-D491).
- `who takes part in the unified money network (الشبكة الموحدة للأموال)`: includes the ban on exchange companies dealing with the unified network in Houthi-controlled areas (YQ-D029) and item 79's report that the Houthi group prevents dealings with it (YQ-D477).
- `how taxes, fees and fines can be paid electronically`: item 23's taxes and fines (YQ-D111) with item 46's government transactions (YQ-D233).
- `fee for sending money between areas held by different parties`: item 21's fee from government-controlled to Houthi-controlled areas (YQ-D076) with item 127's fees in each direction (YQ-D621, YQ-D622, YQ-D626).
- `whether foreign payment platforms move money to and from Yemen`: Mellow's payouts to Yemeni cards (YQ-D542), Wallex's prohibited-countries list (YQ-D544) and PayPal's send-only status for Yemen (YQ-D634).
- `what a merchant needs to take electronic payments through a bank`: Kuraimi Bank's E-Pay API requirements (YQ-D294), its Haseb online link (YQ-D597) and its Haseb payment point (YQ-D617).
- `whether international money transfer companies pay out in Yemen`: Western Union (YQ-D305).
- `whether online stores are approved by the government`: approval by the Ministry of Trade and Industry (YQ-D171).
- `whether the government controls prices of basic goods`: includes item 74's 'price controls' in Houthi-controlled areas, for which the source names no goods (YQ-D391), and item 89's power to set price ceilings (YQ-D513).
- `whether banks and exchange companies may deal at a rate of their own`: includes item 74's 'enforced official rates' (YQ-D390) and item 76's fixed rate and floating rate (YQ-D466, YQ-D467).
- `which goods may not be imported`: includes US restrictions on petroleum imports via Houthi-held facilities (YQ-D400, YQ-D559) and a ban on wheat flour imports whose authority the source does not name (YQ-D530).
- `whether imports can reach Yemen's ports`: damage to Hodeidah port (YQ-D399), shipments blocked short of IRG-controlled ports (YQ-D418) and the fall at Ras Issa (YQ-D531).
- `whether depositors can draw their bank deposits`: includes item 76's increased cash withdrawals by the business community (YQ-D442) and Yemenia's funds frozen in Sanaa banks (YQ-D541).
- `where banks keep their head offices` and `where financial institutions are based` are kept apart: item 74 speaks of financial institutions relocating (YQ-D397), not of head offices.

## Place groupings within the part

Place names used in the rows that a single source uses for the same area:

- `Central Bank in Aden's area` and `CBY-Aden's area`: item 73, lines 518-519 ('the Central Bank of Yemen in Aden (CBY-Aden)'); item 74 also writes 'Central Bank of Yemen (CBY) in Aden' (lines 186-187) and 'CBY-Aden' (lines 200, 877).
- `Aden-CBY's area` and `Central Bank in Aden's area`: item 76, which writes 'Aden-CBY' (line 547), 'CBY in Aden' (lines 159, 245) and 'the Central Bank of Yemen (CBY) in Aden' (lines 910-911) for the same bank.
- `CBY-Sana'a's area` and `Central Bank in Sana'a's area`: item 73, lines 519-520 ('the Central Bank of Yemen in Sana'a (CBY-Sana'a), under the Houthi's control'); item 76 writes 'the Central Bank in Sana'a, under Houthis control' (line 545) and 'The Sana'a-CBY' (line 547).
- `Houthis' area`, `Houthi-controlled area`, `DFA-controlled territory` and `DFA's area`: item 73, line 796 ('the Houthis, or De-Facto Authority') and line 472 ('DFA Yemen De facto Authority').
- `Ansar Allah's area`, `areas under Ansar Allah's control`, `Ansar Allah-controlled territories`, `Ansar Allah-controlled areas` and `Ansar Allah-controlled regions`: item 46, for the same party (line 112: 'Ansar Allah (Partisans of God, led by the Houthi family)').
- `Houthis' area` and `Ansar Allah's area`: item 42 calls the party 'الحوثيين' (line 37) and the envoy's briefing 'أنصار الله' (line 67); item 84 writes 'Ansar Allah (Houthis)' (line 25); item 86 lists 'THE HOUTHIS' with the aliases 'ANSARALLAH' and 'ANSAR ALLAH' (line 373); item 114 writes 'Ansarallah, commonly known as the Houthis' (line 29).
- `Houthi group's area`: item 76 also calls the same party 'the Houthi authorities' (line 604) and 'the Houthi group' (lines 244, 867).
- `IRG-controlled territory` and `IRG's area`: item 46 (lines 112, 596). `IRG areas` and `IRG area`: item 73 (lines 6481, 8091).
- `SBA controlled areas` and `Sana'a-Based Authority (SBA) areas`: item 91 (lines 23, 95, 159).
- `areas under 'occupation' control` and `areas under the control of the 'occupation' and the 'mercenary government'`: item 127 (lines 23 and 29); its `areas of 'national control'` are also called 'مناطق سيطرة الجيش واللجان' (line 24).

## Disagreements recorded as given

- The U.S. designation of the Houthis as a Foreign Terrorist Organization: 'effective on March 3, 2025' (item 82, YQ-D490), 'March 4, 2025' (items 81, 93, 115; YQ-D488, YQ-D535, YQ-D553) and 'March 5, 2025' (item 116, YQ-D557).
- Exchange companies in Aden in 2023: 96 (item 73, YQ-D347; item 76, YQ-D429) and 91 (item 73, YQ-D352; item 76, YQ-D432). In Sana'a: over 170 (YQ-D348, YQ-D430) and 415 (YQ-D351, YQ-D431).
- The unified network's start: item 79 says it was established 'in February' (line 29) and 'in February of the previous year' (line 76); item 76 says it was activated in February 2024 (YQ-D450).

## Read with no condition

- 47: about e-commerce platforms in Africa (June 2019); nothing on Yemen.
- 66: the Central Bank in Aden's list of monthly report titles.
- 77: a WooCommerce payment plugin for Sudan.
- 88: a currency-converter form with no rates in the text.
- 110: Salla's (Saudi) cash-on-delivery help article; nothing on Yemen.
- 111: `raw.html` holds Shopify's manual-payments help page; nothing on Yemen.

## Could not be read

- 2: the address returns a 404 page (text.txt); no archived copy (the archive fetch was reset).
- 15: a not-found page of what is now an unrelated site; no archived copy.
- 18, 19, 20, 24, 130: text.txt, raw.html and raw-browser.html hold only a Cloudflare check page; no archived copy.
- 25: no text file: the TLS connection failed for both fetches; no archived copy.
- 28: text.txt holds only a maintenance notice.
- 49, 50, 51, 52, 53, 55, 56, 58: text.txt holds only form feeds (scanned PDFs); their OCR text is part F's.
- 59: text.txt holds only '2026' and the numbers 1 to 232.
- 75: the page's content did not load: text.txt shows 'خطأ في تحميل البيانات' and 'تعذر تحميل بيانات الخبر'.
- 111: text.txt holds only a verification page (the browser fetch got 403); `raw.html` was read instead (see above).

## Source dates that differ from the manifest

- Items 10, 79, 80, 81, 82, 83 and 84 show a date on the page, though the manifest calls them undated; that date is their source date (item 10's as `published`, the others' as `shown`).
- Items 113 to 116: the manifest's 2026-06-23 is a page time tag; each release's own date is used (December 28, 2023; January 17, 2025; April 17, 2025; September 11, 2025).
- Item 44: the page shows 'Sep 12, 2025', used as its published date; its JSON-LD gives published 2024-01-15 and modified 2024-01-20.
- Item 73: its text dates it April 5, 2024 (line 42); the manifest gives the PDF's creation date, 2024 Oct.
- Item 76: the cover's 'December 2025'. Item 91: 'Issued on 15th March 2026' (line 10). Item 89: the law's year, 2008, in its title (line 1); the manifest's 2023 Oct is the FAOLEX PDF's creation date.
- Items 54, 57, 74 and 92 are dated by the PDF creation date the manifest gives (2025-01, 2025-12, 2026-05, 2024-03).
- Items 127, 128 and 129 show no date for the text cited; their states have `no date`.
