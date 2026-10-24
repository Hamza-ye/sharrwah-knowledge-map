# Cards: Q3 on zid

8 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 17:** - Checked against a merchant selling in the Yemeni market: any country beyond the 40 on Shopify's list of supported countries is absent, Yemen not among the 40, and for store fake-demo-sharrwah, whose business entity is in Yemen, observed 5 October 2026, the admin's ShopifyPaymentsData answer gave Shopify Payments "eligible":false. Zid Pay's Kuwait terms bar activities dealing with countries under international sanctions, naming اليمن; its Saudi terms' list doesn't. Q3-SH-A0002; Q3-SH-100; Q3-ZD-P0112; Q3-ZD-P0111
- **section 1, line 21:** - All five verify the person and the business before payments, a match on role (help pages, stated): Shopify and its banking partners "collect and verify information about you and your business"; WooPayments verifies business details with Stripe; Salla asks for an ID or iqama matching Absher, the entity's document, and a stamped IBAN certificate in a matching name; Zid's gateway approves the account on requirements set by business entity; and BigCommerce Payments shows KYC status among its Actions tasks. Q3-SH-012; Q3-WC-012; Q3-SA-013; Q3-ZD-P0118; Q3-BC-P0072
- **section 1, line 22:** - What is asked differs by entity type and place. Zid: "تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة". Salla's table asks an individual for a freelance document (Saudi citizens only), an establishment or company for a commercial registration, and a charity for its certificate, each with its own kind of bank account. Shopify's Proof of Liveness depends on the country; on store capture-advanced, the saved markup of the business details step, observed 4 October 2026, gives a US Individual's Social Security Number field as "Used for tax filing and verification.", as its accessibility tree did. Q3-ZD-K0240; Q3-SA-014; Q3-SH-041; Q3-SH-111
- **section 1, line 23:** - Other steps come first. Zid needs one published product matching the activity, and the store owner's Nafath check (not checked on WooCommerce; shown by Zid). Shopify needs two-step authentication; on store ibx5bt-xy, the saved markup of the Payments step, observed 30 September 2026, holds in a dialog "You need to set-up two-step authentication before adding a bank account.", words its accessibility tree doesn't show. Shopify and WooCommerce need test mode off, the same term for the same thing, and on store demo-fake-dev-store the saved markup of the Payments step, observed 30 September 2026, says "Development stores can only process test payments", as its accessibility tree did. Salla's activation includes accepting سياسة البيع. Q3-ZD-P0116; Q3-ZD-P0117; Q3-SH-K1274; Q3-SH-107; Q3-SH-028; Q3-WC-017; Q3-SH-106; Q3-SA-K1532
- **section 1, line 29:** - The payout account's holder must match the verified identity, a match on role. Shopify compares the bank account's name with the legal business name or the account representative's. Salla: "تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق". Zid: "لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح". On both Salla and Zid an establishment needs a business account in its own name. Q3-SH-062; Q3-SA-K1563; Q3-ZD-K0037; Q3-SA-010; Q3-ZD-015
- **section 1, line 30:** - Salla requires verification to withdraw the store balance and transfer the electronic payments balance; on store merchant (Basic, observed 8 October 2026) withdrawal was disabled for `store_documents_required`. Zid's wallet takes balance the seller adds and spends, and "لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب"; its words don't say it holds sales proceeds, so the draft leaves it out of the money flow. Q3-SA-P0162; Q3-SA-077; Q3-ZD-P0063
- **section 1, line 35:** - Salla and Zid keep their own lists too: Salla's سياسة البيع, from gambling to resold shipping labels, and Zid Pay's الأنشطة المحظورة. Q3-SA-054; Q3-SA-K1532; Q3-ZD-P0111
- **section 1, line 53:** - Some checks fall on the owner in person: on Shopify only the account owner can complete a Proof of Liveness check, and on Zid the store owner passes Nafath (not checked on WooCommerce; shown by Zid). Q3-SH-043; Q3-ZD-P0117
- **section 1, line 60:** - Payment partners approve, a match on role (BigCommerce's pricing page, official; the others help pages, stated): Zid's requirements go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and its Nafath request is in the service provider's name; a PayPal Braintree application on BigCommerce doesn't guarantee approval; WooPayments verifies with Stripe; and Shopify's banking partners require a real person on every account. Q3-ZD-P0118; Q3-ZD-P0047; Q3-BC-P0065; Q3-WC-012; Q3-SH-020
- **section 2, line 81:** - **Seller** (proposed): the person who opens the account and contracts with Sharrwah, and the first subject of requirements, including the identity checks only that person can complete. It takes Shopify's Store Owner as the contracting party and BigCommerce's creator as the owner, and puts the owner-only checks on it, as Shopify's Proof of Liveness and Zid's Nafath do. Why: rule 3, since who carries a requirement is the data model. Q3-SH-K1237; Q3-BC-004; Q3-SH-043; Q3-ZD-P0117
- **section 2, line 82:** - **Business** (proposed): the legal entity behind one or more stores, with its **entity type** and its **registration place**, the place whose government documents it uses. These two choose each requirement set. The registration place comes from Salla's question for the country whose government documents the store uses (observed, Store 1, 8 October 2026) and WooPayments' country of registration; the entity types from Salla and Zid, whose requirements differ by entity type and country. Why: rule 1, since the place selects configuration rather than code, and rule 3. Q3-SA-085; Q3-WC-K0402; Q3-SA-056; Q3-ZD-K0239; Q3-ZD-K0240
- **section 2, line 88:** - **Requirement** (proposed): one condition, with its kind, subject, setter, validity and check. Its kinds come from the platforms: information, a document, an identity check, a plan, an accepted agreement, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account age such as WooPayments' 7 days before a first payout, a match between subjects such as the payout account's holder and the verified name, not being a listed party, as under Shopify Payments' sanctions rule, and another capability being active. Validity follows rules such as Zid's commercial register valid two months from activation. Its subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-WC-P0038; Q3-SA-K1563; Q3-SH-K2268; Q3-ZD-013
- **section 2, line 89:** - **Requirement set** (proposed): the requirements one capability needs, for one registration place, entity type, plan and provider; configured, versioned and shown to the seller. It combines Salla's per-country verification (a UAE trade licence, Emirates IDs and an IBAN certificate; in Saudi Arabia, an Absher-matched ID and a citizens-only freelance document), Zid's per-entity and per-country requirements, and Shopify's per-country Proof of Liveness. Why: rule 1. Q3-SA-072; Q3-SA-014; Q3-SA-013; Q3-ZD-K0240; Q3-SH-041
- **section 2, line 90:** - The lists change: Shopify's Shop requirements are "subject to change without notice", its European and UK verification is being updated throughout 2026, and Zid's prohibited activities "يمكن تحديثها في أي وقت، مع إشعار التاجر". So a set is versioned data, and a met requirement keeps the version it was met under. Why: rule 2. Q3-SH-083; Q3-SH-065; Q3-ZD-P0111
- **section 2, line 91:** - **Submission** and **Review** (proposed): the seller gives information and documents inside Sharrwah and declares them true, as Salla's KYC schema requires; a review decides: pending, approved, rejected with reasons, or more needed. Each review has a checker, which is Sharrwah's team, a provider or an identity service, with its own attempt limits and timing, as Zid's team, Zid's gateway, and the daily attempts of Absher and Nafath show. Documents come only through Sharrwah, as Shopify accepts them only through its admin. Why: rule 2 for the checker, rule 3 for the data. Q3-SA-057; Q3-ZD-P0038; Q3-ZD-P0118; Q3-SA-008; Q3-ZD-K0262; Q3-SH-015
- **section 3, line 107:** - Checkers: an identity service, such as Nafath on Zid and Absher on Salla, or a provider's own onboarding, such as Stripe's for WooPayments and the gateway that approves a Zid Pay account. Q3-ZD-P0117; Q3-SA-013; Q3-WC-012; Q3-ZD-P0118
- **section 3, line 114:** - Per registration place: the documents and checks, as on Salla by country, on Zid by country, and for Shopify's Proof of Liveness. Q3-SA-072; Q3-ZD-K0240; Q3-SH-041
- **section 3, line 115:** - Per entity type and place: the documents, the fields, and the kind of payout account, as in Salla's table, on Zid, and in the Social Security Number field for a US Individual in Shopify store capture-advanced's saved markup, observed 4 October 2026. Q3-SA-014; Q3-SA-010; Q3-ZD-015; Q3-SH-111
- **section 3, line 120:** - Per person: the identity checks only the owner completes. Q3-SH-043; Q3-ZD-P0117
- **section 3, line 126:** - A provider: its own requirements and its approval. Q3-ZD-P0118; Q3-BC-P0065; Q3-SH-110
- **section 5, line 145:** - Who checks a seller before payments in a place: Sharrwah's own review (Salla), a gateway's approval (Zid), a partner's check (Stripe for WooPayments, Shopify's banking partners), or more than one. It is costly to change, being legal structure and partner contracts, and a partner's check may not reach a place, as for Yemen. Keep open: the checker as a plug-in and the setter on every requirement, with no single path built in. Settled by the company decisions on providers and on Sharrwah's own position (section 7). Q3-SA-037; Q3-ZD-P0118; Q3-WC-012; Q3-SH-012; YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 168:** - Whether Sharrwah checks sellers itself, relies on payment providers' checks, or both, and in which places. Q3-SA-037; Q3-ZD-P0118; Q3-WC-012
- **section 7, line 169:** - Which identity services and payment providers Sharrwah works with, since their requirements then bind its sellers. Q3-ZD-P0117; Q3-SA-013; Q3-SH-057

## The cards

### Q3-ZD-P0111

**Cited at:** section 1, line 17; section 1, line 35; section 2, line 90

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-110
- bullet: e
- placement: decides
- identifier: شروط وأحكام زد باي > الأنشطة المحظورة
- statement: لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن: الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخدرات والمنظمات الإرهابية. الأشخاص ذوو طبيعة نشاط من الصعب التحقق من شرعيته أو مصدر دخله، أو ذوو مصدر دخل لا يتوافق مع أوضاعهم المالية. الأشخاص الذين يرفضون تزويدنا بأي معلومات أو مستندات مطلوبة للتحقق من أنشطتهم أو مصادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو متلاعب بها. المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي. مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها. المؤسسات المالية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إليها بـ (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة. الأنشطة غير المتوافقة مع الشريعة الإسلامية. الوكلاء الوسطاء غير الرسميين. شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية. الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك. التجار الذين لا يقدموا أي معلومات كافية للتحقق من هوياتهم، أو هوية المستفيد النهائي. التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين طبقت عليهم عقوبات بناء على قرارات الأمم المتحدة، أو وزارة الخزانة الإنجليزية، أو الاتحاد الأوروبي، أو مكتب مراقبة الأصول الأجنبية، أو من هو مطالب للامتثال إذا كان الاسم مطابق لأي قائمة عقوبات أخرى. التاجر أو المستفيد النهائي ( الشريك في عملية البيع والشراء) الذي يقطن في البلدان الخاضعة للعقوبات الدولية تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية أفريقيا الوسطى) وما إلى ذلك. التجار مقدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات وخلافه). الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية. الحسابات المجهولة والمسجلة بأسماء وهمية. الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء. التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة أو أي نشاط آخر لا يتوافق مع مزود الخدمة.
- scope: السعودية
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C219;S01-ZD-C220;S01-ZD-C221;S01-ZD-C222;S01-ZD-C223;S01-ZD-C224;S01-ZD-C225;S01-ZD-C226;S01-ZD-C227;S01-ZD-C228;S01-ZD-C229;S01-ZD-C230;S01-ZD-C231;S01-ZD-C232;S01-ZD-C233;S01-ZD-C234;S01-ZD-C235;S01-ZD-C236;S01-ZD-C237;S01-ZD-C238;S01-ZD-C239;S01-ZD-C240;S01-ZD-C241;S01-ZD-C242
- from: new
- note: The list opens with تتضمن and closes with أو أي نشاط آخر لا يتوافق مع مزود الخدمة; no words present it as complete. Each item is cited.

**Citation S01-ZD-C219:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن:
- title: Zid | Create your online store with modern retail services
- in context: …الدفع "Apple Pay" أنه خاضع لشروط وأحكام شركة أبل (Apple Pay Merchant Terms) وأن زد باي غير مسؤولة عن عدم امتثال التاجر لهذه الشروط. الأنشطة المحظورة: ⟪لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن:⟫ الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخدرات و…

**Citation S01-ZD-C220:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخدرات والمنظمات الإرهابية.
- title, opening and note boxes: as for this source's citation above
- in context: …أنشطة المحظورة: لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن: ⟪الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخدرات والمنظمات الإرهابية.⟫ الأشخاص ذوو طبيعة نشاط من الصعب التحقق من شرعيته أو مصدر دخله، أو ذوو مصدر دخل لا يتوافق مع أوضاعهم المالية. الأشخاص الذين يرفضون تزويدنا بأي معلومات…

**Citation S01-ZD-C221:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الأشخاص ذوو طبيعة نشاط من الصعب التحقق من شرعيته أو مصدر دخله، أو ذوو مصدر دخل لا يتوافق مع أوضاعهم المالية.
- title, opening and note boxes: as for this source's citation above
- in context: …م معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخدرات والمنظمات الإرهابية. ⟪الأشخاص ذوو طبيعة نشاط من الصعب التحقق من شرعيته أو مصدر دخله، أو ذوو مصدر دخل لا يتوافق مع أوضاعهم المالية.⟫ الأشخاص الذين يرفضون تزويدنا بأي معلومات أو مستندات مطلوبة للتحقق من أنشطتهم أو مصادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو مت…

**Citation S01-ZD-C222:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الأشخاص الذين يرفضون تزويدنا بأي معلومات أو مستندات مطلوبة للتحقق من أنشطتهم أو مصادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو متلاعب بها.
- title, opening and note boxes: as for this source's citation above
- in context: … والاتجار بالمخدرات والمنظمات الإرهابية. الأشخاص ذوو طبيعة نشاط من الصعب التحقق من شرعيته أو مصدر دخله، أو ذوو مصدر دخل لا يتوافق مع أوضاعهم المالية. ⟪الأشخاص الذين يرفضون تزويدنا بأي معلومات أو مستندات مطلوبة للتحقق من أنشطتهم أو مصادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو متلاعب بها.⟫ المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي. مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها. المؤسسات المالية …

**Citation S01-ZD-C223:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي.
- title, opening and note boxes: as for this source's citation above
- in context: …لذين يرفضون تزويدنا بأي معلومات أو مستندات مطلوبة للتحقق من أنشطتهم أو مصادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو متلاعب بها. ⟪المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي.⟫ مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها. المؤسسات المالية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إل…

**Citation S01-ZD-C224:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها.
- title, opening and note boxes: as for this source's citation above
- in context: …صادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو متلاعب بها. المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي. ⟪مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها.⟫ المؤسسات المالية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إليها ب (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خا…

**Citation S01-ZD-C225:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: المؤسسات المالية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إليها بـ (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة.
- title, opening and note boxes: as for this source's citation above
- in context: …ها أو متلاعب بها. المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي. مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها. ⟪المؤسسات المالية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إليها ب (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة.⟫ الأنشطة غير المتوافقة مع الشريعة الإسلامية. الوكلاء الوسطاء غير الرسميين. شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية. الأنشطة …

**Citation S01-ZD-C226:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الأنشطة غير المتوافقة مع الشريعة الإسلامية.
- title, opening and note boxes: as for this source's citation above
- in context: …الية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إليها ب (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة. ⟪الأنشطة غير المتوافقة مع الشريعة الإسلامية.⟫ الوكلاء الوسطاء غير الرسميين. شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية. الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلد…

**Citation S01-ZD-C227:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الوكلاء الوسطاء غير الرسميين.
- title, opening and note boxes: as for this source's citation above
- in context: …يكون لها حضورًا ماديًا والمشار إليها ب (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة. الأنشطة غير المتوافقة مع الشريعة الإسلامية. ⟪الوكلاء الوسطاء غير الرسميين.⟫ شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية. الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، ت…

**Citation S01-ZD-C228:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية.
- title, opening and note boxes: as for this source's citation above
- in context: … إليها ب (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة. الأنشطة غير المتوافقة مع الشريعة الإسلامية. الوكلاء الوسطاء غير الرسميين. ⟪شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية.⟫ الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الو…

**Citation S01-ZD-C229:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك.
- title, opening and note boxes: as for this source's citation above
- in context: …للرقابة. الأنشطة غير المتوافقة مع الشريعة الإسلامية. الوكلاء الوسطاء غير الرسميين. شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية. ⟪الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك.⟫ التجار الذين لا يقدموا أي معلومات كافية للتحقق من هوياتهم، أو هوية المستفيد النهائي. التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين…

**Citation S01-ZD-C230:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: التجار الذين لا يقدموا أي معلومات كافية للتحقق من هوياتهم، أو هوية المستفيد النهائي.
- title, opening and note boxes: as for this source's citation above
- in context: …مل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك. ⟪التجار الذين لا يقدموا أي معلومات كافية للتحقق من هوياتهم، أو هوية المستفيد النهائي.⟫ التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين طبقت عليهم عقوبات بناء على قرارات الأمم المتحدة، أو وزارة الخزانة الإنجليزية، أو الا…

**Citation S01-ZD-C231:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين طبقت عليهم عقوبات بناء على قرارات الأمم المتحدة، أو وزارة الخزانة الإنجليزية، أو الاتحاد الأوروبي، أو مكتب مراقبة الأصول الأجنبية، أو من هو مطالب للامتثال إذا كان الاسم مطابق لأي قائمة عقوبات أخرى.
- title, opening and note boxes: as for this source's citation above
- in context: …جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك. التجار الذين لا يقدموا أي معلومات كافية للتحقق من هوياتهم، أو هوية المستفيد النهائي. ⟪التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين طبقت عليهم عقوبات بناء على قرارات الأمم المتحدة، أو وزارة الخزانة الإنجليزية، أو الاتحاد الأوروبي، أو مكتب مراقبة الأصول الأجنبية، أو من هو مطالب للامتثال إذا كان الاسم مطابق لأي قائمة عقوبات أخرى.⟫ التاجر أو المستفيد النهائي ( الشريك في عملية البيع والشراء) الذي يقطن في البلدان الخاضعة للعقوبات الدولية تتضمن (إيران، سوريا، جنوب السودان، كوبا، ار…

**Citation S01-ZD-C232:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: التاجر أو المستفيد النهائي ( الشريك في عملية البيع والشراء) الذي يقطن في البلدان الخاضعة للعقوبات الدولية تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية أفريقيا الوسطى) وما إلى ذلك.
- title, opening and note boxes: as for this source's citation above
- in context: … أو وزارة الخزانة الإنجليزية، أو الاتحاد الأوروبي، أو مكتب مراقبة الأصول الأجنبية، أو من هو مطالب للامتثال إذا كان الاسم مطابق لأي قائمة عقوبات أخرى. ⟪التاجر أو المستفيد النهائي ( الشريك في عملية البيع والشراء) الذي يقطن في البلدان الخاضعة للعقوبات الدولية تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية أفريقيا الوسطى) وما إلى ذلك.⟫ التجار مقدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات …

**Citation S01-ZD-C233:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: التجار مقدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات وخلافه).
- title, opening and note boxes: as for this source's citation above
- in context: …ية البيع والشراء) الذي يقطن في البلدان الخاضعة للعقوبات الدولية تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية أفريقيا الوسطى) وما إلى ذلك. ⟪التجار مقدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات وخلافه).⟫ الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية. الحسابات المجهولة والمسجلة بأسماء وهمية. الحسابات …

**Citation S01-ZD-C234:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية.
- title, opening and note boxes: as for this source's citation above
- in context: …قدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات وخلافه). ⟪الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية.⟫ الحسابات المجهولة والمسجلة بأسماء وهمية. الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء. التجار الذين لم تكتمل إجراءات التحقق الو…

**Citation S01-ZD-C235:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الحسابات المجهولة والمسجلة بأسماء وهمية.
- title, opening and note boxes: as for this source's citation above
- in context: … شركات التداول، تجميع الأموال أو الحوالات وخلافه). الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية. ⟪الحسابات المجهولة والمسجلة بأسماء وهمية.⟫ الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء. التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لع…

**Citation S01-ZD-C236:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء.
- title, opening and note boxes: as for this source's citation above
- in context: … وخلافه). الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية. الحسابات المجهولة والمسجلة بأسماء وهمية. ⟪الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء.⟫ التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. تجارة السجائر والسجا…

**Citation S01-ZD-C237:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم.
- title, opening and note boxes: as for this source's citation above
- in context: …هات المعنية في المملكة العربية السعودية. الحسابات المجهولة والمسجلة بأسماء وهمية. الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء. ⟪التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم.⟫ تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاج…

**Citation S01-ZD-C238:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ.
- title, opening and note boxes: as for this source's citation above
- in context: …قم بدلاً عن الأسماء. التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. ⟪تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ.⟫ المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقيي…

**Citation S01-ZD-C239:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: المراهنة/ المزاد.
- title, opening and note boxes: as for this source's citation above
- in context: … عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. ⟪المراهنة/ المزاد.⟫ الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من …

**Citation S01-ZD-C240:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر.
- title, opening and note boxes: as for this source's citation above
- in context: …لتحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. ⟪الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر.⟫ المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة أو أي نشاط آخر لا يتوافق مع مزود الخدمة. طريقة الاستف…

**Citation S01-ZD-C241:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة
- title, opening and note boxes: as for this source's citation above
- in context: …ارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. ⟪المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة⟫ أو أي نشاط آخر لا يتوافق مع مزود الخدمة. طريقة الاستفادة من خدمات زد باي -تفعيل الخدمة: يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. …

**Citation S01-ZD-C242:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | الأنشطة المحظورة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: أو أي نشاط آخر لا يتوافق مع مزود الخدمة.
- title, opening and note boxes: as for this source's citation above
- in context: …ة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة ⟪أو أي نشاط آخر لا يتوافق مع مزود الخدمة.⟫ طريقة الاستفادة من خدمات زد باي -تفعيل الخدمة: يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. يجب أن يكون نشاط التاجر صحيح ولا يخدم أي …

### Q3-ZD-P0118

**Cited at:** section 1, line 21; section 1, line 60; section 2, line 91; section 3, line 107; section 3, line 126; section 5, line 145; section 7, line 168

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-117
- bullet: b;e
- placement: decides
- identifier: متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- statement: لإتاحة خيار الدفع الإلكتروني في المتجر يتطلب تزويد بوابة الدفع بمتطلبات التفعيل حسب الكيان التجاري (فرد – شركة – مؤسسة) ليتم اعتماد الحساب لدى بوابة الدفع.
- scope: متطلبات تفعيل الدفع الالكتروني للسعودية
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C285
- from: index:ZD-C-001:ZD-S-0528

**Citation S01-ZD-C285:** `https://help.zid.sa/payment-requirements/` | opening paragraph | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T04:53:19Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/066-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T10:50:42Z, captured
- quote: لإتاحة خيار الدفع الإلكتروني في المتجر يتطلب تزويد بوابة الدفع بمتطلبات التفعيل حسب الكيان التجاري (فرد – شركة – مؤسسة) ليتم اعتماد الحساب لدى بوابة الدفع.
- title: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ا…
- in context: … الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي العمليات روابط الدفع الإيداعات الحسابات البنكية المدفوعات تفعيل زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال زد باي متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 6, 2026 ⟪لإتاحة خيار الدفع الإلكتروني في المتجر يتطلب تزويد بوابة الدفع بمتطلبات التفعيل حسب الكيان التجاري (فرد - شركة - مؤسسة) ليتم اعتماد الحساب لدى بوابة الدفع.⟫ متطلبات تفعيل الدفع الالكتروني للسعودية : الكيانات المدعومة : فرد. مؤسسة. شركة. متطلبات الأفراد : وثيقة عمل حر. الهوية الوطنية. حساب بنكي تجاري. شهادة العنوان الوطني. الوثيقة : عند إرفاق الوثيقة يجب مراعاة التالي: أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر ( مثال : في حال بيع التاجر لمنتجات العطور يجب أن تكون الوثيقة "صناعة العطور" أو "إدارة المبيعات" ) مراعاة أهمية تاريخ صلاحية الوثيقة (يجب أن يكون التاريخ ساري) ولاستخراج وثيقة عمل حر يرجى …

### Q3-ZD-K0240

**Cited at:** section 1, line 22; section 2, line 82; section 2, line 89; section 3, line 114

**The same record as Q1-ZD-K0240,** whose card is in `Q1-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة.
- scope: 

### Q3-ZD-P0116

**Cited at:** section 1, line 23; section 2, line 88

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-115
- bullet: e
- placement: decides
- identifier: تفعيل الدفع الالكتروني > ملاحظة
- statement: لابد من اضافة منتج واحد منشور ومطابق للنشاط في المتجر قبل رفع طلب التفعيل
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C283
- from: index:ZD-C-001:ZD-S-0531

**Citation S01-ZD-C283:** `https://help.zid.sa/activate-online-payments/` | ملاحظة | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: لابد من اضافة منتج واحد منشور ومطابق للنشاط في المتجر قبل رفع طلب التفعيل
- title: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: …تروني خلال الشهر الواحد ، وحجم المبيعات المتوقعة لعمليات الدفع الإلكتروني وتفاصيل بياناتك البنكية. في حال الرغبة بإضافة حساب بنكي جديد يرجى اتباع الخطوات التالية: إضافة حساب بنكي في صفحة خيارات الدفع. العودة لتفعيل زد باي مرة أخرى. ملاحظة 💡 : مشاركة عدد العمليات المتوقعة لغرض ضمان حقك المالي ولا يوجد تأثير على رسوم الخدمة. قم باختيار الحساب البنكي لاستقبال إيداعات المبالغ المحصلة . ملاحظة 💡 : لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح ⟪لابد من اضافة منتج واحد منشور ومطابق للنشاط في المتجر قبل رفع طلب التفعيل⟫ وبعد ذلك ، قم بالضغط على ايقونة التالي الخطوة الثالثة والأخيرة وهي تفعيل الشبكات ،اختر شبكات الدفع التي ترغب بتفعيلها في متجرك ، وبإمكانك التحكم بجميع الشبكات لاحقاً. مع أهمية الموافقة على الشروط والاحكام ✅ بعد ذلك ، قم بالضغط على ايقونة تفعيل ملاحظة 💡 : يمكنك الوصول لاحقاً على الشروط والأحكام عن طريق صفحة إدارة المدفوعات بعد التفعيل. في حال لديك بوابة دفع أخرى مفعلة سيتم تعطيلها وتفعيل المدفوعات بشكل مؤتمت. مراجعة المعلومات واستقبال عمليات الدف…

### Q3-ZD-P0117

**Cited at:** section 1, line 23; section 1, line 53; section 2, line 81; section 3, line 107; section 3, line 120; section 7, line 169

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-116
- bullet: e
- placement: decides
- identifier: اجتياز التحقق من نفاذ
- statement: لتفعيل زد باي و استقبال عمليات الدفع الإلكتروني يشترط لمالك المتجر اجتياز التحقق من نفاذ.
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C284
- from: new

**Citation S01-ZD-C284:** `https://help.zid.sa/nafath_verification/` | opening paragraph | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/140-help.zid.sa/text.txt` (4982 bytes), fetched 2026-10-12T04:53:12Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/064-help.zid.sa/text.txt` (4982 bytes), fetched 2026-10-12T10:50:40Z, captured
- quote: لتفعيل زد باي و استقبال عمليات الدفع الإلكتروني يشترط لمالك المتجر اجتياز التحقق من نفاذ.
- title: زد - مركز المساعدة - اجتياز التحقق من نفاذ
- the page opens: زد - مركز المساعدة - اجتياز التحقق من نفاذ menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الرئيسية الرئيسية اجتياز التحقق من نفاذ عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون --> إدارة المخزون…
- in context: …ر زد الأسئلة الشائعة تواصل معنا مركز المساعدة الرئيسية الرئيسية اجتياز التحقق من نفاذ عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية تعرف على زد إعدادات المتجر المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال الرئيسية اجتياز التحقق من نفاذ مشاركة متصفح الكمبيوتر آخر تحديث August 6, 2026 ⟪لتفعيل زد باي و استقبال عمليات الدفع الإلكتروني يشترط لمالك المتجر اجتياز التحقق من نفاذ.⟫ خطوات اجتياز تحقق نفاذ قبل البدء بخطوات التحقق يرجى التأكد من: تحميل تطبيق نفاذ و تسجيل الدخول. التأكد من صحة رقم الهوية الوطنية لمالك النشاط المسجل في إعدادات بيانات المتجر. لاجتياز التحقق من نفاذ يرجى إتباع الخطوات التالية : قم بالضغط على أيقونة تأكيد تفعيل زد باي في أخر خطوة من التفعيل و الموافقة على الشروط والأحكام. سيتم الانتقال إلى خطوة التحقق من نفاذ. ملاحظة : المدة المتاحة للتحقق في الجلسة الواحدة هي 3 دقائق. عدد محاولات التحقق المتاحة خ…

### Q3-ZD-K0037

**Cited at:** section 1, line 29

**Record** (`studies/proposals/records/Q3/zid/copied.tsv`):
- concern_id: ZD-C-004
- placement: decides
- structure: help.zid.sa article: تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- identifier: مطابقة الهوية
- statement: لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح
- cite_ids: ZD-S-0559

**Citation ZD-S-0559:** `https://help.zid.sa/activate-online-payments/` | ملاحظة | 2026-09-28 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/085-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T04:52:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/048-help.zid.sa/text.txt` (7640 bytes), fetched 2026-10-12T10:50:24Z, captured
- quote: لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح
- title: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: … الحساب البنكي ،اختر العدد المتوقع لعمليات الدفع الإلكتروني خلال الشهر الواحد ، وحجم المبيعات المتوقعة لعمليات الدفع الإلكتروني وتفاصيل بياناتك البنكية. في حال الرغبة بإضافة حساب بنكي جديد يرجى اتباع الخطوات التالية: إضافة حساب بنكي في صفحة خيارات الدفع. العودة لتفعيل زد باي مرة أخرى. ملاحظة 💡 : مشاركة عدد العمليات المتوقعة لغرض ضمان حقك المالي ولا يوجد تأثير على رسوم الخدمة. قم باختيار الحساب البنكي لاستقبال إيداعات المبالغ المحصلة . ملاحظة 💡 : ⟪لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح⟫ لابد من اضافة منتج واحد منشور ومطابق للنشاط في المتجر قبل رفع طلب التفعيل وبعد ذلك ، قم بالضغط على ايقونة التالي الخطوة الثالثة والأخيرة وهي تفعيل الشبكات ،اختر شبكات الدفع التي ترغب بتفعيلها في متجرك ، وبإمكانك التحكم بجميع الشبكات لاحقاً. مع أهمية الموافقة على الشروط والاحكام ✅ بعد ذلك ، قم بالضغط على ايقونة تفعيل ملاحظة 💡 : يمكنك الوصول لاحقاً على الشروط والأحكام عن طريق صفحة إدارة المدفوعات بعد التفعيل. في حال لديك بوابة دفع أخرى مفعلة سيتم …

### Q3-ZD-015

**Cited at:** section 1, line 29; section 3, line 115

**Record** (`studies/proposals/records/Q3/zid/statements.tsv`):
- stmt_id: Q3-ZD-015
- bears_on: 1;2
- identifier: متطلبات تفعيل الدفع الالكتروني للمؤسسات > الحساب البنكي و الشهادة البنكية
- statement: يجب اختيار حساب بنكي تجاري. يجب أن يكون اسم المستفيد للحساب البنكي مطابق لاسم المنشأة في السجل التجاري. يجب إرفاق الشهادة البنكية مع مراعاة أن يكون اسم المستفيد في الشهادة البنكية باللغة الانجليزي.
- scope: المؤسسات
- cite_ids: Q3-ZD-C016
- from: held

**Citation Q3-ZD-C016:** `https://help.zid.sa/payment-requirements/` | متطلبات تفعيل الدفع الالكتروني للمؤسسات > الحساب البنكي و الشهادة البنكية | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T04:53:19Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/066-help.zid.sa/text.txt` (11499 bytes), fetched 2026-10-12T10:50:42Z, captured
- quote: يجب اختيار حساب بنكي تجاري. يجب أن يكون اسم المستفيد للحساب البنكي مطابق لاسم المنشأة في السجل التجاري. يجب إرفاق الشهادة البنكية مع مراعاة أن يكون اسم المستفيد في الشهادة البنكية باللغة الانجليزي.
- title: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> ا…
- in context: …ر مطابقة لنشاط السجل يجب إضافة أنشطة فرعية للسجل التجاري بشكل مباشر من خلال موقع وزارة التجارة). أن يكون السجل التجاري ساري المدة مع مراعاة أن لا تقل الصلاحية عن شهرين من تاريخ التفعيل و يمكن تجديد السجل التجاري بكل سهولة من خلال موقع وزارة التجارة الكترونياً. الهوية الوطنية : يجب توفير الهوية الوطنية مع مراعاة التالي: تاريخ صلاحية الهوية المرفقة (يجب أن تكون الهوية سارية). حامل الهوية مطابق لمالك السجل التجاري. الحساب البنكي و الشهادة البنكية : ⟪يجب اختيار حساب بنكي تجاري. يجب أن يكون اسم المستفيد للحساب البنكي مطابق لاسم المنشأة في السجل التجاري. يجب إرفاق الشهادة البنكية مع مراعاة أن يكون اسم المستفيد في الشهادة البنكية باللغة الانجليزي.⟫ شهادة العنوان الوطني: عند إرفاق شهادة العنوان الوطني يجب مراعاة التالي: أن يكون اسم المستفيد مطابق للسجل التجاري أن تكون جميع البيانات واضحة. ملاحظة : يجب التأكد من إرفاق المستندات التالية كاملة وصحيحة و بجودة عالية متطلبات تفعيل الدفع الالكتروني للشركات: السجل التجاري. الهوية الوطنية لجميع الملّاك. عقد التأسيس. حساب بنكي تجاري. شهادة العنوان الوطني. ترخيص الاستثمار (للشركات الأجنبية). السجل التجاري : يجب إرفاق السجل التجاري الخاص بالشركة مع مرا…

### Q3-ZD-P0063

**Cited at:** section 1, line 30

**Record** (`studies/proposals/records/Q3/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-062
- bullet: c
- placement: decides
- identifier: محفظة زد ( لوحة التحكم الجديدة ) > توثيق المحفظة > ملاحظة
- statement: يمكنك إضافة رصيد للمحفظة و يمكنك الشراء عن طريق المحفظة لكن لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب .
- cite_ids: S01-ZD-C114
- from: index:ZD-C-017:ZD-S-0653

**Citation S01-ZD-C114:** `https://help.zid.sa/zid-wallet/` | ملاحظة | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/182-help.zid.sa/text.txt` (7931 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/072-help.zid.sa/text.txt` (7931 bytes), fetched 2026-10-12T10:50:48Z, captured
- quote: يمكنك إضافة رصيد للمحفظة و يمكنك الشراء عن طريق المحفظة لكن لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب .
- title: زد - مركز المساعدة - محفظة زد ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - محفظة زد ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الرئيسية الرئيسية محفظة زد ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة الم…
- in context: …حقق وتوثيق المحفظة قم بالضغط على التحقق من الحساب اعلى الصفحة في حال تم اختيار فرد : يتم تعبئة البيانات التالية : رقم الهوية الوطنية. رقم الجوال. البريد الإلكتروني. اختيار الحساب البنكي. صورة الهوية الوطنية. في حال تم اختيار شركة : يتم تعبئة البيانات التالية : رقم الهوية الوطنية. رقم الجوال. البريد الإلكتروني. صورة السجل التجاري. رقم السجل التجاري. رقم مدير عمليات المحفظة. اختيار الحساب البنكي. ثم قم بالضغط على أيقونة تأكيد المعلومات. ملاحظة 💡 : ⟪يمكنك إضافة رصيد للمحفظة و يمكنك الشراء عن طريق المحفظة لكن لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب .⟫ تصدير تفاصيل المحفظة : لتصدير تفاصيل المحفظة قم بالضغط على ايقونة تصدير ليتم إرسال الملف على بريدك الإلكتروني إضافة رصيد للمحفظة: يمكنك إضافة رصيد من خلال الضغط على أيقونة إضافة رصيد للمحفظة من اعلى الصفحة او من خلال لوحة التحكم > المالية > المحفظة بإمكانك إضافة رصيد بالخيارات التالية : البطاقة الائتمانية. آبل باي ( لمستخدمين ابل او متصفح جوال ) التحويل البنكي. ملاحظة 💡: في حال تم التحويل عن طريق حساب بنكي موثق من عملية توثيق المحفظة، سيتم إيداع…
