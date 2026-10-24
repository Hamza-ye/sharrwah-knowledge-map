# Cards: Q1 on salla

16 records cited by `studies/proposals/drafts/Q1/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 33:** - Salla and Zid keep one set of terms across their countries. Salla's usage agreement, the same at salla.com/terms and salla.com/ar-ae/terms, names شركة تطبيق سلّة لتقنية المعلومات, follows Saudi law and states "كافة الرسوم تحتسب بالريال السعودي". Zid's, Zid Pay's for Kuwait included, follow Saudi law, though Zid Egypt "operates officially under Commercial Registration No.:201574". Q1-SA-094, Q1-SA-095, Q1-SA-096, Q1-ZD-K0212, Q1-ZD-K0221
- **section 1, line 34:** - The platform's own payment product depends on where the seller is based, matching on role (basis 4), Shopify's in its payments terms and the others in help pages: Shopify Payments needs "a business located in your Designated Country"; Zid Pay is "متاح لتجار المملكة العربية السعودية و دولة الكويت"; WooPayments counts the country "where your business is registered — not the one in which you personally live"; BigCommerce Payments needs a store "located in the United Kingdom or the United States"; Salla pays UAE stores "كل يوم خميس" once their balance passes 250 dirhams. Q1-SH-K1536, Q1-ZD-K0005, Q1-WC-K0402, Q1-BC-P0068, Q1-SA-K1547
- **section 1, line 35:** - What a seller must provide depends on the country, matching on role (basis 4): Salla asks at sign-up for the store's country, "لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها"; Zid's requirements differ "حسب نوع النشاط التجاري والدولة". Q1-SA-K1989, Q1-ZD-K0240
- **section 1, line 37:** - What is offered depends on the seller's place, matching on role (basis 4): where Shopify Payments "isn't available in your country", the seller chooses another provider; WooCommerce's code (shipped) keeps "The payment extension list for each country"; Salla's multiple markets feature "is currently available only in Saudi Arabia". Shopify's admin code (shipped) gates Shopify Balance on `"regions":["US"]`, and one Salla session's feature list (observed, 9 October 2026) gives `kyc_new_workflow` the list `"countries": ["AE", "SA", "KW", "QA", "OM", "BH"]`. Q1-SH-065, Q1-WC-K0054, Q1-SA-036, Q1-SH-K0041, Q1-SA-K1988
- **section 1, line 43:** - A seller adds a place to sell to, matching on role (basis 4): on Shopify, a market with a Regions condition; on Salla, "+ سوق جديد"; on Zid, a market published or kept "كسوق مخفي"; on BigCommerce, a merchant "creates a new channel to sell in a new context"; on WooCommerce, a country added to the shipped setting "Selling location(s)". Q1-SH-031, Q1-SA-005, Q1-ZD-012, Q1-BC-K0211, Q1-WC-K0536
- **section 1, line 45:** - A store's first place comes with it, matching on role (basis 4): Shopify creates markets with a new store automatically, and Zid's first market is "السوق الافتراضي وهو السوق المحلي". In the Salla store named demo, observed on 8 October 2026, activating Markets affects "how inventory is deducted" and "cannot be disabled except by contacting the Account Manager". Q1-SH-027, Q1-ZD-003, Q1-SA-107
- **section 1, line 46:** - Places by plan, matching on role (basis 4): Zid allows one, two or five markets by plan, and Salla's feature is "متاحة للمتاجر على باقة سبيشل". Q1-ZD-K0235, Q1-SA-K1978
- **section 1, line 47:** - The platform adds a place where it operates. Salla says "تنطلق سلة من السوق السعودي إلى الكويت الشقيقة", and for such a country publishes articles on verification, Salla Payments activation, settlements and carriers, as for the UAE. Q1-SA-077, Q1-SA-076
- **section 1, line 52:** - Changing the store's currency, matching on role (basis 4): on Shopify, where it is "used within your Shopify admin for pricing products and running reports", a change after the first sale goes through Shopify Support, and a store currency dialog's markup in capture-advanced's saved step text (4 October 2026), with nothing to show it was open, lists "Testing payment processors not available in current currency" among reasons for a change; on Salla, "بشرط أن لا يكون هناك طلبات شراء للعملاء"; on Zid, prices are converted "بناءً على سعر الصرف في وقت التغيير"; on WooCommerce, "Your product prices keep the same numbers", and earlier orders keep their currency. Q1-SH-K1935, Q1-SH-K1936, Q1-SH-121, Q1-SA-093, Q1-ZD-K0302, Q1-WC-016
- **section 1, line 55:** - Connecting a payment provider, matching on role (basis 4): on Shopify "Only the store owner can add a payment provider"; on Salla the seller copies credentials from their own gateway account (dashboard text, observed 8 October 2026), and for Tabby "Your settlement terms and merchant fees follow your agreement with Tabby"; on Zid the seller enters "مفاتيح الربط"; on BigCommerce, the seller applies to the provider and must "complete underwriting" first; on WooCommerce, gateways "can be added through traditional plugins". Q1-SH-064, Q1-SA-K1656, Q1-SA-089, Q1-ZD-K0094, Q1-BC-P0048, Q1-WC-K0006
- **section 1, line 56:** - The platform's own product can shut out others, matching on role (basis 4): Salla Payments can't be turned on while Tap is linked (dashboard text, observed 8 October 2026); Zid Pay allows no other gateway except Tamara and Tabby; where Shopify Payments is available, "standalone Stripe isn't available as an alternative". Q1-SA-K1653, Q1-ZD-K0089, Q1-SH-K1528
- **section 2, line 64:** - It takes the seller's place as the key, with a set-up for all other places, from Shopify's, BigCommerce's and WooCommerce's contracting parties; a per-country set of verification, payments, payouts and carriers from Salla's country articles; and an ordered provider list from WooCommerce's suggestions. Why: a new place is a new set-up, not new code (rule 1); terms per place change most, so this part hides them (rule 2); legal structure and partner contracts cost most to change, so the slots are fixed now and filled by company decisions (rule 3, section 7). Salla's and Zid's one set of terms is one value it can hold. Q1-WC-K0499, Q1-SA-076, Q1-WC-K0054, Q1-SA-094
- **section 2, line 65:** - Its payout slot, for rules such as Salla's per country, serves only an arrangement that holds sellers' money through Sharrwah, which goes live only by the founder's decision. Q1-SA-K1547
- **section 2, line 67:** - It takes the country of registration from WooPayments; the entity apart from the store, used "for financial products, markets, apps, and taxes in this shop" (capture-gb-plus, observed 5 October 2026), with the store's address in its country (capture-advanced's saved step text, 4 October 2026), from Shopify; and the sign-up country from Salla. Sharrwah verifies it, and it changes only by a controlled change acting on new orders, as Shopify asks a seller to "promptly update your location", a market's entity change "affects only new orders", and Zid wants an empty wallet before a store changes country. Why: apart from the store, it lets one seller run several stores, and a market later use another entity, without changing stored records (rule 3). Q1-WC-K0402, Q1-SH-100, Q1-SH-117, Q1-SA-K1989, Q1-SH-K1271, Q1-SH-043, Q1-ZD-K0230
- **section 2, line 68:** - Not taken: the seller's country as a store setting alone, like Salla's store country, since BigCommerce's contract follows the merchant's country of residence and WooPayments the business's registration. Q1-SA-K1989, Q1-BC-K0425, Q1-WC-K0402
- **section 2, line 70:** - It takes the default from BigCommerce and Zid, the lock after orders from Shopify and Salla, and past orders kept from WooCommerce; converting prices at the day's rate, as Zid does, or keeping the numbers, as WooCommerce does, is the seller's choice. Q1-ZD-015, Q1-SH-K1936, Q1-SA-093, Q1-WC-016, Q1-ZD-K0302
- **section 2, line 72:** - It takes store defaults overridden per market from Shopify, whose markets graph view lists a "Business entity" under "Store defaults" in one store's saved step text (demo-fake-dev-store, 30 September 2026), and from BigCommerce; markets made with the store from Shopify and Zid; the hidden state from Zid; and orders that record their market from BigCommerce's storefront attribution. Why: a seller entering a new place adds a market, not a store (rule 1); and with a home market from the start, a second market changes no stored data (rule 3), where Salla's switch-on changes inventory deduction and is undone only through the account manager. Q1-SH-113, Q1-SH-027, Q1-ZD-003, Q1-ZD-012, Q1-BC-003, Q1-SA-107
- **section 2, line 77:** - **Payment provider**, proposed: a company that takes buyers' payments for a seller, in Sharrwah's **provider catalogue** with its places, currencies and methods. For each operating place Sharrwah sets which providers are offered, in order. The seller makes a **provider connection** with credentials from their own account, after the provider's onboarding, and turns **payment methods** on per market and per charged currency. Q1-SH-065, Q1-SA-K1656, Q1-BC-P0048
- **section 2, line 78:** - It takes the offer by the seller's place from Shopify and WooCommerce, the seller's own credentials from Salla and Zid, the provider's underwriting from BigCommerce, methods per market from Shopify and Salla, and per currency from BigCommerce. Why: providers change, so they sit behind one interface (rule 2); and the seller contracts with the provider, which settles under that contract, as Salla's page on Tabby says, so no seller money is held through Sharrwah (rule 3, the guard). Q1-WC-K0054, Q1-ZD-K0094, Q1-SH-051, Q1-SA-033, Q1-SA-089
- **section 2, line 79:** - Not taken now: a Sharrwah payment product that holds sellers' money and shuts out others, as Salla Payments does Tap, Zid Pay most gateways, and Shopify Payments standalone Stripe. The design keeps room for it (section 5); it, and any payment account opened through Sharrwah, goes live only by the founder's decision. Q1-SA-K1653, Q1-ZD-K0089, Q1-SH-K1528
- **section 2, line 80:** - **Availability rule**, proposed: for each feature, service and provider, the operating places and plans where Sharrwah offers it, set by Sharrwah and read wherever something is offered (rule 1); it takes places as keys from Shopify Balance and Salla's `kyc_new_workflow`, and plans from Zid's markets. Q1-SH-K0041, Q1-SA-K1988, Q1-ZD-K0235
- **section 3, line 96:** - Set by the seller: the home place at sign-up, markets, currencies and prices, provider connections, tax rates and delivery zones; on Shopify "Only the store owner can add a payment provider". Q1-SA-K1989, Q1-SH-064
- **section 3, line 98:** - Set by the provider: its places and currencies, its onboarding and its settlement terms. Q1-BC-P0048, Q1-SA-089
- **section 5, line 118:** - Arrangements that hold sellers' money. Salla pays UAE stores every Thursday, Zid Pay serves merchants in Saudi Arabia and Kuwait, and WooPayments' signup "creates a Stripe Express account that is connected to the WooPayments service". Keep the provider interface able to carry a Sharrwah payment product or an account opened through Sharrwah, and each operating place's payout slot empty, until the founder decides under the guard, with a licence decision (section 7). Q1-SA-K1547, Q1-ZD-K0005, Q1-WC-K0371
- **section 7, line 140:** - Where Sharrwah's company is based, and which entity contracts with sellers in each operating place, under which law and terms. Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499, Q1-SA-095
- **section 7, line 141:** - Whether Sharrwah offers a payment product of its own or opens payment accounts for sellers, and under which licence; the platforms' terms tie such products to a regulator, as Salla's transfers to "سلطة وصلاحيات البنك المركزي" and Shopify's Canadian payments entity to the Bank of Canada. Q1-SA-097, Q1-SH-K1614, Q1-WC-K0371, YA-102 (banks and licensed non-bank institutions @ the internationally recognized government's area, as of 2026-02)
- **section 7, line 144:** - The currency of Sharrwah's own fees, and the tax charged on them, in each place. Q1-SA-096, Q1-BC-K0177, Q1-SH-116
- **section 7, line 147:** - Which plans carry markets, and how many. Q1-ZD-K0235, Q1-SA-K1978

## The cards

### Q1-SA-095

**Cited at:** section 1, line 33; section 7, line 140

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-095
- bears_on: 3
- identifier: المادة السادسة والعشرون – القانون والتشريع المُطبّق
- statement: اتفاقية الاستخدام هذه محكومة ومصاغة بحسب القوانين والأنظمة والتشريعات المعمول بها والسارية في المملكة العربية السعودية، وهي خاضعة تمامًا وكليًا للتشريع المعمول به لدى السلطات في المملكة العربية السعودية.
- scope: https://salla.com/terms; https://salla.com/ar-ae/terms
- cite_ids: Q1-SA-C143;Q1-SA-C144
- from: held

**Citation Q1-SA-C143:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 180 (المادة السادسة والعشرون – القانون والتشريع المُطبّق) | 2026-10-06 | kind: official page | quote check: found
- quote: اتفاقية الاستخدام هذه محكومة ومصاغة بحسب القوانين والأنظمة والتشريعات المعمول بها والسارية في المملكة العربية السعودية
- in context: …إملاء إلى وجود علاقة أي كان نوعها سواء كانت مباشرة أو غير مباشرة بينه كتاجر وبين منصة سلّة أو إدارتها ، وأن أي إشعارات يرغب التاجر في إرسالها إلى منصة سلّة ، عليه أن يقوم بإرسالها عبر البريد الإلكتروني وتقوم منصة سلّة بالرد على الرسالة الإلكترونية. وأنت كتاجر توافق على أن أي إشعارات ترسل إليك من منصة سلّة سوف تُسلّم إليك بواسطة البريد الإلكتروني الذي قمت بتزويد منصة سلّة به خلال عملية التسجيل. المادة السادسة والعشرون - القانون والتشريع المُطبّق: ⟪اتفاقية الاستخدام هذه محكومة ومصاغة بحسب القوانين والأنظمة والتشريعات المعمول بها والسارية في المملكة العربية السعودية⟫، وهي خاضعة تمامًا وكليًا للتشريع المعمول به لدى السلطات في المملكة العربية السعودية. المادة السابعة والعشرون - قواعد يجب على المتجر اتباعها عند التعامل مع المستهلك : يلتزم التاجر عند تعامله مع المستهلك أن يلتزم بالصدق والأمانة والنزاهة. يلتزم التاجر عند تعامله مع المستهلك أن يلتزم بحُسن الأخلاق. المادة الثامنة والعشرون - المنشورات الدعائية الورقية والإلكترونية والعروض الخاصة بمنصة سلّة: تسري قواعد وأحكام اتفاقية الاستخدام هذه على كافة المنشورات …

**Citation Q1-SA-C144:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` | offset 3700206 (https://salla.com/ar-ae/terms), المادة السادسة والعشرون – القانون والتشريع المُطبّق | 2026-10-06 | kind: stated | quote check: found
- quote: اتفاقية الاستخدام هذه محكومة ومصاغة بحسب القوانين والأنظمة والتشريعات المعمول بها والسارية في المملكة العربية السعودية
- title: شروط وأحكام استخدام منصة سلة
- in context: …إملاء إلى وجود علاقة أي كان نوعها سواء كانت مباشرة أو غير مباشرة بينه كتاجر وبين منصة سلّة أو إدارتها ، وأن أي إشعارات يرغب التاجر في إرسالها إلى منصة سلّة ، عليه أن يقوم بإرسالها عبر البريد الإلكتروني وتقوم منصة سلّة بالرد على الرسالة الإلكترونية. وأنت كتاجر توافق على أن أي إشعارات ترسل إليك من منصة سلّة سوف تُسلّم إليك بواسطة البريد الإلكتروني الذي قمت بتزويد منصة سلّة به خلال عملية التسجيل. المادة السادسة والعشرون - القانون والتشريع المُطبّق: ⟪اتفاقية الاستخدام هذه محكومة ومصاغة بحسب القوانين والأنظمة والتشريعات المعمول بها والسارية في المملكة العربية السعودية⟫، وهي خاضعة تمامًا وكليًا للتشريع المعمول به لدى السلطات في المملكة العربية السعودية. المادة السابعة والعشرون - قواعد يجب على المتجر اتباعها عند التعامل مع المستهلك : يلتزم التاجر عند تعامله مع المستهلك أن يلتزم بالصدق والأمانة والنزاهة. يلتزم التاجر عند تعامله مع المستهلك أن يلتزم بحُسن الأخلاق. المادة الثامنة والعشرون - المنشورات الدعائية الورقية والإلكترونية والعروض الخاصة بمنصة سلّة: تسري قواعد وأحكام اتفاقية الاستخدام هذه على كافة المنشورات …

### Q1-SA-096

**Cited at:** section 1, line 33; section 7, line 144

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-096
- bears_on: 3
- identifier: المادة السابعة – التعديلات على اتفاقية الاستخدام والرسوم
- statement: كافة الرسوم تحتسب بالريال السعودي، وعلى التاجر دفع كافة الرسوم المستحقة بالمنصة مضافاً إليها أي نفقات أخرى تضيفها منصة سلّة، على أن يتم السداد بواسطة الوسائل المعتمدة والمحددة والمتاحة عن طريق منصة سلّة.
- scope: https://salla.com/terms; https://salla.com/ar-ae/terms
- cite_ids: Q1-SA-C145;Q1-SA-C146
- from: held

**Citation Q1-SA-C145:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 79 (المادة السابعة – التعديلات على اتفاقية الاستخدام والرسوم) | 2026-10-06 | kind: official page | quote check: found
- quote: كافة الرسوم تحتسب بالريال السعودي، وعلى التاجر دفع كافة الرسوم المستحقة بالمنصة
- in context: …اقية الاستخدام فإن ذلك قد يكون عقبة أمام الولوج إلى المتجر، حيث أنه للاستفادة من خدمات منصة سلة يجب الموافقة على هذه الاتفاقية وعلى أي تعديل يطرأ عليها، ولذلك في حالة عدم قبول التعديل تأمل منكم منصة سلّة التوقف عن استخدام خدماتها حيث أن مجرد ولوجكم إلى حسابكم في منصة سلّة أو استخدامكم لمنصة سلة يُعد قبولًا منكم للتعديلات وموافقة كاملة تامة نافية للجهالة، وتسعد منصة سلة الإجابة على استفساراتكم بشأن هذه الاتفاقية واستقبال أي اقتراحات يراها المتجر. ⟪كافة الرسوم تحتسب بالريال السعودي، وعلى التاجر دفع كافة الرسوم المستحقة بالمنصة⟫ مضافاً إليها أي نفقات أخرى تضيفها منصة سلّة، على أن يتم السداد بواسطة الوسائل المعتمدة والمحددة والمتاحة عن طريق منصة سلّة. ليست كل باقات وعروض منصة سلّة مجانية للتُجّار أو للمتاجر حيث أن بعض هذه الباقات والعروض تخضع لرسوم متفاوتة. قد تفرض منصة سلّة رسومًا على التُجّار أو المتاجر وذلك يعتمد على العروض أو الباقات التي ينضمون إليها أو البوليصات التي يستخدمونها. تحتفظ منصة سلّة بحقها في إضافة أو زيادة أو خفض أو خصم أي رسوم أو نفقات بموجب قواعد وأحك…

**Citation Q1-SA-C146:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` | offset 3700206 (https://salla.com/ar-ae/terms), المادة السابعة – التعديلات على اتفاقية الاستخدام والرسوم | 2026-10-06 | kind: stated | quote check: found
- quote: كافة الرسوم تحتسب بالريال السعودي، وعلى التاجر دفع كافة الرسوم المستحقة بالمنصة
- title: شروط وأحكام استخدام منصة سلة
- in context: …اقية الاستخدام فإن ذلك قد يكون عقبة أمام الولوج إلى المتجر، حيث أنه للاستفادة من خدمات منصة سلة يجب الموافقة على هذه الاتفاقية وعلى أي تعديل يطرأ عليها، ولذلك في حالة عدم قبول التعديل تأمل منكم منصة سلّة التوقف عن استخدام خدماتها حيث أن مجرد ولوجكم إلى حسابكم في منصة سلّة أو استخدامكم لمنصة سلة يُعد قبولًا منكم للتعديلات وموافقة كاملة تامة نافية للجهالة، وتسعد منصة سلة الإجابة على استفساراتكم بشأن هذه الاتفاقية واستقبال أي اقتراحات يراها المتجر. ⟪كافة الرسوم تحتسب بالريال السعودي، وعلى التاجر دفع كافة الرسوم المستحقة بالمنصة⟫ مضافاً إليها أي نفقات أخرى تضيفها منصة سلّة، على أن يتم السداد بواسطة الوسائل المعتمدة والمحددة والمتاحة عن طريق منصة سلّة. ليست كل باقات وعروض منصة سلّة مجانية للتُجّار أو للمتاجر حيث أن بعض هذه الباقات والعروض تخضع لرسوم متفاوتة. قد تفرض منصة سلّة رسومًا على التُجّار أو المتاجر وذلك يعتمد على العروض أو الباقات التي ينضمون إليها أو البوليصات التي يستخدمونها. تحتفظ منصة سلّة بحقها في إضافة أو زيادة أو خفض أو خصم أي رسوم أو نفقات بموجب قواعد وأحك…

### Q1-SA-K1547

**Cited at:** section 1, line 34; section 2, line 65; section 5, line 118

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-111
- placement: decides
- structure: https://help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76
- identifier: تحويلات مدفوعات سلة والتسويات في الإمارات
- statement: لمتاجر الإمارات، تُحوّل المستحقات المؤهلة كل يوم خميس عندما يتجاوز رصيد المدفوعات الإلكترونية 250 درهمًا إماراتيًا.
- scope: الإمارات
- cite_ids: SA-S-0080

**Citation SA-S-0080:** `https://help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76` | تحويلات مدفوعات سلة والتسويات في الإمارات (line 656 of the rendered text) | 2026-09-12 | kind: stated | quote check: found
- quote: لمتاجر الإمارات، تُحوّل المستحقات المؤهلة كل يوم خميس عندما يتجاوز رصيد المدفوعات الإلكترونية 250 درهمًا إماراتيًا.
- title: تحويلات مدفوعات سلة والتسويات في الإمارات | سلة | مركز المساعدة - سلة
- the page opens: Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حلول تقنية متقدمة لنمو أعمال كبار التجار المدفوعات طرق …
- in context: …ات مدفوعات سلة والتسويات في الإمارات | سلة تاريخ اخر تحديث: السبت 12 سبتمبر 2026. محتويات المقال التحويلات بنظرة سريعة كيف تعمل التحويلات؟ الحساب البنكي المستخدم لاستلام التحويلات دورية التحويل والحد الأدنى الرسوم المحفظة وتتبع التحويلات الفرق بين رصيد المتجر ورصيد المدفوعات الإلكترونية متى يصلك التحويل الأسئلة الشائعة بعد أن يدفع العميل قيمة الطلب إلكترونيًا بنجاح، تمر الدفعة بمرحلة المعالجة والتسوية قبل تحويل المستحقات إلى حسابك البنكي المسجل. ⟪لمتاجر الإمارات، تُحوّل المستحقات المؤهلة كل يوم خميس عندما يتجاوز رصيد المدفوعات الإلكترونية 250 درهمًا إماراتيًا.⟫ التحويلات بنظرة سريعة تفاصيل التحويل الإمارات دورية التحويل أسبوعيًا، كل يوم خميس الحد الأدنى للتحويل 250 درهم إماراتي الحساب البنكي المستلم الحساب البنكي المستخدم أثناء توثيق المتجر الرسوم وفق عقد خدمات الدفع الموقّع أثناء التوثيق تتبع المدفوعات الإلكترونية في المحفظة قريبًا لمتاجر الإمارات كيف تعمل التحويلات؟ مسار الدفع: يدفع العميل إلكترونيًا ← تُضاف الدفعة إلى رصيد المدفوعات الإلكترونية ← تُحوّل المستحقات المؤهلة إلى حسابك البنكي. -تتم تسوية…

### Q1-SA-K1989

**Cited at:** section 1, line 35; section 2, line 67; section 2, line 68; section 3, line 96

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-167
- placement: decides
- structure: https://help.salla.sa/article/إنشاء-متجر-جديد-خارج-السعودية-الإمارات/huvvumstnafaadcw6abpol14
- identifier: ثانياً: نظرة عامة عن متجرك
- statement: 🌍دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها.
- cite_ids: SA-S-0141

**Citation SA-S-0141:** `https://help.salla.sa/article/إنشاء-متجر-جديد-خارج-السعودية-الإمارات/huvvumstnafaadcw6abpol14` | ثانياً: نظرة عامة عن متجرك (line 673 of the rendered text) | 2026-09-12 | kind: stated | quote check: found
- quote: 🌍دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها.
- title: إنشاء متجر جديد خارج السعودية - الإمارات | مركز المساعدة - سلة
- the page opens: إنشاء متجر جديد خارج السعودية - الإمارات مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة …
- in context: …م الجوال - كلمة المرور. 2. بعد إدخال كافة البيانات، اضغط على (تسجيل) وذلك إذا كنت موافقًا على : سياسة الاستخدام على منصة سلة. 3. سيُرسل إليك رمز تحقق على هاتفك؛ وذلك للتحقق من الرقم المدخل. 3. بعد إدخال كود التحقق المرسل إلى هاتفك، ستوجَّه إلى صفحة الدخول السريع، حيث يمكنك تفعيلها بالبصمة أو Face ID، أو تأجيلها والمتابعة. ثانياً: نظرة عامة عن متجرك 📱بعد التحقق من رقم الهاتف، ستُنقل إلى رحلة البداية لإنشاء حساب جديد والتعرف على تجارتك بنظرة عامة. ⟪🌍دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها.⟫ 🎯الكيان القانوني حدد كيان متجرك, اختيار الكيان الصحيح يساعدك في الامتثال للأنظمة وإصدار التراخيص اللازمة للتوثيق. 3. لديك مجموعة من الأسئلة الخفيفة حول نشاطك الهدف منها جعل رحلتك أكثر سلاسة اختر المنتجات أو الخدمات التي تخطط لبيعها. 💡مثال 1: إذا اخترت نوع الكيان فرد تبدأ الأسئلة بهل تجارتك قائمة؟ 🏦ثم تكمل بتوضيح حالة المتطلبات النظامية وضّح حالة متطلباتك النظامية للبيع في الإمارات, لتوثيق المتجر واستلام المستحقات. ✨وتنتهي بسؤال: ما هو نشاطك التج…

### Q1-SA-036

**Cited at:** section 1, line 37

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-036
- bears_on: 3;4
- identifier: Edit Restriction
- statement: Important notice: The multiple markets feature is currently available only in Saudi Arabia.
- cite_ids: Q1-SA-C059
- from: held

**Citation Q1-SA-C059:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl` | line 432 (article f9bsa0insqb43sh6r41i4gfm, Create and manage product restrictions), Edit Restriction | 2026-08-31 | kind: stated | quote check: found
- quote: Important notice: The multiple markets feature is currently available only in Saudi Arabia.
- in context: …h by Restriction Name Use the search bar to quickly find a specific restriction using keywords. Manage an Existing Restriction You can edit, disable, or delete a restriction at any time. Only one restriction can be applied per product, but all available conditions within that restriction can be enabled together. To manage a restriction, click the options icon next to it. Edit Restriction Update the restriction details as needed, then click Save. ⟪Important notice: The multiple markets feature is currently available only in Saudi Arabia.⟫ Disable Restriction Disabling a restriction immediately changes its status to Inactive. You can re-enable it at any time by clicking Activate Restriction. Delete Restriction When the delete confirmation appears, choose: Yes, delete to confirm Cancel to keep the restriction Frequently Asked Questions Which plans support product restrictions? The feature is available on Salla Pro and Special plans. How do I apply the restriction to all customers? …

### Q1-SA-K1988

**Cited at:** section 1, line 37; section 2, line 80

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-167
- placement: decides
- structure: observed-sa@145f137:structures/salla/dashboard-features/merchant@en/items.jsonl
- identifier: kyc_new_workflow
- statement: {"position": 140, "name": "kyc_new_workflow", "value": {"enabled": true, "released": true, "plans": [], "countries": ["AE", "SA", "KW", "QA", "OM", "BH"], "type": "feature"}}
- scope: countries: AE, SA, KW, QA, OM, BH
- cite_ids: SA-S-3101

**Citation SA-S-3101:** `observed-sa@145f137:structures/salla/dashboard-features/merchant@en/items.jsonl` | line 141 | 2026-10-09 | kind: observed | quote check: found
- quote: {"position": 140, "name": "kyc_new_workflow", "value": {"enabled": true, "released": true, "plans": [], "countries": ["AE", "SA", "KW", "QA", "OM", "BH"], "type": "feature"}}
- in context: …ion": 137, "name": "gamification-system", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} {"position": 138, "name": "order-print-multi-policy", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} {"position": 139, "name": "auth-recaptcha", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} ⟪{"position": 140, "name": "kyc_new_workflow", "value": {"enabled": true, "released": true, "plans": [], "countries": ["AE", "SA", "KW", "QA", "OM", "BH"], "type": "feature"}}⟫ {"position": 141, "name": "products-importer", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} {"position": 142, "name": "custom-import", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} {"position": 143, "name": "merchant-auth-callback", "value": {"enabled": true, "released": false, "plans": [], "countries": [], "type": "feature"}} {"position": 144, "…

### Q1-SA-005

**Cited at:** section 1, line 43

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-005
- bears_on: 4
- identifier: 🌟 إضافة أسواق جديدة
- statement: 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ).
- cite_ids: Q1-SA-C016;Q1-SA-C017
- from: held

**Citation Q1-SA-C016:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🌟 إضافة أسواق جديدة | 2026-09-27 | kind: stated | quote check: found
- quote: 1. لإضافة سوق جديد ، اضغط (+ سوق جديد).
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ط ( الأسواق المتعددة ). تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين - خيارات الدخول والتسجيل - تصميم المتجر بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة ⟪1. لإضافة سوق جديد ، اضغط (+ سوق جديد).⟫ 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ). القسم 1: المعلومات الأساسية اختر الدول التي سيُعرض لها السوق، واسم يدل على هذه السوق، بالإضافة للغة الافتراضية واللغات الأخرى المدعومة للسوق، وهل تريد إظهار السوق للعملاء أم لا. 🔔 ملاحظة : يتم تحديد اللغة وتطبيقها بشكل مستقل لكل سوق. القسم 2: العملات اختر العملة الافتراضية والعملات الأخرى المدعومة للسوق. القسم 3: الفروع والمستودعات 1. حدد الفروع الخاصة بالسوق، وخصص الخيارات الأخرى. 2. ح…

**Citation Q1-SA-C017:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🌟 إضافة أسواق جديدة | 2026-09-27 | kind: stated | quote check: found
- quote: 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ).
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …اق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين - خيارات الدخول والتسجيل - تصميم المتجر بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). ⟪2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ).⟫ القسم 1: المعلومات الأساسية اختر الدول التي سيُعرض لها السوق، واسم يدل على هذه السوق، بالإضافة للغة الافتراضية واللغات الأخرى المدعومة للسوق، وهل تريد إظهار السوق للعملاء أم لا. 🔔 ملاحظة : يتم تحديد اللغة وتطبيقها بشكل مستقل لكل سوق. القسم 2: العملات اختر العملة الافتراضية والعملات الأخرى المدعومة للسوق. القسم 3: الفروع والمستودعات 1. حدد الفروع الخاصة بالسوق، وخصص الخيارات الأخرى. 2. حدد استراتيجية إنقاص المخزون: تحديد كيفية انقاص كميات المنتجا…

### Q1-SA-107

**Cited at:** section 1, line 45; section 2, line 72

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-107
- bears_on: 4
- identifier: Confirm activating this feature
- statement: Confirm activating this feature Activating this feature will affect how product quantities are configured and how inventory is deducted in your store. Once enabled, it cannot be disabled except by contacting the Account Manager.
- scope: store demo, observed 2026-10-08
- cite_ids: Q1-SA-C159
- from: held

**Citation Q1-SA-C159:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T180430Z-journey-localization-demo/steps/002.text.txt` | step 2 (https://s.salla.sa/localization, Salla | Markets) | 2026-10-08 | kind: observed | quote check: found
- step 2: Activate feature now | https://s.salla.sa/localization | "Salla | Markets" | 2026-10-08T18:04:48.159Z
- the step's files: `observed-sa@4ca2e896a:raw/runs/20261008T180430Z-journey-localization-demo/steps/002.aria.yaml`, `observed-sa@4ca2e896a:raw/runs/20261008T180430Z-journey-localization-demo/steps/002.text.txt`
- quote: Confirm activating this feature Activating this feature will affect how product quantities are configured and how inventory is deducted in your store. Once enabled, it cannot be disabled except by contacting the Account Manager.
- in context: …r warehouse. Offer flexible pickup and delivery options Control order fulfillment across branches and warehouses Fulfill orders from the branch or warehouse closest to the customer Allocate inventory by location, quantity, or priority Shop by fulfillment method Pickup or delivery selection popup Let customers choose delivery or pickup before shopping and see only the products available for their selected option. Activate feature now Learn more i ⟪Confirm activating this feature Activating this feature will affect how product quantities are configured and how inventory is deducted in your store. Once enabled, it cannot be disabled except by contacting the Account Manager.⟫ Confirm Cancel

### Q1-SA-K1978

**Cited at:** section 1, line 46; section 7, line 147

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-165
- placement: decides
- structure: https://help.salla.sa/article/تفعيل-وإدارة-الأسواق-المتعددة/wv9wyqrnhwpm6m2rp3cmg653
- identifier: 🚀الأسواق المتعددة
- statement: ✅ الميزة متاحة للمتاجر على باقة سبيشل.
- scope: باقة سبيشل
- cite_ids: SA-S-0158

**Citation SA-S-0158:** `https://help.salla.sa/article/تفعيل-وإدارة-الأسواق-المتعددة/wv9wyqrnhwpm6m2rp3cmg653` | 🚀الأسواق المتعددة (line 691 of the rendered text) | 2026-09-27 | kind: stated | quote check: found
- quote: ✅ الميزة متاحة للمتاجر على باقة سبيشل.
- title: تفعيل الأسواق المتعددة وإضافة سوق جديد | مركز المساعدة - سلة
- the page opens: تفعيل الأسواق المتعددة وإضافة سوق جديد مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سب…
- in context: …كنك من إنشاء نسخ مخصصة من متجرك الإلكتروني لكل دولة تستهدفها أو منطقة أو مدينة، بما يضمن ظهور المتجر للعملاء في هذه المنطقة بتجربة تتوافق مع توقعاتهم المحلية. يمكنك تخصيص سوق لأي دولة أو منطقة من دول الخليج من حيث: - التصميم - الأسعار - العملة - دومين المتجر - خيارات الشحن كل نسخة تُدار بشكل مستقل مع نظام متكامل لإدارة المخزون والطلبات، ما يتيح لك توصيل الطلبات من أقرب فرع للعميل، ويسهم في تقليل تكاليف الشحن، وتسريع التوصيل، ورفع كفاءة العمليات. ⟪✅ الميزة متاحة للمتاجر على باقة سبيشل.⟫ باختصار، تضع ميزة الأسواق المتعددة أدوات التوسّع الإقليمي بين يديك بسهولة، وفعالية، واحترافية. 🚀تفعيل الأسواق المتعددة: 1. من قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم اضغط (الأسواق المتعددة). 2. اضغط (فعل الآن). 3. للمضي قدماً في تفعيل الأسواق المتعددة، اضغط (تأكيد). 🚀 صفحة الأسواق المتعددة من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط (الأسواق المتعددة). تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - …

### Q1-SA-077

**Cited at:** section 1, line 47

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-077
- bears_on: 3;4
- identifier: إنشاء متجر جديد خارج السعودية - الكويت
- statement: تنطلق سلة من السوق السعودي إلى الكويت الشقيقة، حاملة نفس الإيمان والدعم لكل تاجر طموح.
- scope: الكويت
- cite_ids: Q1-SA-C107
- from: held

**Citation Q1-SA-C107:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 220 (article i8d4lq5xfx3sr05m59uwh64d, إنشاء متجر جديد خارج السعودية - الكويت), introduction | 2026-09-10 | kind: stated | quote check: found
- quote: تنطلق سلة من السوق السعودي إلى الكويت الشقيقة، حاملة نفس الإيمان والدعم لكل تاجر طموح.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … الكوبونات عندما تحتاج إلى أكواد فريدة لعدد كبير من العملاء. ✅ راجع شروط الكوبون قبل نشره للتأكد من توافقها مع العرض الذي تريد تقديمه. هل تريد إنشاء عدة أكواد دفعة واحدة؟ تعرّف على إنشاء مجموعة كوبونات لإنشاء مجموعة من الكوبونات بنفس الإعدادات بسهولة. i8d4lq5xfx3sr05m59uwh64d https://help.salla.sa/article/%D8%A5%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D8%AA%D8%AC%D8%B1-%D8%AC%D8%AF%D9%8A%D8%AF-%D8%A7%D9%84%D9%83%D9%88%D9%8A%D8%AA/i8d4lq5xfx3sr05m59uwh64d ⟪تنطلق سلة من السوق السعودي إلى الكويت الشقيقة، حاملة نفس الإيمان والدعم لكل تاجر طموح.⟫ في هذا المقال، نأخذك خطوة بخطوة في رحلة إنشاء متجرك الجديد على سلة، من أول تسجيل دخول وحتى إطلاق متجرك بثقة✨. خطوات تسجيل حساب في سلة أولاً: إدخال بيانات إنشاء الحساب 1. من صفحة التسجيل حدد اللغة التي ستُكمل بها إعداد حسابك. ثم أدخل البيانات المطلوبة, ومنها: اسم التاجر - البريد الإلكتروني - رقم الجوال - كلمة المرور. 2. بعد إدخال كافة البيانات، اضغط على (تسجيل) وذلك إذا كنت موافقًا على : سياسة الاستخدام على منصة سلة. 3. سيُرسل إليك رمز تحقق على ه…

### Q1-SA-076

**Cited at:** section 1, line 47; section 2, line 64

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-076
- bears_on: 3
- identifier: مقالات ذات صلة
- statement: -توثيق متجرك في الإمارات | سلة - تفعيل مدفوعات سلة في الإمارات | سلة -تحويلات مدفوعات سلة والتسويات في الإمارات | سلة -تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة
- scope: الإمارات
- cite_ids: Q1-SA-C103;Q1-SA-C104;Q1-SA-C105;Q1-SA-C106
- from: held

**Citation Q1-SA-C103:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 221 (article huvvumstnafaadcw6abpol14, إنشاء متجر جديد خارج السعودية - الإمارات), مقالات ذات صلة | 2026-09-12 | kind: stated | quote check: found
- quote: -توثيق متجرك في الإمارات | سلة
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …متطلبات النظامية وضّح حالة متطلباتك النظامية للبيع في الإمارات, لتوثيق المتجر واستلام المستحقات. ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 💡مثال 2: إذا اخترت نوع الكيان شركة تبدأ الأسئلة بسؤال: هل تجارتك قائمة؟ ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 🚀ستُوجَّه إلى تحديد باقة متجرك وإكمال رحلتك في تدشين المتجر. ثالثاً: تحديد باقة المتجر 🛒اختر باقة المتجر التي تناسب نشاطك. في أسفل الصفحة, يمكنك مقارنة باقات سلة لاختيار الباقة الأمثل لتجارتك مقالات ذات صلة ⟪-توثيق متجرك في الإمارات | سلة⟫ - تفعيل مدفوعات سلة في الإمارات | سلة -تحويلات مدفوعات سلة والتسويات في الإمارات | سلة -تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة ✨ ابدأ رحلتك بثقة! ستجد في هذه المقالة دليلك العملي للانطلاق بخطوات واضحة من إعداد متجرك إلى استلام أول طلب، لتختصر وقت البداية وتبدأ نجاحك من اليوم. 🚀 خدمات مساندة في حال احتجت مساعدة في إنشاء متجرك، يمكنك الاستفادة من الخدمات التي يقدمها خبراء موثوقين في مجال إنشاء المتاجر بكافة أنواعها من البداية للإطلاق باحت…

**Citation Q1-SA-C104:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 221 (article huvvumstnafaadcw6abpol14, إنشاء متجر جديد خارج السعودية - الإمارات), مقالات ذات صلة | 2026-09-12 | kind: stated | quote check: found
- quote: - تفعيل مدفوعات سلة في الإمارات | سلة
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …باتك النظامية للبيع في الإمارات, لتوثيق المتجر واستلام المستحقات. ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 💡مثال 2: إذا اخترت نوع الكيان شركة تبدأ الأسئلة بسؤال: هل تجارتك قائمة؟ ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 🚀ستُوجَّه إلى تحديد باقة متجرك وإكمال رحلتك في تدشين المتجر. ثالثاً: تحديد باقة المتجر 🛒اختر باقة المتجر التي تناسب نشاطك. في أسفل الصفحة, يمكنك مقارنة باقات سلة لاختيار الباقة الأمثل لتجارتك مقالات ذات صلة -توثيق متجرك في الإمارات | سلة ⟪- تفعيل مدفوعات سلة في الإمارات | سلة⟫ -تحويلات مدفوعات سلة والتسويات في الإمارات | سلة -تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة ✨ ابدأ رحلتك بثقة! ستجد في هذه المقالة دليلك العملي للانطلاق بخطوات واضحة من إعداد متجرك إلى استلام أول طلب، لتختصر وقت البداية وتبدأ نجاحك من اليوم. 🚀 خدمات مساندة في حال احتجت مساعدة في إنشاء متجرك، يمكنك الاستفادة من الخدمات التي يقدمها خبراء موثوقين في مجال إنشاء المتاجر بكافة أنواعها من البداية للإطلاق باحترافية من تصميم الواجهات وتفعيل طرق الد…

**Citation Q1-SA-C105:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 221 (article huvvumstnafaadcw6abpol14, إنشاء متجر جديد خارج السعودية - الإمارات), مقالات ذات صلة | 2026-09-12 | kind: stated | quote check: found
- quote: -تحويلات مدفوعات سلة والتسويات في الإمارات | سلة
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ق المتجر واستلام المستحقات. ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 💡مثال 2: إذا اخترت نوع الكيان شركة تبدأ الأسئلة بسؤال: هل تجارتك قائمة؟ ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 🚀ستُوجَّه إلى تحديد باقة متجرك وإكمال رحلتك في تدشين المتجر. ثالثاً: تحديد باقة المتجر 🛒اختر باقة المتجر التي تناسب نشاطك. في أسفل الصفحة, يمكنك مقارنة باقات سلة لاختيار الباقة الأمثل لتجارتك مقالات ذات صلة -توثيق متجرك في الإمارات | سلة - تفعيل مدفوعات سلة في الإمارات | سلة ⟪-تحويلات مدفوعات سلة والتسويات في الإمارات | سلة⟫ -تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة ✨ ابدأ رحلتك بثقة! ستجد في هذه المقالة دليلك العملي للانطلاق بخطوات واضحة من إعداد متجرك إلى استلام أول طلب، لتختصر وقت البداية وتبدأ نجاحك من اليوم. 🚀 خدمات مساندة في حال احتجت مساعدة في إنشاء متجرك، يمكنك الاستفادة من الخدمات التي يقدمها خبراء موثوقين في مجال إنشاء المتاجر بكافة أنواعها من البداية للإطلاق باحترافية من تصميم الواجهات وتفعيل طرق الدفع وغيرها. ya5z2fsehfy3ok1wei82jgr0 https://help.…

**Citation Q1-SA-C106:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 221 (article huvvumstnafaadcw6abpol14, إنشاء متجر جديد خارج السعودية - الإمارات), مقالات ذات صلة | 2026-09-12 | kind: stated | quote check: found
- quote: -تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … نشاطك التجاري؟ 💡مثال 2: إذا اخترت نوع الكيان شركة تبدأ الأسئلة بسؤال: هل تجارتك قائمة؟ ✨ وتنتهي بسؤال: ما هو نشاطك التجاري؟ 🚀ستُوجَّه إلى تحديد باقة متجرك وإكمال رحلتك في تدشين المتجر. ثالثاً: تحديد باقة المتجر 🛒اختر باقة المتجر التي تناسب نشاطك. في أسفل الصفحة, يمكنك مقارنة باقات سلة لاختيار الباقة الأمثل لتجارتك مقالات ذات صلة -توثيق متجرك في الإمارات | سلة - تفعيل مدفوعات سلة في الإمارات | سلة -تحويلات مدفوعات سلة والتسويات في الإمارات | سلة ⟪-تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة⟫ ✨ ابدأ رحلتك بثقة! ستجد في هذه المقالة دليلك العملي للانطلاق بخطوات واضحة من إعداد متجرك إلى استلام أول طلب، لتختصر وقت البداية وتبدأ نجاحك من اليوم. 🚀 خدمات مساندة في حال احتجت مساعدة في إنشاء متجرك، يمكنك الاستفادة من الخدمات التي يقدمها خبراء موثوقين في مجال إنشاء المتاجر بكافة أنواعها من البداية للإطلاق باحترافية من تصميم الواجهات وتفعيل طرق الدفع وغيرها. ya5z2fsehfy3ok1wei82jgr0 https://help.salla.sa/article/%D8%A5%D9%86%D8%B4%D8%A7%D8%A1-%…

### Q1-SA-093

**Cited at:** section 1, line 52; section 2, line 70

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-093
- bears_on: 5
- identifier: ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟
- statement: نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء.
- cite_ids: Q1-SA-C140
- from: held

**Citation Q1-SA-C140:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 134 (article u4s3nz2yd3gxd92e8r4dpwbd, إضافة عملة جديدة للمتجر), الأسئلة الشائعة | 2026-08-31 | kind: stated | quote check: found
- quote: نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …: - خطوات إضافة العملات إلى المتجر - الأسئلة الشائعة 🚀 خطوات إضافة العملات إلى المتجر 1. من القائمة الرئيسية، اضغط (مركز الإعدادات). 2. من تبويب ( عام )، اضغط (العملات). 3. عيّن العملات المتاحة في متجرك، ثم اضغط (حفظ). 1- عيّن العملة الحالية للمتجر. 2- فعّل حالة العملات المتاحة حسب حاجة متجرك. 3- اختر عملة جديدة، ثم اضغط (إضافة) لإضافة عملة إلى العملات المتاحة في متجرك. 🚀 الأسئلة الشائعة ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟ ⟪نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء.⟫ ❓كيف يستطيع العميل اختيار العملة التي يُفضل الدفع بها؟ عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر. فتظهر له أسعار المنتجات بالعملة المختارة، بالشكل: 💡 توضيح مهم: عملة المتجر الافتراضية التي تظهر للعميل تعتمد على موقع العميل الجغرافي، وليست مرتبطة بالعملة الافتراضية المضافة داخل إعدادات المتجر. هذا يعني أن الأسعار قد تُعرض بعملة محلية مختلفة تلقائياً لتسهيل تجربة الشراء ل…

### Q1-SA-K1656

**Cited at:** section 1, line 55; section 2, line 77

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-120
- placement: boundary
- structure: observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json
- identifier: gateway_settings.credentials_desc
- statement: يمكنك الحصول على البيانات التالية من حسابك في بوابة الدفع، ثم نسخها وإضافتها في الحقول المخصصة. انتقل إلى
- cite_ids: SA-S-0205

**Citation SA-S-0205:** `observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json` | gateway_settings.credentials_desc | 2026-10-08 | kind: observed | quote check: found
- quote: يمكنك الحصول على البيانات التالية من حسابك في بوابة الدفع، ثم نسخها وإضافتها في الحقول المخصصة. انتقل إلى
- in context: …مل الحر","apply_name_label":"اسم صاحب الحساب البنكي بالإنجليزية","apply_policy":"أوافق على مشاركة البيانات مع {{name}}","apply_policy_desc":"بناءً على طلبك، فإنك توافق وتمنح شركة سلة الحق في مشاركة بيانات متجرك المطلوبة لإتمام تسجيل حسابك مع شركة {{name}}، مع عدم تحميل شركة سلة أي مسؤولية في هذا الشأن.","apply_submit":"إرسال الطلب","apply_success":"أُرسل طلبك إلى {{name}} بنجاح.","choose_option":"اختر طريقة الربط مع {{name}}","credentials_desc":"⟪يمكنك الحصول على البيانات التالية من حسابك في بوابة الدفع، ثم نسخها وإضافتها في الحقول المخصصة. انتقل إلى⟫","credentials_link_apple_pay":"حسابك على أبل باي","credentials_link_tabby":"حسابك على تابي","credentials_link_tamara":"حسابك على تمارا","credentials_title":"بيانات الربط","field_placeholders":{"account":"البريد الإلكتروني المسجَّل في {{name}}"},"field_required":"هذا الحقل مطلوب.","fields":{"account":"البريد الإلكتروني","burn_enabled":"إتاحة استبدال نقاط مكافأة الراجحي","merchant_private_key":"المفتاح الخاص","merchant_public_key":"المفتاح العام",…

### Q1-SA-089

**Cited at:** section 1, line 55; section 2, line 78; section 3, line 98

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-089
- bears_on: 5
- identifier: What is Tabby?
- statement: Payment and settlement: Payments made through Tabby are collected through Tabby rather than Salla Payments. Your settlement terms and merchant fees follow your agreement with Tabby.
- scope: UAE
- cite_ids: Q1-SA-C133
- from: held

**Citation Q1-SA-C133:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl` | line 29 (article wmmkc305vzb52ka2al4zbfrh, Activate Tabby on your Salla store in the UAE | Salla), What is Tabby? | 2026-09-16 | kind: stated | quote check: found
- quote: Payment and settlement: Payments made through Tabby are collected through Tabby rather than Salla Payments. Your settlement terms and merchant fees follow your agreement with Tabby.
- in context: … this guide, you'll learn what you need before activation, how to connect Tabby to your Salla store, and how the payment method works after it is enabled. What is Tabby? Tabby is a Buy Now, Pay Later (BNPL) payment method that lets eligible customers complete a purchase without paying the full order amount upfront. Offering flexible payment options can help increase purchasing power, improve checkout conversion, and increase average order value. ⟪Payment and settlement: Payments made through Tabby are collected through Tabby rather than Salla Payments. Your settlement terms and merchant fees follow your agreement with Tabby.⟫ Before you start Prepare the following before you connect Tabby to your store: Requirement What you need Verified Salla store Your store must be verified before Tabby can be connected and activated. Tabby merchant account You need an active merchant relationship with Tabby. Stores outside Saudi Arabia must complete account setup directly with Tabby. Gateway credentials Have your Merchant Public Key and Merchant Private Key ready from your Tabby …

### Q1-SA-K1653

**Cited at:** section 1, line 56; section 2, line 79

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-120
- placement: decides
- structure: observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json
- identifier: gcc_banner.tap_active.description
- statement: لن تتمكن من تفعيل مدفوعات سلة حاليًا لوجود ربط فعَّال مع تاب.
- cite_ids: SA-S-0100

**Citation SA-S-0100:** `observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json` | gcc_banner.tap_active.description | 2026-10-08 | kind: observed | quote check: found
- quote: لن تتمكن من تفعيل مدفوعات سلة حاليًا لوجود ربط فعَّال مع تاب.
- in context: …صل مع {{name}}","tutorial_alert_text":"ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد،","verification_description":"وثِّق متجرك لتفعيل طرق الدفع وإدارة مدفوعاتك بأمان.","verification_required":"متجرك غير موثَّق","verify_now":"وثِّقه الآن"},"gcc_banner":{"description":"نعمل حاليًا على مراجعة بيانات متجرك لتفعيل المدفوعات الإلكترونية. سنُشعرك فور اكتمال المراجعة أو عند الحاجة إلى أي معلومات إضافية.","tap_active":{"description":"⟪لن تتمكن من تفعيل مدفوعات سلة حاليًا لوجود ربط فعَّال مع تاب.⟫","title":"متجرك مرتبط ببوابة دفع أخرى"},"title":"طلب تفعيل المدفوعات قيد المراجعة"},"market_selector":{"placeholder":"حدِّد السوق"},"merchant_info":{"accordion_title":"عرض المعلومات","account_holder":"اسم صاحب الحساب","annual_sales":"المبيعات السنوية","annual_sales_label":"أقل من 250 ألف دولار","ar_annual_sales_label":"أقل من 250 ألف دولار","bank_account":"الحساب البنكي","business_license":"الرخصة التجارية","commercial_register_name":"اسم المنشأ…

### Q1-SA-097

**Cited at:** section 7, line 141

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-097
- bears_on: 3
- identifier: المادة التاسعة عشرة – عمليات الدفع والبيع والشراء
- statement: يُقر كافة التُجّار وتُقر كافة المتاجر بعلمهم التام والنافي للجهالة بأن إدارة منصة سلّة في تحويلها للأموال الخاصة بأنشطتهم التجارية داخل منصة سلّة تخضع لسلطة وصلاحيات البنك المركزي بالمملكة العربية السعودية
- scope: https://salla.com/terms; https://salla.com/ar-ae/terms
- cite_ids: Q1-SA-C147;Q1-SA-C148
- from: held

**Citation Q1-SA-C147:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 164 (المادة التاسعة عشرة – عمليات الدفع والبيع والشراء) | 2026-10-06 | kind: official page | quote check: found
- quote: بأن إدارة منصة سلّة في تحويلها للأموال الخاصة بأنشطتهم التجارية داخل منصة سلّة تخضع لسلطة وصلاحيات البنك المركزي بالمملكة العربية السعودية
- in context: …لمنصة سلة بأي تقصير يحصل من المستهلك تجاه المتجر، سواءً بتخلّفه عن السداد أو غير ذلك. يوافق التاجر ويقر أنه لن يقوم بعمليات شراء غير حقيقية أو متلاعبة على منصة سلّة، ولن يستخدم اسم غير حقيقي أو أي معلومات شخصية غير حقيقية، أو استخدام بطاقة ائتمان لا تخصه دون تفويض بالشراء، حيث أن منصة سلّة لها الحق في اتخاذ الإجراءات القانونية المناسبة ضد كل من يقوم بعمليات احتيالية من هذا النوع. يُقر كافة التُجّار وتُقر كافة المتاجر بعلمهم التام والنافي للجهالة ⟪بأن إدارة منصة سلّة في تحويلها للأموال الخاصة بأنشطتهم التجارية داخل منصة سلّة تخضع لسلطة وصلاحيات البنك المركزي بالمملكة العربية السعودية⟫، ونتيجة لذلك فإن منصة سلّة تُنوّه كافة المتاجر والتُجار بأنها قدّ تتأخّر في تحويل بعض الأموال وذلك نتيجة لقيود البنك المركزي ووزارة التجارة والاستثمار وأنظمة التجارة الإلكترونية المفروضة على عمليات البيع والشراء الإلكترونية . تحتفظ منصة سلّة بحقها في فرض أي رسوم على التُجّار أو المتاجر نتيجة لعملياتهم داخل منصة سلّة، والرسوم قدّ تكون على سبيل المثال لا الحصر : رسوم الجهات الحكومية أو رسوم بنكية أو رسوم إدارية أو أي رسوم أخرى ، تجري مطالبة منصة س…

**Citation Q1-SA-C148:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` | offset 3700206 (https://salla.com/ar-ae/terms), المادة التاسعة عشرة – عمليات الدفع والبيع والشراء | 2026-10-06 | kind: stated | quote check: found
- quote: بأن إدارة منصة سلّة في تحويلها للأموال الخاصة بأنشطتهم التجارية داخل منصة سلّة تخضع لسلطة وصلاحيات البنك المركزي بالمملكة العربية السعودية
- title: شروط وأحكام استخدام منصة سلة
- in context: …لمنصة سلة بأي تقصير يحصل من المستهلك تجاه المتجر، سواءً بتخلّفه عن السداد أو غير ذلك. يوافق التاجر ويقر أنه لن يقوم بعمليات شراء غير حقيقية أو متلاعبة على منصة سلّة، ولن يستخدم اسم غير حقيقي أو أي معلومات شخصية غير حقيقية، أو استخدام بطاقة ائتمان لا تخصه دون تفويض بالشراء، حيث أن منصة سلّة لها الحق في اتخاذ الإجراءات القانونية المناسبة ضد كل من يقوم بعمليات احتيالية من هذا النوع. يُقر كافة التُجّار وتُقر كافة المتاجر بعلمهم التام والنافي للجهالة ⟪بأن إدارة منصة سلّة في تحويلها للأموال الخاصة بأنشطتهم التجارية داخل منصة سلّة تخضع لسلطة وصلاحيات البنك المركزي بالمملكة العربية السعودية⟫، ونتيجة لذلك فإن منصة سلّة تُنوّه كافة المتاجر والتُجار بأنها قدّ تتأخّر في تحويل بعض الأموال وذلك نتيجة لقيود البنك المركزي ووزارة التجارة والاستثمار وأنظمة التجارة الإلكترونية المفروضة على عمليات البيع والشراء الإلكترونية . تحتفظ منصة سلّة بحقها في فرض أي رسوم على التُجّار أو المتاجر نتيجة لعملياتهم داخل منصة سلّة، والرسوم قدّ تكون على سبيل المثال لا الحصر : رسوم الجهات الحكومية أو رسوم بنكية أو رسوم إدارية أو أي رسوم أخرى ، تجري مطالبة منصة س…
