# Yemen mobile wallets and e-money as rails for online commerce payments (as of 9 October 2026)

Scope note: this file covers mobile wallets and e-money only: wallet-to-merchant checkout, wallet APIs and wallet interoperability. Banks, cards, exchange-house hawala and cash on delivery are covered by other researchers. Source quality key:
- **[primary]** means a regulator, operator or app-store listing.
- **[community code]** means the open-source clients by GitHub user Alsharie and others. They show the shape of an API, are not official documentation, and may be out of date. The date of the last commit is given for each.
- **[secondary]** means a think tank or press source.

The cut-off is 9 October 2026, and dates are given wherever a source has one. Many app-store version entries show only a day and month. Where the year is missing, this file says so.

## Which wallets exist and are active as of 2026, who backs each, and where do they work?

### Takeaway
Yemen has two wallet systems that are now legally hostile to each other.
- **Sana'a side.** A non-bank e-money model was set up under CBY-Sana'a Decision No. 1 of 2020. The wallets licensed there include Jawali, Cash, Floosak, ONE Cash, Jaib, SabaCash, Mobile Money, Yemen Wallet and Al-Dawli Money. In June 2024 the Aden-based CBY named 12 Sana'a-based wallets and entities as unlicensed and banned dealing with them.
- **Aden side.** A bank-led model plus licensed non-bank issuers (instructions of August 2023, amended July 2025). It covers the wallets of banks that moved their headquarters to Aden in 2025: Kuraimi's mFloos and Hasib, Shamil Money, Al-Amal, Tadhamon, Saba Islamic and others. It also covers Aden-native products such as Aden Cash and the MEPS "Yemen National Wallet".

ONE Cash (Hayel Saeed Anam group) is the largest non-bank wallet by its own reported numbers: more than 700,000 active customers and more than 15,000 agents in 2024. It was not on Aden's June 2024 ban list. Kuraimi has historically been the largest bank wallet: 80% of e-money accounts in 2019.

### Cited Findings

**Regulatory frame (both sides)**
- **Before the split (2014–2019).** CBY Circular No. 11 of 2014 set up a bank-led model. Between 2015 and 2019 the CBY licensed four banks to offer mobile e-money: Al-Kuraimi Islamic Microfinance Bank, Tadhamon, Al-Amal Microfinance Bank and Yemen Kuwait Bank (YKB). CBY-Sana'a licensed CAC Bank. — [Sana'a Center, *Challenges and Prospects for Electronic Money and Payment Systems in Yemen*, March 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- **Licensing sequence.** Kuraimi was licensed in 2015 and launched in 2016. Tadhamon was licensed in 2016 and started e-rial services in 2018. Al-Amal was licensed in 2017. YKB and CAC were licensed in 2018. — [Sana'a Center 2022, fn. 46](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- **Sana'a opened e-money to non-banks.** CBY-Sana'a licensed Shamil Bank of Yemen & Bahrain (SBYB) and International Bank of Yemen (IBY) in January 2021. In March 2020 it issued a directive (Decision No. 1 of 2020) that let non-banks, including exchange companies and traders, issue e-rials. It set no cap on issuance. In Q1 2021 it permitted "IBY, SBYB, One and Tamkeen" to provide e-rials. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- **Aden rejected that model.** CBY-Aden challenged the 2020 Sana'a directive. Two models resulted: "the non-bank model in Houthi-controlled areas and the bank-led model in government-controlled areas." — [Sana'a Center, *Fostering Opportunities for E-Commerce Growth in Yemen*, Sept 2025](https://sanaacenter.org/files/RYE_E_Commerce_in_Yemen_NO35_en.pdf)
- **CBY-Aden's own non-bank e-money rules.** CBY-Aden issued instructions for mobile e-money by non-bank institutions: Ref 547/CBY/2023, dated 8–9 August 2023. They define an "E-money Issuer" (a licensed payment service provider), a "Settlement Bank" and a "Trust Account". The trust account is a pooled account at the settlement bank owned by e-money holders, not by the issuer. — [CBY-Aden instructions PDF](https://www.cby-ye.com/files/64dde85e0a84f.pdf) [primary]
- **Prudential rules in those instructions:**
  - The trust account must equal 100% of outstanding e-money.
  - Trust balances at any one settlement bank may not exceed 30% of that bank's total deposits.
  - Issuer capital must be at least 25% of e-money issued.
  - The trust account must be reconciled daily.
  - Accounts were originally YER-only.
  - Legal-person accounts require a commercial register.
  - Each account is tied to one mobile number.
  - Customers must disclose wallets they hold with other issuers.

  — [CBY-Aden instructions 2023](https://www.cby-ye.com/files/64dde85e0a84f.pdf) [primary]
- **Decision No. 4 of 2025 (CBY-Aden, Ref 349/CBY/2025, 9 July 2025).**
  - It allows non-bank e-money issuers to hold USD, SAR and AED as well as YER, but bars conversion from local to foreign currency.
  - Individual account limits in local currency: YER 1,000,000 per transaction, 2,000,000 per day, 5,000,000 per month and 50,000,000 per year.
  - Individual account limits in foreign currency: USD 400 per transaction, 500 per day, 1,000 per month and 10,000 per year.
  - Limits for legal-entity accounts are set by the issuer, with the CBY's prior written approval.
  - The maximum individual balance is YER 8,000,000 or USD 1,500.

  — [CBY-Aden Decision 4/2025](https://www.cby-ye.com/files/6875fc55a253e.pdf) [primary]
- **June 2024 Aden ban list.** On about 26 June 2024, CBY-Aden ordered all banks and exchange companies to stop dealing with 12 unlicensed wallets and e-payment entities "operating from Sana'a":
  - Cash
  - Al-Dawli Money
  - Jawali
  - Floosak
  - Saba Cash
  - Mobile Money
  - Yemen Wallet
  - Electronic Riyal (الريال الإلكتروني)
  - Riyal Mobile
  - Jaib
  - WeCash for e-payment services
  - Al-Mutakamila

  ONE Cash is not on the list. — [Yemen Eco, 26 June 2024](https://yemeneco.org/archives/84396); [CBY-Aden news/703](https://cby-ye.com/news/703)
- **Aden's internal-transfer decision.** A CBY-Aden governor's decision of 26 June 2024 bans internal cash transfers by any means. It exempts licensed e-wallets and payment service providers within approved limits (per a search summary of the CBY page; full text not read). — [CBY-Aden news/706](https://cby-ye.com/news/706)
- **2025 bank exodus to Aden.** On 16–17 March 2025, after the US re-designated the Houthis as a Foreign Terrorist Organization (FTO) on 4 March 2025, CBY-Aden announced that eight banks would move their headquarters from Sana'a to Aden:
  - Tadhamon
  - Al-Kuraimi
  - Shamil Bank of Yemen & Bahrain
  - Yemeni Islamic Bank
  - Saba Islamic Bank
  - Yemen Gulf Bank
  - Yemeni Commercial Bank
  - Al-Amal Microfinance

  — [Barran Press, 16 Mar 2025](http://en.barran.press/news/6389). YBRD became the ninth in July 2025. — [Barran Press](https://en.barran.press/news/6780). CBY-Aden's governor announced on 30 July 2025 that the whole banking system had moved (per a search summary). — [SPA](https://www.spa.gov.sa/N2370482)
- **Sana'a's retaliation against Kuraimi.** CBY-Sana'a ordered exchange companies and remittance networks to stop dealing with Kuraimi from 22 June 2025, with 15 days to clear balances. One observed effect is that mFloos users receiving transfers through Kuraimi channels may be unable to continue through official exchangers. — [Alnkkar](https://www.alnkkar.com/news25084.html); [Al-Nidaa](https://www.alndaa.net/102197/central-bank-sanaa-suspends-dealings-alkuraimi-bank-gives)
- **US sanctions on wallet-linked banks.** OFAC designated Yemen Kuwait Bank on 17 January 2025 and International Bank of Yemen (with three executives) in April 2025, for supporting the Houthis. Neither action mentions wallets. — [US Treasury jy2794](https://home.treasury.gov/news/press-releases/jy2794); [Amwal Al Ghad on IBY](https://en.amwalalghad.com/?p=198781)

**Catalog of wallets** (operator / licensing bank / launch / area / scale)

- **mFloos (ام فلوس) + Kuraimi Jawal + "Hasib" (حاسب) payments — Al-Kuraimi Islamic Microfinance Bank**
  - First bank licensed for e-money (2015); launched 2016. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - Held 80% of all e-money accounts in December 2019, with 132 branches, 2,626 agents and 7,620 points of sale (Institute of Banking Studies figures). — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - Had 210 branches nationwide in 2022. — [Alnkkar](https://www.alnkkar.com/news25084.html)
  - Moved its headquarters to Aden in 2025; Sana'a suspended dealings with it from June 2025 (see above).
  - Hasib is described as "the first and largest e-payment gateway in Yemen", payable from the mFloos or Kuraimi Jawal apps. — [Kuraimi Bank, Hasib service page](https://kuraimibank.com/ar/services/39) [primary]. Text read via the site's JSON at `kuraimibank.com/api/ar/services/39`.
- **Floosak (فلوسك) — Yemen Kuwait Bank (YKB) / Quality Connect**
  - The 2019 IBS channel data labels Floosak as YKB's wallet: 391 agents, 5,071 POS, 17 branches. — [Sana'a Center 2022, Fig. 3](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - Quality Connect is "jointly owned by Yemen Kuwait Bank (YKB), Swaid & Sons for Exchange, and Al Akwaa Exchange". — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - A 2025 community client says merchant credentials come "from QualityConnect". — [Alsharie/floosak-payment-js README, last commit 2025-06-17](https://github.com/Alsharie/floosak-payment-js) [community code]
  - The Play listing describes transfers, cash withdrawal, commercial payments and bills, and "Floosak Network and Akwa Money Network" transfers. — [Google Play, co.ysys.floosak](https://play.google.com/store/apps/details?id=co.ysys.floosak&gl=US)
  - Floosak is on Aden's June 2024 ban list, and YKB was OFAC-designated in January 2025.
  - The floosak.com site returned HTTP 522 when probed on 9 October 2026, so no current operator site was found.
- **Cash / Cash Pay (كاش) — Tamkeen (Sana'a)**
  - Cash's site lists a Sana'a address, "around 1500 service agents throughout Yemen", QR payments, and the Cash Pay e-commerce service with "API" integration. The contact address is customercare@tamkeen.com.ye. — [cash.com.ye about](https://www.cash.com.ye/en/about-us); [Cash Pay page](https://www.cash.com.ye/en/cash-pay-electronic-payment-service) [primary]
  - The Play package ID is `com.tamkeen.sms`. — [cash.com.ye links](https://www.cash.com.ye/en/about-us)
  - The CashPay API base URL in the community client is `https://www.tamkeen.com.ye:33291/CashPG`. — [Alsharie/cash-payment](https://github.com/Alsharie/cash-payment) [community code, last commit 2024-03-17]
  - Cash is on Aden's June 2024 ban list.
  - Conflict: a consumer blog attributes Cash (and Floosak) to Yemen Kuwait Bank. — [TechMadar, ~May 2025](https://www.techmadar.com/2025/05/Electronic%20wallets%20in%20Yemen.html). The operator's own site points to Tamkeen. YKB may be a settlement bank; an undated forum comment says YKB is licensed for three wallets and acts as a settlement bank (search summary only, not verified).
- **Jawali (جوالي) — WeCash for Electronic Payment Services and Systems (Sana'a)**
  - Jawali is "a service provided by WeCash". Cash-in and cash-out run through agents and the Al-Najm, Al-Imtiaz and Yemen Express exchange networks. Opening an account needs a mobile number and an ID. — [jawali.com.ye/en/about](https://jawali.com.ye/en/about) [primary]
  - The Terms say the service operates "under the supervision of the Central Bank of Yemen", with balances in escrow accounts. Partner banks are Yemen & Kuwait Bank, Yemeni Commercial Bank and YBRD. Accounts may be held in YER and "some foreign currencies". — [Jawali Terms](https://jawali.com.ye/Terms/) [primary]
  - WeCash launched in 2021. — [Lendsqr profile](https://lendsqr.com/providers/wecash) [secondary]
  - A headline dated 13 July 2022 reads "وي كاش تطلق خدمة جوالي" (WeCash launches Jawali). — [tech-ye.com related links](https://tech-ye.com/%D8%A7%D9%84%D9%85%D8%AD%D8%A7%D9%81%D8%B8-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A%D8%A9/)
  - Self-reported "more than a Million subscribers" (seen only in a search-result summary of jawali.com.ye).
  - Both Jawali and WeCash are on Aden's June 2024 ban list.
- **ONE Cash (ون كاش) — National Electronic Wallet Co. (Hayel Saeed Anam group)**
  - Established in 2018; launched in December 2022; founders Ahmed N. and Mohamed N. Hayel Saeed. Reported figures: more than 700,000 active customers; 14.7M transactions worth US$2.5bn in 2024; more than 1.4M downloads by December 2024; more than 15,000 agents. — [Forbes ME Fintech 50, 2025](https://www.forbesmiddleeast.com/lists/the-middle-easts-fintech-50-2025/one-cash/)
  - CBY-Sana'a issued an initial license in July 2020 and a final license in early 2022. CBY-Aden had not accepted its license request as of March 2022. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - Earlier figures: 200,000 active customers, more than 14,000 outlets and "800 corporations reportedly use the mobile service to accept payment" (Forbes 2024 via Sana'a Center 2025). — [Sana'a Center 2025](https://sanaacenter.org/files/RYE_E_Commerce_in_Yemen_NO35_en.pdf)
  - The App Store seller is "National Electronic Wallet Company". The first version (1.0.1) is dated 5 April 2023. — [App Store](https://apps.apple.com/us/app/id1661455867)
  - The Google Play operator address is in Sana'a (per search summary). — [Google Play](https://play.google.com/store/apps/details?id=com.one.onecustomer&hl=en_US)
  - More than 1M Android downloads. — [Fintech Times, 10 Sept 2026](https://thefintechtimes.com/yemen-can-fintech-connect-an-economy-divided-by-war/)
  - YKB's website has a page at `/ar/Personal/e-wallet/one-cash` titled "ون كاش" (it returned HTTP 403, so the content was not read). — [yk-bank.com](https://www.yk-bank.com/ar/Personal/e-wallet/one-cash)
- **Jaib (جيب) — AHD for Financial Services and Electronic Payment Systems Co.**
  - The App Store seller is "AHD for Financial Services and Electronic Payment Systems Company". The earliest iOS version is dated 19 March 2024 and v1.0.0 is dated 18 September 2024. Recent versions (3.0.x) show no year.
  - Features: merchant purchases by scanning a QR code or entering the point-of-sale number, and agent cash-in/out.
  - Integrations: the Al-Najm, Al-Imtiaz, Yemen Express, Al-Akwa and other exchange networks, "WeNet" for merchant transfers, and "Tahweel".

  — [App Store](https://apps.apple.com/us/app/id6472856710) [primary]. Jaib is on Aden's June 2024 ban list. Its licensing bank was not found.
- **SabaCash (سبأ كاش) — SabaFon (Yemen Company for Mobile Telephony) with "CAC Islamic Bank"**
  - The App Store listing describes an e-money service by SabaFon in partnership with CAC Islamic Bank, with "Pay to merchant" and USSD access for SabaFon numbers. The earliest listed version is dated 15 January 2023, and versions are dated as late as 31 December 2025. — [App Store](https://apps.apple.com/app/id1591917243)
  - The community client's API base is `https://api.sabacash.ye:49901`. — [Alsharie/sabacash-payment, last commit 2023-12-17](https://github.com/Alsharie/sabacash-payment) [community code]
  - SabaCash is on Aden's ban list. The SabaFon launch page (`sabafon.com.ye/?p=23434`) returned HTTP 503.
- **Mobile Money (موبايل موني) — CAC Bank (Cooperative & Agricultural Credit Bank)**
  - Licensed by CBY-Sana'a in 2018. In 2019 its channels were 2,222 POS, 50 branches and 26 agents (IBS). — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - It was one of three platforms authorized in December 2019 to swap new rial notes for e-rials. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - It is on Aden's June 2024 ban list.
- **PYes — Al-Amal Microfinance Bank**
  - Licensed in 2017. In 2019 it had 238 agents, 1,547 POS and 15 branches. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - Al-Amal moved its headquarters to Aden in 2025. — [Barran Press](http://en.barran.press/news/6389)
  - No 2025–26 product information was found.
- **Mahfathati (محفظتي) / "Tadhamon Pay" — Tadhamon Bank**
  - In 2019 it had 90 agents, 116 POS and 28 branches. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - ONE Cash added "Vouchers via Tadhamon Pay" on 26 March 2025. — [ONE Cash App Store version history](https://apps.apple.com/us/app/id1661455867)
  - Tadhamon moved to Aden in 2025. No Tadhamon Pay product page was found.
- **Shamil Money (شامل موني) — Shamil Bank of Yemen & Bahrain**
  - The bank's FAQ says Shamil Money runs "under the license of the Central Bank of Yemen".
  - Merchant payment works by entering the store code or scanning the store's QR code. Merchants need a commercial register or business license.
  - Limits: temporary (self-registered) customers YER 10,000 per day and 100,000 per month; permanent customers up to YER 30 million.
  - Fees: no deposit fee; withdrawals at agents start at YER 100.
  - Up to three accounts are allowed on three mobile numbers.

  — [sbyb.net/faq](https://www.sbyb.net/faq) [primary, undated]. SBYB moved to Aden in 2025.
- **Al-Dawli Money (الدولي موني) — International Bank of Yemen (IBY)**
  - IBY was licensed by CBY-Sana'a in January 2021. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
  - Al-Dawli Money is on Aden's 2024 ban list, and IBY was OFAC-designated in April 2025.
- **Yemen Wallet (يمن والت) — Yemen Post (Sana'a)**
  - The App Store seller is YEMEN POST. Features: top-up, cash-in/out, bills and wallet-to-bank transfers. — [App Store id6449282553](https://apps.apple.com/us/app/-/id6449282553) (per search summary)
  - It is on Aden's ban list.
- **Aden Cash (عدن كاش) — Aden Islamic Bank for Microfinance (Aden)**
  - Described as a wallet "under the license of the Central Bank of Yemen"; the HQ is in Al-Mansoura, Aden. — [aden.adenbank.com](https://aden.adenbank.com/en/service/aden-cash-wallet) [primary]
  - A community merchant client exists, with base `https://api.adenbank.ye:49901`. — [Alsharie/adenbank-payment, last commit 2024-03-23](https://github.com/Alsharie/adenbank-payment) [community code]
- **Yemen National Wallet — MEPS Yemen (Middle East Payment Services)**
  - Features: wallet-to-wallet and bank-to-wallet transfers, store payment by card or QR, a prepaid card linked to the wallet that works on global e-commerce, and agent/ATM cash-in/out. No release date is shown. — [App Store id6503729833](https://apps.apple.com/us/app/id6503729833)
- **Al-Qutaibi Islamic Bank (بنك القطيبي) e-payment**
  - A community client calls "E_Payment/RequestPayment" and "E_Payment/ConfirmPayment" at `https://newdc.qtb-bank.com:5052/PayBills`. — [Alsharie/AlQutaibiBank-payment, last commit 2024-03-06; repo updated 2026-09-23](https://github.com/Alsharie/AlQutaibiBank-payment) [community code]
  - The wallet's brand name, licensing side and launch date were not found (qtb-bank.com returned a 502 through the proxy).
- **"National Wallet Company" (Telepin) — background, 2020**
  - Telepin (Ottawa) announced in January 2020 that it would supply wallet technology to Yemen's "National Wallet Company", "backed by 11 major banks in Yemen". — [Ottawa Business Journal, 21 Jan 2020](https://obj.ca/?p=89016)
- **Others named only in the Aden ban list, with operators not found:** Electronic Riyal, Riyal Mobile, Al-Mutakamila. — [Yemen Eco](https://yemeneco.org/archives/84396)

**Aggregate scale (stale)**
- E-money accounts rose from about 82,000 (2017) to 807,919 (December 2019). Of new accounts, 91% were urban. — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf); [Sana'a Center 2025](https://sanaacenter.org/files/RYE_E_Commerce_in_Yemen_NO35_en.pdf)
- In the 2021 Findex, 98.9% of respondents had made no digital payment to a merchant. Cash still accounts for 61.9% of online transactions. — [Sana'a Center 2025](https://sanaacenter.org/files/RYE_E_Commerce_in_Yemen_NO35_en.pdf)

### Inferences
- **"Seller in Sana'a" vs "seller in Aden" is a first-order design axis, not a detail.**
  - A wallet licensed in Sana'a is, from Aden's point of view, an unlicensed entity that Aden-regulated banks and exchangers may not deal with. This covers Jawali, Cash, Floosak, Jaib, SabaCash and Mobile Money.
  - Since June 2025, Kuraimi, the biggest bank wallet, is in turn blocked by Sana'a for exchanger dealings. Its app-based services in Houthi areas were not confirmed either way.
- **ONE Cash may be the only large non-bank wallet that both sides tolerate.** It is HSA-owned, is absent from Aden's ban list, has a Sana'a license and is linked to WeNet. This rests on absence from a list, not on a confirmed Aden license; treat it as unverified.
- **US sanctions are a risk for any foreign-linked platform** that settles through YKB (OFAC-designated) or IBY. Floosak/Quality Connect has YKB as a co-owner, and Jawali names YKB as a partner bank.

### Gaps
- No authoritative list of wallets licensed by CBY-Aden or CBY-Sana'a as of 2026 was found. The CBY-Aden supervision page lists licensed banks and exchangers for 2026, but no e-money issuers. — [cby-ye.com/pages/14](https://cby-ye.com/pages/14)
- No 2025–26 user or agent numbers were found for Jawali, Cash, Floosak, Jaib, SabaCash, mFloos, Shamil Money or Aden Cash, apart from self-reported figures.
- The GSMA Mobile Money Deployment Tracker was not consulted (no result surfaced).
- Several provider sites were not reachable from this environment (connection resets): onecash, jaib, sabacash and floosak (HTTP 522).
- The relationships between WeCash (Jawali) and WeNet, and between ONE Cash and the 2020 Telepin "National Wallet Company", are unconfirmed.

## How do merchants and online sellers actually accept wallet payments today, and which wallets offer integration APIs to third parties?

### Takeaway
There are five acceptance patterns, all live:
1. **Merchant-initiated pull confirmed by the buyer's OTP:** Floosak "P2MCL", CashPay, SabaCash, Aden Cash, Al-Qutaibi.
2. **Buyer PIN entered on the merchant's site after a one-time store activation in the bank app:** Kuraimi Hasib.
3. **Buyer-made voucher redeemed by the merchant:** Jawali e-commerce.
4. **In-store QR or merchant code:** Jaib, Shamil Money, Cash, Hasib points, MEPS.
5. **Informal "send to my wallet number and show proof":** used by many small sellers. A 2026 open-source gateway automates it by reading SMS and notifications.

Partner APIs exist for Floosak, CashPay, Jawali, SabaCash, Kuraimi (Hasib/E-Pay), Aden Cash and Al-Qutaibi. Every one is bilateral, needs credentials and is onboarded manually. None has public developer documentation.

### Cited Findings

**How merchants accept, as operators describe it** [primary]
- **Cash Pay (Cash/Tamkeen).**
  - The merchant opens a Cash wallet account, adds Cash Pay to the site, and completes integration "with Cash Wallet's technical support team" via API.
  - The buyer enters the wallet phone number, an "Online Purchase Code" (in the Cash app under Settings → Online Purchase Code) and an SMS verification code.
  - Funds go "deducted from their account and added to your Cash Wallet account", and the merchant withdraws cash at any Cash agent.
  - Merchant tools reportedly allow sales reports and "refund money instantly".

  — [Cash Pay page](https://www.cash.com.ye/en/cash-pay-electronic-payment-service). The separate consumer "Online Shopping" page still reads "SOON..". — [cash.com.ye/en/online-shopping](https://www.cash.com.ye/en/online-shopping)
- **Cash merchant features:** invoice creation and payment, branch-level tracking ("Connect your branches"), salary disbursement and cash withdrawal "with financial limits that suit your business". — [Cash companies and merchants](https://www.cash.com.ye/en/companies-merchants-features)
- **Kuraimi Hasib, online.** The buyer:
  1. creates a 4-digit PIN in Kuraimi Jawal or mFloos;
  2. activates each shopping app or site once from a list in the bank app, selecting the bank account to debit and entering the mobile or email registered at that store;
  3. at checkout, chooses Hasib on the store and enters the PIN.

  The online limit is "up to one million rials per operation", and multiple currencies are supported. — [Kuraimi service 33 FAQ inside service 39](https://kuraimibank.com/ar/services/39); [service 32](https://kuraimibank.com/ar/services/32). Kuraimi has also posted instructions for setting the identification code for shopping apps. — [Kuraimi on X](https://x.com/Kuraimibank/status/1757763346227425454)
- **Kuraimi Hasib, in store ("Hasib points").** The buyer enters the merchant's point number or scans its QR code, with a limit of YER 400,000 per transaction.
  - Merchants need a fixed physical address, a business account at Kuraimi and a signed agreement at a branch.
  - Merchants can add multiple cashier points, see reports, "return amounts of operations to customers", and re-use collections for salaries, bills and supplier payments.

  — [Kuraimi services 39/33](https://kuraimibank.com/ar/services/39)
- **Kuraimi "Electronic linking service (API)".** For apps or sites selling goods:
  - It offers "an independent account for e-payment operations for each region as you need".
  - "Amounts reach your business accounts directly when the customer places the order."
  - It eases reconciliation of purchase and refund operations, and the merchant's app icon is shown inside the bank apps.
  - Requirements: an app or site, a company account at the bank and signed agreements; apply at a branch.

  — [Kuraimi service 50](https://kuraimibank.com/ar/services/50) [primary, undated]
- **Jaib:** QR scan or entry of the POS number at shops. **Shamil Money:** store code or store QR. **MEPS Yemen National Wallet:** card or QR at stores. **SabaCash:** "Pay to merchant". **ONE Cash:** "pay at our wide network of merchants" plus "payments and purchases on apps and websites". — [Jaib](https://apps.apple.com/us/app/id6472856710); [Shamil](https://www.sbyb.net/faq); [MEPS](https://apps.apple.com/us/app/id6503729833); [SabaCash](https://apps.apple.com/app/id1591917243); [ONE Cash](https://apps.apple.com/us/app/id1661455867)
- **ONE Cash's agent and merchant app** ("ONE كاش: الوكيل - نقطة الدفع") lists receiving payment for goods, refunds, and transfers between business wallets and bank accounts. No API is mentioned. — [Google Play com.one.oneagent](https://play.google.com/store/apps/details?id=com.one.oneagent&hl=en_US) (via search summary)
- **Jawali's site** advertises paying for purchases in "stores and electronic applications" and collecting sales value. — [jawali.com.ye](https://jawali.com.ye/en/about)
- **Market practice (2025).** E-commerce still relies mostly on cash on delivery. Bazzarry, a large marketplace, lets customers "choose between paying cash on delivery or via a number of locally available e-wallets and ATMs". An MNO strategist called for a "unified payment gateway". — [Sana'a Center 2025](https://sanaacenter.org/files/RYE_E_Commerce_in_Yemen_NO35_en.pdf)

**API shapes from community clients** [community code: evidence of shape only]

- **Floosak "P2MCL"** — [Alsharie/floosak-payment](https://github.com/Alsharie/floosak-payment) (PHP, last commit 2024-01-30; README: "api after update to (p2mcl)"); [Alsharie/floosak-payment-js](https://github.com/Alsharie/floosak-payment-js) (TS v1.0.0, 2025-06-17)
  - **Merchant authentication:**
    1. `POST /api/v1/request/key` with the merchant phone and short_code returns a `request_id` and sends an OTP to the merchant phone.
    2. `POST /api/v1/verify/key` with request_id and OTP returns a JWT (`key`) and wallet IDs. The README says the token is "valid for one year".
  - **Payment:**
    1. `POST /api/v1/merchant/p2mcl` with `source_wallet_id` (the merchant's wallet), `request_id` (unique, generated by the merchant), `target_phone` (buyer), `amount` and `purpose` returns a purchase id and sends an OTP to the buyer's phone.
    2. `POST /api/v1/merchant/p2mcl/confirm` with `purchase_id` and the buyer's `otp` returns the transaction.
  - **Refund:** `POST /api/v1/merchant/p2mcl/refund` with `transaction_id`, a new `request_id` and `amount` ("Can be a partial or full amount").
  - The transaction object includes `status`, `net`, `fee`, `rate`, `gross` and `reference_id`.
  - The default base URL in the PHP config is `https://staging.fintech-expert.net`.
  - A `FloosakPurchaseStatusResponse` class exists, but the client has no status request method.
- **CashPay (Cash/Tamkeen)** — [Alsharie/cash-payment](https://github.com/Alsharie/cash-payment) (last commit 2024-03-17)
  - Endpoints:
    - `POST {base}/api/CashPay/InitPayment`, with `RequestID` ("Request unique identifier that should be generated by sp"), `TargetMSISDN` (buyer phone), `CustomerCashPayCode` (the buyer's online purchase code), `Amount`, `CurrencyId` and `Desc`. It returns `TransactionRef`.
    - `POST /api/CashPay/ConfirmPayment`, with `RequestID`, `TransactionRef` and `TRCode = md5(TransactionRef + OTP)`.
    - `POST /api/Operation/OperationStatus`, documented as "useful in cases of time out".
  - Authentication: `UserName`, `SpId`, `encPassword` and `MDToken = md5(SpId + UserName + unixtimestamp)`, plus a client certificate and password issued by Cash for production.
  - Currency IDs: 2 = YER, 4 = USD, 5 = SAR.
  - Selected error codes:
    - 6001/6002: duplicated or obsolete timestamp.
    - 6006: "customer not allowed to pay online".
    - 6008: "you must initial payment first (Either the previous step-1 has expired…)".
    - 6010: OTP attempts.
    - 6013: "There is no operation with the entered number (timeout cases)".
    - 6018: "duplicated RequestId".
    - 6020: currency not allowed.
    - 6021: "Exceeding the allowed limit".

  — [CashPayErrorCode.php](https://github.com/Alsharie/cash-payment/blob/master/src/Responses/Error/CashPayErrorCode.php)
  - A separate Flutter plugin, "iframe_cashpay", is listed in a community directory. Its name suggests CashPay also offers an embedded or iframe flow (not inspected). — [awesome-yemeni-open-source](https://github.com/yementechcollective/aweasome-yemeni-open-source)
- **Jawali e-commerce (WeCash "paygate")** — [Alsharie/jawali-payment](https://github.com/Alsharie/jawali-payment) (PHP, last commit 2025-07-16); [Alsharie/jawali-payment-js](https://github.com/Alsharie/jawali-payment-js) (v1.0.3, 2025-02-19)
  - Calls:
    - `POST /oauth/token` (system login).
    - `POST /v1/ws/callWS` with serviceName `PAYWA.WALLETAUTHENTICATION` (merchant "agent wallet" and password), then `PAYAG.ECOMMERCEINQUIRY`, then `PAYAG.ECOMMCASHOUT`.
  - The body carries `voucher`, `receiverMobile`, `purpose`, `accessToken` and a client-generated `refId`. The header `signonDetail` carries `clientID: 'WeCash'`, `orgID`, `userID` and `externalUser`.
  - Flow: an inquiry returns `amount`, `currency`, `state` and `transactionRef`. The merchant checks that `state == 'PENDING'` and the amount and currency match, then calls cash-out to redeem the voucher.
  - The default base URL is a bare IP address (not reproduced here), with an option to disable SSL verification.
  - There is no refund or status-after-cashout call.
- **SabaCash** — [Alsharie/sabacash-payment](https://github.com/Alsharie/sabacash-payment) (last commit 2023-12-17)
  - Calls:
    - `POST /api/user-ms/v1/login` (username/password) returns a token.
    - `POST /api/accounts/v1/adjustment/onLinePayment` with `source.code` (buyer phone), `beneficiary.terminal`, `amount` and `amountCurrencyId` (2 = YER) and `note`. It returns an "adjustment" id and sends an OTP.
    - `PATCH` the same path with `id`, `otp` and `operation: approve|reject`.
    - `GET /api/accounts/v1/adjustment/checkAdjustmentByTransactionId`.
- **Kuraimi E-Pay ("Hasib" API)** — [Alsharie/kuraimiepay](https://github.com/Alsharie/kuraimiepay) (TS v1.0.6, 2025-05-26; cites a "Supplier Integration Guide and Technical Specification")
  - `POST /alk-payments-exp/v1/PHEPaymentAPI/EPayment/SendPayment` with `SCustID` (the customer's ID at the supplier), `REFNO` ("Ensure this is unique"), `AMOUNT`, `CRCY` (default YER), `MRCHNTNAME` and `PINPASS` (the buyer's 4-digit PIN, base64-encoded). It returns `CODE`, `MESSAGE` and `ResultSet.PH_REF_NO`.
  - `POST …/EPayment/ReversePayment` with `SCustID` and `REFNO`.
  - Basic auth; the UAT base URL is `https://web.krmbank.net.ye:44746`.
  - **Reverse call:** the supplier must host a "Verify Customer details API" (HTTP POST with Basic auth). Kuraimi calls it with `SCustID`, `MobileNo`, `Email` and `CustomerZone` to verify the customer when the buyer activates the store. Without it, "E-Payment transactions initiated via Kuraimi Bank's applications (KJ, Mfloos) … may not be possible".
- **Aden Cash (Aden Islamic Bank for Microfinance)** — [Alsharie/adenbank-payment](https://github.com/Alsharie/adenbank-payment) (last commit 2024-03-23)
  - Calls:
    - `auth/v1/auth`.
    - `Payment/Trn` (init), with `cifNo` (buyer phone), `amount`, `currency` (YER), `MrchntID`, `MrchntUser`, `refNo` and `msgID`.
    - `Payment/ApproveTras` (OTP confirmation, with `ApprovalID` and `BankRef`).
    - `Payment/checkOperation` (status).
  - Signing: `password = md5(msgID + username + password)` and `MrchntToken = md5(msgID + username + password + refNo)`.
  - The base host and port (`api.adenbank.ye:49901`) match SabaCash's port pattern (`api.sabacash.ye:49901`). This suggests a shared vendor stack (inference).
- **Al-Qutaibi Islamic Bank** — [Alsharie/AlQutaibiBank-payment](https://github.com/Alsharie/AlQutaibiBank-payment) (last commit 2024-03-06)
  - `E_Payment/RequestPayment` with `payment_CustomerNo` (buyer phone), `payment_Code`, `payment_Amount` and `payment_Curr` (1 = YER). It returns `TransactionID`.
  - `E_Payment/ConfirmPayment`, which adds `payment_OTP`.
  - Headers: `X-APP-KEY` and `X-API-KEY`.
  - The payee is `payment_DestNation`, encrypted into `customer_no` with AES using the API key and a zero IV. It can be set in config or per request.
- **Other community evidence:**
  - "yemeni-payment-gateways" (Laravel) claimed support for Floosak, Jaib, Jawali, Cash, One Cash and Saba Cash. Version 1.0.0 was published on 2024-08-12; the repo has since disappeared and Packagist has frozen it. — [Packagist](https://packagist.org/packages/aymanalhattami/yemeni-payment-gateways)
  - "YemenPay" (created 2026-08-22) is a "unified gateway" for Jaib, Jawaly, Kuraimi, OneCash and Yemen Wallet. Its SDK holds a merchant's wallet numbers per wallet (e.g. `jaib: {YER: "…"}`, `kuraimi: {YER, USD}`). Its Flutter merchant app requests permission to read SMS and notifications to auto-verify customer transfers. Test mode has a 60-second countdown, and failures fall back to "manual WhatsApp support". — [thejulan/yemenpay](https://github.com/thejulan/yemenpay)
  - "Smart-financial-tracker" (2026) parses Jeeb (Jaib) notifications, with mFloos, ONE Cash, SabaCash and Floosak listed as "upcoming". — [shehab-go/Smart-financial-tracker](https://github.com/shehab-go/Smart-financial-tracker)
  - A Yemeni store builder's payment-integration help page lists PayPal, Stripe and MyFatoorah but names no Yemeni wallet. — [Matjari](https://matjari.online/%D8%B1%D8%A8%D8%B7-%D9%85%D8%AA%D8%AC%D8%B1%D9%8A-%D9%85%D8%B9-%D9%88%D8%B3%D8%A7%D8%A6%D9%84-%D8%A7%D9%84%D8%AF%D9%81%D8%B9/)

### Inferences
- **The common API shape is a two-step "initiate then confirm".** The merchant initiates with the buyer's phone number, the wallet sends an OTP to the buyer, and the merchant's checkout collects the OTP and submits it. This applies to Floosak, CashPay, SabaCash, Aden Cash and Al-Qutaibi. The platform therefore sits in the path of the buyer's authentication secrets: OTPs, CashPay purchase codes and Kuraimi PINs. That is a security and liability burden: it is effectively merchant-side credential collection.
- **Jawali's voucher model is the most "pull-free".** The buyer pre-commits funds into a voucher, and the seller redeems it. The voucher is created in the Jawali app; its exact UX (whether it is addressed to the merchant, and whether `receiverMobile` is the buyer's or merchant's number) is not documented in the client.
- **The informal pattern is likely the dominant reality for small sellers:** transfer to the seller's personal wallet number, then a screenshot or SMS. YemenPay's SMS-scraping design exists to automate exactly that.
- **None of these APIs is self-serve.** Credentials, client certificates, short codes and agreements come from the provider after a commercial onboarding. Several require a branch visit.

### Gaps
- No official developer documentation was found for any wallet. Kuraimi's "Supplier Integration Guide" and Floosak's PDF are referenced but not public.
- No API evidence was found for ONE Cash, Jaib, mFloos-as-wallet (distinct from the Kuraimi E-Pay API), Shamil Money, Mobile Money (CAC) or MEPS.
- It is unknown whether the community-client base URLs are still live. Most clients were last updated in 2023–2025, and Floosak's default is a staging host.
- No published merchant discount rates were found for any wallet.

## Do any wallets support refunds/reversals, status queries, or callbacks? What happens on timeouts?

### Takeaway
- **Refunds or reversals** exist in the API for Floosak (full or partial) and Kuraimi (reversal by the merchant reference). Operators also describe merchant-side refunds for Kuraimi Hasib points, Cash Pay and ONE Cash merchant apps.
- **Status queries** exist for CashPay (explicitly for timeouts), SabaCash, Aden Cash and, pre-redemption, Jawali.
- **No wallet** shows evidence of webhooks or callbacks to the merchant. The only server-to-server call into the merchant is Kuraimi's customer-verification call.
- **Timeout handling** relies on the merchant re-querying by its own unique request ID.

### Cited Findings
- **Floosak:** refund by `transaction_id` and a new `request_id`, with an amount that can be partial. — [floosak-payment-js README](https://github.com/Alsharie/floosak-payment-js); [floosak-payment README](https://github.com/Alsharie/floosak-payment) [community code]
- **Kuraimi E-Pay:** `ReversePayment` by `SCustID` and `REFNO`. — [kuraimiepay](https://github.com/Alsharie/kuraimiepay) [community code]
- **Kuraimi's own descriptions:**
  - The API service eases "financial reconciliation of purchase and refund operations". — [service 50](https://kuraimibank.com/ar/services/50)
  - Hasib-point merchants "can return transaction amounts to customers … for any reason". — [service 33](https://kuraimibank.com/ar/services/33) [primary]
- **Cash Pay:** merchant tools to "transfer, and refund money instantly". — [Cash Pay page](https://www.cash.com.ye/en/cash-pay-electronic-payment-service) [primary]. The community CashPay client has no refund endpoint. — [cash-payment](https://github.com/Alsharie/cash-payment)
- **CashPay status and timeouts:**
  - `OperationStatus` "is used to check the state of an operation (It is useful in cases of time out)".
  - Error 6013 covers "timeout cases".
  - Error 6008 says step 1 can expire before the OTP is confirmed.
  - Error 6018 rejects a "duplicated RequestId".

  — [cash-payment source](https://github.com/Alsharie/cash-payment/blob/master/src/Responses/Error/CashPayErrorCode.php)
- **SabaCash:** `checkAdjustmentByTransactionId`, and the confirmation step supports `approve` or `reject` on a pending adjustment. — [sabacash-payment](https://github.com/Alsharie/sabacash-payment)
- **Aden Cash:** a `Payment/checkOperation` status call. — [adenbank-payment](https://github.com/Alsharie/adenbank-payment)
- **Jawali:** `ECOMMERCEINQUIRY` returns the voucher `state` (e.g. `PENDING`) before cash-out. The client retries on HTTP 400/401 (token refresh), with a default timeout of 30s and 2 attempts. No post-cash-out status or refund call exists. — [jawali-payment](https://github.com/Alsharie/jawali-payment)
- **Kuraimi's reverse API:** the bank calls the supplier's "Verify Customer details API" to verify customers. This is identity verification, not a payment-result callback. — [kuraimiepay README](https://github.com/Alsharie/kuraimiepay)
- **ONE Cash merchant app:** lists "refunds" as a merchant feature. — [Google Play com.one.oneagent](https://play.google.com/store/apps/details?id=com.one.oneagent&hl=en_US) (search summary)
- **Regulatory complaint handling (CBY-Aden, non-bank issuers):**
  - The issuer must set procedures "regarding resolution of disputes that may arise between it and related parties".
  - Complaints must be processed within 10 working days of notification, with a complaints register, and unresolved complaints may be referred to the CBY.
  - Customers must receive instant SMS or other notification of every transaction.
  - Fee changes require 2 weeks' notice to users and 14 days' notice to the CBY.

  — [CBY-Aden instructions 2023, sections 17 and 18 (consumer protection, fees, complaints)](https://www.cby-ye.com/files/64dde85e0a84f.pdf) [primary]
- **Jawali Terms:** the company may "settle any amount credited to the customer's account by mistake", which "must be returned to the party that deposited it". Complaints go through toll-free 8000444, 24 hours a day. No resolution deadline and no timeout clause appear; liability for telecom failures is carved out. — [Jawali Terms](https://jawali.com.ye/Terms/) [primary]

### Inferences
- **Recommended timeout pattern** (a design consequence, not a provider statement):
  1. Generate a unique merchant request ID: CashPay `RequestID`, Floosak `request_id`, Kuraimi `REFNO`, Aden `refNo`/`msgID` or Jawali `refId`.
  2. Persist it before calling.
  3. On timeout, call the status endpoint (CashPay, SabaCash, Aden Cash). Where none exists (Kuraimi, Floosak per the clients), call a reversal or refund by the same reference, or reconcile manually.
- **Idempotency** is enforced server-side at least by CashPay (6018 duplicate RequestId) and implied by Kuraimi's "must be unique" `REFNO`.
- **Without webhooks, a platform learns the outcome only from the synchronous confirm response** or by polling. Buyer-side "pay inside the wallet app" flows, such as Kuraimi store activation or Jawali voucher creation, have no push back to the platform. So the platform must drive the final confirm or redeem call itself.
- **Disputes are bilateral** between buyer and wallet issuer. No chargeback-like scheme exists; a seller refund is a voluntary merchant action.

### Gaps
- No documented chargeback or dispute timeline specific to merchant purchases was found for any wallet.
- It was not confirmed whether CashPay, Jawali or SabaCash expose refund APIs beyond the community clients.
- No documented OTP or confirm-window durations were found, other than CashPay's "step-1 expired" error.

## Can a platform hold a master merchant account and pay out to sub-merchants, or must each seller have its own merchant account?

### Takeaway
No wallet publicly offers a marketplace or sub-merchant (split-payment) product.
- Every API surfaced authenticates one merchant identity, and settles into that merchant's own wallet (Cash, Floosak, Jawali) or bank account (Kuraimi).
- **Technical integrator per seller:** possible only where each seller completes the wallet's manual merchant onboarding (wallet or bank account, agreement, often a branch visit).
- **Single master account:** makes the platform the holder of funds, paying sellers by wallet transfer or bulk disbursement. That raises licensing exposure under CBY rules and runs into account limits.

### Cited Findings
- **Single-merchant credentials:**
  - Floosak authenticates the merchant phone and short code, and debits into `source_wallet_id` (the merchant's own wallet). — [floosak-payment-js types](https://github.com/Alsharie/floosak-payment-js)
  - CashPay uses one `SpId`, `UserName` and client certificate per service provider. — [cash-payment](https://github.com/Alsharie/cash-payment)
  - Jawali uses one `orgID` and one agent wallet and password. — [jawali-payment](https://github.com/Alsharie/jawali-payment)
  - SabaCash uses one username and password, with a `beneficiary.terminal` field. — [sabacash-payment](https://github.com/Alsharie/sabacash-payment)
- **Possible per-request payee fields** (unverified semantics):
  - Al-Qutaibi `payment_DestNation` can be set per request. — [AlQutaibiBank-payment](https://github.com/Alsharie/AlQutaibiBank-payment)
  - Aden Cash sends `MrchntID` and `MrchntUser` per request. — [adenbank-payment](https://github.com/Alsharie/adenbank-payment)
  - Kuraimi sends a free-text `MRCHNTNAME` per payment. — [kuraimiepay](https://github.com/Alsharie/kuraimiepay)
- **Kuraimi's API service:**
  - Requires "an application or e-shopping site" and "an account in the company's name at the bank".
  - Offers "an independent account for e-payment operations for each region".
  - Funds reach "your business accounts directly" at order time.
  - Buyers activate each "store or app" from a list inside the bank app.

  — [Kuraimi services 50 and 32](https://kuraimibank.com/ar/services/50) [primary]
- **Cash Pay** settles into the merchant's own Cash wallet. **Cash** also offers bulk "Salaries Disbursement" and branch-level sub-tracking for companies. — [Cash Pay](https://www.cash.com.ye/en/cash-pay-electronic-payment-service); [Cash merchants](https://www.cash.com.ye/en/companies-merchants-features) [primary]
- **Jawali** advertises "collective payments such as salaries and benefits". — [jawali.com.ye](https://jawali.com.ye/en/about)
- **CBY-Aden licensing:**
  - The instructions build on separate "instructions regulating payment service providers and/or payment system operators" (21 September 2022).
  - A payment service provider must be licensed by the CBY.
  - Anyone providing mobile e-money services without a license faces enforcement action, and the CBY "bears no responsibility" for their obligations.
  - Limits for legal-entity accounts are issuer-set with CBY written approval.

  — [CBY-Aden instructions 2023](https://www.cby-ye.com/files/64dde85e0a84f.pdf); [Decision 4/2025](https://www.cby-ye.com/files/6875fc55a253e.pdf) [primary]
- **Aden's June 2024 decision** bars internal cash transfers except through licensed wallets and payment service providers within limits (search summary). — [CBY-Aden news/706](https://cby-ye.com/news/706)

### Inferences

**Rail summary (synthesis of the cited findings above; positions are inferences)**

| Dimension | Wallet rail in Yemen (2026) |
|---|---|
| **Who acquires the buyer's proof** | The merchant or platform checkout collects it. It is the buyer's phone plus an OTP (Floosak, CashPay, SabaCash, Aden Cash, Al-Qutaibi), the CashPay "Online Purchase Code", a Kuraimi 4-digit PIN forwarded base64-encoded, or a Jawali voucher code. In-store, the buyer scans a merchant QR or enters a merchant code in their own app (Jaib, Shamil, Hasib points, MEPS). |
| **Who establishes the outcome, and how the platform learns it** | The wallet's core ledger decides. The platform learns from the synchronous confirm or redeem response, or by polling a status call (CashPay, SabaCash, Aden Cash). No webhooks were found. Informal sellers learn from SMS or notifications (YemenPay design). |
| **Reserve funds before taking them?** | No card-style authorize-then-capture. The nearest analogues are a Jawali voucher (the buyer's funds sit in a voucher in `PENDING` state until the merchant redeems it) and a SabaCash pending "adjustment" that can be approved or rejected. Init→confirm windows are short and expire (CashPay 6008). |
| **Reversal path** | API refund: Floosak (partial allowed). API reversal: Kuraimi (by REFNO). Merchant-app refunds: Kuraimi Hasib points, Cash Pay, ONE Cash merchant app. Otherwise the merchant sends a manual P2P transfer back. No chargeback scheme. |
| **Who holds the money, and how it reaches the seller** | The e-money issuer's pooled trust account at a settlement bank (100% backed; owned by holders under CBY-Aden rules). The merchant is credited instantly in its own wallet (Cash, Floosak, Jawali agent wallet) or Kuraimi bank account. Cash-out is via agents or exchange networks, or by transfer to a bank. |
| **Platform position 1: integrator on the seller's own merchant account** | Technically feasible for CashPay, Floosak, SabaCash, Jawali, Aden Cash and Al-Qutaibi: store each seller's credentials or certificates. Onboarding friction is high: per-seller agreements, branch visits, tech-support-led integration. Kuraimi's model expects the platform (app/site) to be the listed "store", so per-seller listing is impractical. |
| **Platform position 2: aggregator under a master merchant** | No sub-merchant, split or payout-to-sub-merchant API was found. Only per-request payee fields of unknown meaning exist (Al-Qutaibi `payment_DestNation`, Aden `MrchntID`). It would need a bespoke commercial agreement with each wallet. |
| **Platform position 3: holder of funds** | Feasible mechanically with one merchant account per wallet and payouts via wallet transfers or bulk disbursement. Under CBY-Aden rules this resembles unlicensed payment services. It is also constrained by legal-entity limits (issuer-set, CBY-approved) and by individual-seller limits (e.g. YER 1M per transaction and YER 8M maximum balance for non-bank wallets in Aden's zone). |
| **Currency coverage** | YER is the default everywhere. USD and SAR are possible: CashPay currency IDs 4 and 5, Kuraimi multi-currency, and Aden-zone non-bank issuers allowed USD/SAR/AED since July 2025 without local-to-foreign conversion. The "same" YER differs about 3x by zone: about 533 old-note YER/USD in Sana'a vs about 1,565 new-note YER/USD in Aden on 8 September 2026 (unofficial). — [ACAPS YETI](https://yemen.yeti.acaps.org/xr-commodities/) |
| **Territorial coverage** | Sana'a-licensed wallets (Jawali, Cash, Floosak, Jaib, SabaCash, Mobile Money, Yemen Wallet, Al-Dawli) are banned for Aden-regulated institutions. Kuraimi is blocked for exchanger dealings in Sana'a since June 2025. ONE Cash is the candidate for both zones (unverified). Kuraimi's "account per region" suggests separate old-rial and new-rial settlement (inference). |
| **Cost** | No public merchant discount rates were found. Floosak responses carry `fee`, `net`, `gross` and `rate`. Shamil agent cash-out starts at YER 100. Integration means bespoke development per wallet. |
| **Risk** | Political and regulatory bifurcation. OFAC exposure (YKB, Jan 2025; IBY, Apr 2025; Houthi FTO, Mar 2025). Weak API security in clients (MD5 tokens, a bare-IP endpoint with an SSL-disable option, a zero-IV AES). The platform handling buyer PINs and OTPs. No webhooks. Low buyer adoption (98.9% made no digital merchant payment in 2021). Reliability complaints (anecdotal Play reviews). |

- **Most viable near-term setup option** (inference): treat each wallet as a "seller's own merchant account" integration for the few sellers able to onboard (CashPay, Floosak, Jawali, Kuraimi), plus a no-API "pay to seller's wallet number and verify" option for the long tail. Holding funds as a master merchant is the riskiest legally, given both central banks' licensing stance.

### Gaps
- No wallet's merchant agreement, onboarding checklist (beyond Kuraimi's and Cash's short lists) or settlement timetable to a bank account was found.
- No confirmation that any wallet permits marketplace or aggregator models. Wallets would have to be asked directly, which is out of scope here.
- No text of CBY-Aden's 2022 payment service provider instructions or of CBY-Sana'a Decision 1/2020 was read; their aggregator and agent provisions are unknown.

## Are wallets interoperable, and can a buyer on wallet A pay a seller on wallet B?

### Takeaway
- **Sana'a zone:** partial interoperability exists through WeNet, the HSA-owned switch, which is also called the national switch. ONE Cash and Jaib now route transfers and merchant payments over it. Cash offers "transfer to bank accounts or other wallets".
- **Aden zone:** no operating wallet switch was found. A World Bank-funded Fast Payment System and RTGS were approved in June 2025 and are not yet reported live.
- **Across zones:** cross-zone interop is blocked by both central banks.
- **For e-commerce:** wallet-A-buyer to wallet-B-seller checkout is not an established product. It happens, if at all, as a P2P inter-wallet transfer that the seller verifies manually.

### Cited Findings
- **WeNet's origins:**
  - WeNet is the brand of Yemen Financial Services Company (YFSC), registered in 2006 by 11 banks. HSA's Murooj acquired 25% in 2017.
  - In September 2020 WeNet launched an Instant Transfer Scheme (ITS) with six banks: YBRD, YKB, SBYB, Saba Islamic, Islamic Bank of Yemen and CAC. It covered wallet-to-wallet, bank-to-wallet and wallet-to-bank transfers.
  - As of 2022 it had "limited market acceptance", was restricted to Houthi-controlled areas, and did not then allow transfers from wallet-based accounts. WeNet was reportedly licensed by CBY-Sana'a to run the switch.

  — [Sana'a Center 2022](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- **WeNet's platform:** BPC describes WeNet as "Yemen's national financial switch interbank network", founded in 2006 by 12 banks and "approved by the Central Bank of Yemen". It uses BPC SmartVista for the ITS and for a card national switch. — [BPC case study](https://www.bpcbt.com/case-study-wenet). The first phase went live at the end of August 2020 with 6 banks (CTO letter cited in the BPC PDF, via search summary). — [BPC PDF](https://www.bpcbt.com/hubfs/22/case-studies/BPC_case-study-WeNet.pdf)
- **WeNet in wallet apps (2025–26):**
  - ONE Cash lists transfers to "any bank account linked to WeNet" or to any e-wallet. Version 1.5.1 (dated 22 May, year not shown; after a 13 July 2025 version, so likely 2026) added "a merchant payment service via WeNet". — [ONE Cash App Store](https://apps.apple.com/us/app/id1661455867)
  - Jaib lists "WeNet" for merchant transfers. — [Jaib App Store](https://apps.apple.com/us/app/id6472856710)
- **Other inter-wallet links:**
  - Cash advertises "Transfer to Bank Accounts or other Wallets" and cash-out at "more than 1500 points" and ATMs. — [cash.com.ye](https://www.cash.com.ye/en/transfer-to-bank-accounts-or-other-wallets)
  - ONE Cash's marketing (via search summary) says users can transfer to Jawali, Floosak and Mahfathati wallets and to several banks; this was not verified on a primary page. — [ONE Cash Play listing](https://play.google.com/store/apps/details?id=com.one.onecustomer)
  - Floosak supports transfers via the "Floosak Network and Akwa Money Network". — [Floosak Play](https://play.google.com/store/apps/details?id=co.ysys.floosak&gl=US)
  - Jawali and Jaib integrate exchange-company networks (Al-Najm, Al-Imtiaz, Yemen Express, Al-Akwa and others) for cash-in and cash-out. — [Jawali](https://jawali.com.ye/en/about); [Jaib](https://apps.apple.com/us/app/id6472856710)
- **Aden-zone rules:**
  - The CBY-Aden instructions define interoperability as "physical linking among payment service providers enabling them to exchange funds". They require that "when an interoperability system is available, the system must be capable of interconnection with other e-money issuers".
  - Issuers must report monthly on "interoperable (off-us) transactions" and "payments from individual to merchant".

  — [CBY-Aden instructions 2023](https://www.cby-ye.com/files/64dde85e0a84f.pdf) [primary]
- **Aden-zone infrastructure:**
  - The World Bank's Yemen Financial Market Infrastructure and Inclusion Project (US$20M grant, approved 17 June 2025, implemented by UNDP) funds a Fast Payment System and RTGS "under the Central Bank in Aden" and interoperability among financial institutions. — [World Bank, 17 June 2025](https://www.worldbank.org/en/news/press-release/2025/06/17/world-bank-approves-us-30-million-to-support-financial-inclusion-and-education-in-yemen)
  - "Yemen lacks comprehensive national payments infrastructure … Houthi-controlled areas have separate payment infrastructure." Fragmentation "continues to undermine interoperability" (citing a Sana'a Center 2026 review secondhand). — [Fintech Times, 10 Sept 2026](https://thefintechtimes.com/yemen-can-fintech-connect-an-economy-divided-by-war/)
- **Cross-zone legal barriers:** Aden's June 2024 ban on dealing with 12 Sana'a wallets. — [Yemen Eco](https://yemeneco.org/archives/84396). Sana'a's June 2025 suspension of dealings with Kuraimi. — [Alnkkar](https://www.alnkkar.com/news25084.html)
- **Practice:** a 2026 multi-wallet "gateway" works by publishing a seller's account number on each wallet (Jaib, Jawaly, Kuraimi, Cash, OneCash, Yemen Wallet). The buyer pays on the wallet they hold, and the seller's phone parses SMS and notifications. — [thejulan/yemenpay](https://github.com/thejulan/yemenpay)

### Inferences
- **In Sana'a's zone, a WeNet-routed P2P or "merchant transfer" can move money between wallets.** ONE Cash, Jaib and probably others participate; this is evidenced by app changelogs, not by a published participant list. But no merchant-checkout API that accepts payments from other wallets was found. A seller wanting buyers on several wallets must hold an account on each, or accept inter-wallet transfers and reconcile manually.
- **In Aden's zone,** interop depends on the not-yet-live Fast Payment System. Until then a seller needs one account per wallet: Kuraimi/mFloos, Shamil Money, Aden Cash, ONE Cash if permitted, and so on.
- **A platform serving both zones would run two separate wallet stacks,** with different rial values and different legal counterparties.

### Gaps
- No current WeNet participant list or merchant-payment specification was found. The beta.wenet-ye.com site returned 503.
- No evidence was found on whether WeNet merchant payments carry a merchant ID or QR standard (e.g. a national QR).
- No information was found on any Aden-side wallet interop arrangement in 2026, or on the status of the World Bank Fast Payment System build.
