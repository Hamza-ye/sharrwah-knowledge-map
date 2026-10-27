Part RD1-1: bullets (a) and (d), for shopify, salla, zid, woocommerce, bigcommerce.

## Statements noted

### shopify (a)

- S02-SH-052 (a): names the store's home country, which the backup region is set to; not the field or record that holds it
- S02-SH-128 (a): its X is the primary market, 'the main country or region that you sell to', a market the store sells into; the store address appears only in its example
- S02-SH-138 (a): names the business entity associated with a market, with no country, address or jurisdiction
- S02-SH-143 (a): names the primary Shopify Payments account, 'associated with your store's home country'; not the field or record that holds that country
- S02-SH-193 (a): names the home country the domestic market and the backup region are created with; not the field or record that holds it
- S02-SH-230 (a): names where the store is based and the default country, prices and language taken from it; not the field or record that holds it
- S02-SH-259 (a): its words are the options of a list, 'Yemen' selected; they don't name the field or record that holds the store's own country
- S02-SH-260 (a): its words are a list of countries; they don't name the field or record that holds the store's own country
- S02-SH-263 (a): defines the business entity, 'the registered business, or the individual, that your store operates as'; names no country, address or jurisdiction
- S02-SH-285 (a): the CountryCode enum, 'The code designating a country/region'; names no field or record of the store
- S02-SH-316 (a): the store defaults name a business entity ('demo fake dev store - entity Business entity'), with no country, address or jurisdiction
- S02-SH-353 (a): the 'Country/region' and 'Residential address' of a person added to verify a Company entity ('Add person', 'Assign as account representative'); its words make them the person's, not the store's or its business's
- S02-SH-388 (a): admin controls of the store defaults naming a business entity ('capture advanced - entityBusiness entity'), with no country, address or jurisdiction
- S02-SH-389 (a): admin controls of the store defaults naming business entities, with no country, address or jurisdiction
- S02-SH-390 (a): admin controls of the store defaults naming business entities, with no country, address or jurisdiction
- S02-SH-396 (a): a dialog's controls, a button 'Yemen' and a combobox 'Select business type'; its words and scope don't say what the button holds
- S02-SH-406 (a): the markets graph's store defaults name a business entity, with no country, address or jurisdiction
- S02-SH-412 (a): 'There's no page at this address'; names no field or record
- S02-SH-414 (a): the markets graph's store defaults name a business entity, with no country, address or jurisdiction
- S02-SH-418 (a): the markets graph's store defaults name a business entity, with no country, address or jurisdiction
- S02-SH-420 (a): the markets graph's store defaults name a business entity, with no country, address or jurisdiction
- S02-SH-432 (a): the markets graph's store defaults name a business entity, with no country, address or jurisdiction
- S02-SH-435 (a): 'You need permission to view this feature'; names no field or record
- S02-SH-436 (a): 'This feature isn't currently available for your store'; names no field or record

### shopify (d)

- S02-SH-259 (d): its words are the options of a list, 'Yemen' selected; they don't say the countries are where Shopify serves merchants
- S02-SH-275 (d): names no country; says Shopify need not make any service or feature 'available in any jurisdiction'
- S02-SH-285 (d): the CountryCode enum, 'The code designating a country/region'; its words don't say where Shopify serves merchants
- S02-SH-289 (d): an error, 'Can't add unsupported country or region.'; names no country, and its words don't say where Shopify serves merchants

### salla (a)

- S02-SA-107 (a): the shipment pickup location ('موقع استلام الشحنات'), a place the store ships from
- S02-SA-108 (a): names 'تحديد الموقع' (my translation: setting the location) among the launch's basic requirements, without saying whose location it is
- S02-SA-236 (a): the country of a tax record (سجل ضريبي), which Salla's term 'السوق' ties to a market the store sells into ('وسيُستخدم هذا السجل الضريبي تلقائياً عند البيع فيها', terms.tsv); not the store's own country, by rule 1 as clarified at bc24532
- S02-SA-249 (a): its words name a 'country' and a 'city' without the record that holds them; phase A's identifier places them in 'default_branch'
- S02-SA-258 (a): 'موقع المتجر' here is added as the store's branches and warehouses and sets 'مصدر تجهيز الطلبات' (my translation: where orders are prepared): a place the store ships from
- S02-SA-305 (a): the branch's country, 'from which goods are stored and delivered to customers': a place the store keeps stock in and ships from
- S02-SA-306 (a): whether a branch is the default branch; names no country, and a branch is a place the store ships from

### salla (d)

- S02-SA-009 (d): names Salla's 'Primary markets', without saying they are where it serves merchants
- S02-SA-012 (d): names GCC expansion as 'the next priority'; its words don't say Salla serves merchants there

### zid (a)

- S02-ZD-001 (a): names the law that governs the terms, Saudi Arabia's; not the field or record that holds the store's own country
- S02-ZD-002 (a): names the law and courts of the Zid Pay contract; not the field or record that holds the store's own country
- S02-ZD-032 (a): the store's required fields name no country, address or location
- S02-ZD-033 (a): names the store's KYC and Commercial Registration details, with no country, address or jurisdiction
- S02-ZD-034 (a): the store business data's required fields name no country, address or jurisdiction
- S02-ZD-072 (a): an inventory location ('Inventories', 'Create Location'), a place the store keeps stock in
- S02-ZD-074 (a): a location's required fields, from the same page as S02-ZD-075's 'inventory location': a place the store keeps stock in
- S02-ZD-075 (a): 'the city where the new inventory location is based': a place the store keeps stock in
- S02-ZD-076 (a): whether 'this inventory location is the default one for the store': a place the store keeps stock in
- S02-ZD-077 (a): a location code 'for delivery and logistics purposes', from the same page as S02-ZD-075's 'inventory location': a place the store keeps stock in
- S02-ZD-148 (a): its words list address fields ('country', 'city', 'national_address_certificate', 'is_address_confirmed') without the record that holds them; phase A's identifier gives 'user.business_location'
- S02-ZD-149 (a): its words list a person's profile fields ('birth_date', 'country', 'job_title'), without saying whose, or that the country is where the store or its merchant is based
- S02-ZD-157 (a): the store's warehouses ('مخازنك'), places the store keeps stock in
- S02-ZD-158 (a): chooses a country and a city for the inventory addresses its article creates ('عناوين المخزون', S02-ZD-157's page): places the store keeps stock in
- S02-ZD-159 (a): a national address code for the inventory addresses its article creates ('عناوين المخزون', S02-ZD-157's page): places the store keeps stock in

### zid (d)

- S02-ZD-006 (d): a list of links to country pages, under 'Other countries'; its words don't say Zid serves merchants there
- S02-ZD-062 (d): Zid Egypt's commercial registration and tax ID; its words don't say Zid serves merchants in Egypt
- S02-ZD-063 (d): the same in Arabic ('تعمل زد مصر رسميًا تحت: رقم السجل التجاري'); its words don't say Zid serves merchants in Egypt
- S02-ZD-064 (d): 'Ensuring full compliance with Egyptian regulatory and taxation requirements'; names no country where Zid serves merchants

### woocommerce (a)

- S02-WC-014 (a): names the merchant's residence ('If you reside outside of the Designated Countries'), which the contracting entity follows; not the field or record that holds it (S02-V-044, gap S02-WC-G01)
- S02-WC-015 (a): names the merchant's residence ('If you reside in the Designated Countries'), which the contracting entity follows; not the field or record that holds it (S02-V-044, gap S02-WC-G01)
- S02-WC-016 (a): the label of the General settings tab; names no field or record that holds the store's own country
- S02-WC-100 (a): the REST route of the general settings; names no field or record that holds the store's own country
- S02-WC-123 (a): names a filter that changes 'the primary address sent to the tax service', without saying whose address or what record holds it
- S02-WC-169 (a): names the way to WooCommerce > Settings > General ('To edit these settings'), without a field that holds a country, address or location

### woocommerce (d)

- S02-WC-080 (d): reserves the right to restrict or block access, or to end the Agreement; names no country

### bigcommerce (a)

- S02-BC-053 (a): the shipping origin address, a place the store ships from
- S02-BC-103 (a): names a channel's overrides of the store profile settings; names no field that holds a country, address or location
- S02-BC-104 (a): names the Store Profile API ('Identifies and updates store profile'); names no field that holds a country, address or location
- S02-BC-105 (a): names the store/information/updated webhook; names no field that holds a country, address or location
- S02-BC-107 (a): where the store is hosted ('North America Europe Asia-Pacific'), outside X's role
- S02-BC-109 (a): a storefront's own localized country, 'the country that you are planning to sell to': a market the store sells into
- S02-BC-112 (a): a storefront's localized 'shopper-facing store name, address, email, and phone number', set per storefront: what a storefront shows buyers, not the store's own country
- S02-BC-151 (a): the Contracting Entity table's heading 'Country of Residence of Merchant'; names the merchant's residence, not the field or record that holds it

### bigcommerce (d)

- S02-BC-151 (d): the Contracting Entity table's heading row; names no country

## Searches for earlier platforms' rows

### S02-VP-03, raised by salla: shopify (d)

1. Printed the stmt_id and identifier of shopify's (d) statements: S02-SH-012 'restrictions that apply to all users', S02-SH-259 'combobox "I'm located in:"', S02-SH-273 'Unsupported countries and regions', S02-SH-274, S02-SH-275 '3. Shopify Rights', S02-SH-285 'CountryCode', S02-SH-289 'MarketUserErrorCode.UNSUPPORTED_COUNTRY_REGION'. None names where Shopify serves merchants.
2. Searched their statements, and notes-b.md's shopify (d) lines, for: available, support, serve, merchant, located, countries, متاح, مدعوم, Saudi, United Arab Emirates, Kuwait, Qatar.
3. Found: 'available' in S02-SH-275 (noted: names no country); 'support' and 'countries' in S02-SH-012, S02-SH-273, S02-SH-274 (S02-V-011, the countries kept out, under S02-VP-02) and S02-SH-289 (noted); the country names only in S02-SH-259 (noted: its words don't say the countries are where Shopify serves merchants).
4. Row: `not covered` (S02-V-026). Shopify has no gap under (d).

### S02-VP-01 and S02-VP-02, raised by shopify

Shopify is the first platform of this part, and no earlier part covered RD1, so no platform was placed before these points.

## `not covered` rows (for phase A2)

- S02-V-026: shopify, under S02-VP-03 (what countries fill where the platform serves merchants). Shopify's (d) statements name the countries it doesn't support (S02-V-011), and none it serves merchants in; its sign-up list (S02-SH-259) is noted, since its words don't say what the list is.
- S02-V-038: zid, under S02-VP-02 (what countries are kept out). Zid's (d) statements name the countries it serves merchants in, with 'فقط' (only, S02-ZD-007), and no country kept out; S02-ZD-N04 records the countries absent from that list (in S02-V-032's note).

## New kinds

None: this part's bullets, (a) and (d), have no kinds.

## Problems with the method

1. The brief's clarification of rule 1 at bc24532 (tax registration tied to a market): S02-SA-236 (the country of a Salla tax record, tied to markets by Salla's term 'السوق') is noted under (a). No other statement placed under (a) is a tax registration: S02-SA-277 (the company address on the tax invoice), S02-SH-203 (the legal business address that decides tax on Shopify's Managed Markets fee) and S02-WC-117, S02-WC-118 (the store address WooCommerce Tax uses as the primary tax location) are addresses, and their words tie them to no market.
2. Statements whose own words don't name the field or record, such as a list of options or an API field list, are placed only where their scope names it, or where they are read with a statement of the same source; otherwise they are noted (S02-SH-259 and S02-SH-260 under (a), S02-SH-259 under (d), S02-SH-396, S02-SA-249, S02-ZD-148, S02-ZD-149). The brief now lets the identifier or scope name X under (c) and (f); it doesn't say so for (a) and (d), so this part didn't use the identifier alone. If it may, these statements would be read again.
3. Rule 5's Lists asks for the same source and the same identifier. Zid's help articles give each step its own identifier under one heading, so these were read together as one passage of one source, where one identifier continues another's heading: S02-ZD-036 with S02-ZD-037 ('مرحلة التسجيل > ...'), S02-ZD-087, S02-ZD-088 and S02-ZD-089 ('تجهيز المتجر > ...'), S02-ZD-078 with S02-ZD-079 ('... > بيانات المتجر'), S02-ZD-083 with S02-ZD-084 ('العنوان التجاري > العنوان'). Also S02-ZD-138 with S02-ZD-140 (one page). Rule 5 may not mean this.
4. A `gap` row beside answer rows: woocommerce has answers under S02-VP-01 and also the gap S02-WC-G01, which asks where the merchant's residence named by the Terms is held; it has its own row (S02-V-044). BigCommerce's Terms name the merchant's residence too (S02-BC-151, noted), with no gap and no field or record stated; it has no such row. The brief doesn't say whether a gap row stands beside answers.
5. The `term` basis where one platform's terms.tsv entry has a definition and the other's has none (Salla's 'دولة المتجر' and WooCommerce's 'store country' against Shopify's 'store country'; BigCommerce's 'Store Address' against Shopify's 'store address'): taken to hold, since no two definitions differ. Where both are defined and differ ('store address', Shopify against WooCommerce), it is not claimed.
6. S02-ZD-N04 (an absence under (d)) is in the note of S02-V-032, not an `absent` row: Zid's fill point has answers, and an `absent` row under S02-VP-02 would read as no country kept out, while N04 records countries absent from the list of those served.
