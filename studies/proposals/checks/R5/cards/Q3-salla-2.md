# Cards: Q3 on salla

11 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 25:** - Other parties add their own requirements, a match on role. On help pages (stated): American Express's address and name rules on a Shopify Payments account; for Tabby in Salla's UAE stores, a verified store, a Tabby merchant account with its keys, and an eligible plan; and each BigCommerce provider's own application and underwriting. On store ibx5bt-xy, the saved markup of the Shop Pay Installments terms step, observed 30 September 2026, says "Affirm reserves the right to deny you access to the Affirm Services" and asks for information identifying the seller and its beneficial owners, as its accessibility tree did. Q3-SH-057; Q3-SA-069; Q3-BC-P0048; Q3-SH-110
- **section 1, line 29:** - The payout account's holder must match the verified identity, a match on role. Shopify compares the bank account's name with the legal business name or the account representative's. Salla: "تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق". Zid: "لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح". On both Salla and Zid an establishment needs a business account in its own name. Q3-SH-062; Q3-SA-K1563; Q3-ZD-K0037; Q3-SA-010; Q3-ZD-015
- **section 1, line 30:** - Salla requires verification to withdraw the store balance and transfer the electronic payments balance; on store merchant (Basic, observed 8 October 2026) withdrawal was disabled for `store_documents_required`. Zid's wallet takes balance the seller adds and spends, and "لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب"; its words don't say it holds sales proceeds, so the draft leaves it out of the money flow. Q3-SA-P0162; Q3-SA-077; Q3-ZD-P0063
- **section 1, line 35:** - Salla and Zid keep their own lists too: Salla's سياسة البيع, from gambling to resold shipping labels, and Zid Pay's الأنشطة المحظورة. Q3-SA-054; Q3-SA-K1532; Q3-ZD-P0111
- **section 1, line 37:** - Salla's agreement and Zid's terms carry the same clause for products needing an official licence, "بالإفصاح عن الترخيص وكافة بياناته": the same term, both official pages. Neither platform's full list of such products was in what was read; Zid decides the need after reviewing the data, with books and the Ministry of Media as its example. Q3-SA-047; Q3-ZD-K0247; Q3-SA-N02; Q3-ZD-N04; Q3-ZD-023
- **section 1, line 39:** - The registered activity must match the products, a match on role: Salla's KYC schema for a demo store, observed 8 October 2026, says "Commercial registration activity must match the store activity", and Zid's help page "أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر". Q3-SA-058; Q3-ZD-003
- **section 1, line 40:** - Salla's Basic plan allows only ready-made products (منتج جاهز); digital products, food, made-to-order products, bundles and bookings need Plus or Pro. Q3-SA-029
- **section 1, line 45:** - A program or channel often needs another capability active, a match on role. Shop needs Shopify Payments activated; Mahally needs a paid plan and a verified store (not checked on WooCommerce; shown by Salla); and Zid Financing needs Zid Pay activated and approved. Q3-SH-077; Q3-SA-061; Q3-ZD-P0132
- **section 1, line 51:** - Salla requires every verification document to be in the store owner's own name. Its KYC schema for a demo store, observed 8 October 2026, offers the entity types `single`, `company`, `institution`, `charity` and `government`; Zid's business types are فرد، مؤسسة، شركة، جمعية خيرية. They match on role in four of five (Salla's schema observed, Zid's help page stated); Salla adds government. Q3-SA-019; Q3-SA-056; Q3-ZD-K0239
- **section 2, line 86:** - **Capability** (proposed): a thing a seller may do that a requirement set can gate: open the store to buyers, take payments through one method or provider, receive payouts, withdraw a balance, sell a product type or category, join a sales channel or program, or use a financing or tax service. One capability can require another, as Shop requires Shopify Payments, Mahally a verified store, and Zid Financing Zid Pay. Why: rule 2, so a change in one provider's requirements changes only its capability. Q3-SH-077; Q3-SA-061; Q3-ZD-P0132
- **section 2, line 87:** - **Capability status** (proposed): for each store and capability, available, blocked or restricted, with machine-readable reasons naming the unmet requirements. It takes Salla's `blocks_payment_activation`, `blocked_by` and `withdraw_disabled_reason`, WooCommerce's blocked onboarding step, and Shopify's field for setup completed. Why: rule 3, the data model. Q3-SA-073; Q3-SA-074; Q3-SA-077; Q3-WC-041; Q3-SH-086
- **section 2, line 88:** - **Requirement** (proposed): one condition, with its kind, subject, setter, validity and check. Its kinds come from the platforms: information, a document, an identity check, a plan, an accepted agreement, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account age such as WooPayments' 7 days before a first payout, a match between subjects such as the payout account's holder and the verified name, not being a listed party, as under Shopify Payments' sanctions rule, and another capability being active. Validity follows rules such as Zid's commercial register valid two months from activation. Its subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-WC-P0038; Q3-SA-K1563; Q3-SH-K2268; Q3-ZD-013
- **section 2, line 96:** - Holding payouts, blocking withdrawals and returning payments to buyers act on sellers' money. The design provides for them, and for gating payouts and a balance; any arrangement in which sellers' money is held through Sharrwah, by Sharrwah itself or by a payment company in an account opened through Sharrwah, goes live only by the founder's decision. Q3-SA-077; Q3-ZD-P0012; Q3-SH-P0085
- **section 2, line 99:** - **Product rule** (proposed): a rule on what may be sold, with its setter and its reach. It may bar a product for all of Sharrwah; bar it for one provider, blocking only that provider's capability; require a licence disclosed on the store with its details; require the registered activity to match the product; or require a plan for a product type. It takes Salla's selling policy, Shopify Payments' hemp rule and WooPayments' CBD rule, Salla's and Zid's licence clause, their activity match, and Salla's plan-limited product types. Why: rule 2, since each setter's list changes on its own. Q3-SA-054; Q3-SH-095; Q3-WC-K0417; Q3-SA-047; Q3-ZD-K0247; Q3-SA-058; Q3-ZD-003; Q3-SA-029
- **section 3, line 108:** - Payment providers, each with its own requirement set and approval: American Express on Shopify, Tabby on Salla, Tap on Zid, and the providers on BigCommerce. Q3-SH-057; Q3-SA-069; Q3-ZD-K0093; Q3-BC-P0048
- **section 3, line 109:** - Sales channels and programs, each with its own requirement set: Shop and Mahally. Q3-SH-077; Q3-SA-061
- **section 3, line 115:** - Per entity type and place: the documents, the fields, and the kind of payout account, as in Salla's table, on Zid, and in the Social Security Number field for a US Individual in Shopify store capture-advanced's saved markup, observed 4 October 2026. Q3-SA-014; Q3-SA-010; Q3-ZD-015; Q3-SH-111
- **section 3, line 116:** - Per plan: payment methods and product types on Salla, and BigCommerce Payments. Q3-SA-P0068; Q3-SA-029; Q3-BC-P0068
- **section 3, line 117:** - Per provider or payment method: American Express's rules, and Tabby's on Salla. Q3-SH-057; Q3-SA-069
- **section 3, line 125:** - Sharrwah: its own requirement sets, such as its review, its plans and its selling policy, as Salla's own verification and selling policy show. Q3-SA-037; Q3-SA-054
- **section 7, line 173:** - Whether plans gate capabilities such as payment methods, product types and channels. Q3-SA-P0068; Q3-SA-029; Q3-BC-P0068

## The cards

### Q3-SA-069

**Cited at:** section 1, line 25; section 3, line 108; section 3, line 117

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-069
- bears_on: 1;2;4
- identifier: ما الذي تحتاج إلى تجهيزه قبل التفعيل؟
- statement: يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة
- scope: تفعيل تابي على متجرك في سلة الإمارات
- cite_ids: Q3-SA-C133;Q3-SA-C134;Q3-SA-C135;Q3-SA-C136;Q3-SA-C137;Q3-SA-C138;Q3-SA-C139;Q3-SA-C140
- from: held
- note: Table cells in source order: each description is followed by the requirement it describes.

**Citation Q3-SA-C133:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ى زيادة القوة الشرائية، وتحسين إتمام الطلب، ورفع متوسط قيمة السلة. الدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي. ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب ⟪يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها.⟫ متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: م…

**Citation Q3-SA-C134:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: متجر موثّق على سلة
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …متوسط قيمة السلة. الدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي. ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. ⟪متجر موثّق على سلة⟫ تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية …

**Citation Q3-SA-C135:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …لدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي. ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة ⟪تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي.⟫ حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ ال…

**Citation Q3-SA-C136:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: حساب تاجر لدى تابي
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي. ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. ⟪حساب تاجر لدى تابي⟫ جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ث…

**Citation Q3-SA-C137:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …سوم التاجر للاتفاقية المبرمة بينك وبين تابي. ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي ⟪جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي.⟫ بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ثم اختر «تابي». أدخل Merchant Public Key وMerchant Private Key المر…

**Citation Q3-SA-C138:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: بيانات الربط
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …صة سلة، تحديث الحالات تلقائيًا، وإصدار الفواتير الضريبية والمبسطة بما يتوافق مع متطلبات الفوترة الإلكترونية. 👣خطوات الربط مع تطبيق ألفا 1. من القائمة الرئيسية، اضغط (الكل)، ثم من قسم الأدوات المساعدة، اضغط ( متجر التطبيقات ). 2. من صفحة تطبيق ألفا ، اضغط (تثبيت). 3. اختر الخطة المناسبة لك. 4. أكمل بيانات الدفع، ثم اضغط (تأكيد). 5. أضف ⟪بيانات الربط⟫، ثم اضغط (حفظ). 🎉 تم تثبيت التطبيق في صفحة تطبيقاتي في متجرك. 6. سجّل في موقع ألفا من خلال (ابدأ معنا)، حيث يمكنك من خلال الموقع إدارة أنظمتك والتحكم بإعدادات التطبيق. 7. أدخل بيانات التواصل، ثم اضغط (إرسال) ليتم التواصل معك من قبل فريق ألفا لمتابعة خطوات الربط. 🚀إدارة تطبيق ألفا ترقية الباقة 1. من صفحة تفاصيل التطبيق في متجرك، اضغط (…

**Citation Q3-SA-C139:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: تتوفر تابي على باقات بلس، وبرو، وسبيشال.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط ⟪تتوفر تابي على باقات بلس، وبرو، وسبيشال.⟫ باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ثم اختر «تابي». أدخل Merchant Public Key وMerchant Private Key المرتبطين بحسابك لدى تابي. راجع إعدادات تابي المتاحة لمتجر…

**Citation Q3-SA-C140:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة) | 2026-09-16 | kind: stated | quote check: found
- quote: باقة مؤهلة في سلة
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …متجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي. حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. ⟪باقة مؤهلة في سلة⟫ كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ثم اختر «تابي». أدخل Merchant Public Key وMerchant Private Key المرتبطين بحسابك لدى تابي. راجع إعدادات تابي المتاحة لمتجرك. وافق على شروط ا…

### Q3-SA-K1563

**Cited at:** section 1, line 29; section 2, line 88

**Record** (`studies/proposals/records/Q3/salla/copied.tsv`):
- concern_id: SA-C-112
- placement: decides
- structure: https://help.salla.sa/article/-إعداد-الحساب-البنكي/bhrrwm3oexjhzqjibwnic7dg
- identifier: تحديث الحساب البنكي لاستلام مستحقاتك من سلة
- statement: 🚨 تنبيه: تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق، وأن بيانات الحساب صحيحة لتجنب تأخر تحويل المستحقات.
- cite_ids: SA-S-0098

**Citation SA-S-0098:** `https://help.salla.sa/article/-إعداد-الحساب-البنكي/bhrrwm3oexjhzqjibwnic7dg` | تحديث الحساب البنكي لاستلام مستحقاتك من سلة (line 695 of the rendered text) | 2026-10-05 | kind: stated | quote check: found
- quote: 🚨 تنبيه: تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق، وأن بيانات الحساب صحيحة لتجنب تأخر تحويل المستحقات.
- title: إضافة الحساب البنكي وسحب رصيد متجرك | مركز المساعدة - سلة
- the page opens: إضافة الحساب البنكي وسحب رصيد متجرك مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل…
- in context: …كم، اضغط على أيقونة (إعدادات المتجر). 2. من تبويب (الرصيد والفواتير)، اضغط تعديل الحساب البنكي لاستلام المدفوعات. 3. سيتم توجيهك لصفحة التوثيق، اتبع الخطوات واكمل البيانات المطلوبة. عدّل الحساب البنكي، ثم ارفع طلب التوثيق. أو من خلال صفحة التوثيق مباشرة: 1. من تبويب (الكل) في القائمة الرئيسية، اختر (توثيق المتجر). 2. اضغط (التالي) للبدء بتعديل بيانات التوثيق. اتبع خطوات التوثيق واكمل البيانات المطلوبة. 3. عدّل الحساب البنكي، ثم ارفع طلب التوثيق. ⟪🚨 تنبيه: تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق، وأن بيانات الحساب صحيحة لتجنب تأخر تحويل المستحقات.⟫ خطوات إضافة حساب بنكي جديد لاستقبال المدفوعات من العملاء 1. من تبويب (الكل) في القائمة الرئيسية للوحة التحكم، اضغط (طرق الدفع). 2. من صفحة طرق الدفع، من قسم الحسابات البنكية، اضغط (+ إضافة حساب جديد). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). 1- حدد البنك. 2- اسم صاحب الحساب. 3- رقم الحساب المصرفي. 4- رقم الأيبان. 5- خيار إضافة المعرف البديل. بعد إضافة الحساب، يمكن لعملائك استخدامه عند اختيار التحويل البنكي كطريقة دفع أثناء إتمام الط…

### Q3-SA-010

**Cited at:** section 1, line 29; section 3, line 115

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-010
- bears_on: 1
- identifier: ❓ هل يمكنني استخدام حساب بنكي شخصي أو تجاري؟
- statement: إذا كان نوع الكيان فرد، يمكنك استخدام حساب شخصي أو تجاري. إذا كان نوع الكيان مؤسسة، فيجب أن يكون الحساب تجاري باسم المؤسسة.
- cite_ids: Q3-SA-C013;Q3-SA-C014
- from: held

**Citation Q3-SA-C013:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: إذا كان نوع الكيان فرد، يمكنك استخدام حساب شخصي أو تجاري.
- in context: …ا يمكن تخصيص ذلك لسوق معينة. zbcnt9hu9kf8lfh2gmf1vccr https://help.salla.sa/article/%D8%A3%D8%B3%D8%A6%D9%84%D8%A9-%D8%B4%D8%A7%D8%A6%D8%B9%D8%A9-%D8%AD%D9%88%D9%84-%D8%AA%D9%88%D8%AB%D9%8A%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1-1/zbcnt9hu9kf8lfh2gmf1vccr لمزيد من التفاصيل حول إدارة سجل طلب توثيق المتجر أداة تساعدك في معرفة أفضل طريقة توثيق لك خطوة بخطوة: من هنا ❓ هل يمكنني استخدام حساب بنكي شخصي أو تجاري؟ نعم ، لكن ذلك يعتمد على نوع الكيان: ⟪إذا كان نوع الكيان فرد، يمكنك استخدام حساب شخصي أو تجاري.⟫ إذا كان نوع الكيان مؤسسة، فيجب أن يكون الحساب تجاري باسم المؤسسة. ❓ما الفرق بين توثيق منصة الأعمال وتوثيق متجر سلة؟ توثيق متجر سلة : توثيق بيانات المتجر داخل سلة واستكمال متطلبات المتجر توثيق منصة الأعمال : توثيق النشاط داخل منصة الأعمال الحكومية ❓ هل توثيق منصة الأعمال هو نفسه توثيق متجر سلة؟ لا، كلاهما مختلفان ولكل منهما إجراءات مستقلة. ❓ما هي آلية تحويل مبالغ السحب ومتى يتم تحويلها إلى حساب التاجر؟ يتم تحويل المبالغ من رصيد المتجر إلى الحساب …

**Citation Q3-SA-C014:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر) | 2026-08-29 | kind: stated | quote check: found
- quote: إذا كان نوع الكيان مؤسسة، فيجب أن يكون الحساب تجاري باسم المؤسسة.
- title, opening and note boxes: as for this source's citation above
- in context: …s://help.salla.sa/article/%D8%A3%D8%B3%D8%A6%D9%84%D8%A9-%D8%B4%D8%A7%D8%A6%D8%B9%D8%A9-%D8%AD%D9%88%D9%84-%D8%AA%D9%88%D8%AB%D9%8A%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1-1/zbcnt9hu9kf8lfh2gmf1vccr لمزيد من التفاصيل حول إدارة سجل طلب توثيق المتجر أداة تساعدك في معرفة أفضل طريقة توثيق لك خطوة بخطوة: من هنا ❓ هل يمكنني استخدام حساب بنكي شخصي أو تجاري؟ نعم ، لكن ذلك يعتمد على نوع الكيان: إذا كان نوع الكيان فرد، يمكنك استخدام حساب شخصي أو تجاري. ⟪إذا كان نوع الكيان مؤسسة، فيجب أن يكون الحساب تجاري باسم المؤسسة.⟫ ❓ما الفرق بين توثيق منصة الأعمال وتوثيق متجر سلة؟ توثيق متجر سلة : توثيق بيانات المتجر داخل سلة واستكمال متطلبات المتجر توثيق منصة الأعمال : توثيق النشاط داخل منصة الأعمال الحكومية ❓ هل توثيق منصة الأعمال هو نفسه توثيق متجر سلة؟ لا، كلاهما مختلفان ولكل منهما إجراءات مستقلة. ❓ما هي آلية تحويل مبالغ السحب ومتى يتم تحويلها إلى حساب التاجر؟ يتم تحويل المبالغ من رصيد المتجر إلى الحساب البنكي بعد طلب السحب من قبل التاجر، وذلك بشرط اكتمال توثيق المتجر …

### Q3-SA-P0162

**Cited at:** section 1, line 30

**Record** (`studies/proposals/records/Q3/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-161
- bullet: c
- placement: decides
- identifier: Does store verification matter?
- statement: Yes. Verification is required for: Withdrawing Store Balance Transferring Electronic Payments Balance
- scope: Saudi Arabia (English title: Wallet & invoices | Saudi Arabia)
- cite_ids: S01-SA-C241;S01-SA-C242;S01-SA-C243
- from: new
- note: The answer and its two list items, each cited.

**Citation S01-SA-C241:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl` | line 1241 (article g36cl2hlsv256gr55vutx5rv, Wallet & invoices | Saudi Arabia), paragraph 152 | 2026-10-07 | kind: stated | quote check: found
- quote: Yes. Verification is required for:
- in context: …ow: Customer pays → funds go to Electronic Payments Balance Merchant transfers or withdraws funds through Wallet What is the minimum payout amount? The minimum payout threshold is SAR/AED 100. Can I still use smaller amounts? Yes. You can transfer small amounts into your Wallet and use or withdraw them anytime. Can I withdraw wallet funds anytime? Yes, merchants can withdraw available wallet funds whenever needed. Does store verification matter? ⟪Yes. Verification is required for:⟫ Withdrawing Store Balance Transferring Electronic Payments Balance For more details, see the Store Verification guide. nvs6bt51hvlweulqzayp3o76 https://help.salla.sa/en/article/wallet-invoices-uae/nvs6bt51hvlweulqzayp3o76 Once a customer successfully pays for an order online, the payment moves through processing and settlement before the funds are transferred to your registered bank account. For UAE stores, eligible payouts are sent weekly on Th…

**Citation S01-SA-C242:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl` | line 1241 (article g36cl2hlsv256gr55vutx5rv, Wallet & invoices | Saudi Arabia), paragraph 153 | 2026-10-07 | kind: stated | quote check: found
- quote: Withdrawing Store Balance
- in context: …ctronic Payments Balance Merchant transfers or withdraws funds through Wallet What is the minimum payout amount? The minimum payout threshold is SAR/AED 100. Can I still use smaller amounts? Yes. You can transfer small amounts into your Wallet and use or withdraw them anytime. Can I withdraw wallet funds anytime? Yes, merchants can withdraw available wallet funds whenever needed. Does store verification matter? Yes. Verification is required for: ⟪Withdrawing Store Balance⟫ Transferring Electronic Payments Balance For more details, see the Store Verification guide. nvs6bt51hvlweulqzayp3o76 https://help.salla.sa/en/article/wallet-invoices-uae/nvs6bt51hvlweulqzayp3o76 Once a customer successfully pays for an order online, the payment moves through processing and settlement before the funds are transferred to your registered bank account. For UAE stores, eligible payouts are sent weekly on Thursdays when your online-p…

**Citation S01-SA-C243:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl` | line 1241 (article g36cl2hlsv256gr55vutx5rv, Wallet & invoices | Saudi Arabia), paragraph 154 | 2026-10-07 | kind: stated | quote check: found
- quote: Transferring Electronic Payments Balance
- in context: …erchant transfers or withdraws funds through Wallet What is the minimum payout amount? The minimum payout threshold is SAR/AED 100. Can I still use smaller amounts? Yes. You can transfer small amounts into your Wallet and use or withdraw them anytime. Can I withdraw wallet funds anytime? Yes, merchants can withdraw available wallet funds whenever needed. Does store verification matter? Yes. Verification is required for: Withdrawing Store Balance ⟪Transferring Electronic Payments Balance⟫ For more details, see the Store Verification guide. nvs6bt51hvlweulqzayp3o76 https://help.salla.sa/en/article/wallet-invoices-uae/nvs6bt51hvlweulqzayp3o76 Once a customer successfully pays for an order online, the payment moves through processing and settlement before the funds are transferred to your registered bank account. For UAE stores, eligible payouts are sent weekly on Thursdays when your online-payments balance exceeds AED 250. Payouts …

### Q3-SA-077

**Cited at:** section 1, line 30; section 2, line 87; section 2, line 96

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-077
- bears_on: 2;4
- identifier: GET /admin/v2/store-wallet/wallet/summary: data.wallets[type default].metadata
- statement: "wallet_withdrawal_enabled": false, "withdraw_disabled_reason": "store_documents_required", "withdraw_disabled_message": "يُشترط اكمال توثيق المتجر لتتمكن من استرداد الرصيد.", "store_bank_account_exist": false, "is_store_documented": false
- scope: store merchant, observed 2026-10-08; بيسك
- cite_ids: Q3-SA-C168;Q3-SA-C158
- from: held

**Citation Q3-SA-C168:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1722.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, store merchant, step 72 | 2026-10-08 | kind: observed | quote check: found
- quote: "wallet_withdrawal_enabled": false, "withdraw_disabled_reason": "store_documents_required", "withdraw_disabled_message": "يُشترط اكمال توثيق المتجر لتتمكن من استرداد الرصيد.", "store_bank_account_exist": false, "is_store_documented": false
- in context: …sage": "يتم تحويل مستحقاتك كل يوم أربعاء عند تجاوز الرصيد 100 ريال.", "payout_schedule_messages": {"epayment": "يتم تحويل مستحقاتك كل يوم أربعاء عند تجاوز الرصيد 100 ريال.", "cod": "تُحوَّل مستحقاتك من المدفوعات عند الاستلام كل أحد وأربعاء."}, "wallets": [{"type": "default", "name": "المحفظة", "balance": 0, "currency": "SAR", "can_withdraw": false, "metadata": {"wallet_id": "1655351255", "disable_balance_draw": true, "is_withdraw_over_limit": 0, ⟪"wallet_withdrawal_enabled": false, "withdraw_disabled_reason": "store_documents_required", "withdraw_disabled_message": "يُشترط اكمال توثيق المتجر لتتمكن من استرداد الرصيد.", "store_bank_account_exist": false, "is_store_documented": false⟫, "daily_limit": "5008.05", "total_deposits": 0, "total_withdrawals": 0}}, {"type": "salla_pay", "name": "المدفوعات الإلكترونية ", "balance": 0, "currency": "SAR", "can_withdraw": false, "metadata": {"enable_transfer_balance": false, "is_balance_frozen": true, "day_amount_balance": 0, "max_total_to_generate": 100, "total_excluding_fees_and_tax": 0, "total_fees": 0, "total_tax": 0, "total_including_fees_and_tax": 0}}, {"type": "salla_cod", "name":…

**Citation Q3-SA-C158:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.text.txt` | step 76 | 2026-10-08 | kind: observed | quote check: found
- step 76: sweep (Arabic): main navigation: توثيق المتجر — /payments/kyc | https://s.salla.sa/payments/kyc | "سلة | توثيق المتجر" | 2026-10-08T12:44:04.174Z
- the step's files: `observed-sa@4ca2e896a:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.aria.yaml`, `observed-sa@4ca2e896a:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.text.txt`
- quote: Hamza بيسك
- in context: الكل الرئيسية الطلبات المنتجات التسويق المتجر وقنوات البيع التقارير ⟪Hamza بيسك⟫ طرق الدفع المحفظة قيود الدفع إدارة الضرائب عمليات الدفع الإلكتروني توثيق المتجر مشمر لتضمن توثيق متجرك بنجاح وبخطوات سريعة، يرجى تجهيز المتطلبات التالية 1. وثيقة العمل الحر للمواطنين السعوديين فقط الهوية: يجب أن تكون الهوية الوطنية لمالك المتجر سارية الصلاحية ومطابقة تماماً لبياناته في منصة أبشر. الوثيقة المطلوبة: وثيقة عمل حر سارية تابعة لمالك المتجر. الحساب البنكي: يجب أن يكون الحساب البنكي مطابقاً ل: • هوية مالك المتجر. • أو وثيقة العمل الحر …

### Q3-SA-054

**Cited at:** section 1, line 35; section 2, line 99; section 3, line 125

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-054
- bears_on: 1;2
- identifier: سياسة البيع
- statement: هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي). إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات ليست ضمن المتجر الإلكتروني.
- cite_ids: Q3-SA-C106;Q3-SA-C107;Q3-SA-C108;Q3-SA-C109;Q3-SA-C110;Q3-SA-C111;Q3-SA-C112;Q3-SA-C113;Q3-SA-C114
- from: held

**Citation Q3-SA-C106:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 16 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص:
- in context: منصة سلة: حلول التجارة الإلكترونية الشاملة في السعودية الحلول الموارد القطاعات سلة سبيشل الأسعار En تسجيل دخول أنشئ متجرك مجانًا أنشئ متجرك مجانًا سياسة البيع A A A في سلة ساعدنا الاف التجار التجار لبدء اعمالهم التجارية على الانترنت والتوسع بكل سهولة. ⟪هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص:⟫ أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به.…

**Citation Q3-SA-C107:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 17 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون.
- in context: …خول أنشئ متجرك مجانًا أنشئ متجرك مجانًا سياسة البيع A A A في سلة ساعدنا الاف التجار التجار لبدء اعمالهم التجارية على الانترنت والتوسع بكل سهولة. هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص: ⟪أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون.⟫ أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر…

**Citation Q3-SA-C108:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 18 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال.
- in context: … الاف التجار التجار لبدء اعمالهم التجارية على الانترنت والتوسع بكل سهولة. هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. ⟪أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال.⟫ أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللم…

**Citation Q3-SA-C109:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 19 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر.
- in context: …ل سهولة. هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. ⟪أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر.⟫ أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي). إعادة بيع بوليصة الشحن…

**Citation Q3-SA-C110:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 20 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك.
- in context: …لجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. ⟪أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك.⟫ أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي). إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات…

**Citation Q3-SA-C111:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 21 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به.
- in context: …ً بيع المنتجات والخدمات التالية بشكل عام أو خاص: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. ⟪أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به.⟫ البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي). إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات ليست ضمن المتجر الإلكتروني. A A A في سلة ساعدنا …

**Citation Q3-SA-C112:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 22 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم.
- in context: …أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منتج عشوائي غير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. ⟪البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم.⟫ عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي). إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات ليست ضمن المتجر الإلكتروني. A A A في سلة ساعدنا الاف التجار التجار لبدء اعمالهم التجارية على الانترنت والتوسع…

**Citation Q3-SA-C113:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 23 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي).
- in context: …ير مضمون. أي منتج/خدمة قد تؤدي إلى أي أذى جسدي أو نفسي بأي شكل من الأشكال. أي محتويات أو اشتراكات مقرصنة وكل ما يخالف حقوق الملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. ⟪عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي).⟫ إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات ليست ضمن المتجر الإلكتروني. A A A في سلة ساعدنا الاف التجار التجار لبدء اعمالهم التجارية على الانترنت والتوسع بكل سهولة. هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع …

**Citation Q3-SA-C114:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt` | line 24 (سياسة البيع) | 2026-10-08 | kind: official page | quote check: found
- quote: إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات ليست ضمن المتجر الإلكتروني.
- in context: …لملكية الفكرية والنشر. أي منتج/خدمة جنسية أو اباحية أو تدعو لذلك. أي منتج/خدمة تحتوي على قراءة للغيب أو التنبؤ به. البيع المسبق لمنتج لم يطرح بشكل رسمي بعد من قبل الشركة الأم. عدم توّفر إثبات للبيع ضمن الطلب، وهي للمنتجات الجاهزة (بوليصة الشحن)، وللمنتجات والخدمات الرقمية (الأكواد والمحتوى الرقمي). ⟪إعادة بيع بوليصة الشحن لأي طرف آخر او إساءة استخدامها لشحن منتجات ليست ضمن المتجر الإلكتروني.⟫ A A A في سلة ساعدنا الاف التجار التجار لبدء اعمالهم التجارية على الانترنت والتوسع بكل سهولة. هدفنا تسهيل التجارة الالكترونية وخلق بيئة تجارية موثوقة وآمنة للجميع. لذلك ومن هذا المبدأ ُيمنع منعاً باتاً بيع المنتجات والخدمات التالية بشكل عام أو خاص: أي منتج/خدمة تحتوي على مقامرة أو صناديق الحظ أو منت…

### Q3-SA-047

**Cited at:** section 1, line 37; section 2, line 99

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-047
- bears_on: 1;2
- identifier: المادة الرابعة – ضوابط إنشاء المتجر الالكتروني
- statement: .ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.
- cite_ids: Q3-SA-C096
- from: held

**Citation Q3-SA-C096:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 49 (المادة الرابعة – ضوابط إنشاء المتجر الالكتروني) | 2026-10-06 | kind: official page | quote check: found
- quote: .ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.
- in context: …التجّار الالتزام بالإفصاح في المتجر الالكتروني عن البيانات التالية: الاسم والعنوان - السجل التجاري أو وثيقة العمل الحر - وسائل الاتصال الرسمية. ينبغي على كافة المتاجر والتجّار الالتزام بإيضاح الشروط والأحكام للمستهلك وسياسة الخصوصية وسرية المعلومات والتي تعد في حكم العقد الإلكتروني. ينبغي على كافة المتاجر والتجّار تقديم فاتورة إلى المستهلك تبيّن تكاليف شراء تقديم الخدمة أو المنتج، وإجمالي السعر، وتاريخ التسليم ومكانه وسياسة الاستبدال والاسترجاع. ⟪.ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.⟫ .ينبغي على كافة المتاجر والتجّار الذين يحملون سجلاً تجارياً لمحلهم، بتقييد المحل الالكتروني بالسجل التجاري للمنشأة وفقاً للنظام. .يقر التاجر بأنه قبل تسجيله في منصة سلة الالكترونية قد تحقق من توافر جميع الإجراءات والاشتراطات المطلوبة من قبل الجهات الرسمية في المملكة العربية السعودية وقد استوفى جميع هذه الإجراءات والاشتراطات لممارسة نشاطه في المتجر. .ينبغي على كافة المتاجر الراغبة بالتسجيل بمنصة سلة ومزاولة نشاط التجارة الإلكترونية بالمنصة أن يكو…

### Q3-SA-058

**Cited at:** section 1, line 39; section 2, line 99

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-058
- bears_on: 1;2
- identifier: commercial registration activity must match the store activity
- statement: "en":"Commercial registration activity must match the store activity"
- scope: merchants_saudi_kyc
- cite_ids: Q3-SA-C119
- from: held

**Citation Q3-SA-C119:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/kyc-schema/demo@en/source.json` | data.renderer_schema.translations["commercial registration activity must match the store activity"] | 2026-10-08 | kind: observed | quote check: found
- quote: "en":"Commercial registration activity must match the store activity"
- in context: …7\u0644\u0633\u062c\u0644 \u0627\u0644\u062a\u062c\u0627\u0631\u064a.","en":"Your identity does not belong to this commercial certificate."},"commercial registration activity must match the store activity":{"ar":"\u0623\u0646 \u064a\u0643\u0648\u0646 \u0646\u0634\u0627\u0637 \u0627\u0644\u0633\u062c\u0644 \u0627\u0644\u062a\u062c\u0627\u0631\u064a \u0645\u0637\u0627\u0628\u0642 \u0644\u0646\u0634\u0627\u0637 \u0627\u0644\u0645\u062a\u062c\u0631",⟪"en":"Commercial registration activity must match the store activity"⟫},"enter your national id or iqama number consisting of 10 digits":{"ar":"\u0623\u062f\u062e\u0644 \u0631\u0642\u0645 \u0647\u0648\u064a\u062a\u0643 \u0627\u0644\u0648\u0637\u0646\u064a\u0629 \u0623\u0648 \u0627\u0644\u0625\u0642\u0627\u0645\u0629 \u0627\u0644\u0645\u0643\u0648\u0651\u0646 \u0645\u0646 10 \u0623\u0631\u0642\u0627\u0645","en":"Enter your national ID or Iqama number consisting of 10 digits"},"official authorization letter from the …

### Q3-SA-029

**Cited at:** section 1, line 40; section 2, line 99; section 3, line 116; section 7, line 173

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-029
- bears_on: 1;2
- identifier: ❓ ماهي أنواع المنتجات التي يمكنني إضافتها في باقة بيسك؟
- statement: يمكنك إضافة منتجات بنوع منتج جاهز فقط، قم بالترقية إلى باقة برو أو باقة بلس لكي تتمكن من إضافة أنواع أخرى من المنتجات مثل: (منتجات رقمية، بطاقات رقمية، منتج اكل، منتج حسب الطلب، مجموعة منتجات، أو منتج حجوزات).
- scope: باقة بيسك
- cite_ids: Q3-SA-C054
- from: held

**Citation Q3-SA-C054:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 780 (article zgflevdt56pvfugbbnnkzr06, تدشين متجرك على سلة) | 2026-09-14 | kind: stated | quote check: found
- quote: يمكنك إضافة منتجات بنوع منتج جاهز فقط، قم بالترقية إلى باقة برو أو باقة بلس لكي تتمكن من إضافة أنواع أخرى من المنتجات مثل: (منتجات رقمية، بطاقات رقمية، منتج اكل، منتج حسب الطلب، مجموعة منتجات، أو منتج حجوزات).
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …من الصفحة الرئيسة لمتجرك، توجه إلى (المزيد) ثم (طرق الدفع). 2. من صفحة طرق الدفع، اضغط (وسائل الدفع المفعّلة). فعّل أو ألغِ تفعيل وسائل الدفع بما يناسبك واضغط (حفظ). ❓ هل يمكنني الربط أو إزالة الربط مع شركات الشحن والتوصيل بعد إكمال التسجيل؟ نعم ، وذلك بالطريقة التالية: 1. من الصفحة الرئيسة لمتجرك، توجه إلى (المزيد) ثم (الشحن). 2. يمكنك التحكم بكافة خيارات بوليصات سلة وشركات الشحن والتوصيل. ❓ ماهي أنواع المنتجات التي يمكنني إضافتها في باقة بيسك؟ ⟪يمكنك إضافة منتجات بنوع منتج جاهز فقط، قم بالترقية إلى باقة برو أو باقة بلس لكي تتمكن من إضافة أنواع أخرى من المنتجات مثل: (منتجات رقمية، بطاقات رقمية، منتج اكل، منتج حسب الطلب، مجموعة منتجات، أو منتج حجوزات).⟫ 🚀 خدمات مساندة في حال احتجت مساعدة في إنشاء وإعداد متجر سلة، لإضافة المنتجات والخدمات، تفعيل طرق الدفع للمتجر . أو توثيق المتجر وإصدار شهادة العمل الحر يمكنك الاستفادة من خدمات التاجر، والتي توفر خدمات نوعية من مزودي خدمات خارجيين لإنجاز أعمال تخص نشاطك التجاري باحترافية . 🔍 مصادر تعلم إضافية لكي تكتشف كيف يمكنك بناء متجر إلكتروني احترافي ومعرفة أهم الأدوات والأساليب التي تجذب العملاء وتساعدك على تحقيق نجاح ملموس سجّل في دورة إنشاء متجر على سلة …

### Q3-SA-061

**Cited at:** section 1, line 45; section 2, line 86; section 3, line 109

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-061
- bears_on: 1;2;4
- identifier: ما هي شروط الانضمام لمحلي؟
- statement: أن يكون لديك متجر على سلة. أن تكون مشتركًا بإحدى الباقات المدفوعة مثل باقة بلس أو برو. أن يكون متجرك موثقًا. الموافقة على شروط الخصوصية والاستخدام لمنصة محلي.
- cite_ids: Q3-SA-C122;Q3-SA-C123;Q3-SA-C124;Q3-SA-C125
- from: held
- note: Q3-SA-K1450 copies the fourth condition only.

**Citation Q3-SA-C122:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1397 (article pvoh9k11k2sjti6k1xu667e5, منصة محلي والانضمام لها) | 2026-08-22 | kind: stated | quote check: found
- quote: أن يكون لديك متجر على سلة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …%A7%D9%84%D8%B4%D8%A7%D8%A6%D8%B9%D8%A9-%D8%AD%D9%88%D9%84-%D9%85%D9%86%D8%B5%D8%A9-%D9%85%D8%AD%D9%84%D9%8A-1/i6552boeb92lhuug905exq0i ❓ ما هي منصة محلي؟ محلي من سلة هي قناة بيع متكاملة تمكِّن تجار سلة من عرض منتجاتهم وتسويقها مجانًا لآلاف العملاء الجدد في مكان واحد. يمكن للعميل التجول بين عشرات آلاف المتاجر المحليَّة على منصة سلة، وملايين المنتجات المميَّزة، مع إمكانية البحث باسم المنتج وتصنيفه، والمدينة. ❓ ما هي شروط عرض منتجاتي على لمحلي؟ 1- ⟪أن يكون لديك متجر على سلة.⟫ 2- أن تكون مشتركًا بإحدى الباقات المدفوعة مثل باقة بلس أو برو. 3- أن يكون متجرك موثّقًا. 4- الموافقة على شروط الخصوصية والاستخدام لمنصة محلي. ❓ لماذا لا تظهر بعض منتجاتي في منصة محلي؟ قد لا تظهر منتجاتك في محلي إذا كان سعر المنتج 0 ريال، لأن محلي يعرض المنتجات التي يمكن شراؤها فقط. أما المنتجات التي نفدت كميتها، فستظل ظاهرة في محلي مع إتاحة خيار أبلغني عند توفر المنتج للعملاء. لضمان ظهور منتجاتك بشكل صحيح، تأكد من إضافة سعر مناسب لكل منتج وتحديث…

**Citation Q3-SA-C123:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1397 (article pvoh9k11k2sjti6k1xu667e5, منصة محلي والانضمام لها) | 2026-08-22 | kind: stated | quote check: found
- quote: أن تكون مشتركًا بإحدى الباقات المدفوعة مثل باقة بلس أو برو.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …%B9%D8%A9-%D8%AD%D9%88%D9%84-%D9%85%D9%86%D8%B5%D8%A9-%D9%85%D8%AD%D9%84%D9%8A-1/i6552boeb92lhuug905exq0i ❓ ما هي منصة محلي؟ محلي من سلة هي قناة بيع متكاملة تمكِّن تجار سلة من عرض منتجاتهم وتسويقها مجانًا لآلاف العملاء الجدد في مكان واحد. يمكن للعميل التجول بين عشرات آلاف المتاجر المحليَّة على منصة سلة، وملايين المنتجات المميَّزة، مع إمكانية البحث باسم المنتج وتصنيفه، والمدينة. ❓ ما هي شروط عرض منتجاتي على لمحلي؟ 1- أن يكون لديك متجر على سلة. 2- ⟪أن تكون مشتركًا بإحدى الباقات المدفوعة مثل باقة بلس أو برو.⟫ 3- أن يكون متجرك موثّقًا. 4- الموافقة على شروط الخصوصية والاستخدام لمنصة محلي. ❓ لماذا لا تظهر بعض منتجاتي في منصة محلي؟ قد لا تظهر منتجاتك في محلي إذا كان سعر المنتج 0 ريال، لأن محلي يعرض المنتجات التي يمكن شراؤها فقط. أما المنتجات التي نفدت كميتها، فستظل ظاهرة في محلي مع إتاحة خيار أبلغني عند توفر المنتج للعملاء. لضمان ظهور منتجاتك بشكل صحيح، تأكد من إضافة سعر مناسب لكل منتج وتحديث بياناته بشكل كامل. ❓ كيف يمكنني الخروج من المنصة بعد الانضمام؟…

**Citation Q3-SA-C124:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1397 (article pvoh9k11k2sjti6k1xu667e5, منصة محلي والانضمام لها) | 2026-08-22 | kind: stated | quote check: found
- quote: أن يكون متجرك موثقًا.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …pvoh9k11k2sjti6k1xu667e5 ما هي منصة محلي؟ محلي من سلة هي قناة بيع متكاملة تمكّن تجار سلة من عرض وتسويق منتجاتهم مجاناً لآلاف العملاء الجدد في مكان واحد، حيث يمكن للعميل التجول بين عشرات الآلاف من المتاجر المحلية على منصة سلة، وملايين المنتجات المميَّزة، مع إمكانية البحث باسم وتصنيف المنتج، والمدينة. محلِّي تجربة تسوُّق محليَّة فريدة! ما هي شروط الانضمام لمحلي؟ أن يكون لديك متجر على سلة. أن تكون مشتركًا بإحدى الباقات المدفوعة مثل باقة بلس أو برو. ⟪أن يكون متجرك موثقًا.⟫ الموافقة على شروط الخصوصية والاستخدام لمنصة محلي. 🔔 تنويه: بعد انضمامك لمنصة محلي، لا يمكنك إلغاء الانضمام أو الخروج من المنصة، وستبقى المنتجات المفعّلة ظاهرة. عند وجود أي إشكال، يُرجى التواصل مع مدير نجاح التجار خطوات الانضمام لمنصة محلي: 1. من قائمة (قنوات البيع) في القائمة الجانبية للوحة التحكم، اضغط (محلي). 2. من صفحة محلي، اضغط (اربط منتجاتك بمحلي) من أسفل الشاشة. في حال عدم استيفاء شرط من شروط الانضمام لمنصة محلي ستظهر رسالة تفيد بذلك. 3. …

**Citation Q3-SA-C125:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1397 (article pvoh9k11k2sjti6k1xu667e5, منصة محلي والانضمام لها) | 2026-08-22 | kind: stated | quote check: found
- quote: الموافقة على شروط الخصوصية والاستخدام لمنصة محلي.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …b92lhuug905exq0i ❓ ما هي منصة محلي؟ محلي من سلة هي قناة بيع متكاملة تمكِّن تجار سلة من عرض منتجاتهم وتسويقها مجانًا لآلاف العملاء الجدد في مكان واحد. يمكن للعميل التجول بين عشرات آلاف المتاجر المحليَّة على منصة سلة، وملايين المنتجات المميَّزة، مع إمكانية البحث باسم المنتج وتصنيفه، والمدينة. ❓ ما هي شروط عرض منتجاتي على لمحلي؟ 1- أن يكون لديك متجر على سلة. 2- أن تكون مشتركًا بإحدى الباقات المدفوعة مثل باقة بلس أو برو. 3- أن يكون متجرك موثّقًا. 4- ⟪الموافقة على شروط الخصوصية والاستخدام لمنصة محلي.⟫ ❓ لماذا لا تظهر بعض منتجاتي في منصة محلي؟ قد لا تظهر منتجاتك في محلي إذا كان سعر المنتج 0 ريال، لأن محلي يعرض المنتجات التي يمكن شراؤها فقط. أما المنتجات التي نفدت كميتها، فستظل ظاهرة في محلي مع إتاحة خيار أبلغني عند توفر المنتج للعملاء. لضمان ظهور منتجاتك بشكل صحيح، تأكد من إضافة سعر مناسب لكل منتج وتحديث بياناته بشكل كامل. ❓ كيف يمكنني الخروج من المنصة بعد الانضمام؟ بعد انضمامك لمنصة محلي، لا يمكنك إلغاء الانضمام أو الخروج منها، وستبقى المنتجا…

### Q3-SA-019

**Cited at:** section 1, line 51

**Record** (`studies/proposals/records/Q3/salla/statements.tsv`):
- stmt_id: Q3-SA-019
- bears_on: 4
- identifier: أسباب رفض طلب التوثيق وكيف تتجنبها
- statement: وثائق غير مرتبطة بهوية مالك المتجر يجب أن تكون كل الوثائق باسم مالك المتجر نفسه — وقد يؤدي خلاف ذلك إلى رفض نهائي
- cite_ids: Q3-SA-C039
- from: held
- note: One row of the table.

**Citation Q3-SA-C039:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1346 (article evrib312myg7282hjg7nlrje, متطلبات توثيق المتجر في سلة وأسباب رفض الطلب) | 2026-08-29 | kind: stated | quote check: found
- quote: وثائق غير مرتبطة بهوية مالك المتجر يجب أن تكون كل الوثائق باسم مالك المتجر نفسه — وقد يؤدي خلاف ذلك إلى رفض نهائي
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … الكويت بنك الخليج STC bank بنك الإمارات دبي الوطني بنك المشرق الإمارات أسباب رفض طلب التوثيق وكيف تتجنبها سبب الرفض أو التأخير كيف تتجنبه اسم صاحب الحساب البنكي لا يطابق الهوية أو السجل التجاري انسخ الاسم حرفياً من شهادة الآيبان، وتأكد من تطابقه مع وثيقة كيانك وثيقة منتهية الصلاحية (هوية، إقامة، عمل حر، سجل تجاري) تحقق من تاريخ الانتهاء قبل الرفع وجدّد الوثيقة إن لزم مستندات غير واضحة أو مقصوصة الأطراف ارفع الملف الأصلي بجودة عالية وبكامل حوافه ⟪وثائق غير مرتبطة بهوية مالك المتجر يجب أن تكون كل الوثائق باسم مالك المتجر نفسه - وقد يؤدي خلاف ذلك إلى رفض نهائي⟫ استخدام حساب بنكي شخصي لشركة أو مؤسسة افتح حساباً تجارياً باسم الكيان ومرتبطاً بالسجل التجاري تكرار إدخال بيانات خاطئة راجع الحقول قبل كل إرسال - التكرار قد يؤدي إلى رفض الطلب بشكل نهائي عدم اكتمال المتطلبات أكمل قائمة التحقق أعلاه قبل بدء الطلب لتفادي توقف العملية في منتصفها بعد إرسال الطلب يراجع فريق سلة بياناتك ومستنداتك. عند اكتمال البيانات وصحتها يُعتمد الطلب. تصلك رسالة تفيد بأنه تم توثيق متجرك بنجاح 🎉 وفي حال الرفض أو طلب تعديل، يمكنك تحد…
