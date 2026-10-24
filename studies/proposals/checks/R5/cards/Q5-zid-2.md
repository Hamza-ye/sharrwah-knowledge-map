# Cards: Q5 on zid

13 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 44:** - When it is paid out, and at what level: Salla by plan, from weekly on Plus to daily on Special; Zid by country; WooPayments daily, "the default for almost all accounts", changeable per account; BigCommerce Payments holds a new account's initial payments "for up to 21 days". They match by role; the level differs. Q5-SA-P0020, Q5-SA-P0022, Q5-ZD-P0041, Q5-WC-P0036, Q5-BC-P0083
- **section 1, line 45:** - Deductions come off first, matching by role, in the own services' terms (official pages): Shopify may hold funds in a Reserve Account; Stripe pays out "net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe"; زد باي takes chargebacks "مباشرة من رصيده المتوفر". Services, financing and apps draw on it too: Salla's dashboard text, as captured on 8 October 2026, holds label amounts to pay "نيابةً عنك إلى شركة الشحن", and its financing takes "%25 من صافي المبيعات لكل دفعة" (observed); a dropshipping app may "temporarily withhold a specific amount of money" (Salla's developer docs). Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0131, Q5-SA-K1690
- **section 1, line 46:** - Some keep separate balances, matching by role: in Salla's store real-merchant, observed on 12 October 2026, the wallet summary listed "Wallet", "Electronic Payments" and "Cash on Delivery Payments"; Zid's الاستقطاع للمحفظة moves part of order payments into محفظة زد; Shopify's Shop Cash comes in the same payouts; WooPayments' FROD balance is "a special bucket of funds inside your WooPayments account". Q5-SA-075, Q5-ZD-P0067, Q5-SH-074, Q5-WC-042
- **section 1, line 47:** - Through a gateway the merchant connects, money goes to the merchant's own account with it, matching by role: funds are in "your merchant account with your merchant service provider" (BigCommerce); "the purchase amount is transferred to your merchant account" (Shopify); Salla's dashboard text, as captured on 8 October 2026, collects through the gateway "بدلًا من مدفوعات سلة" (observed); "المدفوعات توصل لحسابك مباشرة" (Zid's Paymob page). Where the money is held between the buyer's payment and its transfer was not in what was read on Shopify. WooCommerce says only that it is "unable to assist with Stripe account issues", payouts among them: a statement of no part, naming no one. Q5-BC-P0089, Q5-SH-P0050, Q5-SA-K1639, Q5-ZD-P0107, Q5-SH-N02, Q5-WC-P0159
- **section 1, line 49:** - Pay-later providers pay the merchant directly, or into the platform's own service: at Salla (UAE help), "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة"; at Zid, "تقوم تابي بالدفع للمتاجر مباشرة"; with BigCommerce's PayPal Pay Later, "you, the merchant, always get paid"; these match by role. Shopify and WooCommerce differ: Shop Pay Installments payouts "are included with your Shopify Payments payouts", and WooPayments receives "the entire purchase amount immediately". Q5-SA-P0102, Q5-ZD-P0077, Q5-BC-P0095, Q5-SH-K1686, Q5-WC-P0056
- **section 1, line 51:** - Cash on delivery is settled with the merchant, or collected through the platform, matching by role: at Salla, with a carrier outside its labels, it is settled "مباشرة بين التاجر وشركة الشحن", while through its labels "تحوِّل شركة الشحن المبلغ إلى سلة" (dashboard text, as captured on 8 October 2026, observed); through Zid's shipping, "تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم" (its terms, official); WooCommerce's cash on delivery takes payment "at the time of delivery". Q5-SA-P0092, Q5-SA-P0042, Q5-ZD-P0070, Q5-WC-P0097
- **section 2, line 66:** - It draws on Salla's choice between an existing account and a request the provider may reject, the own account Zid's pay-later providers need, BigCommerce's application and underwriting, and Shopify's apps, where the merchant may "log in or create an account with the payment provider". Q5-SA-053, Q5-SA-057, Q5-ZD-P0080, Q5-BC-P0048, Q5-SH-053
- **section 2, line 69:** - It draws on Shopify's, Zid's and Salla's methods by the store's address or country, and, for conditions, on their plans, Salla's verification, Zid's كي نت for institutions and companies only, and Salla's limits by country. Q5-SH-012, Q5-ZD-001, Q5-SA-036, Q5-SA-P0068, Q5-ZD-P0150, Q5-SA-K0091, Q5-ZD-K0042, Q5-SA-048
- **section 2, line 83:** - It draws on the direct route the platforms show for gateways the merchant connects, pay-later providers that pay the store, and bank transfer, and on the held route of their own services. Q5-SH-P0050, Q5-ZD-P0107, Q5-ZD-P0077, Q5-SA-P0099, Q5-WC-P0024, Q5-ZD-P0024
- **section 2, line 84:** - Cash on delivery collected through a carrier Sharrwah contracts would pass through Sharrwah, as it passes through Salla and Zid: a held route. Cash the merchant collects is direct. Q5-SA-P0042, Q5-ZD-P0070, Q5-SA-P0092
- **section 2, line 88:** - It draws on the platforms' own balances and their deductions and reserves, Salla's label holds under the merchant's authorization, and the payout account Salla takes at verification. Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0055
- **section 2, line 89:** - Why: rule 3, the ledger's shape is expensive to change; rule 2, a deduction plugs into the ledger without touching orders. Q5-SA-P0126, Q5-ZD-P0061
- **section 2, line 90:** - Where the platforms differ, one balance with credits folded in (Shopify's Shop Cash; WooPayments' FROD bucket) against several wallets (Salla's observed store; Zid's wallet), typed entries in one ledger can show either; the choice is kept open. Q5-SH-074, Q5-WC-042, Q5-SA-075, Q5-ZD-P0067
- **section 3, line 104:** - An offered method's conditions are set per plan, verification state and business type, by Sharrwah. Q5-SA-P0068, Q5-SA-K0091, Q5-ZD-K0042
- **section 3, line 111:** - On the held route, the payout schedule is set per plan (Salla), per country (Zid) or per account, by the merchant (WooPayments). Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0036
- **section 5, line 137:** - On the held route only, the payout schedule's level (plan, place or account) and whether balances show as one or as several: the design keeps both as data. The holder's terms settle them. Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0036, Q5-SA-075
- **section 7, line 164:** - Whether Sharrwah collects cash on delivery through carriers it contracts, which would be a held route. Q5-SA-P0042, Q5-ZD-P0070
- **section 7, line 168:** - Who may take online payments through Sharrwah, since the platforms' own services take only businesses from listed countries, and some methods only some business types. Q5-ZD-P0108, Q5-WC-K0402, Q5-ZD-K0042
- **section 8, line 173:** - Records: Shopify's financial services provider, Stripe's pooled accounts and BigCommerce Payments' account hold it; Salla's (UAE help) and Zid's balances hold sales proceeds before payout, but who holds either balance was not in what was read; a connected gateway pays the merchant's own account. S01-VP-01, Q5-SH-P0033, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-P0057, Q5-ZD-P0035, Q5-SA-H0002, Q5-ZD-H0002, Q5-BC-P0089
- **section 8, line 179:** - Records: Shopify sends Shopify Payments' payouts, processed by partners, in the United States and France; WooPayments sends them to a bank account; Salla's dashboard text, as captured on 8 October 2026, lists transfers "من سلة إلى حسابك البنكي" (observed); Zid deposits on set days by country; BigCommerce Payments pays out to a linked bank or PayPal account. S01-VP-03, Q5-SH-P0076, Q5-WC-P0027, Q5-SA-P0040, Q5-ZD-P0041, Q5-BC-P0074
- **section 8, line 182:** - Records: the own services' processors (Shopify Payments; BigCommerce Payments, "powered by PayPal"); a connected gateway, at Salla "بدلًا من مدفوعات سلة" (dashboard text as captured on 8 October 2026, observed); the merchant, for Salla's bank transfer; and Zid, for cash on delivery through its shipping. S01-VP-04, Q5-SH-K1555, Q5-BC-P0055, Q5-SA-K1639, Q5-SA-P0099, Q5-ZD-P0070
- **section 8, line 185:** - Records: Shopify is the merchant's agent "to deliver information and instructions on your behalf"; Stripe, "for the limited purpose of directing, receiving, holding and settling funds"; Zid executes "payment processes on their behalf" (official pages); Salla passes label amounts on the merchant's behalf (dashboard text as captured on 8 October 2026, observed). BigCommerce's "No agency" statement is one of no part, naming no one; no reading rests on it. S01-VP-06, Q5-SH-P0002, Q5-WC-P0121, Q5-ZD-P0008, Q5-SA-P0126, Q5-BC-P0129
- **section 8, line 188:** - Records: Shopify deducts refunds from the next payout; Stripe pays out net of fees, disputes and refunds; Zid takes fees from amounts collected, and dues by "الخصم الآلي والمباشر"; Salla's dashboard text, as captured on 8 October 2026, takes postpaid label amounts from the wallet or coming dues (observed). S01-VP-09, Q5-SH-P0094, Q5-WC-P0124, Q5-ZD-P0024, Q5-ZD-P0061, Q5-SA-P0129
- **section 8, line 191:** - Records: Shopify's merchant opens accounts with Payment Processors; WooCommerce's Stripe extension uses the merchant's Stripe account; BigCommerce Payments creates a PayPal platform account per store; Zid's pay-later providers need an account with them; in Salla's store real-merchant, observed on 12 October 2026, the wallet listed "Electronic Payments" and "Cash on Delivery Payments". S01-VP-11, Q5-SH-P0010, Q5-WC-P0023, Q5-BC-P0069, Q5-ZD-P0080, Q5-SA-075
- **section 8, line 194:** - Records: by plan at Salla, by country at Zid, by account country for WooPayments' "pending period"; up to 21 days for a new BigCommerce Payments account's first payments; at most 5 days for Shopify's payment apps to settle. S01-VP-15, Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0033, Q5-BC-P0083, Q5-SH-064
- **section 8, line 203:** - Records: Shopify's terms for the EU, EEA and UK, if the merchant fails its checks, "funds may be held or refunded to your customers"; Zid's terms, after 14 days of uncorrected activation data, "إعادة جميع المبالغ للعملاء النهائيين"; Salla's terms, for a breach, "إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين". S01-VP-21, Q5-SH-P0107, Q5-ZD-P0012, Q5-SA-P0083
- **section 8, line 209:** - Records: with BigCommerce's PayPal Pay Later the shopper owes PayPal, while the merchant will "always get paid"; WooPayments receives "the entire purchase amount immediately"; Shop Pay Installments come with Shopify Payments payouts; Tabby pays Zid's stores directly and collects Salla's payments itself (UAE help). S01-VP-22, Q5-BC-P0095, Q5-WC-P0056, Q5-SH-K1686, Q5-ZD-P0077, Q5-SA-P0102

## The cards

### Q5-ZD-P0041

**Cited at:** section 1, line 44; section 3, line 111; section 5, line 137; section 8, line 179; section 8, line 194

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-040
- bullet: c;end-payout
- placement: decides
- identifier: تفعيل الدفع الالكتروني > تحصيل المدفوعات
- statement: في السعودية يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. لا يوجد رسوم لعملية الإيداع.
- scope: في السعودية; في الكويت
- cite_ids: S01-ZD-C073;S01-ZD-C074;S01-ZD-C075;S01-ZD-C076;S01-ZD-C077;S01-ZD-C078;S01-ZD-C079;S01-ZD-C080
- from: new

**Citation S01-ZD-C073:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: في السعودية
- title: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: …يس ). عليك اتباع الخطوات التالية في حالة الرفض : تصحيح معلومات الحساب في إعدادات المتجر. إعادة تقديم متطلبات التفعيل إيداع المبالغ: يتم إيداع المبالغ المحصلة إلى حسابك البنكي بعد اعتماد المعلومات بشكل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إتمام الشراء. تحصيل المدفوعات : ⟪في السعودية⟫ يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. …

**Citation S01-ZD-C074:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس
- title, opening and note boxes: as for this source's citation above
- in context: …تباع الخطوات التالية في حالة الرفض : تصحيح معلومات الحساب في إعدادات المتجر. إعادة تقديم متطلبات التفعيل إيداع المبالغ: يتم إيداع المبالغ المحصلة إلى حسابك البنكي بعد اعتماد المعلومات بشكل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إتمام الشراء. تحصيل المدفوعات : في السعودية ⟪يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس⟫ الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. لا يوجد رسوم لعملية الإيداع. لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: https://hel…

**Citation S01-ZD-C075:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: الحد الأدنى للإيداع هو 100 ريال.
- title, opening and note boxes: as for this source's citation above
- in context: …لبات التفعيل إيداع المبالغ: يتم إيداع المبالغ المحصلة إلى حسابك البنكي بعد اعتماد المعلومات بشكل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إتمام الشراء. تحصيل المدفوعات : في السعودية يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس ⟪الحد الأدنى للإيداع هو 100 ريال.⟫ رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. لا يوجد رسوم لعملية الإيداع. لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: https://help.zid.sa/wp-content/uploads/2025/…

**Citation S01-ZD-C076:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع.
- title, opening and note boxes: as for this source's citation above
- in context: …يداع المبالغ المحصلة إلى حسابك البنكي بعد اعتماد المعلومات بشكل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إتمام الشراء. تحصيل المدفوعات : في السعودية يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. ⟪رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع.⟫ في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. لا يوجد رسوم لعملية الإيداع. لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: سوف تتعلم: تفعيل المدفوعات مراجعة المعلومات واستقبال عمليات الدفع التقييمات والمراجعات 0 0 من أص…

**Citation S01-ZD-C077:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: في الكويت
- title, opening and note boxes: as for this source's citation above
- in context: …علومات بشكل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إتمام الشراء. تحصيل المدفوعات : في السعودية يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. ⟪في الكويت⟫ يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. لا يوجد رسوم لعملية الإيداع. لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: سوف تتعلم: تفعيل المدفوعات مراجعة المعلومات واستقبال عمليات الدفع التقييمات والمراجعات 0 0 من أصل 5 نجوم (…

**Citation S01-ZD-C078:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس.
- title, opening and note boxes: as for this source's citation above
- in context: …ل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إتمام الشراء. تحصيل المدفوعات : في السعودية يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت ⟪يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس.⟫ الحد الأدنى للإيداع هو 1 دينار. لا يوجد رسوم لعملية الإيداع. لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: سوف تتعلم: تفعيل المدفوعات مراجعة المعلومات واستقبال عمليات الدفع التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars …

**Citation S01-ZD-C079:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: الحد الأدنى للإيداع هو 1 دينار.
- title, opening and note boxes: as for this source's citation above
- in context: …ء. تحصيل المدفوعات : في السعودية يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. ⟪الحد الأدنى للإيداع هو 1 دينار.⟫ لا يوجد رسوم لعملية الإيداع. لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: سوف تتعلم: تفعيل المدفوعات مراجعة المعلومات واستقبال عمليات الدفع التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم متطلبات تفع…

**Citation S01-ZD-C080:** `https://help.zid.sa/activate-online-payments/` | تحصيل المدفوعات | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: لا يوجد رسوم لعملية الإيداع.
- title, opening and note boxes: as for this source's citation above
- in context: … يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. في الكويت يتم إيداع المبالغ في حسابك البنكي بشكل يومي خلال أيام العمل الرسمية : الأحد ، الاثنين ، الثلاثاء ، الأربعاء ،الخميس. الحد الأدنى للإيداع هو 1 دينار. ⟪لا يوجد رسوم لعملية الإيداع.⟫ لمزيد من المعلومات يرجى الإطلاع على الفيديو التالي: سوف تتعلم: تفعيل المدفوعات مراجعة المعلومات واستقبال عمليات الدفع التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم متطلبات تفعيل الدفع الالكتروني ( لوحة ال…

### Q5-ZD-P0011

**Cited at:** section 1, line 45; section 2, line 88

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-010
- bullet: a;c
- placement: responsible
- identifier: شروط وأحكام زد باي > الشروط العامة
- statement: يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة “charge back ” أو المبالغ التي تخص دعاوى الاحتيال “Fraud” و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية، ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة “chargeback” المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي.
- scope: السعودية; الكويت
- cite_ids: S01-ZD-C013;S01-ZD-C014;S01-ZD-C015;S01-ZD-C016
- from: index:ZD-C-007:ZD-S-0584
- note: The section حدود المسؤولية of both documents repeats the deduction right in shorter words.

**Citation S01-ZD-C013:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الشروط العامة | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة “charge back ” أو المبالغ التي تخص دعاوى الاحتيال “Fraud” و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية
- title: Zid | Create your online store with modern retail services
- in context: …م أو الضرائب التي قد يكون التاجر مسؤولاً عن دفعها بموجب هذه الأحكام والشروط أو أي نظام ساري في المملكة العربية السعودية بما في ذلك نظام ضريبة القيمة المضافة، سواء بزيادة الأسعار أو غير ذلك، أو دفع أي تكلفة تمويل مطلوبة تتعلق بالبطاقات المستخدمة عبر الخدمة. لا يحق للتاجر استخدام خدمة زد باي بخلاف مانصت عليه شروط وأحكام الخدمة. يقر التاجر ويفهم أن معاملات "Apple Pay " غير محمية بطريقة ثلاثية الأبعاد(3D Secure)من قبل بعض البنوك وأنظمة بطاقات الدفع. ⟪يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة "charge back " أو المبالغ التي تخص دعاوى الاحتيال "Fraud" و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية⟫، ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة "chargeback" المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي. يقر ويفهم التاجر الذي يستخدم طريقة الدفع "Apple Pay" أنه خاضع لشروط وأحكام شركة أبل (Apple Pay Merchant Terms) وأن زد باي غير مسؤولة عن عدم امتثال التاجر لهذه الشروط. الأنشطة المحظورة: ل…

**Citation S01-ZD-C014:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الشروط العامة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة “chargeback” المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي.
- title, opening and note boxes: as for this source's citation above
- in context: … تكلفة تمويل مطلوبة تتعلق بالبطاقات المستخدمة عبر الخدمة. لا يحق للتاجر استخدام خدمة زد باي بخلاف مانصت عليه شروط وأحكام الخدمة. يقر التاجر ويفهم أن معاملات "Apple Pay " غير محمية بطريقة ثلاثية الأبعاد(3D Secure)من قبل بعض البنوك وأنظمة بطاقات الدفع. يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة "charge back " أو المبالغ التي تخص دعاوى الاحتيال "Fraud" و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية، ⟪ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة "chargeback" المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي.⟫ يقر ويفهم التاجر الذي يستخدم طريقة الدفع "Apple Pay" أنه خاضع لشروط وأحكام شركة أبل (Apple Pay Merchant Terms) وأن زد باي غير مسؤولة عن عدم امتثال التاجر لهذه الشروط. الأنشطة المحظورة: لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن: الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية و…

**Citation S01-ZD-C015:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | الشروط العامة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة “charge back ” أو المبالغ التي تخص دعاوى الاحتيال “Fraud” و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية
- title: Zid | Create your online store with modern retail services
- in context: …ا عليه من الطرف المتنازل. كما لا يعتبر تقاعس أي طرف أو تهاونه في إنفاذ أو فرض تنفيذ هذه الشروط والأحكام أو في استعمال حقوقه أو تعويضاته بموجبها أو تخليًا منه عن حقه في تثبيت أو الاستناد إلى تلك الأحكام أو الحقوق أو التعويضات، بل تبقى جميعها سارية ومنتجة لجميع آثارها القانونية. يحق لزد تغيير عمولة عمليات شراء التاجر في أي وقت. يقر التاجر ويفهم أن معاملات "Apple Pay " غير محمية بطريقة ثلاثية الأبعاد(3D Secure)من قبل بعض البنوك وأنظمة بطاقات الدفع. ⟪يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة "charge back " أو المبالغ التي تخص دعاوى الاحتيال "Fraud" و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية⟫، ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة "chargeback" المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي. يقر ويفهم التاجر الذي يستخدم طريقة الدفع "Apple Pay" أنه خاضع لشروط وأحكام شركة أبل (Apple Pay Merchant Terms) وأن زد باي غير مسؤولة عن عدم امتثال التاجر لهذه الشروط. الأنشطة المحظورة: ل…

**Citation S01-ZD-C016:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | الشروط العامة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة “chargeback” المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي.
- title, opening and note boxes: as for this source's citation above
- in context: …ام أو الحقوق أو التعويضات، بل تبقى جميعها سارية ومنتجة لجميع آثارها القانونية. يحق لزد تغيير عمولة عمليات شراء التاجر في أي وقت. يقر التاجر ويفهم أن معاملات "Apple Pay " غير محمية بطريقة ثلاثية الأبعاد(3D Secure)من قبل بعض البنوك وأنظمة بطاقات الدفع. يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة "charge back " أو المبالغ التي تخص دعاوى الاحتيال "Fraud" و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية، ⟪ويقر التاجر ويوافق على أنه يحق لزد باي خصم هذه المبالغ مباشرة من رصيده المتوفر، كما يتعهد التاجر بسداد أي مبالغ تم خصمها من زد باي بسبب الاحتيال أو عمليات رد المبالغ المدفوعة "chargeback" المتعلقة بأنشطة التاجر في حال لم يكن لديه رصيد متوفر في حسابه لدى زد باي.⟫ يقر ويفهم التاجر الذي يستخدم طريقة الدفع "Apple Pay" أنه خاضع لشروط وأحكام شركة أبل (Apple Pay Merchant Terms) وأن زد باي غير مسؤولة عن عدم امتثال التاجر لهذه الشروط. الأنشطة المحظورة: لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو دولة الكويت أو بلد النشاط، تتضمن: الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخ…

### Q5-ZD-P0067

**Cited at:** section 1, line 46; section 2, line 90

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-066
- bullet: c;end-payout
- placement: decides
- identifier: الاستقطاع للمحفظة ( لوحة التحكم الجديدة )
- statement: تتيح خاصية لك خاصية الاستقطاع للمحفظة من تخصيص جزء من مدفوعات الطلبات بشكل تلقائي ليُحوَّل إلى محفظة زد الخاصة بك
- cite_ids: S01-ZD-C130
- from: new

**Citation S01-ZD-C130:** `https://help.zid.sa/wallet-split/` | opening paragraph | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/168-help.zid.sa/text.txt` (4458 bytes), fetched 2026-10-12T04:53:40Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/070-help.zid.sa/text.txt` (4458 bytes), fetched 2026-10-12T10:50:46Z, captured
- quote: تتيح خاصية لك خاصية الاستقطاع للمحفظة من تخصيص جزء من مدفوعات الطلبات بشكل تلقائي ليُحوَّل إلى محفظة زد الخاصة بك
- title: زد - مركز المساعدة - الاستقطاع للمحفظة ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - الاستقطاع للمحفظة ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الرئيسية إعدادات المتجر الاستقطاع للمحفظة ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: …ة تواصل معنا مركز المساعدة الرئيسية إعدادات المتجر الاستقطاع للمحفظة ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال الرئيسية الاستقطاع للمحفظة ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 6, 2026 ⟪تتيح خاصية لك خاصية الاستقطاع للمحفظة من تخصيص جزء من مدفوعات الطلبات بشكل تلقائي ليُحوَّل إلى محفظة زد الخاصة بك⟫ يساعد ذلك في ضمان توفر رصيد دائم لتغطية المصاريف الأساسية مثل شراء بوليصات الشحن، دون الحاجة لانتظار تحويل الأرباح بالكامل إلى الحساب البنكي. يمكنك الوصول الى خاصية الاستقطاع للمحفظة من خلال اعلى الصفحة الرئيسية بعد ذلك , اختيار إدارة المحفظة ملاحظة : خاصية الاستقطاع للمحفظة متوفرة فقط للتجار السعوديين والكويتيين المفعلين لمدفوعات زد ( زد باي ) إعداد وتفعيل الاستقطاع للمحفظة : للبدء في إعداد استقطاع مبلغ من المحفظة قم بالضغط على ايقونة إعداد الا…

### Q5-ZD-P0107

**Cited at:** section 1, line 47; section 2, line 83

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-106
- bullet: a;end-payout
- placement: responsible
- identifier: جاوبنا على أسئلتك > كيف أستقبل المدفوعات؟
- statement: المدفوعات توصل لحسابك مباشرة عن طريق بوابات الدفع الإلكترونية، وتحصل على تقارير مفصله عن كل عملية
- scope: عملاء Paymob
- cite_ids: S01-ZD-C210;S01-ZD-C211
- from: new
- note: Landing page offering a Zid store to Paymob's customers; the same question and answer appear on https://zid.sa/ar/mispay/. The answer opens on click.

**Citation S01-ZD-C210:** `https://zid.sa/ar/paymob/` | جاوبنا على أسئلتك، كيف أستقبل المدفوعات؟ (answer held in the page's embedded data) | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/125-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/125-zid.sa/raw.html` (280492 bytes), fetched 2026-10-12T10:51:29Z, captured
- quote: المدفوعات توصل لحسابك مباشرة عن طريق بوابات الدفع الإلكترونية، وتحصل على تقارير مفصله عن كل عملية
- title: افتح متجرك و بيع في أقل من 24 ساعة
- in context: …\"languages_id\":{\"name\":\"ar\"}},{\"id\":276,\"question\":\"How do I ship orders to customers?\",\"answer\":\"Connect your store instantly and for free with Zid Ship and ship your orders with 35+ shipping companies under one electronic contract.\",\"languages_id\":{\"name\":\"en\"}}]}},{\"id\":140,\"questions_id\":{\"id\":\"6d2d8c7f-0ee1-4660-ba00-f392719b39ea\",\"translations\":[{\"id\":277,\"question\":\"كيف أستقبل المدفوعات؟\",\"answer\":\"⟪المدفوعات توصل لحسابك مباشرة عن طريق بوابات الدفع الإلكترونية، وتحصل على تقارير مفصله عن كل عملية⟫\",\"languages_id\":{\"name\":\"ar\"}},{\"id\":278,\"question\":\"How do I receive payments?\",\"answer\":\"Payments arrive directly to your account through electronic payment gateways, and you get detailed reports on every transaction.\",\"languages_id\":{\"name\":\"en\"}}]}}]}}]}}]]}]}]}]\n"])</script><script>self.__next_f.push([1,"c:[[\"$\",\"meta\",\"0\",{\"name\":\"viewport\",\"content\":\"width=device-width, initial-scale=1\"}]]\na:[[\"$\",…

**Citation S01-ZD-C211:** `https://zid.sa/ar/paymob/` | جاوبنا على أسئلتك | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/125-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/125-zid.sa/raw.html` (280492 bytes), fetched 2026-10-12T10:51:29Z, captured
- quote: كيف أستقبل المدفوعات؟
- title: افتح متجرك و بيع في أقل من 24 ساعة
- in context: …لّت كل المشاكل والتحديات وساعدتنا نوفر وقت وجهد براند سما فارما https://samapharma.com/ زد تعاملني كشريك، مو مجرد عميل. وخدمة ربط سعر الذهب مع المتجر وفّرت علي مجهود كبير. مبيعاتي تضاعفت 40× بعد ما أطلقت متجري الإلكتروني مع زد. مجوهرات السمحان https://alsamhan-jewelry.com/ جاوبنا على أسئلتك كم يأخذ وقت إطلاق المتجر؟ هل أحتاج خبرة تقنية؟ هل في تكامل بين الفروع والمتجر الإلكتروني؟ هل أقدر أفعل الدفع والشحن من البداية؟ كيف أشحن الطلبات إلى العملاء؟ ⟪كيف أستقبل المدفوعات؟⟫ جاهز توسع تجارتك وتوصل لعملاء جدد بدون تكاليف إضافية؟ افتح متجرك اليوم واستفيد من العرض الحصري لعملاء Paymob افتح متجرك الآن الحلول المتجر الإلكتروني نقاط البيع (الكاشير) المدفوعات الشحن إدارة المخزون التطبيقات الثيمات منصة مزيد التمويل أدوات التسويق لماذا زد لماذا ابدأ مع زد؟ لماذا أنتقل إلى زد؟ لماذا أتوسع مع زد؟ كيف تخدمك زد الشركات الصغيرة الشركات المتوسطة الشركات الكبيرة حسب نوع المنتج مدير المتجر الفريق المالي فريق العمليات فريق التسويق ال…

### Q5-ZD-P0077

**Cited at:** section 1, line 49; section 2, line 83; section 8, line 209

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-076
- bullet: a;end-payout
- placement: responsible
- identifier: خدمات التقسيط (لوحة التحكم الجديدة ) > خدمة تابي
- statement: تقدم لك تابي حلولاً لتسهيل عمليات التسوق و الدفع من غير فوائد وتقسيم قيمة مدفوعاتهم على 4 دفعات شهرية وتقوم تابي بالدفع للمتاجر مباشرة عن طريق عمليات الشراء المدفوعة
- cite_ids: S01-ZD-C148
- from: index:ZD-C-013:ZD-S-0625

**Citation S01-ZD-C148:** `https://help.zid.sa/bnpl-2/` | خدمة تابي | 2026-10-07 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/090-help.zid.sa/text.txt` (8691 bytes), fetched 2026-10-12T04:52:22Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/050-help.zid.sa/text.txt` (8691 bytes), fetched 2026-10-12T10:50:26Z, captured
- quote: تقدم لك تابي حلولاً لتسهيل عمليات التسوق و الدفع من غير فوائد وتقسيم قيمة مدفوعاتهم على 4 دفعات شهرية وتقوم تابي بالدفع للمتاجر مباشرة عن طريق عمليات الشراء المدفوعة
- title: زد - مركز المساعدة - خدمات التقسيط (لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - خدمات التقسيط (لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي خدمات التقسيط (لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة…
- in context: …مكان ادفع لاحقا بالمتجر في حال تفعيل زد باي في المتجر اتبع التالي: من المدفوعات ← إدارة ثم تفعيل الزر من هنا. ملاحظة : في حال استخدام بوابات دفع اخرى غير زد باي اتبع التالي لتفعيل خدمة إمكان ادفع لاحقا بالمتجر يتطلب أن يكون لديك حساب لديهم , وللتسجيل اتبع التالي : تقدم عبر موقع إمكان هنا ارفع ملفات التسجيل. انسخ مفاتيح الربط وارفقها في خانة تفعيل التطبيق ليتم ربطها في المتجر قم بوضع علامة لتفعيل إمكان لمزيد من المعلومات حول إمكان هنا خدمة تابي : ⟪تقدم لك تابي حلولاً لتسهيل عمليات التسوق و الدفع من غير فوائد وتقسيم قيمة مدفوعاتهم على 4 دفعات شهرية وتقوم تابي بالدفع للمتاجر مباشرة عن طريق عمليات الشراء المدفوعة⟫، والهدف من ذلك زيادة سقف مبيعات التاجر عن طريق توفير خيارات دفع مريحة وميسرة لعملاء المتاجر. يوجد طريقتين لتفعيل تابي : إرسال طلب فتح حساب اعمال في حال لا يوجد لديك حساب في تابي وترغب في تفعيله ، قم بإدخال رمز وثيقة العمل الحر وسنقوم بطلب إنشاء الحساب لك تلقائيا من لوحة التحكم بعد ذلك، قم بالضغط على ايقونة تفعيل 2. لدي حساب تابي للأعمال في حال لديك حساب في تابي وترغب في ربطه، قم بإدخال الرموز التالية : Public key secret key قم بوضع علامة لإظهار …

### Q5-ZD-P0070

**Cited at:** section 1, line 51; section 2, line 84; section 7, line 164; section 8, line 182

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-069
- bullet: a;c;end-payment;end-payout
- placement: responsible
- identifier: الشروط والأحكام > زد شب > خدمة الدفع عند الاستلام (COD)
- statement: هي خدمة تتيح للعميل النهائي الدفع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه. تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر. تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع. التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى شركة الشحن المعنية فوراً وإخطار زد بذلك.
- scope: زد شب (الشحن المباشر)
- cite_ids: S01-ZD-C135;S01-ZD-C136;S01-ZD-C137;S01-ZD-C138
- from: index:ZD-C-015:ZD-S-0641

**Citation S01-ZD-C135:** `https://zid.sa/ar/legal/terms-conditions/` | خدمة الدفع عند الاستلام (COD) | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: هي خدمة تتيح للعميل النهائي الدفع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه.
- title: Zid | Create your online store with modern retail services
- in context: …للتاجر تقديم طلب استرداد مالي لقيمة ما تبقى من رصيد تلك الباقة. يتحمل التاجر/المتجر أي رسوم أو تكاليف إضافية ("التكاليف الإضافية للشحن") والتي يتم تطبيقها من قِبل زد أو شركة الشحن، على سبيل المثال لا الحصر: (الرسوم الجمركية، رسوم الشحنات العكسية والرجيع من العميل النهائي إلى التاجر، وأي رسوم نقل إضافية، والرسوم الحكومية، ورسوم الدفع عند الاستلام، وفروقات الأوزان الإضافية، وأي تكاليف أو خدمات إضافية أخرى تم تطبيقها). خدمة الدفع عند الاستلام (COD) ⟪هي خدمة تتيح للعميل النهائي الدفع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه.⟫ تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر. تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع. التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى ش…

**Citation S01-ZD-C136:** `https://zid.sa/ar/legal/terms-conditions/` | خدمة الدفع عند الاستلام (COD) | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر.
- title, opening and note boxes: as for this source's citation above
- in context: …بيل المثال لا الحصر: (الرسوم الجمركية، رسوم الشحنات العكسية والرجيع من العميل النهائي إلى التاجر، وأي رسوم نقل إضافية، والرسوم الحكومية، ورسوم الدفع عند الاستلام، وفروقات الأوزان الإضافية، وأي تكاليف أو خدمات إضافية أخرى تم تطبيقها). خدمة الدفع عند الاستلام (COD) هي خدمة تتيح للعميل النهائي الدفع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه. ⟪تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر.⟫ تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع. التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى شركة الشحن المعنية فوراً وإخطار زد بذلك. في حال عدم استلام العميل النهائي للشحنة وتحول حالة الطلب إلى (رجيع)، تُعاد رسوم الد…

**Citation S01-ZD-C137:** `https://zid.sa/ar/legal/terms-conditions/` | خدمة الدفع عند الاستلام (COD) | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع.
- title, opening and note boxes: as for this source's citation above
- in context: …سوم الحكومية، ورسوم الدفع عند الاستلام، وفروقات الأوزان الإضافية، وأي تكاليف أو خدمات إضافية أخرى تم تطبيقها). خدمة الدفع عند الاستلام (COD) هي خدمة تتيح للعميل النهائي الدفع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه. تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر. ⟪تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع.⟫ التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى شركة الشحن المعنية فوراً وإخطار زد بذلك. في حال عدم استلام العميل النهائي للشحنة وتحول حالة الطلب إلى (رجيع)، تُعاد رسوم الدفع عند الاستلام فقط إلى محفظة التاجر، بينما لا تُعاد رسوم الشحن الأساسية. التقارير المالية والفواتير يتلقى التاجر تقارير مالية أسبوعية توضح وتفصّل جميع عمليات الشراء والدفع…

**Citation S01-ZD-C138:** `https://zid.sa/ar/legal/terms-conditions/` | خدمة الدفع عند الاستلام (COD) | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى شركة الشحن المعنية فوراً وإخطار زد بذلك.
- title, opening and note boxes: as for this source's citation above
- in context: …فع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه. تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر. تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع. ⟪التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى شركة الشحن المعنية فوراً وإخطار زد بذلك.⟫ في حال عدم استلام العميل النهائي للشحنة وتحول حالة الطلب إلى (رجيع)، تُعاد رسوم الدفع عند الاستلام فقط إلى محفظة التاجر، بينما لا تُعاد رسوم الشحن الأساسية. التقارير المالية والفواتير يتلقى التاجر تقارير مالية أسبوعية توضح وتفصّل جميع عمليات الشراء والدفع المتعلقة بخدمات الشحن المباشر التي تم خصمها من المحفظة، بما يشمل كافة التكاليف الأساسية للشحن والتكاليف الإضافية للشحن. بناءً على هذه التقارير والتسويات تُصدر الفواتير الخاصة بالتاجر، والذي يحق…

### Q5-ZD-P0080

**Cited at:** section 2, line 66; section 8, line 191

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-079
- bullet: b
- placement: decides
- identifier: خدمات التقسيط (لوحة التحكم الجديدة ) > خدمة مدفوع
- statement: لتفعيل خدمة مدفوع بالمتجر يتطلب أن يكون لديك حساب لديهم
- cite_ids: S01-ZD-C151
- from: index:ZD-C-013:ZD-S-0622

**Citation S01-ZD-C151:** `https://help.zid.sa/bnpl-2/` | خدمة مدفوع | 2026-10-07 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/090-help.zid.sa/text.txt` (8691 bytes), fetched 2026-10-12T04:52:22Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/050-help.zid.sa/text.txt` (8691 bytes), fetched 2026-10-12T10:50:26Z, captured
- quote: لتفعيل خدمة مدفوع بالمتجر يتطلب أن يكون لديك حساب لديهم
- title: زد - مركز المساعدة - خدمات التقسيط (لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - خدمات التقسيط (لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي خدمات التقسيط (لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة…
- in context: …راء لعملائك من خلال دفع قيمة المنتجات على أقساط مرنة، مما يعزز قدرتهم على الشراء ويساهم في زيادة مبيعات متجرك وجذب شرائح أوسع من العملاء. يمكنك الوصول الى خيارات الدفع بالتقسيط من خلال : لوحة التحكم > المدفوعات > الدفع لاحقاً خدمات الدفع بالتقسيط بإمكانك تفعيل خدمات التقسيط المربوطة مع زد وهي كالآتي خدمة مدفوع مدفوع يساعدك تزيد مبيعات متجرك لأنه يسمح لعملائك بتقسيم فواتيرهم لدفعات مرنة ومريحة، خلك مع مدفوع اليوم وكون جزء من مستقبل التجارة الذكية ⟪لتفعيل خدمة مدفوع بالمتجر يتطلب أن يكون لديك حساب لديهم⟫ , وللتسجيل اتبع التالي : تقدم عبر موقع مدفوع هنا انسخ مفاتيح الربط وارفقها في خانة تفعيل التطبيق ليتم ربطها في المتجر خدمة إمكان - ادفع لاحقا: تقدم شركة امكان خدمة "ادفع لاحقاً" المتوافقة مع الشريعة عدد دفعات أكبر مما يزيد مبيعاتك بنسبة تصل الى ٢٥٪؜ مقارنه مع مقدمي الخدمة الآخرين وذلك بتقسيم مشتريات عملائك على ٥ دفعات بسعر الكاش مما يتيح لعميلك قوة شرائية اعلى وزيادة مبلغ السله دون عناء! لتفعيل خدمة إمكان ادفع لاحقا بالمتجر في حال تفعيل زد باي ف…

### Q5-ZD-K0042

**Cited at:** section 2, line 69; section 3, line 104; section 7, line 168

**The same record as Q2-ZD-K0042,** whose card is in `Q2-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: لا. في زد باي متاح لك حرية تفعيل الشبكات بحسب ما تراه مناسب لك, سواء كنت فرد أم مؤسسة بإمكانك التحكم بتفعيل جميع الشبكات باستثناء شبكة كي نت فهي متاحة للمؤسسات والشركات فقط.
- scope: 

### Q5-ZD-P0061

**Cited at:** section 2, line 89; section 8, line 188

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-060
- bullet: a;c
- placement: responsible
- identifier: الشروط والأحكام > محفظة زد > خصم الخدمات والمستحقات من المحفظة
- statement: يحق لزد الخصم الآلي والمباشر من أي مبالغ تُودع أو تُدخل في محفظة التاجر وذلك فور إيداعها لتسوية وسداد أي مستحقات، أو فروقات مالية، أو مبالغ مطالب بها لصالح زد كلما كان ذلك ضرورياً.
- cite_ids: S01-ZD-C109
- from: index:ZD-C-017:ZD-S-0657

**Citation S01-ZD-C109:** `https://zid.sa/ar/legal/terms-conditions/` | خصم الخدمات والمستحقات من المحفظة | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: يحق لزد الخصم الآلي والمباشر من أي مبالغ تُودع أو تُدخل في محفظة التاجر وذلك فور إيداعها لتسوية وسداد أي مستحقات، أو فروقات مالية، أو مبالغ مطالب بها لصالح زد كلما كان ذلك ضرورياً.
- title: Zid | Create your online store with modern retail services
- in context: …والات الخارجية، أو خارج خدمات منصة زد، أو استخدامه لغير الأغراض المخصصة له. المبالغ التي تضاف لرصيد التاجر كمكافآت ترويجية أو كاش باك يمكن الاستفادة منها في شراء الخدمات أو المنتجات داخل منصة زد ولا يمكن سحبها أو استردادها من المحفظة نهائياً. خصم الخدمات والمستحقات من المحفظة يحق لزد الخصم مباشرة من رصيد التاجر في المحفظة بقيمة توازي الخدمة المراد الاستفادة منها كعملية شرائية، على سبيل المثال لا الحصر خصم رسوم التوصيل، الأوزان الإضافية، ... إلخ. ⟪يحق لزد الخصم الآلي والمباشر من أي مبالغ تُودع أو تُدخل في محفظة التاجر وذلك فور إيداعها لتسوية وسداد أي مستحقات، أو فروقات مالية، أو مبالغ مطالب بها لصالح زد كلما كان ذلك ضرورياً.⟫ آلية استيفاء المبالغ في حالة عدم توافر رصيد بالمحفظة في حال عدم وجود رصيد كافٍ في محفظة التاجر مع وجود مستحقات على التاجر مقابل خدمات تمت الاستفادة منها، يتم خصمها من القيمة الصفرية في الرصيد على أن تسجل بالسالب. في حال استمرار رصيد التاجر لدى محفظة زد بقيمة سالبة كمستحقات مستحقة الدفع لصالح زد نظير خدمات قدمتها له، يحق لزد اتخاذ الإجراءات التالية: سحب المبالغ من رصيد المحفظة. سحب أي مبالغ فور إيداعها في المحفظة، حتى تسديد المستحقات بالكامل. سحب…

### Q5-ZD-P0108

**Cited at:** section 7, line 168

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-107
- bullet: e
- placement: decides
- identifier: شروط وأحكام زد باي > الشروط العامة
- statement: يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي. ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم.
- scope: السعودية; الكويت
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C212;S01-ZD-C213;S01-ZD-C214;S01-ZD-C215
- from: index:ZD-C-001:ZD-S-0529

**Citation S01-ZD-C212:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الشروط العامة | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي.
- title: Zid | Create your online store with modern retail services
- in context: …ك شروط وأحكام زد باي الشروط والأحكام: تمثل الشروط والأحكام المذكورة أدناه العقد المبرم بين مستخدمي زد باي وشركة زد. التعريفات: زد باي: هي خدمة تمكين التاجر من تنفيذ عمليات البيع والتجارة الإلكترونية من خلال مقدمي خدمات الدفع على منصة تابعة لزد، ويشار إليها -أيضًا- في هذه الشروط والأحكام ب (" زد باي، أو الخدمة"). تفعيل الخدمة: وهي عملية طلب التاجر لتفعيل خدمة زد باي. التاجر: هو المستخدم المشترك في زد باي، والمالك لمتجر على منصة زد. الشروط العامة: ⟪يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي.⟫ ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم. المبالغ المنفذة في عمليات البيع بواسطة زد باي لابد أن تخدم نفس الغرض المذكور في الفاتورة وتتوافق مع الأنشطة المرخصة للتاجر. الاسم التجاري الموضح في الفاتورة لابد أن يمثل التاجر وأنشطته المصرح بها. يجب أن يكون التاجر قد تحصّل على متجره وفق شروط وأحكام الدفع الإلكتروني المعتمدة في زد عند الاشتراك ومتوافقة مع جميع المتطلبات النظامية والقانوني…

**Citation S01-ZD-C213:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الشروط العامة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم.
- title, opening and note boxes: as for this source's citation above
- in context: …التاجر من تنفيذ عمليات البيع والتجارة الإلكترونية من خلال مقدمي خدمات الدفع على منصة تابعة لزد، ويشار إليها -أيضًا- في هذه الشروط والأحكام ب (" زد باي، أو الخدمة"). تفعيل الخدمة: وهي عملية طلب التاجر لتفعيل خدمة زد باي. التاجر: هو المستخدم المشترك في زد باي، والمالك لمتجر على منصة زد. الشروط العامة: يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي. ⟪ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم.⟫ المبالغ المنفذة في عمليات البيع بواسطة زد باي لابد أن تخدم نفس الغرض المذكور في الفاتورة وتتوافق مع الأنشطة المرخصة للتاجر. الاسم التجاري الموضح في الفاتورة لابد أن يمثل التاجر وأنشطته المصرح بها. يجب أن يكون التاجر قد تحصّل على متجره وفق شروط وأحكام الدفع الإلكتروني المعتمدة في زد عند الاشتراك ومتوافقة مع جميع المتطلبات النظامية والقانونية، التاجر وحده مسؤولا عن الالتزام بكافة هذه المتطلبات. يوافق التاجر المشترك في الخدمة على أن زد باي قد تطلب …

**Citation S01-ZD-C214:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | الشروط العامة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي.
- title: Zid | Create your online store with modern retail services
- in context: …دخول أنشئ متجرك شروط وأحكام زد باي - الكويت الشروط والأحكام: تمثل الشروط والأحكام المذكورة أدناه العقد المبرم بين مستخدمي زد باي وشركة زد. التعريفات: زد باي: هي خدمة تمكن التاجر من تنفيذ عمليات البيع من خلال مقدمي خدمات الدفع على منصة تابعة لزد، ويشار إليها -أيضًا- في هذه الشروط والأحكام ب ("زد باي، أو الخدمة"). تفعيل الخدمة: وهي عملية طلب التاجر لتفعيل خدمة زد باي. التاجر: هو المستخدم المشترك في زد باي، والمالك لمتجر على منصة زد. الشروط العامة: ⟪يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي.⟫ ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم. المبالغ المنفذة في عمليات البيع بواسطة زد باي لابد أن تخدم نفس الغرض المذكور في الفاتورة وتتوافق مع الأنشطة المرخصة للتاجر. الاسم التجاري الموضح في الفاتورة لابد أن يمثل التاجر وأنشطته المصرح بها. يجب أن يكون التاجر قد تحصّل على متجره وفق الشروط والأحكام المعتمدة في زد عند الاشتراك ومتوافقة مع جميع المتطلبات النظامية والقانونية، التاجر وحد…

**Citation S01-ZD-C215:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | الشروط العامة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم.
- title, opening and note boxes: as for this source's citation above
- in context: … زد باي: هي خدمة تمكن التاجر من تنفيذ عمليات البيع من خلال مقدمي خدمات الدفع على منصة تابعة لزد، ويشار إليها -أيضًا- في هذه الشروط والأحكام ب ("زد باي، أو الخدمة"). تفعيل الخدمة: وهي عملية طلب التاجر لتفعيل خدمة زد باي. التاجر: هو المستخدم المشترك في زد باي، والمالك لمتجر على منصة زد. الشروط العامة: يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي. ⟪ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية داخل بلادهم.⟫ المبالغ المنفذة في عمليات البيع بواسطة زد باي لابد أن تخدم نفس الغرض المذكور في الفاتورة وتتوافق مع الأنشطة المرخصة للتاجر. الاسم التجاري الموضح في الفاتورة لابد أن يمثل التاجر وأنشطته المصرح بها. يجب أن يكون التاجر قد تحصّل على متجره وفق الشروط والأحكام المعتمدة في زد عند الاشتراك ومتوافقة مع جميع المتطلبات النظامية والقانونية، التاجر وحده مسؤولا عن الالتزام بكافة هذه المتطلبات. يوافق التاجر المشترك في الخدمة على أن زد باي قد تطلب معلومات إضافي…

### Q5-ZD-P0035

**Cited at:** section 8, line 173

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-034
- bullet: a;b;c
- placement: where
- identifier: كشف الحساب والإيداعات > لم يتم الإيداع
- statement: وهي المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد ، إذ يتم إيداعها في أقرب يوم للتحصيل خلال الأيام التالية ( الأحد ، الثلاثاء ، الخميس).
- cite_ids: S01-ZD-C067
- from: new

**Citation S01-ZD-C067:** `https://help.zid.sa/deposits_zidpay/` | لم يتم الإيداع | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/110-help.zid.sa/text.txt` (11593 bytes), fetched 2026-10-12T04:52:42Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/052-help.zid.sa/text.txt` (11593 bytes), fetched 2026-10-12T10:50:28Z, captured
- quote: وهي المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد ، إذ يتم إيداعها في أقرب يوم للتحصيل خلال الأيام التالية ( الأحد ، الثلاثاء ، الخميس).
- title: زد - مركز المساعدة - خصائص زد باي | كشف الحساب و الإيداعات
- the page opens: زد - مركز المساعدة - خصائص زد باي كشف الحساب و الإيداعات menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي خصائص زد باي كشف الحساب و الإيداعات عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة ا…
- in context: …لرسوم التي يتم استقطاعها بحسب شبكة الدفع المستخدمة التي تتمثل باستقطاع نسبة من العملية الأساسية. ● رسوم تشغيلية: الرسوم التي يتم استقطاعها بحسب شبكة الدفع المستخدمة التي تتمثل باستقطاع رسوم من العملية الأساسية. ● رسوم العملية: قيمة نسبة الرسوم باستثناء ضريبة القيمة المضافة. ● ضريبة القيمة المضافة: قيمة الضريبة. المبلغ المستحق: قيمة عملية الشراء بعد استقطاع نسبة الرسوم (رسوم العملية). ● الرصيد : القيمة التراكمية للمبالغ المستحقة. لم يتم الإيداع : ⟪وهي المبالغ المتوفرة في رصيد حسابك في زد باي و لكن لم يتم إيداعها إلى حسابك البنكي بعد ، إذ يتم إيداعها في أقرب يوم للتحصيل خلال الأيام التالية ( الأحد ، الثلاثاء ، الخميس).⟫ ● رقم العملية: الرقم المعرّف لعملية الدفع الإلكتروني ● التاريخ والوقت: تاريخ و وقت حدوث العملية ● نوع العملية: في حال كانت شراء أو استرداد ● رقم الطلب: رقم الطلب في المتجر الإلكتروني ● قيمة العملية: المبلغ الإجمالي لعملية الشراء. ● شبكة الدفع: شبكة الدفع المستخدمة من قبل العميل النهائي في عملية الشراء. ● نسبة الرسوم : الرسوم التي يتم استقطاعها بحسب شبكة الدفع المستخدمة التي تتمثل باستقطاع نسبة من العملية الأساسية. ● رسوم تشغيلية: الرسوم التي يتم…

### Q5-ZD-P0008

**Cited at:** section 8, line 185

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-007
- bullet: a
- placement: responsible
- identifier: Zid Pay Terms and Conditions > General Conditions
- statement: Merchants authorize Zid to execute payment processes on their behalf upon using the service.
- scope: Saudi Arabia
- cite_ids: S01-ZD-C006
- from: new
- note: English page for the Saudi Zid Pay terms; the Arabic wording is S01-ZD-003.

**Citation S01-ZD-C006:** `https://zid.sa/en/legal/zidpay-terms-conditions-sa/` | General Conditions | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/195-zid.sa/text.txt` (54 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/195-zid.sa/raw.html` (166411 bytes), fetched 2026-10-12T04:54:01Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/128-zid.sa/text.txt` (54 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/128-zid.sa/raw.html` (166411 bytes), fetched 2026-10-12T10:51:32Z, captured
- quote: Merchants authorize Zid to execute payment processes on their behalf upon using the service.
- title: Zid | Create your online store with modern retail services
- in context: …iance in providing required details may result in service suspension or contract termination. Merchants must notify Zid Pay of any changes in their business activities. This agreement is governed by the laws of Saudi Arabia, and disputes arising between the merchant and Zid Pay fall under the jurisdiction of courts in Riyadh. Zid Pay reserves the right to modify these terms and conditions at any time and will notify the merchant of such changes. ⟪Merchants authorize Zid to execute payment processes on their behalf upon using the service.⟫ If a merchant suspects unauthorized or incorrect payment transactions, they must notify Zid Pay immediately by submitting a ticket. Delay in reporting may result in lost opportunities for claim recovery. Zid Pay will make efforts to retrieve funds from incorrect recipients but does not guarantee success. Any waiver of rights or obligations under these terms must be in writing and signed by the waiving party. Lack of enforcement does not constitu…

### Q5-ZD-P0012

**Cited at:** section 8, line 203

**The same record as Q3-ZD-P0012,** whose card is in `Q3-zid-3.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين.
- scope: السعودية; الكويت
