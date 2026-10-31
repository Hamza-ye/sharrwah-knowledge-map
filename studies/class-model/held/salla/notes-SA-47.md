# Held pass, Salla, batch SA-47: notes

130 entries (effort high), evidence at observed-sa@b0bd0b16. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-47`).
- 1 to 12: `report-widgets` (`demo@en`), its items 111 to 124 of 124, the last of the elements Salla offers for Create report (`/reports/create`). Entry 10 (SA-E-d7008573) stands for items 120, 121 and 122, three app widgets of one text. **`report-widgets` ends here.**
- 13 to 32: `report-widgets-legacy` (`demo@en`), all its 20 items, the answer of `GET api.salla.dev/reports/widgets/legacy` (page 1 of a cursor; `meta.json`: `raw/runs/20261008T212405Z-journey-reports-create-demo/responses/0050.json`, step 2). **It ends here.**
- 33 to 130: `salla-academy`, the first 98 of its entries: entries 33 to 127 are the courses page (`courses@ar`, academy.salla.com/ar/courses), 94 of them also on the home page; 128 to 130 are the first three home-page-only lines (`home@ar`, lines 12, 13 and 54). **No batch had placed `salla-academy`. SA-48 holds the rest of it (the home page from its line 55 on) and hasn't run.** The rules my lines follow are below (A1 to A8), so it can keep to them; the coordinator aligns the two.

**Placed:** 87 entries on capabilities, none `new`, 43 `out`, in 111 lines.
- Widgets (32 entries, 34 lines): 32 lines on CM-ANL-002 `core`; second lines on CM-ANL-006 `extension-point` (entry 10, the app widget) and CM-CAT-012 `core` (entry 14, the legacy Summary).
- Academy (98 entries, 77 lines): 51 lines on CM-ONB-003 `core`; CM-TRU-013 `core` twice (83, 126); CM-ACC-001 `core` (38); CM-APP-002 `core` (87); CM-PTN-009 `extension-point` (89); 21 `out` lines for 43 entries.
- No `own-service`, `outside` or `shows`, no scope, no filler. Three qualities: `course price: مجاناً` (61), `password reset link validity: ساعة واحدة فقط` (111), `verification code expiry: 60 ثانية` (115).

**Sources read:** the brief and what it names; SA-45's and SA-46's notes (with the coordinator's checks) and placements; the rulings, their last section included; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for `report-widgets`, `report-widgets-legacy`, `portal-report-builder-widgets` and `salla-academy`; `selection.tsv`'s three rows. Then each structure's `meta.json`, `items.jsonl` (each widget whole, `config.component` included) and source: for the academy, `text.txt` of both pages and the archive records their `meta.json` names, `raw/runs/20261012T061544Z-thin-surfaces/fetch.warc.gz@89535` (courses) and `@52566` (home), whose HTML gives each link's address. To clarify only: `structures/salla/dashboard-translations/{en,ar}/reportsv2.json` for the widgets' keys, SA-27's line for the Google Analytics setup task, SA-2, SA-5 and SA-6's lines for the academy and App Store links, and the model's cells.

## The widgets: SA-45's rules, kept

1. **Every widget is CM-ANL-002 `core`** (SA-45's rule 1 and the coordinator's checks): a part of the custom report at `/reports/create`, which SA-12 placed there. A widget's subject (wallet, wishlists, landing pages, visits, orders, payments, shipping, stock) gives no line where that capability's cell already holds.
2. **Publisher `salla`:** CM-ANL-002 alone. **Publisher `App ID: <REAL_APP_ID>`** (entry 10, items 120 to 122, 'MySQL Probe', data from `/platform/partners/<REAL_APP_ID>/dev`): CM-ANL-002 `core` and CM-ANL-006 `extension-point`, as SA-45's rule 4 sets them; the app's maker isn't stated, a gap.
3. **Category and the market tooltip** go in `reading`, never a line or a scope (SA-45's rules 5 and 6). Terms are the title key and the category (SA-45's rule 7).
4. **`static` values are sample data** (SA-46): item 114's distribution `recovered_abandoned_carts` / `total_abandoned_carts` places nothing.
5. **The legacy list is report-widgets' items 1 to 20, key for key** (I compared every key but `position`; the register says the same of page 1). Each legacy entry takes SA-45's line for the same item, its reading pointing at the legacy source (`report-widgets-legacy/demo@en/source.json`, `/reports/widgets/legacy`) and naming SA-45's entry.

### Where I part from SA-45, for the coordinator to align

- **Entry 14 (legacy item 2, Summary) takes a second line, CM-CAT-012 `core`.** The item's `config.component` lists the summary's values, among them 'Cost of goods sold', 'Total cost of products sold during the selected period, based on the cost per item set in product details.' (`cost_of_goods_and_services_description`), and 'Total costs', 'تشمل تكاليف المنتجات (حسب التكلفة المُسجَّلة في بيانات المنتج)'. That is the same thing as SA-46's Total costs tooltip (SA-E-fffef6d8), whose CM-CAT-012 line the coordinator let stand: a cost entered on the product, the field the ruling after SA-25 places. SA-45 placed the identical widget, report-widgets' item 2 (SA-E-f1c487cf), on CM-ANL-002 alone. Either SA-45's entry takes the same second line, or mine goes; the cell is made held by SA-25 and SA-46 either way. The term is `summary`, the only word of the entry's text (the cost is inside `config.component`, which the rendering leaves out).
- **Total visits (entries 1 and 3): 'Total store visits during the selected period (from Google Analytics).'** (`total_visits_description`). The locale names a third party as the source of the visit counts. SA-27 placed the dashboard's setup task that links Google Analytics, 'يفعّل ظهور عدد زوار متجرك في تقارير سلة', on CM-ANL-001 `extension-point` and CM-ANL-002 `core` (SA-E-5aa3d1c6). I gave the widgets no second line, by the coordinator's check after SA-46 (a report kind stays with the reports except where its words state the thing of a cell that holds nothing): CM-ANL-001@salla holds `core;extension-point`. A CM-ANL-001 `extension-point` line like SA-27's would change no cell; an `outside` line would add a support, which I don't think the widget's words carry (the interface, the setup task's app, is in SA-27's source, not here).

## The academy: the rules my lines follow (for SA-48)

- **A1. The academy is CM-ONB-003's, `core`**: Salla's own learning for merchants at academy.salla.com, as SA-2, SA-5 and SA-6 placed the link أكاديمية سلة. The brand in its name names no maker. Its pages and their parts take this line: the page titles (33, 93), the header's links to the academy's home and courses (35, 36), the section headings over courses or paths (128, 130), the link to all courses (129).
- **A2. A course** is a page of the academy: CM-ONB-003 `core`, its address and category in `reading`. It is placed by what its title says the platform does, as the brief reads a help page's title:
  - a title that names the platform's own place or feature as Salla's (SA-48 holds 'دورة إنشاء متجر في سلة', 'دورة إنشاء متجر واستخدام لوحة التحكم الجديدة', 'دورة إنشاء متجر منتجات رقمية على سلة') takes a second line on that capability, `core`;
  - a title that names a topic which is a capability's thing, without saying Salla does it (SA-48's 'دورة الاستفادة من السلات المتروكة', 'دورة صفحات الهبوط', 'دورة السيو SEO للمبتدئين', 'دورة التسويق بالعمولة', 'دورة الطباعة حسب الطلب', 'دورة إنشاء متجر دروب شبينيق'), takes a second line `shows` there;
  - a course about a third party's tool (TikTok, 64; SA-48's 'دورة جوجل انلتيكس') or a general business topic places nothing more. All 12 courses of SA-47 are of this kind: abayas (60, 63), content (64, 65, 70), the brand (66), zakat and tax obligations (67), managing a store (68), choosing a field (69), the product life cycle (71), crafts (72), candles (73).
  - A trainer named in a title (SA-48's '- فارس الشريف') goes in `reading`, not `filler`: no held statement says whether the trainer is of Salla's company or a third party, a gap to note.
- **A3. A category of courses** (49 to 55, the filter's heading 48, the footer's أقسام الموقع 91) is a container on CM-ONB-003 (M-13, by its group, the academy's course categories). Its title names a learning topic, not what the platform does, so it takes no topic line, even where it is a dashboard term: التسويق (CM-MKT-005's term), تصميم المتجر (CM-SFR-001's), إدارة الطلبات (CM-ORD-001's), الاستيراد (CM-MIG-001's). The home page bears this out: إدارة الطلبات is the category of a course on packaging products (home@ar line 179). A `shows` line on each would change no cell, since all four are `core`.
- **A4. A link to another Salla place takes that place's capability:** the help centre (37, CM-ONB-003), create a free store (38, CM-ACC-001, as SA-2's أنشئ متجرك), the App Store (87, CM-APP-002, as SA-2's root), the affiliate marketers' join request (89, CM-PTN-009 `extension-point`), the webinars on YouTube (86, CM-ONB-003; YouTube isn't in the entry's words, so no filler).
- **A5. A footer heading** over one capability's pages takes it (82 عن الموقع, whose title names the site; 91); over several capabilities' pages it is `out` (85 روابط مهمة), by the ruling after SA-2 and SA-5.
- **A6. The academy's own pages and forms** are CM-ONB-003's: its terms of use (84, and 126's first line), its complaints page (90), its join request (88), its booking form (95), its cart (98), its waitlist for a course's round (77; CM-MKT-016 is a homonym, buyers of a store), its ratings filter (42). Its privacy policy is CM-TRU-013 `core` (83, and 126's second line), the platform's privacy policy for one of its sites, as the cell's salla.com/privacy.
- **A7. The academy's learner account** (sign-in, registration, email code, Google, password reset) is a part of the academy: CM-ONB-003 `core` (34, 99, 105, 108, 111, 113, 114, 115, 123, 127). CM-TRU-001's note keeps the store's admin sign-in, which this isn't. Google (105) signs in and doesn't teach, so it is no filler of CM-ONB-003. A limit the form states is a quality (111, 115).
- **A8. `out`:** buttons, sort tabs, filter values, page numbers, form fields, prompts, messages and the copyright line. A sentence split over text nodes is read with its first node, which takes the line (115 'ينتهي الرمز خلال', with '60' and 'ثانية', lines 126 to 128); its other nodes are `out`. 'مجاناً' on every course card takes CM-ONB-003 with the price as its quality (61).

## `new` things

None. Searched with `caps --terms`: Google Analytics / تحليلات / جوجل أناليتكس; Google, pixel, tracking / تتبع; academy, course / دورة; terms of service, user agreement / اتفاقية الاستخدام / شروط وأحكام; affiliate / بالعمولة / المسوقين; webinar / اللقاءات / youtube; consultation / استشار / حجز موعد / appointment; free plan / مجاني / create store / إنشاء متجر / sign up; App Store / متجر التطبيقات; dropshipping / بدون مخزون; import / الاستيراد. Each thing is held by a capability. The academy's account has no capability of its own: I read it as a part of the academy (A7).

## Entries I couldn't tell, and what would settle each

- **83 and 126, the academy's privacy policy, on CM-TRU-013:** its text isn't held. If the coordinator reads CM-TRU-013 as salla.com's policy over stores' data only, the two lines go to CM-ONB-003 with the terms of use. No cell changes either way.
- **84, the academy's terms of use, on CM-ONB-003:** CM-ACC-002 holds 'اتفاقيه الاستخدام' as the merchant's usage agreement and its contracting party; the academy's page isn't held, so its party isn't known.
- **89, the affiliate marketers' community:** CM-PTN-009 (partners who earn commission on merchants' orders) or CM-PTN-008 (the referral programme for Salla's plans, 'اتفاقية استخدام التسويق بالعمولة'). The form at f.nativeforms.com isn't held; it would settle which.
- **88, the request to join Salla's academy** (a Google Form): who joins, trainers or learners, isn't stated.
- **95, the booking form 'حجز موعد':** its content is filled when it opens (`consult-modal`, empty in the page); what an appointment is for, and with whom, isn't held.
- **105 and the other sign-in lines, on CM-ONB-003:** CM-TRU-001 (the sign-in methods of the platform's accounts) is the alternative if the academy's account counts as one of them. No cell changes either way.
- **55, الاستيراد:** importing goods or the store's data; its courses aren't on the held page.
- **63, 'دورة إنشاء متجر عبايات بدون مخزون':** a store without stock is near dropshipping (CM-CAT-010), but the title doesn't use the word; SA-48's 'دروب شبينيق' does (A2).
- **67, 'الالتزامات الزكوية والضريبية':** a general topic of law (A2). CM-TRU-010 (the merchant's legal compliance, whose Salla cell holds `shows` lines) or CM-TAX-003 would take a `shows` line if the coordinator reads it as that capability's topic; neither changes a cell.

## A structure whose items and sources disagree

- **`report-widgets-legacy` is report-widgets' first 20 items, key for key**, but held as its own structure, so each widget has two entries (SA-45's and mine). The legacy cursor's later pages aren't held (register).
- **The widgets' rendering leaves out `config.component`** (as SA-45 and SA-46 said): entry 14's cost of goods sold, and items 120 to 122 sharing one entry.
- **The academy's `text.txt` holds the text nodes only.** Each link's address, the categories' ids (`cat2` التسويق, `cat5` تصميم المتجر, `cat6` إدارة الطلبات, `cat10`, `cat11`, `cat12`, `cat13` الاستيراد), the waitlist's `round_id` and the forms' names are in the archived HTML, which my readings cite by its record. The text shows the categories, some of which the page hides until 'أظهر المزيد'.

## For the second stage: what the sources state that no entry holds

- **Who runs the academy's software:** the sign-in forms show a logo whose `alt` is 'OSARH Pro', and the course images are served with `host=osarh.pro` (`raw/runs/20261012T061544Z-thin-surfaces/fetch.warc.gz@89535`). No text entry names it, and no held statement says whether OSARH is a provider of Salla's: a lead for CM-ONB-003's maker (the cell's reading already notes no maker for the help centre).
- **A course's own page, and the courses list's pages 2 and 3** (`/ar/courses?order=available&view=grid&page=2`), aren't held (register: 'a course's own page is not held').
- **CM-ANL-001 / CM-MKT-009:** visits counted 'from Google Analytics' (`reportsv2.json`, `total_visits_description`; items 111 and 113).
- **The legacy Summary's components** (`report-widgets-legacy/demo@en/items.jsonl`, line 2; the same in report-widgets, line 2): 'Cash on delivery fees' (CM-PAY-029), 'Payment processing fees', 'Total fees charged by payment providers (e.g., credit card fees) for processing transactions.' (CM-PAY-007), and 'Taxes', 'This amount is typically remitted to tax authorities.' (CM-TAX), with the formulas 'Total costs = Product costs + Shipping + COD fees + Online payment processing fees + Taxes' and 'Net profit = Net sales - Total costs'.
- **CM-LOY-001 / CM-API:** the wallet's credit sources include 'API partner deposit' / 'إضافة من خلال واجهة برمجة التطبيقات' and deductions 'API partner withdraw' (legacy lines 9, 10): partners' apps credit and debit a customer's wallet through the API.
- **CM-ORD-001 / CM-SHP:** item 124's link 'View orders' opens `/orders?shipping_policy_status=0`, the orders list filtered by shipping policy status; 'Count of shippable orders that do not yet have a shipping (waybill) number.'
- **The academy's home page** holds learning paths with course counts and a rating ('15 الدورات', '★', '0.3'; home@ar lines 55 to 70) and categories with counts ('مشاهدة الكل (7)'): SA-48's entries.

## Leads set aside as no leads

- **Widgets:** CM-INV-010 (by 'display', 'حسب'; the checker's NOTE on line 26), CM-AIA-003 and CM-NTF-002 (by 'such', 'order'), CM-CUS-011 (by 'salla', 'single'), CM-ACC-001, CM-EVO-001 and CM-MKS-009 (by `merchant`, `feature`, 'data' in the tooltip's condition), CM-MKS-001 (by `multi-countries`, SA-45's rule 6), CM-ORD-008 and CM-ORD-009 (by name), CM-CHK-006 (by 'change', 'line'), CM-TRU-005 (by 'data'), CM-CUS-003 (by 'مجموعة'), CM-CHN-001 (by 'channel'), CM-LOY-001, CM-LOY-005, CM-PAY-001 (by category values, rule 3).
- **Academy:** CM-MKT-016 (a homonym, 77), CM-API-004 (by 'email', 'protected' in Cloudflare's '[email protected]'; the checker's NOTE on line 92), CM-PAY-032 and CM-SUP-002 (by 'إرسال', 'رابط' in the reset message), CM-PTN-001 (by 'انضمام', 'سلة' in the academy's join request), CM-PTN-008 (by 'اتفاقية', 'استخدام'), CM-TRU-010 (by 'تجارة', 'الكترونية', a category's words), CM-CUS-001 (by 'العملاء', a category's words), CM-MKT-005, CM-SFR-001, CM-ORD-001 (category titles, A3).

## The checker's lines, read again

- **`CHANGES` CM-CAT-012@salla gains `core` and becomes held, by line 17** (entry 14). Read again against `report-widgets-legacy/demo@en/items.jsonl` line 2 (`config.component`'s `cost_of_goods_and_services`, `total_costs_summary`) and both locales' words. Kept, for the coordinator to align with SA-45's SA-E-f1c487cf (above). SA-25's and SA-46's lines make the same change; the amendment hasn't run.
- **`NOTE` line 26, first lead CM-INV-010:** by 'display' and 'حسب'. No lead.
- **`NOTE` line 92, first lead CM-API-004:** by Cloudflare's email placeholder. No lead.
- No `NEW`.

## Problems with the brief or the script

- **Two structures hold the same items** (`report-widgets` 1 to 20 and `report-widgets-legacy`), so the same widget is read twice, by two batches. The entries could note it, or the legacy list could be read as a container of the other.
- **A sentence split across text nodes** ('ينتهي الرمز خلال' / '60' / 'ثانية') makes three entries, only one of which can carry the limit.
- **A text structure's links aren't in its entries**, so where a link goes (help.salla.sa, apps.salla.sa, a Google Form) is read from the archive record each time. `text.txt` could carry each node's `href`.
- **Quoting:** I wrote ’ in prose, as SA-44 to SA-46 did, so each ' … ' in a reading is a quote. No placement row holds a double quote.

The checker's last line for SA-47, after this file was written: `130 of 130 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **The batch's one cell change stands.** CM-CAT-012 takes the legacy Summary's 'Cost of goods sold', which is counted from the cost recorded on each product, as SA-46's Total costs is. SA-45's entry for the same widget in `report-widgets` (SA-E-f1c487cf, item 2) now takes the same line, added by the coordinator. The two lists now read the same widget the same way.
- **The legacy list repeats `report-widgets` item for item,** and each legacy entry takes SA-45's line for the same item. The selection reads both lists, so the same widgets were read twice. That is recorded for the method report; nothing is changed now.
- **Google Analytics takes no second line.** CM-ANL-001@salla already holds `core;extension-point`, and SA-27's setup task holds the link.
- **The academy's rules A1 to A8 stand,** and SA-48 keeps to them. Of the entries the agent couldn't settle:
  - 89 stays on CM-PTN-009 `extension-point`: the partners' affiliate opportunities.
  - 83 and 126 stay on CM-TRU-013: the platform's privacy policy for one of its sites.
  - 84, the academy's terms of use, stays on CM-ONB-003: no capability holds the platform's terms of use as such.
  - 88 and 95 stay on CM-ONB-003 as the academy's own forms.
  - 55, الاستيراد, is a category with no topic line (A3).
  - 67, the zakat and tax course, is a general topic (A2).
- **Lead for the second stage: OSARH Pro.** The academy's sign-in forms show its logo, and its images come from osarh.pro. Who runs the academy's site isn't held. The pages' brand is Salla's, and A1 reads the academy as the platform's learning, so no line changes.
- **The checker's two NOTE lines are set aside:**
  - CM-INV-010 matched only 'display' and 'حسب';
  - CM-API-004 matched only Cloudflare's placeholder for a protected email.
- **Cost:** 13.6 million tokens over 71 requests, about 105,000 an entry.
