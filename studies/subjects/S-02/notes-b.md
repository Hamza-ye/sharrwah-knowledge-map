# RD1

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

Part RD1-2: bullet (b), for shopify, salla, zid, woocommerce, bigcommerce.

## Statements noted (part RD1-2)

### shopify (b)

- S02-SH-128 (b): its X is the primary market, 'the main country or region that you sell to', a market the store sells into
- S02-SH-129 (b): its X is the primary market ('Markets with subfolders configured'), a market the store sells into
- S02-SH-269 (b): the eligibility of the route settings:general ('PREFERENCES'); its words and identifier name no field or record that holds the store's country
- S02-SH-272 (b): its X is the store currency ('change your store currency after making your first sale'), not the store's own country
- S02-SH-326 (b): the identification number types offered ('Individual Taxpayer Identification Number', 'Passport Number'); names no party who sets, checks or changes the country, nor a condition on its change
- S02-SH-327 (b): a checkbox, 'This business has an EIN from the IRS'; names no party who sets, checks or changes the country, nor a condition on its change
- S02-SH-334 (b): archiving the store's entity ('Are you sure you want to archive this legal entity?'); names no party who sets, checks or changes its country, nor a condition on that change
- S02-SH-336 (b): a prompt on a person's name ('A person with this name already exists'); names no party who sets, checks or changes the country, nor a condition on its change
- S02-SH-353 (b): the 'Country/region' of a person added to verify the entity ('Add person'), the person's and not the store's or its business's, as under (a)
- S02-SH-354 (b): the identification number types for a person added to the entity ('Passport Number', 'National ID'); not the store's country
- S02-SH-383 (b): the gate of the business entities list route ('VIEW_LEGAL_ENTITIES'); names who may view the list, not who sets, checks or changes an entity's country
- S02-SH-396 (b): a form's controls, a button 'Yemen' and a combobox 'Select business type'; its words and identifier don't say what the button holds, as under (a)
- S02-SH-429 (b): archiving an entity ('Are you sure you want to archive this legal entity?'); names no party who sets, checks or changes its country, nor a condition on that change
- S02-SH-435 (b): a staff user ('role POS user administrator') is refused the organization details page ('You need permission to view this feature'): only a party kept out of who sets or changes the country, in S02-VP-04's and S02-VP-06's notes
- S02-SH-436 (b): the same staff user ('role POS user administrator') meets 'This feature isn't currently available for your store' on the route that creates business details: only a party kept out, in S02-VP-04's and S02-VP-06's notes
- S02-SH-441 (b): the business types for a country code ('legalEntityTypesByCountryCode'); names no party who sets, checks or changes the country, nor a condition on its change
- S02-SH-447 (b): the entity's fields and their requirements, its country code among them ('"field":"legalEntity.countryCode"'); names no party, and ties no condition to a change of the country
- S02-SH-448 (b): the entity's fields and their requirements for a Yemeni company, its country code among them ('"field":"legalEntity.countryCode"'); names no party, and ties no condition to a change of the country
- S02-SH-449 (b): a save refused for want of an account representative ('Legal entity must have exactly one account representative.'); its words tie no condition to a change of the country
- S02-SH-451 (b): whether the entity can be archived ('"archivable":false'); names no party who sets, checks or changes its country, nor a condition on that change
- S02-SH-452 (b): the store's primary entity and the entities assignable to it ('primaryLegalEntity', 'assignableLegalEntities'); names no party who sets, checks or changes the country, nor a condition on its change
- S02-SH-574 (b): the location of 'the people associated with the business' ('where they're located'), theirs and not the store's or its business's

### salla (b)

- S02-SA-107 (b): the shipments' pickup location ('موقع استلام الشحنات'; my translation: the shipments' pickup location), a place the store ships from, as under (a)
- S02-SA-210 (b): says only that Salla may refuse a store's registration ('الحق في رفض تسجيل أي متجر الكتروني'; my translation: the right to refuse registering any online store), without a check of a field or record that holds the store's country; not who sets, checks or changes it
- S02-SA-258 (b): 'موقع المتجر' here is added as branches and warehouses ('أضف موقع المتجر من خلال إضافة فروع ومستودعات المتجر'; my translation: add the store's location by adding the store's branches and warehouses): a place the store ships from, as under (a)

### zid (b)

- S02-ZD-073 (b): a staff permission for inventory locations ('Manage inventory locations'), places the store keeps stock in
- S02-ZD-148 (b): lists the business location's fields ('country', 'is_address_confirmed'), without naming who sets, checks or changes them, or a condition on their change
- S02-ZD-158 (b): the inventory addresses' country and city ('قم باختيار الدولة والمدينة'; my translation: choose the country and the city), places the store keeps stock in, as under (a)

### woocommerce (b)

- S02-WC-123 (b): names who may change 'the primary address sent to the tax service' ('Developers', by a filter), without saying whose address it is, as under (a)
- S02-WC-126 (b): the base country is returned through a filter ('woocommerce_countries_base_country'); its words name no party who sets, checks or changes it
- S02-WC-169 (b): names where the general settings are edited ('To edit these settings, go to WooCommerce > Settings > General in your WordPress dashboard'), without naming the store's address or country among them, as under (a)
- S02-WC-187 (b): names 'account information' as not always changeable once saved, without naming the account's country among it
- S02-WC-188 (b): says 'Most of the KYC information' can be changed via the Stripe dashboard, without a check, and without saying the country is among it (S02-WC-182 says the account's country 'cannot be changed later')
- S02-WC-189 (b): says 'certain account information' is updated only in the Stripe Express dashboard, without a check, and without naming the country among it
- S02-WC-223 (b): the function that sets the business location country ('Set the business location country for the Payments settings.'), without naming who calls it

### bigcommerce (b)

- S02-BC-100 (b): names only what is kept out of who changes the country ('cannot be modified with channel-specific overrides'), in S02-VP-06's note; that the setting holds for the whole store is the half under (g), RD3's
- S02-BC-107 (b): where the store is hosted ('Where should your store be hosted?'), outside X's role, as under (a)
- S02-BC-108 (b): the hosting region ('select the region nearest to your prospective customers'), outside X's role

## Searches for earlier platforms' rows (part RD1-2)

### S02-VP-04 to S02-VP-07, raised by shopify

Shopify is the first platform of this part, and no earlier part covered (b), so no platform was placed before these points. Each later platform's (b) statements were all read and placed under the four points, or noted, so no search for earlier rows was needed.

## `not covered` rows (part RD1-2, for phase A2)

None.

## New kinds (part RD1-2)

None: (b) has no kinds.

## Problems with the method (part RD1-2)

1. S02-VP-05's X, 'new information', is the only words of S02-SH-580, the point's first statement, that name what is checked; the business details it means are named only in its identifier, which the checker doesn't take for X's quote.
2. Readings under `who checks`: Salla's verification request and data (S02-SA-118, S02-SA-125, S02-SA-133, S02-SA-157), the Saudi Business Center's verification (S02-ZD-090) and the merchant's identity at WooCommerce (S02-WC-186) are read as checks of the business's registration or of the KYC information. Their words don't name the record, and each row marks the reading as mine.
3. S02-ZD-085 and S02-ZD-154 name the national address proof from SPL, which the seller uploads, but not who reviews it; SPL is the row's party, as the one the statements name.
4. Settings and permissions: S02-ZD-171's permission names the store settings, the same words in which S02-ZD-055 holds the merchant's country, so it is placed under S02-VP-06; S02-SH-269's route key, settings:general, names no field or record of (a), so it is noted.
5. S02-SH-116 is placed under S02-VP-04 as the platform's by 'automatically', which its words say of the markets created with the store, the domestic market being the store's home country. S02-WC-221's fallback to the base location's country, where the user set none, is taken as a default, though its words don't say 'by default'.
6. Feature gates: S02-SH-266's and S02-SH-382's centralLegalEntitiesEnabled is placed under S02-VP-07 as a condition; S02-SH-382 is under (h) too, where the later step reads it again.

## Changes after the coordinator's message at 7430da9 (part RD1-2)

1. The brief at 7430da9 clarified rule 4, 'Who sets, changes or checks it', on this part's first, second, third and fifth problems; it is applied below.
2. `who checks` (S02-VP-05), placed, with their notes removed: S02-SH-573 into S02-V-057; S02-SH-572 and S02-SH-582 as new rows; S02-SA-118, S02-SA-125, S02-SA-133 and S02-SA-157 as S02-V-073, which was `not covered`, and S02-SA-157's government bodies as a new row; S02-ZD-085 with S02-ZD-154, and S02-ZD-090, as new rows; S02-WC-186 as a new row. Still noted: S02-SA-210, a right to refuse without a check; S02-WC-188 and S02-WC-189, changes without a check and without the country.
3. `gap` rows kept beside the new answers, each asking for an answer they don't give: S02-V-058 (S02-SH-G01), S02-V-077 (S02-ZD-G02) and S02-V-084 (S02-WC-G02); under S02-VP-06, S02-V-074 (S02-SA-G01) and S02-V-090 (S02-BC-G02). Their notes say so.
4. `who changes` (S02-VP-06): the admin's Edit and Switch controls join S02-V-059 (S02-SH-330, S02-SH-333, S02-SH-335, S02-SH-337, S02-SH-338, S02-SH-347 to S02-SH-351, S02-SH-397, S02-SH-427, S02-SH-428, S02-SH-430, S02-SH-431, S02-SH-437, S02-SH-438, S02-SH-450, and the switch's S02-SH-261 and S02-SH-339 to S02-SH-343); the store's settings' controls join S02-V-078 (S02-ZD-083, S02-ZD-084) and S02-V-085 (S02-WC-017, S02-WC-113, S02-WC-170, S02-WC-221); new seller rows for Salla (S02-SA-179) and BigCommerce (S02-BC-110).
5. Unchanged, as the coordinator ruled: rows for permissions, roles and the account owner (S02-V-055, S02-V-060 to S02-V-063, S02-V-079), and S02-V-086, 'it cannot be changed later'.
6. Ids: the 39 earlier rows keep theirs; the new rows are S02-V-092 onward, at the end of variants.tsv. No `not covered` row is left.

Part RD1-3: bullet (c), for shopify and salla.

## Statements noted (part RD1-3)

### shopify (c)

- S02-SH-009 (c): names the contracting party for the Services' payment activities regulated under a Canadian Act ('solely with respect to any aspect of the Services that are payment activities regulated under the Canadian Retail Payment Activities Act'); its words name the Act's reach, not the store's country, as what decides it (in S02-VP-08's note)
- S02-SH-010 (c): names Shopify Inc. as billing agent 'in some jurisdictions, as applicable', without naming what decides which
- S02-SH-028 (c): an item of the supported countries for Shopify Payments with POS ('United States (Shopify Payments isn't available to US territories except Puerto Rico)'); its words and identifier don't say whose country decides it
- S02-SH-029 (c): names where Shopify Payments in France is offered ('available only in mainland France'), without saying whose country or address decides it
- S02-SH-267 (c): the validation schema's context, 'jurisdiction YE' (its scope), names a country without saying whose: a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-308 (c): observes a conversion fee on one market's currency ('Product pricing will include a 2% conversion rate fee paid by customers'), without naming what decides it
- S02-SH-354 (c): a person's identification number types; its scope gives both the entity's 'Country code Yemen' and 'the person's Country Yemen', and its words don't say which decides them
- S02-SH-361 (c): observes one new account's plan price at sign-up ('$27/mo + tax'), without naming what decides it
- S02-SH-363 (c): observes the plans and their prices for one store (its scope: its business entity in Yemen, the admin seen from the United Kingdom), without naming what decides them
- S02-SH-364 (c): observes the plans' prices in USD for the same store, without naming what decides them
- S02-SH-384 (c): a route for the payments settings of a business entity ('/payments/business-entities/:businessEntityId'); its words don't say which payment service or provider it holds
- S02-SH-441 (c): a call by country code, 'legalEntityTypesByCountryCode (countryCode YE)' (its identifier): a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-442 (c): a call by country code, 'governmentIdentifierTypesByCountryCode (countryCode YE, category BUSINESS)' (its identifier): a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-443 (c): a call by country code for a person, 'governmentIdentifierTypesByCountryCode (countryCode YE, category PERSONAL)' (its identifier): a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-444 (c): a call by country code, 'documentPurposeMetadataList (countryCode YE, entityType LEGAL_ENTITY)' (its identifier): a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-445 (c): a call by country code for a person, 'documentPurposeMetadataList (countryCode YE, entityType PERSON)' (its identifier): a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-446 (c): a call by country code, 'SupportingDocumentTypesQuery (countryCode YE, entityCategory BUSINESS)' (its identifier): a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-448 (c): the validation schema's context, 'jurisdiction YE' (its identifier), names a country without saying whose: a key whose words say country without saying whose fails the role test (rule 2)
- S02-SH-465 (c): a feature flag, 'threeDSecureEligibilityForCountry', whose words say country without saying whose: the role test fails (rule 2)
- S02-SH-496 (c): names domestic and international transactions, not the store's country, as what decides between Shopify Payments and Managed Markets (in S02-VP-11's note)
- S02-SH-543 (c): names fulfillment locations, places the store ships from, as what decides Managed Markets shipping (in S02-VP-17's note)
- S02-SH-578 (c): states the payout bank account's currency ('The bank account must be in EUR currency.'), without naming what decides it; its scope lists the countries whose pages it was recorded from

### salla (c)

- S02-SA-010 (c): a feature flag, 'kyc_new_workflow', with '"countries": ["AE", "SA", "KW", "QA", "OM", "BH"]': its words say countries without saying whose, so the role test fails (rule 2)
- S02-SA-016 (c): names a method coming soon, 'ستتوفر هذه الطريقة قريبًا في الإمارات' (my translation: this method will be available soon in the UAE); its words and scope don't say whose country
- S02-SA-019 (c): a related article's title, 'تحويلات مدفوعات سلة والتسويات في قطر' (my translation: Salla Payments' transfers and settlements in Qatar); names no decider
- S02-SA-111 (c): 'وضّح حالة متطلباتك النظامية للبيع في الإمارات' (my translation: state your regulatory requirements for selling in the UAE): its words don't say whether the UAE is the store's own country or a market it sells into; its scope is the Kuwait article
- S02-SA-112 (c): the same words, 'للبيع في الإمارات' (my translation: for selling in the UAE), in the UAE article: they don't say whether the UAE is the store's own country or a market it sells into
- S02-SA-181 (c): names what the e-commerce law requires of its practitioners ('إيضاح مقر العمل'; my translation: stating the place of business); its words name the law, not the store's country, as what decides it
- S02-SA-223 (c): a feature flag, 'shipping-tier-pricing-system', with '"countries": ["SA", "AE"]': its words say countries without saying whose, so the role test fails (rule 2)
- S02-SA-256 (c): the Salla Plus plan at 'AED 990 / year' on the UAE path of salla.com (its scope); its words don't name what decides the price, and the path is the site's, not a field or record of the store
- S02-SA-283 (c): ties cash on delivery to the market it is shown in ('Cash on Delivery can be shown only in Saudi Arabia and will be hidden in other markets automatically'), not to the store's own country; that half is RD3's (f) (in S02-VP-12's note)
- S02-SA-295 (c): names the store's verification, not its country, as what Salla Payments' activation follows ('يمكنك البدء بمجرد توثيق متجرك'; my translation: you can start once your store is verified); its scope is the Saudi path of salla.com

## Searches for earlier platforms' rows (part RD1-3)

### S02-VP-08 to S02-VP-18, raised by shopify

No earlier part covered (c), and Shopify is the first platform of this part, so no platform was placed before these points: no search was needed.

### Salla

Salla raised no point: each of its (c) statements was placed under one of Shopify's points, or noted. All of its (c) statements were read, so its two `not covered` rows rest on that reading. For them, its (c) statements were also searched for: ضريب, زكاة, VAT, tax, عملة, العملة, لغة, اللغة, currency, language, بالريال, الدرهم, الدينار, افتراضي, default. Found: S02-SA-127 and S02-SA-128 (VAT data and the TRN asked at a UAE store's verification, under S02-VP-10), S02-SA-244 (the Zakat and Tax Authority's app, under S02-VP-17), S02-SA-294 (VAT on subscriptions, under S02-VP-15), S02-SA-123 and S02-SA-130 (the bank account's currency, under S02-VP-13), S02-SA-208 (the fees in Saudi riyals, under S02-VP-14), and S02-SA-280 ('default template', a page's identifier, under S02-VP-17).

## `not covered` rows (part RD1-3, for phase A2)

- S02-V-164: salla, under S02-VP-16. Salla's (c) statements name no tax on a store's own sales by its country: the TRN asked of a UAE store at verification (S02-SA-128) is under S02-VP-10, the VAT on subscriptions (S02-SA-294) under S02-VP-15, and the Zakat and Tax Authority's app, a feature for stores in Saudi Arabia (S02-SA-244), under S02-VP-17.
- S02-V-168: salla, under S02-VP-18. Salla's (c) statements name no default the platform sets from the store's country, such as its currency or language: the fees' currency (S02-SA-208) and the bank accounts' (S02-SA-123, S02-SA-130) are under S02-VP-14 and S02-VP-13.

## New kinds (part RD1-3)

None: every thing bound is of one of rule 1's kinds under (c).

## Problems with the method (part RD1-3)

1. One answer per decider. Rule 4 makes two answers distinct when their excerpts name a different who or what. Each field or record that holds the store's own country (S02-VP-01's answers: the billing address, the store address, the business entity, the legal business's address, the home country) is its own answer, and so is each of Shopify's own terms for it (Designated Country, primary country, store country, which Shopify translates as it does shop country). Words that name only where someone is, with no field or record, are grouped by whose place they name: the store's ('stores based in', 'Store location', 'your store's location', 'stores in'), the business's ('your business is located in', 'businesses based in', 'where your business is based') or the merchant's ('merchants in', 'merchants located in', 'your location', 'your region', 'your country'); the residence ('resident', 'live in', 'residential address') and the business's registration ('registered in') are their own. Rule 0's sameness may be meant to split these further.
2. Reading by the same source. Several statements don't name their decider and are read with a statement of the same source, as RD1-2 did (its problem 3), though rule 5's Lists asks for the same identifier too: S02-SH-022 with S02-SH-021; S02-SH-024 with S02-SH-025; S02-SH-510 to S02-SH-516 and S02-SH-518 to S02-SH-524 with S02-SH-509 and S02-SH-517, whose pages are for 'stores based in' Canada and the United Kingdom; S02-SH-499 with S02-SH-502; S02-SH-534 to S02-SH-536 with S02-SH-533; and S02-SH-572 to S02-SH-574 with S02-SH-575 and S02-SH-577. Each row marks it as a reading. S02-SH-582 is read with S02-SH-581 under rule 5 itself (same source and identifier).
3. Keys by country code. Under the brief's line at 238b3c3 (a key whose words say country without saying whose fails the role test), the API calls 'ByCountryCode' and the validation schemas by 'jurisdiction' are noted (S02-SH-267, S02-SH-441 to S02-SH-446, S02-SH-448), though their scope names the store's business entity as the call's context. The admin forms that show the same fields under the entity's 'Country code' are placed (S02-VP-10).
4. 'every store'. Rule 4 asks for a statement that a thing is offered to every store whatever its country. A clause of the terms that names no country, address or entity as its condition (S02-SH-011, the governing law; S02-SH-276, the PayPal Express Checkout account) is read as one, marked as a reading. So are Salla's terms that name, with no condition, their company, Saudi Arabia's law and authorities, the fees' currency or the VAT on subscriptions (S02-SA-013, S02-SA-014, S02-SA-207, S02-SA-208, S02-SA-209, S02-SA-212, S02-SA-213, S02-SA-216, S02-SA-294), most of them read with S02-SA-214, of the same source, which says the agreement applies to all its users.
5. Payment methods that aren't providers. Cash on delivery, bank transfer and Google Pay (S02-SA-017, S02-SA-158, S02-SA-170, S02-SA-265) are placed under 'other payment providers' (S02-VP-12), as the store's payment options beside the platform's own service; rule 1's kinds under (c) have no kind for payment methods, which RD3's kinds under (f) have. Apple Pay and KNET are under the platform's own service (S02-VP-11), since Salla lists them under 'مدفوعات سلة' (S02-SA-137, S02-SA-138).
6. Salla's articles by country. Many of Salla's statements name the store's country only in their scope, the title of the article they come from, such as 'توثيق متجرك في الكويت' (my translation: verifying your store in Kuwait). They are placed where the title names the store ('متجرك'), and, for S02-SA-137 ('تفعيل مدفوعات سلة في الإمارات', activating Salla Payments in the UAE), as a marked reading. S02-SA-016, whose scope names only 'الإمارات', is noted; S02-SA-111, whose words name the UAE in the Kuwait article, and S02-SA-112 are noted, since 'للبيع في' (for selling in) may name a market.
7. Ids. The message said to continue from the earlier parts' last ids and named S02-VP-08 and S02-V-100; the folder's last ids were S02-VP-07 and S02-V-099, so this part's ids start at S02-VP-08 and S02-V-100.

Part RD1-4: bullet (c), for zid, woocommerce and bigcommerce.

## Statements noted (part RD1-4)

### zid (c)

- S02-ZD-008 (c): names where Zid Payments is available ('Currently in Saudi Arabia and Kuwait.'), without saying whose country decides it (in S02-V-177's note)
- S02-ZD-058 (c): names the transfer, within Saudi Arabia or to the Gulf states, as what decides the bank transfer fee on a refunded annual subscription ('9 ريالات للحوالات داخل السعودية و50 ريال لحوالات دول الخليج'), not the store's country (in S02-VP-14's note)
- S02-ZD-062 (c): Zid Egypt's commercial registration and tax ID; its words don't say the merchant contracts with Zid Egypt, or what decides it (S02-ZD-G03, S02-V-170)
- S02-ZD-063 (c): the same in Arabic ('تعمل زد مصر رسميًا تحت: رقم السجل التجاري'); its words don't say the merchant contracts with Zid Egypt, or what decides it
- S02-ZD-064 (c): 'Ensuring full compliance with Egyptian regulatory and taxation requirements'; names no thing bound to the store's country, nor what decides it
- S02-ZD-065 (c): names the banks Zid Pay supports ('زد باي تدعم جميع البنوك في السعودية'; my translation: Zid Pay supports all banks in Saudi Arabia), without naming what decides them
- S02-ZD-066 (c): names the banks of the list ('البنوك السعودية، بالإضافة إلى مجموعة من بنوك دول الخليج'; my translation: the Saudi banks, with a group of the Gulf states' banks), without naming what decides which a store can choose
- S02-ZD-067 (c): Zid Payments' networks ('K-Net, Apple Pay, Visa, American Express'); its words name no decider, and its scope, 'Kuwait', doesn't say whose country
- S02-ZD-082 (c): the business types the seller selects ('فرد، مؤسسة، شركة، جمعية خيرية'); names no decider of what is required, and its scope, 'السعودية', doesn't say whose country
- S02-ZD-112 (c): 'تتوفر حاليًا في المملكة العربية السعودية ودولة الكويت فقط' (my translation: currently available in Saudi Arabia and Kuwait only), as S02-ZD-008, without saying whose country; its identifier's headings, 'لنجومنا السعوديين; لطاقمنا الكويتي' (my translation: for our Saudi stars; for our Kuwaiti crew), don't say they are the merchants (in S02-V-177's note)
- S02-ZD-119 (c): names where Zid has Amazon ('حاليًا، لدينا أمازون في السعودية والإمارات'; my translation: currently we have Amazon in Saudi Arabia and the UAE), without saying whose country they are
- S02-ZD-122 (c): the e-payments' activation requirements follow the business's legal form ('حسب الكيان التجاري (فرد – شركة – مؤسسة)'), not the store's country; its scope names Saudi Arabia without saying whose country (in S02-VP-10's note)
- S02-ZD-123 (c): the same for Kuwait ('حسب الكيان التجاري (فرد – شركة )'), its scope naming Kuwait without saying whose country (in S02-VP-10's note)
- S02-ZD-154 (c): the documents of an individual ('متطلبات الأفراد'), under 'متطلبات تفعيل الدفع الالكتروني للسعودية', which names Saudi Arabia without saying whose country (in S02-VP-10's note)
- S02-ZD-155 (c): the documents to activate payments 'كـ فرد' (my translation: as an individual), its scope 'الكويت' naming Kuwait without saying whose country (in S02-VP-10's note)
- S02-ZD-156 (c): the documents of companies ('للشركات'), among them 'ترخيص الاستثمار (للشركات الأجنبية)' (my translation: an investment licence, for foreign companies); its words don't say what makes a company foreign, nor whose country decides them (in S02-VP-10's note)
- S02-ZD-167 (c): names who submits the sender name request ('سيتولى الفريق المختص من طرفهم برفع الطلب نيابةً عنكم'; my translation: the competent team will submit the request on your behalf) and the telecoms authority's requirements; names no decider

### woocommerce (c)

- S02-WC-001 (c): a code comment, 'The payment extension list for each country'; its words and identifier ('$country_extensions') say country without saying whose: the role test fails (rule 2)
- S02-WC-002 (c): 'Get the list of payment extensions details for a specific country'; its words say country without saying whose: the role test fails (rule 2)
- S02-WC-003 (c): 'The list of payment extensions (their full details) for the given country'; its words say country without saying whose: the role test fails (rule 2)
- S02-WC-006 (c): names how WooPayments' new countries are prioritized ('including the number of requests by WooCommerce store owners in that country'); not what decides the service for a store
- S02-WC-007 (c): '(Available in the U.S., U.K., Ireland, Australia, New Zealand, Canada, Spain, France, Germany, and Italy)' names where something is available, without saying whose country decides it
- S02-WC-012 (c): says WooPayments is being made available to other countries ('actively working to make WooPayments available to other countries'); names no decider
- S02-WC-048 (c): lists the countries both plugins support ('Both plugins support the following'), without saying whose country decides it
- S02-WC-049 (c): lists the countries the Stripe plugin also supports ('The Stripe plugin also supports these'), without saying whose country decides it
- S02-WC-050 (c): compares the instant payouts' countries ('Countries U.S. Australia, Canada, Singapore, UK, U.S.'), without saying whose country decides them
- S02-WC-056 (c): 'get_wcpay_countries()' returns a list of country codes; its words, identifier and scope say countries without saying whose: the role test fails (rule 2)
- S02-WC-061 (c): 'The order is important as it will be used to determine the priority of the suggestions'; names no decider tied to the store's country
- S02-WC-108 (c): 'WooPayments (Available in the U.S., U.K., Ireland, Australia, New Zealand, Canada, Spain, France, Germany, and Italy)' names where WooPayments is available, without saying whose country decides it
- S02-WC-109 (c): 'WooCommerce Shipping (U.S.-only)' names where it is offered, without saying whose country decides it

### bigcommerce (c)

- S02-BC-071 (c): names Commerce as agent of the Unified Billing Partners ('appointed Commerce as agent for the collection and disbursement of monies'); its scope, 'United States, United Kingdom, and Canada', doesn't say whose countries
- S02-BC-072 (c): the Unified Billing Apps' funds collected through Commerce's processor; its scope, 'India', doesn't say whose country
- S02-BC-085 (c): '*Pay Later is available in US, UK, DE, FR, IT, ES, AU', without saying whose country decides it
- S02-BC-086 (c): 'integrations with leading providers that power online payments in more than 150 countries'; names no decider
- S02-BC-087 (c): '65+ payment providers across 100+ countries'; names no decider
- S02-BC-094 (c): the countries the Stripe OCS integration supports ('Our integration supports the following countries'), without saying whose country decides it
- S02-BC-095 (c): the countries an integration supports ('Our integration supports the following countries'), without saying whose country decides it
- S02-BC-111 (c): 'The selected country determines tax and shipping zone settings'; its words and identifier say country without saying whose (rule 2); the country a storefront is localized to is a market the store sells into (S02-BC-109, noted under (a))
- S02-BC-129 (c): the tax zones apply by 'a customer’s billing address, shipping or pickup address, or your store’s shipping origin address': the buyer's addresses and a place the store ships from, outside the decider's role (in S02-VP-16's note)

## Searches for earlier platforms' rows (part RD1-4)

### S02-VP-08 to S02-VP-18, raised by shopify in part RD1-3

Zid's, WooCommerce's and BigCommerce's (c) statements were all read and placed under these points, or noted: no search was needed for them.

### S02-VP-19 (the store's data), raised by woocommerce: shopify, salla and zid (c)

Shopify and Salla were covered under (c) by part RD1-3, and Zid earlier in this part.
1. Printed their (c) statements' stmt_id and identifier, and read those naming data, privacy or personal information: S02-SH-354 ('Add personal information', a person's identification numbers), S02-SH-443 to S02-SH-445 (the API's identifier and document types by country code), S02-SA-114, S02-SA-115 (the store owner's data at verification), S02-SA-122, S02-SA-123, S02-SA-129, S02-SA-130 (the bank details) and S02-ZD-003 (the company's name, 'لتقنية المعلومات'). None names where the store's data is held, a privacy law that applies to it, or its controller.
2. Searched their (c) statements, and notes-b.md, for: privacy, personal information, personal data, information about you, your information, data, controller, processing, stored, data protection, GDPR, transfer, hosted, data center; الخصوصية, البيانات الشخصية, بياناتك, البيانات, بيانات, المعلومات, معلوماتك, سرية, معالجة, تخزين, حماية البيانات, نقل البيانات; and the point's x_words, 'personal information', 'the information about you that we process'.
3. Found and read: S02-SH-572 and S02-SH-573 ('information about you and your business', what the banking partners verify, under S02-VP-10); S02-SH-525 ('processing fee', a fee); S02-SA-013, S02-SA-014, S02-SA-207, S02-SA-215 ('تقنية المعلومات' in the companies' names); S02-SA-115, S02-SA-120, S02-SA-121, S02-SA-127 (verification data and documents, under S02-VP-10); S02-SA-209 ('وسياسة الخصوصية وسرية المعلومات المعمول بها لدى منصة سلة'; my translation: and the privacy and information-confidentiality policy in force at Salla), which binds the merchant to Salla's policy and Saudi Arabia's laws, under S02-VP-09, and says nothing of what decides the store's data; S02-SA-270 (shipping); and S02-ZD-004 ('the collection, processing, and use of your personal data by Al Qudrah Technical for Information and Communication Technology Company L.L.C'), which answers. notes-b.md: no match.
4. Rows: shopify `not covered` (S02-V-218); salla `not covered` (S02-V-219); zid S02-ZD-004, every store (S02-V-220). S02-ZD-004 was first placed under S02-VP-08 in this part, read as the company the merchant contracts with; it was moved to S02-VP-19, which its words answer, and taken out of S02-V-169 and S02-VP-08's x_words. Neither Shopify nor Salla has a gap under (c) that asks for it (Salla's S02-SA-G02 asks for the payment services contract's party).

## `not covered` rows (part RD1-4, for phase A2)

- S02-V-182: zid, under S02-VP-15 (taxes on the platform's fees). Zid's (c) statements name no tax on Zid's own fees: the VAT law in the Zid Pay terms (S02-ZD-069) is under S02-VP-09, the VAT certificate and settings (S02-ZD-097, S02-ZD-098, S02-ZD-100) under S02-VP-16.
- S02-V-194: woocommerce, under S02-VP-10 (documents and checks). No (c) statement names a document or check the merchant provides; the account types by country (S02-WC-011, S02-WC-055) are under S02-VP-11.
- S02-V-200: woocommerce, under S02-VP-12 (other payment providers). The payment extension suggestions by country (S02-WC-001 to S02-WC-003, S02-WC-061) and the Stripe extension's countries (S02-WC-048, S02-WC-049) are noted: their words don't say whose country.
- S02-V-218: shopify, under S02-VP-19 (the store's data), from the search.
- S02-V-219: salla, under S02-VP-19 (the store's data), from the search.
- S02-V-226: bigcommerce, under S02-VP-10 (documents and checks).
- S02-V-233: bigcommerce, under S02-VP-13 (payouts).
- S02-V-236: bigcommerce, under S02-VP-15 (taxes on the platform's fees).
- S02-V-237: bigcommerce, under S02-VP-16 (the store's taxes). The tax zones (S02-BC-129) are kept out, and S02-BC-111 ('The selected country') is noted.
- S02-V-239: bigcommerce, under S02-VP-18 (the store's defaults).
- S02-V-240: bigcommerce, under S02-VP-19 (the store's data).

## New kinds (part RD1-4)

None. S02-VP-19 is raised for a kind of rule 1's list, the store's data, which no earlier point held; it is not a new kind.

## Problems with the method (part RD1-4)

1. The store's data. S02-VP-19's X, 'personal information', is the merchant's personal information that the platform processes (S02-WC-073, S02-WC-084, S02-ZD-004); it is read as the store's data, rule 1's 'where it is held, and the privacy law that applies', with its controller among what is decided (a reading). S02-ZD-004 was placed under S02-VP-08 before the point was raised, and moved to it (the search under S02-VP-19).
2. Third parties of the platform's own payment service. Stripe's contracting entity by 'User's Stripe Account Country' (S02-WC-044) is under S02-VP-11, not S02-VP-08, since rule 1's contracting party is 'the platform's company'; Shopify's acquirer is under S02-VP-11 too (S02-V-111). Stripe's agreements and regional terms by the same country (S02-WC-043, S02-WC-045, S02-WC-046) are under S02-VP-09, read as 'which terms apply'. The 'Stripe Account Country' is read as the WooPayments account's country (S02-V-042), marked in each row.
3. Kinds read widely: the base country's tax label, address format, address locale and fields, and the article before a country's name (S02-WC-136 to S02-WC-139, S02-WC-141, S02-WC-145, S02-WC-154, S02-WC-155, S02-WC-158) are under the store's defaults (S02-VP-18), as what the platform sets from the store's country; the store address's shipping rates (S02-WC-090, S02-WC-170) are under other features and services (S02-VP-17), as a shipping service the store uses (a reading). Zid's wallet: its use (S02-ZD-121) and the wallet deduction feature (S02-ZD-113) are under S02-VP-17, a withdrawal from it (S02-ZD-114) under payouts (S02-VP-13), read as a payout. The sender name's documents (S02-ZD-163 to S02-ZD-166) are under documents and checks (S02-VP-10), read as documents that verify the business.
4. Countries named without whose. As part RD1-3 noted S02-SA-016, a statement whose words, identifier and scope name only a country is noted: S02-ZD-008, S02-ZD-067, S02-ZD-082, S02-ZD-112, S02-ZD-119, S02-WC-007, S02-WC-048 to S02-WC-050, S02-WC-108, S02-WC-109, S02-BC-071, S02-BC-072, S02-BC-085, S02-BC-094, S02-BC-095. Statements whose scope names the merchant or the store are placed: 'تجار السعودية', 'المتاجر السعودية', 'مستخدمي دول الخليج', 'التجار خارج المملكة', 'U.S. businesses', 'eligible US merchants', 'Customers domiciled in Germany'. Zid's e-payments requirements by section, 'للسعودية' and 'للكويت', name the business's legal form as what the documents follow, and are in S02-VP-10's note.
5. Readings by the same source, as parts RD1-2 and RD1-3 made them (marked in each row): S02-ZD-080 and S02-ZD-081 with S02-ZD-084; S02-ZD-039 and S02-ZD-040 with S02-ZD-035; S02-WC-033 with S02-WC-034; S02-WC-038 with S02-WC-039; S02-WC-066 with S02-WC-200; S02-WC-136 with S02-WC-137; S02-WC-190 with S02-WC-101; S02-WC-214 with S02-WC-064; S02-WC-215 with S02-WC-213; S02-BC-060, S02-BC-061 and S02-BC-152 with the Contracting Entity table (S02-BC-151, S02-BC-062 to S02-BC-066). Under rule 5's Lists (same source and identifier): S02-ZD-114 with S02-ZD-121; S02-WC-063 with S02-WC-034; S02-WC-071 with S02-WC-070; S02-WC-074 with S02-WC-073; S02-WC-102 with S02-WC-101; S02-WC-116 with S02-WC-115.
6. One answer per decider (part RD1-3's problem 1), applied: the merchant's place ('merchants in', 'US-based merchants', 'U.S. merchants', 'your country', 'customers' read as merchants), the business's ('a business must be located in', 'businesses based in', 'U.S. businesses'), the store's ('stores based in', 'stores located in', 'للمتاجر السعودية', 'US stores'), each record (the store address, the base country, the Business location, the account country, the store's country), and the residence, the domicile and the registration, each its own. BigCommerce's 'domiciled' (S02-BC-068 to S02-BC-070) is kept apart from its 'Country of Residence of Merchant', by their words. Zid's 'للتجار السعوديين والكويتيين' (S02-ZD-113) is read as the merchant's place, though it may name a nationality (marked).
7. 'every store' readings (part RD1-3's problem 4): Zid's terms, their company and Saudi Arabia's law (S02-ZD-001, S02-ZD-002, S02-ZD-003, S02-ZD-005, S02-ZD-069), and the privacy policy's company (S02-ZD-004); WooCommerce's governing law and venue (S02-WC-075, S02-WC-076). Mazeed (S02-ZD-115) says 'لجميع متاجر زد' (my translation: to all Zid stores) itself.
8. The `term` basis: claimed for 'Regional Terms' (S02-WC-045, S02-WC-046, against Shopify's S02-SH-031), which neither terms.tsv defines. Not claimed for WooCommerce's 'Designated Countries' (S02-WC-013 to S02-WC-015) against Shopify's 'Designated Country' (S02-SH-030): the words differ in number, and only WooCommerce's terms.tsv defines its term, as a list of countries. If rule 0's sameness covers a plural, the basis would hold, since no two definitions differ.
9. Absences under (c) (S02-ZD-N01 to S02-ZD-N03) are in the notes of the answer rows whose lists they bear on (S02-V-177, S02-V-185, S02-V-187), not `absent` rows, as part RD1-1 did with S02-ZD-N04.
10. Zid's gap S02-ZD-G03 gives a `gap` row under both S02-VP-08 and S02-VP-09 (S02-V-170, S02-V-173), beside the answer rows, as S02-V-148 does for Salla.
11. Ids: this part's rows are S02-V-169 to S02-V-240, and its point S02-VP-19. RD1 holds 19 points, under its cap of 25.

# RD2

## RD2-1: shopify, bullets (e) and (g)

RD2-1 raised S02-VP-26 to S02-VP-29, one point per question of (e) (rule 3), and wrote S02-V-400 to S02-V-430, all of them shopify's. The later part, RD2-2, gives the rows of salla, zid, woocommerce and bigcommerce.

### Statements noted under (e)

- S02-SH-038 (e): a link to the Markets admin page ('[**Markets**](https://admin.shopify.com/markets)'); answers none of (e)'s questions
- S02-SH-039 (e): the admin's navigation label 'Markets'; answers none of (e)'s questions
- S02-SH-040 (e): the API reference's navigation label 'Shopify Markets'; answers none of (e)'s questions
- S02-SH-041 (e): the admin route's path 'markets'; answers none of (e)'s questions
- S02-SH-042 (e): the markets route's eligibility, the permissions to view it ('VIEW_MARKETS'); it gates viewing a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-043 (e): an app access scope to read markets ('customer_read_markets'); answers none of (e)'s questions
- S02-SH-044, S02-SH-045, S02-SH-046 (e): webhook topics for a market's creation, deletion and update ('Occurs when a new market is created'); they name no party that creates, changes or removes a market, and a hook alone names no party (rule 4)
- S02-SH-047 (e): the access scope's name 'read_markets'; answers none of (e)'s questions
- S02-SH-048 (e): the webhook topic's value 'markets/create', in the platform's code; a hook alone names no party (rule 4), so it names no party that creates a market
- S02-SH-049 (e): a captured request with the variables '"action": "create", "type": "market"'; its words, identifier and scope name no party that creates a market
- S02-SH-050, S02-SH-051, S02-SH-052, S02-SH-053, S02-SH-054 (e): the backup region, which S02-SH-190 says 'isn't a market': X fails the role test (S02-VP-26's note)
- S02-SH-067, S02-SH-190, S02-SH-192, S02-SH-283, S02-SH-455 (e): the backup region, which S02-SH-190 says 'isn't a market': X fails the role test (S02-VP-26's note)
- S02-SH-063 (e): how a customer is matched to a market ('automatically match customers to the right market'), market selection, a setting under (f); answers none of (e)'s questions
- S02-SH-079 (e): how a customer's market is determined ('it's determined which market they belong to'), market selection; answers none of (e)'s questions
- S02-SH-120 (e): how a customer's market is determined ('Markets for a customer are automatically determined'), market selection; answers none of (e)'s questions
- S02-SH-122 (e): automatic redirection ('You can choose whether you want to automatically or manually localize your customers'), market selection; answers none of (e)'s questions
- S02-SH-123 (e): the market a shipping address gives at checkout ('A customer's shipping address determines the final experience they receive'), market selection; answers none of (e)'s questions
- S02-SH-229 (e): deep links ('You can create a parameter that sends customers to the correct country or region'), market selection; answers none of (e)'s questions
- S02-SH-553 (e): the markets a company location matches ('determined by the markets that they match'), market selection; answers none of (e)'s questions
- S02-SH-563 (e): the market associated with an order ('determined by the shipping address of the customer'), market selection; answers none of (e)'s questions
- S02-SH-093 (e): the permissions a staff member needs 'To access the Markets page'; it gates access to a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-127 (e): 'Deleting a market is permanent. Deleted markets can't be recovered': names no party that changes or removes a market
- S02-SH-196 (e): a link to the General settings page; answers none of (e)'s questions
- S02-SH-235 (e): 'Countries and regions can be added to your shipping zones in your Shipping and delivery settings only when those countries and regions belong to a market': a limit on shipping zones (shipping, under (f)), not on a market
- S02-SH-284 (e): 'marketCreate Creates a Market': the schema's mutation names no party that calls it, and sets no value or default (rule 4); the rest names a market's settings, under (f)
- S02-SH-302 (e): the Markets page's tree ('Store default', 'Regions'); states no definer, limit or party for a market
- S02-SH-306 (e): a market without shipping rates ('there are no shipping rates for this market'): checkout and shipping in a market, under (f); states no definer, limit or party for a market
- S02-SH-307 (e): a market's 'Parent market' ('Store default') and its links to shipping and customer privacy, under (f); states no definer, limit or party for a market
- S02-SH-362 (e): the setup task 'Review shipping rates' ('Look over the defaults set up for you based on your location'): shipping defaults, under (f); states no definer, limit or party for a market
- S02-SH-366, S02-SH-375 (e): the checkout's 'Country/Region' options (the buyer's address and checkout, under (f)); they state no definer, limit or party for a market
- S02-SH-377 (e): the markets using a domain, when a language is assigned to it ('Markets using this domain'): domain and language, under (f); states no definer, limit or party for a market
- S02-SH-378 (e): the permission gate on the Managed Markets route ('MANAGE_PAYMENTS_SETTINGS', 'markets/managed'); it gates a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-379 (e): the permission gate on the route 'markets/managed/deactivate', which deactivates Managed Markets, a setting of a market (S02-SH-488: 'deactivate Managed Markets for that market'), under (f); not a gate on creating, changing or removing a market
- S02-SH-380 (e): the gate on the route 'markets/shipping-option/update', a market's shipping option (shipping, under (f)); not a gate on creating, changing or removing a market
- S02-SH-434 (e): 'You need permission to view this feature': a staff account without access to the Markets page; it gates viewing a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-488 (e): 'deactivate Managed Markets for that market': Managed Markets is a setting of the market, under (f); states no definer, limit or party for a market
- S02-SH-319, S02-SH-332, S02-SH-345 (e): the store's defaults and its backup region ('Determines settings for customers outside of your markets'); state no definer, limit or party for a market, and S02-SH-190 says the backup region 'isn't a market'
- S02-SH-398 (e): the General settings page's controls, a link to Markets and the select 'Backup Region' ('currency.backupRegion'); states no definer, limit or party for a market
- S02-SH-399, S02-SH-400, S02-SH-401, S02-SH-402, S02-SH-403, S02-SH-404 (e): the store's business entity, address and defaults, and its backup region; they state no definer, limit or party for a market

### Statements noted under (g)

None of shopify's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, which is RD3's half: noted here (rule 4), and placed by RD3's parts.

- S02-SH-058 (g): 'Discounts and gift cards work across markets': a setting that holds for the whole store, RD3's half
- S02-SH-088 (g): 'Fixed amount discounts can be created only in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-089 (g): 'Staff permissions can't be assigned per market': a setting that holds for the whole store, RD3's half
- S02-SH-090 (g): 'Only one theme can be published at a time': a setting that holds for the whole store, RD3's half
- S02-SH-091 (g): 'Post-purchase apps work only in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-094 (g): 'customers in all markets pay in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-095 (g): 'On other plans, all markets share the same theme customization': a setting that holds for the whole store, RD3's half
- S02-SH-152 (g): 'You can add any product to a draft order regardless of market restrictions': a setting that holds for the whole store, RD3's half
- S02-SH-171 (g): 'Before you can assign a language to a market, the language must be added to your store': a setting that holds for the whole store, RD3's half
- S02-SH-186 (g): 'The following theme elements can't be customized for your markets on any plan': a setting that holds for the whole store, RD3's half
- S02-SH-187 (g): 'Homepage banners, announcement bars, and block content can't differ between markets on the Basic or Grow plans': a setting that holds for the whole store, RD3's half
- S02-SH-188 (g): 'By default, discount codes work across all markets': a setting that holds for the whole store, RD3's half
- S02-SH-189 (g): 'Gift cards are created and denominated in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-198 (g): 'A discount that applies to a customer segment or to specific customers applies to all markets': a setting that holds for the whole store, RD3's half
- S02-SH-227 (g): 'Because all markets use the same store URL, you can't customize which languages are available to each market': a setting that holds for the whole store, RD3's half
- S02-SH-231 (g): 'change your store's default language': a setting that holds for the whole store, RD3's half
- S02-SH-244 (g): 'Address validations at checkout ... apply to all regions': a setting that holds for the whole store, RD3's half
- S02-SH-246 (g): 'Store defaults: Manage your default currency, currency formatting, measurement and weight units, and time zone': settings that hold for the whole store, RD3's half
- S02-SH-272 (g): 'If you need to change your store currency after making your first sale, then contact Shopify Support': the store currency, a setting that holds for the whole store, RD3's half
- S02-SH-291 (g): 'The primary market must use the shop currency': the shop currency, a setting that holds for the whole store, RD3's half
- S02-SH-319, S02-SH-332, S02-SH-345 (g): the store's defaults ('Currency display To manage the currencies customers see, go to Markets'): settings that hold for the whole store, RD3's half
- S02-SH-398 (g): the store's defaults ('currency.unitSystem', 'currency.weightUnit', 'currency.timeZone'): settings that hold for the whole store, RD3's half
- S02-SH-399, S02-SH-400, S02-SH-401, S02-SH-402, S02-SH-403, S02-SH-404 (g): the store's defaults ('Currency display To manage the currencies customers see, go to Markets'): settings that hold for the whole store, RD3's half

### The brief's change on a platform's code (rule 4)

The coordinator's message during this run says the sentence on a platform's code applies to Shopify's shipped schema, under `who creates "market"` and `who changes or removes "market"`. Shopify's shipped statements under (e) were read again against it, and no row changed:

* placed under S02-VP-28 or S02-VP-29: S02-SH-278, whose words name the merchant ('A merchant-defined group of buyers'), the seller, in S02-V-425; S02-SH-288, whose words name the user and a permission ('The user doesn't have permission access to create or edit markets'), in S02-V-427 and S02-V-429; S02-SH-287, whose words say no one can ('Can’t delete, disable, or change the type of the last region market'), in S02-V-430; and the admin's controls S02-SH-386, S02-SH-387, S02-SH-391, S02-SH-392 and S02-SH-393, the seller's, in S02-V-425 and S02-V-428;
* noted: S02-SH-041, a route's path; S02-SH-042, a route's permissions to view it; S02-SH-048 and S02-SH-054, hooks, which alone name no party; S02-SH-283, the backup region's mutation; S02-SH-284, the mutation that creates a market, which names no party and sets no value or default; S02-SH-398, the General settings page's controls.

None of them sets a value or default for who creates, changes or removes a market. The suggested markets in S02-SH-387 are listed by the platform's code, but the seller creates each one, through its link (S02-V-425's note).

### New kinds

None: (e)'s points take no kind (rule 3).

### Searches for earlier platforms' rows

S02-VP-26, S02-VP-27, S02-VP-28 and S02-VP-29: no platform was placed under (e) before these points. RD2-1 is RD2's first part and shopify its first platform, so no search was made. Their rows for salla, zid, woocommerce and bigcommerce are RD2-2's.

### Rows `not covered`

None: shopify answers each of the four points.

### Problems with the method

- S02-VP-27, `what limits "market"`: bullet (e) asks how many markets a store can hold, while the question's form is wider. Its rows hold both: limits on the number (S02-V-411 to S02-V-414, S02-V-423 and the gap S02-V-424) and limits on what a market holds or when it can be active (S02-V-415 to S02-V-422). Rule 3 gives each question of (e) one point, so they share it.
- Permission gates. Rule 4 counts a permission that the statement says gates creating or changing a market. S02-SH-288 says so ('permission access to create or edit markets'), and is placed. S02-SH-042, S02-SH-093, S02-SH-378 and S02-SH-434 gate a page or route, and are noted. If access to the Markets page counts as gating creation, they belong in S02-V-427 and S02-V-429.
- S02-V-404 rests in part on a reading, marked in its basis_evidence: S02-SH-279's enum value 'LOCATION' is read as the retail (POS) location condition. The same API's Market object (S02-SH-278) names 'their region, retail location, or company location'.
- S02-V-407: the domestic market is defined by 'Your store's home country or region'. The point's X is the market, one of those the platform creates for the store to sell to (S02-SH-116), so it passes the role test. The variant names the store's own country as what defines it.
- S02-V-409 ('customer group', 'customer segments', from help pages) and the absent row S02-V-410 (S02-SH-N03: no condition type for a group of customers other than a company location) stand side by side, as their statements give them.

## RD2-2: salla, zid, woocommerce and bigcommerce, bullets (e) and (g)

RD2-2 places its platforms' statements under S02-VP-26 to S02-VP-29 and writes S02-V-431 onwards. It is RD2's last part.

### salla: statements noted under (e)

- S02-SA-001 (e): the label 'Market selection' ('"markets/browse_product_method":"Market selection"'); answers none of (e)'s questions
- S02-SA-002 (e): the label 'Markets' ('"markets":"Markets"'); answers none of (e)'s questions
- S02-SA-003 (e): the API docs' folder 'Store Scopes'; answers none of (e)'s questions
- S02-SA-007 (e): the API docs' folder 'Store Scopes'; answers none of (e)'s questions
- S02-SA-004 (e): the feature flag 'multi-market-origin-country-filter'; its words name a filter, and state no definer, limit or party for a market
- S02-SA-008 (e): 'This endpoint allows you to list store scopes for multi-country functionality.': an endpoint that lists store scopes; states no definer, limit or party for a market
- S02-SA-025 (e): each copy of the store 'تُدار بشكل مستقل' (my translation: is managed independently), with delivery from the branch nearest the customer: locations, under (f); names no party, and states no definer or limit for a market
- S02-SA-026 (e): the steps that activate the multiple markets feature ('اضغط (فعل الآن)', 'اضغط (تأكيد)'); the statement doesn't say they create, change or remove a market
- S02-SA-027 (e): the path to the multiple markets page; answers none of (e)'s questions
- S02-SA-028 (e): the multiple markets page's list of markets, with each market's information ('العملات', 'الفروع والمستودعات', 'الشحن', 'الدومين', 'تصميم المتجر'): a market's settings, under (f); states no definer, limit or party for a market
- S02-SA-029 (e): the tasks of managing multiple markets ('1- إضافة أسواق جديدة', '5- حذف السوق'); names no party that adds or deletes a market
- S02-SA-037 (e): the customer's country, shown in an order under the market's name; states no definer, limit or party for a market
- S02-SA-046 (e): searching the multiple markets page by a market's name or country ('يمكنك البحث باسم السوق أو دولته'); states no definer, limit or party for a market
- S02-SA-049 (e): languages per market ('ويمكنك تحديد اللغات لكل سوق إضافي بشكل مستقل'): language, under (f); states no definer, limit or party for a market
- S02-SA-054 (e): 'Contact your account manager to enable this feature.': who enables the feature; the statement doesn't say this creates a market
- S02-SA-055 (e): 'To disable it later, you'll need to contact your account manager.': who disables the feature; the statement doesn't say this changes or removes a market
- S02-SA-057 (e): 'Managing multiple branches/warehouses for my current market': locations, under (f); states no definer, limit or party for a market
- S02-SA-059 (e): 'Disabling can only be done by contacting the account manager': who disables the feature; the statement doesn't say this changes or removes a market
- S02-SA-065 (e): 'Run all your markets from one dashboard with independent settings for each market.': a market's settings, under (f); states no definer, limit or party for a market
- S02-SA-071 (e): 'Customers will be automatically redirected to their local market based on their IP address': market selection, under (f); answers none of (e)'s questions
- S02-SA-072 (e): 'Choose how customers select a market when visiting your store for the first time.': market selection, under (f); answers none of (e)'s questions
- S02-SA-073 (e): 'Set the market automatically using the customer’s IP address': market selection, under (f); answers none of (e)'s questions
- S02-SA-074 (e): 'Show customers a prompt to select their market before browsing the store.': market selection, under (f); answers none of (e)'s questions
- S02-SA-075 (e): 'Display a top bar where customers can switch markets.': market selection, under (f); answers none of (e)'s questions
- S02-SA-076 (e): 'Customers can only shop in the market that matches their country': market selection, under (f); answers none of (e)'s questions
- S02-SA-102 (e): redirection to a market's own domain ('ae.example.com'), an example: domain and market selection, under (f); answers none of (e)'s questions
- S02-SA-104 (e): restricting moves between markets ('يمنع التنقل'), an example with its reason: market selection, under (f); answers none of (e)'s questions
- S02-SA-106 (e): the customer selects the market to buy from ('يمكنه تحديد السوق الذي يرغب بالشراء منه'): market selection, under (f); answers none of (e)'s questions
- S02-SA-235 (e): the taxes page, for selling 'لأي دولة في العالم' (my translation: to any country in the world): taxes, under (f); states no definer, limit or party for a market
- S02-SA-250 (e): an endpoint that fetches 'the associated store scope details of a specific branch (scope)'; states no definer, limit or party for a market
- S02-SA-255 (e): the navigation item 'Multi Market', with '"permission": ["branches_management"]'; it gates a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SA-257 (e): the staff permission 'branches_management'; the statement doesn't say it gates creating, changing or removing a market
- S02-SA-278 (e): 'كل متجر يحدد الدول التي يشحن إليها' (my translation: each store sets the countries it ships to): shipping, under (f); states no definer, limit or party for a market
- S02-SA-286 (e): the label 'Country' ('"stores.country":"Country"'); answers none of (e)'s questions

### salla: statements noted under (g)

None of salla's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, or for every market, which is RD3's half.

- S02-SA-064 (g): 'Your whole store is in maintenance mode, which overrides this market's settings.': store status, a setting that holds for the whole store, RD3's half
- S02-SA-156 (g): 'ولا يمكن تخصيص ذلك لسوق معينة' (my translation: and this can't be customized for a given market), on removing a product's category: a setting that holds for the whole store, RD3's half
- S02-SA-168 (g): 'هذا الترتيب وأي تعديل عليه تلقائيًا على جميع الأسواق' (my translation, of the unified order: this order, and any change to it, automatically on all markets): a setting that holds for the whole store, RD3's half
- S02-SA-300 (g): '"Passing scope Id will make the products sort is per scope in this category, multi country feature needs to be enabled."': the products' order, a setting, RD3's half
- S02-SA-310 (g): 'it can be set as null or left blank to indicate that the tax rate is intended to apply to all countries': a tax rate for all countries, a setting that holds for the whole store, RD3's half

### zid: statements noted under (e)

- S02-ZD-009 (e): the path to the markets feature ('الاعدادات > الأسواق'); answers none of (e)'s questions
- S02-ZD-024 (e): the theme's customization shown to the customer 'على حسب دولته' (my translation: according to their country): storefront design and market selection, under (f); answers none of (e)'s questions
- S02-ZD-026 (e): 'Retrieve a list of countries where the store operates.': X fails the role test: the statement doesn't call these countries markets or places the store sells into, and rule 1 counts the store's country of operation as its own country
- S02-ZD-027 (e): the API scope 'countries_cities.read'; answers none of (e)'s questions
- S02-ZD-028 (e): 'Retrieve a list of countries where the store operates.': X fails the role test, as for S02-ZD-026
- S02-ZD-029 (e): the country schema's codes ('Two-letter country code according to ISO 3166-1 alpha-2'); answers none of (e)'s questions
- S02-ZD-030 (e): 'The endpoint returns all countries' names, codes, and IDs': a list of all countries; answers none of (e)'s questions
- S02-ZD-031 (e): 'Retrieve a list of cities for a specific country where the store operates or delivers.': the statement doesn't call these cities markets; answers none of (e)'s questions
- S02-ZD-045 (e): 'عند تفعيل عملة دولة يتم تفعيل الشحن إليها' (my translation: when a country's currency is turned on, shipping to it is turned on): currency and shipping, under (f); states no definer, limit or party for a market
- S02-ZD-160 (e): a warehouse's sales channels, 'إما المتجر الإلكتروني أو زد كاشير' (my translation: either the online store or Zid Cashier): locations, under (f); states no definer, limit or party for a market

zid has no statement under (g) in RD2's slice.

### woocommerce: statements noted under (e)

woocommerce has no markets feature. Its selling locations, 'Selling location(s)', the countries the store sells to, pass the role test and are placed (S02-V-448 to S02-V-452). Its shipping locations and shipping zones are shipping, under (f): a shipping zone 'is a geographic region where a certain set of shipping methods and rates apply' (S02-WC-217), and the shipping locations are the countries the store ships to. They fail the role test, as RD2-1 held for shopify's shipping zones (S02-SH-235).

- S02-WC-016 (e): the settings tab's label 'General'; answers none of (e)'s questions
- S02-WC-019 (e): 'Choose which countries you want to ship to, or choose to ship to all locations you sell to.': the shipping locations, shipping under (f); X fails the role test
- S02-WC-020 (e): the filter 'woocommerce_countries_allowed_countries'; a filter alone names no party (rule 4), and it states no definer or limit for a market
- S02-WC-021 (e): the filter 'woocommerce_countries_shipping_countries', on the countries the store ships to: shipping, under (f); a filter alone names no party
- S02-WC-030 (e): 'Returns an array of countries and codes.': the list of all countries; answers none of (e)'s questions
- S02-WC-031 (e): 'Country codes and names should follow the Unicode CLDR recommendation'; answers none of (e)'s questions
- S02-WC-032 (e): the filter 'woocommerce_countries', on the list of all countries; answers none of (e)'s questions
- S02-WC-096 (e): the label 'Shipping zones'; answers none of (e)'s questions
- S02-WC-097 (e): 'The shipping zones API allows you to create, view, update, and delete individual shipping zones.': shipping zones, shipping under (f); X fails the role test
- S02-WC-098 (e): 'The shipping zone locations API allows you to view and batch update locations of a shipping zone.': shipping, under (f); X fails the role test
- S02-WC-124 (e): 'The WooCommerce countries class stores country/state data.'; answers none of (e)'s questions
- S02-WC-131 (e): 'Get countries that the store ships to.': shipping, under (f); X fails the role test
- S02-WC-132 (e): 'If shipping is disabled, return an empty array.': shipping, under (f); X fails the role test
- S02-WC-133 (e): 'Default to selling countries.', the default of the countries the store ships to: shipping, under (f); X fails the role test
- S02-WC-134 (e): the option 'woocommerce_specific_ship_to_countries': shipping, under (f); X fails the role test
- S02-WC-152 (e): the address locales of the allowed and shipping countries ('array_merge( $this->get_allowed_countries(), $this->get_shipping_countries() )'): the buyer's address, under (f); states no definer, limit or party for a market
- S02-WC-156 (e): a code comment on the address's country field, with its reason, and 'Merchants who sell to a single country should use "Sell to specific countries" instead.': the buyer's address, under (f); states no definer, limit or party for a market
- S02-WC-172 (e): 'Shipping location(s): Choose to ship to only the countries you sell to or a subset of countries.': shipping, under (f); X fails the role test
- S02-WC-181 (e): 'you can accept payments from customers anywhere in the world in over 100 supported currencies': WooPayments' payments; states no definer, limit or party for a market
- S02-WC-210 (e): the shipping zone's properties ('Shipping zone name', 'Shipping zone order'): shipping, under (f); X fails the role test
- S02-WC-211 (e): the shipping zone location's properties ('Options: postcode, state, country and continent. Default is country.'): shipping, under (f); X fails the role test
- S02-WC-216 (e): 'A shipping zone consists of the region(s) you'd like to ship to and the shipping method(s) offered.': shipping, under (f); X fails the role test
- S02-WC-217 (e): 'A shipping zone is a geographic region where a certain set of shipping methods and rates apply.': shipping, under (f); X fails the role test
- S02-WC-218 (e): the zone 'Rest of the world', 'An optional zone you can use to set the shipping method(s) available to any regions that have not been listed above.': shipping, under (f); X fails the role test
- S02-WC-219 (e): 'List the regions you\'d like to include in your shipping zone.': shipping, under (f); X fails the role test
- S02-WC-220 (e): a shipping zone that 'will not be matched because "%1$s" covers the same region earlier in the list': shipping, under (f); X fails the role test

### woocommerce: statements noted under (g)

None of woocommerce's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, which is RD3's half.

- S02-WC-017 (g): 'select the currency your shop will use for sales': a setting that holds for the whole store, RD3's half
- S02-WC-025 (g): 'If you’d like to display products in different currencies' and 'you will need to add a multi-currency extension/plugin.': currency, a setting that holds for the whole store, RD3's half
- S02-WC-085 (g): 'WooCommerce only allows for one base currency per store.': a setting that holds for the whole store, RD3's half
- S02-WC-086 (g): 'This controls what currency prices are listed at in the catalog and which currency gateways will take payments in.': a setting that holds for the whole store, RD3's half
- S02-WC-087 (g): 'Each WooCommerce store can set one base currency.': a setting that holds for the whole store, RD3's half
- S02-WC-088 (g): 'Changing your base currency changes which currency your store displays and charges in.': a setting that holds for the whole store, RD3's half
- S02-WC-089 (g): the option 'woocommerce_currency', with ''default' => 'USD'': a setting that holds for the whole store, RD3's half
- S02-WC-175 (g): 'Currency: Sets your store’s default currency. Only one currency may be selected.': a setting that holds for the whole store, RD3's half
- S02-WC-176 (g): 'Currency position: Choose the default position of the currency symbol for prices': a setting that holds for the whole store, RD3's half
- S02-WC-177 (g): 'Thousand separator: Choose which symbol to use for the thousand separator': a setting that holds for the whole store, RD3's half
- S02-WC-178 (g): 'Decimal separator': a setting that holds for the whole store, RD3's half
- S02-WC-179 (g): 'Number of decimals': a setting that holds for the whole store, RD3's half
- S02-WC-207 (g): 'taxes are always calculated based on your store’s location, regardless of the customer’s address': a setting that holds for the whole store, RD3's half

### bigcommerce: statements noted under (e)

- S02-BC-001 (e): the API reference's section 'Create and manage sales channels, their sites, and their product listings.'; names no party that creates, changes or removes a channel
- S02-BC-017 (e): 'Group customers into segments to offer them promotions and other customized shopping experiences.': customer segments for promotions, discounts and offers under (f); the statement doesn't call a segment a channel, storefront or market
- S02-BC-055 (e): 'You can configure shipping zones in the control panel or use the API to designate where a merchant ships their products': shipping, under (f); X fails the role test
- S02-BC-158 (e): 'The default country in the drop-down menu is based on the customer’s IP address.': the buyer's address, under (f); answers none of (e)'s questions

### bigcommerce: statements noted under (g)

None of bigcommerce's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, which is RD3's half.

- S02-BC-035 (g): 'They are suitable for any global information against the store that is not channel specific.': store metafields, data that holds for the whole store, RD3's half
- S02-BC-100 (g): 'the following settings are inherently global and cannot be modified with channel-specific overrides': settings that hold for the whole store, RD3's half
- S02-BC-142 (g): 'some store functions are global and are shared across storefronts, such as the built-in blog': functions that hold for the whole store, RD3's half
- S02-BC-147 (g): 'All apps are designed to work at a store level and are installed at the store level.': apps that hold for the whole store, RD3's half

### RD2-2: new kinds

None: (e)'s points take no kind (rule 3). The brand in S02-V-457 is none of the things that bullet (e) lists (problems, below).

### RD2-2: searches for earlier platforms' rows

RD2-2 raised no point. Each of its statements under (e) answers one of S02-VP-26 to S02-VP-29, or is noted, and none of its statements under (g) says that the platform has no market of the kind in (e). So no search for shopify's rows was made.

### RD2-2: rows `not covered`, `gap` and `absent`

No row is `not covered`. Every point has a row for every platform. The rows without an answer are:

- S02-V-442: zid, S02-VP-26, `gap` S02-ZD-G06 (what the default market holds), beside zid's answer rows;
- S02-V-447: zid, S02-VP-29, `gap` S02-ZD-G05 (who removes a market);
- S02-V-449: woocommerce, S02-VP-27, `gap` S02-WC-G04 (how many a store can hold);
- S02-V-459: bigcommerce, S02-VP-26, `absent` S02-BC-N01 (a country, region or other place among what defines a channel), beside bigcommerce's answer rows.

### RD2-2: matching (rule 5)

Each point's `raised_by` holds only shopify's statements, so RD2-2's rows were compared with them. Each takes `answers` alone:

- `term`: salla's 'السوق' (translation 'Market') is the same word as shopify's translation of 'market', 'السوق', but their definitions in `terms.tsv` differ: 'السوق هو الدولة أو المنطقة التي تستهدف البيع إليها' and 'A market is a set of customers that you define in your store.' So `term` fails. zid's 'الأسواق (خاصية الأسواق)' has no translation, and a definition other than shopify's. bigcommerce's 'channel' and shopify's 'Channel markets' are different terms, with different definitions. woocommerce has no term for a market.
- `identifiers`: no key, scope, topic, field or entitlement in RD2-2's statements is the same as one in the statements of `raised_by` (S02-SH-077, S02-SH-065, S02-SH-279; S02-SH-111, S02-SH-301, S02-SH-286; S02-SH-115, S02-SH-116, S02-SH-288; S02-SH-061, S02-SH-128).
- `definition`: no statement of RD2-2's gives the same definition as one of those.

### RD2-2: problems with the method

- Salla's feature 'multi-countries' (S02-V-436): its 'limit' of 10 and its 'count' are read as how many markets a store can hold and how many it holds. This is a reading, marked in the row's basis_evidence: the flag's words, 'multi-countries', don't say market. If the reading doesn't hold, S02-SA-187 and S02-SA-234 are to be noted under (e), and the row goes.
- Salla's store scopes: S02-SA-219 holds a store scope whose scope phase A gives as 'its one market after activating multiple markets', and S02-SA-251 is the store scope's schema. They are placed in S02-V-431 and S02-V-432 as a market's countries and cities. S02-SA-251's store scope is read as a market, a reading marked in S02-V-431.
- Enabling and disabling the multiple markets feature: S02-SA-054, S02-SA-055 and S02-SA-059 name the account manager, and S02-SA-026 the seller's controls. They are noted, since the statements don't say that enabling or disabling the feature creates, changes or removes a market. If enabling the feature counts as a gate on creating a market, they belong under S02-VP-28 and S02-VP-29, as RD2-1 said of shopify's page permissions.
- Zid's 'الاسواق المتوفرة' (S02-V-443): the sales channels app calls the selling platforms it reaches (Amazon, Trendyol, Jahez, Mazeed) markets. The row places them as markets defined by a channel. If the role test reads 'الاسواق' there as a homonym, S02-ZD-145 and S02-ZD-146 are to be noted instead, and the row goes.
- Zid's default market: S02-ZD-012 says that the default market appears automatically. It is placed under S02-VP-26 only: it doesn't say who creates the default market (S02-V-446's note).
- WooCommerce has no markets feature. Its selling locations ('Selling location(s)') are placed as its market, and its shipping locations and shipping zones are noted as shipping, under (f), as RD2-1 held for shopify's shipping zones. Phase A's gap S02-WC-G04 asks, under (e)'s how many, about shipping zones and currencies; it is the `gap` row S02-V-449 under S02-VP-27, though by this role test its things are not markets. WooCommerce's rows under S02-VP-28 and S02-VP-29 are for a setting that always exists: the platform's default 'all' (S02-V-451) and the seller (S02-V-450, S02-V-452). No statement says who removes it.
- BigCommerce: a channel is where a store sells (S02-BC-002), so its channels and storefronts are placed as its markets. The rows for a region, a group of customers and a brand (S02-V-455 to S02-V-457) rest on uses the platform suggests ('can help you', 'can be useful', 'may work for some merchants'), and stand beside the `absent` row S02-V-459 (S02-BC-N01). A brand (S02-V-457) is none of the things that bullet (e) lists: a country, region, city, group of customers, location, channel or storefront.
- BigCommerce's default channel (S02-V-466): 'provisioned with one channel out of the box' is read as 'by default', so the platform's (a reading, marked in the row).
- Scopes and permissions: bigcommerce's S02-BC-004, the API scope 'store_channel_settings' at 'modify', 'View and modify a list of channels', is placed under S02-VP-29 as a permission that gates changing channels (S02-V-467). RD2-1 noted shopify's read scopes, which gate no change, and its page permissions; salla's 'branches_management' (S02-SA-255, S02-SA-257) gates a page, and is noted the same way.
- Activation and publishing: salla's activating a market (S02-SA-044) is placed under S02-VP-29, as RD2-1 placed shopify's activating and deactivating (S02-V-428). Zid's creating a market hidden or published (S02-ZD-022) is placed under S02-VP-28, since its identifier puts it among the steps of creating a market.

# RD3

## Part RD3-1: shopify, bullets f and g

Shopify is the first platform placed under RD3, so every variation point here is raised by Shopify's statements, and every basis is `answers` (rule 5: no other platform's statement is in `raised_by` yet). No earlier platform's rows were searched for: no part ran before this one.

### Statements noted (rule 2)

- S02-SH-056 (f): names the store's settings in general ('your store's default settings', overridden 'for specific markets'), of no one kind of setting
- S02-SH-062 (f): names the store's settings in general ('their parent market's settings', inherited by submarkets), of no one kind of setting
- S02-SH-064 (f): names the store's settings in general ('the customizations you apply to that market'), of no one kind of setting
- S02-SH-078 (f): names the store's settings in general ('market customizations' that 'inherit your store's default settings'), of no one kind of setting
- S02-SH-080 (f): names the store's settings in general ('the customizations of their parent market'), of no one kind of setting
- S02-SH-093 (f): states the staff permissions needed to access the Markets page; names neither what staff access takes its value per nor who sets it
- S02-SH-110 (f): names the store's settings in general (how 'customizations' are inherited across market types), of no one kind of setting
- S02-SH-118 (f): names the store's settings in general ('These settings are inherited from your store defaults, or from a parent market'), of no one kind of setting
- S02-SH-121 (f): states what customers in different countries expect of how prices are displayed; names no setting's value per market, and not who sets it
- S02-SH-128 (f): names the store's settings in general ('All changes to your store's default settings apply to your primary market automatically'), of no one kind of setting; that the store currency decides the primary market is (e)
- S02-SH-137 (f): names the store's settings in general (a deleted parent market's submarkets' 'inherited settings revert to your store's defaults'), of no one kind of setting
- S02-SH-141 (f): names the store's settings in general (a market without 'a specific customization' inherits from its parent, or 'the store default is used'), of no one kind of setting
- S02-SH-144 (f): gives reasons a business uses business entities; names no setting's value per market, and not who sets it
- S02-SH-145 (f): each entity's 'payout currency and schedule' belong to its Shopify Payments account: payouts are a thing bound under (c), not a setting of the store toward buyers
- S02-SH-153 (f): a step to open Markets > Catalogs in the admin; names no setting's value per market, and not who sets it
- S02-SH-154 (f): an admin route's path; names no setting's value per market, and not who sets it
- S02-SH-155 (f): an admin label; names no setting's value per market, and not who sets it
- S02-SH-156 (f): the permissions and entitlements needed to view catalogs, a condition of access; names no setting's value per market, and not who sets it
- S02-SH-157 (f): the permission needed to create a catalog; names no setting's value per market, and not who sets it
- S02-SH-158 (f): the access scope and permission needed to create and edit catalogs; names no setting's value per market, and not who sets it
- S02-SH-159 (f): the access scope and permission needed to delete catalogs; names no setting's value per market, and not who sets it
- S02-SH-160 (f): an API reference entry for the query catalogs; names no setting's value per market, and not who sets it
- S02-SH-161 (f): an API reference entry for the mutation catalogCreate; names no setting's value per market, and not who sets it
- S02-SH-162 (f): an admin request's variables to create a catalog; names no setting's value per market, and not who sets it
- S02-SH-183 (f): the conversion fee, a fee of the platform's (c), depends on the entity that processes the payment; names no setting's value per market, and not who sets it
- S02-SH-197 (f): a rollout's Eligibility setting displays the markets 'determined by the changes that you added to the rollout': changes to settings in general, of no one kind of setting
- S02-SH-206 (f): describes Managed Markets' features in general; names no setting's value per market, and not who sets it
- S02-SH-210 (f): names only who is kept out of setting the merchant of record disclaimer ('You can't hide or reword it, and no setting in your Shopify admin or your theme turns it off'); in the note of the point who sets 'Checkout profile and customer account configuration' (rule 5)
- S02-SH-213 (f): the permission needed to update a market's Managed Markets settings; names no setting's value per market, and not who sets it
- S02-SH-214 (f): the permissions needed to deactivate Managed Markets; names no setting's value per market, and not who sets it
- S02-SH-215 (f): an admin route's section and path, without a market; names no setting's value per market, and not who sets it
- S02-SH-224 (f): residency or business registration requirements for buying some country-specific domains, a condition on the merchant under (c); names no setting's value per market
- S02-SH-294 (f): the feature and permissions needed to create a shipping option, a condition of access; names no setting's value per market, and not who sets it
- S02-SH-302 (f): an admin tree whose node 'Store default' holds the store's settings in general, of no one kind of setting
- S02-SH-365 (f): a product price, 'Regular price 699,95 YER', on a visit intended from the United Kingdom before the market Capture UK existed (scope); one value, not what it is taken per or who sets it
- S02-SH-366 (f): the checkout's Country/Region options and one shipping rate, 'YER 2,600.00', with 'Yemen' selected, before the market Capture UK existed (scope); one value of each, not what it is taken per or who sets it
- S02-SH-373 (f): the same product price, 'Regular price 699,95 YER', on a visit intended from the United Kingdom after the market Capture UK was created and active (scope); one value, not what it is taken per or who sets it
- S02-SH-374 (f): the storefront's cookie consent banner on a visit intended from the United Kingdom (scope); one banner, not what it is taken per or who sets it
- S02-SH-375 (f): the checkout's Country/Region options, now with 'United Kingdom', and one shipping rate, 'YER 2,600.00', with 'Yemen' selected, after the market Capture UK was created (scope); one value of each, not what it is taken per or who sets it
- S02-SH-380 (f): the feature and permissions that gate the route to update a shipping option, a condition of access; names no setting's value per market, and not who sets it
- S02-SH-409 (f): the admin shows 'There's no page at this address' at the routes to create or update a market's shipping option on one store (scope 'store ibx5bt-xy'); names no setting's value per market, and not who sets it
- S02-SH-553 (f): names the experience in general ('The experience that a company location receives'), determined by the markets a company location matches, of no one kind of setting
- S02-SH-571 (f): names only the catalogs kept out of a B2B market ('You will not be able to add region catalogs or catalogs that are directly assigned to company locations to a B2B market'); in the notes of the points what 'product availability' and 'pricing' take their value per (rule 5)

### New kinds (rule 1)

- **the store's address**: the fields and format of the address the store, or its business entity, holds: the store address, and a business entity's business or residential address. Raised by S02-SH-349; its row rests on S02-SH-324, S02-SH-342, S02-SH-349, S02-SH-357 and S02-SH-359, whose captured forms show 'State' and 'ZIP code' for the country code 'United States' and 'City' with no 'State' or 'ZIP code' for 'Yemen'. Rule 1's 'the buyer's address' is the buyer's, so these fit none of its kinds.
- **units and time zone**: the store's unit system, default weight unit and time zone, which Shopify lists under 'Store defaults' in Settings > General. Raised by S02-SH-246; its row rests on S02-SH-246, S02-SH-345 and S02-SH-398.

### Kept out (rule 5)

- S02-SH-210 and S02-SH-571 are noted above, and named in their points' notes.
- S02-SH-242 and S02-SH-244: their words on who sets the address fields and validations name only who is kept out: 'You can't change which additional fields are included or whether a field is required'; 'can't be deactivated unless the store is on the Shopify Plus plan'. They are in the note of the point who sets "address autocompletion feature". Both are placed under the point what "the checkout shipping and billing address form" takes its value per, for what their other words answer.

### Gap rows

- Under the point what "the checkout shipping and billing address form" takes its value per, a `gap` row with S02-SH-G04 stands beside Shopify's answer rows (rule 4): the gap asks for the address format the platform applies for each buyer's country, beyond the countries the statements name.

### Searches for earlier platforms' rows

None: no part placed statements under RD3 before this one, and Shopify is this part's only platform.

### `not covered` rows

None: Shopify has a row under each of the 37 points, all raised from its own statements.

### How this part reads Shopify's statements

- **One market answer.** Shopify's terms make each of its market types a market: 'A submarket is a market that exists within another market', 'Channel markets use sales channels as their condition', 'A sub-region market targets a specific state or province, instead of a whole country', 'B2B markets let you create customized experiences specific to the wholesale company locations you sell to' (`terms.tsv`). A value set for any of them is one answer, `a market the store sells into`; each statement's market type is quoted in `basis_evidence`.
- **Inherited values and store defaults.** A market that takes the store's default, or its parent market's value, until the seller customizes it takes its value per `a market the store sells into` (rule 4). So the values a market shows as 'Inherited from Store default', and the 'Store defaults' node that the markets graph shows as the parent of the markets, are placed under that answer.
- **The whole store.** A row of `the whole store` rests on a statement that one value holds for the store: that a value is the same for every market or buyer ('Only one theme can be published at a time', 'Staff permissions can't be assigned per market'), or that the store holds one value of the setting (its store currency, its backup region, its contact details, its units and time zone, in Settings > General).
- **Catalogs.** Shopify's term makes a catalog 'a set of products with optional custom pricing that you assign to a market' (`terms.tsv`), so a market's catalog is placed under both products and prices.
- **Settings in general.** A statement that names the store's settings or a market's customizations in general, without a setting of one kind, is noted: its X is of no one kind (rule 1).
- **One value observed.** A capture that shows one value, such as one price or one banner, without what the value is taken per or who sets it, is noted.
- **Who sets.** A statement answers `who sets` only where it names who. The seller: 'you', an instruction to the merchant, or a control that sets the value in the store's admin. The platform: a value set 'automatically', 'by default' or 'on your behalf', or by the platform's own service or rules, with no other party named. A party the statements name besides these is its own answer: Managed Markets, with Global-e as the merchant of record it adds; Avalara; the Geolocation app; the customer. A statement whose setting is changed in the passive voice, with no party named, answers only what the value is taken per.

### Problems with the brief or the tools

- **Who sets.** Bullet (f) and rule 1 name 'the platform or the seller'. Shopify's statements also name Managed Markets with Global-e, Avalara, the Geolocation app and the customer as who sets or takes on a setting; each is kept as its own answer.
- **Store defaults.** Shopify's 'Store defaults' appear in two places: the markets graph, as the parent node of the markets (statements under (a) and (f)), and Settings > General (statements under (e) and (g) only). Rule 4's inheritance clause places the first under `a market the store sells into`; the checker requires a row resting only on statements under (g) to name `the whole store`, so the second is placed there. The two readings of one Shopify section stand side by side under the points what "currency" and what "business entities" take their value per.
- **The brief changed during this run.** Rule 4 now lets a `gap` row stand beside answer rows, and rule 5 lets a statement's `identifier` or `scope` name X or what fills it. Both fit what this part did; nothing was redone.
- **Long fields.** `basis_evidence` quotes each statement of a row, so the largest rows run to about 10,000 characters, such as the currency's row for `a market the store sells into`, with 59 statements.

## Part RD3-2: salla, bullets f and g

Salla is the second platform placed under RD3. Its statements are placed under RD3-1's 37 points first, and seven points are raised where none matched: S02-VP-78 to S02-VP-84. Salla's rows, and Shopify's under the points raised, are S02-V-676 to S02-V-750. Each Salla row under an earlier point is compared with the Shopify statement in the point's `raised_by` (rule 5): every row takes `answers`, and `term` where Salla's word for X, by its own translation in `terms.tsv` or by mine (marked 'my translation'), is the word of that Shopify statement and `terms.tsv` gives no definitions that differ. No Salla row rests on `identifiers` or `definition`.

### Statements noted (rule 2)

- S02-SA-005 (f): names the store's settings in general ('إنشاء نسخ مخصصة من متجرك الإلكتروني لكل دولة تستهدفها أو منطقة أو مدينة', my translation: 'creating customized copies of your online store for each country, region or city you target'), of no one kind of setting; its closing 'من حيث:' ('in terms of:') has no list in its own text
- S02-SA-023 (f): an admin label ('"customers/address":"Shipping addresses settings"'); names no setting's value per market, and not who sets it
- S02-SA-065 (f): names the store's settings in general ('independent settings for each market'), of no one kind of setting
- S02-SA-101 (f): steps to open the multiple markets page's Settings tab in the admin; names no setting of one kind, what its value is taken per, or who sets it
- S02-SA-142 (f): the electronic payment limits 'حسب الدولة ونوع المنتج' (my translation: 'by country and product type'), which the merchant only views ('تتيح لك الاطلاع', 'lets you view'); names neither whose country nor who sets them
- S02-SA-222 (f): one country's record in the admin's country list ('Saudi Arabia', its code and mobile code); names no setting's value per market, and not who sets it
- S02-SA-226 (f): a feature flag of the platform, 'restrict-shipping-by-country' ('"enabled": false, "released": false'): its key names shipping by 'country' without saying whose country; its value says whether the store has the feature, not a setting's value per market or who sets it
- S02-SA-227 (f): a feature flag of the platform, 'restrict-shipping-companies-by-country' ('"enabled": true, "released": true'): its key names shipping companies by 'country' without saying whose country; its value says whether the store has the feature, not a setting's value per market or who sets it
- S02-SA-228 (f): a feature flag of the platform, 'enable-shipping-by-country' ('"enabled": false, "released": false'): its key names shipping by 'country' without saying whose country; its value says whether the store has the feature, not a setting's value per market or who sets it
- S02-SA-229 (f): a feature flag of the platform, 'tax-profiles-disable-usa-country' ('"enabled": false, "released": false', plans 'pro' and 'special'): its key names one country, 'usa', without saying in what role; its value says whether the store has the feature, not a setting's value per market or who sets it
- S02-SA-230 (f): a feature flag of the platform, 'coupon-countries' ('"enabled": false, "released": false', plans 'plus', 'pro' and 'special'): its key names coupons by 'countries' without saying whose; its value says whether the store has the feature, not a setting's value per market or who sets it
- S02-SA-252 (f): one country of a live store's storefront shipping countries ('Saudi Arabia', '"is_international": false'); one value, not what it is taken per or who sets it
- S02-SA-274 (f): the customer's search history, 'سجل بحث مستقل' (my translation: 'a search history of its own') for each market: the customer's own data, not a setting whose value the seller or the platform sets (rule 1)
- S02-SA-288 (f): the countries the admin's payment limits list ('Bahrain' to 'United Arab Emirates', and 'Other countries'); names no setting's value per market, and not who sets it
- S02-SA-300 (g): states that passing a scope id makes a category's product sort 'per scope'; it doesn't state that a setting holds for the whole store, or that Salla has no market (its (f) is placed under S02-VP-47)
- S02-SA-307 (f): a branch's short address, 'National Address  required if saudi-national-address feature is enabled': a condition on a field of a branch's address; names neither what it is taken per nor who sets it

### Points raised (rule 3), and the searches for Shopify's rows

Each point below is its own: no earlier point asks its question of its kind (rule 3: two points never share a question and a kind). For each, Shopify's statements under (f) were printed by `stmt_id` and `identifier` (`| cut -f1,4,7`) and those whose identifier names X or its kind were read; then Shopify's statements under (f) and this notes-b.md were searched for the words listed, in English and Arabic (the Arabic words find nothing in Shopify's English statements).

**S02-VP-78, who sets "الفروع" (locations).** S02-VP-67 asks what locations take their value per; no point asked who sets them. Raised by S02-SA-033.
- Searched: location, inventory, fulfil, warehouse, pickup, pick up, stock, branch, allocat, priorit; الفروع, المستودعات, المخزون, and my translations branches, warehouses, stock; Shopify's 'inventory and fulfillment priorities' (S02-VP-67's x_words).
- Found: S02-SH-284 ('inventory and fulfillment priorities', under S02-VP-67), which names no one who sets them; S02-SH-209 ('organizing shipping and fulfillment', the merchant of record's responsibility, under S02-VP-60), not a setting of locations; 'location' elsewhere names a customer's or a company's location, the store's location, or a shipping profile's 'Shop location' (S02-SH-315).
- Shopify's row: `not covered`.

**S02-VP-79, who sets "معلومات خدمة العملاء" (contact information shown to buyers).** S02-VP-68 asks what it takes its value per; no point asked who sets it. Raised by S02-SA-038.
- Searched: contact, contact information, customer service, support, phone number, email; معلومات التواصل, معلومات خدمة العملاء; Shopify's 'Store contact details' (S02-VP-68's x_words).
- Found: 'contact' only inside 'Bancontact' (S02-SH-534, S02-SH-535, S02-SH-536); 'support' only of supported countries, currencies or channels. S02-SH-246 ('Store contact details: Manage store contact information') is under (a) and (g), not (f); a statement under (g) goes only under a point that asks what a value is taken per (rule 4), where RD3-1 placed it.
- Shopify's row: `not covered`.

**S02-VP-80 and S02-VP-81, what "maintenance" takes its value per, and who sets "maintenance" (store status).** No point of store status existed. Raised by S02-SA-063 and S02-SA-064, and by S02-SA-063.
- Searched: maintenance, maintenance mode, password, storefront password, store status, open, opened, closed, pause, offline, coming soon, inactive, deactivat, unavailable; صيانة.
- Found: 'open' in S02-SH-202 ('open a market', a step); 'deactivat' only of Managed Markets, its features, address autocompletion, and duties in prices; nothing of the store's status.
- Shopify's rows: `not covered`.

**S02-VP-82 and S02-VP-83, what "التذكير" takes its value per, and who sets "التذكير" (messages to buyers).** No point of messages to buyers existed. Raised by S02-SA-259.
- Searched: notification, reminder, abandon, sender, message, sms, whatsapp, email; التذكير, تذكير, السلة المتروكة, and my translations reminder, abandoned cart.
- Found: 'message' in S02-SH-457 (an API's error messages) and S02-SH-560, S02-SH-561 ('a warning message is displayed' to the merchant): not messages to buyers.
- Shopify's rows: `not covered`.

**S02-VP-84, who sets "cookie preferences" (privacy and consent).** S02-VP-75 asks what privacy and consent take their value per; no point asked who sets them. Raised by S02-SA-291.
- Searched: cookie, privacy, consent, banner, data sharing, opt-out, preferences; Shopify's 'Customer privacy', 'Cookie banner', 'Data sharing opt-out' (S02-VP-75's x_words).
- Found and placed: S02-SH-307, S02-SH-372, S02-SH-391, S02-SH-413, S02-SH-422, S02-SH-423, S02-SH-424, S02-SH-425 (the admin's link 'Customer privacy Cookie banner, Data sharing opt-out' to the store's privacy settings: the seller); S02-SH-374 (the storefront's cookie consent, 'unless you accept them', 'Manage preferences Accept Decline': the buyer). RD3-1 noted S02-SH-374 under (f) as one banner observed; read for who sets, its words name the visitor as who accepts. 'banner' elsewhere names theme banners (S02-SH-095, S02-SH-172, S02-SH-185, S02-SH-392); 'preferences' elsewhere names a customer's saved country or language (S02-SH-120) or a staff permission (S02-SH-214, S02-SH-294, S02-SH-380).
- Shopify's rows: the seller; the buyer.

### New kinds (rule 1)

None. The points raised take kinds of rule 1's list: locations, contact information shown to buyers, store status, messages to buyers, privacy and consent.

### Kept out (rule 5)

- S02-SA-105: its words on who applies tax by the market's country name only who is kept out: 'دون أي تدخل يدوي من التاجر' (my translation: 'without any manual step by the merchant'). It is in the note of S02-VP-58, and placed under S02-VP-57 for what its other words answer.

### `not covered` rows

- Salla, back to Salla for gap-closing (phase A2): S02-VP-63 and S02-VP-64 (who sells to the buyer), S02-VP-65 and S02-VP-66 (returns and cancellations), S02-VP-76 (the store's address), S02-VP-77 (units and time zone). Salla has no gap or absence in RD3's slice. Searched in Salla's statements under (f) and (g): إرجاع, استرجاع, إلغاء, return, refund, cancel, withdraw, كيان, منشأة, entity, merchant of record, وحدة, الوزن, unit, weight, time zone, المنطقة الزمنية, التوقيت, عنوان المتجر, store address, business address. Found: 'إلغاء التصنيف' (removing a category, S02-SA-156), 'unit' inside 'United Arab Emirates' (S02-SA-288), and 'المنشأة' in a tax record's fields (S02-SA-236, under S02-VP-57 and S02-VP-58).
- Shopify, back to Shopify: S02-VP-78 (who sets locations), S02-VP-79 (who sets contact information), S02-VP-80 and S02-VP-81 (store status), S02-VP-82 and S02-VP-83 (messages to buyers).

### How this part reads Salla's statements

- **A market.** Salla's 'السوق' (its own translation 'Market'): 'السوق هو الدولة أو المنطقة التي تستهدف البيع إليها' (`terms.tsv`). Salla's API calls a market a 'scope' ('store scopes ... for multi-country functionality', `terms.tsv`; 'the store markets/scopes', S02-SA-297). A value set for a market, a scope, or one of a market's sections (`القسم 1` to `القسم 8`, scope 'each market') is `a market the store sells into`. Salla's 'السوق' and Shopify's 'market' have different definitions in `terms.tsv`, so no row takes `term` from them.
- **Inherited values.** A market that takes the main store's theme, the store's main domain, the store defaults of its login options, or (the default market) the store settings' languages, until the seller changes it, takes its value per `a market the store sells into` (rule 4).
- **The whole store.** A row of `the whole store` rests on words that one value holds for the store: 'تلقائيًا على جميع الأسواق' (S02-SA-168), 'ولا يمكن تخصيص ذلك لسوق معينة' (S02-SA-156), 'Your whole store is in maintenance mode' (S02-SA-064), 'the tax rate is intended to apply to all countries' (S02-SA-310); and, for stores with one market or without multiple markets only, S02-SA-298 and S02-SA-259, whose rows say so in their notes. An option to offer something 'in every market', beside one to choose markets (S02-SA-090, S02-SA-271, S02-SA-273, S02-SA-289), is one of a per-market setting's values, and is placed under `a market the store sells into`.
- **Who sets.** The seller: 'you' ('يمكنك', 'تستطيع'), 'the merchant' ('التاجر'), the store ('كل متجر'), an instruction to the merchant ('اختر', 'حدد', 'أضف', 'فعّل'), or the text of a control in the merchant dashboard, from its own translations, quoted with its identifier where its words name no party. The platform: a value set 'تلقائياً' or 'automatically', 'افتراضياً' (by default), or by the platform's own rules (its API's mandatory fields, S02-SA-303). The buyer: the visitor who accepts cookie preferences (S02-SA-291). A statement whose setting is changed in the passive voice, with no party named, answers only what the value is taken per.
- **Feature flags.** S02-SA-224 to S02-SA-233, from the merchant dashboard's feature list, state whether a feature of the platform is enabled and released, and for which plans. They are placed where the key names a market, by Salla's 'multi-market' (its own translation of 'الأسواق المتعددة') or its API's 'scopes': S02-SA-224 'reflect-market-currency', S02-SA-231 'coupon-multi-market', S02-SA-233 'affiliate-multi-scopes', under `a market the store sells into`. Those whose key names a 'country' without saying whose are noted. None is placed under who sets: a flag's value says whether the store has the feature, not who sets the setting.
- **Translations.** Each Arabic quote carries my translation, marked 'my translation'; where `terms.tsv` gives Salla's own translation, it is named as Salla's.
- **Kinds.** Product restrictions ('قيود المنتج', S02-SA-173) are read as rules an order must pass (checkout), marked as a reading in the row; the customs information field at checkout (S02-SA-247) as checkout's settings; the national address and the local mobile number (S02-SA-021, S02-SA-022, S02-SA-092, S02-SA-094, S02-SA-095, S02-SA-303, S02-SA-304) as the buyer's address; the branches' availability on the product page (S02-SA-035) as locations; the abandoned cart reminders (S02-SA-259, S02-SA-260) as messages to buyers; the store app's markets (S02-SA-081) as storefront design (the store's app) and market selection both, and 'Restrict purchases by market' (S02-SA-076) as market selection and checkout's rules both (rule 1: a thing that sets two kinds goes under both); the conversion of amounts by exchange rate (S02-SA-079, S02-SA-103, S02-SA-273) as currency besides prices or offers.
- **Candidates not placed.** S02-SA-031's 'وهل تريد إظهار السوق للعملاء أم لا' (my translation: 'and whether you want to show the market to customers or not') and S02-SA-220's '"status": true' are the market's own state, RD2's question of who changes a market, not a setting of one of rule 1's kinds; S02-SA-275's 'إتاحة الشراء' (my translation: 'purchase availability') doesn't say which kind of setting it is. Both statements are placed under other points.

### Problems with the brief or the tools

- **A term against rule 1.** S02-SA-237's 'الدولة التي تبيع فيها' is Salla's term translated 'Country of operation' (`terms.tsv`), which rule 1 lists as the store's own country; but the statement is a step of creating a tax record that Salla's own term 'السوق' ('وسيُستخدم هذا السجل الضريبي تلقائياً عند البيع فيها') and step 7 (S02-SA-238) tie to a market. Rule 1's clause on a tax registration tied to a market is read to settle it as a market's country, and the row's note says so; the coordinator may want to rule on it.
- **Lists across sources.** S02-SA-005 and S02-SA-024 share their identifier and words but not their source (the live help page, and the capture's `texts.jsonl`), so rule 5's Lists doesn't join them. S02-SA-024 holds the whole list, and S02-SA-005 is noted.
- **Feature flags.** A feature flag's key names its setting only in a few hyphenated words. Placing or noting each flag by whether its key names a market or a country without saying whose is this part's reading; the coordinator may want to rule on it before the later parts.
- **Who requires and who sets.** S02-SA-021 names the Transport General Authority ('الهيئة العامة للنقل') as who requires the national address. Rule 1's 'a third party the statement names' is read as one that sets the value, not one that requires it, so the row is the seller's.

## Part RD3-3: zid and bigcommerce, bullets f and g

Zid and BigCommerce are the third and fourth platforms placed under RD3. Their statements are placed under the 44 points of RD3-1 and RD3-2 first. Zid's rows are S02-V-751 to S02-V-808. Each row is compared with the statement in its point's `raised_by` from another platform (rule 5): Shopify's for S02-VP-41 to S02-VP-77, Salla's for S02-VP-78 to S02-VP-84. Every row takes `answers`, and `term` where the platform's word for X, by its own translation in `terms.tsv` or by mine (marked 'my translation'), is the word of that statement and `terms.tsv` gives no definitions that differ (a definition on one side only differs from none, as RD3-2 read it).

### Zid: statements noted (rule 2)

- S02-ZD-046 (f): states that product prices are converted to the new currency at the exchange rate of the time of the change, in the passive voice with no party named ('سيتم تحويل أسعار المنتجات إلى العملة الجديدة', my translation: 'product prices will be converted to the new currency'); names neither what the currency or the prices take their value per nor who sets them
- S02-ZD-049 (f): gives reasons to offer more than one language and currency ('يعتبر فرصة ممتازة لزيادة أرباحك', my translation: 'is an excellent opportunity to increase your profits'); names no setting's value per market, and not who sets it
- S02-ZD-052 (f): an order field's description, the exchange rate of the order currency to the store currency; names neither what a currency takes its value per nor who sets it
- S02-ZD-070 (f): the cost of each WhatsApp message, which Meta classifies, differs by the receiving customer's number's country code and is taken from the store's points balance: a fee charged to the store, of (c)'s kinds (the platform's fees), not a setting of the store of (f)'s kinds (rule 1)
- S02-ZD-077 (f): a field of a location the store creates, its short address, 'Required only when country = "SA"': its words don't say whose location it is (the store's own address, or a place it ships from or keeps stock in, rule 1), so neither the kind of its X nor the role of its country is given; names no one who sets it
- S02-ZD-105 (f): an admin path to the shipping and payment restrictions ('الطريقة الاولى : الاعدادات > عام > قيود الشحن والدفع', my translation: 'the first way: Settings > General > Shipping and payment restrictions'); says where they are reached, not what they take their value per or who sets them (as RD3-1 noted S02-SH-153)
- S02-ZD-121 (f): the currency of the merchant's Zid wallet, the Saudi riyal or, for merchants in the Gulf countries, their country's local currency: the wallet is the platform's own payment service, of (c)'s kinds, not a setting of the store (rule 1)
- S02-ZD-141 (f): an admin path to the checkout page's options ('يمكنك الوصول إلى خيارات صفحة إتمام الشراء من خلال : لوحة التحكم > الاعدادات', my translation: 'you can reach the checkout page options through: Dashboard > Settings'); says where they are reached, not what they take their value per or who sets them

### Zid: `not covered` rows

Back to Zid for gap-closing (phase A2): S02-VP-44 (who sets language), S02-VP-45 and S02-VP-46 (domain), S02-VP-55 and S02-VP-56 (checkout and customer accounts), S02-VP-63 and S02-VP-64 (who sells to the buyer), S02-VP-65 and S02-VP-66 (returns and cancellations), S02-VP-67 and S02-VP-78 (locations), S02-VP-68 and S02-VP-79 (contact information shown to buyers), S02-VP-71 and S02-VP-72 (staff access), S02-VP-73 and S02-VP-74 (market selection), S02-VP-75 and S02-VP-84 (privacy and consent), S02-VP-76 (the store's address), S02-VP-77 (units and time zone), S02-VP-80 and S02-VP-81 (store status). Zid has no statement under (g) and no gap or absence in RD3's slice.

### How this part reads Zid's statements

- **A market.** Zid's 'السوق' (my translation: 'the market'), a geographic market by Zid's own term: 'تتيح خاصية الأسواق للتاجر إدارة أسعار المنتجات وتوفّرها حسب كل سوق جغرافي بشكل مستقل.' (`terms.tsv`, 'الأسواق (خاصية الأسواق)'). A value set for a market, or for a market and a sales channel ('لكل سوق وقناة', S02-ZD-011), is `a market the store sells into`. Zid's 'السوق' and Shopify's 'market' (Shopify's own translation 'السوق') have different definitions in `terms.tsv`, so no row takes `term` from them.
- **The whole store.** A row of `the whole store` rests on words that the store holds one value: the store's base or main currency ('العملة الأساسية للمتجر', 'العملة الرئيسية للمتجر'), in which buyers pay (S02-ZD-047, S02-ZD-048); the store's supported languages and currencies (S02-ZD-054); the VAT settings configured on the store (S02-ZD-099).
- **The buyer's country.** A value that follows the customer's location, country or city ('موقع العميل', 'مدينة العميل', 'دولته'), or a shipping address's currency (S02-ZD-053), is `the buyer's country`. Three readings, marked in their rows: the region of a payment or shipping restriction (S02-ZD-103, S02-ZD-104) is the customer's location that S02-ZD-106 names for the same feature; local and international shipping (S02-ZD-128, S02-ZD-129) differ by the buyer's country; the Gulf country a sender name is turned on in (S02-ZD-163 to S02-ZD-166) is where the messages are received.
- **The store's own country.** 'دولتك' and 'بلدك' (my translation: 'your country'), addressed to the merchant (S02-ZD-043, S02-ZD-100).
- **Who sets.** The seller: 'you' ('يمكنك', 'بإمكانك', 'ستتمكن', 'تمنحك', 'تتيح لك'), the merchant ('للتاجر'), an instruction to the merchant ('حدّد', 'أدخل', 'قم بـ', 'احرص'), or the dashboard's control that sets it ('لوحة التحكم > الاعدادات > اللغات والعملات'). The platform: a value set 'تلقائيًا' or 'Automatically', or by the platform's own terms for its shipping service (S02-ZD-128, S02-ZD-129). Other parties the statements name are their own answers: the enabled payment gateway, whose exchange rate converts the amount paid (S02-ZD-050); partners, who convert an order's total (S02-ZD-053); shipping companies that support cash on delivery (S02-ZD-127, a reading); a staff permission, 'manage.store.vat.settings' (S02-ZD-172, rule 4). S02-ZD-047's 'سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل' (my translation: 'product prices will be viewed by the customer in the chosen currency, such as the Omani riyal') says who views the prices, not who chooses the currency, so it isn't placed under who sets.
- **Kinds.** The products shown in a market's theme (S02-ZD-023) are products besides storefront design, and its promotional offers ('العروض الترويجية') discounts and offers (rule 1: a thing that sets several kinds goes under each); a market's sale price ('سعر التخفيض', S02-ZD-021) is a product price; the conversion of prices at the exchange rate (S02-ZD-020) is currency besides prices, as RD3-2 read Salla's; the payment and shipping restrictions (S02-ZD-104, S02-ZD-106) are payment methods and shipping, not checkout's rules, since their words name what they restrict; the sender name ('اسم المرسل', S02-ZD-163 to S02-ZD-166) is messages to buyers (rule 1 names the sender's name); invoice settings, which Zid names with its VAT settings in the one feature 'Invoice & Tax Settings' (S02-ZD-100), are read under taxes (a reading).
- **Candidates not placed.** S02-ZD-014's market name in English, 'وفي حال تفعيل اللغة الإنجليزية ستتمكن من إدخال اسم السوق باللغة الإنجليزية أيضًا' (my translation: 'and if English is turned on you can enter the market's name in English too'), is the market's own name, which Zid's term enters 'لتمييزه داخلياً' (my translation: 'to tell it apart internally'), RD2's question, not a setting of one of rule 1's kinds. S02-ZD-094's tax number and certificate per country, and the documents S02-ZD-163 to S02-ZD-166 require by the merchant's registration, are documents and checks of (c)'s kinds. All these statements are placed under other points.

### BigCommerce: statements noted (rule 2)

BigCommerce's rows are S02-V-809 to S02-V-867 under the earlier points, and its rows under the points it raised are among S02-V-868 to S02-V-892.

- S02-BC-005 (f): an API account scope ('store_channel_listings', 'View and modify a list of all channel listings for a particular channel'), a condition of an app's access; names neither what a channel's listings take their value per nor who sets them (as RD3-1 noted S02-SH-158)
- S02-BC-024 (f): an API account scope ('store_sites', 'View and modify sites and routes'), a condition of an app's access; names no setting's value per market, and not who sets it
- S02-BC-044 (f): says what the transactional currency is used for ('what BigCommerce passes to the payment provider and what is charged to a shopper's bank account'); names neither what it takes its value per nor who sets it
- S02-BC-046 (f): gives the reason to let customers shop and check out in their native currency ('provides a more consistent and positive shopping experience'); names no setting's value per market, and not who sets it
- S02-BC-047 (f): an API reference entry for countries, states and provinces, 'geographic data for use in shipping, tax, and address validation workflows'; names no setting's value per market, and not who sets it
- S02-BC-097 (f): names the store's settings in general ('They can be configured both on the **global** level and as channel-specific **contextual overrides**'), of no one kind of setting
- S02-BC-098 (f): names the store's settings in general ('Each new channel will use the store's global default values unless the merchant chooses to override them'), of no one kind of setting
- S02-BC-099 (f): names the store's settings in general ('they're modifying the global default versions of their settings'), of no one kind of setting
- S02-BC-101 (f): names the store's settings in general ('You can modify global and channel-specific settings alike'), of no one kind of setting
- S02-BC-102 (f): names the store's settings in general ('channel-specific settings are displayed first'; 'Global default settings will only appear to shoppers when channel-specific values for those properties are not defined'), of no one kind of setting
- S02-BC-119 (f): gives the reason merchants need settings per storefront ('need to be able to customize settings per storefronts in order to provide shoppers with local units of measurement, currencies, and localized content'): a need, not that a setting takes its value per market, or who sets it
- S02-BC-146 (f): says that all the Multi-Storefront features are available through the API as well; names the features in general, of no one kind of setting
- S02-BC-035 (g): store metafields, for 'any global information against the store that is not channel specific': information in general, of no one kind of setting

### BigCommerce: `not covered` rows

Back to BigCommerce for gap-closing (phase A2): S02-VP-63 and S02-VP-64 (who sells to the buyer), S02-VP-65 and S02-VP-66 (returns and cancellations), S02-VP-71 and S02-VP-72 (staff access), S02-VP-73 and S02-VP-74 (market selection), S02-VP-79 (who sets contact information shown to buyers). BigCommerce's one gap in RD3's slice, S02-BC-G03, asks for the address format per buyer's country or storefront: it is a `gap` row (S02-V-850) beside BigCommerce's answer rows under S02-VP-69, which answer the phone number's validation, address autocompletion and the default country (the buyer's country) and the fields' order (the whole store), not which fields show, their labels or which are required.

### Points raised (rule 3), and the searches for the earlier platforms' rows

Each point below is its own: no earlier point asks its question of its kind, and none of rule 1's kinds fits its X (rule 1: a thing that fits none raises a new kind). For each, Shopify's, Salla's and Zid's statements under (f), and under (g) for a point that asks what a value is taken per (rule 4), were printed by `stmt_id` and `identifier` (`| cut -f1,4,7`), those whose identifier names X or its kind were read, and their statements and this notes-b.md were searched for the words listed, in English and Arabic.

**S02-VP-85, what "country" takes its value per (the store's country).** Raised by S02-BC-109, whose localization settings set 'the country' per storefront, and S02-BC-100, whose store_country is 'inherently global'.
- Read by identifier: Shopify's Settings > General captures (S02-SH-246, S02-SH-398 to S02-SH-404) and business details forms (S02-SH-324, S02-SH-342, S02-SH-349, S02-SH-357, S02-SH-359).
- Searched: store country, shop country, store's country, store_country, country of operation, store's location, store location, store address, Country code, based in, home country, primary country, where you operate, your country; دولة المتجر, بلد المتجر, بلد متجرك (Shopify's own translation of 'store country'), دولتك, بلدك, دولته, الدولة التي تبيع فيها, عنوان المتجر, موقع المتجر.
- Found and placed: S02-SH-246 ('such as your store country', in Settings > General) and S02-SH-399 to S02-SH-404 ('Store address Yemen', each store's Settings > General): Shopify's row, the whole store.
- Found, not placed: S02-SH-143 ('your store's home country', its primary Shopify Payments account's), S02-SH-184 ('your store's location'), S02-SH-230 ('if your store is based in the United States'), S02-SH-538 ('the country where you operate'), Salla's S02-SA-276 ('دولة المتجر'), Zid's S02-ZD-043 ('عملة دولتك') and S02-ZD-100 ('بلدك'): each names the store's country as what another setting follows, placed under that setting's point, not what the store's country takes its value per; S02-SH-324 to S02-SH-359, a business entity's country code in its forms, under S02-VP-76; S02-SH-128 ('your domestic market') and Salla's S02-SA-237 ('الدولة التي تبيع فيها', a market's tax country by RD3-2's reading), a market.
- Rows: Shopify the whole store; Salla and Zid `not covered`.

**S02-VP-86, what "apps" takes its value per (apps).** Raised by S02-BC-147, under (g): 'All apps are designed to work at a store level and are installed at the store level.' No earlier point's X is of its kind (rule 4: a statement under (g) raises one).
- Searched: app, apps, application, plugin, extension, integration; تطبيق, تطبيقات; BigCommerce's 'App Support'.
- Found and placed: S02-SH-091 ('Post-purchase apps work only in your store's default currency', under (g)): Shopify's row, the whole store, as RD3-1 read the statement under S02-VP-51.
- Found, not placed: S02-SH-172 and S02-SH-187 (the Translate & Adapt app, a tool for a market's content, under storefront design); S02-SH-230 (the Geolocation app, a party under S02-VP-74); S02-SH-399 to S02-SH-401 ('Business entity used for financial products, markets, apps, and taxes', the business entity's); Salla's S02-SA-081 and S02-SA-279 (the store's own app, which rule 1 puts under storefront design); 'تطبيق' elsewhere in Salla's statements means applying a language, a route, a tax, a reminder or an offer (S02-SA-032, S02-SA-175, S02-SA-240, S02-SA-259, S02-SA-273). Zid: nothing.
- Rows: Shopify the whole store; Salla and Zid `not covered`.

**S02-VP-87 and S02-VP-88, what "web analytics" takes its value per, and who sets "web analytics" (analytics and tracking).** Raised by S02-BC-144 ('Set up web analytics (like Google Analytics) specific to each storefront. Set up a Meta Pixel specific to each storefront.') and S02-BC-145 ('Set up analytics tracking for each headless storefront.').
- Searched: analytics, pixel, tracking, Google, Meta, Facebook, tag; تحليلات, بكسل, تتبع.
- Found, not placed: S02-SH-093 (the 'Analytics (all permissions)' staff permission, noted by RD3-1); S02-SH-374 (the cookie banner's 'perform analytics', under privacy and consent); S02-SH-345 ('when orders and analytics are recorded', the time zone); Salla's S02-SA-094 ('Google Place', an address capture method). Zid: nothing.
- Rows: Shopify, Salla and Zid `not covered`.

**S02-VP-89 and S02-VP-90, what "internal notifications" takes its value per, and who sets "internal notifications" (notifications to the merchant).** Raised by S02-BC-144 ('Configure storefront settings and internal notifications for each storefront.').
- Searched: notification, notify, internal, alert, staff notification; إشعار, إشعارات, تنبيه.
- Found, not placed: 'internal' only in the names of interface elements in Shopify's captures ('s-internal-button', 's-internal-select': S02-SH-389 to S02-SH-393, S02-SH-398, S02-SH-458). Salla and Zid: nothing; Salla's reminders (S02-VP-82) are messages to buyers.
- Rows: Shopify, Salla and Zid `not covered`.

### New kinds (rule 1)

- **the store's country** (S02-VP-85): the country a store, or one of its storefronts, holds or presents as its own: BigCommerce's store_country, global only (S02-BC-100), and a storefront's localization country, which 'allows your storefront to present itself as a domestic store based in the country that you are planning to sell to' (S02-BC-109); Shopify's store country in Settings > General. RD1 asks what fills the store's own country; this point asks only what the setting takes its value per. Rule 1's 'the store's address' kind (S02-VP-76) holds the address's fields and format, not its country, so store_address_type is placed there and store_country here.
- **apps** (S02-VP-86): the apps a store installs, not the store's own app, which rule 1 puts under storefront design.
- **analytics and tracking** (S02-VP-87, S02-VP-88): web analytics and tracking pixels set up for a storefront.
- **notifications to the merchant** (S02-VP-89, S02-VP-90): notifications the store sends its merchant or staff; rule 1's 'messages to buyers' are the buyer's.

### `not covered` rows under the points raised

- Shopify, back to Shopify: S02-VP-87 to S02-VP-90.
- Salla, back to Salla: S02-VP-85 to S02-VP-90.
- Zid, back to Zid: S02-VP-85 to S02-VP-90.

### How this part reads BigCommerce's statements

- **A market.** BigCommerce's 'channel' ('A channel is anywhere a merchant sells their products. This encompasses headless storefronts, marketplaces, POS systems, and marketing platforms.', `terms.tsv`), a storefront among its types. A value set for a channel or a storefront, or a global default a channel can override (BigCommerce's 'global default' and 'channel-specific contextual overrides', `terms.tsv`), takes its value per `a market the store sells into` (rule 4). A customer group, to which a price list may be assigned (S02-BC-020, S02-BC-021), is read as a group of customers, which bullet (e) names among what defines a market (a reading, marked in its row).
- **The whole store.** A row of `the whole store` rests on words that one value holds for the store: 'inherently global and cannot be modified with channel-specific overrides' (S02-BC-100), 'some store functions are global and are shared across storefronts' and 'cannot be overridden into a different language' (S02-BC-142), 'installed at the store level' (S02-BC-147), 'the list of enabled currencies on your store' (S02-BC-115), 'in the order they are configured in your store's settings' (S02-BC-161).
- **The buyer's country.** Shoppers in associated countries (S02-BC-042) or from different regions (S02-BC-058), the customer's address (S02-BC-129, S02-BC-159, S02-BC-160), the shopper's geolocation (S02-BC-057's identifier) or IP address (S02-BC-158), and the countries a payment method is available in or supports for shoppers (S02-BC-052, S02-BC-124, S02-BC-128). Readings, marked in their rows: a tax zone's countries (S02-BC-130, read with S02-BC-129 of the same source) and a shipping zone's regions (S02-BC-055).
- **The store's own country.** S02-BC-128's 'store ... countries', beside its merchant account's and the shopper's.
- **Who sets.** The seller: 'you', 'merchants', an API reference's instruction ('Manage', 'Create', 'Add', 'Populate'), or the control panel ('managed from one BigCommerce control panel', 'you can do all of this within the control panel', Channel Manager, Settings > Setup > Currencies). The platform: 'by default' (S02-BC-050, S02-BC-155), built-in fields (S02-BC-154), and a default taken from the customer's IP address (S02-BC-158). Stripe, which detects the shopper's currency and converts the amounts (S02-BC-045). No one: 'These fields cannot be removed' and 'cannot be made optional' (S02-BC-156, S02-BC-157), passives that name no party (rule 4's 'no one can'). Webhook descriptions ('Fires when ...') and passives ('can be customized', 'can be localized') name no party, and are placed only under what a value is taken per.
- **Kinds,** as read here (readings marked in their rows): storefront search settings (S02-BC-026) and product filtering (S02-BC-144) as products, of which products a shopper finds and in what order; inventory settings (S02-BC-144, S02-BC-145) as locations, of how stock is taken; storefront security settings (S02-BC-034) as privacy and consent, since S02-BC-029's identifier 'Security Settings' holds cookie consent; scripts, pages, widgets, social media links and the built-in blog as storefront design; email templates, transactional store emails and abandoned cart notifications as messages to buyers; login access and creating customers as customer accounts; sites, URL structure, 301 redirects and SSL certificates as domain; the store profile's shopper-facing name, address, email and phone (S02-BC-103, S02-BC-112) as contact information shown to buyers; physical dimensions, date and timezone (S02-BC-109) as units and time zone (S02-VP-77); a payment provider enabled for a channel (S02-BC-028) as payment methods offered to buyers.
- **Candidates not placed.** In S02-BC-144 and S02-BC-145: creating and managing storefronts (RD2's question of who creates a market); 'Configure storefront settings' (settings in general); 'Stores on a Performance plan will have access to additional product localization fields' (a plan's condition, (h)'s kind); viewing orders and customers in one place and filtering sales reports by channel (the admin's views, not a setting of the store); 'Manage customer groups (like retail or wholesale) for each storefront and set the default group' (a group of customers, which bullet (e) names among what defines a market: RD2's question); 'Collect and export newsletter subscriptions per storefront' (the customers' own subscriptions, not a setting, as RD3-2 read S02-SA-274); 'Enable/disable purchasing on the storefront' (it doesn't say which kind of setting it is, as RD3-2 read S02-SA-275's 'إتاحة الشراء'). S02-BC-134's 'containers for settings and objects that only apply to websites' (settings in general). S02-BC-128's Braintree and PayPal business account countries (the merchant's payment accounts, of (c)'s kinds). S02-BC-045's 'renders a currency selector next to the payment methods' doesn't say who chooses. S02-BC-142's 'the same product can be assigned to different storefronts' is under (e) and (g), not (f); a statement under (g) is placed only under the whole store (rule 4). All these statements are placed under other points.

### Problems with the brief or the tools

- **Zid's tax countries against rule 1.** Each country Zid's tax settings add holds the merchant's tax number and VAT certificate (S02-ZD-094), which rule 1 counts as the store's own country unless a statement or term ties the registration to a market; no Zid statement or term does. Zid's own words name the country 'الدولة المطبق عليها الضريبة' (my translation: 'the country the tax is applied to', S02-ZD-093, and its term in `terms.tsv`) and 'Tax-Applicable Countries' (S02-ZD-101). S02-V-776 reads them as the buyers' country, marked as a reading, as RD3-1 placed Shopify's tax registrations per region (S02-SH-176) under the buyer's country; the coordinator may rule that rule 1's clause makes them the store's own country.
- **BigCommerce's selected country.** S02-BC-111 ('The selected country determines tax and shipping zone settings', marker 'still in development') names the country of a storefront's localization settings (S02-BC-109: 'present itself as a domestic store based in the country that you are planning to sell to'). S02-V-833 and S02-V-836 read it as a market's country (a reading); phase A placed S02-BC-109 under (a) and S02-BC-111 under (c) as well, so the coordinator may read it as the store's own country instead.
- **Staff permissions.** Rule 4 makes a staff permission that gates a setting its own answer under who sets it; S02-V-780 places Zid's 'manage.store.vat.settings' (S02-ZD-172) so. RD3-1 noted Shopify's permission statements (such as S02-SH-157 and S02-SH-213) as conditions of access; the coordinator may want the two platforms read alike.
- **'No one' and 'kept out'.** RD3-1 read Shopify's 'You can't change which additional fields are included or whether a field is required' (S02-SH-242) as naming who is kept out (rule 5). BigCommerce's 'These fields cannot be removed' and 'cannot be made optional' (S02-BC-156, S02-BC-157) name no party, and are placed as rule 4's 'no one can' (S02-V-853).
- **Kinds.** Four new kinds take six points (S02-VP-85 to S02-VP-90); nine of RD3's cap remain for RD3-4. Several BigCommerce settings are placed under rule 1's kinds by a reading, listed above; the coordinator may prefer new kinds for some (search and filtering, inventory, security settings), and Zid's invoice settings are read under taxes.
- **A scope with a semicolon.** Zid's S02-ZD-163 has the scope 'سجل تجاري سعودي; دول الخليج', which S02-V-806 and S02-V-807 copy as it is, so their `scope` field holds a semicolon inside one statement's scope.
- **Writes.** No write was refused. The rows were appended with scripts in this part's scratch folder, which validate each excerpt and each quote attributed to a statement against the slice before appending; they append and never rebuild the files.
- **Rows resting on a statement under (g).** They take `answers` alone (rule 4). The checker flagged S02-V-873 (S02-SH-091, under (g) only), which had `answers;term`; it didn't flag S02-V-816 (S02-BC-142, under (e) and (g)), which had the same. Both were corrected to `answers`.

## Part RD3-4: woocommerce, bullets f and g

WooCommerce is the fifth and last platform placed under RD3. Its statements are placed under the 50 points of RD3-1 to RD3-3, and no point is raised: every candidate whose X passes the role test is of a kind that an earlier point asks about, under the same question. WooCommerce's rows are S02-V-893 to S02-V-960, one or more under each of the 50 points. Each row is compared with the statement in its point's `raised_by` from another platform (rule 5): Shopify's for S02-VP-41 to S02-VP-77, Salla's for S02-VP-78 to S02-VP-84, BigCommerce's for S02-VP-85 to S02-VP-90. Every answer row takes `answers`, and `term` where WooCommerce's word for X is the word of that statement and `terms.tsv` gives no definitions that differ: 'currency' (S02-SH-037, S02-SH-055), 'pricing' (S02-SH-055) and 'tax' (S02-SH-086). Rows that rest on a statement under (g) take `answers` alone (rule 4). No row rests on `identifiers` or `definition`.

### Statements noted (rule 2)

- S02-WC-001 (f): the payment extension list the platform suggests 'for each country', without saying whose country; suggestions to the merchant of providers to install, of (c)'s kinds (other payment providers), not a setting of the store (rule 1)
- S02-WC-002 (f): gets that list 'for a specific country', without saying whose; as S02-WC-001
- S02-WC-003 (f): the list returned 'for the given country' ('Empty array if no extensions are available for the country or the country is not supported'), without saying whose; as S02-WC-001
- S02-WC-061 (f): the order of those suggestions ('it will be used to determine the priority of the suggestions'); as S02-WC-001
- S02-WC-205 (f): the tax solutions the platform recommends, which 'vary by your store country and by extensions that are already installed or active': recommendations to the merchant, of (c)'s kinds (the store's taxes), not a setting of the store (rule 1)
- S02-WC-033 (f): the methods WooPayments sends payouts by ('a bank account (all countries) or a debit card (U.S. only)'): payouts are a thing bound under (c), not a setting of the store toward buyers (as RD3-1 noted S02-SH-145)
- S02-WC-035 (f): the pending period of payouts by country (scope 'WooPayments account country'): payouts, of (c)'s kinds
- S02-WC-036 (f): the payout schedules open to merchants in Japan ('Merchants in Japan cannot receive daily payouts'): payouts, of (c)'s kinds
- S02-WC-038 (f): the payout currencies of 'your country': payouts, of (c)'s kinds
- S02-WC-039 (f): the payout currencies by country (scope 'WooPayments account country'): payouts, of (c)'s kinds
- S02-WC-064 (f): what WooPayments' fees depend on ('The country your business is located in. The country your customer is located in. The currency in which the customer paid. The specific payment method used to pay.'): the platform's fees, of (c)'s kinds, not a setting of the store (as RD3-1 noted S02-SH-183)
- S02-WC-213 (f): the International Payment fee, 'applied if the customer’s payment method originates from outside your WooPayments account country': the platform's fees, of (c)'s kinds
- S02-WC-215 (f): the countries whose cards WooPayments counts as 'European cards' for the International Payment fee: the platform's fees, of (c)'s kinds
- S02-WC-066 (f): the currency that card readers and Tap to Pay collect payments in, 'the default currency for each country', without saying whose country; names neither what it takes its value per in one of rule 4's roles nor who sets it
- S02-WC-026 (f): the customer currency 'can be changed' with WooPayments' multi-currency functions, in the passive voice with no party named; names neither what it takes its value per nor who sets it
- S02-WC-106 (f): where the EU VAT Number settings are ('WooCommerce > Settings > Tax'); says where they are reached, not what they take their value per or who sets them (as RD3-1 noted S02-SH-153, and RD3-3 S02-ZD-105)
- S02-WC-124 (f): the description of a class of the release's code ('stores country/state data'); names no setting's value per market, and not who sets it
- S02-WC-164 (f): the heading of a file of the release ('Locales information'); names no setting's value per market, and not who sets it
- S02-WC-165 (f): the values the release's file i18n/locale-info.php holds for one country code, 'AD' (among them 'currency_code' => 'EUR', 'weight_unit' => 'kg', 'default_locale' => 'ca_AD'), without saying whose country it is or which setting of the store takes them; the gap S02-WC-G05 asks, and stands as a `gap` row under S02-VP-41 to S02-VP-44 and S02-VP-77
- S02-WC-166 (f): Bulgaria's change from BGN to EUR on 2026-01-01 in the same file (scope 'BG'), without saying whose country it is or which setting takes it; as S02-WC-165
- S02-WC-167 (f): the package the release's postcode patterns are generated from ('postcode-validator', version '3.9.2'); names no setting's value per market, and not who sets it
- S02-WC-168 (f): the per-country postcode patterns of the release's file i18n/postcode-validation-rules.json, without saying where they apply; the gap S02-WC-G05 asks, and stands as a `gap` row under S02-VP-69
- S02-WC-161 (f): a rule for writing the release's states file ('States should be defined in English and translated native through localisation files'); names neither what the states take their value per in one of rule 4's roles nor who sets them
- S02-WC-162 (f): a rule for naming the release's countries and states after the Unicode CLDR recommendation: a third party's recommendation, not who sets them (rule 4: a party that requires a value without setting it isn't who sets it); names no value per market
- S02-WC-140 (f): the article the release's code puts before a country's name ('to the' or 'to', its 'shipping country prefix'), by the country's code, by default the customer's shipping country: the wording of a text, not a setting whose value the seller or the platform sets for the store (rule 1's role)
- S02-WC-141 (f): the article 'the' that the release's code puts before a country's name in the text its identifier calls 'estimated_for_prefix', by the country's code, by default the store's base country: as S02-WC-140; its words don't say which text it goes in
- S02-WC-203 (f): the reason WooPay works only for customers in the U.S. ('various country-specific laws around cookie consent and marketing opt-ins in GDPR countries'): laws that require, not a party that sets (rule 4); names no setting's value per market

By reason: 13 of (c)'s kinds, not a setting of the store (5 payouts, 3 fees, 5 suggestions or recommendations to the merchant, 4 of these also without saying whose country); 4 per-country values or patterns of the release's files whose country's role and setting aren't said, which the gap S02-WC-G05 asks (S02-WC-165, S02-WC-166, S02-WC-167, S02-WC-168); 1 a country without saying whose (S02-WC-066); 1 a passive with no party and no per (S02-WC-026); 4 naming no setting's value or who sets it (an admin path, a class's description, a file's heading, a reason: S02-WC-106, S02-WC-124, S02-WC-164, S02-WC-203); 2 rules for writing the release's files (S02-WC-161, S02-WC-162); 2 the wording of a text (S02-WC-140, S02-WC-141). All 27 are under (f); every statement under (g) is placed.

### `gap` rows

WooCommerce's one gap in RD3's slice, S02-WC-G05, asks which store settings take the per-country values of i18n/locale-info.php and whether the platform applies them or the seller chooses, and where the per-country postcode patterns apply. It stands as a `gap` row under S02-VP-41 and S02-VP-42 (currency, beside the answer rows, which give the store's base currency and WooPayments' multi-currency, not those values), S02-VP-43 and S02-VP-44 (language: direction and default_locale), S02-VP-77 (units: weight_unit and dimension_unit), and S02-VP-69 (the buyer's address: the postcode patterns, beside the answer rows).

### `not covered` rows

Back to WooCommerce for gap-closing (phase A2), 31 rows: S02-VP-45 and S02-VP-46 (domain), S02-VP-47 and S02-VP-48 (products), S02-VP-52 (who sets discounts), S02-VP-53 (what storefront design takes its value per), S02-VP-55 and S02-VP-56 (checkout and customer accounts), S02-VP-63 and S02-VP-64 (who sells to the buyer), S02-VP-65 and S02-VP-66 (returns and cancellations), S02-VP-67 and S02-VP-78 (locations), S02-VP-68 and S02-VP-79 (contact information shown to buyers), S02-VP-71 and S02-VP-72 (staff access), S02-VP-73 and S02-VP-74 (market selection), S02-VP-75 and S02-VP-84 (privacy and consent), S02-VP-80 and S02-VP-81 (store status), S02-VP-82 and S02-VP-83 (messages to buyers), S02-VP-86 (apps), S02-VP-87 and S02-VP-88 (analytics and tracking), S02-VP-89 and S02-VP-90 (notifications to the merchant).
- Searched in WooCommerce's statements under (f) and (g): domain, subdomain, url, product, catalog, theme, widget, block, checkout, customer account, registration, login, business entit, merchant of record, return, refund, cancel, inventory, stock, warehouse, pickup, fulfil, contact, phone, email, staff, permission, role, country selector, redirect, switch, privacy, cookie, consent, maintenance, coming soon, notification, message, sender, app, extension, plugin, analytics, pixel, tracking, unit, weight, dimension, time zone, timezone, language, locale, translat.
- Found: 'product' and 'catalog' only of currencies and prices (S02-WC-025, S02-WC-086, S02-WC-087, S02-WC-192, S02-WC-196, S02-WC-197); 'theme', 'widget' and 'block' only in S02-WC-198, placed under S02-VP-42 and S02-VP-54; 'checkout' only in statements on taxes and the address (S02-WC-091, S02-WC-092, S02-WC-103, S02-WC-147, S02-WC-154, S02-WC-208); 'return' only as a word of the code; 'phone' only of the address's phone field (S02-WC-147, S02-WC-149) and of Tap to Pay on iPhone (S02-WC-066); 'switch' only of currencies (S02-WC-027, S02-WC-194, S02-WC-198); 'cookie' and 'consent' only in the reason S02-WC-203, noted; 'app' only inside other words, such as apply_filters; 'extension' and 'plugin' in the suggestions and recommendations, noted, in S02-WC-025, placed under S02-VP-41, and in S02-WC-024 ('core WooCommerce plugin') and S02-WC-157 (plugin_path); 'unit', 'weight' and 'dimension' only in S02-WC-165, noted, and inside country names; 'locale' only of the address's country locale (S02-VP-69, S02-VP-70) and of the file i18n/locale-info.php, noted; 'translat' only in S02-WC-147's note to translators and S02-WC-161 and S02-WC-162, noted. Nothing for the other words.
- S02-VP-52: WooCommerce's one statement on coupons, S02-WC-017 ('enable tax calculations and coupons'), is under (g) for RD3, and rule 4 places a statement under (g) only under a point that asks what a value is taken per; it is under S02-VP-51.

### Points raised (rule 3), and searches for the earlier platforms' rows

None. No search for the other platforms' rows was needed.

### New kinds (rule 1)

None.

### How this part reads WooCommerce's statements

- **A market.** No statement of WooCommerce's in RD3's slice gives a value per a market the store defines and sells into, so no WooCommerce row takes `a market the store sells into`. Its shipping zones match a shopper 'by their shipping address' (S02-WC-216), so a value set per zone takes its value per the buyer's country, as RD3-1 and RD3-3 read Shopify's and BigCommerce's shipping zones. The regions the store ships orders to (S02-WC-017) are set once for the store, and are placed under shipping as the whole store; the regions it sells to, in the same words, are the market's own definition, RD2's question under (e), and are not placed.
- **The store's own country.** The store address, the shop base address, the shop's country or region, the base country, and get_base_country() in the release's code (WooCommerce's terms 'Store Address', 'base country', 'store country' and 'Shop country/region').
- **The buyer's country.** The customer's shipping or billing address, the customer's location, geolocated or entered, and the country chosen for an address. Readings, marked in their rows: a tax rate's country (S02-WC-209, S02-WC-212) and a manual rate for a state (S02-WC-120), matched against the address WooCommerce calculates tax from; the address formats (S02-WC-142 to S02-WC-144), which are those of any address, the buyer's among them.
- **The whole store.** The statements under (g), and statements under (f) that the store holds one value or one list (S02-WC-028, S02-WC-193).
- **Code.** The release's code and its comments are read by their words and identifiers (rule 5), and the readings are marked in their rows. A value the code sets, or a default it gives ('default' =>), is read as the platform's (rule 4's 'by default'). A filter (apply_filters) names no party, so a filter alone isn't placed under who sets. Where the words name a party, it is placed: 'Developers' (S02-WC-122) as its own answer, and a code comment's 'you' (S02-WC-159) as the seller, as RD3-3 read an API reference's instructions. A checkbox or select among the general settings (S02-WC-023, S02-WC-091), from their source path includes/admin/settings/class-wc-settings-general.php, is read as a control in the store's settings.
- **Who sets.** The seller: 'you', 'store owners', an instruction to the merchant, or a control in the store's settings. The platform: 'by default', 'automatically', 'we', the release's own code, and the platform's own services WooPayments, WooCommerce Tax and WooPay, by their names (a reading). The buyer: the customer who selects or chooses a currency (S02-WC-192, S02-WC-198). Developers (S02-WC-122). No one: 'cannot be changed while automated taxes are enabled' (S02-WC-121), 'cannot have custom validation rules' (S02-WC-103), 'Country cannot be hidden or optional via locale' (S02-WC-156).
- **Kinds.** The default customer location (S02-WC-023, S02-WC-173, S02-WC-174) is placed under taxes and shipping, which its own words and WooCommerce's term name ('This is used help calculate default tax and shipping rates'), not under market selection. The words taxes are named by, 'VAT' or 'Tax' (S02-WC-137 to S02-WC-139), are placed under taxes, as how taxes are shown, with the lists of countries they check the base country against (S02-WC-135, S02-WC-136). Price rounding and charm pricing (S02-WC-196, S02-WC-197) are under currency and prices both, as RD3-2 and RD3-3 read conversion. The currency switcher block or widget (S02-WC-198) is under currency and storefront design both (rule 1). The address formats, locales, default fields and states are under the buyer's address. WooPay (S02-WC-202) is read as a payment method offered to buyers.
- **One option, two sources.** The default customer location is one option in the code (S02-WC-023) and in the documentation (S02-WC-173, S02-WC-174), read as one by WooCommerce's term 'Default customer location'. The Calculate tax based on setting is under (f) in S02-WC-206 and its option 'Shop base address' under (g) in S02-WC-207: S02-WC-206's option is placed under the store's own country, and S02-WC-207 under the whole store (rule 4).
- **Lists.** S02-WC-022 and S02-WC-024 share a source and an identifier ('MaxMind geolocation integration'), so S02-WC-022's 'To determine this' is read with S02-WC-024 (rule 5, Lists). The runs of i18n/states.php (S02-WC-160 to S02-WC-163) are read together: S02-WC-160 and S02-WC-163 are placed, and S02-WC-161 and S02-WC-162 noted.
- **Candidates not placed.** S02-WC-017's 'define the regions you will sell ... to' and S02-WC-156's 'Merchants who sell to a single country should use "Sell to specific countries" instead' name the countries a store sells to, RD2's question; S02-WC-092's 'It does not file returns, remit tax, or determine where your business has a tax obligation', S02-WC-120's 'WooCommerce Tax does not calculate or update them' and S02-WC-103's 'not by your settings' name who is kept out, beside words of theirs that are placed. All these statements are placed under other points.

### Problems with the brief or the tools

- **Code and who sets.** Rule 4 says nothing of a value that the release's code sets, or of its filters. This part reads a value or a default in the code as the platform's, and a filter as naming no party, except where the words name one; the coordinator may want to rule on it, since many of WooCommerce's statements are code.
- **Statements under (g) and who sets.** Some of WooCommerce's statements under (g) also say who sets the setting: the seller, in S02-WC-017 ('you can ... enable tax calculations and coupons, and select the currency your shop will use for sales'), S02-WC-087 ('Each WooCommerce store can set one base currency') and S02-WC-175 to S02-WC-179 (the currency options). Rule 4 places a statement under (g) only under a point that asks what a value is taken per, and the checker refuses one under a point that asks who sets, so these are placed only under the whole store, and S02-VP-52 (who sets discounts) is `not covered`.
- **The wording of a text.** S02-WC-140 and S02-WC-141 are noted as not a setting of the store. The coordinator may read them as a setting of a kind instead: the buyer's address (S02-WC-140's country is the customer's shipping country) or a new kind.
- **(c)'s kinds under (f).** Payouts, the platform's fees, and the platform's suggestions and recommendations to the merchant are noted, as RD3-1 and RD3-3 noted payouts and fees; phase A put them under (c) and (f) both.
- **The store's country.** WooCommerce's row under S02-VP-85 rests on S02-WC-017's 'business address', read through WooCommerce's terms 'store country' ('The store country comes from WooCommerce > Settings > General > Store Address.') and 'Store address'; it is marked as a reading.
- **Writes.** No write was refused. The rows were written with scripts in this part's scratch folder, which validate each excerpt, and each quote attributed to a statement or a term, against the slice with the checker's normalization, and which append rows or replace this part's own rows, never rebuilding the file: S02-V-912 (S02-VP-54) was appended as `not covered` and replaced in place by the seller's row after the search above found S02-WC-198. In variation-points.tsv, only the `x_words` of 16 points changed, by WooCommerce's words.

