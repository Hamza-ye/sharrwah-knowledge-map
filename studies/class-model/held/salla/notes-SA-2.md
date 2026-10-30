# Held pass, Salla, batch SA-2: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163:
- `apps-route-manifest`, the App Store's 28 routes (entries 1 to 28);
- `canvas-apps`, 1 (29);
- `changelog-categories`, 22 (30 to 51);
- `changelog-entries`, 20 (52 to 71);
- the first 59 of `com-plans` (72 to 130): the Arabic plans page's header, its plan cards and the first testimonials, ar-ae text.txt lines 1 to 68.

Entry numbers below are the batch's order (`held_entries.py show --batch SA-2`).

**Placed:** 106 entries on capabilities, 4 `new`, 20 `out`, in 135 lines. 14 entries take two or three lines. Supports: 117 `core`, 8 `shows`, 1 `extension-point` (54, the partners' apps newsletter), no `own-service` and no `outside`. Fillers: Apple Pay (56) and SPL (70). Qualities: two prices, a free price, unlimited customers, the free Salla Point app, a 250 MB video limit and a 30 kg weight limit.

**Sources read:**
- the guides the brief names: observed-sa's README, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's five rows and `index/ledger-summary.tsv`. No ledger file enumerates these structures; the apps sitemap ledger joins the App Store's pages;
- `apps-route-manifest`: items, meta and `urls.json`, and the manifest's record, `raw/runs/20261009T024920Z-apps-route-manifest/fetch.warc.gz@1152`. The route modules aren't held, so to clarify a route I read the App Store pages the register names (`raw/runs/20261008T121633Z-apps-pages/fetch.warc.gz`): kit/starter @7238549, company/997551250 @6606820, app/939200655 @4895218, faq @6717369, contact @6662299, general-policy @6774621. I also read /en, `raw/runs/20261008T095742Z-stage0-entry-points/fetch.warc.gz@1091149`;
- `canvas-apps`: `source.json` and meta;
- `changelog-categories` and `changelog-entries`: items and `source.json`. Each post's `content`, which the selection drops, was read to clarify. Scope and quality were taken from it as the item's own source (rule 1);
- `com-plans`: ar-sa and ar-ae `text.txt`, and the pages' records, `raw/runs/20261008T133928Z-com-plans/fetch.warc.gz@876595` (ar-sa) and `@1129` (ar-ae).

No batch has placed these structures before. SA-1 and SA-7 hold lines on the same things, and I kept to them:
- the App Store is CM-APP-002;
- Mushammir, the dashboard's assistant, is CM-AIA-002;
- the merchant's sign-in and sign-out are CM-ACC-001.

## Rules my lines follow, for SA-3 and SA-4

`SA-3` and `SA-4` hold the rest of `com-plans` and haven't run. Their part starts at SA-E-1347a5cf, the testimonial at ar-ae line 69, and covers the ar-sa lines no ar-ae line holds, the English pages and the comparison table. Here are the rules I kept, so the coordinator can align the batches.

1. **One entry, every place it stands.** An entry is one text, wherever the page repeats it. I grepped `text.txt` for each place, and the readings cite each line. The page draws every block twice, once per layout: the cards at ar-sa lines 15 to 68 and again at 134 to 187; the testimonials, the footer and the comparison table repeat too.
2. **A card's line is scoped to the plan whose card holds it, and to the plans that hold that plan's lines.** Plus's card says 'كل مزايا سلة بيسك + المزايا التالية:' (line 35), and Pro's card says 'كل مزايا سلة بيسك وسلة بلس + المزايا التالية:' (line 53). So:
   - Basic's lines take `سلة بيسك;سلة بلس;سلة برو`;
   - Plus's lines take `سلة بلس;سلة برو`;
   - Pro's lines take `سلة برو`;
   - the Special card's lines take `سلة سبيشل`. No card says Special holds the others' lines, so I gave Special nothing more.
3. **The comparison table's marks (the brief's known case).** The table "قارن واختر الباقة الأنسب لانطلاقتك" (ar-sa line 87) has three columns, سلة بيسك, سلة بلس and سلة برو. Special has no column.
   - In the page's HTML (ar-sa record @876595), each row of المزايا الأساسية is followed by three marks in the cards' order: `data-framer-name="Included (Check)"` or `"Not Included (Cross)"`. That is 27 marks over 9 rows, 19 included and 8 not.
   - Read this way, and by my reading of the bytes:
     - unlimited products, unlimited orders and the discounted labels are ✔✔✔;
     - all product types, electronic payment, إعلانات سلة and محلي are ✘✔✔;
     - SEO and the VAT line with the Zakat authority are ✘✘✔.
   - Each row's scope is the plans it is included in. A row isn't placed on a plan that is ✘.
   - The other groups (الدفع to العملاء, lines 118 to 126) hold no rows in the held text: their bodies are collapsed. Each is a container (rule 3).
4. **What the cards say, and how it is placed:**
   - a plan's name, its choose button, its price, the policy 'كل مزايا …', the header's plan links and the Special card's 'تواصل معنا' are `core` on CM-PLN-001;
   - a price is a `quality` ('annual price: 990'). Its currency (ر.س on /plans, د.إ on /ar-ae/plans) and its period (سنوي) are in `reading`;
   - a tagline (whom the plan is for, a claim of what it does) and the cards' '+30 ميزة أخرى' and '+50 ميزة أخرى' are `shows`;
   - the billing toggle شهري / سنوي is CM-PLN-002, `core`;
   - a card's feature line is `core` on its feature's capability, with the plans as its scope. A limit it states ('عدد لا محدود') is its quality.
5. **Market.** The ar-sa and ar-ae pages are the same text, except the currency. I put no market in `scope`: the labels are the capture's, and the pages state no country beside the prices. The UAE page's currency sign (96) is `out` as market data.
6. **Out:**
   - the language switch, the 'Button' placeholder, the 'الأكثر طلبًا' badge, the merchant-count claim and the slogan;
   - each testimonial and its author's name, since they are one person's words.
7. **The site's navigation headings** are containers (rule 3). الموارد goes on CM-ONB-003, since its footer children are the help centre, academy and community. الحلول and القطاعات are `new` (below). The footer's links themselves come later in the text (ar-sa lines 280 to 327), so they are SA-3's or SA-4's.
8. **Lines with no entry.** Some card lines are missing from the entries, even where the page states them: 'عدد لا محدود من المنتجات', 'عدد لا محدود من الطلبات', 'تفعيل الدفع الإلكتروني' and 'إضافة كل أنواع المنتجات'. Each equals a concern-map statement or inventory entry (SA-C-020/decides/SA-S-1949; SA-I-0949, SA-I-0952), so the batch's entries leave them out. They aren't placed here.

## New things

1. **`new:canvas`** (29, SA-E-93778890).
   - What the entry states: the dashboard's canvas registry (api.salla.dev/ui/v1/apps/prod/canvas) serves one app, `@salla.sa/platform/app`, at '/^/canvas($|/)/'.
   - Place of its own: an admin route, the registry's path, kept apart from the main dashboard registry's 82 apps.
   - What it is isn't stated. The bundle is a stub, `raw/runs/20261008T115555Z-dashboard-bundles/fetch.warc.gz@35681529`, 258 bytes, which loads `./index-7JoHKsy4.js`; that chunk is held at `raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz@359246`, and I didn't read it. No run opened s.salla.sa/canvas.
   - The feature `canvas-mode` (plans plus, pro and special; enabled on the demo stores, not on the merchant store, `index/ledger/feature.tsv`) is probably the same thing. It is `dashboard-features`', another batch's.
   - What would settle it: that chunk's strings, or a run that opens /canvas.
   - Proposed: domain E (the store's design) or A (the admin), parent unknown. Its name is canvas in English; no Arabic name is held.
   - Searched: canvas; كانفاس. Nothing found.
2. **`new:تحسينات المنصة`**, Platform improvements (30, SA-E-bd796c09).
   - A changelog category (id 2). It names only a grouping, and no capability holds it, so it is placed as a container (M-13), `core`, its parent the changelog.
   - Its posts here are storefront search (53), cookie preferences (58) and Mushammir's store analysis (68). Each took its own capability.
   - No place of its own in the admin; it is a category of changelog.salla.sa.
   - Proposed: no domain. The coordinator may well read it as `out`, or fold it into a new thing for the changelog itself (below).
3. **`new:الحلول`**, Solutions (73, SA-E-e5f85d18).
   - A heading of salla.com's header and footer. Its footer children (ar-sa lines 305 to 312) are متجر التطبيقات, صانع التطبيقات, ادوات التسويق, محلي, التسويق مع المؤثرين, المدفوعات and سلة سبيشل: the platform's products, each another capability's (CM-APP-002, CM-CHN-006, CM-MKT-005, CM-CHN-002, CM-MKT-015, CM-PAY-002, CM-PLN-001).
   - No capability holds the grouping, so it is new, `core`, by M-13.
   - Place of its own: none in the admin. It is the public site's menu.
   - **A reading on M-13:** M-13 gives a container `core` "since it is the platform's own admin place". salla.com's menu isn't the admin. If the coordinator reads M-13 as covering only admin containers, 73 and 75 are `out`, as menu labels with no page.
4. **`new:القطاعات`**, Sectors (75, SA-E-4f9d972e).
   - A heading of salla.com's header and footer, over 'متاجر سلة فى القطاعات' and nine sectors (ar-sa lines 313 to 323): Salla's stores shown by business sector.
   - The page's FAQ asks 'ما القطاعات التجارية المدعومة في سلة؟' (line 267). Its answer is held in the FAQ runs the register names (20261028T145430Z-journey-com-plans-faq-ar) and isn't read here.
   - Proposed: domain A, near CM-ACC-008 (where the platform offers its service), if the sectors are what Salla supports. Otherwise it is showcase content, and `out`.
   - Searched: sector; قطاع; industry; صناعة. No capability.

**The changelog itself** (changelog.salla.sa, served by the dashboard at s.salla.sa/changelog, and the footer's مركز التحديثات, ar-sa line 301) has no capability. Searched: changelog; release notes; سجل التغييرات; التحديثات; what's new; announcement. Its categories and posts here are each placed on the capability they name. The changelog as a place for merchants is the coordinator's to decide; no entry of this batch is the changelog itself.

## Entries I couldn't tell, and what would settle each

- **The App Store's redirects (2 to 9).** Their modules (`/assets/redirect-*.js`) aren't held. I read them as redirects to the :lang routes of the same path, from their ids and the parallel routes. The root-redirect's target is read the same way. Each is placed on its target's capability, as SA-7's rule 3 does for redirects.
- **The share images, crawler files and vitals (10 to 15)** are `out`: they are the App Store site's own files, not something offered to merchants or developers. SA-7 placed a store's `llms.txt` route on CM-CNT-007, but that was the merchant's own store SEO. The alternative is CM-APP-002 `core`, as routes of the App Store.
- **preview/:id (21)** opens on no held page (the register). I placed it on CM-APP-002. It may be a developer's preview of an app listing (CM-PTN, or CM-APP-002's review) or a merchant's preview of an app. A run opening it would settle it.
- **company/:id (5, 22)** is a page per app developer company (name and 'Joined on'). I placed it on CM-APP-002, as the App Store's listing of its developers. CM-PTN-002 (the partner's account) is the alternative.
- **The App Store's FAQ (24)** takes CM-APP-002 and CM-ONB-003. Its contact page (8, 25) takes CM-ONB-003 only.
- **logout (16)** is on CM-ACC-001, as the App Store's sign-out. `out` as a router action is the alternative.
- **37, صانع التطبيقات وتطبيق الجوال.** I gave one line, on CM-CHN-006. تطبيق الجوال could instead be Salla's merchant app (CM-SRF-001), which the category's posts would settle; none is in this batch.
- **40, محلي:** Mahally (CM-CHN-002), by the cell's term. The word also means "local".
- **55 and 63, Mushammir's storefront suggestions,** are on CM-AIA-001 (AI tools; its Salla cell holds the flag suggested-by-moshamer "whose statement doesn't say what it suggests") and CM-MKT-023, not on CM-AIA-002. CM-AIA-002 is the assistant the merchant asks in the admin (51, 68, 69).
  - 63 also takes CM-SFR-001: the post's words are design elements, and its category is store design.
  - 55's scope 'الباقات المدفوعة' comes from its content ('العناصر مخصصة للباقات المدفوعة، وهي مُفعّلة تلقائياً لباقتي برو وبلس.').
- **59, smart recommendations in the cart,** is on CM-MKT-023 only. The title 'ارفع قيمة كل طلب' reads like upsell (CM-MKT-021). But CM-MKT-021's Salla cell is `extension-point` alone, so a `core` line there would change it, and CM-MKT-023's note says no statement defines upsell or cross-sell. I didn't add the line. The coordinator may.
- **60, AI-ready reviews.**
  - CM-SUP-001 `core`, and CM-AIA-005 `shows`: the CHANGES line, below.
  - Its content puts the reviews in the store's llms.txt, so CM-CNT-007 (where SA-7 placed llms.txt) is a further candidate. The entry's own words don't name it.
- **64, a coupon scheduled for the plan's renewal,** is a discount on the platform's own plan. I placed it on CM-PLN-002 (renewal), though its changelog category is marketing tools. No capability holds coupons for the platform's plans.
- **66, offers in the market's currency,** is on CM-MKT-003 (Salla's العروض, special offers) and CM-MKS-006. 62's offer priority is CM-MKT-001's, as that cell's Offer priority.
- **71, landing page templates,** whose content says they are bought from the theme store ('اختيار قالب صفحة هبوط جاهز من متجر الثيمات'), is a lead for CM-SFR-003. Its words don't name the theme store, so it has no line there.
- **Two plan card lines:**
  - 99, 'شحن محلي وعالمي', is on CM-SHP-015: the cell holds the full plan line 'شحن محلي وعالمي مع أكثر من 100 شركة شحن' (SA-C-139/decides/SA-S-2105), and the card's line is its short form. CM-SHP-001 or CM-SHP-020 (international) are the alternatives;
  - 101, selling in branches with Salla Point, is on CM-POS-001 only. 'فروعك' could also give CM-INV-005 a line.
- **The plan taglines (86, 94, 105, 117, 118) are `shows`.** They are the plan's terms and support no placement. The coordinator may read 117 and 118, the Special section's own heading and text, as `core`.

## The CHANGES line

- **CM-AIA-005@salla becomes held, by a `shows` line** (60, SA-E-1cd88cb6).
  - The post makes the store's product reviews 'جاهزة للذكاء الاصطناعي لتدعم اكتشافها واتخاذ قرار الشراء'. Its content: 'AI-Ready Product Reviews', in a structured form in llms.txt.
  - It names no channel where buyers buy through AI, and the content says it guarantees no appearance in any tool. So the line is `shows`, and the cell gains no placement.
  - Kept. `out` of CM-AIA-005, with only the CM-SUP-001 line, is the alternative.

No other line changes a cell's supports.

## Items against sources

- **`apps-route-manifest`:** I compared the 28 items' id, parentId, path, index, module, hasAction and hasLoader against the manifest's record (@1152). They are equal and in the same order.
- **`changelog-categories`:** 22 items equal `source.json`. The posts' `category_id` and `category_name` agree with the categories (5 بوليصات الشحن, 2 تحسينات المنصة, 12 متجر التطبيقات, and so on).
- **`changelog-entries`:**
  - four briefs end mid-word in the source itself: 56 ('أكثر مرونة و'), 59 ('باستخدام الذك'), 61 ('بشك'), 71 ('للمعاي'). They are Salla's truncation, not the extractor's;
  - `release_date` is relative ('منذ 13 ساعة'), as of the run, 2026-10-12;
  - the structure's label `real-merchant@ar` is a store's, and the list is the first 20 posts (the register: its later pages aren't held).
- **`com-plans`:** the items are text nodes. The comparison table's marks are only in the HTML (rule 3 above). The ar-sa toggle reads 'سنوي (خصم 16%)' (line 14) where ar-ae's reads 'سنوي' (line 14). ar-sa's struck price '11,88' (line 32), against 1,188 for twelve months, is cut in the text node.

## For the second stage: what the sources state that no entry holds

- **The App Store's FAQ** (`raw/runs/20261008T121633Z-apps-pages/fetch.warc.gz@6717369`):
  - 'The Salla App Store is your one-stop marketplace for apps built by Salla and trusted third-party developers.' This is a maker lead for CM-APP-011 on Salla, which holds nothing. It names no app;
  - 'All apps, whether made by Salla or external developers, are reviewed for quality and security before being published on the App Store.' (CM-APP-002's review);
  - the install permissions an app requests (CM-API, scopes);
  - refunds and trials, for CM-APP-003: 'uninstalling does not trigger a refund after the trial days " 7 days "';
  - 'You can only rate an app after it’s been installed and active for 14 days.';
  - 'Store admins will receive a dashboard notification when an update is available. They'll be able to accept or decline the update before it takes effect.' (CM-APP-001 or CM-APP-004).
- **The App Store's general policy** (`…@6774621`): 'Applications offered in the Salla App Store allow a 7-day trial period upon installation.', and the refund 'to the merchant's wallet automatically' (CM-APP-003, CM-PLN-006).
- **The App Store's contact page** (`…@6662299`) and footer: '24/7 instant support available', '7 days money back guarantee', 'Safe and secure payment via Salla platform' (CM-ONB-003, CM-APP-003).
- **The changelog's content:**
  - 52: the four carriers within Salla's labels: Naqel, Ajax, Sent, Logistiq. These are CM-SHP-015 fillers;
  - 53: the search history kept per market (CM-SFR-013, CM-MKS-001);
  - 56: Apple Pay by QR, with Face ID, Touch ID or the passcode (CM-PAY-012);
  - 59: the two features, turned on from the store's settings, then marketing (CM-MKT-023);
  - 65: non-buyers' reviews are moderated and carry no 'شراء موثّق' badge (CM-SUP-001);
  - 67: the video formats MP4, MOV and WEBM;
  - 70: SPL's 'نطاق تغطية الشحن محلي' and no refrigerated shipping (CM-SHP-015);
  - 71: landing page templates bought from the theme store (CM-SFR-003);
  - 54: the partners' apps it names, such as 'فلاش بوكس - إشعارات تسويقية', Javna, Rasil and others (CM-APP-002, CM-MKT-007, CM-NTF-004).
- **salla.com's plans page, beyond SA-2's entries** (ar-sa `text.txt`; SA-3 and SA-4 will meet some of these as entries):
  - the footer's 'مدعوم في: السعودية الامارات' (lines 281 to 283; CM-ACC-008);
  - 'أحِل التجار إلى سلة واكسب عمولة قد تصل إلى ١٠٠ ألف ريال' (line 295; CM-PTN-008, a quality);
  - 'مكتبة برومبتات' and 'محلل المتاجر' under أدوات التجار (lines 302 to 304; CM-AIA-001?);
  - 'جميع الحقوق محفوظة لشركة سلة القابضة' (line 324), which CM-ACC-002 already holds;
  - the FAQ's 11 questions (lines 258 to 279), answered in runs 20261028T145011Z-journey-com-plans-faq-en and 20261028T145430Z-journey-com-plans-faq-ar.

## Problems with the brief or the script

- **M-13 and a public site's menu.** The brief's container rule assumes an admin place. salla.com's header and footer headings (73, 75) fall under its letter, which gives `new` with `core`, but not under its reason. I followed the letter and said so above.
- **The checker reads no inventory entry.** A quote of a plan line held as SA-I-1105 is found only through the statement that holds the same words (SA-C-139/decides/SA-S-2105), so I cited the statement.
- **Plan-card lines with no entry.** The com-plans entries leave out the lines that equal a concern-map statement or inventory entry (rule 8 above). Their scope by card, and their marks in the comparison table, aren't read by this pass. The coordinator may want them read with SA-3 and SA-4's table rows, since the concern map's SA-S-1949 is the dashboard's plan feature (scope سلة بلس), not the public page's card for سلة بيسك.

The checker's last line, for SA-2: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (30 October 2026, after the batch)

- **The public site's headings are `out`:** الحلول (73) and القطاعات (75), by the ruling after SA-2 and SA-5 (`review-H-rulings.md`). Their links are several capabilities' pages, so each heading names only a grouping. الموارد stays on CM-ONB-003, since its links are all that capability's.
- **تحسينات المنصة (30) is CM-ONB-003's.** The changelog is the platform's news for its merchants, which salla.com's footer lists under الموارد. A category that names only a grouping of its posts goes where the changelog goes (the same ruling).
- **`canvas` (29) is Mushammir Studio, not a new thing.** The chunk the notes name, `raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz@359246`, does three things:
  - it names itself 'Salla-Mushammir-Studio/1.0 (canvas; design-preview)';
  - it holds the keys of landing pages (templates, drafts, publish, history) and of the store's identity (colours, fonts, corner radius);
  - it sends the merchant's prompts to a chat.

  So it takes CM-SFR-006 (landing pages and page builders) and CM-AIA-002 (Mushammir), both `core`. The feature `canvas-mode` (plans plus, pro and special) is probably its gate. SA-15 to SA-17 (`dashboard-features`) keep to this line, with the feature's plans as scope.
- **llms.txt (60).** The reviews' line on CM-AIA-005 stays `shows`. The entry also takes CM-CNT-007 `core`: the store's llms.txt, which Salla keeps in its SEO pages (the ruling after SA-2). Zid's three llms.txt lines on CM-AIA-005 become `shows` too, each with a CM-CNT-007 line (ZD-1, ZD-4 and ZD-12).
- **The plan cards' lines with no entry** (rule 8) are read again at Salla's amendment. CM-CAT-001's Salla cell holds 'عدد لا محدود من المنتجات' as Salla Plus's plan line (SA-S-1949, the dashboard's plans list). The public page puts the same line on سلة بيسك's card (`com-plans/ar-sa/text.txt` line 19), so the cell's scope starts at Basic. 'عدد لا محدود من الطلبات' (line 20) is the same case.
- **The other lines stand:**
  - the renewal coupon (64) is the merchant's coupon on Salla's own plan;
  - the cart's smart recommendations (59) are CM-MKT-023's;
  - Mushammir's storefront suggestions (55, 63) are CM-AIA-001's.
- **Cost:** 17.5 million tokens over 90 requests, about 135,000 an entry. The batch changes one cell, CM-AIA-005, held by a `shows` line only. A plans page mostly repeats what the concern map read.
