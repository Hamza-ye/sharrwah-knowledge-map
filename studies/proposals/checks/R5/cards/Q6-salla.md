# Cards: Q6 on salla

20 records cited by `studies/proposals/drafts/Q6/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Who registers, a match on role, in their terms and, for Shopify's business entity, its help: on Shopify the person who opens the account is the contracting party, the "Store Owner", or the employer they sign up for, and the business entity is "the registered business, or the individual, that your store operates as"; Salla's merchant registers "سواءً كان شخص طبيعي أو معنوي". Shopify asks for full legal name, business address, phone number and email, and Salla checks the phone with a code. Q6-SH-K1237; Q6-SH-003; Q6-SH-K1260; Q6-SA-014; Q6-SH-K1238; Q6-SA-002
- **section 1, line 8:** - Conditions, a match on role: Shopify takes 18 or "the age of majority in the jurisdiction where you reside", whichever is older, and Zid 18 or the age of majority of "الدولة التي تستخدم منها الخدمة", both taking it from the seller's own place. Salla takes eighteen "كما هو معتبر في القوانين والأنظمة المرعية بالمملكة العربية السعودية", one country's law, and lets a minor trade with the guardian's consent. Shopify also requires "a business activity and not for any personal, household or family purpose", and may reject an application "for any reason, at our sole discretion". Q6-SH-001; Q6-ZD-009; Q6-SA-011; Q6-SA-012; Q6-SH-002; Q6-SH-K1238
- **section 1, line 9:** - Entity types: Salla and Zid name the same four in the same words, a match on term: Salla's "فرداَ, مؤسسة, شركة, أو جمعية خيرية" and Zid's "فرد، مؤسسة، شركة، جمعية خيرية". For country code YE, Shopify's admin offered an "Individual" type, observed for store ctcbwa-r1 on 30 September 2026; the same day, the saved markup's text of store ibx5bt-xy's organization step held two Yemen entities, one "Company" and one "Individual", words its accessibility tree also showed. The types differ by place: Salla's Saudi individual type is "للمواطنين السعوديين فقط", and on WooCommerce "Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type." Q6-SA-026; Q6-ZD-K0239; Q6-SH-K2674; Q6-SH-045; Q6-WC-006
- **section 1, line 10:** - The seller's place: Shopify, Salla, Zid and WooCommerce each ask where the seller is, a match on role, but key it differently. Shopify's sign-up has a location field, observed on 6 October 2026, and its billing address "must match the country of one of your active business entities"; in store ibx5bt-xy, observed 30 September 2026, the saved markup's text of the billing-address step holds two legal entities marked "YE" and "Country/region [Yemen] Yemen", words its accessibility tree also showed. Salla's onboarding, observed for store store-sherawya on 8 October 2026, asks "Where is your business based?" with `"is_mandatory": true`, meaning "the country where your business is legally registered or where you issue official documents". For WooPayments the country is "the one where your business is registered — not the one in which you personally live". Zid asks for "تحديد موقعك أو موقع المخزون". The store records are observed, the others help pages. Q6-SH-043; Q6-SH-K1259; Q6-SH-046; Q6-SA-059; Q6-WC-K0402; Q6-ZD-K0231
- **section 1, line 11:** - What the place sets, a match on role: Salla's dashboard strings, observed on 8 October 2026, say "اختيارك للدولة يحدِّد المتطلبات القانونية اللازمة لمتجرك."; Zid, "تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة."; and on Shopify the billing address decides bill taxes, payment methods, billing currencies and "the Shopify company that issues your bill". Q6-SA-008; Q6-ZD-K0240; Q6-SH-013
- **section 1, line 15:** - Salla's agreement, as served at its UAE address, names a company registered in Saudi Arabia, and which Salla company contracts in each market was not found. Zid's terms name one Saudi company and Saudi law. Q6-SA-023; Q6-SA-G0213; Q6-ZD-K0214; Q6-ZD-K0211
- **section 1, line 19:** - Documents: Salla's agreement asks every store for "سجل تجاري قائم أو وثيقة عمل حر" and licences "كحساب أبشر وحساب بنكي في أحد البنوك السعودية ورقم جوال سعودي", and a foreign merchant's verification needs a "سجلاً تجارياً سعودياً". Zid asks for a commercial registration only "إلا إن كنت ترغب بربط المتجر ببوابات الدفع". Q6-SA-019; Q6-SA-035; Q6-ZD-K0241
- **section 1, line 20:** - Verification as a gate, a match on role: without Salla's verification "يتم تعليق عمليات الدفع والسداد", and on "باقة بيسك" "التحقق متطلب أساسي للبدء في عملية البيع"; for store store-sherawya, observed 8 October 2026, Salla's payment data gave `"blocks_payment_activation": true`. On BigCommerce's payment service, funds "may be held or blocked", and the seller is told to complete any requests for documents or verification. Q6-SA-037; Q6-SA-036; Q6-SA-061; Q6-BC-P0084
- **section 1, line 21:** - Who verifies differs: on Salla, "يقوم فريق سلة بمراجعة طلب التوثيق."; on Zid the documents go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and Zid Pay needs the store owner to pass Nafath; WooCommerce sellers "verify your personal and business information with Stripe". Q6-SA-K0087; Q6-ZD-K0003; Q6-ZD-K0261; Q6-WC-K0393
- **section 1, line 27:** - What a seller elsewhere uses, a match on role: on Shopify, a third-party provider, for which Shopify charges transaction fees by plan while "Your third-party payment provider charges you their credit card rates themselves, separately."; on Zid, by its Gulf store-creation article, Tap: "يمكنك تفعيل بوابة الدفع تاب من خلال الاعدادات > طرق الدفع"; on Salla, for a store outside Saudi Arabia, Tabby: "تواصل مع تابي مباشرة لاستكمال إعداد حساب التاجر". On BigCommerce, "Each provider has its own application process." Q6-SH-024; Q6-ZD-K0090; Q6-SA-056; Q6-BC-P0048
- **section 1, line 31:** - Saying so at sign-up: Salla's dashboard strings, captured 8 October 2026, hold for another country "We’re currently available in Saudi Arabia and the UAE. We’ll notify you when Salla becomes available in your country."; what follows choosing another country in the onboarding was not held. Q6-SA-007; Q6-SA-N03
- **section 1, line 32:** - Zid's FAQ, dated 30 August 2023, says "حاليًا زد يخدم التجار المتواجدين في السعودية ودول الخليج فقط من جميع الجنسيات" and "في المستقبل باذن الله نتوسع للعالم العربي."; its site index, read 12 October 2026, lists pages for Egypt, the UAE, Kuwait, Oman and Syria. The two disagree on whether Zid serves only Saudi Arabia and the Gulf, and the proposal rests on neither list. Zid's FAQ and Salla's string above match on role: each says where the platform serves now and that more places will follow; Salla's is observed, Zid's stated. Q6-ZD-K0226; Q6-ZD-024; Q6-ZD-K0225; Q6-SA-007
- **section 1, line 33:** - Saying so for one part, a match on role with Salla's notice: WooCommerce asks sellers to "vote for your country to be supported", and weighs "the number of requests by WooCommerce store owners in that country"; BigCommerce says of its payment service "Additional regions and countries will be launching soon."; these are help pages, Salla's notice observed. Q6-WC-007; Q6-WC-K0403; Q6-BC-P0030; Q6-SA-007
- **section 1, line 34:** - Saying so in the admin, a match on role: Salla's strings hold "التحويل البنكي غير متاح حالياً لدولتك ({{country}})."; Zid's API answers stores in other currencies `Customer wallets is only available for GCC countries.`; Salla's payment data, observed for store real-merchant on 12 October 2026, give each method `"available_countries": []` and `"unavailable_reason": null`. Salla's records are observed, Zid's stated. Q6-SA-058; Q6-ZD-025; Q6-SA-062
- **section 2, line 38:** - **Seller**: in Sharrwah's proposed design, the party Sharrwah contracts with, an individual or an organization, following Shopify's contracting "Store Owner" and Salla's merchant, "سواءً كان شخص طبيعي أو معنوي". It accepts Sharrwah's seller terms on registering and may own several stores, as one Salla owner may. Rule 3: the data model is expensive to change after launch. Q6-SH-K1237; Q6-SA-014; Q6-SA-038
- **section 2, line 39:** - **Account user**: the person who signs up and acts in Sharrwah. One who registers for an employer makes the employer the Seller, as on Shopify, and Sharrwah checks the user's phone at sign-up, as Salla does. Rule 3, for the same reason. Q6-SH-003; Q6-SA-002
- **section 2, line 40:** - **Eligibility rules**: what Sharrwah requires to register, held per place in the **Place set-up**: a minimum age of 18 or the place's age of majority, whichever is older, following Shopify and Zid, which take it from the seller's own place, not Salla's tie to one country's law, since Sharrwah is built once for several places (rule 1); a business purpose, as on Shopify; and Sharrwah's right to refuse, as Shopify keeps. Whether minors may register through a guardian is a company decision (section 7). Q6-SH-001; Q6-ZD-009; Q6-SA-011; Q6-SH-002; Q6-SH-K1238
- **section 2, line 41:** - **Seller entity**: the registered business, or the individual, that a Seller trades as: its type, its place of registration, its documents and its bank details. The types offered are set per place, since Salla limits its individual type to Saudi citizens and WooCommerce gives UAE businesses none; Salla's and Zid's four shared types are the starting list; for Yemen, the saved markup's text of store ibx5bt-xy's organization step held a company and an individual, on 30 September 2026. A Seller may hold several entities, as Shopify's billing rule speaks of "one of your active business entities" and that step held two; the first build gives each store one, and the data model keeps more (rule 3). Q6-SH-K1260; Q6-SA-026; Q6-ZD-K0239; Q6-WC-006; Q6-SH-045; Q6-SH-K1259
- **section 2, line 42:** - **Business place**: the place a Seller's business is based, which sets its requirements, its contracting company and the parts open to it. For a registered business it is where the business is registered, following Salla's question, observed for store store-sherawya on 8 October 2026, and WooCommerce's rule; for an individual, where they reside and trade, as Shopify's age rule reads. Sharrwah asks it at sign-up and requires it, as Salla does, offering the places Sharrwah has set up and an option for any other. Rules 1 and 3. Q6-SA-059; Q6-WC-K0402; Q6-SH-001
- **section 2, line 43:** - Sharrwah also records the address the seller sells or ships from, which Zid accepts as the location, and a billing address. Neither is the key: a place's documents follow where the business is registered, as Salla's step gives its reason, "لأن ذلك يحدد الوثائق الحكومية", and Shopify itself ties its billing address to an entity's country. Q6-ZD-K0231; Q6-SA-K0083; Q6-SH-K1259
- **section 2, line 44:** - **Place set-up**: for each place Sharrwah serves, one record of what differs there: whether registration is open; the entity types and the documents each needs; the age of majority; the contracting company and any supplement to the terms; the parts available, with their providers in order; and the wording of notices. This is rule 1, following Salla's country choice that sets legal requirements, in its dashboard strings, Zid's requirements by type and country, Shopify's billing address and WooCommerce's list per country. Q6-SA-008; Q6-ZD-K0240; Q6-SH-013; Q6-WC-K0054
- **section 2, line 47:** - **Contracting company map**: which Sharrwah company contracts with a Seller, chosen by its **Business place**, with a row for any other place, and each place's supplement to the seller terms. It follows Shopify, BigCommerce and WooCommerce, which choose the company by the seller's place, and BigCommerce's supplements. It sits behind its own part (rule 2), and its structure is decided now (rule 3: legal structure and partner contracts); with one company, it has one row. Not taken: one company written into the terms, as Salla's and Zid's terms read, since adding a company later would then touch every seller's contract. Q6-SH-K1243; Q6-BC-008; Q6-BC-K0425; Q6-WC-K0498; Q6-BC-010; Q6-SA-023; Q6-ZD-K0214
- **section 2, line 48:** - **Verification**: checks in stages, each opening particular capabilities, with requirements set per place and entity type in the **Place set-up**. First, the Account user's phone at sign-up. Second, the Seller entity's identity and documents, before Sharrwah activates any part that takes payments or pays out, as Salla's payment data showed `"blocks_payment_activation": true` for store store-sherawya on 8 October 2026, and WooCommerce has sellers verify with Stripe when they sign up for its payments. Third, a provider's own checks when it plugs in. A store can be built and opened before the second stage, as on Zid, where a commercial registration is needed only to connect payment gateways; whether the second stage comes before any selling, as on Salla's "باقة بيسك", is set per place in the **Place set-up** (rule 1). Q6-SA-061; Q6-WC-K0393; Q6-ZD-K0241; Q6-SA-036; Q6-BC-P0048
- **section 2, line 49:** - Gating activation, not money: Sharrwah takes no payment for a seller before the second stage, rather than suspending payments and settlement afterwards, as Salla's FAQ describes, or holding funds, as BigCommerce's payment service may. Either would hold sellers' money, and under the guard could go live only by the founder's decision. Rule 3: money flows are decided now. Q6-SA-037; Q6-BC-P0084
- **section 2, line 50:** - Who reviews, Sharrwah's own team as on Salla, or the provider as on Zid, stays open (section 5). Q6-SA-K0087; Q6-ZD-K0003
- **section 2, line 51:** - **Part availability**: for each part Sharrwah offers, its own or a provider's, where it is available: the places, and, where the evidence shows a second key, the currencies, plans and product types; with a reason when a seller can't use it. Zid limits a part by place, BigCommerce adds currency, Shopify plan and product type, and Salla's payment data, observed for store real-merchant on 12 October 2026, carry per method `"available_countries": []` and `"unavailable_reason": null`. Rule 2: availability is data per part, so opening a part in a new place changes no code. Q6-ZD-K0177; Q6-BC-022; Q6-SH-030; Q6-SA-062
- **section 2, line 53:** - Two arrangements are possible: the seller contracts with the provider directly, as Salla tells stores outside Saudi Arabia to do with Tabby, or an account is opened through the platform, as WooPayments signup creates a Stripe Express account. Under the guard, an arrangement in which a provider holds sellers' money in an account opened through Sharrwah goes live only by the founder's decision. Q6-SA-056; Q6-WC-K0393
- **section 2, line 54:** - **Availability notice**: how Sharrwah says something isn't available, built from the **Place set-up** and **Part availability** and never written screen by screen (rule 2): at sign-up, when the Business place isn't set up, a message naming where Sharrwah serves now, as Salla's dashboard strings, captured 8 October 2026, do; in the admin, where the part is used, naming the seller's place, as Salla's bank-transfer string does; and through the API, as Zid's message does. Whether a place not set up gets this notice, or a store with fewer parts as Shopify gave a sign-up from Yemen, stays open (section 5). Q6-SA-007; Q6-SA-058; Q6-ZD-025; Q6-SH-011
- **section 2, line 55:** - **Place interest list**: a seller from a place not set up can leave its details and be told when Sharrwah opens there, as Salla's strings promise; the requests count toward which places come next, as WooCommerce counts them. Q6-SA-007; Q6-WC-K0403
- **section 3, line 60:** - Plugs in: payment providers, and providers of other parts such as pay-later, each with its own places, approval and rules, as BigCommerce's application process, Zid's gateway approval and Salla's direct Tabby account show. Q6-BC-P0048; Q6-ZD-K0003; Q6-SA-056
- **section 3, line 63:** - Set per place and entity type: the entity types and their documents, as Salla's verification and Zid's note show; the age of majority per place, as Shopify and Zid take it. Q6-SA-026; Q6-ZD-K0240; Q6-SH-001; Q6-ZD-009
- **section 3, line 68:** - The seller sets its **Business place** and **Seller entity**, as Salla's onboarding asked for store store-sherawya on 8 October 2026, and picks a provider, as Salla's stores outside Saudi Arabia set up Tabby themselves. Q6-SA-059; Q6-SA-056
- **section 3, line 70:** - Government bodies issue the documents a place requires, as Salla's step says, and run identity checks, as Nafath for Zid Pay. Q6-SA-K0083; Q6-ZD-K0261
- **section 5, line 88:** - Which address decides what: the place of registration on Salla, observed for store store-sherawya on 8 October 2026, and on WooCommerce, residence on BigCommerce, the billing address on Shopify, the seller's or inventory's location on Zid. The design records each address apart, and each rule names the address it reads; the company decision on contracting, with a lawyer's advice to the founder, settles which address keys the contract. Q6-SA-059; Q6-WC-K0402; Q6-BC-008; Q6-SH-K1243; Q6-ZD-K0231
- **section 5, line 89:** - Whether a seller from a place not set up may register with fewer parts, or is turned away: on Shopify a sign-up from Yemen created store 2jiwxs-gr on 6 October 2026, and its own payment service was not eligible for store ts15uk-ug, with its entity in Yemen, on 7 October 2026; Salla's dashboard strings, captured 8 October 2026, turn another country away with a notice. The design keeps registration and each part's availability as separate settings per place; the founder settles each place on deciding to enter it. Q6-SH-011; Q6-SH-036; Q6-SA-007
- **section 5, line 90:** - Who verifies: Salla's own team, or the payment provider on Zid and WooCommerce. The design keeps **Verification** behind an interface that a Sharrwah review or a provider's check can fill; partner contracts settle it. Q6-SA-K0087; Q6-ZD-K0003; Q6-WC-K0393
- **section 5, line 92:** - A payment service or wallet of Sharrwah's own: Salla suspends payments and settlement until a store is verified, and BigCommerce's payment service holds a new account's first payments before payout. The design keeps payments behind **Provider choice**, so that such a service, if the founder decides on one, plugs in as one more provider; under the guard, nothing that holds sellers' money goes live without the founder's decision. Q6-SA-037; Q6-BC-P0084
- **section 5, line 93:** - Several entities and stores per Seller: Shopify's billing rule speaks of several active entities, store ibx5bt-xy's organization step held two in its saved markup's text on 30 September 2026, and Salla sets no limit on stores per owner. The data model keeps a Seller with many **Seller entity** records and stores from the start; the first build uses one entity per store. Q6-SH-K1259; Q6-SH-045; Q6-SA-038
- **section 5, line 94:** - Businesses registered outside the place they sell in: Salla requires a Saudi commercial registration of a foreign merchant, and Zid serves sellers "من جميع الجنسيات". The design keeps an entity's place of registration apart from the places it may sell in; a company decision settles who may register from abroad (section 7). Q6-SA-035; Q6-ZD-K0226
- **section 7, line 114:** - Who may register: the minimum age and minors through a guardian; individuals without a commercial registration; businesses registered outside the place. Q6-SH-001; Q6-SA-012; Q6-ZD-K0241; Q6-SA-019; Q6-SA-035
- **section 7, line 115:** - Which payment providers and other partners Sharrwah works with in each place, and whether any would hold sellers' money in an account opened through Sharrwah, which goes live only by the founder's decision. Q6-SH-041; Q6-SH-048; Q6-WC-K0333; Q6-WC-K0393; Q6-SA-056
- **section 7, line 116:** - Whether Sharrwah reviews sellers itself, and against which identity sources. Q6-SA-K0087; Q6-ZD-K0261
- **section 7, line 118:** - Whether Sharrwah offers a payment service of its own, or any arrangement holding sellers' money, anywhere: under the guard, only by the founder's decision. Q6-SA-037; Q6-BC-P0084

## The cards

### Q6-SA-014

**Cited at:** section 1, line 7; section 2, line 38

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-014
- bears_on: 1
- identifier: ( التاجر )
- statement: ( التاجر ) يقصَد بهذه العبارة كل تاجر يسجّل في منصة سلة لإنشاء متجره الالكتروني، سواءً كان شخص طبيعي أو معنوي، ويشمل هذا التعريف كافة أوجه المتجر طالما أنه يقوم بتجارته عن طريق منصة سلة، ويشمل ذلك الموقع الالكتروني للتاجر.
- cite_ids: Q6-SA-C020
- from: held

**Citation Q6-SA-C020:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 20 (المادة الأولى – المقدّمة والتعريفات) | 2026-10-06 | kind: official page | quote check: found
- quote: ( التاجر ) يقصَد بهذه العبارة كل تاجر يسجّل في منصة سلة لإنشاء متجره الالكتروني، سواءً كان شخص طبيعي أو معنوي، ويشمل هذا التعريف كافة أوجه المتجر طالما أنه يقوم بتجارته عن طريق منصة سلة، ويشمل ذلك الموقع الالكتروني للتاجر.
- in context: …ا والبدء في التسجيل بمنصة سلّة. المادة الأولى - المقدّمة والتعريفات: يعتبر التمهيد أعلاه جزءاً لا يتجزأ من هذه الاتفاقية، كما تجدون أدناه الدلالات والتعريفات للعبارات الرئيسية المستخدمة في هذه الاتفاقية: ( منصة سلّة المملوكة لشركة سلّة القابضة ) يقصَد بهذه العبارة شركة تطبيق سلة لتقنية المعلومات، ويشمل هذا التعريف كافة أشكال شركة تطبيق سلّة لتقنية المعلومات على الشبكة العنكبوتية، سواءً كانت تطبيق الكتروني، أو موقع الكتروني على الشبكة العنكبوتية. ⟪( التاجر ) يقصَد بهذه العبارة كل تاجر يسجّل في منصة سلة لإنشاء متجره الالكتروني، سواءً كان شخص طبيعي أو معنوي، ويشمل هذا التعريف كافة أوجه المتجر طالما أنه يقوم بتجارته عن طريق منصة سلة، ويشمل ذلك الموقع الالكتروني للتاجر.⟫ ( المتجر ) يقصَد بهذه العبارة المتجر المستخدَم من قبل التاجر في منصة سلة الالكترونية. ( المستهلك ) يقصَد بهذه العبارة كل مستهلك يقوم بشراء المنتج أو الخدمة من التاجر، وذلك عن طريق متجر التاجر الالكتروني الذي أسسه عبر منصة سلة. ( الاتفاقية ) يقصَد بهذه العبارة قواعد وشروط وأحكام استخدام منصة سلة الإلكترونية، أي كافة أحكام وشروط هذه الاتفاقية، والتي تحكم وتنظّم العلاقة فيما بين أطراف هذه الاتفاقية. ( مزود الخدمة ) يقصَد بهذه العبارة الخدمات التي ت…

### Q6-SA-002

**Cited at:** section 1, line 7; section 2, line 39

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-002
- bears_on: 1
- identifier: أولاً: إدخال بيانات إنشاء الحساب
- statement: 3. سيُرسل إليك رمز تحقق على هاتفك؛ وذلك للتحقق من الرقم المدخل.
- scope: article filed under: إنشاء متجر جديد في السعودية
- cite_ids: Q6-SA-C003
- from: held
- note: The same sentence is in the UAE and Kuwait articles (lines 221 and 220).

**Citation Q6-SA-C003:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 222 (article ya5z2fsehfy3ok1wei82jgr0, إنشاء متجر جديد على سلة); أولاً: إدخال بيانات إنشاء الحساب | 2026-09-14 | kind: stated | quote check: found
- quote: 3. سيُرسل إليك رمز تحقق على هاتفك؛ وذلك للتحقق من الرقم المدخل.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …الإيمان والدعم لكل تاجر طموح. في هذا المقال، نأخذك خطوة بخطوة في رحلة إنشاء متجرك الجديد على سلة، من أول تسجيل دخول وحتى إطلاق متجرك بثقة✨. خطوات تسجيل حساب في سلة أولاً: إدخال بيانات إنشاء الحساب 1. من صفحة التسجيل حدد اللغة التي ستُكمل بها إعداد حسابك. ثم أدخل البيانات المطلوبة, ومنها: اسم التاجر - البريد الإلكتروني - رقم الجوال - كلمة المرور. 2. بعد إدخال كافة البيانات، اضغط على (تسجيل) وذلك إذا كنت موافقًا على : سياسة الاستخدام على منصة سلة. ⟪3. سيُرسل إليك رمز تحقق على هاتفك؛ وذلك للتحقق من الرقم المدخل.⟫ 3. بعد إدخال كود التحقق المرسل إلى هاتفك، ستوجَّه إلى صفحة الدخول السريع، حيث يمكنك تفعيلها بالبصمة أو Face ID، أو تأجيلها والمتابعة. ثانياً: نظرة عامة عن متجرك 📱بعد التحقق من رقم الهاتف، ستُنقل إلى رحلة البداية لإنشاء حساب جديد والتعرف على تجارتك بنظرة عامة. 🌍دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها. 🎯الكيان القانوني حدد كيان متجرك, اختيار الكيان الصحيح يساعدك في الامتثال للأنظمة وإصدار الترا…

### Q6-SA-011

**Cited at:** section 1, line 8; section 2, line 40

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-011
- bears_on: 1
- identifier: المادة الثانية – أهلية التاجر القانونية
- statement: يقر التاجر بأنه ذا أهلية قانونية معتبرة شرعاً وقانوناً، وأن عمره لا يقل عن ثمانية عشرة عاماً، كما هو معتبر في القوانين والأنظمة المرعية بالمملكة العربية السعودية ، وأنه ذا دراية كافية لإنشاء وتأسيس وإدارة متجره الالكتروني عبر منصة سلة.
- cite_ids: Q6-SA-C017
- from: held

**Citation Q6-SA-C017:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 26 (المادة الثانية – أهلية التاجر القانونية) | 2026-10-06 | kind: official page | quote check: found
- quote: يقر التاجر بأنه ذا أهلية قانونية معتبرة شرعاً وقانوناً، وأن عمره لا يقل عن ثمانية عشرة عاماً، كما هو معتبر في القوانين والأنظمة المرعية بالمملكة العربية السعودية ، وأنه ذا دراية كافية لإنشاء وتأسيس وإدارة متجره الالكتروني عبر منصة سلة.
- in context: …قصَد بهذه العبارة قواعد وشروط وأحكام استخدام منصة سلة الإلكترونية، أي كافة أحكام وشروط هذه الاتفاقية، والتي تحكم وتنظّم العلاقة فيما بين أطراف هذه الاتفاقية. ( مزود الخدمة ) يقصَد بهذه العبارة الخدمات التي تقوم منصة سلّة بتوفيرها للتُجّار عن طريق أطراف ثالثة ، ويُقصد ب توفير الخدمات أي مجرد توفير الربط بين التاجر ومزود الخدمة ، حيث أنه لا سلطان ولا علاقة لمنصة سلّة بالاتفاق المبرم بين التاجر ومزود الخدمة. المادة الثانية - أهلية التاجر القانونية: ⟪يقر التاجر بأنه ذا أهلية قانونية معتبرة شرعاً وقانوناً، وأن عمره لا يقل عن ثمانية عشرة عاماً، كما هو معتبر في القوانين والأنظمة المرعية بالمملكة العربية السعودية ، وأنه ذا دراية كافية لإنشاء وتأسيس وإدارة متجره الالكتروني عبر منصة سلة.⟫ استثناءً مما ورد في البند الأول ( 1 ) من المادة الثانية ( 2 ) ، يجوز للتاجر أن يمارس التجارة إذا كان يقل عن سن الرشد المعتبر في المملكة العربية السعودية (ثمانية عشرة عاماً) ، حيث أنه يلتزم بأن يقدّم ما يثبت موافقة وليه على تأسيسه للمتجر الالكتروني، كصك الولاية، وإفادة الموافقة الموقّعة من قبل وليه القانوني الشرعي في حال استلزم ذلك. يقر التاجر بأنه ذا أهلية سليمة وأنه غير مصاب بأي عارض من عوارض الأهلية. في حال قيام التاجر بالتسجيل كمؤسسة أو شركة،…

### Q6-SA-012

**Cited at:** section 1, line 8; section 7, line 114

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-012
- bears_on: 1
- identifier: المادة الثانية – أهلية التاجر القانونية
- statement: استثناءً مما ورد في البند الأول ( 1 ) من المادة الثانية ( 2 ) ، يجوز للتاجر أن يمارس التجارة إذا كان يقل عن سن الرشد المعتبر في المملكة العربية السعودية (ثمانية عشرة عاماً) ، حيث أنه يلتزم بأن يقدّم ما يثبت موافقة وليه على تأسيسه للمتجر الالكتروني، كصك الولاية، وإفادة الموافقة الموقّعة من قبل وليه القانوني الشرعي في حال استلزم ذلك.
- cite_ids: Q6-SA-C018
- from: held

**Citation Q6-SA-C018:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 27 (المادة الثانية – أهلية التاجر القانونية) | 2026-10-06 | kind: official page | quote check: found
- quote: يجوز للتاجر أن يمارس التجارة إذا كان يقل عن سن الرشد المعتبر في المملكة العربية السعودية (ثمانية عشرة عاماً) ، حيث أنه يلتزم بأن يقدّم ما يثبت موافقة وليه على تأسيسه للمتجر الالكتروني، كصك الولاية
- in context: …ربط بين التاجر ومزود الخدمة ، حيث أنه لا سلطان ولا علاقة لمنصة سلّة بالاتفاق المبرم بين التاجر ومزود الخدمة. المادة الثانية - أهلية التاجر القانونية: يقر التاجر بأنه ذا أهلية قانونية معتبرة شرعاً وقانوناً، وأن عمره لا يقل عن ثمانية عشرة عاماً، كما هو معتبر في القوانين والأنظمة المرعية بالمملكة العربية السعودية ، وأنه ذا دراية كافية لإنشاء وتأسيس وإدارة متجره الالكتروني عبر منصة سلة. استثناءً مما ورد في البند الأول ( 1 ) من المادة الثانية ( 2 ) ، ⟪يجوز للتاجر أن يمارس التجارة إذا كان يقل عن سن الرشد المعتبر في المملكة العربية السعودية (ثمانية عشرة عاماً) ، حيث أنه يلتزم بأن يقدّم ما يثبت موافقة وليه على تأسيسه للمتجر الالكتروني، كصك الولاية⟫، وإفادة الموافقة الموقّعة من قبل وليه القانوني الشرعي في حال استلزم ذلك. يقر التاجر بأنه ذا أهلية سليمة وأنه غير مصاب بأي عارض من عوارض الأهلية. في حال قيام التاجر بالتسجيل كمؤسسة أو شركة، أو أي شكل نظامي آخر، فإن هذه المؤسسة أو الشركة أو الشكل النظامي المسجّل عن طريقه يجب أن تتوافر فيه الأهلية القانونية والنظامية والشرعية اللازمة للقيام بأعمال التجارة عبر منصة سلة الالكترونية. يوافق التاجر بأنه في حال مخالفته لهذه المادة " أهلية التاجر القانوني…

### Q6-SA-026

**Cited at:** section 1, line 9; section 2, line 41; section 3, line 63

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-026
- bears_on: 1
- identifier: 3. حدّد نوع الكيان
- statement: -حدد إن كنت فرداَ, مؤسسة, شركة, أو جمعية خيرية. - فرد : وثيقة العمل الحر تابعه لمالك المتجر (للمواطنين السعوديين فقط). - مؤسسة - شركة : سجل تجاري ساري الصلاحية للشركة أو المؤسسة تابع لمالك المتجر (للمواطنين والمقيمين) . - جمعية خيرية: شهادة تسجيل الجمعية الخيرية.
- scope: توثيق متجرك الجديد في السعودية
- cite_ids: Q6-SA-C036;Q6-SA-C037
- from: held
- note: The full list whose first item is copied as Q6-SA-K0084.

**Citation Q6-SA-C036:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 926 (article ig4b4l5hc542j4bcd2tp82bz, توثيق متجرك الجديد في السعودية); 3. حدّد نوع الكيان | 2026-08-31 | kind: stated | quote check: found
- quote: -حدد إن كنت فرداَ, مؤسسة, شركة, أو جمعية خيرية.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …في منصة أبشر. -تاريخ الميلاد لمالك المتجر (يتم إدخال التاريخ بالهجري للمواطن، وبالميلادي للمقيم). -صورة الهوية الرقيمة لمالك المتجر. سترسل رسالة نصية من أبشر إلى رقم مالك المتجر الذي تم تسجيله في الخطوة السابقة. تم التحقق من مالك المتجر بنجاح. 2. ادخل بيانات مدير المتجر إن كان مالك المتجر هو المدير فعّل خيار (مالك المتجر هو المدير). 3. حدّد نوع الكيان وبناء على نوع الكيان ادخل البيانات المطلوبة سواء بيانات العمل الحر أو السجل التجاري أو غير ذلك. ⟪-حدد إن كنت فرداَ, مؤسسة, شركة, أو جمعية خيرية.⟫ - فرد : وثيقة العمل الحر تابعه لمالك المتجر (للمواطنين السعوديين فقط). - مؤسسة - شركة : سجل تجاري ساري الصلاحية للشركة أو المؤسسة تابع لمالك المتجر (للمواطنين والمقيمين) . - جمعية خيرية: شهادة تسجيل الجمعية الخيرية. ملاحظة : يمكن للأسر المنتجة استخدام شهادة الأسر المنتجة لاستخراج وثيقة العمل الحر عبر موقع العمل الحر، مما يسهّل ويسرّع الإجراءات، حيث يمكن إصدار الوثيقة خلال مدة تقارب 24 ساعة. سنكمل الشرح بإدخال بيانات وثيقة العمل الحر، على سبيل ال…

**Citation Q6-SA-C037:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 926 (article ig4b4l5hc542j4bcd2tp82bz, توثيق متجرك الجديد في السعودية); 3. حدّد نوع الكيان | 2026-08-31 | kind: stated | quote check: found
- quote: - فرد : وثيقة العمل الحر تابعه لمالك المتجر (للمواطنين السعوديين فقط). - مؤسسة - شركة : سجل تجاري ساري الصلاحية للشركة أو المؤسسة تابع لمالك المتجر (للمواطنين والمقيمين) . - جمعية خيرية: شهادة تسجيل الجمعية الخيرية.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …دخال التاريخ بالهجري للمواطن، وبالميلادي للمقيم). -صورة الهوية الرقيمة لمالك المتجر. سترسل رسالة نصية من أبشر إلى رقم مالك المتجر الذي تم تسجيله في الخطوة السابقة. تم التحقق من مالك المتجر بنجاح. 2. ادخل بيانات مدير المتجر إن كان مالك المتجر هو المدير فعّل خيار (مالك المتجر هو المدير). 3. حدّد نوع الكيان وبناء على نوع الكيان ادخل البيانات المطلوبة سواء بيانات العمل الحر أو السجل التجاري أو غير ذلك. -حدد إن كنت فرداَ, مؤسسة, شركة, أو جمعية خيرية. ⟪- فرد : وثيقة العمل الحر تابعه لمالك المتجر (للمواطنين السعوديين فقط). - مؤسسة - شركة : سجل تجاري ساري الصلاحية للشركة أو المؤسسة تابع لمالك المتجر (للمواطنين والمقيمين) . - جمعية خيرية: شهادة تسجيل الجمعية الخيرية.⟫ ملاحظة : يمكن للأسر المنتجة استخدام شهادة الأسر المنتجة لاستخراج وثيقة العمل الحر عبر موقع العمل الحر، مما يسهّل ويسرّع الإجراءات، حيث يمكن إصدار الوثيقة خلال مدة تقارب 24 ساعة. سنكمل الشرح بإدخال بيانات وثيقة العمل الحر، على سبيل المثال: -ادخل بيانات العمل الحر, وتحقق بأن تكون سارية المفعول وتطابق الشروط المطلوبة لنجاح توثيق متجرك. 4. ادخل بيانات الحساب البنكي 📝 ملاحظة: للفرد: يجب أن يكون اسم صاحب الحساب البنكي مطابقًا للاسم الوارد في شهادة الآ…

### Q6-SA-059

**Cited at:** section 1, line 10; section 2, line 42; section 3, line 68; section 5, line 88

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-059
- bears_on: 1;2
- identifier: GET /admin/v2/onboarding/persona-country: data
- statement: "slug": "store-country", "question": "Where is your business based?", "type": "main", "description": "Select the country where your business is legally registered or where you issue official documents. We'll use this to apply the correct regulations to your store.", "is_mandatory": true, "options": [{"slug": "SA", "label": "🇸🇦 Saudi Arabia", "selected": false, "dependent_questions": []}, {"slug": "AE", "label": "🇦🇪 United Arab Emirates", "selected": false, "dependent_questions": []}, {"slug": "KW", "label": "🇰🇼 Kuwait", "selected": false, "dependent_questions": []}, {"slug": "QA", "label": "🇶🇦 Qatar", "selected": false, "dependent_questions": []}, {"slug": "OM", "label": "🇴🇲 Oman", "selected": false, "dependent_questions": []}, {"slug": "BH", "label": "🇧🇭 Bahrain", "selected": false, "dependent_questions": []}, {"slug": "other", "label": "Other country", "selected": false, "dependent_questions": []}]
- scope: store store-sherawya, observed 2026-10-08
- cite_ids: Q6-SA-C077;Q6-SA-C078
- from: held
- note: Saved response of the onboarding question page (/persona/qna). The options list is recorded in full. Bears on Q6-SA-G0162: it shows the country step's options, not what each choice connects to.

**Citation Q6-SA-C077:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T133523Z-sweep-demo-store-en/responses/5134.json` | GET https://api.salla.dev/admin/v2/onboarding/persona-country, step 133 | 2026-10-08 | kind: observed | quote check: found
- quote: "question": "Where is your business based?", "type": "main", "description": "Select the country where your business is legally registered or where you issue official documents. We'll use this to apply the correct regulations to your store."
- in context: store-country Where is your business based? main Select the country where your business is legally registered or where you issue official documents. We'll use this to apply the correct regulations to your store. SA 🇸🇦 Saudi Arabia AE 🇦🇪 United Arab Emirates KW 🇰🇼 Kuwait QA 🇶🇦 Qatar OM 🇴🇲 Oman BH 🇧🇭 Bahrain other Other country {"status": 200, "success": true, "data": {"slug": "store-country", ⟪"question": "Where is your business based?", "type": "main", "description": "Select the country where your business is legally registered or where you issue official documents. We'll use this to apply the correct regulations to your store."⟫, "is_mandatory": true, "options": [{"slug": "SA", "label": "🇸🇦 Saudi Arabia", "selected": false, "dependent_questions": []}, {"slug": "AE", "label": "🇦🇪 United Arab Emirates", "selected": false, "dependent_questions": []}, {"slug": "KW", "label": "🇰🇼 Kuwait", "selected": false, "dependent_questions": []}, {"slug": "QA", "label": "🇶🇦 Qatar", "selected": false, "dependent_questions": []}, {"slug": "OM", "label": "🇴🇲 Oman", "selected": false, "depe…

**Citation Q6-SA-C078:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T133523Z-sweep-demo-store-en/responses/5134.json` | GET https://api.salla.dev/admin/v2/onboarding/persona-country, step 133 | 2026-10-08 | kind: observed | quote check: found
- quote: {"slug": "other", "label": "Other country", "selected": false, "dependent_questions": []}
- title, opening and note boxes: as for this source's citation above
- in context: …_questions": []}, {"slug": "AE", "label": "🇦🇪 United Arab Emirates", "selected": false, "dependent_questions": []}, {"slug": "KW", "label": "🇰🇼 Kuwait", "selected": false, "dependent_questions": []}, {"slug": "QA", "label": "🇶🇦 Qatar", "selected": false, "dependent_questions": []}, {"slug": "OM", "label": "🇴🇲 Oman", "selected": false, "dependent_questions": []}, {"slug": "BH", "label": "🇧🇭 Bahrain", "selected": false, "dependent_questions": []}, ⟪{"slug": "other", "label": "Other country", "selected": false, "dependent_questions": []}⟫]}} {"status": 200, "success": true, "data": {"slug": "store-country", "question": "Where is your business based?", "type": "main", "description": "Select the country where your business is legally registered or where you issue official documents. We'll use this to apply the correct regulations to your store.", "is_mandatory": true, "options": [{"slug": "SA", "label": "🇸🇦 Saudi Arabia", "selected": false, "dependent_questions": []}, {"slug": "AE"…

### Q6-SA-008

**Cited at:** section 1, line 11; section 2, line 44

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-008
- bears_on: 1
- identifier: countryOther.alert
- statement: اختيارك للدولة يحدِّد المتطلبات القانونية اللازمة لمتجرك.
- scope: persona, countryOther
- cite_ids: Q6-SA-C011;Q6-SA-C012
- from: held

**Citation Q6-SA-C011:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/persona.json` | key countryOther.alert | 2026-10-08 | kind: observed | quote check: found
- quote: اختيارك للدولة يحدِّد المتطلبات القانونية اللازمة لمتجرك.
- in context: …تك: استقبل وأدِر وتتبَّع التبرعات بسهولة أتِح خيار إهداء التبرع للأحباب والأقارب صمِّم متجر يناسب نشاط جمعيتك مع ثيم عطاء مكِّن التبرع السريع بدون إنشاء حساب مزايا أخرى ستُفعّل باقة سلة برو فور اكتمال توثيق متجرك كجمعية خيرية من داخل لوحة التحكم لاحقًا. سلة برو مجانًا مدى الحياة اكتشف باقي المزايا أنشئ متجر لجمعيتك ندعم مسيرتك في العطاء رجوع إغلاق تأكيد النقل استكمال النقل لاحقًا دقيقة ابدأ نقل متجري اختياري السؤال السابق تخطي حاول مجددًا حيَّاك ⟪اختيارك للدولة يحدِّد المتطلبات القانونية اللازمة لمتجرك.⟫ العودة لتسجيل الدخول منصة سلة متاحة حاليًا في السعودية والإمارات فقط، وسنبلغك فور التوسُّع إلى منطقتك لتنطلق بتجارتك معنا. نسعد باهتمامك بالتسجيل في سلة! الوقت المتوقع: {{minutes}} دقيقة الوقت المتوقع الوقت المتوقع: 1 دقيقة الوقت المتوقع: 1 دقيقة نحب نعرف أكثر عنك وعن تجارتك عبر أسئلة قصيرة تهدف لتخصيص تجربتك حدث خطأ أثناء إنشاء متجرك. فضلًا أعد المحاولة. تعذَّر إنشاء متجرك نمهِّد الطريق لانطلاقتك... نرتِّب رفوف متجرك الجديد.. مستعد تبدأ رحلتك ف…

**Citation Q6-SA-C012:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/persona.json` | key countryOther.alert | 2026-10-08 | kind: observed | quote check: found
- quote: Your country selection sets the legal requirements for your store.
- in context: …ored for your charity with Atta'a theme Enable quick donations without the need for an account other features Your Salla Pro plan will be activated once your store is verified as a charity from the dashboard. Salla Pro, free for life Explore other features Create your charity store Supporting your journey of giving Go back Close Confirm migration Continue migration Later minute Migrate your store Optional Go back Skip Try again Nice to meet you, ⟪Your country selection sets the legal requirements for your store.⟫ Back to log in We're currently available in Saudi Arabia and the UAE. We'll notify you when Salla becomes available in your country. Thanks for your interest in joining Salla! Estimated time: {{minutes}} minute Estimated time Estimated time: 1 minute Estimated time: 1 minute Let's learn more about your business, so we can set you up for success! Something went wrong while creating your store. Please try again. We couldn't create your store Prepa…

### Q6-SA-023

**Cited at:** section 1, line 15; section 2, line 47

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-023
- bears_on: 1;2
- identifier: المقدّمة
- statement: منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513 ترحّب بكم
- scope: https://salla.com/ar-ae/terms
- cite_ids: Q6-SA-C033
- from: held
- note: Closes Q6-SA-G0161 for the page its route names: the usage agreement served at https://salla.com/ar-ae/terms opens with this introduction. No Kuwait version was read (Q6-SA-G0213 stays open).

**Citation Q6-SA-C033:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` | record at offset 3700206 (https://salla.com/ar-ae/terms); المقدّمة | 2026-10-06 | kind: stated | quote check: found
- quote: منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513 ترحّب بكم
- title: شروط وأحكام استخدام منصة سلة
- in context: شروط وأحكام استخدام منصة سلة ')"> الحلول الموارد القطاعات سلة سبيشل الأسعار En تسجيل دخول أنشئ متجرك مجانًا أنشئ متجرك مجانًا ')"> اتفاقية الاستخدام A A A المقدّمة: ⟪منصة سلّة المملوكة لشركة تطبيق سلّة لتقنية المعلومات المسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري رقم: 7011845513 ترحّب بكم⟫ ، وتبلغكم بأنكم سوف تجدون أدناه الشروط والأحكام المُنظّمة لاستخدامكم لمنصة سلّة وكافة الآثار القانونية التي تنتج عن استخدامكم لخدمات منصة سلّة في الشبكة العنكبوتية ، حيث أن استخدام أي شخصٍ كان لمنصة سلّة سواءً كان مستهلكاً أو تاجراً أو غير ذلك فإن هذا يُعد موافقة وقبول منه وهو بكامل أهليته المعتبرة شرعاً ونظاماً وقانوناً لكافة مواد وبنود وأحكام هذه الاتفاقية وهو تأكيد لالتزامكم بأنظمتها ولما ذُكر فيها، ونشير إليكم بأن منصة سلّة قد تكون عبارة عن …

### Q6-SA-019

**Cited at:** section 1, line 19; section 7, line 114

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-019
- bears_on: 1;2
- identifier: المادة الرابعة – ضوابط إنشاء المتجر الالكتروني
- statement: .ينبغي على كافة المتاجر الراغبة بالتسجيل بمنصة سلة ومزاولة نشاط التجارة الإلكترونية بالمنصة أن يكون لديها سجل تجاري قائم أو وثيقة عمل حر، بالإضافة إلى استيفاء الاشتراطات النظامية الأخرى وإصدار التراخيص اللازمة المتعلقة بممارسة التجار لأنشطتهم التجارية في متاجرهم الإلكترونية كحساب أبشر وحساب بنكي في أحد البنوك السعودية ورقم جوال سعودي.
- cite_ids: Q6-SA-C026;Q6-SA-C027
- from: held

**Citation Q6-SA-C026:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 52 (المادة الرابعة – ضوابط إنشاء المتجر الالكتروني) | 2026-10-06 | kind: official page | quote check: found
- quote: ينبغي على كافة المتاجر الراغبة بالتسجيل بمنصة سلة ومزاولة نشاط التجارة الإلكترونية بالمنصة أن يكون لديها سجل تجاري قائم أو وثيقة عمل حر
- in context: … يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته. .ينبغي على كافة المتاجر والتجّار الذين يحملون سجلاً تجارياً لمحلهم، بتقييد المحل الالكتروني بالسجل التجاري للمنشأة وفقاً للنظام. .يقر التاجر بأنه قبل تسجيله في منصة سلة الالكترونية قد تحقق من توافر جميع الإجراءات والاشتراطات المطلوبة من قبل الجهات الرسمية في المملكة العربية السعودية وقد استوفى جميع هذه الإجراءات والاشتراطات لممارسة نشاطه في المتجر. .⟪ينبغي على كافة المتاجر الراغبة بالتسجيل بمنصة سلة ومزاولة نشاط التجارة الإلكترونية بالمنصة أن يكون لديها سجل تجاري قائم أو وثيقة عمل حر⟫، بالإضافة إلى استيفاء الاشتراطات النظامية الأخرى وإصدار التراخيص اللازمة المتعلقة بممارسة التجار لأنشطتهم التجارية في متاجرهم الإلكترونية كحساب أبشر وحساب بنكي في أحد البنوك السعودية ورقم جوال سعودي. .في حال كان التاجر المتقدّم لطلب الانضمام وتأسيس المتجر عبارة عن تاجر فرد "شخص طبيعي"، فيلتزم كذلك بالتحقق من الاشتراطات المطلوبة لدى الجهات الرسمية وتوفيرها بحسب طبيعة نشاط الفرد التاجر، حيث إن التاجر الفرد يقر بأنه ملتزم بهذه الاشتراطات وملتزم بتو…

**Citation Q6-SA-C027:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 52 (المادة الرابعة – ضوابط إنشاء المتجر الالكتروني) | 2026-10-06 | kind: official page | quote check: found
- quote: وإصدار التراخيص اللازمة المتعلقة بممارسة التجار لأنشطتهم التجارية في متاجرهم الإلكترونية كحساب أبشر وحساب بنكي في أحد البنوك السعودية ورقم جوال سعودي.
- title, opening and note boxes: as for this source's citation above
- in context: …روني بالسجل التجاري للمنشأة وفقاً للنظام. .يقر التاجر بأنه قبل تسجيله في منصة سلة الالكترونية قد تحقق من توافر جميع الإجراءات والاشتراطات المطلوبة من قبل الجهات الرسمية في المملكة العربية السعودية وقد استوفى جميع هذه الإجراءات والاشتراطات لممارسة نشاطه في المتجر. .ينبغي على كافة المتاجر الراغبة بالتسجيل بمنصة سلة ومزاولة نشاط التجارة الإلكترونية بالمنصة أن يكون لديها سجل تجاري قائم أو وثيقة عمل حر، بالإضافة إلى استيفاء الاشتراطات النظامية الأخرى ⟪وإصدار التراخيص اللازمة المتعلقة بممارسة التجار لأنشطتهم التجارية في متاجرهم الإلكترونية كحساب أبشر وحساب بنكي في أحد البنوك السعودية ورقم جوال سعودي.⟫ .في حال كان التاجر المتقدّم لطلب الانضمام وتأسيس المتجر عبارة عن تاجر فرد "شخص طبيعي"، فيلتزم كذلك بالتحقق من الاشتراطات المطلوبة لدى الجهات الرسمية وتوفيرها بحسب طبيعة نشاط الفرد التاجر، حيث إن التاجر الفرد يقر بأنه ملتزم بهذه الاشتراطات وملتزم بتوفيرها وتجهيزها، كما يلتزم التاجر الفرد بتوفير بيانات هويته الوطنية بالإضافة إلى بيانات وثيقة العمل الحر وغير ذلك من المعلومات اللازمة والوثائق التي تطلبها منصة سلة. في حالة كان التاجر المتقدم لطلب الا…

### Q6-SA-035

**Cited at:** section 1, line 19; section 5, line 94; section 7, line 114

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-035
- bears_on: 1;2
- identifier: ❓ في حال كان التاجر أجنبيّاً كيف يتم التحقق من صحة بيانات متجره؟
- statement: يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري. 📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات.
- scope: أسئلة شائعة حول توثيق المتجر (filed under توثيق المتجر في السعودية)
- cite_ids: Q6-SA-C048;Q6-SA-C049
- from: held

**Citation Q6-SA-C048:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر); ❓ في حال كان التاجر أجنبيّاً | 2026-08-29 | kind: stated | quote check: found
- quote: يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري.
- in context: …نات الجمعية كيف سيتم التحقق من صحة البيانات لمالك المتجر في هذه الحالة؟ يحق للمؤسسة الوقفية تعيين ممثل نظامي كمستخدم للمتجر. ❓ عند التحقق من صحة البيانات لمتجر جمعية، من يعتبر مالك المتجر؟ ولماذا لا يتم تغيير المسمى من مالك المتجر إلى الصفة المطلوبة (رئيس مجلس، مدير تنفيذي، الخ) يعتبر اسم مالك المتجر من البيانات التي تحفظ ضمن بيانات معلومات المتجر لدى منصة سلة لضمان موثوقية المتجر. ❓ في حال كان التاجر أجنبيّاً كيف يتم التحقق من صحة بيانات متجره؟ ⟪يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري.⟫ 📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات. ❓ كيف يظهر للتاجر أن المتجر قد تُحُقِقَ من صحة بياناته؟ يتم إظهار علامة مكتمل أمام توثيق المتجر في صفحة اعدادات الدفع. ❓ عند التحقق من صحة بيانات مؤسسة مبيعاتها أقل من 375 ألف ريال، كيف يتم التحقق من صحة الرقم الضريبي؟ يتم الرجوع إلى هيئة الزكاة والدخل بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ قرار التحقق من صحة البي…

**Citation Q6-SA-C049:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر); ❓ في حال كان التاجر أجنبيّاً | 2026-08-29 | kind: stated | quote check: found
- quote: 📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات.
- title, opening and note boxes: as for this source's citation above
- in context: …خدم للمتجر. ❓ عند التحقق من صحة البيانات لمتجر جمعية، من يعتبر مالك المتجر؟ ولماذا لا يتم تغيير المسمى من مالك المتجر إلى الصفة المطلوبة (رئيس مجلس، مدير تنفيذي، الخ) يعتبر اسم مالك المتجر من البيانات التي تحفظ ضمن بيانات معلومات المتجر لدى منصة سلة لضمان موثوقية المتجر. ❓ في حال كان التاجر أجنبيّاً كيف يتم التحقق من صحة بيانات متجره؟ يمكن للتاجر الأجنبي إنشاء متجره على سلة سواء بصفته شركة أو مؤسسة، ولكن لإتمام عملية التوثيق يجب إصدار سجل تجاري. ⟪📝 ملاحظة: يشترط أن يكون السجل التجاري المستخدم للتوثيق سجلاً تجارياً سعودياً حتى يتم اعتماد المتجر وتفعيل كامل الخدمات.⟫ ❓ كيف يظهر للتاجر أن المتجر قد تُحُقِقَ من صحة بياناته؟ يتم إظهار علامة مكتمل أمام توثيق المتجر في صفحة اعدادات الدفع. ❓ عند التحقق من صحة بيانات مؤسسة مبيعاتها أقل من 375 ألف ريال، كيف يتم التحقق من صحة الرقم الضريبي؟ يتم الرجوع إلى هيئة الزكاة والدخل بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ قرار التحقق من صحة البيانات حكومي أم من شركة سلة؟ هي مبادرة من شركة سلة لتنظيم سوق التجارة الإلكترونية في المملكة العربية السعودية تهدف إلى رفع…

### Q6-SA-037

**Cited at:** section 1, line 20; section 2, line 49; section 5, line 92; section 7, line 118

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-037
- bears_on: 1
- identifier: ❓ ما هي النتائج المحتملة لعدم التحقق من صحة بيانات لمتجري؟
- statement: سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر.
- scope: أسئلة شائعة حول توثيق المتجر
- cite_ids: Q6-SA-C051;Q6-SA-C052
- from: held

**Citation Q6-SA-C051:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر); ❓ ما هي النتائج المحتملة لعدم التحقق | 2026-08-29 | kind: stated | quote check: found
- quote: سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر.
- in context: …يكون باسم مالك المتجر وصاحب وثيقة العمل الحر (للكيان الفردي). 3- للمؤسسات: يجب أن تتطابق بيانات الحساب مع السجل التجاري والهوية الوطنية. ❓ماذا يحدث إذا كان البنك لا يدعم التحقق التلقائي؟ في هذه الحالة، يمكنك إدخال بيانات الحساب البنكي يدوياً، وسيتم التحقق منها من قبل فريق الدعم في سلة. ❓ هل يظهر اسم صاحب الحساب بعد التحقق؟ نعم ، في حال نجاح التحقق، يظهر الاسم الثلاثي لصاحب الحساب مباشرة. ❓ ما هي النتائج المحتملة لعدم التحقق من صحة بيانات لمتجري؟ ⟪سوف يتم تعليق عمليات الدفع والسداد بعد انتهاء المهلة إلى حين إتمام إجراءات توثيق المتجر.⟫ ❓ هل يطلع أحد على معلومات متجري، أم التحقق من صحة البيانات فقط لتوثيق المتجر؟ التحقق من أجل توثيق صحة بيانات المتجر ولا يمكن للعملاء الاطلاع على بيانات متجرك ❓ هل ملف ال Pdf مدعوم في التحقق من صحة البيانات ؟ يمكن رفعه ولكنه يستغرق وقتاً أطول، يفضّل رفع صورة. ❓ كم يأخذ توثيق المتجر في سلة؟ مدة توثيق المتجر من 24 إلى 48 ساعة، إذا تأخر عن ذلك تواصل مع الدعم الفني لسلة من لوحة تحكم متجرك ❓ ماهي قنوات اشعار التاجر بحالات التوثيق؟ بجانب اشعارات لوحة ا…

**Citation Q6-SA-C052:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر); ❓ في حال لم أوثق متجري | 2026-08-29 | kind: stated | quote check: found
- quote: يتم تعليق عمليات الدفع والسداد إلى أن يتم إتمام خطوات توثيق المتجر.
- in context: …تاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟ التحقق متطلب أساسي للبدء في عملية البيع ❓ هل يوجد مزامنة بين تفعيل الدفع والتحقق من صحة البيانات، وأيضاً نوع الكيان؟ نعم يوجد، ويجب أن تكون البيانات المدخلة متوافقة وصحيحة ويتم تدقيق كل الطلبات وفي حال إدخال بيانات خاطئة يتم رفض الطلب. ❓ هل يمكن رفع صورة من الهوية الرقمية ؟ نعم، تُقبل صورة الهوية الرقمية. ❓ في حال لم أوثق متجري هل ستُلغى طرق الدفع من متجري، أم أن الطلبات تستمر ولكن تحجز المبالغ؟ ⟪يتم تعليق عمليات الدفع والسداد إلى أن يتم إتمام خطوات توثيق المتجر.⟫ في حال احتجت مساعدة لتوثيق متجرك بإمكانك الاستفادة من ميزة خدمات التاجر حيث يتم تقديم خدمة توثيق المتجر أو إصدار وثيقة عمل حر مما يضمن لك إنجاز أعمالك التجارية باحترافية. iparbtoxqor7rjnuhg9ppnrh https://help.salla.sa/article/%D8%A3%D8%B3%D8%A6%D9%84%D8%A9-%D8%B4%D8%A7%D8%A6%D8%B9%D8%A9-%D8%AD%D9%88%D9%84-%D8%AA%D9%88%D8%AB%D9%8A%D9%82-%D8%A7%D9%84%D9%85%D8%AA%D8%AC%D8%B1/iparbtoxqor7rjnuhg9ppnrh لمزيد من التفاصيل حول إدارة سجل طلب توثيق المتجر …

### Q6-SA-036

**Cited at:** section 1, line 20; section 2, line 48

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-036
- bears_on: 1
- identifier: ❓ ما الإجراء المتبع في حق متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟
- statement: ❓ ما الإجراء المتبع في حق متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟ التحقق متطلب أساسي للبدء في عملية البيع
- scope: أسئلة شائعة حول توثيق المتجر
- cite_ids: Q6-SA-C050
- from: held

**Citation Q6-SA-C050:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر); ❓ ما الإجراء المتبع في حق متاجر على باقة بيسك | 2026-08-29 | kind: stated | quote check: found
- quote: ❓ ما الإجراء المتبع في حق متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟ التحقق متطلب أساسي للبدء في عملية البيع
- in context: …ف ريال، كيف يتم التحقق من صحة الرقم الضريبي؟ يتم الرجوع إلى هيئة الزكاة والدخل بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ قرار التحقق من صحة البيانات حكومي أم من شركة سلة؟ هي مبادرة من شركة سلة لتنظيم سوق التجارة الإلكترونية في المملكة العربية السعودية تهدف إلى رفع ثقة المستهلك بالمتاجر المسجّلة عبر منصة سلة وإلى توفير بيئة آمنة لممارسة التجارة الإلكترونية، ولا يغني ذلك عن التحقق من صحة بيانات أي من التجار لمتاجرهم لدى الجهات الحكومية. ⟪❓ ما الإجراء المتبع في حق متاجر على باقة بيسك ولم يتم التحقق من صحة بياناتها؟ التحقق متطلب أساسي للبدء في عملية البيع⟫ ❓ هل يوجد مزامنة بين تفعيل الدفع والتحقق من صحة البيانات، وأيضاً نوع الكيان؟ نعم يوجد، ويجب أن تكون البيانات المدخلة متوافقة وصحيحة ويتم تدقيق كل الطلبات وفي حال إدخال بيانات خاطئة يتم رفض الطلب. ❓ هل يمكن رفع صورة من الهوية الرقمية ؟ نعم، تُقبل صورة الهوية الرقمية. ❓ في حال لم أوثق متجري هل ستُلغى طرق الدفع من متجري، أم أن الطلبات تستمر ولكن تحجز المبالغ؟ يتم تعليق عمليات الدفع والسداد إلى أن يتم إتمام خطوات توثيق المتجر. في حال احتجت مساعدة لت…

### Q6-SA-061

**Cited at:** section 1, line 20; section 2, line 48

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-061
- bears_on: 1
- identifier: GET /admin/v2/gateways/payment: data.verification; data.merchant_type
- statement: "verification": {"status": "uncompleted", "is_owner": true, "blocks_payment_activation": true, "verify_url": "https://s.salla.sa/entity/verification/verify", "summary": {"store_documented": false, "kyc_complete": false, "has_approved_epayment_request": false}, "rejection": null}, "merchant_type": "KSA"
- scope: store store-sherawya, observed 2026-10-08; merchant_type KSA
- cite_ids: Q6-SA-C080
- from: held
- note: Saved response of the payment methods page (/payments).

**Citation Q6-SA-C080:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T133523Z-sweep-demo-store-en/responses/2518.json` | GET https://api.salla.dev/admin/v2/gateways/payment, step 71 | 2026-10-08 | kind: observed | quote check: found
- quote: "verification": {"status": "uncompleted", "is_owner": true, "blocks_payment_activation": true
- in context: …p/assets/images/mokafaa-alrajhi.png uncompleted cod other_payment_method Cash on Delivery https://cdn.assets.salla.network/prod/admin/cp/assets/images/cod.png uncompleted 1377181007 1473353380 National Commercial Bank https://cdn.assets.salla.network/banks-logo/NCBK.png Demo Account 000000608010167519 SA2380000382608010130308 iban active {"status": 200, "success": true, "data": {"master": {"epayment_enabled": false}, "is_first_time_setup": true, ⟪"verification": {"status": "uncompleted", "is_owner": true, "blocks_payment_activation": true⟫, "verify_url": "https://s.salla.sa/entity/verification/verify", "summary": {"store_documented": false, "kyc_complete": false, "has_approved_epayment_request": false}, "rejection": null}, "merchant_type": "KSA", "quick_methods": [{"slug": "mada", "is_enabled": false, "is_available": true, "is_effective": false, "blocked_by": "master_disabled", "unavailable_reason": null, "has_advance_settings": false, "label": "Mada", "logo": "https://cdn.assets.…

### Q6-SA-K0087

**Cited at:** section 1, line 21; section 2, line 50; section 5, line 90; section 7, line 116

**Record** (`studies/proposals/records/Q6/salla/copied.tsv`):
- concern_id: SA-C-006
- placement: decides
- structure: https://help.salla.sa/article/توثيق-متجرك-الجديد-في-السعودية/ig4b4l5hc542j4bcd2tp82bz
- identifier: ثالثاً: مرحلة ما بعد إرسال طلب التوثيق
- statement: يقوم فريق سلة بمراجعة طلب التوثيق.
- scope: السعودية (article: توثيق متجرك الجديد في السعودية)
- cite_ids: SA-S-0134

**Citation SA-S-0134:** `https://help.salla.sa/article/توثيق-متجرك-الجديد-في-السعودية/ig4b4l5hc542j4bcd2tp82bz` | ثالثاً: مرحلة ما بعد إرسال طلب التوثيق (line 780 of the rendered text) | 2026-08-31 | kind: stated | quote check: found
- quote: يقوم فريق سلة بمراجعة طلب التوثيق.
- title: توثيق متجرك الجديد في السعودية | مركز المساعدة - سلة
- the page opens: توثيق متجرك الجديد في السعودية مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حلول…
- in context: … اسم صاحب الحساب البنكي مطابقًا للاسم الوارد في شهادة الآيبان (وليس الاسم الموجود على البطاقة البنكية). كما يجب أن يتطابق صاحب الحساب مع هوية مالك المتجر أو وثيقة العمل الحر الخاصة به. للشركة أو المؤسسة: يجب إضافة حساب بنكي تجاري بإسم المؤسسة أو الشركة، وأن يكون مرتبطاً بالسجل التجاري. راجع وتأكد من المعلومات التي سجلتها, ثم اضغط (إرسال الطلب). سيتم مراجعة طلبك من فريق سلة.. 🎉 تهانينا، تم توثيق متجرك بنجاح. ثالثاً: مرحلة ما بعد إرسال طلب التوثيق ⟪يقوم فريق سلة بمراجعة طلب التوثيق.⟫ في حال اكتمال البيانات وصحتها، سيتم اعتماد الطلب. ستصلك رسالة تفيد بأنه تم توثيق متجرك بنجاح 🎉 نصائح لضمان قبول طلب التوثيق من أول مرة استخدم مستندات واضحة وسارية المفعول. تأكد من تطابق الأسماء في الهوية والوثائق والحساب البنكي. أدخل البيانات دون أخطاء إملائية أو رقمية. راجع جميع الخطوات قبل إرسال الطلب. قد يؤدي إدخال وثائق غير مرتبطة بهوية مالك المتجر إلى رفض طلب التوثيق بشكل نهائي. أسئلة شائعة ❓ كيف يمكنني توثيق متجري على منصة سلة؟ يمكنك توثيق…

### Q6-SA-056

**Cited at:** section 1, line 27; section 2, line 53; section 3, line 60; section 3, line 68; section 7, line 115

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-056
- bears_on: 2
- identifier: تفعيل تابي على متجرك في سلة الإمارات
- statement: مهم : إذا كان متجرك خارج السعودية، تواصل مع تابي مباشرة لاستكمال إعداد حساب التاجر وتفعيله قبل ربط الحساب بسلة.
- scope: تابي; سلة الإمارات
- cite_ids: Q6-SA-C072;Q6-SA-C073
- from: held

**Citation Q6-SA-C072:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة); خطوات التفعيل | 2026-09-16 | kind: stated | quote check: found
- quote: مهم : إذا كان متجرك خارج السعودية، تواصل مع تابي مباشرة لاستكمال إعداد حساب التاجر وتفعيله قبل ربط الحساب بسلة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …سابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ثم اختر «تابي». أدخل Merchant Public Key وMerchant Private Key المرتبطين بحسابك لدى تابي. راجع إعدادات تابي المتاحة لمتجرك. وافق على شروط استخدام سلة، ثم اضغط «حفظ». ⟪مهم : إذا كان متجرك خارج السعودية، تواصل مع تابي مباشرة لاستكمال إعداد حساب التاجر وتفعيله قبل ربط الحساب بسلة.⟫ ماذا يحدث بعد التفعيل؟ بعد تفعيل تابي، يمكن أن تظهر كطريقة دفع متاحة للعملاء المؤهلين في صفحة إتمام الطلب. وتحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة. كيف تعمل تابي؟ الشراء: يختار العميل تابي عند إتمام الطلب ويقدّم المعلومات التي تطلبها تابي. الدفع على دفعات: يختار العميل أحد خيارات الدفع المتاحة له من تابي. تنفيذ الطلب: تعالج الطلب وتشحنه كالمعتاد. وتتولى تابي تحصيل المدفوعات من العميل وفق شروطها، ويستلم متجرك مستحقاته وفق اتفاقية التاجر …

**Citation Q6-SA-C073:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة); قبل البدء | 2026-09-16 | kind: stated | quote check: found
- quote: تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …مقدمًا. ويمكن أن تساعد خيارات الدفع المرنة على زيادة القوة الشرائية، وتحسين إتمام الطلب، ورفع متوسط قيمة السلة. الدفع والتسوية: تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة. وتخضع مواعيد تحويل المستحقات ورسوم التاجر للاتفاقية المبرمة بينك وبين تابي. ما الذي تحتاج إلى تجهيزه قبل التفعيل؟ جهّز المتطلبات التالية قبل ربط تابي بمتجرك: ما تحتاج إليه المتطلب يجب أن يكون متجرك موثّقًا قبل ربط تابي وتفعيلها. متجر موثّق على سلة ⟪تحتاج إلى حساب تاجر مفعّل لدى تابي. إذا كان متجرك خارج السعودية، استكمل إعداد الحساب مباشرة مع تابي.⟫ حساب تاجر لدى تابي جهّز Merchant Public Key وMerchant Private Key من حسابك لدى تابي. بيانات الربط تتوفر تابي على باقات بلس، وبرو، وسبيشال. باقة مؤهلة في سلة كيفية تفعيل تابي على متجرك لربط حساب تابي بمتجرك على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ثم اختر «تابي». أدخل Merchant Public Key وMerchant Private Key المرتبطين بحسابك لدى تابي. راجع …

### Q6-SA-007

**Cited at:** section 1, line 31; section 1, line 32; section 1, line 33; section 2, line 54; section 2, line 55; section 5, line 89

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-007
- bears_on: 1;2
- identifier: countryOther.description
- statement: We’re currently available in Saudi Arabia and the UAE. We’ll notify you when Salla becomes available in your country.
- scope: persona (merchant dashboard translations, en), countryOther
- cite_ids: Q6-SA-C010
- from: held

**Citation Q6-SA-C010:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/persona.json` | key countryOther.description | 2026-10-08 | kind: observed | quote check: found
- quote: We’re currently available in Saudi Arabia and the UAE. We’ll notify you when Salla becomes available in your country.
- in context: …r an account other features Your Salla Pro plan will be activated once your store is verified as a charity from the dashboard. Salla Pro, free for life Explore other features Create your charity store Supporting your journey of giving Go back Close Confirm migration Continue migration Later minute Migrate your store Optional Go back Skip Try again Nice to meet you, Your country selection sets the legal requirements for your store. Back to log in ⟪We're currently available in Saudi Arabia and the UAE. We'll notify you when Salla becomes available in your country.⟫ Thanks for your interest in joining Salla! Estimated time: {{minutes}} minute Estimated time Estimated time: 1 minute Estimated time: 1 minute Let's learn more about your business, so we can set you up for success! Something went wrong while creating your store. Please try again. We couldn't create your store Preparing for your big launch... Getting your shelves ready... Ready to set up your store? Creating your store... Higher trust in Salla st…

### Q6-SA-058

**Cited at:** section 1, line 34; section 2, line 54

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-058
- bears_on: 2
- identifier: bank_transfer.country_not_supported
- statement: التحويل البنكي غير متاح حالياً لدولتك ({{country}}).
- scope: payments (merchant dashboard translations)
- cite_ids: Q6-SA-C075;Q6-SA-C076
- from: held

**Citation Q6-SA-C075:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | key bank_transfer.country_not_supported | 2026-10-08 | kind: observed | quote check: found
- quote: التحويل البنكي غير متاح حالياً لدولتك ({{country}}).
- in context: …nt_name":"اسم صاحب الحساب","account_number":"رقم الحساب","account_number_alphanumeric_invalid":"رقم الحساب يجب أن يحتوي على أرقام وحروف إنجليزية فقط.","account_number_invalid":"رقم الحساب يجب أن يحتوي على أرقام فقط.","add_account":"إضافة حساب بنكي","alternate_identifier_enabled":"إضافة المعرِّف البديل للتحويل الفوري (سريع)","bank_name":"البنك","cancel":"تراجع","certificate_type":"نوع الشهادة","copied":"تم نسخ {{field}}.","country_not_supported":"⟪التحويل البنكي غير متاح حالياً لدولتك ({{country}}).⟫","delete":"حذف الحساب","delete_confirm_message":"سيتُحذف الحساب نهائيًا من متجرك ولن تتمكن من استعادة بياناته.","delete_modal_title":"هل تود حذف هذا الحساب البنكي؟","delete_success":"حُذف الحساب البنكي.","edit":"تعديل","edit_title":"تعديل الحساب البنكي","empty":{"description":"أضف حسابًا بنكيًا لمتجرك لاستقبال الحوالات البنكية من عملائك.","title_bold":" حسابًا بنكيًا","title_end":" بعد","title_start":"لم تُضِف"},"iban_invalid":"رقم الآيبان غير ص…

**Citation Q6-SA-C076:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/payments.json` | key bank_transfer.country_not_supported | 2026-10-08 | kind: observed | quote check: found
- quote: Bank transfer isn't available yet for your country ({{country}}).
- in context: … name","account_number":"Account number","account_number_alphanumeric_invalid":"The account number must contain only English letters and digits.","account_number_invalid":"The account number must contain digits only.","add_account":"Add bank account","alternate_identifier_enabled":"Add a Sarie ID for instant transfers","bank_name":"Bank","cancel":"Cancel","certificate_type":"Certificate type","copied":"{{field}} copied.","country_not_supported":"⟪Bank transfer isn't available yet for your country ({{country}}).⟫","delete":"Delete account","delete_confirm_message":"Once deleted, this bank account and its data can't be restored.","delete_modal_title":"Delete this bank account?","delete_success":"Bank account deleted.","edit":"Edit","edit_title":"Edit bank account","empty":{"description":"Add a bank account to start accepting bank transfer payments.","title_bold":" a bank account","title_end":" yet","title_start":"You haven't added"},"iban_invalid":"This I…

### Q6-SA-062

**Cited at:** section 1, line 34; section 2, line 51

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-062
- bears_on: 2
- identifier: GET /admin/v2/gateways/payment: data.online_payment_gateways; data.digital_wallets; data.bnpl; data.other_payment_methods
- statement: "online_payment_gateways": [{"slug": "salla", "category": "online_payment_gateway", "label": "noon", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/salla.png", "is_active": false, "unavailable_reason": null, "verification_status": "completed", "available_countries": [], "next_action_url": "https://api.salla.dev/admin/v2/gateways/payment/salla/activate"}], "digital_wallets": [{"slug": "paypal", "category": "digital_wallet", "label": "باي بال", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/paypal.png", "is_active": false, "unavailable_reason": null, "verification_status": "uncompleted", "available_countries": []}], "bnpl": [{"slug": "tabby", "category": "bnpl", "label": "تابي", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/tabby_en.png", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}, {"slug": "tamara", "category": "bnpl", "label": "تمارا", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/tamara.svg", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}, {"slug": "mispay", "category": "bnpl", "label": "إم آي إس باي", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/mispay_installment.png", "is_active": false, "unavailable_reason": null, "verification_status": "uncompleted", "available_countries": []}, {"slug": "madfu", "category": "bnpl", "label": "مدفوع", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/madfu_installment.png", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}, {"slug": "emkan", "category": "bnpl", "label": "إمكان", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/emkan.png", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}], "other_payment_methods": [{"slug": "mokafaa-alrajhi", "category": "other_payment_method", "label": "مكافآت الراجحي", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/mokafaa-alrajhi.png", "is_active": false, "unavailable_reason": null, "verification_status": "uncompleted", "available_countries": []}, {"slug": "cod", "category": "other_payment_method", "label": "الدفع عند الاستلام", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/cod.png", "is_active": false, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}]
- scope: store real-merchant, observed 2026-10-12; merchant_type KSA
- cite_ids: Q6-SA-C081;Q6-SA-C082
- from: held
- note: Saved response of the payment methods page (/payments). The four lists are recorded in full; each item carries available_countries and unavailable_reason. Bears on Q6-SA-N04.

**Citation Q6-SA-C081:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/1488.json` | GET https://api.salla.dev/admin/v2/gateways/payment, step 42 | 2026-10-12 | kind: observed | quote check: found
- quote: "merchant_type": "KSA", "quick_methods": [{"slug": "mada"
- in context: …تجارية 572000010006086281444 SA0380000572608016281444 active {"status": 200, "success": true, "data": {"master": {"epayment_enabled": true}, "is_first_time_setup": false, "verification": {"status": "completed", "is_owner": false, "blocks_payment_activation": false, "verify_url": "https://s.salla.sa/entity/verification/verify", "summary": {"store_documented": true, "kyc_complete": false, "has_approved_epayment_request": true}, "rejection": null}, ⟪"merchant_type": "KSA", "quick_methods": [{"slug": "mada"⟫, "is_enabled": true, "is_available": true, "is_effective": true, "blocked_by": null, "unavailable_reason": null, "has_advance_settings": false, "label": "مدى", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/mada.png", "description": null, "fees": {"percentage": 1, "flat_amount": "1.00", "currency": "SAR"}, "limits": null, "advance_settings_state": null, "next_action_url": null, "verification_status": null}, {"slug": "credi…

**Citation Q6-SA-C082:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/1488.json` | GET https://api.salla.dev/admin/v2/gateways/payment, step 42 | 2026-10-12 | kind: observed | quote check: found
- quote: {"slug": "emkan", "category": "bnpl", "label": "إمكان", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/emkan.png", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}
- title, opening and note boxes: as for this source's citation above
- in context: ….assets.salla.network/prod/admin/cp/assets/images/mispay_installment.png", "is_active": false, "unavailable_reason": null, "verification_status": "uncompleted", "available_countries": []}, {"slug": "madfu", "category": "bnpl", "label": "مدفوع", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/madfu_installment.png", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}, ⟪{"slug": "emkan", "category": "bnpl", "label": "إمكان", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/emkan.png", "is_active": true, "unavailable_reason": null, "verification_status": "completed", "available_countries": []}⟫], "other_payment_methods": [{"slug": "mokafaa-alrajhi", "category": "other_payment_method", "label": "مكافآت الراجحي", "logo": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/mokafaa-alrajhi.png", "is_active": false, "unavailable_reason": null, "verification_status": "uncompleted", "available_countries": []}, {"slug": "cod", "category": "other_payment_method", "label": "الدفع عند الاستلام", "logo": "https://cdn.assets.salla.network…

### Q6-SA-038

**Cited at:** section 2, line 38; section 5, line 93

**Record** (`studies/proposals/records/Q6/salla/statements.tsv`):
- stmt_id: Q6-SA-038
- bears_on: 1
- identifier: ❓ في حال كان لدى التاجر أكثر من متجر
- statement: نعم يمكن إدخال نفس البيانات إذا كان مالك المتاجر هو نفس الشخص، ولا يوجد حد أعلى لعدد المتاجر التابعة لمالك واحد.
- scope: أسئلة شائعة حول توثيق المتجر
- cite_ids: Q6-SA-C053
- from: held

**Citation Q6-SA-C053:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 23 (article zbcnt9hu9kf8lfh2gmf1vccr, أسئلة شائعة حول توثيق المتجر); ❓ في حال كان لدى التاجر أكثر من متجر | 2026-08-29 | kind: stated | quote check: found
- quote: نعم يمكن إدخال نفس البيانات إذا كان مالك المتاجر هو نفس الشخص، ولا يوجد حد أعلى لعدد المتاجر التابعة لمالك واحد.
- in context: …فق في منصة الأعمال. ❓ كيف يمكنني إضافة معلومات تواصل إلى متجري؟ من صفحة (تخصيص الثيم)، من قسم رأس وتذييل الصفحة . ❓ في حال فشل توثيق متجري على ابشر، كم مرة يمكنني المحاولة؟ التوثيق عبر منصة ابشر يمكنك المحاولة ثلاثة مرات في اليوم، البيانات الأخرى لا يوجد عدد محدود للمحاولة. ❓ في حال كان لدى التاجر أكثر من متجر، هل يمكن له التحقق من صحة بيانات جميع متاجره على سلة باستخدام نفس البيانات؟ وهل يوجد حد أقصى لعدد المتاجر التي تم التحقق من صحة بياناتها؟ ⟪نعم يمكن إدخال نفس البيانات إذا كان مالك المتاجر هو نفس الشخص، ولا يوجد حد أعلى لعدد المتاجر التابعة لمالك واحد.⟫ ❓ في حال نوع الكيان فرد، ولدى التاجر متجرين، ومجموع مبيعاتهما معاً أكثر من 375 ألف ريال سنوياً، هل سيتم تطبيق قيمة الضريبة بشكل منفصل على كل متجر أم يتم معاملتهما معاً كمتجر واحد؟ يتم الرجوع إلى هيئة الزكاة والدخل بأي استفسارات تتعلق باستحقاق ضريبة القيمة المضافة. ❓ كيف سيعرف العملاء أن المتجر تم التحقق من صحة بيانات؟ التحقق من صحة البيانات خاص بمنصة سلة. ❓ تنفرد المؤسسات الوقفية بأن ليس لها مالك وإنما يقوم عليها ناظر أو مجلس إدارة، عند التحقق م…

### Q6-SA-K0083

**Cited at:** section 2, line 43; section 3, line 70

**The same record as Q2-SA-K0083,** whose card is in `Q2-salla.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: 🌍دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها.
- scope: الإمارات (article: إنشاء متجر جديد خارج السعودية - الإمارات)
