# Pass 1, part C: the operators run

Run: `evidence/yemen/runs/20261010T072550Z-sanaa-operators-search/`, 99 items. Its README says it was fetched from a cloud container outside Yemen on 10 October 2026, so every citation has `fetched_from` = `outside Yemen`. Every `source` uses commit 9d0de523f1852ebf7716f0da01b6b619edc5e8fc. For items whose manifest gives no `text_file` (001, 040, 043: JSON answers), the JSON file itself was read and cited, with the JSON path in `locator`.

## What was read, item by item

Each line: item, file read, what it is, conditions recorded from it.

- 001 ymp.ye, `raw.json`: list of 11 e-wallets with each provider's description (live page). Read in full. Conditions from 9 of the 11 entries; ONE Cash's entry states only aims, and Jaib's states no act.
- 002 pmo-ye.net, `text.txt`: Prime Minister's Office news item dated 2024-06-26 on the page, on the Aden central bank's circular banning dealings with 12 unlicensed e-wallets. Read in full; 2 conditions. The manifest calls it undated; the page shows the date, so that date is used.
- 003 cby-ye.com, `text.txt`: the Aden central bank's announcement dated 2020-02-26 on the page, under a live news list. Read in full; 6 conditions (one from an undated headline in the news list).
- 004 yemenwillasil.com, `text.txt`: blog post shown as 31 May 2024 (URL path 2019/12) on the Sana'a central bank's decisions on the new currency, quoting its statement. Read in full; 5 conditions. Its own summary says the Sana'a bank issued a new banknote replacing the old, while the statement it quotes deems the new notes illegal; both are recorded.
- 005 centralbank.gov.ye: not readable. Blocked from here (connection reset); no page content was captured (`fetch.json`, `headers.txt`, `render.json` only).
- 006 cash.com.ye, `text.txt`: the Cash wallet's page on Cash Pay, its online-payment service for store and app owners (live page). Read in full; 7 conditions.
- 007 cash.com.ye, `text.txt`: the Cash wallet's features for companies and merchants (live page). Read in full; 10 conditions.
- 008 cash.com.ye, `text.txt`: the Cash wallet's terms and conditions (Tamkeen), 20 sections (live page). Read in full; 45 conditions. Clause 4.5 says the balance can be withdrawn at any time; clause 14.1 says at any time within official working hours; both are recorded.
- 009 jawali.com.ye, `text.txt` and `raw.html`: Jawali's FAQ (live page). The text file holds only the questions; the answers sit collapsed in the page's accordion, so `raw.html` was read too and cited for them. 1 condition.
- 010 jawali.com.ye, `text.txt` (and `raw.html` checked): Jawali's merchant QR request page (live page). Its form answered with a database connection error when captured; the page's QR links remain. 1 condition.
- 011 jawali.com.ye, `text.txt`: Jawali service page on transfers through local networks (live page). Read in full; 4 conditions.
- 012 jawali.com.ye, `text.txt`: Jawali service page on purchases and online shopping (live page). Read in full; 2 conditions.
- 013 wecash.com.ye, `text.txt`: WeCash's "about" page (live page). Read in full; 1 condition.
