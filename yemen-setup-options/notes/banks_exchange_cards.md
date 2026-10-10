# Yemen non-wallet payment rails for online commerce: banks, money-exchange and remittance networks, cards, foreign processors, crypto

Research date: 9 October 2026. Scope: every non-wallet electronic or institutional rail a buyer could use to pay a seller in Yemen, judged as a SETUP OPTION for a Shopify-class platform (Sharrwah). Wallets (Jawali, Jaib, Floosak, ONE Cash, etc.) are covered by another researcher and appear here only where a bank or exchange rail touches them.

How to read these notes:
- Every line under "Cited Findings" has a source. Where I could not read the primary page (PDF dumps, 403s), the line says it came from a search-result summary and should be treated as weaker.
- "Inferences" are my reasoning, not verified fact. That includes the setup-option records, the per-rail tables required by the brief.
- Background that applies to every rail: Yemen has two central banks, CBY-Aden (internationally recognized) and CBY-Sana'a (Houthi). It also has two rial note series with very different values: "old" notes in the Houthi north, roughly YER 530–540/USD in 2024–25, and "new" notes in the government south, roughly YER 1,800–1,900/USD in 2024 and up to YER 3,000/USD in 2025. In addition, SAR and USD circulate widely. Because of this split, the currency and the territory together define every rail.

---

## Q1. How do Yemeni banks support payments today? (accounts, transfers, mobile apps, APIs/corporate integration, virtual accounts or payment references, which banks are large and where they operate)

### Takeaway
Banks reach only a small minority of Yemenis: about 4.8% of adults hold deposits, and account ownership of any kind, wallets included, is about 9%. There is still no interbank instant-payment system. CBY-Aden approved a fast payment system (FPS) operator company and a mandatory national QR standard in March 2026, but these are not yet live. In practice, "bank payment" today means one of two things:
- an intra-bank transfer inside one large bank's app, mostly Al-Kuraimi (KJ / Mfloos), Tadhamon and a few others;
- a bank-run merchant API. Kuraimi's "E-Payment" API, in which a buyer approves a payment from the Kuraimi app, is the clearest example of a payment-reference integration a platform could plug into.

The 2024–2025 sanctions shocks were the OFAC designations of Yemen Kuwait Bank (YKB) and International Bank of Yemen (IBY), the March 2025 US designation of the Houthis as a Foreign Terrorist Organization (FTO), and the forced relocation of bank headquarters to Aden. Together they make a bank's reliability depend on which authority it answers to.

### Cited Findings

**Scale of banking / inclusion**
- "The population is almost entirely unbanked, including about 90% of men and 99% of women. Just 1.6 percent of adults borrow from formal financial institutions, while 4.8 percent have deposits... Only 6.3 percent of adults have access to financial service points, and there are just 1.6 bank branches per 100,000 adults." Formal banking is "largely restricted to major cities, while rural and remote areas are mainly served by money exchangers." — [World Bank, Yemen Financial Sector Diagnostic (Dec 2024)](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- Findex account ownership rose from 3.7% (2011) to 6.4% (2014). A 2022 study (SMEPS, 2023) found that about 8.8% of the population owned an account of any type, including e-wallets. The World Bank says inclusion "likely worsened during the conflict." — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- In 2014, 94% of adults had no financial account. By 2019, 3 million Yemenis (10% of the population) held at least one account, 27% of them e-money accounts. Only 2% of women held an account. Between 2015 and 2016 the number of open accounts fell 40%, to about 2.4 million accounts held by 1.5 million people. — [Sana'a Center, "Challenges and Prospects for Electronic Money and Payment Systems in Yemen" (Mar 2022)](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- Firms: in 2022, 59% of formal firms used exchange companies as their main financial intermediary and only 20% used commercial banks. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)

**Which banks exist and which are large**
- The CBY-Aden list reproduced by the World Bank names 29 banks:
  - State-owned commercial banks: Yemen Bank for Reconstruction and Development, National Bank of Yemen (NBY), CAC Bank.
  - Private commercial banks: Yemen Kuwait Bank, (Yemen) International Bank, Yemen Commercial Bank, Yemen Gulf Bank, Hadramout Commercial Bank (2022), First Aden Islamic Bank (2024).
  - Islamic banks: Tadhamon, Saba Islamic, Yemeni Islamic Bank, Shamil Bank of Yemen & Bahrain (SBYB), Al-Kuraimi Islamic Bank.
  - Foreign banks: UBL, Arab Bank, Rafidain, QNB.
  - Microfinance banks: Al-Amal, Al-Kuraimi Islamic Microfinance, Al-Qutaibi, Aden MF, Al-Busairi, Alinma MF, **Bin Dowal Islamic Microfinance (2022)**, Shamoul, Sharq Yemen, Al-Qasemi, Tamkeen. — [World Bank FSD 2024, Table 2](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- The World Bank's stress test used "seven of the ten largest commercial banks": IBY, Tadhamon, CAC, NBY, Kuraimi Islamic Microfinance Bank, YKB and Yemen Commercial Bank. It names IBY, CAC and NBY among "the country's largest banks." Tadhamon "remains one of Yemen's largest banks" (37 branches, largest shareholder the Hayel Saeed Anam Group). Al-Kuraimi is the second-largest microfinance institution. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- Some large money exchangers have turned into banks. Al-Kuraimi and Al-Qutaibi became microfinance Islamic banks, and Bin Dowal was finalizing a microfinance bank licence. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)

**Interbank infrastructure / instant payments**
- CBY-Aden payment-systems work since 2019 has included a payment systems department and "SWIFT activation for near-same-day settlements." An automated clearing house (ACH) and a real-time clearing system (RTCS) were still "proposals... pending financing" (as of the 2024 report). Yemen joined the Arab Monetary Fund's Buna cross-border platform. Three Aden commercial banks offered e-wallets as of Dec 2023. — [World Bank FSD 2024, Box 11](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- By Dec 2023, most banks in Sana'a and Aden were connected to Swiftscope, which lets the central bank monitor banks' transactions. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- On 10 July 2025, CBY-Aden met all banks to discuss setting up an instant-payment company ("شركة الدفع الفوري") with "direct World Bank support." The same meeting discussed restructuring the Unified Network company, raising its capital and handing its management "fully to the banking sector." — [Belqees, 10 Jul 2025](https://belqees.net/locals/%D8%A7%D9%84%D9%85%D8%B1%D9%83%D8%B2%D9%8A-%D9%81%D9%8A-%D8%B9%D8%AF%D9%86-%D9%8A%D8%AC%D8%AA%D9%85%D8%B9-%D8%A8%D9%85%D9%85%D8%AB%D9%84%D9%8A-%D8%A7%D9%84%D8%A8%D9%86%D9%88%D9%83-%D8%A7%D9%84%D9%8A%D9%85%D9%86%D9%8A%D8%A9-%D9%84%D8%A8%D8%AD%D8%AB-%D8%AA%D8%A7%D8%B3%D9%8A%D8%B3-%D8%B4%D8%B1%D9%83%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A7%D9%84%D9%81%D9%88%D8%B1%D9%8A-%D9%88%D8%A7%D8%B9%D8%A7%D8%AF%D8%A9-%D9%87%D9%8A%D9%83%D9%84%D8%A9-%D8%A7%D9%84%D8%B4%D8%A8%D9%83%D8%A9-%D8%A7%D9%84%D9%85%D9%88%D8%AD%D8%AF%D8%A9)
- On 29 March 2026, the CBY-Aden board made three decisions:
  - the central bank becomes "a principal shareholder in the Fast Payment System (FPS) operator company";
  - "a unified, binding national standard for QR Code service for all financial institutions" was adopted;
  - linking of e-wallets through unified connection routes was approved.

  No go-live date was given. — [CBY-Aden news/922 (29 Mar 2026)](https://cby-ye.com/news/922)
- A national switch has existed on paper since before the war. The CBY supported 11 banks in founding the Yemen Financial Services Company (YFSC) to run a "National Financial Switch Interbank Network," and a 2014 CBY circular endorsed a bank-led e-money model. This comes from a search-result summary of the paper; I read the table of contents, which confirms a section "4.3 The National Financial Switch Interbank Network," but not the section text. — [Sana'a Center (Mar 2022)](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)

**Bank apps and merchant APIs (payment references)**
- Kuraimi "E-Payment" gateway. A third-party open-source package describes "a Web API integration" that facilitates "transactions between domestic e-commerce suppliers and the Kuraimi bank applications, namely KJ and Mfloos." Configuration is a bank-issued username and password plus a base URL. A `KURAIMI_CURRENCY_ZONE` setting takes `old` ("North Yemen Coin"), `new` ("South Yemen Coin") or `all`. The merchant hosts a webhook at a default path of `webhooks/kuraimibank/check-user`, and customers are matched by the `mobile` column. — [Packagist: al-saloul/kuraimibank-payment](https://root.packagist.org/packages/al-saloul/kuraimibank-payment); [GitHub README](https://github.com/al-saloul/kurimibanck)
- A second third-party SDK (npm `@alsharie/kuraimiepay`), per its search-result description:
  - it supports "E-Payment and reversal transactions," uses Basic Authentication, Base64-encodes the customer PIN, and supports UAT and production environments;
  - the merchant "MUST expose a 'Verify Customer details API'" that Kuraimi calls, or "subsequent E-Payment transactions initiated via Kuraimi Bank's applications (KJ, Mfloos)" fail.

  I could not open the page (403), so this is a snippet. — [Yarn: @alsharie/kuraimiepay](https://classic.yarnpkg.com/en/package/@alsharie/kuraimiepay)
- An app-store aggregator lists a new Alkuraimi Islamic Bank app (first released 11 Aug 2025) offering "instant money transfers" and real-time statements. This came from a search summary of an aggregator listing (weak). — [mwm.ai listing](https://mwm.ai/apps/ki-bank-app/6748606298)
- A Yemeni developer said in Jan 2023 that his team had "integrated the Al Amal bank API and the Cash Pay bank API" for e-commerce. This is an unverified forum comment. — [WooCommerce feature request](https://woocommerce.com/feature-request/we-need-paymen-in-yemen-we-have-a-huge-market-of-e-commerce-here-and-we-need-this-feature/)
- Bank-led e-money licences (CBY, 2015–2019) went to Al-Kuraimi Islamic Microfinance Bank, Tadhamon, Al-Amal Microfinance Bank and YKB. CBY-Sana'a licensed CAC Bank, and in Jan 2021 also SBYB and IBY. — [Sana'a Center (Mar 2022)](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- A Yemeni e-commerce blog names Floosak, founded in 2016 by "Yemen Kuwait Bank," which works by mobile number without a bank account, and a "Pyes" service from Al-Amal Microfinance Bank. This is a search snippet of a commercial blog (weak). — [Fatora blog](https://fatora.io/blog/online-payment-in-yemen/)

**Sanctions, relocation and split-authority disruptions (bank reliability)**
- April 2024: CBY-Aden ordered all banks to move their headquarters from Sana'a to Aden within 60 days (Decision 17 of 2024). — [SEMC policy paper (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- On 3 July 2024, CBY-Aden revoked the licences of six Sana'a-headquartered banks: Tadhamon, YKB, SBYB, Al-Amal Microfinance, Al-Kuraimi Islamic Microfinance and IBY. The Houthi Money Changers Syndicate suspended dealings with CBY-Aden-controlled exchange networks. — [Sana'a Center, Yemen Review Jul–Sep 2024](https://sanaacenter.org/the-yemen-review/july-sept-2024/23500)
- On 23 July 2024, a UN-announced, Saudi-brokered deal had both sides cancel "all the recent decisions and procedures against banks... and refrain[] in the future from any similar decisions." The Houthis had banned dealings with 13 Aden banks in retaliation. — [Gulf News, 23 Jul 2024](https://gulfnews.com/world/gulf/yemen/al-houthis-yemen-govt-reach-financial-de-escalation-deal-un-envoy-1.103583412); [The New Arab](https://www.newarab.com/news/houthis-yemeni-government-reach-financial-de-escalation-deal)
- On 17 Jan 2025, OFAC designated Yemen Kuwait Bank for supporting the Houthis, with a wind-down general licence to 16 Feb 2025. — [Willkie Compliance Concourse](https://complianceconcourse.willkie.com/articles/united-states-sanctions-yemen-kuwait-bank-for-supporting-the-houthis/); [Treasury release via GlobalSecurity](https://www.globalsecurity.org/military/library/news/2025/01/mil-250117-treasury02.htm)
- On 17 Apr 2025, OFAC designated the International Bank of Yemen (Sana'a) and three senior officials for giving the Houthis SWIFT access and other support. — [US Treasury sb0092](https://home.treasury.gov/news/press-releases/sb0092)
- On 4 Mar 2025, the US designated the Houthis a Foreign Terrorist Organization, and Sana'a banks began moving their headquarters to Aden. — [Barran Press, 14 Mar 2025](https://en.barran.press/news/6377); [Xinhua, 15 Mar 2025](https://english.news.cn/20250315/312bd698021244cc9ec3e80617c17f35/c.html)
- Eight banks notified CBY-Aden of relocation, including Tadhamon, Yemen Commercial Bank and Saba Islamic Bank. — [South24](https://south24.net/news/newse.php?nid=4542)
- By late 2025, "all major banks and leading exchange companies" had moved their headquarters to Aden, "making the Yemeni banking sector fully operational from Aden, according to the Governor of Aden-CBY." — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- Correspondent banks follow CBY-Aden directives and "requested proof of relocation" from institutions wanting to keep international transactions. — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- Earlier deposit freezes: CBY-Aden and CBY-Sana'a set conflicting withdrawal rules (CBY-Sana'a allowed withdrawals only on deposits accumulated since 2017), which "de facto froze most cash deposits made before" the split. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)

### Inferences

- There is no evidence of virtual accounts or reference-based reconciliation products, such as unique deposit references per order, at any Yemeni bank. For a platform, the bank-transfer rail therefore means either (a) manual matching of transfers into a merchant or platform account against screenshots or reference numbers, or (b) a bank-specific API such as Kuraimi E-Pay.
- Kuraimi is the natural first bank partner. It is a former exchange company with a very large branch and agent footprint, it has a documented merchant API in which the buyer approves inside the bank app, and it explicitly supports both currency zones (old north / new south).
- Bank reliability now depends on the institution's sanctions and authority status:
  - YKB and IBY are OFAC SDNs. A platform with any US nexus, or one that needs international processors, should not route through them.
  - Banks that relocated to Aden have correspondent access, but their branches in the Houthi north face pressure from CBY-Sana'a. The July 2024 truce shows that either authority can suspend dealings with short notice.
- The FPS and national QR standard approved in March 2026 could become a real interbank instant rail. It is not yet live, so a platform should design for it as a future option, not a launch dependency.

#### Setup option B1: Intra-bank / mobile-banking transfer into a merchant (or platform) bank account, manually reconciled
| Dimension | Record |
|---|---|
| Buyer proof | Buyer sends from the bank app (or a branch) and shares a screenshot or transaction number. Inference. |
| Who establishes outcome / how platform learns | The bank. The account holder learns from the app or SMS or the statement. There is no evidence of push notifications or statement APIs. The platform learns only through the seller, or through its own account if it is the payee. Inference. |
| Reserve before take | No. A transfer is final once sent. Inference. |
| Reversal / dispute | Through the bank only, and only by agreement between the parties. No chargeback scheme. Inference. |
| Who holds money / how long | The payee bank account holds it immediately on an intra-bank transfer. Inference. |
| How money reaches seller | Directly, if the seller is the payee. If the platform is the payee, the platform must pay out, which raises licensing questions. Inference. |
| Platform position | Software only (seller's own account, platform reconciles); or collecting intermediary (platform account), which likely needs a CBY payment-services licence or a partner bank. Inference. |
| Licence / partner | None if seller-to-buyer direct. If the platform collects, CBY-Aden regulates payment services for banks and non-banks ([World Bank FSD 2024, Box 11](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)). |
| Currency / territory | Bank-dependent. Rials are split into old (north) and new (south) zones (see Kuraimi config above). USD and SAR accounts are common. |
| Cost / limits / settlement time | Not found. Intra-bank is likely near-instant. Inter-bank goes through CBY/SWIFT "near-same-day" ([World Bank FSD](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)). |
| Risks | Fake screenshots. Only about 5–9% of buyers hold accounts. Sanctions on specific banks (YKB, IBY). Authority split (north/south suspensions). |

#### Setup option B2: Bank merchant API, "pay from your bank app" (Kuraimi E-Pay via KJ / Mfloos; possibly Al-Amal / CashPay)
| Dimension | Record |
|---|---|
| Buyer proof | Buyer identifies by mobile number and authorizes with a PIN generated in or entered through the Kuraimi app. Per the SDK description, the PIN is Base64-encoded in the API call ([Yarn SDK](https://classic.yarnpkg.com/en/package/@alsharie/kuraimiepay)). |
| Who establishes outcome / how platform learns | The bank, through a synchronous API response. The merchant also hosts a "Verify Customer details" endpoint that Kuraimi calls ([Packagist](https://root.packagist.org/packages/al-saloul/kuraimibank-payment)). |
| Reserve before take | No evidence of an authorize/capture split. The flow appears to be an immediate debit. Inference. |
| Reversal / dispute | The API supports "reversal transactions" ([Yarn SDK](https://classic.yarnpkg.com/en/package/@alsharie/kuraimiepay)). No time window is documented. There is no consumer dispute scheme. |
| Who holds money / how long | Credited to the merchant's Kuraimi account. Inference: the merchant must hold an account at Kuraimi. |
| How money reaches seller | If the platform is the API merchant, the platform pays sellers out by transfer or UNMoney. If each seller has its own credentials, it is direct. Inference. |
| Platform position | Technical integrator for sellers who each hold Kuraimi merchant credentials (lowest licence burden); or master merchant / aggregator (needs bank agreement and probably CBY approval). Inference. |
| Licence / partner | Contract with Kuraimi (credentials are bank-issued). Kuraimi's licence and HQ status are post-2025 Aden relocation; it was in the July 2024 revoked-then-reinstated six ([Sana'a Center](https://sanaacenter.org/the-yemen-review/july-sept-2024/23500)). |
| Currency / territory | "old" (north), "new" (south) or "all" zones ([GitHub README](https://github.com/al-saloul/kurimibanck)). Whether SAR or USD are supported was not found. |
| Cost / limits / settlement | Not found. |
| Risks | Single-bank coverage (only Kuraimi customers). Undocumented SLA. The documentation is third-party, not official. The bank could be caught in north/south escalation. |

### Gaps
- No official Kuraimi E-Pay documentation, fees, limits, settlement terms or onboarding criteria found. kuraimibank.com did not surface in search. The same goes for Tadhamon, SBYB (Shamil Money), CAC, YKB and Al-Amal merchant APIs.
- No source on whether any bank offers virtual accounts, payment references, corporate host-to-host or statement APIs.
- No current (2025–26) customer/account totals per bank. No ranking of banks by assets beyond the World Bank's qualitative "largest" list.
- The status of YFSC / the national switch after 2015 is unknown. MEPS Yemen mentions ATM and POS management but no switch (see Q3). The relationship between the planned FPS company and the existing switch is unclear.
- How Sana'a-area branches of relocated banks operate in 2026 (accounts, transfers in old rials) was not found. The Barran (Mar 2025) article does not say.
- No Global Findex 2025 figure for Yemen found. Yemen appears to be absent from recent Findex rounds; the latest is 2014.

---

## Q2. How do exchange companies and remittance networks work for domestic payments, what do they cost, and could a platform use them to collect from buyers or pay sellers?

### Takeaway
Exchange companies, not banks, are Yemen's real domestic payment network. They hold most cash outside banks, serve far more people than banks do, and are the main intermediary for most firms. Since June 2024, CBY-Aden has required that all domestic cash transfers by exchange companies run through a single network, the Unified Money Network (UNMONEY / الشبكة الموحدة للأموال). It says the network consolidated 22 previous transfer networks, carried more than YER 251 billion in 2024, and now includes all banks and e-wallets. UNMONEY was restructured in July 2026 so that banks are shareholders.

A transfer of this kind ("حوالة") is a code-based, cash-in / cash-out instrument. In principle a platform could:
- collect from buyers as a named beneficiary, or
- pay sellers by sending them transfer codes.

However, there is no public API. Exchange companies are legally barred from opening accounts. Fees were not found. The north/south split (and Houthi refusal to deal with Aden networks) breaks the rail across the front line.

### Cited Findings

**Size and role**
- Money exchangers are "the primary destination for deposits and the main source of credit for traders," "serve a much larger share of the population than Yemeni banks," and "operate more extensive networks than banks." They hold 12–15% of banking-sector assets but 35–40% of its net foreign assets. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- 71% of communities rely on informal exchange outlets, and 64% use hawala as their primary way to transfer money rather than banks (citing the World Bank). — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- Counts of exchange businesses (citing the World Bank FSD):
  - By 2023, Aden had 332 licensed individual exchange outlets, 96 exchange companies and 86 money-transfer agents, and Sana'a had more than 170 licensed exchange companies.
  - Between 2014 and 2023, exchange companies grew from 179 to 415 in Sana'a and from 34 to 91 in Aden.
  - In 2018, about 800 of 1,350 outlets operated without a licence.

  — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- Legal limits: Law No. 19 of 1995 (Arts. 21–23) "prohibit exchange companies from performing banking functions such as commercial financial transfers, opening accounts, conducting credit and debit operations." The parallel market has nevertheless "surpassed them." — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- CBY-Aden prohibits non-bank institutions from accepting deposits and has pushed large exchangers either to obtain banking licences or to return deposits. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- CBY-Aden capital minimums (Decision 58 of 2022): YER 1 bn for exchange companies, YER 500 m for individual outlets, YER 100 m for remittance agents. — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)

**Named networks**
- "Most exchange companies engage in interregional transactions facilitated by remittance networks such as the Al-Najm and Al-Imtiaz networks." About 22 exchangers launched a joint network with CBY-Aden support to restore interoperability. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- Emtiaz Express is owned by Al-Montab Exchange, one of the 25 largest exchange companies, with assets of about YER 13.7 bn. A leaked 2023 list showed 1,927 unclaimed transfers, 60% of their value in YER, which "indicat[es] that most of the transfers were domestic." Networks then built name-search tools for unclaimed transfers, and CBY-Aden required reporting of unclaimed transfers after two months. — [World Bank FSD 2024, Box 7](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- One network reportedly held more than 60,000 uncollected transfers, worth nearly YER 2 bn and more than SAR 6 m (Al Jazeera, Feb 2023). — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- Al-Kuraimi and Al-Qutaibi are former exchangers that are now microfinance banks. Bin Dowal was converting into Bin Dowal Islamic Microfinance Bank, listed in 2022. Al-Amal is a microfinance bank (2008), not an exchange company. — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)

**Unified Money Network (UNMONEY)**
- Origin: CBY-Aden Decree No. 18 of 2020 (Nov 2020 resolution). UNMONEY was officially activated in Feb 2024 with initial capital of YER 5 bn. Capital was later raised to YER 12 bn as relocated banks joined (CBY statement, July 2025). — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf); [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- Decision No. 23 of 2024 (26 June 2024) did the following:
  - It halted "completely and permanently" the domestic transfer networks owned by banks and exchange companies.
  - It required new domestic cash transfers to go "through the unified network (UNMONEY)" and banned other domestic cash transfers.
  - Bank networks could run in parallel until 30 July 2024.
  - E-wallets and licensed PSPs were exempt within set caps.
  - Pending items had to be liquidated within 15 days and undelivered transfers reported within 20 days.
  - Penalties include licence withdrawal and fines.

  — [CBY-Aden news/706](https://cby-ye.com/news/706)
- Same day: CBY-Aden circular banning banks and exchanges from dealing with 12 unlicensed entities, wallets and e-payment services. — [CBY-Aden news/703](https://cby-ye.com/news/703)
- The Houthi response: CBY-Sana'a condemned the decree, and the Houthi Money Changers Syndicate suspended dealings with CBY-Aden-controlled exchange networks. — [Sana'a Center Yemen Review Jul–Sep 2024](https://sanaacenter.org/the-yemen-review/july-sept-2024/23500)
- A Barran Press article says the Houthis "restricted dealings with the unified network and required two currencies of differing sizes and values, which increased domestic transfer fees." The same article says there are "thousands" of transfer networks, mostly outside central-bank control. — [Barran Press (June 2024)](https://en.barran.press/news/3195)
- At the CBY-sponsored cashless expo in Aden on 22 Jan 2026, CBY said it had consolidated 22 cash transfer networks into one unified network, that more than YER 251 bn was transacted through it in 2024, and that "all banks and e-wallets have joined the network." — [CBY-Aden news/915 (22 Jan 2026)](https://cby-ye.com/news/915)
- On 27 July 2026, an extraordinary general assembly of the Unified Money Network Company approved a completed capital increase, a shareholder base widened to "the banks operating in Yemen," and a new nine-member board. CBY calls the company "a key pillar for developing the payments system." — [CBY-Aden news/957 (27 Jul 2026)](https://cby-ye.com/news/957)
- Feb 2025 measures reported in a search summary: CBY-Aden circulars halted FX buying and selling through digital platforms and apps, and required exchange companies to clear pending balances with UNMoney "or similar networks" within two weeks. I did not open the page, so this is a snippet. — [South24](https://south24.net/news/newse.php?nid=4503)
- 2024–2026 enforcement: there were repeated licence suspensions and closures of exchange companies and agents:
  - 11 companies in July 2024 ([Sana'a Center](https://sanaacenter.org/the-yemen-review/july-sept-2024/23500));
  - Governor's Decisions Nos. 14, 15, 17 and 18 (2026), listed on the CBY site ([CBY-Aden news/922 page listing](https://cby-ye.com/news/922));
  - "Suspends Licenses of 12... Bringing Total to 15" (search snippet only) ([Barran](https://en.barran.press/news/3291)).

**International remittance channel rules (relevant to diaspora → Yemen)**
- On 28 May 2024, CBY-Aden limited the receipt of international transfers to banks and exchange companies it has qualified, operating through Aden head offices and their branches. Sub-agents may serve under annual contracts. Remittances must be paid in the currency sent unless the beneficiary chooses otherwise. — [Asharq Al-Awsat, 28 May 2024](https://aawsat.com/node/5025163)

**Costs**
- No published domestic fee schedule for UNMONEY or any exchange company was found. Barran says fees rose because of the dual currency, without figures ([Barran](https://en.barran.press/news/3195)). Global transfer companies and hawala agents are said to have "relatively low fees and extensive networks" ([World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)).

### Inferences

- The domestic code-based transfer (حوالة) works like a quasi-escrow. Funds sit at the network between cash-in and cash-out, and the payout requires the transfer code plus recipient ID. Two things follow:
  - A platform-held code could act as a "reserved, not yet taken" payment, for example a buyer sends to the seller but gives the code to the platform, which releases it on delivery.
  - Whether an uncollected transfer can be cancelled or refunded to the sender, and within what time, is network practice that I did not verify. Treat it as an important open question.
- Because exchange companies cannot legally hold customer accounts, a platform cannot hold a "merchant account at an exchange company" under the law. Any collection through exchangers should be designed as named-beneficiary transfers or as an agent relationship with a licensed company. The latter would likely require CBY-Aden approval of the platform as a sub-agent or PSP.
- Since June 2024, UNMONEY is the legally mandated rail for domestic exchange transfers in government areas. It is the obvious target for any platform integration: a reference lookup or payout API via a member bank or exchange. Its 2025–26 handover to bank ownership suggests it may become the backbone for the FPS. North-south transfers remain politically fragile, because the Houthi syndicate refused to deal with Aden networks in 2024.
- 2026 enforcement against exchange companies means a platform partner exchange could lose its licence with no notice. Partner selection should favour the largest Aden-licensed, UNMONEY-member companies, or exchange-origin banks such as Kuraimi and Bin Dowal.

#### Setup option X1: Buyer pays through a domestic exchange transfer (UNMONEY or member company) to the seller; transfer code shared
| Dimension | Record |
|---|---|
| Buyer proof | Buyer pays cash (or from a wallet or bank) at any exchange outlet and receives a transfer number. The buyer gives the code to the seller or platform. Partly verified: the transfer-number practice is in [World Bank FSD Box 7](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf). |
| Who establishes outcome / how platform learns | The network or paying outlet when the recipient collects. The platform learns from the seller (person) or by checking the code. No public API found. |
| Reserve before take | Effectively yes: funds stay at the network until collected. Sender-cancellation rules are unverified. Inference. |
| Reversal / dispute | Before payout: possibly cancellable by the sender at the sending outlet (unverified). After payout: none. Unclaimed transfers must be reported to CBY-Aden after two months ([World Bank FSD](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)). |
| Who holds money / how long | The exchange network, until pickup. That can be days to indefinitely; tens of thousands of uncollected transfers have been reported ([SEMC](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)). |
| How money reaches seller | The seller collects cash with the code and ID, or into a wallet or bank account if the network supports it. Inference. |
| Platform position | Software only (records codes, the seller confirms); or escrow-like code holder (the platform receives the code and releases it to the seller, which needs care around money-transfer regulation). Inference. |
| Licence / partner | None for software-only use. A formal integration needs a UNMONEY member partner and probably CBY-Aden approval. |
| Currency / territory | YER (old or new zone), SAR, USD. Government areas are under CBY-Aden rules. North-south and Houthi-area coverage depends on the Houthi stance ([Sana'a Center](https://sanaacenter.org/the-yemen-review/july-sept-2024/23500)). |
| Cost / limits / settlement | Fees not found. Caps for e-wallet/PSP-originated transfers are "set under separate instructions" ([CBY news/706](https://cby-ye.com/news/706)). Pickup is usually same-day. Inference. |
| Risks | Code sharing and fraud (wrong name or phone). Cross-zone currency conversion losses. Exchange licence revocations. Houthi/Aden split. AML exposure: exchange houses in Sana'a have been OFAC-designated (2023–24) ([Treasury jy2014](https://home.treasury.gov/news/press-releases/jy2014)). |

#### Setup option X2: Platform pays sellers (payouts) by exchange transfer
| Dimension | Record |
|---|---|
| Mechanics | The platform (or its agent) sends a UNMONEY transfer to each seller, and the seller collects cash or credits a wallet. Inference. |
| Licence | Bulk disbursement by a non-licensed platform is likely to attract regulatory scrutiny. Partnering with a licensed bank or exchange for disbursement is safer. Inference. |
| Precedent | Humanitarian cash programmes pay beneficiaries "over the counter at an exchange house, or at the post office" ([World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)). |

### Gaps
- No fee table for UNMONEY, Al-Najm, Al-Imtiaz/Emtiaz, Bin Dowal or Kuraimi domestic transfers (YER or %), and no per-transfer or daily limits.
- Whether UNMONEY exposes an API or reference-lookup service to third parties (merchants or platforms) is unknown, as is whether bank and wallet members can deliver into accounts or wallets rather than cash.
- Cancellation and refund rules for unpaid transfers are unknown.
- Whether the Houthi side ran its own parallel unified network in 2025–26, and the current state of north-south transfers after the 2025 relocations and FTO designation, were not found.
- Many of the 2025–26 licence-suspension articles name companies only in attached PDFs that I did not read.

---

## Q3. Is card acquiring for e-commerce available in Yemen (online gateway, 3-D Secure, local switch)? What share of people hold cards?

### Takeaway
Card ownership is tiny: about 400,000 active debit cards at end-2019 (mostly used at ATMs) and about 1,200 active credit cards, in a population above 30 million. POS terminals numbered only 817 in 2019. There is at least one live, CBY-licensed e-commerce card gateway: MEPS Yemen (the National Payment Company). It accepts local and international Visa, Mastercard, Amex and UnionPay cards via Mastercard Payment Gateway Services (MPGS), Visa CyberSource and PayTabs, and it offers payment links and invoicing. Some banks issue online-capable cards: CAC's Visa "Net" card (internet only) and SBYB's "WebSurfer" prepaid Mastercard. For domestic buyers, cards are a niche rail. They matter mainly for diaspora and foreign-card buyers.

### Cited Findings
- Active debit cards fell from more than 1 million (2014–15) to 200,000 by end-2016, then recovered to about 400,000 at end-2019, "mostly used for ATM services." Active credit cards fell from about 6,600 (2014) to 1,206 (2019). — [Sana'a Center (Mar 2022)](https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf)
- ATMs: 6.4 per 100,000 adults in 2014. POS fell to 200 devices in 2016 from 1,500 in 2014, then "tripl[ed] to reach 817 in 2019." — [World Bank FSD 2024](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- MEPS Yemen (الشركة الوطنية للمدفوعات) "electronic payment gateway":
  - It accepts local and international cards (Mastercard, Visa, American Express, UnionPay).
  - It is powered by Mastercard Payment Gateway Service (MPGS), Visa CyberSource and PayTabs (KSA).
  - It offers on-site checkout without redirect, plugins, e-invoicing by email or SMS with payment URL, and fixed-amount payment links for social media.
  - It says it is licensed by the Central Bank of Yemen and was formed by Middle East Payment Services (MEPS) and the National Cash Transfer Company.
  - Other services: ATM management, POS operation, card issuance and e-collection.
  - 3-D Secure, currencies, fees and settlement are not stated.

  — [MEPS Yemen, Electronic Payment Gateway page](https://www.mepsyemen.com/electronic-payment-gateway); [MEPS Yemen home](https://www.mepsyemen.com/)
- MEPS took part in the CBY-sponsored cashless expo in Aden (22 Jan 2026), alongside more than 9 e-wallets and the unified network. — [CBY-Aden news/915](https://cby-ye.com/news/915)
- CAC Bank "Visa Net" card is used "to buy from internet only." It cannot be used at POS or ATMs. CAC's other Visa cards work at ATMs, POS and online. — [CAC Bank Visa Cards page](https://www.cacbank.com.ye/en-Us/Contents/SubPage/Visa-Cards)
- SBYB "WebSurfer" is a prepaid Mastercard for online shopping, "accepted on most websites worldwide," and recharged via the Shamil Money app. Undated bank marketing page. — [SBYB Electronic Cards Service](https://www.sbyb.net/en/service/17)
- National Bank of Yemen issues Silver and Gold Visa and Mastercard credit cards with Arab Financial Services (Bahrain). Undated. — [NBY credit cards](http://www.nbyemen.com/creditCard_en.html)
- SabaCard was founded in 2005 by Al Rowaishan Group and Yemen Commercial Bank. It describes itself as "the first local e-payment solutions provider" and offers ATM and POS switching, working with Mastercard and Visa. — [SabaCard](https://www.sabacards-rg.com/en/)
- UnionPay International signed with CAC Bank to issue UnionPay cards in Yemen. The URL slug suggests 29 Dec 2014. — [Electronic Payments International](https://www.electronicpaymentsinternational.com/news/unionpay-partners-with-cac-to-issue-payment-cards-in-yemen-291214-4478310)
- A third-party payouts firm lists Al-Kuraimi Bank Mastercard BINs as having a "history of successful transactions" (weak, operational evidence only). — [Mellow help center](https://help.mellow.io/en/articles/9647437-tested-bank-cards-of-yemen)
- CBY-Aden adopted a mandatory national QR standard (29 Mar 2026). This is a non-card alternative for in-person and online "scan to pay." — [CBY-Aden news/922](https://cby-ye.com/news/922)

### Inferences
- E-commerce card acceptance is technically available through MEPS Yemen. Because it runs on MPGS and CyberSource, 3-D Secure and authorize-then-capture are probably supported. That is an inference: the MEPS page does not say so. These two features would give the platform a "reserve before take" ability and a scheme-based chargeback process that no other Yemeni rail offers.
- Domestic card penetration (about 400k active debit cards in 2019, largely ATM-only) means few local buyers will pay by card. The real value of the MEPS gateway is foreign or diaspora cards paying Yemeni sellers in-country, if MEPS settles to a Yemeni bank account. That means Visa and Mastercard cards issued abroad; whether Saudi mada cards are accepted is not stated.
- Sanctions context: Visa and Mastercard serve Yemen through licensed local issuers and acquirers. Card-scheme connectivity for banks still under Sana'a control or OFAC-designated (YKB, IBY) is unreliable. A platform should confirm which acquiring bank MEPS settles through and that bank's sanctions and relocation status.

#### Setup option C1: Card e-commerce acquiring through MEPS Yemen gateway (platform or seller as merchant)
| Dimension | Record |
|---|---|
| Buyer proof | Card details entered on hosted or embedded checkout or a payment link. Probably 3-D Secure (inferred from MPGS/CyberSource; not stated). [MEPS Yemen](https://www.mepsyemen.com/electronic-payment-gateway) |
| Who establishes outcome / how platform learns | The gateway and issuer. Real-time authorization response; a confirmation email to merchant and customer for invoices ([MEPS Yemen](https://www.mepsyemen.com/electronic-payment-gateway)). The platform gets an API callback or webhook (inferred from "plugins / developer-friendly options"). |
| Reserve before take | Likely (MPGS supports authorization/capture). Unverified for MEPS Yemen. |
| Reversal / dispute | Refunds through the gateway. Chargebacks through Visa/MC rules. Inference. |
| Who holds money / how long | The acquiring bank and MEPS until settlement. Settlement terms not found. |
| How money reaches seller | To the merchant's account at the acquiring bank (if the seller is the merchant), or to the platform, which then pays out. Inference. |
| Platform position | Payment facilitator / aggregator (platform as merchant of record, sub-merchants underneath), or technical integrator with each seller onboarded to MEPS separately. Inference. |
| Licence / partner | Merchant agreement with MEPS Yemen (CBY-licensed per its site) and its acquiring bank. A payfac model probably needs CBY-Aden approval. Inference. |
| Currency / territory | Not stated. Likely YER (new) and/or USD. Inference. |
| Cost / limits / settlement time | Not found. |
| Risks | Low domestic card ownership. Cross-border card fraud. Acquirer bank's correspondent/sanctions status. MEPS Yemen's actual live volume unknown. |

#### Setup option C2: Local POS card acceptance at delivery (card-on-delivery)
| Dimension | Record |
|---|---|
| Feasibility | Very limited: about 817 POS terminals in 2019 ([World Bank FSD](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)). MEPS Yemen and SabaCard operate POS ([MEPS](https://www.mepsyemen.com/electronic-payment-gateway); [SabaCard](https://www.sabacards-rg.com/en/)). The QR standard (2026) may replace POS for this use ([CBY news/922](https://cby-ye.com/news/922)). Inference: not a launch rail. |

### Gaps
- No MEPS Yemen pricing, settlement time, currency list, 3-D Secure confirmation, acquiring bank, or merchant onboarding criteria. No count of live merchants.
- No 2020–2026 data on card numbers, POS counts or online card usage. No Global Findex card-ownership figure for Yemen after 2014.
- No current Visa or Mastercard country pages or press releases for Yemen found. Whether Saudi mada cards can be accepted via MEPS Yemen is unknown.
- Whether any other Yemeni bank (Tadhamon, Kuraimi, YCB, CAC) operates its own e-commerce acquiring gateway was not established.

---

## Q4. Which foreign payment processors or wallets accept Yemeni merchants or Yemen-based buyers, and which explicitly exclude Yemen? How do diaspora buyers pay for goods delivered in Yemen today?

### Takeaway
None of the mainstream global processors onboard Yemen-based merchants:
- Stripe does not list Yemen.
- Wise explicitly does not support Yemen.
- PayTabs' published coverage (per an integrator) excludes Yemen, although MEPS Yemen uses PayTabs behind its own gateway.
- PayPal's Yemen status is unconfirmed, at best "send-only."
- Several fintechs (Rho, CoinGate, Wallex) list Yemen as restricted.

Diaspora money reaches Yemen mainly through three channels:
- Yemeni banks: USD 4.9 bn inbound in 2022.
- Western Union and MoneyGram: USD 1.1 bn inbound in 2022.
- Yemeni exchange-company agents abroad, especially in Saudi Arabia, in a hawala pattern.

STC Pay (KSA) sends to Western Union pickup. For a commerce platform, the realistic diaspora options are (a) card checkout through MEPS Yemen, or a foreign entity of the platform (e.g., UAE, where Stripe operates) with onward settlement into Yemen, and (b) "pay by remittance": the buyer abroad sends a WU, MoneyGram or exchange-company transfer to the seller or platform agent, quoting the order reference.

### Cited Findings

**Exclusions / availability**
- Stripe "Global availability" lists 51 countries. Yemen is not listed. The UAE is the only nearby Middle East country listed; Saudi Arabia is not. — [Stripe Global](https://stripe.com/global)
- Wise lists Yemen under "Countries and regions we don't support." Users there cannot register, and Wise cannot "send or receive money to or from" these places. — [Wise Help: countries we can send to](https://wise.com/help/articles/2978049/what-countries-and-regions-can-i-send-money-to)
- PayPal has a Yemen-locale page (/ye/) offering send and pay functions. PayPal says members in some countries "may only use PayPal to send payments and not receive payments." No Yemen-specific statement was found. A Wise hub page claims PayPal is "accepted in Yemen" (secondary source). — [PayPal /ye/](https://www.paypal.com/ye/webapps/mpp/home); [PayPal Help: send-only](https://www.paypal.com/va/cshelp/article/why-does-my-paypal-account-have-only-send-capabilities-help1027); [Wise payment-methods hub (Yemen)](https://wise.com/gb/hub/payment-methods/yemen)
- PayTabs coverage per an integrator: UAE, Saudi Arabia, Egypt, Oman, Jordan, Kuwait, Iraq. Yemen is not listed. Integrator page, not PayTabs' own. — [Mewayz PayTabs docs](https://mewayz.com/docs/payment-gateway-paytabs). Separately, MEPS Yemen lists PayTabs among its back-end processors ([MEPS Yemen](https://www.mepsyemen.com/electronic-payment-gateway)).
- Rho lists Yemen as restricted. CoinGate lists it among jurisdictions where payments are not permitted. Wallex cannot send to or receive from Yemen. These are search summaries. — [Rho](https://www.rho.co/hc/restricted-countries-and-international-payment-types); [CoinGate](https://support.coingate.com/hc/en-us/articles/23236010880412-Countries-and-territories-not-supported-for-payments); [Wallex](https://help.wallex.asia/list-of-restricted-countries)
- Payoneer's prohibited-transactions page says eligibility depends on "country of residency or incorporation," but the search summary showed no Yemen-specific statement. — [Payoneer prohibited list](https://www.payoneer.com/ar/legal/prohibited-transaction-list/)

**How diaspora money flows today**
- In 2022, Yemen's banking sector processed USD 4.9 bn inbound and USD 5.6 bn outbound transfers. Most inbound transfers were in USD, then SAR, EUR and AED. Western Union and MoneyGram are "the second largest channel," with USD 1.1 bn inbound in 2022 (USD 400 m in Q1 2023) and a net inflow of USD 945 m. — [World Bank FSD 2024, Box 8](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)
- Typical hawala flow from Saudi Arabia: an expatriate pays a Yemeni exchange company's agent in KSA, and the Yemeni exchange pays the beneficiary in Yemen "at the parallel-market exchange rate." The agent then uses the KSA balance to pay importers' suppliers abroad. "Electronic banking services in neighboring countries have facilitated these operations." — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- A large share of remittances bypasses banks and goes through exchange companies or informal networks (ACAPS, Oct 2021). — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- Remittances are about 20% of GDP (2023), per a search summary of the IGC brief. The same brief puts 2025 exchange rates at about 530 YER/USD in Houthi areas and 1,550 in government areas. — [IGC, "From Cash to Capital" (Feb 2026)](https://www.theigc.org/sites/default/files/2026-02/From-Cash-to-Capital-Leveraging-Remittances-for-Yemens-Economic-Future.pdf)
- Formal inflows are estimated at USD 4–6 bn, and informal flows possibly up to USD 10 bn. International bank de-risking has narrowed formal options. Search summary. — [AidData](https://www.aiddata.org/blog/leveraging-remittances-for-economic-recovery-in-yemen)
- STC Pay (KSA) international transfers can be collected at Western Union locations ("more than 525,000 worldwide") or sent to bank accounts or wallets. The World Bank Remittance Prices database lists an STC Pay Saudi→Yemen entry (data collected 6–15 Nov 2024). I could not open the RPW page (403); this is a search summary. — [STC Pay international transfer](https://stcpay.com.sa/international-transfer); [World Bank RPW SA→YE](https://remittanceprices.worldbank.org/corridor/SA/YE)
- Since 28 May 2024, only CBY-Aden-qualified banks and exchange companies, and their sub-agents, may pay out international remittances. Payout must be in the currency sent. — [Asharq Al-Awsat](https://aawsat.com/node/5025163)
- In the Saudi→Yemen hawala, the exchanger profits from FX margins: for example it sells USD at SAR 3.85 versus the official 3.75. — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- About 3 million Yemenis work in Saudi Arabia (search summary of a Noonpost article; undated and weak). — [Noonpost](https://www.noonpost.com/41375/amp/)

### Inferences
- No foreign processor will onboard a Yemen-domiciled merchant or platform entity. For card checkout aimed at diaspora buyers, Sharrwah has two options:
  - (a) use MEPS Yemen in-country; or
  - (b) set up a foreign entity (e.g., UAE, which Stripe supports) as merchant of record, collect cards abroad, and move funds into Yemen through a licensed bank or a WU/MoneyGram/exchange remittance.

  Option (b) carries heavy compliance obligations: OFAC/FTO screening of every seller and payout recipient, and processor acceptable-use rules on high-risk jurisdictions. Processors may still refuse because the sellers are located in Yemen. That is an inference; I did not verify Stripe's restricted-business terms for Yemen-located sellers.
- Inference, not verified in this session: the US Yemen sanctions programme is list-based, not a comprehensive embargo. The Houthi FTO designation (Mar 2025) plus the SDN listings of YKB, IBY and several Sana'a exchange houses make north-Yemen counterparties the main compliance risk, rather than Yemen as a whole.
- "Pay by remittance" is the practice diaspora buyers already follow for family support. A buyer in KSA or the US sends a WU, MoneyGram, STC Pay or exchange-agent transfer to a named recipient, the seller or a platform collection agent, and passes on the reference number. It inherits the X1 dimensions: code-based outcome, funds held by the network until pickup, and no chargeback.
- PayPal and Payoneer are not dependable rails for Yemen-based sellers. At most, a Yemeni seller could hold a send-only PayPal account, which cannot receive.

#### Setup option F1: Foreign card acquiring via a platform entity abroad (e.g., UAE Stripe/Checkout.com account), diaspora buyer pays by card
| Dimension | Record |
|---|---|
| Buyer proof | Card with 3-D Secure on the foreign PSP (standard PSP behaviour; inference). |
| Outcome / platform learns | PSP API and webhooks. Real-time. |
| Reserve before take | Yes: authorize and capture (standard). Inference. |
| Reversal / dispute | Refunds, plus card-scheme chargebacks. The platform bears the risk. |
| Who holds money / how long | The PSP, until payout to the foreign entity's bank (days). Then the platform holds it until it is remitted to Yemen. Inference. |
| How money reaches seller | The foreign entity remits through a Yemeni bank (SWIFT; banks processed USD 4.9 bn inbound in 2022 ([World Bank FSD](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf))), WU/MoneyGram, or a qualified exchange company. |
| Platform position | Merchant of record / marketplace collecting on behalf of Yemeni sellers. Inference. |
| Licence / partner | Foreign entity, PSP account and money-transmission or marketplace exemptions in that jurisdiction. In Yemen, a CBY-Aden-qualified receiving bank or exchange ([Asharq Al-Awsat](https://aawsat.com/node/5025163)). |
| Currency / territory | Buyer worldwide in USD, SAR, AED etc. Payout in USD or SAR, or converted to old or new YER. |
| Cost / limits / settlement | PSP fees plus remittance fees plus FX spread (parallel-market margins). Not quantified. |
| Risks | PSP account termination for Yemen-linked activity. OFAC/FTO screening. Cross-border settlement delays. FX spread between the two rial zones. |

#### Setup option F2: Diaspora "pay by remittance" (WU / MoneyGram / STC Pay→WU / Saudi agent of a Yemeni exchange) to seller or platform collection agent
| Dimension | Record |
|---|---|
| Buyer proof | MTCN or transfer reference from the remittance provider. Inference. |
| Outcome / platform learns | The seller or agent confirms pickup or credit. No API for third parties. Inference. |
| Reserve before take | Funds are held until pickup. Sender cancellation is typically possible before payout (unverified). |
| Reversal / dispute | Only before payout. No chargeback. |
| Who holds money / how long | The remittance provider or exchange until pickup. Inference. |
| How money reaches seller | Cash or account payout in the sent currency, through a CBY-qualified institution ([Asharq Al-Awsat](https://aawsat.com/node/5025163)). |
| Platform position | Software only (records the reference); or named collection agent (licensing risk). Inference. |
| Cost | Not found. RPW has SA→YE data but I could not open it. |
| Risks | Recipient name and ID errors (unclaimed transfers are common: [World Bank FSD Box 7](https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf)). Sanctions screening. Saudi transfer limits. |

### Gaps
- Official PayPal country terms for Yemen (full vs send-only vs unavailable) not confirmed. Payoneer's Yemen status not confirmed. Checkout.com, HyperPay, Moyasar and Tap coverage not individually checked. I found nothing showing they onboard Yemeni entities, and PayTabs (per an integrator) does not.
- No source on whether Saudi wallets (STC Pay, urpay) or banks (Al Rajhi's Tahweel, Enjaz) pay directly into Yemeni bank accounts or wallets (e.g., Kuraimi) rather than WU cash. No RPW cost figures (403).
- No evidence found of Saudi- or US-based e-commerce sites that sell goods for delivery inside Yemen and how they collect. The only result was a corporate gifting site (Giftsenda) with marketing claims. This "diaspora gift-commerce" practice remains unverified.
- No processor statements on whether they would accept a non-Yemeni merchant entity whose sellers or deliveries are in Yemen.

---

## Q5. Is crypto or USDT used in practice for commerce or remittances in Yemen?

### Takeaway
I found no reliable evidence that USDT or crypto is used for ordinary commerce or household remittances in Yemen. The documented use is illicit or sanctions-evasion finance: OFAC designated eight Tron (USDT) addresses tied to the Houthi financier Sa'id al-Jamal's network, which reportedly moved large sums. A Yemeni policy paper also lists crypto trading as a laundering method of the parallel market. The Sana'a "e-rial" (2019–) is a central-bank electronic balance, not crypto. Crypto is not a practical or defensible rail for a Yemen commerce platform.

### Cited Findings
- OFAC added eight Tron wallet addresses linked to a Houthi financial-facilitator network (Sa'id al-Jamal) to the SDN list. The addresses "largely transacted with Tether's USDT," and coverage says they reportedly moved nearly USD 1 bn (a secondary figure). The action is from 2025 per coverage; the exact date was not verified. — [Decrypt](https://decrypt.co/312999/us-treasury-sanctions-tron-wallets-tehter-houthis); [TRM Labs](https://www.trmlabs.com/post/us-treasury-sanctions-houthi-financial-networks-including-eight-crypto-addresses)
- TRM links the funds to IRGC-QF and al-Jamal entities such as Davos Exchange and Remittances Company, which operated "under the guise of legitimate financial institutions." It also notes Houthi crypto-mining since at least 2017 with limited impact. — [TRM Labs](https://www.trmlabs.com/post/us-treasury-sanctions-houthi-financial-networks-including-eight-crypto-addresses)
- Dec 2023: OFAC targeted the head of the Sana'a Currency Exchangers Association and exchange houses moving funds for al-Jamal. — [US Treasury jy2014](https://home.treasury.gov/news/press-releases/jy2014)
- SEMC lists "Cryptocurrency trading to obscure the origin of funds" among the parallel market's money-laundering methods. — [SEMC (Dec 2025)](https://economicmedia.net/en/wp-content/uploads/2025/12/The-Parallel-Market-in-Yemen-Banking-Sector-December-2025.pdf)
- The AGSI (Feb 2020) piece on the Yemeni "e-rial" describes a CBY-Sana'a digital balance (in trial since 2018) usable for a few services such as phone, water and electricity bills. It is not cryptocurrency. — [AGSI](https://agsi.org/ar/?p=22899)
- A NewHedge guide says Binance advertised YER P2P support, and that users worry about account freezes for Yemen residents. This is a promotional, unverified source. — [NewHedge](https://newhedge.io/buy/yemen)
- Arabic-language sites sell USDT, Perfect Money and Payeer balances to Yemenis (e.g., "المتجر اليمني للدفع الإلكتروني"). These are commercial listings with no usage data. — [ysfep.com](https://www.ysfep.com/); [Digibankar guide](https://digibankar.com/docs/transfer/yemen/global/)

### Inferences
- Crypto exists at the margins, through P2P and resellers of e-currency balances, and in documented illicit finance. There is no evidence of merchant acceptance or meaningful household remittance use.
- For Sharrwah, a USDT rail would combine the following:
  - no consumer protection;
  - fraud and scam risk;
  - CBY-Aden's stance against unlicensed e-payment services (12 entities banned in June 2024 ([CBY news/703](https://cby-ye.com/news/703)));
  - OFAC exposure (Houthi-linked Tron addresses).

  It should be excluded or treated as out of scope.

### Gaps
- No survey data on crypto ownership or P2P volumes in Yemen. No explicit CBY-Aden or CBY-Sana'a statement on cryptocurrency found in this session.
- Exact date and Treasury press-release number for the Tron-wallet designation not verified.
