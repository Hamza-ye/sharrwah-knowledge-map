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
