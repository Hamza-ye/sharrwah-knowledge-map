# Cards: Q5 on salla

21 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 42:** - Through the platform's own service, money goes into a balance, then to the merchant's bank account, matching by role on stated pages and Zid's terms (official): Salla's "رصيد المدفوعات الإلكترونية" comes before the transfer to the bank account; Zid's terms add "المبلغ المستحق لرصيد التاجر" after fees; WooPayments adds the payment "(minus our fees)" to the balance; BigCommerce Payments and Shopify Payments pay out to the merchant's bank account. Q5-SA-P0006, Q5-ZD-P0024, Q5-WC-P0024, Q5-BC-P0074, Q5-SH-P0060
- **section 1, line 44:** - When it is paid out, and at what level: Salla by plan, from weekly on Plus to daily on Special; Zid by country; WooPayments daily, "the default for almost all accounts", changeable per account; BigCommerce Payments holds a new account's initial payments "for up to 21 days". They match by role; the level differs. Q5-SA-P0020, Q5-SA-P0022, Q5-ZD-P0041, Q5-WC-P0036, Q5-BC-P0083
- **section 1, line 45:** - Deductions come off first, matching by role, in the own services' terms (official pages): Shopify may hold funds in a Reserve Account; Stripe pays out "net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe"; زد باي takes chargebacks "مباشرة من رصيده المتوفر". Services, financing and apps draw on it too: Salla's dashboard text, as captured on 8 October 2026, holds label amounts to pay "نيابةً عنك إلى شركة الشحن", and its financing takes "%25 من صافي المبيعات لكل دفعة" (observed); a dropshipping app may "temporarily withhold a specific amount of money" (Salla's developer docs). Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0131, Q5-SA-K1690
- **section 1, line 46:** - Some keep separate balances, matching by role: in Salla's store real-merchant, observed on 12 October 2026, the wallet summary listed "Wallet", "Electronic Payments" and "Cash on Delivery Payments"; Zid's الاستقطاع للمحفظة moves part of order payments into محفظة زد; Shopify's Shop Cash comes in the same payouts; WooPayments' FROD balance is "a special bucket of funds inside your WooPayments account". Q5-SA-075, Q5-ZD-P0067, Q5-SH-074, Q5-WC-042
- **section 1, line 47:** - Through a gateway the merchant connects, money goes to the merchant's own account with it, matching by role: funds are in "your merchant account with your merchant service provider" (BigCommerce); "the purchase amount is transferred to your merchant account" (Shopify); Salla's dashboard text, as captured on 8 October 2026, collects through the gateway "بدلًا من مدفوعات سلة" (observed); "المدفوعات توصل لحسابك مباشرة" (Zid's Paymob page). Where the money is held between the buyer's payment and its transfer was not in what was read on Shopify. WooCommerce says only that it is "unable to assist with Stripe account issues", payouts among them: a statement of no part, naming no one. Q5-BC-P0089, Q5-SH-P0050, Q5-SA-K1639, Q5-ZD-P0107, Q5-SH-N02, Q5-WC-P0159
- **section 1, line 49:** - Pay-later providers pay the merchant directly, or into the platform's own service: at Salla (UAE help), "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة"; at Zid, "تقوم تابي بالدفع للمتاجر مباشرة"; with BigCommerce's PayPal Pay Later, "you, the merchant, always get paid"; these match by role. Shopify and WooCommerce differ: Shop Pay Installments payouts "are included with your Shopify Payments payouts", and WooPayments receives "the entire purchase amount immediately". Q5-SA-P0102, Q5-ZD-P0077, Q5-BC-P0095, Q5-SH-K1686, Q5-WC-P0056
- **section 1, line 50:** - With methods outside any provider, the buyer pays the merchant and the order waits, matching by role: Salla's customer transfers "مباشرة من حسابه البنكي إلى حسابك"; BigCommerce's pay "directly into your bank account"; the order is "marked as unpaid" (Shopify), in "Awaiting Payment" (BigCommerce), or on hold, `OrderStatus::ON_HOLD` in WooCommerce's shipped code. In Shopify's store demo-fake-dev-store (countryCode YE), observed on 30 September 2026, the order then read "You manually marked YER699.95 as paid for this order." Q5-SA-P0099, Q5-BC-P0116, Q5-SH-K1736, Q5-BC-P0115, Q5-WC-K0037, Q5-SH-093
- **section 1, line 51:** - Cash on delivery is settled with the merchant, or collected through the platform, matching by role: at Salla, with a carrier outside its labels, it is settled "مباشرة بين التاجر وشركة الشحن", while through its labels "تحوِّل شركة الشحن المبلغ إلى سلة" (dashboard text, as captured on 8 October 2026, observed); through Zid's shipping, "تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم" (its terms, official); WooCommerce's cash on delivery takes payment "at the time of delivery". Q5-SA-P0092, Q5-SA-P0042, Q5-ZD-P0070, Q5-WC-P0097
- **section 2, line 65:** - **Provider account**: the merchant's own account with a provider, connected with the credentials of an account it holds, or applied for through Sharrwah. The provider decides each application; Sharrwah shows its state: applied, approved, rejected or connected. Q5-SA-053, Q5-SA-057, Q5-BC-P0048
- **section 2, line 66:** - It draws on Salla's choice between an existing account and a request the provider may reject, the own account Zid's pay-later providers need, BigCommerce's application and underwriting, and Shopify's apps, where the merchant may "log in or create an account with the payment provider". Q5-SA-053, Q5-SA-057, Q5-ZD-P0080, Q5-BC-P0048, Q5-SH-053
- **section 2, line 67:** - Why: rule 3; whose account receives the money fixes the money route and the contract. An account applied for through Sharrwah may count as one opened through Sharrwah, under the guard (section 5). Q5-BC-P0048, Q5-SA-053
- **section 2, line 73:** - It draws on the activation and payments permissions the platforms show, Shopify's owner-only provider change and one card provider at a time, BigCommerce's change log, Salla's market selector and BigCommerce's methods per currency. Q5-SH-K0193, Q5-SA-K1509, Q5-BC-072, Q5-SA-016, Q5-BC-074
- **section 2, line 82:** - **Money route**: for each provider, and for manual methods, the path the buyer's money takes to the merchant's own bank account. On the **direct route**, it goes to the merchant's own account with the provider, or straight from buyer to merchant; Sharrwah never holds it, and its records show the payment, not the payout. On the **held route**, it waits in a **merchant balance**, held before payout by a payment company in an account opened through Sharrwah, or by Sharrwah itself. This proposal provides for the held route, in its data model and as a later part; under the founder's guard, it goes live nowhere without the founder's decision. Q5-BC-P0089, Q5-SA-K1639, Q5-SA-P0006
- **section 2, line 83:** - It draws on the direct route the platforms show for gateways the merchant connects, pay-later providers that pay the store, and bank transfer, and on the held route of their own services. Q5-SH-P0050, Q5-ZD-P0107, Q5-ZD-P0077, Q5-SA-P0099, Q5-WC-P0024, Q5-ZD-P0024
- **section 2, line 84:** - Cash on delivery collected through a carrier Sharrwah contracts would pass through Sharrwah, as it passes through Salla and Zid: a held route. Cash the merchant collects is direct. Q5-SA-P0042, Q5-ZD-P0070, Q5-SA-P0092
- **section 2, line 87:** - **Merchant balance**, with its payouts, on the held route only, and live only by the founder's decision: a ledger, per merchant, holder and currency, of credits from payments and debits for fees, refunds, chargebacks, reserves and other deductions, each debit naming the party it pays and the merchant's authorization for it; and payouts of the amount available to the merchant's own bank account, given at verification, on a schedule. Q5-ZD-P0024, Q5-SA-P0055, Q5-WC-P0124
- **section 2, line 88:** - It draws on the platforms' own balances and their deductions and reserves, Salla's label holds under the merchant's authorization, and the payout account Salla takes at verification. Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0055
- **section 2, line 89:** - Why: rule 3, the ledger's shape is expensive to change; rule 2, a deduction plugs into the ledger without touching orders. Q5-SA-P0126, Q5-ZD-P0061
- **section 2, line 90:** - Where the platforms differ, one balance with credits folded in (Shopify's Shop Cash; WooPayments' FROD bucket) against several wallets (Salla's observed store; Zid's wallet), typed entries in one ledger can show either; the choice is kept open. Q5-SH-074, Q5-WC-042, Q5-SA-075, Q5-ZD-P0067
- **section 3, line 102:** - On the held route only, financing repaid from the balance, and apps that hold amounts from it, could plug in. Q5-SA-P0131, Q5-SA-K1690
- **section 3, line 107:** - Activated methods, and the one provider for each, are set per store, and per market or currency where the store has them, by staff holding the payments permission. Q5-SH-K1524, Q5-SA-016, Q5-BC-074, Q5-SH-K0193
- **section 3, line 110:** - A provider's money route is set by its own terms; which routes may run at a place, by Sharrwah, and any held route by the founder. Q5-BC-P0089, Q5-SA-K1639
- **section 3, line 111:** - On the held route, the payout schedule is set per plan (Salla), per country (Zid) or per account, by the merchant (WooPayments). Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0036
- **section 5, line 129:** - Whether a provider account applied for through Sharrwah is one opened through Sharrwah under the guard, where that provider holds the merchant's money before paying it out. The design records how each account was opened. The founder settles it. Q5-SA-053, Q5-BC-P0048
- **section 5, line 137:** - On the held route only, the payout schedule's level (plan, place or account) and whether balances show as one or as several: the design keeps both as data. The holder's terms settle them. Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0036, Q5-SA-075
- **section 7, line 164:** - Whether Sharrwah collects cash on delivery through carriers it contracts, which would be a held route. Q5-SA-P0042, Q5-ZD-P0070
- **section 7, line 165:** - Whether Sharrwah offers financing repaid from sellers' sales, which needs a held route. Q5-SA-P0131, Q5-ZD-P0097
- **section 7, line 166:** - Sharrwah's own terms with merchants and providers, for the founder with a lawyer: whether a merchant's dealings with a provider are a contract of their own, whether Sharrwah acts for the merchant in any part of a payment, any security interest over sellers' money on a held route, and who answers for card data security. The platforms' terms show only what each requires of its sellers. Q5-SA-005, Q5-BC-K0453, Q5-BC-099, Q5-SH-P0002, Q5-SH-P0024
- **section 8, line 173:** - Records: Shopify's financial services provider, Stripe's pooled accounts and BigCommerce Payments' account hold it; Salla's (UAE help) and Zid's balances hold sales proceeds before payout, but who holds either balance was not in what was read; a connected gateway pays the merchant's own account. S01-VP-01, Q5-SH-P0033, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-P0057, Q5-ZD-P0035, Q5-SA-H0002, Q5-ZD-H0002, Q5-BC-P0089
- **section 8, line 179:** - Records: Shopify sends Shopify Payments' payouts, processed by partners, in the United States and France; WooPayments sends them to a bank account; Salla's dashboard text, as captured on 8 October 2026, lists transfers "من سلة إلى حسابك البنكي" (observed); Zid deposits on set days by country; BigCommerce Payments pays out to a linked bank or PayPal account. S01-VP-03, Q5-SH-P0076, Q5-WC-P0027, Q5-SA-P0040, Q5-ZD-P0041, Q5-BC-P0074
- **section 8, line 182:** - Records: the own services' processors (Shopify Payments; BigCommerce Payments, "powered by PayPal"); a connected gateway, at Salla "بدلًا من مدفوعات سلة" (dashboard text as captured on 8 October 2026, observed); the merchant, for Salla's bank transfer; and Zid, for cash on delivery through its shipping. S01-VP-04, Q5-SH-K1555, Q5-BC-P0055, Q5-SA-K1639, Q5-SA-P0099, Q5-ZD-P0070
- **section 8, line 185:** - Records: Shopify is the merchant's agent "to deliver information and instructions on your behalf"; Stripe, "for the limited purpose of directing, receiving, holding and settling funds"; Zid executes "payment processes on their behalf" (official pages); Salla passes label amounts on the merchant's behalf (dashboard text as captured on 8 October 2026, observed). BigCommerce's "No agency" statement is one of no part, naming no one; no reading rests on it. S01-VP-06, Q5-SH-P0002, Q5-WC-P0121, Q5-ZD-P0008, Q5-SA-P0126, Q5-BC-P0129
- **section 8, line 188:** - Records: Shopify deducts refunds from the next payout; Stripe pays out net of fees, disputes and refunds; Zid takes fees from amounts collected, and dues by "الخصم الآلي والمباشر"; Salla's dashboard text, as captured on 8 October 2026, takes postpaid label amounts from the wallet or coming dues (observed). S01-VP-09, Q5-SH-P0094, Q5-WC-P0124, Q5-ZD-P0024, Q5-ZD-P0061, Q5-SA-P0129
- **section 8, line 191:** - Records: Shopify's merchant opens accounts with Payment Processors; WooCommerce's Stripe extension uses the merchant's Stripe account; BigCommerce Payments creates a PayPal platform account per store; Zid's pay-later providers need an account with them; in Salla's store real-merchant, observed on 12 October 2026, the wallet listed "Electronic Payments" and "Cash on Delivery Payments". S01-VP-11, Q5-SH-P0010, Q5-WC-P0023, Q5-BC-P0069, Q5-ZD-P0080, Q5-SA-075
- **section 8, line 194:** - Records: by plan at Salla, by country at Zid, by account country for WooPayments' "pending period"; up to 21 days for a new BigCommerce Payments account's first payments; at most 5 days for Shopify's payment apps to settle. S01-VP-15, Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0033, Q5-BC-P0083, Q5-SH-064
- **section 8, line 197:** - Records: WooPayments credits payments "(minus our fees)"; Shopify's terms for the EU, EEA and UK settle "net of fees, refunds, chargebacks, reserves, and other amounts owed"; Salla transfers "بعد خصم الرسوم والضريبة" (dashboard text as captured on 8 October 2026, observed), while its store balance is for Salla's subscriptions and services (UAE help); Zid takes fees from amounts collected. S01-VP-19, Q5-WC-P0024, Q5-SH-P0107, Q5-SA-P0037, Q5-SA-P0057, Q5-ZD-P0024
- **section 8, line 200:** - Records: Shopify's funds in custody are paid out "subject to the Payment Processor Terms"; WooPayments' and Zid's balances are paid out, Zid's not before its financing is repaid; Salla may stop the service and close the store for a breach. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. S01-VP-20, Q5-SH-P0033, Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-SA-P0083, Q5-BC-H0040
- **section 8, line 203:** - Records: Shopify's terms for the EU, EEA and UK, if the merchant fails its checks, "funds may be held or refunded to your customers"; Zid's terms, after 14 days of uncorrected activation data, "إعادة جميع المبالغ للعملاء النهائيين"; Salla's terms, for a breach, "إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين". S01-VP-21, Q5-SH-P0107, Q5-ZD-P0012, Q5-SA-P0083
- **section 8, line 209:** - Records: with BigCommerce's PayPal Pay Later the shopper owes PayPal, while the merchant will "always get paid"; WooPayments receives "the entire purchase amount immediately"; Shop Pay Installments come with Shopify Payments payouts; Tabby pays Zid's stores directly and collects Salla's payments itself (UAE help). S01-VP-22, Q5-BC-P0095, Q5-WC-P0056, Q5-SH-K1686, Q5-ZD-P0077, Q5-SA-P0102

## The cards

### Q5-SA-P0006

**Cited at:** section 1, line 42; section 2, line 82

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-005
- bullet: a;end-payment;end-payout
- placement: boundary
- identifier: بمعنى آخر
- statement: دفع العميل إلكترونيًا ← رصيد المدفوعات الإلكترونية ← التحويل إلى حسابك البنكي
- cite_ids: S01-SA-C005
- from: new

**Citation S01-SA-C005:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1052 (article k6l988az2r60ucvfsfnpvlhn, دورة تحويل المدفوعات الإلكترونية), paragraph 11 | 2026-09-22 | kind: stated | quote check: found
- quote: دفع العميل إلكترونيًا ← رصيد المدفوعات الإلكترونية ← التحويل إلى حسابك البنكي
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …: يجب أن يصل إجمالي المبلغ المستحق للتحويل إلى 100 ريال سعودي على الأقل حتى يتم تحويله إلى حسابك البنكي. قبل أن تبدأ تأكد من: ✅ تفعيل المدفوعات الإلكترونية في متجرك. ✅ وجود حساب بنكي صالح لاستقبال المستحقات. ✅ تعرّف على دورة تحويل المدفوعات الإلكترونية عند دفع العميل قيمة الطلب باستخدام إحدى وسائل الدفع الإلكتروني، تُضاف قيمة العملية إلى رصيد المدفوعات الإلكترونية، ثم تُحوّل المستحقات المؤهلة إلى حسابك البنكي وفق دورة التحويل المحددة. بمعنى آخر: ⟪دفع العميل إلكترونيًا ← رصيد المدفوعات الإلكترونية ← التحويل إلى حسابك البنكي⟫ وإذا كان المبلغ المستحق أقل من 100 ريال، يبقى في رصيد المدفوعات الإلكترونية حتى يصل إجمالي المستحقات إلى الحد الأدنى للتحويل. 🧭 خطوات إعداد دورة تحويل المدفوعات الإلكترونية 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم مدفوعات سلة، اضغط (دورة التحويل). 3. حدد الخيار الذي يناسبك لدورة التحويل، واضغط (حفظ). ماذا يحدث بعد تغيير دورة التحويل؟ عند تغيير دورة التحويل، يتم اعتماد التغيير بعد 48 ساعة، …

### Q5-SA-P0020

**Cited at:** section 1, line 44; section 3, line 111; section 5, line 137; section 8, line 194

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-019
- bullet: c;end-payout
- placement: decides
- identifier: الأسئلة الشائعة
- statement: - باقة بلس: يتم الإيداع مرة واحدة أسبوعياً، حيث تصدر الفاتورة كل يوم أربعاء ثم تُحوَّل المبالغ إلى حسابك البنكي.
- scope: باقة بلس
- cite_ids: S01-SA-C019
- from: index:SA-C-111:SA-S-0071
- note: In the help centre section 'مقالات قديمة'.

**Citation S01-SA-C019:** `https://help.salla.sa/article/-إدارة-طرق-الدفع-وتفعيل-المدفوعات-الإلكترونية/dtdojcntv3f4lwqzj4h0jvij` | الأسئلة الشائعة (line 879 of the rendered text) | 2026-08-22 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/013-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:32Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/014-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:46Z, captured)
- quote: - باقة بلس: يتم الإيداع مرة واحدة أسبوعياً، حيث تصدر الفاتورة كل يوم أربعاء ثم تُحوَّل المبالغ إلى حسابك البنكي.
- title: تفعيل طرق الدفع الإلكتروني في متجرك | مركز المساعدة - سلة
- the page opens: تفعيل طرق الدفع الإلكتروني في متجرك مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل…
- in context: …سيلة الدفع الآجل تمارا تفعيل وسيلة الدفع الآجل | مدفوع تفعيل وسيلة الدفع الآجل Mispay خامساً: الحسابات البنكية يمكنك إضافة أكثر من حساب بنكي إلى متجرك، من خلال: من صفحة طرق الدفع، ومن قسم الحسابات البنكية اضغط على (+ حساب جديد). أدخل البيانات المطلوبة، ثم اضغط (حفظ). لمزيد من التفاصيل حول إعداد الحساب البنكي الأسئلة الشائعة متى يتم إيداع المبالغ في حسابي ؟ يختلف موعد إيداع المبالغ حسب نوع الباقة ودورة المدفوعات الخاصة بها، وذلك على النحو التالي: ⟪- باقة بلس: يتم الإيداع مرة واحدة أسبوعياً، حيث تصدر الفاتورة كل يوم أربعاء ثم تُحوَّل المبالغ إلى حسابك البنكي.⟫ - باقة برو: يتم الإيداع كل 48 ساعة، ثم تُحوَّل المبالغ إلى حسابك البنكي. - باقة سلة سبيشل: يتم الإيداع يومياً. ما هي الآلية الجديدة لتحويل المدفوعات للتجار؟ عُدلت آلية تحويل المدفوعات للتجار بحيث لن يتم تحويل المبالغ التي تقل عن 100 ريال إلى حساب التاجر مباشرةً. بدلاً من ذلك، ستبقى هذه المبالغ في حساب التاجر حتى يصل المجموع إلى الحد الأدنى المطلوب للتحويل. ما هو الحد الأدنى لمجموع المبالغ التي يمكن تحويلها للتاجر؟ الحد الأدنى لمجموع المبالغ التي…

### Q5-SA-P0022

**Cited at:** section 1, line 44

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-021
- bullet: c;end-payout
- placement: decides
- identifier: الأسئلة الشائعة
- statement: - باقة سلة سبيشل: يتم الإيداع يومياً.
- scope: باقة سلة سبيشل
- cite_ids: S01-SA-C021
- from: index:SA-C-111:SA-S-0073
- note: In the help centre section 'مقالات قديمة'.

**Citation S01-SA-C021:** `https://help.salla.sa/article/-إدارة-طرق-الدفع-وتفعيل-المدفوعات-الإلكترونية/dtdojcntv3f4lwqzj4h0jvij` | الأسئلة الشائعة (line 883 of the rendered text) | 2026-08-22 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/013-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:32Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/014-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:46Z, captured)
- quote: - باقة سلة سبيشل: يتم الإيداع يومياً.
- title: تفعيل طرق الدفع الإلكتروني في متجرك | مركز المساعدة - سلة
- the page opens: تفعيل طرق الدفع الإلكتروني في متجرك مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل…
- in context: …م الحسابات البنكية اضغط على (+ حساب جديد). أدخل البيانات المطلوبة، ثم اضغط (حفظ). لمزيد من التفاصيل حول إعداد الحساب البنكي الأسئلة الشائعة متى يتم إيداع المبالغ في حسابي ؟ يختلف موعد إيداع المبالغ حسب نوع الباقة ودورة المدفوعات الخاصة بها، وذلك على النحو التالي: - باقة بلس: يتم الإيداع مرة واحدة أسبوعياً، حيث تصدر الفاتورة كل يوم أربعاء ثم تُحوَّل المبالغ إلى حسابك البنكي. - باقة برو: يتم الإيداع كل 48 ساعة، ثم تُحوَّل المبالغ إلى حسابك البنكي. ⟪- باقة سلة سبيشل: يتم الإيداع يومياً.⟫ ما هي الآلية الجديدة لتحويل المدفوعات للتجار؟ عُدلت آلية تحويل المدفوعات للتجار بحيث لن يتم تحويل المبالغ التي تقل عن 100 ريال إلى حساب التاجر مباشرةً. بدلاً من ذلك، ستبقى هذه المبالغ في حساب التاجر حتى يصل المجموع إلى الحد الأدنى المطلوب للتحويل. ما هو الحد الأدنى لمجموع المبالغ التي يمكن تحويلها للتاجر؟ الحد الأدنى لمجموع المبالغ التي يمكن تحويلها للتاجر هو 100 ريال. ماذا يحدث إذا كان مجموع المبالغ أقل من 100 ريال؟ إذا كان مجموع المبالغ أقل من…

### Q5-SA-P0126

**Cited at:** section 1, line 45; section 2, line 88; section 2, line 89; section 8, line 185

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-125
- bullet: a;c
- placement: responsible
- identifier: apps.managed_settlement.description
- statement: بتثبيتك لهذا التطبيق، فإنك تُفوّض سلة بحجز مبالغ بوليصات الشحن من رصيدك في المحفظة، وتحويلها نيابةً عنك إلى شركة الشحن — دون الحاجة إلى الدفع لشركة الشحن بشكل مباشر.
- scope: تطبيق {{carrier}}
- cite_ids: S01-SA-C140
- from: new
- note: Heading apps.managed_settlement.heading 'صلاحية مطلوبة لتثبيت تطبيق {{carrier}}'.

**Citation S01-SA-C140:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/apps.json` | apps.managed_settlement.description | 2026-10-08 | kind: observed | quote check: found
- quote: بتثبيتك لهذا التطبيق، فإنك تُفوّض سلة بحجز مبالغ بوليصات الشحن من رصيدك في المحفظة، وتحويلها نيابةً عنك إلى شركة الشحن — دون الحاجة إلى الدفع لشركة الشحن بشكل مباشر.
- in context: …ات تقييم تقييمات الدخول للوحة تحكم التطبيق تم حفظ الإعدادات بنجاح. تسعيرة الشحن مواصفات الشحن نبذة عن التطبيق مطابق للمعايير تجربة تشبه سلة فريدة من نوعها. تاريخ بداية الاشتراك تفاصيل الاشتراك تاريخ انتهاء الاشتراك الدعم الفني تطبيقات لم يتم تقييمها ترقية الباقة تعرف على كيفية البدء مع التطبيق الموقع التكامل تفويض وتثبيت التطبيق تعذّر تسجيل الموافقة، حاول مرة أخرى. أوافق على تفويض سلة بحجز مبالغ بوليصات الشحن من رصيد محفظتي وتحويلها لشركة الشحن. ⟪بتثبيتك لهذا التطبيق، فإنك تُفوّض سلة بحجز مبالغ بوليصات الشحن من رصيدك في المحفظة، وتحويلها نيابةً عنك إلى شركة الشحن - دون الحاجة إلى الدفع لشركة الشحن بشكل مباشر.⟫ صلاحية مطلوبة لتثبيت تطبيق {{carrier}} عند إنشاء بوليصة شحن، تُحجز قيمتها تلقائياً من رصيد المدفوعات الإلكترونية. يظهر المبلغ المحجوز في سجل محفظتك مع رقم الطلب. تتولى سلة تسوية المبالغ مع شركة الشحن بعد خصم عمولة سلة. كيف تعمل الآلية؟ إدارة مبالغ تكلفة الشحن يجب أن يتوفر رصيد كافٍ في محفظتك لإتمام عمليات الشحن. عند عدم كفاية الرصيد لن يتم إنشاء البوليصة. التفعيل لاحقاً تم اكمال إجراءات استخدام التطبيق بنجاح رجوع تثبيت التطبيق الإنتقال إلى {{ste…

### Q5-SA-P0131

**Cited at:** section 1, line 45; section 3, line 102; section 7, line 165

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-130
- bullet: c;end-payout
- placement: decides
- identifier: capital.active.payment_details.footnote
- statement: يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة، ويُحوّل المتبقي إلى حسابك البنكي. يُدار الاستثمار من خلال صندوق سلة بالشراكة مع تنامي.
- scope: صندوق سلة
- cite_ids: S01-SA-C145
- from: index:SA-C-128:SA-S-0111

**Citation S01-SA-C145:** `observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json` | capital.active.payment_details.footnote | 2026-10-08 | kind: observed | quote check: found
- quote: يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة، ويُحوّل المتبقي إلى حسابك البنكي. يُدار الاستثمار من خلال صندوق سلة بالشراكة مع تنامي.
- in context: …details":{"cols":{"date":"التاريخ","net_sales":"صافي المبيعات","payment_no":"رقم الدفعة","repayment_amount":"مبلغ التحصيل","repayment_rate":"نسبة التحصيل","salla_fees":"الرسوم","tax":"ضريبة الرسوم","total_sales":"إجمالي المبيعات","transferred":"المبلغ المحوّل"},"empty_desc":"ستظهر تفاصيل الدفعات هنا عند بدء التحصيل من مبيعاتك.","empty_label":"لا توجد دفعات بعد","export":"تصدير","footnote":"صافي المبيعات = إجمالي المبيعات - الرسوم - ضريبة الرسوم. ⟪يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة، ويُحوّل المتبقي إلى حسابك البنكي. يُدار الاستثمار من خلال صندوق سلة بالشراكة مع تنامي.⟫","period_label":"التاريخ","subtitle":"اعرف كيف يُحسب كل تحصيل من مبيعاتك.","title":"تفاصيل التحصيل","total":"الإجمالي"},"statement":{"cols":{"balance":"الرصيد","credit":"دائن","date":"التاريخ","debit":"مدين","description":"البيان","payment_no":"رقم الدفعة"},"empty_desc":"ستظهر عمليات كشف الحساب هنا عند توفّرها.","empty_label":"لا توجد عمليات بعد","export":"تصدير","net_note":"يُحسب مبلغ التحصيل من صافي مبيعات مدى والبطاقات الائتمانية بعد خصم رسوم…

### Q5-SA-K1690

**Cited at:** section 1, line 45; section 3, line 102

**Record** (`studies/proposals/records/Q5/salla/copied.tsv`):
- concern_id: SA-C-124
- placement: boundary
- structure: https://docs.salla.dev/1973350f0.md
- identifier: # Settlements
- statement: This endpoint allows you to temporarily withhold a specific amount of money for settlement from the Merchant's wallet.
- cite_ids: SA-S-0178

**Citation SA-S-0178:** `https://docs.salla.dev/1973350f0.md` | # Settlements (line 6 of the markdown) | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/002-docs.salla.dev/text.txt` (fetched 2026-10-10T23:51:30Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/009-docs.salla.dev/text.txt` (fetched 2026-10-12T10:49:43Z, captured)
- quote: This endpoint allows you to temporarily withhold a specific amount of money for settlement from the Merchant's wallet.
- title: Settlements
- the page opens: Docs - List Instant Settlements: This endpoint lists all the instant settlements including details such as amount and status that are associated with the store. - Create Instant Settlement: This endpoint allows you to temporarily withhold a specific amount of money for settlement from the Merchant's wallet. - Update Instant Settlement: This endpoint allows you to update the status and the amount of a specific settlment by by passing the id as a path parameter. - Instant Settlement Details: This …
- headings: Settlements > Docs
- in context: # Settlements ## Docs - [List Instant Settlements](https://docs.salla.dev/settlements/list.md): This endpoint lists all the instant settlements including details such as amount and status that are associated with the store. - [Create Instant Settlement](https://docs.salla.dev/settlements/create.md): ⟪This endpoint allows you to temporarily withhold a specific amount of money for settlement from the Merchant's wallet.⟫ - [Update Instant Settlement](https://docs.salla.dev/settlements/update.md): This endpoint allows you to update the status and the amount of a specific settlment by by passing the `id` as a path parameter. - [Instant Settlement Details](https://docs.salla.dev/settlements/details.md): This endpoint allows you to fetch the details for a specific settlement by passing the `id` as a path parameter. - [Delete Instant Settlement](https://docs.salla.de…

### Q5-SA-075

**Cited at:** section 1, line 46; section 2, line 90; section 5, line 137; section 8, line 191

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-075
- bears_on: 5
- identifier: GET /admin/v2/store-wallet/wallet/summary: data.wallets
- statement: "wallets": [{"type": "default", "name": "Wallet", "balance": 69.96, "currency": "SAR", "can_withdraw": true, "metadata": {"wallet_id": "140877344", "disable_balance_draw": false, "is_withdraw_over_limit": 0, "wallet_withdrawal_enabled": false, "withdraw_disabled_reason": null, "withdraw_disabled_message": null, "store_bank_account_exist": true, "is_store_documented": true, "daily_limit": "5008.05", "total_deposits": 27687.47, "total_withdrawals": 27617.51}}, {"type": "salla_pay", "name": "Electronic Payments", "balance": 1690.37, "currency": "SAR", "can_withdraw": true, "metadata": {"enable_transfer_balance": true, "is_balance_frozen": false, "day_amount_balance": 0, "max_total_to_generate": 100, "total_excluding_fees_and_tax": 1690.37, "total_fees": 23.15, "total_tax": 3.48, "total_including_fees_and_tax": 1717}}, {"type": "salla_cod", "name": "Cash on Delivery Payments", "balance": 0, "currency": "SAR", "can_withdraw": true, "metadata": {"max_total_to_generate": 100, "total_excluding_fees_and_tax": 0, "total_fees": 0, "total_tax": 0, "total_including_fees_and_tax": 0}}]
- scope: store real-merchant, observed 2026-10-12
- cite_ids: Q5-SA-C112
- from: held
- note: the list's three items, in full

**Citation Q5-SA-C112:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/0614.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, step 17 | 2026-10-12 | kind: observed | quote check: found
- quote: "wallets": [{"type": "default", "name": "Wallet", "balance": 69.96, "currency": "SAR", "can_withdraw": true, "metadata": {"wallet_id": "140877344", "disable_balance_draw": false, "is_withdraw_over_limit": 0, "wallet_withdrawal_enabled": false, "withdraw_disabled_reason": null,
- in context: …d", "status": null, "status_label": null, "due_date": null, "due_date_format": null, "due_amount": 0, "send_date": null, "send_date_humans": null, "amount": 0, "currency": "SAR", "is_over_limit": false, "hint": null}}, "payout_schedule_message": null, "payout_schedule_messages": {"epayment": "Your funds are transferred every 48 hours when the balance exceeds 100 SAR.", "cod": "Your cash-on-delivery payouts are sent every Sunday and Wednesday."}, ⟪"wallets": [{"type": "default", "name": "Wallet", "balance": 69.96, "currency": "SAR", "can_withdraw": true, "metadata": {"wallet_id": "140877344", "disable_balance_draw": false, "is_withdraw_over_limit": 0, "wallet_withdrawal_enabled": false, "withdraw_disabled_reason": null,⟫ "withdraw_disabled_message": null, "store_bank_account_exist": true, "is_store_documented": true, "daily_limit": "5008.05", "total_deposits": 27687.47, "total_withdrawals": 27617.51}}, {"type": "salla_pay", "name": "Electronic Payments", "balance": 1690.37, "currency": "SAR", "can_withdraw": true, "metadata": {"enable_transfer_balance": true, "is_balance_frozen": false, "day_amount_balance": 0, "max_total_to_generate": 100, "total_excluding_fees…

### Q5-SA-K1639

**Cited at:** section 1, line 47; section 2, line 82; section 3, line 110; section 8, line 182

**Record** (`studies/proposals/records/Q5/salla/copied.tsv`):
- concern_id: SA-C-120
- placement: where
- structure: observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json
- identifier: gateway_settings.tutorial_alert_text
- statement: ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد،
- cite_ids: SA-S-0099

**Citation SA-S-0099:** `observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json` | gateway_settings.tutorial_alert_text | 2026-10-08 | kind: observed | quote check: found
- quote: ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد،
- in context: … مراجعته","status_failed_retry":"إعادة المحاولة","status_failed_title":"تعذَّر إرسال الطلب","status_rejected_desc":"فضلًا تواصل مع خدمة عملاء {{name}} لمعرفة أسباب الرفض.","status_rejected_retry":"إعادة المحاولة","status_rejected_title":"عذرًا، تم رفض طلبك لفتح حساب للأعمال في {{name}}","toggle_error":"تعذَّر تحديث حالة بوابة الدفع.","toggle_success":"تم تحديث حالة {{name}} بنجاح.","tutorial_alert_link":"تواصل مع {{name}}","tutorial_alert_text":"⟪ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد،⟫","verification_description":"وثِّق متجرك لتفعيل طرق الدفع وإدارة مدفوعاتك بأمان.","verification_required":"متجرك غير موثَّق","verify_now":"وثِّقه الآن"},"gcc_banner":{"description":"نعمل حاليًا على مراجعة بيانات متجرك لتفعيل المدفوعات الإلكترونية. سنُشعرك فور اكتمال المراجعة أو عند الحاجة إلى أي معلومات إضافية.","tap_active":{"description":"لن تتمكن من تفعيل مدفوعات سلة حاليًا لوجود ربط فعَّال مع تاب.","title":"متجرك مرتبط ببوابة دفع أخرى"},"tit…

### Q5-SA-P0102

**Cited at:** section 1, line 49; section 8, line 209

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-101
- bullet: a;b;c;d
- placement: responsible
- identifier: الدفع والتسوية
- statement: الدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي.
- scope: الإمارات (article: تفعيل تابي على متجرك في سلة الإمارات)
- cite_ids: S01-SA-C112
- from: new

**Citation S01-SA-C112:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة), paragraph 5 | 2026-09-16 | kind: stated | quote check: found
- quote: الدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ا أو تقسيم قيمة مشترياتهم على دفعات، بينما يستلم متجرك مستحقاته وفق الاتفاقية المبرمة مع تابي. في هذا الدليل، ستتعرّف على متطلبات التفعيل، وطريقة ربط حساب تابي بمتجرك على سلة، وكيف تعمل طريقة الدفع بعد تفعيلها. ما هي تابي؟ تابي هي طريقة دفع بنظام «اشترِ الآن وادفع لاحقًا» تتيح للعملاء المؤهلين إتمام عملية الشراء دون دفع كامل قيمة الطلب مقدمًا. ويمكن أن تساعد خيارات الدفع المرنة على زيادة القوة الشرائية، وتحسين إتمام الطلب، ورفع متوسط قيمة السلة. ⟪الدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي.⟫ ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي عل…

### Q5-SA-P0099

**Cited at:** section 1, line 50; section 2, line 83; section 8, line 182

**The same record as Q4-SA-P0099,** whose card is in `Q4-salla-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك.
- scope: باقة بيسك

### Q5-SA-P0092

**Cited at:** section 1, line 51; section 2, line 84

**The same record as Q4-SA-P0092,** whose card is in `Q4-salla-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين.
- scope: شركة شحن خارج نطاق بوليصات سلة

### Q5-SA-P0042

**Cited at:** section 1, line 51; section 2, line 84; section 7, line 164

**The same record as Q4-SA-P0042,** whose card is in `Q4-salla-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: تحوِّل شركة الشحن المبلغ إلى سلة
- scope: 

### Q5-SA-053

**Cited at:** section 2, line 65; section 2, line 66; section 2, line 67; section 5, line 129

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-053
- bears_on: 3
- identifier: gateway_settings.radio_existing
- statement: لدي حساب {{name}} للأعمال
- cite_ids: Q5-SA-C086
- from: held

**Citation Q5-SA-C086:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | gateway_settings.radio_existing | 2026-10-08 | kind: observed | quote check: found
- quote: لدي حساب {{name}} للأعمال
- in context: …madfu":"مدفوع","gateway_name_mispay":"إم آي إس باي","gateway_name_mokafaa-alrajhi":"مكافأة الراجحي","gateway_name_moyasar":"ميسر","gateway_name_paypal":"باي بال","gateway_name_paytabs":"بيتابس","gateway_name_spoti":"سبوتي","gateway_name_stc-pay":"stc pay","gateway_name_tabby":"تابي","gateway_name_tamara":"تمارا","gateway_name_tap":"تاب","help_link":"مركز المساعدة","help_text":"تحتاج مساعدة في ربط {{name}} بمتجرك؟ تفضَّل بزيارة","radio_existing":"⟪لدي حساب {{name}} للأعمال⟫","radio_request":"إرسال طلب فتح حساب أعمال","save":"حفظ","save_success":"حُفظت بيانات ربط {{name}} بنجاح.","settings_section":"الإعدادات","status_applied_desc":"ستصلك رسالة من فريق {{name}} عبر البريد الإلكتروني لتزويدك ببيانات الربط، بعد استلامها، عد لإكمال إعدادات الربط هنا.","status_applied_title":"أُرسل طلبك إلى {{name}} وجارٍ مراجعته","status_failed_retry":"إعادة المحاولة","status_failed_title":"تعذَّر إرسال الطلب","status_rejected_desc":"ف…

### Q5-SA-016

**Cited at:** section 2, line 73; section 3, line 107

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-016
- bears_on: 1;2
- identifier: - خيار تحديد السوق
- statement: في حال تم تفعيل ميزة الأسواق المتعددة ، ستظهر أيقونة اختيار السوق في صفحة طرق الدفع، حيث تتيح لك اختيار السوق الذي ترغب في إدارة إعداداته، والتنقل بسهولة بين الأسواق المختلفة المرتبطة بمتجرك.
- cite_ids: Q5-SA-C029
- from: held

**Citation Q5-SA-C029:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 45 | 2026-08-31 | kind: stated | quote check: found
- quote: في حال تم تفعيل ميزة الأسواق المتعددة ، ستظهر أيقونة اختيار السوق في صفحة طرق الدفع، حيث تتيح لك اختيار السوق الذي ترغب في إدارة إعداداته، والتنقل بسهولة بين الأسواق المختلفة المرتبطة بمتجرك.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ات الموحد. لمزيد من التفاصيل حول تفاصيل صفحة الدفع للعميل - حاسبة الرسوم يمكنك حساب الرسوم المترتبة على الطلبات من خلال إدخال قيمة الطلب في الحقل المخصص وتحديد طريقة الدفع، فتظهر قيمة الرسوم المترتبة على الطلب بالشكل: - حدود الدفع الإلكتروني تتيح لك الاطلاع على الحدود المسموحة لعمليات الدفع الإلكتروني حسب الدولة ونوع المنتج لضمان عمليات دفع آمنة ومتوافقة مع السياسات المعتمدة. لمزيد من التفاصيل حول حدود معاملات الدفع الإلكتروني - خيار تحديد السوق ⟪في حال تم تفعيل ميزة الأسواق المتعددة ، ستظهر أيقونة اختيار السوق في صفحة طرق الدفع، حيث تتيح لك اختيار السوق الذي ترغب في إدارة إعداداته، والتنقل بسهولة بين الأسواق المختلفة المرتبطة بمتجرك.⟫ لمزيد من التفاصيل حول تفعيل وإدارة الأسواق المتعددة. الأسئلة الشائعة ❓ ما هي طرق الدفع المتاحة في باقة بيسك؟ في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك. كما يمكنك تفعيل الدفع عند الاستلام ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص. أما طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط. ❓من يمكنه استخدام ميزة عرض رسالة التبرع؟ التجار الذين يستخدمون مدفوعات …

### Q5-SA-P0055

**Cited at:** section 2, line 87; section 2, line 88

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-054
- bullet: c;end-payout
- placement: boundary
- identifier: الحساب البنكي المستخدم لاستلام التحويلات
- statement: تُرسل التحويلات إلى الحساب البنكي الذي قدّمته أثناء توثيق المتجر. تأكد من تطابق بيانات الحساب مع مستنداتك البنكية.
- scope: الإمارات
- cite_ids: S01-SA-C054
- from: index:SA-C-112:SA-S-0085

**Citation S01-SA-C054:** `https://help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76` | الحساب البنكي المستخدم لاستلام التحويلات (line 725 of the rendered text) | 2026-09-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/021-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:40Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/018-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:52Z, captured)
- quote: تُرسل التحويلات إلى الحساب البنكي الذي قدّمته أثناء توثيق المتجر. تأكد من تطابق بيانات الحساب مع مستنداتك البنكية.
- title: تحويلات مدفوعات سلة والتسويات في الإمارات | سلة | مركز المساعدة - سلة
- the page opens: Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حلول تقنية متقدمة لنمو أعمال كبار التجار المدفوعات طرق …
- in context: …راتي الحساب البنكي المستلم الحساب البنكي المستخدم أثناء توثيق المتجر الرسوم وفق عقد خدمات الدفع الموقّع أثناء التوثيق تتبع المدفوعات الإلكترونية في المحفظة قريبًا لمتاجر الإمارات كيف تعمل التحويلات؟ مسار الدفع: يدفع العميل إلكترونيًا ← تُضاف الدفعة إلى رصيد المدفوعات الإلكترونية ← تُحوّل المستحقات المؤهلة إلى حسابك البنكي. -تتم تسوية المدفوعات وتحويلها وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق متجرك. الحساب البنكي المستخدم لاستلام التحويلات ⟪تُرسل التحويلات إلى الحساب البنكي الذي قدّمته أثناء توثيق المتجر. تأكد من تطابق بيانات الحساب مع مستنداتك البنكية.⟫ -لتغيير الحساب البنكي المستخدم لاستلام التحويلات، أرسل طلب توثيق جديدًا يتضمن البيانات البنكية المحدثة، ثم تواصل مع دعم سلة للمساعدة. دورية التحويل والحد الأدنى - دورية التحويل: أسبوعيًا، كل يوم خميس. - الحد الأدنى للتحويل: 250 درهمًا إماراتيًا. إذا كان رصيد المدفوعات الإلكترونية المؤهل أقل من 250 درهمًا، يبقى المبلغ في الرصيد حتى يتجاوز الحد الأدنى، ثم يُضمّن في دورة التحويل التالية. الرسوم تُحتسب رسوم المدفوعات الإلكترونية وفق عقد خدمات الدفع …

### Q5-SA-005

**Cited at:** section 7, line 166

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-005
- bears_on: 2;3;4
- identifier: المادة الثالثة – طبيعة التزام منصة سلة
- statement: إن جميع التعاملات التي تتم بين التاجر ومزودي الخدمات ( خدمات الطرف الثالث ) الذين توفر منصة سلّة الربط مع خدماتهم أو عرض خدماتهم ليستفيد منها التاجر والمستهلك لا علاقة لها بمنصة سلّة ، حيث أن هذا التعامل هو علاقة تعاقدية مستقلة عن منصة سلّة وخاضعة للاتفاق المبرم بين التاجر ومزود الخدمة ، وبناءً عليه فإذا تخلّف أو امتنع أو لم يلتزم أحد الاطراف في تنفيذ التزاماته التي جرى الاتفاق عليها أو لم ينفذها على الوجه المطلوب فإن منصة سلّة غير مسئولة عن ما ينتج عن هذه التصرفات، إن منصة سلّة غير مسئولة عن أي مخالفات تحدث أو يتم ارتكابها بين التاجر ومزود الخدمة.
- cite_ids: Q5-SA-C005;Q5-SA-C006
- from: held

**Citation Q5-SA-C005:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 37 (المادة الثالثة – طبيعة التزام منصة سلة) | 2026-10-06 | kind: official page | quote check: found
- quote: إن جميع التعاملات التي تتم بين التاجر ومزودي الخدمات ( خدمات الطرف الثالث ) الذين توفر منصة سلّة الربط مع خدماتهم أو عرض خدماتهم ليستفيد منها التاجر والمستهلك لا علاقة لها بمنصة سلّة ، حيث أن هذا التعامل هو علاقة تعاقدية مستقلة عن منصة سلّة وخاضعة للاتفاق المبرم بين التاجر ومزود الخدمة ،
- in context: …محددة ومعيّنة فإن رغب التاجر بخدمات إضافية عليه أن يتواصل مع الدعم الفني الخاص بمنصة سلّة للاستفسار عن العروض ورسوم الباقات والخدمات الإضافية. إن جميع التعاملات التي تتم بين التاجر والمستهلك لا علاقة لها بشخص منصة سلة، ومنصة سلة غير مسئولة عنها، حيث أن هذا التعامل هو علاقة تعاقدية مستقلة تخضع للاتفاق الذي يبرم بين التاجر والمستهلك. وبناءً عليه فإذا تخلّف المستهلك عن سداد ثمن الخدمة أو المنتج الذي يوفّره التاجر فلا علاقة لمنصة سلة بهذه المخالفات. ⟪إن جميع التعاملات التي تتم بين التاجر ومزودي الخدمات ( خدمات الطرف الثالث ) الذين توفر منصة سلّة الربط مع خدماتهم أو عرض خدماتهم ليستفيد منها التاجر والمستهلك لا علاقة لها بمنصة سلّة ، حيث أن هذا التعامل هو علاقة تعاقدية مستقلة عن منصة سلّة وخاضعة للاتفاق المبرم بين التاجر ومزود الخدمة ،⟫ وبناءً عليه فإذا تخلّف أو امتنع أو لم يلتزم أحد الاطراف في تنفيذ التزاماته التي جرى الاتفاق عليها أو لم ينفذها على الوجه المطلوب فإن منصة سلّة غير مسئولة عن ما ينتج عن هذه التصرفات، إن منصة سلّة غير مسئولة عن أي مخالفات تحدث أو يتم ارتكابها بين التاجر ومزود الخدمة. أنت تعلم أن منصة سلّة تعتبر منصة إلكترونية تقنية على شبكة الانترنت تتيح للتاجر الذي يوافق على هذه الاتفاقية تأسيس متجره الالكتروني ، وممارسة نشاطه عبر المتجر ، ومهمتها تنتهي عند هذا ا…

**Citation Q5-SA-C006:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 37 (المادة الثالثة – طبيعة التزام منصة سلة) | 2026-10-06 | kind: official page | quote check: found
- quote: وبناءً عليه فإذا تخلّف أو امتنع أو لم يلتزم أحد الاطراف في تنفيذ التزاماته التي جرى الاتفاق عليها أو لم ينفذها على الوجه المطلوب فإن منصة سلّة غير مسئولة عن ما ينتج عن هذه التصرفات، إن منصة سلّة غير مسئولة عن أي مخالفات تحدث أو يتم ارتكابها بين التاجر ومزود الخدمة.
- title, opening and note boxes: as for this source's citation above
- in context: …تخضع للاتفاق الذي يبرم بين التاجر والمستهلك. وبناءً عليه فإذا تخلّف المستهلك عن سداد ثمن الخدمة أو المنتج الذي يوفّره التاجر فلا علاقة لمنصة سلة بهذه المخالفات. إن جميع التعاملات التي تتم بين التاجر ومزودي الخدمات ( خدمات الطرف الثالث ) الذين توفر منصة سلّة الربط مع خدماتهم أو عرض خدماتهم ليستفيد منها التاجر والمستهلك لا علاقة لها بمنصة سلّة ، حيث أن هذا التعامل هو علاقة تعاقدية مستقلة عن منصة سلّة وخاضعة للاتفاق المبرم بين التاجر ومزود الخدمة ، ⟪وبناءً عليه فإذا تخلّف أو امتنع أو لم يلتزم أحد الاطراف في تنفيذ التزاماته التي جرى الاتفاق عليها أو لم ينفذها على الوجه المطلوب فإن منصة سلّة غير مسئولة عن ما ينتج عن هذه التصرفات، إن منصة سلّة غير مسئولة عن أي مخالفات تحدث أو يتم ارتكابها بين التاجر ومزود الخدمة.⟫ أنت تعلم أن منصة سلّة تعتبر منصة إلكترونية تقنية على شبكة الانترنت تتيح للتاجر الذي يوافق على هذه الاتفاقية تأسيس متجره الالكتروني ، وممارسة نشاطه عبر المتجر ، ومهمتها تنتهي عند هذا الحد. فليس هناك أدنى مسئولية على منصة سلة حول المخالفات التي يقوم بها التاجر في متجره بالمخالفة لأحكام هذه الاتفاقية، وليس لمنصة سلة أي علاقة بالنسبة للتعاملات التي تتم بين التاجر والمستهلك. المادة الرابعة - ضوابط إنشاء المتجر الالكتروني: يجوز لكل شخص توافرت فيه الأه…

### Q5-SA-P0057

**Cited at:** section 8, line 173; section 8, line 197

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-056
- bullet: a
- placement: where
- identifier: الأسئلة الشائعة
- statement: لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها.
- scope: الإمارات
- cite_ids: S01-SA-C056
- from: index:SA-C-111:SA-S-0083

**Citation S01-SA-C056:** `https://help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76` | الأسئلة الشائعة (line 843 of the rendered text) | 2026-09-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/021-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:40Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/018-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:52Z, captured)
- quote: لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها.
- title: تحويلات مدفوعات سلة والتسويات في الإمارات | سلة | مركز المساعدة - سلة
- the page opens: Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حلول تقنية متقدمة لنمو أعمال كبار التجار المدفوعات طرق …
- in context: …لمدفوعات الإلكترونية المؤهل 250 درهمًا إماراتيًا. ماذا يحدث إذا كان رصيدي أقل من 250 درهمًا؟ يبقى المبلغ في رصيد المدفوعات الإلكترونية حتى يتجاوز الحد الأدنى، ثم يُضمّن في دورة التحويل التالية. إلى أي حساب بنكي تصل التحويلات؟ إلى الحساب البنكي المستخدم أثناء توثيق المتجر. هل يمكنني تغيير الحساب البنكي المستخدم للتحويلات؟ نعم. أرسل بيانات بنكية محدثة من خلال التوثيق، ثم تواصل مع دعم سلة للمساعدة. هل رصيد المتجر هو نفسه رصيد المدفوعات الإلكترونية؟ ⟪لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها.⟫ كيف تُحتسب رسوم المدفوعات الإلكترونية؟ وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق المتجر. اسأل, واطلب الدعم من التجار وفريق سلة. السابق التالي تصنيفات ذات صلة أساسيات في طرق الدفع وسائل الدفع الآجل المحافظ الرقمية وسائل الدفع الأخرى أقسام ذات صلة 🏡 الصفحة الرئيسية 📦 الطلبات 🏷️ المنتجات 📢 التسويق 🎨 تصميم المتجر 🚛 إدارة الشحن والتوصيل 📱 تطبيق التاجر وتطبيق الجوال 🏪 كاشير سلة بوينت 🧩 التطبيقات المثبتة ومتجر التطبيقات

### Q5-SA-P0040

**Cited at:** section 8, line 179

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-039
- bullet: a;end-payout
- placement: where
- identifier: wallet.transfer_cycle_invoices.page_description
- statement: استعرض تفاصيل عمليات تحويل المدفوعات من سلة إلى حسابك البنكي.
- cite_ids: S01-SA-C039
- from: new
- note: The page title is wallet.transfer_cycle_invoices.title 'تحصيل المدفوعات'.

**Citation S01-SA-C039:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | wallet.transfer_cycle_invoices.page_description | 2026-10-08 | kind: observed | quote check: found
- quote: استعرض تفاصيل عمليات تحويل المدفوعات من سلة إلى حسابك البنكي.
- in context: …فع شركة الشحن الضريبة الإجمالي لا توجد طلبات ضمن هذه العملية. الطلبات الإجمالي دفعة الاستثمار (نسبة السداد 25%) الصافي المحوَّل للحساب البنكي تفاصيل العملية #{{id}} الكل إجراءات المبلغ البنك الرسوم التاريخ المبلغ المستحق رقم الآيبان تفاصيل الفاتورة الرقم المرجعي (UTI) المصدر الحالة الضريبة رقم الفاتورة الضريبية الإجمالي رقم العملية تأكيد الاستلام تم تأكيد استلام المبلغ. ستتمكَّن من استعراض فواتير دورة التحويل عند توفرها. لا توجد فواتير بعد تصدير ⟪استعرض تفاصيل عمليات تحويل المدفوعات من سلة إلى حسابك البنكي.⟫ ابحث برقم العملية تحصيل المدفوعات عرض التفاصيل عرض العمليات المبلغ أدخل المبلغ الذي تود استرداده الرصيد المتوفر الحساب البنكي تأكيد لا يمكن استرداد أكثر من الحد اليومي المسموح به ({{limit}}). الحد الأقصى للاسترداد اليومي تعذَّر تنفيذ طلب الاسترداد. حاول لاحقًا. تُنفَّذ طلبات الاسترداد أسبوعيًا كل يوم ثلاثاء، وتُؤجَّل الطلبات المقدَّمة يوم الاثنين إلى الأسبوع التالي. المبلغ يتجاوز الرصيد المتاح. الحد الأقصى لمبلغ الاسترداد هو الحد الأدنى لمبلغ ال…

### Q5-SA-P0129

**Cited at:** section 8, line 188

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-128
- bullet: c
- placement: decides
- identifier: actions_bar.create_shipping_policy.summary.postpaid.terms_collection_method_text
- statement: تُخصم المبالغ المستحقة تلقائيًا من محفظة المتجر أو من مستحقاتك القادمة عبر سلة.
- scope: الدفع الآجل لبوليصات سلة
- cite_ids: S01-SA-C143
- from: new
- note: Under 'الشروط والأحكام للدفع الآجل لبوليصات سلة', label 'آلية التحصيل'.

**Citation S01-SA-C143:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/orders.json` | actions_bar.create_shipping_policy.summary.postpaid.terms_collection_method_text | 2026-10-08 | kind: observed | quote check: found
- quote: تُخصم المبالغ المستحقة تلقائيًا من محفظة المتجر أو من مستحقاتك القادمة عبر سلة.
- in context: …ع أو المستودع شركة التوصيل تعديل أوزان المنتجات خيارات البوليصة اختر نوع البوليصة عدم عرض تفاصيل المنتجات في بوليصة الشحن سأقوم بتسليم الطلب إلى أقرب فرع لشركة الشحن تكلفة الشحن المستردة بعد توصيل الطلب (متبقي {{remaining}}/{{total}}) لديك فاتورة مستحقة. سدِّدها خلال 5 أيام للاستمرار في استخدام الدفع الآجل لبوليصات سلة. سداد الفاتورة الدفع الآجل الإلغاء تخضع البوليصات المُصدرة لسياسات الإلغاء والاسترجاع الخاصة بشركات الشحن المعتمدة. آلية التحصيل ⟪تُخصم المبالغ المستحقة تلقائيًا من محفظة المتجر أو من مستحقاتك القادمة عبر سلة.⟫ الحد الائتماني تمنحك سلة حدًا ائتمانيًا لإصدار البوليصات. عند تجاوز الحد، يلزم سداد المبلغ المستحق للاستمرار في إصدار البوليصات. الشروط والأحكام للدفع الآجل لبوليصات سلة التعديل يحق لسلة تحديث شروط الخدمة أو الحد الائتماني في أي وقت وفقًا لما تراه مناسبًا. مواعيد السداد يلتزم التاجر بسداد المبالغ المستحقة في موعدها لتجنُّب إيقاف خدمة الدفع الآجل أو بعض مزايا المتجر. يمكنك إصدار البوليصات الآن وسداد رسومها لاحقًا. اطّلع على شروط وأحكام الدفع الآج…

### Q5-SA-P0037

**Cited at:** section 8, line 197

**Record** (`studies/proposals/records/Q5/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-036
- bullet: c;end-payout
- placement: decides
- identifier: wallet.epayment.summary.tooltips.net
- statement: المبلغ الذي سيُحوَّل إلى حسابك البنكي بعد خصم الرسوم والضريبة.
- cite_ids: S01-SA-C036
- from: new
- note: The COD tab's tooltip wallet.cod.summary.tooltips.net has the same text.

**Citation S01-SA-C036:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | wallet.epayment.summary.tooltips.net | 2026-10-08 | kind: observed | quote check: found
- quote: المبلغ الذي سيُحوَّل إلى حسابك البنكي بعد خصم الرسوم والضريبة.
- in context: …لدفع للاشتراكات والخدمات والمشتريات. إجمالي الرصيد طلب استرداد المبلغ رسوم الدفع عند الاستلام تاريخ الطلب الإجمالي رقم الطلب شركة الشحن الضريبة تفاصيل العملية ستتمكن من استعراض عمليات تحويل مستحقات الدفع عند الاستلام هنا. لا توجد عمليات بعد ابحث برقم الطلب إجمالي الرسوم استعرض مستحقاتك من الطلبات المدفوعة عند الاستلام التي ستُحوَّل إلى حسابك البنكي. إجمالي المستحقات ضريبة الرسوم تشمل رسوم الدفع عند الاستلام من قِبل شركة الشحن ورسوم تجربة الشراء. ⟪المبلغ الذي سيُحوَّل إلى حسابك البنكي بعد خصم الرسوم والضريبة.⟫ قيمة ضريبة القيمة المضافة (15%) المطبَّقة على إجمالي الرسوم. إجمالي المبالغ المحصَّلة من طلبات الدفع عند الاستلام قبل خصم الرسوم والضريبة، والتي لم تُحوَّل بعد إلى حسابك البنكي. إجمالي المدفوعات عمليات المدفوعات عند الاستلام المبلغ الرسوم تاريخ الطلب الرسوم: الإجمالي ملاحظات تاريخ الطلب رقم الطلب طريقة الدفع الضريبة تفاصيل العملية ستتمكن من استعراض عمليات تحويل مستحقات المدفوعات الإلكترونية هنا. لا توجد عمليات بعد ابحث برقم الطلب إجمالي الرسوم ا…

### Q5-SA-P0083

**Cited at:** section 8, line 200; section 8, line 203

**The same record as Q3-SA-P0083,** whose card is in `Q3-salla-3.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: في حال مخالفة أي من التجار لما ورد في البند الأول من المادة العاشرة فإنه يقر بحق منصة سلة في اتخاذ أي من الاجراءات التالية وهي على سبيل المثال لا الحصر: التنبيه، إيقاف الخدمة وإغلاق المتجر، إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين.
- scope: 
