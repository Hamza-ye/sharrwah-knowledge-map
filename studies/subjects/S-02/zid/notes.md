# S-02, phase A: zid (ZD)

Read "from what is recorded", as the brief (`studies/subjects/S-02/briefs/A-one-platform.md`) defines it.

## Documents read, in order

1. `studies/subjects/S-02/briefs/A-one-platform.md`, the brief, in full (2026-10-27).
2. `studies/subjects/S-02/bullets.tsv`, in full (2026-10-27).
3. `studies/subjects/S-02/zid/recorded.tsv`, in full: 72 rows, R001 to R072 (2026-10-27).
4. `studies/subjects/S-02/zid/recorded-citations.tsv`, in full: 154 citations (2026-10-27).
5. `studies/concern-map/platforms/zid/concerns.tsv`, in full: 96 concerns, ZD-C-001 to ZD-C-116 (2026-10-27).
6. `studies/concern-map/platforms/zid/statements.tsv`, searched with short scripts, not loaded whole: every row of the concerns ZD-C-030 to ZD-C-036, ZD-C-050 to ZD-C-053, ZD-C-060 to ZD-C-063, ZD-C-077, ZD-C-096, ZD-C-099, ZD-C-103, and of ZD-C-001, ZD-C-005, ZD-C-006, ZD-C-012, ZD-C-014, ZD-C-020, ZD-C-075, ZD-C-080, ZD-C-091, ZD-C-108, ZD-C-110; and every other row whose identifier or statement names a country, region, city, address, location, market, currency or language (2026-10-27).
7. `studies/concern-map/platforms/zid/gaps.tsv`, searched with a short script: the gaps of the concerns ZD-C-017, ZD-C-020, ZD-C-030 to ZD-C-036, ZD-C-050 to ZD-C-053, ZD-C-060 to ZD-C-063, ZD-C-077, ZD-C-099 and ZD-C-110 (2026-10-27).
8. https://help.zid.sa/markets/ (الأسواق ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/136-help.zid.sa/text.txt` (the rendered text, captured 2026-10-12T04:53:08Z), found with `method/held_index.py`. Read again because the recorded excerpts (ZD-S-0748 to ZD-S-0750) are too short to show what defines a market and what a market takes (2026-10-27).
9. https://docs.zid.sa/retrieve-store-operating-countries.md (List Store Operating Countries), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/058-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:56Z). Read again for the Country schema behind ZD-S-0744 and ZD-S-0117 (2026-10-27).
10. https://docs.zid.sa/llms.txt (the docs page index), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/044-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:42Z), searched with grep for its lines on countries, cities, addresses, locations, currencies, languages, localization, markets, regions, VAT and store settings, and those lines read; not read in full. Read again because ZD-S-0035 holds only the first words of the List Countries line (2026-10-27).
11. https://docs.zid.sa/store-33664558e0.md (Store), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/060-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:58Z): the description, the 200 example and the StoreCorePresenter schema, searched for country, city, address, location, currency, language, region and timezone. Read again because ZD-S-0087 holds only its scope (2026-10-27).
12. https://docs.zid.sa/business-33664762e0.md (Business), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/012-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:10Z): the description, the 200 example and the StoreBusinessPresenter schema, searched for country, city, address, location, national and region. Read again because ZD-S-0757 holds only its description (2026-10-27).
13. https://help.zid.sa/gcc-merchants/ (إنشاء متجر في زد لمستخدمي دول الخليج, آخر تحديث August 5, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/128-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:00Z). Read again because ZD-S-0747 is too short to show what fills the store's location (2026-10-27).
14. https://help.zid.sa/store-language/ (لغة وعملات المتجر ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:31Z). Read again because ZD-S-0745, ZD-S-0806, ZD-S-0808 and ZD-S-0810 are too short to show how the store's currency is set (2026-10-27).
15. https://zid.sa/ar/legal/terms-conditions/ (الشروط والأحكام, آخر تحديث اغسطس 2026), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (fetched 2026-10-12T04:53:53Z; its rendered text.txt holds only an error message), as text with tags removed, searched for زد متاحة في, دولته, للتجار خارج المملكة, العملة المحلية, عملة التاجر, دول الخليج, بلد and مقر, and the passages around each match read. Read again because ZD-S-0746 and ZD-S-0726 are too short to show the conditions on changing the store's country and the footer's country list (2026-10-27). The footer's زد متاحة في is followed in the text by English (EN), with no country names.
16. https://help.zid.sa/about-zid-egypt/ (حول زد مصر, آخر تحديث March 30, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/080-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:52:12Z). Read again to see whether it names the terms or the entity for merchants in Egypt (the Q1 index gap of ZD-C-031): it does not (2026-10-27).
17. https://docs.zid.sa/add-a-new-location.md (Create Location), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/004-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:02Z): the description, the request and 201 examples, and the LocationCreate schema in full; the InventoryLocation schema searched for descriptions (it has none for its fields). Read again because ZD-S-0023 and ZD-S-0100 hold only its place in the page index and its scope (2026-10-27).
18. https://help.zid.sa/store-info-ksa/ (بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/158-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:30Z). Read again because ZD-S-0751, ZD-S-0753, ZD-S-0754 and ZD-S-0763 are too short to show the store's address (2026-10-27).
19. https://help.zid.sa/saudi-merchants/ (إنشاء متجر في زد لمستخدمي السعودية, آخر تحديث August 5, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/151-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:23Z). Read again because ZD-S-0752 is too short to show what the sign-up asks of a Saudi store (2026-10-27).
20. https://help.zid.sa/tax-settings/ (اعدادات الضريبة ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/163-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:35Z). Read again because ZD-S-0814, ZD-S-0817, ZD-S-0818 and ZD-S-0820 are too short to show how VAT is set per country (2026-10-27).
21. https://help.zid.sa/shipping-settings/ (اعدادات الشحن ( لوحة التحكم الجديدة ), آخر تحديث August 5, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/155-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:27Z). Read again because ZD-S-0855 is too short to show what a region (منطقة) takes (2026-10-27).
22. https://help.zid.sa/payment-constraints/ (قيود الشحن و الدفع (لوحة التحكم الجديدة ), آخر تحديث August 11, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/144-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:53:16Z). Read again because ZD-S-0857 to ZD-S-0860 are too short to show whether a restriction takes a country or city (2026-10-27).
23. https://zid.sa/_next/static/chunks/2501-f29c20b24ab64821.js (the pricing page's compare-plans data), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/185-zid.sa/text.txt` (fetched 2026-10-12T04:53:51Z), searched with grep: the feature names (name:{ar,en}) for currency, language, country, international, global, shipping, domain, market, tax, region, address and location, and the full entries of شحن دولي, تغطية كاملة لجميع مناطق المملكة, موقع العملاء and مبيعات حسب موقع الجرد. No feature names markets (أسواق) or the activation of currencies. Read to look for the plans of markets and currencies before recording a gap (2026-10-27).
24. https://web.zid.sa/register (redirected to https://dashboard.zid.sa/ar-sa/register), its held copy in full: `evidence/product-class/runs/20261019T003529Z-proposals-Q6-zid-ar/items/001-web.zid.sa/text.txt` (rendered text, fetched 2026-10-19T00:35:29Z). It shows the first step of sign-up only (the e-mail address, then the steps معلوماتك and تفاصيل المتجر); it names no country (2026-10-27).
25. https://zid.sa/en/uae/, https://zid.sa/en/syria/ and https://zid.sa/en/egypt/ (country pages), their held copies: `evidence/product-class/runs/20261019T003516Z-proposals-Q6-zid/items/002-zid.sa/raw.html` (fetched 2026-10-19T00:35:17Z), `.../items/001-zid.sa/raw.html` (fetched 2026-10-19T00:35:16Z) and `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/190-zid.sa/raw.html` (fetched 2026-10-12T04:53:56Z), as text with tags removed, in full; their rendered text.txt holds only an error message. The Syria page's FAQ holds the answer to its first question only; the other answers are not in the page (2026-10-27). Each Starter card lists Basic payment methods (bank transfer, cash on delivery), as the Egypt page does (S02-ZD-126).
26. https://help.zid.sa/checkout-page-options/ (إعدادات صفحة إتمام عملية الشراء ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/097-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:52:29Z). Read before recording a gap on the buyer's address format; ZD-S-0961 holds only its place in the dashboard (2026-10-27).
27. https://help.zid.sa/about-marketplaces/ (عن قنوات البيع ( لوحة التحكم الجديدة), آخر تحديث August 16, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/079-help.zid.sa/text.txt` (rendered text, fetched 2026-10-12T04:52:11Z), found by `python3 -I method/corpus_search.py zid "حذف السوق" "حذف الأسواق" "إلغاء السوق" "تعطيل السوق" "السوق الافتراضي" "السوق المحلي" "السوق الرئيسي" "الأسواق" "markets" "market"` (2026-10-27). The article calls the marketplaces الأسواق.
28. https://docs.zid.sa/get-manager-profile.md (Retrieve Store Manager Profile), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/027-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:25Z), found by `python3 -I method/corpus_search.py zid "delete" "remove" "deactivate" --with "market" "markets"`: the description; the schema of user.user_profile_data, user.business_location (DefaultStoreLocationSerializer, CityPresenter) and user.store (store_business_data, currency, currencies, language); the keys markets_management.active_markets, shipping.address_fields_customizations, shipping.countries_and_cities_customization and store_language_and_currencies.* in store.subscription.policies and policies_v2, and their entries in the 200 example. Not read in full: it runs to 33,000 lines, most of them other subscription policies (2026-10-27).
29. https://help.zid.sa/payment-requirements/ (متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة ), آخر تحديث August 6, 2026) and https://help.zid.sa/shipping-adress/ (عناوين المخزون ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), their held copies in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/147-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:19Z) and `.../items/154-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:26Z), found by `python3 -I method/corpus_search.py zid "إثبات العنوان" "تأكيد العنوان" "توثيق العنوان" "is_address_confirmed" "national_address_certificate" "proof of address" "address verification" "verify address" "العنوان الوطني"` (2026-10-27). The search also listed https://zid.sa/ar/solutions/payments/, https://help.zid.sa/category/zid-pay/ and https://help.zid.sa/, not read: a category page and the help centre's home list articles, and the payments page is the source of S02-ZD-112.
30. https://help.zid.sa/senderid/ (تفعيل اسم المرسل ( لوحة التحكم الجديدة ), آخر تحديث August 3, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/152-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:24Z), found by `python3 -I method/corpus_search.py zid "زد مصر" "Zid Egypt" "Zid Syria" "زد سوريا" "Zid Kuwait" "Zid UAE" "سجل تجاري" "السجل التجاري" "Commercial Registration" --with "مصر" "Egypt" "الإمارات" "UAE" "عمان" "Oman" "البحرين" "Bahrain" "قطر" "Qatar" "سوريا" "Syria" "الكويت" "Kuwait"` (2026-10-27). The other documents that search listed match on the help centre footer (السجل التجاري 1010365366) or were read already.
31. https://zid.sa/en/legal/terms-conditions/ (the English Terms), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/194-zid.sa/raw.html`, as text with tags removed, searched for KYC, verif*, country, Kuwait and Syria, and the passages around each match read; the Arabic Terms (item 15) then searched for الأهلية القانونية, ثمانية عشر and 18. Found by `python3 -I method/corpus_search.py zid "التحقق" "توثيق" "verify" "verification" "KYC" --with "الكويت" "الإمارات" "عمان" "البحرين" "قطر" "مصر" "سوريا" "Kuwait" "UAE" "Oman" "Bahrain" "Qatar" "Egypt" "Syria"` (2026-10-27).
32. https://help.zid.sa/tap-gateway/ (بوابة الدفع تاب | Tap, آخر تحديث August 5, 2026), its held copy in full: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/162-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:34Z), listed by the second search of gap S02-ZD-G02. It names verification through نفاذ, not a check of the store's country (2026-10-27).
33. https://zid.sa/en/pricing/, its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/197-zid.sa/raw.html` (fetched 2026-10-12), as text with tags removed and as raw data, searched for market(s), أسواق, currenc*, عملات, countries, دول, international and دولي: no plan line names markets or currencies; the matches are the menu and a quote from a merchant (2026-10-27).
34. https://docs.zid.sa/-user-roles-and-permissions-604944m0.md (User Roles and Permissions), its held copy `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/003-docs.zid.sa/text.txt` (fetched 2026-10-12T04:51:01Z): the overview, and the list of permissions searched for store settings, store data, markets, currencies and tax. Read again because ZD-S-0493 holds one permission only; the list has none for markets or currencies (2026-10-27).

## Method notes

- `method/check_subject.py` and `method/quote_check.py` were read in part, to learn what the checker tests (2026-10-27).
- The container restarted after item 8; the files held items 1 to 8's reading in notes only, and no rows. Work continued from them.
- Rows of `recorded.tsv` not copied, as bearing on no bullet: R001, R004, R006, R009, R031, R032, R038, R039, R050, R051, R052, R062, R063, R064, R067, R068, R071, R072. R018 is not copied: S02-ZD-030 records the full line of the page index whose first words R018 holds.
- S02-ZD-126 (R070, the Egypt page's Starter line Basic payment methods (bank transfer, cash on delivery)) is placed under (h) only: its words name payment methods, not a country, and the Starter cards of the UAE and Syria pages read the same (item 25).
- The rendered text (text.txt) of the zid.sa pages held in the capture runs (the Terms, the country pages) is an error message (عفواً! حدث خطأ.); their raw.html holds the page, and quotes from them were tested against it.
- Every help.zid.sa page carries the help centre's footer (السجل التجاري 1010365366, الرقم الضريبي 300827827900003), so a corpus search for registration words matches every help page; the documents such a search listed were read where they could state what was sought (items 30 to 32).
- Zid uses الأسواق for two things: the markets feature (خاصية الأسواق, item 8) and the marketplaces of عن قنوات البيع (Amazon, Trendyol, Jahez, Mazeed, item 27). Statements are placed by what they say.
- S02-ZD-151 to S02-ZD-153 come from the 200 example of a response in the API reference, not from its schema; their notes say so.
- The repository's HEAD moved during the run (the coordinator's checkpoints). Held paths in `gaps.tsv` are cited at e3ac9d16c8b399ae287f9fb6e66c93f23a53cf80.
- Held pages are cited by their live URL, as the brief says, with `accessed` the date they were read here (2026-10-27) and, for an undated page, `source_date` the date its held copy was fetched.

## Not read

Checked with `python3 -I method/held_index.py` and not held, so not read: under "from what is recorded" a live page is read only when held.
- https://docs.zid.sa/countries-list.md (List Countries) and https://docs.zid.sa/retrieve-cities-by-country-id.md (List Cities for Country); their page-index lines are read (S02-ZD-030, S02-ZD-031).
- https://docs.zid.sa/countries-and-cities-1810988f0.md, https://docs.zid.sa/region-language-popup-1861342m0.md (Features: Region & Language Popup) and https://docs.zid.sa/addresses-as-a-popup-1706785m0.md (Features: Addresses as a Popup), named in the docs page index.
- https://zid.sa/en/kuwait/ and https://zid.sa/en/oman/, two of the country pages the site index names (S02-ZD-006).
- https://zid.eg/ar/ and https://zid.eg/ar/legal/terms-conditions/.
- https://dashboard.zid.sa/en/register?package_code=rise; the sign-up held at https://web.zid.sa/register shows its first step only (item 24).
- The answers of the Syria page's FAQ after its first question are not in the held page (item 25).

## Check on a copy

`python3 -I method/check_subject.py` on a copy at /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02/check-zid/S-02, output in /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02/check-zid/out (2026-10-27): no line of level error; every quote found; one review line, the claims of absence not yet audited (phase A3).

## Absence audit

Phase A3, step 1, first part: the gaps S02-ZD-G01 to S02-ZD-G03 and the absences S02-ZD-N01 to S02-ZD-N03, read under `studies/subjects/S-02/briefs/A3-absence-audit.md` (2026-10-27). S02-ZD-G04 to S02-ZD-G07 and S02-ZD-N04 are left to the second part. No capture request in `handoffs/` names these claims.

### What was found

- All six claims are **confirmed**: no held or live document read states what they say is missing. `absence-audit.tsv` gives each claim's searches, the documents read and the statements that bear on it.
- Statements added, S02-ZD-173 to S02-ZD-182, with citations S02-ZD-C299 to S02-ZD-C316, and two terms (العنوان الوطني المختصر; نقل متجرك من دولة إلى دولة أخرى). Each statement's note names its claim.
  - S02-ZD-173 (b): zid-wallet's condition on moving a Gulf merchant's store from one country to another.
  - S02-ZD-174, S02-ZD-175 (c): the collection of payments under في السعودية and في الكويت (activate-online-payments).
  - S02-ZD-176, S02-ZD-177 (c, h): ضمان زد, applied in Saudi Arabia only, for stores with Zid Pay or Mazeed.
  - S02-ZD-178 (c;h): the financing page's qualification, a company or establishment registered in Saudi Arabia (live).
  - S02-ZD-179, S02-ZD-180 (c; a;c): the entity and the governing law in the Terms served at zid.eg/ar/ (live).
  - S02-ZD-181, S02-ZD-182 (f): the short national address, required for shipments to and within Saudi Arabia (live).
- The (h) exception of the brief: S02-ZD-130 (Rise, Zid Payments gateway) now also names S02-ZD-174 and S02-ZD-175 in `conditions`; S02-ZD-133 (تمويل زد متاح لجميع الباقات ماعدا لايت) now also names S02-ZD-178.
- Read but already recorded, so not added again: the other gateways' countries (S02-ZD-116 to S02-ZD-118), the Kuwait payment requirements (S02-ZD-123, S02-ZD-155), the sender ID by Gulf country (S02-ZD-C288 to S02-ZD-C292), the Zid Pay terms' prohibited activities and sanctioned countries (S02-ZD-C164 to S02-ZD-C199), the business address's country (S02-ZD-C107), Amazon in Saudi Arabia and the UAE (S02-ZD-C209).

### Documents read, in order (2026-10-27)

Held copies are in `evidence/product-class/runs/`, at 89bf3710fdc21bd6f09fa940900e403133d69220; help pages as their article alone (`method/corpus_search.py`'s `zid_article`), zid.sa pages as raw.html with tags removed.
1. In full: help.zid.sa about_zidpay (082), zidpay_staff_and_currencies (184), activate-online-payments (085), payment-gateways (145), wallet-split (168), about-zid-financing (081), defaulting (109), zid-wallet (182), nafath_verification (140), bank-accounts (088), faq-zid-warranty (114), gcc-merchants (128), payment-requirements (147), store-info-ksa (158), and the FAQs on Zid Pay's banks (119) and on Zid Pay outside Saudi Arabia (123).
2. In passages, around the words each search matched: the Arabic and English Terms (187, 194); the Zid Pay terms for Kuwait (188, and 20261012T190225Z-s01-sources-zid item 001) and for Saudi Arabia (189, 195); the privacy policies (186, 193); the logistics terms (20261012T104936Z-s01-sources item 121) and the global and domestic shipping terms (192, 191); the partner-payouts post (196); the payments pages (20261012T104936Z-s01-sources item 126, and 198); zid.sa/llms.txt (201); the country pages of the UAE, Syria and Egypt (20261019T003516Z-proposals-Q6-zid items 002 and 001, and 190); zid-assurance (200); pricing (197); the compare-plans data (185); help.zid.sa store-language (159), saudi-merchants (151), tap-gateway (162), senderid (152), whatsapp-templates (170), whatsapp-app-vs-api (169), logistics-shipping-methods (134), deposits_zidpay (110), transactions (166), refund-requests (149) and the sales channels' FAQ (077); docs.zid.sa get-vat-settings (031), list-store-locations (043), list-store-delivery-options (042), list-of-orders (039) and credit-customer-wallet (021); the Zid Payments docs 052, 054 and 050, searched for countries and currencies (none named).
3. Live, not held (checked with `method/held_index.py` first): https://zid.eg/ar/legal/terms-conditions/ (raw; compared line by line with the held zid.sa Terms: the same 930 lines save one banner line); https://zid.sa/ar/solutions/financing/ and https://zid.sa/en/solutions/financing/ (raw); https://help.zid.sa/national-address/, https://help.zid.sa/business-verification/, https://help.zid.sa/zidfinance-requirements/, https://help.zid.sa/finance-management/ and five FAQs (ماهي متطلبات تفعيل زد باي ؟; ما هو تمويل زد؟; هل يشترط تفعيل زد باي للحصول على التمويل; هل زد باي تدعم خاصية العملات المتاحة في; كيفية تزويد زد باي بالمتطلبات لتفعيل), rendered through `method/capture/page_text.mjs`. They were found in the help centre's sitemaps (https://help.zid.sa/sitemap_index.xml, post-sitemap1.xml, post-sitemap2.xml, faqs-sitemap.xml), read as indexes only.

### Searches too many to read in full, and how they were narrowed

- `n01-own` (زد باي, مدفوعات زد, Zid Pay, ZidPay, Zid Payments) listed 48 documents past its cap of 40; it was rerun with `--max 48`. It was narrowed by `--with` the countries the absence names (12 documents) and `--with الدولة country` (19).
- Documents listed but not read, because their match cannot state what a claim says is missing: API pages whose match is a customer's or an order's field (Commercial Registration, registration, ZidPay as an order's payment method: items 005, 017, 019, 020, 028, 036, 037, 038, 062, 066, 067), an app's sign-up (029, 030, 071), Apple Pay (008, 009) or products (013, 016); category and home pages of the help centre (074, 094), which list articles; changelog.zid.sa/ar (Q8 run item 001), which names no country; zid.sa/ar/paymob/ (s01 run item 125), which names no country; help pages on WhatsApp costs, payment links, Zid Pay's payment page and digital products, partial returns and returns, whose match was زد باي or محفظة زد alone.
- The search on country names `--with الدولة country` listed every page that holds a country anywhere (13 documents); each was read in passages around the country names.

### Problems with the method

- An Arabic term matches inside words, so country names over-match: مصر matches مصرح, مصرف and المصروفات, and عمان matches العماني. The counts were checked by reading the passages; the zid.eg Terms hold no مصر as a word.
- The held corpus lacks help articles and FAQs that bear on these claims (the national address, Zid Financing's requirements, Zid Pay's requirements); `corpus_search.py` cannot list a page that is not held. They were found through the help centre's sitemaps and read live.
- The live pages' quotes were tested against the working copies with `quote_check.py`'s `norm`, since `quote_check.py` finds a live URL only once it is captured; the checker will show them as pending capture.

### Second part: S02-ZD-G04 to S02-ZD-G07 and S02-ZD-N04 (2026-10-27)

Phase A3, step 1, second part, read under `studies/subjects/S-02/briefs/A3-absence-audit.md`. No capture request in `handoffs/` names these claims.

#### What was found

- S02-ZD-N04 is **contradicted**: the FAQ's list السعودية ودول الخليج فقط (S02-ZD-007, last updated August 30, 2023) is not complete as a list of the countries Zid serves merchants in. About Zid Egypt, the Egypt page and the Syria page (S02-ZD-060, S02-ZD-061, S02-ZD-138, S02-ZD-140, recorded in phase A) and zid.eg/ar/ (S02-ZD-184, read live) state merchants in Egypt and Syria.
- S02-ZD-G04, S02-ZD-G05, S02-ZD-G06 and S02-ZD-G07 are **confirmed**: no held or live document read states what they say is missing. `absence-audit.tsv` gives each claim's searches and the documents read.
- Statements added, S02-ZD-183 to S02-ZD-191, with citations S02-ZD-C317 to S02-ZD-C326, and three terms (Region & Language popup; store countries; Display products in your store based on the customer location). Each statement's note names its claim.
  - S02-ZD-183 (d): the FAQ's next sentence, في المستقبل باذن الله نتوسع للعالم العربي (N04).
  - S02-ZD-184, S02-ZD-185 (d): zid.eg/ar/ on merchants in Egypt, and Zid as the platform of the Middle East and North Africa (N04, live).
  - S02-ZD-186 (e): List Countries, GET /v1/settings/countries with countries_cities.read, the page in G04's route (live).
  - S02-ZD-187 to S02-ZD-191 (e, f): the Region & Language popup, its settings on the inventory page, the switch off by default, and the APIs zid.store.region.countries and zid.store.region.setRegion (G06, live).
- The (h) exception: no (h) statement's conditions changed. S02-ZD-189's switch (Display products in your store based on the customer location, on the inventory page) and عرض المنتجات حسب المدينة of shipping-adress, whose arrangement S02-ZD-162 conditions, are not tied by any source read.
- Read but already recorded, so not added again: the market's actions (S02-ZD-013), the store operating countries (S02-ZD-C034), the localization endpoint (S02-ZD-054), the country pages of the site index (S02-ZD-006).

#### Documents read, in order (2026-10-27)

Held copies are in `evidence/product-class/runs/`, at 378311abab45103381b1e9d5ce672bc93955dc35; HEAD moved to e0ee694236ac99850584182f77e4661bd15a6e8b during the run, with changes to phase B's files only. Help pages are read as their article alone (`method/corpus_search.py`'s `zid_article`), zid.sa pages as raw.html through `method/quote_check.py`'s `html_text`.
1. In full: help.zid.sa markets (136); the FAQs زد يخدم التجار في السعودية فقط؟ هل يخدم الخليج؟ (175), on payment methods (176) and on a commercial registration for signing up (178); about-zid-egypt (080).
2. In passages, around the words the searches matched: gcc-merchants (128) and saudi-merchants (151) on the location; docs retrieve-store-operating-countries (058), localization (045), get-manager-profile (027: markets_management.active_markets, business_location, the countries of the 200 example, which are the store's currencies'), webhooks (070), events (025), list-store-locations (043) and list-of-orders (039); changelog.partner.zid.sa (20261019T052111Z-proposals-Q8-zid item 001); zid-growth (179); zid.sa/llms.txt (201); the Egypt and Syria pages (190, and 20261019T003516Z-proposals-Q6-zid item 001); the Arabic Terms (187) and the Kuwait Zid Pay terms (188), on their sanctions list.
3. Live, not held (checked with `method/held_index.py` first), raw or `.md`: https://docs.zid.sa/countries-list.md; https://docs.zid.sa/countries-and-cities-1810988f0.md; https://docs.zid.sa/region-language-popup-1861342m0.md; https://zid.eg/ar/; https://zid.sa/ar/pricing/ and the compare-plans data it loads, https://zid.sa/_next/static/chunks/1540-05a4190cb15785f4.js (its 183 feature names searched for markets, أسواق and سوق); and three FAQs, rendered from their raw HTML: كيف ابدأ و انشئ متجر الكتروني؟, عن زد؟ and ماهي الخدمات والخصائص المقدمة في زد؟. Held, and read live only to compare with the held copy: https://docs.zid.sa/llms.txt (its lines naming market are the same) and https://zid.sa/llms.txt (its Other countries are the same five).
4. As indexes only: the help centre's sitemaps, https://help.zid.sa/sitemap_index.xml and the six it lists that hold articles and FAQs (post-sitemap1.xml, post-sitemap2.xml, faqs-sitemap.xml, zid-faqs-sitemap.xml, page-sitemap.xml, tips-sitemap.xml), their addresses decoded and searched for slugs on markets, countries and sign-up. They list no article on the markets feature other than markets/ (lastmod 2026-08-03, the held copy's date), and zid-faqs-sitemap.xml dates the FAQ of S02-ZD-007 2023-08-30.

#### Searches too many to read in full, and how they were narrowed

- None passed its cap of 40; the plans search (`g07`, 40 documents) reached it and listed every document in full.
- The country search `--with الدولة country countries` (37 documents), the sign-up search (33) and N04's own words (33) were narrowed by their titles and matched terms. Not read: API pages whose match is an order's, customer's, coupon's or location's field (registration, a country value: items 004, 005, 016, 017, 019, 020, 021, 028, 036, 037, 038, 042, 062, 067), an app's sign-up or the App Market (008, 009, 010, 018, 071, 072, api.zid.sa's app categories), help pages on fees, gateways, wallets, shipping, tax, sender IDs, WhatsApp, warranty and returns, read by phase A or the first part for these words (081, 088, 097, 114, 123, 134, 150, 152, 154, 162, 163, 170, 182), the help centre's home and category pages (074, 093, 094), which list articles, and zid.sa pages read by phase A or the first part (185, 186, 189, 191 to 200, and the s01 runs' 121, 125, 126).
- The plans search matched Growth and النمو in the growth of a business as well as the plan; its documents were settled by their matched terms and, where open, by passages.

#### Problems with the method

- `corpus_search.py` also lists pages of the capture run 20261027T065700Z-s02-a3-zid-sources (the zid.eg Terms, national-address, the financing pages), which is in the working tree but not in git at the run's HEAD; they are the first part's live reads, and nothing here is cited from that run.
- zid.sa's pricing page loads its plan comparison from a script chunk whose name changes between versions (held: 2501-f29c20b24ab64821.js; live: 1540-05a4190cb15785f4.js); the page's own HTML does not hold the comparison, so a search of it alone does not reach the plans' features.
- The help centre's sitemap index lists zid-faqs-sitemap.xml, page-sitemap.xml and tips-sitemap.xml besides the four the first part read; zid-faqs-sitemap.xml holds the FAQ of S02-ZD-007 and the FAQs read live here.
- An Arabic term matches inside words: السوق matched السوق in general text (احتياجات السوق, كل جديد في السوق); the documents were settled by reading the passages.
- The live pages' quotes were tested against the working copies with `quote_check.py`'s `norm` (and `html_text` for HTML), since `quote_check.py` finds a live URL only once it is captured; the checker will show them as pending capture.

#### Check on a copy

`python3 -I method/check_subject.py` on a copy at /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a3-zid-2/check/S-02, output in /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a3-zid-2/check/out (2026-10-27): no line of level error and none saying a claim is not settled; 191 statements; 317 quotes found; 17 lines of level pending capture, the live citations S02-ZD-C318 to S02-ZD-C326 and the statements S02-ZD-184 to S02-ZD-191 that cite them.

## Gap-closing (phase A2)

### ZD-1: S02-VP-15, S02-VP-02, S02-VP-63 to S02-VP-66, S02-VP-76 and S02-VP-85 (2026-10-27)

Read under `studies/subjects/S-02/briefs/A2-close-gaps.md`. Zid's eight rows under these points in `variants.tsv` (S02-V-038, S02-V-182, S02-V-787 to S02-V-790, S02-V-800, S02-V-870) were all `not covered`, so all eight were taken. No lead was named. Earlier parts of zid: none; later parts: ZD-2, ZD-3. Each point's row is in `a2.tsv`, with the searches and documents in `read`.

#### What was found, by group

- **Taxes on the platform's fees (S02-VP-15):** S02-ZD-192 to S02-ZD-205 (c), citations S02-ZD-C327 to S02-ZD-C346.
  - The Terms' subscriptions section (الاشتراكات): local tax rates may vary depending on the payment method used (S02-ZD-192); the merchant pays all taxes, VAT included (S02-ZD-193); the fees exclude national sales taxes (S02-ZD-194); Zid charges taxes with its fees to the payment method (S02-ZD-195).
  - Direct shipping (زد شب): its 1-riyal service fee and its prices exclude VAT (S02-ZD-196, S02-ZD-197). Transfer fees on App Market and Theme Market refunds: 9 riyals including VAT for domestic transfers, 50 riyals for Gulf transfers (S02-ZD-198). The wallet's transfer fee: 9 riyals including VAT within Saudi Arabia, 50 riyals outside it (S02-ZD-199, S02-ZD-200).
  - Zid Pay: the mada cap excludes VAT (S02-ZD-201, the Saudi contract); Zid Payments' fees by plan exclude VAT (S02-ZD-202, S02-ZD-203); VAT is the fees x 15% (S02-ZD-204, an FAQ last updated July 16, 2024); the deposit's tax invoice (S02-ZD-205).
  - Gap S02-ZD-G08 (c, searched, not found): no document read names the tax on Zid's fees for a store by its country.
- **The countries served (S02-VP-02):** no statement added. The countries kept out are named only in the Zid Pay sections (international sanctions, S02-ZD-109, S02-ZD-110), which the general Terms and the zid.eg Terms hold in their Zid Pay sections; the Terms' sections on accounts name no country kept out. Gap S02-ZD-G09 (d, searched, not found).
- **Who sells to the buyer (S02-VP-63, S02-VP-64):** S02-ZD-206 to S02-ZD-211, citations S02-ZD-C347 to S02-ZD-C356.
  - The Terms' ضوابط المتجر الإلكتروني (E-Commerce Store Regulations): every store discloses its name and address, CR and tax number (S02-ZD-206) and gives the consumer an invoice (S02-ZD-207).
  - store-info-ksa, under السعودية: the establishment's and the company's name used in invoices (S02-ZD-208).
  - The Terms' Mazeed section: Zid, as Mazeed, the legal representative of the seller (البائع) before other commercial parties (S02-ZD-209).
  - Two FAQs read live: Zid Financing for Saudi companies and establishments only (S02-ZD-210), and financing on the business entity approved in Zid Pay, which cannot be updated (S02-ZD-211).
  - Recorded in phase A and bearing on these points: S02-ZD-080 to S02-ZD-082 (c), the business details the merchant chooses, whose requirements vary by business type and country.
  - No gap recorded.
- **Returns and cancellations (S02-VP-65, S02-VP-66):** S02-ZD-212 to S02-ZD-222, citations S02-ZD-C357 to S02-ZD-C369, and two terms (سياسة الاستبدال والارجاع; الصفحات القانونية).
  - legal-pages: الاعدادات > المتجر > الصفحات القانونية, where the merchant manages and customizes the legal policies, سياسة الاستبدال والارجاع among them, with each policy's content in Arabic and English (S02-ZD-212 to S02-ZD-217); a note for Saudi stores pointing to the Ministry of Commerce's rules (S02-ZD-218).
  - The Terms: every store makes clear its exchange and return policy (S02-ZD-219) and complies with the e-commerce laws they name (S02-ZD-220).
  - store-language: the return policy and the store's other pages are written again in English when English is activated (S02-ZD-221). List Orders: return_policy, Return policy applicable to the order (S02-ZD-222).
  - Read and not recorded: cancel-orders (live), return-order and partial-return name no market, country or policy.
  - No gap recorded.
- **The store's address (S02-VP-76):** S02-ZD-223 to S02-ZD-226, citations S02-ZD-C370 to S02-ZD-C376, and S02-ZD-206.
  - invoice-settings: the store address an invoice shows is the one in the store's basic information, an item the merchant shows or hides (S02-ZD-223); stopping Zid's invoices without another accounting system exposes the merchant to the Ministry of Commerce's fines (S02-ZD-225).
  - List Orders: store_business_address and is_store_address_active, shown on printed invoices (S02-ZD-224).
  - account-settings: the merchant adds an address to their own account (S02-ZD-226).
  - Recorded in phase A: the business address in بيانات المتجر (S02-ZD-083 to S02-ZD-085) and business_location (S02-ZD-148).
  - No gap recorded.
- **The store's country (S02-VP-85):** S02-ZD-226 only.
  - The matches on the store's country are statements recorded in phase A and A3: the country in store settings and its change (S02-ZD-055, S02-ZD-056, S02-ZD-173, all a;b), the store operating countries (S02-ZD-029, S02-ZD-C034) and user_profile_data.country_id (S02-ZD-149).
  - The markets article's دولته is the customer's (S02-ZD-024); the compare-plans data's نقل متجرك is the migration of a store from another platform.
  - S02-ZD-G01 (which setting holds the store's country; confirmed by the absence audit) remains for this point and is named in its `a2.tsv` row; no new gap.
- **The (h) exception:**
  - S02-ZD-130 (Rise, Zid Payments gateway) now also names S02-ZD-201 to S02-ZD-205 in `conditions`.
  - S02-ZD-133 (تمويل زد متاح لجميع الباقات ماعدا لايت) now also names S02-ZD-210.
  - S02-ZD-135 (no commercial registration needed to sign up) now also names S02-ZD-208.
  - S02-ZD-100 (Invoice & Tax Settings, by plan) now also names S02-ZD-223 to S02-ZD-225.

#### Documents read, in order (2026-10-27)

Held copies are in `evidence/product-class/runs/`, at d061aa38ba098252411513a77655f0b5735f1490; help pages as rendered text, zid.sa and zid.eg pages as raw.html through `method/quote_check.py --text`. Item numbers are those of 20261012T045101Z-q1-zid-sources unless another run is named.
1. In passages: the Arabic and English Terms (187, 194) on subscriptions, ضوابط المتجر الإلكتروني, زد شب, the App Market and Theme Market refunds, محفظة زد, Mazeed, the Zid Pay sections and accounts; the zid.eg Terms (20261027T065700Z-s02-a3-zid-sources item 002) on the same passages.
2. In passages: the Zid Pay terms for Saudi Arabia (189, 195) and Kuwait (188, and 20261012T190225Z-s01-sources-zid item 001).
3. In full: the payments pages (20261012T104936Z-s01-sources item 126, and 198).
4. help.zid.sa. In full: legal-pages (133), invoice-settings (131), account-settings (083), return-order (150), partial-return (143). In passages: the FAQ كيف يتم تحديد رسوم العمليات؟ (117), transactions (166), refund-requests (149), deposits_zidpay (110), zid-wallet (182), zatca-integration (174), store-info-ksa (158), store-language (159), about-zid-financing (081), the FAQ on Zid Pay's requirements (20261027T065700Z-s02-a3-zid-sources item 004), the help centre's FAQ page (077: its matches on عقوبات are Amazon's and Trendyol's penalties), gcc-merchants (128), the FAQ of S02-ZD-007 (175), payment-requirements (147), markets (136).
5. zid.sa, in passages (most matches are the footer's VAT number or زد متاحة في): partner payouts (196, on app developers' invoices; not recorded), pricing (197, and 20261027T071937Z-s02-a3-zid-sources-2 item 005), the UAE, Egypt and Syria pages (20261019T003516Z-proposals-Q6-zid items 002 and 001, and 190), zid-voice (199), paymob (20261012T104936Z-s01-sources item 125), the privacy policies (186, 193), zid.sa/llms.txt (201), the compare-plans data (185, and 20261027T071937Z-s02-a3-zid-sources-2 item 006).
6. docs.zid.sa, in passages: list-of-orders (039), get-manager-profile (027), business (012), upload-logo-image (064), llms.txt (044, its Store Settings lines).
7. Live, not held (checked with `method/held_index.py` first): https://zid.eg/ar/pricing/ (raw: no prices and no tax; its rendered text, like that of https://zid.sa/ar/pricing/, is only Zid's error text); https://help.zid.sa/cancel-orders/; two FAQs found in faqs-sitemap.xml, ما هي الكيانات المدعومة للحصول على التمويل (S02-ZD-C355) and هل بالامكان تغيير الكيان التجاري قبل\بعد الحصول على التمويل؟ (S02-ZD-C356); https://help.zid.sa/business-account/ (Meta's business portfolio for WhatsApp) and the FAQ شروط الإستخدام (a link to the Terms), neither recorded. All rendered through `method/capture/page_text.mjs` save zid.eg/ar/pricing/.
8. As indexes only: https://help.zid.sa/sitemap_index.xml and the nine sitemaps it lists (post-sitemap1.xml, post-sitemap2.xml, page-sitemap.xml, faqs-sitemap.xml, tips-sitemap.xml, zid-academy-sitemap.xml, promotion-sitemap.xml, zid-faqs-sitemap.xml, category-sitemap.xml): 656 addresses, decoded and searched for slugs on each group. They list no store-information article other than store-info-ksa.

#### Searches, and how they were narrowed

- Only S02-VP-15's second search (`--with` the market and country words) passed its cap of 40, at 44 documents; it was rerun with `--max 44`. The others were run with `--max 100` and listed every document (at most 44).
- No search was narrowed by its terms. Documents listed but not read, by their matches: the footer's VAT number or زد متاحة في alone; API pages whose match is an order's, customer's, coupon's, cart's, delivery option's or location's field (country_id, VAT, return policy); help pages whose match is an order status (إلغاء الطلب: credit-debit-notifications, change-order-status, orders-properties, customer-wallet, jahez, product-properties, activate-online-payments); the help centre's home and category pages, which list articles.
- From the sitemaps, not read: هل-مزيد-متاح-لتجار-الخليج (Mazeed for Gulf merchants) and هل-يستطيع-العملاء-من-خارج-السعودية-إتم (customers outside Saudi Arabia), whose slugs name Mazeed and buyers.

#### Problems with the method

- Single generic words (البائع, seller, fees, رسوم) went only after `--with`, as the brief says; the Terms' passages naming البائع were found by reading the Terms around the group's other terms.
- An Arabic term matches inside words: دولتك matched عملة دولتك and حسب دولتك, and دولته the customer's country in the markets article; the documents were settled by reading the passages.
- The rendered text of the pricing pages of zid.sa and zid.eg is Zid's error text, and their raw HTML holds no prices, which a script loads.
- The live pages' quotes were tested against the working copies with `method/quote_check.py`'s own `variants` and `html_text`, through a helper in the scratch folder, since `quote_check.py` finds a live URL only once it is captured; the checker shows them as pending capture.
- The repository's HEAD moved during the run (the coordinator's checkpoints); held paths are cited at d061aa38ba098252411513a77655f0b5735f1490.

#### Check on a copy

`python3 -I method/check_subject.py` on a copy at /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a2-zd-1/check/S-02, output in /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a2-zd-1/check/out (2026-10-27): no line of level error; 226 statements; 374 quotes found; 4 lines of level pending capture, the live citations S02-ZD-C355 and S02-ZD-C356 and the statements S02-ZD-210 and S02-ZD-211 that cite them.

### ZD-2: S02-VP-44 to S02-VP-46, S02-VP-55, S02-VP-56, S02-VP-67, S02-VP-68, S02-VP-73, S02-VP-74, S02-VP-78 and S02-VP-79 (2026-10-27)

Read under `studies/subjects/S-02/briefs/A2-close-gaps.md`. Zid's eleven rows under these points in `variants.tsv` (S02-V-760 to S02-V-762, S02-V-774, S02-V-775, S02-V-791, S02-V-792, S02-V-797, S02-V-798, S02-V-802, S02-V-803) were all `not covered`, so all eleven were taken. One lead was named: the FAQ هل يستطيع العملاء من خارج السعودية إتمام … (item 4 below). Earlier part: ZD-1; later part: ZD-3. Each point's row is in `a2.tsv`, with the searches and documents in `read`. Held copies were read at 00a87e3aa35463857a13342705714e963399a5c5.

#### Documents read, in order (2026-10-27)

Item numbers are those of 20261012T045101Z-q1-zid-sources unless another run is named.
1. Domain: help.zid.sa/domain/ (112) in full; settings-url-redirects (153), gcc-merchants (128) and saudi-merchants (151) in passages; the Arabic and English Terms (187, 194) in passages (أسماء النطاقات (رابط المتجر), Domain Names (Store Link), and the refunds of domains); the permission row manage.store.custom.domain (003); the compare-plans data's Custom Domain Linking (185); get-manager-profile's store_domain.* policies (027); the FAQ ماهي الخدمات والخصائص المقدمة في زد؟ (20261027T071937Z-s02-a3-zid-sources-2 item 009) in passages, not recorded.
2. Live, not held (checked with `method/held_index.py` first), rendered through `method/capture/page_text.mjs`: https://help.zid.sa/buy-new-domain/ (شراء نطاق جديد ( لوحة التحكم الجديدة), last updated August 4, 2026) and the FAQ هل اقدر أغير رابط (دومين) المتجر لاسم نطاق (domain) خاص فيني؟ بدون zid.store ؟ (last updated February 27, 2024), found in ZD-1's copies of the help centre's sitemaps.
3. As indexes only: ZD-1's decoded copies of the help centre's sitemaps (all-urls.tsv), searched for slugs on each group.
4. The lead, live, not held: https://help.zid.sa/faqs/%d9%87%d9%84-%d9%8a%d8%b3%d8%aa%d8%b7%d9%8a%d8%b9-%d8%a7%d9%84%d8%b9%d9%85%d9%84%d8%a7%d8%a1-%d9%85%d9%86-%d8%ae%d8%a7%d8%b1%d8%ac-%d8%a7%d9%84%d8%b3%d8%b9%d9%88%d8%af%d9%8a%d8%a9-%d8%a5%d8%aa%d9%85/ (هل يستطيع العملاء من خارج السعودية إتمام عملية الدفع الإلكتروني في حال تفعيل زد باي ؟, last updated July 15, 2023), rendered.
5. Checkout and customer accounts: checkout-page-options (097) in full; get-manager-profile's checkout_page_options.* policies (027); llms.txt's lines on checkout and Register Guest (044); national-address (20261027T065700Z-s02-a3-zid-sources item 009) in passages; zidpay-paymentpage (183), the security settings (076) and working-hours (173), their bodies, none recorded.
6. Language: store-language (159) in full; the Region & Language Popup (20261027T071937Z-s02-a3-zid-sources-2 item 003) in passages; Localization (045): description, 200 example and schema; get-manager-profile's store_language_and_currencies.* policies; the compare-plans feature names on language, countries, locations and inventory (185); markets (136), store-design (157) and the Egypt page (190) in passages.
7. Contact information: store-info-ksa (158), saudi-merchants (151) and gcc-merchants (128) in passages; the Terms (187) in passages; Store (060), its StoreCorePresenter; the settings category page (093). Live, not held: the category page الإعدادات > التواصل, rendered; its text lists no articles.
8. Locations: withdrawal-priority (172) and shipping-adress (154) in full; checkout-page-options (097); jahez (132), national-address, store-info-ksa and shipping-settings (155) in passages; List Locations (043): description, 200 example and schema; View Order (067) in passages; get-manager-profile's inventory_locations.* policies; the compare-plans entries on inventory (185). Live, not held, found in the help centre's sitemaps, rendered: https://help.zid.sa/create-inventory-address/ and https://help.zid.sa/inventory-transfer/ (both last updated August 3, 2026), and the FAQ كيف يتم إدارة مخزون الفرع مع مخزن المتجر الإلكتروني؟ (last updated July 15, 2023).
9. Market selection: the Region & Language Popup (20261027T071937Z-s02-a3-zid-sources-2 item 003) in full; markets (136) in passages; the compare-plans entry Customer Location (185); get-manager-profile's checkout_page_options.geolocation_service; llms.txt's line on the popup.

#### What was found, by group

- **Domain (S02-VP-45, S02-VP-46):** S02-ZD-227 to S02-ZD-246, citations S02-ZD-C377 to S02-ZD-C408, eight terms.
  - The domain article (قائمة النطاقات): the domain is the online store's address (S02-ZD-227), reached at الإعدادات > رابط المتجر الألكتروني (S02-ZD-228); the merchant links a custom domain and changes its name servers (S02-ZD-229, S02-ZD-230); لا يمكن تفعيل أكثر من نطاق في نفس الوقت (S02-ZD-231, f;g); the default domain can be activated at any time (S02-ZD-232); a free domain request is reviewed by the team, one per store, on Growth and Professional (S02-ZD-233, S02-ZD-234, S02-ZD-238); a domain ending in sa is booked by the merchant (S02-ZD-235); renewal and change (S02-ZD-236, S02-ZD-237).
  - The Terms' أسماء النطاقات (رابط المتجر): subdomains under zid.store (S02-ZD-239); the merchant answers for purchasing, activating and deactivating the domain (S02-ZD-240).
  - The permission manage.store.custom.domain (S02-ZD-241); plans: compare-plans Custom Domain Linking (S02-ZD-242) and the store_domain.* policies of the profile's 200 example (S02-ZD-243).
  - Live: the FAQ on changing the store's link (S02-ZD-244); buy-new-domain (S02-ZD-245). The sign-up articles for Saudi and Gulf users give the same words on the store's link (S02-ZD-246).
  - No gap recorded. None of the pages names a market.
- **Checkout and customer accounts (S02-VP-55, S02-VP-56):** S02-ZD-247 to S02-ZD-257, citations S02-ZD-C409 to S02-ZD-C430, three terms.
  - checkout-page-options: the merchant controls the payment settings (S02-ZD-247); login by SMS, e-mail and WhatsApp (S02-ZD-248 to S02-ZD-250); the login pop-up, on by default (S02-ZD-251); guest checkout and its payment methods (S02-ZD-252); one-page checkout (S02-ZD-253); changing the customer type to a company, on the Professional plan (S02-ZD-254, S02-ZD-255). Plans of e-mail login and single-page checkout in the profile's 200 example (S02-ZD-256).
  - The lead (S02-ZD-257): customers outside Saudi Arabia can complete electronic payment according to the activated networks and currencies, when Zid Pay is activated. Its id is added to the conditions of S02-ZD-130 (Zid Payments gateway) and S02-ZD-071 (the networks activated in Zid Pay).
  - Gap S02-ZD-G10 (S02-VP-55, searched, not found): whether the checkout page options take a value per market or per buyer's country.
- **Language (S02-VP-44):** S02-ZD-258 to S02-ZD-265, citations S02-ZD-C431 to S02-ZD-C442, four terms.
  - store-language: the merchant activates English at الاعدادات > اللغات والعملات (S02-ZD-258); activating a language is not an automatic translation (S02-ZD-259); the article lists تحديد اللغة الأساسية للمتجر among what it teaches (S02-ZD-260).
  - Localization's language and languages (S02-ZD-261, S02-ZD-262); the popup's zid.store.region.languages (S02-ZD-263); store_language_and_currencies.languages on Rise in the profile's 200 example (S02-ZD-264); compare-plans Message Language on Growth and Pro (S02-ZD-265).
  - Recorded before and bearing on this point: S02-ZD-187 and S02-ZD-191 (customers change the store language), S02-ZD-014, S02-ZD-016, S02-ZD-214, S02-ZD-221.
  - No gap recorded.
- **Contact information shown to buyers (S02-VP-68, S02-VP-79):** S02-ZD-266 to S02-ZD-268, citations S02-ZD-C443 to S02-ZD-C445, two terms.
  - store-info-ksa: the merchant edits the basic information shown to customers (S02-ZD-266); the e-mail, phone and commercial registration number show at the bottom of the store page (S02-ZD-267). saudi-merchants: بيانات التواصل under موثوقية المتجر (S02-ZD-268); gcc-merchants names موثوقية المتجر and gives no lines under it.
  - Recorded before: S02-ZD-206 (the Terms: every store discloses its official contact means), S02-ZD-032 (the Store API's phone and e-mail). S02-ZD-282 (Jahez: each branch's phone number), recorded for S02-VP-78, bears on S02-VP-68 too.
  - Gap S02-ZD-G11 (S02-VP-68, searched, not found): whether the contact details take a value per market.
- **Locations (S02-VP-67, S02-VP-78):** S02-ZD-269 to S02-ZD-287, citations S02-ZD-C446 to S02-ZD-C473, five terms.
  - withdrawal-priority: the path, the order of the warehouses set by the merchant, and the plans (S02-ZD-269 to S02-ZD-271).
  - shipping-adress: warehouse management, the number of warehouses by plan, the default warehouse, and choosing the warehouse when an order turns ready (S02-ZD-272 to S02-ZD-275).
  - Live: create-inventory-address (S02-ZD-276), inventory-transfer (S02-ZD-277 to S02-ZD-279), the FAQ on branch inventory with Zid Cashier (S02-ZD-280).
  - checkout-page-options: pickup from a branch's inventory (S02-ZD-281); jahez: each branch's phone and working hours (S02-ZD-282); national-address: the warehouses inside Saudi Arabia take the short national address (S02-ZD-283).
  - The API: a location's fulfillment_priority (S02-ZD-284) and an order's fulfillment location(s) (S02-ZD-285); compare-plans: Inventory Withdrawal Priority and Transfer Inventory Between Branches (S02-ZD-286, S02-ZD-287).
  - Gap S02-ZD-G12 (S02-VP-67, searched, not found): whether the withdrawal priority takes a value per market, channel or city.
- **Market selection (S02-VP-73, S02-VP-74):** S02-ZD-288 to S02-ZD-292, citations S02-ZD-C474 to S02-ZD-C478, two terms.
  - The Region & Language popup: Require customer to select city manually, or a default city (S02-ZD-288); the countries API depends on the merchant's switch (S02-ZD-289); setRegion (S02-ZD-290); the popup is turned on in the theme (S02-ZD-291). Compare-plans Customer Location (S02-ZD-292).
  - Recorded before: S02-ZD-024 (the customer sees the market's customization according to their country), S02-ZD-051, S02-ZD-187 to S02-ZD-191.
  - Gap S02-ZD-G13 (S02-VP-73 and S02-VP-74, searched, not found): how a customer's market is found and who sets it.
- **The (h) exception:** S02-ZD-130 (Rise, Zid Payments gateway) and S02-ZD-071 (activating the networks in Zid Pay; كي نت for establishments and companies only) now also name S02-ZD-257 in `conditions`.

#### Searches, and how they were narrowed

- Each group's two searches were run with `--max 100`; none passed it (the largest listed 71 documents, the first search on language). No search was narrowed by its terms.
- Documents listed but not read are named in each point's `read` in `a2.tsv`, by their matches: the Accept-Language header and names per language in the API pages, فرع inside other words (الفرعي, فرعية), Zid's own support and contact pages, and customers' or consignees' contact details and countries.

#### The lead

- The FAQ هل يستطيع العملاء من خارج السعودية إتمام عملية الدفع الإلكتروني في حال تفعيل زد باي ؟ (item 4) answers S02-VP-55: recorded as S02-ZD-257 and named in that point's `a2.tsv` row. No gap of zid is routed to a capture request.

#### Problems with the method

- The live pages' quotes were tested against working copies with `method/quote_check.py`'s own `variants` and `html_text`, through a helper in the scratch folder, as ZD-1 did; the checker shows them as pending capture.
- The help centre's category page الإعدادات > التواصل renders no article list in its text; its articles were found through the sitemaps instead.
- The gaps S02-ZD-G10 to S02-ZD-G12 each name a setting that the pages read state with no market named; their kind, `searched, not found`, records that no page read states its value per market. S02-ZD-G13 records that no page read states how a customer's market is found.
- The repository's HEAD moved during the run (the coordinator's checkpoints); held paths are cited at 00a87e3aa35463857a13342705714e963399a5c5.

#### Check on a copy

`python3 -I method/check_subject.py` on a copy at /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a2-zd-2/check/S-02, output in /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a2-zd-2/check/out (2026-10-27): no line of level error; 292 statements; 469 quotes found and 9 unresolved; 17 lines of level pending capture, the live citations S02-ZD-C404, S02-ZD-C405, S02-ZD-C430 and S02-ZD-C457 to S02-ZD-C462 and the statements S02-ZD-244, S02-ZD-245, S02-ZD-257 and S02-ZD-276 to S02-ZD-280 that cite them.

### ZD-3: S02-VP-71, S02-VP-72, S02-VP-75, S02-VP-77, S02-VP-80, S02-VP-81, S02-VP-84 and S02-VP-86 to S02-VP-90, and the lead (2026-10-27)

Read under `studies/subjects/S-02/briefs/A2-close-gaps.md`, with the coordinator's change to "Reading a live page" (a raw file is quoted only for what the rendered page shows) and the rendered copies of run 20261027T112044Z-zid-rerender preferred. Zid's twelve rows under these points in `variants.tsv` (S02-V-795, S02-V-796, S02-V-799, S02-V-801, S02-V-804, S02-V-805, S02-V-808, S02-V-875, S02-V-879, S02-V-883, S02-V-887, S02-V-891) were all `not covered`, so all twelve were taken. One lead was named: Zid's pricing pages, held with their text in run 20261027T111455Z-s02-a2-sources-batch-1 (items 006 to 008). Earlier parts: ZD-1, ZD-2; later parts: none. Each point's row is in `a2.tsv`, with the searches and documents in `read`.

#### Documents read, in order (2026-10-27)

Item numbers are those of 20261012T045101Z-q1-zid-sources unless another run is named. Live pages were checked with `method/held_index.py` first (none held) and rendered through `method/capture/page_text.mjs`.
1. Analytics and tracking. Live, found in the help centre's post-sitemap1.xml (ZD-1's decoded copy): https://help.zid.sa/google-analytics/ (August 13, 2026), https://help.zid.sa/facebook-pixel/ (August 17, 2026), https://help.zid.sa/tiktok-pixel-tiktok-conversion-api/ (August 17, 2026) and https://help.zid.sa/google-tag-manager/ (August 13, 2026), in full. The category page أدوات التتبع (https://help.zid.sa/category/%d8%aa%d8%b5%d9%85%d9%8a%d9%85-%d8%a7%d9%84%d9%85%d8%aa%d8%ac%d8%b1/tracking-tool/) rendered with no article list in its text. Held, in passages: dashboard-analytics (108; no market, country or currency named), the compare-plans data (185; its analytics and reports entries).
2. Apps. Live: https://help.zid.sa/apps/ (August 17, 2026) and four FAQs found in faqs-sitemap.xml, each last updated July 23, 2023: كم عدد التطبيقات التي استطيع ربطها بمتجري؟, كيف استطيع تفعيل التطبيق على متجري؟, ماهو سوق تطبيقات زد؟ and ما هي التطبيقات المتاحة في سوق التطبيقات؟, in full. Held, in passages: Zid Apps Overview (072), the App activation and OAuth policy (071), create-first-app (018; not recorded), and the Terms' section سوق تطبيقات زد / Zid App Market in the rendered copies (20261027T112044Z-zid-rerender items 003 and 010).
3. Notifications to the merchant. Live, found in post-sitemap2.xml and post-sitemap1.xml: https://help.zid.sa/team-notification/ (اشعارات الفريق, August 3, 2026) and https://help.zid.sa/app-notifications-2/ (August 13, 2026: notifications to the users of the store's mobile app, not recorded), in full. Held: zid-reminder (180, تنبيهات زد: WhatsApp messages to customers with abandoned carts, not recorded), in full; the compare-plans entry Team Notifications (185); the docs' User Roles and Permissions (003), in full.
4. Staff access. Held (`method/held_index.py` found both after they had been rendered live; the held copies were read and cited): team-member (164, فريق العمل, August 3, 2026) and zidpay_staff_and_currencies (184, August 6, 2026), in full; User Roles and Permissions (003), in full; the compare-plans entry Add Team Members (185).
5. Privacy and consent. Held rendered (20261027T112044Z-zid-rerender): the Privacy Policy in English (item 009), in passages (cookies, consent, Merchants, Customers, countries), and the English Terms (item 010), in passages (privacy, consent). Live: https://help.zid.sa/whatsapp-opt-out/ (إلغاء الاشتراك من الرسائل, October 21, 2026), in full, and the FAQ ماهي سياسة الخصوصية والأمان في زد؟ (September 24, 2026; a link to the Privacy Policy, not recorded), both found in the help centre's sitemaps. legal-pages (133) was recorded by ZD-1 (S02-ZD-212 to S02-ZD-218) and not read again.
6. Store status. Held: working-hours (173, اوقات العمل الرسمية, August 5, 2026), in full; the Terms' ضوابط المتجر الإلكتروني in the rendered copies (20261027T112044Z-zid-rerender items 003 and 010), in passages (الصيانة, إغلاق المتجر; maintenance, closing the store); Store (060), in passages; the compare-plans data (185), in passages (no entry on working hours). The help centre's sitemaps list no other article whose slug names a store's closure or maintenance (two FAQs name disabling Zid Pay).
7. Units and time zone. Held, in passages: store-info-ksa (158; المنطقة الزمنية), Store (060; timezone), get-manager-profile (027; timezone, expiry_timezone), create-a-new-product (013; a product's weight, whose examples give unit kg, with no description of the unit), list-of-orders (039; ip_timezone), payment-constraints (144; the cart's weight, with no unit named).
8. The lead. Held rendered with their text in 20261027T111455Z-s02-a2-sources-batch-1: https://zid.sa/ar/pricing/ (item 006), https://zid.sa/en/pricing/ (item 007) and https://zid.eg/ar/pricing/ (item 008, باقات وأسعار زد مصر), in full. Their raw.html and rendered.html were searched for tax and price words (ضريب, VAT, tax, شامل, excl, incl, ريال, SAR, ج.م) and not quoted.

#### What was found, by group

- **Analytics and tracking (S02-VP-87, S02-VP-88):** S02-ZD-293 to S02-ZD-299, citations S02-ZD-C479 to S02-ZD-C487, one term (تتبع الحملات).
  - Google Analytics, Facebook pixel, TikTok Pixel and Google tag manager are apps under لوحة التحكم > سوق التطبيقات > تتبع الحملات (S02-ZD-293, S02-ZD-295 to S02-ZD-297); the merchant adds the account's identifier in each app's activation field (S02-ZD-294, S02-ZD-298).
  - The Google Analytics article's step for the account the merchant creates on Google's site: the site's name, time zone, country and currency (S02-ZD-299).
  - Gap S02-ZD-G14 (S02-VP-87, searched, not found): whether the identifiers take a value per market. S02-VP-88 is answered by the statements; no gap.
- **Apps (S02-VP-86):** S02-ZD-300 to S02-ZD-312, citations S02-ZD-C488 to S02-ZD-C501, five terms.
  - No set limit on the number of apps linked to a store (S02-ZD-300); تطبيقاتي lists the apps activated in the store (S02-ZD-301); embedded apps (S02-ZD-302); the App Market's apps come from third parties independent of Zid (S02-ZD-303), linked as each app's page says (S02-ZD-304), in nine categories (S02-ZD-305).
  - Zid Apps Overview: public apps for all merchants; private apps for stores granted access, on the Professional or Enterprise plan or with API Access (S02-ZD-306 to S02-ZD-308). The activation policy: Zid records the installation for the authorized store (S02-ZD-309); partners disclose eligibility and country prerequisites (S02-ZD-310, c;f).
  - The Terms' سوق تطبيقات زد: the platform's definition (S02-ZD-311) and the partner as the provider of the service (S02-ZD-312).
  - Gap S02-ZD-G15 (searched, not found): whether apps take a value per market.
- **Notifications to the merchant (S02-VP-89, S02-VP-90):** S02-ZD-313 to S02-ZD-318, citations S02-ZD-C502 to S02-ZD-C507, one term.
  - اشعارات الفريق: e-mail to the team on the order statuses chosen, at لوحة التحكم > الإعدادات > اشعارات الفريق, with the statuses and e-mail addresses the merchant sets (S02-ZD-313 to S02-ZD-316); by plan in the compare-plans data (S02-ZD-317, f;h); the permission manage.store.staff.notifications (S02-ZD-318).
  - Read and not recorded: app-notifications-2 and zid-reminder, whose messages go to customers.
  - Gap S02-ZD-G16 (S02-VP-89, searched, not found): whether team notifications take a value per market. S02-VP-90 is answered; no gap.
- **Staff access (S02-VP-71, S02-VP-72):** S02-ZD-318 to S02-ZD-333, citations S02-ZD-C507 to S02-ZD-C522, four terms; and from the lead S02-ZD-356 to S02-ZD-361.
  - فريق العمل at لوحة التحكم > الاعدادات > المتجر > فريق العمل: permissions per member or group (S02-ZD-319 to S02-ZD-322); the limits by plan and buying more members (S02-ZD-323, S02-ZD-324, S02-ZD-333, and the pricing pages' lines, S02-ZD-356 to S02-ZD-361); export limited to users with an e-mail on the store's domain (S02-ZD-325).
  - User Roles and Permissions: the store owner assigns permissions to staff (S02-ZD-326 to S02-ZD-328); the permission rows manage.store.settings and manage.app.market.settings (S02-ZD-329, S02-ZD-330).
  - Zid Pay's staff permissions (S02-ZD-331, S02-ZD-332).
  - Gap S02-ZD-G17 (S02-VP-71 and S02-VP-72, searched, not found): whether a permission can be limited to a market. The docs' List of Available Permissions holds no permission named for markets; it was not recorded as an absence, since its rows cannot be cited whole and no words present it as the full set other than its heading.
- **Privacy and consent (S02-VP-75, S02-VP-84):** S02-ZD-334 to S02-ZD-339, citations S02-ZD-C523 to S02-ZD-C528, one term.
  - The Privacy Policy, which the Terms incorporate: for a store's customers, Zid acts under the Merchant's direction and the Merchant's terms and privacy policy apply (S02-ZD-334); opting out of targeted advertising on the Merchant's site (S02-ZD-335); rights regardless of where you live (S02-ZD-336).
  - إلغاء الاشتراك من الرسائل: customers stop WhatsApp messages from the store themselves (S02-ZD-337), at الواتساب ← الإعدادات ← إلغاء الاشتراك من الرسائل (S02-ZD-338), with keywords set by the platform in Arabic and English that cannot be changed (S02-ZD-339).
  - Recorded before: the store's legal pages, سياسة الخصوصية among them (S02-ZD-212 to S02-ZD-218), and the Terms' clause on privacy policies (S02-ZD-219).
  - Gaps S02-ZD-G18 (S02-VP-75, searched, not found): whether the store's privacy policy or its customers' opt-outs take a value per market; S02-ZD-G19 (S02-VP-84, searched, not found): no page read names a cookie setting for a store.
- **Store status (S02-VP-80, S02-VP-81):** S02-ZD-340 to S02-ZD-345, citations S02-ZD-C529 to S02-ZD-C535, three terms.
  - أوقات العمل الرسمية at الاعدادات > المتجر: closing the store fully, stopping orders while customers browse, or ordering in set hours and days, set by the merchant, with a text in Arabic and English (S02-ZD-340 to S02-ZD-344).
  - The Terms' ضوابط المتجر الإلكتروني: Zid may suspend the service and close the store when the merchant does not comply (S02-ZD-345).
  - No page names maintenance (الصيانة) as a store setting; the Terms' matches are the maintenance of themes and point-of-sale devices.
  - Gap S02-ZD-G20 (S02-VP-80, searched, not found): whether the closure takes a value per market. S02-VP-81 is answered; no gap.
- **Units and time zone (S02-VP-77):** S02-ZD-346, citation S02-ZD-C536, one term (المنطقة الزمنية).
  - store-info-ksa: the merchant chooses the time zone for showing and exporting order times (S02-ZD-346). Recorded before: the Store API's timezone (S02-ZD-032).
  - Gap S02-ZD-G21 (searched, not found): whether the time zone or a unit takes a value per market; no page read names a store setting for units.
- **The (h) exception:** no existing (h) statement conditions an arrangement that the new (a) to (f) statements describe; no `conditions` was changed.

#### Searches, and how they were narrowed

- Each group's two searches were run with `--max 100`; none passed it (the largest listed 82 documents, the first search on store status, whose head word status matched the API pages' response status). No search was narrowed by its terms.
- Documents listed but not read are named in each point's `read` in `a2.tsv`, by their matches: order and shipment tracking, notifications and messages to customers, footers and menus of zid.sa and zid.eg pages, API fields named status, unit or timezone in other senses.

#### The lead

- The pricing pages, now held with their text (items 006 to 008 of 20261027T111455Z-s02-a2-sources-batch-1), were read in full and quoted from their rendered text only.
- The plans and their prices: zid.sa, البداية free, الانطلاقة 99 and النمو 299 ريال a month, الاحترافية on request (S02-ZD-347 to S02-ZD-349, S02-ZD-353; Starter, Rise, Growth, Pro on the English page); zid.eg (باقات وأسعار زد مصر), الانطلاقة 1,128 and 940 and النمو 3,408 and 2,840 ج.م a month, with 11,286 and 34,086 ج.م billed yearly (S02-ZD-350 to S02-ZD-353). They answer S02-VP-14 (the platform's fees), which gets a new `a2.tsv` row; each names S02-ZD-057 (fees in Saudi riyals or the merchant's local currency) in `conditions`.
- The taxes on Zid's fees: the pages name none, in their rendered text or their HTML; the footers name the company with registration and tax numbers that differ between zid.sa and zid.eg (S02-ZD-354, S02-ZD-355, c). They do not answer S02-VP-15: S02-ZD-G08 remains, and ZD-1's row for S02-VP-15 now names the pages in `read`.
- What each plan offers (h): the team members' lines (S02-ZD-356 to S02-ZD-361, added to the rows of S02-VP-71 and S02-VP-72); VAT calculation on النمو (S02-ZD-362, zid.sa); two currencies on النمو and several VAT configurations on الإحترافية (S02-ZD-363, S02-ZD-364, zid.eg); electronic payment on الانطلاقة (S02-ZD-365, zid.eg); inventory shown by customers' city on الإحترافية (S02-ZD-366, zid.sa, conditions S02-ZD-161). These and the footers are in the `a2.tsv` row `none`. Read and not recorded: the shipping rates by plan and the other feature lines, which name no market, country or setting of S-02's bullets.
- No gap of zid is routed to a capture request.

#### Problems with the method

- The coordinator's change to "Reading a live page" applied during the run: the pricing pages were quoted from their rendered text; the rendered copies of 20261027T112044Z-zid-rerender were used for the Terms and the Privacy Policy. S02-ZD-179 and S02-ZD-180 were not built on: the footers' statements name only what the footers show.
- Some searches held single generic words as terms (permissions, unit, cookie, status), which the brief puts after `--with`; they broadened the searches, and the documents they added were read or listed as not read.
- team-member and zidpay_staff_and_currencies were rendered live in the same command that found them held; the held copies (164, 184) were read and cited.
- The help centre's category page أدوات التتبع renders no article list in its text; the tracking articles were found through the sitemaps.
- The live pages' quotes were tested against working copies with `method/quote_check.py`'s own `variants` and `html_text`, through a helper in the scratch folder, as ZD-1 and ZD-2 did; the checker shows them as pending capture.
- The repository's HEAD moved during the run; held paths are cited at the commit at which they were read: d91058af4b50a75208df739741b1e9a86b605748 (analytics), 1b32e347f3cfe8a3f285e523ba3867aaf77726bd (apps to units), 42d054999c85b3fdd48b8ca32d10aef650a42fe4 (the lead).

#### Check on a copy

`python3 -I method/check_subject.py` on a copy at /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a2-zd-3/check/S-02, output in /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-a2-zd-3/check/out (2026-10-27): no line of level error; 366 statements, 21 gaps; 537 quotes found and 22 unresolved; 42 lines of level pending capture, the live citations S02-ZD-C479 to S02-ZD-C493, S02-ZD-C502 to S02-ZD-C505 and S02-ZD-C526 to S02-ZD-C528, and the statements S02-ZD-293 to S02-ZD-305, S02-ZD-313 to S02-ZD-316 and S02-ZD-337 to S02-ZD-339 that cite them.
