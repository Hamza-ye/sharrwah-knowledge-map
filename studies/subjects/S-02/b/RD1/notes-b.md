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
