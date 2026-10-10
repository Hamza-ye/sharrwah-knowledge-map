# Sana'a-side rules: source search notes (pass A)

Search date: 2026-10-10. Companion table: `A_rules.tsv` (rows A001–A083). This file lists sources only. It does not give analysis or recommendations.

## Access conditions observed from this container

- `centralbank.gov.ye`, `www.centralbank.gov.ye` and `ftp.centralbank.gov.ye` reset the connection over https (curl error 35). Over http, `centralbank.gov.ye` and `ftp.centralbank.gov.ye` return 503. WebFetch also got 503.
- `saba.ye` returns 403 to both curl and WebFetch.
- `moit.gov.ye` / `www.moit.gov.ye` **answered 200** on most requests. The site has been rebuilt on Drupal 10 as the "Ministry of Economy, Industry and Investment" site. A few requests for PDFs were reset and succeeded on retry, so access is intermittent. `e-moit.gov.ye` (the e-services portal) reset the connection.
- `tax.gov.ye` (now the merged Tax and Customs Authority site) answered 200. `zakat.gov.ye` / `gaz.gov.ye` returned proxy 502 (CONNECT tunnel failed).
- Archives: `web.archive.org` resets the connection, and WebFetch refuses it. `archive.ph` resets. The Common Crawl index reset or returned 504. Only the `archive.org/wayback/available` API worked, and it rate-limits (429). Archive URLs in the TSV come from that API's closest snapshot. "none" means the API reported no snapshot for that exact URL. "not determined" means the API kept returning 429 for that URL. That applies to 21 rows:
- A004, a central bank page blocked here.
- Ministry files A041–A051 and A057, reachable here.
- Tax files A069, A070, A073 and A075, reachable here.
- Yemen Eco items A031, A036, A038 and A052, reachable here.

The three image rows were not checked.
- Several Sana'a-side outlets were reachable: althawrah.ye (state daily), 26sep.net, yemeneco.org (its WordPress REST API also works), yemen-yba.com / yba.org.ye (Yemen Banks Association) and yemen-nic.info (National Information Center).

## Queries run

WebSearch, Arabic first (the `[site:]` prefix marks searches restricted with allowed_domains; `(ext)` marks extended mode):
1. البنك المركزي صنعاء تعميم المحافظ الإلكترونية
2. قرار رقم 1 لسنة 2020 النقود الإلكترونية البنك المركزي
3. centralbank.gov.ye تعليمات الدفع الإلكتروني
4. بنك الكريمي صنعاء إيقاف التعامل 2025 البنك المركزي
5. [site:centralbank.gov.ye] البنك المركزي اليمني تعميم شركات الصرافة المحافظ
6. [site:centralbank.gov.ye] النقود الإلكترونية قرار إصدار
7. [site:centralbank.gov.ye] خدمات الدفع الإلكتروني عبر الهاتف المحمول القواعد التنظيمية
8. [site:centralbank.gov.ye] منشور دوري البنوك تعميم 2025
9. [site:centralbank.gov.ye] شركات خدمات الدفع الإلكتروني المرخصة البنك المركزي اليمني
10. [site:centralbank.gov.ye] الكريمي
11. [site:centralbank.gov.ye] قرار محافظ البنك المركزي حظر التعامل
12. [site:centralbank.gov.ye] centralbank.gov.ye pdf تعليمات
13. [site:centralbank.gov.ye] القرارات البنك المركزي اليمني قرار رقم لسنة 1446
14. [site:centralbank.gov.ye] انظمة المدفوعات قرار محافظ البنك المركزي رقم (4) لسنة 1445
15. [site:centralbank.gov.ye] وحدة جمع المعلومات المالية تعليمات مكافحة غسل الأموال المؤسسات المالية
16. [site:centralbank.gov.ye] شبكات التحويل المحلية شركات الصرافة تعليمات منشور
17. [site:centralbank.gov.ye] أسعار الصرف الحد الأعلى لأسعار بيع العملات وحدة التعاملات بالنقد الأجنبي
18. [site:saba.ye] البنك المركزي الكريمي إيقاف التعامل
19. [site:saba.ye] البنك المركزي المحافظ الإلكترونية
20. [site:saba.ye] البنك المركزي البنوك التي نقلت مراكزها إلى عدن حظر
21. [site:saba.ye] البنك المركزي شركات الصرافة الشبكة الحوالات تعميم
22. [site:saba.ye] القواعد التنظيمية خدمات الدفع الإلكتروني عبر الهاتف المحمول قرار محافظ البنك المركزي 2020
23. [site:saba.ye] "البنك المركزي اليمني يصدر بياناً مهماً" سبأ
24. [site:saba.ye] صدور قانون بمنع التعاملات الربوية رئيس المجلس السياسي الأعلى 2023
25. [site:saba.ye] رئيس مجلس الوزراء مؤسسة الاتصالات منصة سداد
26. [site:saba.ye] وزارة الاقتصاد والصناعة والاستثمار التجارة الإلكترونية منصة
27. [site:saba.ye] الهيئة العامة للزكاة زكاة عروض التجارة الإقرارات التجار الشركات 2025
28. [site:saba.ye] زبارة يؤكد مساندة المشاريع التي تسهم في إحداث نقلة في التعاملات المالية الإلكترونية جوالي وي كاش
29. [site:saba.ye] انعقاد الملتقى الأول لمكافحة جرائم الاحتيال وغسل الأموال بالعاصمة صنعاء شركات الصرافة توصيات
30. [site:tax.gov.ye] ضريبة المبيعات
31. [site:tax.gov.ye,yemen-nic.info,mof.gov.ye] قانون الضريبة العامة على المبيعات رقم 19 لسنة 2001 وتعديلاته pdf
32. [site:tax.gov.ye] الفاتورة الإلكترونية الفوترة نظام
33. [site:tax.gov.ye] التجارة الإلكترونية الخدمات الرقمية الإنترنت ضريبة
34. [site:tax.gov.ye] قرار رئيس المصلحة 2024 2025 تعميم المكلفين
35. تعديل قانون الضريبة العامة على المبيعات صنعاء مجلس النواب 2024 OR 2025
36. مصلحة الضرائب صنعاء التجارة الإلكترونية المتاجر الإلكترونية ضريبة
37. [site:yba.org.ye,yemen-yba.com] البنك المركزي صنعاء المحافظ الإلكترونية تعميم الدفع
38. [site:althawrah.ye,26sep.net] البنك المركزي الكريمي إيقاف التعامل
39. [site:althawrah.ye,26sep.net] البنك المركزي الدفع الإلكتروني المحافظ تعليمات
40. [site:yemeneco.org] البنك المركزي صنعاء المحافظ الإلكترونية الدفع الإلكتروني
41. [site:yemeneco.org] البنك المركزي بصنعاء الكريمي
42. (ext) البنك المركزي اليمني صنعاء الكريمي يونيو 2025 قرار
43. (ext) الكريمي صنعاء استئناف التعامل البنك المركزي إلغاء قرار إيقاف
44. (ext) الحوثي بنك الكريمي صنعاء فروع إغلاق حارس قضائي أرصدة 2025 2026
45. منشور دوري رقم (11) لسنة 2014 النقود الإلكترونية البنك المركزي اليمني خدمات الدفع عبر الهاتف المحمول
46. (ext) "القواعد التنظيمية" المؤسسات المالية خدمات الدفع الالكتروني الهاتف المحمول البنك المركزي اليمني
47. المنشور الدوري رقم (6) لسنة 2021 البنك المركزي اليمني العناية الواجبة اعرف عميلك
48. (ext) مركزي صنعاء المحافظ الإلكترونية تعليمات جديدة 2026
49. (ext) مركزي صنعاء يوقف محفظة إلكترونية ترخيص 2025
50. (ext) الربط البيني بين المحافظ الإلكترونية صنعاء البنك المركزي التحويل بين المحافظ
51. (ext) المحافظ الإلكترونية المرخصة من البنك المركزي بصنعاء قائمة 2025
52. [site:saba.ye,althawrah.ye,26sep.net,yemeneco.org] "قانون التجارة الإلكترونية" صنعاء وزير الاقتصاد مجلس الوزراء
53. (ext) مشروع قانون التجارة الإلكترونية اليمن صنعاء 2025 2026
54. (ext) ترخيص شركات التوصيل صنعاء الهيئة العامة للبريد البريد السريع ترخيص شركات النقل السريع
55. (ext) صنعاء وزارة الاقتصاد إلزام التجار البيع بالريال اليمني منع التسعير بالعملة الأجنبية تعميم
56. صنعاء استضافة البيانات داخل اليمن وزارة الاتصالات قرار مراكز البيانات توطين
57. [site:saba.ye,althawrah.ye,26sep.net,yemen-yba.com] البنك المركزي يمهل المواطنين 30 يوما استبدال العملة غير القانونية المحافظ الإلكترونية ديسمبر 2019
58. [site:saba.ye,yemen-nic.info,althawrah.ye] قانون الزكاة تعديل مجلس النواب الهيئة العامة للزكاة اللائحة التنفيذية
59. [site:yemen-nic.info,althawrah.ye,26sep.net,saba.ye] قانون تعديل قانون الزكاة رقم (2) لسنة 1999 2019 الهيئة العامة للزكاة نص
60. [site:yemen-nic.info] قانون رقم (1) لسنة 2010م بشأن مكافحة غسل الأموال وتمويل الإرهاب
61. جمعية الصرافين اليمنيين صنعاء قناة تليجرام t.me تعميم

WebSearch, English:
62. [site:centralbank.gov.ye] Central Bank of Yemen Sanaa circular electronic money e-wallet
63. [site:centralbank.gov.ye] Electronic payment services companies licensed
64. [site:centralbank.gov.ye] Laws and Directives electronic payment instructions agents
65. [site:centralbank.gov.ye] Exchangers requirements and forms money changers license
66. (ext) Kuraimi bank Sanaa Houthi central bank suspension lifted OR reversed OR resumed 2025 2026

Search terms used against the yemeneco.org WordPress REST API (`/wp-json/wp/v2/posts?search=`): المركزي صنعاء تعميم · المحافظ الإلكترونية · محفظة · الدفع الإلكتروني · الكريمي · كريمي · بنك الكريمي · الكريمي للتمويل · التجارة الإلكترونية · البطائق الشخصية · الأرصدة والحوالات · شبكات التحويل · الزكاة · ضريبة المبيعات · السجل التجاري · حماية المستهلك · العملة الأجنبية · نقل مقراتها · الشبكة الموحدة · التكنولوجيا المالية · منصة معتمد · المعاملات الربوية · الخوادم · بنك اليمن والكويت · التضامن · شركات التوصيل · خدمات التوصيل · البريد السريع · منصة سداد · أسعار الصرف المركزي صنعاء · البنك المركزي صنعاء الصرف.

Search terms used against the tax.gov.ye WordPress REST API: صغار المكلفين · المنشآت الصغيرة والاصغر · التجارة الإلكترونية · الفواتير · المبيعات.

Site crawls:
- moit.gov.ye: home, /legislations (2 pages), /legislations/laws (2 pages), /legislations/regulations (2 pages), /legislations/decisions, /legislations/circulars (empty), /electronic-services and each service page title
- tax.gov.ye: home, /salestaxes/, /forms/, /incometaxes/, the legislation library (shows "coming soon"), the registration guide page, 7-2020/
- yba.org.ye: home and the guides-and-laws section

## Looked for but not found

- **Decision No. 1 of 2020 (CBY Sana'a, e-payment by non-bank financial institutions):** no copy on centralbank.gov.ye or saba.ye surfaced in any search index. The only text found is the YBA report (yemen-yba.com/7623), which is already cited.
- **CBY Circular No. 11 of 2014 (e-money):** text not found. Only summaries exist, including the AFI article, which is already cited.
- **2021–2026 CBY-Sana'a instructions on electronic payments:** no instructions found on e-money agents, merchant payments or QR codes, wallet interoperability, wallet balance or transaction caps, or platforms and technical service providers. The QR standard and wallet-linking items found are CBY-Aden (March 2026) and outside this scope.
- **Dated licensed-wallet list:** no dated CBY-Sana'a circular listing licensed wallets or payment service providers was found. Only the undated "Electronic payment service companies" page exists (A001).
- **Kuraimi order of 22 June 2025:** the circular itself was not found. Only news reports exist (A013, A014). No later reversal or modification by Sana'a was found through 2026-10-10, in Arabic or English searches.
- **Bans on banks that moved to Aden in 2025:** no Sana'a decision was found targeting banks that relocated their headquarters to Aden in 2025, other than the Kuraimi order. The main bank ban list found is Decision No. 4 of 1445 AH (31 May 2024; A011, A012).
- **Remittance networks:** no CBY-Sana'a rule specific to remittance or transfer networks was found, such as network licensing or a Sana'a counterpart to Aden's "unified network". Only exchanger circulars, ban and reinstatement lists, and the cash-payout directive were found.
- **Periodic Circular No. 6 of 2021 (KYC/AML basis for Circular 17/1447):** text not found.
- **Sana'a Cabinet Decision No. 57 (confiscation of "illegal" currency, cited in 2020 reporting):** text not found.
- **E-commerce rules (Ministry of Economy, Industry and Investment):** no e-commerce law, regulation or circular in force was found. Nor was a commercial-registration category or procedure specific to online stores. What exists is a draft e-commerce law reported as sent to Cabinet (A061, A062), plus the planned "Mutamad" marketplace and a productive-families platform (A063, A064). The ministry's circulars page is empty.
- **Sales tax on online sales:** no Tax Authority rule was found on sales tax for goods or services sold online, on platform subscriptions or digital services, or on e-invoicing. The e-invoicing items on tax.gov.ye are reposted Egyptian material.
- **Zakat:** the text of the 2019 amending law (referred to as Law No. 1 of 2019) was not found. Nor was any executive regulation, or any zakat rule specific to e-commerce businesses.
- **E-transactions and data localisation:** no Sana'a-side law or rule was found on electronic transactions or data localisation, beyond Law 40/2006, which is already cited.
- **Courier and cash-on-delivery collection:** no licensing rule for courier or delivery firms collecting cash on delivery was found.
- **Yemeni Exchangers Association Telegram channel:** many CBY-Sana'a circulars are relayed through this channel, but its URL was not found.

## Pre-2023 rules with no 2023+ confirmation found

These are rules dated before 2023 for which no source dated 2023–2026 was found showing whether they are in force, amended or replaced:
- Cabinet directive of 30 Oct 2018 requiring a CBY technical permit before any ministry licenses an e-payment service (A033).
- Decision No. 1 of 2020 and Circular No. 11 of 2014 (both already cited). The only 2023+ source is a Yemen Banks Association article (A032, Feb 2026), which is an association source, not an authority. No official 2023+ confirmation was found.
- Ministry of Finance Decision 93/2002, the GST registration regulation (A068).
- Tax Authority Decision 108/2002 on sales invoices (A069).
- Tax Authority Decision 86/2005 on cash registers (A070).
- The undated invoices-and-records guide (A071).
- The four items above are still linked from the live tax.gov.ye sales-tax page (A067, undated, Wayback snapshot of 2025-11-28), but no dated 2023+ source mentions them.
- Internal Trade Law No. 5 of 2007 (A049). The only later source is the ministry's 2026 legislation archive listing (A040). It is not named among the 2025 draft amendments (A062).
- Consumer-protection executive regulation, PM Decision 272 (A044). Year illegible in the PDF text layer. The 2025 source (A062) mentions amending the law, not the regulation.
- Executive regulations of the Commercial Register Law and the Commercial Agencies Law (A042, A046; scanned, undated). The only later source is the 2026 legislation archive listing.
- Periodic Circular No. 6 of 2021 (KYC/AML). Its text was not found, but CBY Circular 17/1447 (A015, Nov 2025) cites it as the basis for that circular.
- Note on the exchanger forms page (A006): it is undated, but shows renewal forms for 2021 and 2022. The Jan 2026 circular (A025) says renewals now go through the e-portal.

Pre-2023 rules that do have a 2023–2026 source, and where it is:
- Law 40/2006 (CBY copy, A008): cited as in force in A029 (Dec 2025).
- AML Law 1/2010 as amended in 2013 (A039): cited in A029 and A015.
- Dec 2019 currency measures (A024): A023 (2024), A021 and A022 (2025).
- Commercial Register Law (A041): A058 (2024) and A062 (2025).
- Consumer Protection Law (A043): A062.
- Commercial Agencies Law (A045): A060 and A062.
- Trade Names Law (A047): A062.
- Companies Law (A048): A062.
- Consolidated GST law (A066): A073 (2024) and A074 (2026).
- GST registration guide of Dec 2022 (A072): A073.
- Small-enterprise exemption notice of 2021 (A075): A076 (2023).
- Zakat Law, the 2018 decision establishing the General Zakat Authority, and the 2019 amendment (A079–A081): A082 and A083 (2026).

## Most important documents only someone inside Yemen can fetch (ranked)

1. **CBY-Sana'a "Electronic payment service companies" page.** This is the licensed wallet/provider list.
   - https://www.centralbank.gov.ye/Home/payment
   - Alternate: https://centralbank.gov.ye/Home/payment?lang=en
   - Arabic: https://ftp.centralbank.gov.ye/Home/ChangeLanguage?lang=ar&act=payment
   - Wayback: https://web.archive.org/web/20250421060540/https://centralbank.gov.ye/Home/payment
2. **CBY-Sana'a "Payment Systems" section.** Indexed with Governor Resolution 4/1445. Check here for Decision 1/2020 and any later e-payment resolutions.
   - https://centralbank.gov.ye/Home/Detail/141-43104/%D8%A7%D9%86%D8%B8%D9%85%D8%A9-%D8%A7%D9%84%D9%85%D8%AF%D9%81%D9%88%D8%B9%D8%A7%D8%AA?lang=en
3. **CBY-Sana'a Decisions index.**
   - https://centralbank.gov.ye/Home/Detail/143-00124/%D8%A7%D9%84%D9%82%D8%B1%D8%A7%D8%B1%D8%A7%D8%AA?lang=en
4. **CBY-Sana'a circulars to banks and financial institutions.** Look for Circular 11/2014, Periodic Circular 6/2021, Circulars 17, 18 and 40 of 1447 AH, and the 22 Jun 2025 Kuraimi circular.
   - https://centralbank.gov.ye/Home/Detail/1186-20312/%D9%85%D9%86%D8%B4%D9%88%D8%B1%D8%A7%D8%AA?lang=en
5. **Saba (English) text of CBY-Sana'a Decision No. 4 of 1445 AH**, the bank ban list.
   - https://www.saba.ye/en/news3335749.htm
   - Wayback: https://web.archive.org/web/20240531202349/https://www.saba.ye/en/news3335749.htm
6. **Saba notice of Law No. 4 of 1444 AH prohibiting usurious transactions** (23 Mar 2023).
   - https://www.saba.ye/ar/news3230501.htm
7. **CBY-hosted text of Law 40/2006 on payment systems and electronic financial and banking operations.**
   - http://centralbank.gov.ye/ar/CBY.aspx?cattype=1&keyid=80&lang=2&pid=74
   - Wayback (2021): https://web.archive.org/web/20211112045257/http://centralbank.gov.ye/ar/CBY.aspx?keyid=80&pid=74&lang=2&cattype=1
   - Also the Financial Laws index: https://centralbank.gov.ye/Home/Detail/1254-22242/Financial%20Laws
8. **CBY-Sana'a money-changer circulars, and exchanger licensing requirements and forms.** Relevant to exchange and remittance channels and to KYC.
   - Circulars: https://centralbank.gov.ye/Home/Detail/160-41024/%D8%A7%D9%84%D9%85%D9%86%D8%B4%D9%88%D8%B1%D8%A7%D8%AA?lang=en
   - Requirements and forms: https://www.centralbank.gov.ye/Home/Detail/1264-13344/Exchangers-requirements-and-forms
9. **CBY-Sana'a official exchange-rate report.**
   - https://centralbank.gov.ye/Home/ExchangeRateReport
   - Wayback (Apr 2025): https://web.archive.org/web/20250419115912/https://centralbank.gov.ye/Home/ExchangeRateReport
10. **CBY-Sana'a licensed banks list**, including the Kuraimi Islamic Bank and Kuraimi Islamic Microfinance Bank entries.
    - https://www.centralbank.gov.ye/Home/banks
    - Wayback (Mar 2025): https://web.archive.org/web/20250324122759/https://www.centralbank.gov.ye/Home/banks
11. **Saba, July 2025 currency issues** (200-rial second issue; 50-rial coin).
    - https://www.saba.ye/ar/news3516903.htm
    - https://www.saba.ye/ar/news3515394.htm
12. **Saba items on payment rails and e-commerce policy.**
    - Sadad platform (3 Mar 2025): https://www.saba.ye/ar/news3445820.htm
    - E-commerce law listed for Cabinet (Oct 2024): https://www.saba.ye/ar/news3389327.htm
    - Productive-families e-marketing platform (May 2025): https://www.saba.ye/ar/news3474361.htm
13. **Ministry e-services portal** (reset from here). Needed to see the actual commercial-registration activity categories and fees online.
    - https://e-moit.gov.ye/
14. **General Zakat Authority website** (proxy 502 from here; domain zakat.gov.ye unconfirmed). Not in the TSV because no document URL was found.
