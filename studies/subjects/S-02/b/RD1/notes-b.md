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
