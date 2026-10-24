# Cards: Q3 on salla

17 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 51:** - Salla requires every verification document to be in the store owner's own name. Its KYC schema for a demo store, observed 8 October 2026, offers the entity types `single`, `company`, `institution`, `charity` and `government`; Zid's business types are فرد، مؤسسة، شركة، جمعية خيرية. They match on role in four of five (Salla's schema observed, Zid's help page stated); Salla adds government. Q3-SA-019; Q3-SA-056; Q3-ZD-K0239
- **section 1, line 59:** - Salla calls its verification an "إجراء تشغيلي داخلي لتفعيل بوابات الدفع والحساب البنكي", apart from the government's Business Platform licence. Q3-SA-037
- **section 1, line 61:** - Law, regulators and networks set others, as the platforms report them: Shopify's European and UK verification follows the FCA and the Central Bank of Ireland, and its prohibited categories may come from law, network rules, Shopify or processors' providers; Zid's licences come from the relevant authorities; and Salla's e-commerce obligations from the e-commerce law and the Ministry of Commerce's guide. Q3-SH-065; Q3-SH-P0045; Q3-ZD-023; Q3-SA-033
- **section 1, line 65:** - When the seller applies, with review times that differ: Salla 24 to 48 hours; Shopify's documents up to 24 hours; WooPayments typically a couple of days. Zid's team reviews and notifies by email. Q3-SA-003; Q3-SH-014; Q3-WC-004; Q3-ZD-P0038
- **section 1, line 66:** - Attempts are limited: Absher three a day on Salla, Nafath three a day on Zid. Q3-SA-008; Q3-ZD-K0262
- **section 1, line 67:** - And again later. Shopify re-verifies periodically, and re-checks bank ownership when a payout account is added or replaced or business details change. Salla may ask for documents at any time, and Zid Pay's seller must report changes within a week. On BigCommerce, Stripe flags accounts for verification after a processing threshold. Q3-SH-066; Q3-SH-061; Q3-SA-051; Q3-ZD-078; Q3-BC-020
- **section 1, line 71:** - The store keeps working while a payment requirement is pending. On Shopify, the store stays usable while payouts are on hold. Salla lets the seller prepare the store and products before verification, a rejection leaves settings and products intact, and a verified store updating its data keeps taking orders and payments. Q3-SH-P0085; Q3-SA-016; Q3-SA-023; Q3-SA-006
- **section 1, line 74:** - Zid Pay gives 14 days to correct wrong data, then disables the account and returns all amounts to end customers. Salla suspends payments and settlement "بعد انتهاء المهلة", a period whose length was not in what was read. WooPayments may restrict payments or payouts once a deadline for missing information passes. Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01; Q3-WC-P0055
- **section 1, line 75:** - Returning buyers' money matches on role across kinds: Zid Pay's terms (official page), Shopify's European and UK help page (stated), and Salla's agreement, which allows returning pending electronic payments to consumers for a breach of its tenth article (official page). Q3-ZD-P0012; Q3-SH-072; Q3-SA-P0083
- **section 1, line 76:** - Each records the state, a match on role across kinds: Shopify's ShopifyPaymentsAccount has a field for whether setup is completed (developer documentation, stated); Salla's payments answer carries `blocks_payment_activation` and each method's `blocked_by` (observed, store merchant, 8 October 2026); WooCommerce's shipped code gives an onboarding step a blocked status; and BigCommerce shows tasks and fund holds in its Actions section (stated). On Shopify store ibx5bt-xy, the saved markup of the Subscribe to Plus step, observed 30 September 2026, says "Shopify Payments is not available on your store.", as its accessibility tree did. Q3-SH-086; Q3-SA-073; Q3-SA-074; Q3-WC-041; Q3-BC-P0072; Q3-SH-108
- **section 2, line 82:** - **Business** (proposed): the legal entity behind one or more stores, with its **entity type** and its **registration place**, the place whose government documents it uses. These two choose each requirement set. The registration place comes from Salla's question for the country whose government documents the store uses (observed, Store 1, 8 October 2026) and WooPayments' country of registration; the entity types from Salla and Zid, whose requirements differ by entity type and country. Why: rule 1, since the place selects configuration rather than code, and rule 3. Q3-SA-085; Q3-WC-K0402; Q3-SA-056; Q3-ZD-K0239; Q3-ZD-K0240
- **section 2, line 87:** - **Capability status** (proposed): for each store and capability, available, blocked or restricted, with machine-readable reasons naming the unmet requirements. It takes Salla's `blocks_payment_activation`, `blocked_by` and `withdraw_disabled_reason`, WooCommerce's blocked onboarding step, and Shopify's field for setup completed. Why: rule 3, the data model. Q3-SA-073; Q3-SA-074; Q3-SA-077; Q3-WC-041; Q3-SH-086
- **section 2, line 89:** - **Requirement set** (proposed): the requirements one capability needs, for one registration place, entity type, plan and provider; configured, versioned and shown to the seller. It combines Salla's per-country verification (a UAE trade licence, Emirates IDs and an IBAN certificate; in Saudi Arabia, an Absher-matched ID and a citizens-only freelance document), Zid's per-entity and per-country requirements, and Shopify's per-country Proof of Liveness. Why: rule 1. Q3-SA-072; Q3-SA-014; Q3-SA-013; Q3-ZD-K0240; Q3-SH-041
- **section 2, line 91:** - **Submission** and **Review** (proposed): the seller gives information and documents inside Sharrwah and declares them true, as Salla's KYC schema requires; a review decides: pending, approved, rejected with reasons, or more needed. Each review has a checker, which is Sharrwah's team, a provider or an identity service, with its own attempt limits and timing, as Zid's team, Zid's gateway, and the daily attempts of Absher and Nafath show. Documents come only through Sharrwah, as Shopify accepts them only through its admin. Why: rule 2 for the checker, rule 3 for the data. Q3-SA-057; Q3-ZD-P0038; Q3-ZD-P0118; Q3-SA-008; Q3-ZD-K0262; Q3-SH-015
- **section 2, line 92:** - **Re-verification** (proposed): a met requirement is checked again when business details or the payout account change, at intervals, on request, or after a threshold; a duty to report changes within a set time is a per-place setting. While an update is reviewed, the met state holds and the store keeps taking orders and payments, as on Salla. Q3-SH-061; Q3-SH-066; Q3-SA-051; Q3-BC-020; Q3-ZD-078; Q3-SA-006
- **section 2, line 93:** - Not taken: a seller's declaration in place of any review, BigCommerce's way with products' legality. A declaration stays one requirement kind, used where a set calls for it. Q3-BC-K0460; Q3-SA-057
- **section 2, line 94:** - **Restriction** (proposed): what an unmet requirement does, scoped to the capability it gates: keep the store from buyers, block a payment method or checkout, allow only test payments (as store demo-fake-dev-store's saved markup, observed 30 September 2026, says of development stores), hold payouts, block withdrawals, or suspend the store. Each records its reason and the requirements it waits on, and lifts when they are met, as Shopify's pauses lift "automatically after you complete verification". It follows the narrow effects the platforms show: American Express alone stopping, other providers unaffected, the store usable while payouts are held, products kept after a rejection. Why: rule 2. Q3-SH-058; Q3-SH-073; Q3-SH-P0085; Q3-SA-023; Q3-SH-070; Q3-SH-106
- **section 2, line 97:** - Not taken: one store-wide check blocking all selling until met, as Salla's Basic stores show with verification "متطلب أساسي للبدء في عملية البيع". It ties every capability to one check; the design can still express it as the requirement set for opening the store. Q3-SA-001
- **section 3, line 110:** - Government services whose records a requirement may ask for: the Business Platform (منصة الأعمال), whose licence Salla keeps apart from its own verification, and SPL's national address, which Zid asks for to activate services such as payments. Q3-SA-037; Q3-ZD-039
- **section 3, line 114:** - Per registration place: the documents and checks, as on Salla by country, on Zid by country, and for Shopify's Proof of Liveness. Q3-SA-072; Q3-ZD-K0240; Q3-SH-041
- **section 3, line 125:** - Sharrwah: its own requirement sets, such as its review, its plans and its selling policy, as Salla's own verification and selling policy show. Q3-SA-037; Q3-SA-054
- **section 3, line 128:** - Authorities and the law, as the platforms report them: licences on Zid, and the e-commerce law's obligations on Salla. These show what the platforms require of their sellers, not what any law requires of Sharrwah. Q3-ZD-023; Q3-SA-033
- **section 5, line 145:** - Who checks a seller before payments in a place: Sharrwah's own review (Salla), a gateway's approval (Zid), a partner's check (Stripe for WooPayments, Shopify's banking partners), or more than one. It is costly to change, being legal structure and partner contracts, and a partner's check may not reach a place, as for Yemen. Keep open: the checker as a plug-in and the setter on every requirement, with no single path built in. Settled by the company decisions on providers and on Sharrwah's own position (section 7). Q3-SA-037; Q3-ZD-P0118; Q3-WC-012; Q3-SH-012; YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 5, line 146:** - What unmet requirements do to money: holding payouts, blocking withdrawals, returning payments to buyers, and the days between, as Shopify, Zid and Salla show them; Salla's period was not in what was read. Keep open, as a money flow: a restriction type for each, with schedules per place, all off until decided. Settled by the founder's decision under the guard, Q5's proposal and providers' terms. Q3-SH-072; Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01
- **section 5, line 147:** - Which place selects a requirement set, and what moving it costs: the country of the documents (Salla), of registration (WooPayments), or of the business's location (Shopify). Yemen adds places below a country, where two areas set one requirement differently. Keep open: a registration place that can name an area within a country, kept apart from the store's selling places, and rules for moving it, such as Zid's zero balance first. Settled by the proposals for Q1 and Q6. Q3-SA-085; Q3-WC-K0402; Q3-SH-K1536; Q3-ZD-K0230; YA-150 (within thirty days of founding or licensing @ Houthis' area, as of 2026-10-10); YA-150 (within sixty days of starting its activity @ the unified Republic's area, as of 1991)
- **section 7, line 168:** - Whether Sharrwah checks sellers itself, relies on payment providers' checks, or both, and in which places. Q3-SA-037; Q3-ZD-P0118; Q3-WC-012
- **section 7, line 170:** - Who may register and take payments, by entity type and nationality, as Salla verifies a foreign merchant's store only with a Saudi commercial registration. Q3-SA-005; Q3-SA-014
- **section 7, line 172:** - Whether Sharrwah reviews products against licences or takes the seller's declaration, and who answers when a product breaks a law. Q3-BC-K0460; Q3-SA-057; Q3-SH-053
- **section 7, line 175:** - Sharrwah's own legal position in checking sellers and in returning buyers' payments, for the founder with a lawyer. Q3-SA-037; Q3-SH-072

## The cards

### Q3-SA-056

**Cited at:** section 1, line 51; section 2, line 82

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-056
- bears_on: 1
- identifier: government_documents.entity_type
- statement: "options":[{"label":"single establishment option","value":"single"},{"label":"company option","value":"company"},{"label":"institution option","value":"institution"},{"label":"charity option","value":"charity"},{"label":"government option","value":"government"}]
- scope: merchants_saudi_kyc
- cite_ids: Q3-SA-C117
- from: held

**Citation Q3-SA-C117:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/kyc-schema/demo@en/source.json` | data.renderer_schema.states.government_documents (entity type select) | 2026-10-08 | kind: observed | quote check: found
- quote: "options":[{"label":"single establishment option","value":"single"},{"label":"company option","value":"company"},{"label":"institution option","value":"institution"},{"label":"charity option","value":"charity"},{"label":"government option","value":"government"}]
- in context: …ment documents"},{"id":3,"label":"bank account"},{"id":4,"label":"review and confirm"}],"value":2}},{"type":"section","options":{"className":"w-full space-y-2"},"children":[{"type":"h4","options":{"className":"text-primary font-medium text-lg"},"children":["government documents"]}]},{"type":"fieldset","options":{"className":"w-full space-y-4"},"children":[{"type":"select","options":{"name":"government_documents.entity_type","label":"entity type",⟪"options":[{"label":"single establishment option","value":"single"},{"label":"company option","value":"company"},{"label":"institution option","value":"institution"},{"label":"charity option","value":"charity"},{"label":"government option","value":"government"}]⟫,"required":true,"placeholder":"select entity type"}},{"type":"div","options":{"className":"w-full space-y-4","visibleOn":{"or":[{"==":[{"var":"government_documents.entity_type"},"company"]},{"==":[{"var":"government_documents.entity_type"},"institution"]}]}},"children":[{"type":"textinput","options":{"name":"government_documents.commercial_registration_number","type":"text","label":"commercial registration number","required":true,"placeholder":"…

### Q3-SA-037

**Cited at:** section 1, line 59; section 3, line 110; section 3, line 125; section 5, line 145; section 7, line 168; section 7, line 175

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-037
- bears_on: 4
- identifier: ❓ ما الفرق بين التوثيق في سلة وتوثيق منصة الأعمال؟
- statement: التوثيق في سلة هو إجراء تشغيلي داخلي لتفعيل بوابات الدفع والحساب البنكي، بينما توثيق منصة الأعمال هو ترخيص حكومي رسمي يُظهر متجرك كمنشأة معتمدة لدى وزارة التجارة والمركز السعودي للأعمال.
- cite_ids: Q3-SA-C070
- from: held

**Citation Q3-SA-C070:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1150 (article poppbr8akg1iqlr2798u8gfz, شهادة توثيق التجارة الإلكترونية: الإصدار والتجديد) | 2026-08-29 | kind: stated | quote check: found
- quote: التوثيق في سلة هو إجراء تشغيلي داخلي لتفعيل بوابات الدفع والحساب البنكي، بينما توثيق منصة الأعمال هو ترخيص حكومي رسمي يُظهر متجرك كمنشأة معتمدة لدى وزارة التجارة والمركز السعودي للأعمال.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ثيق الظاهر في أسفل متجرك أو بالبحث برقم الشهادة في استعلامات المركز السعودي للأعمال. أسئلة شائعة حول توثيق منصة الأعمال ❓ كم رسوم إصدار شهادة توثيق التجارة الإلكترونية؟ خدمة إصدار شهادة التوثيق عبر منصة الأعمال مجانية 100% وبدون أي رسوم حكومية. ❓ هل يلزم وجود سجل تجاري لإصدار الشهادة؟ لا، يمكنك إصدار شهادة توثيق التجارة الإلكترونية بواسطة **وثيقة العمل الحر** الصادرة للأفراد من منصة العمل الحر . ❓ ما الفرق بين التوثيق في سلة وتوثيق منصة الأعمال؟ ⟪التوثيق في سلة هو إجراء تشغيلي داخلي لتفعيل بوابات الدفع والحساب البنكي، بينما توثيق منصة الأعمال هو ترخيص حكومي رسمي يُظهر متجرك كمنشأة معتمدة لدى وزارة التجارة والمركز السعودي للأعمال.⟫ ✨ بإتمام توثيق متجرك في سلة وفي منصة الأعمال، تكتمل جاهزية متجرك للانطلاق والبيع برسمية وموثوقية كاملة. ابدأ الآن وربط شهادة التوثيق بمتجرك لتضمن ثقة عملائك ونمو تجارتك. aojzcev1o7dknew45lnah27y https://help.salla.sa/article/%D8%B4%D9%88%D8%A7%D9%87%D8%AF-%D9%84%D9%88%D8%AC%D8%B3%D8%AA%D9%8A%D9%83-shawahid-logistics-1/aojzcev1o7dknew45lnah27y تطبيق شواهد لوجستيك: شواهد لوجستيك هي شركة سعودية تقدّم خدمات الشحن والتوصيل داخل المملكة العربية السعود…

### Q3-SA-033

**Cited at:** section 1, line 61; section 3, line 128

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-033
- bears_on: 4
- identifier: تاسعاً. العقوبات
- statement: ملاحظة : جميع ما سبق مستمد من أحكام نظام التجارة الإلكترونية ودليل اشتراطات المتاجر الإلكترونية الصادر عن وزارة التجارة.
- cite_ids: Q3-SA-C058
- from: held

**Citation Q3-SA-C058:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 302 (article g0cbvwqncrfmptexs580y6f7, الالتزامات المفروضة على التاجر وممارس التجارة الإلكترونية) | 2026-08-18 | kind: stated | quote check: found
- quote: ملاحظة : جميع ما سبق مستمد من أحكام نظام التجارة الإلكترونية ودليل اشتراطات المتاجر الإلكترونية الصادر عن وزارة التجارة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …أو تنفيذ السلعة لأكثر من 15 يوم يحق للمستهلك إلغاء الطلب. على التاجر الالتزام بأحكام إتفاقية الاستخدام الخاصة بمنصة سلة وبأحكام نظام التجارة الإلكترونية وعدم مخالفتها. تاسعاً. العقوبات يُعاقب كل من يخالف أياً من أحكام النظام أو اللائحة بواحدة أو أكثر من العقوبات الآتية: الإنذار. غرامة مالية تصل إلى مليون ريال. إيقاف مزاولة التجارة الإلكترونية مؤقتاً أو دائماً. حجب المتجر الإلكتروني - بالتنسيق مع الجهة المختصة - جزئياً أو كلياً، مؤقتاً أو دائماً. ⟪ملاحظة : جميع ما سبق مستمد من أحكام نظام التجارة الإلكترونية ودليل اشتراطات المتاجر الإلكترونية الصادر عن وزارة التجارة.⟫ لمزيد من التفاصيل حول أبرز المواد التي تضمنها قانون التجارة الإلكترونية الأسئلة الشائعة هل البيع على سلة يحتاج سجل تجاري؟ وقد يسأل آخرون: هل يمكن فتح متجر إلكتروني بدون سجل تجاري؟ هل المتجر الإلكتروني يحتاج سجل تجاري؟ يمكنك البدء بنشاط التجارة الإلكترونية على سلة بعد الحصول على سجل تجاري في المملكة أو شهادة العمل الحر (فرد أو أسرة منتجة) raxpa40e0dduc83xmpa4xlh2 https://help.salla.sa/article/%D8%A7%D9%84%D8%A7%D9%85%D9%8A%D8%A7%D9%84-%D8%A7%D9%8…

### Q3-SA-003

**Cited at:** section 1, line 65

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-003
- bears_on: 4
- identifier: ❓ كم يأخذ توثيق المتجر في سلة؟
- statement: مدة توثيق المتجر من 24 إلى 48 ساعة، إذا تأخر عن ذلك تواصل مع الدعم الفني لسلة من لوحة تحكم متجرك
- cite_ids: Q3-SA-C003
- from: held

**Citation Q3-SA-C003:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: مدة توثيق المتجر من 24 إلى 48 ساعة، إذا تأخر عن ذلك تواصل مع الدعم الفني لسلة من لوحة تحكم متجرك
- in context: …ساب مباشرة. ❓ ما هي النتائج المحتملة لعدم التحقق من صحة بيانات لمتجري؟ سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر. ❓ هل يطلع أحد على معلومات متجري، أم التحقق من صحة البيانات فقط لتوثيق المتجر؟ التحقق من أجل توثيق صحة بيانات المتجر ولا يمكن للعملاء الاطلاع على بيانات متجرك ❓ هل ملف ال Pdf مدعوم في التحقق من صحة البيانات ؟ يمكن رفعه ولكنه يستغرق وقتاً أطول، يفضّل رفع صورة. ❓ كم يأخذ توثيق المتجر في سلة؟ ⟪مدة توثيق المتجر من 24 إلى 48 ساعة، إذا تأخر عن ذلك تواصل مع الدعم الفني لسلة من لوحة تحكم متجرك⟫ ❓ ماهي قنوات اشعار التاجر بحالات التوثيق؟ بجانب اشعارات لوحة التحكم، سيصل للتاجر اشعار عبر البريد الالكتروني والواتس اب، مع توضيح سبب الرفض في حال رفض طلب التوثيق ❓ كيف يمكنني تحديث بيانات حسابي البنكي في صفحة توثيق لمتجر ؟ يمكنك من خلال رفع طلب توثيق جديد بالحساب البنكي الجديد، علماً بأن متجرك سيستمر في استقبال الطلبات والمدفوعات. ❓ كيف يُعامل طلب التوثيق لمتجر اكتمل توثيقه بنجاح سابقاً؟ عند تحديث بيانات توثيق لمتجر سبق توثيقه بنجاح، سيتم: يستم…

### Q3-SA-008

**Cited at:** section 1, line 66; section 2, line 91

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-008
- bears_on: 4
- identifier: ❓ في حال فشل توثيق متجري على ابشر، كم مرة يمكنني المحاولة؟
- statement: التوثيق عبر منصة ابشر يمكنك المحاولة ثلاثة مرات في اليوم، البيانات الأخرى لا يوجد عدد محدود للمحاولة.
- cite_ids: Q3-SA-C009
- from: held

**Citation Q3-SA-C009:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: التوثيق عبر منصة ابشر يمكنك المحاولة ثلاثة مرات في اليوم، البيانات الأخرى لا يوجد عدد محدود للمحاولة.
- in context: … وأن تكون واضحة بشكل كامل. شهادة منصة الأعمال لا تنتمي لمالك التاجر، يجب عليك ارفاق شهادة منصة الأعمال التي تعود لاسم مالك المتجر. الحساب البنكي الموجود في منصة الأعمال لا يطابق الحساب البنكي اللي تم ارفاقه من قبل التاجر، يجب عليك تعديل رقم الحساب البنكي بحيث يطابق الحساب المرفق في منصة الأعمال. ❓ كيف يمكنني إضافة معلومات تواصل إلى متجري؟ من صفحة (تخصيص الثيم)، من قسم رأس وتذييل الصفحة . ❓ في حال فشل توثيق متجري على ابشر، كم مرة يمكنني المحاولة؟ ⟪التوثيق عبر منصة ابشر يمكنك المحاولة ثلاثة مرات في اليوم، البيانات الأخرى لا يوجد عدد محدود للمحاولة.⟫ ❓ في حال كان لدى التاجر أكثر من متجر، هل يمكن له التحقق من صحة بيانات جميع متاجره على سلة باستخدام نفس البيانات؟ وهل يوجد حد أقصى لعدد المتاجر التي تم التحقق من صحة بياناتها؟ نعم يمكن إدخال نفس البيانات إذا كان مالك المتاجر هو نفس الشخص، ولا يوجد حد أعلى لعدد المتاجر التابعة لمالك واحد. ❓ في حال نوع الكيان فرد، ولدى التاجر متجرين، ومجموع مبيعاتهما معاً أكثر من 375 ألف ريال سنوياً، هل سيتم تطبيق قيمة الضريبة بشكل منفصل على كل متجر أم يتم معاملتهم…

### Q3-SA-051

**Cited at:** section 1, line 67; section 2, line 92

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-051
- bears_on: 1;4
- identifier: المادة الخامسة – الحسابات والتزامات التسجيل
- statement: .لمنصة سلّة الحق في أي وقت في أن تجري أي تحقيقات تراها ضرورية سواء كانت مباشرة أو عبر طرف ثالث، وتطالبك بالإفصاح عن أي معلومات إضافية أو وثائق مهما كان حجمها لإثبات هويتك أو ملكيتك لأموالك أو للحساب الخاص بك.
- cite_ids: Q3-SA-C101
- from: held

**Citation Q3-SA-C101:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 70 (المادة الخامسة – الحسابات والتزامات التسجيل) | 2026-10-06 | kind: official page | quote check: found
- quote: .لمنصة سلّة الحق في أي وقت في أن تجري أي تحقيقات تراها ضرورية سواء كانت مباشرة أو عبر طرف ثالث، وتطالبك بالإفصاح عن أي معلومات إضافية أو وثائق مهما كان حجمها لإثبات هويتك أو ملكيتك لأموالك أو للحساب الخاص بك.
- in context: …ومات المعمول بها لدى منصة سلة. .أنت ملزمًا بالحفاظ على بيانات التسجيل وتحديثها دائمًا لإبقائها حقيقية وصحيحة وراهنة وكاملة وقانونية، وإذا أفصحت عن معلومات غير حقيقية أو غير صحيحة أو غير راهنة أو غير كاملة أو غير قانونية أو مخالفة لما جاء في اتفاقية الاستخدام، فإن منصة سلّة تمتلك الحق في وقف أو تجميد أو إلغاء عضويتك أو متجرك وحسابك في المنصة، وذلك دون إلحاق الأضرار بحقوق منصة سلّة الأخرى ووسائلها المشروعة في استرداد حقوقها وحماية باقي المستخدمين. ⟪.لمنصة سلّة الحق في أي وقت في أن تجري أي تحقيقات تراها ضرورية سواء كانت مباشرة أو عبر طرف ثالث، وتطالبك بالإفصاح عن أي معلومات إضافية أو وثائق مهما كان حجمها لإثبات هويتك أو ملكيتك لأموالك أو للحساب الخاص بك.⟫ .في حالة عدم الالتزام بأي مما ورد أعلاه فإن لإدارة منصة سلّة الحق في إيقاف أو إلغاء متجرك أو عضويتك أو حجبك من الولوج لخدمات منصة سلة مرة أخرى. وتحتفظ كذلك بالحق في إلغاء أي حسابات غير مؤكدة وغير مثبتة أو عمليات أو حسابات مر عليها مدة طويلة دون نشاط. المادة السادسة - الاتصالات الإلكترونية ووسائل التواصل الرسمية: يوافق التاجر في منصة سلّة على أن يتم التواصل معه عبر البريد الإلكتروني، أو من خلال قيام إدارة منصة سلّة ببث رسائل عامة ترد إلى كافة الم…

### Q3-SA-016

**Cited at:** section 1, line 71

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-016
- bears_on: 2;4
- identifier: ❓ هل يمكنني البيع قبل اكتمال التوثيق؟
- statement: يمكنك تجهيز متجرك ومنتجاتك، لكن تفعيل بوابات الدفع واستقبال المبالغ يتطلب اكتمال التوثيق.
- cite_ids: Q3-SA-C032
- from: held

**Citation Q3-SA-C032:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1346 (article evrib312myg7282hjg7nlrje, متطلبات توثيق المتجر في سلة وأسباب رفض الطلب) | 2026-08-29 | kind: stated | quote check: found
- quote: يمكنك تجهيز متجرك ومنتجاتك، لكن تفعيل بوابات الدفع واستقبال المبالغ يتطلب اكتمال التوثيق.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …كرار إدخال بيانات خاطئة راجع الحقول قبل كل إرسال - التكرار قد يؤدي إلى رفض الطلب بشكل نهائي عدم اكتمال المتطلبات أكمل قائمة التحقق أعلاه قبل بدء الطلب لتفادي توقف العملية في منتصفها بعد إرسال الطلب يراجع فريق سلة بياناتك ومستنداتك. عند اكتمال البيانات وصحتها يُعتمد الطلب. تصلك رسالة تفيد بأنه تم توثيق متجرك بنجاح 🎉 وفي حال الرفض أو طلب تعديل، يمكنك تحديث البيانات وإعادة الإرسال دون البدء من جديد. أسئلة شائعة ❓ هل يمكنني البيع قبل اكتمال التوثيق؟ ⟪يمكنك تجهيز متجرك ومنتجاتك، لكن تفعيل بوابات الدفع واستقبال المبالغ يتطلب اكتمال التوثيق.⟫ ❓ هل يمكن استخدام حساب بنكي باسم أحد أفراد العائلة؟ لا. يجب أن يكون الحساب باسم مالك المتجر نفسه للفرد، أو باسم الكيان التجاري للمؤسسات والشركات. ❓ ماذا أفعل إن رُفض طلبي؟ راجع سبب الرفض في الإشعار، صحّح الحقل أو المستند المعني، ثم أعد إرسال الطلب - لا حاجة لإعادة إدخال كل البيانات. ❓ هل التوثيق مطلوب لكل متجر؟ نعم، فهو شرط أساسي لتشغيل المتجر رسمياً وتفعيل خدمات الدفع والشحن. ❓ كم يستغرق التوثيق؟ تختلف مدة المراجعة حسب اكتمال البيانات ودقتها، و…

### Q3-SA-023

**Cited at:** section 1, line 71; section 2, line 94

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-023
- bears_on: 4
- identifier: ❓ هل يؤدي رفض التوثيق إلى حذف المتجر أو خسارة البيانات؟
- statement: لا، لا يؤثر الرفض على إعدادات متجرك أو منتجاتك أو تصميمك مطلقاً. هو فقط إيقاف مؤقت لتفعيل المدفوعات لحين تصحيح مستند التوثيق.
- cite_ids: Q3-SA-C045
- from: held

**Citation Q3-SA-C045:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 30 (article ndz1k0tts5p7gfnqqxcubspl, أسباب رفض توثيق المتجر في سلة وطريقة حل كل حالة) | 2026-08-29 | kind: stated | quote check: found
- quote: لا، لا يؤثر الرفض على إعدادات متجرك أو منتجاتك أو تصميمك مطلقاً. هو فقط إيقاف مؤقت لتفعيل المدفوعات لحين تصحيح مستند التوثيق.
- in context: …فق بالنسخة الجديدة الواضحة. 4. راجع كافة الخطوات البنكية والشخصية واضغط على (إعادة إرسال الطلب) . 5. سيقوم فريق مراجعة سلة بفحص التعديل والموافقة عليه خلال مدة قصيرة لتفعيل متجرك فورياً. أسئلة شائعة حول رفض وتعديل التوثيق ❓ كم يستغرق رد الفريق بعد إعادة إرسال طلب التوثيق المعدل؟ تتم مراجعة الطلبات المعدلة بسرعة، وغالباً ما يتم الرد بالاعتماد القاطعي خلال عدة ساعات وحتى 24 ساعة عمل كحد أقصى. ❓ هل يؤدي رفض التوثيق إلى حذف المتجر أو خسارة البيانات؟ ⟪لا، لا يؤثر الرفض على إعدادات متجرك أو منتجاتك أو تصميمك مطلقاً. هو فقط إيقاف مؤقت لتفعيل المدفوعات لحين تصحيح مستند التوثيق.⟫ ❓ ماذا أفعل إذا تكرر رفض الطلب رغم تعديل البيانات؟ تواصل مباشر مع فريق الدعم الفني في سلة عبر المحادثة المباشرة في لوحة التحكم، وسيقوم ممثل الدعم بتوجيهك للمستند الدقيق المطلوب قبوله. ✨ بتصحيح بيانات التوثيق وفق الملاحظات الواردة، يكتمل توثيق متجرك بنجاح لتنطلق في استقبال المبيعات والتسويات المالية بكل أمان. راجع طلبك الآن وأعد الإرسال لبدء البيع فوراً. c4t9zj8cnotfaa1a2opd8n0f https://help.salla.sa/article/%D8%A3%D8%B3%D8%B9%D8%A7%D8%B1-%D8%A8%…

### Q3-SA-006

**Cited at:** section 1, line 71; section 2, line 92

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-006
- bears_on: 4
- identifier: ❓ كيف يُعامل طلب التوثيق لمتجر اكتمل توثيقه بنجاح سابقاً؟
- statement: يستمر عمل المتجر دون تعطيل لاستقبال الطلبات أو المدفوعات الإلكترونية.
- scope: عند تحديث بيانات توثيق لمتجر سبق توثيقه بنجاح
- cite_ids: Q3-SA-C007
- from: held

**Citation Q3-SA-C007:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: يستمر عمل المتجر دون تعطيل لاستقبال الطلبات أو المدفوعات الإلكترونية.
- in context: …تجرك ❓ ماهي قنوات اشعار التاجر بحالات التوثيق؟ بجانب اشعارات لوحة التحكم، سيصل للتاجر اشعار عبر البريد الالكتروني والواتس اب، مع توضيح سبب الرفض في حال رفض طلب التوثيق ❓ كيف يمكنني تحديث بيانات حسابي البنكي في صفحة توثيق لمتجر ؟ يمكنك من خلال رفع طلب توثيق جديد بالحساب البنكي الجديد، علماً بأن متجرك سيستمر في استقبال الطلبات والمدفوعات. ❓ كيف يُعامل طلب التوثيق لمتجر اكتمل توثيقه بنجاح سابقاً؟ عند تحديث بيانات توثيق لمتجر سبق توثيقه بنجاح، سيتم: ⟪يستمر عمل المتجر دون تعطيل لاستقبال الطلبات أو المدفوعات الإلكترونية.⟫ لن يتم تحديث الطلب القديم وإنما سيُرسل طلب توثيق جديد تماماً إلى مرحلة التحقق من الفريق المختص. قبول أو رفض طلب التوثيق: قبول طلب التوثيق الجديد وإبلاغ التاجر بإن طلب التوثيق الجديد أصبح مكتملاً رفض طلب التوثيق الجديد وإبلاغ التاجر بالأسباب، والاحتفاظ بحالة التوثيق المكتمل من الطلب السابق. ❓ ما الأسباب المحتملة لفشل توثيق متجري؟ بطاقة الهوية منتهية الصلاحية، يجب عليك توثيق المتجر بهوية سارية لمالك المتجر بطاقة الهوية غير واضحة، يجب عليك توثيق ال…

### Q3-SA-002

**Cited at:** section 1, line 74; section 5, line 146

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-002
- bears_on: 4
- identifier: ❓ ما هي النتائج المحتملة لعدم التحقق من صحة بيانات لمتجري؟
- statement: سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر.
- cite_ids: Q3-SA-C002
- from: held

**Citation Q3-SA-C002:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر.
- in context: …يكون باسم مالك المتجر وصاحب وثيقة العمل الحر (للكيان الفردي). 3- للمؤسسات: يجب أن تتطابق بيانات الحساب مع السجل التجاري والهوية الوطنية. ❓ماذا يحدث إذا كان البنك لا يدعم التحقق التلقائي؟ في هذه الحالة، يمكنك إدخال بيانات الحساب البنكي يدوياً، وسيتم التحقق منها من قبل فريق الدعم في سلة. ❓ هل يظهر اسم صاحب الحساب بعد التحقق؟ نعم ، في حال نجاح التحقق، يظهر الاسم الثلاثي لصاحب الحساب مباشرة. ❓ ما هي النتائج المحتملة لعدم التحقق من صحة بيانات لمتجري؟ ⟪سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر.⟫ ❓ هل يطلع أحد على معلومات متجري، أم التحقق من صحة البيانات فقط لتوثيق المتجر؟ التحقق من أجل توثيق صحة بيانات المتجر ولا يمكن للعملاء الاطلاع على بيانات متجرك ❓ هل ملف ال Pdf مدعوم في التحقق من صحة البيانات ؟ يمكن رفعه ولكنه يستغرق وقتاً أطول، يفضّل رفع صورة. ❓ كم يأخذ توثيق المتجر في سلة؟ مدة توثيق المتجر من 24 إلى 48 ساعة، إذا تأخر عن ذلك تواصل مع الدعم الفني لسلة من لوحة تحكم متجرك ❓ ماهي قنوات اشعار التاجر بحالات التوثيق؟ بجانب اشعارات لوحة ا…

### Q3-SA-P0083

**Cited at:** section 1, line 75

**Record** (`studies/proposals/records/Q3/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-082
- bullet: a;c
- placement: decides
- identifier: المادة العاشرة – تعهد التاجر بـالالتزام بالقوانين والأنظمة في المملكة العربية السعودية
- statement: في حال مخالفة أي من التجار لما ورد في البند الأول من المادة العاشرة فإنه يقر بحق منصة سلة في اتخاذ أي من الاجراءات التالية وهي على سبيل المثال لا الحصر: التنبيه، إيقاف الخدمة وإغلاق المتجر، إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين.
- cite_ids: S01-SA-C086
- from: new

**Citation S01-SA-C086:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 98 (المادة العاشرة – تعهد التاجر بـالالتزام بالقوانين والأنظمة في المملكة العربية السعودية) | 2026-10-06 | kind: official page | quote check: found
- quote: في حال مخالفة أي من التجار لما ورد في البند الأول من المادة العاشرة فإنه يقر بحق منصة سلة في اتخاذ أي من الاجراءات التالية وهي على سبيل المثال لا الحصر: التنبيه، إيقاف الخدمة وإغلاق المتجر، إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين.
- in context: …ات المتاجر والتجار لقواعد "سياسة الخصوصية وسرية المعلومات" الخاصة بمنصة سلة. المادة العاشرة - تعهد التاجر بالالتزام بالقوانين والأنظمة في المملكة العربية السعودية : يتعهّد التاجر بالالتزام بكافة القوانين والأنظمة المعمول بها داخل المملكة العربية السعودية حيال منتجاته أو/وأثناء استخدامه لمنصة سلّة، وللقوانين والشروط والأحكام المعمول بها والمُنظِّمة لاستخدام فضاء الإنترنت واتفاقية الاستخدام وسياسة الخصوصية وسرية المعلومات المعمول بها لدى منصة سلة. ⟪في حال مخالفة أي من التجار لما ورد في البند الأول من المادة العاشرة فإنه يقر بحق منصة سلة في اتخاذ أي من الاجراءات التالية وهي على سبيل المثال لا الحصر: التنبيه، إيقاف الخدمة وإغلاق المتجر، إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين.⟫ المادة الحادية عشرة - الحقوق: كافة المحتويات المتواجدة على منصة سلّة، إلكترونية كانت أو غير ذلك، مكتوبة أو غير مكتوبة، على سبيل المثال لا الحصر: النصوص المكتوبة وغير المكتوبة - التصاميم الجرافيكية - الأفكار التقنية - الشعارات - العروض - أيقونات الأزرار - الرموز - المقاطع الصوتية - البيانات المجمّعة والبرامج الإلكترونية، هي ملك لمنصة سلّة وحقوقها محفوظة لمنصة سلّة، ولا يحق لكائنًا من كان أن يستخدمها بأي شكل من الأشكال سواء كان استخدام مباشر أو غي…

### Q3-SA-073

**Cited at:** section 1, line 76; section 2, line 87

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-073
- bears_on: 2;4
- identifier: GET /admin/v2/gateways/payment: data.verification
- statement: "verification": {"status": "uncompleted", "is_owner": true, "blocks_payment_activation": true, "verify_url": "https://s.salla.sa/entity/verification/verify", "summary": {"store_documented": false, "kyc_complete": false, "has_approved_epayment_request": false}, "rejection": null}
- scope: store merchant, observed 2026-10-08; بيسك
- cite_ids: Q3-SA-C160;Q3-SA-C158
- from: held

**Citation Q3-SA-C160:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1683.json` | GET api.salla.dev/admin/v2/gateways/payment, store merchant, step 71 | 2026-10-08 | kind: observed | quote check: found
- quote: "verification": {"status": "uncompleted", "is_owner": true, "blocks_payment_activation": true, "verify_url": "https://s.salla.sa/entity/verification/verify", "summary": {"store_documented": false, "kyc_complete": false, "has_approved_epayment_request": false}, "rejection": null}
- in context: …ssets.salla.network/prod/admin/cp/assets/images/emkan.png uncompleted mokafaa-alrajhi other_payment_method مكافآت الراجحي https://cdn.assets.salla.network/prod/admin/cp/assets/images/mokafaa-alrajhi.png uncompleted cod other_payment_method الدفع عند الاستلام https://cdn.assets.salla.network/prod/admin/cp/assets/images/cod.png uncompleted {"status": 200, "success": true, "data": {"master": {"epayment_enabled": false}, "is_first_time_setup": true, ⟪"verification": {"status": "uncompleted", "is_owner": true, "blocks_payment_activation": true, "verify_url": "https://s.salla.sa/entity/verification/verify", "summary": {"store_documented": false, "kyc_complete": false, "has_approved_epayment_request": false}, "rejection": null}⟫, "merchant_type": "KSA", "quick_methods": [{"slug": "mada", "is_enabled": false, "is_available": true, "is_effective": false, "blocked_by": "requires_paid_plan", "unavailable_reason": "قم بترقية باقتك لتفعيل المدفوعات الإلكترونية", "has_advance_settings": false, "label": "مدى", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/mada.png", "description": null, "fees": {"percentage": 1, "flat_amount": "1.00", "currency": "SAR"},…

**Citation Q3-SA-C158:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.text.txt` | step 76 | 2026-10-08 | kind: observed | quote check: found
- step 76: sweep (Arabic): main navigation: توثيق المتجر — /payments/kyc | https://s.salla.sa/payments/kyc | "سلة | توثيق المتجر" | 2026-10-08T12:44:04.174Z
- the step's files: `observed-sa@4ca2e896a:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.aria.yaml`, `observed-sa@4ca2e896a:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.text.txt`
- quote: Hamza بيسك
- in context: الكل الرئيسية الطلبات المنتجات التسويق المتجر وقنوات البيع التقارير ⟪Hamza بيسك⟫ طرق الدفع المحفظة قيود الدفع إدارة الضرائب عمليات الدفع الإلكتروني توثيق المتجر مشمر لتضمن توثيق متجرك بنجاح وبخطوات سريعة، يرجى تجهيز المتطلبات التالية 1. وثيقة العمل الحر للمواطنين السعوديين فقط الهوية: يجب أن تكون الهوية الوطنية لمالك المتجر سارية الصلاحية ومطابقة تماماً لبياناته في منصة أبشر. الوثيقة المطلوبة: وثيقة عمل حر سارية تابعة لمالك المتجر. الحساب البنكي: يجب أن يكون الحساب البنكي مطابقاً ل: • هوية مالك المتجر. • أو وثيقة العمل الحر …

### Q3-SA-085

**Cited at:** section 2, line 82; section 5, line 147

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-085
- bears_on: 1
- identifier: GET /admin/v2/onboarding/persona-country: data
- statement: "slug": "store-country", "question": "من أي دولة تسجِّل متجرك؟", "type": "main", "description": "اختر الدولة التي تصدر منها وثائقك الحكومية لتهيئة متجرك وفقًا لأنظمتها.", "is_mandatory": true
- scope: store "Store 1" (named by the run's GET /admin/v2/store/info answer), observed 2026-10-08; "plan": "basic", "kyc_country": "SA"
- cite_ids: Q3-SA-C180;Q3-SA-C176;Q3-SA-C177
- from: held

**Citation Q3-SA-C180:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T125139Z-sweep-merchant-routes-ar/responses/0535.json` | GET api.salla.dev/admin/v2/onboarding/persona-country, store not named in run.json, step 23 | 2026-10-08 | kind: observed | quote check: found
- quote: "slug": "store-country", "question": "من أي دولة تسجِّل متجرك؟", "type": "main", "description": "اختر الدولة التي تصدر منها وثائقك الحكومية لتهيئة متجرك وفقًا لأنظمتها.", "is_mandatory": true
- in context: store-country من أي دولة تسجِّل متجرك؟ main اختر الدولة التي تصدر منها وثائقك الحكومية لتهيئة متجرك وفقًا لأنظمتها. SA 🇸🇦 السعودية AE 🇦🇪 الإمارات KW 🇰🇼 الكويت QA 🇶🇦 قطر OM 🇴🇲 عمان BH 🇧🇭 البحرين other دولة أخرى {"status": 200, "success": true, "data": {⟪"slug": "store-country", "question": "من أي دولة تسجِّل متجرك؟", "type": "main", "description": "اختر الدولة التي تصدر منها وثائقك الحكومية لتهيئة متجرك وفقًا لأنظمتها.", "is_mandatory": true⟫, "options": [{"slug": "SA", "label": "🇸🇦 السعودية", "selected": false, "dependent_questions": []}, {"slug": "AE", "label": "🇦🇪 الإمارات", "selected": false, "dependent_questions": []}, {"slug": "KW", "label": "🇰🇼 الكويت", "selected": false, "dependent_questions": []}, {"slug": "QA", "label": "🇶🇦 قطر", "selected": false, "dependent_questions": []}, {"slug": "OM", "label": "🇴🇲 عمان", "selected": false, "dependent_questions": []}, {"slug": "BH", "l…

**Citation Q3-SA-C176:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T125139Z-sweep-merchant-routes-ar/responses/0709.json` | GET api.salla.dev/admin/v2/store/info, store not named in run.json, step 37 | 2026-10-08 | kind: observed | quote check: found
- quote: "name": "Store 1", "entity": "person", "type": "live"
- in context: Store 1 person live https://cdn.salla.sa/XeOVKD/stores/logos/5X4RlEPWC6lsf7I6ti5eFZwMwZYFFzpZtpqaWG9Q.jpg basic active SAR https://salla.sa/store-1-da SA Store 1 description {"status": 200, "success": true, "data": {"id": 60460195, ⟪"name": "Store 1", "entity": "person", "type": "live"⟫, "email": "", "avatar": "https://cdn.salla.sa/XeOVKD/stores/logos/5X4RlEPWC6lsf7I6ti5eFZwMwZYFFzpZtpqaWG9Q.jpg", "plan": "basic", "status": "active", "verified": false, "currency": "SAR", "domain": "https://salla.sa/store-1-da", "kyc_country": "SA", "description": "Store 1 description", "licenses": {"tax_number": null, "commercial_number": null, "freelance_number": null}, "social": {"telegram": "", "instagram": "", "tiktok": "", "twitter": "", "…

**Citation Q3-SA-C177:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T125139Z-sweep-merchant-routes-ar/responses/0709.json` | GET api.salla.dev/admin/v2/store/info, store not named in run.json, step 37 | 2026-10-08 | kind: observed | quote check: found
- quote: "plan": "basic", "status": "active", "verified": false, "currency": "SAR"
- title, opening and note boxes: as for this source's citation above
- in context: Store 1 person live https://cdn.salla.sa/XeOVKD/stores/logos/5X4RlEPWC6lsf7I6ti5eFZwMwZYFFzpZtpqaWG9Q.jpg basic active SAR https://salla.sa/store-1-da SA Store 1 description {"status": 200, "success": true, "data": {"id": 60460195, "name": "Store 1", "entity": "person", "type": "live", "email": "", "avatar": "https://cdn.salla.sa/XeOVKD/stores/logos/5X4RlEPWC6lsf7I6ti5eFZwMwZYFFzpZtpqaWG9Q.jpg", ⟪"plan": "basic", "status": "active", "verified": false, "currency": "SAR"⟫, "domain": "https://salla.sa/store-1-da", "kyc_country": "SA", "description": "Store 1 description", "licenses": {"tax_number": null, "commercial_number": null, "freelance_number": null}, "social": {"telegram": "", "instagram": "", "tiktok": "", "twitter": "", "facebook": "", "maroof": null, "youtube": "", "snapchat": "", "whatsapp": "", "appstore_link": null, "googleplay_link": null}}} {"status": 200, "success": true, "data": {"id": 60460195, "…

### Q3-SA-072

**Cited at:** section 2, line 89; section 3, line 114

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-072
- bears_on: 1;4
- identifier: ماذا تجهّز قبل البدء؟
- statement: جهّز ما الذي يجب التحقق منه الرخصة التجارية أو السجل التجاري سارية الصلاحية وغير منتهية. عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. الهوية الإماراتية وجواز السفر لكل مالك ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع التراخيص يمكن توفير الهوية البديلة ) شهادة الآيبان يجب أن تتضمن اسم البنك واسم صاحب الحساب ورقم الايبان.
- scope: توثيق متجرك في الإمارات
- cite_ids: Q3-SA-C146;Q3-SA-C147;Q3-SA-C148;Q3-SA-C149;Q3-SA-C150;Q3-SA-C151;Q3-SA-C152;Q3-SA-C153;Q3-SA-C154;Q3-SA-C155;Q3-SA-C156;Q3-SA-C157
- from: held
- note: Table of the documents to prepare (جهّز) and what is checked in each (ما الذي يجب التحقق منه), in source order.

**Citation Q3-SA-C146:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: جهّز
- in context: …/متابعة) بموافقتك https://salla.com/tools/ai-prompts/mcp-order-note-logger 24 مسترجع الفواتير يجلب فواتير طلباتك وينظّمها للمراجعة أو المحاسبة https://salla.com/tools/ai-prompts/mcp-invoice-retriever 25 تحديث المتجر الموسمي ي⟪جهّز⟫ متجرك لموسمٍ (هوية/واجهة/ثيم) ويطبّق التغييرات بموافقتك https://salla.com/tools/ai-prompts/mcp-seasonal-store-refresh 26 منسّق الصفحة الرئيسية يرتّب صفحتك الرئيسية لإبراز الأعلى ربحاً وطلباً ويطبّق الترتيب بموافقتك https://s…

**Citation Q3-SA-C147:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: ما الذي يجب التحقق منه
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …لإمارات، كما يتيح لك الانتقال إلى تفعيل المدفوعات الإلكترونية لعملائك. تمر عملية التوثيق بأربعة أقسام: تفاصيل النشاط، الملكية وإدارة المتجر، المعلومات البنكية، ثم المراجعة النهائية قبل إرسال الطلب. ماذا تجهّز قبل البدء؟ جهّز ⟪ما الذي يجب التحقق منه⟫ الرخصة التجارية أو السجل التجاري سارية الصلاحية وغير منتهية. عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نش…

**Citation Q3-SA-C148:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: الرخصة التجارية أو السجل التجاري
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … بأربعة أقسام: تفاصيل النشاط، الملكية وإدارة المتجر، المعلومات البنكية، ثم المراجعة النهائية قبل إرسال الطلب. ماذا تجهّز قبل البدء؟ تجهيز المستندات الصحيحة قبل البدء يجعل عملية التوثيق أسرع وأسهل. جهّز ما الذي يجب التحقق منه ⟪الرخصة التجارية أو السجل التجاري⟫ سارية الصلاحية وغير منتهية. مستخرج حديث من السجل التجاري يجب أن يتضمن بيانات المستفيد الفعلي للملّاك والمديرين المطلوبين في عملية التوثيق، بما في ذلك المدير حتى إن كانت نسبة ملكيته 0%. البطاقة المدنية وجواز السفر جهّز الوجه …

**Citation Q3-SA-C149:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: سارية الصلاحية وغير منتهية.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …رونية لعملائك. تمر عملية التوثيق بأربعة أقسام: تفاصيل النشاط، الملكية وإدارة المتجر، المعلومات البنكية، ثم المراجعة النهائية قبل إرسال الطلب. ماذا تجهّز قبل البدء؟ جهّز ما الذي يجب التحقق منه الرخصة التجارية أو السجل التجاري ⟪سارية الصلاحية وغير منتهية.⟫ عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. الهوية الإماراتية وجواز ا…

**Citation Q3-SA-C150:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …وثيق بأربعة أقسام: تفاصيل النشاط، الملكية وإدارة المتجر، المعلومات البنكية، ثم المراجعة النهائية قبل إرسال الطلب. ماذا تجهّز قبل البدء؟ جهّز ما الذي يجب التحقق منه الرخصة التجارية أو السجل التجاري سارية الصلاحية وغير منتهية. ⟪عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص⟫ مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. الهوية الإماراتية وجواز السفر لكل مالك ارفع الوجهين الأمامي والخلفي لكل هوية…

**Citation Q3-SA-C151:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …متجر، المعلومات البنكية، ثم المراجعة النهائية قبل إرسال الطلب. ماذا تجهّز قبل البدء؟ جهّز ما الذي يجب التحقق منه الرخصة التجارية أو السجل التجاري سارية الصلاحية وغير منتهية. عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص ⟪مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة.⟫ شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. الهوية الإماراتية وجواز السفر لكل مالك ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية.…

**Citation Q3-SA-C152:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN)
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … إرسال الطلب. ماذا تجهّز قبل البدء؟ جهّز ما الذي يجب التحقق منه الرخصة التجارية أو السجل التجاري سارية الصلاحية وغير منتهية. عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. ⟪شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN)⟫ فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. الهوية الإماراتية وجواز السفر لكل مالك ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع الترا…

**Citation Q3-SA-C153:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يجب التحقق منه الرخصة التجارية أو السجل التجاري سارية الصلاحية وغير منتهية. عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) ⟪فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة.⟫ الهوية الإماراتية وجواز السفر لكل مالك ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع التراخيص يمكن توفير الهوية البديلة ) شهادة الآيبان يجب …

**Citation Q3-SA-C154:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: الهوية الإماراتية وجواز السفر لكل مالك
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …رية الصلاحية وغير منتهية. عقد التأسيس أو النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. ⟪الهوية الإماراتية وجواز السفر لكل مالك⟫ ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع التراخيص يمكن توفير الهوية البديلة ) شهادة الآيبان يجب أن تتضمن اسم البنك واسم صاحب الحساب ورق…

**Citation Q3-SA-C155:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع التراخيص يمكن توفير الهوية البديلة )
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …و النظام الأساسي أو مستند توزيع الحصص مطلوب إذا لم تكن بيانات الملكية موضحة في الرخصة. شهادة التسجيل الضريبي ورقم التسجيل الضريبي (TRN) فقط إذا كان نشاطك مسجلًا في ضريبة القيمة المضافة. الهوية الإماراتية وجواز السفر لكل مالك ⟪ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع التراخيص يمكن توفير الهوية البديلة )⟫ شهادة الآيبان يجب أن تتضمن اسم البنك واسم صاحب الحساب ورقم الايبان. قاعدة بسيطة: أدخل جميع البيانات تمامًا كما تظهر في مستنداتك الرسمية. إذا اختلفت الكتابة، اعتمد دائمًا النسخة الموجودة في المستند الرسمي. كيفية فتح صفحة توثي…

**Citation Q3-SA-C156:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: شهادة الآيبان
- title, opening and note boxes: as for this source's citation above
- in context: …ا تمثل السجل التجاري، يجب عليك توثيق المتجر بشهادة سجل المؤسسة/الشركة سارية المفعول وتكون واضحة بشكل كامل. سجل المؤسسة / الشركة غير واضح، يجب عليك توثيق صورة سجل المؤسسة / الشركة بشكل واضح وكامل لأن الصورة المرفقة ليست كذلك. ⟪شهادة الآيبان⟫ ليست باسم مالك المتجر، يجب عليك إضافة الحساب البنكي وشهادة الآيبان المطابقة لمالك المتجر. الحساب البنكي لمؤسسة والكيان فرد، يجب عليك إضافة حساب بنكي شخصي وارفاق شهادة الايبان. الحساب البنكي شخصي والكيان مؤسسة/شركة، يجب عليك …

**Citation Q3-SA-C157:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 929 (article itmpqrf58xz73g2yyxfnllbz, توثيق متجرك في الإمارات | سلة ) | 2026-09-12 | kind: stated | quote check: found
- quote: يجب أن تتضمن اسم البنك واسم صاحب الحساب ورقم الايبان.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …افة. الهوية الإماراتية وجواز السفر لكل مالك ارفع الوجهين الأمامي والخلفي لكل هوية. يجب أن يكون كل من الهوية والجواز ساري الصلاحية. ( في حال عدم وجود هوية إماراتية لبعض أنواع التراخيص يمكن توفير الهوية البديلة ) شهادة الآيبان ⟪يجب أن تتضمن اسم البنك واسم صاحب الحساب ورقم الايبان.⟫ قاعدة بسيطة: أدخل جميع البيانات تمامًا كما تظهر في مستنداتك الرسمية. إذا اختلفت الكتابة، اعتمد دائمًا النسخة الموجودة في المستند الرسمي. كيفية فتح صفحة توثيق المتجر 1. من الصفحة الرئيسية لمتجرك، توجه إلى قسم (توثيق المتجر)، …

### Q3-SA-057

**Cited at:** section 2, line 91; section 2, line 93; section 7, line 172

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-057
- bears_on: 1;4
- identifier: review_confirm.truth_declaration
- statement: "truth_declaration":{"type":"boolean","one_of":[true],"required":"truth declaration required"}
- scope: merchants_saudi_kyc
- cite_ids: Q3-SA-C118
- from: held

**Citation Q3-SA-C118:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/kyc-schema/demo@en/source.json` | data.renderer_schema.validations.review_confirm | 2026-10-08 | kind: observed | quote check: found
- quote: "truth_declaration":{"type":"boolean","one_of":[true],"required":"truth declaration required"}
- in context: …INMA","NCBK","ALBI","RIBL","ARNB","BSFR","BJAZ","SIBC","GULF","SABB","RJHI"]]}]}]},{"!!":{"var":"iban_manual_fallback"}}]},"required":"account holder name required"},"bank_account_number":{"when":{"or":[{"and":[{"!!":[{"var":"bank"}]},{"!":[{"in":[{"var":"bank"},["INMA","NCBK","ALBI","RIBL","ARNB","BSFR","BJAZ","SIBC","GULF","SABB","RJHI"]]}]}]},{"!!":{"var":"iban_manual_fallback"}}]},"required":"bank account number required"}},"review_confirm":{⟪"truth_declaration":{"type":"boolean","one_of":[true],"required":"truth declaration required"}⟫},"bank_account_manual":{"bank":{"required":"bank required"},"iban":{"required":"iban required"},"iban_certificate":{"mimes":"jpeg,jpg,png,pdf","required":"iban certificate required","max_file_size":10485760},"account_holder_name":{"required":"account holder name required"},"bank_account_number":{"required":"bank account number required"}},"store_owner_details":{"owner_id":{"required":"owner id required"},"digital_id_image":{"mimes":"jpeg,jpg,png…

### Q3-SA-001

**Cited at:** section 2, line 97

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-001
- bears_on: 1;4
- identifier: ❓ ما الإجراء المتبع في حق متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟
- statement: التحقق متطلب أساسي للبدء في عملية البيع
- scope: متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها
- cite_ids: Q3-SA-C001
- from: held

**Citation Q3-SA-C001:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: التحقق متطلب أساسي للبدء في عملية البيع
- in context: … بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ قرار التحقق من صحة البيانات حكومي أم من شركة سلة؟ هي مبادرة من شركة سلة لتنظيم سوق التجارة الإلكترونية في المملكة العربية السعودية تهدف إلى رفع ثقة المستهلك بالمتاجر المسجّلة عبر منصة سلة وإلى توفير بيئة آمنة لممارسة التجارة الإلكترونية، ولا يغني ذلك عن التحقق من صحة بيانات أي من التجار لمتاجرهم لدى الجهات الحكومية. ❓ ما الإجراء المتبع في حق متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟ ⟪التحقق متطلب أساسي للبدء في عملية البيع⟫ ❓ هل يوجد مزامنة بين تفعيل الدفع والتحقق من صحة البيانات، وأيضاً نوع الكيان؟ نعم يوجد، ويجب أن تكون البيانات المدخلة متوافقة وصحيحة ويتم تدقيق كل الطلبات وفي حال إدخال بيانات خاطئة يتم رفض الطلب. ❓ هل يمكن رفع صورة من الهوية الرقمية ؟ نعم، تُقبل صورة الهوية الرقمية. ❓ في حال لم أوثق متجري هل ستُلغى طرق الدفع من متجري، أم أن الطلبات تستمر ولكن تحجز المبالغ؟ يتم تعليق عمليات الدفع والسداد إلى أن يتم إتمام خطوات توثيق المتجر. في حال احتجت مساعدة لت…

### Q3-SA-005

**Cited at:** section 7, line 170

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-005
- bears_on: 1;4
- identifier: ❓ في حال كان التاجر أجنبيّاً كيف يتم التحقق من صحة بيانات متجره؟
- statement: يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري. 📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات.
- cite_ids: Q3-SA-C005;Q3-SA-C006
- from: held

**Citation Q3-SA-C005:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري.
- in context: …نات الجمعية كيف سيتم التحقق من صحة البيانات لمالك المتجر في هذه الحالة؟ يحق للمؤسسة الوقفية تعيين ممثل نظامي كمستخدم للمتجر. ❓ عند التحقق من صحة البيانات لمتجر جمعية، من يعتبر مالك المتجر؟ ولماذا لا يتم تغيير المسمى من مالك المتجر إلى الصفة المطلوبة (رئيس مجلس، مدير تنفيذي، الخ) يعتبر اسم مالك المتجر من البيانات التي تحفظ ضمن بيانات معلومات المتجر لدى منصة سلة لضمان موثوقية المتجر. ❓ في حال كان التاجر أجنبيّاً كيف يتم التحقق من صحة بيانات متجره؟ ⟪يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري.⟫ 📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات. ❓ كيف يظهر للتاجر أن المتجر قد تُحُقِقَ من صحة بياناته؟ يتم إظهار علامة مكتمل أمام توثيق المتجر في صفحة اعدادات الدفع. ❓ عند التحقق من صحة بيانات مؤسسة مبيعاتها أقل من 375 ألف ريال، كيف يتم التحقق من صحة الرقم الضريبي؟ يتم الرجوع إلى هيئة الزكاة والدخل بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ قرار التحقق من صحة البي…

**Citation Q3-SA-C006:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: 📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات.
- title, opening and note boxes: as for this source's citation above
- in context: …خدم للمتجر. ❓ عند التحقق من صحة البيانات لمتجر جمعية، من يعتبر مالك المتجر؟ ولماذا لا يتم تغيير المسمى من مالك المتجر إلى الصفة المطلوبة (رئيس مجلس، مدير تنفيذي، الخ) يعتبر اسم مالك المتجر من البيانات التي تحفظ ضمن بيانات معلومات المتجر لدى منصة سلة لضمان موثوقية المتجر. ❓ في حال كان التاجر أجنبيّاً كيف يتم التحقق من صحة بيانات متجره؟ يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري. ⟪📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات.⟫ ❓ كيف يظهر للتاجر أن المتجر قد تُحُقِقَ من صحة بياناته؟ يتم إظهار علامة مكتمل أمام توثيق المتجر في صفحة اعدادات الدفع. ❓ عند التحقق من صحة بيانات مؤسسة مبيعاتها أقل من 375 ألف ريال، كيف يتم التحقق من صحة الرقم الضريبي؟ يتم الرجوع إلى هيئة الزكاة والدخل بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ قرار التحقق من صحة البيانات حكومي أم من شركة سلة؟ هي مبادرة من شركة سلة لتنظيم سوق التجارة الإلكترونية في المملكة العربية السعودية تهدف إلى رفع…
