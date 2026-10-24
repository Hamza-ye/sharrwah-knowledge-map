# Cards: Q1 on salla

13 records cited by `studies/proposals/drafts/Q1/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 8:** - Salla's market matches Shopify's on the term (basis 1, Salla's own translation counting): its help centre's الأسواق المتعددة copy a store "لكل دولة تستهدفها أو منطقة أو مدينة", and its dashboard text (observed, 8 October 2026) calls them "Markets". Q1-SA-K1976, Q1-SA-037
- **section 1, line 9:** - Zid's الأسواق manage prices and availability "حسب كل سوق جغرافي بشكل مستقل", matching Salla's on the term (basis 1) and Shopify's on role (basis 4). Q1-ZD-001, Q1-SA-K1976
- **section 1, line 12:** - What a market or storefront can set for itself, matching on role (basis 4): Shopify lists "currency, product availability, theme content, domains, languages, and taxes"; Salla's market page holds currencies, branches, shipping, domain, login options and design; a Zid market has a name, countries and "عملة السوق"; BigCommerce's storefronts set domains, themes, currencies and price lists. Q1-SH-K1931, Q1-SA-004, Q1-ZD-004, Q1-BC-005
- **section 1, line 13:** - Prices: Salla's are entered per market or follow "سعرها الأساسي وسعر الصرف للعملة"; Zid's are copied from the main market, converted at the current rate, or entered by hand; BigCommerce's price lists set "different prices in the same currency per different storefronts". Q1-SA-019, Q1-ZD-011, Q1-BC-034
- **section 1, line 14:** - Tax: on Salla "ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط"; BigCommerce and WooCommerce set rates by geography, in zones "based on country, state, or postal code" and, in WooCommerce's shipped code, by a rate's "2 digit country code". Q1-SA-023, Q1-BC-129, Q1-WC-024
- **section 1, line 15:** - Payment methods: Shopify shows local payment methods on a market's payments card when it "contains a country that is eligible"; Salla lets the merchant "تخصيص طرق الدفع حسب السوق الذي يختاره العميل"; BigCommerce sets them for each transactional currency. Q1-SH-051, Q1-SA-033, Q1-BC-053
- **section 1, line 17:** - What stays one for the whole store: on Shopify, "Staff permissions can't be assigned per market", while Salla can restrict a role "بحسب السوق المطلوب"; on BigCommerce, orders arrive in one area with "storefront attribution", and the store's address type and country are "inherently global" (not checked on Zid), as WooCommerce's store address, "the location where you are based as a seller", is one, a match on role (basis 4). Q1-SH-035, Q1-SA-028, Q1-BC-003, Q1-BC-018, Q1-WC-001
- **section 1, line 18:** - Placing a buyer, matching on role (basis 4): Shopify uses the IP address or "a market-specific domain, subdomain, or subfolder"; Salla's buyer picks the market; WooCommerce offers "Geolocate". Q1-SH-060, Q1-SH-061, Q1-SA-032, Q1-WC-005
- **section 1, line 19:** - Buyers outside the store's places, matching on role (basis 4): on Shopify they "can browse your store, but can't complete a purchase"; Salla's merchant can confine buying "على السوق المطابق لدولة العميل"; WooCommerce's shipped code has an optional zone for "any regions that have not been listed above". Q1-SH-018, Q1-SA-022, Q1-WC-027
- **section 1, line 25:** - Salla: the merchant sets markets in the dashboard under المزيد then الأسواق المتعددة, and their settings under الإعدادات. The store's language setting "ينطبق على السوق الافتراضي فقط", so the default market holds the store's own settings, partly overlapping Shopify's and BigCommerce's defaults. Its dashboard text (observed, 8 October 2026) says enabling Markets goes through the account manager. Q1-SA-018, Q1-SA-016, Q1-SA-045
- **section 1, line 33:** - Salla and Zid keep one set of terms across their countries. Salla's usage agreement, the same at salla.com/terms and salla.com/ar-ae/terms, names شركة تطبيق سلّة لتقنية المعلومات, follows Saudi law and states "كافة الرسوم تحتسب بالريال السعودي". Zid's, Zid Pay's for Kuwait included, follow Saudi law, though Zid Egypt "operates officially under Commercial Registration No.:201574". Q1-SA-094, Q1-SA-095, Q1-SA-096, Q1-ZD-K0212, Q1-ZD-K0221
- **section 2, line 62:** - It draws on WooCommerce's standard country list and BigCommerce's countries, states and provinces, with levels below country from Shopify's sub-region markets, Salla's markets for an "منطقة أو مدينة" and BigCommerce's tax zones. Why: places are data (rule 1) behind their own part (rule 2), with levels below country from the start, since adding them later changes every record naming a place (rule 3). Not taken: countries only, as in WooCommerce's selling locations, since Shopify and BigCommerce set delivery and tax below a country. Q1-WC-K1382, Q1-SH-022, Q1-SA-K1976, Q1-BC-129, Q1-WC-K0536
- **section 2, line 64:** - It takes the seller's place as the key, with a set-up for all other places, from Shopify's, BigCommerce's and WooCommerce's contracting parties; a per-country set of verification, payments, payouts and carriers from Salla's country articles; and an ordered provider list from WooCommerce's suggestions. Why: a new place is a new set-up, not new code (rule 1); terms per place change most, so this part hides them (rule 2); legal structure and partner contracts cost most to change, so the slots are fixed now and filled by company decisions (rule 3, section 7). Salla's and Zid's one set of terms is one value it can hold. Q1-WC-K0499, Q1-SA-076, Q1-WC-K0054, Q1-SA-094
- **section 2, line 73:** - Not taken: WooCommerce's store-wide places, since the other four set prices, currencies and content per place; and Salla's default market holding the store's settings, since explicit store defaults let a setting be set once and differ only where a market overrides it. Q1-WC-N01, Q1-SA-016
- **section 2, line 74:** - **Market selection**, proposed: a buyer is placed by the market's web address, else by choice, else by location; the seller can confine checkout to the market's places, and chooses the **fallback** for a buyer in no market, browsing only or buying in the home market, since Shopify blocks such buying while Salla and WooCommerce make it optional. The rest is left to the build (rule 3). Q1-SH-061, Q1-SA-032, Q1-SH-018, Q1-SA-022, Q1-WC-027
- **section 2, line 76:** - It takes the two kinds from BigCommerce's display and transactional currencies and Shopify's gateway-bound local currency, and the price modes from Salla's per-market or automatic prices and Zid's copied, converted or manual ones. Why: what the buyer is charged in decides what the provider must support and what reaches the seller (rule 3); rates come from sources that change, so the rate source is its own part (rule 2). Q1-SA-019, Q1-ZD-011, Q1-SH-057
- **section 2, line 78:** - It takes the offer by the seller's place from Shopify and WooCommerce, the seller's own credentials from Salla and Zid, the provider's underwriting from BigCommerce, methods per market from Shopify and Salla, and per currency from BigCommerce. Why: providers change, so they sit behind one interface (rule 2); and the seller contracts with the provider, which settles under that contract, as Salla's page on Tabby says, so no seller money is held through Sharrwah (rule 3, the guard). Q1-WC-K0054, Q1-ZD-K0094, Q1-SH-051, Q1-SA-033, Q1-SA-089
- **section 2, line 82:** - **Market access**, proposed and left to the build (rule 3): staff can be limited to a market, as on Salla and unlike Shopify, and apps reach markets through scopes, as Shopify's `read_markets`. Q1-SA-028, Q1-SH-035, Q1-SH-K0862
- **section 3, line 91:** - Set per market: its places and the settings it holds for itself (section 2). Q1-SH-K1931, Q1-SA-004
- **section 5, line 116:** - Levels below country. The records don't settle which settings vary below a country: Shopify's sub-region markets customize "only the shipping options", while Salla's markets reach an "منطقة أو مدينة" but tax by market needs "دولة واحدة فقط"; in Yemen, facts hold at cities and at areas of control (section 6). Keep the register's levels open, areas of control among them, and each setting's levels; the design settles them. Q1-SH-022, Q1-SA-K1976, Q1-SA-023, YK-12 (split @ Sana'a and Aden, as of 2026)

## The cards

### Q1-SA-K1976

**Cited at:** section 1, line 8; section 1, line 9; section 2, line 62; section 5, line 116

**Record** (`studies/proposals/records/Q1/salla/copied.tsv`):
- concern_id: SA-C-165
- placement: decides
- structure: https://help.salla.sa/article/تفعيل-وإدارة-الأسواق-المتعددة/wv9wyqrnhwpm6m2rp3cmg653
- identifier: 🚀الأسواق المتعددة
- statement: ميزة الأسواق المتعددة تمكنك من إنشاء نسخ مخصصة من متجرك الإلكتروني لكل دولة تستهدفها أو منطقة أو مدينة، بما يضمن ظهور المتجر للعملاء في هذه المنطقة بتجربة تتوافق مع توقعاتهم المحلية. يمكنك تخصيص سوق لأي دولة أو منطقة من دول الخليج من حيث:
- scope: أي دولة أو منطقة من دول الخليج
- cite_ids: SA-S-0157

**Citation SA-S-0157:** `https://help.salla.sa/article/تفعيل-وإدارة-الأسواق-المتعددة/wv9wyqrnhwpm6m2rp3cmg653` | 🚀الأسواق المتعددة (line 675 of the rendered text) | 2026-09-27 | kind: stated | quote check: found
- quote: ميزة الأسواق المتعددة تمكنك من إنشاء نسخ مخصصة من متجرك الإلكتروني لكل دولة تستهدفها أو منطقة أو مدينة، بما يضمن ظهور المتجر للعملاء في هذه المنطقة بتجربة تتوافق مع توقعاتهم المحلية. يمكنك تخصيص سوق لأي دولة أو منطقة من دول الخليج من حيث:
- title: تفعيل الأسواق المتعددة وإضافة سوق جديد | مركز المساعدة - سلة
- the page opens: تفعيل الأسواق المتعددة وإضافة سوق جديد مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سب…
- in context: …فعيل السوق 📍استعراض وزيارة السوق 🔍 البحث عن سوق 🗑️ حذف السوق 🛍️ ترتيب المنتجات حسب الأسواق الأسئلة الشائعة عند التوسع في أكثر من دولة أو مدينة أو منطقة، قد تواجه تحديات في تلبية اختلافات العملاء من حيث الأسعار والعملات واللغات. ميزة الأسواق المتعددة تتيح لك تقديم تجربة محلية مخصصة لكل سوق، مع إدارة مرنة للمخزون والطلبات. حل واحد يختصر التعقيدات ويمنح متجرك أداءً احترافياً في كل سوق. 🚀الأسواق المتعددة: قدّم تجربة تسوّق مخصصة لكل سوق بكل احترافية. ⟪ميزة الأسواق المتعددة تمكنك من إنشاء نسخ مخصصة من متجرك الإلكتروني لكل دولة تستهدفها أو منطقة أو مدينة، بما يضمن ظهور المتجر للعملاء في هذه المنطقة بتجربة تتوافق مع توقعاتهم المحلية. يمكنك تخصيص سوق لأي دولة أو منطقة من دول الخليج من حيث:⟫ - التصميم - الأسعار - العملة - دومين المتجر - خيارات الشحن كل نسخة تُدار بشكل مستقل مع نظام متكامل لإدارة المخزون والطلبات، ما يتيح لك توصيل الطلبات من أقرب فرع للعميل، ويسهم في تقليل تكاليف الشحن، وتسريع التوصيل، ورفع كفاءة العمليات. ✅ الميزة متاحة للمتاجر على باقة سبيشل. باختصار، تضع ميزة الأسواق المتعددة أدوات التوسّع الإقليمي بين يديك بسهولة، وفعالية، واحترافية. 🚀تفعيل الأسواق المتعددة: 1. من قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم ا…

### Q1-SA-037

**Cited at:** section 1, line 8

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-037
- bears_on: 2
- identifier: breadcrumb
- statement: "/localization":"Markets","/localization/$0":"Market #{{$0}}","/localization/journey":"Create new market","/localization/new":"New market","/localization/settings":"Settings"
- cite_ids: Q1-SA-C060;Q1-SA-C061;Q1-SA-C062;Q1-SA-C063
- from: held

**Citation Q1-SA-C060:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/localization.json` | breadcrumb | 2026-10-08 | kind: observed | quote check: found
- quote: "/localization":"Markets"
- in context: …and warehouses","no_selection_label":"No branches or warehouses added yet","no_selection_label_desc":"Search and add branches or warehouses.","show_product_availability_on_product_page":"Show product availability","stock_reduction":"Reduce stock","supported_branches_store_label":"Market branches and warehouses","supported_branches_store_placeholder":"Assign branches or warehouses to handle inventory and operations for this market"},"breadcrumb":{⟪"/localization":"Markets"⟫,"/localization/$0":"Market #{{$0}}","/localization/journey":"Create new market","/localization/new":"New market","/localization/settings":"Settings"},"common":{"active":"Active","add_new_store":"New market","cancel":"Cancel","confirm":"Confirm","default_store":"Default market","defualt_store":"Default store","email":{"label":"Email","placeholder":"Enter email address"},"facebook":{"label":"Facebook","placeholder":"Enter Facebook account link"},"…

**Citation Q1-SA-C061:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/localization.json` | breadcrumb | 2026-10-08 | kind: observed | quote check: found
- quote: "/localization/journey":"Create new market"
- title, opening and note boxes: as for this source's citation above
- in context: …s added yet","no_selection_label_desc":"Search and add branches or warehouses.","show_product_availability_on_product_page":"Show product availability","stock_reduction":"Reduce stock","supported_branches_store_label":"Market branches and warehouses","supported_branches_store_placeholder":"Assign branches or warehouses to handle inventory and operations for this market"},"breadcrumb":{"/localization":"Markets","/localization/$0":"Market #{{$0}}",⟪"/localization/journey":"Create new market"⟫,"/localization/new":"New market","/localization/settings":"Settings"},"common":{"active":"Active","add_new_store":"New market","cancel":"Cancel","confirm":"Confirm","default_store":"Default market","defualt_store":"Default store","email":{"label":"Email","placeholder":"Enter email address"},"facebook":{"label":"Facebook","placeholder":"Enter Facebook account link"},"instagram":{"label":"Instagram","placeholder":"Enter Instagram account link"},"m…

**Citation Q1-SA-C062:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/localization.json` | breadcrumb | 2026-10-08 | kind: observed | quote check: found
- quote: "/localization/new":"New market"
- title, opening and note boxes: as for this source's citation above
- in context: …ch and add branches or warehouses.","show_product_availability_on_product_page":"Show product availability","stock_reduction":"Reduce stock","supported_branches_store_label":"Market branches and warehouses","supported_branches_store_placeholder":"Assign branches or warehouses to handle inventory and operations for this market"},"breadcrumb":{"/localization":"Markets","/localization/$0":"Market #{{$0}}","/localization/journey":"Create new market",⟪"/localization/new":"New market"⟫,"/localization/settings":"Settings"},"common":{"active":"Active","add_new_store":"New market","cancel":"Cancel","confirm":"Confirm","default_store":"Default market","defualt_store":"Default store","email":{"label":"Email","placeholder":"Enter email address"},"facebook":{"label":"Facebook","placeholder":"Enter Facebook account link"},"instagram":{"label":"Instagram","placeholder":"Enter Instagram account link"},"mobile":{"label":"Mobile number","…

**Citation Q1-SA-C063:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/localization.json` | breadcrumb | 2026-10-08 | kind: observed | quote check: found
- quote: "/localization/settings":"Settings"
- title, opening and note boxes: as for this source's citation above
- in context: ….","show_product_availability_on_product_page":"Show product availability","stock_reduction":"Reduce stock","supported_branches_store_label":"Market branches and warehouses","supported_branches_store_placeholder":"Assign branches or warehouses to handle inventory and operations for this market"},"breadcrumb":{"/localization":"Markets","/localization/$0":"Market #{{$0}}","/localization/journey":"Create new market","/localization/new":"New market",⟪"/localization/settings":"Settings"⟫},"common":{"active":"Active","add_new_store":"New market","cancel":"Cancel","confirm":"Confirm","default_store":"Default market","defualt_store":"Default store","email":{"label":"Email","placeholder":"Enter email address"},"facebook":{"label":"Facebook","placeholder":"Enter Facebook account link"},"instagram":{"label":"Instagram","placeholder":"Enter Instagram account link"},"mobile":{"label":"Mobile number","placeholder":"0xx xxx xxxx"},"no_mor…

### Q1-SA-004

**Cited at:** section 1, line 12; section 3, line 91

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-004
- bears_on: 2
- identifier: 🚀 صفحة الأسواق المتعددة
- statement: تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين - خيارات الدخول والتسجيل - تصميم المتجر
- scope: من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة )
- cite_ids: Q1-SA-C010;Q1-SA-C011;Q1-SA-C012;Q1-SA-C013;Q1-SA-C014;Q1-SA-C015
- from: held

**Citation Q1-SA-C010:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🚀 صفحة الأسواق المتعددة | 2026-09-27 | kind: stated | quote check: found
- quote: تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها:
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …الشحن، وتسريع التوصيل، ورفع كفاءة العمليات. ✅ الميزة متاحة للمتاجر على باقة سبيشل. باختصار، تضع ميزة الأسواق المتعددة أدوات التوسّع الإقليمي بين يديك بسهولة، وفعالية، واحترافية. 🚀تفعيل الأسواق المتعددة: 1. من قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم اضغط ( الأسواق المتعددة ). 2. اضغط (فعل الآن). 3. للمضي قدماً في تفعيل الأسواق المتعددة، اضغط (تأكيد). 🚀 صفحة الأسواق المتعددة من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). ⟪تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها:⟫ - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين - خيارات الدخول والتسجيل - تصميم المتجر بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ). القسم 1…

**Citation Q1-SA-C011:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🚀 صفحة الأسواق المتعددة | 2026-09-27 | kind: stated | quote check: found
- quote: - المعلومات الأساسية حول السوق
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …اختصار، تضع ميزة الأسواق المتعددة أدوات التوسّع الإقليمي بين يديك بسهولة، وفعالية، واحترافية. 🚀تفعيل الأسواق المتعددة: 1. من قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم اضغط ( الأسواق المتعددة ). 2. اضغط (فعل الآن). 3. للمضي قدماً في تفعيل الأسواق المتعددة، اضغط (تأكيد). 🚀 صفحة الأسواق المتعددة من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: ⟪- المعلومات الأساسية حول السوق⟫ - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين - خيارات الدخول والتسجيل - تصميم المتجر بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ). القسم 1: المعلومات الأساسية اختر الدول…

**Citation Q1-SA-C012:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🚀 صفحة الأسواق المتعددة | 2026-09-27 | kind: stated | quote check: found
- quote: - الفروع والمستودعات
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …المُنشأة سابقاً، متضمنة: اسم الحدث ونوعه وهل هو مفعل أم معطل. 2- إنشاء ويب هوك جديد webhooks 1. من تبويب ال Webhooks، اضغط (إضافة Webhook جديد). 2. في صفحة الحدث الجديد، أدخل البيانات المطلوبة للحدث الجديد، ثم اضغط (حفظ). اسم الحدث: اختر اسم الحدث بحيث يعبر عن وظيفته. حدد نوع الحدث من قائمة الأحداث المتوفرة والتي تتضمن أحداث تخص: الشحن - شركات الشحن - الدفع - المنتجات - الكوبونات - بيانات العملاء - التصنيفات - العلامات التجارية - السلات المتروكة ⟪- الفروع والمستودعات⟫. نسخة إصدار الإشعار المرسل : يمكنك اختيار أحد الإصدارين: V1 أو V2. لك الحرية في إدخال أي شرط متقدم لفلترة البيانات المراد إرسالها عبر الويب هوك. أدخل رابط الخدمة التي سيُرسل إليها بيانات الحدث. 🔔 تنويه: قد لا تتضمن بعض إشعارات الويب هوك بيانات معينة مثل الطلبات (orders webhooks are hidden for now)، وذلك بناءً على تعديلات فنية وفق احتياجات محددة. يُنصح دائماً بمراجعة تفاصيل الحدث داخل لوحة التحكم للتحقق من البيانات المرسلة بدقة. 3- تفعيل/تعطيل وي…

**Citation Q1-SA-C013:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🚀 صفحة الأسواق المتعددة | 2026-09-27 | kind: stated | quote check: found
- quote: - معلومات التواصل
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …لة، وفعالية، واحترافية. 🚀تفعيل الأسواق المتعددة: 1. من قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم اضغط ( الأسواق المتعددة ). 2. اضغط (فعل الآن). 3. للمضي قدماً في تفعيل الأسواق المتعددة، اضغط (تأكيد). 🚀 صفحة الأسواق المتعددة من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن ⟪- معلومات التواصل⟫ - الدومين - خيارات الدخول والتسجيل - تصميم المتجر بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ). القسم 1: المعلومات الأساسية اختر الدول التي سيُعرض لها السوق، واسم يدل على هذه السوق، بالإضافة …

**Citation Q1-SA-C014:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🚀 صفحة الأسواق المتعددة | 2026-09-27 | kind: stated | quote check: found
- quote: - خيارات الدخول والتسجيل
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يل الأسواق المتعددة: 1. من قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم اضغط ( الأسواق المتعددة ). 2. اضغط (فعل الآن). 3. للمضي قدماً في تفعيل الأسواق المتعددة، اضغط (تأكيد). 🚀 صفحة الأسواق المتعددة من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين ⟪- خيارات الدخول والتسجيل⟫ - تصميم المتجر بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ). القسم 1: المعلومات الأساسية اختر الدول التي سيُعرض لها السوق، واسم يدل على هذه السوق، بالإضافة للغة الافتراضية واللغات الأخرى المد…

**Citation Q1-SA-C015:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), 🚀 صفحة الأسواق المتعددة | 2026-09-27 | kind: stated | quote check: found
- quote: - تصميم المتجر
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ن قائمة لوحة التحكم الرئيسية، اضغط (المنتجات)، ثم اضغط ( الأسواق المتعددة ). 2. اضغط (فعل الآن). 3. للمضي قدماً في تفعيل الأسواق المتعددة، اضغط (تأكيد). 🚀 صفحة الأسواق المتعددة من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). تحتوي صفحة الأسواق المتعددة على قائمة بالأسواق المُضافة ومعلومات حول كل سوق، أهمها: - المعلومات الأساسية حول السوق - العملات - الفروع والمستودعات - الشحن - معلومات التواصل - الدومين - خيارات الدخول والتسجيل ⟪- تصميم المتجر⟫ بالإضافة لحقل البحث عن سوق معين. 🚀 إدارة الأسواق المتعددة تتضمن إدارة الأسواق المتعددة ما يلي: 1- إضافة أسواق جديدة 2- تفعيل السوق 3- استعراض وزيارة السوق 4- البحث عن سوق 5- حذف السوق 🌟 إضافة أسواق جديدة 1. لإضافة سوق جديد ، اضغط (+ سوق جديد). 2. أدخل البيانات المطلوبة لإضافة السوق الجديد، واضغط (حفظ). القسم 1: المعلومات الأساسية اختر الدول التي سيُعرض لها السوق، واسم يدل على هذه السوق، بالإضافة للغة الافتراضية واللغات الأخرى المدعومة للسوق، وهل…

### Q1-SA-019

**Cited at:** section 1, line 13; section 2, line 76

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-019
- bears_on: 1;2
- identifier: ثانياً- تخصيص تسعير المنتجات
- statement: هل سيُدخل التاجر أسعار المنتجات بشكل مخصص لكل الأسواق أم سيعتمد تحديد سعر المنتجات تلقائياً بناء على سعرها الأساسي وسعر الصرف للعملة.
- cite_ids: Q1-SA-C038
- from: held

**Citation Q1-SA-C038:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 756 (article epj429qolc9kuugn5gqroamo, تخصيص إعدادات الأسواق المتعددة), ثانياً- تخصيص تسعير المنتجات | 2026-03-14 | kind: stated | quote check: found
- quote: هل سيُدخل التاجر أسعار المنتجات بشكل مخصص لكل الأسواق أم سيعتمد تحديد سعر المنتجات تلقائياً بناء على سعرها الأساسي وسعر الصرف للعملة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يًا إلى النطاق المخصّص لضمان عرض الأسعار واللغة والمحتوى الخاص بالسوق الإماراتي دون أي خطوات إضافية من العميل. 💡 مثال توضيحي: في حال تخصيص دومين للسوق. و تفعيل الخاصية. سيتم توجيه العميل إلى الدومين المخصص. وفي حال لم يكن هناك نطاق | دومين خاص بالسوق أو تم تعطيل الخاصية، سيتم توجيه العميل إلى الدومين الرئيسي للمتجر. ثانياً- تخصيص تسعير المنتجات يُشير تخصيص تسعير المنتجات إلى طريقة حساب وعرض أسعار المنتجات التي ستظهر في المتجر عند عرضه لسوق معين. ⟪هل سيُدخل التاجر أسعار المنتجات بشكل مخصص لكل الأسواق أم سيعتمد تحديد سعر المنتجات تلقائياً بناء على سعرها الأساسي وسعر الصرف للعملة.⟫ في حال اختار التاجر تسعير المنتجات وفق سعر مخصص من قبل التاجر سيتعين عليه إدخال الأسعار لمختلف الأسواق. حالات استخدام: تاجر يبيع منتجات إلكترونية تختلف أسعارها بين السعودية والإمارات بسبب الفروقات في تكلفة الشحن والضريبة. يقوم بإدخال سعر مخصص لكل سوق لتكون الأسعار دقيقة وملائمة. تاجر يبيع منتجات ذات سعر ثابت بالدولار. يفعّل "تسعير المنتجات حسب سعر الصرف"، ليتم احتساب السعر تلقائيًا وفق العملة المرتبطة بكل سوق دون الحاجة لإدخال السعر يدويًا. 💡 مث…

### Q1-SA-023

**Cited at:** section 1, line 14; section 5, line 116

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-023
- bears_on: 1;2
- identifier: خامساً- تفعيل الضريبة حسب دولة السوق
- statement: ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط.
- cite_ids: Q1-SA-C042
- from: held

**Citation Q1-SA-C042:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 756 (article epj429qolc9kuugn5gqroamo, تخصيص إعدادات الأسواق المتعددة), خامساً- تفعيل الضريبة حسب دولة السوق | 2026-03-14 | kind: stated | quote check: found
- quote: ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يود شحن). يمنع التنقل لضمان الالتزام بقوانين الشحن والتسعير الخاصة بكل دولة. رابعاً- تقييد الشراء حسب السوق احصر تجربة الشراء على السوق المطابق لدولة العميل، وقيِّد إتمام الطلب لعنوان توصيل خارج نطاق هذا السوق. حالة استخدام: متجر يوفّر التوصيل داخل السعودية فقط لاعتبارات لوجستية. عند تفعيل هذا الخيار، لا يتمكن العميل من إتمام الطلب إذا كان عنوان التوصيل خارج السعودية، مما يمنع الطلبات الخاطئة ويقلل الإلغاءات. خامساً- تفعيل الضريبة حسب دولة السوق ⟪ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط.⟫ حالة استخدام: متجر يبيع داخل الإمارات والسعودية. بما أن لكل دولة نظام ضريبة مختلف، يتم تفعيل الضريبة حسب دولة السوق بحيث تظهر الضريبة الإماراتية لعملاء الإمارات، والضريبة السعودية لعملاء السعودية، دون أي تدخل يدوي من التاجر. mfuh5y8na810irj8ecic2jaw https://help.salla.sa/article/%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5-%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF%D8%A7%D8%AA-%D8%A7%D9%84%D8%AA%D8%B3%D9%88%D9%8A%D9%82/mfuh5y8na810irj8ecic2jaw ربما واجهتك صعوبة في التحكم…

### Q1-SA-033

**Cited at:** section 1, line 15; section 2, line 78

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-033
- bears_on: 1;2;5
- identifier: الأسواق المتعددة
- statement: الأسواق المتعددة: يتيح لك تخصيص طرق الدفع حسب السوق الذي يختاره العميل، مثل إتاحة الدفع عند الاستلام في سوق وإخفائه في سوق آخر.
- scope: قيود الدفع
- cite_ids: Q1-SA-C056
- from: held

**Citation Q1-SA-C056:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), الأسواق المتعددة | 2026-09-29 | kind: stated | quote check: found
- quote: الأسواق المتعددة: يتيح لك تخصيص طرق الدفع حسب السوق الذي يختاره العميل، مثل إتاحة الدفع عند الاستلام في سوق وإخفائه في سوق آخر.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …معينة مثلا منعها عن العملاء غير الجادين. تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات من تصنيفات محددة في السلة، مثل إخفاء الدفع عند الاستلام عند شراء منتجات من تصنيف العناية بالبشرة. 📝 ملاحظة: إذا تم تفعيل الخيار واحتوت السلة على منتجات من التصنيفات المحددة في القيد، بالإضافة إلى منتجات من تصنيفات أخرى، فسيتم تطبيق الإجراء المحدد على الطلب. الشراء كضيف: يتيح لك تحديد القيود على طرق الدفع عند إتمام العميل للطلب دون تسجيل الدخول إلى حسابه. ⟪الأسواق المتعددة: يتيح لك تخصيص طرق الدفع حسب السوق الذي يختاره العميل، مثل إتاحة الدفع عند الاستلام في سوق وإخفائه في سوق آخر.⟫ طريقة الدفع الجزئي: تتيح لك تحديد طريقتي دفع لا يمكن للعميل استخدامهما معًا في الطلب نفسه، مثل منع الجمع بين رصيد المحفظة والدفع الآجل. 📝 ملاحظة : عند تفعيل رصيد المحفظة في الطلب، يمكنك منع استخدام طريقة دفع محددة معه، مثل طرق الدفع بالتقسيط. إذا كان الإجراء (إخفاء طريقة الدفع)، فستختفي طرق التقسيط المحددة للعميل: أما إذا كان الإجراء (رفض العملية)، فستظهر للعميل رسالة خطأ عند محاولة استخدامها، وسيظهر تنبيه للعميل عند الجمع بينهما. 6. حدد الإجراء…

### Q1-SA-028

**Cited at:** section 1, line 17; section 2, line 82

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-028
- bears_on: 1;2
- identifier: هل يمكنني تقييد صلاحيات موظف بسوق معين؟
- statement: نعم ، يمكنك تقييد دور الموظف بتقييد العناصر المطلوبة بحسب السوق المطلوب.
- cite_ids: Q1-SA-C048;Q1-SA-C049
- from: held

**Citation Q1-SA-C048:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 273 (article rvmsx19zkex4wgybruk7ovii, الأسئلة الشائعة حول الأسواق المتعددة), هل يمكنني تقييد صلاحيات موظف بسوق معين؟ | 2026-03-14 | kind: stated | quote check: found
- quote: نعم ، يمكنك تقييد دور الموظف
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …تفعيل خيار شحنات متعددة؟ ستختفي خيارات الشحن من صفحة الدفع للعميل. هل يمكن ل لطلب أن يحتوي على شحنات ك توصيل واستلام من الفرع سوياً؟ لا يمكن للطلب أن يحتوي على شحنات ك توصيل واستلام من الفرع سوياً إلا إذا تم التعديل عليه من قبل التاجر. حيث يستلم التاجر الطلبات من العميل إما ك توصيل أو استلام من الفرع. هل يمكنني تصفية الطلبات القادمة من سوق معين؟ نعم ، من صفحة ( إدارة الطلبات ) يمكنك تصفية الطلبات من أي سوق هل يمكنني تقييد صلاحيات موظف بسوق معين؟ ⟪نعم ، يمكنك تقييد دور الموظف⟫ بتقييد العناصر المطلوبة بحسب السوق المطلوب. لمزيد من التفاصيل حول إدارة موظفي المتجر عند إنشاء الطلب من قبل التاجر هل يمكن اختيار أكثر من شركة شحن للطلب؟ لا، سيتم تطبيق شركة الشحن والتكلفة على جميع الشحنات. إذا كان التاجر مفعل التصفح حسب المدينة، ومفعل انقاص الكمية حسب الفرع الذي فيه أكثر كمية، والعميل طلب منتج في مدينة معينة؟ يتم انقاص الكمية من الفرع الأكثر كمية في المدينة. bhsa3p5c3nvwu0qyqr3qennb https://help.salla.sa/article/%D8%A7%D9%84%D8…

**Citation Q1-SA-C049:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 273 (article rvmsx19zkex4wgybruk7ovii, الأسئلة الشائعة حول الأسواق المتعددة), هل يمكنني تقييد صلاحيات موظف بسوق معين؟ | 2026-03-14 | kind: stated | quote check: found
- quote: بتقييد العناصر المطلوبة بحسب السوق المطلوب.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … الاسترجاع. 1- نُنشئ دور جديد لموظف مسؤول عن تعديل طلبات الاسترجاع. حالياً، قبل تخصيص قيد على تعديل الطلبات يمكن للموظف تعديل جميع الطلبات التي أُضيف لها كموظف. 2- نخصص قيد العنصر الرئيسي ب (تعديل الطلبات) والعنصر الفرعي (تعديل الطلبات إلى حالة معينة) ثم نحدد قيمة العنصر (قيد الاسترجاع). بعد وضع القيد، بإمكان الموظف تعديل الطلبات المُضاف لها كموظف، ولكن التي حالتها قيد الاسترجاع فقط. 🔔 في حال تفعيل الأسواق المتعددة في متجر يمكنك تقييد دور الموظف ⟪بتقييد العناصر المطلوبة بحسب السوق المطلوب.⟫ 🔔 تنويه هام صلاحيات الدور الوظيفي الخاصة ب: محلي سلة بوينت سوق الجملة متاحة حالياً للمتاجر في المملكة العربية السعودية فقط. الأسئلة الشائعة ❓هل يمكن للموظف الدخول للوحة التحكم بدون دور وظيفي؟ لن يتمكن الموظف من تسجيل الدخول في حال لم يتم تحديد دور وظيفي له، وسيتم حذف حسابه تلقائياً بعد 15 يومًا إذا لم يتم تعيين دور. ❓هل يمكن تعديل صلاحيات دور وظيفي بعد إنشائه؟ نعم، يمكنك تعديل: اسم الدور الصلاحيات القيود وسيتم تطبيق التعديلات مباشرة على جميع الم…

### Q1-SA-032

**Cited at:** section 1, line 18; section 2, line 74

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-032
- bears_on: 1
- identifier: أولاً: تحديد السوق
- statement: عند دخول العميل للمتجر يمكنه تحديد السوق الذي يرغب بالشراء منه، وذلك حسب تخصيص التاجر لعرض المنتجات في المتجر.
- cite_ids: Q1-SA-C055
- from: held

**Citation Q1-SA-C055:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 738 (article gkq7zm64xnf29y8wew2r8x7h, تجربة العميل للأسواق المتعددة), أولاً: تحديد السوق | 2026-03-14 | kind: stated | quote check: found
- quote: عند دخول العميل للمتجر يمكنه تحديد السوق الذي يرغب بالشراء منه، وذلك حسب تخصيص التاجر لعرض المنتجات في المتجر.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …84-%D9%84%D9%84%D8%A3%D8%B3%D9%88%D8%A7%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%B9%D8%AF%D8%AF%D8%A9/gkq7zm64xnf29y8wew2r8x7h يواجه بعض العملاء صعوبة في تصفح المتجر بالشكل المناسب لبلدهم أو عملتهم. ميزة الأسواق المتعددة تحل هذه المشكلة عبر تخصيص تجربة العميل حسب السوق، و تساعد في عرض الأسعار، والعملات، وخيارات التوصيل بشكل دقيق لكل عميل. 🚀 خيارات العميل لإدارة مشترياته من متجر متعدد: للعميل عدة خيارات للشراء من متاجر التجزئة، أهمها: أولاً: تحديد السوق ⟪عند دخول العميل للمتجر يمكنه تحديد السوق الذي يرغب بالشراء منه، وذلك حسب تخصيص التاجر لعرض المنتجات في المتجر.⟫ ثم اختيار الفرع الذي يرغب بالتسوق منه، وضغط (تأكيد). ثانياً. تحديد الاستلام من فرع معين من صفحة الشراء اختيار استلام من الفرع، وتحديد الفرع حسب توفر المنتجات فيه وحسب الأقرب للعميل. ثالثاً. عرض تعدد الشحنات في صفحة تفاصيل الطلب عند العميل تُوضح الشحنات المصدرة للعميل في تفاصيل الطلب عند العميل، وتتضمن: - شركة الشحن - الفرع - المنتجات - الكميات - السعر - المجموع بالإضافة للبيانات الأخرى: - رقم البوليصة - حالة الشحن / تتبع الشحنة رابعاً. التحقق من…

### Q1-SA-022

**Cited at:** section 1, line 19; section 2, line 74

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-022
- bears_on: 1;2
- identifier: رابعاً- تقييد الشراء حسب السوق
- statement: احصر تجربة الشراء على السوق المطابق لدولة العميل، وقيِّد إتمام الطلب لعنوان توصيل خارج نطاق هذا السوق.
- cite_ids: Q1-SA-C041
- from: held

**Citation Q1-SA-C041:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 756 (article epj429qolc9kuugn5gqroamo, تخصيص إعدادات الأسواق المتعددة), رابعاً- تقييد الشراء حسب السوق | 2026-03-14 | kind: stated | quote check: found
- quote: احصر تجربة الشراء على السوق المطابق لدولة العميل، وقيِّد إتمام الطلب لعنوان توصيل خارج نطاق هذا السوق.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …م الشريط العلوي لإتاحة تغيير السوق بسهولة أثناء التصفح دون مقاطعة تجربة العميل. 2. نافذة منبثقة متجر يفضّل تحديد السوق منذ الزيارة الأولى لضمان عرض الأسعار الصحيحة مباشرة، مثل متجر يبيع منتجات تتأثر بشدة بتغيّر العملة والشحن. 3. تقييد التنقل بين الأسواق متجر يريد أن يتسوق العميل فقط في السوق الذي يطابق عنوانه (مثل متجر أدوية أو منتجات لها قيود شحن). يمنع التنقل لضمان الالتزام بقوانين الشحن والتسعير الخاصة بكل دولة. رابعاً- تقييد الشراء حسب السوق ⟪احصر تجربة الشراء على السوق المطابق لدولة العميل، وقيِّد إتمام الطلب لعنوان توصيل خارج نطاق هذا السوق.⟫ حالة استخدام: متجر يوفّر التوصيل داخل السعودية فقط لاعتبارات لوجستية. عند تفعيل هذا الخيار، لا يتمكن العميل من إتمام الطلب إذا كان عنوان التوصيل خارج السعودية، مما يمنع الطلبات الخاطئة ويقلل الإلغاءات. خامساً- تفعيل الضريبة حسب دولة السوق ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط. حالة استخدام: متجر يبيع داخل الإمارات والسعودية. بما أن لكل دولة نظام ضريبة مختلف، يتم تفعيل الضريبة حسب دولة السوق بحيث تظهر…

### Q1-SA-018

**Cited at:** section 1, line 25

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-018
- bears_on: 2
- identifier: 🚀 تخصيص إعدادات الأسواق المتعددة
- statement: 1. من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). 2. اضغط تبويب ( الإعدادات ).
- cite_ids: Q1-SA-C036;Q1-SA-C037
- from: held

**Citation Q1-SA-C036:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 756 (article epj429qolc9kuugn5gqroamo, تخصيص إعدادات الأسواق المتعددة), 🚀 تخصيص إعدادات الأسواق المتعددة | 2026-03-14 | kind: stated | quote check: found
- quote: 1. من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ).
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …/article/%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5-%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF%D8%A7%D8%AA-%D8%A7%D9%84%D8%A3%D8%B3%D9%88%D8%A7%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%B9%D8%AF%D8%AF%D8%A9/epj429qolc9kuugn5gqroamo توفر ميزة الأسواق المتعددة إمكانية تخصيص تجربة المتجر حسب السوق المستهدف. يمكنك من خلالها ضبط إعادة التوجيه، وتخصيص الأسعار، وتحديد طريقة اختيار السوق. في هذه المقالة، نستعرض خطوات تخصيص هذه الإعدادات بسهولة وفعالية. 🚀 تخصيص إعدادات الأسواق المتعددة ⟪1. من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ).⟫ 2. اضغط تبويب ( الإعدادات ). يمكنك تخصيص العديد من الإعدادات، وهي: أولاً- ضبط إعادة التوجيه متجر يمتلك نطاقًا مخصصًا للسوق الإماراتي (ae.example.com). عند زيارة عميل من الإمارات للمتجر، يتم توجيهه تلقائيًا إلى النطاق المخصّص لضمان عرض الأسعار واللغة والمحتوى الخاص بالسوق الإماراتي دون أي خطوات إضافية من العميل. 💡 مثال توضيحي: في حال تخصيص دومين للسوق. و تفعيل الخاصية. سيتم توجيه العميل إلى الدومين المخصص. وفي حال لم يكن هناك نطاق | دومين خاص بال…

**Citation Q1-SA-C037:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 756 (article epj429qolc9kuugn5gqroamo, تخصيص إعدادات الأسواق المتعددة), 🚀 تخصيص إعدادات الأسواق المتعددة | 2026-03-14 | kind: stated | quote check: found
- quote: 2. اضغط تبويب ( الإعدادات ).
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …F%D8%A7%D8%AA-%D8%A7%D9%84%D8%A3%D8%B3%D9%88%D8%A7%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%B9%D8%AF%D8%AF%D8%A9/epj429qolc9kuugn5gqroamo توفر ميزة الأسواق المتعددة إمكانية تخصيص تجربة المتجر حسب السوق المستهدف. يمكنك من خلالها ضبط إعادة التوجيه، وتخصيص الأسعار، وتحديد طريقة اختيار السوق. في هذه المقالة، نستعرض خطوات تخصيص هذه الإعدادات بسهولة وفعالية. 🚀 تخصيص إعدادات الأسواق المتعددة 1. من القائمة الرئيسية، اضغط (المزيد)، ثم اضغط ( الأسواق المتعددة ). ⟪2. اضغط تبويب ( الإعدادات ).⟫ يمكنك تخصيص العديد من الإعدادات، وهي: أولاً- ضبط إعادة التوجيه متجر يمتلك نطاقًا مخصصًا للسوق الإماراتي (ae.example.com). عند زيارة عميل من الإمارات للمتجر، يتم توجيهه تلقائيًا إلى النطاق المخصّص لضمان عرض الأسعار واللغة والمحتوى الخاص بالسوق الإماراتي دون أي خطوات إضافية من العميل. 💡 مثال توضيحي: في حال تخصيص دومين للسوق. و تفعيل الخاصية. سيتم توجيه العميل إلى الدومين المخصص. وفي حال لم يكن هناك نطاق | دومين خاص بالسوق أو تم تعطيل الخاصية، سيتم…

### Q1-SA-016

**Cited at:** section 1, line 25; section 2, line 73

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-016
- bears_on: 1;2
- identifier: ❓ هل إعداد اللغات من إعدادات المتجر ينطبق على جميع الأسواق؟
- statement: لا، ينطبق على السوق الافتراضي فقط. ويمكنك تحديد اللغات لكل سوق إضافي بشكل مستقل.
- cite_ids: Q1-SA-C034
- from: held

**Citation Q1-SA-C034:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 878 (article wv9wyqrnhwpm6m2rp3cmg653, تفعيل وإدارة الأسواق المتعددة), الأسئلة الشائعة | 2026-09-27 | kind: stated | quote check: found
- quote: لا، ينطبق على السوق الافتراضي فقط. ويمكنك تحديد اللغات لكل سوق إضافي بشكل مستقل.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ضغط (حذف) 🛍️ ترتيب المنتجات حسب الأسواق الآن يمكنك جعل متجرك يعكس ذوق واهتمام كل سوق على حدة من خلال ترتيب المنتجات داخل كل تصنيف بشكل مختلف بحسب السوق (الدولة). فالمفضّل في السعودية قد لا يكون نفسه في الإمارات، لذا يمكنك عرض المنتجات بترتيب مختلف في كل سوق لتناسب ثقافة واهتمامات عملائك المحليين. 📖 لمعرفة طريقة ترتيب المنتجات لكل سوق: طلع على مقالة إدارة تصنيفات المنتجات الأسئلة الشائعة ❓ هل إعداد اللغات من إعدادات المتجر ينطبق على جميع الأسواق؟ ⟪لا، ينطبق على السوق الافتراضي فقط. ويمكنك تحديد اللغات لكل سوق إضافي بشكل مستقل.⟫ ❓ كيف أحدد اللغات للأسواق المتعددة في متجري؟ من إعدادات كل سوق، يمكنك تحديد اللغات الخاصة به بشكل مستقل. koda8pykc6pdhylg7zb2iu0g https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%88%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%B9%D9%86%D8%AF-%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%84%D8%A7%D9%85-%D9%85%D8%B9-%D8%A8%D9%88%D9%84%D9%8A%D8%B5%D8%A7%D8%AA-%D8%B3%D9%84%D8%A9/koda8pykc6pdhylg7zb2iu0g هل تواجه تحديات في إدا…

### Q1-SA-045

**Cited at:** section 1, line 25

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-045
- bears_on: 4
- identifier: feature.feature_desc
- statement: Contact your account manager to enable this feature.
- scope: feature.feature_name: Markets
- cite_ids: Q1-SA-C071
- from: held

**Citation Q1-SA-C071:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/localization.json` | feature.feature_desc | 2026-10-08 | kind: observed | quote check: found
- quote: Contact your account manager to enable this feature.
- in context: …ns Select market subdomain Existing subdomain Select subdomain You need to add your store domain in Salla to link it to the market. Enter subdomain The subdomain name can't include numbers. Activate Start creating new markets and selling in multiple countries. Enable multi-market feature Activating this changes how customers browse and view pricing. To disable it later, you'll need to contact your account manager. Confirm activating this feature ⟪Contact your account manager to enable this feature.⟫ Markets Back Branches and warehouses Create market Customize Choose the default storefront language carefully. It can't be changed after the market is created. e.g. Saudi Arabia market Create your first market and choose the countries and settings that best fit your customers. Your market will be ready in a moment. Creating your market Default market Maintenance Maintenance title must be at least 5 characters and the message at least 15 characte…

### Q1-SA-094

**Cited at:** section 1, line 33; section 2, line 64

**Record** (`studies/proposals/records/Q1/salla/statements.tsv`):
- stmt_id: Q1-SA-094
- bears_on: 3
- identifier: المقدّمة
- statement: منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513 ترحّب بكم ، وتبلغكم بأنكم سوف تجدون أدناه الشروط والأحكام المُنظّمة لاستخدامكم لمنصة سلّة
- scope: https://salla.com/terms; https://salla.com/ar-ae/terms
- cite_ids: Q1-SA-C141;Q1-SA-C142
- from: held
- note: bears on copied gaps Q1-SA-G0161 and Q1-SA-G0213 for the pages at salla.com/terms and salla.com/ar-ae/terms; no Kuwait version is held

**Citation Q1-SA-C141:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 16 (المقدّمة) | 2026-10-06 | kind: official page | quote check: found
- quote: منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513
- in context: شروط وأحكام استخدام منصة سلة الحلول الموارد القطاعات سلة سبيشل الأسعار En تسجيل دخول أنشئ متجرك مجانًا أنشئ متجرك مجانًا اتفاقية الاستخدام A A A المقدّمة: ⟪منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513⟫ ترحّب بكم ، وتبلغكم بأنكم سوف تجدون أدناه الشروط والأحكام المُنظّمة لاستخدامكم لمنصة سلّة وكافة الآثار القانونية التي تنتج عن استخدامكم لخدمات منصة سلّة في الشبكة العنكبوتية ، حيث أن استخدام أي شخصٍ كان لمنصة سلّة سواءً كان مستهلكاً أو تاجراً أو غير ذلك فإن هذا يُعد موافقة وقبول منه وهو بكامل أهليته المعتبرة شرعاً ونظاماً وقانوناً لكافة مواد وبنود وأحكام هذه الاتفاقية وهو تأكيد لالتزامكم بأنظمتها ولما ذُكر فيها، ونشير إليكم بأن منصة سلّة قد تكون…

**Citation Q1-SA-C142:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` | offset 3700206 (https://salla.com/ar-ae/terms), المقدّمة | 2026-10-06 | kind: stated | quote check: found
- quote: منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513
- title: شروط وأحكام استخدام منصة سلة
- in context: شروط وأحكام استخدام منصة سلة ')"> الحلول الموارد القطاعات سلة سبيشل الأسعار En تسجيل دخول أنشئ متجرك مجانًا أنشئ متجرك مجانًا ')"> اتفاقية الاستخدام A A A المقدّمة: ⟪منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513⟫ ترحّب بكم ، وتبلغكم بأنكم سوف تجدون أدناه الشروط والأحكام المُنظّمة لاستخدامكم لمنصة سلّة وكافة الآثار القانونية التي تنتج عن استخدامكم لخدمات منصة سلّة في الشبكة العنكبوتية ، حيث أن استخدام أي شخصٍ كان لمنصة سلّة سواءً كان مستهلكاً أو تاجراً أو غير ذلك فإن هذا يُعد موافقة وقبول منه وهو بكامل أهليته المعتبرة شرعاً ونظاماً وقانوناً لكافة مواد وبنود وأحكام هذه الاتفاقية وهو تأكيد لالتزامكم بأنظمتها ولما ذُكر فيها، ونشير إليكم بأن منصة سلّة قد تكون…
