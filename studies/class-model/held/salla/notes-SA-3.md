# Held pass, Salla, batch SA-3: notes

130 entries of `com-plans` (effort high), evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-3`).
- 1 to 78: the Arabic page from the testimonial at ar-ae line 69 to the footer's email (ar-ae lines 69 to 293; ar-sa lines 77 to 327 and the footer's repeats): the last testimonials, the comparison table's header as the narrow layout draws it, the logo carousel, the closing banner, the FAQ's questions and the footer;
- 79 to 92: the Saudi page's lines no UAE line holds (ar-sa): the yearly discount, the savings, the struck prices, the currency sign and four FAQ questions worded differently;
- 93 to 130: the English page's header, hero and the first three plan cards, to Salla Pro's tagline (en-ae lines 1 to 39).

**Placed:** 86 entries on capabilities, 0 `new`, 44 `out`, in 116 lines (88 on capabilities, 28 `out`). Three entries take two lines: 23 and 89 (the FAQ's developer-or-designer question) and 101 (Join for free). Supports: 59 `core`, 29 `shows`; no `extension-point`, `own-service` or `outside`. Fillers: none. Qualities: Basic's price, two struck prices, three savings, the yearly discount (16%), the UAE page's AED 990, unlimited products, orders and customers, the free Salla Point app and the referral commission.

**Sources read:**
- the brief and what it names: observed-sa's `README.md`, `docs/READING.md`, `structures/README.md`; the register's `com-plans` row; `selection.tsv`'s row; the evidence map; the coordinator's rulings, its last section most;
- SA-2's placements and notes (its eight rules and the coordinator's check) and SA-5's placements and notes (its footer lines and the coordinator's corrections);
- the four labels' `meta.json` and `text.txt`, and the four pages' records, printed with `warc_text.py`: ar-sa `raw/runs/20261008T133928Z-com-plans/fetch.warc.gz@876595`, ar-ae `@1129`, en-ae `@235115`, en-sa `@555939` (sha256 as each `meta.json` states). The links' addresses, the struck prices and the comparison table's marks were read there;
- the FAQ's answers, in the runs the register names: `raw/runs/20261028T145430Z-journey-com-plans-faq-ar/steps/012.text.txt` (/plans, all 11 opened) and `steps/024.text.txt` (/ar-ae/plans), and its `index/run-notes.tsv` row. They clarify the questions only (M-12).

## Rules my lines follow

I kept to SA-2's eight rules and to SA-5's corrected footer lines. Where my lines meet theirs:

1. **One entry, every place it stands.** Each reading cites the lines in ar-sa `text.txt` (the Saudi page) and, where they differ, ar-ae; the English readings cite en-ae and say where en-sa differs.
2. **Plan scope by card.** As SA-2's rule 2. The English page's words are 'Basic', 'Salla Plus' and 'Salla Pro' (the table's columns are 'Basic', 'Plus', 'Pro'). Basic's lines take `Basic;Salla Plus;Salla Pro`, since Plus's card says 'Everything in Basic, plus:' (en-ae line 30) and Pro's 'All of Basic. All of Plus. And more' (line 43, SA-4's entry, read here as the card's words). Plus's lines take `Salla Plus;Salla Pro`.
3. **The comparison table's header** (9 to 14, ar-sa lines 206 to 223): the heading, Basic's 'مجانًا' and the short names بيسك, بلس, برو are `core` on CM-PLN-001, as SA-2's card lines. The button 'اختر' (12) and the English 'Get started' (109) name no plan in their text, but each is a link to s.salla.sa/auth/register with `utm_content` choose_basic_annual, compare_basic_annual, compare_plus_annual or compare_pro_annual, under its plan's column. I read them with the column's words, as SA-2's 'اختر سلة بيسك': `core` on CM-PLN-001, scoped to the three plans. The alternative is `out`, as a button's text alone.
4. **The English card lines are placed as SA-2's Arabic ones,** on the capability whose cell holds the same plan line: unlimited products and all product types on CM-CAT-001, unlimited orders on CM-ORD-001, online payments on CM-PAY-002 (the cell's تفعيل الدفع الإلكتروني), local and international shipping on CM-SHP-015, Salla Point on CM-POS-001. One differs (below): 'Run discount promotions' (113).
5. **No market in scope,** as SA-2's rule 5. The currency signs are `out` as market data (81, as SA-2's د.إ). The UAE page's 'AED 990' (118) is one text node: its quality keeps it whole, 'annual price: AED 990'.
6. **The footer, as SA-5's corrected lines:** الحلول's children each on their product's capability; عن سلة, أدوات التجار and the sectors `out`; the updates centre CM-ONB-003 `core`; the prompts library CM-ONB-003 `shows`; محلل المتاجر CM-CNT-007 `shows`; مدعوم في's السعودية CM-ACC-008 `shows`; the rights line CM-ACC-002 `shows`; the contact details `out`. The ar-sa footer's addresses are those of SA-5's ar-ae footer without the /ar-ae/ prefix.
7. **FAQ questions are `shows`** on the capability each names, as SA-5's. Here the answers are held (point above), so each reading quotes the answer that clarifies it. A question asks; it states nothing Salla does. The heading is CM-ONB-003 `shows`; the subheading and the numbers 1 to 11 are `out`.
8. **The savings and struck prices** (79 to 88, Saudi page only) are `core` on CM-PLN-001 with their plan as scope and the value as quality ('yearly saving: 198', 'struck price: 11,88'); the yearly discount is CM-PLN-002's ('yearly discount: خصم 16%'), the toggle's period. The two struck prices are drawn with `text-decoration:line-through` (`…@876595`).

**For SA-4**, which holds the rest of `com-plans` and hasn't run (from en-ae line 40, 'AED 2,990', to the English footer, with the English comparison table and FAQ): the English footer is SA-5's footer in English (SA-6's, which hasn't run either), and the English FAQ's answers are in `raw/runs/20261028T145011Z-journey-com-plans-faq-en/steps/012.text.txt` and `024.text.txt`.

## New things

None. Every entry's thing has a capability, or is `out` by the rulings.

## Entries I couldn't tell, and what would settle each

- **17 to 19, the closing banner's text** ('أنشئ متجرك الآن بأدوات مرنة وحلول متكاملة تساعدك في كل خطوة نحو نمو مبيعاتك وتسويق منتجاتك', drawn whole and in two halves): CM-ACC-001 `shows`, a call to create a store over its register button. `out` as a slogan is the alternative; SA-5 made the Special page's closing banner text CM-PLN-001 `shows`, since it named the plan, which this doesn't.
- **15, شركاء النجاح:** `out`. It heads a block named 'Partners Carousel' whose logos have no text or alt (`…@876595`). Whose logos they are (merchants', partners', carriers') isn't stated. The images' contents would settle it.
- **23 and 89, the developer-or-designer question:** CM-ACC-001 `shows` (creating a store) and CM-SFR-001 `shows` (a designer; the Saudi answer names ready, customizable themes).
- **25 and 90, the requirements to start a store:** CM-ACC-001 `shows`. The answers name the documents of the store's verification: a legal document by entity type (CM-ACC-004), and on the Saudi page a Saudi mobile number and a Saudi bank account (CM-PAY-003's verification, CM-PAY-005's payouts). The question's words name only starting a store.
- **31 and 92, which businesses and sectors may use Salla, and 33, what may be sold:** CM-TRU-009 `shows`, read as the platform's rules on who may use it and for what. The coordinator ruled that a sector's link is `out`, as whom Salla markets to; a question of which sectors Salla "supports" is a rule of use, so I didn't apply that ruling here. `out` is the alternative for 31 and 92. 33's answer also puts the merchant under the local laws, a lead for CM-TRU-010.
- **35, whether Salla supplies products:** CM-CAT-010 `shows`, from its answer naming dropshipping partners and marketplaces.
- **37, the shipping options:** CM-SHP-001 `shows`. The answer names local and international carriers and the merchant's own carrier, CM-SHP-015's.
- **41, moving a store from another platform:** CM-MIG-005 `shows`, the question's words. The answer names only importing products and customers with Salla's tools, CM-MIG-001's.
- **111, 'Accept orders with no limits':** CM-ORD-001, whose cell holds the plan line عدد لا محدود من الطلبات. The lead CM-ORD-010 (order receiving settings) is the store's own setting to stop or limit orders, not the plan's.
- **113, 'Run discount promotions':** CM-MKT-001 (discounts), by the English words. The Arabic card's same line is 'إنشاء كوبونات تخفيض', which SA-2 put on CM-MKT-002 (coupons). The coordinator may want the two aligned on CM-MKT-002.
- **126, Salla Point:** CM-POS-001 only, as SA-2; 'branches' could also give CM-INV-005 a line.

## The checker's lines, read again

- **No `CHANGES` line.** No line alone changes a cell.
- **`NOTE` on a product named with the brand** (93 'Salla Packages', 97 'Salla Special', 116 'Salla Plus', 120 'Choose Salla Plus', 129 'Salla Pro', 126 Salla Point): the first five are Salla's plans, not separate products: `core` on CM-PLN-001, as the Arabic lines. Salla Point is CM-POS-001 `core` by what the card shows, its maker not stated here, as SA-2's Arabic line (the cell's own-service rests on other statements).
- **`NOTE` on first leads that hold nothing:** CM-AIA-005 (125, by 'product' and 'sell'), CM-EVO-001 (127, by 'features') and CM-B2B-002 (130, 'companies', which there are business buyers): none is the entry's thing; each reading says so.

## A structure whose items and sources disagree

- **The UAE page isn't the Saudi page with another currency** (SA-2's rule 5 says it is). ar-ae and en-ae draw no yearly discount ('سنوي', 'Yearly' against 'سنوي (خصم 16%)', 'Annual (16% off)'), no savings and no struck prices, and their comparison table's المزايا الأساسية has 5 rows, not 9: no بوليصات شحن سلة المُخفضة, إعلانات سلة, محلي or the VAT and Zakat line (ar-sa lines 111, 114, 115, 117; absent from ar-ae lines 194 to 199). Its marks in `…@1129`: unlimited products and orders ✔✔✔, all product types and electronic payment ✘✔✔, SEO ✘✘✔ (11 included, 4 not). The Basic card on both pages keeps 'اشحن مع بوليصات سلة المخفضة'. The pages state no country beside these differences, so I put none in scope; the coordinator may read the four rows as Saudi only, for SA-2's table lines and SA-4's.
- **The struck prices are cut in the page itself:** '11,88' (ar-sa) and '11.88' (en-sa) where 990 with its saving of 198 is 1,188 (a reading); Pro's '3,588' is whole. The HTML holds the same text, so it is the page's, not the extractor's.
- **The FAQ differs by page:** the Saudi page asks 'هل خدمات سلة متاحة للتجار من خارج المملكة العربية السعودية؟' (ar-sa line 263, no entry of this batch, so it is likely a concern-map statement left out of the entries) where the UAE page asks 'هل يمكنني استخدام سلة خارج السعودية؟' (27); four questions are worded differently (23/89, 25/90, 29/91, 31/92).

## What the sources state that no entry holds (for the second stage)

- **The FAQ's answers** (`raw/runs/20261028T145430Z-journey-com-plans-faq-ar/steps/012.text.txt` lines 130 to 161, /plans; `steps/024.text.txt` lines 112 to 143, /ar-ae/plans):
  - the markets: /plans 'منصة سلة حاليًا متاحة في السعودية وفي الإمارات وقريبًا الخليج كامل.' (line 137); /ar-ae/plans 'سلة متاحة حاليًا في السعودية، والإمارات، والكويت، وعُمان، وقطر، والبحرين.' (line 119). For CM-ACC-008, whose cell holds the Saudi and UAE footer markets: the two pages differ;
  - the requirements to open a store: /plans a legal document by entity type, 'رقم جوال سعودي' and 'حساب بنكي سعودي' (line 134); /ar-ae/plans a document and a bank account (line 116). For CM-ACC-004, CM-PAY-003 and CM-PAY-005;
  - Basic is free with no time limit, and upgrading is open at any time (steps/024 line 122; steps/012 line 140, which names the upgrade to سلة بلس and سلة برو). For CM-PLN-001 (no trial on Basic; CM-PLN-001's cell holds plan-free-trial as not released);
  - the payment methods: مدى, cards, Apple Pay, cash on delivery and buy now, pay later on /plans (line 155), the same without مدى on /ar-ae/plans (line 137). For CM-PAY-002, CM-PAY-012, CM-PAY-029 and CM-PAY-015, with the UAE as the scope of mada's absence;
  - shipping: local and international carriers, and the merchant's own carrier (line 152). For CM-SHP-015;
  - import of products and customers with Salla's tools (line 158). For CM-MIG-001;
  - the store's own iOS and Android app built from the dashboard (line 161). For CM-CHN-006;
  - dropshipping partners and marketplaces as product sources (line 149). For CM-CAT-010;
  - what may be sold: 'أي منتج أو خدمة يتوافق مع الأنظمة المحلية وشروط سلة' (line 146). For CM-TRU-009 and CM-TRU-010.
- **The UAE page's comparison table** (above): four rows the Saudi page's table holds and the UAE page's doesn't, for the cells of CM-SHP-002, CM-MKT-010 (إعلانات سلة), CM-CHN-002 and CM-TAX-001.
- **The closing banner's layer names** carry text the page doesn't show ('النظام المتكامل لدعم متجرك من أقوي الخبراء في التجارة الإلكترونية', 'أسعار حصرية لتجار سلة مقابل خدمات شحن وحلول لوجستية متكاملة!', 'اصنع تطبيقك الان', `…@876595`), as SA-5 found on the Special page: the designer's names, placed nowhere.

## Problems with the brief or the script

- **The checker reads a grouped line's terms against each entry.** A banner drawn whole and in halves can't share one line with a term; I split it (17 and 18; 19).
- **The checker's brand note** fires on the English plan names (Salla Plus, Salla Pro, Salla Special) and not on the Arabic ones, as SA-5 said.

The checker's last line, for SA-3: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (30 October 2026, after the batch)

- **The Saudi pages' own lines take السعودية in their scope:** the yearly discount, the savings and the struck prices (79 to 88), by the ruling after SA-3 (`review-H-rulings.md`). The notes found what SA-2's rule 5 missed: the UAE pages draw none of these, and their comparison table has five rows, not nine. SA-4 places the table's rows and the English pages under the same ruling.
- **'Run discount promotions' (113) moves to CM-MKT-002.** It is the English of the Basic card's 'إنشاء كوبونات تخفيض', which SA-2 placed there: the same card line in the page's other language. Its English words read wider than coupons.
- **The other lines stand:**
  - the FAQ's questions are `shows`, their answers quoted only to clarify;
  - the questions on which businesses and what goods may use Salla (31, 33, 92) are CM-TRU-009 `shows`, rules of use, not the sectors' marketing links;
  - the plan-choice buttons are CM-PLN-001 `core`, as SA-2's.
- **Cost:** 8.5 million tokens over 54 requests, about 65,000 an entry. No cell changes.
