# Notes: SA-5, Salla's `com-specialplan`, entries 1 to 130 (30 October 2026)

**What I read** (effort `high`):
- the brief and what it names: observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `com-specialplan` and `com-plans`, `selection.tsv`'s rows, the evidence map, B-extent's "Cells and evidence" and conventions, the coordinator's rulings;
- the four labels' `meta.json` and `text.txt`. ar-sa and ar-ae are the same text (`diff` is empty), so the readings cite ar-ae, the entries' locator;
- the page itself, the archive record its `meta.json` names: ar-ae at `raw/runs/20261008T133928Z-com-plans/fetch.warc.gz@131106` (sha256 `c5b87bda…`, as `meta.json` states), printed with `warc_text.py`. Its links, its comparison table's marks and its FAQ's state were read there;
- SA-1's, SA-7's and SA-2's placements and notes, for the lines of salla.com and the plans that are the same things.

## The batch

- Entries 1 to 118 are the Arabic page, in the order of ar-ae `text.txt` (lines 1 to 210); 119 to 130 are the English page's header and hero (en-ae lines 1 to 16).
- **`SA-6` holds the rest of `com-specialplan` and hasn't run.** Its part starts at SA-E-5b26113e, 'Get in touch' (en-ae line 17), and is the English page from the hero's button to the footer. Its entries are, nearly one for one, the English of mine. The rules below are the ones my lines follow, so SA-6 can keep to them and the coordinator can align the two.
- No batch had placed `com-specialplan` before this one.

## Rules my lines follow, for SA-6

1. **One entry, every place it stands.** The page draws most blocks twice (one per layout) and the footer three times (ar-ae lines 163 to 210, 211 to 258, 259 to 306). Each reading cites the lines where the text stands.
2. **Lines with no entry.** The entries leave out the page's lines that equal a concern-map statement: the six card headings (ربط تكاملي ذكي … البيع للشركات وبالجملة B2B, SA-S-2188 to SA-S-2192, SA-S-2200), فريقنا معك في كل خطوة (SA-S-2194), the comparison rows' headings (SA-S-2195 to SA-S-2199) and the card text ابق متصلًا بالعالم … (SA-S-2193). So my entries are their descriptions. **Each description goes on the capability whose cell cites its heading**, and takes a line on any other thing it names (rule 2). The English page's headings aren't concern-map statements, so SA-6 holds them as entries: 'Smart Integrative Integration' is CM-PAY-028's, 'Seamless data transfer' CM-MIG-001's, 'Advanced Inventory Management' CM-INV-005's, 'Flexible payment gateway fees' CM-PAY-007's, 'An app for your store' CM-CHN-006's, 'Integration with global shopping platforms' CM-CHN-003's, 'Dedicated Account Manager' and 'Our team is with you every step of the way' CM-ONB-003's, 'Platform stability and peak readiness' CM-OPS-001's, 'Zero platform commission on your sales' CM-PLN-003's (`shows`, as the cell reads it), 'Full store customization without code' CM-SFR-002's. 'B2B Corporate and Wholesale Sales' is CM-B2B-001's: its Arabic heading is an inventory entry the concern map left unplaced (SA-I-1200, 'a marketing line for selling to businesses').
3. **Scope.** The plan page's own body (the hero, the intro, the six cards, the support card, the comparison table and the closing banner) takes `سلة سبيشل`, the page's words, as the concern map scopes its headings ('plan: سلة سبيشل'). The English page's words are 'Salla Special'. The account manager's row adds its own words, `الباقات المتقدمة`. The header, the footer, the KPI block, the testimonials and the FAQ take no scope: they state nothing for the plan. No market is put in scope: the labels are the capture's, and the ar-sa and ar-ae pages are the same text.
4. **The comparison table** (ar-ae lines 107 to 137). Its header has two image logos with no text and no alt, in blocks named `Salla` and `Other` (`…@131106`). Each row has a heading, a description and a cell per column. Read in the HTML, as the brief's known case on `com-plans` reads a plans page's marks:
   - the rows الربط بمنصات التسوّق العالمية, مدير حساب مخصص and تخصيص كامل للمتجر بدون كود are marked `Included (Check)` (and `Included (Check) Phone`) in **both** columns, with the same check image;
   - the rows استقرار المنصة وجاهزيتها للذروة and بدون عمولة منصة على مبيعاتك carry text instead: under Salla '100% uptime · 15 مليون معاملة في يوم واحد' and 'بدون عمولة منصة'; under Other '99% وفق بيانات المنصة' and 'عمولة على كل طلب عبر منصة مزيد'.

   The column Salla is the plan the page compares (its heading: محتار بين سلة سبيشل والحلول الأخرى؟), so its rows take `سلة سبيشل`. **The column Other is another platform as this page states it**: its two values (47, 50) are `out`. A platform's own words are the evidence of what it does; Salla's words about another don't place anything, on Salla or on the other platform. SA-6's 'According to platform data' and 'Commission on every order through the Mazeed platform' are the same.
5. **The two buttons to a form.** 'احجز موعدك الآن' (13) and 'تقدم بطلبك الآن' (55) open the same form at share.hsforms.com, tagged `utm_campaign=special_plan` and `utm_content=hero_book_appointment` or `cta_apply_now`. The first books the consultant the hero names (CM-ONB-003); the second applies for the plan (CM-PLN-001, as SA-2 reads the Special card's 'تواصل معنا'). SA-6's 'Get in touch' and 'Apply now' should check their own addresses in the en-ae record.
6. **Out:**
   - slogans that name nothing (10, 17, 53, 128), the merchant-count claim (14), the testimonial and its author (15, 16), the language switches (7, 125), the FAQ's subheading and its numbers 1 to 9, the comparison's button 'عرض كل المقارنة' (a `<button>` with no address);
   - **the KPI block** (ar-ae lines 40 to 70): its counters are drawn as '+', '0', '%', 'مليار ريال +' and 'مليون +' for a script (`AnimatedNumberCounter_Prod`) to fill, so no value is held. A count of buyers, orders, transaction value or visits names no feature. Two labels name a thing and take `shows`: نسبة استقرار أنظمة سلة (CM-OPS-001) and شركة تقدم خدماتها لتجار سلة (CM-PTN-005, unsure, below);
   - the footer's contact details: the phone number, the city and the email address (116 to 118), which name no service;
   - jobs at Salla (80).
7. **The site's navigation** (rule 3, containers), as SA-2 places the same headings of `com-plans`: الحلول and القطاعات are `new` with `core`, الموارد goes on CM-ONB-003, سلة سبيشل and الأسعار on CM-PLN-001, تسجيل دخول and أنشئ متجرك مجانًا on CM-ACC-001 (the second also on CM-PLN-001, for 'free'). The English headings are the same new things and capabilities. The footer's own headings: عن سلة is `new` (below); شركاء سلة goes on CM-PTN-001, the capability its title names.
8. **The footer's links** are placed by their words, read with their addresses in the record:
   - **الحلول's children:** each is the capability of the product it links to, as SA-2's note on الحلول names them: متجر التطبيقات CM-APP-002, صانع التطبيقات CM-CHN-006, ادوات التسويق CM-MKT-005, محلي CM-CHN-002, التسويق مع المؤثرين CM-MKT-015, المدفوعات CM-PAY-002, all `core`. محلي names no maker, so it is `core` by what it shows; the cell's own-service rests on SA-S-0002;
   - **الموارد's children:**
     - مركز المساعدة, أكاديمية سلة, مجتمع سلة and مدونة سلة are CM-ONB-003 `core`, the platform's help and learning for merchants;
     - مركز التحديثات and أدوات التجار are `new`, `core`;
     - مكتبة برومبتات is `new`, `shows`;
     - محلل المتاجر is CM-CNT-007, `shows`, by its address SEO-GEO-checker;
   - **عن سلة's children:**
     - اتفاقية الاستخدام is CM-ACC-001 `shows`, and سياسة الخصوصية CM-TRU-013 `core`, each as the cell already reads the same page from the sitemap (SA-S-2208, SA-S-2209);
     - اتفاقية استخدام التسويق بالعمولة is CM-PTN-008 `shows` (SA-S-2210), not the store's own affiliate marketing (CM-MKT-014), the lead's;
     - منصة الشكاوي is CM-TRU-020 `core`;
   - **شركاء سلة's children** are CM-PTN-001:
     - انضم كشريك, برامج الشركاء and موارد الشركاء are `core`;
     - مجتمع الشركاء, a form on form.nativeforms.com, is `shows`;
     - the referral line is CM-PTN-008 `core`, with its quality 'قد تصل إلى ١٠٠ ألف ريال';
   - **مدعوم في and its two markets** are CM-ACC-008 `shows`, as the cell already reads the footer's markets (SA-I-1206, SA-I-1207);
   - **the rights line** is CM-ACC-002 `shows`, as the cell already holds it (SA-S-0011, SA-S-0020).
9. **The sectors** (105 to 114) take the line of their heading's new thing, القطاعات, `shows`: each is a kind of the heading's thing, a business sector, and links to a page of salla.com about it. المنتجات الرقمية also takes CM-SEL-002 `shows`. Its link goes to this page, not to a sector page.
10. **The FAQ's questions** (59 to 75) are `shows` on the capability each names. Every question is `Closed` in the held page and its answer isn't in the HTML, so none states what Salla does. No run holds this page with its questions opened (`index/run-notes.tsv` names only the fetch `20261008T133928Z-com-plans`).

## New things

The six new things are the site's own groupings and pages. None has an admin place of its own.

1. **`new:الحلول`**, Solutions (2; 120, 'Solutions'): SA-2's new thing (SA-E-e5f85d18), the same heading on this page. Its children, as rule 8. Searched as SA-2 did.
2. **`new:القطاعات`**, Sectors (4; 122, 'Sectors'; the footer's 105 to 114). SA-2's new thing (SA-E-4f9d972e).
   - Its children here are 'متاجر سلة فى القطاعات', a link to salla.com/blog/sectors/fashion/, and nine sectors, each a page of salla.com (/ar-ae/fashion-sector, …/design-services-sector); المنتجات الرقمية links to this page.
   - Place of its own: none in the admin, only salla.com's pages.
   - Proposed, as SA-2: domain A near CM-ACC-008 if the sectors are what Salla serves, otherwise showcase content, `out`.
   - Searched: sector; قطاع; القطاعات; industry.
3. **`new:عن سلة`**, About Salla (79), the footer's heading over jobs, the usage agreement, the affiliate agreement, the privacy policy and the complaints platform. It has no address. It is a container whose title names no capability, so it is `new` with `core` by M-13's letter. The coordinator may read it as `out`, as SA-2 says of الحلول (M-13's reason is an admin place). Proposed: none.
4. **`new:مركز التحديثات`**, the updates centre (95), a footer link to community.salla.sa's category salla-news.
   - SA-2 searched for a capability of Salla's changelog and found none (changelog; release notes; سجل التغييرات; التحديثات; what's new; announcement), and proposed folding its categories into one new thing for the changelog. This is that thing's first entry.
   - Place of its own: none on this page. SA-2 notes the dashboard serves the changelog at s.salla.sa/changelog.
   - Proposed: domain A, beside CM-ONB-003 (the platform's communication with its merchants).
5. **`new:أدوات التجار`**, Merchants' tools (96), a footer link to salla.com/tools. Searched: tools; أدوات; أدوات التجار; free tools: nothing. Its address is the prefix of the two links after it (ai-prompts, SEO-GEO-checker), but a path's prefix isn't the entry's words, so they don't take its line. Place of its own: a page of salla.com, not the admin. Proposed: domain A, beside CM-ONB-003; or `out` if the coordinator reads salla.com's free tools as marketing.
6. **`new:مكتبة برومبتات`**, a prompts library (97), at salla.com/tools/ai-prompts.
   - Its page isn't held, so it is `shows`, with no place of its own.
   - Searched: prompt; برومبت; مكتبة. CM-AIA-001 (AI tools in the admin) and CM-AIA-003 (AI content generation) are features of the admin, which this isn't.
   - Proposed: domain F, beside CM-AIA-001.

## Entries I couldn't tell, and what would settle each

- **21, شركة تقدم خدماتها لتجار سلة** (a KPI label): placed on CM-PTN-005, partners' services for merchants, `shows`. A count of companies serving Salla's merchants could also be read as `out`, a statistic. Its value isn't held either way.
- **33, the description of ربط تكاملي ذكي:** CM-PAY-028 `shows`, as its heading. It names programs, tools and systems the merchant uses to run its business, not accounting or an ERP. SA-2 places the Special card's own line on ERP (com-plans) `core` on CM-PAY-028. Its English (SA-6) is the same.
- **34, the data transfer card:** on CM-MIG-005 `core` (a plan line that includes moving a store's data from other platforms by a specialized team), and CM-MIG-001 `shows`, whose cell cites the heading. Who the team is isn't stated. If the coordinator reads it as the migration service whose terms name شركة منصة سلة للاتصالات وتقنية المعلومات (SA-S-5121), the line is `own-service` instead (M-1).
- **43, Amazon and Noon through the App Store:** CM-CHN-003 `core`, with the venues as fillers, and CM-APP-002 `core`. It names no maker of the integrations: if they are partners' apps, the line is `extension-point`. The App Store's listings for Amazon and Noon would settle it (a maker gap).
- **71, SKUs:** CM-CAT-001 `shows` (a product's code). If 'track my products' means stock, it is CM-INV-001's.
- **73, minimum order quantity or purchase value:** no capability is this thing. I placed it on CM-ACC-006 `shows`, because that cell cites the Plus plan line تخصيص خيارات المتجر, whose order options list 'حد أدنى' (SA-S-2097). CM-CHK-005's and CM-ORD-010's readings also name that line. If a minimum order is its own thing, it is `new:أدنى كمية للطلب أو أدنى قيمة للشراء` (English, SA-6: 'minimum order quantity or minimum purchase value'), `shows`, with no place of its own.
- **87, برامج الشركاء:** its address is apps.salla.sa/ar/categories, the App Store's categories, not a page of the partner programme. Placed by its words on CM-PTN-001.
- **89, موارد الشركاء:** its address is docs.salla.dev. Placed by its words on CM-PTN-001. CM-DVT-001, the developer docs, is the alternative.
- **98, محلل المتاجر:** CM-CNT-007 `shows` by its address (SEO-GEO-checker). What it checks isn't held. GEO may also bear on CM-AIA-005.

## The checker's lines, read again

- **`CHANGES` CM-MIG-005 gains `core` (34).** Read against the record: 'اضمن سرعة وسهولة انطلاقتك في تجارتك مع فريق مختص لنقل بيانات متجرك مثل بيانات المنتجات والعملاء من مختلف منصات التجارة الإلكترونية إلى سلة.' (ar-ae lines 80, 82), in the Special plan's card نقل البيانات بسلاسة. This is the plan including the move of a store from other platforms. I kept it (`own-service` is the alternative, above).
- **`CHANGES` CM-SHP-003 becomes held (63), `shows` only.** The question 'وإلى أي مبلغ مدى تصل تغطية التأمين؟' names insurance cover on shipments of valuable goods. Its answer is closed. So the cell gains its terms and no placement, and whether the cover comes with Salla's own labels isn't stated. I kept it. The FAQ's answer would settle it.
- **`CHANGES` CM-CHN-003 gaining `extension-point`.** It came from my first draft of 43. I read the statement again and made it `core` (M-3: it names only the venues), so the line no longer changes the cell.
- **`NOTE` on lines for Salla Special in English (119, 123):** 'core on a product named with the platform's brand'. Salla Special is a plan of the platform, not a separate product; `core` on CM-PLN-001, as the Arabic سلة سبيشل lines are.
- **`NOTE` on new things with leads:**
  - 105's lead (CM-PTN-006) matches only سلة and متاجر, and is no lead;
  - 107's lead, CM-SEL-002, has its own line.

## A structure whose items and sources disagree

- **The entries and the text.** The entries of `com-specialplan` leave out the page's lines that equal a concern-map statement (rule 2 above). The text holds them, and the concern map reads them as plan lines. That is the selection's rule, not a fault. It means the Arabic card headings reach the model only through the concern map, while their English (SA-6) come as entries.
- **The text and the page.** The support card's text (ar-ae lines 104, 106) runs on, after its last sentence, with 'م مع خيارات الشحن المتنوعة في سلة، ودعم جميع وسائل الدفع الإلكتروني، وإيداع المبيعات كل 24 ساعة، لتجارة أيسر ونمو أسرع.', the end of the card above it (line 100) cut at its start. The HTML holds the same text, so it is the page's own, not the extractor's. I placed the sentence's things (shipping options, payment methods, the daily deposit) as the entry's own.
- **ar-sa against ar-ae.** The same text, ar-ae's KPI included: 'إجمالي قيمة العمليات بالريال السعودي' stands on the UAE page too. en-ae's is 'Total value of transactions in AED' (SA-6).

## What the sources state that no entry holds (for the second stage)

- **The comparison table's column Other.** The page's HTML shows a second logo (`framerusercontent.com/images/O2VFS3zl06rDLSTWifCfhj2maog.png`, `…@131106`) with no text. Its values name 'منصة مزيد'. This page's statement about another platform is no evidence of that platform's fees (rule 4 above), but the image may say whose column it is.
- **The FAQ's answers** (nine questions, `Closed` in `…@131106`). Not held. They would bear on:
  - CM-SHP-003, which holds nothing on Salla but this question;
  - CM-SHP-015 (heavy freight carriers);
  - CM-ACC-006 or a new thing (minimum order);
  - CM-CAT-001, CM-CAT-003, CM-SUP-001 and CM-SFR-001.
- **The KPI values** are filled by a script (`framerusercontent.com/sites/2ocTt1g4Tn7yih7svjc1R7/AnimatedNumberCounter_Prod.BmHS6QTb.mjs`, named in the record). Neither the script nor its values are held. The stability rate would be a quality of CM-OPS-001.
- **Framer's layer names** carry text the page doesn't show, such as 'ماهي المدة لتجهيز التطبيق؟' on every FAQ question, 'النظام المتكامل لدعم متجرك من أقوي الخبراء في التجارة الإلكترونية' and 'أسعار حصرية لتجار سلة مقابل خدمات شحن وحلول لوجستية متكاملة!' on the closing banner. They are the designer's names, left over from other pages, and nothing a reader sees. I placed nothing on them.
- **The footer's app links** to Google Play (`com.emoney.sallacp`) and Apple's App Store (an app whose address names it سلة تجارة إلكترونية سهلة, id1148458340), with no text: a lead for Salla's mobile apps, which observed-sa's GAPS lists as not held.

## Problems with the brief or the script

- **M-13 and a public site's footer.** As SA-2 says, the container rule's reason is an admin place, and salla.com's headings fall only under its letter. I followed the letter (الحلول, القطاعات, عن سلة). The coordinator may make them `out`.
- **The checker's brand note** fires on 'Salla Special', a plan, in English, and not on سلة سبيشل in Arabic.
- **The KPI fragments ('+', '0', '%') carry the English labels too**, since the same text stands in all four pages. So SA-6 has none of them, and they are all here.

## The coordinator's check (30 October 2026, after the batch)

- **The public site's headings and the sectors are `out`,** by the ruling after SA-2 and SA-5 (`review-H-rulings.md`):
  - الحلول and Solutions;
  - القطاعات and Sectors, and the ten sector links, المنتجات الرقمية's CM-SEL-002 line with them;
  - عن سلة;
  - أدوات التجار.

  A heading over several capabilities' pages names only a grouping. A sector's link names whom Salla markets to, and its page isn't held.
- **The updates centre (95) is CM-ONB-003 `core`,** as the changelog, the platform's news for its merchants. The prompts library (97) is CM-ONB-003 `shows`: a learning resource on the public site whose page isn't held, not a feature of the admin.
- **The data migration card is `own-service` on CM-MIG-005.** Its specialized team is the store migration service, whose terms name Salla's company as its provider (SA-S-5121). By the brief, a cell's own maker evidence counts, so the line is `own-service`, as the cell is. The checker's CHANGES line for CM-MIG-005 goes with it.
- **The other lines stand:** CM-SHP-003 held by the insurance question's `shows`, CM-CHN-003 `core` by M-3 with Amazon and Noon as fillers, and the Other column's two values `out`.
- **For SA-6:** it keeps to these corrections on the English page's same headings and links.
- **Cost:** 13.8 million tokens over 78 requests, about 106,000 an entry. The batch changes one cell, CM-SHP-003, held by a `shows` line only.
