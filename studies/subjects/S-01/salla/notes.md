# S-01, phase A: salla (SA)

Subject: who holds the merchant's funds between the buyer's payment and the merchant's payout.

## What I read

**Q1 index**, `studies/concern-map/platforms/salla/`: `concerns.tsv`, `statements.tsv`, `gaps.tsv`, `citations.tsv`. I read in full the statements and gaps of SA-C-005, 006, 095, 096, 098, 110 to 128, 140, 164, 167, 170, 172, 177, 230, 231, 235 and 304, and the concern list.

**Held**, observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3` (the working tree was clean at that commit):

- `structures/salla/com-policies/terms/text.txt` (salla.com/terms, all 623 lines; the agreement text appears twice on the page, the first copy is cited), `com-policies/payments/text.txt`, `com-policies/shipping/text.txt`, `com-policies/policies-selling/text.txt`.
- `structures/salla/partners-legal/apps-policy`, `privacy`, `themes-policy` (`text.txt`): searched for amounts, transfers and settlements. They concern partners' dues, not the merchant's sales money.
- `structures/salla/help-articles/ar/texts.jsonl` and `en/texts.jsonl`, with `items.jsonl` for titles and `last_update_at`: the whole corpus searched by pattern (balances, transfer cycle, payouts, settlement, contract, licence, central bank, withholding, countries, COD, BNPL, gateways). Read in full: دورة تحويل المدفوعات الإلكترونية (ar, en), تحويلات مدفوعات سلة والتسويات في الإمارات (ar, en), … في الكويت (ar, en), تفعيل المدفوعات الإلكترونية (ar, en), صفحة المحفظة, - محفظة المتجر, -دورة تحويل المدفوعات الإلكترونية, إعداد الحساب البنكي واسترداد رصيد متجرك, إعداد الحساب البنكي ونظام الحوالات السريع, إدارة الطلبات المشتبه بها, تفعيل وإدارة الدفع عند الاستلام مع بوليصات سلة, تفعيل طرق الدفع في المتجر (Saudi), تفعيل مدفوعات سلة في الإمارات, تفعيل طرق الدفع في المتجر - الكويت. Read in part (money-flow paragraphs): the Tabby, Tamara and Madfu articles, the UAE Tabby and Tamara articles, طريقة تفعيل خدمات التقسيط, PayPal, stc pay, مكافأة الراجحي, the charity-store articles (PayTabs, Moyasar, Apple Pay), إدارة استرجاع الطلبات, the Salla Point articles, the Mahally articles, أسئلة شائعة حول توثيق المتجر (both), مركز الإعدادات الموحد, - تعيين إعدادات الفوترة في المتجر, the five English Salla Capital articles.
- `structures/salla/dashboard-translations/ar/payments.json` and `en/payments.json` (all keys), `apps.json`, `orders.json`, `shipping.json`; the other Arabic namespaces searched for balance, transfer, withholding and deduction wording.
- `structures/salla/kyc-schema/demo@en/source.json` (the store verification form).
- `structures/salla/docs-operations/md-openapi/items.jsonl` (settlements and transactions operations).
- `structures/salla/dashboard-features/merchant@en/items.jsonl` (payment, wallet, COD and financing flags).
- `structures/salla/merchant-plans/merchant@ar`, `com-plans`, `com-specialplan` (ar-sa, en-sa, ar-ae).
- Fetch-archive records read with `method/warc_text.py`: `raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@8607584` (salla.com/payments, text and raw) and `@28743756` (salla.com/en-sa/terms).

**Live**, read 2026-10-12: https://docs.salla.dev/1973350f0.md (Settlements; same descriptions as the held operations).

**Second run, 2026-10-12, after an interruption.** `method/check_subject.py` reported no error for `salla/`; the 36 unresolved quotes are live URLs awaiting capture (35 on help.salla.sa, copied from the index, and docs.salla.dev/1973350f0.md). For the gaps (brief rule 9):
- `method/held_index.py https://s.salla.sa/payments/kyc` (G01's route): not held. G02's route names no address.
- Read at the brief's commit, for G02: `dashboard-countries/merchant@ar` and `real-merchant@en` `items.jsonl` (242 countries; fields id, name, name_en, code, mobile_code, capital, position); `portal-countries/partner@en/items.jsonl` (240 countries; id, code, mobile_code, name, position); `settings-center/merchant@ar` `payments.json`, `payments~payment-restrictions.json`, `wallet.json` (feature `customer-wallet`) and `billing.json`; `showcase-store-payments/com-en-sa/items.jsonl` (payment-method slugs shown on merchants' storefronts).
- Searched: `com-plans` and `com-specialplan` (ar-sa, ar-ae, en-sa, en-ae); `settings-center`, `dashboard-restrictions` and `com-llms`; all of `structures/salla` for Salla Payments, مدفوعات سلة, salla_payments and sallapay (hits in help-articles, dashboard-translations, com-policies, help-sitemaps, help-embedded-tree, docs-index, twilight-components, dashboard-importmap).
- `dashboard-translations/{ar,en}/payments.json`, key `payment_limits`, titled حدود الدفع الإلكتروني / Transaction limits: a table with columns الدولة, منتجات ملموسة, منتجات رقمية and rows المملكة العربية السعودية, الإمارات العربية المتحدة, الكويت, البحرين, عمان, قطر, باقي الدول. No statement was taken from it.

## What I couldn't read

- The answers to the four FAQ questions on salla.com/payments, among them «متى يتم تحويل المدفوعات من لوحة تحكم متجري إلى حسابي البنكي؟». They are collapsed: they are not in the held text, and the archived record holds the questions without the answers. salla.com is not among the live sources the brief allows for salla.
- The text and parties of عقد خدمات الدفع (payment services agreement). The UAE and Kuwait payout articles name it as signed during store verification; no held file carries it. `kyc-schema/demo@en` holds the verification form (owner, documents, bank account, review) with no contract text.
- No Arabic Salla Capital article is held. The five English articles describe eligibility, application and tracking, not the deduction from sales; the deduction is stated in the dashboard's `capital.*` text, which is cited.
- The English usage agreement (salla.com/en-sa/terms) is held only in fetch archives (`20261005T235211Z-com-en-scheme@4672139`, `20261006T030341Z-com-toplevel@28743756`). I read the second. It carries the platform's English for terms recorded here, for example "returning any pending amounts in electronic payments to consumers", "Saudi Central Bank", "the payment and settlement system". I did not cite it: see the first problem below.

## Not recorded one by one

About 200 carrier articles (120 in the Arabic section مقالات قديمة, 78 in the English section Older articles, 2 current) each answer «ما هي آلية تسوية المبالغ؟» or a similar question with that carrier's own settlement schedule. Recording each would pass the 150-statement cap. The general statements are recorded instead: Salla does not collect COD amounts for carriers outside بوليصات سلة, and those amounts are settled directly between the merchant and the carrier under their agreement (from SA-S-0120 and SA-S-0121).

## Problems with the method or the brief

- The checker reads a local source with `git show <commit>:<path>` and does not open gzipped fetch archives, so a quote cited to `raw/runs/.../fetch.warc.gz` is reported "not found". The brief asks for archive records to be cited by archive path and offset. I cited nothing from archives; the English translations that exist only in the archived English terms are therefore not in `terms.tsv`.
- The usage agreement names only سياسة الخصوصية وسرية المعلومات as a further policy binding the merchant. The selling policy (سياسة البيع) is accepted when e-payments are activated (help articles), and عقد خدمات الدفع is named in help articles; the usage agreement names neither. The selling policy page is Salla's own and lists prohibited products and services only.
- Some held statements disagree with each other. Each is recorded with a note and not resolved: the Kuwait minimum payout (KWD 1, and "لا يوجد حد أدنى للتحويل" on the same page); moving amounts from رصيد المدفوعات الإلكترونية to رصيد المتجر (allowed in تفعيل المدفوعات الإلكترونية, not allowed in the older - محفظة المتجر); when a suspicious order's amount reaches the e-payments balance (on completion by the merchant, or recorded before confirmation).
- Statements copied from the index keep their index citations: several are help.salla.sa pages read rendered on 2026-10-10 and cited by live URL, which wait for the coordinator's capture. The same articles are held in `help-articles` at the brief's commit; new statements from them cite the held copy.
- Statements from articles in the help centre's مقالات قديمة section carry a note saying so.

## Phase A2, 2026-10-13

Worked on S01-VP-02 (who settles Salla Payments funds), and on the rows left as gap or not covered: S01-VP-07, 10, 11, 12, 13, 17. What was read for each is in `a2.tsv`.

- Read at observed-sa `4ca2e896a729215f422a137a364e7e9488610ba3`: `help-articles/{ar,en}/texts.jsonl` searched by pattern (settlement, reserve, security interest, licence, central bank, account, contract words); أسئلة شائعة حول توثيق المتجر (ar, en) read for the verification answers; `dashboard-translations/{ar,en}` all namespaces searched, `settings.json` keys `payments#settlement-cycle` and `billing#bank-account` read; `com-policies/terms`, `com-policies/payments`, `partners-legal`, `com-llms/llms-full-txt`, `com-plans`, `com-specialplan`, `kyc-schema`, `settings-center/merchant@ar` (`payments.json`, `wallet.json`), `docs-operations`, `docs-index` searched.
- `method/held_index.py https://s.salla.sa/payments/kyc` and `https://s.salla.sa/settings/payments`: not held.
- No held text names who settles Salla Payments funds, a reserve, a security interest, or the entity, licence or account under which the funds are held. G01 stays open for S01-VP-11, 12 and 13.

## What I couldn't read (A2)

- The payment services contract (عقد خدمات الدفع) and the merchant dashboard pages, as in phase A.

## Phase A2, second run, 2026-10-13

Brief `briefs/A2-close-gaps.md`, for S01-VP-02 (who settles مدفوعات سلة funds) and the gap rows S01-VP-07, 10, 11, 12, 13, 17. Added S01-SA-137 to 139 and S01-SA-C190 to C193. No existing row was changed.

**Sweep**, observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`, `structures/salla/help-articles/{ar,en}/texts.jsonl` (1,658 ar, 1,280 en), titles from `items.jsonl`, slugs from each record's URL:
- by term: مدفوعات سلة, رصيد المدفوعات الإلكترونية, تسوية/تسويات, دورة التحويل, المستحقات, المحفظة/محفظة المتجر/رصيد المتجر, عقد خدمات الدفع, حجز/المبالغ المحجوزة/تعليق عمليات الدفع/مبالغ معلقة, خصم (المبلغ, الرسوم, عمولة), استرداد رصيد/سحب رصيد, إيداع, الحد الأدنى للتحويل, احتياطي/رهن/مقاصة; Salla Payments, online-payments or electronic payments balance, settle/settlement, payout, transfer cycle, dues, wallet, payment services agreement, withhold/held from/suspended until, deduct, withdraw, deposit, minimum transfer or payout, reserve/lien/set-off/collateral;
- by country: الكويت, الإمارات, السعودية, البحرين, عمان, قطر, مصر, الخليج, الأردن, Kuwait, UAE, Emirates, KSA, Saudi, Bahrain, Oman, Qatar, Egypt, GCC, Jordan, in title or slug, or in the text of an article whose title or slug is about payments, payouts, settlement, the wallet, invoices, billing, bank accounts or verification.

597 articles listed (327 ar, 270 en). Line numbers (line = position + 1):
- ar, not cited before: 3, 5, 6, 17, 18, 19, 24, 35, 42, 47, 48, 59, 62, 64, 66, 75, 81, 83, 107, 109, 111, 113, 114, 119, 132, 155, 159, 161, 165, 166, 169, 177, 183, 197, 198, 211, 214, 219, 220, 221, 226, 242, 249, 267, 269, 277, 278, 280, 284, 285, 288, 289, 291, 295, 298, 301, 303, 307, 330, 337, 343, 344, 345, 347, 353, 354, 360, 361, 369, 374, 375, 379, 386, 392, 396, 400, 401, 402, 403, 416, 421, 423, 429, 434, 435, 451, 455, 457, 460, 461, 468, 470, 471, 472, 475, 476, 477, 478, 479, 480, 481, 482, 483, 486, 487, 488, 489, 490, 491, 492, 493, 495, 500, 502, 504, 507, 514, 515, 516, 517, 520, 521, 523, 526, 527, 532, 533, 536, 543, 548, 550, 551, 552, 553, 554, 555, 557, 558, 559, 563, 564, 565, 566, 568, 575, 577, 584, 593, 603, 610, 627, 628, 640, 645, 657, 659, 672, 690, 691, 693, 699, 700, 706, 707, 717, 718, 722, 732, 795, 825, 848, 852, 855, 859, 869, 870, 871, 880, 883, 884, 886, 890, 891, 893, 897, 906, 907, 909, 916, 924, 926, 928, 936, 979, 984, 987, 1011, 1024, 1029, 1032, 1043, 1054, 1058, 1091, 1095, 1107, 1117, 1118, 1132, 1133, 1139, 1140, 1143, 1144, 1150, 1153, 1161, 1172, 1180, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1206, 1208, 1241, 1242, 1253, 1269, 1299, 1303, 1310, 1312, 1313, 1318, 1319, 1346, 1357, 1358, 1363, 1365, 1371, 1373, 1375, 1389, 1392, 1393, 1425, 1430, 1431, 1437, 1447, 1465, 1466, 1484, 1486, 1487, 1491, 1494, 1495, 1496, 1497, 1499, 1510, 1520, 1522, 1526, 1533, 1535, 1543, 1546, 1552, 1555, 1556, 1557, 1560, 1588, 1592, 1596, 1597, 1599, 1600, 1605, 1625, 1628, 1629, 1638, 1647.
- ar, already cited: 23, 60, 71, 225, 664, 754, 755, 758, 858, 863, 866, 872, 873, 874, 879, 881, 882, 927, 929, 1052, 1297, 1502, 1524, 1565, 1590, 1611, 1624.
- en, not cited before: 1, 2, 4, 5, 7, 20, 22, 28, 29, 31, 32, 37, 40, 41, 48, 56, 77, 81, 117, 135, 136, 143, 144, 145, 146, 149, 156, 157, 160, 164, 165, 169, 174, 190, 192, 193, 195, 196, 200, 201, 205, 207, 208, 209, 210, 213, 214, 218, 219, 220, 221, 222, 224, 225, 226, 233, 234, 235, 240, 244, 247, 253, 256, 257, 278, 286, 294, 295, 296, 300, 301, 302, 303, 304, 305, 308, 309, 311, 316, 319, 321, 322, 325, 333, 334, 338, 339, 340, 343, 344, 347, 349, 350, 351, 353, 354, 355, 356, 362, 363, 365, 371, 378, 379, 386, 387, 388, 394, 398, 401, 404, 405, 426, 429, 437, 447, 462, 465, 468, 469, 477, 481, 483, 484, 496, 502, 503, 519, 543, 545, 548, 551, 558, 561, 562, 563, 566, 570, 571, 576, 578, 579, 597, 598, 606, 608, 610, 621, 633, 645, 649, 652, 653, 662, 664, 666, 680, 681, 687, 694, 708, 710, 715, 717, 722, 728, 729, 732, 733, 734, 735, 737, 746, 754, 764, 765, 776, 788, 791, 792, 793, 794, 803, 805, 806, 807, 808, 824, 829, 835, 836, 837, 838, 844, 869, 870, 871, 874, 889, 892, 898, 914, 915, 921, 922, 923, 924, 936, 939, 942, 943, 947, 994, 995, 1002, 1008, 1016, 1028, 1033, 1034, 1035, 1036, 1039, 1040, 1047, 1050, 1051, 1058, 1066, 1072, 1074, 1080, 1081, 1087, 1091, 1101, 1109, 1130, 1131, 1138, 1139, 1141, 1145, 1148, 1152, 1155, 1158, 1165, 1175, 1184, 1193, 1201, 1208, 1210, 1218, 1222, 1223, 1224, 1225, 1226, 1241, 1243, 1258, 1278.
- en, already cited: 10, 25, 550, 567, 613, 1242.

**Read in full:** en 1047 (Salla Payments Kuwait Payouts & Settlement), 652 (How to Activate Salla payments in Kuwait), 1223 (Verify your Salla store in Kuwait), 447 (Create a Salla store in Kuwait), 1080 (Set up shipping companies for your Kuwaiti store), 145 (Billing settings in your store | UAE), 144 (… | Saudi Arabia), 1241 (Wallet & invoices | Saudi Arabia), 710 (instant transfers); ar 755 (تحويلات مدفوعات سلة والتسويات في الكويت), 1627 (نظام الحوالات السريع). In every other listed article, the paragraphs carrying settlement, Salla Payments, balance, reserve, security, licence, agreement, account, gateway and hold words were read. About 250 carrier articles (both languages) answer settlement questions with the carrier's own COD schedule, as phase A noted.

**Found:** the held Kuwait article states settlement "according to the payment services agreement signed during your store verification" (S01-SA-137) and that the payment "moves through processing and settlement" (S01-SA-138); neither version names who settles. The English article on payment methods (en 808) calls Electronic payments "a Salla service ... settling transactions with banks" (S01-SA-139); its Arabic (ar 1502) says "إتمام العمليات المالية مع البنوك". No listed article names the entity, licence or account under which Salla Payments funds are held, a reserve kept from them, or a security interest over them. G01, G03, G04, G05 and G06 remain; no new gap was made, because the existing ones name the same missing items.

**Held but not recorded, being outside the variation points worked on:**
- the Kuwait article's English "Minimum payout: KWD 1" against the held Arabic "لايوجد حد أدنى للحوالات" (S01-VP-16);
- its "The online-payments balance holds eligible store-sales earnings before payout" (S01-VP-01);
- en 1241's "Unverified stores will have funds pending until verification is complete" (S01-VP-18);
- the IBAN-certificate articles for بنك البحرين (ar 1192), بنك الخليج (ar 1195), بنك الكويت (ar 1198) and Emirates NBD and Mashreq (ar 1190, 1199), which say a certificate from that bank lets the merchant "تُفعّل بوابات الدفع الإلكتروني وتستقبل أرباح مبيعاتك" (bears on G02's country list, which is not among this run's variation points).

## What I couldn't read (A2, second run)

- عقد خدمات الدفع and the dashboard's verification page, as before. No held help article carries the agreement's text or parties.
- en 145 (Billing settings | UAE) has the heading "Bank account for receiving payouts" with no text under it in the held copy. No Arabic version of en 145 is held.

## Phase A2, second run, continued (2026-10-13)

The brief's step 2 now asks for everything found that bears on the subject, with the scope the source states. From the same sweep and the same held copies (observed-sa `4ca2e896a729215f422a137a364e7e9488610ba3`, `help-articles/{ar,en}/texts.jsonl`), I added S01-SA-140 to 177 (citations S01-SA-C194 to C275). The previous section's list "Held but not recorded" is now recorded:
- Kuwait (ar line 755, en line 1047): minimum payout in both languages (S01-SA-140 English "KWD 1", S01-SA-141 held Arabic "لايوجد حد أدنى للحوالات"; they disagree, as S01-SA-061 and 062 already did, and neither is resolved), schedule, balance, bank account, fees under the payment services agreement, wallet tracking (marker قادم قريبًا) and COD tracking; verification bank step (ar 927, en 1223).
- UAE (ar line 754, en line 1242): schedule and AED 250 minimum in both languages, the held copy of S01-SA-051's sentence, bank account change, fees, wallet tracking; verification bank step and the account types by licence (ar 929, en 1225).
- Saudi Arabia, as the English titles state it (en 1241, en 144): funds of unverified stores pending until verification, verification required for transfers, invoice frequency by plan, SAR/AED 100 minimum, the payout bank account and its review; from the Arabic صفحة المحفظة (ar 664), withdrawal timing and the net amount after fees; ar 1502 / en 808: SAR 100 minimum and payments received in SAR.
- Waybill costs and international customs fees taken from the wallet balance (ar 1310, en 1051).
- IBAN-certificate articles for بنك البحرين, بنك الخليج, بنك الكويت, Emirates NBD and Mashreq (ar 1192, 1195, 1198, 1190, 1199), and their account-name notice. They name the bank, not a country; the scope is the bank as named. The 11 articles for Saudi banks (ar 1186 to 1201) open with the same sentence and are not recorded one by one.

Statements now added in phase A2: 44 (S01-SA-134 to 177), within the cap.

Not recorded: customer-wallet and cashback articles (the customer's balance, not the merchant's sales money), affiliate commissions, Salla Ads billing, subscription refunds to رصيد المتجر, and transaction limits (they concern the buyer's payment, not the merchant's funds).

## Absence audit

Phase A3, 2026-10-13, brief `briefs/A3-absence-audit.md` (with the coordinator's additions of the result `partly contradicted` and of fetch-archive search). Seven claims audited: S01-SA-G01 to G06 (no gap is of kind `page not read`) and S01-SA-N01. One row each in `absence-audit.tsv`, with every `corpus_search` command and every document read. Added S01-SA-178 to 189 (12 statements) and S01-SA-C276 to C290, and two terms (لحساب المتجر; الطرف الذي حُصّل المبلغ لحسابه). No existing row was changed.

**What I found**
- G01 (entity, licence or account), partly contradicted. Two shopper-facing articles, held in both languages, say payments are collected for the store's account: 'المبالغ تُحصَّل لحساب المتجر' / 'Payments are collected for the store's account' (S01-SA-178) and the store is 'الطرف الذي حُصّل المبلغ لحسابه' (S01-SA-179). Neither names مدفوعات سلة or a payment method. The entity holding Salla Payments funds, its licence, and the text and parties of عقد خدمات الدفع are still unstated; `held_index.py` again reports the route page https://s.salla.sa/payments/kyc not held. Also recorded from these searches: the dashboard's chargeback metric, 'payments held by the issuing bank due to disputes' (S01-SA-180, 181).
- Paylink: the salla.com blog posts in the fetch archives say Salla acquired Paylink, a company 'مرخصة من البنك المركزي السعودي لتقديم خدمات مدفوعات التجارة الإلكترونية'. No record read says that Salla Payments funds are processed, settled or held by Paylink or under its licence. Nothing was recorded from them.
- G02 (complete country list), confirmed. Added without closing it: a help article held only in a fetch archive (توثيق متجرك في قطر | سلة, run 20261009T034955Z-help-sitemap-missing) names 'تحويلات مدفوعات سلة والتسويات في قطر' and a Qatari payout account in QAR (S01-SA-182 to 186). The sign-up text 'منصة سلة متاحة حاليًا في السعودية والإمارات فقط' (S01-SA-189) is a list presented as complete. It covers the platform, not Salla Payments, and it disagrees with the Kuwait and Qatar articles. Not resolved.
- G03 (who settles), partly contradicted, with no new statement. The English 'Electronic payments is a Salla service that processes payments in your store directly, settling transactions with banks ...' (S01-SA-139, added in phase A2 after the gap was written) names a Salla service as settling with banks. No source names the entity that settles the funds before transfer to the merchant.
- G04 and G06 (reserve), confirmed. G05 (security interest), partly contradicted: صندوق سلة's page says its investment is given 'بلا أوراق ولا ضمانات' (S01-SA-187), repaid as a share of sales (S01-SA-188). For Salla Payments balances in general, no source states a security interest, lien, pledge or set-off, or that none is taken.
- N01 (wallet tabs), confirmed. Every held or captured source that lists the merchant wallet's sections gives the same three, including the wallet FAQ held only in a fetch archive.

**Searches too broad to read in full, and how I narrowed them**
- Country names alone (السعودية 233 ar documents, Saudi 232 en; الإمارات 47, الكويت 32; plus fetch-archive records): I read the payment, payout, wallet, verification and billing articles among them. For the rest I ran combined searches (`--all` with عقد, agreement, payment services, تسوية, المدفوعات الإلكترونية, مدفوعات سلة, فقط, only).
- Partner names and plan names alone (929 Arabic documents, because تاب and مدفوع match inside other words; 232 and 385 for plan words): narrowed with `--all` on ترخيص, licensed, البنك المركزي and central bank, and on المحفظة or wallet with each partner.
- تسوية/settle (147 ar, 123 en): about 220 are carrier articles whose settlement answer is the carrier's own COD schedule. I read them by title and snippet. The rest I read at the matching paragraphs.
- تبويب/tabs (658 ar): narrowed to المحفظة or wallet with رصيد or balance, and to each partner.
- Fetch archives (1,315 records across the re-run searches): I grouped them by URL. salla.com navigation and footers, help.salla.sa category pages, app listings and cdn.translations copies of the held translation files were read by URL and snippet. Terms pages, payment, Capital and GCC pages, payment-related blog posts and the two help articles missing from `help-articles` were read with `method/warc_text.py`.

**Problems with the method**
- `corpus_search.py` changed twice during this run. Some matching moved to whole words, so earlier hits such as SAMA inside "samaritan" are gone. Then it began searching observed-sa's fetch archives. I re-ran every logged search after the second change and compared the results. Some matches disappeared and fetch-archive records were added. Nothing else changed.
- The default listing caps at 40 documents per source, so the hit counts in the summary line exceed what is listed. I re-ran the narrow searches with `--max 500` to list every fetch-archive hit.
- For G03, the statement that partly contradicts the claim was already recorded (S01-SA-139), but the brief defines `stmt_ids` as the statements the auditor added. The checker requires a contradicted gap to name a statement, so the row names S01-SA-139 and the note says it was added in phase A2.
- The phase A cap of 150 statements had been passed before this phase (177 statements). The coordinator said A3's cap counts only the statements added here, which is 12.
- Quotes cited to fetch-archive records (S01-SA-C282 to C288) were checked by `check_subject.py` and resolved.

## Phase A2, third run, 2026-10-17 (S01-VP-06)

Brief `briefs/A2-close-gaps.md`. Task: `variants.tsv` row S01-V-655, Salla's `not covered` row under S01-VP-06 (who or what fills "agent"). The message named no other arrangement. Added S01-SA-190 to 201 (12 statements), S01-SA-C291 to C321, four terms, the gap S01-SA-G07 and the `a2.tsv` row for S01-VP-06. One existing row was changed, as step 4 of the brief allows: S01-SA-072's `conditions` now read S01-SA-004;S01-SA-195.

**What I read.** observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`; no live page was read.
- `help-articles/{ar,en}/texts.jsonl`: every paragraph of every article searched for the Arabic and English agency words (نيابة, تفويض, تفوض, مفوض, وكيل, وكالة, وكلاء, وسيط, وساطة, مندوب, مناديب, لحساب, لصالح; behalf, authorize, authorization, agent, agency, intermediary, middleman, merchant of record, delivery agent, own courier, collected for). Read in full: ar 77 and en 826 (إدارة المناديب والشركات الخاصة), ar 746 and en 530, ar 872 and en 567 (UAE activation), ar 873 and en 652 (Kuwait activation), ar 1312 and en 1087 (shipping), ar 1651 and en 1102 (shopper help hub). The other hits were read at the matching paragraph. They concern app permissions, AI agents, chat support agents, ad agencies, domain checks, carriers' own agents and Apple developer accounts.
- `dashboard-translations/{ar,en}/*.json`: every key searched for the same words. Read: `apps.json` `apps.agreement.hms.*` and `apps.managed_settlement.*`; `shipping.json` `managed-settlement.*`; `payments.json` `charity_payments.*` and `capital.*`.
- `com-policies` (terms, payments, shipping, privacy, policies-selling, marketing-tools, moshamer-ai, policies-nd96) and `partners-legal` (apps-policy, privacy, themes-policy): searched for the same words. In the usage agreement they occur for the merchant's store used by someone else ('فوّضته باستخدام المتجر باسمك ولحسابك'), for user data given to a third-party provider ('يصرّح لمنصة سلّة ويمنحها الإذن بتزويد مقدم الخدمة'), for unauthorized use of an account or card, and in the subscription refund policy ('حجز المبالغ المستردة'). The English usage agreement (`raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@28743756`) has no agent, agency or 'on behalf' wording.
- Every other structure under `structures/salla` searched for the same words (raw, and unescaped for JSON files). The hits are app permission and app-store texts (`app-categories`, `app-store-tabs`, `marketplace-apps`; `app-categories/apps-salla-sa/source.txt` repeats the `apps.json` managed-settlement and holding-policy texts), OAuth and API descriptions (`docs-dataschemas`, `docs-operations`), influencer-agency routes of the partner portal (`portal-apps`, `portal-app-routes`, `portal-menu-definitions`), an AI-agent changelog entry, a theme description, and `kyc-schema/demo@en` (an entity's authorization letter to the store owner).
- Fetch-archive records read with `method/warc_text.py`: `20261006T030341Z-com-toplevel` @15293952 and @32108089 (salla.com/salla-crossborder, ar and en-sa); `20261005T234928Z-docs-md` @106240, @149379, @151127 and @1329598 (docs.salla.dev settlements, transactions, payments, recurring payments).
- The `corpus_search.py` commands are listed in `gaps.tsv` S01-SA-G07.

**What I found**
- 'تُفوّض سلة' / 'you authorize Salla' and 'نيابةً عنك' / 'on your behalf' occur in the consent the merchant gives before a carrier app holds waybill amounts from the wallet and Salla pays the carrier (S01-SA-125 from phase A; added the English, the shipping-settings text and the consent label: S01-SA-190 to 192). 'تفويضًا صريحًا' / 'you authorize Salla' occurs in سياسة إدارة المبالغ المحجوزة for partner apps (S01-SA-124; added its stated reason and its English: S01-SA-193, 194). For charities, connecting the charity's own gateway account authorizes Salla to use it for payment processing (S01-SA-112; added the English: S01-SA-195).
- salla.com/salla-crossborder lists 'المدفوعات و البيع بالنيابة (MoR)' / 'Payments and Merchant of Record (MoR)' among the partnership areas Salla is looking for, under both of its tabs (S01-SA-196, 197). It names no partner.
- The private-couriers article gives, as the example for turning on cash on delivery for a courier, a courier who collects the amounts at delivery (S01-SA-198). Salla's English names the store's couriers 'Store delivery agents' in one article (en 530) and 'Store couriers' or 'private couriers' in others (en 567, 652, 826).
- Recorded from the same reading: the shopper help hub's 'هو الطرف الوحيد الذي يملك صلاحية تعديل طلبك أو إعادة مبلغك' (S01-SA-199); صندوق سلة's 'تُحصَّل تلقائيًا من مبيعات متجرك عبر مدفوعات سلة' (S01-SA-200); the shipping article's 'تختلف طرق تسوية مبالغ الدفع عند الإستلام بحسب سياسة شركة الشحن' (S01-SA-201).
- No source read says in what capacity Salla, or another party, receives or holds buyers' payments made through مدفوعات سلة: new gap S01-SA-G07 (`searched, not found`, for the founder). `held_index.py https://s.salla.sa/payments/kyc`: not held.

**Read, not recorded**
- 'اتفاقية الوكالة بالاستثمار' / 'investment agency agreement' (`payments.json` `capital.status.terms.*`, `capital.faq.items.timing.answer`; salla.com/sallacapital1): the agreement the merchant accepts before the صندوق سلة investment amount is transferred to it. The texts read do not say what it provides about the merchant's sales funds; S01-SA-200's note names it.
- The subscription refund policy in the usage agreement ('يحق لسلة حجز المبالغ المستردة لمدة تصل إلى (15) يوم عمل'): it concerns refunds of subscription fees.
- The partner, agency and affiliate agreements (partners.salla.com/legal/*, اتفاقية استخدام التسويق بالعمولة): their agency wording concerns Salla and its partners or marketers.
- The searches `--all 'الدفع عند الاستلام' 'المندوب'` and `--all 'cash on delivery' 'courier'` list 110 Arabic and 86 English help articles, mostly carrier articles that say whether the carrier collects cash on delivery and when it settles. As phase A did for their settlement answers, they are not recorded one by one.

**What I couldn't read**
- The text of سياسة إدارة المبالغ المحجوزة, of اتفاقية الوكالة بالاستثمار and of عقد خدمات الدفع: no held file carries them. The dashboard texts name the first two (`apps.json`, `payments.json`; the second also on salla.com/sallacapital1), and the UAE and Kuwait payout articles name the third.

**Problems with the method**
- `corpus_search.py` matches an Arabic term as a string, so 'الجمعيات الخيرية' does not match 'للجمعيات الخيرية': the `--all` search for it with 'الإذن' found nothing, and the search with 'الخيرية' found `payments.json`.
- `check_subject.py` rewrites `studies/subjects/S-01/kinds.tsv` when it runs; the run at the end of this phase adds the new statements' rows to it.

## Absence audit, second run (S01-SA-G07), 2026-10-17

Phase A3, brief `briefs/A3-absence-audit.md`, for the one claim phase A2 added: S01-SA-G07 (in what capacity Salla, or another party, receives or holds buyers' payments made through مدفوعات سلة). One row added to `absence-audit.tsv`; the seven earlier rows are unchanged. Added S01-SA-202 (one statement), S01-SA-C322 and C323, and two terms (أموالك; حل متكامل). No existing row was changed.

**What I found**
- G07, confirmed. No held or captured source names Salla or a partner as the merchant's agent for these payments, says it receives or holds them on the merchant's behalf or under its authorization, or names another capacity. The agency and authorization words occur only where phase A2 recorded them (carrier-app waybill consent, the holding management policy for partner apps, charity gateway accounts, the cross-border MoR partnership area) and in senses unrelated to the money: app OAuth permissions, ads, domains, AI agents, chat agents, carriers' agents, and the affiliate agreement's clause that it creates no agency between Salla and the affiliate.
- Two older salla.com blog posts (shown as 'نشر منذ 3 سنوات') describe payment gateways in general as 'وسيط إلكتروني بين طرفين' and 'وسيط إلكتروني -بين المشتري والتاجر - لاستلام وتسليم الأموال'. They do not apply it to Salla's own service. Nothing was recorded from them.
- Recorded without closing the gap: a salla.com blog post held in the fetch archive, in Arabic and in Salla's English, says 'ما يحتاج تروح لبنك، ولا توقع عقود مع شركات دفع خارجية. سلة تعطيك حل متكامل يستقبل أموالك ويحولها لحسابك بكل أمان' (S01-SA-202). It names no entity, account or capacity, and names neither مدفوعات سلة nor عقد خدمات الدفع.
- `held_index.py https://s.salla.sa/payments/kyc` (the route's page): not held.

**Searches too broad to read in full, and how I narrowed them**
- 72 `corpus_search.py` commands, each with `--max 500`, listed 1,206 documents in all. Broad hits: 'agent' (about 340 documents, mostly docs.salla.dev navigation, 'user-agent' fields, AI and chat agents), 'authorization' (about 170, mostly app permission texts and API headers), 'أمين' (146 Arabic articles, matching تأمين), 'on your behalf' and 'نيابة عنك' (about 110, mostly apps.salla.sa permission texts).
- I read titles and snippets of every listed document. Then, with a script run with `python3 -I` from my scratchpad, I printed every paragraph of every listed document that carries both an agency, capacity or receipt word and a word for the money (98 paragraphs), and read those. I read in full the documents whose paragraphs bore on the claim.
- The `--all` searches that pair مدفوعات سلة with لحساب or وسيط match mostly through the salla.com and help.salla.sa navigation menus ('المدفوعات', and لحساب inside 'الحساب'). I read the listed help articles at their لحساب paragraphs; the salla.com pages by URL and snippet.

**Problems with the method**
- `corpus_search.py` matches an Arabic term inside words, so 'لحساب' matches 'الحساب' and 'مُيسّر' matches 'ميسر' (Moyasar). These searches list far more than they should.
- The capture-run locators in the search output carry this repository's current commit, which changed while the searches ran (four different commits appear across the outputs).
- The brief defines `stmt_ids` only for contradictions, so the row for this confirmed claim leaves it empty; S01-SA-202 is named in its note.
