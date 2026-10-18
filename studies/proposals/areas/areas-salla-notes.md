# Salla's broad areas: notes

28 areas in `areas-salla.tsv`, from `extract-salla.md`. Every one of the 152 concerns is placed under an area.

## Under none

None. Every concern fits one area. Six concerns have no terms of their own in the extract (SA-C-101, SA-C-114, SA-C-164, SA-C-231, SA-C-233, SA-C-235), so they were placed by their description and scopes alone. See the last section.

## Names that were hard to read

- **Merchant ServicesEssentials, Salla PointFree Cashier, Store designMost Viewed, ProductsNew, Loyalty programNew, GiftingNew, My Opportunities NEW.** These are menu names with a badge's text joined on ("Essentials", "Free Cashier", "Most Viewed", "New"). They are copied exactly as the extract gives them, because the checker takes them only whole. I read them as "Merchant Services", "Salla Point" and so on. I settled this from the concerns' terms in the extract, without reading a source.
- **سوق الجملة (SA-C-098).** I read SA-S-2069 in `citations.tsv`. In the merchant plans list it is a sub-feature under the plan-feature group `knoat-albyaa` (قنوات البيع, sales channels). I also read SA-S-3553: its dashboard app (`@salla.sa/ui-merchant-vendors`) sits at the path `/channel/vendors`. So it is placed with Sales channels (SA-A-16). That grouping counts as the platform's own, and SA-A-16 now carries the heading قنوات البيع [plan-features] as a name. Who sells to whom there is still unclear. The permission names (`vendors_buy_products`, `vendors_manage_products`) suggest both buying and selling.
- **منصة الشكاوي (SA-C-178).** I read SA-S-2204. It is only a footer link's text on the plans page. Whose complaints it takes (customers' about stores, or merchants' about Salla) is still unclear. It is placed with the other published documents in SA-A-23.
- **https://salla.com/policies/nd96 (SA-C-180).** I read SA-S-2213. It is a sitemap entry only, and its content wasn't reached. It is placed in SA-A-23 because it is a policy page.
- **payments-operations (SA-C-123).** I read SA-S-3298. It is a feature flag with its plans only, which says nothing more about the concern's terms ("Transactions"). It is placed with the wallet and transactions (SA-A-18).
- **other:portal-countries (SA-C-166).** I read SA-S-2705. The list is the Partners portal's country picker, with a phone code for each country. That changed SA-A-22's plain line, which first named only the API's lists.
- **Store management [admin-navigation].** This is a Partners-portal menu entry, tied to SA-C-013 (partner and support access to a merchant's store). It is not the merchant's own store management. It is used in SA-A-01 with that meaning.

## What the extract seemed to lack

- **Menu headings.** The headings that group menus are out of the concern map's scope. That covers the dashboard's Store & Channels, Help Desk, Tools & Settings and Payment, the settings page's Account, Store, Operations and More, and the plan table's groups such as قنوات البيع and محفظة المتجر والفوترة. At first the checker didn't take them as names. After the coordinator's fix to the checker (18 October 2026), they now count as the platform's own names under their list's label, and the areas that follow them carry them.
  - The extract doesn't say which entries a heading holds. I read that from the order of the list: the inventory ids run in sequence, with a heading in each gap. For example, Help Desk is followed by Reviews & questions, Self-service system, Quality gateway, Salla Chat and Complaints. The plan table's محفظة المتجر والفوترة is followed by the store balance, billing settings and the e-payments log.
  - Four groupings now rest on such a heading and are marked "platform's own":
    - SA-A-08 (Help Desk);
    - SA-A-12 (Online Store, and تصميم المتجر);
    - SA-A-17 (الدفع);
    - SA-A-18 (محفظة المتجر والفوترة, and the Wallet page).
  - Headings were added as names, without changing the grouping, to:
    - SA-A-01 (Staff, Logs, موظفو المتجر);
    - SA-A-02 (Store Settings, دومين المتجر);
    - SA-A-05, SA-A-06, SA-A-07, SA-A-09, SA-A-19 and SA-A-28 (their dashboard and plan-table headings);
    - SA-A-13 (Storefront, Themes);
    - SA-A-15 (Salla Point);
    - SA-A-16 (قنوات البيع, Sales Channels);
    - SA-A-22 (مدعوم في:);
    - SA-A-25 (Merchant, Partner APIs, Dev Tools);
    - SA-A-26 (Affiliates, Influencer, Payments, Stores);
    - SA-A-27 (My Services).
  - Some headings span several areas, so I used them in none. They are the dashboard's Payment and Tools, the settings page's Account, Store, Operations and More, and the plan table's إدارة الحساب والمتجر, إدارة تجربة العميل and المزايا المتقدمة.
- **Concerns with no terms.** Six concerns have no terms: SA-C-101, SA-C-114, SA-C-164, SA-C-231, SA-C-233 and SA-C-235. SA-C-233 (where data is stored and processed) also has no statements. It is placed in SA-A-23 only because privacy and data belong with the published policies.
- **Plan table lines.** The extract says the plan comparison table's lines are not in the held page text. So which plan includes which feature shows only as scopes ("plans: plus, pro, special").
- **What differs by country.** This shows only as scopes, such as articles for Saudi Arabia, the UAE and Kuwait, and "countries: AE, SA, KW, QA, OM, BH". No list of Salla Payments' countries or of shipping by country is given. The only contracting entity named is شركة سلة القابضة / Salla Holding Company. Nothing says which company contracts in each country.
- **Help-centre categories with no subcategories.** Sales channels, Charity stores, Mahally, Support center and Shopper Help Hub each hold only "Home". So the help centre shows nothing inside them.
- **Charity stores.** The help centre gives them their own category. Charity also shows in `e-payment-charity`, `product-donation-options` and `quick-donation`, and as an App Maker scope. No concern covers charity stores as such. SA-C-127 (charity stores' payment gateways) is placed with payments in SA-A-17.
- **Special plan features.** The help centre's "Wholesale stores" and "Retail sales" under the Special plan have no concern of their own.

## Entries

`place_entries.py` placed 2,364 entries, with none under no area and 84 split across areas. The other 263 of the inventory's 2,627 entries are out of the concern map's scope. Most splits come from entries tied to two concerns:
- the App Store's country list (SA-C-167 with SA-C-194), split between SA-A-22 and SA-A-24;
- App Store categories that also name a store feature, split between SA-A-24 and SA-A-09, SA-A-19, SA-A-07 or SA-A-28;
- the API's resources and scopes, split between SA-A-25 and the area of the resource.

Two areas hold far more entries than their plain lines' weight would suggest:
- **SA-A-22 holds 254 entries.** 240 of them are countries in the Partners portal's country picker, which says little about where Salla operates.
- **SA-A-13 holds 235 entries.** Most are the storefront's web components and the e-commerce events in the developer documentation.

Every area's entries fit its plain line.

## Re-cut after the review

The coordinator re-cut these areas after the review of the areas list (`review.md`, findings 2 to 5 and 7), on 18 October 2026. Each area's note says why.
- SA-A-21 keeps Markets. SA-A-29 (Currencies) is split from it, and SA-A-30 (Languages) from SA-A-02.
- SA-A-31 holds Salla Payments (from SA-A-17), and SA-A-33 charity stores' payment gateways (from SA-A-17), under the help centre's 🤝 Charity stores.
- SA-A-32 holds financing (from SA-A-18).
- SA-A-34 holds the customer wallet (from SA-A-09).
