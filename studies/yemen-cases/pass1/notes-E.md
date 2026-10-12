# Pass 1, part E: notes

**Part E** is the cited-sources run, `evidence/yemen/runs/20261010T050304Z-cited-sources/`, items whose `n` in its `manifest.tsv` is 132 to 262. Its `README.md` says it was fetched from a container outside Yemen on 10 October 2026, so every citation here has `fetched_from` = `outside Yemen`. Each item was read from the file named in its `text_file` column.

**Commit** in every `source`: `9d0de523f1852ebf7716f0da01b6b619edc5e8fc`.

**Resumed work.** An earlier agent wrote YQ-E001 to YQ-E009 and YE-E001 to YE-E014 (items 133 to 137) and was interrupted before writing these notes. Those rows were kept as written; the rows from item 138 on, and these notes, were written after the restart.

**Numbering of the manifest.** The `n` column has no rows 29, 30, 94 to 107, 186 or 244, and runs to 280. So part E holds 129 rows (`n` 132 to 262, without 186 and 244), and items 263 to 280 are in neither part D (1 to 131) nor part E. They were not read here.

## Identifications within the part

Rows given the same `condition` wording because they name the same act or availability for the same role:

- Mobile-wallet services available to buyers: YQ-E006, YQ-E010.
- Identity verification of mobile-wallet users: YQ-E016, YQ-E017.

## Place groupings within the part

Two place names counted as one place because a single source uses both for the same area:

## Not readable

## Reading log

One line per item: `n`, folder, what was read, and the rows it gave.

- 132 `132-newdc.qtb-bank.com`: not readable. The run did not fetch it (manifest: "live payment endpoint, not a public page; not fetched"); the folder has no text file. 0 conditions.
- 133 `133-newhedge.io`: read (`text.txt`). Conditions YQ-E001 to YQ-E003; citations YE-E001 to YE-E004.
- 134 `134-obj.ca`: read (`text.txt`). Conditions YQ-E004 to YQ-E006; citations YE-E005 to YE-E008.
- 135 `135-ofac.treasury.gov` (recent actions, 5 March 2025): read (`text.txt`). Conditions YQ-E007, YQ-E008; citations YE-E009 to YE-E011.
- 136 `136-ofac.treasury.gov` (Counter Terrorism Sanctions programme page): read (`text.txt`). It lists advisories and recent actions and states nothing about selling or paying in Yemen. 0 conditions.
- 137 `137-packagist.org`: read (`text.txt`). Condition YQ-E009; citations YE-E012 to YE-E014.
- 138 `138-play.google.com` (Floosak wallet, Play Store page, Arabic): read (`text.txt`). The developer's description is a live page (capture date); reviews and replies carry their own dates. Conditions YQ-E010 to YQ-E017; citations YE-E015 to YE-E025.
- 139 `139-play.google.com` (Floosak wallet, Play Store page, English): read (`text.txt`). Live page; reviews carry their own dates. Conditions YQ-E018 to YQ-E024; citations YE-E026 to YE-E033.
- 140 `140-play.google.com` (Etlobni delivery app, Sana'a): read (`text.txt`). Live page; reviews carry their own dates. Conditions YQ-E025 to YQ-E030; citations YE-E034 to YE-E042.
- 141 `141-play.google.com` (jeeey shopping app): read (`text.txt`). Live page. Conditions YQ-E031 to YQ-E033; citations YE-E043 to YE-E045.
- 142 `142-play.google.com` (ONE Cash agent and merchant app): read (`text.txt`). Live page. Conditions YQ-E034 to YQ-E039; citations YE-E046 to YE-E055.
- 143 `143-play.google.com` (ONE Cash customer app, Arabic): read (`text.txt`). Live page; reviews carry their own dates. Conditions YQ-E040 to YQ-E057; citations YE-E056 to YE-E075.
- 144 `144-play.google.com` (ONE Cash customer app, English): read (`text.txt`). Live page. Conditions YQ-E058 to YQ-E073; citations YE-E076 to YE-E094.
- 145 `145-press.un.org`: not readable. The run's result is "blocked from here" (HTTP 406; the browser failed too); the folder has no text file. 0 conditions.
- 146 `146-radar2.net` (exchange rates in Aden and Sana'a, 26 December 2025): read (`text.txt`). It gives no figures. Conditions YQ-E074, YQ-E075; citations YE-E095, YE-E096.
- 147 `147-rbi.org.in` (Reserve Bank of India, Master Directions on Prepaid Payment Instruments): read (`text.txt`, headings and a search). It sets rules for India and does not mention Yemen. 0 conditions.
- 148 `148-remittanceprices.worldbank.org`: not readable. The run's result is "blocked from here" (HTTP 403); `text.txt` holds only Cloudflare's bot-check page. 0 conditions.
- 149 `149-root.packagist.org` (PHP package for Kuraimi Bank's E-Pay API): read (`text.txt`). Conditions YQ-E076 to YQ-E078; citations YE-E097 to YE-E101.
- 150 `150-s205.q4cdn.com` (Jumia's fourth-quarter 2025 results, PDF text): read (`text.txt`, opening and a search). It reports on Jumia's African markets and does not mention Yemen. 0 conditions.
- 151 `151-sahafah24.net` (exchange rates in Sana'a and Aden, 4 October 2026): read (`text.txt`). Conditions YQ-E079, YQ-E080; citations YE-E102 to YE-E104.
- 152 `152-sahafahonline.net` (women's e-commerce, Shein resellers): read (`text.txt`). The page shows only "منذ سنة"; its `raw.html` gives `date_added` 2025-05-14, used as the published date. Conditions YQ-E081 to YQ-E089; citations YE-E105 to YE-E124.
- 153 `153-sanaacenter.org` (Sana'a Center, "Fostering Opportunities for E-Commerce Growth in Yemen", 15 September 2025, PDF text): read in full (`text.txt`). Conditions YQ-E090 to YQ-E147; citations YE-E125 to YE-E191. Where `pdftotext -layout` broke a word across lines (e.g. "bank-" / "led"), the quote was split at the break.
- 154 `154-sanaacenter.org` (Sana'a Center, "Challenges and Prospects for Electronic Money and Payment Systems in Yemen", March 2022, PDF text): read in full (`text.txt`). Conditions YQ-E148 to YQ-E248; citations YE-E192 to YE-E306. The source gives two figures for account holders in 2019 (3 million, YQ-E155; almost 2.9 million at the end of 2019, YQ-E208), and says both that CAC Bank was permitted to collect customs revenue in e-rials in early 2021 (YQ-E196) and that public revenues are accepted only in cash in Houthi-held areas (YQ-E241); each is recorded.
- 155 `155-sanaacenter.org` (Sana'a Center, "Supporting Trade Finance in Yemen Amid Uncertainty", 17 February 2026, PDF text): read in full (`text.txt`). Conditions YQ-E249 to YQ-E301; citations YE-E307 to YE-E374. It dates the Houthi ban on new notes "starting in 2020" (YQ-E287), where item 154 gives 18 December 2019 for the extended ban (YQ-E184); both are recorded.
- 156 `156-sanaacenter.org` (Sana'a Center Economic Bulletin, 27 November 2020): read in full (`text.txt`). Conditions YQ-E302 to YQ-E313; citations YE-E375 to YE-E388.
- 157 `157-sanaacenter.org` (Sana'a Center, "Currency War Threatens to Deepen Yemen's Monetary Rift", 18 July 2025): read in full (`text.txt`). Conditions YQ-E314 to YQ-E321; citations YE-E389 to YE-E396.
- 158 `158-sanaacenter.org` (Sana'a Center Economic Bulletin, 9 September 2020): read in full (`text.txt`). Conditions YQ-E322 to YQ-E330; citations YE-E397 to YE-E404.
- 159 `159-sanaacenter.org` (The Yemen Review, April-June 2025, the economy section, 22 July 2025): read in full (`text.txt`). Conditions YQ-E331 to YQ-E360; citations YE-E405 to YE-E441.
- 160 `160-sanaacenter.org` (The Yemen Review, April-June 2026, the economy section, 31 July 2026): read in full (`text.txt`). Conditions YQ-E361 to YQ-E391; citations YE-E442 to YE-E482.
- 161 `161-sanaacenter.org` (The Yemen Review, January-March 2026, the economy section, 24 April 2026): read in full (`text.txt`). Conditions YQ-E392 to YQ-E410; citations YE-E483 to YE-E505.
- 162 `162-sanaacenter.org` (The Yemen Review, July-September 2025, the economy section, 28 October 2025): read in full (`text.txt`). Conditions YQ-E411 to YQ-E439; citations YE-E506 to YE-E539. It dates the Houthi ban on American (and Israeli) products to 25 April 2025, where item 159 gives 23 April; both are recorded.
- 163 `163-sanaacenter.org` (The Yemen Review, July-September 2024, the economy section, 16 October 2024): read in full (`text.txt`). Conditions YQ-E440 to YQ-E469; citations YE-E540 to YE-E579.
- 164 `164-sanaacenter.org` (The Yemen Review, October-December 2025, the economy section, 2 February 2026): read in full (`text.txt`). Conditions YQ-E470 to YQ-E508; citations YE-E580 to YE-E630. It gives the customs exchange rate as YR700 before liberalization (YQ-E485), where item 159 gives YR750 (YQ-E347); both are recorded.
- 165 `165-sanctionsnews.bakermckenzie.com` (Baker McKenzie, "US Redesignates Ansarallah as a Foreign Terrorist Organization", 12 March 2025): read in full (`text.txt`). Conditions YQ-E509 to YQ-E516; citations YE-E631 to YE-E645.
- 166 `166-scb.gov.bs` (Securities Commission of The Bahamas notice of 25 June 2026, enclosing the FATF statement of 19 June 2026, PDF text): read (`text.txt`: the notice, the general FATF text and the Yemen entry; the other countries' entries were passed over). Conditions YQ-E517, YQ-E518; citations YE-E646 to YE-E650.
- 167 `167-shiprocket.in` (Shiprocket "Early COD" blog post, 2019): read (`text.txt`). It concerns cash-on-delivery remittance plans in India and does not mention Yemen. 0 conditions.
- 168 `168-shopify.dev` (Shopify developer docs, building an alternative payment extension): read (`text.txt`, skimmed, with searches for Yemen and for country, region and sanction terms). Platform-wide rules; no statement about Yemen. 0 conditions.
- 169 `169-shopify.dev` (Shopify developer docs, payments app requirements): read (`text.txt`, skimmed, with the same searches). Platform-wide rules; no statement about Yemen. 0 conditions.
- 170 `170-south24.net` (South24, CBY-Aden directives on the exchange market, 25 February 2025): read in full (`text.txt`). Conditions YQ-E519 to YQ-E525; citations YE-E651 to YE-E658. It dates the UNMoney mandate to February 2024 (YQ-E524), where item 163 dates the closure of other local networks to June 2024 (YQ-E441); both are recorded.
- 171 `171-south24.net` (South24, eight banks to relocate to Aden, 18 March 2025): read in full (`text.txt`). Conditions YQ-E526 to YQ-E531; citations YE-E659 to YE-E666. It places the CBY-Aden's measures against six Sana'a banks in June 2024 (SWIFT suspension, YQ-E529), where item 163 gives the licence revocation as 3 July 2024 (YQ-E443); both are recorded.
- 172 `172-south24.net` (South24, "E-commerce in Yemen: Individual Successes and Collective Challenges", 15 April 2025): read in full (`text.txt`). Conditions YQ-E532 to YQ-E541; citations YE-E667 to YE-E678. On legal protection it reports three positions (no e-commerce legislation, YQ-E538; a lawyer's view that commercial laws cover it, YQ-E539; the ministry applying general laws for now, YQ-E540); each is recorded.
- 173 `173-staging.fintech-expert.net` (a Floosak admin portal sign-in page): read (`text.txt`). It is a login form for operators and states nothing about selling or paying. 0 conditions.
- 174 `174-stcpay.com.sa`: not readable. The run's result is "blocked from here" (connection reset; the browser failed too); the folder has no text file. 0 conditions.
- 175 `175-stripe.com` (Stripe, global availability, live page): read (`text.txt`). Condition YQ-E543; citations YE-E683, YE-E684. The page lists the countries where Stripe is supported; Yemen is not in the list.
- 176 `176-support.coingate.com` (CoinGate, countries not supported for payments, live page): read (`text.txt`). Condition YQ-E542; citations YE-E679 to YE-E682.
- 177 `177-tax.gov.ye` (Law No. 7 of 2020 amending the General Sales Tax Law, on the tax authority's site; issued in Sana'a on 3 May 2020): read in full (`text.txt`). Conditions YQ-E544, YQ-E545; citations YE-E685 to YE-E700.
- 178 `178-tech-ye.com` (Technology Community magazine, interview with a banker on e-wallets, 9 December 2021, Arabic): read in full (`text.txt`). Conditions YQ-E546 to YQ-E550; citations YE-E701 to YE-E706.
- 179 `179-thefintechtimes.com` (The Fintech Times, "Yemen: Can Fintech Connect an Economy Divided by War?", 10 September 2026): read in full (`text.txt`). Conditions YQ-E551 to YQ-E561; citations YE-E707 to YE-E718.
- 180 `180-torodexpress.com` (Torod courier, FAQ, live page, Arabic): read in full (`text.txt`). The page names no place, so its rows have `place not stated`. Conditions YQ-E562 to YQ-E570; citations YE-E719 to YE-E731.
- 181 `181-tradingeconomics.com` (Trading Economics, Yemeni rial page): read (`text.txt`). Condition YQ-E571; citation YE-E732. Its quote (USD/YER 236.15 on 9 October 2026) is far from the rates other items give for Aden and Sana'a; it is recorded as given.
- 182 `182-trilegal.com`: not readable. The run's result is "blocked from here" (HTTP 429; the browser got 403); `text.txt` holds 58 bytes. 0 conditions.
- 183 `183-ukrpublisher.com` (journal article on Bazzarry customers in Aden, published 31 August 2026, PDF text in two columns): read (`text.txt`; the statistical tables and regression results were skimmed). Conditions YQ-E572, YQ-E573; citations YE-E733 to YE-E738.
- 184 `184-unctad.org`: not readable. The run's result is "blocked from here" (HTTP 403; the browser got 403); `text.txt` holds only Cloudflare's security-check page. 0 conditions.
- 185 `185-usa.visa.com` (Visa, "Visa's Payment Facilitator Model", dated 21 February 2024, PDF text): read in full (`text.txt`). It sets out Visa's rules for payment facilitators, which it says apply across all Visa regions and countries; it does not mention Yemen. 0 conditions.
- 187 `187-wise.com` (Wise currency converter, Yemeni rial to US dollar, live page): read in full (`text.txt`). Condition YQ-E574; citations YE-E739, YE-E740. Its mid-market rate (1 USD = 236.197 YER) is close to item 181's and far from the rates other items give for Aden and Sana'a; it is recorded as given.
- 188 `188-wise.com` (Wise guide, "Top payment methods in Yemen", undated): read in full (`text.txt`). Its statements about Yemen's payments and about PayPal are not about Wise's own service, so they have no date; its listing of Wise itself takes the capture date. Conditions YQ-E575 to YQ-E580; citations YE-E741 to YE-E750.
- 189 `189-wise.com` (Wise help centre, "Where can I use Wise?", live page): read in full (`text.txt`). Condition YQ-E581; citations YE-E751 to YE-E754. It lists Yemen among the places where Wise does not offer its services, where item 188 lists Wise among the payment options for use in Yemen (YQ-E580); both are recorded.
- 190 `190-woocommerce.com` (WooCommerce feature request "we need paymen in Yemen", 20 December 2021, with a comment of 25 January 2023): read in full (`text.txt`). Conditions YQ-E582, YQ-E583; citations YE-E755 to YE-E759.
- 191 `191-2dec.net` (2 December news agency, currency prices against the rial in Sana'a and Aden, Arabic): read in full (`text.txt`; the gold prices and the news ticker were passed over). Conditions YQ-E584, YQ-E585; citations YE-E760 to YE-E765.
- 192 `192-aa.com.tr` (Anadolu Agency, "Yemen's warring rivals agree to de-escalate economic conflict: UN", 23 July 2024): read in full (`text.txt`). Conditions YQ-E586, YQ-E587; citations YE-E766 to YE-E768. It dates the Central Bank of Yemen's suspension of six Sana'a-headquartered banks' licences to 10 July (YQ-E586), where item 163 gives 3 July 2024 (YQ-E443); both are recorded.
- 193 `193-adslgate.com` (ADSLGATE forum thread, 24 to 26 December 2015, on checking whether Instagram stores can be trusted; captured through the browser): read in full (`text.txt`). It names banks such as Al-Ahli and Al-Rajhi and Aramex's pay-on-receipt shipping, and does not mention Yemen. 0 conditions.
- 194 `194-afi-global.org` (AFI opinion piece, "Central Bank of Yemen issues new mobile banking regulations", 7 March 2015): read in full (`text.txt`). Conditions YQ-E588, YQ-E589; citations YE-E769 to YE-E772.
- 195 `195-aiddata.org` (AidData blog, "Leveraging remittances for economic recovery in Yemen", April 29, 2026; the manifest calls it undated, but the page shows the date): read in full (`text.txt`). The report's six recommended reforms are not recorded. Conditions YQ-E590 to YQ-E598; citations YE-E773 to YE-E782.
- 196 `196-alarabiya.net` (Al Arabiya, 30 May 2024, on the central bank and banks): not readable. The run's result is "blocked from here" (HTTP 403; the browser got 403); `text.txt` holds only a CAPTCHA page, and `raw.html` and `raw-browser.html` are an access-denied page and the same CAPTCHA page. 0 conditions.
- 197 `197-alaraby.co.uk` (Al-Araby Al-Jadeed, on the central bank fixing a new rial exchange rate, 15 February 2026, Arabic; captured through the browser): read in full (`text.txt`). Conditions YQ-E599 to YQ-E606; citations YE-E783 to YE-E792. On the supply of banknotes it reports banking sources describing a liquidity crisis (YQ-E602) and an economist doubting it (YQ-E603); both are recorded. The experts' proposals are not recorded.
- 198 `198-alayyam.info` (Al-Ayyam, from Asharq Al-Awsat, on Houthi restrictions on internal travel and money transfers, 25 August 2020, Arabic; the manifest calls it undated, but the page shows the date): read in full (`text.txt`; the site's lists of other articles were passed over). Conditions YQ-E607 to YQ-E614; citations YE-E793 to YE-E801.
- 199 `199-alayyam.info` (Al-Ayyam, "the central bank stops money transfers through exchange companies' networks", 18 February 2024, Arabic; the manifest calls it undated, but the page shows the date): read in full (`text.txt`; the site's lists of other articles were passed over). Condition YQ-E615; citations YE-E802 to YE-E804.
- 200 `200-alayyam.info` (Al-Ayyam, launch of the unified money transfer network in Aden, 2 March 2024, Arabic; the manifest calls it undated, but the page shows the date): read in full (`text.txt`; the site's lists of other articles were passed over). Conditions YQ-E616 to YQ-E619; citations YE-E805 to YE-E814.
- 201 `201-aljazeera.net` (Al Jazeera, "between Aden and Sana'a, the divided rial", 19 July 2025, Arabic): read in full (`text.txt`). Conditions YQ-E620 to YQ-E630; citations YE-E815 to YE-E828. It dates the Houthi ban on banknotes printed after 2016 to 2020 (YQ-E621), as item 155 does (YQ-E287).
- 202 `202-almashhad.news` (Al-Mashhad Al-Yemeni, the Minister of Justice's decision No. 15/2025 on the rial, 18 August 2025, Arabic): read in full (`text.txt`). Condition YQ-E631; citations YE-E829 to YE-E835. It says the decision applies within the Republic of Yemen; items 162 and 164 give the rule for the government's or CBY-Aden's area (YQ-E426, YQ-E480); each is recorded as its source gives it.
- 203 `203-alndaa.net` (Al-Nidaa, the central bank in Sana'a stops dealings with Al-Kuraimi Bank, published 22 June 2025 per its JSON-LD, Arabic): read in full (`text.txt`). Conditions YQ-E632, YQ-E633; citations YE-E836 to YE-E838.
- 204 `204-alnkkar.com` (Al-Nakkar, Al-Kuraimi Bank cut off from the banking system in Sana'a, published 22 June 2025 per its metadata, Arabic): read in full (`text.txt`). Its forecasts of the decision's effects are recorded only where they state how payments are made now (YQ-E639, YQ-E640). Conditions YQ-E634 to YQ-E641; citations YE-E839 to YE-E847.
- 205 `205-arabnews.com` (Arab News, "How the Houthis built a parallel economy in Yemen", 7 August 2026): read in full from `raw.html`. Its `text.txt` holds only Cloudflare's security-check page (the browser got 403), but the raw fetch (HTTP 200) holds the article, one paragraph to a line, so the citations quote `raw.html` by line. Conditions YQ-E642 to YQ-E655; citations YE-E848 to YE-E864.
- 206 `206-bain.com` (Google and Bain & Company, "E-commerce in MENA: Opportunity beyond the hype", 2019, PDF text): read (`text.txt`: the report skimmed, its payments section read, and a search for Yemen). Yemen appears only in the notes that define MENA for regional totals; the report states nothing about Yemen itself (its consumer survey covered Saudi Arabia, the UAE and Egypt). 0 conditions.
- 207 `207-bpcbt.com` (BPC, "Case study WeNet" landing page, undated): read in full (`text.txt`; the rest is a download form). BPC describes its client's service, so the rows have no date. Conditions YQ-E656, YQ-E657; citations YE-E865 to YE-E867.
- 208 `208-bpcbt.com` (BPC case study PDF on WeNet; it shows no date, so its rows take the PDF's creation date, July 2022; text partly in two columns): read in full (`text.txt`). Two-column passages are quoted line by line. Conditions YQ-E658 to YQ-E665; citations YE-E868 to YE-E896.
- 209 `209-cacbank.com.ye` (CAC Bank, Visa cards page, live page): read in full (`text.txt`; the FAQ shows only questions). The page names no place, so its rows have `place not stated`. Conditions YQ-E666, YQ-E667; citations YE-E897 to YE-E904.
