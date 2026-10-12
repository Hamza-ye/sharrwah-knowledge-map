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
- 014 play.google.com, `text.txt`: Play listing of the Jawali app (live description, plus dated user reviews). Read in full; 15 conditions, 4 of them from two users' reviews.
- 015 play.google.com, `text.txt`: Play listing of the Cash app (Tamkeen). Read in full; 16 conditions, 1 from a 2023 review. It says cash is available around the clock; the same wallet's terms (item 008) say within official working hours; both are recorded.
- 016 play.google.com, `text.txt`: Play listing of Cash Mughtarib, the Cash wallet for customers outside Yemen. Read in full; 2 conditions. Its reviews report only app faults.
- 017 play.google.com, `text.txt`: Play listing of the SabaCash app. Read in full; 6 conditions. Its reviews are praise only.
- 018 play.google.com, `text.txt`: Play listing of the Jaib app (AHD Financial). Read in full; 11 conditions, 2 from users' reviews.
- 019 onecashye.com, `text.txt`: ONE Cash's join page for payment points and agents (page metadata: published 2020-08-31, modified 2023-03-23). Read in full; 4 conditions.
- 020 onecashye.com, `text.txt`: ONE Cash's home page (published 2020-08-31, modified 2025-06-04). Read in full; 13 conditions.
- 021 onecashye.com, `text.txt` and `raw.html`: ONE Cash's FAQ (published 2020-06-03, modified 2024-04-16). The text file holds only the customer questions; the answers sit collapsed in the page, so `raw.html` was read too and cited for them. 18 conditions.
- 022 qc-yemen.com, `text.txt`: Quality Connect's page on the Floosak wallet (published 2020-05-27, modified 2025-02-16). Read in full; 6 conditions.
- 023 qc-yemen.com, `text.txt` and `raw.html`: the Floosak FAQ on Quality Connect's site (published 2020-05-27, modified 2025-02-07). The text file holds only the questions; the answers were read in `raw.html` and cited from it. 25 conditions.
- Dating of items 019 to 023: these are the providers' own pages describing their current services, still served when captured, so the live-page rule gives them the capture date. Their metadata dates (published 2020, modified 2023 to 2025) are kept in each citation's `date_basis`. News items, announcements, posts and reviews keep their own dates.
- Check for hidden text: each item's `raw.html` was compared with its text file for visible text missing from the text file. Where it held statements (accordion answers in 009, 021 and 023; a menu label in 008), `raw.html` is cited. Other differences were menus, titles and footers.
- 024 yemen-wallet.ye, `text.txt` and `raw.html`: Yemen Wallet's home page (live page; metadata published 2026-04-28), with dated news snippets. Its services list is only in `raw.html` and is cited from it. 13 conditions, 1 from a news snippet dated 28 April 2026.
- 025 yemen-wallet.ye, `text.txt` and `raw.html`: Yemen Wallet's "about us" (live page; metadata modified 2026-04-16). 2 conditions. It says the wallet is provided by the General Authority for Post and Postal Savings; providers' identities are kept in notes, not recorded as conditions, here and elsewhere.
- 026 play.google.com, `text.txt`: Play listing of the Mobile Money app (CAC Bank), with reviews and the provider's replies. Read in full; 19 conditions, 3 from a review and the provider's reply to it.
- 027 play.google.com, `text.txt`: Play listing of the Mobile Money Business app (CAC Bank) for companies and merchants. Read in full; 12 conditions, 2 from a business user's review.
- 028 t.me (ONE Cash, posted 2026-10-04), `embed-text.txt`: invitation to the Yemen Health 2026 exhibition in Sana'a. Read; no condition stated.
- 029 t.me (ONE Cash, 2026-10-03), `embed-text.txt`: local transfers in three currencies. 1 condition.
- 030 t.me (ONE Cash, 2026-09-23), `embed-text.txt`: use by SMS without internet. 1 condition.
- 031 t.me (SabaCash, 2026-08-23), `embed-text.txt`: cashback for buyers and commission for merchants from 24 August 2026. 2 conditions.
- 032 t.me (SabaCash, 2026-09-22), `embed-text.txt`: partnership slogan with CAC Islamic bank. Read; no condition stated.
- Telegram items: `text.txt` holds only the page's buttons; the post text is in `embed-text.txt`, which is the manifest's `text_file` and was read for every post.
- 033 sabacash.com: not readable. Blocked from here (connection reset); no page content was captured.
- 034 floosak.com: not readable. `text.txt` is Cloudflare's error 522 page (the origin server timed out); no content of the site.
- 035 yk-bank.com (its Floosak page): not readable. `text.txt` is Cloudflare's block page (HTTP 403); no content of the site.
- 036 ahdfinancial.com, `text.txt`: AHD Financial Services' site (live page): founded 2022, Jaib wallet launched March 2023, aims. Read in full; no condition stated.
- 037 yemeneco.org, `text.txt`: Yemen Eco news item of 24 November 2024 on the launch in Sana'a of the MB wallet, under a live ticker of headlines. Read in full; 4 conditions, 1 from an undated ticker headline (road levies in Lahj). The other headlines are about other countries, or name gold and exchange-rate reports without their figures.
