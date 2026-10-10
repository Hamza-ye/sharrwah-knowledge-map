# Analog setup patterns: how commerce platforms in cash-heavy, fragmented, sanctioned or low-card markets bridged payments (for a Yemen launch)

Scope note: this file covers patterns from other markets, not Yemen. "Setup option" means one practical way money can move from buyer to seller. Facts carry an inline source. Anything without a source is marked as inference or listed under Gaps. Research date: 9 October 2026. Several sources are vendor blogs or forum posts; they are flagged as weaker where used.

---

## KQ1. How did platforms in Iraq, Libya, Sudan, Syria, Somalia/Somaliland, Afghanistan, Ethiopia, Egypt, Pakistan/Bangladesh, Nigeria/Kenya and Saudi Arabia handle payments, and how did their setups evolve?

### Takeaway
In every analog market, cash on delivery (COD) came first. Digital money then arrived as one of three things: (a) a manual "pay to this wallet or account, then send proof" method the seller verifies; (b) direct integrations with one dominant wallet or reference-code network; or (c) a platform-branded payment layer, usually run through a licensed partner and only later licensed in its own right. COD was not replaced; it stayed the bulk of volume for years. Jumia still had about 28% of 2025 GMV going through its payment gateways, and roughly 20% of Daraz Pakistan orders were prepaid in 2025. Platforms improved COD by digitising collection at the door, netting COD through platform wallets, and financing COD receivables. The strongest late-stage move was a licensed wallet or bank-card issuer taking over the marketplace (QiCard buying Miswag in Iraq).

### Cited Findings

**Nigeria / Kenya / pan-Africa (Jumia, Paystack, M-Pesa)**
- About 95% of Jumia's Kenyan consumers paid COD in 2016. Jumia Logistics handled 92% of Jumia's deliveries in 2018 using leased warehouses, drop-off centres, more than 100 integrated local third-party logistics providers, and its own last-mile fleet in some cities (Caribou summary of Jumia's 2019 F-1) — [Caribou Digital, June 2019](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)
- A Mastercard case study says more than 95% of Jumia's sales were COD at one point and that delivery agents carrying cash were exposed to theft. Read via search snippet only; the PDF returned 403 — [Mastercard mPOS Jumia case study, 2017](https://www.mastercard.com/corporate/_assets/pdf/MPOS_Jumia_CaseStudy_031717.pdf)
- In Q1 2024 the share of Jumia physical-goods orders paid through JumiaPay rose from 20% to 32.5% year on year. Jumia credited the "continued rollout of JumiaPay on delivery in Nigeria and Kenya to increase cashless orders" — [TechCrunch, 7 May 2024](https://techcrunch.com/2024/05/07/jumia-is-back-growing-total-sales-and-orders-in-q1-2024)
- In one 2022 quarter JumiaPay processed 34% of orders on the platform, mostly food delivery — [TechCrunch, 17 May 2022](https://techcrunch.com/2022/05/17/the-e-commerce-boom-is-still-afoot-in-africa-jumias-earnings-indicate/)
- Jumia FY2025: GMV was $818.6M and TPV (value of orders using Jumia payment gateways) was $232.2M. Q4 2025: GMV $279.5M, TPV $81.4M. Jumia Payment Gateways Transactions fell from 10.1M to 7.1M (-30%), and JumiaPay App orders fell from 4.4M to 0.7M as Jumia "reduced our emphasis on digital products sold through our JumiaPay App". Jumia states that it uses TPV and gateway transactions "to measure the development of our payment services and the progressive conversion of cash on delivery orders into prepaid orders". Q4 2025 working capital improved partly from "better payment flows" — [Jumia Q4 2025 results, Exhibit 99.1, 10 Feb 2026](https://s205.q4cdn.com/370993272/files/doc_financials/2025/q4/Jumia-EX-99-1-Q4-2025-2-10-2026-Final-v5.pdf)
- Paystack (Nigeria) was founded in 2015, went through Y Combinator in 2016, and served more than 60,000 businesses when Stripe acquired it in 2020 for over $200M — [Wikipedia: Paystack](https://en.wikipedia.org/wiki/Paystack)
- Paystack's early product was a simple tool for creating payment links without a developer, because "most businesses don't have access to developers" — [How We Made It In Africa](https://www.howwemadeitinafrica.com/the-nigerian-entrepreneur-behind-africas-response-to-paypal-and-stripe/84780/)
- Kenya (M-Pesa): a Paybill's "account number" field is the standard carrier of the order ID in Kenyan e-commerce integrations, and a Till has no reference field. Online shops typically trigger an STK Push prompt so the buyer only enters a PIN, which needs retry and abandonment handling. Vendor guide, weaker source — [paybillke.com guide, 2026](https://paybillke.com/guides/mpesa-for-online-businesses-2026)

**Egypt (Fawry reference codes, CBE rules, payment on delivery)**
- Fawry launched in 2008 as an e-payment switch linking utilities and telecom operators to consumers through retail agents. It started with bill payments, not e-commerce, and now processes about six million transactions a day — [TechCabal, 20 Apr 2026](https://techcabal.com/2026/04/20/how-fawry-built-a-profitable-fintech/)
- Fawry e-commerce reference-code flow: the merchant requests a reference number through the API and the payment stays "Pending" until the buyer pays cash at any Fawry agent, kiosk, store or the Fawry app. Limits are EGP 1 to EGP 100,000, and an unpaid reference expires after 7 days — [EBANX docs: Fawry](https://docs.ebanx.com/docs/payments/guides/accept-payments/api/egypt/fawry)
- Valu (a lender), PayTabs Egypt (gateway) and ShipBlu (courier) partnered so that buyers can pay ShipBlu-delivered orders with Valu credit inside the courier's myBlu app, turning COD into "Payment-on-Delivery". Cards, QR codes and e-wallets are also accepted at the door. The article does not say who pays the merchant or when — [WAYA, 30 Sep 2024](https://waya.media/valu-paytabs-and-shipblu-partner-to-streamline-e-commerce/)
- Bosta (Egyptian courier) advertises next-day COD transfers to merchants — [Bosta Shopify app listing](https://apps.shopify.com/bosta-shipping-app)

**Iraq (ZainCash, Qi Card, Miswag)**
- Iraq Wallet launched "Pay with ZainCash" in August 2016, described as Iraq's first online payment solution, so that sellers could accept payments on websites and apps — [TelecomTV](https://telecomtv.com/content/tracker/iraq-wallet-expands-zaincash-service-to-boost-e-commerce-with-country-s-first-online-payment-solution-23106)
- A December 2021 analysis says Iraq's weak payment system and low financial inclusion force e-commerce onto COD. It names the risks as buyers refusing at delivery, multiple fake orders, and cash flow tied up until physical cash is received. Miswag was founded in 2014 — [IraqTech, 1 Dec 2021](https://iraqtech.io/an-analysis-on-the-rise-of-e-commerce-in-iraq/)
- Miswag's app listing names these payment options: payment on receipt, Visa/Mastercard, ZainCash, Asia Transfer, and six-month instalments with Qi cards (undated self-description) — [Miswag on App Store](https://apps.apple.com/mx/app/miswag/id1025309304)
- QiCard (International Smart Card) acquired Miswag for an undisclosed "seven-figure" sum, reported 3 Dec 2024. Miswag keeps operating and becomes a mini-app inside the SuperQi super-app, with BNPL among the new features — [Iraq Business News, 3 Dec 2024](https://www.iraq-businessnews.com/2024/12/03/qicard-acquires-miswag/)
- Central Bank of Iraq Electronic Payment Services Regulation No. 2 of 2024 replaced the 2014 rules and was published 29 Apr 2024. Providers need a CBI licence valid for ten years; covered activities include cards, wallets, mobile payments, transfers and payment aggregation, plus agents acting for licensed providers. Providers must hold financial guarantees or liquid assets and keep records for five years — [vLex summary](https://vlex.com/vid/electronic-payment-service-companies-1090421790)

**Saudi Arabia (Salla, Zid)**
- Salla payment methods: Salla's built-in "electronic payments" (mada, Visa, Apple Pay), which processes payments and settles with banks; wallets (PayPal, stc pay, Google Pay); third-party gateways (Moyasar, HyperPay, KNET via Tap); and BNPL (Tabby, Tamara, Emkan, Madfu, MISpay). Settlement depends on plan: Special daily, Pro every 48 hours, Plus weekly. The minimum transfer is SAR 100 — [Salla Help: manage payment methods (marked old)](https://help.salla.sa/en/article/manage-payment-methods/dtdojcntv3f4lwqzj4h0jvij)
- Salla COD through Salla-issued waybills: carriers include Aramex, J&T, AyMakan, SMSA, RedBox and Shipa. The merchant sets a COD fee and can add min/max order value, weight limits, product exclusions, and hide COD from buyers blocked by other Salla stores. The page states (flagged for verification) a SAR 1,000 maximum, no COD under SAR 20, COD balances paid out Sundays and Wednesdays, and an invoice covering "Delivered/Shipped" orders from the previous week. A per-transaction ledger is exportable to Excel — [Salla Help: COD with Salla waybills](https://help.salla.sa/en/article/manage-cash-on-delivery-salla-waybills/nonfrowzfu421ewhv6klylv6)
- Refunds run through Salla only for mada, Visa, Apple Pay or Tamara payments. Read via search snippet — [Salla Help: returns and refunds](https://help.salla.sa/en/article/manage-order-returns-refunds/lwd3jzhb0qs7v51b50rcc50a)
- Salla's cross-border payouts: UAE weekly on Thursdays above AED 250; Kuwait next business day, minimum KWD 1 — [Salla Help UAE](https://help.salla.sa/article/salla-payments-uae-payouts-settlement-salla/n047k89ek7oycx73uxh9lv1y); [Salla Help Kuwait](https://help.salla.sa/en/article/salla-payments-kuwait-payouts-settlement-salla/oklj5eoidm82h73hfra94dv2)
- Zid Pay terms (Saudi): merchants authorise Zid to execute payment processes on their behalf. Zid Pay may request invoices, delivery receipts and proof of delivery to meet risk-assessment requirements, and non-compliance can lead to suspension or termination. The Kuwait terms define Zid Pay as "a service that allows merchants to conduct sales transactions through payment service providers on a platform belonging to Zid" — [Zid Pay T&C KSA](https://zid.sa/en/legal/zidpay-terms-conditions-sa); [Zid Pay T&C Kuwait](https://zid.sa/en/legal/zidpay-terms-conditions-kw)
- Earlier PayTabs–Zid partnership (undated): PayTabs to power payments for Zid stores (about 4,000 stores), with COD offered through partners and logistics arranged by Zid — [PayTabs](https://paytabs.com/?p=16032)
- SAMA licence categories include micro and major payment institutions and micro and major e-wallet (e-money) institutions — [SAMA: payment licence forms](https://sama.gov.sa/en-US/ApplyLicense/Pages/Payment_Forms.aspx)
- Market shift: Checkout.com research reports that the share of Saudi consumers preferring COD fell 66% since 2020, and that 75% would pay by card if COD were unavailable — [Gulf Business, 2024](https://gulfbusiness.com/en/2024/retail/e-commerce-drives-mena-digital-payments). Mada e-commerce sales reached SR197.42bn ($52.6bn) in 2024, up 25.8% — [Arab News](https://www.arabnews.com/node/2589350/business-economy)

**Pakistan / Bangladesh (Daraz, couriers, regulators)**
- A Daraz executive told Dawn's Aurora that about 80% of transactions were COD (older interview) — [Aurora/Dawn](https://aurora.dawn.com/news/1143493). In September 2025, ProPakistani reported nearly 20% of Daraz Pakistan orders were prepaid — [ProPakistani, 12 Sep 2025](https://propakistani.pk/2025/09/12/a-decade-of-daraz-pakistan-pioneering-e-commerce-and-shaping-access-trust-and-opportunity/amp/)
- Daraz Pakistan refunds "all orders paid through Cash on Delivery (COD), Easypaisa Shop (OTC) or JazzCash Mobile Account" only to the Daraz Wallet. The Daraz Wallet pages say only the refund portion of a wallet balance can be withdrawn; deposits and bonuses are spend-only. Read via search snippets; the refund page returned 503 when fetched — [Daraz PK refund policy](https://www.daraz.pk/refund-policy/); [Daraz Wallet](https://www.daraz.pk/daraz-wallet/)
- Daraz Bangladesh refunds COD orders by bank deposit within 5 working days, or by Daraz refund voucher within 1 working day — [Daraz BD refunds policy](https://www.daraz.com.bd/refunds-policy/)
- Daraz reportedly cut its seller payment cycle from 14 to 7 days (undated article) — [Pakistan Observer](https://pakobserver.net/dawood-appreciates-darazs-contribution-to-ecommerce-industry/)
- Pakistan's Finance Act 2025, effective 1 July 2025, sets withholding of 1% on digital-channel payments through a payment intermediary and 2% on COD collected by a courier — [KPMG brief on Finance Act 2025](https://assets.kpmg.com/content/dam/kpmg/pk/pdf/2025/07/A-Brief-on-Finance-Act-2025.pdf). The FBR defined "courier" to include persons who deliver goods and collect cash for e-commerce sellers and made couriers withholding agents — [FBR Circular 02 of 2025-26](https://download1.fbr.gov.pk/Docs/202584118361586CircularNO02of2025-26SalesTax%26FederalExcise.pdf). Online marketplaces and couriers were barred from serving unregistered sellers from 1 July 2025 — [Profit, 3 Sep 2025](https://profit.pakistantoday.com.pk/2025/09/03/online-marketplaces-and-couriers-barred-from-serving-unregistered-sellers)
- Bangladesh Bank's 30 June 2021 notice requires money collected by banks, PSOs, MFS or PSPs for digital-commerce businesses to be used only to pay the merchant. For "other" businesses, the PSP releases funds only after delivery: the business submits each buyer's name, mobile number and purchase details, and the PSP spot-checks. Refunds and chargebacks go back through the original payment medium, with charges borne by the business. Existing COD continues. Sellers of daily essentials and own products settle under existing arrangements if they deliver within 5 or 7 days — [Mahbub & Company summary](https://mahbub-law.com/bangladesh-bank-issues-guidelines-on-settling-payments-in-e-commerce-transactions)

**Somalia / Somaliland**
- In Hargeisa shops (2016), a ZAAD account number is commonly written on a board for customers to pay into — [ICTworks, 2016](https://www.ictworks.org/the-rise-of-mobile-money-services-in-somaliland/). Telesom's CEO told GSMA that ZAAD is used by 70% of Telesom subscribers — [GSMA](https://www.gsma.com/mobilefordevelopment/uncategorized/developing-a-currency-exchange-functionality-to-drive-mobile-money-usage-a-new-mobile-money-innovation-in-somaliland/)
- The Central Bank of Somalia issued the country's first mobile money licence to Hormuud (EVC Plus) on 27 Feb 2021. It had first licensed banks and money transfer businesses — [CBS press statement](https://centralbank.gov.so/wp-content/uploads/2021/11/PRESS-STATEMENT.pdf)
- A merchant setting up a Shopify store for Somalia found no ZAAD, eDahab or EVC integrations among Shopify's gateways. A reply pointed to Sifalo Pay as a third-party option (unverified vendor claim) — [Shopify Community](https://community.shopify.com/t/mobile-payment-method-integration-in-somalia/260502)
- Somaliland/Somalia e-commerce runs on third-party delivery firms (e.g., Gulivery in Hargeisa and Mogadishu) and dollar-denominated mobile money — [Quartz, 2018](https://qz.com/africa/1428066/somalias-e-commerce-start-ups-gullivery-saami-online-thrive); [How We Made It In Africa](https://www.howwemadeitinafrica.com/p/the-somaliland-entrepreneur-solving-problems-unique-to-his-home)

**Ethiopia (telebirr)**
- Ethio Telecom integrated telebirr with Ethiopian Airlines for online domestic tickets. During the test phase from 14 Apr 2022, 6.67M birr of tickets were sold through telebirr — [Ethio Telecom](https://www.ethiotelecom.et/ethio-telecom-launches-ethiopian-airlines-flight-ticket-online-payment-system-via-telebirr/)
- Third-party aggregators such as Chapa offer WooCommerce plugins accepting telebirr, CBE Birr and others for Ethiopian merchants — [Chapa WooCommerce plugin](https://es.wordpress.org/plugins/chapa-payment-gateway-for-woocommerce/)
- NBE's April 2020 directive opened payment instrument issuance (e-money in birr) to licensed non-bank issuers — [Capital Ethiopia, 5 Apr 2020](https://capitalethiopia.com/2020/04/05/new-directive-clears-way-for-e-payment/). A revised directive raised the wallet balance limit from Birr 30,000 to 75,000 and set a daily aggregate limit of Birr 150,000 — [NBE](https://nbe.gov.et/nbe_news/the-national-bank-of-ethiopia-has-issued-a-revised-directive-for-mobile-money-providers-to-promote-safety-competition-and-innovation/)

**Sudan / Syria / Afghanistan / Libya (sanctioned, conflict or split-authority markets)**
- Sudan: a WooCommerce plugin displays local bank or mobile-money details (e.g., Bankak, O-Cash) at checkout. Buyers upload a screenshot of the payment receipt and the store admin must manually verify it and update the order. The plugin is not affiliated with Bankak and has very low adoption — [Sudan Online Payments for WooCommerce](https://emoji.wordpress.org/plugins/sudan-online-payments-for-woocommerce/)
- Syria: a WooCommerce plugin supports Syriatel Cash, Sham Cash and MTN Cash. The merchant enters a wallet ID and QR code, and orders sit "On-Hold" until manual confirmation — [Syrian Payment Gateways for WooCommerce](https://ug.wordpress.org/plugins/syrian-payment-gateways-for-woocommerce/)
- Syria (2025–26): Sham Cash started in opposition-held Idlib and was adopted nationally for public-sector salaries from May 2025. It has had regular outages, faces security and ownership-transparency concerns, and is not on official app stores, which one expert attributes to sanctions. Most US sanctions were lifted in 2025, parts of the banking system reconnected to SWIFT, Visa and Mastercard, and cash "remains the preferred method for most consumers and merchants" — [EnterpriseAM, 24 Jun 2026](https://enterpriseam.com/menaplus/2026/06/24/syrias-banking-rebuild-creates-opening-for-fintechs-filling-the-gaps/); [Enab Baladi, May 2025](https://english.enabbaladi.net/archives/2025/05/sham-cash-app-technical-concerns-and-incomplete-benefits/amp/)
- Afghanistan: HesabPay, a Kabul wallet founded in 2016, offers a hosted checkout that merchants call server-side, with redirect and webhook status, and an official WooCommerce plugin — [HesabPay docs](https://docs.hesab.com/introduction/overview/). Sanctions, frozen assets, a paralysed banking sector and shortages of physical currency constrain liquidity — [Algorand Foundation case study](https://algorand.foundation/news/how-hesabpay-became-the-first-and-only-interoperable-digital-payments-platform-in-afghanistan)
- Libya: COD is described as the default for online purchases, with buyers ordering via Facebook and Instagram and wanting to see goods before paying (vendor blogs, weaker) — [eGrow, 2026](https://www.egrow.com/en/blog/cod-libya-ecommerce-2026). Vixio reports Libya's split central-bank structure had not been fully ended, most transactions are cash, about a third of cash is held outside banks, and an EU-backed project (2022–2025) covers instant payments, open banking and eKYC — [Vixio](https://www.vixio.com/insights/pc-libya-embarks-payment-modernisation-journey-eu-backing). Wallets and banks are described as siloed and non-interoperable (commercial source) — [TransFi](https://www.transfi.com/jp/blog/libyas-payment-rails-how-they-work---challenges-in-banking-mobile-money-card-payments)

### Inferences
- The universal first layer in these markets is COD plus "pay my wallet or account and show proof" handled by the seller. The platform records the method and the seller confirms receipt. The Sudan and Syria WooCommerce plugins, Shopify manual methods, and Somaliland's ZAAD-number-on-a-board all follow this shape.
- In single-dominant-wallet markets (Kenya/M-Pesa, Somalia/EVC, Somaliland/ZAAD, Ethiopia/telebirr), the next step was integrating the wallet's merchant collection API, with an order reference in the payment so the platform can confirm automatically. Funds still land in the seller's (or an aggregator's) own wallet account.
- Platform-branded payments (Salla electronic payments, Zid Pay, JumiaPay) appear only once a licensed PSP partner or licence exists. Salla and Zid both kept third-party gateways and COD alongside their own product rather than forcing migration.
- The Iraq path (wallet launches online payments in 2016 → central-bank licensing regime including aggregators in 2024 → licensed card and wallet issuer buys the leading marketplace in 2024) suggests that in fragmented wallet markets, the wallet or issuer may become the marketplace's owner or acquirer rather than the reverse.
- Libya's split central bank, siloed wallets and cash shortages is the closest structural analog found for Yemen's split authorities. No platform-level case study was found showing how a Libyan platform settles across the split. This is inferred relevance only.

### Gaps
- No primary source found on how Salla's own "electronic payments" is licensed: a SAMA licence in Salla's name or a licensed PSP partner. SAMA licensee news did not name Salla or Zid. Not verified.
- No official Salla article found on a "bank transfer with receipt upload" flow. Treat that pattern in Saudi Arabia as unverified, though the generic pattern is evidenced elsewhere (Sudan/Syria plugins, Shopify manual methods).
- No primary data found on COD share in Iraq, Libya, Somalia or Ethiopia.
- Could not fetch Jumia's 20-F for current wording on agent cash remittance or seller payout holds.
- No source found on Noon's COD settlement cycle or Amazon's COD remittance terms in the Gulf.
- Libya: did not verify whether the 2023 announced central bank reunification was completed. Vixio says the split persists, but its article date is unclear.

---

## KQ2. What standard legal and operational positions can a platform take in a money flow, with preconditions and risks, and what setup patterns do they produce?

### Takeaway
The legal position depends on whose money it is and when. If the platform never receives funds (record-only, or technical integrator on the seller's own account), it generally stays outside payments regulation. Once it receives and forwards funds (facilitator, aggregator, marketplace collector, escrow), regulators in the EU, UK, India, Egypt, Bangladesh and Iraq either require a licence or force the funds into a licensed party's escrow or settlement account. The marketplace commercial-agent exemption has been narrowed in Europe to platforms acting genuinely for one side only. Closed-loop store credit is exempt nearly everywhere only while it cannot be cashed out or used with third parties.

### Cited Findings

**Record-only (manual payment methods)**
- Shopify's manual payment methods (COD, money orders, bank transfers) mark orders "unpaid" until the merchant marks them paid after receiving payment. Payment instructions appear on the order confirmation page — [Shopify Help: Manual payment methods](https://help.shopify.com/en/manual/payments/manual-payments)

**Technical integrator on the seller's own provider account (Shopify Payments Apps model)**
- Shopify's payments platform is invitation-only. Partners need approval and must sign a separate revenue-share agreement. Card extensions require a PCI Attestation of Compliance. "Generally Available" status is granted on request, with example criteria of at least 50 stores and over $1,000,000 processed — [Shopify.dev: Get approved for payments](https://shopify.dev/docs/apps/build/payments/payments-extension-review)
- Extension types are credit card, custom credit card, alternative (with or without redirect), offsite (redirect to an app-hosted page) and redeemables (third-party gift cards). Supported actions are charge, authorize, capture (at purchase or at fulfilment), void, and refund initiated from Shopify admin. The merchant installs the app and configures it; the app signals readiness via API — [Shopify.dev: Extensions for payments](https://shopify.dev/docs/apps/payments)
- Egypt's PSP rules (as summarised by the IBA) distinguish "technical payment aggregators", which provide only the collection platform, from "payment facilitators", which also receive funds in their own name and settle to merchants — [IBA](https://www.ibanet.org/article/6FC3317B-4F9C-4DFC-BDF1-80CF98B68B21)

**Payment facilitator / aggregator with sub-merchants**
- Visa: a payment facilitator (PF) signs acceptance contracts with sponsored merchants on behalf of an acquirer and receives and distributes settlement for them. "Acquirers are responsible for the acts of both PFs and sponsored merchants." A PF cannot sponsor another PF, a staged digital wallet, or P2P or money-transfer activity. Sponsored merchants must be located within the acquirer's jurisdiction and may need a direct acquirer agreement above an annual sales volume (footnote excludes high-integrity-risk MCCs and merchants that conduct advance payments) — [Visa Payment Facilitator Model, 2024](https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-payment-facilitator-model.pdf)
- Egypt payment facilitators must keep a local registered office, hold customer funds in a separate account, settle in EGP, transfer received funds to merchants within three working days, and give the bank a guarantee equal to three days' collections. Banks may not contract a PSP without CBE approval — [IBA](https://www.ibanet.org/article/6FC3317B-4F9C-4DFC-BDF1-80CF98B68B21). Date caveat: the IBA article appears to describe the pre-2025 framework. The CBE issued new PSP licensing rules effective 17 June 2025 with a 12-month transition — [Baker McKenzie](https://insightplus.bakermckenzie.com/bm/banking-finance_1/egypt-new-regulation-on-payment-solutions); [LaunchBase Africa, 24 Jun 2025](https://launchbaseafrica.com/2025/06/24/the-rulebook-for-egypts-fintech-startups-has-changed-heres-how-to-get-licensed/?amp=1)
- India: RBI's 2020 PA/PG guidelines required e-commerce marketplaces performing payment aggregation to stop or separate that activity by 30 June 2021. Authorised PAs moved from bank "nodal accounts" to at most two escrow accounts. The rules do not apply to delivery-versus-payment transactions, only to advance payment with deferred delivery — [Trilegal](https://trilegal.com/knowledge-repository/rbis-guidelines-on-regulation-of-payment-aggregators-and-payment-gateways/); [Law.asia](https://law.asia/payment-regulations-nodals-licences/); [RBI notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12050)
- Iraq's 2024 regulation explicitly lists payment aggregation as a licensed electronic payment service — [vLex](https://vlex.com/vid/electronic-payment-service-companies-1090421790)

**Marketplace commercial-agent exemption (EU/UK)**
- EBA Q&A 2020_5355: a B2C platform may be excluded from PSD2 if, as a commercial agent, "it is authorised by the payee to negotiate or conclude the sale of goods or services" and "does not also act on behalf of the payer". Competent authorities assess each business model — [EBA Q&A 2020_5355](https://eba.europa.eu/single-rule-book-qa/qna/view/publicId/2020_5355)
- EBA Q&A 2020_5354: a platform settling the payer's debt "is not in itself to be a reason to exclude" it; treating it so would weaken buyer and seller protection and distort competition — [EBA Q&A 2020_5354](https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2020_5354)
- UK FCA: the exclusion needs a commercial agent with formal authority to negotiate or conclude, acting for payer or payee "but not both". Authority means the ability to bind the principal. A business is likely acting for both if payments go "into an account that it controls or manages before being sent to the payee" (page updated 17 Feb 2023) — [FCA: Commercial agent exclusion](https://www.fca.org.uk/firms/commercial-agent-exclusion-cae)
- Commentary on PERG 15.5 Q33A: an escrow provider holding funds pending the payee's fulfilment of conditions falls outside the exclusion (secondary interpretation) — [Bratby Law](https://bratby.law/practice-areas/payments-regulation/psrs-2017-perimeter-exclusions/)
- The EBA flagged inconsistent national application of the exclusion and proposed clarifying it in PSD3 — [Sidley, Jul 2022](https://www.sidley.com/en/insights/newsupdates/2022/07/psd3-what-to-expect-based-on-the-european-banking-authority-opinion)

**Collection agent / agent of the payee (US analog)**
- Federal FinCEN rules have no "agent of payee" exemption as such. Instead they exclude "payment processors" when there is a formal agreement with the payee (seller or creditor) and the processor runs through clearing systems that admit only BSA-regulated institutions. About 22 US states have express agent-of-payee exemptions — [Modern Treasury](https://moderntreasury.com/learn/what-is-an-agent-of-the-payee-exemption)
- California's DFPI has held that a payment processing service was not exempt as agent of the payee, showing state-level variance — [DFPI opinion letter, 14 Nov 2018](https://dfpi.ca.gov/wp-content/uploads/sites/337/2019/03/11-14-18-Payment-processing-service-not-exempt-as-agent-of-payee-or-factoring.pdf)

**Escrow / regulator-mandated holding**
- Bangladesh Bank (30 June 2021): payment gateways hold buyers' advance payments and release to the e-commerce company only after it submits delivery documents that the gateway checks. The commerce ministry also asked that banks stop accepting direct customer deposits into e-commerce company accounts because some firms were bypassing escrow — [TBS News](https://www.tbsnews.net/economy/no-more-direct-payments-e-commerce-accounts-293197)

**Closed-loop store credit / wallet vs licensed e-money**
- India: closed-system PPIs are issued by an entity for purchases from that entity only and do not allow cash withdrawal. Their issuance "is not classified as a payment system requiring approval" — [RBI Master Directions on PPIs](https://rbi.org.in/scriptS/BS_ViewMasDirections.aspx?id=12156)
- EU: PSD2 Article 3(k) excludes instruments usable only at the issuer's premises, within a limited network under direct commercial agreement, or for a very limited range of goods. EBA Guidelines (final 24 Feb 2022, applying from 1 June 2022) tighten the assessment, and excluded issuers above EUR 1M per 12 months must notify the authority — [EBA press release](https://www.eba.europa.eu/eba-publishes-final-guidelines-limited-network-exclusion-under-payment-services-directive); [Loyens & Loeff](https://www.loyensloeff.com/insights/news--events/news/eba-guidelines-on-the-limited-network-exclusion-under-psd2/)
- Daraz Wallet (Pakistan): COD refunds go to the wallet; only the refund portion is withdrawable, while deposits and bonuses are spend-only (search snippet) — [Daraz Wallet](https://www.daraz.pk/daraz-wallet/)
- Amazon Pay (India): delivery agents on COD orders can load extra cash or change into the buyer's Amazon Pay balance. This is limited to video-KYC'd customers, up to Rs 50,000 a month (2023); the 2018 version allowed up to INR 10,000 — [About Amazon India, Jun 2023](https://www.aboutamazon.in/news/retail/need-to-deposit-2-000-notes-amazon-pay-has-a-doorstep-solution); [MediaNama, Jan 2018](https://www.medianama.com/2018/01/223-amazon-rolls-out-doorstep-cash-pickup-for-adding-money-to-amazon-pay/)
- Licensed e-money examples: Somalia's CBS licensed Hormuud's mobile money in 2021 — [CBS](https://centralbank.gov.so/wp-content/uploads/2021/11/PRESS-STATEMENT.pdf); SAMA licenses e-wallet institutions — [SAMA](https://sama.gov.sa/en-US/ApplyLicense/Pages/Payment_Forms.aspx); NBE licenses payment instrument issuers — [Capital Ethiopia](https://capitalethiopia.com/2020/04/05/new-directive-clears-way-for-e-payment/)

**Reference-code cash payment networks**
- Fawry: the merchant generates a reference, the buyer pays cash at an agent, payment stays pending until then, and the reference expires after 7 days — [EBANX](https://docs.ebanx.com/docs/payments/guides/accept-payments/api/egypt/fawry)
- M-Pesa Paybill: the account number carries the order ID. Malformed references (hyphens, slashes, spaces) can leave payments in suspense for manual reconciliation (weaker source) — [paybillke.com](https://paybillke.com/guides/mpesa-for-online-businesses-2026); [paybillke.com example](https://paybillke.com/paybill/copia-kenya)

### Inferences — SETUP PATTERN CATALOG
Each pattern lists: roles; who acquires the buyer's proof; who establishes the outcome; who holds money and for how long; how money reaches the seller; reversals and disputes; licence or partner needed; typical evolution. Facts are cited above. The synthesis below is inference unless a source is given.

**P1. Record-only manual method (seller-collected)**
- Roles: buyer, seller, seller's bank or wallet. Platform records only.
- Buyer proof: the seller receives it (cash in hand, wallet SMS, bank credit).
- Outcome: the seller marks the order paid ([Shopify](https://help.shopify.com/en/manual/payments/manual-payments)).
- Money held by: never the platform. The seller holds it from receipt.
- Payout: none needed; the money is already with the seller.
- Reversals: off-platform between buyer and seller. The platform can only record them.
- Licence: none for the platform.
- Evolution: the default start everywhere. Platforms later add proof capture (P2) and integrations (P3).

**P2. Manual transfer + uploaded proof (receipt or screenshot) verified by the seller**
- Roles: buyer, seller, buyer's and seller's wallets or banks. Platform hosts the upload.
- Buyer proof: the platform acquires a screenshot or reference number, but it is only an assertion.
- Outcome: the seller confirms after checking their own wallet or bank statement ([Sudan plugin](https://emoji.wordpress.org/plugins/sudan-online-payments-for-woocommerce/); [Syria plugin](https://ug.wordpress.org/plugins/syrian-payment-gateways-for-woocommerce/)).
- Money held by: the seller's account, immediately.
- Payout: direct.
- Reversals: off-platform.
- Risk: forged screenshots and alerts. Nigerian fraud schemes use fake credit alerts to get goods released before funds clear — [Dubawa](https://dubawa.org/four-bank-credit-alert-schemes-scammers-have-used-to-defraud-victims/?amp=1).
- Licence: none for the platform.
- Evolution: replaced by API confirmation (P3/P4) where the wallet offers merchant APIs.

**P3. Technical integrator on the seller's own provider account (Shopify Payments Apps style; Egypt's "technical aggregator")**
- Roles: buyer, seller, the seller's PSP, wallet or bank merchant account. Platform supplies checkout UI and order-state sync.
- Buyer proof: the provider acquires it (authorisation, wallet PIN, STK push).
- Outcome: the provider sends a callback or API result and the platform records it.
- Money held by: the provider on the seller's merchant account, for the provider's own settlement cycle.
- Payout: provider to the seller.
- Reversals: refunds are initiated in the platform UI and executed by the provider; disputes follow the provider's rules ([Shopify.dev](https://shopify.dev/docs/apps/payments)).
- Licence: the platform needs none, but each provider must be licensed and must onboard the seller (KYC) itself. Shopify gates partners by invitation, revenue share and PCI ([Shopify.dev](https://shopify.dev/docs/apps/build/payments/payments-extension-review)).
- Weakness: each seller must open their own merchant account with each wallet, which is friction in fragmented wallet markets.
- Evolution: this is where Salla and Zid started with third-party gateways (Moyasar, HyperPay, Tap, PayTabs), and where single-wallet integrations sit (ZainCash 2016, HesabPay, Chapa/telebirr, M-Pesa Daraja).

**P4. Payment facilitator / aggregator with sub-merchants (platform or its partner is the PF)**
- Roles: acquirer or wallet operator (sponsor), PF (platform or licensed partner), sub-merchant sellers, buyer.
- Buyer proof: the PSP or wallet acquires it.
- Outcome: the PSP establishes it.
- Money held by: the PF or its partner, in a segregated or escrow account, for 1 to 7 days (Egypt PF max 3 working days; Salla daily, 48h or weekly by plan; India escrow accounts).
- Payout: the PF nets fees and pays sellers on a schedule.
- Reversals: the PF debits the seller balance. The acquirer stays liable for PF and sub-merchant acts ([Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-payment-facilitator-model.pdf)).
- Licence: a PSP or aggregator licence (Iraq 2024, Egypt, India), or operating under a licensed partner's licence (Zid Pay terms say it works "through payment service providers"). The PF must do sub-merchant KYC and hold a reserve or guarantee (Egypt: 3 days' collections).
- Evolution: Salla's built-in electronic payments and Zid Pay sit here. JumiaPay functions similarly for Jumia sellers (inference).

**P5. Marketplace collection with escrow-style hold and payouts (platform as collector for sellers)**
- Roles: buyer, platform (marketplace), PSP or bank holding the collection account, sellers, often platform-run logistics.
- Buyer proof: the PSP for prepaid orders; the courier for COD.
- Outcome: the platform decides, using delivery events and the return window.
- Money held by: the platform or its escrow bank from payment until delivery plus the return window, then the payout cycle. Daraz moved from 14 to 7 days ([Pakistan Observer](https://pakobserver.net/dawood-appreciates-darazs-contribution-to-ecommerce-industry/)).
- Payout: periodic net settlement to the seller's bank or wallet, after commissions and return deductions.
- Reversals: the platform refunds the buyer, often into a platform wallet (Daraz), and claws back from the seller balance.
- Licence: in the EU/UK this is generally regulated unless the platform genuinely acts only for the seller (EBA/FCA above). India forced marketplaces to separate PA activity by 2021 ([Trilegal](https://trilegal.com/knowledge-repository/rbis-guidelines-on-regulation-of-payment-aggregators-and-payment-gateways/)). Bangladesh put the hold at the gateway, not the marketplace ([TBS](https://www.tbsnews.net/economy/no-more-direct-payments-e-commerce-accounts-293197)).
- Risk: commingling of buyer funds (Evaly, see KQ4).

**P6. Commercial-agent / collection-agent of the seller (agent-of-payee)**
- Roles: buyer, seller (principal), platform as the seller's agent with formal authority. A payout bank sits behind it.
- Buyer proof: the platform or its PSP acquires it.
- Outcome: payment to the agent discharges the buyer's debt to the seller. This is the key legal feature in US agent-of-payee exemptions ([Modern Treasury](https://moderntreasury.com/learn/what-is-an-agent-of-the-payee-exemption)).
- Money held by: the platform as agent, briefly. Payout: the agent remits to the principal.
- Reversals: the seller remains liable; the agent processes refunds for the seller.
- Preconditions: formal agency agreement with the seller only; real authority to negotiate or conclude; no acting for the buyer (no escrow-for-buyer promises). The FCA treats funds held in a platform-controlled account before payee settlement as acting for both sides ([FCA](https://www.fca.org.uk/firms/commercial-agent-exclusion-cae); [EBA 2020_5355](https://eba.europa.eu/single-rule-book-qa/qna/view/publicId/2020_5355)).
- Risk: the exemption is narrow and jurisdiction-specific. Its existence in a given non-EU or non-US market cannot be assumed (inference).

**P7. Platform-run COD (own or 3PL couriers collect cash for the marketplace)**
- Roles: buyer, courier or delivery agent, platform (or its logistics arm), seller.
- Buyer proof: the courier acquires cash and a proof of delivery.
- Outcome: the courier's delivery event, reconciled by the platform.
- Money held by: the courier until remittance, then the platform until the seller payout. Jumia found late remittances and unrecoverable receivables from 3PL agent fraud or insolvency ([Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)).
- Payout: the platform nets and pays the seller on its cycle.
- Reversals: refusal means the parcel returns and no money moves. Returns after payment are refunded by bank deposit, voucher or wallet ([Daraz BD](https://www.daraz.com.bd/refunds-policy/); [Daraz PK](https://www.daraz.pk/refund-policy/)).
- Licence: often treated as outside payments regulation as delivery-versus-payment (India's PA rules exclude DvP), but couriers can become tax agents (Pakistan 2025).

**P8. Courier COD remittance as a service (merchant ↔ courier contract; platform integrates waybills and ledger)**
- Roles: buyer, courier (collector), seller. Platform is the waybill and ledger integrator, sometimes the remittance conduit (Salla wallet).
- Buyer proof: the courier acquires it. Outcome: courier delivery status.
- Money held by: the courier, then possibly the platform wallet. Salla pays COD balances twice weekly ([Salla](https://help.salla.sa/en/article/manage-cash-on-delivery-salla-waybills/nonfrowzfu421ewhv6klylv6)); Bosta advertises next day ([Bosta](https://apps.shopify.com/bosta-shipping-app)); Shiprocket's standard cycle is about 7–9 days ([Shiprocket](https://shiprocket.in/blog/early-cod-by-shiprocket)).
- Payout: bank transfer from the courier or platform.
- Reversals: refused parcels return to the seller; shipping fees are usually charged.
- Licence: the courier's own; the platform needs none if it only integrates. When the platform pays out COD from its own wallet it moves toward P5/P7 (inference).

**P9. COD receivables financing / early remittance (lender role)**
- Roles: courier-fintech or lender, seller, courier.
- Mechanism: the lender advances part or all of expected COD before the courier remits. Shiprocket Early COD costs 0.99% for D+2, 0.69% for D+3 and 0.49% for D+4. Shiprocket "Instant COD" pays up to 70% the day after shipping for up to 5% ([Shiprocket support](https://support.shiprocket.in/support/solutions/articles/152000000970-instant-cod-faqs)). PostEx in Pakistan pays merchants upfront on COD and runs its own fleet to cut failures ([Profit, Oct 2021](https://profit.pakistantoday.com.pk/2021/10/05/pakistans-fintech-postex-raises-1-5mn-for-its-cod-financing-and-logistics-platform)).
- Licence: lending licence. PostEx was "awaiting NBFC license" in 2022 ([Profit, Aug 2022](https://profit.pakistantoday.com.pk/2022/08/30/postex-acquires-call-courier-to-expand-its-logistics-network-awaits-nbfc-license)).

**P10. Digital pay-on-delivery (wallet, QR, card mPOS or credit at the door)**
- Roles: buyer, courier with a device or QR, PSP, wallet or lender, platform.
- Buyer proof: the PSP or wallet acquires it at the door. This removes cash custody from the courier.
- Examples: JumiaPay on delivery in Nigeria and Kenya ([TechCrunch](https://techcrunch.com/2024/05/07/jumia-is-back-growing-total-sales-and-orders-in-q1-2024)); ShipBlu/PayTabs/Valu "Payment-on-Delivery" with credit, cards, QR and e-wallets ([WAYA](https://waya.media/valu-paytabs-and-shipblu-partner-to-streamline-e-commerce/)); Mastercard mPOS at Jumia (2017).
- Licence: the PSP's. The platform acts as P3 or P4.

**P11. Closed-loop store credit / platform wallet (refunds, change, top-ups) vs licensed e-money**
- Roles: platform as issuer of spend-only credit.
- Uses: COD refunds into the wallet (Daraz PK), change or top-up loaded by couriers (Amazon Pay, under a KYC'd regime).
- Exemption precondition: no cash-out, no third-party use, limited network ([RBI](https://rbi.org.in/scriptS/BS_ViewMasDirections.aspx?id=12156); [EBA](https://www.eba.europa.eu/eba-publishes-final-guidelines-limited-network-exclusion-under-payment-services-directive)).
- Risk: allowing withdrawal or P2P, or use at other merchants, turns it into e-money needing a licence. Daraz limits withdrawal to the refund portion.

**P12. Reference-code cash payment network (Fawry-type) or wallet bill-pay reference**
- Roles: buyer, agent network (kiosks or stores), network operator (aggregator), merchant or platform.
- Buyer proof: the network operator acquires it at the agent.
- Outcome: the network sends a callback when the reference is paid; the reference expires if unpaid (7 days at Fawry).
- Money held by: the operator until settlement to the merchant (cycle not found).
- Reversals: generally merchant-side refunds; no chargeback concept (inference).
- Licence: the operator's. The platform integrates as P3, or as P4 if the platform is the merchant of record.

**P13. Licensed wallet or issuer owns or embeds the marketplace (super-app)**
- Example: QiCard acquires Miswag (2024), which becomes a SuperQi mini-app with BNPL ([Iraq Business News](https://www.iraq-businessnews.com/2024/12/03/qicard-acquires-miswag/)).
- Proof, holding and payout all sit inside the licensed issuer, so the platform inherits the licence.

**P14. Lender / BNPL at checkout or at the door**
- Examples: Tabby and Tamara on Salla ([Salla](https://help.salla.sa/en/article/manage-payment-methods/dtdojcntv3f4lwqzj4h0jvij)); Qi instalments on Miswag ([App Store](https://apps.apple.com/mx/app/miswag/id1025309304)); Valu on ShipBlu ([WAYA](https://waya.media/valu-paytabs-and-shipblu-partner-to-streamline-e-commerce/)).
- The lender pays the merchant and holds the credit risk. The platform is an integrator.

### Gaps
- Could not retrieve FCA PERG 15.5 Q33A text directly. The escrow point rests on secondary commentary.
- No source found on how the commercial-agent concept is treated in Arab or MENA payment laws. Its availability outside the EU/UK/US is unknown.
- Egypt: the full 2025 CBE rulebook was not read. The PF obligations cited come from an IBA article that may describe the earlier framework.
- No source found on Fawry's merchant settlement cycle or refund mechanics.

---

## KQ3. How do COD-heavy platforms manage courier cash remittance, reconciliation, refusal rates and seller payout timing?

### Takeaway
COD platforms treat cash as a receivable owed by couriers. Documented failures (Jumia Kenya 2018) led to daily automated cash monitoring. Remittance cycles range from next-day (Bosta) through twice-weekly (Salla) to about 7–9 days (Shiprocket standard) and 7–14 days for marketplace seller payouts (Daraz). Refusals and failed deliveries are the main cost: 14.4% of Jumia GMV in 2018, and roughly 20–30% RTO on COD versus single digits on prepaid in India per vendor data. Mitigations include COD fees and limits, blocking repeat refusers, pickup points, digital pay-on-delivery, and paid early remittance.

### Cited Findings
- Jumia found in early 2018 that about $800,000 of cash payments in Kenya had never been collected. It then moved to an automated system for daily monitoring of cash transactions — [Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)
- Late collections from third parties and unrecoverable receivables from delivery-agent fraud or insolvency were problems where deliveries were outsourced — [Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)
- In 2018, 14.4% of Jumia's GMV was failed deliveries and customer returns. Jumia returns products to the seller after three failed delivery attempts. Cash-paying customers must be present, which raises failures — [Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)
- Many SME sellers lack bank accounts, and payout frequency and destination restrictions delayed seller payments. Caribou recommends flexible payout frequency and mobile-money payout destinations — [Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)
- Salla COD controls: per-carrier COD fee, min/max cart value, weight caps, product exclusions, and hiding COD from customers blocked by other Salla stores (a cross-merchant refusal blocklist). COD balances are paid Sundays and Wednesdays. A per-transaction ledger is exportable — [Salla Help](https://help.salla.sa/en/article/manage-cash-on-delivery-salla-waybills/nonfrowzfu421ewhv6klylv6)
- Shiprocket's standard COD remittance is about 7–9 days after delivery. Early COD is paid for (0.49% to 0.99%) and the plan is locked for 30 days once activated — [Shiprocket blog](https://shiprocket.in/blog/early-cod-by-shiprocket)
- Bosta advertises next-day COD transfers — [Bosta Shopify listing](https://apps.shopify.com/bosta-shipping-app)
- India RTO benchmarks: 20–25% overall RTO, with refusal a common cause — [Razorpay](https://razorpay.com/blog/return-to-origin-challenges-and-how-to-solve-it/). COD RTO is 25–30% versus 4–8% for prepaid (vendor benchmark, weaker) — [EasySell](https://easysellapp.com/blogs/wiki/cod-conversion-rate-benchmarks-by-country-2026). The same vendor gives Pakistan first-attempt delivery failure of 15–30% depending on courier and region, and Egypt COD at about 51% of online transactions (weaker).
- Iraq: COD lets buyers refuse at the door or place multiple fake orders, and ties up seller cash flow — [IraqTech](https://iraqtech.io/an-analysis-on-the-rise-of-e-commerce-in-iraq/)
- Pakistan: from 1 July 2025 couriers deduct 2% withholding tax from COD before remitting to sellers — [KPMG](https://assets.kpmg.com/content/dam/kpmg/pk/pdf/2025/07/A-Brief-on-Finance-Act-2025.pdf); [Profit](https://profit.pakistantoday.com.pk/2025/09/03/online-marketplaces-and-couriers-barred-from-serving-unregistered-sellers)
- PostEx targeted slow COD cash recovery and last-mile failures in a market where "more than 90% of e-commerce payments" were cash (2021). In 2022 it acquired Call Courier to own delivery — [Profit, Oct 2021](https://profit.pakistantoday.com.pk/2021/10/05/pakistans-fintech-postex-raises-1-5mn-for-its-cod-financing-and-logistics-platform); [Profit, Aug 2022](https://profit.pakistantoday.com.pk/2022/08/30/postex-acquires-call-courier-to-expand-its-logistics-network-awaits-nbfc-license)
- Amazon India lets COD delivery agents load leftover change or extra cash to a KYC'd buyer's Amazon Pay balance, converting surplus cash at the door into stored value — [About Amazon India](https://www.aboutamazon.in/news/retail/need-to-deposit-2-000-notes-amazon-pay-has-a-doorstep-solution)

### Inferences
- The COD ledger needs three linked records per order: courier-collected (proof of delivery plus amount), courier-remitted (batch), and seller-settled (net of fees, COD fee, returns, tax). Salla's exportable COD ledger and Jumia's daily monitoring both implement this. A Yemen platform on courier COD should treat each courier as a counterparty with an exposure limit.
- Refusal is a platform-wide risk, not a per-seller one. Salla's cross-store blocklist shows a platform can add value no single seller can: shared buyer-reliability signals.
- Paid early remittance (Shiprocket) and COD advances (PostEx) show that payout timing can become a revenue line or a lender partnership. This requires the platform or lender to trust courier remittance data.
- When couriers hold cash for days, the courier is the de facto money holder. In Pakistan, government recognised this by making couriers tax withholding agents.

### Gaps
- No official Jumia, Daraz or Noon documents found giving current seller payout cycles for COD orders, or reserve or holdback rules.
- No country-specific refusal rates found from primary sources for Egypt, Iraq, Saudi Arabia or Somalia. The figures available are vendor estimates.
- No data on courier insolvency or loss events beyond Jumia 2018.

---

## KQ4. What staged evolution paths did platforms follow, what triggered each step, and what mistakes or failures are documented?

### Takeaway
The typical path is: COD and record-only manual methods → integrations with dominant wallets or PSPs on sellers' or partners' accounts → a platform-branded payment layer as facilitator through a licensed partner, with platform-netted COD → own licence or merger with a licensed issuer. Each step was triggered by scale, cash losses, regulation, or partner availability. The worst documented failures came from platforms that collected advance payments into their own accounts without segregation (Evaly in Bangladesh, 2021), which triggered forced escrow-at-gateway rules. Operational failures came from courier cash leakage (Jumia 2018). Some steps were reversed: Jumia cut its JumiaPay App digital products in 2025 for weak economics.

### Cited Findings
- **Jumia path:** ~95% COD in Kenya in 2016 → own logistics (92% of deliveries in 2018) plus daily cash monitoring after the $800k shortfall ([Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)) → JumiaPay prepaid and JumiaPay on delivery (32.5% of physical orders in Q1 2024) ([TechCrunch](https://techcrunch.com/2024/05/07/jumia-is-back-growing-total-sales-and-orders-in-q1-2024)) → 2025 retreat from JumiaPay App digital products ("limited revenue impact"), with gateway transactions down 30% while TPV rose 19% to $232.2M on GMV of $818.6M ([Jumia Q4 2025](https://s205.q4cdn.com/370993272/files/doc_financials/2025/q4/Jumia-EX-99-1-Q4-2025-2-10-2026-Final-v5.pdf))
- **Daraz path:** ~80% COD → nearly 20% prepaid by 2025 ([Aurora](https://aurora.dawn.com/news/1143493); [ProPakistani](https://propakistani.pk/2025/09/12/a-decade-of-daraz-pakistan-pioneering-e-commerce-and-shaping-access-trust-and-opportunity/amp/)). COD refunds routed to a closed-loop Daraz Wallet in Pakistan ([Daraz PK](https://www.daraz.pk/refund-policy/)). Seller cycle shortened from 14 to 7 days ([Pakistan Observer](https://pakobserver.net/dawood-appreciates-darazs-contribution-to-ecommerce-industry/))
- **Saudi SaaS path (Salla/Zid):** COD plus third-party gateway partnerships (PayTabs–Zid; Salla with Moyasar, HyperPay, Tap) → platform-branded payments with plan-based settlement (Salla electronic payments; Zid Pay "through payment service providers") and platform-issued courier waybills with COD netted in the platform wallet → BNPL integrations ([Salla](https://help.salla.sa/en/article/manage-payment-methods/dtdojcntv3f4lwqzj4h0jvij); [Zid](https://zid.sa/en/legal/zidpay-terms-conditions-kw); [PayTabs](https://paytabs.com/?p=16032)). The market trigger was the falling COD preference and mada e-commerce growth ([Gulf Business](https://gulfbusiness.com/en/2024/retail/e-commerce-drives-mena-digital-payments); [Arab News](https://www.arabnews.com/node/2589350/business-economy))
- **Iraq path:** COD → ZainCash online payments in 2016 ([TelecomTV](https://telecomtv.com/content/tracker/iraq-wallet-expands-zaincash-service-to-boost-e-commerce-with-country-s-first-online-payment-solution-23106)) → CBI Regulation No. 2 of 2024 licensing aggregators ([vLex](https://vlex.com/vid/electronic-payment-service-companies-1090421790)) → QiCard acquires Miswag, adding a super-app mini-app and BNPL ([Iraq Business News](https://www.iraq-businessnews.com/2024/12/03/qicard-acquires-miswag/))
- **India regulatory trigger:** marketplaces collecting through 2009-era nodal accounts were required under the 2020 PA/PG guidelines to separate PA activity by 30 June 2021 and use escrow accounts — [Trilegal](https://trilegal.com/knowledge-repository/rbis-guidelines-on-regulation-of-payment-aggregators-and-payment-gateways/)
- **Egypt path:** Fawry bill-pay switch in 2008 → e-commerce reference codes ([TechCabal](https://techcabal.com/2026/04/20/how-fawry-built-a-profitable-fintech/); [EBANX](https://docs.ebanx.com/docs/payments/guides/accept-payments/api/egypt/fawry)) → bank-sponsored PSP rules separating technical aggregators from facilitators ([IBA](https://www.ibanet.org/article/6FC3317B-4F9C-4DFC-BDF1-80CF98B68B21)) → 2025 CBE PSP licensing rules with a 12-month transition ([Baker McKenzie](https://insightplus.bakermckenzie.com/bm/banking-finance_1/egypt-new-regulation-on-payment-solutions)) → courier-led digital pay-on-delivery with credit, 2024 ([WAYA](https://waya.media/valu-paytabs-and-shipblu-partner-to-streamline-e-commerce/))
- **Nigeria path:** Paystack payment links for merchants without developers (2015–16) → Stripe acquisition in 2020 with 60,000+ businesses — [Wikipedia](https://en.wikipedia.org/wiki/Paystack); [How We Made It In Africa](https://www.howwemadeitinafrica.com/the-nigerian-entrepreneur-behind-africas-response-to-paypal-and-stripe/84780/)
- **Somalia regulatory step:** mobile money operated with limited regulation until the CBS issued the first licence (Hormuud) on 27 Feb 2021 — [CBS](https://centralbank.gov.so/wp-content/uploads/2021/11/PRESS-STATEMENT.pdf)
- **Failure: Evaly (Bangladesh), the advance-payment model.** A Bangladesh Bank inspection found liabilities of Tk403.80 crore against current assets of Tk65.17 crore, and Tk213.94 crore of customer advance payments with undelivered products. Discounts below cost were funded by new customers' prepayments — [Daily Star](https://www.thedailystar.net/business/economy/e-commerce/news/evaly-has-no-money-pay-back-2182056); [TBS](https://www.tbsnews.net/node/304822). Banks suspended card use for advance payments to Evaly and nine others — [TBS](https://www.tbsnews.net/node/266947). The commerce ministry instructed Evaly to follow cash on delivery (headline) — [TBS](https://www.tbsnews.net/node/213748)
- **Policy response to Evaly:** Bangladesh Bank escrow-at-gateway, 30 June 2021 ([TBS](https://www.tbsnews.net/economy/no-more-direct-payments-e-commerce-accounts-293197)). The draft Digital Commerce Operational Guideline set delivery in 5 days (same city) or 10 days (elsewhere) after advance payment, and refunds within 7 days via the same channel — [TBS](https://www.tbsnews.net/economy/e-commerce-cos-must-deliver-products-within-5-days-268159)
- **Aftermath:** in Dec 2021 Bangladesh Bank instructed gateways to start refunding. Advance payments of Tk512 crore were stuck with gateways — [Dhaka Tribune](https://www.dhakatribune.com/business/317441/bb-instructs-payment-gateways-to-start-paying-back). In Nov 2021 the High Court sought an explanation of Bangladesh Bank's inaction on refunds — [Financial Express](https://old.thefinancialexpress.com.bd/national/hc-seeks-bb-report-over-inaction-of-gateways-in-refunding-buyers-money-1636292328)
- **Failure: Jumia cash leakage.** About $800k in uncollected COD cash (Kenya, early 2018) — [Caribou](https://caribou.global/publications/how-financial-exclusion-and-lack-of-trust-hamper-e-commerce-platform-models/)
- **Failure / risk: wallet reliability.** Sham Cash in Syria has had outages during salary periods, frozen accounts, missing two-factor authentication on transfers, and no app-store listing — [EnterpriseAM](https://enterpriseam.com/menaplus/2026/06/24/syrias-banking-rebuild-creates-opening-for-fintechs-filling-the-gaps/); [Enab Baladi](https://english.enabbaladi.net/archives/2025/05/sham-cash-app-technical-concerns-and-incomplete-benefits/amp/)
- **Regulatory dependency risk:** PostEx was operating a COD-advance lending book while "awaiting NBFC license" in 2022 — [Profit](https://profit.pakistantoday.com.pk/2022/08/30/postex-acquires-call-courier-to-expand-its-logistics-network-awaits-nbfc-license)
- **Card-scheme constraint:** Visa notes that merchants conducting advance payments are a carve-out category in its PF sponsorship rules, which flags prepay-before-delivery as higher risk in the scheme's view — [Visa PF Model](https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-payment-facilitator-model.pdf)

### Inferences
- **Generic staged path transferable to a new market (inference from the cases above):**
  1. Record-only plus courier COD (P1, P2, P8). No licence. The platform builds an order and payment state machine and a COD ledger.
  2. Integrations on sellers' own wallet or bank accounts (P3, P12). No platform licence; the wallets are the licensed parties.
  3. Platform-branded collection through a licensed partner acting as PF or aggregator (P4), plus platform-netted courier COD (P7, P8 with a wallet), plus a closed-loop refund wallet (P11).
  4. Own licence, or merger or partnership with a licensed issuer (P13). Lending partners for COD advances and BNPL (P9, P14).
- **Triggers observed:** cash losses and courier leakage (Jumia) led to automation. Regulator action after consumer losses (Evaly, Bangladesh) led to mandated escrow at licensed gateways. Regulator perimeter reform (India 2020; Egypt 2025; Iraq 2024) forced separation or licensing. Wallet maturity and new licensing (Somalia 2021; Ethiopia 2020) enabled integrations. The economics of digital-product volume (Jumia 2025) led to retrenchment.
- **Key lesson:** the moment a platform takes buyer prepayments into its own account and pays sellers later, it carries regulatory and failure risk. In Evaly's case this ended in central-bank-imposed escrow and customer losses. Holding prepaid funds at a licensed third party (gateway or wallet) with delivery-conditioned release is the pattern regulators converged on in Bangladesh and India.
- **Mistake to avoid:** building payment features whose volume does not support the core commerce economics (Jumia's 2025 JumiaPay App de-emphasis).

### Gaps
- No documented case of a platform operating across two rival central-bank jurisdictions within one country (the Yemen split). Libya is the nearest analog, but no platform-level account was found.
- No details found on whether Jumia or Daraz hold their own payment licences in each market, or operate under partners.
- No primary documentation found for Salla's or Zid's licensing timeline with SAMA.
- Final gazetted text of Bangladesh's Digital Commerce Operational Guideline 2021 not reviewed. Delivery and refund windows come from draft-stage reporting, and sources conflict.
