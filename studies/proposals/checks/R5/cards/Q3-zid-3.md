# Cards: Q3 on zid

15 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 34:** - Payment providers and card networks set lists of what may not be sold, a match on role. On Shopify, "Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers" (its terms, official page). WooPayments cites "restrictions put in place by card networks, our payment processors, and their financial service providers", and BigCommerce points to Stripe's list (help pages, stated). Zid Pay's terms accept some digital products on the service provider's assessment. Q3-SH-P0045; Q3-WC-K0416; Q3-BC-021; Q3-ZD-K0070
- **section 1, line 37:** - Salla's agreement and Zid's terms carry the same clause for products needing an official licence, "بالإفصاح عن الترخيص وكافة بياناته": the same term, both official pages. Neither platform's full list of such products was in what was read; Zid decides the need after reviewing the data, with books and the Ministry of Media as its example. Q3-SA-047; Q3-ZD-K0247; Q3-SA-N02; Q3-ZD-N04; Q3-ZD-023
- **section 1, line 39:** - The registered activity must match the products, a match on role: Salla's KYC schema for a demo store, observed 8 October 2026, says "Commercial registration activity must match the store activity", and Zid's help page "أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر". Q3-SA-058; Q3-ZD-003
- **section 1, line 45:** - A program or channel often needs another capability active, a match on role. Shop needs Shopify Payments activated; Mahally needs a paid plan and a verified store (not checked on WooCommerce; shown by Salla); and Zid Financing needs Zid Pay activated and approved. Q3-SH-077; Q3-SA-061; Q3-ZD-P0132
- **section 1, line 46:** - The business's country is hard to change: WooPayments' country "cannot be changed later", and Zid's terms for merchants outside Saudi Arabia ask one moving the store to another country to zero the wallet balance first. Q3-WC-011; Q3-ZD-K0230
- **section 1, line 51:** - Salla requires every verification document to be in the store owner's own name. Its KYC schema for a demo store, observed 8 October 2026, offers the entity types `single`, `company`, `institution`, `charity` and `government`; Zid's business types are فرد، مؤسسة، شركة، جمعية خيرية. They match on role in four of five (Salla's schema observed, Zid's help page stated); Salla adds government. Q3-SA-019; Q3-SA-056; Q3-ZD-K0239
- **section 1, line 60:** - Payment partners approve, a match on role (BigCommerce's pricing page, official; the others help pages, stated): Zid's requirements go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and its Nafath request is in the service provider's name; a PayPal Braintree application on BigCommerce doesn't guarantee approval; WooPayments verifies with Stripe; and Shopify's banking partners require a real person on every account. Q3-ZD-P0118; Q3-ZD-P0047; Q3-BC-P0065; Q3-WC-012; Q3-SH-020
- **section 1, line 61:** - Law, regulators and networks set others, as the platforms report them: Shopify's European and UK verification follows the FCA and the Central Bank of Ireland, and its prohibited categories may come from law, network rules, Shopify or processors' providers; Zid's licences come from the relevant authorities; and Salla's e-commerce obligations from the e-commerce law and the Ministry of Commerce's guide. Q3-SH-065; Q3-SH-P0045; Q3-ZD-023; Q3-SA-033
- **section 1, line 65:** - When the seller applies, with review times that differ: Salla 24 to 48 hours; Shopify's documents up to 24 hours; WooPayments typically a couple of days. Zid's team reviews and notifies by email. Q3-SA-003; Q3-SH-014; Q3-WC-004; Q3-ZD-P0038
- **section 1, line 66:** - Attempts are limited: Absher three a day on Salla, Nafath three a day on Zid. Q3-SA-008; Q3-ZD-K0262
- **section 1, line 67:** - And again later. Shopify re-verifies periodically, and re-checks bank ownership when a payout account is added or replaced or business details change. Salla may ask for documents at any time, and Zid Pay's seller must report changes within a week. On BigCommerce, Stripe flags accounts for verification after a processing threshold. Q3-SH-066; Q3-SH-061; Q3-SA-051; Q3-ZD-078; Q3-BC-020
- **section 1, line 74:** - Zid Pay gives 14 days to correct wrong data, then disables the account and returns all amounts to end customers. Salla suspends payments and settlement "بعد انتهاء المهلة", a period whose length was not in what was read. WooPayments may restrict payments or payouts once a deadline for missing information passes. Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01; Q3-WC-P0055
- **section 1, line 75:** - Returning buyers' money matches on role across kinds: Zid Pay's terms (official page), Shopify's European and UK help page (stated), and Salla's agreement, which allows returning pending electronic payments to consumers for a breach of its tenth article (official page). Q3-ZD-P0012; Q3-SH-072; Q3-SA-P0083
- **section 2, line 82:** - **Business** (proposed): the legal entity behind one or more stores, with its **entity type** and its **registration place**, the place whose government documents it uses. These two choose each requirement set. The registration place comes from Salla's question for the country whose government documents the store uses (observed, Store 1, 8 October 2026) and WooPayments' country of registration; the entity types from Salla and Zid, whose requirements differ by entity type and country. Why: rule 1, since the place selects configuration rather than code, and rule 3. Q3-SA-085; Q3-WC-K0402; Q3-SA-056; Q3-ZD-K0239; Q3-ZD-K0240
- **section 2, line 84:** - Changing the registration place is a fresh verification with its own requirement set, not an edit, since WooPayments can't change it and Zid asks for the wallet at zero first. Why: rule 3. Q3-WC-011; Q3-ZD-K0230
- **section 2, line 86:** - **Capability** (proposed): a thing a seller may do that a requirement set can gate: open the store to buyers, take payments through one method or provider, receive payouts, withdraw a balance, sell a product type or category, join a sales channel or program, or use a financing or tax service. One capability can require another, as Shop requires Shopify Payments, Mahally a verified store, and Zid Financing Zid Pay. Why: rule 2, so a change in one provider's requirements changes only its capability. Q3-SH-077; Q3-SA-061; Q3-ZD-P0132
- **section 2, line 88:** - **Requirement** (proposed): one condition, with its kind, subject, setter, validity and check. Its kinds come from the platforms: information, a document, an identity check, a plan, an accepted agreement, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account age such as WooPayments' 7 days before a first payout, a match between subjects such as the payout account's holder and the verified name, not being a listed party, as under Shopify Payments' sanctions rule, and another capability being active. Validity follows rules such as Zid's commercial register valid two months from activation. Its subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-WC-P0038; Q3-SA-K1563; Q3-SH-K2268; Q3-ZD-013
- **section 2, line 91:** - **Submission** and **Review** (proposed): the seller gives information and documents inside Sharrwah and declares them true, as Salla's KYC schema requires; a review decides: pending, approved, rejected with reasons, or more needed. Each review has a checker, which is Sharrwah's team, a provider or an identity service, with its own attempt limits and timing, as Zid's team, Zid's gateway, and the daily attempts of Absher and Nafath show. Documents come only through Sharrwah, as Shopify accepts them only through its admin. Why: rule 2 for the checker, rule 3 for the data. Q3-SA-057; Q3-ZD-P0038; Q3-ZD-P0118; Q3-SA-008; Q3-ZD-K0262; Q3-SH-015
- **section 2, line 92:** - **Re-verification** (proposed): a met requirement is checked again when business details or the payout account change, at intervals, on request, or after a threshold; a duty to report changes within a set time is a per-place setting. While an update is reviewed, the met state holds and the store keeps taking orders and payments, as on Salla. Q3-SH-061; Q3-SH-066; Q3-SA-051; Q3-BC-020; Q3-ZD-078; Q3-SA-006
- **section 2, line 95:** - **Escalation** (proposed): a restriction can step up on a schedule (hold payouts, then pause charges, then return payments to buyers), with steps and days set per registration place, as Shopify's European and UK timeline and Zid Pay's 14 days show. Why: rule 1. Q3-SH-072; Q3-ZD-P0012
- **section 2, line 96:** - Holding payouts, blocking withdrawals and returning payments to buyers act on sellers' money. The design provides for them, and for gating payouts and a balance; any arrangement in which sellers' money is held through Sharrwah, by Sharrwah itself or by a payment company in an account opened through Sharrwah, goes live only by the founder's decision. Q3-SA-077; Q3-ZD-P0012; Q3-SH-P0085
- **section 2, line 99:** - **Product rule** (proposed): a rule on what may be sold, with its setter and its reach. It may bar a product for all of Sharrwah; bar it for one provider, blocking only that provider's capability; require a licence disclosed on the store with its details; require the registered activity to match the product; or require a plan for a product type. It takes Salla's selling policy, Shopify Payments' hemp rule and WooPayments' CBD rule, Salla's and Zid's licence clause, their activity match, and Salla's plan-limited product types. Why: rule 2, since each setter's list changes on its own. Q3-SA-054; Q3-SH-095; Q3-WC-K0417; Q3-SA-047; Q3-ZD-K0247; Q3-SA-058; Q3-ZD-003; Q3-SA-029
- **section 3, line 108:** - Payment providers, each with its own requirement set and approval: American Express on Shopify, Tabby on Salla, Tap on Zid, and the providers on BigCommerce. Q3-SH-057; Q3-SA-069; Q3-ZD-K0093; Q3-BC-P0048
- **section 3, line 110:** - Government services whose records a requirement may ask for: the Business Platform (منصة الأعمال), whose licence Salla keeps apart from its own verification, and SPL's national address, which Zid asks for to activate services such as payments. Q3-SA-037; Q3-ZD-039
- **section 3, line 118:** - Per product category: a provider's exclusions, such as hemp and CBD, and Zid Pay's assessment of digital products. Q3-SH-095; Q3-WC-K0417; Q3-ZD-K0070
- **section 3, line 128:** - Authorities and the law, as the platforms report them: licences on Zid, and the e-commerce law's obligations on Salla. These show what the platforms require of their sellers, not what any law requires of Sharrwah. Q3-ZD-023; Q3-SA-033
- **section 5, line 146:** - What unmet requirements do to money: holding payouts, blocking withdrawals, returning payments to buyers, and the days between, as Shopify, Zid and Salla show them; Salla's period was not in what was read. Keep open, as a money flow: a restriction type for each, with schedules per place, all off until decided. Settled by the founder's decision under the guard, Q5's proposal and providers' terms. Q3-SH-072; Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01
- **section 5, line 147:** - Which place selects a requirement set, and what moving it costs: the country of the documents (Salla), of registration (WooPayments), or of the business's location (Shopify). Yemen adds places below a country, where two areas set one requirement differently. Keep open: a registration place that can name an area within a country, kept apart from the store's selling places, and rules for moving it, such as Zid's zero balance first. Settled by the proposals for Q1 and Q6. Q3-SA-085; Q3-WC-K0402; Q3-SH-K1536; Q3-ZD-K0230; YA-150 (within thirty days of founding or licensing @ Houthis' area, as of 2026-10-10); YA-150 (within sixty days of starting its activity @ the unified Republic's area, as of 1991)
- **section 5, line 149:** - Which entity types a place admits, and what each gives, as Salla's freelance document is for Saudi citizens only. Keep open: entity types as a list per place. Settled by Q6 and the company decision on who may register. Q3-SA-014; Q3-ZD-K0239

## The cards

### Q3-ZD-K0070

**Cited at:** section 1, line 34; section 3, line 118

**Record** (`studies/proposals/records/Q3/zid/copied.tsv`):
- concern_id: ZD-C-009
- placement: decides
- structure: شروط وأحكام زد باي, Saudi Arabia (zid.sa/ar/legal/zidpay-terms-conditions-sa)
- identifier: المنتجات الرقمية
- statement: المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة
- scope: Zid Pay, Saudi Arabia
- cite_ids: ZD-S-0590

**Citation ZD-S-0590:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة
- title: Zid | Create your online store with modern retail services
- in context: …غير المعتمدة من الجهات المعنية في المملكة العربية السعودية. الحسابات المجهولة والمسجلة بأسماء وهمية. الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء. التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. ⟪المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة⟫ أو أي نشاط آخر لا يتوافق مع مزود الخدمة. طريقة الاستفادة من خدمات زد باي -تفعيل الخدمة: يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. يجب أن يكون نشاط التاجر صحيح ولا يخدم أي من النشاطات المحظورة. في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين. التاجر وحده مسؤول عن مطابقة المنتجات مع المنتجات الموجودة في المتجر، وعن ت…

### Q3-ZD-K0247

**Cited at:** section 1, line 37; section 2, line 99

**Record** (`studies/proposals/records/Q3/zid/copied.tsv`):
- concern_id: ZD-C-036
- placement: decides
- structure: الشروط والأحكام (zid.sa/ar/legal/terms-conditions; the Arabic version prevails)
- identifier: الترخيص
- statement: ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.
- cite_ids: ZD-S-0761

**Citation ZD-S-0761:** `https://zid.sa/ar/legal/terms-conditions/` | ضوابط المتجر الإلكتروني | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.
- title: Zid | Create your online store with modern retail services
- in context: … - السجل التجاري والرقم الضريبي أو وثيقة العمل الحر - ووسائل الاتصال الرسمية. ينبغي على كافة المتاجر والتجّار الالتزام بإيضاح الشروط والأحكام للمستهلك، وتوضيح الوسائل اللازمة لتلقي شكاوى المستهلك ومعالجتها، وسياسة الاستبدال والارجاع وكيفية ارجاع المبالغ -إن وجدت- وسياسة الخصوصية وحماية بيانات المستهلك. ينبغي على كافة المتاجر والتجّار تقديم فاتورة إلى المستهلك تبيّن تكاليف شراء تقديم الخدمة أو المنتج وأوصافه، وإجمالي السعر، وتاريخ التسليم ومكانه. ⟪ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.⟫ في حالة عدم الالتزام بأي مما ورد أعلاه فإن لزد الحق في اتخاذ أي من الإجراءات التالية والتي تشمل -على سبيل المثال لا الحصر-: التنبيه، أو إيقاف الخدمة وإغلاق المتجر، أو حجب التاجر من الوصول واستخدام الخدمات حسبما تراه مناسباً، وعلى أن زد غير مسؤولة قانوناً أو شرعاً عن هذا الإخلال الحاصل من قبل التاجر في مواجهة المستهلك، حيث إنها ليست طرفاً في العلاقة بين المستهلك والتاجر، ولكنها تقوم بذلك لدواعي تحسين جودة تجربة التاجر والمستهلك مع زد. الأخطاء وعد…

### Q3-ZD-023

**Cited at:** section 1, line 37; section 1, line 61; section 3, line 128

**Record** (`studies/proposals/records/Q3/zid/statements.tsv`):
- stmt_id: Q3-ZD-023
- bears_on: 1;2;4
- identifier: متطلبات تفعيل الدفع الالكتروني  للشركات > التراخيص ( إن تطلب الأمر )
- statement: بعض الأنشطة التجارية تستلزم وجود تراخيص من الجهات المعنية ويحدد ذلك بعد مراجعة البيانات(مثال: بيع الكتب ،يتم استخراج الترخيص من وزارة الإعلام).
- cite_ids: Q3-ZD-C025
- from: held

**Citation Q3-ZD-C025:** `https://help.zid.sa/payment-requirements/` | متطلبات تفعيل الدفع الالكتروني  للشركات > التراخيص ( إن تطلب الأمر ) | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T04:53:19Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/066-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T10:50:42Z, captured
- quote: بعض الأنشطة التجارية تستلزم وجود تراخيص من الجهات المعنية ويحدد ذلك بعد مراجعة البيانات(مثال: بيع الكتب ،يتم استخراج الترخيص من وزارة الإعلام).
- title: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ا…
- in context: … مراعاة أن يكون اسم المستفيد في الشهادة البنكية باللغة الانجليزية . للاطلاع على طريقة استخراج الشهادة البنكية بكل سهولة : هنا شهادة العنوان الوطني: عند إرفاق شهادة العنوان الوطني يجب مراعاة التالي: أن يكون اسم المستفيد مطابق للسجل التجاري. أن تكون جميع البيانات واضحة. ترخيص الاستثمار (للشركات الأجنبية): عند ارفاق ترخيص الاستثمار يجب مراعاة التالي: أن يكون ترخيص الاستثمار ساري المدة. أن يكون جميع بيانات الترخيص واضحة. التراخيص ( إن تطلب الأمر ) : ⟪بعض الأنشطة التجارية تستلزم وجود تراخيص من الجهات المعنية ويحدد ذلك بعد مراجعة البيانات(مثال: بيع الكتب ،يتم استخراج الترخيص من وزارة الإعلام).⟫ ملاحظة : يجب التأكد من إرفاق المستندات التالية كاملة وصحيحة و بجودة عالية. سوف تتعلم: متطلبات تفعيل الدفع الالكتروني للسعودية متطلبات تفعيل الدفع الالكتروني للكويت متطلبات تفعيل الدفع الالكتروني للمؤسسات متطلبات تفعيل الدفع الالكتروني للشركات التقييمات والمراجعات 5.0 5.0 من أصل 5 نجوم (بناءً على 7 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم متجر البوليصات ( لوحة ال…

### Q3-ZD-003

**Cited at:** section 1, line 39; section 2, line 99

**Record** (`studies/proposals/records/Q3/zid/statements.tsv`):
- stmt_id: Q3-ZD-003
- bears_on: 1;2;4
- identifier: متطلبات تفعيل الدفع الالكتروني للسعودية > الوثيقة
- statement: أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر
- scope: السعودية; الأفراد
- cite_ids: Q3-ZD-C003
- from: held

**Citation Q3-ZD-C003:** `https://help.zid.sa/payment-requirements/` | متطلبات تفعيل الدفع الالكتروني للسعودية > الوثيقة | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T04:53:19Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/066-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T10:50:42Z, captured
- quote: أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر
- title: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ا…
- in context: …لكتروني ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 6, 2026 لإتاحة خيار الدفع الإلكتروني في المتجر يتطلب تزويد بوابة الدفع بمتطلبات التفعيل حسب الكيان التجاري (فرد - شركة - مؤسسة) ليتم اعتماد الحساب لدى بوابة الدفع. متطلبات تفعيل الدفع الالكتروني للسعودية : الكيانات المدعومة : فرد. مؤسسة. شركة. متطلبات الأفراد : وثيقة عمل حر. الهوية الوطنية. حساب بنكي تجاري. شهادة العنوان الوطني. الوثيقة : عند إرفاق الوثيقة يجب مراعاة التالي: ⟪أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر⟫ ( مثال : في حال بيع التاجر لمنتجات العطور يجب أن تكون الوثيقة "صناعة العطور" أو "إدارة المبيعات" ) مراعاة أهمية تاريخ صلاحية الوثيقة (يجب أن يكون التاريخ ساري) ولاستخراج وثيقة عمل حر يرجى زيارة منصة العمل الحر الهوية الوطنية : عند توفر الهوية الوطنية يجب مراعاة التالي: تاريخ صلاحية الهوية المرفقة (يجب أن تكون الهوية سارية) حامل الهوية مطابق لحامل الوثيقة. الحساب البنكي والشهادة البنكية : عند ارفاق الحساب البنكي و الشهادة البنكية يجب مراعاة التال…

### Q3-ZD-P0132

**Cited at:** section 1, line 45; section 2, line 86

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-131
- bullet: e
- placement: decides
- identifier: عن تمويل زد ( لوحة التحكم الجديدة ) > متطلبات التقديم لتمويل زد
- statement: متطلبات التقديم لتمويل زد : الدولة : متاح لتجار المملكة العربية السعودية فقط. الكيان التجاري: شركة أو مؤسسة فقط. بوابة الدفع: تفعيل واعتماد زد باي. صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر
- conditions: S01-ZD-094;S01-ZD-095;S01-ZD-096
- cite_ids: S01-ZD-C308;S01-ZD-C309;S01-ZD-C310;S01-ZD-C311;S01-ZD-C312
- from: index:ZD-C-023:ZD-S-0693

**Citation S01-ZD-C308:** `https://help.zid.sa/about-zid-financing/` | متطلبات التقديم | 2026-08-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/081-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T04:52:13Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/046-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T10:50:22Z, captured
- quote: الدولة : متاح لتجار المملكة العربية السعودية فقط.
- title: زد - مركز المساعدة - عن تمويل زد ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - عن تمويل زد ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة تمويل زد تمويل زد عن تمويل زد ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدا…
- in context: …د منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال تمويل زد عن تمويل زد ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 13, 2026 تمويل زد هو حل متكامل لتنمية متجرك الإلكتروني عن طريق رحلة تفعيل سلسة مع خطة سداد مرنة مؤتمتة. مميزات تمويل زد : تقديم المتطلبات الأولية تمويل يصل إلى 10 مليون هامش ربح سنوي من 10% إلى 25% خطط سداد مرنة من 5 إلى 36 شهرًا. متطلبات التقديم لتمويل زد : ⟪الدولة : متاح لتجار المملكة العربية السعودية فقط.⟫ الكيان التجاري: شركة أو مؤسسة فقط. بوابة الدفع: تفعيل واعتماد زد باي. صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر شروط التقديم لتمويل زد : عمر النشاط التجاري: - إذا كان عمر المتجر 3 أشهر أو أكثر وأقل من 6 أشهر: متوسط المبيعات الشهرية خلال آخر 3 أشهر يجب أن يكون 40,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 6 أشهر أو أكثر وأقل من 12 شهرًا: متوسط المبيعات الشهرية خلال آخر 6 أشهر يجب أن يكون 20,000 ريال سعودي أو أكثر. -إ…

**Citation S01-ZD-C309:** `https://help.zid.sa/about-zid-financing/` | متطلبات التقديم لتمويل زد | 2026-08-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/081-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T04:52:13Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/046-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T10:50:22Z, captured
- quote: متطلبات التقديم لتمويل زد :
- title: زد - مركز المساعدة - عن تمويل زد ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - عن تمويل زد ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة تمويل زد تمويل زد عن تمويل زد ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدا…
- in context: …منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال تمويل زد عن تمويل زد ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 13, 2026 تمويل زد هو حل متكامل لتنمية متجرك الإلكتروني عن طريق رحلة تفعيل سلسة مع خطة سداد مرنة مؤتمتة. مميزات تمويل زد : تقديم المتطلبات الأولية تمويل يصل إلى 10 مليون هامش ربح سنوي من 10% إلى 25% خطط سداد مرنة من 5 إلى 36 شهرًا. ⟪متطلبات التقديم لتمويل زد :⟫ الدولة : متاح لتجار المملكة العربية السعودية فقط. الكيان التجاري: شركة أو مؤسسة فقط. بوابة الدفع: تفعيل واعتماد زد باي. صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر شروط التقديم لتمويل زد : عمر النشاط التجاري: - إذا كان عمر المتجر 3 أشهر أو أكثر وأقل من 6 أشهر: متوسط المبيعات الشهرية خلال آخر 3 أشهر يجب أن يكون 40,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 6 أشهر أو أكثر وأقل من 12 شهرًا: متوسط المبيعات الشهرية خلال آخ…

**Citation S01-ZD-C310:** `https://help.zid.sa/about-zid-financing/` | متطلبات التقديم لتمويل زد | 2026-08-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/081-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T04:52:13Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/046-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T10:50:22Z, captured
- quote: الكيان التجاري: شركة أو مؤسسة فقط.
- title, opening and note boxes: as for this source's citation above
- in context: …بيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال تمويل زد عن تمويل زد ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 13, 2026 تمويل زد هو حل متكامل لتنمية متجرك الإلكتروني عن طريق رحلة تفعيل سلسة مع خطة سداد مرنة مؤتمتة. مميزات تمويل زد : تقديم المتطلبات الأولية تمويل يصل إلى 10 مليون هامش ربح سنوي من 10% إلى 25% خطط سداد مرنة من 5 إلى 36 شهرًا. متطلبات التقديم لتمويل زد : الدولة : متاح لتجار المملكة العربية السعودية فقط. ⟪الكيان التجاري: شركة أو مؤسسة فقط.⟫ بوابة الدفع: تفعيل واعتماد زد باي. صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر شروط التقديم لتمويل زد : عمر النشاط التجاري: - إذا كان عمر المتجر 3 أشهر أو أكثر وأقل من 6 أشهر: متوسط المبيعات الشهرية خلال آخر 3 أشهر يجب أن يكون 40,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 6 أشهر أو أكثر وأقل من 12 شهرًا: متوسط المبيعات الشهرية خلال آخر 6 أشهر يجب أن يكون 20,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 12 شهرًا أو أكثر:…

**Citation S01-ZD-C311:** `https://help.zid.sa/about-zid-financing/` | متطلبات التقديم | 2026-08-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/081-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T04:52:13Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/046-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T10:50:22Z, captured
- quote: بوابة الدفع: تفعيل واعتماد زد باي.
- title, opening and note boxes: as for this source's citation above
- in context: …الثيمات تطبيق الجوال تمويل زد عن تمويل زد ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 13, 2026 تمويل زد هو حل متكامل لتنمية متجرك الإلكتروني عن طريق رحلة تفعيل سلسة مع خطة سداد مرنة مؤتمتة. مميزات تمويل زد : تقديم المتطلبات الأولية تمويل يصل إلى 10 مليون هامش ربح سنوي من 10% إلى 25% خطط سداد مرنة من 5 إلى 36 شهرًا. متطلبات التقديم لتمويل زد : الدولة : متاح لتجار المملكة العربية السعودية فقط. الكيان التجاري: شركة أو مؤسسة فقط. ⟪بوابة الدفع: تفعيل واعتماد زد باي.⟫ صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر شروط التقديم لتمويل زد : عمر النشاط التجاري: - إذا كان عمر المتجر 3 أشهر أو أكثر وأقل من 6 أشهر: متوسط المبيعات الشهرية خلال آخر 3 أشهر يجب أن يكون 40,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 6 أشهر أو أكثر وأقل من 12 شهرًا: متوسط المبيعات الشهرية خلال آخر 6 أشهر يجب أن يكون 20,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 12 شهرًا أو أكثر: متوسط المبيعات الشهرية خلال آخر 12…

**Citation S01-ZD-C312:** `https://help.zid.sa/about-zid-financing/` | متطلبات التقديم لتمويل زد | 2026-08-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/081-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T04:52:13Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/046-help.zid.sa/text.txt` (4437 bytes), fetched 2026-10-12T10:50:22Z, captured
- quote: صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر
- title, opening and note boxes: as for this source's citation above
- in context: …ويل زد ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 13, 2026 تمويل زد هو حل متكامل لتنمية متجرك الإلكتروني عن طريق رحلة تفعيل سلسة مع خطة سداد مرنة مؤتمتة. مميزات تمويل زد : تقديم المتطلبات الأولية تمويل يصل إلى 10 مليون هامش ربح سنوي من 10% إلى 25% خطط سداد مرنة من 5 إلى 36 شهرًا. متطلبات التقديم لتمويل زد : الدولة : متاح لتجار المملكة العربية السعودية فقط. الكيان التجاري: شركة أو مؤسسة فقط. بوابة الدفع: تفعيل واعتماد زد باي. ⟪صلاحية السجل التجاري يجب أن تكون صلاحية السجل التجاري لا تقل عن 3 أشهر⟫ شروط التقديم لتمويل زد : عمر النشاط التجاري: - إذا كان عمر المتجر 3 أشهر أو أكثر وأقل من 6 أشهر: متوسط المبيعات الشهرية خلال آخر 3 أشهر يجب أن يكون 40,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 6 أشهر أو أكثر وأقل من 12 شهرًا: متوسط المبيعات الشهرية خلال آخر 6 أشهر يجب أن يكون 20,000 ريال سعودي أو أكثر. -إذا كان عمر المتجر 12 شهرًا أو أكثر: متوسط المبيعات الشهرية خلال آخر 12 شهرًا يجب أن يكون 13,300 ريال سعودي أو أكثر ملاحظه: تمويل زد متاح لجمي…

### Q3-ZD-K0230

**Cited at:** section 1, line 46; section 2, line 84; section 5, line 147

**The same record as Q1-ZD-K0230,** whose card is in `Q1-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر إلى دولة أخرى، يشترط تصفير رصيد المحفظة أولاً
- scope: 

### Q3-ZD-K0239

**Cited at:** section 1, line 51; section 2, line 82; section 5, line 149

**Record** (`studies/proposals/records/Q3/zid/copied.tsv`):
- concern_id: ZD-C-035
- placement: decides
- structure: help.zid.sa article: بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )
- identifier: نوع النشاط
- statement: اختر تفاصيل النشاط، ثم حدد نوع النشاط (فرد، مؤسسة، شركة، جمعية خيرية) وأكمل البيانات المطلوبة ثم اضغط حفظ.
- scope: السعودية
- cite_ids: ZD-S-0753

**Citation ZD-S-0753:** `https://help.zid.sa/store-info-ksa/` | تفاصيل النشاط التجاري | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/158-help.zid.sa/text.txt` (10849 bytes), fetched 2026-10-12T04:53:30Z, captured
- quote: اختر تفاصيل النشاط، ثم حدد نوع النشاط (فرد، مؤسسة، شركة، جمعية خيرية) وأكمل البيانات المطلوبة ثم اضغط حفظ.
- title: زد - مركز المساعدة - بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة المتجر الإعدادات بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ال…
- in context: …اطك التجاري. ملاحظة: البريد الإلكتروني و رقم الهاتف و رقم السجل التجاري ستظهر للعملاء في أسفل صفحة المتجر. تفاصيل النشاط التجاري : في تفاصيل النشاط لابد من اختيار نوع النشاط التجاري وارفاق المستندات الرسمية ، تختلف المتطلبات باختلاف نوع النشاط والدولة تفاصيل النشاط التجاري : في تفاصيل النشاط لابد من اختيار نوع النشاط التجاري وارفاق المستندات الرسمية حسب دولتك. ملاحظة : تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة. السعودية : ⟪اختر تفاصيل النشاط، ثم حدد نوع النشاط (فرد، مؤسسة، شركة، جمعية خيرية) وأكمل البيانات المطلوبة ثم اضغط حفظ.⟫ فرد : الاسم التجاري : الاسم التجاري للنشاط أو المتجر . رقم الشهادة الضريبية : أضف رقم الشهادة الضريبية في حال استخراج الشهادة. المستندات الرسمية : ارفق المستندات الرسمية كما هو ظاهر ، لكل نوع نشاط تجاري مستندات مختلفة في حال كان مدير المتجر هو المالك قم بوضع علامة في حال لم يكون مدير المتجر هو المالك قم بادخال البيانات التالية : اسم المالك : اسم مالك النشاط الأصلي. هاتف المالك : رقم التواصل مع المالك. البريد الإلكتروني للمالك. رقم الهوية الوطنية…

### Q3-ZD-P0047

**Cited at:** section 1, line 60

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-046
- bullet: b
- placement: decides
- identifier: اجتياز التحقق من نفاذ > ملاحظة
- statement: يكون طلب التحقق باسم مزود الخدمة.
- cite_ids: S01-ZD-C086
- from: index:ZD-C-009:ZD-S-0591

**Citation S01-ZD-C086:** `https://help.zid.sa/nafath_verification/` | ملاحظة | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/140-help.zid.sa/text.txt` (4982 bytes), fetched 2026-10-12T04:53:12Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/064-help.zid.sa/text.txt` (4982 bytes), fetched 2026-10-12T10:50:40Z, captured
- quote: يكون طلب التحقق باسم مزود الخدمة.
- title: زد - مركز المساعدة - اجتياز التحقق من نفاذ
- the page opens: زد - مركز المساعدة - اجتياز التحقق من نفاذ menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الرئيسية الرئيسية اجتياز التحقق من نفاذ عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون --> إدارة المخزون…
- in context: … لاجتياز التحقق من نفاذ يرجى إتباع الخطوات التالية : قم بالضغط على أيقونة تأكيد تفعيل زد باي في أخر خطوة من التفعيل و الموافقة على الشروط والأحكام. سيتم الانتقال إلى خطوة التحقق من نفاذ. ملاحظة 💡 : المدة المتاحة للتحقق في الجلسة الواحدة هي 3 دقائق. عدد محاولات التحقق المتاحة خلال اليوم الواحد هي 3 محاولات. طلب التحقق يصل لمالك المتجر برقم الهوية كما هو موضح في صفحة التحقق ، في حال الرغبة بتحديث رقم الهوية يرجى التواصل عن طريق المحادثات المباشرة. ⟪يكون طلب التحقق باسم مزود الخدمة.⟫ يتم تلقائياً إرسال إشعار عن طريق تطبيق نفاذ لمالك المتجر أو يمكن للمالك الدخول على تطبيق نفاذ و ظهور طلب تحقق جديد. قم بإدخال رمز الأمان لتطبيق نفاذ. ثم قم بالانتقال إلى قسم الطلبات ثم قم بالضغط على أيقونة قبول التحقق. تأكيد قبول التحقق بالضغط على أيقونة إكمال. قم باختيار الرقم المطابق للرقم الظاهر في لوحة التحكم في خطوة نفاذ. إعادة إدخال رمز الأمان. إتمام التحقق بمسح الوجه (Biometric Verification). ستظهر لك رسالة تم قبول الطلب بنجاح. قم بالعودة…

### Q3-ZD-P0038

**Cited at:** section 1, line 65; section 2, line 91

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-037
- bullet: c;end-payout
- placement: decides
- identifier: تفعيل الدفع الالكتروني > مراجعة المعلومات واستقبال عمليات الدفع
- statement: بعد تفعيلك للمدفوعات سيقوم فريقنا بمراجعة المعلومات المرفوعة والتحقق من صحتها لتتمكن من استقبال العمليات و المبالغ المحصلة في حسابك البنكي ،و سيصلك إشعار عن طريق الايميل فور التحقق من قِبل الفريق.
- cite_ids: S01-ZD-C070
- from: new

**Citation S01-ZD-C070:** `https://help.zid.sa/activate-online-payments/` | مراجعة المعلومات واستقبال عمليات الدفع | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: بعد تفعيلك للمدفوعات سيقوم فريقنا بمراجعة المعلومات المرفوعة والتحقق من صحتها لتتمكن من استقبال العمليات و المبالغ المحصلة في حسابك البنكي ،و سيصلك إشعار عن طريق الايميل فور التحقق من قِبل الفريق.
- title: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: … وبعد ذلك ، قم بالضغط على ايقونة التالي الخطوة الثالثة والأخيرة وهي تفعيل الشبكات ،اختر شبكات الدفع التي ترغب بتفعيلها في متجرك ، وبإمكانك التحكم بجميع الشبكات لاحقاً. مع أهمية الموافقة على الشروط والاحكام بعد ذلك ، قم بالضغط على ايقونة تفعيل ملاحظة : يمكنك الوصول لاحقاً على الشروط والأحكام عن طريق صفحة إدارة المدفوعات بعد التفعيل. في حال لديك بوابة دفع أخرى مفعلة سيتم تعطيلها وتفعيل المدفوعات بشكل مؤتمت. مراجعة المعلومات واستقبال عمليات الدفع : ⟪بعد تفعيلك للمدفوعات سيقوم فريقنا بمراجعة المعلومات المرفوعة والتحقق من صحتها لتتمكن من استقبال العمليات و المبالغ المحصلة في حسابك البنكي ،و سيصلك إشعار عن طريق الايميل فور التحقق من قِبل الفريق.⟫ في حالة القبول: سيتم إيداع المبالغ المحصلة إلى حسابك البنكي في أقرب يوم تحصيل خلال الأيام التالية ( الأحد ، الاثنين، الثلاثاء ، الاربعاء، الخميس ). عليك اتباع الخطوات التالية في حالة الرفض : تصحيح معلومات الحساب في إعدادات المتجر. إعادة تقديم متطلبات التفعيل إيداع المبالغ: يتم إيداع المبالغ المحصلة إلى حسابك البنكي بعد اعتماد المعلومات بشكل يومي من الأحد إلى الخميس. ستظهر جميع الشبكات المفعلة في: أسفل المتجر. صفحة خيارات الدفع والتوصيل. خطوات إت…

### Q3-ZD-K0262

**Cited at:** section 1, line 66; section 2, line 91

**Record** (`studies/proposals/records/Q3/zid/copied.tsv`):
- concern_id: ZD-C-038
- placement: decides
- structure: help.zid.sa article: اجتياز التحقق من نفاذ
- identifier: عدد المحاولات
- statement: عدد محاولات التحقق المتاحة خلال اليوم الواحد هي 3 محاولات.
- cite_ids: ZD-S-0776

**Citation ZD-S-0776:** `https://help.zid.sa/nafath_verification/` | ملاحظة | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/140-help.zid.sa/text.txt` (4982 bytes), fetched 2026-10-12T04:53:12Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/064-help.zid.sa/text.txt` (4982 bytes), fetched 2026-10-12T10:50:40Z, captured
- quote: عدد محاولات التحقق المتاحة خلال اليوم الواحد هي 3 محاولات.
- title: زد - مركز المساعدة - اجتياز التحقق من نفاذ
- the page opens: زد - مركز المساعدة - اجتياز التحقق من نفاذ menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الرئيسية الرئيسية اجتياز التحقق من نفاذ عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون --> إدارة المخزون…
- in context: …تجر اجتياز التحقق من نفاذ. خطوات اجتياز تحقق نفاذ قبل البدء بخطوات التحقق يرجى التأكد من: تحميل تطبيق نفاذ و تسجيل الدخول. التأكد من صحة رقم الهوية الوطنية لمالك النشاط المسجل في إعدادات بيانات المتجر. لاجتياز التحقق من نفاذ يرجى إتباع الخطوات التالية : قم بالضغط على أيقونة تأكيد تفعيل زد باي في أخر خطوة من التفعيل و الموافقة على الشروط والأحكام. سيتم الانتقال إلى خطوة التحقق من نفاذ. ملاحظة 💡 : المدة المتاحة للتحقق في الجلسة الواحدة هي 3 دقائق. ⟪عدد محاولات التحقق المتاحة خلال اليوم الواحد هي 3 محاولات.⟫ طلب التحقق يصل لمالك المتجر برقم الهوية كما هو موضح في صفحة التحقق ، في حال الرغبة بتحديث رقم الهوية يرجى التواصل عن طريق المحادثات المباشرة. يكون طلب التحقق باسم مزود الخدمة. يتم تلقائياً إرسال إشعار عن طريق تطبيق نفاذ لمالك المتجر أو يمكن للمالك الدخول على تطبيق نفاذ و ظهور طلب تحقق جديد. قم بإدخال رمز الأمان لتطبيق نفاذ. ثم قم بالانتقال إلى قسم الطلبات ثم قم بالضغط على أيقونة قبول التحقق. تأكيد قبول التحقق بالضغط على أيقونة إكمال. قم باختيار …

### Q3-ZD-078

**Cited at:** section 1, line 67; section 2, line 92

**Record** (`studies/proposals/records/Q3/zid/statements.tsv`):
- stmt_id: Q3-ZD-078
- bears_on: 4
- identifier: شروط وأحكام زد باي > حدود المسؤولية
- statement: التاجر مسؤول عن إشعار وإعلام زد باي بأي تغيير في العمليات أو الإدارة خلال أسبوع من تاريخه. مثل هذا التغيير قد يتضمن تغيير في الأنشطة، وتغيير في العنوان أو معلومات التواصل، وتغير في هيكل الملكية أو أي تغييرات أخرى ذات صلة. عدم إعلام زد باي بهذه التغييرات قد يؤدى إلى ايقاف الحساب وانقطاع خدمة زد باي.
- cite_ids: Q3-ZD-C096;Q3-ZD-C097
- from: held

**Citation Q3-ZD-C096:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | حدود المسؤولية | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: التاجر مسؤول عن إشعار وإعلام زد باي بأي تغيير في العمليات أو الإدارة خلال أسبوع من تاريخه. مثل هذا التغيير قد يتضمن تغيير في الأنشطة، وتغيير في العنوان أو معلومات التواصل، وتغير في هيكل الملكية أو أي تغييرات أخرى ذات صلة.
- title: Zid | Create your online store with modern retail services
- in context: …والحصول على اذونات الاستلام بما أنها ستكون مطلوبة للتحقق من عمليات معينة طبقا لمتطلبات إجراءات تقييم المخاطر الخاصة بزد باي. ولابد أن يحرص على الحصول دائما على أدلة داعمة لعمليات الدفع الخاصة بحسابه . الموافقة على أن زد باي قد تشير إلى التاجر أو تستخدم الشعار الخاص بك عند تقديم سابقة أعمالها للقطاع العام أو الخاص. يجب على المستخدمين الذين لديهم حسابات معلقة أو منتهية الامتناع عن استخدام العلامة التجارية لزد باي في أي من أنشطتهم العامة او الخاصة. ⟪التاجر مسؤول عن إشعار وإعلام زد باي بأي تغيير في العمليات أو الإدارة خلال أسبوع من تاريخه. مثل هذا التغيير قد يتضمن تغيير في الأنشطة، وتغيير في العنوان أو معلومات التواصل، وتغير في هيكل الملكية أو أي تغييرات أخرى ذات صلة.⟫ عدم إعلام زد باي بهذه التغييرات قد يؤدى إلى ايقاف الحساب وانقطاع خدمة زد باي. يقر التاجر ويوافق على أن خيارات الدفع (شبكات الدفع) خاضعة لشروط وأحكام مقدم الخدمة. يحق لزد باي بناءً على توصية مزودي الخدمة القيام ب -على سبيل المثال لا الحصر- تعليق الخدمة مؤقتًا، احتجاز الأموال في حال الاشتباه بعدد من عمليات الاحتيال إلى حين ظهور نتيجة التحقيق. يحق لزد باي بناءً على توصية مزودي الخدمة القيام ب -على سبيل المثال لا الحصر- تعليق الخدمة مؤقتًا، احتجاز ب…

**Citation Q3-ZD-C097:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | حدود المسؤولية | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: عدم إعلام زد باي بهذه التغييرات قد يؤدى إلى ايقاف الحساب وانقطاع خدمة زد باي.
- title, opening and note boxes: as for this source's citation above
- in context: …ي قد تشير إلى التاجر أو تستخدم الشعار الخاص بك عند تقديم سابقة أعمالها للقطاع العام أو الخاص. يجب على المستخدمين الذين لديهم حسابات معلقة أو منتهية الامتناع عن استخدام العلامة التجارية لزد باي في أي من أنشطتهم العامة او الخاصة. التاجر مسؤول عن إشعار وإعلام زد باي بأي تغيير في العمليات أو الإدارة خلال أسبوع من تاريخه. مثل هذا التغيير قد يتضمن تغيير في الأنشطة، وتغيير في العنوان أو معلومات التواصل، وتغير في هيكل الملكية أو أي تغييرات أخرى ذات صلة. ⟪عدم إعلام زد باي بهذه التغييرات قد يؤدى إلى ايقاف الحساب وانقطاع خدمة زد باي.⟫ يقر التاجر ويوافق على أن خيارات الدفع (شبكات الدفع) خاضعة لشروط وأحكام مقدم الخدمة. يحق لزد باي بناءً على توصية مزودي الخدمة القيام ب -على سبيل المثال لا الحصر- تعليق الخدمة مؤقتًا، احتجاز الأموال في حال الاشتباه بعدد من عمليات الاحتيال إلى حين ظهور نتيجة التحقيق. يحق لزد باي بناءً على توصية مزودي الخدمة القيام ب -على سبيل المثال لا الحصر- تعليق الخدمة مؤقتًا، احتجاز بعض أو كل الأموال، تمديد فترة احتجاز الأموال، أو تعليق الخدمة في حال وجود تكرار…

### Q3-ZD-P0012

**Cited at:** section 1, line 74; section 1, line 75; section 2, line 95; section 2, line 96; section 5, line 146

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-011
- bullet: c
- placement: decides
- identifier: شروط وأحكام زد باي > طريقة الاستفادة من خدمات زد باي > تفعيل الخدمة
- statement: في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين.
- scope: السعودية; الكويت
- cite_ids: S01-ZD-C017;S01-ZD-C018
- from: new

**Citation S01-ZD-C017:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | طريقة الاستفادة من خدمات زد باي، تفعيل الخدمة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين.
- title: Zid | Create your online store with modern retail services
- in context: …ائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة أو أي نشاط آخر لا يتوافق مع مزود الخدمة. طريقة الاستفادة من خدمات زد باي -تفعيل الخدمة: يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. يجب أن يكون نشاط التاجر صحيح ولا يخدم أي من النشاطات المحظورة. ⟪في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين.⟫ التاجر وحده مسؤول عن مطابقة المنتجات مع المنتجات الموجودة في المتجر، وعن توصيلها للعميل النهائي. عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر. -رسوم العمليات: رسوم زد باي تعتمد على حسب باقتك المختارة في متجر زد، فإن كانت باقتك الأساسية تُفرض عليك رسوم زد باي للباقة الأساسية وإن كانت باقة النمو تُفرض عليك رسوم زد باي لباقة النمو. يتم فرض رسوم كنسبة مقتطعة من العمليات الناجحة. تحديد سقف أعلى بقيمة ٢٠٠ ريال لنسبة شبكة الدفع مدى (غير …

**Citation S01-ZD-C018:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | طريقة الاستفادة من خدمات زد باي، تفعيل الخدمة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين.
- title: Zid | Create your online store with modern retail services
- in context: …الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة أو أي نشاط آخر لا يتوافق مع مزود الخدمة. طريقة الاستفادة من خدمات زد باي -تفعيل الخدمة: يجب إرفاق صورة الهوية الوطنية من الخلف والامام للاستفادة من خدمة زد باي. يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. يجب أن يكون نشاط التاجر صحيح ولا يخدم أي من النشاطات المحظورة. ⟪في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين.⟫ التاجر وحده مسؤول عن مطابقة المنتجات مع المنتجات الموجودة في المتجر، وعن توصيلها للعميل النهائي. عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر. -رسوم العمليات: رسوم زد باي تعتمد على حسب باقتك المختارة في متجر زد، فإن كانت باقتك الأساسية تُفرض عليك رسوم زد باي للباقة الأساسية وإن كانت باقة النمو تُفرض عليك رسوم زد باي لباقة النمو، وفي حال كانت باقتك الباقة الاحترافية ستفرض عليك رسوم الباقة الاحترافية. يتم فرض رسوم كنسبة مقتطعة من ال…

### Q3-ZD-013

**Cited at:** section 2, line 88

**Record** (`studies/proposals/records/Q3/zid/statements.tsv`):
- stmt_id: Q3-ZD-013
- bears_on: 1;2;4
- identifier: متطلبات تفعيل الدفع الالكتروني للمؤسسات > السجل التجاري
- statement: أن يكون نشاط السجل التجاري مطابقاً للمنتجات التي يتم بيعها من خلال المتجر ( في حال وجود منتجات غير مطابقة لنشاط السجل يجب إضافة أنشطة فرعية للسجل التجاري بشكل مباشر من خلال موقع وزارة التجارة). أن يكون السجل التجاري ساري المدة مع مراعاة  أن لا تقل الصلاحية عن شهرين من تاريخ التفعيل و يمكن تجديد السجل التجاري بكل سهولة من خلال موقع وزارة التجارة الكترونياً.
- scope: المؤسسات
- cite_ids: Q3-ZD-C013;Q3-ZD-C014
- from: held

**Citation Q3-ZD-C013:** `https://help.zid.sa/payment-requirements/` | متطلبات تفعيل الدفع الالكتروني للمؤسسات > السجل التجاري | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T04:53:19Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/066-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T10:50:42Z, captured
- quote: أن يكون نشاط السجل التجاري مطابقاً للمنتجات التي يتم بيعها من خلال المتجر ( في حال وجود منتجات غير مطابقة لنشاط السجل يجب إضافة أنشطة فرعية للسجل التجاري بشكل مباشر من خلال موقع وزارة التجارة).
- title: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ا…
- in context: …لبطاقة المدنية من الجهتين الترخيص التجاري اعتماد التوقيع البيانات البنكية الخاصة بالشركة في حال كنت ترغب بتفعيل المدفوعات ك شركة تحتاج إلى: الترخيص التجاري اعتماد التوقيع البطاقات المدنية من الجهتين لجميع الشركاء والمدراء عقد التأسيس البيانات البنكية الخاصة بالشركة متطلبات تفعيل الدفع الالكتروني للمؤسسات: السجل التجاري. الهوية الوطنية. حساب بنكي تجاري. شهادة العنوان الوطني. السجل التجاري : يجب إرفاق السجل التجاري الخاص بالمؤسسة مع مراعاة التالي: ⟪أن يكون نشاط السجل التجاري مطابقاً للمنتجات التي يتم بيعها من خلال المتجر ( في حال وجود منتجات غير مطابقة لنشاط السجل يجب إضافة أنشطة فرعية للسجل التجاري بشكل مباشر من خلال موقع وزارة التجارة).⟫ أن يكون السجل التجاري ساري المدة مع مراعاة أن لا تقل الصلاحية عن شهرين من تاريخ التفعيل و يمكن تجديد السجل التجاري بكل سهولة من خلال موقع وزارة التجارة الكترونياً. الهوية الوطنية : يجب توفير الهوية الوطنية مع مراعاة التالي: تاريخ صلاحية الهوية المرفقة (يجب أن تكون الهوية سارية). حامل الهوية مطابق لمالك السجل التجاري. الحساب البنكي و الشهادة البنكية : يجب اختيار حساب بنكي تجاري. يجب أن يكون اسم المستفيد للحساب البنكي مطابق لاسم المنشأة في السجل ا…

**Citation Q3-ZD-C014:** `https://help.zid.sa/payment-requirements/` | متطلبات تفعيل الدفع الالكتروني للمؤسسات > السجل التجاري | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T04:53:19Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/066-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T10:50:42Z, captured
- quote: أن يكون السجل التجاري ساري المدة مع مراعاة  أن لا تقل الصلاحية عن شهرين من تاريخ التفعيل و يمكن تجديد السجل التجاري بكل سهولة من خلال موقع وزارة التجارة الكترونياً.
- title, opening and note boxes: as for this source's citation above
- in context: …هتين لجميع الشركاء والمدراء عقد التأسيس البيانات البنكية الخاصة بالشركة متطلبات تفعيل الدفع الالكتروني للمؤسسات: السجل التجاري. الهوية الوطنية. حساب بنكي تجاري. شهادة العنوان الوطني. السجل التجاري : يجب إرفاق السجل التجاري الخاص بالمؤسسة مع مراعاة التالي: أن يكون نشاط السجل التجاري مطابقاً للمنتجات التي يتم بيعها من خلال المتجر ( في حال وجود منتجات غير مطابقة لنشاط السجل يجب إضافة أنشطة فرعية للسجل التجاري بشكل مباشر من خلال موقع وزارة التجارة). ⟪أن يكون السجل التجاري ساري المدة مع مراعاة أن لا تقل الصلاحية عن شهرين من تاريخ التفعيل و يمكن تجديد السجل التجاري بكل سهولة من خلال موقع وزارة التجارة الكترونياً.⟫ الهوية الوطنية : يجب توفير الهوية الوطنية مع مراعاة التالي: تاريخ صلاحية الهوية المرفقة (يجب أن تكون الهوية سارية). حامل الهوية مطابق لمالك السجل التجاري. الحساب البنكي و الشهادة البنكية : يجب اختيار حساب بنكي تجاري. يجب أن يكون اسم المستفيد للحساب البنكي مطابق لاسم المنشأة في السجل التجاري. يجب إرفاق الشهادة البنكية مع مراعاة أن يكون اسم المستفيد في الشهادة البنكية باللغة الانجليزي. شهادة العنوان الوطني: عند إرفاق شهادة العنوان الوطني يجب مراعا…

### Q3-ZD-K0093

**Cited at:** section 3, line 108

**Record** (`studies/proposals/records/Q3/zid/copied.tsv`):
- concern_id: ZD-C-011
- placement: boundary
- structure: help.zid.sa article: بوابة الدفع تاب | Tap
- identifier: رقم الهوية المسجل في تاب
- statement: ادخل رقم الهوية المسجل في تاب للتحقق عن طريق نفاذ واكمل المعلومات المطلوبة
- cite_ids: ZD-S-0613

**Citation ZD-S-0613:** `https://help.zid.sa/tap-gateway/` | تفعيل تاب | 2026-08-05 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/162-help.zid.sa/text.txt` (5267 bytes), fetched 2026-10-12T04:53:34Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/068-help.zid.sa/text.txt` (5267 bytes), fetched 2026-10-12T10:50:44Z, captured
- quote: ادخل رقم الهوية المسجل في تاب للتحقق عن طريق نفاذ واكمل المعلومات المطلوبة
- title: زد - مركز المساعدة - بوابة الدفع تاب | Tap
- the page opens: زد - مركز المساعدة - بوابة الدفع تاب Tap menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الرئيسية الرئيسية بوابة الدفع تاب Tap عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون --> إدارة المخزون إدا…
- in context: … لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال الرئيسية بوابة الدفع تاب | Tap مشاركة متصفح الكمبيوتر آخر تحديث August 5, 2026 تاب بوابة دفع الكترونية مصرحة من البنك المركزي تسمح لك باستقبال المدفوعات عن طريق الوسائل المختلفة مثل مدى، ڤيزا ، ماستر كارد وغيرها كما انها تقدم خدماتها لجميع التجار في السعودية و دول الخليج ومصر. تفعيل تاب : لتفعيل تاب قم باختيار الاعدادات من لوحة التحكم > طرق الدفع اختر بوابة الدفع تاب ⟪ادخل رقم الهوية المسجل في تاب للتحقق عن طريق نفاذ واكمل المعلومات المطلوبة⟫ قم بالضغط على عرض تفاصيل اكثر لتحويلك على صفحة العمليات العمليات في متجرك : بعد التحقق والتفعيل، سيتم نقلك إلى صفحة العمليات في تاب حيث يمكنك مشاهدة جميع العمليات الناجحة، الفاشلة، والمستردة. كما يمكنك تصفية العمليات حسب ما يناسبك، بالإضافة إلى إمكانية البحث عنها وتصديرها. العمليات المستردة : لإسترداد المبلغ للعميل قم باختيار تفاصيل العملية والضغط على استرداد وادخل المبلغ سواء كان كامل او استرداد جزئي سيتم اضافة قائمة الاسترداد اسفل العملية الاس…

### Q3-ZD-039

**Cited at:** section 3, line 110

**Record** (`studies/proposals/records/Q3/zid/statements.tsv`):
- stmt_id: Q3-ZD-039
- bears_on: 1;2
- identifier: بيانات المتجر > العنوان التجاري > سبل
- statement: قم برفع ملف إثبات العنوان الوطني من سُبل SPL ، هذة الخطوة مطلوبة لتفعيل بعد الخدمات مثل المدفوعات.
- scope: السعودية
- cite_ids: Q3-ZD-C049
- from: held

**Citation Q3-ZD-C049:** `https://help.zid.sa/store-info-ksa/` | العنوان التجاري > سبل | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/158-help.zid.sa/text.txt` (10849 bytes), fetched 2026-10-12T04:53:30Z, captured
- quote: قم برفع ملف إثبات العنوان الوطني من سُبل SPL ، هذة الخطوة مطلوبة لتفعيل بعد الخدمات مثل المدفوعات.
- title: زد - مركز المساعدة - بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة المتجر الإعدادات بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ال…
- in context: …jpeg -.jpg -.png.) ولا يزيد الحجم عن 8 MB عدد الفروع. النشاط التجاري نوع النشاط التجاري العنوان التجاري : اختر العنوان التجاري وأكمل البيانات المطلوبة , في حال رغبتك بإظهار العنوان اسفل الصفحة قم بوضع علامة ال وقم بالضغط على حفظ. المنطقة الزمنية : عند رغبتك في تخصيص الوقت للمنطقة الزمنية بدقة، يمكنك اختيار المنطقة الزمنية المناسبة لعرض أوقات الطلبات وتصديرها بشكل صحيح. العنوان : ادخل عنوان الدولة والمدينة والشارع وقم بتحديد عن طريق الخرائط سبل : ⟪قم برفع ملف إثبات العنوان الوطني من سُبل SPL ، هذة الخطوة مطلوبة لتفعيل بعد الخدمات مثل المدفوعات.⟫ للمزيد من المعلومات حول بيانات المتجر يمكنك الإطلاع الفديو التالي: سوف تتعلم: معلومات المتجر تفاصيل النشاط التجاري العنوان التجاري التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم أولوية السحب من المخزون ( لوحة التحكم الجديدة ) المنتجات الرقمية و إيداع المبالغ ( لوحة التحكم الجديدة ) تواصل معنا هل تحتاج إلى مساعدة إضاف…
