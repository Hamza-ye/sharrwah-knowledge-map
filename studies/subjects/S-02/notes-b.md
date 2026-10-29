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

## Second pass, RD1-S2

Part RD1-S2 of the second pass: the tasks of `b/second-pass/RD1/worklist.tsv` under (c) for Shopify and Salla.

### Revisit S02-V-164 (salla, S02-VP-16, the store's taxes)

Replaced: `not covered` became an answer row, S02-V-164, 'This option is currently available for stores in Saudi Arabia only.' (S02-SA-349, S02-SA-350, S02-SA-358). Its leads noted:
- S02-SA-353 (c): a list of products' VAT exemption reasons ('VATEX-SA-29':'Financial services' and the rest); names no decider (rule 4)
- S02-SA-354 (c): the same list's next run (rule 5, Lists); names no decider (rule 4)
- S02-SA-355 (c): the same list's next run (rule 5, Lists); names no decider (rule 4)
- S02-SA-356 (c): the same list's last run (rule 5, Lists); names no decider (rule 4)
- S02-SA-357 (c): the complete address of the store's main, default branch ('بيانات الفرع الرئيسي (الإفتراضي) لمتجرك مكتملة من حيث العنوان'; my translation: that the data of your store's main, default branch be complete as to its address), a requirement of ZATCA integration: its decider is a branch, which rule 1 keeps out of the store's own country; in S02-VP-16's note
- S02-SA-361 (c): 'Enter the official rate that applies in the market you are selling into': its decider is a market the store sells into, RD3's (f), not the store's own country; in S02-VP-16's note
- S02-SA-363 (c): 'Select a country and create your tax record first to enable tax collection': the tax record's country, which Salla's term ties to a market the store sells into ('السوق' in terms.tsv: 'وسيُستخدم هذا السجل الضريبي تلقائياً عند البيع فيها'; my translation: this tax record will be used automatically when selling in it), not the store's own country; in S02-VP-16's note
- S02-SA-364 (c): 'Select a country and create your tax record first to enable government integrations': the tax record's country, as for S02-SA-363; in S02-VP-16's note
- S02-SA-374 (c): customs duties on international shipments 'are calculated on the waybill and then settled directly from your wallet balance': names no decider of the store's taxes (rule 4)
- S02-SA-375 (c): customs duties on DHL international shipping 'are settled through your store wallet balance': names no decider (rule 4)

### Revisit S02-V-168 (salla, S02-VP-18, the store's defaults)

Replaced: `not covered` became `gap`, S02-V-168, with S02-SA-G07, which asks whether the store's country sets the default currency or language. No lead answers. Its leads noted:
- S02-SA-387 (c): the merchant can change the store's default currency 'بشرط أن لا يكون هناك طلبات شراء للعملاء' (my translation: provided there are no customer purchase orders): the merchant's choice and a condition on changing it, not the store's own country; in S02-VP-18's note
- S02-SA-388 (c): 'you can change the default currency as long as there are no existing customer orders in the system': as S02-SA-387; in S02-VP-18's note
- S02-SA-390 (c): what the default language is, the language of the base definition of the store's sections; names no decider (rule 4)
- S02-SA-391 (c): the merchant sets the default language by choosing it from the languages added to the store: the merchant's choice, not the store's own country; in S02-VP-18's note
- S02-SA-392 (c): the default language can't be changed after content is translated into other languages: a condition on changing it, not the store's own country; in S02-VP-18's note
- S02-SA-393 (c): 'You cannot change the default language after content ... has already been translated': as S02-SA-392; in S02-VP-18's note
- S02-SA-400 (c): entering the national address 'will be mandatory on Salla when creating or completing orders, in accordance with Transport Authority requirements': an order's address, not a default the platform sets for the store; it fits none of (c)'s kinds of thing bound, and the second pass raises no point (brief, second pass)

### Revisit S02-V-219 (salla, S02-VP-19, the store's data)

Replaced: `not covered` became an answer row, S02-V-219, every store, 'The merchant must comply with Salla’s Privacy Policy and all provisions of the Personal Data Protection Law in the Kingdom of Saudi Arabia.' (S02-SA-335, S02-SA-336, S02-SA-324, S02-SA-328, S02-SA-325, S02-SA-337, S02-SA-338, S02-SA-319, S02-SA-320, S02-SA-321); and a `gap` row beside it, S02-V-241, with S02-SA-G05, which asks where the store's data is stored or accessed, which the answer doesn't give. Its leads noted:
- S02-SA-322 (c): a contact for the personal data protection department of 'شركة منصة سلة للاتصالات و تقنية المعلومات'; names no decider (rule 4)
- S02-SA-323 (c): the definition of 'منصة سلة' (Salla's platform) and the company that owns it; names no decider of the store's data (rule 4)
- S02-SA-326 (c): the law 'يطبق ... على أي عملية معالجة لبيانات شخصية تتعلق بالأفراد المواطنين أو المقيمين في المملكة' (my translation: applies to any processing of personal data of individuals who are citizens or residents of the Kingdom): its decider is the persons whose data is processed, not the store's own country; in S02-VP-19's note
- S02-SA-327 (c): the Saudi Data and AI Authority receives the complaints about the law; names no decider (rule 4)
- S02-SA-329 (c): the merchant 'يمكنك تفعيل آلية الموافقة الصريحة على ملفات تعريف الارتباط' (my translation: you can enable explicit consent to cookies): a setting the merchant switches on, RD3's privacy and consent; names no decider (rule 4)
- S02-SA-332 (c): 'Enable cookie consent to comply with regulations like: PDPL (Saudi Arabia) GDPR (EU)': as S02-SA-329; names no decider (rule 4)

A call the brief left to me: rule 4's `every store` holds 'where neither it nor its scope names a country'. These statements name Saudi Arabia only as the country of the law that applies, which is X itself (the privacy law that applies), not as a country the law is offered to or restricted to; I read them as `every store`, as part RD1-3 read S02-SA-209 (Salla's policy and Saudi Arabia's laws) under S02-VP-09's every-store row, S02-V-149.

### Revisit S02-V-218 (shopify, S02-VP-19, the store's data)

Replaced: `not covered` became three answer rows:
- S02-V-218, every store, 'Shopify's collection, use, disclosure and processing of your personal information is governed by our Merchant Privacy Policy.' (S02-SH-613, S02-SH-614, S02-SH-615, S02-SH-618, S02-SH-619, S02-SH-622, S02-SH-624);
- S02-V-242 (added), the merchant's location or residence, 'including such laws that apply based on the location or residence of Merchant and/or Your Customer(s).' (S02-SH-621, S02-SH-623, S02-SH-625, S02-SH-717);
- S02-V-243 (added), where the person whose data it is is located, 'If you are located in Canada or the United States, your Personal Data is received by: Shopify Inc.' (S02-SH-617, S02-SH-616); the reading that the Privacy Policy's 'you' includes the merchant is marked as mine in its basis_evidence, as part RD1-4 read S02-WC-073.

Leads placed under another point of (c): S02-SH-626 joined S02-V-101 (S02-VP-08: 'Shopify's primary contracting entity with merchants in EMEA ... and LATAM'); S02-SH-614 also joined S02-V-105 (S02-VP-09, every store: the terms every merchant accepts before signing up). Leads noted:
- S02-SH-620 (c): Appendix C applies 'Where the processing of Personal Data under this DPA is subject to data protection requirements in the European Economic Area': its decider is the law's reach over the processing, not the store's own country; in S02-VP-19's note
- S02-SH-713 (c): the admin shows 'the primary location where Shopify stores your store data, order data, and customer personal data'; names no decider (rule 4)
- S02-SH-714 (c): the admin shows 'information about the geographic storage location of your data'; names no decider (rule 4)
- S02-SH-716 (c): two stores' 'Data storage hosting location', observed as 'United States'; names no decider (rule 4)
- S02-SH-718 (c): 'The GDPR doesn't require personal data to be processed or stored in Europe' and protects 'personal data of European residents transferred outside of Europe': its decider is the residence of the persons whose data it is, not the store's own country; in S02-VP-19's note

### Rereads (shopify, (c)), noted by part RD1-3 under rule 2, since widened

Placed, joined to S02-V-108 (S02-VP-10, documents and checks, the business entity's country code): S02-SH-441, S02-SH-442, S02-SH-443, S02-SH-444, S02-SH-445, S02-SH-446 and S02-SH-448, whose scope names the call's business entity ('its business entity 'My Store - entity' (196406207); the call's countryCode YE'), and S02-SH-267, whose identifier is the legal entity's field ('legalEntity.governmentIdentifiers') and whose scope is the legal entity's schema ('jurisdiction YE, legalEntityType default_company'); its source's file is S02-SH-448's, from another run. That the call's country code is the business entity's is my reading of the scope, marked in S02-V-108's basis_evidence. Their earlier notes stay.

Left noted: S02-SH-465 ('threeDSecureEligibilityForCountry'): its words, its identifier and its scope, a list of stores and plans, don't say whose country.

### Place tasks: salla (c)

Placed: S02-SA-312 joined S02-V-152 (S02-VP-10; the Arabic of S02-SA-284's words); S02-SA-313 joined S02-V-151 (S02-VP-10; the question 'store-country'); S02-SA-314 joined S02-V-162 (S02-VP-14) and S02-V-150 (S02-VP-09), as Salla's English of S02-SA-147, which part RD1-3 placed in both; S02-SA-315 joined S02-V-159 (S02-VP-13), by its scope, Kuwait's and the UAE's payout articles, as part RD1-3 read S02-SA-145 and S02-SA-150. Noted:
- S02-SA-316 (c): 'Your settlement terms and merchant fees follow your agreement with Tabby', and Tabby's payments 'are collected through Tabby rather than Salla Payments': its decider is the merchant's agreement with Tabby and the payment method, not the store's own country (rule 4); in S02-VP-13's note
- S02-SA-317 (c): Tamara settles its orders 'according to the agreement between Tamara and the store': its decider is that agreement, not the store's own country (rule 4); in S02-VP-13's note
- S02-SA-376 (c): the consumer's right under the Saudi E-commerce Law to withdraw within seven days of receiving the product: a buyer's right of return, which fits none of (c)'s kinds of thing bound, and names no decider (rule 4)
- S02-SA-383 (c): 'The law entitles the consumer to return a product ... within 7 days of the purchase date': as S02-SA-376
- S02-SA-384 (c): '5. إضافة سياسة الاستبدال والاسترجاع' (my translation: 5. add an exchange and return policy), a step of an article on the Saudi E-commerce Law: names no decider (rule 4), and returns fit none of (c)'s kinds
- S02-SA-385 (c): '5. Add exchange and return policy': as S02-SA-384
- S02-SA-425 (c): 'Saudi E-commerce law requires a verified store address' under 'Set your pickup location', where 'carriers will pick up orders': a place the store ships from (rule 1); and its other text's key, 'uae_desc', names a country without saying whose (rule 2)

### Place tasks: shopify (c)

Placed (joined to a row unless said): S02-SH-593 joined S02-V-128, S02-V-135, S02-V-138 and S02-V-145 (S02-SH-248's list); S02-SH-602 joined S02-V-142; S02-SH-612 joined S02-V-143, S02-V-113 and S02-V-121, and is a new row under S02-VP-14, S02-V-244 ('pricing and payment options can differ depending on where your business is based'); S02-SH-630, S02-SH-631, S02-SH-633 and S02-SH-637 are a new row under S02-VP-11, S02-V-245 ('Your Shopify Payments account must be located in one of the following countries'; that the account's location is where the merchant's business is is my reading, marked there); S02-SH-636 and S02-SH-641 joined S02-V-119; S02-SH-639 joined S02-V-110; S02-SH-642 joined S02-V-112; S02-SH-644 and S02-SH-645 joined S02-V-108; S02-SH-650 joined S02-V-137; S02-SH-699 and S02-SH-700 joined S02-V-127; S02-SH-701 joined S02-V-113 and S02-V-121; S02-SH-702 joined S02-V-130; S02-SH-705 joined S02-V-143; S02-SH-709 joined S02-V-115. Noted:
- S02-SH-594 (c): the Terms of Service 'require you to maintain an accurate location', and the store address 'updates to match your new business entity address and country': what fills and changes the store's own country, (a) and (b), not a thing bound to it
- S02-SH-651 (c): additional tax fields in early access, by 'Destination is Chile' and the like: the shipping destination, a buyer's country, not the store's own country (rule 1); in S02-VP-16's note
- S02-SH-692 (c): 'The Shopify Plus plan pricing varies depending on the term and your billing currency': its deciders are the term and the billing currency, outside rule 1's table (rule 4), and its table's 'Available countries' don't say whose country (rule 2); in S02-VP-14's note
- S02-SH-710 (c): 'the physical location where the POS device is logged in determines the entity': a place the store sells at (rule 1), not the store's own country
- S02-SH-712 (c): 'you must have a separate entity for each country with retail locations': the retail locations' countries, places the store sells at (rule 1)

Placed, continued: S02-SH-733 joined S02-V-242; S02-SH-823 joined S02-V-137; S02-SH-825 joined S02-V-245; S02-SH-858 joined S02-V-120; S02-SH-869 and S02-SH-870 are a new row under S02-VP-17, S02-V-246 ('SMS notifications are supported only when your business address is in one of the following countries'); S02-SH-883 joined S02-V-146; S02-SH-891 joined S02-V-138; S02-SH-921 is a new row under S02-VP-18, S02-V-247 ('The entity assigned to each retail location determines the currency for Shopify POS at that location'). Noted:
- S02-SH-855 (c): 'you must follow the payment rules for the country you're processing the transaction in': the country of an in-person sale, a place the store sells at (rule 1); in S02-VP-11's note
- S02-SH-856 (c): 'To accept in-person POS payments in multiple countries, you must create a separate Shopify store and Shopify Payments account for each additional country': the countries of in-person sales, places the store sells at (rule 1); in S02-VP-11's note
- S02-SH-859 (c): in-person country requirements don't apply to sales 'using a payment solution other than Shopify Payments' or at locations 'that don't accept payments': its deciders are the payment solution and the location's use (rule 4); in S02-VP-11's note

Placed, continued: S02-SH-931 joined S02-V-137; S02-SH-932 joined S02-V-142; S02-SH-933 joined S02-V-138; S02-SH-935 is a new row under S02-VP-18, S02-V-248 ('Cash rounding rules might apply automatically at checkout depending on your store's location'); S02-SH-953 and S02-SH-954 joined S02-V-242. Noted:
- S02-SH-923 (c): 'the entity for that location must use a default payout currency that matches the country and currency requirements for that country': the country of a retail location, a place the store sells at (rule 1); in S02-VP-11's note
- S02-SH-928 (c): 'In France, Spain, Italy, Germany, and Sweden, a return or exchange ... must be processed by the same legal entity as the original sale', for Shopify POS there: the countries of retail sales, places the store sells at (rule 1); and returns fit none of (c)'s kinds
- S02-SH-930 (c): 'You can't sell product bundles in Shopify POS for retail locations in Spain': a retail location, a place the store sells at (rule 1); in S02-VP-17's note
- S02-SH-936 (c): additional cash rounding rules for 'new stores created on or after July 6, 2026' and stores 'that set up their first retail location in a listed country': the store's creation date (rule 4) and a retail location (rule 1); in S02-VP-18's note
- S02-SH-942 (c): 'Automatic receipt printing is on by default for Shopify POS locations in Italy': a POS location, a place the store sells at (rule 1); in S02-VP-18's note
- S02-SH-950 (c): 'A $2.15 USD monthly charge applies to each approved toll-free number used for SMS marketing in the United States and Canada': where the number is used, not the store's own country (rule 4); in S02-VP-14's note

Placed, continued: S02-SH-956 is a new row under S02-VP-17, S02-V-249, every store ('There are no specific country requirements for your store's location'); S02-SH-959 and S02-SH-971 joined S02-V-127; S02-SH-964 joined S02-V-141; S02-SH-965, S02-SH-966 (its list's next run, rule 5, Lists), S02-SH-968, S02-SH-969 and S02-SH-970 joined S02-V-142. Noted:
- S02-SH-960 (c): 'You're charged based on the number of SMS marketing messages sent to each recipient': its decider is the messages and their recipients (rule 4); its example's 'if you're located in Denmark' doesn't say the location decides the charge; in S02-VP-14's note

Rows compared with a statement of their own platform were rechecked under rule 5: each joined statement names its row's decider in its own words, or, where said, by its scope.

## Second pass, RD1-S1

Part RD1-S1 of the second pass: the tasks of `b/second-pass/RD1/worklist.tsv` under (a), (b) and (d), for Shopify, Salla, Zid, WooCommerce and BigCommerce.

### Revisits S02-V-089, S02-V-090 and S02-V-091 (bigcommerce, S02-VP-05, S02-VP-06 and S02-VP-07)

S02-V-089 (S02-VP-05, who checks): `gap` (S02-BC-G01) became an answer row, S02-V-089, 'validating the VAT number with the issuing country' (S02-BC-277): the account's VAT number is the merchant's tax registration, which rule 1 counts as the store's own country; that BigCommerce ('We', in the error message its identifier quotes) validates it with the issuing country is my reading, marked in its basis_evidence. Beside it, a `gap` row, S02-V-250, with S02-BC-G09, which asks who checks the default country, the country defined at sign-up or the hosting region, which the answer doesn't give. S02-BC-G01 was settled by gap-closing and goes.

S02-V-090 (S02-VP-06, who changes): `gap` (S02-BC-G02) became two answer rows: S02-V-090, 'the Manage Settings permission must be enabled on your user account' (S02-BC-261), and S02-V-251 (added), 'Information & Settings | modify | `store_v2_information`' (S02-BC-207, S02-BC-205, S02-BC-206), the OAuth scope of Update Locale Settings, which updates store_country. The seller's answer was already S02-V-099's: S02-BC-254, S02-BC-251, S02-BC-260 and S02-BC-282 joined it. 'default country' is BigCommerce's term for 'The country your store is run from' (terms.tsv; S02-BC-263), so it passes the role test.

Placed under another point of (b), S02-VP-04 (who sets), as S02-BC-110's 'configure' was read in the first pass under both: S02-BC-260 ('manage') joined S02-V-088 (the seller); S02-BC-261 is a new row, S02-V-252 (the Manage Settings permission); S02-BC-206 is a new row, S02-V-253, 'default: United States', a default the platform sets (rule 4).

S02-V-091 (S02-VP-07, what must hold before it changes): `gap` (S02-BC-G02) became an answer row, S02-V-091, 'you can adjust these settings at any time' (S02-BC-251). Its other leads are placed under S02-VP-06 (S02-BC-207, S02-BC-254, S02-BC-261) or noted below (S02-BC-264, S02-BC-272). A call the brief left to me: as in the first pass (S02-SH-255 and S02-SH-266's permissions under S02-VP-06, its feature under S02-VP-07), a permission or scope that must be held is placed under who changes, not under what must hold.

Leads noted (b):
- S02-BC-212 (b): `country` is the 'Country where the store is located (as defined during the store sign-up process)': it says when the country is defined, not who sets, checks or changes it (rule 2)
- S02-BC-217 (b): the Information & Settings scope manages 'store profile contact details, date and time preferences, and default language': it doesn't name the store's country (rule 2)
- S02-BC-257 (b): channel-specific localization settings, edited with the Edit Channels permission: a channel's settings, not the store's country, which S02-BC-100 says channel-specific overrides can't modify (rule 2)
- S02-BC-259 (b): 'You can manage store information globally from Settings › Store profile': the store information it names is 'the basic contact information ... such as the store name and email address', not the store's country (rule 2)
- S02-BC-264 (b): 'To view and manage your store’s settings, the Manage Settings permission must be enabled': the Store Settings page, which S02-BC-110 names for 'physical dimensions and date and timezone settings', apart from the Locale settings in Store Profile; it doesn't name the store's country (rule 2)
- S02-BC-266 (b): 'The Store Owner or a System Admin can create or delete users and grant permissions': who grants staff permissions, not who sets, checks or changes the store's country (rule 2)
- S02-BC-267 (b): what the Manage Settings permission gives access to, 'Product Filtering, Store Settings, Checkout, ...': it doesn't name the store's country (rule 2)
- S02-BC-268 (b): the Edit Channels permission edits 'channel settings and additional storefronts': a channel's settings, not the store's country (rule 2)
- S02-BC-269 (b): 'Only the store owner user can grant high-risk permissions': who grants permissions, not the store's country (rule 2)
- S02-BC-270 (b): the Store Owner role 'Includes all permissions' and 'is the person financially responsible for the account': it doesn't say the role gates the store's country (rule 4)
- S02-BC-272 (b): 'Once you have selected a hosting region for your trial store, it cannot be changed': the hosting region, where the platform hosts the store, which rule 1 keeps out; in S02-VP-06's and S02-VP-07's notes
- S02-BC-273 (b): 'Make sure that you are entering your actual business information in the form instead of placeholder data': it names no one who checks, and not the store's country (rule 2)
- S02-BC-274 (b): a mismatch 'with the country, date, or time settings between your browser and your store information', a possible cause of a trial-creation error: it names no one who checks the store's country (rule 2)
- S02-BC-283 (b): 'Our system uses your device's IP address to determine the zip code of your location when attempting to make a payment': a check of the place a payment is made from, against the billing address, not a check of the store's country (rule 2)

### Revisit S02-V-026 (shopify, S02-VP-03, the countries the platform serves)

Replaced: `not covered` became an answer row, S02-V-026, 'Shopify is available in nearly every country in the world' (S02-SH-612), the answer to 'In what countries can I use Shopify?'. Its one lead is placed.

### Revisit S02-V-084 (woocommerce, S02-VP-05, who checks)

Replaced: `gap` (S02-WC-G02) became an answer row, S02-V-084, 'Verify your business details with our payments partner, Stripe.' (S02-WC-258, S02-WC-257, S02-WC-260, S02-WC-261); added S02-V-254, 'The location argument must be a valid ISO3166 alpha-2 country code.' (S02-WC-262), the platform's code checking the business location's form, by S02-WC-224's description of the same REST routes' location; and a `gap` row beside them, S02-V-255, with S02-WC-G06, which asks whether the country itself is checked beyond its form, which the answers don't give. S02-WC-511 ('we use an embedded iframe from Stripe to verify information about you and your business') joined S02-V-098 (WooCommerce, with Stripe). S02-WC-259 ('Where is your business located?') is placed under another point of (b): it joined S02-V-082 (S02-VP-04, the seller sets it). S02-WC-G02 was settled by gap-closing (S02-WC-G06 replaces it) and goes. Leads noted:
- S02-WC-512 (b): a test account 'requires no personal information' and 'will only operate in test mode': it names neither the store's country nor who checks it (rule 2)

### Revisit S02-V-038 (zid, S02-VP-02, the countries kept out)

Replaced: `not covered` became `gap`, S02-V-038, with S02-ZD-G09, which asks which countries, if any, Zid keeps out of creating a store. The revisit had no lead.

### Rereads (shopify, salla and zid, (a), (b) and (d)), noted by parts RD1-1 and RD1-3, since widened

Placed, under rule 5's identifier or scope:
- S02-SH-259, under (a): joined S02-V-006 (S02-VP-01): its identifier, 'combobox "I'm located in:"', names the field its words list the options of
- S02-SH-260, under (a): joined S02-V-001 (S02-VP-01): its identifier, 'Add business entity, country', names the business entity's country
- S02-SH-396, under (a) and (b): joined S02-V-001 (S02-VP-01) and S02-V-053 (S02-VP-04, the seller): its identifier names the admin's form that creates business details, whose first control is the button 'Yemen'
- S02-ZD-148, under (a): a new row, S02-V-256 (S02-VP-01), 'required: - country - city': its identifier names the record, 'user.business_location (DefaultStoreLocationSerializer)'

Already placed: S02-SH-260 under (b), in S02-V-053 (S02-VP-04), by the first pass; no change.

Left noted (their earlier notes stand):
- S02-SA-249 (a): its identifier places the country in 'default_branch', a branch, which rule 1 keeps out of the store's own country
- S02-SH-259 (d): its identifier names the field where the merchant gives their location, not where Shopify serves merchants
- S02-SH-441 (b): its scope now says whose country, the business entity's, but it names no one who sets, checks or changes it, nor a condition on its change
- S02-SH-448 (b): its scope now says whose country, but its words give the fields' requirements ('"required":true', '"validations":null'), and name no one who sets, checks or changes it, nor a condition on its change
- S02-ZD-148 (b): its identifier names the business location, but it names no one who sets, checks or changes it ('is_address_confirmed' is a field's name), nor a condition on its change
- S02-ZD-149 (a): its identifier says whose profile, the account user's ('GET /v1/managers/account/profile > user.user_profile_data'), but not that its 'country' is where the merchant is based, registered or resident

### Note task (zid, (a))

- S02-ZD-180 (a): They quote the Saudi Terms that zid.eg's Terms page holds in its raw HTML. The page's scripts replace them with the Terms of شركة زد مصر, under Egyptian law, so the page doesn't show these words (`method-report.md`, section 9). The statements recorded from the page as shown take their place.

### Place tasks: bigcommerce (a) and (b)

Placed under S02-VP-01 (a): S02-BC-206 and S02-BC-205 joined S02-V-048 (store_country, the same key); S02-BC-210 joined S02-V-050 ('store_address / Store Address', one term in terms.tsv); new rows: S02-V-257, '`country` ... Country where the store is located' (S02-BC-212); S02-V-258, '`country_code`' (S02-BC-213); S02-V-259, '`address` ... Display address.' (S02-BC-216); S02-V-260, 'Default country — The country your store is run from' (S02-BC-263, S02-BC-262, S02-BC-265, S02-BC-251, S02-BC-260); S02-V-261, 'Provide your VAT Number and Issuing Country' (S02-BC-277, S02-BC-275), the country of the merchant's tax registration; S02-V-262, 'your BigCommerce account's address' (S02-BC-282); S02-V-263, 'Address — The physical address of your store or place of business' (S02-BC-310). Under (b): S02-BC-275 joined S02-V-099 (S02-VP-06, the seller); S02-BC-276 is a new row, S02-V-264 (S02-VP-06), 'To access the Account Dashboard, you must be the store owner.'

A call the brief left to me: `country` and `country_code` of Get Store Information are two fields, so two rows (rule 4, (a)); whether the store profile's 'Address' (S02-BC-310) is the 'Store Address' of S02-V-050 isn't stated, so it is its own row.

Noted (a):
- S02-BC-188 (a): a webhook that 'Fires when any of the global store profile settings are updated': it doesn't name the field or record that holds the store's country (rule 2)
- S02-BC-208 (a): the locale settings, 'used to give shopper information about languages, countries, etc.': it doesn't say which country is the store's own (rule 2)
- S02-BC-209 (a): 'If omitted, you will interact with the global settings only': a query parameter, which names no country (rule 2)
- S02-BC-211 (a): `store_address_type`, 'Home Office', 'Commercial Office', 'Retail', 'Warehouse': the address's type, not what holds the country (rule 2)
- S02-BC-214 (a): 'The infrastructure region where the store is located', to compare 'against GCP regions': where the platform hosts the store, which rule 1 keeps out; in S02-VP-01's note
- S02-BC-215 (a): Get Store Information 'Returns metadata about the global settings for a store': it names no country (rule 2)
- S02-BC-235 (a): regional hosting 'for merchants interested in hosting their stores in Europe or the Asia-Pacific (APAC) region': where the platform hosts the store, which rule 1 keeps out; in S02-VP-01's note
- S02-BC-256 (a): 'configure the default country ... separately per channel' for additional storefronts: a storefront's country, a market the store sells into, not the store's own country (rule 1); in S02-VP-01's note
- S02-BC-258 (a): 'The store profile provides basic information about your business': it doesn't name the store's country (rule 2)
- S02-BC-259 (a): the store profile's 'basic contact information ... such as the store name and email address': it doesn't name the store's country (rule 2)
- S02-BC-271 (a): the trial form's fields, 'your name, email address, a password, store name, the size of your business, and the region your store should be hosted': no country of the store; the hosting region, which rule 1 keeps out; in S02-VP-01's note
- S02-BC-272 (a): the hosting region, which 'cannot be changed': where the platform hosts the store, which rule 1 keeps out; in S02-VP-01's note
- S02-BC-274 (a): 'There may be a mismatch with the country, date, or time settings between your browser and your store information', a possible cause of an error: it doesn't name the field that holds the store's country (rule 2)
- S02-BC-293 (a): 'Your Timezone — the timezone where you are located': a timezone, not a country, address or jurisdiction (rule 1)
- S02-BC-294 (a): stores under one account 'share the same contact and billing information': it names neither the store's country nor an address (rule 2)
- S02-BC-308 (a): 'Go to Settings › Store profile to update or change your store's contact information': it doesn't name the store's country or address (rule 2)
- S02-BC-311 (a): 'Address type — Specifies whether the above address is a home or commercial office, retail store, or warehouse': the address's type, not what holds the country (rule 2)

Noted (b):
- S02-BC-221 (b): 'You will provide true, accurate, current, and complete information when registering for an Account': it doesn't name the store's country or an address (rule 2)
- S02-BC-222 (b): 'Commerce reserves the right to refuse registration of, or cancel, accounts that violate this Agreement': a refusal for a violation, not who sets, checks or changes the store's country (rule 2)
- S02-BC-243 (b): 'your default currency is assigned based on your location': it names no one who sets, checks or changes the location (rule 2)

### Place tasks: salla (a), (b) and (d)

Placed: S02-SA-311 and S02-SA-422 joined S02-V-015 (S02-VP-01, 'موقع المتجر', the store's location), and S02-SA-311 also S02-V-095 (S02-VP-06, the seller); S02-SA-312 and S02-SA-313 joined S02-V-013 (S02-VP-01, the Arabic and the API of S02-SA-284's onboarding question) and S02-V-072 (S02-VP-04, the seller); S02-SA-318 joined S02-V-024 (S02-VP-03, the UAE); S02-SA-430 joined S02-V-012 (store_country) and S02-V-018 (country), as S02-SA-292 is in both.

A call the brief left to me: S02-SA-311 and S02-SA-422 say the store's location is updated 'from the branches and warehouses page'. Rule 1 keeps out a branch or warehouse, and lets the statement's own words decide: theirs don't say orders ship from the store's location or stock is kept in it, so I placed them with S02-V-015. S02-SA-423, which says branches and warehouses 'ship orders to customers', is noted.

Noted:
- S02-SA-312 (d): the options of the store-country question, 'من أي دولة تسجِّل متجرك؟' (my translation: from which country do you register your store?), 'دولة أخرى' (my translation: another country) among them: their words don't say the countries are where Salla serves merchants, as S02-SH-259's options were read under (d)
- S02-SA-313 (d): the same question's options, from the onboarding's API ('"slug": "store-country"'): as S02-SA-312
- S02-SA-357 (a): the address of the store's main, default branch, 'بيانات الفرع الرئيسي (الإفتراضي) لمتجرك' (my translation: the data of your store's main, default branch): a branch, which rule 1 keeps out; in S02-VP-01's note
- S02-SA-360 (a): a tax record's country, for which the seller will 'select which markets the record applies to': a tax registration its own words tie to markets the store sells into (rule 1); in S02-VP-01's note
- S02-SA-421 (a): 'Choose the country, address, postal code, street, and district', for a branch or warehouse: a branch or warehouse, which rule 1 keeps out; in S02-VP-01's note
- S02-SA-423 (a): branches and warehouses, 'used to define working hours, display store locations, and ship orders to customers': places the store ships from, which rule 1 keeps out; in S02-VP-01's note

### Place tasks: shopify (a) and (b)

Placed under S02-VP-01 (a): S02-SH-591, S02-SH-644 and S02-SH-881 joined S02-V-001 (business details, the business entity); S02-SH-593, S02-SH-760, S02-SH-882, S02-SH-885, S02-SH-886 and S02-SH-891 joined S02-V-002 (the store address); S02-SH-598, S02-SH-627 and S02-SH-886 joined S02-V-003 (the billing address); S02-SH-600 joined S02-V-006 ('I'm located in'); S02-SH-702 joined S02-V-007 (an accurate location); S02-SH-599 is a new row, S02-V-265, the sign-up's '"storeCreatePayload": {... "country": "YE"'.

Placed under (b): S02-SH-592, S02-SH-594, S02-SH-599, S02-SH-600, S02-SH-644, S02-SH-702 and S02-SH-881 joined S02-V-053 (S02-VP-04, the seller); S02-SH-594, S02-SH-595, S02-SH-602, S02-SH-702, S02-SH-881 and S02-SH-895 joined S02-V-059 (S02-VP-06, the seller); S02-SH-595 and S02-SH-884 joined S02-V-065 (S02-VP-07, deactivating financial services); S02-SH-598 joined S02-V-067 (S02-VP-07, the billing address's country matches an entity's: its Country/region is disabled beside the selected entity). New rows: S02-V-266 (S02-VP-05), 'Business entity information is sent to assessors to verify your business.' (S02-SH-589); S02-V-267 (S02-VP-07), 'Adding new business entities or making changes might require additional verification.' (S02-SH-590, S02-SH-596); S02-V-268 (S02-VP-06), 'You can't change the business type, country, or the person associated with individual or sole proprietor entities.' (S02-SH-596); S02-V-269 (S02-VP-06), 'you might need to contact Shopify Support to change a store's default business entity' (S02-SH-597); S02-V-270 (S02-VP-04), 'Your user role might not have the View permission for Business entities.' (S02-SH-601).

Calls the brief left to me: 'manage' and 'maintain' are read as both setting and changing (S02-SH-594, S02-SH-702, S02-SH-881), as S02-SH-013 is in both S02-V-053 and S02-V-059; S02-SH-601's 'View permission for Business entities' is its own row, since nothing quoted shows it is S02-V-055's 'VIEW_LEGAL_ENTITIES'; S02-SH-599's store-creation payload is its own row under (a), a record apart from the sign-up's field 'I'm located in:' (S02-V-006).

Noted (b):
- S02-SH-591 (b): it lists what the business entity must include, 'The country your business is operating from' among them: no one who sets, checks or changes it, and no condition on its change (rule 2)
- S02-SH-593 (b): 'Changing the store country creates a new business entity and might affect the following details': what a change does, not who makes it or what must hold before it (rule 2)
- S02-SH-627 (b): 'Before creating a new store in your organization, your main store must have ... a complete billing address': a condition on creating an expansion store, not on setting or changing the store's country; it names no party (rule 2)

### Place tasks: woocommerce (a) and (b)

Placed under S02-VP-01 (a): S02-WC-245 and S02-WC-385 joined S02-V-040 (the base country); S02-WC-267 joined S02-V-041 (Business location); S02-WC-388 and S02-WC-397 joined S02-V-039 (Store Address, woocommerce_default_country); new rows: S02-V-271, '“Stripe Account Country” means the country or region User selected when opening User’s Stripe Account' (S02-WC-228); S02-V-272, 'You may provide us with more information — like your address' (S02-WC-235), the WordPress.com account's address; S02-V-273, 'Where is your business located?' (S02-WC-259); S02-V-274, 'Where is your store located?' (S02-WC-294, S02-WC-322).

Placed under (b): S02-WC-228, S02-WC-243, S02-WC-292, S02-WC-294 and S02-WC-322 joined S02-V-082 (S02-VP-04, the seller); S02-WC-293 joined S02-V-083 (S02-VP-04, the platform: its code saves the setting when the profiler is skipped); S02-WC-322 joined S02-V-085 (S02-VP-06, the seller); S02-WC-230 joined S02-V-086 (S02-VP-06, no one: 'there isn’t a way to update the country'); S02-WC-231 joined S02-V-084 (S02-VP-05, Stripe); S02-WC-240 and S02-WC-295 joined S02-V-254 (S02-VP-05, the platform's code); new rows under S02-VP-06: S02-V-275, "wc_rest_check_manager_permissions( 'settings', 'edit' )" (S02-WC-241), and S02-V-276, 'Migrate the state code for the store location.' (S02-WC-242), the platform.

Calls the brief left to me: the onboarding's questions 'Where is your store located?' and 'Where is your business located?' are their own rows under (a), since nothing quoted says which field stores their answers; S02-WC-295's geolocation notice is a check of the store's country by the platform's code, joined with its form checks in S02-V-254.

Noted (a):
- S02-WC-229 (a): WooPayments creates 'a special kind of Stripe account ... called a Stripe Express account': it names no country (rule 2)
- S02-WC-236 (a): the Ecommerce Services need a WordPress.com account and, for some, 'your site URL': it names no country or address (rule 2)
- S02-WC-237 (a): 'We may determine the approximate location of your device from your IP address': a device's location, not a country held as where the store or its merchant is based (rule 1)
- S02-WC-238 (a): information 'relating to your Stripe account, such as your email address and phone number': it names no country or address (rule 2)
- S02-WC-247 (a): the entity 'depends on where you reside and which Services you use': it names the merchant's residence, but not the field or record that holds it (rule 1, (a))
- S02-WC-249 (a): 'the billing country associated with your payment method' and 'your detected location': a payment method's billing country and a detected location, neither said to be where the store or its merchant is based (rule 1)
- S02-WC-250 (a): 'You must provide accurate and up-to-date payment information': it names no country or address (rule 2)
- S02-WC-382 (a): the Point of Sale's 'Physical address' ('woocommerce_pos_store_address'): a place the store sells at, which rule 1 keeps out; in S02-VP-01's note

Noted (b):
- S02-WC-232 (b): reasons to delete a WooPayments account, 'the wrong country was chosen' among them: not who sets, checks or changes the country, nor what must hold before it changes (rule 2)
- S02-WC-233 (b): 'WooPayments accounts can only be deleted by our support staff': who deletes the account, not who changes its country (rule 2)
- S02-WC-234 (b): when an account can be deleted: not the store's country (rule 2)
- S02-WC-239 (b): "add_action( 'update_option_woocommerce_default_country', ... )": a hook alone names no party (rule 4)
- S02-WC-244 (b): it sets the store's currency and units from '$country_info': not who sets, checks or changes the country (rule 2)
- S02-WC-250 (b): 'You must provide accurate and up-to-date payment information': it names no country or address (rule 2)
- S02-WC-251 (b): 'you agree to provide us with complete and accurate information and to keep the information current': it names no country or address (rule 2)
- S02-WC-252 (b): 'We may limit your access ... until we’re able to verify your account information, like your email address': it doesn't name the store's country (rule 2)
- S02-WC-296 (b): 'Setting up your store in the wrong country may lead to the following issues:': what a wrong country leads to, not who checks or changes it (rule 2)
- S02-WC-313 (b): the legacy wizard takes a currency by country ('$currency_by_country'): not the store's country's setter (rule 2)
- S02-WC-314 (b): 'Before changing the currency, confirm that your payment gateway supports it': the currency, not the store's country (rule 2)

## Second pass, RD1-S3

Part RD1-S3 of the second pass: the tasks of `b/second-pass/RD1/worklist.tsv` under (c) for Zid, WooCommerce and BigCommerce.

### Revisit S02-V-226 (bigcommerce, S02-VP-10, documents and checks)

Replaced: `not covered` became `gap`, S02-V-226, with S02-BC-G06, which asks which documents or checks the merchant provides and what decides them. No lead names a decider. Its leads noted:
- S02-BC-218 (c): the Actions section shows tasks 'such as completing your profile, linking a bank account, Know Your Customer (KYC) status': a check, with no decider named (rule 4); its scope is BigCommerce Payments, not every store
- S02-BC-219 (c): an 'Account verification pending' banner until the account or business profile is complete: names no decider (rule 4)
- S02-BC-220 (c): 'Funds may be held or blocked for several reasons, depending on different factors ... complete any requests for documents or verification': names no decider (rule 4)

### Revisit S02-V-233 (bigcommerce, S02-VP-13, payouts)

Replaced: `not covered` became an answer row, S02-V-233, 'Your first payout might take longer, depending on your industry risk level and country of operation.' (S02-BC-223, Stripe OCS): 'country of operation' is in rule 1's store's own country; that the first payout's timing is how the merchant is paid is my reading, marked there, as WooCommerce's S02-V-203 ('how often your balance will be paid out depending on your business location'). Its leads noted:
- S02-BC-224 (c): 'payouts to your account are settled in your default currency': its decider is the store's default currency, outside rule 1's table (rule 4); in S02-VP-13's note
- S02-BC-225 (c): 'The merchant can set their settlement currency through its payment provider': the merchant's choice, not the store's own country (rule 4); in S02-VP-13's note
- S02-BC-226 (c): 'If the shopper’s card-issuing bank differs from the merchant's bank account country, additional cross-border fees may apply': the shopper's card-issuing bank and the bank account's country, neither in rule 1's table (rule 4); in S02-VP-13's note
- S02-BC-227 (c): 'view the linked bank account and set up automatic payouts to your bank or PayPal account': names no decider (rule 4)
- S02-BC-228 (c): 'By default, automatic payouts are transferred to your PayPal account. To switch to a bank account, click Change': the default and the merchant's choice, not the store's own country (rule 4); in S02-VP-13's note
- S02-BC-229 (c): 'For new BigCommerce Payments accounts, initial payments are held for up to 21 days': its decider is the account's age (rule 4); in S02-VP-13's note
- S02-BC-230 (c): 'The Fast option for a manual payout is subject to a fee of 1.50%': its decider is the payout option (rule 4); in S02-VP-13's note
- S02-BC-231 (c): the Money dashboard's 'multi-currency balances in GBP, EUR, and more': names no decider (rule 4)

### Place tasks: zid (a), (b) and (d)

Placed: S02-ZD-226 is a new row under S02-VP-01, S02-V-277, 'و إضافة العنوان' (my translation: and add the address), the address the account settings hold for their user, as S02-WC-235's account address is read (S02-V-272); S02-ZD-173 joined S02-V-078 (S02-VP-06, the merchant moves the store), S02-V-080 (S02-VP-07, the wallet's balance zeroed first) and S02-V-081 (S02-VP-07, a request through customer service); S02-ZD-184 joined S02-V-035 (S02-VP-03, Egypt: the Arabic of its words); S02-ZD-444 joined S02-V-033 (S02-VP-03, the Gulf states: 'فالخليج', my translation: in the Gulf); new rows under S02-VP-03: S02-V-278, 'المنصّة المتكاملة للتجارة الإلكترونية في الشرق الأوسط وشمال أفريقيا' (S02-ZD-185; my translation: the integrated e-commerce platform in the Middle East and North Africa); S02-V-279, Kuwait (S02-ZD-386); S02-V-280, Oman (S02-ZD-387, S02-ZD-388).

A call the brief left to me: an address the account holds for its user (S02-ZD-226, S02-WC-235) is read as the merchant's address, in X's role, while a profile's bare 'country' (S02-ZD-149) stays noted, since a country in a profile may not be where the merchant is based or resident.

Noted:
- S02-ZD-183 (d): 'في المستقبل باذن الله نتوسع للعالم العربي' (my translation: in the future, God willing, we will expand to the Arab world): a future expansion, not the countries Zid serves merchants in (rule 2)
- S02-ZD-373 (a): the merchant's duty to comply with 'جميع القوانين المصرية المعمول بها الحاكمة لنشاطك التجاري' (my translation: all applicable Egyptian laws governing your business activity), in zid.eg's Terms: a law that applies, not the field or record that holds the store's country (rule 1, (a))
- S02-ZD-380 (a): zid.eg's Terms are governed by 'قوانين جمهورية مصر العربية' (my translation: the laws of the Arab Republic of Egypt): the terms' law, not the field or record that holds the store's country (rule 1, (a))
- S02-ZD-381 (a): 'الاختصاص الحصري للمحاكم المصرية المختصة' (my translation: the exclusive jurisdiction of the competent Egyptian courts): the terms' courts, not the field or record that holds the store's country (rule 1, (a))

### Candidates for a new point

None. Each question of (a), (b) and (d) already has its point (S02-VP-01 to S02-VP-07), and under these bullets every candidate of one question makes one point (rule 3), so no statement of this part answered a question for an X that no point fits. The statements whose X failed the role test (hosting regions, branches and warehouses, a Point of Sale's address, a channel's country, a tax record tied to markets) are noted above, not candidates.

### Searches

This part raised no point, so it searched for no earlier platform's rows (rule 3).

### Rechecks (part RD1-S1)

Rows compared with a statement of their own platform were rechecked under rule 5: each joined statement names its row's answer in its own words or, where said, by its identifier or scope, and keeps the row's basis (S02-BC-206 and S02-BC-210 by the same key or term as S02-V-048's and S02-V-050's; S02-SA-430 by S02-SA-292's keys).

### Revisit S02-V-236 (bigcommerce, S02-VP-15, taxes on the platform's fees)

Replaced: `not covered` became an answer row, S02-V-236, every store, 'All fees are exclusive of all applicable governmental fees, charges, or taxes' (S02-BC-232, S02-BC-234); and a `gap` row beside it, S02-V-281, with S02-BC-G10, which asks which taxes BigCommerce adds to its fees and what decides them, which the answer doesn't give. That 'US Sales, GST, VAT' (S02-BC-234) name the taxes excluded, not a country the prices are restricted to, is my reading, as part RD1-S2 read S02-V-219.

Leads placed under another point of (c), S02-VP-14 (the platform's fees), read as how BigCommerce's invoice is paid (my reading, marked in each row): S02-BC-280 is a new row, S02-V-282, the store's location ('your store is located in India, the payment must be made manually'); S02-BC-281 joined S02-V-234, the merchant's place ('Merchants in India must pay their invoice manually'), and is a new row, S02-V-283, the business's location ('If your business is located in India, you will be sent an email reminder'), one answer per decider as part RD1-4's problem 6 gives. Leads noted:
- S02-BC-233 (c): the merchant is 'solely responsible for payment of any and all taxes assessed as a result of you opting into unified billing': names no decider, and its scope, 'United States, United Kingdom, and Canada Only', doesn't say whose countries (as part RD1-4 noted S02-BC-071, of the same terms)
- S02-BC-278 (c): 'The methods available to pay your invoice can vary depending on your store’s plan and region': the plan is outside rule 1's table, and its words don't say the store's region is where the store is based rather than where it is hosted, which rule 1 keeps out (BigCommerce's terms hold 'infrastructure_region', 'The infrastructure region where the store is located'); in S02-VP-14's note
- S02-BC-279 (c): 'Form 1099-K is issued by your payments provider(s)': names who issues the form, not a decider (rule 4); its scope, 'US taxes', doesn't say whose country
- S02-BC-283 (c): a 'MAX 7' error 'when the geographic distance between your billing address and the location you are attempting to make a payment from is too great': a check on where an invoice's payment is made from, not a thing bound to the store's own country (rule 4); in S02-VP-14's note

### Revisit S02-V-237 (bigcommerce, S02-VP-16, the store's taxes)

Left `not covered` (rewritten with a note): no lead names a decider, and gap-closing recorded no gap and no absence for the point, so none of the brief's four replacements applies (a problem with the work list, below). Its leads noted:
- S02-BC-247 (c): 'If you have nexus in multiple states or local jurisdictions, the additional jurisdictions need to be adjusted from within your tax provider's account dashboard': names where they are adjusted, not a decider (rule 4); its words don't say the nexus is where the store is based or registered (rule 1)
- S02-BC-249 (c): 'Access your US 1099-K and other tax forms in your account’s portal': names where the forms are, not a decider (rule 4)
- S02-BC-250 (c): 'Your US 1099-K and other tax forms are provided by the payment processor': names who provides them, not a decider (rule 4)

### Revisit S02-V-239 (bigcommerce, S02-VP-18, the store's defaults)

Replaced: `not covered` became three answer rows and a `gap` row:
- S02-V-239, your location: 'When you first create your store, your default currency is assigned based on your location.' (S02-BC-243);
- S02-V-284 (added), the store's default country: 'To reset values to the standard formats for your store’s default country, click Set standard formats for [country].' (S02-BC-285, S02-BC-253); that the standard formats are defaults the platform sets from the store's country is my reading, marked there;
- S02-V-285 (added), where the store is based: 'If you create a new store based in one of the following countries, the store's content will be in your country's native language by default.' (S02-BC-288, with its list, S02-BC-289 to S02-BC-291, read with it by source and identifier, marked);
- S02-V-286 (added), `gap`, S02-BC-G11, which asks whether the units and the date and timezone settings take the default country's standard formats when the store is created, which the answers don't give.

Lead placed under another point of (c): S02-BC-253 ('The default country setting determines which payment methods are available to be set up on your store') is also in a new row under S02-VP-12, S02-V-287, with the place tasks S02-BC-263 and S02-BC-260 (below). Lead noted:
- S02-BC-244 (c): to change the default currency, add it, then 'click Action › Set as default': the merchant's choice, not the store's own country (rule 4); in S02-VP-18's note

### Place tasks: bigcommerce (c)

Placed: S02-BC-263 ('Default country — The country your store is run from, which determines the payment methods that are available for use with your store') and S02-BC-260 (the locale information's 'country where your store is located', whose settings 'allow you to access region-specific payment methods') are a new row under S02-VP-12, S02-V-287, with S02-BC-253: the default country, the field part RD1-S1 holds for the three under (a) in S02-V-260. Noted:
- S02-BC-258 (c): the store profile 'can affect which payment gateways are available': its words don't say the profile holds the store's country, nor which of its information affects the gateways, as part RD1-S1 noted it under (a) (rule 4)

### Revisit S02-V-240 (bigcommerce, S02-VP-19, the store's data)

Replaced: `not covered` became an answer row, S02-V-240, every store, 'We use this information as a Controller to provide Merchants with, support, and improve our services' (S02-BC-237, Merchants' information) with S02-BC-238 ('The Merchant is the Controller of this information', of Shoppers' information, Commerce acting 'as a Processor'): their words apply to all Merchants, with no country or scope. Its leads noted:
- S02-BC-235 (c): regional hosting 'available for merchants interested in hosting their stores in Europe or the Asia-Pacific (APAC) region rather than in the United States': the merchant's choice of where the store is hosted, which rule 1 keeps out of the store's own country, not a decider from its table (rule 4); in S02-VP-19's note
- S02-BC-236 (c): 'Commerce primarily utilizes Google Cloud’s U.S.-Central1 region as our primary data storage location': names where the data is held, not a decider (rule 4), as part RD1-S2 noted S02-SH-713
- S02-BC-239 (c): 'it may be necessary to transmit Personal Data outside of the country, state, or province where the data was collected/received': its decider is where the data was collected, not the store's own country (rule 4); in S02-VP-19's note
- S02-BC-240 (c): 'For third-country transfers outside of the EU/EEA we also use the Standard Contractual Clauses': its decider is the transfer's reach, as S02-SH-620 (rule 4); in S02-VP-19's note
- S02-BC-241 (c): 'This DPA applies when a Commerce Entity acts as a Processor on behalf of the Customer': its decider is the entity's role in the processing (rule 4); in S02-VP-19's note
- S02-BC-242 (c): 'Commerce.com may transfer, process and store Personal Data in regions in which Commerce.com or its Subprocessors operate': its decider is where Commerce.com and its subprocessors operate (rule 4); in S02-VP-19's note

### Revisit S02-V-194 (woocommerce, S02-VP-10, documents and checks)

Replaced: `not covered` became an answer row, S02-V-194, the onboarding's business types found by the country answered ('l=a.find(t=>"PR"===e.country?"US"===t.key:t.key===e.country)', S02-WC-263); and a `gap` row beside it, S02-V-288, with S02-WC-G07, which asks which documents or checks the business verification asks for, which the answer doesn't give. Two readings, marked there: that 'e.country' is the answer to the same step's 'Where is your business located?' (S02-WC-259, the same file, its identifier 'WooPayments onboarding, business step'), since its own words, identifier and scope don't say whose country; and that the business type is among what the merchant provides to verify the business. If the coordinator holds that the role test can't rest on another statement of the source, S02-WC-263 is noted instead, and the row is S02-V-288's gap alone.

### Revisit S02-V-200 (woocommerce, S02-VP-12, other payment providers)

Replaced: `not covered` became two answer rows:
- S02-V-200, the store's location: 'you are offered different payment gateways based on your store location' (S02-WC-265), with S02-WC-264 ('Shop location and currency are factors. A payment gateway company/processor may only serve merchants based in certain countries'), the same page; that 'Shop location' and 'store location' name one location is my reading, marked;
- S02-V-289 (added), the Payments settings' business location: '("Business location:","woocommerce")' (S02-WC-267), with the providers route's 'location', which 'Defaults to WooCommerce\'s base location country' (S02-WC-268); `term` with Shopify's 'Business location' (S02-SH-027); that the route's location is that field is my reading, by S02-WC-221.

Lead placed under another point of (c): S02-WC-265 ('different payment gateways based on your store location, which includes Core Payment Options and WooPayments') is also a new row under S02-VP-11, S02-V-290, the store's location, since it names WooPayments.

### Revisit S02-V-182 (zid, S02-VP-15, taxes on the platform's fees)

Replaced: `not covered` became an answer row, S02-V-182, every store, 'جميع الرسوم لا تشمل المبيعات الحكومية أو الإقليمية أو المحلية' (S02-ZD-194; my translation: all fees exclude governmental, regional or local sales [taxes]), with S02-ZD-193, S02-ZD-197 and S02-ZD-203, whose own words apply the tax to all tax charges, prices and plans; and a `gap` row beside it, S02-V-291, with S02-ZD-G08, which asks whether the store's country decides the tax on Zid's fees and what tax a store's fees carry outside Saudi Arabia, which the answer doesn't give. Its leads noted:
- S02-ZD-192 (c): 'قد تختلف رسوم الضرائب المحلية اعتمادًا على طريقة الدفع المستخدمة' (my translation: local tax charges may differ depending on the payment method used): its decider is the payment method (rule 4); in S02-VP-15's note
- S02-ZD-195 (c): Zid may charge the fees 'مثل الضرائب ورسوم المعاملات المحتملة، على طريقة الدفع التي اخترتها' (my translation: such as taxes and possible transaction fees, to the payment method you chose): names where the charges are taken, not a decider (rule 4)
- S02-ZD-196 (c): a service fee of 1 riyal '(غير شاملة لضريبة القيمة المضافة) لكل بوليصة شحن' (my translation: excluding VAT, per waybill) when the merchant links its own shipping company: names no decider of the tax, and its words don't apply it to all stores or fees (rule 4)
- S02-ZD-198 (c): the bank transfer fee '9 ريالات شاملة ضريبة القيمة المضافة للحوالات الداخلية و 50 ريال لحوالات دول الخليج' (my translation: 9 riyals including VAT for domestic transfers and 50 riyals for transfers to the Gulf states): its decider is the transfer, as S02-ZD-058 (rule 4); in S02-VP-15's note
- S02-ZD-199 (c): the wallet transfer fee of 9 riyals including VAT 'في حال كانت الحوالة داخل السعودية' (my translation: if the transfer is within Saudi Arabia): its decider is the transfer's destination (rule 4); in S02-VP-15's note
- S02-ZD-200 (c): the wallet transfer fee of 50 riyals 'في حال كانت الحوالة خارج السعودية' (my translation: if the transfer is outside Saudi Arabia): as S02-ZD-199; in S02-VP-15's note
- S02-ZD-201 (c): the Mada rate's cap of 200 riyals '(غير شامل لضريبة القيمة المضافه)' (my translation: excluding VAT): names no decider (rule 4), and its scope, 'Zid Pay, Saudi Arabia', doesn't say whose country (rule 2)
- S02-ZD-202 (c): operating fees per transaction 'حسب باقتك في زد (بدون ضريبة)' (my translation: according to your plan in Zid, without tax): names no decider of the tax (rule 4)
- S02-ZD-204 (c): 'ضريبة القيمة المضافة: الرسوم 15x%' (my translation: VAT: the fees x 15%): names the rate, not a decider, and its words don't apply it to all stores or fees (rule 4)
- S02-ZD-205 (c): a path in the admin to the transaction's 'الفاتورة الضريبية' (my translation: the tax invoice): names no decider (rule 4)
- S02-ZD-398 (c): the Mada cap, '200 SAR (excluding VAT).': names no decider (rule 4); its scope's 'For our Saudi Superstars' doesn't say they are the merchants, as part RD1-4 noted S02-ZD-112
- S02-ZD-408 (c): the fees 'غير شاملة لضريبة القيمة المضافة، ويتم احتسابها بحسب شبكة الدفع و الباقة المختارة' (my translation: excluding VAT, and calculated by the payment network and the chosen plan): names no decider of the tax (rule 4); its scope's 'لنجومنا السعوديين' (my translation: for our Saudi stars) doesn't say they are the merchants, as part RD1-4 noted S02-ZD-112
- S02-ZD-411 (c): the Mada cap of 200 riyals '(غير شاملة لضريبة القيمة المضافة)': as S02-ZD-398
- S02-ZD-418 (c): as S02-ZD-408, its scope 'لطاقمنا الكويتي' (my translation: for our Kuwaiti crew) not saying they are the merchants

### Place tasks: woocommerce (c)

Placed: S02-WC-246 joined S02-V-212 (S02-VP-17) and S02-V-217 (S02-VP-18), and is a new row under S02-VP-12, S02-V-292, the store address ('Your store address is required to set the origin country for shipping, currencies, and payment options'); S02-WC-247 joined S02-V-190 (S02-VP-08, where the user resides, read as the merchant's residence, marked); S02-WC-248 and S02-WC-286 are a new row under S02-VP-09, S02-V-293, where the user is ('If you are a user in countries located in the European Economic Area, Switzerland, or the United Kingdom'; Stripe's Regional Terms for 'Users in India'), the user read as the merchant (marked); S02-WC-254 joined S02-V-192 (S02-VP-09, the user's country of residence, as S02-WC-077); S02-WC-317 joined S02-V-201 (S02-VP-13, the WooPayments account's country); S02-WC-318 is a new row under S02-VP-12, S02-V-294, the WooPayments account's country ('Their billing country matches your WooPayments account country', of Affirm, Afterpay and Klarna); S02-WC-416, S02-WC-417, S02-WC-419 and S02-WC-420 are a new row under S02-VP-17, S02-V-295, the base country (`'type' => 'base_location_country'`), the extensions the platform suggests read as features the store can use (marked); S02-WC-433 joined S02-V-209 (S02-VP-16, the base country); S02-WC-434 is a new row under S02-VP-11, S02-V-296, the base country ('Maybe add a note on WooCommerce Payments for US based sites'). Noted:
- S02-WC-249 (c): 'Fees for some Paid Services may vary based on the billing country associated with your payment method', the price shown 'an estimate based on your detected location': a payment method's billing country and a detected location, neither said to be where the store or its merchant is based (rule 2), as part RD1-S1 noted it under (a); in S02-VP-14's note
- S02-WC-253 (c): the user 'Will comply with all applicable laws and regulations (including ... the transmission of technical data exported from the United States or the country in which you reside': the country of residence decides which export laws on technical data apply, an X that fits none of (c)'s kinds (neither the law that governs the terms nor the store's data), and the second pass raises no point (listed below under 'Candidates for a new point')
- S02-WC-287 (c): 'Provide clear refund and exchange language that is consistent with Laws and the Card Network Rules': names no decider (rule 4)
- S02-WC-296 (c): 'Setting up your store in the wrong country may lead to the following issues:': names no thing bound, and the issues it introduces are under none of this decision's bullets (rule 2)
- S02-WC-319 (c): Affirm 'requires that your site only be available in U.S. English (en_US), Canadian English (en_CA), and/or Canadian French (fr_CA)': its decider is the site's languages (rule 4); in S02-VP-12's note
- S02-WC-323 (c): 'Payment provider availability varies by country and by the information you entered during setup': its words don't say whose country (rule 2), and the information entered during setup is outside rule 1's table (rule 4); in S02-VP-12's note
- S02-WC-421 (c): 'Rule processor that performs a comparison operation against the base * location - country': names the rule that S02-WC-419's and S02-WC-420's visibility uses, but no thing bound itself (rule 2)

### Note tasks: zid (c)

- S02-ZD-179 (c): They quote the Saudi Terms that zid.eg's Terms page holds in its raw HTML. The page's scripts replace them with the Terms of شركة زد مصر, under Egyptian law, so the page doesn't show these words (`method-report.md`, section 9). The statements recorded from the page as shown take their place.
- S02-ZD-180 (c): They quote the Saudi Terms that zid.eg's Terms page holds in its raw HTML. The page's scripts replace them with the Terms of شركة زد مصر, under Egyptian law, so the page doesn't show these words (`method-report.md`, section 9). The statements recorded from the page as shown take their place.

### Correction: S02-WC-253 (woocommerce, (c))

S02-WC-253, noted above as a candidate for a new point, is placed instead: it joined S02-V-192 (S02-VP-09, the user's country of residence). Part RD1-4 read the laws a merchant must comply with under the terms as the law that applies (S02-SA-209 under S02-VP-09), and Zid's S02-ZD-220 below is read the same way; the export laws on technical data 'exported from the United States or the country in which you reside' are read so too (my reading, marked in the row). Its note above stays, and it is not a candidate.

### Place tasks: zid (c)

Placed: S02-ZD-178 joined S02-V-187 (S02-VP-17, the business's registered country: 'أن تكون شركة أو مؤسسة مسجّلة في المملكة العربية السعودية'; my translation: to be a company or establishment registered in Saudi Arabia, for Zid financing); S02-ZD-210 joined S02-V-185 (S02-VP-17, the merchant's place: 'تمويل زد متاح لتجار المملكة العربية السعودية'; my translation: Zid financing is available to the merchants of Saudi Arabia); S02-ZD-220 joined S02-V-171 (S02-VP-09, every store: 'ينبغي على كافة المتاجر والتُجّار الالتزام بكافة القوانين المعمول بها'; my translation: all stores and merchants must comply with all the laws in force), read as the law that applies, as S02-SA-209; S02-ZD-218 is a new row under S02-VP-09, S02-V-297, the store's place ('للمتاجر السعودية'; my translation: for Saudi stores), the Ministry of Commerce's regulations on e-commerce terms read as the law that applies (marked). Noted:
- S02-ZD-174 (c): deposits to the bank account 'في السعودية' (my translation: in Saudi Arabia) on Sundays, Tuesdays and Thursdays, with a 3-riyal fee: its words, identifier and scope name Saudi Arabia without saying whose country (rule 2), as part RD1-4 noted S02-ZD-112
- S02-ZD-175 (c): deposits 'في الكويت' (my translation: in Kuwait) daily, with no fee: as S02-ZD-174
- S02-ZD-176 (c): Zid's warranty program 'حاليا فقط في السعودية' (my translation: currently only in Saudi Arabia): its words and scope don't say whose country (rule 2)
- S02-ZD-225 (c): stopping the invoices without another accounting system 'سيعرضك لغرامات وزارة التجارة' (my translation: will expose you to the Ministry of Commerce's fines): names no decider (rule 4)
- S02-ZD-310 (c): apps must 'Disclose applicable eligibility, country, contract or verification prerequisites': a rule for apps, naming no thing bound to the store's country nor a decider (rule 2)
- S02-ZD-347 (c): the plans' monthly prices on zid.sa's pricing page (scope 'zid.sa pricing page'): its decider is the site, outside rule 1's table, and a scope that names a site isn't every store (rule 4); in S02-VP-14's note
- S02-ZD-348 (c): Rise's price on zid.sa's pricing page: as S02-ZD-347
- S02-ZD-349 (c): Growth's price on zid.sa's pricing page: as S02-ZD-347
- S02-ZD-350 (c): zid.eg's plans, 'البداية مجاناً مدى الحياة' (my translation: Starter free for life; scope 'zid.eg pricing page (زد مصر)'): as S02-ZD-347
- S02-ZD-351 (c): Rise's price in Egyptian pounds on zid.eg's pricing page: as S02-ZD-347
- S02-ZD-352 (c): Growth's price in Egyptian pounds on zid.eg's pricing page: as S02-ZD-347
- S02-ZD-353 (c): Professional's custom price on both sites' pricing pages: as S02-ZD-347
- S02-ZD-354 (c): zid.sa's footer, 'Al-Qudrah Al-Taqniyah for Technology and Communication Company', its registration and VAT numbers: its words don't say the merchant contracts with it, nor what decides it (rule 4), as part RD1-4 noted S02-ZD-062
- S02-ZD-355 (c): zid.eg's footer, the same company with another registration and tax number: as S02-ZD-354
- S02-ZD-367 (c): zid.eg's Terms, 'اتفاقية ملزمة قانونياً بينك ... وبين شركة زد مصر' (my translation: a legally binding agreement between you ... and Zid Egypt), scope 'www.zid.eg': its decider is the site, outside rule 1's table (rule 4); in S02-VP-08's note
- S02-ZD-368 (c): 'ومن يصل إلى المنصة من خارج مصر يتحمل مسؤولية الامتثال للقوانين المحلية المعمول بها' (my translation: whoever reaches the platform from outside Egypt bears responsibility for complying with the applicable local laws): the place the platform is reached from, not said to be where the merchant is based (rule 1); in S02-VP-09's note
- S02-ZD-369 (c): Zid Egypt's plans, 'منشورة على المنصة' (my translation: published on the platform), scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-14's note
- S02-ZD-370 (c): the payment methods zid.eg's Terms accept (Mastercard, Visa, Fawry and others), scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-14's note
- S02-ZD-371 (c): payments 'بالجنيه المصري ... وتخضع لضريبة القيمة المضافة' (my translation: in Egyptian pounds ... and subject to VAT), scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-14's and S02-VP-15's notes
- S02-ZD-372 (c): consumers' 14-day right to withdraw from a digital subscription under Egypt's consumer protection law, scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-09's note
- S02-ZD-373 (c): the merchant's responsibility for 'الامتثال لجميع القوانين المصرية المعمول بها الحاكمة لنشاطك التجاري' (my translation: compliance with all applicable Egyptian laws governing your business activity), scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-09's note
- S02-ZD-374 (c): the merchant's obligations to its customers 'وفقاً للقانون المصري' (my translation: under Egyptian law), scope 'www.zid.eg': as S02-ZD-373
- S02-ZD-375 (c): Zid Egypt 'تعمل بوصفها مزوّداً لمنصة تقنية فحسب' (my translation: acts only as a provider of a technical platform), not a party to the merchant's sales: names no decider (rule 4)
- S02-ZD-376 (c): use of the platform only for lawful business 'وفقاً لهذه الشروط والقانون المصري المعمول به' (my translation: under these terms and the applicable Egyptian law), scope 'www.zid.eg': as S02-ZD-373
- S02-ZD-377 (c): an amicable settlement of disputes for at least 15 days: names no decider (rule 4)
- S02-ZD-378 (c): consumers' right under Egyptian law to complain to the Consumer Protection Agency, scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-09's note
- S02-ZD-379 (c): disputes referred to 'المحاكم المصرية المختصة' (my translation: the competent Egyptian courts), scope 'www.zid.eg': as S02-ZD-378
- S02-ZD-380 (c): 'تخضع هذه الشروط وتُفسَّر وفقاً لقوانين جمهورية مصر العربية' (my translation: these terms are governed and construed by the laws of Egypt), scope 'www.zid.eg': as S02-ZD-378
- S02-ZD-381 (c): the Egyptian courts' exclusive jurisdiction, scope 'www.zid.eg': as S02-ZD-378
- S02-ZD-382 (c): the entire agreement 'بينك وبين زد مصر' (my translation: between you and Zid Egypt), scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-08's note
- S02-ZD-383 (c): zid.eg's Privacy Policy names 'زد مصر' (Zid Egypt) as responsible for processing your personal data, scope 'www.zid.eg': its decider is the site (rule 4); in S02-VP-19's note
- S02-ZD-384 (c): zid.eg's Privacy Policy issued under Egypt's Personal Data Protection Law No. 151 of 2020, scope 'www.zid.eg': as S02-ZD-383
- S02-ZD-385 (c): some personal data 'قد يتم نقل ... ومعالجتها في دول خارج مصر' (my translation: may be transferred and processed in countries outside Egypt), scope 'www.zid.eg': as S02-ZD-383
- S02-ZD-421 (c): Zid Syria's 'No, there's no commission on your sales' (scope 'zid.sa/en/syria (Zid Syria)'): its decider is the site (rule 4); in S02-VP-14's note

### Place tasks: zid (c), continued

Noted:
- S02-ZD-389 (c): Rise's price in Egyptian pounds on zid.sa's page for Egypt (scope 'zid.sa/en/egypt: Rise'): its decider is the page, whose country isn't said to be the merchant's (rule 2), and a scope that names a site isn't every store (rule 4); in S02-VP-14's note
- S02-ZD-390 (c): Growth's price on the same page: as S02-ZD-389
- S02-ZD-391 (c): Rise's price in dollars on zid.sa's page for Syria: as S02-ZD-389
- S02-ZD-392 (c): Growth's price on the same page: as S02-ZD-389
- S02-ZD-393 (c): Rise's price in riyals on zid.sa's pages for the UAE, Kuwait and Oman: as S02-ZD-389
- S02-ZD-394 (c): Growth's price on the same pages: as S02-ZD-389
- S02-ZD-396 (c): '3 SAR per deposit, but Riyad Bank users get a free pass!': its decider is the merchant's bank (rule 4); in S02-VP-13's note
- S02-ZD-397 (c): 'All banks in Saudi Arabia!': names the banks, not a decider (rule 4), as part RD1-4 noted S02-ZD-065
- S02-ZD-399 (c): currencies 'Activate through your store settings': the merchant's choice, not a decider from rule 1's table (rule 4)
- S02-ZD-400 (c): 'Every 2-3 days, minimum 100 SAR.': names no decider (rule 4); its scope's 'For our Saudi Superstars' doesn't say they are the merchants, as part RD1-4 noted S02-ZD-112
- S02-ZD-401 (c): 'We'll verify your info within two business days.': names no decider (rule 4); its scope as S02-ZD-400's
- S02-ZD-402 (c): 'Just the operational fees based on your plan and payment network.': its deciders are the plan and the payment network (rule 4); in S02-VP-14's note
- S02-ZD-403 (c): 'All banks in Kuwait.': names the banks, not a decider (rule 4)
- S02-ZD-404 (c): currencies 'Set it up in your store settings.': as S02-ZD-399
- S02-ZD-405 (c): fees 'based on the network and your plan': as S02-ZD-402
- S02-ZD-406 (c): 'operational fees based on your chosen plan': as S02-ZD-402
- S02-ZD-407 (c): 'Daily (Sunday to Thursday), minimum 1 KWD.': names no decider (rule 4); its scope's 'For our Kuwait Crew' doesn't say they are the merchants, as part RD1-4 noted S02-ZD-112
- S02-ZD-409 (c): a 3-riyal deposit fee, 'عدا بنك الرياض معفي من رسوم الإيداع' (my translation: except Riyad Bank, exempt from the deposit fee): as S02-ZD-396
- S02-ZD-410 (c): 'جميع البنوك في المملكة العربية السعودية.' (my translation: all banks in Saudi Arabia): as S02-ZD-397
- S02-ZD-412 (c): currencies 'يتم تفعيلها من خلال إعدادات المتجر' (my translation: activated through the store's settings): as S02-ZD-399
- S02-ZD-413 (c): collection 'خلال ٢-٣ أيام، والحد الأدنى ... 100 ريال' (my translation: within 2-3 days, the minimum 100 riyals): as S02-ZD-400
- S02-ZD-414 (c): 'يتم التأكد من صحة البيانات المرفوعة خلال يومي عمل' (my translation: the uploaded data is verified within two working days): as S02-ZD-401
- S02-ZD-415 (c): 'جميع البنوك في دولة الكويت.' (my translation: all banks in Kuwait): as S02-ZD-397
- S02-ZD-416 (c): Kuwait's payment networks, 'كيه نت٫ آبل باي، فيزا، أمريكان اكسبريس': names no decider (rule 4), and its identifier's Kuwait doesn't say whose country (rule 2), as part RD1-4 noted S02-ZD-067
- S02-ZD-417 (c): fees 'بحسب الشبكة المستخدمة في عملية الدفع وباقة المتجر' (my translation: by the network used for the payment and the store's plan): as S02-ZD-402
- S02-ZD-419 (c): collection 'بشكل يومي "من الأحد إلى الخميس"' (my translation: daily, Sunday to Thursday), minimum 1 Kuwaiti dinar: as S02-ZD-407
- S02-ZD-420 (c): Zid Syria's 'shipping and delivery solutions suited to the Syrian market', with delivery 'inside Syria': the market orders go to and the site (scope 'zid.sa/en/syria (Zid Syria)'), not the store's own country (rule 1, rule 4); in S02-VP-17's note
- S02-ZD-422 (c): Zid Syria's payments 'through Bemira for e-payments': its decider is the site (rule 4); in S02-VP-12's note
- S02-ZD-423 (c): Zid Syria: 'a commercial registration isn't required to start and open your online store': its decider is the site (rule 4); in S02-VP-10's note
- S02-ZD-436 (c): shipping 'يبدأ من 11 ريال للشحنة' (my translation: starts from 11 riyals per shipment) for Rise, on zid.sa's pages for the UAE, Kuwait and Oman: its deciders are the plan and the page (rule 4); in S02-VP-17's note
- S02-ZD-440 (c): shipping from 10.5 riyals for Growth on the same pages: as S02-ZD-436
- S02-ZD-443 (c): shipping from 8.5 riyals for Professional on the same pages: as S02-ZD-436
- S02-ZD-445 (c): 'شبكة شركاء موثوقين في المدفوعات والخدمات اللوجستية والتكنولوجيا' (my translation: a network of trusted partners in payments, logistics and technology): names no decider (rule 4), and its scope, 'الإمارات; عمان' (the UAE; Oman), doesn't say whose countries (rule 2)
- S02-ZD-446 (c): the same for Egypt and Kuwait (scope 'مصر; الكويت'): as S02-ZD-445

### Candidates for a new point (part RD1-S3)

None. S02-WC-253, first noted as one (X: the export laws on technical data; question: what decides it), was placed under S02-VP-09 instead (the correction above).

### Searches for earlier platforms' rows (part RD1-S3)

None: the second pass raises no point, and every row written here is of Zid, WooCommerce or BigCommerce, under (c).

### Rechecks (part RD1-S3)

Rows compared with a statement of their own platform were rechecked under rule 5: each joined statement names its row's decider in its own words, or, where said, by its scope: S02-BC-281 (S02-V-234, 'Merchants in India'); S02-WC-246 (S02-V-212 and S02-V-217, 'Your store address'); S02-WC-247 (S02-V-190, 'where you reside'); S02-WC-253 and S02-WC-254 (S02-V-192, 'the country in which you reside', 'your country of residence'); S02-WC-317 (S02-V-201, 'If your WooPayments account is in'); S02-WC-433 (S02-V-209, 'get_base_country()'); S02-ZD-178 (S02-V-187, 'مسجّلة في المملكة العربية السعودية'; my translation: registered in Saudi Arabia); S02-ZD-210 (S02-V-185, 'لتجار المملكة العربية السعودية'; my translation: to the merchants of Saudi Arabia); S02-ZD-220 (S02-V-171, every store, 'كافة المتاجر والتُجّار'; my translation: all stores and merchants). Each keeps its row's basis, `answers`.

### This section's order (part RD1-S3)

The subsections '### Place tasks: zid (a), (b) and (d)', '### Candidates for a new point', '### Searches' and '### Rechecks (part RD1-S1)', between 'Revisit S02-V-233' and 'Revisit S02-V-236' above, are part RD1-S1's, appended while this part ran, without a heading of their own. The rest under '## Second pass, RD1-S3' is this part's.

### Problems with the method (part RD1-S3)

1. A revisit with no answer and no gap. S02-V-237 (bigcommerce, S02-VP-16): its three leads name no decider, and its `why` names no gap or absence, so none of the brief's four replacements applies. The row stays `not covered`, rewritten with a note; the coordinator decides whether it goes back to gap-closing.
2. Sites as deciders. zid.eg's Terms and Privacy Policy (S02-ZD-367 to S02-ZD-385), the pricing pages of zid.sa and zid.eg and zid.sa's country pages (S02-ZD-347 to S02-ZD-353, S02-ZD-389 to S02-ZD-394, S02-ZD-436, S02-ZD-440, S02-ZD-443) and Zid Syria's page (S02-ZD-420 to S02-ZD-423) have scopes that name a site, which rule 4 keeps out of `every store`, and a site is outside rule 1's table of deciders. So they are noted, each named in its point's note. What zid.eg's pages bind (Zid Egypt as the contracting party, Egypt's law and courts, fees in Egyptian pounds with VAT, Zid Egypt as the data controller) stands only in notes; S02-ZD-G03's and S02-ZD-G08's gap rows remain.
3. The headings of Zid Payments' sections ('For our Saudi Superstars', 'For our Kuwait Crew', 'لنجومنا السعوديين', 'لطاقمنا الكويتي') are read, as part RD1-4 read them (S02-ZD-112), as not saying they are the merchants. Read as the merchant's place, S02-ZD-398, S02-ZD-400, S02-ZD-401, S02-ZD-407, S02-ZD-408, S02-ZD-411, S02-ZD-413, S02-ZD-414, S02-ZD-418 and S02-ZD-419 would answer S02-VP-10, S02-VP-13 or S02-VP-15.
4. The laws a merchant must comply with are read, as part RD1-4 read S02-SA-209, as the law that applies under the terms (S02-VP-09): S02-ZD-218, S02-ZD-220 and S02-WC-253, marked in their rows.
5. An x_words slip, corrected: 'country of operation', a decider, not X, was added to S02-VP-13's x_words for bigcommerce with `xwords`, and taken out again by a script run under the folder's lock, since the tool can't remove words. S02-VP-13's x_words for bigcommerce read 'your initial payout'.
6. Ids: this part's new rows are S02-V-281 to S02-V-297. It raised no point.

### Check (part RD1-S3)

On a copy holding only `b/RD1`: `merge_slices.py` merged 19 points and 297 rows; `check_subject.py` gave no line of level `error`, 17 warnings (phase A's quote lengths) and 14 reviews (quotes found only in a page's source, the coordinator's; and RD2's and RD3's statements, whose folders the copy leaves out); its `unplaced.tsv` holds no row of RD1. `second_pass_list.py --check`: RD1 has no revisit, reread or note task without a row in `done.tsv`.

## Second pass, RD1-S4

Part RD1-S4 rereads, under (c), the 51 Zid statements that earlier parts noted and that the work list names under rule 4's last clause under (c), widened on 27 October 2026: the merchant's country is the decider where the platform's own words tie the site, page or section a statement comes from to one country, and address it to merchants. Each reread's earlier note stays as it is, whether the reread places it or not.

### How the rereads are decided (part RD1-S4)

1. Tied to one country. A statement is placed where each site, page or section it is recorded from (its `source`, `identifier` and `scope`) is one that the platform's own words tie to one country:
   - zid.eg: 'زد مصر' (my translation: Zid Egypt), in the scopes and identifiers of its pricing page, Terms and Privacy Policy, and 'الدولة: جمهورية مصر العربية' (S02-ZD-383; my translation: country: the Arab Republic of Egypt);
   - zid.sa's pages for Egypt, the UAE, Kuwait and Oman, whose heroes read 'Join thousands of merchants in Egypt and launch your online store easily.' (S02-ZD-061), and the same in the UAE (S02-ZD-137), in Kuwait (S02-ZD-386) and in Oman (S02-ZD-387);
   - zid.sa's page for Syria: 'The best and easiest e-commerce platform in Syria' (S02-ZD-138, its hero), and 'Zid Syria' (its statements' scopes);
   - Zid Payments' sections 'For our Saudi Superstars', 'For our Kuwait Crew', 'لنجومنا السعوديين' and 'لطاقمنا الكويتي' (my translation: for our Saudi stars; for our Kuwaiti crew), the coordinator's own example of a Zid Payments section headed for one country's merchants;
   - the help centre's sections 'متطلبات تفعيل الدفع الالكتروني للسعودية' and 'متطلبات تفعيل الدفع الالكتروني للكويت' (my translation: the requirements to activate e-payment for Saudi Arabia; for Kuwait), and 'تحصيل المدفوعات > في السعودية' and 'تحصيل المدفوعات > في الكويت' (my translation: collecting payments > in Saudi Arabia; in Kuwait).

   Where those words don't name merchants, which holds for all of them but the four heroes that read 'Join thousands of merchants in ...', the row's evidence marks the decider as a reading.
2. Joined where the decider already has a row. Under (c), things of one kind with the same decider are one answer, and which country gets which stays in the statements and their scope (rule 4). So where a point already holds a Zid row whose decider is where the merchant is, or the merchant's country (S02-V-172, S02-V-175, S02-V-177, S02-V-179, S02-V-180, S02-V-181, S02-V-184), the statements placed under that point join it, and the evidence they add names each country as the platform ties it. Where no such row is there (S02-VP-08, S02-VP-15, S02-VP-19), a new row is added. S02-V-297 (S02-VP-09) and S02-V-183 (S02-VP-16), whose decider is the store's place ('للمتاجر السعودية'; my translation: for Saudi stores), are not joined.
3. Left noted, where the source is tied to no country, or to several (rule 4).

### Rereads, in the work list's order (part RD1-S4)

- S02-ZD-008, left noted: it is recorded at the page, Zid Payments' (scope 'Zid Payments', no section in its identifier), which holds sections for two countries, Saudi Arabia and Kuwait: tied to several.
- S02-ZD-112, placed: joined S02-V-177 (S02-VP-11). Its identifier records it under each of Zid Payments' sections, 'لنجومنا السعوديين; لطاقمنا الكويتي', each headed for one country (a reading).
- S02-ZD-119, left noted: the help centre's FAQ on sales channels (scope 'أمازون') is tied to no country, and the statement names two, Saudi Arabia and the UAE.
- S02-ZD-122, S02-ZD-123, S02-ZD-154 and S02-ZD-155, placed: joined S02-V-175 (S02-VP-10), the merchant's country, Saudi Arabia or Kuwait, by each section's heading (a reading).
- S02-ZD-174 and S02-ZD-175, placed: joined S02-V-180 (S02-VP-13), the merchant's country, Saudi Arabia or Kuwait, by each section's heading (a reading).
- S02-ZD-347, S02-ZD-348 and S02-ZD-349, left noted: zid.sa's pricing page (scope 'zid.sa pricing page') is tied by no words of the platform to one country, and zid.sa holds pages for several (S02-ZD-389 to S02-ZD-394's scopes).
- S02-ZD-350, S02-ZD-351 and S02-ZD-352, placed: joined S02-V-181 (S02-VP-14), the merchant's country, Egypt, by the site zid.eg (a reading).
- S02-ZD-353, left noted: its source is two pricing pages (scope 'zid.eg and zid.sa pricing pages'), zid.eg's, tied to Egypt, and zid.sa's, tied to no one country.
- S02-ZD-367, placed: a new row, S02-V-298 (S02-VP-08), 'وبين شركة زد مصر' (my translation: and the company Zid Egypt), and joined S02-V-172 (S02-VP-09). The merchant's country, Egypt, by the site zid.eg (a reading).
- S02-ZD-369, S02-ZD-370 and S02-ZD-371, placed: joined S02-V-181 (S02-VP-14). S02-ZD-371 also raises a new row, S02-V-299 (S02-VP-15), 'وتخضع لضريبة القيمة المضافة (ض.ق.م) بالنسبة القانونية السارية' (my translation: and are subject to VAT at the applicable legal rate). The merchant's country, Egypt, by the site zid.eg (a reading). S02-ZD-370's payment methods, which zid.eg's Terms accept for its plans, are read as how the platform's fees are billed (my reading).
- S02-ZD-372, S02-ZD-373, S02-ZD-374, S02-ZD-376, S02-ZD-378, S02-ZD-379, S02-ZD-380, S02-ZD-381 and S02-ZD-382, placed: joined S02-V-172 (S02-VP-09), Egypt's law and courts under zid.eg's Terms. S02-ZD-373 also joined S02-V-184 (S02-VP-16), for 'الضرائب' (my translation: taxes) among the Egyptian laws the merchant must comply with. S02-ZD-382 also joined S02-V-298 (S02-VP-08). The merchant's country, Egypt, by the site zid.eg (a reading).
- S02-ZD-383, S02-ZD-384 and S02-ZD-385, placed: a new row, S02-V-300 (S02-VP-19), 'الجهة المسؤولة عن معالجة بياناتك الشخصية هي: زد مصر' (my translation: the party responsible for processing your personal data is Zid Egypt), with Egypt's Personal Data Protection Law and transfers outside Egypt. The merchant's country, Egypt, by the site zid.eg (a reading).
- S02-ZD-389 and S02-ZD-390, placed: joined S02-V-181 (S02-VP-14), the merchant's country, Egypt, by zid.sa's page for Egypt, whose hero names merchants.
- S02-ZD-391 and S02-ZD-392, placed: joined S02-V-181 (S02-VP-14), the merchant's country, Syria, by zid.sa's page for Syria (a reading).
- S02-ZD-393 and S02-ZD-394, placed: joined S02-V-181 (S02-VP-14). Each is recorded from three pages, zid.sa's for the UAE, Kuwait and Oman, each tied to one country by its hero, which names merchants, and the same price stands on each.
- S02-ZD-398, S02-ZD-408, S02-ZD-411 and S02-ZD-418, placed: joined S02-V-181 (S02-VP-14), Zid Payments' fees, and S02-V-299 (S02-VP-15), the fees 'غير شاملة لضريبة القيمة المضافة' (my translation: excluding VAT). The merchant's country, Saudi Arabia or Kuwait, by Zid Payments' sections (a reading).
- S02-ZD-400, S02-ZD-407, S02-ZD-413 and S02-ZD-419, placed: joined S02-V-180 (S02-VP-13), when Zid Payments pays the merchant, by the same sections (a reading).
- S02-ZD-401 and S02-ZD-414, placed: joined S02-V-175 (S02-VP-10), the check of the merchant's information within two working days, and S02-V-177 (S02-VP-11), activation at once. Saudi Arabia, by the same sections (a reading).
- S02-ZD-421, placed: joined S02-V-181 (S02-VP-14), no commission on sales, read as one of the platform's fees (my reading). Syria, by zid.sa's page for Syria (a reading).
- S02-ZD-422, placed: joined S02-V-179 (S02-VP-12), Bemira for e-payments. Syria, by the same page (a reading).
- S02-ZD-423, placed: joined S02-V-175 (S02-VP-10), no commercial registration needed to open the store. Syria, by the same page (a reading).

### Rows added and joined (part RD1-S4)

No row was replaced or removed. Three rows were added: S02-V-298 (S02-VP-08), S02-V-299 (S02-VP-15) and S02-V-300 (S02-VP-19). Nine rows took statements: S02-V-172, S02-V-175, S02-V-177, S02-V-179, S02-V-180, S02-V-181, S02-V-184, S02-V-298 and S02-V-299, each with the evidence for them added after its own. x_words took Zid's words for X under S02-VP-08, S02-VP-10 to S02-VP-16 and S02-VP-19. Each point the part touched has a note, "Second pass, RD1-S4", naming what it placed there.

### Points that now hold both an every store answer and a country's answer (part RD1-S4)

S02-VP-08 (S02-V-169 and S02-V-298), S02-VP-09 (S02-V-171 and S02-V-172), S02-VP-15 (S02-V-182 and S02-V-299) and S02-VP-19 (S02-V-220 and S02-V-300). Both are kept, and each point's note says so: phase C weighs them. Zid's gap rows S02-V-170 (S02-VP-08) and S02-V-173 (S02-VP-09), on S02-ZD-G03, and S02-V-291 (S02-VP-15), on S02-ZD-G08, stand as they were: no task of this part leads to them.

### Candidates for a new point (part RD1-S4)

None. Every placed statement answers one of (c)'s twelve kinds. S02-ZD-370's payment methods, which zid.eg's Terms accept for its plans, are read as how the platform's fees are billed (S02-VP-14), not as a new kind. Read otherwise, they would be a candidate: X, the means by which the merchant pays the platform, 'وسائل الدفع' (my translation: payment methods); the question, what decides it.

### Searches (part RD1-S4)

No point was raised, so no earlier platform's rows were searched for. To find the platform's own words that tie each page to its country, the slice's Zid statements were filtered by source: zid.sa's pages for Egypt, Syria, the UAE, Kuwait and Oman, and zid.sa's and zid.eg's pricing pages. The pages' heroes, S02-ZD-061, S02-ZD-137, S02-ZD-138, S02-ZD-386, S02-ZD-387 and S02-ZD-388 (under (d)), were read.

### Rechecks (part RD1-S4)

Each joined row was compared with the Zid statements already in it: its basis, `answers`, holds for each statement joined, whose own words name X, and whose site, page or section names the decider in its role.

### Calls (part RD1-S4)

1. S02-ZD-112 and S02-ZD-008, the Arabic and English answers to whether Zid Payments is available across the Gulf, are recorded differently. S02-ZD-112's identifier names both of the page's sections, for Saudi Arabia and for Kuwait, as S02-ZD-393's names each of three one-country pages: each place it is recorded from is tied to one country, so it is placed. S02-ZD-008's identifier and scope name only the page, which holds both sections: tied to several, it stays noted. Its answer, Saudi Arabia and Kuwait, is S02-V-177's already.
2. S02-ZD-393 and S02-ZD-394, each recorded from three pages each tied to one country, are placed: no page they come from is tied to several.
3. S02-ZD-353, recorded from zid.eg's and zid.sa's pricing pages, stays noted: one of its two pages is tied to no one country.
4. zid.sa's own pricing page (S02-ZD-347 to S02-ZD-349) is read as tied to no one country: its recorded scope names none, and the site holds pages for several.
5. Joining, not adding ("How the rereads are decided", 2): where the merchant is, and the merchant's country, are read as one decider in rule 4's sense, so one answer stays one row, and the evidence each joined statement adds names its country.
6. Ids: this part's new rows are S02-V-298 to S02-V-300. It raised no point.

### Problems with the method (part RD1-S4)

1. A row's own note can't be changed with the tool. S02-V-177's note still says that S02-ZD-008 and S02-ZD-112 'are noted: their words don't say whose country', while S02-ZD-112 is now joined to that row. S02-VP-11's note says so. The same holds for the points' notes: their earlier "Kept out" passages on the statements this part placed stand, and the note appended to each point names what is now placed.
2. Rule 4 says the variant names the country as the platform ties it, and a variant is a verbatim excerpt. A row that statements joined keeps its own excerpt: S02-V-181's names 'بالريال السعودي أو بعملة التاجر المحلية' (my translation: in Saudi riyals or the merchant's local currency). Egypt, Syria, the UAE, Kuwait, Oman, Saudi Arabia and Kuwait are named only in the evidence each joined statement adds. The new rows' excerpts name the country as the platform ties it ('زد مصر').
3. Outside the work list: S02-ZD-420, S02-ZD-436, S02-ZD-440, S02-ZD-443, S02-ZD-445 and S02-ZD-446 are noted under (c) from zid.sa's one-country pages, but their earlier notes give other reasons as well (the plan, the market orders go to, no thing bound named), and the work list doesn't name them. This part leaves them.

### Check (part RD1-S4)

On a copy holding only `b/RD1`: `merge_slices.py` merged 19 points and 300 rows. `check_subject.py` gave no line of level `error`, 17 warnings (phase A's citations) and 14 reviews: 12 quotes found only in a page's source, the coordinator's, and RD2's and RD3's statements, whose folders the copy leaves out. None names this part's rows or statements. Its `unplaced.tsv` holds no row of RD1. `second_pass_list.py --check`: RD1 has no revisit, reread or note task without a row in `done.tsv`.

## Second pass, RD1-S5

Part RD1-S5 does, in RD1's work list, the six rereads under (c) for Zid whose `why` begins "RD1-S5", and the last round's 22 tasks, whose `why` begins "last round" (after A2-T, A2-SH-H, A2-SA-H, A2-SA-S and A3-2): two revisits and twenty place tasks, for Shopify, Salla, WooCommerce and BigCommerce under (a), (b) and (c). Revisits first, then the rereads, then the place tasks.

### Revisit S02-V-237 (bigcommerce, S02-VP-16, the store's taxes), again (part RD1-S5)

RD1-S3 left the row `not covered`, since gap-closing had recorded no gap for the point. Gap-closing has since recorded S02-BC-G15 for it, and the row is replaced with `gap`, S02-BC-G15. Its leads, read again, still name no decider, and stay noted as RD1-S3 noted them:
- S02-BC-247 (c): 'If you have nexus in multiple states or local jurisdictions, the additional jurisdictions need to be adjusted from within your tax provider's account dashboard': says where jurisdictions are adjusted, not what decides the store's taxes (rule 4); its words don't say the nexus is where the store is based or registered (rule 1)
- S02-BC-249 (c): 'Access your US 1099-K and other tax forms in your account’s portal': names where the forms are, not a decider (rule 4)
- S02-BC-250 (c): 'Your US 1099-K and other tax forms are provided by the payment processor': names who provides them, not a decider (rule 4)

S02-BC-246 and S02-BC-248 are outside RD1's slice, and left.

### Revisit S02-V-058 (shopify, S02-VP-05, who checks), again (part RD1-S5)

Replaced with `gap`, S02-SH-G09, which stands in place of S02-SH-G01. None of the leads names who checks: they say the merchant 'may need to verify your business', and not who verifies. The leads answer two other points of (b):
- S02-SH-1031, placed: joined S02-V-059 (S02-VP-06): 'When changing country, you'll receive multiple tax forms ...', in the admin's 'Confirm store address' dialog (Settings > General, business details), a control in the store's admin, so the seller changes it (rule 4). Also joined S02-V-066 (S02-VP-07): 'Store address must be in the same country as the business entity' and 'Country needs to be the same as your business entity'. Also joined S02-V-267 (S02-VP-07): 'may need to verify your business', the same answer as 'might require additional verification' (S02-SH-590).
- S02-SH-1032, placed: joined the same three rows, from the dialog of the admin's business entity switch. Its 'Changing country creates a new entity ... The current entity ({entityName}) stays the same.' is quoted in S02-V-059's evidence. It isn't joined to S02-V-268 ('You can't change the business type, country, or the person associated with individual or sole proprietor entities'), because its words don't say the country can't be changed.
- S02-SH-1033 (b): 'Changing business type creates a new entity. You'll get multiple tax forms and may need to verify your business': a change of business type, not of the store's country, and it names no party that checks (rule 2)

### Rereads under (c), Zid, in the work list's order (part RD1-S5)

Read by rule 4's clause under (c) on sites, pages and sections tied to one country, as RD1-S4 read the others ("How the rereads are decided (part RD1-S4)", 1 to 3). Two things differ here:
- zid.sa's Arabic pages for the UAE, Kuwait and Oman (zid.sa/ar/uae, /ar/kuwait, /ar/oman) don't carry the English pages' hero. RD1-S4 cited 'Join thousands of merchants in the UAE ...' (S02-ZD-137), and the same for Kuwait (S02-ZD-386) and Oman (S02-ZD-387); those are zid.sa/en's. The Arabic pages' own hero, recorded from all three, is 'المنصة الأسهل للتجارة الالكترونية فالخليج' (S02-ZD-444; my translation: the easiest e-commerce platform in the Gulf). Read as RD1-S4 read the Syria page's hero, it ties the pages to the Gulf, several countries.
- Each Arabic page also holds a partners' section headed for one country: 'شركاؤنا في الإمارات', 'شركاؤنا في الكويت', 'شركاؤنا في عمان' and, on zid.sa/ar/egypt, 'شركاؤنا في مصر' (my translation: our partners in the UAE; in Kuwait; in Oman; in Egypt). A statement recorded from such a section is tied to one country by it, as RD1-S4 placed the statements recorded from Zid Payments' sections, which sit on a page that holds two countries.

The rereads:
- S02-ZD-420, placed: joined S02-V-185 (S02-VP-17), the Zid row whose decider is where the merchant is: 'بإمكان التاجر إذا كان موجودا في المملكة العربية السعودية أو أي من دول الخليج تفعيل الشحن' (my translation: the merchant, if located in Saudi Arabia or any Gulf state, can activate shipping). The statement places Tarabot for shipping and Mersal for delivery in Syria, by zid.sa's page for Syria (S02-ZD-138's hero; scope 'Zid Syria'), as RD1-S4 placed S02-ZD-421 to S02-ZD-423 from the same page (a reading). Its own 'suited to the Syrian market' and 'delivery inside Syria' say where deliveries go, not what decides that the store can use them; the earlier note read them as the decider, and the widened rule reads the page.
- S02-ZD-436, S02-ZD-440 and S02-ZD-443, left noted: shipping from 11, 10.5 and 8.5 riyals per shipment, by plan, recorded from the plans' section 'باقات تناسب احتياجك' (my translation: plans that suit your needs) of the three Arabic pages. That section names no country, and the pages are tied by their own hero to the Gulf (S02-ZD-444), several countries. Only another section of each page, its partners' heading, names one country. Their earlier notes stay as they are.
- S02-ZD-445, placed: joined S02-V-179 (S02-VP-12), for its 'شركاء موثوقين في المدفوعات' (my translation: trusted partners in payments), read as payment providers the store can use (my reading). Also joined S02-V-185 (S02-VP-17), for its partners in 'الخدمات اللوجستية' and 'التكنولوجيا' (my translation: logistics services; technology). The UAE and Oman, by the sections it is recorded from, 'شركاؤنا في الإمارات' and 'شركاؤنا في عمان' (a reading: the headings don't name merchants, and the statement speaks to the merchant's business, 'تجارتك').
- S02-ZD-446, placed: as S02-ZD-445, with marketing ('التسويق') in place of technology. Egypt and Kuwait, by 'شركاؤنا في مصر' and 'شركاؤنا في الكويت' (a reading).

x_words took Zid's words under S02-VP-12 and S02-VP-17, and each of the two points has a note, "Second pass, RD1-S5". S02-VP-17's earlier "Kept out (second pass, RD1-S3)" passage stands; the note after it says what is now placed.

### Place tasks, last round: salla, shopify, woocommerce, under (a), (b) and (c) (part RD1-S5)

Placed:
- S02-SA-441 (a), placed: a new row, S02-V-301 (S02-VP-01), 'P.storage.get("merchant")?.merchant?.kyc_country': the merchant record's kyc_country, which the dashboard sends as the request header 's-merchant-kyc', or 'SA' where the record holds none. It is read as the country of the merchant's KYC (my translation: know your customer) verification, a country the platform holds for the merchant (a reading). It is a field of its own, apart from S02-V-017's '"country":"Country of operation"', so it is a row of its own (rule 4). a2.tsv leads it to S02-VP-06, a point of (b), but the statement is under (a) only.
- S02-SH-1000 (a) and S02-SH-1001 (a), placed: joined S02-V-265 (S02-VP-01), storeCreatePayload's country, the country the store is created with. S02-SH-1000 is the code that sends the payload, 'country:Q.country||Yf'. S02-SH-1001, 'const Yf="US"', is the value that country takes when the sign-up gives none, by its identifier; its own words name a value, not a field (a call, below).
- S02-SH-1000 (b) and S02-SH-1001 (b), placed: joined S02-V-054 (S02-VP-04), the platform: where the sign-up gives no country, the code sets 'US', a default the code sets (rule 4). Who fills the sign-up's own country, their words don't say; S02-SH-G10 asks it.
- S02-WC-517 (a), placed: joined S02-V-273 (S02-VP-01), the country field of WooPayments onboarding's business step, 'Where is your business located?', the same field as S02-WC-259, from the same chunk. The absence S02-WC-N02, which the audit partly contradicted, still stands for what its note says: no page holds the business's legal name or a merchant of record, and nothing per selling location.
- S02-WC-516 (c), placed: joined S02-V-209 (S02-VP-16), the store's base country: 'have not configured a standard tax rate for your base location'. 'Base location' and 'base country' are read as one decider (my reading; a call, below). a2.tsv leads it to S02-VP-07, a point of (b), but the statement is under (c) only.

Noted:
- S02-SA-440 (a): Salla's storefront 'scope' object ('"name": "متجر السعودية"', my translation: the Saudi Arabia store; '"type": "scope"', with '"countries": ["SA"]', '"currencies": ["SAR"]' and '"languages"'): its keys say country without saying whose, and the object holds what a storefront scope sells in, not where the store is based (rule 2's role test; rule 1). a2.tsv leads it to S02-VP-85, RD3's; its (e) and (f) are RD2's and RD3's
- S02-SH-1002 (a): the address the sign-up reached carries 'country=YE' beside the new store's 'shopPermanentDomain': the parameter's words don't say whose country it is (rule 2's role test), and whether the new store takes the sign-up's country is what S02-SH-G10 asks
- S02-SH-1006 (a): the Dev Dashboard's call that creates a store sends '"shopName"', '"priceLookupKey"' and '"prepopulateTestData"', and no country: it names no field or record that holds the store's country (rule 2)
- S02-SH-1002 (b): the address carries country=YE after a sign-up that chose 'I'm located in:' Yemen, from a network in Yemen (its scope; S02-SH-G10): its words name no party that set it, and whether the choice or the network filled it is S02-SH-G10's question (rule 2)
- S02-SH-1003 (b): the mutation 'SignupCountryUpdate', with its variable 'countryCode': a definition alone names no party (rule 4), and its words, the signup country, don't say the country is where the store or its merchant is based (rule 2's role test)
- S02-SH-1004 (b): 'updateSignupCountry' sends a country code it is given to that mutation for a shop, or throws 'Failed to update signup country': as S02-SH-1003; the code sets no value of its own (rule 4)
- S02-SH-1005 (b): the sign-up's checkout code reads 'country' from its address, and passes a 'newCountryCode' to the sign-up's data and, for a shop, to the signup country's update: as S02-SH-1003; who gives the new country code, its words don't say
- S02-SH-1006 (b): the call sends no country: it names no party that sets the store's country (rule 2)
- S02-SH-1026 (b): the legal entity types for the country code YE ('Individual', 'Company', 'Non-Profit'): the types a business entity may take in a country, which names no party that sets, checks or changes the store's country, and no condition on a change (rule 2)
- S02-SH-1027 (b): the same for US ('Individual', 'Sole Proprietorship', 'Single Member LLC', and others): as S02-SH-1026
- S02-WC-518 (a): WooPayments reads the 'self_assessment' of the business verification step from the user's NOX profile, by '$location': its words don't say the record holds where the business is located, or whose the location is (rule 2's role test). The audit's note on S02-WC-N02 reads it as the business step's answers (S02-WC-517): a lead, not its words
- S02-WC-519 (c): 'The location for which the providers are being determined. This is an ISO 3166-1 alpha-2 country code': a location without saying whose, so no decider from rule 1's table (rule 4), as S02-WC-001 to S02-WC-003 were noted. The audit's note on S02-WC-N04 reads it as the business location, which the same file's 'Get the business location country code for the Payments settings' gives (S02-WC-221); its own words don't (a call, below)
- S02-WC-520 (c): ''recommended_payment_methods' => $this->get_recommended_payment_methods( $gateway, $country_code )': a country code without saying whose: as S02-WC-519

S02-WC-N04, which the audit partly contradicted, still stands for what its note says: no page makes an extension take a value per selling location or per customer's country.

### Rows replaced, removed, added and joined (part RD1-S5)

Replaced: S02-V-237 (not covered, now gap S02-BC-G15) and S02-V-058 (gap S02-SH-G01, now gap S02-SH-G09). None removed. Added: S02-V-301 (S02-VP-01, salla). Joined: S02-V-054, S02-V-059, S02-V-066, S02-V-265 and S02-V-267 (shopify); S02-V-179 and S02-V-185 (zid); S02-V-209 and S02-V-273 (woocommerce). Each joined row's evidence names what was added, after "Second pass, RD1-S5". x_words took salla's words under S02-VP-01, shopify's under S02-VP-04, woocommerce's under S02-VP-16, and zid's under S02-VP-12 and S02-VP-17.

### Candidates for a new point (part RD1-S5)

None. Each statement placed answers one of its bullet's questions for an X of one of rule 1's kinds. Each statement noted answers none of its bullet's questions, or names no decider, or fails the role test.

### Searches (part RD1-S5)

No point was raised, so no earlier platform's rows were searched for. To read the Arabic country pages' ties, the slice's Zid statements whose source is zid.sa/ar/uae, /ar/kuwait, /ar/oman, /ar/egypt or /ar/syria were listed: S02-ZD-436, S02-ZD-440, S02-ZD-443, S02-ZD-444 (the hero), S02-ZD-445 and S02-ZD-446. The English pages' heroes S02-ZD-061, S02-ZD-137, S02-ZD-138, S02-ZD-386 and S02-ZD-387 were read. To compare the WooCommerce statements' locations, S02-WC-001 to S02-WC-003 (noted), S02-WC-221, S02-WC-223, S02-WC-226, S02-WC-227, S02-WC-259, S02-WC-263, S02-WC-267 and S02-WC-268 were read.

### Rechecks (part RD1-S5)

Each row joined was compared with its own platform's statements already in it: S02-V-054, S02-V-059, S02-V-066, S02-V-265 and S02-V-267 (shopify), S02-V-179 and S02-V-185 (zid), S02-V-209 and S02-V-273 (woocommerce). Its basis, `answers`, holds for each statement joined: each one's words, or for S02-SH-1001 its identifier (rule 5), name what fills X, or the party, condition or decider, in its role.

### Calls (part RD1-S5)

1. S02-ZD-436, S02-ZD-440 and S02-ZD-443 are left noted, though the work list calls their pages "zid.sa's pages for one country each". The Arabic pages' own hero names the Gulf (S02-ZD-444), and their plans' section names no country. RD1-S4 tied the English pages by their heroes, which name one country and its merchants. If the Arabic pages are read as tied to one country by those English versions, by their addresses, or by their partners' headings, the three join S02-V-185 as the merchant's country: the UAE, Kuwait or Oman.
2. S02-ZD-445 and S02-ZD-446 are placed by their sections' headings, 'شركاؤنا في ...' (our partners in ...), each for one country. 'Partners in payments' is read as payment providers the store can use, and partners in logistics, technology or marketing as other services it can use (my readings).
3. S02-WC-519 and S02-WC-520 are noted, as S02-WC-001 to S02-WC-003 were: their words name a location or country code without saying whose. Read with S02-WC-221 (same file as S02-WC-519), they would join S02-V-289, the business location, marked as a reading.
4. S02-WC-516 joined S02-V-209 (base country), not S02-V-208 (the store address) and not a new row: 'base location' is the base country's own word family in WooCommerce's code (S02-V-040 under (a)).
5. S02-SH-1001 joined S02-V-265 under (a) by its identifier, since its words, 'const Yf="US"', name the value and not the field. It could instead be noted under (a), as a value rather than a field; its (b) answer, the platform's default, holds either way.
6. S02-SA-441's kyc_country is read as the merchant's country (KYC), a new field under (a). Read otherwise, it would be noted under the role test.
7. S02-SH-G10, which a2.tsv leaves for S02-VP-04 in place of S02-SH-G02, is in no row. No row named S02-SH-G02, and no task leads to a gap row for Shopify beside S02-VP-04's answers, so none was added. The coordinator may add one.

### Problems (part RD1-S5)

1. One command of this part wrote a wrong line to `done.tsv` ('revisit S02-V-058', with 'S02-VP-05' as its bullet and 'b' as its outcome). It was removed by hand under the folder's lock, and the right line stands. The tool has no command to remove a ledger line.
2. RD1-S4's notes give the heroes of zid.sa's English pages (zid.sa/en/...) as what ties zid.sa's pages for the UAE, Kuwait and Oman to one country. The Arabic pages (zid.sa/ar/...), from which this part's rereads S02-ZD-436 to S02-ZD-446 are recorded, carry another hero, which names the Gulf (call 1).

### Check (part RD1-S5)

On a copy holding only `b/RD1`, `merge_slices.py` merged 19 points and 301 rows. `check_subject.py` gave no line of level `error`. It gave 17 warnings, on phase A's citations (16 of Shopify's, 1 of WooCommerce's), and 14 reviews: 12 quotes found only in a page's source, which are the coordinator's, and the statements of RD2 and RD3, whose folders the copy leaves out. None names this part's rows or statements. Its `unplaced.tsv` holds no row of RD1. `second_pass_list.py --check`: RD1 has no revisit, reread or note task without a row in `done.tsv`.

## Second pass, RD1-S6

Part RD1-S6 does, in RD1's work list, the capture round's 71 tasks, whose `why` begins "capture round" (27 and 28 October, after A2-SH-R1 and A2-SH-R2, observed-sh 19a5f6435), all of them Shopify's: one revisit, of S02-V-058 under S02-VP-05, and 70 place tasks, 26 under (a), 21 under (b) and 23 under (c). The revisit first, then the place tasks, by bullet, in the work list's order.

### The slice this part read (part RD1-S6)

RD1's slice, `slices/RD1/`, was cut at 19:21 on 27 October, before the capture round's statements reached Shopify's phase A files (statements at 23:39, gaps at 23:42), and holds none of them: the printer named S02-SH-1035 as not in RD1's slice, and `variants_edit.py` refuses an id outside the slice. `kinds.tsv` (23:25) had no kind for 68 of the round's ids. This part writes only in its scratch folder and `b/RD1/`, so it cut the slice again on a copy of S-02 in its scratch folder: `check_subject.py` on the copy, which writes the copy's `kinds.tsv`, then `subject_slice.py` on the copy. It printed from that cut, and ran `variants_edit.py` on a scratch folder whose `slices` is that cut and whose `b` is the repository's own `b`, so every row was written to `b/RD1/` under the tool's lock. The cut reads the same phase A files the coordinator's would.

### Revisit S02-V-058 (shopify, S02-VP-05, who checks), a third time (part RD1-S6)

Replaced with `gap`, S02-SH-G14, which stands in place of S02-SH-G09: whether the platform checks the new country of a store's business entity, and of the store address that follows it, after a change of country saves, on a store that uses no financial services; and if it does, who checks it and against what. None of the new leads names who checks. They come from two runs: capture-gb-plus's switch from its Yemen entity to the organization's US entity, 'Capture Entity', and back (run 20261027T184800Z), and capture-us-plus's switch to another US entity (run 20261027T194111Z). Each is an observation of one store on one day, and each row joined keeps its scope. The leads under (b):
- S02-SH-1031 and S02-SH-1032: placed by RD1-S5 (S02-V-059, S02-V-066, S02-V-267), unchanged.
- S02-SH-1033: noted by RD1-S5, unchanged.
- S02-SH-1060, placed: joined S02-V-059 (S02-VP-06): Settings > General before the switch, with 'Manage entities in Organization settings' beside the store's entity 'capture gb plus - entity Yemen': where the seller manages the entity that holds the store's country, a control in the store's admin (rule 4). That the line is a link the text doesn't show: a reading.
- S02-SH-1062, placed: joined S02-V-059: the switch's dialog 'Review payment methods after switching', with its 'button "Continue"', a control in the store's admin. Its (c) is placed below.
- S02-SH-1063, placed: joined S02-V-059 ('Switching will update this store's business details', the words of S02-SH-338, which the row holds) and S02-V-267 (S02-VP-07): 'may need to verify your business', the same answer as S02-SH-1031 and S02-SH-1032. It names no party that checks.
- S02-SH-1064, placed: joined S02-V-059 (the seller's choice in the switch's dialog, 'radio "Capture Entity, United States" [checked]') and S02-V-066 ('Store address will update to match new legal entity', the words of S02-SH-261, which S02-V-066 holds).
- S02-SH-1065, placed: joined S02-V-059 (the dialog 'Confirm store address' and its 'button "Confirm"') and S02-V-066 ('Store address must be in the same country as the business entity').
- S02-SH-1066, placed: joined S02-V-059: the admin's call 'UpdatePrimaryLegalEntity' at Confirm, with the store address the run entered, '"country": "US"' (step 30, Confirm, by its scope).
- S02-SH-1067, placed: joined S02-V-059: Settings > General after Confirm, 'Capture Entity United States' and 'Store address 476 5th Ave, New York New York 10018, United States'.
- S02-SH-1072, placed: joined S02-V-059 (the dialog of the switch back) and S02-V-066 (its same-country line), and raised a new row, S02-V-302 (S02-VP-07): Confirm on the switch back to Yemen met 'Street can't be blank' and 'City can't be blank', and the switch saved after the run filled both (S02-SH-1073): a store address with a street and a city held before the country changed. No row of S02-VP-07 held that condition.
- S02-SH-1073, placed: joined S02-V-059: Settings > General after the switch back, 'capture gb plus - entity Yemen' and 'Store address 1 Capture Street, Sanaa, Yemen'.
- S02-SH-1088 (b): capture-us-plus's switch to 'Capture Placeholder LLC', a US entity, saved with '"userErrors":[]': a change of the store's business entity within one country, the United States, not of the store's country, and it names no party that checks (rule 2), as RD1-S5 noted S02-SH-1033
- S02-SH-1089 (b): Settings > General after that switch, 'Capture Placeholder LLC Single member LLC · United States': as S02-SH-1088. Its (a) is placed below

S02-V-267's evidence ended by naming S02-SH-G09 as what asks who verifies. It was replaced, keeping its variant and statements, to join S02-SH-1063 and to name S02-SH-G14 in its place; its note says so.

### Place tasks, capture round: shopify (a) (part RD1-S6)

Placed:
- S02-SH-1035, S02-SH-1036: joined S02-V-006 (S02-VP-01), the sign-up's field 'I'm located in:' (their identifier), with 'Yemen' selected before any input and 'United States' after the run chose it (run 20261027T175456Z, from a network in Yemen).
- S02-SH-1039: joined S02-V-265, storeCreatePayload's '"country": "US"', sent after that choice.
- S02-SH-1040: joined S02-V-005, the new shop's '"countryCode":"US"'.
- S02-SH-1041: joined S02-V-003 (its 'billingAddress', '"countryCodeV2":"US"') and S02-V-004 (its 'shopAddress', the same).
- S02-SH-1071: joined S02-V-003, capture-gb-plus's billing address after the switch, in New York. Its (c) is noted below.
- S02-SH-1044, S02-SH-1056, S02-SH-1060, S02-SH-1067, S02-SH-1073: joined S02-V-001 (Settings > General's business entity, with its name and country) and S02-V-002 (the store address on the same page).
- S02-SH-1065, S02-SH-1072: joined S02-V-002, the switch's 'Updated store address', with its country.
- S02-SH-1066: joined S02-V-001 (the store's primary legal entity, which the call 'UpdatePrimaryLegalEntity' sets, by its '"externalLegalEntityId"') and S02-V-002 (the address it sends, '"country": "US"').
- S02-SH-1047, S02-SH-1058, S02-SH-1081: joined S02-V-001, the shop API's 'primaryLegalEntity' with its '"countryCode":"US"'.
- S02-SH-1051: joined S02-V-001, the shop API's 'businessEntities', each with its address's country code.
- S02-SH-1087, S02-SH-1089: joined S02-V-001, the switch's choices, each entity with its country, and the page after the switch.
- S02-SH-1152, S02-SH-1153: joined S02-V-001: 'An entity can be assigned to multiple stores' and 'You can set a default business entity for a store', of the business entity, the record S02-V-001 holds. They are the Help Center's, with no scope.

Noted:
- S02-SH-1037 (a): the trace the run took, when it started, of the network its browser used for the sign-up host, '"loc": "YE"': a location of that network, not a field or record that holds where the store or its merchant is based (rule 1; rule 2's role test)
- S02-SH-1038 (a): '"geoCountryCode":"YE"' in the admin page's own data for store tuu1u4-v0, whose shop holds '"countryCode":"US"' (S02-SH-1040): its key doesn't say whose country it is (rule 2's role test)
- S02-SH-1050 (a): SignupCountryUpdate's '"countryCode": "YE"' at step 17 and '"countryCode": "US"' at step 18, the steps at which the plan checkout's 'I’m selling from' changed (S02-SH-1049): its words, the signup country, don't say whose country it is (rule 2's role test), as RD1-S5 noted S02-SH-1002 and S02-SH-1003 (a call, below)
- S02-SH-1055 (a): the Dev Dashboard's call that created capture-us-plus sends '"shopName": "capture us plus"', '"priceLookupKey"' and '"prepopulateTestData"', and no country: it names no field or record that holds the store's country (rule 2), as RD1-S5 noted S02-SH-1006

x_words took 'primaryLegalEntity; businessEntities' under S02-VP-01.

### Place tasks, capture round: shopify (b) (part RD1-S6)

Placed:
- S02-SH-1035: joined S02-V-054 (S02-VP-04, the platform): before any input, 'I'm located in:' held 'Yemen', on a sign-up from a network in Yemen: a value the page sets before the merchant chooses (a reading of its scope, 'Shift pressed, no input').
- S02-SH-1036, S02-SH-1039: joined S02-V-053 (the seller): the run's choice of 'United States', and the sign-up's call that followed it, '"country": "US"'.
- S02-SH-1048, S02-SH-1049: joined S02-V-053: the plan checkout's combobox 'Business location' (their identifier), 'I’m selling from', a control the seller sets; the run set it to Yemen and back. Their (c) is placed below.
- S02-SH-1082, S02-SH-1085: joined S02-V-053: capture-us-plus's 'Edit business details' form for a 'Single Member LLC' ('Country code United States', its identifier), and the save's answer, the new entity with '"countryCode":"US"', as that row holds S02-SH-437, S02-SH-438 and S02-SH-450.
- S02-SH-1153: joined S02-V-053: 'You can set a default business entity for a store from the Settings > General page of your Shopify admin'.
- S02-SH-1083, S02-SH-1084: a new row, S02-V-303 (S02-VP-05): the admin's 'Registered legal business name is required' and its API's 'Legal entity must have exactly one account representative.', when the store's entity was saved as a Single Member LLC: the platform checks the business entity's details, a check of the record that holds the store's country (rule 4). No row of S02-VP-05 named the platform alone (a call, below).
- S02-SH-1087: joined S02-V-059 (S02-VP-06): the switch's choices of the organization's entities, by country, a control in the store's admin.
- S02-SH-1154: joined S02-V-059 ('before you can switch business entities in your Shopify admin') and S02-V-065 (S02-VP-07: 'you need to deactivate all financial services before you can switch business entities', and 'Only the store owner can deactivate Shopify Payments').

Noted:
- S02-SH-1047 (b): the store's primary legal entity on tuu1u4-v0, '"countryCode":"US"': its words name no party that set, checked or changed it (rule 2)
- S02-SH-1050 (b): as under (a): the signup country's words don't say whose country it is (rule 2's role test), as RD1-S5 noted S02-SH-1003 to S02-SH-1005
- S02-SH-1051 (b): the store's business entities, the primary with '"countryCode":"US"' and an archived one with '"countryCode":"YE"': their words name no party that set, checked or changed them (rule 2)
- S02-SH-1055 (b): the call sends no country: it names no party that sets the store's country (rule 2), as RD1-S5 noted S02-SH-1006
- S02-SH-1058 (b): as S02-SH-1047, on capture-us-plus
- S02-SH-1075 (b): the first step of Shopify Payments' set-up, where the seller says how the store is run ('I am running my store as: [x] An individual'): it sets the business type, not the store's country, and names no party that checks it (rule 2). Its (c) is placed below
- S02-SH-1080 (b): the set-up's call records the seller's answer, '"kind": "INDIVIDUAL"', with the entity's '"countryCode": "US"': as S02-SH-1075. Its (c) is placed below
- S02-SH-1081 (b): as S02-SH-1047, on capture-us-plus
- S02-SH-1086 (b): the store's primary legal entity after the save, still 'capture us plus - entity' with '"countryCode":"US"' and '"category":"INDIVIDUAL"', and the entities assignable to the shop: names no party that sets, checks or changes the store's country (rule 2)

x_words took 'I’m selling from; Business location' under S02-VP-04 and 'Legal entity' under S02-VP-05.

### Place tasks, capture round: shopify (c) (part RD1-S6)

Placed:
- S02-SH-1075, S02-SH-1076, S02-SH-1077, S02-SH-1078, S02-SH-1079, S02-SH-1080: joined S02-V-108 (S02-VP-10), the business entity's country code: capture-us-plus's Shopify Payments set-up for its US entity, with its US registration, identification numbers and documents. S02-SH-1079 by its scope, which names the entity's country (a reading, as for S02-SH-326 and S02-SH-327 in that row).
- S02-SH-1054, S02-SH-1061, S02-SH-1068: joined S02-V-115 (S02-VP-11), the business entity: Shopify Payments' account and eligibility held per business entity, not eligible for capture-gb-plus's Yemen entity and eligible for its US entity.
- S02-SH-1062: joined S02-V-122 (S02-VP-12), the business entity: third-party or manual payment methods may need reconnecting after changing business entity.
- S02-SH-1048, S02-SH-1049: joined S02-V-244 (S02-VP-14), where the business is based: the plan's price at the same checkout, $39 a month with the United States and $27 with Yemen.
- S02-SH-1064: joined S02-V-129 (S02-VP-14) and S02-V-139 (S02-VP-17), the words of S02-SH-261, which both rows hold.
- S02-SH-1044, S02-SH-1056, S02-SH-1067: joined S02-V-136 (S02-VP-16) and S02-V-139 (S02-VP-17), 'Business entity used for financial products, markets, apps, and taxes in this shop', the words of S02-SH-318, which both rows hold. a2.tsv also leads S02-SH-1041, S02-SH-1044, S02-SH-1056 and S02-SH-1067 to S02-VP-18: each shows the store's currency beside its country, and none says what decides it (a call, below).

Noted:
- S02-SH-1041 (c): the new store's addresses, '"countryCodeV2":"US"', beside its '"currencyCode":"USD"': its words don't say what decides the currency (rule 4)
- S02-SH-1052 (c): the mail 'Payment settings changed', 'My Store Admin deactivated Shopify Payments as a payment provider': it names who changed the setting, not what decides whether or how the store can use Shopify Payments (rule 4)
- S02-SH-1053 (c): Settings > Payments of tuu1u4-v0 offers Shopify Payments ('Complete setup'), with 'Card rates starting at 2.5% + $0.30': its words name no decider (rule 4)
- S02-SH-1069 (c): Settings > Payments of capture-gb-plus after the switch: 'Development stores can only process test payments', and Shopify Payments with 'Card rates starting at 3.5% + $0.30': the store's type, a development store, is no decider of rule 1's table, and its words name no other (rule 4). Named in S02-VP-11's note
- S02-SH-1070 (c): Managed Markets' '"ineligibilityReasons":["UNSUPPORTED_REGION","MISSING_SHOPIFY_PAYMENTS"]' on capture-gb-plus with its US entity and New York address: Shopify Payments is no decider of rule 1's table, and 'UNSUPPORTED_REGION' doesn't say whose region (rule 4; rule 2's role test). Named in S02-VP-17's note
- S02-SH-1071 (c): the Markets page's query 'ManagedMarketsShopAddress' returns the shop's billing address, in New York: its words don't say the address decides Managed Markets, or anything else (rule 4). Its (a) is placed above
- S02-SH-1074 (c): Settings > Payments of capture-us-plus: 'Development stores can only process test payments', and Shopify Payments with 'Card rates starting at 2.5% + $0.30': as S02-SH-1069

x_words took 'documentRequirements; Identification numbers' under S02-VP-10, 'third-party or manual payment methods' under S02-VP-12 and 'Basic plan' under S02-VP-14.

### Rows replaced, removed, added and joined (part RD1-S6)

Replaced: S02-V-058 (gap S02-SH-G09, now gap S02-SH-G14); S02-V-267 (the same answer, joined by S02-SH-1063, its evidence naming S02-SH-G14 where it named S02-SH-G09). None removed. Added: S02-V-302 (S02-VP-07, 'Street can't be blank - listitem: City can't be blank') and S02-V-303 (S02-VP-05, 'Legal entity must have exactly one account representative.'). Joined, all Shopify's: S02-V-001, S02-V-002, S02-V-003, S02-V-004, S02-V-005, S02-V-006 and S02-V-265 (S02-VP-01); S02-V-053 and S02-V-054 (S02-VP-04); S02-V-059 (S02-VP-06); S02-V-065 and S02-V-066 (S02-VP-07); S02-V-108 (S02-VP-10); S02-V-115 (S02-VP-11); S02-V-122 (S02-VP-12); S02-V-129 and S02-V-244 (S02-VP-14); S02-V-136 (S02-VP-16); S02-V-139 (S02-VP-17). Each joined row's evidence names what was added, after "Second pass, RD1-S6", and keeps each statement's scope: the store, its plan, and the run and step. Points' notes: S02-VP-11 and S02-VP-17. x_words: Shopify's under S02-VP-01, S02-VP-04, S02-VP-05, S02-VP-10, S02-VP-12 and S02-VP-14. S02-V-053's note named S02-SH-G02 as the gap that asks which field 'I'm located in:' sets; it was replaced, keeping the row's variant, statements and evidence, with what run 20261027T175456Z shows (call 11).

### Candidates for a new point (part RD1-S6)

None. Each statement placed answers one of its bullet's questions for an X of one of rule 1's kinds. Each statement noted answers none of its bullet's questions, names no decider of rule 1's table, or fails the role test; none was noted because its X fits no point's kind.

### Searches (part RD1-S6)

No point was raised, so no earlier platform's rows were searched for. To place the round's statements beside the rows that hold their like, Shopify's rows were read under S02-VP-01, S02-VP-04 to S02-VP-07, S02-VP-10 to S02-VP-12, S02-VP-14 and S02-VP-16 to S02-VP-18; the full rows of S02-V-053, S02-V-058, S02-V-059, S02-V-066, S02-V-108, S02-V-115, S02-V-122 and S02-V-267; the statements S02-SH-437, S02-SH-438 and S02-SH-450 (an earlier save of a business entity's details, in S02-V-053); and S02-SH-1031 to S02-SH-1033 (the revisit's earlier leads).

### Rechecks (part RD1-S6)

Each row joined was compared with its own platform's statements already in it (rule 5). Its basis, `answers`, holds for each statement joined: by the statement's words, or, where rule 5 allows, by its identifier or scope (S02-SH-1035, S02-SH-1048, S02-SH-1049, S02-SH-1066, S02-SH-1079, S02-SH-1082). The new rows, S02-V-302 and S02-V-303, rest on `answers` alone: their points' `raised_by` holds no other platform's statement.

### Calls (part RD1-S6)

1. The slice: RD1's slice held none of the round's statements, and this part cut it again on a copy in its scratch folder (above). The coordinator may cut the slices again in place; the cut reads the same phase A files.
2. S02-SH-1083 and S02-SH-1084 raised S02-V-303 under S02-VP-05 (who checks): the admin's own messages on saving a business entity's details, read as the platform's check of the business entity (rule 4: a check of the business entity is a check of X; what a platform's code does is the platform's). S02-SH-437 ('Couldn't save changes', 'Assign a business representative'), an earlier statement of the same kind, sits in S02-V-053 and S02-V-059 and not under S02-VP-05; no task led to it, and it is left. Read instead as a requirement of the form, S02-SH-1083 and S02-SH-1084 would join S02-V-053 beside S02-SH-437, and S02-V-303 would go.
3. S02-SH-1088 and S02-SH-1089 are noted under (b), and S02-SH-1087 placed: capture-us-plus's switch went from one US entity to another, so the store's country didn't change, while the dialog of S02-SH-1087 offers an entity in Yemen too, a control that can change it. Read as a change of the business entity, the record that holds the store's country, S02-SH-1088 and S02-SH-1089 would join S02-V-059.
4. S02-SH-1050 is noted under (a) and (b), as RD1-S5 noted S02-SH-1002 to S02-SH-1005: the signup country's words don't say whose it is. Read with S02-SH-1049, whose step is the same and whose combobox is 'Business location', it would join S02-V-053 under (b), and S02-VP-01 under (a) (a reading).
5. S02-SH-1035 joined S02-V-054, the platform, by its scope: 'Yemen' was selected before any input, on a sign-up from a network in Yemen. That the page set it by default is a reading.
6. S02-SH-1048 and S02-SH-1049: the plan checkout's 'I’m selling from' (combobox 'Business location') is read as the business's location, the store's own country (rule 1), not a place the store sells at. Read otherwise, both would be noted under (b) and (c).
7. S02-SH-1075 to S02-SH-1080 joined S02-V-108 by the reading that row already makes: each set-up shows, under its entity's country code, what it asks for. a2.tsv also leads S02-SH-1075, S02-SH-1076, S02-SH-1077 and S02-SH-1080 to S02-VP-11; they were placed under S02-VP-10 only, since what they show is what the set-up asks the merchant to provide.
8. S02-VP-18 (the store's defaults): a2.tsv leads S02-SH-1041, S02-SH-1044, S02-SH-1056 and S02-SH-1067 to it. Each shows the store's currency beside its country: US Dollar on the US stores, and Yemeni Rial still after capture-gb-plus's switch to a US entity (S02-SH-1067). None says what decides the currency, so none is placed there (rule 4).
9. S02-SH-1054, S02-SH-1061 and S02-SH-1068 joined S02-V-115 (the business entity), since the shop API holds Shopify Payments' account and eligibility under each business entity.
10. S02-V-302 holds a condition met on one store on one day, a store address with a street and a city, as the run showed it. It is a row of its own, apart from S02-V-066's same-country condition.
11. S02-V-053's note named S02-SH-G02, which S02-SH-G10 replaced. The checker reads only a row's `gap_ids`, and this part doesn't read whether gap-closing recorded S02-SH-G10 as answered, so the note now gives what the run shows, on one store on one day: chosen as United States from a network in Yemen, 'I'm located in:' filled the sign-up's country, and the new store held US as its countryCode, its addresses' and its business entity's. If the coordinator reads S02-SH-G10 as still open, the note should name it as open instead.

### Problems (part RD1-S6)

1. RD1's slice, cut at 19:21 on 27 October, held none of the capture round's statements, and `kinds.tsv` had no kind for 68 of them, though the work list, written at 23:50, names them. The printer named them as outside RD1's slice, which the brief reads as "under none of your root decision's bullets"; read so, all 70 place tasks would have been left. This part cut the slice again on a copy (above).
2. The task message points to Shopify's `notes.md` sections "Part A2-SH-R1" and "Part A2-SH-R2", and to the statements' `note` column ("answers S02-SH-Gnn"), which the brief says not to read. This part read neither: it read `a2.tsv` and the gaps' own words in the slice, and left the checker to name rows that name a settled gap.
3. `second_pass_list.py --check` keys on (task, id, bullet), so RD1-S5's ledger line for the same revisit satisfied it before this part ran: the check can't show whether this part's revisit was done. The ledger holds a second line for it.

### Check (part RD1-S6)

On a copy holding only `b/RD1`, `merge_slices.py` merged 19 points and 303 rows. `check_subject.py` gave 247 lines of level `error`, all in `answers.tsv`, each 'not a variation point' for a point of RD2 or RD3 (S02-VP-26 to S02-VP-92), which the copy leaves out; none names this part's rows or statements. Before this part wrote, the checker run on the copy that cut the slice named S02-V-058 ('gap S02-SH-G09 was narrowed into S02-SH-G14'), which the revisit replaced; that line is gone. It gave 17 warnings, on phase A's citations (16 of Shopify's, 1 of WooCommerce's), and 33 reviews: 12 quotes found only in a page's source, which are the coordinator's; the statements of RD2 and RD3, whose folders the copy leaves out; and 19 points with no phase C row yet. Its `unplaced.tsv` holds no row of RD1: the place tasks and the revisit's leads are gone from it. `second_pass_list.py --check`: RD1 has no revisit, reread or note task without a row in `done.tsv`, as before this part (problem 3).

## Second pass, RD1-S7

Part RD1-S7: the Salla and Zid round's Salla tasks under RD1 (bullets a to d), from A2-SA-R, which read the runs of 28 October for capture requests H-001 to H-005 (observed-sa b0bd0b16). Most of the statements are observations of one store on one day; each row keeps the store, its plan, and the run and step, in its scope or evidence.

### Revisit S02-V-074 and S02-V-075 (salla, S02-VP-06 and S02-VP-07, who changes the store's country, and on what conditions) (part RD1-S7)

- S02-V-074 (S02-VP-06), was gap S02-SA-G01: replaced with an answer, 'As the store owner, you can make this change.' (S02-SA-483): the store owner, its own answer beside the seller's, by rule 4. S02-SA-483 is the answer of Mushammir, the dashboard's assistant, on the merchant store store-1-da (Basic), run 20261028T150337Z-journey-store-country-merchant-en, step 011, marked AI-generated, as its scope says.
- S02-SA-483 also joined S02-V-095 (S02-VP-06, the seller): 'You can change the store country after creation from Settings > Store settings > Basic store settings, then update the country/currency and save', a control in the store's admin, by rule 4. Rechecked under rule 5: S02-V-095's basis stays `answers`.
- S02-V-307 (S02-VP-06), added: gap S02-SA-G16, in place of S02-SA-G01, beside the answers. It asks who can change the store's country as a page, a setting or a person of Salla's states it, and names S02-SA-483 as AI-generated. S02-V-095's note now names S02-SA-G16 in S02-SA-G01's place.
- S02-V-075 (S02-VP-07), was gap S02-SA-G01: replaced with gap S02-SA-G16 (in place of S02-SA-G01). No lead states a condition. S02-SA-483 names who changes it, under S02-VP-06.

Leads noted under (b):
- S02-SA-477 (b): the merchant store's settings menu (store-1-da, Basic; run 20261028T150337Z, step 002) lists its items, none of which names the store's country, a party that changes it, or a condition; answers none of (b)'s questions
- S02-SA-478 (b): the General section's items (Store information, Store design, Languages, Currencies) name no party that sets, checks or changes the store's country, and no condition; answers none of (b)'s questions
- S02-SA-479 (b): the General section's items (Salla AI Connector, Salla Community, Latest platform updates) say nothing of the store's country; answers none of (b)'s questions
- S02-SA-480 (b): the General section's items (Clear cache, Maintenance mode, Delete store) say nothing of the store's country; answers none of (b)'s questions
- S02-SA-481 (b): the Store information page shows a Store activity field and Save, with no field for the store's country and no party for it; answers none of (b)'s questions
- S02-SA-482 (b): the store list (Store, Store website, Plan, Role 'مدير عام') names the account's role in the store, not who sets, checks or changes the store's country; answers none of (b)'s questions

### Revisit S02-V-168 (salla, S02-VP-18, the store's defaults) (part RD1-S7)

S02-V-168, was gap S02-SA-G07: replaced with gap S02-SA-G18, in place of S02-SA-G07. S02-SA-G18 asks only whether the store's country, chosen at onboarding, sets the default language. No lead names what decides a default (rule 4). S02-VP-18's note now names S02-SA-G18 for Salla's row.

Leads noted under (c):
- S02-SA-499 (c): the plans after onboarding, 'Plus For small businesses 99.00 AED Month', on the new UAE store (store 21123834; run 20261028T174130Z, step 040): its words don't say what decides the price or its currency (rule 4), and the page's words tie it to no country
- S02-SA-500 (c): 'Pro For established companies 299.00 AED Month', on the same store and step: as S02-SA-499
- S02-SA-501 (c): the new UAE store's information, '"currency":"AED"' beside '"kyc_country":"AE"' (store 21123834, Basic; run 20261028T174130Z, responses/0451.json): its words don't say what decides the currency (rule 4), as RD1-S6 noted S02-SH-1041. Its (a) is placed below
- S02-SA-515 (c): an app's price in the App Store, '96.94 AED67.57 AED / Monthly', on the new UAE store (run 20261028T174130Z, step 051): its words don't say what decides the price or its currency (rule 4)
- S02-SA-516 (c): the same app's price, '99 69 / Monthly', on the merchant store store-1-da (Basic; run 20261028T181625Z, step 002): as S02-SA-515

S02-SA-387, S02-SA-388, S02-SA-390, S02-SA-391, S02-SA-392, S02-SA-393 and S02-SA-400, the earlier leads, stay noted under (c), with the reasons given above in this file; the new run adds nothing to them.

### Revisit S02-V-241 (salla, S02-VP-19, the store's data) (part RD1-S7)

S02-V-241, was gap S02-SA-G05: replaced with gap S02-SA-G17, in place of S02-SA-G05. It stands beside S02-V-219 (every store), which doesn't say where the data is held. The earlier leads stay where they are: S02-SA-319 to S02-SA-321, S02-SA-324, S02-SA-325, S02-SA-328 and S02-SA-335 to S02-SA-338 in S02-V-219, and S02-SA-322, S02-SA-323, S02-SA-326, S02-SA-327, S02-SA-329 and S02-SA-332 noted above in this file.

Leads noted under (c):
- S02-SA-510 (c): a report export's download, 'https://sallaexport.s3.amazonaws.com/...', its credential naming 'eu-central-1', on the demo store (run 20261008T213916Z, responses/0291.json): where one file is held, with no decider named (rule 4)
- S02-SA-511 (c): the advanced import's file, 'https://migration-stores.s3.eu-central-1.amazonaws.com/...', on the demo store (run 20261008T171647Z, responses/0063.json): as S02-SA-510
- S02-SA-512 (c): a verification document, the store's 'cr_license_document', at 'https://storage.googleapis.com/salla-274413-kyb-api-documents/...', its credential naming the region 'auto', on the new UAE store (store 21123834, Basic; run 20261028T182142Z, responses/0053.json): where one file is held, and a document the store provided, with no decider named for either (rule 4); a2.tsv also leads it to S02-VP-10

### Revisit S02-V-027 (salla, S02-VP-02, the countries kept out), with the place task S02-SA-491 (d) (part RD1-S7)

S02-V-027, was gap S02-SA-G04, which gap-closing settled (the work list names no gap or absence for it): replaced with an answer, 'We’ll notify you when Salla becomes available in your country.' (S02-SA-492). Its identifier says it is the onboarding's answer to 'Where is your business based?' answered 'Other country', and the step offers only 'Back to log in': the countries kept out, as the onboarding shows them, are 'Other country', every country beside the six its options list (S02-SA-491).

Placed under S02-VP-03 (what countries fill), from the revisit's leads:
- S02-SA-463, S02-SA-465 (the Saudi path's answer to 'Can I use Salla outside Saudi Arabia?', in English and Arabic: Saudi Arabia and the UAE, 'coming soon to the rest of the GCC') and S02-SA-492 (the onboarding's message: 'We’re currently available in Saudi Arabia and the UAE'): joined S02-V-020, the same two countries.
- S02-SA-464, S02-SA-466 (the UAE path's answer, in English and Arabic), S02-SA-475, S02-SA-476 (the plans pages' footer, 'Available in' and 'مدعوم في') and the place task's S02-SA-491 (the onboarding's options): a new row, S02-V-304, the same six countries: Saudi Arabia, the United Arab Emirates, Kuwait, Qatar, Oman and Bahrain.

x_words took 'available in your country' under S02-VP-02, and 'currently available in; Available in' under S02-VP-03.

### Place tasks, Salla and Zid round: salla (a) and (b) (part RD1-S7)

Placed:
- S02-SA-490, under (a): joined S02-V-013 (S02-VP-01), the onboarding's question by its slug 'store-country', now 'Where is your business based?', 'Select the country where your business is legally registered or where you issue official documents' (run 20261028T174130Z, responses/0033.json).
- S02-SA-501, under (a): joined S02-V-301 (S02-VP-01), the key 'kyc_country', '"kyc_country":"AE"' in the store's information of the new UAE store (store 21123834, Basic; run 20261028T174130Z, responses/0451.json).
- S02-SA-490, under (b): joined S02-V-072 (S02-VP-04), the seller: the merchant selects the country in the onboarding, '"is_mandatory":true'.

Noted:
- S02-SA-477 (a): the merchant store's settings menu (store-1-da, Basic; run 20261028T150337Z, step 002) lists its items, none of which is a field or record holding the store's country; answers none of (a)'s questions
- S02-SA-478 (a): the General section's items (Store information, Store design, Languages, Currencies) hold no field for the store's country; answers none of (a)'s questions
- S02-SA-479 (a): the General section's items (Salla AI Connector, Salla Community, Latest platform updates) hold no field for the store's country; answers none of (a)'s questions
- S02-SA-480 (a): the General section's items (Clear cache, Maintenance mode, Delete store) hold no field for the store's country; answers none of (a)'s questions
- S02-SA-481 (a): the Store information page (step 003) shows 'Store activity' and Save, and no field for the store's country; answers none of (a)'s questions
- S02-SA-482 (a): the store list (step 005) shows Store, Store website, Plan and Role, and no country; answers none of (a)'s questions
- S02-SA-489 (a): the sign-up's body keys, '"name","email","mobile","country_code","password"' (run 20261028T164828Z, writes.jsonl): 'country_code', beside 'mobile', doesn't say whose country it is (rule 2's role test)
- S02-SA-489 (b): as under (a): the key doesn't say whose country it is (rule 2's role test), and the body names no party that sets the store's country

x_words took 'Where is your business based?; kyc_country' under S02-VP-01, 'Where is your business based?' under S02-VP-04, and 'store country' under S02-VP-06.

### Place tasks, Salla and Zid round: salla (c) (part RD1-S7)

Placed:
- S02-SA-467, S02-SA-468, S02-SA-469, S02-SA-470: a new row, S02-V-305 (S02-VP-10), the merchant's country, by the coordinator's ruling of 27 October 2026 (a reading): the plans pages' answer to 'What do I need to start a store on Salla?' names 'A Saudi mobile number' and 'A Saudi bank account' on the Saudi paths (salla.com/en-sa/plans, salla.com/plans) and no country on the UAE paths (salla.com/en-ae/plans, salla.com/ar-ae/plans). The paths' codes tie each page to one country; the words don't name the country's merchants.
- S02-SA-488: joined S02-V-305 (S02-VP-10): the merchant store's verification form renders the schema 'merchants_saudi_kyc' (store-1-da, Basic; run 20261028T150337Z, responses/0226.json), the platform's identifier tying the form to Saudi merchants (a reading).
- S02-SA-485: joined S02-V-154 (S02-VP-10), the owner's residence: 'For Citizens and Residents', the words of S02-SA-117 in English, on store-1-da's Store Verification page (step 006).
- S02-SA-490, S02-SA-493, S02-SA-494, S02-SA-495, S02-SA-496, S02-SA-497, S02-SA-498: joined S02-V-152 (S02-VP-10), the country selected in the onboarding (run 20261028T174130Z): 'We'll use this to apply the correct regulations to your store' (S02-SA-490, a reading: the regulations read as S02-SA-284's legal requirements); the legal entities offered for the country queried, each slug carrying its code (S02-SA-493 to S02-SA-497, a reading: the legal entity as part of what the merchant provides); 'Do you have the legal requirements to sell in the UAE?' with its documents (S02-SA-498).
- S02-SA-471, S02-SA-472, S02-SA-473, S02-SA-474: joined S02-V-158 (S02-VP-12), the merchant's country, by the coordinator's ruling (a reading): 'What payment methods does Salla support?' names Mada, cards, Apple Pay, cash on delivery and Buy Now, Pay Later on the Saudi paths, and the same without Mada on the UAE paths. None names Salla Payments, so none is placed under S02-VP-11.
- S02-SA-498: also a new row, S02-V-306 (S02-VP-13, payouts): 'To activate your store and receive payouts you need: ... Business bank account (UAE)', on the onboarding whose country was the United Arab Emirates (its scope).

Noted:
- S02-SA-484 (c): store-1-da's Store Verification requirement '1. Freelance Work Permit For Saudi Citizens Only' (step 006): the owner's nationality, outside the decider's role, as S02-V-153's note says of S02-SA-116; its scope names the store and no country; names no decider (rule 4)
- S02-SA-486 (c): the verification's requirements preview, '"consent":true' and its next states (store_owner_details, government_documents, bank_account, review_confirm, finish), on store-1-da (responses/0229.json): the verification's steps, with no decider named (rule 4)
- S02-SA-487 (c): store-1-da's Store Owner Details step, the owner's mobile 'registered in Absher' and 'national ID or Iqama number consisting of 10 digits' (step 008): names no decider (rule 4)

x_words took 'requirements for creating a store on Salla; Choose your legal entity; Store Verification; merchants_saudi_kyc' under S02-VP-10, 'payment options' under S02-VP-12, and 'receive payouts' under S02-VP-13.

### Rows replaced, removed, added and joined (part RD1-S7)

Replaced: S02-V-074 (S02-VP-06, gap S02-SA-G01, now 'As the store owner, you can make this change.', S02-SA-483); S02-V-075 (S02-VP-07, gap S02-SA-G01, now gap S02-SA-G16); S02-V-168 (S02-VP-18, gap S02-SA-G07, now gap S02-SA-G18); S02-V-241 (S02-VP-19, gap S02-SA-G05, now gap S02-SA-G17); S02-V-027 (S02-VP-02, gap S02-SA-G04, now 'We’ll notify you when Salla becomes available in your country.', S02-SA-492). None removed. Added: S02-V-307 (S02-VP-06, gap S02-SA-G16), S02-V-304 (S02-VP-03, the six countries), S02-V-305 (S02-VP-10, the merchant's country), S02-V-306 (S02-VP-13, a business bank account in the UAE). Joined, all Salla's: S02-V-013 and S02-V-301 (S02-VP-01); S02-V-020 (S02-VP-03); S02-V-072 (S02-VP-04); S02-V-095 (S02-VP-06); S02-V-152 and S02-V-154 (S02-VP-10); S02-V-158 (S02-VP-12). Each joined row's evidence names what was added, after "second pass, RD1-S7", with the store, its plan, and the run and step. Notes added: S02-VP-18's (Salla's row now S02-SA-G18's gap) and S02-V-095's (S02-SA-G16 in S02-SA-G01's place).

S02-V-303 is the id that RD1-S6's notes, above, give to a Shopify row under S02-VP-05, which was removed after that part (its statements, S02-SH-1083 and S02-SH-1084, are now in S02-V-053). `add` gave the id again, as the next after the folder's last. Here it names the Salla gap row under S02-VP-06. (The coordinator renumbered this part's row S02-V-307 on 28 October, so that each id names one row; `add` no longer gives an id that a ledger or note has named.)

### Candidates for a new point (part RD1-S7)

None noted. Two placements rest on a reading (calls 5 and 6, below). If the coordinator rejects those readings, they are candidates:
- S02-SA-490, under (c): X 'the correct regulations', which 'Where is your business based?' is used to apply to the store. The question it answers: what decides the regulations applied to the store. Placed in S02-V-152 (documents and checks), read as S02-SA-284's legal requirements.
- S02-SA-493 to S02-SA-497, under (c): X 'legal entity', from 'Choose your legal entity'. The question they answer: what decides which legal entities a store can register as. The options differ by the country queried. Placed in S02-V-152 (documents and checks), read as part of what the merchant provides.

### Searches (part RD1-S7)

No point was raised, so no earlier platform's rows were searched for. To place the round's statements beside the rows that hold their like, this part read: Salla's rows under S02-VP-01 to S02-VP-04, S02-VP-06 to S02-VP-13, S02-VP-18 and S02-VP-19; every platform's rows under S02-VP-06, S02-VP-07 and S02-VP-18; the full rows of S02-V-095, S02-V-151 to S02-V-154, S02-V-157, S02-V-158 and S02-V-179; and Zid's rows under S02-VP-10, by their excerpts. In this file, it searched for the earlier notes on S02-SA-387 to S02-SA-400, and for 'en-ae', 'ar-ae', 'en-sa', 'Saudi path', 'UAE path' and 'ties the', to see how earlier parts read salla.com's paths. It found S02-SA-256 and S02-SA-295, noted in the first pass (call 3).

### Rechecks (part RD1-S7)

Each row joined was compared with its own platform's statements already in it (rule 5). Its basis, `answers`, holds for each statement joined: S02-V-013, S02-V-020, S02-V-072, S02-V-095, S02-V-152, S02-V-154, S02-V-158 and S02-V-301. The new and replaced answer rows rest on `answers` alone: S02-V-027, S02-V-074, S02-V-304, S02-V-305 and S02-V-306. Their points' `raised_by` statements from other platforms share no term, identifier or definition with them. S02-V-074's 'store owner' isn't S02-SH-579's 'account owner of the store' in the same words.

### Calls (part RD1-S7)

1. S02-SA-483, the dashboard assistant's answer, is placed although its scope marks it AI-generated. It gives two answers: the store owner (S02-V-074) and the seller (joined S02-V-095). S02-SA-G16 stands beside them, as S02-V-307, since it asks for the answer as a page, a setting or a person of Salla's states it. If an answer marked AI-generated isn't to be placed, S02-SA-483 would be noted, S02-V-074 would be gap S02-SA-G16, and S02-V-307 would go.
2. S02-SA-492 answers S02-VP-02 by its identifier, 'answered Other country': the countries kept out are 'Other country', as the onboarding shows them. Read as S02-V-027's earlier note read S02-SA-020 (the same message in Arabic: it 'names no country kept out'), S02-SA-492 would sit under S02-VP-03 only, and S02-V-027 would be `not covered`, since gap-closing settled S02-SA-G04. S02-SA-020 itself is left in S02-V-020: no task leads to it.
3. salla.com's paths are read as tying a page to one country, by the coordinator's ruling of 27 October 2026 (a reading): 'en-sa' and the default path to Saudi Arabia, 'en-ae' and 'ar-ae' to the UAE, as phase A's scopes name them. That gives S02-V-305 (S02-VP-10) and the joins to S02-V-158 (S02-VP-12). Earlier, in the first pass, S02-SA-256 and S02-SA-295 were noted with 'the path is the site's, not a field or record of the store', before the ruling, and have no reread task. Read the other way, S02-SA-467 to S02-SA-474 would be noted, and S02-V-305 would hold only S02-SA-488.
4. S02-SA-488's schema id, 'merchants_saudi_kyc', is read as tying the merchant store's verification form to Saudi merchants (a reading: an identifier, not a heading). S02-SA-484, S02-SA-486 and S02-SA-487 come from the same run and form, and their own words name no decider, so they are noted. Read together with S02-SA-488, they would join S02-V-305.
5. In S02-SA-490 (c), 'We'll use this to apply the correct regulations to your store' is read as S02-SA-284's 'legal requirements' (S02-V-152, documents and checks), since the same description names 'where you issue official documents'. Read otherwise, it fits no kind of (c) (above).
6. S02-SA-493 to S02-SA-497: the legal entities the onboarding offers for the country it queries are read as part of what the merchant provides to verify the business (documents and checks), as a2.tsv also leads them. Read otherwise, they fit no kind of (c) (above).
7. S02-SA-498 answers two points. Its documents join S02-V-152 (S02-VP-10), and 'receive payouts ... Business bank account (UAE)' raises S02-V-306 (S02-VP-13). a2.tsv doesn't lead it to S02-VP-13. Its decider is the onboarding's country, from its scope. Its words 'to sell in the UAE' name the same country.
8. S02-SA-501 is placed under (a), as kyc_country (S02-V-301), and noted under (c), as RD1-S6 noted S02-SH-1041. Gap-closing narrowed S02-SA-G07 into S02-SA-G18, which asks only about the default language. So, under S02-VP-18, Salla's default currency now has neither an answer row nor a gap. If the coordinator reads S02-SA-501 with its scope (a store whose onboarding answered the UAE holds the currency AED) as the store's country deciding the currency, it would raise a Salla answer row there (a reading).

### Problems (part RD1-S7)

1. Six statements are in RD1's slice and in `unplaced.tsv`, but no task in the work list names them: S02-SA-504 to S02-SA-509 (c). They are Salla's, from the same runs of 28 October. a2.tsv leads them to S02-VP-08, with S02-SA-G02 still open, and all but S02-SA-507 and S02-SA-509 to S02-VP-10 as well. S02-V-148, S02-SA-G02's gap row under S02-VP-08, has no revisit task either. This part left them all, since no task leads to them. From their words: S02-SA-504 is the new UAE store's verification schema 'merchants_uae_kyb_workflow', and S02-SA-509 the verification's state 'my_fatoorah_review'.
2. `add` gives the id after the folder's last, so the id of a removed last row is given again (S02-V-303, above). (The coordinator renumbered this part's row S02-V-307 on 28 October, so that each id names one row; `add` no longer gives an id that a ledger or note has named.)

### Check (part RD1-S7)

This part ran the check on a copy holding only `b/RD1`. `merge_slices.py` merged 19 points and 306 rows. `check_subject.py` (3,073 statements, as phase A3 ran beside it) gave 5 lines of level `error`. All five are on Zid's rows of this round, which another part revisits: S02-V-038, S02-V-077, S02-V-170, S02-V-173 and S02-V-291, each naming a gap that was narrowed into another. None names this part's rows or statements. It gave 17 warnings, on phase A's citations, and 38 reviews, among them the quotes found only in a page's source, which are the coordinator's. In its `unplaced.tsv`, RD1's only Salla rows are S02-SA-504 to S02-SA-509 (c), for which the work list has no task (problem 1). This part's place tasks and its revisits' leads are gone from it. In `second_pass_list.py --check`, RD1's open tasks are four revisits of Zid's (S02-V-077, S02-V-170, S02-V-173, S02-V-291). This part's five revisits are gone from it.

## Second pass, RD1-S8

Part RD1-S8: the Salla and Zid round's Zid tasks under RD1 (bullets a to d), from A2-ZD-R and A3-ZD-R (other-product-class f44be3f, folder `zid/`); Salla's revisit of S02-V-148, which the round's first task list dropped; and six tasks of the coordinator's rulings on RD1-S7's calls (b/second-pass.md). Zid's statements are observations of two stores on 28 October: the development store 3277610 (plan new_professional.lifetime) and the public demo 127604 (Professional), both with the feature flag `must_use_markets_pricing` false. Each row keeps the store, its plan, the flag, and the run and step, in its scope or evidence.

### Revisit S02-V-077 (zid, S02-VP-05, who checks the store's country) (part RD1-S8)

S02-V-077, was gap S02-ZD-G02: replaced with gap S02-ZD-G30, in place of S02-ZD-G02. S02-ZD-G30 asks who checks the country and address of a store outside Saudi Arabia, and how, after they are saved. No lead names a party that checks.

Leads placed under (b):
- S02-ZD-468: joined S02-V-078 (S02-VP-06, who changes the store's country): the business location gave Kuwait 'after Kuwait and Kuwait City were chosen on Business address and saved (steps 49 to 55, POST /v1/managers/store/business-place answered 200 at step 55)' (its scope), where it gave Saudi Arabia at step 22 (S02-ZD-467). Business address > Country > Save is a control in the store's admin, so the seller changes it (rule 4), as S02-V-078's 'في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر' says. It is a change of a value already set, so it isn't joined under S02-VP-04 (who sets) too (call 1).
- S02-ZD-469: a new row, S02-V-308 (S02-VP-07, what must hold before the store's country changes): 'District district cannot be null Street street cannot be null', on the first save after Kuwait and Kuwait City were chosen (step 52): the district and the street must be given before the save that changes the country goes through (a reading: the words name the fields the save requires).

Lead noted under (b):
- S02-ZD-470 (b): the business location after the save that set Kuwait, '"national_address_certificate":null,"is_address_confirmed":true' (development store 3277610; run 20261028T170107Z-devstore-markets-en, steps 55 and 56): two keys of the record, which name no party that checks the store's country or address, and no check after the save (S02-ZD-G30); answers none of (b)'s questions

### Revisit S02-V-170 and S02-V-173 (zid, S02-VP-08 and S02-VP-09, the contracting party and the terms) (part RD1-S8)

S02-V-170 (S02-VP-08) and S02-V-173 (S02-VP-09), each was gap S02-ZD-G03: each replaced with gap S02-ZD-G31, in place of S02-ZD-G03. S02-ZD-G31 asks which company contracts with a merchant outside Saudi Arabia, and under which terms.

Lead noted under (c):
- S02-ZD-484 (c): the Rise monthly checkout's link '- link "Terms and conditions": - /url: https://zid.sa/en/legal/terms-conditions', the same with the development store's Business address country Egypt, the UAE, Oman, Qatar, Syria, Bahrain, Saudi Arabia and Kuwait (its scope; runs 20261028T190952Z-devstore-country-checkout-en and 20261028T190230Z-devstore-billing-en): a link names no company that contracts (S02-VP-08); for the terms (S02-VP-09), its words name no decider, and its scope names eight countries, so it isn't 'every store, whatever its country' (rule 4) (call 2)

### Revisit S02-V-291 (zid, S02-VP-15, taxes on the platform's fees) (part RD1-S8)

S02-V-291, was gap S02-ZD-G08: replaced with an answer, '"name":"VAT %15","value":{"amount":13874,"currency":"EGP","formatted":"EGP 138.74"}' (S02-ZD-476 to S02-ZD-483): the Rise monthly checkout's VAT line on the development store, each with a different Business address country in its scope. Egypt gives EGP 138.74 on 991.00; the UAE, Oman, Qatar, Bahrain and Kuwait 0; the Syrian Arab Republic and Saudi Arabia SAR 1.17 on 7.83; each labelled 'VAT %15'. The decider is the store's own country as its Business address holds it (S02-V-029), a reading: the statements give the line for each country, and their words don't say what decides it. The coordinator read S02-SA-501's currency with its store's country the same way (28 October, on RD1-S7's call 8) (call 3).

S02-V-309 (S02-VP-15), added: gap S02-ZD-G32, in place of S02-ZD-G08, beside the answer. It asks what tax Zid's other fees carry for a store outside Saudi Arabia (the transaction fees, Zid Pay's fees, the apps' and services' fees), and the tax on the invoice Zid issues.

S02-V-310 (S02-VP-14, the platform's fees), added from the same leads: the invoice lines' 'VAT Subjected Amount' is in a currency for each Business address country (EGP, AED, OMR, QAR, SAR, BHD, KWD), the currency the subscription is billed in. Same decider and reading as S02-V-291. It stands beside S02-V-181 (the merchant's local currency; zid.eg's prices in Egyptian pounds), whose decider is another (call 3).

The earlier leads stay where they are: S02-ZD-193, S02-ZD-194, S02-ZD-197 and S02-ZD-203 in S02-V-182 (every store); S02-ZD-398, S02-ZD-408, S02-ZD-411 and S02-ZD-418 in S02-V-299; S02-ZD-192, S02-ZD-195, S02-ZD-196, S02-ZD-198 to S02-ZD-202, S02-ZD-204 and S02-ZD-205 noted under (c) above in this file.

x_words took 'VAT %15' under S02-VP-15, and 'Rise - Monthly; VAT Subjected Amount' under S02-VP-14.

### Revisit S02-V-038 (zid, S02-VP-02, the countries kept out) (part RD1-S8)

S02-V-038, was gap S02-ZD-G09: replaced with gap S02-ZD-G33, in place of S02-ZD-G09. S02-ZD-G33 asks which countries, if any, Zid keeps out of creating a store at its public sign-up. The work list also names absence S02-ZD-N17: Iran, Cuba, Korea (North or South), Russia and Israel are not among the 162 countries a store can take as its Business address's country. Its audit contradicts it (zid/absence-audit.tsv). The cities endpoint, GET /v1/settings/cities?per_page=3000 (run 20261028T190952Z-devstore-country-checkout-en, step 74), names cities of 43 countries outside the 162, among them the five of S02-ZD-495 to S02-ZD-499. So the 162 are not all the countries Zid's API holds, and the list isn't shown complete. What still stands: none of the five is among the 162 that the Business address page lists (step 48) and the countries endpoint answers; whether a store can take any of them as its country isn't shown. An `absent` row needs a complete list (rule 4), so none rests on S02-ZD-N17. The row's note says so.

Lead noted under (d):
- S02-ZD-475 (d): the options of Business address's Country, 162 countries, from 'Saudi Arabia UAE Kuwait Oman Bahrain Egypt Qatar Jordan' to 'Palestinian South Sudan Isle of Man', Yemen and the Syrian Arab Republic among them (development store 3277610; run 20261028T170107Z-devstore-markets-en, step 48; 'GET /v1/settings/countries gives the same 162 names in the same order', its scope): their words don't say the countries are where Zid serves merchants, or name any it keeps out, as S02-SH-259's and S02-SA-312's options were read under (d)

### Revisit S02-V-148 (salla, S02-VP-08, the contracting party) (part RD1-S8)

S02-V-148, gap S02-SA-G02: replaced with the same gap, which the work list names as still open. S02-SA-G02 asks for the contracting party of the payment services contract ('عقد خدمات الدفع') that stores in the UAE and Kuwait sign during store verification. The new UAE store's verification (store 21123834, Basic; A2-SA-R, observed-sa b0bd0b16) names no contracting party. This task was missing from the round's first task list (RD1-S7's problem 1).

Leads placed under (c):
- S02-SA-504: joined S02-V-305 (S02-VP-10, the merchant's country, as the platform ties a page or form to one country): '"renderer_schema":{"id":"merchants_uae_kyb_workflow"', the platform's identifier tying the UAE store's verification form to the UAE's merchants (a reading), as the coordinator ruled S02-SA-488's 'merchants_saudi_kyc' names the merchant's country (28 October, on RD1-S7's call 4).
- S02-SA-505, S02-SA-506: joined S02-V-152 (S02-VP-10, the country selected for the store): the UAE store's Business Details step asks for 'Company Name*', 'TL/CR Number*', 'TL/CR Expiry Date*', 'Tax Registration Number (Optional)', 'TL/CR Document*', 'VAT Registration Certificate (Optional)' and 'Memorandum or Articles of Association'. Their identifier and scope name the UAE store, whose onboarding answered United Arab Emirates (S02-SA-501's scope). A reading: their words name no country, and S02-SA-284 says 'Your country selection sets the legal requirements for your store' (call 4).

Leads noted under (c):
- S02-SA-507 (c): the UAE store's declaration, 'I confirm that my Salla store information is accurate and up to date, and I agree to keep it updated and comply with applicable regulations and Salla's User Agreement.' (store 21123834, Basic): it names the terms the merchant agrees to, but no decider (rule 4), and no company that contracts; it isn't the payment services contract S02-SA-G02 asks about
- S02-SA-508 (c): the notice after submission, 'Your application has been received and is being reviewed. We will notify you via WhatsApp once a decision is made.' (store 21123834, Basic): a review of the verification, with no decider named (rule 4), and no contracting party
- S02-SA-509 (c): the verification's status after completion, '"status":"completed","current_state":"my_fatoorah_review"' (store 21123834, Basic; GET api.aws.salla.dev/kyc/api/kyc/status): it names a review state, not the party of a contract (S02-SA-G02), and no decider (rule 4)

### Revisit S02-V-074, S02-V-307 and S02-V-095 (salla, S02-VP-06, who changes the store's country), by the coordinator's ruling on RD1-S7's call 1 (part RD1-S8)

The coordinator ruled on 28 October (b/second-pass.md, RD1-S7's call 1) that S02-SA-483, the reply of Salla's dashboard assistant under the notice that responses are AI-generated, is a lead to S02-SA-G16, not an answer. So:
- S02-V-074, was 'As the store owner, you can make this change.' (S02-SA-483): replaced with gap S02-SA-G16.
- S02-V-307, the second gap row of S02-SA-G16 under the point: removed, since S02-V-074 now holds the gap.
- S02-V-095 (the seller): replaced without S02-SA-483, keeping S02-SA-179 and S02-SA-311, its excerpt 'اضغط (تحديد الموقع) لتحديد موقع المتجر من الخريطة', their basis `answers` and their evidence. Its note now names S02-SA-G16's row, S02-V-074, beside it.
- S02-V-075 (S02-VP-07, gap S02-SA-G16): its note took a line saying that S02-SA-483 is now noted.

Noted under (b):
- S02-SA-483 (b): the reply of Mushammir, the dashboard's assistant, 'You can change the store country after creation from Settings > Store settings > Basic store settings, then update the country/currency and save. As the store owner, you can make this change.' (store-1-da, Basic; run 20261028T150337Z-journey-store-country-merchant-en, step 011), under Salla's notice 'Responses are AI-generated. Verify what matters most.': an answer the platform's own assistant generates, under a notice that it may be wrong, is a lead to the gap it bears on (S02-SA-G16), not an answer (the coordinator's ruling of 28 October on RD1-S7's call 1)

### Place tasks, Salla and Zid round: zid (a) and (d) (part RD1-S8)

Placed:
- S02-ZD-467, S02-ZD-468, under (a): joined S02-V-029 (S02-VP-01, the business address, 'العنوان التجاري'). Their identifier names 'settings/information (Store information) > Business address (settings/information/address) > Country' and 'GET /v1/managers/store/business-place > business_location > country'. The record gave Saudi Arabia at step 22 (S02-ZD-467) and Kuwait after the save at step 55 (S02-ZD-468) (development store 3277610; run 20261028T170107Z-devstore-markets-en). The record's key, 'business_location', is the key S02-V-256 names in the account's profile ('user.business_location'), from another endpoint; they aren't joined there (call 5).

Noted:
- S02-ZD-495 (d): the cities endpoint's entry '"country_id":54,"country_name":"Cuba","country_code":"CU"' (GET /v1/settings/cities?per_page=3000&countries_ids=+; development store 3277610; run 20261028T190952Z-devstore-country-checkout-en, step 74): a country whose cities Zid's API holds; its words don't say Zid serves merchants there or keeps them out (rule 2's role test). With S02-ZD-496 to S02-ZD-499, it contradicts absence S02-ZD-N17's completeness (revisit S02-V-038, above)
- S02-ZD-496 (d): the same answer's entry '"country_id":101,"country_name":"Iran( Islamic Republic of)","country_code":"IR"': as S02-ZD-495
- S02-ZD-497 (d): the same answer's entry '"country_id":112,"country_name":"North Korea","country_code":"KP"': as S02-ZD-495
- S02-ZD-498 (d): the same answer's entry '"country_id":113,"country_name":"South Korea","country_code":"KR"': as S02-ZD-495
- S02-ZD-499 (d): the same answer's entry '"country_id":176,"country_name":"Russian Federation","country_code":"RU"': as S02-ZD-495

x_words took 'Business address; business_location' under S02-VP-01.

### Rereads, by the coordinator's rulings on RD1-S7's calls 3 and 8 (part RD1-S8)

Placed (each earlier note stays as it is):
- S02-SA-256 (c), the coordinator's ruling on call 3: a new row, S02-V-311 (S02-VP-14, the platform's fees). 'Salla Plus For small businesses AED 990 / year', on salla.com/en-ae/plans, the UAE path (its scope): the path's code, 'ae', ties the page to the UAE. So the decider is the merchant's country, the UAE, as the platform ties the page to it (a reading: the words don't name merchants), by rule 4 under (c) as ruled on 27 October. It stands beside S02-V-161 (every store, 'كافة الرسوم تحتسب بالريال السعودي') and S02-V-162 (the payment services contract).
- S02-SA-295 (c), the coordinator's ruling on call 3: a new row, S02-V-312 (S02-VP-11, the platform's own payment service). 'لا يتطلب تفعيل مدفوعات سلة توقيع عقود مع طرف ثالث أو فتح حساب في بنك محدد. يمكنك البدء بمجرد توثيق متجرك!' (my translation: activating Salla Payments doesn't require signing contracts with a third party or opening an account at a specific bank; you can start once your store is verified), on salla.com/payments, the Saudi path (its scope), addressed to the merchant ('يمكنك'). So the decider is the merchant's country, Saudi Arabia, as the platform ties the page to it (a reading). It stands beside S02-V-156, whose decider is where the store is ('لمتاجر الكويت'). Its words also name the store's verification as what activation follows; that stays in the row's evidence, not as a second decider.
- S02-SA-501 (c), the coordinator's ruling on call 8: a new row, S02-V-313 (S02-VP-18, the store's defaults), '"currency":"AED"' beside '"kyc_country":"AE"' on the new UAE store (store 21123834, Basic), whose onboarding answered United Arab Emirates: the store's country, as kyc_country holds it (S02-V-301), decides its currency, for this one store (a reading). S02-V-168, gap S02-SA-G18 (the default language), stands beside it.

x_words took 'Salla Plus' under S02-VP-14, 'currency' under S02-VP-18, and 'مدفوعات سلة' under S02-VP-11, which Salla's words there already held (problem 2).

### Rows replaced, removed, added and joined (part RD1-S8)

Replaced: S02-V-077 (S02-VP-05, gap S02-ZD-G02, now gap S02-ZD-G30); S02-V-170 (S02-VP-08) and S02-V-173 (S02-VP-09), each gap S02-ZD-G03, now gap S02-ZD-G31; S02-V-291 (S02-VP-15, gap S02-ZD-G08, now the Rise monthly checkout's VAT line, S02-ZD-476 to S02-ZD-483); S02-V-038 (S02-VP-02, gap S02-ZD-G09, now gap S02-ZD-G33); S02-V-148 (S02-VP-08, gap S02-SA-G02, the same gap); S02-V-074 (S02-VP-06, 'As the store owner, you can make this change.', S02-SA-483, now gap S02-SA-G16); S02-V-095 (S02-VP-06, the seller, now without S02-SA-483).

Removed: S02-V-307 (S02-VP-06, gap S02-SA-G16), whose gap S02-V-074 now holds.

Added: S02-V-308 (S02-VP-07, zid, the district and street the save requires, S02-ZD-469); S02-V-309 (S02-VP-15, zid, gap S02-ZD-G32); S02-V-310 (S02-VP-14, zid, the subscription's billing currency by the Business address country, S02-ZD-476 to S02-ZD-483); S02-V-311 (S02-VP-14, salla, S02-SA-256); S02-V-312 (S02-VP-11, salla, S02-SA-295); S02-V-313 (S02-VP-18, salla, S02-SA-501).

Joined: S02-V-029 (S02-VP-01, zid: S02-ZD-467, S02-ZD-468); S02-V-078 (S02-VP-06, zid: S02-ZD-468); S02-V-305 (S02-VP-10, salla: S02-SA-504); S02-V-152 (S02-VP-10, salla: S02-SA-505, S02-SA-506). Each joined row's evidence names what was added, after "second pass, RD1-S8". S02-V-075's note took a line saying S02-SA-483 is now noted.

### Candidates for a new point (part RD1-S8)

None. Every statement this part placed fits a point's kind; those noted answer none of their bullet's questions, or name no decider.

### Searches (part RD1-S8)

No point was raised, so no earlier platform's rows were searched for. To place the round's statements beside the rows that hold their like, this part read: Zid's rows under S02-VP-01 to S02-VP-04, S02-VP-06 to S02-VP-09 and S02-VP-14; every platform's rows under S02-VP-05 and S02-VP-15; Salla's rows under S02-VP-06, S02-VP-11, S02-VP-14 and S02-VP-18; and the full rows of S02-V-074, S02-V-095, S02-V-148, S02-V-152, S02-V-156, S02-V-158, S02-V-181, S02-V-182, S02-V-299, S02-V-305 and S02-V-307. In Zid's terms.tsv, it searched for 'Business address', 'العنوان التجاري' and 'business_location' (no translation or definition). In this file, it searched for the earlier notes on S02-ZD-192 to S02-ZD-205, S02-ZD-398, S02-ZD-408, S02-ZD-411, S02-ZD-418, S02-SA-256, S02-SA-295, S02-SA-483 and S02-SA-501, and, among notes under (d), for 'list', 'options', 'select' and 'countries a store', to see how earlier parts read a list of countries under (d). It found S02-SH-259 and S02-SA-312.

### Rechecks (part RD1-S8)

Each row joined was compared with its own platform's statements already in it (rule 5). S02-V-029's basis, `term;answers`, holds for S02-ZD-467 and S02-ZD-468: 'Business address' is the same words as Shopify's 'your business address' (S02-SH-258), and the field holds the store's country. `answers` holds for each statement joined to S02-V-078, S02-V-152 and S02-V-305, the last two as readings, as their evidence marks. S02-V-095 keeps `answers` for S02-SA-179 and S02-SA-311. The new answer rows rest on `answers` alone: S02-V-291, S02-V-308, S02-V-310, S02-V-311, S02-V-312 and S02-V-313. Their points' `raised_by` statements from other platforms share no term, identifier or definition with them. Shopify's 'billing address' (S02-SH-251) isn't Zid's 'Business address'. 'currency', in S02-SA-501's key, is only a common word with S02-SH-248's 'local language and currency for your store'; the decider's words don't match.

### Calls (part RD1-S8)

1. S02-ZD-468, under (b), is placed under S02-VP-06 (who changes) only. It saved Kuwait over Saudi Arabia, which the record gave at step 22 (S02-ZD-467). Earlier parts placed the Business address help (S02-ZD-083, S02-ZD-084) under both S02-VP-04 and S02-VP-06. If saving a new value also answers who sets the country, S02-ZD-468 would join S02-V-076 as well, with the same answer, the seller.
2. S02-ZD-484, the same Terms link at the subscription checkout for eight Business address countries, is noted under (c). It names no company. For the terms, eight countries in its scope aren't 'every store, whatever its country' (rule 4). Read as every store, it would join S02-V-171 (the terms, every store). Reading the linked Terms as the ones that bind, it would also join S02-V-169 (the Saudi company, every store). Gap-closing kept S02-ZD-G31 open on it.
3. S02-ZD-476 to S02-ZD-483 are placed with the decider their scopes name: the development store's Business address country, one checkout each (a reading). This follows the coordinator's ruling on RD1-S7's call 8, which read S02-SA-501's currency with its store's country. They also answer the platform's fees: the invoice's currency changes with the country. So they raise S02-V-310 under S02-VP-14, although a2.tsv leads them only to S02-VP-15. If the reading is rejected, they would be noted, S02-V-291 would be gap S02-ZD-G32, S02-V-309 would go, and S02-V-310 would go.
4. S02-SA-505 and S02-SA-506 join S02-V-152 (the country selected for the store). Their identifier and scope name 'the UAE store' (rule 5), and S02-SA-284 says 'Your country selection sets the legal requirements for your store'. The coordinator kept S02-SA-484, S02-SA-486 and S02-SA-487 noted (RD1-S7's call 4), but those came from store-1-da's form, whose scope names no country. If the UAE store's form is read the same way, S02-SA-505 and S02-SA-506 would be noted. S02-SA-507 to S02-SA-509 are noted. They come from the same store, but S02-SA-284's words cover legal requirements, not Salla's User Agreement, a review notice or a review state.
5. S02-ZD-467 and S02-ZD-468, under (a), join S02-V-029 (the Business address), as their identifier names the page's field. They don't join S02-V-256 ('user.business_location', from the account's profile, GET /v1/managers/account/profile). That row's key is the same, 'business_location', but from another endpoint. If the coordinator reads the two as one record, they would join S02-V-256 too.
6. S02-ZD-469 is placed under S02-VP-07 as a condition (a reading): the save that changes the country requires the address's district and street. Read as the save's own requirements, not a condition on the country, it would be noted under (b), and S02-V-308 would go.
7. S02-SA-295's own words name the store's verification as what Salla Payments' activation follows. Under the ruling, the decider placed is the merchant's country, as the Saudi path ties the page. The verification stays in the row's evidence, and the first pass's note stands.

### Problems (part RD1-S8)

1. S02-ZD-G33, made in place of S02-ZD-G09, says the Business address takes 162 countries 'and not Iran, Cuba, Korea, Russia or Israel (S02-ZD-N17)'. Its audit contradicts S02-ZD-N17, and the audit's note says the coordinator may need to restate the gap. S02-V-038 names S02-ZD-G33 and records S02-ZD-N17's state in its note.
2. `xwords` adds a word that the platform's x_words already hold. 'مدفوعات سلة' is now twice in Salla's words under S02-VP-11, and the tool has no command to take a word out. Likewise, S02-VP-06 keeps Salla's 'store country', which RD1-S7 added from S02-SA-483, now noted. Salla uses the same words under S02-VP-01.
3. S02-SA-499 and S02-SA-500 (the plans in AED on the new UAE store) and S02-SA-515 (an app's price in AED there) stay noted under (c), as RD1-S7 noted them. Under the coordinator's ruling on call 8, they would read as S02-SA-501 does, under S02-VP-14. No task leads to them, so this part left them.

### Check (part RD1-S8)

This part ran the check on a copy holding only `b/RD1`. `merge_slices.py` merged 19 points and 311 rows. `check_subject.py` (3,073 statements, 90 gaps) gave no line of level `error`; the five errors RD1-S7's check gave, on Zid's rows naming a gap narrowed into another (S02-V-038, S02-V-077, S02-V-170, S02-V-173, S02-V-291), are gone. It gave 17 warnings, on the length of phase A's quotes (Shopify's and WooCommerce's citations), and 33 reviews: 19 on points with no phase C row yet, 12 on quotes found only in a page's source (WooCommerce's and Zid's citations), which are the coordinator's, and 2 on RD2's and RD3's statements, whose folders the copy leaves out. None names this part's rows or statements. In its `unplaced.tsv`, RD1 has no row: this part's place tasks and its revisits' leads are gone from it. In `second_pass_list.py --check`, RD1 has no open revisit, reread or note task.

## Second pass, RD1-S9

Part RD1-S9: the BigCommerce and WooCommerce round's tasks under RD1 (bullets a to d), from A2-BC-R and A2-WC-R (other-product-class 3f2438f3, folders `bigcommerce/` and `woocommerce/`): 9 revisits and 12 place tasks. BigCommerce's new statements are observations of the free trial store w5pamplexj (Capture Test Store NA: online payments off, one storefront, hosted in North America; default country Oman as made, and Saudi Arabia during the plan checkout). WooCommerce's are observations of a test store (WordPress 7.1.4, WooCommerce 11.2.1, WooPayments 11.2.0, WooCommerce Tax 3.7.3), whose WooPayments onboarding stopped before an account existed. Each row keeps the store, its plan or versions, and the run and step, in its scope or evidence.

### Revisit S02-V-250 (bigcommerce, S02-VP-05, who checks the store's country) (part RD1-S9)

S02-V-250, was gap S02-BC-G09: replaced with gap S02-BC-G16, in place of S02-BC-G09. S02-BC-G16 asks who checks the store's default country, and what set it when the store was made. No lead names a party that checks.

Lead placed under (b):
- S02-BC-378: joined S02-V-099 (S02-VP-06, who changes the store's country: the seller). 'Localization updated' answered each save under 'Settings › Localization: Default country saved (PUT v3/settings/store/locale)' (its identifier), the default country saved as United States, Oman, United Kingdom and Saudi Arabia in turn (store w5pamplexj; run 20261029T012951Z-store-settings-en, steps 40, 50, 55 and 60). A control in the store's admin, so the seller changes it (rule 4). It changes a value already set, so it isn't joined under S02-VP-04 (who sets) too, as RD1-S8 placed S02-ZD-468 (its call 1). It names no party that checks and no condition, so it is under neither S02-VP-05 nor S02-VP-07.

Lead noted under (b):
- S02-BC-380 (b): the free trial form's request, '"name":"Capture Test Store NA","projectedAnnualRevenue":"I'm not sure","region":"NA","plan_sku":"STORE-TRIAL-15DAY"' (the sign-up of store w5pamplexj; run 20261029T011432Z-trial-signup-ye-hand-en, step 1): the fields the merchant sent hold no country, and 'region' is where the store is hosted ('hosted in North America', its scope), which rule 1 keeps out; it names no party that sets, checks or changes the store's country. What set the country when the store was made is S02-BC-G16's

The earlier leads stay where they are: S02-BC-277 in S02-V-089 (S02-VP-05); S02-BC-282 in S02-V-099 (S02-VP-06); S02-BC-212, S02-BC-259, S02-BC-273, S02-BC-274 and S02-BC-283 noted under (b) above in this file. S02-BC-213, S02-BC-214, S02-BC-258, S02-BC-271, S02-BC-379 and S02-BC-381, under RD1's other bullets, are placed or noted under their own tasks or earlier.

### Revisit S02-V-226 (bigcommerce, S02-VP-10, documents and checks) (part RD1-S9)

S02-V-226, gap S02-BC-G06: replaced with the same gap, which the work list names as still open. S02-BC-G06 asks which documents or checks a merchant provides to verify the store or the business, and what decides them. The new lead names neither.

Lead placed under (c):
- S02-BC-385: joined S02-V-228 (S02-VP-11, the platform's own payment service: 'Your store must be located in the United Kingdom or the United States.'). 'When you connect BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created. The BigCommerce Payments account is automatically linked to your PayPal Business account.' (Connecting with BigCommerce Payments: Setting up BigCommerce Payments) says how the store can use the service. Its words name no decider. Its scope, 'stores with BigCommerce Payments (a store located in the United Kingdom or the United States, S02-BC-081)', names the store's location, the requirement S02-BC-081 gives on the same page (rule 5) (call 1).

The earlier leads stay noted under (c): S02-BC-218, S02-BC-219 and S02-BC-220. S02-BC-221 and S02-BC-222, under (b), stay noted. S02-BC-386 is outside RD1's slice, and left.

### Revisit S02-V-237 (bigcommerce, S02-VP-16, the store's taxes), again (part RD1-S9)

S02-V-237, was gap S02-BC-G15: the work list names no gap for the point, so gap-closing settled S02-BC-G15, and the gap goes. Replaced with an answer, every store: 'All stores contain a Default Zone, which applies a 0% tax rate to any regions not set up in another zone.' (S02-BC-371, Basic Tax Setup: Default Zone). Its own words apply the Default Zone to all stores, and neither it nor its scope names a country, a site or a region (rule 4).

Leads noted under (c):
- S02-BC-368 (c): 'Configure your own tax classes, rates and zones. Basic tax will be used if your tax service is not targeted to a given country/subdivision, or is unavailable during a purchase.' (Settings › Tax: Tax rules: Basic Tax (Enabled); store w5pamplexj, default country United States; run 20261029T012951Z-store-settings-en, step 43): which tax is used follows the tax service's targeting to a country or subdivision, whose words don't say it is the store's own; outside rule 1's table (in S02-VP-16's note)
- S02-BC-369 (c): '- heading "All tax services" [level=2]' (Settings › Tax › Add tax service: Avalara recommended; CereTax, TaxCloud Simple Sales Tax, TaxJar, Vertex and CCH® SureTax®), the same page and the same answer of GET /internalapi/v1/tax/providers with the default country saved as United States, Oman, United Kingdom and Saudi Arabia in turn (store w5pamplexj; run 20261029T012951Z-store-settings-en, steps 45, 51, 56 and 61): it names no decider, and its scope names four countries of one store, so it isn't every store (rule 4) (call 2)
- S02-BC-372 (c): Avalara AvaTax calculates VAT/GST 'if your business has transactions into European Union member states or any other country around the world that charges VAT/GST. However, you must specify which countries you'll be collecting VAT/GST from, whether they have a permanent establishment, and whether they are the Importer of Record.' (stores with Avalara AvaTax): the countries the business has transactions into and collects from are markets it sells into, not the store's own country (rule 1); outside rule 1's table (in S02-VP-16's note)
- S02-BC-373 (c): 'The Importer of Record is a person or entity who assumes the responsibility for ensuring goods imported to a particular country are appropriately documented and valued.' (stores with Avalara AvaTax): a definition of the party responsible for duties on imports, with no decider (rule 4)
- S02-BC-374 (c): the shipping origin address, '{"data":{"city":"","country_code":"US",' (GET /internalapi/v1/shipping/origin/address, read on Settings › Tax and Settings › Shipping; store w5pamplexj; the same answer at steps 43 to 62 of run 20261029T012951Z-store-settings-en, the default country saved as United States, Oman, United Kingdom and Saudi Arabia in turn): a place the store ships from, which rule 1 keeps out; it names no decider of the store's taxes (rule 4)

The earlier leads stay noted under (c): S02-BC-247, S02-BC-249 and S02-BC-250. S02-BC-246, S02-BC-248 and S02-BC-370 are outside RD1's slice, and left. x_words took 'Default Zone' under S02-VP-16.

### Revisit S02-V-281 (bigcommerce, S02-VP-15, taxes on the platform's fees), again (part RD1-S9)

S02-V-281, was gap S02-BC-G10: the work list names no gap for the point, so gap-closing settled S02-BC-G10, and the gap goes. Replaced with an answer, 'Taxes $69.60' (S02-BC-359 to S02-BC-365): the Taxes line of the Core plan's annual upgrade checkout ($348.00) on store w5pamplexj, one statement for each amount, with the billing contact's city and country in its scope. $0.00 for Muscat (OM), Los Angeles, CA (US), Toronto (CA), Tokyo (JP), Singapore (SG), New Delhi (IN), Riyadh (SA), Dubai (AE) and Sana'a (YE); $34.80 for Sydney (AU); $69.60 for London (GB); $22.96 for Austin, TX, $30.89 for New York, NY and $36.71 for Seattle, WA (US); $66.12 for Berlin (DE). The default country stayed Saudi Arabia throughout (their scope; run 20261029T015915Z-plan-upgrade-en). The decider is the store's own country, with its city, as the account's billing contact holds it: the account's address, which S02-V-262 holds under (a) ('click Edit to the right of the contact listed as the billing contact', S02-BC-282). A reading: the statements give the line for each billing contact, and their words don't say what decides it (call 3). It stands beside S02-V-236 (every store: 'All fees are exclusive of all applicable governmental fees, charges, or taxes').

Leads noted under (c):
- S02-BC-366 (c): 'All prices shown in US Dollars. Purchases in Australia will be assessed GST.' (Choose a Plan, on store w5pamplexj, default country Oman as made; run 20261029T015915Z-plan-upgrade-en, step 4): the GST's decider is where the purchase is, outside rule 1's table (in S02-VP-15's note); the prices' currency names no decider, and its scope names the store's country, so it isn't every store (rule 4) (call 3)
- S02-BC-367 (c): 'Country [Oman]', the account's billing contact as BigCommerce had filled it (Account › Contacts › Edit Contact; run 20261029T015915Z-plan-upgrade-en, step 6): the record S02-V-281's reading rests on, but its words name no thing bound to it (rule 2); placed under (a), below

The earlier leads stay where they are: S02-BC-232 and S02-BC-234 in S02-V-236; S02-BC-280 in S02-V-282, and S02-BC-281 in S02-V-234 and S02-V-283 (S02-VP-14); S02-BC-233, S02-BC-278, S02-BC-279 and S02-BC-283 noted under (c) above in this file. S02-BC-270, S02-BC-275, S02-BC-276, S02-BC-277, S02-BC-282 and S02-BC-294, under RD1's other bullets, are placed or noted earlier. S02-BC-284 and S02-BC-295 are outside RD1's slice, and left.

### Revisit S02-V-286 (bigcommerce, S02-VP-18, the store's defaults), again (part RD1-S9)

S02-V-286, was gap S02-BC-G11: replaced with gap S02-BC-G17, in place of S02-BC-G11. S02-BC-G17 asks whether a store made with a default country whose standard formats differ from the shared set (16 of 245 countries, such as the United States) takes them when it is made.

Leads placed under (c):
- S02-BC-376, S02-BC-377: joined S02-V-284 (the store's default country decides the standard formats that 'Set standard formats for [country]' sets). The endpoint of 'Set standard formats for <country>' (their identifier) gives a set for each country: for Oman, KGS and Centimeters with 'jS M Y' at '+00:00' (S02-BC-376); for the United States, Ounces and Inches with 'M jS Y' (S02-BC-377); 229 of 245 countries share Oman's set, in 14 distinct sets (S02-BC-376's scope; run 20261029T040218Z-standard-formats-all-en). The button sets them 'for your store’s default country' (S02-BC-285), so that the default country decides which set it takes is a reading (call 4).

Leads noted under (c):
- S02-BC-375 (c): '1,234.00 KGS/Centimeters', the store's physical dimensions as it was made, beside the button 'Set standard formats for Oman' (its identifier; store w5pamplexj, default country Oman as made; run 20261029T012951Z-store-settings-en, step 4): the values are Oman's standard set (S02-BC-376), which 228 other countries share, so its words don't show what set them when the store was made; that is S02-BC-G17's
- S02-BC-378 (c): 'Localization updated', on the save of the default country as United States, after which the physical dimensions were 'still 1,234.00 KGS/Centimeters' and the date and timezone 'still 24th Jul 2020 @ 3:49 AM, (GMT +00:00)' (its scope; run 20261029T012951Z-store-settings-en, step 40): the save left the store's units and date formats as they were; it names no decider of the store's defaults (rule 4), and is a lead to S02-BC-G17

The earlier leads stay where they are: S02-BC-243 in S02-V-239; S02-BC-253 and S02-BC-285 in S02-V-284; S02-BC-288 to S02-BC-291 in S02-V-285; S02-BC-244 noted under (c) above in this file. S02-BC-251 and S02-BC-293, under RD1's other bullets, are placed or noted earlier. S02-BC-245, S02-BC-286, S02-BC-287 and S02-BC-292 are outside RD1's slice, and left.

### Revisit S02-V-044 (woocommerce, S02-VP-01, what fills the store's country), again (part RD1-S9)

S02-V-044, was gap S02-WC-G01: replaced with gap S02-WC-G10, in place of S02-WC-G01. S02-WC-G10 asks where Automattic holds the merchant's country of residence that the Terms read to name the contracting entity, and where the WooPayments account's country is held once an account exists. The test store made no account.

Leads placed under (a):
- S02-WC-521: joined S02-V-039 (the store's Country / State): 'woocommerce_default_country on US:CA', the row of wp_options on the test store after the set-up (run 20261029T023002Z-db-after-setup). Its key is the id the Country / State setting has ("'id' => 'woocommerce_default_country'", S02-WC-113), which 'The country and state or province, if any, in which your business is located.' describes there (call 5).
- S02-WC-522: joined S02-V-041 (the Payments settings' business location): user 1's row of wp_usermeta, 'woocommerce_payments_nox_profile' with 'business_country_code' OM (the business location saved as Oman at run 20261029T020454Z-store-setup-en, step 102): the key the code reads for the business location ('$user_nox_meta['business_country_code']', S02-WC-222), held per user.

S02-WC-014 and S02-WC-015, noted under (a) above in this file beside S02-V-044's earlier gap, stay as they are.

### Revisit S02-V-087 (woocommerce, S02-VP-07, what must hold before the store's country changes), again (part RD1-S9)

S02-V-087, was gap S02-WC-G03: replaced with an answer, 'Your settings have been saved.' (S02-WC-523). It was the only message when the store's Country / State was changed to Saudi Arabia and saved, on the test store with two orders and two tax rates (its identifier; run 20261029T023051Z-country-change-en, step 23). The change went through with orders and tax rates on the store, so neither had to be removed before it. A reading: the message names no condition (call 6). S02-V-314 (added): gap S02-WC-G09, in place of S02-WC-G03, beside it. It asks for any condition on the change once a WooPayments account exists, and what the change then carries to the account and to the Payments settings.

Lead placed under (b):
- S02-WC-523: the answer above; also joined S02-V-085 (S02-VP-06, who changes the store's country: the seller), since 'Settings > General > Save changes' is a control in the store's admin (rule 4). It changes a value already set, so it isn't joined under S02-VP-04 too.

Leads noted under (b):
- S02-WC-524 (b): 'Currency [United States (US) dollar ($) — USD]', the general settings' currency after the change of Country / State to Saudi Arabia (run 20261029T023051Z-country-change-en, step 23): what the change left as it was; it names no party that sets, checks or changes the store's country, and no condition before it changes
- S02-WC-525 (b): '{"id":1,"country":"US","state":"CA","postcode":"","city":"","rate":"7.2500","name":"CA sales tax (TEST)"', a tax rate read back after each change of Country / State (steps 24, 28, 32 and 36): as S02-WC-524
- S02-WC-526 (b): '"id":14,"parent_id":0,"status":"pending","currency":"USD"', an order read back after each change (steps 24, 28, 32 and 36): as S02-WC-524
- S02-WC-527 (b): the WooPayments onboarding's state with the business location Oman, after each change of Country / State to Saudi Arabia, Yemen, United Kingdom and United States (US) — California, '"messages":{"not_supported":"WooPayments is not supported in the selected business location."}' (steps 24, 28, 32 and 36): it names the business location, not the store's Country / State, as what WooPayments' support follows, and no party or condition that (b) asks for; placed under (c), below

S02-WC-516 and S02-WC-528, under (c), have their own tasks or were placed earlier. x_words took 'Country / State' under S02-VP-07.

### Revisit S02-V-255 (woocommerce, S02-VP-05, who checks the store's country), again (part RD1-S9)

S02-V-255, was gap S02-WC-G06: replaced with an answer, 'It looks like you’re located in Yemen . Are you sure you want to create a store in United States (US) — California ?' (S02-WC-530, S02-WC-529). The core profiler showed the notice when the country chosen for the store wasn't where the visitor was geolocated, through the set-up's request to 'https://public-api.wordpress.com/geo/' (S02-WC-529) (run 20261029T020454Z-store-setup-en, steps 73 and 74). So the platform's set-up checks the country chosen for the store, which the profiler's 'Where is your store located?' holds (S02-V-274), against the visitor's location, and asks the merchant to confirm it. A check in the platform's code is the platform's (rule 4). It stands beside the platform's check of the location's form (S02-V-254), Stripe's verification (S02-V-084) and WooCommerce's work with Stripe (S02-V-098) (call 7). S02-V-315 (added): gap S02-WC-G11, in place of S02-WC-G06, beside them. It asks whether Stripe's verification checks the country answered at WooPayments' onboarding against the documents it asks for.

Lead noted under (b):
- S02-WC-531 (b): '{"id":"business_verification","path":"\/woopayments\/onboarding\/business_verification","required_steps":["wpcom_connection"],"status":"not_started"' (WooPayments onboarding on the test store, business location United States (US); run 20261029T020454Z-store-setup-en, step 87): the business verification step waits on the WordPress.com connection and wasn't started; it names no party that checks the store's country (S02-WC-G11)

The earlier leads stay where they are: S02-WC-257, S02-WC-258, S02-WC-260 and S02-WC-261 in S02-V-084; S02-WC-511 in S02-V-098; S02-WC-262 in S02-V-254; S02-WC-259 in S02-V-082 (S02-VP-04); S02-WC-512 noted under (b) above in this file. x_words took 'create a store in' under S02-VP-05.

### Revisit S02-V-288 (woocommerce, S02-VP-10, documents and checks), again (part RD1-S9)

S02-V-288, was gap S02-WC-G07: replaced with gap S02-WC-G12, in place of S02-WC-G07. S02-WC-G12 asks which documents or checks WooPayments' own business verification asks for in each country. No lead gives them.

Leads noted under (c):
- S02-WC-531 (c): the business verification step, '"required_steps":["wpcom_connection"],"status":"not_started"' (as under (b), above): a step not reached, which names no document or check, and no decider (rule 4)
- S02-WC-532 (c): '"context":{"fields":[],"sub_steps":[],"self_assessment":[],"has_test_account":false,"has_sandbox_account":false}' (the business verification's context before the WordPress.com connection; run 20261029T020454Z-store-setup-en, step 87): no fields, so no document or check, and no decider (rule 4)
- S02-WC-533 (c): 'individual.ssn_last_4 Must be the last 4 digits of a 9 digit U.S. Social Security number (SSN). Card payments and Payouts will be paused immediately if not provided.' (Stripe's Required verification information tool, as a visitor: platform country United States (US), dashboard type none, account country United States (US); run 20261029T032517Z-stripe-requirements-en, step 23): Stripe's requirements for a connected account, under settings its words don't say are WooPayments', so they aren't stated to be what a WooCommerce merchant provides (rule 2's role test) (call 8)
- S02-WC-534 (c): 'Trade license documents.company_license.files — Card payments, Payouts, and Transfers will be paused immediately if not provided.' (the same tool, account country United Arab Emirates (AE), business type company; step 28): as S02-WC-533
- S02-WC-535 (c): 'Account country only supports recipient service agreements.' (the same tool, account country Saudi Arabia (SA), business type individual; step 31): as S02-WC-533

S02-WC-263 stays in S02-V-194.

### Place tasks, BigCommerce and WooCommerce round: bigcommerce (a) and (b) (part RD1-S9)

Placed:
- S02-BC-367, under (a): joined S02-V-262 (S02-VP-01, your BigCommerce account's address). 'Country [Oman]' is the field of 'Account › Contacts › Edit Contact (the account's billing contact)' (its identifier), the contact S02-BC-282 names for the account's address ('click Edit to the right of the contact listed as the billing contact'), as BigCommerce had filled it on store w5pamplexj, made with default country Oman (run 20261029T015915Z-plan-upgrade-en, step 6).
- S02-BC-378 and S02-BC-379, under (a): joined S02-V-260 (S02-VP-01, Default country — The country your store is run from). S02-BC-379, 'Determines available payment options.', is the help of 'Settings › Localization › Country: Default country' (its identifier), with the value [Oman] (step 4); S02-BC-378, 'Localization updated', answered each save under 'Settings › Localization: Default country saved (PUT v3/settings/store/locale)', the default country saved as United States, Oman, United Kingdom and Saudi Arabia, and restored to Oman (run 20261029T012951Z-store-settings-en; run 20261029T025746Z-store-country-restore-en). The save goes through the endpoint whose body holds store\_country (S02-V-048), but S02-BC-378's words don't name the key, so it isn't joined there (call 9).
- S02-BC-381, under (a): a new row, S02-V-316 (S02-VP-01): '"storeCountry":"Oman"', the control panel's config (GET /internalapi/v1/controlpanel/config) at its first load after the sign-up (run 20261029T011432Z-trial-signup-ye-hand-en, step 10). 'storeCountry' is the words 'store' and 'Country' joined, the same words as Shopify's 'store country' (S02-SH-246), so its basis is `term;answers`. Its key and endpoint are not those of store\_country (S02-V-048), Get Store Information's country (S02-V-257) or the Default country field (S02-V-260), so it is its own row, as RD1-S8 kept 'business_location' of two Zid endpoints apart (its call 5) (call 9).

Noted:
- S02-BC-374 (a): the shipping origin address, '{"data":{"city":"","country_code":"US",' (GET /internalapi/v1/shipping/origin/address, read on Settings › Tax and Settings › Shipping; store w5pamplexj, the same answer with the default country saved as United States, Oman, United Kingdom and Saudi Arabia): a place the store ships from, which rule 1 keeps out of the store's own country
- S02-BC-375 (a): '1,234.00 KGS/Centimeters', the store's physical dimensions as it was made (Settings › Localization; step 4): units, not a country, address or jurisdiction (rule 2); the button its identifier names, 'Set standard formats for Oman', names the default country that S02-V-260 holds, and no field of its own
- S02-BC-380 (a): the free trial form's request, '"name":"Capture Test Store NA","projectedAnnualRevenue":"I'm not sure","region":"NA","plan_sku":"STORE-TRIAL-15DAY"' (run 20261029T011432Z-trial-signup-ye-hand-en, step 1): it holds no country; 'region' is where the store is hosted ('hosted in North America', its scope), which rule 1 keeps out
- S02-BC-385 (b): 'When you connect BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created. The BigCommerce Payments account is automatically linked to your PayPal Business account.': a PayPal account made for the store and linked to the merchant's; it names no party that sets, checks or changes the store's country (rule 2); placed under (c) in S02-V-228, above

x_words took 'storeCountry; billing contact' under S02-VP-01.

### Place tasks, BigCommerce and WooCommerce round: bigcommerce and woocommerce (c) (part RD1-S9)

Placed:
- S02-BC-379, under (c): joined S02-V-287 (S02-VP-12, other payment providers: 'Default country — The country your store is run from, which determines the payment methods that are available for use with your store.'). 'Determines available payment options.' is the help the store's admin shows under 'Settings › Localization › Country: Default country' (its identifier), with the value [Oman] on store w5pamplexj (run 20261029T012951Z-store-settings-en, step 4): the default country, in the decider's role. BigCommerce's terms.tsv gives the same words as the definition of 'Default country'.
- S02-WC-527 and S02-WC-528, under (c): joined S02-V-199 (S02-VP-11, the platform's own payment service: 'The Business location at the top of the page is not set to one of our supported countries.'). With the business location Oman, the onboarding's state gave 'WooPayments is not supported in the selected business location.' after each change of the store's Country / State to Saudi Arabia, Yemen, United Kingdom and United States (US) — California (S02-WC-527; run 20261029T023051Z-country-change-en, steps 24, 28, 32 and 36). After the business location was set to US, it gave '"supported":true', the store's Country / State still United States (US) — California (S02-WC-528; step 37). The business location (S02-V-041 under (a)) decides, in the decider's role; the store's Country / State, changed four times, left the answer as it was.

Noted:
- S02-WC-525 (c): '{"id":1,"country":"US","state":"CA","postcode":"","city":"","rate":"7.2500","name":"CA sales tax (TEST)"', the store's tax rate read back after each change of Country / State to Saudi Arabia, Yemen, United Kingdom and United States (US) — California (run 20261029T023051Z-country-change-en, steps 24, 28, 32 and 36): the change left the rate as it was; it names no decider of the store's taxes (rule 4)

### Rows replaced, removed, added and joined (part RD1-S9)

Replaced: S02-V-250 (S02-VP-05, gap S02-BC-G09, now gap S02-BC-G16); S02-V-226 (S02-VP-10, gap S02-BC-G06, the same gap); S02-V-237 (S02-VP-16, gap S02-BC-G15, now the Default Zone, every store, S02-BC-371); S02-V-281 (S02-VP-15, gap S02-BC-G10, now the plan checkout's Taxes line by the billing contact, S02-BC-359 to S02-BC-365); S02-V-286 (S02-VP-18, gap S02-BC-G11, now gap S02-BC-G17); S02-V-044 (S02-VP-01, gap S02-WC-G01, now gap S02-WC-G10); S02-V-087 (S02-VP-07, gap S02-WC-G03, now 'Your settings have been saved.', S02-WC-523); S02-V-255 (S02-VP-05, gap S02-WC-G06, now the set-up's geolocation notice, S02-WC-530 and S02-WC-529); S02-V-288 (S02-VP-10, gap S02-WC-G07, now gap S02-WC-G12).

Removed: none.

Added: S02-V-314 (S02-VP-07, woocommerce, gap S02-WC-G09); S02-V-315 (S02-VP-05, woocommerce, gap S02-WC-G11); S02-V-316 (S02-VP-01, bigcommerce, '"storeCountry":"Oman"', S02-BC-381).

Joined: S02-V-099 (S02-VP-06, bigcommerce: S02-BC-378); S02-V-228 (S02-VP-11, bigcommerce: S02-BC-385); S02-V-284 (S02-VP-18, bigcommerce: S02-BC-376, S02-BC-377); S02-V-260 (S02-VP-01, bigcommerce: S02-BC-378, S02-BC-379); S02-V-262 (S02-VP-01, bigcommerce: S02-BC-367); S02-V-287 (S02-VP-12, bigcommerce: S02-BC-379); S02-V-039 (S02-VP-01, woocommerce: S02-WC-521); S02-V-041 (S02-VP-01, woocommerce: S02-WC-522); S02-V-085 (S02-VP-06, woocommerce: S02-WC-523); S02-V-199 (S02-VP-11, woocommerce: S02-WC-527, S02-WC-528). Each joined row's evidence names what was added, after "second pass, RD1-S9". The notes of S02-VP-15 and S02-VP-16 took the statements kept out (S02-BC-366; S02-BC-368 and S02-BC-372).

The rows the checker names for RD1 as naming a settled gap are all rewritten: S02-V-044 (now S02-WC-G10), S02-V-087 (an answer, with S02-WC-G09 in S02-V-314), S02-V-237 (an answer), S02-V-250 (S02-BC-G16), S02-V-255 (an answer, with S02-WC-G11 in S02-V-315), S02-V-281 (an answer), S02-V-286 (S02-BC-G17) and S02-V-288 (S02-WC-G12).

### Candidates for a new point (part RD1-S9)

None. Every statement this part placed fits a point's kind; those noted answer none of their bullet's questions, name no decider from rule 1's table, or fail the role test.

### Searches (part RD1-S9)

No point was raised, so no earlier platform's rows were searched for. To place the round's statements beside the rows that hold their like, this part read: BigCommerce's rows under S02-VP-01, S02-VP-04 to S02-VP-07, S02-VP-10, S02-VP-11, S02-VP-15, S02-VP-16 and S02-VP-18; WooCommerce's rows under S02-VP-01, S02-VP-04 to S02-VP-07, S02-VP-10, S02-VP-11 and S02-VP-16; the full rows of S02-V-039, S02-V-041, S02-V-048, S02-V-099, S02-V-199, S02-V-260, S02-V-262, S02-V-284 and S02-V-287; and the notes of S02-VP-10, S02-VP-15, S02-VP-16 and S02-VP-18. In this file, it searched for the earlier notes on each lead of its revisits, by id, and on S02-BC-129 and S02-BC-111, to see how the tax zones were read under S02-VP-16. In terms.tsv, it searched BigCommerce's terms for 'storeCountry', 'store_country', 'store country', 'billing contact' and 'default country' (it found 'store_country', with no definition, and 'default country' and 'Default country', the last defined as 'Determines available payment options.'), and Shopify's for 'store country' (no definition).

### Rechecks (part RD1-S9)

Each row joined was compared with its own platform's statements already in it (rule 5). `answers` holds for each statement joined: S02-BC-378 to S02-V-099 (a control in the store's admin), and with S02-BC-379 to S02-V-260 (the Default country field, by their identifiers); S02-BC-385 to S02-V-228 (the store's location, by its scope); S02-BC-376 and S02-BC-377 to S02-V-284 (a reading, as the evidence marks); S02-BC-367 to S02-V-262 (the account's billing contact, the contact S02-BC-282 names); S02-BC-379 to S02-V-287 (the default country, by its identifier); S02-WC-521 to S02-V-039 (the key S02-WC-113 gives the Country / State setting); S02-WC-522 to S02-V-041 (the key S02-WC-222 reads); S02-WC-523 to S02-V-085 (a control in the store's admin); S02-WC-527 and S02-WC-528 to S02-V-199 (the business location). S02-V-039's `term` rests on S02-WC-116 and stays; S02-WC-521's own words don't give it. The new answer rows S02-V-087, S02-V-237, S02-V-255 and S02-V-281 rest on `answers` alone: their points' `raised_by` statements from other platforms share no term, identifier or definition with them. Shopify's 'billing address' (S02-SH-251, under S02-VP-15) isn't in the words of S02-BC-359 to S02-BC-365, whose billing contact is in their scope. S02-V-316 rests on `term;answers`: 'storeCountry' and Shopify's 'store country' (S02-SH-246), neither defined in its platform's terms.tsv.

### Calls (part RD1-S9)

1. S02-BC-385 joins S02-V-228 (BigCommerce Payments, the store's location) by its scope, 'stores with BigCommerce Payments (a store located in the United Kingdom or the United States, S02-BC-081)', which phase A recorded from the page's Requirements (rule 5). Its own words name no decider. If the scope isn't read so, it would be noted under (c).
2. S02-BC-369 is noted: the same tax services, and the same answer of the tax providers' endpoint, with the store's default country saved as United States, Oman, United Kingdom and Saudi Arabia in turn. One store with four countries isn't 'every store, whatever its country' (rule 4), and its scope names the countries. If the coordinator reads it as offered whatever the store's country, it would join S02-V-237 (every store). S02-BC-374, the shipping origin unchanged across the same four countries, is noted under (a) and (c) as a place the store ships from.
3. S02-V-281 reads the account's billing contact's address as the decider of the taxes on the Core plan's price: the Taxes line differs with the billing contact's city and country, while the default country stayed Saudi Arabia. RD1-S8 read Zid's VAT line by the Business address country the same way (its call 3), after the coordinator's ruling on RD1-S7's call 8. If rejected, S02-BC-359 to S02-BC-365 would be noted, and S02-V-281 would be `not covered`, since the work list names no gap. S02-BC-366 is noted: 'Purchases in Australia will be assessed GST.' names where the purchase is. Read as the merchant's location as the billing contact holds it (S02-BC-360: Sydney (AU), Taxes $34.80), it would join S02-V-281. Its 'All prices shown in US Dollars.' names no decider, and its scope names the store's country (Oman), so it isn't every store under S02-VP-14.
4. S02-BC-376 and S02-BC-377 join S02-V-284 (the store's default country decides the standard formats the reset sets), a reading: their endpoint takes any country, and S02-BC-285 ties the button to the store's default country. If rejected, they would be noted under (c) as leads to S02-BC-G17, as S02-BC-375 and S02-BC-378 are.
5. S02-WC-521's key, 'woocommerce_default_country', names a country without saying whose. It joins S02-V-039 because S02-WC-113 gives that key as the id of the Country / State setting, 'The country and state or province, if any, in which your business is located.' Read alone, under rule 2's role test for a key, it would be noted under (a).
6. S02-V-087's answer, 'Your settings have been saved.' (S02-WC-523), reads a save that went through on a store with two orders and two tax rates as no condition on them (a reading, as BigCommerce's 'you can adjust these settings at any time' is S02-V-091's answer). If rejected, S02-WC-523 would stay under S02-VP-06 only, S02-V-087 would hold gap S02-WC-G09, and S02-V-314 would go.
7. S02-V-255's answer is the platform's set-up comparing the country chosen for the store with the visitor's geolocated country (S02-WC-530, S02-WC-529). It is a row apart from S02-V-254, the platform's code checking the location's two-letter form, though both name the platform as the party. If the coordinator reads them as one answer, the platform, S02-WC-529 and S02-WC-530 would join S02-V-254, S02-V-255 would hold gap S02-WC-G11, and S02-V-315 would go.
8. S02-WC-533 to S02-WC-535 are noted: they come from Stripe's Required verification information tool, used as a visitor, under settings that S02-WC-G12 says are not stated to be WooPayments'. Read as WooPayments' verification, they would give an answer under S02-VP-10: the account country decides the information asked for.
9. S02-BC-381 ('storeCountry', the control panel's config) is a new row, S02-V-316, apart from S02-V-048 ('store\_country', Update Locale Settings), S02-V-257 and S02-V-260, since its key and endpoint differ, as RD1-S8 kept Zid's 'business_location' of two endpoints apart. S02-BC-378 joins S02-V-260 (the Default country field) and not S02-V-048, although its identifier names PUT v3/settings/store/locale, the endpoint whose body holds store\_country. If the coordinator reads these as one field, S02-BC-381 and S02-BC-378 would join S02-V-048 too.
10. S02-V-237's answer, the Default Zone every store contains (S02-BC-371), is a tax zone, which applies to regions the store sells to. An earlier part kept S02-BC-129's tax zones out of S02-VP-16, because their decider was the buyer's addresses or the shipping origin. S02-BC-371's own words apply it to all stores, so rule 4 makes it every store. If the coordinator reads it as RD3's alone, S02-BC-371 would be noted under (c), and S02-V-237 would be `not covered`, since the work list names no gap.

### Problems (part RD1-S9)

1. The work list names no gap for S02-V-237 (was S02-BC-G15) or S02-V-281 (was S02-BC-G10), so gap-closing settled both, but this part can't see which statement's note says it 'answers' either gap: phase A's notes are closed to it. It replaced both rows with the answers the rules give from the leads (calls 3 and 10).
2. `done` records the revisit, reread and note tasks, as the brief's Writing section gives. This part's 12 place tasks have no `done` line; the checker's `unplaced.tsv` shows whether they are placed or noted.

### Check (part RD1-S9)

This part ran the check on a copy holding only `b/RD1`. `merge_slices.py` merged 19 points and 314 rows. `check_subject.py` (3,116 statements, 97 gaps) gave no line of level `error`: the rows naming a settled gap that the checker named for RD1 (S02-V-044, S02-V-087, S02-V-237, S02-V-250, S02-V-255, S02-V-281, S02-V-286 and S02-V-288) no longer do. It gave 17 warnings, on the length of phase A's quotes (Shopify's and WooCommerce's citations), and 14 reviews: 12 on quotes found only in a page's source (WooCommerce's and Zid's citations), which are the coordinator's, and 2 on RD2's and RD3's statements, whose folders the copy leaves out. None names this part's rows or statements. In its `unplaced.tsv`, RD1 has no row: this part's place tasks and its revisits' leads are gone from it. In `second_pass_list.py --check`, RD1 has no open revisit, reread or note task.

### The coordinator's rulings on calls 1 and 10 (part RD1-S9)

The coordinator ruled on 29 October on two of this part's calls; the other eight stand. What follows replaces what this section says above about S02-BC-385, S02-BC-371 and S02-V-237.

Call 1, S02-BC-385: a statement is placed by what its own words name, not by its scope (the role test). S02-V-228 (S02-VP-11) was replaced without S02-BC-385, with its statements (S02-BC-081, S02-BC-082), excerpt, basis and evidence as they were before this part; its note says why.
- S02-BC-385 (c): 'When you connect BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created. The BigCommerce Payments account is automatically linked to your PayPal Business account.' (Connecting with BigCommerce Payments: Setting up BigCommerce Payments): its words name no decider of the payment service; the store's location is in its scope only, citing S02-BC-081 (the coordinator's ruling on RD1-S9's call 1)

Call 10, S02-V-237 (S02-VP-16): the Default Zone applies a rate to buyers' regions. It is a tax zone, which S02-VP-16's note keeps out, as it does S02-BC-129 (rule 1). S02-BC-369 answers S02-BC-G15. S02-V-237 was replaced with the answer S02-BC-369 gives: 'heading "All tax services"', every store, a reading of one store under four countries. On store w5pamplexj, the Add tax service page (Avalara recommended; CereTax, TaxCloud Simple Sales Tax, TaxJar, Vertex and CCH® SureTax®) was the same, and the tax providers' endpoint gave one answer, with the default country saved as United States, Oman, United Kingdom and Saudi Arabia in turn (run 20261029T012951Z-store-settings-en, steps 45, 51, 56 and 61). So the tax services the store can add are offered whatever its default country, of the four (rule 4). The four countries are in its scope, as phase A recorded the run's steps from the source (rule 5). It isn't a gap row, since S02-BC-G15 is answered and the point has no other gap. S02-BC-369's note under (c), above in this section, stays as it is, as a reread's earlier note does. S02-VP-16's note took S02-BC-371 as kept out.
- S02-BC-371 (c): 'All stores contain a Default Zone, which applies a 0% tax rate to any regions not set up in another zone.' (Basic Tax Setup: Default Zone): a tax zone, which applies a rate to buyers' regions; kept out of S02-VP-16, as S02-BC-129 is (rule 1; the coordinator's ruling on RD1-S9's call 10)

x_words took 'tax services' under S02-VP-16. 'Default Zone', which this part added there from S02-BC-371, stays, since the tool has no command to take a word out (RD1-S8's problem 2).

Rows: replaced S02-V-228 (S02-VP-11, without S02-BC-385) and S02-V-237 (S02-VP-16, now S02-BC-369's answer); none removed or added. `done` took a line for each of the two revisits these change (S02-V-226 and S02-V-237).

Check, after the rulings: on a fresh copy holding only `b/RD1`, `merge_slices.py` merged 19 points and 314 rows. `check_subject.py` (3,116 statements, 97 gaps) gave no line of level `error`, 17 warnings on the length of phase A's quotes, and 14 reviews: 12 on quotes found only in a page's source, which are the coordinator's, and 2 on RD2's and RD3's statements, whose folders the copy leaves out. None names S02-V-228, S02-V-237, S02-BC-369, S02-BC-371 or S02-BC-385. RD1 has no row in its `unplaced.tsv`, and no open task in `second_pass_list.py --check`.

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

## Second pass, RD2-S1: every task of RD2's work list, bullets (e) and (g), all five platforms

### Revisits

- S02-V-424 (shopify, S02-VP-27, was `gap` S02-SH-G03). Its leads: S02-SH-689, S02-SH-704 and S02-SH-706 ('unlimited number of country or region markets') joined S02-V-411; S02-SH-707 ('The number of markets that you can create depends on your subscription plan.') joined S02-V-412; S02-SH-689 ('Create B2B markets'), S02-SH-706 and S02-SH-707 ('you can create') joined S02-V-425, the seller, under S02-VP-28. Two answers no row held: S02-V-424 is replaced by 'you can assign up to 3 active catalogs across all your B2B markets' (S02-SH-703, S02-SH-704), and S02-V-470 is added, 'you can create an unlimited number of B2B market catalogs' (S02-SH-703, S02-SH-704), both rules on what B2B markets may hold. S02-SH-G03 was settled by gap-closing and goes; the gap `why` names, S02-SH-G07, stands beside them as S02-V-471.
- S02-V-449 (woocommerce, S02-VP-27, was `gap` S02-WC-G04). Its leads are about shipping zones, which RD2-2 held to be shipping, under (f), not a market; they are noted below. Gap-closing settled S02-WC-G04 and left no gap or absence for the point, so the row is now `not covered` (see "Rows `not covered`").

### Rereads (RD2-2, (e); rule 4 as widened on 27 October 2026)

All four are placed; their earlier notes stay.
- S02-SA-026: the seller's controls that switch the multiple markets feature on ('اضغط (فعل الآن)', 'اضغط (تأكيد)'), joined to the seller's rows S02-V-438 (S02-VP-28) and S02-V-439 (S02-VP-29).
- S02-SA-054: the account manager who enables the feature, a new row S02-V-472 under S02-VP-28, and in the new row S02-V-473 under S02-VP-29.
- S02-SA-055 and S02-SA-059: the account manager who disables it, in S02-V-473 under S02-VP-29.

### Statements noted under (e)

- S02-WC-269 (e): 'You can add as many shipping zones or shipping methods as you need to your shipping settings; there is no limit.': a limit on shipping zones, shipping under (f), not on a market; X fails the role test
- S02-WC-270 (e): 'A shipping zone is a geographical area to which you ship items.': shipping, under (f); X fails the role test
- S02-SA-382 (e): 'Each store decides which countries it ships to and which payment methods it accepts.': the countries a store ships to, shipping under (f), and payment methods; X fails the role test
- S02-SH-628 (e): 'Pre-approved expansion store types', such as 'International stores': an expansion store is a store of its own on a Shopify Plus organization's contract, not a market a store sells into; X fails the role test
- S02-SH-629 (e): 'Shopify Plus plan organizations can have a maximum of ten stores on their contract': a limit on an organization's stores, not on a store's markets; X fails the role test
- S02-SH-783 (e): 'you can restrict access so that only logged-in B2B customers can view your store': who may view the store, a setting under (f); answers none of (e)'s questions
- S02-SH-784 (e): 'restricting access might redirect D2C customers to authentication on some pages': a setting of the store's access, under (f); answers none of (e)'s questions
- S02-SH-927 (e): 'Shipping profiles and shipping rates are gradually moving to shipping options by market': shipping per market, under (f); answers none of (e)'s questions
- S02-SH-939 (e): the shipping zone's countries and regions, with 'Add more countries/regions in Markets': a shipping zone, shipping under (f), not a market; X fails the role test, as RD2-1 held for S02-SH-235

### Statements noted under (g)

- S02-SH-653 (g): 'the Customer information settings apply to every country and market that you sell to': a setting that holds for the whole store, RD3's half

### Shopify's other statements under (e), placed

S02-SH-603, S02-SH-604, S02-SH-606, S02-SH-607, S02-SH-609, S02-SH-611, S02-SH-920, S02-SH-924 and S02-SH-925 joined S02-VP-26's rows S02-V-400, S02-V-401, S02-V-403, S02-V-404 and S02-V-405; S02-SH-605 joined S02-V-420 and S02-SH-937 S02-V-412. New rows: under S02-VP-27, S02-V-474 (S02-SH-604, what a channel market may hold), S02-V-475 (S02-SH-924, locations on Shopify POS Lite) and S02-V-476 (S02-SH-925, retail and online customers within one region); under S02-VP-28 and S02-VP-29, S02-V-477 and S02-V-478, apps (S02-SH-606); under S02-VP-29, S02-V-479, the platform, which deactivates the markets past a new plan's limit (S02-SH-937). S02-SH-609 names market types by their use ('for cross-border selling, wholesale, retail, and selling across sales channels'): only its 'sales channels' names what defines one, so it is placed in S02-V-405 only.

### zid: statements noted under (e)

- S02-ZD-186 (e): 'The endpoint returns all countries' names, codes, and IDs, and is not specific to any particular store's operations': a list of every country, not a market; answers none of (e)'s questions
- S02-ZD-187 (e): 'The **Region & Language popup** allows customers to change the store language, country, and city': the buyer switches region, market selection under (f); answers none of (e)'s questions
- S02-ZD-190 (e): '`zid.store.region.countries`', 'Returns the list of store countries': a theme function's list of countries, which the statement doesn't say define a market; answers none of (e)'s questions
- S02-ZD-191 (e): '`zid.store.region.setRegion`', 'Changes the store language, country, and city': the buyer's region, market selection under (f); answers none of (e)'s questions
- S02-ZD-447 (e): 'نربطك مباشرة بأكبر الأسواق' (my translation: we connect you directly to the biggest markets): names markets without what defines one, a limit, or who creates, changes or removes one; answers none of (e)'s questions

### zid, bigcommerce and salla: statements noted under (g)

None of these says that the platform has no market of the kind in (e), RD2's half of (g) (rule 4). Each is noted with what it says: a setting that holds for the whole store is RD3's half; the rest are neither half.

- S02-ZD-231 (g): 'لا يمكن تفعيل أكثر من نطاق في نفس الوقت.' (my translation: more than one domain can't be activated at the same time): the domain, a setting that holds for the whole store, RD3's half
- S02-BC-176 (g): 'Other features, like tax, belong to the global store': taxes, a setting that holds for the whole store, RD3's half
- S02-BC-185 (g): 'Currently, you cannot have different warehouse locations and inventory service different storefront channels.': locations, a setting that holds for the whole store, RD3's half
- S02-BC-292 (g): 'settings like measurement units and factoring dimension are applied globally': units, a setting that holds for the whole store, RD3's half
- S02-SA-339 (g): the Terms of Use's definition of the consumer, '( المستهلك ) يقصَد بهذه العبارة كل مستهلك يقوم بشراء المنتج أو الخدمة من التاجر' (my translation: the consumer means every consumer who buys the product or service from the merchant): neither half
- S02-SA-340 (g): 'في حال قيام التاجر بالتسجيل كمؤسسة أو شركة' (my translation: where the merchant registers as an establishment or company): the merchant's legal capacity, in the Terms; neither half
- S02-SA-341 (g): 'لا تلتزم منصة سلة بإتمام عمليات بيع المنتجات أو الخدمات بين المستهلك والمتجر' (my translation: Salla doesn't undertake to complete sales between the consumer and the store): who sells, for every store; not RD2's half
- S02-SA-342 (g): 'إن جميع التعاملات التي تتم بين التاجر والمستهلك لا علاقة لها بشخص منصة سلة' (my translation: all dealings between the merchant and the consumer have no relation to Salla itself): who sells, for every store; not RD2's half
- S02-SA-343 (g): 'كافة المتاجر الإلكترونية المسجلة في منصة سلة تمتلك سجل تجاري الكتروني خاص بها' (my translation: every online store registered on Salla holds its own commercial register): who sells, for every store; not RD2's half
- S02-SA-344 (g): 'اتفاقية الاستخدام هذه سارية على كافة المستخدمين لمنصة سلّة' (my translation: these Terms of Use apply to all of Salla's users): the terms, for every user; neither half
- S02-SA-377 (g): 'المتجر الذي اشتريت منه هو من ينفّذ الاسترجاع ويصدر ردّ المبلغ' (my translation: the store you bought from carries out the return and issues the refund): returns, for every store; not RD2's half
- S02-SA-378 (g): 'تختلف تجربة الاسترجاع من متجر لآخر' (my translation: the return experience differs from store to store): returns, which differ by store; not RD2's half
- S02-SA-379 (g): 'As a shopper, you buy from the store itself, not from Salla.': who sells; not RD2's half
- S02-SA-380 (g): 'It owns the product, sets the price and the return policy, prepares and ships your order': who sells, and who sets prices and returns; not RD2's half
- S02-SA-381 (g): 'The seller is the store where you placed the order': who sells; not RD2's half
- S02-SA-386 (g): 'Allow customers to cancel orders before they're processed.': cancellations, a setting of the whole store, RD3's half
- S02-SA-394 (g): 'الطلبات بالعملات المختلفة بعد تحويلها إلى العملة الأساسية للمتجر' (my translation: orders in different currencies after converting them to the store's base currency): reports in the store's base currency, RD3's half
- S02-SA-395 (g): 'converted to the store currency': reports in the store's currency, RD3's half
- S02-SA-401 (g): 'تثبيت تطبيق Google Analytics واختيار حساب المتجر على Google Analytics' (my translation: install the Google Analytics app and choose the store's account on Google Analytics): an app linked for the store; not RD2's half
- S02-SA-402 (g): 'أدخل نطاق/دومين متجرك' (my translation: enter your store's domain), in linking Google Analytics: not RD2's half
- S02-SA-403 (g): 'اختر مصدر بيانات متجرك من القائمة المتاحة' (my translation: choose your store's data source from the list): an app's setting for the store; not RD2's half
- S02-SA-404 (g): 'ويمكنك إعادة الربط مع أي حساب آخر على Google Analytics في أي وقت تريد' (my translation: you can link again with any other Google Analytics account at any time): an app's link for the store; not RD2's half
- S02-SA-405 (g): 'create a Google Tag Manager account and container for your store URL': an app for the store; not RD2's half
- S02-SA-406 (g): 'Keep one container per store.': an app's container for the whole store; not RD2's half
- S02-SA-407 (g): 'The pixel, the Conversions API and your product catalog are all connected automatically when you link your account.': an app's link for the store; not RD2's half
- S02-SA-408 (g): 'Choose the pixel you want, then click (Continue).': a step in linking an app; not RD2's half
- S02-SA-416 (g): 'The Salla App Store is where you browse and install apps that add features to your store': apps for the store; not RD2's half
- S02-SA-417 (g): 'Turn all store notifications on or off.': messages, a setting that holds for the whole store, RD3's half
- S02-SA-418 (g): the notifications table's headers, 'Email' and 'App notifications': messages, RD3's half
- S02-SA-419 (g): the staff permission 'store_notification_settings_management': staff access to the store's notification settings, RD3's half
- S02-SA-420 (g): 'استقبل إشعارات مباشرة على جوالك أو جهازك اللوحي' (my translation: receive notifications directly on your phone or tablet): notifications to the merchant; not RD2's half
- S02-SA-431 (g): 'Saudi Arabia time is currently the only time zone available.': the time zone of booking products, RD3's half
- S02-SA-432 (g): 'Currently, booking times use Saudi Arabia time only.': the time zone of booking products, RD3's half
- S02-SA-433 (g): 'If enabled, Saudi Arabia (Riyadh) time will be used in the order prep list.': the time zone of the order prep list, RD3's half
- S02-SA-434 (g): the weight units, 'Gram', 'Kilogram', 'Pound' and 'Ounce': units, RD3's half
- S02-SA-435 (g): 'Product weight and weight unit': units, per product; not RD2's half
- S02-SA-436 (g): 'Default product weight for shipping': a default for the whole store, RD3's half

### bigcommerce: statements under (e)

Placed: S02-BC-162 in S02-V-453 and S02-V-462; S02-BC-163, S02-BC-164, S02-BC-172, S02-BC-174, S02-BC-177, S02-BC-180 and S02-BC-323 in S02-V-455, S02-BC-323 also in S02-V-456 and S02-V-457; S02-BC-172 and S02-BC-177 in S02-V-465, the merchant. New rows under S02-VP-27: S02-V-480, storefront seats or the plan (S02-BC-178); S02-V-481, a locale in one storefront only (S02-BC-179); S02-V-482, up to five languages a channel (S02-BC-286). Noted:

- S02-BC-173 (e): 'Each locale's subfolder is set in the control panel on your default channel.': a domain subpath for a language on one channel, domain and language under (f); answers none of (e)'s questions
- S02-BC-183 (e): 'The Carts API supports selling in different markets by allowing locale-based overrides for product details.': names markets without what defines one; its overrides are product details per locale, under (f); answers none of (e)'s questions
- S02-BC-204 (e): 'Fires when customer settings that affect the specified channel are updated': a webhook on a channel's settings, under (f); answers none of (e)'s questions

### woocommerce: statements noted under (g)

None of woocommerce's statements under (g) in this work list says that the platform has no market of the kind in (e), RD2's half of (g) (rule 4). Each is noted with what it says: a setting that holds for the whole store is RD3's half; the rest are neither half.

- S02-WC-266 (g): 'customers from all over the world can use the gateway to check out and pay': payment methods, for every buyer, RD3's half
- S02-WC-274 (g): 'you're solely responsible for all of your ecommerce activities': who sells, in the terms; not RD2's half
- S02-WC-275 (g): 'User is solely responsible for, and Stripe disclaims all liability for, the provision of goods and services sold to User's Customers': who sells, in a provider's terms; not RD2's half
- S02-WC-276 (g): 'must maintain fair and legally compliant return, refund, cancellation, and adjustment policies': returns, for every store; not RD2's half
- S02-WC-277 (g): 'are responsible for all products and services you provide, including delivery, support, refunds, returns': who sells; not RD2's half
- S02-WC-281 (g): 'WITHDRAWAL_WINDOW_IN_DAYS           = 14': returns, a value for the whole store, RD3's half
- S02-WC-282 (g): 'Enable the public order withdrawal feature for customer requests.': returns, a setting of the whole store, RD3's half
- S02-WC-283 (g): 'It’s up to you how withdrawal requests are handled': returns, RD3's half
- S02-WC-284 (g): 'The form accepts requests for orders of any age.': returns, RD3's half
- S02-WC-285 (g): 'We have created a sample draft Refund and Returns Policy page for you.': returns, a page of the whole store, RD3's half
- S02-WC-288 (g): '$default_weight_unit = $locale_info['US']['weight_unit'];': the units' default, RD3's half
- S02-WC-289 (g): 'This controls what unit you will define weights in.': units, a setting of the whole store, RD3's half
- S02-WC-290 (g): 'which determines the weight unit used throughout the store': units, a setting that holds for the whole store, RD3's half
- S02-WC-291 (g): 'This controls what unit you will define lengths in.': units, a setting of the whole store, RD3's half
- S02-WC-310 (g): the site's time zone, 'timezone_string': a setting of the whole site, RD3's half
- S02-WC-311 (g): 'The date the order was created, in the site's timezone.': the site's time zone, RD3's half
- S02-WC-312 (g): 'Set your store\'s address, visibility, currency, language, and timezone.': settings of the whole store, RD3's half
- S02-WC-315 (g): 'Choose the currency the store will display on products.': currency, RD3's half
- S02-WC-324 (g): 'Go to WP Admin > Settings > General and adjust the Site Language.': language, RD3's half
- S02-WC-325 (g): 'the shop displays in your locale if the language file exists': language, RD3's half
- S02-WC-329 (g): 'Allows customers to checkout without an account.': checkout and customer accounts, RD3's half
- S02-WC-330 (g): 'Account creation', 'After checkout (recommended)': checkout and customer accounts, RD3's half
- S02-WC-331 (g): 'Customers can create an account before placing their order.': checkout and customer accounts, RD3's half
- S02-WC-332 (g): 'Account creation', 'On "My account" page': customer accounts, RD3's half
- S02-WC-333 (g): 'Set options relating to customer accounts and data privacy.': customer accounts and privacy, RD3's half
- S02-WC-338 (g): 'Go to WooCommerce > Settings and select the Accounts and Privacy tab.': customer accounts and privacy, RD3's half
- S02-WC-339 (g): 'Use these settings to enable or disable guest checkout, control customer account creation': checkout and customer accounts, RD3's half
- S02-WC-340 (g): 'Allow customers to check out without creating an account.': checkout and customer accounts, RD3's half
- S02-WC-341 (g): 'Allow customers to create an account before placing their order.': customer accounts, RD3's half
- S02-WC-346 (g): 'This setting determines which shop pages products will be listed on.': products, RD3's half
- S02-WC-347 (g): the catalog visibility options 'Shop and search results', 'Shop only', 'Search results only' and 'Hidden': products, RD3's half
- S02-WC-348 (g): 'Hide out of stock items from the catalog': products, RD3's half
- S02-WC-361 (g): 'WooCommerce core offers fixed-cart, fixed-product, and percentage-based coupons.': discounts, RD3's half
- S02-WC-362 (g): 'You need an administrator or shop manager account to manage coupons.': discounts and staff access, RD3's half
- S02-WC-364 (g): 'WooCommerce core does not apply coupon codes automatically.': discounts, RD3's half
- S02-WC-366 (g): 'Enable the use of coupon codes': discounts, a setting of the whole store, RD3's half
- S02-WC-368 (g): 'Enable or disable coupons in your store.': discounts, RD3's half
- S02-WC-373 (g): the product's 'Sale price', labelled with 'get_woocommerce_currency_symbol()': prices in the store's one currency, RD3's half
- S02-WC-375 (g): 'select options that apply site-wide for Store Notice, Product Catalog, and Product Images': storefront design, RD3's half
- S02-WC-376 (g): 'Add a store wide alert/banner notice': storefront design, RD3's half
- S02-WC-377 (g): 'If enabled, this text will be shown site-wide.': storefront design, RD3's half
- S02-WC-379 (g): 'The Customize your store task opens a simplified design screen': storefront design, RD3's half
- S02-WC-386 (g): the option '"From" name', 'woocommerce_email_from_name': messages to buyers, RD3's half
- S02-WC-387 (g): the option '"From" address', 'woocommerce_email_from_address': messages to buyers, RD3's half
- S02-WC-395 (g): 'Enable stock management': stock, a setting of the whole store, RD3's half
- S02-WC-396 (g): 'Track stock quantity for this product': stock, a setting per product; not RD2's half
- S02-WC-401 (g): 'Enable this feature to track and credit channels and campaigns that contribute to orders on your site': a feature of the whole site, RD3's half
- S02-WC-404 (g): 'You can enable (or disable) this feature by going to WooCommerce > Settings > Advanced > Features > Order Attribution.': RD3's half
- S02-WC-408 (g): 'All data in your site’s Analytics menu will be converted into your store’s default currency.': reports in the default currency, RD3's half
- S02-WC-411 (g): 'check or uncheck the Enable tracking checkbox': data sharing, a setting of the whole store, RD3's half
- S02-WC-412 (g): 'You can configure GA4 in your store’s WP Admin dashboard': an extension's setting for the whole store, RD3's half
- S02-WC-418 (g): 'Leave this box unchecked if you do not want to pull suggested extensions from WooCommerce.com.': a setting of the admin; not RD2's half
- S02-WC-422 (g): 'One active subscription key can be used on one active (production) site': a WooCommerce.com subscription, the platform's own account; neither half
- S02-WC-423 (g): 'Set the locale to the store locale for customer emails to make sure emails are in the store language.': messages in the store's language, RD3's half
- S02-WC-425 (g): 'For each WooCommerce email listed, it’s possible to configure your settings (optional).': messages, RD3's half
- S02-WC-426 (g): 'use the “From” name and “From” address fields to set the sender identity customers see': messages, RD3's half
- S02-WC-428 (g): 'Let customers sign up to be notified when products in your store are restocked.': messages, RD3's half
- S02-WC-430 (g): 'Enter recipients (comma separated) that will receive this notification.': notifications to the store's own staff; not RD2's half
- S02-WC-431 (g): 'Enable low stock notifications': notifications to the store's own staff; not RD2's half
- S02-WC-432 (g): 'Enter comma-separated recipients for this email.': emails to shop managers and admins; not RD2's half
- S02-WC-440 (g): 'Enable WooCommerce Analytics to track your store\'s key metrics': reports, a feature of the whole store, RD3's half
- S02-WC-441 (g): 'This section controls the display of your website privacy policy.': privacy, RD3's half
- S02-WC-442 (g): 'Optionally add some text about your store privacy policy to show on account registration forms.': privacy, RD3's half
- S02-WC-443 (g): 'Optionally add some text about your store privacy policy to show during checkout.': privacy, RD3's half
- S02-WC-444 (g): 'Choose how long to retain personal data': privacy, RD3's half
- S02-WC-445 (g): 'This section lets you select a privacy policy page': privacy, RD3's half
- S02-WC-446 (g): 'Open Settings > Privacy, where you can select your privacy policy page.': privacy, RD3's half
- S02-WC-447 (g): 'Use this section to decide how long your store keeps order data.': privacy, RD3's half
- S02-WC-451 (g): 'Use these roles to control who can manage products, view reports, and configure store settings.': staff access, RD3's half
- S02-WC-452 (g): 'choose a role from the Role dropdown': staff access, RD3's half
- S02-WC-453 (g): 'WooCommerce adds several capabilities to the existing Administrator role.': staff access, RD3's half
- S02-WC-454 (g): 'Manage WooCommerce — Access to WooCommerce settings and configuration.': staff access, RD3's half
- S02-WC-455 (g): 'View WooCommerce reports — Access to all WooCommerce analytics and reports.': staff access, RD3's half
- S02-WC-456 (g): 'The Shop Manager role allows someone to manage your store without granting full Administrator access.': staff access, RD3's half
- S02-WC-457 (g): 'Manage WooCommerce — Full access to all WooCommerce settings and configuration.': staff access, RD3's half
- S02-WC-458 (g): 'View WooCommerce reports — Access to all WooCommerce analytics and reports.': staff access, RD3's half
- S02-WC-459 (g): 'Manage products — Create, edit, delete, and publish products': staff access, RD3's half
- S02-WC-460 (g): 'Manage orders — View, edit, and delete orders, as well as process refunds.': staff access, RD3's half
- S02-WC-461 (g): 'Manage customers — Shop Managers can view user details for all roles.': staff access, RD3's half
- S02-WC-462 (g): 'Shop Managers also have general WordPress editor capabilities': staff access, RD3's half
- S02-WC-463 (g): 'you can use an extension or plugin to adjust permissions without editing code': staff access, RD3's half
- S02-WC-464 (g): 'A WooCommerce extension that allows you to add, assign, and switch user roles within your store.': staff access, RD3's half
- S02-WC-465 (g): 'A WordPress plugin that provides a detailed interface for editing role capabilities.': staff access, RD3's half
- S02-WC-466 (g): 'A WordPress plugin for managing user roles, capabilities, and content permissions.': staff access, RD3's half
- S02-WC-467 (g): 'A WordPress plugin for managing group-based access control and permissions.': staff access, RD3's half
- S02-WC-468 (g): 'add_role( 'shop_manager', 'Shop manager',': staff access, RD3's half
- S02-WC-469 (g): '$wp_roles->add_cap( 'shop_manager', $cap );': staff access, RD3's half
- S02-WC-470 (g): 'these are assigned to admin/shop manager during installation or reset': staff access, RD3's half
- S02-WC-471 (g): '$capabilities['core'] = array( 'manage_woocommerce', 'create_customers', 'view_woocommerce_reports', );': staff access, RD3's half
- S02-WC-472 (g): '$capability_types = array( 'product', 'shop_order', 'shop_coupon' );': staff access, RD3's half
- S02-WC-473 (g): 'woocommerce_shop_manager_editable_roles': staff access, RD3's half
- S02-WC-474 (g): ''settings' => 'manage_woocommerce'': staff access, RD3's half
- S02-WC-475 (g): ''shipping_methods' => 'manage_woocommerce'': staff access, RD3's half
- S02-WC-476 (g): 'Coming soon mode controls who can visit your site while you prepare it for launch.': store status, a setting of the whole site, RD3's half
- S02-WC-477 (g): 'Go to WooCommerce > Settings > Site visibility to switch between Coming soon and Live.': store status, RD3's half
- S02-WC-478 (g): 'The badge reads Coming soon, Store coming soon, or Live based on your visibility settings.': store status, RD3's half
- S02-WC-479 (g): 'From this screen, choose Coming soon or Live.': store status, RD3's half
- S02-WC-480 (g): 'When Coming soon mode is enabled, your site is in a development state and not accessible to the public.': store status, RD3's half
- S02-WC-481 (g): 'Enabling this option ensures that only store-related pages are protected by Coming soon mode.': store status, RD3's half
- S02-WC-482 (g): 'Visitors will not be able to access store pages without permission': store status, RD3's half
- S02-WC-483 (g): 'the Coming soon landing page is displayed instead of the following WooCommerce store pages': store status, RD3's half
- S02-WC-484 (g): 'Cart (Assigned via WooCommerce > Settings > Advanced).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-485 (g): 'Checkout (Assigned via WooCommerce > Settings > Advanced).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-486 (g): 'Terms and conditions (Assigned via WooCommerce > Settings > Advanced).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-487 (g): 'Shop (Assigned via WooCommerce > Settings > Products > General).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-488 (g): 'Privacy policy (Assigned via Settings > Accounts & Privacy).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-489 (g): 'A private link is generated for you to provide selective access to your site': store status, RD3's half
- S02-WC-490 (g): 'When live mode is enabled, your site is fully accessible to all visitors': store status, RD3's half
- S02-WC-491 (g): 'Stores that are already live will default to live mode': store status, RD3's half
- S02-WC-492 (g): 'Stores that install WooCommerce and complete the onboarding process will default to Coming soon mode.': store status, RD3's half
- S02-WC-493 (g): 'This is the default setting for new sites, determined by the fresh_site WordPress flag.': store status, RD3's half
- S02-WC-494 (g): 'If the first admin user registration date is less than a month ago.': store status, RD3's half
- S02-WC-495 (g): 'the Apply to store pages only toggle is enabled by default': store status, RD3's half
- S02-WC-496 (g): 'This guide provides examples for third-party developers and hosting providers on how to integrate their systems with WooCommerce's coming soon mode.': store status, RD3's half
- S02-WC-497 (g): 'WooCommerce's coming soon mode allows you to temporarily make your site invisible to the public while you work on it.': store status, RD3's half
- S02-WC-498 (g): 'The coming soon mode can be programmatically synced from a plugin or application.': store status, RD3's half
- S02-WC-499 (g): 'Integrating with a maintenance mode plugin.': store status, RD3's half
- S02-WC-500 (g): 'Integrating with a hosting provider's coming soon mode.': store status, RD3's half
- S02-WC-501 (g): 'enable or disable WooCommerce coming soon mode from another plugin by directly updating woocommerce_coming_soon option': store status, RD3's half
- S02-WC-502 (g): 'We could also programmatically bind the coming soon option from another plugin': store status, RD3's half
- S02-WC-503 (g): 'It is possible for developers to add custom exclusions that bypass the coming soon protection.': store status, RD3's half
- S02-WC-504 (g): 'you may want to add a custom page to the list of store pages which will be restricted by coming soon mode': store status, RD3's half
- S02-WC-505 (g): 'Use the Launch your store task when you’re ready to make your store public.': store status, RD3's half
- S02-WC-506 (g): 'From the site visibility settings, you’ll be able to enable Coming soon mode': store status, RD3's half
- S02-WC-507 (g): 'if ( current_user_can( 'manage_woocommerce' ) ) {': store status and staff access, RD3's half
- S02-WC-508 (g): 'apply_filters( 'woocommerce_coming_soon_exclude', false )': store status, RD3's half
- S02-WC-509 (g): ''woocommerce_coming_soon' => array( 'yes', 'no' )': store status, RD3's half

### woocommerce: statements noted under (e)

- S02-WC-359 (e): 'You can only select the countries that you’re targeting on Google Merchant Center. Your target countries must be eligible for both Google Merchant Center and Google Ads.': the countries the Google for WooCommerce extension targets with listings and ads on Google, which the statement doesn't say are a market the store sells into; X fails the role test (WooCommerce's market is its selling locations, as RD2-2 held)

### RD2-S1: rows `not covered`

- S02-V-449: woocommerce, S02-VP-27 (`what limits "market"`), was `gap` S02-WC-G04. Gap-closing settled the gap and left none for the point, and its leads (S02-WC-269, S02-WC-270) are about shipping zones, noted above. No statement, gap or absence of woocommerce answers the point, so the row goes back to woocommerce (rule 4).

### RD2-S1: matching (rule 5)

Each statement placed was compared with the point's `raised_by`. The rows joined are each platform's own, and keep their bases. The new rows of salla (S02-V-472, S02-V-473) and bigcommerce (S02-V-480 to S02-V-482) share no term, identifier or definition with the shopify statements in `raised_by` (S02-SH-111, S02-SH-301, S02-SH-286; S02-SH-115, S02-SH-116, S02-SH-288; S02-SH-061, S02-SH-128, S02-SH-288), so each takes `answers` alone, as do shopify's new rows.

### RD2-S1: new kinds, searches and candidates for a new point

- New kinds: none; (e)'s points take no kind (rule 3).
- Searches for earlier platforms' rows: none; the second pass raised no point.

### Candidates for a new point

None. Every statement of the work list that answers one of (e)'s questions does so for a market a store sells into, the one X of (e)'s points, and none of the (g) statements says that the platform has no market of the kind in (e).

### RD2-S1: problems with the method

- S02-V-449 is now `not covered`, after gap-closing. Phase A's gap S02-WC-G04 asked, under (e), how many shipping zones a store can hold; gap-closing answered it (S02-WC-269: 'there is no limit'), but under the role test, as RD2-2 held, a shipping zone is not a market, so the answer is noted. The row goes back to woocommerce, and A2 has run: the coordinator decides.
- Rule 4, as widened on 27 October 2026, makes the party that switches a feature on its own answer under both `who creates` and `who changes or removes`. S02-SA-054 ('Contact your account manager to enable this feature.') names no feature by name: that it is the multiple markets feature is a reading, marked in S02-V-472 and S02-V-473. S02-SA-059 is in the same list as S02-SA-058, which names the market. S02-SA-026, the seller's own controls, joined the seller's rows.
- S02-SH-703 and S02-SH-704 set limits on the catalogs B2B markets hold. They are placed under S02-VP-27 as rules on what a market may hold (S02-V-424, S02-V-470), as RD2-1 placed what a channel market may hold (S02-V-420). If such rules are read as (f)'s alone, the two rows go.
- S02-SH-604 ('Merchants can't configure web presence, domains, or discounts for channel markets.'), S02-SH-925 and S02-BC-286 ('Each channel can support up to five languages.') are rules on which settings a market may hold. They are placed under S02-VP-27 (S02-V-474, S02-V-476, S02-V-482), whose note holds both limits on how many and on what a market holds; they also bear on RD3's points.
- S02-SH-628 and S02-SH-629, Shopify Plus's expansion stores (including 'International stores' in another region or currency), are noted: an expansion store is a store of its own, not a market of a store.
- S02-WC-359, Google for WooCommerce's target countries, is noted. If a sales channel's target countries count as a market a store sells into, as zid's and bigcommerce's channels do (S02-V-443, S02-V-453), it answers S02-VP-27 for woocommerce, and S02-V-449 would take it in place of `not covered`.

## Second pass, RD2-S2: the last round's tasks of RD2's work list (after A2-T, A2-SH-H, A2-SA-H, A2-SA-S and A3-2), bullets (e) and (g); shopify, salla, woocommerce and bigcommerce

### Revisits

- S02-V-471 (shopify, S02-VP-27, was `gap` S02-SH-G07; RD2-S1 had revisited S02-V-424 into it). Its new lead S02-SH-1024 ('You’ve reached the limit of 100 markets using the “All” condition.', in the admin's code) gives an answer no row held, and replaces S02-V-471. S02-SH-1025 names two error codes: 'SHOP_REACHED_PLAN_MARKETS_LIMIT', a plan's markets limit, joined S02-V-412 ('The number of markets that you can create depends on your subscription plan.'); 'SHOP_REACHED_MARKETS_LIMIT', the same key as S02-SH-286's, joined S02-V-413 ('Can't have more than 50 markets.'), whose evidence now says the admin's code names it with no number. The leads RD2-S1 placed (S02-SH-689, S02-SH-703, S02-SH-704, S02-SH-706, S02-SH-707) stay in S02-V-411, S02-V-412, S02-V-424, S02-V-470 and S02-V-425. S02-SH-G12, which says it is 'in place of S02-SH-G07', stands beside the answers as the new row S02-V-483; S02-SH-G07 goes.
- S02-V-449 (woocommerce, S02-VP-27, was `not covered` after RD2-S1's revisit). Its leads S02-WC-513 ('Sell to all countries, except for&hellip;', 'woocommerce_all_except_countries') and S02-WC-514 ('Sell to specific countries', 'woocommerce_specific_allowed_countries') are the selling locations' two country lists: they say what defines the market, and joined S02-V-448 under S02-VP-26, which already held the two options (S02-WC-129, S02-WC-130). They name no party, so they join no row of S02-VP-28 or S02-VP-29. S02-WC-515 is noted below; S02-WC-269 and S02-WC-270 stay noted, as RD2-S1 noted them. The row is now `absent`, with S02-WC-N01 (kind shipped; A3-2 confirmed it): no settings page caps the countries a store sells to or sets when a selling location applies.

### Statements noted under (e)

- S02-WC-515 (e): 'if ( ! empty( $value['options'] ) ) { $countries = $value['options']; } else { $countries = WC()->countries->countries; }': the countries any 'multi_select_countries' field offers; its words, identifier ('output_fields(), case 'multi_select_countries': the countries a country list offers') and scope name no selling location, so X fails the role test. S02-WC-N01's own words read it with S02-WC-513 and S02-WC-514 (see "Problems")

### Statements placed (`place` tasks)

- S02-SA-440 (salla, (e)): the storefront's settings answer on the store aldakheel-test, whose 'scope' ('"type": "scope"'), named 'متجر السعودية', holds '"countries": ["SA"]'. Joined S02-V-431 under S02-VP-26 (a country defines a market), the scope read as a market as S02-V-431 reads S02-SA-251's store scope (a reading, marked there). Its null 'country_id' and 'city_id' name no city, so it doesn't join S02-V-432. It answers none of (e)'s other questions.
- S02-BC-358 (bigcommerce, (e)): 'Note that many third-party sales channels are apps, which can only be installed by the store owner or users with the Install applications permission.' Two new rows under S02-VP-28, each its own answer by rule 4, as S02-V-427 holds a permission for shopify: S02-V-484 'the store owner' and S02-V-485 'users with the Install applications permission'. That installing a sales channel's app creates the channel in the store is a reading, marked in both rows. 'third-party sales channels' is added to S02-VP-28's x_words for bigcommerce. It names no change or removal, so it isn't placed under S02-VP-29.

### Statements noted under (g)

Each is a statement under (g) on a setting of the store, which each platform's `a2.tsv` names for RD3's points (bigcommerce: S02-VP-92; salla: S02-VP-65, S02-VP-73, S02-VP-74, S02-VP-87 and S02-VP-89). None says that the platform has no market of the kind in (e), RD2's half of (g).
- S02-BC-352 (g): 'To install or update apps and leave reviews, you must be the store owner or have the Install applications permission enabled on your user account.': who may install a store's apps, RD3's half
- S02-BC-353 (g): 'To uninstall apps or cancel an app installation, you must have the Uninstall applications permission enabled.': who may uninstall a store's apps, RD3's half
- S02-BC-354 (g): 'To launch apps, you must be the store owner, have the Launch applications permission, or have been granted access to a multi-user Single Click App.': who may launch a store's apps, RD3's half
- S02-BC-355 (g): 'View a searchable list of your installed apps by going to Apps › My apps in the control panel.': the store's installed apps, managed in its control panel, RD3's half
- S02-BC-356 (g): 'Install applications Install apps from the App Marketplace.': a user permission over the store's apps, RD3's half
- S02-BC-357 (g): 'Uninstall applications Uninstall apps from the store.': a user permission over the store's apps, RD3's half
- S02-SA-437 (g): '"id":"order-cancellation-form","method":"PUT","action":"settings/fields/orders.cancel_order"': the order cancellation setting's form in the settings center, RD3's half
- S02-SA-438 (g): '"id":"all-notifications"', with '/notifications/v1/inbox/preferences/': the notifications section's field, RD3's half
- S02-SA-442 (g): 'storeData:{id:t.id,domain:t.domain,name:t.name,currency:t.currency,kycCountry:n}': the store's data the ads tools send to connect a pixel catalog, RD3's half
- S02-SA-443 (g): 'await rLe.post({endpoint:"ReturnPolicy",payload:{days:x}})': the return policy's days, set from the theme editor, RD3's half
- S02-SA-450 (g): '"action":"settings/fields/scopes.browse_product_method"': the markets section's setting of how products are browsed, RD3's half
- S02-SA-456 (g): '{"status":200,"success":true,"data":{"enabled":false,"hours":48}}': the order cancellation setting's saved value, RD3's half
- S02-SA-457 (g): 'ze="settings/fields/orders.cancel_order"': the order cancellation setting in the dashboard's code, RD3's half
- S02-SA-458 (g): 'fetch(Xt("/inbox/preferences/")': the signed-in user's notification preferences, read in the dashboard's code, RD3's half
- S02-SA-459 (g): '{"level":"global","enabled":true,"channels":{"in_app":true}}': the signed-in user's notification preferences, RD3's half
- S02-SA-460 (g): 'notifications#table.header.in_app' and 'notifications#table.header.email': the notification preferences table's columns, RD3's half

### RD2-S2: rows replaced or removed

- S02-V-471 (shopify, S02-VP-27): `gap` S02-SH-G07, replaced by the answer 'You’ve reached the limit of 100 markets using the “All” condition.' (S02-SH-1024); S02-SH-G12 stands beside it as S02-V-483.
- S02-V-449 (woocommerce, S02-VP-27): `not covered`, replaced by `absent` (S02-WC-N01).
- No row removed.

### RD2-S2: rows `not covered`

None. RD2-S1's one `not covered` row of RD2, S02-V-449, is now `absent`.

### RD2-S2: matching (rule 5)

S02-VP-27's `raised_by` (S02-SH-111, S02-SH-301, S02-SH-286) holds only shopify's statements, so shopify's rows take `answers`. S02-SH-1025 was compared with S02-SH-286, its own platform's, to join S02-V-413: they name the same key, 'SHOP_REACHED_MARKETS_LIMIT'; rechecked, the row keeps `answers`, since rule 5's bases compare with another platform's statement. S02-BC-358 shares no term, identifier or definition with S02-VP-28's `raised_by` (S02-SH-115, S02-SH-116, S02-SH-288), so S02-V-484 and S02-V-485 take `answers` alone. The rows joined (S02-V-412, S02-V-413, S02-V-431, S02-V-448) keep their bases.

### RD2-S2: new kinds and searches

- New kinds: none; (e)'s points take no kind (rule 3).
- Searches for earlier platforms' rows: none; the second pass raised no point.

### Candidates for a new point (RD2-S2)

None. The statements of these tasks that answer one of (e)'s questions do so for a market a store sells into (shopify's markets, woocommerce's selling locations, salla's scope, bigcommerce's sales channels), the one X of (e)'s points; S02-WC-515's X is any country list field, which fails the role test rather than raising another X. None of the (g) statements says that the platform has no market of the kind in (e).

### RD2-S2: problems with the method

- S02-WC-515 is noted, but bears on S02-VP-27. It fills any 'multi_select_countries' field with the field's options or else WooCommerce's countries; its own words, identifier and scope name no selling location. S02-WC-513 and S02-WC-514 give the selling locations' two lists that type ('type' => 'multi_select_countries'), and S02-WC-N01's words read the three together ('its two country lists (S02-WC-513, S02-WC-514) offer the countries WooCommerce lists (S02-WC-515)'). If a reading across two statements may pass the role test, S02-WC-515 answers S02-VP-27 for woocommerce as a rule on what a selling location may hold, as S02-V-417 ('Can't add unsupported country or region.') does for shopify, and it would stand beside the `absent` row, whose absence is of a cap and of a condition on when a selling location applies. The coordinator decides.
- S02-SH-1025's 'SHOP_REACHED_MARKETS_LIMIT' joined S02-V-413 by the same key as S02-SH-286, which the schema marks deprecated ('"isDeprecated":true', 'No longer used'). The admin's code names the key with no number. If the key in the admin's code is read as another limit than the schema's 50, S02-SH-1025 takes a row of its own for it, and stays in S02-V-412.
- S02-BC-358 says the store owner or users with the permission install a third-party sales channel's app. That this creates a channel, S02-VP-28's question, is a reading, marked in S02-V-484 and S02-V-485.
- `place` tasks have no `done` line: the brief's `done` records revisit, reread and note tasks, and `unplaced.tsv` checks the rest. The message's "Record each task with `done` as usual" was read that way.

## Second pass, RD2-S3: the capture round's tasks of RD2's work list (after A2-SH-R1 and A2-SH-R2, observed-sh 19a5f6435), bullet (e); shopify

Most statements of this round are observations of one store on one day, 27 October 2026. Each row they joined took its `kind` and `scope` again from all its statements (rule 6), and each `basis_evidence` added names the store, its plan, and the run and step: a run says what one store showed, not what every store does.

### Revisits

- S02-V-483 (shopify, S02-VP-27, was `gap` S02-SH-G12; RD2-S2 had revisited S02-V-471 into it). Its new leads are the runs of 27 October on demo-fake-dev-store (Basic App Development) and fake-demo-sharrwah (Advanced, paid). None states a limit, or a rule on how many markets a store can hold or on what one may hold, so none answers S02-VP-27 (see "Problems"). They say what defines a market, and joined S02-VP-26's rows:
  - S02-SH-1101, the condition types' menu on demo-fake-dev-store ('menuitem "Regions"', 'menuitem "POS locations"', 'menuitem "Company locations"', 'menuitem "Channels"'), joined S02-V-401, S02-V-403, S02-V-404 and S02-V-405, which hold the same menu of S02-SH-304 and S02-SH-370;
  - S02-SH-1113, the menu on fake-demo-sharrwah ('menuitem "Regions"', 'menuitem "Company locations"', 'menuitem "Channels"'), joined S02-V-401, S02-V-403 and S02-V-405; it shows no 'POS locations', so it didn't join S02-V-404;
  - S02-SH-1102 and S02-SH-1103, markets of the type 'B2B' that include 'Powderbound' and 'Snowdevil', and S02-SH-1115, 'Condition type Company locations' with 'Include all existing and future locations in all regions', joined S02-V-403; that Powderbound and Snowdevil are company locations is a reading, marked there;
  - S02-SH-1104 and S02-SH-1105, markets of the type 'Retail' that include 'Shop location' and 'Capture location 2', joined S02-V-404;
  - S02-SH-1109, 'Condition type Channels' with 'Showing 0 channels No channels found', joined S02-V-405;
  - S02-SH-1107 ('Capture submarket Germany Region Active', 'Includes Germany', 'Parent market Austria, Belgium, Czechia, Denmark, Finland, France, and others (European Union)') joined S02-V-401 and S02-V-406, and S02-SH-1108 ('Parent market European Union', on that parent market) joined S02-V-406: a market whose parent market is another market is a submarket (S02-SH-080, S02-SH-062). RD2-1 noted S02-SH-307, whose parent market is 'Store default'; these two name another market as the parent;
  - S02-SH-1106, the markets list after the run's markets were saved, is noted below.

  The leads earlier parts placed stay: S02-SH-1024 in S02-V-471; S02-SH-1025 in S02-V-412 and S02-V-413; S02-SH-689, S02-SH-704 and S02-SH-706 in S02-V-411; S02-SH-703 and S02-SH-704 in S02-V-424 and S02-V-470; S02-SH-707 in S02-V-412; S02-SH-689, S02-SH-706 and S02-SH-707 in S02-V-425. No lead gives S02-VP-27 an answer its rows don't hold. S02-SH-G16 says it is 'in place of S02-SH-G12', so S02-SH-G12 goes, and S02-V-483 is now `gap` S02-SH-G16, beside shopify's answers. The statements the `why` names outside the slice (S02-SH-1019 to S02-SH-1023, S02-SH-1112, S02-SH-1114, S02-SH-690 to S02-SH-702, S02-SH-705) are left.

### Statements noted under (e)

- S02-SH-1106 (e): the markets list on demo-fake-dev-store (Basic App Development, run 20261027T194903Z, step 63), 'Capture B2B market 1 Active Powderbound Capture B2B market 2 Active Snowdevil Currency Capture retail market 1 Active Shop location Currency Capture retail market 2 Active Capture location 2 Currency': four markets the run made and named, each 'Active'. Its own words state no limit or rule on how many markets a store can hold, and name no market's type or condition and no party; the markets it lists are those of S02-SH-1102 to S02-SH-1105, placed under S02-VP-26 (see "Problems")

### Statements placed (`place` tasks)

- Placed in S02-V-401 (countries define a Region market): S02-SH-1091 and S02-SH-1095, the market 'Capture UK market', 'Region', 'Includes United Kingdom', on capture-us-plus (Plus dev store) in two runs; S02-SH-1118, 'Capture checkout countries Region Active' with 'Includes Brazil Japan Saudi Arabia +1 more', and S02-SH-1120, the market Canada with 'Includes Brazil Canada Japan +2 more', both on demo-fake-dev-store.
- Placed in S02-V-401 and S02-V-425: S02-SH-1100, the admin's 'MarketsHomeMarketCreate (marketCreate)' answer at 'step 10 (Save)' on capture-us-plus: its '"type":"REGION"' says what defines the market, and the admin's Save that created it is a control in the store's admin, the seller (rule 4). Its '"businessEntity":null' is (f)'s, RD3's.
- Placed in S02-V-400 and S02-V-425: S02-SH-1093 and S02-SH-1116, the New market page ('Includes Add condition') on capture-us-plus and fake-demo-sharrwah: conditions define a market, and the seller creates it from the admin, as the rows already hold the New market pages S02-SH-368, S02-SH-407, S02-SH-415, S02-SH-419 and S02-SH-421.
- Placed in S02-V-428 (the seller changes or removes a market): S02-SH-1110, 'Edit market handle Delete market' under 'More actions', and S02-SH-1111, the 'Delete Capture submarket Germany?' dialog with its 'Delete' button, both on demo-fake-dev-store: controls in the store's admin (rule 4). S02-SH-1120 also joined S02-V-428: its scope says Saudi Arabia, the United Arab Emirates, Japan and Brazil were 'added to the Canada market' and saved, a change of what a market includes, made with the admin's Save, as S02-SH-125 ('You can adjust which countries or regions belong to a market') has it.
- Not placed under S02-VP-28 or S02-VP-29: S02-SH-1118, S02-SH-1102 to S02-SH-1105 and S02-SH-1107, whose scope names a 'Save' but not whether it created or changed the market.

### Statements placed that RD2's work list doesn't hold

S02-SH-1092, S02-SH-1094 and S02-SH-1095 are shopify's, under (e), in RD2's slice as cut again (28 October, 00:18), and were in no row and no note. RD2's work list (27 October, 23:50) has no task for them; shopify's `a2.tsv` names them for S02-VP-26, and S02-SH-1092 for S02-VP-28 too. By the brief's Output, step 5, they are this part's to place:
- Placed in S02-V-401: S02-SH-1092, the markets list on capture-us-plus ('Market Status Includes', over 'Canada Active Canada' and 'United States Active United States'), its 'Includes' column read as each market's condition (a reading, marked in the row). It shows no control that creates a market, so it isn't placed under S02-VP-28.
- Placed in S02-V-401, S02-V-403, S02-V-404 and S02-V-405: S02-SH-1094, the condition types' menu on capture-us-plus, with the same four items as S02-SH-1101.
- Placed in S02-V-401: S02-SH-1095, with S02-SH-1091 (above).

### RD2-S3: rows replaced or removed

- S02-V-483 (shopify, S02-VP-27): `gap` S02-SH-G12, replaced by `gap` S02-SH-G16, which is 'in place of S02-SH-G12'. No lead gave S02-VP-27 an answer its rows don't hold, so no answer row was added.
- No row removed.

### RD2-S3: rows `not covered`

None.

### RD2-S3: matching (rule 5)

The `raised_by` of S02-VP-26 (S02-SH-077, S02-SH-065, S02-SH-279), S02-VP-28 (S02-SH-115, S02-SH-116, S02-SH-288) and S02-VP-29 (S02-SH-061, S02-SH-128, S02-SH-288) hold only shopify's statements. Each statement joined was compared with its own platform's rows; rechecked, the rows joined (S02-V-400, S02-V-401, S02-V-403, S02-V-404, S02-V-405, S02-V-406, S02-V-425, S02-V-428) keep `answers`, since rule 5's other bases compare with another platform's statement.

### RD2-S3: new kinds, searches and x_words

- New kinds: none; (e)'s points take no kind (rule 3).
- Searches for earlier platforms' rows: none; the second pass raised no point.
- x_words: none added; the statements call X 'market', as shopify's x_words already hold it.

### Candidates for a new point (RD2-S3)

None. Every statement of these tasks that answers one of (e)'s questions does so for shopify's market, a market a store sells into, the one X of (e)'s points.

### RD2-S3: problems with the method

- S02-VP-27 and the runs of 27 October. On demo-fake-dev-store (Basic App Development), a second B2B market (S02-SH-1103), a second retail market (S02-SH-1105), and a market within a market within the market European Union (S02-SH-1107, S02-SH-1108) each showed 'Active', and the markets list held the four B2B and retail markets at once (S02-SH-1106); S02-SH-G16 adds that no step of the run showed a limit or upgrade message. These statements show how many markets one store held, not a limit or a rule, which is what an answer to `what limits "market"` names (rule 1), so they are placed under S02-VP-26, or noted, and S02-SH-G16 stands as shopify's `gap` row. If a count one store held, with its scope, counts as an answer to how many a store can hold, S02-SH-1102 to S02-SH-1106 give S02-VP-27 an answer row for that store and plan (two B2B and two retail markets, each Active, at once), beside the gap. The coordinator decides.
- S02-SH-1113 shows no 'POS locations' among fake-demo-sharrwah's condition types, where S02-SH-1101 and S02-SH-1094 show it on demo-fake-dev-store and capture-us-plus. That a store whose menu lacks the item can't hold a retail market would be an inference, so S02-SH-1113 joined only the rows of the items it shows, and isn't placed under S02-VP-27. S02-SH-G16 pairs it with S02-SH-1114 (RequestDetails, retail enabled false), which is outside RD2's slice.
- S02-SH-1092, S02-SH-1094 and S02-SH-1095 were in RD2's slice under (e) with no task in RD2's work list (above), which was written before the slice was cut again. They are placed here.
- `place` tasks have no `done` line, as RD2-S2 read the brief: `second_pass_list.py --check` lists only revisit, reread and note tasks. The revisit's `done` line is S02-V-483's first.

### RD2-S3: row notes added

- S02-V-425: its note now says that S02-SH-1116 shows the New market page on fake-demo-sharrwah (Advanced, paid, 27 October 2026), beside the earlier note's S02-SH-386 (the control 'Create market', listed without that store) and S02-SH-387 ('Request access' on it). No cause is given; each statement's scope gives its own store and plan.

## Second pass, RD2-S4: the Salla and Zid round's tasks of RD2's work list (after A2-SA-R at observed-sa b0bd0b16, and A2-ZD-R and A3-ZD-R at other-product-class f44be3f), bullet (e); salla and zid

Most statements of this round are observations of one store on one day, 28 October 2026: salla's public demo (giftshop2024, badge Special) and demo store (store-sherawya, Pro); zid's demo store 127604 (Zid Demo Store, plan new_professional.yearly) and development store 3277610 (Capture Dev Store, plan new_professional.lifetime), both with zid's feature flag `must_use_markets_pricing` false. Each row they joined took its `kind` and `scope` again from all its statements (rule 6), and each `basis_evidence` added names the store, its plan where the statement gives it, and the run and step: a run says what one store showed, not what every store does.

### Revisits

- S02-V-442 (zid, S02-VP-26, was `gap` S02-ZD-G06). RD2's work list names no gap or absence left for it: gap-closing settled S02-ZD-G06. Its leads give no answer zid's rows don't hold, so they joined S02-V-440 and the row is removed:
  - S02-ZD-471, the record of the primary market 'Main Market' (السوق الرئيسي) of the development store 3277610 ('"is_primary": true, "is_published": true, "countries": ["SA"]', run 20261028T170107Z-devstore-markets-en, steps 3 and 57, the second after the store's country was changed to Kuwait), joined S02-V-440: a market's record holds its countries. Its words name 'Main Market', not السوق الافتراضي (S02-ZD-012, S02-V-441), and zid's terms hold السوق الرئيسي and السوق الافتراضي as separate terms, so it doesn't join S02-V-441 (rule 0). S02-V-441 has a row note saying so.
  - S02-ZD-472, the answer of POST /v1/markets for the market Kuwait on the same store ('"countries": ["KW"]', run 20261028T185150Z-devstore-tracking-apps-en, step 2), joined S02-V-440. Its words name no party, so it isn't placed under S02-VP-28.
- S02-V-447 (zid, S02-VP-29, was `gap` S02-ZD-G05). RD2's work list names no gap or absence left for it: gap-closing settled S02-ZD-G05. Its leads give two answers no row held, and one under S02-VP-28:
  - S02-ZD-473, the dialog of 'More > Remove market' on settings/markets ('Remove Kuwait This market will be permanently deleted. This action cannot be undone. Cancel Remove'), development store 3277610, run 20261028T170107Z-devstore-markets-en, step 44: a control in the store's admin, so the seller removes a market (rule 4). It replaces S02-V-447.
  - S02-ZD-461, the store permission '"slug": "markets.delete", "name": "Delete markets"' on the demo store 127604 (run 20261028T144855Z-dashboard-routes-en, step 1): a staff permission that gates deleting a market, its own answer by rule 4, the new row S02-V-486.
  - S02-ZD-460, the store permission '"slug": "markets.create", "name": "Create markets"' on the same store and step: a staff permission that gates creating a market, placed under S02-VP-28 as the new row S02-V-487. It names 'markets.edit' only among the permissions markets.create relies on ('"relies_on": ["markets.view", "markets.edit", "markets.products.edit"]'), not what markets.edit gates, so it isn't placed under S02-VP-29.

### Statements noted under (e)

- S02-SA-528 (e): 'Manage every market Run all your markets from one dashboard with independent settings for each market. Set market-specific pricing Adjust product prices to match each market and currency.': a market's settings and its prices, under (f); states no definer, limit or party for a market, as S02-SA-065, the same sentence, is noted above
- S02-SA-529 (e): 'Customize each market Tailor your store’s design and content to connect with local customers.', 'Choose the sign-in methods available to customers in each market.' and 'Control which products are available in each market based on customer demand.': a market's settings (its design and content, sign-in methods, products), under (f); states no definer, limit or party for a market

### Statements placed (`place` tasks)

salla (the runs of 28 October on the public demo, giftshop2024, badge Special, and the demo store, store-sherawya, Pro):
- S02-SA-517 (Settings > Markets, the public demo, run 20261028T153241Z-journey-markets-public-demo-en, step 4): 'Start creating new markets and selling in multiple countries.', the words of S02-SA-053, joined S02-V-438 under S02-VP-28 (the seller creates a market), where S02-SA-053 stands. 'selling in multiple countries' names where the store sells, not what a market is, so it isn't placed under S02-VP-26, as S02-SA-053 isn't.
- S02-SA-518 (Settings > Markets, the demo store, run 20261028T154256Z-journey-markets-demo-store-en, step 3): the same words with the control 'Activate', joined S02-V-438, and S02-V-439 under S02-VP-29, as S02-SA-026's control 'فعل الآن' stands in both (the seller's controls switch the multiple markets feature on).
- S02-SA-527 (Products > Multi Market, the public demo, step 5): the control 'Create your first market', joined S02-V-438. 'Sell across countries and markets' states no definer, so it isn't placed under S02-VP-26.
- S02-SA-530 (/localization/journey, 'Default market', step 17): 'Create your first market and choose the countries and settings that best fit your customers.', the words of S02-SA-061, with 'Countries Saudi Arabia' and the control 'Create market', joined S02-V-431 under S02-VP-26 (countries define a market) and S02-V-438, where S02-SA-061 stands.
- S02-SA-531 (the default market's countries field, step 7): 'Select countries [Search] Saudi Arabia United Arab Emirates Kuwait Qatar Bahrain Oman Egypt United Kingdom United States', joined S02-V-431.
- S02-SA-532 (the dialog after 'Create market', run 20261028T155312Z-journey-markets-public-demo-en, step 29): 'Confirm activating this feature', joined S02-V-438 and S02-V-439, as S02-SA-026's 'اضغط (تأكيد)'; 'Once enabled, it cannot be disabled except by contacting the Account Manager.', joined S02-V-473 under S02-VP-29 (the account manager), with S02-SA-055 and S02-SA-059.
- S02-SA-533 (the write the 'Confirm' sent, POST api.salla.dev/admin/v2/multi-countries/activate, the same run): its body's 'countries' joined S02-V-431; the write on the seller's 'Confirm' joined S02-V-438 and S02-V-439, as S02-SA-532.
- S02-SA-534 (the write's 422 answer, the same run): 'The multi-country feature was previously deactivated. To reactivate it, please contact support.' Two new rows, each its own answer by rule 4, as S02-SA-054 ('Contact your account manager to enable this feature.') stands in S02-V-472 and S02-V-473: S02-V-488 under S02-VP-28 and S02-V-489 under S02-VP-29, 'To reactivate it, please contact support.' (support, a party the statement names). That the multi-country feature is the multiple markets feature is a reading, marked in both rows.

zid (the runs and structures of 28 October on the demo store 127604 and the development store 3277610, and zid's changelog):
- S02-ZD-485 (the subscription policies of the demo store 127604, plan new_professional.yearly, run 20261028T144855Z-dashboard-routes-en, step 1): '"key": "markets_management.active_markets", "enabled": true, "config": {"limit": 5}', the key and limit of S02-ZD-151, joined S02-V-445 under S02-VP-27.
- S02-ZD-487 (the Kuwait market's manage page on the development store 3277610, run 20261028T170107Z-devstore-markets-en, step 12): 'Countries Kuwait [Select countries]' joined S02-V-440 under S02-VP-26; the page's controls ('Save', 'Market name (Arabic)', 'Countries', 'Market currency', 'Show market Publish market') joined S02-V-447 under S02-VP-29 (the seller changes a market). It shows no control that creates a market, so it isn't placed under S02-VP-28.
- S02-ZD-488 (the dashboard's code, the save of route settings/markets/:id/manage): 'country_codes:r' joined S02-V-440; the save joined S02-V-447, read as the save of the seller's changes on S02-ZD-487's page (a reading, marked in the row: the code's words name no party; see "Problems").
- S02-ZD-492 (the dashboard's message common:upgrade.marketLimitReached): 'You have reached the maximum number of markets allowed in your package.', joined S02-V-444 under S02-VP-27 (the plan limits how many markets a store holds).
- S02-ZD-494 (zid's changelog, changelog.zid.sa/ar, its entry 'المنتجات ١٨, ١٠, ٢٠٢٦'): 'ويبدأ متجرك بسوق رئيسي تلقائيًا' (my translation: and your store starts with a main market automatically) is the new row S02-V-490 under S02-VP-28 (the platform, by 'تلقائيًا', automatically: rule 4); 'وتقدر تضيف أسواق أخرى حسب باقتك' (my translation: and you can add other markets according to your plan) joined S02-V-446 under S02-VP-28 (the seller) and S02-V-444 under S02-VP-27 (the plan). 'سوق رئيسي' names a market, not what defines it, so it isn't placed under S02-VP-26.

### RD2-S4: rows replaced or removed

- S02-V-442 (zid, S02-VP-26): `gap` S02-ZD-G06, removed; its leads S02-ZD-471 and S02-ZD-472 joined S02-V-440. Gap-closing settled S02-ZD-G06: the work list names no gap or absence for the point.
- S02-V-447 (zid, S02-VP-29): `gap` S02-ZD-G05, replaced by the answer 'Remove Kuwait This market will be permanently deleted.' (S02-ZD-473, the seller); S02-V-486 ('"slug": "markets.delete", "name": "Delete markets"', S02-ZD-461) added beside it. Gap-closing settled S02-ZD-G05: the work list names no gap or absence for the point.
- New rows: S02-V-486 and S02-V-489 (S02-VP-29), S02-V-487, S02-V-488 and S02-V-490 (S02-VP-28).

### RD2-S4: rows `not covered`

None. Salla and zid have no `gap`, `absent` or `not covered` row left under RD2's points.

### RD2-S4: matching (rule 5)

The `raised_by` of S02-VP-26 (S02-SH-077, S02-SH-065, S02-SH-279), S02-VP-27 (S02-SH-111, S02-SH-301, S02-SH-286), S02-VP-28 (S02-SH-115, S02-SH-116, S02-SH-288) and S02-VP-29 (S02-SH-061, S02-SH-128, S02-SH-288) hold only shopify's statements. The new rows share no term, identifier or definition with them: S02-V-486 and S02-V-487 name zid's own permission slugs, where S02-SH-288 names the error code 'USER_LACKS_PERMISSION'; S02-V-490 says what S02-SH-116 says ('created for you automatically'), with no term of `terms.tsv` in common; S02-V-488 and S02-V-489 name support, whom no raised_by statement names. Each takes `answers` alone. Statements joined to rows of their own platform were compared with those rows' statements: S02-SA-517 and S02-SA-518 with S02-SA-053 (the same words), S02-SA-530 with S02-SA-061 (the same words), S02-ZD-485 with S02-ZD-151 (the same key, 'markets_management.active_markets'); rechecked, the rows joined (S02-V-431, S02-V-438, S02-V-439, S02-V-440, S02-V-444, S02-V-445, S02-V-446, S02-V-447, S02-V-473) keep `answers`, since rule 5's other bases compare with another platform's statement.

### RD2-S4: new kinds, searches and x_words

- New kinds: none; (e)'s points take no kind (rule 3).
- Searches for earlier platforms' rows: none; the second pass raised no point.
- x_words added for zid: 'market' (S02-VP-26: 'Market details', S02-ZD-487); 'markets; أسواق' (S02-VP-27: S02-ZD-492, S02-ZD-494); 'markets; أسواق; سوق رئيسي' (S02-VP-28: 'Create markets', S02-ZD-460; S02-ZD-494); 'market; markets' (S02-VP-29: 'Remove market', S02-ZD-473; 'Delete markets', S02-ZD-461). None for salla: its statements call X 'market', as salla's x_words already hold it.

### Candidates for a new point (RD2-S4)

None. Every statement of these tasks that answers one of (e)'s questions does so for salla's or zid's market, a market a store sells into, the one X of (e)'s points. Salla's 'multi-country feature' (S02-SA-534) and 'this feature' (S02-SA-532) are the feature that holds the markets, as S02-SA-054's 'this feature' is in S02-V-472, not another X.

### RD2-S4: row notes added

- S02-V-441: its note now says that S02-V-442, the gap row its evidence names (S02-ZD-G06), is removed, that its leads joined S02-V-440, and why S02-ZD-471 doesn't join S02-V-441 (rule 0).

### RD2-S4: problems with the method

- RD2's slice was cut again during this part (its `statements.tsv` at 22:46 on 28 October, after the work list at 22:38). S02-ZD-492 printed kind 'unknown' before and 'shipped' after; every row of this part was written after the new cut, so its rows take the new kinds. No other statement of these tasks changed its kind, bullets or scope.
- S02-ZD-488 joined S02-V-447 (the seller changes a market) on its identifier, the save of the admin's route settings/markets/:id/manage, whose page S02-ZD-487 shows with its 'Save'; the code's own words name no party, and the row marks this as a reading. If code that names no party can't answer `who changes or removes "market"` through its route, S02-ZD-488 leaves S02-V-447 and stays in S02-V-440.
- S02-SA-518 ('Activate'), S02-SA-532 ('Confirm activating this feature') and S02-SA-533 (the write on 'Confirm') joined S02-V-439 under S02-VP-29, and S02-SA-534 ('To reactivate it, please contact support.') made S02-V-489 there, as S02-SA-026 (the seller's controls that switch the feature on) and S02-SA-054 ('Contact your account manager to enable this feature.') stand under S02-VP-29 beside S02-VP-28 (rule 4, as widened on 27 October 2026). If switching the multiple markets feature on isn't a change of a market, they leave S02-V-439, and S02-V-489 goes, with S02-SA-534 staying in S02-V-488.
- S02-ZD-G06 asked what the default market (السوق الافتراضي, S02-ZD-012) holds. The work list names no gap left, and the leads show the primary market 'Main Market' (السوق الرئيسي) and its countries (S02-ZD-471); S02-ZD-494 says the store starts with a main market (سوق رئيسي) automatically. Zid's terms hold السوق الرئيسي and السوق الافتراضي as separate terms, so S02-ZD-471 joined S02-V-440 only, and S02-V-446's note (S02-ZD-012 doesn't say who creates the default market) stands beside the new row S02-V-490. If the two terms name one market, S02-ZD-471 joins S02-V-441 too. The coordinator decides.
- Salla's `a2.tsv` names S02-SA-517, S02-SA-518, S02-SA-527, S02-SA-528 and S02-SA-529 for S02-VP-26, and S02-SA-530 for S02-VP-27, as leads. Their words state no definer of a market ('selling in multiple countries', 'Sell across countries and markets'), or, for S02-SA-530, no limit: its marks 'Market name *' and 'Market branches and warehouses *' would be a rule on what a market must hold only as a reading of the asterisks. So they aren't placed under those points.
- `place` tasks have no `done` line, as RD2-S2 and RD2-S3 read the brief: `second_pass_list.py --check` lists only revisit, reread and note tasks. Both revisits have their `done` lines.

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

## Second pass, RD3-S5: bigcommerce, bullets f and g

BigCommerce's tasks in `b/second-pass/RD3/worklist.tsv`: ten revisits, then the `place` tasks. Each row is compared with the statement in its point's `raised_by` from another platform (rule 5); every new row takes `answers`. A market is read as the first pass read it (BigCommerce's 'channel', a storefront among its types, `terms.tsv`); a storefront that takes the store's global value until the seller changes it takes its value per a market (rule 4).

### Revisits: rows replaced, and what took their place

- S02-V-842 (S02-VP-63, was `not covered`): replaced by S02-BC-351, 'while remaining merchant of record', the whole store, a reading of 'remaining' as the merchant staying merchant of record in AI-powered shopping experiences as in its other sales; S02-V-961 added beside it, `gap` S02-BC-G14, which asks whether a market can sell through another entity.
- S02-V-843 (S02-VP-64, was `not covered`): replaced by `gap` S02-BC-G14. S02-BC-351 names who the merchant of record is in agentic checkout, not who sets it; it is placed under S02-VP-63.
- S02-V-844 (S02-VP-65, was `not covered`): replaced by a market, 'the default values for return reasons and actions will be automatically translated per storefront' (S02-BC-339, S02-BC-341); added S02-V-962, the whole store ('You can click to enable returns for your store.', S02-BC-339, with S02-BC-335, S02-BC-340, S02-BC-341 as readings), and S02-V-963, `gap` S02-BC-G13.
- S02-V-845 (S02-VP-66, was `not covered`): replaced by the seller, Settings › Returns in the control panel (S02-BC-330 to S02-BC-335, S02-BC-337, S02-BC-339, S02-BC-340); added S02-V-964, the platform ('will be automatically translated per storefront', S02-BC-339, S02-BC-341, S02-BC-335), and S02-V-965, the Manage Settings permission (S02-BC-336).
- S02-V-850 (S02-VP-69, was `gap` S02-BC-G03): replaced by a market, 'translations by resourceType, channel, and locale' (S02-BC-296, S02-BC-297, S02-BC-300); S02-V-966 added, `gap` S02-BC-G12 (S02-BC-G03 was settled by gap-closing, and goes). S02-BC-301 and S02-BC-302 joined the buyer's country (S02-V-848). Under S02-VP-70: S02-BC-301 and S02-BC-303 joined the seller (S02-V-851), S02-BC-300 the platform (S02-V-852), and S02-V-967 added, the Manage Settings permission (S02-BC-304). The leads placed under other points they answer: S02-BC-296 to S02-BC-300 joined S02-V-815 (S02-VP-43, translated content per channel and locale); S02-V-968 added under S02-VP-44, the platform (S02-BC-300, Country/State names translated within the platform); S02-BC-305 to S02-BC-307 joined S02-V-830 (S02-VP-55, a market); S02-BC-306 joined S02-V-831 (S02-VP-56, the seller); S02-V-969 added under S02-VP-56, the platform ('By default, your storefront uses your store’s checkout settings.', S02-BC-306); S02-V-970 added under S02-VP-56, the Manage Settings permission (S02-BC-304).
- S02-V-854 (S02-VP-71, was `not covered`): replaced by the whole store, a reading of a policy's targets, 'a specific store, or the account itself', none of them a channel or storefront (S02-BC-345, S02-BC-342).
- S02-V-855 (S02-VP-72, was `not covered`): replaced by the seller, 'To edit user permissions, go to Settings › Users' (S02-BC-348); added S02-V-971, the store owner (S02-BC-348, the account's owner, rule 4); S02-V-972, the Manage Users and Edit Users permissions (S02-BC-348); S02-V-973, the platform (S02-BC-346's default group 'provisioned with each account'; S02-BC-344's 'Predefined permission bundles', a reading).
- S02-V-856 (S02-VP-73, was `not covered`): replaced by a market, the Allow global logins setting of each channel, which sets the storefronts a customer may shop (S02-BC-327 to S02-BC-329). The same three joined S02-V-830 (S02-VP-55, customer accounts' sign-in per storefront), S02-BC-328 and S02-BC-329 joined S02-V-831 (the seller), and S02-BC-327 and S02-BC-329 joined S02-V-969 (the platform, 'default behavior'). S02-BC-322 is a currency converter, not a choice of market: it joined S02-V-810 (S02-VP-41, the buyer's country), S02-V-813 (S02-VP-42, the platform: 'automatically') and S02-V-812 (the seller: 'the currencies you have set up'), and S02-V-976 was added under S02-VP-42, the buyer ('allow customers to choose among the currencies you have set up').
- S02-V-857 (S02-VP-74, was `not covered`): replaced by the seller, 'You can add a selector to a theme' (S02-BC-323 to S02-BC-326, S02-BC-328, S02-BC-329); added S02-V-974, the buyer (S02-BC-323, S02-BC-326), and S02-V-975, the platform (S02-BC-327, S02-BC-329). S02-BC-323 to S02-BC-326 give no answer under S02-VP-73: they say who adds and uses the storefront selector, not what the buyer's market is taken per.
- S02-V-862 (S02-VP-79, was `not covered`): replaced by the seller, 'Go to Settings › Store profile to update or change your store's contact information.' (S02-BC-308 to S02-BC-313, S02-BC-315 to S02-BC-321); added S02-V-977, the platform (S02-BC-316's 'By default', S02-BC-317's fallback, a reading). S02-BC-307, S02-BC-308 to S02-BC-316, S02-BC-320 and S02-BC-321 joined S02-V-847 (S02-VP-68, a market). The leads placed under other points they answer: S02-BC-314 joined S02-V-863 (store status), S02-V-827 (storefront design: 'logo and favicon') and S02-V-846 (locations: 'inventory rules'); S02-BC-321 joined S02-V-863 and S02-V-864 (store status), S02-V-858 and S02-V-867 (privacy and consent: 'customer privacy'), S02-V-820 and S02-V-821 (products: 'search settings', as the first pass read them); S02-BC-319 and S02-BC-320 joined S02-V-866 (messages to buyers, the seller), and S02-BC-320 joined S02-V-865 (a market: 'specify a store email address per storefront').

### Statements noted (rule 2)

- S02-BC-343 (f): defines user groups ('Named, reusable bundles of access'); names neither what staff access takes its value per nor who sets it
- S02-BC-347 (f): says each of a store's users 'should have their own account, with permissions limited to only their areas of responsibility'; names neither what staff access takes its value per (a market, a buyer's country, the whole store) nor who sets it
- S02-BC-349 (f): names a staff permission, Create Channels ('Add channels in the Channel Manager'), which gates creating a channel, RD2's question of who creates a market; names neither what staff access takes its value per nor who sets it
- S02-BC-350 (f): names a staff permission, Delete Channels ('Delete channels from the Channel Manager'), which gates removing a channel, RD2's question; names neither what staff access takes its value per nor who sets it
- S02-BC-184 (f): the format of the Carts API's locale field ('supports language, script, and region codes in the ISO-639 standard format'); names neither what a setting takes its value per nor who sets it
- S02-BC-186 (f): the lead-in of the channel settings webhooks ('The following settings webhook events fire in response to actions that affect a specific channel on a store'): settings in general, of no one kind of setting, as RD3-3 noted S02-BC-097 to S02-BC-102
- S02-BC-215 (f): 'Returns metadata about the global settings for a store. Some of these values are independently configurable on a per-storefront or per-channel basis.': the store's settings in general, of no one kind of setting

### `place` tasks: where the statements went

- S02-BC-163, S02-BC-164, S02-BC-171, S02-BC-172, S02-BC-174 (Catalyst's multi-storefront overview): language, currency, domain and payment methods per channel, joined to S02-V-815, S02-V-809, S02-V-818, S02-V-840 (a market); S02-BC-172 and S02-BC-173 to S02-V-819 (the seller, domains), S02-BC-172 to S02-V-817, S02-V-812, S02-V-841 (the seller: 'where you want to personalize the language, currency, payment methods'); S02-BC-174 and S02-BC-175 to S02-V-857 (the seller, market selection: 'mapping locales to BigCommerce channels').
- S02-BC-165 ('manage localization settings and content for each storefront'): its localization settings joined S02-V-860 (units) and S02-V-871 (the store's country), a market.
- S02-BC-166 to S02-BC-170, runs of one list ('The storefront content to localize includes the following'), read with S02-BC-165, of the same page, as content set per storefront: products and categories (S02-V-820), currency (S02-V-809), pricing via price lists (S02-V-822), date and physical dimension formats (S02-V-860), checkout (S02-V-830), promotions (S02-V-825), emails (S02-V-865), payment methods (S02-V-840), shipping options (S02-V-836), tax settings (S02-V-833).
- S02-BC-175 (catalog and pricing 'assigned to storefront channels'): S02-V-820, S02-V-822 (a market), S02-V-821, S02-V-824 (the seller).
- S02-BC-176, under (f) and (g) ('Other features, like tax, belong to the global store and require that you create zones, or regions, where you want tax rules to apply'): S02-V-978 added under S02-VP-57, the whole store, `answers` alone; joined S02-V-832 (the buyer's country, tax zones as the first pass read them) and S02-V-834 (the seller).
- S02-BC-179, S02-BC-183, S02-BC-189, S02-BC-190, S02-BC-286 (locales per storefront or channel): S02-V-815 (a market); S02-BC-179, S02-BC-183, S02-BC-286 also S02-V-817 (the seller).
- S02-BC-180 (US and Swiss products per channel): S02-V-820, S02-V-821.
- S02-BC-181 ('Currencies must be **Visible** on the storefront in the global settings'): S02-V-811 (the whole store). S02-BC-182, S02-BC-187, S02-BC-245 (currency per channel): S02-V-809; S02-BC-182 and S02-BC-245 also S02-V-812 (the seller).
- S02-BC-185, under (g) ('you cannot have different warehouse locations and inventory service different storefront channels'): S02-V-979 added under S02-VP-67, the whole store, `answers` alone.
- S02-BC-188, S02-BC-209, S02-BC-259 (the store profile, global or per channel): S02-V-847 (a market, contact information); S02-BC-209 and S02-BC-259 also S02-V-862 (the seller).
- S02-BC-191 to S02-BC-204 (the channel settings webhooks, 'that affect the specified channel', read as the first pass read S02-BC-043): logo, favicon, SEO and robots under storefront design (S02-V-827); checkout and customer settings (S02-V-830); search, category, product, catalog settings and search context filters under products (S02-V-820); inventory under locations (S02-V-846); security and privacy settings under privacy and consent (S02-V-858).
- S02-BC-224 (Stripe Adaptive Pricing: 'shoppers can complete orders in their local currency'): S02-V-810 (the buyer's country) and S02-V-814 (Stripe).
- S02-BC-246, S02-BC-248 (tax by the countries and subdivisions targeted, and price display per tax zone): S02-V-832 (the buyer's country), S02-V-834 (the seller); S02-V-980 added under S02-VP-58, the automatic tax provider ('you want the provider to calculate tax for').
- S02-BC-253 ('The default country setting determines which payment methods are available to be set up on your store'): S02-V-839 (the store's own country, a reading of the default country); with S02-BC-285, S02-V-983 added under S02-VP-77, the store's own country ('the standard formats for your store’s default country').
- S02-BC-255: S02-V-981 added under S02-VP-44, the Manage Settings permission ('To view and manage languages').
- S02-BC-256, S02-BC-257 (localization settings per channel): S02-V-860 and S02-V-871 (a market).
- S02-BC-268: S02-V-982 added under S02-VP-54, the Edit Channels and Store Design permissions that gate the Theme Marketplace and Edit Theme Files.
- S02-BC-287 (PayPal translates its payment methods by the shopper's location): S02-V-986 added under S02-VP-43 (the buyer's country); S02-V-838 (the buyer's country, payment methods); S02-V-968 (the platform, S02-VP-44); S02-V-987 added under S02-VP-44 and S02-V-989 under S02-VP-62 (PayPal); S02-V-988 added under S02-VP-62 (the platform: 'automatically translated by BigCommerce').
- S02-BC-288 to S02-BC-291 (a new store's content in the native language of the country it is based in, and the list of those languages, read together as one list): S02-V-985 added under S02-VP-43, the store's own country; S02-BC-288 also S02-V-968 (the platform: 'by default').
- S02-BC-292, under (g) ('settings like measurement units and factoring dimension are applied globally', answering whether they apply per product): S02-V-984 added under S02-VP-77, the whole store, `answers` alone. S02-V-860 holds S02-BC-256's 'configure ... physical dimensions ... separately per channel': both are rows.
- S02-BC-295 (invoice email templates per storefront, or 'Global (storefront defaults)'): S02-V-865 (a market), S02-V-866 (the seller).

### Candidates not placed

Each of these statements is placed under another point; these candidates are not:
- S02-BC-168's 'Order statuses', among the storefront content to localize: of none of rule 1's kinds, and the second pass raises no point.
- S02-BC-165's 'content': settings in general.
- S02-BC-224's 'payouts to your account are settled in your default currency': payouts, (c)'s kind, not a setting under (f), as RD3-1 and RD3-3 read payouts.
- S02-BC-257's Edit Channels permission for a channel's localization settings: S02-VP-77 and S02-VP-85 ask only what the value is taken per, and no point asks who sets units or the store's country.
- S02-BC-246's 'Basic Tax is then used for all regions that are not targeted by the provider', S02-BC-288's 'All other countries and languages require theme lang file customization', S02-BC-302's 'UK customers must manually enter their postcode': they name no party that sets the setting.
- S02-BC-323's 'multiple storefronts that target specific shopper segments, regions, or brands': RD2's question.

### Words searched for

None: the second pass raises no point, so no search for earlier platforms' rows was run.

### Problems with the brief or the tools

- **`done` prints nothing.** `method/variants_edit.py ... done` writes its row to `b/RD3/done.tsv` and prints nothing; the rows were checked in the file.
- **Joins to a row with `term`.** S02-BC-176 is under (f) and (g); joined to S02-V-832 and S02-V-834 for its (f) half, rows that take `answers;term`. Its (g) half is S02-V-978, `answers` alone.
- **S02-BC-322 among S02-VP-73's leads.** It is a currency converter by the visitor's IP address; BigCommerce's market is a channel, so it is placed under currency, not market selection.
- **Leads placed under several points.** The revisits placed leads under every point they answer, as rule 2 asks, so some rows of points without a task changed by a join or gained a row (listed above); no row was replaced or removed outside a revisit.

## Second pass, RD3-S1: shopify, bullets f and g

Shopify's tasks in `b/second-pass/RD3/worklist.tsv`: eleven revisits, then the `place` tasks, then the rereads. A market is read as RD3-1 read it ('a set of customers that you define in your store', `terms.tsv`, with its types). Every new row takes `answers`: rows are compared with a statement of another platform in the point's `raised_by` where there is one (rule 5), and no term, identifier or definition is shared with it unless said.

### Revisit S02-V-662 (S02-VP-69, was `gap` S02-SH-G04)

- Replaced by `gap` S02-SH-G06, the gap `why` names; S02-SH-G04 was settled by gap-closing, and goes. Every answer the leads give under S02-VP-69 is one Shopify's rows hold: S02-SH-653, S02-SH-656, S02-SH-658, S02-SH-659, S02-SH-661, S02-SH-663, S02-SH-664 joined S02-V-660 (the buyer's country); S02-SH-653, under (f) and (g), joined S02-V-661 (the whole store, its (g) half).
- Under S02-VP-70: S02-SH-652 and S02-SH-658 joined S02-V-663 (the seller; S02-SH-652 a reading of its identifier, 'Editing the checkout form options'); S02-SH-653 and S02-SH-656 joined S02-V-664 (the platform; S02-SH-656's 'always active on your store' a reading); S02-V-990 added, no one (S02-SH-653: 'depends on the customer's country or region and can't be changed'); S02-V-991 added, Managed Markets (S02-SH-657: 'Managed Markets checks whether the address that your customer adds during checkout is valid', a reading of checking as applying the validation; scope Managed Markets).
- S02-SH-665 to S02-SH-687 are runs of one list: the address service's answer to the admin's Edit business details page, by their scope. The form they format is the store's address, not the buyer's, so under S02-VP-69 their X fails the role test; they joined S02-V-674 (S02-VP-76, the store's own country), the answer RD3-1 gave from the same page's captured forms.
- The additional tax fields (S02-SH-648 to S02-SH-651, S02-SH-654) are fields of checkout 'grouped with the payment details in a section titled Additional Information', not of the address form: they are placed under checkout (S02-VP-55, S02-VP-56). S02-V-992 added, the buyer's country (S02-SH-648, S02-SH-650, S02-SH-651; S02-SH-654's 'vary checkout fields by country' a reading of whose country); S02-V-993, the store's own country (S02-SH-650: 'Italy Destination is Italy, shop billing country is Italy', the store's billing address by rule 1); S02-V-994, the whole store (S02-SH-653 (g), 'the Customer information settings apply to every country and market that you sell to', and S02-SH-649, 'activated or deactivated for all applicable countries and regions together'); S02-SH-652 joined S02-V-632 (the seller, a reading of its identifier); S02-V-995 added, the platform (S02-SH-649: 'activated by default for all stores', changed through Shopify Support; S02-SH-651); S02-V-996, an app (S02-SH-654: 'you need an app that customizes the information, shipping, and payment pages of checkout').
- S02-SH-655 (the Marketing opt-in section): S02-V-997 added under S02-VP-75, the buyer's country ('which customer regions have the email marketing consent checkbox preselected'); joined S02-V-747 (S02-VP-84, the seller: 'You can manually choose the customer regions'); S02-V-998 added under S02-VP-84, the platform ('chosen based on the latest recommendations from Shopify. These automatic recommendations').

Statements noted (rule 2):
- S02-SH-647 (f): names the cases in which additional address fields aren't available or required (accelerated checkout such as PayPal, renamed labels, apps that read or edit addresses); names neither what the address form's value is taken per nor who sets it
- S02-SH-660 (f): says how the platform parses and merges the additional fields' data (the library Worldwide); names neither what the address form's value is taken per nor who sets it
- S02-SH-662 (f): lists the modes an address form field takes ('IGNORED', 'OPTIONAL', 'REQUIRED'); names neither what a field's mode is taken per nor who sets it
- S02-SH-688 (f): the address service's answer to a buyer checkout lists each country's name, code and phone prefix only; it shows no address field, format or validation per country, nor who sets one

### Revisit S02-V-733 (S02-VP-78, was `not covered`)

- Replaced by the seller, 'You can add, deactivate, reactivate, and delete your locations from the Locations settings in your Shopify admin' (S02-SH-844, S02-SH-845, S02-SH-847, S02-SH-848, S02-SH-850, S02-SH-853, S02-SH-860, S02-SH-861, S02-SH-862, S02-SH-905 to S02-SH-907, S02-SH-938, S02-SH-943); added S02-V-1002, the platform ('activated by default for each new location', S02-SH-847, S02-SH-848, S02-SH-850, S02-SH-851), and S02-V-1003, third-party fulfillment service apps ('can create and manage their own locations', S02-SH-910, S02-SH-913). Compared with S02-SA-033 in `raised_by`: Shopify's 'location' (الموقع, `terms.tsv`) is not Salla's الفروع, so `answers` alone.
- Under S02-VP-67: S02-SH-850 to S02-SH-852 joined S02-V-657 (a market: 'Locations within the same market as the shipping address are prioritized'); S02-V-1004 added, the whole store, a reading of the store's one default location (S02-SH-862).
- Leads placed under the other points they answer: S02-SH-920 joined S02-V-603 (the whole store: POS 'transactions process in your store’s default currency', scope one business entity), S02-V-614 and S02-V-620 (a market: 'Retail markets still control catalog and price rules'); S02-SH-924 joined S02-V-614, S02-V-620, S02-V-618, S02-V-622 ('You assign catalogs to a Region market'); S02-SH-921 joined S02-V-600 and S02-V-649 (a market: 'The entity assigned to each retail location determines the currency', read with Shopify's term 'Retail markets use POS locations as their condition'); S02-SH-934 joined S02-V-600 and S02-V-604 ('You can configure the currency used at checkout with Retail markets'); S02-SH-935 joined S02-V-602 (the store's own country: 'depending on your store's location') and S02-V-605 (the platform: 'apply automatically'); S02-SH-926 joined S02-V-639, S02-V-642, S02-V-643; S02-SH-927 joined S02-V-639; S02-SH-938 joined S02-V-642; S02-SH-939 joined S02-V-640 and S02-V-642; S02-SH-940 and S02-SH-941 joined S02-V-633 and S02-V-635 (duties, by market). S02-SH-893 is placed in the revisit of S02-V-735 (contact details), and S02-SH-942 in the revisit of S02-V-745 (messages to buyers).

Statements noted (rule 2):
- S02-SH-846 (f): says which apps are treated as locations; names neither what locations take their value per nor who sets them
- S02-SH-854 (f): the POS subscription plan chosen per location by the account owner is the platform's fees, a setting of the platform's account, not of the store (rule 1)
- S02-SH-855 (f): a rule the merchant must follow by the country a POS transaction is processed in; names no setting of the store and who sets it
- S02-SH-908 (f): shows one location's POS devices, subscription and staff; names neither what locations take their value per nor who sets them
- S02-SH-909 (f): defines a location ('A physical location where merchants store and fulfill inventory'); names neither what locations take their value per nor who sets them
- S02-SH-911 (f): the API mutation that adds a location names no party that adds it (rule 4: an API alone names no party); its 'you' is who stocks inventory
- S02-SH-912 (f): what a location must hold ('a name and address with at least a country code'); names neither what locations take their value per nor who sets them
- S02-SH-923 (f): a requirement on the payout currency of a location's entity: payouts, (c)'s kind, not a setting under (f)
- S02-SH-925 (f): names market settings in general ('different market settings to retail and online customers'), of no one kind of setting
- S02-SH-928 (f): a legal requirement on which entity processes a POS return in five countries; names no setting's value per market and no party that sets it (rule 4: a party that requires a value isn't who sets it)
- S02-SH-929 (f): what POS receipts include by the country or province of a location, a place the store sells at (rule 1), none of the four phrases; names no party that sets it
- S02-SH-930 (f): a restriction by the country of a retail location (Spain), a place the store sells at (rule 1), none of the four phrases; its 'You can't sell' names only who is kept out
- S02-SH-931 (f): where the merchant's obligation to collect tax starts (its default location, where it operates from), RD1's (c); names no setting's value per market and no party that sets one
- S02-SH-932 (f): what buying the platform's shipping labels requires (an eligible fulfillment location, the store based in the same country): a service of the platform, (c)'s kind, not a setting under (f)
- S02-SH-933 (f): as S02-SH-932, for Evri and DPD labels: a service of the platform, (c)'s kind, not a setting under (f)
- S02-SH-936 (f): when additional cash rounding rules apply (by when the store was created, or its first retail location in a listed country, a place the store sells at): none of the four phrases; names no party that sets them

### Revisit S02-V-735 (S02-VP-79, was `not covered`)

- Replaced by the seller, 'You can update your store's name, email address, and phone number' (S02-SH-809 to S02-SH-815, S02-SH-817, S02-SH-821 to S02-SH-823, S02-SH-825 to S02-SH-827, S02-SH-829, S02-SH-830, S02-SH-832, S02-SH-833, S02-SH-835 to S02-SH-837, S02-SH-840 to S02-SH-843, S02-SH-879, S02-SH-880, S02-SH-885, S02-SH-887, S02-SH-894, S02-SH-895, S02-SH-897 to S02-SH-899, S02-SH-902, S02-SH-905). A requirement on the merchant to show its contact information ('you must provide', 'mandatory for merchants selling in the EU') is read as naming the merchant as who sets it; the law or terms that require it are not who sets it (rule 4). Added S02-V-1006, the platform: automated policies and defaults (S02-SH-815, S02-SH-826, S02-SH-890, S02-SH-900), and, a reading, the platform's fallbacks (S02-SH-817, S02-SH-819, S02-SH-893), as RD3-S5 read S02-BC-317. Compared with S02-SA-038 in `raised_by`: no shared term, so `answers` alone.
- Under S02-VP-68: S02-SH-809, S02-SH-811, S02-SH-816 to S02-SH-819, S02-SH-879, S02-SH-880, S02-SH-885, S02-SH-895, S02-SH-901 joined S02-V-658 (the whole store: one value of each in Settings > General > Store contact details, a reading as RD3-1's).
- Leads placed under other points: S02-SH-883 joined S02-V-602 (currency, the store's own country: 'set based on the business country selected in Business details'; passive, so no `who sets` answer); S02-SH-894 joined S02-V-604 (the seller, 'store currency'); S02-SH-820 joined S02-V-609 (language, the seller: 'review the policy content available to customers in each language'). S02-SH-889 and S02-SH-892 are placed in the revisit of S02-V-745 (messages to buyers). S02-SH-823 also names a requirement by where the merchant is located or ships to; a requirement, not a value the store holds, so it is placed only under the seller.

Statements noted (rule 2):
- S02-SH-839 (f): a legal requirement on what seller information must be displayed (INFORM Consumers Act), in the passive voice; names no party that sets it, nor what it is taken per
- S02-SH-882 (f): a renamed section ('Billing address' to 'Store address'); names neither what the contact information takes its value per nor who sets it
- S02-SH-888 (f): says the account's email is separate from the store email; names neither what the contact information takes its value per nor who sets it
- S02-SH-896 (f): lists the Liquid variables a privacy policy takes ('{{address}} Store address'); names neither what the contact information takes its value per nor who sets it
- S02-SH-903 (f): names a policy type ('CONTACT_INFORMATION The contact information.'); names neither what it takes its value per nor who sets it
- S02-SH-904 (f): the API mutation that updates a policy names no party that sets it (rule 4)

### Revisits S02-V-737 and S02-V-740 (S02-VP-80, S02-VP-81, were `not covered`)

- S02-V-737 replaced by the whole store, 'In private mode, all of your online store's pages are hidden from visitors and search engines' (S02-SH-719, S02-SH-752, S02-SH-756, S02-SH-759, S02-SH-775, S02-SH-778, S02-SH-781; S02-SH-726 a reading of its identifier). No lead sets the store's access per market or per buyer's country. S02-SH-723 and S02-SH-783 restrict access to B2B customers, a group of buyers, none of the four phrases: placed under S02-VP-81 only.
- S02-V-740 replaced by the seller, 'You can manage access to your online store by activating or deactivating private mode' (S02-SH-719 to S02-SH-724, S02-SH-749, S02-SH-750, S02-SH-753 to S02-SH-756, S02-SH-760, S02-SH-776, S02-SH-777, S02-SH-779, S02-SH-780, S02-SH-783 to S02-SH-785); added S02-V-1013, the platform (by default, automatically: S02-SH-720, S02-SH-759, S02-SH-775, S02-SH-783; S02-SH-778's frozen store, a reading); S02-V-1014, the store owner (S02-SH-758, S02-SH-781); S02-V-1015, the Manage settings permission (S02-SH-727, a reading of its 'Preferences page').
- Compared with S02-SA-063 and S02-SA-064 in `raised_by`: Shopify's 'private mode' and Salla's maintenance share no term, so `answers` alone.

Statements noted (rule 2):
- S02-SH-725 (f): defines the password page ('the landing page displayed when ... private mode is active'); names neither what the store's status takes its value per nor who sets it
- S02-SH-751 (f): says the platform's subscription charges continue while access is restricted: the platform's fees, not a setting under (f)
- S02-SH-772 (f): a store's status in the organization's settings (active or pending Shopify Plus contract addition) is a setting of the platform's account, not of the store (rule 1)
- S02-SH-774 (f): as S02-SH-772, the statuses Active and Pending contract addition of the organization's stores: a setting of the platform's account, not of the store (rule 1)

### Revisits S02-V-742 and S02-V-745 (S02-VP-82, S02-VP-83, were `not covered`)

- S02-V-742 replaced by the buyer's country, 'you can send SMS marketing messages only to customers located in the following countries' (S02-SH-956 and S02-SH-957, runs of one list; S02-SH-946 to S02-SH-949, S02-SH-955, S02-SH-963, S02-SH-965 to S02-SH-970, S02-SH-972; S02-SH-872 a reading of whose countries). Added S02-V-1021, the store's own country ('if your business address is in a supported country', S02-SH-869; 'If your store is located in Brazil or Indonesia', S02-SH-965, S02-SH-966; S02-SH-968 to S02-SH-970), and S02-V-1022, the whole store, a reading of the store's one sender name and sender email (S02-SH-871, S02-SH-879).
- S02-V-745 replaced by the seller, 'You can automatically send an email to customers after they have abandoned their checkout' (S02-SH-866 to S02-SH-869, S02-SH-873 to S02-SH-879, S02-SH-914 to S02-SH-919, S02-SH-942, S02-SH-944 to S02-SH-946, S02-SH-948, S02-SH-951, S02-SH-963, S02-SH-965); added S02-V-1023, the platform ('Most customer notifications are sent automatically', S02-SH-863, S02-SH-874, S02-SH-877, S02-SH-889, S02-SH-890, S02-SH-942; S02-SH-871, S02-SH-872 a reading); S02-V-1024, no one (S02-SH-863: 'can't be deactivated'); S02-V-1025, the buyer (S02-SH-864: 'can only be turned off through a customer's Shop app settings'); S02-V-1026, a third-party app (S02-SH-958). S02-SH-942 (POS receipts in Italy, from the revisit of S02-V-733) and S02-SH-889 (from the revisit of S02-V-735) are placed here; S02-SH-942's 'Shopify POS locations in Italy' is a place the store sells at (rule 1), so it answers only who sets.
- S02-SH-874's 'the language that they placed their order in' and S02-SH-945's customers 'within a certain distance of a specific retail location' name what the message differs by, none of the four phrases: placed only under S02-VP-83.
- Compared with S02-SA-259 in `raised_by`: no shared term, so `answers` alone.

Statements noted (rule 2):
- S02-SH-892 (f): names which addresses a Shopify Flow invoice's sender email can be ('the store email or one of the staff account emails'); names neither what it is taken per nor who sets it
- S02-SH-950 (f): a charge for each toll-free number used for SMS marketing: the platform's fees, not a setting under (f)
- S02-SH-952 (f): says there are additional requirements to send SMS marketing to customers in some regions: requirements, not a value the store holds; names no party that sets one
- S02-SH-953 (f): a legal requirement (the ePrivacy Directive) on stores located in or sending to the European Union; a party that requires isn't who sets (rule 4), and no value of the store is named
- S02-SH-954 (f): as S02-SH-953, for the United Kingdom's Privacy and Electronic Communications Regulations
- S02-SH-959 (f): charges for SMS marketing by region: the platform's fees, not a setting under (f)
- S02-SH-960 (f): the per-message charge for SMS marketing: the platform's fees, not a setting under (f)
- S02-SH-961 (f): SMS marketing prices per country, runs of one list with S02-SH-962: the platform's fees, not a setting under (f)
- S02-SH-962 (f): as S02-SH-961, the list's last run: the platform's fees
- S02-SH-971 (f): WhatsApp messages are charged per message by region: the platform's fees, not a setting under (f)
- S02-SH-973 (f): WhatsApp prices per region, runs of one list with S02-SH-974 to S02-SH-977: the platform's fees, not a setting under (f)
- S02-SH-974 (f): as S02-SH-973: the platform's fees
- S02-SH-975 (f): as S02-SH-973: the platform's fees
- S02-SH-976 (f): as S02-SH-973: the platform's fees
- S02-SH-977 (f): as S02-SH-973: the platform's fees

### Revisits S02-V-877 and S02-V-881 (S02-VP-87, S02-VP-88, were `not covered`)

- S02-V-877 replaced by a market, 'In markets configured to require consent (usually the European Economic Area (EEA) and the United Kingdom), web pixels run only when visitors have provided the permissions required' (S02-SH-731); S02-V-1027 added, the buyer's country (S02-SH-803, S02-SH-804: 'In configured cookie banner regions', 'the consent obtained in these regions', a reading of the regions as the visitors'; S02-SH-801: 'customers, such as those located in the European Economic Area').
- S02-V-881 replaced by the seller, 'You can add and manage pixels in the Customer events section of your Shopify admin' (S02-SH-728, S02-SH-763 to S02-SH-765, S02-SH-767, S02-SH-769, S02-SH-771, S02-SH-794 to S02-SH-796, S02-SH-798 to S02-SH-800, S02-SH-805 to S02-SH-808); added S02-V-1028, the platform (S02-SH-730, S02-SH-731, S02-SH-769, S02-SH-771); S02-V-1029, apps and the third-party app partner (S02-SH-729, S02-SH-768); S02-V-1030, a developer (S02-SH-729, rule 4); S02-V-1031, the buyer (S02-SH-731, S02-SH-732, S02-SH-802); S02-V-1032, the Manage and add custom pixels permission (S02-SH-735); S02-V-1033, the Manage and install apps and channels permission (S02-SH-766); S02-V-1034, no one (S02-SH-770: 'can't be optimized').
- S02-SH-797 ('Google Analytics can't track events until you deactivate private mode') joined S02-V-740 (S02-VP-81, the seller of the store's access).
- Compared with S02-BC-144 and S02-BC-145 in `raised_by`: Shopify's market and pixels are not BigCommerce's storefront and web analytics as terms, so `answers` alone.

Statements noted (rule 2):
- S02-SH-734 (f): the View customer events permission gates viewing pixels, not setting them; names neither what the analytics take their value per nor who sets them
- S02-SH-736 (f): the API object for web pixels names no party that sets them (rule 4: an API alone names no party); its 'you' is the API's caller, unnamed
- S02-SH-737 (f): the API field for a web pixel's settings names neither what they are taken per nor who sets them
- S02-SH-738 (f): pixels don't fire in Google AI Mode and Gemini's direct checkout: a fact of one sales channel's checkout, none of the four phrases; names no party that sets it
- S02-SH-739 (f): as S02-SH-738, for Meta's direct checkout
- S02-SH-740 (f): as S02-SH-738, for Microsoft Copilot's direct checkout

### Revisits S02-V-885 and S02-V-889 (S02-VP-89, S02-VP-90, were `not covered`)

- S02-V-885 replaced by the whole store, 'You can turn the notification off for your whole store, or for individual recipients' (S02-SH-787). A recipient is a staff member, none of the four phrases. S02-SH-744's notifications 'for orders from a particular POS location or from the web' name a place the store sells at, or a channel, not a market: placed only under S02-VP-90.
- S02-V-889 replaced by the seller, 'You can create and edit email notifications to let you or staff know' (S02-SH-741, S02-SH-742, S02-SH-744 to S02-SH-747, S02-SH-761, S02-SH-762, S02-SH-786 to S02-SH-793; S02-SH-792 and S02-SH-793 a reading of the merchant's Shopify Flow workflows); added S02-V-1035, the platform (by default: S02-SH-741, S02-SH-742, S02-SH-788; S02-SH-791 a reading), and S02-V-1036, the Orders and Manage settings permissions (S02-SH-743, S02-SH-748). S02-SH-786's Disputes > Manage permission gates who receives the notification, not who sets it: no row.
- S02-SH-747 and S02-SH-748 name the notifications sent to customers too: S02-SH-747 joined S02-V-745 (S02-VP-83, the seller), and S02-V-1037 was added under S02-VP-83, the Manage settings permission (S02-SH-748).
- Compared with S02-BC-144 in `raised_by`: no shared term, so `answers` alone.

### `place` tasks: where the statements went

- S02-SH-604 (channel markets: 'channel-specific product availability, pricing, or currency'): S02-V-614, S02-V-620, S02-V-600 (a market), S02-V-618, S02-V-622, S02-V-604 (the seller). Its 'Merchants can't configure web presence, domains, or discounts for channel markets' gives no answer: it names what a channel market can't hold, not what the setting is taken per.
- S02-SH-608 (MarketCatalog: 'distinct shopping experiences for different geographic regions or customer segments'): S02-V-614, S02-V-620.
- S02-SH-610 (Retail markets: 'Set different prices for different retail locations'): S02-V-620, S02-V-622.
- S02-SH-631, S02-SH-634, S02-SH-636, S02-SH-638, S02-SH-641 (Przelewy24, MB WAY, Bizum): S02-V-645 (a market: 'an active market that includes Portugal with EUR'); S02-SH-634 and S02-SH-638 also S02-V-646 (the buyer's country: 'Your customers must be located in Portugal'); S02-V-1048 added under S02-VP-61, the store's own country ('If your store isn't located in Portugal', S02-SH-636, S02-SH-641; S02-SH-631's 'If your Shopify Payments account is in Poland'); S02-SH-636 and S02-SH-641 joined S02-V-647 (the seller: 'You might need to change your currency or checkout settings').
- S02-SH-646 ('You can sell products from multiple business entities on a single store'): S02-V-651 (the seller).
- S02-SH-689, S02-SH-693 (customizing theme and checkout for each market): S02-V-627, S02-V-631 (a market), S02-V-629, S02-V-632 (the seller); S02-SH-689's B2B catalogs also S02-V-614, S02-V-620.
- S02-SH-698 ('Custom pricing by market'): S02-V-620, S02-V-622; its 'setting manual exchange rates' S02-V-604.
- S02-SH-710, S02-SH-711 (the entity by POS location, and regional markets for each country's entity): S02-V-649 (a market; S02-SH-710 read with Shopify's term 'Retail markets use POS locations as their condition'); S02-SH-711 and S02-SH-712 also S02-V-651 (the seller). S02-SH-710's 'staff can't manually change the entity during checkout' names only who is kept out.
- S02-SH-714, S02-SH-715 (cookie banner regions): S02-V-997 (the buyer's country), S02-V-673 (a market: 'based on your configured markets', 'if you have active markets in these regions'), S02-V-747 (the seller), S02-SH-715 also S02-V-998 (the platform: 'we will automatically configure your cookie banner'); S02-V-1052 added under S02-VP-75, the whole store (S02-SH-714: 'Your setting for Shopify Network Intelligence takes effect globally').
- S02-SH-978 to S02-SH-988, S02-SH-990 to S02-SH-994 (Settings > Taxes and duties): the buyer's country (S02-V-634: tax regions, S02-SH-979 to S02-SH-981 runs of one list; 'sold to European customers'; 'shipments to the United States'), a market (S02-V-633: 'in markets with dynamic tax inclusion', 'Market Duties Taxes Canada', 'markets that have tax registration'), the seller (S02-V-635: the page's controls), the platform (S02-V-636: 'Automatically calculated for Canada, European Union, and United States'), Avalara (S02-V-638: S02-SH-986).
- S02-SH-653, under (g): placed by S02-V-661 and S02-V-994 (the revisit of S02-V-662).

Statements noted (rule 2):
- S02-SH-621 (f): names which data protection laws apply to Shopify's processing (by the merchant's or customers' location): law, not a setting of the store; names no party that sets one
- S02-SH-623 (f): a contractual obligation on the merchant to obtain consent where it or its customers are in the EEA, United Kingdom or Switzerland: an obligation, not a value the store holds; a party that requires isn't who sets (rule 4)
- S02-SH-694 (f): names settings in general ('configure specific settings for each international region'), of no one kind of setting
- S02-SH-695 (f): as S02-SH-694, for the Grow plan: settings in general, of no one kind of setting
- S02-SH-703 (f): which B2B features each plan offers: conditions (h), not what a setting takes its value per or who sets it
- S02-SH-704 (f): which cross-border features each plan offers: conditions (h), not what a setting takes its value per or who sets it
- S02-SH-717 (f): the obligations the GDPR and equivalent laws impose by where a business is or whom it sells to: law, not a setting of the store; names no party that sets one

### Rereads (rule 4, widened)

- S02-SH-093 (f): left noted. Its permissions gate the Markets page, whose settings are of no one kind (settings in general); it names no setting it gates by kind.
- S02-SH-156 (f): left noted. 'VIEW_CATALOGS' gates viewing catalogs, not setting them.
- S02-SH-157, S02-SH-158 (f): placed. S02-V-1057 (S02-VP-48) and S02-V-1058 (S02-VP-50) added, the permission to create and edit catalogs ('"permissions":["CREATE_AND_EDIT_CATALOGS"]'; 'The user must have permission to create and edit catalogs'): a catalog sets a market's products and prices, as RD3-1 read Shopify's term.
- S02-SH-159 (f): placed. S02-V-1059 (S02-VP-48) and S02-V-1060 (S02-VP-50) added, the permission to delete catalogs.
- S02-SH-210 (f): placed. S02-V-1061 added under S02-VP-56, no one: 'no setting in your Shopify admin or your theme turns it off'. Its 'You can't hide or reword it' names who is kept out, as RD3-1 noted. The point's note says so.
- S02-SH-213, S02-SH-214 (f): placed. S02-V-1062 added under S02-VP-64, the Manage payments settings permission, which gates updating and deactivating a market's Managed Markets (a reading of Managed Markets as the merchant of record it adds, as in the point's `x_words`).
- S02-SH-242, S02-SH-244 (f), and S02-SH-244 (g): placed. Joined S02-V-990 (S02-VP-70, no one), with S02-SH-653's 'can't be changed'. S02-SH-242's 'You can't change which additional fields are included or whether a field is required' is read as no one can, since S02-SH-653 states the same requirement in the passive; S02-SH-244's 'can't be deactivated unless the store is on the Shopify Plus plan' is passive. Their placements under S02-VP-69 stand. The point's note says so.
- S02-SH-294, S02-SH-380 (f): placed. S02-V-1063 added under S02-VP-60, the permissions that gate creating and updating a market's shipping option ('OVERVIEWS', 'REPORTS', 'PRODUCTS', 'DOMAINS', 'PREFERENCES', or 'VIEW_MARKETS' and 'CREATE_AND_EDIT_MARKETS').
- S02-SH-571 (f): left noted. 'You will not be able to add region catalogs ... to a B2B market' is a rule on what a market may hold, RD2's question, not that no one sets the products or prices.

### Candidates for a new point

None. Every statement that answered (f)'s questions had an X of one of the points' kinds. The closest calls, placed by a reading: cash rounding on POS (S02-SH-934, S02-SH-935) under currency, as how amounts are paid in a currency; POS receipts printed automatically in Italy (S02-SH-942) under messages to buyers; Shopify Network Intelligence (S02-SH-714) under privacy and consent.

### Words searched for

None: the second pass raises no point, so no search for earlier platforms' rows was run.

### Problems with the brief or the tools

- **Leads that fail their point's role test.** S02-SH-665 to S02-SH-687, leads for the buyer's address (S02-VP-69), are the address service's answer to the admin's Edit business details page, the store's address: they are placed under S02-VP-76, where RD3-1 placed the same page's captured forms. S02-SH-G06, which names them, stays as the `gap` row of S02-VP-69.
- **Values per location.** Many of Shopify's leads set a value per location: a POS location, a fulfillment location, a retail location's country. A location is a place the store sells at (rule 1), none of the four phrases. They are placed under a market only where Shopify's term ties a POS location to a market ('Retail markets use POS locations as their condition', `terms.tsv`); otherwise only their `who sets` half is placed, or they are noted.
- **Points without a task.** The revisits and place tasks placed statements under every point they answer, so rows were joined or added under points with no task (S02-VP-41, 42, 47 to 50, 55, 56, 57 to 64, 67, 68, 70, 75, 76, 84). No row was replaced or removed outside a revisit.
- **Ids.** RD3-S2 writes beside this part, so this part's new ids are not consecutive (S02-V-990 to S02-V-998, S02-V-1002 to S02-V-1006, S02-V-1013 to S02-V-1015, S02-V-1021 to S02-V-1037, S02-V-1048, S02-V-1052, S02-V-1057 to S02-V-1063).
- **`done`** now prints what it recorded.
- **Correction to the Ids line above:** this part's rows in that range are S02-V-1002 to S02-V-1004 and S02-V-1006; S02-V-1005 is not this part's.

## Second pass, RD3-S2: woocommerce, bullet f

WooCommerce's tasks under (f) in `b/second-pass/RD3/worklist.tsv`: 37 revisits, then 4 `place` tasks. Each row is compared with the statement in its point's `raised_by` from another platform (rule 5); every new row takes `answers` alone. This part places the (f) half of statements under (f) and (g): where that half answers a point, it is placed there, and their (g) half is left to RD3-S3. Some rows that this part wrote under a point's `the whole store` hold statements under (f) and (g) (S02-V-911, S02-V-941, S02-V-950), so RD3-S3 will find them already placed.

How this part reads WooCommerce's new statements, beside the first pass's readings:
- **A market.** A channel is among rule 1's markets, so the second pass reads three things as a market the store sells into: Point of Sale beside the online store (S02-WC-351 to S02-WC-355, S02-WC-380 to S02-WC-385); Google, by its 'Channel Visibility' (S02-WC-356, S02-WC-357, S02-WC-371); and the countries the store sells to, its allowed countries (S02-WC-278, S02-WC-279), as the first pass read 'define the regions you will sell ... to' as WooCommerce's market under (e). Each is a reading, marked in its row. The first pass's "no WooCommerce row takes `a market the store sells into`" no longer holds.
- **Code.** As the first pass read it. Also, the default value that the code passes to its own filter (`apply_filters( '...', true )`) is read as the platform's, and marked as a reading (S02-WC-403, S02-WC-424, S02-WC-508).
- **Parties named.** WordPress (S02-WC-326), developers (S02-WC-342, S02-WC-496, S02-WC-503), an extension or plugin (S02-WC-343, S02-WC-450, S02-WC-463 to S02-WC-467, S02-WC-498 to S02-WC-502), a hosting provider (S02-WC-500) and Affirm (S02-WC-319) are each their own answer. 'Store managers' (S02-WC-365) and 'you' in the platform's instructions to developers (S02-WC-345, S02-WC-414) are read as the seller, as the first pass read S02-WC-159. Roles and permissions that the statements say gate a setting are their own answers (rule 4).
- **Notifications to the merchant.** The platform's inbox notes are read under S02-VP-89 and S02-VP-90. The extensions that the platform suggests or shows to the merchant by the store's country are noted, as the first pass noted S02-WC-001: they are (c)'s kinds, not a setting of the store.

### Revisits: rows replaced or removed, and what took their place

- S02-V-895 (S02-VP-41, was `gap` S02-WC-G05): replaced by the store's own country, S02-WC-292 (onboarding updates the store's currency from 'storeLocation', a reading of the minified code). S02-WC-318, S02-WC-320 and S02-WC-321 joined S02-V-927 (S02-VP-61, the buyer's country), and S02-V-1000 was added there: the store's own country ('your WooPayments account country', S02-WC-318, a reading).
- S02-V-899 (S02-VP-42, was `gap` S02-WC-G05): removed. S02-WC-312, S02-WC-314 and S02-WC-315 joined the seller (S02-V-896); S02-WC-292 and the place task S02-WC-244 joined the platform (S02-V-897).
- S02-V-900 (S02-VP-43, was `gap` S02-WC-G05): replaced by the whole store, S02-WC-326 ('a 100% complete translation for your language', a reading of 'your language' as the site's one language). S02-WC-319 was placed under S02-VP-62: S02-V-1001 added, Affirm ('Affirm may disable your access to their payment method').
- S02-V-901 (S02-VP-44, was `gap` S02-WC-G05): replaced by the seller (S02-WC-324, S02-WC-325, S02-WC-312). S02-V-999 was added: WordPress (S02-WC-326).
- S02-V-902, S02-V-903 (S02-VP-45, S02-VP-46, were `not covered`): replaced by `gap` S02-WC-G08.
- S02-V-904 (S02-VP-47, was `not covered`): replaced by a market, the channel: Point of Sale beside the online store, and Google (S02-WC-351 to S02-WC-353, S02-WC-355 to S02-WC-357, a reading).
- S02-V-905 (S02-VP-48, was `not covered`): replaced by the seller (S02-WC-346, S02-WC-348, S02-WC-351, S02-WC-352, S02-WC-354 to S02-WC-357, S02-WC-360). S02-V-1005 was added: the platform (S02-WC-354, S02-WC-357, S02-WC-348).
- S02-V-910 (S02-VP-52, was `not covered`): replaced by the seller (S02-WC-361 to S02-WC-363, S02-WC-365, S02-WC-366, S02-WC-368, S02-WC-370, S02-WC-371, S02-WC-373, S02-WC-374). Three rows were added: S02-V-1009, the administrator or shop manager role (S02-WC-362, S02-WC-369); S02-V-1010, the buyer (S02-WC-364, S02-WC-374); S02-V-1011, the platform ('default' => 'yes', S02-WC-366). Also added: S02-V-1012 under S02-VP-51, a market (Show coupon on Google, S02-WC-371, a reading).
- S02-V-911 (S02-VP-53, was `not covered`): replaced by the whole store ('apply site-wide', S02-WC-375, S02-WC-377). S02-WC-375, S02-WC-377, S02-WC-378 and S02-WC-379 joined the seller (S02-V-912, S02-VP-54).
- S02-V-913 (S02-VP-55, was `not covered`): replaced by the buyer's country ('based on what country the shopper is in', S02-WC-344).
- S02-V-914 (S02-VP-56, was `not covered`): replaced by the seller (S02-WC-345, S02-WC-342). Added S02-V-1007, developers (S02-WC-342), and S02-V-1008, an extension (S02-WC-343).
- S02-V-929, S02-V-930 (S02-VP-63, S02-VP-64): left `not covered`. No lead under (f), no gap and no absence; S02-WC-274, S02-WC-275 and S02-WC-277 are under (g) only, and are RD3-S3's.
- S02-V-931 (S02-VP-65): left `not covered`. No lead answers what returns and cancellations take their value per (S02-WC-278 and S02-WC-279 were placed under other points, and S02-WC-280, S02-WC-286 and S02-WC-287 noted), and there is no gap or absence. S02-WC-281 is under (g) only, and is RD3-S3's.
- S02-V-932 (S02-VP-66, was `not covered`): replaced by the seller, 'enable the order withdrawal feature in the Advanced settings' (S02-WC-279, a lead of S02-V-931).
- S02-V-933 (S02-VP-67, was `not covered`): replaced by the whole store ('available at checkout regardless of customer location', S02-WC-390). Added S02-V-1018, the buyer's country (the legacy local pickup method by shipping zone, S02-WC-392, S02-WC-390). Local pickup is also a delivery method (rule 1: a thing of two kinds goes under both), so S02-WC-390 and S02-WC-392 joined S02-V-922, and S02-WC-390 joined S02-V-924 (S02-VP-59).
- S02-V-934 (S02-VP-68, was `not covered`): replaced by a market: Point of Sale's own store details, which take the store's base address until the seller changes them (S02-WC-380 to S02-WC-385, rule 4, a reading). Added S02-V-1016, the whole store (the email Store Address tag, S02-WC-388). S02-WC-386 and S02-WC-387 (the sender's 'From' name and address) are messages to buyers, so they were placed under S02-VP-83.
- S02-V-937 (S02-VP-69, was `gap` S02-WC-G05): removed. S02-WC-304 to S02-WC-309 joined the buyer's country (S02-V-935): the postcode is validated by its address's country. Under S02-VP-70, S02-WC-303 to S02-WC-309 and S02-WC-327 ('our policy') joined the platform (S02-V-939), and S02-WC-328 ('custom snippets') joined the seller (S02-V-938).
- S02-V-941 (S02-VP-71, was `not covered`): replaced by the whole store: the roles' capabilities reach all the store's settings, reports, products and orders, and none is by market or country (S02-WC-454, S02-WC-455, S02-WC-457 to S02-WC-462, S02-WC-471, S02-WC-472, S02-WC-474, S02-WC-475, a reading).
- S02-V-942 (S02-VP-72, was `not covered`): replaced by the seller (S02-WC-451, S02-WC-452, S02-WC-463, S02-WC-464). Three rows were added: S02-V-1049, the platform (S02-WC-451, S02-WC-453, S02-WC-456, S02-WC-468 to S02-WC-472); S02-V-1050, an extension or plugin (S02-WC-463 to S02-WC-467); S02-V-1051, the Administrator role (S02-WC-461, S02-WC-473).
- S02-V-943, S02-V-944 (S02-VP-73, S02-VP-74): left `not covered`. The leads give the default customer location, which the first pass read under taxes and shipping, not market selection, through WooCommerce's term 'Default customer location'. So S02-WC-397 joined S02-V-916 and S02-V-923 (the store's own country), S02-WC-399 joined S02-V-915 and S02-V-922 (the buyer's country), and S02-WC-397 to S02-WC-399 joined S02-V-919 and S02-V-926 (the platform). S02-WC-400 was noted. There is no gap or absence.
- S02-V-945 (S02-VP-75, was `not covered`): replaced by the buyer's country, cookie consent asked of users in the EEA, UK and Switzerland (S02-WC-413, a lead of S02-V-957).
- S02-V-947 (S02-VP-77, was `gap` S02-WC-G05): replaced by the store's own country (S02-WC-292: the measurement units are set from the store's location in onboarding).
- S02-V-948 (S02-VP-78, was `not covered`): replaced by the seller (S02-WC-389, S02-WC-390, S02-WC-395, S02-WC-396). Added S02-V-1019, the manage_woocommerce capability of Shop Managers (S02-WC-394), and S02-V-1020, the platform (S02-WC-395, S02-WC-393).
- S02-V-949 (S02-VP-79, was `not covered`): replaced by the seller (S02-WC-380 to S02-WC-384). Added S02-V-1017, the platform (the defaults of S02-WC-381 to S02-WC-385).
- S02-V-950 (S02-VP-80, was `not covered`): replaced by the whole store: Coming soon or Live is one mode for the site or its store pages (S02-WC-476, S02-WC-478, S02-WC-480 to S02-WC-488, S02-WC-490, S02-WC-497, S02-WC-509).
- S02-V-951 (S02-VP-81, was `not covered`): replaced by the seller (S02-WC-312, read as site visibility, and S02-WC-476, S02-WC-477, S02-WC-479, S02-WC-481, S02-WC-489, S02-WC-497, S02-WC-504 to S02-WC-506). Four rows were added: S02-V-1053, the platform (S02-WC-491 to S02-WC-495, S02-WC-508); S02-V-1054, another plugin or application (S02-WC-498, S02-WC-499, S02-WC-501, S02-WC-502); S02-V-1055, a hosting provider (S02-WC-500, S02-WC-496); S02-V-1056, developers (S02-WC-503, S02-WC-496).
- S02-V-952 (S02-VP-82, was `not covered`): replaced by the whole store (customer emails 'in the store language', S02-WC-423).
- S02-V-953 (S02-VP-83, was `not covered`): replaced by the seller (S02-WC-425, S02-WC-426, S02-WC-428, S02-WC-429, S02-WC-386, S02-WC-387). Added S02-V-1042, the platform (S02-WC-423, S02-WC-424, S02-WC-427, S02-WC-428, S02-WC-386, S02-WC-387), and S02-V-1043, the buyer (customers sign up, S02-WC-428, S02-WC-429).
- S02-V-954 (S02-VP-84, was `not covered`): replaced by the buyer (S02-WC-448, S02-WC-413, S02-WC-415). Added S02-V-1046, the seller (S02-WC-415), and S02-V-1047, an extension (S02-WC-450, S02-WC-415).
- S02-V-956 (S02-VP-86): left `not covered`. The leads are the extensions the platform suggests or shows to the merchant by the store's base country, and the merchant's WooCommerce.com subscriptions. All were noted, and there is no gap or absence.
- S02-V-957 (S02-VP-87, was `not covered`): replaced by the buyer's country (S02-WC-413). Added S02-V-1038, the whole store (analytics in the store's default currency, S02-WC-408).
- S02-V-958 (S02-VP-88, was `not covered`): replaced by the seller (S02-WC-401, S02-WC-404, S02-WC-406, S02-WC-409, S02-WC-411, S02-WC-412, S02-WC-414, S02-WC-415, S02-WC-440). Three rows were added: S02-V-1039, the platform (S02-WC-401, S02-WC-403, S02-WC-410, S02-WC-440); S02-V-1040, the buyer (S02-WC-402, S02-WC-413, S02-WC-415, S02-WC-448); S02-V-1041, the permission to manage WooCommerce (S02-WC-407).
- S02-V-959 (S02-VP-89, was `not covered`): replaced by the store's own country (inbox notes by the base country, S02-WC-433, S02-WC-434). Added S02-V-1044, a market (the order withdrawal note, for stores whose allowed countries include the EU: S02-WC-278, S02-WC-279, S02-WC-510, a reading).
- S02-V-960 (S02-VP-90, was `not covered`): replaced by the seller (S02-WC-430 to S02-WC-432, S02-WC-436 to S02-WC-439). Added S02-V-1045, the platform (S02-WC-430 to S02-WC-435, S02-WC-278, S02-WC-279, S02-WC-510).

A gap named in no revisit's `why` (S02-WC-G05) was settled by gap-closing, and went with the rows it stood in.

### `place` tasks

- S02-WC-244 (update_store_currency_and_measurement_units()) joined S02-V-897 (S02-VP-42, the platform: `'woocommerce_currency' => $country_info['currency_code']`). Its words don't say whose country `$country_info` is, so it is not placed under S02-VP-41. Its units are listed below as a candidate.
- S02-WC-271, S02-WC-272 and S02-WC-273 were noted. S02-WC-272 and S02-WC-273 are runs of one list (rule 5).

### Statements noted (rule 2)

- S02-WC-293 (f): saves the store's country ('woocommerce_default_country') from the location entered in onboarding, which is (b)'s question. Its words don't name the setting that `t(...)` sets from that location. S02-WC-292, which binds t to updateStoreCurrencyAndMeasurementUnits, has another identifier, so rule 5's Lists don't join them. It names no setting's value per market, and not who sets it
- S02-WC-297 (f): the REST API's response includes 'detailed locale information' for a country, without saying whose country it is or which setting of the store takes it; as the first pass noted S02-WC-165
- S02-WC-298 (f): the keys the REST API returns for each country ('currency_code', 'dimension_unit' and 'weight_unit' among them), without saying whose country it is or which setting of the store takes them; as S02-WC-165
- S02-WC-299 (f): 'Default ISO4127 alpha-3 currency code for the country.', a field of the REST API's data for each country, without saying whose country it is or which setting of the store takes it; as S02-WC-165
- S02-WC-300 (f): 'The unit weights are defined in for this country.'; as S02-WC-299
- S02-WC-301 (f): 'The unit lengths are defined in for this country.'; as S02-WC-299
- S02-WC-302 (f): the onboarding settings include the file i18n/locale-info.php ('localeInfo'); names no setting's value per market, and not who sets it
- S02-WC-313 (f): a map of currencies by country in the legacy setup wizard ('$currency_by_country'), without saying whose country it is, that the store's currency takes it, or who sets it; as S02-WC-165
- S02-WC-316 (f): MultilingualPress 'can display your content, products, and prices in multiple languages and currencies'; names neither what the languages or currencies take their value per nor who sets them
- S02-WC-317 (f): the daily cutoff of WooPayments' payouts by the account's country ('each day starts at midnight in your local time zone'): payouts, of (c)'s kinds, not a setting of the store; as the first pass noted S02-WC-035
- S02-WC-288 (f): the platform's default units, those of 'US' in i18n/locale-info.php ("$locale_info['US']['weight_unit']"). This answers who sets the units (the platform, a default the code sets), and no point asks who sets units and time zone: a candidate for a new point (below)
- S02-WC-289 (f): 'This controls what unit you will define weights in.' answers who sets the units ('you', the seller), and no point asks it: a candidate for a new point (below)
- S02-WC-291 (f): 'This controls what unit you will define lengths in.'; as S02-WC-289
- S02-WC-347 (f): the options of the setting Catalog visibility ('Shop and search results', 'Shop only', 'Search results only', 'Hidden'), behind a filter. It names neither what the products offered take their value per in one of rule 4's roles nor who sets them (rule 4: a filter alone names no party)
- S02-WC-349 (f): the filter woocommerce_product_is_visible; a filter alone names no party (rule 4), and it names no value per market
- S02-WC-350 (f): the filter woocommerce_is_purchasable; as S02-WC-349
- S02-WC-358 (f): 'If you’re selling in the United States, your products can also appear on Google Search, Google Images, and Gmail.': where a service of Google's is offered, which is (h)'s question, not a setting of the store
- S02-WC-359 (f): the countries the store targets on Google Merchant Center ('You can only select the countries that you’re targeting'): the market's own definition, RD2's question under (e); 'must be eligible' is a requirement, not who sets (rule 4); names no setting's value per market
- S02-WC-367 (f): the filter woocommerce_coupons_enabled, which reads the store's option; a filter alone names no party (rule 4), and it names no value per market
- S02-WC-334 (f): the checkout document object's schema, 'to be used for conditional visibility, requirement, and validation of fields'; it names neither what a field takes its value per in one of rule 4's roles nor who sets it
- S02-WC-335 (f): the document object's 'Customer's billing address'; names no setting's value per market, and not who sets it
- S02-WC-336 (f): the country field of the document object's address ('Country code (e.g., US, UK)'), without saying that a setting takes its value by it
- S02-WC-337 (f): the release's code that evaluates a field's 'required' rules against the document object; names neither what the field takes its value per in one of rule 4's roles nor who sets its rules
- S02-WC-280 (f): 'If you sell to customers in the EU, review the right of withdrawal and its exceptions': the right is the law's, not a setting of the store, and 'review' names no party that sets it; the law requires, it doesn't set (rule 4)
- S02-WC-286 (f): Stripe's terms for users in India require the website to show its returns timeline: a third party that requires without setting (rule 4), the terms of (c)'s kinds; names no value per market
- S02-WC-287 (f): Network International's terms require 'clear refund and exchange language': as S02-WC-286
- S02-WC-391 (f): a pickup location's fields, and taxes taken from the address of the location the customer chooses. Rule 1 says a pickup point isn't the store's own country, so that is none of rule 4's four phrases, and the statement names no party that sets the locations
- S02-WC-400 (f): the filter woocommerce_customer_default_location; a filter alone names no party (rule 4), and it names no value per market
- S02-WC-405 (f): 'we made WooCommerce’s order attribution compatible with WP Consent API'; names neither what order attribution takes its value per nor who sets it
- S02-WC-416 (f): the request for marketplace suggestions carries the store's base country. These are suggestions to the merchant of extensions to install, of (c)'s kinds (other features and services of the platform), not a setting of the store; as the first pass noted S02-WC-001
- S02-WC-417 (f): the Extensions page fetches its list with the store's base country; as S02-WC-416
- S02-WC-418 (f): 'Leave this box unchecked if you do not want to pull suggested extensions from WooCommerce.com.', 'default' => 'yes'. It answers who sets the marketplace suggestions (the seller, and the platform's default), which no point asks, of none of rule 1's kinds of setting: a candidate for a new point (below)
- S02-WC-419 (f): the free extension ShipStation is shown to stores whose base location country is CA, GB, AU or NZ; as S02-WC-416
- S02-WC-420 (f): the free extension Packlink is shown to stores whose base location country is among nine European countries; as S02-WC-416
- S02-WC-421 (f): the rule processor that compares 'against the base location - country'; names no setting, only the comparison that S02-WC-419 and S02-WC-420 use
- S02-WC-422 (f): one WooCommerce.com subscription key per production site: the merchant's account with the platform, not a setting of the store (rule 1); names no value per market
- S02-WC-449 (f): the GDPR grants EU residents rights, and developers must make extensions comply: a law and a requirement, not a setting of the store, and a party that requires isn't who sets (rule 4)
- S02-WC-507 (f): users with manage_woocommerce bypass the Coming soon screen. This names who the mode lets through, not what it takes its value per in one of rule 4's roles or who sets it
- S02-WC-271 (f): 'The full list of available currencies is shown below.': the currencies WooPayments accepts. It names neither what a store's currencies take their value per nor who sets them, and 'not supported by American Express' names a party that doesn't support some, not one that sets them
- S02-WC-272 (f): the list of currencies WooPayments accepts, read with S02-WC-273 as one list (rule 5, Lists); as S02-WC-271
- S02-WC-273 (f): as S02-WC-272

By reason, 41 statements:
- 9 of (c)'s kinds: payouts, terms, and suggestions to the merchant (S02-WC-286, S02-WC-287, S02-WC-317, S02-WC-416, S02-WC-417, S02-WC-419 to S02-WC-422).
- 8 of per-country data, or a filter, whose country's role or party isn't said (S02-WC-297 to S02-WC-301, S02-WC-313, S02-WC-349, S02-WC-350).
- 4 candidates for a new point (S02-WC-288, S02-WC-289, S02-WC-291, S02-WC-418).
- The rest name no setting's value per market and no party that sets one.

### Candidates for a new point

The second pass adds no point. These candidates answer a question that no point of their kind asks:
- **who sets "units", of the kind units and time zone.** S02-VP-77 asks only what the units take their value per. The candidates are S02-WC-288 (the platform: the default units are those of 'US'), and S02-WC-289 and S02-WC-291 ('you'), all noted. Two statements give the platform and are placed under other points: S02-WC-244 (`'woocommerce_weight_unit' => $country_info['weight_unit']`) and S02-WC-292 ('updateStoreCurrencyAndMeasurementUnits').
- **who sets "timezone", of the kind units and time zone.** S02-WC-312, the seller: 'address, visibility, currency, language, and timezone'. It is placed under S02-VP-42, S02-VP-44 and S02-VP-81.
- **who sets "address", of the kind the store's address.** S02-VP-76 asks only what it takes its value per, and (b) asks who sets the store's own country. The candidate is S02-WC-312, as above.
- **who sets "suggested extensions" (Show Suggestions), of no kind of rule 1's.** The suggestions are what the platform shows the merchant, not the apps a store installs (S02-VP-86's kind). The candidate is S02-WC-418 (the seller, and the platform's default 'yes'), noted.

### Candidates not placed

Each of these statements is placed under another point. These candidates are not:
- S02-WC-319's 'Affirm also requires that your site only be available in U.S. English (en_US), Canadian English (en_CA), and/or Canadian French (fr_CA)': a party that requires the site's languages without setting them (rule 4).
- S02-WC-364's 'WooCommerce core does not apply coupon codes automatically' names only who is kept out (rule 5).
- S02-WC-318's 'They are paying in your account country’s national currency' is a condition on the currency the buyer pays in, under the payment method's point, not currency's.
- S02-WC-480's 'Only authorized users or those with a private link can view the store' names who may view, not who sets.

### Words searched for

None. The second pass raises no point, so no search was run for the earlier platforms' rows.

### Problems with the brief or the tools

- **Revisits that end with no answer.** Six revisits are left `not covered`, each with its `done` row: S02-V-929, S02-V-930, S02-V-931, S02-V-943, S02-V-944 and S02-V-956. Their leads under (f) answer the point under none of the rules, and `why` names no gap or absence. The brief gives no outcome for this: a `gap` row needs a gap that `why` names. The coordinator may rule on each. RD3-S3's statements under (g) (S02-WC-274, S02-WC-275, S02-WC-277, S02-WC-281, S02-WC-418, S02-WC-422) may answer some of them, and the part that places one replaces the `not covered` row, since such a row never stands beside another.
- **Calls this part made that the coordinator may read otherwise.**
  - The default customer location (S02-WC-397 to S02-WC-399) is kept under taxes and shipping, as the first pass read it, not under market selection. That leaves S02-VP-73 and S02-VP-74 `not covered`.
  - The channel readings: Point of Sale, Google, and the allowed countries as markets.
  - S02-WC-293 is noted rather than read with S02-WC-292.
  - S02-WC-334 to S02-WC-336 read together would say that a checkout field can follow the customer's billing country, which S02-V-913 already holds from S02-WC-344. They are noted, because rule 5's Lists need one identifier and theirs differ.
  - S02-WC-280 is noted, not placed under S02-VP-65 as the buyer's country, because the right of withdrawal is the law's, not a setting of the store.
  - Inbox notes are read as notifications to the merchant (S02-VP-89, S02-VP-90). The extensions suggested to the merchant are noted as (c)'s kinds.
- **Ids.** RD3-S1 wrote rows at the same time, so this part's new ids interleave with its own: S02-V-999 to S02-V-1056, not all of them this part's. The tool's lock kept the two parts' writes apart.
- **Leads placed under several points.** The revisits placed leads under every point they answer, so rows of points that have no WooCommerce task gained statements by a join, or gained a row: S02-VP-51, S02-VP-54, S02-VP-57 to S02-VP-62, S02-VP-70, S02-VP-89 and S02-VP-90. No row was replaced or removed outside a revisit.

## Second pass, RD3-S4: zid, bullets f and g

Zid's tasks in `b/second-pass/RD3/worklist.tsv`: 29 revisits, then 11 `place` tasks, in the list's order; revisits whose points share their leads were done together. Zid's statements are read as the first pass read them (Part RD3-3, 'How this part reads Zid's statements'): Zid's market is its 'السوق'; 'you', the merchant, an instruction to the merchant or a control of the dashboard is the seller; 'تلقائيًا' (automatically) or a default is the platform. Each row is compared with the statement in its point's `raised_by` from another platform (rule 5); `term` rests on Zid's own translations in `terms.tsv` or on mine, marked 'my translation'. Readings are marked in their rows.

### Revisits: rows replaced or removed, and what took their place

- S02-V-760 (S02-VP-44, was `not covered`): replaced by the seller (S02-ZD-258 to S02-ZD-260, S02-ZD-265; later joined by S02-ZD-214 and S02-ZD-221, the legal pages' and the store's content written again in English). The leads placed under other points they answer: S02-ZD-260 to S02-ZD-263 joined S02-V-759 (S02-VP-43, the whole store: 'Current language configured for the store.', 'List of languages supported by the store.', 'Returns the store languages', and 'تحديد اللغة الأساسية للمتجر', read as the first pass read the store's base currency); S02-ZD-260's 'تفعيل العملات' joined S02-V-755 (S02-VP-42, the seller); S02-ZD-265 ('Message Language', the language of marketing messages, plans growth and pro) joined S02-V-807 (S02-VP-83, the seller), a thing of two kinds, language and messages to buyers (rule 1).
- S02-V-761 (S02-VP-45, was `not covered`): replaced by the whole store, S02-ZD-231 under (g) ('لا يمكن تفعيل أكثر من نطاق في نفس الوقت.', my translation: 'more than one domain cannot be active at the same time'), `answers` alone (rule 4). S02-ZD-231 is also task 40's `place` under (g).
- S02-V-762 (S02-VP-46, was `not covered`): replaced by the seller (S02-ZD-229, S02-ZD-230, S02-ZD-232 to S02-ZD-236, S02-ZD-239, S02-ZD-240, S02-ZD-244 to S02-ZD-246, S02-ZD-424); added S02-V-1064, the platform (S02-ZD-246's default link, 'رابط المتجر سيكون الرابط الافتراضي'; S02-ZD-244's temporary link created at registration, a reading), and S02-V-1065, the staff permission `manage.store.custom.domain` (S02-ZD-241, rule 4).
- S02-V-774 (S02-VP-55, was `not covered`): replaced by `gap` S02-ZD-G10; no lead names a market, a buyer's country or the whole store for the checkout page's options. Its leads are placed under S02-VP-56.
- S02-V-775 (S02-VP-56, was `not covered`): replaced by the seller (S02-ZD-247 to S02-ZD-254; S02-ZD-248, S02-ZD-250 and S02-ZD-253 name no party, and are read with S02-ZD-247 as options of the same page's list, a reading; later joined by S02-ZD-281); added S02-V-1066, the platform (S02-ZD-251: 'الخاصية يتم تفعيلها بشكل تلقائي', the sign-in pop-up turned on automatically). S02-ZD-252's cash on delivery in guest checkout joined S02-V-784 (S02-VP-62, the seller).
- S02-V-787 (S02-VP-63, was `not covered`): replaced by the whole store, a reading of S02-ZD-208 ('اسم المؤسسة المستخدم في الفواتير', my translation: 'the establishment's name used in the invoices'): one name, used in the store's invoices.
- S02-V-788 (S02-VP-64, was `not covered`): replaced by the seller (S02-ZD-206, the disclosure in the store that Zid's Terms require of every merchant; S02-ZD-208, a field of the store's data, read as the merchant's control).
- S02-V-789 (S02-VP-65, was `not covered`): left `not covered`. No lead names a market, a buyer's country or the whole store for the exchange and return policy, and `why` names no gap; A2 recorded S02-ZD-G18 for the same legal pages under privacy ('the pages read name no market'), not for returns. Its leads are placed under S02-VP-66, or noted.
- S02-V-790 (S02-VP-66, was `not covered`): replaced by the seller (S02-ZD-213, S02-ZD-214, S02-ZD-216, S02-ZD-217, S02-ZD-219, S02-ZD-221). S02-ZD-214 and S02-ZD-221 also joined S02-V-760.
- S02-V-800 (S02-VP-76, was `not covered`): replaced by the whole store, a reading of S02-ZD-223 ('سيظهر العنوان الخاص الذي تم إضافة سابقاً في معلومات المتجر الأساسية', my translation: 'the address previously added in the store's basic information will appear'): the one address the invoice shows. S02-ZD-206 is placed under S02-VP-64; S02-ZD-224 and S02-ZD-226 are noted.
- S02-V-870 (S02-VP-85, was `not covered`): left `not covered`. Its one lead, S02-ZD-226, is the account's own information, noted; the work list's gap S02-ZD-G01 is not in RD3's slice, so it is under none of RD3's bullets and gives no `gap` row (rule 4).
- S02-V-791 (S02-VP-67, was `not covered`): replaced by a market, a reading of S02-ZD-280 (an inventory 'مع تخصيص قناة البيع لهذا المخزون إما زد كاشير أو للمتجر الإلكتروني', my translation: 'with the sales channel assigned to it, either Zid Cashier or the online store'; a sales channel is among what bullet (e) names as defining a market); added S02-V-1067 beside it, `gap` S02-ZD-G12, which asks what the inventory withdrawal priority takes its value per.
- S02-V-802 (S02-VP-78, was `not covered`): replaced by the seller (S02-ZD-270, S02-ZD-272, S02-ZD-274 to S02-ZD-277, S02-ZD-281 to S02-ZD-283, S02-ZD-286, S02-ZD-287). S02-ZD-281 (products available for pickup, an option of the checkout page) also joined S02-V-775.

### Statements noted (rule 2)

- S02-ZD-227 (f): defines the domain ('النطاق هو عنوان متجرك الإلكتروني', my translation: 'the domain is your online store's address'); names neither what it takes its value per nor who sets it
- S02-ZD-228 (f): an admin path to the domains list ('يمكنك الوصول إلى قائمة النطاقات من خلال : لوحة التحكم', my translation: 'you can reach the domains list through: Dashboard'); says where it is reached, not what it takes its value per or who sets it (as the first pass noted S02-ZD-105 and S02-ZD-141)
- S02-ZD-257 (f): says customers outside Saudi Arabia can pay electronically with Zid Pay 'بحسب الشبكات والعملات المفعلة' (my translation: 'according to the networks and currencies enabled'); names what the payment depends on, not a market, a buyer's country or the whole store, and not who sets it
- S02-ZD-207 (f): Zid's Terms require every store to give the consumer an invoice of the costs, the total price and the delivery's date and place ('ينبغي على كافة المتاجر والتجّار تقديم فاتورة إلى المستهلك'); names no business entity, and neither what a setting takes its value per nor who sets it
- S02-ZD-209 (f): the merchant authorizes Zid, through the Mazeed platform ('منصة مزيد'), as 'الممثل القانوني للبائع أمام الأطراف التجارية الأخرى' (my translation: 'the seller's legal representative before other commercial parties'): a term of the merchant's contract with Zid, of (c)'s kinds (the terms), not who sells to the buyer; names no market, buyer's country or whole store
- S02-ZD-224 (f): an order field's description ('Indicates whether the store business address is shown on printed invoices.'); names neither what the address takes its value per nor who sets it (as the first pass noted S02-ZD-052, an order field)
- S02-ZD-226 (f): the account's own information ('إعدادات الحساب > بيانات الحساب أو معلوماتك الأساسية', my translation: 'account settings > account data or your basic information'), to which the user can add an address: a setting of the account, not of the store (rule 1); names no country, market or buyer's country
- S02-ZD-212 (f): an admin path to the legal pages ('الاعدادات > المتجر > الصفحات القانونية'); says where they are reached, not what they take their value per or who sets them
- S02-ZD-215 (f): lists the legal pages (the privacy policy, terms and conditions, exchange and return policy, complaints and suggestions, licenses); names neither what they take their value per nor who sets them
- S02-ZD-218 (f): points Saudi stores to the Ministry of Commerce's regulations on e-commerce terms ('الرجاء مراجعة تنظيمات وزارة التجارة', my translation: 'please review the Ministry of Commerce's regulations'); names neither what a setting takes its value per nor who sets it: a regulator that requires a value isn't who sets it (rule 4)
- S02-ZD-222 (f): an order field's description ('Return policy applicable to the order.'); names neither a market, a buyer's country or the whole store, nor who sets it
- S02-ZD-269 (f): an admin path to the withdrawal priority ('يمكنك الوصول الى خاصية أولوية السحب من المخزون من خلال : لوحة التحكم'); says where it is reached, not what it takes its value per or who sets it
- S02-ZD-278 (f): an admin path to inventory transfer requests ('يمكنك الوصول الى خاصية نقل المخزون من خلال : لوحة التحكم'); says where it is reached, not what it takes its value per or who sets it
- S02-ZD-284 (f): an API field with no description ('fulfillment_priority: type: integer nullable: true'); names neither what it takes its value per nor who sets it
- S02-ZD-285 (f): an order field's description ('Inventory location(s) associated with the order.'); names neither what locations take their value per nor who sets them

## Second pass, RD3-S3: woocommerce, bullet g

WooCommerce's tasks under (g) in `b/second-pass/RD3/worklist.tsv`: 127 `place` tasks, then 7 rereads. This part had no revisit of its own; the six rows RD3-S2 left `not covered` were read against its statements under (g). Every row or join this part wrote rests on (g) and takes `answers` alone (rule 4). A statement under (g) is placed under the whole store of each `what "X" takes its value per` point whose kind its setting is of, and under that kind's `who sets` point where it also names who sets (rule 4).

How this part reads WooCommerce's statements under (g), beside the first pass's readings:
- **The whole store.** Words that one value holds for the store or the site ('site-wide', 'throughout the store', 'your store's', 'in your store', 'the site's timezone', 'the entire site'), and one option of the store's settings (an option id such as 'woocommerce_enable_guest_checkout'), read as one value for every buyer, as the first pass read 'the store holds one value'; a reading where the words don't say so, marked in the row. A value for each product or each email is read the same way where the words name it (S02-WC-346, S02-WC-373, S02-WC-396).
- **Not the whole store.** A statement that names only where a setting is reached, who handles a request, a party that can change a setting, or who a setting lets through, with no words that the setting holds for the whole store, is noted under (g) (rule 2).
- **Statements under (f) and (g).** The work list was cut before RD3-S2 ran, so most of this part's `place` tasks under (f) and (g) were already in one of RD3-S2's rows, which the checker counts as placed under (g) too. This part read each one's (g) half all the same: where its words say the setting holds for the whole store and RD3-S2 had placed it only under a `who sets` point, it joined the whole-store row; where they don't, it is noted under (g), and RD3-S2's placement stands.

### Revisits RD3-S2 left `not covered`

- S02-V-929 (S02-VP-63, who sells to the buyer): replaced by the whole store (S02-WC-274, S02-WC-275, S02-WC-277): the merchant sells to every customer, for all the products and services the store provides, and the platform is not party to it ('We’re not involved in your relationships or transactions with any customer or potential customer, and you’re solely responsible for all of your ecommerce activities'), a reading. Recorded with `done revisit S02-V-929 f`.
- S02-V-930 (S02-VP-64): still `not covered`. No statement under (g) names who sets who sells to the buyer: S02-WC-274's 'You have control over your store' names no setting of this kind, and its 'We’re not involved' names who is kept out (rule 5).
- S02-V-931 (S02-VP-65, returns and cancellations): replaced by the whole store (S02-WC-281, S02-WC-282, S02-WC-284, S02-WC-285): one order withdrawal feature for the store, whose form 'accepts requests for orders of any age', one constant window (`WITHDRAWAL_WINDOW_IN_DAYS`, `= 14;`), and one Refund and Returns Policy page 'to fit your store', a reading. Recorded with `done revisit S02-V-931 f`. Under S02-VP-66, S02-WC-282 and S02-WC-285 joined the seller (S02-V-932), and S02-V-1077 was added, the platform ('We have created a sample draft Refund and Returns Policy page for you', and the constant of S02-WC-281).
- S02-V-943, S02-V-944 (S02-VP-73, S02-VP-74, market selection): still `not covered`. No statement under (g) in this part says how a buyer's market is chosen, suggested, switched or restricted.
- S02-V-956 (S02-VP-86, apps): still `not covered`. S02-WC-418 (Show Suggestions) is the suggestions the platform shows the merchant, not the apps a store installs, as RD3-S2 read it; S02-WC-422 is the merchant's WooCommerce.com subscription, a setting of the platform's account, not of the store (rule 1). Both are noted below.

### `place` tasks: where the statements went

New rows, each the whole store unless said:
- S02-V-1078 (S02-VP-61, payment methods offered to buyers): S02-WC-266, 'customers from all over the world can use the gateway to check out and pay', a reading of the gateway as a payment method offered to buyers.
- S02-V-1079 (S02-VP-77, units and time zone): S02-WC-290 ('the weight unit used throughout the store'); S02-WC-288, S02-WC-289 and S02-WC-291, one option each and their defaults; S02-WC-310 and S02-WC-311, the site's timezone; S02-WC-312.
- S02-V-1080 (S02-VP-55, checkout and customer accounts): S02-WC-329 to S02-WC-333, S02-WC-338 to S02-WC-341. S02-WC-338 and S02-WC-339 share a source and an identifier, and are read together (rule 5, Lists).
- S02-V-1081 (S02-VP-56): the platform, the defaults of S02-WC-329, S02-WC-331 and S02-WC-332.
- S02-V-1082 (S02-VP-75, privacy and consent): S02-WC-441 to S02-WC-443, S02-WC-445, S02-WC-446, S02-WC-333, S02-WC-338, S02-WC-339.
- S02-V-1083 (S02-VP-47, products): S02-WC-346, S02-WC-348.
- S02-V-1084 (S02-VP-89, notifications to the merchant): S02-WC-430 to S02-WC-432.
- S02-V-1077 (S02-VP-66): the platform, above.

Joined to rows already there:
- S02-V-893 (S02-VP-41, the whole store): S02-WC-312, S02-WC-315.
- S02-V-900 (S02-VP-43, the whole store): S02-WC-312, S02-WC-324, S02-WC-325, and S02-WC-423 ('make sure emails are in the store language'), which RD3-S2 placed under messages to buyers.
- S02-V-946 (S02-VP-76, the whole store): S02-WC-312.
- S02-V-950 (S02-VP-80, the whole store): S02-WC-312, S02-WC-477, S02-WC-479, S02-WC-491 to S02-WC-495, S02-WC-501, S02-WC-502, S02-WC-504 to S02-WC-506.
- S02-V-909 (S02-VP-51, the whole store): S02-WC-362, S02-WC-366, S02-WC-368, S02-WC-373.
- S02-V-911 (S02-VP-53, the whole store) and S02-V-912 (S02-VP-54, the seller): S02-WC-376, the store notice, under storefront design as RD3-S2 placed S02-WC-375 and S02-WC-377.
- S02-V-914 (S02-VP-56, the seller): S02-WC-329 to S02-WC-333, S02-WC-338 to S02-WC-341.
- S02-V-1046 (S02-VP-84, the seller): S02-WC-333, S02-WC-338, S02-WC-339, S02-WC-441 to S02-WC-443, S02-WC-445, S02-WC-446.
- S02-V-933 (S02-VP-67, the whole store): S02-WC-395, S02-WC-396, stock management, under locations as RD3-S2 placed them.
- S02-V-952 (S02-VP-82, the whole store): S02-WC-386, S02-WC-387, S02-WC-426, S02-WC-428.
- S02-V-1038 (S02-VP-87, the whole store): S02-WC-401, S02-WC-404, S02-WC-411, S02-WC-412, S02-WC-440.
- S02-V-941 (S02-VP-71, the whole store): S02-WC-451, S02-WC-456, S02-WC-464.
- S02-V-932 (S02-VP-66, the seller): S02-WC-282, S02-WC-285.

Already under the whole store in RD3-S2's rows, so nothing was written for them: S02-WC-375 and S02-WC-377 (S02-V-911); S02-WC-408 (S02-V-1038); S02-WC-423 (S02-V-952); S02-WC-454, S02-WC-455, S02-WC-457 to S02-WC-462, S02-WC-471, S02-WC-472, S02-WC-474, S02-WC-475 (S02-V-941); S02-WC-476, S02-WC-478, S02-WC-480 to S02-WC-488, S02-WC-490, S02-WC-497, S02-WC-509 (S02-V-950).

By count: 69 placed by this part, 29 already under the whole store, 29 noted (below): 127.

### Rereads (rule 4, widened)

- Reread of S02-WC-017: placed. Joined the seller under S02-VP-42 (S02-V-896), S02-VP-52 (S02-V-910), S02-VP-58 (S02-V-918) and S02-VP-60 (S02-V-925): 'From your store’s general settings page, you can enter your business address', with 'select the currency', 'enable tax calculations and coupons' and 'define the regions you will sell and ship orders to'. RD3 has no `who sets` point for the business address or the store's country.
- Rereads of S02-WC-087, S02-WC-175, S02-WC-176 and S02-WC-179: placed. S02-V-1085 added under S02-VP-42, the seller ('Each WooCommerce store can set one base currency', the store read as its merchant; 'Choose', 'Specify').
- Rereads of S02-WC-177 and S02-WC-178: placed, under S02-V-1085, and S02-V-1086 added under S02-VP-42, the platform ('this is the default option').
- S02-V-1085 and S02-V-1086 give the answers of S02-V-896 and S02-V-897, and are kept apart from them, as each row's `note` says: a row that rests on a statement under (g) alone takes `answers` alone (rule 4), and the checker refuses one with `term`, which S02-V-896 and S02-V-897 take. S02-WC-017 is also under (a), (b) and (e), so it joined S02-V-896 and S02-V-918 themselves.

### Statements noted (rule 2)

- S02-WC-276 (g): 'must maintain fair and legally compliant return, refund, cancellation, and adjustment policies' names who maintains the return policies, as the terms require, without saying that they hold for the whole store; rule 4 places a statement under (g) under a `who sets` point only beside its whole-store answer
- S02-WC-283 (g): 'It’s up to you how withdrawal requests are handled' names who handles each withdrawal request, case by case, and what the platform doesn't do ('does not automatically change the order status, cancel the order, or issue a refund'), not a setting that holds for the whole store
- S02-WC-347 (g): the options of Catalog visibility, behind a filter; names neither what they take their value per nor that they hold for the whole store, as RD3-S2 noted it under (f)
- S02-WC-361 (g): the coupon types WooCommerce core offers ('fixed-cart, fixed-product, and percentage-based coupons'): the platform's, not a setting of the store that holds for the whole store
- S02-WC-364 (g): names who applies a coupon code, the customer, and who doesn't ('WooCommerce core does not apply coupon codes automatically'), not a setting that holds for the whole store
- S02-WC-379 (g): the Customize your store task 'opens a simplified design screen'; names where the merchant starts designing, not that the design holds for the whole store
- S02-WC-418 (g): Show Suggestions, one checkbox ('Leave this box unchecked if you do not want to pull suggested extensions from WooCommerce.com.', 'default' => 'yes'), which holds for the whole store and names who sets it; but the suggestions the platform shows the merchant are of none of rule 1's kinds of setting, and not the apps a store installs (S02-VP-86's kind), as RD3-S2 read it: a candidate for a new point (below)
- S02-WC-422 (g): one WooCommerce.com subscription key per production site: the merchant's account with the platform, not a setting of the store (rule 1), as RD3-S2 noted it under (f)
- S02-WC-425 (g): 'For each WooCommerce email listed, it’s possible to configure your settings (optional).': settings for each email, without saying what they take their value per or that they hold for the whole store
- S02-WC-444 (g): 'Personal data retention', one setting for the store ('Choose how long to retain personal data'), but of none of rule 1's kinds: privacy and consent holds cookie consent and the privacy settings shown to buyers, and the statement doesn't say that retention is shown to buyers: a candidate for a new point (below)
- S02-WC-447 (g): 'Use this section to decide how long your store keeps order data.': as S02-WC-444; 'make sure they comply with applicable laws, such as the EU GDPR' names a law that requires, not who sets (rule 4)
- S02-WC-452 (g): how a role is assigned to a user ('choose a role from the Role dropdown'); names who assigns it, as RD3-S2 placed it under S02-VP-72, not that staff access holds for the whole store
- S02-WC-453 (g): introduces two capabilities of the Administrator role (S02-WC-454 and S02-WC-455, under the whole store), without saying their scope
- S02-WC-463 (g): an extension or plugin can change what each role can do; names who changes it, as RD3-S2 placed it, not that staff access holds for the whole store
- S02-WC-465 (g): a plugin for editing role capabilities; names no scope
- S02-WC-466 (g): as S02-WC-465
- S02-WC-467 (g): as S02-WC-465
- S02-WC-468 (g): the roles the release's code creates ('customer', 'shop_manager'); names no scope
- S02-WC-469 (g): the code adds the core capabilities to two roles; names no scope
- S02-WC-470 (g): the capabilities 'are assigned to admin/shop manager during installation or reset'; names when, not their scope
- S02-WC-473 (g): the roles a shop manager may edit (by default 'customer'); names who may edit which roles, not the scope of staff access
- S02-WC-489 (g): a private link 'to provide selective access to your site' names who the mode lets through, as RD3-S2 noted S02-WC-507, not that the mode holds for the whole store
- S02-WC-496 (g): a guide for 'third-party developers and hosting providers' on integrating with the mode; names who integrates, not the mode's scope
- S02-WC-498 (g): the mode 'can be programmatically synced from a plugin or application'; names who may change it, not its scope
- S02-WC-499 (g): as S02-WC-498 ('a maintenance mode plugin')
- S02-WC-500 (g): as S02-WC-498 ('a hosting provider's coming soon mode')
- S02-WC-503 (g): exclusions that developers add, which bypass the mode 'on a specific IP address' or for 'a specific landing page': none of rule 4's four phrases, and not that the mode holds for the whole store
- S02-WC-507 (g): users with manage_woocommerce bypass the mode; names who the mode lets through, as RD3-S2 noted it under (f)
- S02-WC-508 (g): the exclusion filter woocommerce_coming_soon_exclude ('Defaults to false'); names whether a request is excluded, not that the mode holds for the whole store

By reason, 29 statements: 13 name a party that changes, assigns, integrates with or handles a setting, or who a setting lets through, without words that it holds for the whole store (S02-WC-276, S02-WC-283, S02-WC-452, S02-WC-463, S02-WC-473, S02-WC-489, S02-WC-496, S02-WC-498 to S02-WC-500, S02-WC-503, S02-WC-507, S02-WC-508); 9 name no scope or what a value is taken per (S02-WC-347, S02-WC-379, S02-WC-425, S02-WC-453, S02-WC-465 to S02-WC-470); 2 are the platform's own, not the store's (S02-WC-361, S02-WC-422); 1 names who applies a coupon (S02-WC-364); 3 are candidates for a new point (S02-WC-418, S02-WC-444, S02-WC-447).

### Candidates for a new point

The second pass adds no point. These statements under (g) answer one of its questions for an X that no point's kind fits, or that no point of their kind asks:
- **"Personal data retention"**, of none of rule 1's kinds (privacy and consent holds cookie consent and the privacy settings shown to buyers): what it takes its value per, the whole store (S02-WC-444, S02-WC-447, and S02-WC-339's 'decide how your store retains or removes personal data'); and who sets it, the seller ('Choose how long to retain personal data', 'Use this section to decide how long your store keeps order data').
- **"suggested extensions" (Show Suggestions)**, of none of rule 1's kinds: what it takes its value per, the whole store (one checkbox, S02-WC-418); and who sets it, the seller and the platform's default 'yes'. RD3-S2 listed its `who sets` half.
- **who sets the units and the time zone**, of the kind units and time zone (S02-VP-77 asks only what they take their value per): S02-WC-289 and S02-WC-291 ('you'), S02-WC-288 (the platform's default) and S02-WC-312 ('Set your store\'s address, visibility, currency, language, and timezone.'), whose whole-store half is under S02-V-1079. RD3-S2 listed them under (f).
- **who sets the store's address**, of the kind the store's address (S02-VP-76 asks only what it takes its value per): S02-WC-312, and S02-WC-017 ('you can enter your business address'), whose whole-store half is under S02-V-946.

### Words searched for

None: the second pass raises no point, so no search was run for the earlier platforms' rows.

### Problems with the brief or the tools

- **(g) and `who sets`.** Rule 4 places a statement under (g) under a `who sets` point only beside its whole-store answer, so statements under (g) that name who sets a setting without saying it holds for the whole store are noted (S02-WC-276, S02-WC-283). The coordinator may rule otherwise: S02-WC-276 would join the seller under S02-VP-66.
- **Rows with `term`.** A row that holds a statement under (g) alone must take `answers` alone, by the checker. The rereads' S02-WC-087 and S02-WC-175 to S02-WC-179 give the answers of S02-V-896 and S02-V-897, which take `answers;term`; joining them would have dropped `term`, which holds for those rows' statements under (f). So they have rows of their own (S02-V-1085, S02-V-1086), which leaves two rows of one answer each under S02-VP-42. The coordinator may merge them.
- **The work list and RD3-S2.** Most of this part's `place` tasks were already placed by RD3-S2 when this part ran (see above); the work list was cut before. Each was read for its (g) half.
- **Calls this part made that the coordinator may read otherwise.**
  - Who sells to the buyer read as the merchant, the same for every buyer, from terms that say the merchant is responsible for all its ecommerce activities and the platform isn't involved (S02-V-929).
  - The order withdrawal window, a constant that only sets when the merchant is warned of an order's age (S02-WC-284), read with the feature, its form and the policy page as returns and cancellations held for the whole store (S02-V-931).
  - One option of the store's settings, or one value for each product or each email, read as the whole store.
  - The gateway that customers 'from all over the world' can use (S02-V-1078), read as a payment method offered to buyers.
  - Personal data retention read as of none of rule 1's kinds (a candidate), though S02-WC-339 names it beside the privacy policy notices.
- **Ids.** RD3-S4 writes beside this part. This part's new rows are S02-V-1077 to S02-V-1086.
- **Correction to RD3-S3's count "By reason" above:** 10 of the noted statements name no scope or what a value is taken per (S02-WC-347, S02-WC-379, S02-WC-425, S02-WC-453, S02-WC-465 to S02-WC-470), not 9; the total, 29, stands.

## Second pass, RD3-S4: zid, bullets f and g (continued)

RD3-S3 appended its section above while this part ran; this part's notes continue here.

### Revisits, continued

- S02-V-792 (S02-VP-68, was `not covered`): replaced by `gap` S02-ZD-G11; its leads are placed under S02-VP-79.
- S02-V-803 (S02-VP-79, was `not covered`): replaced by the seller (S02-ZD-266 to S02-ZD-268, S02-ZD-206; S02-ZD-267 names no party, and is read with S02-ZD-266, a note of the same section, a reading). S02-ZD-266's store link also joined S02-V-762 (S02-VP-46, the seller).
- S02-V-797 (S02-VP-73, was `not covered`): replaced by `gap` S02-ZD-G13. The leads name the Region & Language popup's country and city, which their words don't name as a market (as S02-ZD-G13 reads them). S02-ZD-289 (the 'Display products in your store based on the customer location' switch) joined S02-V-764 (S02-VP-47, the buyer's country); S02-ZD-292 ('Know your customers' locations precisely to customize offers') gave S02-V-1068 under S02-VP-51, the buyer's country (a reading); S02-ZD-291 (the popup included in 'your theme') joined S02-V-773 (S02-VP-54, the seller, a reading). S02-ZD-288 and S02-ZD-290 are noted.
- S02-V-798 (S02-VP-74, was `not covered`): replaced by `gap` S02-ZD-G13. S02-ZD-289 joined S02-V-765 (S02-VP-48, the seller) and S02-ZD-292 joined S02-V-770 (S02-VP-52, the seller).
- S02-V-795 (S02-VP-71, was `not covered`): replaced by `gap` S02-ZD-G17; the leads give permissions per member or group, none per market, buyer's country or the whole store.
- S02-V-796 (S02-VP-72, was `not covered`): replaced by the seller (S02-ZD-319, S02-ZD-321, S02-ZD-322, S02-ZD-325, S02-ZD-331 to S02-ZD-333; S02-ZD-325 names no party, read as an option of the team section, a reading); added S02-V-1069, the store owner (S02-ZD-326, S02-ZD-327, S02-ZD-319, S02-ZD-331; rule 4, the account's owner), and S02-V-1070 beside them, `gap` S02-ZD-G17, which asks who sets a limit of permissions to a market. S02-ZD-332 also gave S02-V-1071 under S02-VP-62, the permission to turn the payment networks on or off (rule 4). S02-ZD-318 is placed under S02-VP-90.
- S02-V-799 (S02-VP-75, was `not covered`): replaced by `gap` S02-ZD-G18; its leads are placed under S02-VP-84 and S02-VP-83, or noted (S02-ZD-336).
- S02-V-808 (S02-VP-84, was `not covered`): replaced by the seller (S02-ZD-334, S02-ZD-335, S02-ZD-338, and the legal pages' privacy policy, S02-ZD-213, S02-ZD-214, S02-ZD-219); added S02-V-1072, the buyer (S02-ZD-335's opt-out, S02-ZD-337's unsubscribe), S02-V-1073, the platform (S02-ZD-339: the opt-out words recognized automatically, which can't be changed), and S02-V-1074 beside them, `gap` S02-ZD-G19, which asks about cookie preferences. The same leads under S02-VP-83 (messages to buyers): S02-ZD-338 and S02-ZD-344 joined S02-V-807 (the seller); S02-V-1075 added, the buyer (S02-ZD-337); S02-V-1076 added, the platform (S02-ZD-339).
- S02-V-801 (S02-VP-77, was `not covered`): replaced by `gap` S02-ZD-G21. Its lead S02-ZD-346 says the merchant chooses the time zone; no point asks who sets units or time zone, so it is noted.
- S02-V-804 (S02-VP-80, was `not covered`): replaced by `gap` S02-ZD-G20; its leads are placed under S02-VP-81.
- S02-V-805 (S02-VP-81, was `not covered`): replaced by the seller (S02-ZD-340 to S02-ZD-344; S02-ZD-343 names no party, read with S02-ZD-340 as an option of the same list, a reading); added S02-V-1087, the platform (S02-ZD-345: Zid's right under its Terms to stop the service and close the store). S02-ZD-344's text in Arabic and English also joined S02-V-760 (S02-VP-44), and its notice to customers when the store reopens S02-V-807 (S02-VP-83).
- S02-V-875 (S02-VP-86, was `not covered`): replaced by `gap` S02-ZD-G15. No lead names what apps take their value per (S02-ZD-G15: 'they name no market'); those that name who connects or manages apps answer a question no point asks of apps. All are noted.
- S02-V-879 (S02-VP-87, was `not covered`): replaced by `gap` S02-ZD-G14; its leads are placed under S02-VP-88, or noted (S02-ZD-299).
- S02-V-883 (S02-VP-88, was `not covered`): replaced by the seller (S02-ZD-293 to S02-ZD-298).
- S02-V-887 (S02-VP-89, was `not covered`): replaced by `gap` S02-ZD-G16; its leads are placed under S02-VP-90.
- S02-V-891 (S02-VP-90, was `not covered`): replaced by the seller (S02-ZD-313 to S02-ZD-317); added S02-V-1088, the staff permission `manage.store.staff.notifications` (S02-ZD-318, rule 4).

### `place` tasks: where the statements went

- S02-ZD-181 and S02-ZD-182 (the short national address required for shipments into Saudi Arabia, for customers' addresses there): joined S02-V-793 (S02-VP-69, the buyer's country). The Council of Ministers' decision S02-ZD-182 names requires the value without setting it (rule 4), so neither gives a row under S02-VP-70.
- S02-ZD-187 (the Region & Language popup): S02-V-1089 added under S02-VP-44, the buyer ('allows customers to change the store language'); S02-V-1090 added under S02-VP-49, the buyer's country ('pricing ... tailored to the selected region'); joined S02-V-764 (products), S02-V-781 (shipping: 'delivery options') and S02-V-772 (storefront design: 'content'), the buyer's country. The selected region is the country and city the customer selects, read as the first pass read the customer's location ('موقع العميل'). Its words don't name a market (S02-ZD-G13), so it is not placed under S02-VP-73 or S02-VP-74.
- S02-ZD-188 (the region popup settings managed on the inventory page): joined S02-V-765 (S02-VP-48, the seller), read with S02-ZD-189 as the lead-in of its list (rule 5, Lists).
- S02-ZD-189 ('By default, Display products in your store based on the customer location is disabled for all stores.'): joined S02-V-764 (S02-VP-47, the buyer's country, which the store switches on, rule 4); S02-V-1091 added under S02-VP-48, the platform ('By default').
- S02-ZD-399, S02-ZD-404 and S02-ZD-412 (Zid Payments' answers for Saudi Arabia and Kuwait: currencies turned on through the store's settings): joined S02-V-755 (S02-VP-42, the seller); their identifiers name the currencies (rule 5).
- S02-ZD-231, under (g): S02-V-761 (S02-VP-45, the whole store), with its revisit above.
- S02-ZD-191 and S02-ZD-447: noted.

### Statements noted (rule 2), continued

- S02-ZD-288 (f): the city a customer selects in the Region & Language popup, or 'a default city in the region that has a shipping option': its words don't name it as a market (as S02-ZD-G13 reads the popup), and it is of none of rule 1's kinds otherwise (listed below as a candidate for a new point)
- S02-ZD-290 (f): an API to 'change the store language, country, and city'; names no party that sets them, and no market (as S02-ZD-G13 reads the popup)
- S02-ZD-191 (f): the setRegion API ('Changes the store language, country, and city'); names no party that sets them, and no market (as S02-ZD-G13 reads the popup)
- S02-ZD-320 (f): an admin path to the team feature ('يمكنك الوصول الى خاصية الفريق من خلال : لوحة التحكم'); says where it is reached, not what it takes its value per or who sets it
- S02-ZD-328 (f): defines user roles and permissions ('User roles and permissions determine what a user can view, change, or manage in a store's setting'); names neither what staff access takes its value per nor who sets it
- S02-ZD-329 (f): a staff permission over the store's settings in general ('manage.store.settings Manage store settings'), of no one kind of setting (as RD3-3 noted S02-BC-097 to S02-BC-102)
- S02-ZD-330 (f): a staff permission over the apps' settings ('manage.app.market.settings Manage application settings'): S02-VP-86 asks only what apps take their value per, and no point asks who sets apps (listed below)
- S02-ZD-336 (f): Zid's own Privacy Policy, the rights it gives over personal information 'regardless of where you live': Zid's policy, not a setting of the store (rule 1)
- S02-ZD-346 (f): the merchant chooses the store's time zone ('يمكنك اختيار المنطقة الزمنية المناسبة', my translation: 'you can choose the suitable time zone'); S02-VP-77 asks only what units and time zone take their value per, and no point asks who sets them (listed below)
- S02-ZD-299 (f): the details added when creating a Google Analytics property ('يتم اضافة اسم الموقع ( المتجر ) والمنطقة الزمنية والبلد والعملة', my translation: 'the site's (store's) name, time zone, country and currency are added'), in the passive with no party: a setting of the Google Analytics property; names neither what web analytics takes its value per nor who sets it
- S02-ZD-300 (f): the merchant can connect any number of apps to the store ('يمكنك ربط العديد من التطبيقات ولا يوجد عدد محدد'); names no market, buyer's country or whole store (S02-ZD-G15), and no point asks who sets apps (listed below)
- S02-ZD-301 (f): the merchant views and manages the apps activated in the store ('يمكنك استعراض جميع التطبيقات المفعّلة في متجرك، مع إمكانية إدارتها'); names no market, buyer's country or whole store, and no point asks who sets apps (listed below)
- S02-ZD-302 (f): embedded apps, which the merchant controls in the App Market page ('التطبيقات التي يمكنك التحكم في التطبيق داخل صفحة سوق التطبيقات'); names no market, buyer's country or whole store, and no point asks who sets apps (listed below)
- S02-ZD-303 (f): defines Zid's App Market, apps and services of third parties independent of Zid; names neither what apps take their value per nor who sets them
- S02-ZD-304 (f): the merchant can connect the store to any app by its linking mechanism ('يمكنك ربط متجرك بأي تطبيق'); names no market, buyer's country or whole store, and no point asks who sets apps (listed below)
- S02-ZD-305 (f): lists the App Market's categories of apps; names neither what apps take their value per nor who sets them
- S02-ZD-306 (f): public apps, which 'All merchants on the platform can view, install, and benefit from': for whom apps are offered, (h)'s kind; names no market, buyer's country or whole store, and no point asks who sets apps (listed below)
- S02-ZD-307 (f): private apps, installed only 'by stores explicitly granted access': a value per store, none of rule 4's four phrases; no point asks who sets apps
- S02-ZD-309 (f): an app records the authorized store's connection, and 'Zid records the installation during token exchange': an installation per store, none of rule 4's four phrases (S02-ZD-G15); no point asks who sets apps
- S02-ZD-310 (f): tells app partners to disclose an app's 'eligibility, country, contract or verification prerequisites'; its country doesn't say whose (rule 2's role test), and it names neither what an app takes its value per nor who sets it
- S02-ZD-311 (f): defines Zid's App Market, a platform owned by Zid that links the merchant and the partner; names neither what apps take their value per nor who sets them
- S02-ZD-312 (f): the merchant agrees that the partner is the app's service provider, independent of Zid: a term of the merchant's contract, of (c)'s kinds (the terms), not a setting of the store; names neither what apps take their value per nor who sets them
- S02-ZD-447 (f): names the languages, currencies and international shipping Zid supports ('مع دعم لغات متعددة، عملات متنوعة، وشحن دولي', my translation: 'with support for many languages, various currencies and international shipping'); names neither what they take their value per nor who sets them

### Candidates for a new point

The second pass raises no point. These statements answer one of (f)'s questions for an X that no point's kind fits, or for a kind no point asks that question of:
- S02-ZD-213, S02-ZD-217, S02-ZD-219: X 'الشروط والأحكام', 'الشكاوى والاقتراحات', 'التراخيص' (my translation: 'terms and conditions', 'complaints and suggestions', 'licenses'), the store's legal pages other than its return and privacy policies; question: who sets them (the seller: 'يمكنك إدارة وتخصيص السياسات القانونية'). The statements are placed under S02-VP-66 and S02-VP-84 for their return and privacy policies.
- S02-ZD-288: X 'a default city in the region that has a shipping option', the city a customer selects in the Region & Language popup; question: who sets it (the customer; a default city otherwise). Noted.
- S02-ZD-346: X 'المنطقة الزمنية' (my translation: 'the time zone'), of S02-VP-77's kind (units and time zone); question: who sets it (the seller: 'يمكنك اختيار المنطقة الزمنية المناسبة'), which no point asks of that kind. Noted.
- S02-ZD-300 to S02-ZD-302, S02-ZD-304, S02-ZD-306 and S02-ZD-330: X 'التطبيقات' (apps), S02-VP-86's kind; question: who sets them (the seller: 'يمكنك ربط العديد من التطبيقات'; the permission 'manage.app.market.settings'), which no point asks of that kind. Noted.

### Candidates not placed

Each of these statements is placed under another point, or noted; these candidates are not placed:
- S02-ZD-258's 'وسيتم تحويلها تلقائيا' (my translation: 'and it will be switched automatically'): its words don't say what is switched, so it gives the platform no row under S02-VP-43 or S02-VP-44.
- S02-ZD-233's review by 'الفريق' (the team) of a request for a free domain: a review of the merchant's request, not who sets the domain (rule 4).
- S02-ZD-280's 'يتم إتاحة مخزون للعميل' (an inventory is made available) names no party, so it gives no row under S02-VP-78.
- S02-ZD-275's warehouse chosen for each order when it turns 'جاهز', S02-ZD-282's data per branch, S02-ZD-283's national address per warehouse in Saudi Arabia, and the permissions per member or group (S02-ZD-319 to S02-ZD-322) under S02-VP-71: values per order, location or member, none of rule 4's four phrases.
- S02-ZD-317's 'automatic notifications': the platform sends them, but the statement names the merchant as who sets them, so no platform row under S02-VP-90.
- S02-ZD-187's 'the store ... country, and city', changed by the customer: its words don't name a market (S02-ZD-G13), so no row under S02-VP-73 or S02-VP-74.

### Words searched for

None: the second pass raises no point, so no search for earlier platforms' rows was run.

### Problems with the brief, the work list or the tools

- **S02-ZD-G01 (S02-VP-85).** The work list names it among the A2 gaps for S02-VP-85, but it is not in RD3's slice (`slices/RD3/gaps.tsv`): it is under none of RD3's bullets, so it gives no `gap` row (rule 4: a gap under the same bullet), and S02-V-870 stays `not covered`. `method/variants_edit.py` would have taken it: it checks a gap's id against nothing.
- **S02-V-789 (S02-VP-65) stays `not covered`.** Gap-closing found leads for the point but recorded no gap, and no lead names a market, a buyer's country or the whole store for the return policy; S02-ZD-G18 asks this of the privacy policy on the same pages. The coordinator may want a gap recorded, or the leads read as the whole store.
- **Readings of the whole store.** S02-V-787 (the establishment's name used in the invoices, S02-ZD-208) and S02-V-800 (the address from the store's basic information that the invoice shows, S02-ZD-223) rest on readings of one value for the store, marked in their rows; gap-closing recorded no gap for these points. The coordinator may prefer `not covered` for them, as for S02-V-789.
- **A sales channel read as a market.** S02-V-791 reads S02-ZD-280's sales channel (Zid Cashier or the online store) as a market the store sells into, since bullet (e) names a channel among what defines a market; the first pass read only 'لكل سوق وقناة' so.
- **The Region & Language popup.** Its country and city are read as the buyer's country, not a market, as S02-ZD-G13 reads the popup; RD2's parts may read S02-ZD-187 and S02-ZD-191 (also under e) otherwise.
- **Ids.** This part's new rows are S02-V-1064 to S02-V-1076 and S02-V-1087 to S02-V-1091; S02-V-1077 to S02-V-1086 went to RD3-S2, which ran beside it.

## Second pass, the coordinator's merge (27 October)

- S02-V-1085 and S02-V-1086, which RD3-S3 gave their own rows under S02-VP-42 because the checker then wanted `answers` alone on any row holding a statement under (g), give the same answers as S02-V-896 (the seller) and S02-V-897 (the platform). Rule 4 keeps one answer in one row, so their statements joined those rows, with their evidence, and the two rows were removed. The checker and rule 4's (g) basis now say: a row resting only on statements under (g) takes `answers` alone; a row that also holds other statements lists every basis that holds, `answers` among them.

## Second pass, RD3-S6: salla, bullets f and g

Salla's tasks in `b/second-pass/RD3/worklist.tsv`: 12 revisits, then 22 `place` tasks under (f) and 33 under (g), in the list's order; the statements under (g) that answer a revisited point were placed with its revisit. Salla's statements are read as the first pass read them (Part RD3-2, 'How this part reads Salla's statements'). Under (g), as RD3-S3 read WooCommerce's: words that one value holds for the store ('your store', 'the store's', 'per store') and one option of the store's settings are read as the whole store, marked a reading where the words don't say so; a statement under (g) goes under a `who sets` point only beside its whole-store answer (rule 4); a row resting only on statements under (g) takes `answers` alone. Each statement joined to a row is compared with the statement in its point's `raised_by` from another platform (rule 5), and its own basis is given in the row's evidence. Where I compared it with a Salla statement already in the row (S02-SA-382 with S02-SA-278, S02-SA-389 with S02-SA-243), the row's bases were rechecked against `raised_by`, and stand.

### Revisits: rows replaced or removed, and what took their place

- S02-V-714 (S02-VP-63, was `not covered`): replaced by the whole store, from statements under (g): S02-SA-379 ('As a shopper, you buy from the store itself, not from Salla.'), S02-SA-381, S02-SA-380, S02-SA-377, and the terms of use's S02-SA-339, S02-SA-341 to S02-SA-344: the store, the merchant, sells to every buyer, and Salla is not party to the sale, a reading. Its four leads, S02-SA-345 to S02-SA-348, are noted.
- S02-V-715 (S02-VP-64, was `not covered`): replaced by the seller, S02-SA-344 under (g), beside its whole-store answer: the legal form or entity 'يتخذه التاجر أو المتجر' (my translation: 'that the merchant or the store takes'), a reading. The leads name no one who sets it.
- S02-V-716 (S02-VP-65, was `not covered`): replaced by the whole store, S02-SA-378 (the return experience 'تختلف ... من متجر لآخر', my translation: 'differs from one store to another', set out in the store's exchange and return policy page) and S02-SA-386 (the option 'Order cancellation' of the store's settings), both under (g), a reading; added S02-V-1092 beside it, `gap` S02-SA-G06, which asks whether the policy or the cancellation setting can take a value per market. The lead S02-SA-382 names the countries a store ships to and the payment methods it accepts, not returns: it joined S02-V-708 (S02-VP-59, the buyer's country), S02-V-709 (S02-VP-60, the seller) and S02-V-712 (S02-VP-62, the seller), where its Arabic counterpart S02-SA-278 stands.
- S02-V-717 (S02-VP-66, was `not covered`): replaced by the seller, S02-SA-378 (some stores let the buyer submit a return from the account, some ask for customer service: the stores as who sets it, a reading) and S02-SA-386 (a control of the store's settings), under (g).
- S02-V-731 (S02-VP-76, was `not covered`): left `not covered`. Its leads are not the store's address: S02-SA-421 is a branch's or warehouse's details ('Choose the country, address, postal code, street, and district.'), and S02-SA-425 the pickup location, 'where carriers will pick up orders' (rule 1: a location the statement says orders ship from is not the store's own). Both joined S02-V-734 (S02-VP-78, who sets locations: the seller). `why` names no gap.
- S02-V-732 (S02-VP-77, was `not covered`): replaced by the whole store, from statements under (g): S02-SA-431 and S02-SA-432 (bookings use Saudi Arabia time only), S02-SA-433 (an option of the store's settings for the order prep list's time zone, a reading) and S02-SA-435 (a product's weight unit, set for each product, the same for every buyer, a reading, as RD3-S3 read a value for each product). No lead under (f).
- S02-V-869 (S02-VP-85, was `not covered`): replaced by `gap` S02-SA-G11. Its five leads are noted: S02-SA-426 to S02-SA-429, a digital card product's 'store countries', several per product, whose role their words don't state; S02-SA-430, one store's observed settings.
- S02-V-874 (S02-VP-86, was `not covered`): replaced by the buyer's country, S02-SA-413 to S02-SA-415: one default app for the local SMS notifications to customers and another for the international ones, read as told apart by the customer's country (a reading); added S02-V-1093, the whole store (S02-SA-416 under (g): apps installed 'to your store', a reading), and S02-V-1094, `gap` S02-SA-G09. The same leads are messages to buyers too (rule 1: a setting of two kinds goes under both): added S02-V-1095 under S02-VP-82 (the buyer's country, as above), and joined S02-V-746 under S02-VP-83 (the seller). Leads S02-SA-409 to S02-SA-411 are noted.
- S02-V-878 (S02-VP-87, was `not covered`): replaced by the whole store, from statements under (g): S02-SA-406 ('Keep one container per store.'), S02-SA-405, and S02-SA-401 to S02-SA-404 (one Google Analytics account and data stream for the store's domain, a reading); and S02-SA-394 and S02-SA-395, the store's reports in its one base currency (a reading, as S02-V-1038 reads WooCommerce's Analytics). Added S02-V-1096 beside it, `gap` S02-SA-G08. No lead under (f).
- S02-V-882 (S02-VP-88, was `not covered`): replaced by the seller, S02-SA-401 to S02-SA-406 under (g), beside their whole-store answer. No lead under (f). S02-SA-407 (the pixel 'connected automatically') and S02-SA-408 are noted: neither says the pixel holds for the whole store.
- S02-V-886 (S02-VP-89, was `not covered`): replaced by the whole store, S02-SA-417 under (g), 'Turn all store notifications on or off.', read as the notifications to the merchant, as S02-SA-G10 describes the settings page (a reading); added S02-V-1097 beside it, `gap` S02-SA-G10. No lead under (f).
- S02-V-890 (S02-VP-90, was `not covered`): replaced by the seller, S02-SA-417 (a control of the store's settings). No lead under (f). S02-SA-418 to S02-SA-420 are noted.

### `place` tasks: where the statements went

Under (f):
- S02-SA-330 and S02-SA-331 (runs of one list: one source and identifier), S02-SA-333 and S02-SA-334 (the same): joined S02-V-730 (S02-VP-75, the buyer's country: the cookie banner by the visitors' regions); S02-SA-331, S02-SA-333 and S02-SA-334 also joined S02-V-749 (S02-VP-84, the seller).
- S02-SA-351, S02-SA-352, S02-SA-363, S02-SA-366, S02-SA-369: joined S02-V-705 (S02-VP-58, the seller) only. Their country ('the country the tax will be applied to', 'tax rates for other countries', 'Select a country', 'the selected country') isn't said to be whose, so none is placed under S02-VP-57 (rule 2's role test). S02-SA-369 ('Legal business name') is the text of the tax record's control, read as the first pass read the dashboard's controls.
- S02-SA-359: joined the market rows and the seller's rows of products (S02-V-684, S02-V-686), prices (S02-V-688, S02-V-689), storefront design (S02-V-696, S02-V-697) and taxes (S02-V-702, S02-V-705): 'controlling how the store appears, how products are priced, and what is available to buy and taxed in each market'.
- S02-SA-360, S02-SA-361, S02-SA-370: joined S02-V-702 (S02-VP-57, a market) and S02-V-705 (the seller).
- S02-SA-362, S02-SA-367, S02-SA-368: joined S02-V-703 (S02-VP-57, the buyer's country: the IOSS number 'applies to orders shipped to the EU'; S02-SA-362's 'selling to European Union countries' read the same way, a reading) and S02-V-705 (the seller).
- S02-SA-389: joined S02-V-677 (S02-VP-41, the buyer's country) and S02-V-679 (S02-VP-42, the platform: 'displayed automatically').
- S02-SA-396, S02-SA-397, S02-SA-399: joined S02-V-721 (S02-VP-69, the buyer's country); S02-SA-397 also S02-V-723 (S02-VP-70, the platform: 'change automatically'). S02-SA-396 and S02-SA-398 joined S02-V-700 (S02-VP-55, the buyer's country: identity fields at checkout, read as checkout's settings, as the first pass read S02-SA-247).
- S02-SA-365: noted.

Under (g):
- S02-SA-339, S02-SA-341 to S02-SA-344, S02-SA-377, S02-SA-379 to S02-SA-381: S02-V-714 (S02-VP-63, the whole store); S02-SA-344 also S02-V-715 (S02-VP-64, the seller).
- S02-SA-378, S02-SA-386: S02-V-716 (S02-VP-65, the whole store) and S02-V-717 (S02-VP-66, the seller).
- S02-SA-394, S02-SA-395, S02-SA-401 to S02-SA-406: S02-V-878 (S02-VP-87, the whole store); S02-SA-401 to S02-SA-406 also S02-V-882 (S02-VP-88, the seller).
- S02-SA-416: S02-V-1093 (S02-VP-86, the whole store).
- S02-SA-417: S02-V-886 (S02-VP-89, the whole store) and S02-V-890 (S02-VP-90, the seller).
- S02-SA-431 to S02-SA-433, S02-SA-435: S02-V-732 (S02-VP-77, the whole store).
- S02-SA-340, S02-SA-407, S02-SA-408, S02-SA-418 to S02-SA-420, S02-SA-434, S02-SA-436: noted.

### Statements noted (rule 2)

- S02-SA-345 (f): an area of partnership that the salla-crossborder page lists for merchants expanding outside Saudi Arabia (its scope), 'المدفوعات و البيع بالنيابة (MoR)' (my translation: 'payments and selling on behalf (MoR)'), which collects payments and manages taxes and obligations 'في السوق المستهدف' (my translation: 'in the target market'): an area of partnership, not a setting of the store (rule 1); it says neither what who sells to a store's buyer takes its value per nor who sets it
- S02-SA-346 (f): as S02-SA-345, in English ('Areas of partnership we are looking for', its scope): 'Payments and Merchant of Record (MoR) Collect payments, and manage taxes, settlements, and financial obligations in the target market.'
- S02-SA-347 (f): as S02-SA-345, for global brands entering Saudi Arabia (its scope): 'حلول في التحصيل والتسويات، وادارة الضرائب والالتزامات المحلية' (my translation: 'solutions in collection and settlements, and the management of taxes and local obligations'); names no market, buyer's country or whole store, and no one who sets it
- S02-SA-348 (f): as S02-SA-347, in English: 'Solutions in collection and settlements, and tax and local compliance management.'
- S02-SA-365 (f): the tax types the tax record lists ('Value added tax (VAT)' to 'Profit Margin Tax'); names neither what a tax takes its value per nor who sets it
- S02-SA-409 (f): the supported countries of an app's listing in the Partners portal (its scope), which the app's partner sets ('Select specific countries, or leave empty to support all'): a setting of an app's listing, not of the store (rule 1); its 'target countries' don't say whose country, the store's own or a market's (S02-SA-G09 asks it)
- S02-SA-410 (f): the countries the Partners portal offers an app's listing ('SA +966 السعودية Saudi Arabia' to 'JO +962 الأردن Jordan'): not a setting of the store; names neither what it takes its value per nor who sets it
- S02-SA-411 (f): a filter's label in the apps list ('"supported_countries":"Supported countries"'); names no value, what it is taken per, or who sets it
- S02-SA-426 (f): a digital card product's codes by 'store country' ('Click + New Value to add a store country.'): a product holds several ('Store countries ({{count}}/{{max}})', S02-SA-429) with a default among them (S02-SA-427), so not the one country a store holds as its own (S02-VP-85's role), and the statement doesn't say whose country it is (rule 2's role test); it names the seller as who adds them, but no point's kind fits a product's codes: a candidate for a new point (below)
- S02-SA-427 (f): as S02-SA-426: 'You can set a default country or remove unused options.'; a candidate for a new point (below)
- S02-SA-428 (f): a digital card product's codes 'not linked to a specific country' ('Enter codes that are not linked to a specific country.'): the seller enters them, but no point's kind fits a product's codes, and it names no market, buyer's country or whole store: a candidate for a new point (below)
- S02-SA-429 (f): a header counting a digital card product's store countries ('Store countries ({{count}}/{{max}})'); names neither what they are taken per nor who sets them
- S02-SA-430 (f): one store's settings, as its storefront at https://sa.aldakheeloud.com/en/ returns them ('"store_country": "SA", "country": "SA"'): one value, not what it is taken per or who sets it (as the first pass noted S02-SA-252); S02-SA-G11 asks whether a market holds a country of its own
- S02-SA-340 (g): the legal capacity that the establishment, company or other legal form the merchant registers as must have ('يجب أن تتوافر فيه الأهلية القانونية والنظامية والشرعية اللازمة', my translation: 'must have the necessary legal, regulatory and lawful capacity'): a requirement on the business, not that who sells to the buyer, or another setting, holds for the whole store
- S02-SA-407 (g): 'The pixel, the Conversions API and your product catalog are all connected automatically when you link your account.' names who connects the pixel, the platform, not that it holds for the whole store; rule 4 places a statement under (g) under a `who sets` point only beside its whole-store answer
- S02-SA-408 (g): 'Choose the pixel you want, then click (Continue).' names who chooses the pixel, the seller, not that it holds for the whole store
- S02-SA-418 (g): the headers of the Notifications settings' table ('Email', 'App notifications'): a notification's channels, not that its value holds for the whole store, and not who sets it
- S02-SA-419 (g): a staff permission, 'store notification settings management': who may manage the store's notification settings, not that they hold for the whole store; rule 4 places a statement under (g) under a `who sets` point only beside its whole-store answer
- S02-SA-420 (g): the merchant app's notifications of orders' statuses and the platform's updates ('استقبل إشعارات مباشرة على جوالك أو جهازك اللوحي', my translation: 'receive direct notifications on your phone or tablet'): what the merchant receives, not that a setting holds for the whole store, or who sets it
- S02-SA-434 (g): the weight units offered ('"g":"Gram","kg":"Kilogram","lb":"Pound","oz":"Ounce"'): the options of a product's weight unit, not that one holds for the whole store
- S02-SA-436 (g): 'Default product weight for shipping', one setting of the store's, which holds for the whole store (a reading); but a product's default weight is of none of rule 1's kinds, and neither a unit nor a time zone (S02-VP-77's kind): a candidate for a new point (below)

### Candidates for a new point

- S02-SA-426, S02-SA-427 and S02-SA-428 (f): X, a digital card product's codes ('Codes by store country' and 'General codes', their identifiers); the question they answer, `who sets "X"`: the seller ('Click + New Value to add a store country.', 'You can set a default country or remove unused options.', 'Enter codes that are not linked to a specific country.'). They also take the codes per 'store country', several per product, without saying whose country that is, so they answer no `what "X" takes its value per` in rule 4's four phrases. No kind of rule 1 fits a product's codes: products holds which products are offered, and in what order.
- S02-SA-436 (g): X, 'Default product weight for shipping'; the question it answers, `what "X" takes its value per`: the whole store (one setting of the store's, a reading). Neither a unit nor a time zone (S02-VP-77's kind), nor shipping's zones, rates, options or carriers.

### Words searched for

None. Every task named its statements, each was printed by id, and no point was raised, so no earlier platform's rows were searched for.

### Problems with the brief, the work list or the tools

- **Revisits with no lead under (f).** For S02-VP-77 and S02-VP-87 to S02-VP-90, `why` names no lead under (f), only statements under (g) with their own `place` tasks. Their `not covered` rows were replaced from those statements, since a `not covered` row never stands beside another row of its platform; each outcome is recorded with `done`.
- **A lead of another point.** S02-SA-382, the only lead the work list names for S02-VP-65 and S02-VP-66, names shipping countries and payment methods, not returns; it was placed where its Arabic counterpart S02-SA-278 stands.
- **(g) and who sets.** A statement under (g) whose words name who sets but not the whole store is noted, as RD3-S3 noted S02-WC-276 (rule 4 places it under a `who sets` point only beside its whole-store answer). So S02-SA-407's platform ('connected automatically') and S02-SA-419's staff permission are in no row of S02-VP-88 or S02-VP-90, though the statements state them. The coordinator may want to rule.
- **Readings of kind.** 'local' and 'international' SMS (S02-SA-413 to S02-SA-415) are read as the customer's country, and the default SMS app as of two kinds, apps (S02-VP-86) and messages to buyers (S02-VP-82, S02-VP-83); both readings are mine. The pickup location (S02-SA-425) is read as a location that fulfils orders (S02-VP-78), not as shipping.

## Second pass, RD3-S7: salla and woocommerce, bullet g

Fourteen `reread` tasks, the last fourteen rows of the work list: statements under (g) that RD3-S3 and RD3-S6 noted because rule 4 then placed a statement under (g) under a `who sets` point only beside its whole-store answer. Rule 4 as widened on 27 October 2026 places a statement under (g) that names who sets, changes or may manage a setting of the store under that setting's `who sets "X"` point. Each task is recorded in `done.tsv`. The earlier notes stay as they are.

### Rereads placed: new rows
- S02-SA-407: S02-V-1098, a new row under S02-VP-88 (who sets "web analytics"), the platform: 'The pixel, the Conversions API and your product catalog are all connected automatically when you link your account.' ('automatically', rule 4). Its 'when you link your account' names the merchant's linking of the Meta account, not who connects the pixel. Its 'your product catalog' is not placed under S02-VP-48 (products): the statement names the catalog's connection to Meta, not which products the store offers or their order. Listed below as a candidate.
- S02-SA-419: S02-V-1099, a new row under S02-VP-90 (who sets "internal notifications"), a staff permission: 'store notification settings management', of the staff permission group 'إعدادات المتجر'. Rule 4: a staff permission that the statement says gates it is its own answer, beside the seller's (S02-V-890). A reading: the settings it gates are read as those of the settings page Notifications (S02-SA-417: 'Turn all store notifications on or off.'), by the same words 'store notification'.

### Rereads placed: joined to a row
- S02-SA-408: joined S02-V-882 (S02-VP-88, the seller): 'Choose the pixel you want, then click (Continue).', an instruction to the merchant.
- S02-WC-276: joined S02-V-932 (S02-VP-66, the seller): 'must maintain fair and legally compliant return, refund, cancellation, and adjustment policies', under its identifier 'Your responsibilities'. The terms require the policies, and a party that requires a value isn't who sets it (rule 4). This is the placement RD3-S3 named for the coordinator.
- S02-WC-283: joined S02-V-932 (S02-VP-66, the seller), a reading: 'It’s up to you how withdrawal requests are handled', read as who manages the store's returns and cancellations. Its 'does not automatically change the order status, cancel the order, or issue a refund' names what the platform doesn't do, so it gives no row of the platform.
- S02-WC-473: joined S02-V-1049 (S02-VP-72, the platform): the code sets the roles a Shop Manager may edit, apply_filters( 'woocommerce_shop_manager_editable_roles', array( 'customer' ) ), and leaves 'administrator' out of them for a user without the administrator role. A value the code sets is the platform's (rule 4), and the filter alone names no party. It was already in S02-V-1051 (the Administrator role), from (f). The Shop Manager role gets no row: its editable roles, 'customer' by default, name what it is kept out of, not staff access it sets.

### Rereads placed by rows they already held, from (f)
Each of these is under (f) and (g). RD3-S2 placed it under (f) in rows of the `who sets` point that the widened rule places it under for (g). No row changed.
- S02-WC-364: S02-V-1010 (S02-VP-52, the buyer): 'Customers enter the code at cart or checkout to receive the discount'. Its 'Send your coupon code to customers' names who sends the code, not who sets the discount, as RD3-S2 read it.
- S02-WC-452: S02-V-942 (S02-VP-72, the seller).
- S02-WC-463: S02-V-942 (the seller) and S02-V-1050 (an extension or plugin), under S02-VP-72.
- S02-WC-489: S02-V-951 (S02-VP-81, the seller): 'for you to provide selective access to your site'.
- S02-WC-496: S02-V-1055 (a hosting provider) and S02-V-1056 (developers), under S02-VP-81.
- S02-WC-498: S02-V-1054 (S02-VP-81, another plugin or application).

### Rereads left noted (rule 2)
- S02-WC-418 (g): Show Suggestions names who sets it, the seller by its checkbox ('Leave this box unchecked if you do not want to pull suggested extensions from WooCommerce.com.') and the platform by 'default' => 'yes'; but the suggestions the platform shows the merchant are of no point's kind, and not the apps a store installs (S02-VP-86's kind), as RD3-S2 and RD3-S3 read it, and RD3 has no `who sets` point for apps: a candidate for a new point (below)
- S02-WC-507 (g): 'if ( current_user_can( 'manage_woocommerce' ) ) { return false;' names who the coming soon mode lets through, not who sets, changes or may manage the mode, as RD3-S2 and RD3-S3 read it

### Candidates for a new point
- **who sets "suggested extensions"** (Show Suggestions: 'pull suggested extensions from WooCommerce.com'), S02-WC-418: the seller (its checkbox) and the platform ('default' => 'yes'). Of none of rule 1's kinds. RD3-S2 and RD3-S3 listed it too.
- **who sets "your product catalog"** (its connection to Meta), S02-SA-407: the platform ('connected automatically when you link your account'). The statement is placed under S02-VP-88 for the pixel and the Conversions API. The catalog's connection is read as of no point's kind, since the statement names neither which products the store offers nor their order (S02-VP-48's kind). Read as of the products kind, it would be a new row of S02-VP-48 (salla, the platform).

### Words searched for
- In the slice's `terms.tsv`, for Salla: 'pixel', 'notification', 'إشعار', 'تنبيه'. None found.
- Points' rows read: S02-VP-83 and S02-VP-87 to S02-VP-90 (salla); S02-VP-52, S02-VP-65, S02-VP-66, S02-VP-72 and S02-VP-81 (woocommerce).
- x_words added: S02-VP-88, salla, 'Meta pixel; Conversions API'; S02-VP-90, salla, 'store notification settings'; S02-VP-66, woocommerce, 'return, refund, cancellation, and adjustment policies; withdrawal requests'.

### Problems with the brief, the work list or the tools
- Six of the fourteen rereads (S02-WC-364, S02-WC-452, S02-WC-463, S02-WC-489, S02-WC-496, S02-WC-498) were already in rows of the point that their (g) reading answers, placed there under (f) by RD3-S2. Their reread changed no row. S02-WC-473 was also already in one, and joined one more.
- S02-WC-489 and S02-WC-507 both concern who the coming soon mode lets through. RD3-S2 placed S02-WC-489 in the seller's row by its 'for you to provide selective access to your site', and noted S02-WC-507. This part keeps both readings: in S02-WC-489 the merchant provides the access; S02-WC-507's capability names whom the mode doesn't apply to.

## Second pass, RD3-S8: the two new who-sets points, S02-VP-91 and S02-VP-92, and rereads under (f) and (g)

The 26 tasks of the coordinator's rulings when the parts ended (`b/second-pass.md`): a row for every platform under S02-VP-91 and S02-VP-92, and 24 rereads. No row was replaced or removed, and no statement was noted.

### New rows: S02-VP-91, who sets "measurement and weight units, and time zone" (S02-VP-77's twin)
- S02-V-1100, shopify, the seller: S02-SH-246 (under (g): 'Store defaults: Manage your default currency, currency formatting, measurement and weight units, and time zone in this section.'), S02-SH-345 and S02-SH-398 (the section's controls in the store's admin: 'Unit system', 'Default weight unit', 'Time zone'), from S02-VP-77's row S02-V-675. S02-SH-345's 'user level time zone' is a setting of the user's account, not of the store (rule 1), and is not read as X.
- S02-V-1101, salla, the seller: S02-SA-433 (the order prep list's setting 'Use Saudi Arabia time zone'), from S02-V-732.
- S02-V-1102, salla, no one can: S02-SA-431 ('Is there an option to add a time zone?': 'Not yet.') and S02-SA-432 ('Can I set a custom time zone?'), booking products, from S02-V-732. A reading: the statements say the store has no option to set the bookings' time zone, and name no party that sets it.
- S02-V-1103, zid, the seller: the reread S02-ZD-346.
- S02-V-1104, woocommerce, the seller: the rereads S02-WC-289 and S02-WC-291 ('This controls what unit you will define weights in.', '... lengths in.') and S02-WC-312 ('Set your store\'s address, visibility, currency, language, and timezone.').
- S02-V-1105, woocommerce, the platform: the rereads S02-WC-244 and S02-WC-292 (onboarding sets the units from a country's locale info, with the store's location) and S02-WC-288 (the settings' defaults are the units of 'US').
- S02-V-1106, bigcommerce, the seller: S02-BC-165, S02-BC-253, S02-BC-256 and S02-BC-285, from S02-V-860 and S02-V-983, and the reread S02-BC-257.
- S02-V-1107, bigcommerce, the Edit Channels permission: the reread S02-BC-257.
- S02-VP-77's statements read and not placed under S02-VP-91, as they name no one who sets, changes or may manage the setting: S02-SA-435, S02-BC-109 ('can be customized'), S02-BC-168, S02-BC-292, S02-WC-290, S02-WC-310, S02-WC-311.
- No platform needed the search under (f) and (g): each had an answer from the rereads or from S02-VP-77's rows.

### New rows: S02-VP-92, who sets "apps" (S02-VP-86's twin)
- S02-V-1108, shopify, the seller: S02-SH-767 ('When you install an app that has app pixels') and S02-SH-946 ('After you install the Shopify Messaging app'), found by the search.
- S02-V-1109, shopify, the staff permission 'Manage and install apps and channels': S02-SH-766, found by the search. A reading: the statement names the permission that gates managing an app's pixels, and the permission's own name is to manage and install apps. S02-SH-766 is also under S02-VP-88 (S02-V-1033).
- S02-V-1110, salla, the seller: S02-SA-413 to S02-SA-415 (the default apps for SMS, from S02-V-874) and S02-SA-416 ('where you browse and install apps', from S02-V-1093).
- S02-V-1111, zid, the seller: the rereads S02-ZD-300 to S02-ZD-302, S02-ZD-304 and S02-ZD-306.
- S02-V-1112, zid, the staff permission manage.app.market.settings: the reread S02-ZD-330, read as a permission from its source, Zid's page on user roles and permissions.
- S02-V-1113, woocommerce, the seller: S02-WC-025 (under (g): 'you will need to add a multi-currency extension/plugin') and S02-WC-415 ('you can pick another extension'), found by the search.
- S02-V-1114, bigcommerce, `not covered` (below).
- S02-VP-86's statements read and not placed under S02-VP-92, as they name no one who installs or manages apps: S02-SH-091, S02-BC-147.

### Rereads placed: joined to a row
- S02-WC-444 and S02-WC-447 (g), personal data retention: S02-V-1082 (S02-VP-75, the whole store) and S02-V-1046 (S02-VP-84, the seller). S02-WC-339 (g) was already in both rows, which give its retention words the same answers; their evidence now names retention.
- S02-ZD-213, S02-ZD-217 and S02-ZD-219 (f), the store's legal pages: S02-V-773 (S02-VP-54, the seller). None of them names a market, a buyer's country or the whole store, so none answers S02-VP-53.
- The rereads under S02-VP-91 and S02-VP-92 are in the new rows above.

### `not covered` rows
- S02-V-1114 (S02-VP-92, bigcommerce): S02-BC-147 says apps 'are installed at the store level' and names no one who installs them, and the search found no other statement. For gap-closing.

### Candidates for a new point
None.

### Words searched for
- **S02-VP-92**, in the (f) and (g) statements of shopify, bigcommerce and woocommerce: 'app', 'apps', 'app store', 'app market', 'extension', 'plugin', 'install', 'marketplace', 'تطبيق', and for woocommerce 'activate'. Read and not placed under it:
  - shopify: S02-SH-654 ('you need an app') and S02-SH-958 ('consider using a third-party app'), an app the seller needs or uses, not who installs or manages it; S02-SH-744, S02-SH-790 and S02-SH-796, a sales channel or Inbox installed, which they don't call an app; S02-SH-729 and S02-SH-768 to S02-SH-771, the pixels' settings, under S02-VP-88; S02-SH-844, S02-SH-846, S02-SH-862, S02-SH-910, S02-SH-913 and S02-SH-943, apps as locations or as who sets them; and the others the search found, where 'app' is the Shopify app, the Shop app, Translate & Adapt's work, or the business entity used for apps (S02-SH-399 to S02-SH-401).
  - woocommerce: S02-WC-463 ('you can use an extension or plugin to adjust permissions'), using one, as above; S02-WC-418, left noted by the coordinator's ruling; the extensions the platform suggests or recommends by the store's country (S02-WC-001 to S02-WC-003, S02-WC-061, S02-WC-205, S02-WC-416, S02-WC-417, S02-WC-419, S02-WC-420, S02-WC-434), what the platform shows the merchant, as that ruling reads S02-WC-418; S02-WC-436, S02-WC-449 and S02-WC-464 to S02-WC-467, what an extension does; S02-WC-498 to S02-WC-502, a plugin as who sets coming soon mode; S02-WC-024, S02-WC-326, S02-WC-481 and S02-WC-492, WooCommerce itself installed.
  - bigcommerce: S02-BC-174, S02-BC-175, S02-BC-179 and S02-BC-326 (the Catalyst app, the storefront's own), S02-BC-268 (the Theme Marketplace).
- In the slice's `terms.tsv`: 'time zone', 'timezone', 'weight', 'app', 'تطبيق', 'المنطقة الزمنية', 'extension', 'plugin', 'الصفحات القانونية', 'الشروط والأحكام'. Found: zid's 'سوق تطبيقات زد' ('Zid App Market'), 'تطبيقاتي', 'التطبيقات المدمجة', 'Public apps', 'Private apps', 'المنطقة الزمنية', 'الصفحات القانونية'; woocommerce's 'Weight unit'; bigcommerce's 'Localization settings'.
- In the five platforms' gaps under (f), the same words: none asks who sets the units, the time zone or apps. S02-ZD-G15, S02-ZD-G21 and S02-SA-G09 ask what they take their value per. S02-WC-G05 asks whether the platform applies the per-country units or the seller chooses; S02-V-1104 and S02-V-1105 give both, so no `gap` row stands beside them.
- `term` rests on the same words, or on a translation, marked in `basis_evidence` (rule 0): zid's own ('سوق تطبيقات زد': 'Zid App Market', so 'تطبيقات' is 'App'), or mine ('المنطقة الزمنية': 'the time zone').
- x_words added: S02-VP-91, salla 'Use Saudi Arabia time zone; custom time zone', zid 'المنطقة الزمنية', bigcommerce 'date and timezone settings; standard dimension and date and time formats'; S02-VP-92, shopify 'app; Shopify Messaging app', zid 'التطبيقات; تطبيقاتي; التطبيقات المدمجة; Public apps; application settings', woocommerce 'extension; plugin; multi-currency extension/plugin'; S02-VP-75 and S02-VP-84, woocommerce 'Personal data retention'; S02-VP-54, zid 'الصفحات القانونية; الشروط والأحكام; الشكاوى والاقتراحات; التراخيص'.

### Problems with the brief, the work list or the tools
- The message that started this part arrived as the literal text `$(cat .../b2-parts/RD3-S8.txt)`, unexpanded; the part read that file for its tasks.
- Rule 5 lets a statement's identifier or scope name what fills X, but not its source. S02-ZD-330's words, identifier and scope don't say it is a permission; only its source does. S02-V-1112 rests on that, as a reading.
- `method/variants_edit.py` has a `rownote` command its usage doesn't list, and its usage doesn't say that `join` with a statement the row already holds adds only the evidence.

### After the check (RD3-S8)
- S02-V-1100, S02-V-1101 and S02-V-1102 replaced, keeping their answers and statements: each rests only on statements under (g), so each takes the basis `answers` alone (rule 4, (g), Basis), where they first gave `answers;term`. The checker named S02-V-1101 and S02-V-1102; S02-V-1100's statements also carry RD1's or RD2's bullets, but under RD3 they are (g)'s alone.
- The checker found that the questions of S02-VP-91 and S02-VP-92 quote an X from none of their `raised_by` statements (rule 3). This part added to `raised_by`, with a line in each point's `note`: S02-SH-246 to S02-VP-91, the statement its question quotes ('measurement and weight units, and time zone'), placed in S02-V-1100; and S02-ZD-306 to S02-VP-92, a statement of the raising platform that holds 'apps' ('All merchants on the platform can view, install, and benefit from these apps.'), placed in S02-V-1111. The coordinator may prefer another; the questions are as the coordinator wrote them.
- With S02-SH-246 in S02-VP-91's `raised_by`, S02-V-1103 (zid) was compared with it again (rule 5) and replaced with the basis `answers;term`: Zid's 'المنطقة الزمنية' (my translation: 'the time zone') and Shopify's 'time zone'.

## Second pass, RD3-S10: zid, woocommerce, bigcommerce and shopify, bullets f and g, the last round's tasks

The work list's rows whose `why` begins 'last round' (after A2-T, A2-SH-H, A2-SA-H, A2-SA-S and A3-2), for these four platforms under (f) and (g): eight revisits and eleven `place` tasks.

### Revisit S02-V-1114 (bigcommerce, S02-VP-92, who sets "apps"): was `not covered`
- Replaced S02-V-1114 with the seller: 'you can access app details, apply updates, and uninstall apps' at Apps › My apps in the control panel (S02-BC-355).
- Added S02-V-1115, the store owner, the account's owner, its own answer (rule 4), as S02-V-971 holds it for bigcommerce (S02-BC-352, S02-BC-358); S02-V-1116, the Install applications permission (S02-BC-352, S02-BC-356, S02-BC-358); S02-V-1117, the Uninstall applications permission (S02-BC-353, S02-BC-357). Two permissions with different names are different answers (rule 4).
- `place` tasks S02-BC-352, S02-BC-353, S02-BC-355, S02-BC-356 and S02-BC-357 under (g): placed by the same rows, by rule 4, (g): each names who sets, changes or may manage the store's apps. None of them says that apps hold for the whole store, so none joins S02-VP-86; S02-V-876 already holds bigcommerce's answer there (S02-BC-147).
- S02-BC-354 (f, g): it names who may launch an installed app ('To launch apps, you must be the store owner, have the Launch applications permission, or have been granted access to a multi-user Single Click App'), which in its words sets, changes or manages none of the store's apps or their settings.
- S02-BC-358 is under (e) too: RD2's, left.

### Revisit S02-V-662 (shopify, S02-VP-69, the buyer's address form): was `gap` (S02-SH-G06)
- Replaced S02-V-662 with `gap` S02-SH-G11, which A2-SH-H wrote 'in place of S02-SH-G06': the form for buyer countries other than the United States, Canada, the United Kingdom and Yemen.
- Joined S02-SH-1007 to S02-SH-1010, S02-SH-1012, S02-SH-1013 and S02-SH-1015 to S02-SH-1018 (the held checkouts' address forms, and the checkout's CountryDetails answers for 'US' and 'CA') to S02-V-660, the buyer's country: 'State' and 'ZIP code' for the United States, 'Province' and 'Postal code' for Canada, 'Postcode' and no state for the United Kingdom, and, in the same store as Canada's form (capture-plus), neither for Yemen.
- The earlier leads S02-SH-647 to S02-SH-688 stay as the earlier revisit of this row placed or noted them: each is in a row or noted under (f).
- S02-SH-1011 (f): the countries one store's checkout offers in its Country/Region field ('option "United States" [selected]'), seen once; it shows no value that differs by a market or a country, or that holds for the whole store, and names no one who sets it. The forms for the countries selected are in S02-V-660.
- S02-SH-1014 (f): the same, for another store ('option "Canada" [selected] - option "United Kingdom" - option "Yemen"').

### Revisit S02-V-930 (woocommerce, S02-VP-64, who sets "business entities"): was `not covered`
- No leads under (f). Replaced S02-V-930 with `absent` S02-WC-N02, for the part the second audit (A3-2, 'partly contradicted') left standing: no settings page holds the business's legal name or a merchant of record, and nothing per selling location.
- `place` task S02-WC-517 (f), the statement the audit found: added S02-V-1118 beside the `absent` row, the seller (a reading): the Payments settings' WooPayments onboarding, a control in the store's admin (rule 4), asks 'What type of legal entity is your business?'; the legal entity of the business that sells, as S02-V-715 (salla) holds 'any legal form or legal entity the merchant or store takes'. It says nothing of what the value is taken per, so it doesn't join S02-VP-63. S02-WC-517 is under (a) too: RD1's, left. The audit's S02-WC-263 and S02-WC-518 are outside RD3's slice: left.
- The A2 statements under (g), S02-WC-274, S02-WC-275 and S02-WC-277, are already in S02-V-929 (S02-VP-63).
- x_words added: S02-VP-64, woocommerce 'legal entity; type of legal entity'.

### Revisits S02-V-943 and S02-V-944 (woocommerce, S02-VP-73 and S02-VP-74, market selection): were `not covered`
- Replaced both with `absent` S02-WC-N03, which the second audit confirmed: no settings page places a customer in a selling location, or lets a customer choose one or sends them to one.
- The leads: S02-WC-397 to S02-WC-399, the customer's default location (the base location, the allowed countries, geolocation), are the buyer's location for taxes and shipping, not a market (S02-WC-N03's words: 'none places a customer in a selling location'), so they fail the role test of 'Markets for a customer'; they stay in their rows under S02-VP-57 to S02-VP-60. S02-WC-400, the filter, stays noted under (f) ('a filter alone names no party').

### Revisit S02-V-956 (woocommerce, S02-VP-86, what "apps" takes its value per): was `not covered`
- Replaced S02-V-956 with `absent` S02-WC-N04, for the part the second audit (A3-2, 'partly contradicted') left standing: no page makes an extension take a value per selling location or per customer's country.
- The leads S02-WC-416 to S02-WC-422 stay noted under (f), as earlier parts noted them: the extensions the platform suggests to the merchant by the store's base country, as the coordinator's ruling read S02-WC-418 (what the platform shows the merchant, not the apps a store installs).
- The statements the audit found: S02-WC-519 and S02-WC-520 are `place` tasks, noted below; S02-WC-001 to S02-WC-003 stay noted; S02-WC-221, S02-WC-223, S02-WC-226, S02-WC-227 and S02-WC-267 are outside RD3's slice: left.
- S02-WC-519 (f): the payment providers the Payments settings page lists for 'The location for which the providers are being determined. This is an ISO 3166-1 alpha-2 country code.', without saying whose: what the platform lists to the merchant, of (c)'s kind 'other payment providers' (RD1's), not a setting of the store whose value differs by market; as the first pass noted S02-WC-001. Under (c) too: RD1's, left.
- S02-WC-520 (f): each gateway's 'recommended_payment_methods' for a '$country_code', without saying whose: the payment methods the platform recommends to the merchant, of (c)'s kind 'other payment providers' (RD1's), not the methods the store offers its buyers; as S02-WC-519. Under (c) too: RD1's, left.

### Revisit S02-V-789 (zid, S02-VP-65, what "Returns and cancellations" takes its value per): was `not covered`
- Replaced S02-V-789 with `gap` S02-ZD-G22, which gap-closing wrote after the earlier revisit ('searched, not found').
- The leads S02-ZD-212 to S02-ZD-219, S02-ZD-221 and S02-ZD-222 stay as the earlier revisit of this row placed them (S02-VP-66, and S02-VP-54, S02-VP-44, S02-VP-84) or noted them (S02-ZD-212, S02-ZD-215, S02-ZD-218, S02-ZD-222): none names a market, a buyer's country or the whole store. S02-ZD-220 is outside RD3's slice: left.

### Revisit S02-V-870 (zid, S02-VP-85, what "country" takes its value per): was `not covered`
- Replaced S02-V-870 with `gap` S02-ZD-G23 ('searched, not found'). S02-ZD-G01, which `why` names too, is under (a), outside RD3's slice, so it gives no `gap` row under an (f) point (rule 4), as the earlier revisit found.
- The lead S02-ZD-226 stays noted under (f) (the account's own information); it is under (a) too: RD1's, left.

### `place` tasks: where the statements went
- S02-BC-352, S02-BC-353, S02-BC-355, S02-BC-356, S02-BC-357 (g): in S02-V-1114 to S02-V-1117 under S02-VP-92 (who sets "apps"), by rule 4, (g), as the revisit of S02-V-1114 above says. S02-BC-354 (g) is noted above.
- S02-SH-1030, under (f): joined S02-V-649 (S02-VP-63, a market the store sells into), a reading from its identifier and scope (rule 5): the admin's market details page (MarketsV2MarketDetailsPage) labels a market's '"businessEntity":{"title":"Business entity"'. It names no one who sets it.
- S02-SH-1034, under (f): joined S02-V-649 (S02-VP-63), as S02-SH-1030, from the market graph page (MarketGraphPage): 'BusinessEntity:{subtitle:"Business entity",businessType:"Business type",country:"Country",address:"Address",manageBusinessEntity:"Manage business entity"'; and S02-V-651 (S02-VP-64, the seller), a reading: 'Manage business entity' is a control in the store's admin (rule 4).
- S02-WC-517, under (f): S02-V-1118 (S02-VP-64), as the revisit of S02-V-930 above says.
- S02-WC-519 and S02-WC-520 (f): noted, as the revisit of S02-V-956 above says.

### Candidates for a new point
None. No statement of these tasks answers one of (f)'s or (g)'s questions for an X that no point's kind fits.

### Words searched for
No point was raised, and no row of an earlier platform was looked for, so no search for X's words was needed. The revisits read the statements their `why` names, the platforms' `a2.tsv` and `absence-audit.tsv` rows for them, and the rows of the points they name.

## Second pass, RD3-S9: salla, bullets f and g (the last round)

Salla's 27 tasks of the work list whose `why` begins 'last round' (after A2-T, A2-SH-H, A2-SA-H, A2-SA-S and A3-2): 4 revisits, then 13 `place` tasks under (f) and 10 under (g), in the list's order. The place tasks that answer a revisited point's rows were placed with its revisit. Salla's statements are read as Part RD3-2 and RD3-S6 read them. Most of the new statements are the settings center's definitions (structures/salla/settings-center/demo@en/*.json) or the dashboard's code. A form, field, select, toggle or radio of the settings center, or code that saves a value from a dashboard page, is read as a control in the store's admin, so the seller (rule 4), a reading. A value read or fetched (S02-SA-456, S02-SA-458, S02-SA-459, S02-SA-461), or a table's headers (S02-SA-460), names no one who sets it. Salla's API's 'scopes' is its word for a market ('store scopes ... for multi-country functionality', `terms.tsv`). The absences the revisits name, S02-SA-N01 to S02-SA-N03, all confirmed by the second audit, each say that a section of the settings center has no market field. Each is cited in the evidence of the whole-store row it bears on, and none became an `absent` row (below). Each statement joined to a row was compared with the statement in its point's `raised_by` from another platform (rule 5): none shares a term, identifier or definition with it, so each rests on `answers`.

### Revisits: rows replaced or removed, and what took their place
- S02-V-1092 (S02-VP-65, was `gap` S02-SA-G06): replaced by `gap` S02-SA-G13, which names itself in place of G06. Its leads: S02-SA-437 (the order cancellation form, PUT settings/fields/orders.cancel_order) and S02-SA-443 (the theme editor's ReturnPolicy, 'payload:{days:x}') joined S02-V-716 (the whole store: statements under (g), a reading; absence S02-SA-N01 cited there) and S02-V-717 (the seller: a control in the store's admin, a reading). S02-SA-439 (guest checkout's option scopes) answers checkout, not returns: it joined S02-V-699 (S02-VP-55, a market) and S02-V-701 (S02-VP-56, the seller). S02-SA-382 stays where RD3-S6 placed it (S02-V-708, S02-V-709, S02-V-712).
- S02-V-1094 (S02-VP-86, was `gap` S02-SA-G09): replaced by `gap` S02-SA-G15, in place of G09. No lead gives a new answer: S02-SA-413 to S02-SA-415 stay in S02-V-874 (and S02-V-1095, S02-V-746, S02-V-1110), and S02-SA-409 to S02-SA-411 stay noted (RD3-S6). Absence S02-SA-N03 is cited in S02-V-1093 (the whole store). The statement the second audit recorded for it, S02-SA-461 (a place task), gave a new row, S02-V-1119 (below).
- S02-V-1097 (S02-VP-89, was `gap` S02-SA-G10): replaced by `gap` S02-SA-G14, in place of G10. Its lead S02-SA-438 (the settings page's field all-notifications) joined S02-V-886 (the whole store, a reading; absence S02-SA-N02 cited there) and S02-V-890 (the seller). Its lead S02-SA-439 is guest checkout's (above).
- S02-V-731 (S02-VP-76, was `not covered`): replaced by `gap` S02-SA-G12, which gap-closing recorded after RD3-S6's revisit. Its leads, S02-SA-421 and S02-SA-425, are locations, not the store's address. They stay in S02-V-734 (S02-VP-78, the seller).

### `place` tasks: where the statements went
Under (f):
- S02-SA-444, S02-SA-447, S02-SA-448 and S02-SA-449: the offers' priorities, the gift option, the loyalty program and the wallet's credit limits, each set per market in the settings center. They joined S02-V-691 (S02-VP-51, a market) and S02-V-695 (S02-VP-52, the seller).
- S02-SA-445 and S02-SA-446: a market's login methods, and the markets the WhatsApp OTP applies to. They joined S02-V-699 (S02-VP-55, a market) and S02-V-701 (S02-VP-56, the seller).
- S02-SA-456 and S02-SA-457: the order cancellation setting's saved value, and the dashboard section that writes it. They joined S02-V-716 (S02-VP-65, the whole store). S02-SA-457 also joined S02-V-717 (the seller, a reading: the section PUTs the field).
- S02-SA-458 to S02-SA-460: the notification preferences, which are read with the signed-in user's token; their answer; and the table's columns. They joined S02-V-886 (S02-VP-89, the whole store, a reading). None is placed under S02-VP-90. S02-SA-459's '"source":"subscriber"' names the source of an override, and its words don't say that the source is who set it.
- S02-SA-461: a market's login settings take their OTP provider from the installed SMS apps, local and international, as its identifier and scope say (rule 5). It gave a new row, S02-V-1119 (S02-VP-86, a market, a reading), and joined S02-V-699 (S02-VP-55, a market). It names no one who sets the provider.
- S02-SA-462: the help article's steps for the customer's order cancellation, 'اضغط (تخصيص)' (my translation: 'click (Customize)'). It joined S02-V-717 (S02-VP-66, the seller). Its 'من إعدادات المتجر' (my translation: 'from the store settings') names where the setting is, not that one value holds for the store, so it is not placed under S02-VP-65.

Under (g):
- S02-SA-437, S02-SA-443, S02-SA-456 and S02-SA-457: S02-V-716 (S02-VP-65, the whole store). S02-SA-437, S02-SA-443 and S02-SA-457 are also in S02-V-717 (S02-VP-66, the seller).
- S02-SA-438 and S02-SA-458 to S02-SA-460: S02-V-886 (S02-VP-89, the whole store). S02-SA-438 is also in S02-V-890 (S02-VP-90, the seller).
- S02-SA-442, the Meta pixel's catalog connected with one set of the store's data: S02-V-878 (S02-VP-87, the whole store, a reading).
- S02-SA-450, one field of the store's settings, scopes.browse_product_method: a new row, S02-V-1120 (S02-VP-73, the whole store), and S02-V-728 (S02-VP-74, the seller). Both are readings (below).

### Statements noted (rule 2)
None.

### Candidates for a new point
None.

### Words searched for
None. Every task named its statements, each was printed by id, and no point was raised. x_words added for salla:
- S02-VP-51 and S02-VP-52: 'gift_option; customer-wallet; offers_settings_rules';
- S02-VP-55 and S02-VP-56: 'login-methods; whatsapp_otp; guest_checkout_option';
- S02-VP-65: 'orders.cancel_order; ReturnPolicy'; S02-VP-66: the same, and 'السماح للعميل بإلغاء الطلب';
- S02-VP-73 and S02-VP-74: 'browse_product_method';
- S02-VP-86: 'local_sms_apps; international_sms_apps';
- S02-VP-87: 'connectPixelCatalog';
- S02-VP-89: 'all-notifications; NotificationsPreferencesTable'.

### Calls this part made, and problems with the brief, the work list or the tools
- **Absences beside answers.** Each revisit's absence (S02-SA-N01 to S02-SA-N03) is confirmed by the second audit and says that a section of the settings center has no market field. The statements it rests on answer the point with the whole store. The brief's revisit offers an `absent` row in place of the old one, but says nothing of one beside answers. An `absent` row would also say the point's answer is absent, where the platform's rows give one. So no `absent` row was written: each absence is cited in the evidence of the whole-store row it bears on (S02-V-716, S02-V-886, S02-V-1093). The coordinator may prefer `absent` rows.
- **A value per user.** The notification preferences (S02-SA-458, S02-SA-459) are the signed-in user's own. Rule 4's four phrases hold no value per user. The value differs by no market or buyer's country, so it is read as the whole store, as the statements' (g) says.
- **The kind of S02-SA-450.** 'browse_product_method' names none of its options. It is read as market selection by its section, markets, and by gap-closing's lead (S02-VP-73 and S02-VP-74 in salla's `a2.tsv`). If it is instead which products are offered, S02-V-1120 belongs under S02-VP-47, and its seller's row under S02-VP-48.
- **Controls, from definitions and code.** The settings center's definitions, and the dashboard's code that saves a value, are read as controls in the store's admin, so the seller (rule 4). The theme editor's ReturnPolicy (S02-SA-443) is read the same way, by its identifier's page, /design/return-policy.
- **S02-SA-461 under two kinds.** A market's OTP provider, chosen from the installed SMS apps, is read as of two kinds: apps (S02-VP-86, as S02-V-874 reads the default SMS apps), and checkout and customer accounts (S02-VP-55, sign-in).
- **S02-SA-442 and S02-VP-87.** The work list gives S02-SA-442 a task under (g) only, though the slice gives it (f) and (g); its row under S02-VP-87 places it under both. Salla's `a2.tsv` names it for S02-VP-87, beside S02-SA-G08, but the work list holds no last-round revisit of S02-V-1096 (`gap` S02-SA-G08), which is left as it was. Its storeData carries the store's kycCountry, which this part does not read as what the connection's value differs by.
- **The message and the brief on notes.md.** The message says that each platform's notes.md says what the late parts found, beside its `a2.tsv` and `absence-audit.tsv`. The brief says not to read the platforms' notes.md. This part read only `a2.tsv` and `absence-audit.tsv`.
- **No partly contradicted absence.** The second audit confirmed each absence these tasks name, S02-SA-N01 to S02-SA-N03; it partly contradicted none of them.

### Problems with the brief, the work list or the tools
- The message that started this part says each platform's `notes.md` tells what the A2 and A3 parts found; the brief forbids reading the platforms' `notes.md`. This part didn't read them, and worked from `a2.tsv`, `absence-audit.tsv` and the slice. It did read one row of `shopify/gaps.tsv` (S02-SH-G13, under (h)), a file the brief doesn't name, while finding the gap that `a2.tsv` gives S02-SH-1030 and S02-SH-1034 with; it changed no placement.
- `why` of S02-V-870 names S02-ZD-G01, which is under (a) and outside RD3's slice, so it can give no `gap` row under an (f) point; and `why` of S02-V-662 lists again the earlier revisit's leads (S02-SH-647 to S02-SH-688), which were placed or noted already.
- The brief says a `gap` row may stand beside answers and a `not covered` row never does, but not whether an `absent` row may. S02-V-930 (`absent`, S02-WC-N02) stands beside S02-V-1118 (S02-WC-517), as the message's rule on partly contradicted absences reads: the absence 'still stands for the part its note says'.
- This part first wrote its lines for S02-SH-1030, S02-SH-1034 and S02-WC-517 in '`place` tasks' in a note's form (the id, then a bullet in brackets), though they are placed. It reworded those three lines alone, in place, to 'under (f)', after checking that the file hadn't changed meanwhile; nothing else in `notes-b.md` was rewritten.

### After the check (RD3-S10)
- The checker, on a copy holding only `b/RD3`, gave no `error` or `warning` on this part's ids. Its three errors are on salla's rows S02-V-1092, S02-V-1094 and S02-V-1097 (gaps narrowed since), RD3-S9's tasks. RD3's rows in `unplaced.tsv` are all salla's (S02-SA-437 to S02-SA-462), RD3-S9's. `second_pass_list.py --check` lists none of this part's tasks.

### After the check (RD3-S9)
- The checker raised no error on this part's ids. Its `unplaced.tsv` listed one statement of this part's platform and bullets that no task names: S02-SA-440, under (f). Salla's `a2.tsv` names it for S02-VP-85, but the work list's only revisit of S02-V-869 (its first-round row) names S02-SA-426 to S02-SA-430, and no `place` task names it. It is a market's record, as the storefront at sa.aldakheeloud.com returns it ('"type": "scope"'), with its own languages, currencies and countries. It joined S02-V-676 (S02-VP-41, a market: '"currencies": ["SAR"]') and S02-V-680 (S02-VP-43, a market: '"languages": ["ar", "en"]'). It is not placed under S02-VP-85: its '"countries": ["SA"]' are the market's, and its words don't say they are the store's own country (rule 2's role test). S02-V-869 (`gap` S02-SA-G11), which no task of this round revisits, is left as it was.

## Second pass, RD3-S11: shopify, bullet f, the capture round's tasks

**The slice.** The capture round's statements (A2-SH-R1 and A2-SH-R2, observed-sh 19a5f6435) were in no slice when this part started: `slices/` was last cut at 19:21 on 27 October, and `kinds.tsv` (23:25) held A2-SH-R1's statements but not A2-SH-R2's. `method/variants_edit.py` refuses a statement outside `slices/RD3/`. So this part ran the full check on a copy of S-02 in its scratch folder, which wrote the copy's `kinds.tsv`, and cut the copy's slices with `method/subject_slice.py`. The copy's `slices/RD3/` differs from the real one only by 58 added statements (this part's 38 `place` tasks and the revisit's 20 new leads) and 2 added terms: no line of the real slice changed or went. This part ran `variants_edit.py` on a scratch folder holding that slice, with `b/RD3` and `b/ranges.tsv` linked to the real ones, so every row was written to `b/RD3/` by the tool, under its lock. The real `slices/` and `kinds.tsv` are as they were: cutting them again is the coordinator's.

### Revisit S02-V-662 (shopify, S02-VP-69, the buyer's address form): was `gap` (S02-SH-G11)
- The checker names S02-SH-1122 as answering S02-SH-G11, and `why` names no gap, so G11 is settled and goes.
- Every answer the new leads give is one Shopify's rows already hold. Joined S02-SH-1122 to S02-SH-1137 to S02-V-660, the buyer's country: one store's checkout (demo-fake-dev-store, Basic App Development, run 20261027T202345Z, steps 60 to 65), its address form for the Delivery countries Saudi Arabia, the United Arab Emirates, Japan, Brazil, Italy and the United States (S02-SH-1122 to S02-SH-1127), and the checkout's CountryDetails answer for each, its labels and its formatting with required fields (S02-SH-1128 to S02-SH-1137). Removed S02-V-662.
- S02-VP-70 (who sets "address autocompletion feature"): joined S02-SH-1129, S02-SH-1131, S02-SH-1133, S02-SH-1135 and S02-SH-1137, and the earlier leads S02-SH-1008 and S02-SH-1010, which hold the same keys, to S02-V-664, the platform: each CountryDetails answer sets the field the autocompletion works on ('"autocompletionField":"ADDRESS1"', '"autocompletionField":"POSTAL_CODE"') and which fields are required, values the platform's code sets (rule 4), as S02-SH-456 there already. The forms S02-SH-1122 to S02-SH-1127, also leads to S02-VP-70 in `a2.tsv`, name no one who sets them: they are placed under S02-VP-69 only.
- S02-SH-1118 (the market 'Capture checkout countries', step 14) and S02-SH-1120 (the market 'Canada', step 58), leads to this point, say nothing of the address form. Each shows its market's own value for other settings, so they joined the `a market the store sells into` rows: S02-SH-1118 to S02-V-600 (currency, 'Customized Currency Use local currencies'), S02-V-606 and S02-V-611 (language and domain, 'Domain / language demo-fake-dev-store.myshopify.com · English'), S02-V-614 and S02-V-620 (products and prices, 'Inherited Catalogs All products'), S02-V-624 (discounts, 'All eligible discounts'), S02-V-633 (taxes and duties, 'Not collecting') and S02-V-639 (shipping, 'Not shipping'); S02-SH-1120 to S02-V-614 and S02-V-620 ('Customized Catalogs Catalog for Canada') and S02-V-639 ('Shipping International, Free International Shipping, International Shipping'). Both are under (e) too: RD2's, left.
- The earlier leads S02-SH-647 to S02-SH-688 and S02-SH-1007 to S02-SH-1018 stay as the earlier revisits placed or noted them.
- S02-SH-1119 (f): the countries one store's checkout offers in its Country/Region field at step 30 ('option "United States" [selected]'), seen once; it shows no value that differs by a market or a country, or that holds for the whole store, and names no one who sets it, as S02-SH-1011 and S02-SH-1014 were noted. The forms for the countries chosen are in S02-V-660.
- S02-SH-1121 (f): the same, for the same store's checkout at step 59 ('option "Saudi Arabia"', 'option "United Arab Emirates"').

### `place` tasks (A2-SH-R1 and A2-SH-R2)
- S02-SH-1042 and S02-SH-1043 (the shop API's general settings, time zone and units, store tuu1u4-v0): joined S02-V-675 (S02-VP-77, the whole store), the shop's one value each (identifier 'SettingsGeneral (shop API)'), as S02-SH-455's one backup region is in S02-V-668. They name no one who sets the values, so they don't join S02-VP-91.
- S02-SH-1045 and S02-SH-1057 (Settings > General, Regional settings, stores tuu1u4-v0 and capture-us-plus): joined S02-V-675 and S02-V-1100 (the seller, the section's controls), as S02-SH-345 and S02-SH-398 are there; S02-V-668 (S02-VP-73, the backup region, the whole store); and S02-V-669 (S02-VP-74, the seller), for the Backup Region control '[United States]' in the store's admin (rule 4). Earlier parts placed the same control, in S02-SH-345 and S02-SH-398 to S02-SH-404, under S02-V-668 but not under S02-VP-74. No task leads to those rows, so they are as they were: for the coordinator.
- S02-SH-1046 and S02-SH-1059 (the shop API's BackupRegion): joined S02-V-668, the shop's one backup region, as S02-SH-455 is there.
- S02-SH-1060 and S02-SH-1067 (Settings > General before and after a switch of the business entity, store capture-gb-plus): joined, as S02-SH-399 to S02-SH-404 are there, S02-V-603 (the currency display of the store defaults), S02-V-650 (the business entity 'used for financial products, markets, apps, and taxes in this shop'), S02-V-658 (store contact details), S02-V-668 (the backup region) and S02-V-868 (the store address); and S02-V-669, for the Backup Region control. 'Manage entities in Organization settings' points to another settings area and is no control of the store's entity, so neither joins S02-VP-64. The store address they show isn't the address form whose fields S02-VP-76 holds (S02-V-674), so neither joins S02-VP-76, which `a2.tsv` names. Both are under (a) and (b) too, and S02-SH-1067 under (c): RD1's, left.
- S02-SH-1091, S02-SH-1093, S02-SH-1095 and S02-SH-1116 (market pages: a new market before any condition, and the market 'Capture UK market' once saved): joined the `a market the store sells into` row of each setting the page shows: S02-V-600 (currency), S02-V-606 and S02-V-611 (domain / language), S02-V-614 and S02-V-620 (catalogs), S02-V-624 (discounts), S02-V-627 (online store), S02-V-631 (checkout and accounts), S02-V-639 (shipping; not S02-SH-1116, which shows none), and, for S02-SH-1091 and S02-SH-1095, S02-V-633 (taxes and duties) and S02-V-653 (returns and cancellations). They show no business entity, so S02-SH-1095 doesn't join S02-VP-63, which `a2.tsv` names. All four are under (e) too: RD2's, left.
- S02-SH-1096 (the market's taxes and duties customization): joined S02-V-633 (per market) and S02-V-635 (the seller, its controls).
- S02-SH-1097 (the market's domain customization): joined S02-V-611 (per market) and S02-V-613 (the seller, its controls). It customizes the domain, and the language it shows ('English Primary') is the domain's, so it joins no language point.
- S02-SH-1100 (marketCreate's answer, with '"businessEntity":null'): joined S02-V-649 (S02-VP-63, a market): the market record holds its own business entity field, unset at creation. Under (e) too: RD2's, left.
- S02-SH-1117 (Settings > Shipping and delivery, 'Shipping has moved to Markets'): joined S02-V-639 (per market) and S02-V-642 (the seller, 'Manage where you ship and what it costs').
- S02-SH-1138 and S02-SH-1139 (the countries and regions where shipping is taxed regardless of the setting, one list in two runs), S02-SH-1142 (postal duty rates for the United States as the destination) and S02-SH-1143 (the Section 232 percentage, for shipments to the United States): joined S02-V-634, the buyer's country. For S02-SH-1138 this is a reading: the countries are where the order is taxed. S02-SH-1143 also joined S02-V-635 (the seller, 'The percentage that you select') and S02-V-636 (the platform, 'The default percentage for the Section 232 setting is 100%').
- S02-SH-1140 (the steps to charge tax on shipping, 'In the Global settings section'): joined S02-V-635 (the seller). Its 'Global settings' is where the store switches the setting on once, and S02-SH-1138 says the setting's effect differs by country, so by rule 4 it joins no `the whole store` row.
- S02-SH-1141: joined S02-V-633 (the Markets section, 'for countries and regions') and S02-V-635 (the seller).
- S02-SH-1144: joined S02-V-651 (S02-VP-64, the seller: 'other Shopify accounts that you add are considered your secondary entities'). Its 'Certain features such as adding a third-party payment method are available only for the primary entity' ties a payment method to the primary entity, none of rule 4's four phrases, so it joins neither S02-VP-61 nor S02-VP-62, which `a2.tsv` names.
- S02-SH-1145 (f): which payment providers a primary or secondary business entity can use ('you can't add Shopify Payments to your secondary entity'), of (c)'s kinds 'the platform's own payment service' and 'other payment providers' (RD1's); it gives no setting a value per one of rule 4's four phrases, and names no one who sets a business entity.
- S02-SH-1146 and S02-SH-1149: joined S02-V-650 (S02-VP-63, the whole store): for some orders one entity, the primary, whatever the market or buyer ('all subscription payments are processed through your primary entity'; 'Purchases made through unsupported apps are routed to the primary entity, regardless of the customer's market'). S02-SH-1149 also joined S02-V-1108 (S02-VP-92, the seller: 'Deactivate the app', 'Configure the app'), and gives a new row, S02-V-1122 (S02-VP-86, a market the store sells into: 'Configure the app to work only in markets served by the primary entity'), which Shopify's rows didn't hold (S02-V-873 is the whole store).
- S02-SH-1147: joined S02-V-645 (S02-VP-61, a market): third-party payment methods 'are displayed only on checkouts and for markets associated with the primary entity'.
- S02-SH-1148: joined S02-V-647 (S02-VP-62, the seller: 'You can offer Shop Pay Installments on any of your entities'), and gives a new row, S02-V-1121 (S02-VP-62, the platform: 'Newly added eligible entities might have Shop Pay Installments activated by default when Shopify Payments is activated'; rule 4, 'by default'). Its 'activated and managed separately for each entity's Shopify Payments account' is per entity, none of rule 4's four phrases, so it joins no row of S02-VP-61 or S02-VP-63, which `a2.tsv` names.
- S02-SH-1153 and S02-SH-1154: joined S02-V-651 (S02-VP-64, the seller: 'You can set a default business entity for a store from the Settings > General page'; 'before you can switch business entities in your Shopify admin'). The store's default entity is the value its markets take until the seller changes it (rule 4), so S02-SH-1153 joins no `the whole store` row. S02-SH-1154's 'Only the store owner can deactivate Shopify Payments' is said of a payment provider, (c)'s kind, not of the business entity: no row for the store owner. Both are under (b) too, and S02-SH-1153 under (a): RD1's, left.
- S02-SH-1155: joined S02-V-645 (a market: 'ensure those countries are set up as markets'), S02-V-1048 (the store's own country: 'countries outside your business location'), as S02-SH-636 and S02-SH-641 are in both, and S02-V-647 (the seller, whom it instructs).
- S02-SH-1156: joined S02-V-646 (the buyer's country: 'Each method is available only when a customer is in a supported country and selects an eligible currency') and S02-V-647 (the seller: 'You can activate local payment methods with Shopify Payments').
- S02-SH-1157: joined S02-V-647 (the seller: 'After you activate Shop Pay Installments'). Affirm 'periodically reviews your online store to make sure that you're in compliance with their prohibited business policy': a party that requires compliance without setting the method, so no row for Affirm (rule 4).
- S02-SH-1150 (f): a condition on selling from several business entities ('If you're using managed markets, then you can't sell from multiple entities with Shopify Payments'); it gives the entity no value per one of rule 4's four phrases and names no one who sets it.
- S02-SH-1151 (f): the same, with automated tax filing ('If you're using automated tax filing, then you can't sell from multiple entities with Shopify Payments'); it gives the taxes no value per one of the four phrases either.
- S02-SH-1152 (f): an entity is shared by the stores it is assigned to ('Changes to an entity affect all stores that the entity is assigned to'), which is none of rule 4's four phrases, and it names no one who sets it. Under (a) too: RD1's, left.
- S02-SH-1158 (f): the heading of the list of reasons a store's Shop Pay Installments account can be suspended; read with its run S02-SH-1159.
- S02-SH-1159 (f): the reasons, conditions on the store such as 'The primary currency of your online store isn't USD, CAD, or GBP' and 'The primary language of your online store isn't English'; they give the method no value per one of rule 4's four phrases and name no one who sets it.
- x_words added for shopify: S02-VP-57 'Charge tax on shipping rates; postal duty rates; Section 232 setting'; S02-VP-61 'third-party payment methods; Shop Pay Installments'; S02-VP-62 'Shop Pay Installments'; S02-VP-63 'primary entity; secondary entities; default business entity; businessEntity'; S02-VP-64 'primary entity; secondary entities; default business entity'; S02-VP-70 'autocompletionField'.
- Searches: none. The second pass raises no point, so rule 3's search for earlier platforms' rows doesn't arise.

### Candidates for a new point
- None. Each statement that answers one of (f)'s questions does so for an X of one of rule 1's kinds. Those noted above fail on the answer, which is none of rule 4's four phrases and names no party, not on their X.

## Second pass, RD3-S12: zid, bullet f, the Salla and Zid round's tasks

From A2-ZD-R and A3-ZD-R (other-product-class f44be3f, folder `zid/`). The new leads are observations of two stores, the public demo (127604, Professional) and the development store (3277610), which held a second market (Kuwait) for a time; both have the feature flag `must_use_markets_pricing` false. Each row written here keeps its statements' scope (store, plan, flag, run and step): what one store showed on one day isn't what every Zid store does. The absences S02-ZD-N05 to S02-ZD-N16, each that the dashboard's complete list of routes holds no page under a market for one setting, are confirmed by A3-ZD-R; where a lead gives the row's answer, the absence is cited in that row's `basis_evidence`, as RD3-S9 did for Salla's (S02-V-716, S02-V-886, S02-V-1093).

### Revisit S02-V-1067 (zid, S02-VP-67, locations): was `gap` (S02-ZD-G12)
- Replaced by the whole store (a reading): S02-ZD-451 (the Priority for withdrawal from warehouse page: one ordered list of the store's locations, no market field) and S02-ZD-452 (the locations answer: one `fulfillment_priority` per location, no market field); absence S02-ZD-N07 cited there.
- Added S02-V-1123, gap S02-ZD-G25 (in place of S02-ZD-G12): per sales channel or per buyer's city.
- S02-V-791 (a market, a reading of S02-ZD-280's sales channel per inventory) stays. The other leads (S02-ZD-269 to S02-ZD-287) stay as the revisit of S02-V-791 placed or noted them.

### Revisit S02-V-1070 (zid, S02-VP-72, who sets staff access): was `gap` (S02-ZD-G17)
- Removed: why names no gap, so gap-closing settled S02-ZD-G17. Lead S02-ZD-459 (the Create group page in the store's admin) joined S02-V-796 (the seller), which the platform's rows already hold. The other leads stay in S02-V-796, S02-V-1069 or noted, as the earlier revisit placed them. Absence S02-ZD-N11 is of a route under a market, so it is cited under S02-VP-71 (S02-V-795), not here.

### Revisit S02-V-774 (zid, S02-VP-55, checkout and customer accounts): was `gap` (S02-ZD-G10)
- Replaced by the whole store (a reading): S02-ZD-448 (Buy as a guest, shown once on settings/checkout, no country or market field) and S02-ZD-449 (the store's settings answer, one value per key: `is_single_page_checkout_enabled`); absence S02-ZD-N05 cited there.
- Added S02-V-1124, gap S02-ZD-G24 (in place of S02-ZD-G10): per buyer's country.
- S02-ZD-448 also joined S02-V-775 (S02-VP-56, the seller: a control in the store's admin).
- S02-ZD-449 names several settings (rule 2), so it also joined S02-V-753 (S02-VP-41, the whole store: one `config_currency`) and S02-V-759 (S02-VP-43, the whole store: one `config_language`), and goes under S02-VP-68 and S02-VP-77 with their revisits.
- The other leads (S02-ZD-247 to S02-ZD-254, S02-ZD-257) stay as the earlier revisit placed or noted them.

### Revisit S02-V-789 (zid, S02-VP-65, returns and cancellations): was `gap` (S02-ZD-G22)
- Replaced by the whole store (a reading): S02-ZD-466 (the Exchange and returns page, one page of the store, no country or market field; its 'For Saudi stores' points to the Ministry's rules and sets no value); absence S02-ZD-N15 cited there.
- Added S02-V-1125, gap S02-ZD-G28 (in place of S02-ZD-G22): per buyer's country.
- S02-ZD-466 also joined S02-V-790 (S02-VP-66, the seller: the page's Save in the store's admin). The other leads (S02-ZD-212 to S02-ZD-219, S02-ZD-221, S02-ZD-222) stay as the earlier revisits placed or noted them.

### Revisit S02-V-792 (zid, S02-VP-68, contact information shown to buyers): was `gap` (S02-ZD-G11)
- Replaced by the whole store (a reading): S02-ZD-450 (the Store information page: one Email and one Phone that appear to the customer in the storefront, no market or country field) and S02-ZD-449 (one `config_email`, `config_telephone` and `commercial_registration_number`); absence S02-ZD-N06 cited there. Why names no gap: S02-ZD-G11 was settled by gap-closing, and goes.
- S02-ZD-450 also joined S02-V-803 (S02-VP-79, the seller). S02-ZD-266 to S02-ZD-268 stay in S02-V-803.

### Revisit S02-V-795 (zid, S02-VP-71, staff access): was `gap` (S02-ZD-G17)
- Replaced by the whole store (a reading): S02-ZD-459 (the Create group page asks a group's name and users, no market field); absence S02-ZD-N11 cited there. Why names no gap: S02-ZD-G17 was settled by gap-closing, and goes.
- S02-ZD-459 also joined S02-V-796 (S02-VP-72, the seller), with the revisit of S02-V-1070. The other leads stay as the earlier revisit placed or noted them.

### Revisit S02-V-799 (zid, S02-VP-75, privacy and consent): was `gap` (S02-ZD-G18)
- Replaced by the whole store (a reading): S02-ZD-462 (the Privacy policy page, headed 'Privacy policy for your store', no country or market field); absence S02-ZD-N12 cited there.
- Added S02-V-1126, gap S02-ZD-G26 (in place of S02-ZD-G18): the policy or the opt-outs per buyer's country, and the opt-outs per market.
- S02-ZD-462 also joined S02-V-808 (S02-VP-84, the seller). The other leads (S02-ZD-334 to S02-ZD-339) stay as the earlier revisit placed or noted them.

### Revisit S02-V-801 (zid, S02-VP-77, units and time zone): was `gap` (S02-ZD-G21)
- Replaced by the whole store (a reading; `answers;term`): S02-ZD-465 ('Selecting your store's time zone', one field of Business address) and S02-ZD-449 (one `default_timezone`); absence S02-ZD-N14 cited there. `term`: 'Time zone', the same words as S02-SH-246 (raised_by); terms.tsv defines neither differently.
- Added S02-V-1127, gap S02-ZD-G27 (in place of S02-ZD-G21): whether any setting holds a unit of weight or measurement.
- S02-ZD-465 also joined S02-V-1103 (S02-VP-91, the seller), where S02-ZD-346 stays.

### Revisit S02-V-804 (zid, S02-VP-80, store status): was `gap` (S02-ZD-G20)
- Replaced by the whole store (a reading): S02-ZD-463 ('Manage your store closure or stop receiving orders.', the Hours of operation page) and S02-ZD-464 (one set of the store's availability settings, `is_store_closed`); absence S02-ZD-N13 cited there. Why names no gap: S02-ZD-G20 was settled by gap-closing, and goes.
- S02-ZD-463 also joined S02-V-805 (S02-VP-81, the seller). S02-ZD-340 to S02-ZD-345 stay in S02-V-805 and S02-V-1087.

### Revisit S02-V-870 (zid, S02-VP-85, the store's country): was `gap` (S02-ZD-G23)
- Replaced by the whole store (a reading): S02-ZD-467 (one country in the store's business place, Business address > Country) and S02-ZD-471 (the primary market's own countries, unchanged after the store's country was changed to Kuwait, as its scope records); absence S02-ZD-N16 cited there.
- Why names gap S02-ZD-G29, which is under a bullet outside RD3's slice (the slice's gaps for zid end at S02-ZD-G28), so it gives no gap row, as the earlier revisit found for S02-ZD-G01.
- S02-ZD-471 also joined S02-V-751 (S02-VP-41, a market: the market's own `main_currency`). S02-ZD-226 stays noted. S02-ZD-468 and S02-ZD-472 are outside the slice, left. S02-ZD-467 is under (a) too: RD1's, left.

### Revisit S02-V-875 (zid, S02-VP-86, apps): was `gap` (S02-ZD-G15)
- Replaced by the whole store (a reading; `answers;term`): S02-ZD-455 (the My apps page: one list of the store's activated and deactivated apps, no market field) and S02-ZD-456 (one list of the store's installed applications); absence S02-ZD-N09 cited there. The 'market' in S02-ZD-456's path is Zid's app market (سوق تطبيقات زد), a homonym, not a market the store sells into: no basis rests on it. `term`: 'apps', as S02-BC-147 (raised_by). Why names no gap: S02-ZD-G15 was settled by gap-closing, and goes.
- The other leads stay noted (S02-ZD-303, S02-ZD-305, S02-ZD-307, S02-ZD-309 to S02-ZD-312, RD3-S4) or in S02-V-1111 (S02-VP-92, the seller), as earlier parts placed them. S02-ZD-308 is outside the slice, left.

### Revisit S02-V-879 (zid, S02-VP-87, analytics and tracking): was `gap` (S02-ZD-G14)
- Replaced by the whole store (a reading): S02-ZD-453 and S02-ZD-454 (each tracking app's activation page asks one Account code, no market field) and S02-ZD-456 (one Google Analytics among the store's installed apps); absence S02-ZD-N08 cited there. Why names no gap: S02-ZD-G14 was settled by gap-closing, and goes.
- S02-ZD-453 and S02-ZD-454 also joined S02-V-883 (S02-VP-88, the seller) and S02-V-1111 (S02-VP-92, the seller: an app's activation is the app's own setting). S02-ZD-293 to S02-ZD-298 stay in S02-V-883; S02-ZD-299 stays noted.

### Revisit S02-V-887 (zid, S02-VP-89, notifications to the merchant): was `gap` (S02-ZD-G16)
- Replaced by the whole store (a reading): S02-ZD-457 (the Staff notifications page: one set of statuses and e-mails) and S02-ZD-458 (one `order_statuses` and one `emails`, no market field); absence S02-ZD-N10 cited there. Why names no gap: S02-ZD-G16 was settled by gap-closing, and goes.
- S02-ZD-457 also joined S02-V-891 (S02-VP-90, the seller). S02-ZD-313 to S02-ZD-317 stay in S02-V-891, S02-ZD-318 in S02-V-1088.

### `place` tasks (A2-ZD-R and A3-ZD-R)
- S02-ZD-474: joined S02-V-771 (S02-VP-53, a market: 'By default, all markets use your store's active theme. You can assign a different theme to each market', a market that takes the store's value until the seller changes it, rule 4) and S02-V-773 (S02-VP-54, the seller: 'You can assign').
- S02-ZD-487: joined S02-V-751 (S02-VP-41, a market: the Kuwait market's 'Market currency [KWD]') and S02-V-755 (S02-VP-42, the seller: a field of the market's manage page in the store's admin). Its 'Product prices and currency' is a section heading that shows no value, so it joins no row of S02-VP-49. Under (e) too: RD2's, left.
- S02-ZD-488: joined S02-V-751 (a market: the code that saves a market sends 'main_currency:t.market_currency' with the market's id). Not under S02-VP-42: the code's words name no party, and the value it sends is the form's (rule 4). Under (e) too: RD2's, left.
- S02-ZD-489: joined S02-V-766 (S02-VP-49, a market: 'Set different product prices for each market and customer type') and S02-V-767 (S02-VP-50, the seller). Per customer type is none of rule 4's four phrases; it stays in the evidence.
- S02-ZD-490: joined S02-V-751 (S02-VP-41, a market: 'Customer Wallet uses this market's currency.'), S02-V-769 (S02-VP-51, a market, a reading: the Customer Wallet read as store credit) and S02-V-756 (S02-VP-42, the platform, a reading: 'Contact support if you need to change it.', a change made by Zid's support, not by a control of the store's admin).
- S02-ZD-491: joined S02-V-771 (a market: 'Customers from this market will see the selected theme') and S02-V-773 (the seller: 'Select a theme to assign to this market.').
- S02-ZD-493: joined S02-V-763 (S02-VP-47) and S02-V-766 (S02-VP-49), a market ('حسب السوق المستهدف', my translation: 'by the target market'), and S02-V-765 (S02-VP-48) and S02-V-767 (S02-VP-50), the seller ('تقدر', my translation: 'you can').

### x_words added for zid
- S02-VP-55 'Checkout page options; Buy as a guest; is_single_page_checkout_enabled'; S02-VP-65 'Exchange and returns'; S02-VP-67 'Priority for withdrawal from warehouse; fulfillment_priority'; S02-VP-68 'Store information; Email; Phone; config_email; config_telephone'; S02-VP-71 'Create group; Group information'; S02-VP-75 'Privacy policy'; S02-VP-77 'Time zone; default_timezone'; S02-VP-80 'Hours of operation; store closure; is_store_closed'; S02-VP-85 'Business address > Country; business_location'; S02-VP-86 'My apps; تطبيقاتي; installed_applications'; S02-VP-87 'Google Analytics; Google Tag Manager; Meta pixel; TikTok pixel; Account code'; S02-VP-89 'Staff notifications; order_statuses; emails'; S02-VP-41 'Market currency; main_currency'; S02-VP-49 'product prices; B2B pricing'; S02-VP-51 'Customer Wallet'; S02-VP-53 'Used theme; Assign theme; active theme'.

### Statements noted (rule 2)
- None: every lead under (f) and every place task's statement is placed. The earlier leads stay as earlier parts placed or noted them, and their notes stay as they are.

### Candidates for a new point
- S02-ZD-449's key `enforce_2fa` ('"key":"enforce_2fa","value":"0"'): X is two-step sign-in enforced through the store's settings, and the statement answers what it takes its value per (one value in the store's settings answer, the whole store, a reading). No kind of rule 1 fits: staff access is what staff may manage, not how they sign in; and its words don't say whose sign-in it governs, so it may be a setting of the platform's own account, which isn't a setting of the store. The statement is placed for its other keys (S02-VP-41, S02-VP-43, S02-VP-55, S02-VP-68, S02-VP-77), so this is listed here and not as a note.

### Words searched for
- None: the second pass raises no point, so rule 3's search for earlier platforms' rows doesn't arise.

### Calls this part made, and problems with the brief, the work list or the tools
- A confirmed absence beside a lead that answers: one `the whole store (a reading)` row per point, citing the absence in its `basis_evidence`, as RD3-S9 did, and no separate `absent` row; where the revisit's why names a newer gap ("in place of" the older), a `gap` row stands beside it (S02-V-1123 to S02-V-1127).
- The reading `the whole store` rests on a page or answer that holds the setting once, with no market or country field, outside the routes under a market, on the development store with two markets and `must_use_markets_pricing` false; the rows' scope keeps the store, plan, flag, run and step.
- S02-V-1070 was removed, not replaced by `absent`: absence S02-ZD-N11 is of a route under a market, which S02-VP-71 asks, not who sets staff access (S02-VP-72).
- S02-ZD-449 names several settings, so it joined the rows of each point it answers (S02-VP-41, S02-VP-43, S02-VP-55, S02-VP-68, S02-VP-77); S02-ZD-453 and S02-ZD-454 joined S02-VP-92's seller row beside S02-VP-88's.
- S02-ZD-471 sits in S02-V-870 by a reading of its scope (the store's country changed to Kuwait and the primary market's countries didn't); S02-ZD-490 sits in S02-V-756 (the platform: its support) and S02-V-769 (store credit) by readings, both marked.
- The RD3 slice's statements.tsv was cut again at 22:46 while this part ran: S02-ZD-489 to S02-ZD-491 printed as kind `unknown` before and `shipped` after, and their rows took `shipped`.
- 11 of the 13 revisits' ids already had lines in done.tsv from earlier rounds, so `second_pass_list.py --check` listed only S02-V-1067 and S02-V-1070 before this part ran, as the message said it would.
- Gap S02-ZD-G29, which S02-V-870's why names, is under a bullet outside RD3's slice, so it gives no row here.

### After the check (RD3-S12)
- `check_subject.py` on a copy holding only b/RD3: no `error` lines; 17 warnings (Shopify's and WooCommerce's quote lengths) and 15 reviews (quotes found only in a page's source, the coordinator's, among them zid's S02-ZD-C008, C086, C313, C314). RD3's rows in `unplaced.tsv`: 11 of Salla's (S02-SA-513 to S02-SA-537, RD3-S13's); none of Zid's.
- `second_pass_list.py --check`: RD3's list holds only S02-V-1096 (salla, RD3-S13's).

## Second pass, RD3-S13: salla, bullet f, the Salla and Zid round's tasks

From A2-SA-R, which read the runs of 28 October for capture requests H-001 to H-005 (observed-sa at b0bd0b16): six revisits of `gap` rows whose gaps are still open (S02-V-1092, S02-V-1094, S02-V-1096, S02-V-1097, S02-V-731, S02-V-869), and four place tasks (S02-SA-527, S02-SA-528, S02-SA-529, S02-SA-535). Each new statement's scope (the store, its plan) is kept in the rows it joined, which take their scope again from all their statements.

### Revisit S02-V-1092 (salla, S02-VP-65, returns and cancellations): was `gap` (S02-SA-G13)
- Left `gap` S02-SA-G13, which why names, with a row note. No lead gives an answer to S02-VP-65; absence S02-SA-N01 stays cited in S02-V-716 (the whole store), as RD3-S9 placed it.
- New leads S02-SA-530 (the public demo's form that creates its first market) and S02-SA-533 (the request its Confirm sends) name the market's language, currency and branches, and no return or cancellation setting. Both joined S02-V-680 (S02-VP-43), S02-V-676 (S02-VP-41) and S02-V-718 (S02-VP-67), a market the store sells into. S02-SA-530 also joined S02-V-681 (S02-VP-44), S02-V-678 (S02-VP-42) and S02-V-734 (S02-VP-78), the seller: each of the three fields has a control 'Customize' in the store's admin (rule 4). S02-SA-533 is under none of the who-sets points: the request's keys name no party, and the values it sends are the form's (as RD3-S12 did for S02-ZD-488). Its keys 'name', 'translations' and 'countries' are (e)'s, RD2's.
- New lead S02-SA-532, the confirmation shown before the market is created, names no return or cancellation setting either:
- S02-SA-532 (f): says activating markets 'will affect how product quantities are configured and how inventory is deducted in your store', without saying what they take their value per or who sets them; and that 'Once enabled, it cannot be disabled except by contacting the Account Manager', of the markets feature itself, (e)'s question (RD2), not a setting of one of rule 1's kinds
- Earlier leads stay as earlier parts placed them: S02-SA-382 in S02-V-708, S02-V-709 and S02-V-712 (RD3-S6); S02-SA-437 and S02-SA-443 in S02-V-716 and S02-V-717, and S02-SA-439 in S02-V-699 and S02-V-701 (RD3-S9).

### Revisit S02-V-1094 (salla, S02-VP-86, apps): was `gap` (S02-SA-G15)
- Left `gap` S02-SA-G15, which why names, with a row note. No lead gives an answer to S02-VP-86; absence S02-SA-N03 stays cited in S02-V-1093 (the whole store), as RD3-S9 placed it.
- New leads S02-SA-513 and S02-SA-514 are the App Store's filter of all apps, the same labels on two stores; noted:
- S02-SA-513 (f): the App Store's filter of all apps ('Filter Categories Delivery service type Shipping zone Support change company name Company type Price Rating Salla Apps Reset'), on the merchant store (store-1-da, Basic): filters of the apps the App Store lists, not a setting of the store; names no value of the store's apps, what one is taken per, or who sets it
- S02-SA-514 (f): the same filter, on the new UAE store (store 21123834, Basic): as S02-SA-513
- Earlier leads stay as earlier parts placed or noted them: S02-SA-409 to S02-SA-411 noted (RD3-S6); S02-SA-413 to S02-SA-415 in S02-V-874, S02-V-1095, S02-V-746 and S02-V-1110.

### Revisit S02-V-1096 (salla, S02-VP-87, analytics and tracking): was `gap` (S02-SA-G08)
- Left `gap` S02-SA-G08, which why names, with a row note. No lead gives an answer to S02-VP-87.
- New leads S02-SA-530, S02-SA-532 and S02-SA-533 (the public demo's first market) name no analytics or tracking setting; they are placed or noted with the revisit of S02-V-1092, above.
- Earlier lead S02-SA-442 stays in S02-V-878 (the whole store), as RD3-S9 placed it.

### Revisit S02-V-1097 (salla, S02-VP-89, notifications to the merchant): was `gap` (S02-SA-G14)
- Left `gap` S02-SA-G14, which why names, with a row note. No lead gives an answer to S02-VP-89; absence S02-SA-N02 stays cited in S02-V-886 (the whole store), as RD3-S9 placed it.
- New leads S02-SA-530, S02-SA-532 and S02-SA-533 name no notification to the merchant or staff; they are placed or noted with the revisit of S02-V-1092, above.
- Earlier leads stay as RD3-S9 placed them: S02-SA-438 in S02-V-886 and S02-V-890; S02-SA-439 (guest checkout's) in S02-V-699 and S02-V-701.

### Revisit S02-V-731 (salla, S02-VP-76, the store's address): was `gap` (S02-SA-G12)
- Left `gap` S02-SA-G12, which why names, with a row note. No lead gives an answer to S02-VP-76.
- New leads S02-SA-536 and S02-SA-537 are the markets module's translations of its section 'contacts' (English and Arabic: 'Contact information', 'Customer support channels', 'Social media accounts'; 'معلومات التواصل', 'قنوات خدمة العملاء', 'حسابات التواصل الاجتماعي'). They name contact information shown to buyers, not the store's address, so they joined S02-V-720 (S02-VP-68, a market the store sells into): a reading from their identifier (ui-merchant-localization) and scope ('every store's dashboard: the markets module'), rule 5, beside S02-SA-028 and S02-SA-038, which name 'معلومات التواصل' among each market's sections. They name no one who sets it, so they are not under S02-VP-79.
- Earlier leads S02-SA-421 and S02-SA-425 stay in S02-V-734 (S02-VP-78, locations), as RD3-S6 placed them.

### Revisit S02-V-869 (salla, S02-VP-85, the store's country): was `gap` (S02-SA-G11)
- Left `gap` S02-SA-G11, which why names, with a row note. No lead gives an answer to S02-VP-85.
- New leads S02-SA-530 and S02-SA-533 name the countries of the market being created ('Countries Saudi Arabia' in the form; the key 'countries' in the request): the countries that define the market, (e)'s question (RD2), not a country the market or its storefront holds as the store's own, which S02-VP-85 asks. S02-SA-532 names no country. All three are placed or noted with the revisit of S02-V-1092, above.
- Earlier leads stay as earlier parts placed or noted them: S02-SA-426 to S02-SA-430 noted (RD3-S6); S02-SA-440 in S02-V-676 and S02-V-680.

### `place` tasks (A2-SA-R)
- S02-SA-527 (f): the public demo's Multi Market page, before a market exists ('Expand into new markets Sell across countries and markets while delivering a localized shopping experience from one store.'): names no setting of the store, only 'a localized shopping experience', and nothing a value is taken per or who sets it; its markets are (e)'s, RD2's
- S02-SA-528: joined S02-V-688 (S02-VP-49, a market: 'Set market-specific pricing Adjust product prices to match each market and currency.') and S02-V-689 (S02-VP-50, the seller: the page's instruction to the merchant). Its 'independent settings for each market' names a market's settings in general, of no one kind of setting, as the same words in S02-SA-065 were noted in the first pass. Its currency is what prices are adjusted to, not a setting it says takes a value per market, so it joins no row of S02-VP-41.
- S02-SA-529: joined S02-V-696 (S02-VP-53, a market: 'Customize each market Tailor your store’s design and content') and S02-V-697 (S02-VP-54, the seller); S02-V-699 (S02-VP-55, a market: 'Choose the sign-in methods available to customers in each market.') and S02-V-701 (S02-VP-56, the seller); S02-V-684 (S02-VP-47, a market: 'Control which products are available in each market') and S02-V-686 (S02-VP-48, the seller). Each who-sets row rests on the page's instruction to the merchant in the store's admin, as S02-SA-078 to S02-SA-083 rest on the same module's.
- S02-SA-535: joined S02-V-719 (S02-VP-67, the buyer's country or location, a reading: 'Personalize your customers' shopping experience using the nearest branch or warehouse.', 'nearest' read as nearest the customers it names, as S02-SA-034's 'الأقرب للعميل') and S02-V-734 (S02-VP-78, the seller: the page's instruction to the merchant). Its scope is the demo store store-markets (Pro).
- The rows joined keep their bases: `answers` holds for each statement joined, by its own words or, for S02-SA-533, S02-SA-536 and S02-SA-537, its identifier and scope (rule 5); `term` stays as earlier parts found it.

### Candidates for a new point
- None. The statements this part noted name no setting of the store (S02-SA-513, S02-SA-514, S02-SA-527), or a setting of one of rule 1's kinds without an answer (S02-SA-532's inventory deduction, locations), or the markets feature itself, which (e) asks about (S02-SA-532). S02-SA-528's 'independent settings for each market' names a market's settings in general, of no one kind, as in S02-SA-065.

### Words searched for
- None: the second pass raises no point, so rule 3's search for earlier platforms' rows doesn't arise.

### Calls this part made, and problems with the brief, the work list or the tools
- No lead gives an answer to its revisited point, so each of the six `gap` rows stays as it was, with the one gap its why names, and a row note (`rownote`) records the revisit. A `replace` would have written the same row and dropped the note an earlier part left on it.
- Of the 31 statements, 20 are earlier leads, which stay as RD3-S6, RD3-S8 and RD3-S9 placed or noted them; 11 are new: seven leads (S02-SA-513, S02-SA-514, S02-SA-530, S02-SA-532, S02-SA-533, S02-SA-536, S02-SA-537) and the four place tasks.
- A lead that answers another point of (f) is placed there, and its not answering the revisited point is recorded under the revisit, not as a note, since a note in rule 2's form says a statement answers none of the bullet's questions.
- S02-SA-533, a request the admin sent, joined only the rows of what a value is taken per: its keys name no party, as RD3-S12 did for S02-ZD-488. S02-SA-530, the form that sent it, gives the seller by its controls 'Customize'.
- The Multi Market page's feature texts (S02-SA-528, S02-SA-529, S02-SA-535) are instructions to the merchant in the store's admin, so the seller, as the same module's S02-SA-078 to S02-SA-083 were placed.
- S02-SA-535 joined S02-V-719, whose basis_evidence reads the branch or warehouse nearest the customer as `the buyer's country` ('the buyer's country or location'), as an earlier part placed S02-SA-034. Nearness is a location, not a country; the row's phrase is that part's call, kept.
- S02-SA-532 is noted, though A2-SA-R gave it as a lead of S02-VP-67: its words say activating markets affects how inventory is deducted 'in your store', not what it is taken per.

### After the check (RD3-S13)
- `check_subject.py` on a copy holding only b/RD3: no `error` lines; 17 warnings (Shopify's and WooCommerce's quote lengths) and 14 reviews (quotes found only in a page's source, the coordinator's, and RD1's and RD2's statements, whose folders the copy leaves out). RD3's rows in `unplaced.tsv`: none.
- `second_pass_list.py --check`: RD3's list holds no revisit, reread or note task without a row in done.tsv.

## Second pass, RD3-S14: bigcommerce and woocommerce, bullets f and g, the BigCommerce and WooCommerce round's tasks

From A2-BC-R, which read the founder's local agent's captures of the free trial store w5pamplexj (other-product-class at 3f2438f3, folder `bigcommerce/`), and A2-WC-R, which read those of the test store (folder `woocommerce/`): two revisits of BigCommerce's `gap` rows whose gap S02-BC-G14 was narrowed into S02-BC-G18 (S02-V-843, S02-V-961), and nine place tasks (S02-BC-368 to S02-BC-371, S02-BC-375 to S02-BC-378, S02-WC-524). All eleven are under (f); none is under (g). Each new statement's scope (the store, its plan or versions, the run and step) is kept in the rows it joined, which take their scope again from all their statements (rule 6).

### Revisit S02-V-843 (bigcommerce, S02-VP-64, who sells to the buyer: who sets it): was `gap` (S02-BC-G14)
- Replaced by `gap` S02-BC-G18, the one gap why names, which says it is 'in place of S02-BC-G14'. The row's earlier note is kept, and the revisit added to it.
- No lead names a business entity or a merchant of record per storefront or market, or who sets one. Each lead is placed under another point of (f), or noted:
  - Lead S02-BC-351 stays in S02-V-842 (S02-VP-63), as the first pass placed it: it names the merchant as merchant of record in agentic checkout, not who sets it.
  - Lead S02-BC-372, Avalara AvaTax's cross-border collection ('you must specify which countries you'll be collecting VAT/GST from, whether they have a permanent establishment, and whether they are the Importer of Record'): joined S02-V-832 (S02-VP-57, the buyer's country, a reading: the country a transaction goes into), S02-V-834 (S02-VP-58, the seller: 'you must specify') and S02-V-980 (S02-VP-58, a third party: 'Avalara AvaTax will calculate VAT/GST'). The Importer of Record it names is, in S02-BC-373's definition, the party responsible for an import's documents and customs duties: taxes and duties, not who sells to the buyer. The words differ from 'merchant of record' and 'business entity', and no translation makes them the same (rule 0).
  - Leads S02-BC-382, S02-BC-383 and S02-BC-384, Multi-Storefront Payment Methods (a payment provider set up several times with different merchant accounts, currencies and settings, each configuration assigned to its channels): joined S02-V-840 (S02-VP-61, a market the store sells into: the channels the configurations are assigned to, read as one list, rule 5) and S02-V-841 (S02-VP-62, the seller). A merchant account is the merchant's account with a payment provider, not a business entity or a merchant of record (rule 0), as S02-BC-G18 reads the same three statements.
- S02-BC-373 (f): defines the Importer of Record ('a person or entity who assumes the responsibility for ensuring goods imported to a particular country are appropriately documented and valued', 'the responsible party for the payment of customs duties, tariffs, and fees related to the imported goods'); names no setting of the store, what one takes its value per, or who sets one; the setting, whether the merchant is the Importer of Record for a country, is S02-BC-372's, placed under S02-VP-57 and S02-VP-58

### Revisit S02-V-961 (bigcommerce, S02-VP-63, who sells to the buyer: what it takes its value per): was `gap` (S02-BC-G14)
- Replaced by `gap` S02-BC-G18, the one gap why names, beside S02-V-842 (the whole store, a reading, S02-BC-351). S02-BC-G18 asks whether a storefront can sell to its buyers through another business or legal entity, or a merchant of record: an answer S02-V-842 doesn't give, so the gap row stands beside it (rule 4).
- The leads are the same six as S02-V-843's, placed or noted as written there. S02-BC-351's answer is the one S02-V-842 holds; none of the other five answers S02-VP-63.

### `place` tasks (A2-BC-R and A2-WC-R)
- S02-BC-368, Basic Tax on store w5pamplexj ('Configure your own tax classes, rates and zones. Basic tax will be used if your tax service is not targeted to a given country/subdivision, or is unavailable during a purchase.'): joined S02-V-832 (S02-VP-57, the buyer's country, a reading: the country or subdivision of a purchase), S02-V-834 (S02-VP-58, the seller: 'Configure your own') and S02-V-980 (S02-VP-58, a third party, a reading: the store's tax service gives the tax where it is targeted, as S02-BC-246's Provider Targeting says).
- S02-BC-369, the page Settings › Tax › Add tax service (the same at the four default countries saved): joined S02-V-834 (S02-VP-58, the seller), by its identifier, a control in the store's admin from which a tax service is added (rules 4 and 5). Its statement is the heading 'All tax services'. That the services listed are the same whatever the default country is (c)'s question, RD1's. No row of S02-VP-57 takes it, since it names no value of a tax setting that differs by a market or a buyer's country.
- S02-BC-370, 'Tax calculation [By destination address]' (Settings › Tax › Store tax settings, store w5pamplexj): joined S02-V-832 (S02-VP-57, the buyer's country, a reading of the destination address as the buyer's) and S02-V-834 (S02-VP-58, the seller: a control in the store's admin, rule 4).
- S02-BC-371, the Default Zone: joined S02-V-832 (S02-VP-57, the buyer's country: the rate differs by the region a tax zone covers) and S02-V-834 (S02-VP-58, the seller: 'Do not set up tax rates in this zone', 'you will want to keep this as'). Added S02-V-1128 (S02-VP-58, the platform, a reading): 'All stores contain a Default Zone, which applies a 0% tax rate to any regions not set up in another zone'. The statement names no party that sets the zone or its rate, and rule 4 reads a value set by default as the platform's.
- S02-BC-375, '1,234.00 KGS/Centimeters', the store's physical dimensions as made, with the control 'Set standard formats for Oman' (default country Oman as made): joined S02-V-983 (S02-VP-77, the store's own country, a reading, as the row's) and S02-V-1106 (S02-VP-91, the seller: the fields and the control in Settings › Localization, rule 4, by its identifier). Its scope's 'the values as the store was made' is not read as the platform setting them: neither the statement nor its scope names who set them.
- S02-BC-376 and S02-BC-377, the standard formats the control 'Set standard formats for <country>' gives for Oman (KGS, Centimeters, 'jS M Y') and for the United States (Ounces, Inches, 'M jS Y'): joined S02-V-983 (S02-VP-77, the store's own country, a reading: the standard formats differ by country, and the control takes the store's default country). They are under no who-sets point. Their statements are the formats themselves, and they name no party. The control that applies them gives the seller under S02-VP-91, through S02-BC-375 and S02-BC-285.
- S02-BC-378, 'Localization updated', the default country saved as United States (then Oman, United Kingdom and Saudi Arabia): joined S02-V-984 (S02-VP-77, the whole store, a reading), by its scope (rule 5): 'Physical dimensions still 1,234.00 KGS/Centimeters, Date and timezone still 24th Jul 2020 @ 3:49 AM, (GMT +00:00)'. The store's one value stayed as it was when its own country changed. It joins no row of S02-VP-85: the save names the store's default country, not what that country takes its value per.
- S02-WC-524, 'Currency [United States (US) dollar ($) — USD]' after the store's Country / State was changed to Saudi Arabia (the test store: WordPress 7.1.4, WooCommerce 11.2.1, WooPayments 11.2.0, WooCommerce Tax 3.7.3): joined S02-V-893 (S02-VP-41, the whole store, a reading: the store's one currency, which a change of its country left as it was) and S02-V-896 (S02-VP-42, the seller: the control Settings > General > Currency options > Currency, rule 4, by its identifier). S02-V-895 (S02-VP-41, the store's own country: the onboarding code that sets the currency from the store's location) stays as it was. It rests on the release's onboarding code, and this observation is of the settings page.
- The rows joined keep their bases. `answers` holds for each statement joined, by its own words, or by its identifier or scope (rule 5): for S02-BC-369, S02-BC-375, S02-BC-376, S02-BC-377, S02-BC-378 and S02-WC-524. `term` stays as earlier parts found it.

### x_words added
- S02-VP-57, bigcommerce: Basic tax; tax service; Tax calculation; Default Zone; VAT/GST. S02-VP-58, bigcommerce: tax classes, rates and zones; tax service; Tax calculation; Default Zone. S02-VP-61 and S02-VP-62, bigcommerce: payment configurations.

### Candidates for a new point
- None. Each statement placed fits a point's kind: taxes and duties, payment methods, units and time zone, currency. The one noted, S02-BC-373, defines a role, the Importer of Record, of the taxes and duties kind, and is noted because it answers no question, not for want of a kind.

### Words searched for
- None: the second pass raises no point, so rule 3's search for earlier platforms' rows doesn't arise.

### Calls this part made, and problems with the brief, the work list or the tools
- The message names bullets f and g, but all eleven tasks are under (f), and none of the fifteen statements the tasks name carries (g).
- Both revisited rows keep `gap`, now S02-BC-G18 in place of S02-BC-G14, written with `replace`, since the gap changed. S02-V-843's earlier note is passed again with the replace, which would otherwise drop it.
- A lead that answers another point of (f) is placed there, and its not answering the revisited point is recorded under the revisit, not as a note (as RD3-S13 did).
- S02-BC-382 and S02-BC-383 name currencies, those a payment configuration is set up with. They join no row of S02-VP-41 or S02-VP-42: neither says that the currency a buyer sees or pays in takes its value per channel, and a payment configuration is of the payment methods kind.
- S02-BC-372's countries ('transactions into European Union member states or any other country') are read as the buyer's country, not a market the store sells into. BigCommerce's market is a channel (S02-V-809, S02-V-840), and these countries are not channels.
- S02-V-1128, the platform under S02-VP-58, rests on reading 'All stores contain a Default Zone' as a value set by default (rule 4). S02-BC-378's join to S02-V-984 rests on reading an unchanged value as one value for the whole store. Both are marked as readings in their rows.

### After the check (RD3-S14)
- `merge_slices.py` on a copy holding only b/RD3: 52 variation points, 523 variants, no refusal.
- `check_subject.py` on that copy: no `error` lines; 17 warnings (Shopify's and WooCommerce's citations) and 14 reviews (12 quotes found only in a page's source, the coordinator's; and RD1's and RD2's statements, whose folders the copy leaves out). RD3's rows in `unplaced.tsv`: none. The lines there that carry this part's statements are RD1's, under (a), (b) and (c).
- `second_pass_list.py --check`: RD3's list holds no revisit, reread or note task without a row in done.tsv. RD1's seven are RD1-S9's, running beside this part.

