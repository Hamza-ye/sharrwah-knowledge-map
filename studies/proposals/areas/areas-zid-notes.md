# zid: notes on the broad areas

## Under none

None. All 96 concerns in the extract are placed under one area each.

## Names that were hard to read

- **Zid Agent / خدمة وكيل زد (ZD-C-025).** Read the passage for ZD-S-0397 (zid.sa/ar/legal/terms-conditions/, a section heading): "خدمة وكيل زد (Zid Agent) آلية التنفيذ وحدود المسؤولية". It shows that this is a service Zid carries out under its terms, but not what the service does. Placed in ZD-A-26 with Zid's other services.
- **خدمة المميزات الإضافية VAS (ZD-C-026).** Read the passage for ZD-S-0404 (the same terms page, a section heading): "خدمة المميزات الإضافية VAS آلية التنفيذ وحدود المسؤولية". Again a service under Zid's terms; what it adds isn't said. Placed in ZD-A-26.
- **زد نمو (ZD-C-115).** Read the passage for ZD-S-0152 (help.zid.sa sidebar): only the heading "منتجات وخدمات زد ✨". The entries file later showed that the staff permissions `manage.store.ecosystem.*` (consulting, store preparation, designs, photography, printing, packaging, order fulfilment, payments, marketing, delivery, self-storage, co-working spaces) are tied to this concern, and the plain line for ZD-A-26 draws on those permission names from the extract.
- **Zid Voice (ZD-C-112).** Read the passage for ZD-S-0452 (zid.sa header menu Solutions): "Zid Voice Recover abandoned carts with a voice agent". Placed in ZD-A-16 with abandoned carts.
- **ZID Assurance (ZD-C-111).** Read the passage for ZD-S-0459 (zid.sa header menu Solutions): "ZID Assurance Boost your customers' trust and increase purchase rates". Given its own area, ZD-A-28.
- **الأسواق (ZD-C-034).** Read the passage for ZD-S-0125 (help.zid.sa settings › عام): only the article title "الأسواق ( لوحة التحكم الجديدة )". Its scopes are plans, not countries, so what it covers comes from the concern map's description alone. Placed with the countries in ZD-A-10, as the extract's nearest fit; this is the least certain placement.
- **طلبات التصدير (ZD-C-044).** Read the passage for ZD-S-0130 (help.zid.sa settings › عام): only the article title "طلبات التصدير ( لوحة التحكم الجديدة )". It doesn't settle whether this is data export from the dashboard or something else. Placed with the general settings in ZD-A-25.
- **خاصية الإهداء (ZD-C-101).** Read the passage for ZD-S-0131: only the article title. Placed with orders in ZD-A-15.
- **Group headings as names.** At first the checker didn't accept a list's group headings as names. After the coordinator's fix it accepts each part of an entry's path, so the headings now go under their lists' labels, and the `[term]` names given earlier are kept beside them:
  - `[plan-features]` headings: `Payments / الدفع` (ZD-A-02), `Shipping / الشحن` (ZD-A-13), `Product & Inventory Management / إدارة المنتجات والمخزون` (ZD-A-14), `Order Management / إدارة الطلبات` (ZD-A-15), `Marketing & Growth Tools / أدوات التسويق والنمو` (ZD-A-16), `Customer Management / إدارة العملاء` (ZD-A-17), `Reports & Analytics / التقارير والتحليلات` (ZD-A-18) and `Store Design / تصميم المتجر` (ZD-A-19).
  - `[settings]` headings: `التواصل` (ZD-A-24), and `عام` and `المتجر` (ZD-A-25).
  - Some of these headings hold entries that went to other areas by their concerns. Under `Payments / الدفع`, `Batch Print Shipping Papers` went to shipping and `Card Discount` to marketing. Under `عام` and `المتجر`, tax, languages and currencies, Markets, legal pages and business data have areas of their own. Each heading names the area that holds most of its entries.

## What the extract seemed to lack

- What Zid Agent, value added services (VAS) and the Markets setting (الأسواق) do. The cited passages are headings or titles only.
- The eligibility rules for each service by country. Scopes show that Zid Pay has separate Saudi and Kuwaiti terms (ZD-C-001 to ZD-C-009, ZD-C-037), that Zid Wallet differs for merchants outside Saudi Arabia (ZD-C-017), that Zid Financing is scoped to Saudi Arabia (ZD-C-023), and that the store business data setting is for Saudi merchants (ZD-C-035). There is no list of which services are available in which of the five countries (Egypt, UAE, Kuwait, Oman, Syria).
- The plan table itself. Plan names (Starter, Rise, Growth, Pro, Lite plan) appear as terms and plan cards, and many concerns are scoped to `compare-plans: starter, launch, growth, pro`, but the extract gives no single list of plans and what each costs.
- Six `plan-features` entries and two staff permissions are out of the concern map's scope (dashboard-wide search, bulk and filter tools; Zid Academy; the dashboard home). They have no concern, so they have no area.

## Entries

- `place_entries.py` placed 535 entries (the extract's 543 less the 8 out of scope), 0 under none, 14 split across areas.
- The splits are mostly broad API resources and scopes that touch several concerns: `Merchant APIs > Store Settings` (5 areas), `Merchant APIs > Account > Store` (3), `Merchant APIs > Orders`, `Merchant APIs > Reverse Orders` and `orders.read` (orders and tax, through credit notes), `account.read` and `third_store_details_read`. The general `Terms & Conditions / الشروط والأحكام` agreement splits across four areas (terms, subscriptions, payment methods, settings) because its concerns include subscriptions, cash on delivery, bank transfer and domains. Also split are `زد باي › المدفوعات` and `Various Payment Methods` (Zid Pay and store payment methods), `سوق التطبيقات › طرق الربط` (App Market and API connection), and `Request Inventory via POS` (inventory and POS). Each split follows the entry's own concerns, and none looks misplaced.
- ZD-A-21 (App Market) holds 58 entries, of which 34 are the App Market's own categories (the 35th, الشحن والتخزين, follows its concern to shipping, ZD-A-13). That fits its plain line: the categories describe the apps on offer, though the subjects they name (shipping, tax, marketing, CRM) also have areas of their own.
- ZD-A-26 holds 15 entries, 12 of them `manage.store.ecosystem.*` staff permissions tied to زد نمو; its plain line was written to match them.
- The other areas' entries fit their plain lines.

## Re-cut after the review

The coordinator re-cut these areas after the review of the areas list (`review.md`, findings 4 and 5), on 18 October 2026. Each area's note says why.
- ZD-A-10 keeps الأسواق (Markets).
- ZD-A-30 holds the store's languages and currencies (لغة وعملات المتجر), and ZD-A-31 the countries Zid serves, Zid Egypt, and the store's operating countries and cities.
- ZD-A-32 holds customer wallets (from ZD-A-16).
- The counts of areas and entries given above predate the re-cut. `areas-zid.tsv` and `areas-zid-entries.tsv` hold the current areas and placing.
