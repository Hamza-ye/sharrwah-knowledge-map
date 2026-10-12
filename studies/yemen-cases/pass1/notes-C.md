# Pass 1, part C: the operators run

Run: `evidence/yemen/runs/20261010T072550Z-sanaa-operators-search/`, 99 items. Its README says it was fetched from a cloud container outside Yemen on 10 October 2026, so every citation has `fetched_from` = `outside Yemen`. Every `source` uses commit 9d0de523f1852ebf7716f0da01b6b619edc5e8fc. For items whose manifest gives no `text_file` (001, 040, 043: JSON answers), the JSON file itself was read and cited, with the JSON path in `locator`.

## What was read, item by item

Each line: item, file read, what it is, conditions recorded from it.

- 001 ymp.ye, `raw.json`: list of 11 e-wallets with each provider's description (live page). Read in full; 67 conditions, from 9 of the 11 entries; ONE Cash's entry states only aims, and Jaib's states no act.
- 002 pmo-ye.net, `text.txt`: Prime Minister's Office news item dated 2024-06-26 on the page, on the Aden central bank's circular banning dealings with 12 unlicensed e-wallets. Read in full; 2 conditions. The manifest calls it undated; the page shows the date, so that date is used.
- 003 cby-ye.com, `text.txt`: the Aden central bank's announcement dated 2020-02-26 on the page, under a live news list. Read in full; 6 conditions (one from an undated headline in the news list).
- 004 yemenwillasil.com, `text.txt`: blog post shown as 31 May 2024 (URL path 2019/12) on the Sana'a central bank's decisions on the new currency, quoting its statement. Read in full; 5 conditions. Its own summary says the Sana'a bank issued a new banknote replacing the old, while the statement it quotes deems the new notes illegal; both are recorded.
- 005 centralbank.gov.ye: not readable. Blocked from here (connection reset); no page content was captured (`fetch.json`, `headers.txt`, `render.json` only).
- 006 cash.com.ye, `text.txt`: the Cash wallet's page on Cash Pay, its online-payment service for store and app owners (live page). Read in full; 7 conditions.
- 007 cash.com.ye, `text.txt`: the Cash wallet's features for companies and merchants (live page). Read in full; 10 conditions.
- 008 cash.com.ye, `text.txt`: the Cash wallet's terms and conditions (Tamkeen), 20 sections (live page). Read in full; 46 conditions. Clause 4.5 says the balance can be withdrawn at any time; clause 14.1 says at any time within official working hours; both are recorded.
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
- 038 kuraimibank.com, `text.txt`: Kuraimi Bank's page on Hasseb points for merchants (live page). Its tabs are empty in the capture. 1 condition.
- 039 kuraimibank.com, `text.txt`: Kuraimi Bank's page on paying through Hasseb points, with a list of related services. 4 conditions.
- 040 kuraimibank.com, `raw.json`: the bank site's JSON for the M Floos service: Hasseb terms for merchants and customers, and an FAQ. Read in full; 14 conditions, one of them shared with item 039.
- 041 kuraimibank.com, `text.txt`: Kuraimi Bank's M Floos page. 3 conditions.
- 042 kuraimibank.com, `text.txt`: Kuraimi Bank's internal transfers page, with a list of related services. 3 conditions. It gives 4,000 M Floos agents; item 040 gives 12,000; both recorded.
- 043 kuraimibank.com, `raw.json`: the bank site's JSON for its API linking service for online sellers. Read in full; 4 conditions.
- 044 to 048 t.me (Kuraimi Bank channel, posted 2026-08-22, 2026-03-03, 2026-02-22, 2025-11-12, 2026-07-13), `embed-text.txt`: posts on Hasseb. Read in full; 1, 2, 5, 2 and 1 conditions.
- 049 to 053 t.me (M Floos channel, posted 2026-02-01, 2026-08-09, 2026-05-19, 2026-10-08, 2026-10-08), `embed-text.txt`: offers for paying through Hasseb and free transfers. Read in full; 2, 1, 1, 1 and 1 conditions.
- 054 hakikah.net, `text.txt`: fact-check of 22 June 2025 on the Sana'a central bank's circular about Kuraimi Bank. Read in full; 4 conditions.
- 055 yemenat.net, `text.txt`: news item of 22 June 2025 on the same circular, with the site's news list of headlines, several marked with their age at capture (dated by counting back from 10 October 2026, as each `date_basis` says). Read in full; 9 conditions, 7 from headlines.
- 056 barran.press, `text.txt`: news item of 22 June 2025 on the circular, the March 2025 stop of Kuraimi Express by the Sana'a exchangers' association, and eight banks' move of head offices to Aden. Read in full; 3 conditions.
- 057 yemenat.net, `text.txt`: news item of 16 January 2026 on Kuraimi's apps failing, with two accounts of the cause (blocking by the Sana'a authorities, or a technical fault); both recorded. 3 conditions. Its news list repeats item 055's and was not recorded again.
- 058 ainaden.com, `text.txt`: Kuraimi Bank's statement of 13 September 2025 on its app's stoppage. The manifest calls the page undated; it shows that date. 1 condition. The rest of the page is unrelated headlines and advertisements.
- 059 alayyam.info, `text.txt`: Al-Ayyam news item shown as 17 March 2024: transfers from the liberated areas to Houthi-controlled areas stopped except through Kuraimi, the unified transfer network and national switch, exchange rates, and the Sana'a central bank's circular on paying out international transfers. The manifest calls it undated; the page shows the date. Read in full; 6 conditions.
- 060 almashhad.news, `text.txt`: news item of 1 October 2020 on the closure and reopening of Kuraimi's branches in Sana'a. Read in full; 3 conditions.
- 061 kibanks.com, `text.txt`: service points of the bank named in its footer as Kuraimi Islamic Bank (live page). Read in full; 4 conditions.
- 062 play.google.com, `text.txt`: Play listing of the M Floos customer app (Kuraimi). Read in full; 8 conditions. Its reviews report only app faults.
- 063 play.google.com, `text.txt`: Play listing of the M Floos merchant and agent app. Read in full; 8 conditions; its description repeats 062's and is recorded again as a separate source.
- 064 play.google.com, `text.txt`: Play listing of the Kuraimi Jawal bank app. Read in full; 9 conditions, 1 from a review.
- 065 x.com, `text.txt`: Kuraimi Bank's post of 9 September 2025 on requesting a Hasseb point in its app. 1 condition.
- 066 kuraimibank.com, `text.txt`: Kuraimi's page on accounts for projects and businesses. 1 condition.
- 067 kuraimibank.com, `text.txt`: Kuraimi's agency page (Kuraimi Express agencies; 4,000 M Floos agents). 2 conditions.
- 068 kuraimibank.com, `text.txt`: Kuraimi's interactive service-point finder, captured as first loaded with no results. Its filters list point types (branches, ATMs, Kuraimi Express agents inside and outside Yemen), six countries and 21 governorates, but no service point is shown; no condition recorded, since reading the filter options as availability would be inference.
- 069 and 070 t.me (Kuraimi Bank channel, posted 2023-02-18 and 2026-09-30), `embed-text.txt`. 2 and 1 conditions.
- 071 and 072 t.me (M Floos channel, posted 2025-07-31 and 2026-05-24), `embed-text.txt`. 1 condition each.
- 073 alayyam.info, `text.txt`: Al-Ayyam news item shown as 12 February 2025 on the Sana'a authorities' planned unified transfer network. The manifest calls it undated; the page shows the date. Read in full; 4 conditions. Its allegations about named shareholders are not conditions and were not recorded.
- 074 yemeneco.org, `text.txt`: Yemen Eco news item of 24 June 2025 on the exchangers' association's circular. 1 condition. Its ticker is the same as item 037's and was not recorded again.
- 075 x.com, `text.txt`: Yemen Telecom's post of 5 August 2024 on paying its bills through the 16 partners of the e-sadad platform. The page marks the account as suspended. 2 conditions.
- 076 alaraby.co.uk, `text.txt` (and `raw-browser.html` checked): Al-Araby Al-Jadeed report of 11 July 2026 on e-wallets, the liquidity crisis, ATM ceilings, damaged notes, Kuraimi's split systems and exchange rates in Aden and Sana'a. The raw fetch was refused; the browser capture is the page. Read in full; 15 conditions, 2 from headlines of related articles. The browser capture also holds the site's AI-generated summary of the same article, labelled as such, which was not recorded separately.
- 077 almahriah.net, `text.txt` (and `raw.html` checked): Al-Mahriah's report of 11 July 2026 re-reporting the Al-Araby Al-Jadeed article of item 076, with its own wording. Read in full; 11 conditions. The raw page adds only related-news headlines with no figures.
- 078 shahedpress.net, `text.txt` (and `raw.html` checked): Shahed Press article of 21 October 2024 ranking e-wallets by Google Play downloads. Read in full; 2 conditions. The ranked list is one paragraph on the page (lines 51 to 59 of the text file). Its claims about who owns or backs Jawali are not conditions and were not recorded; the raw page adds only other headlines.
- 079 play.google.com, `text.txt` (and `raw.html` checked): Play listing of the OnTime delivery app (Quality Connect), with dated reviews. Read in full; 5 conditions, 2 from users' reviews. Its latest-features list is part of the live listing and takes the capture date, as for the other Play listings; the raw page adds only the developer's contact addresses.
- 080 qc-yemen.com, `text.txt` (and `raw.html` checked): Quality Connect's own page for its On Time delivery service, a live page (page metadata: published 2020-05-27, modified 2025-02-16), so dated by capture. Read in full; 2 conditions. The address block (Sana'a, Hadda Street) is the company's address and was not taken as the place of the service.
- 081 play.google.com, `text.txt` (and `raw.html` checked): Play listing of the Tawseel One delivery app (Tawseel Yemen), with dated reviews and the developer's replies. Read in full; 6 conditions, 1 from a user's review. The review of 13 July 2026 asks for orders from several restaurants in one basket; the latest-features list at capture says the feature was added; both are recorded. The long lists of restaurants and the keyword text are not conditions.
- 082 play.google.com, `text.txt` (and `raw.html` checked): Play listing of the Wagbat food-delivery app, with reviews from 2019 to 2021. Read in full; 5 conditions, 1 from a user's review of 12 December 2019. The listing names two places for the same service, anywhere in Yemen and most areas of Sana'a; both are recorded as written. It names a Rasidi (رصيدي) payment service without saying what it is.
- 083 post.ye, `text.txt` (and `raw-browser.html`, `rendered.html` checked): Yemen Post's own page for its parcel service, a live page dated by capture (the footer's © 2022 is not a date of the content). The raw fetch failed on the site's certificate; the browser capture is the page. Read in full; 6 conditions. The browser files add only menu entries.
- 084 yesmediastore.com, `text.txt` (and `raw.html` checked): home page of the Yes Media store in Sana'a, a merchant's live page (page metadata: published 2022-09-09, modified 2026-08-15), so dated by capture. Read in full; 4 conditions. The footer's list of accepted payment methods is an image without text and could not be read; product prices are not conditions.
- 085 anayees.com, `text.txt` and `raw.html`: the Anayees store's FAQ page, a merchant's live page with no date. The text file holds only the questions; the answers, shown when a question is opened, and the shopping-cart panel's delivery note are in `raw.html` and are cited from it. Read in full; 11 conditions. The answers on product grading, sources and sizes, and the promotion banners, are not conditions.
- 086 procorners.com, `text.txt` (and `raw.html` checked): Procorners' own post on buying from Alibaba through it, shown as 20 December 2022 (page metadata: modified 2024-04-23, kept in the citations' `date_basis`). As a dated post it keeps its shown date, not the capture date. Read in full; 21 conditions, 7 of them from excerpts of the store's other posts shown on the page with their own dates (22 December 2022, 28 February 2023, 10 August 2023, 20 April 2024, 26 October 2024). FAQ answers and list items are cited one by one, as each is its own paragraph on the page. The excerpts' cut-off endings ("...") were not quoted.
- 087 procorners.com, `text.txt` (and `raw.html` checked): Procorners' own post on buying from SHEIN, shown as 23 October 2022 (page metadata: modified 2024-04-23). Read in full; 18 conditions, 4 from excerpts of other posts shown with their own dates (22 December 2022, 23 April 2024, 30 October 2025). Two excerpts repeat ones already recorded from item 086 (the shipping-policy post and the November 2024 sales guide) and were not recorded again. Its heading offers free delivery while its text adds delivery and customs costs to the price; both are recorded.
- 088 procorners.com, `text.txt` (and `raw.html` checked): Procorners' own post on buying from Noon, shown as 9 August 2023 (page metadata: published 2023-08-08 21:04 UTC, modified 2023-08-25). Read in full; 8 conditions, 2 from excerpts of other posts shown with their own dates (13 February 2023, 12 June 2024). Three excerpts repeat ones recorded from item 086 and were not recorded again.
- 089 play.google.com, `text.txt` (and `raw.html` checked): Play listing of the Awsan fashion store app (Bunyan Tech), no reviews shown. Read in full; 6 conditions. Its description names cash on delivery once without a place and once for all customers in the capital Sana'a; both are recorded.
- 090 uptownye.com, `text.txt` (and `raw.html` checked): ordering site of the Uptown restaurant in Sana'a, a merchant's live page with no date. Read in full; 3 conditions. The raw page adds only the cookie notice. Opening hours and the keyword list of districts are not recorded.
- 091 play.google.com, `text.txt` (and `raw.html` checked): Play listing of the CardNet app (SwiftLife) for buying local Wi-Fi internet cards. Read in full; 3 conditions. Its reviews report only app faults and slow responses.
- 092 1mdp.com: not readable. The fetch was reset by the server and the browser capture failed (`fetch.json`, `render.json`); no page was captured.
- 093 perfumgardeen.com, `text.txt` (and `raw.html` checked): About page of the Perfume Garden online store in Sana'a, a merchant's live page (page metadata: published 2025-05-08, modified 2025-12-13), so dated by capture. Read in full; 2 conditions. The raw page adds only brand menus.
- 094 perfumgardeen.com, `text.txt` (and `raw.html` checked): Perfume Garden's returns and refund policy, a merchant's own rule on a live page (page metadata: updated 2026-06-22), so dated by capture. Read in full; 3 conditions. Its footer repeats item 093's cash-on-delivery line, which was not recorded again.
- 095 play.google.com, `text.txt` (and `raw.html` checked): Play listing of the Taiba Hypermarket app (EBDA'A SOFT). Read in full; 3 conditions. Its reviews report only app faults and wishes.
- 096 apps.apple.com, `text.txt` (and `raw.html` checked): App Store listing of the DeliFast delivery app (Lightbulb Tech), latest version shown as 7 June; a live listing, dated by capture. Read in full; 5 conditions. The raw page adds the app's subtitle, which repeats the description, and the store's country menu.
- 097 apps.apple.com, `text.txt` (and `raw.html` checked): App Store listing of the Etlobni delivery app (Murad Al-hathrah), latest version shown as 30 September; a live listing, dated by capture. Read in full; 7 conditions. Its keyword text repeats Tawseel One's listing (item 081) nearly word for word and one sentence even names Tawseel One; that sentence was not recorded. Its reviews, shown without a year, are praise only.
- 098 apps.apple.com, `text.txt` (and `raw.html` checked): App Store listing of the Al Naeem Delivery app for Ibb, latest version shown as 1 May; a live listing, dated by capture. Read in full; 3 conditions. Its dated reviews (2024 and 2025) are praise only.
- 099 emahallat.com: not readable. The fetch failed at the proxy tunnel and the browser capture failed (`fetch.json`, `render.json`); no page was captured.

## Same condition, one wording

Rows that name the same act or availability for the same role share one `condition` wording. The main identifications made in this part:

- **Paying from a phone.** A payment from a mobile e-wallet and one from a bank's mobile app are the same act for the buyer, so the wordings say "by phone (e-wallet or bank app)": for purchases, online purchases, bills and fees, sending money to a person, and the fee to pay. They join each provider's own name for the act, for example Jawali's purchases at stores, Kuraimi's Hasseb (through M Floos or the Kuraimi app), Cash Pay, Mobile Money's merchant payments, SabaCash's and ONE Cash's payments, and the wallets the stores of items 084 to 098 accept.
- **Wallet and bank account.** "Buyer: move money between a mobile e-wallet and a bank account" joins each wallet's link to bank accounts, whatever it is called (wallet-to-bank and bank-to-wallet transfers, linking a bank account, services such as Wasel and We Net in item 078).
- **Wallet and transfer networks.** "Buyer: send and receive transfers between an e-wallet and local money-transfer networks" joins each wallet's named networks.
- **Central bank actions on exchange firms.** "Exchange company or transfer agent: central bank suspends or restores its operation" joins suspensions and restorations by either central bank; row YQ-C075 was reworded into it during this pass.
- **Cash on delivery.** "Buyer: pay cash on delivery for an online order" joins every seller's or app's option to pay in cash on receipt, under whatever name (الدفع عند الاستلام, الدفع نقدًا عند الاستلام, كاش عند الستلام as item 097 spells it, السداد عند الاستلام, or choosing cash as the payment method).
- **Paying by remittance.** "Buyer: pay for an online order by money transfer" joins an exchange-house transfer (item 084) and domestic transfers such as Al-Najm (item 085).
- **Delivery.** "Buyer: order deliveries through a delivery app" joins food and general delivery apps (items 079 to 082, 096 to 098) and the Talqa home-gas app (item 049). A seller's own site or app that delivers (items 090, 095) has its own wording, "Buyer: order online from a seller's own site or app for delivery". "Buyer: delivery fee for an online order" joins a delivery app (081, 097), a store's app (089) and a restaurant's site (090); its row from item 081 was renamed from "Buyer: delivery fee for orders through a delivery app" during this pass. Delivery times within Yemen ("Buyer: delivery time for an online order") are kept apart from those for orders from abroad and for parcels sent by post.
- **Buying from abroad.** "Buyer: buy from foreign online stores through an intermediary in Yemen" joins Procorners' posts for Alibaba, SHEIN, Noon, Amazon, AliExpress, eBay and iHerb (items 086 to 088) and Etlobni's delivery of orders from international sites (item 097).
- **Returns.** "Buyer: return or exchange an online purchase" joins the return rules of stores (085, 089, 094) and of an intermediary (086, 087).

Each wording below is used by more than one row; the rows listed under it are identified as the same condition. Item numbers are those of the cited sources.

- Bank or exchange company: deal with e-wallets and e-payment services that lack a central bank licence: YQ-C068, YQ-C073 (items 002, 003).
- Bank or exchange company: linked to a unified (national) network for money transfers: YQ-C389, YQ-C390, YQ-C435 (items 059, 073).
- Bank: head office in Sana'a or Aden: YQ-C383, YQ-C436 (items 056, 073).
- Bank: run one system across the government-held and Houthi-held areas: YQ-C452, YQ-C465 (items 076, 077).
- Business: pay salaries and bulk disbursements into mobile e-wallets: YQ-C026, YQ-C029, YQ-C038, YQ-C094, YQ-C209, YQ-C256, YQ-C305 (items 001, 007, 020, 023, 027).
- Buyer and merchant: availability of banknotes (cash liquidity): YQ-C443, YQ-C457 (items 076, 077).
- Buyer and merchant: banknotes that may be used for payment: YQ-C070, YQ-C074, YQ-C076, YQ-C077, YQ-C078, YQ-C448, YQ-C451, YQ-C458, YQ-C459 (items 003, 004, 076, 077).
- Buyer and merchant: problems of paying in banknotes: YQ-C177, YQ-C193, YQ-C207, YQ-C266, YQ-C325, YQ-C355, YQ-C450, YQ-C464 (items 015, 018, 020, 023, 039, 046, 076, 077).
- Buyer and merchant: rial exchange rate against the US dollar and Saudi riyal: YQ-C391, YQ-C392, YQ-C453, YQ-C454, YQ-C466, YQ-C467 (items 059, 076, 077).
- Buyer outside Yemen: pay for purchases and bills in Yemen electronically: YQ-C183, YQ-C232, YQ-C264, YQ-C326, YQ-C580 (items 016, 021, 023, 039, 096).
- Buyer: bank account required to use a mobile e-wallet: YQ-C001, YQ-C010, YQ-C013, YQ-C027, YQ-C157, YQ-C206, YQ-C249, YQ-C287 (items 001, 014, 020, 023, 026).
- Buyer: banks whose branches serve customers: YQ-C371, YQ-C373, YQ-C394, YQ-C395, YQ-C397 (items 054, 055, 060, 061).
- Buyer: buy from foreign online stores through an intermediary in Yemen: YQ-C509, YQ-C526, YQ-C527, YQ-C528, YQ-C530, YQ-C547, YQ-C548, YQ-C554, YQ-C555, YQ-C582 (items 086, 087, 088, 097).
- Buyer: cost of buying from a foreign online store through an intermediary: YQ-C514, YQ-C538 (items 086, 087).
- Buyer: currencies an e-wallet account can hold: YQ-C101, YQ-C158, YQ-C172, YQ-C194 (items 008, 014, 015, 018).
- Buyer: daily limit on cash withdrawal from bank ATMs: YQ-C449, YQ-C463 (items 076, 077).
- Buyer: delivery fee for an online order: YQ-C479, YQ-C556, YQ-C564, YQ-C586 (items 081, 089, 090, 097).
- Buyer: delivery time for an online order: YQ-C502, YQ-C503, YQ-C524, YQ-C525, YQ-C544, YQ-C545, YQ-C546, YQ-C559 (items 085, 086, 087, 089).
- Buyer: delivery time for an order from abroad: YQ-C516, YQ-C523, YQ-C535, YQ-C551 (items 086, 087, 088).
- Buyer: delivery within Yemen of an order bought abroad: YQ-C518, YQ-C542, YQ-C553 (items 086, 087, 088).
- Buyer: deposit and withdraw cash to and from a mobile e-wallet through agents or branches: YQ-C016, YQ-C033, YQ-C037, YQ-C049, YQ-C061, YQ-C103, YQ-C127, YQ-C153, YQ-C173, YQ-C178, YQ-C189, YQ-C197, YQ-C205, YQ-C213, YQ-C222, YQ-C255, YQ-C279, YQ-C289, YQ-C336, YQ-C349, YQ-C405, YQ-C412, YQ-C428 (items 001, 008, 014, 015, 017, 018, 019, 020, 021, 023, 024, 026, 040, 042, 062, 063, 067).
- Buyer: discounts for paying by phone instead of cash: YQ-C361, YQ-C362, YQ-C364, YQ-C365, YQ-C366, YQ-C430, YQ-C433, YQ-C434 (items 048, 049, 050, 051, 052, 069, 071, 072).
- Buyer: documents required to open a mobile e-wallet: YQ-C034, YQ-C066, YQ-C226, YQ-C243, YQ-C296, YQ-C334 (items 001, 021, 023, 026, 040).
- Buyer: fare for a ride within the city: YQ-C446, YQ-C447 (items 076).
- Buyer: fee for cash withdrawal from an e-wallet: YQ-C105, YQ-C273 (items 008, 024).
- Buyer: fee on a declined payment by an e-wallet's card: YQ-C300, YQ-C301 (items 026).
- Buyer: fee to fund an e-wallet: YQ-C118, YQ-C274 (items 008, 024).
- Buyer: fee to open a mobile e-wallet: YQ-C174, YQ-C219 (items 015, 021).
- Buyer: fee to pay by phone (e-wallet or bank app): YQ-C120, YQ-C217, YQ-C265, YQ-C283, YQ-C352, YQ-C354 (items 008, 020, 023, 025, 045, 046).
- Buyer: fee to send money transfers from an e-wallet: YQ-C272, YQ-C275, YQ-C340, YQ-C367 (items 024, 040, 053).
- Buyer: have the seller supply a product on request: YQ-C508, YQ-C577 (items 085, 096).
- Buyer: limits on e-wallet balance and transactions: YQ-C108, YQ-C298, YQ-C331 (items 008, 026, 040).
- Buyer: move money between a mobile e-wallet and a bank account: YQ-C018, YQ-C021, YQ-C062, YQ-C116, YQ-C175, YQ-C214, YQ-C225, YQ-C270, YQ-C292, YQ-C319, YQ-C339, YQ-C404, YQ-C411, YQ-C422, YQ-C469 (items 001, 008, 015, 020, 021, 024, 026, 037, 040, 062, 063, 064, 078).
- Buyer: number of e-wallet accounts one customer may hold: YQ-C112, YQ-C231, YQ-C263 (items 008, 021, 023).
- Buyer: open a mobile e-wallet remotely, without visiting an agent: YQ-C067, YQ-C143, YQ-C227, YQ-C245, YQ-C297, YQ-C402 (items 001, 009, 021, 023, 026, 062).
- Buyer: order deliveries by phone call instead of the app: YQ-C480, YQ-C587 (items 081, 097).
- Buyer: order deliveries through a delivery app: YQ-C363, YQ-C470, YQ-C474, YQ-C475, YQ-C476, YQ-C477, YQ-C483, YQ-C484, YQ-C487, YQ-C576, YQ-C581, YQ-C588 (items 049, 079, 080, 081, 082, 096, 097, 098).
- Buyer: order from several stores in one basket through a delivery app: YQ-C481, YQ-C482 (items 081).
- Buyer: order online from a seller's own site or app for delivery: YQ-C562, YQ-C573 (items 090, 095).
- Buyer: pay bills and fees by phone (e-wallet or bank app): YQ-C009, YQ-C017, YQ-C022, YQ-C023, YQ-C032, YQ-C036, YQ-C047, YQ-C052, YQ-C058, YQ-C063, YQ-C148, YQ-C154, YQ-C171, YQ-C187, YQ-C195, YQ-C210, YQ-C224, YQ-C240, YQ-C260, YQ-C278, YQ-C286, YQ-C327, YQ-C346, YQ-C407, YQ-C414, YQ-C419, YQ-C420, YQ-C421, YQ-C425, YQ-C440, YQ-C565 (items 001, 011, 014, 015, 017, 018, 020, 021, 022, 023, 024, 026, 039, 040, 041, 062, 063, 064, 075, 091).
- Buyer: pay by phone using NFC: YQ-C043, YQ-C302, YQ-C351 (items 001, 026, 044).
- Buyer: pay by phone without internet: YQ-C188, YQ-C338, YQ-C356 (items 017, 040, 046).
- Buyer: pay cash on delivery for an online order: YQ-C471, YQ-C478, YQ-C485, YQ-C494, YQ-C499, YQ-C519, YQ-C540, YQ-C557, YQ-C560, YQ-C563, YQ-C569, YQ-C575, YQ-C584, YQ-C589 (items 079, 081, 082, 084, 085, 086, 087, 089, 090, 093, 095, 097, 098).
- Buyer: pay for an online order by money transfer: YQ-C497, YQ-C500 (items 084, 085).
- Buyer: pay for foreign online purchases in Yemeni rials: YQ-C510, YQ-C529, YQ-C532 (items 086, 087).
- Buyer: pay for online purchases by phone (e-wallet or bank app): YQ-C039, YQ-C053, YQ-C082, YQ-C147, YQ-C150, YQ-C156, YQ-C291, YQ-C358, YQ-C431, YQ-C472, YQ-C496, YQ-C498, YQ-C520, YQ-C539, YQ-C552, YQ-C574, YQ-C578, YQ-C583, YQ-C590 (items 001, 006, 011, 012, 014, 026, 046, 069, 079, 084, 085, 086, 087, 088, 095, 096, 097, 098).
- Buyer: pay for purchases by phone (e-wallet or bank app): YQ-C002, YQ-C006, YQ-C011, YQ-C030, YQ-C035, YQ-C045, YQ-C051, YQ-C056, YQ-C059, YQ-C146, YQ-C149, YQ-C160, YQ-C165, YQ-C170, YQ-C186, YQ-C191, YQ-C212, YQ-C223, YQ-C239, YQ-C257, YQ-C277, YQ-C284, YQ-C324, YQ-C330, YQ-C337, YQ-C345, YQ-C353, YQ-C357, YQ-C408, YQ-C415, YQ-C423, YQ-C442, YQ-C460 (items 001, 011, 012, 014, 015, 017, 018, 020, 021, 022, 023, 024, 026, 039, 040, 041, 045, 046, 062, 063, 064, 076, 077).
- Buyer: pay from a mobile e-wallet by SMS: YQ-C004, YQ-C012, YQ-C060, YQ-C180, YQ-C190, YQ-C262, YQ-C294, YQ-C316 (items 001, 015, 017, 023, 026, 030).
- Buyer: pay games and entertainment subscriptions from a mobile e-wallet: YQ-C162, YQ-C199, YQ-C241, YQ-C261 (items 014, 018, 022, 023).
- Buyer: pay part of an order from abroad on arrival: YQ-C521, YQ-C541 (items 086, 087).
- Buyer: receive money transfers from abroad into a mobile e-wallet: YQ-C041, YQ-C054, YQ-C169, YQ-C254 (items 001, 015, 023).
- Buyer: recover an e-wallet payment sent to the wrong account: YQ-C133, YQ-C234 (items 008, 021).
- Buyer: refund if an order from abroad does not arrive: YQ-C515, YQ-C534 (items 086, 087).
- Buyer: register an e-wallet on a phone number registered in someone else's name: YQ-C230, YQ-C247 (items 021, 023).
- Buyer: return or exchange an online purchase: YQ-C504, YQ-C522, YQ-C543, YQ-C558, YQ-C570 (items 085, 086, 087, 089, 094).
- Buyer: send and receive international money transfers through a bank: YQ-C350, YQ-C400, YQ-C432 (items 042, 061, 070).
- Buyer: send and receive transfers between an e-wallet and local money-transfer networks: YQ-C145, YQ-C159, YQ-C168, YQ-C198, YQ-C238, YQ-C253, YQ-C271, YQ-C315, YQ-C321 (items 011, 014, 015, 018, 022, 023, 024, 029, 037).
- Buyer: send money from a mobile e-wallet to a phone number not registered with the wallet: YQ-C020, YQ-C216, YQ-C236, YQ-C252, YQ-C281, YQ-C288, YQ-C335, YQ-C347, YQ-C406, YQ-C413 (items 001, 020, 021, 023, 024, 026, 040, 041, 062, 063).
- Buyer: send money to another person by phone (e-wallet or bank app): YQ-C003, YQ-C008, YQ-C019, YQ-C028, YQ-C046, YQ-C048, YQ-C057, YQ-C155, YQ-C167, YQ-C185, YQ-C192, YQ-C211, YQ-C221, YQ-C237, YQ-C251, YQ-C276, YQ-C285, YQ-C403, YQ-C410, YQ-C418 (items 001, 014, 015, 017, 018, 020, 021, 022, 023, 024, 026, 062, 063, 064).
- Buyer: send money within Yemen through a money-transfer network: YQ-C348, YQ-C417 (items 042, 064).
- Buyer: transact from an e-wallet before the account is activated: YQ-C163, YQ-C228 (items 014, 021).
- Buyer: transfer money from one provider's e-wallet to another provider's e-wallet: YQ-C015, YQ-C117, YQ-C176, YQ-C235, YQ-C269, YQ-C293 (items 001, 008, 015, 021, 024, 026).
- Buyer: use a bank's or e-wallet's mobile app: YQ-C384, YQ-C387 (items 057, 058).
- Buyer: use a mobile e-wallet from a basic (non-smart) phone: YQ-C025, YQ-C064, YQ-C208, YQ-C250 (items 001, 020, 023).
- Buyer: use e-wallet agents and points of sale: YQ-C014, YQ-C044, YQ-C065, YQ-C179, YQ-C218, YQ-C220, YQ-C333 (items 001, 015, 020, 021, 040).
- Buyer: use the apps of banks that moved their head offices to Aden: YQ-C385, YQ-C386 (items 057).
- Buyer: virtual card for paying online, issued by an e-wallet: YQ-C268, YQ-C299 (items 008, 026).
- Buyer: what is needed to activate an e-wallet account: YQ-C164, YQ-C200, YQ-C229, YQ-C246 (items 014, 018, 021, 023).
- Buyer: what is needed to authorize an online e-wallet payment: YQ-C087, YQ-C566 (items 006, 091).
- Buyer: what is needed to buy from a foreign online store through an intermediary: YQ-C511, YQ-C533, YQ-C550 (items 086, 087, 088).
- Buyer: where a mobile e-wallet can be opened: YQ-C401, YQ-C409 (items 062, 063).
- Buyer: who may open a mobile e-wallet: YQ-C109, YQ-C267 (items 008, 023).
- Buyer: withdraw cash from a mobile e-wallet at ATMs: YQ-C024, YQ-C050, YQ-C320 (items 001, 037).
- E-wallet provider: area served: YQ-C151, YQ-C282 (items 013, 025).
- E-wallet provider: authority licensing mobile e-wallet services: YQ-C005, YQ-C069, YQ-C098, YQ-C152, YQ-C248 (items 001, 002, 008, 014, 023).
- E-wallet provider: number of e-wallets in operation: YQ-C444, YQ-C445, YQ-C461, YQ-C462 (items 076, 077).
- E-wallet provider: rules under which a mobile e-money service operates: YQ-C055, YQ-C072, YQ-C099 (items 001, 003, 008).
- Exchange company or transfer agent: central bank suspends or restores its operation: YQ-C075, YQ-C377, YQ-C378 (items 003, 055).
- Exchange company: deal with a bank's money-transfer network: YQ-C370, YQ-C382, YQ-C429 (items 054, 056, 067).
- Exchange company: dealing with it suspended or restored by the exchangers' association: YQ-C379, YQ-C439 (items 055, 074).
- Financial institution or exchange company: banks it may deal with: YQ-C368, YQ-C369, YQ-C372, YQ-C381 (items 054, 055, 056).
- Haulier: road routes open for goods transport: YQ-C374, YQ-C375 (items 055).
- Merchant: accept electronic payment on an online store or app: YQ-C081, YQ-C242, YQ-C341 (items 006, 022, 043).
- Merchant: accept mobile e-wallet payment by QR code: YQ-C042, YQ-C144, YQ-C196, YQ-C215, YQ-C312 (items 001, 010, 018, 020, 027).
- Merchant: limit on receiving e-wallet payments: YQ-C119, YQ-C314 (items 008, 027).
- Merchant: link branches or points of sale to one e-wallet account: YQ-C093, YQ-C311 (items 007, 027).
- Merchant: move money between a business e-wallet, bank accounts and other e-wallets: YQ-C307, YQ-C328 (items 027, 040).
- Merchant: order wholesale quantities from a foreign online store through an intermediary: YQ-C517, YQ-C536 (items 086, 087).
- Merchant: receive buyers' payments for sales electronically: YQ-C007, YQ-C031, YQ-C090, YQ-C202, YQ-C258, YQ-C303, YQ-C323, YQ-C359 (items 001, 007, 019, 023, 027, 038, 047).
- Merchant: refund an e-wallet payment to the buyer: YQ-C086, YQ-C306, YQ-C329 (items 006, 027, 040).
- Merchant: ship online orders to buyers in other governorates: YQ-C495, YQ-C561, YQ-C568 (items 084, 089, 093).
- Merchant: sign up to accept electronic payments remotely: YQ-C203, YQ-C310, YQ-C360, YQ-C426 (items 019, 027, 047, 065).
- Merchant: time for an electronic payment to reach the merchant: YQ-C085, YQ-C343 (items 006, 043).
- Merchant: what is needed to accept electronic payment online: YQ-C083, YQ-C344 (items 006, 043).
- Merchant: what is needed to open a merchant account for electronic payments: YQ-C113, YQ-C244, YQ-C332 (items 008, 023, 040).
- Merchant: withdraw e-wallet balance as cash: YQ-C084, YQ-C095 (items 006, 007).

## Places

Places are written as each source names them, with the source's words in brackets where it gave them; names that differ in their Arabic are kept apart, even where the English reads alike (for example "all regions of Yemen" from جميع مناطق اليمن, كل مناطق اليمن and لكل مناطق اليمن).

Groupings, each made inside one source that uses both names for the same area:
- Item 079: مدينة صنعاء and داخل صنعاء (the OnTime app's service area), written "Sana'a city (مدينة صنعاء)" (YQ-C470).
- Item 085: شارع حدة جولة ريماس and ش. حدة، جولة ريماس (the Anayees store's service point), written "Hadda Street, Raymas roundabout (ش. حدة، جولة ريماس)" (YQ-C501).
- Item 093: جميع المدن اليمنية, جميع المحافظات and لكل اليمن (the Perfume Garden store's delivery area), written "all Yemeni cities (جميع المدن اليمنية)" (YQ-C568).

Places named after an authority, where the source names the authority but not the area (the brief's `<authority>'s area`):
- "Central Bank of Yemen in Aden's area": sources that name the central bank's head office or seat in Aden, or dateline its decision in Aden (items 003, 055, 073).
- "Central Bank of Yemen in Sana'a's area": sources that name the central bank in Sana'a (items 004, 055, 074).
- "Central Bank of Yemen's area": sources that name the Central Bank of Yemen with no seat (items 001, 008, 014, 023). These are not joined to either of the two above.
- "the Central Bank's area (البنك المركزي)": item 059, which names only "the central bank".
- "the Salvation Government's area" (item 004), "the Houthis' area" (item 003) and "the Sana'a authorities' area (سلطات صنعاء)" (item 057), as those sources name the authority.

## Not readable

- 005 centralbank.gov.ye and 033 sabacash.com: connection reset; nothing captured.
- 034 floosak.com: Cloudflare error 522 page only.
- 035 yk-bank.com: Cloudflare block page (HTTP 403) only.
- 092 1mdp.com: connection reset; nothing captured.
- 099 emahallat.com: proxy tunnel failure (502); nothing captured.

Read but with no condition: 028, 032 and 036 state none; 068, the Kuraimi service-point finder, was captured with no results shown.

## Totals

99 items: 93 readable, 6 not readable. Conditions were recorded from 89 items: 590 conditions (YQ-C001 to YQ-C590) and 705 citations (YE-C001 to YE-C705).
